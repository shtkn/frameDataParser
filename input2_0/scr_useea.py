@State
def EffNmlAtk5A():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_071_00', 5)
    sprite('Action_071_01', 5)
    sprite('Action_071_02', 1)

@State
def EffNmlAtk5A_2nd():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_084_00', 5)
    sprite('Action_084_01', 5)
    sprite('Action_084_02', 5)

@State
def EffNmlAtk5A_3rd():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_082_00', 5)
    sprite('Action_082_01', 5)
    sprite('Action_082_02', 5)
    sprite('Action_082_03', 1)

@State
def EffNmlAtk5A_4th_AirShadow():

    def upon_IMMEDIATE():
        Unknown3026(-16777216)
        teleportRelativeX(26000)
        Unknown1007(50000)
        Unknown23022(1)
        Unknown2035(1)
    sprite('Action_364_03', 2)
    Unknown3001(128)
    Unknown3004(-20)
    sprite('Action_364_03', 2)
    physicsXImpulse(25000)
    physicsYImpulse(21000)
    setGravity(1900)
    sprite('Action_364_04', 6)

@State
def EffNmlAtk5A_4th_LandZanzo():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown1007(200000)
        physicsXImpulse(100000)
        Unknown2035(1)
    sprite('Action_101_00', 4)
    sprite('Action_101_01', 4)
    sprite('Action_101_02', 4)
    sprite('Action_101_03', 4)
    sprite('Action_101_04', 4)
    sprite('Action_101_05', 4)
    sprite('Action_101_06', 2)

@State
def EffNmlAtk5A_4th_Dummy_Zanzo():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_082_00', 5)
    sprite('Action_082_01', 5)
    sprite('Action_082_02', 5)
    sprite('Action_082_03', 1)

@State
def EffNmlAtk5A_4th_AtkSub():

    def upon_IMMEDIATE():
        Unknown1007(100000)
    sprite('Action_379_00', 3)
    sprite('Action_379_01', 3)
    sprite('Action_379_02', 3)
    sprite('Action_379_03', 3)

@State
def EffNmlAtk5B_2nd_LandShadow():

    def upon_IMMEDIATE():
        Unknown3026(-16777216)
        teleportRelativeX(75000)
        Unknown2035(1)
    sprite('Action_270_00', 6)
    Unknown3001(128)
    Unknown3004(-10)
    sprite('Action_270_01', 6)
    sprite('Action_270_02', 6)

@State
def EffNmlAtk5B_2nd_Zanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_382_00', 4)
    sprite('Action_382_01', 4)
    sprite('Action_382_02', 4)
    sprite('Action_382_03', 1)

@State
def EffNmlAtk5B_2nd_Zanzo2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1007(120000)
    sprite('Action_376_00', 2)
    sprite('Action_376_01', 2)
    sprite('Action_376_02', 2)
    sprite('Action_376_03', 2)
    sprite('Action_376_04', 2)
    sprite('Action_376_05', 2)
    sprite('Action_376_06', 2)
    sprite('Action_376_07', 2)

@State
def EffNmlAtk5B_3rd_Zanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_383_00', 4)
    sprite('Action_383_01', 4)
    sprite('Action_383_02', 4)
    sprite('Action_383_03', 1)

@State
def EffNmlAtk5B_3rd_Zanzo2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2005()
    sprite('Action_219_00', 2)
    sprite('Action_219_01', 2)
    sprite('Action_219_02', 2)
    sprite('Action_219_03', 2)
    sprite('Action_219_04', 2)
    sprite('Action_219_05', 2)
    sprite('Action_219_06', 2)
    sprite('Action_219_07', 1)

@State
def EffReversal_Zanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown1072(-15000)
    sprite('Action_383_00', 4)
    sprite('Action_383_01', 4)
    sprite('Action_383_02', 4)
    sprite('Action_383_03', 1)

@State
def EffNmlAtk5B_4th_AirZanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_218_00', 2)
    sprite('Action_218_01', 2)
    sprite('Action_218_02', 2)
    sprite('Action_218_03', 2)
    sprite('Action_218_04', 2)
    sprite('Action_218_05', 2)
    sprite('Action_218_06', 2)
    sprite('Action_218_07', 1)

@State
def EffNmlAtk5B_4th_LandZanzo1():
    sprite('Action_224_00', 6)
    Unknown3004(-20)
    Unknown2035(1)
    sprite('Action_224_01', 6)
    sprite('Action_224_02', 6)

@State
def EffNmlAtk5B_4th_LandZanzo2():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown2035(1)
    sprite('Action_226_00', 4)
    sprite('Action_226_01', 4)
    sprite('Action_226_02', 4)
    sprite('Action_226_03', 1)

@State
def EffNmlAtk5B_4th_AssistZanzo1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23022(1)
        Unknown3026(-16777216)
        Unknown2035(1)
    sprite('Action_045_01', 6)
    Unknown3004(-20)
    sprite('Action_045_01', 6)
    sprite('Action_045_01', 6)

@State
def EffNmlAtk5B_3rd_Kick():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_223_00', 4)
    sprite('Action_223_01', 4)
    sprite('Action_223_02', 4)

@State
def EffConfuse_AtkMatome():

    def upon_IMMEDIATE():
        Unknown2054(1)

        def upon_43():
            if (SLOT_48 == 100):
                Unknown1086(22)
                Unknown1007(200000)
                GFX_0('EffConfuse_AtkEff', 100)
                GFX_0('EffConfuse_AtkEffSub1', 100)
                GFX_0('EffConfuse_AtkEffSub2', 100)
                GFX_0('EffConfuse_AtkEffSub3', 100)
            if (SLOT_48 == 101):
                Unknown1086(23)
                Unknown1007(200000)
                GFX_0('EffConfuse_AtkEff', 100)
                GFX_0('EffConfuse_AtkEffSub1', 100)
                GFX_0('EffConfuse_AtkEffSub2', 100)
                GFX_0('EffConfuse_AtkEffSub3', 100)
    sprite('null', 30)

@State
def EffConfuse_AtkEff():

    def upon_IMMEDIATE():
        Unknown2054(1)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_375_00', 4)
    sprite('Action_375_01', 4)
    sprite('Action_375_02', 4)
    sprite('Action_375_03', 4)
    sprite('Action_375_04', 4)
    sprite('Action_375_05', 4)
    sprite('Action_375_06', 4)
    ExitState()
    label(1)
    sprite('Action_375_08', 4)
    sprite('Action_375_09', 4)
    sprite('Action_375_10', 4)
    sprite('Action_375_11', 4)
    sprite('Action_375_12', 4)
    sprite('Action_375_13', 4)
    sprite('Action_375_14', 4)
    sprite('Action_375_15', 4)

@State
def EffConfuse_AtkEffSub1():

    def upon_IMMEDIATE():
        Unknown2003(0)
        teleportRelativeX(-320000)
        Unknown1007(-150000)
        Unknown2054(1)
    sprite('null', 10)
    sprite('Action_378_00', 4)
    sprite('Action_378_01', 4)
    sprite('Action_378_02', 4)
    sprite('Action_378_03', 4)

@State
def EffConfuse_AtkEffSub2():

    def upon_IMMEDIATE():
        Unknown2003(0)
        teleportRelativeX(12000)
        Unknown1007(150000)
        Unknown2054(1)
    sprite('null', 10)
    sprite('Action_378_04', 4)
    sprite('Action_378_05', 4)
    sprite('Action_378_06', 4)
    sprite('Action_378_07', 4)

@State
def EffConfuse_AtkEffSub3():

    def upon_IMMEDIATE():
        Unknown2003(0)
        teleportRelativeX(320000)
        Unknown1007(-110000)
        Unknown2054(1)
    sprite('null', 10)
    sprite('Action_378_08', 4)
    sprite('Action_378_09', 4)
    sprite('Action_378_10', 4)
    sprite('Action_378_11', 4)

