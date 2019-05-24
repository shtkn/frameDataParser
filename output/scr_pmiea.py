@State
def PMI_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('504d495f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PMI_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PMI_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PMI_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 9990):
            Unknown23185('504d495f506572736f6e6135413474680000000000000000000000000000000032000000')
        if (SLOT_48 == 9980):
            Unknown23185('504d495f506572736f6e6134505300000000000000000000000000000000000032000000')
        if (SLOT_48 == 4320):
            Unknown23185('504d495f506572736f6e6136505300000000000000000000000000000000000032000000')
        if (SLOT_48 == 2330):
            Unknown23185('504d495f506572736f6e613242326e640000000000000000000000000000000032000000')
        if (SLOT_48 == 2540):
            Unknown23185('504d495f506572736f6e614169723541326e640000000000000000000000000032000000')
        if (SLOT_48 == 2550):
            Unknown23185('504d495f506572736f6e6141697235430000000000000000000000000000000032000000')
        if (SLOT_48 == 2320):
            Unknown23185('504d495f506572736f6e614d6172696e4b6172696e000000000000000000000064000000')
        if (SLOT_48 == 4030):
            Unknown23185('504d495f506572736f6e6154656e74617261666f6f000000000000000000000064000000')
        if (SLOT_48 == 4020):
            Unknown23185('504d495f506572736f6e61427566756c6100000000000000000000000000000064000000')
        if (SLOT_48 == 4310):
            Unknown23185('504d495f506572736f6e614275667564796e6500000000000000000000000000c8000000')
        if (SLOT_48 == 4311):
            Unknown23185('504d495f506572736f6e614275667564796e6553500000000000000000000000c8000000')
        if (SLOT_48 == 4312):
            Unknown23185('504d495f506572736f6e614275667564796e655f445344000000000000000000c8000000')
        if (SLOT_48 == 4313):
            Unknown23185('504d495f506572736f6e614275667564796e6553505f44534400000000000000c8000000')
        if (SLOT_48 == 4500):
            Unknown23185('504d495f506572736f6e614963686967656b69310000000000000000000000002c010000')
        if (SLOT_48 == 4501):
            Unknown23185('504d495f506572736f6e614963686967656b69320000000000000000000000002c010000')
        if (SLOT_48 == 9999):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')
        if (SLOT_48 == 6100):
            Unknown23185('504d495f506572736f6e614d6174636857696e000000000000000000000000002c010000')

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
def PMI_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PMI_AttackInit():
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
    callSubroutine('PMI_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PMI_SPAttackInit():
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
    callSubroutine('PMI_ReceptionSignal')
    Unknown11034(1)
    Unknown11033(0)
    Unknown23023()
    Unknown2017(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PMI_DDAttackInit():
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
    callSubroutine('PMI_ReceptionSignal')
    Unknown23023()

@Subroutine
def PMI_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PMI_ForceWarp():
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
    enterState('PMI_PersonaWait')

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
        callSubroutine('PMI_ReceptionSignal')
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
def PMI_Persona5A4th():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000000000000000000c0f2fcff400d03000000000000000000')
        callSubroutine('PMI_AttackInit')
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(1)
        Unknown9310(10)
        Unknown9266(9)
        Unknown23078(0)
        Unknown4007(3)
        Unknown2017(1)
        Unknown2053(1)
        callSubroutine('PMI_CheckWarp')

        def upon_56():

            def upon_44():
                sendToLabel(2)
            sendToLabel(1)
        Unknown23059(1)
    sprite('ar204_00', 3)	# 1-3
    sprite('ar204_01', 1)	# 4-4
    physicsXImpulse(80000)
    Unknown4007(0)
    sprite('ar204_01', 1)	# 5-5
    Unknown1019(60)
    sprite('ar204_01', 1)	# 6-6
    Unknown1019(60)
    label(0)
    sprite('ar204_02', 2)	# 7-8
    Unknown1019(0)
    SLOT_51 = (SLOT_51 + 1)
    sprite('ar204_03', 1)	# 9-9	 **attackbox here**
    GFX_0('aref_204', 100)
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(0)
    PushbackX(4000)
    SFX_3('hit_h_middle')
    sprite('ar204_03', 1)	# 10-10	 **attackbox here**
    Unknown23022(0)
    sprite('ar204_04', 2)	# 11-12
    sprite('ar204_05', 2)	# 13-14
    sprite('ar204_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(-5000)
    AirPushbackX(-2000)
    PushbackX(8000)
    SFX_3('hit_l_slow')
    sprite('ar204_07', 2)	# 17-18
    sprite('ar204_08', 2)	# 19-20
    sprite('ar204_09', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(-15000)
    AirPushbackX(2000)
    PushbackX(2000)
    SFX_3('hit_m_middle')
    if (SLOT_51 == 1):
        AirUntechableTime(40)
        Unknown9310(0)
        AirPushbackY(-100000)
        AirPushbackX(10000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9190(1)
        Unknown9118(30)
    sprite('ar204_10', 4)	# 24-27
    Unknown23029(3, 7000, 0)
    if (SLOT_51 == 1):
        sendToLabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ar204_11', 3)	# 28-30
    physicsXImpulse(0)
    clearUponHandler(56)
    sprite('ar204_12', 4)	# 31-34
    sprite('ar204_13', 4)	# 35-38
    sprite('ar204_14', 4)	# 39-42
    sprite('ar204_12', 5)	# 43-47
    sprite('ar204_13', 5)	# 48-52
    sprite('ar204_14', 5)	# 53-57
    sprite('ar204_12', 5)	# 58-62
    sprite('ar204_13', 5)	# 63-67
    sprite('ar204_14', 5)	# 68-72
    label(2)
    sprite('keep', 32767)	# 73-32839
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona6PS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000010b6fdff00000000e05ef8ffe09304000000000000000000')
        callSubroutine('PMI_AttackInit')
        AttackLevel_(3)
        Hitstop(6)
        Unknown9266(9)
        Unknown11042(1)
        Unknown2017(0)
        Unknown2053(1)
        Unknown2034(1)
        Unknown2019(501)
        callSubroutine('PMI_CheckWarp')
    sprite('ar432_00', 6)	# 1-6
    sprite('ar432_01', 3)	# 7-9
    sprite('ar432_02', 3)	# 10-12
    sprite('ar432_03', 3)	# 13-15
    sprite('ar432_04', 3)	# 16-18
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4321, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4324, 0)
    sprite('ar432_05', 3)	# 19-21
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4322, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4323, 0)
    sprite('ar432_06', 3)	# 22-24
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4323, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4322, 0)
    sprite('ar432_07', 3)	# 25-27
    SFX_3('ice_fast')
    GFX_0('Tsurara_Shot', 0)
    Unknown23029(1, 4324, 0)
    GFX_0('Tsurara_Shot', 1)
    Unknown23029(1, 4321, 0)
    sprite('ar432_08', 3)	# 28-30
    sprite('ar432_09', 3)	# 31-33
    sprite('ar432_10', 3)	# 34-36
    sprite('ar432_19', 3)	# 37-39
    Unknown21015('547375726172615f53686f740000000000000000000000000000000000000000e510000000000000')
    sprite('ar432_20', 6)	# 40-45
    sprite('ar432_21', 6)	# 46-51
    sprite('ar432_22', 6)	# 52-57
    sprite('ar432_20', 6)	# 58-63
    sprite('ar432_21', 6)	# 64-69
    sprite('ar432_22', 6)	# 70-75
    sprite('ar432_20', 6)	# 76-81
    sprite('ar432_21', 6)	# 82-87
    sprite('ar432_22', 6)	# 88-93
    sprite('ar432_20', 6)	# 94-99
    sprite('ar432_21', 6)	# 100-105
    sprite('ar432_22', 6)	# 106-111
    sprite('keep', 32767)	# 112-32878
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona4PS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c3000000000000000000000000000000000000')
        callSubroutine('PMI_SPAttackInit')
        AttackLevel_(4)
        AttackP1(70)
        Hitstop(7)
        AirUntechableTime(60)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-4000)
        AirPushbackY(28000)
        YImpluseBeforeWallbounce(1500)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9266(9)
        Unknown23078(1)
        Unknown11056(2)
        Unknown11042(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PMI_CheckWarp')
        Unknown23059(1)
    sprite('ar254_00', 4)	# 1-4
    sprite('ar254_01', 3)	# 5-7
    GFX_0('aref_254', 100)
    sprite('ar254_02', 1)	# 8-8	 **attackbox here**
    SFX_3('slash_pole_middle')
    RefreshMultihit()
    sprite('ar254_02', 3)	# 9-11	 **attackbox here**
    sprite('ar254_03', 4)	# 12-15	 **attackbox here**
    sprite('ar254_04', 4)	# 16-19
    Unknown23029(3, 7000, 0)
    sprite('ar254_05', 4)	# 20-23
    sprite('ar254_06', 4)	# 24-27
    sprite('ar254_07', 5)	# 28-32
    sprite('ar254_08', 5)	# 33-37
    sprite('ar254_09', 5)	# 38-42
    sprite('ar254_10', 5)	# 43-47
    sprite('keep', 32767)	# 48-32814
    enterState('PersonaDeleteAndIdling')

@State
def PMI_Persona2B2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0f2fcff400d03000000000000000000')
        callSubroutine('PMI_AttackInit')
        AttackLevel_(5)
        Damage(1300)
        Hitstop(7)
        AirPushbackX(20000)
        AirPushbackY(24000)
        YImpluseBeforeWallbounce(1500)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        PushbackX(3000)
        Unknown9266(9)
        Unknown11034(0)
        Unknown11033(1)
        callSubroutine('PMI_CheckWarp')

        def upon_77():
            SLOT_51 = 1
    sprite('ar233_00', 4)	# 1-4
    Unknown2006()
    sprite('ar233_01', 4)	# 5-8
    sprite('ar233_02', 4)	# 9-12
    GFX_1('mief_muchispeeds_04', 0)
    SFX_3('slash_sword_middle')
    sprite('ar233_03', 2)	# 13-14	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 0)
    GFX_0('MuchiAura2D', 1)
    RefreshMultihit()
    SFX_3('ice_fast')
    sprite('ar233_03a', 1)	# 15-15	 **attackbox here**
    if (not SLOT_51):
        Unknown23029(3, 7000, 0)
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_03a', 1)	# 16-16	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_04', 1)	# 17-17	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_04', 1)	# 18-18	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 1)
    sprite('ar233_04a', 1)	# 19-19	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar233_04a', 1)	# 20-20	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 1)
    sprite('ar233_03b', 1)	# 21-21	 **attackbox here**
    GFX_1('mief_muchispeeds_04', 0)
    sprite('ar234_00', 1)	# 22-22
    StartMultihit()
    sprite('ar234_01', 1)	# 23-23
    sprite('ar234_02', 1)	# 24-24	 **attackbox here**
    StartMultihit()
    if SLOT_51:
        GFX_0('2BBhikiyose', -1)
    SFX_3('slash_rapier_fast')
    sprite('ar234_03', 4)	# 25-28
    sprite('ar234_04', 4)	# 29-32
    sprite('ar234_05', 3)	# 33-35
    sprite('ar234_06', 3)	# 36-38
    sprite('ar234_07', 3)	# 39-41
    sprite('keep', 32767)	# 42-32808
    enterState('PersonaDeleteAndIdling')

@State
def __2BBhikiyose():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1300)
        Hitstop(0)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-5000)
        AirPushbackY(-30000)
        PushbackX(-60000)
        Unknown9190(1)
        Unknown9118(20)
        Unknown9266(9)
        Unknown23151(22, 103)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 2331, 0)
        Unknown23059(1)
    sprite('dmy_atk01', 1)	# 1-1
    RefreshMultihit()
    sprite('null', 1)	# 2-2
    Unknown23029(3, 7000, 0)

