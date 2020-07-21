@Subroutine
def HomingAtkInt():
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(22000)
    AirPushbackY(17000)
    AirUntechableTime(60)
    YImpluseBeforeWallbounce(400)
    Hitstop(12)
    Unknown11001(0, -4, -4)
    Unknown2037(1)
    setInvincible(1)
    Unknown11044(1)
    Unknown11069('HomingAttack')
    Unknown11068(1)

@State
def ShotAtkObj_A():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        physicsXImpulse(50000)
        FreezeCount(15)
        FreezeDuration(28)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_Eff', 100)
    Unknown38(5, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown21007(5, 32)

@State
def ShotAtkObj_B1():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        physicsXImpulse(50000)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_B_Eff', 100)
    Unknown38(7, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown23029(7, 4402, 0)

@State
def ShotAtkObj_B2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        physicsXImpulse(45000)
        Unknown1007(15000)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_B_Eff', 100)
    Unknown38(8, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown23029(8, 4402, 0)

@State
def ShotAtkObj_B3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        physicsXImpulse(35000)
        Unknown1007(-15000)
        FreezeCount(15)
        FreezeDuration(28)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_B_Eff', 100)
    Unknown38(9, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown23029(9, 4402, 0)

@State
def ShotAtkObj_P1():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        AttackP1(70)
        Unknown11042(1)
        Unknown53(1)
        physicsXImpulse(50000)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_B_Eff', 100)
    Unknown38(7, 1)
    GFX_0('kym_ShotWind00_Eff', 100)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown23029(7, 4402, 0)

@State
def ShotAtkObj_P2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        AttackP1(70)
        Unknown11042(1)
        Unknown53(1)
        physicsXImpulse(45000)
        Unknown1007(15000)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_B_Eff', 100)
    Unknown38(8, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown23029(8, 4402, 0)

@State
def ShotAtkObj_P3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        AttackP1(70)
        Unknown11042(1)
        Unknown53(1)
        physicsXImpulse(35000)
        Unknown1007(-15000)
        FreezeCount(15)
        FreezeDuration(40)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
        Unknown3038(1)
    sprite('vr_ShotAtkObj', 120)
    GFX_0('kym_Shot_B_Eff', 100)
    Unknown38(9, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown23029(9, 4402, 0)

@State
def ShotAtkObjAir1():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        physicsXImpulse(50000)
        FreezeCount(15)
        FreezeDuration(28)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_43():
            if (SLOT_48 == 4401):
                MinimumDamagePct(10)
                Unknown30065(0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)
    sprite('vr_ShotAtkObj', 120)
    Unknown3038(1)
    GFX_0('kym_Shot_Eff', 100)
    Unknown38(6, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown21007(6, 32)

@State
def ShotAtkObjAir2():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        Unknown1056(800)
        Unknown1064(500)
        physicsXImpulse(50000)
        physicsYImpulse(-33500)
        FreezeCount(15)
        FreezeDuration(28)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(0)

        def upon_43():
            if (SLOT_48 == 4401):
                MinimumDamagePct(10)
                Unknown30065(0)
    sprite('vr_ShotAtkObj', 120)
    Unknown3038(1)
    GFX_0('kym_Shot_30_Eff', 100)
    Unknown38(6, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown21007(6, 32)

@State
def ShotAtkObjAir3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(8000)
        AirUntechableTime(30)
        Hitstop(5)
        Unknown9019(1)
        Unknown53(1)
        Unknown1056(500)
        Unknown1064(600)
        physicsXImpulse(50000)
        physicsYImpulse(-12500)
        FreezeCount(15)
        FreezeDuration(28)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)

        def upon_3():
            if SLOT_38:
                Unknown23045(105)
                if (SLOT_22 < SLOT_0):
                    Unknown13(25)
            else:
                Unknown23045(105)
                if (SLOT_22 > SLOT_0):
                    Unknown13(25)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(0)

        def upon_43():
            if (SLOT_48 == 4401):
                MinimumDamagePct(10)
                Unknown30065(0)
    sprite('vr_ShotAtkObj', 120)
    Unknown3038(1)
    GFX_0('kym_Shot_45_Eff', 100)
    GFX_0('kym_ShotWind02_Eff', 100)
    Unknown38(6, 1)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown21007(6, 32)

@State
def __274atk_00():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1300)
        ProjectileDurabilityLvl(2)
        AirPushbackX(15000)
        AirPushbackY(12000)
        Unknown30056(100000, 50, 0)
        GroundedHitstunAnimation(1)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        Unknown23182(2)
        MinimumDamagePct(10)
        Unknown30065(0)
        AirUntechableTime(29)
        Unknown11056(0)
        Hitstop(3)
        Unknown9019(1)
        Unknown11001(-1, -1, -1)
        Unknown2053(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)
        loopRelated(17, 90)

        def upon_17():
            Unknown23090(25)
        HitLow(2)
        Unknown3038(1)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 4002, 0)
        SLOT_4 = SLOT_83
    sprite('vr_kymef274atk_00', 5)
    GFX_0('kym402_Ice_Eff', 100)
    sprite('vr_kymef274atk_00', 90)
    StartMultihit()
    label(0)
    sprite('vr_kymef274atk_00', 3)
    sprite('keep', 2)
    Unknown1084(1)

@State
def __274atk_01():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1300)
        ProjectileDurabilityLvl(2)
        AirPushbackX(15000)
        AirPushbackY(22000)
        Unknown30056(100000, 50, 0)
        PushbackX(39800)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        Unknown23182(2)
        MinimumDamagePct(10)
        Unknown30065(0)
        GroundedHitstunAnimation(1)
        AttackP1(80)
        AirUntechableTime(29)
        Unknown11056(0)
        Hitstop(3)
        Unknown9019(1)
        Unknown11001(-1, -1, -1)
        Unknown2053(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)
        loopRelated(17, 90)

        def upon_17():
            Unknown23090(25)
        HitLow(2)
        Unknown3038(1)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 4002, 0)
        SLOT_83 = SLOT_4
        teleportRelativeX(170000)
    sprite('vr_kymef274atk_00ex01', 5)
    GFX_0('kym402_Ice2_Eff', 100)
    sprite('vr_kymef274atk_00ex01', 90)
    StartMultihit()
    label(0)
    sprite('vr_kymef274atk_00ex01', 3)
    sprite('keep', 2)
    Unknown1084(1)

@State
def __274atk_02():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(2000)
        ProjectileDurabilityLvl(2)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(25000)
        Unknown30056(100000, 50, 0)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        Unknown23182(2)
        MinimumDamagePct(10)
        Unknown30065(0)
        AirUntechableTime(60)
        Hitstop(15)
        Unknown9019(1)
        Unknown2053(1)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)
        sendToLabelUpon(54, 0)
        loopRelated(17, 90)

        def upon_17():
            Unknown23090(25)
        HitLow(2)

        def upon_78():
            clearUponHandler(78)
            callSubroutine('HomingAtkInt')
            Unknown21015('EXPushUpAttack', 4001, 0)
            Unknown11064(1)
        Unknown3038(1)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 4002, 0)
        SLOT_83 = SLOT_4
        teleportRelativeX(320000)
    sprite('vr_kymef274atk_00ex02', 5)
    GFX_0('kym402_Ice3_Eff', 100)
    sprite('vr_kymef274atk_00ex02', 90)
    StartMultihit()
    label(0)
    sprite('vr_kymef274atk_00ex02', 3)
    sprite('keep', 2)
    Unknown1084(1)

@State
def __231atk_00():

    def upon_IMMEDIATE():
        Unknown2009()
        AttackLevel_(3)
        Damage(900)
        AirPushbackX(12000)
        AirPushbackY(9000)
        AttackP1(100)
        AttackP2(80)
        Unknown11092(1)
        Hitstop(1)
        Unknown11001(-1, -1, -1)
        PushbackX(15000)
        Unknown9016(1)
        hitstun(23)
        AirUntechableTime(23)
        Unknown30056(-80000, 50, 0)
        ProjectileDurabilityLvl(0)
        Unknown11034(1)
        AttackAttributes(0, 1, 0, 0, 0)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(0)
        Unknown3029(1)
        AfterimageCount(4)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown23029(3, 2001, 0)

        def upon_12():
            clearUponHandler(12)
            Unknown23029(3, 2002, 0)
    sprite('kym201_04ex1', 1)
    RefreshMultihit()
    SFX_0('slash_knife_slow')
    GFX_0('kym201_Eff', 100)
    sprite('kym201_04ex1', 1)
    teleportRelativeX(150000)
    sprite('kym201_04ex2', 1)
    sprite('kym201_04ex2', 1)
    teleportRelativeX(100000)
    SFX_0('slash_knife_slow')
    sprite('kym201_04ex3', 1)
    sprite('kym201_04ex3', 1)
    teleportRelativeX(50000)
    sprite('kym201_04ex1', 1)
    SFX_0('slash_knife_slow')
    sprite('kym201_04ex1', 1)
    teleportRelativeX(25000)
    sprite('kym201_04ex2', 1)
    sprite('kym201_04ex2', 1)
    PushbackX(-10000)
    SFX_0('slash_knife_slow')
    sprite('kym201_04ex3', 1)
    AirPushbackX(-14000)
    PushbackX(-30400)
    RefreshMultihit()
    sprite('kym201_04ex3', 1)
    sprite('kym201_04ex1', 1)
    physicsXImpulse(-64000)
    SFX_0('slash_knife_slow')
    blockstun(10)
    sprite('kym201_04ex1', 1)
    sprite('kym201_04ex2', 1)
    sprite('kym201_04ex2', 1)
    SFX_0('slash_knife_slow')
    sprite('kym201_04ex3', 1)
    loopRest()
    sprite('null', 1)
    teleportRelativeX(-82000)
    Unknown1007(-20000)

@State
def Hamaryu_01():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        ProjectileDurabilityLvl(2)
        Damage(1000)
        AttackP1(80)
        AttackP2(100)
        hitstun(50)
        AirPushbackX(0)
        AirPushbackY(0)
        AirHitstunAnimation(4)
        Unknown11045(1)
        HitLow(2)
        AttackAttributes(0, 0, 1, 0, 0)
        Unknown9266(9)
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(1)
        Unknown2073(1)

        def upon_77():
            clearUponHandler(77)
            GFX_0('Hamaryu_02', 0)
            PushbackX(0)
            sendToLabel(1)
            DisableAttackRestOfMove()
            Unknown11064(1)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 4082, 0)

        def upon_82():
            clearUponHandler(82)
            Unknown9215()
            Unknown11064(0)
            Unknown9155()
        Unknown3038(1)
    sprite('vr_HamaryuAtk_ex01', 1)
    SFX_3('kymse_16')
    RefreshMultihit()
    GFX_0('kym408_IceBoard_1st_Eff', 100)
    GFX_0('kym408_IceBoard_sml2_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 2)
    physicsXImpulse(50000)
    sprite('vr_HamaryuAtk_ex01', 1)
    SFX_3('kymse_16')
    GFX_0('kym408_IceBoard1_Eff', 100)
    GFX_0('kym408_IceBoard_sml1_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 2)
    sprite('vr_HamaryuAtk_ex01', 1)
    SFX_3('kymse_16')
    GFX_0('kym408_IceBoard2_Eff', 100)
    GFX_0('kym408_IceBoard_sml2_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 2)
    GFX_0('kym408_IceBoard2_Eff', 100)
    GFX_0('kym408_IceBoard_sml2_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 2)
    SFX_3('kymse_16')
    GFX_0('kym408_IceBoard3_Eff', 100)
    GFX_0('kym408_IceBoard_sml3_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 1)
    Unknown1084(1)
    GFX_0('Hamaryu_02', 0)
    GFX_0('kym408_IceBoard1_Eff', 100)
    GFX_0('kym408_IceBoard_sml1_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 2)
    SFX_3('kymse_16')
    DisableAttackRestOfMove()
    GFX_0('kym408_IceBoard_sml1_Eff', 100)
    sprite('vr_HamaryuAtk_ex01', 1)
    label(1)
    sprite('vr_HamaryuAtk_ex01', 2)
    sprite('vr_HamaryuAtk_ex01', 7)
    Unknown1084(1)

@State
def Hamaryu_02():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(90)
        ProjectileDurabilityLvl(2)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(25000)
        AirUntechableTime(60)
        Hitstop(12)
        HitLow(2)
        AttackAttributes(0, 0, 1, 0, 0)

        def upon_78():
            clearUponHandler(78)
            callSubroutine('HomingAtkInt')
            Hitstop(12)
            Unknown23029(3, 4081, 0)
            Unknown11064(1)

        def upon_80():
            clearUponHandler(80)
            Unknown23029(3, 4082, 0)
        Unknown3038(1)
    sprite('null', 8)
    GFX_0('kym402_Ice3_Eff', 100)
    GFX_0('kym408_IceBoard_End_Eff', 100)
    GFX_0('kym408_IceBoard_smlEnd_Eff', 100)
    sprite('vr_HamaryuAtk_02', 4)
    sprite('keep', 30)
    StartMultihit()

@State
def ShotAtkObj_Hasei3():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(5)
        Damage(2000)
        AttackP2(80)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(-28000)
        PushbackX(5000)
        Unknown9310(10)
        Unknown11065(1)
        Unknown9190(1)
        Unknown9118(30)
        AirUntechableTime(60)
        Hitstop(4)
        HitOverhead(2)
        Unknown1056(1300)
        Unknown1064(1300)
        physicsXImpulse(0)
        physicsYImpulse(-100000)
        Unknown23089(1, 1, 1, 1, 1, 0, 1, 0)

        def upon_54():
            DisableAttackRestOfMove()
        loopRelated(17, 75)

        def upon_17():
            Unknown23090(25)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(0)
            Unknown4049(1200)
            Unknown4045('kymef409_icegrow', 100)
            GFX_0('kym409_iceGrow_Eff', 100)
        if (SLOT_163 < 0):
            if (SLOT_163 >= (-250000)):
                Unknown48(25, 2, 83, 22, 2, 83)
                (SLOT_163 <= 0)
            else:
                teleportRelativeX(-250000)
    sprite('vr_kymef403atk_hasei3', 120)
    Unknown4003('kymef_409_icedrop.DIG', '')
    GFX_2('kymef409_bloom02')
    Unknown4049(1100)
    Unknown4045('kymef409_icemake', 100)
    GFX_0('kym409_Wave3_Eff', 100)
    GFX_0('kym409_IceWave_Eff', 100)
    label(0)
    sprite('keep', 10)
    Unknown1084(1)
    Unknown3004(-64)
    Unknown4049(1200)
    Unknown4045('kymef409_icebreak', 100)

@State
def UltimateShotAtkObj():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        ProjectileDurabilityLvl(2)
        Damage(1740)
        MinimumDamagePct(14)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(45000)
        AirPushbackY(20000)
        PushbackX(50000)
        AirUntechableTime(60)
        Unknown1056(2000)
        Unknown1064(2000)
        Hitstop(2)
        Unknown11001(5, 0, 0)
        Unknown9019(1)
        Unknown2055(60)

        def upon_3():
            if SLOT_38:
                Unknown23045(125)
                if (SLOT_22 < SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)
            else:
                Unknown23045(125)
                if (SLOT_22 > SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)
        Unknown2037(4)

        def upon_77():
            Unknown11001(5, 5, 5)
            if SLOT_2:
                Unknown2038(-1)
            else:
                clearUponHandler(77)
                Unknown2003(1)

        def upon_81():
            SLOT_52 = (SLOT_52 + 1)
            if (SLOT_52 >= 5):
                clearUponHandler(81)
                Unknown30048(1)
        Unknown3038(1)
        teleportRelativeX(120000)
        Unknown1007(60000)

        def upon_STATE_END():
            Unknown23090(4)
    sprite('vr_ShotAtkObj', 2)
    GFX_0('kym430_Ice_Eff', 100)
    Unknown38(4, 1)
    GFX_0('kym430_ShotMuzzle_Eff', 100)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 2)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 2)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 2)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 2)
    RefreshMultihit()
    physicsXImpulse(70000)
    label(10)
    sprite('vr_ShotAtkObj', 2)
    RefreshMultihit()
    gotoLabel(10)
    label(0)
    sprite('keep', 2)
    Unknown1084(1)

@State
def UltimateShotSPAtkObj():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        ProjectileDurabilityLvl(2)
        Damage(1220)
        MinimumDamagePct(12)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(45000)
        AirPushbackY(20000)
        PushbackX(50000)
        AirUntechableTime(60)
        Unknown1056(2000)
        Unknown1064(2000)
        Hitstop(2)
        Unknown11001(5, 0, 0)
        Unknown9019(1)
        Unknown11110(77)
        Unknown2055(60)

        def upon_3():
            if SLOT_38:
                Unknown23045(125)
                if (SLOT_22 < SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)
            else:
                Unknown23045(125)
                if (SLOT_22 > SLOT_0):
                    clearUponHandler(3)
                    clearUponHandler(54)
                    Unknown13(25)
        Unknown2037(9)

        def upon_77():
            Unknown11001(5, 5, 5)
            if SLOT_2:
                Unknown2038(-1)
            else:
                clearUponHandler(77)
                Unknown2003(1)

        def upon_81():
            SLOT_52 = (SLOT_52 + 1)
            if (SLOT_52 >= 10):
                clearUponHandler(81)
                Unknown30048(1)
        Unknown3038(1)
        teleportRelativeX(120000)
        Unknown1007(60000)

        def upon_STATE_END():
            Unknown23090(4)
    sprite('vr_ShotAtkObj', 1)
    GFX_0('kym430_Ice_Eff', 100)
    Unknown38(4, 1)
    GFX_0('kym430_ShotMuzzle_Eff', 100)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    physicsXImpulse(70000)
    label(10)
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    sprite('vr_ShotAtkObj', 1)
    RefreshMultihit()
    gotoLabel(10)
    label(0)
    sprite('keep', 2)
    Unknown1084(1)

@State
def __430_ougi():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(3)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 4302):
                sendToLabel(1)
        Unknown1007(-40000)
    sprite('kym430_ougi00', 3)
    GFX_0('kym430_Charge_Eff', 100)
    sprite('kym430_ougi01', 3)
    sprite('kym430_ougi02', 3)
    label(0)
    sprite('kym430_ougi03', 3)
    sprite('kym430_ougi04', 3)
    sprite('kym430_ougi05', 3)
    sprite('kym430_ougi06', 3)
    sprite('kym430_ougi07', 3)
    gotoLabel(0)
    label(1)
    sprite('kym430_ougi06', 3)
    sprite('kym430_ougi07', 3)

@State
def __430_ougi_Rolling():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4007(3)
        Unknown4011(3)

        def upon_43():
            if (SLOT_48 == 4302):
                sendToLabel(1)
    label(0)
    sprite('kym430_ougi03', 3)
    sprite('kym430_ougi04', 3)
    sprite('kym430_ougi05', 3)
    sprite('kym430_ougi06', 3)
    sprite('kym430_ougi07', 3)
    gotoLabel(0)
    label(1)
    sprite('kym430_ougi03', 3)
    sprite('kym430_ougi04', 1)

@State
def AstWhite():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown1096(200000)
        Unknown3033()
        Unknown3001(0)
        Unknown2034(0)

        def upon_3():
            teleportRelativeY(-3000000)
            Unknown23032(50)
    sprite('vr_white', 90)
    Unknown3004(11)
    sprite('vr_white', 40)
    SFX_3('kymse_33')
    sprite('vr_white', 30)
    Unknown3001(240)
    Unknown3004(-8)

@State
def AstWhite2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23015(1)
        Unknown1096(200000)
        Unknown3032()
        Unknown3001(0)
        Unknown2034(0)

        def upon_3():
            teleportRelativeY(-3000000)
            Unknown23032(50)
    sprite('null', 60)
    sprite('vr_white', 120)
    Unknown3001(255)
    sprite('vr_white', 50)
    Unknown3004(-5)

@State
def Astral_Atk_dmy():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11064(3)
        Damage(36000)
        MinimumDamagePct(100)
        Hitstop(0)
        Unknown11050(5, '')
        Unknown1086(22)
        Unknown11068(1)
        Unknown11078(1)
        Unknown2054(1)
        Unknown21010(1)
    sprite('vr_dmy', 2)
    sprite('keep', 3)
    Unknown26('kym450_BG_Ice00_Eff')
    Unknown26('kym450_BG_Ice01_Eff')
    Unknown26('kym450_BG_Ice02_Eff')
    Unknown26('kym450_BG_Ice03_Eff')
    Unknown26('kym450_BG_Ice04_Eff')
    Unknown26('kym450_Ice02_Eff')

@State
def AstralHeat_Camera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20001(1)
        Unknown20003(1)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4008(3)
        teleportRelativeY(280000)

        def upon_43():
            if (SLOT_48 == 4501):
                sendToLabel(0)
            if (SLOT_48 == 4502):
                sendToLabel(1)
            if (SLOT_48 == 4503):
                sendToLabel(2)
            if (SLOT_48 == 4504):
                Unknown4007(0)
            if (SLOT_48 == 4505):
                sendToLabel(3)
    sprite('null', 1)
    Unknown4007(2)
    Unknown20001(0)
    sprite('null', 119)
    teleportRelativeX(90000)
    Unknown20009(400)
    sprite('null', 32767)
    Unknown20001(0)
    Unknown20009(1000)
    label(0)
    sprite('null', 32767)
    Unknown4007(0)
    Unknown20001(0)
    label(1)
    sprite('null', 32767)
    teleportRelativeX(-90000)
    Unknown1086(22)
    Unknown20001(1)
    label(2)
    sprite('null', 32767)
    Unknown4007(2)
    Unknown20001(0)
    label(3)
    sprite('null', 10)
    physicsXImpulse(17000)
    teleportRelativeX(700000)
    Unknown1086(22)
    Unknown20001(0)
    sprite('null', 32767)
    Unknown1084(1)

@State
def __450_cutin():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown6001(1)
        Unknown1000(500000)
        teleportRelativeY(-335000)
        if SLOT_38:
            Unknown1000(-780000)
        Unknown23015(1)
        Unknown3001(0)
    sprite('kym450cutin_00a', 20)
    Unknown3004(25)
    Unknown1045(10000)
    sprite('kym450cutin_00a', 32767)
    Unknown1084(1)
    loopRest()

@State
def XhitEff_Kagura():

    def upon_IMMEDIATE():
        Unknown2006()
        Unknown1086(22)
        teleportRelativeY(200000)
    sprite('null', 22)
    GFX_1('ef_hitx_kgr', 0)

@State
def kym030_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4022(2)
        Unknown4003('kymef_030_icedash00.DIG', '')
        Unknown3032()
        Unknown3001(180)
        Unknown1056(330)
        Unknown1064(600)
        Unknown1062(600, 300)
        Unknown1070(1600, 50)
        Unknown1099(100)
        teleportRelativeX(-120000)
        physicsXImpulse(-7000)
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 101):
                Unknown4022(0)
    sprite('null', 4)
    GFX_0('kym030_Ice_pa_Eff', 100)
    GFX_1('kymef030_Glitter', 100)
    Unknown4049(700)
    Unknown4045('kymef030_icefloor', 100)
    SFX_3('kymse_04')
    sprite('null', 1)
    GFX_1('kymef030_icebreak', 100)
    sprite('null', 2)
    Unknown1099(0)
    sprite('null', 2)
    Unknown3004(-43)