@State
def EffNmlAtk5B():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_083_00', 5)
    sprite('Action_083_01', 5)
    sprite('Action_083_02', 5)
    sprite('Action_083_03', 1)

@State
def EffNmlAtk2B():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_080_00', 6)
    sprite('Action_080_01', 6)
    sprite('Action_080_02', 1)

@State
def EffNmlAtk5C():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_092_00', 5)
    sprite('Action_092_01', 5)
    sprite('Action_092_02', 5)
    sprite('Action_092_03', 1)

@State
def EffNmlAtk5C_Chace2nd():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_093_00', 5)
    sprite('Action_093_01', 5)
    sprite('Action_093_02', 5)
    sprite('Action_093_03', 1)

@State
def EffNmlAtkAIR5A():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_086_00', 5)
    sprite('Action_086_01', 5)
    sprite('Action_086_02', 5)
    sprite('Action_086_03', 1)

@State
def EffNmlAtkAIR5B():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_087_00', 5)
    sprite('Action_087_01', 5)
    sprite('Action_087_02', 5)
    sprite('Action_087_03', 1)

@State
def EffNmlAtkAIR5C_Shadow():

    def upon_IMMEDIATE():
        teleportRelativeX(50000)
        Unknown1007(200000)
    sprite('Action_125_00', 2)
    Unknown4004('6566666563745f3239350000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    teleportRelativeX(-50000)
    Unknown1072(60000)
    Unknown35()
    sprite('Action_125_01', 2)
    sprite('Action_125_02', 2)
    sprite('Action_125_03', 2)
    sprite('Action_125_04', 2)
    sprite('Action_125_05', 2)
    sprite('Action_125_06', 2)
    sprite('Action_125_07', 1)

@State
def EffNmlAtkThow():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_098_00', 3)
    sprite('Action_098_01', 3)
    sprite('Action_098_02', 3)
    sprite('Action_098_03', 3)
    sprite('Action_098_03', 3)

@State
def EffAirBackDash():
    sprite('Action_219_00', 2)
    sprite('Action_219_01', 2)
    sprite('Action_219_02', 2)
    sprite('Action_219_03', 2)
    sprite('Action_219_04', 2)
    sprite('Action_219_05', 2)
    sprite('Action_219_06', 2)
    sprite('Action_219_07', 2)

@State
def EffReversalAdd():

    def upon_IMMEDIATE():
        Unknown1072(150000)
        Unknown1007(100000)
        teleportRelativeX(100000)
    sprite('Action_219_00', 2)
    sprite('Action_219_01', 2)
    sprite('Action_219_02', 2)
    sprite('Action_219_03', 2)
    sprite('Action_219_04', 2)
    sprite('Action_219_05', 2)
    sprite('Action_219_06', 2)
    sprite('Action_219_07', 2)

@State
def EffAssalut_Blade():

    def upon_IMMEDIATE():
        Unknown1007(250000)
        physicsXImpulse(60000)
        Unknown2054(1)
    sprite('Action_100_00', 3)
    sprite('Action_100_01', 3)
    sprite('Action_100_02', 3)
    sprite('Action_100_03', 3)
    sprite('Action_100_04', 3)
    sprite('Action_100_05', 3)
    sprite('Action_100_06', 1)

@State
def EffAssalut_BladeEx():

    def upon_IMMEDIATE():
        Unknown1007(250000)
        physicsXImpulse(150000)
        Unknown2054(1)
    sprite('Action_100_00', 3)
    sprite('Action_100_01', 3)
    sprite('Action_100_02', 3)
    sprite('Action_100_03', 3)
    sprite('Action_100_04', 3)
    sprite('Action_100_05', 3)
    sprite('Action_100_06', 1)

@State
def EffAssalut_Zanzo():

    def upon_IMMEDIATE():
        Unknown2054(1)
    sprite('Action_171_00', 6)
    Unknown3004(-40)
    sprite('Action_171_01', 2)

@State
def EffAirAssalut_Add():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown4009(3)
    sprite('Action_388_00', 3)
    sprite('Action_388_01', 2)
    sprite('Action_388_02', 1)

@State
def EffAirAssalut_GripSlush():

    def upon_IMMEDIATE():
        teleportRelativeX(55000)
        Unknown1007(-75000)
    sprite('Action_091_00', 5)
    sprite('Action_091_01', 7)
    sprite('Action_091_02', 6)
    sprite('Action_091_03', 1)

@State
def EffAirAssalut_GripAtkEff():
    sprite('Action_103_00', 5)
    sprite('Action_103_01', 2)
    sprite('Action_103_02', 3)
    sprite('Action_103_03', 7)
    sprite('Action_103_04', 3)
    sprite('Action_103_05', 1)

@State
def Shot_Zanzo():
    sprite('Action_089_00', 5)
    sprite('Action_089_01', 5)
    sprite('Action_089_02', 5)
    sprite('Action_089_03', 5)
    sprite('Action_089_04', 5)

@State
def Shot_HitEff():

    def upon_IMMEDIATE():

        def upon_43():
            if (SLOT_48 == 100):
                Unknown1086(22)
                Unknown1007(200000)
                Unknown26('Shot_HitEffSub')
                GFX_0('Shot_HitEffSub', 100)
                Unknown23029(1, 210, 0)
            if (SLOT_48 == 101):
                Unknown1086(23)
                Unknown1007(200000)
                Unknown26('Shot_HitEffSub')
                GFX_0('Shot_HitEffSub', 100)
                Unknown23029(1, 211, 0)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_112_00', 3)
    sprite('Action_112_01', 3)
    sprite('Action_112_02', 3)
    sprite('Action_112_03', 3)
    sprite('Action_112_04', 3)
    sprite('Action_112_05', 3)
    sprite('Action_112_06', 3)
    ExitState()
    label(1)
    sprite('Action_112_08', 3)
    sprite('Action_112_09', 3)
    sprite('Action_112_10', 3)
    sprite('Action_112_11', 3)
    sprite('Action_112_12', 3)
    sprite('Action_112_13', 3)
    sprite('Action_112_14', 3)
    sprite('Action_112_15', 3)

@State
def Shot_HitEffSub():

    def upon_IMMEDIATE():
        Unknown2055(51)

        def upon_43():
            if (SLOT_48 == 210):
                clearUponHandler(43)
                SLOT_51 = 0
            if (SLOT_48 == 211):
                clearUponHandler(43)
                SLOT_51 = 1

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                Unknown1086(23)
            else:
                Unknown1086(22)
            Unknown1007(200000)
    sprite('null', 15)
    label(999)
    random_(2, 0, 33)
    if SLOT_ReturnVal:
        _gotolabel(2)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_111_00', 3)
    sprite('Action_111_01', 3)
    sprite('Action_111_02', 3)
    sprite('Action_111_03', 3)
    loopRest()
    gotoLabel(999)
    label(1)
    sprite('Action_111_06', 3)
    sprite('Action_111_07', 3)
    sprite('Action_111_08', 3)
    sprite('Action_111_09', 3)
    loopRest()
    gotoLabel(999)
    label(2)
    sprite('Action_111_06', 3)
    sprite('Action_111_07', 3)
    sprite('Action_111_08', 3)
    sprite('Action_111_09', 3)
    loopRest()
    gotoLabel(999)

@Subroutine
def Shot_Atk_InitParam():
    AttackLevel_(3)
    Damage(1000)
    blockstun(11)
    AttackP1(60)
    AttackP2(95)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    AirPushbackY(12000)
    AirUntechableTime(25)
    Unknown11001(0, 25, 25)
    Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown9266(16)
    Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')
    Unknown2019(-1000)
    Unknown2006()
    Unknown48('19000000020000003a000000020000000200000038000000')
    if SLOT_58:
        AttackP1(70)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(110)
        YAccel(110)
        SLOT_54 = (SLOT_54 + 1)
        if (SLOT_54 >= 3):
            SLOT_54 = 0
            GFX_0('Shot_Hasen', 100)
            GFX_0('Shot_Hasens', 100)
    loopRelated(17, 90)

    def upon_17():
        Unknown13(25)

    def upon_ON_HIT_OR_BLOCK():
        SFX_3('SE242')

    def upon_78():
        Unknown2038(1)
        GFX_0('Shot_HitEff', 104)
        Unknown23029(1, 100, 0)

    def upon_82():
        Unknown2038(1)
        GFX_0('Shot_HitEff', 104)
        Unknown23029(1, 101, 0)

    def upon_LANDING():
        clearUponHandler(2)
        clearUponHandler(53)
        Unknown23090(25)

    def upon_53():
        clearUponHandler(2)
        clearUponHandler(53)
        Unknown23090(25)

    def upon_54():
        GFX_0('Shot_AtkKoware', 100)
        Unknown13(25)

@State
def Shot_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Atk_InitParam')

        def upon_43():
            if (SLOT_48 == 208):
                Unknown11042(1)
    sprite('Action_139_00', 3)
    Unknown1111(80000, 22)
    Unknown1108(1000)
    Unknown1073(90000)
    Unknown1019(7)
    YAccel(7)
    SFX_3('SE_ShotBall')
    label(0)
    sprite('Action_139_01', 3)
    sprite('Action_139_02', 3)
    sprite('Action_139_03', 3)
    sprite('Action_139_04', 3)
    sprite('Action_139_05', 3)
    sprite('Action_139_06', 3)
    gotoLabel(0)

@State
def Shot_Hasen():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown2019(-998)
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown48('19000000020000000d00000002000000020000000d000000')
        Unknown1019(80)
        YAccel(80)

        def upon_CLEAR_OR_EXIT():
            if (not Unknown46(2)):
                clearUponHandler(3)
                Unknown1084(1)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_109_00', 6)
    sprite('Action_109_01', 6)
    sprite('Action_109_02', 15)
    sprite('Action_109_03', 1)
    ExitState()
    label(1)
    sprite('Action_109_05', 6)
    sprite('Action_109_06', 6)
    sprite('Action_109_07', 15)
    sprite('Action_109_08', 1)

@State
def Shot_Hasens():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown2019(-997)
        Unknown48('19000000020000000c00000002000000020000000c000000')
        Unknown48('19000000020000000d00000002000000020000000d000000')
        Unknown1019(80)
        YAccel(80)

        def upon_CLEAR_OR_EXIT():
            if (not Unknown46(2)):
                clearUponHandler(3)
                Unknown1084(1)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('Action_110_00', 6)
    sprite('Action_110_01', 6)
    sprite('Action_110_02', 15)
    sprite('Action_110_03', 1)
    ExitState()
    label(1)
    sprite('Action_110_05', 6)
    sprite('Action_110_06', 6)
    sprite('Action_110_07', 15)
    sprite('Action_110_08', 1)

@State
def Shot_AtkKoware():

    def upon_IMMEDIATE():
        teleportRelativeX(-50000)
        Unknown1096(500)
    sprite('Action_079_00', 5)
    sprite('Action_079_01', 5)
    sprite('Action_079_02', 5)
    sprite('Action_079_03', 5)
    sprite('Action_079_04', 5)
    sprite('Action_079_05', 5)

@State
def ShotEx_AtkMatome():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown11092(1)
        SLOT_51 = 3

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 <= 0):
                SLOT_2 = 15
                if SLOT_51:
                    GFX_0('ShotEx_Atk', 100)
                    SLOT_51 = (SLOT_51 + (-1))
                if (not SLOT_51):
                    clearUponHandler(3)
                    Unknown23029(2, 206, 0)
            Unknown2038(-1)
    sprite('null', 360)

