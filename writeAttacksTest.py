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

    def test_create_basic_text_one_value(self):
        test = ["a"]
        self.assertEqual("a", create_basic_text(test))

    def test_create_basic_two_same_value(self):
        test = ["a", "a"]
        self.assertEqual("a", create_basic_text(test))

    def test_create_basic_two_different_value(self):
        test = ["a", "b"]
        self.assertEqual("a, b", create_basic_text(test))

    def test_create_basic_two_same_two_different_values(self):
        test = ["a", "a", "b", "b"]
        self.assertEqual("a*2, b*2", create_basic_text(test))

    def test_create_p2_value_attack_level_default(self):
        test = AttackInfo(attack_level=3)
        self.assertEqual("80", create_p2_value(test))

    def test_create_p2_value_attack_level_default_p2_once(self):
        test = AttackInfo(attack_level=3, p2once=True)
        self.assertEqual("80 (Once)", create_p2_value(test))

    def test_create_p2_value_custom_p2(self):
        test = AttackInfo(p2=33)
        self.assertEqual("33", create_p2_value(test))

    def test_create_p2_value_custom_p2_and_p2_once(self):
        test = AttackInfo(p2=33, p2once=True)
        self.assertEqual("33 (Once)", create_p2_value(test))

    def test_create_blockstop_value_attack_level_default(self):
        test = AttackInfo(attack_level=5)
        self.assertEqual("13", create_blockstop_value(test))

    def test_create_blockstop_value_attack_level_default_with_positive_bonus_blockstop(self):
        test = AttackInfo(attack_level=5, bonus_blockstop=5)
        self.assertEqual("13/+5", create_blockstop_value(test))

    def test_create_blockstop_value_attack_level_default_with_negative_bonus_blockstop(self):
        test = AttackInfo(attack_level=5, bonus_blockstop=-4)
        self.assertEqual("13/-4", create_blockstop_value(test))

    def test_create_bonus_hitstop_value_none(self):
        test = AttackInfo()
        self.assertEqual("", create_bonus_hitstop_value(test))

    def test_create_bonus_hitstop_value_attack_level_default(self):
        test = AttackInfo(attack_level=1)
        self.assertEqual("+0", create_bonus_hitstop_value(test))

    def test_create_bonus_hitstop_value_attack_level_default_with_positive_bonus_blockstop(self):
        test = AttackInfo(bonus_hitstop=5)
        self.assertEqual("+5", create_bonus_hitstop_value(test))

    def test_create_bonus_hitstop_value_attack_level_default_with_negative_bonus_blockstop(self):
        test = AttackInfo(bonus_hitstop=-4)
        self.assertEqual("-4", create_bonus_hitstop_value(test))

    def test_create_bonus_hitstop_ch_value_attack_level_default(self):
        test = AttackInfo(attack_level=2)
        self.assertEqual("+1", create_bonus_hitstop_ch_value(test))

    def test_create_bonus_hitstop_ch_value_attack_level_default_with_positive_bonus_blockstop(self):
        test = AttackInfo(bonus_counterhitstop=5)
        self.assertEqual("+5", create_bonus_hitstop_ch_value(test))

    def test_create_bonus_hitstop_ch_value_attack_level_default_with_zero_bonus_blockstop(self):
        test = AttackInfo(bonus_counterhitstop=0)
        self.assertEqual("+0", create_bonus_hitstop_ch_value(test))

    def test_create_bonus_hitstop_ch_value_attack_level_default_with_negative_bonus_blockstop(self):
        test = AttackInfo(bonus_counterhitstop=-4)
        self.assertEqual("-4", create_bonus_hitstop_ch_value(test))

    def test_get_hitstun_basic_text(self):
        info = AttackInfo()
        info.normalHitEffects.hitstun = 10
        self.assertEqual("10", create_hitstun_value(info))

    def test_get_hitstun_spinFall_text(self):
        info = AttackInfo()
        info.normalHitEffects.hitstun = 10
        info.normalHitEffects.groundHitAni = 6
        self.assertEqual("Spin Fall 26", create_hitstun_value(info))

    def test_get_hitstun_stagger_text(self):
        info = AttackInfo()
        info.normalHitEffects.stagger = 15
        info.normalHitEffects.groundHitAni = 2
        self.assertEqual("Stagger 15", create_hitstun_value(info))

    def test_get_hitstun_launch_text(self):
        info = AttackInfo()
        info.normalHitEffects.groundHitAni = 10
        self.assertEqual("Launch", create_hitstun_value(info))

    def test_get_hitstun_ch_basic_text(self):
        info = AttackInfo()
        info.counterHitEffects.hitstun = 10
        self.assertEqual("10", create_hitstun_ch_value(info))

    def test_get_hitstun_ch_spinFall_text(self):
        info = AttackInfo()
        info.counterHitEffects.hitstun = 10
        info.counterHitEffects.groundHitAni = 6
        self.assertEqual("Spin Fall 26", create_hitstun_ch_value(info))

    def test_get_hitstun_ch_stagger_text(self):
        info = AttackInfo()
        info.counterHitEffects.stagger = 15
        info.counterHitEffects.groundHitAni = 2
        self.assertEqual("Stagger 15", create_hitstun_ch_value(info))

    def test_get_hitstun_ch_launch_text(self):
        info = AttackInfo()
        info.counterHitEffects.groundHitAni = 10
        self.assertEqual("Launch", create_hitstun_ch_value(info))

    def test_get_untech_basic_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        self.assertEqual("10", create_untech_value(info))

    def test_get_untech_with_wallbounce_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.wallBounce = 0
        self.assertEqual("10 + WBounce", create_untech_value(info))

        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.wallBounce = 10
        self.assertEqual("10 + WBounce 10", create_untech_value(info))

    def test_get_untech_with_cornerstick_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.cornerStick = 0
        self.assertEqual("10 + WStick", create_untech_value(info))

        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.cornerStick = 10
        self.assertEqual("10 + WStick 10", create_untech_value(info))

    def test_get_untech_with_knockdown_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.knockdown = 50
        self.assertEqual("10 + Down 50", create_untech_value(info))

        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.knockdown = 24
        self.assertEqual("10 + Down 24", create_untech_value(info))

    def test_get_untech_with_slide_text(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.slide = 7
        self.assertEqual("10 + Slide 7", create_untech_value(info))

    def test_get_untech_ch_basic_text(self):
        info = AttackInfo()
        info.counterHitEffects.untech = 10
        self.assertEqual("10", create_untech_ch_value(info))

    def test_get_untech_ch_with_wallbounce_text(self):
        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.wallBounce = 0
        self.assertEqual("10 + WBounce", create_untech_ch_value(info))

        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.wallBounce = 10
        self.assertEqual("10 + WBounce 10", create_untech_ch_value(info))

    def test_get_untech_ch_with_cornerstick_text(self):
        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.cornerStick = 0
        self.assertEqual("10 + WStick", create_untech_ch_value(info))

        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.cornerStick = 10
        self.assertEqual("10 + WStick 10", create_untech_ch_value(info))

    def test_get_untech_ch_with_knockdown_text(self):
        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.knockdown = 50
        self.assertEqual("10 + Down 50", create_untech_ch_value(info))

        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.knockdown = 24
        self.assertEqual("10 + Down 24", create_untech_ch_value(info))

    def test_get_untech_ch_with_slide_text(self):
        info = AttackInfo()
        info.counterHitEffects.untech = 10
        info.counterHitEffects.slide = 7
        self.assertEqual("10 + Slide 7", create_untech_ch_value(info))

    def test_get_untech_with_many_extras(self):
        info = AttackInfo()
        info.normalHitEffects.untech = 10
        info.normalHitEffects.knockdown = 50
        info.normalHitEffects.slide = 7
        info.normalHitEffects.cornerStick = 0
        self.assertEqual("10 + WStick + Slide 7 + Down 50", create_untech_value(info))

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
        self.assertEqual("H", create_attr_value(attr))

    def test_get_attr_text_B(self):
        attr = [False, True, False, False, False]
        self.assertEqual("B", create_attr_value(attr))

    def test_get_attr_text_F(self):
        attr = [False, False, True, False, False]
        self.assertEqual("F", create_attr_value(attr))

    def test_get_attr_text_P(self):
        attr = [False, False, False, True, False]
        self.assertEqual("P", create_attr_value(attr))

    def test_get_attr_text_T(self):
        attr = [False, False, False, False, True]
        self.assertEqual("T", create_attr_value(attr))

    def test_get_attr_text_HP(self):
        attr = [True, False, False, True, False]
        self.assertEqual("HP", create_attr_value(attr))

    def test_get_attr_text_HBFPT(self):
        attr = [True, True, True, True, True]
        self.assertEqual("HBFPT", create_attr_value(attr))

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
