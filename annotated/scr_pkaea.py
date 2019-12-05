@State
def PKA_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('504b415f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PKA_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PKA_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
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
    sprite('keep', 32767)	# 1-32767
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_0('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PKA_PersonaWait')

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
        callSubroutine('PKA_ReceptionSignal')
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
        Unknown23059(1)
    sprite('ta408_00', 2)	# 1-2
    SFX_3('airbackdash_l')
    Unknown2006()
    Unknown4007(0)
    SLOT_6 = 1
    sprite('ta408_01', 2)	# 3-4
    SFX_3('airbackdash_l')
    sprite('ta408_00', 2)	# 5-6
    SFX_3('airbackdash_l')
    sprite('ta408_02', 2)	# 7-8
    SFX_3('airdash_m')
    physicsXImpulse(20000)
    sprite('ta408_03', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    Unknown1019(200)
    sprite('ta408_03', 3)	# 12-14	 **attackbox here**
    SFX_3('airdash_m')
    Unknown1019(110)
    sprite('ta408_03', 3)	# 15-17	 **attackbox here**
    Unknown1019(105)
    sprite('ta408_03', 3)	# 18-20	 **attackbox here**
    SFX_3('airdash_m')
    Unknown1019(105)
    sprite('ta408_03', 3)	# 21-23	 **attackbox here**
    Unknown1019(80)
    label(0)
    sprite('keep', 8)	# 24-31
    clearUponHandler(11)
    Unknown23027()
    sprite('ta408_04', 2)	# 32-33
    SFX_3('brake_normal_heavy')
    Unknown1019(50)
    sprite('ta408_04', 2)	# 34-35
    Unknown1019(30)
    sprite('ta408_05', 2)	# 36-37
    Unknown1019(30)
    sprite('ta408_05', 3)	# 38-40
    Unknown1019(20)
    sprite('ta408_06', 3)	# 41-43
    Unknown1019(20)
    sprite('ta408_06', 30)	# 44-73
    SLOT_6 = 0
    Unknown1019(0)
    sprite('ta408_06', 3)	# 74-76
    sprite('keep', 32767)	# 77-32843
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
        Unknown23059(1)
    sprite('ta204_50', 3)	# 1-3
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta204_51', 3)	# 4-6
    sprite('ta204_00', 2)	# 7-8
    loopRest()
    Unknown4007(0)
    label(0)
    sprite('ta204_50', 3)	# 9-11
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta204_51', 3)	# 12-14
    sprite('ta204_00', 2)	# 15-16
    loopRest()
    gotoLabel(0)
    label(580)
    label(1)
    sprite('keep', 32767)	# 17-32783
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B_Normal():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B_ATK')
        callSubroutine('PKA_CheckWarp')
        Unknown23059(1)
    sprite('ta204_04', 3)	# 1-3
    GFX_0('ta_5C_zanzoh', 100)
    SFX_3('slash_blade_fast')
    sprite('ta204_05', 3)	# 4-6	 **attackbox here**
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    Unknown4007(0)
    sprite('ta204_05', 20)	# 7-26	 **attackbox here**
    StartMultihit()
    sprite('keep', 32767)	# 27-32793
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B_Hold():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B_ATK')
        callSubroutine('PKA_CheckWarp')
        Unknown23059(1)
    sprite('ta204_01', 3)	# 1-3
    sprite('ta204_02', 3)	# 4-6
    sprite('ta204_03', 3)	# 7-9
    sprite('ta204_04', 3)	# 10-12
    SFX_3('slash_blade_fast')
    GFX_0('ta_5C_zanzoh', 100)
    sprite('ta204_05', 3)	# 13-15	 **attackbox here**
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    Unknown4007(0)
    sprite('ta204_05', 20)	# 16-35	 **attackbox here**
    StartMultihit()
    sprite('keep', 32767)	# 36-32802
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
        Unknown23059(1)
    sprite('ta204_01', 3)	# 1-3
    sprite('ta204_02', 3)	# 4-6
    sprite('ta204_03', 3)	# 7-9
    sprite('ta204_04', 3)	# 10-12
    SFX_3('slash_blade_fast')
    GFX_0('ta_5C_zanzoh', 100)
    sprite('ta204_05', 3)	# 13-15	 **attackbox here**
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    Unknown4007(0)
    sprite('ta204_05', 20)	# 16-35	 **attackbox here**
    StartMultihit()
    sprite('keep', 32767)	# 36-32802
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
    sprite('ta204_50', 2)	# 1-2
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta204_51', 2)	# 3-4
    sprite('ta204_00', 2)	# 5-6
    sprite('ta204_04', 2)	# 7-8
    GFX_0('ta_5C_zanzoh', 100)
    SFX_3('slash_blade_fast')
    sprite('ta204_05', 3)	# 9-11	 **attackbox here**
    ScreenShake(20000, 20000)
    SFX_3('ka005')
    sprite('ta204_05', 20)	# 12-31	 **attackbox here**
    StartMultihit()
    sprite('keep', 32767)	# 32-32798
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
        Unknown23059(1)
    sprite('ta232_10', 3)	# 1-3
    Unknown2006()
    sprite('ta232_11', 2)	# 4-5
    sprite('ta232_12', 2)	# 6-7
    sprite('ta232_13', 2)	# 8-9
    sprite('ta232_14', 2)	# 10-11
    sprite('ta232_15', 4)	# 12-15
    label(0)
    sprite('ta232_55', 3)	# 16-18
    sprite('ta232_56', 3)	# 19-21
    sprite('ta232_57', 3)	# 22-24
    loopRest()
    gotoLabel(0)
    label(580)
    label(1)
    sprite('keep', 32767)	# 25-32791
    enterState('PersonaDeleteAndIdling')

@State
def PKA_Persona5B2nd_Hold():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff00000000c0bdf0ff80841e000000000000000000')
        callSubroutine('PKA_AttackInit')
        callSubroutine('PKA_Persona5B2nd_ATK')
        callSubroutine('PKA_CheckWarp')
        Unknown23059(1)
    sprite('ta232_00', 1)	# 1-1
    Unknown2006()
    physicsXImpulse(20000)
    Unknown1028(60000)
    sprite('ta232_01', 1)	# 2-2
    sprite('ta232_02', 1)	# 3-3
    sprite('ta232_03', 1)	# 4-4	 **attackbox here**
    SFX_3('slash_blade_slow')
    physicsXImpulse(0)
    Unknown1084(1)
    StartMultihit()
    sprite('ta232_05', 2)	# 5-6	 **attackbox here**
    Unknown23054('74613233325f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown4007(0)
    sprite('ta232_05', 3)	# 7-9	 **attackbox here**
    StartMultihit()
    sprite('ta232_06', 5)	# 10-14
    sprite('ta232_07', 20)	# 15-34
    sprite('keep', 32767)	# 35-32801
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
        Unknown23059(1)
    sprite('ta232_00', 1)	# 1-1
    Unknown2006()
    physicsXImpulse(20000)
    Unknown1028(60000)
    sprite('ta232_01', 1)	# 2-2
    sprite('ta232_02', 1)	# 3-3
    sprite('ta232_03', 1)	# 4-4	 **attackbox here**
    SFX_3('slash_blade_slow')
    physicsXImpulse(0)
    Unknown1084(1)
    StartMultihit()
    sprite('ta232_05', 2)	# 5-6	 **attackbox here**
    Unknown23054('74613233325f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown4007(0)
    sprite('ta232_05', 3)	# 7-9	 **attackbox here**
    StartMultihit()
    sprite('ta232_06', 5)	# 10-14
    sprite('ta232_07', 20)	# 15-34
    sprite('keep', 32767)	# 35-32801
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
    sprite('ta232_00', 2)	# 1-2
    teleportRelativeX(-200000)
    physicsXImpulse(20000)
    sprite('ta232_01', 2)	# 3-4
    sprite('ta232_02', 2)	# 5-6
    sprite('ta232_03', 2)	# 7-8	 **attackbox here**
    SFX_3('slash_blade_slow')
    physicsXImpulse(0)
    StartMultihit()
    sprite('ta232_05', 2)	# 9-10	 **attackbox here**
    Unknown23054('74613233325f303400000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('ta232_05', 3)	# 11-13	 **attackbox here**
    StartMultihit()
    sprite('ta232_06', 5)	# 14-18
    sprite('ta232_07', 20)	# 19-38
    sprite('keep', 32767)	# 39-32805
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
        Unknown23059(1)
    sprite('ta254_00', 3)	# 1-3
    label(0)
    sprite('ta254_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)	# 7-32773
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
        Unknown11001(0, 0, 12)
        Unknown2017(1)
        Unknown4007(3)
        Unknown2053(1)
        Unknown23022(1)
        callSubroutine('PKA_CheckWarp')
        Unknown23059(1)

        def upon_STATE_END():
            Unknown23029(3, 2031, 0)
    sprite('ta254_02', 3)	# 1-3
    Unknown4007(0)
    physicsXImpulse(20000)
    SFX_3('slash_blade_slow')
    sprite('ta254_03', 2)	# 4-5
    physicsXImpulse(0)
    sprite('ta254_04', 5)	# 6-10	 **attackbox here**
    SFX_3('down_steal_m')
    GFX_0('taef_Air5C_Zanzoh', 100)
    sprite('ta254_04', 20)	# 11-30	 **attackbox here**
    StartMultihit()
    Unknown23022(0)
    Unknown23029(3, 2031, 0)
    sprite('keep', 32767)	# 31-32797
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
        Unknown23059(1)
    sprite('ta205_00', 6)	# 1-6
    SLOT_4 = 1
    SLOT_6 = 1
    GFX_0('ta_5DThunder', 100)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_01', 6)	# 7-12
    Unknown4007(0)
    sprite('ta205_02', 6)	# 13-18
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_03', 5)	# 19-23
    sprite('ta205_04', 5)	# 24-28
    sprite('ta205_05', 3)	# 29-31
    Unknown23029(1, 4081, 0)
    ScreenShake(10000, 0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_06', 2)	# 32-33
    sprite('ta205_07', 1)	# 34-34
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    label(819)
    sprite('ta205_06', 1)	# 35-35
    sprite('ta205_05', 2)	# 36-37
    GFX_0('ta_5DThunderTuika', 100)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('ta205_06', 1)	# 38-38
    sprite('ta205_07', 2)	# 39-40
    sprite('ta205_06', 1)	# 41-41
    sprite('ta205_07', 2)	# 42-43
    sprite('ta205_06', 1)	# 44-44
    sprite('ta205_07', 2)	# 45-46
    ScreenShake(10000, 0)
    SLOT_51 = (SLOT_51 + 1)
    if (SLOT_51 == 3):
        sendToLabel(0)
    loopRest()
    gotoLabel(819)
    label(0)
    sprite('ta205_07', 5)	# 47-51
    SLOT_6 = 0
    sprite('ta205_06', 5)	# 52-56
    sprite('ta205_05', 5)	# 57-61
    sprite('ta205_04', 5)	# 62-66
    sprite('ta205_03', 5)	# 67-71
    sprite('ta205_02', 5)	# 72-76
    sprite('ta205_01', 5)	# 77-81
    sprite('ta205_00', 25)	# 82-106
    sprite('keep', 32767)	# 107-32873
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
    sprite('ta403_07', 4)	# 1-4
    sprite('ta403_08', 1)	# 5-5
    sprite('ta403_09', 2)	# 6-7
    GFX_0('taef_taiden', 100)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 2)	# 8-9
    sprite('ta403_09', 2)	# 10-11
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 2)	# 12-13
    sprite('ta403_09', 3)	# 14-16
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 3)	# 17-19
    sprite('ta403_09', 3)	# 20-22
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 3)	# 23-25
    sprite('ta403_09', 4)	# 26-29
    sprite('ta403_10', 4)	# 30-33
    sprite('ta403_09', 4)	# 34-37
    sprite('ta403_10', 4)	# 38-41
    sprite('keep', 32767)	# 42-32808
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
    sprite('ta403_00', 20)	# 1-20
    Unknown20000(1)
    sprite('ta403_00', 5)	# 21-25
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)	# 26-30
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)	# 31-35
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)	# 36-40
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)	# 41-43	 **attackbox here**
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    Unknown11069('ta_NageThunder')
    Unknown11067(1)
    sprite('ta403_03', 3)	# 44-46
    Unknown4007(0)
    sprite('ta403_04', 3)	# 47-49
    sprite('ta403_05', 3)	# 50-52
    sprite('ta403_06', 6)	# 53-58
    sprite('ta403_07', 10)	# 59-68
    sprite('ta403_08', 5)	# 69-73
    GFX_0('ta_NageThunder', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)	# 74-77
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 78-81
    sprite('ta403_09', 4)	# 82-85
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 86-89
    sprite('ta403_09', 4)	# 90-93
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 94-97
    sprite('ta403_09', 4)	# 98-101
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 102-105
    sprite('ta403_09', 4)	# 106-109
    sprite('ta403_10', 4)	# 110-113
    sprite('ta403_09', 5)	# 114-118
    sprite('ta403_10', 5)	# 119-123
    sprite('ta403_09', 6)	# 124-129
    sprite('ta403_10', 6)	# 130-135
    sprite('keep', 32767)	# 136-32902
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
    sprite('ta403_00', 20)	# 1-20
    Unknown20000(1)
    sprite('ta403_00', 5)	# 21-25
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)	# 26-30
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)	# 31-35
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)	# 36-40
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)	# 41-43	 **attackbox here**
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    Unknown11069('ta_NageThunderEX')
    Unknown11067(1)
    sprite('ta403_03', 3)	# 44-46
    Unknown4007(0)
    sprite('ta403_04', 3)	# 47-49
    sprite('ta403_05', 3)	# 50-52
    sprite('ta403_06', 6)	# 53-58
    sprite('ta403_07', 10)	# 59-68
    sprite('ta403_08', 5)	# 69-73
    GFX_0('ta_NageThunderEX', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)	# 74-77
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 78-81
    sprite('ta403_09', 4)	# 82-85
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 86-89
    sprite('ta403_09', 4)	# 90-93
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 94-97
    sprite('ta403_09', 4)	# 98-101
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 102-105
    sprite('ta403_09', 4)	# 106-109
    sprite('ta403_10', 4)	# 110-113
    sprite('ta403_09', 5)	# 114-118
    sprite('ta403_10', 5)	# 119-123
    sprite('ta403_09', 6)	# 124-129
    sprite('ta403_10', 6)	# 130-135
    sprite('keep', 32767)	# 136-32902
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
    sprite('ta405_00', 5)	# 1-5
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown2006()
    sprite('ta405_01', 3)	# 6-8	 **attackbox here**
    Unknown3029(1)
    Unknown4007(0)
    Unknown2053(1)
    physicsYImpulse(39000)
    Unknown47('030000000200000013000000000000000a000000020000000c000000')
    if (SLOT_12 > 35000):
        physicsXImpulse(35000)
    SFX_3('airdash_m')
    GFX_1('ef_charge_ground', 104)
    sprite('ta405_01', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    sprite('ta405_01', 1)	# 10-10	 **attackbox here**
    sprite('ta405_01', 1)	# 11-11	 **attackbox here**
    sprite('ta405_01', 1)	# 12-12	 **attackbox here**
    sprite('ta405_01', 1)	# 13-13	 **attackbox here**
    sprite('ta405_01', 1)	# 14-14	 **attackbox here**
    sprite('ta405_01', 1)	# 15-15	 **attackbox here**
    sprite('ta405_01', 1)	# 16-16	 **attackbox here**
    sprite('ta405_01', 1)	# 17-17	 **attackbox here**
    Unknown1019(45)
    YAccel(45)
    sprite('ta405_01', 1)	# 18-18	 **attackbox here**
    sprite('ta405_01', 1)	# 19-19	 **attackbox here**
    sprite('ta405_02', 2)	# 20-21	 **attackbox here**
    Unknown3029(0)
    Unknown23027()
    setInvincible(0)
    sprite('ta405_03', 2)	# 22-23
    sprite('ta405_04', 2)	# 24-25	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)	# 26-29	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)	# 30-33	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)	# 34-37	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 4)	# 38-41	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('ta405_04', 5)	# 42-46	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    sprite('ta405_04', 15)	# 47-61	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    sprite('keep', 32767)	# 62-32828
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
    sprite('keep', 1)	# 1-1
    sprite('keep', 32767)	# 2-32768
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
    sprite('ta405_01', 2)	# 1-2	 **attackbox here**
    SFX_3('grip_hugs')
    SFX_3('bound_marble_m')
    ScreenShake(10000, 0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    SLOT_8 = 0
    SLOT_9 = 0
    Unknown1019(30)
    YAccel(30)
    sprite('ta405_02', 2)	# 3-4	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_03', 2)	# 5-6
    Unknown1019(45)
    YAccel(45)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)	# 7-9	 **attackbox here**
    Unknown1019(85)
    YAccel(85)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)	# 10-12	 **attackbox here**
    Unknown1019(70)
    YAccel(70)
    sprite('ta405_04', 3)	# 13-15	 **attackbox here**
    Unknown1019(60)
    YAccel(60)
    sprite('ta405_04', 10)	# 16-25	 **attackbox here**
    Unknown1019(0)
    YAccel(0)
    sprite('ta405_04', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    SFX_3('electric_l')
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(24000, 0)
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)	# 32-34	 **attackbox here**
    RefreshMultihit()
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 3)	# 35-37	 **attackbox here**
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)	# 38-40	 **attackbox here**
    RefreshMultihit()
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(24000, 0)
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 3)	# 41-43	 **attackbox here**
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_04', 3)	# 44-46	 **attackbox here**
    RefreshMultihit()
    Unknown5000(16, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('ta_AntiAir', 100)
    GFX_1('taef_antiair', 1)
    sprite('ta405_04', 20)	# 47-66	 **attackbox here**
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(24000, 0)
    sprite('ta405_05', 5)	# 67-71
    Unknown5000(25, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    setGravity(3000)
    physicsYImpulse(21000)
    physicsXImpulse(5000)
    SFX_3('slash_blade_slow')
    sprite('ta405_06', 4)	# 72-75
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ta405_07', 32767)	# 76-32842	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('ta405_08', 4)	# 32843-32846	 **attackbox here**
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
    sprite('ta405_09', 40)	# 32847-32886
    sprite('keep', 32767)	# 32887-65653
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
    sprite('ta432_00', 42)	# 1-42	 **attackbox here**
    SFX_3('electric_l')
    Unknown20000(1)
    Unknown2017(1)
    GFX_0('taef432_wait', 1)
    sprite('ta432_01', 5)	# 43-47	 **attackbox here**
    SFX_3('electric_l')
    SFX_3('airdash_m')
    physicsXImpulse(90000)
    SLOT_51 = 1
    GFX_0('taef432_push', 1)
    Unknown38(4, 1)
    sprite('ta432_02', 30)	# 48-77	 **attackbox here**
    RefreshMultihit()
    Unknown13(4)
    GFX_0('taef432_push', 1)
    sprite('keep', 32767)	# 78-32844
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
    sprite('ta432_02', 1)	# 1-1	 **attackbox here**
    SFX_3('grip_hugs')
    SLOT_51 = 1
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('taef432_push', 1)
    Unknown38(4, 1)
    loopRest()
    sprite('ta432_02', 180)	# 2-181	 **attackbox here**
    loopRest()
    label(3)
    sprite('ta432_03', 2)	# 182-183	 **attackbox here**
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
    sprite('ta432_04', 2)	# 184-185	 **attackbox here**
    SFX_3('electric_m')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    ScreenShake(0, 34000)
    GFX_0('taef432_hold', 1)
    Unknown38(5, 1)
    sprite('ta432_04', 8)	# 186-193	 **attackbox here**
    sprite('ta432_05', 40)	# 194-233	 **attackbox here**
    SFX_3('electric_m')
    SFX_3('quake_l')
    Unknown21015('4b75726f6b6f67655f4578650000000000000000000000000000000000000000d910000000000000')
    sprite('ta432_06', 8)	# 234-241	 **attackbox here**
    SFX_3('electric_m')
    ScreenShake(0, 5000)
    sprite('ta432_06', 8)	# 242-249	 **attackbox here**
    SFX_3('electric_m')
    ScreenShake(0, 10000)
    sprite('ta432_06', 8)	# 250-257	 **attackbox here**
    SFX_3('electric_m')
    ScreenShake(0, 15000)
    sprite('ta432_06', 8)	# 258-265	 **attackbox here**
    SFX_3('electric_m')
    ScreenShake(0, 20000)
    sprite('ta432_06', 8)	# 266-273	 **attackbox here**
    SFX_3('electric_m')
    ScreenShake(0, 25000)
    sprite('ta432_06', 8)	# 274-281	 **attackbox here**
    SFX_3('electric_m')
    ScreenShake(0, 30000)
    sprite('ta432_06', 3)	# 282-284	 **attackbox here**
    SFX_3('electric_m')
    sprite('ta432_06', 6)	# 285-290	 **attackbox here**
    ScreenShake(0, 40000)
    sprite('ta432_05', 1)	# 291-291	 **attackbox here**
    ScreenShake(0, 50000)
    SFX_3('bomb_l')
    SFX_3('bonebroken_h')
    RefreshMultihit()
    Damage(3700)
    if SLOT_7:
        Damage(4700)
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
    sprite('ta432_05', 40)	# 292-331	 **attackbox here**
    sprite('ta432_05', 30)	# 332-361	 **attackbox here**
    sprite('keep', 32767)	# 362-33128
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
        Damage(1500)
        AttackP2(100)
        Unknown11091(10)
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
    sprite('ta403_00', 20)	# 1-20
    sprite('ta403_00', 5)	# 21-25
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)	# 26-30
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)	# 31-35
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)	# 36-40
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)	# 41-43	 **attackbox here**
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    sprite('ta403_03', 3)	# 44-46
    Unknown4007(0)
    sprite('ta403_04', 3)	# 47-49
    sprite('ta403_05', 3)	# 50-52
    sprite('ta403_06', 3)	# 53-55
    sprite('ta403_07', 5)	# 56-60
    sprite('ta403_08', 4)	# 61-64
    GFX_0('ta_NageThunderOD', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)	# 65-68
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 69-72
    sprite('ta403_09', 4)	# 73-76
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 77-80
    sprite('ta403_09', 4)	# 81-84
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 85-88
    sprite('ta403_09', 4)	# 89-92
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 93-96
    sprite('ta403_09', 4)	# 97-100
    sprite('ta403_10', 4)	# 101-104
    sprite('ta403_09', 5)	# 105-109
    sprite('ta403_10', 5)	# 110-114
    sprite('ta403_09', 6)	# 115-120
    sprite('ta403_10', 6)	# 121-126
    sprite('keep', 32767)	# 127-32893
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
    sprite('ta403_00', 20)	# 1-20
    sprite('ta403_00', 5)	# 21-25
    SFX_3('slash_blade_slow')
    physicsYImpulse(-10000)
    sprite('ta403_01', 5)	# 26-30
    physicsYImpulse(-20000)
    sprite('ta403_01', 5)	# 31-35
    physicsYImpulse(-40000)
    sprite('ta403_01', 5)	# 36-40
    physicsYImpulse(-60000)
    loopRest()
    sprite('ta403_02', 3)	# 41-43	 **attackbox here**
    physicsYImpulse(0)
    RefreshMultihit()
    ScreenShake(30000, 30000)
    SFX_3('bomb_l')
    sprite('ta403_03', 3)	# 44-46
    Unknown4007(0)
    sprite('ta403_04', 3)	# 47-49
    sprite('ta403_05', 3)	# 50-52
    sprite('ta403_06', 3)	# 53-55
    sprite('ta403_07', 5)	# 56-60
    sprite('ta403_08', 4)	# 61-64
    GFX_0('ta_NageThunderOD_DUO', 0)
    Unknown23029(3, 4022, 0)
    sprite('ta403_09', 4)	# 65-68
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 69-72
    sprite('ta403_09', 4)	# 73-76
    Unknown20000(0)
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 77-80
    sprite('ta403_09', 4)	# 81-84
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 85-88
    sprite('ta403_09', 4)	# 89-92
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_1('taef_thunderbolt', 2)
    sprite('ta403_10', 4)	# 93-96
    sprite('ta403_09', 4)	# 97-100
    sprite('ta403_10', 4)	# 101-104
    sprite('ta403_09', 5)	# 105-109
    sprite('ta403_10', 5)	# 110-114
    sprite('ta403_09', 6)	# 115-120
    sprite('ta403_10', 6)	# 121-126
    sprite('keep', 32767)	# 127-32893
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
    sprite('vr_ka203_col', 5)	# 1-5
    ScreenShake(10000, 10000)
    GFX_0('fukidashi_bg', 100)
    if (not SLOT_168):
        GFX_0('fukidashi_font', 100)
    else:
        GFX_0('fukidashi_font_e', 100)
    sprite('vr_ka203_col', 15)	# 6-20
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
    sprite('vr_ka203_col', 5)	# 1-5
    ScreenShake(10000, 10000)
    GFX_0('fukidashi_bg', 100)
    Unknown23029(1, 2030, 0)
    if (not SLOT_168):
        GFX_0('fukidashi_font', 100)
        Unknown23029(1, 2030, 0)
    else:
        GFX_0('fukidashi_font_e', 100)
        Unknown23029(1, 2030, 0)
    sprite('vr_ka203_col', 15)	# 6-20
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
    sprite('vr_ka203_00', 1)	# 1-1
    sprite('vr_ka203_00', 1)	# 2-2
    sprite('vr_ka203_01', 2)	# 3-4
    sprite('vr_ka203_00', 2)	# 5-6
    sprite('vr_ka203_01', 3)	# 7-9
    sprite('vr_ka203_00', 3)	# 10-12
    Unknown1099(10)
    Unknown3004(-15)
    sprite('vr_ka203_01', 4)	# 13-16
    sprite('vr_ka203_00', 4)	# 17-20
    sprite('vr_ka203_01', 5)	# 21-25
    sprite('vr_ka203_00', 5)	# 26-30

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
    sprite('vr_ka203_10', 3)	# 1-3
    Unknown1007(32000)
    sprite('vr_ka203_10', 1)	# 4-4
    Unknown1007(-32000)
    teleportRelativeX(-16000)
    sprite('vr_ka203_10', 2)	# 5-6
    sprite('vr_ka203_10', 3)	# 7-9
    sprite('vr_ka203_10', 4)	# 10-13
    Unknown3004(-15)
    Unknown1007(16000)
    teleportRelativeX(-32000)
    sprite('vr_ka203_10', 4)	# 14-17
    sprite('vr_ka203_10', 5)	# 18-22
    Unknown1007(-32000)
    teleportRelativeX(32000)
    sprite('vr_ka203_10', 5)	# 23-27

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
    sprite('vr_ka203_11', 3)	# 1-3
    Unknown1007(32000)
    sprite('vr_ka203_11', 1)	# 4-4
    Unknown1007(-32000)
    teleportRelativeX(-16000)
    sprite('vr_ka203_11', 2)	# 5-6
    sprite('vr_ka203_11', 3)	# 7-9
    sprite('vr_ka203_11', 4)	# 10-13
    Unknown3004(-15)
    Unknown1007(16000)
    teleportRelativeX(-32000)
    sprite('vr_ka203_11', 4)	# 14-17
    sprite('vr_ka203_11', 5)	# 18-22
    Unknown1007(-32000)
    teleportRelativeX(32000)
    sprite('vr_ka203_11', 5)	# 23-27

