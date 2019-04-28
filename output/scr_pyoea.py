@State
def PYO_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('50594f5f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PYO_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PYO_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PYO_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 101):
            Unknown23185('50594f5f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 104):
            Unknown23185('50594f5f506572736f6e6158000000000000000000000000000000000000000032000000')
        if (SLOT_48 == 102):
            Unknown23185('50594f5f506572736f6e6136430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 201):
            Unknown23185('50594f5f506572736f6e6132430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 301):
            Unknown23185('50594f5f506572736f6e6141495235430000000000000000000000000000000032000000')
        if (SLOT_48 == 401):
            Unknown23185('50594f5f506572736f6e6154656e74617261687500000000000000000000000032000000')
        if (SLOT_48 == 441):
            Unknown23185('50594f5f506572736f6e61526576657273616c0000000000000000000000000032000000')
        if (SLOT_48 == 421):
            Unknown23185('50594f5f506572736f6e6157617270000000000000000000000000000000000064000000')
        if (SLOT_48 == 431):
            Unknown23185('50594f5f506572736f6e6156536c61736800000000000000000000000000000064000000')
        if (SLOT_48 == 432):
            Unknown23185('50594f5f506572736f6e6156536c61736845780000000000000000000000000064000000')
        if (SLOT_48 == 433):
            Unknown23185('50594f5f506572736f6e6156536c61736845780000000000000000000000000064000000')
        if (SLOT_48 == 501):
            Unknown23185('50594f5f506572736f6e61556c74696d61746554617473756d616b6900000000c8000000')
        if (SLOT_48 == 502):
            Unknown23185('50594f5f506572736f6e61556c74696d61746554617473756d616b694f440000c8000000')
        if (SLOT_48 == 511):
            Unknown23185('50594f5f556c74696d61746553756b756b616a61000000000000000000000000c8000000')
        if (SLOT_48 == 521):
            Unknown23185('50594f5f506572736f6e61556c74696d6174654b756e61690000000000000000c8000000')
        if (SLOT_48 == 522):
            Unknown23185('50594f5f506572736f6e61556c74696d6174654b756e61694f44000000000000c8000000')
        if (SLOT_48 == 151):
            Unknown23185('50594f5f506572736f6e6157617270544147000000000000000000000000000032000000')
        if (SLOT_48 == 154):
            Unknown23185('50594f5f506572736f6e6154656e7461726168755f544147000000000000000032000000')
        if (SLOT_48 == 152):
            Unknown23185('50594f5f506572736f6e61556c74696d61746554617473756d616b6954414700c8000000')
        if (SLOT_48 == 153):
            Unknown23185('50594f5f506572736f6e61556c74696d61746554617473756d616b694f445400c8000000')
        if (SLOT_48 == 601):
            Unknown23185('506572736f6e614963686967656b690000000000000000000000000000000000c8000000')
        if (SLOT_48 == 10):
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
def PYO_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PYO_AttackInit():
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
    callSubroutine('PYO_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PYO_SPAttackInit():
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
    callSubroutine('PYO_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PYO_DDAttackInit():
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
    callSubroutine('PYO_ReceptionSignal')
    Unknown23023()

@Subroutine
def PYO_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PYO_ForceWarp():
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
    enterState('PYO_PersonaWait')

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
        callSubroutine('PYO_ReceptionSignal')
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
def PYO_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000040420f000000000000000000')
        callSubroutine('PYO_AttackInit')
        AttackLevel_(4)
        Damage(1500)
        AttackP1(90)
        AirPushbackX(20000)
        AirPushbackY(26000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown4007(3)
        Unknown23078(1)
        callSubroutine('PYO_CheckWarp')
    sprite('ji204_00', 3)	# 1-3
    Unknown2006()
    sprite('ji204_01', 1)	# 4-4
    physicsXImpulse(40000)
    sprite('ji204_01', 1)	# 5-5
    Unknown1019(80)
    sprite('ji204_01', 1)	# 6-6
    Unknown1019(80)
    sprite('ji204_01', 1)	# 7-7
    Unknown1019(80)
    sprite('ji204_01', 1)	# 8-8
    Unknown1019(80)
    sprite('ji204_03', 3)	# 9-11	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_0('Zanzoh5C_', 100)
    SFX_3('hit_m_slow')
    sprite('ji204_04', 4)	# 12-15
    Unknown23027()
    Unknown2017(0)
    sprite('ji204_05', 4)	# 16-19
    SFX_3('cloth_l')
    sprite('ji204_03', 4)	# 20-23	 **attackbox here**
    sprite('ji204_04', 4)	# 24-27
    sprite('ji204_05', 4)	# 28-31
    SFX_3('cloth_l')
    sprite('ji204_03', 4)	# 32-35	 **attackbox here**
    sprite('ji204_04', 4)	# 36-39
    sprite('ji204_05', 4)	# 40-43
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 44-32810
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaX():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e000000000000000000')
        callSubroutine('PYO_AttackInit')
        Unknown4007(3)
        Unknown23078(1)
        callSubroutine('PYO_CheckWarp')
        Unknown23022(1)
        Unknown2003(1)
    sprite('ji204_00', 3)	# 1-3
    Unknown2006()
    sprite('ji204_01', 1)	# 4-4
    physicsXImpulse(30000)
    sprite('ji204_01', 1)	# 5-5
    Unknown1019(80)
    sprite('ji204_01', 1)	# 6-6
    Unknown1019(80)
    sprite('ji204_01', 1)	# 7-7
    Unknown1019(80)
    sprite('ji204_01', 1)	# 8-8
    Unknown1019(80)
    sprite('ji204_03', 3)	# 9-11	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_0('Zanzoh5C_', 100)
    SFX_3('hit_m_slow')
    sprite('ji204_04', 4)	# 12-15
    Unknown23027()
    Unknown2017(0)
    sprite('ji204_05', 4)	# 16-19
    SFX_3('cloth_l')
    sprite('ji204_03', 4)	# 20-23	 **attackbox here**
    sprite('ji204_04', 4)	# 24-27
    sprite('ji204_05', 4)	# 28-31
    SFX_3('cloth_l')
    sprite('ji204_03', 4)	# 32-35	 **attackbox here**
    sprite('ji204_04', 4)	# 36-39
    sprite('ji204_05', 4)	# 40-43
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 44-32810
    enterState('PersonaDeleteAndIdling')

@State
def PYO_Persona2C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PYO_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        Unknown9016(1)
        AirPushbackX(8000)
        AirPushbackY(12000)
        AirUntechableTime(30)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23078(1)
        callSubroutine('PYO_CheckWarp')
        Unknown2017(1)
        Unknown2053(1)
    sprite('ji232_00', 6)	# 1-6
    sprite('ji232_01', 2)	# 7-8
    sprite('ji232_02', 2)	# 9-10
    GFX_0('Zanzoh2C', 100)
    physicsXImpulse(60000)
    sprite('ji232_03', 2)	# 11-12
    SFX_3('slash_sword_slow')
    sprite('ji232_04', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Unknown4007(0)
    physicsXImpulse(0)
    sprite('ji232_06', 4)	# 15-18
    Unknown23027()
    sprite('ji232_07', 4)	# 19-22
    sprite('ji232_06', 4)	# 23-26
    SFX_3('cloth_l')
    sprite('ji232_07', 4)	# 27-30
    sprite('ji232_06', 4)	# 31-34
    sprite('ji232_07', 4)	# 35-38
    SFX_3('cloth_l')
    sprite('ji232_06', 4)	# 39-42
    sprite('ji232_07', 4)	# 43-46
    sprite('keep', 32767)	# 47-32813
    enterState('PersonaDeleteAndIdling')

@State
def PYO_Persona6C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a086010000000000807be1ff80841e000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        AttackLevel_(4)
        Damage(700)
        AttackP1(70)
        Unknown11092(1)
        AirUntechableTime(50)
        AirPushbackY(15000)
        Unknown9016(1)
        PushbackX(19800)
        Unknown11042(1)
        Unknown11058('0000000001000000000000000000000000000000')

        def upon_77():
            sendToLabel(0)
        callSubroutine('PYO_CheckWarp')
    sprite('ji205_00', 3)	# 1-3
    Unknown2006()
    sprite('ji205_01', 3)	# 4-6
    sprite('ji205_02', 3)	# 7-9
    sprite('ji205_03', 3)	# 10-12
    sprite('ji205_04', 6)	# 13-18
    Unknown4007(0)
    sprite('ji205_05', 6)	# 19-24
    sprite('ji205_06', 3)	# 25-27	 **attackbox here**
    GFX_0('5Dtornado01', 0)
    GFX_0('5Dtornado00', 0)
    physicsXImpulse(30000)
    Unknown30032(1)
    sprite('ji205_07', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(60000)
    SFX_3('yo010')
    sprite('ji205_06', 3)	# 31-33	 **attackbox here**
    sprite('ji205_07', 3)	# 34-36	 **attackbox here**
    sprite('ji205_06', 3)	# 37-39	 **attackbox here**
    sprite('ji205_07', 3)	# 40-42	 **attackbox here**
    sprite('ji205_08', 4)	# 43-46
    Unknown1019(30)
    sprite('ji205_09', 4)	# 47-50
    Unknown1019(60)
    sprite('ji205_10', 4)	# 51-54
    Unknown1019(60)
    sprite('ji205_11', 4)	# 55-58
    Unknown1019(60)
    sprite('ji205_12', 4)	# 59-62
    Unknown1019(60)
    SFX_0('cloth_l')
    sprite('ji205_10', 4)	# 63-66
    Unknown1019(60)
    sprite('ji205_11', 4)	# 67-70
    Unknown1019(60)
    sprite('ji205_12', 4)	# 71-74
    Unknown1019(0)
    SFX_0('cloth_l')
    sprite('ji205_10', 4)	# 75-78
    sprite('ji205_11', 4)	# 79-82
    sprite('ji205_12', 4)	# 83-86
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('keep', 3)	# 87-89
    Unknown21015('436d6e4163744368616e6765506172746e657241737369737441746b5f4100009b00000000000000')
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(15000)
    AirPushbackY(40000)
    Hitstop(1)
    Unknown23027()
    clearUponHandler(77)
    physicsXImpulse(40000)
    clearUponHandler(10)
    sprite('ji206_00', 3)	# 90-92
    Unknown1019(60)
    sprite('ji206_01', 3)	# 93-95
    Unknown1019(60)
    sprite('ji206_02', 3)	# 96-98	 **attackbox here**
    RefreshMultihit()
    Unknown1019(60)
    SFX_3('yo010')
    sprite('ji206_04', 3)	# 99-101	 **attackbox here**
    RefreshMultihit()
    Unknown1019(30)
    sprite('ji206_05', 4)	# 102-105	 **attackbox here**
    RefreshMultihit()
    Unknown1019(60)
    sprite('ji206_06', 4)	# 106-109
    Unknown1019(60)
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 110-113	 **attackbox here**
    Unknown1019(0)
    Unknown23027()
    sprite('ji206_05', 4)	# 114-117	 **attackbox here**
    sprite('ji206_06', 4)	# 118-121
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 122-125	 **attackbox here**
    sprite('ji206_05', 4)	# 126-129	 **attackbox here**
    sprite('ji206_06', 4)	# 130-133
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 134-137	 **attackbox here**
    sprite('ji206_05', 4)	# 138-141	 **attackbox here**
    sprite('ji206_06', 4)	# 142-145
    label(9)
    sprite('keep', 32767)	# 146-32912
    enterState('PersonaDeleteAndIdling')

@State
def PYO_Persona6CAdd():

    def upon_IMMEDIATE():
        callSubroutine('PYO_AttackInit')
        AttackLevel_(3)
        Hitstop(1)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        AirPushbackY(45000)
        AirPushbackX(18000)
        SLOT_9 = 0
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_9 = 0
            SLOT_10 = 0
    sprite('ji206_00', 3)	# 1-3
    physicsXImpulse(40000)
    clearUponHandler(10)
    sprite('ji206_01', 3)	# 4-6
    Unknown1019(60)
    sprite('ji206_02', 3)	# 7-9	 **attackbox here**
    RefreshMultihit()
    Unknown1019(60)
    SFX_3('yo010')
    sprite('ji206_04', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    Unknown9016(1)
    Unknown1019(30)
    sprite('ji206_05', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    Unknown9016(1)
    Unknown1019(60)
    sprite('ji206_06', 4)	# 17-20
    Unknown1019(60)
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 21-24	 **attackbox here**
    Unknown1019(0)
    Unknown23027()
    sprite('ji206_05', 4)	# 25-28	 **attackbox here**
    Unknown23027()
    sprite('ji206_06', 4)	# 29-32
    SFX_0('cloth_l')
    SLOT_10 = 0
    sprite('ji206_04', 4)	# 33-36	 **attackbox here**
    Unknown23027()
    sprite('ji206_05', 4)	# 37-40	 **attackbox here**
    Unknown23027()
    sprite('ji206_06', 4)	# 41-44
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 45-48	 **attackbox here**
    Unknown23027()
    sprite('ji206_05', 4)	# 49-52	 **attackbox here**
    Unknown23027()
    sprite('ji206_06', 4)	# 53-56
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 57-60	 **attackbox here**
    Unknown23027()
    sprite('ji206_05', 4)	# 61-64	 **attackbox here**
    Unknown23027()
    sprite('ji206_06', 4)	# 65-68
    SFX_0('cloth_l')
    sprite('ji206_04', 4)	# 69-72	 **attackbox here**
    Unknown23027()
    sprite('ji206_05', 4)	# 73-76	 **attackbox here**
    Unknown23027()
    sprite('keep', 32767)	# 77-32843
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaAIR5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000b03cffff00000000000000000000000000000000')
        callSubroutine('PYO_AttackInit')
        AttackLevel_(3)
        Damage(720)
        AttackP1(80)
        Unknown11092(1)
        Unknown9016(1)
        Hitstop(1)
        Unknown11001(1, 1, 1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown23078(1)
        callSubroutine('PYO_ForceWarp')

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            if (SLOT_2 >= 3):
                Unknown2003(1)
        Unknown4007(3)

        def upon_43():
            if (SLOT_48 == 3001):
                sendToLabel(0)
            if (SLOT_48 == 3003):
                sendToLabel(0)
        Unknown2017(0)
        Unknown2053(1)
    sprite('ji254_00', 5)	# 1-5
    physicsXImpulse(8000)
    sprite('ji254_01', 3)	# 6-8
    Unknown1019(80)
    YAccel(80)
    SFX_3('yo008')
    sprite('ji254_02', 3)	# 9-11
    Unknown1019(80)
    YAccel(80)
    sprite('ji254_03', 1)	# 12-12	 **attackbox here**
    Unknown1019(0)
    YAccel(0)
    RefreshMultihit()
    GFX_0('Air5Ctornado00', 0)
    SFX_3('yo008')
    sprite('ji254_03', 2)	# 13-14	 **attackbox here**
    Unknown23022(0)
    sprite('ji254_04', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_03', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_04', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    SFX_3('cloth_l')
    sprite('ji254_03', 3)	# 24-26	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_04', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_03', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_04', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    SFX_3('cloth_l')
    sprite('ji254_03', 3)	# 36-38	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_04', 3)	# 39-41	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_03', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    sprite('ji254_04', 3)	# 45-47	 **attackbox here**
    Unknown21015('4169723543746f726e61646f3030000000000000000000000000000000000000ba0b000000000000')
    Unknown23027()
    SFX_3('cloth_l')
    sprite('ji254_03', 5)	# 48-52	 **attackbox here**
    sprite('ji254_04', 5)	# 53-57	 **attackbox here**
    sprite('ji254_03', 5)	# 58-62	 **attackbox here**
    sprite('ji254_04', 5)	# 63-67	 **attackbox here**
    SFX_3('cloth_l')
    sprite('ji254_03', 5)	# 68-72	 **attackbox here**
    sprite('ji254_04', 5)	# 73-77	 **attackbox here**
    label(0)
    sprite('keep', 32767)	# 78-32844
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaTentarahu():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        AttackLevel_(4)
        AttackP1(90)
        Unknown11066(1)
        Damage(0)
        Unknown11031(0)
        Unknown11091(0)
        Unknown9021(1)
        Unknown9154(60)
        Unknown11032('60c00700e0a501003075000000000000')
        Unknown30055('20b304003200000000000000')
        Hitstop(0)
        PushbackX(12000)
        Unknown11092(1)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown11044(1)
        Unknown11042(1)
        Unknown11068(1)
        Unknown30048(1)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown23027()
        callSubroutine('PYO_CheckWarp')
        Unknown23078(1)
        Unknown4007(3)
        Unknown2017(1)
        Unknown2053(1)

        def upon_78():
            sendToLabel(1)
            setInvincible(1)
            clearUponHandler(78)
            Unknown23029(3, 4001, 0)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0

        def upon_61():
            PushbackX(30400)
            Hitstop(12)
    sprite('ji402_00', 2)	# 1-2
    Unknown2006()
    SLOT_67 = SLOT_19
    if (SLOT_67 > 1070000):
        SLOT_67 = 1070000
    if (SLOT_67 < 750000):
        SLOT_67 = 750000
    SLOT_12 = SLOT_67
    Unknown1019(4)
    sprite('ji402_02', 2)	# 3-4
    Unknown3029(1)
    sprite('ji402_03', 2)	# 5-6
    Unknown1019(80)
    sprite('ji402_04', 2)	# 7-8	 **attackbox here**
    Unknown1019(70)
    sprite('ji402_05', 2)	# 9-10	 **attackbox here**
    Unknown1019(0)
    GFX_0('Tentarafu_BindMark', 0)
    ScreenShake(0, 12000)
    RefreshMultihit()
    sprite('ji402_06', 4)	# 11-14	 **attackbox here**
    Unknown2001()
    sprite('ji402_05', 4)	# 15-18	 **attackbox here**
    physicsXImpulse(0)
    SFX_3('cloth_l')
    sprite('ji402_06', 4)	# 19-22	 **attackbox here**
    sprite('ji402_05', 4)	# 23-26	 **attackbox here**
    Unknown3029(0)
    sprite('ji402_06', 4)	# 27-30	 **attackbox here**
    SFX_3('cloth_l')
    sprite('ji402_05', 4)	# 31-34	 **attackbox here**
    sprite('ji402_06', 4)	# 35-38	 **attackbox here**
    sprite('ji402_05', 4)	# 39-42	 **attackbox here**
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 43-32809
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('ji402_05', 3)	# 32810-32812	 **attackbox here**
    Unknown1084(1)
    Unknown23027()
    sprite('ji402_06', 3)	# 32813-32815	 **attackbox here**
    sprite('ji402_05', 3)	# 32816-32818	 **attackbox here**
    sprite('ji402_06', 3)	# 32819-32821	 **attackbox here**
    sprite('ji402_05', 3)	# 32822-32824	 **attackbox here**
    sprite('ji402_06', 3)	# 32825-32827	 **attackbox here**
    sprite('ji402_05', 3)	# 32828-32830	 **attackbox here**
    sprite('ji402_07', 3)	# 32831-32833
    sprite('ji402_08', 3)	# 32834-32836
    sprite('ji402_09', 3)	# 32837-32839
    sprite('ji402_10', 3)	# 32840-32842
    sprite('ji402_11', 3)	# 32843-32845
    SFX_3('yo004')
    sprite('ji402_12', 3)	# 32846-32848
    sprite('ji402_13', 8)	# 32849-32856
    sprite('ji402_14', 3)	# 32857-32859
    sprite('ji402_15', 3)	# 32860-32862	 **attackbox here**
    sprite('ji402_16', 3)	# 32863-32865	 **attackbox here**
    GFX_1('jief_tentarasmoke_11', 0)
    SFX_3('yo002')
    sprite('ji402_17', 3)	# 32866-32868	 **attackbox here**
    RefreshMultihit()
    Damage(2400)
    Hitstop(0)
    Unknown11066(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirUntechableTime(60)
    AirPushbackX(0)
    AirPushbackY(32000)
    YImpluseBeforeWallbounce(1600)
    Unknown9021(1)
    Unknown30055('000000000000000000000000')
    Unknown23066(1)
    sprite('ji402_18', 10)	# 32869-32878	 **attackbox here**
    sprite('ji402_18', 15)	# 32879-32893	 **attackbox here**
    sprite('keep', 32767)	# 32894-65660
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaTentarahu_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        Unknown2010()
        Hitstop(0)
        Unknown11066(1)
        Damage(100)
        Unknown9021(1)
        Unknown9154(20)
        Unknown11032('60c00700e0a501003075000000000000')
        Unknown30055('20b304001400000000000000')
        Unknown11092(1)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown11044(1)
        Unknown11042(1)
        Unknown11068(1)
        Unknown30048(1)
        callSubroutine('PYO_CheckWarp')
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown4007(3)
        Unknown2017(1)
        Unknown2053(1)

        def upon_78():
            sendToLabel(1)
            clearUponHandler(78)
            Unknown23029(3, 4001, 0)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0

        def upon_61():
            Hitstop(5)
    sprite('ji402_00', 3)	# 1-3
    SLOT_67 = SLOT_19
    if (SLOT_67 > 1070000):
        SLOT_67 = 1070000
    if (SLOT_67 < 750000):
        SLOT_67 = 750000
    SLOT_12 = SLOT_67
    Unknown1019(8)
    Unknown1019(80)
    sprite('ji402_01', 2)	# 4-5
    setInvincible(1)
    sprite('ji402_02', 4)	# 6-9
    Unknown3029(1)
    sprite('ji402_03', 2)	# 10-11
    Unknown1019(80)
    sprite('ji402_04', 2)	# 12-13	 **attackbox here**
    Unknown1019(70)
    sprite('ji402_05', 1)	# 14-14	 **attackbox here**
    sprite('ji402_05', 1)	# 15-15	 **attackbox here**
    Unknown1019(0)
    GFX_0('Tentarafu_BindMark', 0)
    ScreenShake(0, 12000)
    RefreshMultihit()
    sprite('ji402_06', 4)	# 16-19	 **attackbox here**
    Unknown2001()
    setInvincible(0)
    sprite('ji402_05', 4)	# 20-23	 **attackbox here**
    physicsXImpulse(0)
    SFX_3('cloth_l')
    sprite('ji402_06', 4)	# 24-27	 **attackbox here**
    sprite('ji402_05', 4)	# 28-31	 **attackbox here**
    Unknown3029(0)
    sprite('ji402_06', 4)	# 32-35	 **attackbox here**
    SFX_3('cloth_l')
    sprite('ji402_05', 4)	# 36-39	 **attackbox here**
    sprite('ji402_06', 4)	# 40-43	 **attackbox here**
    sprite('ji402_05', 4)	# 44-47	 **attackbox here**
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 48-32814
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('ji402_05', 3)	# 32815-32817	 **attackbox here**
    Unknown1084(1)
    setInvincible(1)
    RefreshMultihit()
    Damage(0)
    Unknown9154(60)
    GFX_0('Tentarafu_BindMark', 0)
    sprite('ji402_06', 3)	# 32818-32820	 **attackbox here**
    sprite('ji402_05', 3)	# 32821-32823	 **attackbox here**
    sprite('ji402_06', 3)	# 32824-32826	 **attackbox here**
    sprite('ji402_05', 3)	# 32827-32829	 **attackbox here**
    sprite('ji402_06', 3)	# 32830-32832	 **attackbox here**
    sprite('ji402_05', 3)	# 32833-32835	 **attackbox here**
    sprite('ji402_07', 3)	# 32836-32838
    sprite('ji402_08', 3)	# 32839-32841
    sprite('ji402_09', 3)	# 32842-32844
    sprite('ji402_10', 3)	# 32845-32847
    sprite('ji402_11', 3)	# 32848-32850
    SFX_3('yo004')
    sprite('ji402_12', 3)	# 32851-32853
    sprite('ji402_13', 8)	# 32854-32861
    sprite('ji402_14', 3)	# 32862-32864
    sprite('ji402_15', 3)	# 32865-32867	 **attackbox here**
    sprite('ji402_16', 3)	# 32868-32870	 **attackbox here**
    GFX_1('jief_tentarasmoke_11', 0)
    SFX_3('yo002')
    sprite('ji402_17', 3)	# 32871-32873	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(3)
    Damage(1300)
    Hitstop(0)
    Unknown11066(0)
    AirUntechableTime(60)
    GroundedHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(30000)
    YImpluseBeforeWallbounce(1600)
    Unknown9021(1)
    Unknown30055('000000000000000000000000')
    Unknown23066(1)
    sprite('ji402_18', 10)	# 32874-32883	 **attackbox here**
    sprite('ji402_18', 15)	# 32884-32898	 **attackbox here**
    sprite('keep', 32767)	# 32899-65665
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaReversal():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff0000000000000000000000000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        AttackLevel_(4)
        Damage(2200)
        Unknown11091(5)
        Unknown30065(100)
        AttackP1(80)
        AttackP2(60)
        AirUntechableTime(50)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(22000)
        AirPushbackY(28000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11064(0)
        Unknown11044(1)
        Unknown11001(0, -8, -8)
        Unknown4007(3)
        Unknown23078(1)
        callSubroutine('PYO_ForceWarp')
        setInvincible(1)
    sprite('ji204_00', 3)	# 1-3
    Unknown2006()
    sprite('ji204_01', 1)	# 4-4
    physicsXImpulse(85000)
    sprite('ji204_01', 1)	# 5-5
    Unknown1019(80)
    sprite('ji204_01', 1)	# 6-6
    Unknown1019(80)
    sprite('ji204_01', 1)	# 7-7
    Unknown1019(80)
    sprite('ji204_01', 1)	# 8-8
    Unknown1019(80)
    sprite('ji204_03ex01', 3)	# 9-11	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    GFX_0('Zanzoh5C_', 100)
    SFX_3('hit_m_slow')
    sprite('ji204_04', 4)	# 12-15
    Unknown23027()
    Unknown2017(0)
    sprite('ji204_05', 4)	# 16-19
    SFX_3('cloth_l')
    setInvincible(0)
    sprite('ji204_03', 4)	# 20-23	 **attackbox here**
    sprite('ji204_04', 4)	# 24-27
    sprite('ji204_05', 4)	# 28-31
    SFX_3('cloth_l')
    sprite('ji204_03', 4)	# 32-35	 **attackbox here**
    sprite('ji204_04', 4)	# 36-39
    sprite('ji204_05', 4)	# 40-43
    SFX_3('cloth_l')
    sprite('keep', 32767)	# 44-32810
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaVSlash():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000b03cffff00000000000000000000000000000000')
        callSubroutine('PYO_AttackInit')
        Unknown2009()
        callSubroutine('PYO_ForceWarp')
        Unknown23022(1)
        Unknown2017(0)
        Unknown4007(3)
    sprite('ji407_00', 2)	# 1-2
    sprite('ji407_01', 3)	# 3-5
    Unknown4007(0)
    sprite('ji407_02', 3)	# 6-8
    sprite('ji407_03', 3)	# 9-11
    sprite('ji407_04', 3)	# 12-14
    sprite('ji407_05', 3)	# 15-17
    Unknown23022(0)
    sprite('ji407_06', 3)	# 18-20
    sprite('ji407_07', 3)	# 21-23
    sprite('ji407_05', 3)	# 24-26
    sprite('ji407_06', 3)	# 27-29
    sprite('ji407_07', 3)	# 30-32
    sprite('keep', 32767)	# 33-32799
    enterState('PersonaDeleteAndIdling')
    loopRest()

@State
def PYO_PersonaVSlashEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000b03cffff00000000000000000000000000000000')
        callSubroutine('PYO_AttackInit')
        Unknown2009()
        callSubroutine('PYO_ForceWarp')
        Unknown23022(1)
        Unknown2017(0)
        Unknown4007(3)
    sprite('ji407_00', 7)	# 1-7
    sprite('ji407_01', 3)	# 8-10
    Unknown4007(0)
    sprite('ji407_02', 3)	# 11-13
    sprite('ji407_03', 3)	# 14-16
    sprite('ji407_04', 3)	# 17-19
    sprite('ji407_05', 3)	# 20-22
    Unknown23022(0)
    sprite('ji407_06', 3)	# 23-25
    sprite('ji407_07', 3)	# 26-28
    sprite('ji407_05', 3)	# 29-31
    sprite('ji407_06', 3)	# 32-34
    sprite('keep', 32767)	# 35-32801
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaVSlashEx_2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000e05ef8ff00000000000000000000000000000000')
        callSubroutine('PYO_AttackInit')
        Unknown2009()
        callSubroutine('PYO_ForceWarp')
        Unknown23022(1)
        Unknown4007(3)
        Unknown2017(0)
    sprite('ji407_00', 1)	# 1-1
    Unknown4007(0)
    sprite('ji407_01', 1)	# 2-2
    sprite('ji407_02', 2)	# 3-4
    sprite('ji407_03', 2)	# 5-6
    sprite('ji407_04', 3)	# 7-9
    sprite('ji407_05', 3)	# 10-12
    Unknown23022(0)
    sprite('ji407_06', 3)	# 13-15
    sprite('ji407_07', 3)	# 16-18
    sprite('ji407_05', 3)	# 19-21
    sprite('ji407_06', 3)	# 22-24
    sprite('keep', 32767)	# 25-32791
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaWarp():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000089feff0089feff00000000000000000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        Unknown23022(1)
        Unknown2009()
        callSubroutine('PYO_ForceWarp')
    sprite('ji406_00', 2)	# 1-2
    sprite('ji406_01', 3)	# 3-5
    sprite('ji406_02', 3)	# 6-8
    sprite('ji406_50', 3)	# 9-11
    GFX_0('WarpSmoke', 0)
    sprite('ji406_03', 2)	# 12-13
    sprite('ji406_04', 2)	# 14-15
    sprite('ji406_05', 2)	# 16-17
    sprite('ji406_03', 2)	# 18-19
    sprite('ji406_04', 2)	# 20-21
    sprite('ji406_05', 2)	# 22-23
    sprite('ji406_03', 2)	# 24-25
    sprite('ji406_04', 2)	# 26-27
    sprite('ji406_05', 2)	# 28-29
    sprite('ji406_03', 2)	# 30-31
    sprite('ji406_04', 2)	# 32-33
    sprite('ji406_05', 2)	# 34-35
    sprite('ji406_03', 2)	# 36-37
    sprite('ji406_04', 2)	# 38-39
    sprite('ji406_05', 2)	# 40-41
    sprite('ji406_03', 2)	# 42-43
    sprite('ji406_04', 2)	# 44-45
    sprite('ji406_05', 2)	# 46-47
    sprite('ji406_03', 2)	# 48-49
    sprite('ji406_04', 2)	# 50-51
    sprite('ji406_05', 2)	# 52-53
    sprite('keep', 32767)	# 54-32820
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaUltimateTatsumaki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff10b6fdff0000000060ea00000000000000000000')
        callSubroutine('PYO_DDAttackInit')
        Unknown2010()
        callSubroutine('PYO_ForceWarp')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23078(0)
        Unknown23022(1)
        Unknown13024(1)
        Unknown23023()
    sprite('ji431_00', 4)	# 1-4
    sprite('ji431_01', 4)	# 5-8
    sprite('ji431_02', 4)	# 9-12
    sprite('ji431_03', 4)	# 13-16
    sprite('ji431_04', 4)	# 17-20
    sprite('ji431_05', 4)	# 21-24
    sprite('ji431_06', 4)	# 25-28
    Unknown4007(0)
    GFX_0('Tatsumaki', 100)
    sprite('ji431_07', 4)	# 29-32
    sprite('ji431_08', 4)	# 33-36
    sprite('ji431_09', 12)	# 37-48
    sprite('ji431_10', 4)	# 49-52
    ScreenShake(20000, 0)
    sprite('ji431_11', 4)	# 53-56
    sprite('ji431_12', 4)	# 57-60
    sprite('ji431_13', 4)	# 61-64
    sprite('ji431_11', 4)	# 65-68
    sprite('ji431_12', 4)	# 69-72
    sprite('ji431_13', 4)	# 73-76
    sprite('ji431_11', 5)	# 77-81
    sprite('ji431_12', 5)	# 82-86
    sprite('ji431_13', 5)	# 87-91
    sprite('ji431_11', 6)	# 92-97
    sprite('ji431_12', 6)	# 98-103
    sprite('ji431_13', 6)	# 104-109
    sprite('keep', 32767)	# 110-32876
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaUltimateTatsumakiOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff10b6fdff0000000060ea00000000000000000000')
        callSubroutine('PYO_DDAttackInit')
        Unknown2010()
        callSubroutine('PYO_ForceWarp')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23078(0)
        Unknown23022(1)
        Unknown13024(1)
        Unknown23023()
        Unknown23056('')
    sprite('ji431_00', 4)	# 1-4
    sprite('ji431_01', 4)	# 5-8
    sprite('ji431_02', 4)	# 9-12
    sprite('ji431_03', 4)	# 13-16
    sprite('ji431_04', 4)	# 17-20
    sprite('ji431_05', 4)	# 21-24
    sprite('ji431_06', 4)	# 25-28
    Unknown4007(0)
    GFX_0('TatsumakiOD', 100)
    sprite('ji431_07', 4)	# 29-32
    sprite('ji431_08', 4)	# 33-36
    sprite('ji431_09', 12)	# 37-48
    sprite('ji431_10', 4)	# 49-52
    ScreenShake(20000, 0)
    sprite('ji431_11', 4)	# 53-56
    sprite('ji431_12', 4)	# 57-60
    sprite('ji431_13', 4)	# 61-64
    sprite('ji431_11', 4)	# 65-68
    sprite('ji431_12', 4)	# 69-72
    sprite('ji431_13', 4)	# 73-76
    sprite('ji431_11', 5)	# 77-81
    sprite('ji431_12', 5)	# 82-86
    sprite('ji431_13', 5)	# 87-91
    sprite('ji431_11', 6)	# 92-97
    sprite('ji431_12', 6)	# 98-103
    sprite('ji431_13', 6)	# 104-109
    sprite('keep', 32767)	# 110-32876
    enterState('PersonaDeleteAndIdling')

@State
def PYO_UltimateSukukaja():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000060f0ffff0000000000000000000000000000000000000000')
        callSubroutine('PYO_DDAttackInit')
        Unknown23023()
        Unknown4007(3)
        Unknown4009(3)
        Unknown23022(1)
        callSubroutine('PYO_ForceWarp')

        def upon_43():
            if (SLOT_48 == 5101):
                sendToLabel(1)
    sprite('ji430_00', 6)	# 1-6
    Unknown4007(0)
    sprite('ji430_02', 4)	# 7-10
    sprite('ji430_03', 4)	# 11-14
    sprite('ji430_04', 4)	# 15-18
    Unknown3004(-26)
    GFX_0('jief_sukukaja', 100)
    label(0)
    sprite('ji430_03', 4)	# 19-22
    sprite('ji430_02', 4)	# 23-26
    sprite('ji430_03', 4)	# 27-30
    sprite('ji430_04', 4)	# 31-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 1)	# 35-35
    sprite('keep', 32767)	# 36-32802
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaUltimateKunai():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000060f0ffff0000000000000000000000000000000000000000')
        callSubroutine('PYO_DDAttackInit')
        Unknown23023()
        Unknown4007(3)
        Unknown4009(3)
        Unknown23022(1)
        callSubroutine('PYO_ForceWarp')

        def upon_43():
            if (SLOT_48 == 5101):
                sendToLabel(1)
    sprite('ji432_00', 14)	# 1-14
    sprite('ji432_01', 35)	# 15-49
    sprite('ji432_02', 4)	# 50-53
    sprite('ji432_03', 4)	# 54-57
    sprite('ji432_04', 4)	# 58-61
    sprite('ji432_03', 4)	# 62-65
    sprite('ji432_04', 4)	# 66-69
    sprite('ji432_03', 4)	# 70-73
    sprite('ji432_04', 4)	# 74-77
    sprite('ji432_03', 4)	# 78-81
    sprite('ji432_04', 4)	# 82-85
    sprite('ji432_03', 4)	# 86-89
    sprite('ji432_04', 4)	# 90-93
    sprite('ji432_03', 4)	# 94-97
    sprite('ji432_04', 4)	# 98-101
    sprite('ji432_03', 4)	# 102-105
    sprite('keep', 32767)	# 106-32872
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaUltimateKunaiOD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c300000000000010b6fdff000000000000000000000000')
        callSubroutine('PYO_DDAttackInit')
        callSubroutine('PYO_ForceWarp')
        Unknown2054(1)
        Unknown23022(1)
    sprite('ji432_00', 14)	# 1-14
    sprite('ji432_01', 35)	# 15-49
    sprite('ji432_02', 4)	# 50-53
    sprite('ji432_03', 4)	# 54-57
    sprite('ji432_04', 4)	# 58-61
    sprite('ji432_03', 4)	# 62-65
    sprite('ji432_04', 4)	# 66-69
    sprite('ji432_03', 4)	# 70-73
    sprite('ji432_04', 4)	# 74-77
    sprite('ji432_03', 4)	# 78-81
    sprite('ji432_04', 4)	# 82-85
    sprite('ji432_03', 4)	# 86-89
    sprite('ji432_04', 4)	# 90-93
    sprite('ji432_03', 4)	# 94-97
    sprite('ji432_04', 4)	# 98-101
    sprite('ji432_03', 4)	# 102-105
    sprite('ji432_04', 4)	# 106-109
    sprite('ji432_03', 4)	# 110-113
    sprite('ji432_04', 4)	# 114-117
    sprite('ji432_03', 4)	# 118-121
    sprite('ji432_04', 4)	# 122-125
    sprite('ji432_03', 4)	# 126-129
    sprite('ji432_04', 4)	# 130-133
    sprite('ji432_03', 4)	# 134-137
    sprite('ji432_04', 4)	# 138-141
    sprite('ji432_03', 4)	# 142-145
    sprite('ji432_04', 4)	# 146-149
    sprite('ji432_03', 4)	# 150-153
    sprite('ji432_04', 4)	# 154-157
    sprite('ji432_03', 4)	# 158-161
    sprite('ji432_04', 4)	# 162-165
    sprite('ji432_03', 4)	# 166-169
    sprite('ji432_04', 4)	# 170-173
    sprite('ji432_03', 4)	# 174-177
    sprite('ji432_04', 4)	# 178-181
    sprite('ji432_03', 4)	# 182-185
    sprite('ji432_04', 4)	# 186-189
    sprite('ji432_03', 4)	# 190-193
    sprite('ji432_04', 4)	# 194-197
    sprite('ji432_03', 4)	# 198-201
    sprite('ji432_04', 4)	# 202-205
    sprite('ji432_03', 4)	# 206-209
    sprite('keep', 32767)	# 210-32976
    enterState('PersonaDeleteAndIdling')

@State
def PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a08601000000000000000000000000000000000000000000')
        callSubroutine('PYO_AttackInit')
        Unknown2012()
        callSubroutine('PYO_ForceWarp')
        AttackLevel_(5)
        Damage(500)
        Unknown11091(100)
        Unknown11064(1)
        Unknown9001(6)
        Unknown4009(3)
        Unknown2054(1)
        Unknown23066(1)
        Unknown2053(1)
        Unknown2017(0)
        Unknown23022(1)

        def upon_32():
            SLOT_52 = 1
            GFX_0('IchigekiCamera', 100)
        teleportRelativeY(0)

        def upon_14():
            Unknown21012('4963686967656b6973746172743030000000000000000000000000000000000020000000')
            Unknown21012('4963686967656b69546f726e61646f303000000000000000000000000000000020000000')
            Unknown21012('4963686967656b6973746172743032000000000000000000000000000000000020000000')
    sprite('ji450_00', 30)	# 1-30
    GFX_0('IchigekiTatsumakiAtk', 100)
    Unknown3032()
    Unknown3001(0)
    sprite('ji450_00', 20)	# 31-50
    Unknown3004(26)
    GFX_0('Ichigekistart01', 0)
    sprite('ji450_01', 3)	# 51-53
    physicsXImpulse(30000)
    sprite('ji450_02', 3)	# 54-56
    sprite('ji450_03', 3)	# 57-59
    sprite('ji450_04', 4)	# 60-63
    physicsXImpulse(0)
    physicsYImpulse(3000)
    setGravity(0)
    sprite('ji450_05', 4)	# 64-67
    sprite('ji450_06', 4)	# 68-71
    sprite('ji450_07', 4)	# 72-75
    sprite('ji450_04', 4)	# 76-79
    sprite('ji450_05', 3)	# 80-82
    if (not SLOT_52):
        Unknown23022(0)
    sprite('ji450_06', 3)	# 83-85
    sprite('ji450_07', 3)	# 86-88
    sprite('ji450_04', 3)	# 89-91
    sprite('ji450_05', 3)	# 92-94
    physicsYImpulse(0)
    if SLOT_52:
        Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000020000000')
    sprite('ji450_06', 2)	# 95-96
    sprite('ji450_07', 2)	# 97-98
    sprite('ji450_04', 2)	# 99-100
    sprite('ji450_05', 2)	# 101-102
    sprite('ji450_06', 2)	# 103-104
    sprite('ji450_07', 2)	# 105-106
    sprite('ji450_04', 2)	# 107-108
    sprite('ji450_05', 2)	# 109-110
    sprite('ji450_06', 2)	# 111-112
    sprite('ji450_07', 2)	# 113-114
    sprite('ji450_04', 2)	# 115-116
    sprite('ji450_05', 2)	# 117-118
    sprite('ji450_06', 2)	# 119-120
    sprite('ji450_07', 2)	# 121-122
    sprite('ji450_04', 2)	# 123-124
    sprite('ji450_05', 2)	# 125-126
    sprite('ji450_06', 2)	# 127-128
    sprite('ji450_07', 2)	# 129-130
    sprite('ji450_04', 2)	# 131-132
    sprite('ji450_05', 2)	# 133-134
    sprite('ji450_06', 2)	# 135-136
    sprite('ji450_07', 2)	# 137-138
    if SLOT_52:
        _gotolabel(0)
    sprite('ji450_04', 2)	# 139-140
    sprite('ji450_05', 2)	# 141-142
    sprite('ji450_06', 3)	# 143-145
    sprite('ji450_07', 3)	# 146-148
    sprite('ji450_04', 3)	# 149-151
    sprite('ji450_05', 3)	# 152-154
    sprite('ji450_06', 3)	# 155-157
    sprite('ji450_07', 4)	# 158-161
    sprite('ji450_04', 4)	# 162-165
    sprite('ji450_05', 4)	# 166-169
    sprite('ji450_06', 4)	# 170-173
    sprite('ji450_07', 5)	# 174-178
    sprite('ji450_04', 5)	# 179-183
    sprite('ji450_05', 5)	# 184-188
    setGravity(1000)
    Unknown23022(0)
    sprite('ji450_08', 4)	# 189-192
    sprite('ji450_09', 4)	# 193-196
    sprite('ji450_10', 3)	# 197-199
    sprite('ji450_11', 3)	# 200-202
    sprite('keep', 32767)	# 203-32969
    enterState('PersonaDeleteAndIdling')
    label(0)
    sprite('ji450_13', 30)	# 32970-32999
    teleportRelativeY(200000)
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(2200000)
    Unknown35()
    sprite('ji450_13', 80)	# 33000-33079
    Unknown1000(0)
    sprite('ji450_13', 166)	# 33080-33245
    physicsYImpulse(65000)
    setGravity(0)
    sprite('ji450_13', 5)	# 33246-33250
    Unknown1007(25000)
    teleportRelativeX(-5000)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000022000000')
    Unknown4004('534345465f41737452797568616955707065720000000000000000000000000064000000')
    Unknown36(1)
    Unknown1007(500000)
    Unknown35()
    sprite('ji450_14', 5)	# 33251-33255
    sprite('ji450_15', 5)	# 33256-33260
    sprite('ji450_16', 5)	# 33261-33265
    GFX_0('vr_ji450_body', 100)
    sprite('ji450_17', 5)	# 33266-33270
    sprite('ji450_18', 5)	# 33271-33275
    sprite('ji450_19', 5)	# 33276-33280
    sprite('ji450_20', 5)	# 33281-33285
    sprite('ji450_21', 5)	# 33286-33290
    GFX_0('Ichigeki_Syuri_Zanzoh', 100)
    GFX_0('Ichigeki_Syuri_Zanzoh2', 100)
    sprite('ji450_22', 5)	# 33291-33295
    sprite('ji450_23', 5)	# 33296-33300
    sprite('ji450_24', 5)	# 33301-33305
    sprite('ji450_25', 5)	# 33306-33310	 **attackbox here**
    sprite('ji450_26', 5)	# 33311-33315
    sprite('ji450_24', 5)	# 33316-33320
    Unknown3004(-24)
    sprite('ji450_25', 5)	# 33321-33325	 **attackbox here**
    sprite('ji450_26', 5)	# 33326-33330
    GFX_0('IchigekiBrack', 0)
    GFX_0('IchigekiSlash00', 0)
    Unknown26('SCEF_AstRyuhaiUpper')
    sprite('ji450_24', 4)	# 33331-33334
    GFX_0('IchigekiSlash01', 0)
    SFX_3('damage_ichigeki_slash')
    physicsYImpulse(0)
    setGravity(0)
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000026000000')
    sprite('ji450_24', 4)	# 33335-33338
    SFX_3('damage_ichigeki_slash')
    sprite('ji450_24', 8)	# 33339-33346
    SFX_3('damage_ichigeki_slash')
    sprite('ji450_25', 60)	# 33347-33406	 **attackbox here**
    RefreshMultihit()
    Unknown11023(1)
    AttackLevel_(5)
    Damage(8355)
    Unknown11064(3)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    AirPushbackX(0)
    Unknown11023(1)
    YImpluseBeforeWallbounce(1300)
    RefreshMultihit()
    Unknown21007(3, 33)
    sprite('null', 32767)	# 33407-66173
    Unknown21012('4963686967656b6943616d65726100000000000000000000000000000000000023000000')
    enterState('PersonaDeleteAndIdling')

@State
def PersonaWinroop():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown3032()
        Unknown23015(2)
    sprite('ji611_00', 4)	# 1-4
    sprite('ji611_01', 4)	# 5-8
    sprite('ji611_02', 4)	# 9-12
    sprite('ji611_00', 4)	# 13-16
    sprite('ji611_01', 4)	# 17-20
    sprite('ji611_02', 4)	# 21-24
    sprite('ji611_00', 4)	# 25-28
    sprite('ji611_01', 4)	# 29-32
    sprite('ji611_02', 4)	# 33-36
    sprite('ji611_00', 4)	# 37-40
    sprite('ji611_01', 4)	# 41-44
    sprite('ji611_02', 4)	# 45-48
    sprite('ji611_00', 4)	# 49-52
    sprite('ji611_01', 4)	# 53-56
    sprite('ji611_02', 4)	# 57-60
    sprite('ji611_00', 4)	# 61-64
    sprite('ji611_01', 4)	# 65-68
    sprite('ji611_02', 4)	# 69-72
    label(0)
    sprite('ji611_00', 4)	# 73-76
    sprite('ji611_01', 4)	# 77-80
    sprite('ji611_02', 4)	# 81-84
    loopRest()
    gotoLabel(0)
    enterState('PersonaDeleteAndIdling')

@State
def Zanzoh5C_():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown13044(1)
        Unknown4061(1)
        Unknown3001(250)
    sprite('vr_ji204_00', 6)	# 1-6
    Unknown4007(2)
    Unknown3005(-42)

@State
def Zanzoh2C():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(3)
        Unknown3001(250)
    sprite('vr_ji232_00', 2)	# 1-2
    Unknown3005(-15)
    sprite('vr_ji232_01', 2)	# 3-4
    sprite('vr_ji232_02', 2)	# 5-6
    sprite('vr_ji232_03', 16)	# 7-22
    Unknown3005(-45)

@State
def Air5Ctornado00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3235345f77696e6430302e44494700000000000000000000000000796f65665f3235345f77696e6430305f303030302e6d6d6f7400000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)

        def upon_43():
            if (SLOT_48 == 3002):
                Unknown3004(-52)
            if (SLOT_48 == 3003):
                Unknown4007(0)
                sendToLabel(0)
    sprite('null', 10)	# 1-10
    Unknown1099(50)
    GFX_0('Air5Ctornado01', 100)
    sprite('null', 10)	# 11-20
    Unknown1099(0)
    label(0)
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def Air5Ctornado01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3235345f77696e6430310000000000000000000000000000000000796f65665f3235345f77696e6430315f303030302e6d6d6f7400000000000000')
        Unknown4015()
        Unknown4010(3)
        Unknown4007(2)
        Unknown3001(150)

        def upon_43():
            if (SLOT_48 == 3003):
                Unknown4007(0)
                Unknown13(25)
    sprite('null', 10)	# 1-10
    sprite('null', 20)	# 11-30
    GFX_0('Air5CtornadoBrake', 100)
    Unknown3004(-17)

@State
def Air5CtornadoBrake():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3235345f77696e6430322e44494700000000000000000000000000796f65665f3235345f77696e6430325f303030302e6d6d6f7400000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3001(255)
    sprite('null', 20)	# 1-20
    Unknown1099(10)
    Unknown3004(-26)

@State
def __5Dtornado00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4015()
        Unknown4010(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown3001(255)
    sprite('null', 10)	# 1-10
    sprite('null', 5)	# 11-15
    Unknown3004(-26)
    sprite('null', 5)	# 16-20
    GFX_0('5DBrake', 100)
    sprite('null', 5)	# 21-25
    Unknown3001(0)

@State
def __5Dtornado01():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('jief_speedsmoke_02')
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
    sprite('null', 10)	# 1-10
    Unknown1059(10)
    sprite('null', 10)	# 11-20
    Unknown3004(-26)

@State
def __5DBrake():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3230355f77696e6430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4009(2)
        Unknown3001(150)
    sprite('null', 6)	# 1-6
    Unknown1099(100)
    physicsXImpulse(600)

@State
def yoef_throw():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown4053(-10000, 10000)
    Unknown4045('796f65665f7468726f776869740000000000000000000000000000000000000064000000')

@State
def yoef_Airthrow():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown4053(90000, 90000)
    Unknown4045('796f65665f7468726f776869740000000000000000000000000000000000000064000000')

@State
def yoef_Sukukaja5A():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown4053(-5000, 5000)
    Unknown4049(800)
    Unknown4045('796f65665f7468726f776869740000000000000000000000000000000000000064000000')

@State
def yoef_reaction():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(0)
    sprite('vr_yo001_00', 2)	# 1-2
    physicsYImpulse(4000)
    Unknown1021(-1000)
    sprite('vr_yo001_01', 2)	# 3-4
    sprite('vr_yo001_00', 2)	# 5-6
    physicsYImpulse(0)
    Unknown1021(0)
    sprite('vr_yo001_01', 2)	# 7-8
    physicsYImpulse(-1000)
    sprite('vr_yo001_00', 2)	# 9-10

@State
def Entry_wind():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3630335f74756d756a696b617a6530302e44494700000000000000796f65665f3630335f74756d756a696b617a6530305f303030302e6d6d6f7400')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(4)
        Unknown3001(0)
    sprite('null', 5)	# 1-5
    GFX_1('yoef_toujouwindunder_03', 100)
    Unknown3004(26)
    SFX_3('highjump_m')
    sprite('null', 10)	# 6-15
    GFX_0('Entry_wind00', 100)
    sprite('null', 10)	# 16-25
    GFX_1('yoef_toujouwind_02', 100)
    sprite('null', 10)	# 26-35
    Unknown3004(-26)
    Unknown1099(100)

@State
def Entry_wind00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3630335f74756d756a696b617a6530302e44494700000000000000796f65665f3630335f74756d756a696b617a6530305f303030302e6d6d6f7400')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(4)
        Unknown3001(0)
        teleportRelativeY(80000)
        Unknown1096(1200)
    sprite('null', 5)	# 1-5
    Unknown3004(26)
    sprite('null', 15)	# 6-20
    GFX_0('Entry_wind01', 100)
    sprite('null', 10)	# 21-30
    Unknown3004(-26)
    Unknown1099(60)

@State
def Entry_wind01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3630335f74756d756a696b617a6530302e44494700000000000000796f65665f3630335f74756d756a696b617a6530305f303030302e6d6d6f7400')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(4)
        Unknown3001(0)
        teleportRelativeY(180000)
        Unknown1096(1400)
    sprite('null', 5)	# 1-5
    Unknown3004(26)
    sprite('null', 10)	# 6-15
    GFX_0('Entry_wind02', 100)
    sprite('null', 10)	# 16-25
    Unknown3004(-26)
    Unknown1099(60)

@State
def Entry_wind02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3630335f74756d756a696b617a6530302e44494700000000000000796f65665f3630335f74756d756a696b617a6530305f303030302e6d6d6f7400')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(4)
        Unknown3001(0)
        teleportRelativeY(260000)
        Unknown1096(1600)
    sprite('null', 5)	# 1-5
    Unknown3004(26)
    sprite('null', 5)	# 6-10
    sprite('null', 10)	# 11-20
    Unknown3004(-26)
    Unknown1099(60)

@State
def Entry_2rope_ex00():
    sprite('vr_yo601_14', 5)	# 1-5
    sprite('vr_yo601_15', 5)	# 6-10
    sprite('vr_yo601_16', 5)	# 11-15
    sprite('vr_yo601_17', 5)	# 16-20

@State
def Entry_2rope_ex01():
    sprite('vr_yo601_21', 5)	# 1-5
    physicsXImpulse(-10000)
    physicsYImpulse(10000)
    setGravity(1000)
    sprite('vr_yo601_22', 5)	# 6-10
    sprite('vr_yo601_22', 20)	# 11-30
    Unknown3032()
    Unknown3004(-20)

@State
def Entry_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(2)
    sprite('vr_yo601_00', 3)	# 1-3
    sprite('null', 4)	# 4-7
    sprite('vr_yo601_00', 3)	# 8-10
    sprite('null', 4)	# 11-14

@State
def Entry_clashsmoke():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3032()
        Unknown1000(-1910000)
        teleportRelativeY(112000)
        GFX_1('yoef_entry_crash_itemC', 100)
    sprite('null', 1)	# 1-1
    GFX_1('yoef_entry2_crash', 100)

@State
def yoef_baketsu():

    def upon_IMMEDIATE():
        pass
    sprite('vr_yo602_00', 300)	# 1-300
    physicsXImpulse(-10000)
    physicsYImpulse(14000)
    setGravity(100)
    Unknown1074(-5000)

@State
def yoef_wheel():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3032()
        Unknown4010(3)
    sprite('vr_yo602_10', 600)	# 1-600
    Unknown2035(1)
    teleportRelativeY(64000)
    physicsXImpulse(15000)
    Unknown1074(6000)

@State
def win_kunai():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(0)
        Unknown1007(412000)
    sprite('vr_yo610_00', 3)	# 1-3
    physicsYImpulse(30000)
    sprite('vr_yo610_01', 3)	# 4-6
    sprite('vr_yo610_00', 3)	# 7-9
    sprite('vr_yo610_01', 3)	# 10-12
    sprite('vr_yo610_00', 3)	# 13-15
    sprite('vr_yo610_01', 3)	# 16-18
    sprite('vr_yo610_00', 3)	# 19-21
    sprite('vr_yo610_01', 3)	# 22-24
    sprite('vr_yo610_00', 3)	# 25-27
    sprite('vr_yo610_01', 3)	# 28-30
    sprite('vr_yo610_00', 3)	# 31-33
    sprite('vr_yo610_01', 3)	# 34-36

@State
def win_bomber():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3631315f77696e736d6f6b6530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown23015(2)
        Unknown3001(0)
    sprite('null', 3)	# 1-3
    sprite('null', 10)	# 4-13
    GFX_1('yoef_winmoya_05', 100)
    Unknown3001(255)
    sprite('null', 10)	# 14-23
    GFX_0('PersonaWinroop', 100)
    Unknown3004(-26)

@State
def yoef_moonslash():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown3033()
        Unknown4061(2)
        Unknown1007(-34000)
        teleportRelativeX(-44000)
    sprite('vr_yo405_00', 2)	# 1-2
    sprite('vr_yo405_01', 4)	# 3-6
    sprite('vr_yo405_01', 20)	# 7-26
    Unknown3001(128)
    Unknown3004(-20)

@State
def WarpSmoke():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(3)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23015(1)
    sprite('vr_ji406_00', 10)	# 1-10
    Unknown1099(30)
    Unknown3004(-26)
    GFX_1('jief_warpbom_07', 100)

@State
def Warp_Out():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    Unknown4045('6a6965665f77617270626f6d656e645f3035000000000000000000000000000000000000')

@State
def kunaishotA_Matome():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('kunaishot_ExPoint', 1)	# 1-1
    GFX_0('yo_kunaishot_a', 0)
    Unknown23029(1, 4101, 0)
    GFX_0('yo_kunaishot_a', 1)
    Unknown23029(1, 4102, 0)
    GFX_0('yo_kunaishot_a', 2)
    Unknown23029(1, 4103, 0)
    GFX_0('yo_kunaishot_a', 3)
    Unknown23029(1, 4104, 0)
    GFX_0('yo_kunaishot_a', 4)
    Unknown23029(1, 4105, 0)
    GFX_0('yo_kunaishot_a', 5)
    Unknown23029(1, 4106, 0)
    sprite('null', 59)	# 2-60
    Unknown4010(0)

@State
def kunaishotB_Matome():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('kunaishot_ExPoint', 1)	# 1-1
    GFX_0('yo_kunaishot_a', 0)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4101, 0)
    GFX_0('yo_kunaishot_a', 1)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4102, 0)
    GFX_0('yo_kunaishot_a', 2)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4103, 0)
    GFX_0('yo_kunaishot_a', 3)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4104, 0)
    GFX_0('yo_kunaishot_a', 4)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4105, 0)
    GFX_0('yo_kunaishot_a', 5)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4106, 0)
    sprite('null', 59)	# 2-60
    Unknown4010(0)

@State
def yo_kunaishot_a():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(2)
        Damage(600)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Hitstop(1)
        Unknown11001(12, 12, 12)
        AirUntechableTime(45)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(2400)
        Unknown23182(2)
        AirHitstunAfterWallbounce(25)
        Unknown11057(800)
        Unknown9016(1)
        Unknown23182(2)
        Unknown2035(1)
        Unknown4061(0)
        Unknown2055(360)
        physicsXImpulse(35000)
        physicsYImpulse(-40000)
        Unknown23089('0100000000000000010000000000000001000000000000000000000000000000')
        sendToLabelUpon(54, 1)

        def upon_LANDING():
            clearUponHandler(7)
            Unknown23090(25)
            sendToLabel(0)
        Unknown1072(55000)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3070(0)
        Unknown3072('be000000ff000000ff000000ff000000')
        Unknown3073('5a000000ff000000ff000000ff000000')
        Unknown11084(1)

        def upon_43():
            if (SLOT_48 == 4101):
                Unknown1007(0)
                teleportRelativeX(0)
                Unknown1073(800)
                Unknown1110(99123, 0)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4102):
                Unknown1073(-800)
                Unknown1110(99123, 0)
                Unknown1019(91)
                YAccel(91)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4103):
                Unknown1073(2400)
                Unknown1110(99123, 0)
                Unknown1019(82)
                YAccel(82)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4104):
                Unknown1073(-2400)
                Unknown1110(99123, 0)
                Unknown1019(73)
                YAccel(73)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4105):
                Unknown1073(3800)
                Unknown1110(99123, 0)
                Unknown1019(64)
                YAccel(64)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4106):
                Unknown1073(-3800)
                Unknown1110(99123, 0)
                Unknown1019(55)
                YAccel(55)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4107):
                Unknown1072(42000)
                AirPushbackY(-40000)
                AirPushbackX(36000)

        def upon_12():
            SLOT_52 = 1
        Unknown2053(1)

        def upon_7():
            clearUponHandler(7)
            clearUponHandler(2)
            Unknown2053(0)
            Unknown1084(1)
            sendToLabel(2)
            Unknown1072(46000)
            Unknown1000(1930000)
    sprite('vr_yo404_00', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    sprite('vr_yo404_00', 1)	# 2-2	 **attackbox here**
    sprite('vr_yo404_01ex01', 32767)	# 3-32769	 **attackbox here**
    Unknown1018()
    Unknown1023()
    label(0)
    sprite('vr_yo404_02', 3)	# 32770-32772
    SFX_3('walk_steal_light')
    Unknown1084(1)
    Unknown3029(0)
    Unknown2001()
    sprite('vr_yo404_03', 40)	# 32773-32812
    Unknown23183('0000000000000000000000000000000000000000000000000000000000000000050000000200000034000000')
    sprite('vr_yo404_03', 20)	# 32813-32832
    Unknown23183('00000000000000000000000000000000000000000000000000000000000000000a0000000200000034000000')
    Unknown3032()
    Unknown3004(-40)
    loopRest()
    ExitState()
    label(2)
    sprite('vr_yo404_02', 3)	# 32833-32835
    SFX_3('walk_steal_light')
    Unknown1084(1)
    Unknown3029(0)
    Unknown2001()
    sprite('vr_yo404_03', 40)	# 32836-32875
    Unknown23183('00000000000000000000000000000000000000000000000000000000000000000a0000000200000034000000')
    sprite('vr_yo404_03', 20)	# 32876-32895
    Unknown23183('00000000000000000000000000000000000000000000000000000000000000000a0000000200000034000000')
    Unknown3032()
    Unknown3004(-40)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 1)	# 32896-32896
    Unknown3029(0)
    GFX_0('yo_kunaishot_reflect', 100)

@State
def kunaishotTAG_Matome():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('kunaishot_ExPoint', 1)	# 1-1
    GFX_0('yo_kunaishot_tag', 0)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4101, 0)
    GFX_0('yo_kunaishot_tag', 1)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4102, 0)
    GFX_0('yo_kunaishot_tag', 2)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4103, 0)
    GFX_0('yo_kunaishot_tag', 3)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4104, 0)
    GFX_0('yo_kunaishot_tag', 4)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4105, 0)
    GFX_0('yo_kunaishot_tag', 5)
    Unknown23029(1, 4107, 0)
    Unknown23029(1, 4106, 0)
    sprite('null', 59)	# 2-60
    Unknown4010(0)

