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
def Land_Assault_Int():
    AttackLevel_(4)
    AttackP1(80)
    AttackP2(85)
    Hitstop(9)
    PushbackX(19800)
    AirPushbackX(20000)
    AirPushbackY(20000)
    Unknown11001(0, 0, 0)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    hitstun(24)
    AirUntechableTime(40)
    Unknown11056(0)

@Subroutine
def Air_Assault_Int():
    AttackLevel_(3)
    Damage(1700)
    AttackP1(90)
    AirHitstunAnimation(13)
    PushbackX(4800)
    Unknown11056(0)

@State
def Air_Assault_damy():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown2035(1)
        Unknown4019(2)
        Unknown2019(1)
        Unknown13044(1)
    sprite('rne406_07', 16)
    GFX_0('rne406_Kick_Eff', 100)
    sprite('rne406_07', 10)
    Unknown3038(1)
    GFX_0('rne406_Decoy_Eff', -1)
    Unknown21012('rne406_Kick_Eff', 32)
    sprite('null', 1)

@State
def Air_Assault_damy2():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown2035(1)
        Unknown4019(2)
        Unknown2019(1)
        Unknown13044(1)
    sprite('rne406_07', 8)
    GFX_0('rne406_Kick_Eff', 100)
    sprite('rne406_07', 5)
    Unknown3038(1)
    GFX_0('rne406_Decoy_Eff', -1)
    Unknown21012('rne406_Kick_Eff', 32)
    sprite('null', 1)

@State
def Land_Assault_damy():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown4019(2)
        Unknown4007(3)
        Unknown2019(1)
        Unknown13044(1)
        loopRelated(17, 60)

        def upon_17():
            GFX_0('rne400_Decoy2_Eff', -1)
            Unknown13(25)

        def upon_43():
            if (SLOT_48 == 1000):
                SLOT_51 = 15
                clearUponHandler(17)
                clearUponHandler(43)
            if (SLOT_48 == 1001):
                if (SLOT_18 >= 4):
                    GFX_0('rne400_Decoy_Eff', -1)
                    Unknown13(25)
                Unknown13(25)
            if (SLOT_48 == 1008):
                Unknown4007(0)

        def upon_3():
            if SLOT_51:
                Unknown2019(1)
                Unknown2035(1)
                SLOT_51 = (SLOT_51 + (-1))
                if (not SLOT_51):
                    GFX_0('rne400_Decoy_Eff', -1)
                    Unknown13(25)
    sprite('null', 3)
    sprite('rne400_00', 4)
    Unknown3001(0)
    Unknown3004(56)
    SFX_3('rnese_02')
    sprite('rne400_01', 4)
    SFX_3('rnese_00')
    sprite('rne400_02', 4)
    sprite('rne400_03', 4)
    sprite('rne400_04', 5)
    sprite('rne400_05', 5)
    label(0)
    sprite('rne400_06', 5)
    sprite('rne400_07', 5)
    sprite('rne400_08', 5)
    gotoLabel(0)

