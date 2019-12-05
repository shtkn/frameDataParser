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
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('50454c5f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PEL_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PEL_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
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
    sprite('keep', 32767)	# 1-32767
    if SLOT_143:
        GFX_0('PersonaDeleteEffect', 100)
        SFX_3('persona_disappear')
    SLOT_11 = 10
    SLOT_59 = (-1)
    enterState('PEL_PersonaWait')

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
        callSubroutine('PEL_ReceptionSignal')
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

@State
def elef_cardlight():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 60)	# 1-60
    GFX_2('elef_cardlight')
    gotoLabel(0)

@State
def elef_cardlight_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 3)	# 1-3
    GFX_1('elef_cardlight_add', 100)
    gotoLabel(0)

@State
def elef121_Burst():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown23067('elef_burst')
        Unknown2054(1)
    sprite('null', 60)	# 1-60

@State
def elef200_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(2)
        Unknown3033()
    sprite('vr_el200_00', 16)	# 1-16
    Unknown3004(-42)

@State
def elef207_all():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1074(-12500)
    sprite('null', 7)	# 1-7
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
    sprite('null', 32767)	# 8-32774
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
    sprite('vr_el207_00', 32767)	# 1-32767

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
    sprite('dmy_el208', 10)	# 1-10	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(30000)
    label(1)
    sprite('dmy_el208', 12)	# 11-22	 **attackbox here**
    Unknown3004(-30)
    physicsXImpulse(1000)
    Unknown2001()
    sprite('null', 6)	# 23-28

@State
def dmy_el208_tatsumaki():

    def upon_IMMEDIATE():
        GFX_2('elef_208tornade')
        Unknown4011(3)
    sprite('null', 5)	# 1-5
    teleportRelativeY(0)
    Unknown3001(0)
    sprite('null', 14)	# 6-19
    teleportRelativeX(150000)
    teleportRelativeY(0)
    sprite('null', 5)	# 20-24
    Unknown3004(175)
    sprite('null', 25)	# 25-49
    GFX_0('dmy_el208_col', 100)
    sprite('null', 10)	# 50-59
    label(0)
    sprite('null', 16)	# 60-75
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
    sprite('dmy_el208_tatsumaki_col', 4)	# 1-4
    StartMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 5-7
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    Unknown2037(6)
    label(1)
    sprite('dmy_el208_tatsumaki_col', 3)	# 8-10
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
    sprite('vr_elef203_cardshot00', 1)	# 1-1	 **attackbox here**
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
    sprite('vr_elef203_cardshot01', 1)	# 2-2	 **attackbox here**
    sprite('vr_elef203_cardshot02', 1)	# 3-3	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef203_cardshot03', 1)	# 4-4	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot00', 1)	# 5-5	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef203_cardshot01', 1)	# 6-6	 **attackbox here**
    sprite('vr_elef203_cardshot02', 1)	# 7-7	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_elef203_cardshot03', 1)	# 8-8	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef203_cardshot00', 1)	# 9-9	 **attackbox here**
    AirPushbackX(-15000)
    PushbackX(-19800)
    Unknown1067(0)
    physicsYImpulse(0)
    physicsXImpulse(20000)
    setGravity(0)
    sprite('vr_elef203_cardshot01', 1)	# 10-10	 **attackbox here**
    physicsXImpulse(10000)
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot02', 1)	# 11-11	 **attackbox here**
    physicsXImpulse(5000)
    sprite('vr_elef203_cardshot03', 1)	# 12-12	 **attackbox here**
    physicsXImpulse(0)
    sprite('vr_elef203_cardshot00', 1)	# 13-13	 **attackbox here**
    Unknown1067(-50)

    def upon_45():
        Unknown2071('0300000050c3000090d003000a00000000000000')
    setGravity(0)
    RefreshMultihit()
    AirHitstunAnimation(11)
    Unknown30055('f0d8ffff6400000064000000')
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot01', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef203_cardshot02', 1)	# 15-15	 **attackbox here**
    sprite('vr_elef203_cardshot03', 1)	# 16-16	 **attackbox here**
    SFX_3('slash_knife_slow')
    RefreshMultihit()
    sprite('vr_elef203_cardshot00', 1)	# 17-17	 **attackbox here**
    sprite('vr_elef203_cardshot01', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef203_cardshot02', 1)	# 19-19	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_elef203_cardshot03', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    Unknown30055('b88800006400000064000000')
    AirPushbackX(-500)
    AirPushbackY(12000)
    sprite('vr_elef203_cardshot00', 1)	# 21-21	 **attackbox here**
    sprite('vr_elef203_cardshot01', 1)	# 22-22	 **attackbox here**
    DisableAttackRestOfMove()

    def upon_45():
        Unknown2071('030000006079feff90d003003200000000000000')
    sprite('vr_elef203_cardshot02', 1)	# 23-23	 **attackbox here**
    loopRest()
    clearUponHandler(1)
    sprite('null', 1)	# 24-24
    GFX_1('elef_cardshotcrash05', 100)

@State
def elef203_CardShotCrash():

    def upon_IMMEDIATE():
        GFX_2('elef_cardshotcrash')
    sprite('null', 60)	# 1-60

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
    sprite('null', 40)	# 1-40

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
    sprite('null', 10)	# 1-10
    sprite('null', 10)	# 11-20
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
    sprite('null', 12)	# 1-12
    sprite('null', 10)	# 13-22
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
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
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
    sprite('null', 14)	# 1-14
    sprite('null', 10)	# 15-24
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
    sprite('null', 14)	# 1-14
    sprite('null', 10)	# 15-24
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
    sprite('null', 14)	# 1-14
    sprite('null', 10)	# 15-24
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
    sprite('null', 15)	# 1-15
    sprite('null', 15)	# 16-30
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
    sprite('null', 15)	# 1-15
    sprite('null', 15)	# 16-30
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
    sprite('vr_elef251_cardshotair00', 1)	# 1-1	 **attackbox here**
    Unknown1056(900)
    Unknown1064(1000)
    Unknown1059(100)
    Unknown1067(50)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)	# 2-2	 **attackbox here**
    teleportRelativeX(150000)
    RefreshMultihit()
    sprite('vr_elef251_cardshotair02', 1)	# 3-3	 **attackbox here**
    sprite('vr_elef251_cardshotair00', 1)	# 4-4	 **attackbox here**
    teleportRelativeX(100000)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)	# 5-5	 **attackbox here**
    sprite('vr_elef251_cardshotair02', 1)	# 6-6	 **attackbox here**
    teleportRelativeX(50000)
    sprite('vr_elef251_cardshotair00', 1)	# 7-7	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)	# 8-8	 **attackbox here**
    teleportRelativeX(25000)
    sprite('vr_elef251_cardshotair02', 1)	# 9-9	 **attackbox here**
    sprite('vr_elef251_cardshotair00', 1)	# 10-10	 **attackbox here**
    Unknown1059(0)
    Unknown1067(0)
    PushbackX(-22000)
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)	# 11-11	 **attackbox here**
    sprite('vr_elef251_cardshotair02', 1)	# 12-12	 **attackbox here**
    sprite('vr_elef251_cardshotair00', 1)	# 13-13	 **attackbox here**
    AirPushbackX(-12000)
    physicsXImpulse(-59000)
    Unknown3029(1)
    Unknown3071(3)
    RefreshMultihit()
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)	# 14-14	 **attackbox here**
    sprite('vr_elef251_cardshotair02', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef251_cardshotair00', 1)	# 16-16	 **attackbox here**
    SFX_3('slash_knife_slow')
    sprite('vr_elef251_cardshotair01', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('vr_elef251_cardshotair02', 1)	# 18-18	 **attackbox here**
    sprite('vr_elef251_cardshotair00', 1)	# 19-19	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('vr_elef251_cardshotair01', 1)	# 20-20	 **attackbox here**
    loopRest()
    clearUponHandler(1)
    sprite('null', 1)	# 21-21
    teleportRelativeX(-82000)
    Unknown1007(-20000)
    Unknown4054(5)
    Unknown4045('656c65665f6361726473686f746372617368303500000000000000000000000064000000')

@State
def elef251_CardShotCrashAir():

    def upon_IMMEDIATE():
        GFX_2('elef_cardshotcrashair')
    sprite('null', 60)	# 1-60

@State
def elef400_HandAuraSuccess():

    def upon_IMMEDIATE():
        GFX_2('elef_400_miss')
        Unknown1096(1500)
    sprite('null', 60)	# 1-60

@State
def elef400_Soul():

    def upon_IMMEDIATE():
        GFX_0('elef400_SoulA', 100)
        GFX_0('elef400_SoulB', 100)

        def upon_CLEAR_OR_EXIT():
            Unknown4049(1500)
            Unknown4045('656c65665f3430305f68616e64617572615f616674657200000000000000000064000000')
            Unknown1021(-1200)
    sprite('null', 6)	# 1-6
    Unknown1099(-20)
    sprite('null', 32)	# 7-38
    Unknown1028(-700)
    physicsYImpulse(24000)
    sprite('null', 1)	# 39-39
    GFX_0('elef400_HandAuraSuccess', 100)

@State
def elef400_SoulA():

    def upon_IMMEDIATE():
        GFX_2('elef_400_soul_bodyA')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
    sprite('null', 32767)	# 1-32767

@State
def elef400_SoulB():

    def upon_IMMEDIATE():
        GFX_2('elef_400_soul_bodyB')
        Unknown4010(2)
        Unknown4007(2)
        Unknown4013(2)
        Unknown4009(2)
    sprite('null', 32767)	# 1-32767

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
    sprite('null', 20)	# 1-20
    physicsXImpulse(14000)
    sprite('null', 5)	# 21-25
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)	# 26-29
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)	# 30-30
    GFX_0('elef400_LOVERS', 100)

@State
def elef400_LOVERS():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f6c6f766572735f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_lovers_bom', 100)
    sprite('null', 9)	# 1-9
    sprite('null', 12)	# 10-21
    Unknown7007('70656c3230325f3000000000000000006400000070656c3230325f3100000000000000006400000070656c3230325f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('badst_charm_damage')
    Unknown1099(0)
    GFX_1('elef_card_lovers', 100)

@State
def elef400_EnemyCard_DEATH():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)	# 1-20
    physicsXImpulse(14000)
    sprite('null', 5)	# 21-25
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)	# 26-29
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)	# 30-30
    GFX_0('elef400_DEATH', 100)

@State
def elef400_DEATH():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f64656174685f646566000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_death_bom', 100)
    sprite('null', 9)	# 1-9
    SFX_3('damage_slash_mh')
    SFX_3('cut_l')
    SFX_3('slash_blade_fast')
    sprite('null', 4)	# 10-13
    Unknown7007('70656c3230335f3000000000000000006400000070656c3230335f3100000000000000006400000070656c3230335f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1099(0)
    GFX_1('elef_card_death', 100)
    sprite('null', 8)	# 14-21
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
    sprite('null', 10)	# 1-10

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
    sprite('null', 10)	# 1-10

@State
def elef400_EnemyCard_DEVIL():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)	# 1-20
    physicsXImpulse(14000)
    sprite('null', 5)	# 21-25
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)	# 26-29
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)	# 30-30
    GFX_0('elef400_DEVIL', 100)

@State
def elef400_DEVIL():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f646576696c5f646566000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_devil_bom', 100)
            SFX_3('blaze_short')
    sprite('null', 9)	# 1-9
    sprite('null', 1)	# 10-10
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
    sprite('null', 11)	# 11-21
    SFX_3('distortion_a')

@State
def elef400_DEVIL_EYE():

    def upon_IMMEDIATE():
        GFX_2('elef_card_devil')
    sprite('null', 12)	# 1-12

@State
def elef400_EnemyCard_TOWER():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f7572615f6465660000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardInit')
    sprite('null', 20)	# 1-20
    physicsXImpulse(14000)
    sprite('null', 5)	# 21-25
    clearUponHandler(3)
    Unknown1099(0)
    Unknown1074(0)
    Unknown1084(1)
    sprite('null', 4)	# 26-29
    Unknown1059(-200)
    Unknown23119(-1, 20, 1)
    sprite('null', 1)	# 30-30
    GFX_0('elef400_TOWER', 100)

@State
def elef400_TOWER():

    def upon_IMMEDIATE():
        Unknown4003('656c65665f636172645f746f7765725f646566000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('ThrowCardActivateInit')

        def upon_STATE_END():
            GFX_1('elef_card_tower_bom', 100)
            SFX_3('thunder_s')
    sprite('null', 9)	# 1-9
    sprite('null', 12)	# 10-21
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
    sprite('null', 60)	# 1-60
    loopRest()
    label(0)
    sprite('null', 5)	# 61-65
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
    sprite('null', 6)	# 1-6
    Unknown3001(0)
    Unknown3004(50)
    SFX_3('distortion_b')
    sprite('null', 6)	# 7-12
    Unknown3004(0)
    label(0)
    sprite('null', 6)	# 13-18
    SFX_3('distortion_b')
    sprite('null', 6)	# 19-24
    gotoLabel(0)
    label(1)
    sprite('null', 10)	# 25-34
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
    sprite('null', 240)	# 1-240
    Unknown20000(1)
    label(1)
    sprite('null', 10)	# 241-250
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
    sprite('vr_dmy_tatsumaki', 1)	# 1-1
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 10)	# 2-11
    DisableAttackRestOfMove()
    ExitState()
    label(0)
    sprite('vr_dmy_tatsumaki', 110)	# 12-121
    clearUponHandler(12)
    sprite('vr_dmy_tatsumaki', 25)	# 122-146
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
    sprite('vr_dmy_tatsumaki', 10)	# 147-156
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
    sprite('null', 8)	# 1-8
    Unknown3001(0)
    Unknown3004(32)
    sprite('null', 8)	# 9-16
    sprite('null', 4)	# 17-20
    Unknown3004(0)
    sprite('null', 20)	# 21-40
    sprite('null', 1)	# 41-41
    Unknown3001(0)
    GFX_0('elef407_card_top_end', 100)

@State
def elef407_card_under():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('656c65665f343037636172645f726f742e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
    sprite('null', 8)	# 1-8
    Unknown3001(0)
    Unknown3004(32)
    sprite('null', 8)	# 9-16
    sprite('null', 4)	# 17-20
    Unknown3004(0)
    sprite('null', 20)	# 21-40
    sprite('null', 1)	# 41-41
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
    sprite('null', 20)	# 1-20
    physicsYImpulse(-11200)

@State
def elef407_card_under_end():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('656c65665f343037636172645f656e64322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        GFX_2('elef_407card')
    sprite('null', 20)	# 1-20
    physicsYImpulse(11200)
    sprite('null', 20)	# 21-40
    physicsYImpulse(0)

@State
def elef407_pillar():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown4007(22)
        GFX_2('elef_407pillar')
        Unknown1007(224000)
    sprite('null', 15)	# 1-15
    Unknown3001(0)
    Unknown3004(16)
    sprite('null', 15)	# 16-30
    sprite('null', 10)	# 31-40
    Unknown1059(-85)
    Unknown1067(-10)
    Unknown36(22)
    Unknown1059(-100)
    Unknown35()
    sprite('null', 1)	# 41-41
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
    sprite('null', 1)	# 1-1
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
    sprite('vr_el402_card', 4)	# 1-4
    sprite('vr_el402_card', 32767)	# 5-32771
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef402_ply_garu_infinity():

    def upon_IMMEDIATE():
        GFX_2('elef_card_ply_garu')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767

@State
def elef402_ply_jio():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef402_ply_jio_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_jio', 100)
        Unknown4010(2)
    sprite('vr_el402_card', 4)	# 1-4
    sprite('vr_el402_card', 32767)	# 5-32771
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef402_ply_jio_infinity():

    def upon_IMMEDIATE():
        GFX_2('elef_card_ply_jio')
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 32767)	# 1-32767

@State
def elef403_ply_bufu():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef403_ply_bufu_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_bufu', 100)
    sprite('vr_el403_card', 4)	# 1-4
    sprite('vr_el403_card', 32767)	# 5-32771
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef403_ply_bufu_infinity():

    def upon_IMMEDIATE():
        Unknown23067('elef_card_ply_bufu')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(4000)
    sprite('null', 32767)	# 1-32767

@State
def elef403_ply_ragi():

    def upon_IMMEDIATE():
        callSubroutine('SpecialCardInit')
        GFX_0('elef403_ply_ragi_infinity', 100)

        def upon_STATE_END():
            GFX_1('elef_card_crash_ragi', 100)
    sprite('vr_el403_card', 4)	# 1-4
    sprite('vr_el403_card', 32767)	# 5-32771
    Unknown1059(0)
    Unknown1056(1000)

@State
def elef403_ply_ragi_infinity():

    def upon_IMMEDIATE():
        GFX_2('elef_card_ply_ragi')
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(4000)
    sprite('null', 32767)	# 1-32767

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
    sprite('null', 4)	# 1-4
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)	# 5-8
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    sprite('null', 4)	# 9-12
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)	# 13-16
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    sprite('null', 4)	# 17-20
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)	# 21-24
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    sprite('null', 4)	# 25-28
    GFX_0('elef431_WhiteCard', 100)
    GFX_0('elef431_CardWind1', 100)
    sprite('null', 4)	# 29-32
    GFX_0('elef431_BlackCard', 100)
    GFX_0('elef431_CardWind2', 100)
    loopRest()
    sprite('null', 32767)	# 33-32799

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
    sprite('null', 30)	# 1-30
    sprite('null', 10)	# 31-40
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
    sprite('null', 30)	# 1-30
    sprite('null', 10)	# 31-40
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
    sprite('null', 25)	# 1-25
    Unknown3004(10)
    sprite('null', 25)	# 26-50
    Unknown3004(-10)
    ExitState()
    label(0)
    sprite('null', 10)	# 51-60
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
    sprite('null', 25)	# 1-25
    Unknown3004(10)
    sprite('null', 25)	# 26-50
    Unknown3004(-10)
    ExitState()
    label(0)
    sprite('null', 10)	# 51-60
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
    sprite('vr_elef431_mudo', 32767)	# 1-32767