@State
def yo_kunaishot_tag():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(171)
        Hitstop(3)
        PushbackX(0)
        Unknown9154(25)
        AttackP2(80)
        Unknown11092(1)
        Unknown23182(2)
        Unknown9178(1)
        WallbounceReboundTime(1)
        Unknown9362(1)
        AirUntechableTime(45)
        AirHitstunAfterWallbounce(25)
        Unknown9364(25)
        Unknown9346(1)
        Unknown11057(500)
        Unknown23182(2)
        Unknown11001(10, 0, 0)
        AirHitstunAnimation(9)
        AirPushbackY(-40000)
        AirPushbackX(25000)
        Unknown30055('400d03006400000000000000')
        Unknown9016(1)
        Unknown11042(1)
        Unknown2035(1)
        Unknown4061(0)
        Unknown2055(360)
        physicsXImpulse(35000)
        physicsYImpulse(-40000)
        Unknown23089('0100000000000000010000000000000001000000000000000000000000000000')
        sendToLabelUpon(54, 1)

        def upon_LANDING():
            clearUponHandler(7)
            Unknown23090(25)
            sendToLabel(0)
        Unknown1072(55000)
        Unknown3029(1)
        Unknown3071(2)
        Unknown3070(0)
        Unknown3072('be000000ff000000ff000000ff000000')
        Unknown3073('5a000000ff000000ff000000ff000000')

        def upon_43():
            if (SLOT_48 == 4101):
                Unknown1007(0)
                teleportRelativeX(0)
                Unknown1073(800)
                Unknown1110(99123, 0)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4102):
                Unknown1073(-800)
                Unknown1110(99123, 0)
                Unknown1019(91)
                YAccel(91)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4103):
                Unknown1073(2400)
                Unknown1110(99123, 0)
                Unknown1019(82)
                YAccel(82)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4104):
                Unknown1073(-2400)
                Unknown1110(99123, 0)
                Unknown1019(73)
                YAccel(73)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4105):
                Unknown1073(3800)
                Unknown1110(99123, 0)
                Unknown1019(64)
                YAccel(64)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4106):
                Unknown1073(-3800)
                Unknown1110(99123, 0)
                Unknown1019(55)
                YAccel(55)
                Unknown1017()
                Unknown1022()
                Unknown1084(1)
            if (SLOT_48 == 4107):
                Unknown1072(42000)
                AirPushbackY(-40000)
                AirPushbackX(36000)

        def upon_12():
            SLOT_52 = 1
        Unknown2053(1)

        def upon_7():
            clearUponHandler(7)
            clearUponHandler(2)
            Unknown2053(0)
            Unknown1084(1)
            sendToLabel(2)
            Unknown1072(46000)
            Unknown1000(1930000)
    sprite('vr_yo404_00', 1)	# 1-1	 **attackbox here**
    RefreshMultihit()
    sprite('vr_yo404_00', 1)	# 2-2	 **attackbox here**
    sprite('vr_yo404_01ex01', 32767)	# 3-32769	 **attackbox here**
    Unknown1018()
    Unknown1023()
    label(0)
    sprite('vr_yo404_02', 3)	# 32770-32772
    SFX_3('walk_steal_light')
    Unknown1084(1)
    Unknown3029(0)
    Unknown2001()
    sprite('vr_yo404_03', 40)	# 32773-32812
    Unknown23183('0000000000000000000000000000000000000000000000000000000000000000050000000200000034000000')
    sprite('vr_yo404_03', 20)	# 32813-32832
    Unknown23183('00000000000000000000000000000000000000000000000000000000000000000a0000000200000034000000')
    if SLOT_52:
        pass
    Unknown3032()
    Unknown3004(-40)
    loopRest()
    ExitState()
    label(2)
    sprite('vr_yo404_02', 3)	# 32833-32835
    SFX_3('walk_steal_light')
    Unknown1084(1)
    Unknown3029(0)
    Unknown2001()
    sprite('vr_yo404_03', 40)	# 32836-32875
    Unknown23183('00000000000000000000000000000000000000000000000000000000000000000f0000000200000034000000')
    sprite('vr_yo404_03', 20)	# 32876-32895
    Unknown23183('00000000000000000000000000000000000000000000000000000000000000000a0000000200000034000000')
    if SLOT_52:
        pass
    Unknown3032()
    Unknown3004(-40)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 1)	# 32896-32896
    Unknown3029(0)
    GFX_0('yo_kunaishot_reflect', 100)