@State
def IsuBreak():
    sprite('null', 1)	# 1-1
    GFX_0('IsuBreakParts1', 100)
    GFX_0('IsuBreakParts2', 100)
    GFX_0('IsuBreakParts3', 100)
    SFX_3('ka004')

@State
def IsuBreakParts1():
    sprite('vr_ka401_00', 20)	# 1-20
    setGravity(2000)
    physicsXImpulse(4000)
    physicsYImpulse(25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(-25000)
    Unknown3007(170)
    Unknown3019(170)
    Unknown3013(170)
    sprite('keep', 30)	# 21-50
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts2():
    sprite('vr_ka401_01', 20)	# 1-20
    setGravity(2000)
    physicsXImpulse(-4000)
    physicsYImpulse(25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)
    Unknown3007(170)
    Unknown3019(170)
    Unknown3013(170)
    sprite('keep', 30)	# 21-50
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts3():
    sprite('vr_ka401_02', 20)	# 1-20
    setGravity(2000)
    physicsXImpulse(1000)
    physicsYImpulse(30000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)
    Unknown3007(170)
    Unknown3019(170)
    Unknown3013(170)
    sprite('keep', 30)	# 21-50
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts1ex():
    sprite('vr_ka401_00', 2)	# 1-2
    Unknown2054(1)
    teleportRelativeX(3000)
    Unknown1007(3000)
    sprite('vr_ka401_00', 2)	# 3-4
    teleportRelativeX(-3000)
    Unknown1007(-3000)
    sprite('vr_ka401_00', 20)	# 5-24
    setGravity(2000)
    physicsXImpulse(8000)
    physicsYImpulse(-25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(-25000)

    def upon_LANDING():
        YAccel(-95)
    sprite('keep', 30)	# 25-54
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts2ex():
    sprite('vr_ka401_01', 2)	# 1-2
    Unknown2054(1)
    teleportRelativeX(3000)
    Unknown1007(-3000)
    sprite('vr_ka401_01', 2)	# 3-4
    teleportRelativeX(-3000)
    Unknown1007(3000)
    sprite('vr_ka401_01', 20)	# 5-24
    setGravity(2000)
    physicsXImpulse(-8000)
    physicsYImpulse(-25000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)

    def upon_LANDING():
        YAccel(-95)
    sprite('keep', 30)	# 25-54
    Unknown3004(-20)
    Unknown3032()

@State
def IsuBreakParts3ex():
    sprite('vr_ka401_02', 2)	# 1-2
    Unknown2054(1)
    teleportRelativeX(-3000)
    Unknown1007(-3000)
    sprite('vr_ka401_02', 2)	# 3-4
    teleportRelativeX(3000)
    Unknown1007(3000)
    sprite('vr_ka401_02', 20)	# 5-24
    setGravity(2000)
    physicsXImpulse(2000)
    physicsYImpulse(-30000)
    Unknown1025(0, 1000)
    Unknown1026(0, 1000)
    Unknown1074(25000)

    def upon_LANDING():
        YAccel(-95)
    sprite('keep', 30)	# 25-54
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
    sprite('vr_ta204_00', 3)	# 1-3
    GFX_1('taef_thunderbolt', 0)
    GFX_1('taef_thunderbolt', 1)
    sprite('vr_ta204_01', 30)	# 4-33
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
    sprite('vr_ta254_00', 16)	# 1-16

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
    sprite('vr_ka430_00', 3)	# 1-3	 **attackbox here**
    GFX_0('kaef_chairthrow', 0)
    RefreshMultihit()
    Unknown53(0)
    teleportRelativeX(-70000)
    sprite('vr_ka430_00', 1)	# 4-4	 **attackbox here**
    Unknown53(1)
    label(0)
    sprite('vr_ka430_00', 1)	# 5-5	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(33)
    sprite('vr_ka430_01', 3)	# 6-8	 **attackbox here**
    Unknown9215()
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsXImpulse(15000)
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 15)	# 9-23	 **attackbox here**
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)	# 24-32790	 **attackbox here**
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
    sprite('null', 1)	# 32791-32791
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
    sprite('null', 3)	# 1-3
    teleportRelativeX(300000)
    GFX_0('ta_ThunderFall_bigen', 100)
    label(0)
    sprite('null', 3)	# 4-6
    gotoLabel(0)
    label(1)
    sprite('vr_ta205_col', 5)	# 7-11	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('null', 15)	# 12-26
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
    sprite('vr_ta205_col', 5)	# 1-5	 **attackbox here**
    SFX_3('thunder_s')
    teleportRelativeX(300000)
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('null', 15)	# 6-20
    GFX_0('ta_ThunderFall', 100)