@State
def PMI_PersonaAir5A2nd():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c30000c0f2fcff400d03000000000000000000')
        callSubroutine('PMI_AttackInit')
        AttackLevel_(4)
        AirHitstunAnimation(10)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9266(9)
        Unknown23078(1)
        callSubroutine('PMI_CheckWarp')
        Unknown4007(3)
    sprite('ar254_00', 4)	# 1-4
    Unknown1007(-80000)
    sprite('ar254_01', 3)	# 5-7
    GFX_0('aref_254', 100)
    sprite('ar254_02', 1)	# 8-8	 **attackbox here**
    SFX_3('slash_pole_middle')
    RefreshMultihit()
    sprite('ar254_02', 3)	# 9-11	 **attackbox here**
    sprite('ar254_03', 4)	# 12-15	 **attackbox here**
    sprite('ar254_04', 4)	# 16-19
    sprite('ar254_05', 4)	# 20-23
    sprite('ar254_06', 4)	# 24-27
    sprite('ar254_07', 5)	# 28-32
    sprite('ar254_08', 5)	# 33-37
    sprite('ar254_09', 5)	# 38-42
    sprite('ar254_10', 5)	# 43-47
    sprite('keep', 32767)	# 48-32814
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaAir5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff50c30000c0f2fcff400d03000000000000000000')
        callSubroutine('PMI_AttackInit')
        AttackLevel_(5)
        Damage(1300)
        Hitstop(7)
        AirPushbackX(15000)
        AirPushbackY(14000)
        YImpluseBeforeWallbounce(2500)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        PushbackX(3000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9266(9)
        Unknown11034(0)
        Unknown11033(1)
        callSubroutine('PMI_CheckWarp')

        def upon_77():
            SLOT_51 = 1
        Unknown23059(1)
    sprite('ar255_00', 12)	# 1-12
    sprite('ar255_01', 4)	# 13-16
    sprite('ar255_02', 2)	# 17-18
    GFX_1('mief_muchispeeda_04', 0)
    SFX_3('slash_sword_middle')
    sprite('ar255_02', 2)	# 19-20
    GFX_1('mief_muchispeeda_04', 1)
    GFX_0('MuchAuraAir5D', 2)
    sprite('ar255_03', 2)	# 21-22	 **attackbox here**
    GFX_1('mief_muchispeeda_04', 0)
    SFX_3('ice_fast')
    RefreshMultihit()
    sprite('ar255_03a', 2)	# 23-24	 **attackbox here**
    GFX_1('mief_muchispeeda_04', 0)
    sprite('ar255_04', 2)	# 25-26	 **attackbox here**
    sprite('ar255_04a', 2)	# 27-28	 **attackbox here**
    sprite('ar255_05', 1)	# 29-29	 **attackbox here**
    sprite('ar256_00', 1)	# 30-30
    if (not SLOT_51):
        Unknown23029(3, 7000, 0)
    sprite('ar256_01', 1)	# 31-31
    sprite('ar256_02', 1)	# 32-32
    sprite('ar256_03', 1)	# 33-33
    sprite('ar256_04', 4)	# 34-37	 **attackbox here**
    StartMultihit()
    if SLOT_51:
        GFX_0('Air5Chikiyose', -1)
    SFX_3('slash_rapier_fast')
    sprite('ar256_05', 5)	# 38-42
    sprite('ar256_06', 5)	# 43-47
    sprite('ar256_07', 5)	# 48-52
    sprite('keep', 32767)	# 53-32819
    enterState('PersonaDeleteAndIdling')

@State
def Air5Chikiyose():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(1300)
        Hitstop(0)
        AirUntechableTime(60)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(-10000)
        AirPushbackY(40000)
        PushbackX(-60000)
        YImpluseBeforeWallbounce(2200)
        Unknown9266(9)
        Unknown23151(22, 103)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 2551, 0)
    sprite('dmy_atk01', 1)	# 1-1
    RefreshMultihit()
    sprite('null', 1)	# 2-2
    Unknown23029(3, 7000, 0)

@State
def PMI_PersonaMarinKarin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0f2fcff400d03000000000000000000')
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
    sprite('ar232_00', 4)	# 1-4
    Unknown2006()
    sprite('ar232_01', 4)	# 5-8
    sprite('ar232_02', 4)	# 9-12
    sprite('ar232_03', 3)	# 13-15
    sprite('ar232_04', 3)	# 16-18
    sprite('ar232_05', 3)	# 19-21
    sprite('ar232_06', 1)	# 22-22
    GFX_0('MarinKarin_shot', 0)
    sprite('ar232_06', 4)	# 23-26
    Unknown23022(0)
    sprite('ar232_07', 5)	# 27-31
    sprite('ar232_08', 5)	# 32-36
    sprite('ar232_06', 5)	# 37-41
    sprite('ar232_07', 5)	# 42-46
    sprite('ar232_08', 5)	# 47-51
    sprite('keep', 32767)	# 52-32818
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaTentarafoo():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff0000000000000000000000000000000000000000')
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')

        def upon_3():
            if SLOT_51:
                clearUponHandler(3)
                sendToLabel(1)

        def upon_56():
            clearUponHandler(3)
        Unknown2006()
        Unknown23022(1)
    sprite('ar403_00', 3)	# 1-3
    GFX_0('aref_403_hand', 0)
    sprite('ar403_01', 3)	# 4-6
    sprite('ar403_02', 3)	# 7-9
    sprite('ar403_03', 2)	# 10-11
    sprite('ar403_04', 3)	# 12-14
    SFX_3('hit_m_fast')
    Unknown26('aref_403_hand')
    sprite('ar403_05', 3)	# 15-17
    GFX_0('Tentarafu_dmy', 0)
    sprite('ar403_06', 3)	# 18-20
    sprite('ar403_07', 3)	# 21-23
    sprite('ar403_05', 4)	# 24-27
    sprite('ar403_06', 4)	# 28-31
    sprite('ar403_07', 4)	# 32-35
    sprite('ar403_05', 4)	# 36-39
    sprite('ar403_06', 4)	# 40-43
    sprite('ar403_07', 4)	# 44-47
    sprite('ar403_05', 4)	# 48-51
    sprite('ar403_06', 4)	# 52-55
    sprite('ar403_07', 4)	# 56-59
    sprite('ar403_05', 4)	# 60-63
    sprite('ar403_06', 4)	# 64-67
    sprite('ar403_07', 4)	# 68-71
    sprite('ar403_05', 4)	# 72-75
    sprite('ar403_06', 4)	# 76-79
    sprite('keep', 32767)	# 80-32846
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('ar403_05', 3)	# 32847-32849
    sprite('ar403_06', 3)	# 32850-32852
    sprite('ar403_07', 3)	# 32853-32855
    sprite('ar403_05', 3)	# 32856-32858
    sprite('ar403_06', 3)	# 32859-32861
    sprite('ar403_07', 3)	# 32862-32864
    sprite('ar403_05', 3)	# 32865-32867
    sprite('ar403_06', 3)	# 32868-32870
    sprite('ar403_07', 3)	# 32871-32873
    sprite('ar403_05', 3)	# 32874-32876
    sprite('ar403_06', 3)	# 32877-32879
    sprite('ar403_07', 3)	# 32880-32882
    Unknown21015('54656e7461726166755f646d7900000000000000000000000000000000000000c00f000000000000')
    sprite('ar403_06', 3)	# 32883-32885
    sprite('ar403_07', 3)	# 32886-32888
    sprite('ar403_05', 3)	# 32889-32891
    sprite('ar403_06', 3)	# 32892-32894
    sprite('ar403_07', 3)	# 32895-32897
    sprite('ar403_05', 3)	# 32898-32900
    sprite('ar403_06', 3)	# 32901-32903
    sprite('ar403_07', 3)	# 32904-32906
    sprite('ar403_05', 3)	# 32907-32909
    sprite('ar403_06', 4)	# 32910-32913
    sprite('keep', 32767)	# 32914-65680
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufula():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c300000000000000000000000000000000000000000000')
        callSubroutine('PMI_SPAttackInit')
        callSubroutine('PMI_CheckWarp')
    sprite('ar402_00', 4)	# 1-4
    GFX_0('IceMiller_Shot', 100)
    sprite('ar402_01', 4)	# 5-8
    sprite('ar402_02', 4)	# 9-12
    sprite('ar402_03', 4)	# 13-16
    sprite('ar402_04', 4)	# 17-20
    sprite('ar402_05', 6)	# 21-26
    sprite('ar402_06', 6)	# 27-32
    sprite('ar402_07', 6)	# 33-38
    sprite('keep', 32767)	# 39-32805
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyne():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffa086010000000000000000000000000000000000')
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)	# 1-6
    sprite('ar431_01', 6)	# 7-12
    sprite('ar431_02', 6)	# 13-18
    sprite('ar431_03', 6)	# 19-24
    GFX_0('aref_431C', 100)
    GFX_0('aref_431_colC', 100)
    sprite('ar431_04', 4)	# 25-28
    sprite('ar431_05', 4)	# 29-32
    sprite('ar431_06', 6)	# 33-38
    sprite('ar431_07', 6)	# 39-44
    sprite('ar431_08', 6)	# 45-50
    sprite('ar431_06', 8)	# 51-58
    sprite('ar431_07', 8)	# 59-66
    sprite('ar431_08', 8)	# 67-74
    sprite('ar431_06', 8)	# 75-82
    sprite('ar431_07', 8)	# 83-90
    sprite('ar431_08', 8)	# 91-98
    sprite('ar431_06', 8)	# 99-106
    sprite('ar431_07', 8)	# 107-114
    sprite('ar431_08', 8)	# 115-122
    sprite('keep', 32767)	# 123-32889
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyneSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffa086010000000000000000000000000000000000')
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)	# 1-6
    sprite('ar431_01', 6)	# 7-12
    sprite('ar431_02', 6)	# 13-18
    sprite('ar431_03', 6)	# 19-24
    GFX_0('aref_431CD', 100)
    GFX_0('aref_431_colCD', 100)
    sprite('ar431_04', 4)	# 25-28
    sprite('ar431_05', 4)	# 29-32
    sprite('ar431_06', 6)	# 33-38
    sprite('ar431_07', 6)	# 39-44
    sprite('ar431_08', 6)	# 45-50
    sprite('ar431_06', 8)	# 51-58
    sprite('ar431_07', 8)	# 59-66
    sprite('ar431_08', 8)	# 67-74
    sprite('ar431_06', 8)	# 75-82
    sprite('ar431_07', 8)	# 83-90
    sprite('ar431_08', 8)	# 91-98
    sprite('ar431_06', 8)	# 99-106
    sprite('ar431_07', 8)	# 107-114
    sprite('ar431_08', 8)	# 115-122
    sprite('keep', 32767)	# 123-32889
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyne_DSD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffa086010000000000000000000000000000000000')
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)	# 1-6
    sprite('ar431_01', 6)	# 7-12
    sprite('ar431_02', 6)	# 13-18
    sprite('ar431_03', 6)	# 19-24
    GFX_0('aref_431C', 100)
    GFX_0('aref_431_colC_DSD', 100)
    sprite('ar431_04', 4)	# 25-28
    sprite('ar431_05', 4)	# 29-32
    sprite('ar431_06', 6)	# 33-38
    sprite('ar431_07', 6)	# 39-44
    sprite('ar431_08', 6)	# 45-50
    sprite('ar431_06', 8)	# 51-58
    sprite('ar431_07', 8)	# 59-66
    sprite('ar431_08', 8)	# 67-74
    sprite('ar431_06', 8)	# 75-82
    sprite('ar431_07', 8)	# 83-90
    sprite('ar431_08', 8)	# 91-98
    sprite('ar431_06', 8)	# 99-106
    sprite('ar431_07', 8)	# 107-114
    sprite('ar431_08', 8)	# 115-122
    sprite('keep', 32767)	# 123-32889
    enterState('PersonaDeleteAndIdling')

