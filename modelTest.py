import unittest

from model import *


class TestModel(unittest.TestCase):

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

    def test_calc_damage_strike_delays_2nd_hit_projectile_hits_first(self):
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
                                              info=AttackInfo(subroutine.attackInfo.damage, p1=50, p2=75, blockstun=10,
                                                              hitstop=20,
                                                              p2once=True)),
                                 WaitFrames(5)
                                 ]
        self.assertEqual(expected, result)

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
        self.assertItemsEqual(('2+(3 Flash)+0', '1(3)1', '12', 21, 27, 18, []), result)

    def test_simulate_hit_basic_normal(self):
        chunks = [WaitFrames(4), ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4, attack_level=2)),
                  WaitFrames(12),
                  ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4)), WaitFrames(12)]
        to_test_chunks = [WaitFrames(4), ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4, attack_level=2)),
                          WaitFrames(12),
                          ActiveFrames(1, info=AttackInfo(0, blockstun=4, hitstop=4)), WaitFrames(12)]
        expected = Move()
        expected.frame_chunks = chunks
        to_test = Move()
        to_test.frame_chunks = to_test_chunks
        # no effects to combine, just expect teh same chunks back
        result = combine_with_effects_on_block(to_test, {})
        self.assertEqual(0, len(result.additional_chunks))
        self.assertItemsEqual(expected.frame_chunks, result.frame_chunks)

    def test_simulate_hit_projectile(self):
        chunks = [WaitFrames(4), SubroutineCall("Shot"), WaitFrames(12)]
        shot = Move()
        shot.frame_chunks = [WaitFrames(4), ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0,
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
                    ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0,
                                                    0, 3, [False, True, False, False, False])),
                    ]
        self.assertItemsEqual(expected, result.additional_chunks[0])

    def test_simulate_hit_projectile_spawned_by_other_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("ShotGenerator1"), WaitFrames(12)]
        shot_generator1 = Move()
        shot_generator1.frame_chunks = [SubroutineCall("ShotGenerator2")]
        shot_generator2 = Move()
        shot_generator2.frame_chunks = [SubroutineCall("Shot")]

        shot = Move()
        shot.frame_chunks = [WaitFrames(4), ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0,
                                                                            0, 3, [False, True, False, False, False]))]
        effect_list = {"Shot": shot, "ShotGenerator1": shot_generator1, "ShotGenerator2": shot_generator2}
        move = Move()
        move.frame_chunks = chunks
        # combine with ShotAnimation
        result = combine_with_effects_on_block(move, effect_list)
        self.assertEqual(1, len(result.additional_chunks))
        self.assertItemsEqual([WaitFrames(16)], result.frame_chunks)
        # basically increasing the startup of hte shot by 4
        expected = [WaitFrames(8),
                    ActiveFrames(2, info=AttackInfo(0, 100, 100, 0, False, 0, 0, 0,
                                                    0, 3, [False, True, False, False, False])),
                    ]
        self.assertItemsEqual(expected, result.additional_chunks[0])

    def test_simulate_hit_use_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("InitValues"), ActiveFrames(1, info=AttackInfo(0)), WaitFrames(4)]
        init = Subroutine()
        init.attackInfo = AttackInfo(500, 50, 60, 99, False, 2, 1, 10, 11, 0, normal_hit=HitEffects(90, 91))
        init.landingRecovery = 4
        effect_list = {"InitValues": init}
        move = Move()
        move.frame_chunks = chunks
        move.landing_recovery = 4
        result = combine_with_effects_on_block(move, effect_list)
        # expect hitstop, blockstun, landing recovery etc to be replaced by values from InitValues
        self.assertEqual(0, len(result.additional_chunks))
        expected_frame_chunks = [WaitFrames(4),
                                 ActiveFrames(1, info=AttackInfo(500, 50, 60, 99, False, 2, 1, 10, 11, 0,
                                                                 normal_hit=HitEffects(90, 91))),
                                 WaitFrames(4)]
        self.assertItemsEqual(expected_frame_chunks, result.frame_chunks)
        self.assertEqual(init.landingRecovery, result.landing_recovery)

    def test_simulate_projectile_using_subroutine(self):
        chunks = [WaitFrames(4), SubroutineCall("Shot"), WaitFrames(12)]
        shot = Move()
        shot.frame_chunks = [SubroutineCall("ShotInit"), WaitFrames(4),
                             ActiveFrames(2, info=AttackInfo(500, 50, 60, 0, False))]
        shot_init = Subroutine()
        shot_init.attackInfo.normalHitEffects.hitstun = 0
        shot_init.attackInfo.normalHitEffects.untech = 0
        shot_init.attackInfo.hitstop = 1
        shot_init.attackInfo.blockstun = 2
        shot_init.attackInfo.bonusBlockstop = 3
        shot_init.attackInfo.bonusHitstop = 4
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
                                 ActiveFrames(2, info=AttackInfo(500, 50, 60, 15, False, 2, 1, 3, 4,
                                                                 normal_hit=HitEffects(hitstun=0, untech=0)))
                                 ]
        self.assertItemsEqual(result.additional_chunks[0], expected_frame_chunks)

    def test_get_blockstun_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_blockstun(), 13)

    def test_get_blockstun_custom_value(self):
        test = AttackInfo(attack_level=2, blockstun=10)
        self.assertEqual(test.get_blockstun(), 10)

    def test_get_hitstun_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_hitstun(), 14)

    def test_get_hitstun_custom_value(self):
        test = AttackInfo(attack_level=2, normal_hit=HitEffects(hitstun=10))
        self.assertEqual(test.get_hitstun(), 10)

    def test_get_hitstun_ch_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_hitstun_ch(), 18)

    def test_get_hitstun_ch_attack_level_defaults_with_fatal(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(fatal=True))
        self.assertEqual(test.get_hitstun_ch(), 21)

    def test_get_hitstun_ch_custom_value(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(hitstun=10))
        self.assertEqual(test.get_hitstun_ch(), 10)

    def test_get_hitstun_ch_custom_value_with_fatal(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(hitstun=10, fatal=True))
        self.assertEqual(test.get_hitstun_ch(), 13)

    def test_get_hitstop_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_hitstop(), 10)

    def test_get_hitstop_custom_value(self):
        test = AttackInfo(attack_level=2, hitstop=15)
        self.assertEqual(test.get_hitstop(), 15)

    def test_get_untech_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_untech(), 14)

    def test_get_untech_custom_value(self):
        test = AttackInfo(attack_level=2, normal_hit=HitEffects(untech=10))
        self.assertEqual(test.get_untech(), 10)

    def test_get_untech_ch_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_untech_ch(), 26)

    def test_get_untech_ch_attack_level_defaults_with_fatal(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(fatal=True))
        self.assertEqual(test.get_untech_ch(), 29)

    def test_get_untech_ch_custom_value(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(untech=10))
        self.assertEqual(test.get_untech_ch(), 10)

    def test_get_untech_ch_custom_value_with_fatal(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(untech=10, fatal=True))
        self.assertEqual(test.get_untech_ch(), 13)

    def test_get_stagger_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_stagger(), 24)

    def test_get_stagger_custom_value(self):
        test = AttackInfo(attack_level=2, normal_hit=HitEffects(stagger=50))
        self.assertEqual(test.get_stagger(), 50)

    def test_get_stagger_ch_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_stagger_ch(), 48)

    def test_get_stagger_ch_custom_value(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(stagger=30))
        self.assertEqual(test.get_stagger_ch(), 30)

    def test_get_crumple_start_attack_level_defaults(self):
        test = AttackInfo(attack_level=4)
        self.assertEqual(test.get_stagger_fall_start(), 39)

    def test_get_crumple_start_custom_value(self):
        test = AttackInfo(attack_level=2, normal_hit=HitEffects(stagger_fall_start=50))
        self.assertEqual(test.get_stagger_fall_start(), 50)

    def test_get_crumple_start_ch_attack_level_defaults(self):
        test = AttackInfo(attack_level=4)
        self.assertEqual(test.get_stagger_fall_start_ch(), 58)

    def test_get_crumple_start_ch_normal_stagger_custom_value(self):
        test = AttackInfo(normal_hit=HitEffects(stagger_fall_start=30))
        self.assertEqual(test.get_stagger_fall_start_ch(), 45)

    def test_get_crumple_start_ch_custom_value(self):
        test = AttackInfo(attack_level=2, counter_hit=HitEffects(stagger_fall_start=30))
        self.assertEqual(test.get_stagger_fall_start_ch(), 30)

    def test_get_p1_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_p1(), 100)

    def test_get_p1_custom_value(self):
        test = AttackInfo(attack_level=2, p1=70)
        self.assertEqual(test.get_p1(), 70)

    def test_get_p2_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_p2(), 75)

    def test_get_p2_custom_value(self):
        test = AttackInfo(attack_level=2, p2=70)
        self.assertEqual(test.get_p2(), 70)

    def test_get_damage_attack_level_defaults(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual(test.get_damage(), 1000)

    def test_get_damage_custom_value(self):
        test = AttackInfo(attack_level=2, damage=700)
        self.assertEqual(test.get_damage(), 700)

    def test_attack_info_override_non_none_values_all_values_are_non_none(self):
        first = AttackInfo()
        second = AttackInfo(100, 90, 80, 10, True, 5, 1, 1, 1, 2, [True, False, False, False, False],
                            HitEffects(), HitEffects(), 1)
        first.override_non_none_values(second)
        self.assertEqual(first, second)

    def test_attack_info_override_non_none_values_all_values_are_none(self):
        first = AttackInfo(100, 90, 80, 10, True, 5, 1, 1, 1, 2, [True, False, False, False, False],
                           HitEffects(), HitEffects(), 1)
        second = AttackInfo(min_damage=None)
        first.override_non_none_values(second)
        expected = AttackInfo(100, 90, 80, 10, True, 5, 1, 1, 1, 2, [True, False, False, False, False],
                              HitEffects(), HitEffects(), 1)
        self.assertEqual(first, expected)

    def test_hit_effect_override_non_none_values_all_values_are_non_none(self):
        first = HitEffects()
        second = HitEffects(10, 10, 1, 1, 10, 10, 10, 10, 10, 10, 1, 10, 10, 10, True)
        first.override_non_none_values(second)
        self.assertEqual(first, second)

    def test_hit_effect_override_non_none_values_all_values_are_none(self):
        first = HitEffects(10, 10, 1, 1, 10, 10, 10, 10, 10, 10, 1, 10, 10, 10, True)
        second = HitEffects()
        first.override_non_none_values(second)
        expected = HitEffects(10, 10, 1, 1, 10, 10, 10, 10, 10, 10, 1, 10, 10, 10, True)
        self.assertEqual(first, expected)

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
            self.compare_frame_chunks_util(first.additional_chunks[i], second.additional_chunks[i],
                                           "move.additonal_chunks[" + str(i) + "]")

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
        self.assertEqual(first.attackLevel, second.attackLevel, "attackLevel not equal")
        self.assertEqual(first.hitstop, second.hitstop, "hitstop not equal")
        self.assertEqual(first.bonusHitstop, second.bonusHitstop, "bonusHitstop not equal")
        self.assertEqual(first.bonusHitstopCH, second.bonusHitstopCH, "bonusHitstopCH not equal")
        self.assertEqual(first.attribute, second.attribute, "attribute not equal")
        self.compare_hit_effect(first.normalHitEffects, second.normalHitEffects)
        self.compare_hit_effect(first.counterHitEffects, second.counterHitEffects)

    def compare_hit_effect(self, first, second):
        self.assertEqual(first.hitstun, second.hitstun, "hitstun not equal")
        self.assertEqual(first.untech, second.untech, "untech not equal")
        self.assertEqual(first.groundHitAni, second.groundHitAni, "groundHitAni not equal")
        self.assertEqual(first.airHitAni, second.airHitAni, "airHitAni not equal")
        self.assertEqual(first.knockdown, second.knockdown, "knockdown not equal")
        self.assertEqual(first.slide, second.slide, "slide not equal")
        self.assertEqual(first.hitstunAfterWallBounce, second.hitstunAfterWallBounce,
                         "hitstunAfterWallBounce not equal")
        self.assertEqual(first.cornerStick, second.cornerStick, "cornerStick not equal")
        self.assertEqual(first.stagger, second.stagger, "stagger not equal")
        self.assertEqual(first.staggerFallStart, second.staggerFallStart, "crumpleStart not equal")
        self.assertEqual(first.groundBounce, second.groundBounce, "groundBounce not equal")
        self.assertEqual(first.wallBounce, second.wallBounce, "wallBounce not equal")
        self.assertEqual(first.fatal, second.fatal, "fatal not equal")
