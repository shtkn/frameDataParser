@State
def WalkOnpuMatome():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown4007(3)
        Unknown1000(20000)
        teleportRelativeY(350000)
    sprite('null', 10)	# 1-10
    label(0)
    sprite('null', 5)	# 11-15
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(1)
    sprite('null', 5)	# 16-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 25)	# 21-45
    GFX_0('WalkOnpuControl', 100)
    loopRest()
    gotoLabel(0)

@State
def WalkOnpuControl():

    def upon_IMMEDIATE():
        Unknown2020(-1)
        Unknown1010(-10000, 30000)
        Unknown1011(0, 90000)
        Unknown1026(3000, 6000)
        Unknown1025(3000, 6000)

        def upon_3():
            YAccel(96)
            Unknown2038(1)
            if (SLOT_2 <= 15):
                Unknown1019(105)
            else:
                Unknown1019(95)
            if (SLOT_2 >= 30):
                SLOT_2 = 0
                if (SLOT_12 <= 0):
                    Unknown1019(0)
                    Unknown1025(2000, 4000)
                else:
                    Unknown1019(0)
                    Unknown1025(-3000, -2000)
    sprite('null', 90)	# 1-90
    GFX_0('WalkOnpu', 103)
    loopRest()

@State
def WalkOnpu():

    def upon_IMMEDIATE():
        Unknown4007(2)
        Unknown2008()
    sprite('null', 1)	# 1-1
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    label(0)
    sprite('Action_076_00', 30)	# 2-31
    sprite('Action_076_01', 30)	# 32-61
    sprite('Action_076_02', 1)	# 62-62
    ExitState()
    label(1)
    sprite('Action_076_04', 30)	# 63-92
    sprite('Action_076_05', 30)	# 93-122
    sprite('Action_076_06', 1)	# 123-123

@State
def __5B_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2020(1)
    sprite('Action_095_00', 3)	# 1-3
    sprite('Action_095_01', 3)	# 4-6
    sprite('Action_095_02', 3)	# 7-9
    sprite('Action_095_03', 3)	# 10-12

@State
def __5C_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(-80000)
        Unknown1007(-35000)
    sprite('Action_081_00', 3)	# 1-3
    sprite('Action_081_01', 3)	# 4-6
    sprite('Action_081_02', 3)	# 7-9
    sprite('Action_081_03', 3)	# 10-12

@State
def __6B_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(50000)
    sprite('Action_093_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_093_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_093_02', 5)	# 11-15
    sprite('Action_093_03', 1)	# 16-16

@State
def __6A_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(50000)
    sprite('Action_092_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_092_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_092_02', 5)	# 11-15
    sprite('Action_092_03', 1)	# 16-16

@State
def __6C_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(50000)
    sprite('Action_094_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_094_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_094_02', 5)	# 11-15
    sprite('Action_094_03', 1)	# 16-16

@State
def __4C_Zanzo():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_122_00', 3)	# 1-3
    sprite('Action_122_01', 3)	# 4-6
    sprite('Action_122_02', 3)	# 7-9
    sprite('Action_122_03', 3)	# 10-12

@State
def __4B_Zanzo():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(35000)
        Unknown1007(15000)
    sprite('Action_123_00', 3)	# 1-3
    sprite('Action_123_01', 3)	# 4-6
    sprite('Action_123_02', 3)	# 7-9
    sprite('Action_123_03', 1)	# 10-10

@State
def __4BAdd_Zanzo():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_124_00', 3)	# 1-3
    sprite('Action_124_01', 3)	# 4-6
    sprite('Action_124_02', 3)	# 7-9
    sprite('Action_124_03', 1)	# 10-10

@State
def __66C_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_399_00', 3)	# 1-3
    sprite('Action_399_01', 3)	# 4-6
    sprite('Action_399_02', 3)	# 7-9
    sprite('Action_399_03', 3)	# 10-12
    sprite('Action_399_04', 3)	# 13-15

@State
def __2C_Blade_1st():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_083_00', 3)	# 1-3
    sprite('Action_083_01', 3)	# 4-6
    sprite('Action_083_02', 3)	# 7-9
    sprite('Action_083_03', 3)	# 10-12

@State
def __2C_Blade_2nd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_084_00', 3)	# 1-3
    sprite('Action_084_01', 3)	# 4-6
    sprite('Action_084_02', 3)	# 7-9
    sprite('Action_084_03', 3)	# 10-12

@State
def AIR5B_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_086_00', 5)	# 1-5
    sprite('Action_086_01', 3)	# 6-8
    sprite('Action_086_02', 3)	# 9-11
    sprite('Action_086_03', 1)	# 12-12

@State
def AIR5B_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_087_00', 3)	# 1-3
    sprite('Action_087_01', 3)	# 4-6
    sprite('Action_087_02', 3)	# 7-9

@State
def AIR2C_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_100_00', 3)	# 1-3
    sprite('Action_100_01', 3)	# 4-6
    sprite('Action_100_02', 3)	# 7-9
    sprite('Action_100_03', 3)	# 10-12

@State
def AIR2C_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        teleportRelativeX(30000)
    sprite('Action_099_00', 3)	# 1-3
    sprite('Action_099_01', 3)	# 4-6
    sprite('Action_099_02', 3)	# 7-9

@State
def AIR5C_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_105_00', 5)	# 1-5
    sprite('Action_105_01', 3)	# 6-8
    sprite('Action_105_02', 3)	# 9-11
    sprite('Action_105_03', 3)	# 12-14

@State
def AIR5C_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_106_00', 3)	# 1-3
    sprite('Action_106_01', 3)	# 4-6
    sprite('Action_106_02', 3)	# 7-9

@State
def AIR6A_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(50000)
    sprite('Action_092_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_092_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_092_02', 5)	# 11-15
    sprite('Action_092_03', 1)	# 16-16

@State
def AIR6B_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(50000)
    sprite('Action_093_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_093_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_093_02', 2)	# 5-6
    sprite('Action_093_03', 1)	# 7-7

@State
def AIR6C_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(50000)
    sprite('Action_094_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_094_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_094_02', 2)	# 5-6
    sprite('Action_094_03', 1)	# 7-7

@State
def FF_Start():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_231_00', 5)	# 1-5
    sprite('Action_231_01', 6)	# 6-11
    sprite('Action_231_02', 8)	# 12-19
    sprite('Action_231_03', 8)	# 20-27
    sprite('Action_231_04', 8)	# 28-35
    sprite('Action_231_05', 8)	# 36-43
    sprite('Action_231_06', 1)	# 44-44