@State
def PMI_PersonaBufudyneSP_DSD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffffa086010000000000000000000000000000000000')
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown23022(1)
        Unknown2054(1)
    sprite('ar431_00', 6)	# 1-6
    sprite('ar431_01', 6)	# 7-12
    sprite('ar431_02', 6)	# 13-18
    sprite('ar431_03', 6)	# 19-24
    GFX_0('aref_431CD', 100)
    GFX_0('aref_431_colCD_DSD', 100)
    sprite('ar431_04', 4)	# 25-28
    sprite('ar431_05', 4)	# 29-32
    sprite('ar431_06', 6)	# 33-38
    sprite('ar431_07', 6)	# 39-44
    sprite('ar431_08', 6)	# 45-50
    sprite('ar431_06', 8)	# 51-58
    sprite('ar431_07', 8)	# 59-66
    sprite('ar431_08', 8)	# 67-74
    sprite('ar431_06', 8)	# 75-82
    sprite('ar431_07', 8)	# 83-90
    sprite('ar431_08', 8)	# 91-98
    sprite('ar431_06', 8)	# 99-106
    sprite('ar431_07', 8)	# 107-114
    sprite('ar431_08', 8)	# 115-122
    sprite('keep', 32767)	# 123-32889
    enterState('PersonaDeleteAndIdling')

@State
def mief203_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi203_00', 2)	# 1-2
    sprite('vr_mi203_01', 2)	# 3-4
    sprite('vr_mi203_02', 30)	# 5-34

@State
def mief207_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        teleportRelativeX(-100000)
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi207_00', 30)	# 1-30

@State
def mief201_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi201_00', 2)	# 1-2
    sprite('vr_mi201_01', 2)	# 3-4
    teleportRelativeX(-182000)
    sprite('vr_mi201_02', 30)	# 5-34
    teleportRelativeX(-30000)

@State
def mief202_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi202_00', 1)	# 1-1
    sprite('vr_mi202_01', 3)	# 2-4
    sprite('vr_mi202_02', 30)	# 5-34

@State
def mief210_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi210_00', 2)	# 1-2
    sprite('vr_mi210_01', 2)	# 3-4
    sprite('vr_mi210_02', 3)	# 5-7

@State
def mief211_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi211_00', 2)	# 1-2
    sprite('vr_mi211_01', 30)	# 3-32

@State
def mief211_Zanzoh_CA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi211_00', 2)	# 1-2
    sprite('vr_mi211_01', 28)	# 3-30

@State
def aref_204():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663230345f6d7563686930302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 30)	# 1-30
    GFX_1('mief_slashkira_01', 100)

@State
def MuchiAura2D():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('mief_muchisentan_02')
        Unknown1072(-30000)
    sprite('null', 8)	# 1-8
    physicsXImpulse(30000)
    physicsYImpulse(15000)
    sprite('null', 5)	# 9-13
    Unknown3004(-51)

@State
def aref_254():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663235345f6d7563686930302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4015()
    sprite('null', 15)	# 1-15
    GFX_1('mief_slashkira_01', 100)

@State
def MuchAuraAir5D():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('mief_muchisentan_02')
        Unknown1072(30000)
    sprite('null', 6)	# 1-6
    physicsXImpulse(40000)
    physicsYImpulse(-21000)
    sprite('null', 5)	# 7-11
    Unknown3004(-51)

@State
def mief_311():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vr_mi311_00', 2)	# 1-2
    sprite('vr_mi311_01', 2)	# 3-4
    sprite('vr_mi311_02', 2)	# 5-6
    sprite('vr_mi311_03', 2)	# 7-8
    sprite('vr_mi311_04', 2)	# 9-10

@State
def mief_311_HitEff():

    def upon_IMMEDIATE():
        Unknown23151(22, 105)
        Unknown23067('ef_hit_slashm')
        Unknown4049(500)
        Unknown4053(30000, 150000)
        Unknown4045('65665f6869746c7a30300000000000000000000000000000000000000000000064000000')
        SFX_3('damage_slash_h')
    sprite('null', 10)	# 1-10

@State
def mief_311_finish():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(255)
        Unknown3004(-25)
    sprite('vr_mi311_10', 4)	# 1-4
    sprite('vr_mi311_11', 16)	# 5-20

@State
def Tsurara_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(600)
        AttackP1(70)
        AttackP2(97)
        Unknown11042(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(50)
        Unknown9016(1)
        Unknown9266(9)
        Unknown11057(500)
        Unknown4008(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(2, 9)
        sendToLabelUpon(54, 9)

        def upon_43():
            if (SLOT_48 == 4321):
                SLOT_51 = 1
                physicsYImpulse(400)
                Unknown1007(400)
            if (SLOT_48 == 4322):
                SLOT_51 = 2
                physicsYImpulse(-400)
                Unknown1007(-400)
            if (SLOT_48 == 4323):
                SLOT_51 = 3
                physicsYImpulse(-400)
                Unknown1007(-400)
            if (SLOT_48 == 4324):
                SLOT_51 = 4
                physicsYImpulse(400)
                Unknown1007(400)
                SLOT_52 = 1
            if (SLOT_48 == 4325):
                if (SLOT_51 > 0):
                    sendToLabel(1)
            if (SLOT_48 == 4326):
                sendToLabel(9)
        Unknown4061(3)
        Unknown3033()
        GFX_0('aref_432_pa', 100)
        Unknown38(4, 1)
        Unknown23027()
    sprite('vr_ar432_00', 15)	# 1-15	 **attackbox here**
    label(5)
    sprite('vr_ar432_00', 30)	# 16-45	 **attackbox here**
    YAccel(-100)
    loopRest()
    gotoLabel(5)
    label(1)
    sprite('vr_ar432_00', 5)	# 46-50	 **attackbox here**
    Unknown4010(0)
    Unknown1074(30000)
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 5)	# 51-55	 **attackbox here**
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 5)	# 56-60	 **attackbox here**
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 5)	# 61-65	 **attackbox here**
    RefreshMultihit()
    Unknown1074(0)
    Unknown1072(0)
    SLOT_12 = SLOT_19
    Unknown1019(5)
    if (SLOT_12 < 20000):
        SLOT_12 = 20000
    Unknown1028(300)
    Unknown47('0100000000000000400d03000200000017000000020000000d000000')
    YAccel(5)
    Unknown1108(0)
    GFX_1('aref_turarashot_fire', 100)
    GFX_0('aref_432_move', 100)
    Unknown38(5, 1)
    if SLOT_52:
        SFX_3('slash_rapier_fast')
    sprite('vr_ar432_00', 180)	# 66-245	 **attackbox here**
    Unknown53(1)
    label(9)
    sprite('null', 30)	# 246-275
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown23027()
    Unknown13(4)
    Unknown13(5)
    GFX_1('aref_turarashot_delete', 100)

@State
def aref_432_pa():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 1)	# 1-1
    GFX_1('aref_turarashot', 100)
    loopRest()
    gotoLabel(0)

@State
def aref_432_move():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 1)	# 1-1
    GFX_1('aref_turarashot_move', 100)
    loopRest()
    gotoLabel(0)