@State
def kunai_hit():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)	# 1-1
    GFX_1('yoef_kunai_hit_00', 100)

@State
def KunaiBakuhatsu():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(100)
        Hitstop(1)
        AirUntechableTime(20)
        AttackP2(100)
        AirHitstunAnimation(9)
        AirPushbackY(32000)
        AirPushbackX(1000)
        Unknown11066(1)
        Unknown9016(1)
        Unknown11050('0400000065665f6869745f736c6173686d00000000000000000000000000000000000000')
        Unknown53(1)
        Unknown48('19000000020000003a00000016000000020000001e000000')
        if (not SLOT_58):
            Unknown2001()
    sprite('dmy_atk', 4)	# 1-4
    Unknown1007(100000)
    sprite('dmy_atk', 1)	# 5-5
    Hitstop(6)
    sprite('dmy_atk', 1)	# 6-6

@State
def yo_kunaishot_reflect():

    def upon_IMMEDIATE():
        Unknown2035(1)
        Unknown4061(0)
        Unknown3032()
    sprite('null', 2)	# 1-2
    sprite('vr_yo404_00', 30)	# 3-32	 **attackbox here**
    Unknown3004(-4)
    Unknown1074(15000)
    physicsYImpulse(20000)
    physicsXImpulse(5000)
    setGravity(2000)