@State
def elef431_WhitePick():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2054(1)
    sprite('vr_elef431_mao', 32767)	# 1-32767

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
    sprite('vr_el432_00', 4)	# 1-4
    GFX_0('KaihukuAura', 1)
    GFX_1('ttef_kaihuku_cl', 0)
    sprite('vr_el432_01', 4)	# 5-8
    sprite('vr_el432_02', 4)	# 9-12
    sprite('vr_el432_01', 4)	# 13-16
    sprite('vr_el432_02', 4)	# 17-20
    sprite('vr_el432_01', 4)	# 21-24
    sprite('vr_el432_02', 4)	# 25-28
    sprite('vr_el432_01', 4)	# 29-32
    sprite('vr_el432_02', 4)	# 33-36
    sprite('vr_el432_01', 4)	# 37-40
    sprite('vr_el432_02', 4)	# 41-44
    sprite('vr_el432_01', 4)	# 45-48
    sprite('vr_el432_02', 4)	# 49-52
    sprite('vr_el432_01', 4)	# 53-56
    sprite('vr_el432_02', 4)	# 57-60
    sprite('vr_el432_01', 4)	# 61-64
    sprite('vr_el432_02', 4)	# 65-68
    sprite('vr_el432_01', 4)	# 69-72
    sprite('vr_el432_02', 4)	# 73-76
    sprite('vr_el432_01', 4)	# 77-80
    sprite('vr_el432_02', 4)	# 81-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_el432_01', 4)	# 85-88
    Unknown3004(-17)
    sprite('vr_el432_02', 4)	# 89-92
    sprite('vr_el432_00', 4)	# 93-96
    sprite('vr_el432_01', 4)	# 97-100
    sprite('vr_el432_02', 4)	# 101-104
    sprite('vr_el432_00', 4)	# 105-108
    sprite('vr_el432_01', 4)	# 109-112
    sprite('vr_el432_02', 4)	# 113-116
    sprite('vr_el432_00', 4)	# 117-120
    sprite('vr_el432_01', 4)	# 121-124
    sprite('vr_el432_02', 4)	# 125-128
    sprite('vr_el432_00', 4)	# 129-132
    ExitState()

@State
def KaihukuAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('656c65665f6b616968756b75617572615f30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
        Unknown3001(0)
    sprite('null', 20)	# 1-20
    GFX_1('ttef_kaihukuaura_la', 100)
    Unknown3004(26)
    sprite('null', 20)	# 21-40
    Unknown3004(-17)
    Unknown1059(10)

@State
def elef430_Concentraite():

    def upon_IMMEDIATE():
        GFX_2('elef_concentrate')
        Unknown4007(2)
        Unknown2054(1)
        physicsYImpulse(6000)
    sprite('null', 45)	# 1-45
    GFX_0('elef430_ConcentraitePtc', 100)
    sprite('null', 25)	# 46-70
    Unknown3004(-10)

@State
def elef430_ConcentraitePtc():

    def upon_IMMEDIATE():
        GFX_2('elef_concentrate_ptc')
        Unknown2054(1)
        physicsYImpulse(5000)
    sprite('null', 130)	# 1-130

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
    sprite('null', 5)	# 1-5
    Unknown1099(25)
    sprite('null', 32767)	# 6-32772
    Unknown1099(0)
    loopRest()
    label(0)
    clearUponHandler(33)
    sprite('null', 10)	# 32773-32782
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(-75)
    ExitState()
    label(1)
    clearUponHandler(32)
    sprite('null', 10)	# 32783-32792
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
    sprite('null', 5)	# 1-5
    Unknown1086(22)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(175)
    sprite('null', 25)	# 6-30
    GFX_0('elef450_CounterCardAtk', 100)
    sprite('null', 10)	# 31-40
    label(0)
    sprite('null', 16)	# 41-56
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
    sprite('dmy_el208_tatsumaki_col', 4)	# 1-4
    StartMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 5-7
    RefreshMultihit()
    SFX_3('slash_pole_slow')
    sprite('dmy_el208_tatsumaki_col', 3)	# 8-10
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 11-13
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 14-16
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 17-19
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 20-22
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 23-25
    RefreshMultihit()
    sprite('dmy_el208_tatsumaki_col', 3)	# 26-28
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
    sprite('null', 5)	# 1-5
    Unknown1099(25)
    sprite('null', 32767)	# 6-32772
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 10)	# 32773-32782
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
    sprite('null', 5)	# 1-5
    Unknown1099(25)
    sprite('null', 32767)	# 6-32772
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 10)	# 32773-32782
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
    sprite('null', 5)	# 1-5
    Unknown1099(25)
    sprite('null', 32767)	# 6-32772
    Unknown1099(0)
    loopRest()
    label(0)
    sprite('null', 10)	# 32773-32782
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
    sprite('null', 32767)	# 1-32767

@State
def elef450_CardLayParent():

    def upon_IMMEDIATE():
        Unknown2055(72)
    label(0)
    sprite('null', 1)	# 1-1
    GFX_0('elef450_CardLay', 100)
    sprite('null', 2)	# 2-3
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
    sprite('null', 120)	# 1-120
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
    sprite('vr_elef450_cardlay', 30)	# 1-30
    DisableAttackRestOfMove()
    sprite('vr_elef450_cardlay', 32767)	# 31-32797
    RefreshMultihit()

@State
def elef450_cardA():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown23067('elef_450_cardA')
        Unknown1096(750)
    sprite('null', 32767)	# 1-32767

