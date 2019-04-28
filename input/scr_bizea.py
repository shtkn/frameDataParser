@State
def EMB_IZ():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f495a2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown1096(900)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 8)
    Unknown3025(-1, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 18)

@State
def EMB_IZ_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f495a2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown1096(900)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 18)

@State
def EMB_IZ_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f495a2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown1096(900)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 8)
    Unknown3025(-55256, 10)
    sprite('null', 8)
    Unknown3025(-19276, 10)
    sprite('null', 8)
    Unknown3025(-65536, 10)
    sprite('null', 18)

@Subroutine
def LightSaverSwitch():
    Unknown3033()
    Unknown4061(2)
    Unknown3053(1)
    Unknown3001(255)
    Unknown3040(2)
    Unknown3042(243)
    Unknown3041(244)
    Unknown3043(245)

@Subroutine
def ShotColorSwitch():
    Unknown4061(5)

@State
def KakuseiMagicCircle():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f6d61676963636972636c6530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(300)
        teleportRelativeX(-20000)
        Unknown1007(10000)
        Unknown3001(160)
        Unknown1072(0)
        sendToLabelUpon(56, 1)
    sprite('null', 8)
    Unknown3026(-3639041)
    Unknown3025(-128, 8)
    sprite('null', 32767)
    Unknown23131()
    label(1)
    sprite('null', 3)
    Unknown4007(0)
    Unknown4010(0)
    Unknown3001(120)
    Unknown3004(-20)
    Unknown1099(20)

@State
def KakuseiMagicCircleDD():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f6d61676963636972636c6530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(300)
        teleportRelativeX(-20000)
        Unknown1007(10000)
        Unknown3001(160)
        Unknown1072(0)
        sendToLabelUpon(56, 1)
    sprite('null', 8)
    Unknown3026(-3639041)
    Unknown3025(-128, 8)
    sprite('null', 32767)
    Unknown23131()
    label(1)
    sprite('null', 3)
    Unknown4007(0)
    Unknown4010(0)
    Unknown3001(120)
    Unknown3004(-20)
    Unknown1099(20)

@State
def Install():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f77696e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1096(500)
        teleportRelativeX(-20000)
        Unknown3001(255)
        sendToLabelUpon(56, 1)
    sprite('null', 10)
    Unknown3026(-3639041)
    Unknown3025(-128, 8)
    sprite('null', 32767)
    Unknown23131()
    label(1)
    sprite('null', 5)
    Unknown4007(0)
    Unknown4010(0)
    Unknown3001(200)
    Unknown3004(-50)

@State
def InstallDD():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f77696e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1096(500)
        teleportRelativeX(-20000)
        Unknown3001(255)
        sendToLabelUpon(56, 1)
    sprite('null', 10)
    Unknown3026(-3639041)
    Unknown3025(-128, 8)
    sprite('null', 32767)
    Unknown23131()
    label(1)
    sprite('null', 5)
    Unknown4007(0)
    Unknown4010(0)
    Unknown3001(200)
    Unknown3004(-50)

@State
def __5DLightsaber_on():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrizef204_00', 6)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef204_00', 6)
    Unknown3004(0)
    sprite('vrizef204_00', 6)
    Unknown3004(-50)

@State
def __5DLightsaber_onDD():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown2054(1)
    sprite('vrizef204_00', 6)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef204_00', 6)
    Unknown3004(0)
    sprite('vrizef204_00', 6)
    Unknown3004(-50)

@State
def __5DLightsaber_off():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrizef204_00', 4)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef204_00', 4)
    Unknown3004(-50)

@State
def KakuseiAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(300)
        Unknown1056(300)
        Unknown1072(-48000)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-40)
    Unknown3004(-30)

@State
def KakuseiAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(280)
        Unknown1056(250)
        Unknown1072(-70000)
        Unknown23015(5)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def KakuseiAuraDD():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1064(300)
        Unknown1056(300)
        Unknown1072(-48000)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-40)
    Unknown3004(-30)

@State
def KakuseiAuraDD_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown2054(1)
        Unknown3033()
        Unknown1064(280)
        Unknown1056(250)
        Unknown1072(-70000)
        Unknown23015(5)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def __2DLightsaber_on():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrizef234_00', 6)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef234_00', 6)
    Unknown3004(0)
    sprite('vrizef234_00', 6)
    Unknown3004(-50)

@State
def __2DLightsaber_off():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrizef234_00', 4)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef234_00', 4)
    Unknown3004(-50)

@State
def __2DKakuseiAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(350)
        Unknown1056(300)
        Unknown1072(18000)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def __2DKakuseiAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(300)
        Unknown1056(250)
        Unknown1072(28000)
        Unknown23015(5)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def AirLightsaber_on():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrizef254_00', 6)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef254_00', 6)
    Unknown3004(0)
    sprite('vrizef254_00', 6)
    Unknown3004(-50)

@State
def AirLightsaber_off():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('vrizef254_00', 4)
    Unknown3001(0)
    Unknown3004(50)
    sprite('vrizef254_00', 4)
    Unknown3004(-50)

@State
def AirKakuseiAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1096(350)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def AirKakuseiAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1096(300)
        Unknown23015(5)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def OverDriveAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(350)
        Unknown1056(300)
        Unknown1072(-20000)
    sprite('null', 32767)

@State
def OverDriveAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(300)
        Unknown1056(250)
        Unknown1072(-40000)
        Unknown23015(5)
    sprite('null', 32767)

@State
def __5CKakuseiAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1064(400)
        Unknown1056(300)
        Unknown1072(-30000)
    sprite('null', 6)
    sprite('null', 2)
    Unknown1072(-80000)
    Unknown3004(-30)
    Unknown1064(100)
    Unknown1056(200)
    teleportRelativeX(130000)

@State
def __5CKakuseiAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1064(300)
        Unknown1056(250)
        Unknown1072(-20000)
        Unknown23015(5)
    sprite('null', 6)
    sprite('null', 2)
    Unknown1072(-80000)
    Unknown3004(-30)
    Unknown1064(100)
    Unknown1056(200)
    teleportRelativeX(130000)

@State
def __2CKakuseiAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1096(300)
    sprite('null', 5)
    Unknown1072(-15000)
    sprite('null', 5)
    teleportRelativeX(15000)
    Unknown1007(10000)
    Unknown1072(-10000)
    Unknown1064(350)
    sprite('null', 4)
    teleportRelativeX(20000)
    Unknown1007(10000)
    sprite('null', 3)
    Unknown1072(-20000)
    Unknown3004(-30)

