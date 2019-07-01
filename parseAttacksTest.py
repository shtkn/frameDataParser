import unittest
import StringIO
from parseAttacks import *


class TestParseAttackMethods(unittest.TestCase):
    def test_combine_2_wait_frames(self):
        chunks = [WaitFrames(2), WaitFrames(4)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrames(6)]
        self.assertItemsEqual(expected, result)

    def test_combine_2_active_frames(self):
        chunks = [ActiveFrames(2), ActiveFrames(2, is_new_hit=False)]
        result = consolidate_frame_chunks(chunks)
        expected = [ActiveFrames(4)]
        self.assertItemsEqual(expected, result)

    def test_dont_combine_2_active_frames(self):
        chunks = [ActiveFrames(2, is_new_hit=True), ActiveFrames(2, is_new_hit=True)]
        result = consolidate_frame_chunks(chunks)
        expected = [ActiveFrames(2), ActiveFrames(2)]
        self.assertItemsEqual(expected, result)

    def test_combine_2_wait_frames_with_active_after(self):
        chunks = [WaitFrames(2), WaitFrames(4), ActiveFrames(1), WaitFrames(2)]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrames(6), ActiveFrames(1), WaitFrames(2)]
        self.assertItemsEqual(expected, result)

    def test_do_not_combine_wait_frames_with_inv(self):
        chunks = [WaitFrames(2), WaitFrames(4)]
        chunks[0].inv_type = 0
        chunks[1].inv_type = 1
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(expected, result)

    def test_do_not_combine_wait_frames_with_diff_inv(self):
        chunks = [WaitFrames(2), WaitFrames(2)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(result, expected)

    def test_do_combine_wait_frames_with_diff_inv(self):
        chunks = [WaitFrames(2), WaitFrames(2)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks, True)
        expected = [WaitFrames(4)]
        self.assertEqual(len(expected), len(result))
        self.assertEqual(expected[0].duration, result[0].duration)  # inv for this combined chunk is undefined behavior

    def test_do_not_combine_active_frame_types_with_same_inv(self):
        chunks = [ActiveFrames(2, is_new_hit=True), ActiveFrames(2, is_new_hit=True)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [True, False, False, False, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, False, False, False, False]
        result = consolidate_frame_chunks(chunks)
        expected = chunks
        self.assertItemsEqual(result, expected)

    def test_combine_active_frame_types_with_same_inv(self):
        chunks = [ActiveFrames(2, is_new_hit=True), ActiveFrames(2, is_new_hit=False)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, False, False, False, True]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [False, False, False, False, True]
        result = consolidate_frame_chunks(chunks)
        expected = [ActiveFrames(4)]
        expected[0].inv_type = 1
        expected[0].inv_attr = [False, False, False, False, True]
        self.assertItemsEqual(result, expected)

    def test_combine_same_frame_types_with_same_inv(self):
        chunks = [WaitFrames(2), WaitFrames(4)]
        chunks[0].inv_type = 1
        chunks[0].inv_attr = [False, True, True, True, False]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [False, True, True, True, False]
        result = consolidate_frame_chunks(chunks)
        expected = [WaitFrames(6)]
        expected[0].inv_type = 1
        expected[0].inv_attr = [False, True, True, True, False]
        self.assertItemsEqual(result, expected)

    def test_get_duration(self):
        self.assertEqual(15, get_duration("    sprite('null', 15)"))

    def test_simulate_hit_basic_normal(self):
        chunks = [WaitFrames(4), ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4)), WaitFrames(12),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4)), WaitFrames(12)]
        expected = Move()
        expected.frame_chunks = chunks
        # no effects to combine, just expect teh same chunks back
        result = combine_with_effects_on_block(expected, {})
        self.assertEqual(0, len(result.additional_chunks))
        self.assertItemsEqual(expected.frame_chunks, chunks)

    def test_simulate_hit_projectile(self):
        chunks = [WaitFrames(4), SubroutineCall("Shot"), WaitFrames(12)]
        shot = Move()
        shot.frame_chunks = [WaitFrames(4), ActiveFrames(2)]
        effect_list = {"Shot": shot}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual([WaitFrames(16)], result.frame_chunks)
        # basically increasing the startup of hte shot by 4
        self.assertItemsEqual([WaitFrames(8), ActiveFrames(2)], result.additional_chunks[0])

    def test_simulate_hit_use_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("InitValues"), ActiveFrames(1, info=AttackInfo(0)), WaitFrames(4)]
        init = Subroutine()
        init.hitstop = 1
        init.blockstun = 2
        init.bonus_blockstop = 3
        init.landingRecovery = 4
        init.damage = 500
        init.p1 = 50
        init.p2 = 60
        init.minDamage = 99
        effect_list = {"InitValues": init}
        move = Move()
        move.frame_chunks = chunks
        move.landing_recovery = 4
        result = combine_with_effects_on_block(move, effect_list)
        # expect hitstop, blockstun, landing recovery etc to be replaced by values from InitValues
        self.assertEqual(0, len(result.additional_chunks))
        expected_frame_chunks = [WaitFrames(4),
                                 ActiveFrames(1, info=AttackInfo(500, 50, 60, 99, False, 0, 0, 2, 1, 3)),
                                 WaitFrames(4)]
        self.assertItemsEqual(expected_frame_chunks, result.frame_chunks)
        self.assertEqual(init.landingRecovery, result.landing_recovery)

    def test_simulate_projectile_using_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("Shot"), WaitFrames(12)]
        shot = Move()
        shot.frame_chunks = [SubroutineCall("ShotInit"), WaitFrames(4), ActiveFrames(2, info=AttackInfo(500, 50, 60))]
        shot_init = Subroutine()
        shot_init.hitstop = 1
        shot_init.blockstun = 2
        shot_init.bonus_blockstop = 3
        shot_init.minDamage = 15
        effect_list = {"Shot": shot,
                       "ShotInit": shot_init}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual(result.frame_chunks, [WaitFrames(16)])
        # basically increasing the startup of hte shot by 4
        expected_frame_chunks = [WaitFrames(8),
                                 ActiveFrames(2, info=AttackInfo(500, 50, 60, 15, False, 0, 0, 2, 1, 3))
                                 ]
        self.assertItemsEqual(result.additional_chunks[0], expected_frame_chunks)

    def test_parse_inv_attr_str1(self):
        values = parse_attributes("0000000000000000010000000000000001000000")
        self.assertEqual([False, False, True, False, True], values)

    def test_parse_inv_attr_str2(self):
        values = parse_attributes("0100000001000000000000000100000000000000")
        self.assertEqual([True, True, False, True, False], values)

    def test_calculate_frame_adv_1_hit(self):
        chunks = [WaitFrames(4), ActiveFrames(1, info=AttackInfo(0, blockstun=3, hitstop=3)), WaitFrames(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '1', '12', 17, 20, 11, []), result)

    def test_calculate_frame_adv_2_hit(self):
        chunks = [WaitFrames(4),
                  ActiveFrames(3, info=AttackInfo(0, blockstun=3, hitstop=3)),
                  ActiveFrames(3, info=AttackInfo(0, blockstun=3, hitstop=3)),
                  WaitFrames(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '3,3', '12', 22, 28, 17, []), result)

    def test_calculate_frame_adv_2_hit_with_gap(self):
        chunks = [WaitFrames(4),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=3, hitstop=3)),
                  WaitFrames(3),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=3, hitstop=3)),
                  WaitFrames(12)
                  ]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '1(3)1', '12', 21, 27, 18, []), result)

    def test_calculate_frame_adv_with_5_active_frames(self):
        chunks = [WaitFrames(4), ActiveFrames(5, info=AttackInfo(0, blockstun=3, hitstop=3)), WaitFrames(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '5', '12', 21, 24, 11, []), result)

    def test_calculate_frame_adv_1_hit_bonus_hitstop(self):
        chunks = [WaitFrames(4),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=3, hitstop=3, bonus_blockstop=10)),
                  WaitFrames(12)]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '1', '12', 17, 20, 21, []), result)

    def test_calculate_frame_adv_attr_inv(self):
        chunks = [WaitFrames(4), ActiveFrames(3, info=AttackInfo(0, blockstun=3, hitstop=3)), WaitFrames(12)]
        chunks[1].inv_type = 1
        chunks[1].inv_attr = [True, True, False, False, False]
        result = calc_frames_for_subroutine(chunks)
        self.assertItemsEqual(('5', '3', '12', 19, 22, 11, [[5, 3, 1, [True, True, False, False, False]]]), result)

    def test_calculate_startup_with_superflash(self):
        chunks = [WaitFrames(4),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=3, hitstop=3)),
                  WaitFrames(3),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=3, hitstop=3)),
                  WaitFrames(12)
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
        subroutine.attackLevel = 1
        subroutine.p2Once = False
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
        expected.frame_chunks = [WaitFrames(7),
                                 SubroutineCall("esef_201"),
                                 ActiveFrames(5),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[2].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(0, blockstun=10, hitstop=10)),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(2),
                                 ActiveFrames(3),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
        expected.frame_chunks[2].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5),
                                 WaitFrames(6)
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5),
                                 WaitFrames(6)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

        self.assertTrue("NmlAtk6X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5),
                                 WaitFrames(9)
                                 ]
        self.assertEqual(expected, move_list["NmlAtk6X"])

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
     sprite('es201_07', 3)	# 19-21
     """
        buf = StringIO.StringIO(state)
        move_list = parse_move_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(5),
                                 WaitFrames(2),
                                 ActiveFrames(5),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].inv_type = 1
        expected.frame_chunks[1].inv_attr = [True, False, False, False, False]
        expected.frame_chunks[2].inv_type = 1
        expected.frame_chunks[2].inv_attr = [True, False, False, False, False]
        expected.frame_chunks[2].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(5),
                                 SubroutineCall("esef_aaaa"),
                                 WaitFrames(2),
                                 ActiveFrames(5),
                                 WaitFrames(9)
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
        expected.frame_chunks = [WaitFrames(5),
                                 SubroutineCall("esef_aaaa"),
                                 WaitFrames(2),
                                 ActiveFrames(5),
                                 WaitFrames(9)
                                 ]
        expected.superflash_start = 2
        expected.superflash_duration = 2
        expected.frame_chunks[3].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(500, 100, 80, 0, False, 17, 17, 16, 11, 0, 3)),
                                 WaitFrames(3),
                                 ActiveFrames(5, info=AttackInfo(1000, 100, 80, 0, False, 17, 17, 16, 11, 0, 3)),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
        expected.frame_chunks[3].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(0, blockstun=16, hitstop=11)),
                                 WaitFrames(3),
                                 ActiveFrames(5, info=AttackInfo(0, blockstun=16, hitstop=11)),
                                 ActiveFrames(1, info=AttackInfo(0, blockstun=16, hitstop=11)),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].info = AttackInfo(500, 50, 75, 0, True, 17, 17, 16, 11, 0,  3)
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
        expected.frame_chunks[3].info = AttackInfo(1000, 80, 75, 0, True, 17, 17, 16, 11, 0, 3)
        expected.frame_chunks[3].info.attribute = [False, True, False, False, False]
        expected.frame_chunks[4].info = AttackInfo(1000, 55, 15, 0, True, 17, 17, 16, 11, 0, 3)
        expected.frame_chunks[4].info.attribute = [False, True, False, False, False]
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
        expected.frame_chunks = [WaitFrames(5),
                                 ActiveFrames(3),
                                 ]
        expected.frame_chunks[1].info = AttackInfo(0, 100, 100, 0, False, 0, 40)
        expected.frame_chunks[1].info.hitstop = 0
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
                                 WaitFrames(7),
                                 ActiveFrames(5),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[2].info.attribute = [False, True, False, False, False]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_parse_move_with_attack_level_defaults(self):
        state = """@State