@State
def elef450_cardB():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
    label(0)
    sprite('null', 40)	# 1-40
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
    sprite('null', 40)	# 1-40

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
    sprite('null', 10)	# 1-10
    Unknown3004(-15)
    sprite('null', 90)	# 11-100
    Unknown3004(0)
    sprite('null', 32767)	# 101-32867

    def upon_CLEAR_OR_EXIT():
        Unknown1057(8)
        Unknown1065(5)
    label(0)
    sprite('null', 10)	# 32868-32877
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
    sprite('ichigeki', 15)	# 1-15	 **attackbox here**
    Unknown3004(5)
    sprite('ichigeki', 32767)	# 16-32782	 **attackbox here**
    label(0)
    sprite('ichigeki', 15)	# 32783-32797	 **attackbox here**
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
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 32767)	# 32768-65534
    clearUponHandler(3)
    physicsYImpulse(0)
    label(1)
    sprite('null', 10)	# 65535-65544

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
    sprite('null', 30)	# 1-30
    Unknown1099(80)
    GFX_0('elef450_PowUpA', 100)
    sprite('null', 30)	# 31-60
    Unknown1101(80)
    GFX_0('elef450_PowUpB', 100)
    sprite('null', 30)	# 61-90
    Unknown1101(80)
    GFX_0('elef450_PowUpC', 100)
    sprite('null', 30)	# 91-120
    Unknown1101(80)
    GFX_0('elef450_PowUpD', 100)
    sprite('null', 30)	# 121-150
    Unknown1101(80)
    sprite('null', 90)	# 151-240
    Unknown1101(80)
    Unknown1099(10)
    clearUponHandler(3)
    sprite('null', 32767)	# 241-33007
    loopRest()
    label(0)
    sprite('null', 2)	# 33008-33009
    Unknown1007(-1050000)
    Unknown1096(2000)
    sprite('null', 2)	# 33010-33011
    Unknown1056(1600)
    Unknown1064(1200)
    sprite('null', 6)	# 33012-33017
    Unknown1059(2000)
    Unknown1067(2000)
    sprite('null', 60)	# 33018-33077
    physicsXImpulse(0)
    physicsYImpulse(0)
    sprite('null', 25)	# 33078-33102
    Unknown3004(-10)
    sprite('null', 30)	# 33103-33132
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
    sprite('null', 32767)	# 1-32767

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
    sprite('null', 32767)	# 1-32767

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
    sprite('null', 32767)	# 1-32767

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
    sprite('null', 32767)	# 1-32767

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
    sprite('null', 32767)	# 1-32767
    label(1)
    sprite('null', 30)	# 32768-32797
    sprite('null', 30)	# 32798-32827
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
    sprite('vr_elef450_damage_num', 20)	# 1-20
    sprite('vr_elef450_damage_num', 25)	# 21-45
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
    sprite('tt204_00', 3)	# 1-3
    sprite('tt204_01', 4)	# 4-7
    sprite('tt204_02', 3)	# 8-10
    GFX_0('ttef204_Zanzoh', 100)
    SFX_3('hit_m_slow')
    sprite('tt204_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('tt204_03', 2)	# 12-13	 **attackbox here**
    Unknown23022(0)
    DisableAttackRestOfMove()
    sprite('tt204_04', 9)	# 14-22
    sprite('tt204_05', 3)	# 23-25
    GFX_0('ttef204_Zanzoh2', 100)
    physicsXImpulse(85000)
    SFX_3('chain_move')
    sprite('tt204_06', 3)	# 26-28
    SFX_3('hit_m_slow')
    sprite('tt204_07', 1)	# 29-29	 **attackbox here**
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
    sprite('tt204_07', 2)	# 30-31	 **attackbox here**
    Unknown23029(3, 2011, 0)
    DisableAttackRestOfMove()
    sprite('tt204_08', 4)	# 32-35
    sprite('tt204_09', 4)	# 36-39
    sprite('tt204_10', 4)	# 40-43
    sprite('tt204_08', 4)	# 44-47
    sprite('tt204_09', 4)	# 48-51
    sprite('tt204_10', 4)	# 52-55
    sprite('tt204_08', 4)	# 56-59
    sprite('tt204_09', 4)	# 60-63
    sprite('tt204_10', 4)	# 64-67
    sprite('tt204_08', 4)	# 68-71
    sprite('tt204_09', 4)	# 72-75
    sprite('tt204_10', 4)	# 76-79
    sprite('keep', 32767)	# 80-32846
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(580)
    sprite('keep', 16)	# 32847-32862
    Unknown1019(0)
    DisableAttackRestOfMove()
    Unknown21012('747465663230345f5a616e7a6f6832000000000000000000000000000000000020000000')
    sprite('keep', 32767)	# 32863-65629
    enterState('PersonaDeleteAndIdling')

@State
def ttef204_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3032()
    sprite('vr_tt204_00', 3)	# 1-3
    sprite('vr_tt204_01', 3)	# 4-6
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
    sprite('vr_tt204_10', 3)	# 1-3
    sprite('vr_tt204_11', 3)	# 4-6
    sprite('vr_tt204_12', 10)	# 7-16
    Unknown3004(-42)
    ExitState()
    label(0)
    sprite('null', 1)	# 17-17

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
    sprite('tt205_00', 4)	# 1-4
    sprite('tt205_01', 4)	# 5-8
    sprite('tt205_02', 4)	# 9-12
    sprite('tt205_00', 4)	# 13-16
    sprite('tt205_01', 5)	# 17-21
    sprite('tt205_03', 4)	# 22-25
    sprite('tt205_04', 2)	# 26-27	 **attackbox here**
    physicsXImpulse(24000)
    RefreshMultihit()
    sprite('tt205_05', 2)	# 28-29	 **attackbox here**
    physicsXImpulse(48000)
    sprite('tt205_04', 2)	# 30-31	 **attackbox here**
    SFX_3('chain_move')
    sprite('tt205_06', 2)	# 32-33
    Unknown1019(30)
    Unknown23029(3, 2013, 0)
    sprite('tt205_07', 2)	# 34-35
    EnableCollision(0)
    sprite('tt205_08', 2)	# 36-37
    Unknown1019(60)
    sprite('tt205_09', 4)	# 38-41
    sprite('tt205_10', 4)	# 42-45
    Unknown1019(60)
    sprite('tt205_09', 4)	# 46-49
    sprite('tt205_10', 4)	# 50-53
    Unknown1019(60)
    sprite('tt205_09', 4)	# 54-57
    sprite('tt205_10', 4)	# 58-61
    Unknown1019(60)
    sprite('tt205_09', 4)	# 62-65
    sprite('tt205_10', 4)	# 66-69
    Unknown1019(0)
    sprite('tt205_09', 4)	# 70-73
    sprite('tt205_10', 4)	# 74-77
    sprite('tt205_09', 4)	# 78-81
    sprite('tt205_10', 4)	# 82-85
    sprite('keep', 32767)	# 86-32852
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32853-65619
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
    sprite('keep', 2)	# 1-2
    RefreshMultihit()
    sprite('tt205_06', 2)	# 3-4
    Unknown1019(30)
    sprite('tt205_07', 2)	# 5-6
    EnableCollision(0)
    sprite('tt205_08', 2)	# 7-8
    Unknown1019(60)
    sprite('tt205_09', 4)	# 9-12
    sprite('tt205_10', 4)	# 13-16
    Unknown1019(60)
    sprite('tt205_09', 4)	# 17-20
    sprite('tt205_10', 4)	# 21-24
    Unknown1019(60)
    sprite('tt205_09', 4)	# 25-28
    sprite('tt205_10', 4)	# 29-32
    Unknown1019(60)
    sprite('tt205_09', 4)	# 33-36
    sprite('tt205_10', 4)	# 37-40
    Unknown1019(0)
    sprite('tt205_09', 4)	# 41-44
    sprite('tt205_10', 4)	# 45-48
    sprite('tt205_09', 4)	# 49-52
    sprite('tt205_10', 4)	# 53-56
    sprite('keep', 32767)	# 57-32823
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
    sprite('tt233_00', 3)	# 1-3
    SFX_0('chain_move')
    sprite('tt233_03', 3)	# 4-6
    sprite('tt233_04', 3)	# 7-9
    sprite('tt233_05', 2)	# 10-11
    GFX_1('ttef_poisonbreath_add', 0)
    sprite('tt233_06', 2)	# 12-13
    GFX_1('ttef_poisonbreath_add', 0)
    sprite('tt233_07', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    SFX_3('el050')
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_08', 3)	# 17-19	 **attackbox here**
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_09', 3)	# 20-22	 **attackbox here**
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_10', 3)	# 23-25	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown23029(3, 2014, 0)
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_11', 3)	# 26-28
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_12', 3)	# 29-31
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_10', 3)	# 32-34	 **attackbox here**
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_11', 3)	# 35-37
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_12', 3)	# 38-40
    GFX_1('ttef_poisonbreath', 0)
    sprite('tt233_10', 3)	# 41-43	 **attackbox here**
    sprite('tt233_11', 3)	# 44-46
    sprite('tt233_12', 3)	# 47-49
    sprite('tt233_10', 3)	# 50-52	 **attackbox here**
    sprite('tt233_11', 3)	# 53-55
    sprite('tt233_12', 3)	# 56-58
    sprite('tt233_10', 3)	# 59-61	 **attackbox here**
    sprite('tt233_11', 3)	# 62-64
    sprite('tt233_12', 3)	# 65-67
    sprite('tt233_10', 3)	# 68-70	 **attackbox here**
    sprite('tt233_11', 3)	# 71-73
    sprite('tt233_12', 3)	# 74-76
    sprite('keep', 32767)	# 77-32843
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
    sprite('tt254_00', 3)	# 1-3
    if SLOT_2:
        Unknown1005()
    sprite('tt254_01', 3)	# 4-6
    SFX_3('hit_m_slow')
    SFX_3('chain_move')
    sprite('tt254_02', 3)	# 7-9
    sprite('tt254_03', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('tt254_03', 2)	# 11-12	 **attackbox here**
    Unknown23022(0)
    sprite('tt254_04', 3)	# 13-15
    Unknown23029(3, 2015, 0)
    SFX_3('chain_move')
    sprite('tt254_05', 3)	# 16-18
    sprite('tt254_06', 3)	# 19-21
    sprite('tt254_07', 6)	# 22-27
    sprite('tt254_08', 6)	# 28-33
    sprite('tt254_09', 6)	# 34-39
    sprite('tt254_07', 6)	# 40-45
    sprite('tt254_08', 6)	# 46-51
    sprite('tt254_09', 6)	# 52-57
    sprite('tt254_07', 6)	# 58-63
    sprite('tt254_08', 6)	# 64-69
    sprite('tt254_09', 6)	# 70-75
    sprite('keep', 32767)	# 76-32842
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
    sprite('tt205_03', 4)	# 1-4
    if SLOT_2:
        Unknown1005()
    sprite('tt205_04', 2)	# 5-6	 **attackbox here**
    physicsXImpulse(64000)
    RefreshMultihit()
    sprite('tt205_05', 2)	# 7-8	 **attackbox here**
    SFX_3('chain_move')
    sprite('tt205_06', 2)	# 9-10
    Unknown1019(30)
    EnableCollision(0)
    Unknown23029(3, 2016, 0)
    sprite('tt205_07', 2)	# 11-12
    sprite('tt205_08', 2)	# 13-14
    sprite('tt205_09', 4)	# 15-18
    sprite('tt205_10', 4)	# 19-22
    Unknown1019(0)
    sprite('tt205_09', 3)	# 23-25
    sprite('tt205_10', 3)	# 26-28
    sprite('tt205_09', 3)	# 29-31
    sprite('keep', 32767)	# 32-32798
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32799-65565
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
    sprite('keep', 2)	# 1-2
    RefreshMultihit()
    sprite('tt205_06', 2)	# 3-4
    Unknown1019(30)
    EnableCollision(0)
    sprite('tt205_07', 2)	# 5-6
    sprite('tt205_08', 2)	# 7-8
    sprite('tt205_09', 4)	# 9-12
    sprite('tt205_10', 4)	# 13-16
    Unknown1019(0)
    sprite('tt205_09', 3)	# 17-19
    sprite('tt205_10', 3)	# 20-22
    sprite('tt205_09', 3)	# 23-25
    sprite('keep', 32767)	# 26-32792
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
    sprite('tt205_04', 4)	# 1-4	 **attackbox here**
    StartMultihit()
    physicsXImpulse(0)
    if Unknown23145('PEL_PersonaAir5DGrip'):
        physicsYImpulse(20000)
        setGravity(2000)
    Unknown23015(0)
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000008000000')
    sprite('tt206_00', 5)	# 5-9
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2019(100)
    sprite('tt206_01', 5)	# 10-14	 **attackbox here**
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('tt206_02', 5)	# 15-19
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_03', 5)	# 20-24
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_04', 60)	# 25-84
    Unknown2037(1)
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    label(1)
    sprite('tt206_04', 3)	# 85-87
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_01', 12)	# 88-99	 **attackbox here**
    GFX_1('ttef_biteblood', 0)
    RefreshMultihit()
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    SFX_3('blood_l')
    sprite('tt206_05', 3)	# 100-102
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('tt206_06', 6)	# 103-108
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('tt206_07', 4)	# 109-112	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    RefreshMultihit()
    Damage(1000)
    Unknown23015(11)
    sprite('tt206_08', 4)	# 113-116	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    sprite('tt206_09', 4)	# 117-120
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    GFX_1('ttef_biteblood', 0)
    SFX_3('blood_l')
    sprite('tt206_10', 4)	# 121-124
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt206_11', 4)	# 125-128
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt206_12', 4)	# 129-132
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt206_07', 3)	# 133-135	 **attackbox here**
    Unknown2005()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    StartMultihit()
    sprite('tt206_08', 3)	# 136-138	 **attackbox here**
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
    sprite('tt206_09', 3)	# 139-141
    Unknown23029(3, 2029, 0)
    SLOT_10 = 0
    sprite('tt206_10', 5)	# 142-146
    sprite('tt206_11', 5)	# 147-151
    sprite('tt206_12', 5)	# 152-156
    sprite('tt206_10', 5)	# 157-161
    sprite('tt206_11', 5)	# 162-166
    sprite('tt206_12', 3)	# 167-169
    sprite('keep', 32767)	# 170-32936
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
    sprite('tt232_00', 3)	# 1-3
    sprite('tt232_01', 3)	# 4-6
    sprite('tt232_02', 3)	# 7-9
    sprite('tt232_03', 3)	# 10-12
    Unknown1045(18000)
    setInvincible(1)
    GuardPoint_(1)
    sprite('tt232_04', 3)	# 13-15
    sprite('tt232_05', 3)	# 16-18	 **attackbox here**
    sprite('tt232_06', 1)	# 19-19	 **attackbox here**
    ScreenShake(7000, 7000)
    GFX_0('houkouSphereLoop', 0)
    RefreshMultihit()
    SFX_3('el006')
    sprite('tt232_06', 2)	# 20-21	 **attackbox here**
    Unknown23022(0)
    sprite('tt232_07', 3)	# 22-24	 **attackbox here**
    ScreenShake(7000, 7000)
    setInvincible(0)
    sprite('tt232_08', 3)	# 25-27	 **attackbox here**
    sprite('tt232_06', 3)	# 28-30	 **attackbox here**
    sprite('tt232_07', 3)	# 31-33	 **attackbox here**
    sprite('tt232_08', 3)	# 34-36	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown23029(3, 2012, 0)
    sprite('tt232_06', 3)	# 37-39	 **attackbox here**
    sprite('tt232_07', 3)	# 40-42	 **attackbox here**
    SFX_3('chain_move')
    sprite('tt232_08', 3)	# 43-45	 **attackbox here**
    sprite('tt232_06', 3)	# 46-48	 **attackbox here**
    sprite('tt232_07', 3)	# 49-51	 **attackbox here**
    sprite('tt232_08', 3)	# 52-54	 **attackbox here**
    sprite('tt232_06', 3)	# 55-57	 **attackbox here**
    sprite('tt232_07', 3)	# 58-60	 **attackbox here**
    sprite('tt232_08', 3)	# 61-63	 **attackbox here**
    sprite('keep', 32767)	# 64-32830
    enterState('PersonaDeleteAndIdling')

@State
def houkouSphereLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        GFX_2('ttef_houkou_snb')
        Unknown4010(2)
    sprite('null', 5)	# 1-5
    GFX_0('houkouSphere', 100)
    sprite('null', 5)	# 6-10
    GFX_0('houkouSphere', 100)
    sprite('null', 5)	# 11-15
    GFX_0('houkouSphere', 100)
    sprite('null', 5)	# 16-20
    GFX_0('houkouSphere', 100)
    sprite('null', 5)	# 21-25

@State
def houkouSphere():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('656c65665f686f756b6f7573686f636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 3)	# 1-3
    sprite('null', 5)	# 4-8
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
    sprite('null', 60)	# 1-60

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
    sprite('tt404_00', 2)	# 1-2
    SFX_3('chain_move')
    sprite('tt404_01', 2)	# 3-4
    sprite('tt404_02', 2)	# 5-6
    GFX_0('GarudineTatsumakiJizoku', 0)
    Unknown38(6, 1)
    Unknown23029(6, 7001, 0)
    sprite('tt404_03', 2)	# 7-8
    sprite('tt404_04', 2)	# 9-10
    sprite('tt404_05', 2)	# 11-12
    sprite('tt404_03', 2)	# 13-14
    sprite('tt404_04', 2)	# 15-16
    sprite('tt404_05', 2)	# 17-18
    sprite('tt404_03', 2)	# 19-20
    sprite('tt404_04', 2)	# 21-22
    sprite('tt404_05', 2)	# 23-24
    sprite('tt404_03', 2)	# 25-26
    sprite('tt404_04', 2)	# 27-28
    sprite('tt404_05', 2)	# 29-30
    sprite('tt404_03', 2)	# 31-32
    sprite('tt404_04', 2)	# 33-34
    sprite('tt404_05', 2)	# 35-36
    sprite('tt404_03', 2)	# 37-38
    sprite('tt404_04', 2)	# 39-40
    sprite('tt404_05', 2)	# 41-42
    sprite('tt404_03', 2)	# 43-44
    sprite('tt404_04', 2)	# 45-46
    sprite('tt404_05', 2)	# 47-48
    sprite('tt404_03', 2)	# 49-50
    sprite('tt404_04', 2)	# 51-52
    sprite('tt404_05', 2)	# 53-54
    sprite('tt404_03', 2)	# 55-56
    sprite('tt404_04', 2)	# 57-58
    sprite('tt404_05', 2)	# 59-60
    sprite('tt404_03', 2)	# 61-62
    Unknown23029(6, 7004, 0)
    sprite('tt404_04', 2)	# 63-64
    sprite('tt404_05', 2)	# 65-66
    sprite('tt404_03', 2)	# 67-68
    Unknown4007(0)
    clearUponHandler(3)
    sprite('tt404_04', 2)	# 69-70
    sprite('tt404_05', 2)	# 71-72
    sprite('tt404_03', 2)	# 73-74
    sprite('tt404_04', 2)	# 75-76
    sprite('tt404_05', 2)	# 77-78
    sprite('tt404_03', 2)	# 79-80
    sprite('tt404_04', 2)	# 81-82
    sprite('tt404_05', 2)	# 83-84
    gotoLabel(10)
    label(0)
    sprite('tt404_03', 2)	# 85-86
    sprite('tt404_04', 2)	# 87-88
    sprite('tt404_05', 2)	# 89-90
    gotoLabel(0)
    label(10)
    sprite('keep', 2)	# 91-92
    sprite('keep', 32767)	# 93-32859
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
    sprite('vr_dmy_tatsumaki', 2)	# 1-2
    GFX_0('AssaultSEMaster', -1)
    sprite('vr_dmy_tatsumaki', 5)	# 3-7
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 8-12
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 13-17
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 18-22
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 23-27
    Unknown3004(26)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 28-32
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 33-37
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 38-42
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 43-47
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 48-52
    RefreshMultihit()
    AirPushbackX(30000)
    AirPushbackY(25000)
    AirUntechableTime(60)
    Unknown30055('000000003200000000000000')
    Unknown30056('000000003200000000000000')
    Unknown30088(1)
    sprite('null', 5)	# 53-57
    Unknown2063()
    DisableAttackRestOfMove()
    ExitState()
    label(0)
    sprite('vr_dmy_tatsumaki', 2)	# 58-59
    GFX_0('AssaultSEMaster', -1)
    Damage(300)
    sprite('vr_dmy_tatsumaki', 3)	# 60-62
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 63-65
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 66-68
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 69-71
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 72-74
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 75-77
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 78-80
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 81-83
    Unknown3004(26)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 84-86
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 87-89
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 90-92
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 93-95
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 96-98
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 99-101
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 3)	# 102-104
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 105-109
    RefreshMultihit()
    AirPushbackX(30000)
    AirPushbackY(25000)
    AirUntechableTime(60)
    Unknown30055('000000003200000000000000')
    Unknown30056('000000003200000000000000')
    Unknown30088(1)
    sprite('null', 5)	# 110-114
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
    sprite('null', 30)	# 1-30

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
    sprite('tt402_00', 2)	# 1-2
    SFX_3('chain_move')
    sprite('tt402_01', 2)	# 3-4
    sprite('tt402_02', 2)	# 5-6
    sprite('tt402_00', 2)	# 7-8
    sprite('tt402_03', 2)	# 9-10
    sprite('tt402_04', 2)	# 11-12
    sprite('tt402_05', 2)	# 13-14
    sprite('tt402_06ex2', 1)	# 15-15	 **attackbox here**
    GFX_0('UltimateLaserJizoku', 0)
    Unknown36(1)
    Unknown1056(500)
    Unknown1064(250)
    teleportRelativeX(-3000)
    Unknown1007(-15000)
    Unknown35()
    GFX_0('ShotSEMaster', -1)
    RefreshMultihit()
    sprite('tt402_06ex2', 1)	# 16-16	 **attackbox here**
    Unknown23022(0)
    sprite('tt402_07ex', 3)	# 17-19	 **attackbox here**
    Unknown23029(3, 3013, 0)
    DisableAttackRestOfMove()
    sprite('tt402_08ex', 3)	# 20-22	 **attackbox here**
    sprite('tt402_09ex', 3)	# 23-25	 **attackbox here**
    sprite('tt402_10ex', 3)	# 26-28	 **attackbox here**
    sprite('tt402_11ex', 3)	# 29-31	 **attackbox here**
    sprite('tt402_06ex', 3)	# 32-34	 **attackbox here**
    sprite('tt402_07ex', 3)	# 35-37	 **attackbox here**
    sprite('tt402_08ex', 3)	# 38-40	 **attackbox here**
    sprite('tt402_09ex', 3)	# 41-43	 **attackbox here**
    sprite('tt402_10', 3)	# 44-46	 **attackbox here**
    Unknown2001()
    label(0)
    sprite('tt402_11', 3)	# 47-49	 **attackbox here**
    sprite('tt402_06', 3)	# 50-52	 **attackbox here**
    sprite('tt402_07', 3)	# 53-55	 **attackbox here**
    sprite('tt402_08', 3)	# 56-58	 **attackbox here**
    sprite('tt402_09', 3)	# 59-61	 **attackbox here**
    sprite('tt402_10', 3)	# 62-64	 **attackbox here**
    sprite('tt402_11', 3)	# 65-67	 **attackbox here**
    sprite('keep', 32767)	# 68-32834
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
    sprite('tt402_00', 2)	# 1-2
    SFX_3('chain_move')
    sprite('tt402_01', 2)	# 3-4
    sprite('tt402_02', 2)	# 5-6
    sprite('tt402_00', 1)	# 7-7
    sprite('tt402_03', 2)	# 8-9
    sprite('tt402_04', 2)	# 10-11
    sprite('tt402_05', 1)	# 12-12
    sprite('tt402_05', 1)	# 13-13
    sprite('tt402_06', 1)	# 14-14	 **attackbox here**
    GFX_0('UltimateLaserJizoku', 0)
    GFX_0('ShotSEMaster', -1)
    sprite('tt402_06', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07', 2)	# 16-17	 **attackbox here**
    Unknown23022(0)
    sprite('tt402_08', 2)	# 18-19	 **attackbox here**
    sprite('tt402_09', 2)	# 20-21	 **attackbox here**
    sprite('tt402_10', 2)	# 22-23	 **attackbox here**
    Unknown23029(3, 3013, 0)
    DisableAttackRestOfMove()
    sprite('tt402_11', 2)	# 24-25	 **attackbox here**
    sprite('tt402_06', 2)	# 26-27	 **attackbox here**
    sprite('tt402_07', 2)	# 28-29	 **attackbox here**
    sprite('tt402_08', 2)	# 30-31	 **attackbox here**
    sprite('tt402_09', 2)	# 32-33	 **attackbox here**
    sprite('tt402_10', 2)	# 34-35	 **attackbox here**
    Unknown2001()
    sprite('tt402_11', 2)	# 36-37	 **attackbox here**
    sprite('tt402_06', 2)	# 38-39	 **attackbox here**
    sprite('tt402_07', 2)	# 40-41	 **attackbox here**
    sprite('tt402_08', 2)	# 42-43	 **attackbox here**
    sprite('tt402_09', 2)	# 44-45	 **attackbox here**
    sprite('tt402_10', 2)	# 46-47	 **attackbox here**
    sprite('tt402_11', 2)	# 48-49	 **attackbox here**
    sprite('tt402_06', 2)	# 50-51	 **attackbox here**
    sprite('tt402_07', 2)	# 52-53	 **attackbox here**
    sprite('tt402_08', 2)	# 54-55	 **attackbox here**
    sprite('tt402_09', 2)	# 56-57	 **attackbox here**
    sprite('tt402_10', 2)	# 58-59	 **attackbox here**
    sprite('tt402_11', 2)	# 60-61	 **attackbox here**
    sprite('tt402_06', 2)	# 62-63	 **attackbox here**
    sprite('tt402_07', 2)	# 64-65	 **attackbox here**
    sprite('tt402_08', 2)	# 66-67	 **attackbox here**
    sprite('tt402_09', 2)	# 68-69	 **attackbox here**
    sprite('tt402_10', 2)	# 70-71	 **attackbox here**
    sprite('tt402_11', 2)	# 72-73	 **attackbox here**
    sprite('keep', 32767)	# 74-32840
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
    sprite('null', 5)	# 1-5
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 5)	# 6-10
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)	# 11-15
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(-200)
    Unknown3004(-51)
    ExitState()
    label(1)
    sprite('null', 4)	# 16-19
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 15)	# 20-34
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)	# 35-39
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
    sprite('tt403_00', 4)	# 1-4
    SFX_3('chain_move')
    sprite('tt403_01', 4)	# 5-8
    sprite('tt403_02', 4)	# 9-12
    sprite('tt403_03', 3)	# 13-15
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 2)	# 16-17	 **attackbox here**
    SFX_3('slash_blade_fast')
    Unknown1019(40)
    sprite('tt403_05', 1)	# 18-18	 **attackbox here**
    Unknown1019(0)
    RefreshMultihit()
    sprite('tt403_05', 3)	# 19-21	 **attackbox here**
    Unknown23029(3, 3015, 0)
    Unknown23022(0)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)	# 22-29
    sprite('tt403_06', 20)	# 30-49
    sprite('tt403_06', 10)	# 50-59
    sprite('keep', 32767)	# 60-32826
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
    sprite('tt403_00', 3)	# 1-3
    SFX_3('chain_move')
    sprite('tt403_01', 3)	# 4-6
    sprite('tt403_02', 3)	# 7-9
    sprite('tt403_03', 3)	# 10-12
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(10)
    physicsXImpulse(80000)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 <= 200000):
            clearUponHandler(3)
            Unknown1019(0)
    sprite('tt403_03', 3)	# 13-15
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 1)	# 16-16	 **attackbox here**
    clearUponHandler(3)
    SFX_3('slash_blade_fast')
    Unknown1019(40)
    RefreshMultihit()
    sprite('tt403_04', 1)	# 17-17	 **attackbox here**
    Unknown23022(0)
    sprite('tt403_05', 1)	# 18-18	 **attackbox here**
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
    sprite('tt403_05', 3)	# 19-21	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown23029(3, 3015, 0)
    sprite('tt403_06', 8)	# 22-29
    sprite('tt403_06', 37)	# 30-66
    sprite('keep', 32767)	# 67-32833
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
    sprite('tt404_00', 2)	# 1-2
    SFX_3('chain_move')
    sprite('tt404_01', 2)	# 3-4
    sprite('tt404_02', 2)	# 5-6
    GFX_0('GarudineTatsumakiJizoku', 0)
    Unknown38(6, 1)
    Unknown23029(6, 7002, 0)
    sprite('tt404_03', 2)	# 7-8
    sprite('tt404_04', 2)	# 9-10
    sprite('tt404_05', 2)	# 11-12
    sprite('tt404_03', 2)	# 13-14
    sprite('tt404_04', 2)	# 15-16
    sprite('tt404_05', 2)	# 17-18
    sprite('tt404_03', 2)	# 19-20
    sprite('tt404_04', 2)	# 21-22
    sprite('tt404_05', 2)	# 23-24
    sprite('tt404_03', 2)	# 25-26
    sprite('tt404_04', 2)	# 27-28
    sprite('tt404_05', 2)	# 29-30
    sprite('tt404_03', 2)	# 31-32
    sprite('tt404_04', 2)	# 33-34
    sprite('tt404_05', 2)	# 35-36
    sprite('tt404_03', 2)	# 37-38
    sprite('tt404_04', 2)	# 39-40
    sprite('tt404_05', 2)	# 41-42
    sprite('tt404_03', 2)	# 43-44
    sprite('tt404_04', 2)	# 45-46
    sprite('tt404_05', 2)	# 47-48
    sprite('tt404_03', 2)	# 49-50
    sprite('tt404_04', 2)	# 51-52
    sprite('tt404_05', 2)	# 53-54
    sprite('tt404_03', 2)	# 55-56
    sprite('tt404_04', 2)	# 57-58
    sprite('tt404_05', 2)	# 59-60
    sprite('tt404_03', 2)	# 61-62
    sprite('tt404_04', 2)	# 63-64
    sprite('tt404_05', 2)	# 65-66
    sprite('tt404_03', 2)	# 67-68
    Unknown23029(6, 7004, 0)
    sprite('tt404_04', 2)	# 69-70
    sprite('tt404_05', 2)	# 71-72
    sprite('tt404_03', 2)	# 73-74
    Unknown4007(0)
    clearUponHandler(3)
    sprite('tt404_04', 2)	# 75-76
    sprite('tt404_05', 2)	# 77-78
    sprite('tt404_03', 2)	# 79-80
    sprite('tt404_04', 2)	# 81-82
    sprite('tt404_05', 2)	# 83-84
    sprite('tt404_03', 2)	# 85-86
    sprite('tt404_04', 2)	# 87-88
    sprite('tt404_05', 2)	# 89-90
    gotoLabel(10)
    label(0)
    sprite('tt404_03', 2)	# 91-92
    sprite('tt404_04', 2)	# 93-94
    sprite('tt404_05', 2)	# 95-96
    gotoLabel(0)
    label(10)
    sprite('keep', 2)	# 97-98
    sprite('keep', 32767)	# 99-32865
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
    sprite('vr_dmy_tatsumaki', 2)	# 1-2
    GFX_0('AssaultSEMaster', -1)
    sprite('vr_dmy_tatsumaki', 5)	# 3-7
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 8-12
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 13-17
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 18-22
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 23-27
    Unknown3004(26)
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 28-32
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 33-37
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 38-42
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 43-47
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 48-52
    RefreshMultihit()
    sprite('vr_dmy_tatsumaki', 5)	# 53-57
    RefreshMultihit()
    sprite('null', 5)	# 58-62
    DisableAttackRestOfMove()
    if SLOT_58:
        Unknown21012('50454c5f506572736f6e6141737361756c74457800000000000000000000000026000000')
        Unknown23029(3, 7005, 0)
        sendToLabel(10)
    ExitState()
    label(10)
    sprite('vr_dmy_tatsumaki', 2)	# 63-64
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
    sprite('vr_dmy_tatsumaki', 5)	# 65-69
    RefreshMultihit()
    AirHitstunAnimation(10)
    Damage(500)
    AirPushbackX(2500)
    AirPushbackY(40000)
    if SLOT_4:
        AirUntechableTime(55)
        AirPushbackX(15000)
        AirPushbackY(45000)
    sprite('null', 13)	# 70-82
    sprite('null', 10)	# 83-92
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
    sprite('null', 1)	# 1-1
    GFX_0('GarudineTatsumakiStartMato', 100)
    sprite('null', 14)	# 2-15
    if SLOT_IsInOverdrive2:
        GFX_0('TatsumakiAAAA', 100)
    if SLOT_56:
        GFX_0('TatsumakiEx', 100)
    sprite('null', 5)	# 16-20
    Unknown3004(51)
    sprite('null', 32767)	# 21-32787
    label(0)
    sprite('null', 10)	# 32788-32797
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
    sprite('null', 5)	# 1-5
    GFX_0('GarudineTatsumakiStart', 100)
    sprite('null', 5)	# 6-10
    GFX_0('GarudineTatsumakiStart', 100)
    sprite('null', 5)	# 11-15
    GFX_0('GarudineTatsumakiStart', 100)
    sprite('null', 10)	# 16-25
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
    sprite('null', 20)	# 1-20
    Unknown3004(51)
    Unknown1099(50)
    physicsYImpulse(10000)
    sprite('null', 10)	# 21-30
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
    sprite('tt402_00', 1)	# 1-1
    SFX_3('chain_move')
    sprite('tt402_01', 1)	# 2-2
    sprite('tt402_02', 2)	# 3-4
    sprite('tt402_00', 2)	# 5-6
    sprite('tt402_01', 2)	# 7-8
    sprite('tt402_02', 2)	# 9-10
    sprite('tt402_00', 2)	# 11-12
    sprite('tt402_01', 2)	# 13-14
    sprite('tt402_02', 2)	# 15-16
    sprite('tt402_00', 2)	# 17-18
    sprite('tt402_01', 2)	# 19-20
    sprite('tt402_03', 2)	# 21-22
    sprite('tt402_04', 2)	# 23-24
    sprite('tt402_05', 1)	# 25-25
    sprite('tt402_05', 1)	# 26-26
    sprite('tt402_06', 1)	# 27-27	 **attackbox here**
    GFX_0('UltimateLaserJizokuEX', 0)
    SFX_3('el054')
    sprite('tt402_06', 1)	# 28-28	 **attackbox here**
    sprite('tt402_07', 1)	# 29-29	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07', 1)	# 30-30	 **attackbox here**
    Unknown23022(0)
    sprite('tt402_08', 2)	# 31-32	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)	# 33-34	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10', 2)	# 35-36	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)	# 37-38	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_06', 2)	# 39-40	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07', 2)	# 41-42	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08', 2)	# 43-44	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)	# 45-46	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10', 2)	# 47-48	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)	# 49-50	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_06', 2)	# 51-52	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07', 2)	# 53-54	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08', 2)	# 55-56	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10', 2)	# 59-60	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_06', 2)	# 63-64	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07', 2)	# 65-66	 **attackbox here**
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 2)	# 67-68	 **attackbox here**
    Unknown23029(3, 4013, 0)
    Unknown2001()
    label(0)
    sprite('tt402_11', 2)	# 69-70	 **attackbox here**
    sprite('tt402_06', 2)	# 71-72	 **attackbox here**
    sprite('tt402_07', 2)	# 73-74	 **attackbox here**
    sprite('tt402_08', 2)	# 75-76	 **attackbox here**
    sprite('tt402_09', 2)	# 77-78	 **attackbox here**
    sprite('tt402_10', 2)	# 79-80	 **attackbox here**
    sprite('tt402_11', 2)	# 81-82	 **attackbox here**
    sprite('tt402_06', 2)	# 83-84	 **attackbox here**
    sprite('tt402_07', 2)	# 85-86	 **attackbox here**
    sprite('tt402_08', 2)	# 87-88	 **attackbox here**
    sprite('tt402_09', 2)	# 89-90	 **attackbox here**
    sprite('tt402_10', 2)	# 91-92	 **attackbox here**
    sprite('tt402_11', 2)	# 93-94	 **attackbox here**
    sprite('tt402_06', 2)	# 95-96	 **attackbox here**
    sprite('tt402_07', 2)	# 97-98	 **attackbox here**
    sprite('tt402_08', 2)	# 99-100	 **attackbox here**
    sprite('tt402_09', 2)	# 101-102	 **attackbox here**
    sprite('tt402_10', 2)	# 103-104	 **attackbox here**
    sprite('tt402_11', 2)	# 105-106	 **attackbox here**
    sprite('tt402_06', 2)	# 107-108	 **attackbox here**
    sprite('tt402_07', 2)	# 109-110	 **attackbox here**
    sprite('tt402_08', 2)	# 111-112	 **attackbox here**
    sprite('keep', 32767)	# 113-32879
    enterState('PersonaDeleteAndIdling')