@State
def Kakusei3CAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(350)
        Unknown1056(400)
        Unknown3001(200)

        def upon_43():
            if (SLOT_48 == 101):
                sendToLabel(1)
    sprite('null', 3)
    Unknown1072(15000)
    sprite('null', 40)
    Unknown1096(400)
    Unknown1072(0)
    teleportRelativeX(45000)
    Unknown1007(-25000)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def Kakusei3CAuraFire():

    def upon_IMMEDIATE():
        Unknown23067('izef_hoverdashaura')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1072(180000)

        def upon_43():
            if (SLOT_48 == 102):
                sendToLabel(1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def AirThrowAura1():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(350)
        Unknown1056(400)
        Unknown3001(200)
        Unknown1072(30000)
    sprite('null', 40)

@State
def AirThrowAura2():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(350)
        Unknown1056(400)
        Unknown3001(200)
        Unknown1072(30000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    teleportRelativeX(-20000)
    Unknown1007(-30000)
    Unknown1072(20000)

@State
def AirThrowAuraFire():

    def upon_IMMEDIATE():
        Unknown23067('izef_hoverdashaura')
        Unknown4010(3)
        Unknown4007(3)
        Unknown2005()
        Unknown1072(-30000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def HoverDashAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(350)
        Unknown1056(400)
        Unknown3001(255)
        Unknown1072(-20000)

        def upon_43():
            if (SLOT_48 == 401):
                sendToLabel(1)
    sprite('null', 32767)
    GFX_0('HoverDashFire', -1)
    label(1)
    sprite('null', 3)
    Unknown21012('486f76657244617368466972650000000000000000000000000000000000000020000000')
    Unknown1007(5000)
    Unknown1072(-15000)
    Unknown1067(-70)
    Unknown3004(-20)

@State
def HoverDashFire():

    def upon_IMMEDIATE():
        Unknown23067('izef_hoverdashaura')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1072(170000)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def HoverDashAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(300)
        Unknown1056(350)
        Unknown3001(200)
        Unknown1072(-25000)
        Unknown23015(5)
        sendToLabelUpon(32, 1)
    sprite('null', 40)
    label(1)
    sprite('null', 3)
    Unknown1067(-70)
    Unknown3004(-20)

@State
def BackHoverDashAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1096(350)
        Unknown3001(200)
        Unknown1072(-25000)
        Unknown2005()

        def upon_43():
            if (SLOT_48 == 402):
                sendToLabel(1)
    sprite('null', 40)
    GFX_0('BackHoverDashFire', -1)
    label(1)
    sprite('null', 3)
    Unknown3001(0)

@State
def BackHoverDashFire():

    def upon_IMMEDIATE():
        Unknown23067('izef_hoverdashaura')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1072(160000)

        def upon_43():
            if (SLOT_48 == 403):
                sendToLabel(1)
    sprite('null', 40)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def BackHoverDashAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1096(300)
        Unknown3001(200)
        Unknown1072(-20000)
        Unknown23015(5)
        Unknown2005()

        def upon_43():
            if (SLOT_48 == 404):
                sendToLabel(1)
    sprite('null', 40)
    label(1)
    sprite('null', 3)
    Unknown3001(0)

@State
def ShotD_Aura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(150)
        Unknown1056(250)
        Unknown1072(-60000)
    sprite('null', 3)
    sprite('null', 3)
    Unknown1072(-65000)
    teleportRelativeX(40000)
    Unknown1096(300)
    sprite('null', 10)
    Unknown1072(-70000)
    teleportRelativeX(30000)
    sprite('null', 2)
    teleportRelativeX(-10000)
    Unknown1064(150)
    Unknown1056(250)

@State
def ShotD_Aura_back():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1072(-55000)
        Unknown1096(250)
        Unknown23015(5)
    sprite('null', 3)
    sprite('null', 12)
    Unknown1072(-45000)
    Unknown1096(300)
    sprite('null', 2)
    Unknown1072(-45000)
    Unknown1064(150)
    Unknown1056(250)

@State
def AirShotAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown2005()
        Unknown1064(290)
        Unknown1056(250)
        Unknown1072(18000)
    sprite('null', 12)
    sprite('null', 2)
    Unknown1072(-2500)
    teleportRelativeX(-14000)
    Unknown1007(-20000)
    Unknown1064(110)
    Unknown3004(-30)

@State
def AirShotAura_oku():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown1064(280)
        Unknown1056(250)
        Unknown1072(-70000)
        Unknown23015(5)
    sprite('null', 17)
    sprite('null', 4)
    Unknown1067(-60)
    Unknown3004(-30)

@State
def ShieildBit():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown23027()
        Unknown2037(0)
        Unknown9016(1)
        Hitstop(5)
        Unknown23013(1)
        Unknown3032()

        def upon_33():
            clearUponHandler(33)
            clearUponHandler(34)
            SLOT_56 = 1
            Unknown2019(-500)
            Unknown2037(1)

        def upon_34():
            clearUponHandler(33)
            clearUponHandler(34)
            SLOT_56 = 0
            Unknown2019(500)
            Unknown1096(900)
            Unknown2037(1)

        def upon_38():
            sendToLabel(200)

        def upon_35():
            Unknown21012('4269745f77696e6730300000000000000000000000000000000000000000000021000000')
            Unknown21012('4269745f77696e6730310000000000000000000000000000000000000000000021000000')
            sendToLabel(100)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(300)
        if (not SLOT_21):
            SLOT_32 = 0
            if SLOT_2:
                sendToLabel(300)

        def upon_53():
            SLOT_32 = 0

        def upon_44():
            Unknown23027()

        def upon_3():
            if SLOT_2:
                Unknown23023()
                if SLOT_56:
                    Unknown2071('03000000b817fefff04902000f00000001000000')
                else:
                    Unknown2071('030000003850ffff20bf02000f00000001000000')
            if (SLOT_32 <= 0):
                if SLOT_2:
                    sendToLabel(300)
    sprite('vrizef431_00', 10)
    Unknown1072(30000)
    GFX_0('Bit_particle', 100)
    GFX_1('izef_bit_lost', 100)
    GFX_0('Bit_wing00', 0)
    GFX_0('Bit_wing01', 1)
    Unknown2037(1)
    sprite('keep', 1)
    Unknown21012('4269745f77696e6730300000000000000000000000000000000000000000000020000000')
    Unknown21012('4269745f77696e6730310000000000000000000000000000000000000000000020000000')
    label(0)
    sprite('vrizef431_00', 32767)
    label(100)
    sprite('vrizef431_01', 10)
    Unknown2037(0)
    physicsXImpulse(-3000)
    physicsYImpulse(-8000)
    GFX_1('izef_bit_ready', 100)
    GFX_0('Bit_Particle_Attack', 100)
    GFX_0('Bit_particle_add', 103)
    sprite('vrizef431_01', 8)
    RefreshMultihit()
    AttackLevel_(2)
    Damage(200)
    Unknown9154(17)
    AirUntechableTime(17)
    AttackP2(100)
    physicsXImpulse(60000)
    physicsYImpulse(-30000)
    Unknown3069(2)
    Unknown3029(1)
    sprite('vrizef431_01', 4)
    Unknown23027()
    physicsXImpulse(6250)
    physicsYImpulse(-1250)
    Unknown3029(0)
    Unknown26('Bit_particle_add')
    sprite('vrizef431_01', 10)
    physicsXImpulse(2500)
    physicsYImpulse(5000)
    label(200)
    sprite('vrizef431_00', 20)
    Unknown2037(1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('vrizef431_00', 1)
    gotoLabel(0)
    label(300)
    sprite('vrizef431_00', 2)
    GFX_1('izef_bit_lost', 100)
    Unknown13(25)

@State
def Bit_wing00():

    def upon_IMMEDIATE():
        Unknown4019(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1072(30000)

        def upon_32():
            Unknown4007(0)
            sendToLabel(0)
        sendToLabelUpon(33, 100)
        Unknown2037(1)

        def upon_48():
            if SLOT_2:
                Unknown23151(2, 0)
    sprite('vrizef431_w00', 32767)
    label(0)
    sprite('vrizef431_w00', 20)
    Unknown1074(-500)
    sprite('vrizef431_w00', 20)
    Unknown1074(500)
    gotoLabel(0)
    label(100)
    sprite('vrizef431_w00', 10)
    Unknown4007(2)
    Unknown2037(0)
    Unknown1072(30000)
    Unknown1074(3000)
    sprite('vrizef431_w00', 12)
    Unknown1072(15000)
    Unknown1074(0)
    sprite('vrizef431_w00', 10)
    Unknown4007(0)
    Unknown2037(1)
    sprite('vrizef431_w00', 4)
    Unknown1074(1500)
    sprite('vrizef431_w00', 1)
    Unknown1072(30000)
    Unknown1074(0)
    gotoLabel(0)

@State
def Bit_wing01():

    def upon_IMMEDIATE():
        Unknown4019(2)
        Unknown4009(2)
        Unknown4013(2)
        Unknown4008(2)
        Unknown4010(2)
        Unknown3032()
        Unknown1072(30000)

        def upon_32():
            Unknown4007(0)
            sendToLabel(0)
        sendToLabelUpon(33, 100)
        Unknown2037(1)

        def upon_48():
            if SLOT_2:
                Unknown23151(2, 1)
    sprite('vrizef431_w01', 32767)
    label(0)
    sprite('vrizef431_w01', 20)
    Unknown1074(500)
    sprite('vrizef431_w01', 20)
    Unknown1074(-500)
    gotoLabel(0)
    label(100)
    sprite('vrizef431_w01', 10)
    Unknown4007(2)
    Unknown2037(0)
    Unknown1072(30000)
    Unknown1074(-3000)
    sprite('vrizef431_w01', 12)
    Unknown1072(45000)
    Unknown1074(0)
    sprite('vrizef431_w01', 10)
    Unknown4007(0)
    Unknown2037(1)
    sprite('vrizef431_w01', 4)
    Unknown1074(-1500)
    sprite('vrizef431_w01', 1)
    Unknown1072(30000)
    Unknown1074(0)
    gotoLabel(0)

@State
def Bit_particle():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 4)
    GFX_1('izef_bit_dust', 103)
    gotoLabel(0)

@State
def Bit_Particle_Attack():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(2)
        GFX_2('izef_bit_attack')
    sprite('null', 35)

@State
def Bit_particle_add():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 2)
    GFX_1('izef_bit_dust', 103)
    gotoLabel(0)

@State
def EffLightSaber():

    def upon_IMMEDIATE():
        Unknown3038(1)
        Unknown32('497a4566664c69676874536162657200')
    sprite('null', 32767)

@State
def __6AZanzo():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown23015(2)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(246)
        Unknown3041(247)
        Unknown3043(248)
        Unknown3044(0)
        Unknown3001(200)
    sprite('vrizef210_f04', 5)
    GFX_0('6Afanel', -1)
    sprite('null', 10)

@State
def __6Afanel():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
    sprite('iz210_f04', 3)
    Unknown3001(255)

@State
def __6BZanzo():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(246)
        Unknown3041(247)
        Unknown3043(248)
        Unknown3044(0)
        Unknown3001(200)
    sprite('vrizef211_f09', 3)

@State
def __6CZanzo():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(2)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(246)
        Unknown3041(247)
        Unknown3043(248)
        Unknown3044(0)
        Unknown3001(200)
    sprite('vrizef212_f06', 2)
    sprite('vrizef212_f07', 3)

@State
def __5CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
        Unknown23015(3)
    sprite('vrizef202_00', 2)
    sprite('vrizef202_01', 3)
    sprite('vrizef202_01', 7)
    Unknown3004(-20)

@State
def Kaku5CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
        Unknown23015(3)
    sprite('vrizef203_00', 3)
    sprite('vrizef203_00', 4)
    Unknown3004(-20)

@State
def __2CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
        Unknown23015(3)
    sprite('vrizef232_00', 3)
    sprite('vrizef232_01', 3)
    teleportRelativeX(-10000)
    Unknown1007(7000)
    sprite('vrizef232_02', 6)
    Unknown3001(100)

@State
def ParAtk2C():

    def upon_IMMEDIATE():
        GFX_2('izef_atk2c')
        Unknown4010(3)
        Unknown23015(1)
        Unknown2054(1)
        Unknown3033()
        Unknown1064(600)
    sprite('null', 10)
    sprite('null', 6)
    Unknown3004(-40)

@State
def Kaku2CZanzo00():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
        Unknown23015(3)
    sprite('vrizef233_00', 2)
    sprite('vrizef233_01', 10)
    GFX_0('ParAtk2C', 0)

@State
def Kaku2CZanzo01():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
        Unknown23015(3)
    sprite('vrizef233_02', 10)
    sprite('vrizef233_02', 10)
    Unknown3004(-10)

@State
def __3CZanzo00():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
        Unknown23015(3)
    sprite('vrizef235_00', 2)
    sprite('vrizef235_01', 10)

@State
def AIR5CZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        callSubroutine('LightSaverSwitch')
        Unknown3044(0)
    sprite('vrizef252_00', 3)
    sprite('vrizef252_01', 3)
    sprite('vrizef252_01', 7)
    Unknown4007(0)

@State
def ParSpDash_6():

    def upon_IMMEDIATE():
        GFX_2('copy00 izef__drivelight00')
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', 24)
    Unknown3001(255)
    sprite('null', 6)

@State
def GuardCrushZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        callSubroutine('LightSaverSwitch')
        Unknown23015(3)
    sprite('vrizef412_00', 10)

@State
def ThrowLock_MagicCircle():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown4003('697a65665f6c6f636b6d616769632e4449470000000000000000000000000000697a65665f6c6f636b6d616769635f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(2)
        Unknown4015()
        Unknown3033()
        Unknown1096(800)
        Unknown1007(220000)
        Unknown3026(-76)

        def upon_43():
            if (SLOT_48 == 302):
                sendToLabel(99)
    sprite('null', 32767)
    Unknown3004(-2)
    loopRest()
    label(99)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3004(-30)
    Unknown1059(200)
    Unknown1067(100)

@State
def ThrowFunnel():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 301):
                sendToLabel(99)
    sprite('iz311_f02', 32767)
    label(99)
    sprite('null', 1)

@State
def AirThrowLock_MagicCircle():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown4003('697a65665f6c6f636b6d616769632e4449470000000000000000000000000000697a65665f6c6f636b6d616769635f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(2)
        Unknown4015()
        Unknown3033()
        Unknown1096(800)
        Unknown1007(220000)
        Unknown3026(-76)

        def upon_32():
            sendToLabel(98)
    sprite('null', 32767)
    Unknown3004(-2)
    loopRest()
    label(98)
    sprite('null', 5)
    Unknown4007(0)
    sprite('null', 10)
    Unknown3004(-30)
    Unknown1059(200)
    Unknown1067(100)

@State
def Iaimcircle():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(2)
        Unknown4047(48, 48, 48)
        Unknown23067('izef_iaimcircle')

        def upon_43():
            if (SLOT_48 == 1001):
                sendToLabel(99)
    sprite('null', 6)
    Unknown3001(0)
    Unknown3004(30)
    Unknown1096(1600)
    Unknown1099(-100)
    sprite('null', 32767)
    Unknown3001(255)
    Unknown1096(1000)
    Unknown1099(0)
    label(99)
    sprite('null', 4)
    sprite('null', 8)
    Unknown1099(200)
    Unknown3004(-30)

@State
def Iaimcircle_EntryVsMu():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(2)
        Unknown4010(3)
        Unknown4047(48, 48, 48)
        Unknown23067('izef_iaimcircle')
        sendToLabelUpon(33, 99)
    sprite('null', 6)
    Unknown3001(0)
    Unknown3004(30)
    Unknown1096(1500)
    sprite('null', 32767)
    Unknown3001(255)
    Unknown1096(1500)
    Unknown1058(120)
    Unknown1066(120)
    Unknown1099(0)
    label(99)
    sprite('null', 4)
    sprite('null', 8)
    Unknown1099(200)
    Unknown3004(-15)

@State
def izef_413_a():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4061(4)
        Unknown3033()
        callSubroutine('ShotColorSwitch')
        teleportRelativeX(110000)
        Unknown1007(410000)
    sprite('vrizef_413_00', 2)
    sprite('vrizef_413_01', 3)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    sprite('vrizef_413_02', 3)
    sprite('vrizef_413_03', 3)
    sprite('vrizef_413_04', 8)
    Unknown3004(-32)

@State
def izef_413_b():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4061(4)
        Unknown3033()
        callSubroutine('ShotColorSwitch')
        teleportRelativeX(120000)
        Unknown1007(270000)
    sprite('vrizef_413_11', 3)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    sprite('vrizef_413_12', 3)
    sprite('vrizef_413_13', 3)
    sprite('vrizef_413_14', 3)
    sprite('vrizef_413_15', 8)
    Unknown3004(-32)

@State
def izef_413_c():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4061(4)
        Unknown3033()
        callSubroutine('ShotColorSwitch')
        teleportRelativeX(116000)
        Unknown1007(132000)
    sprite('vrizef_413_21', 3)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    sprite('vrizef_413_22', 3)
    sprite('vrizef_413_23', 3)
    sprite('vrizef_413_24', 3)
    Unknown3004(-32)

@State
def Iai_SlashZanzo00():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(128000)
        Unknown1007(192000)
        Unknown23015(3)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef_402_00', 2)
    sprite('vrizef_402_01', 2)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    GFX_1('izef_Iai_feather', 7)
    GFX_1('izef_Iai_feather', 8)
    sprite('vrizef_402_02', 2)
    sprite('vrizef_402_03', 2)
    sprite('vrizef_402_04', 2)
    sprite('vrizef_402_05', 8)
    Unknown3004(-32)

@State
def Iai_SlashZanzo_Gedan():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(160000)
        Unknown1007(160000)
        Unknown23015(3)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef_402_10', 3)
    sprite('vrizef_402_11', 2)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    GFX_1('izef_Iai_feather', 7)
    GFX_1('izef_Iai_feather', 8)
    sprite('vrizef_402_12', 2)
    sprite('vrizef_402_13', 2)
    sprite('vrizef_402_14', 2)
    sprite('vrizef_402_15', 8)
    Unknown3004(-32)

@State
def Iai_SlashZanzo_AntiAirA():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(256000)
        Unknown1007(380000)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef_404_00', 2)
    sprite('vrizef_404_01', 2)
    Unknown2019(100)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    GFX_1('izef_Iai_feather', 7)
    GFX_1('izef_Iai_feather', 8)
    GFX_1('izef_Iai_feather', 9)
    sprite('vrizef_404_02', 2)
    sprite('vrizef_404_03', 2)
    sprite('vrizef_404_04', 2)
    sprite('vrizef_404_05', 8)
    Unknown3004(-32)

@State
def Iai_SlashZanzo_AntiAirB():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown1007(384000)
        Unknown23015(3)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef_405_01', 2)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    GFX_1('izef_Iai_feather', 7)
    GFX_1('izef_Iai_feather', 8)
    GFX_1('izef_Iai_feather', 9)
    sprite('vrizef_405_02', 2)
    sprite('vrizef_405_03', 2)
    sprite('vrizef_405_04', 2)
    sprite('vrizef_405_05', 8)
    Unknown3004(-32)

@State
def Iai_AntiAirNext_Zanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(3)
        callSubroutine('ShotColorSwitch')
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 1002):
                sendToLabel(1)
    label(0)
    sprite('vrizef_406_00', 3)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    sprite('vrizef_406_00', 2)
    gotoLabel(0)
    label(1)
    sprite('vrizef_406_01', 3)
    Unknown1007(-5000)
    sprite('vrizef_406_01', 5)
    Unknown3004(-20)

@State
def IaiAntiAirNextAuraL():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown2005()
        Unknown1056(600)
        Unknown1064(450)
        Unknown3001(255)
        Unknown1072(110000)

        def upon_43():
            if (SLOT_48 == 1003):
                sendToLabel(1)
    label(0)
    sprite('null', 2)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    teleportRelativeX(-5000)
    Unknown1007(-130000)
    Unknown1096(350)
    Unknown1073(20000)
    sprite('null', 5)
    teleportRelativeX(5000)
    Unknown1007(-20000)
    Unknown1096(300)
    Unknown1073(5000)

@State
def IaiAntiAirNextAuraR():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(600)
        Unknown1064(450)
        Unknown3001(255)
        Unknown1072(110000)

        def upon_43():
            if (SLOT_48 == 1004):
                sendToLabel(1)
    label(0)
    sprite('null', 2)
    sprite('null', 2)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    teleportRelativeX(30000)
    Unknown1007(-150000)
    Unknown1096(250)
    Unknown1073(30000)
    sprite('null', 5)
    teleportRelativeX(5000)
    Unknown1007(-10000)
    Unknown1073(5000)

@State
def Iai_AntiAir_Next_404F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz404_03', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(6000)
    Unknown1028(2000)
    Unknown3004(-20)
    sprite('iz404_04', 2)
    sprite('iz404_05', 6)

@State
def Iai_AntiAir_Next_404B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz404_03', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(-6000)
    Unknown1028(-2000)
    Unknown3004(-20)
    sprite('iz404_04', 2)
    sprite('iz404_05', 6)

@State
def Iai_AntiAir_Next_405F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz405_07', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(6000)
    Unknown1028(2000)
    Unknown3004(-20)
    sprite('iz405_08', 2)
    sprite('iz405_09', 6)

@State
def Iai_AntiAir_Next_405B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz405_07', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(-6000)
    Unknown1028(-2000)
    Unknown3004(-20)
    sprite('iz405_08', 2)
    sprite('iz405_09', 6)

@State
def EX_Iai_AntiAir_Next_405F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz403_02', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(6000)
    Unknown1028(2000)
    Unknown3004(-20)
    sprite('iz403_03', 2)
    sprite('iz403_04', 6)

@State
def EX_Iai_AntiAir_Next_405B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz403_02', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(-6000)
    Unknown1028(-2000)
    Unknown3004(-20)
    sprite('iz403_03', 2)
    sprite('iz403_04', 6)

@State
def Iai_AntiAir_Next_408F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz408_07', 3)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(6000)
    Unknown1028(2000)
    Unknown3004(-20)
    sprite('iz408_08', 7)

@State
def Iai_AntiAir_Next_408B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz408_07', 3)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(-6000)
    Unknown1028(-2000)
    Unknown3004(-20)
    sprite('iz408_08', 7)

@State
def Iai_AntiAir_Next_403F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1086(3)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz403_00', 5)
    Unknown23119(51200, 6, 2)
    teleportRelativeX(400000)
    physicsXImpulse(-80000)
    Unknown3001(128)

@State
def Iai_AntiAir_Next_403B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1086(3)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz403_00', 5)
    Unknown23119(51200, 6, 2)
    teleportRelativeX(-400000)
    physicsXImpulse(80000)
    Unknown3001(128)

@State
def Iai_AntiAir_Next_406F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1086(3)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz406_00', 3)
    Unknown23119(51200, 6, 2)
    teleportRelativeX(240000)
    physicsXImpulse(-20000)
    Unknown3001(128)
    sprite('iz406_01', 4)
    sprite('iz406_02', 3)

@State
def Iai_AntiAir_Next_406B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1086(3)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz406_00', 3)
    Unknown23119(51200, 6, 2)
    teleportRelativeX(-240000)
    physicsXImpulse(20000)
    Unknown3001(128)
    sprite('iz406_01', 4)
    sprite('iz406_02', 3)

@State
def Iai_AntiAir_Next_413F():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz413_15', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(6000)
    Unknown1028(2000)
    Unknown3004(-20)
    sprite('iz413_16', 2)
    sprite('iz413_17', 6)

@State
def Iai_AntiAir_Next_413B():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz413_15', 2)
    Unknown23119(51200, 6, 2)
    physicsXImpulse(-6000)
    Unknown1028(-2000)
    Unknown3004(-20)
    sprite('iz413_16', 2)
    sprite('iz413_17', 6)

@State
def Iai_hold():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        callSubroutine('ShotColorSwitch')
    label(0)
    sprite('null', 2)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f4961695f686f6c640000000000000000000000000000000000000000000000')
    gotoLabel(0)

@State
def Iai_hold_add():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
    label(0)
    sprite('null', 1)
    GFX_1('izef_Iai_hold_add', 0)
    gotoLabel(0)

@State
def AirAssaultZanzo():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4007(3)
        Unknown4010(3)
        Unknown3033()
        Unknown4061(2)
        Unknown3001(200)
        Unknown23015(3)
    sprite('vrizef_408_00', 2)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    sprite('vrizef_408_01', 3)
    Unknown3004(-30)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    sprite('vrizef_408_02', 2)
    sprite('null', 5)

@State
def Ia_SlashNextZanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(50000)
        Unknown1007(160000)
        Unknown23015(3)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef_402_11', 2)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    GFX_1('izef_Iai_feather', 7)
    GFX_1('izef_Iai_feather', 8)
    sprite('vrizef_402_12', 2)
    sprite('vrizef_402_13', 2)
    sprite('vrizef_402_14', 2)
    sprite('vrizef_402_15', 8)
    Unknown3004(-32)

@State
def Ia_SlashNextZanzo_EntryVsMu():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeX(50000)
        Unknown1007(160000)
        Unknown23015(3)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef_402_11', 16)
    GFX_1('izef_Iai_feather', 0)
    GFX_1('izef_Iai_feather', 1)
    GFX_1('izef_Iai_feather', 2)
    GFX_1('izef_Iai_feather', 3)
    GFX_1('izef_Iai_feather', 4)
    GFX_1('izef_Iai_feather', 5)
    GFX_1('izef_Iai_feather', 6)
    GFX_1('izef_Iai_feather', 7)
    GFX_1('izef_Iai_feather', 8)
    sprite('vrizef_402_12', 4)
    sprite('vrizef_402_13', 4)
    sprite('vrizef_402_14', 4)
    sprite('vrizef_402_15', 8)
    Unknown3004(-32)

@State
def IaiSlashNextAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(600)
        Unknown1064(450)
        Unknown3001(255)
    sprite('null', 6)
    sprite('null', 3)
    Unknown1064(300)
    Unknown1056(400)
    teleportRelativeX(40000)
    Unknown1072(-25000)

@State
def DIST_IZShot():

    def upon_3():
        Unknown3057(1)
        Unknown3058(20000)
        Unknown3059(-1000)
        Unknown4006(2)
        Unknown4007(2)
    sprite('vrdist_iz00', 6)
    Unknown3001(200)
    Unknown1056(750)
    Unknown1064(500)
    Unknown1059(150)
    Unknown1067(100)
    sprite('vrdist_iz00', 10)
    Unknown1067(-100)
    Unknown1067(-100)

@State
def DIST_IZSpecial_Shot():

    def upon_3():
        Unknown3057(1)
        Unknown3058(20000)
        Unknown3059(-1000)
        Unknown4006(2)
        Unknown4007(2)
    sprite('vrdist_iz00', 6)
    Unknown3001(200)
    Unknown1056(1000)
    Unknown1064(600)
    Unknown1059(150)
    Unknown1067(100)
    sprite('vrdist_iz00', 10)
    Unknown1067(-100)
    Unknown1067(-100)

@State
def Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown2055(120)
        AttackLevel_(3)
        Damage(1500)
        Unknown9016(1)
        Hitstop(7)
        Unknown11001(0, 3, 4)
        Unknown11057(600)
        Unknown9154(19)
        AirUntechableTime(19)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        Unknown4047(240, 241, 241)
        Unknown4045('697a65665f73686f745f636972636c650000000000000000000000000000000064000000')
    sprite('vrizef_shot00', 16)
    physicsXImpulse(1000)
    Unknown3001(0)
    Unknown3004(12)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 100)
    Unknown23118(-1)
    Unknown23119(0, 20, 1)
    sprite('vrizef_shot00', 6)
    RefreshMultihit()
    physicsXImpulse(25000)
    physicsYImpulse(0)
    Unknown1108(0)
    sprite('vrizef_shot00', 32)
    Unknown1019(160)
    sprite('vrizef_shot00', 12)
    Unknown23027()
    physicsXImpulse(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Air_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown2055(120)
        AttackLevel_(3)
        Damage(1500)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(10)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        Unknown4048(45000)
        Unknown4047(240, 241, 241)
        Unknown4045('697a65665f73686f745f636972636c650000000000000000000000000000000064000000')
    sprite('vrizef_shot00', 11)
    Unknown1072(45000)
    physicsXImpulse(1000)
    physicsYImpulse(-1000)
    Unknown3001(0)
    Unknown3004(12)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 100)
    Unknown23118(-1)
    Unknown23119(0, 20, 1)
    sprite('vrizef_shot00', 2)
    RefreshMultihit()
    physicsXImpulse(5000)
    physicsYImpulse(-5000)
    Unknown1028(900)
    setGravity(900)
    Unknown2055(240)
    sprite('vrizef_shot00', 4)
    sprite('vrizef_shot00', 4)
    YAccel(140)
    sprite('vrizef_shot00', 40)
    label(1)
    sprite('vrizef_shot00', 6)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def shotD_Matome():
    sprite('iz400_expoint', 90)
    GFX_0('Shot_D', 0)
    GFX_0('Shot_D', 1)
    Unknown21007(1, 32)
    GFX_0('Shot_D', 2)
    Unknown21007(1, 33)
    GFX_0('Shot_D_circle', 1)

@State
def shotD_MatomeOD():
    sprite('iz400_expointOD', 90)
    GFX_0('Shot_D_OD', 0)
    Unknown21007(1, 32)
    GFX_0('Shot_D_OD', 1)
    GFX_0('Shot_D_OD', 2)
    Unknown21007(1, 33)
    GFX_0('Shot_D_OD', 3)
    Unknown21007(1, 34)
    GFX_0('Shot_D_OD', 4)
    Unknown21007(1, 35)
    GFX_0('Shot_D_OD_circle', 1)

@State
def AirshotD_Matome():
    sprite('iz401_expoint', 90)
    GFX_0('Air_Shot_D', 0)
    GFX_0('Air_Shot_D', 1)
    Unknown21007(1, 32)
    GFX_0('Air_Shot_D', 2)
    Unknown21007(1, 33)
    GFX_0('Air_Shot_D_circle', 0)

@State
def AirshotD_MatomeOD():
    sprite('iz401_expointOD', 90)
    GFX_0('Air_Shot_D_OD', 0)
    GFX_0('Air_Shot_D_OD', 1)
    Unknown21007(1, 32)
    GFX_0('Air_Shot_D_OD', 2)
    Unknown21007(1, 33)
    GFX_0('Air_Shot_D_OD', 3)
    Unknown21007(1, 34)
    GFX_0('Air_Shot_D_OD', 4)
    Unknown21007(1, 35)
    GFX_0('Air_Shot_D_OD_circle', 0)

@State
def Shot_D():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown1096(835)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown2055(120)
        AttackLevel_(3)
        Damage(1500)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(10)
        Unknown11057(600)
        Unknown9154(19)
        AirUntechableTime(19)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        Unknown23182(2)
        Unknown11091(10)
        Unknown30065(0)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')

        def upon_32():
            Unknown1072(-10000)

        def upon_33():
            Unknown1072(-20000)

        def upon_34():
            Unknown1072(20000)

        def upon_35():
            Unknown1072(-20000)
    sprite('vrizef_shot00', 1)
    Unknown3001(0)
    Unknown3004(12)
    Unknown23118(-1)
    Unknown23119(0, 20, 1)
    sprite('vrizef_shot00', 15)
    Unknown1110(500, 0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 100)
    sprite('vrizef_shot00', 15)
    RefreshMultihit()
    Unknown1019(600)
    YAccel(600)
    sprite('vrizef_shot00', 20)
    Unknown1019(150)
    YAccel(150)
    Unknown1108(0)
    sprite('vrizef_shot00', 30)
    Unknown1019(1000)
    YAccel(1000)
    sprite('vrizef_shot00', 6)
    Unknown23027()
    Unknown1019(0)
    YAccel(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Air_Shot_D():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown1096(835)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown2055(120)
        AttackLevel_(3)
        Damage(1500)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(10)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        Unknown11091(10)
        Unknown30065(0)
        Unknown23182(2)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        Unknown1072(40000)

        def upon_32():
            Unknown1072(10000)

        def upon_33():
            Unknown1072(70000)

        def upon_34():
            Unknown1072(25000)

        def upon_35():
            Unknown1072(65000)
    sprite('vrizef_shot00', 1)
    Unknown3001(0)
    Unknown3004(12)
    Unknown23118(-1)
    Unknown23119(0, 20, 1)
    sprite('vrizef_shot00', 10)
    Unknown1110(1000, 0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 100)
    sprite('vrizef_shot00', 5)
    RefreshMultihit()
    Unknown1019(500)
    YAccel(500)
    Unknown2055(240)
    sprite('vrizef_shot00', 5)
    Unknown1019(200)
    YAccel(200)
    sprite('vrizef_shot00', 5)
    Unknown1019(200)
    YAccel(200)
    sprite('vrizef_shot00', 20)
    Unknown1019(200)
    YAccel(200)
    sprite('vrizef_shot00', 4)
    sprite('vrizef_shot00', 60)
    label(1)
    sprite('vrizef_shot00', 6)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Shot_D_OD():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown1096(760)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown2055(120)
        AttackLevel_(2)
        Damage(600)
        if SLOT_136:
            Unknown10000(80)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(10)
        Unknown11057(600)
        Unknown9154(19)
        AirUntechableTime(19)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        Unknown12051(2)
        Unknown12052(1)
        Unknown23182(2)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')

        def upon_32():
            Unknown1072(10000)

        def upon_33():
            Unknown1072(-10000)

        def upon_34():
            Unknown1072(20000)

        def upon_35():
            Unknown1072(-20000)
    sprite('vrizef_shot00', 1)
    Unknown3001(0)
    Unknown3004(12)
    Unknown23118(-1)
    Unknown23119(0, 20, 1)
    sprite('vrizef_shot00', 15)
    Unknown1110(500, 0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 100)
    sprite('vrizef_shot00', 15)
    RefreshMultihit()
    Unknown1019(600)
    YAccel(600)
    sprite('vrizef_shot00', 20)
    Unknown1019(150)
    YAccel(150)
    Unknown1108(0)
    sprite('vrizef_shot00', 30)
    Unknown1019(1000)
    YAccel(1000)
    sprite('vrizef_shot00', 6)
    Unknown23027()
    Unknown1019(0)
    YAccel(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Air_Shot_D_OD():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown1096(760)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown2055(120)
        AttackLevel_(2)
        Damage(600)
        if SLOT_136:
            Unknown10000(80)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(10)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        AttackP1(80)
        Unknown12051(2)
        Unknown12052(1)
        Unknown23182(2)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('AdditionalExGage')
        callSubroutine('ShotColorSwitch')
        Unknown1072(45000)

        def upon_32():
            Unknown1072(35000)

        def upon_33():
            Unknown1072(55000)

        def upon_34():
            Unknown1072(25000)

        def upon_35():
            Unknown1072(65000)
    sprite('vrizef_shot00', 1)
    Unknown3001(0)
    Unknown3004(12)
    Unknown23118(-1)
    Unknown23119(0, 20, 1)
    sprite('vrizef_shot00', 10)
    Unknown1110(1000, 0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 100)
    sprite('vrizef_shot00', 5)
    RefreshMultihit()
    Unknown1019(500)
    YAccel(500)
    Unknown2055(240)
    sprite('vrizef_shot00', 5)
    Unknown1019(200)
    YAccel(200)
    sprite('vrizef_shot00', 5)
    Unknown1019(200)
    YAccel(200)
    sprite('vrizef_shot00', 20)
    Unknown1019(200)
    YAccel(200)
    sprite('vrizef_shot00', 4)
    sprite('vrizef_shot00', 60)
    label(1)
    sprite('vrizef_shot00', 6)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Shot_D_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    Unknown4049(1250)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f636972636c650000000000000000000000000000000064000000')

@State
def Shot_D_OD_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    Unknown4049(1750)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f636972636c650000000000000000000000000000000064000000')

@State
def Air_Shot_D_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    Unknown4049(1250)
    Unknown4048(45000)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f636972636c650000000000000000000000000000000064000000')

@State
def Air_Shot_D_OD_circle():
    sprite('null', 1)
    callSubroutine('ShotColorSwitch')
    Unknown4049(1750)
    Unknown4048(45000)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f636972636c650000000000000000000000000000000064000000')

@State
def Special_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        AttackLevel_(3)
        Damage(1200)
        Unknown9016(1)
        PushbackX(20000)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(5000)
        Unknown11092(1)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        callSubroutine('ShotColorSwitch')
        Unknown4047(240, 241, 241)
        Unknown4045('697a65665f535073686f745f636972636c65000000000000000000000000000064000000')
        Unknown4047(241, 240, 240)
        Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

    def upon_78():
        Hitstop(34)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 32)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 33)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 34)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 35)
    sprite('vrizef_shot01aex', 5)
    Unknown3001(0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 1)
    sprite('vrizef_shot01aex', 5)
    Unknown3004(40)
    sprite('vrizef_shot01bex', 1)
    Unknown3001(255)
    sprite('vrizef_shot01cex', 1)
    sprite('vrizef_shot01dex', 1)
    sprite('vrizef_shot01eex', 1)
    sprite('vrizef_shot01fex', 1)
    sprite('vrizef_shot01gex', 1)
    sprite('vrizef_shot01hex', 1)
    RefreshMultihit()
    physicsXImpulse(28000)
    Unknown1028(800)
    physicsYImpulse(0)
    Unknown1108(0)
    sprite('vrizef_shot01iex', 1)
    sprite('vrizef_shot01ex', 10)
    sprite('vrizef_shot01ex', 8)
    sprite('vrizef_shot01ex', 60)
    Unknown1028(1600)
    sprite('vrizef_shot01ex', 12)
    Unknown23027()
    physicsXImpulse(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Special_Shot_PS():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        Unknown11042(1)
        AttackLevel_(3)
        Damage(1200)
        Unknown9016(1)
        PushbackX(20000)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(5000)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        callSubroutine('ShotColorSwitch')
        Unknown4047(240, 241, 241)
        Unknown4045('697a65665f535073686f745f636972636c65000000000000000000000000000064000000')
        Unknown4047(241, 240, 240)
        Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

    def upon_78():
        Hitstop(34)
        GFX_0('Special_Shot_Next_PS', -1)
        Unknown21007(1, 32)
        GFX_0('Special_Shot_Next_PS', -1)
        Unknown21007(1, 33)
        GFX_0('Special_Shot_Next_PS', -1)
        Unknown21007(1, 34)
        GFX_0('Special_Shot_Next_PS', -1)
        Unknown21007(1, 35)
    sprite('vrizef_shot01aex', 5)
    Unknown3001(0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 1)
    sprite('vrizef_shot01aex', 5)
    Unknown3004(40)
    sprite('vrizef_shot01bex', 1)
    Unknown3001(255)
    sprite('vrizef_shot01cex', 1)
    sprite('vrizef_shot01dex', 1)
    sprite('vrizef_shot01eex', 1)
    sprite('vrizef_shot01fex', 1)
    sprite('vrizef_shot01gex', 1)
    sprite('vrizef_shot01hex', 1)
    RefreshMultihit()
    physicsXImpulse(28000)
    Unknown1028(800)
    physicsYImpulse(0)
    Unknown1108(0)
    sprite('vrizef_shot01iex', 1)
    sprite('vrizef_shot01ex', 10)
    sprite('vrizef_shot01ex', 8)
    sprite('vrizef_shot01ex', 60)
    Unknown1028(1600)
    sprite('vrizef_shot01ex', 12)
    Unknown23027()
    physicsXImpulse(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def AirSpecial_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        AttackLevel_(3)
        Damage(1200)
        Unknown9016(1)
        PushbackX(20000)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(5000)
        Unknown11092(1)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        callSubroutine('ShotColorSwitch')
        Unknown4047(240, 241, 241)
        Unknown4048(45000)
        Unknown4045('697a65665f535073686f745f636972636c65000000000000000000000000000064000000')
        Unknown4047(241, 240, 240)
        Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
        Unknown1072(40000)

    def upon_78():
        Hitstop(34)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 32)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 33)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 34)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 35)
    sprite('vrizef_shot01a', 5)
    Unknown3001(0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 1)
    sprite('vrizef_shot01a', 5)
    Unknown3004(40)
    sprite('vrizef_shot01b', 1)
    Unknown3001(255)
    sprite('vrizef_shot01c', 1)
    sprite('vrizef_shot01d', 1)
    sprite('vrizef_shot01e', 1)
    sprite('vrizef_shot01f', 1)
    sprite('vrizef_shot01g', 1)
    sprite('vrizef_shot01h', 1)
    RefreshMultihit()
    physicsXImpulse(14000)
    Unknown1028(800)
    physicsYImpulse(-14000)
    setGravity(800)
    Unknown1108(0)
    sprite('vrizef_shot01i', 1)
    sprite('vrizef_shot01', 10)
    sprite('vrizef_shot01', 8)
    sprite('vrizef_shot01', 60)
    Unknown1028(1600)
    setGravity(1600)
    label(1)
    sprite('vrizef_shot01', 12)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown1028(0)
    setGravity(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 6)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Special_Shot_Event():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        AttackLevel_(3)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(16)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(5000)
        AttackP1(85)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        callSubroutine('ShotColorSwitch')
        Unknown4047(240, 241, 241)
        Unknown4045('697a65665f535073686f745f636972636c65000000000000000000000000000064000000')
        Unknown4047(241, 240, 240)
        Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

    def upon_11():
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 32)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 33)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 34)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 35)
    sprite('vrizef_shot01a', 5)
    Unknown3001(0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 1)
    sprite('vrizef_shot01a', 5)
    Unknown3004(40)
    sprite('vrizef_shot01b', 1)
    Unknown3001(255)
    RefreshMultihit()
    sprite('vrizef_shot01c', 1)
    sprite('vrizef_shot01d', 1)
    sprite('vrizef_shot01e', 1)
    sprite('vrizef_shot01f', 1)
    sprite('vrizef_shot01g', 1)
    sprite('vrizef_shot01h', 1)
    Unknown1028(200)
    physicsYImpulse(0)
    Unknown1108(0)
    sprite('vrizef_shot01i', 1)
    sprite('vrizef_shot01', 10)
    sprite('vrizef_shot01', 8)
    Unknown1028(800)
    sprite('vrizef_shot01', 60)
    Unknown1028(1600)
    sprite('vrizef_shot01', 12)
    Unknown23027()
    physicsXImpulse(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    Unknown1019(30)
    YAccel(30)
    Unknown1028(0)
    sprite('keep', 12)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Special_Shot_Air():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        AttackLevel_(3)
        Unknown9016(1)
        PushbackX(20000)
        Hitstop(16)
        Unknown11057(600)
        Unknown9154(22)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        PushbackX(0)
        AttackP1(85)
        Unknown23027()
        if SLOT_109:
            SLOT_52 = 1
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        sendToLabelUpon(2, 1)
        callSubroutine('ShotColorSwitch')
        Unknown4047(240, 241, 241)
        Unknown4048(45000)
        Unknown4045('697a65665f535073686f745f636972636c65000000000000000000000000000064000000')
        Unknown4047(241, 240, 240)
        Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

    def upon_11():
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 32)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 33)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 34)
        GFX_0('Special_Shot_Next', -1)
        Unknown21007(1, 35)
        if SLOT_52:
            GFX_0('Special_Shot_Next', -1)
            Unknown21007(1, 36)
            GFX_0('Special_Shot_Next', -1)
            Unknown21007(1, 37)
            GFX_0('Special_Shot_Next', -1)
            Unknown21007(1, 38)
            GFX_0('Special_Shot_Next', -1)
            Unknown21007(1, 39)
    sprite('vrizef_shot01a', 5)
    Unknown1072(45000)
    physicsXImpulse(300)
    physicsYImpulse(-300)
    Unknown3001(0)
    GFX_0('Shot_particle', 100)
    GFX_1('izef_armchange', 1)
    sprite('vrizef_shot01a', 5)
    Unknown3004(40)
    sprite('vrizef_shot01b', 1)
    Unknown3001(255)
    Unknown1028(100)
    setGravity(100)
    sprite('vrizef_shot01c', 1)
    sprite('vrizef_shot01d', 1)
    sprite('vrizef_shot01e', 1)
    sprite('vrizef_shot01f', 1)
    sprite('vrizef_shot01g', 1)
    sprite('vrizef_shot01h', 1)
    sprite('vrizef_shot01i', 1)
    RefreshMultihit()
    sprite('vrizef_shot01', 10)
    sprite('vrizef_shot01', 4)
    Unknown1028(800)
    setGravity(800)
    Unknown1108(0)
    Unknown2055(240)
    sprite('vrizef_shot01', 50)
    Unknown1028(1600)
    setGravity(1600)
    label(1)
    sprite('vrizef_shot01', 12)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    Unknown1084(1)
    sprite('keep', 12)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZSpecial_Shot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f73686f745f64656c6574655f636972636c6500000000000000000064000000')
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Special_Shot_Next():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        AttackLevel_(3)
        Damage(500)
        Unknown9016(1)
        Hitstop(0)
        Unknown11001(4, 4, 5)
        Unknown11057(600)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        Unknown11092(1)
        Unknown23182(2)
        Unknown23027()
        Unknown1096(800)
        callSubroutine('ShotColorSwitch')

        def upon_32():
            Unknown1086(22)
            teleportRelativeX(-250000)
            Unknown1007(400000)
            Unknown1072(45000)
            sendToLabel(0)
            SLOT_51 = 1
            Unknown4047(240, 241, 241)
            Unknown4048(45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_33():
            Unknown1086(22)
            teleportRelativeX(250000)
            Unknown1007(0)
            Unknown1072(-45000)
            Unknown2006()
            SLOT_51 = 4
            sendToLabel(1)
            Unknown11099(1)
            Unknown4047(240, 241, 241)
            Unknown4048(-45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_34():
            Unknown1086(22)
            teleportRelativeX(-250000)
            Unknown1007(0)
            Unknown1072(-45000)
            SLOT_51 = 3
            sendToLabel(2)
            Unknown4047(240, 241, 241)
            Unknown4048(-45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_35():
            Unknown1086(22)
            teleportRelativeX(250000)
            Unknown1007(400000)
            Unknown1072(45000)
            Unknown2006()
            SLOT_51 = 2
            sendToLabel(3)
            Unknown11099(1)
            Unknown4047(240, 241, 241)
            Unknown4048(45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_38():
            Unknown1086(22)
            teleportRelativeX(300000)
            Unknown1007(200000)
            Unknown1072(0)
            Unknown2006()
            SLOT_51 = 7
            sendToLabel(7)
            Unknown11099(1)
            Unknown4047(240, 241, 241)
            Unknown4048(0)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_39():
            Unknown1086(22)
            teleportRelativeX(-300000)
            Unknown1007(200000)
            Unknown1072(0)
            Unknown2006()
            SLOT_51 = 8
            sendToLabel(6)
            Unknown11099(0)
            Unknown4047(240, 241, 241)
            Unknown4048(0)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_36():
            Unknown1086(22)
            teleportRelativeX(0)
            Unknown1007(450000)
            Unknown1072(90000)
            Unknown2006()
            SLOT_51 = 5
            sendToLabel(4)
            Unknown11099(0)
            Unknown4047(240, 241, 241)
            Unknown4048(90000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_37():
            Unknown1086(22)
            teleportRelativeX(0)
            Unknown1007(-100000)
            Unknown1072(-90000)
            Unknown2006()
            SLOT_51 = 6
            sendToLabel(5)
            Unknown11099(0)
            Unknown4047(240, 241, 241)
            Unknown4048(-90000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
    label(7)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 26)
    gotoLabel(10)
    label(6)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 23)
    gotoLabel(10)
    label(5)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 20)
    gotoLabel(10)
    label(4)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 17)
    gotoLabel(10)
    label(3)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 14)
    gotoLabel(10)
    label(2)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 11)
    gotoLabel(10)
    label(1)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 8)
    gotoLabel(10)
    label(0)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 1)
    label(10)
    sprite('vrizef_shot02', 4)
    Unknown1110(40000, 0)
    sprite('vrizef_shot02', 20)
    RefreshMultihit()
    sendToLabelUpon(10, 11)
    sendToLabelUpon(2, 11)
    label(11)
    sprite('vrizef_shot02', 12)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Special_Shot_Next_PS():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
        Unknown3076(1000)
        Unknown3077(1000)
        AttackLevel_(3)
        Damage(500)
        AttackP1(70)
        Unknown9016(1)
        Hitstop(0)
        Unknown11001(4, 4, 5)
        Unknown11057(600)
        AirUntechableTime(22)
        AirPushbackY(13000)
        AirPushbackX(3000)
        Unknown11092(1)
        Unknown23182(2)
        Unknown23027()
        Unknown11042(1)
        Unknown1096(800)
        callSubroutine('ShotColorSwitch')

        def upon_32():
            Unknown1086(22)
            teleportRelativeX(-250000)
            Unknown1007(400000)
            Unknown1072(45000)
            sendToLabel(0)
            SLOT_51 = 1
            Unknown4047(240, 241, 241)
            Unknown4048(45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_33():
            Unknown1086(22)
            teleportRelativeX(250000)
            Unknown1007(0)
            Unknown1072(-45000)
            Unknown2006()
            SLOT_51 = 4
            sendToLabel(1)
            Unknown11099(1)
            Unknown4047(240, 241, 241)
            Unknown4048(-45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_34():
            Unknown1086(22)
            teleportRelativeX(-250000)
            Unknown1007(0)
            Unknown1072(-45000)
            SLOT_51 = 3
            sendToLabel(2)
            Unknown4047(240, 241, 241)
            Unknown4048(-45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_35():
            Unknown1086(22)
            teleportRelativeX(250000)
            Unknown1007(400000)
            Unknown1072(45000)
            Unknown2006()
            SLOT_51 = 2
            sendToLabel(3)
            Unknown11099(1)
            Unknown4047(240, 241, 241)
            Unknown4048(45000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_38():
            Unknown1086(22)
            teleportRelativeX(300000)
            Unknown1007(200000)
            Unknown1072(0)
            Unknown2006()
            SLOT_51 = 7
            sendToLabel(7)
            Unknown11099(1)
            Unknown4047(240, 241, 241)
            Unknown4048(0)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_39():
            Unknown1086(22)
            teleportRelativeX(-300000)
            Unknown1007(200000)
            Unknown1072(0)
            Unknown2006()
            SLOT_51 = 8
            sendToLabel(6)
            Unknown11099(0)
            Unknown4047(240, 241, 241)
            Unknown4048(0)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_36():
            Unknown1086(22)
            teleportRelativeX(0)
            Unknown1007(450000)
            Unknown1072(90000)
            Unknown2006()
            SLOT_51 = 5
            sendToLabel(4)
            Unknown11099(0)
            Unknown4047(240, 241, 241)
            Unknown4048(90000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')

        def upon_37():
            Unknown1086(22)
            teleportRelativeX(0)
            Unknown1007(-100000)
            Unknown1072(-90000)
            Unknown2006()
            SLOT_51 = 6
            sendToLabel(5)
            Unknown11099(0)
            Unknown4047(240, 241, 241)
            Unknown4048(-90000)
            Unknown4045('697a65665f73686f745f636972636c655f736d616c6c0000000000000000000001000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
    label(7)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 26)
    gotoLabel(10)
    label(6)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 23)
    gotoLabel(10)
    label(5)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 20)
    gotoLabel(10)
    label(4)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 17)
    gotoLabel(10)
    label(3)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 14)
    gotoLabel(10)
    label(2)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 11)
    gotoLabel(10)
    label(1)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 8)
    gotoLabel(10)
    label(0)
    sprite('vrizef_shot02a', 1)
    sprite('vrizef_shot02b', 1)
    sprite('vrizef_shot02c', 1)
    sprite('vrizef_shot02d', 1)
    sprite('vrizef_shot02e', 1)
    sprite('vrizef_shot02f', 1)
    sprite('vrizef_shot02g', 1)
    sprite('vrizef_shot02h', 1)
    sprite('vrizef_shot02i', 1)
    sprite('vrizef_shot02j', 1)
    sprite('vrizef_shot02', 1)
    label(10)
    sprite('vrizef_shot02', 4)
    Unknown1110(40000, 0)
    sprite('vrizef_shot02', 20)
    RefreshMultihit()
    sendToLabelUpon(10, 11)
    sendToLabelUpon(2, 11)
    label(11)
    sprite('vrizef_shot02', 12)
    Unknown23027()
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1028(0)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')
    loopRest()
    ExitState()
    label(580)
    sprite('keep', 12)
    Unknown1084(1)
    Unknown1059(60)
    Unknown1067(-60)
    Unknown3004(-20)
    GFX_0('DIST_IZShot', 100)
    GFX_1('izef_shot_delete_feather', 100)
    Unknown4047(241, 240, 240)
    Unknown4045('697a65665f73686f745f6475737400000000000000000000000000000000000064000000')

