@State
def ModelMagicCircle1():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown4003('726765665f6d632e444947000000000000000000000000000000000000000000726765665f6d635f6d6f74696f6e5f3030302e6d6d6f74000000000000000000')
        Unknown4015()
        Unknown21004(224)
        Unknown2054(1)
    sprite('null', 74)	# 1-74

@State
def Lin_082():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_082_00', 6)	# 1-6
    sprite('Action_082_01', 6)	# 7-12
    sprite('Action_082_02', 1)	# 13-13

@State
def EffNmlAtk5ABlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_081_00', 6)	# 1-6
    sprite('Action_081_01', 6)	# 7-12
    sprite('Action_081_02', 1)	# 13-13

@State
def EffNmlAtk5BBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_082_00', 6)	# 1-6
    sprite('Action_082_01', 6)	# 7-12
    sprite('Action_082_02', 1)	# 13-13

@State
def EffNmlAtk5CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
    sprite('Action_094_00', 4)	# 1-4
    sprite('Action_094_01', 4)	# 5-8
    sprite('Action_094_02', 4)	# 9-12
    sprite('Action_094_03', 1)	# 13-13

@State
def EffNmlAtk6CBlade1st():

    def upon_IMMEDIATE():
        Unknown4011(3)
        teleportRelativeX(60000)
        Unknown1007(10000)
    sprite('Action_135_00', 6)	# 1-6
    GFX_0('EffNmlAtk6CBlade1stAdd', 100)
    sprite('Action_135_01', 3)	# 7-9
    sprite('Action_135_02', 5)	# 10-14
    sprite('Action_135_03', 5)	# 15-19
    sprite('Action_135_04', 1)	# 20-20

@State
def EffNmlAtk6CBlade1stAdd():

    def upon_IMMEDIATE():
        Unknown4011(3)
    sprite('Action_109_00', 3)	# 1-3
    sprite('Action_109_01', 3)	# 4-6
    sprite('Action_109_02', 5)	# 7-11
    sprite('Action_109_03', 5)	# 12-16
    sprite('Action_109_04', 1)	# 17-17

@State
def EffNmlAtk6CBlade2nd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        teleportRelativeX(60000)
        Unknown1007(10000)
    sprite('Action_136_00', 6)	# 1-6
    GFX_0('EffNmlAtk6CBlade2ndAdd', 100)
    sprite('Action_136_01', 3)	# 7-9
    sprite('Action_136_02', 4)	# 10-13
    sprite('Action_136_03', 5)	# 14-18
    sprite('Action_136_04', 1)	# 19-19

@State
def EffNmlAtk6CBlade2ndAdd():

    def upon_IMMEDIATE():
        Unknown4011(3)
    sprite('Action_110_00', 3)	# 1-3
    sprite('Action_110_01', 3)	# 4-6
    sprite('Action_110_02', 5)	# 7-11
    sprite('Action_110_03', 5)	# 12-16
    sprite('Action_110_04', 1)	# 17-17

@State
def EffNmlAtk6CBlade3rd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)

        def upon_43():
            if (SLOT_48 == 1000):
                teleportRelativeX(250000)
                Unknown2038(1)
    sprite('null', 1)	# 1-1
    sprite('Action_137_00', 6)	# 2-7
    GFX_0('EffNmlAtk6CBlade3rdAdd', 100)
    sprite('Action_137_01', 3)	# 8-10
    sprite('Action_137_02', 4)	# 11-14
    sprite('Action_137_03', 5)	# 15-19
    sprite('Action_137_04', 1)	# 20-20

@State
def EffNmlAtk6CBlade3rdAdd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(230000)
    sprite('Action_111_00', 3)	# 1-3
    sprite('Action_111_01', 3)	# 4-6
    sprite('Action_111_02', 5)	# 7-11
    sprite('Action_111_03', 5)	# 12-16
    sprite('Action_111_04', 1)	# 17-17

@State
def EffNmlAtk2ABlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_084_00', 6)	# 1-6
    sprite('Action_084_01', 6)	# 7-12
    sprite('Action_084_02', 1)	# 13-13

@State
def EffNmlAtk2BBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
    sprite('Action_097_00', 6)	# 1-6
    sprite('Action_097_01', 10)	# 7-16
    sprite('Action_097_02', 1)	# 17-17

@State
def EffNmlAtk2CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_093_00', 6)	# 1-6
    sprite('Action_093_01', 6)	# 7-12
    sprite('Action_093_02', 10)	# 13-22
    sprite('Action_093_03', 1)	# 23-23

@State
def EffNmlAtkAir5ABlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_088_00', 6)	# 1-6
    sprite('Action_088_01', 6)	# 7-12
    sprite('Action_088_02', 1)	# 13-13

@State
def EffNmlAtkAir5A2ndBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_089_00', 6)	# 1-6
    sprite('Action_089_01', 6)	# 7-12
    sprite('Action_089_02', 1)	# 13-13

@State
def EffNmlAtkAir5BBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_090_00', 6)	# 1-6
    sprite('Action_090_01', 6)	# 7-12
    sprite('Action_090_02', 1)	# 13-13

@State
def EffNmlAtkAir5CBlade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_092_00', 6)	# 1-6
    sprite('Action_092_01', 6)	# 7-12
    sprite('Action_092_02', 1)	# 13-13

@State
def Lin_430():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_430_00', 3)	# 1-3
    sprite('Action_430_01', 4)	# 4-7
    sprite('Action_430_02', 3)	# 8-10

@State
def Lin_432():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_432_00', 2)	# 1-2
    sprite('Action_432_01', 3)	# 3-5
    sprite('Action_432_02', 1)	# 6-6

@State
def Lin_433():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(3)
        teleportRelativeX(800000)
        Unknown1007(200000)
    sprite('Action_433_00', 2)	# 1-2
    sprite('Action_433_01', 5)	# 3-7	 **attackbox here**
    sprite('Action_433_02', 5)	# 8-12
    sprite('Action_433_03', 1)	# 13-13

@State
def Lin_434():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4009(3)
        teleportRelativeX(770000)
        Unknown1007(180000)
    sprite('Action_434_00', 3)	# 1-3
    sprite('Action_434_01', 4)	# 4-7	 **attackbox here**
    sprite('Action_434_02', 4)	# 8-11
    sprite('Action_434_03', 1)	# 12-12

@State
def EffNmlReversalAction00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_103_00', 3)	# 1-3
    sprite('Action_103_01', 3)	# 4-6
    sprite('Action_103_02', 3)	# 7-9
    sprite('Action_103_03', 1)	# 10-10

@State
def EffNmlReversalAction01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_104_00', 5)	# 1-5
    sprite('Action_104_01', 3)	# 6-8
    sprite('Action_104_02', 3)	# 9-11
    sprite('Action_104_03', 1)	# 12-12

@State
def EffShotSlash():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_430_00', 4)	# 1-4
    sprite('Action_430_01', 4)	# 5-8
    sprite('Action_430_02', 3)	# 9-11

@State
def EffARushSlash00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_225_00', 6)	# 1-6
    sprite('Action_225_01', 10)	# 7-16
    sprite('Action_225_02', 1)	# 17-17

@State
def EffARushSlash01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_226_00', 6)	# 1-6
    sprite('Action_226_01', 10)	# 7-16
    sprite('Action_226_02', 1)	# 17-17