@State
def taiden():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(2)
    sprite('vr_ka400_00', 2)	# 1-2
    sprite('null', 2)	# 3-4
    sprite('vr_ka400_00', 2)	# 5-6
    sprite('null', 2)	# 7-8
    sprite('vr_ka400_00', 3)	# 9-11
    sprite('null', 3)	# 12-14
    sprite('vr_ka400_00', 4)	# 15-18
    sprite('null', 4)	# 19-22

@State
def taef_taiden():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
    sprite('vr_ta400_00', 2)	# 1-2
    Unknown3001(255)
    sprite('vr_ta400_00', 2)	# 3-4
    Unknown3001(0)
    sprite('vr_ta400_00', 2)	# 5-6
    Unknown3001(255)
    sprite('vr_ta400_00', 2)	# 7-8
    Unknown3001(0)
    sprite('vr_ta400_00', 2)	# 9-10
    Unknown3001(255)
    sprite('vr_ta400_00', 2)	# 11-12
    Unknown3001(0)
    sprite('vr_ta400_00', 2)	# 13-14
    Unknown3001(255)
    sprite('vr_ta400_00', 2)	# 15-16
    Unknown3001(0)
    sprite('vr_ta400_00', 2)	# 17-18
    Unknown3001(255)
    sprite('vr_ta400_00', 2)	# 19-20
    Unknown3001(0)