@State
def UltimateLaserJizokuEX():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('656c65665f6a696f64696e655f6a697a6f6b7530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 5)	# 1-5
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 40)	# 6-45
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)	# 46-50
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
    sprite('tt402_00', 1)	# 1-1
    SFX_3('chain_move')
    sprite('tt402_01', 1)	# 2-2
    sprite('tt402_02', 2)	# 3-4
    sprite('tt402_00', 2)	# 5-6
    sprite('tt402_01', 2)	# 7-8
    sprite('tt402_02', 2)	# 9-10
    sprite('tt402_00', 2)	# 11-12
    sprite('tt402_01', 2)	# 13-14
    sprite('tt402_02', 2)	# 15-16
    sprite('tt402_00', 2)	# 17-18
    sprite('tt402_01', 2)	# 19-20
    sprite('tt402_02', 2)	# 21-22
    sprite('tt402_03', 2)	# 23-24
    sprite('tt402_04', 2)	# 25-26
    sprite('tt402_05', 1)	# 27-27
    sprite('tt402_05', 1)	# 28-28
    sprite('tt402_06ex', 1)	# 29-29	 **attackbox here**
    SFX_3('el054')
    GFX_0('UltimateLaserJizokuSB', 0)
    Unknown36(1)
    Unknown1096(1500)
    teleportRelativeX(-33000)
    Unknown35()
    RefreshMultihit()
    sprite('tt402_06ex', 1)	# 30-30	 **attackbox here**
    Unknown23022(0)
    sprite('tt402_07ex', 1)	# 31-31	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07ex', 1)	# 32-32	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08ex', 1)	# 33-33	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_08ex', 1)	# 34-34	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_09ex', 1)	# 35-35	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_09ex', 1)	# 36-36	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10ex', 1)	# 37-37	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_10ex', 1)	# 38-38	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_11ex', 1)	# 39-39	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_11ex', 1)	# 40-40	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07ex', 2)	# 41-42	 **attackbox here**
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 2)	# 43-44	 **attackbox here**
    sprite('tt402_00', 1)	# 45-45
    SFX_3('chain_move')
    sprite('tt402_01', 1)	# 46-46
    sprite('tt402_02', 2)	# 47-48
    sprite('tt402_00', 2)	# 49-50
    sprite('tt402_01', 2)	# 51-52
    sprite('tt402_03', 2)	# 53-54
    sprite('tt402_04', 2)	# 55-56
    sprite('tt402_05', 2)	# 57-58
    sprite('tt402_06ex', 1)	# 59-59	 **attackbox here**
    RefreshMultihit()
    GFX_0('UltimateLaserJizokuSB', 0)
    Unknown36(1)
    Unknown1096(1500)
    teleportRelativeX(-33000)
    Unknown35()
    SFX_3('el054')
    sprite('tt402_06ex', 1)	# 60-60	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07ex', 1)	# 61-61	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07ex', 1)	# 62-62	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08ex', 1)	# 63-63	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_08ex', 1)	# 64-64	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_09ex', 1)	# 65-65	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_09ex', 1)	# 66-66	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10ex', 1)	# 67-67	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_10ex', 1)	# 68-68	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_11ex', 1)	# 69-69	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_11ex', 1)	# 70-70	 **attackbox here**
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 3)	# 71-73	 **attackbox here**
    Unknown2001()
    sprite('tt402_11', 3)	# 74-76	 **attackbox here**
    sprite('tt402_06', 3)	# 77-79	 **attackbox here**
    sprite('tt402_07', 3)	# 80-82	 **attackbox here**
    sprite('tt402_08', 3)	# 83-85	 **attackbox here**
    sprite('tt402_09', 3)	# 86-88	 **attackbox here**
    sprite('tt402_10', 3)	# 89-91	 **attackbox here**
    sprite('tt402_11', 3)	# 92-94	 **attackbox here**
    sprite('tt402_06', 3)	# 95-97	 **attackbox here**
    sprite('tt402_07', 3)	# 98-100	 **attackbox here**
    sprite('tt402_08', 3)	# 101-103	 **attackbox here**
    sprite('tt402_09', 3)	# 104-106	 **attackbox here**
    sprite('tt402_10', 3)	# 107-109	 **attackbox here**
    sprite('tt402_11', 3)	# 110-112	 **attackbox here**
    sprite('tt402_06', 3)	# 113-115	 **attackbox here**
    sprite('tt402_07', 3)	# 116-118	 **attackbox here**
    sprite('tt402_08', 3)	# 119-121	 **attackbox here**
    sprite('tt402_09', 3)	# 122-124	 **attackbox here**
    sprite('tt402_10', 3)	# 125-127	 **attackbox here**
    sprite('tt402_11', 3)	# 128-130	 **attackbox here**
    sprite('tt402_06', 3)	# 131-133	 **attackbox here**
    sprite('tt402_07', 3)	# 134-136	 **attackbox here**
    sprite('tt402_08', 3)	# 137-139	 **attackbox here**
    sprite('keep', 32767)	# 140-32906
    enterState('PersonaDeleteAndIdling')