@State
def Tentarafu_BindMark():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_2('jief_402_bindmark02')
    sprite('null', 60)	# 1-60

@State
def V-Slasher():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown1007(-108000)
        teleportRelativeX(64000)
        Unknown1096(900)
    sprite('vr_yo407_00', 10)	# 1-10
    sprite('vr_yo407_01', 8)	# 11-18
    sprite('vr_yo407_01', 8)	# 19-26
    GFX_1('yoef_v_slasher', 0)
    GFX_1('yoef_v_slasher', 1)
    GFX_1('yoef_v_slasher', 2)
    GFX_1('yoef_v_slasher', 3)
    GFX_1('yoef_v_slasher', 4)
    GFX_1('yoef_v_slasher', 5)
    GFX_1('yoef_v_slasher', 6)
    GFX_1('yoef_v_slasher', 7)
    GFX_1('yoef_v_slasher', 8)
    GFX_1('yoef_v_slasher', 9)
    GFX_1('yoef_v_slasher', 10)
    sprite('vr_yo407_01', 16)	# 27-42
    Unknown3004(-16)

@State
def V-Slasher_Ex():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(2)
        Unknown1007(-108000)
        teleportRelativeX(64000)
        Unknown1096(900)
        sendToLabelUpon(33, 1)
    sprite('vr_yo407_00', 5)	# 1-5
    sprite('vr_yo407_01', 8)	# 6-13
    sprite('vr_yo407_01', 8)	# 14-21
    GFX_1('yoef_v_slasher', 0)
    GFX_1('yoef_v_slasher', 1)
    GFX_1('yoef_v_slasher', 2)
    GFX_1('yoef_v_slasher', 3)
    GFX_1('yoef_v_slasher', 4)
    GFX_1('yoef_v_slasher', 5)
    GFX_1('yoef_v_slasher', 6)
    GFX_1('yoef_v_slasher', 7)
    GFX_1('yoef_v_slasher', 8)
    GFX_1('yoef_v_slasher', 9)
    GFX_1('yoef_v_slasher', 10)
    sprite('vr_yo407_01', 16)	# 22-37
    Unknown3004(-16)
    ExitState()
    label(1)
    sprite('vr_yo407_00', 3)	# 38-40
    sprite('vr_yo407_01', 8)	# 41-48
    sprite('vr_yo407_01', 8)	# 49-56
    GFX_1('yoef_v_slasher', 0)
    GFX_1('yoef_v_slasher', 1)
    GFX_1('yoef_v_slasher', 2)
    GFX_1('yoef_v_slasher', 3)
    GFX_1('yoef_v_slasher', 4)
    GFX_1('yoef_v_slasher', 5)
    GFX_1('yoef_v_slasher', 6)
    GFX_1('yoef_v_slasher', 7)
    GFX_1('yoef_v_slasher', 8)
    GFX_1('yoef_v_slasher', 9)
    GFX_1('yoef_v_slasher', 10)
    sprite('vr_yo407_01', 16)	# 57-72
    Unknown3004(-16)

