@State
def Stand5ACaterpillar():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(3)
        Unknown4026(1)
        Unknown4019(3)
        Unknown2018(1, 30)
        Unknown2020(-240)

        def upon_CLEAR_OR_EXIT():
            if CheckInput(0x6b):
                if (not (SLOT_51 == 5)):
                    SLOT_51 = 5
                    sendToLabel(0)
            if CheckInput(0x78):
                if (not (SLOT_51 == 6)):
                    SLOT_51 = 6
                    sendToLabel(1)
            if CheckInput(0x5e):
                if (not (SLOT_51 == 7)):
                    SLOT_51 = 7
                    sendToLabel(2)
            if SLOT_IsUnlimitedCharacter:
                if (not (SLOT_51 == 6)):
                    SLOT_51 = 6
                    sendToLabel(1)
    label(0)
    sprite('ubl030_00ex', 32767)	# 1-32767
    label(1)
    sprite('ubl030_00ex', 1)	# 32768-32768
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_01ex', 1)	# 32769-32769
    sprite('ubl030_02ex', 1)	# 32770-32770
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_03ex', 1)	# 32771-32771
    sprite('ubl030_04ex', 1)	# 32772-32772
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_05ex', 1)	# 32773-32773
    sprite('ubl030_06ex', 1)	# 32774-32774
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_07ex', 1)	# 32775-32775
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ubl030_07ex', 1)	# 32776-32776
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_06ex', 1)	# 32777-32777
    sprite('ubl030_05ex', 1)	# 32778-32778
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_04ex', 1)	# 32779-32779
    sprite('ubl030_03ex', 1)	# 32780-32780
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_02ex', 1)	# 32781-32781
    sprite('ubl030_01ex', 1)	# 32782-32782
    GFX_0('ubl_forward_Eff', 100)
    sprite('ubl030_00ex', 1)	# 32783-32783
    loopRest()
    gotoLabel(2)