@State
def Land_Assault_damyAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Land_Assault_Int')
        Unknown4019(2)
        Unknown2019(-1)
        Unknown2053(1)
        Unknown4007(3)
        Unknown13044(1)
        if SLOT_6:
            callSubroutine('PartnerSkillInit')
            AirPushbackX(5000)
            AirPushbackY(28000)
            GroundedHitstunAnimation(10)
            AirHitstunAnimation(10)
            SLOT_6 = 0

        def upon_ON_HIT_OR_BLOCK():
            Unknown23022(1)
            Unknown23029(3, 1009, 1)
            SLOT_52 = 15
            clearUponHandler(10)
            clearUponHandler(54)
            clearUponHandler(19)

        def upon_43():
            if (SLOT_48 == 1002):
                if (SLOT_18 >= 4):
                    GFX_0('rne400_Decoy_Eff', -1)
                    Unknown13(25)
                Unknown13(25)
        Unknown23089(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            if (SLOT_18 >= 4):
                if (not SLOT_53):
                    GFX_0('rne400_Decoy_Eff', -1)
            Unknown13(25)
        Unknown23020(1)
        Unknown23021(1)

        def upon_19():
            Unknown23090(25)

        def upon_3():
            (SLOT_19 < 300000)
            if op(5, 2, 0, 2, 51):
                sendToLabel(0)
    sprite('null', 3)
    sprite('rne400_09', 3)
    Unknown3001(0)
    Unknown3004(56)
    SFX_3('rnese_02')
    sprite('rne400_10', 3)
    physicsXImpulse(5000)
    Unknown2015(150)
    Unknown4007(0)
    SFX_3('rnese_05')
    sprite('rne400_11', 3)
    teleportRelativeX(120000)
    physicsXImpulse(60000)
    SLOT_51 = 1
    sprite('rne400_12', 3)
    sprite('rne400_13', 3)
    sprite('rne400_11', 3)
    sprite('rne400_12', 3)
    sprite('rne400_13', 3)
    label(0)
    sprite('rne400_14', 3)
    SLOT_51 = 0
    clearUponHandler(3)
    Unknown1019(20)
    sprite('rne400_15', 3)
    Unknown1019(20)
    SFX_3('rnese_07')
    sprite('rne400_16', 3)
    Unknown2015(-1)
    Unknown1084(1)
    GFX_0('rne400_Slash_Eff', -1)

    def upon_3():
        if SLOT_52:
            clearUponHandler(43)
            Unknown2019(1)
            Unknown2035(1)
            SLOT_52 = (SLOT_52 + (-1))
            if (not SLOT_52):
                GFX_0('rne400_Decoy_Eff', -1)
    sprite('rne400_17', 3)
    SLOT_53 = 1
    clearUponHandler(43)
    sprite('rne400_18', 2)
    sprite('rne400_19', 2)
    sprite('keep', 2)
    sprite('keep', 1)
    GFX_0('rne400_Decoy_Eff', -1)
    Unknown13(25)
    loopRest()

@State
def Counter_Assault_damy():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown2075(1)
        Unknown23142(1)
        Unknown13044(1)

        def upon_43():
            if (SLOT_48 == 1004):
                clearUponHandler(52)
                clearUponHandler(43)
                sendToLabel(580)
                Unknown3038(1)
                Unknown4007(0)
        Unknown2053(1)
        Unknown23089(1, 0, 0, 0, 0, 1, 1, 1)
        sendToLabelUpon(54, 580)
    sprite('null', 3)
    sprite('rne403_04', 3)
    setInvincible(1)
    GuardPoint_(1)
    Unknown22031(15, 30)

    def upon_52():
        clearUponHandler(52)
        clearUponHandler(43)
        Unknown23029(3, 1003, 1)
        sendToLabel(580)
        Unknown3038(1)
        Unknown4007(0)
    label(0)
    sprite('rne403_05', 5)
    sprite('rne403_06', 5)
    sprite('rne403_07', 5)
    gotoLabel(0)
    label(580)
    sprite('null', 5)
    Unknown3038(1)
    Unknown23022(1)
    Unknown4007(0)

@State
def Counter_Assault_damy_Land():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown4009(3)
        Unknown23022(1)
        Unknown2005()
        teleportRelativeY(5000)
        Unknown2053(1)
        EnableCollision(1)
        sendToLabelUpon(2, 1)
        Unknown13044(1)
    sprite('rne404_00', 1)
    Unknown1045(-10000)
    physicsYImpulse(6000)
    setGravity(800)
    sprite('rne404_00', 2)
    Unknown4007(0)
    sprite('rne404_01', 3)
    sprite('rne404_02', 3)
    sprite('rne404_03', 20)
    label(1)
    sprite('rne404_04', 5)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rne404_05', 5)
    sprite('rne404_06', 5)
    sprite('rne404_07', 2)
    sprite('rne404_08', 2)
    sprite('rne404_09', 2)
    sprite('rne404_10', 1)

@State
def Counter_Assault_damy_Air():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4009(3)
        Unknown23022(1)
        Unknown2053(1)
        EnableCollision(0)
        Unknown1086(22)
        Unknown2005()
        Unknown13044(1)
    sprite('rne407_00', 1)
    physicsXImpulse(-5000)
    physicsYImpulse(23000)
    teleportRelativeX(-150000)
    Unknown1043()
    sprite('rne407_00', 2)
    sprite('rne407_01', 3)
    sprite('rne407_02', 3)
    sprite('rne407_03', 3)
    sprite('rne407_04', 1)

@State
def Counter_Parachute_damy():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown2075(1)
        Unknown23142(1)
        Unknown13044(1)

        def upon_43():
            if (SLOT_48 == 1006):
                Unknown13(25)
        Unknown2053(1)
        Unknown23089(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            Unknown13(25)
    sprite('null', 4)
    sprite('rne410_03', 5)
    setInvincible(1)
    GuardPoint_(1)
    Unknown22031(15, 30)

    def upon_52():
        Unknown23029(3, 1005, 1)
        Unknown13(25)
    label(0)
    sprite('rne410_01', 5)
    sprite('rne410_02', 5)
    sprite('rne410_03', 5)
    gotoLabel(0)

@State
def Partner_Assist_damyAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Air_Assault_Int')
        callSubroutine('PartnerSkillInit')
        AttackP2(80)
        GroundedHitstunAnimation(11)
        AirUntechableTime(80)
        YImpluseBeforeWallbounce(0)
        blockstun(20)
        PushbackX(4800)
        AirPushbackY(-80000)
        Unknown9190(1)
        Unknown9118(40)
        Unknown13044(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            clearUponHandler(2)
            Unknown2053(0)
            sendToLabel(2)
        Unknown4019(2)
        Unknown2019(-1)
        Unknown2053(1)

        def upon_43():
            if (SLOT_48 == 1007):
                GFX_0('rne406_Decoy_Eff', -1)
                Unknown21012('rne406_Kick_Eff', 32)
                Unknown13(25)
        Unknown23089(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            GFX_0('rne406_Decoy_Eff', -1)
            Unknown21012('rne406_Kick_Eff', 32)
            Unknown13(25)
            sendToLabel(1)
        Unknown23020(1)
        Unknown23021(1)

        def upon_19():
            Unknown23090(25)
        teleportRelativeX(-10000)
        teleportRelativeY(400000)
    sprite('rne406_00', 3)
    Unknown3001(0)
    Unknown3004(56)
    SFX_3('rnese_02')
    sprite('rne406_01', 3)
    sprite('rne406_02', 3)
    sprite('rne406_03', 3)
    sprite('rne406_04', 3)
    SFX_3('rnese_08')
    sprite('rne406_05', 3)
    physicsXImpulse(30000)
    physicsYImpulse(-50000)
    setGravity(2000)
    GFX_0('rne406_Kick_Eff', 100)
    sprite('rne406_06', 3)
    label(0)
    sprite('rne406_05', 3)
    sprite('rne406_06', 3)
    gotoLabel(0)
    label(1)
    sprite('keep', 1)
    Unknown1084(1)
    GFX_0('rne406_Decoy_Eff', -1)
    Unknown21012('rne406_Kick_Eff', 32)
    sprite('null', 1)
    Unknown13(25)
    label(2)
    sprite('null', 1)
    Unknown1084(1)
    GFX_0('rne406_Decoy_Eff', -1)
    Unknown21012('rne406_Kick_Eff', 32)
    sprite('null', 1)
    Unknown13(25)

@State
def CrushAttac_damy():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown4019(2)
        Unknown2019(-1)
        Unknown13044(1)
        Unknown2003(1)
        Unknown23022(1)
    sprite('null', 4)
    sprite('rne400_04', 5)
    sprite('rne400_05', 5)
    sprite('rne400_06', 5)
    sprite('rne400_07', 5)
    sprite('rne400_08', 5)
    sprite('rne400_06', 5)
    sprite('rne400_07', 5)
    sprite('rne400_08', 5)
    sprite('rne400_06', 5)
    sprite('rne400_07', 5)
    sprite('rne400_08', 5)
    sprite('rne400_06', 5)
    sprite('rne400_07', 5)
    sprite('rne400_08', 5)

@State
def CrushAttac_damyAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown11023(1)
        Unknown4019(2)
        Unknown2019(-1)
        Unknown13044(1)
        teleportRelativeX(-30000)
        teleportRelativeY(400000)
        Unknown2003(1)
        Unknown23022(1)
    sprite('rne406_03', 3)
    Unknown3001(0)
    Unknown3004(31)
    SFX_3('rnese_02')
    sprite('rne406_04', 3)
    SFX_3('rnese_08')
    sprite('rne406_05', 3)
    physicsXImpulse(30000)
    physicsYImpulse(-40000)
    setGravity(2000)
    GFX_0('rne406_Kick_Eff', 100)
    sprite('rne406_06', 3)
    sprite('rne406_05', 3)
    Unknown2035(1)
    Unknown2019(1)
    Unknown1084(1)
    sprite('rne406_07', 16)
    Unknown21012('rne406_Kick_Eff', 32)
    GFX_0('rne406_Decoy_Eff', -1)
    Unknown13(25)

@State
def CrushAttac_2nddamyAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(3)
        Unknown11023(1)
        Unknown2003(1)
        Unknown23022(1)
        Unknown4019(2)
        Unknown2019(-1)
        Unknown13044(1)
    sprite('rne400_09', 3)
    SFX_3('rnese_02')
    sprite('rne400_10', 3)
    sprite('rne400_14', 3)
    teleportRelativeX(180000)
    sprite('rne400_15', 3)
    SFX_3('rnese_07')
    sprite('rne400_16', 4)
    GFX_0('rne400_Slash_Eff', -1)
    sprite('rne400_17', 3)
    sprite('rne400_18', 3)
    sprite('rne400_19', 3)
    sprite('rne400_20', 3)
    sprite('rne400_21', 3)
    GFX_0('rne400_Decoy_Eff', -1)
    Unknown13(25)

@State
def CrushAttac_Assistdamy():

    def upon_IMMEDIATE():
        Unknown23022(1)
        Unknown2035(1)
        Unknown4019(2)
        Unknown2019(1)
        Unknown13044(1)
    sprite('rne406_05', 2)
    sprite('rne406_07', 16)
    GFX_0('rne406_Decoy_Eff', -1)
    Unknown13(25)

@State
def UltimateAssault_damyAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4019(2)
        Unknown2019(-1)
        Unknown2053(1)
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        hitstun(60)
        AirUntechableTime(60)
        Unknown23182(3)
        Hitstop(1)
        Unknown11001(6, 0, 2)
        Unknown11056(0)
        Unknown23022(1)
        if SLOT_5:
            Unknown11069('UltimateAssault_OD')
        else:
            Unknown11069('UltimateAssault')

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(1)
            Unknown23029(3, 2001, 1)

        def upon_78():
            sendToLabel(2)
            Unknown48(25, 2, 54, 22, 2, 26)
            if (SLOT_54 <= 200000):
                SLOT_7 = 1
            PushbackX(29800)
            hitstun(60)
            AirUntechableTime(60)
            Unknown11064(1)
            Unknown11001(0, 10, 12)
            AirHitstunAnimation(4)
            GroundedHitstunAnimation(4)
            clearUponHandler(10)
            clearUponHandler(78)
            clearUponHandler(7)
            clearUponHandler(17)
            clearUponHandler(19)
        loopRelated(17, 23)

        def upon_17():
            sendToLabel(1)
        Unknown2053(1)
        Unknown23089(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            Unknown23029(3, 2002, 1)
            GFX_0('rne400_Decoy_Eff', -1)
            Unknown13(25)
        Unknown23020(1)
        Unknown23021(1)

        def upon_19():
            Unknown23090(25)
    sprite('null', 3)
    sprite('rne430_09', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    Unknown3001(0)
    Unknown3004(56)
    SFX_3('rnese_02')
    SFX_3('rnese_05')
    sprite('rne430_10', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    physicsXImpulse(5000)
    sprite('rne430_11', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    teleportRelativeX(120000)
    physicsXImpulse(60000)
    Unknown1028(1000)
    sprite('rne430_12', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)

    def upon_7():
        sendToLabel(1)
    sprite('rne430_11', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    Unknown1019(105)
    sprite('rne430_12', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    sprite('rne430_11', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    sprite('rne430_12', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    label(0)
    sprite('rne430_11', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    Unknown23022(0)
    sprite('rne430_12', 3)
    GFX_0('rne430_DashPa_Eff', 100)
    Unknown8010(100, 1, 1)
    gotoLabel(0)
    label(1)
    sprite('rne430_09', 20)
    Unknown23029(3, 2002, 1)
    clearUponHandler(7)
    clearUponHandler(17)
    clearUponHandler(19)
    Unknown1084(1)
    Unknown1045(10000)
    Unknown23022(1)
    GFX_0('rne400_Decoy_Eff', -1)
    Unknown13(25)
    sprite('null', 1)
    ExitState()
    label(2)
    sprite('keep', 2)
    Unknown2003(1)
    Unknown23029(3, 2000, 1)
    Unknown23022(1)
    Unknown3004(-127)
    Unknown2035(1)
    sprite('null', 1)
    ExitState()

@State
def UltimateAssaultDD_damyAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        Unknown4019(2)
        Unknown2019(-1)
        Unknown2054(1)
        Unknown2053(1)
        AttackLevel_(4)
        Damage(500)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        hitstun(60)
        AirUntechableTime(60)
        MinimumDamagePct(100)
        Unknown23182(3)
        Hitstop(1)
        Unknown11001(6, 0, 2)
        Unknown11056(0)
        Unknown23022(1)
        if SLOT_5:
            Unknown11069('ChangePartnerDDOD_Exe')
        else:
            Unknown11069('ChangePartnerDD_Exe')

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(1)
            Unknown23029(3, 2001, 1)

        def upon_78():
            sendToLabel(2)
            Unknown48(25, 2, 54, 22, 2, 26)
            if (SLOT_54 <= 200000):
                SLOT_7 = 1
            PushbackX(29800)
            hitstun(60)
            AirUntechableTime(60)
            Unknown11064(1)
            Unknown11001(0, 10, 12)
            AirHitstunAnimation(4)
            GroundedHitstunAnimation(4)
            clearUponHandler(10)
            clearUponHandler(78)
            clearUponHandler(7)
            clearUponHandler(17)
            clearUponHandler(19)
        loopRelated(17, 23)

        def upon_17():
            sendToLabel(1)
        Unknown2053(1)
        Unknown23089(1, 0, 0, 0, 0, 1, 1, 1)

        def upon_54():
            GFX_0('rne400_Decoy_Eff', -1)
            Unknown13(25)
            Unknown23029(3, 2002, 1)
            Unknown13(25)
        Unknown23020(1)
        Unknown23021(1)

        def upon_19():
            Unknown23090(25)
    sprite('null', 3)
    sprite('rne430_09', 3)
    SFX_3('rnese_02')
    SFX_3('rnese_05')
    sprite('rne430_10', 3)
    physicsXImpulse(5000)
    sprite('rne430_11', 3)
    teleportRelativeX(120000)
    physicsXImpulse(60000)
    Unknown1028(1000)
    sprite('rne430_12', 3)

    def upon_7():
        sendToLabel(1)
    sprite('rne430_11', 3)
    Unknown1019(105)
    sprite('rne430_12', 3)
    sprite('rne430_11', 3)
    sprite('rne430_12', 3)
    label(0)
    sprite('rne430_11', 3)
    Unknown23022(0)
    sprite('rne430_12', 3)
    gotoLabel(0)
    label(1)
    sprite('rne430_09', 20)
    Unknown23029(3, 2002, 1)
    clearUponHandler(7)
    clearUponHandler(17)
    clearUponHandler(19)
    Unknown1084(1)
    Unknown1045(10000)
    Unknown23022(1)
    Unknown2035(1)
    Unknown2018(0, 50)
    Unknown3004(-30)
    sprite('null', 1)
    ExitState()
    label(2)
    sprite('keep', 2)
    Unknown2003(1)
    Unknown23029(3, 2000, 1)
    Unknown23022(1)
    Unknown3004(-127)
    Unknown2035(1)
    sprite('null', 1)
    ExitState()

@State
def UltimateAssault_Camera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)

        def upon_3():
            Unknown1086(3)
    sprite('null', 400)

@State
def UltimateAssault_OD_damyAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        Damage(2600)
        AttackP1(80)
        AttackP2(60)
        MinimumDamagePct(8)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        WallbounceReboundTime(0)
        AirPushbackX(90000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(100)
        Unknown9310(30)
        AirUntechableTime(60)
        Unknown9202(39)
        Hitstop(20)
        Unknown11092(1)
        Unknown23182(3)
        Unknown11056(0)
        Unknown11001(0, 12, 12)
        Unknown11064(0)
        Unknown4019(2)
        Unknown2019(1)
        Unknown2054(1)
    sprite('rne430_40', 33)
    teleportRelativeX(20000)
    Unknown1007(-20000)
    Unknown1045(5000)
    physicsYImpulse(2000)
    setGravity(50)
    Unknown3001(0)
    Unknown3004(7)
    Unknown3029(1)
    AfterimageColor_1(128, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    Unknown3069(1)
    Unknown3070(1)
    AfterimageCount(4)
    SFX_3('rnese_02')
    sprite('rne430_41', 7)
    Unknown2019(-1)
    Unknown1051(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('rne430_42', 12)
    Unknown1084(1)
    SFX_3('rnese_08')
    sprite('rne430_43', 7)
    GFX_0('rne430_KickKiseki_Eff', 100)
    GFX_0('rne430_KickSlashBack_Eff', 100)
    GFX_0('rne430_KickSlashAdd_Eff', 100)
    GFX_0('rne430_Ring3_Eff', 100)
    sprite('rne430_44', 14)
    ScreenShake(5000, 5000)
    Unknown23029(3, 2003, 1)
    sprite('rne430_45', 6)
    Unknown3029(0)
    Unknown2019(1)
    sprite('rne430_46', 6)
    Unknown1045(-20000)
    physicsYImpulse(2000)
    setGravity(200)
    sprite('rne430_47', 6)
    loopRest()
    GFX_0('rne430_Decoy_Eff', 100)
    Unknown13(25)

@State
def UltimateAssaultDD_OD_damyAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056()
        AttackLevel_(4)
        Damage(500)
        AttackP1(80)
        AttackP2(60)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        WallbounceReboundTime(0)
        AirPushbackX(90000)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(100)
        Unknown9310(30)
        AirUntechableTime(60)
        Unknown9202(39)
        Hitstop(20)
        Unknown11092(1)
        Unknown23182(3)
        Unknown11056(0)
        Unknown11001(0, 12, 12)
        Unknown11064(0)
        Unknown4019(2)
        Unknown2019(1)
        Unknown2054(1)
    sprite('rne430_40', 33)
    teleportRelativeX(20000)
    Unknown1007(-20000)
    Unknown1045(5000)
    physicsYImpulse(2000)
    setGravity(50)
    Unknown3001(0)
    Unknown3004(7)
    Unknown3029(1)
    AfterimageColor_1(128, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    Unknown3069(1)
    Unknown3070(1)
    AfterimageCount(4)
    SFX_3('rnese_02')
    sprite('rne430_41', 7)
    Unknown2019(-1)
    Unknown1051(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('rne430_42', 12)
    Unknown1084(1)
    sprite('rne430_43', 7)
    GFX_0('rne430_KickKiseki_Eff', 100)
    GFX_0('rne430_KickSlashBack_Eff', 100)
    GFX_0('rne430_KickSlashAdd_Eff', 100)
    GFX_0('rne430_Ring3_Eff', 100)
    sprite('rne430_44', 14)
    ScreenShake(5000, 5000)
    Unknown23029(3, 2003, 1)
    sprite('rne430_45', 6)
    Unknown3029(0)
    Unknown2019(1)
    sprite('rne430_46', 6)
    Unknown1045(-20000)
    physicsYImpulse(2000)
    setGravity(200)
    sprite('rne430_47', 6)
    loopRest()
    GFX_0('rne430_Decoy_Eff', 100)
    Unknown13(25)

@State
def AstralHeat_damyAtk1st():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Unknown11056(0)
        MinimumDamagePct(100)
        AirUntechableTime(120)
        hitstun(120)
        Unknown9310(1)
        Hitstop(4)
        AirPushbackX(15000)
        YImpluseBeforeWallbounce(0)
        Unknown23022(1)
        Unknown1086(22)
        teleportRelativeX(150000)
        Unknown11023(1)
    sprite('rne407_00', 3)
    Unknown3001(0)
    Unknown3004(25)
    teleportRelativeY(200000)
    Unknown3038(0)
    physicsXImpulse(5000)
    physicsYImpulse(23000)
    Unknown1043()
    Unknown2006()
    SFX_3('rnese_02')
    sprite('rne407_01', 3)
    sprite('rne407_02', 3)
    sprite('rne407_03', 3)
    sprite('rne407_04', 3)
    sprite('rne406_00', 3)
    Unknown1084(1)
    sprite('rne406_01', 3)
    sprite('rne406_02', 3)
    sprite('rne406_03', 3)
    sprite('rne406_04', 3)
    SFX_3('rnese_08')
    sprite('rne406_05', 3)
    GFX_0('rne406_Kick_Eff', 100)
    physicsXImpulse(32000)
    physicsYImpulse(-50000)
    setGravity(2000)
    StartMultihit()
    sprite('rne406_06', 3)
    Unknown3038(1)
    GFX_0('Air_Assault_damy2', -1)
    GFX_0('AstralHeat_damyAtk2nd', -1)
    Unknown26('rne406_Kick_Eff')
    sprite('rne406_05', 3)
    sprite('rne406_06', 3)
    sprite('rne406_05', 3)
    sprite('rne406_06', 3)

@State
def AstralHeat_damyAtk2nd():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Unknown11056(0)
        MinimumDamagePct(100)
        AirUntechableTime(120)
        hitstun(120)
        Unknown9310(1)
        Hitstop(4)
        AirPushbackX(15000)
        YImpluseBeforeWallbounce(0)
        Unknown23022(1)
        Unknown11023(1)
        Unknown1086(22)
        teleportRelativeX(400000)
        teleportRelativeY(0)

        def upon_LANDING():
            sendToLabel(1)
        sendToLabelUpon(32, 2)
    sprite('rne202_00', 3)
    Unknown3001(0)
    Unknown3004(25)
    Unknown3038(0)
    Unknown2006()
    GFX_0('rne450_Warp_Eff', 103)
    Unknown36(1)
    teleportRelativeX(50000)
    Unknown1007(50000)
    Unknown1064(1200)
    Unknown1056(800)
    Unknown1072(25000)
    Unknown35()
    sprite('rne202_01', 2)
    sprite('rne202_02', 2)
    physicsYImpulse(20000)
    setGravity(2000)
    Unknown23087(100000)
    sprite('rne202_03', 3)
    sprite('rne202_04', 3)
    sprite('rne202_05', 3)
    sprite('rne202_06', 3)
    SFX_3('rnese_00')
    sprite('rne202_07', 32767)
    GFX_0('rne202_KickSlash_Eff', 100)
    label(1)
    sprite('rne202_08', 3)
    teleportRelativeX(55000)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    GFX_0('AstralHeat_damyAtk4th', -1)
    sprite('rne202_09', 1)
    sprite('rne202_10', 1)
    sprite('rne202_11', 1)
    sprite('rne202_12', 2)
    sprite('rne202_13', 2)
    sprite('rne202_14', 2)
    sprite('rne272_01', 4)
    Unknown1045(45000)
    physicsYImpulse(28000)
    setGravity(1800)
    sendToLabelUpon(2, 2)
    Unknown2006()
    Unknown3029(1)
    AfterimageColor_1(128, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    Unknown3069(1)
    Unknown3070(1)
    AfterimageCount(4)
    SFX_0('002_highjump_1')
    sprite('rne272_02', 5)
    sprite('rne272_03', 5)
    sprite('rne272_04', 6)
    sprite('rne250_00', 2)
    Unknown2005()
    Unknown1051(60)
    setGravity(900)
    sprite('rne250_01', 2)
    sprite('rne250_02', 3)
    sprite('rne250_03', 4)
    RefreshMultihit()
    Hitstop(7)
    GFX_0('rne250_UmbSlash_Eff', 103)
    Unknown36(1)
    Unknown1007(200000)
    Unknown35()
    AirPushbackX(10000)
    AirPushbackY(-40000)
    Unknown9202(100)
    sprite('rne250_04', 2)
    GFX_0('AstralHeat_damyAtk3rd', -1)
    GFX_0('rne410_Decoy_Eff', -1)
    Unknown3004(-85)
    Unknown2035(1)
    Recovery()
    Unknown2063()
    sprite('rne250_05', 3)
    sprite('rne250_06', 3)
    sprite('rne250_07', 3)
    sprite('rne250_08', 3)
    label(2)
    sprite('rne403_00', 3)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown3004(12)
    Unknown3001(12)
    Unknown2035(0)
    sprite('rne403_01', 3)
    sprite('rne403_02', 3)
    sprite('rne403_03', 3)
    sprite('rne403_04', 3)
    sprite('rne403_05', 5)
    sprite('rne403_06', 5)
    GFX_0('AstralHeat_damyAtk6th', -1)
    Unknown23029(3, 3000, 0)
    sprite('rne403_07', 5)
    sprite('rne403_05', 5)
    sprite('rne403_06', 5)
    sprite('rne403_07', 5)
    sprite('rne403_05', 5)
    sprite('rne030_00', 6)
    physicsXImpulse(8000)
    Unknown3029(1)
    AfterimageColor_1(128, 255, 255, 255)
    AfterimageColor_2(0, 255, 255, 255)
    Unknown3069(1)
    Unknown3070(2)
    AfterimageCount(3)
    sprite('rne431_00ex', 4)
    physicsXImpulse(20000)
    Unknown1028(440)
    Unknown8007(100, 1, 1)
    Unknown11072(1, 200000, 0)
    SFX_3('rnese_05')
    sprite('rne431_01', 4)
    RefreshMultihit()
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9130(100)
    Unknown9142(100)

    def upon_78():
        Unknown23029(3, 3001, 0)
        Unknown13(25)
    sprite('rne431_00', 4)
    Unknown13(25)
    Unknown8006(100, 1, 1)
    EnableCollision(0)
    Unknown1028(1320)
    sprite('rne431_01', 4)
    sprite('rne431_00', 4)
    sprite('rne431_01', 4)

@State
def AstralHeat_damyAtk3rd():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Unknown11056(0)
        MinimumDamagePct(100)
        AirUntechableTime(120)
        hitstun(120)
        Unknown9310(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackY(20000)
        AirPushbackX(2000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(60)
        Unknown23022(1)
        Unknown1086(22)
        teleportRelativeY(0)
        teleportRelativeX(450000)
        Unknown11023(1)
        Unknown2006()
    sprite('rne405_00', 2)
    Unknown3001(0)
    Unknown3004(25)
    teleportRelativeY(0)
    physicsXImpulse(20000)
    Unknown1045(10000)
    SFX_3('rnese_02')
    sprite('rne405_00', 1)
    Unknown8006(100, 1, 1)
    Unknown3004(85)
    SFX_3('rnese_08')
    sprite('rne405_01', 2)
    sprite('rne405_02', 1)
    sprite('rne405_03', 1)
    sprite('rne405_04', 4)
    Unknown1084(1)
    GFX_0('rne405_Slash_Eff', 100)
    GFX_0('rne405_SlashEdge_Eff', 100)
    sprite('rne405_05', 3)
    sprite('rne405_06', 3)
    GFX_0('rne403_Decoy_Eff', -1)

@State
def AstralHeat_damyAtk4th():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Unknown11056(0)
        MinimumDamagePct(100)
        AirUntechableTime(120)
        hitstun(120)
        Unknown9310(1)
        Hitstop(14)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(30)
        Unknown23022(1)
        Unknown1086(22)
        teleportRelativeX(100000)
        Unknown11023(1)
        Unknown2006()
    sprite('rne403_08', 2)
    Unknown3001(0)
    Unknown3004(25)
    Unknown1007(420000)
    setGravity(1200)
    Unknown3001(0)
    Unknown3004(25)
    SFX_3('rnese_02')
    sprite('rne403_09', 2)
    sprite('rne403_10', 2)
    SFX_3('rnese_07')
    sprite('rne403_11', 2)
    sprite('rne403_12', 3)
    GFX_0('rne403_Eff', 100)
    physicsXImpulse(5000)
    physicsYImpulse(-80000)
    setGravity(2000)
    StartMultihit()
    sprite('rne403_13', 3)
    Unknown3004(-85)
    Unknown2035(1)
    GFX_0('rne410_Decoy_Eff', -1)
    sprite('rne403_12', 3)

@State
def AstralHeat_damyAtk5th():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Unknown11056(0)
        MinimumDamagePct(100)
        AirUntechableTime(600)
        hitstun(600)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-5000)
        AirPushbackY(50000)
        Unknown9310(999)
        Hitstop(0)
        Unknown11072(1, 50000, 0)
        Unknown23022(1)

        def upon_78():
            Unknown11064(1)
            clearUponHandler(78)
            Unknown21007(2, 32)
            Unknown21007(3, 33)
            Unknown13(25)
    sprite('null', 3)
    sprite('rne430_09', 3)
    sprite('rne430_10', 3)
    physicsXImpulse(5000)
    sprite('rne430_11', 3)
    teleportRelativeX(120000)
    physicsXImpulse(60000)
    Unknown1028(1000)
    sprite('rne430_12', 3)
    sprite('rne430_11', 3)
    Unknown1019(105)
    sprite('rne430_12', 3)
    sprite('rne430_11', 3)
    sprite('rne430_12', 3)
    label(0)
    sprite('rne430_11', 3)
    Unknown23022(0)
    sprite('rne430_12', 3)
    gotoLabel(0)

@State
def AstralHeat_damyAtk6th():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Unknown11056(0)
        MinimumDamagePct(100)
        AirUntechableTime(600)
        hitstun(600)
        AirPushbackX(-1000)
        AirPushbackY(-40000)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9310(999)
        Unknown9190(1)
        Unknown9118(40)
        Unknown23022(1)
        Unknown1086(22)
        teleportRelativeX(200000)
        teleportRelativeY(0)
        Unknown11023(1)
        Unknown2006()
    sprite('rne320_00', 4)
    Unknown3001(0)
    Unknown3004(25)
    Unknown3001(0)
    Unknown3004(25)
    SFX_3('rnese_02')
    sprite('rne320_01', 3)
    sprite('rne320_02', 3)
    teleportRelativeX(5000)
    sprite('rne320_03', 3)
    teleportRelativeX(30000)
    GFX_0('rne320_Eff', 100)
    SFX_3('rnese_08')
    sprite('rne320_04', 3)
    teleportRelativeX(-20000)
    GFX_0('rne410_Decoy_Eff', -1)
    sprite('rne320_05', 3)
    Unknown3004(-85)
    Unknown2035(1)
    Unknown1084(1)
    sprite('rne320_06', 4)

@State
def AstralHeat_damyAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(3)
        Damage(24500)
        Unknown11056(0)
        Unknown11064(3)
        MinimumDamagePct(100)
        AirUntechableTime(120)
        hitstun(120)
        Unknown9310(1)
        AirPushbackX(15000)
        YImpluseBeforeWallbounce(0)
        Unknown11050(5, '')
        Unknown1086(22)
        Unknown11023(1)
        Unknown3038(1)
    sprite('rne450_37', 4)
    RefreshMultihit()
    Unknown36(22)
    Unknown1000(-200000)
    teleportRelativeY(1800000)
    Unknown3038(1)
    Unknown35()

@Subroutine
def rneef_Color_Slash():
    Unknown4061(1)
    Unknown21004(1)

@Subroutine
def rneef_Color_Slash_ptcl():
    Unknown4061(1)
    Unknown4047(1, 1, 1)

@Subroutine
def rneef_Color_Umb():
    Unknown4061(0)
    Unknown21004(192)

@Subroutine
def rneef_Color_Umb2():
    Unknown4061(0)
    Unknown21004(212)

@Subroutine
def rneef_Color_Boots():
    Unknown4061(0)
    Unknown21004(118)

@Subroutine
def skin_color():
    Unknown4047(16, 16, 16)

@Subroutine
def hair_color():
    Unknown4047(48, 48, 48)

@Subroutine
def hair2_color():
    Unknown4047(32, 32, 32)

@Subroutine
def tops_color():
    Unknown4047(22, 22, 22)

@Subroutine
def inner_color():
    Unknown4047(55, 55, 55)

@Subroutine
def bottom_color():
    Unknown4047(102, 102, 102)

@Subroutine
def umb_color():
    Unknown4047(160, 160, 160)

@Subroutine
def umb2_color():
    Unknown4047(176, 176, 176)

@State
def rne400_Decoy_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne400_Decoy_atk', 1)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 0)
    callSubroutine('hair_color')
    Unknown4045('rneef_DecoyClash', 1)
    callSubroutine('hair2_color')
    Unknown4045('rneef_DecoyClash', 2)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 3)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 4)
    callSubroutine('inner_color')
    Unknown4045('rneef_DecoyClash', 5)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 6)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 7)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 8)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 9)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 10)
    callSubroutine('umb_color')
    Unknown4045('rneef_DecoyClash', 11)
    callSubroutine('umb2_color')
    Unknown4045('rneef_DecoyClash', 12)
    SFX_3('rnese_04')

@State
def rne400_Decoy2_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne400_Decoy', 1)
    callSubroutine('skin_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 0)
    callSubroutine('hair_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 1)
    callSubroutine('hair2_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 2)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 3)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 4)
    callSubroutine('inner_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 5)
    callSubroutine('skin_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 6)
    callSubroutine('bottom_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 7)
    callSubroutine('bottom_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 8)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 9)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 10)
    callSubroutine('umb_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 11)
    callSubroutine('umb2_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash', 12)
    SFX_3('rnese_04')

@State
def rne403_Decoy_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne403_Decoy', 1)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 0)
    callSubroutine('hair_color')
    Unknown4045('rneef_DecoyClash', 1)
    callSubroutine('hair2_color')
    Unknown4045('rneef_DecoyClash', 2)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 3)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 4)
    callSubroutine('inner_color')
    Unknown4045('rneef_DecoyClash', 5)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 6)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 7)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 8)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 9)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 10)
    callSubroutine('umb_color')
    Unknown4045('rneef_DecoyClash', 11)
    callSubroutine('umb2_color')
    Unknown4045('rneef_DecoyClash', 12)
    SFX_3('rnese_04')

@State
def rne406_Decoy_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne406_Decoy', 1)
    callSubroutine('skin_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 0)
    callSubroutine('hair_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 1)
    callSubroutine('hair2_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 2)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 3)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 4)
    callSubroutine('inner_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 5)
    callSubroutine('skin_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 6)
    callSubroutine('bottom_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 7)
    callSubroutine('bottom_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 8)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 9)
    callSubroutine('tops_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 10)
    callSubroutine('umb_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 11)
    callSubroutine('umb2_color')
    Unknown4054(11)
    Unknown4045('rneef_DecoyClash2', 12)
    SFX_3('rnese_04')

@State
def rne410_Decoy_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne403_Decoy', 1)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 0)
    callSubroutine('hair_color')
    Unknown4045('rneef_DecoyClash', 1)
    callSubroutine('hair2_color')
    Unknown4045('rneef_DecoyClash', 2)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 3)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 4)
    callSubroutine('inner_color')
    Unknown4045('rneef_DecoyClash', 5)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 6)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 7)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 8)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 9)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 10)
    callSubroutine('umb_color')
    Unknown4045('rneef_DecoyClash', 11)
    callSubroutine('umb2_color')
    Unknown4045('rneef_DecoyClash', 12)
    SFX_3('rnese_04')

@State
def rne430_Decoy_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne430_Decoy', 1)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 0)
    callSubroutine('hair_color')
    Unknown4045('rneef_DecoyClash', 1)
    callSubroutine('hair2_color')
    Unknown4045('rneef_DecoyClash', 2)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 3)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 4)
    callSubroutine('inner_color')
    Unknown4045('rneef_DecoyClash', 5)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash', 6)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 7)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash', 8)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 9)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash', 10)
    callSubroutine('umb_color')
    Unknown4045('rneef_DecoyClash', 11)
    callSubroutine('umb2_color')
    Unknown4045('rneef_DecoyClash', 12)
    SFX_3('rnese_04')

@State
def rne620_Decoy_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        Unknown3038(1)
    sprite('vr_rne620_Decoy', 1)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash3', 0)
    callSubroutine('hair_color')
    Unknown4045('rneef_DecoyClash3', 1)
    callSubroutine('hair2_color')
    Unknown4045('rneef_DecoyClash3', 2)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash3', 3)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash3', 4)
    callSubroutine('inner_color')
    Unknown4045('rneef_DecoyClash3', 5)
    callSubroutine('skin_color')
    Unknown4045('rneef_DecoyClash3', 6)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash3', 7)
    callSubroutine('bottom_color')
    Unknown4045('rneef_DecoyClash3', 8)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash3', 9)
    callSubroutine('tops_color')
    Unknown4045('rneef_DecoyClash3', 10)
    callSubroutine('umb_color')
    Unknown4045('rneef_DecoyClash3', 11)
    callSubroutine('umb2_color')
    Unknown4045('rneef_DecoyClash3', 12)
    SFX_3('rnese_04')

@State
def rne400_Warp_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_B')
        Unknown1007(-10000)
        teleportRelativeX(80000)
        Unknown1064(1000)
        Unknown1056(1450)
        Unknown1096(750)
        Unknown1072(180000)
    sprite('null', 3)
    physicsXImpulse(-5000)
    sprite('null', 57)
    Unknown3004(-16)
    SFX_3('rnese_01')

@State
def rne403_Warp_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_A')
        Unknown1064(1000)
        Unknown1056(800)
        Unknown1072(-25000)
    sprite('null', 3)
    physicsXImpulse(-5000)
    physicsYImpulse(5000)
    sprite('null', 57)
    Unknown3004(-20)
    SFX_3('rnese_01')

@State
def rne404_Warp_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_A')
        Unknown1064(1500)
        Unknown1056(800)
    sprite('null', 3)
    physicsXImpulse(0)
    sprite('null', 57)
    Unknown3004(-18)
    SFX_3('rnese_01')

@State
def rne405_Warp_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        GFX_2('rneef_Warp_B')
        teleportRelativeX(100000)
        Unknown1007(50000)
        Unknown1064(600)
        Unknown1056(1350)
        Unknown1072(180000)
    sprite('null', 3)
    physicsXImpulse(-5000)
    sprite('null', 57)
    Unknown3004(-16)
    SFX_3('rnese_01')

@State
def rne406_Warp_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_B')
        teleportRelativeX(-100000)
        Unknown1007(75000)
        Unknown1064(600)
        Unknown1056(1350)
    sprite('null', 3)
    physicsXImpulse(-5000)
    sprite('null', 57)
    Unknown3004(-16)
    SFX_3('rnese_01')

@State
def rne407_Warp_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_A')
        Unknown1007(65000)
        Unknown1064(1200)
        Unknown1056(800)
        Unknown1072(-25000)
    sprite('null', 3)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    sprite('null', 57)
    Unknown3004(-20)
    SFX_3('rnese_01')

@State
def rne450_Warp_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_A')
    sprite('null', 3)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    sprite('null', 57)
    Unknown3004(-20)
    SFX_3('rnese_01')

@State
def rne450_Warp2_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Warp_B')
    sprite('null', 3)
    physicsXImpulse(-5000)
    sprite('null', 57)
    Unknown3004(-16)
    SFX_3('rnese_01')

@State
def rne601_Warp_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown1007(-128000)
    sprite('null', 20)
    sprite('null', 60)
    SFX_3('rnese_01')
    Unknown1096(685)
    Unknown1099(15)
    GFX_2('rneef601_Warp')

@State
def rne200_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_200_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
    sprite('null', 13)

@State
def rne270_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_270_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
    sprite('null', 11)

@State
def rne271_KickStrike_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(3)
        Unknown1096(1500)
        GFX_2('rneef271_center_00')
    sprite('null', 60)
    GFX_0('rne271_ShockBig00_Eff', 100)
    GFX_0('rne271_ShockBig01_Eff', 100)
    GFX_0('rne271_ShockCircle_Eff', 100)

@State
def rne271_ShockBig00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4003('rneef_271_Shock.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(750)
        Unknown1064(650)
        Unknown1072(155000)
        Unknown23015(11)
    sprite('null', 21)

@State
def rne271_ShockBig01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4003('rneef_271_Shock.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1056(500)
        Unknown1064(300)
        Unknown1072(148000)
        Unknown23015(11)
    sprite('null', 21)

@State
def rne271_ShockCircle_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4003('rneef_271_ShockCircle.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1096(500)
    sprite('null', 1)
    Unknown3001(255)
    sprite('null', 14)
    Unknown3001(175)

@State
def rne272_KickSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_272_KickSlash.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(240)
        Unknown1000(-10000)
        teleportRelativeY(-10000)
        Unknown1056(1400)
        Unknown1064(900)
    sprite('null', 15)

@State
def rne272_KickSlash2_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_272_KickSlash2.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(240)
        teleportRelativeY(-10000)
        Unknown1056(1100)
        Unknown1064(800)
        Unknown1072(2500)
    sprite('null', 15)

@State
def rne201_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4022(3)
        Unknown4009(2)
        Unknown4003('rneef_201_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
    sprite('null', 10)

@State
def rne273_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4022(3)
        Unknown4009(2)
        Unknown4003('rneef_273_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        Unknown1007(-10000)
    sprite('null', 10)

@State
def rne274_UmbShock_Eff():

    def upon_IMMEDIATE():
        Unknown4003('rneef_274_Shock.DIG', '')
        Unknown4015()
        Unknown4009(2)
        callSubroutine('rneef_Color_Umb')
        Unknown3033()
        Unknown1096(1250)
        teleportRelativeX(-30000)
    sprite('null', 3)
    Unknown4047(192, 192, 192)
    Unknown4045('rneef274_shock', 100)
    sprite('null', 3)
    Unknown1099(20)
    sprite('null', 16)
    Unknown3004(-24)

@State
def rne202_KickSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_202_KickSlash.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(240)
        teleportRelativeX(-20000)
    sprite('null', 19)

@State
def rne231_KickSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4022(3)
        Unknown4009(2)
        Unknown4003('rneef_231_KickSlash.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(220)
        teleportRelativeX(-185000)
        Unknown1096(1175)
    sprite('null', 6)
    sprite('null', 13)
    Unknown4022(0)
    Unknown3005(-22)

@State
def rne232_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_232_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        teleportRelativeX(5000)
        Unknown1007(6000)
    sprite('null', 20)

@State
def rne232_KickSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_232_KickSlash.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(10000)
        Unknown1007(-60000)
    sprite('null', 12)

@State
def rne250_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_250_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        Unknown1007(10000)
        teleportRelativeX(-15000)
    sprite('null', 15)

@State
def rne251_UmbSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_251_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        Unknown1007(20000)
        teleportRelativeX(10000)
    sprite('null', 15)

@State
def rne275_KickSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_275_KickSlash.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(224)
        Unknown1007(15000)
    sprite('null', 19)

@State
def rne252_KickSlash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_252_KickSlash.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeY(8000)
        Unknown1000(2000)
        Unknown3001(180)
        Unknown1096(950)
    sprite('null', 13)
    sprite('null', 6)
    Unknown4007(0)

@State
def rne320_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        teleportRelativeY(30000)
        Unknown1000(-36000)
    sprite('null', 150)
    GFX_0('rne320_BloomBlur_Eff', 100)
    GFX_0('rne320_Slash_Eff', 100)

@State
def rne320_Slash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_320_Slash.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3001(115)
    sprite('null', 15)

@State
def rne320_BloomBlur_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_320_Bloom.DIG', '')
        Unknown4015()
        Unknown3032()
        callSubroutine('rneef_Color_Slash')
    sprite('null', 11)
    sprite('null', 4)
    Unknown3005(-25)

@State
def rne350_Appeal_Eff():

    def upon_IMMEDIATE():
        GFX_2('rneef_Provocation01')
        Unknown1096(1000)
    sprite('null', 13)

@State
def rne400_Slash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_400_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
    sprite('null', 18)
    GFX_0('rne400_SlashEdge_Eff', 100)
    GFX_0('rne400_SlashEdgeAdd_Eff', 100)

@State
def rne400_SlashEdge_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_400_SlashEdge.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3007(255)
        Unknown3013(160)
        Unknown3019(200)
    sprite('null', 15)

@State
def rne400_SlashEdgeAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_400_SlashEdge.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(255)
        Unknown3013(160)
        Unknown3019(200)
    sprite('null', 15)

@State
def rne402_Slash_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_402_Slash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
    sprite('null', 18)
    GFX_0('rne402_SlashEdge_Eff', 100)
    GFX_0('rne402_SlashEdgeAdd_Eff', 100)

@State
def rne402_SlashEdge_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_402_SlashEdge.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3007(255)
        Unknown3013(160)
        Unknown3019(200)
    sprite('null', 12)

@State
def rne402_SlashEdgeAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_402_SlashEdge.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown3007(255)
        Unknown3013(160)
        Unknown3019(200)
    sprite('null', 12)

@State
def rne403_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
    sprite('null', 60)
    Unknown4061(0)
    Unknown4047(48, 48, 48)
    Unknown4048(30000)
    Unknown4049(1080)
    Unknown4045('rneef403_Line_2', 103)
    GFX_0('rne403_Kick_Eff', 100)
    GFX_0('rne403_Circle_Eff', 100)
    GFX_0('rne403_GlowBack_Eff', 100)

@State
def rne403_Kick_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_403_hit.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Slash')
        Unknown3033()
        Unknown1096(640)
        Unknown1073(13000)
        teleportRelativeX(10000)
        Unknown1007(-10000)
    sprite('null', 5)
    Unknown1099(32)
    sprite('null', 4)
    Unknown3004(-63)

@State
def rne403_GlowBack_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        teleportRelativeX(-5000)
        Unknown1007(99000)
    sprite('null', 1)
    Unknown4054(15)
    Unknown4047(48, 48, 48)
    Unknown4048(-20000)
    Unknown4049(700)
    Unknown4045('rneef403_GlowBack', 103)

@State
def rne403_Circle_Eff():

    def upon_IMMEDIATE():
        Unknown4061(0)
        teleportRelativeX(37000)
        Unknown1007(-120000)
    sprite('null', 1)
    Unknown4048(-10000)
    Unknown4045('rneef403_Shock', 103)
    Unknown4048(-10000)
    Unknown4047(48, 48, 48)
    Unknown4045('rneef403_Shock00', 103)

@State
def rne405_Slash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_405_Slash.DIG', '')
        Unknown4015()
        Unknown3032()
        callSubroutine('rneef_Color_Slash')
        teleportRelativeX(45000)
        Unknown1007(-50000)
        Unknown1056(1240)
        Unknown1064(1860)
    sprite('null', 12)

@State
def rne405_SlashEdge_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_405_SlashEdge.DIG', '')
        Unknown4015()
        Unknown3033()
        callSubroutine('rneef_Color_Slash')
        teleportRelativeX(45000)
        Unknown1007(-50000)
        Unknown1056(1240)
        Unknown1064(1860)
    sprite('null', 12)

@State
def rne406_Kick_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_406_Kick.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown23015(15)
        teleportRelativeX(175000)
        Unknown1007(-155000)
        Unknown1072(-28000)
        sendToLabelUpon(32, 0)

        def upon_43():
            if (SLOT_48 == 1010):
                sendToLabel(0)
                teleportRelativeX(-100000)
    sprite('null', 300)
    label(0)
    sprite('null', 8)
    Unknown4007(0)
    Unknown1059(-100)
    Unknown1067(-75)
    GFX_0('rne406_Hit_Eff', 100)
    sprite('null', 4)
    Unknown3004(-64)

@State
def rne406_KickEnd_Eff():

    def upon_IMMEDIATE():
        Unknown4003('rneef_406_KickEnd.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Slash')
        Unknown3032()
        Unknown1099(22)
        Unknown23015(15)
    sprite('null', 8)
    sprite('null', 2)
    Unknown3004(-32)

@State
def rne406_Hit_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(-80000)
        Unknown1007(150000)
    sprite('null', 1)
    GFX_0('rne406_KickEnd_Eff', 100)
    Unknown4049(1250)
    Unknown4048(-23000)
    callSubroutine('rneef_Color_Slash_ptcl')
    Unknown4045('rneef406_center_00', 100)

@State
def rne430_Dashwind_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 4)
    GFX_0('rne430_Dashwind01_Eff', 100)
    sprite('null', 3)
    GFX_0('rne430_Dashwind00_Eff', 100)

@State
def rne430_Dashwind00_Eff():

    def upon_IMMEDIATE():
        Unknown4003('rneef_430_Dash00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
        teleportRelativeX(170000)
        physicsXImpulse(-2000)
        Unknown1096(8100)
        Unknown1100(20)
    sprite('null', 12)
    sprite('null', 17)
    Unknown3004(-20)

@State
def rne430_Dashwind01_Eff():

    def upon_IMMEDIATE():
        Unknown4003('rneef_430_Dash00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
        teleportRelativeX(370000)
        physicsXImpulse(-2000)
        Unknown1056(7900)
        Unknown1064(6900)
        Unknown1100(10)
    sprite('null', 12)
    sprite('null', 17)
    Unknown3004(-20)

@State
def rne430_DashPa_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4009(2)
        Unknown23067('rneef_430_Dash00')
        Unknown4015()
        Unknown1064(1000)
        Unknown1056(1000)
    sprite('null', 16)
    sprite('null', 5)

@State
def rne430_Umbrella_Slash_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_430_TornadeSlash.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        Unknown1064(1000)
        Unknown1056(1000)
    sprite('null', 32)
    SFX_3('rnese_22')

@State
def rne430_Umbrella_Slash_Edge_Add_():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_430_TornadeSlashEdge.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3033()
        Unknown1064(1000)
        Unknown1056(1000)
    sprite('null', 32)

@State
def rne430_Umbrella_Slash_Edge_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        Unknown1064(1000)
        Unknown1056(1000)
    sprite('null', 32)

@State
def rne430_Umbrella_Slash_Edge_Whit():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4003('rneef_430_TornadeSlashEdgeWhite', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3033()
        Unknown1064(1000)
        Unknown1056(1000)
    sprite('null', 32)
    Unknown3001(200)

@State
def rne430_SembranceShock_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3033()
        Unknown1064(1968)
        Unknown1056(1559)
        teleportRelativeX(-105000)
        Unknown1007(-250000)
    sprite('null', 3)
    sprite('null', 20)
    Unknown4003('rneef_430_SembranceShock.DIG', '')
    Unknown4015()
    sprite('null', 13)
    Unknown4007(0)

@State
def rne430_Umbrella_Smash_Eff():

    def upon_IMMEDIATE():
        Unknown1007(200000)
    sprite('null', 5)
    GFX_0('rne430_UmbEdgeNormal_Eff', 100)
    GFX_0('rne430_UmbNormal_Eff', 100)
    GFX_0('rne430_UmbEdgeBack_Eff', 100)
    GFX_0('rne430_UmbEdgeAdd_Eff', 100)
    SFX_3('rnese_10')
    sprite('null', 60)
    GFX_0('rne430_ShockGround_Eff', 100)
    GFX_0('rne430_ShockLoop_Eff', 100)
    GFX_0('rne430_Ring_Eff', 100)
    GFX_0('rne430_Ring2_Eff', 100)

@State
def rne430_UmbNormal_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_UmbNormal.DIG', '')
        Unknown23015(6)
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3033()
        Unknown1064(900)
        Unknown1056(900)
        Unknown1007(-200000)
    sprite('null', 4)
    GFX_0('rne430_hahen_Eff', 100)
    GFX_0('rne430_hahenAdd_Eff', 100)
    sprite('null', 2)
    GFX_0('rne430_shockAdd00_Eff', 100)
    GFX_0('rne430_shockAdd01_Eff', 100)
    sprite('null', 14)
    sprite('null', 20)
    Unknown3004(-13)

@State
def rne430_UmbEdgeBack_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_UmbEdgeBack.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb2')
        Unknown3032()
        Unknown1064(900)
        Unknown1056(900)
        Unknown1007(-200000)
        Unknown23015(6)
    sprite('null', 30)
    Unknown3001(255)
    sprite('null', 10)
    Unknown3004(-23)

@State
def rne430_UmbEdgeNormal_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_UmbEdgeNormal.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Umb')
        Unknown3032()
        Unknown1064(900)
        Unknown1056(900)
        Unknown1007(-200000)
        Unknown23015(6)
    sprite('null', 20)
    Unknown3001(200)
    sprite('null', 20)
    Unknown3004(-10)

@State
def rne430_UmbEdgeAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_UmbEdge.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(900)
        Unknown1056(900)
        Unknown1007(-200000)
        Unknown23015(6)
    sprite('null', 20)
    sprite('null', 4)
    Unknown3004(-35)
    sprite('null', 16)
    Unknown3004(-6)

@State
def rne430_hahen_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown23067('rneef430_hahen00')
        Unknown1096(1200)
        teleportRelativeX(-100000)
        Unknown1007(-50000)
    sprite('null', 60)

@State
def rne430_hahenAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown23067('rneef430_hahenAdd00')
        Unknown1096(1200)
        teleportRelativeX(-100000)
        Unknown1007(-50000)
    sprite('null', 60)

@State
def rne430_shockAdd00_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown23067('rneef430_shockAdd')
        Unknown1064(1600)
        Unknown1056(1300)
        teleportRelativeX(-35000)
        Unknown1007(10000)
    sprite('null', 60)

@State
def rne430_shockAdd01_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown23067('rneef430_shockAdd')
        Unknown1064(1350)
        Unknown1056(1200)
        Unknown1072(-8000)
        teleportRelativeX(345000)
        Unknown1007(10000)
    sprite('null', 60)

@State
def rne430_shockAdd02_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown23067('rneef430_togeAdd0')
        Unknown1064(1800)
        Unknown1056(1600)
        teleportRelativeX(105000)
        Unknown1007(10000)
    sprite('null', 60)

@State
def rne430_shockAdd03_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown23067('rneef430_togeAdd0')
        Unknown1064(1600)
        Unknown1056(1350)
        Unknown1072(-8000)
        teleportRelativeX(295000)
        Unknown1007(10000)
    sprite('null', 60)

@State
def rne430_ShockGround_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_ShockGround.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1000)
        Unknown1056(1000)
        Unknown1007(-200000)
        teleportRelativeX(135000)
        Unknown23015(6)
    sprite('null', 8)
    Unknown1100(100)
    sprite('null', 3)
    Unknown1100(60)
    Unknown3004(-33)
    sprite('null', 5)
    Unknown1100(30)

@State
def rne430_ShockGround01_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_ShockGround01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1000)
        Unknown1056(1000)
        Unknown1007(-200000)
        teleportRelativeX(135000)
        Unknown23015(6)
    sprite('null', 20)
    Unknown3001(150)
    sprite('null', 7)
    Unknown3004(-22)

@State
def rne430_ShockLoop_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 1)
    GFX_0('rne430_ShockGround02_Eff', 100)
    loopRelated(17, 22)

    def upon_17():
        sendToLabel(1)
    label(0)
    sprite('null', 5)
    GFX_0('rne430_ShockGround02_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 1)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-65)

@State
def rne430_ShockGround02_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_ShockGround02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1096(1400)
        Unknown1007(-200000)
        teleportRelativeX(-125000)
        Unknown23015(6)
    sprite('null', 5)
    sprite('null', 3)
    Unknown3004(-65)

@State
def rne430_Ring_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 6)
    GFX_0('rne430_Ring00_Eff', 100)
    sprite('null', 2)
    GFX_0('rne430_Ptcl00_Eff', 100)
    sprite('null', 1)
    GFX_0('rne430_Ptcl01_Eff', 100)
    sprite('null', 60)
    GFX_0('rne430_Ptcl02_Eff', 100)

@State
def rne430_Ring2_Eff():

    def upon_IMMEDIATE():
        teleportRelativeX(250000)
    sprite('null', 6)
    GFX_0('rne430_Ring00_Rev_Eff', 100)
    sprite('null', 1)
    GFX_0('rne430_Ptcl00_Rev_Eff', 100)
    sprite('null', 1)
    GFX_0('rne430_Ptcl01_Rev_Eff', 100)
    sprite('null', 60)
    GFX_0('rne430_Ptcl02_Rev_Eff', 100)

@State
def rne430_Ring00_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ring.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(-15000)
        Unknown23015(6)
    sprite('null', 20)
    sprite('null', 7)
    Unknown3004(-35)

@State
def rne430_Ptcl00_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ptcl00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(-15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ptcl01_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ptcl01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(-15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ptcl02_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ptcl02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(-15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ring00_Rev_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown4003('rneef_430_Ring.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 20)
    sprite('null', 7)
    Unknown3004(-35)

@State
def rne430_Ptcl00_Rev_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown4003('rneef_430_Ptcl00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ptcl01_Rev_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown4003('rneef_430_Ptcl01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ptcl02_Rev_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown2005()
        Unknown4003('rneef_430_Ptcl02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(-100000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_KickKiseki_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4015()
        callSubroutine('rneef_Color_Boots')
        Unknown3032()
    sprite('null', 3)
    SFX_3('rnese_11')
    sprite('null', 3)
    Unknown4003('rneef_430_KickKiseki.DIG', '')
    sprite('null', 3)
    Unknown3004(20)
    sprite('null', 8)
    Unknown3004(10)

@State
def rne430_KickSlashBack_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_KickSlash.DIG', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 25)

@State
def rne430_KickSlashAdd_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_KickSlashAdd.DIG', '')
        Unknown4015()
        Unknown3033()
    sprite('null', 25)

@State
def rne430_Ring3_Eff():

    def upon_IMMEDIATE():
        pass
    sprite('null', 2)
    sprite('null', 6)
    GFX_0('rne430_Ring01_Eff', 100)
    sprite('null', 2)
    GFX_0('rne430_Ptcl03_Eff', 100)
    sprite('null', 1)
    GFX_0('rne430_Ptcl04_Eff', 100)
    sprite('null', 60)
    GFX_0('rne430_Ptcl05_Eff', 100)

@State
def rne430_Ring01_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ring.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(150000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 20)
    sprite('null', 7)
    Unknown3004(-35)

@State
def rne430_Ptcl03_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ptcl00.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(150000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ptcl04_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ptcl01.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(150000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne430_Ptcl05_Eff():

    def upon_IMMEDIATE():
        Unknown4009(2)
        Unknown4003('rneef_430_Ptcl02.DIG', '')
        Unknown4015()
        Unknown3033()
        Unknown1064(1250)
        Unknown1056(1250)
        Unknown1007(150000)
        teleportRelativeX(135000)
        Unknown1072(15000)
        Unknown23015(6)
    sprite('null', 16)
    sprite('null', 5)
    Unknown3004(-55)

@State
def rne431_ThrowWind_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown2054(1)
    sprite('null', 2)
    GFX_0('rne431_Wind00_Eff', 100)
    sprite('null', 6)
    GFX_0('rne431_Tornade_Eff', 100)
    GFX_0('rne431_Wind01_Eff', 100)
    sprite('null', 1)
    GFX_0('rne431_Tornade_Eff', 100)
    GFX_0('rne431_Wind01_Eff', 100)

@State
def rne431_Wind00_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('rneef_431_wind00.DIG', '')
        Unknown4015()
        Unknown3032()
        Unknown3001(200)
        Unknown1007(20000)
        Unknown1096(3000)
        Unknown1100(200)
        Unknown1021(1000)
    sprite('null', 3)
    Unknown1100(-100)
    sprite('null', 2)
    Unknown1100(-40)
    sprite('null', 5)
    Unknown3005(-10)
    sprite('null', 20)

@State
def rne431_Wind01_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        callSubroutine('rneef_Color_Slash_ptcl')
        Unknown23067('rneef_431_Shock02')
        Unknown1007(70000)
        teleportRelativeX(-200000)
        Unknown1096(2200)
        Unknown1100(50)
    sprite('null', 3)
    sprite('null', 2)
    sprite('null', 5)
    sprite('null', 20)

@State
def rne431_Tornade_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('rneef_431_wind01.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Slash')
        Unknown3033()
        Unknown1007(150000)
        teleportRelativeX(90000)
        Unknown1096(2000)
        Unknown1100(170)
        Unknown1021(2000)
    sprite('null', 3)
    GFX_0('rne431_Tornade00_Eff', 100)
    GFX_0('rne431_Tornade01_Eff', 100)
    GFX_0('rne431_Tornade02_Eff', 100)
    sprite('null', 2)
    sprite('null', 5)
    Unknown1100(-100)
    Unknown3005(-10)
    sprite('null', 20)

@State
def rne431_Tornade00_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('rneef_431_wind01.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Slash')
        Unknown3033()
        Unknown1007(-30000)
        teleportRelativeX(-50000)
        Unknown1096(1200)
        Unknown1100(140)
        Unknown1072(174000)
        Unknown1021(3000)
    sprite('null', 3)
    sprite('null', 2)
    sprite('null', 5)
    Unknown1100(-100)
    Unknown3005(-14)
    sprite('null', 20)

@State
def rne431_Tornade01_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('rneef_431_wind02.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Slash')
        Unknown3033()
        Unknown1007(60000)
        teleportRelativeX(-50000)
        Unknown1096(1200)
        Unknown1100(150)
        Unknown1072(-194000)
        Unknown1021(5000)
    sprite('null', 3)
    sprite('null', 2)
    sprite('null', 5)
    Unknown1100(-100)
    Unknown3005(-15)
    sprite('null', 20)

@State
def rne431_Tornade02_Eff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown4003('rneef_431_wind02.DIG', '')
        Unknown4015()
        callSubroutine('rneef_Color_Slash')
        Unknown3033()
        Unknown1007(-130000)
        teleportRelativeX(-20000)
        Unknown1096(700)
        Unknown1100(150)
        Unknown1072(-35000)
    sprite('null', 3)
    sprite('null', 2)
    sprite('null', 5)
    Unknown1100(-100)
    Unknown3005(-8)
    sprite('null', 20)

@State
def rne450_Clash_Eff():

    def upon_IMMEDIATE():
        Unknown4015()
        Unknown4009(2)
        Unknown23015(1)
        Unknown23057(50)
        Unknown23058(48)
        Unknown4061(2)
        sendToLabelUpon(32, 0)
    sprite('rneef_450_crack02', 1)
    Unknown3032()
    SFX_3('rnese_18')
    SFX_3('rnese_18')
    sprite('rneef_450_crack01', 32767)
    Unknown3033()
    GFX_0('rneef_450_NeoCrack_Eff', -1)
    GFX_0('rneef_450_White01_Eff', -1)
    GFX_0('rneef_450_BG_Eff', -1)
    if SLOT_8:
        GFX_0('rneef_450_BGCrack_Eff', -1)
    else:
        GFX_0('rneef_450_BGCrack_Eff_Rev', -1)
    label(0)
    sprite('rneef_450_crack02', 2)
    SFX_3('rnese_19')
    Unknown4009(0)
    Unknown21010(1)
    Unknown3032()
    Unknown26('rneef_450_NeoCrack_Eff')
    Unknown26('rneef_450_BGCrack_Eff')
    Unknown26('rneef_450_BGCrack_Eff_Rev')
    Unknown26('rneef_450_BG_Eff')
    GFX_0('rneef_450_GlassPa_Eff', 0)
    GFX_0('rneef_450_Glass01_Eff', 0)
    Unknown36(1)
    Unknown1096(550)
    Unknown1073(-10000)
    Unknown1110(100, 0)
    Unknown35()
    GFX_0('rneef_450_Glass01_Eff', 0)
    Unknown36(1)
    Unknown1096(600)
    Unknown1073(70000)
    Unknown35()
    GFX_0('rneef_450_Glass01_Eff', 0)
    Unknown36(1)
    Unknown1096(650)
    Unknown1073(-90000)
    Unknown1110(50, 0)
    Unknown35()
    GFX_0('rneef_450_Glass02_Eff', 0)
    Unknown36(1)
    Unknown1096(720)
    Unknown1073(-25000)
    Unknown35()
    GFX_0('rneef_450_Glass02_Eff', 0)
    Unknown36(1)
    Unknown1096(770)
    Unknown1073(-90000)
    Unknown35()
    GFX_0('rneef_450_Glass02_Eff', 0)
    Unknown36(1)
    Unknown1096(750)
    Unknown1073(60000)
    Unknown35()
    GFX_0('rneef_450_Glass02_Eff', 0)
    Unknown36(1)
    Unknown2005()
    Unknown1096(650)
    Unknown1073(-80000)
    Unknown35()
    GFX_0('rneef_450_Glass03_Eff', 0)
    Unknown36(1)
    Unknown1096(450)
    Unknown1073(0)
    Unknown1073(80000)
    Unknown35()
    GFX_0('rneef_450_Glass03_Eff', 0)
    Unknown36(1)
    Unknown1096(600)
    Unknown1073(0)
    Unknown1073(55000)
    Unknown35()
    GFX_0('rneef_450_Glass03_Eff', 0)
    Unknown36(1)
    Unknown1096(550)
    Unknown1073(-60000)
    Unknown35()
    GFX_0('rneef_450_Glass03_Eff', 0)
    Unknown36(1)
    Unknown1096(600)
    Unknown1073(-35000)
    Unknown35()
    sprite('null', 110)
    Unknown4009(2)

@State
def rneef_450_White01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown23015(4)
        Unknown3033()
        Unknown1096(2200)
        Unknown23057(50)
        Unknown23058(50)
    sprite('vr_white', 10)
    Unknown3001(160)
    Unknown3004(-25)

@State
def rneef_450_Glass01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('rneef_450_glass01', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 180)

@State
def rneef_450_Glass02_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('rneef_450_glass02', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 180)

@State
def rneef_450_Glass03_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        Unknown4003('rneef_450_glass03', '')
        Unknown4015()
        Unknown3032()
    sprite('null', 180)

@State
def rneef_450_GlassPa_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4009(2)
        GFX_2('rneef_450_glass01')
    sprite('null', 180)

@State
def rneef_450_BG_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(2)
        Unknown4061(3)
    sprite('rneef_450_bg', 120)

@State
def rneef_450_BGCrack_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(6)
        Unknown4061(3)
    sprite('rneef_450_bg_crack01', 120)

@State
def rneef_450_BGCrack_Eff_Rev():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(6)
        Unknown4061(3)
    sprite('rneef_450_bg_crack02', 120)

@State
def rneef_450_NeoCrack_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown23015(7)
    sprite('rneef_450_neo_crack01', 120)

@State
def rneef_450_Hit_Eff():

    def upon_IMMEDIATE():
        Unknown1072(45000)
    sprite('null', 120)
    Unknown23067('rneef_450_Hit_Glow_00')

@State
def rneAss_Slash_00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4003('rneef_450_slash00.DIG', '')
        Unknown4015()
        Unknown3033()
        teleportRelativeX(-900000)
        Unknown1007(125000)
        Unknown1056(25000)
        Unknown1059(100)
        Unknown1064(4000)
        Unknown1072(180)
        physicsXImpulse(20000)
        Unknown23015(11)
    sprite('null', 12)
    GFX_1('rneef_As_slash02', 100)
    sprite('null', 6)
    GFX_0('rneAss_Slash_01_Eff', 100)

@State
def rneAss_Slash_01_Eff():

    def upon_IMMEDIATE():
        Unknown4054(11)
        Unknown23067('rneef_As_slash01')
        teleportRelativeX(500000)
        Unknown1056(3000)
        Unknown1064(1500)
    sprite('null', 23)

@State
def rneAss_sword_light00_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        GFX_2('rneef_As_sword_light001')
        Unknown1096(500)
        Unknown1072(45000)
        Unknown3001(180)
    sprite('null', 25)

@State
def rneAss_sword_light01_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        GFX_2('rneef_As_sword_light03')
        Unknown1096(600)
        Unknown1072(5000)
        Unknown1075(1000)
    sprite('null', 25)
    SFX_3('rnese_17')

@State
def Container():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown3032()
        Unknown2019(100)
        Unknown3001(0)
        Unknown3004(31)
    sprite('rne610_00ex', 32767)
    SFX_3('rnese_02')

@State
def rne611_Change_Eff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1007(-40000)
        physicsYImpulse(5500)
        Unknown4054(6)
        sendToLabelUpon(32, 1)
    SFX_3('rnese_21')
    label(0)
    sprite('null', 3)
    GFX_0('rne611_Change00_Eff', 100)
    GFX_0('rne611_Change01_Eff', 100)
    gotoLabel(0)
    label(1)
    sprite('null', 20)
    sprite('null', 40)
    Unknown4054(6)
    Unknown4045('rneef611_ptcl_Box00', 100)

@State
def rne611_Change00_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4054(6)
        Unknown23067('rneef611_ptcl_tmp00')
        Unknown3033()
    sprite('null', 60)

@State
def rne611_Change01_Eff():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4009(2)
        Unknown4054(6)
        Unknown23067('rneef611_ptcl_tmpadd00')
        Unknown3032()
    sprite('null', 60)

@State
def rne611_Anbrella():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4011(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown23015(7)
    sprite('rne611_05ex', 32767)