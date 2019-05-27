@State
def Wal_081():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_081_00', 2)	# 1-2
    sprite('Action_081_01', 2)	# 3-4
    sprite('Action_081_02', 2)	# 5-6
    sprite('Action_081_03', 2)	# 7-8

@State
def Wal_082():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_082_00', 2)	# 1-2
    sprite('Action_082_01', 2)	# 3-4
    sprite('Action_082_02', 2)	# 5-6
    sprite('Action_082_03', 3)	# 7-9

@State
def Wal_080():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_080_00', 2)	# 1-2
    sprite('Action_080_01', 2)	# 3-4
    sprite('Action_080_02', 2)	# 5-6
    sprite('Action_080_03', 2)	# 7-8

@State
def Wal_094():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_094_00', 2)	# 1-2
    sprite('Action_094_01', 2)	# 3-4
    sprite('Action_094_02', 2)	# 5-6
    sprite('Action_094_03', 2)	# 7-8

@State
def Wal_085():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_085_00', 2)	# 1-2
    sprite('Action_085_01', 2)	# 3-4
    sprite('Action_085_02', 2)	# 5-6
    sprite('Action_085_03', 2)	# 7-8

@State
def Wal_083():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_083_00', 2)	# 1-2
    sprite('Action_083_01', 2)	# 3-4
    sprite('Action_083_02', 2)	# 5-6
    sprite('Action_083_03', 2)	# 7-8

@State
def Wal_084():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_084_00', 4)	# 1-4
    sprite('Action_084_01', 3)	# 5-7
    sprite('Action_084_02', 2)	# 8-9
    sprite('Action_084_03', 2)	# 10-11

@State
def Wal_077():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_077_00', 3)	# 1-3
    sprite('Action_077_01', 3)	# 4-6
    sprite('Action_077_02', 3)	# 7-9
    sprite('Action_077_03', 3)	# 10-12
    sprite('Action_077_04', 3)	# 13-15

@State
def Wal_078():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown2019(500)
    sprite('Action_078_00', 3)	# 1-3
    sprite('Action_078_01', 3)	# 4-6
    sprite('Action_078_02', 3)	# 7-9
    sprite('Action_078_03', 3)	# 10-12
    sprite('Action_078_04', 3)	# 13-15

@State
def Wal_076():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_076_00', 2)	# 1-2
    sprite('Action_076_01', 2)	# 3-4
    sprite('Action_076_02', 2)	# 5-6
    sprite('Action_076_03', 2)	# 7-8

@State
def Wal_088():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_088_00', 2)	# 1-2
    sprite('Action_088_01', 2)	# 3-4
    sprite('Action_088_02', 2)	# 5-6
    sprite('Action_088_03', 2)	# 7-8

@State
def Eff_6A_00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(100000)
    sprite('Action_215_00', 5)	# 1-5
    sprite('Action_215_01', 4)	# 6-9
    sprite('Action_215_02', 2)	# 10-11
    sprite('Action_215_03', 1)	# 12-12

@State
def Eff_6A_01():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        teleportRelativeX(100000)
        Unknown1007(40000)
    sprite('Action_216_00', 3)	# 1-3
    sprite('Action_216_01', 3)	# 4-6
    sprite('Action_216_02', 3)	# 7-9
    sprite('Action_216_03', 3)	# 10-12

