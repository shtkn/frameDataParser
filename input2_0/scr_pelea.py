@Subroutine
def ExSkillInit():
    MinimumDamagePct(10)
    Unknown30065(0)

@Subroutine
def InvSkillInit():
    Unknown30065(100)

@Subroutine
def PartnerSkillInit():
    AttackP1(70)
    Unknown11042(1)

@State
def PEL_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)
    Unknown3038(1)
    Unknown24('50454c5f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PEL_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PEL_ReceptionSignal')
    sprite('null', 32767)
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PEL_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 3001):
            Unknown23185('50454c5f506572736f6e6141737361756c74000000000000000000000000000032000000')
        if (SLOT_48 == 3005):
            Unknown23185('50454c5f506572736f6e61416e7469416972000000000000000000000000000032000000')
        if (SLOT_48 == 3006):
            Unknown23185('50454c5f506572736f6e61416e7469416972535000000000000000000000000032000000')
        if (SLOT_48 == 2001):
            Unknown23185('50454c5f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2002):
            Unknown23185('50454c5f506572736f6e6132430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2003):
            Unknown23185('50454c5f506572736f6e6135440000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2004):
            Unknown23185('50454c5f506572736f6e6132440000000000000000000000000000000000000032000000')
        if (SLOT_48 == 3003):
            Unknown23185('50454c5f506572736f6e6153686f74000000000000000000000000000000000032000000')
        if (SLOT_48 == 3004):
            Unknown23185('50454c5f506572736f6e6153686f74535000000000000000000000000000000032000000')
        if (SLOT_48 == 2005):
            Unknown23185('50454c5f506572736f6e6141697235430000000000000000000000000000000032000000')
        if (SLOT_48 == 2006):
            Unknown23185('50454c5f506572736f6e6141697235440000000000000000000000000000000032000000')
        if (SLOT_48 == 2501):
            Unknown23185('50454c5f506572736f6e6135435053000000000000000000000000000000000032000000')
        if (SLOT_48 == 2502):
            Unknown23185('50454c5f506572736f6e6153686f74505300000000000000000000000000000032000000')
        if (SLOT_48 == 2503):
            Unknown23185('50454c5f506572736f6e6153686f74505353500000000000000000000000000032000000')
        if (SLOT_48 == 2504):
            Unknown23185('50454c5f506572736f6e61416e7469416972505300000000000000000000000032000000')
        if (SLOT_48 == 2505):
            Unknown23185('50454c5f506572736f6e61416e7469416972505353500000000000000000000032000000')
        if (SLOT_48 == 4001):
            Unknown23185('50454c5f506572736f6e6141737361756c74457800000000000000000000000032000000')
        if (SLOT_48 == 4003):
            Unknown23185('50454c5f506572736f6e6153686f74457800000000000000000000000000000032000000')
        if (SLOT_48 == 4004):
            Unknown23185('50454c5f506572736f6e6153686f74457853500000000000000000000000000032000000')
        if (SLOT_48 == 4005):
            Unknown23185('50454c5f506572736f6e61416e7469416972457800000000000000000000000032000000')
        if (SLOT_48 == 4006):
            Unknown23185('50454c5f506572736f6e61416e7469416972457853500000000000000000000032000000')
        if (SLOT_48 == 4007):
            Unknown23185('50454c5f506572736f6e6143686172676553686f74457800000000000000000032000000')
        if (SLOT_48 == 4008):
            Unknown23185('50454c5f506572736f6e6143686172676553686f74457853500000000000000032000000')
        if (SLOT_48 == 4501):
            Unknown23185('50454c5f506572736f6e614c616e64547261700000000000000000000000000032000000')
        if (SLOT_48 == 4502):
            Unknown23185('50454c5f506572736f6e6141697254726170000000000000000000000000000032000000')
        if (SLOT_48 == 4503):
            Unknown23185('50454c5f506572736f6e615370656369616c4865616c0000000000000000000032000000')
        if (SLOT_48 == 5001):
            Unknown23185('50454c5f506572736f6e61556c74696d6174655468726f77000000000000000032000000')
        if (SLOT_48 == 5002):
            Unknown23185('50454c5f506572736f6e61556c74696d6174655468726f77535000000000000032000000')
        if (SLOT_48 == 5003):
            Unknown23185('50454c5f506572736f6e6144554f00000000000000000000000000000000000032000000')
        if (SLOT_48 == 5004):
            Unknown23185('50454c5f506572736f6e6144554f53500000000000000000000000000000000032000000')
        if (SLOT_48 == 6001):
            Unknown23185('50454c5f506572736f6e6141737472616c48656174000000000000000000000032000000')
        if (SLOT_48 == 9001):
            Unknown23185('506572736f6e61456e747279000000000000000000000000000000000000000032000000')
        if (SLOT_48 == 9002):
            Unknown23185('506572736f6e614d6174636857696e000000000000000000000000000000000032000000')
        if (SLOT_48 == 9003):
            Unknown23185('506572736f6e614d6174636857696e535000000000000000000000000000000032000000')
        if (SLOT_48 == 1008):
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
    EnableCollision(0)
    Unknown30041('')
    Unknown23059(1)

@Subroutine
def PEL_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PEL_AttackInit():
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
    callSubroutine('PEL_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PEL_SPAttackInit():
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
    callSubroutine('PEL_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PEL_DDAttackInit():
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
    callSubroutine('PEL_ReceptionSignal')
    Unknown23023()

@Subroutine
def PEL_CheckWarp():
    if SLOT_58:
        Unknown3001(0)
        Unknown3004(85)
        loopRelated(17, 4)

        def upon_17():
            Unknown3001(255)
            Unknown3004(0)

@Subroutine
def PEL_ForceWarp():
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
        SFX_3('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PEL_PersonaWait')

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
        callSubroutine('PEL_ReceptionSignal')
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
    EnableCollision(0)
    Unknown1084(1)

@State
def elef_cardlight():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 60)
    GFX_2('elef_cardlight')
    gotoLabel(0)

@State
def elef_cardlight_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 3)
    GFX_1('elef_cardlight_add', 100)
    gotoLabel(0)

@State
def elef121_Burst():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23067('elef_burst')
        Unknown2054(1)
    sprite('null', 60)

@State
def elef200_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vr_el200_00', 16)
    Unknown3004(-42)

@State
def elef207_all():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1074(-12500)
    sprite('null', 7)
    Unknown1096(200)
    Unknown1099(100)
    GFX_0('elef207', 100)
    Unknown36(1)
    Unknown1073(0)
    Unknown35()
    GFX_0('elef207', 100)
    Unknown36(1)
    Unknown1073(60000)
    Unknown35()
    GFX_0('elef207', 100)
    Unknown36(1)
    Unknown1073(120000)
    Unknown35()
    GFX_0('elef207', 100)
    Unknown36(1)
    Unknown1073(180000)
    Unknown35()
    GFX_0('elef207', 100)
    Unknown36(1)
    Unknown1073(240000)
    Unknown35()
    GFX_0('elef207', 100)
    Unknown36(1)
    Unknown1073(300000)
    Unknown35()
    sprite('null', 32767)
    Unknown1096(1000)
    Unknown1099(0)

@State
def elef207():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4006(2)
        Unknown4013(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vr_el207_00', 32767)

@State
def dmy_el208():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(300)
        AttackP1(100)
        AttackP2(100)
        AirUntechableTime(30)
        Hitstop(1)
        PushbackX(4500)
        AirPushbackX(100)
        AirPushbackY(5000)
        YImpluseBeforeWallbounce(250)
        Unknown9016(1)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(2)
        Unknown9130(40)
        Unknown9142(30)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')

        def upon_12():
            Unknown23029(3, 1001, 0)
            GFX_0('dmy_el208_tatsumaki', 100)
        Unknown23089('0100000001000000010000000000000000000000000000000100000000000000')
        sendToLabelUpon(54, 1)
        Unknown3032()
    sprite('dmy_el208', 10)
    RefreshMultihit()
    physicsXImpulse(30000)
    label(1)
    sprite('dmy_el208', 12)
    Unknown3004(-30)
    physicsXImpulse(1000)
    Unknown2001()
    sprite('null', 6)

@State
def dmy_el208_tatsumaki():

    def upon_IMMEDIATE():
        GFX_2('elef_208tornade')
        Unknown4011(3)
    sprite('null', 5)
    teleportRelativeY(0)
    Unknown3001(0)
    sprite('null', 14)
    teleportRelativeX(150000)
    teleportRelativeY(0)
    sprite('null', 5)
    Unknown3004(175)
    sprite('null', 25)
    GFX_0('dmy_el208_col', 100)
    sprite('null', 10)
    label(0)
    sprite('null', 16)
    Unknown26('dmy_el208_col')
    Unknown3004(-16)

@State
def dmy_el208_col():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(200)
        AttackP1(100)
        Unknown11092(1)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackY(5000)
        AirPushbackX(0)
        YImpluseBeforeWallbounce(300)
        Unknown9016(1)
        Unknown11057(800)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeY(0)
    sprite('dmy_el208_tatsumaki_col', 4)
    StartMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    Unknown2037(6)
    label(1)
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    if SLOT_2:
        SLOT_2 = (SLOT_2 + (-1))
        gotoLabel(1)
    else:
        Unknown23029(3, 1002, 0)
        Unknown30056('000000000000000000000000')
        Unknown30055('000000000000000000000000')
        AirPushbackX(0)
        AirPushbackY(25000)
        YImpluseBeforeWallbounce(1600)
        Unknown11068(0)

@State
def elef203_CardShot():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(400)
        AirHitstunAnimation(9)
        AirUntechableTime(22)
        hitstun(22)
        AirPushbackY(7500)
        Unknown11092(1)
        Hitstop(1)
        Unknown11001(-1, -1, -1)
        Unknown9016(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1064(500)
        Unknown4061(2)
        Unknown3033()
        Unknown2053(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown23029(3, 1003, 0)

        def upon_STATE_END():
            GFX_0('elef203_CardShotCrash', 100)
    sprite('vr_elef203_cardshot00', 1)
    Unknown1067(50)
    physicsXImpulse(65000)
    physicsYImpulse(-4000)
    setGravity(-2000)
    Unknown3029(1)
    Unknown3071(3)
    RefreshMultihit()
    AirPushbackX(25000)
    AirPushbackY(5000)
    PushbackX(19800)
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot01', 1)
    sprite('vr_elef203_cardshot02', 1)
    RefreshMultihit()
    sprite('vr_elef203_cardshot03', 1)
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot00', 1)
    RefreshMultihit()
    sprite('vr_elef203_cardshot01', 1)
    sprite('vr_elef203_cardshot02', 1)
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_elef203_cardshot03', 1)
    RefreshMultihit()
    sprite('vr_elef203_cardshot00', 1)
    AirPushbackX(-15000)
    PushbackX(-19800)
    Unknown1067(0)
    physicsYImpulse(0)
    physicsXImpulse(20000)
    setGravity(0)
    sprite('vr_elef203_cardshot01', 1)
    physicsXImpulse(10000)
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot02', 1)
    physicsXImpulse(5000)
    sprite('vr_elef203_cardshot03', 1)
    physicsXImpulse(0)
    sprite('vr_elef203_cardshot00', 1)
    Unknown1067(-50)

    def upon_45():
        Unknown2071('0300000050c3000090d003000a00000000000000')
    setGravity(0)
    RefreshMultihit()
    AirHitstunAnimation(11)
    Unknown30055('f0d8ffff6400000064000000')
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot01', 1)
    RefreshMultihit()
    sprite('vr_elef203_cardshot02', 1)
    sprite('vr_elef203_cardshot03', 1)
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_elef203_cardshot00', 1)
    sprite('vr_elef203_cardshot01', 1)
    RefreshMultihit()
    sprite('vr_elef203_cardshot02', 1)
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot03', 1)
    RefreshMultihit()
    Unknown30055('b88800006400000064000000')
    AirPushbackX(-500)
    AirPushbackY(12000)
    sprite('vr_elef203_cardshot00', 1)
    sprite('vr_elef203_cardshot01', 1)
    DisableAttackRestOfMove()

    def upon_45():
        Unknown2071('030000006079feff90d003003200000000000000')
    sprite('vr_elef203_cardshot02', 1)
    loopRest()
    clearUponHandler(1)
    sprite('null', 1)
    GFX_1('elef_cardshotcrash05', 100)

@State
def elef203_CardShotCrash():

    def upon_IMMEDIATE():
        GFX_2('elef_cardshotcrash')
    sprite('null', 60)

@State
def CardTornade():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        GFX_2('elef_202_landwind')
        Unknown4007(3)
        Unknown1072(5000)
        GFX_0('CardTornade00', 100)
        GFX_0('CardTornade01', 100)
        GFX_0('CardTornade02', 100)
        GFX_0('CardWindMain', 100)
        GFX_0('CardWindSub', 100)
    sprite('null', 40)

@State
def CardTornade00():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f3230326361726430300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1077(-5000, 5000)
        Unknown3033()
        Unknown23118(-16776961)
        Unknown1096(600)
        Unknown1065(200)
        Unknown1059(6)
        Unknown1007(40000)
        physicsYImpulse(500)
        GFX_0('CardWind00', 100)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-25)

@State
def CardTornade01():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f3230326361726430310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown1077(-5000, 5000)
        Unknown3033()
        Unknown23118(-16776961)
        Unknown3001(150)
        Unknown3004(25)
        Unknown1096(800)
        Unknown1065(200)
        Unknown1059(4)
        teleportRelativeX(20000)
        Unknown1007(140000)
        physicsYImpulse(1000)
        GFX_0('CardWind01', 100)
    sprite('null', 12)
    sprite('null', 10)
    Unknown3004(-25)

@State
def CardTornade02():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f3230326361726430300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1077(-5000, 5000)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown23118(-16776961)
        Unknown3001(100)
        Unknown3004(25)
        Unknown1096(700)
        Unknown1065(200)
        Unknown1059(-4)
        teleportRelativeX(30000)
        Unknown1007(260000)
        physicsYImpulse(1500)
        GFX_0('CardWind02', 100)
    sprite('null', 15)
    sprite('null', 10)
    Unknown3004(-25)

@State
def CardWind00():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f32303277696e6430300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1077(-2000, 2000)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown3001(150)
        Unknown1096(650)
        Unknown1065(200)
        Unknown1099(4)
    sprite('null', 14)
    sprite('null', 10)
    Unknown3004(-15)

@State
def CardWind01():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f32303277696e6430310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1077(-2000, 2000)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown3001(150)
        Unknown1096(900)
        Unknown1065(200)
        Unknown1099(5)
    sprite('null', 14)
    sprite('null', 10)
    Unknown3004(-15)

@State
def CardWind02():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f32303277696e6430300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1077(-2000, 2000)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown3001(150)
        Unknown1096(750)
        Unknown1065(250)
        Unknown1099(-4)
        Unknown1007(-32000)
    sprite('null', 14)
    sprite('null', 10)
    Unknown3004(-15)

@State
def CardWindMain():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f32303277696e6430300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown3001(150)
        Unknown1096(500)
        Unknown1065(200)
        Unknown1099(5)
        teleportRelativeX(30000)
        Unknown1007(300000)
    sprite('null', 15)
    sprite('null', 15)
    Unknown3004(-10)

@State
def CardWindSub():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f32303277696e6430310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown3033()
        Unknown3001(200)
        Unknown1096(1000)
        Unknown1065(500)
        Unknown1099(-5)
        teleportRelativeX(20000)
        Unknown1007(70000)
    sprite('null', 15)
    sprite('null', 15)
    Unknown3004(-12)

@State
def elef251_CardShotAir():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(500)
        AirPushbackX(12000)
        AirPushbackY(14000)
        Unknown11092(1)
        Hitstop(1)
        Unknown11001(-1, -1, -1)
        PushbackX(20000)
        Unknown9016(1)
        Unknown30056('000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown23042()

        def upon_STATE_END():
            GFX_0('elef251_CardShotCrashAir', 100)
    sprite('vr_elef251_cardshotair00', 1)
    Unknown1056(900)
    Unknown1064(1000)
    Unknown1059(100)
    Unknown1067(50)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)
    teleportRelativeX(150000)
    RefreshMultihit()
    sprite('vr_elef251_cardshotair02', 1)
    sprite('vr_elef251_cardshotair00', 1)
    teleportRelativeX(100000)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)
    sprite('vr_elef251_cardshotair02', 1)
    teleportRelativeX(50000)
    sprite('vr_elef251_cardshotair00', 1)
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)
    teleportRelativeX(25000)
    sprite('vr_elef251_cardshotair02', 1)
    sprite('vr_elef251_cardshotair00', 1)
    Unknown1059(0)
    Unknown1067(0)
    PushbackX(-22000)
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)
    sprite('vr_elef251_cardshotair02', 1)
    sprite('vr_elef251_cardshotair00', 1)
    AirPushbackX(-12000)
    physicsXImpulse(-59000)
    Unknown3029(1)
    Unknown3071(3)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)
    sprite('vr_elef251_cardshotair02', 1)
    RefreshMultihit()
    sprite('vr_elef251_cardshotair00', 1)
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)
    RefreshMultihit()
    sprite('vr_elef251_cardshotair02', 1)
    sprite('vr_elef251_cardshotair00', 1)
    DisableAttackRestOfMove()
    sprite('vr_elef251_cardshotair01', 1)
    loopRest()
    clearUponHandler(1)
    sprite('null', 1)
    teleportRelativeX(-82000)
    Unknown1007(-20000)
    Unknown4054(5)
    Unknown4045('656c65665f6361726473686f746372617368303500000000000000000000000064000000')