@State
def ShotEx_Atk():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('Shot_Atk_InitParam')
        Unknown23182(2)
        Unknown30065(0)
        MinimumDamagePct(10)
    sprite('Action_139_00', 3)
    Unknown1111(80000, 22)
    Unknown1108(1000)
    Unknown1073(90000)
    Unknown1019(5)
    YAccel(5)
    SFX_3('SE_ShotBall')
    label(0)
    sprite('Action_139_01', 3)
    sprite('Action_139_02', 3)
    sprite('Action_139_03', 3)
    sprite('Action_139_04', 3)
    sprite('Action_139_05', 3)
    sprite('Action_139_06', 3)
    gotoLabel(0)

@Subroutine
def ShotCharge_Param():
    Unknown2019(-999)
    Unknown2053(1)
    Unknown23013(1)
    Unknown23022(1)
    loopRelated(17, 240)

    def upon_17():
        Unknown13(25)

    def upon_CLEAR_OR_EXIT():
        Unknown2038(1)
        if (not SLOT_51):
            if (SLOT_2 <= 10):
                Unknown1019(110)
                YAccel(110)
            else:
                SLOT_51 = 1
                SLOT_2 = 0
        elif (not SLOT_52):
            if (SLOT_2 <= 10):
                Unknown1019(90)
                YAccel(90)
            else:
                Unknown4007(0)
                Unknown23022(0)
                Unknown1084(1)
                SLOT_52 = 1
                SLOT_2 = 0
        elif (not SLOT_53):
            if (SLOT_2 >= 70):
                Unknown13(1)
                Unknown23022(1)
                if (not SLOT_57):
                    SLOT_53 = 1
                    SLOT_2 = 0
                    if (not SLOT_55):
                        SLOT_55 = 1
                        GFX_0('Shot_Atk', 100)
                        Unknown38(5, 1)
                        if SLOT_56:
                            Unknown23029(1, 208, 0)
                else:
                    SLOT_2 = 0
                    if (not SLOT_56):
                        SLOT_56 = 1
                        GFX_0('ShotEx_AtkMatome', 100)
                        Unknown38(5, 1)
        elif (SLOT_2 >= 10):
            if (not SLOT_58):
                clearUponHandler(3)
                sendToLabel(5)
            else:
                clearUponHandler(3)
                sendToLabel(15)

    def upon_43():
        if (SLOT_48 == 200):
            physicsXImpulse(6500)
            physicsYImpulse(-6000)
        if (SLOT_48 == 201):
            physicsXImpulse(4000)
            physicsYImpulse(6000)
        if (SLOT_48 == 202):
            SLOT_57 = 1
            physicsXImpulse(6000)
            physicsYImpulse(4000)
        if (SLOT_48 == 203):
            physicsXImpulse(6500)
            physicsYImpulse(-4200)
        if (SLOT_48 == 204):
            physicsXImpulse(-4500)
            physicsYImpulse(-4200)
        if (SLOT_48 == 205):
            SLOT_57 = 1
            physicsXImpulse(9000)
            physicsYImpulse(-8000)
        if (SLOT_48 == 206):
            SLOT_2 = 0
            SLOT_53 = 1
        if (SLOT_48 == 207):
            SLOT_56 = 1
            physicsXImpulse(13000)
            physicsYImpulse(6000)
            Unknown4007(3)
        if (SLOT_48 == 212):
            Unknown4007(0)
            Unknown23090(25)
    Unknown23089('0100000001000000010000000000000000000000000000000100000000000000')
    Unknown23091(1)

    def upon_53():
        Unknown23090(25)

    def upon_54():
        clearUponHandler(3)
        clearUponHandler(53)
        if (not SLOT_58):
            Unknown1084(1)
            Unknown23090(5)
            sendToLabel(3)
        else:
            Unknown1084(1)
            Unknown23090(5)
            sendToLabel(13)