@State
def Tatsumaki():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(300)
        Unknown11091(15)
        AttackP2(98)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11050('0400000065665f6164646869745f77696e64000000000000000000000000000000000000')
        AirPushbackY(10500)
        AirPushbackX(7500)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown11057(800)
        Unknown4010(3)
        Unknown4009(3)

        def upon_3():
            Unknown1086(3)
            Unknown1007(-200000)
            if SLOT_51:
                if (SLOT_23 < 60000):
                    GFX_1('jief_garudine_jimen_03', 104)

        def upon_32():
            GFX_0('TatsumakiDelete', 100)
            Unknown13(25)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430322e4449470000000000000000000000796f65665f3433315f746f726e616430325f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown3001(0)
        GFX_0('Tatsumaki_start', 100)
        GFX_0('Tatsumaki_jizoku', 100)
    sprite('vr_dmy_tatsumaki', 24)	# 1-24
    Unknown23027()
    sprite('vr_dmy_tatsumaki', 5)	# 25-29
    SLOT_51 = 1
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 30-34
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 35-39
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 40-44
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 45-49
    Unknown3004(26)
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 50-54
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 55-59
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 60-64
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 65-69
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 70-74
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 75-79
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 80-84
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 85-89
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 90-94
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 95-99
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 100-104
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 105-109
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 110-114
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 115-119
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 120-124
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 125-129
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 130-134
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 135-139
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 140-144
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 145-149
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 150-154
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 155-159
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 160-164
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 165-169
    RefreshMultihit()
    AirPushbackY(24000)
    sprite('vr_dmy_tatsumaki', 5)	# 170-174
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 175-179
    RefreshMultihit()