@State
def FF_Sakura1():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_232_00', 10)	# 1-10
    sprite('Action_232_01', 12)	# 11-22
    sprite('Action_232_02', 13)	# 23-35
    sprite('Action_232_03', 14)	# 36-49
    sprite('Action_232_04', 15)	# 50-64
    sprite('Action_232_05', 15)	# 65-79
    sprite('Action_232_06', 15)	# 80-94

@State
def FF_Sakura2():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_233_00', 10)	# 1-10
    sprite('Action_233_01', 12)	# 11-22
    sprite('Action_233_02', 13)	# 23-35
    sprite('Action_233_03', 14)	# 36-49
    sprite('Action_233_04', 15)	# 50-64
    sprite('Action_233_05', 15)	# 65-79
    sprite('Action_233_06', 15)	# 80-94
    sprite('Action_233_07', 15)	# 95-109

@State
def FF_Sakura3():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_234_00', 10)	# 1-10
    sprite('Action_234_01', 12)	# 11-22
    sprite('Action_234_02', 13)	# 23-35
    sprite('Action_234_03', 14)	# 36-49
    sprite('Action_234_04', 15)	# 50-64
    sprite('Action_234_05', 15)	# 65-79
    sprite('Action_234_06', 15)	# 80-94
    sprite('Action_234_07', 15)	# 95-109
    sprite('Action_234_08', 15)	# 110-124
    sprite('Action_234_09', 1)	# 125-125

@State
def FF_Charge():

    def upon_IMMEDIATE():
        teleportRelativeX(-50000)
        Unknown1007(200000)
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_227_00', 3)	# 1-3
    sprite('Action_227_01', 3)	# 4-6
    sprite('Action_227_02', 3)	# 7-9
    sprite('Action_227_03', 3)	# 10-12
    sprite('Action_227_04', 3)	# 13-15

@State
def FF_Blade_1st():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_238_00', 3)	# 1-3
    sprite('Action_238_01', 3)	# 4-6
    sprite('Action_238_02', 3)	# 7-9
    sprite('Action_238_03', 3)	# 10-12
    sprite('Action_238_04', 1)	# 13-13

@State
def FF_Blade_2nd():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
    sprite('Action_239_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_239_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_239_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_239_03', 5)	# 16-20	 **attackbox here**

@State
def FF_Blade_Lv3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
    sprite('Action_242_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_242_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_242_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_242_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_242_04', 1)	# 21-21

@State
def AirFF_Blade_Lv3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(100000)
    sprite('Action_242_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_242_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_242_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_242_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_242_04', 1)	# 21-21

@State
def AirFF_Blade_1st():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown1007(100000)
    sprite('Action_238_00', 3)	# 1-3
    sprite('Action_238_01', 3)	# 4-6
    sprite('Action_238_02', 3)	# 7-9
    sprite('Action_238_03', 3)	# 10-12
    sprite('Action_238_04', 1)	# 13-13

@State
def AirFF_Blade_2nd():

    def upon_IMMEDIATE():
        teleportRelativeX(100000)
        Unknown1007(100000)
    sprite('Action_239_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_239_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_239_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_239_03', 5)	# 16-20	 **attackbox here**

@State
def AirFF_Start():

    def upon_IMMEDIATE():
        teleportRelativeX(0)
        Unknown1007(50000)
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_231_00', 5)	# 1-5
    sprite('Action_231_01', 6)	# 6-11
    sprite('Action_231_02', 8)	# 12-19
    sprite('Action_231_03', 8)	# 20-27
    sprite('Action_231_04', 8)	# 28-35
    sprite('Action_231_05', 8)	# 36-43
    sprite('Action_231_06', 1)	# 44-44

@State
def AirFF_Charge():

    def upon_IMMEDIATE():
        teleportRelativeX(-50000)
        Unknown1007(250000)
        Unknown2019(-1000)
        Unknown2054(1)
    sprite('Action_227_00', 3)	# 1-3
    sprite('Action_227_01', 3)	# 4-6
    sprite('Action_227_02', 3)	# 7-9
    sprite('Action_227_03', 3)	# 10-12
    sprite('Action_227_04', 3)	# 13-15

@State
def Yae_AirRelease():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_104_00', 3)	# 1-3
    sprite('Action_104_01', 3)	# 4-6
    sprite('Action_104_02', 3)	# 7-9
    sprite('Action_104_03', 3)	# 10-12

@State
def Yae_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(3)
        Damage(600)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(3)
        Hitstop(2)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackY(18000)
        YImpluseBeforeWallbounce(1500)
        Unknown30056('68c5ffff4600000000000000')
        Unknown30065(100)
        Unknown11108('03000000')
        Unknown9016(1)
        Unknown1007(250000)
        Unknown11044(1)

        def upon_78():
            Unknown23029(3, 1000, 1)
    sprite('Action_463_00', 5)	# 1-5	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_01', 5)	# 6-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_02', 5)	# 11-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_03', 4)	# 16-19
    Unknown23027()

