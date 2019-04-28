@State
def PBC_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('5042435f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PBC_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PBC_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PBC_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 200):
            Unknown23185('5042435f506572736f6e615f364173736973740000000000000000000000000032000000')
        if (SLOT_48 == 202):
            Unknown23185('5042435f506572736f6e614a440000000000000000000000000000000000000032000000')
        if (SLOT_48 == 220):
            Unknown23185('5042435f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 230):
            Unknown23185('5042435f506572736f6e6132430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 210):
            Unknown23185('5042435f506572736f6e6153686f745f4134746800000000000000000000000064000000')
        if (SLOT_48 == 240):
            Unknown23185('5042435f506572736f6e6135440000000000000000000000000000000000000032000000')
        if (SLOT_48 == 250):
            Unknown23185('5042435f506572736f6e6135444400000000000000000000000000000000000032000000')
        if (SLOT_48 == 260):
            Unknown23185('5042435f506572736f6e614a430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 700):
            Unknown23185('5042435f506572736f6e61437275736841747461636b0000000000000000000032000000')
        if (SLOT_48 == 500):
            Unknown23185('5042435f506572736f6e6153686f74410000000000000000000000000000000064000000')
        if (SLOT_48 == 510):
            Unknown23185('5042435f506572736f6e6153686f74420000000000000000000000000000000064000000')
        if (SLOT_48 == 520):
            Unknown23185('5042435f506572736f6e6153686f745f4578000000000000000000000000000064000000')
        if (SLOT_48 == 530):
            Unknown23185('5042435f506572736f6e614c6f7741737361756c74410000000000000000000064000000')
        if (SLOT_48 == 540):
            Unknown23185('5042435f506572736f6e614c6f7741737361756c74420000000000000000000064000000')
        if (SLOT_48 == 550):
            Unknown23185('5042435f506572736f6e614c6f7741737361756c745f4578000000000000000064000000')
        if (SLOT_48 == 900):
            Unknown23185('5042435f506572736f6e61556c74696d6174654c617365720000000000000000c8000000')
        if (SLOT_48 == 910):
            Unknown23185('5042435f506572736f6e61556c74696d6174654c617365724f44000000000000c8000000')
        if (SLOT_48 == 920):
            Unknown23185('5042435f506572736f6e61556c74696d617465426c6164650000000000000000c8000000')
        if (SLOT_48 == 930):
            Unknown23185('5042435f506572736f6e61556c74696d617465426c6164654f44000000000000c8000000')
        if (SLOT_48 == 940):
            Unknown23185('5042435f506572736f6e61556c74696d617465426c6164655441470000000000c8000000')
        if (SLOT_48 == 950):
            Unknown23185('5042435f506572736f6e61556c74696d617465426c6164654f44544147000000c8000000')
        if (SLOT_48 == 960):
            Unknown23185('506572736f6e614963686967656b690000000000000000000000000000000000c8000000')
        if (SLOT_48 == 1000):
            Unknown23185('5042435f506572736f6e61456e747279000000000000000000000000000000002c010000')
        if (SLOT_48 == 9999):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')
        if (SLOT_48 == 1100):
            Unknown23185('506572736f6e614963686967656b6957696e0000000000000000000000000000c8000000')

@Subroutine
def PersonaReset():
    Unknown4061(1)
    Unknown23022(0)
    Unknown2053(0)
    Unknown23015(11)
    Unknown2019(-1)
    Unknown1084(1)
    Unknown4009(0)
    Unknown4008(0)
    Unknown4007(0)
    Unknown2017(0)
    Unknown30041('')
    Unknown3031()

@Subroutine
def PBC_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PBC_AttackInit():
    Unknown23028(1, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 100
    callSubroutine('PBC_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PBC_SPAttackInit():
    Unknown23028(2, 1)
    Unknown30037('')
    Unknown30035(1)
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    SLOT_11 = 110
    callSubroutine('PBC_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PBC_DDAttackInit():
    Unknown23028(3, 1)
    Unknown30037('')
    callSubroutine('PersonaReset')
    Unknown23015(11)
    Unknown2019(10)
    if (SLOT_11 == 0):
        SLOT_58 = 1
    if (SLOT_11 == 10):
        SLOT_58 = 1
    Unknown11034(1)
    Unknown11033(0)
    SLOT_11 = 120
    callSubroutine('PBC_ReceptionSignal')
    Unknown23023()

@Subroutine
def PBC_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PBC_ForceWarp():
    SLOT_58 = 1
    Unknown3001(0)
    Unknown3004(85)
    loopRelated(17, 4)

    def upon_17():
        Unknown3001(255)
        Unknown3004(0)

@State
def PersonaDeleteAndIdling():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
    sprite('keep', 32767)	# 1-32767
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_0('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PBC_PersonaWait')

@State
def PersonaSummonEffect():
    sprite('null', 30)	# 1-30
    Unknown23015(13)
    Unknown4054(11)
    Unknown4045('706572736f6e615f73756d6d6f6e00000000000000000000000000000000000064000000')

@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)	# 1-30
    Unknown1007(288000)
    teleportRelativeX(112000)
    GFX_1('persona_summon_ply', 100)

@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PBC_ReceptionSignal')
    sprite('null', 30)	# 1-30
    Unknown2019(1)
    Unknown23053('190000000b000000')
    Unknown4061(1)
    Unknown3032()
    Unknown1059(-100)
    Unknown1067(150)
    Unknown3004(-20)
    Unknown23022(1)
    Unknown4054(11)
    Unknown4045('706572736f6e615f64656c65746500000000000000000000000000000000000064000000')
    Unknown2054(1)
    Unknown2017(0)
    Unknown1084(1)

@State
def PBC_Persona5D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000040420f000000000000000000')
        callSubroutine('PBC_AttackInit')
        AttackLevel_(3)
        AttackP1(90)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Hitstop(9)
        Unknown23027()
        Unknown23078(1)
        callSubroutine('PBC_CheckWarp')
        Unknown2053(1)
        Unknown2015(180)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 250000):
                    sendToLabel(0)
    sprite('iz205_00', 2)	# 1-2
    Unknown2006()
    sprite('iz205_01', 3)	# 3-5
    sprite('iz205_02', 3)	# 6-8
    Unknown4007(0)
    sprite('iz205_03', 9)	# 9-17
    ScreenShake(20000, 0)
    sprite('iz205_04', 2)	# 18-19
    sprite('iz205_05', 2)	# 20-21
    physicsXImpulse(20000)
    sprite('iz205_06', 1)	# 22-22
    Unknown1019(150)
    SFX_3('slash_blade_slow')
    sprite('iz205_07', 3)	# 23-25	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    Unknown1019(150)
    Unknown2037(1)
    sprite('iz205_08', 3)	# 26-28	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    sprite('iz205_07', 3)	# 29-31	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    sprite('iz205_08', 3)	# 32-34	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    label(0)
    sprite('keep', 4)	# 35-38
    clearUponHandler(3)
    Unknown1019(50)
    RefreshMultihit()
    sprite('iz205_10', 3)	# 39-41	 **attackbox here**
    GFX_0('TsukiZanzoh5D', 100)
    Unknown38(4, 1)
    RefreshMultihit()
    Unknown23029(2, 12, 0)
    sprite('iz205_11', 3)	# 42-44
    Unknown1019(50)
    Unknown23027()
    sprite('iz205_12', 3)	# 45-47
    Unknown1019(50)
    sprite('iz205_10', 3)	# 48-50	 **attackbox here**
    Unknown1019(0)
    sprite('iz205_11', 3)	# 51-53
    sprite('iz205_12', 3)	# 54-56
    sprite('iz205_10', 4)	# 57-60	 **attackbox here**
    sprite('iz205_11', 4)	# 61-64
    sprite('iz205_12', 4)	# 65-68
    label(580)
    sprite('keep', 32767)	# 69-32835
    enterState('PersonaDeleteAndIdling')

@State
def PBC_Persona5DD():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PBC_AttackInit')
        AttackLevel_(5)
        AttackP1(90)
        AirPushbackY(-30000)
        Unknown9310(1)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23078(1)
        callSubroutine('PBC_CheckWarp')
        Unknown2053(1)
        Unknown2015(180)
    sprite('iz206_00', 2)	# 1-2
    Unknown2006()
    Unknown1084(1)
    physicsXImpulse(17000)
    Unknown1028(-500)
    sprite('iz206_01', 2)	# 3-4
    sprite('iz206_02', 2)	# 5-6
    sprite('iz206_03', 2)	# 7-8
    sprite('iz206_04', 2)	# 9-10
    sprite('iz206_05', 2)	# 11-12
    SFX_3('slash_blade_middle')
    sprite('iz206_07', 3)	# 13-15	 **attackbox here**
    Unknown1084(1)
    GFX_0('Zanzoh5D', 100)
    sprite('iz206_08', 3)	# 16-18
    Unknown23027()
    sprite('iz206_09', 3)	# 19-21
    sprite('iz206_07', 3)	# 22-24	 **attackbox here**
    SFX_3('cloth_h')
    sprite('iz206_08', 3)	# 25-27
    sprite('iz206_09', 3)	# 28-30
    sprite('iz206_07', 3)	# 31-33	 **attackbox here**
    sprite('iz206_08', 3)	# 34-36
    sprite('iz206_09', 3)	# 37-39
    sprite('iz206_07', 4)	# 40-43	 **attackbox here**
    sprite('iz206_08', 4)	# 44-47
    sprite('iz206_09', 4)	# 48-51
    label(580)
    sprite('keep', 32767)	# 52-32818
    enterState('PersonaDeleteAndIdling')

@State
def PBC_Persona_6Assist():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000040420f000000000000000000')
        callSubroutine('PBC_AttackInit')
        AttackLevel_(4)
        Damage(1100)
        AttackP1(70)
        Unknown11092(1)
        Unknown9154(25)
        AirUntechableTime(40)
        AirPushbackX(12000)
        AirPushbackY(15000)
        Hitstop(8)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11042(1)
        Unknown11031(5)
        Unknown11091(5)
        Unknown23027()
        Unknown23078(1)
        callSubroutine('PBC_CheckWarp')
        Unknown2053(1)
        Unknown2015(180)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 250000):
                    sendToLabel(0)

        def upon_77():
            SLOT_51 = 1

        def upon_14():
            Unknown21015('436d6e4163744368616e6765506172746e657241737369737441746b5f410000c900000000000000')
    sprite('iz205_00', 2)	# 1-2
    sprite('iz205_01', 2)	# 3-4
    sprite('iz205_02', 2)	# 5-6
    Unknown2053(1)
    Unknown4007(0)
    sprite('iz205_03', 9)	# 7-15
    ScreenShake(20000, 0)
    sprite('iz205_04', 2)	# 16-17
    sprite('iz205_05', 2)	# 18-19
    physicsXImpulse(50000)
    sprite('iz205_06', 3)	# 20-22
    physicsXImpulse(64000)
    SFX_3('slash_blade_slow')
    sprite('iz205_07', 3)	# 23-25	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    StartMultihit()
    sprite('iz205_08', 3)	# 26-28	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    Unknown1019(80)
    Unknown2037(1)
    sprite('iz205_08', 3)	# 29-31	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    Unknown1019(80)
    sprite('iz205_07', 3)	# 32-34	 **attackbox here**
    GFX_1('izef_groundzan_04', 0)
    Unknown1019(80)
    label(0)
    sprite('keep', 4)	# 35-38
    clearUponHandler(3)
    Unknown1019(50)
    RefreshMultihit()
    sprite('iz205_10', 3)	# 39-41	 **attackbox here**
    clearUponHandler(3)
    GFX_0('TsukiZanzoh5D', 100)
    Unknown38(4, 1)
    RefreshMultihit()
    AirPushbackY(35000)
    YImpluseBeforeWallbounce(2500)
    Unknown1019(50)
    if SLOT_51:
        _gotolabel(1)
    sprite('iz205_11', 3)	# 42-44
    Unknown1019(50)
    Unknown23027()
    sprite('iz205_12', 3)	# 45-47
    Unknown1019(50)
    sprite('iz205_10', 3)	# 48-50	 **attackbox here**
    Unknown1019(0)
    sprite('iz205_11', 3)	# 51-53
    sprite('iz205_12', 3)	# 54-56
    sprite('iz205_10', 4)	# 57-60	 **attackbox here**
    sprite('iz205_11', 4)	# 61-64
    sprite('iz205_12', 4)	# 65-68
    loopRest()
    gotoLabel(580)
    label(1)
    sprite('iz206_00', 3)	# 69-71
    Unknown23027()
    Unknown1084(1)
    physicsXImpulse(17000)
    Unknown13(4)
    sprite('iz206_01', 3)	# 72-74
    Unknown1019(90)
    sprite('iz206_02', 3)	# 75-77
    Unknown1019(90)
    sprite('iz206_03', 3)	# 78-80
    Unknown1019(90)
    sprite('iz206_04', 3)	# 81-83
    Unknown1019(90)
    sprite('iz206_05', 3)	# 84-86
    Unknown1019(90)
    SFX_3('slash_blade_middle')
    sprite('iz206_07', 3)	# 87-89	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GroundedHitstunAnimation(1)
    AirPushbackY(-30000)
    Unknown9310(1)
    Hitstop(12)
    Unknown9016(1)
    GFX_0('Zanzoh5D', 100)
    sprite('iz206_08', 3)	# 90-92
    Unknown23027()
    sprite('iz206_09', 3)	# 93-95
    sprite('iz206_07', 3)	# 96-98	 **attackbox here**
    SFX_3('cloth_h')
    sprite('iz206_08', 3)	# 99-101
    sprite('iz206_09', 3)	# 102-104
    sprite('iz206_07', 3)	# 105-107	 **attackbox here**
    sprite('iz206_08', 3)	# 108-110
    sprite('iz206_09', 3)	# 111-113
    sprite('iz206_07', 4)	# 114-117	 **attackbox here**
    sprite('iz206_08', 4)	# 118-121
    sprite('iz206_09', 4)	# 122-125
    sprite('iz206_07', 4)	# 126-129	 **attackbox here**
    sprite('iz206_08', 4)	# 130-133
    sprite('iz206_09', 4)	# 134-137
    label(580)
    sprite('keep', 32767)	# 138-32904
    Unknown21015('436d6e4163744368616e6765506172746e657241737369737441746b5f410000c900000000000000')
    enterState('PersonaDeleteAndIdling')

@State
def PBC_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000040420f000000000000000000')
        callSubroutine('PBC_AttackInit')
        AttackLevel_(3)
        Damage(1700)
        AttackP1(90)
        AirPushbackX(15000)
        AirPushbackY(10000)
        Unknown9016(1)
        AirUntechableTime(23)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23078(1)
        callSubroutine('PBC_CheckWarp')
        Unknown2053(1)
    sprite('iz204_00', 3)	# 1-3
    Unknown2006()
    sprite('iz204_01', 1)	# 4-4
    Unknown4007(0)
    physicsXImpulse(80000)
    sprite('iz204_01', 1)	# 5-5
    Unknown1019(80)
    sprite('iz204_01', 1)	# 6-6
    Unknown1019(80)
    sprite('iz204_02', 1)	# 7-7
    Unknown1019(80)
    sprite('iz204_02', 1)	# 8-8
    Unknown1019(80)
    sprite('iz204_04', 1)	# 9-9	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_0('Zanzoh5C', 100)
    SFX_3('slash_blade_fast')
    sprite('iz204_04', 2)	# 10-11	 **attackbox here**
    Unknown23022(0)
    sprite('iz204_05', 3)	# 12-14
    Unknown23027()
    sprite('iz204_06', 3)	# 15-17
    sprite('iz204_04', 4)	# 18-21	 **attackbox here**
    SFX_3('cloth_l')
    sprite('iz204_05', 4)	# 22-25
    sprite('iz204_06', 4)	# 26-29
    sprite('iz204_04', 5)	# 30-34	 **attackbox here**
    sprite('iz204_05', 5)	# 35-39
    sprite('iz204_06', 5)	# 40-44
    label(580)
    sprite('keep', 32767)	# 45-32811
    enterState('PersonaDeleteAndIdling')

@State
def PBC_Persona2C():

    def upon_IMMEDIATE():
        callSubroutine('PBC_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(13)
        AirPushbackX(32000)
        AirPushbackY(20000)
        Unknown9016(1)
        AirUntechableTime(28)
        PushbackX(19800)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown2017(1)
        Unknown2053(1)
        Unknown23078(1)
        callSubroutine('PBC_CheckWarp')
    sprite('iz232_00', 4)	# 1-4
    Unknown2006()
    sprite('iz232_01', 4)	# 5-8
    sprite('iz232_02', 1)	# 9-9
    physicsXImpulse(60000)
    sprite('iz232_03', 1)	# 10-10
    sprite('iz232_05', 2)	# 11-12	 **attackbox here**
    SFX_3('slash_blade_fast')
    GFX_0('Zanzoh2C', 100)
    RefreshMultihit()
    physicsXImpulse(0)
    sprite('iz232_06', 4)	# 13-16
    Unknown23027()
    sprite('iz232_05', 4)	# 17-20	 **attackbox here**
    sprite('iz232_06', 4)	# 21-24
    SFX_3('cloth_l')
    sprite('iz232_05', 4)	# 25-28	 **attackbox here**
    sprite('iz232_06', 5)	# 29-33
    sprite('iz232_05', 5)	# 34-38	 **attackbox here**
    sprite('keep', 32767)	# 39-32805
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000040420f000000000000000000')
        callSubroutine('PBC_AttackInit')
        AttackLevel_(4)
        AirUntechableTime(23)
        AirPushbackX(10000)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('PBC_CheckWarp')
        Unknown4007(3)
        Unknown23078(1)

        def upon_43():
            if (SLOT_48 == 261):
                sendToLabel(580)
            if (SLOT_48 == 262):
                sendToLabel(580)
    sprite('iz254_00', 3)	# 1-3
    teleportRelativeX(100000)
    physicsYImpulse(0)
    sprite('iz254_00', 1)	# 4-4
    Unknown1019(70)
    YAccel(70)
    sprite('iz254_01', 2)	# 5-6
    Unknown1019(70)
    YAccel(70)
    sprite('iz254_03', 1)	# 7-7	 **attackbox here**
    GFX_0('ZanzohAir5C', 100)
    RefreshMultihit()
    Unknown1019(0)
    YAccel(0)
    SFX_3('slash_blade_fast')
    sprite('iz254_03', 1)	# 8-8	 **attackbox here**
    Unknown23022(0)
    sprite('iz254_04', 3)	# 9-11
    Unknown4007(0)
    Unknown1019(70)
    YAccel(70)
    sprite('iz254_05', 3)	# 12-14
    Unknown1019(80)
    YAccel(80)
    sprite('iz254_05', 3)	# 15-17
    Unknown1019(80)
    YAccel(80)
    sprite('iz254_05', 3)	# 18-20
    Unknown1019(0)
    YAccel(0)
    sprite('iz254_05', 20)	# 21-40
    label(580)
    sprite('keep', 32767)	# 41-32807
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaJD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000000000020a1070000000000000000000000000000000000')
        callSubroutine('PBC_AttackInit')
        AttackLevel_(4)
        Damage(1100)
        AttackP1(70)
        Unknown11092(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(-40000)
        AirUntechableTime(40)
        Unknown9310(1)
        Hitstop(8)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11042(1)
        Unknown11031(5)
        Unknown11091(5)
        callSubroutine('PBC_CheckWarp')
        Unknown4007(3)
        Unknown23078(1)
        Unknown4007(0)
        Unknown2053(1)
        sendToLabelUpon(2, 1)
    sprite('iz255_04', 3)	# 1-3
    sprite('iz255_05', 3)	# 4-6
    SFX_0('airdash_m')
    SFX_0('slash_blade_slow')
    sprite('iz255_06', 3)	# 7-9	 **attackbox here**
    Unknown3029(1)
    physicsYImpulse(-75000)
    physicsXImpulse(33750)
    RefreshMultihit()
    sprite('iz255_07', 3)	# 10-12	 **attackbox here**
    label(0)
    sprite('iz255_06', 3)	# 13-15	 **attackbox here**
    sprite('iz255_07', 3)	# 16-18	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz255_08', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(3000)
    AirPushbackY(36000)
    Unknown9310(-1)
    Unknown9016(1)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown1084(1)
    Unknown8004(100, 1, 1)
    ScreenShake(0, 10000)
    sprite('iz255_09', 3)	# 22-24
    Unknown2001()
    sprite('iz255_10', 4)	# 25-28
    sprite('iz255_11', 4)	# 29-32
    sprite('iz255_12', 4)	# 33-36
    sprite('iz255_10', 4)	# 37-40
    SFX_0('cloth_m')
    sprite('iz255_11', 4)	# 41-44
    sprite('iz255_12', 4)	# 45-48
    sprite('iz255_10', 4)	# 49-52
    sprite('iz255_11', 4)	# 53-56
    sprite('iz255_12', 4)	# 57-60
    label(580)
    sprite('keep', 32767)	# 61-32827
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaCrushAttack():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PBC_AttackInit')
        AttackLevel_(5)
        Damage(800)
        AirUntechableTime(23)
        AirPushbackX(10000)
        AirPushbackY(20000)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('PBC_CheckWarp')
        Unknown4007(3)
        Unknown23078(1)
        Unknown23022(1)
        Unknown2003(1)
    sprite('iz254_00', 3)	# 1-3
    Unknown2006()
    physicsXImpulse(45000)
    physicsYImpulse(0)
    sprite('iz254_00', 1)	# 4-4
    Unknown1019(70)
    YAccel(70)
    sprite('iz254_01', 2)	# 5-6
    Unknown1019(70)
    YAccel(70)
    sprite('iz254_03ex', 1)	# 7-7	 **attackbox here**
    Unknown4007(0)
    GFX_0('ZanzohAir5C', 100)
    RefreshMultihit()
    Unknown1019(0)
    YAccel(0)
    SFX_3('slash_blade_fast')
    sprite('iz254_03', 1)	# 8-8	 **attackbox here**
    sprite('iz254_04', 3)	# 9-11
    Unknown1019(70)
    YAccel(70)
    sprite('iz254_05', 3)	# 12-14
    Unknown1019(80)
    YAccel(80)
    sprite('iz254_05', 3)	# 15-17
    Unknown1019(80)
    YAccel(80)
    sprite('iz254_05', 3)	# 18-20
    Unknown1019(0)
    YAccel(0)
    sprite('iz254_05', 20)	# 21-40
    label(580)
    sprite('keep', 32767)	# 41-32807
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaLowAssaultA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PBC_SPAttackInit')
        Unknown2003(1)
        Unknown23022(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown2017(0)
        SLOT_59 = 0
        callSubroutine('PBC_ForceWarp')
        Unknown4007(3)

        def upon_44():
            Unknown4007(0)
            sendToLabel(580)
    sprite('iz402_00', 4)	# 1-4
    sprite('iz402_01', 4)	# 5-8
    sprite('iz402_02', 2)	# 9-10	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    GFX_0('MidAssault_thunderC', 0)
    RefreshMultihit()
    SFX_3('electric_m')
    sprite('iz402_03', 2)	# 11-12	 **attackbox here**
    sprite('iz402_02', 2)	# 13-14	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 2)	# 15-16	 **attackbox here**
    sprite('iz402_02', 2)	# 17-18	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_04', 5)	# 19-23
    sprite('iz402_05', 5)	# 24-28
    sprite('iz402_06', 5)	# 29-33
    sprite('iz402_07', 3)	# 34-36
    sprite('iz402_08', 3)	# 37-39
    sprite('iz402_09', 3)	# 40-42
    sprite('iz402_07', 3)	# 43-45
    sprite('iz402_08', 3)	# 46-48
    sprite('iz402_09', 3)	# 49-51
    label(580)
    sprite('keep', 32767)	# 52-32818
    enterState('PersonaDeleteAndIdling')

@State
def MidAssault_thunderC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('626365665f7375626572696b6f6d695f7468756e64657230302e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('izef_rushwind_05')
    sprite('null', 15)	# 1-15
    Unknown3004(-17)

@State
def PBC_PersonaLowAssaultB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PBC_SPAttackInit')
        Unknown2003(1)
        Unknown23022(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown2017(0)
        SLOT_59 = 0
        callSubroutine('PBC_ForceWarp')
        Unknown4007(3)

        def upon_44():
            Unknown4007(0)
            sendToLabel(580)
    sprite('iz402_00', 4)	# 1-4
    sprite('iz402_01', 4)	# 5-8
    sprite('iz402_02', 3)	# 9-11	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    GFX_0('MidAssault_thunderC', 0)
    SFX_3('electric_m')
    sprite('iz402_03', 3)	# 12-14	 **attackbox here**
    sprite('iz402_02', 3)	# 15-17	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 18-20	 **attackbox here**
    sprite('iz402_02', 3)	# 21-23	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 24-26	 **attackbox here**
    sprite('iz402_02', 3)	# 27-29	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 30-32	 **attackbox here**
    sprite('iz402_04', 7)	# 33-39
    sprite('iz402_05', 7)	# 40-46
    sprite('iz402_06', 7)	# 47-53
    sprite('iz402_07', 3)	# 54-56
    sprite('iz402_08', 3)	# 57-59
    sprite('iz402_09', 3)	# 60-62
    sprite('iz402_07', 3)	# 63-65
    sprite('iz402_08', 3)	# 66-68
    sprite('iz402_09', 3)	# 69-71
    label(580)
    sprite('keep', 32767)	# 72-32838
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaLowAssault_Ex():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PBC_SPAttackInit')
        Unknown2003(1)
        Unknown23022(1)
        Unknown4007(3)
        Unknown4009(3)
        Unknown2017(0)
        SLOT_59 = 0
        callSubroutine('PBC_ForceWarp')
        Unknown4007(3)

        def upon_44():
            Unknown4007(0)
            sendToLabel(580)
    sprite('iz402_00', 2)	# 1-2
    sprite('iz402_01', 3)	# 3-5
    sprite('iz402_02', 3)	# 6-8	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    GFX_0('MidAssault_thunderC', 0)
    SFX_3('electric_m')
    sprite('iz402_03', 3)	# 9-11	 **attackbox here**
    sprite('iz402_02', 3)	# 12-14	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 15-17	 **attackbox here**
    sprite('iz402_02', 3)	# 18-20	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 21-23	 **attackbox here**
    sprite('iz402_02', 3)	# 24-26	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 27-29	 **attackbox here**
    sprite('iz402_02', 3)	# 30-32	 **attackbox here**
    GFX_1('izef_rushthunder_00', 0)
    sprite('iz402_03', 3)	# 33-35	 **attackbox here**
    sprite('iz402_04', 7)	# 36-42
    sprite('iz402_05', 7)	# 43-49
    sprite('iz402_06', 7)	# 50-56
    sprite('iz402_07', 3)	# 57-59
    sprite('iz402_08', 3)	# 60-62
    sprite('iz402_09', 3)	# 63-65
    sprite('iz402_07', 3)	# 66-68
    sprite('iz402_08', 3)	# 69-71
    sprite('iz402_09', 3)	# 72-74
    label(580)
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaShotA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000206cfbff40420f00c0bdf0ff40420f00')
        callSubroutine('PBC_SPAttackInit')
        callSubroutine('PBC_CheckWarp')
    sprite('iz403_00', 3)	# 1-3
    Unknown2006()
    sprite('iz403_01', 3)	# 4-6
    GFX_0('ElectricBall_First', 0)
    SFX_3('electric_m')
    sprite('iz403_02', 3)	# 7-9
    GFX_0('ElectricBall_Throw', 0)
    SFX_3('electric_m')
    sprite('iz403_04', 1)	# 10-10
    GFX_0('ElectricBall_HontaiA', 0)
    sprite('iz403_04', 4)	# 11-14
    Unknown23022(0)
    sprite('iz403_05', 3)	# 15-17
    sprite('iz403_06', 3)	# 18-20
    sprite('iz403_04', 4)	# 21-24
    SFX_3('cloth_h')
    sprite('iz403_05', 4)	# 25-28
    sprite('iz403_06', 4)	# 29-32
    sprite('iz403_04', 4)	# 33-36
    sprite('iz403_05', 4)	# 37-40
    sprite('iz403_06', 4)	# 41-44
    sprite('iz403_04', 5)	# 45-49
    sprite('iz403_05', 5)	# 50-54
    sprite('iz403_06', 5)	# 55-59
    sprite('iz403_04', 5)	# 60-64
    sprite('iz403_05', 5)	# 65-69
    sprite('iz403_06', 5)	# 70-74
    label(580)
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaShotB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000206cfbff40420f00c0bdf0ff40420f00')
        callSubroutine('PBC_SPAttackInit')
        callSubroutine('PBC_CheckWarp')
    sprite('iz403_00', 3)	# 1-3
    Unknown2006()
    sprite('iz403_01', 3)	# 4-6
    GFX_0('ElectricBall_First', 0)
    SFX_3('electric_m')
    sprite('iz403_02', 3)	# 7-9
    GFX_0('ElectricBall_Throw', 0)
    SFX_3('electric_m')
    sprite('iz403_04', 1)	# 10-10
    GFX_0('ElectricBall_HontaiB', 0)
    sprite('iz403_04', 4)	# 11-14
    Unknown23022(0)
    sprite('iz403_05', 3)	# 15-17
    sprite('iz403_06', 3)	# 18-20
    sprite('iz403_04', 4)	# 21-24
    SFX_3('cloth_h')
    sprite('iz403_05', 4)	# 25-28
    sprite('iz403_06', 4)	# 29-32
    sprite('iz403_04', 4)	# 33-36
    sprite('iz403_05', 4)	# 37-40
    sprite('iz403_06', 4)	# 41-44
    sprite('iz403_04', 5)	# 45-49
    sprite('iz403_05', 5)	# 50-54
    sprite('iz403_06', 5)	# 55-59
    sprite('iz403_04', 5)	# 60-64
    sprite('iz403_05', 5)	# 65-69
    sprite('iz403_06', 5)	# 70-74
    label(580)
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaShot_Ex():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000206cfbff40420f00c0bdf0ff40420f00')
        callSubroutine('PBC_SPAttackInit')
        callSubroutine('PBC_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('iz403_00', 3)	# 1-3
    Unknown2006()
    label(0)
    sprite('iz403_01', 2)	# 4-5
    GFX_0('ElectricBall_First', 0)
    SFX_3('electric_m')
    sprite('iz403_01', 1)	# 6-6
    GFX_0('ElectricBall_First', 0)
    SFX_3('electric_m')

    def upon_3():
        if (not CheckInput(0x13)):
            sendToLabel(1)
        SLOT_51 = (SLOT_51 + 1)
        if (SLOT_51 >= 90):
            sendToLabel(1)
    sprite('iz403_01', 3)	# 7-9
    GFX_0('ElectricBall_First', 0)
    SFX_3('electric_m')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('iz403_02', 3)	# 10-12
    GFX_0('ElectricBall_Throw', 0)
    clearUponHandler(3)
    sprite('iz403_04', 1)	# 13-13
    GFX_0('ElectricBall_HontaiEx', 0)
    SFX_3('electric_s')
    sprite('iz403_04', 4)	# 14-17
    SFX_3('cloth_h')
    sprite('iz403_05', 4)	# 18-21
    sprite('iz403_06', 4)	# 22-25
    sprite('iz403_04', 4)	# 26-29
    sprite('iz403_05', 4)	# 30-33
    sprite('iz403_06', 4)	# 34-37
    SLOT_10 = 0
    sprite('iz403_04', 5)	# 38-42
    sprite('iz403_05', 5)	# 43-47
    sprite('iz403_06', 5)	# 48-52
    sprite('iz403_04', 5)	# 53-57
    sprite('iz403_05', 5)	# 58-62
    sprite('iz403_06', 5)	# 63-67
    sprite('keep', 32767)	# 68-32834
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaShot_A4th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a086010000000000206cfbff40420f00c0bdf0ff40420f00')
        callSubroutine('PBC_SPAttackInit')
        callSubroutine('PBC_CheckWarp')
    sprite('iz403_00', 2)	# 1-2
    Unknown2006()
    sprite('iz403_01', 2)	# 3-4
    GFX_0('ElectricBall_First', 0)
    SFX_3('electric_m')
    sprite('iz403_02', 3)	# 5-7
    GFX_0('ElectricBall_Throw', 0)
    SFX_3('electric_m')
    sprite('iz403_04', 2)	# 8-9
    GFX_0('ElectricBall_HontaiA4th', 0)
    sprite('iz403_04', 4)	# 10-13
    Unknown23022(0)
    sprite('iz403_05', 3)	# 14-16
    sprite('iz403_06', 3)	# 17-19
    sprite('iz403_04', 4)	# 20-23
    SFX_3('cloth_h')
    sprite('iz403_05', 4)	# 24-27
    sprite('iz403_06', 4)	# 28-31
    sprite('iz403_04', 4)	# 32-35
    sprite('iz403_05', 4)	# 36-39
    sprite('iz403_06', 4)	# 40-43
    label(580)
    sprite('keep', 32767)	# 44-32810
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateLaser():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000400d03000000000000000000000000000000000000000000')
        callSubroutine('PBC_DDAttackInit')
        AttackLevel_(4)
        Damage(270)
        AttackP2(98)
        Unknown11091(15)
        Hitstop(0)
        Unknown11034(0)
        Unknown11033(1)
        PushbackX(11000)
        AirPushbackY(1000)
        AirPushbackX(100000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9362(1)
        Unknown9364(30)
        AirHitstunAfterWallbounce(30)
        WallbounceReboundTime(1)
        AirUntechableTime(62)
        Unknown9266(4)
        Unknown9021(1)
        Unknown11057(800)
        Unknown2053(1)
        callSubroutine('PBC_ForceWarp')
        Unknown4007(3)
        Unknown23066(1)
        Unknown2053(1)

        def upon_ON_HIT_OR_BLOCK():
            SLOT_51 = 1
            if SLOT_51:
                SLOT_51 = 0
            else:
                SLOT_51 = 1
        Unknown23022(1)
        Unknown2054(1)
        Unknown30056('d00101006400000000000000')
    sprite('iz431_00', 4)	# 1-4
    GFX_0('CreateUltimateLaserMatome', 0)
    Unknown4007(0)
    sprite('iz431_01', 4)	# 5-8
    GFX_1('izef_jiodinetame_06', 0)
    sprite('iz431_02', 4)	# 9-12
    sprite('iz431_03', 3)	# 13-15
    SFX_3('bc000')
    sprite('iz431_04', 3)	# 16-18
    sprite('iz431_05', 3)	# 19-21
    sprite('iz431_03', 3)	# 22-24
    SFX_3('bc000')
    sprite('iz431_04', 3)	# 25-27
    sprite('iz431_05', 3)	# 28-30
    sprite('iz431_03', 3)	# 31-33
    SFX_3('bc000')
    sprite('iz431_04', 3)	# 34-36
    sprite('iz431_06', 3)	# 37-39
    sprite('iz431_07', 3)	# 40-42
    sprite('iz431_08', 3)	# 43-45	 **attackbox here**
    GFX_0('UltimateLaserJizoku', 0)
    GFX_1('izef_giodineshock_01', 0)
    RefreshMultihit()
    Unknown23024(1)
    Unknown2054(0)
    sprite('iz431_09', 3)	# 46-48	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 52-54	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 61-63	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 64-66	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 67-69	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 70-72	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 73-75	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 76-78	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 79-81	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 82-84	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 85-87	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 88-90	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 91-93	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 94-96	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 97-99	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 100-102	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 103-105	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 106-108	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 109-111	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 112-114	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 115-117	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 118-120	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 121-123	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 124-126	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 127-129	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 130-132	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 133-135	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09', 3)	# 136-138	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10', 3)	# 139-141	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 3)	# 142-144	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 4)	# 145-148	 **attackbox here**
    Unknown2001()
    sprite('iz431_09', 4)	# 149-152	 **attackbox here**
    sprite('iz431_10', 4)	# 153-156	 **attackbox here**
    sprite('iz431_08', 5)	# 157-161	 **attackbox here**
    sprite('iz431_09', 5)	# 162-166	 **attackbox here**
    sprite('iz431_10', 5)	# 167-171	 **attackbox here**
    label(580)
    sprite('keep', 32767)	# 172-32938
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateLaserOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000400d03000000000000000000000000000000000000000000')
        callSubroutine('PBC_DDAttackInit')
        Unknown11034(0)
        Unknown11033(1)
        AttackLevel_(4)
        Damage(330)
        AttackP2(98)
        Unknown11091(15)
        Hitstop(0)
        PushbackX(11000)
        AirPushbackY(1000)
        AirPushbackX(100000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9362(1)
        Unknown9364(30)
        AirHitstunAfterWallbounce(30)
        WallbounceReboundTime(1)
        AirUntechableTime(47)
        Unknown9266(4)
        Unknown9021(1)
        Unknown11057(800)
        Unknown2053(1)
        Unknown2054(1)
        callSubroutine('PBC_ForceWarp')
        Unknown4007(3)
        Unknown23022(1)
        Unknown30056('d00101006400000000000000')
    sprite('iz431_00', 4)	# 1-4
    GFX_0('CreateUltimateLaserMatome', 0)
    Unknown23029(1, 911, 0)
    Unknown4007(0)
    sprite('iz431_01', 4)	# 5-8
    GFX_1('izef_jiodinetame_06', 0)
    sprite('iz431_02', 4)	# 9-12
    sprite('iz431_03', 3)	# 13-15
    SFX_3('bc000')
    sprite('iz431_04', 3)	# 16-18
    sprite('iz431_05', 3)	# 19-21
    sprite('iz431_03', 3)	# 22-24
    SFX_3('bc000')
    sprite('iz431_04', 3)	# 25-27
    sprite('iz431_05', 3)	# 28-30
    sprite('iz431_03', 3)	# 31-33
    SFX_3('bc000')
    sprite('iz431_04', 3)	# 34-36
    SFX_3('bc000')
    sprite('iz431_06', 3)	# 37-39
    sprite('iz431_07', 3)	# 40-42
    sprite('iz431_08ex', 3)	# 43-45	 **attackbox here**
    GFX_0('UltimateLaserJizoku', 0)
    Unknown23029(1, 911, 0)
    GFX_1('izef_giodineshock_01', 0)
    RefreshMultihit()
    Unknown23024(1)
    Unknown2054(0)
    sprite('iz431_09ex', 3)	# 46-48	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 52-54	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 61-63	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 64-66	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 67-69	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 70-72	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 73-75	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 76-78	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 79-81	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 82-84	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 85-87	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 88-90	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 91-93	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 94-96	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 97-99	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 100-102	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 103-105	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 106-108	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 109-111	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 112-114	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 115-117	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 118-120	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 121-123	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 124-126	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 127-129	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 130-132	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 133-135	 **attackbox here**
    SFX_3('bc001')
    RefreshMultihit()
    sprite('iz431_09ex', 3)	# 136-138	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_10ex', 3)	# 139-141	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08ex', 3)	# 142-144	 **attackbox here**
    RefreshMultihit()
    sprite('iz431_08', 4)	# 145-148	 **attackbox here**
    Unknown2001()
    sprite('iz431_09', 4)	# 149-152	 **attackbox here**
    sprite('iz431_10', 4)	# 153-156	 **attackbox here**
    sprite('iz431_08', 5)	# 157-161	 **attackbox here**
    sprite('iz431_09', 5)	# 162-166	 **attackbox here**
    sprite('iz431_10', 5)	# 167-171	 **attackbox here**
    label(580)
    sprite('keep', 32767)	# 172-32938
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateBlade():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('160000006400000000000000804f120000000000000000000000000000000000')
        callSubroutine('PBC_DDAttackInit')
        Unknown4061(1)
        Unknown3032()
        Unknown3001(0)
        AttackLevel_(5)
        Damage(4000)
        Unknown11091(25)
        AttackP1(80)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9016(1)
        Unknown9266(4)
        PushbackX(6000)
        AttackP2(60)
        Unknown9156(21)
        Unknown9130(20)
        Unknown9142(300)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown9156(21)
        Unknown9132(20)
        Unknown9144(300)
        SLOT_58 = 1
        Unknown3001(0)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown4009(3)
        Unknown23066(1)
        Unknown23078(0)
        Unknown23022(1)
        sendToLabelUpon(2, 0)

        def upon_43():
            if (SLOT_48 == 9999):
                sendToLabel(580)
    sprite('iz430_00', 10)	# 1-10
    Unknown3029(1)
    Unknown20000(1)
    Unknown20009(1300)
    sprite('iz430_00', 20)	# 11-30
    GFX_0('Cardrotate00', 0)
    sprite('iz430_01', 2)	# 31-32
    Unknown3004(65)
    SFX_0('persona_destroy')
    sprite('iz430_02', 2)	# 33-34
    sprite('iz430_03', 2)	# 35-36
    sprite('iz430_04', 2)	# 37-38
    sprite('iz430_02', 2)	# 39-40
    sprite('iz430_03', 2)	# 41-42
    sprite('iz430_04', 2)	# 43-44
    sprite('iz430_02', 2)	# 45-46
    sprite('iz430_03', 2)	# 47-48
    sprite('iz430_04', 2)	# 49-50
    sprite('iz430_05', 4)	# 51-54
    Unknown20001(1)
    physicsYImpulse(-5000)
    sprite('iz430_06', 4)	# 55-58
    sprite('iz430_07', 32767)	# 59-32825
    physicsYImpulse(-200000)
    GFX_0('jumonjiBigslashTate', 104)
    label(0)
    sprite('iz430_08', 2)	# 32826-32827
    Unknown1084(1)
    Unknown3029(0)
    Unknown20009(1000)
    ScreenShake(20000, 0)
    SFX_3('bc002')
    sprite('iz430_09', 3)	# 32828-32830	 **attackbox here**
    GFX_0('jumonjiBigslashSock00', 1)
    RefreshMultihit()
    Unknown36(3)
    Unknown13024(1)
    Unknown35()
    sprite('iz430_10', 5)	# 32831-32835	 **attackbox here**
    GFX_0('jumonjiBigslashSock01', 100)
    Unknown20001(0)
    SFX_3('thunder_l')
    sprite('iz430_11', 5)	# 32836-32840
    sprite('iz430_12', 5)	# 32841-32845
    sprite('iz430_13', 5)	# 32846-32850
    sprite('iz430_14', 5)	# 32851-32855
    sprite('iz430_15', 50)	# 32856-32905
    Unknown20000(0)
    label(580)
    sprite('keep', 32767)	# 32906-65672
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateBladeTAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('160000006400000000000000804f120000000000000000000000000000000000')
        callSubroutine('PBC_DDAttackInit')
        Unknown4061(1)
        Unknown3032()
        Unknown3001(0)
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9016(1)
        Unknown9266(4)
        PushbackX(6000)
        Unknown9130(20)
        Unknown9142(300)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown9156(21)
        Unknown9132(20)
        Unknown9144(300)
        SLOT_58 = 1
        Unknown3001(0)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        Unknown4009(3)
        Unknown23066(1)
        Unknown23078(0)
        Unknown23022(1)
        sendToLabelUpon(2, 0)
    sprite('iz430_00', 10)	# 1-10
    Unknown3029(1)
    Unknown20000(1)
    Unknown20009(1300)
    sprite('iz430_00', 20)	# 11-30
    GFX_0('Cardrotate00', 0)
    sprite('iz430_01', 2)	# 31-32
    Unknown3004(65)
    SFX_0('persona_destroy')
    sprite('iz430_02', 2)	# 33-34
    sprite('iz430_03', 2)	# 35-36
    sprite('iz430_04', 2)	# 37-38
    sprite('iz430_02', 2)	# 39-40
    sprite('iz430_03', 2)	# 41-42
    sprite('iz430_04', 2)	# 43-44
    sprite('iz430_02', 2)	# 45-46
    sprite('iz430_03', 2)	# 47-48
    sprite('iz430_04', 2)	# 49-50
    sprite('iz430_05', 4)	# 51-54
    Unknown20001(1)
    physicsYImpulse(-5000)
    sprite('iz430_06', 4)	# 55-58
    sprite('iz430_07', 32767)	# 59-32825
    physicsYImpulse(-200000)
    GFX_0('jumonjiBigslashTate', 104)
    label(0)
    sprite('iz430_08', 2)	# 32826-32827
    Unknown1084(1)
    Unknown3029(0)
    Unknown20009(1000)
    ScreenShake(20000, 0)
    SFX_3('bc002')
    sprite('iz430_09', 3)	# 32828-32830	 **attackbox here**
    GFX_0('jumonjiBigslashSock00', 1)
    RefreshMultihit()
    Unknown36(3)
    Unknown13024(1)
    Unknown35()
    sprite('iz430_10', 5)	# 32831-32835	 **attackbox here**
    GFX_0('jumonjiBigslashSock01', 100)
    Unknown20001(0)
    SFX_3('thunder_l')
    sprite('iz430_11', 5)	# 32836-32840
    sprite('iz430_12', 5)	# 32841-32845
    sprite('iz430_13', 5)	# 32846-32850
    sprite('iz430_14', 5)	# 32851-32855
    sprite('iz430_15', 50)	# 32856-32905
    Unknown20000(0)
    label(580)
    sprite('keep', 32767)	# 32906-65672
    enterState('PersonaDeleteAndIdling')

@State
def Cardrotate00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f636172646272616b6530302e44494700000000626365665f6a756d6f6e6a695f636172646272616b6530305f3030302e6d6d00')
        Unknown23015(1)
        Unknown1096(2000)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown3001(0)
    GFX_0('Cardrotate01', 100)

@State
def Cardrotate01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f636172646272616b6530312e44494700000000626365665f6a756d6f6e6a695f636172646272616b6530315f3030302e6d6d00')
        Unknown23015(1)
        Unknown1096(2000)
    sprite('null', 8)	# 1-8
    Unknown23117(-16731137, 8)
    sprite('null', 1)	# 9-9
    GFX_1('izef_cardcrash_03', 100)

@State
def PBC_PersonaUltimateBladeOD():

    def upon_IMMEDIATE():
        Unknown23184('1600000064000000702ffcff0000000000000000000000000000000000000000')
        callSubroutine('PBC_DDAttackInit')
        Unknown3032()
        Unknown3001(0)
        AttackLevel_(5)
        Damage(230)
        Unknown11091(25)
        AttackP2(100)
        Hitstop(2)
        AirPushbackX(3000)
        AirPushbackY(100000)
        YImpluseBeforeWallbounce(2500)
        PushbackX(6000)
        AirUntechableTime(180)
        Unknown9310(1)
        Unknown9190(1)
        Unknown9118(10)
        GroundedHitstunAnimation(1)
        Unknown9016(1)
        Unknown9266(4)
        Unknown11068(1)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        callSubroutine('PBC_ForceWarp')
        Unknown4009(3)
        Unknown23078(0)
        Unknown23022(1)
        Unknown20000(1)
    sprite('iz433_00', 9)	# 1-9
    Unknown1086(22)
    teleportRelativeX(-250000)
    Unknown3004(8)
    sprite('iz433_01', 40)	# 10-49
    sprite('iz433_01', 5)	# 50-54
    sprite('iz433_02', 3)	# 55-57
    GFX_0('WildFinishslash', 104)
    sprite('iz433_03', 2)	# 58-59
    sprite('iz433_04', 2)	# 60-61
    sprite('iz433_05', 1)	# 62-62	 **attackbox here**
    RefreshMultihit()
    SFX_3('thunder_l')
    SFX_3('blaze_long')
    SFX_3('bomb_l')
    SFX_1('bc326')
    sprite('iz433_05', 1)	# 63-63	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 64-64	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 65-65	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 66-66	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 67-67	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 68-68	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 4)	# 69-72	 **attackbox here**
    RefreshMultihit()
    SFX_3('counter_hit_l45')
    SFX_3('blaze_long')
    Damage(4000)
    AttackP2(60)
    Unknown36(3)
    Unknown13024(1)
    Unknown35()
    sprite('iz433_06', 6)	# 73-78
    sprite('iz433_07', 6)	# 79-84
    sprite('iz433_06', 6)	# 85-90
    sprite('iz433_07', 6)	# 91-96
    sprite('iz433_06', 6)	# 97-102
    sprite('iz433_07', 6)	# 103-108
    sprite('iz433_06', 6)	# 109-114
    sprite('iz433_07', 6)	# 115-120
    sprite('iz433_06', 6)	# 121-126
    sprite('iz433_07', 6)	# 127-132
    sprite('iz433_06', 6)	# 133-138
    sprite('iz433_07', 6)	# 139-144
    sprite('iz433_06', 6)	# 145-150
    sprite('iz433_07', 6)	# 151-156
    sprite('iz433_06', 6)	# 157-162
    sprite('iz433_07', 6)	# 163-168
    sprite('iz433_06', 6)	# 169-174
    sprite('iz433_07', 6)	# 175-180
    label(580)
    sprite('keep', 32767)	# 181-32947
    enterState('PersonaDeleteAndIdling')

@State
def PBC_PersonaUltimateBladeODTAG():

    def upon_IMMEDIATE():
        Unknown23184('1600000064000000702ffcff0000000000000000000000000000000000000000')
        callSubroutine('PBC_DDAttackInit')
        Unknown3032()
        Unknown3001(0)
        AttackLevel_(5)
        Damage(100)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(2)
        AirPushbackX(3000)
        AirPushbackY(100000)
        YImpluseBeforeWallbounce(2500)
        PushbackX(6000)
        AirUntechableTime(180)
        Unknown9310(1)
        Unknown9190(1)
        Unknown9118(10)
        GroundedHitstunAnimation(1)
        Unknown9016(1)
        Unknown9266(4)
        Unknown11068(1)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        callSubroutine('PBC_ForceWarp')
        Unknown4009(3)
        Unknown23078(0)
        Unknown23022(1)
        Unknown20000(1)
        Unknown30048(1)
    sprite('iz433_00', 9)	# 1-9
    Unknown1086(22)
    teleportRelativeX(-250000)
    Unknown3004(8)
    sprite('iz433_01', 40)	# 10-49
    sprite('iz433_01', 5)	# 50-54
    sprite('iz433_02', 3)	# 55-57
    GFX_0('WildFinishslash', 104)
    sprite('iz433_03', 2)	# 58-59
    sprite('iz433_04', 2)	# 60-61
    sprite('iz433_05', 1)	# 62-62	 **attackbox here**
    RefreshMultihit()
    SFX_3('thunder_l')
    SFX_3('blaze_long')
    SFX_3('bomb_l')
    SFX_1('bc326')
    sprite('iz433_05', 1)	# 63-63	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 64-64	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 65-65	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 66-66	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 67-67	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 1)	# 68-68	 **attackbox here**
    RefreshMultihit()
    sprite('iz433_05', 4)	# 69-72	 **attackbox here**
    RefreshMultihit()
    SFX_3('counter_hit_l45')
    SFX_3('blaze_long')

    def upon_12():
        pass
    Damage(800)
    Unknown36(3)
    Unknown13024(1)
    Unknown35()
    sprite('iz433_06', 6)	# 73-78
    sprite('iz433_07', 6)	# 79-84
    sprite('iz433_06', 6)	# 85-90
    sprite('iz433_07', 6)	# 91-96
    sprite('iz433_06', 6)	# 97-102
    sprite('iz433_07', 6)	# 103-108
    sprite('iz433_06', 6)	# 109-114
    sprite('iz433_07', 6)	# 115-120
    sprite('iz433_06', 6)	# 121-126
    sprite('iz433_07', 6)	# 127-132
    sprite('iz433_06', 6)	# 133-138
    sprite('iz433_07', 6)	# 139-144
    sprite('iz433_06', 6)	# 145-150
    sprite('iz433_07', 6)	# 151-156
    sprite('iz433_06', 6)	# 157-162
    sprite('iz433_07', 6)	# 163-168
    sprite('iz433_06', 6)	# 169-174
    sprite('iz433_07', 6)	# 175-180
    label(580)
    sprite('keep', 32767)	# 181-32947
    enterState('PersonaDeleteAndIdling')

@State
def Zanzoh_5A3rd_new():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown3001(240)
        Unknown3032()
        Unknown4061(0)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc208_00', 16)	# 1-16

@State
def Zanzoh_5A3rd_new():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown3001(240)
        Unknown3032()
        Unknown4061(0)
    sprite('vr_bc208_00', 30)	# 1-30
    sprite('vr_bc208_00', 16)	# 31-46

    def upon_3():
        Unknown4007(2)
        Unknown3005(-5)

@State
def Zanzoh_5A3rd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4009(2)
        Unknown4010(2)
        Unknown3001(240)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc202_00', 2)	# 1-2
    sprite('vr_bc202_01', 5)	# 3-7

@State
def Zanzoh_5B():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown4009(2)
        Unknown4010(2)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc203_00', 2)	# 1-2
    sprite('vr_bc203_01', 12)	# 3-14

@State
def Zanzoh_2B():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown4009(2)
        Unknown4010(2)
        Unknown2035(1)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc231_00', 3)	# 1-3
    sprite('vr_bc231_01', 2)	# 4-5
    sprite('vr_bc231_02', 60)	# 6-65

@State
def Zanzoh_Air5B():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(0)
        Unknown3001(200)
        Unknown4009(2)
        Unknown4010(2)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-2)
    sprite('vr_bc251_00', 3)	# 1-3
    Unknown2019(-100)
    sprite('vr_bc251_01', 3)	# 4-6
    sprite('vr_bc251_02', 60)	# 7-66
    Unknown2019(100)

@State
def Zanzoh_Air5B2nd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown4009(2)
        Unknown4010(2)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc252_00', 2)	# 1-2
    sprite('vr_bc252_01', 3)	# 3-5
    sprite('vr_bc252_02', 60)	# 6-65

@State
def Zanzoh5C():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown4009(2)
        teleportRelativeX(256000)
        Unknown3001(200)
        callSubroutine('PBC_EffectInit')

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_iz204_00', 20)	# 1-20

@State
def Zanzoh2C():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown2019(-100)
        Unknown4010(2)
        Unknown4007(2)
        Unknown3005(-25)
    sprite('vr_iz232_00', 30)	# 1-30

@State
def ZanzohAir5C():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        callSubroutine('PBC_EffectInit')
        Unknown4009(2)
        Unknown4010(2)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_iz254_00', 20)	# 1-20

@State
def Zanzoh5D():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        callSubroutine('PBC_EffectInit')
        Unknown4010(2)
        Unknown3001(200)
    sprite('vr_iz206_00', 30)	# 1-30
    Unknown3005(-20)

@State
def TsukiZanzoh5D():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(1)
        Unknown2019(-100)
        Unknown4007(2)
        Unknown4010(2)
    sprite('vr_iz205_00', 60)	# 1-60
    Unknown3005(-20)

@State
def Zanzoh_5AB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3001(200)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-20)
    sprite('vr_bc210_00', 40)	# 1-40

@State
def Zanzoh_2AB():

    def upon_IMMEDIATE():

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
        Unknown3032()
        Unknown4061(0)
        Unknown4009(2)
        Unknown4010(2)
    sprite('vr_bc211_00', 2)	# 1-2
    sprite('vr_bc211_01', 10)	# 3-12

@State
def ReversalNigiyakasi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('626365663430305f736c6173682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 23)	# 1-23

@State
def MidAssault():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(-45000)
    sprite('null', 60)	# 1-60
    GFX_2('bcef_midassault_01')

@State
def AirMidAssault():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown1072(-45000)
    sprite('null', 60)	# 1-60
    GFX_2('bcef_midassault_01')

@State
def MidAssault_thunderEX():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('626365665f7375626572696b6f6d695f7468756e64657230302e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('izef_rushwind_05')
    sprite('null', 30)	# 1-30
    Unknown3004(-9)

@State
def ElectricBall_First():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4010(2)
        Unknown1077(0, 360000)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3070(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(900)
    sprite('vr_iz403_00', 2)	# 1-2	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_01', 2)	# 3-4	 **attackbox here**
    sprite('vr_iz403_02', 2)	# 5-6	 **attackbox here**

@State
def ElectricBall_Throw():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown4010(2)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3070(1)
        Unknown3071(2)
        Unknown3076(1000)
        Unknown3077(900)
        Unknown26('ElectricBall_First')
    sprite('vr_iz403_03', 1)	# 1-1
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_03', 1)	# 2-2
    GFX_1('izef_enagyballthunder_04', 1)
    sprite('vr_iz403_03', 1)	# 3-3
    GFX_1('izef_enagyballthunder_04', 1)
    sprite('vr_iz403_04', 1)	# 4-4
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_04', 10)	# 5-14
    GFX_1('izef_enagyballthunder_04', 1)
    Unknown3004(-30)

@State
def ElectricBall_HontaiA():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1300)
        AirPushbackY(16000)
        AirUntechableTime(30)
        Unknown9266(4)
        Unknown9021(1)
        physicsXImpulse(40000)
        callSubroutine('PBC_EffectInit')

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown53(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        loopRelated(17, 75)

        def upon_17():
            Unknown23090(25)
        Unknown3033()
        Unknown4061(3)
    label(10)
    sprite('vr_iz403_05', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('vr_iz403_05', 1)	# 2-2	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_06', 1)	# 3-3	 **attackbox here**
    sprite('vr_iz403_07', 1)	# 4-4	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vr_iz403_08', 2)	# 5-6
    GFX_1('izef_enagyballthunder_04', 0)
    Unknown1084(1)
    sprite('vr_iz403_09', 2)	# 7-8
    sprite('vr_iz403_10', 2)	# 9-10
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_11', 2)	# 11-12

@State
def ElectricBall_HontaiB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        GroundedHitstunAnimation(1)
        AirPushbackY(16000)
        AirUntechableTime(30)
        Unknown9266(4)
        Unknown9021(1)
        Unknown53(1)
        physicsXImpulse(65000)
        callSubroutine('PBC_EffectInit')
        Unknown53(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 0)
        loopRelated(17, 75)

        def upon_17():
            Unknown23090(25)
        Unknown3033()
        Unknown4061(3)
    label(10)
    sprite('vr_iz403_05', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('vr_iz403_05', 1)	# 2-2	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_06', 1)	# 3-3	 **attackbox here**
    sprite('vr_iz403_07', 1)	# 4-4	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('vr_iz403_08', 2)	# 5-6
    GFX_1('izef_enagyballthunder_04', 0)
    Unknown1084(1)
    sprite('vr_iz403_09', 2)	# 7-8
    sprite('vr_iz403_10', 2)	# 9-10
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_11', 2)	# 11-12

@State
def ElectricBall_HontaiEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        GroundedHitstunAnimation(1)
        AirPushbackY(16000)
        AirUntechableTime(30)
        Unknown11092(1)
        Unknown9266(4)
        Unknown9021(1)
        Hitstop(5)
        Unknown11033(2)
        Unknown30065(0)
        Unknown11091(10)
        physicsXImpulse(60000)
        Unknown3033()
        Unknown4061(3)

        def upon_3():
            if SLOT_38:
                Unknown23045('69000000')
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045('69000000')
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown53(1)
        sendToLabelUpon(10, 10)
        sendToLabelUpon(44, 9)
        loopRelated(17, 75)
        sendToLabelUpon(17, 9)
    label(0)
    sprite('vr_iz403_05', 1)	# 1-1	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_06', 1)	# 2-2	 **attackbox here**
    sprite('vr_iz403_07', 1)	# 3-3	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('vr_iz403_08', 2)	# 4-5
    clearUponHandler(10)
    clearUponHandler(44)
    clearUponHandler(17)
    GFX_1('izef_enagyballthunder_04', 0)
    Unknown1084(1)
    sprite('vr_iz403_09', 2)	# 6-7
    sprite('vr_iz403_10', 2)	# 8-9
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_11', 2)	# 10-11
    loopRest()
    ExitState()
    label(10)
    sprite('vr_iz403_00', 2)	# 12-13	 **attackbox here**
    clearUponHandler(10)
    clearUponHandler(44)
    clearUponHandler(17)
    sendToLabelUpon(44, 19)
    StartMultihit()
    GFX_1('izef_enagyballthunder_04', 0)
    Unknown1096(3000)
    Unknown3038(1)
    Unknown2053(1)
    teleportRelativeX(50000)
    Unknown1084(1)
    physicsXImpulse(20000)
    Unknown1028(-1500)
    sprite('vr_iz403_01', 2)	# 14-15	 **attackbox here**
    GFX_0('ElectricBall_Ex_Add', 100)
    RefreshMultihit()
    Damage(400)
    Unknown9266(4)
    Unknown9021(1)
    Hitstop(3)
    sprite('vr_iz403_02', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    sprite('vr_iz403_01', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    GFX_0('ElectricBall_Ex_Add', 100)
    sprite('vr_iz403_02', 2)	# 20-21	 **attackbox here**
    GFX_0('ElectricBall_Ex_Add', 100)
    Unknown23027()
    sprite('vr_iz403_01', 2)	# 22-23	 **attackbox here**
    sprite('vr_iz403_02', 2)	# 24-25	 **attackbox here**
    label(19)
    sprite('vr_iz403_01', 2)	# 26-27	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    Unknown1084(1)
    sprite('vr_iz403_02', 2)	# 28-29	 **attackbox here**
    sprite('vr_iz403_01', 2)	# 30-31	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_02', 2)	# 32-33	 **attackbox here**
    sprite('vr_iz403_01', 2)	# 34-35	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_02', 2)	# 36-37	 **attackbox here**

@State
def ElectricBall_HontaiA4th():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(900)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown9266(4)
        Unknown9021(1)
        Hitstop(0)
        Unknown11001(5, 5, 5)
        Unknown23027()
        Unknown1096(3000)
        Unknown3038(1)
        Unknown2053(1)
    sprite('vr_iz403_00', 2)	# 1-2	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    teleportRelativeX(50000)
    physicsXImpulse(20000)
    Unknown1028(-1500)
    sprite('vr_iz403_01', 2)	# 3-4	 **attackbox here**
    Unknown26('ElectricBall_Throw')
    GFX_0('ElectricBall_Ex_Add', 100)
    RefreshMultihit()
    sprite('vr_iz403_02', 2)	# 5-6	 **attackbox here**
    RefreshMultihit()
    sprite('vr_iz403_01', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    GFX_0('ElectricBall_Ex_Add', 100)
    sprite('vr_iz403_02', 2)	# 9-10	 **attackbox here**
    Unknown11001(5, 13, 18)
    GFX_0('ElectricBall_Ex_Add', 100)
    Unknown23027()
    sprite('vr_iz403_01', 2)	# 11-12	 **attackbox here**
    sprite('vr_iz403_02', 2)	# 13-14	 **attackbox here**
    label(0)
    sprite('vr_iz403_01', 2)	# 15-16	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    Unknown1084(1)
    sprite('vr_iz403_02', 2)	# 17-18	 **attackbox here**
    sprite('vr_iz403_01', 2)	# 19-20	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_02', 2)	# 21-22	 **attackbox here**
    sprite('vr_iz403_01', 2)	# 23-24	 **attackbox here**
    GFX_1('izef_enagyballthunder_04', 0)
    sprite('vr_iz403_02', 2)	# 25-26	 **attackbox here**

@State
def ElectricBall_Ex_Add():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown1077(0, 360000)
        Unknown1096(1500)
        Unknown4007(2)
        Unknown4009(2)
    sprite('vr_iz403_01', 2)	# 1-2	 **attackbox here**
    sprite('vr_iz403_02', 2)	# 3-4	 **attackbox here**
    sprite('vr_iz403_01', 2)	# 5-6	 **attackbox here**
    sprite('vr_iz403_02', 2)	# 7-8	 **attackbox here**

@State
def bcef404_zanzo():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(64000)
        Unknown2019(-100)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc404_00', 2)	# 1-2
    sprite('vr_bc404_01', 2)	# 3-4
    sprite('vr_bc404_02', 16)	# 5-20

@State
def bcef406_zanzo():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(0)
        Unknown13044(1)
        Unknown2019(-100)

        def upon_3():
            Unknown4007(2)
            Unknown3005(-5)
    sprite('vr_bc406_00', 16)	# 1-16

@State
def UltimateLaserJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('626365665f6a696f64696e655f6a697a6f6b752e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 911):
                Unknown1096(1800)
    sprite('null', 10)	# 1-10
    sprite('null', 10)	# 11-20
    Unknown3004(25)
    sprite('null', 80)	# 21-100
    sprite('null', 10)	# 101-110
    Unknown3004(-25)

@State
def CreateUltimateLaserMatome():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        sendToLabelUpon(1, 0)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 911):
                Unknown1096(1500)
                Unknown2037(1)

        def upon_56():
            Unknown2054(0)
    sprite('null', 5)	# 1-5
    GFX_0('rotationSphere', 0)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 10)	# 6-15
    GFX_0('rotationSphere', 0)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 10)	# 16-25
    GFX_0('rotationSphere', 0)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 10)	# 26-35
    GFX_0('rotationSphere', 0)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 5)	# 36-40
    GFX_0('CreateUltimateLaser00', 100)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 2)	# 41-42
    GFX_0('CreateUltimateLaser01', 100)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 2)	# 43-44
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 2)	# 45-46
    GFX_0('CreateUltimateLaser03', 100)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 2)	# 47-48
    GFX_0('CreateUltimateLaser02', 100)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    sprite('null', 100)	# 49-148
    GFX_0('CreateUltimateLaser03', 100)
    if SLOT_2:
        Unknown23029(1, 912, 0)
    label(0)
    sprite('null', 1)	# 149-149

@State
def rotationSphere():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('626365665f74616d6161726f756e642e44494700000000000000000000000000626365665f74616d6161726f756e645f6d6f74696f6e5f3030302e6d6d6f7400')
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 912):
                Unknown1096(1500)

        def upon_56():
            Unknown2054(0)
    sprite('null', 120)	# 1-120
    sprite('null', 20)	# 121-140
    Unknown1099(300)
    Unknown3004(-17)

@State
def CreateUltimateLaser00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('626365665f6a696f64696e655f737461727430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 912):
                Unknown1096(1500)

        def upon_56():
            Unknown2054(0)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    sprite('null', 40)	# 11-50

@State
def CreateUltimateLaser01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a696f64696e655f737461727430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 912):
                Unknown1096(1500)

        def upon_56():
            Unknown2054(0)
    sprite('null', 42)	# 1-42

@State
def CreateUltimateLaser02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1011(0, 100000)
        Unknown1070(400, 1000)
        Unknown1062(800, 1000)
        Unknown4010(2)
        Unknown4003('626365665f6a696f64696e655f737461727430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 912):
                Unknown1096(1500)

        def upon_56():
            Unknown2054(0)
    label(0)
    sprite('null', 5)	# 1-5
    Unknown3001(255)
    sprite('null', 5)	# 6-10
    Unknown3001(0)
    gotoLabel(0)

@State
def CreateUltimateLaser03():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1011(-100000, 0)
        Unknown1070(400, 1000)
        Unknown1062(800, 1000)
        Unknown4010(2)
        Unknown4003('626365665f6a696f64696e655f737461727430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 912):
                Unknown1096(1500)

        def upon_56():
            Unknown2054(0)
    label(0)
    sprite('null', 5)	# 1-5
    Unknown3001(255)
    sprite('null', 5)	# 6-10
    Unknown3001(0)
    gotoLabel(0)

@State
def UltimateLaserAsiba():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_2('izef_giobceaura_02')
        Unknown2054(1)
    sprite('null', 177)	# 1-177
    sprite('null', 10)	# 178-187
    Unknown3004(-25)

@State
def UltimateLaserAsibaOD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_2('izef_giobceaura_02')
        Unknown2054(1)
    sprite('null', 175)	# 1-175
    sprite('null', 10)	# 176-185
    Unknown3004(-25)

@State
def jumonjiBcSlash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3033()
        Unknown4061(2)
        Unknown2054(1)
        Unknown4009(3)
        Unknown3001(150)
    sprite('vr_iz430_01', 3)	# 1-3
    teleportRelativeX(-30000)
    GFX_1('bcef_jumonjithunder_04', 0)
    GFX_1('bcef_jumonjithunder_04', 1)
    GFX_1('bcef_jumonjithunder_04', 2)
    sprite('vr_iz430_02', 3)	# 4-6
    teleportRelativeX(-48000)
    GFX_1('bcef_jumonjithunder_04', 0)
    GFX_1('bcef_jumonjithunder_04', 1)
    GFX_1('bcef_jumonjithunder_04', 2)
    sprite('vr_iz430_03', 3)	# 7-9
    teleportRelativeX(-8000)
    GFX_1('bcef_jumonjithunder_04', 0)
    GFX_1('bcef_jumonjithunder_04', 1)
    GFX_1('bcef_jumonjithunder_04', 2)
    sprite('vr_iz430_04', 1)	# 10-10
    teleportRelativeX(-40000)
    GFX_1('bcef_jumonjithunder_04', 0)
    sprite('vr_iz430_04', 1)	# 11-11
    GFX_1('bcef_jumonjithunder_04', 1)
    sprite('vr_iz430_04', 1)	# 12-12
    GFX_1('bcef_jumonjithunder_04', 2)
    sprite('vr_iz430_05', 1)	# 13-13
    teleportRelativeX(-40000)
    GFX_1('bcef_jumonjithunder_04', 3)
    sprite('vr_iz430_05', 4)	# 14-17
    GFX_1('bcef_jumonjithunder_04', 4)

@State
def jumonjiBigslashYoko():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1064(0)
        Unknown3001(250)
        Unknown1072(5000)
        Unknown23015(2)

        def upon_43():
            if (SLOT_48 == 970):
                Unknown2037(1)
    sprite('null', 10)	# 1-10
    Unknown1067(120)
    sprite('null', 106)	# 11-116
    Unknown1067(0)
    loopRest()
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000320000000200000002000000')
    sprite('null', 10)	# 117-126
    Unknown1067(-100)
    Unknown3004(-26)

@State
def jumonjiBigslashTate():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1064(0)
        Unknown1072(90000)
        Unknown23015(2)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    Unknown3004(12)
    Unknown1067(80)
    sprite('null', 15)	# 21-35
    Unknown1067(0)
    sprite('null', 10)	# 36-45
    Unknown1067(-100)
    Unknown3004(-26)

@State
def jumonjiBigslashSock00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f736c61736830312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3001(150)
        Unknown23015(2)
    sprite('null', 10)	# 1-10
    sprite('null', 10)	# 11-20
    Unknown3004(-26)

@State
def jumonjiBigslashSock01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f736c61736830322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3001(255)
        Unknown23015(2)
    sprite('null', 15)	# 1-15
    sprite('null', 20)	# 16-35
    Unknown1059(30)
    Unknown3004(-12)

@State
def jumonjiSwordAura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('626365665f6a756d6f6e6a695f736c6173685f74616d6530302e4449470000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    Unknown3004(13)
    sprite('null', 53)	# 21-73

@State
def bcef_432charge():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        teleportRelativeX(-58000)
    sprite('null', 1)	# 1-1
    GFX_1('bcef_432charge', 100)

@State
def bcef_433card_finish():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('626365665f343333636172645f66696e6973682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2005()
        Unknown3032()
        Unknown1096(1400)
        Unknown23151(22, 103)
        Unknown1007(50000)

    @State
    def WildFinishslash():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365665f6a756d6f6e6a695f736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown1064(0)
            Unknown1072(90000)
            Unknown23015(2)
            Unknown3001(0)
            teleportRelativeX(-50000)
        sprite('null', 10)	# 1-10
        Unknown1086(22)
        Unknown3004(24)
        Unknown1067(160)
        sprite('null', 10)	# 11-20
        Unknown1067(0)
        sprite('null', 20)	# 21-40
        sprite('null', 10)	# 41-50
        Unknown1067(-100)
        Unknown3004(-26)
        loopRest()

    @State
    def bcef_432ground_thunder():

        def upon_IMMEDIATE():
            Unknown6001(1)
            teleportRelativeY(0)

            def upon_3():
                Unknown23032(50)
            loopRelated(17, 190)

            def upon_17():
                sendToLabel(1)
        label(0)
        sprite('null', 16)	# 1-16
        GFX_1('bcef_432_ground_thunder', -1)
        gotoLabel(0)
        label(1)
        sprite('null', 16)	# 17-32
        GFX_1('bcef_432_ground_thunder03', -1)
        sprite('null', 16)	# 33-48
        GFX_1('bcef_432_ground_thunder03', -1)
        sprite('null', 16)	# 49-64
        GFX_1('bcef_432_ground_thunder04', -1)
        sprite('null', 16)	# 65-80
        GFX_1('bcef_432_ground_thunder04', -1)

    @State
    def bcef_432ground_thunderOD():

        def upon_IMMEDIATE():
            Unknown6001(1)
            teleportRelativeY(0)

            def upon_3():
                Unknown23032(50)
            loopRelated(17, 300)

            def upon_17():
                sendToLabel(1)
        label(0)
        sprite('null', 16)	# 1-16
        GFX_1('bcef_432_ground_thunder', -1)
        gotoLabel(0)
        label(1)
        sprite('null', 16)	# 17-32
        GFX_1('bcef_432_ground_thunder03', -1)
        sprite('null', 16)	# 33-48
        GFX_1('bcef_432_ground_thunder03', -1)
        sprite('null', 16)	# 49-64
        GFX_1('bcef_432_ground_thunder04', -1)
        sprite('null', 16)	# 65-80
        GFX_1('bcef_432_ground_thunder04', -1)

    @State
    def PersonaIchigeki():

        def upon_IMMEDIATE():
            Unknown2012()
            callSubroutine('PBC_AttackInit')
            Unknown23184('03000000640000000000000000b4c404000000000000000000b4c40400b4c404')
            Unknown23066(1)
            Unknown2053(0)
            callSubroutine('PBC_CheckWarp')
            Unknown23022(1)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 2)
        label(1)
        sprite('iz450_00', 3)	# 1-3
        sprite('iz450_01', 3)	# 4-6
        sprite('iz450_02', 3)	# 7-9
        sprite('iz450_00', 3)	# 10-12
        sprite('iz450_01', 3)	# 13-15
        sprite('iz450_02', 3)	# 16-18
        sprite('iz450_00', 3)	# 19-21
        sprite('iz450_01', 3)	# 22-24
        sprite('iz450_02', 3)	# 25-27
        gotoLabel(1)
        label(2)
        sprite('iz450_00', 3)	# 28-30
        sprite('iz450_01', 3)	# 31-33
        sprite('iz450_02', 3)	# 34-36
        sprite('iz450_00', 3)	# 37-39
        sprite('iz450_01', 3)	# 40-42
        sprite('iz450_02', 3)	# 43-45
        sprite('iz450_00', 3)	# 46-48
        sprite('iz450_01', 3)	# 49-51
        sprite('iz450_02', 3)	# 52-54
        SFX_3('bc003')
        SFX_3('bc_total')
        sprite('iz450_00', 3)	# 55-57
        GFX_0('IchigekiHensinLight', 103)
        sprite('iz450_01', 3)	# 58-60
        sprite('iz450_02', 3)	# 61-63
        sprite('iz450_00', 3)	# 64-66
        Unknown23118(-1)
        sprite('iz450_01', 3)	# 67-69
        sprite('iz450_02', 3)	# 70-72
        sprite('iz450_00', 3)	# 73-75
        sprite('iz450_01', 3)	# 76-78
        sprite('iz450_02', 3)	# 79-81
        sprite('iz450_01', 3)	# 82-84
        sprite('iz450_02', 3)	# 85-87
        sprite('iz450_00', 3)	# 88-90
        sprite('iz450_01', 3)	# 91-93
        sprite('iz450_02', 3)	# 94-96
        sprite('iz450_00', 3)	# 97-99
        sprite('iz450_01', 3)	# 100-102
        sprite('iz450_02', 3)	# 103-105
        sprite('iz450_00', 3)	# 106-108
        sprite('iz450_01', 3)	# 109-111
        sprite('iz450_02', 3)	# 112-114
        sprite('iz450_00', 3)	# 115-117
        sprite('iz450_01', 3)	# 118-120
        sprite('iz450_02', 3)	# 121-123
        sprite('iz450_00', 3)	# 124-126
        sprite('iz450_01', 3)	# 127-129
        sprite('iz450_02', 3)	# 130-132
        sprite('iz450_00', 3)	# 133-135
        sprite('iz450_03', 3)	# 136-138
        Unknown4061(4)
        Unknown23118(0)
        sprite('iz450_04', 3)	# 139-141
        sprite('iz450_05', 3)	# 142-144
        sprite('iz450_03', 3)	# 145-147
        sprite('iz450_04', 3)	# 148-150
        sprite('iz450_05', 3)	# 151-153
        sprite('iz450_03', 3)	# 154-156
        sprite('iz450_04', 3)	# 157-159
        sprite('iz450_05', 3)	# 160-162
        sprite('iz450_03', 3)	# 163-165
        sprite('iz450_04', 3)	# 166-168
        sprite('iz450_05', 3)	# 169-171
        sprite('iz450_03', 3)	# 172-174
        sprite('iz450_04', 3)	# 175-177
        sprite('iz450_05', 3)	# 178-180
        sprite('iz450_03', 3)	# 181-183
        sprite('iz450_04', 3)	# 184-186
        sprite('iz450_05', 3)	# 187-189
        sprite('iz450_03', 3)	# 190-192
        sprite('iz450_04', 3)	# 193-195
        sprite('iz450_05', 3)	# 196-198
        sprite('iz450_03', 3)	# 199-201
        sprite('iz450_04', 3)	# 202-204
        sprite('iz450_05', 3)	# 205-207
        sprite('iz450_03', 3)	# 208-210
        sprite('iz450_04', 3)	# 211-213
        sprite('iz450_05', 3)	# 214-216
        sprite('iz450_03', 3)	# 217-219
        sprite('iz450_04', 3)	# 220-222
        sprite('iz450_05', 3)	# 223-225
        GFX_0('IchigekiZanzou', 103)
        sprite('iz450_03', 3)	# 226-228
        sprite('iz450_04', 3)	# 229-231
        sprite('iz450_05', 3)	# 232-234
        sprite('iz450_06', 3)	# 235-237
        SFX_3('magiccircle_a')
        sprite('iz450_07', 3)	# 238-240
        SFX_3('magiccircle_a')
        sprite('iz450_08', 3)	# 241-243
        SFX_3('magiccircle_a')
        sprite('iz450_09', 3)	# 244-246
        SFX_3('magiccircle_a')
        sprite('iz450_10', 3)	# 247-249
        SFX_3('magiccircle_a')
        sprite('iz450_11', 3)	# 250-252
        sprite('iz450_12', 3)	# 253-255
        sprite('iz450_13', 3)	# 256-258
        sprite('iz450_14', 3)	# 259-261
        sprite('iz450_15', 3)	# 262-264
        sprite('iz450_16', 3)	# 265-267
        sprite('iz450_17', 3)	# 268-270
        sprite('iz450_18', 3)	# 271-273
        SFX_3('spsys_sp_special')
        sprite('iz450_19', 3)	# 274-276
        sprite('iz450_20', 3)	# 277-279
        sprite('iz450_20', 1)	# 280-280
        GFX_0('IchigekiPicture', 100)
        sendToLabelUpon(35, 4)
        label(3)
        sprite('iz450_18', 3)	# 281-283
        sprite('iz450_19', 3)	# 284-286
        sprite('iz450_20', 3)	# 287-289
        gotoLabel(3)
        label(4)
        sprite('iz450_20', 3)	# 290-292
        clearUponHandler(35)
        Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000023000000')
        GFX_0('IchigekiFlash', 103)
        SFX_3('bc004')
        SFX_3('bc000')
        sprite('iz450_21', 1)	# 293-293
        SFX_3('bc004')
        sprite('iz450_21', 1)	# 294-294
        SFX_3('bc004')
        sprite('iz450_21', 1)	# 295-295
        SFX_3('bc004')
        sprite('iz450_22', 3)	# 296-298
        SFX_3('bc000')
        sprite('iz450_23', 3)	# 299-301
        Unknown23119(1694498815, 2, 45)
        sprite('iz450_24', 3)	# 302-304
        SFX_3('bc000')
        sprite('iz450_22', 3)	# 305-307
        sprite('iz450_23', 3)	# 308-310
        SFX_3('bc000')
        sprite('iz450_24', 3)	# 311-313
        sprite('iz450_22', 3)	# 314-316
        SFX_3('bc000')
        sprite('iz450_23', 3)	# 317-319
        sprite('iz450_24', 3)	# 320-322
        SFX_3('bc000')
        sprite('iz450_22', 3)	# 323-325
        sprite('iz450_23', 3)	# 326-328
        SFX_3('bc000')
        sprite('iz450_24', 3)	# 329-331
        sprite('iz450_22', 3)	# 332-334
        SFX_3('bc000')
        sprite('iz450_23', 3)	# 335-337
        sprite('iz450_24', 3)	# 338-340
        SFX_3('bc000')
        sprite('iz450_22', 3)	# 341-343
        sprite('iz450_23', 3)	# 344-346
        SFX_3('bc000')
        sprite('iz450_24', 3)	# 347-349
        sprite('iz450_22', 3)	# 350-352
        Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
        Unknown36(1)
        Unknown1007(100000)
        Unknown35()
        sprite('iz450_23', 3)	# 353-355
        sprite('iz450_24', 3)	# 356-358
        sprite('iz450_22', 3)	# 359-361
        sprite('iz450_23', 3)	# 362-364
        sprite('iz450_24', 3)	# 365-367
        sprite('iz450_22', 3)	# 368-370
        sprite('iz450_23', 3)	# 371-373
        sprite('iz450_24', 3)	# 374-376
        sprite('iz450_22', 3)	# 377-379
        Unknown21007(3, 33)
        sprite('iz450_23', 3)	# 380-382
        sprite('iz450_24', 3)	# 383-385
        sprite('iz450_23', 3)	# 386-388
        label(0)
        sprite('keep', 32767)	# 389-33155
        enterState('PersonaDeleteAndIdling')

    @State
    def PersonaIchigekiWin():

        def upon_IMMEDIATE():
            callSubroutine('PBC_AttackInit')
            callSubroutine('PBC_CheckWarp')
            Unknown1086(3)
            teleportRelativeX(-100000)
            Unknown1007(4000000)
            physicsYImpulse(-30000)
            sendToLabelUpon(2, 2)
        label(1)
        sprite('iz450_25', 3)	# 1-3
        Unknown4061(4)
        sprite('iz450_26', 3)	# 4-6
        sprite('iz450_27', 3)	# 7-9
        gotoLabel(1)
        label(2)
        sprite('iz450_28', 3)	# 10-12
        Unknown1084(1)
        Unknown8004(100, 1, 1)
        sprite('iz450_29', 3)	# 13-15
        sprite('iz450_31', 4)	# 16-19
        sprite('iz450_32', 4)	# 20-23
        sprite('iz450_33', 4)	# 24-27
        sprite('iz450_34', 4)	# 28-31
        sprite('iz450_35', 4)	# 32-35
        sprite('iz450_36', 4)	# 36-39
        sprite('iz450_37', 4)	# 40-43
        sprite('iz450_38', 4)	# 44-47
        GFX_0('Zanzoh_IchigekiWin', 100)
        sprite('iz450_39', 4)	# 48-51
        sprite('keep', 1)	# 52-52
        Unknown21007(3, 34)
        label(3)
        sprite('iz450_39', 4)	# 53-56
        sprite('iz450_40', 4)	# 57-60
        sprite('iz450_41', 4)	# 61-64
        gotoLabel(3)

    @State
    def PersonaIchigekiWinEffTest():

        def upon_IMMEDIATE():
            callSubroutine('PersonaReset')
            Unknown1086(3)
            Unknown4061(4)
        sprite('iz450_28', 3)	# 1-3
        Unknown1084(1)
        Unknown8004(100, 1, 1)
        sprite('iz450_29', 3)	# 4-6
        sprite('iz450_31', 4)	# 7-10
        sprite('iz450_32', 4)	# 11-14
        sprite('iz450_33', 4)	# 15-18
        sprite('iz450_34', 4)	# 19-22
        sprite('iz450_35', 4)	# 23-26
        sprite('iz450_36', 4)	# 27-30
        sprite('iz450_37', 4)	# 31-34
        sprite('iz450_38', 4)	# 35-38
        GFX_0('Zanzoh_IchigekiWin', 100)
        sprite('iz450_39', 4)	# 39-42
        sprite('keep', 1)	# 43-43
        Unknown21007(3, 34)
        label(3)
        sprite('iz450_39', 4)	# 44-47
        sprite('iz450_40', 4)	# 48-51
        sprite('iz450_41', 4)	# 52-55
        gotoLabel(3)

    @State
    def IchigekiGroundDenki():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365663435305f64656e6b6967726f756e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown3001(255)
        sprite('null', 60)	# 1-60
        GFX_0('IchigekiGroundDenki2', 100)

    @State
    def IchigekiGroundDenki2():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365663435305f64656e6b6967726f756e64322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown3001(255)
        sprite('null', 10)	# 1-10
        sprite('null', 5)	# 11-15
        Unknown3001(0)
        sprite('null', 10)	# 16-25
        Unknown1072(-15000)
        Unknown3001(255)
        sprite('null', 5)	# 26-30
        Unknown3001(0)
        sprite('null', 10)	# 31-40
        Unknown1072(15000)
        Unknown3001(255)
        sprite('null', 5)	# 41-45
        Unknown3001(0)
        sprite('null', 10)	# 46-55
        Unknown1072(0)
        Unknown3001(255)

    @State
    def IchigekiHensinLight():

        def upon_IMMEDIATE():
            GFX_2('bcef_hensintame_03')
        sprite('null', 80)	# 1-80
        sprite('null', 1)	# 81-81
        Unknown3001(0)
        GFX_1('bcef_hensinend_02', 100)

    @State
    def IchigekiZanzou():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365663435305f7a616e7a6f752e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
        sprite('null', 50)	# 1-50
        sprite('null', 90)	# 51-140
        GFX_0('IchigekiZanzou2', 100)
        Unknown3004(-26)

    @State
    def IchigekiZanzou2():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365663435305f7a616e7a6f75322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
            Unknown3001(0)
        sprite('null', 10)	# 1-10
        Unknown3004(26)
        sprite('null', 100)	# 11-110

    @State
    def IchigekiFlash():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365663435305f666c6173682e444947000000000000000000000000000000626365663435305f666c6173685f303030302e6d6d6f74000000000000000000')
            Unknown2054(1)
        sprite('null', 150)	# 1-150
        GFX_0('IchigekiYugami', 100)
        GFX_2('bcef_flashline_02')
        sprite('null', 20)	# 151-170
        Unknown3004(-13)

    @State
    def IchigekiYugami():

        def upon_IMMEDIATE():
            Unknown4007(2)
            Unknown4010(2)
            Unknown3032()
            Unknown3057(1)
            Unknown3058(2500)
            Unknown2054(1)
        sprite('vr_bc_yugami2', 15)	# 1-15
        Unknown1099(40)
        Unknown1074(3000)
        sprite('vr_bc_yugami2', 120)	# 16-135
        Unknown1099(0)
        sprite('vr_bc_yugami2', 15)	# 136-150
        Unknown3004(-17)
        loopRest()

    @State
    def Ichigekibeam():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4007(2)
            Unknown4003('626365663435305f6265616d2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown2054(1)
        sprite('null', 180)	# 1-180
        physicsYImpulse(-1500)
        sprite('null', 120)	# 181-300
        physicsYImpulse(0)
        Unknown3004(-5)
        Unknown1059(50)
        sprite('null', 20)	# 301-320
        Unknown3004(-13)

    @State
    def Ichigekiwhite():

        def upon_IMMEDIATE():
            Unknown2054(1)
            Unknown4061(2)
            Unknown23015(1)
            Unknown2007()
            Unknown3032()
            Unknown3001(0)
        sprite('vr_bc450_white', 60)	# 1-60
        Unknown3004(5)
        sprite('vr_bc450_white', 200)	# 61-260
        sprite('vr_bc450_white', 10)	# 261-270
        Unknown3004(-26)

    @State
    def LaserJimen():
        Unknown4009(2)
        Unknown4007(2)
        Unknown4010(2)
        sprite('null', 20)	# 1-20
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 21-40
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 41-60
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 61-80
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 81-100
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 101-120
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 121-140
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 141-160
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 161-180
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 181-200
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 201-220
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 221-240
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 241-260
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 261-280
        GFX_1('rgef431mc', 100)
        sprite('null', 20)	# 281-300
        GFX_1('rgef431mc', 100)

    @State
    def IchigekiBeamJizoku():

        def upon_IMMEDIATE():
            Unknown3033()
            Unknown4061(3)
            Unknown2008()
            Unknown1072(90000)
            Unknown3029(1)
            Unknown3069(2)
            Unknown3070(1)
            Unknown3071(2)
            Unknown3076(1000)
            Unknown3077(900)
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 2)
        sprite('dmy_shot_atk', 1)	# 1-1
        GFX_0('Ichigekibeam', 100)
        sprite('dmy_shot_atk', 1)	# 2-2
        GFX_1('izef_enagyballthunder_04', 0)
        sprite('dmy_shot_atk', 1)	# 3-3
        sprite('dmy_shot_atk', 1)	# 4-4
        sprite('dmy_shot_atk', 1)	# 5-5
        label(1)
        sprite('dmy_shot_atk', 3)	# 6-8
        GFX_1('izef_enagyballthunder_04', 0)
        sprite('dmy_shot_atk', 6)	# 9-14
        GFX_1('izef_enagyballthunder_04', 0)
        loopRest()
        gotoLabel(1)
        label(2)
        sprite('dmy_shot_atk', 3)	# 15-17
        GFX_1('izef_enagyballthunder_04', 0)
        sprite('dmy_shot_atk', 6)	# 18-23
        GFX_1('izef_enagyballthunder_04', 0)
        loopRest()
        gotoLabel(2)
        label(0)
        sprite('null', 1)	# 24-24

    @State
    def IchigekiPicture():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown23015(1)
            Unknown3029(1)
            Unknown3072('ff000000ff000000ff000000ff000000')
            Unknown3073('ff000000ff000000ff000000ff000000')
            Unknown3076(1000)
            Unknown3077(1100)
            Unknown3069(2)
            Unknown6001(1)
            Unknown1001(640000)
            teleportRelativeX(600000)
            teleportRelativeY(-720000)
            Unknown1096(3000)

            def upon_STATE_END():
                Unknown21012('506572736f6e614963686967656b69000000000000000000000000000000000023000000')
        sprite('ichigeki0', 6)	# 1-6	 **attackbox here**
        physicsXImpulse(-140000)
        physicsYImpulse(20000)
        Unknown1099(-100)
        Unknown23118(-1)
        Unknown23117(-16777216, 11)
        sprite('ichigeki0', 5)	# 7-11	 **attackbox here**
        Unknown1019(20)
        YAccel(10)
        Unknown1099(-200)
        sprite('ichigeki0', 60)	# 12-71	 **attackbox here**
        Unknown1099(0)
        Unknown1096(900)
        tag_voice(0, 'pbc292_0', 'pbc292_1', '', '')
        Unknown1019(5)
        YAccel(5)
        Unknown3029(0)
        Unknown23120()
        Unknown23118(-16777216)
        loopRest()
        label(0)
        sprite('ichigeki0', 6)	# 72-77	 **attackbox here**
        Unknown23117(-1, 8)
        Unknown3001(200)
        Unknown3004(-25)
        sprite('ichigeki0', 1)	# 78-78	 **attackbox here**
        Unknown21012('506572736f6e614963686967656b69000000000000000000000000000000000023000000')

    @State
    def IchigekiShake():

        def upon_IMMEDIATE():
            Unknown2054(1)
            Unknown4010(2)
        sprite('null', 5)	# 1-5
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 6-10
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 11-15
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 16-20
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 21-25
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 26-30
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 31-35
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 36-40
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 41-45
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 46-50
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 51-55
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 56-60
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 61-65
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 66-70
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 71-75
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 76-80
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 81-85
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 86-90
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 91-95
        ScreenShake(60000, 60000)
        sprite('null', 5)	# 96-100
        ScreenShake(60000, 60000)

    @State
    def IchigekiFinish_Effect():

        def upon_IMMEDIATE():
            Unknown1086(22)
            Unknown1007(150000)
        sprite('null', 30)	# 1-30
        GFX_1('bcef_smallbom_04', 103)
        sprite('null', 60)	# 31-90
        GFX_1('bcef_smallbom_05', 103)
        GFX_0('Ichigekiwhite', 103)

    @State
    def IchigekiCamera():

        def upon_IMMEDIATE():
            sendToLabelUpon(32, 0)
            sendToLabelUpon(33, 1)
            sendToLabelUpon(34, 2)
            sendToLabelUpon(35, 3)
            sendToLabelUpon(36, 4)
            sendToLabelUpon(37, 5)
            Unknown20000(1)
            Unknown20002(1)
            Unknown20003(1)
            Unknown20004(1)
            Unknown2034(0)
            Unknown2053(0)
        sprite('null', 32767)	# 1-32767
        label(1)
        sprite('null', 32767)	# 32768-65534
        physicsYImpulse(60000)
        label(2)
        sprite('null', 32767)	# 65535-98301
        Unknown1084(1)
        teleportRelativeY(80000000)
        Unknown20009(1000)
        label(3)
        sprite('null', 1)	# 98302-98302
        Unknown20009(1400)
        sprite('null', 1)	# 98303-98303
        Unknown20009(1800)
        sprite('null', 1)	# 98304-98304
        Unknown20009(2200)
        sprite('null', 1)	# 98305-98305
        Unknown20009(2600)
        sprite('null', 32767)	# 98306-131072
        label(4)
        sprite('null', 32767)	# 131073-163839
        Unknown1000(0)
        teleportRelativeY(40000000)
        Unknown20009(1000)
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)
        label(5)
        sprite('null', 100)	# 163840-163939
        Unknown23151(3, 103)
        Unknown1007(1000000)
        Unknown20009(1000)
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)
        sprite('keep', 32767)	# 163940-196706
        physicsYImpulse(-35000)
        label(0)
        sprite('null', 1)	# 196707-196707
        loopRest()

    @State
    def Zanzoh_IchigekiWin():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown3032()
            Unknown4061(4)
        sprite('vr_iz450_20', 16)	# 1-16

    @State
    def LifeLinkEff():

        def upon_IMMEDIATE():
            Unknown23032(50)
            Unknown23033(50)
        sprite('null', 1)	# 1-1
        Unknown4045('6e7465665f73746f72795f6c6966656c696e6b6566665f6c696e653200000000ffffffff')

    @State
    def PBC_PersonaEntry():

        def upon_IMMEDIATE():
            Unknown23023()
            Unknown23184('030000006400000050c30000b03cffff00000000000000000000000000000000')
            callSubroutine('PBC_AttackInit')
            Unknown23022(1)
            Unknown4007(3)
            Unknown23015(2)
            callSubroutine('PBC_CheckWarp')
            teleportRelativeY(50000)
        sprite('iz600_00', 6)	# 1-6
        GFX_0('ToujouAura', 100)
        GFX_1('bcef_toujoufire_07', 100)
        SFX_0('persona_call')
        SFX_3('cloth_h')
        sprite('iz600_01', 6)	# 7-12
        sprite('iz600_02', 6)	# 13-18
        sprite('iz600_00', 6)	# 19-24
        sprite('iz600_01', 6)	# 25-30
        sprite('iz600_02', 6)	# 31-36
        sprite('iz600_00', 6)	# 37-42
        sprite('iz600_01', 6)	# 43-48
        sprite('keep', 32767)	# 49-32815
        enterState('PersonaDeleteAndIdling')

    @State
    def Entry():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4061(2)
            Unknown4007(2)
            Unknown4009(2)
            Unknown4010(2)
        sprite('vr_bc600_00', 18)	# 1-18

    @State
    def ToujouAura():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4010(2)
            Unknown4003('626365663630305f746f756a6f756175726130302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
            GFX_2('bcef_mugenfire_01')
            Unknown2054(1)
            Unknown23015(2)
            Unknown3001(0)
        sprite('null', 10)	# 1-10
        sprite('null', 20)	# 11-30
        Unknown3004(13)
        sprite('null', 30)	# 31-60
        Unknown3004(-7)

    @State
    def Entry2():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown4061(0)
            Unknown4007(2)
            Unknown4009(2)
            Unknown1007(24000)
            teleportRelativeX(20000)
        sprite('vr_bc601_00', 4)	# 1-4
        physicsXImpulse(-12000)
        physicsYImpulse(2000)
        sprite('vr_bc601_01', 4)	# 5-8
        Unknown1021(0)
        sprite('vr_bc601_00', 4)	# 9-12
        sprite('vr_bc601_01', 4)	# 13-16
        sprite('vr_bc601_00', 4)	# 17-20
        Unknown3004(-16)
        sprite('vr_bc601_01', 4)	# 21-24
        sprite('vr_bc601_00', 4)	# 25-28
        sprite('vr_bc601_01', 4)	# 29-32

    @State
    def P4U_Cutin_Parent():

        def upon_IMMEDIATE():
            Unknown2054(1)
        sprite('null', 1)	# 1-1
        GFX_0('P4U_Cutin_Face', 100)

    @State
    def P4U_Cutin_Face():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown23015(5)
            Unknown2007()
            Unknown4009(2)
            Unknown2054(1)
            Unknown13044(0)
            Unknown6001(1)
            Unknown1000(-650000)
            teleportRelativeY(-292000)
            Unknown1096(1350)
            Unknown2037(0)
            Unknown3001(0)

            def upon_3():
                if (SLOT_2 == 2):
                    Unknown1007(15000)
                    Unknown3001(150)
                if (SLOT_2 == 3):
                    Unknown1007(-30000)
                    Unknown3001(180)
                if (SLOT_2 == 4):
                    Unknown1007(25000)
                    Unknown3001(210)
                if (SLOT_2 == 5):
                    Unknown1007(-20000)
                    Unknown3001(255)
                if (SLOT_2 == 6):
                    Unknown1007(10000)
                Unknown2038(1)
        sprite('vr_99p4u_face00', 45)	# 1-45
        SFX_0('spsys_over_power')
        SFX_0('spsys_over_power')
        if SLOT_168:
            GFX_0('P4U_ka_NotJPN', 100)
        else:
            GFX_0('P4U_ka_JPN', 100)
        sprite('vr_99p4u_face00', 1)	# 46-46
        Unknown3001(180)
        sprite('vr_99p4u_face00', 1)	# 47-47
        Unknown3001(120)
        sprite('vr_99p4u_face00', 1)	# 48-48
        Unknown3001(60)

    @State
    def P4U_ka_JPN():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown23015(5)
            Unknown2007()
            Unknown4009(2)
            Unknown6001(1)
            Unknown1000(-950000)
            teleportRelativeY(-232000)
            Unknown1096(1350)
        sprite('vr_p4_ka_mozi', 1)	# 1-1
        Unknown1096(100)
        Unknown3001(40)
        sprite('vr_p4_ka_mozi', 1)	# 2-2
        teleportRelativeX(-2000)
        Unknown1007(500)
        Unknown1096(300)
        Unknown3001(70)
        sprite('vr_p4_ka_mozi', 1)	# 3-3
        teleportRelativeX(-2000)
        Unknown1007(550)
        Unknown1096(700)
        Unknown3001(100)
        sprite('vr_p4_ka_mozi', 1)	# 4-4
        teleportRelativeX(-2000)
        Unknown1007(600)
        Unknown1096(900)
        Unknown3001(130)
        sprite('vr_p4_ka_mozi', 1)	# 5-5
        teleportRelativeX(-2000)
        Unknown1007(6500)
        Unknown1096(800)
        Unknown3001(160)
        sprite('vr_p4_ka_mozi', 1)	# 6-6
        teleportRelativeX(-2000)
        Unknown1007(700)
        Unknown1096(900)
        Unknown3001(190)
        sprite('vr_p4_ka_mozi', 1)	# 7-7
        teleportRelativeX(-2000)
        Unknown1007(800)
        Unknown1096(1150)
        Unknown3001(220)
        sprite('vr_p4_ka_mozi', 38)	# 8-45
        teleportRelativeX(-2000)
        Unknown1007(800)
        Unknown1096(1100)
        Unknown3001(255)
        physicsXImpulse(-50)
        physicsYImpulse(50)
        sprite('vr_p4_ka_mozi', 1)	# 46-46
        Unknown3001(180)
        Unknown1096(700)
        sprite('vr_p4_ka_mozi', 1)	# 47-47
        Unknown3001(120)
        Unknown1096(300)
        sprite('vr_p4_ka_mozi', 1)	# 48-48
        Unknown3001(60)
        Unknown1096(100)

    @State
    def P4U_ka_NotJPN():

        def upon_IMMEDIATE():
            Unknown3032()
            Unknown23015(5)
            Unknown2007()
            Unknown4009(2)
            Unknown6001(1)
            Unknown1000(-950000)
            teleportRelativeY(-232000)
            Unknown1096(1350)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 1-1
        Unknown1096(100)
        Unknown3001(40)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 2-2
        teleportRelativeX(-2000)
        Unknown1007(500)
        Unknown1096(300)
        Unknown3001(70)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 3-3
        teleportRelativeX(-2000)
        Unknown1007(550)
        Unknown1096(700)
        Unknown3001(100)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 4-4
        teleportRelativeX(-2000)
        Unknown1007(600)
        Unknown1096(900)
        Unknown3001(130)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 5-5
        teleportRelativeX(-2000)
        Unknown1007(6500)
        Unknown1096(800)
        Unknown3001(160)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 6-6
        teleportRelativeX(-2000)
        Unknown1007(700)
        Unknown1096(900)
        Unknown3001(190)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 7-7
        teleportRelativeX(-2000)
        Unknown1007(800)
        Unknown1096(1150)
        Unknown3001(220)
        sprite('vr_p4_ka_mozi_notjpn', 38)	# 8-45
        teleportRelativeX(-2000)
        Unknown1007(800)
        Unknown1096(1100)
        Unknown3001(255)
        physicsXImpulse(-50)
        physicsYImpulse(50)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 46-46
        Unknown3001(180)
        Unknown1096(700)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 47-47
        Unknown3001(120)
        Unknown1096(300)
        sprite('vr_p4_ka_mozi_notjpn', 1)	# 48-48
        Unknown3001(60)
        Unknown1096(100)