@State
def UltimateLaserJizokuSB():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4010(2)
        Unknown4003('656c65665f6a696f64696e655f6a697a6f6b7530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
    sprite('null', 5)	# 1-5
    GFX_1('ttef_mahagiofin_02', 100)
    Unknown1067(50)
    Unknown3004(51)
    sprite('null', 25)	# 6-30
    GFX_2('ttef_mahagiojizoku_iti')
    Unknown1067(0)
    sprite('null', 5)	# 31-35
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
    sprite('tt403_00', 3)	# 1-3
    SFX_3('chain_move')
    sprite('tt403_01', 3)	# 4-6
    sprite('tt403_02', 3)	# 7-9
    sprite('tt403_03', 1)	# 10-10
    sprite('tt403_03', 3)	# 11-13
    GFX_0('ttef403_Zanzoh', 100)
    physicsXImpulse(70000)
    sprite('tt403_04', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    SFX_3('slash_blade_fast')
    Unknown1019(20)
    sprite('tt403_05', 1)	# 16-16	 **attackbox here**
    Unknown2037(1)
    Unknown1019(0)
    setInvincible(0)
    RefreshMultihit()
    Damage(2000)
    Hitstop(15)
    Unknown30055('f04902002800000000000000')
    sprite('tt403_05', 1)	# 17-17	 **attackbox here**
    Unknown23022(0)
    sprite('tt403_05', 3)	# 18-20	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)	# 21-28
    setInvincible(0)
    sprite('tt403_06', 20)	# 29-48
    sprite('tt403_06', 10)	# 49-58
    sprite('keep', 32767)	# 59-32825
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(1)
    sprite('tt403_06', 4)	# 32826-32829
    Unknown23029(3, 4025, 0)
    sprite('tt403_07', 4)	# 32830-32833
    sprite('tt403_07', 20)	# 32834-32853
    GFX_0('403icecharge', 0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_41 <= 900000):
            clearUponHandler(3)
            sendToLabel(10)
    label(10)
    sprite('tt403_08', 4)	# 32854-32857
    clearUponHandler(3)
    SFX_3('slash_pole_middle')
    GFX_0('Mahabufudain_iceatk', 0)
    sprite('tt403_09', 4)	# 32858-32861
    GFX_0('Mahabufudain', 100)
    sprite('tt403_10', 4)	# 32862-32865
    sprite('tt403_11', 4)	# 32866-32869
    sprite('tt403_12', 4)	# 32870-32873
    sprite('tt403_11', 4)	# 32874-32877
    sprite('tt403_12', 4)	# 32878-32881
    sprite('tt403_11', 4)	# 32882-32885
    sprite('tt403_12', 4)	# 32886-32889
    sprite('tt403_11', 4)	# 32890-32893
    sprite('tt403_12', 4)	# 32894-32897
    sprite('tt403_11', 4)	# 32898-32901
    sprite('tt403_12', 4)	# 32902-32905
    sprite('tt403_11', 4)	# 32906-32909
    sprite('tt403_12', 4)	# 32910-32913
    sprite('tt403_11', 4)	# 32914-32917
    sprite('tt403_12', 4)	# 32918-32921
    sprite('tt403_11', 2)	# 32922-32923
    sprite('keep', 32767)	# 32924-65690
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
    sprite('vr_tt403_00', 3)	# 1-3
    sprite('vr_tt403_01', 2)	# 4-5
    sprite('vr_tt403_02', 4)	# 6-9
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
    sprite('null', 14)	# 1-14
    Unknown3004(60)
    sprite('null', 14)	# 15-28
    sprite('null', 10)	# 29-38
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
    sprite('null', 4)	# 1-4
    Unknown4010(2)
    sprite('vr_tt403ice00', 14)	# 5-18
    Unknown4010(0)
    sprite('vr_tt403ice00', 10)	# 19-28
    Unknown1110(50000, 0)
    RefreshMultihit()

    def upon_12():
        SFX_3('ice_fast')
    sprite('vr_tt403ice00', 6)	# 29-34
    GFX_0('Mahabufudain_move', 0)
    sprite('vr_tt403ice00', 3)	# 35-37
    Unknown1110(0, 0)
    Unknown3004(-90)

@State
def Mahabufudain_move():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1072(-35000)
        Unknown1110(20000, 0)
    sprite('null', 1)	# 1-1
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 2-2
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 3-3
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 4-4
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 5-5
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 6-6
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 7-7
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 8-8
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 9-9
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 10-10
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 11-11
    GFX_0('403icemove', 100)
    sprite('null', 1)	# 12-12
    GFX_0('403icemove', 100)
    sprite('null', 5)	# 13-17
    Unknown3004(-90)

@State
def __403icemove():

    def upon_IMMEDIATE():
        Unknown23067('ttef_403icemove')
        Unknown1072(55000)
    sprite('null', 5)	# 1-5

@State
def __403icecharge():

    def upon_IMMEDIATE():
        Unknown23067('ttef_403icecharge')
    sprite('null', 40)	# 1-40
    sprite('null', 20)	# 41-60
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
    sprite('tt403_00', 3)	# 1-3
    SFX_3('chain_move')
    sprite('tt403_01', 3)	# 4-6
    sprite('tt403_02', 3)	# 7-9
    sprite('tt403_03', 8)	# 10-17
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(10)
    physicsXImpulse(100000)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 <= 300000):
            sendToLabel(101)
    label(101)
    sprite('tt403_03', 3)	# 18-20
    clearUponHandler(3)
    GFX_0('ttef403_Zanzoh', 100)
    Unknown1019(40)
    sprite('tt403_04', 1)	# 21-21	 **attackbox here**
    SFX_3('slash_blade_fast')
    Unknown1019(20)
    RefreshMultihit()
    sprite('tt403_04', 1)	# 22-22	 **attackbox here**
    Unknown23022(0)
    sprite('tt403_05', 1)	# 23-23	 **attackbox here**
    Unknown2037(1)
    Unknown1019(0)
    setInvincible(0)
    RefreshMultihit()
    Damage(2500)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown30055('f04902002800000000000000')
    Hitstop(15)
    sprite('tt403_05', 1)	# 24-24	 **attackbox here**
    Unknown23022(0)
    sprite('tt403_05', 3)	# 25-27	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)	# 28-35
    setInvincible(0)
    sprite('tt403_06', 20)	# 36-55
    sprite('tt403_06', 10)	# 56-65
    sprite('keep', 32767)	# 66-32832
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(1)
    sprite('tt403_06', 4)	# 32833-32836
    Unknown23029(3, 4025, 0)
    sprite('tt403_07', 4)	# 32837-32840
    sprite('tt403_07', 20)	# 32841-32860
    GFX_0('403icecharge', 0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_41 <= 900000):
            clearUponHandler(3)
            sendToLabel(10)
    label(10)
    sprite('tt403_08', 4)	# 32861-32864
    clearUponHandler(3)
    SFX_3('slash_pole_middle')
    GFX_0('Mahabufudain_iceatk', 0)
    Unknown23029(1, 4026, 0)
    sprite('tt403_09', 4)	# 32865-32868
    GFX_0('Mahabufudain', 100)
    sprite('tt403_10', 4)	# 32869-32872
    sprite('tt403_11', 4)	# 32873-32876
    sprite('tt403_12', 4)	# 32877-32880
    sprite('tt403_11', 4)	# 32881-32884
    sprite('tt403_12', 4)	# 32885-32888
    sprite('tt403_11', 4)	# 32889-32892
    sprite('tt403_12', 4)	# 32893-32896
    sprite('tt403_11', 4)	# 32897-32900
    sprite('tt403_12', 4)	# 32901-32904
    sprite('tt403_11', 4)	# 32905-32908
    sprite('tt403_12', 4)	# 32909-32912
    sprite('tt403_11', 4)	# 32913-32916
    sprite('tt403_12', 4)	# 32917-32920
    sprite('tt403_11', 4)	# 32921-32924
    sprite('tt403_12', 4)	# 32925-32928
    sprite('tt403_11', 2)	# 32929-32930
    sprite('keep', 32767)	# 32931-65697
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
    sprite('tt405_00', 3)	# 1-3
    SFX_3('chain_move')
    sprite('tt405_01', 3)	# 4-6
    sprite('tt405_02', 3)	# 7-9
    sprite('tt405_03', 3)	# 10-12
    sprite('tt405_04', 3)	# 13-15
    sprite('tt405_05', 3)	# 16-18
    sprite('tt405_03', 3)	# 19-21
    sprite('tt405_04', 3)	# 22-24
    sprite('tt405_06', 2)	# 25-26
    sprite('tt405_06', 1)	# 27-27
    GFX_0('ChargeShotExAtk', 104)
    sprite('tt405_07', 3)	# 28-30
    SFX_3('hit_m_slow')
    sprite('tt405_08', 3)	# 31-33
    sprite('tt405_09', 4)	# 34-37
    sprite('tt405_10', 4)	# 38-41
    sprite('tt405_11', 4)	# 42-45
    sprite('tt405_09', 4)	# 46-49
    sprite('tt405_10', 4)	# 50-53
    sprite('tt405_11', 4)	# 54-57
    sprite('tt405_09', 4)	# 58-61
    sprite('tt405_10', 4)	# 62-65
    sprite('tt405_11', 4)	# 66-69
    sprite('tt405_09', 4)	# 70-73
    sprite('tt405_10', 4)	# 74-77
    sprite('tt405_11', 4)	# 78-81
    sprite('tt405_09', 4)	# 82-85
    sprite('tt405_10', 4)	# 86-89
    sprite('tt405_11', 4)	# 90-93
    sprite('tt405_09', 4)	# 94-97
    sprite('tt405_10', 4)	# 98-101
    sprite('tt405_11', 4)	# 102-105
    sprite('tt405_09', 4)	# 106-109
    sprite('tt405_10', 4)	# 110-113
    sprite('tt405_11', 4)	# 114-117
    sprite('tt405_09', 4)	# 118-121
    sprite('tt405_10', 4)	# 122-125
    sprite('tt405_11', 3)	# 126-128
    sprite('tt405_11', 1)	# 129-129
    sprite('keep', 32767)	# 130-32896
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
    sprite('null', 1)	# 1-1
    sprite('null', 5)	# 2-6
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(250000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 7-11
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 12-16
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 17-21
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 22-26
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 27-31
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 32-36
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 37-41
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 42-46
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 5)	# 47-51
    Unknown23183('6e756c6c00000000000000000000000000000000000000000000000000000000060000000200000002000000')
    teleportRelativeX(125000)
    GFX_0('ChargeShotExAtkCol', 100)
    sprite('null', 60)	# 52-111

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
    sprite('vr_el405_dmg00', 9)	# 1-9
    Unknown1067(75)
    if SLOT_4:
        Unknown1067(100)
    sprite('vr_el405_dmg00', 5)	# 10-14
    Unknown1067(0)
    RefreshMultihit()
    SFX_3('blaze_long')

    def upon_44():
        DisableAttackRestOfMove()
    sprite('vr_el405_dmg00', 10)	# 15-24
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
    sprite('tt405_00', 3)	# 1-3
    SFX_3('chain_move')
    sprite('tt405_01', 3)	# 4-6
    sprite('tt405_02', 3)	# 7-9
    sprite('tt405_03', 3)	# 10-12
    sprite('tt405_04', 3)	# 13-15
    sprite('tt405_05', 3)	# 16-18
    sprite('tt405_03', 3)	# 19-21
    sprite('tt405_04', 3)	# 22-24
    sprite('tt405_06', 2)	# 25-26
    sprite('tt405_06', 1)	# 27-27
    GFX_0('ChargeShotExAtk', 104)
    Unknown21007(1, 32)
    sprite('tt405_07', 3)	# 28-30
    SFX_3('hit_m_slow')
    sprite('tt405_08', 3)	# 31-33
    sprite('tt405_09', 4)	# 34-37
    sprite('tt405_10', 4)	# 38-41
    sprite('tt405_11', 4)	# 42-45
    sprite('tt405_09', 4)	# 46-49
    sprite('tt405_10', 4)	# 50-53
    sprite('tt405_11', 4)	# 54-57
    sprite('tt405_09', 4)	# 58-61
    sprite('tt405_10', 4)	# 62-65
    sprite('tt405_11', 4)	# 66-69
    sprite('tt405_09', 4)	# 70-73
    sprite('tt405_10', 4)	# 74-77
    sprite('tt405_11', 4)	# 78-81
    sprite('tt405_09', 4)	# 82-85
    sprite('tt405_10', 4)	# 86-89
    sprite('tt405_11', 4)	# 90-93
    sprite('tt405_09', 4)	# 94-97
    sprite('tt405_10', 4)	# 98-101
    sprite('tt405_11', 4)	# 102-105
    sprite('tt405_09', 4)	# 106-109
    sprite('tt405_10', 4)	# 110-113
    sprite('tt405_11', 4)	# 114-117
    sprite('tt405_09', 4)	# 118-121
    sprite('tt405_10', 4)	# 122-125
    sprite('tt405_11', 3)	# 126-128
    sprite('tt405_11', 1)	# 129-129
    sprite('keep', 32767)	# 130-32896
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
    sprite('tt431_00', 4)	# 1-4
    Unknown13(4)
    callSubroutine('SwordFireSet')
    SFX_3('chain_move')
    sprite('tt431_01', 4)	# 5-8
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)	# 9-12
    callSubroutine('SwordFireSet')
    sprite('tt431_00', 4)	# 13-16
    callSubroutine('SwordFireSet')
    sprite('tt431_01', 4)	# 17-20
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)	# 21-24
    callSubroutine('SwordFireSet')
    sprite('tt431_03', 2)	# 25-26
    callSubroutine('SwordFireSet2')
    sprite('tt431_04', 2)	# 27-28
    callSubroutine('SwordFireSet2')
    sprite('tt431_05', 2)	# 29-30
    callSubroutine('SwordFireSet2')
    GFX_0('Mahanmaon_search', -1)
    Unknown38(4, 1)
    sprite('tt431_06', 4)	# 31-34
    sprite('tt431_07', 4)	# 35-38
    sprite('tt431_08', 4)	# 39-42
    sprite('tt431_06', 4)	# 43-46
    sprite('tt431_07', 4)	# 47-50
    sprite('tt431_08', 4)	# 51-54
    sprite('tt431_06', 4)	# 55-58
    sprite('tt431_07', 4)	# 59-62
    sprite('tt431_08', 4)	# 63-66
    sprite('keep', 32767)	# 67-32833
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
    sprite('null', 10)	# 1-10
    Unknown1086(22)
    teleportRelativeY(0)
    Unknown3004(25)
    sprite('null', 10)	# 11-20
    SFX_3('magiccircle_a')
    sprite('null', 600)	# 21-620
    Unknown2037(1)
    label(0)
    sprite('null', 10)	# 621-630
    Unknown3004(-25)
    ExitState()
    label(1)
    sprite('null', 10)	# 631-640
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
    sprite('vr_dmy_mahanmaon', 5)	# 1-5
    GFX_0('Hamathunder_r', 100)
    RefreshMultihit()
    SFX_3('el055')
    sprite('vr_dmy_mahanmaon', 5)	# 6-10
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 11-15
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 16-20
    GFX_0('Hamathunder_l', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 21-25
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 26-30
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 31-35
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 36-40
    GFX_0('Hamathunder_r', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 41-45
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 46-50
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 51-55
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 56-60
    GFX_0('Hamathunder_l', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 61-65
    GFX_0('Hamathunder_c', 100)
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 66-70
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 71-75
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 5)	# 76-80
    RefreshMultihit()
    sprite('vr_dmy_mahanmaon', 10)	# 81-90
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
    sprite('null', 25)	# 1-25
    Unknown3004(60)
    sprite('null', 5)	# 26-30
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
    sprite('null', 25)	# 1-25
    Unknown3004(60)
    sprite('null', 5)	# 26-30
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
    sprite('null', 25)	# 1-25
    Unknown3004(60)
    sprite('null', 5)	# 26-30
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
    sprite('tt431_00', 4)	# 1-4
    teleportRelativeY(0)
    Unknown13(5)
    callSubroutine('SwordFireSet')
    SFX_3('chain_move')
    sprite('tt431_01', 4)	# 5-8
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)	# 9-12
    callSubroutine('SwordFireSet')
    sprite('tt431_00', 4)	# 13-16
    callSubroutine('SwordFireSet')
    sprite('tt431_01', 4)	# 17-20
    callSubroutine('SwordFireSet')
    sprite('tt431_02', 4)	# 21-24
    callSubroutine('SwordFireSet')
    sprite('tt431_03', 2)	# 25-26
    callSubroutine('SwordFireSet2')
    sprite('tt431_04', 2)	# 27-28
    callSubroutine('SwordFireSet2')
    sprite('tt431_05ex', 2)	# 29-30
    callSubroutine('SwordFireSet2')
    GFX_0('Mahamudo_on_search', -1)
    Unknown38(5, 1)
    sprite('tt431_06', 4)	# 31-34
    sprite('tt431_07', 4)	# 35-38
    sprite('tt431_08', 4)	# 39-42
    sprite('tt431_06', 4)	# 43-46
    sprite('tt431_07', 4)	# 47-50
    sprite('tt431_08', 4)	# 51-54
    sprite('tt431_06', 4)	# 55-58
    sprite('tt431_07', 4)	# 59-62
    sprite('tt431_08', 4)	# 63-66
    sprite('keep', 32767)	# 67-32833
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
    sprite('null', 5)	# 1-5
    sprite('null', 15)	# 6-20
    Unknown1086(3)
    Unknown1007(200000)
    Unknown1099(50)
    sprite('null', 5)	# 21-25
    Unknown1099(0)
    SFX_3('magiccircle_b')
    sprite('null', 600)	# 26-625
    Unknown2037(1)
    label(0)
    sprite('null', 10)	# 626-635
    Unknown3004(-25)
    ExitState()
    label(1)
    sprite('null', 10)	# 636-645
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
    sprite('vr_dmy_mahamudoon00', 4)	# 1-4
    GFX_0('Mudothunder_up', 100)
    GFX_0('Mudothunder_down', 100)
    SFX_3('el056')
    sprite('vr_dmy_mahamudoon00', 5)	# 5-9
    sprite('vr_dmy_mahamudoon01', 5)	# 10-14
    GFX_0('Mudothunder_up', 100)
    GFX_0('Mudothunder_down', 100)
    sprite('vr_dmy_mahamudoon01', 10)	# 15-24
    Unknown3004(-26)
    DisableAttackRestOfMove()
    clearUponHandler(3)
    loopRest()
    ExitState()
    label(0)
    sprite('vr_dmy_mahamudoon01', 5)	# 25-29
    clearUponHandler(12)
    Unknown4011(0)
    DisableAttackRestOfMove()
    AirPushbackX(0)
    Unknown9083()
    Unknown9095()
    Unknown11001(0, 8, 8)
    sprite('vr_dmy_mahamudoon01', 5)	# 30-34
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)	# 35-39
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)	# 40-44
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)	# 45-49
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)	# 50-54
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)	# 55-59
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 5)	# 60-64
    RefreshMultihit()
    sprite('vr_dmy_mahamudoon01', 70)	# 65-134
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
    sprite('null', 6)	# 1-6
    Unknown1019(6)
    YAccel(6)
    Unknown1096(50)
    Unknown3001(50)
    Unknown3004(20)
    Unknown1099(150)
    sprite('null', 2)	# 7-8
    GFX_1('ttef_431mudoballsub', 100)
    Unknown1019(1000)
    YAccel(1000)
    Unknown1099(30)
    sprite('null', 2)	# 9-10
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)	# 11-12
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)	# 13-14
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)	# 15-16
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)	# 17-18
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)	# 19-20
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 2)	# 21-22
    GFX_1('ttef_431mudoballsub', 100)
    Unknown3001(180)
    Unknown3004(-20)
    Unknown1019(15)
    YAccel(15)
    sprite('null', 2)	# 23-24
    GFX_1('ttef_431mudoballsub', 100)
    sprite('null', 20)	# 25-44

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
    sprite('null', 20)	# 1-20
    Unknown3004(60)
    sprite('null', 5)	# 21-25
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
    sprite('null', 20)	# 1-20
    Unknown3004(60)
    sprite('null', 5)	# 21-25
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
    sprite('tt432_00', 3)	# 1-3
    sprite('tt432_01', 3)	# 4-6
    sprite('tt432_02', 3)	# 7-9
    sprite('tt432_03', 3)	# 10-12
    sprite('tt432_04', 3)	# 13-15
    sprite('tt432_05', 4)	# 16-19
    label(0)
    sprite('tt432_06', 4)	# 20-23
    GFX_0('diarahanSoulkanoke', 100)
    sprite('tt432_07', 4)	# 24-27
    sprite('tt432_08', 4)	# 28-31
    sprite('tt432_06', 4)	# 32-35
    sprite('tt432_07', 4)	# 36-39
    sprite('tt432_08', 4)	# 40-43
    sprite('tt432_06', 4)	# 44-47
    sprite('tt432_07', 4)	# 48-51
    sprite('tt432_08', 4)	# 52-55
    sprite('tt432_06', 4)	# 56-59
    SFX_3('el053')
    sprite('tt432_07', 4)	# 60-63
    sprite('tt432_08', 4)	# 64-67
    sprite('tt432_06', 4)	# 68-71
    sprite('tt432_07', 4)	# 72-75
    sprite('tt432_08', 4)	# 76-79
    sprite('tt432_06', 4)	# 80-83
    sprite('tt432_07', 4)	# 84-87
    sprite('tt432_08', 4)	# 88-91
    sprite('tt432_06', 4)	# 92-95
    sprite('tt432_07', 4)	# 96-99
    sprite('tt432_08', 4)	# 100-103
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tt432_06', 4)	# 104-107
    sprite('tt432_07', 4)	# 108-111
    sprite('tt432_08', 4)	# 112-115
    sprite('tt432_06', 4)	# 116-119
    sprite('tt432_07', 4)	# 120-123
    sprite('tt432_08', 4)	# 124-127
    sprite('tt432_06', 4)	# 128-131
    sprite('tt432_07', 4)	# 132-135
    sprite('keep', 32767)	# 136-32902
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
    sprite('vr_tt432_00', 4)	# 1-4
    Unknown3004(26)
    sprite('vr_tt432_01', 4)	# 5-8
    GFX_0('soulaura', 0)
    sprite('vr_tt432_02', 4)	# 9-12
    sprite('vr_tt432_03', 4)	# 13-16
    sprite('vr_tt432_01', 4)	# 17-20
    GFX_0('SyuyakuSoul', 0)
    sprite('vr_tt432_02', 4)	# 21-24
    sprite('vr_tt432_03', 4)	# 25-28
    sprite('vr_tt432_01', 4)	# 29-32
    sprite('vr_tt432_02', 4)	# 33-36
    sprite('vr_tt432_03', 4)	# 37-40
    sprite('vr_tt432_01', 4)	# 41-44
    Unknown21012('736f756c6175726100000000000000000000000000000000000000000000000020000000')
    Unknown3004(-17)
    sprite('vr_tt432_02', 4)	# 45-48
    sprite('vr_tt432_03', 4)	# 49-52
    sprite('vr_tt432_01', 4)	# 53-56
    sprite('vr_tt432_02', 4)	# 57-60
    sprite('vr_tt432_03', 4)	# 61-64
    sprite('vr_tt432_01', 4)	# 65-68
    sprite('vr_tt432_02', 4)	# 69-72
    sprite('vr_tt432_03', 4)	# 73-76