@Subroutine
def ShotChargeColor():
    if (SLOT_95 == 0):
        sendToLabel(0)
    if (SLOT_95 == 1):
        SLOT_58 = 1
        sendToLabel(10)
    if (SLOT_95 == 2):
        sendToLabel(0)
    if (SLOT_95 == 3):
        SLOT_58 = 1
        sendToLabel(10)

@State
def Shot_Charge():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ShotCharge_Param')
        callSubroutine('ShotChargeColor')
    label(0)
    sprite('Action_149_00', 2)
    SFX_3('SE074_Sparking')
    sprite('Action_149_01', 2)
    GFX_0('Shot_LightEffMatome', 100)
    sprite('Action_149_02', 2)
    sprite('Action_149_03', 2)
    sprite('Action_149_04', 2)
    sprite('Action_149_05', 2)
    sprite('Action_149_06', 2)
    label(1)
    sprite('Action_149_07', 2)
    sprite('Action_149_08', 2)
    sprite('Action_149_09', 2)
    sprite('Action_149_10', 2)
    sprite('Action_149_11', 2)
    sprite('Action_149_12', 2)
    sprite('Action_149_13', 2)
    sprite('Action_149_06', 2)
    gotoLabel(1)
    label(2)
    sprite('Action_149_14', 2)
    sprite('Action_149_15', 2)
    sprite('Action_149_16', 2)
    sprite('Action_149_17', 2)
    sprite('Action_149_18', 2)
    sprite('Action_149_19', 2)
    sprite('Action_149_20', 2)
    sprite('Action_149_21', 2)
    gotoLabel(2)
    label(3)
    sprite('Action_149_22', 5)
    sprite('Action_149_23', 2)
    sprite('Action_149_24', 3)
    sprite('Action_149_25', 3)
    sprite('Action_149_26', 3)
    sprite('Action_149_27', 3)
    sprite('Action_149_28', 4)
    sprite('Action_149_29', 1)
    ExitState()
    label(5)
    sprite('Action_149_05', 2)
    sprite('Action_149_04', 2)
    sprite('Action_149_03', 2)
    sprite('Action_149_02', 2)
    sprite('Action_149_01', 2)
    sprite('Action_149_00', 2)
    ExitState()
    label(10)
    sprite('Action_150_00', 2)
    SFX_3('SE074_Sparking')
    sprite('Action_150_01', 2)
    GFX_0('Shot_LightEffMatome', 100)
    sprite('Action_150_02', 2)
    sprite('Action_150_03', 2)
    sprite('Action_150_04', 2)
    sprite('Action_150_05', 2)
    sprite('Action_150_06', 2)
    label(11)
    sprite('Action_150_07', 2)
    sprite('Action_150_08', 2)
    sprite('Action_150_09', 2)
    sprite('Action_150_10', 2)
    sprite('Action_150_11', 2)
    sprite('Action_150_12', 2)
    sprite('Action_150_13', 2)
    sprite('Action_150_06', 2)
    gotoLabel(11)
    label(12)
    sprite('Action_150_14', 2)
    sprite('Action_150_15', 2)
    sprite('Action_150_16', 2)
    sprite('Action_150_17', 2)
    sprite('Action_150_18', 2)
    sprite('Action_150_19', 2)
    sprite('Action_150_20', 2)
    sprite('Action_150_21', 2)
    gotoLabel(12)
    label(13)
    sprite('Action_150_22', 5)
    sprite('Action_150_23', 2)
    sprite('Action_150_24', 3)
    sprite('Action_150_25', 3)
    sprite('Action_150_26', 3)
    sprite('Action_150_27', 3)
    sprite('Action_150_28', 4)
    sprite('Action_150_29', 1)
    label(15)
    sprite('Action_150_05', 2)
    sprite('Action_150_04', 2)
    sprite('Action_150_03', 2)
    sprite('Action_150_02', 2)
    sprite('Action_150_01', 2)
    sprite('Action_150_00', 2)

@State
def ShotEx_Charge():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ShotCharge_Param')
        callSubroutine('ShotChargeColor')
    label(0)
    sprite('Action_143_00', 2)
    SFX_3('SE074_Sparking')
    sprite('Action_143_01', 2)
    GFX_0('Shot_LightEffMatome', 100)
    sprite('Action_143_02', 2)
    sprite('Action_143_03', 2)
    sprite('Action_143_04', 2)
    sprite('Action_143_05', 2)
    sprite('Action_143_06', 2)
    label(1)
    sprite('Action_143_07', 2)
    sprite('Action_143_08', 2)
    sprite('Action_143_09', 2)
    sprite('Action_143_10', 2)
    sprite('Action_143_11', 2)
    sprite('Action_143_12', 2)
    sprite('Action_143_13', 2)
    sprite('Action_143_06', 2)
    gotoLabel(1)
    label(2)
    sprite('Action_143_14', 2)
    sprite('Action_143_15', 2)
    sprite('Action_143_16', 2)
    sprite('Action_143_17', 2)
    sprite('Action_143_18', 2)
    sprite('Action_143_19', 2)
    sprite('Action_143_20', 2)
    sprite('Action_143_21', 2)
    gotoLabel(2)
    label(3)
    sprite('Action_143_22', 5)
    sprite('Action_143_23', 2)
    sprite('Action_143_24', 3)
    sprite('Action_143_25', 3)
    sprite('Action_143_26', 3)
    sprite('Action_143_27', 3)
    sprite('Action_143_28', 4)
    sprite('Action_143_29', 1)
    ExitState()
    label(5)
    sprite('Action_143_05', 2)
    sprite('Action_143_04', 2)
    sprite('Action_143_03', 2)
    sprite('Action_143_02', 2)
    sprite('Action_143_01', 2)
    sprite('Action_143_00', 2)
    ExitState()
    label(10)
    sprite('Action_144_00', 2)
    SFX_3('SE074_Sparking')
    sprite('Action_144_01', 2)
    GFX_0('Shot_LightEffMatome', 100)
    sprite('Action_144_02', 2)
    sprite('Action_144_03', 2)
    sprite('Action_144_04', 2)
    sprite('Action_144_05', 2)
    sprite('Action_144_06', 2)
    label(11)
    sprite('Action_144_07', 2)
    sprite('Action_144_08', 2)
    sprite('Action_144_09', 2)
    sprite('Action_144_10', 2)
    sprite('Action_144_11', 2)
    sprite('Action_144_12', 2)
    sprite('Action_144_13', 2)
    sprite('Action_144_06', 2)
    gotoLabel(11)
    label(12)
    sprite('Action_144_14', 2)
    sprite('Action_144_15', 2)
    sprite('Action_144_16', 2)
    sprite('Action_144_17', 2)
    sprite('Action_144_18', 2)
    sprite('Action_144_19', 2)
    sprite('Action_144_20', 2)
    sprite('Action_144_21', 2)
    gotoLabel(12)
    label(13)
    sprite('Action_144_22', 5)
    sprite('Action_144_23', 2)
    sprite('Action_144_24', 3)
    sprite('Action_144_25', 3)
    sprite('Action_144_26', 3)
    sprite('Action_144_27', 3)
    sprite('Action_144_28', 4)
    sprite('Action_144_29', 1)
    ExitState()
    label(15)
    sprite('Action_144_05', 2)
    sprite('Action_144_04', 2)
    sprite('Action_144_03', 2)
    sprite('Action_144_02', 2)
    sprite('Action_144_01', 2)
    sprite('Action_144_00', 2)

