import unittest
import StringIO
from parseAttacks import *


class TestParseAttackMethods(unittest.TestCase):
    def test_combine_2_wait_frames(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6)]
        self.assertItemsEqual(expected, result)

    def test_combine_2_active_frames(self):
        chunks = [AttackFrameChunk(2), AttackFrameChunk(2, is_new_hit=False)]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(4)]
        self.assertItemsEqual(expected, result)

    def test_dont_combine_2_active_frames(self):
        chunks = [AttackFrameChunk(2, is_new_hit=True), AttackFrameChunk(2, is_new_hit=True)]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(2), AttackFrameChunk(2)]
        self.assertItemsEqual(expected, result)

    def test_combine_2_wait_frames_with_active_after(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4), AttackFrameChunk(1), WaitFrameChunk(2)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6), AttackFrameChunk(1), WaitFrameChunk(2)]
        self.assertItemsEqual(expected, result)

    def test_do_not_combine_wait_frames_with_inv(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4)]
        chunks[0].inv_type = 0
        chunks[1].inv_type = 1
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(expected, result)

    def test_do_not_combine_wait_frames_with_diff_inv(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(2)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(result, expected)

    def test_do_combine_wait_frames_with_diff_inv(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(2)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks, True)
        expected = [WaitFrameChunk(4)]
        self.assertEqual(len(expected), len(result))
        self.assertEqual(expected[0].duration, result[0].duration)  # inv for this combined chunk is undefined behavior

    def test_do_not_combine_active_frame_types_with_same_inv(self):
        chunks = [AttackFrameChunk(2, is_new_hit=True), AttackFrameChunk(2, is_new_hit=True)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [True, False, False, False, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(result, expected)

    def test_combine_active_frame_types_with_same_inv(self):
        chunks = [AttackFrameChunk(2, is_new_hit=True), AttackFrameChunk(2, is_new_hit=False)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, False, False, False, True]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [False, False, False, False, True]
        result = consolidate_frame_chunks(chunks)
        expected = [AttackFrameChunk(4)]
        expected[0].inv_type = 1
        expected[0].inv_attr = [False, False, False, False, True]
        self.assertItemsEqual(result, expected)

    def test_combine_same_frame_types_with_same_inv(self):
        chunks = [WaitFrameChunk(2), WaitFrameChunk(4)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [False, True, True, True, False]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrameChunk(6)]
        expected[0].inv_type = 1
        expected[0].inv_attr = [False, True, True, True, False]
        self.assertItemsEqual(result, expected)

    def test_get_duration(self):
        self.assertEqual(15, get_duration("    sprite('null', 15)"))

    def test_simulate_hit_basic_normal(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 4, 4), WaitFrameChunk(12),
                  AttackFrameChunk(1, 4, 4), WaitFrameChunk(12)]
        expected = Move()
        expected.frame_chunks = chunks
        # no effects to combine, just expect teh same chunks back
        result = combine_with_effects_on_block(expected, {})
        self.assertEqual(0, len(result.additional_chunks))
        self.assertItemsEqual(expected.frame_chunks, chunks)

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
        self.assertItemsEqual([WaitFrameChunk(16)], result.frame_chunks)
        # basically increasing the startup of hte shot by 4
        self.assertItemsEqual([WaitFrameChunk(8), AttackFrameChunk(2)], result.additional_chunks[0])

    def test_simulate_hit_use_subroutine(self):
        chunks = [WaitFrameChunk(4), SubroutineCall("InitValues"), AttackFrameChunk(1, 10, 11, 12), WaitFrameChunk(4)]
        init = Subroutine()
        init.hitstop = 1
        init.blockstun = 2
        init.additionalHitstopOpponent = 3
        init.landingRecovery = 4
        init.damage = 500
        init.p1 = 50
        init.p2 = 60
        init.minDamage = 15
        effect_list = {"InitValues": init}
        move = Move()
        move.frame_chunks = chunks
        move.landing_recovery = 4
        result = combine_with_effects_on_block(move, effect_list)
        # expect hitstop, blockstun, landing recovery etc to be replaced by values from InitValues
        self.assertEqual(0, len(result.additional_chunks))
        expected_frame_chunks = [WaitFrameChunk(4),
                                 AttackFrameChunk(1, init.blockstun, init.hitstop, init.additionalHitstopOpponent),
                                 WaitFrameChunk(4)]
        expected_frame_chunks[1].damage = Damage(500, 50, 60, 15)
        self.assertItemsEqual(expected_frame_chunks, result.frame_chunks)
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

    def test_parse_inv_attr_str1(self):
        values = parse_attributes("0000000000000000010000000000000001000000")
        self.assertEqual([False, False, True, False, True], values)

    def test_parse_inv_attr_str2(self):
        values = parse_attributes("0100000001000000000000000100000000000000")
        self.assertEqual([True, True, False, True, False], values)

    def test_calculate_frame_adv_1_hit(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 3, 3), WaitFrameChunk(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '1', '12', 17, 20, 11, []), result)

    def test_calculate_frame_adv_2_hit(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(3, 3, 3), AttackFrameChunk(3, 3, 3), WaitFrameChunk(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '3,3', '12', 22, 28, 17, []), result)

    def test_calculate_frame_adv_2_hit_with_gap(self):
        chunks = [WaitFrameChunk(4),
                  AttackFrameChunk(1, 3, 3),
                  WaitFrameChunk(3),
                  AttackFrameChunk(1, 3, 3),
                  WaitFrameChunk(12)
                  ]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '1(3)1', '12', 21, 27, 18, []), result)

    def test_calculate_frame_adv_with_5_active_frames(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(5, 3, 3), WaitFrameChunk(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '5', '12', 21, 24, 11, []), result)

    def test_calculate_frame_adv_1_hit_bonus_hitstop(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(1, 3, 3, 10), WaitFrameChunk(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '1', '12', 17, 20, 21, []), result)

    def test_calculate_frame_adv_attr_inv(self):
        chunks = [WaitFrameChunk(4), AttackFrameChunk(3, 3, 3), WaitFrameChunk(12)]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, True, False, False, False]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '3', '12', 19, 22, 11, [[5, 3, 1, [True, True, False, False, False]]]), result)

    def test_calculate_startup_with_superflash(self):
        chunks = [WaitFrameChunk(4),
                  AttackFrameChunk(1, 3, 3),
                  WaitFrameChunk(3),
                  AttackFrameChunk(1, 3, 3),
                  WaitFrameChunk(12)
                  ]
        result = calc_frames_for_subroutine(chunks, 2, 3)
        self.assertItemsEqual(('2+3Flash+0', '1(3)1', '12', 21, 27, 18, []), result)

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
    Damage(900)
    Unknown9016(1)"""
        buf = StringIO.StringIO(subroutine)
        effect_list = {}
        effect_list = parse_move_file(buf, effect_list, effect_list)
        subroutine = Subroutine()
        subroutine.hitstop = 6
        subroutine.blockstun = 11
        subroutine.damage = 900
        subroutine.p1 = 70
        subroutine.p2 = 90
        self.assertEquals(effect_list["Monsho_AtkData"], subroutine)

    def test_parse_attack_with_subroutine(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
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
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 SubroutineCall("esef_201"),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

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
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 10, 10),
                                 WaitFrameChunk(9)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

    def test_parse_attack_with_refreshMultihit(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
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
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(2, 0, 0),
                                 AttackFrameChunk(3, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

    def test_parse_attack_with_no_refreshMultihit(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
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
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

    def test_early_exitState(self):
        state = """@State
    def NmlAtk5X():

        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
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
        sprite('es201_05', 3)	# 13-15
        Recovery()
        Unknown2063()
        sprite('es201_06', 3)	# 16-18
        ExitState()
        sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(6)
                                 ]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_early_exitState_and_second_move(self):
        state = """@State
    def NmlAtk5X():

        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
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
        sprite('es201_05', 3)	# 13-15
        Recovery()
        Unknown2063()
        sprite('es201_06', 3)	# 16-18
        ExitState()
        sprite('es201_07', 3)	# 19-21
        
    @State
    def NmlAtk6X():

        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
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
        sprite('es201_05', 3)	# 13-15
        Recovery()
        Unknown2063()
        sprite('es201_06', 3)	# 16-18
        sprite('es201_07', 3)	# 19-21
        """
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 2)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(6)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

        self.assertTrue("NmlAtk6X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        self.assertEqual(expected, move_list["NmlAtk6X"])

    def test_attribute_invul(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AirPushbackY(10000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitJumpCancel(1)
        Unknown1112('')
        Unknown11058('0000000001000000000000000000000000000000')
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('es201_04', 5)	# 8-12	 **attackbox here**
    sprite('es201_05', 3)	# 13-15
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 16-18
    sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(5),
                                 WaitFrameChunk(2),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        expected.frame_chunks[1].inv_type = 1
        expected.frame_chunks[1].inv_attr = [True, False, False, False, False]
        expected.frame_chunks[2].inv_type = 1
        expected.frame_chunks[2].inv_attr = [True, False, False, False, False]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_attribute_inv(self):
        state = """@State
 def NmlAtk5X():

     def upon_IMMEDIATE():
         AttackDefaults_StandingNormal()
         AirPushbackY(10000)
         Unknown9016(1)
         HitOrBlockCancel('NmlAtk2A')
         HitOrBlockCancel('NmlAtk5B')
         HitOrBlockCancel('NmlAtk2B')
         HitJumpCancel(1)
         Unknown1112('')
         Unknown11058('0000000001000000000000000000000000000000')
     sprite('es201_00', 1)	# 1-1
     sprite('es201_01', 2)	# 2-3
     sprite('es201_02', 2)	# 4-5
     SFX_0('006_swing_blade_0')
     sprite('es201_03', 2)	# 6-7
     Unknown7009(1)
     setInvincible(1)
     Unknown22019('0100000000000000000000000000000000000000')
     sprite('es201_04', 5)	# 8-12	 **attackbox here**
     sprite('es201_05', 3)	# 13-15
     setInvincible(0)
     Recovery()
     Unknown2063()
     sprite('es201_06', 3)	# 16-18
     sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(5),
                                 WaitFrameChunk(2),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        expected.frame_chunks[1].inv_type = 1
        expected.frame_chunks[1].inv_attr = [True, False, False, False, False]
        expected.frame_chunks[2].inv_type = 1
        expected.frame_chunks[2].inv_attr = [True, False, False, False, False]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_attribute_inv_with_gfx_in_between(self):
        state = """@State
    def NmlAtk5X():

        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
            AirPushbackY(10000)
            Unknown9016(1)
            HitOrBlockCancel('NmlAtk2A')
            HitOrBlockCancel('NmlAtk5B')
            HitOrBlockCancel('NmlAtk2B')
            HitJumpCancel(1)
            Unknown1112('')
            Unknown11058('0000000001000000000000000000000000000000')
        sprite('es201_00', 1)	# 1-1
        sprite('es201_01', 2)	# 2-3
        sprite('es201_02', 2)	# 4-5
        SFX_0('006_swing_blade_0')
        sprite('es201_03', 2)	# 6-7
        Unknown7009(1)
        setInvincible(1)
        Unknown22019('0100000000000000000000000000000000000000')
        GFX_0('esef_aaaa', -1)
        sprite('es201_04', 5)	# 8-12	 **attackbox here**
        sprite('es201_05', 3)	# 13-15
        setInvincible(0)
        Recovery()
        Unknown2063()
        sprite('es201_06', 3)	# 16-18
        sprite('es201_07', 3)	# 19-21"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(5),
                                 SubroutineCall("esef_aaaa"),
                                 WaitFrameChunk(2),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        expected.frame_chunks[2].inv_type = 1
        expected.frame_chunks[2].inv_attr = [True, False, False, False, False]
        expected.frame_chunks[3].inv_type = 1
        expected.frame_chunks[3].inv_attr = [True, False, False, False, False]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_move_with_superflash(self):
        state = """@State
    def NmlAtk5X():
    
    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AirPushbackY(10000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitJumpCancel(1)
        Unknown1112('')
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    Unknown2036(2, -1, 0)
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    Unknown7009(1)
    Unknown22019('0100000000000000000000000000000000000000')
    GFX_0('esef_aaaa', -1)
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
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(5),
                                 SubroutineCall("esef_aaaa"),
                                 WaitFrameChunk(2),
                                 AttackFrameChunk(5, 0, 0),
                                 WaitFrameChunk(9)
                                 ]
        expected.superflash_start = 2
        expected.superflash_duration = 2
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_parse_damage(self):
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
        Damage(500)
        HitJumpCancel(1)
        Unknown1112('')
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    sprite('es201_04', 5)	# 8-12	 **attackbox here**
    sprite('es201_05', 3)	# 13-15
    sprite('es201_04', 5)	# 16-20	 **attackbox here**
    Damage(1000)
    sprite('es201_05', 3)	# 21-23
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 23-25
    sprite('es201_07', 3)	# 25-27"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 16, 11),
                                 WaitFrameChunk(3),
                                 AttackFrameChunk(5, 16, 11),
                                 WaitFrameChunk(9)
                                 ]
        expected.frame_chunks[1].damage = Damage(500, 100, 80, 0, False)
        expected.frame_chunks[3].damage = Damage(1000, 100, 80, 0, False)
        expected.frame_chunks[3].is_new_hit = False
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_parse_damage_with_many_custom_values(self):
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
        Damage(500)
        AttackP1(50)
        AttackP2(75)
        HitJumpCancel(1)
        Unknown1112('')
        Unknown11092(1)
    sprite('es201_00', 1)	# 1-1
    sprite('es201_01', 2)	# 2-3
    sprite('es201_02', 2)	# 4-5
    SFX_0('006_swing_blade_0')
    sprite('es201_03', 2)	# 6-7
    sprite('es201_04', 5)	# 8-12	 **attackbox here**
    sprite('es201_05', 3)	# 13-15
    sprite('es201_04', 5)	# 16-20	 **attackbox here**
    RefreshMultihit()
    AttackP1(80)
    Damage(1000)
    sprite('es201_04', 1)	# 16-20	 **attackbox here**
    RefreshMultihit()
    AttackP1(55)
    AttackP2(15)
    sprite('es201_05', 3)	# 21-23
    Recovery()
    Unknown2063()
    sprite('es201_06', 3)	# 23-25
    sprite('es201_07', 3)	# 25-27"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(7),
                                 AttackFrameChunk(5, 16, 11),
                                 WaitFrameChunk(3),
                                 AttackFrameChunk(5, 16, 11),
                                 AttackFrameChunk(1, 16, 11),
                                 WaitFrameChunk(9)
                                 ]
        expected.frame_chunks[1].damage = Damage(500, 50, 75, 0, True)
        expected.frame_chunks[3].damage = Damage(1000, 80, 75, 0, True)
        expected.frame_chunks[4].damage = Damage(1000, 55, 15, 0, True)
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_parse_attack_with_no_damage_defined(self):
        state = """
@State
def az406_dummy_5B3rd():

    def upon_IMMEDIATE():
        Unknown2009()
        AirPushbackY(22000)
        AirUntechableTime(40)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9015(1)
        Unknown3038(1)
        Unknown23078(1)
        if SLOT_4:
            AirPushbackX(35000)
            AirPushbackY(1000)
            YImpluseBeforeWallbounce(20)
            Unknown9346(1)
            Unknown9178(1)
            Unknown9362(1)
            Unknown9364(30)
            if (SLOT_4 > 1):
                AirUntechableTime(30)
                AirHitstunAfterWallbounce(30)
                GroundedHitstunAnimation(12)
                AirHitstunAnimation(12)
                Unknown1017()
    sprite('null', 5)	# 1-5
    sprite('vr_azef406_col', 3)	# 6-8	 **attackbox here**"""
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("az406_dummy_5B3rd" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrameChunk(5),
                                 AttackFrameChunk(3, 0, 0)
                                 ]
        expected.frame_chunks[1].damage = Damage(0, 100, 100, 0, False)
        self.assertEqual(expected, move_list["az406_dummy_5B3rd"])

    def test_parse_attack_with_call_subroutine(self):
        state = """@Subroutine
def Init_AtkData():
    AttackLevel_(1)
    AttackP1(70)
    AttackP2(90)
    Damage(500)
    Hitstop(6)
    Unknown9154(17)
    AirUntechableTime(21)
    Unknown11028(11)
    Unknown9016(1)
@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AirPushbackY(10000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitJumpCancel(1)
        Unknown1112('')
        CallSubroutine('Init_AtkData')
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
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)

        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [SubroutineCall("Init_AtkData"),
                                 WaitFrameChunk(7),
                                 AttackFrameChunk(5),
                                 WaitFrameChunk(9)
                                 ]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_calc_damage_strike(self):
        move = Move()
        move.frame_chunks = [WaitFrameChunk(7),
                             AttackFrameChunk(5, 16, 11),
                             WaitFrameChunk(3),
                             AttackFrameChunk(5, 16, 11),
                             WaitFrameChunk(9)
                             ]
        move.frame_chunks[1].damage = Damage(500, 50, 80, 0, True)
        move.frame_chunks[3].damage = Damage(1000, 75, 80, 0, True)
        to_test = calc_damage_for_move(move)
        expected = [Damage(500, 50, 80, 0, True), Damage(1000, 75, 80, 0, True)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_1_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrameChunk(24)]
        shot.additional_chunks = [[WaitFrameChunk(4), AttackFrameChunk(2)]]
        shot.additional_chunks[0][1].damage = Damage(1000, 60, 80, 0, False)
        to_test = calc_damage_for_move(shot)
        expected = [Damage(1000, 60, 80, 0, False)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_2_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrameChunk(24)]
        shot.additional_chunks = [[WaitFrameChunk(10), AttackFrameChunk(2)], [WaitFrameChunk(5), AttackFrameChunk(2)]]
        shot.additional_chunks[0][1].damage = Damage(1000, 60, 80, 0, False)
        shot.additional_chunks[1][1].damage = Damage(500, 60, 80, 0, False)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [Damage(500, 60, 80, 0, False), Damage(1000, 60, 80, 0, False)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_strike_then_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrameChunk(24), AttackFrameChunk(1)]
        shot.frame_chunks[1].damage = Damage(500, 60, 80, 0, False)
        shot.additional_chunks = [[WaitFrameChunk(30), AttackFrameChunk(2)]]
        shot.additional_chunks[0][1].damage = Damage(1000, 60, 80, 0, False)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [Damage(500, 60, 80, 0, False), Damage(1000, 60, 80, 0, False)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_strike_delays_2ndhit_projectile_hits_first(self):
        shot = Move()
        shot.frame_chunks = [WaitFrameChunk(24), AttackFrameChunk(1), WaitFrameChunk(2), AttackFrameChunk(1)]
        shot.frame_chunks[1].hitstop = 10
        shot.frame_chunks[1].damage = Damage(500, 60, 80, 0, False)
        shot.frame_chunks[3].damage = Damage(600, 60, 70, 5, False)
        shot.additional_chunks = [[WaitFrameChunk(30), AttackFrameChunk(2)]]
        shot.additional_chunks[0][1].damage = Damage(1000, 100, 100, 0, False)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [Damage(500, 60, 80, 0, False), Damage(1000, 100, 100, 0, False), Damage(600, 60, 70, 5, False)]
        self.assertEqual(expected, to_test)

    # def test_damage_text_simple_attack(self):
    #     damage_str = create_damage_text([Damage(500, 60, 80)])
    #     self.assertEqual("", damage_str)