@State
def kym030_Ice2_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4022(2)
        Unknown4003('kymef_030_icedash01.DIG', '')
        Unknown3032()
        Unknown3001(220)
        Unknown1056(200)
        Unknown1064(500)
        Unknown1062(700, 400)
        Unknown1070(1800, 500)
        Unknown1099(150)
        teleportRelativeX(-80000)
        physicsXImpulse(-7000)
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 101):
                Unknown4022(0)
    sprite('null', 4)
    sprite('null', 4)
    Unknown1099(0)
    sprite('null', 2)
    Unknown3004(-35)

@State
def kym030_Ice3_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4022(2)
        Unknown4003('kymef_030_icedash02.DIG', '')
        Unknown3033()
        Unknown3001(220)
        Unknown1056(200)
        Unknown1064(650)
        Unknown1102(250, -100)
        Unknown1062(800, 500)
        Unknown1070(1500, 400)
        Unknown1099(150)
        teleportRelativeX(-120000)
        physicsXImpulse(-7000)
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 101):
                Unknown4022(0)
    sprite('null', 4)
    GFX_1('kymef030_Glitter', 100)
    sprite('null', 4)
    Unknown1099(0)
    sprite('null', 2)
    Unknown3004(-35)

@State
def kym030_Ice_pa_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        GFX_2('kymef030_Glitter02')
    sprite('null', 60)

@State
def kym030_Ice_sml_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('kymef_030_icedash00.DIG', '')
        Unknown3032()
        Unknown3001(220)
        Unknown1056(500)
        Unknown1064(530)
        Unknown1070(1200, 800)
        Unknown1062(1800, 1300)
        teleportRelativeX(-120000)
        Unknown23015(11)
    sprite('null', 3)
    Unknown1065(-50)
    sprite('null', 7)
    Unknown1065(-200)
    sprite('null', 5)
    Unknown1065(-325)
    sprite('null', 12)
    Unknown3004(-20)

@State
def kym030_Ice_sml2_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('kymef_030_icedash01.DIG', '')
        Unknown3032()
        Unknown3001(200)
        Unknown1056(500)
        Unknown1064(400)
        Unknown1070(2300, 1500)
        Unknown1062(1800, 1400)
        teleportRelativeX(-80000)
        Unknown23015(11)
    sprite('null', 6)
    Unknown1065(10)
    sprite('null', 4)
    Unknown1065(-200)
    sprite('null', 5)
    Unknown1065(-330)
    sprite('null', 12)
    Unknown3004(-20)

@State
def kym030_Ice_sml3_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('kymef_030_icedash02.DIG', '')
        Unknown3032()
        Unknown3001(190)
        Unknown1056(600)
        Unknown1064(550)
        Unknown1070(2020, 1200)
        Unknown1062(1800, 1200)
        teleportRelativeX(-80000)
        Unknown23015(11)
    sprite('null', 5)
    Unknown1065(10)
    sprite('null', 5)
    Unknown1065(-200)
    sprite('null', 5)
    Unknown1065(-340)
    sprite('null', 13)
    Unknown3004(-21)

@State
def kym200_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(30000)
        Unknown1007(-19000)
    sprite('null', 2)
    sprite('null', 60)
    GFX_0('kym200_Wind_Eff', 100)
    GFX_0('kym200_Bloom_Eff', 100)
    loopRest()

@State
def kym200_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_200_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-51)
    loopRest()

@State
def kym200_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_200_Bloom.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(239)
        Unknown3007(223)
        Unknown3013(239)
    sprite('null', 7)
    sprite('null', 11)
    Unknown3004(-16)
    loopRest()

@State
def kym201_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_201_Wind.DIG', '')
        Unknown3033()
    sprite('null', 4)
    GFX_0('kym201_Cross_Eff', 100)
    Unknown1096(750)
    Unknown1099(50)
    Unknown3001(0)
    Unknown3004(50)
    sprite('null', 10)
    Unknown3001(220)
    Unknown1099(0)
    Unknown1096(1000)
    sprite('null', 9)
    Unknown1099(-100)
    Unknown3004(-50)

@State
def kym201_Cross_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    label(0)
    sprite('null', 2)
    GFX_1('kymef201_kira', 100)
    gotoLabel(0)

@State
def kym202_Flash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('kymef202_bloom02')
    sprite('null', 6)

@State
def kym202_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_202_Ice.DIG', '')
        Unknown4015()
        Unknown3032()
        GFX_2('kymef202_bloom01')
        Unknown1007(-40000)
        Unknown1096(800)
        Unknown1064(600)
        Unknown1072(-5000)
    sprite('null', 3)
    Unknown3001(0)
    sprite('null', 60)
    Unknown3001(255)

@State
def kym202_Ice_Fall_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_202_Ice.DIG', '')
        Unknown4015()
        Unknown3032()
        GFX_2('kymef202_bloom01')
        Unknown1007(-25000)
        teleportRelativeX(-15000)
        Unknown1096(1500)
        Unknown3001(255)
    sprite('vr_kymef401_ice', 1)
    GFX_0('kym202_Ice_FallBloom_Eff', 0)
    GFX_1('kymef202_down', 100)
    sprite('vr_kymef401_ice', 1)
    label(0)
    sprite('vr_kymef401_ice', 1)
    GFX_1('kymef202_down', 100)
    sprite('vr_kymef401_ice', 1)
    gotoLabel(0)

@State
def kym202_Ice_FallBloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_202_Icebloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23067('kymef202_bloom03')
        Unknown1007(-20000)
        teleportRelativeX(-15000)
        Unknown1096(1500)
        Unknown3001(210)
    Unknown1096(1550)
    Unknown3001(80)
sprite('vr_kymef401_ice', 32767)
endState()

@State
def kym202_line_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('kymef202_downMomentum01')
        Unknown1007(-182000)
    label(0)
    sprite('null', 1)
    GFX_1('kymef202_downMomentum01', 100)
    gotoLabel(0)

@State
def kym202_Landing_Eff():

    def upon_IMMEDIATE():
        Unknown4054(11)
        Unknown23067('kymef202_icefloor')
        Unknown1096(1500)

        def upon_32():
            Unknown3004(-12)
    sprite('null', 180)
    GFX_1('kymef202_icebreak', 100)
    SFX_3('kymse_06')

@State
def kym231_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
    sprite('null', 20)
    GFX_0('kym231_Wind_Eff', 100)
    GFX_0('kym231_Bloom_Eff', 100)

@State
def kym231_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_231_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(127)
    sprite('null', 11)
    sprite('null', 4)
    Unknown3004(-38)

@State
def kym231_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_231_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3001(63)
    sprite('null', 11)
    sprite('null', 4)
    Unknown3004(-38)

@State
def kym232_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(60000)
        Unknown1007(-20000)
    sprite('null', 2)
    GFX_0('kym232_Wind_Eff', 100)
    GFX_0('kym232_Bloom_Eff', 100)
    sprite('null', 20)
    Unknown4007(0)

@State
def kym232_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_232_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(127)
    sprite('null', 8)
    sprite('null', 5)
    Unknown3004(-19)

@State
def kym232_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_232_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3001(127)
    sprite('null', 8)
    sprite('null', 5)
    Unknown3004(-35)

@State
def kym232_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        teleportRelativeX(224000)
    sprite('null', 1)
    GFX_0('kym232_Ice00_Eff', 100)
    GFX_0('kym232_Ice01_Eff', 100)
    GFX_0('kym232_Wind2_Eff', 100)
    GFX_1('kymef232_Floor', 100)

