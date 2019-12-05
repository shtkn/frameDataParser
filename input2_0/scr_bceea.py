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
def EMB_CE():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f43452e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-16776961, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 10)
    Unknown3025(-1, 10)
    sprite('null', 10)
    Unknown3025(-8342273, 10)
    sprite('null', 79)

@State
def EMB_CE_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f43452e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
    sprite('null', 8)
    Unknown3026(-16777216)
    Unknown3025(-1, 10)
    sprite('null', 8)
    Unknown3025(-8342273, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 8)
    Unknown3025(-16744193, 10)
    sprite('null', 79)

@State
def EMB_CE_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown2054(1)
        Unknown4003('65665f656d625f43452e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(5)
    sprite('null', 10)
    Unknown3026(-16777216)
    Unknown3025(-65536, 10)
    sprite('null', 10)
    Unknown3025(-55256, 10)
    sprite('null', 10)
    Unknown3025(-19276, 10)
    sprite('null', 10)
    Unknown3025(-65536, 10)
    sprite('null', 79)

@State
def RecoveryCapa():

    def upon_IMMEDIATE():
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            Unknown23151(3, 103)
        Unknown48('19000000020000000200000003000000020000009e000000')
        if (not SLOT_2):
            Unknown13(25)
    label(0)
    sprite('null', 10)
    GFX_0('RecoveryCapa_buff', 100)
    GFX_0('RecoveryCapa_aura', 100)
    sprite('null', 10)
    GFX_0('RecoveryCapa_aura', 100)
    sprite('null', 10)
    GFX_0('RecoveryCapa_aura', 100)
    gotoLabel(0)

@State
def RecoveryCapa_buff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        GFX_2('ceef_RecoveryCapa_buff')
    sprite('null', 60)

@State
def RecoveryCapa_aura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(3)
        GFX_2('ceef_RecoveryCapa_aura')
    sprite('null', 15)
    sprite('null', 15)
    Unknown4007(0)

@Subroutine
def MV_ActReset():
    Unknown2009()
    DisableAttackRestOfMove()
    teleportRelativeY(0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    EnableCollision(0)
    Unknown4019(3)
    Unknown2019(0)
    Unknown2020(1)
    Unknown23022(1)
    Unknown2054(1)
    Unknown4026(1)
    Unknown23078(1)
    Unknown23126(1)
    Unknown23042()

    def upon_48():
        if (not SLOT_4):
            Unknown3038(1)
            Unknown2001()
        else:
            Unknown3038(0)

    def upon_CLEAR_OR_EXIT():
        Unknown23023()
        if (not SLOT_51):
            if SLOT_36:
                Unknown2071('0300000000000000000000001900000000000000')
            else:
                Unknown2071('030000006079feff000000001900000000000000')
        else:
            if (SLOT_52 == 1):
                if SLOT_36:
                    Unknown2071('0300000000000000000000000500000000000000')
                else:
                    Unknown2071('030000006079feff000000000500000000000000')
            if (SLOT_52 == 2):
                if SLOT_36:
                    Unknown2071('0300000000000000000000003200000000000000')
                else:
                    Unknown2071('030000006079feff000000003200000000000000')
            if (SLOT_52 == 3):
                if SLOT_36:
                    Unknown2071('0300000000000000000000006400000000000000')
                else:
                    Unknown2071('030000006079feff000000006400000000000000')
            if (SLOT_52 == 4):
                Unknown1086(3)
    callSubroutine('MinervaSignalSetup')

@Subroutine
def MV_AtkInit():
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    AttackP1(100)
    Unknown11056(3)
    Unknown4009(3)
    Unknown23059(1)
    DisableAttackRestOfMove()

@Subroutine
def MV_PushCollisionCheck():
    Unknown48('190000000200000039000000190000000200000013000000')
    Unknown48('19000000020000003a000000030000000200000013000000')
    if (SLOT_58 > SLOT_57):
        EnableCollision(1)
        Unknown2015(50)
        SLOT_51 = 1

@Subroutine
def MV_ChainAtkInit():
    if (not SLOT_6):
        Unknown1086(3)
        teleportRelativeX(-100000)
    else:
        SLOT_51 = 1
        Unknown59('19000000680000000300000068000000')
        if (SLOT_0 > 200000):
            Unknown48('190000000200000039000000190000000200000013000000')
            Unknown48('19000000020000003a000000030000000200000013000000')
            if (SLOT_58 > SLOT_57):
                Unknown1086(3)
                Unknown2006()
                teleportRelativeX(200000)

    def upon_11():
        SLOT_51 = 1

    def upon_31():
        if (SLOT_25 < 200000):
            teleportRelativeX(-50000)
        if (SLOT_18 == 2):
            SLOT_6 = 1
            clearUponHandler(31)

@State
def MinervaCreate():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown23022(1)
        Unknown1086(3)
        teleportRelativeX(-360000)
        teleportRelativeY(0)
        Unknown13043(-75000)
        Unknown2049(1)

        def upon_CLEAR_OR_EXIT():
            Unknown23023()
            physicsXImpulse(0)
            if (not SLOT_4):
                Unknown3038(1)
            else:
                Unknown3038(0)
    sprite('null', 1)
    sprite('mv000_00', 100)
    enterState('MinervaStand')

@Subroutine
def MinervaSignalSetup():

    def upon_43():
        if (SLOT_48 == 100):
            SLOT_6 = 0
            Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000020030000')
        if (SLOT_48 == 112):
            SLOT_6 = 0
            Unknown24('4d696e657276615374616e645265616374696f6e00000000000000000000000084030000')
        if (SLOT_48 == 101):
            SLOT_6 = 0
            Unknown24('4d696e657276615475726e00000000000000000000000000000000000000000084030000')
        if (SLOT_48 == 102):
            SLOT_6 = 0
            Unknown24('4d696e657276614657616c6b0000000000000000000000000000000000000000bc020000')
        if (SLOT_48 == 103):
            SLOT_6 = 0
            Unknown24('4d696e657276614257616c6b0000000000000000000000000000000000000000bc020000')
        if (SLOT_48 == 110):
            SLOT_6 = 0
            Unknown24('4d696e65727661486f6c6400000000000000000000000000000000000000000020030000')
        if (SLOT_48 == 111):
            SLOT_6 = 0
            Unknown24('4d696e65727661536c6f77486f6d696e6700000000000000000000000000000020030000')
        if (SLOT_48 == 200):
            Unknown24('4d696e6572766141746b35420000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 201):
            Unknown24('4d696e6572766141746b36420000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 202):
            Unknown24('4d696e6572766141746b36430000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 203):
            Unknown24('4d696e6572766141746b41436f6d626f46696e69736800000000000000000000e8030000')
        if (SLOT_48 == 230):
            Unknown24('4d696e6572766141746b32420000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 231):
            Unknown24('4d696e6572766141746b33430000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 250):
            SLOT_6 = 0
            Unknown24('4d696e6572766141746b41495235430000000000000000000000000000000000e8030000')
        if (SLOT_48 == 251):
            SLOT_6 = 0
            Unknown24('4d696e6572766141746b41495235420000000000000000000000000000000000e8030000')
        if (SLOT_48 == 252):
            SLOT_6 = 0
            Unknown24('4d696e6572766141746b41697241737361756c74000000000000000000000000e8030000')
        if (SLOT_48 == 300):
            Unknown24('4d696e6572766141746b35430000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 301):
            Unknown24('4d696e6572766141746b32430000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 400):
            Unknown24('4d696e6572766141746b53686f744100000000000000000000000000000000004c040000')
        if (SLOT_48 == 401):
            Unknown24('4d696e6572766141746b53686f744200000000000000000000000000000000004c040000')
        if (SLOT_48 == 413):
            Unknown13(8)
        if (SLOT_48 == 402):
            Unknown24('4d696e6572766141746b53686f744558000000000000000000000000000000004c040000')
        if (SLOT_48 == 403):
            Unknown24('4d696e6572766141746b53686f745053000000000000000000000000000000004c040000')
        if (SLOT_48 == 404):
            Unknown24('4d696e657276615265636f7665727900000000000000000000000000000000004c040000')
        if (SLOT_48 == 405):
            Unknown24('4d696e657276615265636f76657279456e6400000000000000000000000000004c040000')
        if (SLOT_48 == 430):
            Unknown24('4d696e6572766141746b556c74696d61746553686f7400000000000000000000dc050000')
        if (SLOT_48 == 431):
            Unknown24('4d696e6572766141746b556c74696d61746553686f7453500000000000000000dc050000')
        if (SLOT_48 == 432):
            Unknown24('4d696e6572766141746b556c74696d61746553686f7444554f00000000000000dc050000')
        if (SLOT_48 == 433):
            Unknown24('4d696e6572766141746b556c74696d61746553686f7444554f53500000000000dc050000')
        if (SLOT_48 == 450):
            Unknown24('4d696e6572766141746b42757273744444000000000000000000000000000000dc050000')
        if (SLOT_48 == 500):
            SLOT_6 = 0
            Unknown24('4d696e6572766141746b41737472616c48656174000000000000000000000000d0070000')
        if (SLOT_48 == 600):
            Unknown24('4d696e65727661456e7472793031000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 601):
            Unknown24('4d696e65727661456e747279303146696e697368000000000000000000000000e8030000')
        if (SLOT_48 == 602):
            Unknown24('4d696e65727661456e7472793032000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 607):
            Unknown24('4d696e65727661456e7472793033000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 608):
            Unknown24('4d696e65727661456e747279303346696e697368000000000000000000000000e8030000')
        if (SLOT_48 == 609):
            Unknown24('4d696e657276614576656e7449646c6500000000000000000000000000000000e8030000')
        if (SLOT_48 == 610):
            Unknown24('4d696e657276614576656e7449646c6552657665727365000000000000000000e8030000')
        if (SLOT_48 == 611):
            Unknown24('4d696e657276614576656e74506f736500000000000000000000000000000000e8030000')
        if (SLOT_48 == 603):
            Unknown24('4d696e65727661526f756e6457696e0000000000000000000000000000000000e8030000')
        if (SLOT_48 == 604):
            Unknown24('4d696e6572766157696e30310000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 605):
            Unknown24('4d696e6572766157696e30320000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 606):
            Unknown24('4d696e657276614c6f7365000000000000000000000000000000000000000000e8030000')
        if (SLOT_48 == 999):
            if SLOT_51:
                SLOT_51 = 0
                SLOT_52 = 0
                SLOT_53 = 0
            if (not SLOT_4):
                if (not Unknown64(3)):
                    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000084030000')

@State
def MinervaStand():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_6 = 0
        Unknown1086(3)
        teleportRelativeX(-100000)
    label(0)
    sprite('mv000_00', 7)
    Unknown2071('030000006079feff000000001400000000000000')
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    loopRest()
    gotoLabel(0)

@State
def MinervaStandReaction():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        SLOT_52 = 3
    sprite('mv001_00', 6)
    sprite('mv001_00ex00', 6)
    sprite('mv001_00ex01', 6)
    sprite('mv001_00ex02', 6)
    sprite('mv001_01', 6)
    sprite('mv001_02', 6)
    label(10)
    sprite('mv001_02ex00', 6)
    sprite('mv001_02ex01', 6)
    sprite('mv001_02ex02', 6)
    sprite('mv001_02ex03', 6)
    sprite('mv001_02ex04', 6)
    sprite('mv001_02ex05', 6)
    sprite('mv001_02ex06', 6)
    gotoLabel(10)

@State
def MinervaTurn():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv000_00ex00', 1)
    Unknown2071('030000006079feff000000001400000000000000')
    sprite('mv003_00', 2)
    sprite('mv003_01', 3)
    sprite('mv003_00ex', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaFWalk():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv030_00', 7)
    Unknown2071('030000006079feff000000001400000000000000')
    label(0)
    sprite('mv030_01', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_02', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_03', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_04', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_05', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_06', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    loopRest()
    gotoLabel(0)

@State
def MinervaBWalk():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv031_00', 7)
    Unknown2071('030000006079feff000000001400000000000000')
    label(0)
    sprite('mv031_01', 7)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_02', 7)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_03', 7)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_04', 7)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_05', 7)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_06', 7)
    loopRest()
    gotoLabel(0)

@State
def MinervaHold():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
    label(0)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    loopRest()
    gotoLabel(0)

@State
def MinervaSlowHoming():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        SLOT_52 = 1

        def upon_45():
            teleportRelativeY(0)
    sprite('mv030_00', 2)
    label(0)
    sprite('mv030_01', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_02', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_03', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_04', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_05', 7)
    GFX_1('ceef_arukieff00', 0)
    GFX_1('ceef_arukieff00', 1)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)

@State
def dengeki_mv():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4019(2)
        Unknown2019(100)

        def upon_16():
            Unknown23016()
    label(0)
    sprite('ce082_00m', 2)
    sprite('ce082_01m', 2)
    loopRest()
    gotoLabel(0)

@State
def ceAirDashEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_airdash00')
        Unknown4003('636565665f6169726461736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1056(400)
        Unknown1064(300)
    sprite('null', 5)
    Unknown3001(230)
    GFX_0('ceAirDashEffNokosi', -1)
    sprite('null', 5)

@State
def ceAirDashEffNokosi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f34303065666630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1059(30)
        Unknown1096(300)
        Unknown3001(128)
    sprite('null', 10)
    GFX_1('ceef_airdash_nokosi2', -1)
    Unknown3004(-17)

@State
def ceAirBDashEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_airdash00')
        Unknown4003('636565665f6169726461736830312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1056(400)
        Unknown1064(300)
    sprite('null', 5)
    Unknown3001(230)
    GFX_0('ceAirDashEffNokosi', -1)
    sprite('null', 5)

@Subroutine
def MV_HitBack():
    Unknown9219(1)
    Unknown4007(3)

    def upon_STATE_END():
        Unknown4007(0)

@State
def MinervaAtk5B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(3)
        AirUntechableTime(22)
        AirPushbackY(20000)
        PushbackX(15300)
    sprite('mv201_00', 2)
    sprite('mv201_01', 2)
    physicsXImpulse(25000)
    SLOT_51 = 1
    SLOT_52 = 3
    sprite('mv201_02', 3)
    Unknown1019(50)
    SFX_0('004_swing_grap_1_1')
    SLOT_51 = 1
    SLOT_52 = 0
    callSubroutine('MV_PushCollisionCheck')
    sprite('mv201_03', 3)
    Unknown1019(50)
    RefreshMultihit()
    sprite('mv201_04', 2)
    Unknown1019(0)
    sprite('mv201_05', 4)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    sprite('mv201_06', 4)
    sprite('mv201_07', 4)
    SLOT_51 = 0
    sprite('mv201_08', 4)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtk5C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        callSubroutine('MV_PushCollisionCheck')
        AttackLevel_(4)
        Damage(900)
        AirPushbackY(15000)
        Unknown11092(1)
        hitstun(19)
        Unknown9016(1)
        Unknown11057(700)
        PushbackX(17000)
    sprite('mv202_00', 2)
    sprite('mv202_01', 3)
    sprite('mv202_02', 3)
    sprite('mv202_03', 2)
    physicsXImpulse(0)
    sprite('mv202_04', 2)
    Unknown1019(150)
    SFX_0('010_swing_sword_1')
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_06')
    sprite('mv202_05', 2)
    RefreshMultihit()
    AirPushbackY(15000)
    Unknown1019(25)
    GFX_0('mv202Eff', 100)
    sprite('mv202_06', 2)
    Unknown1019(0)
    sprite('mv202_07', 2)
    sprite('mv202_08', 2)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    Unknown26('mv202Eff')
    sprite('mv202_09', 2)
    sprite('mv202_10', 2)
    sprite('mv202_11', 2)
    sprite('mv202_12', 2)
    sprite('mv202_13', 4)
    SLOT_51 = 0
    sprite('mv202_14', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv202Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown2055(20)
        Unknown4061(1)
        Unknown23015(1)
        Unknown3032()
        Unknown3001(200)
        Unknown4003('636565665f32303265666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('mvef202eff_00', 3)
    GFX_0('mv213thunder', -1)
    Unknown36(1)
    Unknown1007(250000)
    teleportRelativeX(400000)
    Unknown1096(550)
    Unknown35()
    sprite('mvef202eff_01', 3)
    gotoLabel(0)

@State
def mv213thunder():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(700)
        Unknown3001(160)
        Unknown1077(-100000, 100000)
    sprite('null', 15)

@State
def MinervaAtk2B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(2)
        Damage(750)
        AttackP1(90)
        Unknown11092(1)
        PushbackX(5000)
        Unknown9016(1)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
    sprite('mv231_00', 2)
    sprite('mv231_01', 3)
    sprite('mv231_02', 3)
    sprite('mv231_03', 3)
    physicsXImpulse(25000)
    RefreshMultihit()
    SFX_0('010_swing_sword_0')
    SFX_0('004_swing_grap_1_0')
    SFX_3('cese_05')
    callSubroutine('MV_PushCollisionCheck')
    sprite('mv231_04', 3)
    RefreshMultihit()
    Unknown1019(25)
    sprite('mv231_05', 3)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    Unknown1019(0)
    sprite('mv231_06', 3)
    sprite('mv231_07', 3)
    SLOT_51 = 0
    sprite('mv231_08', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtk2C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        callSubroutine('MV_PushCollisionCheck')
        AttackLevel_(4)
        Damage(850)
        AirPushbackY(20000)
        AirPushbackX(-10000)
        PushbackX(-8000)
        Unknown9016(1)
        FatalCounter(1)
        Unknown11058('0000000001000000000000000000000000000000')
    sprite('mv232_00', 3)
    sprite('mv232_01', 4)
    sprite('mv232_02', 4)
    sprite('mv232_03', 2)
    SFX_0('010_swing_sword_1')
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_06')
    sprite('mv232_04', 3)
    RefreshMultihit()
    GFX_0('mv232Eff', -1)
    sprite('mv232_05', 2)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    sprite('mv232_06', 2)
    sprite('mv232_07', 2)
    sprite('mv232_08', 3)
    sprite('mv232_09', 3)
    SLOT_51 = 0
    sprite('mv232_10', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtk3C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        callSubroutine('MV_PushCollisionCheck')
        AttackLevel_(4)
        Unknown9016(1)
        HitLow(2)
        AttackP1(90)
        Unknown11058('0000000000000000010000000000000000000000')
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(20000)
        AirUntechableTime(40)
    sprite('mv236_00', 3)
    sprite('mv236_01', 3)
    sprite('mv236_02', 3)
    sprite('mv236_03', 3)
    SFX_0('010_swing_sword_1')
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_06')
    sprite('mv236_04', 3)
    RefreshMultihit()
    GFX_0('mv236Eff', -1)
    sprite('mv236_05', 3)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    sprite('mv236_06', 3)
    sprite('mv236_07', 3)
    sprite('mv236_08', 3)
    sprite('mv236_09', 3)
    SLOT_51 = 0
    sprite('mv236_10', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv236Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(192)
        Unknown3041(193)
        Unknown3043(194)
        Unknown3044(1)
        Unknown3001(140)
        Unknown23015(1)
    sprite('vr_ce236_00', 3)
    sprite('vr_ce236_00', 10)
    Unknown3004(-12)

@State
def MinervaAtk6B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(3)
        AirPushbackY(-60000)
        Unknown9190(1)
        Unknown9118(25)
        Unknown9016(1)
        AirUntechableTime(22)
        if Unknown23145('MinervaAtk5B'):
            teleportRelativeX(100000)
    sprite('mv211_00', 2)
    sprite('mv211_01', 3)
    sprite('mv211_02', 2)
    sprite('mv211_03', 2)
    sprite('mv211_04', 2)
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_05')
    physicsXImpulse(30000)
    callSubroutine('MV_PushCollisionCheck')

    def upon_45():
        if (SLOT_163 <= 150000):
            Unknown1019(0)
    sprite('mv211_05', 3)
    clearUponHandler(45)
    Unknown1019(50)
    RefreshMultihit()
    GFX_0('mv211Eff', -1)
    sprite('mv211_06', 3)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    Unknown1019(50)
    sprite('mv211_07', 3)
    Unknown1019(0)
    sprite('mv211_08', 3)
    sprite('mv211_09', 3)
    sprite('mv211_10', 3)
    SLOT_51 = 0
    sprite('mv211_11', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv211Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(192)
        Unknown3041(161)
        Unknown3043(162)
        Unknown3044(1)
        Unknown3001(100)
        Unknown23015(1)
    sprite('vr_ce211_00', 3)
    sprite('vr_ce211_01', 2)
    sprite('vr_ce211_02', 10)
    Unknown3004(-12)

@State
def MinervaAtk6C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        callSubroutine('MV_PushCollisionCheck')
        AttackLevel_(4)
        AirHitstunAnimation(10)
        AirPushbackY(25000)
        hitstun(21)
        AirUntechableTime(24)
        Unknown9016(1)
    sprite('mv212_00', 2)
    sprite('mv212_01', 2)
    sprite('mv212_02', 2)
    sprite('mv212_03', 3)
    sprite('mv212_04', 2)
    sprite('mv212_05', 2)
    sprite('mv212_06', 2)
    SFX_0('010_swing_sword_2')
    SFX_0('004_swing_grap_1_2')
    SFX_3('cese_06')
    sprite('mv212_07', 3)
    RefreshMultihit()
    GFX_0('mv212Eff', -1)
    sprite('mv212_08', 2)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    SLOT_51 = 0
    sprite('mv212_09', 2)
    sprite('mv212_10', 2)
    sprite('mv212_11', 4)
    sprite('mv212_12', 5)
    sprite('mv212_13', 3)
    sprite('mv212_14', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv212Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(192)
        Unknown3041(193)
        Unknown3043(194)
        Unknown3044(1)
        Unknown3001(140)
        Unknown23015(1)
    sprite('vr_ce212_00', 3)
    sprite('vr_ce212_01', 10)
    Unknown3004(-12)
    Unknown1007(-60000)

@State
def MinervaAtkAIR5B():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        SLOT_51 = 1
        SLOT_52 = 4
        SLOT_53 = 1
        Unknown9219(1)
        AttackLevel_(4)
        AttackP1(80)
        AirUntechableTime(24)
        Unknown9016(1)
        HitOverhead(2)
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('mv251_00', 2)
    Unknown1086(3)
    sprite('mv251_01', 3)
    sprite('mv251_02', 3)
    sprite('mv251_03', 3)
    RefreshMultihit()
    GFX_0('mv251Eff', -1)
    Unknown36(1)
    Unknown1007(40000)
    Unknown35()
    SFX_0('004_swing_grap_1_0')
    SFX_3('cese_05')
    sprite('mv251_04', 3)
    Unknown23029(3, 800, 0)
    Unknown2019(500)
    sprite('mv251_05', 3)
    sprite('mv251_06', 3)
    sprite('mv251_07', 3)
    sprite('mv251_08', 32767)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv251Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(192)
        Unknown3041(193)
        Unknown3043(194)
        Unknown3044(1)
        Unknown3001(140)
        Unknown23015(1)
    sprite('vr_ce251_00', 3)
    sprite('vr_ce251_01', 3)
    sprite('vr_ce251_02', 10)
    Unknown3004(-12)

@State
def MinervaAtkAIR5C():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        SLOT_51 = 1
        SLOT_52 = 4
        SLOT_53 = 1
        Unknown9219(1)
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(22)
        Hitstop(9)
        AirPushbackY(22000)
        Unknown9016(1)
        HitOverhead(2)
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('mv252_00', 2)
    Unknown1086(3)
    sprite('mv252_01', 3)
    sprite('mv252_02', 3)
    sprite('mv252_03', 3)
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_06')
    sprite('mv252_04', 2)
    RefreshMultihit()
    GFX_0('mv252Eff', -1)
    sprite('mv252_04', 2)
    StartMultihit()
    sprite('mv252_05', 2)
    RefreshMultihit()
    sprite('mv252_04', 2)
    Unknown23029(3, 800, 0)
    StartMultihit()
    sprite('mv252_06', 3)
    Unknown2019(500)
    sprite('mv252_07', 3)
    sprite('mv252_08', 3)
    sprite('mv252_09', 3)
    sprite('mv252_10', 32767)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv252Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        Unknown4009(3)
        Unknown3033()
        Unknown4061(1)
        Unknown3053(1)
        Unknown3040(2)
        Unknown3042(192)
        Unknown3041(193)
        Unknown3043(194)
        Unknown3044(1)
        Unknown3001(140)
        Unknown23015(1)
    sprite('vr_ce252_00', 3)
    sprite('vr_ce252_00', 10)
    Unknown3004(-12)

@State
def MinervaAtkAComboFinish():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_AtkInit')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
        AttackLevel_(4)
        Damage(650)
        Unknown11057(500)
        Hitstop(3)
        AirUntechableTime(100)
        Unknown9310(20)
        Unknown11092(1)
        PushbackX(20000)
        Unknown9016(1)
        Unknown11050('02000000636565665f686974656666343430000000000000000000000000000000000000')
        Unknown11044(1)
    sprite('mv212_08ex01', 2)
    sprite('mv212_09ex01', 2)
    sprite('mv212_10ex01', 1)
    sprite('mv212_11ex01', 1)
    sprite('mv403_00ex01', 2)
    physicsXImpulse(1000)
    callSubroutine('MV_PushCollisionCheck')
    sprite('mv403_01ex01', 2)
    sprite('mv403_02ex01', 3)
    sprite('mv440_00', 3)
    GFX_0('ce440EffMato', -1)
    Unknown1019(200)
    sprite('mv440_01', 3)
    Unknown1019(800)
    SFX_3('cese_10')
    sprite('mv440_02', 1)
    RefreshMultihit()
    Unknown1019(50)
    GFX_0('mv403ConsentEff', 0)
    Unknown36(1)
    Unknown1073(90000)
    Unknown35()
    GFX_0('mv440Eff', -1)
    sprite('mv440_02', 1)
    RefreshMultihit()
    sprite('mv440_02', 1)
    RefreshMultihit()
    sprite('mv440_02', 1)
    RefreshMultihit()
    sprite('mv440_02', 1)
    RefreshMultihit()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackX(50000)
    AirPushbackY(18000)
    Hitstop(10)
    Unknown1019(50)
    Unknown30088(1)
    sprite('mv440_03', 3)
    Unknown23029(3, 800, 0)
    EnableCollision(0)
    Unknown26('ce440EffMato')
    Unknown21012('6d7634343045666600000000000000000000000000000000000000000000000020000000')
    sprite('mv440_04', 3)
    sprite('mv440_05', 3)
    sprite('mv202_09ex01', 4)
    Unknown1084(1)
    sprite('mv202_10ex01', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv202_11ex01', 5)
    sprite('mv202_12ex01', 5)
    sprite('mv202_13ex01', 5)
    sprite('mv202_14ex01', 5)
    sprite('mv031_00', 3)
    SLOT_51 = 0
    sprite('mv031_01', 5)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_02', 5)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_03', 5)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_04', 5)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_05', 5)
    GFX_1('ceef_barukieff00', 0)
    GFX_1('ceef_barukieff00', 1)
    sprite('mv031_06', 5)
    loopRest()
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def ce440EffMato():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        teleportRelativeX(600000)
        Unknown1007(250000)
    label(0)
    sprite('null', 3)
    GFX_0('ce440EffCircle', -1)
    GFX_0('ce440EffCircle2', -1)
    Unknown36(1)
    Unknown1097(-200)
    Unknown35()
    gotoLabel(0)

@State
def ce440EffCircle():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f343430636972636c650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 7)
    physicsXImpulse(-17500)
    sprite('null', 10)
    physicsXImpulse(-8750)
    Unknown1099(120)
    Unknown3004(-26)

@State
def ce440EffCircle2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f343430636972636c650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 7)
    physicsXImpulse(-35000)
    sprite('null', 10)
    Unknown3004(-26)

@State
def mv440Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4003('636565665f3231336566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1064(840)
        Unknown1056(480)
        Unknown3001(200)
        Unknown1072(-90000)
        Unknown1007(200000)
        teleportRelativeX(525000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 1)
    GFX_0('mv440EffSub', -1)
    GFX_1('ceef440_cmnHit01', -1)
    Unknown1097(200)
    sprite('null', 1)
    Unknown1097(-200)
    sprite('null', 1)
    Unknown1097(200)
    sprite('null', 1)
    Unknown1097(-200)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    sprite('null', 5)
    Unknown3004(-51)

@State
def mv440EffSub():

    def upon_IMMEDIATE():
        Unknown1007(-210000)
        teleportRelativeX(-100000)
    sprite('null', 30)
    Unknown1099(120)
    physicsXImpulse(-30000)
    GFX_2('ceef_233shock00')

@State
def ceef_hiteff440():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(35000)
        Unknown1096(1200)
        Unknown1062(200, 800)
        Unknown1077(15000, 45000)
        Unknown23015(11)
        Unknown3001(255)
        teleportRelativeX(75000)
        Unknown3033()
    sprite('vr_mvcmneff_00', 2)
    GFX_0('ceef_hiteff440sub', -1)
    sprite('vr_mvcmneff_01', 2)
    Unknown3004(-8)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def ceef_hiteff440sub():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(35000)
        Unknown1096(1200)
        Unknown1062(200, 800)
        Unknown1077(-45000, -15000)
        Unknown23015(11)
        Unknown3001(255)
        Unknown3033()
    sprite('vr_mvcmneff_00', 2)
    sprite('vr_mvcmneff_01', 2)
    Unknown3004(-8)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def ceef_hiteff440End():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(2500)
        Unknown23015(11)
        teleportRelativeX(-500000)
        Unknown3033()
    sprite('vr_mvcmneff3_00', 3)
    Unknown1067(-30)
    Unknown1059(30)
    sprite('vr_mvcmneff3_01', 3)
    sprite('vr_mvcmneff3_02', 3)
    sprite('vr_mvcmneff3_03', 3)
    sprite('vr_mvcmneff3_04', 3)
    sprite('vr_mvcmneff3_05', 3)
    sprite('vr_mvcmneff3_06', 3)
    Unknown3004(-26)
    sprite('vr_mvcmneff3_07', 3)
    sprite('vr_mvcmneff3_08', 3)

@State
def ceef_hiteff440HitEx():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown2054(1)
        Unknown2005()
        Unknown1096(1500)
        Unknown4003('636565665f3434306869743030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        teleportRelativeX(-400000)
        Unknown1007(280000)
    sprite('null', 5)
    GFX_1('ceef_tamebeam_end2', -1)
    sprite('null', 5)
    Unknown1099(200)
    Unknown3004(-51)

@State
def mv203Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('636565665f3230336566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1056(725)
        Unknown1064(650)
        teleportRelativeX(25000)
        Unknown1007(-25000)
        Unknown3001(210)
    sprite('null', 3)
    sprite('null', 5)
    Unknown4003('636565665f32303365666630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3004(-26)

@State
def mv340ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_208_plugeff_thunder')
        sendToLabelUpon(32, 1)
    sprite('null', 32767)
    label(1)
    sprite('null', 5)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-51)
    Unknown1099(30)

@State
def ceef_hiteffD():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(35000)
        Unknown1096(1200)
        Unknown1062(0, 250)
        Unknown1077(-25000, 30000)
        Unknown23015(1)
        Unknown3001(200)
        Unknown3033()
    sprite('vr_mvcmneff_00', 4)
    GFX_1('ceef_cmnHit01', -1)
    GFX_0('ceef_hiteffDSub', -1)
    sprite('vr_mvcmneff_01', 3)
    Unknown3004(-8)
    sprite('vr_mvcmneff_02', 3)
    sprite('vr_mvcmneff_03', 3)
    sprite('vr_mvcmneff_04', 3)
    sprite('vr_mvcmneff_05', 3)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def ceef_hiteffDSub():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(90000)
        Unknown1096(1300)
        Unknown1062(0, 500)
        Unknown1077(-15000, 15000)
        Unknown23015(1)
        Unknown3001(200)
        Unknown3033()
    sprite('vr_mvcmneff_00', 2)
    sprite('vr_mvcmneff_01', 2)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def mv214Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('636565665f3231346566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1050)
        Unknown3001(255)
        teleportRelativeX(260000)
    sprite('null', 1)
    sprite('null', 2)
    GFX_0('mv214thunder', -1)
    Unknown36(1)
    Unknown1096(400)
    teleportRelativeX(150000)
    Unknown1007(150000)
    Unknown35()
    GFX_0('mv214thunder', -1)
    Unknown36(1)
    Unknown1096(600)
    teleportRelativeX(150000)
    Unknown1007(315000)
    Unknown35()
    GFX_0('mv214thunder', -1)
    Unknown36(1)
    Unknown1096(600)
    teleportRelativeX(-30000)
    Unknown1007(420000)
    Unknown35()
    GFX_0('mv214thunder', -1)
    Unknown36(1)
    Unknown1096(400)
    teleportRelativeX(-240000)
    Unknown1007(420000)
    Unknown35()
    sprite('null', 1)
    sprite('null', 3)
    Unknown4003('636565665f3231346566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3004(-26)

@State
def mv214thunder():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(700)
        Unknown3001(160)
        Unknown1077(-100000, 100000)
    sprite('null', 15)

@State
def mv233Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(3)
    sprite('null', 20)
    GFX_2('ceef_233shock00')

@State
def mv213Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('636565665f3231336566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(700)
        Unknown3001(255)
        Unknown1072(-15000)
        Unknown1007(100000)
    sprite('null', 3)
    GFX_1('ceef_healsphere01', -1)
    GFX_0('mv213thunder', -1)
    sprite('null', 3)
    GFX_0('mv213thunder', -1)

@State
def mv213thunder():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(700)
        Unknown3001(160)
        Unknown1077(-100000, 100000)
    sprite('null', 15)

@State
def mv204Smoke():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(10000)
        Unknown3001(255)
        Unknown1056(700)
        Unknown1064(450)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-17)

@State
def mv204ringLoops():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2055(30)
    label(0)
    sprite('null', 2)
    GFX_0('mv204ring', -1)
    GFX_1('ceef_kiramove00', -1)
    gotoLabel(0)

@State
def mv204ring():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4061(1)
        Unknown2054(1)
    sprite('vr_mvef204_00', 10)
    physicsXImpulse(-7500)
    Unknown1099(60)
    Unknown3004(-26)

@State
def mv234Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('636565665f3233346566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(4000)
        Unknown1007(30000)
        Unknown3001(255)
    sprite('null', 2)
    sprite('null', 10)
    Unknown4003('636565665f3233346566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3004(-26)

@State
def mv234ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_208_plugeff_thunder')
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
        Unknown1073(180000)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    teleportRelativeX(-50000)
    Unknown1007(10000)
    label(1)
    sprite('null', 5)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-51)
    Unknown1099(30)

@State
def mv205ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_205_plugeff_bigc')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-26)
    Unknown1099(30)

@State
def ceef_270():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('ceef_270ring')
    sprite('null', 60)

@State
def ceef_healjunbieff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('ceef_healjunbieff')
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    GFX_1('ceef_healtameendeff', -1)
    Unknown3004(-17)

@State
def ceef_HealJunbiAnim_L():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(1200)
        Unknown1070(0, 450)
        Unknown1010(0, 150000)
        Unknown2019(100)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(3)
    sprite('vr_ce432a_00', 5)
    Unknown3004(-4)
    sprite('vr_ce432a_01', 5)
    sprite('vr_ce432a_02', 5)
    sprite('vr_ce432a_03', 5)
    sprite('vr_ce432a_04', 5)
    sprite('vr_ce432a_05', 4)
    sprite('vr_ce432a_06', 4)
    sprite('vr_ce432a_07', 3)
    sprite('vr_ce432a_08', 3)

@State
def ceef_HealJunbiAnim_R():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4061(1)
        Unknown1096(1200)
        Unknown1070(0, 450)
        Unknown1010(-150000, 0)
        Unknown2019(100)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3071(2)
        Unknown3072('80000000000000000000000000000000')
    sprite('vr_ce432a_00', 5)
    Unknown3004(-4)
    SFX_3('cese_02')
    sprite('vr_ce432a_01', 5)
    sprite('vr_ce432a_02', 5)
    sprite('vr_ce432a_03', 5)
    sprite('vr_ce432a_04', 5)
    sprite('vr_ce432a_05', 4)
    sprite('vr_ce432a_06', 4)
    sprite('vr_ce432a_07', 3)
    sprite('vr_ce432a_08', 3)

@State
def SuperHealEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('636565665f73757065726865616c65666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1007(500000)
        teleportRelativeX(40000)
        Unknown3032()
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    GFX_0('ceCmnHealAura', -1)
    Unknown36(1)
    Unknown1097(500)
    Unknown35()
    GFX_1('ceef_healsphere_start', 100)
    GFX_0('SuperHealEff2', -1)
    GFX_0('SuperHealEff3', -1)
    Unknown1096(100)
    Unknown1099(100)
    SFX_3('cese_03')
    label(0)
    sprite('null', 1)
    GFX_0('ceCmnHealAura', -1)
    Unknown36(1)
    Unknown1097(500)
    teleportRelativeX(70000)
    Unknown35()
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown21012('53757065724865616c456666320000000000000000000000000000000000000020000000')
    Unknown21012('53757065724865616c456666330000000000000000000000000000000000000020000000')
    Unknown3004(-26)
    Unknown1099(30)
    sprite('null', 5)
    loopRest()

@State
def SuperHealEff2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('636565665f73757065726865616c65666630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(1300)
        teleportRelativeX(90000)
        sendToLabelUpon(32, 1)
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(17)
    sprite('null', 32767)
    GFX_2('ceef_superheal01')
    label(1)
    sprite('null', 20)
    Unknown3004(-17)
    loopRest()

@State
def SuperHealEff3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('ceef_healaura00')
        Unknown2054(1)
        sendToLabelUpon(32, 0)
        Unknown1096(800)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    GFX_1('ceef_healauraend2', -1)
    Unknown3004(-26)

@State
def ceCmnHealAura():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e6865616c61757261303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1077(-15000, 10000)
        Unknown3032()
        Unknown1096(650)
        Unknown2054(1)
    sprite('null', 58)
    Unknown3004(-3)
    Unknown1099(10)
    physicsYImpulse(500)

@State
def ceef_hiteffH():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(15000)
        Unknown1096(1300)
        Unknown1062(0, 250)
        Unknown1077(-25000, 25000)
        Unknown23015(1)
        Unknown3033()
    sprite('vr_mvcmneff_00', 4)
    Unknown4049(1100)
    Unknown4045('636565665f636d6e486974303100000000000000000000000000000000000000ffffffff')
    GFX_0('ceef_hiteffDSub2', -1)
    sprite('vr_mvcmneff_01', 3)
    Unknown3004(-8)
    GFX_0('ceef_hiteffHSub', -1)
    sprite('vr_mvcmneff_02', 3)
    sprite('vr_mvcmneff_03', 3)
    sprite('vr_mvcmneff_04', 3)
    sprite('vr_mvcmneff_05', 3)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def ceef_hiteffHSub():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(90000)
        Unknown1096(1600)
        Unknown1062(0, 500)
        Unknown1077(-15000, 15000)
        Unknown23015(1)
        Unknown3033()
    sprite('vr_mvcmneff_00', 2)
    sprite('vr_mvcmneff_01', 2)
    sprite('vr_mvcmneff_02', 2)
    sprite('vr_mvcmneff_03', 2)
    sprite('vr_mvcmneff_04', 2)
    sprite('vr_mvcmneff_05', 2)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def ceef_hiteffDSub2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(90000)
        Unknown1056(900)
        Unknown1064(1300)
        Unknown1062(0, 500)
        Unknown1077(-15000, 15000)
        Unknown23015(1)
        Unknown3033()
        Unknown3001(180)
    sprite('vr_mvcmneff2_00', 2)
    GFX_0('ceef_hiteffDSub3', -1)
    sprite('vr_mvcmneff2_01', 2)
    sprite('vr_mvcmneff2_02', 2)
    sprite('vr_mvcmneff2_03', 2)
    sprite('vr_mvcmneff2_04', 2)
    sprite('vr_mvcmneff2_05', 2)
    sprite('vr_mvcmneff2_06', 3)
    sprite('vr_mvcmneff2_07', 3)
    sprite('vr_mvcmneff2_08', 2)

@State
def ceef_hiteffDSub3():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1056(1600)
        Unknown1064(1800)
        Unknown1062(0, 250)
        Unknown1077(-15000, 15000)
        Unknown23015(1)
        Unknown3001(180)
        Unknown3033()
    sprite('vr_mvcmneff2_00', 2)
    sprite('vr_mvcmneff2_01', 2)
    sprite('vr_mvcmneff2_02', 2)
    sprite('vr_mvcmneff2_03', 2)
    sprite('vr_mvcmneff2_04', 2)
    sprite('vr_mvcmneff2_05', 2)
    sprite('vr_mvcmneff2_06', 3)
    sprite('vr_mvcmneff2_07', 3)
    sprite('vr_mvcmneff2_08', 2)

@State
def mv401tameMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown1007(300000)
        teleportRelativeX(10000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 7)
    GFX_0('mv401tame', -1)
    GFX_1('ceef_401tame_sub', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 7)
    GFX_0('mv401tame', -1)
    GFX_1('ceef_401tame_sub', -1)
    sprite('null', 7)
    GFX_1('ceef_401tame_sub', -1)

@State
def mv401tame():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(800)
        Unknown1077(-100000, 100000)
    sprite('null', 15)

@State
def mv205Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('636565665f3230356566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown2054(1)
        Unknown1007(260000)
        teleportRelativeX(-70000)
        Unknown3001(160)
        Unknown1056(800)
    sprite('null', 2)
    sprite('null', 8)

@State
def MinervaAtkShotA():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
    sprite('mv403_00', 2)
    sprite('mv403_02', 2)
    GFX_0('mv403ConsentEff', 0)
    sprite('mv403_03', 1)
    sprite('mv403_04', 1)
    sprite('mv403_05', 2)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_06', 2)
    sprite('mv403_07', 2)
    sprite('mv403_08', 3)
    GFX_0('ShotAtkObj', 0)
    Unknown38(8, 1)
    Unknown23029(1, 410, 0)
    sprite('mv403_09', 3)
    sprite('mv403_10', 3)
    sprite('mv403_11', 3)
    sprite('mv403_12', 3)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_13', 3)
    SLOT_51 = 0
    sprite('mv403_15', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtkShotB():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
    sprite('mv403_00', 2)
    sprite('mv403_02', 2)
    GFX_0('mv403ConsentEff', 0)
    sprite('mv403_03', 1)
    sprite('mv403_04', 1)
    sprite('mv403_05', 2)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_06', 2)
    sprite('mv403_07', 2)
    sprite('mv403_08', 3)
    GFX_0('ShotAtkObj', 0)
    Unknown38(8, 1)
    Unknown23029(1, 411, 0)
    sprite('mv403_09', 3)
    sprite('mv403_10', 3)
    sprite('mv403_11', 3)
    sprite('mv403_12', 3)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_13', 3)
    SLOT_51 = 0
    sprite('mv403_15', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtkShotEX():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
    sprite('mv403_00', 3)
    sprite('mv403_02', 3)
    GFX_0('mv403ConsentEff', 0)
    sprite('mv403_03', 2)
    sprite('mv403_04', 2)
    sprite('mv403_05', 3)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_06', 2)
    sprite('mv403_07', 2)
    sprite('mv403_08', 3)
    GFX_0('ExShotMasterObj', -1)
    Unknown23029(1, 412, 0)
    sprite('mv403_09', 3)
    sprite('mv403_10', 3)
    sprite('mv403_11', 3)
    sprite('mv403_12', 3)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_13', 3)
    SLOT_51 = 0
    sprite('mv403_15', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtkShotPS():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        callSubroutine('MV_ChainAtkInit')
        callSubroutine('MV_HitBack')
    sprite('mv403_00', 3)
    sprite('mv403_02', 3)
    GFX_0('mv403ConsentEff', 0)
    sprite('mv403_03', 3)
    sprite('mv403_04', 3)
    sprite('mv403_05', 3)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_06', 3)
    GFX_0('mv403PSTameEff', -1)
    sprite('mv403_07', 40)
    sprite('mv403_07', 3)
    Unknown21012('6d76343033505354616d6545666600000000000000000000000000000000000020000000')
    sprite('mv403_08', 3)
    GFX_0('ExShotMasterObj', -1)
    Unknown23029(1, 413, 0)
    sprite('mv403_09', 3)
    sprite('mv403_10', 3)
    sprite('mv403_11', 3)
    sprite('mv403_12', 3)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_13', 6)
    SLOT_51 = 0
    sprite('mv403_15', 6)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv403PSTameEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown2054(1)
        GFX_2('ceef_tamebeam_00')
        sendToLabelUpon(32, 1)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('02000000801a0600503403006400000000000000')
    label(0)
    sprite('null', 3)
    Unknown1096(1200)
    Unknown1077(0, 100000)
    sprite('null', 3)
    Unknown1062(0, 250)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    GFX_1('ceef_tamebeam_end', -1)
    GFX_1('ceef_beamstart00', -1)

@State
def mv403ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_208_plugeff_thunder')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-26)
    Unknown1099(30)

@State
def ShotAtkObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown53(1)
        Unknown4061(1)
        AttackLevel_(3)
        Damage(1500)
        AttackP1(80)
        Hitstop(0)
        Unknown11001(6, 6, 8)
        Unknown11056(2)
        AirUntechableTime(33)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(24000)
        Unknown2019(-500)
        Unknown1007(-70000)
        Unknown1096(800)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0

        def upon_17():
            sendToLabel(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
        sendToLabelUpon(54, 2)

        def upon_43():
            if (SLOT_48 == 410):
                Unknown30070('53686f7441746b41000000000000000000000000000000000000000000000000')
                loopRelated(17, 50)
            if (SLOT_48 == 411):
                Unknown30070('53686f7441746b42000000000000000000000000000000000000000000000000')
                loopRelated(17, 80)
                Unknown2037(1)
        DisableAttackRestOfMove()
    sprite('vrceef999_99test', 5)
    Unknown1099(40)
    physicsXImpulse(1000)
    GFX_0('mv403Nokosistart', 100)
    GFX_0('mv403ShotEff', 100)
    Unknown3038(1)
    sprite('vrceef999_99test', 10)
    Unknown1096(1000)
    Unknown1099(0)
    RefreshMultihit()
    physicsXImpulse(43000)
    Unknown1028(-1000)
    if SLOT_2:
        physicsXImpulse(1000)
        Unknown1028(0)
    sprite('vrceef999_99test', 40)
    if SLOT_2:
        Unknown1028(5)
    sprite('vrceef999_99test', 10)
    if SLOT_2:
        Unknown1028(3000)
    label(0)
    sprite('vrceef999_99test', 6)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vrceef999_99test2', 3)
    Unknown21012('6d7634303353686f74456666000000000000000000000000000000000000000020000000')
    clearUponHandler(17)
    physicsXImpulse(0)
    Unknown1028(0)
    ExitState()
    label(2)
    sprite('null', 10)
    Unknown21012('6d7634303353686f74456666000000000000000000000000000000000000000020000000')
    clearUponHandler(17)
    clearUponHandler(54)
    physicsXImpulse(0)
    Unknown1028(0)

@State
def mv403ShotEff():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b750000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        Unknown1007(75000)
        sendToLabelUpon(32, 1)
    sprite('null', 15)
    Unknown1096(100)
    Unknown1099(60)
    label(0)
    sprite('null', 3)
    Unknown1099(0)
    GFX_0('mv403Nokosi', 100)
    GFX_0('mv403Nokosi2', 100)
    GFX_0('mv403Nokosi3', 100)
    sprite('null', 3)
    GFX_0('mv403Nokosi3', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    GFX_1('ceef_shotbrake00', -1)
    loopRest()

@State
def mv403Nokosi():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e7061727469636c65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(30)
        Unknown1077(-10000, 10000)
        Unknown1011(-150000, 150000)
        Unknown2054(1)
    sprite('null', 10)
    Unknown1099(50)
    GFX_1('ceef_shot_01', -1)
    sprite('null', 10)
    Unknown1099(-10)
    sprite('null', 25)
    Unknown3004(-10)

@State
def mv403Nokosi2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e7061727469636c65303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown1096(30)
        Unknown1077(-10000, 10000)
        Unknown1011(-150000, 150000)
        Unknown2054(1)
    sprite('null', 10)
    Unknown1099(50)
    GFX_1('ceef_shot_01', -1)
    sprite('null', 10)
    Unknown1099(-10)
    sprite('null', 25)
    Unknown3004(-10)

@State
def mv403Nokosi3():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1077(-100000, 100000)
        Unknown1096(600)
    sprite('null', 14)
    Unknown3004(-7)
    Unknown1099(-7)
    physicsXImpulse(-6000)

@State
def mv403Nokosistart():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f7473746172743030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(800)
        Unknown1007(80000)
    sprite('null', 5)
    GFX_0('mv403Impact', 100)
    GFX_0('mv403Impact2', 100)
    Unknown1099(300)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1099(30)

@State
def mv403Impact():

    def upon_IMMEDIATE():
        Unknown4003('636565665f77696e64616e696d303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(-100000)
        Unknown1064(1250)
        Unknown1056(2000)
        Unknown3001(255)
    sprite('null', 5)
    Unknown1099(15)
    physicsXImpulse(-15000)
    sprite('null', 5)
    Unknown3004(-17)

@State
def mv403Impact2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f77696e64616e696d303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(-75000)
        Unknown1064(1000)
        Unknown1056(1800)
        Unknown3001(255)
    sprite('null', 5)
    sprite('null', 5)
    Unknown3004(-17)

@State
def ExShotMasterObj():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f33313165666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4011(3)
        Unknown1096(2000)
        teleportRelativeX(350000)
        Unknown1007(230000)
        Unknown2054(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 412):
                pass
            if (SLOT_48 == 413):
                Unknown2037(1)
    sprite('null', 1)
    SFX_3('cese_12')
    SFX_3('cese_08')
    sprite('null', 1)
    GFX_0('ShotAtkEx', -1)
    if SLOT_2:
        Unknown23029(1, 413, 0)
    else:
        Unknown23029(1, 412, 0)
    GFX_0('Unlimitedmv311ThunderEff', -1)
    GFX_0('Unlimitedmv311ThunderEff2', -1)
    GFX_0('Unlimitedmv311thunder', -1)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown35()
    GFX_0('Unlimitedmv311thunder2', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown35()
    GFX_0('Unlimitedmv311thunder', -1)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown35()
    GFX_0('Unlimitedmv311thunder2', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    sprite('null', 5)
    GFX_0('Unlimitedmv311thunder', -1)
    GFX_0('Unlimitedmv311BeamEnd', -1)
    ScreenShake(10000, 10000)
    Unknown1067(-350)
    Unknown1059(-300)

@State
def ShotAtkEx():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        Unknown9178(1)
        WallbounceReboundTime(10)
        AirHitstunAfterWallbounce(45)
        AirPushbackX(60000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(60)

        def upon_43():
            if (SLOT_48 == 412):
                Unknown30070('53686f7441746b45580000000000000000000000000000000000000000000000')
                callSubroutine('ExSkillInit')
                Damage(2400)
                AttackP2(85)
            if (SLOT_48 == 413):
                Unknown30070('53686f7441746b50530000000000000000000000000000000000000000000000')
                callSubroutine('PartnerSkillInit')
                Damage(2000)
        SLOT_5 = 1

        def upon_STATE_END():
            SLOT_5 = 0
    sprite('UnlimitedShot_B_Atk', 3)
    sprite('UnlimitedShot_B_Atk', 17)
    Unknown2003(1)

@State
def Unlimitedmv311ThunderEff():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown1073(-95000)
        Unknown1056(1250)
        Unknown1064(1500)
        Unknown1070(500, 2000)
        Unknown1062(0, 500)
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)

@State
def Unlimitedmv311ThunderEff2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown1073(-85000)
        Unknown1056(1250)
        Unknown1064(1500)
        Unknown1070(500, 2000)
        Unknown1062(0, 500)
        Unknown2019(-500)
        Unknown2054(1)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)

@State
def Unlimitedmv311thunder():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(700)
        Unknown4006(2)
        Unknown1077(-100000, 100000)
        Unknown2054(1)
    sprite('null', 6)
    Unknown3001(0)
    Unknown1099(15)
    sprite('null', 9)
    Unknown3001(255)
    GFX_1('ceef_healsphere01', -1)

@State
def Unlimitedmv311thunder2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(450)
        Unknown4006(2)
        Unknown1077(-100000, 100000)
        Unknown2054(1)
    sprite('null', 6)
    Unknown3001(0)
    sprite('null', 9)
    Unknown3001(255)
    GFX_1('ceef_healsphere01', -1)

@State
def Unlimitedmv311BeamEnd():

    def upon_IMMEDIATE():
        GFX_2('ceef_311beamend00')
        Unknown4006(2)
        Unknown2054(1)
    sprite('null', 60)

@State
def mv215ConsentEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown1072(90000)
        GFX_2('ceef_208_plugeff_thunder')
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    teleportRelativeX(-7500)
    label(1)
    sprite('null', 5)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-51)
    Unknown1099(30)

@State
def ce215JetEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_400_shock')
        Unknown4003('636565665f34303065666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(600)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 0)
    sprite('null', 5)
    GFX_0('ce215JetEffNokosi', -1)
    label(0)
    sprite('null', 5)
    GFX_0('ce215JetEffNokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)

@State
def ce215JetEffNokosi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f34303065666630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        Unknown1096(300)
        physicsXImpulse(-7500)
    sprite('null', 10)
    GFX_1('ceef_airdash_nokosi2', -1)
    Unknown3004(-26)

@State
def AssaultPlug():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
        Unknown23015(11)
        Unknown2019(100)
        teleportRelativeX(5000)
    sprite('vr_ce215_00', 32767)
    loopRest()
    label(1)
    sprite('vr_ce215_01', 32767)
    loopRest()
    label(2)
    sprite('vr_ce215_03', 10)
    Unknown3004(-25)
    loopRest()

@State
def Cable():

    def upon_IMMEDIATE():
        Unknown2053(1)
        Unknown23013(1)
        Unknown2015(10)
        Unknown4009(3)
        Unknown2055(240)
        Unknown2037(0)
        Unknown1108(0)
        Unknown48('010000000200000001000000190000000200000001000000')
        SLOT_57 = 109
        teleportRelativeX(-240000)
        Unknown1007(-21000)

        def upon_31():
            Unknown23030('4361626c654472617700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23030('4361626c656a6f696e74000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000')
        Unknown23015(0)
        Unknown23030('4361626c6552656e646572537461676500000000000000000000000000000000000000000b000000000000000b00000000000000000000000000000000000000')

        def upon_48():
            Unknown23030('4361626c6549646c696e670000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        SLOT_56 = 1

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                Unknown23030('4361626c65416e676c654279436861696e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            if SLOT_56:
                Unknown1108(0)
            Unknown48('190000000200000034000000030000000200000034000000')
            if (not SLOT_52):
                if (not SLOT_53):
                    Unknown13(25)

        def upon_32():
            clearUponHandler(32)
            Unknown1086(4)
            Unknown1007(120000)
            sendToLabel(100)
    sprite('null', 1)
    Unknown23030('4361626c65506172616d000000000000000000000000000000000000000000000000000000000000000000005a1e000000000000000000000000000000000000')
    Unknown23030('4361626c65506172616d00000000000000000000000000000000000000000000000000000100000000000000210000000000000000000000000000000a000000')
    Unknown23030('4361626c65506172616d00000000000000000000000000000000000000000000000000000200000000000000420000000000000000000000000000000a000000')
    Unknown23030('4361626c65506172616d000000000000000000000000000000000000000000000000000003000000000000005b1e000000000000000000000000000000000000')
    Unknown23030('4361626c6553706565640000000000000000000000000000000000000000000000000000b80b0000000000000000000000000000000000000000000000000000')
    Unknown23030('4361626c654669727374506f736974696f6e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)
    loopRest()
    label(100)
    sprite('vr_ce215_02', 30)
    Unknown23015(0)
    Unknown2019(100)
    clearUponHandler(41)
    Unknown23143(90000, 0, 80)
    SLOT_51 = 1
    SLOT_56 = 0
    loopRest()
    ExitState()

@State
def mv235ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1072(90000)
        GFX_2('ceef_208_plugeff_thunder')
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 32767)
    label(0)
    sprite('null', 32767)
    teleportRelativeX(-75000)
    label(1)
    sprite('null', 5)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-51)
    Unknown1099(30)

@State
def mv235Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4003('636565665f3233356566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(1600)
        Unknown1007(1000)
        Unknown3001(255)
        teleportRelativeX(180000)
    sprite('null', 4)
    GFX_2('ceef_402_shock')
    GFX_1('ceef_402_stone', -1)
    sprite('null', 4)
    Unknown4003('636565665f3233356566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 5)
    Unknown3004(-51)

@State
def MinervaAtkAirAssault():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown4009(3)
        SLOT_53 = 1
        Unknown23013(1)

        def upon_CLEAR_OR_EXIT():
            if (not SLOT_51):
                if SLOT_36:
                    Unknown2071('0300000000000000000000001900000000000000')
                else:
                    Unknown2071('030000006079feff000000001900000000000000')
            if (SLOT_52 == 1):
                Unknown2071('030000006079feff400d03006400000000000000')
            if (SLOT_52 == 2):
                Unknown2071('0300000000000000f0d8ffff3200000000000000')
                physicsYImpulse(-20000)
            if (SLOT_52 == 3):
                Unknown2071('0300000000000000000000006400000000000000')
            if (SLOT_52 == 4):
                Unknown1086(3)
                teleportRelativeX(-100000)

        def upon_32():
            SLOT_52 = 2
            sendToLabel(1)
        sendToLabelUpon(2, 2)
    sprite('mv404_00', 3)
    Unknown1086(3)
    SLOT_52 = 3
    SLOT_51 = 1
    sprite('mv404_01', 3)
    sprite('mv404_02', 3)
    sprite('mv404_03', 3)
    sprite('mv404_04', 3)
    sprite('mv404_05', 3)
    sprite('mv404_06', 3)
    sprite('mv404_07', 3)
    SLOT_52 = 1
    SLOT_51 = 1
    label(0)
    sprite('mv404_08', 3)
    sprite('mv404_07', 3)
    gotoLabel(0)
    label(1)
    sprite('mv404_07', 3)
    sprite('mv404_08', 3)
    gotoLabel(1)
    label(2)
    sprite('mv212_11', 3)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8004(100, 1, 1)
    sprite('mv212_12', 3)
    sprite('mv212_13', 3)
    sprite('mv212_14', 3)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def ce404StarEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown3033()
        Unknown2054(1)
        Unknown2005()
        Unknown23015(1)
    sprite('vr_mvef404_00', 5)
    GFX_0('ceef_404StarSub', -1)
    Unknown1099(80)
    GFX_1('ceef_kickhiteff00', -1)
    sprite('vr_mvef404_00', 10)
    Unknown3004(-26)
    Unknown1099(30)

@State
def ce404KickEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('636565665f6b69636b65666630300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('ceef_404kickjizoku00')
        Unknown3032()
        Unknown1072(-40000)
        teleportRelativeX(90000)
        Unknown1056(1500)
        Unknown1064(3000)
        sendToLabelUpon(32, 1)
    sprite('null', 1)
    GFX_1('ceef_kickeff01', -1)
    GFX_1('ceef_kickstart', -1)
    label(0)
    sprite('null', 5)
    GFX_1('ceef_kickeff01', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown1059(-120)
    Unknown1067(120)
    Unknown3004(-26)
    loopRest()

@State
def ceef_404StarSub():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4061(1)
        Unknown1073(20000)
        Unknown1096(1300)
        Unknown1062(0, 250)
        Unknown1077(-15000, 15000)
        Unknown23015(1)
        Unknown3033()
    sprite('vr_mvcmneff_00', 4)
    sprite('vr_mvcmneff_01', 3)
    Unknown3004(-8)
    sprite('vr_mvcmneff_02', 3)
    sprite('vr_mvcmneff_03', 3)
    sprite('vr_mvcmneff_04', 3)
    sprite('vr_mvcmneff_05', 3)
    sprite('vr_mvcmneff_07', 2)
    sprite('vr_mvcmneff_08', 2)

@State
def ceef_HealKurukuru():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
        Unknown4061(1)
    sprite('vr_ce432_00', 6)
    teleportRelativeX(-10000)
    sprite('vr_ce432_01', 6)
    teleportRelativeX(10000)
    GFX_1('ceef_kurukurutubu', 0)
    GFX_1('ceef_kurukurutubu', 1)
    GFX_1('ceef_kurukurutubu', 2)
    sprite('vr_ce432_02', 6)
    GFX_1('ceef_kurukurutubu', 0)
    GFX_1('ceef_kurukurutubu', 1)
    GFX_1('ceef_kurukurutubu', 2)
    sprite('vr_ce432_03', 6)
    GFX_1('ceef_kurukurutubu', 0)
    GFX_1('ceef_kurukurutubu', 1)
    GFX_1('ceef_kurukurutubu', 2)
    sprite('vr_ce432_04', 6)
    GFX_1('ceef_kurukurutubu', 0)
    GFX_1('ceef_kurukurutubu', 1)
    GFX_1('ceef_kurukurutubu', 2)
    sprite('vr_ce432_05', 6)
    GFX_1('ceef_kurukurutubu', 0)
    GFX_1('ceef_kurukurutubu', 1)
    GFX_1('ceef_kurukurutubu', 2)
    sprite('vr_ce432_06', 6)
    GFX_1('ceef_kurukurutubu', 0)
    GFX_1('ceef_kurukurutubu', 1)
    GFX_1('ceef_kurukurutubu', 2)
    sprite('vr_ce432_07', 6)

@State
def ce401PanchEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown4003('636565665f34303165666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(400000)
        teleportRelativeX(-2000)
        Unknown1096(1000)
    sprite('null', 5)
    GFX_1('ceef_401panch', -1)
    GFX_0('mv401Nokosi', -1)
    GFX_0('mv401Nokosi2', -1)
    sprite('null', 5)
    teleportRelativeX(-50000)

@State
def mv401Nokosi():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown1077(-100000, 100000)
        Unknown1011(0, 15000)
        Unknown1010(100000, 100000)
        Unknown1096(1000)
    sprite('null', 10)
    sprite('null', 5)

@State
def mv401Nokosi2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1077(-100000, 100000)
        Unknown1011(-170000, -170000)
        Unknown1010(-10000, -10000)
        Unknown1096(800)
    sprite('null', 10)
    sprite('null', 5)

@State
def ce400JetEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(2)
        Unknown4011(2)
        GFX_2('ceef_400_shock')
        Unknown4003('636565665f34303065666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(750)
        sendToLabelUpon(32, 1)
    sprite('null', 4)
    GFX_0('ce400JetEffNokosi', -1)
    sprite('null', 1)
    label(0)
    sprite('null', 5)
    GFX_0('ce400JetEffNokosi', -1)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def ce400JetEffBackFireAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(200)
        AttackP2(90)
        Unknown11092(1)
        Hitstop(0)
        AirPushbackX(120000)
        AirPushbackY(-100000)
        Unknown9310(1)
        Unknown11057(500)
        Unknown23182(2)
        Unknown12052(1)
        Unknown11069('ce400JetEffBackFireAtk')
        Unknown11032('a0860100c0bdf0ffffffffffffffffff')
        AirUntechableTime(60)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9017(1)
        Unknown23182(3)
        Unknown4007(2)
        Unknown4010(3)
        Unknown4011(3)
        sendToLabelUpon(33, 1)
    sprite('null', 2)
    label(0)
    sprite('ce400_dummyAtk', 2)
    RefreshMultihit()
    gotoLabel(0)
    label(1)
    sprite('ce400_dummyAtk', 3)
    RefreshMultihit()
    AttackLevel_(4)
    AirPushbackX(5000)
    AirPushbackY(32000)
    Unknown11069('')
    Unknown9310(0)

@State
def ce400JetEffNokosi():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f34303065666630312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        Unknown1096(600)
        physicsXImpulse(-7500)
    sprite('null', 10)
    GFX_1('ceef_airdash_nokosi2', -1)
    Unknown3004(-26)

@State
def mv400windMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    label(0)
    sprite('null', 5)
    GFX_1('ceef_cmn_stone00', -1)
    GFX_0('mv400wind', -1)
    sprite('null', 5)
    GFX_1('ceef_cmn_stone00', -1)
    gotoLabel(0)

@State
def mv400wind():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(10000)
        Unknown3001(255)
        Unknown1056(700)
        Unknown1064(450)
        physicsXImpulse(-3500)
        Unknown1099(30)
        Unknown1070(-150, 0)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-21)

@State
def mv402Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('636565665f3430326566663030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        teleportRelativeX(130000)
        Unknown1007(-20000)
        Unknown1096(1600)
        Unknown2005()
    sprite('null', 4)
    GFX_2('ceef_402_shock')
    GFX_0('mv402Nokosi2', -1)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown35()
    GFX_0('mv402Nokosi2', -1)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    GFX_0('mv402wind', -1)
    GFX_0('mv402Nokosi', -1)
    Unknown36(1)
    Unknown1007(50000)
    Unknown3001(175)
    Unknown35()
    GFX_0('mv402Nokosi', -1)
    Unknown36(1)
    Unknown1096(600)
    Unknown1007(200000)
    teleportRelativeX(150000)
    Unknown3001(175)
    Unknown35()
    GFX_0('mv402Nokosi', -1)
    Unknown36(1)
    Unknown1096(450)
    Unknown1007(200000)
    teleportRelativeX(300000)
    Unknown3001(175)
    Unknown35()
    sprite('null', 4)
    Unknown4003('636565665f3430326566663031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 6)
    Unknown3004(-51)

@State
def mv402Nokosi():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1077(-100000, 100000)
        Unknown1011(300000, 300000)
        Unknown1096(1000)
    sprite('null', 5)
    Unknown3001(0)
    sprite('null', 9)
    Unknown3001(255)

@State
def mv402Nokosi2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1077(-100000, 100000)
        Unknown1011(100000, 100000)
        Unknown1010(-100000, -100000)
        Unknown1096(1000)
    sprite('null', 15)
    Unknown3001(255)

@State
def mv402wind():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(10000)
        Unknown3001(255)
        Unknown1056(-700)
        Unknown1064(450)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-17)

@State
def SuperHealEffSP():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('636565665f73757065726865616c65666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1007(500000)
        teleportRelativeX(40000)
        Unknown3032()
        sendToLabelUpon(32, 1)
    sprite('null', 10)
    GFX_0('SuperHealEffWing', -1)
    GFX_1('ceef_healsphere_start', 100)
    GFX_0('SuperHealEff2', -1)
    GFX_0('SuperHealEff3OD', -1)
    Unknown1096(200)
    Unknown1099(100)
    SFX_3('cese_03')
    label(0)
    sprite('null', 1)
    GFX_0('ceCmnHealAura', -1)
    Unknown36(1)
    Unknown1097(500)
    teleportRelativeX(70000)
    Unknown35()
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    sprite('null', 1)
    Unknown1099(0)
    Unknown1096(1450)
    sprite('null', 3)
    Unknown1102(-100, 100)
    gotoLabel(0)
    label(1)
    sprite('null', 5)
    Unknown21012('53757065724865616c456666320000000000000000000000000000000000000020000000')
    Unknown21012('53757065724865616c456666334f44000000000000000000000000000000000020000000')
    Unknown3004(-26)
    Unknown1099(30)
    sprite('null', 5)
    loopRest()

@State
def SuperHealEff3OD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('ceef_healaura00od')
        Unknown2054(1)
        Unknown1096(1250)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    GFX_1('ceef_healauraend2', -1)
    Unknown3004(-26)

@State
def SuperHealEffWing():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown4061(1)
        Unknown3033()
        Unknown1056(1300)
        Unknown1064(1600)
        Unknown1007(-150000)
        Unknown1074(-125)
        Unknown2019(100)
        Unknown3001(200)
    sprite('vr_ce432b_00', 6)
    GFX_0('SuperHealEffWingL', -1)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_01', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_02', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_03', 6)
    GFX_1('ceef_odhealkira02', 0)
    Unknown1099(5)
    sprite('vr_ce432b_04', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_05', 7)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_06', 7)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_07', 4)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_08', 4)

@State
def SuperHealEffWingL():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown4061(1)
        Unknown3033()
        Unknown2005()
        Unknown1056(1400)
        Unknown1064(1600)
        Unknown1074(-125)
        Unknown2019(100)
        Unknown3001(200)
    sprite('vr_ce432b_00', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_01', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_02', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_03', 6)
    GFX_1('ceef_odhealkira02', 0)
    Unknown1099(5)
    sprite('vr_ce432b_04', 6)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_05', 7)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_06', 7)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_07', 4)
    GFX_1('ceef_odhealkira02', 0)
    sprite('vr_ce432b_08', 4)

@Subroutine
def UltimateShotInit():
    AttackLevel_(3)
    Unknown11092(1)
    AirPushbackX(20000)
    AirPushbackY(30000)
    PushbackX(15300)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirUntechableTime(60)
    Hitstop(0)
    Unknown11001(0, 2, 7)
    Unknown9016(1)

@State
def MinervaAtkUltimateShot():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown2011()
        callSubroutine('MV_ChainAtkInit')
        Unknown23056('')
        callSubroutine('UltimateShotInit')
        Damage(400)
        MinimumDamagePct(10)
        AttackP1(80)
        AttackP2(60)
        SLOT_54 = 10

        def upon_11():
            if (SLOT_54 == 1):
                Damage(1450)
                MinimumDamagePct(14)
                Unknown9215()
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
    sprite('mv000_00', 3)
    sprite('mv403_00', 3)
    sprite('mv403_01', 3)
    sprite('mv403_02', 3)
    GFX_0('mv403ConsentEff', 0)
    GFX_0('mv403TameEff', -1)
    GFX_0('mv403TameEffSub', -1)
    sprite('mv403_03', 3)
    sprite('mv403_17', 3)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_18', 6)
    sprite('mv403_19', 46)
    GFX_0('mv403Eff', 100)
    sprite('mv403_20', 2)
    RefreshMultihit()
    Unknown26('mv403TameEffSub')
    Unknown21012('6d7634303345666600000000000000000000000000000000000000000000000020000000')
    Unknown21012('6d7634303354616d65456666000000000000000000000000000000000000000020000000')
    sprite('mv403_21', 1)
    StartMultihit()
    Unknown23029(3, 434, 0)
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(0)
    sprite('mv403_20', 2)
    RefreshMultihit()
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(1)
    sprite('mv403_23', 10)
    Unknown26('mv403Eff')
    GFX_1('ceef_403beamend00', 0)
    GFX_1('ceef_403beamend00', 1)
    GFX_1('ceef_403beamend00', 2)
    sprite('mv403_24', 5)
    sprite('mv403_25', 5)
    sprite('mv403_14', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_15', 5)
    sprite('mv403_16', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtkUltimateShotDUO():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown2011()
        callSubroutine('MV_ChainAtkInit')
        Unknown23056('')
        callSubroutine('UltimateShotInit')
        AttackLevel_(3)
        Damage(100)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        SLOT_54 = 10

        def upon_11():
            if (SLOT_54 == 1):
                Unknown9215()
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
    sprite('mv000_00', 3)
    sprite('mv403_00', 3)
    sprite('mv403_01', 3)
    sprite('mv403_02', 3)
    GFX_0('mv403ConsentEff', 0)
    GFX_0('mv403TameEff', -1)
    GFX_0('mv403TameEffSub', -1)
    sprite('mv403_03', 3)
    sprite('mv403_17', 3)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_18', 6)
    sprite('mv403_19', 46)
    GFX_0('mv403Eff', 100)
    sprite('mv403_20', 2)
    RefreshMultihit()
    Unknown26('mv403TameEffSub')
    Unknown21012('6d7634303345666600000000000000000000000000000000000000000000000020000000')
    Unknown21012('6d7634303354616d65456666000000000000000000000000000000000000000020000000')
    sprite('mv403_21', 1)
    StartMultihit()
    Unknown23029(3, 434, 0)
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(0)
    sprite('mv403_20', 2)
    RefreshMultihit()
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(1)
    sprite('mv403_23', 10)
    Unknown26('mv403Eff')
    GFX_1('ceef_403beamend00', 0)
    GFX_1('ceef_403beamend00', 1)
    GFX_1('ceef_403beamend00', 2)
    sprite('mv403_24', 5)
    sprite('mv403_25', 5)
    sprite('mv403_14', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_15', 5)
    sprite('mv403_16', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv403TameEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown2054(1)
        GFX_2('ceef_tamebeam_00')
        sendToLabelUpon(32, 1)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('02000000d0dd060090d003006400000000000000')
    label(0)
    sprite('null', 3)
    Unknown1096(1200)
    ScreenShake(2500, 2500)
    Unknown1077(0, 100000)
    sprite('null', 3)
    Unknown1062(0, 250)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(20000, 20000)
    GFX_1('ceef_tamebeam_end', -1)
    GFX_1('ceef_beamstart00', -1)

@State
def mv403TameEffSub():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown2054(1)
        Unknown2019(-500)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('0200000000000000d08affff6400000000000000')
    sprite('null', 8)
    sprite('vr_mvef403s_00', 4)
    sprite('vr_mvef403s_01', 4)
    sprite('vr_mvef403s_02', 3)
    sprite('vr_mvef403s_03', 3)
    sprite('vr_mvef403s_04', 2)
    sprite('vr_mvef403s_05', 2)
    sprite('vr_mvef403s_06', 2)
    label(0)
    sprite('vr_mvef403s_03', 2)
    sprite('vr_mvef403s_04', 2)
    sprite('vr_mvef403s_05', 2)
    sprite('vr_mvef403s_06', 2)
    sprite('null', 3)
    gotoLabel(0)

@State
def mv403Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('vr_mvef403_00', 1)
    GFX_0('mv403EffParticle', 0)
    GFX_0('mv403SubEff', 100)
    GFX_0('mv403mazleEff', 100)
    GFX_0('mv403mazleEff2', 100)
    GFX_0('mv403mazleEff3', 100)
    SFX_3('cese_12')
    label(1)
    sprite('vr_mvef403_00', 2)
    GFX_0('mv403ThunderEff', -1)
    GFX_0('mv403ThunderEff2', -1)
    GFX_0('mv403BeamEff', -1)
    GFX_0('mv403BeamEff2', -1)
    GFX_0('mv403Smoke', 100)
    GFX_0('mvBeamNokosi', 1)
    GFX_0('mvBeamNokosi2', 1)
    GFX_0('mvBeamNokosi', 2)
    GFX_0('mvBeamNokosi2', 2)
    GFX_0('mvBeamNokosi', 3)
    GFX_0('mvBeamNokosi2', 3)
    GFX_0('mvBeamNokosi', 4)
    GFX_0('mvBeamNokosi2', 4)
    GFX_0('mvBeamNokosi', 5)
    GFX_0('mvBeamNokosi2', 5)
    SFX_3('cese_12')
    sprite('vr_mvef403_01', 2)
    GFX_0('mv403BeamEff', -1)
    GFX_0('mv403BeamEff2', -1)
    SFX_3('cese_12')
    sprite('vr_mvef403_02', 2)
    SFX_3('cese_12')
    gotoLabel(1)

@State
def mv403BeamEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('636565665f6265616d45666630302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(300000)
        teleportRelativeX(300000)
        Unknown1096(1300)
        Unknown3032()
        Unknown1011(-25000, 25000)
        Unknown1010(0, 500000)
    sprite('null', 1)
    sprite('null', 1)
    Unknown3001(128)

@State
def mv403BeamEff2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('636565665f6265616d45666630302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(300000)
        teleportRelativeX(300000)
        Unknown1096(1300)
        Unknown3032()
        Unknown1011(-25000, 25000)
        Unknown1010(500000, 1250000)
    sprite('null', 1)
    sprite('null', 1)
    Unknown3001(128)

@State
def mvBeamNokosi():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e7061727469636c65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(500)
        Unknown1077(-10000, 10000)
        Unknown1011(75000, 150000)
        Unknown1010(-150000, 150000)
        Unknown2054(1)
    sprite('null', 10)
    Unknown1099(-30)
    Unknown3004(-26)

@State
def mvBeamNokosi2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e7061727469636c65303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3033()
        Unknown1096(500)
        Unknown1077(-10000, 10000)
        Unknown1011(-170000, -100000)
        Unknown1010(-150000, 150000)
        Unknown2054(1)
    sprite('null', 10)
    Unknown1099(-30)
    Unknown3004(-26)

@State
def mvBeamNokosi3():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1077(-100000, 100000)
        Unknown1011(0, 150000)
        Unknown1010(-150000, 150000)
        Unknown1096(600)
    sprite('null', 14)
    Unknown3004(-7)
    Unknown1099(-7)
    physicsXImpulse(-6000)

@State
def mv403EffParticle():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 32767)
    GFX_2('ceef_ddlaser_00')

@State
def mv403SubEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown2054(1)
        Unknown3035()
    sprite('null', 1)
    label(0)
    sprite('vr_mvef403sub_00', 2)
    GFX_0('mv403BulletEff', 100)
    GFX_0('mv403BulletEff2', 100)
    sprite('vr_mvef403sub_01', 2)
    sprite('vr_mvef403sub_02', 2)
    GFX_0('mv403BulletEff', 100)
    GFX_0('mv403BulletEff2', 100)
    gotoLabel(0)

@State
def mv403BulletEff():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2019(-500)
        Unknown2054(1)
        Unknown1007(80000)
        teleportRelativeX(250000)
        Unknown1011(-40000, 40000)
        Unknown1096(-600)
        Unknown3029(1)
        Unknown3071(5)
    sprite('vr_mvef403_03', 30)
    physicsXImpulse(70000)
    Unknown1059(-100)

@State
def mv403BulletEff2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown2019(-1000)
        Unknown2054(1)
        Unknown1007(350000)
        teleportRelativeX(200000)
        Unknown1011(-60000, 60000)
        Unknown1096(-1000)
        Unknown3029(1)
        Unknown3071(5)
    sprite('vr_mvef403_03', 30)
    physicsXImpulse(70000)
    Unknown1059(-75)

@State
def mv403mazleEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown2054(1)
        Unknown1007(90000)
        teleportRelativeX(270000)
    label(0)
    sprite('vr_mvef403mzl_00', 2)
    sprite('vr_mvef403mzl_01', 2)
    gotoLabel(0)

@State
def mv403mazleEff2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown2054(1)
        Unknown1007(360000)
        teleportRelativeX(230000)
        Unknown1096(600)
        Unknown3033()
        Unknown3001(180)
    label(0)
    sprite('vr_mvef403mzl_00', 2)
    sprite('vr_mvef403mzl_01', 2)
    gotoLabel(0)

@State
def mv403mazleEff3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown2019(1000)
        Unknown2054(1)
        Unknown1007(370000)
        teleportRelativeX(250000)
        Unknown1096(600)
    label(0)
    sprite('vr_mvef403mzl_00', 2)
    sprite('vr_mvef403mzl_01', 2)
    gotoLabel(0)

@State
def mv403ThunderEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown2054(1)
        Unknown3033()
        Unknown1077(-60000, 100000)
        Unknown1056(1250)
        Unknown1064(1500)
        Unknown1070(500, 2000)
        Unknown1062(0, 500)
        Unknown2019(-500)
        Unknown1007(250000)
        teleportRelativeX(300000)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_00', 2)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)

@State
def mv403ThunderEff2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown2054(1)
        Unknown3033()
        Unknown1077(100000, 250000)
        Unknown1056(1250)
        Unknown1064(1500)
        Unknown1070(500, 2000)
        Unknown1062(0, 500)
        Unknown2019(-500)
        Unknown1007(250000)
        teleportRelativeX(300000)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_00', 2)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)

@State
def mv403Smoke():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(150000)
        Unknown3001(126)
        Unknown1056(600)
        Unknown1064(400)
        physicsXImpulse(-7500)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-8)

@State
def MinervaAtkUltimateShotSP():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown2011()
        callSubroutine('MV_ChainAtkInit')
        Unknown23056('')
        callSubroutine('UltimateShotInit')
        AttackLevel_(3)
        Damage(500)
        MinimumDamagePct(10)
        AttackP1(80)
        AttackP2(60)
        Unknown11110(80)
        SLOT_54 = 10

        def upon_11():
            if (SLOT_54 == 1):
                Damage(1800)
                MinimumDamagePct(12)
                Unknown9215()
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
    sprite('mv000_00', 3)
    sprite('mv403_00', 3)
    Unknown1086(3)
    teleportRelativeX(-100000)
    sprite('mv403_01', 3)
    sprite('mv403_02', 3)
    GFX_0('mv403TameEffOD', -1)
    GFX_0('mv403ConsentEff', 0)
    GFX_0('mv403TameEffSub', -1)
    sprite('mv403_03', 3)
    sprite('mv403_17', 3)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_18', 6)
    sprite('mv403_19', 46)
    GFX_0('mv403EffOD', 100)
    sprite('mv403_20', 2)
    RefreshMultihit()
    Unknown26('mv403TameEffSub')
    Unknown21012('6d763430334566664f440000000000000000000000000000000000000000000020000000')
    Unknown21012('6d7634303354616d654566664f4400000000000000000000000000000000000020000000')
    sprite('mv403_21', 1)
    StartMultihit()
    Unknown23029(3, 434, 0)
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(0)
    sprite('mv403_20', 2)
    RefreshMultihit()
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(1)
    sprite('mv403_23', 10)
    Unknown21012('6d763430334566664f440000000000000000000000000000000000000000000021000000')
    GFX_1('ceef_403beamend00', 0)
    GFX_1('ceef_403beamend00', 1)
    GFX_1('ceef_403beamend00', 2)
    sprite('mv403_24', 5)
    sprite('mv403_25', 5)
    sprite('mv403_14', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_15', 5)
    sprite('mv403_16', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtkUltimateShotDUOSP():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown2011()
        callSubroutine('MV_ChainAtkInit')
        Unknown23056('')
        callSubroutine('UltimateShotInit')
        AttackLevel_(3)
        Damage(100)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        SLOT_54 = 10

        def upon_11():
            if (SLOT_54 == 1):
                Damage(350)
                Unknown9215()
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
    sprite('mv000_00', 3)
    sprite('mv403_00', 3)
    Unknown1086(3)
    teleportRelativeX(-100000)
    sprite('mv403_01', 3)
    sprite('mv403_02', 3)
    GFX_0('mv403TameEffOD', -1)
    GFX_0('mv403ConsentEff', 0)
    GFX_0('mv403TameEffSub', -1)
    sprite('mv403_03', 3)
    sprite('mv403_17', 3)
    Unknown8004(100, 1, 1)
    SFX_3('cese_15')
    sprite('mv403_18', 6)
    sprite('mv403_19', 46)
    GFX_0('mv403EffOD', 100)
    sprite('mv403_20', 2)
    RefreshMultihit()
    Unknown26('mv403TameEffSub')
    Unknown21012('6d763430334566664f440000000000000000000000000000000000000000000020000000')
    Unknown21012('6d7634303354616d654566664f4400000000000000000000000000000000000020000000')
    sprite('mv403_21', 1)
    StartMultihit()
    Unknown23029(3, 434, 0)
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(0)
    sprite('mv403_20', 2)
    RefreshMultihit()
    sprite('mv403_21', 1)
    StartMultihit()
    sprite('mv403_21', 1)
    RefreshMultihit()
    sprite('mv403_22', 1)
    sprite('mv403_22', 1)
    StartMultihit()
    SLOT_54 = (SLOT_54 + (-1))
    if (SLOT_54 > 0):
        sendToLabel(0)
    label(1)
    sprite('mv403_23', 10)
    Unknown21012('6d763430334566664f440000000000000000000000000000000000000000000021000000')
    GFX_1('ceef_403beamend00', 0)
    GFX_1('ceef_403beamend00', 1)
    GFX_1('ceef_403beamend00', 2)
    sprite('mv403_24', 5)
    sprite('mv403_25', 5)
    sprite('mv403_14', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv403_15', 5)
    sprite('mv403_16', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def mv403TameEffOD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4061(1)
        Unknown2054(1)
        GFX_2('ceef_tamebeam_00')
        sendToLabelUpon(32, 1)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('02000000d0dd060090d003006400000000000000')
    label(0)
    sprite('null', 3)
    Unknown1096(1500)
    ScreenShake(2500, 2500)
    Unknown1077(0, 100000)
    sprite('null', 3)
    Unknown1062(0, 250)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    ScreenShake(20000, 20000)
    GFX_1('ceef_tamebeam_end', -1)
    GFX_1('ceef_beamstart00', -1)

@State
def mv403EffOD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(1)
        Unknown2019(-500)
        Unknown2054(1)
        Unknown3033()
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 2)
    sprite('null', 32767)
    label(0)
    sprite('vr_mvef403_00od', 1)
    GFX_0('mv403EffAddPartsOD', -1)
    GFX_0('mv403EffParticleOD', 0)
    GFX_0('mv403SubEff', 100)
    GFX_0('mv403mazleEff', 100)
    Unknown36(1)
    Unknown1097(300)
    Unknown35()
    GFX_0('mv403mazleEff2', 100)
    GFX_0('mv403mazleEff3', 100)
    SFX_3('cese_12')
    label(1)
    sprite('vr_mvef403_00od', 2)
    ScreenShake(1000, 1000)
    GFX_0('mv403ThunderEff', -1)
    GFX_0('mv403ThunderEff2', -1)
    GFX_0('mv403Smoke', 100)
    GFX_0('mvBeamNokosi', 1)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    GFX_0('mvBeamNokosi2', 1)
    Unknown36(1)
    Unknown1007(-50000)
    Unknown35()
    GFX_0('mvBeamNokosi', 2)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    GFX_0('mvBeamNokosi2', 2)
    Unknown36(1)
    Unknown1007(-50000)
    Unknown35()
    GFX_0('mvBeamNokosi', 3)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    GFX_0('mvBeamNokosi2', 3)
    Unknown36(1)
    Unknown1007(-50000)
    Unknown35()
    GFX_0('mvBeamNokosi', 4)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    GFX_0('mvBeamNokosi2', 4)
    Unknown36(1)
    Unknown1007(-50000)
    Unknown35()
    GFX_0('mvBeamNokosi', 5)
    Unknown36(1)
    Unknown1007(50000)
    Unknown35()
    GFX_0('mvBeamNokosi2', 5)
    Unknown36(1)
    Unknown1007(-50000)
    Unknown35()
    SFX_3('cese_12')
    sprite('vr_mvef403_01od', 2)
    ScreenShake(1000, 1000)
    SFX_3('cese_12')
    sprite('vr_mvef403_02od', 2)
    ScreenShake(1000, 1000)
    SFX_3('cese_12')
    gotoLabel(1)
    label(2)
    sprite('vr_mvef403_00od', 2)
    Unknown3004(-51)
    Unknown21012('6d7634303345666641646450617274734f44000000000000000000000000000020000000')
    Unknown26('mv403EffParticleOD')
    Unknown26('mv403SubEff')
    Unknown26('mv403mazleEff')
    Unknown26('mv403mazleEff2')
    Unknown26('mv403mazleEff3')
    SFX_3('cese_12')
    sprite('vr_mvef403_01od', 2)
    SFX_3('cese_12')
    sprite('vr_mvef403_02od', 15)
    GFX_0('mvBeamNokosi', 1)
    GFX_0('mvBeamNokosi2', 1)
    GFX_0('mvBeamNokosi', 2)
    GFX_0('mvBeamNokosi2', 2)
    GFX_0('mvBeamNokosi', 3)
    GFX_0('mvBeamNokosi2', 3)
    GFX_0('mvBeamNokosi', 4)
    GFX_0('mvBeamNokosi2', 4)
    GFX_0('mvBeamNokosi', 5)
    GFX_0('mvBeamNokosi2', 5)
    Unknown26('mv403ThunderEff')
    Unknown26('mv403ThunderEff2')
    SFX_3('cese_12')

@State
def mv403EffParticleOD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 32767)
    GFX_2('ceef_ddlaserod_00')

@State
def mv403EffAddPartsOD():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown2054(1)
        Unknown3032()
        Unknown1007(275000)
        teleportRelativeX(300000)
        Unknown1056(2000)
        Unknown1064(2500)
        Unknown3002(128)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    Unknown4003('636565665f3430336f646265616d3030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 10)
    Unknown1067(-80)
    Unknown3004(-26)

@State
def MinervaRecovery():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv601_03', 6)
    sprite('mv615_00', 6)
    sprite('mv615_01', 6)
    sprite('mv601_00', 600)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaRecoveryEnd():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv615_01', 6)
    sprite('mv615_00', 6)
    sprite('mv601_03', 6)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaAtkBurstDD():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown2011()
        AttackLevel_(4)
        Damage(460)
        Hitstop(8)
        Unknown11043(0)
        ChipDamagePct(0)
        MinimumDamagePct(10)
        AirUntechableTime(100)
        AttackP2(100)
        Unknown11092(1)
        PushbackX(20000)
        Unknown9016(1)
        Unknown11064(1)
        Unknown11069('MinervaAtkBurstDD')
        Unknown11066(1)
        Unknown11023(1)
        Unknown48('190000000200000037000000030000000200000033000000')
    sprite('mv236_00ex01', 3)
    SLOT_51 = 4
    sprite('mv236_01ex01', 3)
    sprite('mv236_02ex01', 3)
    sprite('mv236_03ex01', 3)
    SFX_0('010_swing_sword_1')
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_06')
    sprite('mv236_04ex01', 3)
    GFX_0('ce440Eff', -1)
    GFX_0('mv236Eff', -1)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    RefreshMultihit()
    sprite('mv236_05ex01', 3)
    sprite('mv236_06ex01', 3)
    Unknown21012('427572737444444164640000000000000000000000000000000000000000000021000000')
    sprite('mv232_02ex01', 3)
    physicsXImpulse(30000)
    Unknown1028(-3000)
    sprite('mv232_03ex01', 3)
    SFX_0('010_swing_sword_1')
    SFX_0('004_swing_grap_1_1')
    SFX_3('cese_06')
    sprite('mv232_04ex01', 3)
    GFX_0('ce440Eff2', -1)
    GFX_0('mv232Eff', -1)
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    PushbackX(-5000)
    RefreshMultihit()
    Unknown1084(1)
    sprite('mv232_05ex01', 3)
    sprite('mv232_06ex01', 3)
    Unknown21012('427572737444444164640000000000000000000000000000000000000000000022000000')
    sprite('mv212_05ex01', 3)
    physicsYImpulse(18000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
    sprite('mv212_06ex01', 3)
    SFX_0('010_swing_sword_2')
    SFX_0('004_swing_grap_1_2')
    SFX_3('cese_06')
    physicsXImpulse(-18000)
    sprite('mv212_07ex01', 3)
    GFX_0('ce440Eff3', -1)
    GFX_0('mv212Eff', -1)
    AirPushbackX(-1000)
    AirPushbackY(28000)
    RefreshMultihit()
    sprite('mv212_08ex01', 3)
    GFX_0('ce440Eff3', -1)
    sprite('mv212_09ex01', 3)
    sprite('mv212_10ex01', 3)
    sprite('mv212_11ex01', 3)
    loopRest()
    if SLOT_55:
        _gotolabel(100)
    sprite('mv403_00ex01', 3)
    sprite('mv403_01ex01', 3)
    Unknown21012('427572737444444164640000000000000000000000000000000000000000000023000000')
    sprite('mv403_02ex01', 3)
    sprite('mv440_00', 3)
    GFX_0('ce440EffMato', -1)
    physicsXImpulse(3000)
    sprite('mv440_01', 3)
    physicsXImpulse(30000)
    SFX_3('cese_10')
    sprite('mv440_02', 1)
    GFX_0('mv403ConsentEff', 0)
    Unknown36(1)
    Unknown1073(90000)
    Unknown35()
    GFX_0('mv440Eff', -1)
    Damage(1000)
    Unknown11001(-1, -1, -1)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackX(50000)
    AirPushbackY(18000)
    Unknown9016(0)
    Hitstop(10)
    Unknown11050('02000000636565665f686974656666343430000000000000000000000000000000000000')
    Unknown9202(15)
    Unknown9001(5)
    Unknown11064(0)
    RefreshMultihit()
    Unknown1084(1)
    Unknown21012('427572737444444164640000000000000000000000000000000000000000000029000000')
    sprite('mv440_03', 3)
    Unknown26('BurstDD_Camera')
    ScreenShake(40000, 40000)
    Unknown26('ce440EffMato')
    Unknown21012('6d7634343045666600000000000000000000000000000000000000000000000020000000')
    sprite('mv440_04', 3)
    sprite('mv440_05', 3)
    sprite('mv202_09ex01', 4)
    sprite('mv202_10ex01', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv202_11ex01', 5)
    sprite('mv202_12ex01', 5)
    sprite('mv202_13ex01', 5)
    SLOT_51 = 0
    sprite('mv202_14ex01', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')
    label(100)
    sprite('mv403_00ex01', 3)
    sprite('mv403_01ex01', 3)
    sprite('mv403_02ex01', 3)
    Unknown21012('427572737444444164640000000000000000000000000000000000000000000023000000')
    sprite('mv440_00', 3)
    GFX_0('ce440EffMato', -1)
    physicsXImpulse(3000)
    sprite('mv440_01', 3)
    physicsXImpulse(30000)
    SFX_3('cese_10')
    sprite('mv440_02', 3)
    GFX_0('mv403ConsentEff', 0)
    GFX_0('mv440Eff', -1)
    Damage(630)
    Hitstop(0)
    Unknown11001(1, 1, 1)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    AirPushbackX(20000)
    AirPushbackY(2500)
    Unknown9202(15)
    Unknown11057(700)
    RefreshMultihit()
    Unknown1084(1)
    Unknown9016(0)
    Hitstop(3)
    Unknown11050('02000000636565665f686974656666343430000000000000000000000000000000000000')
    sprite('mv440_02ex01', 3)
    RefreshMultihit()
    SFX_3('cese_10')
    sprite('mv440_02ex02', 3)
    RefreshMultihit()
    SFX_3('cese_10')
    sprite('mv440_02', 3)
    RefreshMultihit()
    SFX_3('cese_10')
    sprite('mv440_02ex01', 3)
    RefreshMultihit()
    SFX_3('cese_10')
    sprite('mv440_02ex02', 3)
    AirPushbackX(50000)
    AirPushbackY(18000)
    Unknown9001(5)
    Unknown11064(0)
    RefreshMultihit()
    Unknown21012('427572737444444164640000000000000000000000000000000000000000000029000000')
    sprite('mv440_03', 3)
    Unknown26('BurstDD_Camera')
    Unknown26('ce440EffMato')
    Unknown21012('6d7634343045666600000000000000000000000000000000000000000000000020000000')
    sprite('mv440_04', 3)
    GFX_0('ceef_hiteff440HitEx', -1)
    sprite('mv440_05', 3)
    sprite('mv202_09ex01', 4)
    sprite('mv202_10ex01', 5)
    Unknown21012('6d76343033436f6e73656e74456666000000000000000000000000000000000020000000')
    sprite('mv202_11ex01', 5)
    sprite('mv202_12ex01', 5)
    sprite('mv202_13ex01', 5)
    SLOT_51 = 0
    sprite('mv202_14ex01', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def ThrowUpCelica():

    def upon_IMMEDIATE():
        Unknown1007(100000)
        physicsYImpulse(70000)
        Unknown2054(1)
        Unknown23022(1)
        Unknown4010(3)
        Unknown4011(3)
    sprite('ce430_00', 3)
    sprite('ce430_01', 3)
    sprite('ce430_00', 3)
    sprite('ce430_01', 3)
    sprite('ce430_00', 3)

@State
def ThrowDownCelica():

    def upon_IMMEDIATE():
        Unknown1007(2000000)
        Unknown23022(1)
        Unknown3001(0)
        Unknown3004(31)

        def upon_CLEAR_OR_EXIT():
            Unknown2071('03000000b8880000000000000800000000000000')
            if (SLOT_23 <= 250000):
                Unknown21007(3, 32)
                sendToLabel(1)
    label(0)
    sprite('ce430_02', 3)
    sprite('ce430_03', 3)
    gotoLabel(0)
    label(1)
    sprite('null', 3)
    clearUponHandler(3)

@State
def mv430ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        GFX_2('ceef_205_plugeff_bigc')
        Unknown2054(1)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-26)
    Unknown1099(30)

@State
def HensinThunder():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4003('636565665f7368756e676f6b75737461727430302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(1250)
        teleportRelativeX(-60000)
        Unknown1059(10)
    sprite('null', 1)
    GFX_0('HensinThunderSub', -1)
    label(0)
    sprite('null', 4)
    Unknown3001(255)
    SFX_0('014_electric_m')
    sprite('null', 1)
    Unknown3001(0)
    gotoLabel(0)

@State
def HensinThunderSub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        GFX_2('ceef_shungokutame00')
        Unknown1096(1500)
        Unknown2054(1)
    sprite('null', 32767)

@State
def ShungokuEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown2054(1)
        Unknown1086(22)
        Unknown1007(280000)
        Unknown4003('636565665f7368756e676f6b756566665f62672e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    GFX_0('ShungokuEff3', -1)
    GFX_0('ShungokuShake', -1)
    sprite('null', 30)
    GFX_2('ceef_shungoku_b')
    GFX_0('ShungokuEff2', -1)
    sprite('null', 20)
    GFX_0('ShungokuEff4', -1)
    sprite('null', 5)
    SFX_3('cese_13')

@State
def ShungokuEff2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('636565665f7368756e676f6b7565666630302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(990)
    sprite('null', 35)
    SFX_3('cese_13')

@State
def ShungokuEff3():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f7368756e676f6b7565666630312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1007(-100000)
        Unknown1096(900)
        Unknown1007(28000)
    sprite('null', 4)
    SFX_3('cese_13')
    sprite('null', 6)
    Unknown1096(1250)
    Unknown1007(30000)
    SFX_3('cese_13')
    sprite('null', 4)
    Unknown1096(1350)
    SFX_3('cese_13')

@State
def ShungokuEff4():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('636565665f7368756e676f6b7565666630302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(990)
        Unknown1073(-22500)
    sprite('null', 20)
    SFX_3('cese_13')
    sprite('null', 15)
    Unknown1073(-60000)
    Unknown1064(2000)
    Unknown1056(600)
    ScreenShake(40000, 40000)
    SFX_3('cese_13')

@State
def ShungokuShake():

    def upon_IMMEDIATE():
        Unknown4010(2)
    label(0)
    sprite('null', 10)
    ScreenShake(10000, 10000)
    gotoLabel(0)

@State
def UltimateAssaultAddAttackMissVer():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown3038(1)
        Unknown23022(1)
        AttackLevel_(4)
        Damage(300)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        Unknown11084(1)
        Unknown11066(1)
        AttackP1(70)
        PushbackX(-1000)
        AirPushbackX(0)
        AirPushbackY(16000)
        Unknown9016(1)
        Hitstop(4)
        StarterRating(2)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(22)
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()
    sprite('mv430_15', 2)
    RefreshMultihit()

@State
def UltimateAssaultAddAttack():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown3038(1)
        Unknown1086(22)
        AttackLevel_(4)
        Damage(800)
        MinimumDamagePct(15)
        AttackP2(100)
        Unknown11092(1)
        Unknown11064(1)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30048(1)
        AirPushbackX(0)
        AirPushbackY(36000)
        Unknown9310(30)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultAddAttack')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_54 = (SLOT_54 + 1)
            if (SLOT_54 >= 13):
                Unknown11069('UltimateAssault')
                sendToLabel(1)
        Unknown2037(60)
    label(0)
    sprite('mv430_15', 1)
    Unknown2038(-1)
    RefreshMultihit()
    if SLOT_2:
        _gotolabel(0)
    label(1)
    sprite('mv430_15', 1)
    clearUponHandler(10)
    sprite('null', 3)
    Unknown21007(3, 33)

@State
def UltimateAssaultAddAttackSP():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown3038(1)
        Unknown1086(22)
        AttackLevel_(4)
        Damage(500)
        MinimumDamagePct(15)
        AttackP2(100)
        Unknown11092(1)
        Unknown11064(1)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30048(1)
        AirPushbackX(0)
        AirPushbackY(36000)
        Unknown9310(30)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultAddAttackSP')

        def upon_ON_HIT_OR_BLOCK():
            SLOT_54 = (SLOT_54 + 1)
            if (SLOT_54 >= 5):
                sendToLabel(100)
        Unknown2037(60)
    label(0)
    sprite('mv430_15', 1)
    Unknown2038(-1)
    RefreshMultihit()
    if SLOT_2:
        _gotolabel(0)
    label(100)
    sprite('mv430_15', 1)
    Hitstop(2)
    Unknown2037(60)
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        SLOT_54 = (SLOT_54 + 1)
        if (SLOT_54 >= 17):
            Unknown11069('UltimateAssaultSP')
            sendToLabel(200)
    label(101)
    sprite('mv430_15', 1)
    Unknown2038(-1)
    RefreshMultihit()
    if SLOT_2:
        _gotolabel(101)
    label(200)
    sprite('mv430_15', 1)
    clearUponHandler(10)
    sprite('null', 3)
    Unknown21007(3, 33)

@State
def ShungokuODSlashEff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4003('636565665f7368756e676f6b754f4465666630302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(1300)
        Unknown1007(150000)
        Unknown1073(-20000)
        Unknown2005()
        Unknown23015(2)
    sprite('null', 7)
    Unknown4048(-20000)
    Unknown4045('636565665f6f647368756e676f6b757370656564000000000000000000000000ffffffff')
    ScreenShake(20000, 20000)
    SFX_3('cese_13')
    sprite('null', 6)
    ScreenShake(20000, 20000)

@State
def ShungokuODSlashEff2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4003('636565665f7368756e676f6b754f4465666630302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(1500)
        Unknown1073(-20000)
        Unknown1007(150000)
        teleportRelativeX(-100000)
        Unknown2005()
        Unknown23015(2)
    sprite('null', 7)
    Unknown4048(-20000)
    Unknown4045('636565665f6f647368756e676f6b757370656564000000000000000000000000ffffffff')
    Unknown1059(100)
    ScreenShake(20000, 20000)
    SFX_3('cese_13')
    sprite('null', 6)
    ScreenShake(20000, 20000)

@State
def ShungokuODSlashEff3():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4010(2)
        Unknown4003('636565665f7368756e676f6b754f4465666630302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1064(2000)
        Unknown1086(22)
        Unknown1007(200000)
        Unknown23015(2)
        Unknown2005()
    sprite('null', 7)
    Unknown4045('636565665f6f647368756e676f6b757370656564000000000000000000000000ffffffff')
    Unknown1059(100)
    physicsXImpulse(-30000)
    ScreenShake(20000, 20000)
    SFX_3('cese_13')
    sprite('null', 6)
    ScreenShake(20000, 20000)

@State
def ShungokuODFinishEff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(150000)
    sprite('null', 18)
    sprite('null', 44)
    GFX_2('ceef_shungokuodeff00')
    sprite('null', 1)
    GFX_1('ceef_shungokuodeff_end', -1)
    ScreenShake(20000, 20000)

@State
def MinervaAtkAstralHeat():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        Unknown4009(3)
        Unknown2019(500)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 52)
    sprite('mv450_00', 8)
    Unknown1086(3)
    teleportRelativeX(-100000)
    SLOT_51 = 1
    SLOT_53 = 1
    sprite('mv450_01', 8)
    sprite('mv450_02', 8)
    sprite('mv450_03', 8)
    sprite('mv450_04', 8)
    sprite('mv450_05', 6)
    physicsYImpulse(100000)
    ScreenShake(40000, 40000)
    GFX_0('mv450Smoke', -1)
    SFX_3('cese_09')
    GFX_1('ceef_450_tobishock', -1)
    GFX_0('mv450Smoke', -1)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    sprite('null', 32767)
    Unknown1086(3)
    Unknown1084(1)
    teleportRelativeY(0)
    label(0)
    sprite('mv450_06', 1)
    Unknown3029(1)
    clearUponHandler(32)
    teleportRelativeX(2000000)
    Unknown2019(-500)
    GFX_0('ce450JetEff', 0)
    GFX_0('ce450JetEff', 1)
    GFX_0('ce450JetEff', 2)
    GFX_0('ce450JetEff', 3)
    sprite('mv450_06', 8)
    physicsXImpulse(-150000)
    Unknown2006()
    sprite('mv450_06', 21)
    sprite('mv450_06', 1)
    Unknown26('ce450JetEff')
    sprite('null', 32767)
    Unknown1086(3)
    Unknown1084(1)
    teleportRelativeY(0)
    Unknown2019(500)
    label(1)
    sprite('keep', 1)
    Unknown3029(0)
    Unknown1086(3)
    sprite('mv030_00', 60)
    teleportRelativeX(-850000)
    sprite('mv030_00', 5)
    physicsXImpulse(11000)
    sprite('mv030_01', 5)
    sprite('mv030_02', 5)
    sprite('mv030_03', 5)
    sprite('mv030_04', 5)
    sprite('mv030_05', 5)
    sprite('mv030_06', 5)
    sprite('mv030_01', 5)
    sprite('mv030_02', 5)
    sprite('mv030_03', 5)
    sprite('mv030_04', 5)
    sprite('mv030_05', 5)
    sprite('mv030_06', 5)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def ceef_hiteffAst():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('ceef_shungokuodeff_end', -1)
    ScreenShake(20000, 20000)
    SFX_3('cese_23')

@State
def AstCameraObj():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown20006(1)
        Unknown2053(0)
        Unknown2034(0)
        Unknown1086(22)
        sendToLabelUpon(32, 1)
    sprite('null', 1)
    sprite('null', 32767)
    teleportRelativeX(-10000)
    label(1)
    sprite('null', 1)

@State
def AstDeathAttack():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(5)
        Damage(28000)
        MinimumDamagePct(100)
        Unknown11023(1)
        Unknown11064(3)
        AirPushbackX(-50000)
        AirPushbackY(100000)
        Unknown9017(1)
        Unknown3038(1)
        Unknown2053(0)
        Unknown2034(0)
        Unknown1086(22)
    sprite('mv450_06', 10)

@State
def ceef450_Kousoku():

    def upon_IMMEDIATE():
        GFX_2('ceef_healbaind_00')
        teleportRelativeX(200000)
        Unknown2053(1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                Unknown1086(22)
            else:
                Unknown2071('03000000400d0300000000006400000000000000')
    sprite('null', 30)
    gotoLabel(1)
    label(0)
    sprite('null', 32767)
    Unknown2037(1)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    GFX_1('ceef_healbaind_end', -1)

@State
def ceef450_BG():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('636565665f3435305f42473030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1007(37500)
        sendToLabelUpon(32, 0)
        Unknown23015(2)
        GFX_2('ceef_healBG')
    sprite('null', 32767)
    GFX_1('ceef_450_healaura_pos', -1)
    GFX_0('ceef450_BGa', -1)
    label(0)
    sprite('null', 30)
    Unknown21012('636565663435305f42476100000000000000000000000000000000000000000020000000')

@State
def ceef450_BGa():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4003('636565665f3435305f424730305f6100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    GFX_2('ceef_450_healaura_kira')
    label(0)
    sprite('null', 10)
    GFX_0('ceef450_Ryuhai', -1)

@State
def ceef450_Ryuhai():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4003('636565665f3435305f73686173686100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown23015(1)
    sprite('null', 39)

@State
def AHCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)
        Unknown20002(1)
        sendToLabelUpon(32, 0)
        sendToLabelUpon(33, 1)
    sprite('null', 180)
    physicsYImpulse(150000)
    sprite('null', 2)
    physicsYImpulse(10000)
    sprite('null', 2)
    physicsYImpulse(5000)
    sprite('null', 2)
    physicsYImpulse(0)
    sprite('null', 32767)
    Unknown20001(1)
    label(0)
    sprite('null', 32767)
    Unknown1086(22)
    Unknown20001(1)
    label(1)
    sprite('null', 32767)
    Unknown1086(3)

@State
def AHKiraEff():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown20002(1)
        Unknown3001(0)
        Unknown1096(450)
        Unknown2005()
        teleportRelativeX(400000)
        Unknown3032()
    sprite('null', 20)
    GFX_2('ceef_450ef_c')
    physicsYImpulse(62500)
    GFX_0('ceef450Shake', -1)
    SFX_3('cese_24')
    sprite('null', 15)
    Unknown3004(17)
    physicsYImpulse(187500)
    sprite('null', 153)
    physicsYImpulse(148000)
    sprite('null', 1)
    physicsYImpulse(0)
    Unknown3001(0)
    GFX_0('AHKiraEff2', -1)

@State
def AHKiraEff2():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown20002(1)
        Unknown1064(1100)
        Unknown1056(950)
    sprite('null', 35)
    Unknown4003('636565665f3435306c696e6530300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    SFX_3('cese_25')
    sprite('null', 1)
    physicsYImpulse(0)
    GFX_0('AHce450', -1)

@State
def AHce450():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown20002(1)
        Unknown1056(1000)
        Unknown2005()
        teleportRelativeX(350000)
        Unknown1007(280000)
    sprite('ce450cutin_00', 60)
    GFX_2('ceef_450cutinline01')
    GFX_0('ceef450Shake', -1)
    Unknown1099(2)
    physicsYImpulse(225)
    physicsXImpulse(-750)
    SFX_3('cese_26')
    sprite('ce450cutin_00', 10)
    Unknown3004(-26)

@State
def ceef450Shake():

    def upon_IMMEDIATE():
        Unknown4010(2)
    label(0)
    sprite('null', 8)
    ScreenShake(6000, 6000)
    gotoLabel(0)

@State
def ceef450_BG3():

    def upon_IMMEDIATE():
        Unknown4003('636565665f3435305f42473031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        sendToLabelUpon(32, 0)
    sprite('null', 75)
    teleportRelativeX(400000)
    GFX_0('ceef450_BG3Eff', -1)
    sprite('null', 32767)
    Unknown4003('636565665f3435305f42473032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('ceef450_BG3Eff')
    label(0)
    sprite('null', 20)
    Unknown1086(3)
    Unknown21012('6d7634353057686974654f75740000000000000000000000000000000000000020000000')
    GFX_2('ceef_450_hanatiri')
    sprite('null', 32767)
    GFX_0('ceef_WinBG', -1)

@State
def ceef450_BG3Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
    sprite('null', 32767)
    GFX_2('ceef_healBG')

@State
def ceef_WinBG():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('636565665f343530736b793030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 32767)
    GFX_2('ceef_450winbg')

@State
def mv450Smoke():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(10000)
        Unknown3001(255)
        Unknown1056(1200)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-17)

@State
def mv450SmokeMato():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('null', 4)
    GFX_0('mv450Smoke1', -1)
    ScreenShake(30000, 30000)
    SFX_3('cese_14')
    SFX_3('cese_14')
    sprite('null', 4)
    GFX_0('mv450Smoke1', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown35()
    sprite('null', 4)
    GFX_0('mv450Smoke1', -1)
    Unknown36(1)
    teleportRelativeX(1200000)
    Unknown1065(-300)
    Unknown35()
    sprite('null', 6)
    GFX_0('mv450Smoke2', -1)

@State
def mv450Smoke1():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(20000)
        Unknown3001(255)
        Unknown1056(-1200)
        Unknown1064(1200)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-17)

@State
def mv450Smoke2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f343530736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(-200000)
        Unknown3001(0)
        Unknown1056(-1400)
    sprite('null', 10)
    Unknown3004(26)
    sprite('null', 30)
    sprite('null', 60)
    Unknown3004(-5)

@State
def mv450HanaTiri():

    def upon_IMMEDIATE():
        Unknown1007(300000)
    sprite('null', 60)
    GFX_2('ceef_450_hanatiri')
    sprite('null', 60)
    Unknown3004(-5)

@State
def mv450WhiteOut():

    def upon_IMMEDIATE():
        Unknown1007(300000)
        Unknown4010(2)
        sendToLabelUpon(32, 0)
        Unknown1096(2000)
    sprite('null', 60)
    sprite('null', 32767)
    GFX_2('ceef_450_white')
    label(0)
    sprite('null', 10)
    Unknown1007(300000)
    sprite('null', 60)
    Unknown3004(-5)

@State
def ce450JetEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown2005()
        Unknown4009(2)
        Unknown4010(2)
        GFX_2('ceef_400_shock')
        Unknown4003('636565665f34303065666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(550)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('null', 5)
    gotoLabel(0)
    label(1)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def mv450BomEff():

    def upon_IMMEDIATE():
        Unknown4003('63656566665f636d6e626f6d62303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1086(22)
        Unknown1007(300000)
        teleportRelativeX(150000)
        Unknown1064(1000)
        Unknown1056(800)
        Unknown1073(20000)
        Unknown2054(1)
        Unknown23015(1)
    sprite('null', 3)
    sprite('null', 3)
    GFX_1('ceef_321_fallfireball00', -1)
    GFX_1('ceef_321_fallfireball01', -1)
    GFX_1('ceef_321_fallfireball02', -1)
    Unknown1097(250)
    sprite('null', 3)
    Unknown1097(150)
    GFX_1('ceef_321_bloom', -1)
    ScreenShake(15000, 15000)
    sprite('null', 9)
    Unknown1097(100)

@State
def mv311Eff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('636565665f33313165666630302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4009(2)
        Unknown4011(3)
        Unknown1073(-30000)
        Unknown1096(4000)
        teleportRelativeX(50000)
        Unknown1007(325000)
        Unknown2054(1)
    sprite('null', 1)
    GFX_0('mv311wind', -1)
    SFX_3('cese_12')
    SFX_3('cese_08')
    sprite('null', 1)
    GFX_0('mv311ThunderEff', -1)
    GFX_0('mv311ThunderEff2', -1)
    GFX_0('mv311thunder', -1)
    Unknown36(1)
    teleportRelativeX(150000)
    Unknown1007(75000)
    Unknown35()
    SFX_0('014_electric_sl')
    GFX_0('mv311thunder2', -1)
    Unknown36(1)
    teleportRelativeX(300000)
    Unknown1007(150000)
    Unknown35()
    GFX_0('mv311thunder', -1)
    Unknown36(1)
    teleportRelativeX(450000)
    Unknown1007(225000)
    Unknown35()
    GFX_0('mv311thunder2', -1)
    Unknown36(1)
    teleportRelativeX(600000)
    Unknown1007(300000)
    Unknown35()
    sprite('null', 5)
    GFX_0('mv311thunder', -1)
    GFX_0('mv311BeamEnd', -1)
    ScreenShake(10000, 10000)
    Unknown1067(-350)
    Unknown1059(-300)

@State
def mv311ThunderEff():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown1073(-145000)
        Unknown1056(1250)
        Unknown1064(1500)
        Unknown1070(500, 2000)
        Unknown1062(0, 500)
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('vr_mvef403a_00', 2)
    SFX_0('014_electric_s')
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    SFX_0('014_electric_l')
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    SFX_0('014_electric_m')
    sprite('vr_mvef403a_03', 2)

@State
def mv311ThunderEff2():

    def upon_IMMEDIATE():
        Unknown4061(1)
        Unknown3033()
        Unknown1073(-85000)
        Unknown1056(1250)
        Unknown1064(1500)
        Unknown1070(500, 2000)
        Unknown1062(0, 500)
        Unknown2019(-500)
        Unknown2054(1)
    sprite('vr_mvef403a_00', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_01', 2)
    sprite('null', 1)
    sprite('vr_mvef403a_02', 2)
    sprite('vr_mvef403a_03', 2)

@State
def mv311thunder():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753262000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(700)
        Unknown1077(-100000, 100000)
        Unknown2054(1)
    sprite('null', 6)
    Unknown3001(0)
    Unknown1099(15)
    sprite('null', 9)
    Unknown3001(255)
    GFX_1('ceef_healsphere01', -1)

@State
def mv311thunder2():

    def upon_IMMEDIATE():
        Unknown4003('636565665f73686f746f5f6a697a6f6b753200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown1096(450)
        Unknown1077(-100000, 100000)
        Unknown2054(1)
    sprite('null', 6)
    Unknown3001(0)
    sprite('null', 9)
    Unknown3001(255)
    GFX_1('ceef_healsphere01', -1)

@State
def mv311BeamEnd():

    def upon_IMMEDIATE():
        GFX_2('ceef_311beamend00')
        Unknown1073(-30000)
        Unknown2054(1)
    sprite('null', 60)

@State
def mv311wind():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e736d6f6b65303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown3032()
        Unknown2054(1)
        teleportRelativeX(-25000)
        Unknown1007(-325000)
        Unknown3001(255)
        Unknown1056(750)
        Unknown1064(550)
    sprite('null', 22)
    Unknown1099(5)
    Unknown3004(-5)

@State
def mv311ConsentEff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown1072(180000)
        sendToLabelUpon(32, 1)
        sendToLabelUpon(33, 2)
    sprite('null', 32767)
    GFX_1('ceef_311__plugeff_sc', -1)
    label(1)
    sprite('null', 32767)
    GFX_2('ceef_205_plugeff_bigc')
    label(2)
    sprite('null', 5)
    GFX_1('ceef_plugeff_cmnthunder', -1)
    Unknown3004(-51)
    Unknown1099(30)
    loopRest()

@State
def MinervaEntry01():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_6 = 0
        Unknown1086(3)
        Unknown23023()
        teleportRelativeX(-100000)
        clearUponHandler(3)
    label(1)
    sprite('mv601_00', 3)
    gotoLabel(1)

@State
def MinervaEntry01Finish():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(3)
    sprite('mv601_00', 3)
    sprite('mv601_01', 6)
    sprite('mv601_02', 16)
    sprite('mv601_02ex01', 6)
    sprite('mv601_02ex02', 6)
    sprite('mv601_02ex03', 6)
    sprite('mv601_02ex01', 6)
    sprite('mv601_02ex02', 6)
    sprite('mv601_02ex03', 6)
    sprite('mv601_02ex01', 6)
    sprite('mv601_02ex02', 6)
    sprite('mv601_02ex03', 6)
    sprite('mv601_03', 8)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaEntry02():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_51 = 1
        sendToLabelUpon(32, 100)
        sendToLabelUpon(33, 200)
        sendToLabelUpon(34, 300)
    sprite('mv602_00', 7)
    Unknown1086(3)
    Unknown1084(1)
    teleportRelativeY(0)
    label(0)
    sprite('keep', 1)
    gotoLabel(0)
    label(100)
    sprite('mv602_00', 7)
    label(101)
    sprite('mv602_00', 7)
    gotoLabel(101)
    label(200)
    sprite('keep', 1)
    Unknown1086(3)
    Unknown1084(1)
    teleportRelativeY(0)
    physicsXImpulse(11000)
    sprite('mv602_00', 7)
    sprite('mv602_01', 7)
    sprite('mv602_02', 7)
    sprite('mv602_03', 7)
    sprite('mv602_04', 7)
    sprite('mv602_05', 7)
    label(5)
    sprite('mv602_00', 7)
    sprite('mv602_01', 7)
    sprite('mv602_02', 7)
    sprite('mv602_03', 7)
    sprite('mv602_04', 7)
    sprite('mv602_05', 7)
    gotoLabel(5)
    label(300)
    sprite('mv602_05ex', 5)
    physicsXImpulse(5000)
    sprite('mv602_06', 5)
    physicsXImpulse(0)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def MinervaEntry03():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(3)
    label(0)
    sprite('mv610_03ex01', 8)
    sprite('mv610_03ex02', 8)
    sprite('mv610_03ex03', 8)
    sprite('mv610_03ex04', 8)
    sprite('mv610_03ex05', 8)
    sprite('mv610_03ex06', 8)
    loopRest()
    gotoLabel(0)

@State
def MinervaEntry03Finish():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        clearUponHandler(3)
    sprite('mv610_02', 5)
    sprite('mv610_00', 6)
    sprite('keep', 100)
    Unknown24('4d696e657276615374616e64000000000000000000000000000000000000000064000000')

@State
def EntryCelicaDummy():

    def upon_IMMEDIATE():

        def upon_32():
            clearUponHandler(32)
            sendToLabel(1)

        def upon_33():
            clearUponHandler(33)
            sendToLabel(2)
    sprite('ce602_00', 6)
    Unknown1000(-1936000)
    physicsXImpulse(14000)
    sprite('ce602_01', 6)
    sprite('ce602_02', 6)
    sprite('ce602_03', 6)
    Unknown8006(100, 1, 1)
    sprite('ce602_04', 6)
    sprite('ce602_05', 6)
    label(0)
    sprite('ce602_00', 6)
    sprite('ce602_01', 6)
    sprite('ce602_02', 6)
    sprite('ce602_03', 6)
    Unknown8006(100, 1, 1)
    sprite('ce602_04', 6)
    sprite('ce602_05', 6)
    gotoLabel(0)
    label(1)
    sprite('ce602_06', 7)
    Unknown1000(-1194000)
    physicsXImpulse(-2000)
    sprite('ce602_07', 7)
    SFX_0('cloth_l')
    sprite('ce602_08', 8)
    physicsXImpulse(-1000)
    SFX_0('cloth_l')
    sprite('ce602_09', 20)
    physicsXImpulse(0)
    Unknown1000(-1230000)
    Unknown2034(0)
    sprite('ce602_10', 7)
    sprite('ce602_11', 10)
    sprite('ce602_11', 32767)
    label(2)
    sprite('null', 5)
    loopRest()

@State
def EntryCable():

    def upon_IMMEDIATE():
        Unknown2053(1)
        Unknown23013(1)
        Unknown2015(10)
        Unknown4009(3)
        Unknown2055(600)
        SLOT_51 = 1
        SLOT_54 = 0
        physicsXImpulse(70000)
        Unknown2037(0)
        Unknown1108(0)
        Unknown48('010000000200000001000000190000000200000001000000')

        def upon_31():
            Unknown23030('4361626c654472617700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23030('4361626c656a6f696e74000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000')
        Unknown23015(11)
        Unknown23030('4361626c6552656e646572537461676500000000000000000000000000000000000000000c000000000000000d00000000000000000000000000000000000000')

        def upon_48():
            Unknown23030('4361626c6549646c696e670000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        SLOT_54 = 1

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                Unknown23030('4361626c65416e676c654279436861696e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            if SLOT_IsInOverdrive2:
                Unknown1108(0)
            Unknown48('190000000200000034000000030000000200000033000000')
            if (not SLOT_52):
                if (not SLOT_53):
                    Unknown13(25)

        def upon_32():
            clearUponHandler(32)
            sendToLabel(100)
    sprite('null', 1)
    Unknown23030('4361626c65506172616d000000000000000000000000000000000000000000000000000000000000000000005a1e000000000000000000000000000000000000')
    Unknown23030('4361626c65506172616d00000000000000000000000000000000000000000000000000000100000000000000210000000000000000000000000000000a000000')
    Unknown23030('4361626c65506172616d00000000000000000000000000000000000000000000000000000200000000000000420000000000000000000000000000000a000000')
    Unknown23030('4361626c65506172616d000000000000000000000000000000000000000000000000000003000000000000005b1e000000000000000000000000000000000000')
    Unknown23030('4361626c6553706565640000000000000000000000000000000000000000000000000000b80b0000000000000000000000000000000000000000000000000000')
    Unknown23030('4361626c654669727374506f736974696f6e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('vr_ce215_02', 32767)
    loopRest()
    label(100)
    sprite('vr_ce215_02', 2)
    Unknown1019(5)
    sprite('null', 32767)
    physicsXImpulse(0)
    teleportRelativeX(-150000)
    loopRest()
    ExitState()

@State
def MinervaEventIdle():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_6 = 0
        Unknown1086(3)
        teleportRelativeX(-100000)
        Unknown4022(2)
        clearUponHandler(3)
    label(0)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    loopRest()
    gotoLabel(0)

@State
def MinervaEventIdleReverse():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
        SLOT_6 = 0
        Unknown1086(3)
        teleportRelativeX(100000)
        Unknown2005()
        Unknown4022(2)
        clearUponHandler(3)
    label(0)
    sprite('mv000_00', 7)
    sprite('mv000_01', 7)
    sprite('mv000_02', 7)
    sprite('mv000_03', 7)
    sprite('mv000_04', 7)
    sprite('mv000_05', 7)
    sprite('mv000_06', 7)
    sprite('mv000_07', 7)
    sprite('mv000_08', 7)
    sprite('mv000_09', 7)
    loopRest()
    gotoLabel(0)

@State
def MinervaEventPose():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv611_00', 8)
    sprite('mv611_01', 8)
    sprite('mv611_02', 8)
    sprite('mv611_03', 8)
    sprite('mv611_04', 32767)

@State
def MinervaRoundWin():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')

        def upon_32():
            sendToLabel(10)
    sprite('mv030_00', 7)
    Unknown2071('030000006079feff000000001400000000000000')
    label(0)
    sprite('mv030_01', 7)
    sprite('mv030_02', 7)
    sprite('mv030_03', 7)
    sprite('mv030_04', 7)
    sprite('mv030_05', 7)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('mv601_03', 8)
    sprite('mv615_00', 30)
    sprite('mv615_01', 5)
    sprite('mv601_00', 32767)

@State
def ce615Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('ceef_enshutuheal')
    sprite('null', 10)
    label(0)
    sprite('null', 58)
    GFX_0('ceCmnHealAura', -1)
    gotoLabel(0)

@State
def ceCmnHealAura():

    def upon_IMMEDIATE():
        Unknown4003('636565665f636d6e6865616c61757261303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1077(-15000, 10000)
        Unknown3032()
        Unknown1096(650)
        Unknown2054(1)
    sprite('null', 58)
    Unknown3004(-3)
    Unknown1099(10)
    physicsYImpulse(500)

@State
def ce615Eff2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('ceef_enemyhealaura')
        Unknown1086(22)
    sprite('null', 32767)

@State
def ce615Eff3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        GFX_2('ceef_enemyhealaura')
        Unknown1086(24)
    sprite('null', 32767)

@State
def MinervaWin01():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv610_00', 8)
    sprite('mv610_01', 8)
    sprite('mv610_02', 8)
    sprite('mv610_03', 8)
    label(0)
    sprite('mv610_03ex01', 8)
    sprite('mv610_03ex02', 8)
    sprite('mv610_03ex03', 8)
    sprite('mv610_03ex04', 8)
    sprite('mv610_03ex05', 8)
    sprite('mv610_03ex06', 8)
    gotoLabel(0)

@State
def MinervaWin02():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')

        def upon_32():
            sendToLabel(10)

        def upon_41():
            sendToLabel(90)
    sprite('mv030_00', 7)
    Unknown2071('030000006079feff000000001400000000000000')
    label(0)
    sprite('mv030_01', 7)
    sprite('mv030_02', 7)
    sprite('mv030_03', 7)
    sprite('mv030_04', 7)
    sprite('mv030_05', 7)
    sprite('mv030_06', 7)
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('mv611_00', 8)
    sprite('mv611_01', 8)
    sprite('mv611_02', 8)
    sprite('mv611_03', 8)
    sprite('mv611_04', 32767)
    label(90)
    sprite('null', 32767)

@State
def MinervaLose():

    def upon_IMMEDIATE():
        callSubroutine('MV_ActReset')
    sprite('mv620_00', 6)
    sprite('mv620_01', 6)
    sprite('mv620_01ex1', 6)
    sprite('mv620_01ex2', 6)
    sprite('mv620_01ex3', 6)
    sprite('mv620_01ex4', 6)
    sprite('mv620_01ex5', 6)
    sprite('mv620_01ex6', 6)
    sprite('mv620_01ex1', 6)
    sprite('mv620_01ex2', 6)
    sprite('mv620_01ex3', 6)
    sprite('mv620_01ex4', 6)
    sprite('mv620_01ex5', 6)
    sprite('mv620_01ex6', 6)
    sprite('mv620_02', 6)
    sprite('mv620_03', 32767)