@State
def AirYae_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(3)
        Damage(900)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Unknown23182(3)
        Hitstop(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackY(18000)
        YImpluseBeforeWallbounce(2000)
        Unknown30056('68c5ffff4600000000000000')
        Unknown30065(100)
        Unknown11108('03000000')
        Unknown9016(1)
        Unknown1007(250000)
        Unknown11044(1)

        def upon_78():
            Unknown23029(3, 1000, 1)
    sprite('Action_463_00', 5)	# 1-5	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_01', 5)	# 6-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_02', 5)	# 11-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_03', 4)	# 16-19
    Unknown23027()

@State
def Yae_AddAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(5)
        Damage(2000)
        Hitstop(18)
        AttackP1(100)
        AttackP2(100)
        Unknown30065(100)
        AirPushbackX(3000)
        AirPushbackY(12000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11044(1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23151(22, 103)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown23078(1)

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)
    sprite('Action_461_21_dmyatk', 3)	# 1-3

@State
def Yae_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(15000)
        Unknown1007(125000)
    sprite('Action_431_00', 5)	# 1-5
    sprite('Action_431_01', 5)	# 6-10
    sprite('Action_431_02', 1)	# 11-11

@State
def SlashA_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
    sprite('Action_097_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_097_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_097_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_097_03', 1)	# 16-16

@State
def SlashB_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
    sprite('Action_096_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_096_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_096_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_096_03', 1)	# 16-16

@State
def SlashC_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
    sprite('Action_098_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_098_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_098_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_098_03', 1)	# 16-16

@State
def SlashEx_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        Unknown1096(1400)
        teleportRelativeX(100000)
        Unknown1007(-50000)
    sprite('Action_097_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_097_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_097_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_097_03', 1)	# 16-16

@State
def AirSlashA_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(70000)
    sprite('Action_483_00', 5)	# 1-5
    sprite('Action_483_01', 5)	# 6-10
    sprite('Action_483_02', 5)	# 11-15
    sprite('Action_483_03', 1)	# 16-16

@State
def AirSlashB_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(100000)
    sprite('Action_485_00', 5)	# 1-5
    sprite('Action_485_01', 5)	# 6-10
    sprite('Action_485_02', 5)	# 11-15
    sprite('Action_485_03', 1)	# 16-16

@State
def AirSlashC_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(40000)
    sprite('Action_484_00', 5)	# 1-5
    sprite('Action_484_01', 5)	# 6-10
    sprite('Action_484_02', 5)	# 11-15
    sprite('Action_484_03', 1)	# 16-16

@State
def AirSlashEx_Blade():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        Unknown1096(1400)
        teleportRelativeX(100000)
        Unknown1007(20000)
    sprite('Action_483_00', 5)	# 1-5
    sprite('Action_483_01', 5)	# 6-10
    sprite('Action_483_02', 5)	# 11-15
    sprite('Action_483_03', 1)	# 16-16

@State
def Slash_AddAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(5)
        Damage(2000)
        Hitstop(18)
        AttackP1(100)
        AttackP2(75)
        AirPushbackX(3000)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(2500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11068(1)
        Unknown23151(22, 103)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')

        def upon_78():
            Unknown4004('6566666563745f3331370000000000000000000000000000000000000000000064000000')
            Unknown36(1)
            Unknown1096(1200)
            Unknown1079()
            Unknown23151(22, 103)
            Unknown35()

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 1100):
                Unknown30065(0)
    sprite('Action_461_21_dmyatk', 3)	# 1-3

@State
def SlashFinishSP_AtkCol():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(3)
        Damage(850)
        AttackP1(80)
        AttackP2(90)
        Unknown11092(1)
        Unknown23182(3)
        Hitstop(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(60)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(2000)
        Unknown30056('589effff4600000000000000')
        Unknown11108('03000000')
        Unknown9016(1)
        Unknown1007(150000)
        Unknown11068(1)
        Unknown11044(1)
        Unknown11069('SlashFinishSP_AtkCol')

        def upon_78():
            Unknown23029(3, 1000, 1)
    sprite('Action_463_00', 5)	# 1-5	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_01', 5)	# 6-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_463_02', 5)	# 11-15	 **attackbox here**
    RefreshMultihit()
    Unknown11069('SlashFinishSP_AddAtk')
    sprite('Action_463_03', 4)	# 16-19

@State
def SlashFinishSP_AddAtk():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(5)
        Damage(3000)
        Hitstop(18)
        AttackP1(100)
        AttackP2(80)
        AirPushbackX(3000)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(2500)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11056(3)
        Unknown11068(1)
        Unknown23151(22, 103)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)
    sprite('Action_461_21_dmyatk', 3)	# 1-3

@State
def Shukuchi_WindEff():

    def upon_IMMEDIATE():
        Unknown2019(500)
    sprite('Action_118_00', 2)	# 1-2
    sprite('Action_118_01', 2)	# 3-4
    sprite('Action_118_02', 2)	# 5-6
    sprite('Action_118_03', 1)	# 7-7

@State
def KimonoDmy():

    def upon_IMMEDIATE():
        Unknown2019(-1)
    sprite('Action_216_32', 15)	# 1-15	 **attackbox here**
    Unknown3001(0)
    Unknown3004(25)

@State
def IW_Blade1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_108_00', 3)	# 1-3
    sprite('Action_108_01', 3)	# 4-6
    sprite('Action_108_02', 3)	# 7-9

@State
def IW_Blade2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_109_00', 3)	# 1-3
    sprite('Action_109_01', 3)	# 4-6
    sprite('Action_109_02', 3)	# 7-9

@State
def IW_Blade3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown1007(200000)
    sprite('Action_213_00', 3)	# 1-3
    sprite('Action_213_01', 3)	# 4-6
    sprite('Action_213_02', 3)	# 7-9

@State
def IW_Zanzo():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_111_00', 6)	# 1-6
    sprite('Action_111_01', 6)	# 7-12
    sprite('Action_111_02', 6)	# 13-18

@State
def IW_Ralease():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
    sprite('Action_091_00', 3)	# 1-3
    sprite('Action_091_01', 3)	# 4-6
    sprite('Action_091_02', 3)	# 7-9

@State
def IW_Sakura_Matome():

    def upon_IMMEDIATE():
        Unknown1086(22)
    sprite('null', 1)	# 1-1
    sprite('null', 10)	# 2-11
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)
    GFX_0('IW_SakuraParticle', 100)

@State
def IW_SakuraParticle():

    def upon_IMMEDIATE():
        Unknown1086(22)
        sendToLabelUpon(2, 0)
        Unknown1007(200000)
        Unknown1026(-1000, -500)
        Unknown1011(-250000, 250000)
        Unknown1012(-250000, 250000)

        def upon_3():
            Unknown1025(-250, 250)
    sprite('null', 1)	# 1-1
    random_(2, 0, 25)
    if SLOT_0:
        _gotolabel(4)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(3)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(2)
    label(1)
    sprite('Action_120_00', 40)	# 2-41
    sprite('Action_120_02', 45)	# 42-86
    sprite('Action_120_03', 45)	# 87-131
    sprite('Action_120_04', 1)	# 132-132
    ExitState()
    label(2)
    sprite('Action_120_06', 40)	# 133-172
    sprite('Action_120_08', 45)	# 173-217
    sprite('Action_120_09', 45)	# 218-262
    sprite('Action_120_10', 1)	# 263-263
    ExitState()
    label(3)
    sprite('Action_120_12', 40)	# 264-303
    sprite('Action_120_14', 45)	# 304-348
    sprite('Action_120_15', 45)	# 349-393
    sprite('Action_120_16', 1)	# 394-394
    ExitState()
    label(4)
    sprite('Action_120_18', 40)	# 395-434
    sprite('Action_120_20', 45)	# 435-479
    sprite('Action_120_21', 45)	# 480-524
    sprite('Action_120_22', 1)	# 525-525
    ExitState()
    label(0)
    sprite('Action_120_04', 1)	# 526-526

@State
def IW_Sakura_MatomeFinish():

    def upon_IMMEDIATE():
        Unknown1086(22)
        Unknown1007(-650000)
    sprite('null', 1)	# 1-1
    sprite('null', 10)	# 2-11
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)
    GFX_0('IW_SakuraParticleFinish', 100)