@State
def kym232_Ice00_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('kymef_232_Ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(220)
        teleportRelativeY(-10000)
        teleportRelativeX(-60000)
    sprite('null', 7)
    Unknown1096(250)
    Unknown1099(100)
    sprite('null', 13)
    Unknown1099(0)
    sprite('null', 8)
    Unknown3004(-55)
    Unknown1099(-35)
    GFX_1('kymef232_Ice', 100)

@State
def kym232_Ice01_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4003('kymef_232_Ice01.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeY(-10000)
        teleportRelativeX(-60000)
    sprite('null', 7)
    Unknown1096(250)
    Unknown1099(100)
    sprite('null', 13)
    Unknown1099(0)
    sprite('null', 8)
    Unknown3004(-64)
    Unknown1099(-35)
    GFX_1('kymef232_Ice', 100)

@State
def kym232_Wind2_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(3)
        Unknown4003('kymef_232_Wind2.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-60000)
    sprite('null', 20)

@State
def kym250_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 20)
    GFX_0('kym250_Wind_Eff', 100)
    GFX_0('kym250_Bloom_Eff', 100)

@State
def kym250_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_250_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(159)
    sprite('null', 12)
    sprite('null', 4)
    Unknown3004(-35)

@State
def kym250_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_250_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(191)
        Unknown3013(223)
        Unknown3001(151)
    sprite('null', 12)
    sprite('null', 4)
    Unknown3004(-35)

@State
def kym251_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1007(-8000)
    sprite('null', 20)
    GFX_0('kym251_Wind_Eff', 100)
    GFX_0('kym251_Bloom_Eff', 100)

@State
def kym251_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_251_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(175)
    sprite('null', 12)
    sprite('null', 4)
    Unknown3004(-35)

@State
def kym251_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_251_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3001(95)
    sprite('null', 12)
    sprite('null', 4)
    Unknown3004(-35)

@State
def kym270_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(254000)
        Unknown1007(184000)
        Unknown1073(20000)
    sprite('null', 20)
    GFX_0('kym270_Wind_Eff', 100)
    GFX_0('kym270_Bloom_Eff', 100)

@State
def kym270_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4003('kymef_270_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(151)
    sprite('null', 12)
    sprite('null', 4)
    Unknown3004(-51)

@State
def kym270_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown4009(2)
        Unknown4003('kymef_270_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(63)
        Unknown3013(127)
    sprite('null', 15)
    sprite('null', 5)
    Unknown4007(0)

@State
def kym271_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_271_Ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(215)
        Unknown1096(1075)
        teleportRelativeX(155000)
        Unknown1007(-45000)

        def upon_43():
            if (SLOT_48 == 4051):
                sendToLabel(0)
    sprite('null', 4)
    GFX_0('kym271_IceAdd_Eff', 100)
    GFX_0('kym271_Floor_Eff', 100)
    sprite('null', 30)
    Unknown4007(0)
    label(0)
    sprite('null', 8)
    GFX_0('kym271_IceCrush_Eff', 100)
    Unknown3004(-32)

@State
def kym271_IceAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4013(2)
        Unknown4003('kymef_271_Ice00add.DIG', '')
        Unknown4015()
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 4051):
                sendToLabel(0)
    sprite('null', 4)
    sprite('null', 30)
    Unknown4007(0)
    label(0)
    sprite('null', 8)
    Unknown3004(-32)

@State
def kym271_Floor_Eff():

    def upon_IMMEDIATE():
        GFX_2('kymef271_FloorIce')
        teleportRelativeX(20000)
        teleportRelativeY(-20000)
        Unknown1096(1500)

        def upon_43():
            if (SLOT_48 == 4051):
                sendToLabel(0)
    sprite('null', 4)
    sprite('null', 30)
    label(0)
    sprite('null', 90)
    Unknown3004(-3)

@State
def kym271_IceCrush_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-50000)
    sprite('vr_kymef271_Ice00', 1)
    GFX_0('kym271_IceCrush00_Eff', 100)
    GFX_0('kym271_IceCrush01_Eff', 100)
    GFX_0('kym271_IceCrush00add_Eff', 100)
    GFX_0('kym271_IceCrush01add_Eff', 100)
    GFX_1('kymef271_kira', 3)
    Unknown4048(-30000)
    Unknown4049(500)
    Unknown4045('kymef271_IceCrush', 3)
    GFX_1('kymef271_kira', 2)
    Unknown4048(-20000)
    Unknown4049(750)
    Unknown4045('kymef271_IceCrush', 2)
    GFX_1('kymef271_kira', 1)
    Unknown4048(10000)
    Unknown4049(1000)
    Unknown4045('kymef271_IceCrush', 1)
    GFX_1('kymef271_IceCrush2', 0)

@State
def kym271_IceCrush00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_271_IceCrush00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3019(255)
        Unknown23015(6)
    sprite('null', 11)
    sprite('keep', 16)
    Unknown3004(-16)

@State
def kym271_IceCrush00add_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_271_IceCrush00add.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(7)
        Unknown3001(128)
    sprite('null', 11)
    sprite('keep', 16)
    Unknown3004(-16)

@State
def kym271_IceCrush01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_271_IceCrush01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(8)
    sprite('null', 3)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym271_IceCrush01add_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_271_IceCrush01add.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(9)
    sprite('null', 3)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym272_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_272_Ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(215)
        teleportRelativeX(205000)
        Unknown1007(-50000)

        def upon_43():
            if (SLOT_48 == 4052):
                sendToLabel(0)
    sprite('null', 5)
    GFX_0('kym272_IceAdd_Eff', 100)
    GFX_0('kym272_Ice_Far_Eff', 100)
    GFX_0('kym272_Ice_FarAdd_Eff', 100)
    GFX_0('kym272_Floor_Eff', 100)
    sprite('null', 25)
    Unknown4007(0)
    label(0)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3004(-25)
    GFX_0('kym272_IceCrush_Eff', 100)

@State
def kym272_Ice_Far_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_272_Ice01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(215)
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 4052):
                sendToLabel(0)
    sprite('null', 5)
    sprite('null', 25)
    Unknown4007(0)
    label(0)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3004(-25)

@State
def kym272_IceAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4013(2)
        Unknown4003('kymef_272_Ice00add.DIG', '')
        Unknown4015()
        Unknown3033()

        def upon_43():
            if (SLOT_48 == 4052):
                sendToLabel(0)
    sprite('null', 5)
    sprite('null', 25)
    Unknown4007(0)
    label(0)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3004(-25)

@State
def kym272_Ice_FarAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_272_Ice01add.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(11)

        def upon_43():
            if (SLOT_48 == 4052):
                sendToLabel(0)
    sprite('null', 5)
    sprite('null', 25)
    Unknown4007(0)
    label(0)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3004(-25)

@State
def kym272_Floor_Eff():

    def upon_IMMEDIATE():
        GFX_2('kymef271_FloorIce')
        teleportRelativeX(-60000)
        teleportRelativeY(-10000)
        Unknown1096(1500)

        def upon_43():
            if (SLOT_48 == 4052):
                sendToLabel(0)
    sprite('null', 5)
    sprite('null', 25)
    label(0)
    sprite('null', 90)
    Unknown3004(-3)

@State
def kym272_IceCrush_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-50000)
    sprite('vr_kymef272_Ice00', 1)
    GFX_0('kym272_IceCrush00_Eff', 100)
    GFX_0('kym272_IceCrush00add_Eff', 100)
    GFX_0('kym272_IceCrush01_Eff', 100)
    GFX_0('kym272_IceCrush01add_Eff', 100)
    GFX_1('kymef271_kira', 3)
    Unknown4049(600)
    Unknown4048(-30000)
    Unknown4045('kymef271_IceCrush', 3)
    GFX_1('kymef271_kira', 2)
    Unknown4049(800)
    Unknown4048(-15000)
    Unknown4045('kymef271_IceCrush', 2)
    GFX_1('kymef271_kira', 1)
    Unknown4049(1000)
    Unknown4048(15000)
    Unknown4045('kymef271_IceCrush', 1)
    GFX_1('kymef271_IceCrush2', 0)

@State
def kym272_IceCrush00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_272_IceCrush00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(8)
    sprite('keep', 8)
    sprite('keep', 16)
    Unknown3004(-16)

@State
def kym272_IceCrush00add_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_272_IceCrush00add.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(9)
    sprite('keep', 8)
    sprite('keep', 16)
    Unknown3004(-16)

@State
def kym272_IceCrush01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_272_IceCrush01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3019(255)
        Unknown23015(12)
    sprite('null', 10)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym272_IceCrush01add_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_272_IceCrush01add.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(127)
        Unknown23015(11)
    sprite('null', 10)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym273_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
    sprite('null', 20)
    GFX_0('kym273_Wind_Eff', 100)
    GFX_0('kym273_Bloom_Eff', 100)

@State
def kym273_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_273_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(223)
    sprite('null', 6)
    sprite('null', 8)
    Unknown3005(-28)

@State
def kym273_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_273_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3001(127)
    sprite('null', 6)
    sprite('null', 8)
    Unknown3005(-12)

@State
def kym274_Storm_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(300000)
    sprite('null', 1)
    sprite('null', 1)
    SFX_3('kymse_13')
    GFX_0('kym274_Wind04_01_Eff', 100)
    GFX_1('kymef274_ground', 100)
    sprite('null', 1)
    GFX_0('kym274_Wind00_01_Eff', 100)
    GFX_0('kym274_Wind01_00_Eff', 100)
    sprite('null', 1)
    GFX_0('kym274_Wind02_01_Eff', 100)
    sprite('null', 1)
    GFX_0('kym274_Wind03_01_Eff', 100)
    GFX_0('kym274_Wind04_00_Eff', 100)
    sprite('null', 1)
    GFX_0('kym274_Wind00_00_Eff', 100)
    GFX_0('kym274_Wind02_02_Eff', 100)
    sprite('null', 2)
    GFX_0('kym274_Wind01_02_Eff', 100)
    sprite('null', 4)
    GFX_0('kym274_Wind01_03_Eff', 100)
    sprite('null', 5)
    GFX_0('kym274_Wind02_03_Eff', 100)
    sprite('null', 1)

@State
def kym274_Wind00_00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_274_Wind00.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown1007(300000)
        Unknown1096(850)
        Unknown1072(-18000)
    sprite('null', 15)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym274_Wind00_01_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind00.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        teleportRelativeX(-180000)
        Unknown1007(185000)
        Unknown1056(850)
        Unknown1064(750)
    sprite('null', 15)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym274_Wind01_00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_274_Wind00.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        teleportRelativeX(30000)
        Unknown1007(100000)
        Unknown1096(500)
    sprite('null', 15)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym274_Wind01_01_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind01.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        teleportRelativeX(30000)
        Unknown1007(270000)
        Unknown1096(450)
    sprite('null', 15)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym274_Wind01_02_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind01.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        teleportRelativeX(-120000)
        Unknown1007(290000)
        Unknown1096(550)
        Unknown1072(-18000)
    sprite('null', 15)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym274_Wind01_03_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_274_Wind01.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        teleportRelativeX(-50000)
        Unknown1007(200000)
        Unknown1056(500)
        Unknown1064(650)
    sprite('null', 15)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym274_Wind02_00_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-75000)
        Unknown1056(1600)
        Unknown1064(2300)
        Unknown1072(-11000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym274_Wind02_01_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-120000)
        Unknown1007(225000)
        Unknown1064(2300)
        Unknown1072(-7000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym274_Wind02_02_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-75000)
        Unknown1007(110000)
        Unknown1056(2700)
        Unknown1064(3000)
        Unknown1072(-17000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym274_Wind02_03_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(30000)
        Unknown1007(40000)
        Unknown1056(2000)
        Unknown1064(1500)
        Unknown1072(-15000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-45)

@State
def kym274_Wind03_00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_274_Wind03.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(0)
        Unknown1007(250000)
        Unknown1064(400)
        Unknown1072(-8000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym274_Wind03_01_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind03.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-85000)
        Unknown1007(135000)
        Unknown1056(1400)
        Unknown1064(400)
        Unknown1072(8000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym274_Wind03_02_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind04.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-45000)
        Unknown1007(70000)
        Unknown1056(700)
        Unknown1064(550)
        Unknown1072(-8000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-45)

@State
def kym274_Wind04_00_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind04.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-75000)
        Unknown1007(250000)
        Unknown1056(400)
        Unknown1064(600)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym274_Wind04_01_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4003('kymef_274_Wind04.DIG', '')
        Unknown4015()
        Unknown4009(2)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        teleportRelativeX(-35000)
        Unknown1007(100000)
        Unknown1056(1400)
        Unknown1064(600)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym275_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1007(-10000)
    sprite('null', 20)
    GFX_0('kym275_Wind_Eff', 100)
    GFX_0('kym275_Bloom_Eff', 100)

@State
def kym275_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_275_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(159)
    sprite('null', 8)
    sprite('null', 6)
    Unknown3004(-25)

@State
def kym275_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_275_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(127)
        Unknown3013(191)
        Unknown3001(159)
    sprite('null', 8)
    sprite('null', 6)
    Unknown3004(-25)

@State
def kym320_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
    sprite('null', 45)
    GFX_0('kym320_BG_Add_Eff', 100)
    GFX_0('kym320_BG_Color_Eff', 100)
    GFX_0('kym320_Ring00_Eff', 100)
    GFX_0('kym320_Ring01_Eff', 100)

@State
def kym320_BG_Add_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_320_BGglow.DIG', '')
        Unknown4015()
        Unknown23015(14)
        Unknown3033()
    sprite('null', 20)
    sprite('null', 15)
    Unknown3004(-12)

@State
def kym320_BG_Color_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_320_BGglow.DIG', '')
        Unknown4015()
        Unknown23015(15)
        Unknown3032()
        Unknown1096(1200)
        Unknown3007(0)
        Unknown3013(84)
    sprite('null', 30)
    sprite('null', 15)
    Unknown3004(-12)

@State
def kym320_Ring00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_320_Ring.DIG', '')
        Unknown4015()
        Unknown3033()
    sprite('null', 12)

@State
def kym320_Ring01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_320_Ring.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1096(550)
    sprite('null', 12)

@State
def kym320_Flash_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
    sprite('null', 100)
    GFX_0('kym320_Flash00_Eff', 100)
    GFX_0('kym320_Flash01_Eff', 100)
    GFX_0('kym320_Blur_Eff', 100)
    GFX_0('kym320_Air_Eff', 100)

@State
def kym320_Flash00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4003('kymef_320_Flash.DIG', '')
        Unknown4015()
        Unknown23015(11)
        Unknown3032()
        Unknown1096(720)
    sprite('null', 19)

@State
def kym320_Flash01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4003('kymef_320_Flash.DIG', '')
        Unknown4015()
        Unknown23015(12)
        Unknown3032()
        Unknown1096(1215)
    sprite('null', 19)

@State
def kym320_Blur_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4003('kymef_320_Blur.DIG', '')
        Unknown4015()
        Unknown23015(13)
        Unknown3033()
        Unknown1096(900)
    sprite('null', 14)
    sprite('null', 10)
    Unknown3004(-26)

@State
def kym320_Air_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('null', 2)
    GFX_0('kym320_Air00_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air04a_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air01_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air03a_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air02_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air02a_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air03_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air01a_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air04_Eff', 100)
    sprite('null', 2)
    GFX_0('kym320_Air00a_Eff', 100)

@State
def kym320_Air00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air00.DIG', '')
        Unknown4015()
        Unknown23015(6)
        Unknown3033()
        Unknown3001(190)
        Unknown1077(-15000, 15000)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air01.DIG', '')
        Unknown4015()
        Unknown23015(6)
        Unknown3033()
        Unknown3001(190)
        Unknown1077(-15000, 15000)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air02_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air02.DIG', '')
        Unknown4015()
        Unknown23015(6)
        Unknown3033()
        Unknown3001(190)
        Unknown1077(-15000, 15000)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air03_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air03.DIG', '')
        Unknown4015()
        Unknown23015(6)
        Unknown3033()
        Unknown3001(190)
        Unknown1077(-15000, 15000)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air04_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air04.DIG', '')
        Unknown4015()
        Unknown23015(6)
        Unknown3033()
        Unknown3001(190)
        Unknown1077(-15000, 15000)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air00a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air00.DIG', '')
        Unknown4015()
        Unknown23015(7)
        Unknown3033()
        Unknown1077(0, 360000)
        Unknown1096(900)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air01a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air01.DIG', '')
        Unknown4015()
        Unknown23015(7)
        Unknown3033()
        Unknown1077(0, 360000)
        Unknown1096(900)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air02a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air02.DIG', '')
        Unknown4015()
        Unknown23015(7)
        Unknown3033()
        Unknown1077(0, 360000)
        Unknown1096(900)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air03a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air03.DIG', '')
        Unknown4015()
        Unknown23015(7)
        Unknown3033()
        Unknown1077(0, 360000)
        Unknown1096(900)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Air04a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4003('kymef_320_Air04.DIG', '')
        Unknown4015()
        Unknown23015(7)
        Unknown3033()
        Unknown1077(0, 360000)
        Unknown1096(900)
    sprite('null', 7)
    sprite('null', 16)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym320_Ground_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
    sprite('null', 100)
    GFX_0('kym320_Ground00_Eff', 100)
    GFX_0('kym320_Ground01_Eff', 100)

@State
def kym320_Ground00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(2)
        Unknown4003('kymef_320_Ground00.DIG', '')
        Unknown4015()
        Unknown23015(2)
        Unknown3032()
        Unknown1007(-50000)
    sprite('null', 23)

@State
def kym320_Ground01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(2)
        Unknown4003('kymef_320_Ground01.DIG', '')
        Unknown4015()
        Unknown23015(2)
        Unknown3032()
    sprite('null', 23)

@State
def kym320_Particle_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        teleportRelativeY(200000)
    sprite('null', 1)
    GFX_1('kymef320_ptcl_inside', 100)
    sprite('null', 1)
    GFX_1('kymef320_ptcl_inside', 100)
    sprite('null', 1)
    GFX_1('kymef320_ptcl_outside', 100)

