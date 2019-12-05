@Subroutine
def PreInit():
    Unknown12019('72626c00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(16000)
    DashFInitialVelocity(20000)
    DashFAccel(750)
    DashFMaxVelocity(35000)
    Unknown12038(35000)
    Unknown12034(15)
    AirDashBSpeed(25000)
    AirBDashDuration(12)
    Unknown12024(2)
    Unknown13039(2)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown15013(2000)
    Unknown14015(-100000, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown15003(0)
    Unknown15000(0)
    MoveMaxChainRepeat(1)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(-50000, 450000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(-50000, 400000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(-50000, 400000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAAA', 0x10)
    Unknown14005(1)
    Unknown14015(-100000, 600000, -450000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 300000, -100000, 150000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(700000, 1000000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15015(40, 42)
    Unknown15021(2000)
    Unknown14015(500000, 1200000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(500)
    Unknown15009()
    Unknown14015(600000, 900000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown15021(1)
    Unknown15009()
    Unknown14015(0, 400000, -100000, 150000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-100000, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(-100000, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AAA', 0x10)
    Unknown14005(1)
    Unknown14015(-100000, 450000, -250000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2A', 0xd)
    Unknown15021(500)
    Unknown14015(0, 500000, -350000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(100000, 700000, -500000, -250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15013(500)
    Unknown14015(50000, 350000, -600000, -200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('DashCancel', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown15013(1)
    Unknown15012(3000)
    Unknown14015(0, 450000, -200000, 300000, 250, 1)
    Move_EndRegister()
    Move_Register('LandShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(100000, 450000, -200000, 50000, 500, 10)
    Move_EndRegister()
    Move_Register('LandShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(550000, 800000, -200000, 50000, 500, 10)
    Move_EndRegister()
    Move_Register('LandShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(550000, 1200000, -200000, 250000, 250, 5)
    Move_EndRegister()
    Move_Register('AssaultA', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x300a)
    Unknown15014(1)
    Unknown15021(2000)
    Unknown14015(200000, 480000, -150000, 200000, 150, 5)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x300b)
    Unknown15021(2000)
    Unknown14015(50000, 450000, -150000, 350000, 150, 5)
    Move_EndRegister()
    Move_Register('AssaultC', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x300c)
    Move_AirGround_(0x3086)
    Unknown15021(2000)
    Unknown14015(-50000, 350000, -150000, 400000, 100, 1)
    Move_EndRegister()
    Move_Register('ChainAssaultA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(2000)
    Unknown14015(-600000, 600000, -400000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('ChainAssaultB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(2000)
    Unknown15012(2000)
    Unknown14015(-600000, 600000, -400000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('ChainAssaultC', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15012(2000)
    Unknown14015(-600000, 600000, -400000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('LandShadowCreateA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3008)
    Unknown15014(1)
    Unknown15013(0)
    Unknown15012(1)
    Unknown14015(200000, 450000, -200000, 50000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShadowCreateA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3008)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(50000, 250000, -300000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('LandShadowCreateB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3008)
    Unknown15014(1)
    Unknown15013(0)
    Unknown15012(1)
    Unknown14015(200000, 450000, -200000, 50000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShadowCreateB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3008)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(50000, 250000, -300000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('LandShadowCreateC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3008)
    Unknown15014(1)
    Unknown15013(0)
    Unknown15012(1)
    Unknown14015(200000, 450000, -200000, 50000, 150, 1)
    Move_EndRegister()
    Move_Register('AirShadowCreateC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3008)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(50000, 250000, -300000, 150000, 150, 1)
    Move_EndRegister()
    Move_Register('ChainShadowCreateA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Unknown14013('AirShadowCreateA')
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(-600000, 600000, -400000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('ChainShadowCreateB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Unknown14013('AirShadowCreateB')
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(-600000, 600000, -400000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('ChainShadowCreateC', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Unknown14013('AirShadowCreateC')
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(-600000, 600000, -400000, 400000, 500, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(1)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 200000, -100000, 300000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateShotSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateRush', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 400000, -200000, 250000, 150, 0)
    Move_EndRegister()
    Move_Register('UltimateRushSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 400000, -200000, 250000, 150, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 650000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5AAAA', 'NmlAtk5AAAAA', 10000000)
    Unknown15024('NmlAtk5AAAA', 'AssaultA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk5BB', 'LandShotB', 10000000)
    Unknown15024('NmlAtk5BB', 'AssaultA', 10000000)
    Unknown15024('NmlAtk5BB', 'AssaultB', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2C', 'LandShotA', 10000000)
    Unknown15024('NmlAtk2C', 'AssaultA', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5AAA', 10000000)
    Unknown15024('NmlAtkAIR5AAA', 'AirShadowCreateA', 10000000)
    Unknown15024('NmlAtkAIR5AAA', 'AirShadowCreateB', 10000000)
    Unknown15024('NmlAtkAIR5AAA', 'AirShadowCreateC', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AssaultA', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AssaultB', 10000000)
    Unknown12018(0, 'rbl062_01')
    Unknown12018(1, 'rbl062_03')
    Unknown12018(2, 'rbl062_04')
    Unknown12018(3, 'rbl062_05')
    Unknown12018(4, 'rbl062_06')
    Unknown12018(5, 'rbl062_07')
    Unknown12018(6, 'rbl062_09')
    Unknown12018(7, 'rbl040_02')
    Unknown12018(8, 'rbl040_02')
    Unknown12018(9, 'rbl045_02')
    Unknown12018(10, 'rbl062_00')
    Unknown12018(11, 'rbl062_01')
    Unknown12018(12, 'rbl062_03')
    Unknown12018(13, 'rbl062_05')
    Unknown12018(14, 'rbl062_09')
    Unknown12018(15, 'rbl073_01ex01')
    Unknown12018(16, 'rbl050_00')
    Unknown12018(17, 'rbl052_00')
    Unknown12018(18, 'rbl054_00')
    Unknown12018(19, 'rbl000_00')
    Unknown12018(20, 'rbl000_00')
    Unknown12018(25, 'rbl063_00')
    Unknown12018(26, 'rbl063_01')
    Unknown12018(27, 'rbl063_02')
    Unknown12018(28, 'rbl063_04')
    Unknown12018(29, 'rbl063_09')
    Unknown12018(24, 'rbl073_01')
    Unknown7010(0, 'rbl000')
    Unknown7010(1, 'rbl001')
    Unknown7010(2, 'rbl002')
    Unknown7010(3, 'rbl003')
    Unknown7010(4, 'rbl004')
    Unknown7010(5, 'rbl005')
    Unknown7010(6, 'rbl006')
    Unknown7010(7, 'rbl007')
    Unknown7010(8, 'rbl008')
    Unknown7010(9, 'rbl009')
    Unknown7010(10, 'rbl010')
    Unknown7010(15, 'rbl013')
    Unknown7010(16, 'rbl014')
    Unknown7010(17, 'rbl015')
    Unknown7010(18, 'rbl016')
    Unknown7010(19, 'rbl017')
    Unknown7010(20, 'rbl018')
    Unknown7010(21, 'rbl019')
    Unknown7010(22, 'rbl020')
    Unknown7010(23, 'rbl021')
    Unknown7010(24, 'rbl022')
    Unknown7010(25, 'rbl023')
    Unknown7010(28, 'rbl024')
    Unknown7010(29, 'rbl025')
    Unknown7010(30, 'rbl026')
    Unknown7010(31, 'rbl027')
    Unknown7010(32, 'rbl028')
    Unknown7010(33, 'rbl029')
    Unknown7010(34, 'rbl030')
    Unknown7010(35, 'rbl031')
    Unknown7010(36, 'rbl032')
    Unknown7010(37, 'rbl033')
    Unknown7010(39, 'rbl034')
    Unknown7010(42, 'rbl035')
    Unknown7010(43, 'rbl036')
    Unknown7010(44, 'rbl037')
    Unknown7010(45, 'rbl038')
    Unknown7010(46, 'rbl039')
    Unknown7010(47, 'rbl304_0')
    Unknown7010(48, 'rbl041')
    Unknown7010(49, 'rbl042')
    Unknown7010(50, 'rbl043')
    Unknown7010(52, 'rbl044')
    Unknown7010(53, 'rbl045')
    Unknown7010(54, 'rbl100_0')
    Unknown7010(55, 'rbl100_1')
    Unknown7010(56, 'rbl100_2')
    Unknown7010(63, 'rbl101_0')
    Unknown7010(64, 'rbl101_1')
    Unknown7010(65, 'rbl101_2')
    Unknown7010(57, 'rbl102_0')
    Unknown7010(58, 'rbl102_1')
    Unknown7010(59, 'rbl102_2')
    Unknown7010(66, 'rbl103_0')
    Unknown7010(67, 'rbl103_1')
    Unknown7010(68, 'rbl103_2')
    Unknown7010(60, 'rbl104_0')
    Unknown7010(61, 'rbl104_1')
    Unknown7010(62, 'rbl104_2')
    Unknown7010(69, 'rbl105_0')
    Unknown7010(70, 'rbl105_1')
    Unknown7010(71, 'rbl105_2')
    Unknown7010(72, 'rbl150')
    Unknown7010(73, 'rbl151')
    Unknown7010(74, 'rbl152')
    Unknown7010(85, 'rbl153')
    Unknown7010(88, 'rbl156')
    Unknown7010(94, 'rbl401_0')
    Unknown7010(95, 'rbl401_1')
    Unknown7010(96, 'rbl162_0')
    Unknown7010(97, 'rbl162_1')
    Unknown7010(98, 'rbl164_0')
    Unknown7010(99, 'rbl164_1')
    Unknown7010(100, 'rbl165_0')
    Unknown7010(101, 'rbl165_1')
    Unknown7010(102, 'rbl167_0')
    Unknown7010(103, 'rbl167_1')
    Unknown7010(92, 'rbl163_0')
    Unknown7010(93, 'rbl163_1')
    Unknown7010(90, 'rbl168_0')
    Unknown7010(91, 'rbl168_1')
    Unknown7010(105, 'rbl166_0')
    Unknown7010(106, 'rbl166_1')
    Unknown7010(107, 'rbl169_0')
    Unknown7010(108, 'rbl169_1')
    Unknown7010(110, 'rbl170_0')
    Unknown7010(111, 'rbl170_1')
    Unknown7010(112, 'rbl160_0')
    Unknown7010(113, 'rbl160_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745350000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465527573685350000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_4:
            SLOT_4 = (SLOT_4 + (-1))
    if SLOT_37:
        SLOT_6 = 0
        SLOT_7 = 0
        SLOT_8 = 0

@Subroutine
def EX_Eff():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown3074('000000000400000032000000a0000000')
    Unknown3075('00000000000000000000000010000000')
    Unknown3076(1010)
    Unknown3077(900)

@State
def CmnActStand():
    label(0)
    sprite('rbl000_00', 6)	# 1-6
    sprite('rbl000_01', 6)	# 7-12
    sprite('rbl000_02', 6)	# 13-18
    sprite('rbl000_03', 6)	# 19-24
    sprite('rbl000_04', 6)	# 25-30
    sprite('rbl000_05', 6)	# 31-36
    sprite('rbl000_06', 6)	# 37-42
    sprite('rbl000_07', 6)	# 43-48
    sprite('rbl000_08', 6)	# 49-54
    sprite('rbl000_09', 6)	# 55-60
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('keep', 1)	# 61-61
    SLOT_88 = 960
    SFX_1('rbl000')
    sprite('rbl000_00', 6)	# 62-67
    sprite('rbl001_00', 6)	# 68-73
    sprite('rbl001_01', 6)	# 74-79
    sprite('rbl001_02', 4)	# 80-83
    sprite('rbl001_03', 4)	# 84-87
    sprite('rbl001_04', 6)	# 88-93
    sprite('rbl001_05', 5)	# 94-98
    sprite('rbl001_06', 6)	# 99-104
    sprite('rbl001_05', 5)	# 105-109
    sprite('rbl001_04', 6)	# 110-115
    sprite('rbl001_05', 5)	# 116-120
    sprite('rbl001_06', 6)	# 121-126
    sprite('rbl001_03', 4)	# 127-130
    sprite('rbl001_02', 4)	# 131-134
    sprite('rbl001_01', 6)	# 135-140
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('rbl003_00', 3)	# 1-3
    sprite('rbl003_01', 3)	# 4-6
    sprite('rbl003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('rbl010_00', 4)	# 1-4
    sprite('rbl010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('rbl010_02', 6)	# 1-6
    sprite('rbl010_03', 6)	# 7-12
    sprite('rbl010_04', 6)	# 13-18
    sprite('rbl010_05', 6)	# 19-24
    sprite('rbl010_06', 6)	# 25-30
    sprite('rbl010_07', 6)	# 31-36
    sprite('rbl010_06', 6)	# 37-42
    sprite('rbl010_05', 6)	# 43-48
    sprite('rbl010_04', 6)	# 49-54
    sprite('rbl010_03', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('rbl013_00', 3)	# 1-3
    sprite('rbl013_01', 3)	# 4-6
    sprite('rbl013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('rbl010_01', 4)	# 1-4
    sprite('rbl010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('rbl010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('rbl020_00', 3)	# 1-3
    sprite('rbl020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('rbl020_02', 3)	# 1-3
    sprite('rbl020_03', 3)	# 4-6
    sprite('rbl020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('rbl020_05', 3)	# 1-3
    sprite('rbl020_06', 3)	# 4-6
    label(0)
    sprite('rbl020_07', 3)	# 7-9
    sprite('rbl020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('rbl010_01', 3)	# 1-3
    sprite('rbl010_00', 3)	# 4-6

@State
def CmnActLandingStiffLoop():
    sprite('rbl010_01', 4)	# 1-4
    sprite('rbl010_00', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('rbl010_00', 3)	# 1-3
    sprite('rbl010_00', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ny030_00', 7)	# 1-7
    label(0)
    sprite('ny030_01', 7)	# 8-14
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny030', -1)
    sprite('ny030_02', 7)	# 15-21
    GFX_1('nyef_ny030', -1)
    sprite('ny030_03', 7)	# 22-28
    GFX_1('nyef_ny030', -1)
    sprite('ny030_04', 7)	# 29-35
    GFX_1('nyef_ny030', -1)
    sprite('ny030_05', 7)	# 36-42
    GFX_1('nyef_ny030', -1)
    sprite('ny030_06', 7)	# 43-49
    GFX_1('nyef_ny030', -1)
    sprite('ny030_07', 7)	# 50-56
    GFX_1('nyef_ny030', -1)
    sprite('ny030_08', 7)	# 57-63
    GFX_1('nyef_ny030', -1)
    sprite('ny030_09', 7)	# 64-70
    GFX_1('nyef_ny030', -1)
    sprite('ny030_10', 7)	# 71-77
    GFX_1('nyef_ny030', -1)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('rbl031_00', 7)	# 1-7
    sprite('rbl031_01', 7)	# 8-14
    label(0)
    sprite('rbl031_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rbl031_03', 7)	# 22-28
    sprite('rbl031_04', 7)	# 29-35
    sprite('rbl031_05', 7)	# 36-42
    sprite('rbl031_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rbl031_07', 7)	# 50-56
    sprite('rbl031_08', 7)	# 57-63
    sprite('rbl031_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('rbl032_00', 3)	# 1-3
    sprite('rbl032_01', 3)	# 4-6
    label(0)
    sprite('rbl032_02', 3)	# 7-9
    sprite('rbl032_03', 3)	# 10-12
    sprite('rbl032_04', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('rbl032_05', 3)	# 16-18
    sprite('rbl032_06', 3)	# 19-21
    sprite('rbl032_07', 3)	# 22-24
    sprite('rbl032_08', 3)	# 25-27
    Unknown8006(100, 1, 1)
    sprite('rbl032_09', 3)	# 28-30
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('rbl032_10', 3)	# 1-3
    sprite('rbl032_11', 3)	# 4-6
    sprite('rbl032_12', 3)	# 7-9
    sprite('rbl032_13', 3)	# 10-12
    sprite('rbl032_14', 3)	# 13-15

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincibleFor(7)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('rbl033_00', 2)	# 1-2
    sprite('rbl033_01', 2)	# 3-4
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rbl033_02', 2)	# 5-6
    loopRest()
    label(0)
    sprite('rbl033_01', 2)	# 7-8
    sprite('rbl033_02', 2)	# 9-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl033_03', 3)	# 11-13
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rbl033_04', 3)	# 14-16

@State
def CmnActBDashLanding():
    sprite('ny033_05', 4)	# 1-4
    sprite('ny033_06', 4)	# 5-8

@State
def CmnActAirFDash():
    sprite('rbl035_00', 2)	# 1-2
    label(0)
    sprite('rbl035_01', 3)	# 3-5
    sprite('rbl035_02', 3)	# 6-8
    sprite('rbl035_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('rbl033_00', 3)	# 1-3
    label(0)
    sprite('rbl033_01', 3)	# 4-6
    sprite('rbl033_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('rbl050_00', 1)	# 1-1
    sprite('rbl050_01', 1)	# 2-2
    sprite('rbl050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('rbl050_01', 1)	# 1-1
    sprite('rbl050_02', 1)	# 2-2
    sprite('rbl050_01', 2)	# 3-4
    sprite('rbl050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('rbl050_02', 1)	# 1-1
    sprite('rbl050_02', 1)	# 2-2
    sprite('rbl050_02', 2)	# 3-4
    sprite('rbl050_01', 2)	# 5-6
    sprite('rbl050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('rbl050_02', 1)	# 1-1
    sprite('rbl050_03', 1)	# 2-2
    sprite('rbl050_02', 2)	# 3-4
    sprite('rbl050_02', 2)	# 5-6
    sprite('rbl050_01', 2)	# 7-8
    sprite('rbl050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('rbl050_03', 1)	# 1-1
    sprite('rbl050_03', 1)	# 2-2
    sprite('rbl050_03', 2)	# 3-4
    sprite('rbl050_02', 2)	# 5-6
    sprite('rbl050_02', 2)	# 7-8
    sprite('rbl050_01', 2)	# 9-10
    sprite('rbl050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('rbl052_00', 1)	# 1-1
    sprite('rbl052_01', 1)	# 2-2
    sprite('rbl052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('rbl052_01', 1)	# 1-1
    sprite('rbl052_02', 1)	# 2-2
    sprite('rbl052_01', 2)	# 3-4
    sprite('rbl052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('rbl052_02', 1)	# 1-1
    sprite('rbl052_02', 1)	# 2-2
    sprite('rbl052_02', 2)	# 3-4
    sprite('rbl052_01', 2)	# 5-6
    sprite('rbl052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('rbl052_02', 1)	# 1-1
    sprite('rbl052_03', 1)	# 2-2
    sprite('rbl052_02', 2)	# 3-4
    sprite('rbl052_02', 2)	# 5-6
    sprite('rbl052_01', 2)	# 7-8
    sprite('rbl052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('rbl052_03', 1)	# 1-1
    sprite('rbl052_03', 1)	# 2-2
    sprite('rbl052_03', 2)	# 3-4
    sprite('rbl052_02', 2)	# 5-6
    sprite('rbl052_02', 2)	# 7-8
    sprite('rbl052_01', 2)	# 9-10
    sprite('rbl052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('rbl054_00', 1)	# 1-1
    sprite('rbl054_01', 1)	# 2-2
    sprite('rbl054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('rbl054_01', 1)	# 1-1
    sprite('rbl054_02', 1)	# 2-2
    sprite('rbl054_01', 2)	# 3-4
    sprite('rbl054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('rbl054_02', 1)	# 1-1
    sprite('rbl054_02', 1)	# 2-2
    sprite('rbl054_02', 2)	# 3-4
    sprite('rbl054_01', 2)	# 5-6
    sprite('rbl054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('rbl054_02', 1)	# 1-1
    sprite('rbl054_03', 1)	# 2-2
    sprite('rbl054_02', 2)	# 3-4
    sprite('rbl054_02', 2)	# 5-6
    sprite('rbl054_01', 2)	# 7-8
    sprite('rbl054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('rbl054_03', 1)	# 1-1
    sprite('rbl054_03', 1)	# 2-2
    sprite('rbl054_03', 2)	# 3-4
    sprite('rbl054_02', 2)	# 5-6
    sprite('rbl054_02', 2)	# 7-8
    sprite('rbl054_01', 2)	# 9-10
    sprite('rbl054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('rbl062_00', 3)	# 1-3
    label(0)
    sprite('rbl062_01', 3)	# 4-6
    sprite('rbl062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('rbl062_03', 2)	# 1-2
    sprite('rbl062_04', 2)	# 3-4

@State
def CmnActBDownDown():
    sprite('rbl062_05', 3)	# 1-3
    sprite('rbl062_06', 3)	# 4-6
    label(0)
    sprite('rbl062_07', 3)	# 7-9
    sprite('rbl062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('rbl062_09', 2)	# 1-2
    sprite('rbl062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('ny060_09', 2)	# 1-2
    sprite('ny060_10', 2)	# 3-4
    sprite('ny060_11', 2)	# 5-6
    sprite('ny060_12', 3)	# 7-9
    sprite('ny060_13', 3)	# 10-12

@State
def CmnActBDownLoop():
    sprite('ny060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('ny061_00', 3)	# 1-3
    SFX_0('205_runjump_garden_0')
    SFX_3('nyse_03')
    sprite('ny061_01', 3)	# 4-6
    sprite('ny061_02', 3)	# 7-9
    sprite('ny061_03', 3)	# 10-12
    sprite('ny061_04', 3)	# 13-15
    sprite('ny061_05', 3)	# 16-18
    sprite('ny061_06', 3)	# 19-21
    sprite('ny061_07', 3)	# 22-24
    sprite('ny061_08', 2)	# 25-26
    sprite('ny061_09', 2)	# 27-28

@State
def CmnActFDownUpper():
    sprite('rbl063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('rbl063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('rbl063_02', 3)	# 1-3
    sprite('rbl063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('rbl063_04', 3)	# 1-3
    sprite('rbl063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('rbl063_06', 4)	# 1-4
    sprite('rbl063_07', 3)	# 5-7
    sprite('rbl063_08', 3)	# 8-10
    sprite('rbl063_09', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('rbl063_09', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('rbl064_00', 2)	# 1-2
    sprite('rbl064_01', 3)	# 3-5
    sprite('rbl064_02', 3)	# 6-8
    sprite('rbl064_03', 3)	# 9-11
    sprite('rbl064_04', 3)	# 12-14
    sprite('rbl064_05', 3)	# 15-17
    sprite('rbl010_00', 3)	# 18-20

@State
def CmnActVDownUpper():
    sprite('rbl062_00', 3)	# 1-3
    label(0)
    sprite('rbl062_01', 3)	# 4-6
    sprite('rbl062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('rbl062_03', 2)	# 1-2
    sprite('rbl062_04', 2)	# 3-4

@State
def CmnActVDownDown():
    sprite('rbl062_05', 3)	# 1-3
    sprite('rbl062_06', 3)	# 4-6
    label(0)
    sprite('rbl062_07', 3)	# 7-9
    sprite('rbl062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('rbl063_04', 3)	# 1-3
    sprite('rbl063_05', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('rbl072_00', 3)	# 1-3
    label(0)
    sprite('rbl072_01', 3)	# 4-6
    sprite('rbl072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('rbl074_00', 3)	# 1-3
    sprite('rbl074_01', 3)	# 4-6
    sprite('rbl074_02', 3)	# 7-9
    sprite('rbl074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('ny082_00', 2)	# 1-2
    sprite('ny082_00', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('rbl062_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('rbl073_00', 3)	# 1-3
    sprite('rbl073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('rbl073_02', 3)	# 1-3
    sprite('rbl073_03', 3)	# 4-6
    label(0)
    sprite('rbl063_02', 3)	# 7-9
    sprite('rbl063_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('rbl070_00', 3)	# 1-3
    label(0)
    sprite('rbl070_01', 4)	# 4-7
    sprite('rbl070_02', 4)	# 8-11
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('rbl070_03', 4)	# 1-4
    sprite('rbl070_04', 4)	# 5-8
    sprite('rbl070_05', 4)	# 9-12
    sprite('rbl070_06', 4)	# 13-16
    sprite('rbl070_07', 4)	# 17-20
    sprite('rbl070_08', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('rbl070_09', 4)	# 1-4
    sprite('rbl070_10', 2)	# 5-6
    sprite('rbl070_11', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('rbl113_00', 3)	# 1-3
    sprite('rbl113_01', 3)	# 4-6
    sprite('rbl113_02', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('rbl113_00', 3)	# 1-3
    sprite('rbl113_01', 3)	# 4-6
    sprite('rbl113_02', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('rbl113_00', 3)	# 1-3
    sprite('rbl113_01', 3)	# 4-6
    sprite('rbl113_02', 9)	# 7-15

@State
def CmnActUkemiLandF():
    sprite('ny110_00', 2)	# 1-2
    sprite('ny110_01', 2)	# 3-4
    sprite('ny110_02', 2)	# 5-6
    sprite('ny110_03', 2)	# 7-8
    sprite('ny110_04', 2)	# 9-10
    sprite('ny110_05', 2)	# 11-12
    sprite('ny110_06', 2)	# 13-14
    sprite('ny110_07', 2)	# 15-16
    sprite('ny110_08', 200)	# 17-216
    sprite('ny110_09', 3)	# 217-219
    sprite('ny110_10', 3)	# 220-222

@State
def CmnActUkemiLandB():
    sprite('ny111_00', 3)	# 1-3
    sprite('ny111_01', 3)	# 4-6
    sprite('ny111_02', 3)	# 7-9
    sprite('ny111_03', 3)	# 10-12
    sprite('ny111_04', 3)	# 13-15
    sprite('ny111_06', 3)	# 16-18
    sprite('ny111_07', 200)	# 19-218
    sprite('ny111_08', 2)	# 219-220
    sprite('ny111_09', 2)	# 221-222
    sprite('ny111_10', 2)	# 223-224

@State
def CmnActUkemiLandN():
    sprite('rbl112_00', 2)	# 1-2
    sprite('rbl112_01', 2)	# 3-4
    sprite('rbl112_02', 2)	# 5-6
    sprite('rbl112_03', 2)	# 7-8
    sprite('rbl112_04', 2)	# 9-10
    sprite('rbl112_05', 2)	# 11-12
    sprite('rbl112_06', 2)	# 13-14
    sprite('rbl112_07', 2)	# 15-16
    label(0)
    sprite('rbl020_07', 3)	# 17-19
    sprite('rbl020_08', 3)	# 20-22
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('rbl010_00', 5)	# 1-5
    sprite('rbl010_01', 5)	# 6-10
    sprite('rbl010_00', 5)	# 11-15

@State
def CmnActMidGuardPre():
    sprite('rbl040_00', 3)	# 1-3
    sprite('rbl040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('rbl040_02', 3)	# 1-3
    sprite('rbl040_03', 3)	# 4-6
    sprite('rbl040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('rbl040_01', 3)	# 1-3
    sprite('rbl040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('rbl040_02', 3)	# 1-3
    sprite('rbl040_03', 3)	# 4-6
    sprite('rbl040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('rbl040_01', 3)	# 1-3
    sprite('rbl040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('rbl040_00', 3)	# 1-3
    sprite('rbl040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('rbl040_02', 3)	# 1-3
    sprite('rbl040_03', 3)	# 4-6
    sprite('rbl040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('rbl040_01', 3)	# 1-3
    sprite('rbl040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('rbl040_02', 3)	# 1-3
    sprite('rbl040_03', 3)	# 4-6
    sprite('rbl040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('rbl040_01', 3)	# 1-3
    sprite('rbl040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('rbl043_00', 3)	# 1-3
    sprite('rbl043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('rbl043_02', 3)	# 1-3
    sprite('rbl043_03', 3)	# 4-6
    sprite('rbl043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('rbl043_01', 3)	# 1-3
    sprite('rbl043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('rbl043_02', 3)	# 1-3
    sprite('rbl043_03', 3)	# 4-6
    sprite('rbl043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('rbl043_01', 3)	# 1-3
    sprite('rbl043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('rbl045_00', 3)	# 1-3
    sprite('rbl045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('rbl045_02', 3)	# 1-3
    sprite('rbl045_03', 3)	# 4-6
    sprite('rbl045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('rbl045_01', 3)	# 1-3
    sprite('rbl045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('rbl045_02', 3)	# 1-3
    sprite('rbl045_03', 3)	# 4-6
    sprite('rbl045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('rbl045_01', 3)	# 1-3
    sprite('rbl045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('rbl040_04', 2)	# 1-2
    sprite('rbl040_04', 2)	# 3-4
    sprite('rbl040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('rbl040_02', 4)	# 6-9
    sprite('rbl040_01', 4)	# 10-13
    sprite('rbl040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('rbl043_04', 2)	# 1-2
    sprite('rbl043_04', 2)	# 3-4
    sprite('rbl043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('rbl043_02', 4)	# 6-9
    sprite('rbl043_01', 4)	# 10-13
    sprite('rbl043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('rbl045_04', 2)	# 1-2
    sprite('rbl045_04', 2)	# 3-4
    sprite('rbl045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('rbl045_02', 4)	# 6-9
    sprite('rbl045_01', 4)	# 10-13
    sprite('rbl045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('rbl025_00', 4)	# 1-4
    sprite('rbl025_01', 4)	# 5-8
    sprite('rbl025_00ex01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('rbl312_00', 3)	# 1-3
    sprite('rbl312_01', 2)	# 4-5
    sprite('rbl312_02', 3)	# 6-8	 **attackbox here**
    sprite('rbl312_03', 3)	# 9-11
    sprite('rbl312_04', 3)	# 12-14
    sprite('rbl312_05', 3)	# 15-17
    sprite('rbl312_06', 4)	# 18-21
    sprite('rbl312_07', 4)	# 22-25
    sprite('rbl312_08', 4)	# 26-29

@State
def CmnActAirLockWait():
    sprite('ny045_02', 1)	# 1-1
    sprite('ny045_01', 3)	# 2-4
    sprite('ny045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ny322_00', 2)	# 1-2
    sprite('ny322_01', 2)	# 3-4
    sprite('ny322_02', 2)	# 5-6
    sprite('ny322_03', 8)	# 7-14
    sprite('ny322_04', 4)	# 15-18
    sprite('ny322_05', 3)	# 19-21
    sprite('ny322_06', 3)	# 22-24
    sprite('ny322_07', 3)	# 25-27
    sprite('ny322_08', 2)	# 28-29

@State
def CmnActLandSpin():
    sprite('ny071_00', 3)	# 1-3
    sprite('ny071_01', 3)	# 4-6
    sprite('ny071_02', 3)	# 7-9
    label(0)
    sprite('ny071_03', 2)	# 10-11
    sprite('ny071_04', 2)	# 12-13
    sprite('ny071_05', 2)	# 14-15
    sprite('ny071_06', 2)	# 16-17
    sprite('ny071_07', 2)	# 18-19
    sprite('ny071_08', 2)	# 20-21
    sprite('ny071_09', 2)	# 22-23
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ny071_10', 6)	# 1-6
    sprite('ny071_11', 5)	# 7-11
    sprite('ny071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('ny071_03', 2)	# 1-2
    sprite('ny071_04', 2)	# 3-4
    sprite('ny071_05', 2)	# 5-6
    sprite('ny071_06', 2)	# 7-8
    sprite('ny071_07', 2)	# 9-10
    sprite('ny071_08', 2)	# 11-12
    sprite('ny071_09', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('rbl077_00', 2)	# 1-2
    sprite('rbl077_01', 2)	# 3-4
    sprite('rbl077_00ex00', 2)	# 5-6
    sprite('rbl077_01ex00', 2)	# 7-8
    sprite('rbl077_00ex01', 2)	# 9-10
    sprite('rbl077_01ex01', 2)	# 11-12
    sprite('rbl077_00ex02', 2)	# 13-14
    sprite('rbl077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('rbl077_02', 4)	# 1-4
    label(0)
    sprite('rbl077_03', 3)	# 5-7
    sprite('rbl077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('rbl077_05', 5)	# 1-5
    sprite('rbl077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ny060_07', 3)	# 1-3
    label(0)
    sprite('ny060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ny060_11', 4)	# 1-4
    sprite('ny060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('ny331_00', 2)	# 1-2
    label(0)
    sprite('ny331_01', 3)	# 3-5
    sprite('ny331_02', 3)	# 6-8
    sprite('ny331_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ny331_04', 2)	# 1-2
    label(0)
    sprite('ny331_05', 3)	# 3-5
    sprite('ny331_06', 3)	# 6-8
    sprite('ny331_07', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ny331_08', 2)	# 1-2
    sprite('ny331_09', 2)	# 3-4
    sprite('ny331_10', 2)	# 5-6

@State
def CmnActAirBurstBegin():
    sprite('ny332_00', 2)	# 1-2
    label(0)
    sprite('ny332_01', 3)	# 3-5
    sprite('ny332_02', 3)	# 6-8
    sprite('ny332_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ny332_04', 2)	# 1-2
    label(0)
    sprite('ny332_05', 3)	# 3-5
    sprite('ny332_06', 3)	# 6-8
    sprite('ny332_07', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ny332_08', 3)	# 1-3
    sprite('ny332_09', 3)	# 4-6
    sprite('ny332_10', 3)	# 7-9
    sprite('ny020_04', 3)	# 10-12
    sprite('ny020_05', 3)	# 13-15
    label(0)
    sprite('ny020_06', 4)	# 16-19
    sprite('ny020_07', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('rbl333_00', 3)	# 1-3
    sprite('rbl333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('rbl333_02', 3)	# 1-3
    label(0)
    sprite('rbl333_03', 3)	# 4-6
    sprite('rbl333_04', 3)	# 7-9
    sprite('rbl333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('rbl333_06', 4)	# 5-8
    sprite('rbl333_07', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('rbl333_08', 3)	# 1-3
    sprite('rbl333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('rbl333_02', 3)	# 1-3
    label(0)
    sprite('rbl333_03', 3)	# 4-6
    sprite('rbl333_04', 3)	# 7-9
    sprite('rbl333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('rbl333_09', 3)	# 1-3
    sprite('rbl333_10', 3)	# 4-6
    sprite('rbl020_05', 3)	# 7-9
    sprite('rbl020_06', 3)	# 10-12
    label(0)
    sprite('rbl020_07', 4)	# 13-16
    sprite('rbl020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('rbl333_00', 3)	# 1-3
    sprite('rbl333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('rbl333_02', 3)	# 1-3
    label(0)
    sprite('rbl333_03', 3)	# 4-6
    sprite('rbl333_04', 3)	# 7-9
    sprite('rbl333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('rbl333_06', 4)	# 5-8
    sprite('rbl333_07', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('rbl333_08', 3)	# 1-3
    sprite('rbl333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('rbl333_02', 3)	# 1-3
    label(0)
    sprite('rbl333_03', 3)	# 4-6
    sprite('rbl333_04', 3)	# 7-9
    sprite('rbl333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('rbl333_09', 3)	# 1-3
    sprite('rbl333_10', 3)	# 4-6
    sprite('rbl020_05', 3)	# 7-9
    sprite('rbl020_06', 3)	# 10-12
    label(0)
    sprite('rbl020_07', 4)	# 13-16
    sprite('rbl020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('rbl333_00', 3)	# 1-3
    sprite('rbl333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('rbl333_02', 3)	# 1-3
    label(0)
    sprite('rbl333_03', 3)	# 4-6
    sprite('rbl333_04', 3)	# 7-9
    sprite('rbl333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('keep', 4)	# 1-4
    sprite('rbl333_06', 4)	# 5-8
    sprite('rbl333_07', 4)	# 9-12

@State
def CmnActAirCrossChangeBegin():
    sprite('rbl333_08', 3)	# 1-3
    sprite('rbl333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('rbl333_02', 3)	# 1-3
    label(0)
    sprite('rbl333_03', 3)	# 4-6
    sprite('rbl333_04', 3)	# 7-9
    sprite('rbl333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('rbl333_09', 3)	# 1-3
    sprite('rbl333_10', 3)	# 4-6
    sprite('rbl020_05', 3)	# 7-9
    sprite('rbl020_06', 3)	# 10-12
    label(0)
    sprite('rbl020_07', 4)	# 13-16
    sprite('rbl020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        EnableCollision(0)
        Unknown2034(0)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767

@State
def CmnActChangePartnerAppeal():
    pass

@State
def CmnActChangePartnerAppealAir():
    pass

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)
        DisableAttackRestOfMove()

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 28)	# 603-630
    sprite('rbl272_02', 2)	# 631-632
    Unknown1086(22)
    teleportRelativeX(-1800000)
    teleportRelativeY(500000)
    physicsXImpulse(300000)
    physicsYImpulse(-100000)
    sprite('rbl272_03', 32767)	# 633-33399	 **attackbox here**
    label(1)
    sprite('rbl272_03ex01', 3)	# 33400-33402	 **attackbox here**
    GFX_0('ShadowObjectBurst', -1)
    Unknown36(1)
    Unknown1019(65)
    Unknown35()
    Unknown1019(30)
    sprite('rbl272_04', 3)	# 33403-33405
    Unknown1019(50)
    sprite('rbl272_05', 3)	# 33406-33408
    Unknown1019(50)
    sprite('rbl272_06', 4)	# 33409-33412
    Unknown1084(1)
    sprite('rbl272_07', 4)	# 33413-33416
    sprite('rbl272_08', 4)	# 33417-33420
    sprite('rbl272_09', 4)	# 33421-33424

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rbl033_01', 3)	# 1-3
    sprite('rbl033_02', 3)	# 4-6
    sprite('rbl033_01', 3)	# 7-9
    sprite('rbl033_02', 3)	# 10-12
    sprite('rbl033_01', 3)	# 13-15
    sprite('rbl033_02', 3)	# 16-18
    sprite('rbl033_01', 3)	# 19-21
    sprite('rbl033_02', 3)	# 22-24
    sprite('rbl033_01', 3)	# 25-27
    sprite('rbl033_02', 3)	# 28-30
    sprite('rbl033_01', 30)	# 31-60

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
        loopRelated(17, 66)

        def upon_17():
            sendToLabel(1)
    sprite('rbl350_00', 5)	# 1-5
    sprite('rbl350_01', 5)	# 6-10
    sprite('rbl350_02', 5)	# 11-15
    sprite('rbl350_03', 5)	# 16-20
    label(0)
    sprite('rbl350_04', 4)	# 21-24
    sprite('rbl350_05', 4)	# 25-28
    sprite('rbl350_06', 4)	# 29-32
    gotoLabel(0)
    label(1)
    sprite('rbl350_07', 5)	# 33-37
    sprite('rbl350_08', 5)	# 38-42

@State
def CmnActChangeRequest():
    pass

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 10)	# 121-130
    sprite('null', 1)	# 131-131
    Unknown1086(22)
    teleportRelativeX(-2100000)
    Unknown1007(500000)
    setGravity(1000)
    physicsXImpulse(100000)
    physicsYImpulse(-16000)
    sprite('rbl271_09', 2)	# 132-133
    sprite('rbl271_10', 3)	# 134-136
    sprite('rbl271_11', 3)	# 137-139
    sprite('rbl272_00', 3)	# 140-142
    sprite('rbl272_01', 3)	# 143-145
    sprite('rbl272_02', 3)	# 146-148
    sprite('rbl272_03ex01', 3)	# 149-151	 **attackbox here**
    GFX_0('ShadowObjectBurst', -1)
    teleportRelativeY(0)
    sprite('rbl272_04', 5)	# 152-156
    Unknown1019(25)
    sprite('rbl272_05', 5)	# 157-161
    Unknown1019(25)
    sprite('rbl272_06', 5)	# 162-166
    Unknown1084(1)
    sprite('rbl272_07', 5)	# 167-171
    sprite('rbl272_08', 5)	# 172-176
    sprite('rbl272_09', 5)	# 177-181

@State
def CmnActChangeReturnAppealBurst():
    sprite('rbl300_00', 6)	# 1-6
    sprite('rbl300_01', 6)	# 7-12
    sprite('rbl300_02', 6)	# 13-18
    sprite('rbl300_03', 6)	# 19-24
    sprite('rbl300_04', 6)	# 25-30
    sprite('rbl300_05', 6)	# 31-36
    sprite('rbl300_06', 30)	# 37-66
    sprite('rbl300_05', 6)	# 67-72
    sprite('rbl300_04', 6)	# 73-78
    sprite('rbl300_03', 6)	# 79-84
    sprite('rbl300_02', 6)	# 85-90
    sprite('rbl300_01', 6)	# 91-96
    sprite('rbl300_00', 6)	# 97-102
    sprite('rbl000_00', 6)	# 103-108
    loopRest()

@State
def CmnActChangePartnerQuickIn():
    sprite('rbl032_07', 3)	# 1-3
    sprite('rbl032_08', 3)	# 4-6
    sprite('rbl032_09', 3)	# 7-9
    sprite('rbl032_10', 4)	# 10-13
    sprite('rbl032_11', 4)	# 14-17
    sprite('rbl032_12', 4)	# 18-21
    sprite('rbl032_13', 4)	# 22-25
    sprite('rbl032_14', 4)	# 26-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('rbl033_00', 3)	# 1-3
    sprite('rbl033_01', 2)	# 4-5
    Unknown3001(255)
    Unknown3004(-42)
    Unknown23001(0, 0)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rbl033_01', 1)	# 6-6
    sprite('rbl033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rbl033_01', 3)	# 10-12
    sprite('rbl033_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl033_03', 3)	# 16-18
    Unknown1084(1)
    sprite('rbl033_04', 3)	# 19-21

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(99)
    sprite('null', 2)	# 1-2
    label(0)
    sprite('rbl020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('rbl020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('rbl010_01', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 4006):
                clearUponHandler(43)
                sendToLabel(0)
        Unknown2004(1, 0)
    sprite('rbl000_00', 6)	# 1-6
    sprite('rbl401_00', 6)	# 7-12
    tag_voice(1, 'rbl202_0', 'rbl202_1', 'rbl202_2', '')
    sprite('rbl401_01', 6)	# 13-18
    sprite('rbl401_02', 6)	# 19-24
    sprite('rbl401_03', 3)	# 25-27
    SFX_3('rblse_00')
    SLOT_51 = 1
    sprite('rbl401_04', 3)	# 28-30
    GFX_0('LandShotAtkObjC', 0)
    Unknown38(6, 1)
    Unknown23029(6, 4008, 0)
    sprite('rbl401_05', 4)	# 31-34
    sprite('rbl401_06', 4)	# 35-38
    sprite('rbl401_07', 4)	# 39-42
    sprite('rbl401_08', 4)	# 43-46
    gotoLabel(1)
    label(0)
    sprite('keep', 2)	# 47-48
    label(1)
    sprite('rbl401_09', 4)	# 49-52
    clearUponHandler(43)
    Unknown23029(6, 4007, 0)
    sprite('rbl401_10', 3)	# 53-55
    sprite('rbl401_11', 3)	# 56-58
    tag_voice(0, 'rbl203_0', 'rbl203_1', 'rbl203_2', '')
    sprite('rbl401_12', 3)	# 59-61
    sprite('rbl401_13', 4)	# 62-65
    sprite('rbl401_14', 4)	# 66-69
    SLOT_51 = 0
    Recovery()
    sprite('rbl401_15', 4)	# 70-73

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1600)
        AttackP1(70)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(2500)
        AirPushbackY(50000)
        Unknown11001(0, 6, 8)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11042(1)
    sprite('rbl404_00', 3)	# 1-3
    sprite('rbl404_01', 3)	# 4-6
    sprite('rbl404_02', 3)	# 7-9
    tag_voice(1, 'rbl206_0', 'rbl206_1', 'rbl206_2', '')
    sprite('rbl404_03', 3)	# 10-12
    SFX_0('006_swing_blade_2')
    physicsXImpulse(20000)
    physicsYImpulse(25000)
    sprite('rbl404_04', 5)	# 13-17	 **attackbox here**
    GFX_0('rblef404_Slash', -1)
    Unknown1019(50)
    Unknown1043()
    RefreshMultihit()
    sprite('rbl404_05', 3)	# 18-20
    Recovery()
    sprite('rbl404_06', 3)	# 21-23
    sprite('rbl404_07', 3)	# 24-26
    sprite('rbl404_08', 3)	# 27-29
    sprite('rbl404_09', 3)	# 30-32
    sprite('rbl404_10', 3)	# 33-35
    sprite('rbl404_11', 3)	# 36-38
    sprite('rbl404_12', 3)	# 39-41
    sprite('rbl404_13', 3)	# 42-44
    sprite('rbl020_05', 3)	# 45-47
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(11)
    sprite('rbl020_06', 3)	# 48-50
    label(10)
    sprite('rbl020_07', 3)	# 51-53
    sprite('rbl020_08', 3)	# 54-56
    gotoLabel(10)
    label(11)
    sprite('rbl010_02', 6)	# 57-62
    sprite('rbl010_01', 6)	# 63-68
    sprite('rbl010_00', 6)	# 69-74

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1350)
        AttackP1(70)
        Hitstop(6)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(2500)
        AirPushbackY(20000)
        AirUntechableTime(25)
        Unknown11057(750)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11042(1)

        def upon_12():
            clearUponHandler(12)
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(3)

        def upon_8():
            Unknown2005()
            if (SLOT_40 < 0):
                Unknown21005(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('rbl403_00', 3)	# 1-3
    sprite('rbl403_01', 3)	# 4-6
    Unknown1084(1)
    sprite('rbl403_02', 3)	# 7-9
    sprite('rbl403_03', 3)	# 10-12
    sprite('rbl403_04', 3)	# 13-15
    GFX_0('rblef403_Slash_Assist', -1)
    SFX_3('rblse_10')
    physicsXImpulse(60000)
    Unknown3001(255)
    Unknown3004(-85)
    sprite('rbl403_05_EX', 9)	# 16-24	 **attackbox here**
    physicsYImpulse(7500)
    EnableCollision(0)
    Unknown2015(50)
    Unknown3001(0)
    Unknown3004(0)
    sprite('rbl403_05', 2)	# 25-26	 **attackbox here**
    clearUponHandler(2)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(100)
    Unknown3001(255)
    Unknown3004(0)
    YAccel(200)
    Unknown1043()
    StartMultihit()
    sprite('rbl403_06', 2)	# 27-28
    Unknown1019(50)
    EnableCollision(1)
    Unknown2015(100)
    sprite('rbl403_07', 2)	# 29-30
    Unknown1019(50)
    sprite('rbl403_08', 2)	# 31-32
    sprite('rbl403_09', 2)	# 33-34
    Unknown14077(0)
    sprite('rbl403_10', 4)	# 35-38
    sprite('rbl403_11', 4)	# 39-42
    sprite('rbl403_12', 4)	# 43-46
    sprite('rbl403_13', 30)	# 47-76
    label(100)
    sprite('rbl010_01', 3)	# 77-79
    Unknown2005()
    sprite('rbl010_00', 3)	# 80-82
    ExitState()
    label(1)
    sprite('rbl403_05', 3)	# 83-85	 **attackbox here**
    Unknown3001(255)
    Unknown3004(0)
    YAccel(150)
    StartMultihit()
    sprite('null', 3)	# 86-88
    StartMultihit()
    GFX_0('ShadowObjectAssaultA', -1)
    tag_voice(1, 'rbl207_0', 'rbl207_1', 'rbl207_2', '')
    sprite('rbl406_00', 2)	# 89-90
    SFX_3('rblse_10')
    Unknown2006()
    Unknown1019(25)
    setGravity(0)
    teleportRelativeX(50000)
    Unknown1007(100000)
    sprite('rbl406_01', 2)	# 91-92
    sprite('rbl406_02', 2)	# 93-94
    sprite('rbl406_03', 2)	# 95-96
    physicsXImpulse(10000)
    physicsYImpulse(-5000)
    GFX_0('rblef406', -1)
    sprite('rbl406_04', 3)	# 97-99	 **attackbox here**
    Unknown1019(1000)
    YAccel(1500)
    RefreshMultihit()
    AttackLevel_(4)
    Unknown11099(1)
    Damage(1500)
    AirPushbackX(5000)
    AirPushbackY(25000)
    AirUntechableTime(60)
    Hitstop(9)
    label(2)
    sprite('rbl406_05', 3)	# 100-102	 **attackbox here**
    sprite('rbl406_04', 3)	# 103-105	 **attackbox here**
    gotoLabel(2)
    label(3)
    sprite('rbl406_06', 4)	# 106-109
    EnableCollision(1)
    Unknown1019(25)
    Recovery()
    Unknown21012('72626c656634303600000000000000000000000000000000000000000000000021000000')
    Unknown21012('72626c65663430365f426c6f6f6d00000000000000000000000000000000000021000000')
    sprite('rbl406_07', 4)	# 110-113
    Unknown1019(50)
    sprite('rbl406_08', 4)	# 114-117
    Unknown1019(50)
    sprite('rbl406_09', 4)	# 118-121
    Unknown1084(1)
    sprite('rbl406_10', 4)	# 122-125
    sprite('rbl406_11', 4)	# 126-129
    sprite('rbl406_12', 4)	# 130-133

@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        if SLOT_162:
            SLOT_58 = 1

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)	# 1-1
    Unknown2036(113, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-500000)
    Unknown1019(4)
    label(0)
    sprite('rbl020_07', 3)	# 3-5
    sprite('rbl020_08', 3)	# 6-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 9-18
    if SLOT_58:
        enterState('UltimateDUOSP')
    else:
        enterState('UltimateDUO')

@State
def UltimateDUO():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
        Unknown30063(1)
    sprite('rbl430_00', 5)	# 1-5
    sprite('rbl430_01', 5)	# 6-10
    sprite('rbl430_02', 5)	# 11-15
    label(0)
    sprite('rbl430_03', 3)	# 16-18
    sprite('rbl430_04', 3)	# 19-21
    sprite('rbl430_05', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rbl430_06', 5)	# 25-29
    tag_voice(1, 'rbl291_0', 'rbl291_1', '', '')
    sprite('rbl430_07', 5)	# 30-34
    sprite('rbl430_08', 5)	# 35-39
    sprite('rbl430_09', 5)	# 40-44
    sprite('rbl430_10', 5)	# 45-49
    sprite('rbl430_11', 3)	# 50-52
    SFX_3('rblse_36')
    sprite('rbl430_12', 2)	# 53-54
    GFX_0('UltimateShotObj', -1)
    Unknown23029(1, 4303, 0)
    sprite('rbl430_13', 2)	# 55-56
    Unknown21012('72626c656634333000000000000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('rbl430_14', 3)	# 57-59
    sprite('rbl430_15', 3)	# 60-62
    sprite('rbl430_16', 3)	# 63-65
    sprite('rbl430_14', 4)	# 66-69
    sprite('rbl430_15', 4)	# 70-73
    sprite('rbl430_16', 4)	# 74-77
    sprite('rbl430_14', 5)	# 78-82
    sprite('rbl430_15', 5)	# 83-87
    sprite('rbl430_16', 5)	# 88-92
    sprite('rbl430_17', 5)	# 93-97
    sprite('rbl430_18', 5)	# 98-102

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
        Unknown30063(1)
    sprite('rbl430_00', 5)	# 1-5
    sprite('rbl430_01', 5)	# 6-10
    sprite('rbl430_02', 5)	# 11-15
    label(0)
    sprite('rbl430_03', 3)	# 16-18
    sprite('rbl430_04', 3)	# 19-21
    sprite('rbl430_05', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rbl430_06', 5)	# 25-29
    tag_voice(1, 'rbl291_0', 'rbl291_1', '', '')
    sprite('rbl430_07', 5)	# 30-34
    sprite('rbl430_08', 5)	# 35-39
    sprite('rbl430_09', 5)	# 40-44
    sprite('rbl430_10', 5)	# 45-49
    sprite('rbl430_11', 3)	# 50-52
    SFX_3('rblse_36')
    sprite('rbl430_12', 2)	# 53-54
    GFX_0('UltimateShotObj', -1)
    Unknown23029(1, 4304, 0)
    sprite('rbl430_13', 2)	# 55-56
    sprite('rbl430_14', 3)	# 57-59
    sprite('rbl430_15', 3)	# 60-62
    sprite('rbl430_16', 3)	# 63-65
    sprite('rbl430_19', 3)	# 66-68
    sprite('rbl430_20', 3)	# 69-71
    SFX_3('rblse_36')
    sprite('rbl430_21', 2)	# 72-73
    GFX_0('UltimateShotObj', -1)
    Unknown23029(1, 4305, 0)
    sprite('rbl430_21', 1)	# 74-74
    setInvincible(0)
    sprite('rbl430_22', 3)	# 75-77
    Unknown21012('72626c656634333000000000000000000000000000000000000000000000000020000000')
    sprite('rbl430_23', 3)	# 78-80
    sprite('rbl430_24', 3)	# 81-83
    sprite('rbl430_25', 3)	# 84-86
    sprite('rbl430_23', 4)	# 87-90
    sprite('rbl430_24', 4)	# 91-94
    sprite('rbl430_25', 4)	# 95-98
    sprite('rbl430_23', 5)	# 99-103
    sprite('rbl430_24', 5)	# 104-108
    sprite('rbl430_25', 5)	# 109-113
    sprite('rbl430_26', 5)	# 114-118
    sprite('rbl430_27', 5)	# 119-123

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 30)	# 1-30
    sprite('null', 1)	# 31-31
    teleportRelativeX(-25000)
    Unknown1007(600000)
    setGravity(0)
    physicsYImpulse(-60000)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    sprite('rbl407_03', 3)	# 32-34	 **attackbox here**
    sprite('rbl407_03', 32767)	# 35-32801	 **attackbox here**
    GFX_0('rblef407', -1)
    label(1)
    sprite('keep', 1)	# 32802-32802
    sprite('rbl010_00', 7)	# 32803-32809
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    StartMultihit()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rbl010_01', 16)	# 32810-32825
    sprite('rbl010_00', 7)	# 32826-32832

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('rbl010_01', 10)	# 2-11
    StartMultihit()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rbl010_00', 4)	# 12-15
    sprite('rbl320_00', 8)	# 16-23
    sprite('rbl320_01', 8)	# 24-31
    sprite('rbl320_02', 3)	# 32-34
    Unknown7009(5)
    sprite('rbl320_03', 3)	# 35-37	 **attackbox here**
    GFX_0('rblef320', -1)
    sprite('rbl320_04', 3)	# 38-40
    sprite('rbl320_05', 3)	# 41-43
    sprite('rbl320_06', 3)	# 44-46
    sprite('rbl320_05', 3)	# 47-49
    sprite('rbl320_06', 3)	# 50-52
    sprite('rbl320_07', 4)	# 53-56
    sprite('rbl320_08', 4)	# 57-60
    sprite('rbl320_09', 3)	# 61-63
    sprite('rbl320_10', 3)	# 64-66
    sprite('rbl320_11', 3)	# 67-69
    sprite('rbl320_12', 3)	# 70-72
    sprite('rbl320_13', 3)	# 73-75

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        AirPushbackY(15000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('DashCancel')
        HitOrBlockJumpCancel(1)
        SLOT_59 = 1
    sprite('rbl200_00', 3)	# 1-3
    sprite('rbl200_01', 2)	# 4-5
    Unknown7009(0)
    SFX_0('007_swing_knife_0')
    sprite('rbl200_02', 3)	# 6-8	 **attackbox here**
    GFX_0('rblef200', -1)
    sprite('rbl200_03', 3)	# 9-11
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('rbl200_04', 3)	# 12-14
    sprite('rbl200_05', 4)	# 15-18

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(1200)
        AttackP2(80)
        Unknown9016(1)
        PushbackX(12000)
        AirPushbackY(15000)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('DashCancel')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
        SLOT_59 = 2
    sprite('rbl201_00', 4)	# 1-4
    sprite('rbl201_01', 2)	# 5-6
    SFX_0('010_swing_sword_1')
    sprite('rbl201_02', 2)	# 7-8
    Unknown7009(0)
    GFX_0('rblef201', -1)
    sprite('rbl201_03', 4)	# 9-12	 **attackbox here**
    sprite('rbl201_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('rbl201_05', 4)	# 17-20
    sprite('rbl201_06', 3)	# 21-23
    sprite('rbl201_07', 3)	# 24-26
    sprite('rbl201_08', 3)	# 27-29

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AttackP2(80)
        AirPushbackY(15000)
        Hitstop(6)
        PushbackX(8000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('DashCancel')
        HitOrBlockJumpCancel(1)
        SLOT_59 = 1
    sprite('rbl201_06', 2)	# 1-2
    sprite('rbl200_00', 3)	# 3-5
    physicsXImpulse(5000)
    sprite('rbl200_01', 2)	# 6-7
    Unknown1019(400)
    Unknown7009(0)
    SFX_0('007_swing_knife_0')
    sprite('rbl200_02', 3)	# 8-10	 **attackbox here**
    Unknown1019(25)
    GFX_0('rblef200', -1)
    sprite('rbl200_03', 4)	# 11-14
    Unknown1019(25)
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('rbl200_04', 4)	# 15-18
    Unknown1019(0)
    sprite('rbl200_05', 5)	# 19-23

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AttackP2(80)
        Unknown9016(1)
        AirPushbackY(20000)
        PushbackX(12000)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('DashCancel')
        HitOrBlockJumpCancel(1)
        SLOT_59 = 4
    sprite('keep', 2)	# 1-2
    StartMultihit()
    sprite('rbl270_00', 3)	# 3-5
    sprite('rbl270_01', 2)	# 6-7
    physicsXImpulse(5000)
    sprite('rbl270_02', 2)	# 8-9
    Unknown1019(50)
    SFX_0('007_swing_knife_1')
    sprite('rbl270_03', 3)	# 10-12	 **attackbox here**
    Unknown1019(50)
    GFX_0('rblef270', -1)
    sprite('rbl270_04', 2)	# 13-14
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('rbl270_05', 2)	# 15-16
    sprite('rbl270_06', 2)	# 17-18
    sprite('rbl270_07', 3)	# 19-21
    sprite('rbl270_08', 3)	# 22-24

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1400)
        Unknown11092(1)
        AirPushbackX(-7500)
        AirPushbackY(15000)
        PushbackX(-10000)
        AirUntechableTime(23)
        Hitstop(3)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown14077(0)
        HitOrBlockCancel('NmlAtk5AAAAA')
        HitOrBlockCancel('NmlAtkAIR2A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        Unknown28(2, 'CmnActJumpLanding')
    sprite('keep', 2)	# 1-2
    StartMultihit()
    sprite('rbl271_00', 3)	# 3-5
    sprite('rbl271_01', 3)	# 6-8
    teleportRelativeX(50000)
    Unknown7009(1)
    GFX_0('rblef271_1', -1)
    sprite('rbl271_02', 2)	# 9-10	 **attackbox here**
    physicsXImpulse(-12000)
    physicsYImpulse(30000)
    Unknown1043()
    sprite('rbl271_03', 2)	# 11-12
    sprite('rbl271_04', 2)	# 13-14
    sprite('rbl271_05', 2)	# 15-16
    sprite('rbl271_06', 2)	# 17-18
    sprite('rbl271_07', 3)	# 19-21	 **attackbox here**
    GFX_0('rblef271_2', -1)
    RefreshMultihit()
    AirPushbackX(0)
    AirPushbackY(15000)
    Hitstop(11)
    Unknown14077(1)
    sprite('rbl271_08', 3)	# 22-24
    Recovery()
    Unknown2063()
    sprite('rbl271_09', 4)	# 25-28
    sprite('rbl271_10', 4)	# 29-32
    sprite('rbl271_11', 4)	# 33-36
    sprite('rbl020_05', 3)	# 37-39
    sprite('rbl020_06', 3)	# 40-42
    label(0)
    sprite('rbl020_07', 3)	# 43-45
    sprite('rbl020_08', 3)	# 46-48
    gotoLabel(0)

@State
def NmlAtk5AAAAA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1800)
        AttackP1(100)
        AirPushbackX(2500)
        AirPushbackY(-80000)
        AirUntechableTime(30)
        Unknown9190(1)
        Unknown9118(15)
        Unknown9016(1)
        HitOverhead(0)
        JumpCancel_(0)
        clearUponHandler(2)
        Unknown11044(1)
        Unknown30088(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('rbl271_09', 2)	# 2-3
    sprite('rbl271_10', 2)	# 4-5
    sprite('rbl271_11', 2)	# 6-7
    sprite('rbl272_00', 2)	# 8-9
    GFX_0('ShadowObjectNmlAtk5AAAA', -1)
    sprite('rbl272_01', 3)	# 10-12
    sprite('rbl272_02', 3)	# 13-15
    tag_voice(1, 'rbl106_0', 'rbl106_1', 'rbl106_2', '')
    sprite('rbl272_03', 3)	# 16-18	 **attackbox here**
    GFX_0('rblef272', -1)
    SFX_3('rblse_10')
    teleportRelativeX(550000)
    teleportRelativeY(0)
    physicsXImpulse(10000)
    sprite('rbl272_04', 4)	# 19-22
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('rbl272_05', 4)	# 23-26
    Unknown1019(50)
    sprite('rbl272_06', 4)	# 27-30
    Unknown1019(0)
    sprite('rbl272_07', 3)	# 31-33
    sprite('rbl272_08', 3)	# 34-36
    sprite('rbl272_09', 3)	# 37-39

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(90)
        AirUntechableTime(25)
        AirPushbackX(-7000)
        AirPushbackY(15000)
        PushbackX(-20000)
        Unknown9016(1)
        GroundedHitstunAnimation(9)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown2004(1, 0)
        Unknown1112('')

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(4, 2021, 0)
            HitOrBlockJumpCancel(1)

        def upon_43():
            if (SLOT_48 == 2022):
                DisableAttackRestOfMove()
    sprite('rbl202_00', 4)	# 1-4
    sprite('rbl202_01', 3)	# 5-7
    sprite('rbl202_02', 3)	# 8-10
    sprite('rbl202_03', 2)	# 11-12
    physicsXImpulse(10000)
    SFX_3('rblse_03')
    sprite('rbl202_04', 2)	# 13-14
    GFX_0('rblef202_Slash', -1)
    Unknown1019(50)
    sprite('rbl202_05', 3)	# 15-17	 **attackbox here**
    Unknown7009(2)
    Unknown1084(1)
    GFX_0('Atk5BLineAtkObj', -1)
    Unknown38(4, 1)
    sprite('rbl202_06', 3)	# 18-20	 **attackbox here**
    sprite('rbl202_07', 4)	# 21-24
    Recovery()
    Unknown2063()
    sprite('rbl202_08', 4)	# 25-28
    sprite('rbl202_09', 3)	# 29-31
    sprite('rbl202_10', 3)	# 32-34
    sprite('rbl202_11', 3)	# 35-37
    sprite('rbl202_12', 4)	# 38-41

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(400)
        Unknown11092(1)
        Hitstop(1)
        AirPushbackX(-3000)
        AirPushbackY(10000)
        PushbackX(9800)
        hitstun(16)
        AirUntechableTime(27)
        Unknown9016(1)
        Unknown2037(3)
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
    sprite('rbl202_06ex01', 3)	# 1-3	 **attackbox here**
    sprite('rbl273_00', 4)	# 4-7
    teleportRelativeX(30000)
    sprite('rbl273_01', 4)	# 8-11
    teleportRelativeX(30000)
    SFX_3('rblse_04')
    tag_voice(1, 'rbl107_0', 'rbl107_1', 'rbl107_2', '')
    sprite('rbl273_02', 1)	# 12-12	 **attackbox here**
    teleportRelativeX(30000)
    GFX_0('rblef273', -1)
    RefreshMultihit()
    Unknown2038(-1)
    Unknown1019(0)
    sprite('rbl273_02ex01', 1)	# 13-13	 **attackbox here**
    sprite('rbl273_02ex02', 1)	# 14-14	 **attackbox here**
    sprite('rbl273_03', 2)	# 15-16	 **attackbox here**
    SFX_3('rblse_04')
    sprite('rbl273_04', 2)	# 17-18
    label(0)
    sprite('rbl273_02', 1)	# 19-19	 **attackbox here**
    RefreshMultihit()
    Unknown2038(-1)
    sprite('rbl273_02ex01', 1)	# 20-20	 **attackbox here**
    sprite('rbl273_02ex02', 1)	# 21-21	 **attackbox here**
    sprite('rbl273_03', 2)	# 22-23	 **attackbox here**
    SFX_3('rblse_04')
    sprite('rbl273_04', 2)	# 24-25
    if SLOT_2:
        _gotolabel(0)
    sprite('rbl273_02', 1)	# 26-26	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(18000)
    Hitstop(8)
    sprite('rbl273_02ex01', 1)	# 27-27	 **attackbox here**
    sprite('rbl273_02ex02', 1)	# 28-28	 **attackbox here**
    sprite('rbl273_03', 3)	# 29-31	 **attackbox here**
    sprite('rbl273_04', 3)	# 32-34
    Recovery()
    Unknown2063()
    sprite('rbl273_05', 3)	# 35-37
    sprite('rbl273_06', 3)	# 38-40
    sprite('rbl273_07', 3)	# 41-43
    sprite('rbl202_09ex01', 2)	# 44-45
    sprite('rbl202_10ex01', 2)	# 46-47
    sprite('rbl202_11ex01', 2)	# 48-49
    sprite('rbl202_12ex01', 2)	# 50-51

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        PushbackX(15300)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk4A')
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('DashCancel')
        SLOT_59 = 3
    sprite('rbl230_00', 3)	# 1-3
    sprite('rbl230_01', 3)	# 4-6
    Unknown7009(0)
    SFX_0('003_swing_grap_0_0')
    sprite('rbl230_02', 3)	# 7-9	 **attackbox here**
    sprite('rbl230_03', 4)	# 10-13
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('rbl230_04', 3)	# 14-16
    sprite('rbl230_01', 3)	# 17-19
    sprite('rbl230_00', 3)	# 20-22

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1500)
        AirPushbackY(24000)
        AirUntechableTime(30)
        Unknown9016(1)
        AttackP1(80)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')

        def upon_ON_HIT_OR_BLOCK():
            Unknown23029(4, 2321, 0)
            HitOrBlockJumpCancel(1)

        def upon_43():
            if (SLOT_48 == 2322):
                DisableAttackRestOfMove()
    sprite('rbl232_00', 2)	# 1-2
    sprite('rbl232_01', 2)	# 3-4
    sprite('rbl232_02', 3)	# 5-7
    sprite('rbl232_03', 3)	# 8-10
    GFX_0('rblef232', -1)
    sprite('rbl232_04', 3)	# 11-13
    Unknown7009(2)
    SFX_3('rblse_02')
    sprite('rbl232_05', 3)	# 14-16
    sprite('rbl232_06', 3)	# 17-19	 **attackbox here**
    GFX_0('Atk2BLineAtkObj', -1)
    Unknown38(4, 1)
    sprite('rbl232_07', 3)	# 20-22
    Recovery()
    Unknown2063()
    sprite('rbl232_08', 3)	# 23-25
    sprite('rbl232_09', 3)	# 26-28
    sprite('rbl232_10', 3)	# 29-31
    sprite('rbl232_11', 4)	# 32-35
    sprite('rbl232_12', 4)	# 36-39
    sprite('rbl232_13', 4)	# 40-43
    sprite('rbl232_14', 4)	# 44-47

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1400)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(5000)
        AirPushbackY(13000)
        AirUntechableTime(30)
        Unknown9016(1)
        AttackP1(90)
        HitLow(2)
    sprite('rbl231_00', 3)	# 1-3
    sprite('rbl231_01', 3)	# 4-6
    Unknown7009(1)
    sprite('rbl231_02', 3)	# 7-9
    GFX_0('rblef231', -1)
    SFX_0('010_swing_sword_1')
    sprite('rbl231_03', 3)	# 10-12	 **attackbox here**
    Unknown1019(50)
    sprite('rbl231_04', 4)	# 13-16
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('rbl231_05', 4)	# 17-20
    sprite('rbl231_06', 4)	# 21-24
    sprite('rbl231_07', 4)	# 25-28
    sprite('rbl231_08', 4)	# 29-32

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Unknown9016(1)
        StarterRating(2)
        AttackP2(80)
        WhiffCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR2A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rbl250_00', 3)	# 1-3
    sprite('rbl250_01', 3)	# 4-6
    Unknown7009(3)
    SFX_0('007_swing_knife_0')
    sprite('rbl250_02', 3)	# 7-9	 **attackbox here**
    GFX_0('rblef250', -1)
    sprite('rbl250_03', 3)	# 10-12
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('rbl250_04', 3)	# 13-15
    sprite('rbl250_05', 3)	# 16-18

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1200)
        Unknown9016(1)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5AAA')
        HitOrBlockCancel('NmlAtkAIR2A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('rbl274_00', 2)	# 2-3
    sprite('rbl274_01', 2)	# 4-5
    sprite('rbl274_02', 2)	# 6-7
    SFX_0('007_swing_knife_1')
    sprite('rbl274_03', 3)	# 8-10	 **attackbox here**
    GFX_0('rblef274', -1)
    sprite('rbl274_04', 5)	# 11-15
    Recovery()
    Unknown2063()
    sprite('rbl274_05', 5)	# 16-20
    sprite('rbl274_06', 5)	# 21-25

@State
def NmlAtkAIR5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1500)
        AttackP2(85)
        Unknown9016(1)
        AirUntechableTime(30)
        AirPushbackX(25000)
        AirPushbackY(-30000)
        HitOrBlockCancel('NmlAtkAIR2A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('rbl275_00', 3)	# 2-4
    sprite('rbl275_01', 3)	# 5-7
    sprite('rbl275_02', 3)	# 8-10
    tag_voice(1, 'rbl108_0', 'rbl108_1', 'rbl108_2', '')
    SFX_0('007_swing_knife_2')
    sprite('rbl275_03', 3)	# 11-13	 **attackbox here**
    GFX_0('rblef275', -1)
    GFX_0('rblef275_Wind', -1)
    sprite('rbl275_04', 5)	# 14-18
    Recovery()
    Unknown2063()
    sprite('rbl275_05', 5)	# 19-23
    sprite('rbl275_06', 5)	# 24-28
    sprite('rbl275_07', 5)	# 29-33
    sprite('rbl275_08', 5)	# 34-38

@State
def NmlAtkAIR2A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1300)
        Unknown9016(1)
        StarterRating(2)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rbl251_00', 3)	# 1-3
    sprite('rbl251_01', 3)	# 4-6
    Unknown7009(4)
    sprite('rbl251_02', 3)	# 7-9
    GFX_0('rblef251', -1)
    SFX_0('010_swing_sword_1')
    sprite('rbl251_03', 3)	# 10-12	 **attackbox here**
    sprite('rbl251_04', 5)	# 13-17
    Recovery()
    Unknown2063()
    sprite('rbl251_05', 5)	# 18-22
    sprite('rbl251_06', 5)	# 23-27
    sprite('rbl251_07', 5)	# 28-32

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1500)
        Unknown9016(1)
        StarterRating(2)
        AirUntechableTime(25)
        AirPushbackX(8000)
        AirPushbackY(28000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR2A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOverhead(0)
        if Unknown23145('NmlAtk5AAAA'):
            if (SLOT_25 < 400000):
                Unknown1019(130)
    sprite('rbl252_00', 4)	# 1-4
    sprite('rbl252_01', 4)	# 5-8
    sprite('rbl252_02', 3)	# 9-11
    Unknown7009(5)
    SFX_3('rblse_01')
    sprite('rbl252_03', 3)	# 12-14
    sprite('rbl252_04', 3)	# 15-17
    GFX_0('rblef252', -1)
    sprite('rbl252_05', 1)	# 18-18	 **attackbox here**
    sprite('rbl252_05ex01', 1)	# 19-19	 **attackbox here**
    sprite('rbl252_05ex02', 1)	# 20-20	 **attackbox here**
    sprite('rbl252_06', 4)	# 21-24
    Recovery()
    Unknown2063()
    sprite('rbl252_07', 4)	# 25-28
    sprite('rbl252_08', 4)	# 29-32
    sprite('rbl252_09', 4)	# 33-36
    sprite('rbl252_10', 6)	# 37-42
    sprite('rbl252_11', 6)	# 43-48

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1450)
        AirPushbackY(-40000)
        Unknown9310(10)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('rbl253_00', 3)	# 1-3
    sprite('rbl253_01', 3)	# 4-6
    Unknown1019(25)
    YAccel(25)
    setGravity(800)
    sprite('rbl253_02', 3)	# 7-9
    Unknown1019(150)
    sprite('rbl203_03', 2)	# 10-11
    Unknown3001(255)
    Unknown3004(-42)
    Unknown1019(150)
    tag_voice(1, 'rbl106_0', 'rbl106_1', 'rbl106_2', '')
    sprite('rbl203_04', 2)	# 12-13
    Unknown1019(150)
    YAccel(50)
    GFX_0('DashShadowEff', -1)
    GFX_0('rblef_ShadowParticle', -1)
    SFX_3('rblse_10')
    sprite('rbl203_05', 2)	# 14-15
    clearUponHandler(2)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    label(1)
    sprite('rbl203_06', 3)	# 16-18
    Unknown1015(10000)
    teleportRelativeY(0)
    Unknown3001(0)
    Unknown3004(63)
    SFX_0('010_swing_sword_1')
    sprite('rbl203_07', 2)	# 19-20
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    GFX_0('rblef203', -1)
    sprite('rbl203_08', 3)	# 21-23	 **attackbox here**
    Unknown1019(50)
    sprite('rbl203_09', 4)	# 24-27
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('rbl203_10', 4)	# 28-31
    Unknown1084(1)
    sprite('rbl203_11', 4)	# 32-35
    sprite('rbl203_12', 4)	# 36-39
    sprite('rbl203_13', 4)	# 40-43
    sprite('rbl203_14', 4)	# 44-47
    sprite('rbl203_15', 4)	# 48-51

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('rbl010_00', 3)	# 1-3
    sprite('rbl203_00', 2)	# 4-5
    SLOT_12 = SLOT_19
    Unknown1019(5)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    physicsYImpulse(15000)
    setGravity(2000)
    Unknown23087(100000)
    tag_voice(1, 'rbl157_0', 'rbl157_1', '', '')
    sprite('rbl203_01', 2)	# 6-7
    sprite('rbl203_02', 2)	# 8-9
    label(0)
    sprite('rbl203_03', 3)	# 10-12
    sprite('rbl203_04', 3)	# 13-15
    sprite('rbl203_05', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('rbl203_06', 2)	# 19-20
    SFX_0('010_swing_sword_1')
    sprite('rbl203_07', 2)	# 21-22
    GFX_0('rblef203', -1)
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    sprite('rbl203_08', 3)	# 23-25	 **attackbox here**
    Unknown1019(50)
    sprite('rbl203_09', 3)	# 26-28
    Unknown1019(50)
    sprite('rbl203_10', 3)	# 29-31
    Unknown1084(1)
    sprite('rbl203_11', 3)	# 32-34
    sprite('rbl203_12', 3)	# 35-37
    sprite('rbl203_13', 2)	# 38-39
    sprite('rbl203_14', 2)	# 40-41
    sprite('rbl203_15', 2)	# 42-43

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
    sprite('rbl203_09', 3)	# 1-3
    Unknown1019(50)
    sprite('rbl203_10', 3)	# 4-6
    Unknown1084(1)
    sprite('rbl203_11', 3)	# 7-9
    sprite('rbl203_12', 3)	# 10-12
    sprite('rbl203_13', 3)	# 13-15
    sprite('rbl203_14', 3)	# 16-18
    sprite('rbl203_15', 3)	# 19-21
    sprite('rbl201_00', 4)	# 22-25
    sprite('rbl201_01', 2)	# 26-27
    sprite('rbl201_02', 2)	# 28-29
    GFX_0('rblef201', -1)
    sprite('rbl201_03', 4)	# 30-33	 **attackbox here**
    tag_voice(0, 'rbl158_0', 'rbl158_1', '', '')
    sprite('rbl201_04', 5)	# 34-38
    sprite('rbl201_05', 5)	# 39-43
    sprite('rbl201_06', 3)	# 44-46
    sprite('rbl201_07', 3)	# 47-49
    sprite('rbl201_08', 3)	# 50-52
    sprite('rbl000_00', 6)	# 53-58
    sprite('rbl000_01', 6)	# 59-64
    sprite('rbl000_02', 6)	# 65-70
    sprite('rbl000_03', 6)	# 71-76
    sprite('rbl000_04', 6)	# 77-82
    sprite('rbl000_05', 6)	# 83-88
    sprite('rbl000_06', 6)	# 89-94
    sprite('rbl000_07', 6)	# 95-100
    sprite('rbl000_08', 6)	# 101-106
    sprite('rbl000_09', 6)	# 107-112
    label(1)
    sprite('keep', 1)	# 113-113

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 3)	# 1-3
    StartMultihit()
    sprite('rbl430_19', 5)	# 4-8
    sprite('rbl430_20', 5)	# 9-13
    sprite('rbl430_21', 1)	# 14-14
    GFX_0('rblef430_Slash02', -1)
    sprite('rbl430_21ex01', 3)	# 15-17	 **attackbox here**
    sprite('rbl430_22', 3)	# 18-20
    sprite('rbl430_23', 3)	# 21-23
    sprite('rbl430_24', 3)	# 24-26
    sprite('rbl430_25', 3)	# 27-29
    sprite('rbl430_23', 4)	# 30-33
    sprite('rbl430_24', 4)	# 34-37
    sprite('rbl430_25', 4)	# 38-41
    sprite('rbl430_23', 5)	# 42-46
    sprite('rbl430_24', 5)	# 47-51
    sprite('rbl430_25', 5)	# 52-56
    sprite('rbl430_26', 5)	# 57-61
    sprite('rbl430_27', 5)	# 62-66
    sprite('rbl000_00', 6)	# 67-72
    sprite('rbl000_01', 6)	# 73-78
    sprite('rbl000_02', 6)	# 79-84
    sprite('rbl000_03', 6)	# 85-90
    sprite('rbl000_04', 6)	# 91-96
    sprite('rbl000_05', 6)	# 97-102
    sprite('rbl000_06', 6)	# 103-108
    sprite('rbl000_07', 6)	# 109-114
    sprite('rbl000_08', 6)	# 115-120
    sprite('rbl000_09', 6)	# 121-126
    label(1)
    sprite('keep', 1)	# 127-127

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('rbl320_00', 8)	# 1-8
    sprite('rbl320_01', 8)	# 9-16
    sprite('rbl320_02', 3)	# 17-19
    tag_voice(0, 'rbl159_0', 'rbl159_1', '', '')
    sprite('rbl320_03', 3)	# 20-22	 **attackbox here**
    GFX_0('rblef320', -1)
    sprite('rbl320_04', 3)	# 23-25
    setInvincible(0)
    sprite('rbl320_05', 3)	# 26-28
    sprite('rbl320_06', 3)	# 29-31
    sprite('rbl320_05', 3)	# 32-34
    sprite('rbl320_06', 3)	# 35-37
    sprite('rbl320_07', 4)	# 38-41
    sprite('rbl320_08', 4)	# 42-45
    sprite('rbl320_09', 4)	# 46-49
    sprite('rbl320_10', 4)	# 50-53
    sprite('rbl320_11', 4)	# 54-57
    sprite('rbl320_12', 4)	# 58-61
    sprite('rbl320_13', 4)	# 62-65

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('keep', 32767)	# 2-32768
    label(1)
    sprite('rbl320_00', 8)	# 32769-32776
    sprite('rbl320_01', 8)	# 32777-32784
    sprite('rbl320_02', 3)	# 32785-32787
    tag_voice(0, 'rbl159_0', 'rbl159_1', '', '')
    sprite('rbl320_03', 3)	# 32788-32790	 **attackbox here**
    GFX_0('rblef320', -1)
    sprite('rbl320_04', 3)	# 32791-32793
    setInvincible(0)
    sprite('rbl320_05', 3)	# 32794-32796
    sprite('rbl320_06', 3)	# 32797-32799
    sprite('rbl320_05', 3)	# 32800-32802
    sprite('rbl320_06', 3)	# 32803-32805
    sprite('rbl320_07', 4)	# 32806-32809
    sprite('rbl320_08', 4)	# 32810-32813
    sprite('rbl320_09', 4)	# 32814-32817
    sprite('rbl320_10', 4)	# 32818-32821
    sprite('rbl320_11', 4)	# 32822-32825
    sprite('rbl320_12', 4)	# 32826-32829
    sprite('rbl320_13', 4)	# 32830-32833

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
        DisableAttackRestOfMove()

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 42):
                RefreshMultihit()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 23)	# 1-23
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 24-24
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    sprite('rbl406_00', 2)	# 25-26
    sprite('rbl406_01', 2)	# 27-28
    sprite('rbl406_02', 2)	# 29-30
    sprite('rbl406_03', 2)	# 31-32
    physicsXImpulse(7500)
    physicsYImpulse(-5000)
    sprite('rbl406_04', 3)	# 33-35	 **attackbox here**
    Unknown1019(1000)
    YAccel(1000)
    sprite('rbl406_05', 3)	# 36-38	 **attackbox here**
    GFX_0('rblef406_Assist', -1)
    label(0)
    sprite('rbl406_04', 3)	# 39-41	 **attackbox here**
    sprite('rbl406_05', 3)	# 42-44	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('rbl406_06', 4)	# 45-48
    EnableCollision(1)
    Unknown1019(25)
    sprite('rbl406_07', 4)	# 49-52
    Unknown1019(50)
    sprite('rbl406_08', 4)	# 53-56
    Unknown1019(50)
    sprite('rbl406_09', 4)	# 57-60
    Unknown1084(1)
    sprite('rbl406_10', 4)	# 61-64
    sprite('rbl406_11', 4)	# 65-68
    sprite('rbl406_12', 4)	# 69-72
    sprite('rbl000_00', 6)	# 73-78
    sprite('rbl000_01', 6)	# 79-84
    sprite('rbl000_02', 6)	# 85-90
    sprite('rbl000_03', 6)	# 91-96
    sprite('rbl000_04', 6)	# 97-102
    sprite('rbl000_05', 6)	# 103-108
    sprite('rbl000_06', 6)	# 109-114
    sprite('rbl000_07', 6)	# 115-120
    sprite('rbl000_08', 6)	# 121-126
    sprite('rbl000_09', 6)	# 127-132
    label(1)
    sprite('keep', 1)	# 133-133

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('rbl231_00', 5)	# 1-5
    sprite('rbl231_01', 3)	# 6-8
    sprite('rbl231_02', 3)	# 9-11
    GFX_0('rblef231', -1)
    sprite('rbl231_03', 3)	# 12-14	 **attackbox here**
    sprite('rbl231_04', 4)	# 15-18
    sprite('rbl231_05', 4)	# 19-22
    sprite('rbl231_06', 4)	# 23-26
    sprite('rbl231_07', 4)	# 27-30
    sprite('rbl231_08', 4)	# 31-34
    sprite('rbl000_00', 6)	# 35-40
    sprite('rbl000_01', 6)	# 41-46
    sprite('rbl000_02', 6)	# 47-52
    sprite('rbl000_03', 6)	# 53-58
    sprite('rbl000_04', 6)	# 59-64
    sprite('rbl000_05', 6)	# 65-70
    sprite('rbl000_06', 6)	# 71-76
    sprite('rbl000_07', 6)	# 77-82
    sprite('rbl000_08', 6)	# 83-88
    sprite('rbl000_09', 6)	# 89-94
    label(1)
    sprite('keep', 1)	# 95-95

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('rbl320_00', 8)	# 1-8
    sprite('rbl320_01', 8)	# 9-16
    sprite('rbl320_02', 3)	# 17-19
    sprite('rbl320_03', 3)	# 20-22	 **attackbox here**
    GFX_0('rblef320', -1)
    sprite('rbl320_04', 3)	# 23-25
    setInvincible(0)
    sprite('rbl320_05', 3)	# 26-28
    sprite('rbl320_06', 3)	# 29-31
    sprite('rbl320_05', 3)	# 32-34
    sprite('rbl320_06', 3)	# 35-37
    sprite('rbl320_07', 4)	# 38-41
    sprite('rbl320_08', 4)	# 42-45
    sprite('rbl320_09', 4)	# 46-49
    sprite('rbl320_10', 4)	# 50-53
    sprite('rbl320_11', 4)	# 54-57
    sprite('rbl320_12', 4)	# 58-61
    sprite('rbl320_13', 4)	# 62-65

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('rbl000_00', 6)	# 1-6
    sprite('rbl000_01', 6)	# 7-12
    sprite('rbl000_02', 6)	# 13-18
    sprite('rbl000_03', 6)	# 19-24
    sprite('rbl000_04', 6)	# 25-30
    sprite('rbl000_05', 6)	# 31-36
    sprite('rbl000_06', 6)	# 37-42
    sprite('rbl000_07', 6)	# 43-48
    sprite('rbl000_08', 6)	# 49-54
    sprite('rbl000_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl320_00', 8)	# 61-68
    sprite('rbl320_01', 8)	# 69-76
    sprite('rbl320_02', 3)	# 77-79
    sprite('rbl320_03', 3)	# 80-82	 **attackbox here**
    GFX_0('rblef320', -1)
    sprite('rbl320_04', 3)	# 83-85
    setInvincible(0)
    sprite('rbl320_05', 3)	# 86-88
    sprite('rbl320_06', 3)	# 89-91
    sprite('rbl320_05', 3)	# 92-94
    sprite('rbl320_06', 3)	# 95-97
    sprite('rbl320_07', 4)	# 98-101
    sprite('rbl320_08', 4)	# 102-105
    sprite('rbl320_09', 4)	# 106-109
    sprite('rbl320_10', 4)	# 110-113
    sprite('rbl320_11', 4)	# 114-117
    sprite('rbl320_12', 4)	# 118-121
    sprite('rbl320_13', 4)	# 122-125

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(750)
                if (SLOT_12 >= 35000):
                    SLOT_12 = 35000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rbl032_00', 3)	# 1-3
    sprite('rbl032_01', 3)	# 4-6
    label(0)
    sprite('rbl032_02', 3)	# 7-9
    sprite('rbl032_03', 3)	# 10-12
    sprite('rbl032_04', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('rbl032_05', 3)	# 16-18
    sprite('rbl032_06', 3)	# 19-21
    sprite('rbl032_07', 3)	# 22-24
    sprite('rbl032_08', 3)	# 25-27
    Unknown8006(100, 1, 1)
    sprite('rbl032_09', 3)	# 28-30
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl310_00', 1)	# 31-31
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rbl310_01', 2)	# 32-33
    sprite('rbl310_02', 3)	# 34-36	 **attackbox here**
    Unknown1084(1)
    sprite('rbl310_03', 6)	# 37-42
    SFX_1('rbl155')
    sprite('rbl310_04', 6)	# 43-48
    sprite('rbl310_05', 6)	# 49-54
    sprite('rbl310_06', 5)	# 55-59

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(500)
        Unknown11064(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(41)
        Unknown9142(31)
        AttackP2(50)
        Unknown9016(1)
        StarterRating(2)
        Unknown2004(1, 0)
        if SLOT_IsUnlimitedCharacter:
            JumpCancel_(0)

        def upon_STATE_END():
            Unknown2006()
    sprite('rbl310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rbl311_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rbl311_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rbl311_02', 3)	# 10-12	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    Unknown1043()
    GFX_0('rblef311_Wind', -1)
    sprite('rbl311_03', 3)	# 13-15
    GFX_0('ShadowObjectThrow', -1)
    Unknown1019(50)
    sprite('rbl311_04', 3)	# 16-18
    Unknown1019(50)
    sprite('rbl311_05', 3)	# 19-21
    SFX_1('rbl153')
    sprite('rbl311_06', 3)	# 22-24	 **attackbox here**
    GFX_0('rblef311_1', -1)
    RefreshMultihit()
    AttackP2(100)
    Unknown11099(1)
    Unknown1086(22)
    teleportRelativeX(-20000)
    Unknown1007(20000)
    physicsXImpulse(40000)
    EnableCollision(0)
    Unknown2015(50)
    SFX_3('rblse_10')
    Unknown23072()

    def upon_78():
        Unknown21012('72626c65663331315f310000000000000000000000000000000000000000000020000000')
    sprite('rbl311_07', 3)	# 25-27
    GFX_0('ShadowObjectThrow2nd', -1)
    Unknown1019(50)
    teleportRelativeY(0)
    clearUponHandler(78)
    sprite('rbl311_08', 3)	# 28-30
    Unknown1019(50)
    sprite('rbl311_09', 3)	# 31-33	 **attackbox here**
    GFX_0('rblef311_3', -1)
    RefreshMultihit()
    Damage(1000)
    Unknown11064(0)
    GroundedHitstunAnimation(9)
    AirPushbackX(500)
    AirPushbackY(23000)
    AirUntechableTime(30)
    Unknown1086(22)
    physicsXImpulse(-40000)
    SFX_3('rblse_10')
    Unknown23072()

    def upon_78():
        Unknown21012('72626c65663331315f330000000000000000000000000000000000000000000020000000')
    sprite('rbl311_10', 4)	# 34-37
    Unknown1019(50)
    sprite('rbl311_11', 4)	# 38-41
    Unknown1019(50)
    sprite('rbl311_12', 4)	# 42-45
    Unknown1084(1)

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(750)
                if (SLOT_12 >= 35000):
                    SLOT_12 = 35000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rbl032_00', 3)	# 1-3
    sprite('rbl032_01', 3)	# 4-6
    label(0)
    sprite('rbl032_02', 3)	# 7-9
    sprite('rbl032_03', 3)	# 10-12
    sprite('rbl032_04', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('rbl032_05', 3)	# 16-18
    sprite('rbl032_06', 3)	# 19-21
    sprite('rbl032_07', 3)	# 22-24
    sprite('rbl032_08', 3)	# 25-27
    Unknown8006(100, 1, 1)
    sprite('rbl032_09', 3)	# 28-30
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl310_00', 1)	# 31-31
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rbl310_01', 2)	# 32-33
    sprite('rbl310_02', 3)	# 34-36	 **attackbox here**
    Unknown1084(1)
    sprite('rbl310_03', 6)	# 37-42
    SFX_1('rbl155')
    sprite('rbl310_04', 6)	# 43-48
    sprite('rbl310_05', 6)	# 49-54
    sprite('rbl310_06', 5)	# 55-59

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(500)
        Unknown11064(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(36)
        Unknown9142(26)
        AttackP2(50)
        AirUntechableTime(30)
        Unknown9016(1)
        StarterRating(2)
        Unknown2004(1, 0)
        if SLOT_IsUnlimitedCharacter:
            JumpCancel_(0)

        def upon_STATE_END():
            Unknown2006()
    sprite('rbl310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rbl311_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rbl311_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rbl311_02', 3)	# 10-12	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    Unknown1043()
    GFX_0('rblef311_Wind', -1)
    sprite('rbl311_03', 3)	# 13-15
    GFX_0('ShadowObjectThrow', -1)
    Unknown1019(50)
    sprite('rbl311_04', 3)	# 16-18
    Unknown1019(50)
    sprite('rbl311_05', 3)	# 19-21
    SFX_1('rbl153')
    sprite('rbl311_06', 3)	# 22-24	 **attackbox here**
    GFX_0('rblef311_1', -1)
    SFX_3('rblse_10')
    RefreshMultihit()
    Unknown11099(1)
    AttackP2(100)
    PushbackX(15000)
    Unknown1086(22)
    teleportRelativeX(-20000)
    Unknown1007(20000)
    physicsXImpulse(40000)
    EnableCollision(0)
    Unknown2015(50)
    Unknown23072()

    def upon_78():
        Unknown21012('72626c65663331315f310000000000000000000000000000000000000000000020000000')
    sprite('rbl270_00', 3)	# 25-27
    GFX_0('ShadowObjectThrow2nd', -1)
    Unknown2006()
    Unknown1019(50)
    EnableCollision(1)
    clearUponHandler(78)
    sprite('rbl270_01', 3)	# 28-30
    Unknown1019(50)
    teleportRelativeY(0)
    sprite('rbl270_02', 3)	# 31-33
    Unknown1019(50)
    SFX_0('007_swing_knife_1')
    sprite('rbl270_03', 3)	# 34-36	 **attackbox here**
    GFX_0('rblef270', -1)
    Unknown1019(0)
    RefreshMultihit()
    Damage(1000)
    Unknown11064(0)
    Unknown11099(0)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(500)
    AirPushbackY(22000)
    sprite('rbl270_04', 2)	# 37-38
    sprite('rbl270_05', 2)	# 39-40
    sprite('rbl270_06', 2)	# 41-42
    sprite('rbl270_07', 2)	# 43-44
    sprite('rbl270_08', 3)	# 45-47

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9016(1)
        AirPushbackX(5000)
        AirPushbackY(40000)
        Unknown11001(0, 0, 0)
    sprite('rbl320_00', 4)	# 1-4
    sprite('rbl320_01', 4)	# 5-8
    sprite('rbl320_02', 2)	# 9-10
    tag_voice(1, 'rbl200_0', 'rbl200_1', 'rbl200_2', '')
    sprite('rbl320_03', 3)	# 11-13	 **attackbox here**
    GFX_0('rblef320', -1)
    sprite('rbl320_04', 3)	# 14-16
    setInvincible(0)
    sprite('rbl320_05', 3)	# 17-19
    sprite('rbl320_06', 3)	# 20-22
    sprite('rbl320_05', 4)	# 23-26
    sprite('rbl320_06', 4)	# 27-30
    sprite('rbl320_05', 5)	# 31-35
    sprite('rbl320_06', 5)	# 36-40
    sprite('rbl320_07', 4)	# 41-44
    sprite('rbl320_08', 4)	# 45-48
    sprite('rbl320_09', 4)	# 49-52
    sprite('rbl320_10', 4)	# 53-56
    sprite('rbl320_11', 4)	# 57-60
    sprite('rbl320_12', 4)	# 61-64
    sprite('rbl320_13', 4)	# 65-68

@Subroutine
def DashCancelShadowCreate():
    if (SLOT_59 == 1):
        Unknown1019(50)
        GFX_0('ShadowObjectNmlAtk4A', -1)
    if (SLOT_59 == 2):
        GFX_0('ShadowObjectNmlAtk5A', -1)
    if (SLOT_59 == 3):
        GFX_0('ShadowObjectNmlAtk2A', -1)
    if (SLOT_59 == 4):
        GFX_0('ShadowObjectNmlAtk5AA', -1)
    SLOT_59 = 0

@State
def DashCancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Recovery()
        Unknown30068(1)
        callSubroutine('DashCancelShadowCreate')
    sprite('rbl032_00', 2)	# 1-2
    physicsXImpulse(20000)
    Unknown3026(-14671840)
    Unknown3025(-1, 15)
    sprite('rbl032_01', 2)	# 3-4
    Unknown1019(150)
    sprite('rbl032_02', 3)	# 5-7
    sprite('rbl032_10', 3)	# 8-10
    Unknown1019(50)
    sprite('rbl032_11', 3)	# 11-13
    Unknown1019(50)
    sprite('rbl032_12', 3)	# 14-16
    Unknown1019(50)
    sprite('rbl032_13', 3)	# 17-19
    Unknown1019(0)
    sprite('rbl032_14', 2)	# 20-21

@State
def LandShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 4009):
                Unknown2064(1)
    sprite('rbl400_00', 2)	# 1-2
    sprite('rbl400_01', 2)	# 3-4
    sprite('rbl400_02', 2)	# 5-6
    SFX_3('rblse_21')
    sprite('rbl400_03', 2)	# 7-8
    tag_voice(1, 'rbl201_0', 'rbl201_1', 'rbl201_2', '')
    sprite('rbl400_04', 3)	# 9-11
    sprite('rbl400_05', 3)	# 12-14
    GFX_0('rblef400_Muzzle', -1)
    GFX_0('LandShotAtkObj', -1)
    Unknown23029(1, 4001, 0)
    sprite('rbl400_06', 3)	# 15-17
    sprite('rbl400_07', 3)	# 18-20
    sprite('rbl400_08', 3)	# 21-23
    sprite('rbl400_05', 2)	# 24-25
    sprite('rbl400_05', 3)	# 26-28
    GFX_0('rblef400_Muzzle', -1)
    GFX_0('LandShotAtkObj', -1)
    Unknown23029(1, 4002, 0)
    sprite('rbl400_06', 3)	# 29-31
    sprite('rbl400_07', 3)	# 32-34
    sprite('rbl400_08', 3)	# 35-37
    sprite('rbl400_09', 3)	# 38-40
    sprite('rbl400_10', 3)	# 41-43
    Recovery()
    sprite('rbl400_11', 3)	# 44-46
    sprite('rbl400_12', 3)	# 47-49
    sprite('rbl400_13', 4)	# 50-53
    sprite('rbl400_14', 4)	# 54-57

@State
def LandShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 4009):
                Unknown2064(1)
    sprite('rbl400_00', 5)	# 1-5
    sprite('rbl400_01', 5)	# 6-10
    sprite('rbl400_02', 4)	# 11-14
    SFX_3('rblse_21')
    sprite('rbl400_03', 4)	# 15-18
    tag_voice(1, 'rbl201_0', 'rbl201_1', 'rbl201_2', '')
    sprite('rbl400_04', 3)	# 19-21
    sprite('rbl400_05', 3)	# 22-24
    GFX_0('rblef400_Muzzle', -1)
    GFX_0('LandShotAtkObj', -1)
    Unknown23029(1, 4003, 0)
    sprite('rbl400_06', 3)	# 25-27
    sprite('rbl400_07', 3)	# 28-30
    sprite('rbl400_08', 3)	# 31-33
    sprite('rbl400_05', 2)	# 34-35
    sprite('rbl400_05', 3)	# 36-38
    GFX_0('rblef400_Muzzle', -1)
    GFX_0('LandShotAtkObj', -1)
    Unknown23029(1, 4004, 0)
    sprite('rbl400_06', 3)	# 39-41
    sprite('rbl400_07', 3)	# 42-44
    sprite('rbl400_08', 3)	# 45-47
    sprite('rbl400_05', 2)	# 48-49
    sprite('rbl400_05', 3)	# 50-52
    GFX_0('rblef400_Muzzle', -1)
    GFX_0('LandShotAtkObj', -1)
    Unknown23029(1, 4005, 0)
    sprite('rbl400_06', 3)	# 53-55
    sprite('rbl400_07', 3)	# 56-58
    sprite('rbl400_08', 3)	# 59-61
    sprite('rbl400_09', 3)	# 62-64
    sprite('rbl400_10', 3)	# 65-67
    Recovery()
    sprite('rbl400_11', 3)	# 68-70
    sprite('rbl400_12', 3)	# 71-73
    sprite('rbl400_13', 3)	# 74-76
    sprite('rbl400_14', 3)	# 77-79

@State
def LandShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 4006):
                clearUponHandler(43)
                sendToLabel(0)
        Unknown2004(1, 0)
    sprite('rbl401_00', 3)	# 1-3
    sprite('rbl401_01', 5)	# 4-8
    tag_voice(1, 'rbl202_0', 'rbl202_1', 'rbl202_2', '')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rbl401_02', 5)	# 9-13
    sprite('rbl401_03', 2)	# 14-15
    SFX_3('rblse_00')
    SLOT_51 = 1
    sprite('rbl401_04', 3)	# 16-18
    GFX_0('LandShotAtkObjC', 0)
    Unknown38(6, 1)
    sprite('rbl401_05', 4)	# 19-22
    sprite('rbl401_06', 4)	# 23-26
    sprite('rbl401_07', 4)	# 27-30
    sprite('rbl401_08', 4)	# 31-34
    gotoLabel(1)
    label(0)
    sprite('keep', 2)	# 35-36
    label(1)
    sprite('rbl401_09', 4)	# 37-40
    clearUponHandler(43)
    Unknown23029(6, 4007, 0)
    sprite('rbl401_10', 3)	# 41-43
    sprite('rbl401_11', 3)	# 44-46
    tag_voice(0, 'rbl203_0', 'rbl203_1', 'rbl203_2', '')
    sprite('rbl401_12', 3)	# 47-49
    sprite('rbl401_13', 4)	# 50-53
    sprite('rbl401_14', 4)	# 54-57
    SLOT_51 = 0
    Recovery()
    sprite('rbl401_15', 4)	# 58-61

@Subroutine
def ChainAssaultCancel():
    HitOrBlockCancel('ChainAssaultA')
    HitOrBlockCancel('ChainAssaultB')
    HitOrBlockCancel('ChainAssaultC')
    HitOrBlockCancel('ChainShadowCreateA')
    HitOrBlockCancel('ChainShadowCreateB')
    HitOrBlockCancel('ChainShadowCreateC')

@Subroutine
def ChainAssault_DeriveInput():
    Unknown14070('ChainAssaultA')
    Unknown14070('ChainAssaultB')
    Unknown14070('ChainAssaultC')
    Unknown14070('ChainShadowCreateA')
    Unknown14070('ChainShadowCreateB')
    Unknown14070('ChainShadowCreateC')

@Subroutine
def ChainAssault_DeriveTiming():
    Unknown14072('ChainAssaultA')
    Unknown14072('ChainAssaultB')
    Unknown14072('ChainAssaultC')
    Unknown14072('ChainShadowCreateA')
    Unknown14072('ChainShadowCreateB')
    Unknown14072('ChainShadowCreateC')

@Subroutine
def ChainAssault_DeriveClear():
    Unknown14074('ChainAssaultA')
    Unknown14074('ChainAssaultB')
    Unknown14074('ChainAssaultC')
    Unknown14074('ChainShadowCreateA')
    Unknown14074('ChainShadowCreateB')
    Unknown14074('ChainShadowCreateC')

@Subroutine
def ChainAssaultShadowCreate():
    SLOT_60 = 0
    if (SLOT_59 == 101):
        SLOT_60 = 0
        if Unknown23145('AssaultLandA'):
            SLOT_60 = 1
        if Unknown23145('AssaultAirA'):
            SLOT_60 = 1
        Unknown1019(50)
        if SLOT_60:
            GFX_0('ShadowObjectAssaultA', -1)
    if (SLOT_59 == 102):
        SLOT_60 = 0
        if Unknown23145('AssaultLandB'):
            SLOT_60 = 1
        if Unknown23145('AssaultAirB'):
            SLOT_60 = 1
        if SLOT_60:
            GFX_0('ShadowObjectAssaultB', -1)
    if (SLOT_59 == 103):
        SLOT_60 = 0
        if Unknown23145('AssaultLandC'):
            SLOT_60 = 1
        if Unknown23145('AssaultAirC'):
            SLOT_60 = 1
        if SLOT_60:
            GFX_0('ShadowObjectAssaultC', -1)
    SLOT_59 = 0

@State
def AssaultA():

    def upon_IMMEDIATE():
        if SLOT_36:
            Unknown17003()
            Unknown30070('41737361756c7441697241000000000000000000000000000000000000000000')
            clearUponHandler(2)
        else:
            AttackDefaults_StandingSpecial()
            Unknown30070('41737361756c744c616e64410000000000000000000000000000000000000000')
        AttackLevel_(3)
        Damage(1400)
        AttackP1(80)
        GroundedHitstunAnimation(4)
        hitstun(24)
        AirPushbackX(2500)
        AirPushbackY(21000)
        AirUntechableTime(25)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')

        def upon_11():
            clearUponHandler(11)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        callSubroutine('ChainAssaultCancel')
        SLOT_59 = 101

        def upon_12():
            Unknown21012('72626c65663430335f536c61736800000000000000000000000000000000000020000000')
        if SLOT_36:
            SLOT_6 = 1
    sprite('rbl403_00', 3)	# 1-3
    Unknown23183('72626c3430335f31340000000000000000000000000000000000000000000000020000000200000024000000')
    sprite('rbl403_01', 3)	# 4-6
    Unknown23183('72626c3430335f31350000000000000000000000000000000000000000000000020000000200000024000000')
    tag_voice(1, 'rbl204_0', 'rbl204_1', 'rbl204_2', '')
    Unknown1084(1)
    sprite('rbl403_02', 3)	# 7-9
    Unknown23183('72626c3430335f31360000000000000000000000000000000000000000000000020000000200000024000000')
    sprite('rbl403_03', 3)	# 10-12
    Unknown23183('72626c3430335f31370000000000000000000000000000000000000000000000020000000200000024000000')
    sprite('rbl403_04', 3)	# 13-15
    SFX_3('rblse_10')
    GFX_0('rblef403_Slash', -1)
    physicsXImpulse(60000)
    Unknown3001(255)
    Unknown3004(-85)
    callSubroutine('ChainAssault_DeriveInput')
    sprite('rbl403_05', 6)	# 16-21	 **attackbox here**
    physicsYImpulse(15000)
    Unknown3001(0)
    Unknown3004(0)
    EnableCollision(0)
    Unknown2015(50)
    label(1)
    sprite('rbl403_05', 3)	# 22-24	 **attackbox here**
    callSubroutine('ChainAssault_DeriveTiming')
    Unknown3001(255)
    Unknown3004(0)
    YAccel(150)
    Unknown1043()
    StartMultihit()
    Recovery()
    sprite('rbl403_06', 2)	# 25-26
    Unknown1019(50)
    EnableCollision(1)
    Unknown2015(100)
    sprite('rbl403_07', 2)	# 27-28
    Unknown1019(50)
    sprite('rbl403_08', 2)	# 29-30
    sprite('rbl403_09', 2)	# 31-32
    callSubroutine('ChainAssault_DeriveClear')
    Unknown14077(0)
    sprite('rbl403_10', 4)	# 33-36
    sprite('rbl403_11', 4)	# 37-40
    sprite('rbl403_12', 4)	# 41-44
    sprite('rbl403_13', 4)	# 45-48
    sprite('rbl020_06', 3)	# 49-51
    Unknown2005()

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(11)
    label(10)
    sprite('rbl020_07', 3)	# 52-54
    sprite('rbl020_08', 3)	# 55-57
    gotoLabel(10)
    label(11)
    sprite('rbl010_00', 3)	# 58-60
    sprite('rbl010_01', 3)	# 61-63
    sprite('rbl010_00', 3)	# 64-66

@State
def AssaultB():

    def upon_IMMEDIATE():
        if SLOT_36:
            Unknown17003()
            Unknown30070('41737361756c7441697242000000000000000000000000000000000000000000')
            clearUponHandler(2)
            Unknown2037(1)
        else:
            AttackDefaults_StandingSpecial()
            Unknown30070('41737361756c744c616e64420000000000000000000000000000000000000000')
            Unknown2037(0)
        AttackLevel_(3)
        Hitstop(2)
        Damage(650)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(2500)
        AirPushbackY(18000)
        PushbackX(9800)
        AirUntechableTime(25)
        Unknown9016(1)
        Unknown11057(500)
        Unknown11058('0100000000000000000000000000000000000000')
        SLOT_59 = 102
        if SLOT_36:
            SLOT_7 = 1
    sprite('rbl031_00', 3)	# 1-3
    Unknown23183('72626c3032305f30350000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('rbl405_00', 3)	# 4-6
    Unknown23183('72626c3430355f31340000000000000000000000000000000000000000000000030000000200000024000000')
    tag_voice(1, 'rbl205_0', 'rbl205_1', 'rbl205_2', '')
    sprite('rbl405_01', 3)	# 7-9
    GFX_0('rblef405', -1)
    Unknown23183('72626c3430355f31350000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('rbl405_02', 3)	# 10-12	 **attackbox here**
    physicsXImpulse(15000)
    physicsYImpulse(25000)
    setGravity(1500)
    StartMultihit()
    Unknown23087(80000)
    SFX_3('rblse_12')
    sprite('rbl405_03', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('rbl405_04', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    callSubroutine('ChainAssault_DeriveInput')
    sprite('rbl405_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('rbl405_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('rbl405_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    callSubroutine('ChainAssaultCancel')
    sprite('rbl405_08', 3)	# 23-25
    callSubroutine('ChainAssault_DeriveTiming')
    Recovery()
    sprite('rbl405_09', 3)	# 26-28
    sprite('rbl405_10', 3)	# 29-31
    Unknown1019(50)
    callSubroutine('ChainAssault_DeriveClear')
    Unknown14077(0)
    sprite('rbl405_11', 3)	# 32-34
    sprite('rbl405_12', 3)	# 35-37
    sprite('rbl405_13', 3)	# 38-40
    sprite('rbl020_06', 3)	# 41-43
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(11)
    label(10)
    sprite('rbl020_07', 3)	# 44-46
    sprite('rbl020_08', 3)	# 47-49
    gotoLabel(10)
    label(11)
    sprite('rbl010_00', 3)	# 50-52
    sprite('rbl010_01', 3)	# 53-55
    sprite('rbl010_00', 3)	# 56-58

@State
def AssaultC():

    def upon_IMMEDIATE():
        if SLOT_36:
            Unknown17003()
            Unknown30070('41737361756c7441697243000000000000000000000000000000000000000000')
            clearUponHandler(2)
            Unknown2037(1)
        else:
            AttackDefaults_StandingSpecial()
            Unknown30070('41737361756c744c616e64430000000000000000000000000000000000000000')
            Unknown2037(0)
        AttackLevel_(4)
        Damage(1800)
        AttackP1(90)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(2500)
        AirPushbackY(25000)
        PushbackX(15000)
        AirUntechableTime(45)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        MinimumDamagePct(10)
        Unknown30065(0)
        callSubroutine('ChainAssaultCancel')
        SLOT_59 = 103
        if SLOT_36:
            SLOT_8 = 1
    sprite('rbl404_00', 3)	# 1-3
    Unknown23183('72626c3430345f31340000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('rbl404_01', 3)	# 4-6
    Unknown23183('72626c3430345f31350000000000000000000000000000000000000000000000030000000200000024000000')
    tag_voice(1, 'rbl206_0', 'rbl206_1', 'rbl303_1', '')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    if (not SLOT_2):
        setInvincible(1)
        Unknown22019('0100000000000000000000000000000000000000')
    physicsXImpulse(5000)
    sprite('rbl404_02', 3)	# 7-9
    Unknown23183('72626c3430345f31360000000000000000000000000000000000000000000000030000000200000024000000')
    callSubroutine('ChainAssault_DeriveInput')
    sprite('rbl404_03', 3)	# 10-12
    Unknown1019(150)
    physicsYImpulse(30000)
    Unknown1043()
    SFX_0('006_swing_blade_2')
    sprite('rbl404_04', 5)	# 13-17	 **attackbox here**
    GFX_0('rblef404_Slash', -1)
    RefreshMultihit()
    sprite('rbl404_05', 3)	# 18-20
    Recovery()
    setInvincible(0)
    sprite('rbl404_06', 3)	# 21-23
    callSubroutine('ChainAssault_DeriveTiming')
    sprite('rbl404_07', 2)	# 24-25
    callSubroutine('ChainAssault_DeriveClear')
    Unknown14077(0)
    sprite('rbl404_08', 2)	# 26-27
    sprite('rbl404_09', 2)	# 28-29
    sprite('rbl404_10', 2)	# 30-31
    sprite('rbl404_11', 2)	# 32-33
    sprite('rbl404_12', 2)	# 34-35
    sprite('rbl404_13', 2)	# 36-37

@State
def ChainAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1400)
        AttackP1(80)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        AirUntechableTime(50)
        Unknown9202(12)
        PushbackX(40000)
        Unknown9016(1)
        Unknown11001(-6, -6, -1)
        Unknown11056(0)
        GroundedHitstunAnimation(9)

        def upon_LANDING():
            clearUponHandler(2)
            if SLOT_51:
                sendToLabel(2)
            else:
                sendToLabel(1)
            Unknown23073()
            GFX_0('rblef406_Smoke', -1)
        callSubroutine('ChainAssaultShadowCreate')

        def upon_12():
            Unknown21012('72626c656634303600000000000000000000000000000000000000000000000020000000')
        SLOT_51 = 0
        if Unknown23145('AssaultLandC'):
            SLOT_51 = 1
        if Unknown23145('AssaultAirC'):
            SLOT_51 = 1
        if SLOT_51:
            callSubroutine('EX_Eff')
            Unknown11001(-4, -2, 3)
            MinimumDamagePct(10)
            Unknown30065(0)
    sprite('null', 3)	# 1-3
    StartMultihit()
    sprite('rbl406_00', 2)	# 4-5
    SFX_3('rblse_10')
    if Unknown23145('AssaultLandA'):
        Unknown2005()
    if Unknown23145('AssaultAirA'):
        Unknown2005()
    Unknown1019(75)
    YAccel(5)
    Unknown1021(10000)
    setGravity(0)
    teleportRelativeX(-250000)
    Unknown1007(100000)
    sprite('rbl406_01', 2)	# 6-7
    sprite('rbl406_02', 2)	# 8-9
    sprite('rbl406_03', 2)	# 10-11
    GFX_0('rblef406', -1)
    physicsXImpulse(10000)
    physicsYImpulse(-5000)
    EnableCollision(0)
    tag_voice(1, 'rbl207_0', 'rbl207_1', 'rbl207_2', '')
    sprite('rbl406_04', 3)	# 12-14	 **attackbox here**
    Unknown1019(1500)
    YAccel(2000)
    label(0)
    sprite('rbl406_05', 3)	# 15-17	 **attackbox here**
    sprite('rbl406_04', 3)	# 18-20	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('rbl406_06', 6)	# 21-26
    EnableCollision(1)
    Unknown1019(25)
    Recovery()
    Unknown21012('72626c656634303600000000000000000000000000000000000000000000000021000000')
    Unknown21012('72626c65663430365f426c6f6f6d00000000000000000000000000000000000021000000')
    sprite('rbl406_07', 3)	# 27-29
    Unknown1019(50)
    sprite('rbl406_08', 7)	# 30-36
    sprite('rbl406_09', 7)	# 37-43
    Unknown1084(1)
    sprite('rbl406_10', 7)	# 44-50
    sprite('rbl406_11', 4)	# 51-54
    sprite('rbl406_12', 4)	# 55-58
    ExitState()
    label(2)
    sprite('rbl406_06', 3)	# 59-61
    EnableCollision(1)
    Unknown1019(25)
    Recovery()
    Unknown21012('72626c656634303600000000000000000000000000000000000000000000000021000000')
    Unknown21012('72626c65663430365f426c6f6f6d00000000000000000000000000000000000021000000')
    sprite('rbl406_07', 3)	# 62-64
    Unknown1019(80)
    sprite('rbl406_08', 3)	# 65-67
    sprite('rbl406_09', 3)	# 68-70
    Unknown1084(1)
    sprite('rbl406_10', 3)	# 71-73
    sprite('rbl406_11', 3)	# 74-76
    sprite('rbl406_12', 3)	# 77-79

@State
def ChainAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(80)
        AirPushbackX(2500)
        AirPushbackY(-150000)
        PushbackX(8000)
        GroundedHitstunAnimation(3)
        AirUntechableTime(50)
        hitstun(24)
        Unknown9310(1)

        def upon_LANDING():
            clearUponHandler(2)
            Recovery()
            if SLOT_51:
                sendToLabel(2)
            else:
                sendToLabel(1)
        callSubroutine('ChainAssaultShadowCreate')
        SLOT_51 = 0
        if Unknown23145('AssaultLandC'):
            SLOT_51 = 1
        if Unknown23145('AssaultAirC'):
            SLOT_51 = 1
        if SLOT_51:
            GroundedHitstunAnimation(1)
            callSubroutine('EX_Eff')
            Unknown11001(0, 2, 2)
            MinimumDamagePct(10)
            Unknown30065(0)
    sprite('null', 3)	# 1-3
    StartMultihit()
    Unknown2015(350)
    Unknown2016(350)
    sprite('rbl407_00', 4)	# 4-7
    SFX_3('rblse_10')
    Unknown2006()
    Unknown1019(5)
    YAccel(5)
    Unknown1021(5000)
    teleportRelativeX(50000)
    Unknown1007(-60000)
    setGravity(1000)
    Unknown2015(-1)
    Unknown2016(-1)
    if Unknown23145('AssaultLandA'):
        teleportRelativeX(80000)
    sprite('rbl407_01', 4)	# 8-11
    tag_voice(1, 'rbl208_0', 'rbl208_1', 'rbl208_2', '')
    Unknown1019(50)
    sprite('rbl407_02', 3)	# 12-14
    Unknown1043()
    sprite('rbl407_03', 3)	# 15-17	 **attackbox here**
    GFX_0('rblef407', -1)
    sprite('rbl407_04', 3)	# 18-20
    Recovery()
    sprite('rbl407_05', 3)	# 21-23
    sprite('rbl407_06', 3)	# 24-26
    label(0)
    sprite('rbl020_07', 3)	# 27-29
    sprite('rbl020_08', 3)	# 30-32
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl010_00', 4)	# 33-36
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rbl010_01', 9)	# 37-45
    sprite('rbl010_00', 5)	# 46-50
    ExitState()
    label(2)
    sprite('rbl010_00', 2)	# 51-52
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rbl010_01', 4)	# 53-56
    sprite('rbl010_00', 2)	# 57-58

@State
def ChainAssaultC():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1800)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(-30000)
        AirUntechableTime(40)
        Unknown9202(13)
        Unknown9310(20)
        Unknown21005(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11056(0)
        Unknown11099(1)

        def upon_11():
            physicsXImpulse(10000)
            physicsYImpulse(15000)
            Unknown1043()

        def upon_8():
            Unknown2006()
        callSubroutine('ChainAssaultShadowCreate')
        SLOT_51 = 0
        if Unknown23145('AssaultLandC'):
            SLOT_51 = 1
        if Unknown23145('AssaultAirC'):
            SLOT_51 = 1
        if SLOT_51:
            Unknown9310(23)
        clearUponHandler(2)
    sprite('null', 1)	# 1-1
    StartMultihit()
    sprite('rbl408_00', 2)	# 2-3
    SFX_3('rblse_10')
    Unknown2006()
    Unknown1019(10)
    YAccel(25)
    Unknown1021(2000)
    Unknown23087(75000)
    if SLOT_51:
        setGravity(1500)
    else:
        setGravity(500)
    if SLOT_125:
        teleportRelativeX(150000)
        Unknown1007(8000)
        if SLOT_51:
            setGravity(1000)
    else:
        teleportRelativeX(300000)
        Unknown1007(-260000)
        setGravity(500)
    Unknown48('190000000200000034000000190000000200000017000000')
    if (SLOT_23 <= 40000):
        teleportRelativeY(40000)
    Unknown2006()
    Unknown2005()
    sprite('rbl408_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rbl408_02', 3)	# 7-9
    tag_voice(1, 'rbl209_0', 'rbl209_1', 'rbl209_2', '')
    sprite('rbl408_03', 3)	# 10-12
    sprite('rbl408_04', 3)	# 13-15
    sprite('rbl408_05', 3)	# 16-18
    sprite('rbl408_06', 3)	# 19-21
    GFX_0('rblef408_Wind', -1)
    sprite('rbl408_07', 3)	# 22-24	 **attackbox here**

    def upon_LANDING():
        sendToLabel(1)
    sprite('rbl408_08', 3)	# 25-27
    Recovery()
    Unknown1043()
    sprite('rbl408_09', 3)	# 28-30
    sprite('rbl408_10', 3)	# 31-33
    sprite('rbl408_11', 3)	# 34-36
    sprite('rbl408_12', 3)	# 37-39
    sprite('rbl020_05', 3)	# 40-42
    Unknown2005()
    sprite('rbl020_06', 3)	# 43-45
    label(0)
    sprite('rbl020_07', 3)	# 46-48
    sprite('rbl020_08', 3)	# 49-51
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rbl010_00', 3)	# 52-54
    Unknown1084(1)
    Unknown8000(100, 1, 1)

@State
def LandShadowCreateA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
    sprite('rbl402_00', 3)	# 1-3
    sprite('rbl402_01', 3)	# 4-6
    tag_voice(1, 'rbl210_0', 'rbl210_1', 'rbl210_2', '')
    sprite('rbl402_02', 2)	# 7-8
    sprite('keep', 1)	# 9-9
    if CheckInput(0x79):
        clearUponHandler(3)
        sendToLabel(50)
    sprite('rbl402_03', 3)	# 10-12
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectLandCreateA', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(-23000)
    physicsYImpulse(6000)
    setGravity(800)
    SFX_3('rblse_33')
    sprite('rbl402_04', 3)	# 13-15
    Recovery()
    sprite('rbl402_05', 3)	# 16-18
    sprite('rbl402_06', 3)	# 19-21
    sprite('rbl402_07', 32767)	# 22-32788
    label(0)
    sprite('rbl402_08', 3)	# 32789-32791
    Unknown1019(25)
    sprite('rbl010_01', 3)	# 32792-32794
    Unknown1019(50)
    sprite('rbl010_02', 3)	# 32795-32797
    Unknown1019(50)
    sprite('rbl010_01', 3)	# 32798-32800
    Unknown1019(50)
    sprite('rbl010_00', 3)	# 32801-32803
    Unknown1019(50)
    ExitState()
    label(50)
    sprite('rbl040_01', 3)	# 32804-32806
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectLandCreateA', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    SFX_3('rblse_33')
    sprite('rbl040_00', 3)	# 32807-32809
    sprite('rbl406_06', 3)	# 32810-32812
    teleportRelativeX(20000)
    physicsXImpulse(50000)
    Recovery()
    sprite('rbl406_07', 4)	# 32813-32816
    Unknown1019(75)
    sprite('rbl406_08', 4)	# 32817-32820
    Unknown1019(50)
    sprite('rbl406_09', 4)	# 32821-32824
    Unknown1084(1)
    sprite('rbl406_10', 4)	# 32825-32828
    sprite('rbl406_11', 4)	# 32829-32832
    sprite('rbl406_12', 4)	# 32833-32836
    ExitState()

@State
def AirShadowCreateA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)

        def upon_STATE_END():
            Unknown1043()
        callSubroutine('ChainAssaultShadowCreate')
    sprite('rbl402_09', 3)	# 1-3
    sprite('rbl402_10', 3)	# 4-6
    tag_voice(1, 'rbl210_0', 'rbl210_1', 'rbl210_2', '')
    Unknown1084(1)
    sprite('rbl402_11', 2)	# 7-8
    sprite('keep', 1)	# 9-9
    if CheckInput(0x79):
        clearUponHandler(3)
        sendToLabel(50)
    sprite('rbl402_03', 3)	# 10-12
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectAirCreateA', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(-12000)
    physicsYImpulse(6000)
    setGravity(800)
    SFX_3('rblse_33')
    sprite('rbl402_04', 3)	# 13-15
    Recovery()
    sprite('rbl402_05', 3)	# 16-18
    sprite('rbl402_06', 3)	# 19-21
    sprite('rbl402_12', 3)	# 22-24
    ExitState()
    label(50)
    sprite('rbl405_11', 5)	# 25-29
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectAirCreateA', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(18000)
    physicsYImpulse(8000)
    setGravity(1200)
    SFX_3('rblse_33')
    sprite('rbl405_12', 5)	# 30-34
    Unknown1019(75)
    sprite('rbl405_13', 5)	# 35-39
    Unknown1019(50)

@State
def LandShadowCreateB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
    sprite('rbl402_13', 3)	# 1-3
    sprite('rbl402_14', 3)	# 4-6
    tag_voice(1, 'rbl211_0', 'rbl211_1', 'rbl211_2', '')
    sprite('rbl402_15', 2)	# 7-8
    sprite('keep', 1)	# 9-9
    if CheckInput(0x79):
        clearUponHandler(3)
        sendToLabel(50)
    sprite('rbl402_03', 3)	# 10-12
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectLandCreateB', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(-23000)
    physicsYImpulse(6000)
    setGravity(800)
    SFX_3('rblse_33')
    sprite('rbl402_04', 3)	# 13-15
    Recovery()
    sprite('rbl402_05', 3)	# 16-18
    sprite('rbl402_06', 3)	# 19-21
    sprite('rbl402_07', 32767)	# 22-32788
    label(0)
    sprite('rbl402_08', 3)	# 32789-32791
    Unknown1019(25)
    sprite('rbl010_01', 3)	# 32792-32794
    Unknown1019(50)
    sprite('rbl010_02', 3)	# 32795-32797
    Unknown1019(50)
    sprite('rbl010_01', 3)	# 32798-32800
    Unknown1019(50)
    sprite('rbl010_00', 3)	# 32801-32803
    Unknown1019(50)
    ExitState()
    label(50)
    sprite('rbl040_01', 3)	# 32804-32806
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectLandCreateB', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    SFX_3('rblse_33')
    sprite('rbl040_00', 3)	# 32807-32809
    sprite('rbl406_06', 3)	# 32810-32812
    teleportRelativeX(20000)
    physicsXImpulse(50000)
    Recovery()
    sprite('rbl406_07', 4)	# 32813-32816
    Unknown1019(75)
    sprite('rbl406_08', 4)	# 32817-32820
    Unknown1019(50)
    sprite('rbl406_09', 4)	# 32821-32824
    Unknown1084(1)
    sprite('rbl406_10', 4)	# 32825-32828
    sprite('rbl406_11', 4)	# 32829-32832
    sprite('rbl406_12', 4)	# 32833-32836
    ExitState()

@State
def AirShadowCreateB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)

        def upon_STATE_END():
            Unknown1043()
        callSubroutine('ChainAssaultShadowCreate')
    sprite('rbl402_16', 3)	# 1-3
    sprite('rbl402_17', 3)	# 4-6
    tag_voice(1, 'rbl211_0', 'rbl211_1', 'rbl211_2', '')
    Unknown1084(1)
    sprite('rbl402_18', 2)	# 7-8
    sprite('keep', 1)	# 9-9
    if CheckInput(0x79):
        clearUponHandler(3)
        sendToLabel(50)
    sprite('rbl402_03', 3)	# 10-12
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectAirCreateB', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(-12000)
    physicsYImpulse(6000)
    setGravity(800)
    SFX_3('rblse_33')
    sprite('rbl402_04', 3)	# 13-15
    Recovery()
    sprite('rbl402_05', 3)	# 16-18
    sprite('rbl402_06', 3)	# 19-21
    sprite('rbl402_12', 3)	# 22-24
    ExitState()
    label(50)
    sprite('rbl405_11', 5)	# 25-29
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectAirCreateB', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(18000)
    physicsYImpulse(8000)
    setGravity(1200)
    SFX_3('rblse_33')
    sprite('rbl405_12', 5)	# 30-34
    Unknown1019(75)
    sprite('rbl405_13', 5)	# 35-39
    Unknown1019(50)

@State
def LandShadowCreateC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
    sprite('rbl402_19', 3)	# 1-3
    sprite('rbl402_20', 3)	# 4-6
    tag_voice(1, 'rbl212_0', 'rbl212_1', 'rbl212_2', '')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rbl402_21', 2)	# 7-8
    sprite('keep', 1)	# 9-9
    if CheckInput(0x79):
        clearUponHandler(3)
        sendToLabel(50)
    sprite('rbl402_03', 3)	# 10-12
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectLandCreateC', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(-23000)
    physicsYImpulse(6000)
    setGravity(800)
    SFX_3('rblse_33')
    sprite('rbl402_04', 3)	# 13-15
    Recovery()
    sprite('rbl402_05', 3)	# 16-18
    sprite('rbl402_06', 3)	# 19-21
    sprite('rbl402_07', 32767)	# 22-32788
    label(0)
    sprite('rbl402_08', 3)	# 32789-32791
    Unknown1019(25)
    sprite('rbl010_01', 3)	# 32792-32794
    Unknown1019(50)
    sprite('rbl010_02', 3)	# 32795-32797
    Unknown1019(50)
    sprite('rbl010_01', 3)	# 32798-32800
    Unknown1019(50)
    sprite('rbl010_00', 3)	# 32801-32803
    Unknown1019(50)
    ExitState()
    label(50)
    sprite('rbl040_01', 3)	# 32804-32806
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectLandCreateC', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    SFX_3('rblse_33')
    sprite('rbl040_00', 3)	# 32807-32809
    sprite('rbl406_06', 3)	# 32810-32812
    teleportRelativeX(20000)
    physicsXImpulse(50000)
    Recovery()
    sprite('rbl406_07', 4)	# 32813-32816
    Unknown1019(75)
    sprite('rbl406_08', 4)	# 32817-32820
    Unknown1019(50)
    sprite('rbl406_09', 4)	# 32821-32824
    Unknown1084(1)
    sprite('rbl406_10', 4)	# 32825-32828
    sprite('rbl406_11', 4)	# 32829-32832
    sprite('rbl406_12', 4)	# 32833-32836
    ExitState()

@State
def AirShadowCreateC():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)

        def upon_STATE_END():
            Unknown1043()
        callSubroutine('ChainAssaultShadowCreate')
    sprite('rbl402_22', 3)	# 1-3
    sprite('rbl402_23', 3)	# 4-6
    tag_voice(1, 'rbl212_0', 'rbl212_1', 'rbl212_2', '')
    Unknown1084(1)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rbl402_24', 2)	# 7-8
    sprite('keep', 1)	# 9-9
    if CheckInput(0x79):
        clearUponHandler(3)
        sendToLabel(50)
    sprite('rbl402_03', 3)	# 10-12
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectAirCreateC', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(-12000)
    physicsYImpulse(6000)
    setGravity(800)
    SFX_3('rblse_33')
    sprite('rbl402_04', 3)	# 13-15
    Recovery()
    sprite('rbl402_05', 3)	# 16-18
    sprite('rbl402_06', 3)	# 19-21
    sprite('rbl402_12', 3)	# 22-24
    ExitState()
    label(50)
    sprite('rbl405_11', 5)	# 25-29
    Unknown23029(5, 4021, 0)
    GFX_0('ShadowObjectAirCreateC', -1)
    Unknown38(5, 1)
    SLOT_4 = 60
    physicsXImpulse(18000)
    physicsYImpulse(8000)
    setGravity(1200)
    SFX_3('rblse_33')
    sprite('rbl405_12', 5)	# 30-34
    Unknown1019(75)
    sprite('rbl405_13', 5)	# 35-39
    Unknown1019(50)

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
    sprite('rbl430_00', 5)	# 1-5
    tag_voice(1, 'rbl250_0', 'rbl250_1', '', '')
    Unknown2036(76, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    sprite('rbl430_01', 5)	# 6-10
    sprite('rbl430_02', 5)	# 11-15
    label(0)
    sprite('rbl430_03', 3)	# 16-18
    sprite('rbl430_04', 3)	# 19-21
    sprite('rbl430_05', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rbl430_06', 5)	# 25-29
    sprite('rbl430_07', 5)	# 30-34
    tag_voice(0, 'rbl251_0', 'rbl251_1', '', '')
    sprite('rbl430_08', 5)	# 35-39
    sprite('rbl430_09', 5)	# 40-44
    sprite('rbl430_10', 5)	# 45-49
    sprite('rbl430_11', 3)	# 50-52
    SFX_3('rblse_36')
    sprite('rbl430_12', 2)	# 53-54
    GFX_0('UltimateShotObj', -1)
    sprite('rbl430_13', 2)	# 55-56
    setInvincible(0)
    sprite('rbl430_14', 3)	# 57-59
    sprite('rbl430_15', 3)	# 60-62
    sprite('rbl430_16', 3)	# 63-65
    sprite('rbl430_14', 4)	# 66-69
    sprite('rbl430_15', 4)	# 70-73
    sprite('rbl430_16', 4)	# 74-77
    sprite('rbl430_14', 5)	# 78-82
    sprite('rbl430_15', 5)	# 83-87
    sprite('rbl430_16', 5)	# 88-92
    sprite('rbl430_17', 5)	# 93-97
    sprite('rbl430_18', 5)	# 98-102

@State
def UltimateShotSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        if Unknown23145('ChainAssaultA'):
            Unknown2006()
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
    sprite('rbl430_00', 5)	# 1-5
    tag_voice(1, 'rbl250_0', 'rbl250_1', '', '')
    Unknown2036(76, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    sprite('rbl430_01', 5)	# 6-10
    sprite('rbl430_02', 5)	# 11-15
    label(0)
    sprite('rbl430_03', 3)	# 16-18
    sprite('rbl430_04', 3)	# 19-21
    sprite('rbl430_05', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rbl430_06', 5)	# 25-29
    sprite('rbl430_07', 5)	# 30-34
    tag_voice(0, 'rbl251_0', 'rbl251_1', '', '')
    sprite('rbl430_08', 5)	# 35-39
    sprite('rbl430_09', 5)	# 40-44
    sprite('rbl430_10', 5)	# 45-49
    sprite('rbl430_11', 3)	# 50-52
    SFX_3('rblse_36')
    sprite('rbl430_12', 2)	# 53-54
    GFX_0('UltimateShotObj', -1)
    Unknown23029(1, 4301, 0)
    sprite('rbl430_13', 2)	# 55-56
    sprite('rbl430_14', 3)	# 57-59
    sprite('rbl430_15', 3)	# 60-62
    sprite('rbl430_16', 3)	# 63-65
    sprite('rbl430_19', 3)	# 66-68
    sprite('rbl430_20', 3)	# 69-71
    SFX_3('rblse_36')
    sprite('rbl430_21', 2)	# 72-73
    GFX_0('UltimateShotObj', -1)
    Unknown23029(1, 4302, 0)
    sprite('rbl430_21', 1)	# 74-74
    setInvincible(0)
    sprite('rbl430_22', 3)	# 75-77
    sprite('rbl430_23', 3)	# 78-80
    sprite('rbl430_24', 3)	# 81-83
    sprite('rbl430_25', 3)	# 84-86
    sprite('rbl430_23', 4)	# 87-90
    sprite('rbl430_24', 4)	# 91-94
    sprite('rbl430_25', 4)	# 95-98
    sprite('rbl430_23', 5)	# 99-103
    sprite('rbl430_24', 5)	# 104-108
    sprite('rbl430_25', 5)	# 109-113
    sprite('rbl430_26', 5)	# 114-118
    sprite('rbl430_27', 5)	# 119-123

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1700)
        MinimumDamagePct(35)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(120)
        AirPushbackX(2500)
        AirPushbackY(70000)
        Unknown11056(0)
        Unknown11072(1, 300000, 0)
        Unknown9016(1)
        Unknown2073(1)
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(1)

        def upon_78():
            Unknown11069('UltimateRushChase')
            DisableAttackRestOfMove()
            Unknown13024(0)
            enterState('UltimateRushChase')
    sprite('rbl431_00', 3)	# 1-3
    tag_voice(1, 'rbl252_0', 'rbl252_1', '', '')
    Unknown2036(63, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    setInvincible(1)
    label(0)
    sprite('rbl431_01', 3)	# 4-6
    sprite('rbl431_02', 3)	# 7-9
    sprite('rbl431_03', 3)	# 10-12
    gotoLabel(0)
    label(1)
    sprite('rbl431_04', 3)	# 13-15
    sprite('rbl431_05', 2)	# 16-17
    SFX_3('rblse_36')
    sprite('rbl431_06', 2)	# 18-19
    physicsXImpulse(-10000)
    sprite('rbl431_07', 2)	# 20-21
    Unknown1019(50)
    sprite('rbl431_08', 2)	# 22-23
    GFX_0('rblef431_1st', -1)
    Unknown1019(50)
    sprite('rbl431_09', 6)	# 24-29	 **attackbox here**
    Unknown1084(1)
    sprite('rbl431_10', 6)	# 30-35
    setInvincible(0)
    sprite('rbl431_11', 6)	# 36-41
    sprite('rbl431_27', 6)	# 42-47
    sprite('rbl431_28', 6)	# 48-53
    sprite('rbl431_29', 6)	# 54-59

@State
def UltimateRushChase():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown11108('03000000')
        AttackLevel_(3)
        Damage(1000)
        Unknown11064(1)
        AttackP2(100)
        MinimumDamagePct(30)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(5000)
        Unknown11058('0100000000000000000000000000000000000000')
        Hitstop(15)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('UltimateRushChase')
        Unknown30048(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown20003(1)
        Unknown20000(1)
        Unknown13024(0)
        Unknown13021(1)
        Unknown21005(1)

        def upon_12():
            clearUponHandler(12)
            Unknown20000(0)
            Unknown11023(1)
            sendToLabel(100)
            Unknown21012('72626c65663433315f326e64000000000000000000000000000000000000000020000000')

        def upon_LANDING():
            clearUponHandler(2)
            EnableCollision(1)
            Unknown2015(100)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(2)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2053(1)
            Unknown2034(1)
            EnableCollision(1)
        DisableAttackRestOfMove()
    sprite('rbl431_10', 6)	# 1-6
    setInvincible(1)
    sprite('rbl431_11', 6)	# 7-12
    sprite('rbl431_12', 4)	# 13-16
    sprite('rbl431_13', 4)	# 17-20
    sprite('rbl431_14', 4)	# 21-24
    physicsXImpulse(-25000)
    sprite('rbl431_15', 4)	# 25-28
    tag_voice(0, 'rbl253_0', 'rbl253_1', '', '')
    sprite('rbl431_16', 4)	# 29-32
    sprite('rbl431_17', 4)	# 33-36
    Unknown1019(50)
    sprite('rbl431_18', 8)	# 37-44
    Unknown1019(25)
    sprite('rbl431_19', 8)	# 45-52
    Unknown1019(25)
    sprite('rbl431_20', 3)	# 53-55	 **attackbox here**
    GFX_0('DashShadowEff', -1)
    GFX_0('rblef_ShadowParticle', -1)
    GFX_0('rblef431_2nd', -1)
    SFX_3('rblse_10')
    physicsXImpulse(80000)
    physicsYImpulse(80000)
    Unknown1043()
    Unknown3001(255)
    Unknown3004(-42)
    sprite('rbl431_21', 3)	# 56-58	 **attackbox here**
    sprite('rbl431_20', 3)	# 59-61	 **attackbox here**
    sprite('rbl431_21', 3)	# 62-64	 **attackbox here**
    RefreshMultihit()
    Unknown2034(1)
    Unknown2053(1)
    label(0)
    sprite('rbl020_05', 3)	# 65-67
    Unknown13024(1)
    Unknown20000(0)
    setInvincible(0)
    Unknown3001(0)
    Unknown3004(42)
    Unknown1019(20)
    YAccel(50)
    Unknown2015(50)
    sprite('rbl020_06', 3)	# 68-70
    label(1)
    sprite('rbl020_07', 3)	# 71-73
    sprite('rbl020_08', 3)	# 74-76
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rbl431_22', 6)	# 77-82
    sprite('rbl431_23', 6)	# 83-88
    sprite('rbl431_24', 6)	# 89-94
    sprite('rbl431_25', 6)	# 95-100
    sprite('rbl431_26', 6)	# 101-106
    ExitState()
    label(100)
    sprite('rbl431_20', 2)	# 107-108	 **attackbox here**
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(680)
    Hitstop(4)
    MinimumDamagePct(13)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rbl431_20', 2)	# 109-110	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 111-112	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 113-114	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 115-116	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    sprite('rbl431_20', 2)	# 117-118	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 119-120	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 121-122	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 123-124	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    sprite('rbl431_20', 2)	# 125-126	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 127-128	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 129-130	 **attackbox here**
    RefreshMultihit()
    Unknown11064(0)
    AirPushbackY(20000)
    Unknown9310(10)
    Unknown11069('')
    sprite('rbl431_21', 3)	# 131-133	 **attackbox here**
    Unknown1018()
    Unknown1023()
    YAccel(25)
    setGravity(2000)
    gotoLabel(0)

@State
def UltimateRushSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1700)
        MinimumDamagePct(35)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(120)
        AirPushbackX(2500)
        AirPushbackY(70000)
        Unknown11056(0)
        Unknown11072(1, 300000, 0)
        Unknown9016(1)
        Unknown2073(1)
        loopRelated(17, 60)

        def upon_17():
            sendToLabel(1)
        if Unknown23145('ChainAssaultA'):
            Unknown2006()

        def upon_78():
            Unknown11069('UltimateRushSPChase')
            DisableAttackRestOfMove()
            Unknown13024(0)
            enterState('UltimateRushSPChase')
    sprite('rbl431_00', 3)	# 1-3
    tag_voice(1, 'rbl252_0', 'rbl252_1', '', '')
    Unknown2036(63, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    ConsumeSuperMeter(-10000)
    setInvincible(1)
    label(0)
    sprite('rbl431_01', 3)	# 4-6
    sprite('rbl431_02', 3)	# 7-9
    sprite('rbl431_03', 3)	# 10-12
    gotoLabel(0)
    label(1)
    sprite('rbl431_04', 3)	# 13-15
    sprite('rbl431_05', 2)	# 16-17
    SFX_3('rblse_36')
    sprite('rbl431_06', 2)	# 18-19
    physicsXImpulse(-10000)
    GFX_0('rblef431_1st', -1)
    sprite('rbl431_07', 2)	# 20-21
    Unknown1019(50)
    sprite('rbl431_08', 2)	# 22-23
    Unknown1019(50)
    sprite('rbl431_09', 6)	# 24-29	 **attackbox here**
    Unknown1084(1)
    sprite('rbl431_10', 6)	# 30-35
    setInvincible(0)
    sprite('rbl431_11', 6)	# 36-41
    sprite('rbl431_27', 6)	# 42-47
    sprite('rbl431_28', 6)	# 48-53
    sprite('rbl431_29', 6)	# 54-59

@State
def UltimateRushSPChase():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown11108('03000000')
        AttackLevel_(3)
        Damage(1000)
        Unknown11064(1)
        AttackP2(100)
        MinimumDamagePct(30)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(5000)
        Unknown11058('0100000000000000000000000000000000000000')
        Hitstop(15)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('UltimateRushSPChase')
        Unknown30048(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown20003(1)
        Unknown20000(1)
        Unknown13024(0)
        Unknown13021(1)

        def upon_12():
            clearUponHandler(12)
            Unknown20000(0)
            Unknown11023(1)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            EnableCollision(1)
            Unknown2015(100)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(2)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2053(1)
            Unknown2034(1)
            EnableCollision(1)
        DisableAttackRestOfMove()
    sprite('rbl431_10', 6)	# 1-6
    setInvincible(1)
    sprite('rbl431_11', 6)	# 7-12
    sprite('rbl431_12', 4)	# 13-16
    sprite('rbl431_13', 4)	# 17-20
    sprite('rbl431_14', 4)	# 21-24
    physicsXImpulse(-25000)
    sprite('rbl431_15', 4)	# 25-28
    tag_voice(0, 'rbl253_0', 'rbl253_1', '', '')
    sprite('rbl431_16', 4)	# 29-32
    sprite('rbl431_17', 4)	# 33-36
    Unknown1019(50)
    sprite('rbl431_18', 8)	# 37-44
    Unknown1019(25)
    sprite('rbl431_19', 8)	# 45-52
    Unknown1019(25)
    sprite('rbl431_20', 3)	# 53-55	 **attackbox here**
    GFX_0('DashShadowEff', -1)
    GFX_0('rblef_ShadowParticle', -1)
    GFX_0('rblef431_2nd_OD', -1)
    SFX_3('rblse_10')
    physicsXImpulse(80000)
    physicsYImpulse(80000)
    Unknown1043()
    Unknown3001(255)
    Unknown3004(-42)
    sprite('rbl431_21', 3)	# 56-58	 **attackbox here**
    sprite('rbl431_20', 3)	# 59-61	 **attackbox here**
    sprite('rbl431_21', 3)	# 62-64	 **attackbox here**
    RefreshMultihit()
    Unknown2034(1)
    Unknown2053(1)
    label(0)
    sprite('rbl020_05', 3)	# 65-67
    Unknown13024(1)
    Unknown20000(0)
    setInvincible(0)
    Unknown3001(0)
    Unknown3004(42)
    Unknown1019(20)
    YAccel(50)
    Unknown2015(50)
    sprite('rbl020_06', 3)	# 68-70
    label(1)
    sprite('rbl020_07', 3)	# 71-73
    sprite('rbl020_08', 3)	# 74-76
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rbl431_22', 6)	# 77-82
    sprite('rbl431_23', 6)	# 83-88
    sprite('rbl431_24', 6)	# 89-94
    sprite('rbl431_25', 6)	# 95-100
    sprite('rbl431_26', 6)	# 101-106
    ExitState()
    label(100)
    sprite('rbl431_20', 2)	# 107-108	 **attackbox here**
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(680)
    Hitstop(2)
    MinimumDamagePct(12)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown21012('72626c65663433315f326e645f4f44000000000000000000000000000000000020000000')
    sprite('rbl431_20', 2)	# 109-110	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 111-112	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 113-114	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 115-116	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    sprite('rbl431_20', 2)	# 117-118	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 119-120	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 121-122	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 123-124	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    sprite('rbl431_20', 2)	# 125-126	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 127-128	 **attackbox here**
    RefreshMultihit()
    sprite('rbl431_20', 2)	# 129-130	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(5000)
    Unknown9310(10)
    sprite('null', 3)	# 131-133
    StartMultihit()
    physicsXImpulse(80000)
    physicsYImpulse(30000)
    GFX_0('ShadowObjectAssaultA', -1)
    Unknown1084(1)
    sprite('rbl406_00', 3)	# 134-136
    Unknown3001(255)
    Unknown3004(0)
    GFX_0('DashShadowEff', -1)
    GFX_0('rblef_ShadowParticle', -1)
    SFX_3('rblse_10')
    Unknown2006()
    Unknown1019(75)
    YAccel(5)
    Unknown1021(10000)
    setGravity(0)
    teleportRelativeX(-300000)
    Unknown1007(300000)
    Unknown20000(0)
    sprite('rbl406_01', 3)	# 137-139
    sprite('rbl406_02', 3)	# 140-142
    sprite('rbl406_03', 3)	# 143-145
    physicsXImpulse(5000)
    physicsYImpulse(-5000)
    EnableCollision(0)
    sprite('rbl406_04', 3)	# 146-148	 **attackbox here**
    Unknown3001(255)
    Unknown3004(-51)
    Unknown1019(1500)
    YAccel(2500)
    clearUponHandler(2)

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(102)
    sprite('rbl406_05', 3)	# 149-151	 **attackbox here**
    RefreshMultihit()
    Damage(300)
    Unknown11056(0)
    AirPushbackX(-10000)
    AirPushbackY(-60000)
    MinimumDamagePct(10)
    Unknown9190(1)
    Unknown9118(40)
    Hitstop(12)
    Unknown11069('UltimateRushSPFinishAtk')
    Unknown21012('72626c65663433315f326e645f4f44000000000000000000000000000000000021000000')
    label(101)
    sprite('rbl406_04', 3)	# 152-154	 **attackbox here**
    sprite('rbl406_05', 3)	# 155-157	 **attackbox here**
    gotoLabel(101)
    label(102)
    sprite('rbl406_06', 4)	# 158-161
    tag_voice(0, 'rbl254_0', 'rbl254_1', '', '')
    Unknown3001(0)
    Unknown3004(42)
    Unknown20000(0)
    physicsXImpulse(30000)
    EnableCollision(1)
    sprite('rbl406_07', 4)	# 162-165
    Unknown1019(50)
    sprite('rbl406_08', 4)	# 166-169
    Unknown1019(50)
    sprite('rbl406_09', 4)	# 170-173
    Unknown1084(1)
    GFX_0('UltimateRushSPFinishAtk', -1)
    sprite('rbl406_10', 4)	# 174-177
    sprite('rbl406_11', 4)	# 178-181
    sprite('rbl406_12', 4)	# 182-185
    sprite('rbl430_00', 5)	# 186-190
    GFX_0('rblef431_Finish', -1)
    sprite('rbl430_01', 5)	# 191-195
    sprite('rbl430_02', 5)	# 196-200
    sprite('rbl430_03', 3)	# 201-203
    GFX_1('rblef431_close', 0)
    sprite('rbl430_04', 3)	# 204-206
    sprite('rbl430_05', 3)	# 207-209
    sprite('rbl430_03', 3)	# 210-212
    sprite('rbl430_04', 3)	# 213-215
    sprite('rbl430_05', 3)	# 216-218
    setInvincible(0)
    sprite('rbl430_03', 4)	# 219-222
    sprite('rbl430_04', 4)	# 223-226
    Unknown13024(1)
    sprite('rbl430_05', 4)	# 227-230
    sprite('rbl430_03', 5)	# 231-235
    sprite('rbl430_04', 5)	# 236-240
    sprite('rbl430_05', 5)	# 241-245
    sprite('rbl430_03', 5)	# 246-250
    sprite('rbl430_04', 5)	# 251-255
    sprite('rbl430_05', 5)	# 256-260
    sprite('rbl430_02', 7)	# 261-267
    sprite('rbl430_01', 7)	# 268-274
    sprite('rbl430_00', 7)	# 275-281
    ExitState()

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Damage(0)
        Unknown11056(0)
        AirUntechableTime(60)
        hitstun(60)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        Unknown9016(1)
        Unknown11072(1, 50000, 0)
        loopRelated(17, 70)

        def upon_17():
            sendToLabel(1)

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(11)
            Unknown23088(1, 1)
            PushbackX(0)
            Unknown11069('AstralHeatExe')
            enterState('AstralHeatExe')
            GFX_0('rblef450_1st_BG', -1)

        def upon_11():
            EnableCollision(1)
            sendToLabel(100)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)

        def upon_8():
            Unknown2005()
    sprite('rbl450_00', 3)	# 1-3
    tag_voice(1, 'rbl290_0', 'rbl290_1', '', '')
    setInvincible(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2036(85, -1, 2)
    Unknown23147()
    label(0)
    sprite('rbl450_01', 3)	# 4-6
    sprite('rbl450_02', 3)	# 7-9
    sprite('rbl450_03', 3)	# 10-12
    gotoLabel(0)
    label(1)
    sprite('rbl450_04', 4)	# 13-16
    GFX_0('rblef450', -1)
    sprite('rbl450_05', 5)	# 17-21
    physicsXImpulse(2500)
    sprite('rbl450_06', 6)	# 22-27
    Unknown1019(400)
    sprite('rbl450_07', 6)	# 28-33
    Unknown1019(200)
    sprite('rbl450_08', 6)	# 34-39	 **attackbox here**
    Unknown1019(200)
    StartMultihit()
    Unknown3001(255)
    Unknown3004(-42)
    Unknown21012('72626c656634353000000000000000000000000000000000000000000000000020000000')
    SFX_3('rblse_10')
    sprite('rbl450_08', 6)	# 40-45	 **attackbox here**
    Unknown1019(250)
    Unknown3038(1)
    EnableCollision(0)
    label(100)
    sprite('rbl450_08', 6)	# 46-51	 **attackbox here**
    Unknown3038(0)
    Unknown3001(0)
    Unknown3004(42)
    EnableCollision(0)
    StartMultihit()
    Unknown1019(60)
    Unknown21012('72626c656634353000000000000000000000000000000000000000000000000029000000')
    sprite('rbl450_09', 6)	# 52-57
    EnableCollision(1)
    setInvincible(0)
    Unknown1019(60)
    sprite('rbl450_10', 6)	# 58-63
    Unknown1019(60)
    sprite('rbl450_11', 6)	# 64-69
    Unknown1019(60)
    sprite('rbl311_10ex01', 6)	# 70-75
    Unknown1019(60)
    sprite('rbl311_11ex01', 6)	# 76-81
    Unknown1019(60)
    sprite('rbl311_12ex01', 6)	# 82-87
    Unknown1084(1)

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23157(0)
        Unknown23084(1)
        Unknown20003(1)
        Unknown20000(1)
        Unknown20004(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2053(0)
        setInvincible(1)
        AttackLevel_(3)
        GroundedHitstunAnimation(9)
        AirUntechableTime(150)
        AirPushbackY(50000)
        Unknown11064(1)
        MinimumDamagePct(100)
        Unknown9016(1)
    sprite('rbl450_08', 3)	# 1-3	 **attackbox here**
    Unknown3038(0)
    Unknown3001(0)
    Unknown3004(42)
    EnableCollision(0)
    StartMultihit()
    physicsXImpulse(20000)
    sprite('rbl450_09', 3)	# 4-6
    EnableCollision(1)
    Unknown1019(60)
    sprite('rbl450_10', 3)	# 7-9
    Unknown1019(60)
    sprite('rbl450_11', 3)	# 10-12
    Unknown1019(60)
    sprite('rbl311_10ex01', 3)	# 13-15
    Unknown1019(60)
    sprite('rbl311_11ex01', 3)	# 16-18
    Unknown1019(60)
    sprite('rbl311_12ex01', 3)	# 19-21
    Unknown1084(1)
    sprite('rbl271_00', 3)	# 22-24
    Unknown2006()
    sprite('rbl271_01', 3)	# 25-27
    GFX_0('rblef271_1', -1)
    sprite('rbl271_02', 2)	# 28-29	 **attackbox here**
    GFX_0('rblef450_2nd_BG1', 101)
    RefreshMultihit()
    Damage(1250)
    physicsXImpulse(-12000)
    physicsYImpulse(30000)
    Unknown1043()
    Unknown11072(1, 200000, -100000)
    Unknown11023(1)
    sprite('rbl271_03', 2)	# 30-31
    sprite('rbl271_04', 2)	# 32-33
    sprite('rbl271_05', 2)	# 34-35
    sprite('rbl271_06', 2)	# 36-37
    sprite('rbl271_07', 3)	# 38-40	 **attackbox here**
    GFX_0('rblef450_2nd_BG2', 101)
    GFX_0('rblef271_2', -1)
    RefreshMultihit()
    Damage(1500)
    AirPushbackX(15000)
    AirPushbackY(65000)
    Hitstop(11)
    Unknown11072(0, 0, 0)
    Unknown11023(1)
    sprite('rbl271_08', 3)	# 41-43
    sprite('rbl271_09', 4)	# 44-47
    sprite('rbl271_10', 4)	# 48-51
    sprite('rbl271_11', 4)	# 52-55
    sprite('rbl403_04', 6)	# 56-61
    Unknown20001(1)
    Unknown36(22)
    Unknown1000(0)
    Unknown35()
    SFX_3('rblse_10')
    GFX_0('DashShadowEff', -1)
    GFX_0('rblef_ShadowParticle', -1)
    Unknown21012('72626c656634353000000000000000000000000000000000000000000000000021000000')
    Unknown1000(-700000)
    physicsXImpulse(80000)
    physicsYImpulse(120000)
    setGravity(0)
    Unknown3001(255)
    Unknown3004(-63)
    sprite('rbl403_05', 6)	# 62-67	 **attackbox here**
    RefreshMultihit()
    Damage(1750)
    Unknown11001(0, 30, 30)
    Unknown11099(1)
    AirPushbackX(500)
    AirPushbackY(2000)
    YImpluseBeforeWallbounce(10)
    EnableCollision(0)
    Unknown20001(0)
    Unknown20000(0)
    Unknown11072(1, 50000, 0)
    Unknown11023(0)

    def upon_78():
        clearUponHandler(78)
        Unknown1017()
        Unknown1022()
        enterState('AstralHeatFinish')
    label(1)
    sprite('rbl403_05', 3)	# 68-70	 **attackbox here**
    Unknown3001(0)
    Unknown3004(85)
    Unknown1019(40)
    YAccel(40)
    Unknown1043()
    StartMultihit()
    Recovery()
    setInvincible(0)
    sprite('rbl403_06', 2)	# 71-72
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(50)
    EnableCollision(1)
    Unknown2015(100)
    sprite('rbl403_07', 2)	# 73-74
    Unknown1019(50)
    sprite('rbl403_08', 2)	# 75-76
    sprite('rbl403_09', 2)	# 77-78
    sprite('rbl403_10', 4)	# 79-82
    sprite('rbl403_11', 4)	# 83-86
    sprite('rbl403_12', 4)	# 87-90
    sprite('rbl403_13', 4)	# 91-94
    sprite('rbl020_06', 3)	# 95-97
    Unknown2005()

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(11)
    label(10)
    sprite('rbl020_07', 3)	# 98-100
    sprite('rbl020_08', 3)	# 101-103
    gotoLabel(10)
    label(11)
    sprite('rbl010_00', 3)	# 104-106
    sprite('rbl010_01', 3)	# 107-109
    sprite('rbl010_00', 3)	# 110-112

@State
def AstralHeatFinish():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23157(0)
        Unknown23084(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown2053(0)
        setInvincible(1)
        AttackLevel_(4)
        Damage(1750)
        Hitstop(1)
        GroundedHitstunAnimation(9)
        AirUntechableTime(120)
        Unknown11057(500)
        AirPushbackX(2500)
        AirPushbackY(-50000)
        Unknown11064(1)
        MinimumDamagePct(100)
        Unknown9016(1)
        Unknown9310(10)
        Unknown1018()
        Unknown1023()
        Unknown1043()
        Unknown23024(3)
        SLOT_51 = 1
    sprite('keep', 3)	# 1-3
    Unknown3001(0)
    Unknown3004(85)
    StartMultihit()
    Unknown1019(75)
    YAccel(40)
    setGravity(0)
    GFX_0('AHCable', -1)
    Unknown38(11, 1)
    SFX_3('rblse_44')
    sprite('rbl450_12', 3)	# 4-6
    Unknown2006()
    sprite('rbl450_13', 3)	# 7-9
    Unknown1019(25)
    YAccel(25)
    sprite('rbl450_14', 3)	# 10-12
    Unknown1019(50)
    YAccel(50)
    sprite('rbl450_15', 3)	# 13-15
    sprite('rbl450_16', 3)	# 16-18
    sprite('rbl450_17', 3)	# 19-21
    sprite('rbl450_18', 3)	# 22-24
    SLOT_51 = 0
    Unknown1019(65)
    YAccel(65)
    sprite('rbl450_18', 3)	# 25-27
    Unknown1019(65)
    YAccel(65)
    sprite('rbl450_19', 3)	# 28-30
    Unknown1019(65)
    YAccel(65)
    sprite('rbl450_19', 3)	# 31-33
    Unknown1019(65)
    YAccel(65)
    sprite('rbl450_20', 8)	# 34-41
    tag_voice(0, 'rbl291_0', 'rbl291_1', '', '')
    sprite('rbl450_21', 8)	# 42-49
    sprite('rbl450_22', 8)	# 50-57
    sprite('rbl450_23', 8)	# 58-65
    sprite('rbl450_24', 8)	# 66-73
    sprite('rbl450_25', 8)	# 74-81
    Unknown1019(50)
    YAccel(50)
    SFX_3('rblse_03')
    sprite('rbl450_26', 7)	# 82-88
    physicsXImpulse(1500)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('rbl450_27', 5)	# 89-93
    Unknown21012('72626c656634353000000000000000000000000000000000000000000000000024000000')
    SFX_3('rblse_04')
    SFX_3('rblse_00')
    sprite('rbl450_28', 6)	# 94-99	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('rbl450_28ex01', 6)	# 100-105	 **attackbox here**
    SFX_3('rblse_03')
    sprite('rbl450_29', 6)	# 106-111	 **attackbox here**
    sprite('rbl450_30', 6)	# 112-117	 **attackbox here**
    SFX_3('rblse_04')
    SFX_3('rblse_00')
    sprite('rbl450_28', 5)	# 118-122	 **attackbox here**
    Unknown1039(200)
    sprite('rbl450_28ex01', 5)	# 123-127	 **attackbox here**
    SFX_3('rblse_03')
    sprite('rbl450_29', 5)	# 128-132	 **attackbox here**
    sprite('rbl450_30', 5)	# 133-137	 **attackbox here**
    SFX_3('rblse_04')
    SFX_3('rblse_00')
    sprite('rbl450_28', 4)	# 138-141	 **attackbox here**
    Unknown1039(200)
    sprite('rbl450_28ex01', 4)	# 142-145	 **attackbox here**
    SFX_3('rblse_03')
    sprite('rbl450_29', 4)	# 146-149	 **attackbox here**
    sprite('rbl450_30', 4)	# 150-153	 **attackbox here**
    SFX_3('rblse_02')
    SFX_3('rblse_00')
    sprite('rbl450_28', 3)	# 154-156	 **attackbox here**
    Unknown1039(200)
    YAccel(150)
    RefreshMultihit()
    sprite('rbl450_28ex01', 3)	# 157-159	 **attackbox here**
    RefreshMultihit()
    SFX_3('rblse_03')
    sprite('rbl450_29', 3)	# 160-162	 **attackbox here**
    RefreshMultihit()
    sprite('rbl450_30', 3)	# 163-165	 **attackbox here**
    RefreshMultihit()
    SFX_3('rblse_02')
    SFX_3('rblse_00')
    sprite('rbl450_28', 3)	# 166-168	 **attackbox here**
    Unknown1043()
    RefreshMultihit()
    sprite('rbl450_28ex01', 3)	# 169-171	 **attackbox here**
    RefreshMultihit()
    SFX_3('rblse_03')
    sprite('rbl450_29', 3)	# 172-174	 **attackbox here**
    RefreshMultihit()
    sprite('rbl450_30', 3)	# 175-177	 **attackbox here**
    RefreshMultihit()
    SFX_3('rblse_02')
    SFX_3('rblse_00')
    sprite('rbl450_28', 3)	# 178-180	 **attackbox here**
    RefreshMultihit()
    sprite('rbl450_28ex01', 3)	# 181-183	 **attackbox here**
    RefreshMultihit()
    SFX_3('rblse_03')
    sprite('rbl450_29', 3)	# 184-186	 **attackbox here**
    RefreshMultihit()
    sprite('rbl450_30', 3)	# 187-189	 **attackbox here**
    RefreshMultihit()
    SFX_3('rblse_01')
    SFX_3('rblse_00')
    sprite('rbl450_31', 3)	# 190-192
    sprite('rbl450_32', 3)	# 193-195
    sprite('rbl450_32', 32767)	# 196-32962

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        sendToLabel(1)
    label(1)
    sprite('rbl450_33', 3)	# 32963-32965	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(5)
    Damage(7000)
    ScreenShake(5000, 50000)
    Unknown11001(0, 210, 210)
    GFX_0('AstralLastCamera', -1)
    Unknown21012('72626c656634353000000000000000000000000000000000000000000000000025000000')
    GFX_0('rblef450_RedBack', -1)
    SFX_3('rblse_46')
    sprite('rbl450_34', 3)	# 32966-32968
    sprite('rbl450_35', 3)	# 32969-32971
    sprite('rbl450_36', 3)	# 32972-32974
    sprite('rbl450_37', 3)	# 32975-32977
    sprite('rbl450_34', 4)	# 32978-32981
    sprite('rbl450_35', 4)	# 32982-32985
    sprite('rbl450_36', 4)	# 32986-32989
    sprite('rbl450_37', 4)	# 32990-32993
    sprite('rbl450_34', 5)	# 32994-32998
    sprite('rbl450_35', 5)	# 32999-33003
    sprite('rbl450_36', 5)	# 33004-33008
    sprite('rbl450_37', 5)	# 33009-33013
    sprite('rbl450_34', 6)	# 33014-33019
    sprite('rbl450_35', 6)	# 33020-33025
    sprite('rbl450_36', 6)	# 33026-33031
    sprite('rbl450_37', 6)	# 33032-33037
    sprite('rbl450_34', 6)	# 33038-33043
    sprite('rbl450_35', 6)	# 33044-33049
    sprite('rbl450_36', 6)	# 33050-33055
    sprite('rbl450_37', 6)	# 33056-33061
    sprite('rbl450_34', 6)	# 33062-33067
    sprite('rbl450_35', 6)	# 33068-33073
    sprite('rbl450_36', 6)	# 33074-33079
    sprite('rbl450_37', 6)	# 33080-33085
    sprite('rbl450_34', 6)	# 33086-33091
    sprite('rbl450_35', 6)	# 33092-33097
    sprite('rbl450_36', 6)	# 33098-33103
    sprite('rbl450_37', 6)	# 33104-33109
    sprite('rbl450_34', 6)	# 33110-33115
    sprite('rbl450_35', 6)	# 33116-33121
    sprite('rbl450_36', 6)	# 33122-33127
    sprite('rbl450_37', 6)	# 33128-33133
    sprite('rbl450_34', 6)	# 33134-33139
    sprite('rbl450_35', 6)	# 33140-33145
    sprite('rbl450_36', 6)	# 33146-33151
    sprite('rbl450_37', 6)	# 33152-33157
    sprite('rbl450_34', 6)	# 33158-33163
    sprite('rbl450_35', 6)	# 33164-33169
    sprite('rbl450_36', 6)	# 33170-33175
    Unknown30058('')
    sprite('rbl450_37', 6)	# 33176-33181
    GFX_0('AstralAtkFinal', -1)
    sprite('rbl450_34', 6)	# 33182-33187
    sprite('rbl450_35', 6)	# 33188-33193
    sprite('rbl450_36', 6)	# 33194-33199
    sprite('rbl450_37', 6)	# 33200-33205
    sprite('rbl450_34', 6)	# 33206-33211
    sprite('rbl450_35', 6)	# 33212-33217
    sprite('rbl450_36', 6)	# 33218-33223
    sprite('rbl450_37', 6)	# 33224-33229
    sprite('rbl450_34', 6)	# 33230-33235
    sprite('rbl450_35', 6)	# 33236-33241
    sprite('rbl450_36', 6)	# 33242-33247
    sprite('rbl450_37', 6)	# 33248-33253
    sprite('rbl450_34', 6)	# 33254-33259
    sprite('rbl450_35', 6)	# 33260-33265
    sprite('rbl450_36', 6)	# 33266-33271
    sprite('rbl450_37', 6)	# 33272-33277
    Unknown23024(0)
    GFX_0('rblef450_EffDelete', -1)
    sprite('keep', 3)	# 33278-33280
    Unknown1000(260000)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20006(1)
    Unknown20003(1)
    Unknown20004(1)

@Subroutine
def MouthTableInit():
    Unknown18011('rbl000', 12643, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl500', 12643, 14177, 14691, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl500', '001')
    Unknown18011('rbl501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl501', '002')
    Unknown18011('rbl502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl502', '003')
    Unknown18011('rbl503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl503', '004')
    Unknown18011('rbl504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl504', '005')
    Unknown18011('rbl505', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl505', '006')
    Unknown18011('rbl520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl520', '007')
    Unknown18011('rbl521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl521', '008')
    Unknown18011('rbl522', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl522', '009')
    Unknown18011('rbl523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl523', '010')
    Unknown18011('rbl524', 12643, 12641, 25392, 12338, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl524', '011')
    Unknown18011('rbl525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl525', '012')
    Unknown18011('rbl402', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl403', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600ryn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601bjb', 12643, 14177, 14179, 14177, 13923, 24880, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601brg', 12643, 12641, 25394, 24887, 25399, 12854, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601uyu', 12643, 12897, 25392, 24887, 25399, 14132, 14177, 14179, 14177, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601', 12643, 12641, 25397, 24887, 25399, 24887, 13617, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl604', 12643, 12641, 25397, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600use', 12899, 14177, 14179, 12641, 25394, 12339, 14177, 14179, 14177, 14179, 14177, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl601bsu', 12643, 12897, 25392, 12852, 12641, 25392, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24886, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl600rne', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 13621, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl600pmi', '017')
    Unknown30092('rbl600ryn', '018')
    Unknown30092('rbl600ugo', '019')
    Unknown30092('rbl600uhy', '020')
    Unknown30092('rbl600ume', '021')
    Unknown30092('rbl600uor', '022')
    Unknown30092('rbl601bhz', '023')
    Unknown30092('rbl601biz', '024')
    Unknown30092('rbl601bjb', '025')
    Unknown30092('rbl601bjn', '026')
    Unknown30092('rbl601brg', '027')
    Unknown30092('rbl601rrb', '028')
    Unknown30092('rbl601rwi', '029')
    Unknown30092('rbl601uyu', '030')
    Unknown30092('rbl601', '032')
    Unknown30092('rbl600use', '033')
    Unknown30092('rbl601bsu', '034')
    Unknown30092('rbl600rne', '035')
    Unknown18011('rbl700bjb', 12643, 12641, 25392, 14135, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl700pmi', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl700ryn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl700ugo', 12643, 12641, 25392, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl700uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701biz', 12643, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701bjn', 12643, 14177, 14179, 12641, 25392, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701brg', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701rwi', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701uhy', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 13109, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701uyu', 12643, 14177, 12643, 24880, 25397, 24885, 25397, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701use', 13155, 12641, 25392, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl701bsu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rbl700rne', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rbl700bjb', '036')
    Unknown30092('rbl700pmi', '037')
    Unknown30092('rbl700ryn', '038')
    Unknown30092('rbl700ugo', '039')
    Unknown30092('rbl700uor', '040')
    Unknown30092('rbl701bhz', '041')
    Unknown30092('rbl701biz', '042')
    Unknown30092('rbl701bjn', '043')
    Unknown30092('rbl701brg', '044')
    Unknown30092('rbl701rrb', '045')
    Unknown30092('rbl701rwi', '046')
    Unknown30092('rbl701ryn', '047')
    Unknown30092('rbl701uhy', '048')
    Unknown30092('rbl701ume', '049')
    Unknown30092('rbl701uyu', '050')
    Unknown30092('rbl701use', '051')
    Unknown30092('rbl701bsu', '052')
    Unknown30092('rbl700rne', '053')
    if SLOT_172:
        Unknown18011('rbl000', 12643, 12899, 14177, 14179, 14177, 14179, 12641, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl500', 12643, 12643, 14177, 14179, 14177, 14179, 13665, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 25393, 24881, 25399, 24887, 25399, 25398, 24885, 25399, 24887, 25399, 24887, 25396, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl501', 12643, 13155, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 14179, 14177, 14179, 13153, 13667, 14177, 12899, 12899, 14177, 14179, 13921, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl502', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 14177, 14179, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl503', 12643, 12899, 14177, 14179, 14177, 14179, 13153, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl504', 12643, 12643, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl505', 12643, 13155, 14177, 14179, 14177, 13667, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl520', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 12899, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl521', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 12897, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl522', 12643, 13155, 14177, 14179, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 14177, 14179, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl523', 12643, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13155, 24884, 25399, 25394, 24885, 25399, 24887, 25399, 24887, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl524', 12643, 14177, 14179, 14177, 14179, 12897, 12643, 24880, 25399, 24887, 25399, 24887, 25396, 24882, 25399, 24887, 25395, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl525', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl402', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl403', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600pmi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 14177, 14179, 14177, 14179, 13665, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600ryn', 12643, 12643, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600ugo', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600uhy', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600ume', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13921, 13923, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 13411, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600uor', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13411, 14177, 14179, 14177, 13667, 12643, 12897, 12899, 14177, 13155, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601bhz', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 14177, 14179, 14177, 13923, 12899, 14177, 13411, 13155, 14177, 14179, 14177, 14179, 12897, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601biz', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601bjb', 12643, 12643, 12641, 12643, 14177, 14179, 14177, 14179, 13409, 13667, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 13667, 13155, 14177, 13411, 13155, 13409, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601bjn', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24881, 25397, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601brg', 12643, 12899, 14177, 14179, 14177, 13923, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601rrb', 12643, 13155, 14177, 14179, 14177, 14179, 13409, 13155, 12643, 14177, 14179, 14177, 13155, 12899, 14177, 14179, 14689, 14179, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601rwi', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 24883, 25399, 24887, 25395, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601uyu', 12643, 13155, 14177, 14179, 14177, 13155, 12643, 13409, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 12849, 13923, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl604', 12643, 14177, 14179, 14177, 14179, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600use', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 13105, 14177, 14179, 14177, 14179, 14177, 12899, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl601bsu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 25399, 14385, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl600rne', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl700bjb', 12643, 13155, 14177, 14179, 14177, 14179, 12641, 12899, 24889, 25399, 24887, 25399, 25393, 24881, 25399, 24887, 25396, 24881, 25399, 25393, 24882, 25399, 24887, 25399, 24887, 25395, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl700pmi', 12643, 13155, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl700ryn', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 14179, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl700ugo', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 14179, 14689, 14179, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl700uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701bhz', 12643, 13155, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 13409, 12899, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701biz', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701bjn', 12643, 13155, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 13155, 14177, 14179, 14177, 14179, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701brg', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24881, 25399, 24887, 25399, 24887, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701rrb', 12643, 12899, 14177, 14179, 14177, 14179, 13921, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 24883, 25399, 24887, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701rwi', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 13155, 13155, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701uhy', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 14177, 13411, 13155, 13921, 13667, 14177, 14179, 13665, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701ume', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701uyu', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701use', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl701bsu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rbl700rne', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('727262000000000000000000000000007277690000000000000000000000000072626c0000000000000000000000000072796e00000000000000000000000000'):
        SLOT_171 = 1
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    if SLOT_169:
        _gotolabel(482)
    if SLOT_122:
        _gotolabel(482)
    if SLOT_123:
        _gotolabel(482)
    if SLOT_171:
        _gotolabel(1000)
    PartnerChar('rrb')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('rwi')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bjn')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('bhz')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('bjb')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('uhy')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('ugo')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('uor')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uyu')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('ryn')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('pmi')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('biz')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('ume')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('use')
    if SLOT_ReturnVal:
        _gotolabel(240)
    PartnerChar('bsu')
    if SLOT_ReturnVal:
        _gotolabel(250)
    PartnerChar('rne')
    if SLOT_ReturnVal:
        _gotolabel(260)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('rbl600_00', 30)	# 2-31
    if SLOT_158:
        Unknown7006('rbl500', 100, 896295538, 12592, 0, 0, 100, 896295538, 13360, 0, 0, 100, 896295538, 13616, 0, 0, 100)
    sprite('rbl600_01', 6)	# 32-37
    label(1)
    sprite('rbl600_02', 30)	# 38-67
    if SLOT_97:
        _gotolabel(1)
    sprite('rbl600_03', 6)	# 68-73
    Unknown23018(1)
    sprite('rbl600_04', 6)	# 74-79
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 80-85
    sprite('rbl600_06', 6)	# 86-91
    loopRest()
    ExitState()
    label(10)
    sprite('rbl601_00', 1)	# 92-92
    if SLOT_158:
        Unknown7006('rbl502', 100, 896295538, 13104, 0, 0, 100, 896295538, 13360, 0, 0, 100, 896295538, 13616, 0, 0, 100)
    label(11)
    sprite('rbl601_00', 30)	# 93-122
    if SLOT_97:
        _gotolabel(11)
    sprite('rbl601_01', 6)	# 123-128
    Unknown23018(1)
    sprite('rbl601_02', 6)	# 129-134
    sprite('rbl601_03', 6)	# 135-140
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 141-146
    sprite('rbl601_05', 6)	# 147-152
    loopRest()
    ExitState()
    label(20)
    sprite('rbl000_00', 1)	# 153-153
    SFX_1('rbl604')
    label(21)
    sprite('rbl000_00', 6)	# 154-159
    sprite('rbl000_01', 6)	# 160-165
    sprite('rbl000_02', 6)	# 166-171
    sprite('rbl000_03', 6)	# 172-177
    sprite('rbl000_04', 6)	# 178-183
    sprite('rbl000_05', 6)	# 184-189
    sprite('rbl000_06', 6)	# 190-195
    sprite('rbl000_07', 6)	# 196-201
    sprite('rbl000_08', 6)	# 202-207
    sprite('rbl000_09', 6)	# 208-213
    gotoLabel(21)
    label(100)
    sprite('rbl600_00', 1)	# 214-214
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(101)
    sprite('rbl600_00', 32767)	# 215-32981
    label(101)
    sprite('rbl600_01', 6)	# 32982-32987
    sprite('rbl600_02', 30)	# 32988-33017
    sprite('rbl600_02', 1)	# 33018-33018
    SFX_1('rbl601rrb')
    label(102)
    sprite('rbl600_02', 1)	# 33019-33019
    if SLOT_97:
        _gotolabel(102)
    sprite('rbl600_02', 20)	# 33020-33039
    sprite('rbl600_03', 6)	# 33040-33045
    sprite('rbl600_04', 6)	# 33046-33051
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 33052-33057
    sprite('rbl600_06', 6)	# 33058-33063
    Unknown23018(1)
    label(103)
    sprite('rbl000_00', 6)	# 33064-33069
    sprite('rbl000_01', 6)	# 33070-33075
    sprite('rbl000_02', 6)	# 33076-33081
    sprite('rbl000_03', 6)	# 33082-33087
    sprite('rbl000_04', 6)	# 33088-33093
    sprite('rbl000_05', 6)	# 33094-33099
    sprite('rbl000_06', 6)	# 33100-33105
    sprite('rbl000_07', 6)	# 33106-33111
    sprite('rbl000_08', 6)	# 33112-33117
    sprite('rbl000_09', 6)	# 33118-33123
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('rbl601_00', 1)	# 33124-33124
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(111)
    sprite('rbl601_00', 32767)	# 33125-65891
    label(111)
    sprite('rbl601_00', 90)	# 65892-65981
    SFX_1('rbl601rwi')
    sprite('rbl601_01', 6)	# 65982-65987
    sprite('rbl601_02', 6)	# 65988-65993
    sprite('rbl601_03', 6)	# 65994-65999
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 66000-66005
    sprite('rbl601_05', 6)	# 66006-66011
    Unknown23018(1)
    label(112)
    sprite('rbl000_00', 6)	# 66012-66017
    sprite('rbl000_01', 6)	# 66018-66023
    sprite('rbl000_02', 6)	# 66024-66029
    sprite('rbl000_03', 6)	# 66030-66035
    sprite('rbl000_04', 6)	# 66036-66041
    sprite('rbl000_05', 6)	# 66042-66047
    sprite('rbl000_06', 6)	# 66048-66053
    sprite('rbl000_07', 6)	# 66054-66059
    sprite('rbl000_08', 6)	# 66060-66065
    sprite('rbl000_09', 6)	# 66066-66071
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('rbl600_00', 1)	# 66072-66072
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(121)
    sprite('rbl600_00', 32767)	# 66073-98839
    label(121)
    sprite('rbl600_00', 60)	# 98840-98899
    SFX_1('rbl601brg')
    sprite('rbl600_01', 6)	# 98900-98905
    sprite('rbl600_02', 150)	# 98906-99055
    sprite('rbl600_03', 6)	# 99056-99061
    sprite('rbl600_04', 6)	# 99062-99067
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 99068-99073
    sprite('rbl600_06', 6)	# 99074-99079
    Unknown23018(1)
    label(122)
    sprite('rbl000_00', 6)	# 99080-99085
    sprite('rbl000_01', 6)	# 99086-99091
    sprite('rbl000_02', 6)	# 99092-99097
    sprite('rbl000_03', 6)	# 99098-99103
    sprite('rbl000_04', 6)	# 99104-99109
    sprite('rbl000_05', 6)	# 99110-99115
    sprite('rbl000_06', 6)	# 99116-99121
    sprite('rbl000_07', 6)	# 99122-99127
    sprite('rbl000_08', 6)	# 99128-99133
    sprite('rbl000_09', 6)	# 99134-99139
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('rbl000_00', 1)	# 99140-99140
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('rbl000_00', 6)	# 99141-99146
    sprite('rbl000_01', 6)	# 99147-99152
    sprite('rbl000_02', 6)	# 99153-99158
    sprite('rbl000_03', 6)	# 99159-99164
    sprite('rbl000_04', 6)	# 99165-99170
    sprite('rbl000_05', 6)	# 99171-99176
    sprite('rbl000_06', 6)	# 99177-99182
    sprite('rbl000_07', 6)	# 99183-99188
    sprite('rbl000_08', 6)	# 99189-99194
    sprite('rbl000_09', 6)	# 99195-99200
    gotoLabel(131)
    label(132)
    sprite('rbl300_00', 6)	# 99201-99206
    SFX_1('rbl601bjn')
    sprite('rbl300_01', 6)	# 99207-99212
    sprite('rbl300_02', 6)	# 99213-99218
    sprite('rbl300_03', 6)	# 99219-99224
    sprite('rbl300_04', 6)	# 99225-99230
    sprite('rbl300_05', 6)	# 99231-99236
    label(133)
    sprite('rbl300_06', 1)	# 99237-99237
    if SLOT_97:
        _gotolabel(133)
    sprite('rbl300_05', 6)	# 99238-99243
    sprite('rbl300_04', 6)	# 99244-99249
    sprite('rbl300_03', 6)	# 99250-99255
    sprite('rbl300_02', 6)	# 99256-99261
    sprite('rbl300_01', 6)	# 99262-99267
    sprite('rbl300_00', 6)	# 99268-99273
    Unknown23018(1)
    label(134)
    sprite('rbl000_00', 6)	# 99274-99279
    sprite('rbl000_01', 6)	# 99280-99285
    sprite('rbl000_02', 6)	# 99286-99291
    sprite('rbl000_03', 6)	# 99292-99297
    sprite('rbl000_04', 6)	# 99298-99303
    sprite('rbl000_05', 6)	# 99304-99309
    sprite('rbl000_06', 6)	# 99310-99315
    sprite('rbl000_07', 6)	# 99316-99321
    sprite('rbl000_08', 6)	# 99322-99327
    sprite('rbl000_09', 6)	# 99328-99333
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('rbl000_00', 1)	# 99334-99334
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('rbl000_00', 6)	# 99335-99340
    sprite('rbl000_01', 6)	# 99341-99346
    sprite('rbl000_02', 6)	# 99347-99352
    sprite('rbl000_03', 6)	# 99353-99358
    sprite('rbl000_04', 6)	# 99359-99364
    sprite('rbl000_05', 6)	# 99365-99370
    sprite('rbl000_06', 6)	# 99371-99376
    sprite('rbl000_07', 6)	# 99377-99382
    sprite('rbl000_08', 6)	# 99383-99388
    sprite('rbl000_09', 6)	# 99389-99394
    gotoLabel(141)
    label(142)
    sprite('rbl300_00', 6)	# 99395-99400
    SFX_1('rbl601bhz')
    sprite('rbl300_01', 6)	# 99401-99406
    sprite('rbl300_02', 6)	# 99407-99412
    sprite('rbl300_03', 6)	# 99413-99418
    label(143)
    sprite('rbl300_04', 1)	# 99419-99419
    if SLOT_97:
        _gotolabel(143)
    sprite('rbl300_03', 6)	# 99420-99425
    sprite('rbl300_02', 6)	# 99426-99431
    sprite('rbl300_01', 6)	# 99432-99437
    sprite('rbl300_00', 6)	# 99438-99443
    Unknown23018(1)
    label(144)
    sprite('rbl000_00', 6)	# 99444-99449
    sprite('rbl000_01', 6)	# 99450-99455
    sprite('rbl000_02', 6)	# 99456-99461
    sprite('rbl000_03', 6)	# 99462-99467
    sprite('rbl000_04', 6)	# 99468-99473
    sprite('rbl000_05', 6)	# 99474-99479
    sprite('rbl000_06', 6)	# 99480-99485
    sprite('rbl000_07', 6)	# 99486-99491
    sprite('rbl000_08', 6)	# 99492-99497
    sprite('rbl000_09', 6)	# 99498-99503
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('rbl600_00', 1)	# 99504-99504
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(151)
    sprite('rbl600_00', 32767)	# 99505-132271
    label(151)
    sprite('rbl600_00', 40)	# 132272-132311
    SFX_1('rbl601bjb')
    sprite('rbl600_01', 6)	# 132312-132317
    sprite('rbl600_02', 180)	# 132318-132497
    sprite('rbl600_03', 6)	# 132498-132503
    sprite('rbl600_04', 6)	# 132504-132509
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 132510-132515
    sprite('rbl600_06', 6)	# 132516-132521
    Unknown23018(1)
    label(152)
    sprite('rbl000_00', 6)	# 132522-132527
    sprite('rbl000_01', 6)	# 132528-132533
    sprite('rbl000_02', 6)	# 132534-132539
    sprite('rbl000_03', 6)	# 132540-132545
    sprite('rbl000_04', 6)	# 132546-132551
    sprite('rbl000_05', 6)	# 132552-132557
    sprite('rbl000_06', 6)	# 132558-132563
    sprite('rbl000_07', 6)	# 132564-132569
    sprite('rbl000_08', 6)	# 132570-132575
    sprite('rbl000_09', 6)	# 132576-132581
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('rbl600_00', 60)	# 132582-132641
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rbl600_01', 6)	# 132642-132647
    sprite('rbl600_02', 30)	# 132648-132677
    sprite('rbl600_02', 1)	# 132678-132678
    SFX_1('rbl600uhy')
    label(161)
    sprite('rbl600_02', 1)	# 132679-132679
    if SLOT_97:
        _gotolabel(161)
    sprite('rbl600_02', 30)	# 132680-132709
    sprite('rbl600_03', 6)	# 132710-132715
    sprite('rbl600_04', 6)	# 132716-132721
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 132722-132727
    sprite('rbl600_06', 6)	# 132728-132733
    Unknown21007(24, 40)
    Unknown23018(1)
    label(162)
    sprite('rbl000_00', 6)	# 132734-132739
    sprite('rbl000_01', 6)	# 132740-132745
    sprite('rbl000_02', 6)	# 132746-132751
    sprite('rbl000_03', 6)	# 132752-132757
    sprite('rbl000_04', 6)	# 132758-132763
    sprite('rbl000_05', 6)	# 132764-132769
    sprite('rbl000_06', 6)	# 132770-132775
    sprite('rbl000_07', 6)	# 132776-132781
    sprite('rbl000_08', 6)	# 132782-132787
    sprite('rbl000_09', 6)	# 132788-132793
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('rbl600_00', 1)	# 132794-132794
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rbl600ugo')
    sprite('rbl600_00', 90)	# 132795-132884
    sprite('rbl600_01', 6)	# 132885-132890
    sprite('rbl600_02', 120)	# 132891-133010
    sprite('rbl600_03', 6)	# 133011-133016
    sprite('rbl600_04', 6)	# 133017-133022
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 133023-133028
    sprite('rbl600_06', 6)	# 133029-133034
    Unknown21007(24, 40)
    Unknown23018(1)
    label(171)
    sprite('rbl000_00', 6)	# 133035-133040
    sprite('rbl000_01', 6)	# 133041-133046
    sprite('rbl000_02', 6)	# 133047-133052
    sprite('rbl000_03', 6)	# 133053-133058
    sprite('rbl000_04', 6)	# 133059-133064
    sprite('rbl000_05', 6)	# 133065-133070
    sprite('rbl000_06', 6)	# 133071-133076
    sprite('rbl000_07', 6)	# 133077-133082
    sprite('rbl000_08', 6)	# 133083-133088
    sprite('rbl000_09', 6)	# 133089-133094
    gotoLabel(171)
    ExitState()
    label(180)
    sprite('rbl600_00', 90)	# 133095-133184
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rbl600uor')
    sprite('rbl600_01', 6)	# 133185-133190
    sprite('rbl600_02', 200)	# 133191-133390
    sprite('rbl600_03', 6)	# 133391-133396
    sprite('rbl600_04', 6)	# 133397-133402
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 133403-133408
    sprite('rbl600_06', 6)	# 133409-133414
    Unknown21007(24, 40)
    Unknown23018(1)
    label(181)
    sprite('rbl000_00', 6)	# 133415-133420
    sprite('rbl000_01', 6)	# 133421-133426
    sprite('rbl000_02', 6)	# 133427-133432
    sprite('rbl000_03', 6)	# 133433-133438
    sprite('rbl000_04', 6)	# 133439-133444
    sprite('rbl000_05', 6)	# 133445-133450
    sprite('rbl000_06', 6)	# 133451-133456
    sprite('rbl000_07', 6)	# 133457-133462
    sprite('rbl000_08', 6)	# 133463-133468
    sprite('rbl000_09', 6)	# 133469-133474
    gotoLabel(181)
    ExitState()
    label(190)
    sprite('rbl600_00', 1)	# 133475-133475
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(191)
    sprite('rbl600_00', 32767)	# 133476-166242
    label(191)
    sprite('rbl600_00', 60)	# 166243-166302
    SFX_1('rbl601uyu')
    sprite('rbl600_01', 6)	# 166303-166308
    sprite('rbl600_02', 150)	# 166309-166458
    sprite('rbl600_03', 6)	# 166459-166464
    sprite('rbl600_04', 6)	# 166465-166470
    SFX_0('019_cloth_a')
    sprite('rbl600_05', 6)	# 166471-166476
    sprite('rbl600_06', 6)	# 166477-166482
    Unknown23018(1)
    label(192)
    sprite('rbl000_00', 6)	# 166483-166488
    sprite('rbl000_01', 6)	# 166489-166494
    sprite('rbl000_02', 6)	# 166495-166500
    sprite('rbl000_03', 6)	# 166501-166506
    sprite('rbl000_04', 6)	# 166507-166512
    sprite('rbl000_05', 6)	# 166513-166518
    sprite('rbl000_06', 6)	# 166519-166524
    sprite('rbl000_07', 6)	# 166525-166530
    sprite('rbl000_08', 6)	# 166531-166536
    sprite('rbl000_09', 6)	# 166537-166542
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('rbl601_00', 1)	# 166543-166543
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rbl600ryn')
    label(201)
    sprite('rbl601_00', 1)	# 166544-166544
    if SLOT_97:
        _gotolabel(201)
    sprite('rbl601_00', 20)	# 166545-166564
    sprite('rbl601_01', 6)	# 166565-166570
    sprite('rbl601_02', 6)	# 166571-166576
    sprite('rbl601_03', 6)	# 166577-166582
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 166583-166588
    sprite('rbl601_05', 6)	# 166589-166594
    Unknown21007(24, 40)
    Unknown21011(240)
    label(202)
    sprite('rbl000_00', 6)	# 166595-166600
    sprite('rbl000_01', 6)	# 166601-166606
    sprite('rbl000_02', 6)	# 166607-166612
    sprite('rbl000_03', 6)	# 166613-166618
    sprite('rbl000_04', 6)	# 166619-166624
    sprite('rbl000_05', 6)	# 166625-166630
    sprite('rbl000_06', 6)	# 166631-166636
    sprite('rbl000_07', 6)	# 166637-166642
    sprite('rbl000_08', 6)	# 166643-166648
    sprite('rbl000_09', 6)	# 166649-166654
    gotoLabel(202)
    ExitState()
    label(210)
    sprite('rbl601_00', 1)	# 166655-166655
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rbl600pmi')
    sprite('rbl601_00', 60)	# 166656-166715
    sprite('rbl601_01', 6)	# 166716-166721
    sprite('rbl601_02', 6)	# 166722-166727
    sprite('rbl601_03', 6)	# 166728-166733
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 166734-166739
    sprite('rbl601_05', 6)	# 166740-166745
    Unknown2037(1)
    Unknown21011(400)
    label(211)
    sprite('rbl000_00', 6)	# 166746-166751
    sprite('rbl000_01', 6)	# 166752-166757
    sprite('rbl000_02', 6)	# 166758-166763
    sprite('rbl000_03', 6)	# 166764-166769
    sprite('rbl000_04', 6)	# 166770-166775
    sprite('rbl000_05', 6)	# 166776-166781
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('rbl000_06', 6)	# 166782-166787
    sprite('rbl000_07', 6)	# 166788-166793
    sprite('rbl000_08', 6)	# 166794-166799
    sprite('rbl000_09', 6)	# 166800-166805
    Unknown2038(-1)
    gotoLabel(211)
    ExitState()
    label(220)
    sprite('rbl601_00', 1)	# 166806-166806
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(221)
    sprite('rbl601_00', 32767)	# 166807-199573
    label(221)
    sprite('rbl601_00', 90)	# 199574-199663
    SFX_1('rbl601biz')
    sprite('rbl601_01', 6)	# 199664-199669
    sprite('rbl601_02', 6)	# 199670-199675
    sprite('rbl601_03', 6)	# 199676-199681
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 199682-199687
    sprite('rbl601_05', 6)	# 199688-199693
    Unknown23018(1)
    label(222)
    sprite('rbl000_00', 6)	# 199694-199699
    sprite('rbl000_01', 6)	# 199700-199705
    sprite('rbl000_02', 6)	# 199706-199711
    sprite('rbl000_03', 6)	# 199712-199717
    sprite('rbl000_04', 6)	# 199718-199723
    sprite('rbl000_05', 6)	# 199724-199729
    sprite('rbl000_06', 6)	# 199730-199735
    sprite('rbl000_07', 6)	# 199736-199741
    sprite('rbl000_08', 6)	# 199742-199747
    sprite('rbl000_09', 6)	# 199748-199753
    gotoLabel(222)
    ExitState()
    label(230)
    sprite('rbl601_00', 1)	# 199754-199754
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rbl600ume')
    sprite('rbl601_00', 120)	# 199755-199874
    sprite('rbl601_01', 6)	# 199875-199880
    sprite('rbl601_02', 6)	# 199881-199886
    sprite('rbl601_03', 6)	# 199887-199892
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 199893-199898
    sprite('rbl601_05', 6)	# 199899-199904
    label(232)
    sprite('rbl000_00', 6)	# 199905-199910
    sprite('rbl000_01', 6)	# 199911-199916
    sprite('rbl000_02', 6)	# 199917-199922
    sprite('rbl000_03', 6)	# 199923-199928
    sprite('rbl000_04', 6)	# 199929-199934
    sprite('rbl000_05', 6)	# 199935-199940
    sprite('rbl000_06', 6)	# 199941-199946
    sprite('rbl000_07', 6)	# 199947-199952
    sprite('rbl000_08', 6)	# 199953-199958
    sprite('rbl000_09', 6)	# 199959-199964
    if SLOT_97:
        _gotolabel(232)
    sprite('rbl000_00', 1)	# 199965-199965
    Unknown21007(24, 40)
    Unknown21011(600)
    label(233)
    sprite('rbl000_00', 6)	# 199966-199971
    sprite('rbl000_01', 6)	# 199972-199977
    sprite('rbl000_02', 6)	# 199978-199983
    sprite('rbl000_03', 6)	# 199984-199989
    sprite('rbl000_04', 6)	# 199990-199995
    sprite('rbl000_05', 6)	# 199996-200001
    sprite('rbl000_06', 6)	# 200002-200007
    sprite('rbl000_07', 6)	# 200008-200013
    sprite('rbl000_08', 6)	# 200014-200019
    sprite('rbl000_09', 6)	# 200020-200025
    gotoLabel(233)
    ExitState()
    label(240)
    sprite('rbl601_00', 1)	# 200026-200026

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    SFX_1('rbl600use')
    label(241)
    sprite('rbl601_00', 1)	# 200027-200027
    if SLOT_97:
        _gotolabel(241)
    sprite('rbl601_00', 30)	# 200028-200057
    sprite('rbl601_00', 32767)	# 200058-232824
    Unknown21007(24, 40)
    label(242)
    sprite('rbl601_01', 6)	# 232825-232830
    sprite('rbl601_02', 6)	# 232831-232836
    sprite('rbl601_03', 6)	# 232837-232842
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 232843-232848
    sprite('rbl601_05', 6)	# 232849-232854
    Unknown21011(30)
    label(243)
    sprite('rbl000_00', 6)	# 232855-232860
    sprite('rbl000_01', 6)	# 232861-232866
    sprite('rbl000_02', 6)	# 232867-232872
    sprite('rbl000_03', 6)	# 232873-232878
    sprite('rbl000_04', 6)	# 232879-232884
    sprite('rbl000_05', 6)	# 232885-232890
    sprite('rbl000_06', 6)	# 232891-232896
    sprite('rbl000_07', 6)	# 232897-232902
    sprite('rbl000_08', 6)	# 232903-232908
    sprite('rbl000_09', 6)	# 232909-232914
    gotoLabel(243)
    label(250)
    sprite('rbl601_00', 32767)	# 232915-265681

    def upon_40():
        clearUponHandler(40)
        sendToLabel(251)
        SFX_1('rbl601bsu')
    label(251)
    sprite('rbl601_00', 1)	# 265682-265682
    if SLOT_97:
        _gotolabel(251)
    sprite('rbl601_00', 20)	# 265683-265702
    sprite('rbl601_01', 6)	# 265703-265708
    sprite('rbl601_02', 6)	# 265709-265714
    sprite('rbl601_03', 6)	# 265715-265720
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 265721-265726
    sprite('rbl601_05', 6)	# 265727-265732
    Unknown21011(30)
    label(252)
    sprite('rbl000_00', 6)	# 265733-265738
    sprite('rbl000_01', 6)	# 265739-265744
    sprite('rbl000_02', 6)	# 265745-265750
    sprite('rbl000_03', 6)	# 265751-265756
    sprite('rbl000_04', 6)	# 265757-265762
    sprite('rbl000_05', 6)	# 265763-265768
    sprite('rbl000_06', 6)	# 265769-265774
    sprite('rbl000_07', 6)	# 265775-265780
    sprite('rbl000_08', 6)	# 265781-265786
    sprite('rbl000_09', 6)	# 265787-265792
    gotoLabel(252)
    label(260)
    sprite('rbl601_00', 1)	# 265793-265793
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rbl600rne')
    label(261)
    sprite('rbl601_00', 1)	# 265794-265794
    if SLOT_97:
        _gotolabel(261)
    sprite('rbl601_00', 20)	# 265795-265814
    sprite('rbl601_01', 6)	# 265815-265820
    Unknown21007(24, 40)
    Unknown21011(120)
    sprite('rbl601_02', 6)	# 265821-265826
    sprite('rbl601_03', 6)	# 265827-265832
    SFX_0('019_cloth_a')
    sprite('rbl601_04', 6)	# 265833-265838
    sprite('rbl601_05', 6)	# 265839-265844
    label(262)
    sprite('rbl000_00', 6)	# 265845-265850
    sprite('rbl000_01', 6)	# 265851-265856
    sprite('rbl000_02', 6)	# 265857-265862
    sprite('rbl000_03', 6)	# 265863-265868
    sprite('rbl000_04', 6)	# 265869-265874
    sprite('rbl000_05', 6)	# 265875-265880
    sprite('rbl000_06', 6)	# 265881-265886
    sprite('rbl000_07', 6)	# 265887-265892
    sprite('rbl000_08', 6)	# 265893-265898
    sprite('rbl000_09', 6)	# 265899-265904
    gotoLabel(262)
    ExitState()
    label(991)
    sprite('rbl000_00', 1)	# 265905-265905
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('rbl000_00', 6)	# 265906-265911
    sprite('rbl000_01', 6)	# 265912-265917
    sprite('rbl000_02', 6)	# 265918-265923
    sprite('rbl000_03', 6)	# 265924-265929
    sprite('rbl000_04', 6)	# 265930-265935
    sprite('rbl000_05', 6)	# 265936-265941
    sprite('rbl000_06', 6)	# 265942-265947
    sprite('rbl000_07', 6)	# 265948-265953
    sprite('rbl000_08', 6)	# 265954-265959
    sprite('rbl000_09', 6)	# 265960-265965
    gotoLabel(992)
    label(993)
    sprite('rbl033_00', 3)	# 265966-265968

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(995)

    def upon_STATE_END():
        Unknown2019(0)
        Unknown3038(1)
        Unknown3001(255)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown3001(255)
    Unknown3004(-20)
    physicsXImpulse(-51000)
    physicsYImpulse(18800)
    setGravity(1500)
    Unknown8002()
    label(994)
    sprite('rbl033_01', 3)	# 265969-265971
    sprite('rbl033_02', 3)	# 265972-265974
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 265975-265977
    ExitState()
    label(1000)
    sprite('rbl649_00', 5)	# 265978-265982
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 8001):
            clearUponHandler(43)
            sendToLabel(1002)
    sprite('rbl649_00', 5)	# 265983-265987
    sprite('rbl649_00', 5)	# 265988-265992
    label(1001)
    sprite('rbl649_00', 1)	# 265993-265993
    gotoLabel(1001)
    label(1002)
    sprite('rbl611_04', 6)	# 265994-265999
    SFX_1('rbl601')
    sprite('rbl611_05', 6)	# 266000-266005
    sprite('rbl611_06', 6)	# 266006-266011
    sprite('rbl611_07', 6)	# 266012-266017
    sprite('rbl611_08', 6)	# 266018-266023
    sprite('rbl611_09', 6)	# 266024-266029
    label(1003)
    sprite('rbl611_09', 1)	# 266030-266030
    if SLOT_97:
        _gotolabel(1003)
    sprite('rbl611_09', 20)	# 266031-266050
    Unknown23029(24, 8005, 0)
    Unknown23029(22, 8005, 0)
    Unknown23029(23, 8005, 0)
    sprite('rbl611_09', 6)	# 266051-266056
    Unknown23029(24, 8002, 0)
    Unknown23029(22, 8002, 0)
    Unknown23029(23, 8002, 0)

    def upon_43():
        if (SLOT_48 == 8004):
            clearUponHandler(43)
            SFX_1('rbl604')
            Unknown23018(1)
        if (SLOT_48 == 8008):
            sendToLabel(1005)
    label(1004)
    sprite('rbl611_09', 5)	# 266057-266061
    gotoLabel(1004)
    label(1005)
    sprite('rbl600_04', 5)	# 266062-266066
    sprite('rbl600_05', 5)	# 266067-266071
    sprite('rbl600_06', 5)	# 266072-266076
    label(1006)
    sprite('rbl000_00', 6)	# 266077-266082
    sprite('rbl000_01', 6)	# 266083-266088
    sprite('rbl000_02', 6)	# 266089-266094
    sprite('rbl000_03', 6)	# 266095-266100
    sprite('rbl000_04', 6)	# 266101-266106
    sprite('rbl000_05', 6)	# 266107-266112
    sprite('rbl000_06', 6)	# 266113-266118
    sprite('rbl000_07', 6)	# 266119-266124
    sprite('rbl000_08', 6)	# 266125-266130
    sprite('rbl000_09', 6)	# 266131-266136
    gotoLabel(1006)
    ExitState()

@State
def CmnActMatchWin():
    if SLOT_169:
        _gotolabel(482)
    if SLOT_122:
        _gotolabel(482)
    if SLOT_123:
        _gotolabel(482)
    sprite('keep', 2)	# 1-2

    def upon_CLEAR_OR_EXIT():
        SLOT_58 = 1
        Unknown48('19000000020000003400000018000000020000003a000000')
        if SLOT_52:
            if PartnerChar('brg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('biz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('ume'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('use'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
            if PartnerChar('bsu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(250)
                    clearUponHandler(3)
            if PartnerChar('rne'):
                if (SLOT_145 <= 500000):
                    sendToLabel(260)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(1)
    label(0)
    sprite('rbl610_00', 6)	# 4-9
    if SLOT_158:
        if SLOT_52:
            Unknown7006('rbl524', 100, 896295538, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('rbl402', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rbl520', 100, 896295538, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('rbl610_01', 6)	# 10-15
    sprite('rbl610_02', 6)	# 16-21
    sprite('rbl610_03', 6)	# 22-27
    sprite('rbl610_04', 6)	# 28-33
    sprite('rbl610_05', 6)	# 34-39
    sprite('rbl610_06', 8)	# 40-47
    sprite('rbl610_07', 8)	# 48-55
    sprite('rbl610_08', 6)	# 56-61
    sprite('rbl610_09', 6)	# 62-67
    sprite('rbl610_10', 6)	# 68-73
    sprite('rbl610_11', 6)	# 74-79
    sprite('rbl610_12', 32767)	# 80-32846
    label(1)
    sprite('rbl611_00', 6)	# 32847-32852
    if SLOT_158:
        if SLOT_52:
            Unknown7006('rbl524', 100, 896295538, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('rbl402', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rbl522', 100, 896295538, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('rbl611_01', 6)	# 32853-32858
    sprite('rbl611_02', 6)	# 32859-32864
    sprite('rbl611_03', 6)	# 32865-32870
    sprite('rbl611_04', 6)	# 32871-32876
    sprite('rbl611_05', 6)	# 32877-32882
    sprite('rbl611_06', 6)	# 32883-32888
    sprite('rbl611_07', 30)	# 32889-32918
    sprite('rbl611_08', 6)	# 32919-32924
    sprite('rbl611_09', 32767)	# 32925-65691
    label(100)
    sprite('rbl000_00', 1)	# 65692-65692

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('rbl000_00', 6)	# 65693-65698
    sprite('rbl000_01', 6)	# 65699-65704
    sprite('rbl000_02', 6)	# 65705-65710
    sprite('rbl000_03', 6)	# 65711-65716
    sprite('rbl000_04', 6)	# 65717-65722
    sprite('rbl000_05', 6)	# 65723-65728
    sprite('rbl000_06', 6)	# 65729-65734
    sprite('rbl000_07', 6)	# 65735-65740
    sprite('rbl000_08', 6)	# 65741-65746
    sprite('rbl000_09', 6)	# 65747-65752
    gotoLabel(101)
    label(102)
    sprite('rbl611_00', 6)	# 65753-65758
    if (SLOT_38 == 1):
        if (SLOT_152 == 1):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                Unknown2005()
    if (SLOT_38 == 0):
        if (SLOT_152 == 0):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                Unknown2005()
    SFX_1('rbl701brg')
    sprite('rbl611_01', 6)	# 65759-65764
    sprite('rbl611_02', 6)	# 65765-65770
    sprite('rbl611_03', 6)	# 65771-65776
    sprite('rbl611_04', 6)	# 65777-65782
    sprite('rbl611_05', 6)	# 65783-65788
    sprite('rbl611_06', 6)	# 65789-65794
    sprite('rbl611_07', 30)	# 65795-65824
    sprite('rbl611_08', 6)	# 65825-65830
    sprite('rbl611_09', 32767)	# 65831-98597
    Unknown23018(1)
    label(110)
    sprite('rbl000_00', 1)	# 98598-98598

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('rbl000_00', 6)	# 98599-98604
    sprite('rbl000_01', 6)	# 98605-98610
    sprite('rbl000_02', 6)	# 98611-98616
    sprite('rbl000_03', 6)	# 98617-98622
    sprite('rbl000_04', 6)	# 98623-98628
    sprite('rbl000_05', 6)	# 98629-98634
    sprite('rbl000_06', 6)	# 98635-98640
    sprite('rbl000_07', 6)	# 98641-98646
    sprite('rbl000_08', 6)	# 98647-98652
    sprite('rbl000_09', 6)	# 98653-98658
    gotoLabel(111)
    label(112)
    sprite('rbl611_00', 6)	# 98659-98664
    SFX_1('rbl701bjn')
    sprite('rbl611_01', 6)	# 98665-98670
    sprite('rbl611_02', 6)	# 98671-98676
    sprite('rbl611_03', 6)	# 98677-98682
    sprite('rbl611_04', 6)	# 98683-98688
    sprite('rbl611_05', 6)	# 98689-98694
    sprite('rbl611_06', 6)	# 98695-98700
    sprite('rbl611_07', 30)	# 98701-98730
    sprite('rbl611_08', 6)	# 98731-98736
    sprite('rbl611_09', 32767)	# 98737-131503
    Unknown23018(1)
    label(120)
    sprite('rbl000_00', 1)	# 131504-131504
    if (not SLOT_53):
        if random_(2, 0, 50):
            sendToLabel(0)
        else:
            sendToLabel(1)
    sprite('rbl000_00', 1)	# 131505-131505
    Unknown2034(0)
    Unknown2053(0)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('rbl000_00', 6)	# 131506-131511
    sprite('rbl000_01', 6)	# 131512-131517
    sprite('rbl000_02', 6)	# 131518-131523
    sprite('rbl000_03', 6)	# 131524-131529
    sprite('rbl000_04', 6)	# 131530-131535
    sprite('rbl000_05', 6)	# 131536-131541
    sprite('rbl000_06', 6)	# 131542-131547
    sprite('rbl000_07', 6)	# 131548-131553
    sprite('rbl000_08', 6)	# 131554-131559
    sprite('rbl000_09', 6)	# 131560-131565
    gotoLabel(121)
    label(122)
    sprite('rbl610_00', 6)	# 131566-131571
    SFX_1('rbl701bhz')
    sprite('rbl610_01', 6)	# 131572-131577
    sprite('rbl610_02', 6)	# 131578-131583
    sprite('rbl610_03', 6)	# 131584-131589
    sprite('rbl610_04', 6)	# 131590-131595
    sprite('rbl610_05', 6)	# 131596-131601
    sprite('rbl610_06', 8)	# 131602-131609
    sprite('rbl610_07', 8)	# 131610-131617
    sprite('rbl610_08', 6)	# 131618-131623
    sprite('rbl610_09', 6)	# 131624-131629
    sprite('rbl610_10', 6)	# 131630-131635
    sprite('rbl610_11', 6)	# 131636-131641
    sprite('rbl610_12', 32767)	# 131642-164408
    Unknown23018(1)
    label(130)
    sprite('rbl610_00', 6)	# 164409-164414
    SFX_1('rbl700bjb')
    sprite('rbl610_01', 6)	# 164415-164420
    sprite('rbl610_02', 6)	# 164421-164426
    sprite('rbl610_03', 6)	# 164427-164432
    sprite('rbl610_04', 6)	# 164433-164438
    sprite('rbl610_05', 6)	# 164439-164444
    sprite('rbl610_06', 8)	# 164445-164452
    sprite('rbl610_07', 8)	# 164453-164460
    sprite('rbl610_08', 6)	# 164461-164466
    sprite('rbl610_09', 6)	# 164467-164472
    sprite('rbl610_10', 6)	# 164473-164478
    sprite('rbl610_11', 6)	# 164479-164484
    label(131)
    sprite('rbl610_12', 1)	# 164485-164485
    if SLOT_97:
        _gotolabel(131)
    sprite('rbl610_12', 32767)	# 164486-197252
    Unknown21007(24, 40)
    Unknown21011(240)
    label(140)
    sprite('rbl000_00', 1)	# 197253-197253

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('rbl000_00', 6)	# 197254-197259
    sprite('rbl000_01', 6)	# 197260-197265
    sprite('rbl000_02', 6)	# 197266-197271
    sprite('rbl000_03', 6)	# 197272-197277
    sprite('rbl000_04', 6)	# 197278-197283
    sprite('rbl000_05', 6)	# 197284-197289
    sprite('rbl000_06', 6)	# 197290-197295
    sprite('rbl000_07', 6)	# 197296-197301
    sprite('rbl000_08', 6)	# 197302-197307
    sprite('rbl000_09', 6)	# 197308-197313
    gotoLabel(141)
    label(142)
    sprite('rbl611_00', 6)	# 197314-197319
    SFX_1('rbl701uhy')
    sprite('rbl611_01', 6)	# 197320-197325
    sprite('rbl611_02', 6)	# 197326-197331
    sprite('rbl611_03', 6)	# 197332-197337
    sprite('rbl611_04', 6)	# 197338-197343
    sprite('rbl611_05', 6)	# 197344-197349
    sprite('rbl611_06', 6)	# 197350-197355
    sprite('rbl611_07', 30)	# 197356-197385
    sprite('rbl611_08', 6)	# 197386-197391
    sprite('rbl611_09', 32767)	# 197392-230158
    Unknown21011(150)
    label(150)
    sprite('rbl611_00', 6)	# 230159-230164
    sprite('rbl611_01', 6)	# 230165-230170
    sprite('rbl611_02', 6)	# 230171-230176
    sprite('rbl611_03', 6)	# 230177-230182
    sprite('rbl611_04', 6)	# 230183-230188
    SFX_1('rbl700ugo')
    sprite('rbl611_05', 6)	# 230189-230194
    sprite('rbl611_06', 6)	# 230195-230200
    sprite('rbl611_07', 30)	# 230201-230230
    sprite('rbl611_08', 6)	# 230231-230236
    label(151)
    sprite('rbl611_09', 1)	# 230237-230237
    if SLOT_97:
        _gotolabel(151)
    sprite('rbl611_09', 32767)	# 230238-263004
    Unknown21007(24, 40)
    Unknown21011(240)
    label(160)
    sprite('rbl000_00', 1)	# 263005-263005

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('rbl000_00', 6)	# 263006-263011
    sprite('rbl000_01', 6)	# 263012-263017
    sprite('rbl000_02', 6)	# 263018-263023
    sprite('rbl000_03', 6)	# 263024-263029
    sprite('rbl000_04', 6)	# 263030-263035
    sprite('rbl000_05', 6)	# 263036-263041
    sprite('rbl000_06', 6)	# 263042-263047
    sprite('rbl000_07', 6)	# 263048-263053
    sprite('rbl000_08', 6)	# 263054-263059
    sprite('rbl000_09', 6)	# 263060-263065
    gotoLabel(161)
    label(162)
    sprite('rbl611_00', 6)	# 263066-263071
    SFX_1('rbl701rwi')
    sprite('rbl611_01', 6)	# 263072-263077
    sprite('rbl611_02', 6)	# 263078-263083
    sprite('rbl611_03', 6)	# 263084-263089
    sprite('rbl611_04', 6)	# 263090-263095
    sprite('rbl611_05', 6)	# 263096-263101
    sprite('rbl611_06', 6)	# 263102-263107
    sprite('rbl611_07', 30)	# 263108-263137
    sprite('rbl611_08', 6)	# 263138-263143
    sprite('rbl611_09', 32767)	# 263144-295910
    Unknown23018(1)
    label(170)
    sprite('rbl610_00', 6)	# 295911-295916
    SFX_1('rbl700uor')
    sprite('rbl610_01', 6)	# 295917-295922
    sprite('rbl610_02', 6)	# 295923-295928
    sprite('rbl610_03', 6)	# 295929-295934
    sprite('rbl610_04', 6)	# 295935-295940
    sprite('rbl610_05', 6)	# 295941-295946
    sprite('rbl610_06', 8)	# 295947-295954
    sprite('rbl610_07', 8)	# 295955-295962
    sprite('rbl610_08', 6)	# 295963-295968
    sprite('rbl610_09', 6)	# 295969-295974
    sprite('rbl610_10', 6)	# 295975-295980
    sprite('rbl610_11', 6)	# 295981-295986
    label(171)
    sprite('rbl610_12', 1)	# 295987-295987
    if SLOT_97:
        _gotolabel(171)
    sprite('rbl610_12', 32767)	# 295988-328754
    Unknown21007(24, 40)
    Unknown21011(260)
    label(180)
    sprite('rbl000_00', 1)	# 328755-328755

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('rbl000_00', 6)	# 328756-328761
    sprite('rbl000_01', 6)	# 328762-328767
    sprite('rbl000_02', 6)	# 328768-328773
    sprite('rbl000_03', 6)	# 328774-328779
    sprite('rbl000_04', 6)	# 328780-328785
    sprite('rbl000_05', 6)	# 328786-328791
    sprite('rbl000_06', 6)	# 328792-328797
    sprite('rbl000_07', 6)	# 328798-328803
    sprite('rbl000_08', 6)	# 328804-328809
    sprite('rbl000_09', 6)	# 328810-328815
    gotoLabel(181)
    label(182)
    sprite('rbl610_00', 6)	# 328816-328821
    SFX_1('rbl701rrb')
    sprite('rbl610_01', 6)	# 328822-328827
    sprite('rbl610_02', 6)	# 328828-328833
    sprite('rbl610_03', 6)	# 328834-328839
    sprite('rbl610_04', 6)	# 328840-328845
    sprite('rbl610_05', 6)	# 328846-328851
    sprite('rbl610_06', 8)	# 328852-328859
    sprite('rbl610_07', 8)	# 328860-328867
    sprite('rbl610_08', 6)	# 328868-328873
    sprite('rbl610_09', 6)	# 328874-328879
    sprite('rbl610_10', 6)	# 328880-328885
    sprite('rbl610_11', 6)	# 328886-328891
    sprite('rbl610_12', 32767)	# 328892-361658
    Unknown23018(1)
    label(190)
    sprite('rbl000_00', 1)	# 361659-361659

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('rbl000_00', 6)	# 361660-361665
    sprite('rbl000_01', 6)	# 361666-361671
    sprite('rbl000_02', 6)	# 361672-361677
    sprite('rbl000_03', 6)	# 361678-361683
    sprite('rbl000_04', 6)	# 361684-361689
    sprite('rbl000_05', 6)	# 361690-361695
    sprite('rbl000_06', 6)	# 361696-361701
    sprite('rbl000_07', 6)	# 361702-361707
    sprite('rbl000_08', 6)	# 361708-361713
    sprite('rbl000_09', 6)	# 361714-361719
    gotoLabel(191)
    label(192)
    sprite('rbl300_00', 6)	# 361720-361725
    SFX_1('rbl701uyu')
    sprite('rbl300_01', 6)	# 361726-361731
    sprite('rbl300_02', 6)	# 361732-361737
    sprite('rbl300_03', 6)	# 361738-361743
    sprite('rbl300_04', 32767)	# 361744-394510
    Unknown23018(1)
    label(200)
    sprite('rbl610_00', 6)	# 394511-394516
    SFX_1('rbl700ryn')
    sprite('rbl610_01', 6)	# 394517-394522
    sprite('rbl610_02', 6)	# 394523-394528
    sprite('rbl610_03', 6)	# 394529-394534
    sprite('rbl610_04', 6)	# 394535-394540
    sprite('rbl610_05', 6)	# 394541-394546
    sprite('rbl610_06', 8)	# 394547-394554
    sprite('rbl610_07', 8)	# 394555-394562
    sprite('rbl610_08', 6)	# 394563-394568
    sprite('rbl610_09', 6)	# 394569-394574
    sprite('rbl610_10', 6)	# 394575-394580
    sprite('rbl610_11', 6)	# 394581-394586
    label(201)
    sprite('rbl610_12', 1)	# 394587-394587
    if SLOT_97:
        _gotolabel(201)
    sprite('rbl610_12', 30)	# 394588-394617
    sprite('rbl610_12', 32767)	# 394618-427384
    Unknown21007(24, 40)
    Unknown21011(120)
    label(210)
    sprite('rbl610_00', 6)	# 427385-427390
    SFX_1('rbl700pmi')
    sprite('rbl610_01', 6)	# 427391-427396
    sprite('rbl610_02', 6)	# 427397-427402
    sprite('rbl610_03', 6)	# 427403-427408
    sprite('rbl610_04', 6)	# 427409-427414
    sprite('rbl610_05', 6)	# 427415-427420
    sprite('rbl610_06', 8)	# 427421-427428
    sprite('rbl610_07', 8)	# 427429-427436
    sprite('rbl610_08', 6)	# 427437-427442
    sprite('rbl610_09', 6)	# 427443-427448
    sprite('rbl610_10', 6)	# 427449-427454
    sprite('rbl610_11', 6)	# 427455-427460
    label(211)
    sprite('rbl610_12', 1)	# 427461-427461
    if SLOT_97:
        _gotolabel(211)
    sprite('rbl610_12', 30)	# 427462-427491
    sprite('rbl610_12', 32767)	# 427492-460258
    Unknown21007(24, 40)
    Unknown21011(240)
    label(220)
    sprite('rbl000_00', 1)	# 460259-460259

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('rbl000_00', 6)	# 460260-460265
    sprite('rbl000_01', 6)	# 460266-460271
    sprite('rbl000_02', 6)	# 460272-460277
    sprite('rbl000_03', 6)	# 460278-460283
    sprite('rbl000_04', 6)	# 460284-460289
    sprite('rbl000_05', 6)	# 460290-460295
    sprite('rbl000_06', 6)	# 460296-460301
    sprite('rbl000_07', 6)	# 460302-460307
    sprite('rbl000_08', 6)	# 460308-460313
    sprite('rbl000_09', 6)	# 460314-460319
    gotoLabel(221)
    label(222)
    sprite('rbl611_00', 6)	# 460320-460325
    sprite('rbl611_01', 6)	# 460326-460331
    SFX_1('rbl701biz')
    sprite('rbl611_02', 6)	# 460332-460337
    sprite('rbl611_03', 6)	# 460338-460343
    sprite('rbl611_04', 6)	# 460344-460349
    sprite('rbl611_05', 6)	# 460350-460355
    sprite('rbl611_06', 6)	# 460356-460361
    sprite('rbl611_07', 30)	# 460362-460391
    sprite('rbl611_08', 6)	# 460392-460397
    sprite('rbl611_09', 32767)	# 460398-493164
    Unknown23018(1)
    label(230)
    sprite('rbl000_00', 1)	# 493165-493165

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('rbl000_00', 6)	# 493166-493171
    sprite('rbl000_01', 6)	# 493172-493177
    sprite('rbl000_02', 6)	# 493178-493183
    sprite('rbl000_03', 6)	# 493184-493189
    sprite('rbl000_04', 6)	# 493190-493195
    sprite('rbl000_05', 6)	# 493196-493201
    sprite('rbl000_06', 6)	# 493202-493207
    sprite('rbl000_07', 6)	# 493208-493213
    sprite('rbl000_08', 6)	# 493214-493219
    sprite('rbl000_09', 6)	# 493220-493225
    gotoLabel(231)
    label(232)
    sprite('rbl610_00', 6)	# 493226-493231
    SFX_1('rbl701ume')
    sprite('rbl610_01', 6)	# 493232-493237
    sprite('rbl610_02', 6)	# 493238-493243
    sprite('rbl610_03', 6)	# 493244-493249
    sprite('rbl610_04', 6)	# 493250-493255
    sprite('rbl610_05', 6)	# 493256-493261
    sprite('rbl610_06', 8)	# 493262-493269
    sprite('rbl610_07', 8)	# 493270-493277
    sprite('rbl610_08', 6)	# 493278-493283
    sprite('rbl610_09', 6)	# 493284-493289
    sprite('rbl610_10', 6)	# 493290-493295
    sprite('rbl610_11', 6)	# 493296-493301
    sprite('rbl610_12', 32767)	# 493302-526068
    Unknown23018(1)
    label(240)
    sprite('rbl000_00', 1)	# 526069-526069

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    label(241)
    sprite('rbl000_00', 6)	# 526070-526075
    sprite('rbl000_01', 6)	# 526076-526081
    sprite('rbl000_02', 6)	# 526082-526087
    sprite('rbl000_03', 6)	# 526088-526093
    sprite('rbl000_04', 6)	# 526094-526099
    sprite('rbl000_05', 6)	# 526100-526105
    sprite('rbl000_06', 6)	# 526106-526111
    sprite('rbl000_07', 6)	# 526112-526117
    sprite('rbl000_08', 6)	# 526118-526123
    sprite('rbl000_09', 6)	# 526124-526129
    gotoLabel(241)
    label(242)
    sprite('rbl611_00', 6)	# 526130-526135
    sprite('rbl611_01', 6)	# 526136-526141
    SFX_1('rbl701use')
    sprite('rbl611_02', 6)	# 526142-526147
    sprite('rbl611_03', 6)	# 526148-526153
    sprite('rbl611_04', 6)	# 526154-526159
    sprite('rbl611_05', 6)	# 526160-526165
    sprite('rbl611_06', 6)	# 526166-526171
    sprite('rbl611_07', 30)	# 526172-526201
    sprite('rbl611_08', 6)	# 526202-526207
    sprite('rbl611_09', 32767)	# 526208-558974
    Unknown23018(1)
    label(250)
    sprite('rbl000_00', 1)	# 558975-558975

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
    label(251)
    sprite('rbl000_00', 6)	# 558976-558981
    sprite('rbl000_01', 6)	# 558982-558987
    sprite('rbl000_02', 6)	# 558988-558993
    sprite('rbl000_03', 6)	# 558994-558999
    sprite('rbl000_04', 6)	# 559000-559005
    sprite('rbl000_05', 6)	# 559006-559011
    sprite('rbl000_06', 6)	# 559012-559017
    sprite('rbl000_07', 6)	# 559018-559023
    sprite('rbl000_08', 6)	# 559024-559029
    sprite('rbl000_09', 6)	# 559030-559035
    gotoLabel(251)
    label(252)
    sprite('rbl610_00', 6)	# 559036-559041
    sprite('rbl610_01', 6)	# 559042-559047
    sprite('rbl610_02', 6)	# 559048-559053
    sprite('rbl610_03', 6)	# 559054-559059
    sprite('rbl610_04', 6)	# 559060-559065
    sprite('rbl610_05', 6)	# 559066-559071
    sprite('rbl610_06', 8)	# 559072-559079
    sprite('rbl610_07', 8)	# 559080-559087
    sprite('rbl610_08', 6)	# 559088-559093
    sprite('rbl610_09', 6)	# 559094-559099
    SFX_1('rbl701bsu')
    sprite('rbl610_10', 6)	# 559100-559105
    sprite('rbl610_11', 6)	# 559106-559111
    sprite('rbl610_12', 32767)	# 559112-591878
    Unknown23018(1)
    label(260)
    sprite('rbl610_00', 6)	# 591879-591884
    sprite('rbl610_01', 6)	# 591885-591890
    sprite('rbl610_02', 6)	# 591891-591896
    sprite('rbl610_03', 6)	# 591897-591902
    sprite('rbl610_04', 6)	# 591903-591908
    sprite('rbl610_05', 6)	# 591909-591914
    sprite('rbl610_06', 8)	# 591915-591922
    sprite('rbl610_07', 8)	# 591923-591930
    sprite('rbl610_08', 6)	# 591931-591936
    sprite('rbl610_09', 6)	# 591937-591942
    SFX_1('rbl700rne')
    sprite('rbl610_10', 6)	# 591943-591948
    sprite('rbl610_11', 6)	# 591949-591954
    label(261)
    sprite('rbl610_12', 1)	# 591955-591955
    if SLOT_97:
        _gotolabel(261)
    sprite('rbl610_12', 30)	# 591956-591985
    sprite('rbl610_12', 32767)	# 591986-624752
    Unknown21007(24, 40)
    Unknown21011(180)

@State
def CmnActLose():
    sprite('rbl620_00', 6)	# 1-6
    sprite('rbl620_01', 6)	# 7-12
    sprite('rbl620_02', 6)	# 13-18
    sprite('rbl620_03', 6)	# 19-24
    sprite('rbl620_04', 6)	# 25-30
    sprite('rbl620_05', 6)	# 31-36
    sprite('rbl620_06', 32767)	# 37-32803
    if SLOT_158:
        SFX_1('rbl403')
    Unknown23018(1)