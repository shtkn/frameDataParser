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
        chunks = [WaitFrames(4), ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4, attack_level=2)),
                  WaitFrames(12),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4)), WaitFrames(12)]
        toTestChunks = [WaitFrames(4), ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4, attack_level=2)),
                        WaitFrames(12),
                        ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4)), WaitFrames(12)]
        expected = Move()
        expected.frame_chunks = chunks
        toTest = Move()
        toTest.frame_chunks = toTestChunks
        # no effects to combine, just expect teh same chunks back
        result = combine_with_effects_on_block(toTest, {})
        self.assertEqual(0, len(result.additional_chunks))
        self.assertItemsEqual(expected.frame_chunks, result.frame_chunks)

    def test_simulate_hit_projectile(self):
        chunks = [WaitFrames(4), SubroutineCall("Shot"), WaitFrames(12)]
        shot = Move()
        shot.frame_chunks = [WaitFrames(4), ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0, 0, 0,
                                                                            0, 3, [False, True, False, False, False]))]
        effect_list = {"Shot": shot}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual([WaitFrames(16)], result.frame_chunks)
        # basically increasing the startup of hte shot by 4
        expected = [WaitFrames(8),
                    ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0, 0, 0,
                                                    0, 3, [False, True, False, False, False])),
                    ]
        self.assertItemsEqual(expected, result.additional_chunks[0])

    def test_simulate_hit_projectile_spawned_by_other_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("ShotGenerator1"), WaitFrames(12)]
        shotGenerator1 = Move()
        shotGenerator1.frame_chunks = [SubroutineCall("ShotGenerator2")]
        shotGenerator2 = Move()
        shotGenerator2.frame_chunks = [SubroutineCall("Shot")]

        shot = Move()
        shot.frame_chunks = [WaitFrames(4), ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0, 0, 0,
                                                                            0, 3, [False, True, False, False, False]))]
        effect_list = {"Shot": shot, "ShotGenerator1": shotGenerator1, "ShotGenerator1": shotGenerator2}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual([WaitFrames(16)], result.frame_chunks)
        # basically increasing the startup of hte shot by 4
        expected = [WaitFrames(8),
                    ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0, 0, 0,
                                                    0, 3, [False, True, False, False, False])),
                    ]
        self.assertItemsEqual(expected, result.additional_chunks[0])

    def test_simulate_hit_use_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("InitValues"), ActiveFrames(1, info=AttackInfo(0)), WaitFrames(4)]
        init = Subroutine()
        init.attackInfo = AttackInfo(500, 50, 60, 99, False, 90, 91, 2, 1, 10, 11, 0, None, None, None)
        init.landingRecovery = 4
        effect_list = {"InitValues": init}
        move = Move()
        move.frame_chunks = chunks
        move.landing_recovery = 4
        result = combine_with_effects_on_block(move, effect_list)
        # expect hitstop, blockstun, landing recovery etc to be replaced by values from InitValues
        self.assertEqual(0, len(result.additional_chunks))
        expected_frame_chunks = [WaitFrames(4),
                                 ActiveFrames(1, info=AttackInfo(500, 50, 60, 99, False, 90, 91, 2, 1, 10, 11, 0)),
                                 WaitFrames(4)]
        self.assertItemsEqual(expected_frame_chunks, result.frame_chunks)
        self.assertEqual(init.landingRecovery, result.landing_recovery)

    def test_simulate_projectile_using_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("Shot"), WaitFrames(12)]
        shot = Move()
        shot.frame_chunks = [SubroutineCall("ShotInit"), WaitFrames(4),
                             ActiveFrames(2, info=AttackInfo(500, 50, 60, 0, False))]
        shot_init = Subroutine()
        shot_init.attackInfo.hitstun = 0
        shot_init.attackInfo.untech = 0
        shot_init.attackInfo.hitstop = 1
        shot_init.attackInfo.blockstun = 2
        shot_init.attackInfo.bonus_blockstop = 3
        shot_init.attackInfo.bonus_hitstop = 4
        shot_init.attackInfo.minDamage = 15
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
                                 ActiveFrames(2, info=AttackInfo(500, 50, 60, 15, False, 0, 0, 2, 1, 3, 4))
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
        result = calc_frames_for_subroutine(chunks, [(2, 3)])
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
        subroutine.attackInfo.hitstop = 6
        subroutine.attackInfo.blockstun = 11
        subroutine.attackInfo.hitstun = 17
        subroutine.attackInfo.untech = 21
        subroutine.attackInfo.damage = 900
        subroutine.attackInfo.p1 = 70
        subroutine.attackInfo.p2 = 90
        subroutine.attackInfo.attackLevel = 1
        subroutine.attackInfo.groundHitAni = 0
        subroutine.attackInfo.airHitAni = 0
        subroutine.landingRecovery = 0
        self.assertEquals(effect_list["Monsho_AtkData"], subroutine)

    def test_parse_attack_with_custom_blockstun_hitstop(self):
        state = """@State
def NmlAtk5X():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
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
                                 ActiveFrames(5,
                                              info=AttackInfo(None, attack_level=3, blockstun=10, hitstop=10, p2once=None,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].info.attribute = [False, True, False, False, False]
        self.assertEqual(move_list["NmlAtk5X"], expected)

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
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),

                                 ActiveFrames(2,
                                              info=AttackInfo(None, attack_level=3,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 ActiveFrames(3,
                                              info=AttackInfo(None, attack_level=3,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(9)
                                 ]
        self.assertEqual(move_list["NmlAtk5X"], expected)

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
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(None, attack_level=3,
                                                                 attribute=[False, True, False, False, False],
                                                                 ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(9)
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

        self.assertEqual(7, move_list["NmlAtk5X"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5X"].frame_chunks[0], WaitFrames))
        self.assertEqual(5, move_list["NmlAtk5X"].frame_chunks[1].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5X"].frame_chunks[1], ActiveFrames))
        self.assertEqual(6, move_list["NmlAtk5X"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5X"].frame_chunks[2], WaitFrames))

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
        self.assertEqual(7, move_list["NmlAtk5X"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5X"].frame_chunks[0], WaitFrames))
        self.assertEqual(5, move_list["NmlAtk5X"].frame_chunks[1].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5X"].frame_chunks[1], ActiveFrames))
        self.assertEqual(6, move_list["NmlAtk5X"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5X"].frame_chunks[2], WaitFrames))

        self.assertTrue("NmlAtk6X" in move_list)
        self.assertEqual(7, move_list["NmlAtk6X"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["NmlAtk6X"].frame_chunks[0], WaitFrames))
        self.assertEqual(5, move_list["NmlAtk6X"].frame_chunks[1].duration)
        self.assertTrue(isinstance(move_list["NmlAtk6X"].frame_chunks[1], ActiveFrames))
        self.assertEqual(9, move_list["NmlAtk6X"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["NmlAtk6X"].frame_chunks[2], WaitFrames))

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
        self.assertEqual(expected.frame_chunks[1].inv_type, move_list["NmlAtk5X"].frame_chunks[1].inv_type)
        self.assertEqual(expected.frame_chunks[1].inv_attr, move_list["NmlAtk5X"].frame_chunks[1].inv_attr)
        self.assertEqual(expected.frame_chunks[2].inv_type, move_list["NmlAtk5X"].frame_chunks[2].inv_type)
        self.assertEqual(expected.frame_chunks[2].inv_attr, move_list["NmlAtk5X"].frame_chunks[2].inv_attr)
        self.assertEqual(expected.frame_chunks[2].info.attribute, move_list["NmlAtk5X"].frame_chunks[2].info.attribute)

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
        self.assertEqual(expected.frame_chunks[2].inv_type, move_list["NmlAtk5X"].frame_chunks[2].inv_type)
        self.assertEqual(expected.frame_chunks[2].inv_attr, move_list["NmlAtk5X"].frame_chunks[2].inv_attr)
        self.assertEqual(expected.frame_chunks[3].inv_type, move_list["NmlAtk5X"].frame_chunks[3].inv_type)
        self.assertEqual(expected.frame_chunks[3].inv_attr, move_list["NmlAtk5X"].frame_chunks[3].inv_attr)

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
    Unknown2036(5, -1, 0)
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
        self.assertEqual(1, len(move_list["NmlAtk5X"].superflash_list))
        superflash = move_list["NmlAtk5X"].superflash_list[0]
        self.assertEqual(2, superflash[0])
        self.assertEqual(5, superflash[1])

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
                                 ActiveFrames(5, info=AttackInfo(500, attack_level=3,
                                                                 attribute=[False, True, False, False, False],
                                                                 ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(3),
                                 ActiveFrames(5,
                                              info=AttackInfo(1000, attack_level=3,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(9)
                                 ]
        expected.frame_chunks[1].is_new_hit = True
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
                                 ActiveFrames(5, info=AttackInfo(500, attack_level=3, p1=50, p2=75, p2once=True,
                                                                 attribute=[False, True, False, False, False],
                                                                 ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(3),
                                 ActiveFrames(5,
                                              info=AttackInfo(1000, attack_level=3, p1=80, p2=75, p2once=True,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 ActiveFrames(1,
                                              info=AttackInfo(1000, attack_level=3, p1=55, p2=15, p2once=True,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(9)
                                 ]
        self.assertEqual(expected.frame_chunks[1], move_list["NmlAtk5X"].frame_chunks[1])
        self.assertEqual(expected.frame_chunks[3], move_list["NmlAtk5X"].frame_chunks[3])
        self.assertEqual(expected.frame_chunks[4], move_list["NmlAtk5X"].frame_chunks[4])
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_parse_attack_with_activeframes_that_are_only_one_hit(self):
        state = """