@State
def KandenAtkObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown10001(3)
        Unknown11032('ffffffffffffffffffffffffffffffff')
    sprite('null', 1)	# 1-1
    Unknown4010(3)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 2-3
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 4-5
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 6-7
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 8-9
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 10-11
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 12-13
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 14-15
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 16-17
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('null', 2)	# 18-19
    Unknown23151(29, 105)
    GFX_1('kaef_spark_01', 100)
    sprite('vr_atk_dmy', 30)	# 20-49

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
    sprite('vr_ta403_col', 3)	# 1-3	 **attackbox here**
    SFX_3('thunder_l')
    RefreshMultihit()
    ScreenShake(20000, 20000)
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 4-6	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 7-9	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 10-12	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 13-15	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 16-18	 **attackbox here**
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
    sprite('vr_ta403_col', 3)	# 1-3	 **attackbox here**
    SFX_3('thunder_l')
    RefreshMultihit()
    ScreenShake(20000, 20000)
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 4-6	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 7-9	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 10-12	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 13-15	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)
    sprite('vr_ta403_col', 3)	# 16-18	 **attackbox here**
    SFX_3('thunder_s')
    RefreshMultihit()
    GFX_0('ta_ThunderFall', 100)

@State
def ta_NageThunderOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown17012(2, 0, 0)
        AttackLevel_(5)
        Damage(1300)
        Unknown11091(10)
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
    sprite('vr_ta403_col', 3)	# 1-3	 **attackbox here**
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
    sprite('vr_ta403_col', 3)	# 1-3	 **attackbox here**
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
    sprite('vr_ta205_00', 2)	# 1-2
    GFX_1('taef_thunderfall', 100)
    sprite('vr_ta205_01', 2)	# 3-4
    sprite('vr_ta205_02', 2)	# 5-6
    sprite('vr_ta205_03', 2)	# 7-8
    sprite('vr_ta205_00', 2)	# 9-10
    sprite('vr_ta205_01', 2)	# 11-12
    sprite('vr_ta205_02', 2)	# 13-14
    sprite('vr_ta205_03', 2)	# 15-16

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
    sprite('vr_ta205_10', 2)	# 1-2
    GFX_1('taef_thunderfall_target', 100)
    sprite('vr_ta205_11', 2)	# 3-4
    sprite('vr_ta205_12', 2)	# 5-6
    sprite('vr_ta205_13', 2)	# 7-8