@State
def kym_Shot_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_401_ice.DIG', '')
        Unknown4015()
        Unknown3033()
        GFX_2('kymef_Shot_bloom')
        Unknown1096(2000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave_Eff', 100)
    GFX_1('kymef_Shot_Glitter04', 100)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave2_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('vr_kymef401_ice', 10)
    Unknown3004(-36)
    GFX_1('kymef_Shot_icebreak', 0)
    SFX_0('018_ice_break_1')

@State
def kym_Shot_B_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_401_ice.DIG', '')
        Unknown4015()
        Unknown3033()
        GFX_2('kymef_Shot_bloom')
        Unknown1096(2000)

        def upon_43():
            if (SLOT_48 == 4402):
                sendToLabel(1)
    label(0)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave_Eff', 100)
    GFX_1('kymef_Shot_Glitter', 100)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave2_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('vr_kymef401_ice', 10)
    Unknown3004(-36)
    GFX_1('kymef_Shot_icebreak', 0)
    SFX_0('018_ice_break_1')

@State
def kym_Shot_30_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_401_ice.DIG', '')
        Unknown4015()
        Unknown3033()
        GFX_2('kymef_Shot_bloom')
        Unknown1096(1750)
        Unknown1072(30000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave_30_Eff', 100)
    Unknown4048(30000)
    Unknown4045('kymef_Shot_Glitter04', 100)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave2_30_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('vr_kymef401_ice', 10)
    Unknown3004(-36)
    GFX_1('kymef_Shot_icebreak', 0)
    SFX_0('018_ice_break_1')

@State
def kym_Shot_45_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_401_ice.DIG', '')
        Unknown4015()
        Unknown3033()
        GFX_2('kymef_Shot_bloom')
        Unknown1096(1500)
        Unknown1072(15000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave_45_Eff', 100)
    Unknown4048(15000)
    Unknown4045('kymef_Shot_Glitter04', 100)
    sprite('vr_kymef401_ice', 2)
    GFX_0('kym_ShotWave2_45_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('vr_kymef401_ice', 10)
    Unknown3004(-36)
    GFX_1('kymef_Shot_icebreak', 0)
    SFX_0('018_ice_break_1')

@State
def kym_ShotWave_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave00.DIG', '')
        Unknown3033()
        Unknown3007(112)
        Unknown3013(183)
        Unknown3019(255)
        Unknown1096(800)
        Unknown1056(800)
        Unknown1099(50)
        Unknown1073(-40000)
        Unknown1077(20000, -20000)
    sprite('null', 5)
    sprite('null', 17)
    Unknown3004(-20)

@State
def kym_ShotWave_30_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave00.DIG', '')
        Unknown3033()
        Unknown3007(112)
        Unknown3013(183)
        Unknown3019(255)
        Unknown1096(700)
        Unknown1099(50)
        Unknown1072(30000)
        Unknown1073(-15000)
        Unknown1077(20000, -20000)
    sprite('null', 5)
    sprite('null', 17)
    Unknown3004(-20)

@State
def kym_ShotWave_45_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave00.DIG', '')
        Unknown3033()
        Unknown3007(52)
        Unknown3013(167)
        Unknown3019(255)
        Unknown1056(600)
        Unknown1099(50)
        Unknown1072(45000)
        Unknown1073(-15000)
        Unknown1077(20000, -20000)
    sprite('null', 5)
    sprite('null', 17)
    Unknown3004(-20)

@State
def kym_ShotWave2_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave01.DIG', '')
        Unknown3033()
        Unknown3007(52)
        Unknown3013(167)
        Unknown3019(255)
        teleportRelativeX(150000)
        Unknown1096(600)
        Unknown1056(600)
        Unknown1099(40)
        Unknown1073(-40000)
        Unknown1077(20000, -20000)
    sprite('null', 4)
    sprite('null', 18)
    Unknown3004(-20)

@State
def kym_ShotWave2_30_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave01.DIG', '')
        Unknown3033()
        Unknown3007(52)
        Unknown3013(167)
        Unknown3019(255)
        teleportRelativeX(-20000)
        Unknown1007(20000)
        Unknown1096(500)
        Unknown1056(500)
        Unknown1099(40)
        Unknown1072(30000)
        Unknown1073(-15000)
        Unknown1077(20000, -20000)
    sprite('null', 4)
    sprite('null', 18)
    Unknown3004(-20)

@State
def kym_ShotWave2_45_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave01.DIG', '')
        Unknown3033()
        Unknown3007(112)
        Unknown3013(183)
        Unknown3019(255)
        teleportRelativeX(-10000)
        Unknown1007(20000)
        Unknown1096(400)
        Unknown1056(400)
        Unknown1099(40)
        Unknown1072(45000)
        Unknown1073(-15000)
        Unknown1077(20000, -20000)
    sprite('null', 4)
    sprite('null', 18)
    Unknown3004(-20)

@State
def kym_ShotWind00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_shotwind00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(-45000)
        teleportRelativeX(80000)
        Unknown1096(6000)
        Unknown3001(155)
    sprite('null', 4)
    sprite('null', 4)
    Unknown3004(-12)
    sprite('null', 4)
    sprite('null', 8)
    Unknown3004(-15)

@State
def kym_ShotWind01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_shotwind01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(20000)
        teleportRelativeX(35000)
        Unknown1096(6500)
        Unknown3001(155)
    sprite('null', 4)
    sprite('null', 4)
    Unknown3004(-12)
    sprite('null', 4)
    sprite('null', 8)
    Unknown3004(-15)

@State
def kym_ShotWind02_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_shotwind01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(20000)
        teleportRelativeX(35000)
        Unknown1096(7000)
        Unknown1072(15000)
        Unknown3001(155)
    sprite('null', 4)
    sprite('null', 4)
    Unknown3004(-12)
    sprite('null', 4)
    sprite('null', 8)
    Unknown3004(-15)

@State
def kym402_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(215)
        teleportRelativeX(70000)
        Unknown1056(4000)
        Unknown1064(5000)
        Unknown1072(13000)
    sprite('null', 44)
    SFX_3('kymse_09')
    GFX_0('kym402_IceMp00_Eff', 100)
    GFX_1('kymef402_icemake', 100)
    GFX_1('kymef402_icegrow', 100)
    label(0)
    sprite('null', 29)
    sprite('null', 4)
    GFX_0('kym402_icebreakAn00_Eff', 100)
    GFX_0('kym402_icebreakAn00Mp_Eff', 100)
    Unknown3004(-5)

@State
def kym402_Ice2_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_ice01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(220)
        teleportRelativeX(55000)
        Unknown1056(4500)
        Unknown1064(6000)
        Unknown1072(15000)
        Unknown1073(1000)
    sprite('null', 31)
    SFX_3('kymse_09')
    GFX_0('kym402_IceMp01_Eff', 100)
    Unknown4049(1100)
    Unknown4045('kymef402_icemake', 100)
    Unknown4049(1100)
    Unknown4045('kymef402_icegrow', 100)
    label(0)
    sprite('null', 29)
    sprite('null', 4)
    GFX_0('kym402_icebreakAn01_Eff', 100)
    GFX_0('kym402_icebreakAn01Mp_Eff', 100)
    Unknown3004(-5)

@State
def kym402_Ice3_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_ice02.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(220)
        teleportRelativeX(125000)
        Unknown1007(-30000)
        Unknown1056(5600)
        Unknown1064(6200)
        Unknown1072(15000)
    sprite('null', 16)
    SFX_3('kymse_09')
    GFX_0('kym402_IceMp02_Eff', 100)
    Unknown4049(1300)
    Unknown4045('kymef402_icemake', 100)
    Unknown4049(1300)
    Unknown4045('kymef402_icegrow', 100)
    sprite('null', 29)
    Unknown21012('kym402_Ice_Eff', 32)
    Unknown21012('kym402_Ice2_Eff', 32)
    sprite('null', 4)
    SFX_3('kymse_10')
    GFX_0('kym402_icebreakAn02_Eff', 100)
    GFX_0('kym402_icebreakAn02Mp_Eff', 100)
    Unknown3004(-5)

@State
def kym402_IceMp00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_iceMp00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(4000)
        Unknown1064(5000)
        Unknown1072(13000)
    sprite('null', 76)

@State
def kym402_IceMp01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_iceMp01.DIG', '')
        Unknown4015()
        Unknown1056(4500)
        Unknown1064(6000)
        Unknown1072(16000)
        Unknown3033()
    sprite('null', 60)

@State
def kym402_IceMp02_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_iceMp02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(5600)
        Unknown1064(6200)
        Unknown1072(15000)
    sprite('null', 45)

@State
def kym402_icebreakAn00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_icebreakAn00.DIG', '')
        Unknown4015()
        Unknown1056(4000)
        Unknown1064(5000)
        Unknown1072(13000)
        Unknown3032()
        Unknown3001(200)
    sprite('null', 10)
    Unknown4049(700)
    Unknown4045('kymef402_footice01', 100)
    Unknown4049(700)
    Unknown4048(12000)
    Unknown4045('kymef402_icebreak_pos1', 100)
    Unknown4049(500)
    Unknown4048(15000)
    Unknown4045('kymef402_icebreak_pos2', 100)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym402_icebreakAn01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_icebreakAn01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
        Unknown1056(4500)
        Unknown1064(6000)
        Unknown1072(15000)
    sprite('null', 10)
    Unknown4049(800)
    Unknown4045('kymef402_footice01', 100)
    Unknown4049(800)
    Unknown4048(12000)
    Unknown4045('kymef402_icebreak_pos1', 100)
    Unknown4049(550)
    Unknown4048(15000)
    Unknown4045('kymef402_icebreak_pos2', 100)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym402_icebreakAn02_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_icebreakAn02.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
        Unknown1056(5600)
        Unknown1064(6200)
        Unknown1072(15000)
    sprite('null', 10)
    GFX_1('kymef402_footice', 100)
    Unknown4048(12000)
    Unknown4045('kymef402_icebreak_pos1', 100)
    Unknown4049(600)
    Unknown4048(15000)
    Unknown4045('kymef402_icebreak_pos2', 100)
    sprite('null', 16)
    Unknown3004(-16)

@State
def kym402_icebreakAn00Mp_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_icebreakAnMp00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(4000)
        Unknown1064(5000)
        Unknown1072(13000)
    sprite('null', 7)
    sprite('null', 13)
    Unknown3004(-45)

@State
def kym402_icebreakAn01Mp_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_icebreakAnMp01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(4500)
        Unknown1064(6000)
        Unknown1072(15000)
    sprite('null', 7)
    sprite('null', 13)
    Unknown3004(-45)

@State
def kym402_icebreakAn02Mp_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_icebreakAnMp02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(5600)
        Unknown1064(6200)
        Unknown1072(15000)
    sprite('null', 7)
    sprite('null', 13)
    Unknown3004(-45)

@State
def kym402_ougiwind00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(50000)
        Unknown1007(220000)
        Unknown1096(1400)
    sprite('null', 4)
    sprite('null', 3)
    Unknown1100(10)
    sprite('null', 3)
    Unknown3005(-13)
    sprite('null', 4)
    Unknown3005(-10)

@State
def kym402_ougiwind01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_wind01.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(30000)
        Unknown1007(120000)
        Unknown1064(1400)
        Unknown1056(2400)
        Unknown1073(-20000)
    sprite('null', 4)
    sprite('null', 3)
    Unknown1099(10)
    sprite('null', 3)
    Unknown3005(-13)
    sprite('null', 4)
    Unknown3005(-10)

@State
def kym402_ougiwind02_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_402_wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(170000)
        Unknown1007(225000)
        Unknown1064(1800)
        Unknown1056(2800)
        Unknown1072(-10000)
    sprite('null', 4)
    sprite('null', 4)
    Unknown1100(10)
    sprite('null', 4)
    Unknown3005(-13)
    sprite('null', 7)
    Unknown3005(-10)

@State
def kym_Blow_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym274_Blow_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-120000)
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym407_Blow_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-30000)
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym408_Blow_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-170000)
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym409_Blow_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-100000)
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym413_Blow2_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(150000)
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym413_Blow2_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(150000)
    sprite('null', 1)
    GFX_1('kymef_Blow', 100)

@State
def kym403_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(200000)

        def upon_56():
            Unknown4007(0)
    sprite('null', 20)
    GFX_0('kym403_Wind_Eff', 100)
    GFX_0('kym403_Bloom_Eff', 100)

@State
def kym403_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_403_Wind.DIG', '')
        Unknown4009(3)
        Unknown4015()
        Unknown3033()
        Unknown3001(160)

        def upon_56():
            Unknown4007(0)
    sprite('null', 20)

@State
def kym403_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_403_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(128)
        Unknown3007(127)
        Unknown3013(191)

        def upon_56():
            Unknown4007(0)
    sprite('null', 5)
    sprite('null', 11)
    Unknown3004(-8)

@State
def kym404_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)

        def upon_56():
            Unknown4007(0)
    sprite('null', 20)
    GFX_0('kym404_Wind_Eff', 100)
    GFX_0('kym404_Bloom_Eff', 100)

@State
def kym404_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_404_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(160)

        def upon_56():
            Unknown4007(0)
    sprite('null', 20)

@State
def kym404_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_404_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(128)
        Unknown3007(127)
        Unknown3013(191)

        def upon_56():
            Unknown4007(0)
    sprite('null', 5)
    sprite('null', 15)
    Unknown3004(-9)

@State
def kym405_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(100000)

        def upon_56():
            Unknown4007(0)
    sprite('null', 2)
    sprite('null', 9)
    GFX_0('kym405_Wind00_Eff', 100)
    GFX_0('kym405_Bloom00_Eff', 100)
    sprite('null', 100)
    GFX_0('kym405_b_Eff', 100)

@State
def kym405_Wind00_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_405_Wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(200)

        def upon_56():
            Unknown4007(0)
    sprite('null', 9)
    sprite('null', 1)
    sprite('null', 5)
    Unknown3004(-40)

@State
def kym405_Bloom00_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_405_Bloom00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(120)
        Unknown3013(185)

        def upon_56():
            Unknown4007(0)
    sprite('null', 9)
    sprite('null', 1)
    sprite('null', 5)
    Unknown3004(-53)

@State
def kym405_b_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(20000)

        def upon_56():
            Unknown4007(0)
    sprite('null', 100)
    GFX_0('kym405_Wind01_Eff', 100)
    GFX_0('kym405_Bloom01_Eff', 100)

@State
def kym405_Wind01_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_405_Wind01.DIG', '')
        Unknown4015()
        Unknown3033()

        def upon_56():
            Unknown4007(0)
    sprite('null', 3)
    Unknown3001(50)
    Unknown3004(50)
    sprite('null', 4)
    Unknown3001(200)
    sprite('null', 5)
    Unknown3004(-40)

@State
def kym405_Bloom01_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_405_Bloom01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(120)
        Unknown3013(185)

        def upon_56():
            Unknown4007(0)
    sprite('null', 3)
    Unknown3001(70)
    Unknown3004(50)
    sprite('null', 4)
    Unknown3001(255)
    sprite('null', 5)
    Unknown3004(-53)

@State
def kym405_2nd_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeX(90000)

        def upon_56():
            Unknown4007(0)
    sprite('null', 100)
    GFX_0('kym405_Wind02_Eff', 100)
    GFX_0('kym405_Bloom02_Eff', 100)

@State
def kym405_Wind02_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_405_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(200)

        def upon_56():
            Unknown4007(0)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-40)

@State
def kym405_Bloom02_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_405_Bloom02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(120)
        Unknown3013(185)

        def upon_56():
            Unknown4007(0)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3004(-53)

@State
def kym406_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_201_Wind.DIG', '')
        Unknown1072(80000)
        teleportRelativeX(30000)
        Unknown3033()

        def upon_56():
            Unknown4007(0)
    sprite('null', 4)
    GFX_0('kym201_Cross_Eff', 100)
    GFX_0('kym406_Aroundwind00_Eff', 100)
    GFX_0('kym406_Aroundwind02_Eff', 100)
    GFX_0('kym406_Aroundwind03_Eff', 100)
    GFX_0('kym406_Aroundwind00_Eff', 100)
    GFX_0('kym406_Aroundwind01_Eff', 100)
    Unknown1096(750)
    Unknown1099(50)
    Unknown3001(0)
    Unknown3004(50)
    sprite('null', 4)
    GFX_0('kym406_Aroundwind01_Eff', 100)
    GFX_0('kym406_Aroundwind02_Eff', 100)
    GFX_0('kym406_Aroundwind00_Eff', 100)
    Unknown3001(220)
    Unknown1099(0)
    Unknown1096(1000)
    sprite('null', 5)
    GFX_0('kym406_Aroundwind01_Eff', 100)
    GFX_0('kym406_Aroundwind03_Eff', 100)
    GFX_0('kym406_Aroundwind03_Eff', 100)
    sprite('null', 1)
    GFX_0('kym406_Aroundwind00_Eff', 100)
    GFX_0('kym406_Aroundwind01_Eff', 100)
    GFX_0('kym406_Aroundwind03_Eff', 100)
    sprite('null', 9)
    Unknown1099(-100)
    Unknown3004(-50)

@State
def kym406_Aroundwind00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_406_Aroundwind00.DIG', '')
        Unknown3033()
        Unknown3001(220)
        Unknown1007(-10000)
        teleportRelativeX(-9000)
        Unknown1102(1000, 500)
        Unknown1100(90)
        Unknown1077(15000, -15000)
        GFX_1('kymef406_ice03', 100)

        def upon_56():
            Unknown4007(0)
    sprite('null', 8)
    Unknown1015(5000)
    Unknown3004(-12)
    sprite('null', 12)

@State
def kym406_Aroundwind01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_406_Aroundwind01.DIG', '')
        Unknown3033()
        Unknown3007(112)
        Unknown3013(183)
        Unknown3019(255)
        Unknown3001(220)
        teleportRelativeX(30000)
        teleportRelativeX(-9000)
        Unknown1102(1200, 700)
        Unknown1100(50)
        Unknown1077(15000, -25000)

        def upon_56():
            Unknown4007(0)
    sprite('null', 8)
    Unknown1015(6000)
    Unknown3004(-15)
    sprite('null', 15)

@State
def kym406_Aroundwind02_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_406_Aroundwind02.DIG', '')
        Unknown3033()
        teleportRelativeX(-9000)
        Unknown1096(800)
        Unknown1100(50)
        Unknown1077(25000, -25000)

        def upon_56():
            Unknown4007(0)
    sprite('null', 8)
    Unknown1015(5000)
    Unknown3004(-10)
    sprite('null', 15)

@State
def kym406_Aroundwind03_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_406_Aroundwind02.DIG', '')
        Unknown3033()
        teleportRelativeX(-5000)
        teleportRelativeX(-9000)
        Unknown1096(2500)
        Unknown1100(50)
        Unknown1077(25000, -25000)

        def upon_56():
            Unknown4007(0)
        Unknown3001(255)
    sprite('null', 8)
    Unknown1015(5000)
    Unknown3004(-10)
    sprite('null', 15)

@State
def kym407_Flash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        GFX_2('kymef407_bloom02')
    sprite('null', 3)

@State
def kym407_Ice00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_407_ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        GFX_2('kymef407_bloom01')
        Unknown1096(800)
        Unknown1064(1100)
        Unknown1056(600)
    sprite('null', 32767)
    GFX_0('kym407_Ice_Bloom_Eff', 0)

@State
def kym407_Ice01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_407_ice01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown1096(800)
        Unknown1064(1100)
        Unknown1056(600)
    sprite('null', 32767)

@State
def kym407_Ice_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_407_icebloom.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-35000)
        Unknown1064(1100)
        Unknown1056(600)
        Unknown3001(80)
    sprite('null', 32767)

