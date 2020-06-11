import unittest
from writeAttacks import *


class TestWrite(unittest.TestCase):
    def test_damage_text_one_value(self):
        test = [AttackInfo(500)]
        self.assertEqual("500", create_damage_text(test))

    def test_damage_text_two_different_values(self):
        test = [AttackInfo(500),
                AttackInfo(600)]
        self.assertEqual("500, 600", create_damage_text(test))

    def test_damage_text_two_same_values(self):
        test = [AttackInfo(500),
                AttackInfo(500)]
        self.assertEqual("500*2", create_damage_text(test))

    def test_damage_text_two_same_then_different_values(self):
        test = [AttackInfo(500),
                AttackInfo(500),
                AttackInfo(600)]
        self.assertEqual("500*2, 600", create_damage_text(test))

    def test_p1_text_one_value(self):
        test = [AttackInfo(p1=60)]
        self.assertEqual("60", create_p1_text(test))

    def test_p1_text_two_same_value(self):
        test = [AttackInfo(p1=60),
                AttackInfo(p1=60)]
        self.assertEqual("60", create_p1_text(test))

    def test_p1_text_two_different_value(self):
        test = [AttackInfo(p1=60),
                AttackInfo(p1=80)]
        self.assertEqual("60, 80", create_p1_text(test))

    def test_p1_text_two_same_then_different_values(self):
        test = [AttackInfo(p1=60),
                AttackInfo(p1=60),
                AttackInfo(p1=80)]
        self.assertEqual("60*2, 80", create_p1_text(test))

    def test_p2_text_one_value(self):
        test = [AttackInfo(p2=80)]
        self.assertEqual("80", create_p2_text(test))

    def test_p2_text_two_same_value(self):
        test = [AttackInfo(p2=80),
                AttackInfo(p2=80)]
        self.assertEqual("80", create_p2_text(test))

    def test_p2_text_two_same_value_once(self):
        test = [AttackInfo(p2=80, p2once=True),
                AttackInfo(p2=80, p2once=True)]
        self.assertEqual("80 (Once)", create_p2_text(test))

    def test_p2_text_two_different_value(self):
        test = [AttackInfo(p2=80),
                AttackInfo(p2=92)]
        self.assertEqual("80, 92", create_p2_text(test))

    def test_p2_text_two_same_then_different_values(self):
        test = [AttackInfo(p2=80, p2once=True),
                AttackInfo(p2=80, p2once=True),
                AttackInfo(p2=92),
                AttackInfo(p2=92)]
        self.assertEqual("80 (Once)*2, 92*2", create_p2_text(test))

    def test_blockstop_text_one_value(self):
        test = [AttackInfo(hitstop=10)]
        self.assertEqual("10", create_blockstop_text(test))

    def test_blockstop_text_two_different_value(self):
        test = [AttackInfo(hitstop=10),
                AttackInfo(hitstop=5)]
        self.assertEqual("10, 5", create_blockstop_text(test))

    def test_blockstop_text_two_same_value(self):
        test = [AttackInfo(hitstop=5),
                AttackInfo(hitstop=5)]
        self.assertEqual("5", create_blockstop_text(test))

    def test_blockstop_text_two_same_one_different_value(self):
        test = [AttackInfo(hitstop=5),
                AttackInfo(hitstop=5),
                AttackInfo(hitstop=10),
                AttackInfo(hitstop=10)]
        self.assertEqual("5*2, 10*2", create_blockstop_text(test))

    def test_blockstop_text_one_value_with_bonus_blockstop(self):
        test = [AttackInfo(hitstop=10, bonus_blockstop=2)]
        self.assertEqual("10/+2", create_blockstop_text(test))

    def test_blockstop_text_two_same_value_with_bonus_blockstop_one_different_value(self):
        test = [AttackInfo(hitstop=10, bonus_blockstop=2),
                AttackInfo(hitstop=10, bonus_blockstop=2),
                AttackInfo(hitstop=10, bonus_blockstop=0)]
        self.assertEqual("10/+2*2, 10", create_blockstop_text(test))

    def test_hitstop_text_one_value(self):
        test = [AttackInfo(bonus_hitstop=2)]
        self.assertEqual("+2", create_hitstop_text(test))

    def test_hitstop_text_one_negative_value(self):
        test = [AttackInfo(bonus_hitstop=-1)]
        self.assertEqual("-1", create_hitstop_text(test))

    def test_hitstop_text_two_different_value(self):
        test = [AttackInfo(bonus_hitstop=2),
                AttackInfo(bonus_hitstop=1)]
        self.assertEqual("+2, +1", create_hitstop_text(test))

    def test_hitstop_text_two_same_value(self):
        test = [AttackInfo(bonus_hitstop=-1),
                AttackInfo(bonus_hitstop=-1)]
        self.assertEqual("-1", create_hitstop_text(test))

    def test_hitstop_text_two_same_two_different_value(self):
        test = [AttackInfo(bonus_hitstop=-1),
                AttackInfo(bonus_hitstop=-1),
                AttackInfo(bonus_hitstop=5),
                AttackInfo(bonus_hitstop=5)]
        self.assertEqual("-1*2, +5*2", create_hitstop_text(test))

    def test_hitstop_ch_text_one_value(self):
        test = [AttackInfo(bonus_counterhitstop=2)]
        self.assertEqual("+2", create_hitstop_ch_text(test))

    def test_hitstop_ch_text_one_negative_value(self):
        test = [AttackInfo(bonus_counterhitstop=-1)]
        self.assertEqual("-1", create_hitstop_ch_text(test))

    def test_hitstop_ch_text_two_different_value(self):
        test = [AttackInfo(bonus_counterhitstop=2),
                AttackInfo(bonus_counterhitstop=1)]
        self.assertEqual("+2, +1", create_hitstop_ch_text(test))

    def test_hitstop_ch_text_two_same_value(self):
        test = [AttackInfo(bonus_counterhitstop=-1),
                AttackInfo(bonus_counterhitstop=-1)]
        self.assertEqual("-1", create_hitstop_ch_text(test))

    def test_hitstop_ch_text_two_same_two_different_value(self):
        test = [AttackInfo(bonus_counterhitstop=-1),
                AttackInfo(bonus_counterhitstop=-1),
                AttackInfo(bonus_counterhitstop=5),
                AttackInfo(bonus_counterhitstop=5)]
        self.assertEqual("-1*2, +5*2", create_hitstop_ch_text(test))

    def test_attack_level_text_one_value(self):
        test = [AttackInfo(attack_level=1)]
        self.assertEqual("1", create_attack_level_text(test))

    def test_attack_level_text_two_same_value(self):
        test = [AttackInfo(attack_level=1),
                AttackInfo(attack_level=1)]
        self.assertEqual("1", create_attack_level_text(test))

    def test_attack_level_text_two_different_value(self):
        test = [AttackInfo(attack_level=1),
                AttackInfo(500, 80, 92, 0, None, attack_level=2)]
        self.assertEqual("1, 2", create_attack_level_text(test))

    def test_attack_level_text_two_same_then_different_values(self):
        test = [AttackInfo(attack_level=1),
                AttackInfo(attack_level=1),
                AttackInfo(attack_level=2),
                AttackInfo(attack_level=2)]
        self.assertEqual("1*2, 2*2", create_attack_level_text(test))

    def test_attribute_text_one_value(self):
        test = [AttackInfo(attribute=[True, False, False, False, False])]
        self.assertEqual("H", create_attribute_text(test))

    def test_attribute_text_two_same_value(self):
        test = [AttackInfo(attribute=[True, False, False, False, False]),
                AttackInfo(attribute=[True, False, False, False, False])]
        self.assertEqual("H", create_attribute_text(test))

    def test_attribute_text_two_different_value(self):
        test = [AttackInfo(attribute=[True, False, False, False, False]),
                AttackInfo(attribute=[False, False, False, False, True])]
        self.assertEqual("H, T", create_attribute_text(test))

    def test_attribute_text_two_same_then_different_values(self):
        test = [AttackInfo(attribute=[True, False, False, False, False]),
                AttackInfo(attribute=[True, False, False, False, False]),
                AttackInfo(attribute=[False, False, False, False, True]),
                AttackInfo(attribute=[False, False, False, False, True])]
        self.assertEqual("H*2, T*2", create_attribute_text(test))

    def test_hitstun_text_one_value(self):
        test = [AttackInfo(normal_hit=HitEffects(10, ground_hit_ani=0))]
        self.assertEqual("10", create_hitstun_text(test))

    def test_hitstun_text_two_same_value(self):
        test = [AttackInfo(normal_hit=HitEffects(10, ground_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(10, ground_hit_ani=0))]
        self.assertEqual("10", create_hitstun_text(test))

    def test_hitstun_text_two_different_value(self):
        test = [AttackInfo(normal_hit=HitEffects(10, ground_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(20, ground_hit_ani=0))]
        self.assertEqual("10, 20", create_hitstun_text(test))

    def test_hitstun_text_two_same_two_different_value(self):
        test = [AttackInfo(normal_hit=HitEffects(10, ground_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(10, ground_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(20, ground_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(20, ground_hit_ani=0))]
        self.assertEqual("10*2, 20*2", create_hitstun_text(test))

    def test_untech_text_one_value(self):
        test = [AttackInfo(normal_hit=HitEffects(untech=10, air_hit_ani=0))]
        self.assertEqual("10", create_untech_text(test))

    def test_untech_text_two_same_value(self):
        test = [AttackInfo(normal_hit=HitEffects(untech=10, air_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(untech=10, air_hit_ani=0))]
        self.assertEqual("10", create_untech_text(test))

    def test_untech_text_two_different_value(self):
        test = [AttackInfo(normal_hit=HitEffects(untech=10, air_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(untech=20, air_hit_ani=0))]
        self.assertEqual("10, 20", create_untech_text(test))

    def test_untech_text_two_same_two_different_value(self):
        test = [AttackInfo(normal_hit=HitEffects(untech=10, air_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(untech=10, air_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(untech=20, air_hit_ani=0)),
                AttackInfo(normal_hit=HitEffects(untech=20, air_hit_ani=0))]
        self.assertEqual("10*2, 20*2", create_untech_text(test))

    def test_get_hitstun_basic_text(self):
        info = AttackInfo()
        info.normalHitEffects.hitstun = 10
        self.assertEqual("10", get_hitstun_text(info))

    def test_get_hitstun_spinFall_text(self):
        info = AttackInfo()
        info.normalHitEffects.spinFall = 22
        info.normalHitEffects.groundHitAni = 6
        self.assertEqual("Spin Fall 22", get_hitstun_text(info))

    def test_get_hitstun_stagger_text(self):
        info = AttackInfo()
        info.normalHitEffects.stagger = 15
        self.assertEqual("Stagger 15", get_hitstun_text(info))

    def test_get_hitstun_launch_text(self):
        info = AttackInfo()
        info.normalHitEffects.groundHitAni = 10
        self.assertEqual("Launch", get_hitstun_text(info))

    def test_get_untech_basic_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        self.assertEqual("10", get_untech_text(info))

    def test_get_untech_with_wallbounce_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.wallBounce = 0
        self.assertEqual("10 + WBounce", get_untech_text(info))

        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.wallBounce = 10
        self.assertEqual("10 + WBounce 10", get_untech_text(info))

    def test_get_untech_with_cornerstick_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.cornerStick = 0
        self.assertEqual("10 + WStick", get_untech_text(info))

        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.wallBounce = 10
        self.assertEqual("10 + WBounce 10", get_untech_text(info))

    def test_get_untech_with_knockdown_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.knockdown = 50
        self.assertEqual("10 + Down 50", get_untech_text(info))

        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.knockdown = 24
        self.assertEqual("10 + Down 24", get_untech_text(info))

    def test_get_untech_with_slide_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.slide = 7
        self.assertEqual("10 + Slide 7", get_untech_text(info))

    def test_get_untech_with_many_extras(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.knockdown = 50
        info.normalHitEffects.slide = 7
        info.normalHitEffects.cornerStick = 0
        self.assertEqual("10 + WStick + Slide 7 + Down 50", get_untech_text(info))

    def test_inv_text_basic(self):
        inv_text = create_inv_text(1, 10, 1, [True, False, False, False, False], [])
        self.assertEqual("1-10 H", inv_text)

    def test_inv_text_guard(self):
        inv_text = create_inv_text(1, 10, 2, [False, False, False, True, False], [])
        self.assertEqual("1-10 P Guard", inv_text)

    def test_inv_text_with_superflash_during_inv(self):
        inv_text = create_inv_text(10, 100, 1, [True, False, False, False, False], [(20, 50)])
        self.assertEqual("10-59 H", inv_text)

    def test_inv_text_with_superflash_after_inv(self):
        inv_text = create_inv_text(10, 10, 1, [True, False, False, False, False], [(30, 50)])
        self.assertEqual("10-19 H", inv_text)

    def test_inv_text_with_superflash_before_inv(self):
        inv_text = create_inv_text(100, 10, 1, [True, False, False, False, False], [(30, 50)])
        self.assertEqual("50-59 H", inv_text)

    def test_get_attr_text_H(self):
        attr = [True, False, False, False, False]
        self.assertEqual("H", create_attr_text(attr))

    def test_get_attr_text_B(self):
        attr = [False, True, False, False, False]
        self.assertEqual("B", create_attr_text(attr))

    def test_get_attr_text_F(self):
        attr = [False, False, True, False, False]
        self.assertEqual("F", create_attr_text(attr))

    def test_get_attr_text_P(self):
        attr = [False, False, False, True, False]
        self.assertEqual("P", create_attr_text(attr))

    def test_get_attr_text_T(self):
        attr = [False, False, False, False, True]
        self.assertEqual("T", create_attr_text(attr))

    def test_get_attr_text_HP(self):
        attr = [True, False, False, True, False]
        self.assertEqual("HP", create_attr_text(attr))

    def test_get_attr_text_HBFPT(self):
        attr = [True, True, True, True, True]
        self.assertEqual("HBFPT", create_attr_text(attr))

    def test_get_inv_attr_text_H(self):
        attr = [True, False, False, False, False]
        self.assertEqual("H", create_inv_attr_text(attr))

    def test_get_inv_attr_text_B(self):
        attr = [False, True, False, False, False]
        self.assertEqual("B", create_inv_attr_text(attr))

    def test_get_inv_attr_text_F(self):
        attr = [False, False, True, False, False]
        self.assertEqual("F", create_inv_attr_text(attr))

    def test_get_inv_attr_text_P(self):
        attr = [False, False, False, True, False]
        self.assertEqual("P", create_inv_attr_text(attr))

    def test_get_inv_attr_text_T(self):
        attr = [False, False, False, False, True]
        self.assertEqual("T", create_inv_attr_text(attr))

    def test_get_inv_attr_text_HP(self):
        attr = [True, False, False, True, False]
        self.assertEqual("HP", create_inv_attr_text(attr))

    def test_get_inv_attr_text_All(self):
        attr = [True, True, True, True, True]
        self.assertEqual("All", create_inv_attr_text(attr))