@State
def ta_AntiAir():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3033()
        Unknown4061(3)
    sprite('vr_ta405_00', 6)	# 1-6

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
    sprite('vr_ka406_00', 32767)	# 1-32767

@State
def kaef407_atk1():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34303761746b312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3032()
    sprite('null', 6)	# 1-6
    Unknown3004(80)
    sprite('null', 4)	# 7-10
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
    sprite('null', 6)	# 1-6
    Unknown3004(80)
    sprite('null', 4)	# 7-10
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
    sprite('null', 6)	# 1-6
    Unknown3004(80)
    sprite('null', 4)	# 7-10
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
    sprite('vr_ka430_00', 3)	# 1-3	 **attackbox here**
    GFX_0('kaef_chairthrow', 0)
    RefreshMultihit()
    sprite('vr_ka430_00', 1)	# 4-4	 **attackbox here**
    Unknown53(1)
    label(0)
    sprite('vr_ka430_00', 1)	# 5-5	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(33)
    sprite('vr_ka430_01', 3)	# 6-8	 **attackbox here**
    Unknown2053(1)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 20)	# 9-28	 **attackbox here**
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)	# 29-32795	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(3)
    Hitstop(6)
    AirUntechableTime(77)
    AirPushbackY(-12000)
    YImpluseBeforeWallbounce(2000)
    loopRest()
    ExitState()
    label(66)
    sprite('vr_ka430_01', 3)	# 32796-32798	 **attackbox here**
    Unknown2053(1)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 20)	# 32799-32818	 **attackbox here**
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)	# 32819-65585	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(3)
    Hitstop(6)
    AirUntechableTime(77)
    AirPushbackY(-12000)
    YImpluseBeforeWallbounce(2000)
    loopRest()
    ExitState()
    label(44)
    sprite('null', 1)	# 65586-65586
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
    sprite('vr_ka430_01', 3)	# 1-3	 **attackbox here**
    physicsXImpulse(3000)
    Unknown23027()
    Unknown2053(1)
    Unknown53(0)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 20)	# 4-23	 **attackbox here**
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)	# 24-32790	 **attackbox here**
    RefreshMultihit()
    loopRest()
    ExitState()
    label(66)
    sprite('vr_ka430_01', 3)	# 32791-32793	 **attackbox here**
    physicsXImpulse(3000)
    Unknown23027()
    Unknown2053(1)
    Unknown53(0)
    Unknown23027()
    Unknown26('kaef_conbo_chair')
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 36)	# 32794-32829	 **attackbox here**
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)	# 32830-65596	 **attackbox here**
    RefreshMultihit()
    loopRest()
    ExitState()
    label(77)
    sprite('vr_ka430_01', 3)	# 65597-65599	 **attackbox here**
    Unknown23027()
    Unknown2053(0)
    Unknown26('kaef_conbo_chair')
    physicsXImpulse(15000)
    physicsYImpulse(40000)
    setGravity(2500)
    Unknown1074(35000)
    sprite('vr_ka430_01', 15)	# 65600-65614	 **attackbox here**
    Unknown3029(0)
    sprite('vr_ka430_01', 32767)	# 65615-98381	 **attackbox here**
    RefreshMultihit()
    Unknown11032('40420f006079feffffffffffffffffff')
    loopRest()
    ExitState()
    label(44)
    sprite('null', 1)	# 98382-98382
    GFX_0('IsuBreak', 100)

