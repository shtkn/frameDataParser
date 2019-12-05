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

@Subroutine
def CompositeImageSetting():
    Unknown3060('0000000076725f6d61676174737561757261303000000000000000000000000000000000')
    Unknown3061(0, 4)
    Unknown3063(0, 180000)
    Unknown3064(0, -1000)
    Unknown3068('0000000060000000ff000000ff000000ff000000')

@Subroutine
def PalEffSetting():

    def upon_45():
        Unknown23030('7061645f706572736f6e615f6c696d6974666c6173680000000000000000000000000000f000000000000000f100000000000000fe0000000000000004000000')

@State
def PAD_PersonaCreate():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown13043(-75000)
        teleportRelativeY(0)
        Unknown23013(1)
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown24('5041445f506572736f6e6157616974000000000000000000000000000000000064000000')

@State
def PAD_PersonaWait():

    def upon_IMMEDIATE():
        SLOT_11 = 0
        SLOT_59 = (-1)
        callSubroutine('PAD_ReceptionSignal')
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    loopRest()

@Subroutine
def PAD_ReceptionSignal():

    def upon_43():
        if (SLOT_48 == 2001):
            Unknown23185('5041445f506572736f6e615468726f7753686f7400000000000000000000000032000000')
        if (SLOT_48 == 2002):
            Unknown23185('5041445f506572736f6e6135430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2003):
            Unknown23185('5041445f506572736f6e6135434300000000000000000000000000000000000032000000')
        if (SLOT_48 == 2004):
            Unknown23185('5041445f506572736f6e6135434343000000000000000000000000000000000032000000')
        if (SLOT_48 == 2005):
            Unknown23185('5041445f506572736f6e614a430000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2006):
            Unknown23185('5041445f506572736f6e614a324300000000000000000000000000000000000032000000')
        if (SLOT_48 == 2007):
            Unknown23185('5041445f506572736f6e614a324345780000000000000000000000000000000032000000')
        if (SLOT_48 == 2008):
            Unknown23185('5041445f506572736f6e6143410000000000000000000000000000000000000032000000')
        if (SLOT_48 == 2501):
            Unknown23185('5041445f506572736f6e61416e746941697250536b696c6c000000000000000032000000')
        if (SLOT_48 == 2502):
            Unknown23185('5041445f506572736f6e6153656172636853686f7450536b696c6c000000000032000000')
        if (SLOT_48 == 3001):
            Unknown23185('5041445f506572736f6e615370656369616c4661737453686f7400000000000032000000')
        if (SLOT_48 == 3002):
            Unknown23185('5041445f506572736f6e615370656369616c536c6f7753686f7400000000000032000000')
        if (SLOT_48 == 3501):
            Unknown23185('5041445f506572736f6e615370656369616c53656172636853686f740000000032000000')
        if (SLOT_48 == 3003):
            Unknown23185('5041445f506572736f6e615370656369616c416e74694169724661737400000032000000')
        if (SLOT_48 == 3004):
            Unknown23185('5041445f506572736f6e615370656369616c416e7469416972536c6f7700000032000000')
        if (SLOT_48 == 3005):
            Unknown23185('5041445f506572736f6e615370656369616c5468726f7700000000000000000032000000')
        if (SLOT_48 == 4001):
            SLOT_60 = 0
            Unknown23185('5041445f506572736f6e61556c74696d61746541737361756c7400000000000032000000')
        if (SLOT_48 == 4021):
            SLOT_60 = 1
            Unknown23185('5041445f506572736f6e61556c74696d61746541737361756c7400000000000032000000')
        if (SLOT_48 == 4002):
            SLOT_60 = 0
            Unknown23185('5041445f506572736f6e61556c74696d617465426c616465000000000000000032000000')
        if (SLOT_48 == 4003):
            SLOT_60 = 0
            Unknown23185('5041445f506572736f6e61556c74696d617465426c616465535000000000000032000000')
        if (SLOT_48 == 4004):
            SLOT_60 = 0
            Unknown23185('5041445f506572736f6e61556c74696d6174655468726f77000000000000000032000000')
        if (SLOT_48 == 4501):
            SLOT_60 = 0
            Unknown23185('5041445f506572736f6e6141737472616c48656174000000000000000000000032000000')
        if (SLOT_48 == 4005):
            Unknown23185('5041445f506572736f6e61556c74696d61746544554f0000000000000000000032000000')
        if (SLOT_48 == 4006):
            Unknown23185('5041445f506572736f6e61556c74696d61746544554f5350000000000000000032000000')
        if (SLOT_48 == 9999):
            Unknown23185('506572736f6e6144656c657465416e6449646c696e67000000000000000000002c010000')
        if (SLOT_48 == 10001):
            Unknown23185('5041445f506572736f6e614d6174636857696e0000000000000000000000000032000000')
        if (SLOT_48 == 10002):
            Unknown23185('5041445f506572736f6e614d6174636857696e4d69737400000000000000000032000000')

@Subroutine
def PersonaReset():
    Unknown4061(1)
    Unknown23022(0)
    Unknown2053(0)
    Unknown3001(255)
    Unknown3032()
    callSubroutine('CompositeImageSetting')
    callSubroutine('PalEffSetting')
    Unknown23015(11)
    Unknown2019(-1)
    Unknown1084(1)
    Unknown4009(0)
    Unknown4008(0)
    Unknown4007(0)
    EnableCollision(0)
    Unknown30041('')
    Unknown2053(0)
    Unknown2034(0)

@Subroutine
def PAD_EffectInit():
    Unknown2019(5)
    Unknown23015(11)

@Subroutine
def PAD_AttackInit():
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
    callSubroutine('PAD_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAD_SPAttackInit():
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
    callSubroutine('PAD_ReceptionSignal')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown23023()
    EnableCollision(1)
    Unknown30040(1)
    Unknown30040(2)

@Subroutine
def PAD_DDAttackInit():
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
    callSubroutine('PAD_ReceptionSignal')
    Unknown23023()

@Subroutine
def PAD_CheckWarp():
    if SLOT_58:
        SLOT_58 = 1

@Subroutine
def PAD_ForceWarp():
    SLOT_58 = 1

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
    enterState('PAD_PersonaWait')

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
        callSubroutine('CompositeImageSetting')
        callSubroutine('PalEffSetting')
        callSubroutine('PersonaReset')
        callSubroutine('PAD_ReceptionSignal')
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
def KowarePreset():
    Unknown23089('0100000000000000000000000000000000000000000000000100000000000000')
    sendToLabelUpon(54, 580)
    sendToLabelUpon(32, 580)

@State
def BintaHit():
    sprite('null', 5)	# 1-5
    GFX_1('ef_hit_blowm', 100)
    SFX_3('slap_fast')

@State
def adef_400_explosion():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
    sprite('null', 30)	# 1-30
    Unknown1096(2000)
    Unknown23067('adef_405shot')

@State
def ad400_Gun():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1007(100000)
    sprite('ad400_10z', 3)	# 1-3
    SFX_3('cloth_m')
    physicsXImpulse(14000)
    physicsYImpulse(30000)
    setGravity(2000)
    GFX_0('ad400_Gun_sub', 0)
    sprite('ad400_11z', 3)	# 4-6
    sprite('ad400_10z', 3)	# 7-9
    SFX_3('cloth_m')
    sprite('ad400_11z', 3)	# 10-12
    sprite('ad400_10z', 3)	# 13-15
    SFX_3('cloth_m')
    sprite('ad400_11z', 3)	# 16-18
    sprite('ad400_10z', 3)	# 19-21
    SFX_3('cloth_m')
    Unknown3004(-12)
    sprite('ad400_11z', 3)	# 22-24
    sprite('ad400_10z', 3)	# 25-27
    SFX_3('cloth_m')

@State
def ad400_Gun_sub():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(20000)
    sprite('null', 2)	# 1-2
    label(0)
    sprite('null', 6)	# 3-8
    GFX_1('adef_400gun', 100)
    gotoLabel(0)

@State
def adef_405_muzzle_a():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown1072(40000)
    sprite('null', 5)	# 1-5
    Unknown4048(0)
    Unknown23067('adef_405muzzle')

@State
def dmy_LowShotA_Atk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(4)
        AirPushbackX(12000)
        AirPushbackY(-26000)
        Unknown9310(1)
        HitLow(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown23078(1)
        Unknown2053(1)
    sprite('null', 1)	# 1-1
    GFX_0('adef_405_shot', 100)
    sprite('dmy_LowShot_Atk', 3)	# 2-4
    RefreshMultihit()

@State
def adef_405_shot():

    def upon_IMMEDIATE():
        Unknown4007(2)
    sprite('null', 30)	# 1-30
    SFX_3('ad007')
    Unknown1056(960)
    Unknown1064(1200)
    Unknown23067('adef_405shot')

@State
def adef_401_dash():

    def upon_IMMEDIATE():
        teleportRelativeX(30000)
    sprite('null', 1)	# 1-1
    GFX_1('adef_401dash', 100)

@State
def PowerUpAura():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
    label(0)
    sprite('null', 10)	# 1-10
    GFX_0('PowerUpAuraSub', 103)
    gotoLabel(0)

@State
def PowerUpAuraSub():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(2)
        Unknown1007(150000)
    sprite('null', 30)	# 1-30
    GFX_2('adef_401aura')

@State
def UltimateAirAssaultAsiba():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_2('adef_giobceaura_02')
        Unknown4007(3)
        Unknown2054(1)
        Unknown1007(40000)
        Unknown3001(180)
        callSubroutine('KowarePreset')
    sprite('null', 200)	# 1-200
    sprite('null', 10)	# 201-210
    Unknown3004(-25)
    ExitState()
    label(580)
    sprite('null', 10)	# 211-220
    Unknown4007(0)
    Unknown3004(-25)

@State
def mgef_450_yuka():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('6d6765665f34353079756b612e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown23015(2)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown23089('0100000000000000000000000000000000000000000000000100000000000000')
        sendToLabelUpon(54, 580)

        def upon_32():
            Unknown21012('6d6765665f3435305f79756b615345000000000000000000000000000000000020000000')
            sendToLabel(580)
        GFX_0('mgef_450_yukaSE', -1)
    sprite('null', 14)	# 1-14
    Unknown3001(0)
    GFX_1('mgef_450yuka_splash', 100)
    sprite('null', 1)	# 15-15
    GFX_0('Ichigeki_Atk', 100)
    sprite('null', 32767)	# 16-32782
    Unknown1096(6000)
    Unknown3001(0)
    Unknown3004(12)
    label(580)
    sprite('null', 20)	# 32783-32802
    Unknown3004(-12)

@State
def mgef_450_yukaSE():

    def upon_IMMEDIATE():
        Unknown4010(2)
        sendToLabelUpon(32, 0)
        Unknown2037(40)
    label(1)
    sprite('null', 40)	# 1-40
    SFX_3('ad011')
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(1)
    label(0)
    sprite('null', 1)	# 41-41

@State
def Ichigeki_Atk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown4010(3)
        Unknown2054(1)
        AttackLevel_(5)
        Damage(0)
        Unknown11034(0)
        ProjectileDurabilityLvl(3)
        Hitstop(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(56)
        Unknown9142(9999)
        AirPushbackX(0)
        AirPushbackY(0)
        PushbackX(0)
        YImpluseBeforeWallbounce(0)
        Unknown11064(1)
        Unknown11042(1)
        Unknown11084(1)
        Unknown9021(1)
        Unknown23151(22, 104)

        def upon_12():
            Unknown23029(3, 4511, 0)
    sprite('null', 5)	# 1-5
    sprite('dmy_Ichigeki_Atk', 5)	# 6-10
    RefreshMultihit()

@State
def PAD_PersonaThrowShot():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('1600000064000000f049020000fa000000000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        Unknown2006()
        AttackLevel_(5)
        Damage(2500)
        Unknown11056(2)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown9266(8)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackY(-35000)
        AirPushbackX(2000)
        Unknown9190(1)
        Unknown11084(1)
        Unknown9021(1)
        Unknown11044(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11058('0000000000000000000000000100000000000000')
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PAD_CheckWarp')
        EnableCollision(0)
        Unknown2053(1)
        Unknown23022(1)
        Unknown3032()
        sendToLabelUpon(33, 1)
    sprite('mg406_00', 4)	# 1-4
    Unknown3001(0)
    Unknown3004(9)
    GFX_0('mgef_406_charge', 0)
    GFX_0('charge_se', 0)
    physicsYImpulse(8000)
    sprite('mg406_01', 4)	# 5-8
    sprite('mg406_02', 4)	# 9-12
    physicsYImpulse(3000)
    sprite('mg406_00', 4)	# 13-16
    sprite('mg406_01', 4)	# 17-20
    sprite('mg406_02', 4)	# 21-24
    physicsYImpulse(1000)
    sprite('mg406_00', 4)	# 25-28
    sprite('mg406_01', 4)	# 29-32
    sprite('mg406_02', 4)	# 33-36
    physicsYImpulse(200)
    sprite('mg406_00', 4)	# 37-40
    sprite('mg406_01', 4)	# 41-44
    sprite('mg406_02', 4)	# 45-48
    physicsYImpulse(0)
    label(1)
    sprite('mg406_03', 6)	# 49-54
    Unknown21012('6d6765665f3430365f636861726765000000000000000000000000000000000020000000')
    sprite('mg406_04', 6)	# 55-60
    physicsYImpulse(1000)
    sprite('mg406_05', 8)	# 61-68
    physicsYImpulse(0)
    sprite('mg406_06', 4)	# 69-72
    sprite('mg406_07', 3)	# 73-75	 **attackbox here**
    SFX_3('hit_m_middle')
    Unknown26('mgef_406_charge')
    GFX_0('mgef_406_throw', 0)
    sprite('mg406_08', 3)	# 76-78	 **attackbox here**
    RefreshMultihit()
    GFX_0('mgef_406_blast', 0)
    Unknown2063()
    Unknown11044(1)
    Unknown30088(1)
    sprite('mg406_08', 3)	# 79-81	 **attackbox here**
    sprite('mg406_09', 3)	# 82-84	 **attackbox here**
    sprite('mg406_10', 3)	# 85-87	 **attackbox here**
    Unknown2001()
    Unknown23029(3, 2011, 0)
    sprite('mg406_08', 3)	# 88-90	 **attackbox here**
    sprite('mg406_09', 3)	# 91-93	 **attackbox here**
    sprite('mg406_10', 3)	# 94-96	 **attackbox here**
    sprite('mg406_08', 3)	# 97-99	 **attackbox here**
    sprite('mg406_09', 3)	# 100-102	 **attackbox here**
    sprite('mg406_10', 3)	# 103-105	 **attackbox here**
    sprite('mg406_08', 3)	# 106-108	 **attackbox here**
    sprite('mg406_09', 3)	# 109-111	 **attackbox here**
    sprite('mg406_10', 3)	# 112-114	 **attackbox here**
    sprite('keep', 32767)	# 115-32881
    enterState('PersonaDeleteAndIdling')

@State
def charge_se():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 6)	# 1-6
    SFX_3('electric_m')
    gotoLabel(0)

@State
def mgef_406_charge():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4054(14)
        Unknown23067('mgef_406charge_bk')
        Unknown1007(40000)
        sendToLabelUpon(32, 10)
    sprite('null', 4)	# 1-4
    Unknown4045('6d6765665f34303663686172676500000000000000000000000000000000000064000000')
    label(0)
    sprite('null', 4)	# 5-8
    Unknown4045('6d6765665f34303663686172676530340000000000000000000000000000000064000000')
    gotoLabel(0)
    label(10)
    Unknown1007(20000)
    teleportRelativeX(-66000)
    label(11)
    sprite('null', 4)	# 9-12
    Unknown4045('6d6765665f34303663686172676530330000000000000000000000000000000064000000')
    gotoLabel(11)

@State
def mgef_406_throw():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown1007(-100000)
    sprite('null', 4)	# 1-4
    Unknown4054(12)
    Unknown4045('6d6765665f3430367468726f770000000000000000000000000000000000000064000000')

@State
def mgef_406_blast():

    def upon_IMMEDIATE():
        Unknown4010(2)
        teleportRelativeY(0)
        Unknown1096(1500)
    sprite('null', 60)	# 1-60
    SFX_3('thunder_s')
    SFX_3('damage_magic_mh')
    SFX_3('bomb_m')
    Unknown23067('mgef_406blast')
    Unknown26('charge_se')

@State
def PAD_Persona5C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000000350c000000000000000000')
        callSubroutine('PAD_AttackInit')
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(10)
        AirPushbackX(2500)
        PushbackX(19800)
        AirUntechableTime(24)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PAD_CheckWarp')
        Unknown23059(1)
    sprite('mg204_50', 4)	# 1-4
    if (SLOT_25 < 295000):
        Unknown1000(1865000)
        teleportRelativeX(-295000)
    Unknown2006()
    sprite('mg204_51', 3)	# 5-7
    sprite('mg204_52', 1)	# 8-8
    sprite('mg204_53', 1)	# 9-9
    sprite('mg204_55', 1)	# 10-10	 **attackbox here**
    SFX_3('slash_blade_fast')
    GFX_0('mgef_204_zanzou', 100)
    RefreshMultihit()
    sprite('mg204_55', 1)	# 11-11	 **attackbox here**
    Unknown23022(0)
    sprite('mg204_56', 4)	# 12-15
    DisableAttackRestOfMove()
    Unknown23029(3, 2012, 0)
    sprite('mg204_55', 4)	# 16-19	 **attackbox here**
    sprite('mg204_56', 4)	# 20-23
    SFX_3('cloth_l')
    sprite('mg204_55', 4)	# 24-27	 **attackbox here**
    sprite('mg204_56', 4)	# 28-31
    sprite('mg204_55', 4)	# 32-35	 **attackbox here**
    sprite('keep', 32767)	# 36-32802
    enterState('PersonaDeleteAndIdling')

@State
def PAD_Persona5CC():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PAD_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        AttackP1(90)
        Hitstop(10)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(-200000)
        PushbackX(-8000)
        AirUntechableTime(40)
        Unknown9190(1)
        Unknown9118(11)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        DisableAttackRestOfMove()
        Unknown23078(1)
        Unknown23059(1)

        def upon_11():
            SFX_3('damage_hit_h')
    sprite('mg204_00', 2)	# 1-2
    SFX_3('hit_h_fast')
    sprite('mg204_01', 2)	# 3-4
    sprite('mg204_02', 6)	# 5-10
    sprite('mg204_03', 2)	# 11-12
    Unknown1045(10000)
    SFX_3('slash_blade_middle')
    sprite('mg204_04', 2)	# 13-14
    sprite('mg204_05ex01', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('mg204_06', 6)	# 18-23
    Unknown23029(3, 2013, 0)
    sprite('mg204_06ex1', 6)	# 24-29
    sprite('mg204_06ex2', 6)	# 30-35
    sprite('mg204_06', 6)	# 36-41
    sprite('mg204_06ex1', 6)	# 42-47
    sprite('mg204_06ex2', 6)	# 48-53
    sprite('keep', 32767)	# 54-32820
    Unknown2004(0, 0)
    enterState('PersonaDeleteAndIdling')

@State
def PAD_Persona5CCC():

    def upon_IMMEDIATE():
        Unknown23023()
        callSubroutine('PAD_AttackInit')
        Unknown2006()
        AttackLevel_(4)
        AttackP1(90)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(6000)
        AirPushbackY(-40000)
        PushbackX(19800)
        AirUntechableTime(40)
        Unknown9310(10)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        DisableAttackRestOfMove()
        Unknown23078(1)
        Unknown23059(1)
        Unknown2004(1, 0)

        def upon_11():
            SFX_3('damage_hit_mh')
    sprite('mg204_06', 3)	# 1-3
    sprite('mg204_07', 3)	# 4-6
    sprite('mg204_08', 3)	# 7-9
    sprite('mg204_09', 9)	# 10-18
    SFX_3('hit_l_middle')
    sprite('mg204_10', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    ScreenShake(10000, 30000)
    sprite('mg204_11', 6)	# 22-27
    Unknown23029(3, 2014, 0)
    sprite('mg204_12', 6)	# 28-33
    sprite('mg204_13', 6)	# 34-39
    sprite('mg204_11', 6)	# 40-45
    sprite('keep', 32767)	# 46-32812
    Unknown2004(0, 0)
    enterState('PersonaDeleteAndIdling')

@State
def mgef_204_zanzou():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown3033()
        Unknown4061(3)
        Unknown23015(13)
    sprite('vr_mg204_00', 30)	# 1-30
    Unknown3001(255)
    Unknown3004(-25)
    GFX_1('mgef_204', 0)

@State
def PAD_PersonaJC():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a08601006079feff00000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        AttackLevel_(4)
        AirPushbackY(-32000)
        AirPushbackX(26000)
        AirUntechableTime(29)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        DisableAttackRestOfMove()
        Unknown23078(1)
        callSubroutine('PAD_CheckWarp')
        EnableCollision(0)
        Unknown2053(1)
        Unknown4007(3)
        Unknown23059(1)

        def upon_43():
            if (SLOT_48 == 9001):
                sendToLabel(580)
            if (SLOT_48 == 9002):
                sendToLabel(580)
    sprite('mg253_00', 2)	# 1-2
    sprite('mg253_01', 2)	# 3-4
    sprite('mg253_02', 2)	# 5-6
    sprite('mg253_03', 3)	# 7-9
    SFX_3('slash_rapier_middle')
    SFX_3('slash_rapier_middle')
    GFX_0('mgef_253', 100)
    sprite('mg253_04', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('mg253_04', 2)	# 11-12	 **attackbox here**
    Unknown23022(0)
    sprite('mg253_05', 6)	# 13-18
    sprite('mg253_06', 6)	# 19-24
    sprite('mg253_07', 6)	# 25-30
    if SLOT_2:
        _gotolabel(0)
    sprite('mg253_05', 6)	# 31-36
    sprite('mg253_06', 6)	# 37-42
    sprite('mg253_07', 6)	# 43-48
    label(580)
    sprite('keep', 32767)	# 49-32815
    enterState('PersonaDeleteAndIdling')

@State
def mgef_253():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3033()
        Unknown4061(3)
    sprite('vr_mg253_00', 3)	# 1-3
    sprite('vr_mg253_01', 15)	# 4-18
    Unknown3001(255)
    Unknown3004(-25)

@State
def PAD_PersonaJ2C():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100b03cffff00000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        AttackLevel_(4)
        Damage(1000)
        AirUntechableTime(25)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(13000)
        AirPushbackY(48000)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        Unknown11044(1)
        DisableAttackRestOfMove()
        callSubroutine('PAD_CheckWarp')
        Unknown23059(1)
        EnableCollision(0)
        Unknown2053(1)
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            Unknown23022(1)
            Unknown1017()
            Unknown1022()
            sendToLabel(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('mg232_00', 1)	# 1-1
    if (SLOT_25 < 205000):
        Unknown1000(1865000)
        teleportRelativeX(-205000)
    sprite('mg232_01', 1)	# 2-2
    sprite('mg232_02', 1)	# 3-3
    sprite('mg232_03', 3)	# 4-6
    GFX_0('mgef_232', 0)
    sprite('mg232_04', 1)	# 7-7	 **attackbox here**
    SFX_3('slash_pole_middle')
    SFX_3('airdash_m')
    GFX_0('mgef232_ground', 100)
    Unknown3029(1)
    physicsXImpulse(60000)
    physicsYImpulse(48000)
    RefreshMultihit()
    sprite('mg232_04', 2)	# 8-9	 **attackbox here**
    Unknown23022(0)
    sprite('mg232_05', 3)	# 10-12	 **attackbox here**
    sprite('mg232_06', 3)	# 13-15	 **attackbox here**
    SFX_3('airdash_m')
    sprite('mg232_04', 3)	# 16-18	 **attackbox here**
    SFX_3('airdash_m')
    Unknown1019(50)
    YAccel(50)
    EnableCollision(0)
    Unknown3029(0)
    DisableAttackRestOfMove()
    sprite('mg232_05', 3)	# 19-21	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(50)
    YAccel(50)
    sprite('mg232_06', 3)	# 22-24	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    sprite('mg232_04', 6)	# 25-30	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(0)
    YAccel(0)
    sprite('mg232_05', 6)	# 31-36	 **attackbox here**
    sprite('mg232_06', 6)	# 37-42	 **attackbox here**
    SFX_3('cloth_m')
    sprite('keep', 32767)	# 43-32809
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32810-65576
    enterState('PAD_PersonaJ2CGrip')

@State
def PAD_PersonaJ2CGrip():

    def upon_IMMEDIATE():
        callSubroutine('PAD_AttackInit')
        Unknown17011('PAD_PersonaJ2CExe', 1, 1, 0)
        Unknown2006()
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        DisableAttackRestOfMove()
        Unknown30031(0)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 2017, 0)
        Unknown23078(1)
        Unknown23059(1)
        Unknown2053(1)
        Unknown23022(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('keep', 3)	# 1-3
    RefreshMultihit()
    sprite('mg232_04', 3)	# 4-6	 **attackbox here**
    SFX_3('airdash_m')
    Unknown1019(50)
    YAccel(50)
    EnableCollision(0)
    Unknown3029(0)
    DisableAttackRestOfMove()
    sprite('mg232_05', 3)	# 7-9	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(50)
    YAccel(50)
    sprite('mg232_06', 3)	# 10-12	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    sprite('mg232_04', 6)	# 13-18	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(0)
    YAccel(0)
    sprite('mg232_05', 6)	# 19-24	 **attackbox here**
    sprite('mg232_06', 6)	# 25-30	 **attackbox here**
    SFX_3('cloth_m')
    sprite('keep', 32767)	# 31-32797
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaJ2CExe():

    def upon_IMMEDIATE():
        callSubroutine('PAD_AttackInit')
        Unknown17012(1, 1, 0)
        Unknown2006()
        Unknown30031(0)
        AttackLevel_(5)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(0)
        Unknown9310(1)
        Unknown11072(1, 200000, 1000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-30000)
        Hitstop(6)
        DisableAttackRestOfMove()
        Unknown2034(1)
        Unknown23022(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
        sendToLabelUpon(2, 0)
    sprite('mg232_04', 2)	# 1-2	 **attackbox here**
    SFX_3('grip_hugs')
    SFX_3('bound_marble_m')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1018()
    Unknown1023()
    sprite('mg232_05', 2)	# 3-4	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    YAccel(75)
    Unknown1019(75)
    setGravity(2400)
    sprite('mg232_06', 2)	# 5-6	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(80)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23015(0)
    Unknown2018(1, 80)
    Unknown2019(100)
    sprite('mg232_04', 2)	# 7-8	 **attackbox here**
    Unknown1019(80)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_07', 3)	# 9-11
    SFX_3('cloth_m')
    Unknown1019(80)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_08', 3)	# 12-14
    Unknown1019(80)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    label(1)
    sprite('mg232_09', 3)	# 15-17
    SFX_3('cloth_m')

    def upon_4():
        clearUponHandler(4)
        sendToLabel(2)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_10', 3)	# 18-20
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    gotoLabel(1)
    label(2)
    sprite('keep', 3)	# 21-23
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_11', 5)	# 24-28
    SFX_3('cloth_m')
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_12', 5)	# 29-33
    Unknown5000(4, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_13', 32767)	# 34-32800
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown2018(1, 80)
    Unknown2019(1000)
    label(0)
    sprite('mg232_14', 5)	# 32801-32805	 **attackbox here**
    SFX_3('damage_hit_mh')
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    ScreenShake(10000, 30000)
    Unknown1084(1)
    Unknown2034(0)
    RefreshMultihit()
    sprite('mg232_15', 3)	# 32806-32808
    Unknown23029(3, 2018, 0)
    SLOT_10 = 0
    sprite('mg232_16', 3)	# 32809-32811
    sprite('mg232_17', 3)	# 32812-32814
    sprite('mg232_18', 3)	# 32815-32817
    sprite('mg232_16', 3)	# 32818-32820
    sprite('keep', 32767)	# 32821-65587
    enterState('PersonaDeleteAndIdling')

@State
def mgef_232():

    def upon_IMMEDIATE():
        Unknown1007(128000)
    sprite('null', 30)	# 1-30
    GFX_0('mgef_232_ripper', 100)
    GFX_0('mgef_232_ripper', 100)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown1007(50000)
    Unknown35()
    GFX_0('mgef_232_ripper', 100)
    Unknown36(1)
    teleportRelativeX(0)
    Unknown1007(-50000)
    Unknown35()
    Unknown4048(-40000)
    Unknown4054(14)
    Unknown4045('6d6765665f3233327269707065725f647573740000000000000000000000000064000000')

@State
def mgef_232_ripper():

    def upon_IMMEDIATE():
        Unknown4011(2)
    sprite('null', 30)	# 1-30
    physicsXImpulse(60000)
    physicsYImpulse(40000)
    Unknown1108(0)
    Unknown4048(-40000)
    Unknown4054(14)
    Unknown23067('mgef_232ripper')

@State
def mgef232_ground():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3004(-12)
    sprite('null', 30)	# 1-30
    GFX_2('ef_bousou_ground01')

@State
def PAD_PersonaJ2CEx():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100b03cffff00000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        AttackLevel_(4)
        Damage(1000)
        AttackP2(75)
        Hitstop(6)
        AirUntechableTime(40)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(18000)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        DisableAttackRestOfMove()
        callSubroutine('PAD_CheckWarp')
        Unknown23059(1)
        EnableCollision(0)
        Unknown2053(1)

        def upon_78():
            clearUponHandler(78)
            Unknown1017()
            Unknown1022()
            sendToLabel(1)
    sprite('mg232_00', 1)	# 1-1
    if (SLOT_25 < 205000):
        Unknown1000(1865000)
        teleportRelativeX(-205000)
    sprite('mg232_01', 1)	# 2-2
    sprite('mg232_02', 1)	# 3-3
    sprite('mg232_03', 3)	# 4-6
    GFX_0('mgef_232', 0)
    sprite('mg232_04', 1)	# 7-7	 **attackbox here**
    SFX_3('slash_pole_middle')
    SFX_3('airdash_m')
    GFX_0('mgef232_ground', 100)
    Unknown3029(1)
    physicsXImpulse(60000)
    physicsYImpulse(48000)
    RefreshMultihit()
    sprite('mg232_04', 2)	# 8-9	 **attackbox here**
    Unknown23022(0)
    sprite('mg232_05', 3)	# 10-12	 **attackbox here**
    sprite('mg232_06', 3)	# 13-15	 **attackbox here**
    SFX_3('airdash_m')
    sprite('mg232_04', 3)	# 16-18	 **attackbox here**
    SFX_3('airdash_m')
    Unknown1019(50)
    YAccel(50)
    EnableCollision(0)
    Unknown3029(0)
    DisableAttackRestOfMove()
    sprite('mg232_05', 3)	# 19-21	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(50)
    YAccel(50)
    sprite('mg232_06', 3)	# 22-24	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    sprite('mg232_04', 6)	# 25-30	 **attackbox here**
    SFX_3('cloth_m')
    Unknown1019(0)
    YAccel(0)
    sprite('mg232_05', 6)	# 31-36	 **attackbox here**
    sprite('mg232_06', 6)	# 37-42	 **attackbox here**
    SFX_3('cloth_m')
    sprite('keep', 32767)	# 43-32809
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32810-65576
    enterState('PAD_PersonaJ2CExExe')

@State
def PAD_PersonaJ2CExExe():

    def upon_IMMEDIATE():
        callSubroutine('PAD_AttackInit')
        Unknown2006()
        Unknown11032('400d0300c0f2fcff400d0300c0f2fcff')
        AttackLevel_(4)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AttackP1(60)
        AttackP2(100)
        Unknown11058('0100000000000000000000000000000000000000')
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(20000)
        AirPushbackY(-40000)
        AirUntechableTime(40)
        Unknown9016(1)
        DisableAttackRestOfMove()
        EnableCollision(0)
        Unknown2034(1)

        def upon_11():
            clearUponHandler(11)
            clearUponHandler(2)
            SFX_3('damage_hit_mh')
            Unknown1019(-5)
            YAccel(-5)
            setGravity(0)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(11)
            Unknown1084(1)
            ScreenShake(10000, 30000)
            sendToLabel(0)
    sprite('mg232_05', 3)	# 1-3	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown1018()
    Unknown1023()
    Unknown1019(30)
    YAccel(50)
    sprite('mg232_06', 3)	# 4-6	 **attackbox here**
    sprite('mg232_07', 3)	# 7-9
    SFX_3('cloth_m')
    Unknown1019(30)
    YAccel(75)
    setGravity(1500)
    sprite('mg232_08', 3)	# 10-12
    sprite('mg232_11', 3)	# 13-15
    SFX_3('cloth_m')
    sprite('mg232_12', 3)	# 16-18
    sprite('mg232_13', 3)	# 19-21
    sprite('mg232_14', 5)	# 22-26	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(40000)
    physicsYImpulse(-40000)
    sprite('mg232_15', 60)	# 27-86
    label(0)
    sprite('mg232_16', 6)	# 87-92
    sprite('mg232_17', 6)	# 93-98
    Unknown1084(1)
    sprite('mg232_18', 6)	# 99-104
    sprite('mg232_16', 6)	# 105-110
    sprite('keep', 32767)	# 111-32877
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaCA():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('03000000640000006079feff0000000000000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        Unknown2006()
        DisableAttackRestOfMove()
        callSubroutine('PAD_ForceWarp')
        Unknown23059(1)
        Unknown23022(1)
    sprite('mg204_50', 2)	# 1-2
    sprite('mg204_51', 2)	# 3-4
    sprite('mg204_52', 2)	# 5-6
    sprite('mg204_53', 1)	# 7-7
    sprite('mg204_55', 3)	# 8-10	 **attackbox here**
    SFX_3('slash_blade_fast')
    GFX_0('mgef_204_zanzou', 100)
    sprite('mg204_56', 4)	# 11-14
    DisableAttackRestOfMove()
    Unknown23029(3, 2012, 0)
    sprite('mg204_55', 4)	# 15-18	 **attackbox here**
    sprite('mg204_56', 4)	# 19-22
    SFX_3('cloth_l')
    sprite('mg204_55', 4)	# 23-26	 **attackbox here**
    sprite('mg204_56', 4)	# 27-30
    sprite('mg204_55', 4)	# 31-34	 **attackbox here**
    sprite('mg204_56', 4)	# 35-38
    sprite('mg204_55', 4)	# 39-42	 **attackbox here**
    sprite('mg204_56', 4)	# 43-46
    sprite('mg204_55', 4)	# 47-50	 **attackbox here**
    sprite('mg204_56', 4)	# 51-54
    sprite('keep', 32767)	# 55-32821
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaSpecialFastShot():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000080841e00')
        callSubroutine('PAD_SPAttackInit')
        Unknown2006()
        DisableAttackRestOfMove()
        callSubroutine('PAD_ForceWarp')
        EnableCollision(0)
        Unknown2053(1)
        Unknown4007(3)

        def upon_14():
            Unknown21012('556c74696d6174654c617365724a697a6f6b750000000000000000000000000020000000')
            Unknown21012('437265617465556c74696d6174654c617365724d61746f6d650000000000000020000000')
            Unknown21012('437265617465556c74696d6174654c617365723030000000000000000000000020000000')
            Unknown21012('437265617465556c74696d6174654c617365723031000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726500000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726531000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726532000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726533000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726534000000000000000000000000000000000020000000')
            Unknown21012('6d6765665f6a696f64696e6574616d650000000000000000000000000000000020000000')
            Unknown21012('6d6765665f67696f64696e6573686f636b00000000000000000000000000000020000000')
    sprite('mg205_00', 2)	# 1-2
    GFX_0('mgef_jiodinetame', 0)
    Unknown4007(0)
    sprite('mg205_01', 2)	# 3-4
    sprite('mg205_02', 2)	# 5-6
    sprite('mg205_03', 3)	# 7-9
    SFX_3('ad000')
    sprite('mg205_06', 2)	# 10-11
    sprite('mg205_07', 2)	# 12-13
    sprite('mg205_08', 3)	# 14-16
    Unknown26('mgef_jiodinetame')
    Unknown26('rotationSphere1')
    Unknown26('rotationSphere2')
    Unknown26('rotationSphere3')
    Unknown26('rotationSphere4')
    Unknown26('CreateUltimateLaser02')
    Unknown26('CreateUltimateLaser03')
    Unknown26('CreateUltimateLaser01')
    GFX_0('UltimateLaserJizoku', 0)
    GFX_0('mgef_giodineshock', 0)
    GFX_0('Persona5D_Atk', 100)
    Unknown23029(1, 3021, 0)
    sprite('mg205_09', 3)	# 17-19
    SFX_3('ad001')
    sprite('mg205_10', 3)	# 20-22
    sprite('mg205_08', 4)	# 23-26
    Unknown21012('556c74696d6174654c617365724a697a6f6b750000000000000000000000000020000000')
    Unknown21012('437265617465556c74696d6174654c617365724d61746f6d650000000000000020000000')
    Unknown21012('437265617465556c74696d6174654c617365723030000000000000000000000020000000')
    Unknown21012('726f746174696f6e53706865726500000000000000000000000000000000000020000000')
    Unknown21012('6d6765665f67696f64696e6573686f636b00000000000000000000000000000020000000')
    sprite('mg205_09', 4)	# 27-30
    sprite('mg205_10', 4)	# 31-34
    sprite('mg205_08', 4)	# 35-38
    sprite('mg205_09', 4)	# 39-42
    sprite('mg205_10', 4)	# 43-46
    sprite('mg205_08', 5)	# 47-51
    sprite('mg205_09', 5)	# 52-56
    sprite('mg205_10', 5)	# 57-61
    sprite('mg205_08', 5)	# 62-66
    sprite('mg205_09', 5)	# 67-71
    sprite('mg205_10', 5)	# 72-76
    sprite('keep', 32767)	# 77-32843
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaSpecialSlowShot():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000080841e00')
        callSubroutine('PAD_SPAttackInit')
        Unknown2006()
        DisableAttackRestOfMove()
        callSubroutine('PAD_ForceWarp')
        EnableCollision(0)
        Unknown2053(1)
        Unknown4007(3)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0

        def upon_14():
            Unknown21012('556c74696d6174654c617365724a697a6f6b750000000000000000000000000020000000')
            Unknown21012('437265617465556c74696d6174654c617365724d61746f6d650000000000000020000000')
            Unknown21012('437265617465556c74696d6174654c617365723030000000000000000000000020000000')
            Unknown21012('437265617465556c74696d6174654c617365723031000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726500000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726531000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726532000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726533000000000000000000000000000000000020000000')
            Unknown21012('726f746174696f6e53706865726534000000000000000000000000000000000020000000')
            Unknown21012('6d6765665f6a696f64696e6574616d650000000000000000000000000000000020000000')
            Unknown21012('6d6765665f67696f64696e6573686f636b00000000000000000000000000000020000000')
    sprite('mg205_00', 4)	# 1-4
    GFX_0('CreateUltimateLaserMatome', 0)
    Unknown4007(0)
    sprite('mg205_01', 4)	# 5-8
    GFX_0('mgef_jiodinetame', 0)
    sprite('mg205_02', 4)	# 9-12
    sprite('mg205_03', 3)	# 13-15
    SFX_3('ad000')
    sprite('mg205_04', 3)	# 16-18
    sprite('mg205_05', 3)	# 19-21
    sprite('mg205_03', 3)	# 22-24
    sprite('mg205_04', 3)	# 25-27
    sprite('mg205_05', 3)	# 28-30
    sprite('mg205_03', 3)	# 31-33
    SFX_3('ad000')
    sprite('mg205_04', 3)	# 34-36
    sprite('mg205_05', 3)	# 37-39
    sprite('mg205_03', 3)	# 40-42
    sprite('mg205_04', 3)	# 43-45
    sprite('mg205_06', 3)	# 46-48
    sprite('mg205_07', 3)	# 49-51
    sprite('mg205_08', 3)	# 52-54
    Unknown26('mgef_jiodinetame')
    Unknown26('rotationSphere1')
    Unknown26('rotationSphere2')
    Unknown26('rotationSphere3')
    Unknown26('rotationSphere4')
    Unknown26('CreateUltimateLaser02')
    Unknown26('CreateUltimateLaser03')
    Unknown26('CreateUltimateLaser01')
    GFX_0('UltimateLaserJizoku', 0)
    GFX_0('mgef_giodineshock', 0)
    GFX_0('Persona5D_Atk', 100)
    Unknown23029(1, 3022, 0)
    sprite('mg205_09', 3)	# 55-57
    sprite('mg205_10', 3)	# 58-60
    sprite('mg205_08', 3)	# 61-63
    SFX_3('ad001')
    sprite('mg205_09', 3)	# 64-66
    sprite('mg205_10', 3)	# 67-69
    sprite('mg205_08', 3)	# 70-72
    sprite('mg205_09', 3)	# 73-75
    sprite('mg205_10', 3)	# 76-78
    sprite('mg205_08', 3)	# 79-81
    SFX_3('ad001')
    sprite('mg205_09', 3)	# 82-84
    sprite('mg205_10', 3)	# 85-87
    sprite('mg205_08', 3)	# 88-90
    sprite('mg205_09', 3)	# 91-93
    sprite('mg205_10', 3)	# 94-96
    sprite('mg205_08', 3)	# 97-99
    SFX_3('ad001')
    sprite('mg205_09', 3)	# 100-102
    sprite('mg205_10', 3)	# 103-105
    sprite('mg205_08', 3)	# 106-108
    sprite('mg205_09', 3)	# 109-111
    sprite('mg205_10', 3)	# 112-114
    sprite('mg205_08', 3)	# 115-117
    SFX_3('ad001')
    sprite('mg205_08', 4)	# 118-121
    sprite('mg205_09', 4)	# 122-125
    sprite('mg205_10', 4)	# 126-129
    sprite('mg205_08', 4)	# 130-133
    sprite('mg205_09', 4)	# 134-137
    sprite('mg205_10', 4)	# 138-141
    sprite('mg205_08', 5)	# 142-146
    sprite('mg205_09', 5)	# 147-151
    sprite('mg205_10', 5)	# 152-156
    sprite('mg205_08', 5)	# 157-161
    sprite('mg205_09', 5)	# 162-166
    sprite('mg205_10', 5)	# 167-171
    sprite('keep', 32767)	# 172-32938
    enterState('PersonaDeleteAndIdling')

@State
def UltimateLaserJizoku():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(32)
        Unknown4003('6d6765665f6a696f64696e655f6a697a6f6b752e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 10)	# 1-10
    Unknown3004(32)
    sprite('null', 60)	# 11-70
    sprite('null', 10)	# 71-80
    Unknown3004(-25)
    ExitState()
    label(580)
    sprite('null', 16)	# 81-96
    Unknown3004(-16)

@State
def CreateUltimateLaserMatome():

    def upon_IMMEDIATE():
        callSubroutine('KowarePreset')
    sprite('null', 35)	# 1-35
    GFX_0('rotationSphere', 0)
    sprite('null', 5)	# 36-40
    GFX_0('CreateUltimateLaser00', 100)
    sprite('null', 2)	# 41-42
    GFX_0('CreateUltimateLaser01', 100)
    sprite('null', 2)	# 43-44
    GFX_0('CreateUltimateLaser02', 100)
    sprite('null', 2)	# 45-46
    GFX_0('CreateUltimateLaser03', 100)
    sprite('null', 2)	# 47-48
    GFX_0('CreateUltimateLaser02', 100)
    sprite('null', 70)	# 49-118
    GFX_0('CreateUltimateLaser03', 100)
    sprite('null', 1)	# 119-119
    Unknown21012('437265617465556c74696d6174654c617365723032000000000000000000000021000000')
    Unknown21012('437265617465556c74696d6174654c617365723033000000000000000000000021000000')
    ExitState()
    label(580)
    sprite('null', 16)	# 120-135
    Unknown3032()
    Unknown3004(-16)
    Unknown21012('437265617465556c74696d6174654c617365723032000000000000000000000021000000')
    Unknown21012('437265617465556c74696d6174654c617365723033000000000000000000000021000000')

@State
def rotationSphere():

    def upon_IMMEDIATE():
        callSubroutine('KowarePreset')
    sprite('null', 10)	# 1-10
    GFX_0('rotationSphere1', 0)
    sprite('null', 10)	# 11-20
    GFX_0('rotationSphere2', 0)
    sprite('null', 10)	# 21-30
    GFX_0('rotationSphere3', 0)
    sprite('null', 10)	# 31-40
    GFX_0('rotationSphere4', 0)
    sprite('null', 40)	# 41-80
    ExitState()
    label(580)
    sprite('null', 16)	# 81-96
    Unknown3032()
    Unknown3004(-16)

@State
def rotationSphere1():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f74616d6161726f756e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 40)	# 1-40
    sprite('null', 10)	# 41-50
    Unknown3004(-25)
    ExitState()
    label(580)
    sprite('null', 16)	# 51-66
    Unknown3032()
    Unknown3004(-16)

@State
def rotationSphere2():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f74616d6161726f756e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 30)	# 1-30
    sprite('null', 10)	# 31-40
    Unknown3004(-25)
    ExitState()
    label(580)
    sprite('null', 16)	# 41-56
    Unknown3032()
    Unknown3004(-16)

@State
def rotationSphere3():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f74616d6161726f756e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 20)	# 1-20
    sprite('null', 10)	# 21-30
    Unknown3004(-25)
    ExitState()
    label(580)
    sprite('null', 16)	# 31-46
    Unknown3032()
    Unknown3004(-16)

@State
def rotationSphere4():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f74616d6161726f756e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 10)	# 1-10
    sprite('null', 10)	# 11-20
    Unknown3004(-25)
    ExitState()
    label(580)
    sprite('null', 16)	# 21-36
    Unknown3032()
    Unknown3004(-16)

@State
def CreateUltimateLaser00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown3001(0)
        Unknown4003('6d6765665f6a696f64696e655f737461727430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 10)	# 1-10
    Unknown3004(26)
    sprite('null', 60)	# 11-70
    sprite('null', 20)	# 71-90
    Unknown3004(-12)
    ExitState()
    label(580)
    sprite('null', 16)	# 91-106
    Unknown3004(-16)

@State
def CreateUltimateLaser01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6d6765665f6a696f64696e655f737461727430312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
    sprite('null', 42)	# 1-42
    ExitState()
    label(580)
    sprite('null', 16)	# 43-58
    Unknown3004(-16)

@State
def CreateUltimateLaser02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1011(0, 100000)
        Unknown1070(400, 1000)
        Unknown1062(800, 1000)
        Unknown4003('6d6765665f6a696f64696e655f737461727430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
        sendToLabelUpon(33, 1)
    label(0)
    sprite('null', 5)	# 1-5
    Unknown3001(255)
    sprite('null', 5)	# 6-10
    Unknown3001(0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)	# 11-11
    ExitState()
    label(580)
    sprite('null', 16)	# 12-27
    Unknown3004(-16)

@State
def CreateUltimateLaser03():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1011(-100000, 0)
        Unknown1070(400, 1000)
        Unknown1062(800, 1000)
        Unknown4003('6d6765665f6a696f64696e655f737461727430322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        callSubroutine('KowarePreset')
        sendToLabelUpon(33, 1)
    label(0)
    sprite('null', 5)	# 1-5
    Unknown3001(255)
    sprite('null', 5)	# 6-10
    Unknown3001(0)
    gotoLabel(0)
    label(1)
    sprite('null', 1)	# 11-11
    ExitState()
    label(580)
    sprite('null', 16)	# 12-27
    Unknown3004(-16)

@State
def mgef_jiodinetame():

    def upon_IMMEDIATE():
        callSubroutine('KowarePreset')
    sprite('null', 60)	# 1-60
    GFX_2('mgef_jiodinetame')
    ExitState()
    label(580)
    sprite('null', 16)	# 61-76
    Unknown3032()
    Unknown3004(-16)

@State
def mgef_giodineshock():

    def upon_IMMEDIATE():
        callSubroutine('KowarePreset')
    sprite('null', 60)	# 1-60
    GFX_2('mgef_giodineshock')
    ExitState()
    label(580)
    sprite('null', 16)	# 61-76
    Unknown3032()
    Unknown3004(-16)

@State
def Persona5D_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(2)
        Unknown4007(2)
        Damage(200)
        Unknown11092(1)
        AirUntechableTime(47)
        Unknown9178(1)
        WallbounceReboundTime(0)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(100000)
        AirPushbackY(1000)
        Unknown30056('d0fb01003c0000003c000000')
        YImpluseBeforeWallbounce(0)
        PushbackX(8000)
        Unknown9021(1)
        Unknown9266(3)
        Unknown11057(800)
        Unknown2037(24)

        def upon_ON_HIT_OR_BLOCK():
            if SLOT_51:
                SLOT_51 = 0
            else:
                SLOT_51 = 1

        def upon_43():
            if (SLOT_48 == 3021):
                AttackLevel_(3)
                Damage(600)
                AttackP2(80)
                Unknown2037(6)
            if (SLOT_48 == 3022):
                AttackLevel_(4)
                Damage(200)
                AttackP2(75)
                Unknown2037(24)
                Unknown9362(1)
                Unknown9364(40)
                PushbackX(19800)
    sprite('null', 1)	# 1-1
    label(1)
    sprite('dmy_Persona5D_Atk', 3)	# 2-4
    RefreshMultihit()
    Unknown2038(-1)
    if (not (SLOT_2 <= 0)):
        gotoLabel(1)

@State
def PAD_PersonaSpecialSearchShot():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('16000000640000006079feff40420f0000000000000000000000000000000000')
        callSubroutine('PAD_SPAttackInit')
        callSubroutine('ExSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(3000)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(12, 12, 12)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(-200000)
        PushbackX(6000)
        Unknown9190(1)
        Unknown9118(15)
        Unknown9016(1)
        Unknown9266(3)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        DisableAttackRestOfMove()
        callSubroutine('PAD_ForceWarp')
        EnableCollision(0)
        Unknown2053(1)
        Unknown23022(1)

        def upon_14():
            Unknown21012('6a756d6f6e6a69426967736c617368546174650000000000000000000000000020000000')
            Unknown21012('6a756d6f6e6a69426967736c617368536f636b3030000000000000000000000020000000')
            Unknown21012('6a756d6f6e6a69426967736c617368536f636b3031000000000000000000000020000000')

        def upon_LANDING():
            sendToLabel(0)
    sprite('mg233_00', 1)	# 1-1
    Unknown3032()
    Unknown3001(0)
    Unknown3029(1)
    sprite('mg233_01', 2)	# 2-3
    Unknown3004(65)
    SFX_3('persona_destroy')
    sprite('mg233_02', 2)	# 4-5
    sprite('mg233_03', 2)	# 6-7
    sprite('mg233_04', 2)	# 8-9
    sprite('mg233_05', 2)	# 10-11
    physicsYImpulse(-5000)
    sprite('mg233_06', 2)	# 12-13
    sprite('mg233_07', 32767)	# 14-32780
    physicsYImpulse(-200000)
    GFX_0('jumonjiBigslashTate', 104)
    label(0)
    sprite('mg233_08', 2)	# 32781-32782
    Unknown1084(1)
    Unknown3029(0)
    ScreenShake(20000, 0)
    SFX_3('ad002')
    sprite('mg233_09', 3)	# 32783-32785	 **attackbox here**
    GFX_0('jumonjiBigslashSock00', 1)
    RefreshMultihit()
    Unknown23022(0)
    sprite('mg233_10', 5)	# 32786-32790	 **attackbox here**
    GFX_0('jumonjiBigslashSock01', 100)
    SFX_3('thunder_l')
    sprite('mg233_11', 5)	# 32791-32795
    Unknown23029(3, 3511, 0)
    sprite('mg233_12', 5)	# 32796-32800
    sprite('mg233_13', 5)	# 32801-32805
    sprite('mg233_14', 5)	# 32806-32810
    sprite('mg233_15', 10)	# 32811-32820
    sprite('mg233_15', 20)	# 32821-32840
    sprite('keep', 32767)	# 32841-65607
    enterState('PersonaDeleteAndIdling')

@State
def jumonjiBigslashTate():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown1072(90000)
        teleportRelativeX(65000)
        Unknown1064(0)
        Unknown3001(0)
        callSubroutine('KowarePreset')
    sprite('null', 20)	# 1-20
    Unknown3004(12)
    Unknown1067(65)
    sprite('null', 15)	# 21-35
    Unknown1067(0)
    sprite('null', 10)	# 36-45
    Unknown1067(-80)
    Unknown3004(-26)
    ExitState()
    label(580)
    sprite('null', 16)	# 46-61
    Unknown3004(-16)

@State
def jumonjiBigslashSock00():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown1064(925)
        Unknown1056(700)
        Unknown3001(150)
        callSubroutine('KowarePreset')
    sprite('null', 10)	# 1-10
    GFX_0('jumonji_ground', 100)
    sprite('null', 10)	# 11-20
    Unknown3004(-26)
    ExitState()
    label(580)
    sprite('null', 16)	# 21-36
    Unknown3004(-16)

@State
def jumonji_ground():

    def upon_IMMEDIATE():
        teleportRelativeX(65000)
        GFX_2('mgef_jumonji')
    sprite('null', 8)	# 1-8
    GFX_1('mgef_jumonji_sub', 100)
    sprite('null', 8)	# 9-16
    GFX_1('mgef_jumonji_sub', 100)
    sprite('null', 8)	# 17-24
    GFX_1('mgef_jumonji_sub', 100)
    sprite('null', 8)	# 25-32
    GFX_1('mgef_jumonji_sub', 100)
    Unknown3004(-16)
    sprite('null', 8)	# 33-40
    GFX_1('mgef_jumonji_sub', 100)

@State
def jumonjiBigslashSock01():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown1064(925)
        Unknown1056(700)
        Unknown3001(255)
        callSubroutine('KowarePreset')
    sprite('null', 15)	# 1-15
    sprite('null', 20)	# 16-35
    Unknown1059(20)
    Unknown3004(-12)
    ExitState()
    label(580)
    sprite('null', 16)	# 36-51
    Unknown3004(-16)

@State
def PAD_PersonaSpecialAntiAirFast():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PAD_SPAttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(1200)
        Hitstop(10)
        AttackP2(80)
        Unknown11092(1)
        Unknown11056(0)
        AirPushbackY(-40000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        AirUntechableTime(30)
        Unknown9310(1)
        Unknown9016(1)
        callSubroutine('PAD_ForceWarp')
        Unknown23078(1)
        EnableCollision(0)
        Unknown2053(1)
        Unknown23059(1)
        if Unknown23145('PAD_Persona5C'):
            teleportRelativeX(50000)
        if Unknown23145('PAD_Persona5CC'):
            teleportRelativeX(100000)
    sprite('mg432_00', 3)	# 1-3
    sprite('mg432_01', 3)	# 4-6
    sprite('mg432_02', 3)	# 7-9
    sprite('mg432_03', 3)	# 10-12
    teleportRelativeX(100000)
    SFX_3('hit_m_slow')
    sprite('mg432_04ex01', 3)	# 13-15	 **attackbox here**
    Unknown8000(0, 1, 1)
    ScreenShake(10000, 0)
    sprite('mg432_05', 3)	# 16-18
    sprite('mg432_06', 6)	# 19-24
    sprite('mg432_07', 2)	# 25-26
    sprite('mg432_08', 2)	# 27-28
    GFX_0('mgef_432', 0)
    sprite('mg432_09', 2)	# 29-30
    SFX_3('slash_blade_slow')
    SFX_3('blaze_long')
    sprite('mg432_10', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1800)
    Hitstop(0)
    Unknown11001(13, 13, 13)
    AirUntechableTime(55)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(15000)
    AirPushbackY(50000)
    Unknown11058('0000000000000000000000000100000000000000')
    Unknown11034(0)
    ProjectileDurabilityLvl(1)
    Unknown9311()
    Unknown11084(1)
    Unknown9021(1)
    Unknown9266(1)

    def upon_12():
        SLOT_31 = 1
        Unknown23029(3, 3017, 0)
    sprite('mg432_11', 4)	# 34-37
    GFX_0('vr_mg432_zanzou2', 100)
    Unknown23029(3, 3011, 0)
    sprite('mg432_12', 4)	# 38-41
    sprite('mg432_13', 4)	# 42-45
    sprite('mg432_14', 4)	# 46-49
    sprite('mg432_12', 4)	# 50-53
    sprite('mg432_13', 4)	# 54-57
    sprite('mg432_14', 4)	# 58-61
    sprite('mg432_12', 4)	# 62-65
    sprite('mg432_13', 4)	# 66-69
    sprite('mg432_14', 4)	# 70-73
    sprite('keep', 32767)	# 74-32840
    enterState('PersonaDeleteAndIdling')

@State
def mgef_432():

    def upon_IMMEDIATE():
        teleportRelativeX(32000)
    sprite('null', 2)	# 1-2
    sprite('null', 60)	# 3-62
    Unknown4049(1350)
    Unknown4045('6d6765665f34333261757261000000000000000000000000000000000000000064000000')

@State
def vr_mg432_zanzou2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown2019(-100)
        Unknown2054(1)
        Unknown21010(1)
    sprite('vr_mg432_11', 4)	# 1-4
    Unknown3001(255)
    Unknown3004(-63)

@Subroutine
def AntiAirSlowCreateAura():
    GFX_0('mgef_434_aura', 100)
    GFX_0('mgef_434_aura_bk', 103)
    GFX_0('mgef_434_aura_sub', 0)
    GFX_0('mgef_434_aura_sub', 1)
    GFX_0('mgef_434_aura_sub', 2)
    GFX_0('mgef_434_aura_sub', 3)
    GFX_0('mgef_434_aura_sub', 4)
    GFX_0('mgef_434_aura_sub', 5)
    GFX_0('mgef_434_aura_sub', 6)
    GFX_0('mgef_434_aura_sub', 7)
    GFX_0('mgef_434_aura_sub', 8)
    GFX_0('mgef_434_aura_sub', 9)
    GFX_0('mgef_434_aura_sub', 10)

@Subroutine
def AntiAirSlowDeleteAura():
    Unknown26('mgef_434_aura')
    Unknown26('mgef_434_aura_bk')
    Unknown26('mgef_434_aura_sub')

@Subroutine
def AntiAirSlowCreateTornado():
    GFX_0('mgef_434SE', 100)
    GFX_0('mgef_434_tornado', 100)

@Subroutine
def AntiAirSlowDeleteTornado():
    Unknown21012('6d6765665f34333453450000000000000000000000000000000000000000000020000000')
    Unknown21012('6d6765665f3433345f746f726e61646f0000000000000000000000000000000020000000')
    Unknown21012('6d6765665f3433345f746f726e61646f3200000000000000000000000000000020000000')
    Unknown21012('6d6765665f3433345f746f726e61646f3300000000000000000000000000000020000000')

@State
def PAD_PersonaSpecialAntiAirSlow():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000000000000000000000000000080841e000000000000000000')
        callSubroutine('PAD_SPAttackInit')
        Unknown2006()
        AttackLevel_(5)
        Damage(350)
        AttackP2(80)
        Unknown11092(1)
        AirPushbackX(500)
        Unknown30055('50c300005000000000000000')
        AirPushbackY(120000)
        YImpluseBeforeWallbounce(3000)
        AirUntechableTime(1000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9310(1)
        Unknown11057(600)
        Unknown11055(1)
        Unknown9021(1)
        Unknown11084(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(1)
        Unknown11058('0000000000000000000000000100000000000000')
        callSubroutine('PAD_ForceWarp')
        Unknown4009(3)
        Unknown2053(1)

        def upon_12():
            clearUponHandler(12)
            Unknown23029(3, 3014, 0)
            sendToLabel(1)

        def upon_STATE_END():
            callSubroutine('AntiAirSlowDeleteAura')
            callSubroutine('AntiAirSlowDeleteTornado')
            Unknown21012('6d6765665f3433345f746f726e61646f3400000000000000000000000000000020000000')
    sprite('mg434_00', 3)	# 1-3
    SFX_3('ad017')
    callSubroutine('AntiAirSlowCreateAura')
    sprite('mg434_01', 3)	# 4-6
    sprite('mg434_02', 3)	# 7-9
    sprite('mg434_00', 3)	# 10-12
    sprite('mg434_01', 3)	# 13-15
    sprite('mg434_02', 3)	# 16-18
    sprite('mg434_00', 3)	# 19-21
    sprite('mg434_01', 3)	# 22-24
    sprite('mg434_02', 3)	# 25-27
    sprite('mg434_00', 3)	# 28-30
    sprite('mg434_01', 3)	# 31-33
    sprite('mg434_03', 3)	# 34-36
    SFX_3('ad016')
    callSubroutine('AntiAirSlowDeleteAura')
    callSubroutine('AntiAirSlowCreateTornado')
    sprite('mg434_04', 3)	# 37-39
    sprite('mg434_05', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_06', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_07', 3)	# 46-48	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_08', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_06', 3)	# 52-54	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_07', 3)	# 55-57	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_08', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_06', 4)	# 61-64	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown23029(3, 3012, 0)
    sprite('mg434_07', 6)	# 65-70	 **attackbox here**
    callSubroutine('AntiAirSlowDeleteTornado')
    sprite('mg434_08', 6)	# 71-76	 **attackbox here**
    sprite('mg434_06', 6)	# 77-82	 **attackbox here**
    Unknown21012('6d6765665f3433345f746f726e61646f3400000000000000000000000000000020000000')
    sprite('mg434_07', 6)	# 83-88	 **attackbox here**
    sprite('keep', 32767)	# 89-32855
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('mg434_05', 3)	# 32856-32858	 **attackbox here**

    def upon_12():
        ScreenShake(10000, 30000)
    RefreshMultihit()
    sprite('mg434_06', 3)	# 32859-32861	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_07', 3)	# 32862-32864	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_08', 3)	# 32865-32867	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_06', 3)	# 32868-32870	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_07', 3)	# 32871-32873	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_08', 3)	# 32874-32876	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_06', 3)	# 32877-32879	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_07', 3)	# 32880-32882	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_08', 3)	# 32883-32885	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_06', 3)	# 32886-32888	 **attackbox here**
    RefreshMultihit()
    sprite('mg434_07', 6)	# 32889-32894	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown23029(3, 3012, 0)
    sprite('mg434_08', 6)	# 32895-32900	 **attackbox here**
    sprite('mg434_06', 6)	# 32901-32906	 **attackbox here**
    sprite('mg434_07', 6)	# 32907-32912	 **attackbox here**
    sprite('mg434_08', 6)	# 32913-32918	 **attackbox here**
    sprite('mg434_06', 6)	# 32919-32924	 **attackbox here**
    sprite('mg434_07', 6)	# 32925-32930	 **attackbox here**
    sprite('mg434_08', 6)	# 32931-32936	 **attackbox here**
    sprite('mg434_06', 6)	# 32937-32942	 **attackbox here**
    callSubroutine('AntiAirSlowDeleteTornado')
    sprite('mg434_07', 6)	# 32943-32948	 **attackbox here**
    sprite('mg434_08', 6)	# 32949-32954	 **attackbox here**
    sprite('mg434_06', 6)	# 32955-32960	 **attackbox here**
    sprite('mg434_07', 6)	# 32961-32966	 **attackbox here**
    sprite('mg434_08', 6)	# 32967-32972	 **attackbox here**
    sprite('mg434_06', 6)	# 32973-32978	 **attackbox here**
    Unknown21012('6d6765665f3433345f746f726e61646f3400000000000000000000000000000020000000')
    sprite('mg434_07', 6)	# 32979-32984	 **attackbox here**
    sprite('keep', 32767)	# 32985-65751
    enterState('PersonaDeleteAndIdling')

@State
def mgef_434_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown21010(1)
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4054(14)
    Unknown4045('6d6765665f34333461757261000000000000000000000000000000000000000064000000')
    gotoLabel(0)

@State
def mgef_434_aura_bk():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown21010(1)
        Unknown1007(50000)
        Unknown4054(15)
        Unknown23067('mgef_434aura_bk')
    sprite('null', 32767)	# 1-32767

@State
def mgef_434_aura_sub():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown21010(1)
        Unknown4054(14)
        Unknown23067('mgef_434aura_sub00')
    label(0)
    sprite('null', 4)	# 1-4
    Unknown4054(14)
    Unknown4045('6d6765665f343334617572615f7375620000000000000000000000000000000064000000')
    gotoLabel(0)

@Subroutine
def SpecialAntiAirInit():
    Unknown2054(1)
    Unknown21010(1)
    Unknown3001(0)
    Unknown3004(16)

@State
def mgef_434_tornado():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f343334746f726e61646f2e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown23015(13)
        GFX_0('mgef_434_tornado2', 100)
        GFX_0('mgef_434_tornado3', 100)
        GFX_0('mgef_434_tornado4', 100)
        GFX_2('mgef_434red')
        callSubroutine('SpecialAntiAirInit')
        callSubroutine('KowarePreset')
    label(0)
    sprite('null', 1)	# 1-1
    GFX_1('mgef_434tornado', 100)
    gotoLabel(0)
    label(580)
    sprite('null', 18)	# 2-19
    Unknown3004(-14)

@State
def mgef_434_tornado2():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f343334746f726e61646f322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown23015(13)
        callSubroutine('SpecialAntiAirInit')
        callSubroutine('KowarePreset')
    sprite('null', 32767)	# 1-32767
    label(580)
    sprite('null', 18)	# 32768-32785
    Unknown3004(-14)

@State
def mgef_434_tornado3():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f343334746f726e61646f332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown23015(14)
        callSubroutine('SpecialAntiAirInit')
        callSubroutine('KowarePreset')
    sprite('null', 32767)	# 1-32767
    label(580)
    sprite('null', 18)	# 32768-32785
    Unknown3004(-14)

@State
def mgef_434_tornado4():

    def upon_IMMEDIATE():
        callSubroutine('SpecialAntiAirInit')
        callSubroutine('KowarePreset')
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('mgef_434aura2', 100)
    gotoLabel(0)
    label(580)
    loopRest()

@State
def mgef_434SE():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        sendToLabelUpon(32, 0)
        Unknown2037(100)
    label(1)
    sprite('null', 16)	# 1-16
    SFX_3('ad019')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    label(0)
    sprite('null', 1)	# 17-17

@State
def PAD_PersonaSpecialThrow():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PAD_SPAttackInit')
        Unknown2006()
        AttackLevel_(0)
        Damage(0)
        Unknown11044(1)
        AttackP1(100)
        AttackP2(100)
        Hitstop(1)
        Unknown30048(1)
        Unknown11032('ffffffffffffffff90d0030000000000')
        Unknown11054(200000)
        HitOverhead(2)
        HitLow(2)
        Unknown11025(1)
        Unknown11045(1)
        Unknown11082(1)
        Unknown30048(1)
        Unknown11080(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11058('0000000000000000000000000000000001000000')
        DisableAttackRestOfMove()
        Unknown11069('PAD_PersonaSpecialThrowGrip')
        callSubroutine('PAD_CheckWarp')
        Unknown2034(1)

        def upon_12():
            Unknown23029(3, 3015, 0)
            sendToLabel(1)
    sprite('mg433_00', 4)	# 1-4
    if (SLOT_25 < 205000):
        Unknown1000(1865000)
        teleportRelativeX(-205000)
    Unknown3032()
    Unknown3001(0)
    Unknown3004(21)
    sprite('mg433_01', 4)	# 5-8
    sprite('mg433_02', 4)	# 9-12
    sprite('mg433_00', 4)	# 13-16
    Unknown3001(255)
    Unknown3004(0)
    sprite('mg433_02', 4)	# 17-20
    SFX_3('cut_l')
    sprite('mg433_03', 3)	# 21-23
    sprite('mg433_04', 2)	# 24-25
    GFX_0('mgef_433_slash', 100)
    sprite('mg433_05', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()

    def upon_CLEAR_OR_EXIT():
        Unknown11045(1)
        Unknown48('19000000020000000200000016000000020000001e000000')
        if SLOT_2:
            Unknown11045(0)
    sprite('mg433_06', 5)	# 29-33	 **attackbox here**
    StartMultihit()
    Unknown23029(3, 3013, 0)
    sprite('mg433_07', 5)	# 34-38
    sprite('mg433_08', 5)	# 39-43
    sprite('mg433_09', 5)	# 44-48
    sprite('mg433_07', 5)	# 49-53
    sprite('mg433_08', 5)	# 54-58
    sprite('mg433_09', 5)	# 59-63
    sprite('mg433_07', 5)	# 64-68
    sprite('mg433_08', 5)	# 69-73
    sprite('mg433_09', 5)	# 74-78
    sprite('mg433_08', 5)	# 79-83
    sprite('keep', 32767)	# 84-32850
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('keep', 32767)	# 32851-65617
    enterState('PAD_PersonaSpecialThrowGrip')

@State
def mgef_433_slash():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4003('6d6765665f343333736c6173682e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        teleportRelativeX(75000)
        Unknown1007(-75000)
        Unknown2054(1)
    sprite('null', 14)	# 1-14
    GFX_0('mgef_433_slash_sub', 100)
    GFX_0('mgef_433_slash_bg', 100)

@State
def mgef_433_slash_sub():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
    sprite('null', 3)	# 1-3
    teleportRelativeX(192000)
    Unknown1007(576000)
    Unknown4054(12)
    Unknown4045('6d6765665f343333736c6173680000000000000000000000000000000000000064000000')
    sprite('null', 3)	# 4-6
    teleportRelativeX(-64000)
    Unknown1007(-350000)
    Unknown4054(12)
    Unknown4045('6d6765665f343333736c6173680000000000000000000000000000000000000064000000')

@State
def mgef_433_slash_bg():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        teleportRelativeX(225000)
        Unknown1007(640000)
    sprite('null', 5)	# 1-5
    sprite('null', 1)	# 6-6
    Unknown4048(17000)
    Unknown4054(14)
    Unknown4045('6d6765665f343333736c6173685f62670000000000000000000000000000000064000000')

@State
def PAD_PersonaSpecialThrowGrip():

    def upon_IMMEDIATE():
        callSubroutine('PAD_SPAttackInit')
        Unknown17011('PAD_PersonaSpecialThrowExe', 2, 0, 0)
        Unknown2006()
        AttackLevel_(4)
        AttackP1(100)
        Unknown30048(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown11082(1)
        callSubroutine('PAD_CheckWarp')
        Unknown2034(1)
        Unknown30031(0)
    sprite('mg433_05', 3)	# 1-3	 **attackbox here**
    RefreshMultihit()
    sprite('mg433_06', 5)	# 4-8	 **attackbox here**
    StartMultihit()
    Unknown23029(3, 3013, 0)
    sprite('mg433_07', 5)	# 9-13
    sprite('mg433_08', 5)	# 14-18
    sprite('mg433_09', 5)	# 19-23
    sprite('mg433_07', 5)	# 24-28
    sprite('mg433_08', 5)	# 29-33
    sprite('mg433_09', 5)	# 34-38
    sprite('mg433_07', 5)	# 39-43
    sprite('mg433_08', 5)	# 44-48
    sprite('mg433_09', 5)	# 49-53
    sprite('mg433_08', 5)	# 54-58
    sprite('keep', 32767)	# 59-32825
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaSpecialThrowExe():

    def upon_IMMEDIATE():
        callSubroutine('PAD_SPAttackInit')
        Unknown17012(2, 1, 0)
        Unknown2006()
        AttackLevel_(4)
        Damage(500)
        MinimumDamagePct(5)
        AttackP2(50)
        Unknown11092(1)
        Hitstop(6)
        AirUntechableTime(50)
        Unknown9310(60)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11069('PAD_PersonaSpecialThrowExe')
        Unknown30031(0)
        Unknown23022(1)
    sprite('mg433_05', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    sprite('mg433_06', 10)	# 3-12	 **attackbox here**
    RefreshMultihit()
    Unknown5000(29, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown8003(0, 1, 1)
    ScreenShake(20000, 0)
    sprite('mg433_07', 4)	# 13-16
    sprite('mg433_08', 4)	# 17-20
    sprite('mg433_09', 4)	# 21-24
    sprite('mg433_10', 5)	# 25-29
    sprite('mg433_11', 5)	# 30-34
    sprite('mg433_12', 5)	# 35-39
    sprite('mg433_13', 5)	# 40-44
    SFX_3('slash_blade_slow')
    sprite('mg433_14', 5)	# 45-49	 **attackbox here**
    SFX_3('damage_slash_m')
    SFX_3('counter_slash_l23')
    ScreenShake(20000, 0)
    AttackLevel_(4)
    Damage(1000)
    Hitstop(12)
    Unknown9016(1)
    RefreshMultihit()
    GFX_0('mgef_433_stab', -1)
    sprite('mg433_15', 5)	# 50-54
    sprite('mg433_12', 5)	# 55-59
    sprite('mg433_13', 5)	# 60-64
    SFX_3('slash_blade_slow')
    sprite('mg433_14', 5)	# 65-69	 **attackbox here**
    SFX_3('damage_slash_m')
    SFX_3('counter_slash_l23')
    ScreenShake(20000, 0)
    RefreshMultihit()
    Damage(2000)
    GFX_0('mgef_433_stab', -1)
    sprite('mg433_15', 6)	# 70-75
    sprite('mg433_12', 6)	# 76-81
    sprite('mg433_16', 6)	# 82-87
    sprite('mg433_17', 6)	# 88-93
    sprite('mg433_18', 6)	# 94-99
    SFX_3('slash_blade_slow')
    sprite('mg433_19', 2)	# 100-101
    sprite('mg433_20', 6)	# 102-107	 **attackbox here**
    SFX_3('damage_slash_mh')
    SFX_3('counter_slash_l45')
    SFX_3('counter_slash_l45')
    SFX_3('counter_slash_l45')
    ScreenShake(60000, 60000)
    AttackLevel_(5)
    Damage(3000)
    Hitstop(17)
    Unknown9310(0)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    AirPushbackX(2500)
    AirPushbackY(45000)
    AirUntechableTime(60)
    Unknown11064(0)
    RefreshMultihit()
    Unknown11069('')
    GFX_0('mgef_433_stab', -1)
    Unknown23029(3, 3016, 0)
    sprite('mg433_21', 6)	# 108-113
    Unknown23029(3, 3013, 0)
    sprite('mg433_22', 6)	# 114-119
    sprite('mg433_23', 6)	# 120-125
    sprite('mg433_21', 6)	# 126-131
    sprite('mg433_22', 6)	# 132-137
    sprite('mg433_23', 6)	# 138-143
    sprite('mg433_21', 6)	# 144-149
    sprite('mg433_22', 6)	# 150-155
    sprite('mg433_23', 6)	# 156-161
    sprite('mg433_21', 6)	# 162-167
    sprite('mg433_22', 8)	# 168-175
    sprite('keep', 32767)	# 176-32942
    enterState('PersonaDeleteAndIdling')

@State
def mgef_433_stab():

    def upon_IMMEDIATE():
        Unknown1086(22)
        teleportRelativeY(0)
    sprite('null', 1)	# 1-1
    GFX_1('mgef_433stab', 100)

@State
def PAD_PersonaAntiAirPSkill():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000c0d40100000000000000000080841e000000000000000000')
        callSubroutine('PAD_SPAttackInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(1800)
        AirUntechableTime(60)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2500)
        AirPushbackY(45000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown9016(1)
        callSubroutine('PAD_ForceWarp')
        Unknown23078(1)
        EnableCollision(0)
        Unknown2034(1)
        Unknown2053(1)
        Unknown23059(1)
        callSubroutine('PartnerSkillInit')
    sprite('mg432_05', 3)	# 1-3
    sprite('mg432_06', 3)	# 4-6
    sprite('mg432_07', 2)	# 7-8
    sprite('mg432_08', 2)	# 9-10
    sprite('mg432_09', 2)	# 11-12
    SFX_3('slash_blade_slow')
    sprite('mg432_10', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    sprite('mg432_11', 2)	# 16-17
    GFX_0('vr_mg432_zanzou2', 100)
    Unknown23029(3, 2511, 0)
    sprite('mg432_12', 4)	# 18-21
    sprite('mg432_13', 4)	# 22-25
    sprite('mg432_14', 4)	# 26-29
    sprite('mg432_12', 4)	# 30-33
    sprite('mg432_13', 4)	# 34-37
    sprite('mg432_14', 4)	# 38-41
    sprite('mg432_12', 4)	# 42-45
    sprite('mg432_13', 4)	# 46-49
    sprite('mg432_14', 4)	# 50-53
    sprite('keep', 32767)	# 54-32820
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaSearchShotPSkill():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('16000000640000006079feff40420f0000000000000000000000000000000000')
        callSubroutine('PAD_SPAttackInit')
        callSubroutine('PartnerSkillInit')
        Unknown2006()
        AttackLevel_(4)
        Damage(2300)
        AirUntechableTime(30)
        Unknown9310(1)
        Hitstop(0)
        Unknown11001(12, 12, 12)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(-50000)
        AirPushbackX(0)
        PushbackX(6000)
        Unknown9016(1)
        Unknown9266(3)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11058('0100000000000000000000000000000000000000')
        DisableAttackRestOfMove()
        callSubroutine('PAD_ForceWarp')
        EnableCollision(0)
        Unknown2053(1)

        def upon_14():
            Unknown21012('6a756d6f6e6a69426967736c617368546174650000000000000000000000000020000000')
            Unknown21012('6a756d6f6e6a69426967736c617368536f636b3030000000000000000000000020000000')
            Unknown21012('6a756d6f6e6a69426967736c617368536f636b3031000000000000000000000020000000')

        def upon_LANDING():
            sendToLabel(0)
        callSubroutine('PartnerSkillInit')
    sprite('mg233_00', 12)	# 1-12
    Unknown3032()
    Unknown3001(0)
    Unknown3029(1)
    sprite('mg233_01', 2)	# 13-14
    Unknown1086(22)
    teleportRelativeY(1000000)
    Unknown3004(65)
    SFX_3('persona_destroy')
    sprite('mg233_02', 2)	# 15-16
    sprite('mg233_03', 2)	# 17-18
    sprite('mg233_04', 2)	# 19-20
    sprite('mg233_02', 2)	# 21-22
    sprite('mg233_05', 4)	# 23-26
    physicsYImpulse(-5000)
    sprite('mg233_06', 4)	# 27-30
    sprite('mg233_07', 32767)	# 31-32797
    physicsYImpulse(-200000)
    GFX_0('jumonjiBigslashTate', 104)
    label(0)
    sprite('mg233_08', 2)	# 32798-32799
    Unknown1084(1)
    Unknown3029(0)
    ScreenShake(20000, 0)
    SFX_3('ad002')
    sprite('mg233_09', 3)	# 32800-32802	 **attackbox here**
    GFX_0('jumonjiBigslashSock00', 1)
    RefreshMultihit()
    sprite('mg233_10', 5)	# 32803-32807	 **attackbox here**
    GFX_0('jumonjiBigslashSock01', 100)
    SFX_3('thunder_l')
    sprite('mg233_11', 5)	# 32808-32812
    Unknown23029(3, 2512, 0)
    sprite('mg233_12', 5)	# 32813-32817
    sprite('mg233_13', 5)	# 32818-32822
    sprite('mg233_14', 5)	# 32823-32827
    sprite('mg233_15', 10)	# 32828-32837
    sprite('mg233_15', 20)	# 32838-32857
    sprite('keep', 32767)	# 32858-65624
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateAssault():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000000000000000000000000000000000000000000000000000')
        callSubroutine('PAD_DDAttackInit')
        Unknown23056('')
        callSubroutine('PAD_ForceWarp')
        Unknown23066(1)
        Unknown2054(1)
        Unknown2053(1)
        Unknown23022(1)
        Unknown3032()
        Unknown3001(0)
        Unknown3004(10)
        Unknown23032(50)
        Unknown23033(80)
    sprite('mg430_00', 4)	# 1-4
    sprite('mg430_01', 4)	# 5-8
    sprite('mg430_02', 4)	# 9-12
    sprite('mg430_00', 4)	# 13-16
    sprite('mg430_01', 4)	# 17-20
    sprite('mg430_02', 4)	# 21-24
    sprite('mg430_03', 4)	# 25-28
    sprite('mg430_04', 21)	# 29-49
    sprite('mg430_05', 2)	# 50-51
    sprite('mg430_06', 2)	# 52-53
    sprite('mg430_07', 4)	# 54-57
    SFX_3('slash_sword_slow')
    GFX_0('mgef_430_zanzou', 100)
    sprite('mg430_08', 4)	# 58-61
    sprite('mg430_09', 4)	# 62-65
    sprite('mg430_10', 4)	# 66-69
    GFX_0('mgef_430', 100)
    GFX_0('mgef_430SE', 100)
    GFX_0('UltimateAssault_atk', 100)
    if (SLOT_60 == 1):
        Unknown2037(1)
        Unknown23029(1, 4021, 0)
    if (SLOT_60 == 2):
        Unknown23029(1, 4022, 0)
    if (SLOT_60 == 3):
        Unknown2037(1)
        Unknown23029(1, 4023, 0)
    sprite('mg430_08', 4)	# 70-73
    sprite('mg430_09', 4)	# 74-77
    sprite('mg430_10', 4)	# 78-81
    if SLOT_2:
        GFX_0('mgef_430', 100)
        GFX_0('mgef_430SE', 100)
    sprite('mg430_08', 4)	# 82-85
    sprite('mg430_09', 4)	# 86-89
    sprite('mg430_10', 4)	# 90-93
    if SLOT_2:
        GFX_0('mgef_430', 100)
        GFX_0('mgef_430SE', 100)
    sprite('mg430_08', 4)	# 94-97
    sprite('mg430_09', 4)	# 98-101
    sprite('mg430_10', 6)	# 102-107
    if SLOT_2:
        GFX_0('mgef_430', 100)
        GFX_0('mgef_430SE', 100)
    sprite('mg430_08', 6)	# 108-113
    sprite('mg430_09', 6)	# 114-119
    sprite('mg430_10', 6)	# 120-125
    sprite('mg430_08', 6)	# 126-131
    sprite('mg430_09', 6)	# 132-137
    sprite('mg430_10', 6)	# 138-143
    sprite('mg430_08', 6)	# 144-149
    sprite('mg430_09', 6)	# 150-155
    sprite('mg430_10', 4)	# 156-159
    sprite('keep', 32767)	# 160-32926
    enterState('PersonaDeleteAndIdling')

@State
def UltimateAssault_atk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4010(2)
        Unknown4009(2)
        AttackLevel_(3)
        Damage(930)
        MinimumDamagePct(12)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(2000)
        AirPushbackY(20000)
        PushbackX(0)
        AirUntechableTime(60)
        Unknown11034(2)
        ProjectileDurabilityLvl(0)
        Hitstop(0)
        Unknown11001(12, 12, 12)
        Unknown11084(1)
        Unknown9016(1)
        Unknown11057(750)
        Unknown1096(25000)
        Unknown2037(8)

        def upon_11():
            clearUponHandler(11)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 4021):
                Unknown30070('556c74696d61746541737361756c7453505f61746b0000000000000000000000')
                Damage(500)
                Unknown11110(80)
                MinimumDamagePct(10)
                Unknown2037(23)

                def upon_11():
                    clearUponHandler(11)
                    sendToLabel(2)
            if (SLOT_48 == 4022):
                Unknown30070('556c74696d61746541737361756c7444554f5f61746b00000000000000000000')
                Damage(200)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                Unknown2037(8)

                def upon_11():
                    clearUponHandler(11)
                    sendToLabel(1)
            if (SLOT_48 == 4023):
                Unknown30070('556c74696d61746541737361756c7444554f53505f61746b0000000000000000')
                Damage(100)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                Unknown2037(23)

                def upon_11():
                    clearUponHandler(11)
                    sendToLabel(2)
    sprite('dmy_UltimateAirAssault_Atk', 3)	# 1-3
    Unknown23151(22, 103)
    RefreshMultihit()
    sprite('null', 1)	# 4-4
    Unknown23029(3, 4011, 0)
    ExitState()
    label(1)
    sprite('dmy_UltimateAirAssault_Atk', 4)	# 5-8
    Unknown23151(22, 103)
    RefreshMultihit()
    Unknown2038(-1)
    if (not (SLOT_2 <= 0)):
        gotoLabel(1)
    else:
        gotoLabel(100)
    label(2)
    sprite('dmy_UltimateAirAssault_Atk', 3)	# 9-11
    Unknown23151(22, 103)
    RefreshMultihit()
    Unknown2038(-1)
    if (not (SLOT_2 <= 10)):
        gotoLabel(2)
    else:
        gotoLabel(3)
    label(3)
    sprite('dmy_UltimateAirAssault_Atk', 2)	# 12-13
    Unknown23151(22, 103)
    RefreshMultihit()
    Unknown2038(-1)
    if (not (SLOT_2 <= 0)):
        gotoLabel(3)
    else:
        gotoLabel(100)
    label(100)
    sprite('dmy_UltimateAirAssault_Atk', 4)	# 14-17
    Unknown23151(22, 103)
    RefreshMultihit()
    Unknown11001(12, 25, 25)
    sprite('null', 1)	# 18-18
    Unknown23029(3, 4011, 0)
    ExitState()

@State
def mgef_430_zanzou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(1)
        Unknown2054(1)
        Unknown21010(1)
        callSubroutine('PAD_EffectInit')
        GFX_0('mgef_430_slash', 100)
    sprite('vr_mg430_07', 4)	# 1-4

@State
def mgef_430_UBzanzou():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(1)
        Unknown2054(1)
        Unknown21010(1)
        callSubroutine('PAD_EffectInit')
        GFX_0('mgef_430_slash', 100)
    sprite('vr_mg430_07', 4)	# 1-4

@State
def mgef_430_slash():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(3)
        Unknown3033()
        callSubroutine('PAD_EffectInit')
    sprite('vr_mg430_00', 30)	# 1-30
    Unknown3004(-19)

@State
def mgef_430():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown6001(1)
        Unknown23032(50)
        Unknown23033(50)
        callSubroutine('KowarePreset')
    sprite('null', 60)	# 1-60
    Unknown23067('mgef_430red')
    ExitState()
    label(580)
    sprite('null', 16)	# 61-76
    Unknown3032()
    Unknown3004(-16)

@State
def mgef_430SE():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2037(7)
    label(1)
    sprite('null', 4)	# 1-4
    SFX_3('cut_m')
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(1)

@State
def PAD_PersonaUltimateThrow():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a0860100000000000000000080841e000000000000000000')
        callSubroutine('PAD_DDAttackInit')
        Unknown17011('PAD_PersonaUltimateThrowExe', 3, 0, 0)
        AttackLevel_(4)
        AttackP1(80)
        Unknown30048(1)
        Unknown11032('ffffffffffffffff400d030000000000')
        Unknown11054(200000)
        Unknown11002(-1)
        Unknown30061(1)
        Unknown11082(1)
        callSubroutine('PAD_CheckWarp')
        Unknown2054(1)
        Unknown23022(1)
        Unknown2034(1)
        Unknown30031(0)

        def upon_12():
            Unknown23029(3, 4018, 0)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('mg433_00', 3)	# 1-3
    if (SLOT_25 < 205000):
        Unknown1000(1865000)
        teleportRelativeX(-205000)
    Unknown3032()
    Unknown3001(0)
    Unknown3004(28)
    sprite('mg433_01', 3)	# 4-6
    sprite('mg433_02', 3)	# 7-9
    Unknown3001(255)
    Unknown3004(0)
    sprite('mg433_03', 3)	# 10-12
    SFX_3('cut_l')
    sprite('mg433_04', 2)	# 13-14
    GFX_0('mgef_433_slash', 100)
    sprite('mg433_05', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('mg433_06', 5)	# 18-22	 **attackbox here**
    StartMultihit()
    sprite('mg433_07', 5)	# 23-27
    sprite('mg433_08', 5)	# 28-32
    sprite('mg433_09', 5)	# 33-37
    sprite('mg433_07', 5)	# 38-42
    sprite('mg433_08', 5)	# 43-47
    sprite('mg433_09', 5)	# 48-52
    sprite('mg433_07', 5)	# 53-57
    sprite('mg433_08', 5)	# 58-62
    sprite('mg433_09', 5)	# 63-67
    sprite('mg433_08', 5)	# 68-72
    sprite('keep', 32767)	# 73-32839
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateThrowExe():

    def upon_IMMEDIATE():
        callSubroutine('PAD_DDAttackInit')
        Unknown17012(2, 1, 0)
        AttackLevel_(4)
        Damage(500)
        MinimumDamagePct(20)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        Hitstop(6)
        AirUntechableTime(50)
        Unknown9310(60)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11064(1)
        Unknown11069('PAD_PersonaUltimateThrowExe')
        Unknown2054(1)
        Unknown23022(1)
        Unknown30031(0)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('mg433_05', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(1, 80)
    sprite('mg433_06', 10)	# 3-12	 **attackbox here**
    RefreshMultihit()
    Unknown5000(29, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown8003(0, 1, 1)
    ScreenShake(20000, 0)
    sprite('mg433_07', 4)	# 13-16
    sprite('mg433_08', 4)	# 17-20
    sprite('mg433_09', 4)	# 21-24
    sprite('mg433_10', 3)	# 25-27
    sprite('mg433_11', 3)	# 28-30
    sprite('mg433_12', 3)	# 31-33
    sprite('mg433_13', 3)	# 34-36
    SFX_3('slash_blade_slow')
    sprite('mg433_14', 3)	# 37-39	 **attackbox here**
    SFX_3('damage_slash_m')
    SFX_3('counter_slash_l23')
    ScreenShake(20000, 0)
    AttackLevel_(4)
    Damage(1000)
    Hitstop(12)
    Unknown9016(1)
    RefreshMultihit()
    GFX_0('mgef_433_stab', -1)
    sprite('mg433_12', 3)	# 40-42
    sprite('mg433_13', 3)	# 43-45
    SFX_3('slash_blade_slow')
    sprite('mg433_14', 3)	# 46-48	 **attackbox here**
    SFX_3('damage_slash_m')
    SFX_3('counter_slash_l23')
    ScreenShake(20000, 0)
    RefreshMultihit()
    Damage(2000)
    GFX_0('mgef_433_stab', -1)
    sprite('mg433_11', 3)	# 49-51
    sprite('mg432_00', 6)	# 52-57
    sprite('mg432_03', 3)	# 58-60
    SFX_3('hit_m_slow')
    sprite('mg432_04ex01', 3)	# 61-63	 **attackbox here**
    RefreshMultihit()
    SFX_3('damage_slash_m')
    SFX_3('counter_slash_l23')
    GFX_0('mgef_433_stab', -1)
    Unknown8000(0, 1, 1)
    ScreenShake(10000, 0)
    Hitstop(6)
    Unknown11072(3, 0, 100000)

    def upon_12():
        Unknown11069('PAD_PersonaUltimateReGrip')
        enterState('PAD_PersonaUltimateReGrip')
    sprite('mg432_05', 3)	# 64-66
    sprite('keep', 32767)	# 67-32833
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateReGrip():

    def upon_IMMEDIATE():
        callSubroutine('PAD_DDAttackInit')
        Unknown17011('PAD_PersonaUltimateFinish', 3, 1, 0)
        Unknown2006()
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        DisableAttackRestOfMove()
        Unknown30031(0)
        Unknown23078(1)
        Unknown23059(1)
        Unknown2053(1)
        Unknown23022(1)
        SLOT_10 = 1

        def upon_STATE_END():
            SLOT_10 = 0
    sprite('mg432_04ex01', 3)	# 1-3	 **attackbox here**
    RefreshMultihit()
    sprite('mg432_05', 3)	# 4-6
    sprite('mg432_06', 6)	# 7-12
    sprite('mg432_07', 3)	# 13-15
    sprite('mg432_08', 3)	# 16-18
    sprite('mg432_09', 3)	# 19-21
    sprite('keep', 32767)	# 22-32788
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateFinish():

    def upon_IMMEDIATE():
        callSubroutine('PAD_DDAttackInit')
        Unknown17012(2, 1, 0)
        AttackLevel_(4)
        Damage(1200)
        MinimumDamagePct(20)
        AttackP1(100)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(6)
        AirUntechableTime(50)
        Unknown9310(60)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(0)
        AirPushbackY(-30000)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown11064(1)
        Unknown11069('PAD_PersonaUltimateFinish')
        Unknown2054(1)
        Unknown23022(1)
        Unknown30031(0)
    sprite('mg432_04ex01', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg432_05', 3)	# 4-6
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg432_06', 6)	# 7-12
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg432_07', 3)	# 13-15
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg432_08', 3)	# 16-18
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg432_09', 3)	# 19-21
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_55', 3)	# 22-24	 **attackbox here**
    StartMultihit()
    Unknown5000(0, 0)
    Unknown5001('0200000001000000010000000000000000000000')
    sprite('mg204_00', 3)	# 25-27
    SFX_3('hit_h_fast')
    Unknown5000(25, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_01', 3)	# 28-30
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_02', 6)	# 31-36
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_03', 3)	# 37-39
    SFX_3('slash_blade_middle')
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_04', 2)	# 40-41
    Unknown5000(26, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_05', 3)	# 42-44	 **attackbox here**
    SFX_0('damage_hit_h')
    Unknown5000(28, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('mg204_06', 6)	# 45-50
    sprite('mg433_11', 6)	# 51-56
    teleportRelativeX(100000)
    sprite('mg433_12', 6)	# 57-62
    sprite('mg433_16', 9)	# 63-71
    sprite('mg433_17', 9)	# 72-80
    sprite('mg433_18', 9)	# 81-89
    SFX_3('slash_blade_slow')
    sprite('mg433_19', 3)	# 90-92
    sprite('mg433_20', 6)	# 93-98	 **attackbox here**
    SFX_3('damage_slash_mh')
    SFX_3('counter_slash_l45')
    SFX_3('counter_slash_l45')
    SFX_3('counter_slash_l45')
    ScreenShake(60000, 60000)
    AttackLevel_(5)
    Damage(3000)
    MinimumDamagePct(25)
    Hitstop(17)
    Unknown9310(0)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    AirPushbackX(10000)
    AirPushbackY(50000)
    AirUntechableTime(60)
    Unknown11064(0)
    RefreshMultihit()
    Unknown11069('')
    GFX_0('mgef_433_stab', -1)
    Unknown23029(3, 4019, 0)
    sprite('mg433_21', 6)	# 99-104
    sprite('mg433_22', 6)	# 105-110
    sprite('mg433_23', 6)	# 111-116
    sprite('mg433_21', 6)	# 117-122
    sprite('mg433_22', 6)	# 123-128
    sprite('mg433_23', 6)	# 129-134
    sprite('mg433_21', 6)	# 135-140
    sprite('mg433_22', 6)	# 141-146
    sprite('mg433_23', 6)	# 147-152
    sprite('mg433_21', 6)	# 153-158
    sprite('mg433_22', 8)	# 159-166
    sprite('keep', 32767)	# 167-32933
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateBlade():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000090d003000000000000000000000000000000000000000000')
        callSubroutine('PAD_DDAttackInit')
        Unknown23056('')
        AttackLevel_(5)
        Damage(2500)
        AirHitstunAnimation(5)
        MinimumDamagePct(25)
        AttackP2(100)
        hitstun(130)
        Unknown9310(1)
        Unknown11056(3)
        Unknown9016(1)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown11064(1)
        Unknown9266(3)
        Unknown11069('PAD_PersonaUltimateBlade')
        Unknown11001(0, 0, 0)
        callSubroutine('PAD_ForceWarp')
        Unknown23078(1)
        Unknown2054(1)
        Unknown2053(1)
        Unknown23022(1)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 4012, 0)
            GFX_0('UltimateBladeShockYoko', 0)
            GFX_0('mgef_430_mist', 100)
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
    sprite('mg430_00', 3)	# 1-3
    sprite('mg430_01', 3)	# 4-6
    sprite('mg430_02', 3)	# 7-9
    sprite('mg430_03', 3)	# 10-12
    sprite('mg430_04', 6)	# 13-18
    sprite('mg430_05', 2)	# 19-20
    sprite('mg430_06', 2)	# 21-22
    sprite('mg430_07ex01', 4)	# 23-26	 **attackbox here**
    SFX_3('slash_sword_slow')
    GFX_0('mgef_430_UBzanzou', 100)
    sprite('mg430_08', 4)	# 27-30
    Unknown23029(3, 4014, 0)
    Unknown23022(0)
    sprite('mg430_09', 4)	# 31-34
    sprite('mg430_10', 4)	# 35-38
    sprite('mg430_08', 4)	# 39-42
    sprite('mg430_09', 4)	# 43-46
    sprite('mg430_10', 4)	# 47-50
    sprite('mg430_08', 4)	# 51-54
    sprite('mg430_09', 4)	# 55-58
    sprite('mg430_10', 4)	# 59-62
    sprite('mg430_08', 4)	# 63-66
    sprite('mg430_09', 4)	# 67-70
    sprite('mg430_10', 4)	# 71-74
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('mg430_09', 5)	# 32842-32846
    Unknown26('mgef_430_UBzanzou')
    sprite('mg430_10', 5)	# 32847-32851
    sprite('mg430_08', 5)	# 32852-32856
    sprite('mg430_09', 5)	# 32857-32861
    sprite('mg430_10', 5)	# 32862-32866
    sprite('mg430_08', 5)	# 32867-32871
    Unknown3001(255)
    Unknown3004(-12)
    sprite('mg430_09', 5)	# 32872-32876
    sprite('mg430_10', 5)	# 32877-32881
    sprite('mg233_00', 10)	# 32882-32891
    Unknown1086(22)
    Unknown1007(1200000)
    Unknown3001(0)
    Unknown3004(0)
    Unknown3029(1)
    Unknown20000(1)
    Unknown20009(1300)
    sprite('mg233_00', 20)	# 32892-32911
    GFX_0('Cardrotate00', 0)
    sprite('mg233_01', 2)	# 32912-32913
    Unknown3004(65)
    SFX_3('persona_destroy')
    sprite('mg233_02', 2)	# 32914-32915
    sprite('mg233_03', 2)	# 32916-32917
    sprite('mg233_04', 2)	# 32918-32919
    sprite('mg233_02', 2)	# 32920-32921
    sprite('mg233_03', 2)	# 32922-32923
    sprite('mg233_04', 2)	# 32924-32925
    sprite('mg233_02', 2)	# 32926-32927
    sprite('mg233_03', 2)	# 32928-32929
    sprite('mg233_04', 2)	# 32930-32931
    sprite('mg233_05', 4)	# 32932-32935
    Unknown20001(1)
    physicsYImpulse(-5000)
    sprite('mg233_06', 4)	# 32936-32939
    sprite('mg233_07', 32767)	# 32940-65706
    physicsYImpulse(-200000)
    GFX_0('UltimateBladeShockTate', 104)
    label(10)
    sprite('mg233_08', 2)	# 65707-65708
    Unknown1084(1)
    Unknown3029(0)
    Unknown20009(1000)
    ScreenShake(20000, 0)
    SFX_3('ad002')
    sprite('mg233_09', 3)	# 65709-65711	 **attackbox here**
    GFX_0('UltimateBladeShock00', 1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(4800)
    MinimumDamagePct(30)
    Unknown11064(0)
    AttackP1(80)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9155()
    Unknown9016(1)
    Unknown9266(3)
    PushbackX(6000)
    AttackP2(60)
    Unknown9156(21)
    Unknown9130(20)
    Unknown9142(300)
    Unknown30048(1)
    Unknown11069('')
    Unknown23029(3, 4013, 0)
    sprite('mg233_10', 5)	# 65712-65716	 **attackbox here**
    GFX_0('UltimateBladeShock01', 100)
    Unknown20001(0)
    SFX_3('thunder_l')
    sprite('mg233_11', 5)	# 65717-65721
    sprite('mg233_12', 5)	# 65722-65726
    Unknown20000(0)
    sprite('mg233_13', 5)	# 65727-65731
    sprite('mg233_14', 5)	# 65732-65736
    sprite('mg233_15', 50)	# 65737-65786
    label(580)
    sprite('keep', 32767)	# 65787-98553
    enterState('PersonaDeleteAndIdling')

@State
def Cardrotate00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('616465665f6a756d6f6e6a695f636172646272616b6530302e44494700000000626365665f6a756d6f6e6a695f636172646272616b6530305f3030302e6d6d00')
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
        Unknown4003('616465665f6a756d6f6e6a695f636172646272616b6530312e44494700000000626365665f6a756d6f6e6a695f636172646272616b6530315f3030302e6d6d00')
        Unknown23015(1)
        Unknown1096(2000)
    sprite('null', 8)	# 1-8
    Unknown23117(-16731137, 8)
    sprite('null', 1)	# 9-9
    GFX_1('mgef_cardcrash_03', 100)

@State
def mgef_430_mist():

    def upon_IMMEDIATE():
        pass
    sprite('null', 15)	# 1-15
    GFX_0('mgef_430_mist_a', 100)
    GFX_0('mgef_430_mist_b', 100)
    sprite('null', 120)	# 16-135

@State
def mgef_430_mist_a():

    def upon_IMMEDIATE():
        Unknown6001(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23057(50)
            Unknown23058(50)
        Unknown2055(32)
    label(0)
    sprite('null', 8)	# 1-8
    GFX_1('mgef_610mist_a', 100)
    gotoLabel(0)

@State
def mgef_430_mist_b():

    def upon_IMMEDIATE():
        teleportRelativeX(31000)
        Unknown1007(5000)
    sprite('null', 1)	# 1-1
    Unknown4054(9)
    Unknown4045('6d6765665f3631306d6973745f6200000000000000000000000000000000000064000000')

@State
def mgef_430_mist_3d():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f3631306d69737400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)
        Unknown3032()
        Unknown3013(0)
        Unknown3019(0)
        Unknown1056(1100)
        Unknown1064(880)
        Unknown6001(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23032(50)
            Unknown23033(110)
    sprite('null', 16)	# 1-16
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 40)	# 17-56
    Unknown3001(128)
    Unknown3004(0)
    sprite('null', 128)	# 57-184
    Unknown3004(-2)

@State
def mgef_430_mist_3d_2():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f3631306d69737432000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(15)
        Unknown3032()
        Unknown3013(0)
        Unknown3019(0)
        Unknown1056(-600)
        Unknown1064(400)
        Unknown6001(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23032(50)
            Unknown23033(80)
    sprite('null', 16)	# 1-16
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 92)	# 17-108
    Unknown3001(128)
    Unknown3004(0)
    sprite('null', 64)	# 109-172
    Unknown3004(-4)

@State
def UltimateBladeShockYoko():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1064(0)
        Unknown3001(250)
        Unknown1072(5000)
        Unknown23015(2)
        Unknown1007(110000)
        Unknown23032(160)
        sendToLabelUpon(32, 0)
    sprite('null', 10)	# 1-10
    Unknown1067(120)
    sprite('null', 138)	# 11-148
    Unknown1067(0)
    sprite('null', 10)	# 149-158
    Unknown1067(-100)
    Unknown3004(-26)
    ExitState()
    label(0)
    sprite('null', 9)	# 159-167
    Unknown1067(120)
    sprite('null', 146)	# 168-313
    Unknown1067(0)
    sprite('null', 10)	# 314-323
    Unknown1067(-100)
    Unknown3004(-26)
    ExitState()

@State
def UltimateBladeShockTate():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown1072(90000)
        teleportRelativeX(65000)
        Unknown1064(0)
        Unknown3001(0)
        Unknown2054(1)
        callSubroutine('KowarePreset')
    sprite('null', 20)	# 1-20
    Unknown3004(12)
    Unknown1067(65)
    sprite('null', 15)	# 21-35
    Unknown1067(0)
    sprite('null', 10)	# 36-45
    Unknown1067(-80)
    Unknown3004(-26)
    ExitState()
    label(580)
    sprite('null', 16)	# 46-61
    Unknown3004(-16)

@State
def UltimateBladeShock00():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown1064(925)
        Unknown1056(700)
        Unknown3001(150)
        Unknown2054(1)
        callSubroutine('KowarePreset')
    sprite('null', 10)	# 1-10
    GFX_0('jumonji_ground', 100)
    sprite('null', 10)	# 11-20
    Unknown3004(-26)
    ExitState()
    label(580)
    sprite('null', 16)	# 21-36
    Unknown3004(-16)

@State
def UltimateBladeShock01():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f6a756d6f6e6a695f736c61736830322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown3032()
        Unknown1064(925)
        Unknown1056(700)
        Unknown3001(255)
        Unknown2054(1)
        callSubroutine('KowarePreset')
    sprite('null', 15)	# 1-15
    sprite('null', 20)	# 16-35
    Unknown1059(20)
    Unknown3004(-12)
    ExitState()
    label(580)
    sprite('null', 16)	# 36-51
    Unknown3004(-16)

@State
def PAD_PersonaUltimateBladeSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('030000006400000090d003000000000000000000000000000000000000000000')
        callSubroutine('PAD_DDAttackInit')
        Unknown23056('')
        AttackLevel_(5)
        Damage(2500)
        AirHitstunAnimation(5)
        MinimumDamagePct(25)
        AttackP2(100)
        hitstun(100)
        Unknown9310(1)
        Unknown11056(3)
        Unknown9016(1)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown11064(1)
        Unknown9266(3)
        Unknown11069('PAD_PersonaUltimateBladeSP')
        Unknown11001(0, 0, 0)
        callSubroutine('PAD_ForceWarp')
        Unknown23078(1)
        Unknown2054(1)
        Unknown2053(1)
        Unknown23022(1)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 4015, 0)
            GFX_0('UltimateBladeShockYoko', 0)
            Unknown21007(1, 32)
            GFX_0('mgef_430_mist', 100)
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
    sprite('mg430_00', 3)	# 1-3
    sprite('mg430_01', 3)	# 4-6
    sprite('mg430_02', 3)	# 7-9
    sprite('mg430_03', 3)	# 10-12
    sprite('mg430_04', 6)	# 13-18
    sprite('mg430_05', 2)	# 19-20
    sprite('mg430_06', 2)	# 21-22
    sprite('mg430_07ex01', 4)	# 23-26	 **attackbox here**
    SFX_3('slash_sword_slow')
    GFX_0('mgef_430_UBzanzou', 100)
    sprite('mg430_08', 4)	# 27-30
    Unknown23029(3, 4017, 0)
    Unknown23022(0)
    sprite('mg430_09', 4)	# 31-34
    sprite('mg430_10', 4)	# 35-38
    sprite('mg430_08', 4)	# 39-42
    sprite('mg430_09', 4)	# 43-46
    sprite('mg430_10', 4)	# 47-50
    sprite('mg430_08', 4)	# 51-54
    sprite('mg430_09', 4)	# 55-58
    sprite('mg430_10', 4)	# 59-62
    sprite('mg430_08', 4)	# 63-66
    sprite('mg430_09', 4)	# 67-70
    sprite('mg430_10', 4)	# 71-74
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('mg430_09', 5)	# 32842-32846
    Unknown26('mgef_430_UBzanzou')
    sprite('mg430_10', 5)	# 32847-32851
    sprite('mg430_08', 5)	# 32852-32856
    Unknown3001(255)
    Unknown3004(-12)
    sprite('mg430_09', 5)	# 32857-32861
    sprite('mg430_10', 5)	# 32862-32866
    sprite('null', 27)	# 32867-32893
    sprite('mg450_06', 4)	# 32894-32897
    Unknown20000(1)
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(0)
    Unknown3004(32)
    Unknown2005()
    sprite('mg450_07', 4)	# 32898-32901
    sprite('mg450_08', 4)	# 32902-32905
    sprite('mg450_06', 4)	# 32906-32909
    sprite('mg450_07', 4)	# 32910-32913
    sprite('mg450_08', 4)	# 32914-32917
    sprite('mg450_06', 4)	# 32918-32921
    sprite('mg450_07', 4)	# 32922-32925
    sprite('mg450_08', 4)	# 32926-32929
    sprite('mg450_06', 4)	# 32930-32933
    sprite('mg450_07', 4)	# 32934-32937
    sprite('mg450_08', 4)	# 32938-32941
    sprite('mg450_06', 4)	# 32942-32945
    sprite('mg450_07', 2)	# 32946-32947
    sprite('mg450_09', 3)	# 32948-32950
    GFX_0('UltimateBladeShockTate', 104)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    sprite('mg450_10', 3)	# 32951-32953
    GFX_0('UltimateBladeShock00', 1)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    sprite('mg450_11ex01', 1)	# 32954-32954	 **attackbox here**
    RefreshMultihit()
    Unknown4009(3)
    Unknown23078(0)
    Damage(230)
    Hitstop(2)
    GroundedHitstunAnimation(1)
    AirPushbackX(3000)
    AirPushbackY(-100000)
    YImpluseBeforeWallbounce(2500)
    PushbackX(6000)
    AirUntechableTime(180)
    Unknown9155()
    Unknown9310(1)
    Unknown9190(1)
    Unknown9118(60)
    Unknown11056(1)
    Unknown30048(1)
    sprite('mg450_11ex01', 1)	# 32955-32955	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_11ex01', 1)	# 32956-32956	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_11ex01', 1)	# 32957-32957	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32958-32958	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32959-32959	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32960-32960	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32961-32961	 **attackbox here**
    RefreshMultihit()
    Damage(4700)
    Unknown11064(0)
    AttackP2(60)
    Unknown11069('')
    GFX_0('UltimateBladeShock01', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    SFX_3('thunder_l')
    Unknown23029(3, 4016, 0)
    sprite('mg450_12', 3)	# 32962-32964
    GFX_0('mgef_433_stab', -1)
    sprite('mg450_13', 65)	# 32965-33029	 **attackbox here**
    StartMultihit()
    sprite('keep', 3)	# 33030-33032
    StartMultihit()
    Unknown20000(0)
    label(580)
    sprite('keep', 32767)	# 33033-65799
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateDUO():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a08601000000000000000000000000000000000000000000')
        callSubroutine('PAD_DDAttackInit')
        Unknown23056('')
        AttackLevel_(5)
        Damage(1000)
        AirHitstunAnimation(5)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        hitstun(130)
        Unknown9310(1)
        Unknown11056(3)
        Unknown9016(1)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown11064(1)
        Unknown9266(3)
        Unknown11069('PAD_PersonaUltimateDUO')
        Unknown11001(0, 0, 0)
        callSubroutine('PAD_ForceWarp')
        Unknown23078(1)
        Unknown2054(1)
        Unknown2053(1)
        Unknown23022(1)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 4211, 0)
            GFX_0('UltimateBladeShockYoko', 0)
            GFX_0('mgef_430_mist', 100)
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
    sprite('mg430_00', 3)	# 1-3
    sprite('mg430_01', 3)	# 4-6
    sprite('mg430_02', 3)	# 7-9
    sprite('mg430_03', 3)	# 10-12
    sprite('mg430_04', 6)	# 13-18
    sprite('mg430_05', 2)	# 19-20
    sprite('mg430_06', 2)	# 21-22
    sprite('mg430_07ex01', 4)	# 23-26	 **attackbox here**
    SFX_3('slash_sword_slow')
    GFX_0('mgef_430_UBzanzou', 100)
    sprite('mg430_08', 4)	# 27-30
    Unknown23029(3, 4213, 0)
    Unknown23022(0)
    sprite('mg430_09', 4)	# 31-34
    sprite('mg430_10', 4)	# 35-38
    sprite('mg430_08', 4)	# 39-42
    sprite('mg430_09', 4)	# 43-46
    sprite('mg430_10', 4)	# 47-50
    sprite('mg430_08', 4)	# 51-54
    sprite('mg430_09', 4)	# 55-58
    sprite('mg430_10', 4)	# 59-62
    sprite('mg430_08', 4)	# 63-66
    sprite('mg430_09', 4)	# 67-70
    sprite('mg430_10', 4)	# 71-74
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('mg430_09', 5)	# 32842-32846
    Unknown26('mgef_430_UBzanzou')
    sprite('mg430_10', 5)	# 32847-32851
    sprite('mg430_08', 5)	# 32852-32856
    sprite('mg430_09', 5)	# 32857-32861
    sprite('mg430_10', 5)	# 32862-32866
    sprite('mg430_08', 5)	# 32867-32871
    Unknown3001(255)
    Unknown3004(-12)
    sprite('mg430_09', 5)	# 32872-32876
    sprite('mg430_10', 5)	# 32877-32881
    sprite('mg233_00', 10)	# 32882-32891
    Unknown1086(22)
    Unknown1007(1200000)
    Unknown3001(0)
    Unknown3004(0)
    Unknown3029(1)
    Unknown20000(1)
    Unknown20009(1300)
    sprite('mg233_00', 20)	# 32892-32911
    GFX_0('Cardrotate00', 0)
    sprite('mg233_01', 2)	# 32912-32913
    Unknown3004(65)
    SFX_3('persona_destroy')
    sprite('mg233_02', 2)	# 32914-32915
    sprite('mg233_03', 2)	# 32916-32917
    sprite('mg233_04', 2)	# 32918-32919
    sprite('mg233_02', 2)	# 32920-32921
    sprite('mg233_03', 2)	# 32922-32923
    sprite('mg233_04', 2)	# 32924-32925
    sprite('mg233_02', 2)	# 32926-32927
    sprite('mg233_03', 2)	# 32928-32929
    sprite('mg233_04', 2)	# 32930-32931
    sprite('mg233_05', 4)	# 32932-32935
    Unknown20001(1)
    physicsYImpulse(-5000)
    sprite('mg233_06', 4)	# 32936-32939
    sprite('mg233_07', 32767)	# 32940-65706
    physicsYImpulse(-200000)
    GFX_0('UltimateBladeShockTate', 104)
    label(10)
    sprite('mg233_08', 2)	# 65707-65708
    Unknown1084(1)
    Unknown3029(0)
    Unknown20009(1000)
    ScreenShake(20000, 0)
    SFX_3('ad002')
    sprite('mg233_09', 3)	# 65709-65711	 **attackbox here**
    GFX_0('UltimateBladeShock00', 1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(1500)
    Unknown11064(0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9155()
    Unknown9016(1)
    Unknown9266(3)
    PushbackX(6000)
    Unknown9156(21)
    Unknown9130(20)
    Unknown9142(300)
    Unknown30048(1)
    Unknown11069('')
    Unknown23029(3, 4212, 0)
    sprite('mg233_10', 5)	# 65712-65716	 **attackbox here**
    GFX_0('UltimateBladeShock01', 100)
    Unknown20001(0)
    SFX_3('thunder_l')
    sprite('mg233_11', 5)	# 65717-65721
    sprite('mg233_12', 5)	# 65722-65726
    Unknown20000(0)
    sprite('mg233_13', 5)	# 65727-65731
    sprite('mg233_14', 5)	# 65732-65736
    sprite('mg233_15', 50)	# 65737-65786
    label(580)
    sprite('keep', 32767)	# 65787-98553
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaUltimateDUOSP():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown23184('0300000064000000a08601000000000000000000000000000000000000000000')
        callSubroutine('PAD_DDAttackInit')
        Unknown23056('')
        AttackLevel_(5)
        Damage(1000)
        AirHitstunAnimation(5)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        hitstun(100)
        Unknown9310(1)
        Unknown11056(3)
        Unknown9016(1)
        Unknown11032('ffffffffffffffff801a060000000000')
        Unknown11064(1)
        Unknown9266(3)
        Unknown11069('PAD_PersonaUltimateDUOSP')
        Unknown11001(0, 0, 0)
        callSubroutine('PAD_ForceWarp')
        Unknown23078(1)
        Unknown2054(1)
        Unknown2053(1)
        Unknown23022(1)

        def upon_78():
            clearUponHandler(78)
            Unknown23029(3, 4214, 0)
            GFX_0('UltimateBladeShockYoko', 0)
            Unknown21007(1, 32)
            GFX_0('mgef_430_mist', 100)
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
    sprite('mg430_00', 3)	# 1-3
    sprite('mg430_01', 3)	# 4-6
    sprite('mg430_02', 3)	# 7-9
    sprite('mg430_03', 3)	# 10-12
    sprite('mg430_04', 6)	# 13-18
    sprite('mg430_05', 2)	# 19-20
    sprite('mg430_06', 2)	# 21-22
    sprite('mg430_07ex01', 4)	# 23-26	 **attackbox here**
    SFX_3('slash_sword_slow')
    GFX_0('mgef_430_UBzanzou', 100)
    sprite('mg430_08', 4)	# 27-30
    Unknown23029(3, 4216, 0)
    Unknown23022(0)
    sprite('mg430_09', 4)	# 31-34
    sprite('mg430_10', 4)	# 35-38
    sprite('mg430_08', 4)	# 39-42
    sprite('mg430_09', 4)	# 43-46
    sprite('mg430_10', 4)	# 47-50
    sprite('mg430_08', 4)	# 51-54
    sprite('mg430_09', 4)	# 55-58
    sprite('mg430_10', 4)	# 59-62
    sprite('mg430_08', 4)	# 63-66
    sprite('mg430_09', 4)	# 67-70
    sprite('mg430_10', 4)	# 71-74
    sprite('keep', 32767)	# 75-32841
    enterState('PersonaDeleteAndIdling')
    label(1)
    sprite('mg430_09', 5)	# 32842-32846
    Unknown26('mgef_430_UBzanzou')
    sprite('mg430_10', 5)	# 32847-32851
    sprite('mg430_08', 5)	# 32852-32856
    Unknown3001(255)
    Unknown3004(-12)
    sprite('mg430_09', 5)	# 32857-32861
    sprite('mg430_10', 5)	# 32862-32866
    sprite('null', 27)	# 32867-32893
    sprite('mg450_06', 4)	# 32894-32897
    Unknown20000(1)
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(0)
    Unknown3004(32)
    Unknown2005()
    sprite('mg450_07', 4)	# 32898-32901
    sprite('mg450_08', 4)	# 32902-32905
    sprite('mg450_06', 4)	# 32906-32909
    sprite('mg450_07', 4)	# 32910-32913
    sprite('mg450_08', 4)	# 32914-32917
    sprite('mg450_06', 4)	# 32918-32921
    sprite('mg450_07', 4)	# 32922-32925
    sprite('mg450_08', 4)	# 32926-32929
    sprite('mg450_06', 4)	# 32930-32933
    sprite('mg450_07', 4)	# 32934-32937
    sprite('mg450_08', 4)	# 32938-32941
    sprite('mg450_06', 4)	# 32942-32945
    sprite('mg450_07', 2)	# 32946-32947
    sprite('mg450_09', 3)	# 32948-32950
    GFX_0('UltimateBladeShockTate', 104)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    sprite('mg450_10', 3)	# 32951-32953
    GFX_0('UltimateBladeShock00', 1)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    sprite('mg450_11ex01', 1)	# 32954-32954	 **attackbox here**
    RefreshMultihit()
    Unknown4009(3)
    Unknown23078(0)
    Damage(100)
    Unknown11064(0)
    Hitstop(2)
    GroundedHitstunAnimation(1)
    AirPushbackX(3000)
    AirPushbackY(-100000)
    YImpluseBeforeWallbounce(2500)
    PushbackX(6000)
    AirUntechableTime(180)
    Unknown9155()
    Unknown9310(1)
    Unknown9190(1)
    Unknown9118(60)
    Unknown11056(1)
    Unknown30048(1)
    sprite('mg450_11ex01', 1)	# 32955-32955	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_11ex01', 1)	# 32956-32956	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_11ex01', 1)	# 32957-32957	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32958-32958	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32959-32959	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32960-32960	 **attackbox here**
    RefreshMultihit()
    sprite('mg450_12ex01', 1)	# 32961-32961	 **attackbox here**
    RefreshMultihit()
    Damage(1300)
    Unknown11069('')
    GFX_0('UltimateBladeShock01', 100)
    Unknown36(1)
    teleportRelativeX(-150000)
    Unknown35()
    SFX_3('thunder_l')
    Unknown23029(3, 4215, 0)
    sprite('mg450_12', 3)	# 32962-32964
    GFX_0('mgef_433_stab', -1)
    sprite('mg450_13', 65)	# 32965-33029	 **attackbox here**
    StartMultihit()
    sprite('keep', 3)	# 33030-33032
    StartMultihit()
    Unknown20000(0)
    label(580)
    sprite('keep', 32767)	# 33033-65799
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaAstralHeat():

    def upon_IMMEDIATE():
        Unknown23023()
        Unknown1086(22)
        teleportRelativeX(-350000)
        callSubroutine('PAD_DDAttackInit')
        Unknown2006()
        Unknown17011('PAD_PersonaAstralHeatExe', 6, 1, 0)
        AttackLevel_(4)
        Damage(0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11034(1)
        ProjectileDurabilityLvl(0)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11058('0000000000000000000000000000000001000000')
        Unknown30048(1)
        DisableAttackRestOfMove()
        Unknown30031(0)
        Unknown23022(1)
        sendToLabelUpon(32, 0)
    sprite('null', 60)	# 1-60
    GFX_0('mgef_450_mg_start', 100)
    GFX_0('Ichigeki_Camera', 100)
    Unknown38(4, 1)
    SFX_3('ad011')
    sprite('mg232_00ex', 4)	# 61-64
    physicsXImpulse(15000)
    SFX_3('blood_l')
    SFX_3('blood_l')
    SFX_3('ad011')
    sprite('mg232_03ex', 4)	# 65-68
    sprite('mg232_04ex', 4)	# 69-72	 **attackbox here**
    RefreshMultihit()
    SFX_3('ad011')
    sprite('mg232_05ex', 3)	# 73-75	 **attackbox here**
    sprite('mg232_06ex', 3)	# 76-78	 **attackbox here**
    physicsXImpulse(0)
    sprite('mg232_07ex', 3)	# 79-81
    ExitState()
    label(0)
    sprite('keep', 32767)	# 82-32848
    enterState('PersonaDeleteAndIdling')

@State
def mgef_450_mg_start():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 10)
        Unknown4007(2)
    sprite('null', 20)	# 1-20
    GFX_2('mgef_450start')
    Unknown3001(0)
    Unknown3004(12)
    sprite('null', 10)	# 21-30
    Unknown3001(255)
    Unknown3004(0)
    GFX_1('mgef_450start_sub', 100)
    GFX_0('mgef_450_mg_start2', 100)
    label(0)
    sprite('null', 10)	# 31-40
    GFX_1('mgef_450start_sub', 100)
    gotoLabel(0)
    label(10)
    sprite('null', 20)	# 41-60
    Unknown3004(-12)

@State
def mgef_450_mg_start2():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 10)
        Unknown4007(2)
        GFX_1('mgef_450start_sub3', 100)
    label(0)
    sprite('null', 16)	# 1-16
    GFX_1('mgef_450start_sub2', 100)
    gotoLabel(0)
    label(10)
    sprite('null', 20)	# 17-36
    Unknown3004(-12)

@State
def Ichigeki_Camera():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 4522):
                sendToLabel(1)
            if (SLOT_48 == 4523):
                sendToLabel(2)
    sprite('null', 32767)	# 1-32767
    Unknown1086(22)
    Unknown20000(1)
    Unknown20002(1)
    Unknown20003(1)
    label(1)
    sprite('null', 30)	# 32768-32797
    sprite('null', 170)	# 32798-32967
    GFX_0('IchigekiPicture', 100)
    sprite('null', 6)	# 32968-32973
    Unknown4004('534345465f536861736861496e0000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown1072(180000)
    physicsYImpulse(140000)
    Unknown35()
    sprite('null', 12)	# 32974-32985
    Unknown21012('6d6765665f3435305f79756b615345000000000000000000000000000000000020000000')
    Unknown26('mgef_450_yuka')
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('null', 20)	# 32986-33005
    Unknown1000(0)
    sprite('null', 10)	# 33006-33015
    Unknown23024(3)
    Unknown23029(2, 4502, 0)
    sprite('null', 12)	# 33016-33027
    Unknown36(22)
    Unknown1000(10000)
    Unknown35()
    Unknown26('SCEF_ShashaIn')
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    sprite('null', 110)	# 33028-33137
    GFX_0('IchigekiSE', 100)
    sprite('null', 90)	# 33138-33227
    sprite('null', 32767)	# 33228-65994
    Unknown23029(2, 4503, 0)
    label(2)
    sprite('null', 10)	# 65995-66004
    Unknown23024(0)
    sprite('null', 70)	# 66005-66074
    SFX_3('whitenoize')
    SFX_3('whitenoize')
    SFX_3('whitenoize')
    SFX_3('whitenoize')
    SFX_3('whitenoize')
    SFX_3('whitenoize')
    sprite('null', 120)	# 66075-66194
    Unknown23029(2, 4504, 0)
    sprite('null', 45)	# 66195-66239
    SFX_3('ad003')
    Unknown23029(3, 4521, 0)
    sprite('null', 30)	# 66240-66269
    Unknown23029(2, 4506, 0)
    Unknown23029(3, 4505, 0)
    sprite('null', 32767)	# 66270-99036
    Unknown20006(1)

@State
def IchigekiPicture():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown23015(3)
        Unknown3001(0)
        Unknown3004(2)
        Unknown6001(1)
        Unknown1001(640000)
        Unknown1007(1430000)
    sprite('ichigeki0', 25)	# 1-25	 **attackbox here**
    physicsYImpulse(1000)
    GFX_0('adef_450_light', 100)
    sprite('ichigeki0', 5)	# 26-30	 **attackbox here**
    tag_voice(0, 'pad292_0', 'pad292_1', '', '')
    YAccel(80)
    sprite('ichigeki0', 5)	# 31-35	 **attackbox here**
    YAccel(80)
    sprite('ichigeki0', 30)	# 36-65	 **attackbox here**
    YAccel(80)
    sprite('ichigeki0', 50)	# 66-115	 **attackbox here**
    sprite('ichigeki0', 30)	# 116-145	 **attackbox here**
    sprite('ichigeki0', 30)	# 146-175	 **attackbox here**
    tag_voice(0, 'pad293_0', 'pad293_1', '', '')
    sprite('ichigeki0', 20)	# 176-195	 **attackbox here**
    Unknown3004(-16)

@State
def adef_450_light():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown6001(1)
        Unknown23032(50)
        Unknown23033(100)
        Unknown4054(1)
        Unknown23067('adef_450light')
        Unknown1064(750)
    sprite('null', 16)	# 1-16
    Unknown3001(0)
    Unknown3004(8)
    sprite('null', 32767)	# 17-32783
    Unknown3001(128)
    Unknown3004(0)

@State
def IchigekiSE():
    sprite('null', 40)	# 1-40
    SFX_3('ad009')
    sprite('null', 40)	# 41-80
    SFX_3('ad009')
    sprite('null', 40)	# 81-120
    SFX_3('ad009')
    sprite('null', 40)	# 121-160
    SFX_3('ad009')
    sprite('null', 40)	# 161-200
    SFX_3('ad009')
    sprite('null', 40)	# 201-240
    SFX_3('ad009')

@State
def PAD_PersonaAstralHeatExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 1, 0)
        Damage(0)
        Unknown11064(1)
        Unknown11084(1)
        DisableAttackRestOfMove()
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown23022(1)
        Unknown23015(0)
        Unknown2018(1, 80)
        Unknown2019(100)

        def upon_43():
            if (SLOT_48 == 4502):
                sendToLabel(1)
            if (SLOT_48 == 4503):
                sendToLabel(2)
            if (SLOT_48 == 4504):
                sendToLabel(3)
            if (SLOT_48 == 4506):
                sendToLabel(4)
            if (SLOT_48 == 4508):
                sendToLabel(10)
    sprite('mg232_04ex', 5)	# 1-5	 **attackbox here**
    physicsXImpulse(2500)
    SFX_3('grip_hugs')
    SFX_3('bound_marble_m')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_05ex', 5)	# 6-10	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('mg232_07ex', 6)	# 11-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('null', 32767)	# 17-32783
    physicsXImpulse(0)
    SFX_3('blood_h')
    SFX_3('blood_h')
    GFX_0('mgef_450_mg_grab', 100)
    Unknown21012('6d6765665f3435305f6d675f737461727400000000000000000000000000000020000000')
    Unknown21012('6d6765665f3435305f6d675f737461727432000000000000000000000000000020000000')
    Unknown23029(4, 4522, 0)
    Unknown3029(0)
    Unknown36(22)
    Unknown3001(0)
    Unknown35()
    label(1)
    sprite('mg232_04ex', 3)	# 32784-32786	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(0)
    hitstun(900)
    AirUntechableTime(900)
    Unknown9310(900)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackY(-50000)
    AirPushbackX(0)
    Unknown3001(0)
    Unknown36(22)
    teleportRelativeY(1500000)
    Unknown3001(255)
    Unknown2035(1)
    Unknown35()
    sprite('null', 32767)	# 32787-65553
    label(2)
    sprite('mg450_00', 4)	# 65554-65557
    Unknown2018(1, 80)
    Unknown2019(1000)
    Unknown3032()
    Unknown3001(0)
    Unknown3004(2)
    Unknown1086(22)
    Unknown1007(20000)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3070(1)
    Unknown3071(2)
    Unknown3072('e0000000ff0000000000000000000000')
    Unknown3073('00000000ff0000000000000000000000')
    Unknown3076(1050)
    sprite('mg450_01', 4)	# 65558-65561
    sprite('mg450_02', 4)	# 65562-65565
    sprite('mg450_00', 4)	# 65566-65569
    sprite('mg450_01', 4)	# 65570-65573
    sprite('mg450_02', 4)	# 65574-65577
    sprite('mg450_00', 4)	# 65578-65581
    sprite('mg450_01', 4)	# 65582-65585
    sprite('mg450_02', 4)	# 65586-65589
    sprite('mg450_00', 4)	# 65590-65593
    sprite('mg450_01', 4)	# 65594-65597
    sprite('mg450_02', 4)	# 65598-65601
    sprite('mg450_00', 4)	# 65602-65605
    sprite('mg450_01', 4)	# 65606-65609
    sprite('mg450_02', 4)	# 65610-65613
    sprite('mg450_00', 4)	# 65614-65617
    sprite('mg450_01', 4)	# 65618-65621
    sprite('mg450_02', 4)	# 65622-65625
    sprite('mg450_00', 4)	# 65626-65629
    sprite('mg450_01', 4)	# 65630-65633
    sprite('mg450_02', 4)	# 65634-65637
    sprite('mg450_00', 4)	# 65638-65641
    SFX_3('quake_s')
    ScreenShake(2000, 2000)
    sprite('mg450_01', 4)	# 65642-65645
    ScreenShake(2000, 2000)
    sprite('mg450_02', 4)	# 65646-65649
    ScreenShake(2000, 2000)
    sprite('mg450_00', 4)	# 65650-65653
    ScreenShake(2000, 2000)
    sprite('mg450_01', 4)	# 65654-65657
    SFX_3('quake_s')
    ScreenShake(2000, 2000)
    sprite('mg450_02', 4)	# 65658-65661
    ScreenShake(2000, 2000)
    sprite('mg450_00', 4)	# 65662-65665
    ScreenShake(2000, 2000)
    sprite('mg450_01', 4)	# 65666-65669
    ScreenShake(2000, 2000)
    sprite('mg450_02', 4)	# 65670-65673
    SFX_3('quake_s')
    ScreenShake(5000, 5000)
    sprite('mg450_00', 4)	# 65674-65677
    ScreenShake(5000, 5000)
    sprite('mg450_01', 4)	# 65678-65681
    ScreenShake(5000, 5000)
    sprite('mg450_02', 4)	# 65682-65685
    ScreenShake(5000, 5000)
    sprite('mg450_00', 4)	# 65686-65689
    SFX_3('quake_s')
    ScreenShake(5000, 5000)
    sprite('mg450_01', 4)	# 65690-65693
    ScreenShake(5000, 5000)
    sprite('mg450_02', 4)	# 65694-65697
    ScreenShake(5000, 5000)
    sprite('mg450_00', 4)	# 65698-65701
    ScreenShake(5000, 5000)
    sprite('mg450_01', 4)	# 65702-65705
    SFX_3('quake_s')
    ScreenShake(5000, 5000)
    sprite('mg450_02', 4)	# 65706-65709
    ScreenShake(5000, 5000)
    sprite('mg450_00', 4)	# 65710-65713
    ScreenShake(5000, 5000)
    sprite('mg450_01', 4)	# 65714-65717
    ScreenShake(5000, 5000)
    sprite('mg450_02', 4)	# 65718-65721
    SFX_3('quake_s')
    ScreenShake(5000, 5000)
    sprite('mg450_03', 4)	# 65722-65725
    ScreenShake(10000, 10000)
    GFX_0('mgef_450_aura', 100)
    sprite('mg450_04', 4)	# 65726-65729
    SFX_3('airdash_m')
    ScreenShake(10000, 10000)
    sprite('mg450_05', 4)	# 65730-65733
    ScreenShake(10000, 10000)
    sprite('mg450_06', 4)	# 65734-65737
    SFX_3('ad017')
    SFX_3('airdash_m')
    ScreenShake(10000, 10000)
    Unknown3001(255)
    Unknown3004(0)
    GFX_0('mgef_450_aura2', 0)
    GFX_0('mgef_450_aura2', 1)
    GFX_0('mgef_450_aura2', 2)
    GFX_0('mgef_450_aura2', 3)
    GFX_0('mgef_450_aura2', 4)
    GFX_0('mgef_450_aura2', 5)
    GFX_0('mgef_450_aura2', 6)
    GFX_0('mgef_450_aura2', 7)
    GFX_0('mgef_450_aura2', 8)
    GFX_0('mgef_450_aura2', 9)
    GFX_0('mgef_450_aura2', 10)
    GFX_0('mgef_450_aura2', 11)
    GFX_0('mgef_450_aura2', 12)
    GFX_0('mgef_450_aura2', 13)
    GFX_0('mgef_450_aura2', 14)
    sprite('mg450_07', 4)	# 65738-65741
    SFX_3('airdash_m')
    ScreenShake(10000, 10000)
    sprite('mg450_08', 4)	# 65742-65745
    ScreenShake(10000, 10000)
    sprite('mg450_06', 4)	# 65746-65749
    SFX_3('ad017')
    SFX_3('airdash_m')
    ScreenShake(10000, 10000)
    sprite('mg450_07', 4)	# 65750-65753
    ScreenShake(10000, 10000)
    sprite('mg450_08', 4)	# 65754-65757
    SFX_3('airdash_m')
    ScreenShake(15000, 15000)
    sprite('mg450_06', 4)	# 65758-65761
    ScreenShake(15000, 15000)
    sprite('mg450_07', 4)	# 65762-65765
    SFX_3('ad017')
    SFX_3('airdash_m')
    ScreenShake(15000, 15000)
    sprite('mg450_08', 4)	# 65766-65769
    ScreenShake(15000, 15000)
    sprite('mg450_06', 4)	# 65770-65773
    SFX_3('airdash_m')
    ScreenShake(15000, 15000)
    sprite('mg450_07', 4)	# 65774-65777
    ScreenShake(15000, 15000)
    sprite('mg450_08', 4)	# 65778-65781
    SFX_3('ad017')
    SFX_3('airdash_m')
    ScreenShake(15000, 15000)
    sprite('mg450_09', 3)	# 65782-65784
    ScreenShake(20000, 20000)
    sprite('mg450_10', 3)	# 65785-65787
    SFX_3('slash_blade_slow')
    SFX_3('slash_blade_slow')
    SFX_3('slash_blade_slow')
    ScreenShake(50000, 50000)
    sprite('mg450_11', 3)	# 65788-65790
    ScreenShake(50000, 50000)
    sprite('mg450_12', 3)	# 65791-65793
    ScreenShake(50000, 50000)
    SFX_3('cut_m')
    SFX_3('cut_m')
    SFX_3('cut_m')
    SFX_3('damage_ichigeki_slash')
    SFX_3('damage_ichigeki_slash')
    SFX_3('damage_ichigeki_slash')
    SFX_3('blaze_long')
    Unknown23029(4, 4523, 0)
    GFX_0('Win_TVnoise_off', 100)
    Unknown26('mgef_450_aura')
    Unknown26('mgef_450_aura2')
    Unknown3029(0)
    Unknown3038(1)
    Unknown36(22)
    Unknown3001(0)
    Unknown2035(1)
    Unknown35()
    sprite('mg450_13', 32767)	# 65794-98560	 **attackbox here**
    label(3)
    sprite('mg450_13', 3)	# 98561-98563	 **attackbox here**
    GFX_0('TV_OffBlack', 100)
    RefreshMultihit()
    Damage(43104)
    MinimumDamagePct(100)
    Unknown23011(9)
    AirPushbackX(0)
    AirPushbackY(0)
    Unknown9095()
    Unknown11064(3)
    sprite('mg450_13', 90)	# 98564-98653	 **attackbox here**
    sprite('mg450_13', 32767)	# 98654-131420	 **attackbox here**
    Unknown26('Win_TVnoise_off')
    label(4)
    sprite('mg610_00', 6)	# 131421-131426
    sendToLabelUpon(32, 10)
    Unknown1086(3)
    teleportRelativeX(-90000)
    Unknown1007(20000)
    Unknown3038(0)
    sprite('mg610_01', 6)	# 131427-131432
    sprite('mg610_02', 6)	# 131433-131438
    sprite('mg610_00', 6)	# 131439-131444
    sprite('mg610_01', 6)	# 131445-131450
    sprite('mg610_02', 6)	# 131451-131456
    sprite('mg610_03', 6)	# 131457-131462
    sprite('mg610_04', 6)	# 131463-131468
    sprite('mg610_05', 6)	# 131469-131474
    ScreenShake(15000, 25000)
    Unknown8004(0, 1, 1)
    GFX_1('mgef_groundtsuki', 0)
    sprite('mg610_06', 6)	# 131475-131480
    sprite('mg610_07', 6)	# 131481-131486
    sprite('mg610_08', 6)	# 131487-131492
    sprite('mg610_06', 6)	# 131493-131498
    GFX_0('mgef_450_mist', 100)
    sprite('mg610_07', 6)	# 131499-131504
    sprite('mg610_08', 6)	# 131505-131510
    sprite('mg610_06', 6)	# 131511-131516
    Unknown3032()
    Unknown3004(-7)
    Unknown23130(16711680, 60, 1)
    Unknown2035(1)
    sprite('mg610_07', 6)	# 131517-131522
    sprite('mg610_08', 6)	# 131523-131528
    sprite('mg610_06', 6)	# 131529-131534
    sprite('mg610_07', 6)	# 131535-131540
    sprite('mg610_08', 6)	# 131541-131546
    sprite('mg610_06', 6)	# 131547-131552
    sprite('mg610_07', 6)	# 131553-131558
    sprite('mg610_08', 6)	# 131559-131564
    Unknown3038(1)
    label(5)
    sprite('mg610_06', 6)	# 131565-131570
    sprite('mg610_07', 6)	# 131571-131576
    sprite('mg610_08', 6)	# 131577-131582
    gotoLabel(5)
    label(10)
    sprite('null', 32767)	# 131583-164349
    Unknown3032()
    Unknown3038(1)
    sprite('keep', 32767)	# 164350-197116
    enterState('PersonaDeleteAndIdling')

@State
def mgef_450_mg_grab():

    def upon_IMMEDIATE():
        teleportRelativeX(128000)
    sprite('null', 16)	# 1-16
    GFX_1('mgef_450grab', 100)

@State
def mgef_450_aura():

    def upon_IMMEDIATE():
        Unknown1007(64000)
        GFX_2('mgef_450aura_bk')
        Unknown3001(0)
        Unknown3004(25)
    label(0)
    sprite('null', 2)	# 1-2
    GFX_1('mgef_450aura', 100)
    gotoLabel(0)

@State
def mgef_450_aura2():

    def upon_IMMEDIATE():
        pass
    label(0)
    sprite('null', 4)	# 1-4
    GFX_1('mgef_450aura_sub', 100)
    gotoLabel(0)

@State
def Win_TVnoise_off():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f74766e6f6973655f6f66662e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(1)
        Unknown3032()
        Unknown3001(0)
        Unknown6001(1)
        Unknown23032(45)
        Unknown23033(80)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 80)	# 1-80
    Unknown3004(40)
    sprite('null', 5)	# 81-85
    Unknown23130(0, 5, 1)
    SFX_3('tv_off')
    SFX_3('tv_off')
    SFX_3('tv_off')
    SFX_3('tv_off')
    SFX_3('tv_off')
    SFX_3('tv_off')
    sprite('null', 32767)	# 86-32852

@State
def TV_OffBlack():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(3)
        Unknown3032()
        Unknown13044(1)
        Unknown23015(4)
        Unknown2007()
        Unknown1096(1500)
        Unknown6001(1)
        Unknown23032(75)
        Unknown23033(50)
        sendToLabelUpon(32, 0)
    sprite('vr_mg450_black', 120)	# 1-120
    Unknown3038(1)
    sprite('vr_mg450_black', 45)	# 121-165
    Unknown3038(0)
    sprite('vr_mg450_black', 10)	# 166-175
    GFX_0('TVnoise', 100)
    Unknown3004(-25)

@State
def TVnoise():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3032()
        Unknown23032(45)
        Unknown23033(80)
        Unknown4003('6d6765665f74766e6f6973652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 10)	# 1-10
    SFX_3('whitenoize_short')
    SFX_3('whitenoize_short')
    Unknown3001(0)
    Unknown3004(25)
    sprite('null', 5)	# 11-15
    sprite('null', 30)	# 16-45
    Unknown3004(-8)

@State
def mgef_450_mist():

    def upon_IMMEDIATE():
        pass
    sprite('null', 15)	# 1-15
    SFX_3('ad020')
    GFX_0('mgef_450_mist_a', 100)
    GFX_0('mgef_450_mist_3d', 100)
    GFX_0('mgef_450_mist_3d_2', 100)
    GFX_0('mgef_450_mist_b', 100)
    sprite('null', 60)	# 16-75
    sprite('null', 64)	# 76-139
    Unknown23029(3, 4507, 0)
    Unknown23029(2, 4508, 0)
    Unknown26('mgef_610_mist_a')

@State
def mgef_450_mist_a():

    def upon_IMMEDIATE():
        Unknown6001(1)
        Unknown23032(50)
        Unknown23033(50)
    label(0)
    sprite('null', 8)	# 1-8
    GFX_1('mgef_610mist_a', 100)
    gotoLabel(0)

@State
def mgef_450_mist_b():

    def upon_IMMEDIATE():
        teleportRelativeX(31000)
        Unknown1007(5000)
    sprite('null', 1)	# 1-1
    Unknown4054(9)
    Unknown4045('6d6765665f3631306d6973745f6200000000000000000000000000000000000064000000')

@State
def mgef_450_mist_3d():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f3631306d69737400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown6001(1)
        Unknown23032(50)
        Unknown23033(110)
        Unknown23015(1)
        Unknown3032()
        Unknown3013(0)
        Unknown3019(0)
        Unknown1056(1100)
        Unknown1064(880)
    sprite('null', 64)	# 1-64
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 40)	# 65-104
    Unknown3001(128)
    Unknown3004(0)
    sprite('null', 128)	# 105-232
    Unknown3004(-2)

@State
def mgef_450_mist_3d_2():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f3631306d69737432000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown6001(1)
        Unknown23032(50)
        Unknown23033(80)
        Unknown23015(15)
        Unknown3032()
        Unknown3013(0)
        Unknown3019(0)
        Unknown1056(-600)
        Unknown1064(400)
    sprite('null', 32)	# 1-32
    Unknown3001(0)
    Unknown3004(4)
    sprite('null', 92)	# 33-124
    Unknown3001(128)
    Unknown3004(0)
    sprite('null', 64)	# 125-188
    Unknown3004(-4)

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
def ad600_Cort():

    def upon_IMMEDIATE():
        Unknown1007(300000)
        Unknown3032()
    sprite('ad600_05z', 8)	# 1-8
    sprite('ad600_06z', 8)	# 9-16
    sprite('ad600_07z', 16)	# 17-32
    Unknown3004(-16)
    physicsXImpulse(-8000)
    setGravity(600)

@State
def adef_401aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 5)	# 1-5
    GFX_0('adef_401aura_sub', 100)
    gotoLabel(0)

@State
def adef_401aura_sub():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('null', 30)	# 1-30
    GFX_2('adef_401aura')

@State
def adef_601aura():

    def upon_IMMEDIATE():
        Unknown4007(2)
    label(0)
    sprite('null', 5)	# 1-5
    GFX_1('adef_401aura', 100)
    gotoLabel(0)

@State
def PAD_PersonaMatchWin():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23023()
        Unknown23184('030000006400000070a0feff204e000000000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        callSubroutine('PAD_CheckWarp')
        Unknown2053(1)
        Unknown2019(100)
        Unknown23022(1)
        Unknown23015(0)
        if random_(2, 0, 50):
            Unknown23029(3, 10004, 0)
            Unknown2037(1)

        def upon_43():
            if (SLOT_48 == 10003):
                sendToLabel(10)
    sprite('mg610_00', 6)	# 1-6
    sprite('mg610_01', 6)	# 7-12
    sprite('mg610_02', 6)	# 13-18
    sprite('mg610_00', 6)	# 19-24
    sprite('mg610_01', 6)	# 25-30
    sprite('mg610_02', 6)	# 31-36
    sprite('mg610_03', 6)	# 37-42
    sprite('mg610_04', 6)	# 43-48
    sprite('mg610_05', 6)	# 49-54
    ScreenShake(15000, 25000)
    Unknown8004(0, 1, 1)
    GFX_1('mgef_groundtsuki', 0)
    sprite('mg610_06', 6)	# 55-60
    sprite('mg610_07', 6)	# 61-66
    sprite('mg610_08', 6)	# 67-72
    sprite('mg610_06', 6)	# 73-78
    if SLOT_2:
        GFX_0('adef_DangerCaution', 104)
    else:
        GFX_0('mgef_610_mist', 100)
    sprite('mg610_07', 6)	# 79-84
    sprite('mg610_08', 6)	# 85-90
    sprite('mg610_06', 6)	# 91-96
    if (not SLOT_2):
        Unknown3032()
        Unknown3004(-7)
        Unknown23130(16711680, 60, 1)
        Unknown2035(1)
    sprite('mg610_07', 6)	# 97-102
    sprite('mg610_08', 6)	# 103-108
    sprite('mg610_06', 6)	# 109-114
    sprite('mg610_07', 6)	# 115-120
    sprite('mg610_08', 6)	# 121-126
    sprite('mg610_06', 6)	# 127-132
    sprite('mg610_07', 6)	# 133-138
    sprite('mg610_08', 6)	# 139-144
    if (not SLOT_2):
        Unknown3038(1)
    label(1)
    sprite('mg610_06', 6)	# 145-150
    sprite('mg610_07', 6)	# 151-156
    sprite('mg610_08', 6)	# 157-162
    gotoLabel(1)
    label(10)
    sprite('null', 32767)	# 163-32929
    Unknown3038(1)
    sprite('keep', 32767)	# 32930-65696
    enterState('PersonaDeleteAndIdling')

@State
def PAD_PersonaMatchWinMist():

    def upon_IMMEDIATE():
        callSubroutine('PersonaReset')
        Unknown23023()
        Unknown23184('030000006400000070a0feff204e000000000000000000000000000000000000')
        callSubroutine('PAD_AttackInit')
        callSubroutine('PAD_CheckWarp')
        Unknown2053(1)
        Unknown4019(3)
        Unknown2020(1)
        Unknown23022(1)
        Unknown23015(0)

        def upon_43():
            clearUponHandler(43)
            sendToLabel(10)
    sprite('mg610_00', 6)	# 1-6
    sprite('mg610_01', 6)	# 7-12
    sprite('mg610_02', 6)	# 13-18
    sprite('mg610_00', 6)	# 19-24
    sprite('mg610_01', 6)	# 25-30
    sprite('mg610_02', 6)	# 31-36
    sprite('mg610_03', 6)	# 37-42
    sprite('mg610_04', 6)	# 43-48
    sprite('mg610_05', 6)	# 49-54
    ScreenShake(15000, 25000)
    Unknown8004(0, 1, 1)
    GFX_1('mgef_groundtsuki', 0)
    sprite('mg610_06', 6)	# 55-60
    sprite('mg610_07', 6)	# 61-66
    sprite('mg610_08', 6)	# 67-72
    sprite('mg610_06', 6)	# 73-78
    GFX_0('mgef_610_mist', 100)
    sprite('mg610_07', 6)	# 79-84
    sprite('mg610_08', 6)	# 85-90
    sprite('mg610_06', 6)	# 91-96
    Unknown3032()
    Unknown3004(-7)
    Unknown23130(16711680, 60, 1)
    Unknown2035(1)
    sprite('mg610_07', 6)	# 97-102
    sprite('mg610_08', 6)	# 103-108
    sprite('mg610_06', 6)	# 109-114
    sprite('mg610_07', 6)	# 115-120
    sprite('mg610_08', 6)	# 121-126
    sprite('mg610_06', 6)	# 127-132
    sprite('mg610_07', 6)	# 133-138
    sprite('mg610_08', 6)	# 139-144
    Unknown3038(1)
    label(1)
    sprite('mg610_06', 6)	# 145-150
    sprite('mg610_07', 6)	# 151-156
    sprite('mg610_08', 6)	# 157-162
    gotoLabel(1)
    label(10)
    sprite('null', 32767)	# 163-32929
    Unknown3038(1)
    sprite('keep', 32767)	# 32930-65696
    enterState('PersonaDeleteAndIdling')

@State
def mgef_610_mist():

    def upon_IMMEDIATE():
        pass
    sprite('null', 15)	# 1-15
    SFX_3('ad020')
    GFX_0('mgef_610_mist_a', 100)
    GFX_0('mgef_610_mist_3d', 100)
    GFX_0('mgef_610_mist_3d_2', 100)
    GFX_0('mgef_610_mist_b', 100)
    sprite('null', 60)	# 16-75
    sprite('null', 64)	# 76-139
    Unknown23029(3, 10003, 0)
    Unknown21015('506572736f6e614d6174636800000000000000000000000000000000000000001327000000000000')
    Unknown26('mgef_610_mist_a')

@State
def mgef_610_mist_a():

    def upon_IMMEDIATE():
        Unknown6001(1)
        Unknown23057(50)
        Unknown23058(50)
    label(0)
    sprite('null', 8)	# 1-8
    GFX_1('mgef_610mist_a', 100)
    gotoLabel(0)

@State
def mgef_610_mist_b():

    def upon_IMMEDIATE():
        teleportRelativeX(31000)
        Unknown1007(5000)
    sprite('null', 1)	# 1-1
    Unknown4054(9)
    Unknown4045('6d6765665f3631306d6973745f6200000000000000000000000000000000000064000000')

@State
def mgef_610_mist_3d():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f3631306d69737400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown6001(1)
        Unknown23057(50)
        Unknown23058(110)
        Unknown23015(1)
        Unknown3032()
        Unknown3013(0)
        Unknown3019(0)
        Unknown1056(1250)
        Unknown1064(880)
    sprite('null', 64)	# 1-64
    Unknown3001(0)
    Unknown3004(2)
    sprite('null', 40)	# 65-104
    Unknown3001(128)
    Unknown3004(0)
    sprite('null', 128)	# 105-232
    Unknown3004(-2)

@State
def mgef_610_mist_3d_2():

    def upon_IMMEDIATE():
        Unknown4003('6d6765665f3631306d69737432000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown6001(1)
        Unknown23057(50)
        Unknown23058(80)
        Unknown23015(15)
        Unknown3032()
        Unknown3013(0)
        Unknown3019(0)
        Unknown1056(-600)
        Unknown1064(400)
    sprite('null', 32)	# 1-32
    Unknown3001(0)
    Unknown3004(4)
    sprite('null', 92)	# 33-124
    Unknown3001(128)
    Unknown3004(0)
    sprite('null', 64)	# 125-188
    Unknown3004(-4)

@State
def adef_DangerCaution():

    def upon_IMMEDIATE():
        pass
    sprite('null', 60)	# 1-60
    sprite('null', 5)	# 61-65
    Unknown23084(1)
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape', 100)
    Unknown36(1)
    Unknown23015(1)
    Unknown23057(0)
    Unknown23058(20)
    Unknown1072(30000)
    Unknown1110(256000, 0)
    Unknown1096(1000)
    Unknown35()
    sprite('null', 5)	# 66-70
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape2', 100)
    Unknown36(1)
    Unknown23015(1)
    Unknown23057(90)
    Unknown23058(0)
    Unknown1072(-45000)
    Unknown1110(-256000, 0)
    Unknown1096(1000)
    Unknown35()
    sprite('null', 5)	# 71-75
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape', 100)
    Unknown36(1)
    Unknown23015(1)
    Unknown23057(10)
    Unknown23058(100)
    Unknown1072(-20000)
    Unknown1110(256000, 0)
    Unknown1096(800)
    Unknown35()
    sprite('null', 5)	# 76-80
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape2', 100)
    Unknown36(1)
    Unknown23015(3)
    Unknown23057(100)
    Unknown23058(70)
    Unknown1072(20000)
    Unknown1110(-256000, 0)
    Unknown1096(1750)
    Unknown35()
    sprite('null', 5)	# 81-85
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape2', 100)
    Unknown36(1)
    Unknown23015(3)
    Unknown23057(100)
    Unknown23058(35)
    Unknown1072(-22500)
    Unknown1110(-256000, 0)
    Unknown1096(2400)
    Unknown35()
    sprite('null', 5)	# 86-90
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape', 100)
    Unknown36(1)
    Unknown23015(3)
    Unknown23057(20)
    Unknown23058(40)
    Unknown1072(-15000)
    Unknown1110(256000, 0)
    Unknown1096(1450)
    Unknown35()
    sprite('null', 5)	# 91-95
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape3', 100)
    sprite('null', 5)	# 96-100
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    SFX_3('cloth_h')
    GFX_0('adef_tape', 100)
    Unknown36(1)
    Unknown23015(1)
    Unknown23057(90)
    Unknown23058(110)
    Unknown1072(80000)
    Unknown1110(256000, 0)
    Unknown1096(1750)
    Unknown35()
    GFX_0('adef_tape', 100)
    Unknown36(1)
    Unknown23015(1)
    Unknown23057(0)
    Unknown23058(40)
    Unknown1072(-20000)
    Unknown1110(256000, 0)
    Unknown1096(700)
    Unknown35()
    sprite('null', 32767)	# 101-32867

@State
def adef_tape():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown4003('616465665f746170652e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown6001(1)
        sendToLabelUpon(32, 0)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 16)	# 2-17
    Unknown3001(255)
    sprite('null', 32767)	# 18-32784
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown4003('616465665f746170655f656e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def adef_tape2():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown4003('616465665f74617065322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown6001(1)
        sendToLabelUpon(32, 0)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 16)	# 2-17
    Unknown3001(255)
    sprite('null', 32767)	# 18-32784
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown4003('616465665f74617065325f656e642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def adef_tape3():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown4003('616465665f74617065332e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown6001(1)
        Unknown23057(50)
        Unknown23058(50)
        Unknown23015(3)
        Unknown1072(20000)
        Unknown1096(1500)
        sendToLabelUpon(32, 0)
    sprite('null', 1)	# 1-1
    Unknown3001(0)
    sprite('null', 16)	# 2-17
    Unknown3001(255)
    sprite('null', 32767)	# 18-32784
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown4003('616465665f74617065335f656e642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')