@State
def soulaura():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ttef_soulaura_g2')
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 10)	# 32768-32777
    sprite('null', 10)	# 32778-32787
    Unknown3004(-26)

@State
def SyuyakuSoul():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('656c65665f736f756c5f30302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown2054(1)
    sprite('null', 35)	# 1-35
    sprite('null', 5)	# 36-40
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
    sprite('tt204_00', 3)	# 1-3
    sprite('tt204_01', 4)	# 4-7
    sprite('tt204_02', 3)	# 8-10
    GFX_0('ttef204_Zanzoh', 100)
    SFX_3('hit_m_slow')
    physicsXImpulse(50000)
    sprite('tt204_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('tt204_03', 2)	# 12-13	 **attackbox here**
    Unknown23022(0)
    DisableAttackRestOfMove()
    Unknown1019(50)
    sprite('tt204_04', 9)	# 14-22
    Unknown1019(0)
    sprite('tt204_05', 3)	# 23-25
    GFX_0('ttef204_Zanzoh2', 100)
    physicsXImpulse(65000)
    SFX_3('chain_move')
    sprite('tt204_06', 3)	# 26-28
    SFX_3('hit_m_slow')
    Unknown1019(50)
    sprite('tt204_07', 1)	# 29-29	 **attackbox here**
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
    sprite('tt204_07', 2)	# 30-31	 **attackbox here**
    Unknown23029(3, 2011, 0)
    DisableAttackRestOfMove()
    sprite('tt204_08', 4)	# 32-35
    sprite('tt204_09', 4)	# 36-39
    sprite('tt204_10', 4)	# 40-43
    sprite('tt204_08', 4)	# 44-47
    sprite('tt204_09', 4)	# 48-51
    sprite('tt204_10', 4)	# 52-55
    sprite('tt204_08', 4)	# 56-59
    sprite('tt204_09', 4)	# 60-63
    sprite('tt204_10', 4)	# 64-67
    sprite('tt204_08', 4)	# 68-71
    sprite('tt204_09', 4)	# 72-75
    sprite('tt204_10', 4)	# 76-79
    sprite('keep', 32767)	# 80-32846
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(580)
    sprite('keep', 16)	# 32847-32862
    Unknown1019(0)
    DisableAttackRestOfMove()
    Unknown21012('747465663230345f5a616e7a6f6832000000000000000000000000000000000020000000')
    sprite('keep', 32767)	# 32863-65629
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
    sprite('tt403_00', 2)	# 1-2
    SFX_3('chain_move')
    sprite('tt403_01', 2)	# 3-4
    sprite('tt403_03', 3)	# 5-7
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 2)	# 8-9	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('tt403_05', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('tt403_05', 3)	# 11-13	 **attackbox here**
    Unknown23029(3, 3015, 0)
    Unknown23022(0)
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)	# 14-21
    sprite('tt403_06', 20)	# 22-41
    sprite('tt403_06', 10)	# 42-51
    sprite('keep', 32767)	# 52-32818
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
    sprite('tt403_00', 2)	# 1-2
    SFX_3('chain_move')
    sprite('tt403_01', 2)	# 3-4
    sprite('tt403_03', 3)	# 5-7
    GFX_0('ttef403_Zanzoh', 100)
    Unknown21007(1, 33)
    sprite('tt403_04', 2)	# 8-9	 **attackbox here**
    SFX_3('slash_blade_fast')
    sprite('tt403_05', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('tt403_05', 1)	# 11-11	 **attackbox here**
    Unknown23022(0)
    sprite('tt403_05', 3)	# 12-14	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('tt403_06', 8)	# 15-22
    sprite('tt403_06', 20)	# 23-42
    sprite('tt403_06', 10)	# 43-52
    sprite('keep', 32767)	# 53-32819
    enterState('PersonaDeleteAndIdling')
    ExitState()
    label(1)
    sprite('tt403_06', 4)	# 32820-32823
    Unknown23029(3, 4025, 0)
    sprite('tt403_07', 4)	# 32824-32827
    sprite('tt403_07', 20)	# 32828-32847
    GFX_0('403icecharge', 0)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_41 <= 900000):
            clearUponHandler(3)
            sendToLabel(10)
    label(10)
    sprite('tt403_08', 4)	# 32848-32851
    clearUponHandler(3)
    SFX_3('slash_pole_middle')
    GFX_0('Mahabufudain_iceatk', 0)
    Unknown23029(1, 4027, 0)
    sprite('tt403_09', 4)	# 32852-32855
    GFX_0('Mahabufudain', 100)
    sprite('tt403_10', 4)	# 32856-32859
    sprite('tt403_11', 4)	# 32860-32863
    sprite('tt403_12', 4)	# 32864-32867
    sprite('tt403_11', 4)	# 32868-32871
    sprite('tt403_12', 4)	# 32872-32875
    sprite('tt403_11', 4)	# 32876-32879
    sprite('tt403_12', 4)	# 32880-32883
    sprite('tt403_11', 4)	# 32884-32887
    sprite('tt403_12', 4)	# 32888-32891
    sprite('tt403_11', 2)	# 32892-32893
    sprite('keep', 32767)	# 32894-65660
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
    sprite('tt402_00', 2)	# 1-2
    SFX_0('chain_move')
    sprite('tt402_01', 2)	# 3-4
    sprite('tt402_02', 2)	# 5-6
    label(0)
    sprite('tt402_00', 2)	# 7-8
    sprite('tt402_01', 2)	# 9-10
    sprite('tt402_02', 2)	# 11-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tt402_03', 2)	# 13-14
    sprite('tt402_04', 2)	# 15-16
    sprite('tt402_05', 2)	# 17-18
    sprite('tt402_05', 1)	# 19-19
    sprite('tt402_06', 1)	# 20-20	 **attackbox here**
    SFX_3('el054')
    GFX_0('UltimateLaserJizokuSB', 0)
    RefreshMultihit()
    sprite('tt402_06', 1)	# 21-21	 **attackbox here**
    Unknown23022(0)
    sprite('tt402_07', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08', 2)	# 24-25	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09', 2)	# 26-27	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10', 2)	# 28-29	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_06', 2)	# 32-33	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07', 2)	# 34-35	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_09', 2)	# 38-39	 **attackbox here**
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 3)	# 40-42	 **attackbox here**
    Unknown2001()
    sprite('tt402_11', 3)	# 43-45	 **attackbox here**
    sprite('tt402_06', 3)	# 46-48	 **attackbox here**
    sprite('tt402_07', 3)	# 49-51	 **attackbox here**
    sprite('tt402_08', 3)	# 52-54	 **attackbox here**
    sprite('tt402_09', 3)	# 55-57	 **attackbox here**
    sprite('tt402_10', 3)	# 58-60	 **attackbox here**
    sprite('tt402_11', 3)	# 61-63	 **attackbox here**
    sprite('tt402_06', 3)	# 64-66	 **attackbox here**
    sprite('tt402_07', 3)	# 67-69	 **attackbox here**
    sprite('tt402_08', 3)	# 70-72	 **attackbox here**
    sprite('tt402_09', 3)	# 73-75	 **attackbox here**
    sprite('tt402_10', 3)	# 76-78	 **attackbox here**
    sprite('tt402_11', 3)	# 79-81	 **attackbox here**
    sprite('keep', 32767)	# 82-32848
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
    sprite('tt402_00', 2)	# 1-2
    SFX_0('chain_move')
    sprite('tt402_01', 2)	# 3-4
    sprite('tt402_02', 2)	# 5-6
    label(0)
    sprite('tt402_00', 2)	# 7-8
    sprite('tt402_01', 2)	# 9-10
    sprite('tt402_02', 2)	# 11-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('tt402_03', 2)	# 13-14
    sprite('tt402_04', 2)	# 15-16
    sprite('tt402_05', 2)	# 17-18
    sprite('tt402_05', 1)	# 19-19
    sprite('tt402_06ex', 1)	# 20-20	 **attackbox here**
    SFX_3('el054')
    GFX_0('UltimateLaserJizokuSB', 0)
    Unknown21007(1, 33)
    Unknown36(1)
    Unknown1096(2000)
    teleportRelativeX(-33000)
    Unknown35()
    RefreshMultihit()
    sprite('tt402_06ex', 1)	# 21-21	 **attackbox here**
    Unknown23022(0)
    sprite('tt402_07ex', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08ex', 2)	# 24-25	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09ex', 2)	# 26-27	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10ex', 2)	# 28-29	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11ex', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_06ex', 2)	# 32-33	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_07ex', 2)	# 34-35	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08ex', 2)	# 36-37	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_09ex', 2)	# 38-39	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_10ex', 2)	# 40-41	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_11ex', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_06ex', 2)	# 44-45	 **attackbox here**
    SFX_3('el054')
    RefreshMultihit()
    sprite('tt402_07ex', 2)	# 46-47	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_08ex', 2)	# 48-49	 **attackbox here**
    RefreshMultihit()
    sprite('tt402_09ex', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    PushbackX(30000)
    sprite('tt402_10', 3)	# 52-54	 **attackbox here**
    Unknown2001()
    sprite('tt402_11', 3)	# 55-57	 **attackbox here**
    sprite('tt402_06', 3)	# 58-60	 **attackbox here**
    sprite('tt402_07', 3)	# 61-63	 **attackbox here**
    sprite('tt402_08', 3)	# 64-66	 **attackbox here**
    sprite('tt402_09', 3)	# 67-69	 **attackbox here**
    sprite('tt402_10', 3)	# 70-72	 **attackbox here**
    sprite('tt402_11', 3)	# 73-75	 **attackbox here**
    sprite('tt402_06', 3)	# 76-78	 **attackbox here**
    sprite('tt402_07', 3)	# 79-81	 **attackbox here**
    sprite('tt402_08', 3)	# 82-84	 **attackbox here**
    sprite('tt402_09', 3)	# 85-87	 **attackbox here**
    sprite('tt402_10', 3)	# 88-90	 **attackbox here**
    sprite('tt402_11', 3)	# 91-93	 **attackbox here**
    sprite('keep', 32767)	# 94-32860
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
    sprite('tt433_00', 4)	# 1-4
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)	# 5-8
    sprite('tt433_02', 4)	# 9-12
    sprite('tt433_00', 4)	# 13-16
    sprite('tt433_01', 4)	# 17-20
    sprite('tt433_02', 4)	# 21-24
    sprite('tt433_00', 4)	# 25-28
    sprite('tt433_01', 4)	# 29-32
    sprite('tt433_02', 4)	# 33-36
    sprite('tt433_00', 4)	# 37-40
    sprite('tt433_01', 4)	# 41-44
    sprite('tt433_02', 4)	# 45-48
    sprite('tt433_00', 4)	# 49-52
    sprite('tt433_01', 4)	# 53-56
    sprite('tt433_02', 4)	# 57-60
    sprite('tt433_03', 3)	# 61-63

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
    sprite('tt433_04', 1)	# 64-64	 **attackbox here**
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt433_04', 2)	# 65-66	 **attackbox here**
    if SLOT_52:
        DisableAttackRestOfMove()
    else:
        SLOT_53 = 1
    sprite('tt205_07', 2)	# 67-68
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)	# 69-71
    Unknown1019(0)
    sprite('tt205_09', 4)	# 72-75
    sprite('tt205_10', 4)	# 76-79
    sprite('tt205_09', 4)	# 80-83
    sprite('tt205_10', 4)	# 84-87
    sprite('tt205_09', 4)	# 88-91
    sprite('tt205_10', 4)	# 92-95
    sprite('tt205_09', 4)	# 96-99
    sprite('keep', 32767)	# 100-32866
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
    sprite('tt433_04', 3)	# 1-3	 **attackbox here**
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)	# 4-6
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)	# 7-9
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)	# 10-12
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)	# 13-15
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)	# 16-30
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)	# 31-33
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)	# 34-36
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)	# 37-39	 **attackbox here**
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)	# 40-42
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)	# 43-45
    sprite('tt433_15', 9)	# 46-54
    sprite('tt433_15', 21)	# 55-75
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_16', 6)	# 76-81
    sprite('tt433_17', 20)	# 82-101
    sprite('tt433_18', 1)	# 102-102
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)	# 103-105
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)	# 106-109	 **attackbox here**
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
    sprite('tt433_20', 4)	# 110-113
    sprite('tt433_21', 4)	# 114-117
    sprite('tt433_22', 4)	# 118-121
    sprite('tt433_23', 4)	# 122-125
    sprite('tt433_21', 4)	# 126-129
    sprite('tt433_22', 4)	# 130-133
    sprite('tt433_23', 4)	# 134-137
    sprite('tt433_21', 4)	# 138-141
    sprite('tt433_22', 4)	# 142-145
    sprite('tt433_23', 4)	# 146-149
    sprite('keep', 32767)	# 150-32916
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
    sprite('tt433_00', 4)	# 1-4
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)	# 5-8
    sprite('tt433_02', 4)	# 9-12
    sprite('tt433_00', 4)	# 13-16
    sprite('tt433_01', 4)	# 17-20
    sprite('tt433_02', 4)	# 21-24
    sprite('tt433_00', 4)	# 25-28
    sprite('tt433_01', 4)	# 29-32
    sprite('tt433_02', 4)	# 33-36
    sprite('tt433_00', 4)	# 37-40
    sprite('tt433_01', 4)	# 41-44
    sprite('tt433_02', 4)	# 45-48
    sprite('tt433_00', 4)	# 49-52
    sprite('tt433_01', 4)	# 53-56
    sprite('tt433_02', 4)	# 57-60
    sprite('tt433_03', 3)	# 61-63

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
    sprite('tt433_04', 1)	# 64-64	 **attackbox here**
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt433_04', 2)	# 65-66	 **attackbox here**
    if SLOT_52:
        DisableAttackRestOfMove()
    else:
        SLOT_53 = 1
    sprite('tt205_07', 2)	# 67-68
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)	# 69-71
    Unknown1019(0)
    sprite('tt205_09', 4)	# 72-75
    sprite('tt205_10', 4)	# 76-79
    sprite('tt205_09', 4)	# 80-83
    sprite('tt205_10', 4)	# 84-87
    sprite('tt205_09', 4)	# 88-91
    sprite('tt205_10', 4)	# 92-95
    sprite('tt205_09', 4)	# 96-99
    sprite('keep', 32767)	# 100-32866
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
    sprite('tt433_04', 3)	# 1-3	 **attackbox here**
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)	# 4-6
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)	# 7-9
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)	# 10-12
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)	# 13-15
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)	# 16-30
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)	# 31-33
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)	# 34-36
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)	# 37-39	 **attackbox here**
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)	# 40-42
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)	# 43-45
    sprite('tt433_15', 9)	# 46-54
    sprite('tt433_15', 21)	# 55-75
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_15', 10)	# 76-85
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)	# 86-95
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)	# 96-105
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)	# 106-115
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_16', 15)	# 116-130
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)	# 131-140
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)	# 141-150
    ScreenShake(8000, 8000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)	# 151-160
    ScreenShake(8000, 8000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)	# 161-170
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)	# 171-180
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_18', 1)	# 181-181
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)	# 182-184
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)	# 185-188	 **attackbox here**
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
    sprite('tt433_20', 4)	# 189-192
    sprite('tt433_21', 4)	# 193-196
    sprite('tt433_22', 4)	# 197-200
    sprite('tt433_23', 4)	# 201-204
    sprite('tt433_21', 4)	# 205-208
    sprite('tt433_22', 4)	# 209-212
    sprite('tt433_23', 4)	# 213-216
    sprite('tt433_21', 4)	# 217-220
    sprite('tt433_22', 4)	# 221-224
    sprite('tt433_23', 4)	# 225-228
    sprite('tt433_21', 4)	# 229-232
    sprite('tt433_22', 4)	# 233-236
    sprite('tt433_23', 4)	# 237-240
    sprite('tt433_21', 4)	# 241-244
    sprite('tt433_22', 4)	# 245-248
    sprite('tt433_23', 4)	# 249-252
    sprite('keep', 32767)	# 253-33019
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
    sprite('tt433_00', 4)	# 1-4
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)	# 5-8
    sprite('tt433_02', 4)	# 9-12
    sprite('tt433_00', 4)	# 13-16
    sprite('tt433_01', 4)	# 17-20
    sprite('tt433_02', 4)	# 21-24
    sprite('tt433_00', 4)	# 25-28
    sprite('tt433_01', 4)	# 29-32
    sprite('tt433_02', 4)	# 33-36
    sprite('tt433_00', 4)	# 37-40
    sprite('tt433_01', 4)	# 41-44
    sprite('tt433_02', 4)	# 45-48
    sprite('tt433_00', 4)	# 49-52
    sprite('tt433_01', 4)	# 53-56
    sprite('tt433_02', 4)	# 57-60
    sprite('tt433_00', 4)	# 61-64
    sprite('tt433_01', 4)	# 65-68
    sprite('tt433_03', 3)	# 69-71

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
    physicsXImpulse(50000)
    SFX_3('chain_move')
    sprite('tt433_04', 3)	# 72-74	 **attackbox here**
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)	# 75-76
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)	# 77-79
    Unknown1019(0)
    sprite('tt205_09', 4)	# 80-83
    sprite('tt205_10', 4)	# 84-87
    sprite('tt205_09', 4)	# 88-91
    sprite('tt205_10', 4)	# 92-95
    sprite('tt205_09', 4)	# 96-99
    sprite('tt205_10', 4)	# 100-103
    sprite('tt205_09', 4)	# 104-107
    sprite('keep', 32767)	# 108-32874
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32875-65641
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
    sprite('tt433_04', 3)	# 1-3	 **attackbox here**
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)	# 4-5
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)	# 6-8
    Unknown1019(0)
    sprite('tt205_09', 4)	# 9-12
    sprite('tt205_10', 4)	# 13-16
    sprite('tt205_09', 4)	# 17-20
    sprite('tt205_10', 4)	# 21-24
    sprite('tt205_09', 4)	# 25-28
    sprite('tt205_10', 4)	# 29-32
    sprite('tt205_09', 4)	# 33-36
    sprite('keep', 32767)	# 37-32803
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
    sprite('tt433_04', 3)	# 1-3	 **attackbox here**
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)	# 4-6
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)	# 7-9
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)	# 10-12
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)	# 13-15
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)	# 16-30
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)	# 31-33
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)	# 34-36
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)	# 37-39	 **attackbox here**
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)	# 40-42
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)	# 43-45
    sprite('tt433_15', 9)	# 46-54
    sprite('tt433_15', 21)	# 55-75
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_16', 6)	# 76-81
    sprite('tt433_17', 20)	# 82-101
    sprite('tt433_18', 1)	# 102-102
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)	# 103-105
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)	# 106-109	 **attackbox here**
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
    sprite('tt433_20', 4)	# 110-113
    sprite('tt433_21', 4)	# 114-117
    sprite('tt433_22', 4)	# 118-121
    sprite('tt433_23', 4)	# 122-125
    sprite('tt433_21', 4)	# 126-129
    sprite('tt433_22', 4)	# 130-133
    sprite('tt433_23', 4)	# 134-137
    sprite('tt433_21', 4)	# 138-141
    sprite('tt433_22', 4)	# 142-145
    sprite('tt433_23', 4)	# 146-149
    sprite('keep', 32767)	# 150-32916
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
    sprite('tt433_00', 4)	# 1-4
    if (SLOT_25 < 335000):
        Unknown1000(1865000)
        teleportRelativeX(-335000)
    sprite('tt433_01', 4)	# 5-8
    sprite('tt433_02', 4)	# 9-12
    sprite('tt433_00', 4)	# 13-16
    sprite('tt433_01', 4)	# 17-20
    sprite('tt433_02', 4)	# 21-24
    sprite('tt433_00', 4)	# 25-28
    sprite('tt433_01', 4)	# 29-32
    sprite('tt433_02', 4)	# 33-36
    sprite('tt433_00', 4)	# 37-40
    sprite('tt433_01', 4)	# 41-44
    sprite('tt433_02', 4)	# 45-48
    sprite('tt433_00', 4)	# 49-52
    sprite('tt433_01', 4)	# 53-56
    sprite('tt433_02', 4)	# 57-60
    sprite('tt433_00', 4)	# 61-64
    sprite('tt433_01', 4)	# 65-68
    sprite('tt433_03', 3)	# 69-71

    def upon_CLEAR_OR_EXIT():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
    physicsXImpulse(50000)
    SFX_3('chain_move')
    sprite('tt433_04', 3)	# 72-74	 **attackbox here**
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)	# 75-76
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)	# 77-79
    Unknown1019(0)
    sprite('tt205_09', 4)	# 80-83
    sprite('tt205_10', 4)	# 84-87
    sprite('tt205_09', 4)	# 88-91
    sprite('tt205_10', 4)	# 92-95
    sprite('tt205_09', 4)	# 96-99
    sprite('tt205_10', 4)	# 100-103
    sprite('tt205_09', 4)	# 104-107
    sprite('keep', 32767)	# 108-32874
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32875-65641
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
    sprite('tt433_04', 3)	# 1-3	 **attackbox here**
    clearUponHandler(3)
    RefreshMultihit()
    Unknown1019(40)
    sprite('tt205_07', 2)	# 4-5
    Unknown1019(25)
    teleportRelativeX(-30000)
    sprite('tt205_08', 3)	# 6-8
    Unknown1019(0)
    sprite('tt205_09', 4)	# 9-12
    sprite('tt205_10', 4)	# 13-16
    sprite('tt205_09', 4)	# 17-20
    sprite('tt205_10', 4)	# 21-24
    sprite('tt205_09', 4)	# 25-28
    sprite('tt205_10', 4)	# 29-32
    sprite('tt205_09', 4)	# 33-36
    sprite('keep', 32767)	# 37-32803
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
    sprite('tt433_04', 3)	# 1-3	 **attackbox here**
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    Unknown20000(1)
    Unknown20003(1)
    sprite('tt433_05', 3)	# 4-6
    GFX_0('ttef433_hitsugi', 100)
    Unknown2015(-1)
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_06', 3)	# 7-9
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_07', 3)	# 10-12
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_08', 3)	# 13-15
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_09', 15)	# 16-30
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_10', 3)	# 31-33
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_11', 3)	# 34-36
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('tt433_12', 3)	# 37-39	 **attackbox here**
    ScreenShake(20000, 10000)
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown36(22)
    Unknown1084(1)
    setGravity(0)
    teleportRelativeX(-28000)
    Unknown35()
    SFX_3('damage_hit_h')
    sprite('tt433_13', 3)	# 40-42
    Unknown36(22)
    teleportRelativeX(28000)
    Unknown35()
    sprite('tt433_14', 3)	# 43-45
    sprite('tt433_15', 9)	# 46-54
    sprite('tt433_15', 21)	# 55-75
    Unknown21012('747465663433335f68697473756769000000000000000000000000000000000021000000')
    Unknown5005(0)
    Unknown36(22)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    SFX_3('bound_marble_m')
    sprite('tt433_15', 10)	# 76-85
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)	# 86-95
    ScreenShake(2000, 2000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)	# 96-105
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_15', 10)	# 106-115
    ScreenShake(4000, 4000)
    SFX_3('quake_s')
    sprite('tt433_16', 15)	# 116-130
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)	# 131-140
    ScreenShake(6000, 6000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)	# 141-150
    ScreenShake(8000, 8000)
    SFX_3('quake_s')
    sprite('tt433_17', 10)	# 151-160
    ScreenShake(8000, 8000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)	# 161-170
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_17', 10)	# 171-180
    ScreenShake(10000, 10000)
    SFX_3('quake_l')
    sprite('tt433_18', 1)	# 181-181
    GFX_0('ttef433_Zanzoh', 100)
    sprite('tt433_18', 3)	# 182-184
    SFX_3('slash_blade_middle')
    sprite('tt433_19', 4)	# 185-188	 **attackbox here**
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
    sprite('tt433_20', 4)	# 189-192
    sprite('tt433_21', 4)	# 193-196
    sprite('tt433_22', 4)	# 197-200
    sprite('tt433_23', 4)	# 201-204
    sprite('tt433_21', 4)	# 205-208
    sprite('tt433_22', 4)	# 209-212
    sprite('tt433_23', 4)	# 213-216
    sprite('tt433_21', 4)	# 217-220
    sprite('tt433_22', 4)	# 221-224
    sprite('tt433_23', 4)	# 225-228
    sprite('tt433_21', 4)	# 229-232
    sprite('tt433_22', 4)	# 233-236
    sprite('tt433_23', 4)	# 237-240
    sprite('tt433_21', 4)	# 241-244
    sprite('tt433_22', 4)	# 245-248
    sprite('tt433_23', 4)	# 249-252
    sprite('keep', 32767)	# 253-33019
    enterState('PersonaDeleteAndIdling')

