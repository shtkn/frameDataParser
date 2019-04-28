@State
def PKA_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)
    Unknown3038(1)
    Unknown24('504b415f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PKA_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PKA_ReceptionSignal')
    sprite('null', 32767)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PKA_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 2040):
            Unknown23185('504b415f506572736f6e6135420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2041):
            Unknown23185('504b415f506572736f6e6135425f4e6f726d616c00000000000000000000000032000000')
        if (SLOT_48 == 2042):
            Unknown23185('504b415f506572736f6e6135425f486f6c64000000000000000000000000000032000000')
        if (SLOT_48 == 2043):
            Unknown23185('504b415f506572736f6e6135425f486f6c645f4a75737400000000000000000032000000')
        if (SLOT_48 == 2044):
            Unknown23185('504b415f506572736f6e6135425f43410000000000000000000000000000000032000000')
        if (SLOT_48 == 2050):
            Unknown23185('504b415f506572736f6e613542326e640000000000000000000000000000000032000000')
        if (SLOT_48 == 2051):
            Unknown23185('504b415f506572736f6e613542326e645f486f6c64000000000000000000000032000000')
        if (SLOT_48 == 2052):
            Unknown23185('504b415f506572736f6e613542326e645f486f6c645f4a75737400000000000032000000')
        if (SLOT_48 == 2053):
            Unknown23185('504b415f506572736f6e613542326e645f43410000000000000000000000000032000000')
        if (SLOT_48 == 4080):
            Unknown23185('504b415f506572736f6e6134417373697374000000000000000000000000000032000000')
        if (SLOT_48 == 2540):
            Unknown23185('504b415f506572736f6e61415f46696e6973680000000000000000000000000032000000')
        if (SLOT_48 == 2530):
            Unknown23185('504b415f506572736f6e6141697235430000000000000000000000000000000032000000')
        if (SLOT_48 == 2531):
            Unknown23185('504b415f506572736f6e6141697235435f41544b00000000000000000000000032000000')
        if (SLOT_48 == 4000):
            Unknown23185('504b415f506572736f6e61496e76696e6369626c6541747461636b000000000032000000')
        if (SLOT_48 == 4020):
            Unknown23185('504b415f506572736f6e614b757368697a61736869410000000000000000000032000000')
        if (SLOT_48 == 4040):
            Unknown23185('504b415f506572736f6e615473756b616d65420000000000000000000000000032000000')
        if (SLOT_48 == 4021):
            Unknown23185('504b415f506572736f6e614b757368697a61736869455800000000000000000032000000')
        if (SLOT_48 == 4300):
            Unknown23185('504b415f506572736f6e614b656e6b614f44000000000000000000000000000064000000')
        if (SLOT_48 == 4301):
            Unknown23185('504b415f506572736f6e614b656e6b614f445f44554f0000000000000000000064000000')
        if (SLOT_48 == 4310):
            Unknown23185('504b415f506572736f6e614b75726f6b6f67650000000000000000000000000064000000')
        if (SLOT_48 == 4500):
            Unknown23185('504b415f506572736f6e614963686967656b69000000000000000000000000002c010000')
        if (SLOT_48 == 9999):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')

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
def PKA_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PKA_AttackInit():
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
    callSubroutine('PKA_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PKA_SPAttackInit():
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
    callSubroutine('PKA_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PKA_DDAttackInit():
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
    callSubroutine('PKA_ReceptionSignal')
    Unknown23023()

@Subroutine
def PKA_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PKA_ForceWarp():
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
    sprite('keep', 32767)
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_0('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PKA_PersonaWait')

@State
def PersonaSummonEffect():
    sprite('null', 30)
    Unknown23015(13)
    Unknown4054(11)
    Unknown4045('706572736f6e615f73756d6d6f6e00000000000000000000000000000000000064000000')

@State
def PersonaSummonEffect_PLAYER():
    sprite('null', 30)
    Unknown1007(288000)
    teleportRelativeX(112000)
    GFX_1('persona_summon_ply', 100)

@State
def PersonaDeleteEffect():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        callSubroutine('PKA_ReceptionSignal')
    sprite('null', 30)
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
def PKA_PersonaA_Finish():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        AttackLevel_(5)
        Damage(2400)
        AttackP1(100)
        AirUntechableTime(35)
        AirPushbackX(30000)
        AirPushbackY(20000)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown2017(1)
        Unknown2053(1)
        callSubroutine('PKA_CheckWarp')
        Unknown4007(3)

        def upon_STATE_END():
            SLOT_6 = 0

        def upon_11():
            sendToLabel(0)
    sprite('ta408_00', 2)
    SFX_3('airbackdash_l')
    Unknown2006()
    Unknown4007(0)
    SLOT_6 = 1
    sprite('ta408_01', 2)
    SFX_3('airbackdash_l')
    sprite('ta408_00', 2)
    SFX_3('airbackdash_l')
    sprite('ta408_02', 2)
    SFX_3('airdash_m')
    physicsXImpulse(20000)
    sprite('ta408_03', 3)
    RefreshMultihit()
    Unknown1019(200)
    sprite('ta408_03', 3)
    SFX_3('airdash_m')
    Unknown1019(110)
    sprite('ta408_03', 3)
    Unknown1019(105)
    sprite('ta408_03', 3)
    SFX_3('airdash_m')
    Unknown1019(105)
    sprite('ta408_03', 3)
    Unknown1019(80)
    label(0)
    sprite('keep', 8)
    clearUponHandler(11)
    Unknown23027()
    sprite('ta408_04', 2)
    SFX_3('brake_normal_heavy')
    Unknown1019(50)
    sprite('ta408_04', 2)
    Unknown1019(30)
    sprite('ta408_05', 2)
    Unknown1019(30)
    sprite('ta408_05', 3)
    Unknown1019(20)
    sprite('ta408_06', 3)
    Unknown1019(20)
    sprite('ta408_06', 30)
    SLOT_6 = 0
    Unknown1019(0)
    sprite('ta408_06', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@Subroutine
def PKA_Persona5B_ATK():
    AttackLevel_(5)
    AttackP1(80)
    PushbackX(10000)
    AirUntechableTime(25)
    AirHitstunAnimation(9)
    AirPushbackY(-50000)
    Unknown9190(1)
    Unknown9118(30)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown23078(1)
    Unknown2017(1)
    Unknown4007(3)
    Unknown2053(1)
    Unknown2006()

@State
def PKA_Persona5B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B_ATK')
        callSubroutine('PKA_CheckWarp')

        def upon_54():
            sendToLabel(580)

        def upon_3():
            if (SLOT_18 >= 300):
                sendToLabel(1)
    sprite('ta204_50', 3)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta204_51', 3)
    sprite('ta204_00', 2)
    loopRest()
    Unknown4007(0)
    label(0)
    sprite('ta204_50', 3)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta204_51', 3)
    sprite('ta204_00', 2)
    loopRest()
    gotoLabel(0)
    label(580)
    label(1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B_Normal():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B_ATK')
        callSubroutine('PKA_CheckWarp')
    sprite('ta204_04', 3)
    GFX_0('ta_5C_zanzoh', 100)
    SFX_3('slash_blade_fast')
    sprite('ta204_05', 3)
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    sprite('ta204_05', 20)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B_Hold():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B_ATK')
        callSubroutine('PKA_CheckWarp')
    sprite('ta204_01', 3)
    sprite('ta204_02', 3)
    sprite('ta204_03', 3)
    sprite('ta204_04', 3)
    SFX_3('slash_blade_fast')
    GFX_0('ta_5C_zanzoh', 100)
    sprite('ta204_05', 3)
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    sprite('ta204_05', 20)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B_Hold_Just():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B_ATK')
        Unknown10000(150)
        AttackP1(90)
        Unknown9154(38)
        AirUntechableTime(44)
        Unknown11001(0, 8, 8)
        Unknown9266(7)
        callSubroutine('PKA_CheckWarp')
    sprite('ta204_01', 3)
    sprite('ta204_02', 3)
    sprite('ta204_03', 3)
    sprite('ta204_04', 3)
    SFX_3('slash_blade_fast')
    GFX_0('ta_5C_zanzoh', 100)
    sprite('ta204_05', 3)
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    sprite('ta204_05', 20)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B_CA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        Unknown23078(1)
        callSubroutine('PKA_CheckWarp')
        Unknown4007(3)
        Unknown2053(0)
        Unknown2017(0)
        Unknown23022(1)
        Unknown2003(1)
    sprite('ta204_50', 2)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta204_51', 2)
    sprite('ta204_00', 2)
    sprite('ta204_04', 2)
    GFX_0('ta_5C_zanzoh', 100)
    SFX_3('slash_blade_fast')
    sprite('ta204_05', 3)
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    sprite('ta204_05', 20)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@Subroutine
def PKA_Persona5B2nd_ATK():
    AttackLevel_(5)
    AttackP1(80)
    PushbackX(-30000)
    AirPushbackX(-15000)
    AirPushbackY(18000)
    Unknown30055('605b03001e0000001e000000')
    Unknown11058('0000000000000000010000000000000000000000')
    Unknown23078(1)
    Unknown2017(1)
    Unknown4007(3)
    Unknown2053(1)

@State
def PKA_Persona5B2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B2nd_ATK')
        callSubroutine('PKA_CheckWarp')

        def upon_54():
            sendToLabel(580)

        def upon_3():
            if (SLOT_18 >= 300):
                sendToLabel(1)
    sprite('ta232_10', 3)
    Unknown2006()
    sprite('ta232_11', 2)
    sprite('ta232_12', 2)
    sprite('ta232_13', 2)
    sprite('ta232_14', 2)
    sprite('ta232_15', 4)
    label(0)
    sprite('ta232_55', 3)
    sprite('ta232_56', 3)
    sprite('ta232_57', 3)
    loopRest()
    gotoLabel(0)
    label(580)
    label(1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B2nd_Hold():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B2nd_ATK')
        callSubroutine('PKA_CheckWarp')
    sprite('ta232_00', 1)
    Unknown2006()
    physicsXImpulse(20000)
    sprite('ta232_01', 1)
    sprite('ta232_02', 1)
    sprite('ta232_03', 1)
    SFX_3('slash_blade_slow')
    physicsXImpulse(0)
    StartMultihit()
    sprite('ta232_05', 2)
    Unknown23054('74613233325f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('ta232_05', 3)
    StartMultihit()
    sprite('ta232_06', 5)
    sprite('ta232_07', 20)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B2nd_Hold_Just():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B2nd_ATK')
        Unknown10000(150)
        AttackP1(90)
        Unknown9154(27)
        AirUntechableTime(37)
        Unknown11001(0, 8, 8)
        Unknown9266(7)
        callSubroutine('PKA_CheckWarp')
    sprite('ta232_00', 2)
    physicsXImpulse(20000)
    sprite('ta232_01', 2)
    sprite('ta232_02', 2)
    sprite('ta232_03', 2)
    SFX_3('slash_blade_slow')
    physicsXImpulse(0)
    StartMultihit()
    sprite('ta232_05', 2)
    Unknown23054('74613233325f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('ta232_05', 3)
    StartMultihit()
    sprite('ta232_06', 5)
    sprite('ta232_07', 20)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B2nd_CA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        Unknown23078(1)
        callSubroutine('PKA_CheckWarp')
        Unknown4007(3)
        Unknown2053(0)
        Unknown2017(0)
        Unknown23022(1)
        Unknown2003(1)
    sprite('ta232_00', 2)
    teleportRelativeX(-200000)
    physicsXImpulse(20000)
    sprite('ta232_01', 2)
    sprite('ta232_02', 2)
    sprite('ta232_03', 2)
    SFX_3('slash_blade_slow')
    physicsXImpulse(0)
    StartMultihit()
    sprite('ta232_05', 2)
    Unknown23054('74613233325f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('ta232_05', 3)
    StartMultihit()
    sprite('ta232_06', 5)
    sprite('ta232_07', 20)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaAir5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffb03cffff00000000000000000000000000000000')
        callSubroutine('PKA_AttackInit')
        Unknown2017(1)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PKA_CheckWarp')

        def upon_56():
            sendToLabel(1)
    sprite('ta254_00', 3)
    label(0)
    sprite('ta254_01', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaAir5C_ATK():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PKA_AttackInit')
        AttackLevel_(5)
        Unknown9154(35)
        AirUntechableTime(41)
        AirPushbackY(-20000)
        Unknown9310(1)
        GroundedHitstunAnimation(2)
        Unknown9130(30)
        Unknown9142(30)
        Unknown23078(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2017(1)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PKA_CheckWarp')
    sprite('ta254_02', 5)
    Unknown4007(0)
    physicsXImpulse(20000)
    SFX_3('slash_blade_slow')
    sprite('ta254_03', 2)
    physicsXImpulse(0)
    sprite('ta254_04', 5)
    Unknown23022(0)
    SFX_3('down_steal_m')
    GFX_0('taef_Air5C_Zanzoh', 100)
    sprite('ta254_04', 20)
    StartMultihit()
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona4Assist():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PKA_AttackInit')
        Unknown2017(0)
        Unknown4007(3)
        Unknown2053(0)

        def upon_STATE_END():
            SLOT_4 = 0
            SLOT_6 = 0
        callSubroutine('PKA_CheckWarp')
    sprite('ta205_00', 6)
    SLOT_4 = 1
    SLOT_6 = 1
    GFX_0('ta_5DThunder', 100)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_01', 6)
    Unknown4007(0)
    sprite('ta205_02', 6)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_03', 5)
    sprite('ta205_04', 5)
    sprite('ta205_05', 3)
    Unknown23029(1, 4081, 0)
    ScreenShake(10000, 0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_06', 2)
    sprite('ta205_07', 1)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    label(819)
    sprite('ta205_06', 1)
    sprite('ta205_05', 2)
    GFX_0('ta_5DThunderTuika', 100)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_06', 1)
    sprite('ta205_07', 2)
    sprite('ta205_06', 1)
    sprite('ta205_07', 2)
    sprite('ta205_06', 1)
    sprite('ta205_07', 2)
    ScreenShake(10000, 0)
    SLOT_51 = (SLOT_51 + 1)
    if (SLOT_51 == 3):
        sendToLabel(0)
    loopRest()
    gotoLabel(819)
    label(0)
    sprite('ta205_07', 5)
    SLOT_6 = 0
    sprite('ta205_06', 5)
    sprite('ta205_05', 5)
    sprite('ta205_04', 5)
    sprite('ta205_03', 5)
    sprite('ta205_02', 5)
    sprite('ta205_01', 5)
    sprite('ta205_00', 25)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000012fdff0000000000000000000000000000000000000000')
        callSubroutine('PKA_SPAttackInit')
        Unknown4007(3)
        Unknown23022(1)
        callSubroutine('PKA_CheckWarp')
    sprite('ta403_07', 4)
    sprite('ta403_08', 1)
    sprite('ta403_09', 2)
    GFX_0('taef_taiden', 100)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 2)
    sprite('ta403_09', 2)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 2)
    sprite('ta403_09', 3)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 3)
    sprite('ta403_09', 3)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 3)
    sprite('ta403_09', 4)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    sprite('ta403_10', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaKushizashiA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('16000000640000006079feff10eb090000000000000000000000000000000000')
        Unknown17012(2, 0, 0)
        callSubroutine('PKA_SPAttackInit')
        AttackLevel_(4)
        Damage(2500)
        AttackP1(100)
        AttackP2(50)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown9310(30)
        Unknown11044(1)
        Unknown11064(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown4007(22)
        callSubroutine('PKA_CheckWarp')
    sprite('ta403_00', 20)
    Unknown20000(1)
    sprite('ta403_00', 5)
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    Unknown11069('ta_NageThunder')
    Unknown11067(1)
    sprite('ta403_03', 3)
    Unknown4007(0)
    sprite('ta403_04', 3)
    sprite('ta403_05', 3)
    sprite('ta403_06', 6)
    sprite('ta403_07', 10)
    sprite('ta403_08', 5)
    GFX_0('ta_NageThunder', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    sprite('ta403_10', 4)
    sprite('ta403_09', 5)
    sprite('ta403_10', 5)
    sprite('ta403_09', 6)
    sprite('ta403_10', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaKushizashiEX():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('16000000640000006079feff10eb090000000000000000000000000000000000')
        Unknown17012(2, 0, 0)
        callSubroutine('PKA_SPAttackInit')
        AttackLevel_(4)
        Damage(3000)
        AttackP1(100)
        AttackP2(50)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown9310(30)
        Unknown11044(1)
        Unknown30065(0)
        Unknown11064(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11091(10)
        Unknown23022(1)
        Unknown4007(22)
        callSubroutine('PKA_CheckWarp')
    sprite('ta403_00', 20)
    Unknown20000(1)
    sprite('ta403_00', 5)
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    Unknown11069('ta_NageThunderEX')
    Unknown11067(1)
    sprite('ta403_03', 3)
    Unknown4007(0)
    sprite('ta403_04', 3)
    sprite('ta403_05', 3)
    sprite('ta403_06', 6)
    sprite('ta403_07', 10)
    sprite('ta403_08', 5)
    GFX_0('ta_NageThunderEX', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    sprite('ta403_10', 4)
    sprite('ta403_09', 5)
    sprite('ta403_10', 5)
    sprite('ta403_09', 6)
    sprite('ta403_10', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaTsukameB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000080841e00c0bdf0ff60ae0a00')
        callSubroutine('PKA_SPAttackInit')
        HitAirUnblockable(4)
        Damage(0)
        AttackP1(80)
        AttackP2(100)
        Hitstop(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11046(1)
        Unknown11044(1)
        Unknown11032('f0490200b03cffff20a1070010b6fdff')
        Unknown11034(1)
        Unknown11033(0)
        Unknown11082(1)
        Unknown4007(3)
        Unknown23027()
        Unknown30048(1)

        def upon_78():
            SLOT_8 = SLOT_12
            SLOT_9 = SLOT_13
            Unknown23029(3, 4041, 0)
            enterState('PKA_PersonaTsukameB_plus')
        SLOT_59 = 1
        SLOT_61 = 0

        def upon_STATE_END():
            SLOT_6 = 0
        SLOT_6 = 1
        callSubroutine('PKA_CheckWarp')
    sprite('ta405_00', 5)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown2006()
    sprite('ta405_01', 3)
    Unknown3029(1)
    Unknown4007(0)
    Unknown2053(1)
    physicsYImpulse(39000)
    Unknown47('030000000200000013000000000000000a000000020000000c000000')
    if (SLOT_12 > 35000):
        physicsXImpulse(35000)
    SFX_3('airdash_m')
    GFX_1('ef_charge_ground', 104)
    sprite('ta405_01', 1)
    RefreshMultihit()
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    Unknown1019(45)
    YAccel(45)
    sprite('ta405_01', 1)
    sprite('ta405_01', 1)
    sprite('ta405_02', 2)
    Unknown3029(0)
    Unknown23027()
    setInvincible(0)
    sprite('ta405_03', 2)
    sprite('ta405_04', 2)
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 5)
    Unknown1019(50)
    YAccel(50)
    sprite('ta405_04', 15)
    Unknown1019(50)
    YAccel(50)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaTsukameB_plus():

    def upon_IMMEDIATE():
        callSubroutine('PKA_SPAttackInit')
        Unknown17011('PKA_PersonaTsukame_Exe', 2, 1, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown30061(1)
        Unknown11002(-1)
        HitAirUnblockable(4)
        Unknown11034(1)
        Unknown11033(0)
        Unknown30048(1)
        callSubroutine('PKA_CheckWarp')
        Unknown23022(1)
    sprite('keep', 1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaTsukame_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 1, 0)
        callSubroutine('PKA_SPAttackInit')
        AttackLevel_(4)
        Damage(550)
        AttackP1(100)
        AttackP2(60)
        Unknown11092(1)
        SLOT_59 = (-1)
        Hitstop(0)
        Unknown30079(1)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11064(1)
        Unknown11057(700)
        Unknown23022(1)
        Unknown2034(1)
        Unknown2053(1)
        SLOT_12 = SLOT_8
        SLOT_13 = SLOT_9
        Unknown23027()
        sendToLabelUpon(2, 0)
        Unknown11068(1)
    sprite('ta405_01', 2)
    SFX_3('grip_hugs')
    SFX_3('bound_marble_m')
    ScreenShake(10000, 0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SLOT_8 = 0
    SLOT_9 = 0
    Unknown1019(30)
    YAccel(30)
    sprite('ta405_02', 2)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_03', 2)
    Unknown1019(45)
    YAccel(45)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)
    Unknown1019(85)
    YAccel(85)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)
    Unknown1019(70)
    YAccel(70)
    sprite('ta405_04', 3)
    Unknown1019(60)
    YAccel(60)
    sprite('ta405_04', 10)
    Unknown1019(0)
    YAccel(0)
    sprite('ta405_04', 3)
    RefreshMultihit()
    SFX_3('electric_l')
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(24000, 0)
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 3)
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)
    RefreshMultihit()
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 3)
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)
    RefreshMultihit()
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(24000, 0)
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 3)
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)
    RefreshMultihit()
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 20)
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(24000, 0)
    sprite('ta405_05', 5)
    Unknown5000(25, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    setGravity(3000)
    physicsYImpulse(21000)
    physicsXImpulse(5000)
    SFX_3('slash_blade_slow')
    sprite('ta405_06', 4)
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_07', 32767)
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('ta405_08', 4)
    SFX_3('down_steal_m')
    SFX_3('bonebroken_h')
    Unknown5000(27, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown1084(1)
    RefreshMultihit()
    AttackLevel_(5)
    Unknown30079(0)
    Unknown11044(1)
    AirPushbackY(-20000)
    AirPushbackX(10000)
    YImpluseBeforeWallbounce(0)
    Unknown9310(20)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown9266(0)
    Unknown11064(0)
    Unknown11058('0000000001000000000000000000000000000000')
    AirHitstunAnimation(11)
    ScreenShake(0, 80000)
    sprite('ta405_09', 40)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaKurokoge():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000e05ef8ff0000000000000000000000000000000000000000')
        callSubroutine('PKA_DDAttackInit')
        Unknown17011('PKA_PersonaKurokoge_Exe', 3, 1, 0)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11046(0)
        Unknown11034(1)
        Unknown11033(0)
        Unknown4007(3)
        Unknown23022(1)
        Unknown3032()
        Unknown3001(50)
        Unknown3004(20)

        def upon_3():
            if SLOT_51:
                pass
        SLOT_61 = 0
    sprite('ta432_00', 42)
    SFX_3('electric_l')
    Unknown20000(1)
    Unknown2017(1)
    GFX_0('taef432_wait', 1)
    sprite('ta432_01', 5)
    SFX_3('electric_l')
    SFX_3('airdash_m')
    physicsXImpulse(90000)
    SLOT_51 = 1
    GFX_0('taef432_push', 1)
    Unknown38(4, 1)
    sprite('ta432_02', 30)
    RefreshMultihit()
    Unknown13(4)
    GFX_0('taef432_push', 1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()

@State
def PKA_PersonaKurokoge_Exe():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PKA_DDAttackInit')
        Unknown17012(3, 0, 0)
        AttackLevel_(5)
        Damage(1000)
        AttackP2(100)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown30079(1)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11064(1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        physicsXImpulse(60000)
        Unknown2034(1)
        Unknown2053(1)
        Unknown2017(1)

        def upon_STATE_END():
            SLOT_61 = 0

        def upon_3():
            if SLOT_51:
                pass
            SLOT_58 = SLOT_25
            if (SLOT_25 < 515000):
                clearUponHandler(3)
                sendToLabel(3)
    sprite('ta432_02', 1)
    SFX_3('grip_hugs')
    SLOT_51 = 1
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('taef432_push', 1)
    Unknown38(4, 1)
    loopRest()
    sprite('ta432_02', 180)
    loopRest()
    label(3)
    sprite('ta432_03', 2)
    Unknown1084(1)
    Unknown21015('4b75726f6b6f67655f4578650000000000000000000000000000000000000000da10000000000000')
    Unknown20000(1)
    SFX_3('down_steal_m')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SLOT_51 = 0
    Unknown13(4)
    GFX_1('taef_spthrow_smash', 1)

    def upon_3():
        SLOT_58 = SLOT_25
        Unknown2038(1)
        SLOT_57 = SLOT_2
    sprite('ta432_04', 2)
    SFX_3('electric_m')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    ScreenShake(0, 34000)
    GFX_0('taef432_hold', 1)
    Unknown38(5, 1)
    sprite('ta432_04', 8)
    sprite('ta432_05', 40)
    SFX_3('electric_m')
    SFX_3('quake_l')
    Unknown21015('4b75726f6b6f67655f4578650000000000000000000000000000000000000000d910000000000000')
    sprite('ta432_06', 8)
    SFX_3('electric_m')
    ScreenShake(0, 5000)
    sprite('ta432_06', 8)
    SFX_3('electric_m')
    ScreenShake(0, 10000)
    sprite('ta432_06', 8)
    SFX_3('electric_m')
    ScreenShake(0, 15000)
    sprite('ta432_06', 8)
    SFX_3('electric_m')
    ScreenShake(0, 20000)
    sprite('ta432_06', 8)
    SFX_3('electric_m')
    ScreenShake(0, 25000)
    sprite('ta432_06', 8)
    SFX_3('electric_m')
    ScreenShake(0, 30000)
    sprite('ta432_06', 3)
    SFX_3('electric_m')
    sprite('ta432_06', 6)
    ScreenShake(0, 40000)
    sprite('ta432_05', 1)
    ScreenShake(0, 50000)
    SFX_3('bomb_l')
    SFX_3('bonebroken_h')
    RefreshMultihit()
    Damage(3200)
    if SLOT_7:
        Damage(4200)
    AttackP2(60)
    Unknown30079(0)
    Unknown9346(1)
    Unknown9362(1)
    Unknown9364(40)
    Unknown9178(1)
    AirHitstunAfterWallbounce(100)
    AirPushbackX(100000)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(2000)
    AirHitstunAnimation(12)
    Unknown11064(0)
    Unknown11072(1, 345000, 120000)
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(34000, 0)
    Unknown13(5)
    GFX_1('taef_spthrow_finish', 1)
    Unknown21015('4b75726f6b6f67655f4578650000000000000000000000000000000000000000db10000000000000')
    sprite('ta432_05', 40)
    sprite('ta432_05', 30)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaKenkaOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('16000000640000006079feff10eb090000000000000000000000000000000000')
        Unknown2011()
        Unknown17012(2, 0, 0)
        callSubroutine('PKA_DDAttackInit')
        AttackLevel_(5)
        Damage(1000)
        AttackP2(100)
        Unknown11091(25)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown9310(30)
        Unknown11044(1)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11069('ta_NageThunderOD')
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown4007(22)
        callSubroutine('PKA_CheckWarp')
    sprite('ta403_00', 20)
    sprite('ta403_00', 5)
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    sprite('ta403_03', 3)
    Unknown4007(0)
    sprite('ta403_04', 3)
    sprite('ta403_05', 3)
    sprite('ta403_06', 3)
    sprite('ta403_07', 5)
    sprite('ta403_08', 4)
    GFX_0('ta_NageThunderOD', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    sprite('ta403_10', 4)
    sprite('ta403_09', 5)
    sprite('ta403_10', 5)
    sprite('ta403_09', 6)
    sprite('ta403_10', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PKA_PersonaKenkaOD_DUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('16000000640000006079feff10eb090000000000000000000000000000000000')
        Unknown2011()
        Unknown17012(2, 0, 0)
        callSubroutine('PKA_DDAttackInit')
        AttackLevel_(5)
        Damage(250)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown9310(30)
        Unknown11044(1)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11069('ta_NageThunderOD_DUO')
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown4007(22)
        callSubroutine('PKA_CheckWarp')
    sprite('ta403_00', 20)
    sprite('ta403_00', 5)
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    sprite('ta403_03', 3)
    Unknown4007(0)
    sprite('ta403_04', 3)
    sprite('ta403_05', 3)
    sprite('ta403_06', 3)
    sprite('ta403_07', 5)
    sprite('ta403_08', 4)
    GFX_0('ta_NageThunderOD_DUO', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)
    sprite('ta403_09', 4)
    sprite('ta403_10', 4)
    sprite('ta403_09', 5)
    sprite('ta403_10', 5)
    sprite('ta403_09', 6)
    sprite('ta403_10', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def fukidashi():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Hitstop(5)
        AttackP1(100)
        PushbackX(5000)
        AirPushbackY(10000)
        AirHitstunAnimation(11)
        Unknown9324(0)
        Unknown23078(1)
        Unknown4009(2)
        Unknown4011(2)

        def upon_12():
            SFX_3('ka001_a')
    sprite('vr_ka203_col', 5)
    ScreenShake(10000, 10000)
    GFX_0('fukidashi_bg', 100)
    if (not SLOT_168):
        GFX_0('fukidashi_font', 100)
    else:
        GFX_0('fukidashi_font_e', 100)
    sprite('vr_ka203_col', 15)
    StartMultihit()

@State
def fukidashi_Tame():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Unknown9154(21)
        Hitstop(0)
        PushbackX(0)
        Unknown9216(-6000)
        AirPushbackY(10000)
        GroundedHitstunAnimation(0)
        Unknown4009(2)
        Unknown4011(2)

        def upon_12():
            SFX_3('ka001_a')
        Unknown1064(1250)
        Unknown1056(1300)
    sprite('vr_ka203_col', 5)
    ScreenShake(10000, 10000)
    GFX_0('fukidashi_bg', 100)
    Unknown23029(1, 2030, 0)
    if (not SLOT_168):
        GFX_0('fukidashi_font', 100)
        Unknown23029(1, 2030, 0)
    else:
        GFX_0('fukidashi_font_e', 100)
        Unknown23029(1, 2030, 0)
    sprite('vr_ka203_col', 15)
    StartMultihit()

@State
def fukidashi_bg():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown2007()

        def upon_43():
            if (SLOT_48 == 2030):
                clearUponHandler(43)
                Unknown1096(1200)
    sprite('vr_ka203_00', 1)
    sprite('vr_ka203_00', 1)
    sprite('vr_ka203_01', 2)
    sprite('vr_ka203_00', 2)
    sprite('vr_ka203_01', 3)
    sprite('vr_ka203_00', 3)
    Unknown1099(10)
    Unknown3004(-15)
    sprite('vr_ka203_01', 4)
    sprite('vr_ka203_00', 4)
    sprite('vr_ka203_01', 5)
    sprite('vr_ka203_00', 5)

@State
def fukidashi_font():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown2007()

        def upon_43():
            if (SLOT_48 == 2030):
                clearUponHandler(43)
                Unknown1096(1200)
    sprite('vr_ka203_10', 3)
    Unknown1007(32000)
    sprite('vr_ka203_10', 1)
    Unknown1007(-32000)
    teleportRelativeX(-16000)
    sprite('vr_ka203_10', 2)
    sprite('vr_ka203_10', 3)
    sprite('vr_ka203_10', 4)
    Unknown3004(-15)
    Unknown1007(16000)
    teleportRelativeX(-32000)
    sprite('vr_ka203_10', 4)
    sprite('vr_ka203_10', 5)
    Unknown1007(-32000)
    teleportRelativeX(32000)
    sprite('vr_ka203_10', 5)

@State
def fukidashi_font_e():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown2007()

        def upon_43():
            if (SLOT_48 == 2030):
                clearUponHandler(43)
                Unknown1096(1200)
    sprite('vr_ka203_11', 3)
    Unknown1007(32000)
    sprite('vr_ka203_11', 1)
    Unknown1007(-32000)
    teleportRelativeX(-16000)
    sprite('vr_ka203_11', 2)
    sprite('vr_ka203_11', 3)
    sprite('vr_ka203_11', 4)
    Unknown3004(-15)
    Unknown1007(16000)
    teleportRelativeX(-32000)
    sprite('vr_ka203_11', 4)
    sprite('vr_ka203_11', 5)
    Unknown1007(-32000)
    teleportRelativeX(32000)
    sprite('vr_ka203_11', 5)

@State
def IsuBreak():
    sprite('null', 1)
    GFX_0('IsuBreakParts1', 100)
    GFX_0('IsuBreakParts2', 100)
    GFX_0('IsuBreakParts3', 100)
    SFX_3('ka004')

@State
def IsuBreakParts1():
    sprite('vr_ka401_00', 20)
    setGravity(2000)
    physicsXImpulse(4000)
    physicsYImpulse(25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(-25000)
    Unknown3007(170)
    Unknown3019(170)
    Unknown3013(170)
    sprite('keep', 30)
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts2():
    sprite('vr_ka401_01', 20)
    setGravity(2000)
    physicsXImpulse(-4000)
    physicsYImpulse(25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)
    Unknown3007(170)
    Unknown3019(170)
    Unknown3013(170)
    sprite('keep', 30)
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts3():
    sprite('vr_ka401_02', 20)
    setGravity(2000)
    physicsXImpulse(1000)
    physicsYImpulse(30000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)
    Unknown3007(170)
    Unknown3019(170)
    Unknown3013(170)
    sprite('keep', 30)
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts1ex():
    sprite('vr_ka401_00', 2)
    Unknown2054(1)
    teleportRelativeX(3000)
    Unknown1007(3000)
    sprite('vr_ka401_00', 2)
    teleportRelativeX(-3000)
    Unknown1007(-3000)
    sprite('vr_ka401_00', 20)
    setGravity(2000)
    physicsXImpulse(8000)
    physicsYImpulse(-25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(-25000)

    def upon_LANDING():
        YAccel(-95)
    sprite('keep', 30)
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts2ex():
    sprite('vr_ka401_01', 2)
    Unknown2054(1)
    teleportRelativeX(3000)
    Unknown1007(-3000)
    sprite('vr_ka401_01', 2)
    teleportRelativeX(-3000)
    Unknown1007(3000)
    sprite('vr_ka401_01', 20)
    setGravity(2000)
    physicsXImpulse(-8000)
    physicsYImpulse(-25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)

    def upon_LANDING():
        YAccel(-95)
    sprite('keep', 30)
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts3ex():
    sprite('vr_ka401_02', 2)
    Unknown2054(1)
    teleportRelativeX(-3000)
    Unknown1007(-3000)
    sprite('vr_ka401_02', 2)
    teleportRelativeX(3000)
    Unknown1007(3000)
    sprite('vr_ka401_02', 20)
    setGravity(2000)
    physicsXImpulse(2000)
    physicsYImpulse(-30000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)

    def upon_LANDING():
        YAccel(-95)
    sprite('keep', 30)
    Unknown3004(-20)
    Unknown3032()

@State
def ta_5C_zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_ta204_00', 3)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('vr_ta204_01', 30)
    GFX_1('taef_stand_c_clash', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    GFX_1('taef_thunderbolt', 3)

@State
def taef_Air5C_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown3004(-25)
    sprite('vr_ta254_00', 16)

@State
def ka_isuyoko_assist():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown3029(1)
        Unknown2010()
        AttackLevel_(3)
        Damage(1300)
        AttackP1(70)
        Unknown11092(1)
        AirUntechableTime(32)
        Unknown9310(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(28000)
        YImpluseBeforeWallbounce(1500)
        Unknown11042(1)
        PushbackX(23000)
        physicsXImpulse(70000)
        Unknown23089('0200000001000000010000000100000001000000000000000000000000000000')
        sendToLabelUpon(54, 44)

        def upon_LANDING():
            GFX_0('IsuBreak', 100)
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 4303):

                def upon_ON_HIT_OR_BLOCK():
                    physicsXImpulse(8000)
                    clearUponHandler(10)
                    Unknown26('kaef_conbo_chair')
                    Unknown26('kaef_chairthrow')
                    sendToLabel(33)
        loopRelated(17, 600)

        def upon_17():
            Unknown13(25)
    sprite('vr_ka430_00', 3)
    GFX_0('kaef_chairthrow', 0)
    RefreshMultihit()
    Unknown53(0)
    teleportRelativeX(-70000)
    sprite('vr_ka430_00', 1)
    Unknown53(1)
    label(0)
    sprite('vr_ka430_00', 1)
    loopRest()
    gotoLabel(0)
    label(33)
    sprite('vr_ka430_01', 3)
    Unknown9215()
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsXImpulse(15000)
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 15)
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    AttackLevel_(3)
    Hitstop(6)
    AirUntechableTime(50)
    Unknown9071()
    AirPushbackY(-12000)
    YImpluseBeforeWallbounce(2000)
    Unknown11032('40420f006079feffffffffffffffffff')
    loopRest()
    ExitState()
    label(44)
    sprite('null', 1)
    GFX_0('IsuBreak', 100)

@State
def ta_5DThunder():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(900)
        AttackP1(70)
        AttackP2(95)
        PushbackX(5000)
        AirPushbackX(2000)
        AirPushbackY(35000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(40)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11042(1)
        Unknown2053(1)
        Unknown3033()
        Unknown4061(3)
        Unknown1056(2000)
        Unknown1064(4000)

        def upon_43():
            if (SLOT_48 == 4081):
                sendToLabel(1)
    sprite('null', 3)
    teleportRelativeX(300000)
    GFX_0('ta_ThunderFall_bigen', 100)
    label(0)
    sprite('null', 3)
    gotoLabel(0)
    label(1)
    sprite('vr_ta205_col', 5)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('null', 15)
    GFX_0('ta_ThunderFall', 100)

@State
def ta_5DThunderTuika():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(900)
        AttackP1(70)
        AttackP2(95)
        PushbackX(5000)
        AirPushbackX(2000)
        AirPushbackY(35000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(40)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11042(1)
        Unknown2053(1)
        Unknown3033()
        Unknown4061(3)
        Unknown1056(2000)
        Unknown1064(4000)
    sprite('vr_ta205_col', 5)
    SFX_3('thunder_s')
    teleportRelativeX(300000)
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('null', 15)
    GFX_0('ta_ThunderFall', 100)

@State
def taiden():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(2)
    sprite('vr_ka400_00', 2)
    sprite('null', 2)
    sprite('vr_ka400_00', 2)
    sprite('null', 2)
    sprite('vr_ka400_00', 3)
    sprite('null', 3)
    sprite('vr_ka400_00', 4)
    sprite('null', 4)

@State
def taef_taiden():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
    sprite('vr_ta400_00', 2)
    Unknown3001(255)
    sprite('vr_ta400_00', 2)
    Unknown3001(0)
    sprite('vr_ta400_00', 2)
    Unknown3001(255)
    sprite('vr_ta400_00', 2)
    Unknown3001(0)
    sprite('vr_ta400_00', 2)
    Unknown3001(255)
    sprite('vr_ta400_00', 2)
    Unknown3001(0)
    sprite('vr_ta400_00', 2)
    Unknown3001(255)
    sprite('vr_ta400_00', 2)
    Unknown3001(0)
    sprite('vr_ta400_00', 2)
    Unknown3001(255)
    sprite('vr_ta400_00', 2)
    Unknown3001(0)

@State
def KandenAtkObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown10001(3)
        Unknown11032('ffffffffffffffffffffffffffffffff')
    sprite('null', 1)
    Unknown4010(3)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('vr_atk_dmy', 30)

    def upon_3():
        Unknown23151(22, 103)
    RefreshMultihit()

@State
def ta_NageThunder():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(3)
        Damage(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackY(5000)
        Hitstop(3)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        Unknown9310(15)
        Unknown9021(1)
        Unknown9266(7)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_l')
    RefreshMultihit()
    ScreenShake(20000, 20000)
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)

@State
def ta_NageThunderEX():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(3)
        Damage(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackY(5000)
        Hitstop(3)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        Unknown9310(15)
        Unknown11044(1)
        Unknown9021(1)
        Unknown9266(7)
        Unknown30065(0)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_l')
    RefreshMultihit()
    ScreenShake(20000, 20000)
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)

@State
def ta_NageThunderOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown17012(2, 0, 0)
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(25)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(5000)
        Hitstop(15)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        Unknown9310(110)
        Unknown11044(1)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11069('ka_isuokiseme')
        Unknown1096(1500)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_l')
    RefreshMultihit()
    ScreenShake(20000, 20000)
    GFX_0('ta_ThunderFall', 100)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()

@State
def ta_NageThunderOD_DUO():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown17012(2, 0, 0)
        AttackLevel_(5)
        Damage(250)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(5000)
        Hitstop(15)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        Unknown9310(110)
        Unknown11044(1)
        Unknown9021(1)
        Unknown9266(7)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11069('ka_isuokiseme')
        Unknown1096(1500)
    sprite('vr_ta403_col', 3)
    SFX_3('thunder_l')
    RefreshMultihit()
    ScreenShake(20000, 20000)
    GFX_0('ta_ThunderFall', 100)
    Unknown36(1)
    Unknown1096(1500)
    Unknown35()

@State
def ta_ThunderFall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
        Unknown2019(-100)
    sprite('vr_ta205_00', 2)
    GFX_1('taef_thunderfall', 100)
    sprite('vr_ta205_01', 2)
    sprite('vr_ta205_02', 2)
    sprite('vr_ta205_03', 2)
    sprite('vr_ta205_00', 2)
    sprite('vr_ta205_01', 2)
    sprite('vr_ta205_02', 2)
    sprite('vr_ta205_03', 2)

@State
def ta_ThunderFall_bigen():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
        Unknown2019(-100)
        Unknown3001(0)
        Unknown2007()
    sprite('vr_ta205_10', 2)
    GFX_1('taef_thunderfall_target', 100)
    sprite('vr_ta205_11', 2)
    sprite('vr_ta205_12', 2)
    sprite('vr_ta205_13', 2)

@State
def ta_AntiAir():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
    sprite('vr_ta405_00', 6)

@State
def __406isumove():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        teleportRelativeX(-100000)
        Unknown1007(300000)
        physicsXImpulse(-5000)
        physicsYImpulse(7000)
        setGravity(2000)
        Unknown1074(-25000)

        def upon_LANDING():
            GFX_0('IsuBreak', 100)
            Unknown13(25)
    sprite('vr_ka406_00', 32767)

@State
def kaef407_atk1():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34303761746b312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3032()
    sprite('null', 6)
    Unknown3004(80)
    sprite('null', 4)
    Unknown3004(-70)

@State
def kaef407_atk2():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34303761746b322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3032()
    sprite('null', 6)
    Unknown3004(80)
    sprite('null', 4)
    Unknown3004(-70)

@State
def kaef407_atk3():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34303761746b322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3032()
    sprite('null', 6)
    Unknown3004(80)
    sprite('null', 4)
    Unknown3004(-70)

@State
def ka_isuyoko():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown3029(1)
        Unknown2011()
        AttackLevel_(3)
        AttackP2(60)
        Unknown11092(1)
        AirUntechableTime(77)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(25000)
        YImpluseBeforeWallbounce(1500)
        physicsXImpulse(70000)
        Unknown23089('0200000001000000010000000100000001000000000000000000000000000000')
        sendToLabelUpon(54, 44)

        def upon_LANDING():
            GFX_0('IsuBreak', 100)
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 4303):

                def upon_ON_HIT_OR_BLOCK():
                    physicsXImpulse(8000)
                    clearUponHandler(10)
                    Unknown26('kaef_conbo_chair')
                    Unknown26('kaef_chairthrow')
                    sendToLabel(33)
        loopRelated(17, 600)

        def upon_17():
            Unknown13(25)
    sprite('vr_ka430_00', 3)
    GFX_0('kaef_chairthrow', 0)
    RefreshMultihit()
    sprite('vr_ka430_00', 1)
    Unknown53(1)
    label(0)
    sprite('vr_ka430_00', 1)
    loopRest()
    gotoLabel(0)
    label(33)
    sprite('vr_ka430_01', 3)
    Unknown2053(1)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 20)
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    AttackLevel_(3)
    Hitstop(6)
    AirUntechableTime(77)
    AirPushbackY(-12000)
    YImpluseBeforeWallbounce(2000)
    loopRest()
    ExitState()
    label(66)
    sprite('vr_ka430_01', 3)
    Unknown2053(1)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 20)
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    AttackLevel_(3)
    Hitstop(6)
    AirUntechableTime(77)
    AirPushbackY(-12000)
    YImpluseBeforeWallbounce(2000)
    loopRest()
    ExitState()
    label(44)
    sprite('null', 1)
    GFX_0('IsuBreak', 100)

@State
def ka_isuyamanari():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown3029(1)
        Unknown2011()
        AttackLevel_(3)
        Hitstop(6)
        AirUntechableTime(77)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(-12000)
        YImpluseBeforeWallbounce(2000)
        physicsXImpulse(70000)
        Unknown23089('0100000001000000010000000100000001000000000000000000000000000000')
        sendToLabelUpon(54, 44)

        def upon_LANDING():
            GFX_0('IsuBreak', 100)
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 4303):
                sendToLabel(33)
            if (SLOT_48 == 4307):
                sendToLabel(77)
    label(33)
    sprite('vr_ka430_01', 3)
    physicsXImpulse(3000)
    Unknown23027()
    Unknown2053(1)
    Unknown53(0)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 20)
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    loopRest()
    ExitState()
    label(66)
    sprite('vr_ka430_01', 3)
    physicsXImpulse(3000)
    Unknown23027()
    Unknown2053(1)
    Unknown53(0)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 36)
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    loopRest()
    ExitState()
    label(77)
    sprite('vr_ka430_01', 3)
    Unknown23027()
    Unknown2053(0)
    Unknown26('kaef_conbo_chair')
    physicsXImpulse(15000)
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 15)
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    Unknown11032('40420f006079feffffffffffffffffff')
    loopRest()
    ExitState()
    label(44)
    sprite('null', 1)
    GFX_0('IsuBreak', 100)

@State
def kaef_chairthrow():

    def upon_IMMEDIATE():
        Unknown23067('kaef_chairthrow')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 60)

@State
def ka_isuokiseme():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(0)
        AirPushbackX(18000)
        AirPushbackY(-30000)
        YImpluseBeforeWallbounce(1500)
        physicsXImpulse(5000)
        physicsYImpulse(70000)
        Unknown1074(25000)
        Unknown23027()
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 1)

        def upon_43():
            if (SLOT_48 == 4302):
                Unknown23090(25)
            if (SLOT_48 == 4303):
                sendToLabel(33)
            if (SLOT_48 == 4304):
                sendToLabel(66)
            if (SLOT_48 == 4307):
                Unknown30070('6b615f6973756f6b6973656d655f445344000000000000000000000000000000')
                sendToLabel(77)
            if (SLOT_48 == 4305):
                Unknown30048(1)
                Damage(100)
                Unknown11091(25)
                AttackP2(60)
                sendToLabel(99)
            if (SLOT_48 == 4306):
                Unknown30048(1)
                Damage(200)
                Unknown11091(100)
                AttackP1(100)
                AttackP2(100)
    label(33)
    sprite('vr_ka430_01', 171)
    sprite('vr_ka430_01', 1)
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(500000)
    teleportRelativeX(30000)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    Damage(100)
    AttackP2(60)
    AirUntechableTime(30)
    AirPushbackX(3000)
    AirPushbackY(-20000)
    physicsYImpulse(-60000)
    setGravity(0)
    Unknown1074(15000)
    sendToLabelUpon(2, 1)
    loopRest()
    ExitState()
    label(66)
    sprite('vr_ka430_01', 252)
    sprite('vr_ka430_01', 1)
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(2000000)
    teleportRelativeX(-100000)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    physicsYImpulse(-60000)
    setGravity(0)
    Unknown1074(15000)
    sendToLabelUpon(2, 1)
    loopRest()
    ExitState()
    label(77)
    sprite('vr_ka430_01', 171)
    sprite('vr_ka430_01', 1)
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(500000)
    teleportRelativeX(30000)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    AirUntechableTime(30)
    AirPushbackX(3000)
    AirPushbackY(-20000)
    physicsYImpulse(-60000)
    setGravity(0)
    Unknown1074(15000)
    sendToLabelUpon(2, 1)
    loopRest()
    ExitState()
    label(99)
    sprite('vr_ka430_01', 252)
    sprite('vr_ka430_01', 1)
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(2000000)
    teleportRelativeX(0)
    sprite('vr_ka430_01', 32767)
    RefreshMultihit()
    physicsYImpulse(-60000)
    setGravity(0)
    Unknown1074(15000)
    sendToLabelUpon(2, 1)
    Unknown9310(25)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 1)
    GFX_0('IsuBreak', 100)

@State
def kaef430_atk1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown1096(1100)
        Unknown3004(-25)
    sprite('vr_ka430_10', 12)
    sprite('vr_ka430_10', 18)

@State
def kaef430_atkline1():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34333061746b312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown1096(1050)
        Unknown3032()
    sprite('null', 6)
    sprite('null', 5)
    Unknown3004(-60)

@State
def kaef430_atk3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3033()
        Unknown4061(2)
        Unknown1056(1600)
        Unknown1064(1500)
        Unknown3004(-25)
    sprite('vr_ka430_20', 10)
    sprite('vr_ka430_20', 20)

@State
def kaef430_atkline3():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34333061746b332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown1096(1550)
    sprite('null', 12)
    sprite('null', 6)
    Unknown3004(-50)

@State
def taef432_wait():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23067('taef_spthrow_wait')
    sprite('null', 42)

@State
def taef432_push():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23067('taef_spthrow_push')
    sprite('null', 32767)

@State
def taef432_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23067('taef_spthrow_hold')
    sprite('null', 32767)

@State
def KurokogeCamera1():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 4311):
                sendToLabel(0)
            if (SLOT_48 == 4312):
                sendToLabel(1)
    label(0)
    sprite('keep', 32767)
    Unknown1086(22)
    Unknown20000(1)
    Unknown20003(1)
    teleportRelativeY(0)
    label(1)
    sprite('keep', 70)
    Unknown1086(22)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20001(1)
    physicsYImpulse(60000)

@State
def PKA_PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('1600000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PKA_DDAttackInit')
        Unknown2012()
        Damage(0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Hitstop(0)
        Unknown11001(20, 200, 200)
        AirUntechableTime(10000)
        Unknown9266(7)
        Unknown11064(1)
        Unknown4007(22)
        sendToLabelUpon(39, 0)
        callSubroutine('PKA_CheckWarp')
    sprite('ta450_00', 10)
    Unknown1007(1500000)
    SFX_3('electric_m')
    GFX_0('kaef_ichigeki_BG00', 103)
    sprite('ta450_00', 10)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    Unknown26('SCEF_FadeBlack12In')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_0('ta450_charge', 100)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_01', 3)
    GFX_0('ta450_Light2', 100)
    GFX_0('ta450_Throw', 100)
    SFX_3('slash_blade_middle')
    sprite('ta450_02', 3)
    Unknown26('SCEF_FadeBlack12In')
    sprite('ta450_03', 8)
    sprite('ta450_03', 2)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000022000000')
    sprite('keep', 10)
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown26('SCEF_FadeBlack12In')
    Unknown21012('6b6165665f6963686967656b695f42473030000000000000000000000000000024000000')
    sprite('vr_ta403_col', 4)
    SFX_3('thunder_l')
    RefreshMultihit()
    Unknown11023(1)
    sprite('keep', 32767)
    label(0)
    sprite('ta450_04', 18)
    clearUponHandler(39)
    Unknown4007(0)
    Unknown1000(350000)
    teleportRelativeY(600000)
    physicsYImpulse(-20000)
    sprite('ta450_04', 12)
    sprite('ta450_05', 8)
    SFX_3('down_steal_m')
    physicsYImpulse(0)
    ScreenShake(10000, 25000)
    sprite('ta450_06', 15)
    ScreenShake(10000, 10000)
    sprite('ta450_06', 20)
    sprite('ta450_07', 5)
    sprite('ta450_08', 10)
    sprite('ta450_09', 30)
    sprite('ta450_10', 6)
    sprite('ta450_11', 6)
    SFX_3('chain_snap')
    GFX_0('ta450_PunchAura', 0)
    sprite('ta450_12', 15)
    sprite('ta450_12', 100)
    Unknown23130(0, 30, 1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def ta450_charge():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('6b6165665f3435305f6368617267655f303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3033()
        Unknown4061(3)
    sprite('vr_ta450_00', 80)
    Unknown3001(0)
    Unknown3004(4)
    sprite('vr_ta450_01', 3)

@State
def ta450_Throw():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4003('6b6165665f3435305f7468756e6465725f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1000(100000)
    sprite('null', 7)
    GFX_0('ta450_RandThrowMato', 100)
    sprite('null', 5)
    Unknown3004(-51)
    Unknown1059(-300)

@State
def ta450_RandThrowMato():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 2)
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow01', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow01', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow01', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)
    GFX_0('ta450_RandThrow01', 100)

@State
def ta450_RandThrow00():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 5)
    Unknown4003('6b6165665f3435305f7468756e6465725f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3032()
    Unknown1062(-500, 500)
    Unknown1010(-200000, 0)
    Unknown1059(-100)
    Unknown1067(300)
    Unknown3004(-51)

@State
def ta450_RandThrow01():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 5)
    Unknown4003('6b6165665f3435305f7468756e6465725f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4015()
    Unknown3032()
    Unknown1062(-500, 500)
    Unknown1010(0, 200000)
    Unknown1059(-200)
    Unknown1067(300)
    Unknown3004(-51)

@State
def ta450_ThrowYugami():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(3500)
        Unknown2054(1)
    sprite('vr_ka_yugami_00', 10)
    Unknown1059(40)
    sprite('vr_ka_yugami_00', 5)
    Unknown3004(-17)
    loopRest()

@State
def ta450_Thunder():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown3032()
    sprite('null', 10)
    sprite('null', 2)
    GFX_0('ta450_ThunderFlash', 100)
    SFX_3('thunder_s')
    sprite('null', 5)
    Unknown4003('6b6165665f3435305f7468756e6465725f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('ta450_RandThrowMato', 100)
    Unknown4015()
    SFX_3('damage_slash_m')
    sprite('null', 5)
    Unknown1059(-200)
    GFX_1('taef_tatethundershock_03', 100)
    GFX_0('ta450_ThunderShock', 100)
    GFX_0('ta450_ThunderShock2', 100)
    sprite('null', 15)
    Unknown3004(-51)

@State
def ta450_ThunderFlash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23015(1)
        Unknown4061(2)
        Unknown2054(1)
        Unknown1096(1500)
        Unknown3033()
    sprite('vr_ta450_white', 15)
    Unknown3001(50)

@State
def ta450_Light():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f6c696768745f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1000(100000)
    sprite('null', 30)
    sprite('null', 20)
    Unknown3004(26)
    sprite('null', 30)
    Unknown3004(-9)

@State
def ta450_Light2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f6c696768745f30302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1056(1500)
        Unknown1000(150000)
    sprite('null', 10)
    Unknown3004(26)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ta450_ThunderShock():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f666c6173682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
    sprite('null', 10)
    Unknown1099(100)
    Unknown3004(-17)
    sprite('null', 5)

@State
def ta450_ThunderShock2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f666c617368322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
    sprite('null', 3)
    sprite('null', 10)
    Unknown3004(-17)
    sprite('null', 5)

@State
def ka450_PunchAura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f70756e6368617572615f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1000(180000)
    sprite('null', 5)
    Unknown3004(51)
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')

@State
def ta450_PunchAura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f70756e6368617572615f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown2005()
        Unknown3001(0)
        Unknown1000(180000)
    sprite('null', 5)
    Unknown3004(51)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 3)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')
    sprite('null', 5)
    SFX_3('electric_m')

@State
def ka450_PunchBom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 10)
    ScreenShake(6000, 6000)
    GFX_2('kaef_lastpunch_10')
    sprite('null', 10)
    ScreenShake(7000, 7000)
    sprite('null', 10)
    ScreenShake(7000, 7000)
    sprite('null', 10)
    ScreenShake(8000, 8000)
    sprite('null', 10)
    ScreenShake(8000, 8000)
    sprite('null', 10)
    ScreenShake(9000, 9000)
    sprite('null', 10)
    ScreenShake(9000, 9000)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    sprite('null', 10)
    ScreenShake(11000, 11000)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)
    sprite('null', 10)

@State
def ta450_Black():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23015(1)
        Unknown2019(-100)
        Unknown4061(2)
    sprite('vr_ta450_white', 160)
    Unknown3026(-16777216)
    sprite('vr_ta450_white', 10)
    Unknown3001(230)

@State
def UltimateThrowCamera():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    label(0)
    sprite('keep', 32767)
    Unknown1086(22)
    Unknown20000(1)
    Unknown20003(1)
    teleportRelativeY(0)
    label(1)
    sprite('keep', 70)
    Unknown1086(22)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20001(1)
    physicsYImpulse(60000)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
    label(0)
    sprite('keep', 32767)
    Unknown1086(3)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(1)
    sprite('keep', 10)
    physicsYImpulse(30000)
    sprite('keep', 7)
    Unknown4004('534345465f41737452797568616955707065720000000000000000000000000064000000')
    sprite('keep', 15)
    sprite('keep', 5)
    Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
    sprite('keep', 10)
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    physicsYImpulse(100000)
    sprite('keep', 5)
    Unknown20009(1300)
    teleportRelativeY(3800000)
    Unknown1000(0)
    Unknown1084(1)
    Unknown21007(3, 40)
    sprite('keep', 3)
    Unknown26('SCEF_AstRyuhaiUpper')
    sprite('keep', 3)
    Unknown4004('534345465f5368617368614f757400000000000000000000000000000000000064000000')
    sprite('keep', 5)
    sprite('keep', 32767)
    Unknown26('SCEF_ShashaIn')
    Unknown1084(1)
    label(2)
    sprite('keep', 70)
    Unknown20001(1)
    Unknown20009(1000)
    Unknown1007(-1500000)
    Unknown20007(1)
    GFX_0('ta450_Thunder', 100)
    GFX_0('ta450_Light', 100)
    sprite('keep', 10)
    Unknown4004('534345465f527975686169596f6b6f000000000000000000000000000000000064000000')
    sprite('keep', 60)
    sprite('keep', 32767)
    label(3)
    sprite('keep', 32767)
    Unknown4007(0)
    Unknown1086(3)
    teleportRelativeX(300000)
    Unknown1007(300000)
    Unknown1084(1)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20002(1)
    Unknown20003(1)
    label(4)
    sprite('keep', 1)

@State
def IchigekiPicture1():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown2019(-1000)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(0)
        Unknown1000(1280000)
        Unknown3001(0)
    sprite('null', 14)
    sprite('ichigeki0', 16)
    physicsXImpulse(-80000)
    Unknown3004(9)
    sprite('ichigeki0', 32767)
    physicsXImpulse(0)

@State
def IchigekiPicture2():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown2019(-1000)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(1)
        Unknown1000(-1280000)
        Unknown3001(0)
    sprite('null', 14)
    sprite('ichigeki1', 16)
    physicsXImpulse(80000)
    Unknown3004(9)
    sprite('ichigeki1', 32767)
    physicsXImpulse(0)

@State
def IchigekiPicture3():

    def upon_IMMEDIATE():
        Unknown2019(0)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(7)
        Unknown1000(0)
    sprite('vr_ka450_99c', 100)
    sprite('vr_ka450_99c', 1)
    Unknown21007(3, 41)

@State
def IchigekiPicture4():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown23015(4)
        Unknown2019(-1000)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(3)
        Unknown1000(0)
        Unknown1056(1070)
    sprite('null', 10)
    GFX_0('IchigekiPicture6', 0)
    sprite('vr_ka450_30', 4)
    GFX_0('IchigekiPicture5', 0)
    sprite('vr_ka450_31', 4)
    sprite('vr_ka450_32', 4)
    sprite('null', 15)
    sprite('vr_ka450_33', 4)
    sprite('vr_ka450_30', 4)
    sprite('null', 15)
    sprite('vr_ka450_31', 4)
    sprite('vr_ka450_32', 4)
    sprite('null', 15)
    sprite('vr_ka450_33', 4)
    sprite('vr_ka450_30', 4)

@State
def IchigekiPicture5():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown23015(4)
        Unknown2019(-1000)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(3)
        Unknown1000(0)
        Unknown1056(1070)
    sprite('vr_ka450_40', 2)
    teleportRelativeY(50000)
    sprite('null', 4)
    sprite('vr_ka450_41', 2)
    sprite('null', 4)
    teleportRelativeY(50000)
    sprite('vr_ka450_42', 2)
    sprite('null', 4)
    sprite('vr_ka450_43', 2)
    sprite('vr_ka450_40', 2)
    teleportRelativeY(0)
    sprite('null', 4)
    sprite('vr_ka450_41', 2)
    sprite('null', 4)
    sprite('vr_ka450_42', 2)
    teleportRelativeY(50000)
    sprite('null', 4)
    sprite('vr_ka450_43', 2)
    sprite('vr_ka450_40', 2)
    teleportRelativeY(0)
    sprite('null', 4)
    sprite('vr_ka450_41', 2)
    sprite('null', 4)
    sprite('vr_ka450_42', 2)
    sprite('null', 4)
    sprite('vr_ka450_43', 2)
    teleportRelativeY(50000)
    sprite('vr_ka450_40', 2)
    sprite('null', 4)
    sprite('vr_ka450_41', 2)
    sprite('null', 4)
    sprite('vr_ka450_42', 2)
    teleportRelativeY(0)
    sprite('null', 4)
    sprite('vr_ka450_43', 2)
    sprite('vr_ka450_40', 2)
    sprite('null', 4)
    sprite('vr_ka450_41', 2)
    teleportRelativeY(50000)

@State
def IchigekiPicture6():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown23015(4)
        Unknown2019(-1000)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(3)
        Unknown3001(255)
        Unknown1000(0)
        Unknown1056(1070)
    sprite('vr_ka450_34', 4)
    sprite('vr_ka450_35', 4)
    sprite('vr_ka450_36', 102)
    sprite('vr_ka450_35', 2)

@State
def cutin():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown6001(1)
        Unknown1001(640000)
        teleportRelativeY(-768000)
        Unknown23015(5)
        Unknown3060('0000000076725f637574696e746573743100000000000000000000000000000000000000')
        Unknown3063(0, -505000)
        Unknown3062(0, 0)
        Unknown3060('0100000076725f637574696e746573743200000000000000000000000000000000000000')
        Unknown3063(1, -505000)
        Unknown3062(1, 0)
    sprite('bc_Cutintest', 8)
    Unknown3032()
    teleportRelativeX(-940000)
    physicsXImpulse(65000)
    physicsYImpulse(6500)
    Unknown3001(0)
    Unknown3004(40)
    Unknown1096(840)
    Unknown1099(20)
    sprite('bc_Cutintest', 30)
    Unknown1019(50)
    YAccel(50)
    Unknown1019(5)
    YAccel(5)
    Unknown3031()
    Unknown1099(0)
    Unknown1096(1000)
    sprite('bc_Cutintest', 15)
    physicsXImpulse(60000)
    physicsYImpulse(6000)
    Unknown3032()
    Unknown3004(-25)
    Unknown1099(60)

@State
def kaef_ichigeki_BG00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6b6165665f3435305f626730302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
        Unknown1096(850)
        Unknown1007(-150000)
        sendToLabelUpon(36, 1)
    sprite('null', 32767)
    Unknown3004(30)
    label(1)
    sprite('null', 160)
    Unknown1007(-1600000)

@State
def kaef_450smoke():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('kaef_450bg')
        Unknown4010(2)
    sprite('null', 32767)

@State
def P4U_Cutin_Parent():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 1)
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
    sprite('vr_99p4u_face00', 45)
    SFX_0('spsys_over_power')
    SFX_0('spsys_over_power')
    if SLOT_168:
        GFX_0('P4U_ka_NotJPN', 100)
    else:
        GFX_0('P4U_ka_JPN', 100)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(180)
    sprite('vr_99p4u_face00', 1)
    Unknown3001(120)
    sprite('vr_99p4u_face00', 1)
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
    sprite('vr_p4_ka_mozi', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi', 1)
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
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown1096(100)
    Unknown3001(40)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(500)
    Unknown1096(300)
    Unknown3001(70)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(550)
    Unknown1096(700)
    Unknown3001(100)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(600)
    Unknown1096(900)
    Unknown3001(130)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(6500)
    Unknown1096(800)
    Unknown3001(160)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(700)
    Unknown1096(900)
    Unknown3001(190)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1150)
    Unknown3001(220)
    sprite('vr_p4_ka_mozi_notjpn', 38)
    teleportRelativeX(-2000)
    Unknown1007(800)
    Unknown1096(1100)
    Unknown3001(255)
    physicsXImpulse(-50)
    physicsYImpulse(50)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(180)
    Unknown1096(700)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(120)
    Unknown1096(300)
    sprite('vr_p4_ka_mozi_notjpn', 1)
    Unknown3001(60)
    Unknown1096(100)

@State
def Entry_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        teleportRelativeX(128000)
    sprite('vr_ka601_00', 32767)
    physicsYImpulse(3200)
    physicsXImpulse(25600)
    setGravity(800)
    Unknown1028(-800)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('null', 1)
    GFX_0('Entry_2b', 100)
    GFX_0('Entry_2c', 100)

@State
def Entry_2b():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
    sprite('vr_ka601_10', 3)
    sprite('vr_ka601_11', 3)
    sprite('vr_ka601_10', 3)
    sprite('vr_ka601_12', 3)
    sprite('vr_ka601_13', 16)
    sprite('vr_ka601_13', 32)
    Unknown3004(-8)

@State
def Entry_2c():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        teleportRelativeX(-96000)
    sprite('vr_ka601_20', 60)
    Unknown1099(3)
    GFX_1('kaef_entry2', 100)
    sprite('vr_ka601_20', 32)
    Unknown3004(-8)

@State
def win2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(0)
        Unknown2019(-500)
    sprite('kaef611_00', 3)
    sprite('kaef611_01', 3)
    sprite('kaef611_02', 3)
    sprite('kaef611_03', 30)
    SFX_3('ka004')
    Unknown1007(640000)
    ScreenShake(16000, 0)
    Unknown23015(3)
    sprite('kaef611_03', 32767)
    physicsYImpulse(-10000)