@State
def TatsumakiOD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(360)
        Unknown11091(15)
        AttackP2(98)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11050('0400000065665f6164646869745f77696e64000000000000000000000000000000000000')
        AirPushbackY(6000)
        AirPushbackX(1000)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown11057(800)
        Unknown4010(3)
        Unknown4009(3)
        Unknown13024(1)

        def upon_3():
            Unknown1086(3)
            Unknown1007(-200000)
            if SLOT_51:
                if (SLOT_23 < 60000):
                    GFX_1('jief_garudine_jimen_03', 104)

        def upon_32():
            GFX_0('TatsumakiDelete', 100)
            Unknown13(25)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430322e4449470000000000000000000000796f65665f3433315f746f726e616430325f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown3001(0)
        GFX_0('Tatsumaki_start', 100)
        GFX_0('Tatsumaki_jizoku', 100)
    sprite('vr_dmy_tatsumaki', 24)	# 1-24
    Unknown23027()
    sprite('vr_dmy_tatsumaki', 5)	# 25-29
    SLOT_51 = 1
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 30-34
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 35-39
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 40-44
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 45-49
    Unknown3004(26)
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 50-54
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 55-59
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 60-64
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 65-69
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 70-74
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 75-79
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 80-84
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 85-89
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 90-94
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 95-99
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 100-104
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 105-109
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 110-114
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 115-119
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 120-124
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 125-129
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 130-134
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 135-139
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 140-144
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 145-149
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 150-154
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(18000)
    AirPushbackX(1000)
    sprite('vr_dmy_tatsumaki', 5)	# 155-159
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 160-164
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 165-169
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 170-174
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 175-179
    RefreshMultihit()

@State
def Tatsumaki_start():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('796f65665f3433315f73746172742e4449470000000000000000000000000000796f65665f3433315f73746172745f303030302e6d6d6f740000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown23013(1)
    sprite('null', 15)	# 1-15
    sprite('null', 5)	# 16-20
    GFX_1('jief_garudine_smoke08', 100)
    sprite('null', 10)	# 21-30
    sprite('null', 10)	# 31-40
    Unknown3004(-26)

@State
def Tatsumaki_jizoku():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430302e4449470000000000000000000000796f65665f3433315f746f726e616430305f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    sprite('null', 40)	# 11-50
    GFX_0('Tatsumaki_jizoku00', 100)
    sprite('null', 10)	# 51-60
    Unknown3004(-26)
    Unknown1099(40)

@State
def Tatsumaki_jizoku00():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430302e4449470000000000000000000000796f65665f3433315f746f726e616430305f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3001(0)
        teleportRelativeY(6000)
        Unknown1096(1300)
    sprite('null', 10)	# 1-10
    Unknown3004(51)
    sprite('null', 40)	# 11-50
    GFX_0('Tatsumaki_jizoku01', 100)
    sprite('null', 10)	# 51-60
    Unknown3004(-26)
    Unknown1099(40)

@State
def Tatsumaki_jizoku01():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430302e4449470000000000000000000000796f65665f3433315f746f726e616430305f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3001(0)
        teleportRelativeY(200000)
        Unknown1096(1600)
    sprite('null', 10)	# 1-10
    Unknown3004(51)
    sprite('null', 10)	# 11-20
    GFX_0('Tatsumaki_jizoku02', 100)
    sprite('null', 10)	# 21-30
    Unknown3004(-26)
    Unknown1099(40)

@State
def Tatsumaki_jizoku02():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430302e4449470000000000000000000000796f65665f3433315f746f726e616430305f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3001(0)
        teleportRelativeY(300000)
        Unknown1096(2000)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    sprite('null', 5)	# 11-15
    Unknown3004(-26)
    Unknown1099(40)

@State
def TatsumakiDelete():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e61645f656e642e444947000000000000000000796f65665f3433315f746f726e61645f656e645f303030302e6d6d6f74000000')
        Unknown4015()
        Unknown4007(2)
        Unknown4013(2)
        Unknown3001(255)
    sprite('vr_dmy_tatsumaki', 10)	# 1-10
    GFX_0('TatsumakiDelete2', 100)
    Unknown3004(-26)
    Unknown1059(-100)

@State
def TatsumakiDelete2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3433315f67617264696e655f66696e6973680000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(150)
    sprite('null', 19)	# 1-19
    GFX_1('yoef_finishlight00', 100)

@State
def TatsumakiYoinRoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 10)	# 1-10
    GFX_1('yoef_yoinwind_01', 100)
    gotoLabel(0)

@State
def TatsumakiYoin():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3433315f796f696e2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4007(2)
        Unknown3001(255)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown3004(-26)

@State
def jief_sukukaja():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(3)
        Unknown23015(1)
        Unknown1007(75000)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 5102):
                sendToLabel(1)
    sprite('vr_ji430_00', 4)	# 1-4
    GFX_1('jief_sukutame_04', 0)
    Unknown3004(26)
    sprite('vr_ji430_01', 4)	# 5-8
    sprite('vr_ji430_00', 4)	# 9-12
    sprite('vr_ji430_01', 4)	# 13-16
    label(0)
    sprite('vr_ji430_00', 4)	# 17-20
    sprite('vr_ji430_01', 4)	# 21-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ji430_02', 3)	# 25-27
    sprite('null', 42)	# 28-69
    Unknown3001(0)
    GFX_0('jief_sukukajaHikari', 100)

@State
def jief_sukukajaHikari():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(3)
        Unknown3001(190)
    sprite('vr_ji430_03', 4)	# 1-4
    GFX_0('Tjief_sukukajaAura', 0)
    sprite('vr_ji430_04', 4)	# 5-8
    sprite('vr_ji430_03', 4)	# 9-12
    sprite('vr_ji430_04', 4)	# 13-16
    sprite('vr_ji430_03', 4)	# 17-20
    sprite('vr_ji430_04', 4)	# 21-24
    sprite('vr_ji430_03', 4)	# 25-28
    sprite('vr_ji430_04', 4)	# 29-32
    sprite('vr_ji430_04', 5)	# 33-37
    Unknown1099(200)
    Unknown3004(-51)

@State
def jief_sukukajaHikariD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(3)
        Unknown3001(190)
    sprite('vr_ji430_03', 4)	# 1-4
    GFX_0('Tjief_sukukajaAura', 0)
    sprite('vr_ji430_04', 4)	# 5-8
    sprite('vr_ji430_03', 4)	# 9-12
    sprite('vr_ji430_04', 4)	# 13-16
    sprite('vr_ji430_03', 4)	# 17-20
    sprite('vr_ji430_04', 4)	# 21-24
    sprite('vr_ji430_03', 4)	# 25-28
    sprite('vr_ji430_04', 4)	# 29-32
    sprite('vr_ji430_03', 4)	# 33-36
    sprite('vr_ji430_04', 4)	# 37-40
    sprite('vr_ji430_03', 4)	# 41-44
    sprite('vr_ji430_04', 4)	# 45-48
    sprite('vr_ji430_04', 5)	# 49-53
    Unknown1099(200)
    Unknown3004(-51)

@State
def Tjief_sukukajaAura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3433305f6368617267652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(4)
    sprite('null', 60)	# 1-60

@State
def yoef_sukukajya():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3433305f6368617267652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4009(2)
        Unknown3001(0)
        sendToLabelUpon(32, 0)
    sprite('null', 30)	# 1-30
    Unknown3004(25)
    GFX_1('yoef_sukukajya_03', 100)
    label(0)
    sprite('null', 10)	# 31-40
    Unknown3004(-26)

