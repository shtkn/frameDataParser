@State
def EMB():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(300000)
        Unknown1096(1100)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f4a422e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
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
    sprite('null', 80)

@State
def EMB_OD():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown1096(1250)
        Unknown2054(1)
        Unknown3038(1)
        Unknown4003('65665f656d625f4a422e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
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
    sprite('null', 80)

@State
def EMB_JB_AH():

    def upon_IMMEDIATE():
        Unknown2007()
        Unknown1007(240000)
        Unknown1096(1250)
        Unknown2054(1)
        Unknown4003('65665f656d625f4a422e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
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
    sprite('null', 80)

@State
def jb611_Tail():

    def upon_IMMEDIATE():
        Unknown4010(3)
    sprite('jb611_00s', 8)
    sprite('jb611_01s', 8)
    sprite('jb611_02s', 8)
    label(0)
    sprite('jb611_03s', 10)
    sprite('jb611_04s', 10)
    sprite('jb611_05s', 10)
    sprite('jb611_06s', 10)
    loopRest()
    gotoLabel(0)

@Subroutine
def zanzou():
    Unknown3053(1)
    Unknown3040(2)
    Unknown3042(240)
    Unknown3043(241)
    Unknown3041(242)
    Unknown3044(0)

@Subroutine
def zanzou2():
    Unknown3053(1)
    Unknown3040(2)
    Unknown3042(240)
    Unknown3043(241)
    Unknown3041(242)
    Unknown3044(1)

@State
def jbef202_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
        teleportRelativeX(-88000)
    sprite('vrefjb202_00', 3)
    sprite('vrefjb202_01', 4)

@State
def jbef202_zanzou_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(-88000)
        callSubroutine('zanzou')
    sprite('vrefjb202_10', 3)
    sprite('vrefjb202_11', 4)

@State
def jbef232_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb232_00', 6)
    sprite('vrefjb232_01', 4)

@State
def jbef212_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb212_00', 10)
    teleportRelativeX(64000)

@State
def jbef235_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(-38000)
        callSubroutine('zanzou')
    sprite('vrefjb235_00', 3)
    sprite('vrefjb235_01', 3)
    Unknown4007(0)

@State
def jbef235_zanzou_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(-199000)
        Unknown3053(1)
        callSubroutine('zanzou')
    sprite('vrefjb235_10', 2)
    teleportRelativeX(192000)
    sprite('vrefjb235_10', 8)
    Unknown4007(0)

@State
def jbef252_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb252_00', 2)
    sprite('vrefjb252_01', 4)
    sprite('vrefjb252_01', 4)
    Unknown4007(0)

@State
def jbef252_zanzou_2nd():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb252_10', 2)
    sprite('vrefjb252_10', 4)
    sprite('vrefjb252_10', 4)
    Unknown4007(0)

@State
def jbef255_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb255_00', 2)
    sprite('vrefjb255_01', 3)
    sprite('vrefjb255_01', 4)
    Unknown4007(0)

@State
def jbef340_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb340_00', 3)
    teleportRelativeX(128000)
    sprite('vrefjb340_01', 7)

@State
def jbef210_atemi():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4019(2)
        Unknown4061(1)
        Unknown3033()
        Unknown2019(100)
    sprite('vrefjb210_00', 3)
    GFX_0('jbef_210_bloom', 0)
    Unknown3007(0)
    Unknown3001(0)
    Unknown3004(85)
    sprite('keep', 1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('keep', 23)
    Unknown3004(-10)

@State
def jbef211_atemi():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4019(2)
        Unknown4061(1)
        Unknown3033()
        Unknown2019(100)
    sprite('vrefjb211_00', 3)
    GFX_0('jbef_210_bloom', 0)
    Unknown3007(0)
    Unknown3001(0)
    Unknown3004(85)
    sprite('keep', 1)
    Unknown3001(255)
    Unknown3004(0)
    sprite('keep', 23)
    Unknown3004(-10)

@State
def jbef_210_bloom():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        GFX_2('jbef_210bloom')
    sprite('null', 30)

@State
def jbef311_claw():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(90000)
        Unknown2019(100)
    sprite('vrefjb311_00', 10)
    sprite('vrefjb311_01', 10)
    Unknown3004(-25)

@State
def jbef_DashSmoke():

    def upon_IMMEDIATE():
        pass
    sprite('null', 15)
    GFX_1('jbef_403smoke', 100)

@State
def jbef_claw_pt():

    def upon_IMMEDIATE():
        Unknown4007(2)
        GFX_2('jbef_claw')
    sprite('null', 3)
    sprite('null', 60)
    Unknown4007(0)

@State
def jbef400_slash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(-40000)
    sprite('vrefjb400_00', 2)
    GFX_0('jbef_claw_pt', 0)
    sprite('vrefjb400_00', 4)
    Unknown4007(0)
    sprite('vrefjb400_01', 12)
    Unknown3004(-21)

@State
def jbef400_slash2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1073(3000)
    sprite('vrefjb400_10', 2)
    GFX_1('jbef_claw_pt', 0)
    sprite('vrefjb400_10', 4)
    Unknown4007(0)
    sprite('vrefjb400_11', 12)
    Unknown3004(-21)

@State
def jbef401_slash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1007(96000)
        teleportRelativeX(-32000)
        Unknown1064(1050)
        Unknown1056(1200)
    sprite('vrefjb401_00', 2)
    sprite('vrefjb401_00', 4)
    Unknown4007(0)
    sprite('vrefjb401_01', 12)
    Unknown3004(-21)

@State
def jbef402_slash():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4061(1)
        Unknown3033()
        teleportRelativeX(100000)
        Unknown1007(-10000)
        GFX_0('jbef402_slash2', 100)
    sprite('vrefjb402_00', 2)
    sprite('vrefjb402_00', 4)
    Unknown4007(0)
    sprite('vrefjb402_01', 12)
    Unknown3004(-21)

@State
def jbef402_slash2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4061(1)
        Unknown3033()
    sprite('vrefjb402_10', 2)
    sprite('vrefjb402_10', 4)
    Unknown4007(0)
    sprite('vrefjb402_11', 12)
    Unknown3004(-21)

@State
def jbef403_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou2')
    sprite('vrefjb403_00', 3)
    sprite('vrefjb403_01', 10)

@State
def jbef403_zanzou2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou2')
    sprite('vrefjb403_10', 3)
    sprite('vrefjb403_11', 10)

@State
def jbef404_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb404_00', 4)
    sprite('vrefjb404_01', 10)
    Unknown4007(0)

@State
def jbef404_zanzou_air():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb404_00ex', 3)
    sprite('vrefjb404_01ex', 10)
    Unknown4007(0)

@State
def jbef405_loop():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
    sprite('null', 32767)
    GFX_0('jbef405_loop_swords', 100)
    GFX_0('jbef405_loop_claws', 100)

@State
def jbef405_loop_swords():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
    label(0)
    sprite('null', 3)
    GFX_0('jbef405_loop_sword', 100)
    SFX_0('010_swing_sword_0')
    sprite('null', 3)
    GFX_0('jbef405_loop_sword2', 100)
    SFX_0('010_swing_sword_0')
    sprite('null', 3)
    GFX_0('jbef405_loop_sword3', 100)
    SFX_0('010_swing_sword_0')
    sprite('null', 3)
    GFX_0('jbef405_loop_sword4', 100)
    SFX_0('010_swing_sword_0')
    gotoLabel(0)

@State
def jbef405_loop_claws():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown1007(9000)
    label(0)
    sprite('null', 4)
    GFX_0('jbef405_loop_claw', 100)
    SFX_3('jbse_02')
    sprite('null', 4)
    GFX_0('jbef405_loop_claw2', 100)
    sprite('null', 4)
    GFX_0('jbef405_loop_claw3', 100)
    SFX_3('jbse_02')
    sprite('null', 4)
    GFX_0('jbef405_loop_claw4', 100)
    gotoLabel(0)

@State
def jbef405_loop_sword():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
        teleportRelativeX(40000)
    sprite('vrefjb405_00', 3)
    sprite('vrefjb405_01', 3)

@State
def jbef405_loop_sword2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_10', 3)
    sprite('vrefjb405_11', 3)

@State
def jbef405_loop_sword3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_20', 3)
    sprite('vrefjb405_21', 3)

@State
def jbef405_loop_sword4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_30', 3)
    sprite('vrefjb405_31', 3)

@State
def jbef405_loop_claw():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1072(-15000)
        Unknown1056(1050)
        Unknown1064(1250)
        teleportRelativeX(-80000)
        Unknown1007(200000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_loop_claw2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown2019(100)
        Unknown1072(45000)
        Unknown1056(800)
        Unknown1064(1200)
        teleportRelativeX(48000)
        Unknown1007(224000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_loop_claw3():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1072(120000)
        Unknown1056(800)
        Unknown1064(1200)
        teleportRelativeX(-48000)
        Unknown1007(80000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_loop_claw4():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        Unknown1072(65000)
        Unknown1056(700)
        Unknown1064(1050)
        teleportRelativeX(192000)
        Unknown1007(64000)
    sprite('vrefjb405_40', 2)
    sprite('vrefjb405_41', 2)
    sprite('vrefjb405_42', 2)

@State
def jbef405_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4010(3)
        Unknown4009(3)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb405_80', 3)
    sprite('vrefjb405_81', 10)

@State
def jbef406_zanzou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb406_00', 6)

@State
def jbef406_zanzou2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou')
    sprite('vrefjb406_10', 6)

@State
def jbef600_manto():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4061(0)
        Unknown3032()
        Unknown13044(1)
        Unknown2019(100)
    sprite('efjb600_00', 3)
    teleportRelativeX(80000)
    Unknown1007(-128000)
    physicsXImpulse(-30000)
    physicsYImpulse(8000)
    sprite('efjb600_00', 60)

@State
def __5DStartEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('6a6265665f6d61726b65724d6f766500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        Unknown1007(150000)

        def upon_43():
            if (SLOT_48 == 2030):
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 32767)
    Unknown1059(40)
    GFX_0('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    Unknown4011(0)
    Unknown4007(0)
    Unknown3004(-42)

@State
def AIR5DStartEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('6a6265665f6d61726b65724d6f766500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        Unknown1072(60000)

        def upon_43():
            if (SLOT_48 == 2530):
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 32767)
    Unknown1059(40)
    GFX_0('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    Unknown4011(0)
    Unknown4007(0)
    Unknown3004(-42)

@State
def AIR6DStartEff():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4011(3)
        Unknown4007(2)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('6a6265665f6d61726b65724d6f766500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        Unknown1007(100000)
        Unknown1072(30000)
    sprite('null', 32767)
    Unknown1059(40)
    GFX_0('MAKERMoveEffSumi', 100)
    label(0)
    sprite('null', 6)
    Unknown4011(0)
    Unknown4007(0)
    Unknown3004(-42)

@State
def Drive_AddAtk():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2009()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(100)
        AttackP2(85)
        AirPushbackX(30000)
        AirPushbackY(-60000)
        PushbackX(19800)
        Unknown9202(20)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11057(700)
        Unknown11050('040000006a6265665f6472697665736c6173685f73756d69000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 2031):
                Unknown11044(1)
                Unknown30088(1)
    sprite('null', 25)
    sprite('Drive_Atk', 3)
    Unknown23151(22, 103)
    RefreshMultihit()

@State
def jbef_DriveHit():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f4472697665536c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('jbef_driveslash_speed')
        Unknown1072(10000)
        Unknown1086(22)
        Unknown1007(180000)
        Unknown1065(200)
        Unknown23015(11)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 20)
    GFX_1('jbef_driveslash_sumi', -1)
    sprite('null', 58)
    Unknown1099(10)
    Unknown4003('6a6265665f4472697665536c617368456e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def jbef_Air5DHit():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f4472697665536c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('jbef_driveslash_speed')
        Unknown23015(11)
        Unknown1072(60000)
        Unknown1086(22)
        teleportRelativeX(-50000)
        Unknown1007(120000)
        Unknown1065(200)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 20)
    Unknown4048(80000)
    Unknown4045('6a6265665f6472697665736c6173685f73756d69000000000000000000000000ffffffff')
    sprite('null', 58)
    Unknown1099(10)
    Unknown4003('6a6265665f4472697665536c617368456e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def jbef_Air6DHit():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f4472697665536c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('jbef_driveslash_speed')
        Unknown23015(11)
        Unknown1072(30000)
        Unknown1086(22)
        teleportRelativeX(-50000)
        Unknown1007(170000)
        Unknown1065(200)
        Unknown21010(1)
        Unknown2054(1)
    sprite('null', 20)
    Unknown4048(80000)
    Unknown4045('6a6265665f6472697665736c6173685f73756d69000000000000000000000000ffffffff')
    sprite('null', 58)
    Unknown1099(10)
    Unknown4003('6a6265665f4472697665536c617368456e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def DriveAtk_AtkVector():
    if (SLOT_12 >= 90000):
        AirPushbackX(60000)
    elif (SLOT_12 > 0):
        AirPushbackX(30000)
    elif (SLOT_12 == 0):
        AirPushbackX(0)
    elif (SLOT_12 < 0):
        AirPushbackX(-30000)
    elif (SLOT_12 <= (-90000)):
        AirPushbackX(-60000)
    if (SLOT_13 >= 90000):
        AirPushbackY(60000)
    elif (SLOT_13 > 0):
        AirPushbackY(30000)
    elif (SLOT_13 == 0):
        AirPushbackY(0)
    elif (SLOT_13 < 0):
        AirPushbackY(-30000)
    elif (SLOT_13 <= (-90000)):
        AirPushbackY(-60000)

@Subroutine
def DriveAtk():
    AttackLevel_(4)
    Damage(800)
    AttackP1(80)
    AttackP2(95)
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown11058('0100000000000000000000000000000000000000')
    GroundedHitstunAnimation(9)
    PushbackX(80000)
    AirUntechableTime(40)
    Unknown9202(10)
    Hitstop(0)
    Unknown11001(0, 0, 2)
    Unknown11056(0)
    Unknown9016(1)
    Unknown11072(1, 0, -110000)
    Unknown11032('400d0300c0f2fcff801a060080e5f9ff')
    Unknown11084(1)
    callSubroutine('DriveAtk_AtkVector')

@Subroutine
def DriveAtkFinish():
    AttackLevel_(4)
    Damage(800)
    AttackP1(80)
    AttackP2(95)
    Unknown11034(1)
    ProjectileDurabilityLvl(0)
    Unknown11058('0100000000000000000000000000000000000000')
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirUntechableTime(60)
    AirPushbackY(30000)
    AirPushbackX(30000)
    Unknown9215()
    Unknown9203()
    Hitstop(0)
    Unknown11001(0, 0, 5)
    Unknown11032('400d0300c0f2fcff801a060080e5f9ff')
    Unknown11056(0)
    Unknown9016(1)
    Unknown11084(1)

@Subroutine
def LeverInput():
    if CheckInput(0x45):
        SLOT_57 = 2
    if CheckInput(0x93):
        SLOT_57 = 8
    SLOT_55 = 1

@Subroutine
def CheckPosY():
    if (SLOT_57 == 2):
        Unknown1007(-200000)
    elif (SLOT_57 == 8):
        Unknown1007(200000)
    if (SLOT_23 <= 150000):
        teleportRelativeY(150000)
    elif (SLOT_23 >= 3000000):
        teleportRelativeY(3000000)

@Subroutine
def CourseSetting():
    Unknown2053(1)
    if SLOT_51:
        if 
        if SLOT_58:
            (SLOT_55 == 1)
        else:
            (SLOT_55 == 3):
            teleportRelativeX(200000)
            Unknown1007(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 2)
        else:
            (SLOT_55 == 6):
            teleportRelativeX(400000)
            Unknown1007(-400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 3)
        else:
            (SLOT_55 == 9):
            teleportRelativeX(400000)
            Unknown1007(400000)
            if (SLOT_57 == 2):
                Unknown1007(200000)
            elif (SLOT_57 == 8):
                Unknown1007(-200000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 4)
        else:
            (SLOT_55 == 12):
            teleportRelativeX(400000)
            Unknown1007(-400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if SLOT_52:
        if 
        if SLOT_58:
            (SLOT_55 == 1)
        else:
            (SLOT_55 == 3):
            teleportRelativeX(200000)
            Unknown1007(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 2)
        else:
            (SLOT_55 == 6):
            teleportRelativeX(800000)
            Unknown1007(0)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 3)
        else:
            (SLOT_55 == 9):
            teleportRelativeX(-400000)
            Unknown1007(-400000)
            if (SLOT_57 == 2):
                Unknown1007(200000)
            elif (SLOT_57 == 8):
                Unknown1007(-200000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 4)
        else:
            (SLOT_55 == 12):
            teleportRelativeX(800000)
            Unknown1007(0)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if SLOT_53:
        if 
        if SLOT_58:
            (SLOT_55 == 1)
        else:
            (SLOT_55 == 3):
            teleportRelativeX(200000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 2)
        else:
            (SLOT_55 == 6):
            teleportRelativeX(400000)
            Unknown1007(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 3)
        else:
            (SLOT_55 == 9):
            teleportRelativeX(400000)
            Unknown1007(-400000)
            if (SLOT_57 == 2):
                Unknown1007(200000)
            elif (SLOT_57 == 8):
                Unknown1007(-200000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 4)
        else:
            (SLOT_55 == 12):
            teleportRelativeX(400000)
            Unknown1007(400000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if SLOT_IsInOverdrive2:
        if 
        if SLOT_58:
            (SLOT_55 == 1)
        else:
            (SLOT_55 == 3):
            teleportRelativeX(200000)
            Unknown1007(0)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(5, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 2)
        else:
            (SLOT_55 == 6):
            teleportRelativeX(400000)
            Unknown1007(0)
            if (SLOT_57 == 2):
                teleportRelativeX(-100000)
                Unknown1007(-100000)
            elif (SLOT_57 == 8):
                teleportRelativeX(-100000)
                Unknown1007(100000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(6, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 3)
        else:
            (SLOT_55 == 9):
            teleportRelativeX(400000)
            Unknown1007(0)
            if (SLOT_57 == 2):
                teleportRelativeX(-100000)
                Unknown1007(-100000)
            elif (SLOT_57 == 8):
                teleportRelativeX(-100000)
                Unknown1007(100000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(7, 1)
        if 
        if SLOT_58:
            (SLOT_55 == 4)
        else:
            (SLOT_55 == 12):
            teleportRelativeX(400000)
            Unknown1007(0)
            if (SLOT_57 == 2):
                teleportRelativeX(-100000)
                Unknown1007(-100000)
            elif (SLOT_57 == 8):
                teleportRelativeX(-100000)
                Unknown1007(100000)
            callSubroutine('CheckPosY')
            GFX_0('Mark', 100)
            Unknown38(8, 1)
    if 
    if SLOT_58:
        (SLOT_55 == 5)
    else:
        (SLOT_55 == 13):
        clearUponHandler(3)
        sendToLabel(0)
    SLOT_55 = (SLOT_55 + 1)

@Subroutine
def DriveSpeed():
    Unknown1019(20)
    YAccel(20)
    Unknown1108(0)
    if SLOT_12:
        if SLOT_13:
            GFX_0('MAKERMoveEff', -1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')

@State
def Mark():

    def upon_IMMEDIATE():
        Unknown2053(1)
        Unknown3032()
        Unknown4003('6a6265665f6d61726b65722e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_drive_add')
        SFX_3('jbse_06')

        def upon_43():
            if (SLOT_48 == 5003):
                GFX_1('jbef_drive_move', -1)
                sendToLabel(0)
        sendToLabelUpon(44, 1)
    sprite('null', 120)
    label(0)
    sprite('null', 6)
    clearUponHandler(43)
    clearUponHandler(44)
    Unknown1087(3, 25)
    sprite('null', 6)
    Unknown1099(120)
    Unknown3004(-42)
    ExitState()
    label(1)
    sprite('null', 6)
    clearUponHandler(43)
    clearUponHandler(44)
    sprite('null', 6)
    Unknown1099(120)
    Unknown3004(-42)

@State
def MAKERMoveEff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4007(2)
        Unknown4006(2)
        Unknown1108(0)
        Unknown23013(1)
        Unknown3032()
        Unknown4003('6a6265665f6d61726b65724d6f766500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(1)
    sprite('null', 6)
    Unknown1059(-100)
    GFX_0('MAKERMoveEffSumi', 100)
    ExitState()
    label(0)
    sprite('null', 6)
    Unknown3004(-42)

@State
def MAKERMoveEffSumi():

    def upon_IMMEDIATE():
        Unknown4006(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown3038(1)
    sprite('vrefjb_markerMoveEXpoints', 1)
    Unknown4061(2)
    Unknown4045('6a6265665f64726976655f73756d69000000000000000000000000000000000000000000')
    Unknown4045('6a6265665f64726976655f73756d69000000000000000000000000000000000001000000')
    Unknown4045('6a6265665f64726976655f73756d69000000000000000000000000000000000002000000')

@State
def jbef203_zanzou():

    def upon_IMMEDIATE():
        Unknown4008(2)
        Unknown4007(2)
        Unknown4010(2)
        Unknown4009(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou2')
    sprite('vrefjb203_00', 10)

@State
def test1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown1007(-200000)
        Unknown1096(950)
        Unknown3026(-14671872)
        Unknown23022(1)
        Unknown2003(1)
    sprite('jb252_08', 15)
    Unknown3004(30)
    sprite('jb252_08', 10)
    Unknown3004(-20)

@State
def test2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown1007(-100000)
        Unknown1096(950)
        Unknown3026(-14671872)
        Unknown23022(1)
        Unknown2003(1)
    sprite('jb431_09', 15)
    Unknown3004(30)
    sprite('jb431_09', 10)
    Unknown3004(-20)

@State
def test3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown1007(-200000)
        Unknown1096(950)
        Unknown3026(-14671872)
        Unknown23022(1)
        Unknown2003(1)
    sprite('jb404_05', 15)
    Unknown3004(30)
    sprite('jb404_05', 10)
    Unknown3004(-20)

@State
def Shiranui_Hagane_236Aobj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_55:
                clearUponHandler(43)
                callSubroutine('CourseSetting')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 0
                SLOT_52 = 0
                SLOT_53 = 0
                SLOT_54 = 1
                SLOT_55 = 1
                SLOT_57 = 2
    sprite('null', 300)
    Unknown1007(150000)
    label(0)
    sprite('null', 6)
    sprite('null', 5)
    Unknown23029(3, 5001, 0)
    Unknown1086(3)
    Unknown1007(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000050000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000050000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(5, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000060000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000060000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(6, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000070000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000070000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(7, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000080000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000080000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(8, 5003, 0)
    Unknown23029(3, 5002, 0)
    Unknown1084(1)
    Unknown1086(8)

@State
def Shiranui_Hagane_236Bobj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_55:
                clearUponHandler(43)
                callSubroutine('CourseSetting')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 1
                SLOT_52 = 0
                SLOT_53 = 0
                SLOT_54 = 0
                SLOT_55 = 1
                SLOT_57 = 2
    sprite('null', 300)
    Unknown1007(150000)
    label(0)
    sprite('null', 6)
    sprite('null', 5)
    Unknown23029(3, 5001, 0)
    Unknown1086(3)
    Unknown1007(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000050000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000050000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(5, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000060000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000060000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(6, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000070000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000070000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(7, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000080000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000080000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(8, 5003, 0)
    Unknown23029(3, 5002, 0)
    Unknown1084(1)
    Unknown1086(8)

@State
def Shiranui_Hagane_236EXobj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_55:
                clearUponHandler(43)
                callSubroutine('CourseSetting')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 1
                SLOT_52 = 0
                SLOT_53 = 0
                SLOT_54 = 0
                SLOT_55 = 1
                SLOT_57 = 2
                SLOT_58 = 1
    sprite('null', 300)
    Unknown1007(150000)
    label(0)
    sprite('null', 5)
    sprite('null', 5)
    Unknown23029(3, 5001, 0)
    Unknown1086(3)
    Unknown1007(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000050000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000050000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(5, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000060000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000060000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(6, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000070000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000070000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(7, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000080000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000080000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(8, 5003, 0)
    Unknown23029(3, 5002, 0)
    Unknown1084(1)
    Unknown1086(8)

@State
def Shiranui_Hagane_214Aobj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_55:
                clearUponHandler(43)
                callSubroutine('CourseSetting')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 0
                SLOT_52 = 0
                SLOT_53 = 0
                SLOT_54 = 1
                SLOT_55 = 1
                SLOT_57 = 5
    sprite('null', 300)
    Unknown1007(150000)
    label(0)
    sprite('null', 6)
    sprite('null', 5)
    Unknown23029(3, 5001, 0)
    Unknown1086(3)
    Unknown1007(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000050000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000050000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(5, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000060000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000060000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(6, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000070000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000070000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(7, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000080000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000080000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(8, 5003, 0)
    Unknown23029(3, 5002, 0)
    Unknown1084(1)
    Unknown1086(8)

@State
def Shiranui_Hagane_214Bobj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_55:
                clearUponHandler(43)
                callSubroutine('CourseSetting')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 0
                SLOT_52 = 1
                SLOT_53 = 0
                SLOT_54 = 0
                SLOT_55 = 1
                SLOT_57 = 2
    sprite('null', 300)
    Unknown1007(150000)
    label(0)
    sprite('null', 6)
    sprite('null', 5)
    Unknown23029(3, 5001, 0)
    Unknown1086(3)
    Unknown1007(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000050000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000050000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(5, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000060000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000060000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(6, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000070000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000070000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(7, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000080000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000080000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(8, 5003, 0)
    Unknown23029(3, 5002, 0)
    Unknown1084(1)
    Unknown1086(8)

@State
def Shiranui_Hagane_214EXobj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4010(3)
        Unknown4011(3)

        def upon_CLEAR_OR_EXIT():
            if SLOT_55:
                clearUponHandler(43)
                callSubroutine('CourseSetting')

        def upon_43():
            if (SLOT_48 == 5000):
                SLOT_51 = 0
                SLOT_52 = 1
                SLOT_53 = 0
                SLOT_54 = 0
                SLOT_55 = 1
                SLOT_57 = 2
                SLOT_58 = 1
    sprite('null', 300)
    Unknown1007(150000)
    label(0)
    sprite('null', 5)
    sprite('null', 5)
    Unknown23029(3, 5001, 0)
    Unknown1086(3)
    Unknown1007(150000)
    SFX_0('000_airdash_0')
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000050000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000050000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(5, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(5)
    SFX_0('002_highjump_0')
    GFX_0('test1', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000060000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000060000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(6, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(6)
    SFX_0('001_airbackdash_0')
    GFX_0('test2', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000070000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000070000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtk')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(7, 5003, 0)
    Unknown1084(1)
    Unknown48('03000000020000000c00000019000000020000000c000000')
    Unknown48('03000000020000000d00000019000000020000000d000000')
    Unknown1086(7)
    SFX_0('000_airdash_0')
    GFX_0('test3', 0)
    sprite('Drive_TameMoveAtk', 5)
    Unknown48('190000000200000038000000080000000200000016000000')
    if SLOT_38:
        Unknown47('0100000002000000160000000200000038000000020000000c000000')
    else:
        Unknown47('0100000002000000380000000200000016000000020000000c000000')
    Unknown48('190000000200000038000000080000000200000017000000')
    Unknown47('0100000002000000380000000200000017000000020000000d000000')
    callSubroutine('DriveSpeed')
    RefreshMultihit()
    callSubroutine('DriveAtkFinish')
    Unknown30065(0)
    MinimumDamagePct(10)
    SFX_3('jbse_10')
    sprite('Drive_TameMoveAtk', 5)
    Unknown23029(8, 5003, 0)
    Unknown23029(3, 5002, 0)
    Unknown1084(1)
    Unknown1086(8)

@State
def MarkingPoint():

    def upon_IMMEDIATE():
        Unknown4025(22)
        Unknown3032()
        Unknown1096(700)

        def upon_16():
            Unknown2071('1600000000000000000000006400000001000000')

        def upon_32():
            sendToLabel(0)
    sprite('null', 32767)
    Unknown3001(170)
    GFX_2('jbef_marking_hatudo')
    Unknown4003('6a6265665f6d61726b6572322e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 10)
    Unknown3004(-26)

@State
def jbeff_warp():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f7368756e73696e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2054(1)
        Unknown1096(1000)
        Unknown1007(150000)
        Unknown3001(150)
    sprite('null', 7)
    GFX_1('jbef_shunsin', -1)
    Unknown1099(350)
    sprite('null', 14)
    Unknown1099(30)

@State
def Shot_Eff():

    def upon_IMMEDIATE():
        Unknown2010()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(70)
        AttackP2(80)
        hitstun(22)
        AirUntechableTime(40)
        Unknown11042(1)
        AirPushbackY(15000)
        Unknown9017(1)
        physicsXImpulse(10000)
        physicsYImpulse(26000)
        setGravity(1600)
        Unknown1096(2000)
        Unknown2053(1)
        Unknown23089('0100000001000000010000000100000001000000000000000100000000000000')

        def upon_54():
            sendToLabel(580)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 >= 3):
                sendToLabel(0)
        Unknown23026(100000)

        def upon_5():
            Unknown2038(1)
            YAccel(-90)
            if (SLOT_13 <= 26000):
                physicsYImpulse(26000)
            Unknown8000(104, 1, 0)
            SFX_0('015_blaze_1')
    sprite('Shot_Atk', 300)
    Unknown3038(1)
    GFX_0('jbef407_Nekodama', -1)
    label(0)
    sprite('Shot_Atk', 1)
    clearUponHandler(3)
    label(580)
    sprite('null', 20)
    DisableAttackRestOfMove()
    Unknown1084(1)
    clearUponHandler(3)
    clearUponHandler(54)
    Unknown23029(1, 5010, 0)

@State
def jbef407_NekodamaRady():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        if (SLOT_95 == 1):
            Unknown4061(3)
        if (SLOT_95 == 3):
            Unknown4061(3)
        Unknown3001(170)
        Unknown1007(-50000)
    sprite('vrefjb407_00', 5)
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000000000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000001000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000002000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000003000000')
    sprite('vrefjb407_01', 5)
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000000000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000001000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000002000000')
    sprite('vrefjb407_02', 5)
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000000000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000001000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000002000000')
    sprite('vrefjb407_03', 5)
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000000000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000001000000')
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000002000000')
    sprite('vrefjb407_04', 10)
    Unknown4047(2, 2, 2)
    Unknown4045('6a6265665f3430375f6e6f6b6f7369000000000000000000000000000000000000000000')

@State
def jbef407_Nekodama():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown4061(2)
        if (SLOT_95 == 1):
            Unknown4061(3)
        if (SLOT_95 == 3):
            Unknown4061(3)
        Unknown3001(170)
        Unknown3029(1)
        Unknown3071(3)
        Unknown3070(2)

        def upon_43():
            if (SLOT_48 == 5010):
                sendToLabel(1)
    sprite('vrefjb407_10', 1)
    Unknown4049(800)
    Unknown4048(-30000)
    Unknown4045('6a6265665f3430375f73686f636b000000000000000000000000000000000000ffffffff')
    SFX_0('015_blaze_0')
    label(0)
    sprite('vrefjb407_10', 3)
    Unknown1073(45000)
    Unknown4047(2, 2, 2)
    Unknown4049(1500)
    Unknown4045('6a6265665f3430375f6e6f6b6f73690000000000000000000000000000000000ffffffff')
    sprite('vrefjb407_10', 3)
    Unknown1073(45000)
    gotoLabel(0)
    label(1)
    sprite('vrefjb407_20', 2)
    Unknown3029(0)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    Unknown4047(2, 2, 2)
    Unknown4049(2000)
    Unknown4045('6a6265665f3430375f6e6f6b6f73690000000000000000000000000000000000ffffffff')
    GFX_0('jbef407_NekodamaAura', -1)
    sprite('vrefjb407_21', 2)
    sprite('vrefjb407_22', 2)
    sprite('vrefjb407_23', 2)
    sprite('vrefjb407_24', 2)
    loopRest()

@State
def jbef407_NekodamaAura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown1096(1500)
        Unknown1074(1500)
        Unknown4061(2)
        if SLOT_95:
            Unknown4061(3)
        Unknown21004(2)
        Unknown4003('6a6265665f3430374175726130300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 30)
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    Unknown3004(-8)
    Unknown1099(15)
    loopRest()

@State
def jbef408_DashEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown4007(2)
        GFX_2('jbef_408_dash')
        sendToLabelUpon(32, 0)
    sprite('null', 32767)
    label(0)
    sprite('null', 8)
    Unknown3004(-31)
    loopRest()

@State
def jb430_slashMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)
        teleportRelativeY(0)
        Unknown3032()
    sprite('null', 3)
    GFX_0('jb430_slash1', 100)
    SFX_0('012_stab_deep')
    sprite('null', 3)
    GFX_0('jb430_slash2', 100)
    SFX_0('012_stab_deep')
    sprite('null', 3)
    GFX_0('jb430_slash3', 100)
    SFX_0('012_stab_deep')
    sprite('null', 3)
    GFX_0('jb430_slashAdd', 100)
    GFX_0('jb430_slash4', 100)
    GFX_1('jbef_430_suminokosi', 100)
    SFX_0('012_stab_deep')
    sprite('null', 15)
    sprite('null', 58)
    Unknown4010(0)
    Unknown21015('6a623433305f736c617368416464000000000000000000000000000000000000cd10000000000000')
    GFX_0('jb430_slashEnd', 100)
    Unknown26('jb430_slash1')
    Unknown26('jb430_slash2')
    Unknown26('jb430_slash3')
    Unknown26('jb430_slash4')

@State
def jb430_slashEnd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown21004(1)
        teleportRelativeY(0)
        Unknown2054(1)
    sprite('null', 58)
    Unknown4003('6a6265665f34333066616c6c736c617368456e640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown26('jb430_slash1')
    Unknown26('jb430_slash2')
    Unknown26('jb430_slash3')
    Unknown26('jb430_slash4')
    Unknown1067(7)

@State
def jb430_slashAdd():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown21004(1)
        teleportRelativeY(0)
        Unknown1007(-20000)
        Unknown1057(400)

        def upon_43():
            if (SLOT_48 == 4301):
                clearUponHandler(43)
                sendToLabel(0)
        Unknown23015(12)
    sprite('null', 32767)
    Unknown4003('6a6265665f3433306261636c6b617572613030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('null', 10)
    Unknown2054(1)
    Unknown1059(20)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb430_slash1():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('6a6265665f34333066616c6c736c6173683030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeY(0)
        Unknown4061(2)
        Unknown21004(1)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_slash2():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('6a6265665f34333066616c6c736c6173683031000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeY(0)
        Unknown4061(2)
        Unknown21004(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_slash3():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('6a6265665f34333066616c6c736c6173683032000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeY(0)
        Unknown4061(2)
        Unknown21004(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_slash4():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('6a6265665f34333066616c6c736c6173683033000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeY(0)
        Unknown4061(2)
        Unknown21004(1)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 32767)

@State
def jb430_ODSlash00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        teleportRelativeY(0)
        Unknown4061(2)
        Unknown21004(1)
        Unknown1096(800)
    sprite('null', 4)
    Unknown4003('6a6265665f3433304f445f736c617368303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    GFX_0('jb430_ODSlash00BG', 100)
    sprite('null', 4)
    Unknown4003('6a6265665f3433304f445f736c617368303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 10)
    Unknown4003('6a6265665f3433304f445f736c617368303200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    ScreenShake(10000, 10000)
    Unknown1099(5)
    physicsYImpulse(-1250)
    sprite('null', 58)
    Unknown4003('6a6265665f3433304f445f736c6173683032456e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4010(0)

@State
def jb430_ODSlash00BG():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        teleportRelativeY(0)
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
    sprite('null', 18)
    sprite('null', 58)
    Unknown3004(-4)
    Unknown4010(0)

@State
def jb431_SlashEndEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        Unknown1007(200000)
        Unknown4061(2)
        Unknown21004(1)
    sprite('null', 6)
    GFX_2('jbef_431crossAdd')
    Unknown4003('6a6265665f34333063726f737330302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(2)
    Unknown1057(100)
    Unknown1099(100)
    SFX_3('jbse_09')
    sprite('null', 20)
    Unknown1099(1)
    sprite('null', 27)
    ScreenShake(10000, 10000)
    GFX_1('jbef_431slashEnd', -1)
    Unknown4003('6a6265665f343330736c61736830302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(0)
    Unknown1097(400)
    SFX_0('025_cleanhit_slash')
    sprite('null', 15)
    sprite('null', 15)
    Unknown3004(-17)

@State
def jb431_SlashEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown1086(22)
        teleportRelativeY(0)
        Unknown1007(200000)
        Unknown23067('jbef_431slash')
    sprite('null', 15)
    GFX_0('jb431_SlashBloomEff', 100)

@State
def jb431_SlashBloomEff():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431slashBloom')
    sprite('null', 15)

@State
def jb431_CircleShockEff():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown1096(2000)
    sprite('null', 15)
    Unknown4003('6a6265665f343330636972636c6530302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(40)

@State
def jb431OD_SlashEffMatome():

    def upon_IMMEDIATE():
        Unknown4010(2)

        def upon_43():
            if (SLOT_48 == 4310):
                clearUponHandler(43)
                sendToLabel(0)
    sprite('null', 4)
    GFX_0('jb431OD_SlashEff00', -1)
    sprite('null', 4)
    GFX_0('jb431OD_SlashEff01', -1)
    sprite('null', 32767)
    GFX_0('jb431OD_SlashEff02', -1)
    label(0)
    sprite('null', 4)
    Unknown21015('6a623433314f445f536c61736845666630300000000000000000000000000000d710000000000000')
    sprite('null', 4)
    Unknown21015('6a623433314f445f536c61736845666630310000000000000000000000000000d810000000000000')
    sprite('null', 1)
    Unknown21015('6a623433314f445f536c61736845666630320000000000000000000000000000d910000000000000')

@State
def jb431OD_SlashEff00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown1007(200000)
        Unknown4061(2)
        Unknown21004(1)
        teleportRelativeX(-1000000)
        Unknown1096(1000)
        Unknown4003('6a6265665f3433304f44736c61736830302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')

        def upon_43():
            if (SLOT_48 == 4311):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('null', 5)
    Unknown3001(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('jb431OD_jubei00', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    Unknown4010(0)
    Unknown4003('6a6265665f3433304f44736c6173683030456e642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(5)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb431OD_SlashEff01():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown1007(200000)
        Unknown4061(2)
        Unknown21004(1)
        teleportRelativeX(-700000)
        Unknown1096(800)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
        Unknown4003('6a6265665f3433304f44736c61736830312e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 4312):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('null', 5)
    Unknown3001(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('jb431OD_jubei01', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    Unknown4010(0)
    Unknown4003('6a6265665f3433304f44736c6173683031456e642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(5)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb431OD_SlashEff02():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown1007(200000)
        Unknown4061(2)
        Unknown21004(1)
        teleportRelativeX(-300000)
        Unknown1096(800)
        Unknown4047(1, 1, 1)
        Unknown23067('jbef_431od_slashadd')
        Unknown4003('6a6265665f3433304f44736c61736830322e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_43():
            if (SLOT_48 == 4313):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('null', 5)
    Unknown3001(0)
    ScreenShake(2500, 2500)
    sprite('null', 5)
    Unknown3004(51)
    GFX_0('jb431OD_jubei02', 100)
    sprite('null', 32767)
    label(1)
    sprite('null', 28)
    Unknown4010(0)
    Unknown4003('6a6265665f3433304f44736c6173683032456e642e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(5)
    sprite('null', 30)
    Unknown3004(-8)

@State
def jb431OD_jubei00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown1007(-100000)
        Unknown23015(1)
    sprite('jb201_03', 10)
    SFX_3('jbse_09')
    SFX_0('000_airdash_0')
    sprite('jb201_03', 10)
    Unknown3004(-26)
    physicsXImpulse(3000)

@State
def jb431OD_jubei01():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown1007(-100000)
        Unknown23015(1)
    sprite('jb211_06', 10)
    SFX_3('jbse_02')
    sprite('jb211_06', 10)
    Unknown3004(-26)
    physicsXImpulse(3000)

@State
def jb431OD_jubei02():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4010(2)
        Unknown1007(-100000)
        Unknown23015(1)
    sprite('jb400_03', 10)
    physicsXImpulse(3000)
    SFX_0('000_airdash_0')
    sprite('jb400_03', 10)
    Unknown3004(-26)
    physicsXImpulse(3000)

@State
def jb432_eyerayEff():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4061(2)
        Unknown2054(2)
    sprite('vrefjb432_00', 6)
    sprite('vrefjb432_01', 6)
    sprite('vrefjb432_02', 6)
    sprite('vrefjb432_03', 6)
    Unknown4045('6a6265665f343332627566665f68617475646f0000000000000000000000000064000000')

@State
def jb432_BodyAuraEff():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('6a6265665f3433324175726130302e44494700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(250000)
        Unknown1096(900)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(25)
    GFX_1('jbef_432_shock', 100)
    GFX_0('jb432_BodyAuraEffCore', 100)
    sprite('null', 10)
    sprite('null', 20)
    Unknown3004(-12)
    sprite('null', 20)
    sprite('null', 20)
    Unknown3004(-12)

@State
def jb432_BodyAuraEffCore():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown2054(2)
        Unknown4010(2)
        Unknown4007(2)
        Unknown4003('6a6265665f34333241757261436f72652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(400)
        Unknown1007(-50000)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(25)
    sprite('null', 10)
    sprite('null', 20)
    Unknown3004(-12)

@State
def jb440_startAtk00():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown4009(2)
        Unknown3032()
        Unknown4061(2)
        Unknown21004(1)
        Unknown4003('6a6265665f343430737461727441746b303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(400)
        Unknown1007(300000)
        teleportRelativeX(150000)
    sprite('null', 3)
    Unknown1057(150)
    Unknown1065(45)
    sprite('null', 3)
    Unknown1057(300)
    Unknown1065(75)
    sprite('null', 3)
    Unknown1057(300)
    Unknown1065(75)
    sprite('null', 3)
    Unknown1057(150)
    Unknown1065(37)
    sprite('null', 3)
    Unknown4003('6a6265665f343430737461727441746b303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4010(0)
    Unknown4007(0)
    Unknown4009(0)
    Unknown1099(5)
    sprite('null', 56)
    Unknown1065(75)
    Unknown4003('6a6265665f343430737461727441746b3031656e6400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown3004(-4)

@State
def jb440_slash00():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4061(2)
        Unknown21004(1)
        Unknown4003('6a6265665f343430736c61736830302e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(400)
        Unknown1007(300000)
        teleportRelativeX(200000)
    sprite('null', 10)
    Unknown3001(0)
    Unknown3004(26)
    Unknown21010(1)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown4045('6a6265665f34343073756d696e6f6b6f7369000000000000000000000000000064000000')
    sprite('null', 5)
    Unknown21010(0)
    sprite('null', 57)
    Unknown4003('6a6265665f343430736c6173683030456e642e444947000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1099(2)

@State
def jb440_AddAtk():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown1096(500)
        teleportRelativeX(50000)
    sprite('null', 4)
    GFX_0('jb440_AddAtk00', 100)
    Unknown21010(1)
    sprite('null', 4)
    GFX_0('jb440_AddAtk01', 100)
    sprite('null', 10)
    Unknown1099(3)
    physicsYImpulse(-2500)
    physicsXImpulse(-1500)
    Unknown4061(2)
    Unknown4047(1, 1, 1)
    Unknown4045('6a6265665f34343073756d696e6f6b6f7369320000000000000000000000000064000000')
    Unknown21004(1)
    Unknown4003('6a6265665f34343041646441746b30322e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21010(0)
    sprite('null', 57)
    Unknown4003('6a6265665f34343041646441746b3032456e642e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown4010(0)

@State
def jb440_AddAtk00():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown21004(1)
        Unknown4003('6a6265665f34343041646441746b30302e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(500)
    sprite('null', 4)
    sprite('null', 5)
    Unknown3001(128)
    Unknown3004(-25)

@State
def jb440_AddAtk01():

    def upon_IMMEDIATE():
        Unknown21010(1)
        Unknown4010(2)
        Unknown3032()
        Unknown4061(2)
        Unknown21004(1)
        Unknown4003('6a6265665f34343041646441746b30312e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(500)
    sprite('null', 4)
    sprite('null', 5)
    Unknown3001(128)
    Unknown3004(-25)

@State
def jb430_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown1056(600)
        Unknown1064(6000)
    sprite('null', 30)

@State
def jb430_EffOD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown1056(1000)
        Unknown1064(10000)
    sprite('null', 30)

@State
def jb430_BunshinA():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        Unknown23022(1)
    sprite('jb430_04', 12)
    physicsXImpulse(25000)
    Unknown3004(-21)

@State
def jb430_BunshinB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        Unknown23022(1)
    sprite('jb430_04', 12)
    physicsXImpulse(-25000)
    Unknown3004(-21)

@State
def jb431_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown1056(6000)
        Unknown1064(600)
    sprite('null', 30)
    GFX_2('ef_ukemi')

@State
def jb431_EffOD():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown1064(600)
        Unknown1062(1000, 5000)
        Unknown1077(10000, 60000)
    sprite('null', 3)
    GFX_2('ef_ukemi')

@State
def jb431_BunshinA():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        Unknown23022(1)
    sprite('jb431_01', 12)
    physicsXImpulse(25000)
    Unknown3004(-21)

@State
def jb431_BunshinB():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown3029(1)
        Unknown3069(2)
        Unknown23022(1)
    sprite('jb431_01', 12)
    physicsXImpulse(-25000)
    Unknown3004(-21)

@State
def UltimateChage_Atk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(1500)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(17)
        AirPushbackX(-1000)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(1800)
        Unknown9130(51)
        Unknown9142(41)
        PushbackX(8000)
        AirUntechableTime(60)
        StarterRating(2)
        Unknown1096(1200)
    sprite('Chage_Atk', 3)

@State
def UltimateChageEX_Atk():

    def upon_IMMEDIATE():
        Unknown2011()
        AttackLevel_(5)
        Damage(1500)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(40000)
        AirPushbackY(30000)
        PushbackX(8000)
        AirUntechableTime(60)
        StarterRating(2)
        Unknown1096(1200)
    sprite('Chage_Atk', 3)

@State
def jb432_Eff():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown2054(1)
        Unknown1096(1500)
        Unknown23151(3, 103)
    sprite('null', 30)
    GFX_2('ef_ukemi')

@State
def ChageAuraGenerator():

    def upon_IMMEDIATE():

        def upon_CLEAR_OR_EXIT():
            SLOT_51 = (SLOT_51 + 1)
            if (not op(4, 2, 51, 0, 30)):
                SLOT_52 = 0
                Unknown48('19000000020000003400000002000000020000001e000000')
                if (not SLOT_52):
                    Unknown36(3)
                    GFX_0('ChageAura', 103)
                    Unknown35()
    sprite('null', 32767)

@State
def ChageAura():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4025(3)
        Unknown4011(3)
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1000)
    sprite('null', 30)
    GFX_2('jbef_432_buffNml')

@State
def ChageAura2():

    def upon_IMMEDIATE():
        Unknown4007(3)
        Unknown4025(3)
        Unknown4011(3)
        Unknown3032()
        Unknown2054(1)
        Unknown1096(1000)
    sprite('null', 30)
    GFX_2('jbef_432_buff2')

@State
def BurstDD_Camera():

    def upon_IMMEDIATE():

        def upon_32():
            sendToLabel(580)
        teleportRelativeX(350000)
    sprite('null', 3000)
    Unknown20000(1)
    Unknown20011('1900000019000000')
    label(580)
    sprite('null', 1)
    Unknown20000(0)
    Unknown20011('0000000000000000')

@State
def Astral_Camera():

    def upon_IMMEDIATE():
        Unknown4022(3)
        teleportRelativeX(300000)

        def upon_43():
            if (SLOT_48 == 5000):
                sendToLabel(0)
            if (SLOT_48 == 5001):
                sendToLabel(1)
            if (SLOT_48 == 5002):
                sendToLabel(2)
            if (SLOT_48 == 5003):
                sendToLabel(3)
            if (SLOT_48 == 5004):
                sendToLabel(4)
            if (SLOT_48 == 5005):
                sendToLabel(5)
            if (SLOT_48 == 5006):
                sendToLabel(6)
    sprite('null', 32767)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20004(1)
    Unknown20006(1)
    label(0)
    sprite('null', 32767)
    Unknown20009(800)
    teleportRelativeX(300000)
    label(1)
    sprite('null', 32767)
    Unknown20009(1000)
    teleportRelativeX(-300000)
    label(2)
    sprite('null', 32767)
    Unknown4022(0)
    physicsXImpulse(50000)
    label(3)
    sprite('null', 32767)
    physicsXImpulse(0)
    teleportRelativeX(-300000)
    label(4)
    sprite('null', 32767)
    Unknown4007(22)
    label(5)
    sprite('null', 32767)
    Unknown4007(0)
    label(6)
    sprite('null', 110)
    Unknown1000(700000)
    teleportRelativeY(1000000)
    sprite('null', 20)
    physicsXImpulse(-34000)
    physicsYImpulse(-36000)
    sprite('null', 32767)
    Unknown1084(1)

@State
def jb450_ZanEff():

    def upon_IMMEDIATE():
        Unknown4006(2)
    sprite('null', 6)
    SFX_0('006_swing_blade_1')
    SFX_0('010_swing_sword_2')

@State
def jb450_AtkAura():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown4007(2)
        Unknown3032()
        Unknown4003('6a6265665f34353061746b6175726130300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        GFX_2('jbef_450_underlight')

        def upon_43():
            if (SLOT_48 == 5011):
                sendToLabel(0)
    sprite('null', 10)
    Unknown3001(0)
    GFX_0('jb450_AtkAura2', -1)
    SFX_0('016_explode_0')
    sprite('null', 10)
    Unknown3004(13)
    SFX_0('016_explode_0')
    sprite('null', 32767)
    GFX_0('jb450_AtkAura2', -1)
    label(0)
    sprite('null', 20)
    Unknown1099(15)
    Unknown3004(-12)

@State
def jb450_AtkAura2():

    def upon_IMMEDIATE():
        Unknown3033()
        Unknown4003('6a6265665f34353061746b6175726130310000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(500)
    sprite('null', 39)

@State
def jb450_kaihouAura():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4007(2)
        Unknown4003('6a6265665f3435306b6169686f617572613030000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1200)
        Unknown1065(300)
    sprite('null', 8)
    ScreenShake(10000, 10000)
    GFX_0('jb450_kaihouShock', -1)
    sprite('null', 1)
    sprite('null', 230)
    sprite('null', 15)
    Unknown3004(-17)
    Unknown4007(0)

@State
def jb450_kaihouShock():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        Unknown4003('6a6265665f3435306b6169686f73686f636b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1300)
        Unknown1089(300)
    sprite('null', 10)
    GFX_1('jbef_450shockbrust', -1)
    Unknown1059(30)
    sprite('null', 10)
    Unknown3004(-26)
    Unknown1059(10)

@State
def jb450_kidou():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou2')
        Unknown3029(1)
        Unknown3001(180)
    sprite('vrefjb450_00kidou', 8)
    sprite('vrefjb450_01kidou', 16)

@State
def jb450_kidou2():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown4061(1)
        Unknown3033()
        callSubroutine('zanzou2')
        Unknown3029(1)
        Unknown3001(180)
    sprite('vrefjb450_02kidou', 8)
    sprite('vrefjb450_03kidou', 24)

@State
def jbef_450flash():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown3032()
        GFX_2('jbef_450flash')
    sprite('null', 30)

@State
def jbef_450weakpointBG():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        Unknown4003('6a6265665f3433307765616b706f696e744247000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(1800)
        Unknown1086(22)
        Unknown1007(174000)
        teleportRelativeX(-10000)

        def upon_43():
            if (SLOT_48 == 5012):
                sendToLabel(0)
    sprite('null', 32767)
    label(0)
    sprite('null', 20)
    Unknown1099(120)
    Unknown3004(-12)
    loopRest()

@State
def jbef_450weakpoint():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        GFX_2('jbef_450weakpoint')
        Unknown23151(22, 109)
        Unknown4007(22)

        def upon_43():
            if (SLOT_48 == 5012):
                sendToLabel(0)
    sprite('null', 20)
    Unknown3001(0)
    Unknown1096(10)
    sprite('null', 10)
    Unknown3001(255)
    Unknown1099(100)
    sprite('null', 32767)
    Unknown1099(0)
    label(0)
    sprite('null', 10)
    Unknown1099(-80)
    loopRest()

@State
def jbef_450weakpoint_Terumi():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        Unknown2005()
        Unknown4061(4)
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('6a6265665f343530746572756d690000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(25000)

        def upon_43():
            if (SLOT_48 == 5012):
                sendToLabel(0)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 40)
    Unknown3004(8)
    physicsXImpulse(-100)
    physicsYImpulse(100)
    sprite('null', 32767)
    physicsXImpulse(-50)
    physicsYImpulse(25)
    Unknown3004(0)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def jbef_450weakpoint_Hazama():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown3032()
        Unknown2005()
        Unknown4061(4)
        Unknown1086(22)
        Unknown4007(22)
        Unknown4003('6a6265665f343530746572756d690000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1007(25000)

        def upon_43():
            if (SLOT_48 == 5012):
                sendToLabel(0)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 40)
    Unknown3004(2)
    physicsXImpulse(-100)
    physicsYImpulse(100)
    sprite('null', 32767)
    physicsXImpulse(-50)
    physicsYImpulse(25)
    Unknown3004(-6)
    label(0)
    sprite('null', 10)
    Unknown3004(-26)
    loopRest()

@State
def jb450_BG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f3435307761736962670000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown1064(800)
        Unknown1088(1000)
        Unknown1056(1000)
        Unknown1007(80000)
        Unknown3001(240)
    sprite('null', 150)
    GFX_0('jb450_BGsub', -1)
    sprite('null', 9)
    Unknown3004(-26)

@State
def jb450_BGsub():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f34353066696c6d67617465000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(1)
        Unknown1064(800)
        Unknown1088(1000)
        Unknown1056(1000)
    sprite('null', 150)
    sprite('null', 9)
    Unknown3004(-26)

@State
def jbef_450ZanzoNokosiMato():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown4007(2)
        teleportRelativeY(0)
    sprite('null', 3)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    teleportRelativeX(-400000)
    Unknown35()
    sprite('null', 3)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    teleportRelativeX(-300000)
    Unknown35()
    sprite('null', 3)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown35()
    sprite('null', 60)
    GFX_0('jbef_450ZanzoNokosi', -1)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown35()

@State
def jbef_450ZanzoNokosi():

    def upon_IMMEDIATE():
        Unknown20003(1)
        Unknown4007(2)
        Unknown23015(11)
        teleportRelativeY(0)
    sprite('jb450_26', 50)
    Unknown3004(-5)

@State
def jb450_RedBG():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown20003(1)
        Unknown20004(1)
        Unknown4003('6a6265665f3435307265646267000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
    sprite('null', 30)
    Unknown3001(0)
    sprite('null', 55)
    Unknown3001(255)

@State
def jb450_BG2():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f3435305f77617369626732000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown23015(2)
        Unknown1096(400)
        teleportRelativeX(-325000)
        Unknown3001(225)
        Unknown2054(1)
    sprite('null', 40)
    sprite('null', 50)
    Unknown3004(-12)
    sprite('null', 1)

@State
def jb450_BGEnd():

    def upon_IMMEDIATE():
        Unknown2054(1)
        Unknown3032()
        Unknown4003('6a6265665f3435306267656e64000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1072(-25000)
        Unknown1096(1200)
        Unknown23015(4)
        teleportRelativeX(-1300000)
    sprite('null', 115)

@State
def jb450_Slash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f343530736c617368303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(-50000)
    sprite('null', 5)
    ScreenShake(50000, 50000)
    Unknown1099(5)
    Unknown1096(800)
    sprite('null', 5)
    ScreenShake(40000, 40000)
    sprite('null', 4)
    Unknown1096(850)
    sprite('null', 4)
    Unknown1096(900)
    sprite('null', 6)
    Unknown4003('6a6265665f343530736c617368303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown1096(1100)
    sprite('null', 6)
    Unknown4003('6a6265665f343530736c617368303200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('null', 40)
    GFX_0('jb450_SlashSub', -1)
    Unknown3001(0)

@State
def jb450_SlashSub():

    def upon_IMMEDIATE():
        Unknown4010(2)
        Unknown3032()
        Unknown4003('6a6265665f343530736c617368526f74617465000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown1096(700)
        Unknown1007(1000000)
        teleportRelativeX(-1250000)
        Unknown2054(1)
        Unknown21010(1)
    sprite('null', 4)
    Unknown1073(600000)
    SFX_3('jbse_08')
    sprite('null', 4)
    Unknown1073(600000)
    sprite('null', 4)
    Unknown1073(600000)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown1097(100)
    sprite('null', 4)
    Unknown1073(600000)
    Unknown3004(-31)
    sprite('null', 4)
    Unknown1073(600000)

@State
def jb610_Slash():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('6a6265665f363130736c617368303000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        teleportRelativeX(100000)
        Unknown1007(75000)
        Unknown1096(1500)
    sprite('null', 5)
    Unknown3001(0)
    Unknown3004(51)
    sprite('null', 20)
    sprite('null', 57)
    Unknown3004(-4)
    Unknown4003('6a6265665f363130736c617368303100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def jb900_Ase():

    def upon_IMMEDIATE():
        Unknown3032()
        GFX_2('jbef_900ase')
    sprite('null', 20)
    Unknown3001(0)
    Unknown3004(12)
    sprite('null', 32767)

@State
def jb611_Tail_Event():

    def upon_IMMEDIATE():
        Unknown2019(500)
    sprite('jb611_00s', 8)
    sprite('jb611_01s', 8)
    sprite('jb611_02s', 8)
    label(0)
    sprite('jb611_03s', 10)
    sprite('jb611_04s', 10)
    sprite('jb611_05s', 10)
    sprite('jb611_06s', 10)
    loopRest()
    gotoLabel(0)

@State
def NOISE():

    def upon_IMMEDIATE():
        Unknown3032()
        Unknown4003('65665f6576656e746e6f6973652e4449470000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown4015()
        Unknown23015(4)
        Unknown23032(50)
        Unknown23033(50)
    sprite('null', 120)
    loopRest()