@State
def Shot_particle():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 1)
    GFX_1('izef_shot_dust', 100)
    gotoLabel(0)

@State
def WarpHoverAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown23015(5)
        Unknown2005()
        Unknown3033()
        Unknown1056(700)
        Unknown1064(400)
        Unknown3001(232)
        Unknown3004(50)
    sprite('null', 2)
    sprite('null', 2)
    Unknown3004(0)
    Unknown1056(600)
    teleportRelativeX(10000)
    sprite('null', 2)
    Unknown3001(200)
    Unknown1056(400)
    teleportRelativeX(30000)
    Unknown1007(-30000)
    sprite('null', 2)
    Unknown1064(300)
    Unknown1007(30000)
    Unknown1072(-25000)

@State
def WarpHoverAura_Air():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e4449470000000000000000000000000000697a65665f686f766572617572615f6d6f74696f6e5f3030302e6d6d6f740000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1056(700)
        Unknown1064(400)
        Unknown3001(100)
        Unknown3004(50)
    sprite('null', 2)
    sprite('null', 2)
    Unknown3004(0)
    Unknown1056(600)
    teleportRelativeX(10000)
    sprite('null', 2)
    Unknown3001(200)
    Unknown1056(400)
    teleportRelativeX(-30000)
    Unknown1007(-10000)
    sprite('null', 2)