@State
def Shot_LightEffMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown2019(-998)
    label(0)
    sprite('null', 60)
    GFX_0('Shot_LightEff', 100)
    sprite('null', 60)
    GFX_0('Shot_LightEff', 100)
    gotoLabel(0)

@State
def Shot_LightEff():
    sprite('Action_117_00', 3)
    sprite('Action_117_01', 3)
    sprite('Action_117_02', 3)
    sprite('Action_117_03', 3)
    sprite('Action_117_04', 3)
    sprite('Action_117_05', 3)
    sprite('Action_117_06', 3)
    sprite('Action_117_07', 1)

@State
def UltimateRush_Camera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)
        Unknown2053(0)
        Unknown2034(0)
        EnableCollision(0)

        def upon_45():
            Unknown1086(22)
            teleportRelativeY(0)

        def upon_43():
            if (SLOT_48 == 1001):
                Unknown13(25)
            if (SLOT_48 == 1003):
                sendToLabel(1)
            if (SLOT_48 == 1004):
                sendToLabel(0)
        loopRelated(17, 420)

        def upon_17():
            Unknown13(25)
    label(0)
    sprite('null', 40)
    sprite('null', 32767)
    label(1)
    sprite('null', 23)

@State
def UltimateRush_AtkDmy():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(262)
        AttackP1(48)
        AttackP2(100)
        Unknown11064(1)
        Hitstop(0)
        AirUntechableTime(90)
        MinimumDamagePct(8)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11001(0, 15, 15)
        Unknown30048(1)
        Unknown9016(1)
        Unknown11023(1)
        Unknown11069('UltimateRush_AtkDmy')

        def upon_45():
            Unknown1086(22)

        def upon_43():
            if (SLOT_48 == 1002):
                Damage(100)
                Unknown30048(0)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
    sprite('null', 6)
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 10)
    RefreshMultihit()
    Unknown11069('UltimateRush_FinishShadow')
    sprite('Action_156_atk', 10)
    Unknown23029(3, 1000, 0)

@State
def UltimateRushOD_AtkDmy():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(262)
        AttackP1(48)
        AttackP2(100)
        Unknown11064(1)
        Hitstop(0)
        AirUntechableTime(90)
        MinimumDamagePct(8)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11001(0, 15, 15)
        Unknown30048(1)
        Unknown9016(1)
        Unknown11023(1)
        Unknown11069('UltimateRushOD_AtkDmy')

        def upon_45():
            Unknown1086(22)

        def upon_43():
            if (SLOT_48 == 1002):
                Damage(100)
                Unknown30048(0)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
    sprite('null', 6)
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 7)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 5)
    RefreshMultihit()
    sprite('Action_156_atk', 10)
    RefreshMultihit()
    Unknown11069('UltimateRushOD_FinishShadow')
    sprite('Action_156_atk', 10)
    Unknown23029(3, 1000, 0)

@State
def UltimateRushDDD_Zanzo1():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown23022(1)
        Unknown3026(-16777216)
    sprite('Action_045_01', 20)
    Unknown3004(-12)

@State
def UltimateRush_Shadow():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown1086(22)
        Unknown1007(-150000)
    sprite('Action_158_00', 3)
    sprite('Action_158_01', 3)
    sprite('Action_158_02', 3)
    sprite('Action_158_03', 3)
    sprite('Action_158_04', 3)
    sprite('Action_158_05', 3)
    sprite('Action_158_06', 3)
    sprite('Action_158_07', 3)
    sprite('null', 15)
    sprite('Action_159_00', 2)
    sprite('Action_159_01', 3)
    sprite('Action_159_02', 3)
    sprite('Action_159_03', 3)
    sprite('Action_159_04', 3)
    sprite('Action_159_05', 3)
    sprite('Action_159_06', 3)
    sprite('Action_159_07', 3)

@State
def UltimateRushOD_Shadow():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown1086(22)
        Unknown1096(2000)
        Unknown1007(-350000)
    sprite('Action_158_00', 3)
    sprite('Action_158_01', 3)
    sprite('Action_158_02', 3)
    sprite('Action_158_03', 3)
    sprite('Action_158_04', 3)
    sprite('Action_158_05', 3)
    sprite('Action_158_06', 3)
    sprite('Action_158_07', 3)
    sprite('Action_158_00', 3)
    sprite('Action_158_01', 3)
    sprite('Action_158_02', 3)
    sprite('Action_158_03', 3)
    sprite('Action_158_04', 3)
    sprite('Action_158_05', 3)
    sprite('Action_158_06', 3)
    sprite('Action_158_07', 3)
    sprite('Action_158_00', 3)
    sprite('Action_158_01', 3)
    sprite('Action_158_02', 3)
    sprite('Action_158_03', 3)
    sprite('Action_158_04', 3)
    sprite('Action_158_05', 3)
    sprite('Action_158_06', 3)
    sprite('Action_158_07', 3)
    sprite('Action_158_00', 3)
    sprite('Action_158_01', 3)
    sprite('Action_158_02', 3)
    sprite('Action_158_03', 3)
    sprite('Action_158_04', 3)
    sprite('Action_158_05', 3)
    sprite('Action_158_06', 3)
    sprite('Action_158_07', 3)
    sprite('null', 15)
    Unknown1096(1500)
    Unknown1086(22)
    sprite('Action_159_00', 2)
    sprite('Action_159_01', 3)
    sprite('Action_159_02', 3)
    sprite('Action_159_03', 3)
    sprite('Action_159_04', 3)
    sprite('Action_159_05', 3)
    sprite('Action_159_06', 3)
    sprite('Action_159_07', 3)

@State
def UltimateRush_FinishShadow():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2608)
        MinimumDamagePct(24)
        AttackP1(48)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(90)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown11064(0)
        Unknown30048(1)
        Unknown4009(3)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown2005()
        Unknown3026(-16777216)
        Unknown11069('UltimateRush_Exe2')

        def upon_43():
            if (SLOT_48 == 1002):
                Damage(500)
                Unknown30048(0)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11069('UltimateRushDDD_Exe')
    sprite('Action_160_00', 5)
    RefreshMultihit()
    sprite('Action_160_01', 5)
    sprite('Action_160_02', 5)
    sprite('Action_160_03', 5)
    sprite('Action_160_04', 5)
    Unknown3004(-20)
    sprite('Action_160_05', 5)
    sprite('Action_160_06', 5)
    sprite('Action_160_07', 13)
    Unknown3004(-60)

@State
def UltimateRushOD_FinishShadow():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(5)
        Damage(3258)
        MinimumDamagePct(24)
        AttackP1(48)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(90)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown11064(0)
        Unknown30048(1)
        Unknown4009(3)
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown2005()
        Unknown3026(-16777216)
        Unknown11069('UltimateRushOD_Exe2')

        def upon_43():
            if (SLOT_48 == 1002):
                Damage(500)
                Unknown30048(0)
                MinimumDamagePct(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11069('UltimateRushDDDOD_Exe')
    sprite('Action_160_00', 5)
    RefreshMultihit()
    sprite('Action_160_01', 5)
    sprite('Action_160_02', 5)
    sprite('Action_160_03', 5)
    sprite('Action_160_04', 5)
    Unknown3004(-20)
    sprite('Action_160_05', 5)
    sprite('Action_160_06', 5)
    sprite('Action_160_07', 13)
    Unknown3004(-60)

@State
def UltimateThrow_Camera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)

        def upon_CLEAR_OR_EXIT():
            Unknown1086(22)
            Unknown1007(250000)
    sprite('null', 300)

@State
def UltimateThrow_PauseShadow():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown2019(500)
    sprite('Action_167_00', 16)
    sprite('Action_167_01', 10)
    sprite('Action_167_02', 5)
    sprite('Action_167_03', 3)
    sprite('Action_167_04', 1)