@State
def kaef_chairthrow():

    def upon_IMMEDIATE():
        Unknown23067('kaef_chairthrow')
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 60)	# 1-60

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
    sprite('vr_ka430_01', 171)	# 1-171	 **attackbox here**
    sprite('vr_ka430_01', 1)	# 172-172	 **attackbox here**
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(500000)
    teleportRelativeX(30000)
    sprite('vr_ka430_01', 32767)	# 173-32939	 **attackbox here**
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
    sprite('vr_ka430_01', 252)	# 32940-33191	 **attackbox here**
    sprite('vr_ka430_01', 1)	# 33192-33192	 **attackbox here**
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(2000000)
    teleportRelativeX(-100000)
    sprite('vr_ka430_01', 32767)	# 33193-65959	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(-60000)
    setGravity(0)
    Unknown1074(15000)
    sendToLabelUpon(2, 1)
    loopRest()
    ExitState()
    label(77)
    sprite('vr_ka430_01', 171)	# 65960-66130	 **attackbox here**
    sprite('vr_ka430_01', 1)	# 66131-66131	 **attackbox here**
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(500000)
    teleportRelativeX(30000)
    sprite('vr_ka430_01', 32767)	# 66132-98898	 **attackbox here**
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
    sprite('vr_ka430_01', 252)	# 98899-99150	 **attackbox here**
    sprite('vr_ka430_01', 1)	# 99151-99151	 **attackbox here**
    Unknown1086(22)
    Unknown1084(1)
    teleportRelativeY(2000000)
    teleportRelativeX(0)
    sprite('vr_ka430_01', 32767)	# 99152-131918	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(-60000)
    setGravity(0)
    Unknown1074(15000)
    sendToLabelUpon(2, 1)
    Unknown9310(25)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 1)	# 131919-131919
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
    sprite('vr_ka430_10', 12)	# 1-12
    sprite('vr_ka430_10', 18)	# 13-30

@State
def kaef430_atkline1():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34333061746b312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown1096(1050)
        Unknown3032()
    sprite('null', 6)	# 1-6
    sprite('null', 5)	# 7-11
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
    sprite('vr_ka430_20', 10)	# 1-10
    sprite('vr_ka430_20', 20)	# 11-30

@State
def kaef430_atkline3():

    def upon_IMMEDIATE():
        Unknown4003('6b6165665f34333061746b332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown23015(1)
        Unknown4015()
        Unknown1096(1550)
    sprite('null', 12)	# 1-12
    sprite('null', 6)	# 13-18
    Unknown3004(-50)

@State
def taef432_wait():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23067('taef_spthrow_wait')
    sprite('null', 42)	# 1-42

@State
def taef432_push():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23067('taef_spthrow_push')
    sprite('null', 32767)	# 1-32767

@State
def taef432_hold():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23067('taef_spthrow_hold')
    sprite('null', 32767)	# 1-32767

@State
def KurokogeCamera1():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 4311):
                sendToLabel(0)
            if (SLOT_48 == 4312):
                sendToLabel(1)
    label(0)
    sprite('keep', 32767)	# 1-32767
    Unknown1086(22)
    Unknown20000(1)
    Unknown20003(1)
    teleportRelativeY(0)
    label(1)
    sprite('keep', 70)	# 32768-32837
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
    sprite('ta450_00', 10)	# 1-10
    Unknown1007(1500000)
    SFX_3('electric_m')
    GFX_0('kaef_ichigeki_BG00', 103)
    sprite('ta450_00', 10)	# 11-20
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    Unknown26('SCEF_FadeBlack12In')
    sprite('ta450_00', 10)	# 21-30
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    GFX_0('ta450_charge', 100)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 31-40
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 41-50
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 51-60
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 61-70
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 71-80
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 81-90
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_00', 10)	# 91-100
    GFX_1('taef_ichigeki_charge', 0)
    GFX_1('taef_thunderbolt', 1)
    SFX_3('electric_m')
    sprite('ta450_01', 3)	# 101-103
    GFX_0('ta450_Light2', 100)
    GFX_0('ta450_Throw', 100)
    SFX_3('slash_blade_middle')
    sprite('ta450_02', 3)	# 104-106
    Unknown26('SCEF_FadeBlack12In')
    sprite('ta450_03', 8)	# 107-114
    sprite('ta450_03', 2)	# 115-116
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000022000000')
    sprite('keep', 10)	# 117-126
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown26('SCEF_FadeBlack12In')
    Unknown21012('6b6165665f6963686967656b695f42473030000000000000000000000000000024000000')
    sprite('vr_ta403_col', 4)	# 127-130	 **attackbox here**
    SFX_3('thunder_l')
    RefreshMultihit()
    Unknown11023(1)
    sprite('keep', 32767)	# 131-32897
    label(0)
    sprite('ta450_04', 18)	# 32898-32915
    clearUponHandler(39)
    Unknown4007(0)
    Unknown1000(350000)
    teleportRelativeY(600000)
    physicsYImpulse(-20000)
    sprite('ta450_04', 12)	# 32916-32927
    sprite('ta450_05', 8)	# 32928-32935
    SFX_3('down_steal_m')
    physicsYImpulse(0)
    ScreenShake(10000, 25000)
    sprite('ta450_06', 15)	# 32936-32950
    ScreenShake(10000, 10000)
    sprite('ta450_06', 20)	# 32951-32970
    sprite('ta450_07', 5)	# 32971-32975
    sprite('ta450_08', 10)	# 32976-32985
    sprite('ta450_09', 30)	# 32986-33015
    sprite('ta450_10', 6)	# 33016-33021
    sprite('ta450_11', 6)	# 33022-33027
    SFX_3('chain_snap')
    GFX_0('ta450_PunchAura', 0)
    sprite('ta450_12', 15)	# 33028-33042	 **attackbox here**
    sprite('ta450_12', 100)	# 33043-33142	 **attackbox here**
    Unknown23130(0, 30, 1)
    sprite('keep', 32767)	# 33143-65909
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
    sprite('vr_ta450_00', 80)	# 1-80
    Unknown3001(0)
    Unknown3004(4)
    sprite('vr_ta450_01', 3)	# 81-83

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
    sprite('null', 7)	# 1-7
    GFX_0('ta450_RandThrowMato', 100)
    sprite('null', 5)	# 8-12
    Unknown3004(-51)
    Unknown1059(-300)