@State
def kym407_Ice_extend00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('kymef_407_ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown1007(-5000)
        teleportRelativeX(-1000)
        Unknown1056(1200)
        Unknown1064(1400)
        sendToLabelUpon(32, 0)
    sprite('null', 2)
    GFX_0('kym407_Ice_extendBloom_Eff', 0)
    Unknown1056(1200)
    sprite('null', 2)
    Unknown4009(2)
    Unknown1056(1400)
    sprite('null', 3)
    label(0)
    sprite('null', 0)
    Unknown4007(0)
    sprite('null', 1)
    GFX_0('kym407_icebreak_Eff', 0)
    GFX_0('kym407_Flash_Eff', 1)
    sprite('null', 4)
    sprite('null', 32)
    Unknown3004(-100)

@State
def kym407_Ice_extend01_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('kymef_407_ice01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown1007(-5000)
        teleportRelativeX(-1000)
        Unknown1056(1200)
        Unknown1064(1400)
        sendToLabelUpon(32, 0)
    sprite('null', 3)
    Unknown1096(1200)
    sprite('null', 2)
    Unknown4009(2)
    Unknown1096(1400)
    sprite('null', 4)
    label(0)
    sprite('null', 1)
    Unknown4007(0)
    GFX_0('kym407_Flash_Eff', 1)
    sprite('null', 4)
    sprite('null', 32)
    Unknown3004(-100)

@State
def kym407_Ice_extendBloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_407_icebloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(-2000)
        teleportRelativeX(-1000)
        Unknown1064(1500)
        Unknown1056(1500)
        Unknown3001(80)
    sprite('null', 3)
    Unknown1096(800)
    sprite('null', 1)
    Unknown1096(1200)
    sprite('null', 3)
    Unknown4009(2)
    Unknown1096(1400)
    sprite('null', 8)

@State
def kym407_Ice_airextend00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('kymef_407_ice00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown1007(-5000)
        teleportRelativeX(-1000)
        Unknown1056(1200)
        Unknown1064(1400)
        sendToLabelUpon(32, 0)
    sprite('null', 3)
    GFX_0('kym407_Ice_airextendBloom_Eff', 0)
    Unknown1056(600)
    sprite('null', 1)
    Unknown1056(1200)
    sprite('null', 3)
    Unknown4009(2)
    Unknown1056(1400)
    GFX_0('kym407_icebreak_Eff', 0)
    sprite('null', 32)
    label(0)
    sprite('null', 1)
    Unknown4007(0)
    GFX_0('kym407_Flash_Eff', 1)
    sprite('null', 2)
    sprite('null', 32)
    Unknown3004(-100)

@State
def kym407_Ice_airextend01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('kymef_407_ice01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown1007(-5000)
        teleportRelativeX(-1000)
        Unknown1056(1200)
        Unknown1064(1400)
        sendToLabelUpon(32, 0)
    sprite('null', 3)
    Unknown1096(800)
    sprite('null', 1)
    Unknown1096(1200)
    sprite('null', 2)
    Unknown4009(2)
    Unknown1096(1400)
    sprite('null', 3)
    label(0)
    sprite('null', 1)
    Unknown4007(0)
    GFX_0('kym407_Flash_Eff', 1)
    sprite('null', 2)
    sprite('null', 32)
    Unknown3004(-100)

@State
def kym407_Ice_airextendBloom_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_407_icebloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(-2000)
        teleportRelativeX(-1000)
        Unknown1064(1500)
        Unknown1056(1500)
        Unknown3001(60)
    sprite('null', 3)
    Unknown1096(800)
    sprite('null', 1)
    Unknown1096(1200)
    sprite('null', 3)
    Unknown4009(2)
    Unknown1096(1400)
    sprite('null', 8)
    Unknown3001(0)

@State
def kym407_icebreak_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('kymef407_icebreak')
    sprite('null', 1)
    sprite('null', 64)
    Unknown4007(0)

@State
def kym408_IceBoard_1st_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(11)
        teleportRelativeX(-80000)
        Unknown1007(-20000)
        Unknown1056(120)
        Unknown1064(450)
        Unknown1062(800, 800)
        Unknown1070(800, 800)
        Unknown1099(120)
    sprite('null', 8)
    GFX_1('kymef408_Glitter', 100)
    Unknown4049(2000)
    Unknown4045('kymef408_icefloor', 100)
    Unknown4045('kymef030_icefloor', 100)
    sprite('null', 31)
    Unknown1099(0)
    sprite('null', 15)
    Unknown3004(-35)
    GFX_1('kymef408_icebreak', 100)
    SFX_0('018_ice_break_1')
    Unknown21012('kym408_IceBoard1_Eff', 32)
    Unknown21012('kym408_IceBoard2_Eff', 32)
    Unknown21012('kym408_IceBoard3_Eff', 32)
    Unknown21012('kym408_IceBoard_sml1_Eff', 32)
    Unknown21012('kym408_IceBoard_sml2_Eff', 32)
    Unknown21012('kym408_IceBoard_sml3_Eff', 32)
    Unknown21012('kym408_IceBoard_End_Eff', 32)
    Unknown21012('kym408_IceBoard_smlEnd_Eff', 32)

@State
def kym408_IceBoard1_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(11)
        teleportRelativeX(-80000)
        Unknown1007(-20000)
        Unknown1056(240)
        Unknown1064(450)
        Unknown1062(800, 500)
        Unknown1070(1500, 1500)
        Unknown1099(100)
        GFX_1('kymef408_Glitter', 100)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 2)
    Unknown3004(-35)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard2_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(11)
        teleportRelativeX(-50000)
        Unknown1007(-20000)
        Unknown1056(450)
        Unknown1064(600)
        Unknown1062(850, 700)
        Unknown1070(1800, 1200)
        Unknown1099(120)
        GFX_1('kymef408_Glitter', 100)
        sendToLabelUpon(32, 0)
    sprite('null', 3)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 3)
    Unknown3004(-34)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard3_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash02.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(11)
        teleportRelativeX(-60000)
        Unknown1007(-20000)
        Unknown1056(230)
        Unknown1064(520)
        Unknown1062(860, 700)
        Unknown1070(1600, 1200)
        GFX_1('kymef408_Glitter', 100)
        Unknown1099(100)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 4)
    Unknown3004(-36)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard_sml1_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(11)
        teleportRelativeX(20000)
        Unknown1007(-30000)
        Unknown1062(1000, 1100)
        Unknown1070(1200, 800)
        Unknown1099(86)
        sendToLabelUpon(32, 0)
        GFX_1('kymef408_Glitter', 100)
    sprite('null', 8)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 2)
    Unknown3004(-35)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard_sml2_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(11)
        teleportRelativeX(50000)
        Unknown1007(-20000)
        Unknown3001(240)
        Unknown1056(2500)
        Unknown1064(1200)
        Unknown1070(1100, 900)
        Unknown1099(65)
        sendToLabelUpon(32, 0)
        GFX_1('kymef408_icefloor', 100)
    sprite('null', 6)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 25)
    Unknown3004(-19)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard_sml3_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash01.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(11)
        teleportRelativeX(80000)
        Unknown1007(-20000)
        Unknown3001(240)
        Unknown1056(2400)
        Unknown1064(880)
        Unknown1070(1200, 800)
        Unknown1099(68)
        sendToLabelUpon(32, 0)
        GFX_1('kymef408_Glitter_pin', 100)
    sprite('null', 6)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 25)
    Unknown3004(-18)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard_End_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(11)
        teleportRelativeX(10000)
        Unknown1007(-20000)
        Unknown1056(2500)
        Unknown1064(1800)
        Unknown1072(2500)
        Unknown1099(86)
        sendToLabelUpon(32, 0)
        GFX_1('kymef408_Glitter', 100)
        Unknown3001(200)
    sprite('null', 8)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 2)
    Unknown3004(-35)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_IceBoard_smlEnd_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_030_icedash01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(11)
        teleportRelativeX(-120000)
        Unknown1007(-20000)
        Unknown1056(2000)
        Unknown1064(3000)
        Unknown1099(100)
        sendToLabelUpon(32, 0)
    sprite('null', 5)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 2)
    Unknown3004(-35)
    GFX_1('kymef408_icebreak', 100)

@State
def kym408_wind_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_408_slashwind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(90000)
        teleportRelativeX(90000)
        Unknown1096(1300)
        Unknown3001(180)
    sprite('null', 1)
    sprite('null', 6)
    Unknown3004(-5)
    sprite('null', 5)
    Unknown3004(-16)
    sprite('null', 7)
    SFX_3('kymse_10')

@State
def kym409_IceWave_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 3)
    label(0)
    sprite('null', 3)
    GFX_0('kym409_Wave_Eff', 100)
    Unknown4048(270000)
    Unknown4049(1500)
    Unknown4045('kymef_Shot_Glitter', 100)
    GFX_0('kym409_Wave2_Eff', 100)
    gotoLabel(0)

@State
def kym409_Wave_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave00.DIG', '')
        Unknown3007(112)
        Unknown3013(183)
        Unknown3019(255)
        Unknown1096(800)
        Unknown1056(800)
        Unknown1099(50)
        Unknown3033()
        Unknown1077(12000, -12000)
        Unknown1073(90000)
    sprite('null', 5)
    sprite('null', 17)
    Unknown3004(-20)

@State
def kym409_Wave2_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_401_icewave01.DIG', '')
        Unknown3007(52)
        Unknown3013(167)
        Unknown3019(255)
        Unknown1096(1500)
        Unknown1056(800)
        Unknown1064(500)
        Unknown1007(-50000)
        Unknown1099(50)
        Unknown3033()
        Unknown1077(10000, -10000)
        Unknown1073(90000)
    sprite('null', 5)
    sprite('null', 17)
    Unknown3004(-20)

@State
def kym409_Wave3_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_409_icewave.DIG', '')
        Unknown1096(1620)
        Unknown1057(1800)
        Unknown1099(120)
        Unknown3033()
        Unknown1073(90000)
    sprite('null', 11)
    sprite('null', 11)
    Unknown3004(-25)

@State
def kym409_iceGrow_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_409_icegrow.DIG', '')
        Unknown4015()
        Unknown1096(1500)
        Unknown1065(800)
        Unknown1057(800)
        Unknown3032()
        Unknown23015(11)
    sprite('null', 40)
    SFX_3('kymse_06')
    sprite('null', 100)
    Unknown3004(-15)

@State
def kym_ComboSpark_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        GFX_2('kymef_ComboSpark')
    sprite('null', 13)
    sprite('null', 10)
    Unknown4007(0)

@State
def kym410_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 20)
    GFX_0('kym410_Wind_Eff', 100)
    GFX_0('kym410_Bloom_Eff', 100)

@State
def kym410_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_410_Wind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(160)
    sprite('null', 20)

@State
def kym410_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_410_Bloom.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(128)
        Unknown3007(127)
        Unknown3013(191)
    sprite('null', 5)
    sprite('null', 15)
    Unknown3004(-9)

@State
def kym413_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)

        def upon_56():
            Unknown4007(0)
    sprite('null', 2)
    sprite('null', 1)
    GFX_0('kym413_Wind_Eff', 100)
    GFX_0('kym413_Bloom_Eff', 100)
    sprite('null', 6)
    sprite('null', 1)
    GFX_0('kym413_Wind2_Eff', 100)
    GFX_0('kym413_Bloom2_Eff', 100)
    sprite('null', 1)
    GFX_0('kym413_Wind3_Eff', 100)
    GFX_0('kym413_Bloom3_Eff', 100)
    sprite('null', 40)

@State
def kym413_Wind_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_413_Wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(170)

        def upon_56():
            Unknown4007(0)
    sprite('null', 15)
    sprite('null', 5)
    Unknown3004(-35)

@State
def kym413_Bloom_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_413_Bloom00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(210)
        Unknown3013(230)
        Unknown3001(130)

        def upon_56():
            Unknown4007(0)
    sprite('null', 15)
    sprite('null', 5)
    Unknown3004(-25)

@State
def kym413_Wind2_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_413_Wind01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(200)

        def upon_56():
            Unknown4007(0)
    sprite('null', 20)
    sprite('null', 5)
    Unknown3004(-40)

@State
def kym413_Bloom2_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_413_Bloom01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(210)
        Unknown3013(230)
        Unknown3001(200)

        def upon_56():
            Unknown4007(0)
    sprite('null', 20)
    sprite('null', 5)
    Unknown3004(-40)

@State
def kym413_Wind3_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_413_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(170)

        def upon_56():
            Unknown4007(0)
    sprite('null', 28)
    sprite('null', 5)
    Unknown3004(-20)
    sprite('null', 5)
    Unknown3004(-13)

@State
def kym413_Bloom3_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4003('kymef_413_Bloom02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(210)
        Unknown3013(230)
        Unknown3001(200)

        def upon_56():
            Unknown4007(0)
    sprite('null', 28)
    sprite('null', 5)
    Unknown3004(-25)
    sprite('null', 5)
    Unknown3004(-15)

@State
def kym414_Eff():

    def upon_IMMEDIATE():
        Unknown4015()
        Unknown3033()
        teleportRelativeX(300000)
        Unknown1007(50000)
    sprite('null', 3)
    GFX_0('kym414_Storm_Eff', 100)
    sprite('null', 4)
    GFX_1('kymef414_Wind', 100)
    sprite('null', 4)
    Unknown3010(-13)
    Unknown3016(-14)
    sprite('null', 9)
    GFX_0('kym414_Storm2_Eff', 100)
    Unknown3010(-13)
    Unknown3016(-14)

@State
def kym414_Storm_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 2)
    SFX_3('kymse_13')
    sprite('null', 2)
    GFX_0('kym414_Storm02_2_Eff', 100)
    sprite('null', 2)
    GFX_0('kym414_Storm4', 100)
    GFX_0('kym414_Storm01_1_Eff', 100)
    sprite('null', 3)
    GFX_0('kym414_Storm03_3_Eff', 100)
    GFX_0('kym414_Storm02_3_Eff', 100)
    sprite('null', 6)
    GFX_0('kym414_Storm01_3_Eff', 100)
    GFX_0('kym414_Storm03_1_Eff', 100)

@State
def kym414_Storm2_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_0('kym414_Storm03_4_Eff', 100)
    GFX_0('kym414_Storm02_4_Eff', 100)
    sprite('null', 1)
    GFX_0('kym414_Storm01_4_Eff', 100)
    GFX_0('kym414_Storm03_2_Eff', 100)
    sprite('null', 1)
    GFX_0('kym414_StormEnd01_00_Eff', 100)
    sprite('null', 1)
    GFX_0('kym414_StormEnd00_01_Eff', 100)
    sprite('null', 1)
    GFX_0('kym414_StormEnd00_00_Eff', 100)

@State
def kym414_Storm01_1_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_414_Storm00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(800)
        Unknown1064(500)
        teleportRelativeX(115000)
        Unknown1007(120000)
        Unknown1072(-55000)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym414_Storm01_3_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_Storm00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(1100)
        Unknown1064(350)
        teleportRelativeX(-45000)
        Unknown1007(250000)
        Unknown1072(-75000)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym414_Storm01_4_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_Storm00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(300)
        teleportRelativeX(95000)
        Unknown1007(250000)
        Unknown1072(-75000)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym414_Storm02_2_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_Storm01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(800)
        Unknown1064(500)
        teleportRelativeX(125000)
        Unknown1007(100000)
        Unknown1072(-52000)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym414_Storm02_3_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_Storm01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(1300)
        Unknown1064(625)
        Unknown1007(130000)
        Unknown1072(-70000)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym414_Storm02_4_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_Storm01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(475)
        teleportRelativeX(60000)
        Unknown1007(130000)
        Unknown1072(-70000)
    sprite('null', 10)
    sprite('null', 12)
    Unknown3004(-20)
    Unknown3010(-10)
    Unknown3016(-7)