@State
def Air5CShakeAtk():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(5)
        Damage(800)
        AttackP1(60)
        AttackP2(90)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        HitLow(100)
        HitOverhead(100)
        Unknown11084(1)
        Unknown48('19000000020000003300000016000000020000001e000000')
        if (not SLOT_51):
            Unknown11025(1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(3, 1011, 0)
        Hitstop(0)
        AirPushbackX(6000)
        AirPushbackY(8000)
        Unknown9310(1)
        Unknown1056(4000)
    sprite('vr_dmy_jishin', 1)	# 1-1	 **attackbox here**
    SFX_0('016_explode_0')

@State
def EffOffensiveGuardStart():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown48('190000000200000033000000160000000200000024000000')
        teleportRelativeX(-140000)
        Unknown1007(-170000)
    if SLOT_51:
        _gotolabel(1)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('Action_121_00', 6)	# 2-7
    sprite('Action_121_01', 6)	# 8-13
    sprite('Action_121_02', 1)	# 14-14
    loopRest()
    ExitState()
    label(1)
    sprite('Action_123_00', 6)	# 15-20
    sprite('Action_123_01', 6)	# 21-26
    sprite('Action_123_02', 1)	# 27-27
    loopRest()
    ExitState()

@State
def EffOffensiveGuardBarier():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_120_00', 5)	# 1-5
    sprite('Action_120_01', 5)	# 6-10
    sprite('Action_120_02', 5)	# 11-15
    sprite('Action_120_03', 5)	# 16-20
    sprite('Action_120_04', 5)	# 21-25
    sprite('Action_120_05', 5)	# 26-30
    sprite('Action_120_06', 5)	# 31-35

@State
def EffOffensiveGuardSuccess():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_124_00', 4)	# 1-4
    sprite('Action_124_01', 4)	# 5-8
    sprite('Action_124_02', 4)	# 9-12
    sprite('Action_124_03', 4)	# 13-16
    sprite('Action_124_04', 1)	# 17-17

@State
def EffOffensiveGuardCounter():

    def upon_IMMEDIATE():
        Unknown1007(250000)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('null', 1)	# 1-1
    label(0)
    sprite('Action_126_00', 4)	# 2-5
    sprite('Action_126_01', 4)	# 6-9
    sprite('Action_126_02', 1)	# 10-10
    label(1)
    sprite('Action_126_04', 4)	# 11-14
    sprite('Action_126_05', 4)	# 15-18
    sprite('Action_126_06', 1)	# 19-19

@Subroutine
def ShotBeamInit():
    Unknown2010()
    Unknown4007(3)
    Unknown4009(3)
    Unknown4010(2)
    AttackLevel_(3)
    Damage(1500)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(19000)
    AirPushbackY(15000)
    AirUntechableTime(40)
    PushbackX(12000)
    Unknown9015(1)
    Unknown9266(6)
    DisableAttackRestOfMove()
    Unknown23089('0100000000000000000000000000000000000000010000000100000001000000')

    def upon_54():
        clearUponHandler(54)
        Unknown4007(0)
        Unknown4009(0)
        sendToLabel(9)

@State
def ShotBeam_Low():

    def upon_IMMEDIATE():
        callSubroutine('ShotBeamInit')
        Unknown1072(55000)
        teleportRelativeX(-10000)
        Unknown1007(-10000)
    sprite('null', 1)	# 1-1
    GFX_0('ubl_BeamA_Eff', 100)
    sprite('vr_ubl_NormalShotAtkCol00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ubl_NormalShotAtkCol00', 10)	# 5-14	 **attackbox here**
    DisableAttackRestOfMove()
    label(9)
    sprite('null', 1)	# 15-15

@State
def ShotBeam_Middle():

    def upon_IMMEDIATE():
        callSubroutine('ShotBeamInit')
        Unknown1072(20000)
        teleportRelativeX(-10000)
        Unknown1007(-10000)

        def upon_43():
            if (SLOT_48 == 1101):
                AttackP1(70)
                Unknown11042(1)
    sprite('null', 1)	# 1-1
    GFX_0('ubl_BeamB_Eff', 100)
    sprite('vr_ubl_NormalShotAtkCol00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ubl_NormalShotAtkCol00', 10)	# 5-14	 **attackbox here**
    DisableAttackRestOfMove()
    label(9)
    sprite('null', 1)	# 15-15

@State
def ShotBeam_High():

    def upon_IMMEDIATE():
        callSubroutine('ShotBeamInit')
    sprite('null', 1)	# 1-1
    GFX_0('ubl_BeamC_Eff', 100)
    sprite('vr_ubl_NormalShotAtkCol00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ubl_NormalShotAtkCol00', 10)	# 5-14	 **attackbox here**
    DisableAttackRestOfMove()
    label(9)
    sprite('null', 1)	# 15-15

@State
def AirShotBeam_Low():

    def upon_IMMEDIATE():
        callSubroutine('ShotBeamInit')
        Unknown1072(55000)
        teleportRelativeX(-10000)
        Unknown1007(-10000)
    sprite('null', 1)	# 1-1
    GFX_0('ubl_AirBeamA_Eff', 100)
    sprite('vr_ubl_NormalShotAtkCol00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ubl_NormalShotAtkCol00', 10)	# 5-14	 **attackbox here**
    DisableAttackRestOfMove()
    label(9)
    sprite('null', 1)	# 15-15

@State
def AirShotBeam_Middle():

    def upon_IMMEDIATE():
        callSubroutine('ShotBeamInit')
        Unknown1072(35000)
        Unknown1072(35000)
        teleportRelativeX(-10000)
        Unknown1007(-10000)
    sprite('null', 1)	# 1-1
    GFX_0('ubl_AirBeamB_Eff', 100)
    sprite('vr_ubl_NormalShotAtkCol00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ubl_NormalShotAtkCol00', 10)	# 5-14	 **attackbox here**
    DisableAttackRestOfMove()
    label(9)
    sprite('null', 1)	# 15-15

@State
def AirShotBeam_High():

    def upon_IMMEDIATE():
        callSubroutine('ShotBeamInit')
        Unknown1072(20000)
    sprite('null', 1)	# 1-1
    GFX_0('ubl_AirBeamC_Eff', 100)
    sprite('vr_ubl_NormalShotAtkCol00', 3)	# 2-4	 **attackbox here**
    RefreshMultihit()
    sprite('vr_ubl_NormalShotAtkCol00', 10)	# 5-14	 **attackbox here**
    DisableAttackRestOfMove()
    label(9)
    sprite('null', 1)	# 15-15

@Subroutine
def GrenadeShot_Init():
    Unknown2010()
    Unknown4011(2)
    AttackLevel_(2)
    Damage(0)
    AttackP2(100)
    AttackP1(100)
    Hitstop(0)
    PushbackX(12000)
    physicsYImpulse(35800)
    setGravity(1800)
    Unknown1056(500)
    Unknown1064(500)
    Unknown2015(35)
    Unknown2016(20)
    Unknown23087(20)
    Unknown2053(1)

    def upon_7():
        Unknown1028(0)
        Unknown1019(0)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(2)
        clearUponHandler(10)
        sendToLabel(1)

    def upon_LANDING():
        clearUponHandler(2)
        clearUponHandler(10)
        sendToLabel(1)

@Subroutine
def GrenadeShot2nd_Atk():
    Unknown2010()
    AttackLevel_(2)
    Damage(1500)
    AttackP2(85)
    AirPushbackX(15000)
    AirPushbackY(15000)
    PushbackX(12000)
    Unknown9266(6)
    Unknown1056(1000)
    Unknown1064(1000)
    Unknown1084(1)
    Unknown11001(0, 25, 25)
    SFX_0('013_thunder_0')
    SFX_0('014_electric_ml')
    if SLOT_2:
        MinimumDamagePct(10)
        Unknown30065(0)

@State
def GrenadeA_Shot():

    def upon_IMMEDIATE():
        callSubroutine('GrenadeShot_Init')
        GFX_0('ubl_Grenade_Shot_Eff', 100)
        physicsXImpulse(15000)

        def upon_43():
            if (SLOT_48 == 1012):
                Unknown2037(1)
                Unknown1015(4800)
    label(0)
    sprite('vr_Grenade_col00ex', 2)	# 1-2
    Unknown4049(900)
    Unknown4054(11)
    Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
    sprite('vr_Grenade_col01ex', 2)	# 3-4
    Unknown4049(900)
    Unknown4054(11)
    Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ubl_GranadeAtkCol00', 3)	# 5-7	 **attackbox here**
    RefreshMultihit()
    callSubroutine('GrenadeShot2nd_Atk')
    Unknown4049(1300)
    Unknown4045('75626c65665f3430325f737061726b000000000000000000000000000000000064000000')
    Unknown1084(1)
    sprite('null', 1)	# 8-8
    loopRest()
    ExitState()
    label(9)
    sprite('null', 1)	# 9-9

@State
def GrenadeB_Shot():

    def upon_IMMEDIATE():
        callSubroutine('GrenadeShot_Init')
        GFX_0('ubl_Grenade_Shot_Eff', 100)
        physicsXImpulse(21000)

        def upon_43():
            if (SLOT_48 == 1013):
                Unknown2037(1)
                Unknown1015(4800)
    label(0)
    sprite('vr_Grenade_col00ex', 2)	# 1-2
    Unknown4049(900)
    Unknown4054(11)
    Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
    sprite('vr_Grenade_col01ex', 2)	# 3-4
    Unknown4049(900)
    Unknown4054(11)
    Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ubl_GranadeAtkCol00', 3)	# 5-7	 **attackbox here**
    RefreshMultihit()
    callSubroutine('GrenadeShot2nd_Atk')
    Unknown4049(1300)
    Unknown4045('75626c65665f3430325f737061726b000000000000000000000000000000000064000000')
    Unknown1084(1)
    sprite('null', 1)	# 8-8
    loopRest()
    ExitState()
    label(9)
    sprite('null', 1)	# 9-9

@State
def GrenadeC_Shot():

    def upon_IMMEDIATE():
        callSubroutine('GrenadeShot_Init')
        GFX_0('ubl_Grenade_Shot_Eff', 100)
        physicsXImpulse(26000)

        def upon_43():
            if (SLOT_48 == 1014):
                Unknown2037(1)
    label(0)
    sprite('vr_Grenade_col00ex', 2)	# 1-2
    Unknown4049(900)
    Unknown4054(11)
    Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
    sprite('vr_Grenade_col01ex', 2)	# 3-4
    Unknown4049(900)
    Unknown4054(11)
    Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('vr_ubl_GranadeAtkCol00', 3)	# 5-7	 **attackbox here**
    RefreshMultihit()
    callSubroutine('GrenadeShot2nd_Atk')
    Unknown4049(1300)
    Unknown4045('75626c65665f3430325f737061726b000000000000000000000000000000000064000000')
    Unknown1084(1)
    sprite('null', 1)	# 8-8
    loopRest()
    ExitState()
    label(9)
    sprite('null', 1)	# 9-9

@State
def UltimateBeam_AtkCol():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(600)
        MinimumDamagePct(11)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        Unknown9266(6)
        AirUntechableTime(60)
        AirPushbackX(70000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(1000)
        Hitstop(20)
        PushbackX(12000)
        Unknown30056('f04902001e00000000000000')
        Unknown11110(80)
        DisableAttackRestOfMove()
        WallbounceReboundTime(0)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4010(3)
        SLOT_51 = 26
        SLOT_53 = 10
        SLOT_52 = SLOT_51
        SLOT_52 = (SLOT_52 - SLOT_53)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(0, 5000)

        def upon_43():
            if (SLOT_48 == 2001):
                Damage(350)
                SLOT_51 = 52
                SLOT_52 = SLOT_51
                SLOT_52 = (SLOT_52 - SLOT_53)
            if (SLOT_48 == 2002):
                Damage(100)
                Hitstop(20)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                SLOT_51 = 20
                SLOT_52 = SLOT_51
                SLOT_52 = (SLOT_52 - SLOT_53)
            if (SLOT_48 == 2003):
                Damage(50)
                Hitstop(20)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                SLOT_51 = 50
                SLOT_52 = SLOT_51
                SLOT_52 = (SLOT_52 - SLOT_53)
            if (SLOT_48 == 2000):
                sendToLabel(9)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 == SLOT_51):
                Unknown26('ubl_UltimateBeam_Eff')
                Unknown26('ubl_UltimateBeam_Muzzle_Eff')
                Unknown26('ubl_UltimateBeam_Wave_Eff')
                GFX_0('ubl_UltimateBeam_End_Eff', 0)
            if (SLOT_2 > SLOT_51):
                DisableAttackRestOfMove()
                Unknown23022(1)
    label(0)
    sprite('vr_ubl_UltimateBeamAtkCol00', 2)	# 1-2	 **attackbox here**
    RefreshMultihit()
    Unknown2038(1)
    if (not (SLOT_2 > 26)):
        pass
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('null', 30)	# 3-32

    @State
    def UltimateRush_CameraObj():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown20000(1)

            def upon_43():
                if (SLOT_48 == 2101):
                    sendToLabel(9)
            teleportRelativeX(300000)
        sprite('null', 999)	# 1-999
        label(9)
        sprite('null', 1)	# 1000-1000
        Unknown20000(0)

    @State
    def Grenade_Shot_Astral():

        def upon_IMMEDIATE():
            Unknown2012()
            Unknown4011(2)
            AttackLevel_(2)
            Damage(0)
            AttackP2(100)
            AttackP1(100)
            MinimumDamagePct(100)
            Hitstop(0)
            PushbackX(12000)
            SFX_0('016_explode_1')
            physicsYImpulse(35800)
            setGravity(1800)
            Unknown1056(500)
            Unknown1064(500)
            GFX_0('ubl_Grenade_Shot_Eff', 100)
            physicsXImpulse(26000)
            physicsYImpulse(56000)
            Unknown2003(1)

            def upon_CLEAR_OR_EXIT():
                if (SLOT_18 == 20):
                    sendToLabel(10)
                if SLOT_51:
                    SLOT_52 = (SLOT_52 + 1)
                    if (SLOT_52 >= 40):
                        clearUponHandler(3)
                        sendToLabel(1)

            def upon_43():
                if (SLOT_48 == 3004):
                    Unknown1086(22)
                    teleportRelativeX(-1100000)
                    Unknown1007(300000)
                    setGravity(1800)
                    physicsXImpulse(26000)
                    physicsYImpulse(26000)
                    loopRelated(17, 20)

                    def upon_17():
                        clearUponHandler(17)
                        sendToLabel(1)
                    SLOT_51 = (SLOT_51 + 1)
                    sendToLabel(0)
                if (SLOT_48 == 3005):
                    Unknown1086(22)
                    teleportRelativeX(-1050000)
                    Unknown1007(450000)
                    physicsXImpulse(26000)
                    physicsYImpulse(28000)
                    setGravity(1800)
                    loopRelated(17, 32)

                    def upon_17():
                        clearUponHandler(17)
                        sendToLabel(1)
                    SLOT_51 = (SLOT_51 + 1)
                    sendToLabel(0)
        label(0)
        sprite('vr_Grenade_col00ex', 1)	# 1-1
        StartMultihit()
        Unknown4049(900)
        Unknown4054(11)
        Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
        sprite('vr_Grenade_col00ex', 1)	# 2-2
        StartMultihit()
        sprite('vr_Grenade_col01ex', 1)	# 3-3
        StartMultihit()
        Unknown4049(900)
        Unknown4054(11)
        Unknown4045('75626c65665f3430325f736d6f6b65000000000000000000000000000000000064000000')
        sprite('vr_Grenade_col01ex', 1)	# 4-4
        StartMultihit()
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('vr_ubl_GranadeAtkCol00', 3)	# 5-7	 **attackbox here**
        RefreshMultihit()
        Unknown2003(0)
        AttackLevel_(2)
        Damage(1500)
        AttackP2(85)
        AirPushbackX(15000)
        AirPushbackY(15000)
        PushbackX(12000)
        Unknown9266(6)
        Unknown1056(1000)
        Unknown1064(1000)
        Unknown11023(1)
        Unknown11069('IchigekiCameraFinishAtkCol')
        Unknown1084(1)
        Unknown11001(0, 999, 999)
        SFX_0('013_thunder_0')
        SFX_0('016_explode_1')
        SFX_0('013_thunder_0')
        Unknown4049(1300)
        Unknown4045('75626c65665f3430325f737061726b000000000000000000000000000000000064000000')
        Unknown1084(1)
        sprite('null', 1)	# 8-8
        loopRest()
        ExitState()
        label(10)
        sprite('null', 999)	# 9-1007
        Unknown1084(1)
        setGravity(0)
        label(9)
        sprite('null', 1)	# 1008-1008

    @State
    def IchigekiCamera():

        def upon_IMMEDIATE():

            def upon_43():
                if (SLOT_48 == 3001):
                    sendToLabel(0)
                if (SLOT_48 == 3000):
                    sendToLabel(1)
                if (SLOT_48 == 3002):
                    sendToLabel(3)
                if (SLOT_48 == 3003):
                    Unknown20000(0)
                    Unknown13(25)
            Unknown2054(1)
            Unknown2053(0)
            Unknown2034(0)
            Unknown3038(1)
            Unknown20000(1)
        label(0)
        sprite('keep', 1)	# 1-1
        Unknown1086(3)
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown20003(1)
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('keep', 32767)	# 2-32768
        Unknown1086(22)
        Unknown1084(1)
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown20003(1)
        loopRest()
        label(3)
        sprite('keep', 999)	# 32769-33767
        Unknown20000(1)
        Unknown20001(1)
        Unknown20002(1)
        Unknown20003(1)
        physicsXImpulse(-80000)

    @State
    def IchigekiCameraFinishAtkCol():

        def upon_IMMEDIATE():
            Unknown2012()
            Unknown3038(1)
            Unknown2034(0)
            Unknown2053(0)
            AttackLevel_(5)
            Damage(200)
            AirUntechableTime(180)
            Hitstop(0)
            AirHitstunAnimation(18)
            Unknown11064(1)
            Unknown11023(1)
            Unknown11067(1)
            Unknown11072(1, 0, 0)
            Unknown9266(6)
            Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            YImpluseBeforeWallbounce(0)
            MinimumDamagePct(100)
            Unknown1096(1500)

            def upon_CLEAR_OR_EXIT():
                Unknown1086(22)
            Unknown2037(0)
        sprite('vr_ubl_AH_ShotAtkCol', 2)	# 1-2	 **attackbox here**
        label(0)
        sprite('vr_ubl_AH_ShotAtkCol', 2)	# 3-4	 **attackbox here**
        RefreshMultihit()
        ScreenShake(0, 8000)
        if (SLOT_2 > 47):
            gotoLabel(9)
        Unknown2038(1)
        loopRest()
        gotoLabel(0)
        label(9)
        sprite('vr_ubl_AH_ShotAtkCol', 1)	# 5-5	 **attackbox here**
        RefreshMultihit()
        Unknown11023(1)
        Damage(15166)
        Unknown11064(3)
        AirPushbackX(150000)
        AirPushbackY(5000)
        YImpluseBeforeWallbounce(0)
        Unknown11072(0, 0, 0)
        SFX_0('016_explode_2')
        SFX_0('016_explode_2')
        sprite('vr_ubl_AH_ShotAtkCol', 1)	# 6-6	 **attackbox here**
        Unknown36(22)
        Unknown1084(1)
        Unknown3038(1)
        teleportRelativeY(0)
        Unknown35()

    @State
    def UBLAstBG_Start():

        def upon_IMMEDIATE():
            Unknown2035(1)
            teleportRelativeY(0)
            Unknown2019(1000)
            Unknown3033()
            Unknown3001(0)
            Unknown3004(50)
            Unknown1056(10000)
            Unknown1064(2200)
        label(0)
        sprite('null', 60)	# 1-60
        GFX_1('ublef_450_smoke', -1)
        loopRest()
        gotoLabel(0)

    @State
    def ubl_forward_Eff():

        def upon_IMMEDIATE():
            pass
        sprite('vr_ublef_Smoke', 1)	# 1-1
        GFX_1('ublef_forward_s', 0)
        GFX_1('ublef_forward', 1)
        GFX_1('ublef_forward_s', 2)
        GFX_1('ublef_forward', 3)
        GFX_1('ublef_forward_s', 4)

    @State
    def ubl_backward_Eff():

        def upon_IMMEDIATE():
            pass
        sprite('vr_ublef_Smoke', 1)	# 1-1
        GFX_1('ublef_backward_s', 0)
        GFX_1('ublef_backward', 1)
        GFX_1('ublef_backward_s', 2)
        GFX_1('ublef_backward', 3)
        GFX_1('ublef_backward_s', 4)

    @State
    def ubl_Dash_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown2054(1)
        label(0)
        sprite('vr_ublef_Smoke', 4)	# 1-4
        GFX_1('ublef_forward_s', 0)
        GFX_1('ublef_forward', 1)
        GFX_1('ublef_forward_s', 2)
        GFX_1('ublef_forward', 3)
        GFX_1('ublef_forward_s', 4)
        GFX_0('ubl_dashsmoke_Eff', 3)
        GFX_1('ublef_dash', 1)
        GFX_1('ublef_dash', 3)
        GFX_1('ublef_dashsmoke', 3)
        gotoLabel(0)

    @State
    def ubl_dashsmoke_Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            GFX_2('ublef_dashsmoke2')
            Unknown2054(1)
        sprite('null', 10)	# 1-10

    @State
    def ubl_BDash_Eff():

        def upon_IMMEDIATE():
            pass
        sprite('vr_ublef_Smoke', 1)	# 1-1
        GFX_1('ublef_backward_s', 0)
        GFX_1('ublef_backward', 1)
        GFX_1('ublef_backward_s', 2)
        GFX_1('ublef_backward', 3)
        GFX_1('ublef_backward_s', 4)
        GFX_1('ublef_backdash', 0)
        GFX_1('ublef_backdash', 4)

    @State
    def ubl_Brake_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
        sprite('vr_ublef_Brake', 2)	# 1-2
        GFX_1('ublef_brake', 0)
        GFX_1('ublef_brake', 1)
        GFX_1('ublef_brake', 2)
        sprite('vr_ublef_Brake', 2)	# 3-4
        GFX_1('ublef_brake', 0)
        GFX_1('ublef_brake', 1)
        GFX_1('ublef_brake', 2)
        sprite('vr_ublef_Brake', 2)	# 5-6
        GFX_1('ublef_brake', 0)
        GFX_1('ublef_brake', 1)
        GFX_1('ublef_brake', 2)

    @State
    def ubl_450_backward_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown2054(1)
        label(0)
        sprite('vr_ublef_Smoke', 4)	# 1-4
        GFX_1('ublef_backward_s', 0)
        GFX_1('ublef_backward', 1)
        GFX_1('ublef_backward_s', 2)
        GFX_1('ublef_backward', 3)
        GFX_1('ublef_backward_s', 4)
        GFX_1('ublef_450_backward', 0)
        GFX_1('ublef_450_backward', 1)
        GFX_1('ublef_450_backward', 3)
        GFX_1('ublef_450_backward', 4)
        gotoLabel(0)

    @State
    def ubl_230_Eff():

        def upon_IMMEDIATE():
            pass
        sprite('null', 1)	# 1-1
        GFX_1('ublef_230_smoke', 100)

    @State
    def ubl_231_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown4009(2)
            teleportRelativeX(160000)
        sprite('null', 3)	# 1-3
        GFX_1('ublef_231_smoke', 100)
        sprite('null', 3)	# 4-6
        GFX_1('ublef_231_smoke', 100)
        sprite('null', 3)	# 7-9
        GFX_1('ublef_231_smoke', 100)

    @State
    def ubl_232_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            teleportRelativeX(80000)
        label(0)
        sprite('null', 3)	# 1-3
        GFX_0('ubl_232_smoke_Eff', 100)
        GFX_1('ublef_231_smoke00', 100)
        gotoLabel(0)

    @State
    def ubl_232_smoke_Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            GFX_2('ublef_232_smoke')
        sprite('null', 60)	# 1-60
        loopRest()

    @State
    def ubl_232_b_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
        label(0)
        sprite('null', 3)	# 1-3
        GFX_0('ubl_232_b_smoke_Eff', 100)
        GFX_1('ublef_230_smoke00', 100)
        gotoLabel(0)

    @State
    def ubl_232_b_smoke_Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            GFX_2('ublef_232_smoke_b')
        sprite('null', 60)	# 1-60
        loopRest()

    @State
    def ubl_200_Vulcan_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            teleportRelativeX(45000)
            Unknown1007(5000)
            Unknown1096(1900)
            GFX_2('ublef_200_Muzzle')
        sprite('null', 15)	# 1-15
        loopRest()

    @State
    def ubl_270_Shot_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            teleportRelativeX(45000)
            Unknown1007(5000)
            Unknown1096(1900)
            GFX_2('ublef_200_Muzzle')
        sprite('null', 15)	# 1-15
        loopRest()

    @State
    def ubl_270_Bomb_Eff():

        def upon_IMMEDIATE():
            Unknown4054(6)
            Unknown23067('ublef_200_Bomb')
            Unknown1096(1750)
        sprite('null', 60)	# 1-60
        GFX_0('ubl_270_Bomb01_Eff', 100)
        SFX_0('016_explode_2')
        loopRest()

    @State
    def ubl_270_Bomb01_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown23015(10)
            Unknown4003('75626c65665f3237305f626f6d6230302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3032()
            Unknown1096(6500)
            Unknown1099(300)
            Unknown1077(360000, -360000)
        sprite('null', 8)	# 1-8
        sprite('null', 10)	# 9-18
        Unknown3004(-25)
        loopRest()

    @State
    def ubl_201_Fire_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4007(3)
            teleportRelativeX(108000)
            Unknown1007(-40000)
            Unknown1007(40000)
            Unknown1096(1500)
            GFX_2('ublef_201_fire')
        sprite('null', 90)	# 1-90
        loopRest()

    @State
    def ubl_250_Vulcan_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            teleportRelativeX(40000)
            Unknown1096(1900)
            GFX_2('ublef_200_Muzzle')
        sprite('null', 15)	# 1-15
        loopRest()

    @State
    def ubl_251_Shot_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            teleportRelativeX(40000)
            Unknown1007(-35000)
            Unknown1072(50000)
            Unknown1096(1900)
            GFX_2('ublef_200_Muzzle')
        sprite('null', 15)	# 1-15
        loopRest()

    @State
    def ubl_251_Bomber_Eff():

        def upon_IMMEDIATE():
            Unknown4007(2)
            Unknown4010(2)
            teleportRelativeX(-15000)
            Unknown1007(25000)
        sprite('null', 1)	# 1-1
        GFX_0('ubl_251_Bomb_Eff', 100)
        Unknown4054(6)
        Unknown4049(1600)
        Unknown4045('75626c65665f3230305f426f6d6200000000000000000000000000000000000064000000')
        SFX_0('016_explode_2')
        loopRest()

    @State
    def ubl_251_Bomb_Eff():

        def upon_IMMEDIATE():
            Unknown23015(10)
            Unknown4003('75626c65665f3237305f626f6d6230302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3032()
            Unknown1096(6500)
            Unknown1099(300)
            Unknown1077(360000, -360000)
        sprite('null', 6)	# 1-6
        sprite('null', 10)	# 7-16
        Unknown3004(-30)
        loopRest()

    @State
    def ubl_310_NearSpark_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown1096(1000)
            teleportRelativeX(-45000)
            Unknown23067('ublef_310_spark05')
        sprite('null', 70)	# 1-70
        loopRest()

    @State
    def ubl_320_NearSpark_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown1096(1000)
            teleportRelativeX(-45000)
            Unknown23067('ublef_310_spark05')
        sprite('null', 40)	# 1-40
        loopRest()

    @State
    def ubl_310_BackSpark_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4054(11)
            Unknown1096(1000)
            Unknown23067('ublef_310_sparkF04')
        sprite('null', 18)	# 1-18
        sprite('null', 2)	# 19-20
        GFX_0('ubl_310_Thunder00_Eff', 100)
        sprite('null', 2)	# 21-22
        GFX_0('ubl_310_Thunder01_Eff', 100)
        sprite('null', 2)	# 23-24
        GFX_0('ubl_310_Thunder02_Eff', 100)
        sprite('null', 16)	# 25-40
        GFX_0('ubl_310_Thunder01_Eff', 100)
        sprite('null', 2)	# 41-42
        GFX_0('ubl_310_Thunder02_Eff', 100)
        sprite('null', 12)	# 43-54
        loopRest()

    @State
    def ubl_310_Thunder00_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f7468756e64657230302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(-110000)
            Unknown1007(215000)
            Unknown1056(2400)
            Unknown1064(1870)
            Unknown3002(-70)
            Unknown3001(120)
        sprite('null', 2)	# 1-2
        loopRest()

    @State
    def ubl_310_Thunder01_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f7468756e64657230312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(-110000)
            Unknown1007(215000)
            Unknown1056(2400)
            Unknown1064(1870)
            Unknown3002(-70)
            Unknown3001(120)
        sprite('null', 2)	# 1-2
        loopRest()

    @State
    def ubl_310_Thunder02_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f7468756e64657230322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(-110000)
            Unknown1007(215000)
            Unknown1056(2400)
            Unknown1064(1870)
            Unknown3002(-70)
            Unknown3001(120)
        sprite('null', 2)	# 1-2
        loopRest()

    @State
    def ublef_Idling_Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            Unknown1096(800)
            Unknown23067('ublef_steam05')
        sprite('null', 60)	# 1-60

    @State
    def ublef_smoke_Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            Unknown1056(2500)
            Unknown1064(2250)
            Unknown3033()
            Unknown1007(-38500)
            teleportRelativeX(-13000)
            Unknown3001(0)
            Unknown4003('75626c65665f736d6f6b652e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        sprite('null', 7)	# 1-7
        sprite('null', 5)	# 8-12
        Unknown3004(40)
        sprite('null', 23)	# 13-35
        sprite('null', 8)	# 36-43
        Unknown3004(-30)

    @State
    def XhitEff_Denkou():

        def upon_IMMEDIATE():
            Unknown2006()
            Unknown1086(22)
            teleportRelativeY(200000)
        sprite('null', 22)	# 1-22
        GFX_1('ef_hitx_den', 0)

    @State
    def ubl_BeamA_Eff():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4011(3)
            Unknown4007(3)
            GFX_2('ublef_400_Beam')
            Unknown1072(53000)
        sprite('null', 4)	# 1-4
        sprite('null', 50)	# 5-54
        GFX_0('ubl_BeamEndA_Eff', 100)
        loopRest()

    @State
    def ubl_BeamEndA_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            GFX_2('ublef_400_BeamEnd')
            Unknown1072(53000)
            Unknown1096(700)
        sprite('null', 50)	# 1-50
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_BeamB_Eff():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4011(3)
            Unknown4007(3)
            GFX_2('ublef_400_Beam')
            Unknown1072(20000)
        sprite('null', 4)	# 1-4
        sprite('null', 50)	# 5-54
        GFX_0('ubl_BeamEndB_Eff', 100)
        loopRest()

    @State
    def ubl_BeamEndB_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            GFX_2('ublef_400_BeamEnd')
            Unknown1072(20000)
            Unknown1096(700)
        sprite('null', 50)	# 1-50
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_BeamC_Eff():

        def upon_IMMEDIATE():
            Unknown4010(3)
            Unknown4011(3)
            Unknown4007(3)
            GFX_2('ublef_400_Beam')
            Unknown1072(0)
        sprite('null', 4)	# 1-4
        sprite('null', 50)	# 5-54
        GFX_0('ubl_BeamEndC_Eff', 100)
        loopRest()

    @State
    def ubl_BeamEndC_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            GFX_2('ublef_400_BeamEnd')
            Unknown1072(0)
            Unknown1096(700)
        sprite('null', 50)	# 1-50
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_AirBeamA_Eff():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4007(3)
            GFX_2('ublef_400_Beam')
            Unknown1072(57000)
        sprite('null', 4)	# 1-4
        sprite('null', 50)	# 5-54
        Unknown4007(0)
        GFX_0('ubl_AirBeamEndA_Eff', 100)
        loopRest()

    @State
    def ubl_AirBeamEndA_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            GFX_2('ublef_400_BeamEnd')
            Unknown1072(57000)
            Unknown1096(700)
        sprite('null', 50)	# 1-50
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_AirBeamB_Eff():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4007(3)
            GFX_2('ublef_400_Beam')
            Unknown1072(35000)
        sprite('null', 4)	# 1-4
        sprite('null', 50)	# 5-54
        Unknown4007(0)
        GFX_0('ubl_AirBeamEndB_Eff', 100)
        loopRest()

    @State
    def ubl_AirBeamEndB_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            GFX_2('ublef_400_BeamEnd')
            Unknown1072(35000)
            Unknown1096(700)
        sprite('null', 50)	# 1-50
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_AirBeamC_Eff():

        def upon_IMMEDIATE():
            Unknown4011(3)
            Unknown4007(3)
            GFX_2('ublef_400_Beam')
            Unknown1072(20000)
        sprite('null', 4)	# 1-4
        sprite('null', 50)	# 5-54
        Unknown4007(0)
        GFX_0('ubl_AirBeamEndC_Eff', 100)
        loopRest()

    @State
    def ubl_AirBeamEndC_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            GFX_2('ublef_400_BeamEnd')
            Unknown1072(20000)
            Unknown1096(700)
        sprite('null', 50)	# 1-50
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_Grenade_Shot_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown1096(1200)
            GFX_2('ublef_402_Bomb')
        sprite('null', 32767)	# 1-32767

    @State
    def ubl_UltimateBeam_Charge_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown2054(1)
            teleportRelativeX(72000)
        label(0)
        sprite('null', 5)	# 1-5
        GFX_0('ubl_UltimateBeam_Charge00_Eff', 100)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_UltimateBeam_Charge00_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown2054(1)
            GFX_2('ublef_430_Charge')
        sprite('null', 160)	# 1-160
        loopRest()

    @State
    def ubl_UltimateBeam_Lightbullet_Ef():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown2054(1)
            Unknown1096(1600)
            teleportRelativeX(-10000)
            GFX_2('ublef_430_Lightbullet02')
        sprite('null', 160)	# 1-160
        loopRest()

    @State
    def ubl_UltimateBeam_Muzzle_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown2054(1)
            GFX_2('ublef_430_Muzzle00')
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_UltimateBeam_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
        label(0)
        sprite('null', 2)	# 1-2
        GFX_0('ubl_UltimateBeam_Beam_Eff', 100)
        GFX_0('ubl_UltimateBeam_Beam00_Eff', 100)
        GFX_0('ubl_UltimateBeam_Ground_Eff', 100)
        SFX_0('016_explode_1')
        SFX_0('014_electric_m')
        gotoLabel(0)
        loopRest()

    @State
    def ubl_UltimateBeam_Beam_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown4054(6)
            Unknown23067('ublef_430_Beam')
        sprite('null', 30)	# 1-30
        loopRest()

    @State
    def ubl_UltimateBeam_Beam00_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown4054(6)
            Unknown1000(3500000)
            Unknown1064(1000)
            Unknown23067('ublef_450_Beam03')
            Unknown3001(255)
        sprite('null', 30)	# 1-30
        loopRest()

    @State
    def ubl_UltimateBeam_Ground_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            GFX_2('ublef_430_Ground03')
        sprite('null', 40)	# 1-40
        loopRest()

    @State
    def ubl_UltimateBeam_Wave_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
        label(0)
        sprite('null', 7)	# 1-7
        GFX_0('ubl_UltimateBeam_Wave00_Eff', 100)
        sprite('null', 7)	# 8-14
        GFX_0('ubl_UltimateBeam_Wave01_Eff', 100)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_UltimateBeam_Wave00_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown4003('75626c65665f7761766530302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(7)
            Unknown3032()
            Unknown1062(9000, 7500)
            Unknown1070(6200, 5200)
            Unknown1059(-80)
        sprite('null', 19)	# 1-19
        loopRest()

    @State
    def ubl_UltimateBeam_Wave01_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            Unknown4003('75626c65665f7761766530312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(7)
            Unknown3032()
            Unknown1062(9000, 7500)
            Unknown1070(4500, 3500)
            Unknown1059(-80)
        sprite('null', 19)	# 1-19
        loopRest()

    @State
    def ubl_UltimateBeam_End_Eff():

        def upon_IMMEDIATE():
            Unknown4007(2)
            teleportRelativeX(50000)
        sprite('null', 4)	# 1-4
        Unknown4045('75626c65665f3433305f4265616d6b653030340000000000000000000000000064000000')
        SFX_0('014_electric_sl')
        sprite('null', 1)	# 5-5
        Unknown4049(1100)
        Unknown4045('75626c65665f3433305f4265616d456e6400000000000000000000000000000064000000')
        SFX_0('014_electric_sl')
        loopRest()

    @State
    def ubl_431_Smoke_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown3038(1)
            Unknown2054(1)
        label(0)
        sprite('vr_ublef431_foot', 1)	# 1-1
        GFX_0('ubl_431_Smoke00_Eff', 5)
        GFX_1('ublef_431_fire', 0)
        GFX_1('ublef_431_fire', 3)
        GFX_1('ublef_431_fire2', 0)
        GFX_1('ublef_431_fire2', 3)
        GFX_1('ublef_431_fire_b', 6)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_431_Smoke00_Eff():

        def upon_IMMEDIATE():
            Unknown4007(3)
            Unknown2054(1)
            GFX_2('ublef_431_smoke2')
        sprite('null', 80)	# 1-80
        loopRest()

    @State
    def ubl_431_Eyes_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4007(2)
            Unknown2054(1)
        sprite('null', 65)	# 1-65
        sprite('vr_ublef431_eyes', 60)	# 66-125
        GFX_0('ubl_Eye00_Eff', 0)
        GFX_0('ubl_Eye01_Eff', 1)
        SFX_3('ublse_10')
        loopRest()

    @State
    def ubl_431_Dash_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown4009(3)
        label(0)
        sprite('null', 11)	# 1-11
        GFX_0('ubl_431_Dash01_Eff', 100)
        GFX_0('ubl_431_Dash00_Eff', 100)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_431_Dash00_Eff():

        def upon_IMMEDIATE():
            Unknown4009(3)
            Unknown4003('75626c65665f3433315f4461736830302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3032()
            Unknown1096(1500)
            Unknown1070(7000, 9000)
            Unknown1062(10000, 12000)
            teleportRelativeX(-150000)
            Unknown3001(65)
            Unknown1059(80)
            Unknown1067(20)
            physicsXImpulse(-2000)
        sprite('null', 6)	# 1-6
        Unknown3004(20)
        sprite('null', 22)	# 7-28
        Unknown3004(-10)
        loopRest()

    @State
    def ubl_431_Dash01_Eff():

        def upon_IMMEDIATE():
            Unknown4009(3)
            Unknown4003('75626c65665f3433315f4461736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3032()
            Unknown1096(1500)
            Unknown1070(3000, 5000)
            Unknown1062(7000, 9000)
            teleportRelativeX(2000)
            Unknown3001(35)
            Unknown1059(80)
            Unknown1067(20)
            physicsXImpulse(-2000)
        sprite('null', 6)	# 1-6
        Unknown3004(15)
        sprite('null', 22)	# 7-28
        Unknown3004(-10)
        loopRest()

    @State
    def ubl_431_Dash02_Eff():

        def upon_IMMEDIATE():
            Unknown4009(3)
            Unknown4003('75626c65665f3433315f4461736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3032()
            Unknown1056(12500)
            Unknown1064(11000)
            teleportRelativeX(-470000)
            Unknown1007(15000)
            physicsXImpulse(-5000)
            Unknown3001(64)
        sprite('null', 6)	# 1-6
        Unknown3004(15)
        sprite('null', 22)	# 7-28
        Unknown3004(-10)
        loopRest()

    @State
    def ubl_450_Vulcan_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            teleportRelativeX(80000)
            Unknown1007(10000)
            Unknown1096(1500)
            GFX_2('ublef_200_Muzzle')
        sprite('null', 15)	# 1-15
        loopRest()

    @State
    def ubl450_Fade_Eff():

        def upon_IMMEDIATE():
            sendToLabelUpon(32, 0)
        sprite('null', 35)	# 1-35
        sprite('null', 32767)	# 36-32802
        Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
        label(0)
        sprite('null', 1)	# 32803-32803
        Unknown26('SCEF_FadeBlack12In')
        Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
        loopRest()

    @State
    def ubl_UltimateBeamAH_Lightbullet_():

        def upon_IMMEDIATE():
            Unknown2054(1)
            Unknown1096(1600)
            teleportRelativeX(-10000)
            GFX_2('ublef_450_Lightbullet02')
        sprite('null', 202)	# 1-202
        loopRest()

    @State
    def ubl_UltimateBeamAH_rootWave_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
        label(0)
        sprite('null', 7)	# 1-7
        GFX_0('ubl_UltimateBeamAH_rootWave00_E', 100)
        sprite('null', 7)	# 8-14
        GFX_0('ubl_UltimateBeamAH_rootWave01_E', 100)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_UltimateBeamAH_rootWave00_E():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f726f6f747761766530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(7)
            Unknown3032()
            Unknown1062(9000, 7500)
            Unknown1070(6200, 5200)
            Unknown1059(-80)
        sprite('null', 19)	# 1-19
        loopRest()

    @State
    def ubl_UltimateBeamAH_rootWave01_E():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f726f6f747761766530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(7)
            Unknown3032()
            Unknown1062(9000, 7500)
            Unknown1070(4500, 3500)
            Unknown1059(-80)
        sprite('null', 19)	# 1-19
        loopRest()

    @State
    def ubl_UltimateBeamAH_Eff():

        def upon_IMMEDIATE():
            Unknown1086(22)
            teleportRelativeY(250000)
            Unknown21010(1)
        sprite('null', 60)	# 1-60
        sprite('null', 125)	# 61-185
        GFX_0('ubl_UltimateBeamAH_Loop_Eff', 100)
        GFX_0('ubl_UltimateBeamAH_Wave_Eff', 100)
        sprite('null', 50)	# 186-235
        Unknown26('ubl_UltimateBeamAH_Loop_Eff')
        Unknown26('ubl_UltimateBeamAH_Wave_Eff')
        GFX_0('ubl_UltimateBeamAH_End_Eff', 100)
        loopRest()

    @State
    def ubl_UltimateBeamAH_Loop_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown21010(1)
        label(0)
        sprite('null', 4)	# 1-4
        GFX_0('ubl_UltimateBeamAH00_Eff', 100)
        GFX_0('ubl_UltimateBeamAH01_Eff', 100)
        gotoLabel(0)

    @State
    def ubl_UltimateBeamAH00_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown1056(1800)
            Unknown1064(1300)
            Unknown21010(1)
        sprite('null', 3)	# 1-3
        Unknown4054(6)
        Unknown23067('ublef_450_Beam03')
        loopRest()

    @State
    def ubl_UltimateBeamAH01_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(3)
            teleportRelativeY(-5000)
            Unknown21010(1)
        sprite('null', 1)	# 1-1
        GFX_1('ublef_450_Ground', 100)
        loopRest()

    @State
    def ubl_UltimateBeamAH_Wave_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4007(2)
            Unknown21010(1)
        label(0)
        sprite('null', 3)	# 1-3
        GFX_0('ubl_UltimateBeamAH_Wave00_Eff', 100)
        SFX_0('014_electric_sl')
        SFX_0('016_explode_2')
        SFX_0('100_hit_grap_3')
        sprite('null', 4)	# 4-7
        SFX_0('014_electric_sl')
        SFX_0('016_explode_2')
        SFX_0('100_hit_grap_3')
        sprite('null', 3)	# 8-10
        GFX_0('ubl_UltimateBeamAH_Wave01_Eff', 100)
        SFX_0('014_electric_sl')
        SFX_0('016_explode_2')
        SFX_0('100_hit_grap_3')
        sprite('null', 4)	# 11-14
        SFX_0('014_electric_sl')
        SFX_0('016_explode_2')
        SFX_0('100_hit_grap_3')
        gotoLabel(0)
        loopRest()

    @State
    def ubl_UltimateBeamAH_Wave00_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4003('75626c65665f3435305f7761766530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3032()
            teleportRelativeX(-700000)
            Unknown1062(9000, 7500)
            Unknown1070(3500, 4000)
            Unknown1059(-80)
            physicsXImpulse(30000)
            Unknown23015(10)
            Unknown21010(1)
        sprite('null', 18)	# 1-18
        loopRest()

    @State
    def ubl_UltimateBeamAH_Wave01_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4003('75626c65665f3435305f7761766530312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3032()
            teleportRelativeX(-700000)
            Unknown1062(9000, 7500)
            Unknown1070(4000, 3000)
            Unknown1059(-80)
            physicsXImpulse(40000)
            Unknown23015(10)
            Unknown21010(1)
        sprite('null', 18)	# 1-18
        loopRest()

    @State
    def ubl_UltimateBeamAH_End_Eff():

        def upon_IMMEDIATE():
            Unknown4007(2)
            Unknown21010(1)
        sprite('null', 4)	# 1-4
        GFX_1('ublef_450_Beamfn01', 100)
        sprite('null', 1)	# 5-5
        Unknown4049(1500)
        Unknown4045('75626c65665f3433305f4265616d456e6400000000000000000000000000000064000000')
        loopRest()

    @State
    def ubl_UltimateBeamAH_smokepa_Eff():

        def upon_IMMEDIATE():
            pass
        label(0)
        sprite('null', 5)	# 1-5
        GFX_0('ubl_UltimateBeamAH_smokepa00_Ef', 100)
        GFX_0('ubl_UltimateBeamAH_smokepa02_Ef', 100)
        GFX_0('ubl_UltimateBeamAH_smokepa03_Ef', 100)
        sprite('null', 15)	# 6-20
        GFX_0('ubl_UltimateBeamAH_smokepa01_Ef', 100)
        GFX_0('ubl_UltimateBeamAH_smokepa04_Ef', 100)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_UltimateBeamAH_smokepa00_Ef():

        def upon_IMMEDIATE():
            teleportRelativeY(120000)
            Unknown1000(-100000)
            Unknown23067('ublef_450_Endsmoke03')
            Unknown1096(900)
        sprite('null', 480)	# 1-480

    @State
    def ubl_UltimateBeamAH_smokepa01_Ef():

        def upon_IMMEDIATE():
            Unknown4007(2)
            teleportRelativeY(100000)
            Unknown1000(-340000)
            Unknown23067('ublef_450_Endsmoke03')
            Unknown1096(800)
        sprite('null', 480)	# 1-480

    @State
    def ubl_UltimateBeamAH_smokepa02_Ef():

        def upon_IMMEDIATE():
            Unknown4054(11)
            teleportRelativeY(120000)
            Unknown1000(200000)
            Unknown23067('ublef_450_Endsmoke07')
            Unknown1096(800)
        sprite('null', 480)	# 1-480

    @State
    def ubl_UltimateBeamAH_smokepa03_Ef():

        def upon_IMMEDIATE():
            Unknown4054(6)
            teleportRelativeY(90000)
            Unknown1000(70000)
            Unknown3001(100)
            Unknown23067('ublef_450_Endsmoke03')
            Unknown1096(800)
        sprite('null', 480)	# 1-480

    @State
    def ubl_UltimateBeamAH_smokepa04_Ef():

        def upon_IMMEDIATE():
            Unknown4054(6)
            teleportRelativeY(80000)
            Unknown1000(220000)
            Unknown3001(70)
            Unknown1072(-3000)
            Unknown1096(800)
            Unknown23067('ublef_450_Endsmoke11')
        sprite('null', 480)	# 1-480

    @State
    def ubl_UltimateBeamAH_smoke_Eff():

        def upon_IMMEDIATE():
            pass
        sprite('null', 1)	# 1-1
        GFX_0('ubl_UltimateBeamAH_smoke00_Eff', 100)
        GFX_0('ubl_UltimateBeamAH_smoke01_Eff', 100)
        GFX_0('ubl_UltimateBeamAH_smoke02_Eff', 100)
        GFX_0('ubl_UltimateBeamAH_smoke03_Eff', 100)
        GFX_0('ubl_UltimateBeamAH_smoke04_Eff', 100)
        GFX_0('ubl_UltimateBeamAH_smoke05_Eff', 100)
        loopRest()

    @State
    def ubl_UltimateBeamAH_smoke00_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f3435305f736d6f6b6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(10)
            Unknown3032()
            teleportRelativeY(90000)
            Unknown1000(180000)
            Unknown1056(3000)
            Unknown1064(1800)
            Unknown3001(180)
            Unknown1072(5000)
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_UltimateBeamAH_smoke01_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f3435305f736d6f6b6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(15)
            Unknown3032()
            teleportRelativeY(20000)
            Unknown1000(-160000)
            Unknown1056(3500)
            Unknown1064(2700)
            Unknown3001(200)
            Unknown1072(-18000)
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_UltimateBeamAH_smoke02_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f3435305f736d6f6b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(6)
            Unknown3032()
            teleportRelativeY(-5000)
            Unknown1000(-400000)
            Unknown1056(2100)
            Unknown1064(2000)
            Unknown3001(120)
            Unknown1072(25000)
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_UltimateBeamAH_smoke03_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f3435305f736d6f6b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(15)
            Unknown3032()
            teleportRelativeY(50000)
            Unknown1000(480000)
            Unknown1056(2900)
            Unknown1064(1200)
            Unknown3001(120)
            Unknown1072(55000)
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_UltimateBeamAH_smoke04_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f3435305f736d6f6b6530302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(15)
            Unknown3032()
            teleportRelativeY(225000)
            Unknown1000(-125000)
            Unknown1056(1500)
            Unknown1064(1400)
            Unknown3001(80)
            Unknown1072(0)
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_UltimateBeamAH_smoke05_Eff():

        def upon_IMMEDIATE():
            Unknown4003('75626c65665f3435305f736d6f6b6530312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(10)
            Unknown3032()
            teleportRelativeY(0)
            Unknown1000(-600000)
            Unknown1056(1500)
            Unknown1064(1400)
            Unknown3001(120)
            Unknown1072(30000)
        sprite('null', 32767)	# 1-32767
        loopRest()

    @State
    def ubl_AH_Lamp_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown23015(6)
            Unknown3033()
            Unknown1096(650)
            Unknown3001(150)
        sprite('null', 18)	# 1-18
        Unknown3004(0)
        loopRest()

    @State
    def ubl_AH_LampTrajectory00_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430312e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(20000)
            Unknown1064(3000)
            Unknown1056(7500)
            Unknown3001(200)
            Unknown3013(128)
            Unknown3019(128)
        sprite('null', 11)	# 1-11
        sprite('null', 50)	# 12-61
        Unknown3004(-10)
        Unknown3016(-10)
        Unknown3022(-10)
        loopRest()

    @State
    def ubl_AH_LampTrajectory000_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430342e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(0)
            Unknown1064(3000)
            Unknown1056(7500)
            Unknown3001(200)
            Unknown3013(128)
            Unknown3019(128)
        sprite('null', 11)	# 1-11
        sprite('null', 50)	# 12-61
        Unknown3004(-10)
        Unknown3016(-10)
        Unknown3022(-10)
        loopRest()

    @State
    def ubl_AH_LampTrajectory01_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(20000)
            Unknown1064(3000)
            Unknown1056(7500)
            Unknown3001(200)
            Unknown3013(128)
            Unknown3019(128)
        sprite('null', 11)	# 1-11
        sprite('null', 50)	# 12-61
        Unknown3004(-10)
        Unknown3016(-10)
        Unknown3022(-10)
        loopRest()

    @State
    def ubl_AH_LampTrajectory010_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430352e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(0)
            Unknown1064(3000)
            Unknown1056(7500)
            Unknown3001(200)
            Unknown3013(128)
            Unknown3019(128)
        sprite('null', 11)	# 1-11
        sprite('null', 50)	# 12-61
        Unknown3004(-10)
        Unknown3016(-10)
        Unknown3022(-10)
        loopRest()

    @State
    def ubl_AH_LampTrajectory02_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(20000)
            Unknown1064(3000)
            Unknown1056(7500)
            Unknown3001(200)
            Unknown1059(100)
            Unknown3013(128)
            Unknown3019(128)
        sprite('null', 11)	# 1-11
        sprite('null', 50)	# 12-61
        Unknown3004(-10)
        Unknown3016(-10)
        Unknown3022(-10)
        loopRest()

    @State
    def ubl_AH_LampTrajectory020_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4010(2)
            Unknown4007(2)
            Unknown4003('75626c65665f3435305f5461696c4c6967687430332e444947000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4015()
            Unknown3033()
            teleportRelativeX(0)
            Unknown1064(3000)
            Unknown1056(7500)
            Unknown3001(200)
            Unknown1059(100)
            Unknown3013(128)
            Unknown3019(128)
        sprite('null', 11)	# 1-11
        sprite('null', 50)	# 12-61
        Unknown3004(-10)
        Unknown3016(-10)
        Unknown3022(-10)
        loopRest()

    @State
    def ubl_450_Dash_Eff():

        def upon_IMMEDIATE():
            Unknown4010(2)
            Unknown4011(2)
            Unknown4007(2)
            Unknown4009(3)
        label(0)
        sprite('null', 12)	# 1-12
        GFX_0('ubl_450_Dash01_Eff', 100)
        GFX_0('ubl_450_Dash00_Eff', 100)
        gotoLabel(0)
        loopRest()

    @State
    def ubl_450_Dash00_Eff():

        def upon_IMMEDIATE():
            Unknown4009(3)
            Unknown4003('75626c65665f3433315f4461736830302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3032()
            Unknown1096(1500)
            Unknown1070(7000, 9000)
            Unknown1062(7000, 10000)
            Unknown1010(-250000, -100000)
            Unknown3001(65)
            Unknown1059(90)
            Unknown1067(28)
            Unknown1025(-20000, -15000)
        sprite('null', 6)	# 1-6
        Unknown3004(20)
        sprite('null', 4)	# 7-10
        Unknown3004(-10)
        sprite('null', 18)	# 11-28
        Unknown1015(15500)
        loopRest()

    @State
    def ubl_450_Dash01_Eff():

        def upon_IMMEDIATE():
            Unknown4009(3)
            Unknown4003('75626c65665f3433315f4461736830312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown3032()
            Unknown1096(1500)
            Unknown1070(3000, 4000)
            Unknown1062(7000, 9000)
            teleportRelativeX(120000)
            Unknown3001(35)
            Unknown1059(80)
            Unknown1067(24)
            physicsXImpulse(-6000)
        sprite('null', 6)	# 1-6
        Unknown3004(15)
        sprite('null', 22)	# 7-28
        Unknown3004(-10)
        loopRest()

    @State
    def ubl_000_Eyes_Eff():

        def upon_IMMEDIATE():
            Unknown4007(2)
        sprite('vr_ublef000_eyes', 60)	# 1-60
        GFX_0('ubl_Eye00_Eff', 0)
        GFX_0('ubl_Eye01_Eff', 1)
        SFX_3('ublse_10')
        loopRest()

    @State
    def ubl_Eye00_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4007(3)
            Unknown2054(1)
            GFX_2('ublef_Eye_light')
        sprite('null', 35)	# 1-35

    @State
    def ubl_Eye01_Eff():

        def upon_IMMEDIATE():
            Unknown4011(2)
            Unknown4007(3)
            Unknown2054(1)
            GFX_2('ublef_Eye_light')
            Unknown1096(1250)
        sprite('null', 35)	# 1-35