@State
def ta450_RandThrowMato():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 2)	# 1-2
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)	# 3-4
    GFX_0('ta450_RandThrow01', 100)
    sprite('null', 2)	# 5-6
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)	# 7-8
    GFX_0('ta450_RandThrow01', 100)
    sprite('null', 2)	# 9-10
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)	# 11-12
    GFX_0('ta450_RandThrow01', 100)
    sprite('null', 2)	# 13-14
    GFX_0('ta450_RandThrow00', 100)
    sprite('null', 2)	# 15-16
    GFX_0('ta450_RandThrow01', 100)

@State
def ta450_RandThrow00():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 5)	# 1-5
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
    sprite('null', 5)	# 1-5
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
    sprite('vr_ka_yugami_00', 10)	# 1-10
    Unknown1059(40)
    sprite('vr_ka_yugami_00', 5)	# 11-15
    Unknown3004(-17)
    loopRest()

@State
def ta450_Thunder():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown3032()
    sprite('null', 10)	# 1-10
    sprite('null', 2)	# 11-12
    GFX_0('ta450_ThunderFlash', 100)
    SFX_3('thunder_s')
    sprite('null', 5)	# 13-17
    Unknown4003('6b6165665f3435305f7468756e6465725f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('ta450_RandThrowMato', 100)
    Unknown4015()
    SFX_3('damage_slash_m')
    sprite('null', 5)	# 18-22
    Unknown1059(-200)
    GFX_1('taef_tatethundershock_03', 100)
    GFX_0('ta450_ThunderShock', 100)
    GFX_0('ta450_ThunderShock2', 100)
    sprite('null', 15)	# 23-37
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
    sprite('vr_ta450_white', 15)	# 1-15
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
    sprite('null', 30)	# 1-30
    sprite('null', 20)	# 31-50
    Unknown3004(26)
    sprite('null', 30)	# 51-80
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
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    sprite('null', 10)	# 11-20
    Unknown3004(-26)

@State
def ta450_ThunderShock():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f666c6173682e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
    sprite('null', 10)	# 1-10
    Unknown1099(100)
    Unknown3004(-17)
    sprite('null', 5)	# 11-15

@State
def ta450_ThunderShock2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f666c617368322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
    sprite('null', 3)	# 1-3
    sprite('null', 10)	# 4-13
    Unknown3004(-17)
    sprite('null', 5)	# 14-18

@State
def ka450_PunchAura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('6b6165665f3435305f70756e6368617572615f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown3001(0)
        Unknown1000(180000)
    sprite('null', 5)	# 1-5
    Unknown3004(51)
    sprite('null', 3)	# 6-8
    SFX_3('electric_m')
    sprite('null', 3)	# 9-11
    SFX_3('electric_m')
    sprite('null', 3)	# 12-14
    SFX_3('electric_m')
    sprite('null', 3)	# 15-17
    SFX_3('electric_m')
    sprite('null', 3)	# 18-20
    SFX_3('electric_m')
    sprite('null', 5)	# 21-25
    SFX_3('electric_m')
    sprite('null', 5)	# 26-30
    SFX_3('electric_m')
    sprite('null', 5)	# 31-35
    SFX_3('electric_m')
    sprite('null', 5)	# 36-40
    SFX_3('electric_m')
    sprite('null', 5)	# 41-45
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
    sprite('null', 5)	# 1-5
    Unknown3004(51)
    SFX_3('electric_m')
    sprite('null', 3)	# 6-8
    SFX_3('electric_m')
    sprite('null', 3)	# 9-11
    SFX_3('electric_m')
    sprite('null', 3)	# 12-14
    SFX_3('electric_m')
    sprite('null', 3)	# 15-17
    SFX_3('electric_m')
    sprite('null', 3)	# 18-20
    SFX_3('electric_m')
    sprite('null', 5)	# 21-25
    SFX_3('electric_m')
    sprite('null', 5)	# 26-30
    SFX_3('electric_m')
    sprite('null', 5)	# 31-35
    SFX_3('electric_m')
    sprite('null', 5)	# 36-40
    SFX_3('electric_m')
    sprite('null', 5)	# 41-45
    SFX_3('electric_m')

@State
def ka450_PunchBom():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 10)	# 1-10
    ScreenShake(6000, 6000)
    GFX_2('kaef_lastpunch_10')
    sprite('null', 10)	# 11-20
    ScreenShake(7000, 7000)
    sprite('null', 10)	# 21-30
    ScreenShake(7000, 7000)
    sprite('null', 10)	# 31-40
    ScreenShake(8000, 8000)
    sprite('null', 10)	# 41-50
    ScreenShake(8000, 8000)
    sprite('null', 10)	# 51-60
    ScreenShake(9000, 9000)
    sprite('null', 10)	# 61-70
    ScreenShake(9000, 9000)
    sprite('null', 10)	# 71-80
    ScreenShake(10000, 10000)
    sprite('null', 10)	# 81-90
    ScreenShake(10000, 10000)
    sprite('null', 10)	# 91-100
    ScreenShake(11000, 11000)
    sprite('null', 10)	# 101-110
    sprite('null', 10)	# 111-120
    sprite('null', 10)	# 121-130
    sprite('null', 10)	# 131-140
    sprite('null', 10)	# 141-150
    sprite('null', 10)	# 151-160
    sprite('null', 10)	# 161-170
    sprite('null', 10)	# 171-180
    sprite('null', 10)	# 181-190

@State
def ta450_Black():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23015(1)
        Unknown2019(-100)
        Unknown4061(2)
    sprite('vr_ta450_white', 160)	# 1-160
    Unknown3026(-16777216)
    sprite('vr_ta450_white', 10)	# 161-170
    Unknown3001(230)

@State
def UltimateThrowCamera():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    label(0)
    sprite('keep', 32767)	# 1-32767
    Unknown1086(22)
    Unknown20000(1)
    Unknown20003(1)
    teleportRelativeY(0)
    label(1)
    sprite('keep', 70)	# 32768-32837
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
    sprite('keep', 32767)	# 1-32767
    Unknown1086(3)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(1)
    sprite('keep', 10)	# 32768-32777
    physicsYImpulse(30000)
    sprite('keep', 7)	# 32778-32784
    Unknown4004('534345465f41737452797568616955707065720000000000000000000000000064000000')
    sprite('keep', 15)	# 32785-32799
    sprite('keep', 5)	# 32800-32804
    Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
    sprite('keep', 10)	# 32805-32814
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    physicsYImpulse(100000)
    sprite('keep', 5)	# 32815-32819
    Unknown20009(1300)
    teleportRelativeY(3800000)
    Unknown1000(0)
    Unknown1084(1)
    Unknown21007(3, 40)
    sprite('keep', 3)	# 32820-32822
    Unknown26('SCEF_AstRyuhaiUpper')
    sprite('keep', 3)	# 32823-32825
    Unknown4004('534345465f5368617368614f757400000000000000000000000000000000000064000000')
    sprite('keep', 5)	# 32826-32830
    sprite('keep', 32767)	# 32831-65597
    Unknown26('SCEF_ShashaIn')
    Unknown1084(1)
    label(2)
    sprite('keep', 70)	# 65598-65667
    Unknown20001(1)
    Unknown20009(1000)
    Unknown1007(-1500000)
    Unknown20007(1)
    GFX_0('ta450_Thunder', 100)
    GFX_0('ta450_Light', 100)
    sprite('keep', 10)	# 65668-65677
    Unknown4004('534345465f527975686169596f6b6f000000000000000000000000000000000064000000')
    sprite('keep', 60)	# 65678-65737
    sprite('keep', 32767)	# 65738-98504
    label(3)
    sprite('keep', 32767)	# 98505-131271
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
    sprite('keep', 1)	# 131272-131272

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
    sprite('null', 14)	# 1-14
    sprite('ichigeki0', 16)	# 15-30
    physicsXImpulse(-80000)
    Unknown3004(9)
    sprite('ichigeki0', 32767)	# 31-32797
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
    sprite('null', 14)	# 1-14
    sprite('ichigeki1', 16)	# 15-30
    physicsXImpulse(80000)
    Unknown3004(9)
    sprite('ichigeki1', 32767)	# 31-32797
    physicsXImpulse(0)

@State
def IchigekiPicture3():

    def upon_IMMEDIATE():
        Unknown2019(0)
        Unknown6001(1)
        Unknown2007()
        Unknown4061(7)
        Unknown1000(0)
    sprite('vr_ka450_99c', 100)	# 1-100
    sprite('vr_ka450_99c', 1)	# 101-101
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
    sprite('null', 10)	# 1-10
    GFX_0('IchigekiPicture6', 0)
    sprite('vr_ka450_30', 4)	# 11-14
    GFX_0('IchigekiPicture5', 0)
    sprite('vr_ka450_31', 4)	# 15-18
    sprite('vr_ka450_32', 4)	# 19-22
    sprite('null', 15)	# 23-37
    sprite('vr_ka450_33', 4)	# 38-41
    sprite('vr_ka450_30', 4)	# 42-45
    sprite('null', 15)	# 46-60
    sprite('vr_ka450_31', 4)	# 61-64
    sprite('vr_ka450_32', 4)	# 65-68
    sprite('null', 15)	# 69-83
    sprite('vr_ka450_33', 4)	# 84-87
    sprite('vr_ka450_30', 4)	# 88-91

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
    sprite('vr_ka450_40', 2)	# 1-2
    teleportRelativeY(50000)
    sprite('null', 4)	# 3-6
    sprite('vr_ka450_41', 2)	# 7-8
    sprite('null', 4)	# 9-12
    teleportRelativeY(50000)
    sprite('vr_ka450_42', 2)	# 13-14
    sprite('null', 4)	# 15-18
    sprite('vr_ka450_43', 2)	# 19-20
    sprite('vr_ka450_40', 2)	# 21-22
    teleportRelativeY(0)
    sprite('null', 4)	# 23-26
    sprite('vr_ka450_41', 2)	# 27-28
    sprite('null', 4)	# 29-32
    sprite('vr_ka450_42', 2)	# 33-34
    teleportRelativeY(50000)
    sprite('null', 4)	# 35-38
    sprite('vr_ka450_43', 2)	# 39-40
    sprite('vr_ka450_40', 2)	# 41-42
    teleportRelativeY(0)
    sprite('null', 4)	# 43-46
    sprite('vr_ka450_41', 2)	# 47-48
    sprite('null', 4)	# 49-52
    sprite('vr_ka450_42', 2)	# 53-54
    sprite('null', 4)	# 55-58
    sprite('vr_ka450_43', 2)	# 59-60
    teleportRelativeY(50000)
    sprite('vr_ka450_40', 2)	# 61-62
    sprite('null', 4)	# 63-66
    sprite('vr_ka450_41', 2)	# 67-68
    sprite('null', 4)	# 69-72
    sprite('vr_ka450_42', 2)	# 73-74
    teleportRelativeY(0)
    sprite('null', 4)	# 75-78
    sprite('vr_ka450_43', 2)	# 79-80
    sprite('vr_ka450_40', 2)	# 81-82
    sprite('null', 4)	# 83-86
    sprite('vr_ka450_41', 2)	# 87-88
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
    sprite('vr_ka450_34', 4)	# 1-4
    sprite('vr_ka450_35', 4)	# 5-8
    sprite('vr_ka450_36', 102)	# 9-110
    sprite('vr_ka450_35', 2)	# 111-112

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
    sprite('bc_Cutintest', 8)	# 1-8
    Unknown3032()
    teleportRelativeX(-940000)
    physicsXImpulse(65000)
    physicsYImpulse(6500)
    Unknown3001(0)
    Unknown3004(40)
    Unknown1096(840)
    Unknown1099(20)
    sprite('bc_Cutintest', 30)	# 9-38
    Unknown1019(50)
    YAccel(50)
    Unknown1019(5)
    YAccel(5)
    Unknown3031()
    Unknown1099(0)
    Unknown1096(1000)
    sprite('bc_Cutintest', 15)	# 39-53
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
    sprite('null', 32767)	# 1-32767
    Unknown3004(30)
    label(1)
    sprite('null', 160)	# 32768-32927
    Unknown1007(-1600000)

@State
def kaef_450smoke():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('kaef_450bg')
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767

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

@State
def Entry_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        teleportRelativeX(128000)
    sprite('vr_ka601_00', 32767)	# 1-32767
    physicsYImpulse(3200)
    physicsXImpulse(25600)
    setGravity(800)
    Unknown1028(-800)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('null', 1)	# 32768-32768
    GFX_0('Entry_2b', 100)
    GFX_0('Entry_2c', 100)

@State
def Entry_2b():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
    sprite('vr_ka601_10', 3)	# 1-3
    sprite('vr_ka601_11', 3)	# 4-6
    sprite('vr_ka601_10', 3)	# 7-9
    sprite('vr_ka601_12', 3)	# 10-12
    sprite('vr_ka601_13', 16)	# 13-28
    sprite('vr_ka601_13', 32)	# 29-60
    Unknown3004(-8)

@State
def Entry_2c():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        teleportRelativeX(-96000)
    sprite('vr_ka601_20', 60)	# 1-60
    Unknown1099(3)
    GFX_1('kaef_entry2', 100)
    sprite('vr_ka601_20', 32)	# 61-92
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
    sprite('kaef611_00', 3)	# 1-3
    sprite('kaef611_01', 3)	# 4-6
    sprite('kaef611_02', 3)	# 7-9
    sprite('kaef611_03', 30)	# 10-39
    SFX_3('ka004')
    Unknown1007(640000)
    ScreenShake(16000, 0)
    Unknown23015(3)
    sprite('kaef611_03', 32767)	# 40-32806
    physicsYImpulse(-10000)