@State
def UltimateThrow_MirrorShadow1():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(2, 1)
        Unknown4009(3)
        Unknown2005()
        Unknown3026(-16777216)
        Unknown3004(-10)
    sprite('Action_245_11', 1)
    physicsXImpulse(-18000)
    physicsYImpulse(16000)
    setGravity(4500)
    sprite('Action_145_00', 2)
    sprite('Action_145_01', 2)
    sprite('Action_145_02', 2)
    GFX_0('Shot_Zanzo', 0)
    physicsXImpulse(-9000)
    Unknown1043()
    sprite('Action_145_03', 2)
    GFX_0('UltimateThrowOD_Shot_Charge', 0)
    Unknown23029(1, 1015, 0)
    sprite('Action_145_04', 4)
    Recovery()
    sprite('Action_145_05', 6)
    sprite('Action_145_06', 8)
    label(0)
    sprite('Action_245_16', 3)
    sprite('Action_245_17', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)
    Unknown1084(1)
    sprite('Action_245_19', 5)
    sprite('Action_245_20', 4)

@State
def UltimateThrow_MirrorShadow2():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(2, 1)
        Unknown4009(3)
        Unknown2005()
        Unknown3026(-16777216)
        Unknown3004(-10)

        def upon_43():
            if (SLOT_48 == 1010):
                Unknown2038(1)
    sprite('Action_245_11', 1)
    physicsXImpulse(-18000)
    physicsYImpulse(16000)
    setGravity(4500)
    sprite('Action_145_00', 2)
    sprite('Action_145_01', 2)
    sprite('Action_145_02', 2)
    GFX_0('Shot_Zanzo', 0)
    physicsXImpulse(-9000)
    Unknown1043()
    sprite('Action_145_03', 2)
    GFX_0('UltimateThrowOD_Shot_Charge', 0)
    Unknown23029(1, 1016, 0)
    sprite('Action_145_04', 4)
    Recovery()
    sprite('Action_145_05', 6)
    sprite('Action_145_06', 8)
    label(0)
    sprite('Action_245_16', 3)
    sprite('Action_245_17', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)
    Unknown1084(1)
    sprite('Action_245_19', 5)
    sprite('Action_245_20', 4)

@State
def UltimateThrow_MirrorShadow3():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(2, 1)
        Unknown4009(3)
        Unknown2005()
        Unknown3026(-16777216)
        Unknown3004(-10)
    sprite('Action_245_11', 1)
    physicsXImpulse(-18000)
    physicsYImpulse(16000)
    setGravity(4500)
    sprite('Action_145_00', 2)
    sprite('Action_145_01', 2)
    sprite('Action_145_02', 2)
    GFX_0('Shot_Zanzo', 0)
    physicsXImpulse(-9000)
    Unknown1043()
    sprite('Action_145_03', 2)
    GFX_0('UltimateThrowOD_Shot_Charge', 0)
    Unknown38(5, 1)
    Unknown23029(5, 1017, 0)
    Unknown23029(5, 1011, 0)
    sprite('Action_145_04', 4)
    Recovery()
    sprite('Action_145_05', 6)
    sprite('Action_145_06', 8)
    label(0)
    sprite('Action_245_16', 3)
    sprite('Action_245_17', 3)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)
    Unknown1084(1)
    sprite('Action_245_19', 5)
    sprite('Action_245_20', 4)

@State
def UltimateThrowOD_Shot_Charge():

    def upon_IMMEDIATE():
        Unknown2010()
        callSubroutine('ShotChargeColor')

        def upon_CLEAR_OR_EXIT():
            Unknown2038(1)
            if (not SLOT_51):
                if (SLOT_2 <= 10):
                    Unknown1019(110)
                    YAccel(110)
                else:
                    SLOT_51 = 1
                    SLOT_2 = 0
            elif (not SLOT_52):
                if (SLOT_2 <= 10):
                    Unknown1019(90)
                    YAccel(90)
                else:
                    Unknown1084(1)
                    clearUponHandler(3)

        def upon_43():
            if (SLOT_48 == 1015):
                SLOT_57 = 1
                physicsXImpulse(7000)
                physicsYImpulse(2000)
            if (SLOT_48 == 1016):
                SLOT_57 = 1
                physicsXImpulse(16000)
                physicsYImpulse(-500)
            if (SLOT_48 == 1017):
                SLOT_57 = 1
                physicsXImpulse(4500)
                physicsYImpulse(3500)
            if (SLOT_48 == 206):
                if (not SLOT_58):
                    sendToLabel(5)
                else:
                    sendToLabel(15)
            if (SLOT_48 == 1011):
                SLOT_54 = 1
        loopRelated(17, 45)

        def upon_17():
            clearUponHandler(17)
            GFX_0('UltimateThrowOD_Shot_AtkMatome', 100)
            if SLOT_IsInOverdrive2:
                Unknown23029(1, 1013, 0)
        Unknown23022(1)
    label(0)
    sprite('Action_143_00', 2)
    SFX_3('SE074_Sparking')
    sprite('Action_143_01', 2)
    GFX_0('Shot_LightEffMatome', 100)
    sprite('Action_143_02', 2)
    sprite('Action_143_03', 2)
    sprite('Action_143_04', 2)
    sprite('Action_143_05', 2)
    sprite('Action_143_06', 2)
    label(1)
    sprite('Action_143_07', 2)
    sprite('Action_143_08', 2)
    sprite('Action_143_09', 2)
    sprite('Action_143_10', 2)
    sprite('Action_143_11', 2)
    sprite('Action_143_12', 2)
    sprite('Action_143_13', 2)
    sprite('Action_143_06', 2)
    gotoLabel(1)
    label(2)
    sprite('Action_143_14', 2)
    sprite('Action_143_15', 2)
    sprite('Action_143_16', 2)
    sprite('Action_143_17', 2)
    sprite('Action_143_18', 2)
    sprite('Action_143_19', 2)
    sprite('Action_143_20', 2)
    sprite('Action_143_21', 2)
    gotoLabel(2)
    label(3)
    sprite('Action_143_22', 5)
    sprite('Action_143_23', 2)
    sprite('Action_143_24', 3)
    sprite('Action_143_25', 3)
    sprite('Action_143_26', 3)
    sprite('Action_143_27', 3)
    sprite('Action_143_28', 4)
    sprite('Action_143_29', 1)
    ExitState()
    label(5)
    sprite('Action_143_05', 2)
    sprite('Action_143_04', 2)
    sprite('Action_143_03', 2)
    sprite('Action_143_02', 2)
    sprite('Action_143_01', 2)
    sprite('Action_143_00', 2)
    ExitState()
    label(10)
    sprite('Action_144_00', 2)
    SFX_3('SE074_Sparking')
    sprite('Action_144_01', 2)
    GFX_0('Shot_LightEffMatome', 100)
    sprite('Action_144_02', 2)
    sprite('Action_144_03', 2)
    sprite('Action_144_04', 2)
    sprite('Action_144_05', 2)
    sprite('Action_144_06', 2)
    label(11)
    sprite('Action_144_07', 2)
    sprite('Action_144_08', 2)
    sprite('Action_144_09', 2)
    sprite('Action_144_10', 2)
    sprite('Action_144_11', 2)
    sprite('Action_144_12', 2)
    sprite('Action_144_13', 2)
    sprite('Action_144_06', 2)
    gotoLabel(11)
    label(12)
    sprite('Action_144_14', 2)
    sprite('Action_144_15', 2)
    sprite('Action_144_16', 2)
    sprite('Action_144_17', 2)
    sprite('Action_144_18', 2)
    sprite('Action_144_19', 2)
    sprite('Action_144_20', 2)
    sprite('Action_144_21', 2)
    gotoLabel(12)
    label(13)
    sprite('Action_144_22', 5)
    sprite('Action_144_23', 2)
    sprite('Action_144_24', 3)
    sprite('Action_144_25', 3)
    sprite('Action_144_26', 3)
    sprite('Action_144_27', 3)
    sprite('Action_144_28', 4)
    sprite('Action_144_29', 1)
    ExitState()
    label(15)
    sprite('Action_144_05', 2)
    sprite('Action_144_04', 2)
    sprite('Action_144_03', 2)
    sprite('Action_144_02', 2)
    sprite('Action_144_01', 2)
    sprite('Action_144_00', 2)