@State
def mief_400():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('6d6965663430305f736c6173682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)
        Unknown4061(0)
        Unknown23122(55)
    sprite('null', 5)	# 1-5
    Unknown1096(750)
    Unknown1099(20)
    teleportRelativeX(-16000)
    Unknown1007(64000)
    Unknown1097(20)
    sprite('null', 6)	# 6-11
    teleportRelativeX(-16000)
    Unknown1007(-64000)
    Unknown1097(80)
    sprite('null', 6)	# 12-17
    Unknown1099(0)
    Unknown3004(-48)
    teleportRelativeX(16000)
    Unknown1007(-4000)

@State
def mief_400_2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('6d6965663430305f736c617368322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)
        Unknown4061(0)
        Unknown23122(55)
    sprite('null', 5)	# 1-5
    Unknown1096(750)
    Unknown1099(20)
    Unknown3001(0)
    Unknown3004(32)
    teleportRelativeX(-16000)
    Unknown1007(64000)
    Unknown1097(20)
    sprite('null', 6)	# 6-11
    Unknown3001(255)
    Unknown3004(0)
    teleportRelativeX(-16000)
    Unknown1007(-64000)
    Unknown1097(80)
    sprite('null', 6)	# 12-17
    Unknown1099(0)
    Unknown3004(-48)
    teleportRelativeX(16000)
    Unknown1007(-8000)

@State
def mief_401():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(0)
        Unknown23122(55)
        Unknown4010(2)
        Unknown4003('617265663430315f7473756b6930302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()

        def upon_43():
            if (SLOT_48 == 4011):
                clearUponHandler(43)
                sendToLabel(10)
            if (SLOT_48 == 4012):
                clearUponHandler(43)
                sendToLabel(100)
    sprite('null', 6)	# 1-6
    Unknown3001(150)
    GFX_0('mief401_shock', 100)
    sprite('null', 5)	# 7-11
    Unknown1067(-200)
    Unknown1059(100)
    Unknown3004(51)
    ExitState()
    label(10)
    sprite('null', 13)	# 12-24
    sprite('null', 5)	# 25-29
    Unknown1067(-200)
    Unknown1059(100)
    Unknown3004(51)
    ExitState()
    label(100)
    sprite('null', 5)	# 30-34
    sprite('null', 5)	# 35-39
    Unknown1067(-200)
    Unknown1059(100)
    Unknown3004(51)

@State
def mief401_shock():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663430315f7473756b6930312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown4061(0)
        Unknown23122(55)
        Unknown3001(150)
        Unknown3033()
    sprite('null', 12)	# 1-12
    GFX_0('mief401_shockAdd', 100)

@State
def mief401_shockAdd():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3001(120)
        Unknown3033()
    sprite('vr_mi401_add', 5)	# 1-5
    Unknown1067(-55)
    sprite('vr_mi401_add', 5)	# 6-10
    Unknown3004(-51)

@State
def MarinKarin_shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Unknown11001(0, 10, 10)
        Unknown11050('080000007374617475735f636861726d5f64616d61676500000000000000000000000000')
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 1)
        Unknown11106(0)
        Unknown2053(1)
        Unknown23027()
        Unknown4061(3)
        Unknown3032()
        Unknown3029(1)
        Unknown3070(2)
        Unknown3071(10)
        Unknown3074('00000000ff000000ff000000ff000000')
        Unknown3075('00000000ff000000ff000000ff000000')

        def upon_LANDING():
            clearUponHandler(2)
            Unknown23090(25)

        def upon_43():
            if (SLOT_48 == 2321):
                clearUponHandler(43)
                Unknown23090(25)

        def upon_78():
            SFX_3('mi004')
            Unknown2058(250)
            Unknown36(22)
            Unknown2058(-500)
            Unknown35()
    sprite('vr_ar232_00', 2)	# 1-2	 **attackbox here**
    GFX_0('MarinKarin_Jizoku', 0)
    GFX_1('mief_marincarin_02', 0)
    Unknown1072(12000)
    Unknown1096(500)
    sprite('vr_ar232_01', 2)	# 3-4	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    Unknown1096(600)
    sprite('vr_ar232_02', 2)	# 5-6	 **attackbox here**
    Unknown1096(700)
    sprite('vr_ar232_03', 2)	# 7-8	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    Unknown1096(900)
    sprite('vr_ar232_04', 2)	# 9-10	 **attackbox here**
    Unknown1096(1000)
    sprite('vr_ar232_05', 2)	# 11-12	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_06', 2)	# 13-14	 **attackbox here**
    sprite('vr_ar232_07', 2)	# 15-16	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_08', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ar232_09', 2)	# 19-20	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_10', 2)	# 21-22	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_ar232_11', 2)	# 23-24	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_12', 2)	# 25-26	 **attackbox here**
    sprite('vr_ar232_13', 2)	# 27-28	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_14', 2)	# 29-30	 **attackbox here**
    sprite('vr_ar232_15', 2)	# 31-32	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_16', 2)	# 33-34	 **attackbox here**
    sprite('vr_ar232_17', 2)	# 35-36	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_18', 2)	# 37-38	 **attackbox here**
    sprite('vr_ar232_19', 2)	# 39-40	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    SFX_3('badst_charm_damage')
    physicsXImpulse(1000)
    physicsYImpulse(1000)
    setGravity(0)

    def upon_3():
        Unknown1019(98)
        YAccel(98)
        SLOT_58 = SLOT_40
        if (SLOT_40 > 100):
            SLOT_58 = (SLOT_58 / 5120)
            if SLOT_38:
                SLOT_58 = (SLOT_58 / (-1))
            SLOT_12 = (SLOT_12 + SLOT_58)
        if (SLOT_40 < (-100)):
            SLOT_58 = (SLOT_58 / 5120)
            if SLOT_38:
                SLOT_58 = (SLOT_58 / (-1))
            SLOT_12 = (SLOT_12 + SLOT_58)
        if (SLOT_12 < 5000):
            SLOT_12 = 5000
        SLOT_58 = SLOT_41
        if (SLOT_41 > 100):
            SLOT_58 = (SLOT_58 + 50000)
            SLOT_58 = (SLOT_58 / 5120)
            SLOT_13 = (SLOT_13 + SLOT_58)
        if (SLOT_41 < (-100)):
            SLOT_58 = (SLOT_58 + 50000)
            SLOT_58 = (SLOT_58 / 5120)
            SLOT_13 = (SLOT_13 + SLOT_58)
    SLOT_51 = 4
    label(0)
    sprite('vr_ar232_00', 2)	# 41-42	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_ar232_01', 2)	# 43-44	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_02', 2)	# 45-46	 **attackbox here**
    sprite('vr_ar232_03', 2)	# 47-48	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_04', 2)	# 49-50	 **attackbox here**
    sprite('vr_ar232_05', 2)	# 51-52	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_06', 2)	# 53-54	 **attackbox here**
    sprite('vr_ar232_07', 2)	# 55-56	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_08', 2)	# 57-58	 **attackbox here**
    sprite('vr_ar232_09', 2)	# 59-60	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_10', 2)	# 61-62	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_ar232_11', 2)	# 63-64	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_12', 2)	# 65-66	 **attackbox here**
    sprite('vr_ar232_13', 2)	# 67-68	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_14', 2)	# 69-70	 **attackbox here**
    sprite('vr_ar232_15', 2)	# 71-72	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_16', 2)	# 73-74	 **attackbox here**
    sprite('vr_ar232_17', 2)	# 75-76	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    sprite('vr_ar232_18', 2)	# 77-78	 **attackbox here**
    sprite('vr_ar232_19', 2)	# 79-80	 **attackbox here**
    GFX_1('mief_marincarin_02', 0)
    SLOT_51 = (SLOT_51 + (-1))
    Unknown19(1, 2, 51)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ar232_00', 30)	# 81-110	 **attackbox here**
    GFX_1('mief_maricarifin_04', 0)
    clearUponHandler(3)
    Unknown23027()
    Unknown1084(1)
    Unknown3001(10)

@State
def MarinKarin_Jizoku():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown23067('mief_marinjizoku_00')
        Unknown3032()
    sprite('null', 1200)	# 1-1200
    sprite('null', 10)	# 1201-1210
    Unknown3004(-26)

@State
def Tentarafu_dmy():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Unknown11033(2)
        Damage(300)
        AttackP1(70)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(0)
        AirHitstunAnimation(4)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown9021(1)
        Unknown9266(9)
        Unknown11068(1)
        Unknown11066(1)
        Unknown11044(1)
        Unknown11069('Tentarafu_dmy')
        Unknown3032()
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(1)
        Unknown4061(3)
        Unknown3001(150)
        Unknown3038(1)
        Unknown2073(1)

        def upon_43():
            if (SLOT_48 == 4032):
                clearUponHandler(43)
                sendToLabel(9)

        def upon_77():
            Unknown23027()

        def upon_78():
            clearUponHandler(78)
            PushbackX(0)
            Unknown11064(1)
            Unknown9250(100)
            Unknown9262(120)
            Unknown9154(80)
            SLOT_0 = 1
            Unknown48('020000000200000033000000190000000200000000000000')
            Unknown21015('54656e74617261666f6f00000000000000000000000000000000000000000000bf0f000000000000')
            Hitstop(0)
            sendToLabel(1)

        def upon_82():
            clearUponHandler(82)
            Unknown9215()
            Unknown11064(0)
            Unknown9250(0)
            Unknown9262(0)
            Unknown9155()
            Unknown11069('')
    sprite('vr_ar402Freeze00_dmy', 1)	# 1-1
    SFX_3('ice_fast')
    GFX_0('aref_403_ground', 100)
    RefreshMultihit()
    sprite('vr_ar402Freeze00_dmy', 2)	# 2-3
    GFX_0('aref_403_ground_C', 0)
    physicsXImpulse(68000)
    sprite('vr_ar402Freeze00_dmy', 3)	# 4-6
    SFX_3('ice_fast')
    sprite('vr_ar402Freeze00_dmy', 3)	# 7-9
    SFX_3('ice_fast')
    sprite('vr_ar402Freeze00_dmy', 2)	# 10-11
    SFX_3('ice_fast')
    Unknown26('aref_403_ground_C')
    sprite('vr_ar402Freeze00_dmy', 1)	# 12-12
    Unknown1084(1)
    sprite('vr_ar402Freeze00_dmy', 2)	# 13-14
    SFX_3('ice_fast')
    Unknown23027()
    ExitState()
    label(1)
    sprite('null', 1)	# 15-15
    SFX_3('ice_slow')
    physicsXImpulse(0)
    Unknown26('aref_403_ground_C')
    sprite('null', 59)	# 16-74
    GFX_0('aref_403_bind', -1)
    Unknown36(1)
    Unknown23151(22, 104)
    Unknown35()
    Unknown48('190000000200000033000000160000000200000053000000')
    ExitState()
    label(9)
    sprite('vr_ar402Freeze01_dmy', 6)	# 75-80
    Unknown26('aref_403_bind')
    GFX_0('aref_403_damege', -1)
    Unknown36(1)
    Unknown23151(22, 104)
    Unknown35()
    AttackLevel_(4)
    Damage(3000)
    AttackP2(80)
    AirUntechableTime(45)
    AirPushbackY(38000)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    Unknown9250(0)
    Unknown9262(0)
    Unknown9021(1)
    Unknown9266(9)
    Unknown11064(0)
    Unknown11068(0)
    Unknown11066(0)
    Unknown11044(0)
    Unknown30048(1)
    Unknown11069('')
    SLOT_83 = SLOT_51
    Unknown3038(1)
    RefreshMultihit()
    Unknown21015('54656e74617261666f6f00000000000000000000000000000000000000000000c10f000000000000')

@State
def aref_403_hand():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    Unknown1096(1300)
    Unknown1007(35000)
    teleportRelativeX(-20000)
    GFX_2('aref_403_hand')

@State
def aref_403_ground():

    def upon_IMMEDIATE():
        teleportRelativeX(110000)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767
    GFX_1('aref_403_ground', 100)

@State
def aref_403_ground_C():

    def upon_IMMEDIATE():
        teleportRelativeX(200000)
        physicsXImpulse(75000)
        Unknown4010(2)
    label(0)
    sprite('null', 2)	# 1-2
    GFX_1('aref_403_ground', 100)
    gotoLabel(0)

@State
def aref_403_bind():

    def upon_IMMEDIATE():
        pass
    sprite('null', 60)	# 1-60
    GFX_1('aref_403_ground', 100)
    GFX_2('aref_403_bind')

@State
def aref_403_damege():

    def upon_IMMEDIATE():
        pass
    sprite('null', 60)	# 1-60
    GFX_1('aref_403_damege', 100)

@State
def IceMiller_Shot():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        AttackP2(85)
        AirUntechableTime(60)
        Hitstop(6)
        AirPushbackX(3500)
        AirPushbackY(15000)
        PushbackX(1000)
        YImpluseBeforeWallbounce(1500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9021(1)
        Unknown9266(9)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11032('f049020010b6fdff40420f00c0bdf0ff')
        Unknown2053(1)
        Unknown3038(1)
        Unknown23020(2000)
        Unknown23021(2000)

        def upon_19():
            Unknown23022(1)
            Unknown23090(25)

        def upon_14():
            Unknown1017()
            sendToLabel(2)
        loopRelated(17, 1000)

        def upon_17():
            sendToLabel(1)
        Unknown23089('0300000001000000010000000100000001000000000000000300000000000000')
        sendToLabelUpon(54, 1)
        Unknown3032()
        teleportRelativeX(200000)
        SFX_3('ice_fast')
        SFX_3('distortion_b')

        def upon_43():
            if (SLOT_48 == 4021):
                clearUponHandler(43)
                Unknown23090(25)
        GFX_0('Icemirrorstart_Yugami', 100)
        GFX_0('450icemirrorstart', 100)
    sprite('vr_ar402_00', 12)	# 1-12	 **attackbox here**
    StartMultihit()
    Unknown23022(1)
    sprite('vr_ar402_00', 4)	# 13-16	 **attackbox here**
    StartMultihit()
    Unknown23022(0)
    SFX_3('ice_fast')
    Unknown4003('617265663430325f6963656d6972726f722e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23067('mief_402icemirror')
    Unknown4015()
    sprite('vr_ar402_00', 1)	# 17-17	 **attackbox here**
    StartMultihit()
    physicsXImpulse(2500)
    label(0)
    sprite('vr_ar402_00', 10)	# 18-27	 **attackbox here**
    RefreshMultihit()
    Unknown1019(95)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 36)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('vr_ar402_00', 10)	# 28-37	 **attackbox here**
    physicsXImpulse(-10000)
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 36)
    if SLOT_0:
        _gotolabel(1)

    def upon_3():
        Unknown1019(80)
    sprite('vr_ar402_00', 10)	# 38-47	 **attackbox here**
    SLOT_51 = (SLOT_51 + 1)
    (SLOT_51 >= 36)
    if SLOT_0:
        _gotolabel(1)
    loopRest()
    clearUponHandler(3)
    Unknown1018()
    Unknown1019(50)
    if (SLOT_12 < 300):
        SLOT_12 = 300
    gotoLabel(0)
    label(1)
    clearUponHandler(17)
    clearUponHandler(14)
    clearUponHandler(19)
    clearUponHandler(43)
    clearUponHandler(3)
    sprite('vr_ar402_00', 1)	# 48-48	 **attackbox here**
    Unknown1084(1)
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-70)
    GFX_0('450icemirrorbreak', 100)

@State
def __450icemirrorstart():

    def upon_IMMEDIATE():
        Unknown4003('617265663430325f6963656d6972726f7273746172742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown4015()
        Unknown4010(2)
        Unknown3001(0)
    sprite('null', 13)	# 1-13
    Unknown3004(20)
    sprite('null', 5)	# 14-18
    Unknown23119(-16730881, 5, 1)
    Unknown3004(-60)

@State
def Icemirrorstart_Yugami():

    def upon_IMMEDIATE():
        Unknown1096(600)
        Unknown1007(270000)
    sprite('vr_mi402_yugami', 1)	# 1-1
    GFX_1('mief_402start', 100)
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(35000)
    sprite('keep', 25)	# 2-26
    Unknown1059(140)
    Unknown1067(140)
    Unknown3004(-13)
    loopRest()

@State
def __450icemirrorbreak():

    def upon_IMMEDIATE():
        Unknown4003('617265663430325f6963656d6972726f72627265616b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(4)
        Unknown3032()
        Unknown1096(800)
    sprite('null', 10)	# 1-10
    SFX_3('ice_fast')
    SFX_3('ice_fast')
    sprite('null', 8)	# 11-18
    Unknown3004(-35)

@State
def RenzokuSlash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('mief_430slash_03')
    sprite('null', 25)	# 1-25
    GFX_0('RenzokuSlashThunder', 100)
    GFX_0('RenzokuSlashAdd', 100)
    sprite('null', 10)	# 26-35
    Unknown3004(-26)

@State
def RenzokuSlashAdd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(150)
    sprite('null', 25)	# 1-25
    sprite('null', 10)	# 26-35
    Unknown3004(-26)

@State
def RenzokuSlashThunder():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 10)	# 1-10
    Unknown3001(0)
    sprite('null', 2)	# 11-12
    Unknown3001(150)
    sprite('null', 2)	# 13-14
    Unknown3001(0)
    sprite('null', 2)	# 15-16
    Unknown3001(150)
    sprite('null', 2)	# 17-18
    Unknown3001(0)
    sprite('null', 2)	# 19-20
    Unknown3001(150)

@State
def RenzokuTsukiA():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1056(400)
    sprite('null', 10)	# 1-10
    Unknown1059(10)
    sprite('null', 5)	# 11-15
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1073(-15000)
        Unknown1056(300)
    sprite('null', 10)	# 1-10
    Unknown1059(20)
    sprite('null', 5)	# 11-15
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1073(28000)
        Unknown1056(400)
    sprite('null', 10)	# 1-10
    Unknown1059(20)
    sprite('null', 5)	# 11-15
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1073(28000)
        Unknown1056(300)
    sprite('null', 10)	# 1-10
    Unknown1059(20)
    sprite('null', 5)	# 11-15
    Unknown1067(-180)
    Unknown3004(-26)

@State
def RenzokuTsukiE():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(0)
        Unknown23122(55)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('617265663433305f736c6173685f30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1073(-15000)
        Unknown1056(500)
    sprite('null', 10)	# 1-10
    Unknown1059(20)
    sprite('null', 5)	# 11-15
    Unknown1067(-180)
    Unknown3004(-26)

@State
def aref_431C():

    def upon_IMMEDIATE():
        Unknown4003('617265663433315f626967696365332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        Unknown3001(0)
        Unknown1072(5000)
        teleportRelativeX(8000)
        Unknown2054(1)
        Unknown1096(1200)
    sprite('null', 6)	# 1-6
    ScreenShake(6000, 6000)
    GFX_1('aref_431ice', 100)
    GFX_0('431ice1', 100)
    Unknown36(1)
    Unknown1072(5000)
    Unknown35()
    SFX_3('quake_l')
    sprite('null', 6)	# 7-12
    GFX_0('431ice2', 100)
    Unknown36(1)
    Unknown1072(5000)
    Unknown35()
    SFX_3('ice_fast')
    SFX_3('mi000')
    sprite('null', 20)	# 13-32
    GFX_0('431ice_subeffC', 100)
    ScreenShake(28000, 28000)
    Unknown3004(120)
    SFX_3('mi001')
    sprite('null', 15)	# 33-47
    Unknown23119(-6915876, 15, 1)
    sprite('null', 6)	# 48-53
    GFX_0('431icebreakC', 100)
    ScreenShake(15000, 15000)
    Unknown1099(15)
    Unknown3004(-50)

@State
def aref_431_colC():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(5500)
        AttackP2(60)
        Unknown11091(33)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1100)
    sprite('null', 14)	# 1-14
    sprite('vr_ar431_02', 10)	# 15-24	 **attackbox here**
    RefreshMultihit()

@State
def aref_431_colC_DSD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1100)
    sprite('null', 14)	# 1-14
    sprite('vr_ar431_02', 10)	# 15-24	 **attackbox here**
    RefreshMultihit()

@State
def aref_431CD():

    def upon_IMMEDIATE():
        Unknown4003('617265663433315f626967696365332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        Unknown3001(0)
        Unknown1072(10000)
        teleportRelativeX(8000)
        Unknown2054(1)
        Unknown1096(1800)
    sprite('null', 6)	# 1-6
    ScreenShake(6000, 6000)
    GFX_1('aref_431ice', 100)
    GFX_0('431ice1', 100)
    Unknown36(1)
    Unknown1072(10000)
    Unknown35()
    SFX_3('quake_l')
    sprite('null', 6)	# 7-12
    GFX_0('431ice2', 100)
    Unknown36(1)
    Unknown1072(10000)
    Unknown35()
    SFX_3('ice_fast')
    SFX_3('mi000')
    sprite('null', 20)	# 13-32
    GFX_0('431ice_subeffCD', 100)
    ScreenShake(28000, 28000)
    Unknown3004(120)
    SFX_3('mi001')
    sprite('null', 15)	# 33-47
    Unknown23119(-6915876, 15, 1)
    sprite('null', 6)	# 48-53
    GFX_0('431icebreakCD', 100)
    ScreenShake(15000, 15000)
    Unknown1099(15)
    Unknown3004(-50)

@State
def aref_431_colCD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(6500)
        AttackP2(60)
        Unknown11091(31)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1700)
    sprite('null', 14)	# 1-14
    sprite('vr_ar431_02ex', 10)	# 15-24	 **attackbox here**
    RefreshMultihit()

@State
def aref_431_colCD_DSD():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackX(18000)
        AirPushbackY(60000)
        AirUntechableTime(90)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9021(1)
        Unknown9266(9)
        Unknown4007(2)
        Unknown4061(3)
        Unknown3032()
        Unknown2019(1000)
        Unknown2054(1)
        teleportRelativeX(200000)
        Unknown1007(-128000)
        Unknown3001(0)
        Unknown1096(1700)
    sprite('null', 14)	# 1-14
    sprite('vr_ar431_02ex', 10)	# 15-24	 **attackbox here**
    RefreshMultihit()

@State
def __431ice1():

    def upon_IMMEDIATE():
        Unknown4003('617265663433315f626967696365312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(128000)
        Unknown2054(1)
    sprite('null', 7)	# 1-7
    sprite('null', 2)	# 8-9
    Unknown3004(-130)

@State
def __431ice2():

    def upon_IMMEDIATE():
        Unknown4003('617265663433315f626967696365322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(128000)
        Unknown2054(1)
    sprite('null', 10)	# 1-10
    sprite('null', 5)	# 11-15
    Unknown3004(-80)

@State
def __431ice_subeffC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('aref_431icefin')
        Unknown1072(45000)
        teleportRelativeX(-150000)
        Unknown2054(1)
    sprite('null', 35)	# 1-35
    sprite('null', 5)	# 36-40
    Unknown3004(-51)

@State
def __431icebreakC():

    def upon_IMMEDIATE():
        Unknown4003('617265663433315f696365627265616b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(60000)
        Unknown1007(30000)
        Unknown1072(5000)
        Unknown23119(-8231736, 3, 1)
        Unknown1096(1200)
    sprite('null', 2)	# 1-2
    GFX_0('431icebreakeffC', 100)
    SFX_3('ice_fast')
    sprite('null', 3)	# 3-5
    SFX_3('ice_fast')
    sprite('null', 10)	# 6-15
    SFX_3('down_water_m')
    sprite('null', 8)	# 16-23
    Unknown3004(-40)

@State
def __431icebreakeffC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('mief_431icebreak')
        teleportRelativeX(180000)
        Unknown1007(280000)
        Unknown1096(1200)
    sprite('null', 55)	# 1-55
    sprite('null', 5)	# 56-60
    Unknown3004(-51)

@State
def __431ice_subeffCD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('aref_431icefin')
        Unknown1072(50000)
        teleportRelativeX(-150000)
        Unknown2054(1)
    sprite('null', 35)	# 1-35
    sprite('null', 5)	# 36-40
    Unknown3004(-51)

@State
def __431icebreakCD():

    def upon_IMMEDIATE():
        Unknown4003('617265663433315f696365627265616b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(13)
        Unknown3032()
        teleportRelativeX(75000)
        Unknown1007(30000)
        Unknown1072(15000)
        Unknown23119(-8231736, 3, 1)
        Unknown1096(1800)
    sprite('null', 2)	# 1-2
    GFX_0('431icebreakeffCD', 100)
    SFX_3('ice_fast')
    sprite('null', 3)	# 3-5
    SFX_3('ice_fast')
    sprite('null', 10)	# 6-15
    SFX_3('down_water_m')
    sprite('null', 8)	# 16-23
    Unknown3004(-40)

@State
def __431icebreakeffCD():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('mief_431icebreak')
        teleportRelativeX(430000)
        Unknown1007(280000)
        Unknown1096(1400)
    sprite('null', 55)	# 1-55
    sprite('null', 5)	# 56-60
    Unknown3004(-51)

@State
def PMI_PersonaIchigeki1():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000003004feff0000000000000000000000000000000000000000')
        callSubroutine('PMI_DDAttackInit')
        callSubroutine('PMI_CheckWarp')
        Unknown4007(3)
        Unknown2054(1)
        Unknown3032()
        Unknown23022(1)
    sprite('ar432_20', 3)	# 1-3
    GFX_0('450Personaineff', 100)
    sprite('ar432_21', 3)	# 4-6
    sprite('ar432_22', 3)	# 7-9
    sprite('ar432_21', 3)	# 10-12
    sprite('ar432_20', 3)	# 13-15
    sprite('ar432_21', 3)	# 16-18
    sprite('ar432_22', 3)	# 19-21
    sprite('ar432_21', 3)	# 22-24
    sprite('ar432_20', 3)	# 25-27
    sprite('ar432_21', 3)	# 28-30
    sprite('ar432_22', 3)	# 31-33
    sprite('ar432_21', 3)	# 34-36
    sprite('ar432_20', 3)	# 37-39
    sprite('ar432_21', 3)	# 40-42
    sprite('ar432_22', 3)	# 43-45
    Unknown23119(-1002241, 10, 1)
    sprite('ar432_21', 8)	# 46-53
    enterState('PersonaDeleteAndIdling')
    physicsYImpulse(12000)
    Unknown3004(-35)
    sprite('keep', 32767)	# 54-32820
    enterState('PersonaDeleteAndIdling')

@State
def __450Personaineff():

    def upon_IMMEDIATE():
        GFX_2('aref_450personain')
        Unknown2054(1)
        Unknown3001(0)
        Unknown3004(40)
    sprite('null', 55)	# 1-55
    sprite('null', 7)	# 56-62
    Unknown1099(300)
    Unknown3004(-40)

@State
def Ichigeki_Whip():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(0)
        AttackLevel_(5)
        Hitstop(7)
        Unknown11001(0, 30, 0)
        GroundedHitstunAnimation(1)
        AirPushbackX(-10000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(999)
        Unknown11033(3)
        Unknown11031(0)
        Unknown11042(1)
        Unknown48('190000000200000053000000160000000200000053000000')
        teleportRelativeX(-150000)
        Unknown48('190000000200000017000000160000000200000017000000')
        Unknown1007(1350000)
        Unknown1072(80000)
        Unknown1110(100000, 0)
        SLOT_12 = SLOT_19
        Unknown1019(5)
        SLOT_13 = SLOT_20
        SLOT_13 = (SLOT_13 * (-1))
        YAccel(5)
        Unknown1108(0)
        Unknown2035(1)
        sendToLabelUpon(12, 1)

        def upon_11():
            clearUponHandler(11)
            physicsXImpulse(0)
            physicsYImpulse(0)
    sprite('vr_ar450_00', 1)	# 1-1
    SFX_3('slash_pole_middle')
    sprite('vr_mi450_dummy', 3)	# 2-4	 **attackbox here**
    Unknown1110(120000, 0)
    GFX_0('450muchi', 0)
    RefreshMultihit()
    sprite('vr_ar450_00', 3)	# 5-7
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000008a13000000000000')
    Unknown26('450muchi')
    Unknown23027()
    sprite('vr_ar450_03', 1)	# 8-8
    Unknown1110(-94000, 0)
    SFX_3('highjump_l')
    sprite('vr_ar450_02', 11)	# 9-19
    Unknown3004(-30)
    loopRest()
    ExitState()
    label(1)
    clearUponHandler(11)
    clearUponHandler(12)
    sprite('vr_mi450_dummy', 30)	# 20-49	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown3029(1)
    Unknown3070(1)
    Unknown3071(3)
    Unknown3074('00000000000000007f000000ff000000')
    Unknown3075('00000000000000000000000000000000')
    GFX_0('450upline', -1)
    sprite('vr_ar450_00', 3)	# 50-52
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000008913000000000000')
    sprite('vr_ar450_03', 1)	# 53-53
    Unknown1110(-94000, 0)
    SFX_3('highjump_l')
    sprite('vr_ar450_02', 11)	# 54-64
    Unknown3004(-30)
    Unknown1084(1)

@State
def PMI_PersonaIchigeki2():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PMI_DDAttackInit')
        Unknown2012()
        AirPushbackX(0)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(0)
        Hitstop(0)
        AirUntechableTime(999)
        Unknown11064(1)
        Unknown9266(9)
        Unknown11023(1)
        Unknown23022(1)
        Unknown3032()
        Unknown1000(0)
        teleportRelativeY(2000000)
        callSubroutine('PMI_CheckWarp')
    label(0)
    sprite('ar450_00', 20)	# 1-20
    sprite('ar450_00', 3)	# 21-23
    sprite('ar450_01', 3)	# 24-26
    sprite('ar450_02', 3)	# 27-29
    sprite('ar450_01', 3)	# 30-32
    sprite('ar450_00', 3)	# 33-35
    sprite('ar450_01', 3)	# 36-38
    sprite('ar450_02', 3)	# 39-41
    sprite('ar450_01', 3)	# 42-44
    sprite('ar450_00', 3)	# 45-47
    sprite('ar450_01', 3)	# 48-50
    SFX_3('slash_knife_fast')
    sprite('ar450_02', 3)	# 51-53
    SFX_3('slash_pole_middle')
    label(1)
    sprite('ar450_03', 2)	# 54-55
    sprite('ar450_04', 2)	# 56-57	 **attackbox here**
    Unknown4045('617265665f3435307a616e430000000000000000000000000000000000000000ffffffff')
    GFX_0('450icebase_lv1', -1)
    Unknown36(1)
    Unknown1096(800)
    Unknown35()
    ScreenShake(12000, 12000)
    RefreshMultihit()
    SFX_3('ice_break_fast')
    sprite('ar450_05', 2)	# 58-59
    sprite('ar450_06', 3)	# 60-62
    sprite('ar450_07', 3)	# 63-65
    sprite('ar450_08', 4)	# 66-69
    Unknown3004(-8)
    sprite('ar450_09', 4)	# 70-73
    sprite('ar450_10', 4)	# 74-77
    GFX_0('Ichigeki_Ranbu', -1)
    Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000009613000000000000')
    label(2)
    sprite('ar450_08', 6)	# 78-83
    SLOT_52 = (SLOT_52 + 1)
    sprite('ar450_09', 6)	# 84-89
    sprite('ar450_10', 6)	# 90-95
    Unknown3038(1)
    (SLOT_52 == 20)
    Unknown19(2, 2, 0)
    sprite('keep', 32767)	# 96-32862
    enterState('PersonaDeleteAndIdling')

@State
def Ichigeki_Ranbu():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(0)
        AttackLevel_(5)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(999)
        Unknown11023(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23022(1)
        Unknown11083(1)
    sprite('dmy_atk00', 20)	# 1-20
    Unknown4045('617265665f3435307a616e44000000000000000000000000000000000000000064000000')
    ScreenShake(12000, 12000)
    GFX_0('450icebase', 100)
    GFX_0('Ichigeki_RanbuSE', 100)
    Unknown21015('4963686967656b695f52616e62755345000000000000000000000000000000009d13000000000000')
    SLOT_51 = 15
    label(0)
    sprite('dmy_atk00', 6)	# 21-26
    Unknown4045('617265665f3435307a616e43000000000000000000000000000000000000000064000000')
    RefreshMultihit()
    Unknown23151(22, 105)
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(10, 2, 51)
    gotoLabel(0)
    label(10)
    SLOT_51 = 15
    label(11)
    sprite('dmy_atk00', 4)	# 27-30
    Unknown4045('617265665f3435307a616e44000000000000000000000000000000000000000064000000')
    RefreshMultihit()
    Unknown23151(22, 105)
    SLOT_51 = (SLOT_51 + (-1))
    Unknown21015('4963686967656b695f52616e62755345000000000000000000000000000000009e13000000000000')
    loopRest()
    Unknown19(20, 2, 51)
    gotoLabel(11)
    label(20)
    SLOT_51 = 30
    label(21)
    sprite('dmy_atk00', 2)	# 31-32
    Unknown4045('617265665f3435307a616e44000000000000000000000000000000000000000064000000')
    RefreshMultihit()
    Unknown23151(22, 105)
    SLOT_51 = (SLOT_51 + (-1))
    Unknown21015('4963686967656b695f52616e62755345000000000000000000000000000000009f13000000000000')
    loopRest()
    Unknown19(1, 2, 51)
    gotoLabel(21)
    label(1)
    sprite('dmy_atk00', 1)	# 33-33
    Unknown4045('617265665f3435307a616e45000000000000000000000000000000000000000064000000')
    RefreshMultihit()
    sprite('null', 5)	# 34-38
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000008c13000000000000')

@State
def Ichigeki_RanbuSE():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5021):
                if (not SLOT_52):
                    sendToLabel(1)
            if (SLOT_48 == 5022):
                if (not SLOT_53):
                    sendToLabel(2)
            if (SLOT_48 == 5023):
                if (not SLOT_54):
                    sendToLabel(3)
            if (SLOT_48 == 5024):
                sendToLabel(9)
    label(1)
    sprite('keep', 3)	# 1-3
    SLOT_52 = 1
    SFX_3('slash_pole_middle')
    sprite('keep', 15)	# 4-18
    SFX_3('damage_magic_m')
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('keep', 3)	# 19-21
    SLOT_53 = 1
    SFX_3('slash_pole_middle')
    sprite('keep', 10)	# 22-31
    SFX_3('damage_magic_m')
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('keep', 3)	# 32-34
    SLOT_54 = 1
    SFX_3('slash_pole_middle')
    sprite('keep', 5)	# 35-39
    SFX_3('damage_magic_m')
    loopRest()
    gotoLabel(3)
    label(9)
    sprite('keep', 10)	# 40-49

@State
def IchigekiCamera():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 5011):
                sendToLabel(1)
            if (SLOT_48 == 5012):
                sendToLabel(2)
            if (SLOT_48 == 5013):
                sendToLabel(3)
            if (SLOT_48 == 5014):
                sendToLabel(4)
            if (SLOT_48 == 5015):
                sendToLabel(5)
    label(1)
    sprite('keep', 32767)	# 1-32767
    Unknown1086(22)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(2)
    sprite('keep', 20)	# 32768-32787
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('keep', 30)	# 32788-32817
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown4004('534345465f4c6976655279756861694e616e616d65000000000000000000000064000000')
    Unknown1086(22)
    Unknown20001(1)
    Unknown1007(300000)
    physicsXImpulse(0)
    physicsYImpulse(10000)
    sprite('keep', 20)	# 32818-32837
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown21015('41737472616c48656174000000000000000000000000000000000000000000008b13000000000000')
    label(3)
    sprite('keep', 20)	# 32838-32857
    sprite('keep', 20)	# 32858-32877
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown4004('534345465f4c6976655279756861694e616e616d65000000000000000000000064000000')
    Unknown1086(28)
    Unknown1084(1)
    teleportRelativeY(2120000)
    teleportRelativeX(198000)
    sprite('keep', 32767)	# 32878-65644
    GFX_0('450Circlebg', -1)
    Unknown26('SCEF_LiveRyuhaiNaname')
    Unknown26('subSCEF_LiveRyuhaiUpper2naname')
    label(4)
    sprite('keep', 32767)	# 65645-98411
    Unknown1086(22)
    Unknown20000(1)
    teleportRelativeY(2120000)
    label(5)
    sprite('keep', 20)	# 98412-98431
    Unknown26('SCEF_LiveRyuhaiNaname')
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('keep', 32767)	# 98432-131198
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown1086(0)
    Unknown20000(1)
    Unknown1000(0)
    teleportRelativeY(0)

@State
def __450muchi():

    def upon_IMMEDIATE():
        Unknown23067('aref_450muchi')
        Unknown4007(2)
        Unknown1072(-9000)
    sprite('null', 30)	# 1-30
    sprite('null', 10)	# 31-40
    Unknown1059(200)
    Unknown1067(400)
    Unknown3004(-26)

@State
def __450upline():

    def upon_IMMEDIATE():
        Unknown1072(-10000)
    sprite('null', 30)	# 1-30
    Unknown23067('mief_450upline00')

@State
def __450icebase():

    def upon_IMMEDIATE():
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 20)	# 1-20
    GFX_0('450icemove1', 100)
    sprite('null', 30)	# 21-50
    GFX_0('450icebase_lv1', 100)
    ScreenShake(6000, 6000)
    sprite('null', 20)	# 51-70
    GFX_0('450icemove1', 100)
    sprite('null', 25)	# 71-95
    GFX_0('450icebase_lv2', 100)
    ScreenShake(8000, 8000)
    sprite('null', 20)	# 96-115
    GFX_0('450icemove1', 100)
    sprite('null', 20)	# 116-135
    GFX_0('450icebase_lv3', 100)
    ScreenShake(12000, 12000)
    sprite('null', 15)	# 136-150
    GFX_0('450icemove2', 100)
    sprite('null', 15)	# 151-165
    GFX_0('450icebase_lv4', 100)
    ScreenShake(16000, 16000)
    sprite('null', 15)	# 166-180
    GFX_0('450icemove2', 100)
    sprite('null', 20)	# 181-200
    GFX_0('450icebase_lv5', 100)
    ScreenShake(24000, 24000)
    sprite('null', 20)	# 201-220
    ScreenShake(24000, 24000)
    sprite('null', 20)	# 221-240
    ScreenShake(24000, 24000)
    sprite('null', 20)	# 241-260
    ScreenShake(24000, 24000)
    sprite('null', 32767)	# 261-33027

@State
def __450icebase_lv1():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f696365626173655f6c76312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)	# 1-58
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)	# 59-60
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv2():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f696365626173655f6c76322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)	# 1-58
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)	# 59-60
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv3():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f696365626173655f6c76332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)	# 1-58
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)	# 59-60
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv4():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f696365626173655f6c76342e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4054(1)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 58)	# 1-58
    GFX_1('aref_450icestay', 100)
    sprite('null', 2)	# 59-60
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-130)