@State
def ttef433_Zanzoh():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3032()
    sprite('vr_tt433_00', 4)	# 1-4
    sprite('vr_tt433_01', 4)	# 5-8
    sprite('vr_tt433_02', 3)	# 9-11
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
    sprite('vr_tt433_10', 2)	# 1-2
    GFX_1('elef_hitugi_entry', 100)
    sprite('vr_tt433_10add01', 2)	# 3-4
    sprite('vr_tt433_10add02', 2)	# 5-6
    sprite('vr_tt433_10add02', 3)	# 7-9
    sprite('vr_tt433_10add02', 1)	# 10-10
    teleportRelativeX(-12000)
    sprite('vr_tt433_10add02', 2)	# 11-12
    teleportRelativeX(12000)
    sprite('vr_tt433_11', 2)	# 13-14
    sprite('vr_tt433_12', 3)	# 15-17
    sprite('vr_tt433_13', 32767)	# 18-32784
    label(0)
    sprite('vr_tt433_13', 3)	# 32785-32787
    teleportRelativeX(-48000)
    sprite('vr_tt433_13', 3)	# 32788-32790
    teleportRelativeX(36000)
    sprite('vr_tt433_13', 32767)	# 32791-65557
    teleportRelativeX(-12000)
    label(1)
    sprite('vr_tt433_11', 3)	# 65558-65560
    sprite('vr_tt433_10add02', 2)	# 65561-65562
    Unknown23118(-14081)
    Unknown23119(-16777216, 8, -1)
    GFX_0('ttef433_hitsugi_kusari', 100)
    GFX_1('elef_hitugi_kousoku', 0)
    Unknown3029(1)
    Unknown3069(2)
    sprite('vr_tt433_10add02', 2)	# 65563-65564
    teleportRelativeX(-12000)
    sprite('vr_tt433_10add02', 2)	# 65565-65566
    teleportRelativeX(12000)
    loopRest()
    label(10)
    sprite('vr_tt433_10add02', 1)	# 65567-65567
    sprite('vr_tt433_10add02', 2)	# 65568-65569
    teleportRelativeX(-6000)
    sprite('vr_tt433_10add02', 2)	# 65570-65571
    teleportRelativeX(6000)
    sprite('vr_tt433_10add02', 1)	# 65572-65572
    sprite('vr_tt433_10add02', 2)	# 65573-65574
    teleportRelativeX(12000)
    sprite('vr_tt433_10add02', 2)	# 65575-65576
    teleportRelativeX(-12000)
    loopRest()
    gotoLabel(10)
    label(2)
    sprite('null', 1)	# 65577-65577
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
    sprite('vr_ttef433_chain', 32767)	# 1-32767