@State
def elef251_CardShotCrashAir():

    def upon_IMMEDIATE():
        GFX_2('elef_cardshotcrashair')
    sprite('null', 60)

@State
def elef400_HandAuraSuccess():

    def upon_IMMEDIATE():
        GFX_2('elef_400_miss')
        Unknown1096(1500)
    sprite('null', 60)

@State
def elef400_Soul():

    def upon_IMMEDIATE():
        GFX_0('elef400_SoulA', 100)
        GFX_0('elef400_SoulB', 100)

        def upon_CLEAR_OR_EXIT():
            Unknown4049(1500)
            Unknown4045('656c65665f3430305f68616e64617572615f616674657200000000000000000064000000')
            Unknown1021(-1200)
    sprite('null', 6)
    Unknown1099(-20)
    sprite('null', 32)
    Unknown1028(-700)
    physicsYImpulse(24000)
    sprite('null', 1)
    GFX_0('elef400_HandAuraSuccess', 100)

@State
def elef400_SoulA():

    def upon_IMMEDIATE():
        GFX_2('elef_400_soul_bodyA')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
    sprite('null', 32767)

@State
def elef400_SoulB():

    def upon_IMMEDIATE():
        GFX_2('elef_400_soul_bodyB')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
    sprite('null', 32767)

@Subroutine
def ThrowCardInit():
    Unknown3032()
    Unknown23118(-1)
    Unknown23119(-16777216, 20, 1)
    Unknown1096(200)
    Unknown1099(40)
    Unknown1074(36000)
    Unknown2053(1)

    def upon_CLEAR_OR_EXIT():
        Unknown1015(-700)
        Unknown1021(-700)

@Subroutine
def ThrowCardActivateInit():
    Unknown3032()
    Unknown23118(-1)
    Unknown23119(-16777216, 10, 1)
    Unknown1056(100)
    Unknown1059(100)

@State
def elef400_EnemyCard_LOVERS():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)
    physicsXImpulse(14000)
    sprite('null', 5)
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)
    GFX_0('elef400_LOVERS', 100)

@State
def elef400_LOVERS():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f6c6f766572735f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_lovers_bom', 100)
    sprite('null', 9)
    sprite('null', 12)
    Unknown7007('70656c3230325f3000000000000000006400000070656c3230325f3100000000000000006400000070656c3230325f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('badst_charm_damage')
    Unknown1099(0)
    GFX_1('elef_card_lovers', 100)

@State
def elef400_EnemyCard_DEATH():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)
    physicsXImpulse(14000)
    sprite('null', 5)
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)
    GFX_0('elef400_DEATH', 100)

@State
def elef400_DEATH():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f64656174685f646566000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_death_bom', 100)
    sprite('null', 9)
    SFX_3('damage_slash_mh')
    SFX_3('cut_l')
    SFX_3('slash_blade_fast')
    sprite('null', 4)
    Unknown7007('70656c3230335f3000000000000000006400000070656c3230335f3100000000000000006400000070656c3230335f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1099(0)
    GFX_1('elef_card_death', 100)
    sprite('null', 8)
    Unknown3001(0)
    GFX_0('elef400_DEATH_HALFA', 100)
    GFX_0('elef400_DEATH_HALFB', 100)

@State
def elef400_DEATH_HALFA():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f64656174685f68616c664100000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        physicsXImpulse(4000)
        physicsYImpulse(4000)

        def upon_CLEAR_OR_EXIT():
            Unknown1015(-300)
            Unknown1021(-300)
    sprite('null', 10)

@State
def elef400_DEATH_HALFB():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f64656174685f68616c664200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        physicsXImpulse(-4000)
        physicsYImpulse(-4000)

        def upon_CLEAR_OR_EXIT():
            Unknown1015(300)
            Unknown1021(300)
    sprite('null', 10)

@State
def elef400_EnemyCard_DEVIL():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)
    physicsXImpulse(14000)
    sprite('null', 5)
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)
    GFX_0('elef400_DEVIL', 100)

@State
def elef400_DEVIL():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f646576696c5f646566000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_devil_bom', 100)
            SFX_3('blaze_short')
    sprite('null', 9)
    sprite('null', 1)
    Unknown7007('70656c3230345f3000000000000000006400000070656c3230345f3100000000000000006400000070656c3230345f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('distortion_a')
    Unknown1099(0)
    GFX_0('elef400_DEVIL_EYE', 100)
    Unknown36(1)
    teleportRelativeX(10000)
    Unknown1007(24000)
    Unknown35()
    GFX_0('elef400_DEVIL_EYE', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(24000)
    Unknown35()
    sprite('null', 11)
    SFX_3('distortion_a')

@State
def elef400_DEVIL_EYE():

    def upon_IMMEDIATE():
        GFX_2('elef_card_devil')
    sprite('null', 12)

@State
def elef400_EnemyCard_TOWER():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)
    physicsXImpulse(14000)
    sprite('null', 5)
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)
    GFX_0('elef400_TOWER', 100)

@State
def elef400_TOWER():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f746f7765725f646566000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_tower_bom', 100)
            SFX_3('thunder_s')
    sprite('null', 9)
    sprite('null', 12)
    Unknown7007('70656c3230355f3000000000000000006400000070656c3230355f3100000000000000006400000070656c3230355f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('electric_s')
    SFX_3('electric_m')
    Unknown1099(0)
    GFX_1('elef_card_tower', 100)

@State
def elef311_GuruGuru():

    def upon_IMMEDIATE():
        GFX_2('elef_guruguru')
        Unknown4007(2)
        Unknown4010(2)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(1, 0)
    sprite('null', 60)
    loopRest()
    label(0)
    sprite('null', 5)
    clearUponHandler(32)
    clearUponHandler(1)
    Unknown3004(-50)
    Unknown1099(300)

@State
def elef406():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('elef_406card_loop')

        def upon_43():
            if (SLOT_48 == 1007):
                sendToLabel(1)
    sprite('null', 6)
    Unknown3001(0)
    Unknown3004(50)
    SFX_3('distortion_b')
    sprite('null', 6)
    Unknown3004(0)
    label(0)
    sprite('null', 6)
    SFX_3('distortion_b')
    sprite('null', 6)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    physicsXImpulse(10000)
    physicsYImpulse(10000)
    Unknown1099(-60)
    loopRest()

@State
def RandomizerCamera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown23032(50)
        Unknown23033(50)

        def upon_43():
            if (SLOT_48 == 1005):
                sendToLabel(1)
    label(0)
    sprite('null', 240)
    Unknown20000(1)
    label(1)
    sprite('null', 10)
    Unknown20000(0)

@State
def Randomizer_col():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('InvSkillInit')
        AttackLevel_(4)
        ProjectileDurabilityLvl(0)
        Unknown11034(1)
        Damage(500)
        Unknown11064(1)
        AttackP1(80)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(600)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(100)
        YImpluseBeforeWallbounce(0)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30048(1)
        Unknown1064(1500)
        Unknown11044(1)
        Unknown11068(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('Randomizer_col')
        Unknown4009(3)

        def upon_12():
            Unknown23029(3, 1006, 0)
            sendToLabel(0)
        if (SLOT_29 <= 350000):
            Unknown1086(22)
    sprite('vr_dmy_tatsumaki', 1)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 10)
    DisableAttackRestOfMove()
    ExitState()
    label(0)
    sprite('vr_dmy_tatsumaki', 110)
    clearUponHandler(12)
    sprite('vr_dmy_tatsumaki', 25)
    RefreshMultihit()
    Damage(2500)
    Unknown11064(0)
    AttackP1(100)
    AttackP2(60)
    AirPushbackY(0)
    YImpluseBeforeWallbounce(2600)
    Unknown11084(1)
    Unknown11044(1)
    Unknown11068(1)
    Unknown11069('')
    Unknown1086(22)
    SFX_3('el060')

    def upon_12():
        clearUponHandler(12)
        Unknown36(22)
        Unknown1086(22)
        Unknown1007(1000000)
        teleportRelativeX(-450000)
        Unknown35()
    sprite('vr_dmy_tatsumaki', 10)
    DisableAttackRestOfMove()
    Unknown4010(2)

@State
def elef407_card_top():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('656c65665f343037636172645f726f742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(448000)
        Unknown3032()
    sprite('null', 8)
    Unknown3001(0)
    Unknown3004(32)
    sprite('null', 8)
    sprite('null', 4)
    Unknown3004(0)
    sprite('null', 20)
    sprite('null', 1)
    Unknown3001(0)
    GFX_0('elef407_card_top_end', 100)

@State
def elef407_card_under():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('656c65665f343037636172645f726f742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
    sprite('null', 8)
    Unknown3001(0)
    Unknown3004(32)
    sprite('null', 8)
    sprite('null', 4)
    Unknown3004(0)
    sprite('null', 20)
    sprite('null', 1)
    Unknown3001(0)
    GFX_0('elef407_card_under_end', 100)

@State
def elef407_card_top_end():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('656c65665f343037636172645f656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown1007(448000)
        GFX_2('elef_407card')
    sprite('null', 20)
    physicsYImpulse(-11200)

@State
def elef407_card_under_end():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('656c65665f343037636172645f656e64322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        GFX_2('elef_407card')
    sprite('null', 20)
    physicsYImpulse(11200)
    sprite('null', 20)
    physicsYImpulse(0)

@State
def elef407_pillar():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        GFX_2('elef_407pillar')
        Unknown1007(224000)
    sprite('null', 15)
    Unknown3001(0)
    Unknown3004(16)
    sprite('null', 15)
    sprite('null', 10)
    Unknown1059(-85)
    Unknown1067(-10)
    Unknown36(22)
    Unknown1059(-100)
    Unknown35()
    sprite('null', 1)
    Unknown1056(0)
    Unknown1059(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown1056(0)
    Unknown1059(0)
    Unknown35()

@State
def elef407_card_return():

    def upon_IMMEDIATE():
        teleportRelativeX(430000)
        Unknown1007(137000)
    sprite('null', 1)
    GFX_1('elef_407card_return', 100)

@Subroutine
def SpecialCardInit():
    Unknown4007(2)
    Unknown4010(2)
    Unknown3032()
    Unknown23118(-1)
    Unknown23119(-16777216, 12, -1)
    Unknown1056(250)
    Unknown1059(250)

@State
def elef402_ply_garu():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef402_ply_garu_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_garu', 100)
    sprite('vr_el402_card', 4)
    sprite('vr_el402_card', 32767)
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef402_ply_garu_infinity():

    def upon_IMMEDIATE():
        GFX_2('elef_card_ply_garu')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)

@State
def elef402_ply_jio():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef402_ply_jio_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_jio', 100)
        Unknown4010(2)
    sprite('vr_el402_card', 4)
    sprite('vr_el402_card', 32767)
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef402_ply_jio_infinity():

    def upon_IMMEDIATE():
        GFX_2('elef_card_ply_jio')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)

@State
def elef403_ply_bufu():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef403_ply_bufu_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_bufu', 100)
    sprite('vr_el403_card', 4)
    sprite('vr_el403_card', 32767)
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef403_ply_bufu_infinity():

    def upon_IMMEDIATE():
        Unknown23067('elef_card_ply_bufu')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(4000)
    sprite('null', 32767)

@State
def elef403_ply_ragi():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef403_ply_ragi_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_ragi', 100)
    sprite('vr_el403_card', 4)
    sprite('vr_el403_card', 32767)
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef403_ply_ragi_infinity():

    def upon_IMMEDIATE():
        GFX_2('elef_card_ply_ragi')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(4000)
    sprite('null', 32767)

@State
def elef431_CardPickUp():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()

        def upon_43():
            if (SLOT_48 == 4504):
                clearUponHandler(43)
                Unknown21012('656c65663433315f4361726457696e643100000000000000000000000000000020000000')
                Unknown21012('656c65663433315f4361726457696e643200000000000000000000000000000020000000')
                GFX_1('elef_431_white_end', 100)
                Unknown4054(5)
                Unknown4045('656c65665f3433315f77686974655f656e64303000000000000000000000000064000000')
                Unknown21012('656c65663433315f57686974654361726400000000000000000000000000000020000000')
                Unknown21012('656c65663433315f426c61636b4361726400000000000000000000000000000020000000')
            if (SLOT_48 == 4505):
                clearUponHandler(43)
                Unknown21012('656c65663433315f4361726457696e643100000000000000000000000000000020000000')
                Unknown21012('656c65663433315f4361726457696e643200000000000000000000000000000020000000')
                GFX_1('elef_431_black_end', 100)
                Unknown4054(5)
                Unknown4045('656c65665f3433315f626c61636b5f656e64303000000000000000000000000064000000')
                Unknown21012('656c65663433315f57686974654361726400000000000000000000000000000020000000')
                Unknown21012('656c65663433315f426c61636b4361726400000000000000000000000000000020000000')
    sprite('null', 4)
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    sprite('null', 4)
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    sprite('null', 4)
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    sprite('null', 4)
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    loopRest()
    sprite('null', 32767)

@State
def elef431_WhiteCard():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f343331636172643030000000000000000000000000000000000000656c65665f3433316361726430305f3030300000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()

        def upon_32():
            Unknown14()
    sprite('null', 30)
    sprite('null', 10)
    Unknown3004(-25)

@State
def elef431_BlackCard():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f343331636172643031000000000000000000000000000000000000656c65665f3433316361726430315f3030300000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()

        def upon_32():
            Unknown14()
    sprite('null', 30)
    sprite('null', 10)
    Unknown3004(-25)

@State
def elef431_CardWind1():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f34333177696e6430300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()
        Unknown3026(-1)
        Unknown3001(0)
        Unknown1102(-150, 0)

        def upon_32():
            sendToLabel(0)
    sprite('null', 25)
    Unknown3004(10)
    sprite('null', 25)
    Unknown3004(-10)
    ExitState()
    label(0)
    sprite('null', 10)
    Unknown1059(100)
    Unknown1067(-10)
    Unknown1091(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def elef431_CardWind2():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f34333177696e6430310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()
        Unknown3026(-16777216)
        Unknown3001(0)
        Unknown1102(-100, 50)

        def upon_32():
            sendToLabel(0)
    sprite('null', 25)
    Unknown3004(10)
    sprite('null', 25)
    Unknown3004(-10)
    ExitState()
    label(0)
    sprite('null', 10)
    Unknown1059(100)
    Unknown1067(-10)
    Unknown1091(100)
    Unknown3001(100)
    Unknown3004(-10)

@State
def elef431_BlackPick():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    sprite('vr_elef431_mudo', 32767)

@State
def elef431_WhitePick():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    sprite('vr_elef431_mao', 32767)

@State
def elHikari():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown3033()
        Unknown2054(1)
        Unknown4061(3)
        Unknown2019(500)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    label(0)
    sprite('vr_el432_00', 4)
    GFX_0('KaihukuAura', 1)
    GFX_1('ttef_kaihuku_cl', 0)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_el432_01', 4)
    Unknown3004(-17)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_00', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_00', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_00', 4)
    sprite('vr_el432_01', 4)
    sprite('vr_el432_02', 4)
    sprite('vr_el432_00', 4)
    ExitState()

@State
def KaihukuAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('656c65665f6b616968756b75617572615f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 20)
    GFX_1('ttef_kaihukuaura_la', 100)
    Unknown3004(26)
    sprite('null', 20)
    Unknown3004(-17)
    Unknown1059(10)

@State
def elef430_Concentraite():

    def upon_IMMEDIATE():
        GFX_2('elef_concentrate')
        Unknown4007(2)
        Unknown2054(1)
        physicsYImpulse(6000)
    sprite('null', 45)
    GFX_0('elef430_ConcentraitePtc', 100)
    sprite('null', 25)
    Unknown3004(-10)

@State
def elef430_ConcentraitePtc():

    def upon_IMMEDIATE():
        GFX_2('elef_concentrate_ptc')
        Unknown2054(1)
        physicsYImpulse(5000)
    sprite('null', 130)

@State
def elef450_AtemiCard():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('656c65665f343530636172643030000000000000000000000000000000000000656c65665f3435306361726430305f3030300000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3033()
        Unknown3001(255)
        teleportRelativeX(120000)
        Unknown1007(290000)
        Unknown1096(500)
        Unknown1064(750)

        def upon_43():
            if (SLOT_48 == 6002):
                sendToLabel(0)
            if (SLOT_48 == 6003):
                sendToLabel(1)
    sprite('null', 5)
    Unknown1099(25)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    clearUponHandler(33)
    sprite('null', 10)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(-75)
    ExitState()
    label(1)
    clearUponHandler(32)
    sprite('null', 10)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)
    ExitState()

@State
def elef450_CounterCard():

    def upon_IMMEDIATE():
        GFX_2('elef_208tornade')
        Unknown4011(3)
        Unknown2054(1)
    sprite('null', 5)
    Unknown1086(22)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(175)
    sprite('null', 25)
    GFX_0('elef450_CounterCardAtk', 100)
    sprite('null', 10)
    label(0)
    sprite('null', 16)
    Unknown26('elef450_CounterCardAtk')
    Unknown3004(-16)

@State
def elef450_CounterCardAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Unknown11056(3)
        Damage(0)
        Unknown11064(1)
        Unknown11042(1)
        Unknown11084(1)
        AttackP1(100)
        Unknown11092(1)
        Hitstop(0)
        PushbackX(0)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(600)
        hitstun(600)
        AirPushbackY(5000)
        AirPushbackX(0)
        YImpluseBeforeWallbounce(300)
        Unknown9016(1)
        Unknown11057(800)
        Unknown11066(1)
        Unknown11085(1)
        Unknown11069('elef450_CounterCardAtk')
        Unknown11072(1, 0, 10000)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        teleportRelativeY(0)
    sprite('dmy_el208_tatsumaki_col', 4)
    StartMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)
    RefreshMultihit()
    AirPushbackX(0)
    AirPushbackY(0)
    Unknown11072(1, 0, 0)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    Unknown11069('elef450_CardLay_Base')

    def upon_78():
        GFX_0('elef450_LockCard', 101)
        Unknown23029(3, 6004, 0)

@State
def elef450_LockCard():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('656c65665f343530636172643032000000000000000000000000000000000000656c65665f3435306361726430325f3030300000000000000000000000000000')
        Unknown2054(1)
        Unknown3033()
        Unknown1096(900)
        GFX_0('elef450_LockCardTop', 100)
        GFX_0('elef450_LockCardBottom', 100)

        def upon_32():
            Unknown21012('656c65663435305f4c6f636b43617264546f700000000000000000000000000020000000')
            Unknown21012('656c65663435305f4c6f636b43617264426f74746f6d0000000000000000000020000000')
            sendToLabel(0)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    Unknown1099(25)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 10)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)

@State
def elef450_LockCardTop():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('656c65665f343530636172643031000000000000000000000000000000000000656c65665f3435306361726430315f3030300000000000000000000000000000')
        Unknown2054(1)
        Unknown3033()
        Unknown1007(128000)
        Unknown1096(700)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    Unknown1099(25)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 10)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)

@State
def elef450_LockCardBottom():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('656c65665f343530636172643031000000000000000000000000000000000000656c65665f3435306361726430315f3030300000000000000000000000000000')
        Unknown2054(1)
        Unknown3033()
        Unknown1007(-128000)
        Unknown1096(800)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    Unknown1099(25)
    sprite('null', 32767)
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 10)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)

