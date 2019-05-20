import unittest
import StringIO
from parseAttacks import *


class TestParseAttackMethods(unittest.TestCase):
    def test_combine_2_wait_frames(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6)]
        self.assertItemsEqual(result, expected)

    def test_combine_2_active_frames(self):
        chunks = [AttackFrameChunk(2), AttackFrameChunk(2, is_new_hit=False)]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(4)]
        self.assertItemsEqual(result, expected)

    def test_dont_combine_2_active_frames(self):
        chunks = [AttackFrameChunk(2, is_new_hit=True), AttackFrameChunk(2, is_new_hit=True)]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(2), AttackFrameChunk(2)]
        self.assertItemsEqual(result, expected)

    def test_combine_2_wait_frames_with_active_after(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4), AttackFrameChunk(1), WaitFrameChunk(2)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6), AttackFrameChunk(1), WaitFrameChunk(2)]
        self.assertItemsEqual(result, expected)

    def test_get_duration(self):
        self.assertEqual(15, get_duration("    sprite('null', 15)"))

    def test_simulate_hit_basic_normal(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 4, 4), WaitFrameChunk(12),
                  AttackFrameChunk(1, 4, 4), WaitFrameChunk(12)]
        move = Move()
        move.frame_chunks = chunks
        # no effects to combine, just expect teh same chunks back
        result = combine_with_effects_on_block(move, {})
        self.assertEqual(0, len(result.additional_chunks))
        self.assertItemsEqual(move.frame_chunks, chunks)

    def test_simulate_hit_projectile(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("Shot"), WaitFrameChunk(12)]
        shot = Move()
        shot.frame_chunks = [WaitFrameChunk(4), AttackFrameChunk(2)]
        effect_list = {"Shot": shot}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual(result.frame_chunks, [WaitFrameChunk(16)])
        # basically increasing the startup of hte shot by 4
        self.assertItemsEqual(result.additional_chunks[0], [WaitFrameChunk(8), AttackFrameChunk(2)])

    def test_simulate_hit_use_subroutine(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("InitValues"), AttackFrameChunk(1, 10, 11, 12), WaitFrameChunk(4)]
        init = Subroutine()
        init.hitstop = 1
        init.blockstun = 2
        init.additionalHitstopOpponent = 3
        init.landingRecovery = 4
        effect_list = {"InitValues": init}
        move = Move()
        move.frame_chunks = chunks
        move.landing_recovery = 100
        result = combine_with_effects_on_block(move, effect_list)
        # expect hitstop, blockstun, landing recovery etc to be replaced by values from InitValues
        self.assertEqual(0, len(result.additional_chunks))
        expected_frame_chunks = [WaitFrameChunk(4),
                                 AttackFrameChunk(1, init.blockstun, init.hitstop, init.additionalHitstopOpponent),
                                 WaitFrameChunk(4)]
        self.assertItemsEqual(result.frame_chunks, expected_frame_chunks)
        self.assertEqual(init.landingRecovery, result.landing_recovery)

    def test_simulate_projectile_using_subroutine(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("Shot"), WaitFrameChunk(12)]
        shot = Move()
        shot.frame_chunks = [SubroutineCall("ShotInit"), WaitFrameChunk(4), AttackFrameChunk(2)]
        shot_init = Subroutine()
        shot_init.hitstop = 1
        shot_init.blockstun = 2
        shot_init.additionalHitstopOpponent = 3
        effect_list = {"Shot": shot,
                       "ShotInit": shot_init}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual(result.frame_chunks, [WaitFrameChunk(16)])
        # basically increasing the startup of hte shot by 4
        expected_frame_chunks = [WaitFrameChunk(8),
                                 AttackFrameChunk(2,
                                                  shot_init.blockstun,
                                                  shot_init.hitstop,
                                                  shot_init.additionalHitstopOpponent
                                                  )
                                 ]
        self.assertItemsEqual(result.additional_chunks[0], expected_frame_chunks)

    def test_calculate_frame_adv_1_hit(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 3, 3), WaitFrameChunk(12)]
        result = calc_frame_adv_for_subroutine(chunks)
        self.assertItemsEqual(result, (5, '1', '12', 17, 20, 11))

    def test_calculate_frame_adv_2_hit(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(3, 3, 3), AttackFrameChunk(3, 3, 3), WaitFrameChunk(12)]
        result = calc_frame_adv_for_subroutine(chunks)
        self.assertItemsEqual(result, (5, '3,3', '12', 22, 28, 17))

    def test_calculate_frame_adv_2_hit_with_gap(self):
        chunks = [WaitFrameChunk(4),
                  AttackFrameChunk(1, 3, 3),
                  WaitFrameChunk(3),
                  AttackFrameChunk(1, 3, 3),
                  WaitFrameChunk(12)
                  ]
        result = calc_frame_adv_for_subroutine(chunks)
        self.assertItemsEqual(result, (5, '1(3)1', '12', 21, 27, 18))

    def test_calculate_frame_adv_with_5_active_frames(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(5, 3, 3), WaitFrameChunk(12)]
        result = calc_frame_adv_for_subroutine(chunks)
        self.assertItemsEqual(result, (5, '5', '12', 21, 24, 11))

    def test_calculate_frame_adv_1_hit_bonus_hitstop(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 3, 3, 10), WaitFrameChunk(12)]
        result = calc_frame_adv_for_subroutine(chunks)
        self.assertItemsEqual(result, (5, '1', '12', 17, 20, 21))

    def test_parse_subroutine(self):
        subroutine = """@Subroutine
def Monsho_AtkData():
    AttackLevel_(1)
    AttackP1(70)
    AttackP2(90)
    Hitstop(6)
    Unknown9154(17)
    AirUntechableTime(21)
    Unknown11028(11)
    Unknown9016(1)"""
        buf = StringIO.StringIO(subroutine)
        effect_list = {}
        effect_list = parse_move_file(buf, effect_list, effect_list)
        subroutine = Subroutine()
        subroutine.hitstop = 6
        subroutine.blockstun = 11
        self.assertEquals(effect_list["Monsho_AtkData"], subroutine)

    def test_parse_attack_with_subroutine(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(10000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitJumpCancel(1)
        Unknown1112('')
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    sprite('es201_04', 5)	# 8-12	 **attackbox here**
    GFX_0('esef_201', -1)
    sprite('es201_05', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 16-18
    sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        move = Move()
        move.frame_chunks = [WaitFrameChunk(7),
                             SubroutineCall("esef_201"),
                             AttackFrameChunk(5, 16, 11),
                             WaitFrameChunk(9)
                             ]
        self.assertEqual(move_list["NmlAtk5X"], move)

    def test_parse_attack_with_custom_blockstun_hitstop(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11028(10)
        Hitstop(10)
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    sprite('es201_04', 5)	# 8-12	 **attackbox here**
    sprite('es201_05', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 16-18
    sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        move = Move()
        move.frame_chunks = [WaitFrameChunk(7),
                             AttackFrameChunk(5, 10, 10),
                             WaitFrameChunk(9)
                             ]
        self.assertEqual(move_list["NmlAtk5X"], move)

    def test_parse_attack_with_refreshMultihit(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    sprite('es201_04', 2)	# 8-9	 **attackbox here**
    sprite('es201_04', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('es201_05', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 16-18
    sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        move = Move()
        move.frame_chunks = [WaitFrameChunk(7),
                             AttackFrameChunk(2, 16, 11),
                             AttackFrameChunk(3, 16, 11),
                             WaitFrameChunk(9)
                             ]
        self.assertEqual(move_list["NmlAtk5X"], move)

    def test_parse_attack_with_no_refreshMultihit(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    sprite('es201_04', 2)	# 8-9	 **attackbox here**
    sprite('es201_04', 3)	# 10-12	 **attackbox here**
    sprite('es201_05', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 16-18
    sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        move = Move()
        move.frame_chunks = [WaitFrameChunk(7),
                             AttackFrameChunk(5, 16, 11),
                             WaitFrameChunk(9)
                             ]
        self.assertEqual(move_list["NmlAtk5X"], move)