@State
def WarpEff():

    def upon_IMMEDIATE():
        callSubroutine('ShotColorSwitch')
    sprite('null', 1)
    Unknown4049(800)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f77617270616972303100000000000000000000000000000000000064000000')
    Unknown4049(900)
    Unknown4045('697a65665f77617270616972303000000000000000000000000000000000000064000000')

@State
def WarpEff_D():

    def upon_IMMEDIATE():
        callSubroutine('ShotColorSwitch')
    sprite('null', 1)
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f77617270616972303000000000000000000000000000000000000064000000')
    Unknown4047(240, 241, 241)
    Unknown4045('697a65665f77617270616972303100000000000000000000000000000000000064000000')
    GFX_1('izef_warpair', 100)

@State
def Warp_D_Land_Zanzo00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz409_02', 6)
    Unknown23119(16777215, 6, 2)
    physicsXImpulse(16000)
    Unknown3004(-30)

@State
def Warp_D_Land_Zanzo01():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz409_02', 6)
    Unknown23119(16777215, 6, 2)
    physicsXImpulse(-16000)
    Unknown3004(-30)

@State
def Warp_A_Zanzo00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz409_04', 6)
    teleportRelativeX(96000)
    physicsXImpulse(-16000)
    Unknown3004(30)
    Unknown3001(0)