@State
def kym414_Storm03_1_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown1056(2000)
        Unknown1064(1500)
        teleportRelativeX(-60000)
        Unknown1007(250000)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown1072(-78000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym414_Storm03_2_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(1600)
        Unknown1064(1500)
        teleportRelativeX(-60000)
        Unknown1007(120000)
        Unknown3007(200)
        Unknown3013(240)
        Unknown1072(-78000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym414_Storm03_3_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown1056(1500)
        Unknown1064(1500)
        teleportRelativeX(75000)
        Unknown1007(120000)
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown1072(-55000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym414_Storm03_4_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_274_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1096(1500)
        teleportRelativeX(225000)
        Unknown1007(80000)
        Unknown3007(200)
        Unknown3013(240)
        Unknown1072(-55000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym414_Storm4():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_274_Wind03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1096(900)
        teleportRelativeX(150000)
        Unknown1007(100000)
        Unknown3007(200)
        Unknown3013(240)
        Unknown1072(-65000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym414_StormEnd00_00_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_StormEnd00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(1350)
        Unknown1064(500)
        teleportRelativeX(-80000)
        Unknown1007(260000)
        Unknown3001(135)
        Unknown3007(135)
        Unknown3013(200)
        Unknown1072(-75000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-6)
    sprite('null', 5)
    Unknown3005(-16)

@State
def kym414_StormEnd00_01_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_StormEnd00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(1300)
        Unknown1064(450)
        teleportRelativeX(60000)
        Unknown1007(190000)
        Unknown3001(135)
        Unknown3007(135)
        Unknown3013(200)
        Unknown1072(-75000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-6)
    sprite('null', 5)
    Unknown3005(-16)

@State
def kym414_StormEnd01_00_Eff():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_414_StormEnd01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(750)
        Unknown1064(550)
        teleportRelativeX(170000)
        Unknown1007(155000)
        Unknown3007(200)
        Unknown3013(240)
        Unknown1072(-70000)
    sprite('null', 10)
    sprite('null', 5)
    Unknown3005(-12)
    sprite('null', 5)
    Unknown3005(-35)

@State
def kym415_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('kymef_415_ice00.DIG', '')
        Unknown4015()
        Unknown23015(8)
        Unknown3033()
        teleportRelativeX(130000)
        Unknown1007(5000)
        Unknown1072(-1200)

        def upon_43():
            if (SLOT_48 == 4151):
                clearUponHandler(43)
                sendToLabel(0)
            if (SLOT_48 == 4152):
                clearUponHandler(43)
                Unknown1096(1100)
                Unknown1099(0)
                sendToLabel(1)
    sprite('null', 3)
    Unknown1096(550)
    Unknown1099(68)
    GFX_0('kym415_kira_Eff', 100)
    sprite('null', 5)
    SFX_3('kymse_18')
    sprite('null', 60)
    Unknown1096(1100)
    Unknown1099(0)
    label(0)
    sprite('null', 30)
    Unknown3004(-16)
    loopRest()
    ExitState()
    label(1)
    sprite('null', 30)
    Unknown3001(255)
    Unknown3004(0)
    Unknown23117(16777215, 8)

@State
def kym415_kira_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
    sprite('null', 60)
    GFX_2('kymef415_kira')

@State
def kym415_IceCrash_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_415_ice00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(130000)
        Unknown1007(5000)
        Unknown1096(1100)
        Unknown1072(-1200)
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 10)
    Unknown4003('kymef_415_ice01.DIG', '')
    Unknown4049(1250)
    Unknown4045('kymef415_Clash', 100)
    SFX_3('kymse_10')
    sprite('null', 16)
    Unknown1099(5)
    Unknown3004(-16)

@State
def kym430_Charge_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 68)
    GFX_0('kym430_ChargeAir_Eff', 100)
    sprite('null', 30)
    sprite('null', 30)

@State
def kym430_ChargeCross_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown2054(1)
        GFX_2('kymef430_Charge')
        sendToLabelUpon(32, 0)
    sprite('null', 100)
    label(0)
    sprite('null', 10)
    Unknown4007(0)
    Unknown3004(-25)

@State
def kym430_Ground_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4054(11)
        Unknown23067('kymef430_ChargeGround')
        Unknown1096(1500)
        teleportRelativeX(-22000)
        sendToLabelUpon(32, 0)
    sprite('null', 100)
    GFX_0('kym430_GroundWind_Eff', 100)
    label(0)
    sprite('null', 10)
    Unknown3004(-16)

@State
def kym430_GroundWind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown2054(1)
        Unknown1007(-7000)
    label(0)
    sprite('null', 10)
    GFX_0('kym430_GroundWind00_Eff', 100)
    gotoLabel(0)

@State
def kym430_GroundWind00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_GroundWind.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1096(400)
        Unknown1102(0, 200)
        Unknown3001(192)
    sprite('null', 30)
    Unknown1103(50, 67)
    Unknown3004(-12)

@State
def kym430_ChargeAir_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown2054(1)
    sprite('null', 3)
    GFX_0('kym430_Air00_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air04a_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air01_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air03a_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air02_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air02a_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air03_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air01a_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air04_Eff', 100)
    sprite('null', 3)
    GFX_0('kym430_Air00a_Eff', 100)

@State
def kym430_Air00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1072(-30000)
        Unknown1096(900)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(900)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air02_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1072(-30000)
        Unknown1096(900)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air03_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(900)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air04_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air04.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(900)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air00a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(800)
        Unknown1077(-15000, 15000)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air01a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(800)
        Unknown1077(-15000, 15000)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air02a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(800)
        Unknown1072(-60000)
        Unknown1077(-15000, 15000)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air03a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(800)
        Unknown1077(-15000, 15000)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_Air04a_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2054(1)
        Unknown4003('kymef_430_Air04.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(100)
        Unknown3013(150)
        Unknown1096(800)
        Unknown1077(-15000, 15000)
    sprite('null', 16)
    sprite('null', 7)
    Unknown3010(20)
    Unknown3016(14)

@State
def kym430_ShotMuzzle_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-85000)
    sprite('null', 1)
    GFX_1('kymef430_Muzzleflash05', 100)

@State
def kym430_ShotBlast_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_430_Exicewind00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(240)
        Unknown3005(-15)
        teleportRelativeX(125000)
        physicsXImpulse(-20000)
        Unknown1064(7225)
        Unknown1056(17000)
        Unknown1099(500)
    sprite('null', 15)
    GFX_1('kymef430_ShotSmoke', 100)

@State
def kym430_IceCreate_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_430_Exicemake00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(700)
        Unknown1064(750)
        teleportRelativeX(300000)
        Unknown1007(155000)
        Unknown1007(60000)
        Unknown1099(25)
        sendToLabelUpon(32, 0)
    sprite('null', 23)
    GFX_0('kym430_ChargeCross_Eff', 100)
    GFX_1('kymef430_createice04', 100)
    SFX_3('kymse_21')
    SFX_3('kymse_20')
    sprite('null', 23)
    Unknown4003('kymef_430_Exicemake01.DIG', '')
    GFX_1('kymef430_createice03', 100)
    sprite('null', 23)
    Unknown4003('kymef_430_Exicemake02.DIG', '')
    GFX_1('kymef430_createice03', 100)
    sprite('null', 13)
    Unknown4003('kymef_430_Exiceshot.DIG', '')
    GFX_1('kymef430_createice03', 100)
    sprite('null', 15)
    Unknown1099(0)
    Unknown1056(2750)
    Unknown1064(2950)
    Unknown3001(0)

@State
def kym430_Ice_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_430_Exiceshot.DIG', '')
        Unknown4015()
        Unknown3032()
        GFX_2('kymef430_icebloom')
        Unknown1056(2750)
        Unknown1064(2950)
        teleportRelativeX(30000)
        sendToLabelUpon(54, 1)
    SFX_3('kymse_22')
    sprite('null', 2)
    GFX_0('kym430_Icewave_Eff', 100)
    GFX_0('kym430_Icewave2_Eff', 100)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    sprite('null', 2)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    sprite('null', 2)
    GFX_0('kym430_Icewave_Eff', 100)
    GFX_0('kym430_Icewave2_Eff', 100)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    sprite('null', 2)
    GFX_0('kym430_Icewave_sml_Eff', 100)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    label(0)
    sprite('null', 2)
    GFX_0('kym430_Icewave_Eff', 100)
    GFX_0('kym430_Icewave2_Eff', 100)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    GFX_0('kym430_Icefloor_Eff', 100)
    GFX_0('kym430_IcefloorWind_Eff', 100)
    sprite('null', 2)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    GFX_0('kym430_IcefloorWind_Eff', 100)
    sprite('null', 2)
    GFX_0('kym430_Icewave_Eff', 100)
    GFX_0('kym430_Icewave2_Eff', 100)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    GFX_0('kym430_Icefloor_Eff', 100)
    GFX_0('kym430_IcefloorWind_Eff', 100)
    sprite('null', 2)
    GFX_0('kym430_Icewave_sml_Eff', 100)
    Unknown4054(6)
    Unknown4045('kymef430_grainice', 100)
    GFX_0('kym430_IcefloorWind_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 10)

@State
def kym430_Icewave_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('kymef_430_Exicewave00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1062(1800, 2800)
        Unknown1070(2000, 3000)
        Unknown3001(140)
        Unknown3005(-20)
    sprite('null', 6)
    sprite('null', 2)

@State
def kym430_Icewave2_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_430_Exicewave01.DIG', '')
        Unknown3033()
        Unknown3007(52)
        Unknown3013(167)
        Unknown3019(255)
        teleportRelativeX(-20000)
        Unknown1070(500, 1300)
        physicsXImpulse(-2000)
        Unknown1056(2700)
        Unknown1103(50, 100)
        Unknown1073(-40000)
        Unknown1077(20000, -20000)
        Unknown3001(150)
    sprite('null', 11)
    sprite('null', 19)
    Unknown3004(-8)

@State
def kym430_Icewave_sml_Eff():

    def upon_IMMEDIATE():
        Unknown4003('kymef_430_Exicewave01.DIG', '')
        Unknown3033()
        Unknown3007(112)
        Unknown3013(183)
        Unknown3019(255)
        teleportRelativeX(-15000)
        Unknown1070(200, 500)
        physicsXImpulse(-2000)
        Unknown1056(1200)
        Unknown1103(30, 50)
        Unknown1073(-40000)
        Unknown1077(10000, -10000)
        Unknown3001(150)
    sprite('null', 11)
    sprite('null', 19)
    Unknown3004(-8)

@State
def kym430_Icefloor_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        teleportRelativeY(0)
    sprite('null', 1)
    Unknown4054(11)
    Unknown4045('kymef202_icefloor', 100)

@State
def kym430_IcefloorWind_Eff():

    def upon_IMMEDIATE():
        teleportRelativeY(0)
    sprite('null', 5)
    GFX_1('kymef403_longfoot02', 100)
    sprite('null', 3)
    GFX_1('kymef430_longfoot02', 100)
    sprite('null', 1)
    GFX_1('kymef430_longfoot02', 100)

@State
def kym431_IceStorm_A_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    label(0)
    sprite('null', 15)
    SFX_3('kymse_23')
    GFX_0('kym431_IceStorm_A00_Eff', 100)
    gotoLabel(0)

@State
def kym431_IceStorm_A00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 3)
    GFX_0('kym431_Wind02_1_Eff', 100)
    GFX_0('kym431_Wind03_1_Eff', 100)
    GFX_0('kym431_BlueWind02_Eff', 100)
    GFX_0('kym431_Snow02_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_Wind02_2_Eff', 100)
    GFX_0('kym431_Wind04_1_Eff', 100)
    GFX_0('kym431_BlueWind00_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_Dust00_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_Wind02_3_Eff', 100)
    GFX_0('kym431_Wind03_2_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_Snow03_Eff', 100)
    GFX_0('kym431_Wind04_2_Eff', 100)
    GFX_0('kym431_BlueWind01_Eff', 100)
    sprite('null', 100)

@State
def kym431_IceStorm_B_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    label(0)
    sprite('null', 10)
    GFX_0('kym431_IceStorm_B00_Eff', 100)
    sprite('null', 20)
    GFX_0('kym431_IceStorm_B01_Eff', 100)
    gotoLabel(0)

@State
def kym431_IceStorm_B00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 2)
    GFX_0('kym431_Wind00_1_Eff', 100)
    sprite('null', 3)
    sprite('null', 2)
    GFX_0('kym431_Wind00_3_Eff', 100)
    sprite('null', 3)
    sprite('null', 2)
    GFX_0('kym431_Wind00_2_Eff', 100)
    sprite('null', 3)
    GFX_0('kym431_Dust01_Eff', 100)
    sprite('null', 100)

@State
def kym431_IceStorm_B01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 2)
    GFX_0('kym431_Snow00_Eff', 100)
    sprite('null', 3)
    GFX_0('kym431_Wind01_1_Eff', 100)
    sprite('null', 2)
    sprite('null', 3)
    GFX_0('kym431_Wind00_4_Eff', 100)
    sprite('null', 2)
    sprite('null', 3)
    GFX_0('kym431_Wind01_2_Eff', 100)
    GFX_0('kym431_Snow01_Eff', 100)
    sprite('null', 100)

@State
def kym431_Ground_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        GFX_2('kymef431_Circle')
        GFX_0('kym431_Back_Eff', 100)
    label(0)
    sprite('null', 10)
    GFX_0('kym431_GroundWave_Eff', 100)
    GFX_0('kym431_GroundLight_Eff', 100)
    gotoLabel(0)

@State
def kym431_GroundWave_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Shock.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(210)
        Unknown3007(135)
        Unknown3013(200)
        Unknown3019(255)
        teleportRelativeY(-70000)
        Unknown1056(800)
        Unknown1064(700)
    sprite('null', 8)
    physicsYImpulse(2500)
    Unknown1059(90)
    Unknown1067(35)
    sprite('null', 10)
    physicsYImpulse(1500)
    Unknown1059(35)
    Unknown1067(17)
    Unknown3011(-17)
    Unknown3017(-12)
    Unknown3023(-6)
    Unknown3005(-12)

@State
def kym431_GroundLight_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 20)
    GFX_2('kymef431_GroundLight')

@State
def kym431_Back_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(3)
        Unknown4003('kymef_431_Back', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(0)
        Unknown1007(-120000)
        Unknown1056(2000)
        Unknown1064(2600)
    sprite('null', 7)
    Unknown3005(36)
    sprite('null', 90)
    sprite('null', 20)
    Unknown3005(-12)

@State
def kym431_IceParticle_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
    label(0)
    sprite('null', 17)
    GFX_0('kym431_IceParticle00_Eff', 100)
    gotoLabel(0)

@State
def kym431_IceParticle00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
    sprite('null', 3)
    sprite('vr_kymef431_00', 1)
    GFX_1('kymef431_Ice', 0)
    GFX_1('kymef431_Ice', 3)
    GFX_1('kymef431_Ice', 9)
    sprite('vr_kymef431_00', 2)
    GFX_1('kymef431_Ice', 1)
    GFX_1('kymef431_Ice', 4)
    GFX_1('kymef431_Ice', 6)
    GFX_1('kymef431_Ice', 10)
    sprite('vr_kymef431_00', 1)
    GFX_1('kymef431_Ice', 2)
    GFX_1('kymef431_Ice', 5)
    GFX_1('kymef431_Ice', 7)
    GFX_1('kymef431_Ice', 11)
    sprite('vr_kymef431_00', 2)
    GFX_1('kymef431_Ice', 8)
    GFX_1('kymef431_Ice', 12)
    sprite('vr_kymef431_00', 15)
    GFX_1('kymef431_Ice', 13)

@State
def kym431_End_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 100)
    SFX_3('kymse_24')
    GFX_0('kym431_EndWind_Eff', 100)
    GFX_0('kym431_IceStormEnd_Eff', 100)
    GFX_0('kym431_IceParticleEnd_Eff', 100)
    GFX_1('kymef431_LightVanish00', 100)

@State
def kym431_EndWind_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
    sprite('null', 1)
    GFX_0('kym431_EndWind05_Eff', 100)
    sprite('null', 1)
    GFX_0('kym431_EndWind06_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_EndWind00_Eff', 100)
    sprite('null', 1)
    GFX_0('kym431_EndWind01_Eff', 100)
    GFX_0('kym431_EndWind02_Eff', 100)
    sprite('null', 3)
    GFX_0('kym431_EndWind03_Eff', 100)
    sprite('null', 1)
    GFX_0('kym431_EndWind04_Eff', 100)
    sprite('null', 100)

@State
def kym431_IceStormEnd_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 1)
    GFX_0('kym431_WindEnd00_Eff', 100)
    GFX_0('kym431_BlueWind02_Eff', 100)
    GFX_0('kym431_Snow02_Eff', 100)
    GFX_0('kym431_SnowEnd03_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_SnowEnd00_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_WindEnd01_Eff', 100)
    GFX_0('kym431_BlueWind00_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_Dust00_Eff', 100)
    sprite('null', 1)
    GFX_0('kym431_WindEnd02_Eff', 100)
    sprite('null', 1)
    GFX_0('kym431_SnowEnd02_Eff', 100)
    sprite('null', 2)
    GFX_0('kym431_WindEnd03_Eff', 100)
    GFX_0('kym431_BlueWind01_Eff', 100)
    sprite('null', 100)

@State
def kym431_IceParticleEnd_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
    sprite('vr_kymef431_01', 2)
    GFX_1('kymef431_Cross', 1)
    GFX_1('kymef431_Cross', 2)
    sprite('vr_kymef431_01', 1)
    GFX_1('kymef431_Cross', 0)
    sprite('vr_kymef431_01', 2)
    GFX_1('kymef431_Cross', 1)
    sprite('vr_kymef431_01', 2)
    GFX_1('kymef431_Cross', 0)
    GFX_1('kymef431_Cross', 2)