@State
def UltimateThrowOD_Shot_AtkMatome():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown11092(1)
        SLOT_51 = 3

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 <= 3):
                SLOT_2 = 15
                if SLOT_51:
                    GFX_0('UltimateThrowOD_Shot', 100)
                    SLOT_51 = (SLOT_51 + (-1))
                if (not SLOT_51):
                    if SLOT_58:
                        Unknown23029(1, 1014, 0)
                    clearUponHandler(3)
                    Unknown23029(2, 206, 0)
            Unknown2038(-1)

        def upon_43():
            if (SLOT_48 == 1013):
                SLOT_58 = 1
    sprite('null', 360)

@State
def UltimateThrowOD_Shot():

    def upon_IMMEDIATE():
        Unknown2011()
        callSubroutine('Shot_Atk_InitParam')
        Unknown23056('')
        Unknown13024(0)
        Unknown11064(1)
        Unknown23182(2)
        Damage(300)
        AttackP1(50)
        AttackP2(100)
        AirUntechableTime(100)
        MinimumDamagePct(10)
        Unknown11069('UltimateThrowOD_Shot')

        def upon_43():
            if (SLOT_48 == 1014):
                Unknown11069('UltimateThrow_FinishAtkDmy')
    sprite('Action_139_00', 3)
    Unknown1111(80000, 22)
    Unknown1108(1000)
    Unknown1073(90000)
    Unknown1019(5)
    YAccel(5)
    label(0)
    sprite('Action_139_01', 3)
    sprite('Action_139_02', 3)
    sprite('Action_139_03', 3)
    sprite('Action_139_04', 3)
    sprite('Action_139_05', 3)
    sprite('Action_139_06', 3)
    gotoLabel(0)

@State
def UltimateThrow_FinishBlade():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown2005()
        Unknown23015(1)
        Unknown1096(2500)
        Unknown1072(180000)
        Unknown1086(22)
        Unknown23033(50)
    sprite('Action_419_00', 4)
    GFX_0('UltimateThrow_FinishAtkDmy', 100)
    sprite('Action_419_01', 4)
    sprite('Action_419_02', 8)
    sprite('Action_419_03', 4)
    Unknown1100(-300)
    sprite('Action_419_06', 12)

@State
def UltimateThrow_FinishAtkDmy():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        AttackLevel_(4)
        Damage(7500)
        MinimumDamagePct(20)
        AttackP1(50)
        AttackP2(100)
        AirPushbackX(0)
        AirPushbackY(-185000)
        YImpluseBeforeWallbounce(0)
        Hitstop(0)
        AirUntechableTime(100)
        Unknown9310(20)
        PushbackX(0)
        Unknown9016(1)
        Unknown11023(1)
        Unknown9190(1)
        Unknown9118(2)
        Unknown11056(3)
        Unknown1086(22)
    sprite('Action_156_atk', 2)
    StartMultihit()
    sprite('Action_156_atk', 6)
    RefreshMultihit()
    SFX_3('SE_BigBomb')

@State
def AstralStartCamera():

    def upon_IMMEDIATE():
        Unknown23032(50)
        Unknown20000(1)
    sprite('null', 30)

@State
def AstralExeCamera():

    def upon_IMMEDIATE():
        Unknown20000(1)
        Unknown20003(1)
        Unknown2053(0)
        EnableCollision(0)
        Unknown2034(0)
        Unknown1086(22)

        def upon_43():
            if (SLOT_48 == 5001):
                sendToLabel(1)
    label(0)
    sprite('null', 32767)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_105 <= 1300):
            SLOT_105 = (SLOT_105 + 3)
        else:
            Unknown1084(1)
            SLOT_105 = 1300
            clearUponHandler(3)
    label(1)
    sprite('null', 32767)
    clearUponHandler(3)
    Unknown1000(0)
    Unknown23029(3, 5002, 0)
    Unknown20009(1150)
    Unknown26('AstralBlade_First')
    Unknown26('AstralBlade')

@State
def AstralBlade_First():

    def upon_IMMEDIATE():
        Unknown1072(105000)
        Unknown1007(250000)

        def upon_43():
            (SLOT_48 == 5000)
            Unknown2038(1)
    sprite('Action_419_00', 4)
    sprite('Action_419_01', 4)
    sprite('Action_419_02', 4)
    sprite('Action_419_03', 4)
    label(0)
    sprite('Action_419_04', 4)
    sprite('Action_419_05', 4)
    if SLOT_2:
        _gotolabel(0)
    label(1)
    sprite('Action_419_06', 4)