@State
def Warp_A_Zanzo01():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz409_04', 6)
    teleportRelativeX(-96000)
    physicsXImpulse(16000)
    Unknown3004(30)
    Unknown3001(0)

@State
def firespark():

    def upon_IMMEDIATE():
        GFX_2('izef_firespark')
    sprite('null', 45)
    Unknown2005()

@State
def Warp_D_Air_Zanzo00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz410_02', 6)
    Unknown23119(16777215, 6, 2)
    physicsXImpulse(16000)
    Unknown3004(-30)

@State
def Warp_D_Air_Zanzo01():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz410_02', 6)
    Unknown23119(16777215, 6, 2)
    physicsXImpulse(-16000)
    Unknown3004(-30)

@State
def Warp_B_Air_Zanzo00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz020_02', 6)
    Unknown23119(16777215, 6, 2)
    physicsXImpulse(16000)
    Unknown3004(-30)

@State
def Warp_B_Air_Zanzo01():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        setInvincible(1)
    sprite('iz020_02', 6)
    Unknown23119(16777215, 6, 2)
    physicsXImpulse(-16000)
    Unknown3004(-30)

@State
def DD_3d_zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3033()
        teleportRelativeX(168000)
        Unknown1007(224000)
        Unknown1096(1500)
        Unknown4003('697a65665f3433305f736c6173682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)
    sprite('null', 16)
    sprite('null', 8)
    Unknown3004(-32)

@State
def DD_pt_edge():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(240000)
        Unknown1007(224000)
        Unknown4061(2)
    sprite('null', 60)
    Unknown4047(246, 246, 246)
    Unknown4045('697a65665f44445f65646765000000000000000000000000000000000000000064000000')

@State
def DD_pt_circle():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(260000)
        Unknown1007(224000)
        Unknown1096(1000)
    sprite('null', 15)
    sprite('null', 60)
    GFX_2('izef_DD_circle')
    sprite('null', 30)
    Unknown3004(-8)

@State
def DD_3Dcircle_out():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f444472696e672e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown1096(1320)
        teleportRelativeX(260000)
        Unknown1007(204000)
    sprite('null', 25)
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 50)
    Unknown3001(200)
    Unknown3004(0)
    sprite('null', 40)
    Unknown1099(20)
    Unknown3004(-12)

@State
def DD_3Dcircle_in():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f44446d61686f6a696e2e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown1096(0)
        teleportRelativeX(190000)
        teleportRelativeY(230000)
    sprite('null', 25)
    Unknown3001(0)
    Unknown3004(8)
    Unknown1099(36)
    sprite('null', 50)
    Unknown1096(1080)
    Unknown1099(0)
    Unknown3001(240)
    Unknown3004(0)
    sprite('null', 40)
    Unknown1099(20)
    Unknown3004(-12)

@State
def DD_sword():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(226000)
        Unknown1007(234000)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef430swd00', 20)
    GFX_1('izef_DD_sword', -1)
    sprite('vrizef430swd00', 12)
    Unknown3004(-20)
    GFX_1('izef_dellight', 0)
    GFX_1('izef_dellight', 1)
    GFX_1('izef_dellight', 2)
    GFX_1('izef_dellight', 3)
    GFX_1('izef_dellight', 4)
    GFX_1('izef_dellight', 5)
    GFX_1('izef_dellight', 6)

@State
def DD_sword_env():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        teleportRelativeX(226000)
        Unknown1007(234000)
        Unknown4061(1)
        Unknown3001(100)
    sprite('vrizef430swd_env', 20)
    sprite('vrizef430swd_env', 10)
    Unknown3004(-10)