@State
def kym431_Wind00_1_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_274_Wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-80000)
        Unknown1007(50000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(500)
        Unknown1064(500)
        Unknown1062(-100, 100)
        Unknown1070(-100, 100)
        Unknown1077(-8000, 8000)
    sprite('null', 15)
    Unknown3001(255)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Wind00_2_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(40000)
        Unknown1007(415000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(850)
        Unknown1064(400)
        Unknown1062(-100, 100)
        Unknown1070(-100, 100)
        Unknown1073(-17500)
        Unknown1077(-5000, 5000)
    sprite('null', 15)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Wind00_3_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown2005()
        Unknown4009(2)
        Unknown4003('kymef_431_Wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(0)
        Unknown1007(50000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(550)
        Unknown1064(300)
        Unknown1062(-100, 100)
        Unknown1070(-100, 100)
        Unknown1077(-8000, 8000)
    sprite('null', 15)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Wind00_4_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(0)
        Unknown1007(220000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(650)
        Unknown1064(600)
        Unknown1062(-100, 100)
        Unknown1070(-100, 100)
        Unknown1077(-8000, 8000)
    sprite('null', 15)
    Unknown3001(255)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Wind01_1_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(925)
        Unknown1064(750)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        teleportRelativeX(-75000)
        Unknown1007(370000)
        Unknown1062(-100, 100)
        Unknown1070(-100, 100)
        Unknown1073(-15000)
        Unknown1077(-5000, 20000)
    sprite('null', 15)
    Unknown3001(255)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Wind01_2_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind01.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-32500)
        Unknown1007(220000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(900)
        Unknown1064(750)
        Unknown1062(-100, 100)
        Unknown1070(-100, 100)
        Unknown1073(-6000)
        Unknown1077(-5000, 5000)
    sprite('null', 15)
    Unknown3001(255)
    sprite('null', 8)
    Unknown3004(-25)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Wind02_1_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(-70000)
        Unknown1007(250000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(570)
        Unknown1064(350)
        Unknown1062(-100, 100)
        Unknown1070(-200, 200)
        Unknown1072(-18000)
        Unknown1077(-20000, 20000)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_Wind02_2_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(-120000)
        Unknown1007(485000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(1175)
        Unknown1064(625)
        Unknown1062(-120, 100)
        Unknown1070(-200, 120)
        Unknown1072(0)
        Unknown1077(-10000, 10000)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_Wind02_3_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(-120000)
        Unknown1007(125000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(500)
        Unknown1064(300)
        Unknown1062(-200, 200)
        Unknown1070(-100, 200)
        Unknown1072(14000)
        Unknown1077(-10000, 10000)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_Wind03_1_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(160)
        Unknown3013(200)
        Unknown3019(255)
        teleportRelativeX(40000)
        Unknown1007(125000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(900)
        Unknown1064(450)
        Unknown1062(-100, 200)
        Unknown1070(-100, 50)
        Unknown1072(-14500)
        Unknown1077(-5000, 5000)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_Wind03_2_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(160)
        Unknown3013(200)
        Unknown3019(255)
        teleportRelativeX(140000)
        Unknown1007(275000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 45000)
        Unknown1056(900)
        Unknown1064(520)
        Unknown1062(-250, 100)
        Unknown1070(-150, 100)
        Unknown1072(-10000)
        Unknown1077(-2500, 2500)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_Wind04_1_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind04.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(160)
        Unknown3013(200)
        Unknown3019(255)
        teleportRelativeX(135000)
        Unknown1007(185000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(1100)
        Unknown1064(450)
        Unknown1062(-200, 200)
        Unknown1070(-100, 50)
        Unknown1072(-18000)
        Unknown1077(-5000, 5000)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_Wind04_2_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4003('kymef_431_Wind04.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(160)
        Unknown3013(200)
        Unknown3019(255)
        teleportRelativeX(85000)
        Unknown1007(400000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(1135)
        Unknown1064(630)
        Unknown1062(-150, 125)
        Unknown1070(-100, 50)
        Unknown1072(-18000)
        Unknown1077(-5000, 5000)
    sprite('null', 9)
    sprite('null', 8)
    Unknown3005(-25)

@State
def kym431_BlueWind00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(40)
        Unknown3013(115)
        Unknown3019(180)
        teleportRelativeX(-70000)
        Unknown1007(75000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 90000)
        Unknown1056(950)
        Unknown1064(350)
        Unknown1062(-100, 100)
        Unknown1070(-200, 200)
        Unknown1072(0)
        Unknown1077(-10000, 10000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3005(-25)

@State
def kym431_BlueWind01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(40)
        Unknown3013(115)
        Unknown3019(180)
        teleportRelativeX(-30000)
        Unknown1007(180000)
        Unknown1010(-20000, 20000)
        Unknown1011(-55000, 120000)
        Unknown1056(1000)
        Unknown1064(425)
        Unknown1062(-100, 100)
        Unknown1070(-200, 200)
        Unknown1072(0)
        Unknown1077(-10000, 10000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3005(-25)

@State
def kym431_BlueWind02_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(20)
        Unknown3013(120)
        Unknown3019(175)
        teleportRelativeX(-80000)
        Unknown1007(320000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 135000)
        Unknown1056(1250)
        Unknown1064(400)
        Unknown1062(-100, 100)
        Unknown1070(-200, 200)
        Unknown1072(0)
        Unknown1077(-10000, 10000)
    sprite('null', 10)
    sprite('null', 10)
    Unknown3005(-25)

@State
def kym431_WindEnd00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(-70000)
        Unknown1007(250000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(350)
        Unknown1064(350)
        Unknown1062(-100, 100)
        Unknown1070(-200, 200)
        Unknown1072(-18000)
        Unknown1077(-20000, 20000)
    sprite('null', 9)
    Unknown1060(40)
    sprite('null', 8)
    Unknown3005(-25)
    Unknown1060(20)

@State
def kym431_WindEnd01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(0)
        Unknown1007(365000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1057(-400)
        Unknown1065(-550)
        Unknown1062(-120, 100)
        Unknown1070(-200, 120)
        Unknown1072(-10000)
        Unknown1077(-20000, 20000)
    sprite('null', 9)
    Unknown1060(40)
    sprite('null', 8)
    Unknown3005(-25)
    Unknown1060(20)

@State
def kym431_WindEnd02_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(0)
        Unknown1007(95000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(145)
        Unknown1064(200)
        Unknown1062(-200, 200)
        Unknown1070(-100, 200)
        Unknown1072(-7000)
        Unknown1077(-2000, 2000)
    sprite('null', 9)
    Unknown1060(40)
    sprite('null', 8)
    Unknown3005(-25)
    Unknown1060(20)

@State
def kym431_WindEnd03_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_Wind02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(200)
        Unknown3013(240)
        Unknown3019(255)
        teleportRelativeX(0)
        Unknown1007(400000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(300)
        Unknown1064(300)
        Unknown1062(-200, 200)
        Unknown1070(-100, 200)
        Unknown1072(7000)
        Unknown1077(-2000, 2000)
    sprite('null', 9)
    Unknown1060(40)
    sprite('null', 8)
    Unknown3005(-25)
    Unknown1060(20)

@State
def kym431_Snow00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Snow.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(60000)
        Unknown1007(-8000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(975)
        Unknown1064(250)
        Unknown1062(-100, 100)
        Unknown1070(0, 100)
        Unknown1072(-7000)
        Unknown1077(-2000, 2000)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Snow01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Snow.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(60000)
        Unknown1007(220000)
        Unknown1010(-20000, 20000)
        Unknown1011(-50000, 40000)
        Unknown1056(1125)
        Unknown1064(300)
        Unknown1062(-100, 100)
        Unknown1070(0, 100)
        Unknown1072(-7000)
        Unknown1077(-2500, 2500)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Snow02_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Snow.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(60000)
        Unknown1007(300000)
        Unknown1010(-20000, 20000)
        Unknown1011(-65000, 65000)
        Unknown1056(1055)
        Unknown1064(200)
        Unknown1062(-250, 0)
        Unknown1070(0, 100)
        Unknown1072(-11000)
        Unknown1077(-2000, 2000)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Snow03_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Snow.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(60000)
        Unknown1007(100000)
        Unknown1010(-20000, 20000)
        Unknown1011(-65000, 65000)
        Unknown1056(875)
        Unknown1064(200)
        Unknown1062(-150, 0)
        Unknown1070(0, 100)
        Unknown1072(-12000)
        Unknown1077(-2000, 2000)
    sprite('null', 25)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_SnowEnd00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_SnowEnd.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(100000)
        Unknown1007(90000)
        Unknown1010(-20000, 20000)
        Unknown1011(-25000, 65000)
        Unknown1056(900)
        Unknown1064(550)
        Unknown1062(-70, 35)
        Unknown1070(0, 100)
        Unknown1072(-25000)
        Unknown1077(-5000, 8000)
    sprite('null', 13)
    Unknown3001(255)
    sprite('null', 10)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_SnowEnd01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_SnowEnd.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-100000)
        Unknown1007(250000)
        Unknown1010(-20000, 20000)
        Unknown1011(-25000, 65000)
        Unknown1056(1000)
        Unknown1064(550)
        Unknown1062(-70, 35)
        Unknown1070(0, 100)
        Unknown1072(-18000)
        Unknown1077(-5000, 8000)
    sprite('null', 10)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_SnowEnd02_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_SnowEnd.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(0)
        Unknown1007(0)
        Unknown1010(-20000, 20000)
        Unknown1011(-25000, 65000)
        Unknown1056(400)
        Unknown1064(400)
        Unknown1062(-70, 35)
        Unknown1070(0, 50)
        Unknown1072(-9000)
        Unknown1077(-5000, 8000)
    sprite('null', 15)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_SnowEnd03_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Snow.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(0)
        Unknown1007(300000)
        Unknown1010(-20000, 20000)
        Unknown1011(-65000, 65000)
        Unknown1056(800)
        Unknown1064(350)
        Unknown1062(-250, 0)
        Unknown1070(0, 100)
        Unknown1072(0)
        Unknown1077(-16000, 8000)
    sprite('null', 15)
    Unknown3001(255)
    sprite('null', 15)
    Unknown3004(-17)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Dust00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Dust.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(0)
        Unknown1007(-45000)
        Unknown1010(-20000, 20000)
        Unknown1011(-20000, 20000)
        Unknown1056(600)
        Unknown1064(450)
        Unknown1062(-100, 100)
        Unknown1070(0, 100)
    sprite('null', 20)
    Unknown3001(255)
    sprite('null', 5)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_Dust01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_Dust.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-60000)
        Unknown1007(150000)
        Unknown1010(-50000, 50000)
        Unknown1011(-20000, 80000)
        Unknown1056(850)
        Unknown1064(525)
        Unknown1062(-100, 100)
        Unknown1070(0, 100)
        Unknown1077(-16000, 0)
    sprite('null', 20)
    Unknown3001(255)
    sprite('null', 5)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_EndWind00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_431_EndWind00.DIG', '')
        Unknown4015()
        Unknown23015(12)
        Unknown3033()
    sprite('null', 12)
    sprite('null', 13)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_EndWind01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_431_EndWind01.DIG', '')
        Unknown4015()
        Unknown23015(12)
        Unknown3033()
        teleportRelativeX(150000)
    sprite('null', 12)
    sprite('null', 13)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_EndWind02_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_431_EndWind02.DIG', '')
        Unknown4015()
        Unknown3033()
    sprite('null', 12)
    sprite('null', 13)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_EndWind03_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown4003('kymef_431_EndWind03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(80000)
        Unknown1056(1100)
        Unknown1064(1300)
    sprite('null', 12)
    Unknown3007(175)
    Unknown3013(220)
    sprite('null', 12)
    Unknown3010(-20)
    Unknown3016(-14)

@State
def kym431_EndWind04_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(3)
        Unknown2005()
        Unknown4003('kymef_431_EndWind03.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(80000)
        Unknown1056(1100)
        Unknown1064(1300)
    sprite('null', 12)
    Unknown3001(200)
    Unknown3007(70)
    Unknown3013(120)
    sprite('null', 12)
    Unknown3010(-5)
    Unknown3016(-8)

@State
def kym431_EndWind05_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4003('kymef_431_EndWind04.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(70000)
        Unknown1096(750)
        Unknown1100(20)
        Unknown1073(6000)
    sprite('null', 30)
    Unknown3010(-8)
    Unknown3016(-4)
    Unknown3004(-8)

@State
def kym431_EndWind06_Eff():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown2005()
        Unknown4003('kymef_431_EndWind04.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1007(70000)
        Unknown1096(875)
        Unknown1100(20)
        Unknown1073(9000)
    sprite('null', 30)
    Unknown3010(-8)
    Unknown3016(-4)
    Unknown3004(-8)

@State
def kym450_Tornado_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        loopRelated(17, 32)

        def upon_17():
            sendToLabel(9)
            clearUponHandler(17)
            Unknown21012('kym450_Tornado01_Eff', 32)
            Unknown21012('kym450_Tornado03_Eff', 32)
    sprite('kymef450_TornadoPosition', 1)
    GFX_0('kym450_TornadoBloom_Eff', -1)
    SFX_3('kymse_24')
    SFX_3('kymse_25')
    sprite('keep', 3)
    GFX_0('kym450_Tornado01_Eff', 1)
    Unknown36(1)
    Unknown1097(-300)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 3)
    Unknown36(1)
    Unknown1097(-600)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 7)
    Unknown36(1)
    Unknown1097(-500)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 10)
    Unknown36(1)
    Unknown1097(-200)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 13)
    Unknown36(1)
    Unknown1097(-600)
    Unknown35()
    GFX_0('kym450_Tornado02_Eff', 5)
    GFX_0('kym450_Tornado02_Eff', 13)
    Unknown36(1)
    Unknown1097(-500)
    Unknown35()
    label(0)
    sprite('keep', 2)
    GFX_1('kymef_450_tornado', -1)
    GFX_0('kym450_Tornado01_Eff', 0)
    Unknown36(1)
    Unknown1097(400)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 6)
    GFX_0('kym450_Tornado01_Eff', 16)
    Unknown36(1)
    Unknown1097(0)
    Unknown35()
    GFX_0('kym450_Tornado03_Eff', 6)
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 1)
    Unknown36(1)
    Unknown1097(700)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 11)
    Unknown36(1)
    Unknown1097(-300)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 7)
    Unknown36(1)
    Unknown1097(-500)
    Unknown35()
    GFX_0('kym450_Tornado03_Eff', 19)
    GFX_0('kym450_Tornado02_Eff', 3)
    Unknown36(1)
    Unknown1097(-500)
    Unknown35()
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 3)
    GFX_0('kym450_Tornado01_Eff', 12)
    Unknown36(1)
    Unknown1097(-500)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 18)
    Unknown36(1)
    Unknown1097(500)
    Unknown35()
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 14)
    Unknown36(1)
    Unknown1097(100)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 20)
    Unknown36(1)
    Unknown1097(300)
    Unknown35()
    GFX_0('kym450_Tornado03_Eff', 12)
    Unknown36(1)
    Unknown1097(-300)
    Unknown35()
    gotoLabel(0)
    label(9)
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 0)
    Unknown36(1)
    Unknown1097(300)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 16)
    Unknown36(1)
    Unknown1097(0)
    Unknown35()
    GFX_0('kym450_Tornado03_Eff', 6)
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 1)
    Unknown36(1)
    Unknown1097(350)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 7)
    Unknown36(1)
    Unknown1097(-300)
    Unknown35()
    GFX_0('kym450_Tornado03_Eff', 19)
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 3)
    Unknown36(1)
    Unknown1097(0)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 12)
    Unknown36(1)
    Unknown1097(-300)
    Unknown35()
    sprite('keep', 2)
    GFX_0('kym450_Tornado01_Eff', 14)
    Unknown36(1)
    Unknown1097(100)
    Unknown35()
    GFX_0('kym450_Tornado01_Eff', 20)
    Unknown36(1)
    Unknown1097(700)
    Unknown35()
    GFX_0('kym450_Tornado03_Eff', 12)

@State
def kym450_Tornado01_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown4009(2)
        Unknown3033()
        Unknown1010(30000, -30000)
        Unknown1011(30000, -30000)
        Unknown1026(0, 5000)
        Unknown1102(900, 100)
        Unknown1090(50)
        Unknown1100(20)
        Unknown1092(10)
        Unknown1077(-20000, -5000)
        Unknown3007(200)
        Unknown3013(230)
        Unknown3010(-10)
        Unknown3016(-5)

        def upon_32():
            Unknown1099(100)
            Unknown1069(50)
            clearUponHandler(32)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(1)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(2)
    label(0)
    sprite('null', 12)
    Unknown4003('kymef_450_wind01', '')
    Unknown3004(-19)
    ExitState()
    label(1)
    sprite('null', 14)
    Unknown4003('kymef_450_wind02', '')
    Unknown3004(-17)
    ExitState()
    label(2)
    sprite('null', 13)
    Unknown4003('kymef_450_wind03', '')
    Unknown3004(-18)

@State
def kym450_Tornado02_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown3033()
        Unknown1096(1500)
        Unknown1090(50)
        Unknown1099(20)
        Unknown1091(10)
        Unknown1077(-20000, -5000)
        Unknown1026(0, 5000)
        Unknown3007(200)
        Unknown3013(230)
        Unknown3010(-10)
        Unknown3016(-5)
    sprite('null', 12)
    Unknown4003('kymef_450_wind04', '')
    Unknown3004(-19)

@State
def kym450_Tornado03_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
        Unknown1096(1500)
        Unknown1102(800, -400)
        Unknown3032()
        Unknown1072(-15000)
        Unknown1077(-3000, 3000)
        Unknown1010(30000, -30000)
        Unknown1011(30000, -30000)
        Unknown1026(0, 5000)
        Unknown1090(50)
        Unknown1100(20)
        Unknown1092(10)
        Unknown23118(8256)

        def upon_32():
            Unknown1099(100)
            Unknown1069(50)
            clearUponHandler(32)
    sprite('null', 14)
    Unknown4003('kymef_450_wind05', '')
    Unknown3004(-17)

@State
def kym450_TornadoBloom_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 40)
    Unknown4054(11)
    Unknown23067('kymef_450_bloom')
    sprite('null', 20)
    Unknown3004(-12)

@State
def kym450_Screen_Eff():

    def upon_IMMEDIATE():
        Unknown1096(3100)
        Unknown3033()
        Unknown23015(1)
        Unknown2005()

        def upon_3():
            Unknown23057(50)
            Unknown23058(50)
        Unknown3001(64)
        Unknown3004(4)
        Unknown3007(128)
        Unknown3013(162)
        Unknown3010(2)
        Unknown3016(3)
    sprite('null', 4)
    sprite('null', 40)
    Unknown4003('kymef_450_screenbase01', '')

@Subroutine
def kym450_BG_Ice_Func():
    Unknown4010(2)
    Unknown4011(2)
    Unknown21010(1)
    Unknown2054(1)
    Unknown3032()
    teleportRelativeY(0)
    Unknown1000(0)

    def upon_32():
        Unknown13(25)
        Unknown4003('', '')

@State
def kym450_BG_Ice00_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_BG_Ice_Func')
        Unknown4003('kymef_450_bgice00.DIG', '')
        Unknown23015(3)
    sprite('null', 200)
    sprite('null', 32767)

@State
def kym450_BG_Ice01_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_BG_Ice_Func')
        Unknown4003('kymef_450_bgice01.DIG', '')
    sprite('null', 32767)

@State
def kym450_BG_Ice02_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_BG_Ice_Func')
        Unknown4003('kymef_450_bgice02.DIG', '')
    sprite('null', 32767)

@State
def kym450_BG_Ice03_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_BG_Ice_Func')
        Unknown4003('kymef_450_bgice03.DIG', '')
    sprite('null', 32767)

@State
def kym450_BG_Ice04_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_BG_Ice_Func')
        Unknown4003('kymef_450_bgice04.DIG', '')
    sprite('null', 32767)

@State
def kym450_Breath_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown1007(-1000)
    sprite('null', 60)
    sprite('null', 1)
    GFX_1('kymef450_Breath', 0)

@State
def kym450_Ice01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown1000(0)
        teleportRelativeY(0)
        teleportRelativeX(30000)
        Unknown1007(200000)
        Unknown19001(-20000)
        Unknown3032()
        Unknown4003('kymef_450_ice01', '')
        Unknown4054(1)
        Unknown4045('kymef_450_hit', -1)
        ScreenShake(0, 7500)
    sprite('null', 2)
    Unknown1096(800)
    Unknown1090(30)
    Unknown23118(-8323073)
    sprite('null', 2)
    Unknown1096(920)
    Unknown1090(30)
    Unknown23102(-32)
    Unknown23108(-32)
    Unknown23114(-16)
    sprite('null', 100)
    Unknown1096(1000)
    Unknown1090(30)

@State
def kym450_Ice02_Eff():

    def upon_IMMEDIATE():
        Unknown4007(22)
        Unknown1096(1150)
        Unknown1090(50)
        Unknown1000(0)
        teleportRelativeY(0)
        Unknown3032()
        Unknown4003('kymef_450_ice02', '')
    sprite('null', 600)

@State
def kym450_Speed_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown2055(24)
        Unknown2005()
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
    label(0)
    sprite('null', 5)
    GFX_0('kym450_Speed1_Eff', -1)
    GFX_0('kym450_Speed2_Eff', -1)
    gotoLabel(0)

@State
def kym450_Speed1_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown6001(1)
        Unknown23033(15)
    sprite('null', 1)
    GFX_1('kymef450_speed', -1)

@State
def kym450_Speed2_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4010(2)
        Unknown4011(2)
        Unknown6001(1)
        Unknown23033(95)
    sprite('null', 1)
    GFX_1('kymef450_speed', -1)

@State
def kym450_Dash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown2055(600)

        def upon_32():
            sendToLabel(0)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(3)
    label(99)
    sprite('null', 1)
    GFX_1('kymef450_DriftSmoke', -1)
    SFX_3('kymse_04')
    sprite('null', 1)
    GFX_1('kymef450_DriftSmoke', -1)
    sprite('null', 1)
    GFX_1('kymef450_DriftSmoke', -1)
    sprite('null', 1)
    GFX_1('kymef450_DriftSmoke', -1)
    sprite('null', 1)
    GFX_1('kymef450_DriftSmoke', -1)
    gotoLabel(99)
    label(0)
    sprite('null', 5)
    GFX_1('kymef450_DriftSmoke_R', -1)
    SFX_3('kymse_04')
    gotoLabel(0)
    label(1)
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_R', -1)
    SFX_3('kymse_04')
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_R', -1)
    sprite('null', 4)
    SFX_3('kymse_04')
    sprite('null', 4)
    sprite('null', 4)
    SFX_3('kymse_04')
    GFX_1('kymef450_DriftSmoke_L', -1)
    label(2)
    sprite('null', 5)
    GFX_1('kymef450_DriftSmoke_L', -1)
    SFX_3('kymse_04')
    gotoLabel(2)
    label(3)
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_L', -1)
    SFX_3('kymse_04')
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_L', -1)
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_L', -1)
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_L', -1)
    sprite('null', 4)
    GFX_1('kymef450_DriftSmoke_R', -1)
    label(4)
    sprite('null', 5)
    GFX_1('kymef450_DriftSmoke_R', -1)
    gotoLabel(4)

@State
def kym450_Dash2_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown4007(2)
        Unknown2055(600)
        Unknown1007(-10000)

        def upon_33():
            sendToLabel(1)

        def upon_34():
            sendToLabel(2)
    sprite('null', 32767)
    Unknown23067('kymef450_DriftFoot_R')
    label(1)
    sprite('null', 32767)
    GFX_2('')
    Unknown4054(1)
    Unknown23067('kymef450_DriftFoot_L')
    label(2)
    sprite('null', 32767)
    GFX_2('')
    Unknown4054(1)
    Unknown23067('kymef450_DriftFoot_R')

@State
def kym450_Slash01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown23015(3)
        Unknown4010(2)
        Unknown4011(2)
        Unknown4061(1)
        Unknown1000(20000)
        teleportRelativeY(185000)
    sprite('kymef450_slash01', 8)
    GFX_0('kym450_Hit00_Eff', -1)
    Unknown36(1)
    Unknown1073(10000)
    teleportRelativeX(-300000)
    Unknown35()
    ScreenShake(5000, 5000)
    GFX_0('kym450_Hit01_Eff', -1)
    Unknown36(1)
    Unknown1073(10000)
    teleportRelativeX(-300000)
    Unknown35()
    ScreenShake(5000, 5000)
    sprite('kymef450_slash02', 6)
    sprite('kymef450_slash03', 6)
    sprite('kymef450_slash04', 6)
    sprite('kymef450_slash05', 4)
    sprite('kymef450_slash06', 4)

@State
def kym450_Slash02_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown23015(3)
        Unknown2054(1)
        Unknown21010(1)
        Unknown4061(1)
        Unknown1000(-3000)
        teleportRelativeY(215000)
    sprite('kymef450_slash07', 20)
    GFX_0('kym450_IceBreak01_Eff', -1)
    GFX_0('kym450_Hit02_Eff', -1)
    Unknown36(1)
    Unknown1073(-15000)
    teleportRelativeX(-300000)
    Unknown35()
    GFX_0('kym450_Hit03_Eff', -1)
    Unknown36(1)
    Unknown1073(-15000)
    teleportRelativeX(-300000)
    Unknown35()
    sprite('kymef450_slash08', 6)
    sprite('kymef450_slash09', 6)
    sprite('kymef450_slash10', 6)
    sprite('kymef450_slash11', 6)
    sprite('kymef450_slash12', 6)

@State
def kym450_Hit00_Eff():

    def upon_IMMEDIATE():
        Unknown1056(1000)
        Unknown1064(1000)
        Unknown4003('kymef_450_Asslash00.DIG', '')
        Unknown3032()
    sprite('null', 4)
    sprite('null', 16)
    Unknown4009(0)
    loopRest()

@State
def kym450_Hit01_Eff():

    def upon_IMMEDIATE():
        Unknown1056(1000)
        Unknown1064(1000)
        Unknown4003('kymef_450_Asslash01.DIG', '')
        Unknown3033()
    sprite('null', 4)
    GFX_2('kymef450_SlashHit')
    sprite('null', 16)
    loopRest()

@State
def kym450_Hit02_Eff():

    def upon_IMMEDIATE():
        Unknown1056(1000)
        Unknown1064(1750)
        Unknown4003('kymef_450_Asslash02.DIG', '')
        Unknown3032()
    sprite('null', 7)
    sprite('null', 19)
    Unknown4009(0)
    Unknown1060(1000)
    loopRest()

@State
def kym450_Hit03_Eff():

    def upon_IMMEDIATE():
        Unknown1056(1000)
        Unknown1064(1750)
        Unknown4003('kymef_450_Asslash03.DIG', '')
        Unknown3033()
    sprite('null', 7)
    GFX_2('kymef450_SlashHit')
    sprite('null', 19)
    Unknown1060(1000)
    loopRest()

@State
def kym450_IceBreak01_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4011(2)
        GFX_2('kymef450_IceBreak')
        teleportRelativeY(0)
    sprite('null', 110)

@State
def kym450_IceBreak02_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4011(2)
        GFX_2('kymef450_IceBreak2')
        teleportRelativeY(0)
        Unknown6001(1)

        def upon_3():
            Unknown23032(50)
    sprite('null', 180)

@State
def kym450_cutin_SwordAura_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown23015(4)
        Unknown23032(0)
        Unknown23033(75)
        teleportRelativeX(-480000)
        Unknown1007(75000)
    sprite('null', 20)
    physicsXImpulse(3000)
    GFX_0('kym450_cutin_SAura_Eff', 100)
    GFX_0('kym450_cutin_SAuraPtcl00_Eff', 100)
    GFX_0('kym450_cutin_SAuraPtcl01_Eff', 100)
    GFX_0('kym450_cutin_SAuraPtcl02_Eff', 100)
    GFX_0('kym450_cutin_SAuraPtcl03_Eff', 100)
    sprite('null', 32767)
    Unknown1084(1)

@State
def kym450_cutin_SAura_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown2005()
        Unknown4003('kymef_450_CutIn_SAura.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown23015(4)
        Unknown1096(1050)
        teleportRelativeX(30000)
        Unknown1007(-5000)
        Unknown1072(13500)
        Unknown3001(175)
    sprite('null', 32767)

@State
def kym450_cutin_SAuraPtcl00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(160000)
        Unknown1007(20000)
        Unknown1072(7000)
        Unknown4054(4)
        Unknown23067('kymef450_CutIn_IceSmoke')
    sprite('null', 32767)

@State
def kym450_cutin_SAuraPtcl01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(-200000)
        Unknown1007(-50000)
        Unknown1072(7000)
        Unknown4054(4)
        Unknown23067('kymef450_CutIn_IceSmoke')
    sprite('null', 32767)

@State
def kym450_cutin_SAuraPtcl02_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(-80000)
        Unknown1007(20000)
        Unknown4054(4)
        Unknown23067('kymef450_CutIn_IceSmoke')
    sprite('null', 32767)

@State
def kym450_cutin_SAuraPtcl03_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        teleportRelativeX(-10000)
        Unknown1007(-40000)
        Unknown1072(-20000)
        Unknown4054(4)
        Unknown23067('kymef450_CutIn_IceSmoke')
    sprite('null', 32767)

@State
def kym450_SwoardAura10_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(50000)
    sprite('null', 32767)

@State
def kym450_SwoardAura17_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(50000)
    sprite('null', 32767)

@State
def kym450_SwoardAura18_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(55000)
    sprite('null', 32767)

@State
def kym450_SwoardAura20_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(170000)
    sprite('null', 32767)

@State
def kym450_SwoardAura21_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(230000)
    sprite('null', 32767)

@State
def kym450_SwoardAura22_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(255000)
    sprite('null', 32767)

@State
def kym450_SwoardAura23_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(260000)
    sprite('null', 32767)

@State
def kym450_SwoardAura25_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(230000)
        Unknown1064(750)
    sprite('null', 32767)

@State
def kym450_SwoardAura26_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(220000)
        Unknown1064(900)
    sprite('null', 32767)

@State
def kym450_SwoardAura28_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(115000)
    sprite('null', 32767)

@State
def kym450_SwoardAura28ex_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(95000)
    sprite('null', 32767)

@State
def kym450_SwoardAura28ex2_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc')
        Unknown1072(85000)
    sprite('null', 32767)

@State
def kym450_SwoardAura29_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(80000)
    sprite('null', 32767)

@State
def kym450_SwoardAura30_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(60000)
        Unknown1064(800)
    sprite('null', 32767)

@State
def kym450_SwoardAura31_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(75000)
        Unknown1064(950)
    sprite('null', 32767)

@State
def kym450_SwoardAura32_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(105000)
    sprite('null', 32767)

@State
def kym450_SwoardAura33_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(180000)
        Unknown1064(600)
    sprite('null', 32767)

@State
def kym450_SwoardAura34_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(300000)
        Unknown1064(500)
    sprite('null', 32767)

@State
def kym450_SwoardAura35_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(20000)
        Unknown1064(600)
    sprite('null', 32767)

@State
def kym450_SwoardAura36_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(30000)
        Unknown1064(600)
    sprite('null', 32767)

@State
def kym450_SwoardAura36ex_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(35000)
        Unknown1064(600)
    sprite('null', 32767)

@State
def kym450_SwoardAura36ex2_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(35000)
        Unknown1064(600)
    sprite('null', 32767)

@State
def kym450_SwoardAura37_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(40000)
        Unknown1064(650)
    sprite('null', 32767)

@State
def kym450_SwoardAura40_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(5000)
        Unknown1064(550)
    sprite('null', 32767)

@State
def kym450_SwoardAura41_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(30000)
        Unknown1064(650)
    sprite('null', 32767)

@State
def kym450_SwoardAura42_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(20000)
        Unknown1064(650)
    sprite('null', 32767)

@State
def kym450_SwoardAura42ex_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(330000)
        Unknown1064(450)
    sprite('null', 32767)

@State
def kym450_SwoardAura43_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(325000)
        Unknown1064(500)
    sprite('null', 32767)

@State
def kym450_SwoardAura44_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(300000)
        Unknown1064(500)
    sprite('null', 32767)

@State
def kym450_SwoardAura45_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(290000)
        Unknown1064(900)
    sprite('null', 32767)

@State
def kym450_SwoardAura45ex_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(270000)
        Unknown1064(950)
    sprite('null', 32767)

@State
def kym450_SwoardAura45ex2_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(265000)
        Unknown1064(950)
    sprite('null', 32767)

@State
def kym450_SwoardAura46_Eff():

    def upon_IMMEDIATE():
        callSubroutine('kym450_SwoardAura_Fnc2')
        Unknown1072(255000)
        Unknown1064(900)
    sprite('null', 32767)

@Subroutine
def kym450_SwoardAura_Fnc():
    Unknown4010(2)
    Unknown4011(2)
    Unknown4007(2)
    Unknown4003('kymef_450_SAura00.DIG', '')
    Unknown4015()
    Unknown3033()

@Subroutine
def kym450_SwoardAura_Fnc2():
    Unknown4010(2)
    Unknown4011(2)
    Unknown4007(2)
    Unknown4003('kymef_450_SAura00.DIG', '')
    Unknown4015()
    Unknown3033()
    Unknown23015(1)

@State
def kym450_SAuraDust_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
    label(0)
    sprite('null', 2)
    GFX_1('kymef450_SAuraDust', 100)
    gotoLabel(0)

@State
def kym450_SAuraDust2_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
    label(0)
    sprite('null', 2)
    GFX_1('kymef450_SAuraDust2', 100)
    gotoLabel(0)

@State
def kym450_SAuraDust3_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
    label(0)
    sprite('null', 5)
    GFX_1('kymef450_SAuraDust2', 100)
    gotoLabel(0)

@State
def kym601_Body_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4061(0)
        Unknown3032()
        Unknown3001(255)
    sprite('kymef601_05', 4)
    GFX_0('kym601_Flash_Eff', 100)
    Unknown23117(16777215, 9)
    sprite('kymef601_06', 5)
    sprite('kymef601_07', 5)
    sprite('kymef601_08', 4)

@State
def kym601_Flash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        teleportRelativeX(10000)
        Unknown1007(175000)
    sprite('null', 1)
    GFX_1('kymef601_flash', 100)

@State
def kym601_Particle_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
    sprite('null', 1)
    GFX_1('kymef601_petalfront', 100)
    Unknown4049(1350)
    Unknown4054(11)
    Unknown4045('kymef601_petalback', 100)
    Unknown4054(11)
    Unknown4045('kymef601_linelight', 100)
    Unknown4054(11)
    Unknown4045('kymef601_backlight', 100)
    Unknown4049(800)
    Unknown4054(11)
    Unknown4045('kymef601_Ice', 100)