@State
def IW_SakuraParticleFinish():

    def upon_IMMEDIATE():
        Unknown1086(22)
        sendToLabelUpon(2, 0)
        Unknown1007(-100000)
        Unknown1026(-4500, -2000)
        Unknown1011(-250000, 250000)
        Unknown1012(-250000, 250000)

        def upon_3():
            Unknown1025(-250, 250)
    sprite('null', 1)	# 1-1
    random_(2, 0, 25)
    if SLOT_0:
        _gotolabel(4)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(3)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(2)
    label(1)
    sprite('Action_120_00', 40)	# 2-41
    sprite('Action_120_02', 45)	# 42-86
    sprite('Action_120_03', 45)	# 87-131
    sprite('Action_120_04', 1)	# 132-132
    ExitState()
    label(2)
    sprite('Action_120_06', 40)	# 133-172
    sprite('Action_120_08', 45)	# 173-217
    sprite('Action_120_09', 45)	# 218-262
    sprite('Action_120_10', 1)	# 263-263
    ExitState()
    label(3)
    sprite('Action_120_12', 40)	# 264-303
    sprite('Action_120_14', 45)	# 304-348
    sprite('Action_120_15', 45)	# 349-393
    sprite('Action_120_16', 1)	# 394-394
    ExitState()
    label(4)
    sprite('Action_120_18', 40)	# 395-434
    sprite('Action_120_20', 45)	# 435-479
    sprite('Action_120_21', 45)	# 480-524
    sprite('Action_120_22', 1)	# 525-525
    ExitState()
    label(0)
    sprite('Action_120_04', 1)	# 526-526

@State
def IW_Kanji_Tsubomi():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown23015(1)
        Unknown1096(800)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-200000)
    sprite('Action_113_00', 5)	# 1-5
    sprite('Action_113_01', 5)	# 6-10
    sprite('Action_113_02', 20)	# 11-30
    sprite('Action_113_03', 3)	# 31-33

@State
def IW_Kanji_Moe():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown23015(1)
        Unknown1096(800)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-200000)
    sprite('Action_114_00', 5)	# 1-5
    sprite('Action_114_01', 5)	# 6-10
    sprite('Action_114_02', 20)	# 11-30
    sprite('Action_114_03', 3)	# 31-33

@State
def IW_Kanji_Saku():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown23015(1)
        Unknown1096(800)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-200000)
    sprite('Action_115_00', 5)	# 1-5
    sprite('Action_115_01', 5)	# 6-10
    sprite('Action_115_02', 20)	# 11-30
    sprite('Action_115_03', 3)	# 31-33

@State
def IW_Kanji_Chiru():

    def upon_IMMEDIATE():
        Unknown2008()
        Unknown23015(1)
        Unknown1096(800)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-200000)
    sprite('Action_116_00', 5)	# 1-5
    sprite('Action_116_01', 5)	# 6-10
    sprite('Action_116_02', 20)	# 11-30
    sprite('Action_116_03', 3)	# 31-33

@State
def IW_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(-45000)
        Unknown1007(120000)
    sprite('Action_431_00', 5)	# 1-5
    sprite('Action_431_01', 5)	# 6-10
    sprite('Action_431_02', 1)	# 11-11

@State
def IWExe_Camera():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown2054(1)
        Unknown1086(22)
        Unknown20000(1)
        Unknown20003(1)
        Unknown23022(1)
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown20007(0)
            Unknown20003(0)
            Unknown20001(0)
    sprite('null', 500)	# 1-500

@State
def IWExe_Blade1():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4011(3)
        Unknown4010(3)
    sprite('Action_117_00', 3)	# 1-3
    sprite('Action_117_01', 3)	# 4-6
    sprite('Action_117_02', 3)	# 7-9
    sprite('Action_117_03', 3)	# 10-12

@State
def IWExe_Blade2():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown4011(3)
        Unknown4010(3)
        teleportRelativeX(-50000)
        Unknown1007(50000)
    sprite('Action_110_01', 9)	# 1-9
    sprite('Action_110_02', 9)	# 10-18
    sprite('Action_110_03', 9)	# 19-27

@State
def IWExe_Kimono():

    def upon_IMMEDIATE():
        Unknown4010(3)
        Unknown1007(250000)
        teleportRelativeX(-150000)
    sprite('Action_211_00', 10)	# 1-10
    physicsXImpulse(10240)
    sprite('Action_211_01', 5)	# 11-15	 **attackbox here**
    Unknown1084(1)
    sprite('Action_211_02', 4)	# 16-19	 **attackbox here**
    sprite('Action_211_03', 4)	# 20-23
    sprite('Action_211_04', 4)	# 24-27
    sprite('Action_211_05', 1)	# 28-28

@State
def IWExe_Tanmono():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown4010(3)
        Unknown1007(250000)
    sprite('null', 15)	# 1-15
    GFX_0('IWExe_TanmonoBack', 100)
    sprite('Action_217_01', 4)	# 16-19
    sprite('Action_217_02', 4)	# 20-23
    sprite('Action_217_03', 4)	# 24-27
    sprite('Action_217_04', 4)	# 28-31
    sprite('Action_217_05', 4)	# 32-35
    sprite('Action_217_06', 4)	# 36-39
    sprite('Action_217_07', 4)	# 40-43
    sprite('Action_217_08', 4)	# 44-47
    sprite('Action_217_09', 4)	# 48-51
    sprite('Action_217_10', 4)	# 52-55
    sprite('Action_217_11', 4)	# 56-59
    sprite('Action_217_12', 4)	# 60-63
    sprite('Action_217_13', 4)	# 64-67
    sprite('Action_217_14', 3)	# 68-70
    sprite('Action_217_15', 3)	# 71-73
    sprite('Action_217_16', 5)	# 74-78
    Unknown1099(25)
    Unknown3004(-50)
    sprite('Action_217_17', 1)	# 79-79
    sprite('Action_217_18', 1)	# 80-80