@State
def __450icebase_lv5():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f696365626173655f6c76352e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4054(1)
        Unknown1096(1300)
        Unknown3032()
        Unknown4015()
        Unknown23151(22, 103)
        Unknown1007(75000)
    sprite('null', 55)	# 1-55
    GFX_1('aref_450icestay', 100)
    sprite('null', 100)	# 56-155
    sprite('null', 5)	# 156-160
    Unknown23119(-16776961, 5, 1)
    Unknown3004(-90)

@State
def __450icemove1():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f6963656d6f7665312e444947000000000000000000000000617265663435305f6963656d6f7665315f3030302e6d6d6f7400000000000000')
        Unknown4054(1)
        Unknown3032()
    sprite('null', 17)	# 1-17
    GFX_1('aref_450icesmoke', 100)
    sprite('null', 3)	# 18-20
    Unknown23119(-16744193, 8, 1)
    SFX_3('mi000')
    Unknown3004(-90)

@State
def __450icemove2():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f6963656d6f7665322e444947000000000000000000000000617265663435305f6963656d6f7665325f3030302e6d6d6f7400000000000000')
        Unknown4054(1)
        Unknown3032()
    sprite('null', 12)	# 1-12
    GFX_1('aref_450icesmoke', 100)
    sprite('null', 3)	# 13-15
    Unknown23119(-16744193, 8, 1)
    SFX_3('mi000')
    Unknown3004(-90)