def UltimateShot_DDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(1)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(1)
        Unknown11066(1)
        Unknown11064(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown23027()
        Unknown30063(1)
        Unknown1084(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
        Unknown13024(0)
        Unknown11069('UltimateShot_DDD')
    sprite('hz431_06', 3)	# 1-3
    sprite('hz431_22ex', 1)	# 4-5	 **attackbox here**
    RefreshMultihit()
    sprite('hz431_23ex', 1)	# 6-7	 **attackbox here**
    sprite('null', 1)	# 8-9
    """
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)
        self.assertEqual(3, move_list["UltimateShot_DDD"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["UltimateShot_DDD"].frame_chunks[0], WaitFrames))
        self.assertEqual(2, move_list["UltimateShot_DDD"].frame_chunks[1].duration)
        self.assertTrue(isinstance(move_list["UltimateShot_DDD"].frame_chunks[1], ActiveFrames))
        self.assertEqual(1, move_list["UltimateShot_DDD"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["UltimateShot_DDD"].frame_chunks[2], WaitFrames))

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
        Damage(900)
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
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(900, 70, 90, 0, None, 17, 21, 11, 6,
                                                                 attack_level=1,
                                                                 attribute=[False, True, False, False, False],
                                                                 ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(9)
                                 ]
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
                                 ActiveFrames(2,
                                              info=AttackInfo(None, attack_level=2,
                                                              attribute=[False, True, False, False, False],
                                                              ground_hit_ani=0, air_hit_ani=0)),
                                 WaitFrames(19)
                                 ]
        self.assertEqual(expected, move_list["NmlAtk5A"])

    def test_parse_move_with_gfx_before_refresh_multihit(self):
        state = """@State
    def NmlAtk5A():
        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
            AttackLevel_(2)
        sprite('Action_001_00', 3)	# 1-3
        sprite('Action_001_01', 3)	# 4-6
        Unknown7009(0)
        sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
        GFX_0('esef_201', -1)
        RefreshMultihit()
        sprite('Action_001_02', 2)	# 9-10	 **attackbox here**
        sprite('Action_001_03', 4)	# 11-14
        Unknown23027()
        Recovery()
        Unknown2063()
        sprite('Action_001_04', 8)	# 15-22
        sprite('Action_001_05', 4)	# 23-26
        sprite('Action_001_06', 3)	# 27-29
            """
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)

        self.assertEqual(6, move_list["NmlAtk5A"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[0], WaitFrames))
        self.assertEqual("esef_201", move_list["NmlAtk5A"].frame_chunks[1].name)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[1], SubroutineCall))
        self.assertEqual(4, move_list["NmlAtk5A"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[2], ActiveFrames))
        self.assertEqual(19, move_list["NmlAtk5A"].frame_chunks[3].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[3], WaitFrames))

    def test_parse_move_with_start_multihit(self):
        state = """@State
    def NmlAtk5A():
        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
            AttackLevel_(2)
        sprite('Action_001_00', 3)	# 1-3
        sprite('Action_001_01', 3)	# 4-6
        Unknown7009(0)
        sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
        StartMultihit()
        sprite('Action_001_02', 2)	# 9-10	 **attackbox here**
        sprite('Action_001_02', 2)	# 11-12	 **attackbox here**
        StartMultihit()
        Unknown2063()
        sprite('Action_001_04', 8)	# 13-20
        sprite('Action_001_05', 4)	# 21-24
        sprite('Action_001_06', 3)	# 25-27
            """
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)
        self.assertEqual(8, move_list["NmlAtk5A"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[0], WaitFrames))
        self.assertEqual(2, move_list["NmlAtk5A"].frame_chunks[1].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[1], ActiveFrames))
        self.assertEqual(17, move_list["NmlAtk5A"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[2], WaitFrames))

    def test_parse_move_with_disable_hitboxes_but_refresh_multithit_called(self):
        state = """@State
    def NmlAtk5A():
        def upon_IMMEDIATE():
            AttackDefaults_StandingNormal()
            AttackLevel_(2)
        sprite('Action_001_00', 3)	# 1-3
        Unknown23027()
        sprite('Action_001_01', 3)	# 4-6
        sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
        sprite('Action_001_02', 2)	# 9-10	 **attackbox here**
        sprite('Action_001_02', 2)	# 11-12	 **attackbox here**
        RefreshMultihit()
        sprite('Action_001_04', 8)	# 13-20
        sprite('Action_001_05', 4)	# 21-24
        sprite('Action_001_06', 3)	# 25-27
            """
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)
        self.assertEqual(10, move_list["NmlAtk5A"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[0], WaitFrames))
        self.assertEqual(2, move_list["NmlAtk5A"].frame_chunks[1].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[1], ActiveFrames))
        self.assertEqual(15, move_list["NmlAtk5A"].frame_chunks[2].duration)
        self.assertTrue(isinstance(move_list["NmlAtk5A"].frame_chunks[2], WaitFrames))

    def test_parse_move_with_subroutine_in_upon_immediate(self):
        subroutine = """@Subroutine
def Init_AtkData():
    Damage(900)
    AttackP1(70)
    """
        buf = StringIO.StringIO(subroutine)
        effect_list = OrderedDict()
        effect_list = parse_move_file(buf, effect_list, effect_list)
        state = """@State
def NmlAtk5A():
    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        Damage(500)
        CallSubroutine('Init_AtkData')
    sprite('Action_001_00', 3)	# 1-3
    sprite('Action_001_01', 3)	# 4-6
    sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_001_04', 8)	# 13-20
    sprite('Action_001_05', 4)	# 21-24
    sprite('Action_001_06', 3)	# 25-27
            """
        buf = StringIO.StringIO(state)
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)
        hit_simulations = simulate_on_block(move_list, effect_list)
        expected = AttackInfo(900, p1=70, attack_level=1,
                              attribute=[False, True, False, False, False],
                              ground_hit_ani=0, air_hit_ani=0)
        self.assertEqual(expected, hit_simulations["NmlAtk5A"].frame_chunks[1].info)

    def test_calc_damage_strike(self):
        move = Move()
        move.frame_chunks = [WaitFrames(7),
                             ActiveFrames(5, info=AttackInfo(500, blockstun=16, hitstop=11)),
                             WaitFrames(3),
                             ActiveFrames(5, info=AttackInfo(1000, blockstun=16, hitstop=11)),
                             WaitFrames(9)
                             ]
        to_test = calc_damage_for_move(move)
        expected = [move.frame_chunks[1].info, move.frame_chunks[3].info]
        self.assertEqual(expected, to_test)

    def test_calc_damage_1_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24)]
        shot.additional_chunks = [[WaitFrames(4), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 60, 80, 0, None, 10, 11, 12, 13)
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(1000, 60, 80, 0, None, 10, 11, 12, 13)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_2_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24)]
        shot.additional_chunks = [[WaitFrames(10), ActiveFrames(2)], [WaitFrames(5), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 60, 80, 0, None, 10, 11, 12, 13)
        shot.additional_chunks[1][1].info = AttackInfo(500, 60, 80, 0, None, 10, 11, 12, 13)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(500, 60, 80, 0, None, 10, 11, 12, 13),
                    AttackInfo(1000, 60, 80, 0, None, 10, 11, 12, 13)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_strike_then_projectile(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24), ActiveFrames(1)]
        shot.frame_chunks[1].info = AttackInfo(500, 60, 80, 0, None, 10, 11, 12, 13)
        shot.additional_chunks = [[WaitFrames(30), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 60, 80, 0, None, 10, 11, 12, 13)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(500, 60, 80, 0, None, 10, 11, 12, 13),
                    AttackInfo(1000, 60, 80, 0, None, 10, 11, 12, 13)]
        self.assertEqual(expected, to_test)

    def test_calc_damage_strike_delays_2ndhit_projectile_hits_first(self):
        shot = Move()
        shot.frame_chunks = [WaitFrames(24), ActiveFrames(1), WaitFrames(2), ActiveFrames(1)]
        shot.frame_chunks[1].info = AttackInfo(500, 60, 80, 0, None, 10, 11, 12, 10)
        shot.frame_chunks[3].info = AttackInfo(600, 60, 70, 5, None, 10, 11, 12, 13)
        shot.additional_chunks = [[WaitFrames(30), ActiveFrames(2)]]
        shot.additional_chunks[0][1].info = AttackInfo(1000, 100, 100, 0, None, 10, 11, 12, 13)
        # combine with ShotAnimation
        to_test = calc_damage_for_move(shot)
        expected = [AttackInfo(500, 60, 80, 0, None, 10, 11, 12, 10),
                    AttackInfo(1000, 100, 100, 0, None, 10, 11, 12, 13),
                    AttackInfo(600, 60, 70, 5, None, 10, 11, 12, 13)
                    ]
        self.assertEqual(expected, to_test)

    def test_use_subroutine_in_attack_on_block(self):
        subroutine = Subroutine()
        subroutine.attackInfo.damage = 900
        subroutine.attackInfo.p1 = 50
        subroutine.attackInfo.p2 = 75
        effect_list = {"init": subroutine}
        move = Move()
        move.frame_chunks = [SubroutineCall("init"),
                             WaitFrames(5),
                             ActiveFrames(2,
                                          info=AttackInfo(0, blockstun=10, hitstop=20, p2once=True)),
                             WaitFrames(5)]
        result = combine_with_effects_on_block(move, effect_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(5),
                                 ActiveFrames(2,
                                              info=AttackInfo(subroutine.attackInfo.damage, p1=50, p2=75, blockstun=10, hitstop=20,
                                                              p2once=True)),
                                 WaitFrames(5)
                                 ]
        self.assertEqual(expected, result)

    def test_hitstop_text(self):
        test = [AttackInfo(500, 60, 80, 0, None, hitstop=10),
                AttackInfo(1000, 100, 100, 0, None, hitstop=10, bonus_blockstop=5, bonus_hitstop=1),
                AttackInfo(600, 60, 70, 5, None, hitstop=10, bonus_blockstop=5),
                AttackInfo(600, 60, 70, 5, None, hitstop=10, bonus_hitstop=5)
                ]
        damage, p1, p2, hitstun, untech, level, attribute, hitstop, blockstun = create_damage_text(test)
        print hitstop

    def test_parse_function_with_one_sprite_line(self):
        state = """def vr_lp206atk_04():
    def upon_IMMEDIATE():
        Unknown2009()
        callSubroutine('vr_lp206atk')
        teleportRelativeX(100000)
        Unknown1007(50000)
        physicsXImpulse(50000)
        setGravity(-2000)
    sprite('vr_lp206atkcol_ex', 11)	# 1-11	 **attackbox here**"""
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)
        self.assertEqual(11, move_list["vr_lp206atk_04"].frame_chunks[0].duration)
        self.assertTrue(isinstance(move_list["vr_lp206atk_04"].frame_chunks[0], ActiveFrames))

    def test_parse_hardcoded_inv(self):
        state = """def atk():
    def upon_IMMEDIATE():
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000000000000')
    sprite('jn202_00', 2)	# 1-2
    sprite('jn202_01', 2)	# 3-4
    Unknown22008(5)
    sprite('jn202_02', 2)	# 5-6
    sprite('jn202_01', 4)	# 3-4
    sprite('jn202_02', 8)	# 5-6"""
        buf = StringIO.StringIO(state)
        effect_list = OrderedDict()
        move_list = OrderedDict()
        move_list = parse_move_file(buf, move_list, effect_list)
        atk = move_list["atk"]
        self.assertIsNotNone(atk)
        self.assertEquals(1, len(atk.hardcoded_inv_list))
        inv_values = atk.hardcoded_inv_list[0]
        self.assertEqual(3, inv_values[0])
        self.assertEqual(5, inv_values[1])
        self.assertEqual(1, inv_values[2])
        self.assertEqual([True, True, True, True, False], inv_values[3])

    def test_compare_frame_chunk_util(self):

        frame_chunks1 = [WaitFrames(5),
                        ActiveFrames(2, info=AttackInfo(600, p1=50, p2=75, blockstun=10, hitstop=20,
                                                      p2once=True)),
                        WaitFrames(5)
                        ]

        frame_chunks2 = [WaitFrames(5),
                        ActiveFrames(2, info=AttackInfo(600, p1=50, p2=75, blockstun=10, hitstop=20,
                                                      p2once=True)),
                        WaitFrames(5)
                        ]
        self.compare_frame_chunks_util(frame_chunks1, frame_chunks2)

    # util method to help make debugging what's different between objects easier to detect.
    # Tests should still use normal assertEquals, only use these when debugging or else we may
    # have problems with outdated compare methods.

    def compare_move_util(self, first, second):
        self.assertEqual(first.landing_recovery, second.landing_recovery)
        self.assertEquals(first.superflash_list, second.superflash_list)
        self.assertEquals(first.hardcoded_inv_list, second.hardcoded_inv_list)
        self.compare_frame_chunks_util(first.frame_chunks, second.frame_chunks, "move.frame_chunks")
        self.assertEqual(len(first.frame_chunks), len(second.frame_chunks))
        for i in range(len(first.additional_chunks)):
            self.compare_frame_chunks_util(first.additional_chunks[i], second.additional_chunks[i], "move.additonal_chunks[" + str(i) + "]")

    def compare_frame_chunks_util(self, first, second, name=""):
        self.assertEqual(len(first), len(second))
        for i in range(len(first)):
            if first[i] != second[i] and isinstance(first[i], ActiveFrames) and isinstance(second[i], ActiveFrames):
                print "Unequal Active Frame Chunk detected at " + name + "[" + str(i) + "]"
                self.assertEqual(first[i].is_new_hit, second[i].is_new_hit, "is_new_hit not equal")
                self.compare_attack_info(first[i].info, second[i].info)
            if first[i] != second[i] and isinstance(first[i], AbstractFrames) and isinstance(second[i], AbstractFrames):
                print "Unequal Abstract Frame Chunk detected at " + name + "[" + str(i) + "]"
                self.assertEqual(first[i].inv_type, second[i].inv_type, "inv_type not equal")
                self.assertEqual(first[i].inv_attr, second[i].inv_attr, "inv_attr not equal")
                self.assertEqual(first[i].duration, second[i].duration, "duration not equal")
            else:
                self.assertEqual(first[i], second[i], "Unequal Object detected at [" + str(i) + "]")

    def compare_attack_info(self, first, second):
        self.assertEqual(first.damage, second.damage, "Damage not equal")
        self.assertEqual(first.p1, second.p1, "p1 not equal")
        self.assertEqual(first.p2, second.p2, "p2 not equal")
        self.assertEqual(first.minDamage, second.minDamage, "minDamage not equal")
        self.assertEqual(first.p2Once, second.p2Once, "p2Once not equal")
        self.assertEqual(first.blockstun, second.blockstun, "blockstun not equal")
        self.assertEqual(first.hitstun, second.hitstun, "hitstun not equal")
        self.assertEqual(first.untech, second.untech, "hitstun not equal")
        self.assertEqual(first.attackLevel, second.attackLevel, "attackLevel not equal")
        self.assertEqual(first.hitstop, second.hitstop, "hitstop not equal")
        self.assertEqual(first.bonus_hitstop, second.bonus_hitstop, "bonus_hitstop not equal")
        self.assertEqual(first.bonus_blockstop, second.bonus_blockstop, "bonus_blockstop not equal")
        self.assertEqual(first.attribute, second.attribute, "attribute not equal")
        self.assertEqual(first.groundHitAni, second.groundHitAni, "groundHitAni not equal")
        self.assertEqual(first.airHitAni, second.airHitAni, "groundHitAni not equal")
        self.assertEqual(first.knockdownTime, second.knockdownTime, "knockdownTime not equal")
        self.assertEqual(first.slideTime, second.slideTime, "slideTime not equal")
        self.assertEqual(first.hitstunAfterWallBounce, second.hitstunAfterWallBounce, "hitstunAfterWallBounce not equal")
        self.assertEqual(first.wallStickTime, second.wallStickTime, "wallStickTime not equal")
        self.assertEqual(first.crumpleTime, second.crumpleTime, "crumpleTime not equal")
        self.assertEqual(first.spinFallTime, second.spinFallTime, "spinFallTime not equal")
        self.assertEqual(first.groundBounce, second.groundBounce, "groundBounce not equal")
        self.assertEqual(first.wallBounce, second.wallBounce, "wallBounce not equal")