@State
def CameraDammy():

    def upon_IMMEDIATE():
        teleportRelativeX(256000)
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20002(0)
            Unknown20003(0)
    sprite('null', 32767)

@State
def elef450_CardLayParent():

    def upon_IMMEDIATE():
        Unknown2055(72)
    label(0)
    sprite('null', 1)
    GFX_0('elef450_CardLay', 100)
    sprite('null', 2)
    GFX_0('elef450_CardLay', 100)
    loopRest()
    gotoLabel(0)

@State
def elef450_CardLay():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f343530636172646c61793030000000000000000000000000000000656c65665f343530636172646c61793030000000000000000000000000000000')
        Unknown3032()
        Unknown3001(0)
        Unknown3004(25)
        Unknown1010(-290000, 160000)
        Unknown1011(-120000, 260000)

        def upon_STATE_END():
            Unknown4054(5)
            Unknown4045('656c65665f3435305f6c61796f70656e0000000000000000000000000000000064000000')
            GFX_0('elef450_CardLay_Base', 100)
    sprite('null', 120)
    Unknown23119(-1, 30, -1)

@State
def elef450_CardLay_Base():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown4010(3)
        AttackLevel_(5)
        Damage(999)
        MinimumDamagePct(100)
        AirUntechableTime(600)
        hitstun(600)
        Hitstop(3000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(0)
        AirPushbackY(0)
        Unknown30055('000000000000000000000000')
        Unknown30056('000000000000000000000000')
        YImpluseBeforeWallbounce(0)
        Unknown9021(1)
        GFX_2('elef_450_lay')
        Unknown3038(1)
        Unknown3033()
        physicsXImpulse(-30000)
        physicsYImpulse(15000)
        Unknown1025(-10000, 5000)
        Unknown1026(-30000, 15000)
        Unknown23048('01000000')
        Unknown23051('76725f656c65663435305f636172646c61795f61667465722e646473000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23050('5000000014000000')
        Unknown23049('ffffffff00000000')

        def upon_CLEAR_OR_EXIT():
            Unknown2074(22)
            Unknown103(200000, 10)
            Unknown1108(9000)

        def upon_ON_HIT_OR_BLOCK():
            Unknown14()
            GFX_1('elef_450_layhit', 100)
    sprite('vr_elef450_cardlay', 30)
    DisableAttackRestOfMove()
    sprite('vr_elef450_cardlay', 32767)
    RefreshMultihit()

@State
def elef450_cardA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown23067('elef_450_cardA')
        Unknown1096(750)
    sprite('null', 32767)

@State
def elef450_cardB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 40)
    GFX_0('elef450_cardB_Ptc', 100)
    loopRest()
    gotoLabel(0)

@State
def elef450_cardB_Ptc():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown23067('elef_450_cardB')
        Unknown1096(750)
    sprite('null', 40)

@State
def Cutinbg():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f3435306267303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown2007()
        Unknown3001(255)
        Unknown1056(5)
        Unknown1064(500)

        def upon_CLEAR_OR_EXIT():
            Unknown1065(20)

        def upon_32():
            sendToLabel(0)
    sprite('null', 10)
    Unknown3004(-15)
    sprite('null', 90)
    Unknown3004(0)
    sprite('null', 32767)

    def upon_CLEAR_OR_EXIT():
        Unknown1057(8)
        Unknown1065(5)
    label(0)
    sprite('null', 10)
    Unknown3004(-10)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown23015(1)
        Unknown6001(1)
        Unknown1001(640000)
        Unknown23033(140)
        teleportRelativeX(600000)
        physicsYImpulse(5000)
        Unknown3032()
        Unknown3001(0)

        def upon_32():
            sendToLabel(0)

        def upon_CLEAR_OR_EXIT():
            YAccel(96)
    sprite('ichigeki', 15)
    Unknown3004(5)
    sprite('ichigeki', 32767)
    label(0)
    sprite('ichigeki', 15)
    Unknown3004(-20)

@State
def elef450_MegidoraJon():

    def upon_IMMEDIATE():
        Unknown1007(160000)
        GFX_0('elef450_MBall', 100)

        def upon_32():
            Unknown1007(-144000)
            physicsYImpulse(-5000)
            Unknown21012('656c65663435305f4d42616c6c0000000000000000000000000000000000000021000000')

        def upon_LANDING():
            Unknown21007(2, 41)
            Unknown21012('656c65663435305f4d42616c6c0000000000000000000000000000000000000020000000')
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    clearUponHandler(3)
    physicsYImpulse(0)
    label(1)
    sprite('null', 10)

@State
def elef450_MBall():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('656c65665f3435306d656769646f7261303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3032()
        Unknown1007(1680000)
        GFX_0('elef450_MLight', 100)

        def upon_CLEAR_OR_EXIT():
            Unknown1097(-4)

        def upon_32():
            Unknown21012('656c65663435305f4d4c6967687400000000000000000000000000000000000020000000')
            sendToLabel(0)

        def upon_33():
            Unknown26('elef450_PowUpA')
            Unknown26('elef450_PowUpB')
            Unknown26('elef450_PowUpC')
            Unknown26('elef450_PowUpD')

        def upon_STATE_END():
            Unknown21007(2, 33)
    sprite('null', 30)
    Unknown1099(80)
    GFX_0('elef450_PowUpA', 100)
    sprite('null', 30)
    Unknown1101(80)
    GFX_0('elef450_PowUpB', 100)
    sprite('null', 30)
    Unknown1101(80)
    GFX_0('elef450_PowUpC', 100)
    sprite('null', 30)
    Unknown1101(80)
    GFX_0('elef450_PowUpD', 100)
    sprite('null', 30)
    Unknown1101(80)
    sprite('null', 90)
    Unknown1101(80)
    Unknown1099(10)
    clearUponHandler(3)
    sprite('null', 32767)
    loopRest()
    label(0)
    sprite('null', 2)
    Unknown1007(-1050000)
    Unknown1096(2000)
    sprite('null', 2)
    Unknown1056(1600)
    Unknown1064(1200)
    sprite('null', 6)
    Unknown1059(2000)
    Unknown1067(2000)
    sprite('null', 60)
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('null', 25)
    Unknown3004(-10)
    sprite('null', 30)
    Unknown21012('656c65663435305f4d4c6967687400000000000000000000000000000000000021000000')

@State
def elef450_PowUpA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('656c65665f3435306d656769646f7261303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23118(-16777088)
        Unknown1056(500)
        Unknown1064(600)
        Unknown1098(200)
        Unknown1007(-32000)
        Unknown1059(10)
        Unknown1067(20)
        physicsYImpulse(5000)
        Unknown3032()
        Unknown3001(0)
        Unknown3004(2)
    sprite('null', 32767)

@State
def elef450_PowUpB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('656c65665f3435306d656769646f7261303200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23118(-16777088)
        Unknown1056(500)
        Unknown1064(600)
        Unknown1098(200)
        Unknown1007(-32000)
        Unknown1059(10)
        Unknown1067(20)
        physicsYImpulse(5000)
        Unknown3032()
        Unknown3001(0)
        Unknown3004(2)
    sprite('null', 32767)

@State
def elef450_PowUpC():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('656c65665f3435306d656769646f7261303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23118(-16776961)
        Unknown1057(200)
        Unknown1065(500)
        Unknown1098(200)
        Unknown1073(-25000)
        teleportRelativeX(256000)
        Unknown1007(-1120000)
        physicsXImpulse(-2000)
        physicsYImpulse(5000)
        Unknown1059(4)
        Unknown1067(8)
        Unknown1074(150)
        Unknown3032()
        Unknown3001(0)
        Unknown3004(1)
    sprite('null', 32767)

@State
def elef450_PowUpD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('656c65665f3435306d656769646f7261303200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23118(-16776961)
        Unknown1057(200)
        Unknown1065(500)
        Unknown1098(200)
        Unknown1073(25000)
        teleportRelativeX(-256000)
        Unknown1007(-1120000)
        physicsXImpulse(2000)
        physicsYImpulse(5000)
        Unknown1059(4)
        Unknown1067(8)
        Unknown1074(-150)
        Unknown3032()
        Unknown3001(0)
        Unknown3004(1)
    sprite('null', 32767)

@State
def elef450_MLight():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown23067('elef_450_megidora_light')
        Unknown4007(2)
        Unknown4009(2)

        def upon_32():
            Unknown4013(2)

        def upon_33():
            sendToLabel(1)
    sprite('null', 32767)
    label(1)
    sprite('null', 30)
    sprite('null', 30)
    Unknown3004(-8)

@State
def elef450_DamageNum():

    def upon_IMMEDIATE():
        Unknown1000(128000)
        teleportRelativeY(480000)
        Unknown2007()
        Unknown23015(1)
        Unknown3032()
        Unknown1096(3000)
    sprite('vr_elef450_damage_num', 20)
    sprite('vr_elef450_damage_num', 25)
    Unknown3004(-10)

@State
def PEL_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000080841e000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(1200)
        AttackP1(90)
        Unknown11092(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(20000)
        AirPushbackY(15000)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        AirUntechableTime(29)
        Hitstop(9)
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        Unknown2015(180)
        Unknown2016(280)

        def upon_ON_HIT_OR_BLOCK():
            if SLOT_2:
                clearUponHandler(10)
                Unknown23029(3, 1004, 0)
    sprite('tt204_00', 3)
    sprite('tt204_01', 4)
    sprite('tt204_02', 3)
    GFX_0('ttef204_Zanzoh', 100)
    SFX_3('hit_m_slow')
    sprite('tt204_03', 1)
    RefreshMultihit()
    sprite('tt204_03', 2)
    Unknown23022(0)
    DisableAttackRestOfMove()
    sprite('tt204_04', 9)
    sprite('tt204_05', 3)
    GFX_0('ttef204_Zanzoh2', 100)
    physicsXImpulse(85000)
    SFX_3('chain_move')
    sprite('tt204_06', 3)
    SFX_3('hit_m_slow')
    sprite('tt204_07', 1)
    RefreshMultihit()
    Hitstop(3)
    AirUntechableTime(36)
    Unknown9190(1)
    YImpluseBeforeWallbounce(0)
    AirPushbackX(2500)
    AirPushbackY(-50000)
    Unknown9118(45)
    PushbackX(16000)
    physicsXImpulse(0)
    Unknown2037(1)
    sprite('tt204_07', 2)
    Unknown23029(3, 2011, 0)
    DisableAttackRestOfMove()
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(580)
    sprite('keep', 16)
    Unknown1019(0)
    DisableAttackRestOfMove()
    Unknown21012('747465663230345f5a616e7a6f6832000000000000000000000000000000000020000000')
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def ttef204_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3032()
    sprite('vr_tt204_00', 3)
    sprite('vr_tt204_01', 3)
    Unknown3004(-63)

@State
def ttef204_Zanzoh2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3032()
        sendToLabelUpon(32, 0)
    sprite('vr_tt204_10', 3)
    sprite('vr_tt204_11', 3)
    sprite('vr_tt204_12', 10)
    Unknown3004(-42)
    ExitState()
    label(0)
    sprite('null', 1)

@State
def PEL_Persona5D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000c05c15000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(0)
        Damage(0)
        Unknown11044(1)
        AttackP1(100)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11054(250000)
        Hitstop(1)
        HitOverhead(2)
        HitLow(2)
        Unknown11045(1)
        Unknown11082(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11058('0000000000000000000000000000000001000000')
        DisableAttackRestOfMove()
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(1)
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        EnableCollision(1)
        Unknown2034(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt205_00', 4)
    sprite('tt205_01', 4)
    sprite('tt205_02', 4)
    sprite('tt205_00', 4)
    sprite('tt205_01', 5)
    sprite('tt205_03', 4)
    sprite('tt205_04', 2)
    physicsXImpulse(24000)
    RefreshMultihit()
    sprite('tt205_05', 2)
    physicsXImpulse(48000)
    sprite('tt205_04', 2)
    SFX_3('chain_move')
    sprite('tt205_06', 2)
    Unknown1019(30)
    Unknown23029(3, 2013, 0)
    sprite('tt205_07', 2)
    EnableCollision(0)
    sprite('tt205_08', 2)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)
    enterState('PEL_Persona5DGrip')

@State
def PEL_Persona5DGrip():

    def upon_IMMEDIATE():
        callSubroutine('PEL_AttackInit')
        Unknown17011('PEL_Persona5DExe', 1, 0, 0)
        Unknown2006()
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        HitAirUnblockable(4)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        Unknown23022(1)
        DisableAttackRestOfMove()
        Unknown30031(0)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 2022, 0)
        Unknown23078(1)
        Unknown2053(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('keep', 2)
    RefreshMultihit()
    sprite('tt205_06', 2)
    Unknown1019(30)
    sprite('tt205_07', 2)
    EnableCollision(0)
    sprite('tt205_08', 2)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(60)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_Persona2D():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000400d030000000000807be1ff80841e000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(90)
        GroundedHitstunAnimation(11)
        Unknown11058('0000000000000000010000000000000000000000')
        AirPushbackY(20000)
        HitLow(2)
        AirUntechableTime(30)
        Hitstop(1)
        Unknown11001(12, 12, 17)
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        EnableCollision(1)
        Unknown2034(1)
    sprite('tt233_00', 3)
    SFX_0('chain_move')
    sprite('tt233_03', 3)
    sprite('tt233_04', 3)
    sprite('tt233_05', 2)
    GFX_1('ttef_poisonbreath_add', 0)
    sprite('tt233_06', 2)
    GFX_1('ttef_poisonbreath_add', 0)
    sprite('tt233_07', 3)
    RefreshMultihit()
    SFX_3('el050')
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_08', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_09', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_10', 3)
    DisableAttackRestOfMove()
    Unknown23029(3, 2014, 0)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_11', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_12', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_10', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_11', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_12', 3)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_10', 3)
    sprite('tt233_11', 3)
    sprite('tt233_12', 3)
    sprite('tt233_10', 3)
    sprite('tt233_11', 3)
    sprite('tt233_12', 3)
    sprite('tt233_10', 3)
    sprite('tt233_11', 3)
    sprite('tt233_12', 3)
    sprite('tt233_10', 3)
    sprite('tt233_11', 3)
    sprite('tt233_12', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@Subroutine
def WarpCheckEx():
    Unknown2037(0)
    if (SLOT_11 >= 100):
        Unknown48('190000000200000035000000190000000200000013000000')
        Unknown48('190000000200000037000000030000000200000013000000')
        if (SLOT_55 > SLOT_53):
            Unknown2037(1)
            Unknown1004()

@State
def PEL_PersonaAir5C():

    def upon_IMMEDIATE():
        callSubroutine('WarpCheckEx')
        Unknown23023()
        Unknown23184('03000000640000006079feff50c300000000000080841e000000000000000000')
        callSubroutine('PEL_AttackInit')
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9310(1)
        AirUntechableTime(29)
        Hitstop(9)
        AirPushbackX(3000)
        AirPushbackY(-60000)
        Unknown11058('0100000000000000000000000000000000000000')
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PEL_ForceWarp')
        Unknown2053(1)
    sprite('tt254_00', 3)
    if SLOT_2:
        Unknown1005()
    sprite('tt254_01', 3)
    SFX_3('hit_m_slow')
    SFX_3('chain_move')
    sprite('tt254_02', 3)
    sprite('tt254_03', 1)
    RefreshMultihit()
    sprite('tt254_03', 2)
    Unknown23022(0)
    sprite('tt254_04', 3)
    Unknown23029(3, 2015, 0)
    SFX_3('chain_move')
    sprite('tt254_05', 3)
    sprite('tt254_06', 3)
    sprite('tt254_07', 6)
    sprite('tt254_08', 6)
    sprite('tt254_09', 6)
    sprite('tt254_07', 6)
    sprite('tt254_08', 6)
    sprite('tt254_09', 6)
    sprite('tt254_07', 6)
    sprite('tt254_08', 6)
    sprite('tt254_09', 6)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaAir5D():

    def upon_IMMEDIATE():
        callSubroutine('WarpCheckEx')
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000c05c15000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(0)
        Damage(0)
        Unknown11044(1)
        AttackP1(100)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown11054(250000)
        Hitstop(1)
        HitAirUnblockable(100)
        HitOverhead(2)
        HitLow(2)
        Unknown11046(1)
        Unknown11082(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11058('0000000000000000000000000000000001000000')
        DisableAttackRestOfMove()
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(1)
        Unknown23078(1)
        callSubroutine('PEL_ForceWarp')
        Unknown2053(1)
        EnableCollision(1)
        Unknown2034(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt205_03', 4)
    if SLOT_2:
        Unknown1005()
    sprite('tt205_04', 2)
    physicsXImpulse(64000)
    RefreshMultihit()
    sprite('tt205_05', 2)
    SFX_3('chain_move')
    sprite('tt205_06', 2)
    Unknown1019(30)
    EnableCollision(0)
    Unknown23029(3, 2016, 0)
    sprite('tt205_07', 2)
    sprite('tt205_08', 2)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(0)
    sprite('tt205_09', 3)
    sprite('tt205_10', 3)
    sprite('tt205_09', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)
    enterState('PEL_PersonaAir5DGrip')

@State
def PEL_PersonaAir5DGrip():

    def upon_IMMEDIATE():
        callSubroutine('PEL_AttackInit')
        Unknown17011('PEL_Persona5DExe', 1, 1, 0)
        Unknown2006()
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        HitAirUnblockable(4)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        Unknown23022(1)
        DisableAttackRestOfMove()
        Unknown30031(0)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 2025, 0)
        Unknown23078(1)
        Unknown2053(1)
        Unknown23059(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('keep', 2)
    RefreshMultihit()
    sprite('tt205_06', 2)
    Unknown1019(30)
    EnableCollision(0)
    sprite('tt205_07', 2)
    sprite('tt205_08', 2)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    Unknown1019(0)
    sprite('tt205_09', 3)
    sprite('tt205_10', 3)
    sprite('tt205_09', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_Persona5DExe():

    def upon_IMMEDIATE():
        callSubroutine('PEL_AttackInit')
        Unknown17012(2, 1, 0)
        Unknown2006()
        AttackLevel_(4)
        Damage(2000)
        MinimumDamagePct(0)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown9346(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown30079(1)
        Unknown11064(1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown9016(1)
        Unknown30048(1)
        Unknown23022(1)
        DisableAttackRestOfMove()
        Unknown30031(0)
        Unknown23022(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if SLOT_37:
                    clearUponHandler(3)
                    Unknown2037(0)
                    sendToLabel(1)
    sprite('tt205_04', 4)
    StartMultihit()
    physicsXImpulse(0)
    if Unknown23145('PEL_PersonaAir5DGrip'):
        physicsYImpulse(20000)
        setGravity(2000)
    Unknown23015(0)
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000008000000')
    sprite('tt206_00', 5)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2019(100)
    sprite('tt206_01', 5)
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('tt206_02', 5)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_03', 5)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_04', 60)
    Unknown2037(1)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    label(1)
    sprite('tt206_04', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_01', 12)
    GFX_1('ttef_biteblood', 0)
    RefreshMultihit()
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    SFX_3('blood_l')
    sprite('tt206_05', 3)
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('tt206_06', 6)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_07', 4)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    RefreshMultihit()
    Damage(1000)
    Unknown23015(11)
    sprite('tt206_08', 4)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    sprite('tt206_09', 4)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    GFX_1('ttef_biteblood', 0)
    SFX_3('blood_l')
    sprite('tt206_10', 4)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt206_11', 4)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt206_12', 4)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt206_07', 3)
    Unknown2005()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    StartMultihit()
    sprite('tt206_08', 3)
    Unknown2019(4000)
    Unknown30079(0)
    RefreshMultihit()
    Unknown11068(0)
    AirPushbackX(150000)
    AirPushbackY(20000)
    Unknown11072(1, -10000, 100000)
    Unknown11099(1)
    AirUntechableTime(60)
    AirHitstunAfterWallbounce(60)
    Unknown9178(1)
    WallbounceReboundTime(10)
    Unknown9310(1)
    Unknown9362(1)
    Unknown9364(25)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11064(0)
    SFX_3('hit_m_slow')
    Unknown2034(0)
    sprite('tt206_09', 3)
    Unknown23029(3, 2029, 0)
    SLOT_10 = 0
    sprite('tt206_10', 5)
    sprite('tt206_11', 5)
    sprite('tt206_12', 5)
    sprite('tt206_10', 5)
    sprite('tt206_11', 5)
    sprite('tt206_12', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_Persona2C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a08601000000000010b6fdff80841e000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(30)
        Unknown11001(0, 5, 10)
        AirPushbackX(30000)
        AirPushbackY(20000)
        Unknown11058('0000000001000000000000000000000000000000')
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        EnableCollision(1)
    sprite('tt232_00', 3)
    sprite('tt232_01', 3)
    sprite('tt232_02', 3)
    sprite('tt232_03', 3)
    Unknown1045(18000)
    setInvincible(1)
    GuardPoint_(1)
    sprite('tt232_04', 3)
    sprite('tt232_05', 3)
    sprite('tt232_06', 1)
    ScreenShake(7000, 7000)
    GFX_0('houkouSphereLoop', 0)
    RefreshMultihit()
    SFX_3('el006')
    sprite('tt232_06', 2)
    Unknown23022(0)
    sprite('tt232_07', 3)
    ScreenShake(7000, 7000)
    setInvincible(0)
    sprite('tt232_08', 3)
    sprite('tt232_06', 3)
    sprite('tt232_07', 3)
    sprite('tt232_08', 3)
    DisableAttackRestOfMove()
    Unknown23029(3, 2012, 0)
    sprite('tt232_06', 3)
    sprite('tt232_07', 3)
    SFX_3('chain_move')
    sprite('tt232_08', 3)
    sprite('tt232_06', 3)
    sprite('tt232_07', 3)
    sprite('tt232_08', 3)
    sprite('tt232_06', 3)
    sprite('tt232_07', 3)
    sprite('tt232_08', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def houkouSphereLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        GFX_2('ttef_houkou_snb')
        Unknown4010(2)
    sprite('null', 5)
    GFX_0('houkouSphere', 100)
    sprite('null', 5)
    GFX_0('houkouSphere', 100)
    sprite('null', 5)
    GFX_0('houkouSphere', 100)
    sprite('null', 5)
    GFX_0('houkouSphere', 100)
    sprite('null', 5)

@State
def houkouSphere():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('656c65665f686f756b6f7573686f636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 3)
    sprite('null', 5)
    Unknown1099(30)
    Unknown3004(-51)
    loopRest()

@State
def AssaultSEMaster():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown2037(7)
        SLOT_51 = 10
        SLOT_52 = 5

        def upon_CLEAR_OR_EXIT():
            Unknown2038(1)
            if (SLOT_2 >= SLOT_51):
                SFX_3('el050')
                Unknown2037(0)
                SLOT_52 = (SLOT_52 + (-1))
                if (not SLOT_52):
                    Unknown14()

        def upon_32():
            clearUponHandler(32)
            SLOT_51 = 6
    sprite('null', 60)

@State
def PEL_PersonaAssault():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000006ffff00000000000000000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        Unknown2054(1)
        Unknown23066(1)
        EnableCollision(0)
        Unknown23022(1)
        Unknown23059(0)
        callSubroutine('PEL_CheckWarp')

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown4007(3)
            else:
                Unknown1086(3)
                teleportRelativeY(0)
        Unknown2037(0)

        def upon_32():
            Unknown2037(1)
    sprite('tt404_00', 2)
    SFX_3('chain_move')
    sprite('tt404_01', 2)
    sprite('tt404_02', 2)
    GFX_0('GarudineTatsumakiJizoku', 0)
    Unknown38(6, 1)
    Unknown23029(6, 7001, 0)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    Unknown23029(6, 7004, 0)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    Unknown4007(0)
    clearUponHandler(3)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    gotoLabel(10)
    label(0)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    gotoLabel(0)
    label(10)
    sprite('keep', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def TatsumakiAAAA():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        Damage(350)
        Unknown11092(1)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(-500)
        AirPushbackY(15000)
        AirUntechableTime(33)
        Unknown9016(1)
        Unknown11057(800)
        Unknown30056('e0b1ffff3200000000000000')
        Unknown11044(1)
        DisableAttackRestOfMove()
        Unknown4010(2)
        Unknown4011(3)
        Unknown4009(3)
        Unknown4007(2)
    if SLOT_4:
        _gotolabel(0)
    sprite('vr_dmy_tatsumaki', 2)
    GFX_0('AssaultSEMaster', -1)
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    Unknown3004(26)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    AirPushbackX(30000)
    AirPushbackY(25000)
    AirUntechableTime(60)
    Unknown30055('000000003200000000000000')
    Unknown30056('000000003200000000000000')
    Unknown30088(1)
    sprite('null', 5)
    Unknown2063()
    DisableAttackRestOfMove()
    ExitState()
    label(0)
    sprite('vr_dmy_tatsumaki', 2)
    GFX_0('AssaultSEMaster', -1)
    Damage(300)
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    Unknown3004(26)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    AirPushbackX(30000)
    AirPushbackY(25000)
    AirUntechableTime(60)
    Unknown30055('000000003200000000000000')
    Unknown30056('000000003200000000000000')
    Unknown30088(1)
    sprite('null', 5)
    Unknown2063()
    DisableAttackRestOfMove()
    ExitState()

@State
def ShotSEMaster():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown2037(4)
        SLOT_51 = 4
        SLOT_52 = 4

        def upon_CLEAR_OR_EXIT():
            Unknown2038(1)
            if (SLOT_2 >= SLOT_51):
                SFX_3('el054')
                Unknown2037(0)
                SLOT_52 = (SLOT_52 + (-1))
                if (not SLOT_52):
                    Unknown14()

        def upon_32():
            clearUponHandler(32)
            SLOT_51 = 6
    sprite('null', 30)

@Subroutine
def MahagioEffectInit():
    Unknown11034(0)
    ProjectileDurabilityLvl(1)
    Unknown11058('0000000000000000000000000100000000000000')
    Unknown9266(8)
    Unknown9021(1)
    Unknown11057(800)

@State
def PEL_PersonaShot():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000204e0000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(100000)
        AirPushbackY(28000)
        AirUntechableTime(43)
        DisableAttackRestOfMove()
        callSubroutine('MahagioEffectInit')
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
    sprite('tt402_00', 2)
    SFX_3('chain_move')
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 2)
    sprite('tt402_06ex2', 1)
    GFX_0('UltimateLaserJizoku', 0)
    Unknown36(1)
    Unknown1056(500)
    Unknown1064(250)
    teleportRelativeX(-3000)
    Unknown1007(-15000)
    Unknown35()
    GFX_0('ShotSEMaster', -1)
    RefreshMultihit()
    sprite('tt402_06ex2', 1)
    Unknown23022(0)
    sprite('tt402_07ex', 3)
    Unknown23029(3, 3013, 0)
    DisableAttackRestOfMove()
    sprite('tt402_08ex', 3)
    sprite('tt402_09ex', 3)
    sprite('tt402_10ex', 3)
    sprite('tt402_11ex', 3)
    sprite('tt402_06ex', 3)
    sprite('tt402_07ex', 3)
    sprite('tt402_08ex', 3)
    sprite('tt402_09ex', 3)
    sprite('tt402_10', 3)
    Unknown2001()
    label(0)
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaShotSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000204e0000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(100000)
        AirPushbackY(28000)
        AirUntechableTime(43)
        DisableAttackRestOfMove()
        callSubroutine('MahagioEffectInit')
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
    sprite('tt402_00', 2)
    SFX_3('chain_move')
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_00', 1)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 1)
    sprite('tt402_05', 1)
    sprite('tt402_06', 1)
    GFX_0('UltimateLaserJizoku', 0)
    GFX_0('ShotSEMaster', -1)
    sprite('tt402_06', 1)
    RefreshMultihit()
    sprite('tt402_07', 2)
    Unknown23022(0)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    Unknown23029(3, 3013, 0)
    DisableAttackRestOfMove()
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    Unknown2001()
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    sprite('tt402_11', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()

@State
def UltimateLaserJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('656c65665f6a696f64696e655f6a697a6f6b7530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        sendToLabelUpon(33, 1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                clearUponHandler(3)
                sendToLabel(9)
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 5)
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(-200)
    Unknown3004(-51)
    ExitState()
    label(1)
    sprite('null', 4)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 15)
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(-200)
    Unknown3004(-51)

@Subroutine
def SwordFireSet():
    GFX_1('ttef_431_swordfire00', 0)
    GFX_1('ttef_431_swordfire00', 1)
    GFX_1('ttef_431_swordfire00', 2)
    GFX_1('ttef_431_swordfire00', 3)

@Subroutine
def SwordFireSet2():
    GFX_1('ttef_431_swordfire', 0)
    GFX_1('ttef_431_swordfire', 1)
    GFX_1('ttef_431_swordfire', 2)
    GFX_1('ttef_431_swordfire', 3)

@State
def PEL_PersonaAntiAir():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(2500)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2500)
        AirPushbackY(22000)
        AirUntechableTime(31)
        Hitstop(12)
        Unknown11058('0000000001000000000000000000000000000000')
        FreezeDuration(36)
        FreezeCount(1)
        Unknown9016(1)
        Unknown9266(9)
        DisableAttackRestOfMove()
        EnableCollision(1)
        Unknown2034(1)
        Unknown23066(1)
        callSubroutine('PEL_CheckWarp')
    sprite('tt403_00', 4)
    SFX_3('chain_move')
    sprite('tt403_01', 4)
    sprite('tt403_02', 4)
    sprite('tt403_03', 3)
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 2)
    SFX_3('slash_blade_fast')
    Unknown1019(40)
    sprite('tt403_05', 1)
    Unknown1019(0)
    RefreshMultihit()
    sprite('tt403_05', 3)
    Unknown23029(3, 3015, 0)
    Unknown23022(0)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)
    sprite('tt403_06', 20)
    sprite('tt403_06', 10)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaAntiAirSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(500)
        Unknown11092(1)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(0)
        AirPushbackX(3500)
        AirUntechableTime(31)
        Hitstop(2)
        Unknown9016(1)
        Unknown9266(9)
        Unknown11058('0000000001000000000000000000000000000000')
        DisableAttackRestOfMove()
        EnableCollision(1)
        Unknown2034(1)
        Unknown23066(1)
        callSubroutine('PEL_CheckWarp')
    sprite('tt403_00', 3)
    SFX_3('chain_move')
    sprite('tt403_01', 3)
    sprite('tt403_02', 3)
    sprite('tt403_03', 3)
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(10)
    physicsXImpulse(80000)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 <= 200000):
            clearUponHandler(3)
            Unknown1019(0)
    sprite('tt403_03', 3)
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 1)
    clearUponHandler(3)
    SFX_3('slash_blade_fast')
    Unknown1019(40)
    RefreshMultihit()
    sprite('tt403_04', 1)
    Unknown23022(0)
    sprite('tt403_05', 1)
    Unknown1019(0)
    RefreshMultihit()
    Damage(3000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(2500)
    AirPushbackY(22000)
    Hitstop(12)
    FreezeDuration(39)
    FreezeCount(1)
    sprite('tt403_05', 3)
    DisableAttackRestOfMove()
    Unknown23029(3, 3015, 0)
    sprite('tt403_06', 8)
    sprite('tt403_06', 37)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaAssaultEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000006ffff00000000000000000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        Unknown2054(1)
        Unknown23066(1)
        EnableCollision(0)
        Unknown23022(1)
        Unknown23059(0)
        callSubroutine('PEL_CheckWarp')
        Unknown1086(3)
        Unknown1004()
        Unknown1008()
        teleportRelativeY(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown4007(3)
            else:
                Unknown1086(3)
                Unknown1009()
        Unknown2037(0)

        def upon_32():
            Unknown2037(1)
        sendToLabelUpon(38, 0)
        sendToLabelUpon(40, 10)
    sprite('tt404_00', 2)
    SFX_3('chain_move')
    sprite('tt404_01', 2)
    sprite('tt404_02', 2)
    GFX_0('GarudineTatsumakiJizoku', 0)
    Unknown38(6, 1)
    Unknown23029(6, 7002, 0)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    Unknown23029(6, 7004, 0)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    Unknown4007(0)
    clearUponHandler(3)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    gotoLabel(10)
    label(0)
    sprite('tt404_03', 2)
    sprite('tt404_04', 2)
    sprite('tt404_05', 2)
    gotoLabel(0)
    label(10)
    sprite('keep', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def TatsumakiEx():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(3)
        Unknown4009(3)
        Unknown4007(2)
        Unknown2010()
        AttackLevel_(4)
        Damage(250)
        Unknown11092(1)
        AirUntechableTime(30)
        Hitstop(0)
        PushbackX(5000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(-500)
        AirPushbackY(22000)
        Unknown30056('f0d8ffff6400000000000000')
        Unknown9016(1)
        Unknown11057(800)
        DisableAttackRestOfMove()
        SLOT_57 = 7
        SLOT_2 = 15
        if SLOT_4:
            Damage(230)
            AttackP2(75)
            AirUntechableTime(30)
            SLOT_57 = 7
            SLOT_2 = 20

        def upon_12():
            SLOT_58 = 1
            SLOT_2 = (SLOT_2 - 1)
            Unknown23029(2, 7003, 0)
            if SLOT_56:
                SLOT_57 = (SLOT_57 + 1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 <= 0):
                Unknown23029(3, 7006, 0)
                clearUponHandler(3)
                sendToLabel(0)
    sprite('vr_dmy_tatsumaki', 2)
    GFX_0('AssaultSEMaster', -1)
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    Unknown3004(26)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    sprite('null', 5)
    DisableAttackRestOfMove()
    if SLOT_58:
        Unknown21012('50454c5f506572736f6e6141737361756c74457800000000000000000000000026000000')
        Unknown23029(3, 7005, 0)
        sendToLabel(10)
    ExitState()
    label(10)
    sprite('vr_dmy_tatsumaki', 2)
    RefreshMultihit()
    SFX_3('el050')
    SLOT_56 = 1
    SLOT_57 = (SLOT_57 + (-1))
    if (not SLOT_57):
        Unknown23029(3, 7006, 0)
        sendToLabel(0)
    loopRest()
    gotoLabel(10)
    label(0)
    sprite('vr_dmy_tatsumaki', 5)
    RefreshMultihit()
    AirHitstunAnimation(10)
    Damage(500)
    AirPushbackX(2500)
    AirPushbackY(40000)
    if SLOT_4:
        AirUntechableTime(55)
        AirPushbackX(15000)
        AirPushbackY(45000)
    sprite('null', 13)
    sprite('null', 10)
    Unknown21012('50454c5f506572736f6e6141737361756c74457800000000000000000000000028000000')

@State
def GarudineTatsumakiJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('ttef_garudainjizoku_tu')
        Unknown4003('656c65665f6761727564696e655f6a697a6f6b7530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()

        def upon_43():
            if (SLOT_48 == 7001):
                SLOT_54 = 1
            if (SLOT_48 == 7002):
                SLOT_56 = 1
            if (SLOT_48 == 7003):
                Unknown1099(7)
            if (SLOT_48 == 7004):
                sendToLabel(0)
    sprite('null', 1)
    GFX_0('GarudineTatsumakiStartMato', 100)
    sprite('null', 14)
    if SLOT_IsInOverdrive2:
        GFX_0('TatsumakiAAAA', 100)
    if SLOT_56:
        GFX_0('TatsumakiEx', 100)
    sprite('null', 5)
    Unknown3004(51)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown26('TatsumakiAAA')
    Unknown26('TatsumakiEx')
    Unknown1067(60)
    GFX_1('ttef_garudainfin_sb', 100)
    Unknown3004(-52)

@State
def GarudineTatsumakiStartMato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('656c65665f6761727564696e655f737461727430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 5)
    GFX_0('GarudineTatsumakiStart', 100)
    sprite('null', 5)
    GFX_0('GarudineTatsumakiStart', 100)
    sprite('null', 5)
    GFX_0('GarudineTatsumakiStart', 100)
    sprite('null', 10)
    GFX_0('GarudineTatsumakiStart', 100)

@State
def GarudineTatsumakiStart():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('656c65665f6761727564696e655f737461727430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 20)
    Unknown3004(51)
    Unknown1099(50)
    physicsYImpulse(10000)
    sprite('null', 10)
    Unknown1099(100)
    Unknown3004(-26)

@State
def PEL_PersonaShotEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000204e0000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(220)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown11092(1)
        AirUntechableTime(47)
        Hitstop(0)
        AirPushbackY(1000)
        AirPushbackX(100000)
        PushbackX(6000)
        YImpluseBeforeWallbounce(0)
        Unknown9178(1)
        WallbounceReboundTime(0)
        DisableAttackRestOfMove()
        callSubroutine('MahagioEffectInit')
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt402_00', 1)
    SFX_3('chain_move')
    sprite('tt402_01', 1)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 1)
    sprite('tt402_05', 1)
    sprite('tt402_06', 1)
    GFX_0('UltimateLaserJizokuEX', 0)
    SFX_3('el054')
    sprite('tt402_06', 1)
    sprite('tt402_07', 1)
    RefreshMultihit()
    sprite('tt402_07', 1)
    Unknown23022(0)
    sprite('tt402_08', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)
    RefreshMultihit()
    sprite('tt402_10', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)
    RefreshMultihit()
    sprite('tt402_06', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07', 2)
    RefreshMultihit()
    sprite('tt402_08', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)
    RefreshMultihit()
    sprite('tt402_10', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)
    RefreshMultihit()
    sprite('tt402_06', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07', 2)
    RefreshMultihit()
    sprite('tt402_08', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)
    RefreshMultihit()
    sprite('tt402_10', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)
    RefreshMultihit()
    sprite('tt402_06', 2)
    RefreshMultihit()
    sprite('tt402_07', 2)
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 2)
    Unknown23029(3, 4013, 0)
    Unknown2001()
    label(0)
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('tt402_09', 2)
    sprite('tt402_10', 2)
    sprite('tt402_11', 2)
    sprite('tt402_06', 2)
    sprite('tt402_07', 2)
    sprite('tt402_08', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def UltimateLaserJizokuEX():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('656c65665f6a696f64696e655f6a697a6f6b7530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 40)
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(-200)
    Unknown3004(-51)

@State
def PEL_PersonaShotExSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000204e0000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(210)
        AttackP2(75)
        Unknown11092(1)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(90)
        Hitstop(0)
        AirPushbackY(1000)
        AirPushbackX(100000)
        PushbackX(6000)
        YImpluseBeforeWallbounce(0)
        Unknown9178(1)
        WallbounceReboundTime(3)
        Unknown9366(12)
        DisableAttackRestOfMove()
        callSubroutine('MahagioEffectInit')
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt402_00', 1)
    SFX_3('chain_move')
    sprite('tt402_01', 1)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 1)
    sprite('tt402_05', 1)
    sprite('tt402_06ex', 1)
    SFX_3('el054')
    GFX_0('UltimateLaserJizokuSB', 0)
    Unknown36(1)
    Unknown1096(1500)
    teleportRelativeX(-33000)
    Unknown35()
    RefreshMultihit()
    sprite('tt402_06ex', 1)
    Unknown23022(0)
    sprite('tt402_07ex', 1)
    RefreshMultihit()
    sprite('tt402_07ex', 1)
    RefreshMultihit()
    sprite('tt402_08ex', 1)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_08ex', 1)
    RefreshMultihit()
    sprite('tt402_09ex', 1)
    RefreshMultihit()
    sprite('tt402_09ex', 1)
    RefreshMultihit()
    sprite('tt402_10ex', 1)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_10ex', 1)
    RefreshMultihit()
    sprite('tt402_11ex', 1)
    RefreshMultihit()
    sprite('tt402_11ex', 1)
    RefreshMultihit()
    sprite('tt402_07ex', 2)
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 2)
    sprite('tt402_00', 1)
    SFX_3('chain_move')
    sprite('tt402_01', 1)
    sprite('tt402_02', 2)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 2)
    sprite('tt402_06ex', 1)
    RefreshMultihit()
    GFX_0('UltimateLaserJizokuSB', 0)
    Unknown36(1)
    Unknown1096(1500)
    teleportRelativeX(-33000)
    Unknown35()
    SFX_3('el054')
    sprite('tt402_06ex', 1)
    RefreshMultihit()
    sprite('tt402_07ex', 1)
    RefreshMultihit()
    sprite('tt402_07ex', 1)
    RefreshMultihit()
    sprite('tt402_08ex', 1)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_08ex', 1)
    RefreshMultihit()
    sprite('tt402_09ex', 1)
    RefreshMultihit()
    sprite('tt402_09ex', 1)
    RefreshMultihit()
    sprite('tt402_10ex', 1)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_10ex', 1)
    RefreshMultihit()
    sprite('tt402_11ex', 1)
    RefreshMultihit()
    sprite('tt402_11ex', 1)
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 3)
    Unknown2001()
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def UltimateLaserJizokuSB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('656c65665f6a696f64696e655f6a697a6f6b7530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 25)
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(-200)
    Unknown3004(-51)

@State
def PEL_PersonaAntiAirEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        AttackLevel_(5)
        Damage(800)
        DisableAttackRestOfMove()
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(36000)
        Unknown11092(1)
        Unknown30055('d0dd06002800000000000000')
        Unknown30056('90d003002800000000000000')
        AirUntechableTime(60)
        Hitstop(3)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        Unknown9266(9)
        Unknown2037(0)

        def upon_12():
            if SLOT_2:
                clearUponHandler(12)
                SLOT_51 = 1
                sendToLabel(1)
        setInvincible(1)
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt403_00', 3)
    SFX_3('chain_move')
    sprite('tt403_01', 3)
    sprite('tt403_02', 3)
    sprite('tt403_03', 1)
    sprite('tt403_03', 3)
    GFX_0('ttef403_Zanzoh', 100)
    physicsXImpulse(70000)
    sprite('tt403_04', 2)
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    Unknown1019(20)
    sprite('tt403_05', 1)
    Unknown2037(1)
    Unknown1019(0)
    setInvincible(0)
    RefreshMultihit()
    Damage(2000)
    Hitstop(15)
    Unknown30055('f04902002800000000000000')
    sprite('tt403_05', 1)
    Unknown23022(0)
    sprite('tt403_05', 3)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)
    setInvincible(0)
    sprite('tt403_06', 20)
    sprite('tt403_06', 10)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(1)
    sprite('tt403_06', 4)
    Unknown23029(3, 4025, 0)
    sprite('tt403_07', 4)
    sprite('tt403_07', 20)
    GFX_0('403icecharge', 0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_41 <= 900000):
            clearUponHandler(3)
            sendToLabel(10)
    label(10)
    sprite('tt403_08', 4)
    clearUponHandler(3)
    SFX_3('slash_pole_middle')
    GFX_0('Mahabufudain_iceatk', 0)
    sprite('tt403_09', 4)
    GFX_0('Mahabufudain', 100)
    sprite('tt403_10', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def ttef403_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)

        def upon_33():
            Unknown23067('ttef_403_ice')
            Unknown4049(2000)
        Unknown4061(1)
        Unknown3032()
    sprite('vr_tt403_00', 3)
    sprite('vr_tt403_01', 2)
    sprite('vr_tt403_02', 4)
    Unknown4045('747465665f3430335f696365000000000000000000000000000000000000000000000000')
    Unknown3004(-63)

@State
def Mahabufudain():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(1)
        Unknown4003('656c65665f3430336d616861627566752e444947000000000000000000000000656c65665f3430336d616861627566755f3030302e6d6d6f7400000000000000')
        Unknown1096(1200)
        Unknown3001(0)
    sprite('null', 14)
    Unknown3004(60)
    sprite('null', 14)
    sprite('null', 10)
    Unknown23117(16777215, 10)
    Unknown3004(-26)

@State
def Mahabufudain_iceatk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(72)
        AttackP2(100)
        AirPushbackX(2500)
        AirPushbackY(25000)
        AirUntechableTime(60)
        Hitstop(12)
        Unknown9021(1)
        Unknown9266(9)
        DisableAttackRestOfMove()
        Unknown1072(-35000)

        def upon_43():
            if (SLOT_48 == 4026):
                clearUponHandler(43)
                AirPushbackX(2500)
                AirPushbackY(25000)
                FreezeDuration(50)
                FreezeCount(1)
            if (SLOT_48 == 4027):
                clearUponHandler(43)
                Damage(1000)
                AttackP1(60)
    sprite('null', 4)
    Unknown4010(2)
    sprite('vr_tt403ice00', 14)
    Unknown4010(0)
    sprite('vr_tt403ice00', 10)
    Unknown1110(50000, 0)
    RefreshMultihit()

    def upon_12():
        SFX_3('ice_fast')
    sprite('vr_tt403ice00', 6)
    GFX_0('Mahabufudain_move', 0)
    sprite('vr_tt403ice00', 3)
    Unknown1110(0, 0)
    Unknown3004(-90)

@State
def Mahabufudain_move():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1072(-35000)
        Unknown1110(20000, 0)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 1)
    GFX_0('403icemove', 100)
    sprite('null', 5)
    Unknown3004(-90)

@State
def __403icemove():

    def upon_IMMEDIATE():
        Unknown23067('ttef_403icemove')
        Unknown1072(55000)
    sprite('null', 5)

@State
def __403icecharge():

    def upon_IMMEDIATE():
        Unknown23067('ttef_403icecharge')
    sprite('null', 40)
    sprite('null', 20)
    Unknown3004(-13)

@State
def PEL_PersonaAntiAirExSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        AttackLevel_(5)
        Damage(1000)
        DisableAttackRestOfMove()
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(36000)
        Unknown11092(1)
        Hitstop(3)
        Unknown30055('d0dd06002800000000000000')
        Unknown30056('90d003002800000000000000')
        AirUntechableTime(60)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        Unknown9266(9)
        Unknown2037(0)

        def upon_12():
            if SLOT_2:
                clearUponHandler(12)
                SLOT_51 = 1
                sendToLabel(1)
        setInvincible(1)
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt403_00', 3)
    SFX_3('chain_move')
    sprite('tt403_01', 3)
    sprite('tt403_02', 3)
    sprite('tt403_03', 8)
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(10)
    physicsXImpulse(100000)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 <= 300000):
            sendToLabel(101)
    label(101)
    sprite('tt403_03', 3)
    clearUponHandler(3)
    GFX_0('ttef403_Zanzoh', 100)
    Unknown1019(40)
    sprite('tt403_04', 1)
    SFX_3('slash_blade_fast')
    Unknown1019(20)
    RefreshMultihit()
    sprite('tt403_04', 1)
    Unknown23022(0)
    sprite('tt403_05', 1)
    Unknown2037(1)
    Unknown1019(0)
    setInvincible(0)
    RefreshMultihit()
    Damage(2500)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown30055('f04902002800000000000000')
    Hitstop(15)
    sprite('tt403_05', 1)
    Unknown23022(0)
    sprite('tt403_05', 3)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)
    setInvincible(0)
    sprite('tt403_06', 20)
    sprite('tt403_06', 10)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(1)
    sprite('tt403_06', 4)
    Unknown23029(3, 4025, 0)
    sprite('tt403_07', 4)
    sprite('tt403_07', 20)
    GFX_0('403icecharge', 0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_41 <= 900000):
            clearUponHandler(3)
            sendToLabel(10)
    label(10)
    sprite('tt403_08', 4)
    clearUponHandler(3)
    SFX_3('slash_pole_middle')
    GFX_0('Mahabufudain_iceatk', 0)
    Unknown23029(1, 4026, 0)
    sprite('tt403_09', 4)
    GFX_0('Mahabufudain', 100)
    sprite('tt403_10', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaChargeShotEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        EnableCollision(0)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt405_00', 3)
    SFX_3('chain_move')
    sprite('tt405_01', 3)
    sprite('tt405_02', 3)
    sprite('tt405_03', 3)
    sprite('tt405_04', 3)
    sprite('tt405_05', 3)
    sprite('tt405_03', 3)
    sprite('tt405_04', 3)
    sprite('tt405_06', 2)
    sprite('tt405_06', 1)
    GFX_0('ChargeShotExAtk', 104)
    sprite('tt405_07', 3)
    SFX_3('hit_m_slow')
    sprite('tt405_08', 3)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 3)
    sprite('tt405_11', 1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def ChargeShotExAtk():

    def upon_IMMEDIATE():

        def upon_44():
            Unknown13(25)
        Unknown2037(0)

        def upon_32():
            Unknown2037(1)
        Unknown2053(1)
    sprite('null', 1)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(250000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 60)

@State
def ChargeShotExAtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(500)
        AirUntechableTime(29)
        Hitstop(0)
        ChipDamagePct(25)
        Unknown11110(80)
        PushbackX(50000)
        AirPushbackX(18000)
        AirPushbackY(12000)
        Unknown30055('f04902003200000032000000')
        Unknown30056('b0ad01001e0000001e000000')
        callSubroutine('MaharagidineParam')
        if SLOT_4:
            Damage(550)
            PushbackX(60000)
            AirPushbackX(12000)
            AirPushbackY(10000)
        teleportRelativeX(-125000)
    sprite('vr_el405_dmg00', 9)
    Unknown1067(75)
    if SLOT_4:
        Unknown1067(100)
    sprite('vr_el405_dmg00', 5)
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')

    def upon_44():
        DisableAttackRestOfMove()
    sprite('vr_el405_dmg00', 10)
    DisableAttackRestOfMove()
    Unknown3033()
    Unknown1067(30)
    Unknown23118(-16764161)
    Unknown3004(-25)

@Subroutine
def MaharagidineParam():
    GroundedHitstunAnimation(1)
    Unknown9021(1)
    Unknown9266(2)
    DisableAttackRestOfMove()
    Unknown11092(1)
    Unknown23182(2)
    Unknown3032()
    Unknown4003('656c65665f3430356869626173686972612e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23015(6)
    Unknown4015()
    Unknown3001(0)
    Unknown3004(45)
    Unknown1056(1200)
    Unknown1064(100)
    Unknown1088(10)

@State
def PEL_PersonaChargeShotExSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        Unknown2006()
        Unknown23078(1)
        callSubroutine('PEL_CheckWarp')
        EnableCollision(0)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt405_00', 3)
    SFX_3('chain_move')
    sprite('tt405_01', 3)
    sprite('tt405_02', 3)
    sprite('tt405_03', 3)
    sprite('tt405_04', 3)
    sprite('tt405_05', 3)
    sprite('tt405_03', 3)
    sprite('tt405_04', 3)
    sprite('tt405_06', 2)
    sprite('tt405_06', 1)
    GFX_0('ChargeShotExAtk', 104)
    Unknown21007(1, 32)
    sprite('tt405_07', 3)
    SFX_3('hit_m_slow')
    sprite('tt405_08', 3)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 4)
    sprite('tt405_09', 4)
    sprite('tt405_10', 4)
    sprite('tt405_11', 3)
    sprite('tt405_11', 1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaLandTrap():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000803801000000000000000000000000000000000000000000')
        Unknown2054(1)
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        callSubroutine('PEL_ForceWarp')
        Unknown2053(1)
        Unknown23066(1)
        Unknown23022(1)
        EnableCollision(0)
    sprite('tt431_00', 4)
    Unknown13(4)
    callSubroutine('SwordFireSet')
    SFX_3('chain_move')
    sprite('tt431_01', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_00', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_01', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_03', 2)
    callSubroutine('SwordFireSet2')
    sprite('tt431_04', 2)
    callSubroutine('SwordFireSet2')
    sprite('tt431_05', 2)
    callSubroutine('SwordFireSet2')
    GFX_0('Mahanmaon_search', -1)
    Unknown38(4, 1)
    sprite('tt431_06', 4)
    sprite('tt431_07', 4)
    sprite('tt431_08', 4)
    sprite('tt431_06', 4)
    sprite('tt431_07', 4)
    sprite('tt431_08', 4)
    sprite('tt431_06', 4)
    sprite('tt431_07', 4)
    sprite('tt431_08', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def Mahanmaon_search():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('656c65665f34333168616d615f7365617263682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('ttef_431hama_search')
        Unknown4011(3)
        Unknown23015(2)
        Unknown4015()
        Unknown3001(0)
        Unknown23089('0100000000000000000000000000000000000000000000000100000000000000')

        def upon_54():
            Unknown13(25)

        def upon_39():
            clearUponHandler(39)
            sendToLabel(0)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_19 < 200000):
                    if (SLOT_20 < 350000):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (SLOT_166 < 200000):
                    if (SLOT_167 < 350000):
                        clearUponHandler(3)
                        sendToLabel(1)
    sprite('null', 10)
    Unknown1086(22)
    teleportRelativeY(0)
    Unknown3004(25)
    sprite('null', 10)
    SFX_3('magiccircle_a')
    sprite('null', 600)
    Unknown2037(1)
    label(0)
    sprite('null', 10)
    Unknown3004(-25)
    ExitState()
    label(1)
    sprite('null', 10)
    GFX_0('Mahanmaon', 100)
    Unknown3004(-25)
    ExitState()

@State
def Mahanmaon():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        callSubroutine('ExSkillInit')
        AttackLevel_(5)
        Damage(330)
        AttackP2(80)
        Unknown11092(1)
        AirUntechableTime(75)
        Hitstop(0)
        AirPushbackX(0)
        AirPushbackY(0)
        YImpluseBeforeWallbounce(100)
        PushbackX(0)
        Unknown30055('000000003200000014000000')
        Unknown30056('c0d401003200000000000000')
        Unknown11068(1)
        Unknown9021(1)
        teleportRelativeY(0)
        Unknown3032()
        Unknown4003('656c65665f34333168616d612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('ttef_431hama')
        Unknown23015(2)
        Unknown4015()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_r', 100)
    RefreshMultihit()
    SFX_3('el055')
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_l', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_r', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_l', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 10)
    RefreshMultihit()
    Unknown11064(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    ChipDamagePct(0)
    AirPushbackX(0)
    AirPushbackY(30000)
    Unknown9095()

@State
def Hamathunder_r():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('656c65665f34333168616d617468756e6465722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown2054(1)
        Unknown1010(280000, 180000)
        Unknown1102(250, 0)
        Unknown4015()
    sprite('null', 25)
    Unknown3004(60)
    sprite('null', 5)
    Unknown3004(-60)

@State
def Hamathunder_l():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('656c65665f34333168616d617468756e6465722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown2054(1)
        Unknown1010(-280000, -180000)
        Unknown1102(250, 0)
        Unknown4015()
        Unknown3001(0)
    sprite('null', 25)
    Unknown3004(60)
    sprite('null', 5)
    Unknown3004(-60)

@State
def Hamathunder_c():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('656c65665f34333168616d617468756e6465722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown2054(1)
        Unknown1010(60000, -60000)
        Unknown1102(400, 200)
        Unknown4015()
        Unknown3001(0)
    sprite('null', 25)
    Unknown3004(60)
    sprite('null', 5)
    Unknown3004(-60)

@State
def PEL_PersonaAirTrap():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000803801000000000000000000000000000000000000000000')
        Unknown2054(1)
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        callSubroutine('PEL_ForceWarp')
        Unknown2053(1)
        Unknown23066(1)
        Unknown23022(1)
        EnableCollision(0)
    sprite('tt431_00', 4)
    teleportRelativeY(0)
    Unknown13(5)
    callSubroutine('SwordFireSet')
    SFX_3('chain_move')
    sprite('tt431_01', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_00', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_01', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)
    callSubroutine('SwordFireSet')
    sprite('tt431_03', 2)
    callSubroutine('SwordFireSet2')
    sprite('tt431_04', 2)
    callSubroutine('SwordFireSet2')
    sprite('tt431_05ex', 2)
    callSubroutine('SwordFireSet2')
    GFX_0('Mahamudo_on_search', -1)
    Unknown38(5, 1)
    sprite('tt431_06', 4)
    sprite('tt431_07', 4)
    sprite('tt431_08', 4)
    sprite('tt431_06', 4)
    sprite('tt431_07', 4)
    sprite('tt431_08', 4)
    sprite('tt431_06', 4)
    sprite('tt431_07', 4)
    sprite('tt431_08', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def Mahamudo_on_search():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('656c65665f3433316d75646f5f7365617263682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23067('ttef_431mudo_search')
        Unknown4015()
        Unknown23015(5)

        def upon_33():
            SLOT_51 = 1

        def upon_39():
            clearUponHandler(39)
            sendToLabel(0)
        Unknown1096(0)
        Unknown4011(3)
        Unknown23089('0100000000000000000000000000000000000000000000000100000000000000')

        def upon_54():
            Unknown13(25)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_19 < 600000):
                    if (SLOT_20 < 300000):
                        clearUponHandler(3)
                        sendToLabel(1)
                if (SLOT_166 < 600000):
                    if (SLOT_167 < 300000):
                        clearUponHandler(3)
                        sendToLabel(1)
    sprite('null', 5)
    sprite('null', 15)
    Unknown1086(3)
    Unknown1007(200000)
    Unknown1099(50)
    sprite('null', 5)
    Unknown1099(0)
    SFX_3('magiccircle_b')
    sprite('null', 600)
    Unknown2037(1)
    label(0)
    sprite('null', 10)
    Unknown3004(-25)
    ExitState()
    label(1)
    sprite('null', 10)
    GFX_0('Mahamudo_on', 100)
    Unknown3004(-25)
    ExitState()

@State
def Mahamudo_on():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        callSubroutine('ExSkillInit')
        AttackLevel_(5)
        Damage(700)
        AttackP2(80)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Hitstop(0)
        AirUntechableTime(50)
        AirPushbackY(20000)
        Unknown30056('d019fdff6400000000000000')
        Unknown11084(1)
        Unknown9021(1)
        Unknown9266(10)
        Unknown11068(1)

        def upon_12():
            Unknown4011(0)
            sendToLabel(0)
        Unknown3032()
        Unknown4003('656c65665f3433316d75646f2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
        Unknown4015()

        def upon_CLEAR_OR_EXIT():
            if (SLOT_51 >= 3):
                GFX_0('MudoBall_el', 100)
                SLOT_51 = 0
            else:
                SLOT_51 = (SLOT_51 + 1)
    sprite('vr_dmy_mahamudoon00', 4)
    GFX_0('Mudothunder_up', 100)
    GFX_0('Mudothunder_down', 100)
    SFX_3('el056')
    sprite('vr_dmy_mahamudoon00', 5)
    sprite('vr_dmy_mahamudoon01', 5)
    GFX_0('Mudothunder_up', 100)
    GFX_0('Mudothunder_down', 100)
    sprite('vr_dmy_mahamudoon01', 10)
    Unknown3004(-26)
    DisableAttackRestOfMove()
    clearUponHandler(3)
    loopRest()
    ExitState()
    label(0)
    sprite('vr_dmy_mahamudoon01', 5)
    clearUponHandler(12)
    Unknown4011(0)
    DisableAttackRestOfMove()
    AirPushbackX(0)
    Unknown9083()
    Unknown9095()
    Unknown11001(0, 8, 8)
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 70)
    RefreshMultihit()
    Unknown11064(0)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(150000)
    AirPushbackY(10000)
    Unknown9095()
    Hitstop(0)
    Unknown11001(0, 0, 8)
    Unknown9178(1)
    WallbounceReboundTime(5)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')

@State
def MudoBall_el():

    def upon_IMMEDIATE():
        GFX_2('ttef_431mudoball')
        Unknown2054(1)
        physicsXImpulse(90000)
        Unknown1025(10000, -10000)
        Unknown1026(10000, -10000)
        Unknown1099(20)
        Unknown1011(50000, -50000)
        Unknown1010(25000, -25000)
    sprite('null', 6)
    Unknown1019(6)
    YAccel(6)
    Unknown1096(50)
    Unknown3001(50)
    Unknown3004(20)
    Unknown1099(150)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    Unknown1019(1000)
    YAccel(1000)
    Unknown1099(30)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    Unknown3001(180)
    Unknown3004(-20)
    Unknown1019(15)
    YAccel(15)
    sprite('null', 2)
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 20)

@State
def Mudothunder_up():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('656c65665f3433316d75646f7468756e6465722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown2054(1)
        Unknown1011(150000, 15000)
        Unknown1070(80, 0)
        Unknown4015()
        Unknown1071(0, 70)
        Unknown3001(0)
    sprite('null', 20)
    Unknown3004(60)
    sprite('null', 5)
    Unknown3004(-60)

@State
def Mudothunder_down():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4003('656c65665f3433316d75646f7468756e6465722e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown2054(1)
        Unknown1011(-150000, -15000)
        Unknown1070(80, 0)
        Unknown4015()
        Unknown1071(0, 70)
        Unknown3001(0)
    sprite('null', 20)
    Unknown3004(60)
    sprite('null', 5)
    Unknown3004(-60)

@State
def PEL_PersonaSpecialHeal():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000402bfeff50c3000000000000000000000000000000000000')
        Unknown2054(1)
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        callSubroutine('PEL_ForceWarp')
        Unknown2053(1)
        Unknown23066(1)
        Unknown23022(1)
        EnableCollision(0)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(0)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(1)
    sprite('tt432_00', 3)
    sprite('tt432_01', 3)
    sprite('tt432_02', 3)
    sprite('tt432_03', 3)
    sprite('tt432_04', 3)
    sprite('tt432_05', 4)
    label(0)
    sprite('tt432_06', 4)
    GFX_0('diarahanSoulkanoke', 100)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    SFX_3('el053')
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('tt432_08', 4)
    sprite('tt432_06', 4)
    sprite('tt432_07', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def diarahanSoulkanoke():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3033()
        Unknown2054(1)
        Unknown3001(0)
        Unknown4061(3)
        Unknown2019(500)
    sprite('vr_tt432_00', 4)
    Unknown3004(26)
    sprite('vr_tt432_01', 4)
    GFX_0('soulaura', 0)
    sprite('vr_tt432_02', 4)
    sprite('vr_tt432_03', 4)
    sprite('vr_tt432_01', 4)
    GFX_0('SyuyakuSoul', 0)
    sprite('vr_tt432_02', 4)
    sprite('vr_tt432_03', 4)
    sprite('vr_tt432_01', 4)
    sprite('vr_tt432_02', 4)
    sprite('vr_tt432_03', 4)
    sprite('vr_tt432_01', 4)
    Unknown21012('736f756c6175726100000000000000000000000000000000000000000000000020000000')
    Unknown3004(-17)
    sprite('vr_tt432_02', 4)
    sprite('vr_tt432_03', 4)
    sprite('vr_tt432_01', 4)
    sprite('vr_tt432_02', 4)
    sprite('vr_tt432_03', 4)
    sprite('vr_tt432_01', 4)
    sprite('vr_tt432_02', 4)
    sprite('vr_tt432_03', 4)

@State
def soulaura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ttef_soulaura_g2')
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3004(-26)

@State
def SyuyakuSoul():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('656c65665f736f756c5f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
    sprite('null', 35)
    sprite('null', 5)
    Unknown3004(-51)

@State
def PEL_Persona5CPS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        callSubroutine('PartnerSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(1500)
        Unknown11092(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(20000)
        AirPushbackY(20000)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        AirUntechableTime(29)
        DisableAttackRestOfMove()
        Unknown2015(180)
        EnableCollision(1)
        Unknown2053(1)
        Unknown2034(1)
        callSubroutine('PEL_ForceWarp')

        def upon_ON_HIT_OR_BLOCK():
            if SLOT_2:
                clearUponHandler(10)
                Unknown23029(3, 1004, 0)
    sprite('tt204_00', 3)
    sprite('tt204_01', 4)
    sprite('tt204_02', 3)
    GFX_0('ttef204_Zanzoh', 100)
    SFX_3('hit_m_slow')
    physicsXImpulse(50000)
    sprite('tt204_03', 1)
    RefreshMultihit()
    sprite('tt204_03', 2)
    Unknown23022(0)
    DisableAttackRestOfMove()
    Unknown1019(50)
    sprite('tt204_04', 9)
    Unknown1019(0)
    sprite('tt204_05', 3)
    GFX_0('ttef204_Zanzoh2', 100)
    physicsXImpulse(65000)
    SFX_3('chain_move')
    sprite('tt204_06', 3)
    SFX_3('hit_m_slow')
    Unknown1019(50)
    sprite('tt204_07', 1)
    RefreshMultihit()
    AirUntechableTime(36)
    Unknown9190(1)
    YImpluseBeforeWallbounce(0)
    AirPushbackX(6000)
    AirPushbackY(-50000)
    Unknown9118(45)
    PushbackX(16000)
    Unknown1019(0)
    Unknown2037(1)
    sprite('tt204_07', 2)
    Unknown23029(3, 2011, 0)
    DisableAttackRestOfMove()
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('tt204_08', 4)
    sprite('tt204_09', 4)
    sprite('tt204_10', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(580)
    sprite('keep', 16)
    Unknown1019(0)
    DisableAttackRestOfMove()
    Unknown21012('747465663230345f5a616e7a6f6832000000000000000000000000000000000020000000')
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaAntiAirPS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        callSubroutine('PartnerSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(1800)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2500)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown9266(9)
        DisableAttackRestOfMove()
        EnableCollision(1)
        Unknown2053(1)
        Unknown2034(1)
        callSubroutine('PEL_ForceWarp')
    sprite('tt403_00', 2)
    SFX_3('chain_move')
    sprite('tt403_01', 2)
    sprite('tt403_03', 3)
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 2)
    SFX_3('slash_blade_fast')
    sprite('tt403_05', 1)
    RefreshMultihit()
    sprite('tt403_05', 3)
    Unknown23029(3, 3015, 0)
    Unknown23022(0)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)
    sprite('tt403_06', 20)
    sprite('tt403_06', 10)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaAntiAirPSSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PEL_SPAttackInit')
        callSubroutine('PartnerSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(1800)
        DisableAttackRestOfMove()
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(36000)
        Unknown11092(1)
        Unknown30055('d0dd06002800000000000000')
        AirUntechableTime(60)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        Unknown9266(9)

        def upon_12():
            clearUponHandler(12)
            SLOT_51 = 1
            sendToLabel(1)
        EnableCollision(1)
        Unknown2053(1)
        Unknown2034(1)
        callSubroutine('PEL_ForceWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('tt403_00', 2)
    SFX_3('chain_move')
    sprite('tt403_01', 2)
    sprite('tt403_03', 3)
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 2)
    SFX_3('slash_blade_fast')
    sprite('tt403_05', 1)
    RefreshMultihit()
    sprite('tt403_05', 1)
    Unknown23022(0)
    sprite('tt403_05', 3)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)
    sprite('tt403_06', 20)
    sprite('tt403_06', 10)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(1)
    sprite('tt403_06', 4)
    Unknown23029(3, 4025, 0)
    sprite('tt403_07', 4)
    sprite('tt403_07', 20)
    GFX_0('403icecharge', 0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_41 <= 900000):
            clearUponHandler(3)
            sendToLabel(10)
    label(10)
    sprite('tt403_08', 4)
    clearUponHandler(3)
    SFX_3('slash_pole_middle')
    GFX_0('Mahabufudain_iceatk', 0)
    Unknown23029(1, 4027, 0)
    sprite('tt403_09', 4)
    GFX_0('Mahabufudain', 100)
    sprite('tt403_10', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 4)
    sprite('tt403_12', 4)
    sprite('tt403_11', 2)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaShotPS():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000204e0000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PEL_SPAttackInit')
        callSubroutine('PartnerSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(450)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(90)
        Hitstop(0)
        Unknown11092(1)
        AirPushbackY(1000)
        AirPushbackX(100000)
        PushbackX(6000)
        YImpluseBeforeWallbounce(0)
        Unknown9178(1)
        WallbounceReboundTime(3)
        DisableAttackRestOfMove()
        callSubroutine('MahagioEffectInit')
        Unknown2053(1)
        Unknown2034(1)
        callSubroutine('PEL_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
        loopRelated(17, 50)

        def upon_17():
            sendToLabel(1)
    sprite('tt402_00', 2)
    SFX_0('chain_move')
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    label(0)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 2)
    sprite('tt402_05', 1)
    sprite('tt402_06', 1)
    SFX_3('el054')
    GFX_0('UltimateLaserJizokuSB', 0)
    RefreshMultihit()
    sprite('tt402_06', 1)
    Unknown23022(0)
    sprite('tt402_07', 2)
    RefreshMultihit()
    sprite('tt402_08', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)
    RefreshMultihit()
    sprite('tt402_10', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)
    RefreshMultihit()
    sprite('tt402_06', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07', 2)
    RefreshMultihit()
    sprite('tt402_08', 2)
    RefreshMultihit()
    sprite('tt402_09', 2)
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 3)
    Unknown2001()
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaShotPSSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000204e0000000000000000000080841e00c0bdf0ff40420f00')
        callSubroutine('PEL_SPAttackInit')
        callSubroutine('PartnerSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(310)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(90)
        Hitstop(0)
        Unknown11092(1)
        AirPushbackY(1000)
        AirPushbackX(100000)
        PushbackX(6000)
        YImpluseBeforeWallbounce(0)
        Unknown9178(1)
        WallbounceReboundTime(3)
        DisableAttackRestOfMove()
        callSubroutine('MahagioEffectInit')
        Unknown2053(1)
        Unknown2034(1)
        callSubroutine('PEL_CheckWarp')
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
        loopRelated(17, 50)

        def upon_17():
            sendToLabel(1)
    sprite('tt402_00', 2)
    SFX_0('chain_move')
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    label(0)
    sprite('tt402_00', 2)
    sprite('tt402_01', 2)
    sprite('tt402_02', 2)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tt402_03', 2)
    sprite('tt402_04', 2)
    sprite('tt402_05', 2)
    sprite('tt402_05', 1)
    sprite('tt402_06ex', 1)
    SFX_3('el054')
    GFX_0('UltimateLaserJizokuSB', 0)
    Unknown21007(1, 33)
    Unknown36(1)
    Unknown1096(2000)
    teleportRelativeX(-33000)
    Unknown35()
    RefreshMultihit()
    sprite('tt402_06ex', 1)
    Unknown23022(0)
    sprite('tt402_07ex', 2)
    RefreshMultihit()
    sprite('tt402_08ex', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09ex', 2)
    RefreshMultihit()
    sprite('tt402_10ex', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11ex', 2)
    RefreshMultihit()
    sprite('tt402_06ex', 2)
    RefreshMultihit()
    sprite('tt402_07ex', 2)
    RefreshMultihit()
    sprite('tt402_08ex', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09ex', 2)
    RefreshMultihit()
    sprite('tt402_10ex', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11ex', 2)
    RefreshMultihit()
    sprite('tt402_06ex', 2)
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07ex', 2)
    RefreshMultihit()
    sprite('tt402_08ex', 2)
    RefreshMultihit()
    sprite('tt402_09ex', 2)
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 3)
    Unknown2001()
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('tt402_06', 3)
    sprite('tt402_07', 3)
    sprite('tt402_08', 3)
    sprite('tt402_09', 3)
    sprite('tt402_10', 3)
    sprite('tt402_11', 3)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaUltimateThrow():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000f0490200000000000000000080841e000000000000000000')
        callSubroutine('PEL_DDAttackInit')
        Unknown17011('PEL_PersonaUltimateThrowExe', 3, 0, 0)
        AttackP1(80)
        Unknown30048(1)
        Unknown11032('20bf0200b03cffffffffffffffffffff')
        Unknown11054(200000)
        Unknown11002(-1)
        Unknown30061(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
        Unknown2053(1)
        Unknown2034(1)

        def upon_12():
            Unknown23029(3, 5021, 0)
    sprite('tt433_00', 4)
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_03', 3)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
        if (not SLOT_52):
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11032('c0270900b03cffffffffffffffffffff')
                Unknown11054(1000000)
            else:
                SLOT_52 = 1
                Unknown11032('20bf0200b03cffffffffffffffffffff')
                Unknown11054(200000)
                if SLOT_53:
                    DisableAttackRestOfMove()
    physicsXImpulse(50000)
    SFX_3('chain_move')
    sprite('tt433_04', 1)
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt433_04', 2)
    if SLOT_52:
        DisableAttackRestOfMove()
    else:
        SLOT_53 = 1
    sprite('tt205_07', 2)
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaUltimateThrowExe():

    def upon_IMMEDIATE():
        callSubroutine('PEL_DDAttackInit')
        Unknown17012(3, 1, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown30079(1)
        DisableAttackRestOfMove()
        Unknown13024(0)
        Unknown2053(1)
        Unknown2015(750)
        Unknown23022(1)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20003(0)
    sprite('tt433_04', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)
    sprite('tt433_15', 9)
    sprite('tt433_15', 21)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_16', 6)
    sprite('tt433_17', 20)
    sprite('tt433_18', 1)
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(8500)
    AttackP2(60)
    Unknown30079(0)
    Unknown11064(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7500)
    AirPushbackY(40000)
    AirUntechableTime(60)
    Hitstop(17)
    Unknown9016(1)
    SFX_3('chain_move')
    MinimumDamagePct(25)
    Unknown5005(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown3001(255)
    Unknown35()
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000022000000')
    ScreenShake(60000, 10000)
    Unknown20000(0)
    Unknown20003(0)
    Unknown13024(1)
    sprite('tt433_20', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaUltimateThrowSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000f0490200000000000000000080841e000000000000000000')
        callSubroutine('PEL_DDAttackInit')
        Unknown17011('PEL_PersonaUltimateThrowSPExe', 3, 0, 0)
        AttackP1(80)
        Unknown30048(1)
        Unknown11032('20bf0200b03cffffffffffffffffffff')
        Unknown11054(200000)
        Unknown11002(-1)
        Unknown30061(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
        Unknown2053(1)
        Unknown2034(1)

        def upon_12():
            Unknown23029(3, 5022, 0)
    sprite('tt433_00', 4)
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_03', 3)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
        if (not SLOT_52):
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11032('c0270900b03cffffffffffffffffffff')
                Unknown11054(1000000)
            else:
                SLOT_52 = 1
                Unknown11032('20bf0200b03cffffffffffffffffffff')
                Unknown11054(200000)
                if SLOT_53:
                    DisableAttackRestOfMove()
    physicsXImpulse(50000)
    SFX_3('chain_move')
    sprite('tt433_04', 1)
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt433_04', 2)
    if SLOT_52:
        DisableAttackRestOfMove()
    else:
        SLOT_53 = 1
    sprite('tt205_07', 2)
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaUltimateThrowSPExe():

    def upon_IMMEDIATE():
        callSubroutine('PEL_DDAttackInit')
        Unknown17012(3, 1, 0)
        AttackLevel_(4)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown30079(1)
        DisableAttackRestOfMove()
        Unknown13024(0)
        Unknown2053(1)
        Unknown2015(750)
        Unknown23022(1)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20003(0)
    sprite('tt433_04', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)
    sprite('tt433_15', 9)
    sprite('tt433_15', 21)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_15', 10)
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_16', 15)
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)
    ScreenShake(8000, 8000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)
    ScreenShake(8000, 8000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_18', 1)
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)
    RefreshMultihit()
    AttackLevel_(5)
    Unknown30079(0)
    Damage(10000)
    AttackP2(60)
    Unknown30079(0)
    Unknown11064(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(5000)
    AirPushbackY(60000)
    AirUntechableTime(60)
    YImpluseBeforeWallbounce(2200)
    Unknown9310(10)
    Hitstop(22)
    Unknown9016(1)
    SFX_3('chain_move')
    MinimumDamagePct(23)
    Unknown5005(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown3001(255)
    Unknown35()
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000022000000')
    ScreenShake(90000, 20000)
    Unknown20000(0)
    Unknown20003(0)
    Unknown13024(1)
    sprite('tt433_20', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaDUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000f0490200000000000000000080841e000000000000000000')
        callSubroutine('PEL_DDAttackInit')
        AttackLevel_(0)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown30048(1)
        Unknown11032('20bf0200b03cffffffffffffffffffff')
        Unknown11054(200000)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
        Unknown2053(1)
        Unknown2034(1)
    sprite('tt433_00', 4)
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_03', 3)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
    physicsXImpulse(50000)
    SFX_3('chain_move')
    sprite('tt433_04', 3)
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)
    enterState('PEL_PersonaDUOGrip')

@State
def PEL_PersonaDUOGrip():

    def upon_IMMEDIATE():
        callSubroutine('PEL_DDAttackInit')
        Unknown17011('PEL_PersonaDUOExe', 3, 0, 0)
        Unknown2006()
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        HitAirUnblockable(4)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        Unknown23022(1)
        DisableAttackRestOfMove()
        Unknown30031(0)

        def upon_12():
            Unknown23029(3, 5023, 0)
    sprite('tt433_04', 3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaDUOExe():

    def upon_IMMEDIATE():
        callSubroutine('PEL_DDAttackInit')
        Unknown17012(3, 1, 0)
        AttackLevel_(4)
        Damage(0)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown30079(1)
        DisableAttackRestOfMove()
        Unknown13024(0)
        Unknown2053(1)
        Unknown2015(750)
        Unknown23022(1)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20003(0)
    sprite('tt433_04', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)
    sprite('tt433_15', 9)
    sprite('tt433_15', 21)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_16', 6)
    sprite('tt433_17', 20)
    sprite('tt433_18', 1)
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2500)
    Unknown30079(0)
    Unknown11064(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7500)
    AirPushbackY(40000)
    AirUntechableTime(60)
    Hitstop(17)
    Unknown9016(1)
    SFX_3('chain_move')
    Unknown5005(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown3001(255)
    Unknown35()
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000022000000')
    ScreenShake(60000, 10000)
    Unknown20000(0)
    Unknown20003(0)
    Unknown13024(1)
    sprite('tt433_20', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaDUOSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000f0490200000000000000000080841e000000000000000000')
        callSubroutine('PEL_DDAttackInit')
        AttackLevel_(0)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown30048(1)
        Unknown11032('20bf0200b03cffffffffffffffffffff')
        Unknown11054(200000)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(1)
        callSubroutine('PEL_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
        Unknown2053(1)
        Unknown2034(1)
    sprite('tt433_00', 4)
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_02', 4)
    sprite('tt433_00', 4)
    sprite('tt433_01', 4)
    sprite('tt433_03', 3)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
    physicsXImpulse(50000)
    SFX_3('chain_move')
    sprite('tt433_04', 3)
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)
    enterState('PEL_PersonaDUOSPGrip')

@State
def PEL_PersonaDUOSPGrip():

    def upon_IMMEDIATE():
        callSubroutine('PEL_DDAttackInit')
        Unknown17011('PEL_PersonaDUOSPExe', 3, 0, 0)
        Unknown2006()
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        HitAirUnblockable(4)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        Unknown23022(1)
        DisableAttackRestOfMove()
        Unknown30031(0)

        def upon_12():
            Unknown23029(3, 5024, 0)
    sprite('tt433_04', 3)
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)
    Unknown1019(0)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('tt205_10', 4)
    sprite('tt205_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def PEL_PersonaDUOSPExe():

    def upon_IMMEDIATE():
        callSubroutine('PEL_DDAttackInit')
        Unknown17012(3, 1, 0)
        AttackLevel_(4)
        Damage(0)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        Hitstop(0)
        Unknown30079(1)
        DisableAttackRestOfMove()
        Unknown13024(0)
        Unknown2053(1)
        Unknown2015(750)
        Unknown23022(1)

        def upon_STATE_END():
            Unknown20000(0)
            Unknown20003(0)
    sprite('tt433_04', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)
    sprite('tt433_15', 9)
    sprite('tt433_15', 21)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_15', 10)
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_16', 15)
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)
    ScreenShake(8000, 8000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)
    ScreenShake(8000, 8000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_18', 1)
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)
    RefreshMultihit()
    AttackLevel_(5)
    Unknown30079(0)
    Damage(3000)
    Unknown30079(0)
    Unknown11064(0)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(5000)
    AirPushbackY(60000)
    AirUntechableTime(60)
    YImpluseBeforeWallbounce(2200)
    Unknown9310(10)
    Hitstop(22)
    Unknown9016(1)
    SFX_3('chain_move')
    Unknown5005(1)
    Unknown36(22)
    Unknown3038(0)
    Unknown3001(255)
    Unknown35()
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000022000000')
    ScreenShake(90000, 20000)
    Unknown20000(0)
    Unknown20003(0)
    Unknown13024(1)
    sprite('tt433_20', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('tt433_21', 4)
    sprite('tt433_22', 4)
    sprite('tt433_23', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def ttef433_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3032()
    sprite('vr_tt433_00', 4)
    sprite('vr_tt433_01', 4)
    sprite('vr_tt433_02', 3)
    Unknown3004(-63)

@State
def ttef433_hitsugi():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown23015(2)
        Unknown2005()
        Unknown2053(1)
        teleportRelativeX(-320000)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        sendToLabelUpon(34, 2)
    sprite('vr_tt433_10', 2)
    GFX_1('elef_hitugi_entry', 100)
    sprite('vr_tt433_10add01', 2)
    sprite('vr_tt433_10add02', 2)
    sprite('vr_tt433_10add02', 3)
    sprite('vr_tt433_10add02', 1)
    teleportRelativeX(-12000)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(12000)
    sprite('vr_tt433_11', 2)
    sprite('vr_tt433_12', 3)
    sprite('vr_tt433_13', 32767)
    label(0)
    sprite('vr_tt433_13', 3)
    teleportRelativeX(-48000)
    sprite('vr_tt433_13', 3)
    teleportRelativeX(36000)
    sprite('vr_tt433_13', 32767)
    teleportRelativeX(-12000)
    label(1)
    sprite('vr_tt433_11', 3)
    sprite('vr_tt433_10add02', 2)
    Unknown23118(-14081)
    Unknown23119(-16777216, 8, -1)
    GFX_0('ttef433_hitsugi_kusari', 100)
    GFX_1('elef_hitugi_kousoku', 0)
    Unknown3029(1)
    Unknown3069(2)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(-12000)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(12000)
    loopRest()
    label(10)
    sprite('vr_tt433_10add02', 1)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(-6000)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(6000)
    sprite('vr_tt433_10add02', 1)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(12000)
    sprite('vr_tt433_10add02', 2)
    teleportRelativeX(-12000)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 1)
    GFX_0('ttef433_hitsugi_crash', 100)
    Unknown26('ttef433_hitsugi_kusari')

@State
def ttef433_hitsugi_kusari():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown3033()
        GFX_0('ttef433_hitsugi_kusari_flash', 100)
    sprite('vr_ttef433_chain', 32767)

@State
def ttef433_hitsugi_kusari_flash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(0)
    label(0)
    sprite('vr_ttef433_chain', 25)
    Unknown3004(10)
    sprite('vr_ttef433_chain', 25)
    Unknown3004(-10)
    loopRest()
    gotoLabel(0)

@State
def ttef433_hitsugi_crash():

    def upon_IMMEDIATE():
        teleportRelativeX(64000)
        Unknown1007(256000)
        GFX_2('elef_hitugi_crash')
        GFX_0('ttef433_hitsugi_crash_A', 100)
        GFX_0('ttef433_hitsugi_crash_B', 100)
        GFX_0('ttef433_hitsugi_crash_C', 100)
        GFX_0('ttef433_hitsugi_crash_D', 100)
    sprite('null', 3)
    SFX_3('guard_hit_l')
    sprite('null', 3)
    SFX_3('guard_slash_l')
    sprite('null', 3)
    SFX_3('guard_hit_l')
    sprite('null', 111)

@State
def ttef433_hitsugi_crash_A():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown3004(-5)
        Unknown2019(1000)
        teleportRelativeX(64000)
        Unknown1007(128000)
        physicsXImpulse(30000)
        Unknown1025(-3000, 3000)
        physicsYImpulse(30000)
        Unknown1026(-5000, 8000)

        def upon_CLEAR_OR_EXIT():
            Unknown1019(90)
            Unknown1021(-1200)

        def upon_LANDING():
            Unknown14()
    sprite('vr_tt433_10ex01', 32767)

@State
def ttef433_hitsugi_crash_B():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown3004(-5)
        Unknown2019(-500)
        teleportRelativeX(-64000)
        Unknown1007(128000)
        physicsXImpulse(-30000)
        Unknown1025(-3000, 3000)
        physicsYImpulse(30000)
        Unknown1026(-5000, 8000)

        def upon_CLEAR_OR_EXIT():
            Unknown1019(90)
            Unknown1021(-1200)

        def upon_LANDING():
            Unknown14()
    sprite('vr_tt433_10ex02', 32767)

@State
def ttef433_hitsugi_crash_C():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown3004(-5)
        Unknown2019(1001)
        teleportRelativeX(64000)
        Unknown1007(-80000)
        physicsXImpulse(10000)
        Unknown1025(-1000, 1000)
        physicsYImpulse(20000)
        Unknown1026(0, 5000)

        def upon_CLEAR_OR_EXIT():
            Unknown1019(90)
            Unknown1021(-1000)

        def upon_LANDING():
            Unknown14()
    sprite('vr_tt433_10ex03', 32767)

@State
def ttef433_hitsugi_crash_D():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3032()
        Unknown3004(-5)
        Unknown2019(-100)
        teleportRelativeX(-64000)
        Unknown1007(-80000)
        physicsXImpulse(-10000)
        Unknown1025(-1000, 1000)
        physicsYImpulse(20000)
        Unknown1026(0, 5000)

        def upon_CLEAR_OR_EXIT():
            Unknown1019(90)
            Unknown1021(-1000)

        def upon_LANDING():
            Unknown14()
    sprite('vr_tt433_10ex04', 32767)

@State
def PEL_PersonaAstralHeat():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PEL_DDAttackInit')
        Unknown23028(6, 1)
        Unknown2006()
        callSubroutine('PEL_ForceWarp')
        Unknown2054(1)
        Unknown23022(1)
        Unknown2053(1)
        Unknown2034(1)
        sendToLabelUpon(32, 1)
    sprite('tt450_00ab', 4)
    sprite('tt450_01ab', 4)
    sprite('tt450_02ab', 4)
    sprite('tt450_00ab', 4)
    sprite('tt450_01ab', 4)
    sprite('tt450_02ab', 4)
    sprite('tt450_00ab', 4)
    sprite('tt450_01ab', 4)
    sprite('tt450_02ab', 4)
    sprite('tt450_03ab', 4)
    sprite('tt450_04ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    label(0)
    sprite('tt450_05ab', 4)
    sprite('tt450_06ab', 4)
    sprite('tt450_07ab', 4)
    SFX_3('el006')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

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
        Unknown13044(1)
        Unknown6001(1)
        Unknown1000(-650000)
        teleportRelativeY(-292000)
        Unknown1096(1350)
        Unknown3001(0)
        Unknown2037(0)

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
def PersonaEntry():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        Unknown2015(180)
        Unknown4007(3)
        Unknown23015(2)
        teleportRelativeY(50000)
    sprite('tt600_00', 4)
    SFX_3('chain_move')
    sprite('tt600_01', 4)
    sprite('tt600_02', 4)
    sprite('tt600_00', 4)
    SFX_3('chain_move')
    sprite('tt600_01', 4)
    sprite('tt600_02', 4)
    sprite('tt600_00', 4)
    SFX_3('chain_move')
    sprite('tt600_01', 4)
    sprite('tt600_02', 4)
    sprite('tt600_03', 5)
    sprite('tt600_04', 5)
    sprite('tt600_05', 25)
    sprite('tt600_07', 4)
    GFX_0('EnterHoukouLoop', 0)
    SFX_3('el006')
    sprite('tt600_08', 4)
    SFX_3('chain_move')
    sprite('tt600_09', 4)
    sprite('tt600_07', 4)
    sprite('tt600_08', 4)
    SFX_3('chain_move')
    sprite('tt600_09', 4)
    sprite('tt600_07', 4)
    sprite('tt600_08', 4)
    SFX_3('chain_move')
    sprite('tt600_09', 4)
    sprite('tt600_07', 4)
    sprite('tt600_08', 4)
    sprite('tt600_09', 4)
    sprite('keep', 32767)
    enterState('PersonaDeleteAndIdling')

@State
def EnterHoukou():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('656c65665f686f756b6f7573686f636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(150)
    sprite('null', 3)
    sprite('null', 5)
    Unknown1099(80)
    Unknown3004(-51)
    loopRest()

@State
def EnterHoukouLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)

@State
def elef600_card():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(0)
        Unknown3032()
    GFX_0('elef_cardlight', 100)
    GFX_0('elef600_cardlight_add', 100)
    sprite('vr_el600_00', 4)
    Unknown3001(0)
    Unknown3004(16)
    physicsYImpulse(500)
    sprite('vr_el600_01', 4)
    sprite('vr_el600_02', 4)
    sprite('vr_el600_00', 4)
    sprite('vr_el600_01', 4)
    sprite('vr_el600_02', 4)
    sprite('vr_el600_00', 4)
    sprite('vr_el600_01', 4)
    sprite('vr_el600_02', 4)
    sprite('vr_el600_00', 4)
    sprite('vr_el600_01', 4)
    sprite('vr_el600_02', 4)
    sprite('vr_el600_00', 4)
    sprite('vr_el600_01', 4)
    sprite('vr_el600_02', 4)
    GFX_1('persona_enter_ply', 100)

@State
def elef600_cardlight_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 3)
    GFX_1('elef_cardlight_add', 100)
    gotoLabel(0)

@State
def elef601_EntryLight():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3033()
        Unknown3026(-256)
        Unknown3001(0)
        Unknown3004(25)
        Unknown1056(2000)
        Unknown1064(6000)
        teleportRelativeX(32000)
        teleportRelativeY(0)
        Unknown2019(100)
        GFX_0('elef601_EntryLightPtc', 100)
        sendToLabelUpon(32, 0)
    sprite('vr_elef601_light', 16)
    Unknown1059(40)
    sprite('vr_elef601_light', 32767)
    Unknown1059(2)
    loopRest()
    label(0)
    sprite('vr_elef601_light', 20)
    Unknown3004(-12)
    Unknown1059(-50)
    Unknown21012('656c65663630315f456e7472794c69676874507463000000000000000000000020000000')

@State
def elef601_EntryLightPtc():

    def upon_IMMEDIATE():
        GFX_2('elef_entry_ptc')
        Unknown4010(2)
        Unknown3001(0)
        Unknown3004(25)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown3004(-12)

@State
def elef601_EntryBookEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4054(5)
        Unknown23067('elef_del_book')
        Unknown1074(-5000)
    sprite('null', 20)
    Unknown1099(20)
    sprite('null', 10)
    Unknown1099(0)
    sprite('null', 10)
    Unknown1099(-20)
    Unknown3004(-25)

@State
def elef601_EntryBook():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown3001(0)
        Unknown3004(10)
        Unknown2019(100)
        Unknown1096(0)
    sprite('vr_el601_08', 20)
    Unknown1099(50)
    sprite('vr_el601_08', 32767)
    Unknown1099(0)

    def upon_CLEAR_OR_EXIT():
        Unknown1021(-110)

@State
def elef610_door():

    def upon_IMMEDIATE():
        teleportRelativeX(-256000)
        Unknown1007(8000)
        Unknown3032()
        Unknown4061(2)
        Unknown13044(1)
    sprite('vr_el610_00', 6)
    SFX_3('distortion_b')
    sprite('vr_el610_01', 6)
    sprite('vr_el610_02', 6)
    sprite('vr_el610_03', 220)
    sprite('vr_el610_02', 6)
    SFX_3('distortion_b')
    sprite('vr_el610_01', 6)

@State
def elef610_door_add():

    def upon_IMMEDIATE():
        teleportRelativeX(-256000)
        Unknown1007(8000)
        Unknown3033()
        Unknown4061(2)
        Unknown13044(1)
    sprite('null', 18)
    sprite('vr_el610_10', 220)
    Unknown3001(0)
    Unknown3004(64)
    sprite('vr_el610_10', 12)
    sprite('vr_el610_10', 64)
    Unknown3004(-4)
    GFX_1('elef_win_door', 0)

@State
def PersonaMatchWin():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown23023()
        Unknown23184('0300000064000000b0cbfcff1873010000000000000000000000000000000000')
        callSubroutine('PEL_AttackInit')
        Unknown2006()
        callSubroutine('PEL_CheckWarp')
        Unknown23015(5)
        Unknown2053(1)
        Unknown2019(-100)
    sprite('tt611_00', 5)
    SFX_3('chain_move')
    sprite('tt611_01', 5)
    sprite('tt611_02', 5)
    sprite('tt611_03', 5)
    sprite('tt611_04', 5)
    sprite('tt611_05', 8)
    sprite('tt611_06', 6)
    label(0)
    sprite('tt611_07', 5)
    SFX_3('cloth_l')
    sprite('tt611_08', 5)
    sprite('tt611_09', 5)
    gotoLabel(0)

@State
def elef611_WinCard():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 2)
    GFX_0('elef611_WinCard00', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard01', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard02', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard03', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard04', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard05', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard06', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard07', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard08', 100)
    sprite('null', 2)
    GFX_0('elef611_WinCard09', 100)
    sprite('null', 32767)

@State
def elef611_WinCard00():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one')
        Unknown4010(2)
        physicsXImpulse(1000)
        physicsYImpulse(12000)
        Unknown1026(-1000, 1000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-800)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard01():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one_re')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(-100)
        physicsYImpulse(12000)
        Unknown1026(-1000, 1000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-900)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard02():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(500)
        physicsYImpulse(12000)
        Unknown1026(-1000, 1000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-950)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard03():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one_re')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(50)
        physicsYImpulse(12000)
        Unknown1026(-1000, 1000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1000)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard04():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(25)
        physicsYImpulse(12000)
        Unknown1026(-1000, 1000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1100)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard05():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one_re')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(700)
        physicsYImpulse(12000)
        Unknown1026(-1000, 1000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1150)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard06():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(500)
        physicsYImpulse(12000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1200)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard07():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one_re')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(300)
        physicsYImpulse(12000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1250)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard08():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(600)
        physicsYImpulse(11500)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1350)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_WinCard09():

    def upon_IMMEDIATE():
        GFX_2('elef_flycard_one_re')
        Unknown4010(2)
        physicsXImpulse(1000)
        Unknown1019(400)
        physicsYImpulse(11000)

        def upon_CLEAR_OR_EXIT():
            Unknown1021(-1400)
    sprite('null', 30)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_Book():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
    label(0)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    loopRest()
    gotoLabel(0)

@State
def elef611_DelBook():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown3004(-10)
        GFX_0('elef611_DelBookEff', 100)
        Unknown26('elef611_Book')

        def upon_CLEAR_OR_EXIT():
            Unknown1098(95)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)
    sprite('vr_el611_01', 4)
    sprite('vr_el611_02', 4)
    sprite('vr_el611_03', 4)

@State
def elef611_DelBookEff():

    def upon_IMMEDIATE():
        Unknown4054(5)
        Unknown23067('elef_del_book')
        Unknown4010(2)
        Unknown3001(0)
        Unknown3004(25)
        Unknown1074(-10000)
    sprite('null', 10)
    sprite('null', 20)
    Unknown1099(-50)

@State
def PersonaMatchWinSP():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PEL_AttackInit')
        callSubroutine('PEL_CheckWarp')
        Unknown2053(1)
        Unknown2015(180)
        Unknown4007(3)
        Unknown23015(2)
        teleportRelativeY(50000)
    sprite('tt600_00', 4)
    SFX_3('chain_move')
    sprite('tt600_01', 4)
    sprite('tt600_02', 4)
    sprite('tt600_00', 4)
    SFX_3('chain_move')
    sprite('tt600_01', 4)
    sprite('tt600_02', 4)
    sprite('tt600_00', 4)
    SFX_3('chain_move')
    sprite('tt600_01', 4)
    sprite('tt600_02', 4)
    sprite('tt600_03', 5)
    sprite('tt600_04', 5)
    sprite('tt600_05', 25)
    sprite('tt600_07', 4)
    GFX_0('EnterHoukouLoop', 0)
    SFX_3('el006')
    sprite('tt600_08', 4)
    SFX_3('chain_move')
    label(0)
    sprite('tt600_09', 4)
    sprite('tt600_07', 4)
    sprite('tt600_08', 4)
    gotoLabel(0)