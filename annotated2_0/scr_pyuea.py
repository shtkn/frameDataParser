@State
def PYU_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('5059555f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PYU_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PYU_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PYU_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 101):
            Unknown23185('5059555f506572736f6e6135420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 102):
            Unknown23185('5059555f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 103):
            Unknown23185('5059555f506572736f6e6136430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 201):
            Unknown23185('5059555f506572736f6e6132420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 203):
            Unknown23185('5059555f506572736f6e6132430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 301):
            Unknown23185('5059555f506572736f6e614a420000000000000000000000000000000000000032000000')
        if (SLOT_48 == 302):
            Unknown23185('5059555f506572736f6e614a430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 4010):
            Unknown23185('5059555f506572736f6e61526576657273616c416374696f6e0000000000000064000000')
        if (SLOT_48 == 503):
            Unknown23185('5059555f506572736f6e61437275736841747461636b0000000000000000000064000000')
        if (SLOT_48 == 501):
            Unknown23185('5059555f43726173685f5275736831737400000000000000000000000000000064000000')
        if (SLOT_48 == 502):
            Unknown23185('5059555f43726173685f5275736800000000000000000000000000000000000064000000')
        if (SLOT_48 == 4020):
            Unknown23185('5059555f506572736f6e6141676941000000000000000000000000000000000064000000')
        if (SLOT_48 == 4030):
            Unknown23185('5059555f506572736f6e6141676942000000000000000000000000000000000064000000')
        if (SLOT_48 == 4040):
            Unknown23185('5059555f506572736f6e6141676943000000000000000000000000000000000064000000')
        if (SLOT_48 == 4050):
            Unknown23185('5059555f506572736f6e614d616861726167694100000000000000000000000064000000')
        if (SLOT_48 == 4060):
            Unknown23185('5059555f506572736f6e614d616861726167694200000000000000000000000064000000')
        if (SLOT_48 == 4071):
            Unknown23185('5059555f506572736f6e614d616861726167694300000000000000000000000064000000')
        if (SLOT_48 == 5010):
            Unknown23185('5059555f506572736f6e614669726541747461636b410000000000000000000064000000')
        if (SLOT_48 == 5032):
            Unknown23185('5059555f506572736f6e6141697241676941000000000000000000000000000064000000')
        if (SLOT_48 == 5033):
            Unknown23185('5059555f506572736f6e6141697241676942000000000000000000000000000064000000')
        if (SLOT_48 == 5034):
            Unknown23185('5059555f506572736f6e6141697241676943000000000000000000000000000064000000')
        if (SLOT_48 == 5020):
            Unknown23185('506572736f6e614669726541747461636b42000000000000000000000000000064000000')
        if (SLOT_48 == 5030):
            Unknown23185('5059555f506572736f6e6146697265426972640000000000000000000000000064000000')
        if (SLOT_48 == 4080):
            Unknown23185('5059555f506572736f6e6146697265426f6f737465720000000000000000000064000000')
        if (SLOT_48 == 108):
            Unknown23185('5059555f506572736f6e6135435f54414700000000000000000000000000000064000000')
        if (SLOT_48 == 4074):
            Unknown23185('506572736f6e614669726541747461636b5f544147000000000000000000000064000000')
        if (SLOT_48 == 4072):
            Unknown23185('5059555f506572736f6e614d616861726167695f54414700000000000000000064000000')
        if (SLOT_48 == 4011):
            Unknown23185('5059555f506572736f6e61526576657273616c416374696f6e5f54414700000064000000')
        if (SLOT_48 == 10010):
            Unknown23185('5059555f506572736f6e6141676964696e650000000000000000000000000000c8000000')
        if (SLOT_48 == 10020):
            Unknown23185('5059555f506572736f6e6141676964696e655f4f440000000000000000000000c8000000')
        if (SLOT_48 == 10030):
            Unknown23185('5059555f506572736f6e614d6168617261676964696e65000000000000000000c8000000')
        if (SLOT_48 == 10053):
            Unknown23185('5059555f506572736f6e614d6168617261676964696e655f4f44000000000000c8000000')
        if (SLOT_48 == 10060):
            Unknown23185('5059555f506572736f6e6141676964696e6544554f0000000000000000000000c8000000')
        if (SLOT_48 == 10061):
            Unknown23185('5059555f506572736f6e6141676964696e6544554f5f4f440000000000000000c8000000')
        if (SLOT_48 == 50):
            Unknown23185('506572736f6e61456e7472793200000000000000000000000000000000000000c8000000')
        if (SLOT_48 == 55):
            Unknown23185('506572736f6e61456e7472795f54414700000000000000000000000000000000c8000000')
        if (SLOT_48 == 51):
            Unknown23185('506572736f6e614d6174636857696e0000000000000000000000000000000000c8000000')
        if (SLOT_48 == 13):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e6700000000000000000000c8000000')
        if (SLOT_48 == 10070):
            Unknown23185('506572736f6e614963686967656b690000000000000000000000000000000000c8000000')

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
    EnableCollision(0)
    Unknown30041('')
    Unknown3031()

@Subroutine
def PYU_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PYU_AttackInit():
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
    callSubroutine('PYU_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PYU_SPAttackInit():
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
    callSubroutine('PYU_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PYU_AstralAttackInit():
    Unknown23028(6, 1)
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
    callSubroutine('PYU_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PYU_DDAttackInit():
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
    ProjectileDurabilityLvl(0)
    SLOT_11 = 120
    callSubroutine('PYU_ReceptionSignal')
    Unknown23023()

@Subroutine
def PYU_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PYU_ForceWarp():
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
    enterState('PYU_PersonaWait')

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
        callSubroutine('PYU_ReceptionSignal')
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
    EnableCollision(0)
    Unknown1084(1)

@Subroutine
def BoosterDamageUp():
    Unknown48('19000000020000003c00000003000000020000001f000000')
    if (SLOT_60 == 1):
        Unknown10000(115)
    if (SLOT_60 == 2):
        Unknown10000(125)
    if (SLOT_60 == 3):
        Unknown10000(135)
    if (SLOT_60 == 4):
        Unknown10000(150)
    if (SLOT_60 == 5):
        Unknown10000(160)
        ChipDamagePct(6)
    if (SLOT_60 == 6):
        Unknown10000(180)
        ChipDamagePct(7)
    if (SLOT_60 == 7):
        Unknown10000(190)
        ChipDamagePct(8)
    if (SLOT_60 == 8):
        Unknown10000(210)
        ChipDamagePct(9)
    if (SLOT_60 == 9):
        Unknown10000(230)
        ChipDamagePct(10)

@Subroutine
def Init_CantCancelPersonaAction():
    SLOT_10 = 1

    def upon_STATE_END():
        SLOT_10 = 0

@State
def PYU_Persona5B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0f2fcff80841e000000000000000000')
        callSubroutine('PYU_AttackInit')
        EnableCollision(1)
        AttackLevel_(3)
        Damage(200)
        AttackP1(90)
        Hitstop(1)
        AirPushbackX(11000)
        AirPushbackY(-25000)
        Unknown9310(1)
        Unknown30056('a08601003200000000000000')
        Unknown9016(1)
        Unknown11057(500)
        Unknown11092(1)
        Unknown11058('0000000001000000000000000000000000000000')

        def upon_11():
            SLOT_51 = 1
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown23078(1)
        Unknown23066(0)
        Unknown23059(1)
    sprite('ko205_00', 2)	# 1-2
    teleportRelativeY(0)
    physicsXImpulse(5000)
    physicsYImpulse(18000)
    setGravity(1800)
    Unknown2053(1)
    sprite('ko205_01', 2)	# 3-4
    sprite('ko205_00', 2)	# 5-6
    sprite('ko205_03', 3)	# 7-9
    SFX_3('slash_rapier_middle')
    sprite('ko205_04', 1)	# 10-10	 **attackbox here**
    GFX_1('koef_firewing', 0)
    RefreshMultihit()
    sprite('ko205_04', 1)	# 11-11	 **attackbox here**
    Unknown23022(0)
    RefreshMultihit()
    sprite('ko205_04', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('ko205_05', 1)	# 13-13	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    sprite('ko205_05', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('ko205_05', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('ko205_06', 1)	# 16-16	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    sprite('ko205_06', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('ko205_06', 1)	# 18-18	 **attackbox here**
    Unknown23066(1)
    RefreshMultihit()
    if SLOT_51:
        Unknown23029(2, 105, 0)
        clearUponHandler(11)
    sprite('ko205_07', 2)	# 19-20
    GFX_1('koef_firewing', 0)
    sprite('ko205_08', 2)	# 21-22
    GFX_1('koef_firewing', 0)
    sprite('ko205_09', 3)	# 23-25
    GFX_1('koef_firewing', 0)
    Unknown8000(104, 1, 1)
    sprite('ko205_10', 4)	# 26-29
    Unknown1084(1)
    GFX_1('koef_firewing', 0)
    sprite('ko205_11', 4)	# 30-33
    sprite('ko205_12', 4)	# 34-37
    sprite('ko205_11', 4)	# 38-41
    sprite('ko205_12', 4)	# 42-45
    sprite('ko205_11', 4)	# 46-49
    sprite('ko205_12', 4)	# 50-53
    sprite('ko205_11', 4)	# 54-57
    sprite('ko205_12', 4)	# 58-61
    sprite('ko205_11', 4)	# 62-65
    sprite('ko205_12', 4)	# 66-69
    label(580)
    sprite('keep', 32767)	# 70-32836
    enterState('PersonaDeleteAndIdling')

@State
def PYU_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000020a107000000000000000000')
        callSubroutine('PYU_AttackInit')
        AttackLevel_(3)
        Damage(200)
        AttackP1(90)
        Hitstop(1)
        AirUntechableTime(17)
        Unknown9016(1)
        AirPushbackX(11000)
        AirPushbackY(15000)
        Unknown11057(500)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11092(1)
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        EnableCollision(1)
        Unknown2034(1)
        Unknown2053(1)

        def upon_11():
            SLOT_51 = 1
        Unknown23078(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_19 <= 380000):
                sendToLabel(1)
        Unknown23059(1)

        def upon_STATE_END():
            Unknown2034(0)
            Unknown2053(0)
    sprite('ko206_00', 6)	# 1-6
    physicsXImpulse(17000)
    SFX_3('airdash_m')
    sprite('ko206_01', 6)	# 7-12
    physicsXImpulse(24500)
    sprite('ko206_00', 5)	# 13-17
    Unknown1019(100)
    label(1)
    sprite('ko206_01', 2)	# 18-19
    clearUponHandler(3)
    Unknown1019(60)
    sprite('ko206_00', 2)	# 20-21
    sprite('ko206_02', 2)	# 22-23
    sprite('ko206_03', 1)	# 24-24	 **attackbox here**
    sprite('ko206_03', 1)	# 25-25	 **attackbox here**
    GFX_1('koef_firewing', 0)
    RefreshMultihit()
    Unknown1019(20)
    SFX_3('slash_sword_middle')
    sprite('ko206_03', 1)	# 26-26	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_03', 1)	# 27-27	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_04', 1)	# 28-28	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    Unknown1019(40)
    sprite('ko206_04', 1)	# 29-29	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_04', 1)	# 30-30	 **attackbox here**
    RefreshMultihit()
    if SLOT_51:
        Unknown23029(2, 106, 0)
        clearUponHandler(11)
    sprite('ko206_05', 1)	# 31-31	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    Unknown1019(40)
    sprite('ko206_05', 1)	# 32-32	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_05', 1)	# 33-33	 **attackbox here**
    RefreshMultihit()
    if SLOT_51:
        Unknown23029(2, 106, 0)
        clearUponHandler(11)
    sprite('ko206_06', 3)	# 34-36
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(20)
    Unknown8000(104, 1, 0)
    Unknown23029(2, 109, 0)
    sprite('ko206_07', 3)	# 37-39
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(0)
    sprite('ko206_08', 4)	# 40-43
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko206_09', 4)	# 44-47
    sprite('ko206_10', 2)	# 48-49
    sprite('ko206_10', 1)	# 50-50
    Unknown23029(2, 107, 0)
    sprite('ko206_08', 4)	# 51-54
    sprite('ko206_09', 4)	# 55-58
    sprite('ko206_10', 4)	# 59-62
    sprite('ko206_08', 4)	# 63-66
    sprite('ko206_09', 4)	# 67-70
    sprite('ko206_10', 4)	# 71-74
    sprite('ko206_08', 4)	# 75-78
    sprite('ko206_09', 4)	# 79-82
    sprite('ko206_10', 4)	# 83-86
    label(580)
    sprite('keep', 32767)	# 87-32853
    enterState('PersonaDeleteAndIdling')

@State
def PYU_Persona2B():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000c0f2fcff80841e0000000000a0860100')
        callSubroutine('PYU_AttackInit')
        AttackLevel_(3)
        Damage(200)
        AttackP1(90)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Hitstop(1)
        Unknown9016(1)
        HitLow(2)
        Unknown11057(500)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown11092(1)

        def upon_11():
            SLOT_51 = 1
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        EnableCollision(1)
        Unknown23078(1)
        Unknown23066(0)
        Unknown23059(1)
    sprite('ko232_00', 2)	# 1-2
    teleportRelativeY(0)
    Unknown2053(1)
    sprite('ko232_01', 3)	# 3-5
    physicsXImpulse(7000)
    sprite('ko232_02', 2)	# 6-7
    SFX_3('slash_rapier_middle')
    sprite('ko232_03', 1)	# 8-8	 **attackbox here**
    GFX_1('koef_firewing', 0)
    RefreshMultihit()
    sprite('ko232_03', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    sprite('ko232_03', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('ko232_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('ko232_04', 1)	# 12-12	 **attackbox here**
    GFX_1('koef_firewing', 0)
    RefreshMultihit()
    sprite('ko232_04', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    sprite('ko232_04', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('ko232_04', 1)	# 15-15	 **attackbox here**
    Unknown23066(1)
    RefreshMultihit()
    if SLOT_51:
        Unknown23029(2, 202, 0)
        clearUponHandler(11)
    sprite('ko232_05', 4)	# 16-19
    GFX_1('koef_firewing', 0)
    sprite('ko232_06', 3)	# 20-22
    GFX_1('koef_firewing', 0)
    Unknown1019(80)
    sprite('ko232_06', 1)	# 23-23
    Unknown23029(2, 210, 0)
    sprite('ko232_07', 4)	# 24-27
    sprite('ko232_08', 6)	# 28-33
    Unknown1019(50)
    sprite('ko232_08', 6)	# 34-39
    Unknown1084(1)
    sprite('ko232_08', 6)	# 40-45
    sprite('ko232_08', 10)	# 46-55
    sprite('keep', 32767)	# 56-32822
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaJB():

    def upon_IMMEDIATE():
        Unknown23184('0300000064000000008ffdff0000000000000000000000000000000000000000')
        callSubroutine('PYU_AttackInit')
        AttackLevel_(4)
        Damage(120)
        Hitstop(1)
        AirUntechableTime(24)
        AirPushbackY(30000)
        Unknown9016(1)
        Unknown11057(500)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11092(1)
        callSubroutine('PYU_ForceWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)

        def upon_11():
            SLOT_51 = 1
        Unknown23059(1)
    sprite('ko254_00', 2)	# 1-2
    physicsXImpulse(5000)
    sprite('ko254_01', 2)	# 3-4
    sprite('ko254_02', 1)	# 5-5	 **attackbox here**
    SFX_3('slash_rapier_middle')
    RefreshMultihit()
    sprite('ko254_02', 1)	# 6-6	 **attackbox here**
    RefreshMultihit()
    sprite('ko254_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    Unknown1019(120)
    sprite('ko254_03', 1)	# 8-8	 **attackbox here**
    GFX_1('koef_firewing', 0)
    RefreshMultihit()
    sprite('ko254_03', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    Unknown23022(0)
    sprite('ko254_03', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    Unknown1019(120)
    sprite('ko254_04', 1)	# 11-11	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    sprite('ko254_04', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('ko254_04', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    Unknown1019(120)
    if SLOT_51:
        Unknown23029(2, 5031, 0)
        clearUponHandler(11)
    sprite('ko254_05', 4)	# 14-17
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko254_06', 4)	# 18-21
    GFX_1('koef_firewing', 0)
    sprite('ko254_07', 4)	# 22-25
    Unknown1019(50)
    sprite('ko254_08', 4)	# 26-29
    Unknown1019(50)
    sprite('ko254_07', 4)	# 30-33
    sprite('ko254_08', 4)	# 34-37
    Unknown1084(1)
    sprite('ko254_07', 4)	# 38-41
    sprite('ko254_08', 4)	# 42-45
    sprite('keep', 32767)	# 46-32812
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000000000000000000000c0f2fcff80841e00c0f2fcff002d3101')
        callSubroutine('PYU_AttackInit')
        AttackLevel_(3)
        Damage(500)
        AttackP1(90)
        Unknown11092(1)
        AirUntechableTime(21)
        hitstun(21)
        HitOverhead(2)
        Hitstop(1)
        Unknown23078(1)
        Unknown9016(1)
        GroundedHitstunAnimation(3)
        PushbackX(0)
        AirPushbackX(2000)
        AirPushbackY(-25000)
        YImpluseBeforeWallbounce(1000)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        EnableCollision(0)
        Unknown2053(1)

        def upon_11():
            SLOT_51 = 1
        Unknown23059(1)
        Unknown2049(1)
    sprite('ko233_00', 1)	# 1-1
    sprite('ko233_01', 1)	# 2-2
    sprite('ko233_00', 1)	# 3-3
    Unknown3029(1)
    physicsXImpulse(20000)
    physicsYImpulse(70000)
    Unknown2053(1)
    SFX_0('highjump_m')
    sprite('ko233_01', 1)	# 4-4
    Unknown1028(10000)
    sprite('ko233_00', 1)	# 5-5
    YAccel(50)
    sprite('ko233_01', 1)	# 6-6
    sprite('ko233_00', 1)	# 7-7
    Unknown1019(80)
    YAccel(50)
    Unknown3029(1)
    sprite('ko233_01', 1)	# 8-8
    sprite('ko233_02', 1)	# 9-9
    Unknown1084(1)
    Unknown3029(1)
    sprite('ko233_03', 4)	# 10-13
    clearUponHandler(3)
    sprite('ko233_04', 3)	# 14-16
    sprite('ko233_05', 1)	# 17-17	 **attackbox here**
    physicsYImpulse(-28000)
    RefreshMultihit()
    SFX_3('slash_sword_slow')
    sprite('ko233_07', 1)	# 18-18	 **attackbox here**
    sprite('ko233_09', 1)	# 19-19	 **attackbox here**
    sendToLabelUpon(2, 1)
    label(0)
    sprite('ko233_05', 1)	# 20-20	 **attackbox here**
    GFX_1('koef_233firering', 0)
    GFX_1('koef_233firering', 1)
    GFX_1('koef_233firering', 2)
    RefreshMultihit()
    if SLOT_51:
        Unknown23029(2, 5031, 0)
        clearUponHandler(11)
    sprite('ko233_06', 1)	# 21-21	 **attackbox here**
    sprite('ko233_07', 1)	# 22-22	 **attackbox here**
    sprite('ko233_08', 1)	# 23-23	 **attackbox here**
    sprite('ko233_09', 1)	# 24-24	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ko233_05', 2)	# 25-26	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown8000(104, 1, 1)
    sprite('ko233_06', 2)	# 27-28	 **attackbox here**
    sprite('ko233_07', 2)	# 29-30	 **attackbox here**
    sprite('ko233_08', 2)	# 31-32	 **attackbox here**
    sprite('ko233_09', 2)	# 33-34	 **attackbox here**
    sprite('ko233_05', 3)	# 35-37	 **attackbox here**
    Unknown8000(104, 1, 0)
    sprite('ko233_06', 2)	# 38-39	 **attackbox here**
    sprite('ko233_07', 2)	# 40-41	 **attackbox here**
    sprite('ko233_08', 2)	# 42-43	 **attackbox here**
    sprite('ko233_09', 2)	# 44-45	 **attackbox here**
    sprite('ko233_05', 3)	# 46-48	 **attackbox here**
    Unknown8000(104, 1, 0)
    sprite('keep', 32767)	# 49-32815
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgiA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e00807be1ff00000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(10000)
        PushbackX(30400)
        AirUntechableTime(19)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('ko401_00', 4)	# 1-4
    physicsXImpulse(12000)
    sprite('ko401_01', 2)	# 5-6
    SFX_3('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    sprite('ko401_02', 2)	# 8-9	 **attackbox here**
    sprite('ko401_03', 2)	# 10-11
    GFX_0('AgishotA', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 12-13
    sprite('ko401_05', 2)	# 14-15
    sprite('ko401_06', 2)	# 16-17
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 18-21
    sprite('ko401_08', 4)	# 22-25
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 26-29
    SFX_3('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 30-33
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 34-41
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 42-49
    sprite('ko401_13', 8)	# 50-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAirAgiA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000807be1ff80841e00807be1ff00000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(20000)
        PushbackX(30400)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('ko401_00', 4)	# 1-4
    physicsXImpulse(12000)
    sprite('ko401_01', 2)	# 5-6
    SFX_3('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    sprite('ko401_02', 2)	# 8-9	 **attackbox here**
    sprite('ko401_03', 2)	# 10-11
    GFX_0('AgishotA', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 12-13
    sprite('ko401_05', 2)	# 14-15
    sprite('ko401_06', 2)	# 16-17
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 18-21
    sprite('ko401_08', 4)	# 22-25
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 26-29
    SFX_3('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 30-33
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 34-41
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 42-49
    sprite('ko401_13', 8)	# 50-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgiB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e00807be1ff00000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(37000)
        AirPushbackY(20000)
        PushbackX(30400)
        AirUntechableTime(30)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('ko401_00', 4)	# 1-4
    physicsXImpulse(12000)
    sprite('ko401_01', 2)	# 5-6
    SFX_3('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    sprite('ko401_02', 2)	# 8-9	 **attackbox here**
    Unknown23022(0)
    sprite('ko401_03', 2)	# 10-11
    GFX_0('AgishotB', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 12-13
    sprite('ko401_05', 2)	# 14-15
    sprite('ko401_06', 2)	# 16-17
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 18-21
    sprite('ko401_08', 4)	# 22-25
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 26-29
    SFX_3('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 30-33
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 34-41
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 42-49
    sprite('ko401_13', 8)	# 50-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAirAgiB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000807be1ff80841e00807be1ff00000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(24)
        AirPushbackX(35000)
        AirPushbackY(20000)
        PushbackX(30400)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('ko401_00', 4)	# 1-4
    physicsXImpulse(12000)
    sprite('ko401_01', 2)	# 5-6
    SFX_3('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    sprite('ko401_02', 2)	# 8-9	 **attackbox here**
    Unknown23022(0)
    sprite('ko401_03', 2)	# 10-11
    GFX_0('AgishotB', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 12-13
    sprite('ko401_05', 2)	# 14-15
    sprite('ko401_06', 2)	# 16-17
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 18-21
    sprite('ko401_08', 4)	# 22-25
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 26-29
    SFX_3('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 30-33
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 34-41
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 42-49
    sprite('ko401_13', 8)	# 50-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgiC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e00807be1ff00000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(100)
        Unknown30065(0)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(2000)
        AirPushbackY(28000)
        PushbackX(30400)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('ko401_00', 6)	# 1-6
    physicsXImpulse(6000)
    sprite('ko401_01', 2)	# 7-8
    SFX_3('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    Unknown4007(0)
    sprite('ko401_02', 2)	# 10-11	 **attackbox here**
    Unknown23022(0)
    sprite('ko401_03', 2)	# 12-13
    GFX_0('AgishotAB', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 14-15
    sprite('ko401_05', 2)	# 16-17
    sprite('ko401_06', 2)	# 18-19
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 20-23
    sprite('ko401_08', 4)	# 24-27
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 28-31
    SFX_3('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 32-35
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 36-43
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 44-51
    sprite('ko401_13', 8)	# 52-59
    sprite('keep', 32767)	# 60-32826
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAirAgiC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e00807be1ff00000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(700)
        AttackP1(90)
        AttackP2(100)
        Unknown30065(0)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(2000)
        AirPushbackY(22000)
        PushbackX(30400)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown2053(1)
        Unknown23078(1)
        Unknown23059(1)
    sprite('ko401_00', 4)	# 1-4
    physicsXImpulse(6000)
    sprite('ko401_01', 2)	# 5-6
    SFX_3('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    Unknown4007(0)
    sprite('ko401_02', 2)	# 8-9	 **attackbox here**
    Unknown23022(0)
    sprite('ko401_03', 2)	# 10-11
    GFX_0('AgishotAB', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 12-13
    sprite('ko401_05', 2)	# 14-15
    sprite('ko401_06', 2)	# 16-17
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 18-21
    sprite('ko401_08', 4)	# 22-25
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 26-29
    SFX_3('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 30-33
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 34-41
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 42-49
    sprite('ko401_13', 8)	# 50-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaMaharagiA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff0000000000000000000000000000000000000000')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown4007(2)
        Unknown4008(2)
        callSubroutine('PYU_SPAttackInit')
        Unknown2006()
        Unknown23059(1)
    sprite('ko402_00', 5)	# 1-5
    physicsXImpulse(2000)
    sprite('ko402_01', 2)	# 6-7
    sprite('ko402_02', 1)	# 8-8
    SFX_3('slash_sword_slow')
    GFX_1('koef_firewing', 0)
    GFX_0('SlidingA', 1)
    Unknown23029(1, 4050, 0)
    sprite('ko402_02', 2)	# 9-10
    Unknown23022(0)
    sprite('ko402_03', 2)	# 11-12
    GFX_1('koef_firewing', 0)
    sprite('ko402_04', 2)	# 13-14
    GFX_1('koef_firewing', 0)
    sprite('ko402_05', 2)	# 15-16
    GFX_1('koef_firewing', 0)
    sprite('ko402_06', 2)	# 17-18
    GFX_1('koef_firewing', 0)
    physicsXImpulse(0)
    sprite('ko402_07', 6)	# 19-24
    sprite('ko402_08', 6)	# 25-30
    sprite('ko402_09', 6)	# 31-36
    SLOT_10 = 0
    sprite('ko402_07', 6)	# 37-42
    sprite('ko402_08', 6)	# 43-48
    sprite('ko402_09', 6)	# 49-54
    sprite('ko402_07', 6)	# 55-60
    sprite('keep', 32767)	# 61-32827
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaMaharagiB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff0000000000000000000000000000000000000000')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown4007(2)
        Unknown4008(2)
        callSubroutine('PYU_SPAttackInit')
        Unknown2006()
        Unknown23059(1)
    sprite('ko402_00', 5)	# 1-5
    physicsXImpulse(2000)
    sprite('ko402_01', 2)	# 6-7
    sprite('ko402_02', 1)	# 8-8
    SFX_3('slash_sword_slow')
    GFX_1('koef_firewing', 0)
    GFX_0('SlidingB', 1)
    Unknown23029(1, 4060, 0)
    sprite('ko402_02', 2)	# 9-10
    Unknown23022(0)
    sprite('ko402_03', 2)	# 11-12
    GFX_1('koef_firewing', 0)
    sprite('ko402_04', 2)	# 13-14
    GFX_1('koef_firewing', 0)
    sprite('ko402_05', 2)	# 15-16
    GFX_1('koef_firewing', 0)
    sprite('ko402_06', 2)	# 17-18
    GFX_1('koef_firewing', 0)
    physicsXImpulse(0)
    sprite('ko402_07', 6)	# 19-24
    sprite('ko402_08', 6)	# 25-30
    sprite('ko402_09', 6)	# 31-36
    SLOT_10 = 0
    sprite('ko402_07', 6)	# 37-42
    sprite('ko402_08', 6)	# 43-48
    sprite('ko402_09', 6)	# 49-54
    sprite('ko402_07', 6)	# 55-60
    sprite('keep', 32767)	# 61-32827
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaMaharagiC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000b03cffff0000000000000000000000000000000000000000')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown4007(2)
        Unknown4008(2)
        callSubroutine('PYU_SPAttackInit')
        Unknown2006()
        Unknown23059(1)
    sprite('ko402_00', 5)	# 1-5
    physicsXImpulse(2000)
    sprite('ko402_01', 2)	# 6-7
    sprite('ko402_02', 1)	# 8-8
    SFX_3('slash_sword_slow')
    GFX_1('koef_firewing', 0)
    GFX_0('SlidingC', 1)
    Unknown23029(1, 4071, 0)
    sprite('ko402_02', 2)	# 9-10
    Unknown23022(0)
    sprite('ko402_03', 2)	# 11-12
    GFX_1('koef_firewing', 0)
    sprite('ko402_04', 2)	# 13-14
    GFX_1('koef_firewing', 0)
    sprite('ko402_05', 2)	# 15-16
    GFX_1('koef_firewing', 0)
    sprite('ko402_06', 2)	# 17-18
    GFX_1('koef_firewing', 0)
    physicsXImpulse(0)
    sprite('ko402_07', 6)	# 19-24
    sprite('ko402_08', 6)	# 25-30
    sprite('ko402_09', 6)	# 31-36
    SLOT_10 = 0
    sprite('ko402_07', 6)	# 37-42
    sprite('ko402_08', 6)	# 43-48
    sprite('ko402_09', 6)	# 49-54
    sprite('ko402_07', 6)	# 55-60
    sprite('keep', 32767)	# 61-32827
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaFireBooster():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        callSubroutine('PYU_ForceWarp')
        Unknown4007(3)
        Unknown2019(100)
        Unknown2006()
        Unknown3032()
        Unknown3001(50)
        Unknown3004(20)
        Unknown23022(1)

        def upon_STATE_END():
            SLOT_10 = 0
            Unknown3031()
        Unknown23059(1)
    sprite('ko403_00', 4)	# 1-4
    sprite('ko403_01', 4)	# 5-8
    sprite('ko403_02', 4)	# 9-12
    sprite('ko403_03', 6)	# 13-18
    sprite('ko403_04', 6)	# 19-24
    sprite('ko403_05', 6)	# 25-30
    sprite('keep', 32767)	# 31-32797
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaFireAttackA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        Unknown17003()
        AttackLevel_(3)
        Damage(300)
        AirPushbackY(22000)
        Hitstop(5)
        Unknown9016(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11092(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown23078(0)
        Unknown2006()
        Unknown2053(1)
        callSubroutine('BoosterDamageUp')
        Unknown23059(1)
    sprite('ko404_00', 3)	# 1-3
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_01', 2)	# 4-5
    physicsXImpulse(14000)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_02', 2)	# 6-7
    SFX_3('slash_rapier_fast')
    Unknown1019(110)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_03', 1)	# 8-8	 **attackbox here**
    Unknown1019(110)
    RefreshMultihit()
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_03', 1)	# 9-9	 **attackbox here**
    Unknown23022(0)
    sprite('ko404_04', 2)	# 10-11
    Unknown1019(110)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_05', 2)	# 12-13
    Unknown1019(110)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_06', 2)	# 14-15
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_07', 2)	# 16-17
    SFX_3('bomb_m')
    SFX_3('blaze_normal')
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_08', 3)	# 18-20	 **attackbox here**
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    GFX_1('koef_404_bom', 2)
    GFX_1('koef_404_fire', 3)
    GFX_1('koef_404_fire', 4)
    GFX_1('koef_404_fire', 5)
    GFX_1('koef_404_fire', 6)
    Unknown1019(0)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(1)
    AttackLevel_(3)
    Damage(500)
    AirUntechableTime(32)
    Hitstop(1)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(14000)
    AirPushbackY(21000)
    YImpluseBeforeWallbounce(1800)
    Unknown9016(0)
    Unknown9017(1)
    Unknown9021(1)
    callSubroutine('BoosterDamageUp')
    Unknown11058('0000000000000000000000000000000001000000')
    sprite('ko404_09', 2)	# 21-22	 **attackbox here**
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_08', 4)	# 23-26	 **attackbox here**
    DisableAttackRestOfMove()
    SLOT_10 = 0
    sprite('ko404_09', 4)	# 27-30	 **attackbox here**
    sprite('ko404_08', 4)	# 31-34	 **attackbox here**
    sprite('ko404_09', 4)	# 35-38	 **attackbox here**
    sprite('keep', 32767)	# 39-32805
    enterState('PersonaDeleteAndIdling')

@State
def PersonaFireAttackB():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e000000000000000000')
        callSubroutine('PYU_AttackInit')
        AttackLevel_(3)
        Damage(900)
        AttackP1(90)
        AirPushbackY(22000)
        Hitstop(1)
        Unknown11001(6, 6, 6)
        Unknown9016(1)
        AirHitstunAnimation(9)
        Unknown11092(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23078(1)
        if SLOT_4:
            Unknown11044(1)
        callSubroutine('PYU_ForceWarp')
        Unknown2053(1)
        if Unknown23145('PYU_Persona2B'):
            Unknown2006()
        callSubroutine('BoosterDamageUp')
        Unknown23059(1)
    sprite('ko404_00', 2)	# 1-2
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    physicsXImpulse(20000)
    sprite('ko404_01', 2)	# 3-4
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_02', 1)	# 5-5
    SFX_3('slash_rapier_fast')
    Unknown1019(120)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_03', 1)	# 6-6	 **attackbox here**
    Unknown1019(120)
    RefreshMultihit()
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_03', 1)	# 7-7	 **attackbox here**
    Unknown23022(0)
    sprite('ko404_04', 2)	# 8-9
    Unknown1019(120)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_05', 2)	# 10-11
    Unknown1019(120)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_06', 3)	# 12-14
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_07', 3)	# 15-17
    SFX_3('bomb_m')
    SFX_3('blaze_normal')
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_08', 3)	# 18-20	 **attackbox here**
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    GFX_1('koef_404_bom', 2)
    GFX_1('koef_404_fire', 3)
    GFX_1('koef_404_fire', 4)
    GFX_1('koef_404_fire', 5)
    GFX_1('koef_404_fire', 6)
    Unknown1019(0)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(1)
    AttackLevel_(3)
    Damage(1600)
    Hitstop(1)
    Unknown23078(1)
    AirUntechableTime(47)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(23000)
    AirPushbackY(20000)
    YImpluseBeforeWallbounce(1800)
    Unknown9016(0)
    Unknown9017(1)
    Unknown9021(1)
    callSubroutine('BoosterDamageUp')
    Unknown11058('0000000000000000000000000100000000000000')
    if SLOT_4:
        Unknown30088(1)
    sprite('ko404_09', 2)	# 21-22	 **attackbox here**
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_08', 4)	# 23-26	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('ko404_09', 4)	# 27-30	 **attackbox here**
    sprite('ko404_08', 4)	# 31-34	 **attackbox here**
    sprite('ko404_09', 4)	# 35-38	 **attackbox here**
    sprite('ko404_08', 4)	# 39-42	 **attackbox here**
    sprite('ko404_09', 4)	# 43-46	 **attackbox here**
    sprite('ko404_08', 4)	# 47-50	 **attackbox here**
    sprite('ko404_09', 4)	# 51-54	 **attackbox here**
    sprite('keep', 32767)	# 55-32821
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaFireBird():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feffc0d4010000000000000000000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(4)
        Damage(1000)
        AttackP1(70)
        AirUntechableTime(80)
        AirPushbackY(40000)
        AirPushbackX(10000)
        GroundedHitstunAnimation(1)
        Hitstop(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        WallbounceReboundTime(3)
        Unknown9017(1)
        Unknown23022(1)
        Unknown11092(1)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11042(1)
        Unknown11061(1)
        Unknown23089('0300000001000000010000000100000001000000000000000000000000000000')
        sendToLabelUpon(54, 580)
        callSubroutine('PYU_ForceWarp')
        EnableCollision(0)
        callSubroutine('BoosterDamageUp')
        Unknown23059(1)
    sprite('ko405_00', 3)	# 1-3
    sprite('ko405_01', 3)	# 4-6
    sprite('ko405_02', 3)	# 7-9
    sprite('ko405_03', 2)	# 10-11
    sprite('ko405_04', 2)	# 12-13
    sprite('ko405_05', 2)	# 14-15
    sprite('ko405_06', 3)	# 16-18
    SFX_3('airbackdash_l')
    physicsXImpulse(10000)
    sprite('ko405_07', 2)	# 19-20
    Unknown1019(200)
    sprite('ko405_08', 2)	# 21-22
    Unknown1019(200)
    label(0)
    sprite('ko405_09', 3)	# 23-25	 **attackbox here**
    SLOT_51 = (SLOT_51 + 1)
    if (SLOT_51 >= 8):
        gotoLabel(1)
    GFX_0('firebard', 100)
    SFX_3('airdash_m')
    SFX_3('blaze_normal')
    RefreshMultihit()
    Unknown1019(110)
    sprite('ko405_10', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    Unknown1019(110)
    gotoLabel(0)
    label(580)
    sprite('ko405_09', 3)	# 29-31	 **attackbox here**
    SFX_3('blaze_long')
    Unknown1019(110)
    sprite('ko405_10', 3)	# 32-34	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_09', 3)	# 35-37	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_10', 3)	# 38-40	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_09', 3)	# 41-43	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_10', 3)	# 44-46	 **attackbox here**
    sprite('ko405_09', 3)	# 47-49	 **attackbox here**
    sprite('ko405_10', 3)	# 50-52	 **attackbox here**
    sprite('ko405_09', 3)	# 53-55	 **attackbox here**
    sprite('ko405_10', 3)	# 56-58	 **attackbox here**
    sprite('ko405_09', 3)	# 59-61	 **attackbox here**
    sprite('ko405_10', 3)	# 62-64	 **attackbox here**
    sprite('ko405_09', 3)	# 65-67	 **attackbox here**
    sprite('ko405_10', 3)	# 68-70	 **attackbox here**
    label(1)
    sprite('keep', 32767)	# 71-32837
    enterState('PersonaDeleteAndIdling')

@Subroutine
def Cheak_IputHold():
    SLOT_52 = 0
    if CheckInput(0x1):
        SLOT_52 = 1
    if CheckInput(0xa):
        SLOT_52 = 1
    if CheckInput(0x13):
        SLOT_52 = 1
    if CheckInput(0x1c):
        SLOT_52 = 1

@Subroutine
def Agidine_Move():

    def upon_CLEAR_OR_EXIT():
        if SLOT_55:
            Unknown48('190000000200000035000000020000000200000026000000')
            if (SLOT_53 == SLOT_38):
                physicsYImpulse(0)
                physicsXImpulse(0)
                if CheckInput(0x37):
                    physicsXImpulse(-20000)
                    physicsYImpulse(-20000)
                if CheckInput(0x44):
                    physicsYImpulse(-20000)
                if CheckInput(0x51):
                    physicsXImpulse(20000)
                    physicsYImpulse(-20000)
                if CheckInput(0x5e):
                    physicsXImpulse(-20000)
                if CheckInput(0x6b):
                    pass
                if CheckInput(0x78):
                    physicsXImpulse(20000)
                if CheckInput(0x85):
                    physicsXImpulse(-20000)
                    physicsYImpulse(20000)
                if CheckInput(0x92):
                    physicsYImpulse(20000)
                if CheckInput(0x9f):
                    physicsXImpulse(20000)
                    physicsYImpulse(20000)
            else:
                if CheckInput(0x51):
                    physicsXImpulse(-20000)
                    physicsYImpulse(-20000)
                if CheckInput(0x44):
                    physicsYImpulse(-20000)
                if CheckInput(0x37):
                    physicsXImpulse(20000)
                    physicsYImpulse(-20000)
                if CheckInput(0x78):
                    physicsXImpulse(-20000)
                if CheckInput(0x6b):
                    pass
                if CheckInput(0x5e):
                    physicsXImpulse(20000)
                if CheckInput(0x9f):
                    physicsXImpulse(-20000)
                    physicsYImpulse(20000)
                if CheckInput(0x92):
                    physicsYImpulse(20000)
                if CheckInput(0x85):
                    physicsXImpulse(20000)
                    physicsYImpulse(20000)

@State
def PYU_PersonaAgidine():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PYU_DDAttackInit')
        AttackLevel_(4)
        Damage(540)
        Hitstop(1)
        PushbackX(2000)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AttackP2(98)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(30)
        Unknown9021(1)
        Unknown9017(1)
        Unknown11056(0)
        Unknown30055('000000005000000000000000')
        Unknown30056('60ea0000500000003c000000')
        Unknown11057(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown23182(2)
        Unknown2054(1)
        callSubroutine('BoosterDamageUp')
        callSubroutine('PYU_CheckWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown2006()
        EnableCollision(0)
        Unknown2053(1)
        Unknown2034(0)
        teleportRelativeY(0)
        Unknown23066(1)
        setInvincible(1)
        DisableAttackRestOfMove()
        Unknown23059(1)
    sprite('ko430_00', 2)	# 1-2	 **attackbox here**
    sprite('ko430_01', 2)	# 3-4	 **attackbox here**
    physicsXImpulse(14000)
    sprite('ko430_02', 2)	# 5-6	 **attackbox here**
    sprite('ko430_03', 2)	# 7-8	 **attackbox here**
    sprite('ko430_04', 2)	# 9-10	 **attackbox here**
    sprite('ko430_05', 2)	# 11-12	 **attackbox here**
    SFX_3('spin_m')
    label(0)
    sprite('ko430_00', 2)	# 13-14	 **attackbox here**
    if (SLOT_51 >= 4):
        gotoLabel(1)
    SLOT_51 = (SLOT_51 + 1)
    Unknown1019(50)
    sprite('ko430_01', 2)	# 15-16	 **attackbox here**
    sprite('ko430_02', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    if op(4, 2, 51, 0, 2):
        GFX_0('agidine_firering', 100)
        GFX_0('firering_sub', 100)
    SFX_3('blaze_normal')
    sprite('ko430_03', 2)	# 19-20	 **attackbox here**
    sprite('ko430_04', 2)	# 21-22	 **attackbox here**
    sprite('ko430_05', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    SFX_3('spin_m')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ko430_00', 2)	# 25-26	 **attackbox here**
    Unknown1084(1)
    Unknown2034(0)
    sprite('ko430_01', 2)	# 27-28	 **attackbox here**
    sprite('ko430_02', 2)	# 29-30	 **attackbox here**
    sprite('ko430_03', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(0)
    sprite('ko430_06', 2)	# 33-34
    Unknown1084(1)
    clearUponHandler(3)
    sprite('ko430_07', 3)	# 35-37
    GFX_1('koef_firewing', 0)
    sprite('ko430_08', 3)	# 38-40
    GFX_1('koef_firewing', 0)
    sprite('ko430_09', 3)	# 41-43
    GFX_1('koef_firewing', 0)
    Unknown2006()
    if (SLOT_51 >= 4):
        GFX_0('agidine_fireuzuM', 0)
    sprite('ko430_10', 4)	# 44-47
    GFX_1('koef_firewing', 0)
    Unknown21012('46697265597567616d694232000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('ko430_11', 4)	# 48-51
    sprite('ko430_12', 4)	# 52-55
    sprite('ko430_10', 4)	# 56-59
    sprite('ko430_11', 4)	# 60-63
    sprite('ko430_12', 4)	# 64-67
    sprite('ko430_10', 5)	# 68-72
    sprite('ko430_11', 5)	# 73-77
    sprite('ko430_12', 5)	# 78-82
    sprite('ko430_10', 5)	# 83-87
    sprite('ko430_11', 5)	# 88-92
    sprite('ko430_12', 5)	# 93-97
    SLOT_10 = 0
    sprite('keep', 32767)	# 98-32864
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgidine_OD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PYU_DDAttackInit')
        Unknown23056('')
        AttackLevel_(4)
        Damage(620)
        AttackP2(98)
        Hitstop(1)
        PushbackX(2000)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(30)
        Unknown9021(1)
        Unknown9017(1)
        Unknown11056(0)
        Unknown30055('000000005000000000000000')
        Unknown30056('60ea0000500000003c000000')
        Unknown11057(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown23182(2)
        Unknown2054(1)
        callSubroutine('BoosterDamageUp')
        callSubroutine('PYU_CheckWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown2006()
        EnableCollision(0)
        Unknown2053(1)
        Unknown2034(0)
        teleportRelativeY(0)
        Unknown23066(1)
        setInvincible(1)
        DisableAttackRestOfMove()

        def upon_STATE_END():
            SLOT_10 = 0
        Unknown23059(1)
    sprite('ko430_00', 2)	# 1-2	 **attackbox here**
    sprite('ko430_01', 2)	# 3-4	 **attackbox here**
    physicsXImpulse(14000)
    sprite('ko430_02', 2)	# 5-6	 **attackbox here**
    sprite('ko430_03', 2)	# 7-8	 **attackbox here**
    sprite('ko430_04', 2)	# 9-10	 **attackbox here**
    sprite('ko430_05', 2)	# 11-12	 **attackbox here**
    SFX_3('spin_m')
    label(0)
    sprite('ko430_00', 2)	# 13-14	 **attackbox here**
    if (SLOT_51 >= 4):
        gotoLabel(1)
    SLOT_51 = (SLOT_51 + 1)
    Unknown1019(50)
    sprite('ko430_01', 2)	# 15-16	 **attackbox here**
    sprite('ko430_02', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    if op(4, 2, 51, 0, 2):
        GFX_0('agidine_firering', 100)
        GFX_0('firering_sub', 100)
    SFX_3('blaze_normal')
    sprite('ko430_03', 2)	# 19-20	 **attackbox here**
    sprite('ko430_04', 2)	# 21-22	 **attackbox here**
    sprite('ko430_05', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    SFX_3('spin_m')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ko430_00', 2)	# 25-26	 **attackbox here**
    Unknown1084(1)
    Unknown2034(0)
    sprite('ko430_01', 2)	# 27-28	 **attackbox here**
    sprite('ko430_02', 2)	# 29-30	 **attackbox here**
    sprite('ko430_03', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(0)
    sprite('ko430_06', 2)	# 33-34
    Unknown1084(1)
    clearUponHandler(3)
    sprite('ko430_07', 3)	# 35-37
    GFX_1('koef_firewing', 0)
    sprite('ko430_08', 3)	# 38-40
    GFX_1('koef_firewing', 0)
    sprite('ko430_09', 3)	# 41-43
    GFX_1('koef_firewing', 0)
    Unknown2006()
    if (SLOT_51 >= 4):
        GFX_0('agidine_fireuzuL', 0)
    sprite('ko430_10', 4)	# 44-47
    GFX_1('koef_firewing', 0)
    Unknown21012('46697265597567616d694232000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('ko430_11', 4)	# 48-51
    sprite('ko430_12', 4)	# 52-55
    sprite('ko430_10', 4)	# 56-59
    sprite('ko430_11', 4)	# 60-63
    sprite('ko430_12', 4)	# 64-67
    sprite('ko430_10', 5)	# 68-72
    sprite('ko430_11', 5)	# 73-77
    sprite('ko430_12', 5)	# 78-82
    sprite('ko430_10', 5)	# 83-87
    sprite('ko430_11', 5)	# 88-92
    sprite('ko430_12', 5)	# 93-97
    SLOT_10 = 0
    sprite('keep', 32767)	# 98-32864
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgidineDUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PYU_DDAttackInit')
        AttackLevel_(4)
        Damage(100)
        Hitstop(1)
        PushbackX(2000)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(30)
        Unknown9021(1)
        Unknown9017(1)
        Unknown11056(0)
        Unknown30055('000000005000000000000000')
        Unknown30056('60ea0000500000003c000000')
        Unknown11057(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown23182(2)
        Unknown11092(1)
        AttackP1(100)
        MinimumDamagePct(100)
        AttackP2(100)
        Unknown2054(1)
        callSubroutine('PYU_CheckWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown2006()
        EnableCollision(0)
        Unknown2053(1)
        Unknown2034(0)
        teleportRelativeY(0)
        Unknown23066(1)
        setInvincible(1)
        DisableAttackRestOfMove()
        Unknown23059(1)
    sprite('ko430_06', 2)	# 1-2
    Unknown1084(1)
    clearUponHandler(3)
    sprite('ko430_07', 3)	# 3-5
    GFX_1('koef_firewing', 0)
    sprite('ko430_08', 3)	# 6-8
    GFX_1('koef_firewing', 0)
    sprite('ko430_09', 3)	# 9-11
    GFX_1('koef_firewing', 0)
    Unknown2006()
    GFX_0('agidine_fireuzuL_TAG', 0)
    sprite('ko430_10', 4)	# 12-15
    GFX_1('koef_firewing', 0)
    Unknown21012('46697265597567616d694232000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('ko430_11', 4)	# 16-19
    sprite('ko430_12', 4)	# 20-23
    sprite('ko430_10', 4)	# 24-27
    sprite('ko430_11', 4)	# 28-31
    sprite('ko430_12', 4)	# 32-35
    sprite('ko430_10', 5)	# 36-40
    sprite('ko430_11', 5)	# 41-45
    sprite('ko430_12', 5)	# 46-50
    sprite('ko430_10', 5)	# 51-55
    sprite('ko430_11', 5)	# 56-60
    sprite('ko430_12', 5)	# 61-65
    SLOT_10 = 0
    sprite('keep', 32767)	# 66-32832
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgidineDUO_OD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PYU_DDAttackInit')
        Unknown23056('')
        AttackLevel_(4)
        Damage(100)
        Hitstop(1)
        PushbackX(2000)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(30)
        Unknown9021(1)
        Unknown9017(1)
        Unknown11056(0)
        Unknown30055('000000005000000000000000')
        Unknown30056('60ea0000500000003c000000')
        Unknown11057(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23022(1)
        Unknown23182(2)
        Unknown11092(1)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Unknown2054(1)
        callSubroutine('PYU_CheckWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown2006()
        EnableCollision(0)
        Unknown2053(1)
        Unknown2034(0)
        teleportRelativeY(0)
        Unknown23066(1)
        setInvincible(1)
        DisableAttackRestOfMove()
        Unknown23059(1)
    sprite('ko430_06', 2)	# 1-2
    Unknown1084(1)
    clearUponHandler(3)
    sprite('ko430_07', 3)	# 3-5
    GFX_1('koef_firewing', 0)
    sprite('ko430_08', 3)	# 6-8
    GFX_1('koef_firewing', 0)
    sprite('ko430_09', 3)	# 9-11
    GFX_1('koef_firewing', 0)
    Unknown2006()
    GFX_0('agidine_fireuzuL_OD_TAG', 0)
    sprite('ko430_10', 4)	# 12-15
    GFX_1('koef_firewing', 0)
    Unknown21012('46697265597567616d694232000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('ko430_11', 4)	# 16-19
    sprite('ko430_12', 4)	# 20-23
    sprite('ko430_10', 4)	# 24-27
    sprite('ko430_11', 4)	# 28-31
    sprite('ko430_12', 4)	# 32-35
    sprite('ko430_10', 5)	# 36-40
    sprite('ko430_11', 5)	# 41-45
    sprite('ko430_12', 5)	# 46-50
    sprite('ko430_10', 5)	# 51-55
    sprite('ko430_11', 5)	# 56-60
    sprite('ko430_12', 5)	# 61-65
    SLOT_10 = 0
    sprite('keep', 32767)	# 66-32832
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaMaharagidine():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PYU_DDAttackInit')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown4007(3)
        Unknown2019(100)
        Unknown1084(1)
        Unknown3032()
        Unknown3001(50)
        Unknown3004(10)
        Unknown2054(1)
        Unknown23022(1)
        Unknown2034(0)

        def upon_STATE_END():
            SLOT_10 = 0
            Unknown3031()
        Unknown23059(1)
    sprite('ko431_00', 6)	# 1-6
    physicsYImpulse(-5000)
    sprite('ko431_01', 6)	# 7-12
    sprite('ko431_02', 6)	# 13-18
    sprite('ko431_03', 4)	# 19-22
    sprite('ko431_04', 4)	# 23-26
    sprite('ko431_05', 4)	# 27-30
    sprite('ko431_06', 4)	# 31-34
    sprite('ko431_07', 4)	# 35-38
    sprite('ko431_08', 4)	# 39-42
    sprite('ko431_09', 4)	# 43-46
    sprite('ko431_10', 4)	# 47-50
    physicsYImpulse(8000)
    if (not CheckInput(0xa)):
        if (not CheckInput(0x13)):
            GFX_0('MaharagidineC_fire', 104)
            Unknown23029(2, 10055, 0)
        else:
            GFX_0('MaharagidineD_fire', 104)
    else:
        GFX_0('MaharagidineD_fire', 104)
    sprite('ko431_11', 4)	# 51-54
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_12', 6)	# 55-60
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_13', 6)	# 61-66
    YAccel(80)
    sprite('ko431_14', 6)	# 67-72
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_12', 6)	# 73-78
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_13', 6)	# 79-84
    YAccel(80)
    sprite('ko431_14', 6)	# 85-90
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(0)
    sprite('ko431_12', 8)	# 91-98
    SLOT_10 = 0
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    sprite('keep', 32767)	# 99-32865
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaMaharagidine_OD():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PYU_DDAttackInit')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown4007(3)
        Unknown2019(100)
        Unknown1084(1)
        Unknown3032()
        Unknown3001(50)
        Unknown3004(10)
        Unknown2054(1)
        Unknown23022(1)

        def upon_STATE_END():
            SLOT_10 = 0
            Unknown3031()
        Unknown23059(1)
    sprite('ko431_00', 6)	# 1-6
    physicsYImpulse(-5000)
    sprite('ko431_01', 6)	# 7-12
    sprite('ko431_02', 6)	# 13-18
    sprite('ko431_03', 4)	# 19-22
    sprite('ko431_04', 4)	# 23-26
    sprite('ko431_05', 4)	# 27-30
    sprite('ko431_06', 4)	# 31-34
    sprite('ko431_07', 4)	# 35-38
    sprite('ko431_08', 4)	# 39-42
    sprite('ko431_09', 4)	# 43-46
    sprite('ko431_10', 4)	# 47-50
    physicsYImpulse(8000)
    if CheckInput(0xa):
        if CheckInput(0x13):
            GFX_0('MaharagidineOD_D_fire', 104)
        else:
            GFX_0('MaharagidineOD_C_fire', 104)
            Unknown23029(2, 10055, 0)
    else:
        GFX_0('MaharagidineOD_C_fire', 104)
        Unknown23029(2, 10055, 0)
    sprite('ko431_11', 4)	# 51-54
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_12', 6)	# 55-60
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_13', 6)	# 61-66
    YAccel(80)
    sprite('ko431_14', 6)	# 67-72
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_12', 6)	# 73-78
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(80)
    sprite('ko431_13', 6)	# 79-84
    YAccel(80)
    sprite('ko431_14', 6)	# 85-90
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    YAccel(0)
    sprite('ko431_12', 8)	# 91-98
    SLOT_10 = 0
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    sprite('keep', 32767)	# 99-32865
    enterState('PersonaDeleteAndIdling')

@State
def PersonaIchigeki():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000c0f2fcff0000000000000000000000000000000000000000')
        callSubroutine('PYU_AstralAttackInit')
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(873)
        AttackP1(90)
        Hitstop(1)
        Unknown9016(1)
        Unknown11064(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11056(0)
        AirPushbackX(84000)
        AirPushbackY(28000)
        AirUntechableTime(10000)
        Unknown9310(60)
        Unknown9178(1)
        Unknown9346(0)
        Unknown4007(3)
        callSubroutine('PYU_CheckWarp')
        Unknown23022(1)

        def upon_12():
            SLOT_51 = 1
            Unknown21007(3, 32)
            EnableCollision(0)
    sprite('ko450_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(2)
    Unknown3071(5)
    Unknown3074('00000000c80000000000000000000000')
    Unknown3075('00000000000000000000000000000000')
    physicsXImpulse(20000)
    Unknown2053(1)
    Unknown4007(0)
    sprite('ko450_01', 2)	# 3-4
    SFX_3('airdash_m')
    physicsXImpulse(30000)
    sprite('ko450_00', 2)	# 5-6
    physicsXImpulse(60000)
    sprite('ko450_01', 3)	# 7-9
    sprite('ko206_02', 2)	# 10-11
    Unknown1019(80)
    sprite('ko206_03', 2)	# 12-13	 **attackbox here**
    Unknown23119(-2351616, 20, 2)
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    Unknown1019(80)
    sprite('ko206_04', 2)	# 14-15	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(80)
    SFX_3('slash_sword_middle')
    sprite('ko206_05', 2)	# 16-17	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(80)
    sprite('ko206_06', 2)	# 18-19
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(50)
    sprite('ko206_07', 3)	# 20-22
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    Unknown1084(1)
    sprite('ko206_08', 2)	# 23-24
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko206_09', 2)	# 25-26
    sprite('ko206_10', 2)	# 27-28
    Unknown19(0, 2, 51)
    label(1)
    sprite('ko450_02', 2)	# 29-30

    def upon_CLEAR_OR_EXIT():
        Unknown48('19000000020000003400000016000000020000000c000000')
        if (SLOT_52 > 0):
            clearUponHandler(3)
            Unknown36(22)
            Unknown1019(1)
            YAccel(1)
            Unknown1039(1)
            Unknown35()
    sprite('ko450_02', 3)	# 31-33
    sprite('ko450_03', 3)	# 34-36
    Unknown23119(-7602176, 40, 4)
    GFX_0('Konohana_charge', 0)
    Unknown38(5, 1)
    sprite('ko450_04', 3)	# 37-39
    sprite('ko450_05', 3)	# 40-42
    sprite('ko450_06', 3)	# 43-45
    sprite('ko450_07', 3)	# 46-48
    sprite('ko450_07', 6)	# 49-54
    Unknown23118(-19456)
    sprite('ko450_08', 80)	# 55-134
    GFX_0('Konohana_egg', 0)
    Unknown38(6, 1)
    sprite('ko450_08', 10)	# 135-144
    SFX_3('yu003')
    Unknown21007(5, 32)
    Unknown21007(6, 32)
    GFX_0('Konohana_burst', 0)
    GFX_0('BurstYugami', 0)
    ScreenShake(50000, 50000)
    sprite('null', 6)	# 145-150
    Unknown36(22)
    Unknown1019(0)
    YAccel(0)
    Unknown1039(-1)
    Unknown35()
    sprite('null', 32767)	# 151-32917
    sendToLabel(99)
    label(0)
    sprite('keep', 32767)	# 32918-65684
    enterState('PersonaDeleteAndIdling')
    label(99)
    sprite('keep', 32767)	# 65685-98451
    enterState('PYU_PersonaWait')

@State
def PYU_Crash_Rush1st():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff000000000000000080841e000000000000000000')
        callSubroutine('PYU_AttackInit')
        AttackDefaults_StandingNormal()
        DisableAttackRestOfMove()
        Unknown9016(1)
        Unknown23022(1)
        Unknown4009(3)

        def upon_LANDING():
            Unknown1084(1)
            Unknown8000(104, 1, 1)
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        Unknown23078(1)
    sprite('ko205_00', 3)	# 1-3
    teleportRelativeY(10000)
    physicsXImpulse(5000)
    physicsYImpulse(18000)
    setGravity(1800)
    Unknown2053(1)
    sprite('ko205_01', 3)	# 4-6
    sprite('ko205_00', 3)	# 7-9
    sprite('ko205_03', 4)	# 10-13
    SFX_3('slash_rapier_middle')
    sprite('ko205_04', 4)	# 14-17	 **attackbox here**
    GFX_1('koef_firewing', 0)
    sprite('ko205_04', 1)	# 18-18	 **attackbox here**
    sprite('ko205_04', 1)	# 19-19	 **attackbox here**
    sprite('ko205_06', 2)	# 20-21	 **attackbox here**
    Unknown23054('6b6f3230355f303500000000000000000000000000000000000000000000000005000000')
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko205_06', 1)	# 22-22	 **attackbox here**
    sprite('ko205_06', 1)	# 23-23	 **attackbox here**
    sprite('ko205_07', 4)	# 24-27
    GFX_1('koef_firewing', 0)
    sprite('ko205_08', 4)	# 28-31
    GFX_1('koef_firewing', 0)
    sprite('ko205_09', 4)	# 32-35
    GFX_1('koef_firewing', 0)
    sprite('ko205_10', 4)	# 36-39
    GFX_1('koef_firewing', 0)
    sprite('ko205_11', 4)	# 40-43
    sprite('ko205_12', 4)	# 44-47
    sprite('ko205_11', 4)	# 48-51
    sprite('ko205_12', 4)	# 52-55
    sprite('ko205_11', 4)	# 56-59
    sprite('ko205_12', 4)	# 60-63
    sprite('ko205_11', 4)	# 64-67
    sprite('ko205_12', 4)	# 68-71
    sprite('ko205_11', 4)	# 72-75
    sprite('ko205_12', 4)	# 76-79
    sprite('ko205_11', 4)	# 80-83
    sprite('ko205_12', 4)	# 84-87
    sprite('ko205_11', 4)	# 88-91
    sprite('ko205_12', 4)	# 92-95
    sprite('ko205_11', 4)	# 96-99
    sprite('ko205_12', 4)	# 100-103
    sprite('ko205_11', 4)	# 104-107
    sprite('ko205_12', 4)	# 108-111
    label(580)
    sprite('keep', 32767)	# 112-32878
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaCrushAttack():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff00000000807be1ff80841e00807be1ff80841e00')
        callSubroutine('PYU_AttackInit')
        AttackDefaults_StandingNormal()
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown4007(3)
        DisableAttackRestOfMove()
        Unknown9016(1)
        Unknown23022(1)
        Unknown4009(3)
        Unknown2006()
        Unknown23078(1)
    sprite('ko206_03', 1)	# 1-1	 **attackbox here**
    GFX_1('koef_firewing', 0)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    SFX_3('slash_sword_middle')
    sprite('ko206_03', 1)	# 2-2	 **attackbox here**
    Unknown1018()
    Unknown1023()
    Unknown1038()
    sprite('ko206_03', 1)	# 3-3	 **attackbox here**
    sprite('ko206_04', 1)	# 4-4	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko206_04', 1)	# 5-5	 **attackbox here**
    sprite('ko206_04', 1)	# 6-6	 **attackbox here**
    sprite('ko206_05', 1)	# 7-7	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko206_05', 1)	# 8-8	 **attackbox here**
    sprite('ko206_05', 1)	# 9-9	 **attackbox here**
    sprite('ko206_06', 4)	# 10-13
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown8000(104, 1, 0)
    sprite('ko206_07', 3)	# 14-16
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    sprite('ko206_08', 3)	# 17-19
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko206_09', 3)	# 20-22
    sprite('ko206_10', 3)	# 23-25
    label(580)
    sprite('keep', 32767)	# 26-32792
    enterState('PersonaDeleteAndIdling')

@State
def PYU_Crash_Rush():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        Unknown17003()
        Unknown9016(1)
        DisableAttackRestOfMove()
        Unknown23022(1)
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        EnableCollision(0)
    sprite('ko405_00', 2)	# 1-2
    sprite('ko405_01', 2)	# 3-4
    sprite('ko405_02', 2)	# 5-6
    sprite('ko405_03', 2)	# 7-8
    sprite('ko405_04', 2)	# 9-10
    sprite('ko405_05', 1)	# 11-11
    sprite('ko405_06', 1)	# 12-12
    SFX_3('airbackdash_l')
    physicsXImpulse(10000)
    sprite('ko405_07', 2)	# 13-14
    Unknown1019(200)
    sprite('ko405_08', 2)	# 15-16
    Unknown1019(200)
    sprite('ko405_09', 3)	# 17-19	 **attackbox here**
    GFX_0('firebard', 100)
    SFX_3('airdash_m')
    SFX_3('blaze_normal')
    Unknown1019(110)
    sprite('ko405_10', 3)	# 20-22	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_09', 3)	# 23-25	 **attackbox here**
    SFX_3('airdash_m')
    SFX_3('blaze_long')
    Unknown1019(110)
    sprite('ko405_10', 3)	# 26-28	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_09', 3)	# 29-31	 **attackbox here**
    SFX_3('airdash_m')
    SFX_3('blaze_long')
    Unknown1019(110)
    sprite('ko405_10', 3)	# 32-34	 **attackbox here**
    Unknown1019(110)
    sprite('ko405_09', 3)	# 35-37	 **attackbox here**
    SFX_3('airdash_m')
    SFX_3('blaze_long')
    Unknown1019(110)
    sprite('ko405_10', 3)	# 38-40	 **attackbox here**
    sprite('ko405_09', 3)	# 41-43	 **attackbox here**
    sprite('ko405_10', 3)	# 44-46	 **attackbox here**
    sprite('ko405_09', 3)	# 47-49	 **attackbox here**
    sprite('ko405_10', 3)	# 50-52	 **attackbox here**
    sprite('ko405_09', 3)	# 53-55	 **attackbox here**
    sprite('ko405_10', 3)	# 56-58	 **attackbox here**
    sprite('ko405_09', 3)	# 59-61	 **attackbox here**
    sprite('ko405_10', 3)	# 62-64	 **attackbox here**
    sprite('keep', 32767)	# 65-32831
    enterState('PersonaDeleteAndIdling')

@State
def PYU_Persona5C_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000080841e000000000000000000')
        callSubroutine('PYU_AttackInit')
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(300)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown9016(1)
        GroundedHitstunAnimation(10)
        AirPushbackX(2500)
        AirPushbackY(35000)
        Unknown11057(500)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11092(1)
        Unknown11042(1)
        callSubroutine('PYU_CheckWarp')
        Unknown2006()
        EnableCollision(1)

        def upon_11():
            SLOT_51 = 1
        Unknown23078(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_19 <= 150000):
                sendToLabel(1)
        Unknown23059(1)
    sprite('ko206_00', 3)	# 1-3
    physicsXImpulse(20000)
    SFX_0('airdash_m')
    sprite('ko206_01', 3)	# 4-6
    physicsXImpulse(30000)
    sprite('ko206_00', 3)	# 7-9
    Unknown1019(100)
    label(1)
    sprite('ko206_01', 2)	# 10-11
    clearUponHandler(3)
    sprite('ko206_01', 2)	# 12-13
    sprite('ko206_00', 2)	# 14-15
    sprite('ko206_02', 2)	# 16-17
    sprite('ko206_03', 1)	# 18-18	 **attackbox here**
    sprite('ko206_03', 1)	# 19-19	 **attackbox here**
    GFX_1('koef_firewing', 0)
    RefreshMultihit()
    Unknown1019(20)
    SFX_0('slash_sword_middle')
    sprite('ko206_03', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_03', 1)	# 21-21	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_04', 1)	# 22-22	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    Unknown1019(40)
    sprite('ko206_04', 1)	# 23-23	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_04', 1)	# 24-24	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_05', 1)	# 25-25	 **attackbox here**
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    RefreshMultihit()
    Unknown1019(40)
    sprite('ko206_05', 1)	# 26-26	 **attackbox here**
    RefreshMultihit()
    sprite('ko206_05', 1)	# 27-27	 **attackbox here**
    RefreshMultihit()
    if SLOT_51:
        Unknown23029(2, 106, 0)
        clearUponHandler(11)
    sprite('ko206_06', 3)	# 28-30
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(20)
    Unknown8000(104, 1, 0)
    sprite('ko206_07', 3)	# 31-33
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    GFX_1('koef_firewing', 2)
    Unknown1019(0)
    sprite('ko206_08', 4)	# 34-37
    GFX_1('koef_firewing', 0)
    GFX_1('koef_firewing', 1)
    sprite('ko206_09', 4)	# 38-41
    sprite('ko206_10', 2)	# 42-43
    sprite('ko206_10', 1)	# 44-44
    label(580)
    sprite('keep', 32767)	# 45-32811
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaMaharagi_TAG():

    def upon_IMMEDIATE():
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PYU_DDAttackInit')
        Unknown2010()
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown4007(2)
        Unknown4008(2)
        setInvincible(1)
        Unknown2019(500)
        Unknown23059(1)
    sprite('ko402_00', 7)	# 1-7
    physicsXImpulse(2000)
    sprite('ko402_01', 3)	# 8-10
    sprite('ko402_02', 1)	# 11-11
    SFX_0('slash_sword_slow')
    GFX_1('koef_firewing', 0)
    GFX_0('Sliding_TAG', 1)
    sprite('ko402_02', 2)	# 12-13
    Unknown23022(0)
    sprite('ko402_03', 2)	# 14-15
    GFX_1('koef_firewing', 0)
    sprite('ko402_04', 2)	# 16-17
    GFX_1('koef_firewing', 0)
    sprite('ko402_05', 2)	# 18-19
    GFX_1('koef_firewing', 0)
    sprite('ko402_06', 2)	# 20-21
    GFX_1('koef_firewing', 0)
    physicsXImpulse(0)
    sprite('ko402_07', 6)	# 22-27
    sprite('ko402_08', 6)	# 28-33
    sprite('ko402_09', 6)	# 34-39
    SLOT_10 = 0
    sprite('ko402_07', 6)	# 40-45
    sprite('ko402_08', 6)	# 46-51
    sprite('ko402_09', 6)	# 52-57
    sprite('ko402_07', 6)	# 58-63
    sprite('keep', 32767)	# 64-32830
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaAgi_TAG():

    def upon_IMMEDIATE():
        Unknown23184('03000000640000006079feff000000000000000080841e000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(37)
        AirPushbackX(2000)
        AirPushbackY(28000)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown2006()
        Unknown2053(1)
        Unknown23059(1)
    sprite('ko401_00', 4)	# 1-4
    physicsXImpulse(12000)
    sprite('ko401_01', 2)	# 5-6
    SFX_0('slash_rapier_fast')
    physicsXImpulse(12000)
    physicsYImpulse(5000)
    sprite('ko401_02', 1)	# 7-7	 **attackbox here**
    RefreshMultihit()
    sprite('ko401_02', 2)	# 8-9	 **attackbox here**
    sprite('ko401_03', 2)	# 10-11
    GFX_0('Agishot_TAG', 100)
    Unknown1019(50)
    YAccel(50)
    sprite('ko401_04', 2)	# 12-13
    sprite('ko401_05', 2)	# 14-15
    sprite('ko401_06', 2)	# 16-17
    physicsXImpulse(-15000)
    physicsYImpulse(-2000)
    sprite('ko401_07', 4)	# 18-21
    sprite('ko401_08', 4)	# 22-25
    physicsYImpulse(1000)
    sprite('ko401_09', 4)	# 26-29
    SFX_0('cloth_h')
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_10', 4)	# 30-33
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_11', 8)	# 34-41
    Unknown1019(80)
    YAccel(150)
    sprite('ko401_12', 8)	# 42-49
    sprite('ko401_13', 8)	# 50-57
    sprite('keep', 32767)	# 58-32824
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaReversalAction():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000402bfeffc0d40100402bfeff402bfeffc0d40100c0d40100')
        callSubroutine('PYU_SPAttackInit')
        callSubroutine('Init_CantCancelPersonaAction')
        EnableCollision(0)
        Unknown2006()
        callSubroutine('PYU_ForceWarp')
        Unknown4007(3)
        Unknown3032()
        Unknown3001(50)
        Unknown3004(20)
        Unknown23022(1)
        sendToLabelUpon(56, 1)

        def upon_43():
            if (SLOT_48 == 11):
                sendToLabel(1)
                Unknown3031()
        Unknown23059(1)
    sprite('ko611_00', 6)	# 1-6
    sprite('ko611_01', 6)	# 7-12
    sprite('ko611_02', 6)	# 13-18
    sprite('ko611_03', 6)	# 19-24
    label(0)
    sprite('ko611_04', 6)	# 25-30
    sprite('ko611_05', 6)	# 31-36
    sprite('ko611_06', 6)	# 37-42
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)	# 43-32809
    enterState('PersonaDeleteAndIdling')

@State
def PYU_PersonaReversalAction_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000402bfeffc0d4010000000000000000000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        callSubroutine('PYU_ForceWarp')
        callSubroutine('Init_CantCancelPersonaAction')
        Unknown2006()
        Unknown4007(3)
        Unknown3032()
        Unknown3001(50)
        Unknown3004(20)
        Unknown23022(1)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(56, 1)

        def upon_43():
            if (SLOT_48 == 11):
                sendToLabel(1)
                Unknown3031()
        Unknown23059(1)
    sprite('ko611_00', 6)	# 1-6
    sprite('ko611_01', 6)	# 7-12
    sprite('ko611_02', 6)	# 13-18
    sprite('ko611_03', 6)	# 19-24
    label(0)
    sprite('ko611_04', 6)	# 25-30
    sprite('ko611_05', 6)	# 31-36
    sprite('ko611_06', 6)	# 37-42
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)	# 43-32809
    enterState('PersonaDeleteAndIdling')

@State
def PersonaFireAttack_TAG():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000050c30000000000000000000080841e000000000000000000')
        callSubroutine('PYU_SPAttackInit')
        AttackLevel_(3)
        Damage(900)
        AttackP1(70)
        AttackP2(85)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(60)
        Hitstop(1)
        Unknown9016(1)
        AirHitstunAnimation(9)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23078(1)
        Unknown11042(1)
        callSubroutine('PYU_ForceWarp')
        Unknown2053(1)
        callSubroutine('BoosterDamageUp')
        Unknown23059(1)
    sprite('ko404_00', 4)	# 1-4
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_01', 3)	# 5-7
    physicsXImpulse(20000)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_02', 2)	# 8-9
    SFX_3('slash_rapier_fast')
    Unknown1019(120)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_03', 1)	# 10-10	 **attackbox here**
    Unknown1019(120)
    RefreshMultihit()
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_03', 1)	# 11-11	 **attackbox here**
    Unknown23022(0)
    sprite('ko404_04', 2)	# 12-13
    Unknown1019(120)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_05', 2)	# 14-15
    Unknown1019(120)
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_06', 3)	# 16-18
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_07', 3)	# 19-21
    SFX_3('bomb_m')
    SFX_3('blaze_normal')
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_08', 3)	# 22-24	 **attackbox here**
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    GFX_1('koef_404_bom', 2)
    GFX_1('koef_404_fire', 3)
    GFX_1('koef_404_fire', 4)
    GFX_1('koef_404_fire', 5)
    GFX_1('koef_404_fire', 6)
    Unknown1019(0)
    RefreshMultihit()
    Unknown11034(0)
    ProjectileDurabilityLvl(1)
    AttackLevel_(3)
    Damage(1300)
    Hitstop(6)
    Unknown23078(0)
    AirUntechableTime(60)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(8000)
    AirPushbackY(30000)
    YImpluseBeforeWallbounce(1800)
    Unknown9016(0)
    Unknown9017(1)
    Unknown9021(1)
    callSubroutine('BoosterDamageUp')
    Unknown11058('0000000000000000000000000100000000000000')
    sprite('ko404_09', 2)	# 25-26	 **attackbox here**
    GFX_1('koef_404', 0)
    GFX_1('koef_404', 1)
    sprite('ko404_08', 4)	# 27-30	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('ko404_09', 4)	# 31-34	 **attackbox here**
    sprite('ko404_08', 4)	# 35-38	 **attackbox here**
    sprite('ko404_09', 4)	# 39-42	 **attackbox here**
    sprite('ko404_08', 4)	# 43-46	 **attackbox here**
    sprite('ko404_09', 4)	# 47-50	 **attackbox here**
    sprite('ko404_08', 4)	# 51-54	 **attackbox here**
    sprite('ko404_09', 4)	# 55-58	 **attackbox here**
    sprite('ko404_08', 4)	# 59-62	 **attackbox here**
    sprite('ko404_09', 4)	# 63-66	 **attackbox here**
    sprite('ko404_08', 4)	# 67-70	 **attackbox here**
    sprite('ko404_09', 4)	# 71-74	 **attackbox here**
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')

@State
def SBagidine_fireuzuS():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 18)	# 1-18
    GFX_0('agidine_fireuzuS', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 1)	# 19-19
    GFX_0('agidine_fireuzuS', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 39)	# 20-58
    Unknown4010(0)

@State
def SBagidine_fireuzuM():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 18)	# 1-18
    GFX_0('agidine_fireuzuM', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 1)	# 19-19
    GFX_0('agidine_fireuzuM', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 39)	# 20-58
    Unknown4010(0)

@State
def SBagidine_fireuzuL():

    def upon_IMMEDIATE():
        Unknown4010(2)
        callSubroutine('BoosterDamageUp')
        Unknown23056('')
    sprite('null', 18)	# 1-18
    GFX_0('agidine_fireuzuL', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 1)	# 19-19
    GFX_0('agidine_fireuzuL', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 39)	# 20-58
    Unknown4010(0)

@State
def SBagidine_fireuzuL_TAG():

    def upon_IMMEDIATE():
        Unknown4010(2)
        callSubroutine('BoosterDamageUp')
        Unknown23056('')
    sprite('null', 18)	# 1-18
    GFX_0('agidine_fireuzuL_OD_TAG', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 1)	# 19-19
    GFX_0('agidine_fireuzuL_OD_TAG', 100)
    Unknown23029(1, 10023, 0)
    sprite('null', 39)	# 20-58
    Unknown4010(0)

@State
def reaction_sakura():

    def upon_IMMEDIATE():
        GFX_2('yuef_sakura')
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 50)	# 1-50

@Subroutine
def Init_Sensu():
    Unknown2009()
    AttackLevel_(2)
    Damage(1000)
    PushbackX(12000)
    blockstun(11)
    ProjectileDurabilityLvl(1)
    Hitstop(0)
    Unknown11001(10, 10, 10)
    Unknown53(2)
    Unknown53(1)
    Unknown9016(1)
    Unknown4061(0)
    Unknown3032()
    Unknown1096(900)
    Unknown3029(1)
    Unknown3071(3)
    Unknown3070(1)
    Unknown3072('78000000640000006400000064000000')
    Unknown3073('3c000000640000006400000064000000')
    Unknown3074('00000000ff00000000000000ff000000')
    Unknown3075('00000000ff00000000000000ff000000')
    Unknown3078(1)
    Unknown3069(2)
    Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
    sendToLabelUpon(54, 2)
    GFX_0('sensunage_sakura', 100)

@Subroutine
def Init_Sensu_StandExSignal():
    physicsXImpulse(26000)

    def upon_43():
        if (SLOT_48 == 1011):
            physicsXImpulse(35000)
        if (SLOT_48 == 1012):
            physicsXImpulse(20000)

@Subroutine
def Init_Sensu_Gravity():
    Unknown2037(0)

    def upon_CLEAR_OR_EXIT():
        Unknown2038(1)
        if (SLOT_2 >= 10):
            setGravity(1400)
            Unknown1015(-100)
        if (SLOT_23 <= 100000):
            Unknown2003(1)
        if (SLOT_12 <= 300):
            physicsXImpulse(300)
            clearUponHandler(3)

@State
def Sensu_Stand_A():

    def upon_IMMEDIATE():
        callSubroutine('Init_Sensu')
        callSubroutine('Init_Sensu_StandExSignal')
    sprite('vr_yu204_sensu01ex', 3)	# 1-3	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_yu204_sensu02', 2)	# 4-5	 **attackbox here**
    Unknown11032('90d00300702ffcffffffffffffffffff')
    sprite('vr_yu204_sensu03', 2)	# 6-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 2)	# 8-9	 **attackbox here**
    sprite('vr_yu204_sensu05', 2)	# 10-11	 **attackbox here**
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 12-14	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 15-17	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 18-20	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 21-23	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 24-26	 **attackbox here**
    SFX_3('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 1)	# 27-27
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_hitA', 100)
    ExitState()
    label(3)
    sprite('null', 1)	# 28-28
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_LandingA', 100)

@State
def Sensu_Stand_A_2nd():

    def upon_IMMEDIATE():
        callSubroutine('Init_Sensu')
        callSubroutine('Init_Sensu_StandExSignal')

        def upon_ON_HIT_OR_BLOCK():
            pass
    sprite('vr_yu204_sensu01ex', 3)	# 1-3	 **attackbox here**
    SFX_3('slash_knife_slow')
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 4-6	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 7-9	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 10-12	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 13-15	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 16-18	 **attackbox here**
    SFX_3('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 1)	# 19-19
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_hitA', 100)
    ExitState()
    label(3)
    sprite('null', 1)	# 20-20
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_LandingA', 100)

@State
def Sensu_2A():

    def upon_IMMEDIATE():
        callSubroutine('Init_Sensu')
        Unknown1072(-45000)
        Unknown1110(35000, 0)

        def upon_43():
            if (SLOT_48 == 1021):
                Unknown1072(-20000)
                Unknown1110(35000, 0)
            if (SLOT_48 == 1022):
                Unknown1072(-70000)
                Unknown1110(32000, 0)
    sprite('vr_yu204_sensu01ex', 3)	# 1-3	 **attackbox here**
    SFX_3('slash_knife_slow')
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 4-6	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 7-9	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 10-12	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 13-15	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 16-18	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 1)	# 19-19
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_hitA', 100)

@State
def Sensu_Air():

    def upon_IMMEDIATE():
        callSubroutine('Init_Sensu')
        Unknown1072(750000)
        Unknown1110(32000, 0)

        def upon_43():
            if (SLOT_48 == 1031):
                Unknown1072(740000)
                Unknown1110(35000, 0)
            if (SLOT_48 == 1032):
                Unknown1072(770000)
                Unknown1110(38000, 0)

        def upon_LANDING():
            sendToLabel(3)
    sprite('vr_yu204_sensu01', 3)	# 1-3	 **attackbox here**
    SFX_3('slash_knife_slow')
    GFX_0('sensunage_sakura', 100)
    RefreshMultihit()
    sprite('vr_yu204_sensu02', 3)	# 4-6	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 7-9	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 10-12	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 13-15	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 16-18	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_yu204_sensu02', 3)	# 19-21	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 22-24	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 25-27	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 28-30	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 31-33	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_yu204_sensu02', 3)	# 34-36	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 37-39	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 40-42	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 43-45	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 46-48	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_yu204_sensu02', 3)	# 49-51	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 52-54	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 55-57	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 58-60	 **attackbox here**
    label(10)
    sprite('vr_yu204_sensu01', 3)	# 61-63	 **attackbox here**
    RefreshMultihit()
    sprite('vr_yu204_sensu02', 3)	# 64-66	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 67-69	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 70-72	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 73-75	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(0)
    sprite('vr_yu204_sensu01', 8)	# 76-83	 **attackbox here**
    GFX_0('Sensu_jimen', 100)
    Unknown1084(1)
    Unknown3029(0)
    Unknown2001()
    Unknown23118(-1)
    Unknown1099(30)
    Unknown3004(-32)
    loopRest()
    ExitState()
    label(2)
    sprite('null', 1)	# 84-84
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_hitA', 100)
    ExitState()
    label(3)
    sprite('null', 1)	# 85-85
    GFX_1('yuef_sakura', 100)
    Unknown1084(1)
    GFX_0('Sensu_LandingA', 100)

@State
def Sensu_hitA():

    def upon_IMMEDIATE():
        Unknown53(2)
        Unknown2035(1)
        Unknown4061(0)
        Unknown3032()
        physicsYImpulse(7000)
        physicsXImpulse(-3500)
        setGravity(800)
        teleportRelativeX(100000)
    sprite('vr_yu204_03', 3)	# 1-3
    sprite('vr_yu204_04', 3)	# 4-6
    sprite('vr_yu204_05', 3)	# 7-9
    sprite('vr_yu204_06', 3)	# 10-12
    sprite('vr_yu204_03', 3)	# 13-15
    sprite('vr_yu204_04', 3)	# 16-18
    sprite('vr_yu204_05', 3)	# 19-21
    sprite('vr_yu204_06', 8)	# 22-29
    Unknown3004(-31)

@State
def Sensu_LandingA():

    def upon_IMMEDIATE():
        Unknown53(2)
        Unknown2035(1)
        Unknown4061(0)
        Unknown3032()
        physicsYImpulse(7000)
        physicsXImpulse(3500)
        setGravity(800)
    sprite('vr_yu204_03', 3)	# 1-3
    sprite('vr_yu204_04', 3)	# 4-6
    sprite('vr_yu204_05', 3)	# 7-9
    sprite('vr_yu204_06', 3)	# 10-12
    sprite('vr_yu204_03', 3)	# 13-15
    sprite('vr_yu204_04', 3)	# 16-18
    sprite('vr_yu204_05', 3)	# 19-21
    sprite('vr_yu204_06', 8)	# 22-29
    Unknown3004(-31)

@State
def sensunage_sakura():

    def upon_IMMEDIATE():
        GFX_2('yuef_nagesakura')
    sprite('null', 50)	# 1-50

@State
def sensu_sakura():

    def upon_IMMEDIATE():
        GFX_2('yuef_sakura')
    sprite('null', 50)	# 1-50

@State
def summon_sakura():

    def upon_IMMEDIATE():
        GFX_2('yuef_summon')
        Unknown4010(2)
    sprite('null', 50)	# 1-50

@State
def firebard():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown3033()
        Unknown4061(3)
        Unknown1056(2000)
        Unknown1064(2000)
        Unknown1007(380000)
        teleportRelativeX(-400000)
    label(0)
    sprite('vr_ko405_00', 2)	# 1-2
    GFX_1('koef_405_fire01', 106)
    gotoLabel(0)

@State
def firebard_yugami():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(15000)
        Unknown1096(1500)
        Unknown3004(-16)
        Unknown1100(100)
    sprite('vr_yu_yugami', 8)	# 1-8
    sprite('vr_yu_yugami', 10)	# 9-18
    Unknown3004(-26)

@State
def rinkakuaura():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4015()
        Unknown4009(2)
        Unknown3001(0)
        Unknown3026(9474192)

        def upon_43():
            if (SLOT_48 == 52):
                sendToLabel(0)
            if (SLOT_48 == 56):
                Unknown2019(4000)
    sprite('null', 3)	# 1-3
    Unknown3004(25)
    Unknown4003('797565665f3430306175726130302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4003('797565665f3430306175726130312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4003('797565665f3430306175726130322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 10-12
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 13-15
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 16-18
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 19-21
    Unknown4003('797565665f3430306175726130362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 22-24
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 25-27
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 28-30
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(999)
    sprite('null', 3)	# 31-33
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 34-36
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 37-39
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 40-42
    Unknown4003('797565665f3430306175726130362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    gotoLabel(999)
    label(0)
    sprite('null', 3)	# 43-45
    Unknown3004(-35)
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 46-48
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 49-50
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rinkakuaura_Assist():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4007(2)
        Unknown4010(2)
        Unknown4015()
        Unknown4009(2)
        Unknown3001(0)
        Unknown3026(9474192)

        def upon_43():
            if (SLOT_48 == 52):
                sendToLabel(0)
            if (SLOT_48 == 56):
                Unknown23015(2)
    sprite('null', 3)	# 1-3
    Unknown3004(25)
    Unknown4003('797565665f3430306175726130302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 4-6
    Unknown4003('797565665f3430306175726130312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 7-9
    Unknown4003('797565665f3430306175726130322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 10-13
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 14-17
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 18-21
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 4)	# 22-25
    Unknown4003('797565665f3430306175726130362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(999)
    sprite('null', 3)	# 26-28
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 29-31
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 32-34
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 35-37
    Unknown4003('797565665f3430306175726130362e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    gotoLabel(999)
    label(0)
    sprite('null', 3)	# 38-40
    Unknown3004(-35)
    Unknown4003('797565665f3430306175726130332e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 3)	# 41-43
    Unknown4003('797565665f3430306175726130342e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 2)	# 44-45
    Unknown4003('797565665f3430306175726130352e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def rinkakuaura2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        GFX_2('yuef_reversalaura')

        def upon_43():
            if (SLOT_48 == 57):
                Unknown23015(2)
    sprite('null', 180)	# 1-180

@State
def diacharge():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f3430306368617267652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('yuef_dia')
        Unknown4007(3)
        Unknown4010(2)
        Unknown4015()
        Unknown4009(2)
        Unknown3001(0)

        def upon_43():
            if (SLOT_48 == 53):
                sendToLabel(0)
            if (SLOT_48 == 58):
                Unknown23015(2)
    sprite('null', 32767)	# 1-32767
    Unknown3004(25)
    label(0)
    sprite('null', 15)	# 32768-32782
    Unknown3004(-17)

@State
def diacharge_floor():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 54):
                sendToLabel(0)
            if (SLOT_48 == 59):
                Unknown23015(2)
    label(5)
    sprite('null', 2)	# 1-2
    GFX_1('yuef_diafloor', 100)
    loopRest()
    gotoLabel(5)
    label(0)
    sprite('null', 15)	# 3-17
    Unknown3004(-17)

@Subroutine
def InitAgi():
    Unknown2010()
    AttackLevel_(3)
    Damage(900)
    Unknown9017(1)
    Unknown23089('0100000000000000000000000100000001000000000000000100000001000000')
    sendToLabelUpon(54, 580)
    Unknown1056(2000)
    Unknown2053(1)
    callSubroutine('BoosterDamageUp')

    def upon_CLEAR_OR_EXIT():
        SLOT_51 = (SLOT_51 + 1)

@State
def AgishotA():

    def upon_IMMEDIATE():
        callSubroutine('InitAgi')
        AirUntechableTime(29)
        Hitstop(7)
        AirPushbackX(6000)
        AirPushbackY(9000)
        GroundedHitstunAnimation(1)
        Unknown1007(170000)
        teleportRelativeX(450000)
        sendToLabelUpon(23, 0)

        def upon_43():
            if (SLOT_48 == 4043):
                sendToLabel(0)
    sprite('null', 5)	# 1-5
    GFX_0('agi_firering', 100)
    label(5)
    sprite('null', 35)	# 6-40
    GFX_0('agi_firering_ex', 100)
    loopRest()
    gotoLabel(5)
    label(0)
    sprite('keep', 5)	# 41-45
    Unknown36(1)
    Unknown13(25)
    Unknown35()
    GFX_0('explosion', 100)
    clearUponHandler(23)
    clearUponHandler(3)
    sprite('vr_ko401_col', 15)	# 46-60
    RefreshMultihit()
    label(580)
    clearUponHandler(54)
    clearUponHandler(43)
    sprite('null', 5)	# 61-65

@State
def AgishotB():

    def upon_IMMEDIATE():
        callSubroutine('InitAgi')
        AirUntechableTime(29)
        Hitstop(7)
        AirPushbackX(6000)
        AirPushbackY(9000)
        GroundedHitstunAnimation(1)
        Unknown1007(170000)
        teleportRelativeX(900000)
        sendToLabelUpon(24, 0)

        def upon_43():
            if (SLOT_48 == 4044):
                sendToLabel(0)
    sprite('null', 10)	# 1-10
    GFX_0('agi_firering', 100)
    label(5)
    sprite('null', 35)	# 11-45
    GFX_0('agi_firering_ex', 100)
    loopRest()
    gotoLabel(5)
    label(0)
    sprite('keep', 5)	# 46-50
    Unknown36(1)
    Unknown13(25)
    Unknown35()
    sendToLabelUpon(24, 0)
    GFX_0('explosion_2nd', 100)
    clearUponHandler(24)
    clearUponHandler(3)
    sprite('vr_ko401_col', 15)	# 51-65
    RefreshMultihit()
    label(580)
    clearUponHandler(54)
    clearUponHandler(43)
    sprite('null', 5)	# 66-70

@State
def AgishotAB():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('BoosterDamageUp')
        AttackLevel_(3)
        Damage(2000)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown9017(1)
        AirUntechableTime(29)
        AirPushbackY(17000)
        AirPushbackX(0)
        Unknown23089('0100000000000000000000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 580)
        Unknown1056(2000)
        Unknown2053(1)
        callSubroutine('BoosterDamageUp')
        Hitstop(7)
        GroundedHitstunAnimation(1)
        SLOT_52 = SLOT_23
        Unknown1086(22)
        SLOT_23 = SLOT_52
        Unknown1007(200000)

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)

        def upon_43():
            if (SLOT_48 == 4045):
                sendToLabel(0)
    sprite('null', 3)	# 1-3
    GFX_0('agi_firering', 100)
    sprite('null', 32)	# 4-35
    sendToLabelUpon(25, 0)
    label(5)
    sprite('null', 35)	# 36-70
    GFX_0('agi_firering_ex', 100)
    loopRest()
    gotoLabel(5)
    label(0)
    sprite('keep', 5)	# 71-75
    Unknown36(1)
    Unknown13(25)
    Unknown35()
    GFX_0('explosionC', 100)
    clearUponHandler(25)
    clearUponHandler(3)
    sprite('vr_ko401_col', 15)	# 76-90
    RefreshMultihit()
    label(580)
    clearUponHandler(54)
    clearUponHandler(43)
    sprite('null', 5)	# 91-95

@State
def AgishotAB2nd():

    def upon_IMMEDIATE():
        callSubroutine('InitAgi')
        Hitstop(7)
        AirUntechableTime(36)
        GroundedHitstunAnimation(1)
        Unknown1007(320000)
        SLOT_52 = SLOT_23
        Unknown1086(22)
        SLOT_23 = SLOT_52

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
        callSubroutine('BoosterDamageUp')
        sendToLabelUpon(25, 0)
    sprite('null', 35)	# 1-35
    GFX_0('agi_firering', 100)
    label(5)
    sprite('null', 35)	# 36-70
    GFX_0('agi_firering_ex', 100)
    loopRest()
    gotoLabel(5)
    label(0)
    sprite('keep', 5)	# 71-75
    Unknown36(1)
    Unknown13(25)
    Unknown35()
    GFX_0('explosion_2nd', 100)
    clearUponHandler(25)
    clearUponHandler(3)
    sprite('vr_ko401_col', 15)	# 76-90
    RefreshMultihit()
    label(580)
    clearUponHandler(54)
    clearUponHandler(43)
    sprite('null', 5)	# 91-95

@State
def agi_firering():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f3430316669726572696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('koef236_firering')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4015()
    sprite('null', 15)	# 1-15
    sprite('null', 20)	# 16-35
    Unknown3004(-10)

@State
def agi_firering_ex():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f3430316669726572696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('koef236_firering')
        Unknown4010(2)
        Unknown4015()
    sprite('null', 35)	# 1-35
    Unknown3001(36)
    Unknown3004(0)
    loopRest()

@State
def explosion():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f34303162616b752e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4015()
    sprite('null', 35)	# 1-35
    SFX_3('bomb_m')
    SFX_3('blaze_normal')
    GFX_1('koef_401baku', 100)
    GFX_0('FireYugamiA', 100)
    Unknown1099(10)
    sprite('null', 25)	# 36-60
    Unknown3004(-15)

@State
def explosionC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f34303162616b752e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4015()
        Unknown1096(1500)
    sprite('null', 35)	# 1-35
    SFX_3('bomb_m')
    SFX_3('blaze_normal')
    GFX_1('koef_401baku', 100)
    GFX_0('FireYugamiA', 100)
    Unknown1099(10)
    sprite('null', 25)	# 36-60
    Unknown3004(-15)

@State
def agi_firering_2nd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f3430316669726572696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('koef236_firering')
        Unknown4010(2)
        Unknown4015()
    sprite('null', 15)	# 1-15
    sprite('null', 20)	# 16-35
    Unknown3004(-10)

@State
def agi_firering_2nd_ex():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f3430316669726572696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('koef236_firering')
        Unknown4010(2)
        Unknown4015()
    sprite('null', 35)	# 1-35
    Unknown3001(36)
    Unknown3004(0)

@State
def explosion_2nd():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f34303162616b752e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 35)	# 1-35
    SFX_3('bomb_m')
    SFX_3('blaze_normal')
    GFX_1('koef_401baku', 100)
    GFX_0('FireYugamiA', 100)
    Unknown1099(10)
    sprite('null', 25)	# 36-60
    Unknown3004(-15)

@State
def FireYugamiA():
    sprite('keep', 5)	# 1-5
    GFX_0('fireyugamisub', 100)
    sprite('keep', 5)	# 6-10
    GFX_0('fireyugamisub', 100)
    sprite('keep', 5)	# 11-15
    GFX_0('fireyugamisub', 100)
    sprite('keep', 5)	# 16-20
    GFX_0('fireyugamisub', 100)
    sprite('keep', 5)	# 21-25
    GFX_0('fireyugamisub', 100)
    sprite('keep', 5)	# 26-30
    GFX_0('fireyugamisub', 100)

@State
def fireyugamisub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        Unknown3057(1)
        Unknown3058(14000)
        Unknown1096(900)
        Unknown3004(-13)
        Unknown1062(300, -300)
        Unknown1070(300, -300)
        Unknown1060(100)
        Unknown1068(100)
    sprite('vr_yu_yugami', 8)	# 1-8
    sprite('vr_yu_yugami', 10)	# 9-18
    Unknown3004(-26)

@Subroutine
def Init_Maragi_Sliding():
    Unknown2010()
    AttackLevel_(4)
    ProjectileDurabilityLvl(1)
    Damage(1000)
    AttackP2(100)
    Hitstop(0)
    PushbackX(10000)
    Unknown9310(10)
    Unknown9017(1)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(12000)
    HitLow(2)
    Unknown11058('0000000000000000000000000100000000000000')
    callSubroutine('BoosterDamageUp')
    Unknown23089('0100000000000000000000000100000001000000000000000100000001000000')
    sendToLabelUpon(54, 580)
    sendToLabelUpon(55, 0)
    sendToLabelUpon(11, 0)
    teleportRelativeY(0)
    Unknown2053(1)
    GFX_2('koef_slidefire04')

@State
def SlidingA():

    def upon_IMMEDIATE():
        callSubroutine('Init_Maragi_Sliding')
        physicsXImpulse(25000)

        def upon_43():
            if (SLOT_48 == 4050):

                def upon_24():
                    if (SLOT_18 >= 5):
                        clearUponHandler(24)
                        sendToLabel(0)
                    else:
                        clearUponHandler(24)
            SLOT_5 = (SLOT_5 + 1)

        def upon_CLEAR_OR_EXIT():
            if CheckInput(0xb):
                if (SLOT_18 >= 5):
                    clearUponHandler(3)
                    sendToLabel(0)
    sprite('vr_ko402_col', 5)	# 1-5
    teleportRelativeX(50000)
    SFX_3('airdash_l')
    RefreshMultihit()
    sprite('vr_ko402_col', 10)	# 6-15
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 10)	# 16-25
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 10)	# 26-35
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 10)	# 36-45
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 10)	# 46-55
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 10)	# 56-65
    SFX_3('blaze_normal')
    loopRest()
    label(0)
    sprite('keep', 3)	# 66-68
    clearUponHandler(3)
    clearUponHandler(11)
    clearUponHandler(55)
    clearUponHandler(54)
    clearUponHandler(24)
    clearUponHandler(25)
    Unknown3004(-25)
    DisableAttackRestOfMove()
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fire', 100)
    ExitState()
    label(580)
    sprite('keep', 20)	# 69-88
    clearUponHandler(3)
    clearUponHandler(11)
    clearUponHandler(55)
    clearUponHandler(54)
    clearUponHandler(23)
    physicsXImpulse(10000)
    Unknown3004(-20)
    DisableAttackRestOfMove()
    SLOT_5 = (SLOT_5 + (-1))

@State
def SlidingB():

    def upon_IMMEDIATE():
        callSubroutine('Init_Maragi_Sliding')
        physicsXImpulse(60000)
        Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 4060):

                def upon_23():
                    if (SLOT_18 >= 5):
                        clearUponHandler(23)
                        sendToLabel(0)
                    else:
                        clearUponHandler(23)
            SLOT_5 = (SLOT_5 + 1)

        def upon_CLEAR_OR_EXIT():
            if CheckInput(0x2):
                if (SLOT_18 >= 5):
                    clearUponHandler(3)
                    sendToLabel(0)
    sprite('vr_ko402_col', 2)	# 1-2
    teleportRelativeX(50000)
    SFX_3('airdash_l')
    RefreshMultihit()
    sprite('vr_ko402_col', 5)	# 3-7
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 5)	# 8-12
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 5)	# 13-17
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 5)	# 18-22
    SFX_3('blaze_normal')
    loopRest()
    label(0)
    sprite('keep', 1)	# 23-23
    clearUponHandler(3)
    clearUponHandler(11)
    clearUponHandler(55)
    clearUponHandler(54)
    clearUponHandler(23)
    clearUponHandler(25)
    Unknown3004(-50)
    DisableAttackRestOfMove()
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fireB', 100)
    Unknown23029(1, 4061, 0)
    if SLOT_51:
        Unknown21007(1, 32)
    ExitState()
    label(580)
    sprite('keep', 5)	# 24-28
    clearUponHandler(3)
    clearUponHandler(11)
    clearUponHandler(55)
    clearUponHandler(54)
    clearUponHandler(24)
    physicsXImpulse(10000)
    Unknown3004(-20)
    DisableAttackRestOfMove()
    SLOT_5 = (SLOT_5 + (-1))

@State
def SlidingC():

    def upon_IMMEDIATE():
        callSubroutine('Init_Maragi_Sliding')
        Unknown30065(0)
        MinimumDamagePct(10)
        physicsXImpulse(60000)
        AirPushbackX(3000)
        Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 4071):

                def upon_25():
                    if (SLOT_18 >= 5):
                        clearUponHandler(25)
                        sendToLabel(0)
                    else:
                        clearUponHandler(25)

        def upon_CLEAR_OR_EXIT():
            if CheckInput(0x14):
                if (SLOT_18 >= 5):
                    clearUponHandler(3)
                    sendToLabel(0)
        SLOT_5 = (SLOT_5 + 1)
    sprite('vr_ko402_col', 5)	# 1-5
    teleportRelativeX(50000)
    SFX_3('airdash_l')
    RefreshMultihit()
    sprite('vr_ko402_col', 5)	# 6-10
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 5)	# 11-15
    SFX_3('blaze_normal')
    sprite('vr_ko402_col', 5)	# 16-20
    SFX_3('blaze_normal')
    label(0)
    sprite('null', 10)	# 21-30
    Unknown1019(0)
    clearUponHandler(3)
    clearUponHandler(11)
    clearUponHandler(55)
    clearUponHandler(54)
    clearUponHandler(25)
    Unknown3004(-50)
    DisableAttackRestOfMove()
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fireC', 100)
    sprite('null', 10)	# 31-40
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fireC', 100)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    sprite('null', 10)	# 41-50
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fireC', 100)
    Unknown23029(1, 4061, 0)
    Unknown36(1)
    teleportRelativeX(320000)
    Unknown35()
    if (SLOT_5 == 1):
        SLOT_5 = (SLOT_5 + (-1))
    ExitState()
    label(580)
    sprite('keep', 5)	# 51-55
    clearUponHandler(3)
    clearUponHandler(11)
    clearUponHandler(55)
    clearUponHandler(54)
    clearUponHandler(25)
    physicsXImpulse(10000)
    Unknown3004(-20)
    DisableAttackRestOfMove()
    SLOT_5 = (SLOT_5 + (-1))

@State
def Sliding_TAG():

    def upon_IMMEDIATE():
        DisableAttackRestOfMove()
        physicsXImpulse(40000)
        Unknown2053(1)
    sprite('null', 5)	# 1-5
    sprite('null', 10)	# 6-15
    Unknown1019(0)
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fire_TAG', 100)
    sprite('null', 10)	# 16-25
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fire_TAG', 100)
    Unknown36(1)
    teleportRelativeX(160000)
    Unknown35()
    sprite('null', 10)	# 26-35
    GFX_0('FireYugamiC', 100)
    GFX_0('Maharagi_fire_TAG', 100)
    Unknown23029(1, 4073, 0)
    Unknown36(1)
    teleportRelativeX(320000)
    Unknown35()

@State
def Maharagi_fire():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown9017(1)
        ProjectileDurabilityLvl(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(5000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(1800)
        callSubroutine('BoosterDamageUp')
        Unknown3032()
        Unknown4003('797565665f343331686962617368697261432e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('koef_431baku')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3004(45)
        Unknown1064(100)
        Unknown2053(1)
        Unknown1088(10)
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    StartMultihit()
    sprite('vr_yu431_dmg04', 30)	# 10-39	 **attackbox here**
    SFX_3('blaze_long')
    Unknown1067(0)
    RefreshMultihit()
    sprite('vr_yu431_dmg04', 10)	# 40-49	 **attackbox here**
    clearUponHandler(43)
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown23118(-65536)
    Unknown3004(-25)
    if (SLOT_5 == 1):
        SLOT_5 = (SLOT_5 + (-1))

@State
def Maharagi_fireB():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown9017(1)
        ProjectileDurabilityLvl(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(10000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(1800)
        callSubroutine('BoosterDamageUp')
        Unknown3032()
        Unknown4003('797565665f343331686962617368697261432e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('koef_431baku')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3004(45)
        Unknown1064(100)
        Unknown2053(1)
        Unknown1088(10)
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    StartMultihit()
    sprite('vr_yu431_dmg04', 45)	# 10-54	 **attackbox here**
    SFX_3('blaze_long')
    Unknown1067(0)
    RefreshMultihit()
    sprite('vr_yu431_dmg04', 10)	# 55-64	 **attackbox here**
    clearUponHandler(43)
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown23118(-65536)
    Unknown3004(-25)
    if (SLOT_5 == 1):
        SLOT_5 = (SLOT_5 + (-1))

@State
def Maharagi_fireC():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(85)
        Unknown30065(0)
        MinimumDamagePct(10)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown9017(1)
        ProjectileDurabilityLvl(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(12000)
        AirPushbackY(17000)
        YImpluseBeforeWallbounce(1800)
        callSubroutine('BoosterDamageUp')
        Unknown11092(1)
        Unknown23182(2)
        Unknown3032()
        Unknown4003('797565665f343331686962617368697261432e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('koef_431baku')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3004(45)
        Unknown1064(100)
        Unknown2053(1)
        Unknown1088(10)

        def upon_43():
            if (SLOT_48 == 4061):
                AirPushbackX(3000)
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    StartMultihit()
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    SFX_3('blaze_long')
    Unknown1067(0)
    RefreshMultihit()
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    clearUponHandler(43)
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown23118(-65536)
    Unknown3004(-25)

@State
def Maharagi_fire_TAG():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1000)
        Hitstop(0)
        AirUntechableTime(45)
        Unknown9017(1)
        ProjectileDurabilityLvl(1)
        AirHitstunAnimation(17)
        GroundedHitstunAnimation(17)
        AirPushbackX(12000)
        AirPushbackY(25000)
        YImpluseBeforeWallbounce(1800)
        callSubroutine('BoosterDamageUp')

        def upon_43():
            if (SLOT_48 == 4073):
                AirPushbackX(0)
        Unknown3032()
        Unknown4003('797565665f343331686962617368697261432e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('koef_431baku')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown3004(45)
        Unknown1064(100)
        Unknown2053(1)
        Unknown1088(10)
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    StartMultihit()
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    SFX_3('blaze_long')
    Unknown1067(0)
    RefreshMultihit()
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    clearUponHandler(43)
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown23118(-65536)
    Unknown3004(-25)

@State
def FireYugamiC():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('keep', 10)	# 1-10
    GFX_0('fireyugamisubC', 100)
    sprite('keep', 10)	# 11-20
    GFX_0('fireyugamisubC', 100)
    sprite('keep', 10)	# 21-30
    GFX_0('fireyugamisubC', 100)
    sprite('keep', 5)	# 31-35
    Unknown3004(-60)

@State
def fireyugamisubC():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(19000)
        Unknown1096(1800)
        Unknown1062(-200, -300)
        Unknown1070(500, -500)
        Unknown1060(20)
        Unknown1068(380)
    sprite('vr_yu_yugami', 15)	# 1-15
    sprite('vr_yu_yugami', 13)	# 16-28
    Unknown3004(-20)

@State
def fire_booster():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f343033617572612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown1096(1200)
        Unknown4015()
        Unknown4007(3)
    sprite('null', 15)	# 1-15
    GFX_2('yuef_403boost')
    sprite('null', 10)	# 16-25
    Unknown3004(-26)

@State
def agidine_firering():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('797565665f3433306669726572696e672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4015()
        Unknown1007(300000)
        Unknown3001(0)
    sprite('null', 10)	# 1-10
    Unknown3004(25)
    Unknown1067(70)
    GFX_0('firering_sub', 100)
    sprite('null', 32)	# 11-42
    GFX_0('firering_sub2', 100)
    sprite('null', 10)	# 43-52
    Unknown3004(-26)

@State
def firering_sub():

    def upon_IMMEDIATE():
        GFX_2('koef_430firering')
    sprite('null', 32)	# 1-32
    GFX_0('FireYugamiB2', 100)
    Unknown1067(20)
    sprite('null', 30)	# 33-62
    Unknown3004(-9)

@State
def firering_sub2():

    def upon_IMMEDIATE():
        GFX_2('koef_430firering')
    sprite('null', 32)	# 1-32
    GFX_0('FireYugamiB2', 100)
    Unknown1067(20)
    sprite('null', 30)	# 33-62
    Unknown3004(-9)

@Subroutine
def Init_AgiDine_AtkData():
    Unknown2011()
    AttackLevel_(5)
    AttackP1(70)
    AttackP2(70)
    AirUntechableTime(60)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(75000)
    AirPushbackY(35000)
    Hitstop(7)
    Unknown11001(0, 7, 0)
    Unknown9017(1)
    Unknown9346(0)
    Unknown9178(1)
    WallbounceReboundTime(10)
    Unknown11057(0)
    Unknown23182(2)

@State
def agidine_fireuzuS():

    def upon_IMMEDIATE():
        callSubroutine('Init_AgiDine_AtkData')
        Damage(1400)
        Hitstop(7)
        Unknown3032()
        Unknown4003('797565665f34333066697265757a752e44494700000000000000000000000000797565665f34333066697265757a755f3030302e6d6d6f740000000000000000')
        Unknown23067('koef_430firecore')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown1096(900)
        physicsXImpulse(70000)

        def upon_43():
            if (SLOT_48 == 10023):
                Hitstop(0)
                AirPushbackY(25000)
                MinimumDamagePct(20)
    sprite('vr_ko430_col', 2)	# 1-2
    GFX_0('FireYugamiB1s', 100)
    GFX_1('koef_430firecoresub', 100)
    SFX_3('bomb_s')
    Unknown3004(25)
    RefreshMultihit()
    sprite('vr_ko430_col', 1)	# 3-3
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 4-4
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 5-5
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 6-6
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 7-7
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 8-9
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 10-11
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 12-13
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 14-16
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 17-19
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 20-22
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 23-25
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 10)	# 26-35
    GFX_1('koef_430firecoresub', 100)
    sprite('null', 10)	# 36-45
    Unknown3004(-26)

@State
def agidine_fireuzuM():

    def upon_IMMEDIATE():
        Unknown23056('')
        callSubroutine('Init_AgiDine_AtkData')
        Damage(2200)
        Hitstop(7)
        callSubroutine('BoosterDamageUp')
        Unknown3032()
        Unknown4003('797565665f34333066697265757a752e44494700000000000000000000000000797565665f34333066697265757a755f3030302e6d6d6f740000000000000000')
        Unknown23067('koef_430firecore')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown1096(1200)
        physicsXImpulse(65000)

        def upon_43():
            if (SLOT_48 == 10023):
                Hitstop(0)
                AirPushbackY(25000)
                MinimumDamagePct(20)
    sprite('vr_ko430_col', 2)	# 1-2
    GFX_0('FireYugamiB1m', 100)
    GFX_0('430firecoresub_m', 100)
    SFX_3('bomb_m')
    Unknown3004(25)
    RefreshMultihit()
    sprite('vr_ko430_col', 1)	# 3-3
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 4-4
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 5-5
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 6-6
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 7-7
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 8-9
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 10-11
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 12-13
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 14-16
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 17-19
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 20-22
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 23-25
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 10)	# 26-35
    GFX_1('koef_430firecoresub', 100)
    sprite('null', 10)	# 36-45
    Unknown3004(-26)

@State
def agidine_fireuzuL():

    def upon_IMMEDIATE():
        Unknown23056('')
        callSubroutine('Init_AgiDine_AtkData')
        Damage(3200)
        Hitstop(16)
        callSubroutine('BoosterDamageUp')
        Unknown3032()
        Unknown4003('797565665f34333066697265757a75322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('koef_430firecore')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(0)
        Unknown1096(1500)
        physicsXImpulse(60000)

        def upon_43():
            if (SLOT_48 == 10023):
                Hitstop(0)
                AirPushbackY(25000)
                MinimumDamagePct(20)
    sprite('vr_ko430_col', 2)	# 1-2
    GFX_0('FireYugamiB1l', 100)
    GFX_0('430firecoresub_l', 100)
    SFX_3('bomb_l')
    Unknown3004(25)
    RefreshMultihit()
    sprite('vr_ko430_col', 1)	# 3-3
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 4-4
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 5-5
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 6-6
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 1)	# 7-7
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 8-9
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 10-11
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 2)	# 12-13
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 14-16
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 17-19
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 20-22
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 3)	# 23-25
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_col', 10)	# 26-35
    GFX_1('koef_430firecoresub', 100)
    sprite('null', 10)	# 36-45
    Unknown3004(-26)

@State
def agidine_fireuzuL_TAG():

    def upon_IMMEDIATE():
        Unknown23056('')
        callSubroutine('Init_AgiDine_AtkData')
        Damage(2000)
        Hitstop(16)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        Unknown3032()
        Unknown4003('797565665f34333066697265757a752e44494700000000000000000000000000797565665f34333066697265757a755f3030302e6d6d6f740000000000000000')
        Unknown23067('koef_430firecore')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(50)
        Unknown1096(1200)
        physicsXImpulse(65000)
    sprite('vr_ko430_DUO_col', 2)	# 1-2
    GFX_0('FireYugamiB1l', 100)
    GFX_0('430firecoresub_l', 100)
    SFX_3('bomb_l')
    Unknown3004(25)
    RefreshMultihit()
    sprite('vr_ko430_DUO_col', 1)	# 3-3
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 4-4
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 5-5
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 6-6
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 7-7
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 2)	# 8-9
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 2)	# 10-11
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 2)	# 12-13
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 14-16
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 17-19
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 20-22
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 23-25
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 10)	# 26-35
    GFX_1('koef_430firecoresub', 100)
    sprite('null', 10)	# 36-45
    Unknown3004(-26)

@State
def agidine_fireuzuL_OD_TAG():

    def upon_IMMEDIATE():
        Unknown23056('')
        callSubroutine('Init_AgiDine_AtkData')
        Damage(2500)
        Hitstop(16)
        AttackP2(100)
        MinimumDamagePct(100)
        AttackP1(100)
        Unknown3032()
        Unknown4003('797565665f34333066697265757a75322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('koef_430firecore')
        Unknown23015(1)
        Unknown4015()
        Unknown3001(50)
        Unknown1096(1500)
        physicsXImpulse(60000)
    sprite('vr_ko430_DUO_col', 2)	# 1-2
    GFX_0('FireYugamiB1l', 100)
    GFX_0('430firecoresub_l', 100)
    SFX_3('bomb_l')
    Unknown3004(25)
    RefreshMultihit()
    sprite('vr_ko430_DUO_col', 1)	# 3-3
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 4-4
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 5-5
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 6-6
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 1)	# 7-7
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 2)	# 8-9
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 2)	# 10-11
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 2)	# 12-13
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 14-16
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 17-19
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 20-22
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 3)	# 23-25
    GFX_1('koef_430firecoresub', 100)
    sprite('vr_ko430_DUO_col', 10)	# 26-35
    GFX_1('koef_430firecoresub', 100)
    sprite('null', 10)	# 36-45
    Unknown3004(-26)

@State
def __430firecoresub_m():

    def upon_IMMEDIATE():
        Unknown23067('koef_430firecoresub')
        Unknown4007(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        Unknown1096(1200)
    sprite('null', 25)	# 1-25
    sprite('null', 8)	# 26-33
    Unknown3004(-35)

@State
def __430firecoresub_l():

    def upon_IMMEDIATE():
        Unknown23067('koef_430firecoresub')
        Unknown4007(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        Unknown1096(1400)
    sprite('null', 25)	# 1-25
    sprite('null', 8)	# 26-33
    Unknown3004(-35)

@State
def FireYugamiB1s():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('keep', 10)	# 1-10
    GFX_0('fireyugamisubB1s', 100)
    loopRest()
    gotoLabel(0)

@State
def FireYugamiB1m():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('keep', 10)	# 1-10
    GFX_0('fireyugamisubB1m', 100)
    loopRest()
    gotoLabel(0)

@State
def FireYugamiB1l():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('keep', 10)	# 1-10
    GFX_0('fireyugamisubB1l', 100)
    loopRest()
    gotoLabel(0)

@State
def fireyugamisubB1s():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(30000)
        Unknown1096(1200)
        Unknown1062(400, -400)
        Unknown1070(400, -400)
        Unknown1060(200)
        Unknown1068(200)
    sprite('vr_yu_yugami', 6)	# 1-6
    sprite('vr_yu_yugami', 6)	# 7-12
    Unknown3004(-50)

@State
def fireyugamisubB1m():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(30000)
        Unknown1096(1400)
        Unknown1062(400, -400)
        Unknown1070(400, -400)
        Unknown1060(300)
        Unknown1068(300)
    sprite('vr_yu_yugami', 6)	# 1-6
    sprite('vr_yu_yugami', 6)	# 7-12
    Unknown3004(-50)

@State
def fireyugamisubB1l():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(30000)
        Unknown1096(1700)
        Unknown1062(400, -400)
        Unknown1070(400, -400)
        Unknown1060(400)
        Unknown1068(400)
    sprite('vr_yu_yugami', 6)	# 1-6
    sprite('vr_yu_yugami', 6)	# 7-12
    Unknown3004(-50)

@State
def FireYugamiB2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 5)
    label(0)
    sprite('keep', 8)	# 1-8
    GFX_0('fireyugamisubB2', 100)
    loopRest()
    gotoLabel(0)
    label(5)
    sprite('keep', 5)	# 9-13
    Unknown3004(-60)

@State
def fireyugamisubB2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(19000)
        Unknown1096(2200)
        Unknown3004(-13)
        Unknown1062(400, -400)
        Unknown1070(400, -400)
        Unknown1060(80)
        Unknown1068(80)
    sprite('vr_yu_yugami', 9)	# 1-9
    Unknown3004(-30)

@Subroutine
def Maharagidine_AtkData():
    Unknown2011()
    Unknown23056('')
    AttackLevel_(5)
    Damage(800)
    MinimumDamagePct(15)
    AttackP2(60)
    AirUntechableTime(40)
    Hitstop(0)
    GroundedHitstunAnimation(1)
    PushbackX(-39900)
    AirPushbackY(11000)
    Unknown9021(1)
    Unknown9017(1)
    Unknown23182(2)
    Unknown11092(1)
    Unknown11110(88)
    Unknown3032()
    Unknown4003('797565665f343331686962617368697261432e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23067('koef_431baku')
    Unknown23015(1)
    Unknown4015()
    Unknown3001(0)
    Unknown3004(45)
    Unknown1064(100)
    Unknown1056(1200)
    Unknown1088(10)
    callSubroutine('BoosterDamageUp')

@State
def MaharagidineC_fire():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown2003(1)
    sprite('null', 10)	# 1-10
    Unknown23024(1)
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    sprite('null', 10)	# 11-20
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    sprite('null', 10)	# 21-30
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    sprite('null', 10)	# 31-40
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    sprite('null', 10)	# 41-50
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    sprite('null', 10)	# 51-60
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    sprite('null', 10)	# 61-70
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    sprite('null', 10)	# 71-80
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    sprite('null', 10)	# 81-90
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    sprite('null', 10)	# 91-100
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    sprite('null', 10)	# 101-110
    GFX_0('MaharagidineC_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    GFX_0('MaharagidineC_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    sprite('null', 30)	# 111-140

@State
def MaharagidineC_Frontfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        AirPushbackX(18000)
        Unknown30055('a08601003200000032000000')
        PushbackX(39900)
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineC_Backfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        AirPushbackX(-18000)
        Unknown30055('6079feff3200000032000000')
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineD_fire():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown2003(1)
    sprite('null', 10)	# 1-10
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    sprite('null', 10)	# 11-20
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    sprite('null', 10)	# 21-30
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    sprite('null', 10)	# 31-40
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    sprite('null', 10)	# 41-50
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    sprite('null', 10)	# 51-60
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    sprite('null', 10)	# 61-70
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    sprite('null', 10)	# 71-80
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    sprite('null', 10)	# 81-90
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    sprite('null', 10)	# 91-100
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    sprite('null', 10)	# 101-110
    GFX_0('MaharagidineD_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    GFX_0('MaharagidineD_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    sprite('null', 30)	# 111-140
    clearUponHandler(3)

@State
def MaharagidineD_Frontfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        Unknown30055('6079feff3200000032000000')
        AirPushbackX(-18000)
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineD_Backfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        Unknown30055('a08601003200000032000000')
        AirPushbackX(18000)
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineOD_C_fire():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown2003(1)
    sprite('null', 10)	# 1-10
    Unknown23024(1)
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    sprite('null', 10)	# 11-20
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    sprite('null', 10)	# 21-30
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    sprite('null', 10)	# 31-40
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    sprite('null', 10)	# 41-50
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    sprite('null', 10)	# 51-60
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    sprite('null', 10)	# 61-70
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    sprite('null', 10)	# 71-80
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    sprite('null', 10)	# 81-90
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    sprite('null', 10)	# 91-100
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    sprite('null', 10)	# 101-110
    GFX_0('MaharagidineOD_C_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    GFX_0('MaharagidineOD_C_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    sprite('null', 30)	# 111-140

@State
def MaharagidineOD_C_Frontfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        Damage(1000)
        callSubroutine('BoosterDamageUp')
        AirPushbackX(18000)
        Unknown30055('a08601003200000032000000')
        PushbackX(39900)
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineOD_C_Backfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        Damage(1000)
        callSubroutine('BoosterDamageUp')
        AirPushbackX(-18000)
        Unknown30055('6079feff3200000032000000')
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineOD_D_fire():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown2003(1)
    sprite('null', 10)	# 1-10
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1650000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1650000)
    Unknown35()
    sprite('null', 10)	# 11-20
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1500000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1500000)
    Unknown35()
    sprite('null', 10)	# 21-30
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1350000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1350000)
    Unknown35()
    sprite('null', 10)	# 31-40
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1200000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown35()
    sprite('null', 10)	# 41-50
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-1050000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(1050000)
    Unknown35()
    sprite('null', 10)	# 51-60
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-900000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(900000)
    Unknown35()
    sprite('null', 10)	# 61-70
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-750000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(750000)
    Unknown35()
    sprite('null', 10)	# 71-80
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-600000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    sprite('null', 10)	# 81-90
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-450000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    sprite('null', 10)	# 91-100
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    sprite('null', 10)	# 101-110
    GFX_0('MaharagidineOD_D_Backfire_col', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    GFX_0('MaharagidineOD_D_Frontfire_col', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    if SLOT_51:
        Unknown23029(1, 10052, 0)
    GFX_0('FireYugamiD', 100)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    sprite('null', 30)	# 111-140
    clearUponHandler(3)

@State
def MaharagidineOD_D_Frontfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        Damage(1000)
        callSubroutine('BoosterDamageUp')
        Unknown30055('6079feff3200000032000000')
        AirPushbackX(-18000)
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def MaharagidineOD_D_Backfire_col():

    def upon_IMMEDIATE():
        callSubroutine('Maharagidine_AtkData')
        Damage(1000)
        Unknown30055('a08601003200000032000000')
        AirPushbackX(18000)
        DisableAttackRestOfMove()
    sprite('vr_yu431_dmg04', 9)	# 1-9	 **attackbox here**
    Unknown1067(100)
    sprite('vr_yu431_dmg04', 5)	# 10-14	 **attackbox here**
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')
    sprite('vr_yu431_dmg04', 10)	# 15-24	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown3004(-25)

@State
def FireYugamiD():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('keep', 7)	# 1-7
    GFX_0('fireyugamisubD', 100)
    sprite('keep', 7)	# 8-14
    GFX_0('fireyugamisubD', 100)
    sprite('keep', 7)	# 15-21
    GFX_0('fireyugamisubD', 100)
    sprite('keep', 5)	# 22-26
    Unknown3004(-60)

@State
def fireyugamisubD():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3057(1)
        Unknown3058(19000)
        Unknown1096(1300)
        Unknown1062(-200, -300)
        Unknown1070(500, -500)
        Unknown1060(20)
        Unknown1068(380)
    sprite('vr_yu_yugami', 12)	# 1-12
    sprite('vr_yu_yugami', 9)	# 13-21
    Unknown3004(-30)

@State
def Konohana_charge():

    def upon_IMMEDIATE():
        Unknown23067('koef_450charge')
        Unknown4007(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 8)	# 32768-32775
    Unknown3004(-35)

@State
def Konohana_egg():

    def upon_IMMEDIATE():
        Unknown23067('koef_450egg')
        Unknown4007(2)
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    label(1)
    sprite('null', 8)	# 1-8
    SFX_3('magiccircle_b')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('null', 8)	# 9-16
    SFX_3('damage_magic_mh')
    Unknown3004(-35)

@State
def Konohana_burst():

    def upon_IMMEDIATE():
        Unknown23067('koef_450sakuraburst')
        Unknown4007(2)
        Unknown2054(1)
    sprite('dmy_atk01', 80)	# 1-80
    Unknown2012()
    Damage(0)
    Hitstop(0)
    AirUntechableTime(10000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(0)
    AirPushbackY(4000)
    YImpluseBeforeWallbounce(100)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    RefreshMultihit()
    loopRest()

@State
def BurstYugami():
    sprite('vr_yu450_yugami', 1)	# 1-1
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(14000)
    label(0)
    sprite('keep', 5)	# 2-6
    Unknown1074(1000)
    Unknown1096(3000)
    Unknown1099(0)
    Unknown1062(400, -400)
    Unknown1070(400, -400)
    Unknown1063(80, -80)
    Unknown1071(80, -80)
    GFX_0('yugamisub', 100)
    loopRest()
    gotoLabel(0)

@State
def yugamisub():
    sprite('vr_yu450_yugami', 80)	# 1-80
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown3057(1)
    Unknown3058(14000)
    Unknown3004(-10)
    Unknown1025(1000, -1000)
    Unknown1026(4000, -4000)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown6001(1)
        Unknown2007()
        Unknown23015(2)
        Unknown3032()
        Unknown3001(0)
        Unknown1000(-500000)
        Unknown1007(128000)
    sprite('ichigeki', 12)	# 1-12	 **attackbox here**
    GFX_0('Cutinbg', 100)
    sprite('ichigeki', 12)	# 13-24	 **attackbox here**
    physicsXImpulse(40000)
    Unknown3004(15)
    sprite('ichigeki', 110)	# 25-134	 **attackbox here**
    physicsXImpulse(400)
    sprite('ichigeki', 20)	# 135-154	 **attackbox here**
    Unknown23119(-1, 20, 1)
    physicsXImpulse(80000)
    Unknown3004(-9)

@State
def Cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('797565665f343530637574696e62672e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown3032()
        Unknown2007()
        Unknown3001(0)
    sprite('null', 15)	# 1-15
    Unknown3004(11)
    sprite('null', 125)	# 16-140
    Unknown3004(0)
    sprite('null', 30)	# 141-170
    Unknown3004(-9)

@State
def BG_sakura():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    teleportRelativeX(300000)
    GFX_0('Sakurafubuki_storm', 100)
    Unknown36(1)
    teleportRelativeX(-800000)
    Unknown35()
    GFX_0('BGscr', 100)
    Unknown3004(20)
    sprite('null', 32767)	# 11-32777
    label(0)
    sprite('null', 26)	# 32778-32803
    Unknown3004(-10)

@State
def Sakurafubuki_slow():

    def upon_IMMEDIATE():
        GFX_2('yuef_450sakurafubuki0')
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 10)	# 32768-32777
    Unknown3004(-26)

@State
def Sakurafubuki_storm():

    def upon_IMMEDIATE():
        GFX_2('yuef_450sakurafubuki')
        Unknown3001(0)
    sprite('null', 250)	# 1-250
    Unknown3004(40)
    sprite('null', 5)	# 251-255
    GFX_0('Sakurafubuki_KO', 100)
    Unknown3004(-60)

@State
def Sakurafubuki_KO():

    def upon_IMMEDIATE():
        GFX_2('yuef_450cutinsakura02')
        Unknown3001(0)
    sprite('null', 100)	# 1-100
    Unknown3004(40)
    sprite('null', 5)	# 101-105
    Unknown3004(-60)

@State
def SakuraSE():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    label(1)
    sprite('null', 35)	# 1-35
    SFX_3('yu003')
    sprite('null', 20)	# 36-55
    SFX_3('yu003')
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('null', 1)	# 56-56

@State
def BGscr():

    def upon_IMMEDIATE():
        Unknown4003('797565665f343530424773616b7572612e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown3001(0)
    sprite('null', 250)	# 1-250
    Unknown3004(5)
    sprite('null', 5)	# 251-255
    Unknown3004(-60)

@State
def Sakuraend():

    def upon_IMMEDIATE():
        Unknown4003('797565665f343530424768696b6172692e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('yuef_450sakuraend')
    sprite('null', 32767)	# 1-32767

@State
def IchigekiBlack():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown3001(0)
        Unknown1096(5000)
        Unknown23015(2)
        Unknown4007(2)
        sendToLabelUpon(32, 0)
    sprite('vr_ko450_black', 32767)	# 1-32767
    Unknown3004(7)
    label(0)
    sprite('vr_ko450_black', 5)	# 32768-32772
    Unknown3004(-60)

@State
def IchigekiWhite():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown3001(0)
        Unknown23015(4)
        Unknown1096(5000)
        Unknown4007(2)
    sprite('vr_ko450_white', 8)	# 1-8
    Unknown3004(60)
    sprite('vr_ko450_white', 6)	# 9-14
    Unknown3004(-50)

@State
def __450flash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown3001(0)
        Unknown23015(4)
        Unknown1096(5000)
        Unknown4007(2)
    sprite('vr_ko450_white', 30)	# 1-30
    Unknown3004(15)
    sprite('vr_ko450_white', 30)	# 31-60
    Unknown3004(-9)

@State
def Ichigeki_HitEff():

    def upon_IMMEDIATE():
        Unknown1086(22)
    SLOT_51 = 25
    label(1)
    sprite('dmy_atk01', 1)	# 1-1
    Unknown2012()
    Damage(247)
    Hitstop(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(0)
    AirPushbackY(100)
    YImpluseBeforeWallbounce(0)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    Unknown23011(1)
    RefreshMultihit()
    Unknown23151(22, 105)
    Unknown4045('797565665f34353068697400000000000000000000000000000000000000000064000000')
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(10, 2, 51)
    gotoLabel(1)
    label(10)
    SLOT_51 = 25
    label(11)
    sprite('dmy_atk01', 1)	# 2-2
    Unknown2012()
    Damage(372)
    Hitstop(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(0)
    AirPushbackY(100)
    YImpluseBeforeWallbounce(0)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    Unknown23011(1)
    RefreshMultihit()
    Unknown23151(22, 105)
    Unknown4045('797565665f34353068697400000000000000000000000000000000000000000064000000')
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(20, 2, 51)
    gotoLabel(11)
    label(20)
    SLOT_51 = 140
    label(21)
    sprite('dmy_atk01', 1)	# 3-3
    Unknown2012()
    Damage(297)
    Hitstop(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(0)
    AirPushbackY(100)
    YImpluseBeforeWallbounce(0)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    Unknown23011(1)
    RefreshMultihit()
    Unknown23151(22, 105)
    Unknown4045('797565665f34353068697400000000000000000000000000000000000000000064000000')
    SLOT_51 = (SLOT_51 + (-1))
    loopRest()
    Unknown19(0, 2, 51)
    gotoLabel(21)
    label(0)
    sprite('dmy_atk00', 1)	# 4-4
    RefreshMultihit()
    Unknown2012()
    AttackLevel_(5)
    Hitstop(0)
    Damage(37564)
    MinimumDamagePct(100)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(10000)
    AirPushbackY(70000)
    YImpluseBeforeWallbounce(-1)
    Unknown11064(4)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11023(1)
    Unknown4045('797565665f34353068697400000000000000000000000000000000000000000064000000')
    sprite('null', 1)	# 5-5
    Unknown23011(15)
    Unknown36(22)
    Unknown3038(1)
    Unknown35()

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
        Unknown20001(1)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 1)	# 32768-32768
    loopRest()
    label(1)
    sprite('null', 32767)	# 32769-65535
    Unknown20000(1)
    Unknown20002(1)
    Unknown1086(3)
    Unknown20003(1)
    Unknown1000(0)
    label(2)
    sprite('null', 32767)	# 65536-98302
    Unknown1086(22)
    teleportRelativeX(-200000)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(3)
    sprite('null', 32767)	# 98303-131069
    Unknown20002(1)
    Unknown1086(3)
    Unknown20003(1)
    physicsXImpulse(5000)

@State
def __612flash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown3001(0)
        Unknown23015(4)
        Unknown1096(1000)
        Unknown4007(2)
    sprite('vr_ko450_white', 15)	# 1-15
    Unknown3004(15)
    sprite('vr_ko450_white', 10)	# 16-25
    Unknown3004(0)
    Unknown3001(235)
    sprite('vr_ko450_white', 25)	# 26-50
    Unknown3004(-10)

@State
def PersonaEntry2():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown4061(1)
        Unknown23023()
        Unknown23184('0300000064000000409c0000204e000000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2019(1000)
        Unknown4007(3)
    sprite('ko601_00', 60)	# 1-60
    sprite('ko601_01', 6)	# 61-66
    Unknown23015(0)
    Unknown2019(-500)
    sprite('ko601_02', 6)	# 67-72
    physicsXImpulse(-3000)
    sprite('ko601_03', 8)	# 73-80
    sprite('ko601_04', 10)	# 81-90
    Unknown21007(3, 32)
    sprite('ko601_05', 8)	# 91-98
    sprite('ko601_06', 8)	# 99-106
    physicsXImpulse(-2000)
    sprite('ko601_07', 8)	# 107-114
    Unknown2019(4000)
    sprite('ko601_08', 6)	# 115-120
    sprite('ko601_09', 6)	# 121-126
    physicsXImpulse(0)
    sprite('ko601_10', 6)	# 127-132
    sprite('ko601_09', 6)	# 133-138
    sprite('ko601_08', 6)	# 139-144
    sprite('ko601_09', 6)	# 145-150
    sprite('ko601_10', 6)	# 151-156
    sprite('ko601_09', 6)	# 157-162
    sprite('ko601_08', 6)	# 163-168
    sprite('ko601_09', 6)	# 169-174
    sprite('ko601_10', 6)	# 175-180
    sprite('keep', 32767)	# 181-32947
    enterState('PersonaDeleteAndIdling')

@State
def PersonaEntry_TAG():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown4061(1)
        Unknown2019(1000)
        Unknown23023()
        Unknown23184('0300000064000000409c0000204e000000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown4007(3)
    label(0)
    sprite('ko601_00', 1)	# 1-1
    sendToLabelUpon(32, 1)
    gotoLabel(0)
    label(1)
    sprite('ko601_00', 60)	# 2-61
    sprite('ko601_01', 6)	# 62-67
    Unknown23015(0)
    Unknown2019(-500)
    sprite('ko601_02', 6)	# 68-73
    physicsXImpulse(-3000)
    sprite('ko601_03', 8)	# 74-81
    sprite('ko601_04', 10)	# 82-91
    Unknown21007(3, 32)
    sprite('ko601_05', 8)	# 92-99
    sprite('ko601_06', 8)	# 100-107
    physicsXImpulse(-2000)
    sprite('ko601_07', 8)	# 108-115
    Unknown2019(4000)
    sprite('ko601_08', 6)	# 116-121
    sprite('ko601_09', 6)	# 122-127
    physicsXImpulse(0)
    sprite('ko601_10', 6)	# 128-133
    sprite('ko601_09', 6)	# 134-139
    sprite('ko601_08', 6)	# 140-145
    sprite('ko601_09', 6)	# 146-151
    sprite('ko601_10', 6)	# 152-157
    sprite('ko601_09', 6)	# 158-163
    sprite('ko601_08', 6)	# 164-169
    sprite('ko601_09', 6)	# 170-175
    sprite('ko601_10', 6)	# 176-181
    sprite('keep', 32767)	# 182-32948
    enterState('PersonaDeleteAndIdling')

@State
def PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown4061(1)
        Unknown2019(1000)
        Unknown23023()
        Unknown23184('0300000064000000402bfeffc0d4010000000000000000000000000000000000')
        callSubroutine('PYU_CheckWarp')
        Unknown2053(1)
    sprite('ko611_00', 6)	# 1-6
    sprite('ko611_01', 6)	# 7-12
    sprite('ko611_02', 6)	# 13-18
    sprite('ko611_03', 6)	# 19-24
    label(0)
    sprite('ko611_04', 8)	# 25-32
    sprite('ko611_05', 8)	# 33-40
    sprite('ko611_06', 8)	# 41-48
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

        def upon_CLEAR_OR_EXIT():
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
def Func_DS_Yarare1():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(100)
        PushbackX(1000000)
        AirHitstunAnimation(9)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown11080(0)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare1_2', -1)

@State
def Func_DS_Yarare1_2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(100)
        PushbackX(1000000)
        AirHitstunAnimation(11)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown11080(0)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare1_3', -1)

@State
def Func_DS_Yarare1_3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(100)
        PushbackX(1000000)
        AirHitstunAnimation(10)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare1_4', -1)

@State
def Func_DS_Yarare1_4():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(100)
        PushbackX(1000000)
        AirPushbackX(50000)
        AirPushbackY(15000)
        AirHitstunAnimation(12)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare1_5', -1)

@State
def Func_DS_Yarare1_5():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(100)
        PushbackX(1000000)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    GFX_0('sensunage_sakura', 100)

@State
def Func_DS_Yarare2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(9)
        Unknown11064(1)
        Unknown23151(22, 104)

        def upon_CLEAR_OR_EXIT():
            if SLOT_125:
                FreezeCount(1)
                FreezeDuration(45)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare2_2', -1)

@State
def Func_DS_Yarare2_2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(100)
        PushbackX(1000000)
        AirPushbackX(50000)
        AirPushbackY(-50000)
        GroundedHitstunAnimation(5)
        AirUntechableTime(60)
        Unknown9202(60)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown11080(0)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare2_3', -1)

@State
def Func_DS_Yarare2_3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(13)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown11080(0)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare2_4', -1)

@State
def Func_DS_Yarare2_4():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(5)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare2_5', -1)

@State
def Func_DS_Yarare2_5():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(5)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    GFX_0('sensunage_sakura', 100)

@State
def Func_DS_Yarare3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(0)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(9)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare3_2', -1)

@State
def Func_DS_Yarare3_2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(1)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(3)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare3_3', -1)

@State
def Func_DS_Yarare3_3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(2)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(3)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown11080(0)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare3_4', -1)

@State
def Func_DS_Yarare3_4():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(3)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare3_5', -1)

@State
def Func_DS_Yarare3_5():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(3)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 40)	# 17-56
    GFX_0('sensunage_sakura', 100)
    loopRest()
    GFX_0('Func_DS_Yarare3_6', -1)

@State
def Func_DS_Yarare3_6():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(100)
        PushbackX(1000000)
        GroundedHitstunAnimation(2)
        Unknown9142(60)
        Unknown9130(60)
        Unknown11064(1)
        Unknown23151(22, 104)
        Unknown53(2)
        Unknown53(1)
        Unknown9016(1)
        Unknown11080(0)
        Unknown1096(900)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(1)
        Unknown3072('78000000640000006400000064000000')
        Unknown3073('3c000000640000006400000064000000')
        Unknown3074('00000000ff00000000000000ff000000')
        Unknown3075('00000000ff00000000000000ff000000')
        Unknown3078(1)
        Unknown3069(2)
        Unknown23089('0100000001000000010000000100000001000000000000000100000001000000')
        sendToLabelUpon(54, 2)
    sprite('null', 1)	# 1-1
    teleportRelativeX(-450000)
    Unknown1007(270000)
    label(10)
    sprite('vr_yu204_sensu02', 3)	# 2-4	 **attackbox here**
    sprite('vr_yu204_sensu03', 3)	# 5-7	 **attackbox here**
    sprite('vr_yu204_sensu04', 3)	# 8-10	 **attackbox here**
    sprite('vr_yu204_sensu05', 3)	# 11-13	 **attackbox here**
    sprite('vr_yu204_sensu01', 3)	# 14-16	 **attackbox here**
    SFX_0('slash_knife_slow')
    loopRest()
    gotoLabel(10)
    label(2)
    GFX_0('sensunage_sakura', 100)