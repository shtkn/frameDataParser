@Subroutine
def AtkEffLightningHitmark():

    def upon_78():
        GFX_0('EffAtk_LightningM', 101)

    def upon_82():
        GFX_0('EffAtk_LightningM', 101)

@Subroutine
def AtkEffLightning():

    def upon_78():
        Unknown13(10)
        GFX_0('electshot_eff', 100)
        Unknown38(10, 1)
        Unknown23029(10, 0, 0)

    def upon_82():
        Unknown13(11)
        GFX_0('electshot_eff', 100)
        Unknown38(11, 1)
        Unknown23029(11, 1, 0)

@State
def electshot_eff():

    def upon_IMMEDIATE():
        Unknown2037(2)
        Unknown2019(-500)

        def upon_43():
            if (SLOT_48 == 0):
                sendToLabel(0)
            if (SLOT_48 == 1):
                SLOT_51 = 1
                sendToLabel(1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                Unknown1086(23)
            else:
                Unknown1086(22)
            Unknown1007(200000)
    sprite('null', 10)	# 1-10
    loopRest()
    ExitState()
    label(0)
    sprite('Action_130_00', 3)	# 11-13
    Unknown2038(-1)
    sprite('Action_130_01', 3)	# 14-16
    sprite('Action_130_02', 3)	# 17-19
    sprite('Action_130_03', 3)	# 20-22
    sprite('Action_130_04', 3)	# 23-25
    if SLOT_2:
        _gotolabel(0)
    sprite('Action_130_05', 1)	# 26-26
    ExitState()
    label(1)
    sprite('Action_130_00', 3)	# 27-29
    Unknown23151(23, 105)
    Unknown2038(-1)
    sprite('Action_130_01', 3)	# 30-32
    sprite('Action_130_02', 3)	# 33-35
    sprite('Action_130_03', 3)	# 36-38
    sprite('Action_130_04', 3)	# 39-41
    if SLOT_2:
        _gotolabel(1)
    sprite('Action_130_05', 1)	# 42-42
    ExitState()

@State
def EffAtk_LightningS():

    def upon_IMMEDIATE():
        Unknown2019(-500)

        def upon_43():
            if (SLOT_48 == 0):
                Unknown1086(22)
            if (SLOT_48 == 1):
                Unknown1086(23)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_144_00', 5)	# 1-5
    sprite('Action_144_01', 5)	# 6-10
    sprite('Action_144_02', 5)	# 11-15
    sprite('Action_144_03', 1)	# 16-16
    ExitState()
    label(1)
    sprite('Action_144_05', 5)	# 17-21
    sprite('Action_144_06', 5)	# 22-26
    sprite('Action_144_07', 5)	# 27-31
    sprite('Action_144_08', 1)	# 32-32

@State
def EffAtk_LightningM():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_145_00', 9)	# 1-9
    sprite('Action_145_01', 9)	# 10-18
    sprite('Action_145_02', 9)	# 19-27
    sprite('Action_145_03', 1)	# 28-28
    ExitState()
    label(1)
    sprite('Action_145_05', 5)	# 29-33
    sprite('Action_145_06', 5)	# 34-38
    sprite('Action_145_07', 5)	# 39-43
    sprite('Action_145_08', 1)	# 44-44

@State
def EffAtk_LightningL():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_146_00', 9)	# 1-9
    sprite('Action_146_01', 9)	# 10-18
    sprite('Action_146_02', 9)	# 19-27
    sprite('Action_146_03', 1)	# 28-28
    ExitState()
    label(1)
    sprite('Action_146_05', 9)	# 29-37
    sprite('Action_146_06', 9)	# 38-46
    sprite('Action_146_07', 9)	# 47-55
    sprite('Action_146_08', 1)	# 56-56

@State
def EffAtk_LightningLL():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_147_00', 9)	# 1-9
    sprite('Action_147_01', 9)	# 10-18
    sprite('Action_147_02', 9)	# 19-27
    sprite('Action_147_03', 1)	# 28-28
    ExitState()
    label(1)
    sprite('Action_147_05', 9)	# 29-37
    sprite('Action_147_06', 9)	# 38-46
    sprite('Action_147_07', 9)	# 47-55
    sprite('Action_147_08', 1)	# 56-56

@State
def EffNmlAtk5A2nd():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_102_00', 3)	# 1-3
    sprite('Action_102_01', 3)	# 4-6
    sprite('Action_102_02', 3)	# 7-9

@State
def EffNmlAtk5A3rd():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_101_00', 3)	# 1-3
    sprite('Action_101_01', 3)	# 4-6
    sprite('Action_101_02', 1)	# 7-7

@State
def EffNmlAtk5B():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_106_00', 4)	# 1-4
    sprite('Action_106_01', 4)	# 5-8
    sprite('Action_106_02', 4)	# 9-12
    sprite('Action_106_03', 4)	# 13-16
    sprite('Action_106_04', 1)	# 17-17

@State
def EffNmlAtkCrush():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_105_00', 3)	# 1-3
    sprite('Action_105_01', 5)	# 4-8
    sprite('Action_105_02', 5)	# 9-13
    sprite('Action_105_03', 5)	# 14-18
    sprite('Action_105_04', 1)	# 19-19

@State
def EffNmlAtkAir5B2nd():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_091_00', 3)	# 1-3
    sprite('Action_091_01', 3)	# 4-6
    sprite('Action_091_02', 3)	# 7-9
    sprite('Action_091_03', 1)	# 10-10

@State
def EffNmlAtkAir5C():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    label(0)
    sprite('Action_116_00', 3)	# 1-3
    sprite('Action_116_01', 3)	# 4-6
    sprite('Action_116_02', 3)	# 7-9
    sprite('Action_116_03', 3)	# 10-12
    sprite('Action_116_04', 3)	# 13-15
    sprite('Action_116_05', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def EffNmlAtkAir5CWind():
    sprite('Action_134_00', 3)	# 1-3
    sprite('Action_134_01', 3)	# 4-6
    sprite('Action_134_02', 3)	# 7-9
    sprite('Action_134_03', 1)	# 10-10
    loopRest()

@State
def EffNmlAtkAir5CLanding():
    sprite('Action_117_00', 3)	# 1-3
    sprite('Action_117_01', 3)	# 4-6
    sprite('Action_117_02', 3)	# 7-9
    sprite('Action_117_03', 1)	# 10-10
    loopRest()

@State
def EffThrowFinish():

    def upon_IMMEDIATE():
        Unknown23151(22, 103)
    sprite('Action_114_00', 3)	# 1-3
    sprite('Action_114_01', 3)	# 4-6
    sprite('Action_114_02', 3)	# 7-9
    sprite('Action_114_03', 3)	# 10-12
    sprite('Action_114_04', 3)	# 13-15
    sprite('Action_114_05', 1)	# 16-16

@State
def EffAirThrowAtk():

    def upon_IMMEDIATE():
        teleportRelativeX(50000)
        Unknown1007(100000)
    sprite('Action_118_00', 5)	# 1-5
    sprite('Action_118_01', 5)	# 6-10
    sprite('Action_118_02', 5)	# 11-15
    sprite('Action_118_03', 1)	# 16-16

@State
def EffOffensiveGuardStart():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown48('190000000200000033000000160000000200000024000000')
    if SLOT_51:
        _gotolabel(1)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('Action_121_00', 6)	# 2-7
    sprite('Action_121_01', 6)	# 8-13
    sprite('Action_121_02', 1)	# 14-14
    loopRest()
    ExitState()
    label(1)
    sprite('Action_123_00', 6)	# 15-20
    sprite('Action_123_01', 6)	# 21-26
    sprite('Action_123_02', 1)	# 27-27
    loopRest()
    ExitState()

@State
def EffOffensiveGuardBarier():

    def upon_IMMEDIATE():
        Unknown4010(3)

        def upon_45():
            Unknown23151(3, 0)
    sprite('Action_120_00', 5)	# 1-5
    sprite('Action_120_01', 5)	# 6-10
    sprite('Action_120_02', 5)	# 11-15
    sprite('Action_120_03', 5)	# 16-20
    sprite('Action_120_04', 5)	# 21-25
    sprite('Action_120_05', 5)	# 26-30
    sprite('Action_120_06', 5)	# 31-35

@State
def EffOffensiveGuardSuccess():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_124_00', 4)	# 1-4
    sprite('Action_124_01', 4)	# 5-8
    sprite('Action_124_02', 4)	# 9-12
    sprite('Action_124_03', 4)	# 13-16
    sprite('Action_124_04', 1)	# 17-17

@State
def EffOffensiveGuardCounter():

    def upon_IMMEDIATE():
        Unknown1007(250000)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('Action_126_00', 4)	# 2-5
    sprite('Action_126_01', 4)	# 6-9
    sprite('Action_126_02', 1)	# 10-10
    label(1)
    sprite('Action_126_04', 4)	# 11-14
    sprite('Action_126_05', 4)	# 15-18
    sprite('Action_126_06', 1)	# 19-19

@Subroutine
def ShotInit():
    Unknown2010()
    AttackLevel_(3)
    Hitstop(0)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(1)
    AirPushbackX(8000)
    AirPushbackY(18000)
    AirUntechableTime(28)
    Unknown11001(5, 5, 10)
    Unknown1097(-75)
    Unknown53(1)
    Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
    Unknown9016(1)
    callSubroutine('AtkEffLightning')
    callSubroutine('AtkEffLightningHitmark')
    if SLOT_57:
        AttackP1(70)
        AirUntechableTime(60)
        Unknown11042(1)
    if SLOT_58:
        Damage(1000)
        AirPushbackX(15000)
        AirPushbackY(12000)
        Unknown30065(0)
        MinimumDamagePct(10)

    def upon_12():
        if Unknown23148('EffShotA'):
            GFX_0('EffShotHitMark', 101)
        if Unknown23148('EffShotB'):
            GFX_0('EffShotHitMark', 101)
        if Unknown23148('EffShotEx'):
            GFX_0('EffShotHitMarkEx', 101)
        if Unknown23148('EffShotEx_LastShot'):
            SFX_3('SE205_PunchFinish')
            GFX_0('EffShotHitMarkEx', 101)
        if Unknown23148('EffAirShotA'):
            GFX_0('EffShotHitMark', 101)
        if Unknown23148('EffAirShotB'):
            GFX_0('EffShotHitMark', 101)
        if Unknown23148('EffAirShotEx'):
            GFX_0('EffShotHitMarkEx', 101)
        if Unknown23148('EffAirShotEx_LastShot'):
            SFX_3('SE205_PunchFinish')
            GFX_0('EffShotHitMarkEx', 101)

    def upon_CLEAR_OR_EXIT():
        Unknown2038(1)
        if (SLOT_2 <= 3):
            Unknown1097(50)
        if (SLOT_2 > 3):
            Unknown1097(-50)
        if (SLOT_2 > 7):
            Unknown1096(925)
            Unknown2037(0)

    def upon_LANDING():
        SFX_3('SE011')
        Unknown23090(25)
    sendToLabelUpon(54, 580)

    def upon_54():
        sendToLabel(580)
        Unknown13(4)

@State
def EffShotWind():
    sprite('Action_135_00', 3)	# 1-3
    sprite('Action_135_01', 3)	# 4-6
    sprite('Action_135_02', 3)	# 7-9
    sprite('Action_135_03', 3)	# 10-12

@State
def EffAirShotWind():
    sprite('Action_136_00', 3)	# 1-3
    sprite('Action_136_01', 3)	# 4-6
    sprite('Action_136_02', 3)	# 7-9
    sprite('Action_136_03', 3)	# 10-12

@State
def EffShotHitMark():
    sprite('Action_167_00', 3)	# 1-3
    sprite('Action_167_01', 3)	# 4-6
    sprite('Action_167_02', 3)	# 7-9
    sprite('Action_167_03', 3)	# 10-12
    sprite('Action_167_04', 3)	# 13-15
    sprite('Action_167_05', 3)	# 16-18
    sprite('Action_167_06', 1)	# 19-19

@State
def EffShotHitMarkEx():
    sprite('Action_169_00', 3)	# 1-3
    sprite('Action_169_01', 3)	# 4-6
    sprite('Action_169_02', 3)	# 7-9
    sprite('Action_169_03', 3)	# 10-12
    sprite('Action_169_04', 3)	# 13-15
    sprite('Action_169_05', 1)	# 16-16

@State
def EffShotFragment():

    def upon_IMMEDIATE():
        Unknown4013(2)
    sprite('null', 1)	# 1-1
    random_(2, 0, 33)
    if SLOT_ReturnVal:
        _gotolabel(2)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(3)
    label(1)
    sprite('Action_166_00', 3)	# 2-4
    teleportRelativeX(-20000)
    sprite('Action_166_01', 3)	# 5-7
    sprite('Action_166_02', 3)	# 8-10
    ExitState()
    label(2)
    sprite('Action_166_04', 3)	# 11-13
    teleportRelativeX(120000)
    sprite('Action_166_05', 3)	# 14-16
    sprite('Action_166_06', 3)	# 17-19
    ExitState()
    label(3)
    sprite('Action_166_08', 3)	# 20-22
    teleportRelativeX(120000)
    if random_(2, 0, 50):
        teleportRelativeX(-140000)
    sprite('Action_166_09', 3)	# 23-25
    sprite('Action_166_10', 3)	# 26-28
    ExitState()

@State
def EffAirShotFragment():

    def upon_IMMEDIATE():
        Unknown4013(2)
    sprite('null', 1)	# 1-1
    random_(2, 0, 33)
    if SLOT_ReturnVal:
        _gotolabel(2)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(3)
    label(1)
    sprite('Action_166_00', 3)	# 2-4
    teleportRelativeX(-10000)
    Unknown1007(20000)
    sprite('Action_166_01', 3)	# 5-7
    sprite('Action_166_02', 3)	# 8-10
    ExitState()
    label(2)
    sprite('Action_166_04', 3)	# 11-13
    teleportRelativeX(50000)
    Unknown1007(-50000)
    sprite('Action_166_05', 3)	# 14-16
    sprite('Action_166_06', 3)	# 17-19
    ExitState()
    label(3)
    sprite('Action_166_08', 3)	# 20-22
    teleportRelativeX(50000)
    Unknown1007(-50000)
    if random_(2, 0, 50):
        teleportRelativeX(-60000)
        Unknown1007(70000)
    sprite('Action_166_09', 3)	# 23-25
    sprite('Action_166_10', 3)	# 26-28
    ExitState()

@State
def Shot_Atkdmycol():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    sprite('Action_177_01ex02', 2)	# 1-2
    sprite('Action_177_02ex02', 32767)	# 3-32769

@State
def EffShotA():

    def upon_IMMEDIATE():
        callSubroutine('ShotInit')
    sprite('Action_177_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(25000)
    SFX_3('SE220')
    sprite('Action_177_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    GFX_0('Shot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_177_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_177_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_177_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_177_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_177_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_177_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_177_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_177_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_177_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_177_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_177_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_177_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_177_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_177_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_177_16', 1)	# 36-36	 **attackbox here**

@State
def EffShotB():

    def upon_IMMEDIATE():
        callSubroutine('ShotInit')
    sprite('Action_178_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(50000)
    SFX_3('SE220')
    sprite('Action_178_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    GFX_0('Shot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_178_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_178_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_178_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_178_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_178_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_178_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_178_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_178_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_178_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_178_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_178_16', 1)	# 36-36	 **attackbox here**

@State
def EffShotExMaster():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('null', 5)	# 1-5
    GFX_0('EffShotEx', 100)
    Unknown36(1)
    Unknown2019(-1000)
    Unknown35()
    sprite('null', 5)	# 6-10
    GFX_0('EffShotEx', 100)
    Unknown36(1)
    Unknown2019(-1001)
    Unknown35()
    sprite('null', 5)	# 11-15
    GFX_0('EffShotEx', 100)
    Unknown36(1)
    Unknown2019(-1002)
    Unknown35()
    sprite('null', 5)	# 16-20
    GFX_0('EffShotEx_LastShot', 100)
    Unknown36(1)
    Unknown2019(-1003)
    Unknown35()

@State
def EffShotEx():

    def upon_IMMEDIATE():
        SLOT_58 = 1
        callSubroutine('ShotInit')
    sprite('Action_164_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(25000)
    SFX_3('SE220')
    sprite('Action_164_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    GFX_0('Shot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_164_02ex01', 2)	# 5-6	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_164_03ex01', 2)	# 7-8	 **attackbox here**
    sprite('Action_164_04ex01', 2)	# 9-10	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_164_05ex01', 2)	# 11-12	 **attackbox here**
    sprite('Action_164_06ex01', 2)	# 13-14	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    label(0)
    sprite('Action_164_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_164_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_164_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_164_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_164_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_164_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_164_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_164_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_164_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_164_16', 1)	# 36-36	 **attackbox here**

@State
def EffShotEx_LastShot():

    def upon_IMMEDIATE():
        SLOT_58 = 1
        callSubroutine('ShotInit')
    sprite('Action_165_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(25000)
    SFX_3('SE220')
    sprite('Action_165_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    GFX_0('Shot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_165_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_165_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_165_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_165_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_165_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_165_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_165_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_165_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_165_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_165_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_165_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_165_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_165_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_165_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_165_16', 1)	# 36-36	 **attackbox here**

@State
def EffShotAssist():

    def upon_IMMEDIATE():
        SLOT_57 = 1
        callSubroutine('ShotInit')
    sprite('Action_178_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(50000)
    SFX_3('SE220')
    sprite('Action_178_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    GFX_0('Shot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_178_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_178_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_178_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_178_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_178_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_178_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    sprite('Action_178_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_178_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_178_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_178_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_178_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_178_16', 1)	# 36-36	 **attackbox here**

@State
def AirShot_Atkdmycol():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    sprite('Action_175_01ex02', 2)	# 1-2
    sprite('Action_175_02ex02', 32767)	# 3-32769

@State
def EffAirShotA():

    def upon_IMMEDIATE():
        callSubroutine('ShotInit')
    sprite('Action_175_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(-13500)
    SFX_3('SE220')
    sprite('Action_175_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    GFX_0('AirShot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_175_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_175_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_175_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_175_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_175_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_175_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_175_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_175_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_175_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_175_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_175_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_175_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_175_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_175_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_175_16', 1)	# 36-36	 **attackbox here**

@State
def EffAirShotB():

    def upon_IMMEDIATE():
        callSubroutine('ShotInit')
    sprite('Action_176_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(15000)
    physicsYImpulse(-20250)
    SFX_3('SE220')
    sprite('Action_176_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    GFX_0('AirShot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_176_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_176_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_176_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_176_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_176_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_176_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_176_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_176_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_176_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_176_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_176_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_176_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_176_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_176_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_176_16', 1)	# 36-36	 **attackbox here**

@State
def EffAirShotExMaster():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('null', 5)	# 1-5
    GFX_0('EffAirShotEx', 100)
    Unknown36(1)
    Unknown2019(-1000)
    Unknown35()
    sprite('null', 5)	# 6-10
    GFX_0('EffAirShotEx', 100)
    Unknown36(1)
    Unknown2019(-1001)
    Unknown35()
    sprite('null', 5)	# 11-15
    GFX_0('EffAirShotEx', 100)
    Unknown36(1)
    Unknown2019(-1002)
    Unknown35()
    sprite('null', 5)	# 16-20
    GFX_0('EffAirShotEx_LastShot', 100)
    Unknown36(1)
    Unknown2019(-1003)
    Unknown35()

@State
def EffAirShotEx():

    def upon_IMMEDIATE():
        SLOT_58 = 1
        callSubroutine('ShotInit')
    sprite('Action_195_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(-13500)
    SFX_3('SE220')
    sprite('Action_195_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    GFX_0('AirShot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_195_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_195_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_195_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_195_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_195_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_195_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_195_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_195_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_195_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_195_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_195_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_195_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_195_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_195_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_195_16', 1)	# 36-36	 **attackbox here**

@State
def EffAirShotEx_LastShot():

    def upon_IMMEDIATE():
        SLOT_58 = 1
        callSubroutine('ShotInit')
    sprite('Action_196_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(-13500)
    SFX_3('SE220')
    sprite('Action_196_01ex01', 2)	# 3-4	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    GFX_0('AirShot_Atkdmycol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    sprite('Action_196_02ex01', 2)	# 5-6	 **attackbox here**
    sprite('Action_196_03ex01', 2)	# 7-8	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_196_04ex01', 2)	# 9-10	 **attackbox here**
    sprite('Action_196_05ex01', 2)	# 11-12	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_196_06ex01', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('Action_196_07ex01', 2)	# 15-16	 **attackbox here**
    sprite('Action_196_08ex01', 2)	# 17-18	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_196_09ex01', 2)	# 19-20	 **attackbox here**
    sprite('Action_196_10ex01', 2)	# 21-22	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    sprite('Action_196_11ex01', 2)	# 23-24	 **attackbox here**
    sprite('Action_196_12ex01', 2)	# 25-26	 **attackbox here**
    GFX_0('EffAirShotFragment', 100)
    gotoLabel(0)
    label(580)
    sprite('Action_196_13', 3)	# 27-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_196_14', 3)	# 30-32	 **attackbox here**
    sprite('Action_196_15', 3)	# 33-35	 **attackbox here**
    sprite('Action_196_16', 1)	# 36-36	 **attackbox here**

@State
def EffAssault1st():

    def upon_IMMEDIATE():
        teleportRelativeX(30000)
    sprite('Action_107_00', 3)	# 1-3
    sprite('Action_107_01', 3)	# 4-6
    sprite('Action_107_02', 3)	# 7-9
    sprite('Action_107_03', 1)	# 10-10

@State
def EffAssault2nd():

    def upon_IMMEDIATE():
        teleportRelativeX(30000)
    sprite('Action_108_00', 3)	# 1-3
    sprite('Action_108_01', 3)	# 4-6
    sprite('Action_108_02', 3)	# 7-9
    sprite('Action_108_03', 1)	# 10-10

@State
def EffAssault3rd():

    def upon_IMMEDIATE():
        teleportRelativeX(30000)
    sprite('Action_109_00', 3)	# 1-3
    sprite('Action_109_01', 3)	# 4-6
    sprite('Action_109_02', 3)	# 7-9
    sprite('Action_109_03', 1)	# 10-10

@State
def EffAssaultExStart():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('Action_140_00', 3)	# 1-3
    sprite('Action_140_01', 3)	# 4-6
    sprite('Action_140_02', 3)	# 7-9
    sprite('Action_140_03', 3)	# 10-12
    sprite('Action_140_04', 3)	# 13-15
    sprite('Action_140_05', 1)	# 16-16

@State
def EffAssaultExFinish():

    def upon_IMMEDIATE():
        teleportRelativeX(30000)
        Unknown1007(300000)
    sprite('Action_110_00', 4)	# 1-4
    sprite('Action_110_01', 4)	# 5-8
    sprite('Action_110_02', 4)	# 9-12
    sprite('Action_110_03', 1)	# 13-13

@State
def EffAssaultExBody():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_132_00', 3)	# 1-3
    sprite('Action_132_01', 3)	# 4-6
    sprite('Action_132_02', 3)	# 7-9
    sprite('Action_132_03', 3)	# 10-12

@State
def EffAntiAir1stAtk():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_111_00', 3)	# 1-3
    sprite('Action_111_01', 3)	# 4-6
    sprite('Action_111_02', 1)	# 7-7

@State
def EffAntiAirJumpBeginWind():
    sprite('Action_133_00', 3)	# 1-3
    sprite('Action_133_01', 3)	# 4-6
    sprite('Action_133_02', 3)	# 7-9
    sprite('Action_133_03', 1)	# 10-10

@State
def EffAntiAirJumpBeginImpact():
    sprite('Action_137_00', 3)	# 1-3
    sprite('Action_137_01', 3)	# 4-6
    sprite('Action_137_02', 1)	# 7-7

@State
def DS_testEff():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(5000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(50000)
        AirPushbackY(-30000)
        Unknown9118(10)
        Unknown9190(1)
        callSubroutine('AtkEffLightning')
        Unknown11050('0200000045666641746b5f4c696768746e696e674c000000000000000000000000000000')
        Unknown2003(1)
    sprite('Action_237_01', 4)	# 1-4	 **attackbox here**
    teleportRelativeX(250000)
    sprite('Action_237_02', 4)	# 5-8
    sprite('Action_237_03', 4)	# 9-12
    sprite('Action_237_04', 4)	# 13-16
    sprite('Action_237_05', 4)	# 17-20
    sprite('Action_237_06', 4)	# 21-24

@State
def DStestAtkEff():

    def upon_IMMEDIATE():
        pass
    sprite('Action_091_00', 9)	# 1-9
    sprite('Action_091_01', 9)	# 10-18
    sprite('Action_091_02', 9)	# 19-27
    sprite('Action_091_03', 1)	# 28-28

@State
def DStestShockWave():

    def upon_IMMEDIATE():
        Unknown1064(500)
        physicsXImpulse(28000)
    sprite('Action_235_00', 4)	# 1-4
    sprite('Action_235_01', 4)	# 5-8
    sprite('Action_235_02', 4)	# 9-12
    sprite('Action_235_03', 4)	# 13-16
    sprite('Action_235_04', 4)	# 17-20
    sprite('Action_235_05', 1)	# 21-21

@State
def EffKamiKaze1stAtk():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(250000)
    sprite('Action_218_00', 3)	# 1-3
    sprite('Action_218_01', 3)	# 4-6
    sprite('Action_218_02', 3)	# 7-9
    sprite('Action_218_03', 3)	# 10-12
    sprite('Action_218_04', 3)	# 13-15
    sprite('Action_218_05', 1)	# 16-16

@State
def EffKamiKazeSpeedLine():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_214_00', 4)	# 1-4
    sprite('Action_214_01', 4)	# 5-8
    sprite('Action_214_02', 4)	# 9-12
    sprite('Action_214_03', 4)	# 13-16
    sprite('Action_214_04', 5)	# 17-21
    sprite('Action_214_05', 5)	# 22-26
    sprite('Action_214_06', 5)	# 27-31
    sprite('Action_214_07', 5)	# 32-36
    sprite('Action_214_08', 6)	# 37-42
    sprite('Action_214_09', 6)	# 43-48
    sprite('Action_214_10', 6)	# 49-54
    sprite('Action_214_11', 6)	# 55-60
    sprite('Action_214_12', 7)	# 61-67

@State
def EffKamiKazeSpeedLineLoopL():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    label(0)
    sprite('Action_214_00', 4)	# 1-4
    sprite('Action_214_01', 4)	# 5-8
    sprite('Action_214_02', 4)	# 9-12
    sprite('Action_214_03', 4)	# 13-16
    sprite('Action_214_04', 5)	# 17-21
    sprite('Action_214_05', 5)	# 22-26
    sprite('Action_214_06', 5)	# 27-31
    sprite('Action_214_07', 5)	# 32-36
    sprite('Action_214_08', 6)	# 37-42
    sprite('Action_214_09', 6)	# 43-48
    gotoLabel(0)

@State
def EffKamiKazeSpeedLineLoop():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    label(0)
    sprite('Action_215_00', 3)	# 1-3
    sprite('Action_215_01', 3)	# 4-6
    sprite('Action_215_02', 3)	# 7-9
    sprite('Action_215_03', 3)	# 10-12
    sprite('Action_215_04', 3)	# 13-15
    sprite('Action_215_05', 3)	# 16-18
    sprite('Action_215_06', 3)	# 19-21
    sprite('Action_215_07', 3)	# 22-24
    sprite('Action_215_08', 3)	# 25-27
    sprite('Action_215_09', 3)	# 28-30
    gotoLabel(0)

@State
def EffKamiKazeBomb():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(150000)
        Unknown1007(250000)
        Unknown2019(-1000)
    sprite('Action_216_00', 2)	# 1-2
    sprite('Action_216_01', 3)	# 3-5
    sprite('Action_216_02', 3)	# 6-8
    sprite('Action_216_03', 3)	# 9-11
    sprite('Action_216_04', 3)	# 12-14
    sprite('Action_216_05', 3)	# 15-17
    sprite('Action_216_06', 3)	# 18-20
    sprite('Action_216_07', 3)	# 21-23

@State
def EffKamiKazeBomb_5AAAA():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(150000)
        Unknown1007(250000)
        Unknown2019(-1000)
    sprite('Action_216_00', 2)	# 1-2
    sprite('Action_216_01', 6)	# 3-8
    sprite('Action_216_02', 6)	# 9-14
    sprite('Action_216_03', 6)	# 15-20
    sprite('Action_216_04', 6)	# 21-26
    sprite('Action_216_05', 6)	# 27-32
    sprite('Action_216_06', 6)	# 33-38
    sprite('Action_216_07', 3)	# 39-41

@State
def KamiKazeBG():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown2008()
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-280000)
    sprite('Action_217_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_217_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_217_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_217_03', 3)	# 9-11	 **attackbox here**
    sprite('Action_217_04', 3)	# 12-14	 **attackbox here**
    sprite('Action_217_05', 3)	# 15-17	 **attackbox here**
    sprite('Action_217_06', 3)	# 18-20	 **attackbox here**
    sprite('Action_217_07', 3)	# 21-23	 **attackbox here**
    sprite('Action_217_08', 3)	# 24-26	 **attackbox here**
    sprite('Action_217_09', 3)	# 27-29	 **attackbox here**
    sprite('Action_217_10', 3)	# 30-32	 **attackbox here**
    sprite('Action_217_11', 3)	# 33-35	 **attackbox here**
    sprite('Action_217_12', 3)	# 36-38	 **attackbox here**
    sprite('Action_217_13', 3)	# 39-41	 **attackbox here**
    sprite('Action_217_14', 3)	# 42-44	 **attackbox here**
    sprite('Action_217_15', 3)	# 45-47	 **attackbox here**
    sprite('Action_217_16', 3)	# 48-50	 **attackbox here**
    sprite('Action_217_17', 3)	# 51-53	 **attackbox here**
    sprite('Action_217_18', 3)	# 54-56
    sprite('Action_217_19', 3)	# 57-59
    sprite('Action_217_20', 3)	# 60-62
    sprite('Action_217_21', 3)	# 63-65
    sprite('Action_217_22', 3)	# 66-68
    sprite('Action_217_23', 3)	# 69-71
    sprite('Action_217_24', 3)	# 72-74
    sprite('Action_217_25', 3)	# 75-77
    sprite('Action_217_26', 3)	# 78-80
    sprite('Action_217_27', 1)	# 81-81

@State
def KamikazeCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(3)
    sprite('null', 400)	# 1-400

@State
def AstralAtk_Chop_Blade():
    sprite('Action_234_00', 4)	# 1-4
    sprite('Action_234_01', 4)	# 5-8
    sprite('Action_234_02', 4)	# 9-12
    sprite('Action_234_03', 4)	# 13-16

@State
def AstralAtk_Chop_Impact():
    sprite('Action_233_00', 5)	# 1-5
    sprite('Action_233_01', 5)	# 6-10
    SFX_3('SE023')
    sprite('Action_233_02', 5)	# 11-15
    sprite('Action_233_03', 1)	# 16-16

@State
def AstralAtk_ShockWave():

    def upon_IMMEDIATE():

        def upon_CLEAR_OR_EXIT():
            Unknown2038(1)
            if (SLOT_2 >= 2):
                Unknown2037(0)
                SFX_3('SE210')
    sprite('Action_235_00', 4)	# 1-4
    sprite('Action_235_01', 4)	# 5-8
    sprite('Action_235_02', 4)	# 9-12
    sprite('Action_235_03', 4)	# 13-16
    sprite('Action_235_04', 4)	# 17-20
    sprite('Action_235_05', 1)	# 21-21

@State
def AstralAtk_HitMark():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(5000)
        PushbackX(0)
        Hitstop(0)
        Unknown11001(0, 100, 100)
        MinimumDamagePct(100)
        Unknown11064(1)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        AirPushbackX(0)
        AirPushbackY(300)
        YImpluseBeforeWallbounce(0)
        hitstun(999)
        AirUntechableTime(999)
        Unknown11086(1)
        callSubroutine('AtkEffLightning')
        Unknown11050('0200000045666641746b5f4c696768746e696e674c000000000000000000000000000000')
    sprite('null', 5)	# 1-5
    sprite('Action_237_01', 4)	# 6-9	 **attackbox here**
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('Action_237_02', 4)	# 10-13
    sprite('Action_237_03', 4)	# 14-17
    sprite('Action_237_04', 4)	# 18-21
    sprite('Action_237_05', 4)	# 22-25
    sprite('Action_237_06', 4)	# 26-29

@State
def AstralJiware():

    def upon_IMMEDIATE():
        Unknown2019(-999)
        physicsXImpulse(75000)
        loopRelated(17, 40)

        def upon_17():
            sendToLabel(580)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('null', 1)	# 2-2
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(2)
    label(1)
    sprite('null', 2)	# 3-4
    Unknown4004('6566666563745f3438340000000000000000000000000000000000000000000064000000')
    ScreenShake(0, 8000)
    sprite('null', 2)	# 5-6
    Unknown4004('6566666563745f3438340000000000000000000000000000000000000000000064000000')
    sprite('null', 2)	# 7-8
    Unknown4004('6566666563745f3438340000000000000000000000000000000000000000000064000000')
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('null', 2)	# 9-10
    Unknown4004('6566666563745f3438350000000000000000000000000000000000000000000064000000')
    ScreenShake(0, 8000)
    sprite('null', 2)	# 11-12
    Unknown4004('6566666563745f3438350000000000000000000000000000000000000000000064000000')
    sprite('null', 2)	# 13-14
    Unknown4004('6566666563745f3438350000000000000000000000000000000000000000000064000000')
    loopRest()
    gotoLabel(0)
    label(580)
    sprite('null', 2)	# 15-16

@State
def AstralAtk_ShockWaveAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(2000)
        PushbackX(19800)
        Hitstop(0)
        MinimumDamagePct(100)
        Unknown11064(1)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        AirPushbackX(0)
        AirPushbackY(300)
        YImpluseBeforeWallbounce(0)
        hitstun(999)
        AirUntechableTime(999)
        Unknown11086(1)
        callSubroutine('AtkEffLightning')
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_78():
            Unknown23029(3, 5001, 0)
            PushbackX(0)
            GFX_0('AstralAtk_HitMark', 100)
    sprite('null', 1)	# 1-1
    sprite('Action_235_atkcol', 12)	# 2-13
    physicsXImpulse(95000)
    RefreshMultihit()

@State
def AstralHeatCutIn():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown23015(1)
        Unknown2054(1)
        Unknown23013(0)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown2035(1)
        Unknown3001(0)
        teleportRelativeX(260000)
        Unknown23033(0)
    sprite('Action_245_00', 20)	# 1-20	 **attackbox here**
    physicsYImpulse(-8500)
    Unknown3004(3)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    sprite('Action_245_00', 20)	# 21-40	 **attackbox here**
    GFX_0('AstralCutInBG', 100)
    sprite('Action_245_00', 40)	# 41-80	 **attackbox here**
    Unknown3004(1)
    sprite('Action_245_00', 80)	# 81-160	 **attackbox here**
    Unknown3004(1)
    sprite('Action_245_01', 3)	# 161-163	 **attackbox here**
    Unknown1084(1)
    clearUponHandler(3)
    Unknown36(22)
    Unknown3004(-31)
    Unknown35()
    physicsXImpulse(-1500)
    physicsYImpulse(-3500)

    def upon_CLEAR_OR_EXIT():
        Unknown1097(100)
    ScreenShake(25000, 0)
    GFX_0('AstralCutInSpeedline', 100)
    sprite('Action_245_02', 4)	# 164-167	 **attackbox here**
    sprite('Action_245_03', 13)	# 168-180	 **attackbox here**
    clearUponHandler(3)
    Unknown1084(1)
    sprite('Action_245_04', 10)	# 181-190	 **attackbox here**
    GFX_0('AstralCutInWhiteOut', 100)

@State
def AstralCutIn_Sakura():

    def upon_IMMEDIATE():
        Unknown2019(-999)
        Unknown23015(1)
        Unknown2054(1)
        teleportRelativeX(260000)
        Unknown23033(50)
        Unknown23030('5365744275674669785f50414e495f52696e67427567000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_244_02', 8)	# 1-8
    sprite('Action_244_03', 8)	# 9-16
    sprite('Action_244_04', 8)	# 17-24
    sprite('Action_244_05', 8)	# 25-32
    sprite('Action_244_06', 8)	# 33-40
    sprite('Action_244_07', 8)	# 41-48
    sprite('Action_244_08', 8)	# 49-56
    sprite('Action_244_09', 8)	# 57-64
    sprite('Action_244_10', 8)	# 65-72
    sprite('Action_244_11', 8)	# 73-80
    sprite('Action_244_12', 8)	# 81-88
    sprite('Action_244_13', 8)	# 89-96
    sprite('Action_244_14', 8)	# 97-104
    sprite('Action_244_15', 8)	# 105-112
    sprite('Action_244_16', 8)	# 113-120
    sprite('Action_244_17', 8)	# 121-128
    sprite('Action_244_18', 8)	# 129-136
    sprite('Action_244_19', 8)	# 137-144
    SFX_3('SE_VanishDiscBall')
    sprite('Action_244_20', 8)	# 145-152
    sprite('Action_244_21', 8)	# 153-160
    sprite('Action_244_22', 8)	# 161-168
    sprite('Action_244_23', 8)	# 169-176
    sprite('Action_244_24', 8)	# 177-184

@State
def AstralCutInSpeedline():

    def upon_IMMEDIATE():
        Unknown2019(-1001)
        Unknown23015(1)
        Unknown2008()
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-280000)
    sprite('Action_239_00', 4)	# 1-4
    sprite('Action_239_01', 4)	# 5-8
    sprite('Action_239_02', 4)	# 9-12

@State
def AstralCutInBG():

    def upon_IMMEDIATE():
        Unknown2019(1000)
        Unknown23015(1)
        Unknown2008()
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-280000)
    sprite('Action_240_00', 5)	# 1-5
    sprite('Action_240_01', 155)	# 6-160
    sprite('Action_240_02', 4)	# 161-164
    sprite('Action_240_03', 4)	# 165-168
    sprite('Action_240_04', 4)	# 169-172

@State
def AstralCutInWhiteOut():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown23015(1)
        Unknown2008()
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-280000)
    sprite('Action_241_00', 3)	# 1-3
    sprite('Action_241_01', 3)	# 4-6
    sprite('Action_241_02', 3)	# 7-9
    sprite('Action_241_03', 3)	# 10-12
    sprite('Action_241_04', 3)	# 13-15
    Unknown21015('41737472616c4865617443616d657261000000000000000000000000000000008a13000000000000')
    sprite('Action_241_05', 3)	# 16-18
    SFX_3('SE023')
    sprite('Action_241_06', 3)	# 19-21	 **attackbox here**
    sprite('Action_241_07', 3)	# 22-24	 **attackbox here**
    sprite('Action_241_08', 3)	# 25-27	 **attackbox here**
    sprite('Action_241_09', 3)	# 28-30	 **attackbox here**
    sprite('Action_241_10', 3)	# 31-33	 **attackbox here**
    sprite('Action_241_11', 1)	# 34-34	 **attackbox here**

@State
def FloorLightning():

    def upon_IMMEDIATE():
        Unknown1000(0)
    sprite('Action_247_00', 3)	# 1-3
    sprite('Action_247_01', 3)	# 4-6
    sprite('Action_247_02', 3)	# 7-9
    sprite('Action_247_03', 3)	# 10-12
    sprite('Action_247_04', 3)	# 13-15
    sprite('null', 3)	# 16-18
    sprite('Action_247_06', 3)	# 19-21
    sprite('Action_247_07', 3)	# 22-24
    sprite('Action_247_08', 3)	# 25-27
    sprite('Action_247_09', 3)	# 28-30
    sprite('Action_247_10', 3)	# 31-33

@State
def AstralFinishAtkHitMark():

    def upon_IMMEDIATE():
        Unknown23151(22, 103)
    sprite('Action_246_00', 5)	# 1-5
    sprite('Action_246_01', 5)	# 6-10
    sprite('Action_246_02', 5)	# 11-15
    sprite('Action_246_03', 5)	# 16-20
    Unknown36(22)
    Unknown3026(-16777216)
    Unknown35()

@State
def AstralOuka():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown23015(2)
        Unknown2008()
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-280000)
    sprite('null', 20)	# 1-20
    sprite('Action_243_01', 10)	# 21-30
    sprite('Action_243_02', 10)	# 31-40
    sprite('Action_243_03', 10)	# 41-50
    sprite('Action_243_04', 10)	# 51-60
    sprite('Action_243_05', 10)	# 61-70

@State
def AstralFinalExplosion():

    def upon_IMMEDIATE():
        Unknown2019(1000)
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('Action_242_01', 8)	# 1-8	 **attackbox here**
    sprite('Action_242_02', 8)	# 9-16	 **attackbox here**
    sprite('Action_242_03', 8)	# 17-24	 **attackbox here**
    sprite('Action_242_04', 8)	# 25-32	 **attackbox here**
    sprite('Action_242_05', 8)	# 33-40	 **attackbox here**
    sprite('Action_242_06', 8)	# 41-48	 **attackbox here**
    sprite('Action_242_07', 8)	# 49-56	 **attackbox here**
    GFX_0('AstralWhiteOut', 100)
    sprite('Action_242_08', 8)	# 57-64	 **attackbox here**
    sprite('Action_242_09', 8)	# 65-72	 **attackbox here**
    GFX_0('AstralFinishAtk', 100)

@State
def AstralFinishShake():

    def upon_IMMEDIATE():
        loopRelated(17, 150)

        def upon_17():
            sendToLabel(580)
    sprite('null', 10)	# 1-10
    ScreenShake(7500, 2500)
    sprite('null', 10)	# 11-20
    ScreenShake(9000, 3000)
    sprite('null', 10)	# 21-30
    ScreenShake(12500, 3750)
    sprite('null', 10)	# 31-40
    ScreenShake(15000, 4500)
    label(0)
    sprite('null', 8)	# 41-48
    ScreenShake(18000, 5000)
    loopRest()
    gotoLabel(0)
    label(580)
    sprite('null', 2)	# 49-50

@State
def AstralFinishAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(20000)
        MinimumDamagePct(100)
        Unknown11064(3)
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown9130(16)
        Unknown9142(100)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        PushbackX(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown11086(1)
        Unknown23151(22, 103)
    sprite('Action_237_01', 10)	# 1-10	 **attackbox here**

@State
def AstralWhiteOut():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 15)	# 1-15
    Unknown3004(20)
    sprite('vr_white', 40)	# 16-55
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 60)	# 56-115
    sprite('vr_white', 60)	# 116-175
    Unknown3004(-5)

@State
def AstralHeatCamera():

    def upon_IMMEDIATE():
        Unknown1086(3)
        Unknown2053(0)
        EnableCollision(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20000(1)

        def upon_43():
            if (SLOT_48 == 5002):
                sendToLabel(1)
    label(0)
    sprite('null', 32767)	# 1-32767
    teleportRelativeX(260000)
    label(1)
    sprite('null', 32767)	# 32768-65534
    Unknown20001(1)
    Unknown1000(0)
    Unknown36(3)
    Unknown1000(320000)
    Unknown35()
    Unknown36(22)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1000(320000)
    Unknown35()

@State
def UAK_CutIn():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown23015(5)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_999_01', 3)	# 1-3
    sprite('Action_999_02', 3)	# 4-6
    sprite('Action_999_03', 3)	# 7-9
    sprite('Action_999_04', 2)	# 10-11
    sprite('Action_999_05', 4)	# 12-15
    sprite('Action_999_06', 5)	# 16-20
    sprite('Action_999_07', 4)	# 21-24
    sprite('Action_999_08', 6)	# 25-30
    sprite('Action_999_09', 3)	# 31-33
    sprite('Action_999_10', 13)	# 34-46
    sprite('Action_999_11', 6)	# 47-52
    sprite('Action_999_12', 6)	# 53-58
    sprite('Action_999_13', 12)	# 59-70
    physicsXImpulse(12000)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(20)

@State
def XhitEff_Denkou():

    def upon_IMMEDIATE():
        Unknown2006()
        Unknown1086(22)
        teleportRelativeY(200000)
    sprite('null', 22)	# 1-22
    GFX_1('ef_hitx_den', 0)

@State
def Entry_Coat_Throw():

    def upon_IMMEDIATE():
        Unknown1015(-10000)
        Unknown1021(7000)
        Unknown1028(300)
        setGravity(550)
        Unknown3004(-10)
    sprite('Action_100_00', 5)	# 1-5
    sprite('Action_100_01', 5)	# 6-10
    sprite('Action_100_02', 5)	# 11-15
    sprite('Action_100_03', 5)	# 16-20
    sprite('Action_100_04', 5)	# 21-25

@State
def Entry_Suitcase_Fade():

    def upon_IMMEDIATE():
        Unknown3004(-17)
    sprite('Action_413_00', 16)	# 1-16	 **attackbox here**

@State
def Electricity_Aura():
    sprite('Action_246_00', 3)	# 1-3
    sprite('Action_246_01', 3)	# 4-6
    sprite('Action_246_02', 3)	# 7-9
    sprite('Action_246_03', 3)	# 10-12

@State
def Electricity_Charged():
    sprite('Action_237_01', 4)	# 1-4	 **attackbox here**
    sprite('Action_237_02', 4)	# 5-8
    sprite('Action_237_03', 4)	# 9-12
    sprite('Action_237_04', 4)	# 13-16
    sprite('Action_237_05', 4)	# 17-20
    sprite('Action_247_00', 5)	# 21-25
    sprite('Action_247_01', 5)	# 26-30
    sprite('Action_247_02', 5)	# 31-35
    sprite('Action_247_03', 5)	# 36-40
    sprite('Action_247_04', 5)	# 41-45

@State
def EffKamiKazeBomb_ikazuchi():

    def upon_IMMEDIATE():
        Unknown4010(2)
        teleportRelativeX(50000)
        Unknown1007(200000)
        Unknown1096(1200)
        Unknown2019(999)
    sprite('Action_216_00', 2)	# 1-2
    sprite('Action_216_01', 6)	# 3-8
    sprite('Action_216_02', 6)	# 9-14
    sprite('Action_216_03', 6)	# 15-20
    sprite('Action_216_04', 6)	# 21-26
    sprite('Action_216_05', 6)	# 27-32
    sprite('Action_216_06', 6)	# 33-38
    sprite('Action_216_07', 3)	# 39-41

@State
def ikazuchi_BG():

    def upon_IMMEDIATE():
        Unknown23015(2)
    sprite('null', 5)	# 1-5
    GFX_0('ikazuchi_WhiteOut', 100)
    GFX_0('EffKamiKazeSpeedLineLoop', 100)
    sprite('null', 40)	# 6-45
    GFX_0('ikazuchi_L', 100)
    GFX_0('ikazuchi_R', 100)
    sprite('null', 1)	# 46-46
    Unknown26('EffKamiKazeSpeedLineLoop')

@State
def ikazuchi_WhiteOut():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(17)
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 10)	# 1-10
    Unknown3004(25)
    sprite('vr_white', 50)	# 11-60
    Unknown3001(255)
    Unknown3004(0)
    GFX_0('KamikazeThunder', 100)
    sprite('vr_white', 15)	# 61-75
    Unknown3004(-17)

@State
def ikazuchi_L():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown23015(17)
        Unknown2020(-100)
        Unknown3032()
        Unknown4061(0)
        Unknown21004(255)
        Unknown13044(1)
        Unknown2055(200)

        def upon_CLEAR_OR_EXIT():
            Unknown23032(75)
            Unknown23033(51)
        Unknown1096(600)
    sprite('null', 5)	# 1-5
    GFX_0('EffKamiKazeBomb_ikazuchi', 100)
    Unknown36(1)
    Unknown23032(75)
    Unknown23033(51)
    Unknown35()
    sprite('vr_uakef_ikazuchi00', 15)	# 6-20
    Unknown1099(40)
    sprite('vr_uakef_ikazuchi00', 25)	# 21-45
    Unknown1096(1200)
    Unknown1099(0)
    sprite('vr_uakef_ikazuchi00', 10)	# 46-55
    Unknown3004(-25)

@State
def ikazuchi_R():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown23015(17)
        Unknown2020(-100)
        Unknown3032()
        Unknown4061(0)
        Unknown21004(255)
        Unknown13044(1)
        Unknown2055(200)

        def upon_CLEAR_OR_EXIT():
            Unknown23032(30)
            Unknown23033(51)
        Unknown1096(600)
    sprite('null', 5)	# 1-5
    GFX_0('EffKamiKazeBomb_ikazuchi', 100)
    Unknown36(1)
    Unknown23032(30)
    Unknown23033(51)
    Unknown35()
    sprite('vr_uakef_ikazuchi01', 15)	# 6-20
    Unknown1099(40)
    sprite('vr_uakef_ikazuchi01', 25)	# 21-45
    Unknown1096(1200)
    Unknown1099(0)
    sprite('vr_uakef_ikazuchi01', 10)	# 46-55
    Unknown3004(-25)

@State
def KamikazeThunder():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown4010(2)
        Unknown2019(1000)
        Unknown3032()
        Unknown13044(1)
        Unknown2055(200)

        def upon_CLEAR_OR_EXIT():
            Unknown23032(25)
            Unknown23033(50)
        Unknown1096(1000)
        Unknown1056(2500)
        Unknown1064(1200)
    sprite('Action_700_00', 5)	# 1-5
    sprite('Action_700_01', 5)	# 6-10
    sprite('Action_700_02', 5)	# 11-15
    sprite('Action_700_03', 5)	# 16-20
    sprite('Action_700_04', 5)	# 21-25
    sprite('Action_700_05', 5)	# 26-30
    sprite('Action_700_06', 5)	# 31-35
    sprite('Action_700_07', 5)	# 36-40
    sprite('Action_700_08', 5)	# 41-45