@State
def EffBRushSlash00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_224_00', 6)	# 1-6
    sprite('Action_224_01', 10)	# 7-16
    sprite('Action_224_02', 1)	# 17-17

@State
def EffBRushSlash01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_226_00', 6)	# 1-6
    sprite('Action_226_01', 10)	# 7-16
    sprite('Action_226_02', 1)	# 17-17

@State
def EffARush2ndSlash00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_227_00', 6)	# 1-6
    sprite('Action_227_01', 10)	# 7-16
    sprite('Action_227_02', 1)	# 17-17

@State
def EffARush2ndSlash01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_228_00', 6)	# 1-6
    sprite('Action_228_01', 10)	# 7-16
    sprite('Action_228_02', 1)	# 17-17

@State
def EffBRush2ndSlash00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_237_00', 6)	# 1-6
    sprite('Action_237_01', 10)	# 7-16
    sprite('Action_237_02', 1)	# 17-17

@State
def EffBRush2ndSlash01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_238_00', 6)	# 1-6
    sprite('Action_238_01', 10)	# 7-16
    sprite('Action_238_02', 1)	# 17-17

@State
def EffBRush2ndSlash02():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_239_00', 6)	# 1-6
    sprite('Action_239_01', 10)	# 7-16
    sprite('Action_239_02', 1)	# 17-17

@State
def EffAssaultSlash():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(30000)
    sprite('Action_186_00', 3)	# 1-3
    sprite('Action_186_01', 5)	# 4-8
    sprite('Action_186_02', 3)	# 9-11
    sprite('Action_186_03', 1)	# 12-12

@State
def EffAirShotSlash():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(220000)
    sprite('Action_431_00', 4)	# 1-4
    sprite('Action_431_01', 4)	# 5-8
    sprite('Action_431_02', 3)	# 9-11

@State
def EffEXRushSlash00():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_234_00', 6)	# 1-6
    sprite('Action_234_01', 10)	# 7-16
    sprite('Action_234_02', 1)	# 17-17

@State
def EffEXRushSlash01():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_236_00', 6)	# 1-6
    sprite('Action_236_01', 10)	# 7-16
    sprite('Action_236_02', 1)	# 17-17

@State
def EffEXRushSlash02():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_237_00', 6)	# 1-6
    sprite('Action_237_01', 10)	# 7-16
    sprite('Action_237_02', 1)	# 17-17

@State
def EffEXRushSlash03():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_238_00', 6)	# 1-6
    sprite('Action_238_01', 10)	# 7-16
    sprite('Action_238_02', 1)	# 17-17

@State
def EffEXRushSlash04():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_239_00', 6)	# 1-6
    sprite('Action_239_01', 10)	# 7-16
    sprite('Action_239_02', 1)	# 17-17

@State
def EffEXRushSlash05():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_233_00', 6)	# 1-6
    sprite('Action_233_01', 10)	# 7-16
    sprite('Action_233_02', 1)	# 17-17

@State
def EffEXAssaultSlash():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_187_00', 3)	# 1-3
    sprite('Action_187_01', 5)	# 4-8
    sprite('Action_187_02', 3)	# 9-11
    sprite('Action_187_03', 1)	# 12-12

@State
def ShotA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(16000)
        AirUntechableTime(24)
        Unknown11001(-6, -6, -1)
        Unknown9016(1)
        sendToLabelUpon(10, 1)
        loopRelated(17, 10)
        sendToLabelUpon(17, 1)
    sprite('Action_435_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(65000)
    sprite('Action_435_01', 2)	# 3-4	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouA', 100)
    label(0)
    sprite('Action_435_00', 2)	# 5-6	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouA', 100)
    sprite('Action_435_01', 2)	# 7-8	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouA', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_06', 10)	# 9-18
    clearUponHandler(10)
    clearUponHandler(17)
    Unknown1019(10)
    Unknown23027()
    sprite('Action_435_07', 1)	# 19-19

@State
def ShotB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(16000)
        AirUntechableTime(24)
        Unknown11001(-6, -6, -1)
        Unknown9016(1)
        sendToLabelUpon(10, 1)
        loopRelated(17, 15)
        sendToLabelUpon(17, 1)
    sprite('Action_435_00', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(65000)
    sprite('Action_435_01', 2)	# 3-4	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouA', 100)
    label(0)
    sprite('Action_435_00', 2)	# 5-6	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouA', 100)
    sprite('Action_435_01', 2)	# 7-8	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouA', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_435_06', 10)	# 9-18
    clearUponHandler(10)
    clearUponHandler(17)
    Unknown1019(10)
    Unknown23027()
    GFX_0('ShotZanzouB', 100)
    sprite('Action_435_07', 1)	# 19-19

@State
def ShotAssist():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AttackP1(70)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(16000)
        AirUntechableTime(24)
        Unknown11001(-6, -6, -1)
        Unknown9016(1)
        Unknown11042(1)
        Unknown1007(-60000)
        physicsXImpulse(48000)
        physicsYImpulse(-10000)
        Unknown1108(90000)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 1)
        loopRelated(17, 25)
        sendToLabelUpon(17, 1)
    sprite('Action_437_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_437_01', 2)	# 3-4	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    label(0)
    sprite('Action_437_00', 2)	# 5-6	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    sprite('Action_437_01', 2)	# 7-8	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_437_05', 10)	# 9-18
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(17)
    Unknown1019(10)
    YAccel(10)
    label(2)
    sprite('Action_437_06', 1)	# 19-19

@State
def ShotZanzouA():

    def upon_IMMEDIATE():
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown1019(10)
        teleportRelativeX(-26000)
    sprite('Action_425_00', 10)	# 1-10

@State
def ShotZanzouB():

    def upon_IMMEDIATE():
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown1019(10)
        teleportRelativeX(-26000)
    sprite('Action_425_00', 10)	# 1-10

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(16000)
        AirUntechableTime(24)
        Unknown11001(-6, -6, -1)
        Unknown9016(1)
        Unknown1007(-60000)
        physicsXImpulse(36000)
        physicsYImpulse(-36000)
        Unknown1108(90000)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 1)
        loopRelated(17, 20)
        sendToLabelUpon(17, 1)
    sprite('Action_437_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_437_01', 2)	# 3-4	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    label(0)
    sprite('Action_437_00', 2)	# 5-6	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    sprite('Action_437_01', 2)	# 7-8	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_437_05', 10)	# 9-18
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(17)
    Unknown1019(10)
    YAccel(10)
    label(2)
    sprite('Action_437_06', 1)	# 19-19

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(16000)
        AirUntechableTime(24)
        Unknown11001(-6, -6, -1)
        Unknown9016(1)
        Unknown1007(-60000)
        physicsXImpulse(48000)
        physicsYImpulse(-10000)
        Unknown1108(90000)
        sendToLabelUpon(10, 1)
        sendToLabelUpon(2, 1)
        loopRelated(17, 20)
        sendToLabelUpon(17, 1)
    sprite('Action_437_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_437_01', 2)	# 3-4	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    label(0)
    sprite('Action_437_00', 2)	# 5-6	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    sprite('Action_437_01', 2)	# 7-8	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouA', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_437_05', 10)	# 9-18
    clearUponHandler(10)
    clearUponHandler(2)
    clearUponHandler(17)
    Unknown1019(10)
    YAccel(10)
    label(2)
    sprite('Action_437_06', 1)	# 19-19