@State
def ultimatekunai1():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(200)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AttackP2(100)
        Unknown11089(-1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11068(1)
        Unknown9016(1)
        Hitstop(30)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11023(1)
        Unknown11091(20)
        AirUntechableTime(40)
        Unknown2003(1)
        Unknown2054(1)
        Unknown53(0)

        def upon_43():
            if (SLOT_48 == 5201):
                sendToLabel(1)
            if (SLOT_48 == 5202):
                sendToLabel(2)
            if (SLOT_48 == 5203):
                sendToLabel(3)
            if (SLOT_48 == 5204):
                Unknown1015(20000)
                Unknown1021(4000)
                SFX_3('slash_knife_fast')
            if (SLOT_48 == 5205):
                Unknown1015(-12000)
                Unknown1021(-4000)
            if (SLOT_48 == 5206):
                Unknown1015(-20000)
                Unknown1021(16000)
            if (SLOT_48 == 5207):
                Unknown1015(12500)
                Unknown1021(-8000)
            if (SLOT_48 == 5208):
                Unknown1015(8000)
                Unknown1021(22000)
        Unknown1077(0, 360000)
        Unknown1078(-10000, 10000)
        physicsXImpulse(-5500)
        physicsYImpulse(2500)
    sprite('vr_yo404_00', 4)	# 1-4	 **attackbox here**
    sprite('vr_yo404_00', 4)	# 5-8	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 9-12	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 13-16	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 17-20	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 21-24	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 32767)	# 25-32791	 **attackbox here**
    label(1)
    sprite('vr_yo404_00', 1)	# 32792-32792	 **attackbox here**
    Unknown1019(0)
    YAccel(0)
    Unknown1074(50000)
    label(11)
    sprite('vr_yo404_00', 5)	# 32793-32797	 **attackbox here**
    SFX_3('slash_knife_middle')
    gotoLabel(11)
    label(2)
    sprite('vr_yo404_00', 15)	# 32798-32812	 **attackbox here**
    sprite('vr_yo404_00', 32767)	# 32813-65579	 **attackbox here**
    SFX_3('slash_knife_slow')
    SLOT_12 = SLOT_19
    SLOT_13 = SLOT_20
    Unknown1021(325000)
    Unknown1108(10000)
    Unknown1019(0)
    YAccel(0)
    Unknown1074(0)
    label(3)
    sprite('vr_yo404_00', 1)	# 65580-65580	 **attackbox here**

    def upon_3():
        if (SLOT_29 <= 350000):
            clearUponHandler(3)
            Unknown2003(0)
    sprite('vr_yo404_00', 35)	# 65581-65615	 **attackbox here**
    Unknown1110(140000, 100)
    RefreshMultihit()
    sprite('vr_yo404_00', 2)	# 65616-65617	 **attackbox here**
    Unknown53(1)

@State
def ultimatekunai2():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(4)
        Damage(200)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        Unknown11089(-1)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11068(1)
        Unknown9016(1)
        Hitstop(30)
        Unknown11064(1)
        Unknown11023(1)
        Unknown11091(20)
        AirUntechableTime(40)
        Unknown2003(1)
        Unknown30048(1)
        Unknown2054(1)
        Unknown53(0)

        def upon_43():
            if (SLOT_48 == 5201):
                sendToLabel(1)
            if (SLOT_48 == 5202):
                sendToLabel(2)
            if (SLOT_48 == 5203):
                sendToLabel(3)
            if (SLOT_48 == 5204):
                Unknown1015(20000)
                Unknown1021(4000)
                SFX_3('slash_knife_fast')
            if (SLOT_48 == 5205):
                Unknown1015(-12000)
                Unknown1021(-4000)
            if (SLOT_48 == 5206):
                Unknown1015(-20000)
                Unknown1021(16000)
            if (SLOT_48 == 5207):
                Unknown1015(12500)
                Unknown1021(-8000)
            if (SLOT_48 == 5208):
                Unknown1015(8000)
                Unknown1021(22000)
        Unknown1077(0, 360000)
        Unknown1078(-10000, 10000)
        physicsXImpulse(-5500)
        physicsYImpulse(2500)
    sprite('vr_yo404_00', 4)	# 1-4	 **attackbox here**
    sprite('vr_yo404_00', 4)	# 5-8	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 9-12	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 13-16	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 17-20	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 21-24	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 32767)	# 25-32791	 **attackbox here**
    label(1)
    sprite('vr_yo404_00', 1)	# 32792-32792	 **attackbox here**
    Unknown1019(0)
    YAccel(0)
    Unknown1074(50000)
    label(11)
    sprite('vr_yo404_00', 5)	# 32793-32797	 **attackbox here**
    SFX_3('slash_knife_middle')
    gotoLabel(11)
    label(2)
    sprite('vr_yo404_00', 15)	# 32798-32812	 **attackbox here**
    sprite('vr_yo404_00', 32767)	# 32813-65579	 **attackbox here**
    SFX_3('slash_knife_slow')
    SLOT_12 = SLOT_19
    SLOT_13 = SLOT_20
    Unknown1021(325000)
    Unknown1108(10000)
    Unknown1019(0)
    YAccel(0)
    Unknown1074(0)
    label(3)
    sprite('vr_yo404_00', 1)	# 65580-65580	 **attackbox here**

    def upon_3():
        if (SLOT_29 <= 350000):
            clearUponHandler(3)
            Unknown2003(0)
    sprite('vr_yo404_00', 35)	# 65581-65615	 **attackbox here**
    Unknown1110(140000, 100)
    RefreshMultihit()
    sprite('vr_yo404_00', 2)	# 65616-65617	 **attackbox here**
    Unknown53(1)

@State
def ultimatekunai3():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(3)
        Damage(250)
        if Unknown23146('16000000556c74696d6174654b756e61694f444578650000000000000000000000000000'):
            Damage(200)
        AirPushbackX(3000)
        AirPushbackY(30000)
        Unknown11089(-1)
        AttackP2(100)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11068(1)
        Unknown9016(1)
        Hitstop(10)
        Unknown9310(10)
        Unknown11023(1)
        AirUntechableTime(400)
        Unknown2003(1)
        Unknown2054(1)
        Unknown53(0)
        Unknown30048(1)

        def upon_43():
            if (SLOT_48 == 5201):
                sendToLabel(1)
            if (SLOT_48 == 5202):
                sendToLabel(2)
            if (SLOT_48 == 5203):
                sendToLabel(3)
            if (SLOT_48 == 5204):
                Unknown1015(20000)
                Unknown1021(4000)
                SFX_3('slash_knife_fast')
            if (SLOT_48 == 5205):
                Unknown1015(-12000)
                Unknown1021(-4000)
            if (SLOT_48 == 5206):
                Unknown1015(-20000)
                Unknown1021(16000)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            if (SLOT_48 == 5207):
                Unknown1015(12500)
                Unknown1021(-8000)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            if (SLOT_48 == 5208):
                Unknown1015(8000)
                Unknown1021(22000)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            if (SLOT_48 == 5209):
                Unknown1015(18000)
                Unknown1021(-2000)
            if (SLOT_48 == 5210):
                Unknown1015(16000)
                Unknown1021(10000)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            if (SLOT_48 == 5211):
                Unknown1015(14000)
                Unknown1021(-3000)
            if (SLOT_48 == 5212):
                Unknown1015(13000)
                Unknown1021(8000)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            if (SLOT_48 == 5213):
                Unknown1015(-18000)
                Unknown1021(12000)
            if (SLOT_48 == 5214):
                Unknown1015(-16000)
                Unknown1021(-5000)
                Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1077(0, 360000)
        Unknown1078(-10000, 10000)
        physicsXImpulse(-5500)
        physicsYImpulse(2500)
    sprite('vr_yo404_00', 4)	# 1-4	 **attackbox here**
    sprite('vr_yo404_00', 4)	# 5-8	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 9-12	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 13-16	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 17-20	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 4)	# 21-24	 **attackbox here**
    Unknown1019(80)
    YAccel(80)
    sprite('vr_yo404_00', 32767)	# 25-32791	 **attackbox here**
    label(1)
    sprite('vr_yo404_00', 1)	# 32792-32792	 **attackbox here**
    Unknown1019(0)
    YAccel(0)
    Unknown1074(50000)
    label(11)
    sprite('vr_yo404_00', 5)	# 32793-32797	 **attackbox here**
    if random_(2, 0, 20):
        SFX_3('slash_knife_middle')
    gotoLabel(11)
    label(2)
    sprite('vr_yo404_00', 15)	# 32798-32812	 **attackbox here**
    sprite('vr_yo404_00', 32767)	# 32813-65579	 **attackbox here**
    SLOT_12 = SLOT_19
    SLOT_13 = SLOT_20
    Unknown1021(525000)
    Unknown1108(10000)
    Unknown1019(0)
    YAccel(0)
    Unknown1074(0)
    label(3)
    sprite('vr_yo404_00', 1)	# 65580-65580	 **attackbox here**

    def upon_3():
        if (SLOT_29 <= 350000):
            clearUponHandler(3)
            Unknown2003(0)
    sprite('vr_yo404_00', 35)	# 65581-65615	 **attackbox here**
    Unknown1110(140000, 100)
    RefreshMultihit()
    sprite('vr_yo404_00', 2)	# 65616-65617	 **attackbox here**
    Unknown53(1)

@State
def KunaiZanzoh():
    sprite('null', 10)	# 1-10
    Unknown2019(100)
    Unknown23053('1900000003000000')
    Unknown3032()
    Unknown3004(-4)
    sprite('keep', 120)	# 11-130
    Unknown3004(-15)

@State
def IchigekiCamera():

    def upon_IMMEDIATE():
        Unknown2017(0)
        Unknown2053(0)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
        sendToLabelUpon(35, 3)
        sendToLabelUpon(36, 4)
        sendToLabelUpon(37, 5)
        sendToLabelUpon(38, 6)

        def upon_3():
            SLOT_105 = (SLOT_105 + SLOT_51)
        Unknown3029(1)
        Unknown3032()
        Unknown3001(80)
    sprite('null', 32767)	# 1-32767
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown1086(2)
    label(0)
    sprite('keep', 32767)	# 32768-65534
    Unknown1086(2)
    label(1)
    sprite('keep', 12)	# 65535-65546
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('keep', 15)	# 65547-65561
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown20001(1)
    Unknown1086(22)
    Unknown1007(350000)
    Unknown4007(22)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown4004('534345465f41737452797568616955707065720000000000000000000000000064000000')
    sprite('keep', 60)	# 65562-65621
    sprite('keep', 20)	# 65622-65641
    Unknown26('SCEF_AstRyuhaiUpper')
    sprite('keep', 40)	# 65642-65681
    sprite('keep', 32767)	# 65682-98448
    label(2)
    sprite('keep', 32767)	# 98449-131215
    Unknown4007(0)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20002(1)
    Unknown20003(1)
    Unknown20009(950)
    physicsYImpulse(65000)
    setGravity(0)
    label(3)
    sprite('keep', 120)	# 131216-131335
    Unknown4007(0)
    SLOT_51 = 0
    Unknown20009(1000)
    Unknown1084(1)
    Unknown1086(3)
    teleportRelativeY(0)
    sprite('keep', 32767)	# 131336-164102
    label(4)
    sprite('keep', 32767)	# 164103-196869
    Unknown1007(-100000)
    label(5)
    sprite('keep', 25)	# 196870-196894
    physicsYImpulse(6000)
    sprite('keep', 10)	# 196895-196904
    physicsYImpulse(0)
    sprite('keep', 10)	# 196905-196914
    sprite('keep', 32767)	# 196915-229681
    label(6)
    sprite('keep', 32767)	# 229682-262448
    Unknown1084(1)
    setGravity(0)

@State
def IchigekiTatsumakiAtk():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4010(2)
        Unknown2012()
        AttackLevel_(5)
        Hitstop(12)
        Damage(500)
        Unknown11064(1)
        AirPushbackX(0)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(0)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(10000)
        Unknown9310(60)
        PushbackX(0)
        Unknown9016(1)
        Unknown11031(0)
        Unknown4007(2)

        def upon_12():
            Unknown21007(3, 32)
            Unknown21007(2, 32)

        def upon_44():
            Unknown2003(1)
    sprite('dmy_atk01', 15)	# 1-15
    Unknown2003(1)
    GFX_0('Ichigekistart00', 0)
    sprite('dmy_atk01', 29)	# 16-44
    GFX_1('jief_groundtouch_04', 1)
    sprite('dmy_atk01', 7)	# 45-51
    GFX_0('Ichigekistart03', 0)
    sprite('dmy_atk01', 7)	# 52-58
    GFX_0('IchigekiTornado01', 100)
    sprite('dmy_atk01', 15)	# 59-73
    GFX_0('IchigekiTornado00', 0)
    Unknown2003(0)
    RefreshMultihit()
    Unknown4007(0)
    sprite('dmy_atk01', 10)	# 74-83
    sprite('dmy_atk01', 220)	# 84-303
    Unknown23027()

@State
def Ichigekistart00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f737461727430302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown2054(1)
        Unknown3001(0)
        Unknown1007(25000)
        teleportRelativeX(60000)
        Unknown1096(800)

        def upon_44():
            clearUponHandler(44)
            sendToLabel(0)
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    SFX_3('yo008')
    sprite('null', 10)	# 11-20
    Unknown3004(14)
    sprite('null', 20)	# 21-40
    physicsYImpulse(600)
    Unknown1099(2)
    SFX_3('yo008')
    SLOT_51 = 11
    label(1)
    sprite('null', 10)	# 41-50
    SFX_3('yo008')
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(0, 2, 51)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('null', 60)	# 51-110
    Unknown3004(-26)
    sprite('null', 20)	# 111-130
    Unknown1059(0)

@State
def Ichigekistart01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f737461727430312e444947000000000000000000000000796f65665f3435305f737461727430315f303030302e6d6d6f74000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    GFX_0('Ichigekistart02', 100)
    GFX_1('jief_ichigekistart_09', 100)
    sprite('null', 10)	# 11-20
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def Ichigekistart02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f737461727430322e444947000000000000000000000000796f65665f3435305f737461727430325f303030302e6d6d6f74000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown2054(1)

        def upon_44():
            clearUponHandler(44)
            sendToLabel(0)
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    sprite('null', 10)	# 11-20
    Unknown1099(-10)
    label(0)
    sprite('null', 5)	# 21-25
    Unknown3004(-51)

@State
def Ichigekistart03():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f737461727430332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown2054(1)
        Unknown3001(255)
    sprite('null', 20)	# 1-20
    sprite('null', 10)	# 21-30
    Unknown3004(-26)

@State
def IchigekiTornado00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f746f726e61646f30302e44494700000000000000000000796f65665f3435305f746f726e61646f30305f303030302e6d6d6f7400000000')
        Unknown4015()
        Unknown3001(0)
        Unknown4007(2)
        Unknown1056(0)
        Unknown2054(1)

        def upon_44():
            clearUponHandler(44)
            sendToLabel(0)
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    GFX_1('jief_ichigekistart_07', 100)
    GFX_2('jief_ichigekijizoku_00')
    sprite('null', 10)	# 11-20
    Unknown3004(18)
    Unknown1059(100)
    SFX_3('yo009')
    sprite('null', 10)	# 21-30
    Unknown1059(0)
    SFX_3('yo009')
    sprite('null', 58)	# 31-88
    SFX_3('yo009')
    label(0)
    sprite('null', 10)	# 89-98
    Unknown3004(-26)

@State
def IchigekiTornado01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f746f726e61646f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4007(2)
        Unknown2054(1)

        def upon_44():
            clearUponHandler(44)
            sendToLabel(0)
        sendToLabelUpon(32, 0)
    sprite('null', 2)	# 1-2
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 2)	# 3-4
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 2)	# 5-6
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 2)	# 7-8
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 2)	# 9-10
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 2)	# 11-12
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 13-15
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 16-18
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 19-21
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 22-24
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 25-27
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 28-30
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 31-33
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 34-36
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 37-39
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 40-42
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 43-45
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 46-48
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 49-51
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 52-54
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 55-57
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 58-60
    GFX_0('IchigekiTornado01a', 100)
    sprite('null', 3)	# 61-63
    GFX_0('IchigekiTornado01a', 100)
    label(0)
    sprite('null', 1)	# 64-64