@State
def AstralBlade_Matome():

    def upon_IMMEDIATE():
        Unknown2012()
        AttackLevel_(4)
        Damage(500)
        MinimumDamagePct(100)
        Hitstop(0)
        AirUntechableTime(100)
        PushbackX(0)
        Unknown11001(0, 40, 40)
        Unknown11064(1)
        Unknown9016(1)
        Unknown11023(1)
        Unknown1086(22)
    sprite('Action_156_atk', 45)
    StartMultihit()
    sprite('Action_156_atk', 15)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(230000)
    Unknown23032(52)
    Unknown23033(100)
    Unknown35()
    sprite('Action_156_atk', 15)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(1510000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 15)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(1900000)
    Unknown23032(0)
    Unknown23033(40)
    Unknown35()
    sprite('Action_156_atk', 15)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(320000)
    Unknown23032(65)
    Unknown23033(50)
    Unknown35()
    sprite('Action_156_atk', 12)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(1750000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 12)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(1740000)
    Unknown23032(30)
    Unknown23033(40)
    Unknown35()
    sprite('Action_156_atk', 12)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(1515000)
    Unknown23032(3)
    Unknown23033(90)
    Unknown35()
    sprite('Action_156_atk', 12)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(750000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 12)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(210000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 8)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(650000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 8)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(260000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 8)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(750000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 8)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(210000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 8)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(650000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 6)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(260000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 6)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(600000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 6)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(310000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 6)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(800000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(260000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(700000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(310000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(310000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(1650000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(1260000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 4)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(600000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 2)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(700000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 2)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(20000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 2)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(80000)
    Unknown23032(65)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 2)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(10000)
    Unknown23032(45)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 2)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(80000)
    Unknown23032(25)
    Unknown23033(30)
    Unknown35()
    sprite('Action_156_atk', 2)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown1072(100000)
    Unknown23032(10)
    Unknown23033(15)
    Unknown35()
    sprite('Action_156_atk', 17)
    RefreshMultihit()
    GFX_0('AstralBlade', 100)
    Unknown36(1)
    Unknown2005()
    Unknown1072(160000)
    Unknown23032(3)
    Unknown23033(107)
    Unknown35()
    sprite('Action_156_atk', 3)
    RefreshMultihit()
    GFX_0('AstralLastBlade', 100)
    Unknown36(1)
    Unknown23032(60)
    Unknown23033(50)
    Unknown35()
    sprite('Action_156_atk', 30)
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    hitstun(999)

@State
def AstralBlade():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown23015(1)
    sprite('Action_419_00', 4)
    sprite('Action_419_01', 4)
    sprite('Action_419_02', 4)
    sprite('Action_419_03', 4)
    label(0)
    sprite('Action_419_04', 4)
    sprite('Action_419_05', 4)
    gotoLabel(0)
    label(1)
    sprite('Action_419_06', 4)

@State
def AstralLastBlade():

    def upon_IMMEDIATE():
        Unknown2005()
        Unknown23015(4)
        Unknown1096(1500)
    sprite('Action_421_00', 4)
    sprite('Action_421_01', 4)
    sprite('Action_421_02', 4)
    sprite('Action_421_03', 30)
    Unknown1096(8000)
    Unknown21015('41737472616c45786543616d65726100000000000000000000000000000000008913000000000000')

@State
def AstralFinishCutIn():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown2019(-1000)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        Unknown3026(-16777216)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_426_00', 1)
    Unknown3001(0)
    Unknown36(22)
    Unknown1084(1)
    Unknown3026(-16777216)
    Unknown3038(1)
    Unknown3001(0)
    Unknown35()
    sprite('Action_426_00', 5)
    Unknown3004(30)
    Unknown36(22)
    Unknown3004(9)
    Unknown35()
    sprite('Action_426_01', 15)
    Unknown3025(-1, 15)
    sprite('Action_426_01', 15)
    physicsXImpulse(-12000)
    Unknown1028(300)
    Unknown36(22)
    Unknown3038(0)
    Unknown1000(10)
    physicsXImpulse(-18000)
    Unknown1028(-450)
    Unknown35()
    sprite('Action_426_02', 21)
    sprite('Action_426_02', 28)
    Unknown1084(1)
    Unknown36(22)
    Unknown1084(1)
    Unknown35()
    sprite('Action_426_03', 7)
    sprite('Action_426_04', 7)
    sprite('Action_426_05', 30)
    GFX_0('AstralFinishAtk', 100)
    sprite('Action_426_06', 45)
    Unknown3025(-16777216, 90)

    def upon_CLEAR_OR_EXIT():
        Unknown36(22)
        Unknown3026(-16777216)
        Unknown35()
    sprite('Action_426_06', 45)
    GFX_0('AstWhiteOut', 100)
    sprite('Action_426_07', 1)
    clearUponHandler(3)
    sprite('Action_426_07', 1)

@State
def AstralFinishAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Damage(25500)
        MinimumDamagePct(100)
        Unknown11064(3)
        Hitstop(0)
        Unknown11001(0, 0, 0)
        Unknown9130(16)
        Unknown9142(100)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        PushbackX(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(1)
        Unknown11086(1)
        Unknown23151(22, 103)

        def upon_45():
            Unknown2038(1)
            if (SLOT_2 >= 3):
                SLOT_2 = 0
                Unknown36(22)
                Unknown51(1)
                Unknown3026(-16777216)
                Unknown35()
            else:
                Unknown36(22)
                Unknown51(0)
                Unknown3026(-16777216)
                Unknown35()
    sprite('Action_423_00', 4)
    SFX_3('SE_BigBomb')
    sprite('Action_423_01', 4)
    sprite('Action_423_02', 4)
    sprite('Action_423_03', 4)
    sprite('Action_423_04', 4)

@State
def AstWhiteOut():

    def upon_IMMEDIATE():
        Unknown23015(4)
        Unknown3033()
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 15)
    Unknown3004(20)
    sprite('vr_white', 40)
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 50)
    Unknown23029(3, 5003, 0)
    Unknown36(22)
    Unknown3025(-1, 1)
    Unknown35()
    sprite('vr_white', 60)
    Unknown3004(-5)

@State
def AstralBG():

    def upon_IMMEDIATE():
        Unknown23015(2)
        Unknown2007()
        Unknown6001(1)
        Unknown1000(-640000)
        teleportRelativeY(-320000)
    sprite('Action_422_00', 4)
    sprite('Action_422_01', 4)
    sprite('Action_422_02', 4)
    sprite('Action_422_03', 4)
    sprite('Action_422_04', 32767)
    sprite('Action_422_05', 4)

@State
def AstralStartCutIn():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown2019(-4000)
        Unknown23015(5)
        Unknown6001(1)
        Unknown1000(625000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-655000)
    sprite('Action_999_01', 2)
    sprite('Action_999_02', 2)
    sprite('Action_999_03', 3)
    sprite('Action_999_04', 2)
    sprite('Action_999_05', 4)
    sprite('Action_999_06', 3)
    sprite('Action_999_07', 3)
    sprite('Action_999_08', 2)
    sprite('Action_999_09', 3)
    sprite('Action_999_10', 4)
    sprite('Action_999_11', 6)
    sprite('Action_999_12', 3)
    sprite('Action_999_13', 10)
    sprite('Action_999_14', 3)
    teleportRelativeX(50000)
    sprite('Action_999_15', 3)
    sprite('Action_999_16', 3)
    sprite('Action_999_17', 3)
    sprite('Action_999_18', 3)
    physicsXImpulse(65000)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(100)

@State
def Win_Knife():

    def upon_IMMEDIATE():

        def upon_CLEAR_OR_EXIT():
            Unknown1065(-21)
            Unknown2038(1)
            if (SLOT_2 >= 4):
                Unknown2037(0)
                SFX_3('SE041')
    sprite('Action_097_00', 1)
    Unknown1074(-4500)
    sprite('Action_097_01', 1)
    sprite('Action_097_02', 1)
    sprite('Action_097_03', 1)
    Unknown23144('0300000000000000000000000000000000000000000000000000000000000000320000000000000014000000')
    sprite('Action_097_04', 1)
    sprite('Action_097_06', 1)
    sprite('Action_097_07', 1)
    sprite('Action_097_08', 1)
    sprite('Action_097_09', 1)
    sprite('Action_097_10', 1)
    Unknown23144('0300000000000000000000000000000000000000000000000000000000000000320000000000000014000000')
    sprite('Action_097_11', 1)
    sprite('Action_097_13', 1)
    sprite('Action_097_14', 1)
    sprite('Action_097_15', 1)
    sprite('Action_097_16', 1)
    sprite('Action_097_17', 1)
    sprite('Action_097_18', 1)
    Unknown23144('0300000000000000000000000000000000000000000000000000000000000000320000000000000014000000')
    sprite('Action_097_19', 1)
    sprite('Action_097_21', 1)
    Unknown1074(4500)
    sprite('Action_097_22', 1)
    sprite('Action_097_23', 1)
    sprite('Action_097_24', 1)
    sprite('Action_097_25', 1)
    sprite('Action_097_26', 1)
    sprite('Action_097_27', 1)
    Unknown23144('0300000000000000000000000000000000000000000000000000000000000000320000000000000014000000')
    sprite('Action_097_28', 1)
    sprite('Action_097_30', 1)
    sprite('Action_097_31', 1)
    sprite('Action_097_32', 1)
    sprite('Action_097_33', 1)
    sprite('Action_097_34', 1)
    sprite('Action_097_35', 1)
    sprite('Action_097_36', 1)
    Unknown23144('0300000000000000000000000000000000000000000000000000000000000000320000000000000014000000')
    sprite('Action_097_37', 1)
    sprite('Action_097_39', 1)
    sprite('Action_097_40', 1)
    sprite('Action_097_41', 1)
    Unknown1074(0)
    clearUponHandler(3)
    sprite('Action_097_42', 1)
    sprite('Action_097_43', 1)
    sprite('Action_097_44', 1)
    sprite('Action_097_45', 1)
    sprite('Action_097_46', 1)

@State
def Win_Knife_Equip():
    sprite('Action_104_00', 4)
    SFX_3('')
    sprite('Action_104_01', 4)
    sprite('Action_104_02', 4)
    sprite('Action_104_03', 4)