@State
def IWExe_TanmonoBack():

    def upon_IMMEDIATE():
        Unknown2019(1010)
        Unknown4010(3)
    sprite('null', 15)	# 1-15
    sprite('Action_217_01ex01', 4)	# 16-19
    sprite('Action_217_02ex01', 4)	# 20-23	 **attackbox here**
    sprite('Action_217_03ex01', 4)	# 24-27	 **attackbox here**
    sprite('Action_217_04ex01', 4)	# 28-31	 **attackbox here**
    sprite('Action_217_05ex01', 4)	# 32-35	 **attackbox here**
    sprite('Action_217_06ex01', 4)	# 36-39	 **attackbox here**
    sprite('Action_217_07ex01', 4)	# 40-43	 **attackbox here**
    sprite('Action_217_08ex01', 4)	# 44-47	 **attackbox here**
    sprite('Action_217_09ex01', 4)	# 48-51	 **attackbox here**
    sprite('Action_217_10ex01', 4)	# 52-55	 **attackbox here**
    sprite('Action_217_11ex01', 4)	# 56-59	 **attackbox here**
    sprite('Action_217_12ex01', 4)	# 60-63	 **attackbox here**
    sprite('Action_217_13ex01', 4)	# 64-67	 **attackbox here**
    sprite('Action_217_14ex01', 3)	# 68-70	 **attackbox here**
    sprite('Action_217_15ex01', 3)	# 71-73	 **attackbox here**
    sprite('Action_217_16ex01', 5)	# 74-78	 **attackbox here**
    Unknown1099(25)
    Unknown3004(-50)
    sprite('Action_217_17', 1)	# 79-79
    sprite('Action_217_18', 1)	# 80-80

@State
def IWOD_AddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(5)
        Damage(2000)
        Hitstop(18)
        Unknown11091(30)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(3000)
        AirPushbackY(12000)
        Unknown9310(10)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown23151(22, 103)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown23078(1)

    def upon_45():
        Unknown48('19000000020000003300000016000000020000001e000000')
        if SLOT_51:
            Unknown2003(0)
        else:
            Unknown2003(1)
sprite('Action_461_21_dmyatk', 3)	# 1-3
endState()

@State
def IWOD_AddAtkDDD():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(5)
        Damage(300)
        Hitstop(18)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirPushbackX(3000)
        AirPushbackY(12000)
        Unknown9310(10)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown23151(22, 103)
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown23078(1)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)
    sprite('Action_461_21_dmyatk', 3)	# 1-3

@State
def UltimateRush_Blade1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
    sprite('Action_430_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_430_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_430_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_430_03', 1)	# 7-7	 **attackbox here**
    sprite('Action_430_04', 2)	# 8-9	 **attackbox here**
    sprite('Action_430_05', 2)	# 10-11	 **attackbox here**
    sprite('Action_430_06', 2)	# 12-13	 **attackbox here**
    sprite('Action_430_07', 1)	# 14-14	 **attackbox here**
    sprite('Action_430_08', 2)	# 15-16	 **attackbox here**
    sprite('Action_430_09', 2)	# 17-18	 **attackbox here**
    sprite('Action_430_10', 2)	# 19-20	 **attackbox here**
    sprite('Action_430_11', 1)	# 21-21

@State
def UltimateRush_Blade2_Matome():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown2019(-1)
    sprite('null', 5)	# 1-5
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('null', 5)	# 6-10
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('null', 5)	# 11-15
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('null', 5)	# 16-20
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('null', 5)	# 21-25
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('null', 5)	# 26-30
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('null', 5)	# 31-35
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('null', 5)	# 36-40
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('null', 5)	# 41-45
    GFX_0('UltimateRush_Blade2_Pt1', 100)

@State
def UltimateRush_Blade2_Pt1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
        Unknown23078(1)
        Unknown23182(2)
    label(1)
    sprite('Action_485_00', 2)	# 1-2
    sprite('Action_485_01', 2)	# 3-4
    sprite('Action_485_02', 2)	# 5-6
    sprite('Action_485_03', 1)	# 7-7