@State
def IchigekiTornado01a():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('796f65665f3435305f746f726e61646f30312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown1010(-50000, 50000)
        physicsYImpulse(100000)
        Unknown3001(150)
        Unknown1096(1500)
    sprite('null', 5)	# 1-5
    Unknown1099(-30)
    sprite('null', 10)	# 6-15
    physicsXImpulse(-6000)
    Unknown1099(40)
    Unknown3004(-7)
    physicsYImpulse(50000)
    sprite('null', 10)	# 16-25
    physicsXImpulse(6000)
    Unknown1099(50)

@State
def IchigekiCutIn():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2007()
        Unknown3001(255)
        Unknown23015(1)
        teleportRelativeY(9700000)
        Unknown1000(-920000)
        Unknown1007(480000)
        teleportRelativeX(400000)
    sprite('ichigeki0', 5)	# 1-5	 **attackbox here**
    physicsYImpulse(60000)
    physicsXImpulse(250000)
    sprite('ichigeki0', 25)	# 6-30	 **attackbox here**
    physicsXImpulse(1000)
    sprite('ichigeki0', 5)	# 31-35	 **attackbox here**
    Unknown23118(-1)
    physicsYImpulse(50000)
    physicsXImpulse(40000)
    Unknown1067(100)
    Unknown3004(-51)

@State
def vr_ji450_body():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3032()
    sprite('vr_ji450_16z', 5)	# 1-5
    sprite('vr_ji450_17z', 5)	# 6-10
    sprite('vr_ji450_18z', 5)	# 11-15
    sprite('vr_ji450_19z', 5)	# 16-20
    sprite('vr_ji450_20z', 5)	# 21-25

@State
def IchigekiSlash00():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown2008()
        Unknown3001(255)
        Unknown4054(4)
        Unknown23015(4)
        Unknown1072(-20000)
        Unknown1096(1900)
        Unknown4007(2)
    sprite('vr_ji450_zan00', 4)	# 1-4
    Unknown23067('jief_blood_03')
    sprite('vr_ji450_zan01', 4)	# 5-8
    sprite('vr_ji450_zan02', 4)	# 9-12
    ScreenShake(0, 15000)
    sprite('null', 30)	# 13-42

@State
def IchigekiSlash01():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(3)
        Unknown2007()
        Unknown3001(255)
        Unknown4054(4)
        Unknown23015(4)
        Unknown1072(-20000)
        Unknown1096(1900)
        Unknown4007(2)
    sprite('vr_ji450_zan00', 4)	# 1-4
    Unknown23067('jief_blood_03')
    sprite('vr_ji450_zan01', 4)	# 5-8
    sprite('vr_ji450_zan02', 4)	# 9-12
    ScreenShake(0, 15000)
    sprite('null', 30)	# 13-42

@State
def Ichigeki_Syuri_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown3033()
        Unknown1096(1050)
        Unknown3001(255)
        Unknown23015(4)
        Unknown2008()
    sprite('vr_ji450_syu00', 2)	# 1-2
    GFX_0('IchigekiSyuriNomalR1', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu00', 2)	# 3-4
    GFX_0('IchigekiSyuriNomalR2', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu01', 2)	# 5-6
    GFX_0('IchigekiSyuriNomalR3', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu01', 2)	# 7-8
    GFX_0('IchigekiSyuriNomalR4', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu02', 2)	# 9-10
    GFX_0('IchigekiSyuriNomalR5', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu02', 2)	# 11-12
    GFX_0('IchigekiSyuriNomalR6', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu03', 2)	# 13-14
    GFX_0('IchigekiSyuriNomalR7', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu03', 2)	# 15-16
    GFX_0('IchigekiSyuriNomalR8', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu04', 30)	# 17-46
    Unknown3004(-10)

@State
def IchigekiSyuriNomalR1():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(140)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR2():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(280)
        Unknown1072(15000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR3():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(420)
        Unknown1072(-20000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR4():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(420)
        Unknown1072(-25000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR5():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(560)
        Unknown1072(-30000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR6():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(700)
        Unknown1072(-35000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR7():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(1000)
        Unknown1072(-40000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalR8():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(1200)
        Unknown1072(-45000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def Ichigeki_Syuri_Zanzoh2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown3033()
        Unknown1096(1050)
        Unknown3001(255)
        Unknown23015(4)
        Unknown2007()
    sprite('vr_ji450_syu00', 2)	# 1-2
    GFX_0('IchigekiSyuriNomalL1', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu00', 2)	# 3-4
    GFX_0('IchigekiSyuriNomalL2', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu01', 2)	# 5-6
    GFX_0('IchigekiSyuriNomalL3', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu01', 2)	# 7-8
    GFX_0('IchigekiSyuriNomalL4', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu02', 2)	# 9-10
    GFX_0('IchigekiSyuriNomalL5', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu02', 2)	# 11-12
    GFX_0('IchigekiSyuriNomalL6', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu03', 2)	# 13-14
    GFX_0('IchigekiSyuriNomalL7', 0)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu03', 2)	# 15-16
    GFX_0('IchigekiSyuriNomalL8', 1)
    SFX_3('slash_knife_fast')
    sprite('vr_ji450_syu04', 30)	# 17-46
    Unknown3004(-10)

@State
def IchigekiSyuriNomalL1():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(140)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL2():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(280)
        Unknown1072(15000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL3():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(420)
        Unknown1072(-20000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL4():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(420)
        Unknown1072(-25000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL5():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(560)
        Unknown1072(-30000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL6():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(700)
        Unknown1072(-35000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL7():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(1000)
        Unknown1072(-40000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiSyuriNomalL8():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown3001(255)
        Unknown23015(4)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(1)
        Unknown1096(1200)
        Unknown1072(-45000)
    sprite('vr_ji450_syu05', 10)	# 1-10
    Unknown3004(-26)

@State
def IchigekiBrack():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(3)
        Unknown2007()
        Unknown3001(0)
        Unknown23015(1)
        Unknown1007(60000)
        Unknown4007(2)
    sprite('vr_ji450_black', 15)	# 1-15
    sprite('vr_ji450_black', 10)	# 16-25
    Unknown3004(26)
    sprite('vr_ji450_black', 10)	# 26-35
    Unknown3004(-51)

@State
def RanbuYousuke_L():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('yoef_rashspeed_li')
    sprite('yo123_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3071(2)
    Unknown3070(0)
    Unknown3072('be000000ff000000ff000000ff000000')
    Unknown3073('5a000000ff000000ff000000ff000000')
    physicsXImpulse(160000)
    sprite('yo123_01', 2)	# 3-4
    sprite('yo123_02', 2)	# 5-6
    sprite('yo123_01', 2)	# 7-8
    sprite('yo123_02', 2)	# 9-10
    sprite('yo123_01', 2)	# 11-12

@State
def RanbuYousuke_R():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown2005()
        GFX_2('yoef_rashspeed_li')
    sprite('yo123_01', 2)	# 1-2
    sprite('yo123_02', 2)	# 3-4
    Unknown3029(1)
    Unknown3071(2)
    Unknown3070(0)
    Unknown3072('be000000ff000000ff000000ff000000')
    Unknown3073('5a000000ff000000ff000000ff000000')
    physicsXImpulse(160000)
    sprite('yo123_01', 2)	# 5-6
    sprite('yo123_02', 2)	# 7-8
    sprite('yo123_01', 2)	# 9-10
    sprite('yo123_02', 2)	# 11-12
    sprite('yo123_01', 2)	# 13-14

@State
def RanbuYousuke_DownL():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown1072(45000)
        GFX_2('yoef_rashspeed_li')
    sprite('yo123_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3029(1)
    Unknown3071(2)
    Unknown3070(0)
    Unknown3072('be000000ff000000ff000000ff000000')
    Unknown3073('5a000000ff000000ff000000ff000000')
    physicsYImpulse(-160000)
    physicsXImpulse(160000)
    sprite('yo123_01', 2)	# 3-4
    sprite('yo123_02', 2)	# 5-6
    sprite('yo123_01', 2)	# 7-8
    sprite('yo123_02', 2)	# 9-10
    sprite('yo123_01', 2)	# 11-12

@State
def RanbuYousuke_UpR():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown1072(-45000)
        GFX_2('yoef_rashspeed_li')
    sprite('yo123_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3029(1)
    Unknown3071(2)
    Unknown3070(0)
    Unknown3072('be000000ff000000ff000000ff000000')
    Unknown3073('5a000000ff000000ff000000ff000000')
    physicsYImpulse(160000)
    physicsXImpulse(160000)
    sprite('yo123_01', 2)	# 3-4
    sprite('yo123_02', 2)	# 5-6
    sprite('yo123_01', 2)	# 7-8
    sprite('yo123_02', 2)	# 9-10
    sprite('yo123_01', 2)	# 11-12

@State
def PYO_PersonaWarpTAG():

    def upon_IMMEDIATE():
        Unknown23184('03000000640000000089feff0089feff00000000000000000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        Unknown23142(1)
        Unknown2009()
        callSubroutine('PYO_CheckWarp')
    sprite('ji406_00', 2)	# 1-2
    sprite('ji406_01', 3)	# 3-5
    sprite('ji406_02', 3)	# 6-8
    sprite('ji406_50', 3)	# 9-11
    GFX_0('WarpSmoke', 0)
    sprite('ji406_03', 2)	# 12-13
    sprite('ji406_04', 2)	# 14-15
    sprite('ji406_05', 2)	# 16-17
    sprite('ji406_03', 2)	# 18-19
    sprite('ji406_04', 2)	# 20-21
    sprite('ji406_05', 2)	# 22-23
    sprite('ji406_03', 2)	# 24-25
    sprite('ji406_04', 2)	# 26-27
    sprite('ji406_05', 2)	# 28-29
    sprite('ji406_03', 2)	# 30-31
    sprite('ji406_04', 2)	# 32-33
    sprite('ji406_05', 2)	# 34-35
    sprite('ji406_03', 2)	# 36-37
    sprite('ji406_04', 2)	# 38-39
    sprite('ji406_05', 2)	# 40-41
    sprite('ji406_03', 2)	# 42-43
    sprite('ji406_04', 2)	# 44-45
    sprite('ji406_05', 2)	# 46-47
    sprite('ji406_03', 2)	# 48-49
    sprite('ji406_04', 2)	# 50-51
    sprite('ji406_05', 2)	# 52-53
    sprite('keep', 32767)	# 54-32820
    enterState('PersonaDeleteAndIdling')

@State
def PYO_PersonaUltimateTatsumakiTAG():

    def upon_IMMEDIATE():
        Unknown23184('03000000640000006079feff10b6fdff0000000060ea00000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        callSubroutine('PYO_ForceWarp')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23078(1)
        Unknown23022(1)
        Unknown23023()
    sprite('ji431_00', 4)	# 1-4
    sprite('ji431_01', 4)	# 5-8
    sprite('ji431_02', 4)	# 9-12
    sprite('ji431_03', 4)	# 13-16
    sprite('ji431_04', 4)	# 17-20
    sprite('ji431_05', 4)	# 21-24
    sprite('ji431_06', 4)	# 25-28
    Unknown4007(0)
    GFX_0('TatsumakiTAG', 100)
    sprite('ji431_07', 4)	# 29-32
    sprite('ji431_08', 4)	# 33-36
    sprite('ji431_09', 12)	# 37-48
    sprite('ji431_10', 4)	# 49-52
    ScreenShake(20000, 0)
    sprite('ji431_11', 4)	# 53-56
    sprite('ji431_12', 4)	# 57-60
    sprite('ji431_13', 4)	# 61-64
    sprite('ji431_11', 4)	# 65-68
    sprite('ji431_12', 4)	# 69-72
    sprite('ji431_13', 4)	# 73-76
    sprite('ji431_11', 5)	# 77-81
    sprite('ji431_12', 5)	# 82-86
    sprite('ji431_13', 5)	# 87-91
    sprite('ji431_11', 6)	# 92-97
    sprite('ji431_12', 6)	# 98-103
    sprite('ji431_13', 6)	# 104-109
    sprite('keep', 32767)	# 110-32876
    enterState('PersonaDeleteAndIdling')

@State
def TatsumakiTAG():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11091(100)
        AirPushbackY(8000)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown11057(800)
        Unknown9310(1)
        Unknown11050('0400000065665f6164646869745f77696e64000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4009(3)

        def upon_3():
            Unknown1086(3)
            Unknown1007(-200000)
            if SLOT_51:
                if (SLOT_23 < 60000):
                    GFX_1('jief_garudine_jimen_03', 104)

        def upon_32():
            GFX_0('TatsumakiDelete', 100)
            Unknown13(25)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430322e4449470000000000000000000000796f65665f3433315f746f726e616430325f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown3001(0)
        GFX_0('Tatsumaki_start', 100)
        GFX_0('Tatsumaki_jizoku', 100)
    sprite('vr_dmy_tatsumaki', 24)	# 1-24
    Unknown23027()
    sprite('vr_dmy_tatsumaki', 5)	# 25-29
    SLOT_51 = 1
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 30-34
    sprite('vr_dmy_tatsumaki', 5)	# 35-39
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 40-44
    sprite('vr_dmy_tatsumaki', 5)	# 45-49
    Unknown3004(26)
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 50-54
    sprite('vr_dmy_tatsumaki', 5)	# 55-59
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 60-64
    sprite('vr_dmy_tatsumaki', 5)	# 65-69
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 70-74
    sprite('vr_dmy_tatsumaki', 5)	# 75-79
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 80-84
    sprite('vr_dmy_tatsumaki', 5)	# 85-89
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 90-94
    sprite('vr_dmy_tatsumaki', 5)	# 95-99
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 100-104
    sprite('vr_dmy_tatsumaki', 5)	# 105-109
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 110-114
    sprite('vr_dmy_tatsumaki', 5)	# 115-119
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 120-124
    sprite('vr_dmy_tatsumaki', 5)	# 125-129
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 130-134
    sprite('vr_dmy_tatsumaki', 5)	# 135-139
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 140-144
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 145-149
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 150-154
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 155-159
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 160-164
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 165-169
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 170-174
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 175-179
    RefreshMultihit()

@State
def PYO_PersonaUltimateTatsumakiODT():

    def upon_IMMEDIATE():
        Unknown23184('03000000640000006079feff10b6fdff0000000060ea00000000000000000000')
        callSubroutine('PYO_SPAttackInit')
        callSubroutine('PYO_ForceWarp')
        Unknown4009(3)
        Unknown23066(1)
        Unknown23078(1)
        Unknown23022(1)
        Unknown23023()
        Unknown23056('')
    sprite('ji431_00', 4)	# 1-4
    sprite('ji431_01', 4)	# 5-8
    sprite('ji431_02', 4)	# 9-12
    sprite('ji431_03', 4)	# 13-16
    sprite('ji431_04', 4)	# 17-20
    sprite('ji431_05', 4)	# 21-24
    sprite('ji431_06', 4)	# 25-28
    Unknown4007(0)
    GFX_0('TatsumakiODTAG', 100)
    sprite('ji431_07', 4)	# 29-32
    sprite('ji431_08', 4)	# 33-36
    sprite('ji431_09', 12)	# 37-48
    sprite('ji431_10', 4)	# 49-52
    ScreenShake(20000, 0)
    sprite('ji431_11', 4)	# 53-56
    sprite('ji431_12', 4)	# 57-60
    sprite('ji431_13', 4)	# 61-64
    sprite('ji431_11', 4)	# 65-68
    sprite('ji431_12', 4)	# 69-72
    sprite('ji431_13', 4)	# 73-76
    sprite('ji431_11', 5)	# 77-81
    sprite('ji431_12', 5)	# 82-86
    sprite('ji431_13', 5)	# 87-91
    sprite('ji431_11', 6)	# 92-97
    sprite('ji431_12', 6)	# 98-103
    sprite('ji431_13', 6)	# 104-109
    sprite('keep', 32767)	# 110-32876
    enterState('PersonaDeleteAndIdling')

@State
def TatsumakiODTAG():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11091(100)
        AirPushbackY(8000)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown11057(800)
        Unknown9310(1)
        Unknown11050('0400000065665f6164646869745f77696e64000000000000000000000000000000000000')
        Unknown4010(3)
        Unknown4009(3)

        def upon_3():
            Unknown1086(3)
            Unknown1007(-200000)
            if SLOT_51:
                if (SLOT_23 < 60000):
                    GFX_1('jief_garudine_jimen_03', 104)

        def upon_32():
            GFX_0('TatsumakiDelete', 100)
            Unknown13(25)
        Unknown3032()
        Unknown4003('796f65665f3433315f746f726e616430322e4449470000000000000000000000796f65665f3433315f746f726e616430325f303030302e6d6d6f740000000000')
        Unknown4015()
        Unknown3001(0)
        GFX_0('Tatsumaki_start', 100)
        GFX_0('Tatsumaki_jizoku', 100)
    sprite('vr_dmy_tatsumaki', 24)	# 1-24
    Unknown23027()
    sprite('vr_dmy_tatsumaki', 5)	# 25-29
    SLOT_51 = 1
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 30-34
    sprite('vr_dmy_tatsumaki', 5)	# 35-39
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 40-44
    sprite('vr_dmy_tatsumaki', 5)	# 45-49
    Unknown3004(26)
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 50-54
    sprite('vr_dmy_tatsumaki', 5)	# 55-59
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 60-64
    sprite('vr_dmy_tatsumaki', 5)	# 65-69
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 70-74
    sprite('vr_dmy_tatsumaki', 5)	# 75-79
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 80-84
    sprite('vr_dmy_tatsumaki', 5)	# 85-89
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 90-94
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 95-99
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 100-104
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 105-109
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 110-114
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 115-119
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 120-124
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 125-129
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 130-134
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 135-139
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 140-144
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 145-149
    RefreshMultihit()
    SFX_3('yo008')
    sprite('vr_dmy_tatsumaki', 5)	# 150-154
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 155-159
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 160-164
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 165-169
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 170-174
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 175-179
    RefreshMultihit()

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
def DDD_Wind():

    def upon_IMMEDIATE():
        Unknown2055(120)
        loopRelated(17, 90)

        def upon_17():
            sendToLabel(1)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
            Unknown23033(50)
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('yoef_DDD_wind', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 7)	# 5-11
    GFX_1('yoef_DDD_wind', -1)
    gotoLabel(1)