@State
def Eff_6A_StoneAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AttackP1(70)
        PushbackX(11000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        AirUntechableTime(40)
        Unknown9310(1)
        Unknown11042(1)
        physicsXImpulse(45000)
        physicsYImpulse(-60000)
        sendToLabelUpon(2, 9)
        sendToLabelUpon(77, 9)
    sprite('Action_202_01', 120)	# 1-120	 **attackbox here**
    SFX_3('SE051')
    label(9)
    sprite('Action_202_02', 1)	# 121-121
    Unknown23027()
    Unknown1084(1)
    clearUponHandler(2)
    clearUponHandler(77)
    sprite('Action_202_03', 3)	# 122-124
    SFX_3('SE017_BoundMinHigh')
    sprite('Action_202_04', 3)	# 125-127
    sprite('Action_202_05', 3)	# 128-130
    sprite('Action_202_06', 3)	# 131-133
    sprite('Action_202_07', 3)	# 134-136
    sprite('Action_202_08', 1)	# 137-137

@State
def Eff_4BShock():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown2019(-100)
    sprite('Action_079_00', 2)	# 1-2
    sprite('Action_079_01', 3)	# 3-5
    sprite('Action_079_02', 4)	# 6-9
    sprite('Action_079_03', 5)	# 10-14
    sprite('Action_079_04', 3)	# 15-17

@State
def Wal_086():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
    sprite('Action_086_00', 2)	# 1-2
    sprite('Action_086_01', 2)	# 3-4
    sprite('Action_086_02', 2)	# 5-6
    sprite('Action_086_03', 2)	# 7-8

@State
def Eff_LandSlamThrow():
    teleportRelativeY(0)
    Unknown8004(100, 1, 1)
    SFX_0('209_down_normal_1')
    SFX_0('016_explode_2')
    ScreenShake(5000, 10000)

@State
def Eff_EisenNagel():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        teleportRelativeX(-200000)
    sprite('Action_102_00', 4)	# 1-4
    sprite('Action_102_01', 4)	# 5-8
    sprite('Action_102_02', 3)	# 9-11
    sprite('Action_102_03', 3)	# 12-14

@State
def Eff_FairdeRuben1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown4009(2)
    sprite('Action_223_00', 3)	# 1-3
    sprite('Action_223_01', 3)	# 4-6
    sprite('Action_223_02', 3)	# 7-9
    sprite('Action_223_03', 3)	# 10-12
    sprite('Action_223_04', 1)	# 13-13

@State
def Eff_FairdeRuben2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown4009(2)
        Unknown2019(500)
    sprite('Action_224_00', 3)	# 1-3
    sprite('Action_224_01', 3)	# 4-6
    sprite('Action_224_02', 3)	# 7-9
    sprite('Action_224_03', 3)	# 10-12
    sprite('Action_224_04', 1)	# 13-13

@State
def Eff_FairdeRuben_Impact():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown2019(100)
    sprite('Action_226_00', 3)	# 1-3
    sprite('Action_226_01', 3)	# 4-6
    sprite('Action_226_02', 3)	# 7-9
    sprite('Action_226_03', 3)	# 10-12
    sprite('Action_226_04', 3)	# 13-15
    sprite('Action_226_05', 1)	# 16-16

@State
def Wal_074():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown2019(100)
        Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
        Unknown36(1)
        teleportRelativeY(0)
        Unknown35()
    sprite('Action_074_00', 1)	# 1-1
    sprite('Action_074_01', 2)	# 2-3
    sprite('Action_074_02', 2)	# 4-5
    sprite('Action_074_03', 3)	# 6-8
    sprite('Action_074_04', 3)	# 9-11
    sprite('Action_074_05', 1)	# 12-12

@State
def Wal_075():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4019(2)
        Unknown2019(100)
    sprite('Action_075_00', 1)	# 1-1
    sprite('Action_075_01', 2)	# 2-3
    sprite('Action_075_02', 2)	# 4-5
    sprite('Action_075_03', 3)	# 6-8
    sprite('Action_075_04', 3)	# 9-11
    sprite('Action_075_05', 1)	# 12-12

@State
def Eff_Wirbelwind01():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('Action_091_00', 2)	# 1-2
    sprite('Action_091_01', 2)	# 3-4
    sprite('Action_091_02', 2)	# 5-6
    sprite('Action_091_03', 2)	# 7-8

@State
def Eff_Wirbelwind02():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('Action_093_00', 2)	# 1-2
    sprite('Action_093_01', 2)	# 3-4
    sprite('Action_093_02', 2)	# 5-6
    sprite('Action_093_03', 2)	# 7-8

@State
def Eff_Wirbelwind03():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('Action_095_00', 2)	# 1-2
    sprite('Action_095_01', 2)	# 3-4
    sprite('Action_095_02', 2)	# 5-6
    sprite('Action_095_03', 2)	# 7-8

@State
def Eff_Wirbelwind04():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown4009(2)
    sprite('Action_097_00', 2)	# 1-2
    sprite('Action_097_01', 2)	# 3-4
    sprite('Action_097_02', 2)	# 5-6
    sprite('Action_097_03', 2)	# 7-8

@State
def Eff_DrehenDurchbohren_Spin():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown4009(2)
        teleportRelativeX(100000)

        def upon_43():
            if (SLOT_48 == 201):
                sendToLabel(1)
            if (SLOT_48 == 202):
                sendToLabel(2)
            if (SLOT_48 == 203):
                sendToLabel(3)
    label(0)
    sprite('Action_456_00', 4)	# 1-4
    sprite('Action_456_01', 4)	# 5-8
    sprite('Action_456_02', 4)	# 9-12
    sprite('Action_456_03', 4)	# 13-16
    sprite('Action_456_04', 4)	# 17-20
    sprite('Action_456_05', 4)	# 21-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_456_00', 3)	# 25-27
    sprite('Action_456_01', 3)	# 28-30
    sprite('Action_456_02', 3)	# 31-33
    sprite('Action_456_03', 3)	# 34-36
    sprite('Action_456_04', 3)	# 37-39
    sprite('Action_456_05', 3)	# 40-42
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('Action_456_00', 2)	# 43-44
    sprite('Action_456_01', 2)	# 45-46
    sprite('Action_456_02', 2)	# 47-48
    sprite('Action_456_03', 2)	# 49-50
    sprite('Action_456_04', 2)	# 51-52
    sprite('Action_456_05', 2)	# 53-54
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('Action_456_00', 1)	# 55-55
    sprite('Action_456_01', 1)	# 56-56
    sprite('Action_456_02', 1)	# 57-57
    sprite('Action_456_03', 1)	# 58-58
    sprite('Action_456_04', 1)	# 59-59
    sprite('Action_456_05', 1)	# 60-60
    loopRest()
    gotoLabel(3)

@State
def Eff_DrehenDurchbohren_Bomb():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4019(2)
        teleportRelativeY(0)
        ScreenShake(10000, 30000)
        SFX_0('209_down_normal_1')
        SFX_0('016_explode_2')
        SFX_3('SE220')
    sprite('Action_457_00', 6)	# 1-6
    sprite('Action_457_01', 7)	# 7-13
    sprite('Action_457_02', 9)	# 14-22
    sprite('Action_457_03', 8)	# 23-30
    sprite('Action_457_04', 8)	# 31-38

@State
def Eff_DrehenDurchbohren_BigBomb():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4019(2)
        teleportRelativeY(0)
        ScreenShake(20000, 50000)
        SFX_0('209_down_normal_1')
        SFX_0('016_explode_2')
        SFX_3('SE220')
    sprite('Action_461_00', 6)	# 1-6
    sprite('Action_461_01', 7)	# 7-13
    sprite('Action_461_02', 9)	# 14-22
    sprite('Action_461_03', 8)	# 23-30
    sprite('Action_461_04', 8)	# 31-38

@State
def Eff_SturmAngriff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4019(2)
        ScreenShake(20000, 5000)
        SFX_0('209_down_normal_1')
        SFX_0('016_explode_2')
        SFX_3('SE220')
    sprite('Action_446_00', 3)	# 1-3
    sprite('Action_446_01', 3)	# 4-6
    sprite('Action_446_02', 3)	# 7-9
    sprite('Action_446_03', 3)	# 10-12
    sprite('Action_446_04', 3)	# 13-15

@State
def Wal_104():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4019(2)
        ScreenShake(10000, 10000)
    sprite('Action_104_00', 3)	# 1-3
    sprite('Action_104_01', 3)	# 4-6
    sprite('Action_104_02', 3)	# 7-9
    sprite('Action_104_03', 3)	# 10-12
    sprite('Action_104_04', 3)	# 13-15
    sprite('Action_104_05', 3)	# 16-18

@State
def Eff_UltimateThrowSlam():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4019(2)
        Unknown2019(100)
        teleportRelativeX(-200000)
        ScreenShake(10000, 10000)
    sprite('Action_075_00', 1)	# 1-1
    sprite('Action_075_01', 2)	# 2-3
    sprite('Action_075_02', 2)	# 4-5
    sprite('Action_075_03', 3)	# 6-8
    sprite('Action_075_04', 3)	# 9-11
    sprite('Action_075_05', 1)	# 12-12

@State
def Wal_178():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown4009(2)
        Unknown1007(50000)
    label(0)
    sprite('Action_178_00', 3)	# 1-3
    sprite('Action_178_01', 3)	# 4-6
    sprite('Action_178_02', 3)	# 7-9
    sprite('Action_178_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def UltimateThrowExe4_Camera():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown20001(1)
        Unknown20000(1)
        Unknown20003(1)
    sprite('null', 120)	# 1-120
    setGravity(-90)

@State
def AirCatch_Collision_UT():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown2011()
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown11107(1)
        Unknown11050('090000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11045(0)
        Unknown11072(1, 200000, 0)
        Unknown11069('UltimateThrow')
        Unknown11084(1)
        Unknown3001(0)
    sprite('Action_451_02', 4)	# 1-4	 **attackbox here**

@State
def AirCatch_Collision_UTOD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown2011()
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown11107(1)
        Unknown11050('090000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11045(0)
        Unknown11072(1, 200000, 0)
        Unknown11069('UltimateThrowOD')
        Unknown11084(1)
        Unknown3001(0)
    sprite('Action_451_02', 4)	# 1-4	 **attackbox here**

@State
def AirCatch_Collision_URT():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown2011()
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown11107(1)
        Unknown11050('090000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11045(0)
        Unknown11072(1, 200000, 0)
        Unknown11069('UltimateRunningThrow')
        Unknown11084(1)
        Unknown3001(0)
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def AirCatch_Collision_URTOD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown2011()
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(0)
        Unknown11107(1)
        Unknown11050('090000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11045(0)
        Unknown11072(1, 200000, 0)
        Unknown11069('UltimateRunningThrowOD')
        Unknown11084(1)
        Unknown3001(0)
    label(0)
    sprite('Action_435_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_435_06', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def AstralHeatCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)
        Unknown2034(0)
        Unknown2053(0)

        def upon_43():
            if (SLOT_48 == 901):
                sendToLabel(0)
            if (SLOT_48 == 902):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 15)	# 32768-32782
    Unknown20001(1)
    Unknown1086(3)
    physicsYImpulse(10000)
    sprite('null', 60)	# 32783-32842
    Unknown20001(0)
    setGravity(100)
    sprite('null', 32767)	# 32843-65609
    physicsYImpulse(10000)
    setGravity(-400)
    label(1)
    sprite('null', 32767)	# 65610-98376
    Unknown1084(1)
    Unknown20001(1)
    Unknown1086(3)

@State
def Wal_188():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4019(2)
        Unknown2019(500)
        Unknown1007(200000)
        ScreenShake(10000, 10000)
    sprite('Action_188_00', 3)	# 1-3
    sprite('Action_188_01', 3)	# 4-6
    sprite('Action_188_02', 3)	# 7-9
    sprite('Action_188_03', 3)	# 10-12
    sprite('Action_188_04', 3)	# 13-15
    sprite('Action_188_05', 3)	# 16-18

@State
def Wal_183():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown2019(-500)
        Unknown1007(-80000)
    label(0)
    sprite('Action_183_00', 3)	# 1-3
    sprite('Action_183_01', 3)	# 4-6
    sprite('Action_183_02', 3)	# 7-9
    sprite('Action_183_03', 3)	# 10-12
    sprite('Action_183_04', 3)	# 13-15
    sprite('Action_183_05', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def Wal_187():

    def upon_IMMEDIATE():
        Unknown2019(-1000)

        def upon_3():
            Unknown4007(2)
            if SLOT_2:
                ScreenShake(5000, 2000)
                Unknown2037(0)
            else:
                Unknown2037(1)
        Unknown4013(2)
    sprite('Action_187_00', 110)	# 1-110	 **attackbox here**
    SFX_3('SE_EarthQuake')
    SFX_3('SE_BombTheEarth')
    sprite('Action_187_01', 2)	# 111-112	 **attackbox here**
    sprite('Action_187_02', 2)	# 113-114	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_03', 2)	# 115-116	 **attackbox here**
    sprite('Action_187_04', 2)	# 117-118	 **attackbox here**
    sprite('Action_187_05', 2)	# 119-120	 **attackbox here**
    sprite('Action_187_06', 2)	# 121-122	 **attackbox here**
    sprite('Action_187_07', 2)	# 123-124	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_08', 2)	# 125-126	 **attackbox here**
    sprite('Action_187_09', 2)	# 127-128	 **attackbox here**
    sprite('Action_187_10', 2)	# 129-130	 **attackbox here**
    sprite('Action_187_11', 2)	# 131-132	 **attackbox here**
    sprite('Action_187_12', 2)	# 133-134	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_13', 2)	# 135-136	 **attackbox here**
    sprite('Action_187_14', 2)	# 137-138	 **attackbox here**
    sprite('Action_187_15', 2)	# 139-140	 **attackbox here**
    sprite('Action_187_16', 2)	# 141-142	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_17', 2)	# 143-144	 **attackbox here**
    sprite('Action_187_18', 2)	# 145-146	 **attackbox here**
    sprite('Action_187_19', 2)	# 147-148	 **attackbox here**
    sprite('Action_187_20', 2)	# 149-150	 **attackbox here**
    sprite('Action_187_21', 2)	# 151-152	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_22', 2)	# 153-154	 **attackbox here**
    sprite('Action_187_23', 2)	# 155-156	 **attackbox here**
    sprite('Action_187_24', 2)	# 157-158	 **attackbox here**
    sprite('Action_187_25', 2)	# 159-160	 **attackbox here**
    sprite('Action_187_26', 2)	# 161-162	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_27', 2)	# 163-164	 **attackbox here**
    sprite('Action_187_28', 2)	# 165-166	 **attackbox here**
    sprite('Action_187_29', 2)	# 167-168	 **attackbox here**
    sprite('Action_187_30', 2)	# 169-170	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_31', 2)	# 171-172	 **attackbox here**
    sprite('Action_187_32', 2)	# 173-174	 **attackbox here**
    sprite('Action_187_33', 10)	# 175-184	 **attackbox here**
    sprite('Action_187_34', 10)	# 185-194	 **attackbox here**
    SFX_3('SE_EarthQuake')
    SFX_3('SE_Bomb')
    sprite('Action_187_35', 10)	# 195-204	 **attackbox here**
    sprite('Action_187_36', 10)	# 205-214	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_37', 10)	# 215-224	 **attackbox here**
    sprite('Action_187_38', 10)	# 225-234	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_39', 10)	# 235-244	 **attackbox here**
    sprite('Action_187_40', 10)	# 245-254	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_41', 10)	# 255-264	 **attackbox here**
    sprite('Action_187_42', 10)	# 265-274	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_43', 10)	# 275-284	 **attackbox here**
    sprite('Action_187_44', 10)	# 285-294	 **attackbox here**
    sprite('Action_187_45', 10)	# 295-304	 **attackbox here**
    sprite('Action_187_46', 10)	# 305-314	 **attackbox here**
    SFX_3('SE_Bomb')
    sprite('Action_187_47', 10)	# 315-324	 **attackbox here**
    sprite('Action_187_48', 12)	# 325-336	 **attackbox here**

@State
def Wal_185ex():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4019(2)
        Unknown2019(-500)
        Unknown4007(2)
        Unknown4013(2)
    label(0)
    sprite('Action_185_14ex', 3)	# 1-3
    Unknown3005(-50)
    sprite('Action_185_15ex', 3)	# 4-6
    sprite('Action_185_16ex', 3)	# 7-9
    sprite('Action_185_17ex', 3)	# 10-12
    sprite('Action_185_18ex', 3)	# 13-15
    sprite('Action_185_19ex', 3)	# 16-18
    sprite('Action_185_20ex', 3)	# 19-21
    sprite('Action_185_21ex', 1)	# 22-22
    sprite('Action_185_22ex', 3)	# 23-25
    sprite('Action_185_23ex', 3)	# 26-28
    loopRest()
    gotoLabel(0)

@State
def Wal_999():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_999_01', 3)	# 1-3
    sprite('Action_999_02', 4)	# 4-7	 **attackbox here**
    sprite('Action_999_03', 5)	# 8-12
    sprite('Action_999_04', 6)	# 13-18
    sprite('Action_999_05', 9)	# 19-27
    sprite('Action_999_06', 3)	# 28-30	 **attackbox here**
    sprite('Action_999_07', 5)	# 31-35
    sprite('Action_999_08', 6)	# 36-41	 **attackbox here**
    sprite('Action_999_09', 7)	# 42-48	 **attackbox here**
    sprite('Action_999_10', 5)	# 49-53
    sprite('Action_999_11', 6)	# 54-59
    sprite('Action_999_12', 3)	# 60-62	 **attackbox here**
    sprite('Action_999_13', 10)	# 63-72	 **attackbox here**
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)