@State
def UltimateRush_Blade2_Pt2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
        Unknown23078(1)
        Unknown23182(2)
    sprite('Action_097_00ex01', 2)	# 1-2
    sprite('Action_097_01ex01', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02ex01', 2)	# 5-6
    sprite('Action_097_03', 1)	# 7-7

@State
def UltimateRush_Blade2_Pt3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
        Unknown23078(1)
        Unknown23182(2)
    label(3)
    sprite('Action_485_08', 2)	# 1-2
    sprite('Action_485_09', 2)	# 3-4
    sprite('Action_485_10', 2)	# 5-6
    sprite('Action_485_11', 1)	# 7-7

@State
def UltimateAirRush_Blade1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(40000)
    sprite('Action_430_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_430_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_430_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_430_03', 1)	# 7-7	 **attackbox here**
    sprite('Action_430_04', 2)	# 8-9	 **attackbox here**
    sprite('Action_430_05', 2)	# 10-11	 **attackbox here**
    sprite('Action_430_06', 2)	# 12-13	 **attackbox here**
    sprite('Action_430_07', 1)	# 14-14	 **attackbox here**
    sprite('Action_430_08', 2)	# 15-16	 **attackbox here**
    sprite('Action_430_09', 2)	# 17-18	 **attackbox here**
    sprite('Action_430_10', 2)	# 19-20	 **attackbox here**
    sprite('Action_430_11', 1)	# 21-21

@State
def UltimateAirRush_Blade2_Matome():

    def upon_IMMEDIATE():
        Unknown4009(3)
        Unknown2019(-1)
    sprite('null', 5)	# 1-5
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('null', 5)	# 6-10
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('null', 5)	# 11-15
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('null', 5)	# 16-20
    GFX_0('UltimateRush_Blade2_Pt1', 100)
    sprite('null', 5)	# 21-25
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('null', 5)	# 26-30
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('null', 5)	# 31-35
    GFX_0('UltimateRush_Blade2_Pt3', 100)
    sprite('null', 5)	# 36-40
    GFX_0('UltimateRush_Blade2_Pt2', 100)
    sprite('null', 5)	# 41-45
    GFX_0('UltimateRush_Blade2_Pt1', 100)

@State
def UltimateAirRush_Blade2_Pt1():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(100000)
        Unknown23078(1)
        Unknown23182(2)
    label(1)
    sprite('Action_485_00', 2)	# 1-2
    sprite('Action_485_01', 2)	# 3-4
    sprite('Action_485_02', 2)	# 5-6
    sprite('Action_485_03', 1)	# 7-7

@State
def UltimateAirRush_Blade2_Pt2():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(70000)
        Unknown23078(1)
        Unknown23182(2)
    sprite('Action_097_00ex01', 2)	# 1-2
    sprite('Action_097_01ex01', 2)	# 3-4	 **attackbox here**
    sprite('Action_097_02ex01', 2)	# 5-6
    sprite('Action_097_03', 1)	# 7-7

@State
def UltimateAirRush_Blade2_Pt3():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(100000)
        Unknown23078(1)
        Unknown23182(2)
    label(3)
    sprite('Action_485_08', 2)	# 1-2
    sprite('Action_485_09', 2)	# 3-4
    sprite('Action_485_10', 2)	# 5-6
    sprite('Action_485_11', 1)	# 7-7

@State
def UltimateAirRush_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(-50000)
        Unknown1007(250000)
    sprite('Action_431_00', 5)	# 1-5
    sprite('Action_431_01', 5)	# 6-10
    sprite('Action_431_02', 1)	# 11-11

@State
def UltimateRush_Release():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(-15000)
        Unknown1007(150000)
    sprite('Action_431_00', 5)	# 1-5
    sprite('Action_431_01', 5)	# 6-10
    sprite('Action_431_02', 1)	# 11-11

@State
def UltimateRush_AddAtk():

    def upon_IMMEDIATE():
        Unknown2011()
        Unknown23056('')
        Unknown4011(3)
        Unknown2019(-1)
        AttackLevel_(5)
        Damage(2000)
        Hitstop(15)
        Unknown11091(10)
        AttackP1(100)
        AttackP2(100)
        AirPushbackX(9000)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(3000)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown23151(22, 103)
        Unknown11034(1)
        Unknown11033(0)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11023(1)
        Unknown30048(1)
        Unknown11108('03000000')

        def upon_78():
            SFX_0('025_cleanhit_slash')

        def upon_45():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown2003(0)
            else:
                Unknown2003(1)
    sprite('Action_461_21_dmyatk', 3)	# 1-3

@State
def UltimateRush_Blade2_ODFinish():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(-10000)
    sprite('Action_242_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_242_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_242_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_242_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_242_04', 1)	# 21-21

@State
def UltimateRush_Blade2_ODFinish_Ma():

    def upon_IMMEDIATE():
        Unknown2019(-1)
        Unknown1086(22)
        Unknown1007(50000)
        Unknown23022(1)
    sprite('null', 3)	# 1-3
    sprite('null', 3)	# 4-6
    GFX_0('UltimateRushOD_Finish_Pt1', 100)
    GFX_0('UltimateRushOD_Finish_Pt3', 100)
    sprite('null', 3)	# 7-9
    GFX_0('UltimateRushOD_Finish_Pt2', 100)
    sprite('null', 1)	# 10-10

@State
def UltimateRushOD_Finish_Pt1():

    def upon_IMMEDIATE():
        Unknown1007(150000)
    sprite('Action_243_00', 3)	# 1-3
    sprite('Action_243_01', 3)	# 4-6
    sprite('Action_243_02', 3)	# 7-9
    sprite('Action_243_03', 3)	# 10-12
    sprite('Action_243_03', 1)	# 13-13

@State
def UltimateRushOD_Finish_Pt2():

    def upon_IMMEDIATE():
        pass
    sprite('Action_245_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_245_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_245_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_245_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_245_04', 1)	# 21-21

@State
def UltimateRushOD_Finish_Pt3():
    sprite('Action_244_00', 6)	# 1-6
    sprite('Action_244_01', 6)	# 7-12
    sprite('Action_244_02', 6)	# 13-18

@State
def UltimateAirRush_ODFinish():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown4007(3)
        Unknown2019(-1)
        teleportRelativeX(100000)
        Unknown1007(100000)
    sprite('Action_242_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_242_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_242_02', 5)	# 11-15	 **attackbox here**
    sprite('Action_242_03', 5)	# 16-20	 **attackbox here**
    sprite('Action_242_04', 1)	# 21-21

@State
def UltimateAirRushODFinish_Matome():

    def upon_IMMEDIATE():
        Unknown2019(-1)
        Unknown1086(22)
        Unknown1007(250000)
        Unknown23022(1)
    sprite('null', 3)	# 1-3
    sprite('null', 3)	# 4-6
    GFX_0('UltimateRushOD_Finish_Pt1', 100)
    GFX_0('UltimateRushOD_Finish_Pt3', 100)
    sprite('null', 3)	# 7-9
    GFX_0('UltimateRushOD_Finish_Pt2', 100)
    sprite('null', 1)	# 10-10

@State
def IaiStand_DmyObj():

    def upon_IMMEDIATE():
        Unknown2010()
        Unknown4007(2)
        Unknown3038(1)
        Unknown23091(1)

        def upon_54():
            Unknown23029(3, 100, 0)
    sprite('Action_420_00', 2)	# 1-2

@State
def IWEXIST_Camera():

    def upon_IMMEDIATE():
        Unknown2053(0)
        Unknown2017(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20000(1)
        Unknown1086(22)
        teleportRelativeY(0)

        def upon_43():
            if (SLOT_48 == 8002):
                sendToLabel(1)
    sprite('null', 32767)	# 1-32767
    label(1)
    sprite('null', 15)	# 32768-32782
    Unknown1007(55000)
    Unknown20001(1)
    SLOT_105 = 850
    sprite('null', 32767)	# 32783-65549
    Unknown23029(3, 8003, 0)
    physicsYImpulse(-550)

    def upon_3():
        if (SLOT_105 <= 1050):
            SLOT_105 = (SLOT_105 + 2)
        else:
            clearUponHandler(3)
            YAccel(0)
            Unknown21015('41737472616c4865617400000000000000000000000000000000000000000000441f000000000000')
            SLOT_105 = 1050

@State
def IWEX_WhiteOut():

    def upon_IMMEDIATE():
        Unknown2019(-4000)
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
    sprite('vr_white', 15)	# 1-15
    Unknown3004(20)
    sprite('vr_white', 10)	# 16-25
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 15)	# 26-40
    Unknown3004(-9)

@State
def IWEX_BlackOut():

    def upon_IMMEDIATE():
        Unknown2019(-4000)
        Unknown3001(0)
        Unknown1096(100000000)
        Unknown1056(20000)
        Unknown3026(-16777216)
    sprite('vr_white', 5)	# 1-5
    Unknown3004(50)
    sprite('vr_white', 10)	# 6-15
    Unknown3001(255)
    Unknown3004(0)
    sprite('vr_white', 5)	# 16-20
    Unknown3004(-50)

@State
def IWEXIST_Kimono():

    def upon_IMMEDIATE():
        Unknown4010(3)
        teleportRelativeY(350000)
        teleportRelativeX(-250000)
    sprite('Action_538_00', 20)	# 1-20
    SFX_3('SE_ClothesSwing2')
    physicsXImpulse(5120)
    physicsYImpulse(2560)
    sprite('Action_538_01', 5)	# 21-25	 **attackbox here**
    Unknown1084(1)
    sprite('Action_538_02', 4)	# 26-29	 **attackbox here**
    sprite('Action_538_03', 4)	# 30-33
    sprite('Action_538_04', 4)	# 34-37
    sprite('Action_538_05', 1)	# 38-38
    GFX_0('IWEXIST_TanMono', 100)
    GFX_0('IWEXIST_TanMonoBack', 100)

@State
def IWEXIST_TanMono():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
        Unknown4010(3)
        Unknown1007(-150000)

        def upon_8():
            Unknown26('IWEXIST_TanMonoBack')
            Unknown21015('41737472616c4865617400000000000000000000000000000000000000000000411f000000000000')
    sprite('Action_540_01', 2)	# 1-2
    SFX_3('SE_CoilRound')
    sprite('Action_540_02', 2)	# 3-4
    sprite('Action_540_03', 2)	# 5-6
    sprite('Action_540_04', 2)	# 7-8
    sprite('Action_540_05', 2)	# 9-10
    sprite('Action_540_06', 2)	# 11-12
    sprite('Action_540_07', 2)	# 13-14
    sprite('Action_540_08', 2)	# 15-16
    sprite('Action_540_09', 2)	# 17-18
    sprite('Action_540_10', 2)	# 19-20
    sprite('Action_540_11', 2)	# 21-22
    sprite('Action_540_12', 2)	# 23-24
    sprite('Action_540_13', 14)	# 25-38	 **attackbox here**
    sprite('Action_540_14', 13)	# 39-51	 **attackbox here**
    sprite('Action_540_15', 12)	# 52-63	 **attackbox here**
    sprite('Action_540_16', 11)	# 64-74	 **attackbox here**
    sprite('Action_540_17', 9)	# 75-83	 **attackbox here**
    sprite('Action_540_18', 7)	# 84-90	 **attackbox here**
    sprite('Action_540_19', 5)	# 91-95	 **attackbox here**
    sprite('Action_540_20', 15)	# 96-110	 **attackbox here**
    GFX_0('IWEX_WhiteOut', 100)

@State
def IWEXIST_TanMonoBack():

    def upon_IMMEDIATE():
        Unknown2019(1000)
        Unknown4010(3)
        Unknown1007(-150000)
    sprite('Action_540_01ex01', 2)	# 1-2
    sprite('Action_540_02ex01', 2)	# 3-4
    sprite('Action_540_03ex01', 2)	# 5-6
    sprite('Action_540_04ex01', 2)	# 7-8
    sprite('Action_540_05ex01', 2)	# 9-10
    sprite('Action_540_06ex01', 2)	# 11-12
    sprite('Action_540_07ex01', 2)	# 13-14
    sprite('Action_540_08ex01', 2)	# 15-16
    sprite('Action_540_09ex01', 2)	# 17-18
    sprite('Action_540_10ex01', 2)	# 19-20
    sprite('Action_540_11ex01', 2)	# 21-22
    sprite('Action_540_12ex01', 2)	# 23-24
    sprite('Action_540_13ex01', 32767)	# 25-32791

@State
def IWEXIST_BG_Front():

    def upon_IMMEDIATE():
        Unknown2019(1000)
        Unknown4010(3)
        Unknown4011(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-320000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_520_00', 5)	# 1-5
    sprite('Action_520_00', 5)	# 6-10
    sprite('Action_520_01', 5)	# 11-15
    sprite('Action_520_02', 5)	# 16-20
    sprite('Action_520_03', 5)	# 21-25
    sprite('Action_520_04', 5)	# 26-30
    sprite('Action_520_05', 5)	# 31-35
    sprite('Action_520_06', 5)	# 36-40
    sprite('Action_520_07', 5)	# 41-45
    sprite('Action_520_08', 5)	# 46-50
    sprite('Action_520_09', 5)	# 51-55
    label(0)
    sprite('Action_520_10', 59)	# 56-114
    sprite('Action_520_11', 59)	# 115-173
    sprite('Action_520_12', 59)	# 174-232
    sprite('Action_520_13', 59)	# 233-291
    gotoLabel(0)

@State
def IWEXIST_BG_Back():

    def upon_IMMEDIATE():
        Unknown2019(1010)
        Unknown4010(3)
        Unknown4011(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-320000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_520_00', 5)	# 1-5
    sprite('Action_521_00', 5)	# 6-10
    sprite('Action_521_01', 5)	# 11-15
    sprite('Action_521_02', 5)	# 16-20
    sprite('Action_521_03', 5)	# 21-25
    sprite('Action_521_04', 5)	# 26-30
    sprite('Action_521_05', 5)	# 31-35
    sprite('Action_521_06', 5)	# 36-40
    sprite('Action_521_07', 5)	# 41-45
    sprite('Action_521_08', 5)	# 46-50
    sprite('Action_521_09', 5)	# 51-55
    sprite('Action_521_10', 5)	# 56-60
    sprite('Action_521_11', 5)	# 61-65
    sprite('Action_521_12', 5)	# 66-70
    sprite('Action_521_13', 32767)	# 71-32837

@State
def IWEXIST_SlushEff():

    def upon_IMMEDIATE():
        Unknown23015(1)
        Unknown4010(3)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-320000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_541_00', 2)	# 1-2
    SFX_3('SE_DrawnSword')
    sprite('Action_541_01', 2)	# 3-4
    sprite('Action_541_02', 2)	# 5-6
    sprite('Action_541_03', 2)	# 7-8
    sprite('Action_541_04', 2)	# 9-10
    sprite('Action_541_05', 2)	# 11-12
    sprite('Action_541_06', 2)	# 13-14
    sprite('Action_541_07', 2)	# 15-16
    sprite('Action_541_08', 2)	# 17-18
    sprite('Action_541_09', 2)	# 19-20
    sprite('Action_541_10', 2)	# 21-22
    sprite('Action_541_11', 2)	# 23-24

@State
def IWEX_SakuraParticle():

    def upon_IMMEDIATE():
        Unknown1007(200000)
        Unknown1026(-1000, -500)
        Unknown1011(-250000, 450000)
        Unknown1012(-750000, 750000)
        Unknown1079()
        Unknown1078(-100, 100)
        Unknown1102(-500, 0)

        def upon_3():
            Unknown1025(-250, 250)
    sprite('null', 1)	# 1-1
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(3)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(2)
    label(1)
    sprite('Action_527_00', 240)	# 2-241
    sprite('Action_527_01', 30)	# 242-271
    sprite('Action_527_02', 30)	# 272-301
    sprite('Action_527_03', 2)	# 302-303
    gotoLabel(1)
    label(2)
    sprite('Action_528_00', 240)	# 304-543
    sprite('Action_528_01', 30)	# 544-573
    sprite('Action_528_02', 30)	# 574-603
    sprite('Action_528_03', 2)	# 604-605
    gotoLabel(2)
    label(3)
    sprite('Action_529_00', 240)	# 606-845
    sprite('Action_529_01', 30)	# 846-875
    sprite('Action_529_02', 30)	# 876-905
    sprite('Action_529_03', 2)	# 906-907
    gotoLabel(3)

@State
def IWEX_SakuraParticle2():

    def upon_IMMEDIATE():
        Unknown1007(200000)
        Unknown1026(-5000, 5000)
        Unknown1025(-4500, 100000)
        Unknown1011(650000, 350000)
        Unknown1012(-750000, 750000)
        teleportRelativeX(-800000)
        teleportRelativeY(-250000)
        Unknown1015(50000)
        physicsYImpulse(22000)
        Unknown1079()
        Unknown1078(-500, 500)
        Unknown1102(-200, 1000)
    label(0)
    sprite('Action_530_00', 240)	# 1-240
    sprite('Action_530_01', 30)	# 241-270
    sprite('Action_530_02', 30)	# 271-300
    sprite('Action_530_03', 2)	# 301-302
    gotoLabel(0)

@State
def IWEX_Sakura_MatomeFinish():

    def upon_IMMEDIATE():
        Unknown2019(-1000)
    sprite('null', 1)	# 1-1
    sprite('null', 5)	# 2-6
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 7-8
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 9-10
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 11-12
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 13-14
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 15-16
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 17-18
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 19-20
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 21-22
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 23-24
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 25-26
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 27-28
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 29-30
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 31-32
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 33-34
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 35-36
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 37-38
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 39-40
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 41-42
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 43-44
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 45-46
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 47-48
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 49-50
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 2)	# 51-52
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 20)	# 53-72
    GFX_0('IWEX_SakuraParticle2', 100)
    GFX_0('IWEX_SakuraParticle2', 100)
    sprite('null', 1)	# 73-73
    GFX_0('IWEX_Finish', 100)

@State
def IWEX_IaiDmyAtk():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown11023(1)
        AttackLevel_(5)
        Damage(0)
        Unknown11091(100)
        Hitstop(0)
        AirPushbackX(350)
        AirPushbackY(150)
        YImpluseBeforeWallbounce(9)
        Unknown9310(999)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11086(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown9154(9999)
        AirUntechableTime(9999)
        Unknown11064(1)

        def upon_78():
            Unknown2038(1)

        def upon_45():
            if SLOT_2:
                Unknown36(22)
                Unknown3026(-13619152)
                Unknown35()
    sprite('Action_536_dmycol', 150)	# 1-150

@State
def IWEX_Finish():

    def upon_IMMEDIATE():
        Unknown2012()
        Unknown23015(1)
        Unknown21010(1)
        Unknown2054(1)
        Unknown2012()
        Unknown11023(1)
        AttackLevel_(5)
        Damage(41250)
        Unknown11091(100)
        Unknown9154(9999)
        AirUntechableTime(9999)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11064(3)
        Unknown11056(3)
        AirPushbackX(0)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(450)
        Hitstop(0)
        Unknown11001(0, 30, 30)
        Unknown11086(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2019(-4000)
        Unknown4010(3)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-320000)
        if SLOT_38:
            Unknown1000(-640000)

        def upon_78():
            Unknown36(22)
            Unknown3026(-13619152)
            Unknown35()
    sprite('Action_542_00', 2)	# 1-2
    SFX_3('SE_BigBomb')
    sprite('Action_542_01', 4)	# 3-6	 **attackbox here**
    sprite('Action_542_02', 4)	# 7-10
    sprite('Action_542_03', 4)	# 11-14
    sprite('Action_542_04', 4)	# 15-18
    sprite('Action_542_05', 4)	# 19-22
    sprite('Action_542_06', 20)	# 23-42
    Unknown23029(3, 8005, 0)
    sprite('Action_542_07', 80)	# 43-122
    sprite('Action_543_00', 14)	# 123-136

@State
def UYU_CutIn():

    def upon_IMMEDIATE():
        Unknown4011(3)
        Unknown4010(3)
        Unknown2054(1)
        Unknown6001(1)
        Unknown1000(640000)
        teleportRelativeY(-640000)
        if SLOT_38:
            Unknown1000(-640000)
    sprite('Action_999_01', 4)	# 1-4
    sprite('Action_999_02', 4)	# 5-8
    sprite('Action_999_03', 4)	# 9-12	 **attackbox here**
    sprite('Action_999_04', 4)	# 13-16	 **attackbox here**
    sprite('Action_999_05', 5)	# 17-21	 **attackbox here**
    sprite('Action_999_06', 4)	# 22-25	 **attackbox here**
    sprite('Action_999_07', 5)	# 26-30	 **attackbox here**
    sprite('Action_999_08', 6)	# 31-36	 **attackbox here**
    sprite('Action_999_09', 10)	# 37-46	 **attackbox here**
    sprite('Action_999_10', 4)	# 47-50	 **attackbox here**
    sprite('Action_999_11', 3)	# 51-53
    sprite('Action_999_12', 3)	# 54-56	 **attackbox here**
    sprite('Action_999_13', 3)	# 57-59	 **attackbox here**
    sprite('Action_999_14', 5)	# 60-64	 **attackbox here**
    sprite('Action_999_14', 5)	# 65-69	 **attackbox here**
    physicsXImpulse(35000)
    Unknown3001(200)
    Unknown3004(-20)
    Unknown1099(10)

@State
def TimeUp_Lose():

    def upon_IMMEDIATE():
        Unknown4010(2)
    sprite('Action_249_00', 10)	# 1-10
    sprite('Action_249_01', 10)	# 11-20
    sprite('Action_249_02', 32767	# 21-32787
