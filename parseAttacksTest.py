import unittest
import StringIO
from parseAttacks import *
from model import *


class TestParseAttackMethods(unittest.TestCase):
    def test_get_duration(self):
        self.assertEqual(15, get_duration("    sprite('null', 15)"))

    def test_parse_inv_attr_str1(self):
        values = parse_attributes("0000000000000000010000000000000001000000")
        self.assertEqual([False, False, True, False, True], values)

    def test_parse_inv_attr_str2(self):
        values = parse_attributes("0100000001000000000000000100000000000000")
        self.assertEqual([True, True, False, True, False], values)

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
        effect_list = parse_scr_file(buf, effect_list, effect_list)
        subroutine = Subroutine()
        subroutine.attackInfo.hitstop = 6
        subroutine.attackInfo.blockstun = 11
        subroutine.attackInfo.normalHitEffects.hitstun = 17
        subroutine.attackInfo.normalHitEffects.untech = 21
        subroutine.attackInfo.damage = 900
        subroutine.attackInfo.p1 = 70
        subroutine.attackInfo.p2 = 90
        subroutine.attackInfo.attackLevel = 1
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
        move_list = parse_scr_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(None, attack_level=3, blockstun=10, hitstop=10, p2once=None,
                                                                 attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects()
                                                                 )),
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
        move_list = parse_scr_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),

                                 ActiveFrames(2,
                                              info=AttackInfo(None, attack_level=3,
                                                              attribute=[False, True, False, False, False],
                                                              normal_hit=HitEffects())
                                              ),
                                 ActiveFrames(3,
                                              info=AttackInfo(None, attack_level=3,
                                                              attribute=[False, True, False, False, False],
                                                              normal_hit=HitEffects())
                                              ),
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
        move_list = parse_scr_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(None, attack_level=3,
                                                                 attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects())
                                              ),
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
        move_list = parse_scr_file(buf, {}, {})
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
        move_list = parse_scr_file(buf, {}, {})
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
        move_list = parse_scr_file(buf, {}, {})
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
        move_list = parse_scr_file(buf, {}, {})
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
        move_list = parse_scr_file(buf, {}, {})
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
        move_list = parse_scr_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(500, attack_level=3,
                                                                 attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects())
                                              ),
                                 WaitFrames(3),
                                 ActiveFrames(5,
                                              info=AttackInfo(1000, attack_level=3,
                                                              attribute=[False, True, False, False, False],
                                                              normal_hit=HitEffects())
                                              ),
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
        move_list = parse_scr_file(buf, {}, {})
        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(500, attack_level=3, p1=50, p2=75, p2once=True,
                                                                 attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects())
                                              ),
                                 WaitFrames(3),
                                 ActiveFrames(5,
                                              info=AttackInfo(1000, attack_level=3, p1=80, p2=75, p2once=True,
                                                              attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects())
                                              ),
                                 ActiveFrames(1,
                                              info=AttackInfo(1000, attack_level=3, p1=55, p2=15, p2once=True,
                                                              attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects())
                                              ),
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
        move_list = parse_scr_file(buf, move_list, effect_list)
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
        move_list = parse_scr_file(buf, move_list, effect_list)

        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(900, 70, 90, 0, None, 11, 6,
                                                                 attack_level=1,
                                                                 attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects(hitstun=17,
                                                                                       untech=21)
                                                                 )),
                                 WaitFrames(9)
                                 ]
        self.assertEqual(expected, move_list["NmlAtk5X"])

    def test_parse_attack_with_subroutine_in_immediate_that_does_nothing(self):
        state = """@Subroutine
        def Init_AtkData():
            Unknown7009(1)
            Unknown7009(1)
            Unknown7009(1)
            Unknown7009(1)
            
        @State
        def NmlAtk5X():

            def upon_IMMEDIATE():
                AttackDefaults_StandingNormal()
                AttackLevel_(1)
                AttackP1(70)
                AttackP2(90)
                Damage(500)
                Hitstop(6)
                Unknown9154(17)
                AirUntechableTime(21)
                GroundedHitstunAnimation(5)
                Unknown11028(11)
                Unknown9016(1)
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
        move_list = parse_scr_file(buf, move_list, effect_list)

        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5X" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(7),
                                 ActiveFrames(5, info=AttackInfo(900, 70, 90, 0, None, 11, 6,
                                                                 attack_level=1,
                                                                 attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects(ground_hit_ani=5,
                                                                                       hitstun=17,
                                                                                       untech=21),
                                                                 counter_hit=HitEffects()
                                                                 )),
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
        move_list = parse_scr_file(buf, move_list, effect_list)

        self.assertEqual(len(move_list), 1)
        self.assertTrue("NmlAtk5A" in move_list)
        expected = Move()
        expected.frame_chunks = [WaitFrames(6),
                                 ActiveFrames(2,
                                              info=AttackInfo(None, attack_level=2,
                                                              attribute=[False, True, False, False, False],
                                                                 normal_hit=HitEffects())
                                              ),
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
        move_list = parse_scr_file(buf, move_list, effect_list)

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
        move_list = parse_scr_file(buf, move_list, effect_list)
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
        move_list = parse_scr_file(buf, move_list, effect_list)
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
        effect_list = parse_scr_file(buf, effect_list, effect_list)
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
        move_list = parse_scr_file(buf, move_list, effect_list)
        hit_simulations = simulate_on_block(move_list, effect_list)
        expected = AttackInfo(900, p1=70, attack_level=1,
                              attribute=[False, True, False, False, False],
                              normal_hit=HitEffects())
        self.assertEqual(expected, hit_simulations["NmlAtk5A"].frame_chunks[1].info)

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
        move_list = parse_scr_file(buf, move_list, effect_list)
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
        move_list = parse_scr_file(buf, move_list, effect_list)
        atk = move_list["atk"]
        self.assertIsNotNone(atk)
        self.assertEquals(1, len(atk.hardcoded_inv_list))
        inv_values = atk.hardcoded_inv_list[0]
        self.assertEqual(3, inv_values[0])
        self.assertEqual(5, inv_values[1])
        self.assertEqual(1, inv_values[2])
        self.assertEqual([True, True, True, True, False], inv_values[3])