@State
def __450icebreak():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f696365626173655f6c76352e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4054(1)
        Unknown1096(1100)
        teleportRelativeX(500000)
        Unknown1007(500000)
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 5031):
                sendToLabel(0)
    sprite('null', 32767)	# 1-32767
    GFX_1('aref_450icestay2', 100)
    label(0)
    sprite('null', 2)	# 32768-32769
    GFX_1('mief_450icebreak', 100)
    Unknown23119(-1, 20, 1)
    Unknown3004(-13)
    SFX_3('damage_hit_mh')
    sprite('null', 2)	# 32770-32771
    SFX_3('ice_break_fast')
    sprite('null', 16)	# 32772-32787
    SFX_3('ice_break_fast')

@State
def __450Circlebg():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('617265663435305f636972636c6562672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3001(0)
        Unknown1007(-200000)
    sprite('null', 32767)	# 1-32767
    Unknown3004(30)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3032()
        Unknown6001(1)
        Unknown1001(640000)
        teleportRelativeX(180000)
        teleportRelativeY(100000)
        Unknown3001(0)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('ichigeki', 12)	# 1-12	 **attackbox here**
    physicsXImpulse(80000)
    Unknown3004(10)
    sprite('ichigeki', 80)	# 13-92	 **attackbox here**
    physicsXImpulse(200)
    sprite('ichigeki', 20)	# 93-112	 **attackbox here**
    Unknown23119(10198015, 20, 1)
    sprite('ichigeki', 30)	# 113-142	 **attackbox here**
    Unknown3004(-9)

@State
def __450cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('6d6965663435305f637574696e62672e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 110)	# 1-110
    Unknown3004(30)
    sprite('null', 50)	# 111-160
    Unknown3004(-6)

@State
def Issen():

    def upon_IMMEDIATE():
        Unknown4003('617265663435305f697373656e2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown23015(1)
        Unknown4015()
        Unknown1096(1500)
    sprite('null', 7)	# 1-7
    sprite('null', 5)	# 8-12
    Unknown3004(-60)

@State
def __450KObg():

    def upon_IMMEDIATE():
        Unknown23067('mief_450bg')
        Unknown4003('617265663435305f62672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
    sprite('null', 32767)	# 1-32767
    Unknown3004(30)

@State
def LifeLinkEff():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 1)	# 1-1
    Unknown4045('6e7465665f73746f72795f6c6966656c696e6b6566665f6c696e653200000000ffffffff')

@State
def PMI_PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100204e0000a0860100204e0000a0860100204e0000')
        callSubroutine('PersonaReset')
        Unknown23022(1)
        Unknown4007(3)
        callSubroutine('PMI_CheckWarp')
    sprite('ar610_00', 6)	# 1-6
    sprite('ar610_01', 6)	# 7-12
    sprite('ar610_02', 6)	# 13-18
    sprite('ar610_00', 6)	# 19-24
    sprite('ar610_01', 6)	# 25-30
    sprite('ar610_02', 6)	# 31-36
    sprite('ar610_03', 6)	# 37-42
    sprite('ar610_04', 6)	# 43-48
    sprite('ar610_05', 6)	# 49-54
    sprite('ar610_06', 6)	# 55-60
    sprite('ar610_07', 6)	# 61-66
    label(0)
    sprite('ar610_08', 6)	# 67-72
    SFX_3('cloth_l')
    sprite('ar610_09', 6)	# 73-78
    sprite('ar610_10', 6)	# 79-84
    gotoLabel(0)

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
def rimzineHontaiA():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(6)
        teleportRelativeY(40000)
        teleportRelativeX(-1525000)
        Unknown2019(1000)
        Unknown13044(1)
        Unknown23069(1)
        Unknown2047(1)
        Unknown4010(3)
    sprite('vr_mi601b_00', 110)	# 1-110
    physicsXImpulse(24900)
    GFX_0('rimzineHontaiB', 100)
    GFX_0('rimzineHontaiC', 100)
    GFX_0('rimzineDoor', 100)
    GFX_0('rimzinetaiya', 0)
    SFX_3('mi002')
    sprite('vr_mi601b_00', 10)	# 111-120
    physicsXImpulse(12400)
    sprite('vr_mi601b_00', 10)	# 121-130
    physicsXImpulse(6200)
    SFX_3('mi003')
    sprite('vr_mi601b_00', 10)	# 131-140
    physicsXImpulse(3100)
    sprite('vr_mi601b_00', 130)	# 141-270
    physicsXImpulse(0)
    sprite('vr_mi601b_00', 10)	# 271-280
    physicsXImpulse(3100)
    SFX_3('mi002')
    sprite('vr_mi601b_00', 10)	# 281-290
    physicsXImpulse(6200)
    sprite('vr_mi601b_00', 10)	# 291-300
    physicsXImpulse(12400)
    sprite('vr_mi601b_00', 100)	# 301-400
    physicsXImpulse(24900)

@State
def rimzineHontaiB():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(1000)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601b_01', 32767)	# 1-32767

@State
def rimzineHontaiC():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(0)
        Unknown2019(1000)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601b_02', 110)	# 1-110
    GFX_0('rimzinetaiya2', 0)
    sprite('vr_mi601b_02', 32767)	# 111-32877

@State
def rimzineDoor():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(500)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601a_00', 150)	# 1-150
    sprite('vr_mi601a_01', 4)	# 151-154
    sprite('vr_mi601a_02', 4)	# 155-158
    sprite('vr_mi601a_03', 4)	# 159-162
    sprite('vr_mi601a_04', 45)	# 163-207
    sprite('null', 300)	# 208-507
    Unknown3001(0)
    GFX_0('rimzineDoor2', 100)

@State
def rimzineDoor2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown2019(1000)
        Unknown13044(1)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601a_03', 4)	# 1-4
    sprite('vr_mi601a_02', 4)	# 5-8
    sprite('vr_mi601a_01', 4)	# 9-12
    sprite('vr_mi601a_00', 300)	# 13-312

@State
def rimzinetaiya():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(500)
        Unknown23069(1)
        Unknown2047(1)
    label(0)
    sprite('vr_mi601c_02', 2)	# 1-2
    sprite('vr_mi601c_01', 2)	# 3-4
    sprite('vr_mi601c_00', 2)	# 5-6
    gotoLabel(0)

@State
def rimzinetaiya2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4061(6)
        Unknown13044(1)
        Unknown2019(500)
        Unknown23069(1)
        Unknown2047(1)
    sprite('vr_mi601c_02', 4)	# 1-4
    sprite('vr_mi601c_01', 4)	# 5-8
    sprite('vr_mi601c_00', 4)	# 9-12
    sprite('vr_mi601c_02', 4)	# 13-16
    sprite('vr_mi601c_01', 4)	# 17-20
    sprite('vr_mi601c_00', 4)	# 21-24
    sprite('vr_mi601c_02', 4)	# 25-28
    sprite('vr_mi601c_01', 4)	# 29-32
    sprite('vr_mi601c_00', 4)	# 33-36
    sprite('vr_mi601c_02', 4)	# 37-40
    sprite('vr_mi601c_01', 4)	# 41-44
    sprite('vr_mi601c_00', 4)	# 45-48
    sprite('vr_mi601c_02', 4)	# 49-52
    sprite('vr_mi601c_01', 4)	# 53-56
    sprite('vr_mi601c_00', 4)	# 57-60
    sprite('vr_mi601c_02', 4)	# 61-64
    sprite('vr_mi601c_01', 4)	# 65-68
    sprite('vr_mi601c_00', 4)	# 69-72
    sprite('vr_mi601c_02', 4)	# 73-76
    sprite('vr_mi601c_01', 4)	# 77-80
    sprite('vr_mi601c_00', 4)	# 81-84
    sprite('vr_mi601c_02', 4)	# 85-88
    sprite('vr_mi601c_01', 4)	# 89-92
    sprite('vr_mi601c_00', 4)	# 93-96
    sprite('vr_mi601c_02', 4)	# 97-100
    sprite('vr_mi601c_01', 4)	# 101-104
    sprite('vr_mi601c_00', 4)	# 105-108
    sprite('vr_mi601c_02', 4)	# 109-112
    sprite('vr_mi601c_01', 4)	# 113-116
    sprite('vr_mi601c_00', 4)	# 117-120
    sprite('vr_mi601c_02', 4)	# 121-124
    sprite('vr_mi601c_01', 4)	# 125-128
    sprite('vr_mi601c_00', 4)	# 129-132
    sprite('vr_mi601c_02', 4)	# 133-136
    sprite('vr_mi601c_01', 130)	# 137-266
    sprite('vr_mi601c_00', 4)	# 267-270
    sprite('vr_mi601c_02', 4)	# 271-274
    sprite('vr_mi601c_01', 4)	# 275-278
    sprite('vr_mi601c_00', 4)	# 279-282
    sprite('vr_mi601c_02', 3)	# 283-285
    sprite('vr_mi601c_01', 3)	# 286-288
    sprite('vr_mi601c_00', 3)	# 289-291
    sprite('vr_mi601c_02', 3)	# 292-294
    sprite('vr_mi601c_01', 3)	# 295-297
    sprite('vr_mi601c_00', 3)	# 298-300
    sprite('vr_mi601c_02', 2)	# 301-302
    sprite('vr_mi601c_01', 2)	# 303-304
    sprite('vr_mi601c_00', 2)	# 305-306
    sprite('vr_mi601c_02', 2)	# 307-308
    sprite('vr_mi601c_01', 2)	# 309-310
    sprite('vr_mi601c_00', 2)	# 311-312
    sprite('vr_mi601c_02', 2)	# 313-314
    sprite('vr_mi601c_01', 2)	# 315-316
    sprite('vr_mi601c_00', 2)	# 317-318
    sprite('vr_mi601c_02', 2)	# 319-320
    sprite('vr_mi601c_01', 2)	# 321-322
    sprite('vr_mi601c_00', 2)	# 323-324
    sprite('vr_mi601c_02', 2)	# 325-326
    sprite('vr_mi601c_01', 2)	# 327-328
    sprite('vr_mi601c_00', 2)	# 329-330
    sprite('vr_mi601c_02', 2)	# 331-332
    sprite('vr_mi601c_01', 2)	# 333-334
    sprite('vr_mi601c_00', 2)	# 335-336
    sprite('vr_mi601c_02', 2)	# 337-338
    sprite('vr_mi601c_01', 2)	# 339-340
    sprite('vr_mi601c_00', 2)	# 341-342

@State
def rimzineShadow():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(6)
        Unknown3035()
        Unknown1007(10000)
        Unknown3001(100)
    sprite('vr_mi601s_00', 260)	# 1-260

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