@State
def AirShotZanzouA():

    def upon_IMMEDIATE():
        Unknown53(1)
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown48('19000000020000000d00000002000000020000000d000000')
        Unknown1019(10)
        YAccel(10)
        Unknown1108(90000)
    sprite('Action_427_00', 10)	# 1-10

@State
def AirShotZanzouB():

    def upon_IMMEDIATE():
        Unknown53(1)
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown48('19000000020000000d00000002000000020000000d000000')
        Unknown1019(10)
        YAccel(10)
        Unknown1108(90000)
    sprite('Action_427_00', 10)	# 1-10

@State
def ShotEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(75)
        Unknown11092(1)
        Unknown30065(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(12000)
        AirUntechableTime(24)
        PushbackX(44800)
        Hitstop(4)
        Unknown11001(-3, -3, 2)
        Unknown9016(1)
        Unknown11091(10)
        Unknown2053(1)
        Unknown23089('0300000001000000010000000100000001000000000000000300000003000000')
        sendToLabelUpon(54, 1)
        loopRelated(17, 15)
        sendToLabelUpon(17, 1)
    sprite('Action_436_01', 2)	# 1-2	 **attackbox here**
    physicsXImpulse(65000)
    GFX_0('ShotZanzouEX', 100)
    sprite('Action_436_02', 2)	# 3-4	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouEX', 100)
    label(0)
    sprite('Action_436_01', 2)	# 5-6	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouEX', 100)
    RefreshMultihit()
    Unknown9215()
    sprite('Action_436_02', 2)	# 7-8	 **attackbox here**
    Unknown1019(90)
    GFX_0('ShotZanzouEX', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_436_09', 10)	# 9-18
    clearUponHandler(54)
    clearUponHandler(17)
    Unknown1019(10)
    Unknown23027()
    sprite('Action_436_10', 1)	# 19-19

@State
def UltimateShot1():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(2000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(10000)
        AirUntechableTime(60)
        WallbounceReboundTime(0)
        Hitstop(2)
        Unknown9016(1)
        Unknown1096(1500)
        physicsXImpulse(75000)
        Unknown23089('0100000000000000000000000000000001000000000000000100000001000000')
        sendToLabelUpon(54, 1)
        loopRelated(17, 20)
        sendToLabelUpon(17, 1)
    label(0)
    sprite('Action_436_01', 2)	# 1-2	 **attackbox here**
    GFX_0('ShotZanzouEX', 100)
    sprite('Action_436_02', 2)	# 3-4	 **attackbox here**
    GFX_0('ShotZanzouEX', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_436_09', 10)	# 5-14
    clearUponHandler(54)
    clearUponHandler(17)
    Unknown1019(10)
    Unknown23027()
    sprite('Action_436_10', 1)	# 15-15

@State
def UltimateShot2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(2000)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(80000)
        AirPushbackY(10000)
        AirUntechableTime(60)
        WallbounceReboundTime(0)
        Hitstop(2)
        Unknown9016(1)
        Unknown1096(1500)
        physicsXImpulse(75000)
        teleportRelativeY(184800)
        Unknown23089('0100000000000000000000000000000001000000000000000100000001000000')
        sendToLabelUpon(54, 1)
        loopRelated(17, 20)
        sendToLabelUpon(17, 1)
    label(0)
    sprite('Action_436_01', 2)	# 1-2	 **attackbox here**
    GFX_0('ShotZanzouEX', 100)
    sprite('Action_436_02', 2)	# 3-4	 **attackbox here**
    GFX_0('ShotZanzouEX', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_436_09', 10)	# 5-14
    clearUponHandler(54)
    clearUponHandler(17)
    Unknown1019(10)
    Unknown23027()
    sprite('Action_436_10', 1)	# 15-15

@State
def ShotZanzouEX():

    def upon_IMMEDIATE():
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown1019(10)
        teleportRelativeX(-26000)
    sprite('Action_426_00', 10)	# 1-10

@State
def AirShotEX():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(75)
        Unknown11092(1)
        Unknown30065(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(12000)
        AirUntechableTime(24)
        PushbackX(12000)
        Hitstop(4)
        Unknown11001(-3, -3, 2)
        Unknown9016(1)
        Unknown11091(10)
        Unknown2053(1)
        physicsXImpulse(42000)
        physicsYImpulse(-36000)
        Unknown23089('0300000001000000010000000100000001000000000000000300000003000000')
        sendToLabelUpon(54, 1)

        def upon_LANDING():
            Unknown1019(10)
            YAccel(10)
        loopRelated(17, 20)
        sendToLabelUpon(17, 1)
    sprite('Action_438_01', 2)	# 1-2	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    sprite('Action_438_02', 2)	# 3-4	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouEX', 100)
    label(0)
    sprite('Action_438_01', 2)	# 5-6	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouEX', 100)
    RefreshMultihit()
    sprite('Action_438_02', 2)	# 7-8	 **attackbox here**
    Unknown1019(95)
    YAccel(95)
    GFX_0('AirShotZanzouEX', 100)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_438_09', 10)	# 9-18
    clearUponHandler(54)
    clearUponHandler(2)
    clearUponHandler(17)
    Unknown1019(10)
    YAccel(10)
    sprite('Action_438_10', 1)	# 19-19

@State
def AirShotZanzouEX():

    def upon_IMMEDIATE():
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown48('19000000020000000d00000002000000020000000d000000')
        Unknown1019(10)
        YAccel(10)
    sprite('Action_428_00', 10)	# 1-10

@State
def UltimateSlash():
    sprite('Action_191_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_191_01', 3)	# 5-7
    sprite('Action_191_02', 1)	# 8-8

@State
def UltimateSlashCrush():
    sprite('Action_191_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_191_01', 3)	# 5-7
    sprite('Action_191_02', 1)	# 8-8

@State
def UltimateLightwall():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(500)
        AttackP2(98)
        Unknown11091(15)
        Hitstop(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(15000)
        Unknown30055('881300003200000000000000')
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(100)
        Unknown11033(2)
        Unknown11108('03000000')
        Unknown2037(0)
        Unknown9021(1)
        Unknown2034(1)

        def upon_43():
            if (SLOT_48 == 5000):
                Damage(45)
                Unknown11091(100)
    sprite('null', 1)	# 1-1
    sprite('Action_195_00', 1)	# 2-2
    sprite('null', 5)	# 3-7
    GFX_0('UltimateLightwallEff', 100)
    Unknown38(4, 1)
    label(0)
    sprite('Action_195_01', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_195_02', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    Unknown2038(1)
    (SLOT_2 >= 7)
    if SLOT_0:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('Action_195_03', 1)	# 14-14
    Unknown21007(4, 32)
    sprite('null', 15)	# 15-29

@State
def UltimateLightwallEff():

    def upon_IMMEDIATE():

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
        Unknown4010(2)
        Unknown1007(-29000)

        def upon_41():
            GFX_0('DDD_Particle', -1)
    sprite('Action_193_00', 5)	# 1-5
    SFX_3('SE_ApperLightWall')
    SFX_3('SE_ApperLightWall')
    sprite('Action_193_01', 5)	# 6-10
    sprite('Action_193_02', 5)	# 11-15
    label(0)
    sprite('Action_193_03', 5)	# 16-20
    sprite('Action_193_04', 5)	# 21-25
    sprite('Action_193_05', 5)	# 26-30
    sprite('Action_193_06', 5)	# 31-35
    sprite('Action_193_07', 5)	# 36-40
    sprite('Action_193_08', 5)	# 41-45
    sprite('Action_193_09', 5)	# 46-50
    sprite('Action_193_10', 5)	# 51-55
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_193_11', 1)	# 56-56
    sprite('Action_194_00', 4)	# 57-60
    sprite('Action_194_01', 4)	# 61-64
    sprite('Action_194_02', 4)	# 65-68
    sprite('Action_194_03', 1)	# 69-69

@State
def UltimateSlashOD():
    sprite('Action_191_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_191_01', 3)	# 5-7
    sprite('Action_191_02', 1)	# 8-8

@State
def UltimateLightwallOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(400)
        AttackP2(99)
        Unknown11091(15)
        Hitstop(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(15000)
        Unknown30055('881300003200000000000000')
        YImpluseBeforeWallbounce(2300)
        AirUntechableTime(100)
        Unknown11033(2)
        Unknown11108('03000000')
        Unknown2037(0)
        Unknown9021(1)
        Unknown2034(1)
        Unknown1096(1250)

        def upon_43():
            if (SLOT_48 == 5000):
                Damage(50)
                Unknown11091(100)
    sprite('null', 5)	# 1-5
    sprite('Action_195_00', 1)	# 6-6
    sprite('null', 5)	# 7-11
    GFX_0('UltimateLightwallEffOD', 100)
    Unknown38(4, 1)
    label(0)
    sprite('Action_195_01', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_195_02', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    Unknown2038(1)
    (SLOT_2 >= 10)
    if SLOT_0:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('Action_195_03', 1)	# 18-18
    Unknown21007(4, 32)
    sprite('null', 15)	# 19-33

@State
def UltimateLightwallEffOD():

    def upon_IMMEDIATE():

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)
        Unknown4010(2)
        Unknown1007(-29000)
        Unknown1096(1250)

        def upon_41():
            GFX_0('DDD_Particle', -1)
    sprite('Action_193_00', 5)	# 1-5
    SFX_3('SE_ApperLightWall')
    SFX_3('SE_ApperLightWall')
    sprite('Action_193_01', 5)	# 6-10
    sprite('Action_193_02', 5)	# 11-15
    label(0)
    sprite('Action_193_03', 5)	# 16-20
    sprite('Action_193_04', 5)	# 21-25
    sprite('Action_193_05', 5)	# 26-30
    sprite('Action_193_06', 5)	# 31-35
    sprite('Action_193_07', 5)	# 36-40
    sprite('Action_193_08', 5)	# 41-45
    sprite('Action_193_09', 5)	# 46-50
    sprite('Action_193_10', 5)	# 51-55
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_193_11', 1)	# 56-56
    sprite('Action_194_00', 4)	# 57-60
    sprite('Action_194_01', 4)	# 61-64
    sprite('Action_194_02', 4)	# 65-68
    sprite('Action_194_03', 1)	# 69-69

@State
def UltimateLightwallDDD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(45)
        AttackP1(100)
        AttackP2(100)
        Hitstop(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(15000)
        Unknown30055('881300003200000000000000')
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(100)
        Unknown11091(100)
        Unknown11033(2)
        Unknown11108('03000000')
        Unknown2037(0)
        Unknown9021(1)
        Unknown2034(1)
    sprite('null', 1)	# 1-1
    sprite('Action_195_00', 1)	# 2-2
    sprite('null', 5)	# 3-7
    GFX_0('UltimateLightwallEff', 100)
    Unknown38(4, 1)
    label(0)
    sprite('Action_195_01', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_195_02', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    Unknown2038(1)
    (SLOT_2 >= 7)
    if SLOT_0:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('Action_195_03', 1)	# 14-14
    Unknown21007(4, 32)
    sprite('null', 15)	# 15-29

@State
def UltimateLightwallDDDOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(50)
        AttackP1(100)
        AttackP2(100)
        Hitstop(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(15000)
        Unknown30055('881300003200000000000000')
        YImpluseBeforeWallbounce(2300)
        AirUntechableTime(100)
        Unknown11091(100)
        Unknown11033(2)
        Unknown11108('03000000')
        Unknown2037(0)
        Unknown9021(1)
        Unknown2034(1)
        Unknown1096(1250)
    sprite('null', 5)	# 1-5
    sprite('Action_195_00', 1)	# 6-6
    sprite('null', 5)	# 7-11
    GFX_0('UltimateLightwallEffOD', 100)
    Unknown38(4, 1)
    label(0)
    sprite('Action_195_01', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_195_02', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    Unknown2038(1)
    (SLOT_2 >= 10)
    if SLOT_0:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('Action_195_03', 1)	# 18-18
    Unknown21007(4, 32)
    sprite('null', 15)	# 19-33

@State
def UltimateAssaultFinish():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_192_00', 6)	# 1-6
    sprite('Action_192_01', 4)	# 7-10
    sprite('Action_192_02', 8)	# 11-18
    sprite('Action_192_03', 1)	# 19-19

@State
def UltimateRushEff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown23022(1)
        Unknown2003(1)
        Unknown2017(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown23015(11)
        Unknown2019(-1)
    sprite('Action_189_00ex01', 5)	# 1-5
    sprite('Action_189_01ex01', 8)	# 6-13
    sprite('Action_189_02ex01', 7)	# 14-20
    sprite('Action_189_03ex01', 6)	# 21-26
    sprite('Action_189_04ex01', 5)	# 27-31
    sprite('Action_189_05ex01', 4)	# 32-35
    sprite('Action_189_06ex01', 4)	# 36-39
    sprite('Action_189_07ex01', 4)	# 40-43
    sprite('Action_189_08ex01', 3)	# 44-46
    sprite('Action_189_09ex01', 3)	# 47-49
    Unknown23015(1)
    Unknown2019(1)
    sprite('Action_190_00ex01', 5)	# 50-54
    teleportRelativeX(95000)
    sprite('Action_190_01ex01', 5)	# 55-59
    teleportRelativeX(-95000)
    sprite('Action_190_02ex01', 4)	# 60-63
    sprite('Action_190_03ex01', 4)	# 64-67
    sprite('Action_190_04ex01', 4)	# 68-71
    sprite('Action_190_05ex01', 4)	# 72-75
    sprite('Action_190_06ex01', 3)	# 76-78
    sprite('Action_190_07ex01', 3)	# 79-81
    sprite('Action_190_08ex01', 4)	# 82-85
    sprite('Action_190_09ex01', 2)	# 86-87
    sprite('Action_190_10ex01', 2)	# 88-89
    sprite('Action_190_11ex01', 2)	# 90-91
    sprite('Action_190_12ex01', 2)	# 92-93
    sprite('Action_190_13ex01', 2)	# 94-95
    sprite('Action_190_14ex01', 2)	# 96-97
    sprite('Action_190_15ex01', 2)	# 98-99
    sprite('Action_190_16ex01', 2)	# 100-101
    sprite('Action_190_10ex01', 2)	# 102-103
    sprite('Action_190_11ex01', 2)	# 104-105
    sprite('Action_190_12ex01', 2)	# 106-107
    sprite('Action_190_13ex01', 2)	# 108-109
    sprite('Action_190_14ex01', 2)	# 110-111
    sprite('Action_190_15ex01', 2)	# 112-113
    sprite('Action_190_16ex01', 2)	# 114-115
    sprite('Action_190_17ex01', 2)	# 116-117
    sprite('Action_190_18ex01', 2)	# 118-119
    sprite('Action_190_19ex01', 2)	# 120-121
    sprite('Action_190_20ex01', 2)	# 122-123
    sprite('Action_190_21ex01', 3)	# 124-126
    sprite('Action_190_22ex01', 4)	# 127-130
    sprite('Action_190_23ex01', 6)	# 131-136
    sprite('Action_190_24ex01', 6)	# 137-142
    sprite('Action_190_25ex01', 7)	# 143-149
    sprite('Action_190_26ex01', 10)	# 150-159
    sprite('Action_190_27ex01', 2)	# 160-161
    sprite('Action_190_28ex01', 4)	# 162-165
    sprite('Action_190_29ex01', 28)	# 166-193
    sprite('Action_190_30ex01', 2)	# 194-195
    sprite('Action_190_31ex01', 6)	# 196-201
    sprite('Action_190_32ex01', 3)	# 202-204
    sprite('Action_190_33ex01', 5)	# 205-209
    sprite('Action_190_34ex01', 3)	# 210-212
    sprite('Action_190_35ex01', 6)	# 213-218
    sprite('Action_190_36ex01', 3)	# 219-221

@State
def UltimateRushEffOD():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown23022(1)
        Unknown2003(1)
        Unknown2017(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown23015(11)
        Unknown2019(-1)
    sprite('Action_189_00ex01', 5)	# 1-5
    sprite('Action_189_01ex01', 8)	# 6-13
    sprite('Action_189_02ex01', 7)	# 14-20
    sprite('Action_189_03ex01', 6)	# 21-26
    sprite('Action_189_04ex01', 5)	# 27-31
    sprite('Action_189_05ex01', 4)	# 32-35
    sprite('Action_189_06ex01', 4)	# 36-39
    sprite('Action_189_07ex01', 4)	# 40-43
    sprite('Action_189_08ex01', 3)	# 44-46
    sprite('Action_189_09ex01', 3)	# 47-49
    Unknown23015(1)
    Unknown2019(1)
    sprite('Action_190_00ex01', 5)	# 50-54
    teleportRelativeX(95000)
    sprite('Action_190_01ex01', 5)	# 55-59
    teleportRelativeX(-95000)
    sprite('Action_190_02ex01', 4)	# 60-63
    sprite('Action_190_03ex01', 4)	# 64-67
    sprite('Action_190_04ex01', 4)	# 68-71
    sprite('Action_190_05ex01', 4)	# 72-75
    sprite('Action_190_06ex01', 3)	# 76-78
    sprite('Action_190_07ex01', 3)	# 79-81
    sprite('Action_190_08ex01', 4)	# 82-85
    sprite('Action_190_00ex01', 2)	# 86-87
    label(1)
    sprite('Action_190_01ex01', 2)	# 88-89
    sprite('Action_190_02ex01', 2)	# 90-91
    sprite('Action_190_03ex01', 2)	# 92-93
    sprite('Action_190_04ex01', 2)	# 94-95
    sprite('Action_190_05ex01', 2)	# 96-97
    sprite('Action_190_06ex01', 2)	# 98-99
    sprite('Action_190_07ex01', 2)	# 100-101
    sprite('Action_190_08ex01', 2)	# 102-103
    label(2)
    sprite('Action_190_01ex01', 2)	# 104-105
    sprite('Action_190_02ex01', 2)	# 106-107
    sprite('Action_190_03ex01', 2)	# 108-109
    sprite('Action_190_04ex01', 2)	# 110-111
    sprite('Action_190_05ex01', 2)	# 112-113
    sprite('Action_190_06ex01', 2)	# 114-115
    sprite('Action_190_07ex01', 2)	# 116-117
    sprite('Action_190_08ex01', 2)	# 118-119
    label(3)
    sprite('Action_190_01ex01', 2)	# 120-121
    sprite('Action_190_02ex01', 2)	# 122-123
    sprite('Action_190_03ex01', 2)	# 124-125
    sprite('Action_190_04ex01', 2)	# 126-127
    sprite('Action_190_05ex01', 2)	# 128-129
    sprite('Action_190_06ex01', 2)	# 130-131
    sprite('Action_190_07ex01', 2)	# 132-133
    sprite('Action_190_08ex01', 2)	# 134-135
    label(4)
    sprite('Action_190_01ex01', 2)	# 136-137
    sprite('Action_190_02ex01', 2)	# 138-139
    sprite('Action_190_03ex01', 2)	# 140-141
    sprite('Action_190_04ex01', 2)	# 142-143
    sprite('Action_190_05ex01', 2)	# 144-145
    sprite('Action_190_06ex01', 2)	# 146-147
    sprite('Action_190_07ex01', 2)	# 148-149
    sprite('Action_190_08ex01', 2)	# 150-151
    sprite('Action_190_09ex01', 2)	# 152-153
    sprite('Action_190_10ex01', 2)	# 154-155
    sprite('Action_190_11ex01', 2)	# 156-157
    sprite('Action_190_12ex01', 2)	# 158-159
    sprite('Action_190_13ex01', 2)	# 160-161
    sprite('Action_190_14ex01', 2)	# 162-163
    sprite('Action_190_15ex01', 2)	# 164-165
    sprite('Action_190_16ex01', 2)	# 166-167
    sprite('Action_190_17ex01', 2)	# 168-169
    sprite('Action_190_18ex01', 2)	# 170-171
    sprite('Action_190_19ex01', 2)	# 172-173
    sprite('Action_190_20ex01', 2)	# 174-175
    sprite('Action_190_21ex01', 3)	# 176-178
    sprite('Action_190_22ex01', 4)	# 179-182
    sprite('Action_190_23ex01', 6)	# 183-188
    sprite('Action_190_24ex01', 6)	# 189-194
    sprite('Action_190_25ex01', 7)	# 195-201
    sprite('Action_190_26ex01', 10)	# 202-211
    sprite('Action_190_27ex01', 2)	# 212-213
    sprite('Action_190_28ex01', 4)	# 214-217
    sprite('Action_190_29ex01', 38)	# 218-255
    sprite('Action_190_30ex01', 2)	# 256-257
    sprite('Action_190_31ex01', 6)	# 258-263
    sprite('Action_190_32ex01', 3)	# 264-266
    sprite('Action_190_33ex01', 5)	# 267-271
    sprite('Action_190_34ex01', 3)	# 272-274
    sprite('Action_190_35ex01', 6)	# 275-280
    sprite('Action_190_36ex01', 3)	# 281-283

@State
def Lin_156():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2054(1)
    sprite('Action_156_00', 5)	# 1-5
    sprite('Action_156_01', 5)	# 6-10
    sprite('Action_156_02', 1)	# 11-11

@State
def Lin_157():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_157_00', 4)	# 1-4
    sprite('Action_157_01', 4)	# 5-8
    sprite('Action_157_02', 1)	# 9-9

@State
def Lin_160_1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(180000)
        Unknown1007(250000)
    sprite('Action_160_12ex', 2)	# 1-2
    sprite('Action_160_13ex', 2)	# 3-4
    sprite('Action_160_14ex', 1)	# 5-5

@State
def Lin_160_2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2005()
        Unknown1072(-20000)
        teleportRelativeX(80000)
    sprite('Action_160_12ex', 3)	# 1-3
    sprite('Action_160_13ex', 3)	# 4-6
    sprite('Action_160_14ex', 1)	# 7-7

@State
def Lin_160_3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(30000)
    sprite('Action_160_03ex', 2)	# 1-2
    sprite('Action_160_04ex', 2)	# 3-4
    sprite('Action_160_05ex', 1)	# 5-5	 **attackbox here**

@State
def Lin_160_4():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(20000)
        Unknown2005()
    sprite('Action_160_03ex', 4)	# 1-4
    sprite('Action_160_04ex', 4)	# 5-8
    sprite('Action_160_05ex', 1)	# 9-9	 **attackbox here**

@State
def Lin_160_5():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_160_12ex', 4)	# 1-4
    sprite('Action_160_13ex', 4)	# 5-8
    sprite('Action_160_14ex', 4)	# 9-12

@State
def Lin_166_1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(-30000)
        teleportRelativeX(140000)
    sprite('Action_166_00', 3)	# 1-3
    sprite('Action_166_01', 3)	# 4-6
    sprite('Action_166_02', 1)	# 7-7

@State
def Lin_166_2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_166_00', 3)	# 1-3
    sprite('Action_166_01', 3)	# 4-6
    sprite('Action_166_02', 1)	# 7-7

@State
def Lin_166_3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(-30000)
        Unknown1007(-250000)
    sprite('Action_166_00', 2)	# 1-2
    sprite('Action_166_01', 2)	# 3-4
    sprite('Action_166_02', 1)	# 5-5

@State
def Lin_168_1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(30000)
        teleportRelativeX(-400000)
        Unknown1007(400000)
    sprite('Action_168_01', 3)	# 1-3
    sprite('Action_168_02', 3)	# 4-6
    sprite('Action_168_03', 1)	# 7-7

@State
def Lin_168_2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1072(-80000)
    sprite('Action_168_01', 2)	# 1-2
    sprite('Action_168_02', 2)	# 3-4
    sprite('Action_168_03', 1)	# 5-5

@State
def Lin_168_3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_168_01', 4)	# 1-4
    sprite('Action_168_02', 4)	# 5-8
    sprite('Action_168_03', 1)	# 9-9

@State
def Lin_169():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_169_00', 4)	# 1-4
    sprite('Action_169_01', 4)	# 5-8
    sprite('Action_169_02', 1)	# 9-9

@State
def Lin_091():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_091_00', 6)	# 1-6
    sprite('Action_091_01', 6)	# 7-12
    sprite('Action_091_02', 1)	# 13-13

@State
def Lin_224():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_224_00', 6)	# 1-6
    sprite('Action_224_01', 10)	# 7-16
    sprite('Action_224_02', 1)	# 17-17

@State
def Astral_CutIn():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
        Unknown2017(0)
        Unknown2053(0)
        Unknown2034(0)
    sprite('Action_999_01', 3)	# 1-3
    sprite('Action_999_02', 3)	# 4-6
    sprite('Action_999_03', 4)	# 7-10
    sprite('Action_999_04', 4)	# 11-14
    sprite('Action_999_05', 4)	# 15-18	 **attackbox here**
    sprite('Action_999_06', 3)	# 19-21	 **attackbox here**
    sprite('Action_999_07', 3)	# 22-24	 **attackbox here**
    sprite('Action_999_08', 3)	# 25-27	 **attackbox here**
    sprite('Action_999_09', 3)	# 28-30	 **attackbox here**
    sprite('Action_999_10', 4)	# 31-34	 **attackbox here**
    sprite('Action_999_11', 5)	# 35-39	 **attackbox here**
    sprite('Action_999_12', 8)	# 40-47	 **attackbox here**
    sprite('Action_999_13', 4)	# 48-51	 **attackbox here**
    sprite('Action_999_14', 3)	# 52-54
    sprite('Action_999_15', 3)	# 55-57
    sprite('Action_999_16', 2)	# 58-59
    sprite('Action_999_17', 3)	# 60-62	 **attackbox here**
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)
    sprite('Action_999_18', 3)	# 63-65	 **attackbox here**
    sprite('Action_999_19', 3)	# 66-68	 **attackbox here**
    sprite('Action_999_20', 1)	# 69-69	 **attackbox here**

@State
def Astral_272():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1000(-200000)
        teleportRelativeY(-350000)
    sprite('Action_272_00', 4)	# 1-4
    sprite('Action_272_01', 5)	# 5-9
    sprite('Action_272_02', 5)	# 10-14
    sprite('Action_272_03', 5)	# 15-19
    sprite('Action_272_04', 5)	# 20-24
    sprite('Action_272_05', 5)	# 25-29
    sprite('Action_272_06', 2)	# 30-31
    sprite('Action_272_07', 20)	# 32-51

@State
def Astral_274_2_Parent():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown1000(0)
        teleportRelativeY(1409000)
        Unknown2019(4000)
    sprite('null', 16)	# 1-16
    GFX_0('Astral_274_2', -1)
    Unknown20000(1)

@State
def Astral_274():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown1000(0)
        Unknown23033(0)
        Unknown2019(4000)
    sprite('Action_274_00', 16)	# 1-16
    sprite('Action_274_01', 16)	# 17-32
    sprite('Action_274_02', 16)	# 33-48
    sprite('Action_274_03', 16)	# 49-64
    sprite('Action_274_04', 16)	# 65-80
    sprite('Action_274_05', 50)	# 81-130
    loopRest()

@State
def Astral_274_2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2019(4000)
    label(0)
    sprite('Action_274_05', 1)	# 1-1
    Unknown23057(50)
    Unknown23058(50)
    gotoLabel(0)

@State
def Astral_275():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)
    sprite('Action_275_00', 7)	# 1-7
    sprite('Action_275_01', 7)	# 8-14
    sprite('Action_275_02', 7)	# 15-21
    sprite('Action_275_03', 7)	# 22-28
    sprite('Action_275_04', 7)	# 29-35
    sprite('Action_275_05', 7)	# 36-42
    sprite('Action_275_06', 67)	# 43-109
    sprite('Action_275_07', 1)	# 110-110

@State
def Astral_276():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_276_00', 6)	# 1-6
    sprite('Action_276_01', 6)	# 7-12
    sprite('Action_276_02', 8)	# 13-20
    sprite('Action_276_03', 10)	# 21-30
    sprite('Action_276_04', 12)	# 31-42
    sprite('Action_276_05', 14)	# 43-56
    sprite('Action_276_06', 16)	# 57-72
    sprite('Action_276_07', 18)	# 73-90
    sprite('Action_276_08', 20)	# 91-110
    sprite('Action_276_09', 1)	# 111-111

@State
def Astral_277():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-500)
    sprite('Action_277_00', 4)	# 1-4
    sprite('Action_277_01', 4)	# 5-8
    sprite('Action_277_02', 4)	# 9-12
    sprite('Action_277_03', 4)	# 13-16
    sprite('Action_277_04', 4)	# 17-20
    sprite('Action_277_05', 4)	# 21-24
    sprite('Action_277_06', 1)	# 25-25

@State
def Astral_278():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(-100000)
        physicsYImpulse(-200)
        Unknown2005()
    sprite('Action_278_00', 3)	# 1-3
    GFX_0('Astral_287', 100)
    sprite('Action_278_01', 3)	# 4-6
    sprite('Action_278_02', 3)	# 7-9
    sprite('Action_278_03', 3)	# 10-12
    sprite('Action_278_04', 3)	# 13-15
    sprite('Action_278_05', 3)	# 16-18
    sprite('Action_278_06', 3)	# 19-21
    sprite('Action_278_02', 3)	# 22-24
    sprite('Action_278_03', 3)	# 25-27
    sprite('Action_278_04', 3)	# 28-30
    sprite('Action_278_05', 3)	# 31-33
    sprite('Action_278_06', 3)	# 34-36
    sprite('Action_278_02', 3)	# 37-39
    sprite('Action_278_03', 3)	# 40-42
    sprite('Action_278_04', 3)	# 43-45
    sprite('Action_278_05', 3)	# 46-48
    sprite('Action_278_06', 3)	# 49-51
    sprite('Action_278_02', 3)	# 52-54
    sprite('Action_278_03', 3)	# 55-57
    sprite('Action_278_04', 3)	# 58-60
    sprite('Action_278_05', 3)	# 61-63
    sprite('Action_278_06', 3)	# 64-66
    sprite('Action_278_02', 3)	# 67-69
    sprite('Action_278_04', 3)	# 70-72
    sprite('Action_278_05', 3)	# 73-75
    sprite('Action_278_06', 3)	# 76-78
    sprite('Action_278_02', 3)	# 79-81
    Unknown3026(-1)
    Unknown3025(-16777216, 40)
    sprite('Action_278_03', 3)	# 82-84
    sprite('Action_278_04', 3)	# 85-87
    sprite('Action_278_05', 3)	# 88-90
    sprite('Action_278_06', 3)	# 91-93
    sprite('Action_278_02', 3)	# 94-96
    sprite('Action_278_03', 3)	# 97-99
    Unknown3004(-10)
    sprite('Action_278_04', 3)	# 100-102
    sprite('Action_278_05', 3)	# 103-105
    sprite('Action_278_06', 3)	# 106-108
    sprite('Action_278_02', 3)	# 109-111
    sprite('Action_278_03', 3)	# 112-114
    sprite('Action_278_04', 3)	# 115-117
    sprite('Action_278_05', 3)	# 118-120
    sprite('Action_278_06', 3)	# 121-123
    sprite('Action_278_02', 3)	# 124-126
    sprite('Action_278_03', 3)	# 127-129

@State
def Astral_279():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown1086(22)
        Unknown1007(200000)
    sprite('Action_279_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_279_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_279_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_279_00', 3)	# 10-12	 **attackbox here**
    sprite('Action_279_01', 3)	# 13-15	 **attackbox here**
    sprite('Action_279_02', 3)	# 16-18	 **attackbox here**
    sprite('Action_279_00', 3)	# 19-21	 **attackbox here**
    sprite('Action_279_01', 3)	# 22-24	 **attackbox here**
    sprite('Action_279_02', 3)	# 25-27	 **attackbox here**
    sprite('Action_279_00', 3)	# 28-30	 **attackbox here**
    sprite('Action_279_01', 3)	# 31-33	 **attackbox here**
    sprite('Action_279_02', 3)	# 34-36	 **attackbox here**
    sprite('Action_279_00', 3)	# 37-39	 **attackbox here**
    sprite('Action_279_01', 3)	# 40-42	 **attackbox here**
    sprite('Action_279_02', 3)	# 43-45	 **attackbox here**
    sprite('Action_279_00', 3)	# 46-48	 **attackbox here**
    sprite('Action_279_01', 3)	# 49-51	 **attackbox here**
    sprite('Action_279_02', 3)	# 52-54	 **attackbox here**
    sprite('Action_279_00', 3)	# 55-57	 **attackbox here**
    sprite('Action_279_01', 3)	# 58-60	 **attackbox here**
    sprite('Action_279_02', 3)	# 61-63	 **attackbox here**
    sprite('Action_279_00', 3)	# 64-66	 **attackbox here**
    sprite('Action_279_01', 3)	# 67-69	 **attackbox here**
    sprite('Action_279_02', 3)	# 70-72	 **attackbox here**
    sprite('Action_279_00', 3)	# 73-75	 **attackbox here**
    sprite('Action_279_01', 3)	# 76-78	 **attackbox here**
    sprite('Action_279_02', 3)	# 79-81	 **attackbox here**
    sprite('Action_279_00', 3)	# 82-84	 **attackbox here**
    sprite('Action_279_01', 3)	# 85-87	 **attackbox here**
    sprite('Action_279_02', 3)	# 88-90	 **attackbox here**
    sprite('Action_279_03', 1)	# 91-91	 **attackbox here**
    sprite('Action_279_04', 7)	# 92-98	 **attackbox here**
    sprite('Action_279_05', 7)	# 99-105	 **attackbox here**
    sprite('Action_279_06', 7)	# 106-112	 **attackbox here**
    sprite('Action_279_07', 7)	# 113-119	 **attackbox here**
    sprite('Action_279_11', 3)	# 120-122	 **attackbox here**
    sprite('Action_279_12', 1)	# 123-123	 **attackbox here**

@State
def Astral_280():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_280_00', 4)	# 1-4
    sprite('Action_280_01', 4)	# 5-8
    sprite('Action_280_02', 1)	# 9-9

@State
def Astral_281():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_281_00', 4)	# 1-4
    sprite('Action_281_01', 4)	# 5-8
    sprite('Action_281_02', 1)	# 9-9

@State
def Astral_282():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_282_00', 4)	# 1-4
    sprite('Action_282_01', 4)	# 5-8
    sprite('Action_282_02', 1)	# 9-9

@State
def Astral_283():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_283_00', 4)	# 1-4
    sprite('Action_283_01', 4)	# 5-8
    sprite('Action_283_02', 1)	# 9-9

@State
def Astral_284():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_284_00', 4)	# 1-4
    sprite('Action_284_01', 4)	# 5-8
    sprite('Action_284_02', 1)	# 9-9

@State
def Astral_286():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2005()
        teleportRelativeX(210000)
        Unknown1007(-40000)
    label(0)
    sprite('Action_286_00', 4)	# 1-4
    sprite('Action_286_01', 4)	# 5-8
    gotoLabel(0)

@State
def Astral_287():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown2005()
        teleportRelativeX(210000)
        Unknown1007(-40000)
    label(0)
    sprite('Action_287_00', 4)	# 1-4
    sprite('Action_287_01', 4)	# 5-8
    sprite('Action_287_02', 4)	# 9-12
    sprite('Action_287_03', 4)	# 13-16
    sprite('Action_287_04', 4)	# 17-20
    gotoLabel(0)

@State
def Astral_289_1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2019(100)
        Unknown3001(200)

        def upon_43():
            if (SLOT_48 == 7000):
                sendToLabel(0)
    sprite('Action_270_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_289_01', 3)	# 5-7
    physicsXImpulse(30000)
    sprite('Action_289_02', 3)	# 8-10
    sprite('Action_289_03', 2)	# 11-12
    sprite('Action_289_04', 2)	# 13-14
    sprite('Action_289_05', 2)	# 15-16
    sprite('Action_289_06', 2)	# 17-18
    sprite('Action_289_07', 2)	# 19-20
    sprite('Action_289_00', 2)	# 21-22
    sprite('Action_270_11', 3)	# 23-25	 **attackbox here**
    sprite('Action_045_11', 4)	# 26-29
    Unknown1019(80)
    sprite('Action_045_12', 5)	# 30-34
    sprite('Action_045_11', 4)	# 35-38
    Unknown1019(50)
    sprite('Action_045_12', 5)	# 39-43
    Unknown1019(0)
    sprite('Action_045_13', 6)	# 44-49
    label(0)
    sprite('keep', 1)	# 50-50

@State
def Astral_289_2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2019(100)
        Unknown3001(200)

        def upon_43():
            if (SLOT_48 == 7000):
                sendToLabel(0)
    sprite('Action_270_00', 8)	# 1-8	 **attackbox here**
    sprite('Action_289_01', 3)	# 9-11
    physicsXImpulse(30000)
    sprite('Action_289_02', 3)	# 12-14
    sprite('Action_289_03', 2)	# 15-16
    sprite('Action_289_04', 2)	# 17-18
    sprite('Action_289_05', 2)	# 19-20
    sprite('Action_289_06', 2)	# 21-22
    sprite('Action_289_07', 2)	# 23-24
    sprite('Action_289_00', 2)	# 25-26
    sprite('Action_270_11', 3)	# 27-29	 **attackbox here**
    sprite('Action_045_11', 4)	# 30-33
    Unknown1019(80)
    sprite('Action_045_12', 5)	# 34-38
    sprite('Action_045_11', 4)	# 39-42
    Unknown1019(50)
    sprite('Action_045_12', 5)	# 43-47
    Unknown1019(0)
    sprite('Action_045_13', 6)	# 48-53
    label(0)
    sprite('keep', 1)	# 54-54

@State
def Astral_Atk_dmy():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        Damage(18000)
        Unknown11091(100)
        Hitstop(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1086(22)
        Unknown11001(0, 10, 0)
        AirPushbackX(3000)
        AirPushbackY(150000)
    sprite('astral_dmy', 5)	# 1-5	 **attackbox here**

@State
def TagCutIn():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(2000)
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-580000)
        Unknown1001(640000)
        SFX_0('301_overdrive_end')
        loopRelated(17, 30)

        def upon_17():
            sendToLabel(1)
    sprite('Action_997_01', 2)	# 1-2
    sprite('Action_997_02', 2)	# 3-4
    sprite('Action_997_03', 2)	# 5-6
    label(0)
    sprite('Action_997_04', 3)	# 7-9
    sprite('Action_997_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 13-13

@State
def DDCutIn():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2019(2000)
        Unknown6001(1)
        Unknown2054(1)
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-700000)
        Unknown1001(440000)

@State
def Geboku():

    def upon_IMMEDIATE():
        Unknown2037(1)
        Unknown1086(3)
        teleportRelativeX(-100000)
        Unknown1007(300000)

        def upon_43():
            if (SLOT_48 == 9900):
                if (not SLOT_2):
                    Unknown1086(3)
                    teleportRelativeX(-100000)
                    Unknown1007(300000)
                Unknown2037(1)
            if (SLOT_48 == 9901):
                Unknown2037(0)
            if (SLOT_48 == 9902):
                Unknown1086(3)
                teleportRelativeX(-100000)
                Unknown1007(300000)

        def upon_3():
            Unknown2071('030000006079feffe09304000300000000000000')
            if (SLOT_23 > 1400000):
                teleportRelativeY(1400000)
            Unknown59('19000000640000000300000064000000')
            SLOT_63 = SLOT_0
            Unknown48('19000000020000003b000000190000000200000013000000')
            Unknown48('19000000020000003c000000030000000200000013000000')
            Unknown47('01000000020000003b000000020000003c000000020000003d000000')
            if (SLOT_59 > SLOT_60):
                SLOT_62 = 1
            else:
                SLOT_62 = 2
            if op(15, 2, 62, 0, 0):
                if (SLOT_63 > 2000000):
                    Unknown1086(3)
                    teleportRelativeX(-100000)
                    Unknown1007(300000)
            if SLOT_2:
                Unknown1096(1000)
            else:
                Unknown1096(0)

            def upon_53():
                clearUponHandler(43)
                SLOT_51 = 1
                if SLOT_158:
                    GFX_0('GebokuBattleOut', -1)
            if SLOT_51:
                Unknown1096(0)
    sprite('null', 32767)	# 1-32767
    GFX_0('GebokuFloat', -1)

@State
def GebokuFloat():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4013(2)
        Unknown1084(1)
    sprite('null', 1)	# 1-1
    GFX_0('GebokuImage', -1)
    label(0)
    sprite('keep', 30)	# 2-31
    physicsYImpulse(250)
    setGravity(15)
    sprite('keep', 30)	# 32-61
    Unknown1019(0)
    Unknown1028(-5)
    sprite('keep', 30)	# 62-91
    physicsYImpulse(-250)
    setGravity(-15)
    sprite('keep', 30)	# 92-121
    Unknown1019(0)
    Unknown1028(5)
    loopRest()
    gotoLabel(0)

@State
def GebokuImage():

    def upon_IMMEDIATE():
        Unknown4025(3)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4019(3)
        Unknown2019(1)
        Unknown32('4765626f6b75416e696d4374726c0000')
    sprite('null', 100)	# 1-100
    enterState('GebokuNeutral')

@State
def GebokuNeutral():
    label(0)
    sprite('Action_990_00', 1)	# 1-1
    sprite('Action_990_01', 7)	# 2-8
    sprite('Action_990_02', 6)	# 9-14
    sprite('Action_990_03', 6)	# 15-20
    sprite('Action_990_04', 7)	# 21-27
    gotoLabel(0)

@State
def GebokuFmove():
    sprite('Action_990_05', 1)	# 1-1
    label(0)
    sprite('Action_990_06', 7)	# 2-8
    sprite('Action_990_07', 6)	# 9-14
    sprite('Action_990_08', 6)	# 15-20
    sprite('Action_990_09', 7)	# 21-27
    gotoLabel(0)

@State
def GebokuBmove():
    label(0)
    sprite('Action_990_10', 7)	# 1-7
    sprite('Action_990_11', 7)	# 8-14
    sprite('Action_990_12', 7)	# 15-21
    sprite('Action_990_13', 7)	# 22-28
    gotoLabel(0)

@State
def GebokuTurn():
    sprite('Action_990_14', 7)	# 1-7
    Unknown2005()
    sprite('Action_990_00', 1)	# 8-8
    sprite('keep', 100)	# 9-108
    enterState('GebokuNeutral')

@State
def GebokuBattleOut():

    def upon_IMMEDIATE():
        Unknown2005()
        physicsXImpulse(2500)
    sprite('null', 1)	# 1-1
    sprite('Action_990_05', 1)	# 2-2
    sprite('Action_990_06', 7)	# 3-9
    Unknown1019(200)
    Unknown3001(255)
    Unknown3004(-10)
    sprite('Action_990_07', 6)	# 10-15
    Unknown1019(200)
    sprite('Action_990_08', 6)	# 16-21
    sprite('Action_990_09', 7)	# 22-28

@State
def DDD_Particle():

    def upon_IMMEDIATE():
        pass
    sprite('null', 5)	# 1-5
    Unknown4047(249, 249, 249)
    Unknown4045('756c6965665f4444445f737061726b6c65000000000000000000000000000000ffffffff')