@State
def DD_3d_swordaura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        teleportRelativeX(256000)
        Unknown1007(224000)
        Unknown1056(875)
        Unknown1064(750)
        Unknown4003('697a65665f3433305f617572612e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 8)
    Unknown3004(-32)

@State
def DD_sword_OD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        teleportRelativeX(226000)
        Unknown1007(220000)
        Unknown4061(6)
        Unknown3033()
    sprite('vrizef430swd01', 20)
    GFX_1('izef_DD_sword', -1)
    sprite('vrizef430swd01', 12)
    Unknown3004(-20)
    GFX_1('izef_dellight', 0)
    GFX_1('izef_dellight', 1)
    GFX_1('izef_dellight', 2)
    GFX_1('izef_dellight', 3)
    GFX_1('izef_dellight', 4)
    GFX_1('izef_dellight', 5)
    GFX_1('izef_dellight', 6)
    GFX_1('izef_dellight', 7)
    GFX_1('izef_dellight', 8)
    GFX_1('izef_dellight', 9)
    GFX_1('izef_dellight', 10)
    GFX_1('izef_dellight', 11)
    GFX_1('izef_dellight', 12)

@State
def DD_sword_env_OD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3033()
        teleportRelativeX(226000)
        Unknown1007(234000)
        Unknown4061(1)
        Unknown3001(100)
    sprite('vrizef430swd01_env', 20)
    sprite('vrizef430swd01_env', 10)
    Unknown3004(-10)

@State
def UltimateAssaultAura():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown3033()
        Unknown1056(600)
        Unknown1064(500)
        Unknown1072(18000)
    sprite('null', 27)
    sprite('null', 3)
    Unknown1007(-12000)
    Unknown1056(400)
    Unknown1064(200)
    Unknown1072(-5000)

@State
def UltimateAssaultAura_back():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f617572612e44494700000000000000000000000000000000000000697a65665f617572615f6d6f74696f6e5f3030302e6d6d6f7400000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(500)
        Unknown1072(20000)
    sprite('null', 27)
    sprite('null', 3)
    Unknown1007(-12000)
    Unknown1056(400)
    Unknown1064(200)
    Unknown1072(-5000)

@State
def iz431_mahojin():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f4444326d61686f6a696e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(5)
        Unknown2054(1)
        Unknown4010(3)
        Unknown3033()
        Unknown1096(900)
    sprite('null', 120)
    sprite('null', 10)
    Unknown1099(5)
    sprite('null', 24)
    Unknown3004(-10)

@State
def SummonFunnelAuraR():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f444432617572612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1056(750)
        Unknown1072(-35000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown1096(600)
    Unknown1073(-3000)

@State
def SummonFunnelAuraL():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f444432617572612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown2005()
        Unknown1056(750)
        Unknown1072(-35000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 32767)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    Unknown1096(600)
    Unknown1073(-3000)

@State
def SummonFunnelF():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown23015(2)
        Unknown3032()
    sprite('iz431_f19', 4)
    GFX_0('SummonFunnelAuraL', 0)
    GFX_0('SummonFunnelAuraR', 1)
    GFX_1('izef_GNptcR', 1)
    GFX_1('izef_GNptcR', 2)
    GFX_1('izef_GNptcR', 3)
    GFX_1('izef_GNptcR', 6)
    GFX_1('izef_GNptcL', 0)
    GFX_1('izef_GNptcL', 4)
    GFX_1('izef_GNptcL', 5)
    GFX_1('izef_GNptcL', 7)
    sprite('iz431_f20', 16)
    sprite('iz431_f20', 16)
    sprite('iz431_f24', 4)
    Unknown21012('53756d6d6f6e46756e6e656c417572614c00000000000000000000000000000020000000')
    Unknown21012('53756d6d6f6e46756e6e656c417572615200000000000000000000000000000020000000')
    sprite('iz431_f25', 4)

@State
def AST1st_mahojin():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6d61686f6a696e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(1000)
    sprite('null', 40)
    Unknown1099(5)
    sprite('null', 70)
    Unknown1099(0)
    sprite('null', 10)
    Unknown1099(5)
    sprite('null', 24)
    Unknown3004(-10)

@State
def AST_changelightC():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        GFX_2('izef_AH_changelightC')
    sprite('null', 60)

@State
def AST_changeBG():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown2054(1)
        Unknown23015(5)
        Unknown3033()
        GFX_2('izef_AH_changeBG')
        sendToLabelUpon(32, 90)
    sprite('null', 60)
    loopRest()
    label(90)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(-25)

@State
def AstWhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown1096(10000)
        Unknown3033()
        Unknown3001(0)
    sprite('vr_white', 10)
    Unknown3004(25)
    sprite('vr_white', 20)
    sprite('vr_white', 30)
    Unknown3001(240)
    Unknown3004(-8)

@State
def AST_1stAuraL():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1056(1000)
        Unknown1064(1400)
        sendToLabelUpon(32, 1)
    sprite('null', 16)
    sprite('null', 6)
    teleportRelativeX(-20000)
    Unknown1056(700)
    Unknown1064(1400)
    sprite('null', 6)
    Unknown1064(1100)
    teleportRelativeX(-20000)
    Unknown1007(-32000)
    Unknown1072(18000)
    sprite('null', 6)
    teleportRelativeX(20000)
    Unknown1064(800)
    Unknown1073(2000)
    sprite('null', 6)
    Unknown1007(20000)
    Unknown1073(1000)
    sprite('null', 20)
    Unknown1064(1000)
    label(1)

@State
def AST_1stAuraR():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown2005()
        Unknown1056(1000)
        Unknown1064(1400)
    sprite('null', 16)
    sprite('null', 6)
    Unknown1007(-15000)
    teleportRelativeX(-15000)
    Unknown1056(700)
    Unknown1072(5000)
    sprite('null', 6)
    Unknown1064(1300)
    Unknown1072(14000)
    teleportRelativeX(25000)
    sprite('null', 6)
    Unknown1007(20000)
    teleportRelativeX(20000)
    Unknown1072(10000)
    Unknown1056(300)
    Unknown1064(700)
    sprite('null', 6)
    Unknown2005()
    teleportRelativeX(-48000)
    Unknown1072(28000)
    Unknown1056(200)
    Unknown1064(800)
    sprite('null', 20)
    Unknown1064(1000)
    Unknown1056(400)
    teleportRelativeX(-20000)

@State
def AST_2ndAurafront():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(4)
        Unknown3033()
        Unknown2005()
        Unknown1072(-12000)
    sprite('null', 5)
    sprite('null', 4)
    Unknown1073(-8000)
    Unknown1007(7760000)
    teleportRelativeX(180000)
    Unknown1056(900)
    Unknown1064(600)
    sprite('null', 4)
    Unknown1056(900)
    Unknown1064(450)
    Unknown1007(-9000)
    teleportRelativeX(150000)
    sprite('null', 4)
    teleportRelativeX(70000)
    Unknown1056(700)
    sprite('null', 4)
    teleportRelativeX(15000)
    Unknown1007(-9000)
    Unknown1056(700)
    sprite('null', 4)
    Unknown23015(5)
    Unknown1007(-9000)
    teleportRelativeX(35000)
    Unknown1056(500)
    Unknown1064(300)
    sprite('null', 4)
    Unknown1007(-9000)
    teleportRelativeX(35000)
    Unknown1073(-24000)
    Unknown1056(400)
    sprite('null', 4)
    Unknown1007(-9000)
    teleportRelativeX(30000)
    sprite('null', 4)
    Unknown1073(-24000)
    sprite('null', 4)
    Unknown1073(-28000)
    teleportRelativeX(30000)
    Unknown1064(500)
    Unknown1056(300)
    sprite('null', 4)
    Unknown1073(-28000)
    teleportRelativeX(30000)

@State
def AST_2ndAuraback():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown2005()
        Unknown1072(-20000)
        Unknown1096(900)
    sprite('null', 5)
    sprite('null', 4)
    Unknown1007(7760000)
    teleportRelativeX(150000)
    Unknown1096(600)
    sprite('null', 4)
    Unknown1096(500)
    teleportRelativeX(130000)
    sprite('null', 4)
    teleportRelativeX(100000)
    sprite('null', 4)
    teleportRelativeX(70000)
    Unknown1073(-25000)
    sprite('null', 4)
    teleportRelativeX(60000)
    Unknown1073(-12000)
    sprite('null', 4)
    teleportRelativeX(20000)
    Unknown1073(-20000)
    sprite('null', 4)
    Unknown2005()
    teleportRelativeX(-30000)
    Unknown1073(3000)
    Unknown1064(100)
    sprite('null', 4)
    Unknown1073(30000)
    Unknown1096(800)
    Unknown1007(20000)
    sprite('null', 4)
    sprite('null', 4)

@State
def AST_2ndAura():

    def upon_IMMEDIATE():
        teleportRelativeY(284000)
        Unknown3038(1)
    sprite('iz450cutin_15', 5)
    GFX_0('AST_2ndAurafront', 0)
    GFX_0('AST_2ndAuraback', 1)

@State
def AST_3rdAurafront():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(3)
        Unknown23015(1)
        Unknown3033()
        Unknown1056(900)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    Unknown1072(-30000)
    label(1)
    sprite('null', 5)
    sprite('null', 5)
    Unknown1073(-3000)
    sprite('null', 214)
    Unknown1073(-3000)
    sprite('null', 5)
    Unknown1073(15000)
    sprite('null', 5)
    sprite('null', 5)
    Unknown1007(-5000)
    sprite('null', 5)
    teleportRelativeX(5000)
    Unknown1056(800)
    sprite('null', 40)
    Unknown1072(-15000)
    Unknown1064(1500)
    Unknown1056(800)
    Unknown1007(15000)

@State
def AST_3rdAuraback():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f686f766572617572612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4009(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1096(900)
        Unknown3001(200)
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    Unknown1072(-45000)
    label(1)
    sprite('null', 5)
    sprite('null', 5)
    Unknown1073(-3000)
    sprite('null', 214)
    Unknown1073(-3000)
    sprite('null', 5)
    Unknown1073(15000)
    sprite('null', 5)
    sprite('null', 5)
    Unknown1007(15000)
    sprite('null', 5)
    teleportRelativeX(35000)
    Unknown1056(700)
    sprite('null', 40)
    Unknown1072(-15000)
    Unknown1064(1400)
    Unknown1056(400)
    Unknown1007(15000)

@State
def iz450cutin():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4009(3)
        Unknown4061(0)
        Unknown3032()
        Unknown6001(1)
        Unknown23032(50)
        teleportRelativeY(-384000)
        Unknown1001(640000)
    sprite('iz450cutin_00', 5)
    tag_voice(0, 'biz291_0', 'biz291_1', '', '')
    Unknown3001(0)
    Unknown3004(12)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    Unknown3001(255)
    sprite('iz450cutin_00', 5)
    GFX_0('izef_ah_cloud', -1)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    tag_voice(0, '', 'biz292_1', '', '')
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    tag_voice(0, 'biz292_0', '', '', '')
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_00', 5)
    sprite('iz450cutin_01', 5)
    sprite('iz450cutin_02', 5)
    sprite('iz450cutin_03', 5)
    sprite('iz450cutin_04', 5)
    sprite('iz450cutin_05', 5)
    sprite('iz450cutin_06', 5)
    sprite('iz450cutin_07', 5)
    sprite('iz450cutin_08', 5)
    sprite('iz450cutin_09', 5)
    sprite('iz450cutin_10', 5)
    sprite('iz450cutin_11', 5)
    sprite('iz450cutin_12', 5)
    sprite('iz450cutin_13', 5)
    sprite('iz450cutin_14', 5)
    sprite('iz450cutin_15', 5)
    GFX_0('AST_2ndAurafront', 0)
    GFX_0('AST_2ndAuraback', 1)
    sprite('iz450cutin_16', 4)
    sprite('iz450cutin_17', 4)
    sprite('iz450cutin_18', 4)
    sprite('iz450cutin_19', 4)
    sprite('iz450cutin_20', 4)
    sprite('iz450cutin_21', 4)
    sprite('iz450cutin_22', 4)
    sprite('iz450cutin_23', 4)
    sprite('iz450cutin_24', 4)
    sprite('iz450cutin_25', 4)
    physicsYImpulse(0)

@State
def iz450_shield():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3032()
    sprite('iz450_26ex', 45)

@State
def iz450_shieldlight():

    def upon_IMMEDIATE():
        Unknown3032()
    sprite('iz450_29ex', 20)
    Unknown23119(16777215, 15, 1)
    sprite('iz450_29ex', 5)
    Unknown3004(-50)
    Unknown4049(1500)
    Unknown4045('697a65665f736869656c6444656c00000000000000000000000000000000000000000000')
    Unknown4049(1500)
    Unknown4045('697a65665f736869656c6444656c00000000000000000000000000000000000001000000')

@State
def iz450dammy():

    def upon_IMMEDIATE():
        Unknown23015(0)
        Unknown3032()
        teleportRelativeX(-215000)
        Unknown1007(-102000)
    sprite('iz450_26', 5)
    GFX_0('iz450_shield', -1)
    GFX_0('AST_3rdAurafront', 0)
    GFX_0('AST_3rdAuraback', 1)
    sprite('iz450_27', 5)
    tag_voice(0, 'biz293_0', 'biz293_1', '', '')
    sprite('iz450_28', 5)
    sprite('iz450_26', 5)
    sprite('iz450_27', 5)
    sprite('iz450_28', 5)
    sprite('iz450_26', 5)
    sprite('iz450_27', 5)
    sprite('iz450_28', 5)
    sprite('iz450_29', 10)
    GFX_0('iz450_shieldlight', -1)
    sprite('iz450_30', 5)
    sprite('iz450_31', 5)
    Unknown21012('4153545f3372644175726166726f6e740000000000000000000000000000000020000000')
    Unknown21012('4153545f337264417572616261636b000000000000000000000000000000000020000000')
    sprite('iz450_32', 5)
    SFX_3('izse_05')
    sprite('iz450_33', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    Unknown4054(5)
    Unknown4048(-20000)
    Unknown4045('697a65665f41535470746343686172676574000000000000000000000000000000000000')
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    GFX_0('izef_ah_javelinwind', -1)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    tag_voice(0, 'biz294_0', 'biz294_1', '', '')
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    GFX_0('izef_ah_javelin', 0)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    tag_voice(0, 'biz295_0', 'biz295_1', '', '')
    Unknown4048(-55000)
    Unknown4049(1500)
    Unknown4054(1)
    Unknown4045('697a65665f41535463686172676500000000000000000000000000000000000001000000')
    Unknown4049(1000)
    Unknown4048(-5000)
    Unknown4054(1)
    Unknown4045('697a65665f41535463686172676500000000000000000000000000000000000002000000')
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    GFX_0('izef_ah_javelin_backfire', 0)
    sprite('iz450_34', 5)
    sprite('iz450_35', 5)
    sprite('iz450_36', 5)
    sprite('iz450_37', 5)
    sprite('iz450_38', 5)
    sprite('iz450_39', 5)
    sprite('iz450_40', 5)
    Unknown4049(1200)
    Unknown4048(-20000)
    Unknown4054(5)
    Unknown4045('697a65665f61685f6a6176656c696e6261636b6669726500000000000000000000000000')
    sprite('iz450_41', 5)
    teleportRelativeX(-3000)
    Unknown1007(-2000)
    physicsXImpulse(-5000)
    physicsYImpulse(-2000)
    Unknown21012('697a65665f61685f6a6176656c696e5f6261636b66697265000000000000000020000000')
    sprite('iz450_42', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('iz450_43', 5)
    Unknown1019(40)
    YAccel(40)
    Unknown21012('697a65665f61685f6a6176656c696e5f6261636b66697265000000000000000021000000')
    sprite('iz450_41', 5)
    Unknown1019(30)
    YAccel(30)
    sprite('iz450_42', 5)
    Unknown1019(20)
    YAccel(20)
    sprite('iz450_43', 5)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('iz450_41', 5)
    sprite('iz450_42', 5)

@State
def izef_ah_javelinwind():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f41535477696e64412e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(3)
        Unknown23015(5)
        Unknown3033()
        Unknown1000(-400000)
        Unknown1007(400000)
        Unknown1056(200)
        Unknown1064(80)
        Unknown1072(70000)
    sprite('null', 11)
    Unknown3001(0)
    Unknown3004(8)
    Unknown1099(100)
    sprite('null', 9)
    Unknown1099(0)
    sprite('null', 40)
    Unknown3001(160)
    Unknown3004(0)
    sprite('null', 30)
    Unknown3004(-8)
    Unknown1067(30)
    Unknown1059(100)

@State
def izef_ah_javelin():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6a6176656c696e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown23015(5)
        Unknown3032()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(24)
    Unknown1096(1400)
    Unknown1072(-11000)
    Unknown1007(60000)
    teleportRelativeX(-90000)
    sprite('null', 20)
    Unknown3001(255)
    Unknown3004(0)
    sprite('null', 120)
    GFX_1('izef_shot_haneopen', -1)
    sprite('null', 20)
    label(0)
    sprite('null', 32767)
    physicsYImpulse(60000)
    Unknown3001(0)
    physicsXImpulse(150000)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def izef_ah_cloud():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f636c6f75642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(3)
        Unknown4010(3)
        Unknown3032()
        Unknown1007(7800000)
        Unknown23015(2)
        Unknown3001(80)
    sprite('null', 550)

@State
def izef_ah_javelin2():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6a6176656c696e5f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown3032()
        teleportRelativeX(-100000)
        Unknown1007(-50000)
        Unknown23015(2)
        Unknown2005()
    sprite('null', 38)
    sprite('null', 10)
    ScreenShake(15000, 15000)
    sprite('null', 10)
    GFX_0('izef_ah_kirikaeWhite', -1)
    sprite('null', 1)
    Unknown3001(0)

@State
def izef_ah_javelin3():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6a6176656c696e5f30322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown21010(1)
        Unknown1007(180000)
        Unknown1096(1200)
        Unknown2019(-1000)
        Unknown23015(4)
    sprite('null', 30)
    sprite('null', 10)
    Unknown3001(0)
    GFX_1('izef_ahfinalhit', -1)
    sprite('null', 60)
    GFX_0('izef_ah_killwhite', -1)

@State
def izef_ah_Ryuhai():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown6001(1)
        Unknown4007(3)
        Unknown23032(50)
        Unknown3032()
        Unknown4003('697a65665f61685f6b6972696b616500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 30)

@State
def izef_ah_kirikaeWhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown6001(1)
        Unknown4007(3)
        Unknown23032(50)
        Unknown1096(10000)
        Unknown3032()
        Unknown3026(-16777216)
        Unknown3001(0)
    sprite('vr_white', 5)
    Unknown3004(51)
    sprite('vr_white', 8)
    sprite('vr_white', 5)
    Unknown3004(-51)

@State
def izef_ah_killwhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown6001(1)
        Unknown4007(3)
        Unknown23032(50)
        Unknown1096(10000)
        Unknown3033()
        Unknown3001(0)
    sprite('vr_white', 5)
    Unknown3004(51)
    sprite('vr_white', 120)
    sprite('vr_white', 5)
    Unknown3004(-51)

@State
def izef_ah_javelin_backfire():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6a6176656c696e5f6261636b666972652e444947000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown23015(5)
        Unknown3033()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 10)
    Unknown1096(1400)
    Unknown3001(0)
    Unknown3004(24)
    Unknown1072(-21000)
    sprite('null', 140)
    Unknown1072(-21000)
    label(0)
    sprite('null', 32767)
    physicsYImpulse(60000)
    physicsXImpulse(150000)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def AstWhitefinish():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(4)
        Unknown6001(1)
        Unknown4007(3)
        Unknown23032(50)
        Unknown3026(-16777216)
        Unknown1096(10000)
        Unknown3032()
        Unknown3001(0)
    sprite('vr_white', 15)
    sprite('vr_white', 30)
    Unknown3004(51)
    sprite('vr_white', 30)
    Unknown3004(-20)

@State
def izef_ah_javelin00():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6a6176656c696e2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(0)
        Unknown1072(-30000)
        Unknown1096(2000)

        def upon_43():
            if (SLOT_48 == 9002):
                sendToLabel(1)
    sprite('null', 30)
    teleportRelativeX(-1240000)
    Unknown1007(-475000)
    sprite('null', 10)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    sprite('null', 65)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('null', 5)
    physicsYImpulse(8000)
    physicsXImpulse(15000)
    sprite('null', 32767)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def izef_ah_javelin_backfire00():

    def upon_IMMEDIATE():
        Unknown4003('697a65665f61685f6a6176656c696e5f6261636b666972652e444947000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(0)
        Unknown1072(-30000)
        Unknown1096(2000)

        def upon_43():
            if (SLOT_48 == 9003):
                sendToLabel(1)
    sprite('null', 30)
    teleportRelativeX(-1240000)
    Unknown1007(-475000)
    sprite('null', 10)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    sprite('null', 65)
    physicsYImpulse(0)
    physicsXImpulse(0)
    sprite('null', 5)
    physicsYImpulse(8000)
    physicsXImpulse(15000)
    sprite('null', 32767)
    physicsYImpulse(40000)
    physicsXImpulse(75000)
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def ASTbg():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('697a65665f61685f6a6176656c696e5f736b792e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4007(3)
        Unknown23015(2)
        teleportRelativeY(250000)

        def upon_43():
            if (SLOT_48 == 9001):
                sendToLabel(1)
    sprite('null', 32767)
    GFX_2('izef_shot_ahspeed')
    label(1)
    sprite('null', 1)
    Unknown3001(0)

@State
def AstralHeatNotKillObject():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11023(1)
        AttackLevel_(4)
        AirPushbackY(0)
        Hitstop(3)
        Unknown11064(1)
        PushbackX(0)
        AirPushbackX(0)
        YImpluseBeforeWallbounce(0)
        Unknown11101(10)
        Unknown9154(1200)
        Unknown9015(1)
        Unknown3038(1)
    sprite('vrASTact', 1)
    Unknown1086(22)

@State
def AstralHeatKillObject():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11023(1)
        AttackLevel_(4)
        Damage(37800)
        Unknown11091(100)
        AirPushbackY(0)
        Hitstop(0)
        Unknown11064(3)
        PushbackX(0)
        AirPushbackX(0)
        YImpluseBeforeWallbounce(100000)
        Unknown11064(3)
        Unknown9016(1)
        Unknown3038(1)
    sprite('vrASTact', 1)
    Unknown1086(22)

@State
def Twindrive0():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown32('497a4566665477696e44726976650000')
        SLOT_59 = 0
        Unknown4061(1)
        Unknown3026(-16711808)
    label(0)
    if (SLOT_60 == 1):
        GFX_1('izef_twindrivePtc_f', 0)
    if (SLOT_60 == 2):
        GFX_1('izef_twindrivePtc_b', 0)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def Twindrive1():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown32('497a4566665477696e44726976650000')
        SLOT_59 = 1
        Unknown4061(1)
        Unknown3026(-16711808)
    label(0)
    if (SLOT_60 == 1):
        GFX_1('izef_twindrivePtc_f', -1)
    if (SLOT_60 == 2):
        GFX_1('izef_twindrivePtc_b', -1)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def TwindriveParts_Front0():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3026(-16711808)
        Unknown2019(-500)
        Unknown4010(3)
        Unknown4007(2)
        Unknown4009(3)
        Unknown2054(1)
    sprite('vr_light', 3)
    GFX_1('izef_twindrivePtc_f', 0)

@State
def iz601amourlight():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown4061(1)
    sprite('vrizef601_09', 7)
    sprite('vrizef601_10', 7)
    Unknown3004(-20)
    sprite('vrizef601_11', 7)

@State
def iz601swdlight():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown4061(1)
    sprite('vrizef601_18', 7)
    Unknown3004(-20)
    sprite('vrizef601_19', 7)

@State
def EntryFallSword():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2019(500)
        Unknown3032()
        teleportRelativeY(760000)
        teleportRelativeX(-140000)
    sprite('iz601_f00', 12)
    physicsYImpulse(-60000)
    sprite('iz601_f00', 5)
    physicsYImpulse(-2000)
    Unknown4045('697a65665f6472697665636972636c6500000000000000000000000000000000ffffffff')
    sprite('iz601_f00', 5)
    physicsYImpulse(-1000)
    sprite('iz601_f00', 10)
    physicsYImpulse(-500)
    sprite('iz601_f00', 10)
    GFX_1('izef_entrylightA', 0)
    sprite('iz601_f00', 5)
    sprite('iz601_f00', 12)
    sprite('iz601_f00', 6)
    GFX_1('izef_entrylight01', 0)

@State
def EventJNVsRCDownLoop():
    Unknown4061(7)
    Unknown1000(140000)
    sendToLabelUpon(32, 1)
    label(0)
    sprite('jn063_09', 1)
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    Unknown2019(-500)
    Unknown2034(0)
    Unknown3032()
    sprite('jn063_09', 26)
    GFX_1('story_rc_teni', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('jn063_09', 1)
    Unknown1000(-500000)
    sprite('null', 32767)
    loopRest()

@State
def EventTBYoroke():
    sendToLabelUpon(32, 1)
    Unknown4061(3)
    label(0)
    sprite('tb070_02', 5)
    sprite('tb070_03', 5)
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('null', 32767)
    loopRest()

@State
def BurstDDTwindrive0():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown32('497a4566665477696e44726976650000')
        SLOT_59 = 0
        Unknown4061(1)
        Unknown3026(-16711808)
    label(0)
    if (SLOT_60 == 1):
        GFX_1('izef_twindrivePtc_f', 0)
    if (SLOT_60 == 2):
        GFX_1('izef_twindrivePtc_b', 0)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def BurstDDTwindrive1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown32('497a4566665477696e44726976650000')
        SLOT_59 = 1
        Unknown4061(1)
        Unknown3026(-16711808)
    label(0)
    if (SLOT_60 == 1):
        GFX_1('izef_twindrivePtc_f', -1)
    if (SLOT_60 == 2):
        GFX_1('izef_twindrivePtc_b', -1)
    sprite('vr_light', 5)
    loopRest()
    gotoLabel(0)

@State
def BurstDDFunnel():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown4010(3)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        AirUntechableTime(180)
        Unknown9154(180)
        Hitstop(3)
        PushbackX(4900)
        AttackP2(100)
        Unknown9016(1)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11091(10)
        Unknown11023(1)
        Unknown11066(1)
        Unknown11069('BurstDDFunnel')
        Unknown11108('03000000')

        def upon_43():
            if (SLOT_48 == 6001):
                sendToLabel(100)
    sprite('iz440_f05', 1)
    GFX_0('BurstDDTwindrive0', -1)
    GFX_0('BurstDDTwindrive1', -1)
    sprite('iz440_f05', 2)
    sprite('iz440_f06', 3)
    sprite('iz440_f07', 3)
    sprite('iz440_f08', 3)
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    GFX_0('BurstDDSlash', -1)
    SFX_0('006_swing_blade_1')
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    ScreenShake(10000, 10000)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    Unknown23029(3, 6002, 0)
    sprite('iz440_f10', 2)
    sprite('iz440_f11', 2)
    sprite('iz440_f13', 2)
    sprite('iz440_f14', 2)
    sprite('iz440_f15', 2)
    sprite('iz440_f16', 2)
    sprite('iz440_f17', 2)
    sprite('iz440_f18', 2)
    sprite('iz440_f19', 2)
    sprite('iz440_f20', 3)
    GFX_0('BurstDDSlash2', -1)
    SFX_0('006_swing_blade_1')
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    ScreenShake(10000, 10000)
    RefreshMultihit()
    Unknown11069('BurstDDFunnelLastAtk')
    sprite('iz440_f19', 5)
    sprite('iz440_f21', 5)
    sprite('iz440_f23', 5)
    Unknown23029(3, 6003, 0)
    sprite('iz440_f24', 6)
    sprite('iz440_f25', 6)
    sprite('iz440_f26', 6)
    sprite('iz440_f27', 6)
    sprite('iz440_f28', 9)
    sprite('iz440_f28a', 3)
    sprite('iz440_f28b', 2)
    GFX_1('izef_440fwarp00', 0)
    GFX_1('izef_440fwarp00', 1)
    SFX_3('izse_04')
    sprite('null', 300)
    Unknown3001(0)
    Unknown3004(0)
    GFX_0('BurstDDFunnelLastAtk', -1)
    Unknown23029(1, 6005, 0)
    GFX_0('BurstDDFunnelLastAtk', -1)
    Unknown23029(1, 6006, 0)
    ExitState()
    label(100)
    sprite('iz440_f05', 2)
    Damage(1500)
    sprite('iz440_f06', 3)
    sprite('iz440_f07', 3)
    sprite('iz440_f08', 3)
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    GFX_0('BurstDDSlashEX', -1)
    SFX_0('006_swing_blade_2')
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    sprite('iz440_f10', 3)
    sprite('iz440_f11', 3)
    sprite('iz440_f12', 3)
    RefreshMultihit()
    sprite('iz440_f09', 3)
    Unknown21015('42757273744444536c61736845580000000000000000000000000000000000007917000000000000')
    Unknown23029(3, 6002, 0)
    sprite('iz440_f10', 2)
    sprite('iz440_f11', 2)
    sprite('iz440_f13', 2)
    sprite('iz440_f14', 2)
    sprite('iz440_f15', 2)
    sprite('iz440_f16', 2)
    sprite('iz440_f17', 2)
    sprite('iz440_f18', 2)
    sprite('iz440_f19', 2)
    sprite('iz440_f20', 3)
    GFX_0('BurstDDSlashEX2', -1)
    SFX_0('006_swing_blade_2')
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    RefreshMultihit()
    sprite('iz440_f19', 3)
    sprite('iz440_f20', 3)
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    RefreshMultihit()
    sprite('iz440_f19', 3)
    sprite('iz440_f20', 3)
    sprite('iz440_f21', 3)
    sprite('iz440_f22', 3)
    RefreshMultihit()
    Unknown11069('BurstDDFunnelLastAtk')
    sprite('iz440_f19', 5)
    Unknown21015('42757273744444536c61736845583200000000000000000000000000000000007a17000000000000')
    sprite('iz440_f21', 5)
    sprite('iz440_f23', 5)
    Unknown23029(3, 6003, 0)
    sprite('iz440_f24', 6)
    sprite('iz440_f25', 6)
    sprite('iz440_f26', 6)
    sprite('iz440_f27', 6)
    sprite('iz440_f28', 15)
    sprite('iz440_f28a', 3)
    sprite('iz440_f28b', 2)
    GFX_1('izef_440fwarp00', 0)
    GFX_1('izef_440fwarp00', 1)
    SFX_3('izse_04')
    sprite('null', 300)
    Unknown3001(0)
    Unknown3004(0)
    GFX_0('BurstDDFunnelLastAtk', -1)
    Unknown23029(1, 6007, 0)
    GFX_0('BurstDDFunnelLastAtk', -1)
    Unknown23029(1, 6008, 0)
    ExitState()

@State
def BurstDDFunnelLastAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        AirUntechableTime(60)
        Unknown9310(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(0)
        AirPushbackX(1000)
        AirPushbackY(35000)
        Unknown9016(1)
        AttackP2(100)
        Unknown23182(2)
        Unknown1086(22)
        Unknown11091(25)
        Unknown11066(1)
        Unknown23027()

        def upon_43():
            if (SLOT_48 == 6005):
                teleportRelativeX(-300000)
                Unknown2001()
            if (SLOT_48 == 6006):
                teleportRelativeX(300000)
            if (SLOT_48 == 6007):
                Damage(1700)
                teleportRelativeX(-300000)
                Unknown2001()
                sendToLabel(100)
            if (SLOT_48 == 6008):
                Damage(1700)
                teleportRelativeX(300000)
                sendToLabel(100)

        def upon_12():
            Unknown23011(1)
    sprite('null', 1)
    Unknown1007(400000)
    sprite('null', 4)
    sprite('iz440_f29warp01', 2)
    Unknown2006()
    Unknown2005()
    sprite('iz440_f29warp00', 2)
    sprite('iz440_f29ex01', 3)
    GFX_0('BurstDDSordEff', -1)
    GFX_0('BurstDDTwindrive0', -1)
    sprite('iz440_f29ex01', 5)
    GFX_1('izef_440fwarp00', 0)
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    sprite('iz440_f29ex01', 7)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex01', 7)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex01', 7)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex02', 1)
    Unknown3001(255)
    physicsXImpulse(-150000)
    physicsYImpulse(-100000)
    Unknown21015('427572737444445f4d61676963436972636c65000000000000000000000000007b17000000000000')
    sprite('iz440_f29ex02', 1)
    RefreshMultihit()
    Unknown11069('')
    Unknown23029(3, 6014, 0)
    sprite('iz440_f29ex02', 2)
    GFX_0('BurstDDLastAtk', -1)
    sprite('iz440_f29ex02', 4)
    Unknown3001(0)
    Unknown3004(0)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    Unknown1019(50)
    YAccel(50)
    Unknown21015('427572737444444c61737441746b0000000000000000000000000000000000007c17000000000000')
    ExitState()
    label(100)
    sprite('null', 4)
    SFX_3('izse_12')
    sprite('iz440_f29warp01', 2)
    Unknown2006()
    Unknown2005()
    GFX_1('izef_440fwarp00', 0)
    sprite('iz440_f29warp00', 2)
    sprite('iz440_f29ex01', 3)
    GFX_0('BurstDDSordEff', -1)
    GFX_0('BurstDDTwindrive0', -1)
    sprite('iz440_f29ex01', 5)
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    sprite('iz440_f29ex01', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex01', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex01', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex02', 1)
    Unknown3001(255)
    physicsXImpulse(-150000)
    physicsYImpulse(-100000)
    Unknown21015('427572737444445f4d61676963436972636c65000000000000000000000000007b17000000000000')
    sprite('iz440_f29ex02', 1)
    RefreshMultihit()
    Unknown11069('')
    Unknown23029(3, 6014, 0)
    sprite('iz440_f29ex02', 2)
    GFX_0('BurstDDLastAtkEX', -1)
    sprite('iz440_f29ex02', 4)
    Unknown3001(0)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    Unknown1019(50)
    YAccel(50)
    sprite('iz440_f29ex02', 4)
    Unknown1019(50)
    YAccel(50)
    Unknown21015('427572737444444c61737441746b4558000000000000000000000000000000007d17000000000000')
    ExitState()

@State
def BurstDD_MagicCircle():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('697a65665f6c6f636b6d61676963322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown1096(800)
        Unknown3026(-76)

        def upon_3():
            Unknown1086(22)
            teleportRelativeX(-25000)
            Unknown1007(200000)

        def upon_43():
            if (SLOT_48 == 6011):
                sendToLabel(98)
    sprite('null', 32767)
    loopRest()
    label(98)
    sprite('null', 1)
    Unknown4007(0)
    sprite('null', 4)
    Unknown3004(-51)
    Unknown1059(200)
    Unknown1067(100)

@State
def BurstDDCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)

        def upon_3():
            Unknown1086(3)
            Unknown2006()
            SLOT_51 = SLOT_19
            SLOT_51 = (SLOT_51 / 2)
            Unknown48('190000000200000034000000030000000200000016000000')
            Unknown48('190000000200000035000000160000000200000016000000')
            if (SLOT_52 < SLOT_53):
                SLOT_22 = (SLOT_22 + SLOT_51)
            elif (SLOT_52 > SLOT_53):
                SLOT_22 = (SLOT_22 - SLOT_51)
            else:
                pass
            SLOT_22 = (SLOT_22 + 0)

        def upon_43():
            if (SLOT_48 == 6004):
                sendToLabel(1)
    label(0)
    sprite('null', 300)
    Unknown20000(1)
    Unknown20003(1)
    label(1)
    sprite('null', 1)
    Unknown20000(0)
    Unknown20003(0)

@State
def BurstDDSlash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vrizef440_00', 3)
    sprite('vrizef440_01', 3)
    sprite('vrizef440_02', 3)
    sprite('vrizef440_03', 3)
    sprite('vrizef440_00', 2)
    Unknown3004(-48)
    sprite('vrizef440_01', 2)

@State
def BurstDDSlash2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vrizef440_10', 3)
    sprite('vrizef440_11', 3)
    sprite('vrizef440_12', 3)
    sprite('vrizef440_13', 5)
    Unknown3004(-31)
    sprite('vrizef440_12', 3)

@State
def BurstDDSlashEX():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 6009):
                sendToLabel(1)
    label(0)
    sprite('vrizef440_00', 3)
    sprite('vrizef440_01', 3)
    sprite('vrizef440_02', 3)
    ScreenShake(10000, 10000)
    sprite('vrizef440_03', 3)
    gotoLabel(0)
    label(1)
    sprite('vrizef440_03', 3)
    Unknown3004(-36)
    sprite('vrizef440_00', 2)
    sprite('vrizef440_01', 2)

@State
def BurstDDSlashEX2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 6010):
                sendToLabel(1)
    label(0)
    sprite('vrizef440_10', 3)
    sprite('vrizef440_11', 3)
    sprite('vrizef440_12', 3)
    ScreenShake(10000, 10000)
    sprite('vrizef440_13', 3)
    gotoLabel(0)
    label(1)
    sprite('vrizef440_13', 5)
    Unknown3004(-51)

@State
def BurstDDLastAtk():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown1096(600)
        Unknown1007(250000)
        Unknown4003('697a65665f34343063726f73735f3030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 6012):
                sendToLabel(1)
    sprite('null', 6)
    Unknown1099(150)
    ScreenShake(10000, 10000)
    GFX_1('izef_440open', -1)
    label(0)
    sprite('null', 1)
    Unknown1097(200)
    Unknown1099(0)
    sprite('null', 1)
    Unknown1097(-200)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    GFX_1('izef_440cross', -1)
    sprite('null', 2)
    GFX_1('izef_440endkira_posL', -1)
    GFX_1('izef_440endkira_posR', -1)

@State
def BurstDDLastAtkEX():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown1096(600)
        Unknown1007(250000)
        Unknown4003('697a65665f34343063726f73735f3031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 6013):
                sendToLabel(1)
    sprite('null', 6)
    Unknown1099(200)
    ScreenShake(10000, 10000)
    Unknown4049(1300)
    Unknown4045('697a65665f3434306f70656e4558000000000000000000000000000000000000ffffffff')
    label(0)
    sprite('null', 1)
    Unknown1097(200)
    Unknown1099(0)
    sprite('null', 1)
    Unknown1097(-200)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    GFX_1('izef_440crossEX', -1)
    sprite('null', 2)
    Unknown4049(1300)
    Unknown4045('697a65665f343430656e646b69726145585f706f734c00000000000000000000ffffffff')
    Unknown4049(1300)
    Unknown4045('697a65665f343430656e646b69726145585f706f735200000000000000000000ffffffff')

@State
def BurstDDRetrunEff():

    def upon_IMMEDIATE():
        Unknown4061(2)
        Unknown3033()
    sprite('vrizef440_20', 4)
    sprite('vrizef440_21', 2)
    sprite('vrizef440_22', 2)
    sprite('vrizef440_23', 5)
    Unknown3004(-51)

@State
def BurstDDSlashEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
    sprite('vrizef440_30', 2)
    sprite('vrizef440_31', 2)

@State
def BurstDDSlashEff2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        callSubroutine('ShotColorSwitch')
        Unknown3033()
        Unknown23015(11)
    sprite('vrizef440_50', 6)
    sprite('vrizef440_51', 4)
    sprite('vrizef440_52', 4)

@State
def BurstDDSordEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(2)
    sprite('vrizef440_40', 7)
    sprite('vrizef440_41', 6)
    sprite('vrizef440_42', 6)
    sprite('vrizef440_43', 4)
    sprite('vrizef440_44', 4)
    sprite('vrizef440_45', 32767)

@State
def Act2Event_Yure():
    label(0)
    sprite('null', 10)
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Act3Event_IZDummy():
    sprite('iz063_11', 32767)