@State
def ttef433_hitsugi_kusari_flash():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown3033()
        Unknown3001(0)
    label(0)
    sprite('vr_ttef433_chain', 25)	# 1-25
    Unknown3004(10)
    sprite('vr_ttef433_chain', 25)	# 26-50
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
    sprite('null', 3)	# 1-3
    SFX_3('guard_hit_l')
    sprite('null', 3)	# 4-6
    SFX_3('guard_slash_l')
    sprite('null', 3)	# 7-9
    SFX_3('guard_hit_l')
    sprite('null', 111)	# 10-120

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
    sprite('vr_tt433_10ex01', 32767)	# 1-32767

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
    sprite('vr_tt433_10ex02', 32767)	# 1-32767

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
    sprite('vr_tt433_10ex03', 32767)	# 1-32767

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
    sprite('vr_tt433_10ex04', 32767)	# 1-32767

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
    sprite('tt450_00ab', 4)	# 1-4	 **attackbox here**
    sprite('tt450_01ab', 4)	# 5-8	 **attackbox here**
    sprite('tt450_02ab', 4)	# 9-12	 **attackbox here**
    sprite('tt450_00ab', 4)	# 13-16	 **attackbox here**
    sprite('tt450_01ab', 4)	# 17-20	 **attackbox here**
    sprite('tt450_02ab', 4)	# 21-24	 **attackbox here**
    sprite('tt450_00ab', 4)	# 25-28	 **attackbox here**
    sprite('tt450_01ab', 4)	# 29-32	 **attackbox here**
    sprite('tt450_02ab', 4)	# 33-36	 **attackbox here**
    sprite('tt450_03ab', 4)	# 37-40	 **attackbox here**
    sprite('tt450_04ab', 4)	# 41-44	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 45-48	 **attackbox here**
    sprite('tt450_06ab', 4)	# 49-52	 **attackbox here**
    sprite('tt450_07ab', 4)	# 53-56	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 57-60	 **attackbox here**
    sprite('tt450_06ab', 4)	# 61-64	 **attackbox here**
    sprite('tt450_07ab', 4)	# 65-68	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 69-72	 **attackbox here**
    sprite('tt450_06ab', 4)	# 73-76	 **attackbox here**
    sprite('tt450_07ab', 4)	# 77-80	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 81-84	 **attackbox here**
    sprite('tt450_06ab', 4)	# 85-88	 **attackbox here**
    sprite('tt450_07ab', 4)	# 89-92	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 93-96	 **attackbox here**
    sprite('tt450_06ab', 4)	# 97-100	 **attackbox here**
    sprite('tt450_07ab', 4)	# 101-104	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 105-108	 **attackbox here**
    sprite('tt450_06ab', 4)	# 109-112	 **attackbox here**
    sprite('tt450_07ab', 4)	# 113-116	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 117-120	 **attackbox here**
    sprite('tt450_06ab', 4)	# 121-124	 **attackbox here**
    sprite('tt450_07ab', 4)	# 125-128	 **attackbox here**
    SFX_3('el006')
    sprite('tt450_05ab', 4)	# 129-132	 **attackbox here**
    sprite('tt450_06ab', 4)	# 133-136	 **attackbox here**
    sprite('tt450_07ab', 4)	# 137-140	 **attackbox here**
    SFX_3('el006')
    label(0)
    sprite('tt450_05ab', 4)	# 141-144	 **attackbox here**
    sprite('tt450_06ab', 4)	# 145-148	 **attackbox here**
    sprite('tt450_07ab', 4)	# 149-152	 **attackbox here**
    SFX_3('el006')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 32767)	# 153-32919
    enterState('PersonaDeleteAndIdling')

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
    sprite('tt600_00', 4)	# 1-4
    SFX_3('chain_move')
    sprite('tt600_01', 4)	# 5-8
    sprite('tt600_02', 4)	# 9-12
    sprite('tt600_00', 4)	# 13-16
    SFX_3('chain_move')
    sprite('tt600_01', 4)	# 17-20
    sprite('tt600_02', 4)	# 21-24
    sprite('tt600_00', 4)	# 25-28
    SFX_3('chain_move')
    sprite('tt600_01', 4)	# 29-32
    sprite('tt600_02', 4)	# 33-36
    sprite('tt600_03', 5)	# 37-41
    sprite('tt600_04', 5)	# 42-46
    sprite('tt600_05', 25)	# 47-71
    sprite('tt600_07', 4)	# 72-75
    GFX_0('EnterHoukouLoop', 0)
    SFX_3('el006')
    sprite('tt600_08', 4)	# 76-79
    SFX_3('chain_move')
    sprite('tt600_09', 4)	# 80-83
    sprite('tt600_07', 4)	# 84-87
    sprite('tt600_08', 4)	# 88-91
    SFX_3('chain_move')
    sprite('tt600_09', 4)	# 92-95
    sprite('tt600_07', 4)	# 96-99
    sprite('tt600_08', 4)	# 100-103
    SFX_3('chain_move')
    sprite('tt600_09', 4)	# 104-107
    sprite('tt600_07', 4)	# 108-111
    sprite('tt600_08', 4)	# 112-115
    sprite('tt600_09', 4)	# 116-119
    sprite('keep', 32767)	# 120-32886
    enterState('PersonaDeleteAndIdling')

@State
def EnterHoukou():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('656c65665f686f756b6f7573686f636b2e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3001(150)
    sprite('null', 3)	# 1-3
    sprite('null', 5)	# 4-8
    Unknown1099(80)
    Unknown3004(-51)
    loopRest()

@State
def EnterHoukouLoop():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
    sprite('null', 5)	# 1-5
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)	# 6-10
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)	# 11-15
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)	# 16-20
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)	# 21-25
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)	# 26-30
    GFX_0('EnterHoukou', 100)
    GFX_1('ttef_toujousmoke_l', 100)
    sprite('null', 5)	# 31-35
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
    sprite('vr_el600_00', 4)	# 1-4
    Unknown3001(0)
    Unknown3004(16)
    physicsYImpulse(500)
    sprite('vr_el600_01', 4)	# 5-8
    sprite('vr_el600_02', 4)	# 9-12
    sprite('vr_el600_00', 4)	# 13-16
    sprite('vr_el600_01', 4)	# 17-20
    sprite('vr_el600_02', 4)	# 21-24
    sprite('vr_el600_00', 4)	# 25-28
    sprite('vr_el600_01', 4)	# 29-32
    sprite('vr_el600_02', 4)	# 33-36
    sprite('vr_el600_00', 4)	# 37-40
    sprite('vr_el600_01', 4)	# 41-44
    sprite('vr_el600_02', 4)	# 45-48
    sprite('vr_el600_00', 4)	# 49-52
    sprite('vr_el600_01', 4)	# 53-56
    sprite('vr_el600_02', 4)	# 57-60
    GFX_1('persona_enter_ply', 100)

@State
def elef600_cardlight_add():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
    label(0)
    sprite('null', 3)	# 1-3
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
    sprite('vr_elef601_light', 16)	# 1-16
    Unknown1059(40)
    sprite('vr_elef601_light', 32767)	# 17-32783
    Unknown1059(2)
    loopRest()
    label(0)
    sprite('vr_elef601_light', 20)	# 32784-32803
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
    sprite('null', 32767)	# 1-32767
    label(0)
    sprite('null', 20)	# 32768-32787
    Unknown3004(-12)

@State
def elef601_EntryBookEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4054(5)
        Unknown23067('elef_del_book')
        Unknown1074(-5000)
    sprite('null', 20)	# 1-20
    Unknown1099(20)
    sprite('null', 10)	# 21-30
    Unknown1099(0)
    sprite('null', 10)	# 31-40
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
    sprite('vr_el601_08', 20)	# 1-20
    Unknown1099(50)
    sprite('vr_el601_08', 32767)	# 21-32787
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
    sprite('vr_el610_00', 6)	# 1-6
    SFX_3('distortion_b')
    sprite('vr_el610_01', 6)	# 7-12
    sprite('vr_el610_02', 6)	# 13-18
    sprite('vr_el610_03', 220)	# 19-238
    sprite('vr_el610_02', 6)	# 239-244
    SFX_3('distortion_b')
    sprite('vr_el610_01', 6)	# 245-250

@State
def elef610_door_add():

    def upon_IMMEDIATE():
        teleportRelativeX(-256000)
        Unknown1007(8000)
        Unknown3033()
        Unknown4061(2)
        Unknown13044(1)
    sprite('null', 18)	# 1-18
    sprite('vr_el610_10', 220)	# 19-238
    Unknown3001(0)
    Unknown3004(64)
    sprite('vr_el610_10', 12)	# 239-250
    sprite('vr_el610_10', 64)	# 251-314
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
    sprite('tt611_00', 5)	# 1-5
    SFX_3('chain_move')
    sprite('tt611_01', 5)	# 6-10
    sprite('tt611_02', 5)	# 11-15
    sprite('tt611_03', 5)	# 16-20
    sprite('tt611_04', 5)	# 21-25
    sprite('tt611_05', 8)	# 26-33
    sprite('tt611_06', 6)	# 34-39
    label(0)
    sprite('tt611_07', 5)	# 40-44
    SFX_3('cloth_l')
    sprite('tt611_08', 5)	# 45-49
    sprite('tt611_09', 5)	# 50-54
    gotoLabel(0)

@State
def elef611_WinCard():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 2)	# 1-2
    GFX_0('elef611_WinCard00', 100)
    sprite('null', 2)	# 3-4
    GFX_0('elef611_WinCard01', 100)
    sprite('null', 2)	# 5-6
    GFX_0('elef611_WinCard02', 100)
    sprite('null', 2)	# 7-8
    GFX_0('elef611_WinCard03', 100)
    sprite('null', 2)	# 9-10
    GFX_0('elef611_WinCard04', 100)
    sprite('null', 2)	# 11-12
    GFX_0('elef611_WinCard05', 100)
    sprite('null', 2)	# 13-14
    GFX_0('elef611_WinCard06', 100)
    sprite('null', 2)	# 15-16
    GFX_0('elef611_WinCard07', 100)
    sprite('null', 2)	# 17-18
    GFX_0('elef611_WinCard08', 100)
    sprite('null', 2)	# 19-20
    GFX_0('elef611_WinCard09', 100)
    sprite('null', 32767)	# 21-32787

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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
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
    sprite('null', 30)	# 1-30
    sprite('null', 32767)	# 31-32797
    clearUponHandler(3)
    Unknown1084(1)

@State
def elef611_Book():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
    label(0)
    sprite('vr_el611_01', 4)	# 1-4
    sprite('vr_el611_02', 4)	# 5-8
    sprite('vr_el611_03', 4)	# 9-12
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
    sprite('vr_el611_01', 4)	# 1-4
    sprite('vr_el611_02', 4)	# 5-8
    sprite('vr_el611_03', 4)	# 9-12
    sprite('vr_el611_01', 4)	# 13-16
    sprite('vr_el611_02', 4)	# 17-20
    sprite('vr_el611_03', 4)	# 21-24
    sprite('vr_el611_01', 4)	# 25-28
    sprite('vr_el611_02', 4)	# 29-32
    sprite('vr_el611_03', 4)	# 33-36
    sprite('vr_el611_01', 4)	# 37-40
    sprite('vr_el611_02', 4)	# 41-44
    sprite('vr_el611_03', 4)	# 45-48
    sprite('vr_el611_01', 4)	# 49-52
    sprite('vr_el611_02', 4)	# 53-56
    sprite('vr_el611_03', 4)	# 57-60
    sprite('vr_el611_01', 4)	# 61-64
    sprite('vr_el611_02', 4)	# 65-68
    sprite('vr_el611_03', 4)	# 69-72
    sprite('vr_el611_01', 4)	# 73-76
    sprite('vr_el611_02', 4)	# 77-80
    sprite('vr_el611_03', 4)	# 81-84

@State
def elef611_DelBookEff():

    def upon_IMMEDIATE():
        Unknown4054(5)
        Unknown23067('elef_del_book')
        Unknown4010(2)
        Unknown3001(0)
        Unknown3004(25)
        Unknown1074(-10000)
    sprite('null', 10)	# 1-10
    sprite('null', 20)	# 11-30
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
    sprite('tt600_00', 4)	# 1-4
    SFX_3('chain_move')
    sprite('tt600_01', 4)	# 5-8
    sprite('tt600_02', 4)	# 9-12
    sprite('tt600_00', 4)	# 13-16
    SFX_3('chain_move')
    sprite('tt600_01', 4)	# 17-20
    sprite('tt600_02', 4)	# 21-24
    sprite('tt600_00', 4)	# 25-28
    SFX_3('chain_move')
    sprite('tt600_01', 4)	# 29-32
    sprite('tt600_02', 4)	# 33-36
    sprite('tt600_03', 5)	# 37-41
    sprite('tt600_04', 5)	# 42-46
    sprite('tt600_05', 25)	# 47-71
    sprite('tt600_07', 4)	# 72-75
    GFX_0('EnterHoukouLoop', 0)
    SFX_3('el006')
    sprite('tt600_08', 4)	# 76-79
    SFX_3('chain_move')
    label(0)
    sprite('tt600_09', 4)	# 80-83
    sprite('tt600_07', 4)	# 84-87
    sprite('tt600_08', 4)	# 88-91
    gotoLabel(0)