def NmlAtk5A():
    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
    sprite('Action_001_00', 3)	# 1-3
    sprite('Action_001_01', 3)	# 4-6
    Unknown7009(0)
    sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_001_03', 4)	# 9-12
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_001_04', 8)	# 13-20
    sprite('Action_001_05', 4)	# 21-24
    sprite('Action_001_06', 3)	# 25-27
        """
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)

        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5A" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(6),
                                 ActiveFrames(2, info=AttackInfo(0, blockstun=13, hitstop=10)),
                                 WaitFrames(19)
                                 ]
        expected.frame_chunks[1].info = AttackInfo(1000, 100, 75, 0, False, 14, 14, 13, 10, 0, 2)
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
        self.assertEqual(expected, move_list["NmlAtk5A"])

    def test_calc_damage_strike(self):
        move = Move()
        move.frame_chunks = [WaitFrames(7),
                             ActiveFrames(5, info=AttackInfo(0, blockstun=16, hitstop=11)),
                             WaitFrames(3),
                             ActiveFrames(5, info=AttackInfo(0, blockstun=16, hitstop=11)),
                             WaitFrames(9)
                             ]
        move.frame_chunks[1].info = AttackInfo(500, 50, 80, 0, True)
        move.frame_chunks[3].info = AttackInfo(1000, 75, 80, 0, True)
        to_test = calc_damage_for_move(move)
        expected = [AttackInfo(500, 50, 80, 0, True), AttackInfo(1000, 75, 80, 0, True)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_1_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24)]
        shot.additional_chunks = [[WaitFrames(4), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 60, 80, 0, False)
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(1000, 60, 80, 0, False)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_2_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24)]
        shot.additional_chunks = [[WaitFrames(10), ActiveFrames(2)], [WaitFrames(5), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 60, 80, 0, False)
        shot.additional_chunks[1][1].info = AttackInfo(500, 60, 80, 0, False)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(500, 60, 80, 0, False), AttackInfo(1000, 60, 80, 0, False)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_strike_then_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24), ActiveFrames(1)]
        shot.frame_chunks[1].info = AttackInfo(500, 60, 80, 0, False)
        shot.additional_chunks = [[WaitFrames(30), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 60, 80, 0, False)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(500, 60, 80, 0, False), AttackInfo(1000, 60, 80, 0, False)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_strike_delays_2ndhit_projectile_hits_first(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24), ActiveFrames(1), WaitFrames(2), ActiveFrames(1)]
        shot.frame_chunks[1].info = AttackInfo(500, 60, 80, 0, False)
        shot.frame_chunks[1].info.hitstop = 10
        shot.frame_chunks[3].info = AttackInfo(600, 60, 70, 5, False)
        shot.additional_chunks = [[WaitFrames(30), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 100, 100, 0, False)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(500, 60, 80, 0, False, hitstop=10),
                    AttackInfo(1000, 100, 100, 0, False),
                    AttackInfo(600, 60, 70, 5, False)
                    ]
        self.assertEqual(expected, to_test)

    def test_use_subroutine_in_attack_on_block(self):
        subroutine = Subroutine()
        subroutine.damage = 900
        subroutine.p1 = 50
        subroutine.p2 = 75
        effect_list = {"init": subroutine}
        move = Move()
        move.frame_chunks = [SubroutineCall("init"),
                             WaitFrames(5),
                             ActiveFrames(2, info=AttackInfo(0, blockstun=10, hitstop=20, bonus_blockstop=0, p2once=True)),
                             WaitFrames(5)]
        result = combine_with_effects_on_block(move, effect_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(5),
                                 ActiveFrames(2, info=AttackInfo(subroutine.damage, p1=50, p2=75, blockstun=10, hitstop=20, bonus_blockstop=0)),
                                 WaitFrames(5)
                                 ]
        self.assertEqual(expected, result)
    # def test_damage_text_simple_attack(self):
    #     damage_str = create_damage_text([Damage(500, 60, 80)])
    #     self.assertEqual("", damage_str)


    def test_hitstop_text(self):
        test = [AttackInfo(500, 60, 80, 0, False, hitstop=10),
                AttackInfo(1000, 100, 100, 0, False, hitstop=10, bonus_blockstop=5, bonus_hitstop=1),
                AttackInfo(600, 60, 70, 5, False, hitstop=10, bonus_blockstop=5),
                AttackInfo(600, 60, 70, 5, False, hitstop=10, bonus_hitstop=5)
                ]
        damage, p1, p2, hitstun, untech, level, attribute, hitstop, blockstun = create_damage_text(test)
        print hitstop
