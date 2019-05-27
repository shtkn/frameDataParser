@Subroutine
def PreInit():
    Unknown12019('626e7900000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(14000)
    DashFInitialVelocity(20000)
    DashFMaxVelocity(30000)
    Unknown12024(2)
    Unknown13039(4)
    Unknown2049(1)
    Unknown15019(5000)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('SpecialDashF', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown14005(1)
    Unknown15027(0)
    Unknown15013(0)
    Unknown15012(2000)
    Unknown14015(0, 400000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('SpecialDashB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xdb)
    Unknown14005(1)
    Unknown15013(1)
    Unknown15012(2000)
    Unknown14015(450000, 850000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('SpecialDashAirF', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(0xda)
    Move_AirGround_(0x2007)
    Unknown14005(1)
    Move_AirGround_(0x3036)
    Unknown15027(0)
    Unknown15013(1)
    Unknown15012(2000)
    Unknown14015(450000, 1250000, -500000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('SpecialDashAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(0xdb)
    Move_AirGround_(0x2007)
    Unknown14005(1)
    Move_AirGround_(0x3036)
    Unknown15012(2000)
    Unknown14015(450000, 1250000, -500000, 400000, 1000, 0)
    Move_EndRegister()
    Move_Register('DelayShot_Atk', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_PRESS_B)
    Unknown14018(1, 0, 0)
    Unknown14024('CheckLockReject')
    Unknown14019('Func_DelayShot_Atk')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5A_2nd', 0x7)
    Unknown15015(35, 36)
    Unknown14005(1)
    Unknown14015(300000, 500000, -200000, 180000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_3rd', 0x7)
    Unknown14005(1)
    Unknown15013(1500)
    Unknown15015(35, 37)
    Unknown14015(0, 550000, -100000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_4th', 0x7)
    Unknown14005(1)
    Unknown15013(1500)
    Unknown14015(0, 1000000, -200000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown14015(0, 350000, -100000, 130000, 1000, 50)
    Unknown15009()
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown15021(2000)
    Unknown14015(0, 350000, -200000, 300000, 750, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15013(1500)
    Unknown14015(350000, 1200000, -200000, 180000, 800, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_2nd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_3rd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_4th', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_3rdEx', 0x1)
    Move_Input_(0x9a)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_4thEx', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_5th', 0x1)
    Move_AirGround_(0x2000)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(2000)
    Unknown15012(1)
    Unknown14015(250000, 750000, 200000, 1200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B_2nd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B_3rd', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B_4th', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B_3rdEx', 0x1)
    Move_Input_(0x9a)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk2B_4thEx', 0x1)
    Move_Input_(0x9a)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown15021(1)
    Unknown15015(28, 30)
    Unknown14015(0, 550000, -100000, 160000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15015(28, 30)
    Unknown15013(2000)
    Unknown14015(-100000, 400000, -250000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2nd', 0x10)
    Unknown14005(1)
    Unknown15015(28, 30)
    Unknown15013(1500)
    Unknown14015(-100000, 350000, -250000, 150000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(350000, 900000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_2nd', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_3rd', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_4th', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_5th', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_3rdEx', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x45)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_4thEx', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B', 0x1f)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(250000, 650000, -400000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B_2nd', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B_3rd', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B_4th', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15006(10000)
    Unknown15013(5000)
    Unknown14015(0, 1500000, -200000, 500000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B_3rdEx', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x45)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B_4thEx', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(250000, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 150000, 200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 150000, 200, 0)
    Move_EndRegister()
    Move_Register('LowShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3008)
    Unknown15013(1)
    Unknown14015(1500000, 750000, -200000, 100000, 500, 50)
    Move_EndRegister()
    Move_Register('LowShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3008)
    Unknown14015(800000, 750000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('LowShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3008)
    Unknown14015(150000, 750000, -200000, 100000, 250, 50)
    Move_EndRegister()
    Move_Register('LargeShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x300a)
    Unknown15014(1)
    Unknown15006(1)
    Unknown14015(100000, 200000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('LargeShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x300a)
    Unknown15014(1)
    Unknown15006(1)
    Unknown14015(1000000, 1500000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('LargeShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x300a)
    Unknown15014(1)
    Unknown15006(1)
    Unknown14015(1000000, 1500000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(6000)
    Unknown14015(-50000, 300000, -100000, 350000, 200, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15014(6000)
    Unknown14015(-50000, 300000, -100000, 350000, 200, 0)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordLand', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(150000, 450000, -200000, 400000, 800, 10)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordLandOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15014(2000)
    Unknown15013(1)
    Unknown15012(1)
    Unknown14015(150000, 450000, -200000, 400000, 800, 10)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordAir', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(150000, 450000, -200000, 400000, 800, 10)
    Move_EndRegister()
    Move_Register('UltimateLargeSwordAirOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown14015(150000, 450000, -200000, 400000, 800, 10)
    Move_EndRegister()
    Move_Register('UltimateMultiSword', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x300b)
    Unknown15013(5000)
    Unknown14015(500000, 1800000, -200000, 200000, 750, 0)
    Move_EndRegister()
    Move_Register('UltimateMultiSwordOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x300b)
    Unknown15013(5000)
    Unknown14015(500000, 1800000, -200000, 200000, 750, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A_2nd', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk5A_2nd', 10000000)
    Unknown15024('NmlAtk5A_2nd', 'NmlAtk5A_3rd', 10000000)
    Unknown15024('NmlAtk5A_3rd', 'NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B_2nd', 10000000)
    Unknown15024('NmlAtk5B_2nd', 'NmlAtk5B_3rd', 10000000)
    Unknown15024('NmlAtk5B_3rd', 'NmlAtk5B_4th', 10000000)
    Unknown15024('NmlAtk5B_4th', 'NmlAtk5B_5th', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2B_2nd', 10000000)
    Unknown15024('NmlAtk2B_2nd', 'NmlAtk2B_3rd', 10000000)
    Unknown15024('NmlAtk2B_3rd', 'NmlAtk2B_4th', 10000000)
    Unknown15024('NmlAtk2B_4th', 'NmlAtk5B_5th', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5B_2nd', 10000000)
    Unknown15024('NmlAtkAIR5B_2nd', 'NmlAtkAIR5B_3rd', 10000000)
    Unknown15024('NmlAtkAIR5B_3rd', 'NmlAtkAIR5B_4th', 10000000)
    Unknown15024('NmlAtkAIR5B_4th', 'NmlAtkAIR5B_5th', 10000000)
    Unknown15024('NmlAtkAIR2B', 'NmlAtkAIR2B_2nd', 10000000)
    Unknown15024('NmlAtkAIR2B_2nd', 'NmlAtkAIR2B_3rd', 10000000)
    Unknown15024('NmlAtkAIR2B_3rd', 'NmlAtkAIR2B_4th', 10000000)
    Unknown15024('NmlAtkAIR2B_4th', 'NmlAtkAIR2B_5th', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A_2nd', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2C', 'LowShotA', 10000000)
    Unknown12018(0, 'ny062_01')
    Unknown12018(1, 'ny062_03')
    Unknown12018(2, 'ny062_04')
    Unknown12018(3, 'ny062_05')
    Unknown12018(4, 'ny062_06')
    Unknown12018(5, 'ny062_07')
    Unknown12018(6, 'ny062_09')
    Unknown12018(7, 'ny041_02')
    Unknown12018(8, 'ny040_02')
    Unknown12018(9, 'ny045_02')
    Unknown12018(10, 'ny060_00')
    Unknown12018(11, 'ny060_01')
    Unknown12018(12, 'ny060_03')
    Unknown12018(13, 'ny060_05')
    Unknown12018(14, 'ny060_07')
    Unknown12018(15, 'ny060_14')
    Unknown12018(16, 'ny050_00')
    Unknown12018(17, 'ny052_00')
    Unknown12018(18, 'ny054_00')
    Unknown12018(19, 'ny000_00')
    Unknown12018(20, 'ny000_00')
    Unknown12018(25, 'ny063_00')
    Unknown12018(26, 'ny063_01')
    Unknown12018(27, 'ny063_02')
    Unknown12018(28, 'ny063_05')
    Unknown12018(29, 'ny063_11')
    Unknown12018(24, 'ny073_01')
    Unknown7010(0, 'bny000')
    Unknown7010(1, 'bny001')
    Unknown7010(2, 'bny002')
    Unknown7010(3, 'bny003')
    Unknown7010(4, 'bny004')
    Unknown7010(5, 'bny005')
    Unknown7010(6, 'bny006')
    Unknown7010(7, 'bny007')
    Unknown7010(8, 'bny008')
    Unknown7010(9, 'bny009')
    Unknown7010(10, 'bny010')
    Unknown7010(15, 'bny011')
    Unknown7010(16, 'bny012')
    Unknown7010(17, 'bny013')
    Unknown7010(18, 'bny014')
    Unknown7010(19, 'bny015')
    Unknown7010(20, 'bny016')
    Unknown7010(21, 'bny017')
    Unknown7010(22, 'bny018')
    Unknown7010(23, 'bny019')
    Unknown7010(24, 'bny020')
    Unknown7010(25, 'bny021')
    Unknown7010(28, 'bny022')
    Unknown7010(29, 'bny023')
    Unknown7010(30, 'bny024')
    Unknown7010(31, 'bny025')
    Unknown7010(32, 'bny026')
    Unknown7010(33, 'bny027')
    Unknown7010(34, 'bny028')
    Unknown7010(35, 'bny029')
    Unknown7010(36, 'bny030')
    Unknown7010(37, 'bny031')
    Unknown7010(39, 'bny032')
    Unknown7010(42, 'bny033')
    Unknown7010(43, 'bny034')
    Unknown7010(44, 'bny035')
    Unknown7010(45, 'bny036')
    Unknown7010(46, 'bny037')
    Unknown7010(47, 'bny038')
    Unknown7010(48, 'bny039')
    Unknown7010(49, 'bny040')
    Unknown7010(50, 'bny041')
    Unknown7010(52, 'bny042')
    Unknown7010(53, 'bny043')
    Unknown7010(54, 'bny100_0')
    Unknown7010(55, 'bny100_1')
    Unknown7010(56, 'bny100_2')
    Unknown7010(63, 'bny101_0')
    Unknown7010(64, 'bny101_1')
    Unknown7010(65, 'bny101_2')
    Unknown7010(57, 'bny102_0')
    Unknown7010(58, 'bny102_1')
    Unknown7010(59, 'bny102_2')
    Unknown7010(66, 'bny103_0')
    Unknown7010(67, 'bny103_1')
    Unknown7010(68, 'bny103_2')
    Unknown7010(60, 'bny104_0')
    Unknown7010(61, 'bny104_1')
    Unknown7010(62, 'bny104_2')
    Unknown7010(69, 'bny105_0')
    Unknown7010(70, 'bny105_1')
    Unknown7010(71, 'bny105_2')
    Unknown7010(72, 'bny150')
    Unknown7010(73, 'bny151')
    Unknown7010(74, 'bny152')
    Unknown7010(85, 'bny153')
    Unknown7010(87, 'bny155')
    Unknown7010(88, 'bny154')
    Unknown7010(96, 'bny161_0')
    Unknown7010(97, 'bny161_1')
    Unknown7010(92, 'bny162_0')
    Unknown7010(93, 'bny162_1')
    Unknown7010(98, 'bny163_0')
    Unknown7010(99, 'bny163_1')
    Unknown7010(100, 'bny164_0')
    Unknown7010(101, 'bny164_1')
    Unknown7010(105, 'bny165_0')
    Unknown7010(106, 'bny165_1')
    Unknown7010(102, 'bny166_0')
    Unknown7010(103, 'bny166_1')
    Unknown7010(90, 'bny167_0')
    Unknown7010(91, 'bny167_1')
    Unknown7010(107, 'bny168_0')
    Unknown7010(108, 'bny168_1')
    Unknown7010(110, 'bny169_0')
    Unknown7010(111, 'bny169_1')
    Unknown7010(94, 'bny400_0')
    Unknown7010(95, 'bny400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654d756c746953776f72640000000000000000000000000000')
    Unknown12059('03000000556c74696d6174654d756c746953776f72644f44000000000000000000000000')
    Unknown12059('04000000556c74696d6174654c6172676553776f72644c616e6400000000000000000000')
    Unknown12059('05000000556c74696d6174654c6172676553776f72644c616e644f440000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnEnemyComboBreak():
    SLOT_62 = 0

@Subroutine
def DriveVoice():
    SLOT_62 = (SLOT_62 + 1)
    if (SLOT_62 == 1):
        pass
    elif (SLOT_62 == 2):
        SFX_1('bny309')
    elif (SLOT_62 == 3):
        SFX_1('bny310')
    elif (SLOT_62 == 4):
        SFX_1('bny311')
    elif (SLOT_62 == 5):
        SFX_1('bny312')
    elif (SLOT_62 == 6):
        SFX_1('bny313')
    elif (SLOT_62 == 7):
        SFX_1('bny314')
    elif (SLOT_62 == 8):
        SFX_1('bny315')
    elif (SLOT_62 == 9):
        SFX_1('bny316')
    elif (SLOT_62 == 10):
        SFX_1('bny317')
    elif (SLOT_62 == 11):
        SFX_1('bny318')
    elif (SLOT_62 == 12):
        SFX_1('bny319')
    elif (SLOT_62 == 13):
        SFX_1('bny320')
    elif (SLOT_62 == 14):
        SFX_1('bny321')
    elif (SLOT_62 == 15):
        SFX_1('bny322')
    elif (SLOT_62 == 16):
        SFX_1('bny323')
    elif (SLOT_62 == 17):
        SFX_1('bny324')
    elif (SLOT_62 == 18):
        SFX_1('bny325')
    elif (SLOT_62 == 19):
        SFX_1('bny326')
    elif (SLOT_62 == 20):
        SFX_1('bny327')
    elif (SLOT_62 >= 21):
        SFX_4('bny328')

@Subroutine
def OnFinalize():
    Unknown2038(0)
    Unknown48('19000000020000004700000016000000020000001e000000')
    if (not SLOT_71):
        SLOT_62 = 0

@Subroutine
def OnPreDraw():
    Unknown23030('4e595f4c696768740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def CheckLockReject():
    if (not Unknown23148('CmnActLockReject')):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if (not Unknown23148('CmnActOverDriveLoop')):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if (not Unknown23148('CmnActOverDriveEnd')):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if (not Unknown23148('CmnActAirOverDriveLoop')):
        SLOT_47 = 1
    else:
        SLOT_47 = 0
    if (not Unknown23148('CmnActAirOverDriveEnd')):
        SLOT_47 = 1
    else:
        SLOT_47 = 0

@Subroutine
def Func_DelayShot_Atk():
    Unknown23029(6, 4112, 0)

@Subroutine
def MatchInit2():
    pass

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        SLOT_31 = (SLOT_31 + 1)
        if (SLOT_31 >= 240):
            Unknown23047('0000000000000000')
        else:
            Unknown23047('0000000001000000')
    Unknown58('TRI_RambdasGravity', 2, 67)
    if SLOT_67:
        if SLOT_90:
            SLOT_31 = (SLOT_31 + 100000)

@State
def CmnActStand():
    label(0)
    sprite('ny000_00', 6)	# 1-6
    sprite('ny000_01', 6)	# 7-12
    sprite('ny000_02', 6)	# 13-18
    sprite('ny000_03', 6)	# 19-24
    sprite('ny000_04', 6)	# 25-30
    sprite('ny000_05', 6)	# 31-36
    sprite('ny000_06', 6)	# 37-42
    sprite('ny000_07', 6)	# 43-48
    sprite('ny000_08', 6)	# 49-54
    sprite('ny000_09', 6)	# 55-60
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('ny000_00', 1)	# 61-61
    SLOT_88 = 960
    SFX_1('bny000')
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ny003_02', 3)	# 1-3
    sprite('ny003_01', 3)	# 4-6
    sprite('ny003_00', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('ny010_00', 4)	# 1-4
    sprite('ny010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ny010_02', 6)	# 1-6
    sprite('ny010_03', 6)	# 7-12
    sprite('ny010_04', 6)	# 13-18
    sprite('ny010_05', 6)	# 19-24
    sprite('ny010_06', 6)	# 25-30
    sprite('ny010_07', 6)	# 31-36
    sprite('ny010_08', 6)	# 37-42
    sprite('ny010_09', 6)	# 43-48
    sprite('ny010_10', 6)	# 49-54
    sprite('ny010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ny013_02', 3)	# 1-3
    sprite('ny013_01', 3)	# 4-6
    sprite('ny013_00', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ny010_01', 4)	# 1-4
    sprite('ny010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ny023_00', 2)	# 1-2	 **attackbox here**
    SFX_3('nyse_03')
    sprite('ny023_01', 2)	# 3-4	 **attackbox here**

@State
def CmnActJumpUpper():
    label(0)
    sprite('ny020_00', 3)	# 1-3
    sprite('ny020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ny020_02', 3)	# 1-3
    sprite('ny020_03', 4)	# 4-7

@State
def CmnActJumpDown():
    sprite('ny020_04', 3)	# 1-3
    sprite('ny020_05', 3)	# 4-6
    label(0)
    sprite('ny020_06', 3)	# 7-9
    sprite('ny020_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ny024_00', 3)	# 1-3
    SFX_0('205_runjump_garden_0')
    sprite('ny024_01', 3)	# 4-6
    sprite('ny024_02', 3)	# 7-9
    sprite('ny024_03', 3)	# 10-12
    sprite('ny024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('ny024_00', 2)	# 1-2
    sprite('ny024_01', 2)	# 3-4
    sprite('ny024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('ny024_03', 3)	# 1-3
    sprite('ny024_04', 3)	# 4-6

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
    sprite('ny031_00', 7)	# 1-7
    label(0)
    sprite('ny031_01', 7)	# 8-14
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny031', -1)
    sprite('ny031_02', 7)	# 15-21
    GFX_1('nyef_ny031', -1)
    sprite('ny031_03', 7)	# 22-28
    GFX_1('nyef_ny031', -1)
    sprite('ny031_04', 7)	# 29-35
    GFX_1('nyef_ny031', -1)
    sprite('ny031_05', 7)	# 36-42
    GFX_1('nyef_ny031', -1)
    sprite('ny031_06', 7)	# 43-49
    GFX_1('nyef_ny031', -1)
    sprite('ny031_07', 7)	# 50-56
    GFX_1('nyef_ny031', -1)
    sprite('ny031_08', 7)	# 57-63
    GFX_1('nyef_ny031', -1)
    sprite('ny031_09', 7)	# 64-70
    GFX_1('nyef_ny031', -1)
    sprite('ny031_10', 7)	# 71-77
    GFX_1('nyef_ny031', -1)
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ny030_01', 4)	# 1-4
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny030', -1)
    sprite('ny032_00', 2)	# 5-6
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    label(0)
    sprite('ny032_01', 4)	# 7-10
    sprite('ny032_02', 4)	# 11-14
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 19-22
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ny032_05', 4)	# 1-4
    SFX_3('nyse_22')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_06', 4)	# 5-8

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22008(7)
        Unknown1084(1)
    sprite('ny033_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny033_00', 2)	# 3-4
    SFX_3('nyse_22')
    physicsXImpulse(-36000)
    sprite('ny033_01', 2)	# 5-6
    GFX_1('nyef_ny033', 106)
    sprite('ny033_02', 2)	# 7-8
    GFX_1('nyef_ny033', 106)
    sprite('ny033_03', 2)	# 9-10
    sprite('ny033_04', 1)	# 11-11
    Unknown1019(70)
    sprite('ny033_04', 1)	# 12-12
    Unknown1019(70)
    sprite('ny033_01', 1)	# 13-13
    Unknown1019(70)
    sprite('ny033_01', 1)	# 14-14
    Unknown1019(70)
    sprite('ny033_01', 1)	# 15-15
    Unknown1019(70)
    sprite('ny033_01', 1)	# 16-16
    Unknown1019(70)
    sprite('ny033_05', 1)	# 17-17
    Unknown1019(70)
    sprite('ny033_05', 1)	# 18-18
    Unknown1019(70)
    sprite('ny033_05', 1)	# 19-19
    Unknown1019(70)
    sprite('ny033_05', 1)	# 20-20
    Unknown1019(70)
    sprite('ny033_06', 1)	# 21-21
    Unknown1019(70)
    sprite('ny033_06', 1)	# 22-22
    Unknown1019(70)
    sprite('ny033_06', 1)	# 23-23
    Unknown1019(70)
    sprite('ny033_06', 1)	# 24-24
    Unknown1019(70)
    sprite('ny033_06', 1)	# 25-25
    Unknown1019(70)

@State
def CmnActBDashLanding():
    sprite('ny033_05', 4)	# 1-4
    sprite('ny033_06', 4)	# 5-8

@State
def CmnActAirFDash():
    sprite('ny035_00', 2)	# 1-2
    sprite('ny035_01', 3)	# 3-5
    sprite('ny035_02', 3)	# 6-8
    sprite('ny035_03', 3)	# 9-11
    sprite('ny035_04', 3)	# 12-14
    sprite('ny035_05', 3)	# 15-17	 **attackbox here**
    sprite('ny035_06', 3)	# 18-20	 **attackbox here**

@State
def CmnActAirBDash():
    sprite('ny036_00', 2)	# 1-2
    sprite('ny036_01', 2)	# 3-4
    sprite('ny036_02', 2)	# 5-6
    sprite('ny036_03', 2)	# 7-8
    sprite('ny036_04', 2)	# 9-10
    sprite('ny036_05', 3)	# 11-13
    sprite('ny036_06', 3)	# 14-16

@State
def CmnActHitStandLv1():
    sprite('ny050_00', 1)	# 1-1
    sprite('ny050_01', 7)	# 2-8
    sprite('ny050_00', 2)	# 9-10

@State
def CmnActHitStandLv2():
    sprite('ny050_01', 1)	# 1-1
    sprite('ny050_02', 7)	# 2-8
    sprite('ny050_01', 2)	# 9-10
    sprite('ny050_00', 2)	# 11-12

@State
def CmnActHitStandLv3():
    sprite('ny050_02', 1)	# 1-1
    sprite('ny050_03', 7)	# 2-8
    sprite('ny050_02', 2)	# 9-10
    sprite('ny050_01', 2)	# 11-12
    sprite('ny050_00', 2)	# 13-14

@State
def CmnActHitStandLv4():
    sprite('ny050_03', 1)	# 1-1
    sprite('ny050_04', 8)	# 2-9
    sprite('ny050_03', 2)	# 10-11
    sprite('ny050_02', 2)	# 12-13
    sprite('ny050_01', 2)	# 14-15
    sprite('ny050_00', 2)	# 16-17

@State
def CmnActHitStandLv5():
    sprite('ny050_04', 1)	# 1-1
    sprite('ny050_04', 8)	# 2-9
    sprite('ny050_04', 2)	# 10-11
    sprite('ny050_03', 2)	# 12-13
    sprite('ny050_02', 2)	# 14-15
    sprite('ny050_01', 2)	# 16-17
    sprite('ny050_00', 2)	# 18-19

@State
def CmnActHitStandLowLv1():
    sprite('ny052_00', 1)	# 1-1
    sprite('ny052_01', 7)	# 2-8
    sprite('ny052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv2():
    sprite('ny052_01', 1)	# 1-1
    sprite('ny052_02', 7)	# 2-8
    sprite('ny052_01', 2)	# 9-10
    sprite('ny052_00', 2)	# 11-12

@State
def CmnActHitStandLowLv3():
    sprite('ny052_02', 1)	# 1-1
    sprite('ny052_03', 7)	# 2-8
    sprite('ny052_02', 2)	# 9-10
    sprite('ny052_01', 2)	# 11-12
    sprite('ny052_00', 2)	# 13-14

@State
def CmnActHitStandLowLv4():
    sprite('ny052_03', 1)	# 1-1
    sprite('ny052_04', 8)	# 2-9
    sprite('ny052_03', 2)	# 10-11
    sprite('ny052_02', 2)	# 12-13
    sprite('ny052_01', 2)	# 14-15
    sprite('ny052_00', 2)	# 16-17

@State
def CmnActHitStandLowLv5():
    sprite('ny052_04', 1)	# 1-1
    sprite('ny052_04', 23)	# 2-24
    sprite('ny052_04', 2)	# 25-26
    sprite('ny052_03', 2)	# 27-28
    sprite('ny052_02', 2)	# 29-30
    sprite('ny052_01', 2)	# 31-32
    sprite('ny052_00', 2)	# 33-34

@State
def CmnActHitCrouchLv1():
    sprite('ny054_00', 1)	# 1-1
    sprite('ny054_01', 9)	# 2-10
    sprite('ny054_00', 2)	# 11-12

@State
def CmnActHitCrouchLv2():
    sprite('ny054_01', 1)	# 1-1
    sprite('ny054_02', 11)	# 2-12
    sprite('ny054_01', 2)	# 13-14
    sprite('ny054_00', 2)	# 15-16

@State
def CmnActHitCrouchLv3():
    sprite('ny054_02', 1)	# 1-1
    sprite('ny054_03', 12)	# 2-13
    sprite('ny054_02', 2)	# 14-15
    sprite('ny054_01', 2)	# 16-17
    sprite('ny054_00', 2)	# 18-19

@State
def CmnActHitCrouchLv4():
    sprite('ny054_03', 1)	# 1-1
    sprite('ny054_04', 12)	# 2-13
    sprite('ny054_03', 2)	# 14-15
    sprite('ny054_02', 2)	# 16-17
    sprite('ny054_01', 2)	# 18-19
    sprite('ny054_00', 2)	# 20-21

@State
def CmnActHitCrouchLv5():
    sprite('ny054_04', 1)	# 1-1
    sprite('ny054_04', 25)	# 2-26
    sprite('ny054_04', 2)	# 27-28
    sprite('ny054_03', 2)	# 29-30
    sprite('ny054_02', 2)	# 31-32
    sprite('ny054_01', 2)	# 33-34
    sprite('ny054_00', 2)	# 35-36

@State
def CmnActBDownUpper():
    sprite('ny060_00', 4)	# 1-4
    label(0)
    sprite('ny060_01', 4)	# 5-8
    sprite('ny060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ny062_03', 3)	# 1-3
    sprite('ny062_04', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('ny062_05', 3)	# 1-3
    sprite('ny062_06', 3)	# 4-6
    label(0)
    sprite('ny062_07', 3)	# 7-9
    sprite('ny062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ny060_07', 2)	# 1-2
    sprite('ny060_08', 2)	# 3-4

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
    sprite('ny063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ny063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ny063_02', 3)	# 1-3
    sprite('ny063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ny063_04', 3)	# 1-3
    sprite('ny063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('ny063_06', 2)	# 1-2
    sprite('ny063_07', 2)	# 3-4
    sprite('ny063_08', 3)	# 5-7
    sprite('ny063_09', 3)	# 8-10
    sprite('ny063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('ny063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ny064_00', 2)	# 1-2
    SFX_0('205_runjump_garden_0')
    SFX_3('nyse_03')
    sprite('ny064_01', 2)	# 3-4
    sprite('ny064_02', 2)	# 5-6
    sprite('ny064_03', 2)	# 7-8
    sprite('ny064_04', 2)	# 9-10
    sprite('ny064_05', 2)	# 11-12
    sprite('ny064_06', 2)	# 13-14
    sprite('ny064_07', 2)	# 15-16
    sprite('ny064_08', 2)	# 17-18
    sprite('ny064_09', 2)	# 19-20

@State
def CmnActVDownUpper():
    sprite('ny062_00', 3)	# 1-3
    label(0)
    sprite('ny062_01', 3)	# 4-6
    sprite('ny062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ny062_03', 3)	# 1-3
    sprite('ny062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('ny062_05', 3)	# 1-3
    sprite('ny062_06', 3)	# 4-6
    label(0)
    sprite('ny062_07', 3)	# 7-9
    sprite('ny062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ny062_09', 2)	# 1-2
    sprite('ny062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('ny072_00', 3)	# 1-3
    sprite('ny072_01', 3)	# 4-6
    sprite('ny072_02', 3)	# 7-9
    label(0)
    sprite('ny072_01', 3)	# 10-12
    sprite('ny072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ny074_00', 3)	# 1-3
    sprite('ny074_01', 3)	# 4-6
    sprite('ny074_02', 3)	# 7-9
    sprite('ny074_03', 3)	# 10-12
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
    sprite('ny071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ny073_00', 3)	# 1-3
    sprite('ny073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ny073_02', 3)	# 1-3
    label(0)
    sprite('ny073_03', 3)	# 4-6
    sprite('ny073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ny070_00', 2)	# 1-2
    sprite('ny070_01', 2)	# 3-4
    label(0)
    sprite('ny070_02', 4)	# 5-8
    sprite('ny070_03', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ny070_04', 4)	# 1-4
    sprite('ny070_05', 4)	# 5-8
    sprite('ny070_06', 4)	# 9-12
    sprite('ny070_07', 5)	# 13-17
    sprite('ny070_08', 5)	# 18-22
    sprite('ny070_09', 2)	# 23-24

@State
def CmnActUkemiStagger():
    sprite('ny070_10', 2)	# 1-2
    sprite('ny070_11', 2)	# 3-4
    sprite('ny070_12', 2)	# 5-6
    sprite('ny070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ny113_00', 3)	# 1-3
    sprite('ny113_01', 3)	# 4-6
    sprite('ny113_02', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('ny113_00', 3)	# 1-3
    sprite('ny113_01', 3)	# 4-6
    sprite('ny113_02', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('ny113_00', 3)	# 1-3
    sprite('ny113_01', 3)	# 4-6
    sprite('ny113_02', 9)	# 7-15

@State
def CmnActUkemiLandF():
    sprite('ny112_00', 2)	# 1-2
    sprite('ny112_01', 2)	# 3-4
    sprite('ny112_02', 2)	# 5-6
    sprite('ny112_03', 2)	# 7-8
    sprite('ny112_04', 2)	# 9-10
    sprite('ny112_05', 2)	# 11-12
    sprite('ny112_06', 2)	# 13-14
    sprite('ny112_07', 2)	# 15-16
    sprite('ny112_08', 2)	# 17-18

@State
def CmnActUkemiLandB():
    sprite('ny112_00', 2)	# 1-2
    sprite('ny112_01', 2)	# 3-4
    sprite('ny112_02', 2)	# 5-6
    sprite('ny112_03', 2)	# 7-8
    sprite('ny112_04', 2)	# 9-10
    sprite('ny112_05', 2)	# 11-12
    sprite('ny112_06', 2)	# 13-14
    sprite('ny112_07', 2)	# 15-16
    sprite('ny112_08', 2)	# 17-18

@State
def CmnActUkemiLandN():
    sprite('ny112_00', 2)	# 1-2
    sprite('ny112_01', 2)	# 3-4
    sprite('ny112_02', 2)	# 5-6
    sprite('ny112_03', 2)	# 7-8
    sprite('ny112_04', 2)	# 9-10
    sprite('ny112_05', 2)	# 11-12
    sprite('ny112_06', 2)	# 13-14
    sprite('ny112_07', 2)	# 15-16
    sprite('ny112_08', 2)	# 17-18

@State
def CmnActUkemiLandNLanding():
    sprite('ny024_00', 3)	# 1-3
    sprite('ny024_01', 3)	# 4-6
    sprite('ny024_02', 3)	# 7-9
    sprite('ny024_03', 3)	# 10-12
    sprite('ny024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('ny040_00', 3)	# 1-3
    sprite('ny040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ny040_02', 2)	# 1-2
    sprite('ny040_03', 2)	# 3-4
    sprite('ny040_04', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ny040_01', 3)	# 1-3
    sprite('ny040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ny040_05', 2)	# 1-2
    label(0)
    sprite('ny040_02', 2)	# 3-4
    sprite('ny040_03', 2)	# 5-6
    sprite('ny040_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ny040_01', 3)	# 1-3
    sprite('ny040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ny041_00', 3)	# 1-3
    sprite('ny041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ny041_02', 2)	# 1-2
    sprite('ny041_03', 2)	# 3-4
    sprite('ny041_04', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ny041_01', 3)	# 1-3
    sprite('ny041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ny041_05', 2)	# 1-2
    label(0)
    sprite('ny041_02', 2)	# 3-4
    sprite('ny041_03', 2)	# 5-6
    sprite('ny041_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ny041_01', 3)	# 1-3
    sprite('ny041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ny043_00', 3)	# 1-3	 **attackbox here**
    sprite('ny043_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ny043_02', 2)	# 1-2	 **attackbox here**
    sprite('ny043_03', 2)	# 3-4	 **attackbox here**
    sprite('ny043_04', 2)	# 5-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ny043_01', 3)	# 1-3	 **attackbox here**
    sprite('ny043_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ny043_05', 2)	# 1-2	 **attackbox here**
    label(0)
    sprite('ny043_02', 2)	# 3-4	 **attackbox here**
    sprite('ny043_03', 2)	# 5-6	 **attackbox here**
    sprite('ny043_04', 2)	# 7-8	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ny043_01', 3)	# 1-3	 **attackbox here**
    sprite('ny043_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirGuardPre():
    sprite('ny045_00', 3)	# 1-3
    sprite('ny045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ny045_02', 2)	# 1-2
    sprite('ny045_03', 2)	# 3-4
    sprite('ny045_04', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ny045_01', 3)	# 1-3
    sprite('ny045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ny045_05', 2)	# 1-2
    label(0)
    sprite('ny045_02', 2)	# 3-4
    sprite('ny045_03', 2)	# 5-6
    sprite('ny045_04', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ny045_01', 3)	# 1-3
    sprite('ny045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ny090_00', 2)	# 1-2
    sprite('ny090_01', 2)	# 3-4
    sprite('ny090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ny090_03', 6)	# 6-11
    sprite('ny090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('ny091_00', 2)	# 1-2
    sprite('ny091_01', 2)	# 3-4
    sprite('ny091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ny091_03', 6)	# 6-11
    sprite('ny091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('ny092_00', 2)	# 1-2
    sprite('ny092_01', 2)	# 3-4
    sprite('ny092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ny092_03', 6)	# 6-11
    sprite('ny092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('ny025_00', 4)	# 1-4
    sprite('ny025_01', 4)	# 5-8
    sprite('ny025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('ny040_02', 1)	# 1-1
    sprite('ny040_01', 3)	# 2-4
    sprite('ny040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('ny312_00', 2)	# 1-2
    sprite('ny312_01', 2)	# 3-4
    sprite('ny312_02', 2)	# 5-6
    sprite('ny312_03', 8)	# 7-14	 **attackbox here**
    sprite('ny312_04', 4)	# 15-18
    sprite('ny312_05', 3)	# 19-21
    sprite('ny312_06', 2)	# 22-23
    sprite('ny312_07', 3)	# 24-26
    sprite('ny312_08', 3)	# 27-29

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
    sprite('ny322_03', 8)	# 7-14	 **attackbox here**
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
    sprite('ny077_00', 2)	# 1-2
    sprite('ny077_01', 2)	# 3-4
    sprite('ny077_00ex00', 2)	# 5-6
    sprite('ny077_01ex00', 2)	# 7-8
    sprite('ny077_00ex01', 2)	# 9-10
    sprite('ny077_01ex01', 2)	# 11-12
    sprite('ny077_00ex02', 2)	# 13-14
    sprite('ny077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ny077_02', 4)	# 1-4
    label(0)
    sprite('ny077_03', 3)	# 5-7
    sprite('ny077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ny077_05', 5)	# 1-5
    sprite('ny077_06', 4)	# 6-9

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
    sprite('ny333_00', 3)	# 1-3
    sprite('ny333_01', 3)	# 4-6
    sprite('ny333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ny333_03', 32767)	# 10-32776
    GFX_0('EMB_NY_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ny333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ny333_05', 3)	# 4-6
    sprite('ny333_06', 3)	# 7-9
    sprite('ny333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ny333_08', 4)	# 1-4
    sprite('ny333_09', 4)	# 5-8
    sprite('ny333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('ny333_11', 3)	# 1-3
    sprite('ny333_12', 3)	# 4-6
    sprite('ny333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ny333_03', 32767)	# 10-32776
    GFX_0('EMB_NY_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ny333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ny333_05', 3)	# 4-6
    sprite('ny333_06', 3)	# 7-9
    sprite('ny333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ny333_13', 4)	# 1-4
    sprite('ny333_14', 4)	# 5-8
    sprite('ny333_15', 4)	# 9-12
    sprite('ny020_04', 3)	# 13-15
    sprite('ny020_05', 3)	# 16-18
    label(0)
    sprite('ny020_06', 3)	# 19-21
    sprite('ny020_07', 3)	# 22-24
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ny333_00', 3)	# 1-3
    sprite('ny333_01', 3)	# 4-6
    sprite('ny333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ny333_03', 32767)	# 10-32776
    GFX_0('EMB_NY_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ny333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ny333_05', 3)	# 4-6
    sprite('ny333_06', 3)	# 7-9
    sprite('ny333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ny333_08', 4)	# 1-4
    sprite('ny333_09', 4)	# 5-8
    sprite('ny333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('ny333_11', 3)	# 1-3
    sprite('ny333_12', 3)	# 4-6
    sprite('ny333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('ny333_03', 32767)	# 10-32776
    GFX_0('EMB_NY_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ny333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('ny333_05', 3)	# 4-6
    sprite('ny333_06', 3)	# 7-9
    sprite('ny333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ny333_13', 4)	# 1-4
    sprite('ny333_14', 4)	# 5-8
    sprite('ny333_15', 4)	# 9-12
    sprite('ny020_04', 3)	# 13-15
    sprite('ny020_05', 3)	# 16-18
    label(0)
    sprite('ny020_06', 3)	# 19-21
    sprite('ny020_07', 3)	# 22-24
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        pass
    sprite('ny331_00', 2)	# 1-2
    sprite('ny331_01', 2)	# 3-4
    sprite('ny331_02', 2)	# 5-6
    sprite('ny331_03', 32767)	# 7-32773
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ny331_04', 2)	# 1-2
    label(0)
    sprite('ny331_05', 3)	# 3-5
    sprite('ny331_06', 3)	# 6-8
    sprite('ny331_07', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ny331_08', 2)	# 1-2
    sprite('ny331_09', 2)	# 3-4
    sprite('ny331_10', 2)	# 5-6

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        pass
    sprite('ny331_00', 2)	# 1-2
    sprite('ny331_01', 2)	# 3-4
    sprite('ny331_02', 2)	# 5-6
    sprite('ny331_03', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ny331_04', 2)	# 1-2
    label(0)
    sprite('ny331_05', 3)	# 3-5
    sprite('ny331_06', 3)	# 6-8
    sprite('ny331_07', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ny331_08', 2)	# 1-2
    sprite('ny331_09', 2)	# 3-4
    sprite('ny331_10', 2)	# 5-6
    sprite('ny020_04', 3)	# 7-9
    sprite('ny020_05', 3)	# 10-12
    label(0)
    sprite('ny020_06', 4)	# 13-16
    sprite('ny020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            Unknown2034(0)
            if Unknown30042(25):
                Unknown2034(1)
            if (SLOT_18 == 5):
                Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
                SFX_0('301_overdrive_end')
            if (SLOT_18 == 53):
                sendToLabel(1)
    sprite('ny615_00', 3)	# 1-3	 **attackbox here**
    sprite('ny615_01', 3)	# 4-6	 **attackbox here**
    sprite('ny615_02', 3)	# 7-9	 **attackbox here**
    sprite('ny615_03', 5)	# 10-14	 **attackbox here**
    sprite('ny615_04', 3)	# 15-17	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 3)	# 18-20	 **attackbox here**
    sprite('ny615_06', 3)	# 21-23	 **attackbox here**
    sprite('ny615_07', 3)	# 24-26	 **attackbox here**
    sprite('ny615_08', 3)	# 27-29	 **attackbox here**
    label(0)
    sprite('ny615_09', 4)	# 30-33	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 4)	# 34-37	 **attackbox here**
    sprite('ny615_11', 4)	# 38-41	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('ny615_07', 3)	# 42-44	 **attackbox here**
    sprite('ny615_05', 3)	# 45-47	 **attackbox here**
    sprite('ny615_00', 3)	# 48-50	 **attackbox here**

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown1017()
        Unknown1022()
        Unknown1037()
        Unknown1084(1)

        def upon_3():
            Unknown2034(0)
            if Unknown30042(25):
                Unknown2034(1)
            if (SLOT_18 == 5):
                Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
                SFX_0('301_overdrive_end')
            if (SLOT_18 == 59):
                Unknown1018()
                Unknown1023()
                Unknown1038()
                Unknown1019(40)
                YAccel(40)
            if (SLOT_18 == 72):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('ny045_00', 4)	# 1-4
    sprite('ny045_01', 4)	# 5-8
    label(0)
    sprite('ny045_02', 4)	# 9-12
    sprite('ny045_03', 4)	# 13-16
    sprite('ny045_04', 4)	# 17-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny045_01', 4)	# 21-24
    sprite('ny045_00', 4)	# 25-28

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('null', 12)	# 1-12
    label(0)
    sprite('null', 1)	# 13-13
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    Unknown1007(100000)
    sprite('ny035_05', 2)	# 14-15	 **attackbox here**
    physicsXImpulse(100000)
    physicsYImpulse(-6666)
    sprite('ny035_00', 2)	# 16-17
    sprite('ny035_01', 2)	# 18-19
    sprite('ny035_02', 2)	# 20-21
    sprite('ny035_01', 2)	# 22-23
    sprite('ny035_02', 2)	# 24-25
    sprite('ny035_01', 2)	# 26-27
    sprite('ny254_05', 2)	# 28-29
    Unknown1043()
    Unknown2017(1)
    Unknown2053(1)
    sprite('ny254_06', 2)	# 30-31
    SFX_0('006_swing_blade_1')
    physicsXImpulse(-1000)
    physicsYImpulse(15000)
    setGravity(1700)
    sprite('ny254_07', 2)	# 32-33
    physicsXImpulse(-2000)
    StartMultihit()
    sprite('ny254_08', 2)	# 34-35	 **attackbox here**
    physicsXImpulse(-4000)
    StartMultihit()
    sprite('ny254_09ex00', 3)	# 36-38	 **attackbox here**
    physicsXImpulse(-15000)
    sprite('ny254_10', 3)	# 39-41	 **attackbox here**
    sendToLabelUpon(2, 9)
    Unknown1019(80)
    sprite('ny254_11', 3)	# 42-44	 **attackbox here**
    Unknown1019(80)
    sprite('ny254_13', 3)	# 45-47
    Unknown1019(80)
    sprite('ny254_14', 3)	# 48-50
    Unknown1019(80)
    sprite('ny321_02', 4)	# 51-54
    Unknown1019(80)
    sprite('ny321_03', 4)	# 55-58
    label(1)
    sprite('ny020_06', 3)	# 59-61
    sprite('ny020_07', 3)	# 62-64
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ny024_01', 3)	# 65-67
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ny024_02', 3)	# 68-70
    sprite('ny024_03', 2)	# 71-72
    sprite('ny024_04', 2)	# 73-74

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ny033_01', 2)	# 1-2
    physicsYImpulse(0)
    setGravity(0)
    GFX_1('nyef_ny033', 106)
    sprite('ny033_02', 2)	# 3-4
    GFX_1('nyef_ny033', 106)
    sprite('ny033_03', 2)	# 5-6
    sprite('ny033_04', 2)	# 7-8
    sprite('ny033_01', 2)	# 9-10
    sprite('ny033_02', 2)	# 11-12
    sprite('ny033_03', 2)	# 13-14
    sprite('ny033_04', 2)	# 15-16
    sprite('ny033_01', 40)	# 17-56

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
        Unknown2034(0)
        Unknown2017(0)
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 2)	# 41-42	 **attackbox here**
    sprite('ny300_05', 5)	# 43-47	 **attackbox here**
    sprite('ny300_06', 5)	# 48-52	 **attackbox here**
    sprite('ny300_07', 5)	# 53-57	 **attackbox here**
    sprite('ny300_08', 5)	# 58-62	 **attackbox here**
    sprite('ny300_09', 8)	# 63-70	 **attackbox here**
    sprite('ny300_10', 5)	# 71-75	 **attackbox here**
    sprite('ny300_11', 5)	# 76-80	 **attackbox here**

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 2)	# 41-42	 **attackbox here**
    sprite('ny300_05', 5)	# 43-47	 **attackbox here**
    sprite('ny300_06', 5)	# 48-52	 **attackbox here**
    sprite('ny300_07', 5)	# 53-57	 **attackbox here**
    sprite('ny300_08', 5)	# 58-62	 **attackbox here**
    label(1)
    sprite('ny300_09', 10)	# 63-72	 **attackbox here**
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ny300_10', 6)	# 73-78	 **attackbox here**
    sprite('ny300_11', 6)	# 79-84	 **attackbox here**

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
    sprite('null', 1)	# 121-121
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    Unknown1007(100000)
    sprite('ny035_05', 2)	# 122-123	 **attackbox here**
    physicsXImpulse(75000)
    physicsYImpulse(-5000)
    sprite('ny035_00', 2)	# 124-125
    sprite('ny035_01', 2)	# 126-127
    sprite('ny035_02', 2)	# 128-129
    sprite('ny035_01', 2)	# 130-131
    sprite('ny035_02', 2)	# 132-133
    sprite('ny035_01', 2)	# 134-135
    sprite('ny035_02', 2)	# 136-137
    sprite('ny035_01', 2)	# 138-139
    sprite('ny254_05', 2)	# 140-141
    Unknown1043()
    Unknown2017(1)
    Unknown2053(1)
    sprite('ny254_06', 2)	# 142-143
    SFX_0('006_swing_blade_1')
    physicsXImpulse(-1000)
    physicsYImpulse(15000)
    setGravity(1200)
    sprite('ny254_07', 2)	# 144-145
    physicsXImpulse(-2000)
    StartMultihit()
    sprite('ny254_08', 2)	# 146-147	 **attackbox here**
    physicsXImpulse(-4000)
    StartMultihit()
    sprite('ny254_09ex00', 3)	# 148-150	 **attackbox here**
    physicsXImpulse(-15000)
    sprite('ny254_10', 3)	# 151-153	 **attackbox here**
    sendToLabelUpon(2, 9)
    Unknown1019(80)
    sprite('ny254_11', 3)	# 154-156	 **attackbox here**
    Unknown1019(80)
    sprite('ny254_13', 3)	# 157-159
    Unknown1019(80)
    sprite('ny254_14', 3)	# 160-162
    Unknown1019(80)
    sprite('ny321_02', 4)	# 163-166
    Unknown1019(80)
    sprite('ny321_03', 4)	# 167-170
    label(1)
    sprite('ny020_06', 3)	# 171-173
    sprite('ny020_07', 3)	# 174-176
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ny024_01', 3)	# 177-179
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ny024_02', 3)	# 180-182
    sprite('ny024_03', 3)	# 183-185
    sprite('ny024_04', 3)	# 186-188

@State
def CmnActChangeReturnAppealBurst():
    sprite('ny111_07', 50)	# 1-50
    sprite('ny111_08', 5)	# 51-55
    sprite('ny111_09', 5)	# 56-60
    sprite('ny111_10', 30)	# 61-90

@State
def CmnActChangePartnerQuickIn():
    sprite('ny032_03', 3)	# 1-3
    sprite('ny032_04', 5)	# 4-8
    sprite('ny032_05', 7)	# 9-15
    sprite('ny032_06', 7)	# 16-22
    sprite('ny033_00', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ny033_00', 1)	# 1-1
    sprite('ny033_01', 2)	# 2-3
    sprite('ny033_02', 2)	# 4-5
    sprite('ny033_02', 1)	# 6-6
    sprite('ny033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('ny033_01', 2)	# 10-11
    sprite('ny033_05', 4)	# 12-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny033_05', 3)	# 16-18
    sprite('ny033_06', 3)	# 19-21

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(99)
    label(0)
    sprite('ny020_06', 4)	# 1-4
    Unknown1019(95)
    sprite('ny020_07', 4)	# 5-8
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ny010_02', 2)	# 9-10
    sprite('keep', 100)	# 11-110

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
            Unknown12046(0)
    sprite('ny400_00', 3)	# 1-3
    sprite('ny400_00', 1)	# 4-4
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 5-8
    sprite('ny400_02', 3)	# 9-11
    Unknown12046(50)
    sprite('ny400_03', 5)	# 12-16
    Unknown7006('bny202_0', 100, 846818914, 828322352, 0, 0, 100, 846818914, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 17-21
    SLOT_51 = 1
    sprite('ny400_03', 10)	# 22-31
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 10)	# 32-41
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(2000, 0)
    sprite('ny400_03', 10)	# 42-51
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(4000, 0)
    sprite('ny400_03', 10)	# 52-61
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(8000, 0)
    sprite('ny400_04', 3)	# 62-64
    clearUponHandler(3)
    SLOT_51 = 0
    ScreenShake(16000, 0)
    sprite('ny400_05', 4)	# 65-68
    GFX_0('SummonDmc', -1)
    GFX_0('TripleSwordAssist', -1)
    sprite('ny400_06', 4)	# 69-72
    sprite('ny400_07', 4)	# 73-76
    sprite('ny400_08', 4)	# 77-80
    sprite('ny400_09', 4)	# 81-84
    sprite('ny400_10', 5)	# 85-89
    sprite('ny400_11', 5)	# 90-94
    Unknown12046(0)
    sprite('ny400_12', 5)	# 95-99

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AttackP2(85)
        GroundedHitstunAnimation(9)
        AirPushbackY(9000)
        YImpluseBeforeWallbounce(200)
        AirUntechableTime(75)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ny403_00', 2)	# 1-2
    Unknown1019(25)
    sprite('ny403_01', 2)	# 3-4
    Unknown1019(0)
    sprite('ny403_02', 2)	# 5-6
    sprite('ny403_03', 2)	# 7-8
    sprite('ny403_07', 2)	# 9-10
    Unknown7006('bny201_0', 100, 846818914, 828322096, 0, 0, 100, 846818914, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny403_08', 2)	# 11-12
    sprite('ny403_09', 3)	# 13-15	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    Unknown23029(5, 4034, 0)
    GFX_0('SummonSlowArea', -1)
    Unknown38(5, 1)
    Unknown23029(1, 4035, 0)
    GFX_0('NY_SlowHand', 0)
    sprite('ny403_09', 10)	# 16-25	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('ny403_10', 5)	# 26-30
    sprite('ny403_11', 6)	# 31-36
    sprite('ny403_12', 6)	# 37-42
    sprite('ny403_13', 6)	# 43-48
    sprite('ny403_14', 3)	# 49-51
    sprite('ny403_14', 3)	# 52-54

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ny440_00', 3)	# 1-3
    sprite('ny440_01', 3)	# 4-6
    Unknown7006('bny301_0', 100, 863596130, 811546931, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny440_02', 3)	# 7-9
    physicsXImpulse(-5000)
    sprite('ny440_03', 2)	# 10-11
    GFX_0('AssistD_Shot', -1)
    SFX_0('006_swing_blade_2')
    sprite('ny440_04', 2)	# 12-13
    sprite('ny440_05', 2)	# 14-15
    physicsXImpulse(-15000)
    sprite('ny440_06', 3)	# 16-18
    sprite('ny440_07', 3)	# 19-21
    sprite('ny440_08', 3)	# 22-24
    physicsXImpulse(-7500)
    sprite('ny440_09', 3)	# 25-27
    sprite('ny440_10', 3)	# 28-30
    sprite('ny440_11', 3)	# 31-33
    sprite('ny440_12', 3)	# 34-36
    Recovery()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ny024_03ex01', 6)	# 37-42
    sprite('ny024_04ex01', 3)	# 43-45

@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        if SLOT_162:
            SLOT_58 = 1
        Unknown30063(1)
        Unknown30039(24)
        Unknown30040(1)
        Unknown30019('0000000002000000')

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)	# 1-1
    Unknown2036(92, -1, 0)
    sprite('ny035_05ex01', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(5000)
    setGravity(0)
    physicsYImpulse(-200)
    SLOT_12 = SLOT_19
    teleportRelativeX(-245000)
    Unknown1019(4)
    sprite('ny035_00ex01', 6)	# 3-8
    Unknown3029(1)
    Unknown3070(1)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny035_01ex01', 2)	# 9-10
    sprite('ny035_02ex01', 3)	# 11-13
    SFX_0('000_airdash_0')
    sprite('ny035_03ex01', 3)	# 14-16
    GFX_1('nyef_ny032', 0)
    Unknown3032()
    Unknown3004(-25)
    sprite('ny035_04ex01', 3)	# 17-19
    GFX_1('nyef_ny032', 0)
    sprite('ny035_05ex01', 3)	# 20-22
    GFX_1('nyef_ny032', 0)
    sprite('ny033_04', 2)	# 23-24
    Unknown3004(0)
    Unknown3001(255)
    sprite('ny033_05', 2)	# 25-26
    label(0)
    sprite('ny033_06', 1)	# 27-27
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 28-37
    Unknown1084(1)
    Unknown30019('0000000001000000')
    if SLOT_58:
        enterState('UltimateLargeSwordDDDOD')
    else:
        enterState('UltimateLargeSwordDDD')

@State
def UltimateLargeSwordDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23027()
        setInvincible(1)
        Unknown30063(1)
    sprite('ny431_00', 4)	# 1-4
    sprite('ny431_01', 5)	# 5-9
    sprite('ny431_02', 5)	# 10-14
    GFX_0('SummonDmc', -1)
    sprite('ny431_03', 5)	# 15-19
    sprite('ny431_04', 5)	# 20-24
    SFX_3('nyse_26')
    Unknown7006('bny251_0', 100, 846818914, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny431_05', 30)	# 25-54
    GFX_0('DDBigSwordMasterSearch', -1)
    sprite('ny431_06', 2)	# 55-56
    sprite('ny431_07', 2)	# 57-58
    sprite('ny431_08', 2)	# 59-60
    sprite('ny431_09', 3)	# 61-63
    sprite('ny431_10', 3)	# 64-66
    sprite('ny431_11', 3)	# 67-69
    sprite('ny431_12', 3)	# 70-72
    sprite('ny431_09', 4)	# 73-76
    sprite('ny431_10', 4)	# 77-80
    setInvincible(0)
    sprite('ny431_11', 4)	# 81-84
    sprite('ny431_12', 4)	# 85-88
    sprite('ny431_09', 4)	# 89-92
    sprite('ny431_10', 4)	# 93-96
    sprite('ny431_11', 4)	# 97-100
    sprite('ny431_12', 4)	# 101-104
    sprite('ny431_09', 4)	# 105-108
    sprite('ny431_10', 4)	# 109-112
    sprite('ny431_11', 4)	# 113-116
    sprite('ny431_12', 4)	# 117-120
    sprite('ny431_13', 4)	# 121-124
    sprite('ny431_14', 4)	# 125-128
    sprite('ny431_15', 4)	# 129-132
    sprite('ny431_16', 4)	# 133-136

@State
def UltimateLargeSwordDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23027()
        setInvincible(1)
        Unknown30063(1)
    sprite('keep', 2)	# 1-2
    sprite('ny431_00', 5)	# 3-7
    sprite('ny431_01', 6)	# 8-13
    sprite('ny431_02', 6)	# 14-19
    GFX_0('SummonDmc', -1)
    sprite('ny431_03', 5)	# 20-24
    sprite('ny431_04', 5)	# 25-29
    SFX_3('nyse_26')
    GFX_0('DDBigSwordODMasterSearch', -1)
    sprite('ny431_05', 30)	# 30-59
    Unknown7006('bny251_0', 100, 846818914, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny431_06', 2)	# 60-61
    sprite('ny431_07', 2)	# 62-63
    sprite('ny431_08', 2)	# 64-65
    sprite('ny431_09', 3)	# 66-68
    sprite('ny431_10', 3)	# 69-71
    setInvincible(0)
    sprite('ny431_11', 3)	# 72-74
    sprite('ny431_12', 3)	# 75-77
    sprite('ny431_09', 4)	# 78-81
    sprite('ny431_10', 4)	# 82-85
    sprite('ny431_11', 4)	# 86-89
    sprite('ny431_12', 4)	# 90-93
    sprite('ny431_09', 4)	# 94-97
    sprite('ny431_10', 4)	# 98-101
    sprite('ny431_11', 4)	# 102-105
    sprite('ny431_12', 4)	# 106-109
    sprite('ny431_09', 4)	# 110-113
    sprite('ny431_10', 4)	# 114-117
    sprite('ny431_11', 4)	# 118-121
    sprite('ny431_12', 4)	# 122-125
    sprite('ny431_09', 4)	# 126-129
    sprite('ny431_10', 4)	# 130-133
    sprite('ny431_11', 4)	# 134-137
    sprite('ny431_12', 4)	# 138-141
    sprite('ny431_09', 4)	# 142-145
    sprite('ny431_10', 4)	# 146-149
    sprite('ny431_11', 4)	# 150-153
    sprite('ny431_12', 4)	# 154-157
    sprite('ny431_13', 4)	# 158-161
    sprite('ny431_14', 4)	# 162-165
    sprite('ny431_15', 4)	# 166-169
    sprite('ny431_16', 4)	# 170-173

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackY(20000)
        AirUntechableTime(26)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ny210_00', 2)	# 1-2
    sprite('ny210_01', 2)	# 3-4
    sprite('ny210_02', 2)	# 5-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown7006('bny106_0', 100, 830041698, 828323376, 0, 0, 100, 830041698, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny210_03', 4)	# 7-10
    sprite('ny210_04', 1)	# 11-11	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    sprite('ny210_04', 5)	# 12-16	 **attackbox here**
    setInvincible(0)
    sprite('ny210_05', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('ny210_06', 4)	# 20-23
    sprite('ny210_07', 4)	# 24-27
    sprite('ny210_08', 3)	# 28-30
    sprite('ny210_00', 3)	# 31-33

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(15300)
        AirPushbackY(18000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ny211_00', 2)	# 1-2
    sprite('ny211_01', 2)	# 3-4
    sprite('ny211_02', 2)	# 5-6
    sprite('ny211_03', 2)	# 7-8
    Unknown7009(0)
    SFX_0('010_swing_sword_1')
    sprite('ny211_04', 2)	# 9-10	 **attackbox here**
    sprite('ny211_05', 3)	# 11-13	 **attackbox here**
    sprite('ny211_04', 3)	# 14-16	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ny211_03', 3)	# 17-19
    sprite('ny211_02', 3)	# 20-22
    sprite('ny211_01', 3)	# 23-25
    sprite('ny211_00', 3)	# 26-28

@State
def NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(16500)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('SpecialDashF')
        HitOrBlockCancel('SpecialDashB')

        def upon_STATE_END():
            Unknown23029(4, 2029, 0)

        def upon_43():
            if (SLOT_48 == 2030):
                Unknown2038(1)
    sprite('ny202_00', 3)	# 1-3
    GFX_0('Funnel5BMain', -1)
    Unknown38(4, 1)
    sprite('ny202_01', 2)	# 4-5
    sprite('ny202_02', 2)	# 6-7
    Unknown7009(3)
    sprite('ny202_03', 1)	# 8-8
    sprite('ny202_04', 1)	# 9-9
    sprite('ny202_05', 1)	# 10-10
    sprite('ny202_06', 1)	# 11-11
    Unknown23029(4, 2022, 0)
    sprite('ny202_07', 2)	# 12-13
    sprite('ny202_06', 1)	# 14-14
    sprite('ny202_06', 1)	# 15-15
    Unknown23029(4, 2023, 0)
    sprite('ny202_07', 2)	# 16-17
    sprite('ny202_06', 1)	# 18-18
    sprite('ny202_06', 1)	# 19-19
    Unknown23029(4, 2024, 0)
    sprite('ny202_07', 2)	# 20-21
    sprite('ny202_06', 1)	# 22-22
    Unknown14070('NmlAtk5A_3rd')
    sprite('ny202_06', 1)	# 23-23
    Unknown23029(4, 2025, 0)
    sprite('ny202_07', 2)	# 24-25
    sprite('ny202_06', 1)	# 26-26
    sprite('ny202_06', 1)	# 27-27
    Unknown23029(4, 2026, 0)
    sprite('ny202_07', 2)	# 28-29
    sprite('ny202_06', 1)	# 30-30
    sprite('ny202_06', 1)	# 31-31
    Unknown23029(4, 2027, 0)
    sprite('ny202_07', 2)	# 32-33
    sprite('ny202_06', 1)	# 34-34
    sprite('ny202_06', 3)	# 35-37
    Unknown23029(4, 2028, 0)
    sprite('ny202_07', 3)	# 38-40
    sprite('ny202_06', 7)	# 41-47
    if SLOT_2:
        Unknown14072('NmlAtk5A_3rd')
    sprite('ny202_06', 8)	# 48-55
    Recovery()
    Unknown2063()
    sprite('ny202_08', 4)	# 56-59
    Unknown14074('NmlAtk5A_3rd')
    GFX_0('FunnelRevive', -1)
    sprite('ny202_09', 4)	# 60-63
    sprite('ny202_10', 4)	# 64-67
    sprite('ny202_11', 4)	# 68-71

@State
def NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(300)
        Unknown11092(1)
        AirHitstunAnimation(9)
        AirPushbackX(25000)
        AirPushbackY(18000)
        Unknown9154(24)
        AirUntechableTime(36)
        Hitstop(2)
        Unknown9016(1)
        Unknown11057(700)
        Unknown23027()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('SpecialDashF')
        HitOrBlockCancel('SpecialDashB')

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
    sprite('ny213_00', 2)	# 1-2
    sprite('ny213_01', 2)	# 3-4
    sprite('ny213_02', 2)	# 5-6
    sprite('ny213_03', 3)	# 7-9
    sprite('ny213_04', 3)	# 10-12
    sprite('ny213_05', 2)	# 13-14
    SFX_0('006_swing_blade_1')
    sprite('ny213_06', 2)	# 15-16
    Unknown7007('626e793130385f30000000000000000064000000626e793130385f31000000000000000064000000626e793130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ny213_07', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    GFX_0('5AAAZanzo', -1)
    sprite('ny213_07', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('ny213_08', 1)	# 19-19	 **attackbox here**
    RefreshMultihit()
    sprite('ny213_08', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    Unknown14070('NmlAtk5A_4th')
    sprite('ny213_09', 1)	# 21-21	 **attackbox here**
    SFX_0('011_spin_0')
    RefreshMultihit()
    sprite('ny213_09', 1)	# 22-22	 **attackbox here**
    RefreshMultihit()
    sprite('ny213_10', 1)	# 23-23	 **attackbox here**
    RefreshMultihit()
    sprite('ny213_10', 1)	# 24-24	 **attackbox here**
    RefreshMultihit()
    if SLOT_2:
        Unknown14072('NmlAtk5A_4th')
    sprite('ny213_11', 6)	# 25-30	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ny213_12', 2)	# 31-32
    sprite('ny213_12', 4)	# 33-36
    Unknown14074('NmlAtk5A_4th')
    sprite('ny213_13', 6)	# 37-42
    sprite('ny213_14', 6)	# 43-48

@State
def NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        JumpCancel_(0)
    sprite('ny411_00', 1)	# 1-1
    sprite('ny411_01', 1)	# 2-2
    sprite('ny411_02', 1)	# 3-3
    sprite('ny411_03', 2)	# 4-5
    GFX_0('SummonDmc', -1)
    sprite('ny411_04', 2)	# 6-7
    Unknown7006('bny207_0', 100, 846818914, 828323632, 0, 0, 100, 846818914, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny411_05', 2)	# 8-9
    sprite('ny411_06', 2)	# 10-11
    sprite('ny411_07', 2)	# 12-13
    GFX_0('DelayShotSummon', -1)
    Unknown38(6, 1)
    sprite('ny411_07', 1)	# 14-14
    Unknown23029(6, 4114, 0)
    sprite('ny411_08', 3)	# 15-17
    sprite('ny411_09', 3)	# 18-20
    sprite('ny411_10', 3)	# 21-23
    sprite('ny411_08', 3)	# 24-26
    sprite('ny411_09', 3)	# 27-29
    sprite('ny411_10', 3)	# 30-32
    sprite('ny411_08', 3)	# 33-35
    sprite('ny411_09', 3)	# 36-38
    sprite('ny411_11', 3)	# 39-41
    Recovery()
    sprite('ny203_13', 3)	# 42-44
    sprite('ny203_14', 3)	# 45-47
    sprite('ny203_15', 3)	# 48-50
    sprite('ny203_16', 3)	# 51-53
    sprite('ny203_17', 3)	# 54-56

@Subroutine
def SS_CancelInitNoRA():
    WhiffCancel('SpecialDashF')
    WhiffCancel('SpecialDashB')
    WhiffCancel('SpecialDashAirF')
    WhiffCancel('SpecialDashAirB')

    def upon_43():
        if (SLOT_48 == 2044):
            SLOT_51 = 1
            WhiffCancelEnable(1)
            Unknown2063()
        if (SLOT_48 == 2031):
            if SLOT_57:
                HitOrBlockCancel('NmlAtk5B_5th')
                HitOrBlockCancel('NmlAtkAIR5B_5th')

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B_2nd')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny203_00', 3)	# 1-3
    sprite('ny203_01', 3)	# 4-6
    sprite('ny203_02', 3)	# 7-9
    GFX_0('Sword5B', -1)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny203_03', 3)	# 10-12
    sprite('ny203_04', 5)	# 13-17
    sprite('ny203_04', 8)	# 18-25
    sprite('ny203_03', 4)	# 26-29
    sprite('ny203_02', 4)	# 30-33
    sprite('ny203_01', 4)	# 34-37
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_00', 4)	# 38-41

@State
def NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B_3rd')
        HitOrBlockCancel('NmlAtk5B_3rdEx')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny203_07', 2)	# 1-2
    sprite('ny203_08', 2)	# 3-4
    sprite('ny203_09', 3)	# 5-7
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2041, 0)
    GFX_0('SummonDmc', -1)
    sprite('ny203_10', 9)	# 8-16
    sprite('ny203_10', 2)	# 17-18
    sprite('ny203_11', 4)	# 19-22
    sprite('ny203_12', 4)	# 23-26
    sprite('ny203_13', 4)	# 27-30
    sprite('ny203_14', 4)	# 31-34
    sprite('ny203_15', 4)	# 35-38
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)	# 39-42
    sprite('ny203_17', 4)	# 43-46

@State
def NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B_4th')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny215_00', 2)	# 1-2
    sprite('ny215_01', 2)	# 3-4
    sprite('ny215_01', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny215_02', 1)	# 7-7
    sprite('ny215_03', 2)	# 8-9
    sprite('ny215_03', 2)	# 10-11
    sprite('ny215_04', 3)	# 12-14
    sprite('ny215_05', 5)	# 15-19
    sprite('ny215_05', 9)	# 20-28
    sprite('ny215_04', 4)	# 29-32
    sprite('ny215_03', 4)	# 33-36
    Recovery()
    sprite('ny215_02', 3)	# 37-39
    WhiffCancelEnable(0)
    sprite('ny215_01', 3)	# 40-42
    sprite('ny215_00', 4)	# 43-46

@State
def NmlAtk5B_4th():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny215_08', 2)	# 1-2
    sprite('ny215_09', 2)	# 3-4
    sprite('ny215_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny215_11', 2)	# 7-8
    sprite('ny215_12', 8)	# 9-16
    sprite('ny215_12', 4)	# 17-20
    sprite('ny215_13', 4)	# 21-24
    sprite('ny215_14', 4)	# 25-28
    sprite('ny203_13', 4)	# 29-32
    sprite('ny203_14', 4)	# 33-36
    sprite('ny203_15', 4)	# 37-40
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)	# 41-44
    sprite('ny203_17', 4)	# 45-48

@State
def NmlAtk5B_3rdEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B_4thEx')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny215_00', 2)	# 1-2
    sprite('ny215_01', 2)	# 3-4
    sprite('ny215_01', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny215_02', 1)	# 7-7
    sprite('ny215_03', 2)	# 8-9
    sprite('ny215_03', 2)	# 10-11
    sprite('ny215_04', 3)	# 12-14
    sprite('ny215_05', 5)	# 15-19
    sprite('ny215_05', 9)	# 20-28
    sprite('ny215_04', 4)	# 29-32
    sprite('ny215_03', 4)	# 33-36
    Recovery()
    sprite('ny215_02', 3)	# 37-39
    WhiffCancelEnable(0)
    sprite('ny215_01', 3)	# 40-42
    sprite('ny215_00', 4)	# 43-46

@State
def NmlAtk5B_4thEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny215_08', 2)	# 1-2
    sprite('ny215_09', 2)	# 3-4
    sprite('ny215_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny215_11', 2)	# 7-8
    sprite('ny215_12', 8)	# 9-16
    sprite('ny215_12', 4)	# 17-20
    sprite('ny215_13', 4)	# 21-24
    sprite('ny215_14', 4)	# 25-28
    sprite('ny203_13', 4)	# 29-32
    sprite('ny203_14', 4)	# 33-36
    sprite('ny203_15', 4)	# 37-40
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)	# 41-44
    sprite('ny203_17', 4)	# 45-48

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        HitLow(2)
        AttackP1(90)
        Unknown9016(1)
        Unknown11057(600)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ny231_00', 3)	# 1-3
    sprite('ny231_01', 3)	# 4-6
    sprite('ny231_02', 2)	# 7-8
    Unknown7009(0)
    SFX_0('006_swing_blade_0')
    sprite('ny231_03', 4)	# 9-12	 **attackbox here**
    GFX_1('nyef_ny030back', 0)
    GFX_1('nyef_ny030back', 1)
    GFX_1('nyef_ny030back', 2)
    GFX_1('nyef_ny030back', 3)
    GFX_1('nyef_ny030back', 4)
    sprite('ny231_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('ny231_05', 4)	# 17-20
    sprite('ny231_06', 4)	# 21-24

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk2B_2nd')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny233_00', 2)	# 1-2
    sprite('ny233_01', 2)	# 3-4
    sprite('ny233_02', 2)	# 5-6
    GFX_0('Sword2B', -1)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny233_03', 2)	# 7-8
    Unknown14070('CmnActCrushAttack')
    sprite('ny233_04', 2)	# 9-10
    sprite('ny233_05', 2)	# 11-12
    sprite('ny233_05', 14)	# 13-26
    SLOT_58 = 1
    sprite('ny233_06', 4)	# 27-30
    Unknown14074('CmnActCrushAttack')
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny233_07', 4)	# 31-34
    sprite('ny233_08', 4)	# 35-38

@State
def NmlAtk2B_2nd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_CrouchingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk2B_3rd')
        HitOrBlockCancel('NmlAtk2B_3rdEx')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny255_08ex01', 2)	# 1-2
    sprite('ny255_09ex01', 2)	# 3-4
    sprite('ny255_10ex01', 3)	# 5-7
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2041, 0)
    GFX_0('SummonDmc', -1)
    sprite('ny255_11ex01', 10)	# 8-17
    sprite('ny255_11ex01', 5)	# 18-22
    SLOT_58 = 1
    sprite('ny255_11ex01', 10)	# 23-32
    sprite('ny255_12ex01', 7)	# 33-39
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny255_13ex01', 7)	# 40-46

@State
def NmlAtk2B_3rd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk2B_4th')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny214_00', 2)	# 1-2
    sprite('ny214_01', 2)	# 3-4
    sprite('ny214_02', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny214_03', 2)	# 7-8
    sprite('ny214_04', 2)	# 9-10
    sprite('ny214_05', 8)	# 11-18
    sprite('ny214_05', 10)	# 19-28
    sprite('ny214_04', 3)	# 29-31
    sprite('ny214_03', 3)	# 32-34
    Recovery()
    sprite('ny214_02', 3)	# 35-37
    WhiffCancelEnable(0)
    sprite('ny214_01', 3)	# 38-40
    sprite('ny214_00', 3)	# 41-43

@State
def NmlAtk2B_4th():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny214_08', 2)	# 1-2
    sprite('ny214_09', 2)	# 3-4
    sprite('ny214_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    GFX_0('SummonDmc', -1)
    sprite('ny214_11', 1)	# 7-7
    sprite('ny214_11', 1)	# 8-8
    sprite('ny214_12', 8)	# 9-16
    sprite('ny214_12', 4)	# 17-20
    sprite('ny214_13', 4)	# 21-24
    sprite('ny214_14', 4)	# 25-28
    sprite('ny203_13', 4)	# 29-32
    sprite('ny203_14', 4)	# 33-36
    sprite('ny203_15', 4)	# 37-40
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)	# 41-44
    sprite('ny203_17', 4)	# 45-48

@State
def NmlAtk2B_3rdEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk2B_4thEx')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny214_00', 2)	# 1-2
    sprite('ny214_01', 2)	# 3-4
    sprite('ny214_02', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    GFX_0('SummonDmc', -1)
    callSubroutine('DriveVoice')
    sprite('ny214_03', 2)	# 7-8
    sprite('ny214_04', 2)	# 9-10
    sprite('ny214_05', 8)	# 11-18
    sprite('ny214_05', 10)	# 19-28
    sprite('ny214_04', 3)	# 29-31
    sprite('ny214_03', 3)	# 32-34
    Recovery()
    sprite('ny214_02', 3)	# 35-37
    WhiffCancelEnable(0)
    sprite('ny214_01', 3)	# 38-40
    sprite('ny214_00', 3)	# 41-43

@State
def NmlAtk2B_4thEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny214_08', 2)	# 1-2
    sprite('ny214_09', 2)	# 3-4
    sprite('ny214_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    GFX_0('SummonDmc', -1)
    sprite('ny214_11', 1)	# 7-7
    sprite('ny214_11', 1)	# 8-8
    sprite('ny214_12', 8)	# 9-16
    sprite('ny214_12', 4)	# 17-20
    sprite('ny214_13', 4)	# 21-24
    sprite('ny214_14', 4)	# 25-28
    sprite('ny203_13', 4)	# 29-32
    sprite('ny203_14', 4)	# 33-36
    sprite('ny203_15', 4)	# 37-40
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny203_16', 4)	# 41-44
    sprite('ny203_17', 4)	# 45-48

@State
def NmlAtk5B_5th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        JumpCancel_(0)
    sprite('ny411_00', 1)	# 1-1
    sprite('ny411_01', 1)	# 2-2
    sprite('ny411_02', 1)	# 3-3
    sprite('ny411_03', 1)	# 4-4
    GFX_0('SummonDmc', -1)
    sprite('ny411_04', 1)	# 5-5
    Unknown7006('bny207_0', 100, 846818914, 828323632, 0, 0, 100, 846818914, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny411_05', 1)	# 6-6
    sprite('ny411_06', 1)	# 7-7
    sprite('ny411_07', 1)	# 8-8
    GFX_0('DelayShotSummon', -1)
    Unknown38(6, 1)
    sprite('ny411_07', 1)	# 9-9
    Unknown23029(6, 4114, 0)
    sprite('ny411_08', 3)	# 10-12
    sprite('ny411_09', 3)	# 13-15
    sprite('ny411_10', 3)	# 16-18
    sprite('ny411_08', 3)	# 19-21
    sprite('ny411_09', 3)	# 22-24
    sprite('ny411_10', 3)	# 25-27
    sprite('ny411_08', 3)	# 28-30
    sprite('ny411_09', 3)	# 31-33
    sprite('ny411_11', 3)	# 34-36
    Recovery()
    sprite('ny203_13', 3)	# 37-39
    sprite('ny203_14', 3)	# 40-42
    sprite('ny203_15', 3)	# 43-45
    sprite('ny203_16', 3)	# 46-48
    sprite('ny203_17', 3)	# 49-51

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(280)
        AttackP1(90)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(21000)
        AirUntechableTime(36)
        Hitstop(3)
        HitLow(2)
        Unknown9016(1)
        Unknown11057(700)
        Unknown23027()

        def upon_3():
            if SLOT_94:
                JumpCancel_(0)
                if (SLOT_18 >= 19):
                    JumpCancel_(1)
    sprite('ny234_00', 3)	# 1-3
    sprite('ny234_01', 3)	# 4-6
    sprite('ny234_02', 2)	# 7-8
    sprite('ny234_03', 2)	# 9-10
    SFX_0('006_swing_blade_1')
    Unknown7007('626e793130375f30000000000000000064000000626e793130375f31000000000000000064000000626e793130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ny234_04', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    GFX_0('2CZanzo', -1)
    sprite('ny234_04', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('ny234_05', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    sprite('ny234_05', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    HitLow(0)
    sprite('ny234_06', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_1')
    sprite('ny234_06', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('ny234_07', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('ny234_07', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('ny234_08', 5)	# 19-23
    Recovery()
    Unknown2063()
    sprite('ny234_09', 5)	# 24-28
    sprite('ny234_10', 6)	# 29-34
    sprite('ny234_11', 6)	# 35-40

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(380)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(12000)
        AirUntechableTime(20)
        Hitstop(2)
        Unknown11057(500)
        Unknown9016(1)
        Unknown23027()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            Unknown1021(2000)
    sprite('ny252_00', 3)	# 1-3
    sprite('ny252_01', 4)	# 4-7
    sprite('ny252_02', 3)	# 8-10
    SFX_0('006_swing_blade_1')
    Unknown7009(2)
    sprite('ny252_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_03', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_04', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_05', 2)	# 15-16	 **attackbox here**
    GFX_0('JBZanzo', 0)
    RefreshMultihit()
    SFX_0('006_swing_blade_1')
    sprite('ny252_06', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_07', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_08', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_09', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    sprite('ny252_10', 4)	# 25-28
    Recovery()
    Unknown2063()
    sprite('ny252_11', 5)	# 29-33
    sprite('ny252_12', 6)	# 34-39
    sprite('ny252_13', 10)	# 40-49

@State
def NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(300)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(10)
        AirPushbackX(8000)
        AirPushbackY(32000)
        AirUntechableTime(24)
        Hitstop(3)
        Unknown11057(500)
        Unknown9016(1)
        Unknown23027()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('ny254_00', 1)	# 1-1
    sprite('ny254_01', 1)	# 2-2
    sprite('ny254_02', 1)	# 3-3
    sprite('ny254_03', 1)	# 4-4
    sprite('ny254_04', 1)	# 5-5
    sprite('ny254_05', 1)	# 6-6
    sprite('ny254_06', 1)	# 7-7
    SFX_0('006_swing_blade_0')
    Unknown7009(4)
    sprite('ny254_07', 1)	# 8-8
    sprite('ny254_08', 1)	# 9-9	 **attackbox here**
    RefreshMultihit()
    GFX_0('J2BZanzo', 0)
    sprite('ny254_08', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('ny254_09', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    HitOverhead(0)
    sprite('ny254_09', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    SFX_0('006_swing_blade_0')
    sprite('ny254_10', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    sprite('ny254_10', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('ny254_11', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('ny254_11', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('ny254_12', 2)	# 17-18
    Recovery()
    Unknown2063()
    sprite('ny254_13', 2)	# 19-20
    sprite('ny254_14', 2)	# 21-22
    sprite('ny254_15', 2)	# 23-24
    sprite('ny254_16', 2)	# 25-26

@Subroutine
def PopSpeed():
    Unknown1018()
    Unknown1023()
    Unknown1050()
    Unknown1019(60)
    YAccel(80)
    Unknown1043()

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5B_2nd')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny256_00', 2)	# 1-2
    sprite('ny256_01', 2)	# 3-4
    sprite('ny256_02', 4)	# 5-8
    GFX_0('SwordJB', -1)
    GFX_0('AirSummonDmc', 0)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny256_03', 4)	# 9-12
    sprite('ny256_04', 16)	# 13-28
    sprite('ny256_05', 4)	# 29-32
    sprite('ny256_05', 6)	# 33-38
    callSubroutine('PopSpeed')
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_06', 6)	# 39-44
    sprite('ny256_06', 9)	# 45-53
    sprite('ny020_04', 6)	# 54-59

@State
def NmlAtkAIR5B_2nd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5B_3rdEx')
        HitOrBlockCancel('NmlAtkAIR5B_3rd')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny256_07', 2)	# 1-2
    sprite('ny256_08', 2)	# 3-4
    GFX_0('AirSummonDmc', 0)
    sprite('ny256_09', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2041, 0)
    sprite('ny256_10', 2)	# 7-8
    sprite('ny256_11', 15)	# 9-23
    sprite('ny256_12', 3)	# 24-26
    WhiffCancelEnable(0)
    sprite('ny256_12', 3)	# 27-29
    Recovery()
    sprite('ny256_13', 6)	# 30-35
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)	# 36-38

@State
def NmlAtkAIR5B_3rd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5B_4th')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny255_00', 2)	# 1-2
    sprite('ny255_01', 2)	# 3-4
    sprite('ny255_02', 4)	# 5-8
    Unknown2003(1)
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    GFX_0('AirSummonDmc', 0)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny255_03', 4)	# 9-12
    sprite('ny255_04', 4)	# 13-16
    sprite('ny255_05', 11)	# 17-27
    sprite('ny255_06', 4)	# 28-31
    sprite('ny255_06', 2)	# 32-33
    sprite('ny255_07', 2)	# 34-35
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny255_07', 4)	# 36-39
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)	# 40-43

@State
def NmlAtkAIR5B_4th():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny255_08', 2)	# 1-2
    GFX_0('AirSummonDmc', 0)
    sprite('ny255_09', 2)	# 3-4
    sprite('ny255_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    sprite('ny255_11', 10)	# 7-16
    sprite('ny255_12', 3)	# 17-19
    sprite('ny255_12', 3)	# 20-22
    sprite('ny255_13', 6)	# 23-28
    Recovery()
    WhiffCancelEnable(0)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)	# 29-31

@State
def NmlAtkAIR5B_5th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        JumpCancel_(0)
    sprite('ny256_00', 3)	# 1-3
    sprite('ny256_01', 3)	# 4-6
    GFX_0('AirSummonDmc', 0)
    sprite('ny256_02', 1)	# 7-7
    GFX_0('AirDelayShotSummon', -1)
    Unknown38(6, 1)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    Unknown7006('bny207_0', 100, 846818914, 828323632, 0, 0, 100, 846818914, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny256_02', 3)	# 8-10
    Unknown23029(6, 4114, 0)
    sprite('ny256_03', 4)	# 11-14
    sprite('ny256_04', 16)	# 15-30
    sprite('ny256_05', 8)	# 31-38
    sprite('ny256_06', 4)	# 39-42
    callSubroutine('PopSpeed')
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_06', 4)	# 43-46
    sprite('ny020_04', 4)	# 47-50

@State
def NmlAtkAIR5B_3rdEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5B_4thEx')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny255_00', 2)	# 1-2
    sprite('ny255_01', 2)	# 3-4
    sprite('ny255_02', 4)	# 5-8
    Unknown2003(1)
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    GFX_0('AirSummonDmc', 0)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny255_03', 4)	# 9-12
    sprite('ny255_04', 4)	# 13-16
    sprite('ny255_05', 11)	# 17-27
    sprite('ny255_06', 4)	# 28-31
    sprite('ny255_06', 2)	# 32-33
    Recovery()
    sprite('ny255_07', 2)	# 34-35
    WhiffCancelEnable(0)
    sprite('ny255_07', 4)	# 36-39
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)	# 40-43

@State
def NmlAtkAIR5B_4thEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny255_08', 2)	# 1-2
    GFX_0('AirSummonDmc', 0)
    sprite('ny255_09', 2)	# 3-4
    sprite('ny255_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    sprite('ny255_11', 10)	# 7-16
    sprite('ny255_12', 3)	# 17-19
    sprite('ny255_12', 3)	# 20-22
    sprite('ny255_13', 6)	# 23-28
    Recovery()
    WhiffCancelEnable(0)
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)	# 29-31

@State
def NmlAtkAIR2B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2B_2nd')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny255_00', 2)	# 1-2
    sprite('ny255_01', 2)	# 3-4
    sprite('ny255_02', 4)	# 5-8
    Unknown2003(1)
    GFX_0('SwordJ2B', -1)
    GFX_0('AirSummonDmc', 0)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny255_03', 4)	# 9-12
    sprite('ny255_04', 4)	# 13-16
    sprite('ny255_05', 16)	# 17-32
    sprite('ny255_06', 6)	# 33-38
    callSubroutine('PopSpeed')
    Recovery()
    sprite('ny255_07', 6)	# 39-44
    sprite('ny255_07', 9)	# 45-53
    sprite('ny020_04', 6)	# 54-59

@State
def NmlAtkAIR2B_2nd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR2B_3rd')
        HitOrBlockCancel('NmlAtkAIR2B_3rdEx')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny255_08', 2)	# 1-2
    GFX_0('AirSummonDmc', 0)
    sprite('ny255_09', 2)	# 3-4
    sprite('ny255_10', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2041, 0)
    sprite('ny255_11', 15)	# 7-21
    sprite('ny255_12', 3)	# 22-24
    sprite('ny255_12', 3)	# 25-27
    Recovery()
    WhiffCancelEnable(0)
    sprite('ny255_13', 6)	# 28-33
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)	# 34-36

@State
def NmlAtkAIR2B_3rd():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR2B_4th')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny256_00', 2)	# 1-2
    sprite('ny256_01', 2)	# 3-4
    sprite('ny256_02', 4)	# 5-8
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    GFX_0('AirSummonDmc', 0)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny256_03', 4)	# 9-12
    sprite('ny256_04', 11)	# 13-23
    sprite('ny256_05', 8)	# 24-31
    sprite('ny256_06', 4)	# 32-35
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_06', 4)	# 36-39
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)	# 40-43

@State
def NmlAtkAIR2B_4th():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny256_07', 2)	# 1-2
    sprite('ny256_08', 2)	# 3-4
    GFX_0('AirSummonDmc', 0)
    sprite('ny256_09', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    sprite('ny256_10', 2)	# 7-8
    sprite('ny256_11', 10)	# 9-18
    sprite('ny256_12', 3)	# 19-21
    sprite('ny256_12', 3)	# 22-24
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_13', 6)	# 25-30
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)	# 31-33

@State
def NmlAtkAIR2B_3rdEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR2B_4thEx')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
    sprite('ny256_00', 2)	# 1-2
    sprite('ny256_01', 2)	# 3-4
    sprite('ny256_02', 4)	# 5-8
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2043, 0)
    GFX_0('AirSummonDmc', 0)
    Unknown1017()
    Unknown1022()
    Unknown1049()
    Unknown1084(1)
    Unknown22004(6, 1)
    callSubroutine('DriveVoice')
    sprite('ny256_03', 4)	# 9-12
    sprite('ny256_04', 11)	# 13-23
    sprite('ny256_05', 8)	# 24-31
    sprite('ny256_06', 4)	# 32-35
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_06', 4)	# 36-39
    callSubroutine('PopSpeed')
    sprite('ny020_04', 4)	# 40-43

@State
def NmlAtkAIR2B_4thEx():

    def upon_IMMEDIATE():
        Unknown23085(1)
        AttackDefaults_AirNormal()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitJumpCancel(1)
        callSubroutine('SS_CancelInitNoRA')
        SLOT_57 = 1
    sprite('ny256_07', 2)	# 1-2
    sprite('ny256_08', 2)	# 3-4
    GFX_0('AirSummonDmc', 0)
    sprite('ny256_09', 2)	# 5-6
    GFX_0('SwordChain', -1)
    Unknown23029(1, 2042, 0)
    sprite('ny256_10', 2)	# 7-8
    sprite('ny256_11', 10)	# 9-18
    sprite('ny256_12', 3)	# 19-21
    sprite('ny256_12', 3)	# 22-24
    WhiffCancelEnable(0)
    Recovery()
    sprite('ny256_13', 6)	# 25-30
    callSubroutine('PopSpeed')
    sprite('ny020_04', 3)	# 31-33

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown1084(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ny402_00', 2)	# 1-2
    Unknown1019(10)
    YAccel(10)
    Unknown1051(10)
    setGravity(0)
    physicsYImpulse(1100)
    sprite('ny402_01', 1)	# 3-3
    sprite('ny402_01', 1)	# 4-4
    Unknown7006('bny203_0', 100, 846818914, 828322608, 0, 0, 100, 846818914, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny402_02', 3)	# 5-7
    GFX_0('AirSummonDmc', 0)
    GFX_0('AirSword', -1)
    Unknown23029(1, 4024, 0)
    sprite('ny402_03', 3)	# 8-10
    sprite('ny402_04', 1)	# 11-11
    Unknown22004(15, 1)
    sprite('ny402_04', 1)	# 12-12
    sprite('ny402_05', 5)	# 13-17
    sprite('ny402_06', 5)	# 18-22
    sprite('ny402_07', 5)	# 23-27
    sprite('ny402_08', 5)	# 28-32
    sprite('ny402_09', 5)	# 33-37
    Recovery()
    sprite('ny020_04', 5)	# 38-42
    setGravity(2000)
    Unknown1021(-1000)
    sprite('ny020_05', 5)	# 43-47
    sprite('ny020_06', 5)	# 48-52
    sprite('ny020_07', 5)	# 53-57

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('ny409_00', 3)	# 1-3
    sprite('ny409_01', 3)	# 4-6
    tag_voice(1, 'bny156_0', 'bny156_1', '', '')
    sprite('ny409_02', 3)	# 7-9	 **attackbox here**
    sprite('ny409_03', 3)	# 10-12	 **attackbox here**
    sprite('ny409_04', 3)	# 13-15	 **attackbox here**
    sprite('ny409_02', 2)	# 16-17	 **attackbox here**
    sprite('ny409_05', 4)	# 18-21	 **attackbox here**
    SFX_0('006_swing_blade_2')
    sprite('ny409_06', 3)	# 22-24	 **attackbox here**
    sprite('ny409_06', 4)	# 25-28	 **attackbox here**
    StartMultihit()
    sprite('ny409_07', 2)	# 29-30	 **attackbox here**
    sprite('ny409_08', 2)	# 31-32	 **attackbox here**
    sprite('ny409_09', 3)	# 33-35	 **attackbox here**
    sprite('ny409_10', 3)	# 36-38
    sprite('ny409_11', 3)	# 39-41
    sprite('ny409_12', 3)	# 42-44
    sprite('ny409_13', 2)	# 45-46
    sprite('ny409_14', 2)	# 47-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('ny409_08', 2)	# 2-3	 **attackbox here**
    sprite('ny409_09', 3)	# 4-6	 **attackbox here**
    sprite('ny409_10', 3)	# 7-9
    sprite('ny409_11', 3)	# 10-12
    sprite('ny409_12', 3)	# 13-15
    sprite('ny409_13', 2)	# 16-17
    sprite('ny211_00', 4)	# 18-21
    sprite('ny211_01', 4)	# 22-25
    sprite('ny211_02', 2)	# 26-27
    sprite('ny211_03', 2)	# 28-29
    tag_voice(1, 'bny157_0', 'bny157_1', '', '')
    SFX_0('010_swing_sword_1')
    sprite('ny211_04', 2)	# 30-31	 **attackbox here**
    sprite('ny211_05', 3)	# 32-34	 **attackbox here**
    sprite('ny211_04', 3)	# 35-37	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ny211_03', 3)	# 38-40
    sprite('ny211_02', 3)	# 41-43
    sprite('ny211_01', 3)	# 44-46
    sprite('ny211_00', 3)	# 47-49
    sprite('ny000_00', 6)	# 50-55
    sprite('ny000_01', 6)	# 56-61
    sprite('ny000_02', 6)	# 62-67
    sprite('ny000_03', 6)	# 68-73
    sprite('ny000_04', 6)	# 74-79
    sprite('ny000_05', 6)	# 80-85
    sprite('ny000_06', 6)	# 86-91
    sprite('ny000_07', 6)	# 92-97
    sprite('ny000_08', 6)	# 98-103
    sprite('ny000_09', 6)	# 104-109
    loopRest()
    sprite('ny000_00', 1)	# 110-110
    label(0)
    sprite('ny000_00', 6)	# 111-116
    sprite('ny000_01', 6)	# 117-122
    sprite('ny000_02', 6)	# 123-128
    sprite('ny000_03', 6)	# 129-134
    sprite('ny000_04', 6)	# 135-140
    sprite('ny000_05', 6)	# 141-146
    sprite('ny000_06', 6)	# 147-152
    sprite('ny000_07', 6)	# 153-158
    sprite('ny000_08', 6)	# 159-164
    sprite('ny000_09', 6)	# 165-170
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 171-171

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ny232_00', 2)	# 1-2
    sprite('ny232_00', 2)	# 3-4
    sprite('ny232_01', 3)	# 5-7
    sprite('ny232_02', 2)	# 8-9	 **attackbox here**
    Unknown7009(2)
    SFX_0('006_swing_blade_1')
    sprite('ny232_03', 2)	# 10-11	 **attackbox here**
    StartMultihit()
    sprite('ny232_04', 2)	# 12-13	 **attackbox here**
    StartMultihit()
    GFX_0('2BZanzo', -1)
    SFX_0('006_swing_blade_1')
    sprite('ny232_04', 1)	# 14-14	 **attackbox here**
    StartMultihit()
    sprite('ny232_04ex01', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('ny232_05', 2)	# 17-18	 **attackbox here**
    StartMultihit()
    sprite('ny232_05ex01', 2)	# 19-20	 **attackbox here**
    sprite('ny232_05ex02', 2)	# 21-22
    sprite('ny232_06', 4)	# 23-26
    sprite('ny232_07', 3)	# 27-29
    sprite('ny232_08', 2)	# 30-31
    sprite('ny010_01', 2)	# 32-33
    sprite('ny010_00', 2)	# 34-35
    sprite('ny400_00', 1)	# 36-36
    sprite('ny400_00', 1)	# 37-37
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 38-41
    sprite('ny400_02', 3)	# 42-44
    Unknown12046(50)
    label(0)
    sprite('ny400_03', 5)	# 45-49
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 50-54
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 55-55

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('ny400_03', 13)	# 1-13
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(8000, 0)
    tag_voice(1, 'bny158_0', 'bny158_1', '', '')
    sprite('ny400_04', 3)	# 14-16
    clearUponHandler(3)
    SLOT_51 = 0
    ScreenShake(16000, 0)
    GFX_0('SwordD400_TAG', -1)
    Unknown38(4, 1)
    GFX_0('SummonDmc', -1)
    sprite('ny400_05', 10)	# 17-26
    Unknown4020(4)
    sprite('ny400_06', 5)	# 27-31
    Unknown4020(0)
    sprite('ny400_07', 5)	# 32-36
    sprite('ny400_08', 5)	# 37-41
    sprite('ny400_09', 5)	# 42-46
    sprite('ny400_10', 5)	# 47-51
    sprite('ny400_11', 5)	# 52-56
    Unknown12046(0)
    sprite('ny400_12', 5)	# 57-61

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 31)	# 1-31
    sprite('ny405_00', 2)	# 32-33	 **attackbox here**
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-820000)
    SLOT_12 = SLOT_19
    Unknown1019(6)
    Unknown8006(100, 1, 1)
    GFX_1('nyef_ny032', 0)
    sprite('ny405_01', 2)	# 34-35	 **attackbox here**
    Unknown8006(100, 1, 1)
    GFX_1('nyef_ny032', 0)
    sprite('ny405_02', 2)	# 36-37	 **attackbox here**
    Unknown8006(100, 1, 1)
    GFX_1('nyef_ny032', 0)
    sprite('ny405_03', 2)	# 38-39	 **attackbox here**
    Unknown1019(80)
    sprite('ny405_04', 2)	# 40-41	 **attackbox here**
    GFX_0('NY_ActP2_Down', -1)
    SFX_0('006_swing_blade_2')
    Unknown1019(80)
    sprite('ny405_05', 3)	# 42-44	 **attackbox here**
    Unknown1019(50)
    sprite('ny405_06', 3)	# 45-47	 **attackbox here**
    Unknown1019(50)
    SFX_0('011_spin_0')
    sprite('ny405_07', 2)	# 48-49	 **attackbox here**
    Unknown1019(0)
    Recovery()
    sprite('ny405_08', 2)	# 50-51	 **attackbox here**
    sprite('ny405_09', 2)	# 52-53	 **attackbox here**
    sprite('ny405_10', 2)	# 54-55	 **attackbox here**
    sprite('ny405_11', 2)	# 56-57	 **attackbox here**
    sprite('ny405_12', 2)	# 58-59	 **attackbox here**
    sprite('ny405_13', 2)	# 60-61	 **attackbox here**
    sprite('ny405_14', 2)	# 62-63	 **attackbox here**
    sprite('ny405_15', 2)	# 64-65	 **attackbox here**
    sprite('ny000_00', 6)	# 66-71
    sprite('ny000_01', 6)	# 72-77
    sprite('ny000_02', 6)	# 78-83
    sprite('ny000_03', 6)	# 84-89
    sprite('ny000_04', 6)	# 90-95
    sprite('ny000_05', 6)	# 96-101
    sprite('ny000_06', 6)	# 102-107
    sprite('ny000_07', 6)	# 108-113
    sprite('ny000_08', 6)	# 114-119
    sprite('ny000_09', 6)	# 120-125

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('keep', 2)	# 1-2
    sprite('ny402_00', 1)	# 3-3
    Unknown1019(10)
    YAccel(10)
    Unknown1051(10)
    setGravity(0)
    physicsYImpulse(1100)
    sprite('ny402_02', 1)	# 4-4
    GFX_0('AirSummonDmc', 0)
    GFX_0('AirSwordTAG', -1)
    Unknown38(4, 1)
    sprite('ny402_03', 1)	# 5-5
    sprite('ny402_04', 2)	# 6-7
    sprite('ny402_05', 2)	# 8-9
    sprite('ny402_06', 2)	# 10-11
    sprite('ny402_07', 2)	# 12-13
    Unknown4020(4)
    sprite('ny402_08', 3)	# 14-16
    Unknown4020(0)
    sprite('ny402_09', 3)	# 17-19
    sprite('ny020_04', 3)	# 20-22
    setGravity(2500)
    Unknown1021(-3000)
    sprite('ny400_00', 3)	# 23-25
    sprite('ny400_00', 1)	# 26-26
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 27-30
    sprite('ny400_02', 3)	# 31-33
    Unknown12046(50)
    label(0)
    sprite('ny400_03', 5)	# 34-38
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 39-43
    gotoLabel(0)

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ny400_03', 13)	# 1-13
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(8000, 0)
    sprite('ny400_04', 3)	# 14-16
    clearUponHandler(3)
    SLOT_51 = 0
    ScreenShake(16000, 0)
    GFX_0('SwordD400_TAG', -1)
    Unknown38(4, 1)
    GFX_0('SummonDmc', -1)
    sprite('ny400_05', 10)	# 17-26
    Unknown4020(4)
    sprite('ny400_06', 5)	# 27-31
    Unknown4020(0)
    sprite('ny400_07', 5)	# 32-36
    sprite('ny400_08', 5)	# 37-41
    sprite('ny400_09', 5)	# 42-46
    sprite('ny400_10', 5)	# 47-51
    sprite('ny400_11', 5)	# 52-56
    Unknown12046(0)
    sprite('ny400_12', 5)	# 57-61

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ny030_01', 4)	# 1-4
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny030', -1)
    sprite('ny032_00', 2)	# 5-6
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    label(0)
    sprite('ny032_01', 4)	# 7-10
    sprite('ny032_02', 4)	# 11-14
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 19-22
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny310_00', 1)	# 23-23
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ny310_01', 2)	# 24-25
    SFX_0('010_swing_sword_0')
    sprite('ny310_02', 3)	# 26-28	 **attackbox here**
    Unknown1084(1)
    sprite('ny310_03', 11)	# 29-39
    SFX_4('bny155')
    sprite('ny310_04', 4)	# 40-43
    StartMultihit()
    sprite('ny310_05', 4)	# 44-47
    sprite('ny310_06', 4)	# 48-51

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        GroundedHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(32000)
        AirUntechableTime(40)
        Unknown11072(1, 1000, 116000)
        Unknown9016(1)
    sprite('ny310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ny311_00', 5)	# 5-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_01', 5)	# 10-14	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_02', 7)	# 15-21	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_03', 8)	# 22-29	 **attackbox here**
    SFX_1('bny153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_04', 9)	# 30-38	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_0('010_swing_sword_1')
    sprite('ny311_05', 4)	# 39-42	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_1('nyef_throw', 0)
    ScreenShake(15000, 0)
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2B')
    sprite('ny311_06', 3)	# 43-45	 **attackbox here**
    sprite('ny311_07', 3)	# 46-48	 **attackbox here**
    sprite('ny311_08', 3)	# 49-51	 **attackbox here**
    sprite('ny311_09', 3)	# 52-54	 **attackbox here**
    sprite('ny311_10', 3)	# 55-57	 **attackbox here**
    sprite('ny311_11', 3)	# 58-60	 **attackbox here**
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2B')
    sprite('ny311_12', 3)	# 61-63	 **attackbox here**

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 30000):
                    SLOT_12 = 30000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ny030_01', 4)	# 1-4
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny030', -1)
    sprite('ny032_00', 2)	# 5-6
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    label(0)
    sprite('ny032_01', 4)	# 7-10
    sprite('ny032_02', 4)	# 11-14
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 19-22
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny310_00', 1)	# 23-23
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ny310_01', 2)	# 24-25
    SFX_0('010_swing_sword_0')
    sprite('ny310_02', 3)	# 26-28	 **attackbox here**
    Unknown1084(1)
    sprite('ny310_03', 11)	# 29-39
    SFX_4('bny155')
    sprite('ny310_04', 4)	# 40-43
    StartMultihit()
    sprite('ny310_05', 4)	# 44-47
    sprite('ny310_06', 4)	# 48-51

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        GroundedHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(32000)
        AirUntechableTime(40)
        Unknown11072(1, -1000, 116000)
        Unknown9016(1)
        Unknown11099(1)
        Unknown13021(1)
        Unknown21005(1)
        Unknown2004(1, 0)
    sprite('ny310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ny311_00', 5)	# 5-9	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_01', 5)	# 10-14	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_02', 7)	# 15-21	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_03', 8)	# 22-29	 **attackbox here**
    SFX_1('bny153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ny311_04', 9)	# 30-38	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_0('010_swing_sword_1')
    sprite('ny311_05', 4)	# 39-42	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_1('nyef_throw', 0)
    ScreenShake(15000, 0)
    sprite('ny311_06', 3)	# 43-45	 **attackbox here**
    teleportRelativeX(100)
    sprite('ny311_07', 3)	# 46-48	 **attackbox here**
    sprite('ny313_00', 3)	# 49-51	 **attackbox here**
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2B')
    sprite('ny313_01', 3)	# 52-54	 **attackbox here**
    sprite('ny313_02', 3)	# 55-57	 **attackbox here**
    sprite('ny313_03', 3)	# 58-60	 **attackbox here**
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2B')
    sprite('ny313_04', 3)	# 61-63	 **attackbox here**

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        Damage(550)
        Unknown11092(1)
        Hitstop(2)
        AirUntechableTime(49)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(10000)
        AirPushbackY(44000)
        YImpluseBeforeWallbounce(2300)
        Unknown9016(1)
        Unknown11057(600)
        PushbackX(12000)

        def upon_11():
            Unknown2037(1)
        sendToLabelUpon(2, 1)
    sprite('ny407_00', 3)	# 1-3	 **attackbox here**
    sprite('ny407_01', 3)	# 4-6	 **attackbox here**
    Unknown7006('bny204_0', 100, 846818914, 828322864, 0, 0, 100, 846818914, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny407_02', 7)	# 7-13	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_3('nyse_33')
    sprite('ny407_03', 3)	# 14-16	 **attackbox here**
    sprite('ny407_04', 3)	# 17-19	 **attackbox here**
    physicsXImpulse(-4500)
    physicsYImpulse(13000)
    Unknown1043()
    sprite('ny407_05', 1)	# 20-20	 **attackbox here**
    GFX_0('407slash', -1)
    RefreshMultihit()
    sprite('ny407_05', 1)	# 21-21	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_05', 1)	# 22-22	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_05', 1)	# 23-23	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 24-24	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 25-25	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 26-26	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 27-27	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_07', 4)	# 28-31	 **attackbox here**
    setInvincible(0)
    sprite('ny407_08', 32767)	# 32-32798	 **attackbox here**
    label(1)
    sprite('ny407_09', 5)	# 32799-32803	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    sprite('ny407_10', 5)	# 32804-32808	 **attackbox here**
    Unknown1019(50)
    sprite('ny407_11', 5)	# 32809-32813	 **attackbox here**
    Unknown1019(50)
    sprite('ny407_12', 5)	# 32814-32818	 **attackbox here**
    Unknown1084(1)
    sprite('ny407_13', 5)	# 32819-32823	 **attackbox here**
    sprite('ny407_14', 5)	# 32824-32828	 **attackbox here**
    sprite('ny407_15', 5)	# 32829-32833	 **attackbox here**
    sprite('ny407_16', 5)	# 32834-32838	 **attackbox here**

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(3)
        Damage(550)
        Unknown11092(1)
        Hitstop(2)
        AirUntechableTime(40)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(2300)
        Unknown9016(1)
        Unknown11057(600)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown13024(0)

        def upon_11():
            Unknown2037(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown1084(1)
    sprite('ny407_03', 2)	# 1-2	 **attackbox here**
    sprite('ny407_03', 2)	# 3-4	 **attackbox here**
    Unknown7006('bny204_0', 100, 846818914, 828322864, 0, 0, 100, 846818914, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_0('006_swing_blade_2')
    SFX_3('nyse_33')
    sprite('ny407_04', 4)	# 5-8	 **attackbox here**
    physicsXImpulse(-4500)
    Unknown1021(21000)
    YAccel(70)
    setGravity(2400)
    sprite('ny407_05', 1)	# 9-9	 **attackbox here**
    GFX_0('407slash', -1)
    RefreshMultihit()
    sprite('ny407_05', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_05', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_05', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    sprite('ny407_06', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_06', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('ny407_07', 4)	# 17-20	 **attackbox here**
    setInvincible(0)
    label(0)
    sprite('ny407_08', 3)	# 21-23	 **attackbox here**
    Unknown1039(110)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny407_09', 5)	# 24-28	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    sprite('ny407_10', 5)	# 29-33	 **attackbox here**
    Unknown1019(50)
    sprite('ny407_11', 5)	# 34-38	 **attackbox here**
    Unknown1019(50)
    sprite('ny407_12', 5)	# 39-43	 **attackbox here**
    Unknown1084(1)
    sprite('ny407_13', 5)	# 44-48	 **attackbox here**
    sprite('ny407_14', 5)	# 49-53	 **attackbox here**
    sprite('ny407_15', 5)	# 54-58	 **attackbox here**
    sprite('ny407_16', 5)	# 59-63	 **attackbox here**

@State
def SpecialDashF():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
    sprite('ny035_05ex01', 3)	# 1-3
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny035_00ex01', 6)	# 4-9
    physicsXImpulse(3000)
    sprite('ny035_01ex01', 2)	# 10-11
    sprite('ny035_02ex01', 3)	# 12-14
    Unknown7006('bny205_0', 100, 846818914, 828323120, 0, 0, 100, 846818914, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    physicsXImpulse(36000)
    SFX_0('000_airdash_0')
    Unknown2017(0)
    sprite('ny035_03ex01', 3)	# 15-17
    GFX_1('nyef_ny032', 0)
    Unknown1019(220)
    Unknown3032()
    Unknown3004(-40)
    sprite('ny035_04ex01', 3)	# 18-20
    GFX_1('nyef_ny032', 0)
    sprite('ny035_05ex01', 3)	# 21-23
    GFX_1('nyef_ny032', 0)
    sprite('ny033_04', 1)	# 24-24
    Unknown2006()
    Unknown1019(70)
    Unknown3004(0)
    Unknown3001(255)
    sprite('ny033_04', 1)	# 25-25
    Unknown1019(70)
    Unknown2017(1)
    sprite('ny033_04', 1)	# 26-26
    Unknown1019(70)
    sprite('ny033_04', 1)	# 27-27
    Unknown1019(70)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13021(1)
    sprite('ny033_05', 1)	# 28-28
    Unknown1019(70)
    sprite('ny033_05', 1)	# 29-29
    Unknown1019(70)
    sprite('ny033_05', 1)	# 30-30
    Unknown1019(70)
    sprite('ny033_05', 1)	# 31-31
    Unknown1019(70)
    sprite('ny033_05', 1)	# 32-32
    Unknown1019(70)
    sprite('ny033_05', 1)	# 33-33
    Unknown1019(70)
    sprite('ny033_06', 1)	# 34-34
    Unknown1019(70)
    sprite('ny033_06', 1)	# 35-35
    Unknown1019(70)
    sprite('ny033_06', 1)	# 36-36
    Unknown1019(70)
    sprite('ny033_06', 1)	# 37-37
    Unknown1019(70)
    sprite('ny033_06', 4)	# 38-41
    Unknown1019(70)

@State
def SpecialDashB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23076()
        Unknown11063(1)
        Unknown22008(8)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
    sprite('ny024_00', 2)	# 1-2
    sprite('ny024_01', 2)	# 3-4
    sprite('ny410_02', 2)	# 5-6
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny410_03', 2)	# 7-8
    sprite('ny410_04', 4)	# 9-12
    Unknown7006('bny206_0', 100, 846818914, 828323376, 0, 0, 100, 846818914, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('nyse_03')
    Unknown3004(-30)
    Unknown3032()
    Unknown8001(0, 100)
    teleportRelativeX(-50000)
    physicsXImpulse(-36000)
    physicsYImpulse(48000)
    Unknown1028(200)
    sprite('ny410_05', 3)	# 13-15
    Unknown1019(50)
    YAccel(50)
    sprite('ny410_05', 3)	# 16-18
    Unknown1019(50)
    YAccel(50)
    sprite('ny410_15', 4)	# 19-22
    Unknown1019(50)
    YAccel(50)
    Unknown1043()
    Unknown13014(1)
    Unknown13015(1)
    Unknown13021(1)
    sprite('ny410_15', 4)	# 23-26
    Unknown1019(50)
    Unknown1034(0)
    Unknown3001(0)
    Unknown3004(63)
    Unknown3031()
    sprite('ny410_16', 4)	# 27-30
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(50)

@State
def SpecialDashAirF():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
        Unknown22001(-1)
        Unknown22003(-1)
        Unknown1084(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
    sprite('ny035_05', 3)	# 1-3	 **attackbox here**
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny035_00', 3)	# 4-6
    physicsXImpulse(3000)
    sprite('ny035_01', 2)	# 7-8
    sprite('ny035_02', 2)	# 9-10
    Unknown7006('bny205_0', 100, 846818914, 828323120, 0, 0, 100, 846818914, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    physicsXImpulse(15000)
    Unknown2017(0)
    sprite('ny035_03', 3)	# 11-13
    Unknown8009(1)
    Unknown1019(220)
    Unknown3032()
    Unknown3004(-40)
    sprite('ny035_04', 3)	# 14-16
    sprite('ny035_05', 3)	# 17-19	 **attackbox here**
    sprite('ny036_05', 2)	# 20-21
    Unknown2006()
    setGravity(1400)
    Unknown1019(70)
    Unknown2017(1)
    Unknown3004(0)
    Unknown3001(255)
    sprite('ny036_05', 4)	# 22-25
    Unknown1019(70)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13021(1)
    sprite('ny020_05', 4)	# 26-29
    Unknown1019(70)
    sprite('ny020_06', 4)	# 30-33
    Unknown1019(70)
    sprite('ny020_06', 4)	# 34-37
    Unknown1019(70)

@State
def SpecialDashAirB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23076()
        Unknown11063(1)
        Unknown22001(-1)
        Unknown22003(-1)
        Unknown1084(1)

        def upon_STATE_END():
            Unknown3031()
            Unknown3004(0)
            Unknown3001(255)
    sprite('ny036_00', 3)	# 1-3
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny036_00', 3)	# 4-6
    physicsXImpulse(-4000)
    Unknown3004(-30)
    Unknown3032()
    sprite('ny036_01', 3)	# 7-9
    sprite('ny036_02', 3)	# 10-12
    Unknown7006('bny206_0', 100, 846818914, 828323376, 0, 0, 100, 846818914, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    physicsXImpulse(-25000)
    Unknown8009(1)
    sprite('ny036_03', 3)	# 13-15
    sprite('ny036_04', 3)	# 16-18
    sprite('ny036_05', 3)	# 19-21
    sprite('ny036_05', 4)	# 22-25
    Unknown3004(0)
    Unknown3001(255)
    Unknown3031()
    Unknown1019(70)
    Unknown1043()
    Unknown13014(1)
    Unknown13015(1)
    sprite('ny020_05', 4)	# 26-29
    Unknown1019(70)
    sprite('ny020_06', 4)	# 30-33
    Unknown1019(70)

@State
def LowShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ny401_00', 2)	# 1-2	 **attackbox here**
    sprite('ny401_01', 1)	# 3-3	 **attackbox here**
    sprite('ny401_01', 1)	# 4-4	 **attackbox here**
    GFX_0('SummonDmc', -1)
    SFX_3('nyse_30')
    sprite('ny401_02', 2)	# 5-6	 **attackbox here**
    sprite('ny401_03', 2)	# 7-8
    Unknown7006('bny200_0', 100, 846818914, 828321840, 0, 0, 100, 846818914, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny401_04', 2)	# 9-10
    sprite('ny401_05', 1)	# 11-11
    sprite('ny401_05', 1)	# 12-12
    GFX_0('LowSword', -1)
    Unknown23029(1, 4011, 0)
    SFX_0('006_swing_blade_2')
    sprite('ny401_06', 5)	# 13-17
    sprite('ny401_07', 6)	# 18-23
    sprite('ny401_08', 7)	# 24-30
    sprite('ny401_09', 6)	# 31-36
    sprite('ny401_10', 6)	# 37-42
    sprite('ny401_11', 4)	# 43-46
    Recovery()
    sprite('ny401_12', 4)	# 47-50
    sprite('ny401_13', 4)	# 51-54

@State
def LowShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ny401_00', 2)	# 1-2	 **attackbox here**
    sprite('ny401_01', 1)	# 3-3	 **attackbox here**
    sprite('ny401_01', 1)	# 4-4	 **attackbox here**
    GFX_0('SummonDmc', -1)
    SFX_3('nyse_30')
    sprite('ny401_02', 2)	# 5-6	 **attackbox here**
    sprite('ny401_03', 2)	# 7-8
    Unknown7006('bny200_0', 100, 846818914, 828321840, 0, 0, 100, 846818914, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny401_04', 2)	# 9-10
    sprite('ny401_05', 1)	# 11-11
    sprite('ny401_05', 1)	# 12-12
    sprite('ny401_06', 5)	# 13-17
    sprite('ny401_07', 6)	# 18-23
    GFX_0('LowSword', -1)
    Unknown23029(1, 4012, 0)
    SFX_0('006_swing_blade_2')
    sprite('ny401_08', 7)	# 24-30
    sprite('ny401_09', 6)	# 31-36
    sprite('ny401_10', 6)	# 37-42
    sprite('ny401_11', 4)	# 43-46
    Recovery()
    sprite('ny401_12', 4)	# 47-50
    sprite('ny401_13', 4)	# 51-54

@State
def LowShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ny401_00', 2)	# 1-2	 **attackbox here**
    sprite('ny401_01', 1)	# 3-3	 **attackbox here**
    sprite('ny401_01', 1)	# 4-4	 **attackbox here**
    GFX_0('SummonDmc', -1)
    SFX_3('nyse_30')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ny401_02', 2)	# 5-6	 **attackbox here**
    sprite('ny401_03', 2)	# 7-8
    Unknown7006('bny200_0', 100, 846818914, 828321840, 0, 0, 100, 846818914, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny401_04', 2)	# 9-10
    sprite('ny401_05', 1)	# 11-11
    sprite('ny401_05', 1)	# 12-12
    GFX_0('LowSword_Ex', -1)
    SFX_0('006_swing_blade_2')
    sprite('ny401_06', 5)	# 13-17
    sprite('ny401_07', 6)	# 18-23
    sprite('ny401_08', 7)	# 24-30
    sprite('ny401_09', 6)	# 31-36
    sprite('ny401_10', 6)	# 37-42
    sprite('ny401_11', 4)	# 43-46
    Recovery()
    sprite('ny401_12', 4)	# 47-50
    sprite('ny401_13', 4)	# 51-54

@State
def LargeShot_matome():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_3():
            if (not SLOT_94):
                CheckInput(0x1c)
                SLOT_2 = (SLOT_2 + SLOT_0)
                if SLOT_51:
                    if CheckInput(INPUT_PRESS_C):
                        sendToLabel(0)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('ny400_00', 4)	# 1-4
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 5-8
    sprite('ny400_02', 3)	# 9-11
    Unknown12046(50)
    sprite('ny400_03', 5)	# 12-16
    Unknown7006('bny202_0', 100, 846818914, 828322352, 0, 0, 100, 846818914, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 17-21
    SLOT_51 = 1
    sprite('ny400_03', 10)	# 22-31
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    WhiffCancelEnable(1)
    loopRest()
    (SLOT_2 == SLOT_18)
    Unknown19(1, 2, 0)
    sprite('ny400_03', 10)	# 32-41
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(2000, 0)
    sprite('ny400_03', 10)	# 42-51
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(4000, 0)
    sprite('ny400_03', 10)	# 52-61
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(8000, 0)
    sprite('ny400_04', 3)	# 62-64
    clearUponHandler(3)
    SLOT_51 = 0
    ScreenShake(16000, 0)
    sprite('ny400_05', 3)	# 65-67
    GFX_0('SummonDmc', -1)
    GFX_0('NY_TripleSword_D', -1)
    sprite('ny400_06', 3)	# 68-70
    sprite('ny400_07', 3)	# 71-73
    WhiffCancelEnable(1)
    sprite('ny400_08', 3)	# 74-76
    sprite('ny400_09', 3)	# 77-79
    loopRest()
    gotoLabel(9)
    label(0)
    clearUponHandler(3)
    SLOT_51 = 0
    sprite('ny400_04', 3)	# 80-82
    GFX_0('SummonDmc', -1)
    GFX_0('NY_TripleSword_C', -1)
    ScreenShake(10000, 0)
    sprite('ny400_05', 6)	# 83-88
    WhiffCancelEnable(1)
    sprite('ny400_06', 6)	# 89-94
    sprite('ny400_07', 6)	# 95-100
    sprite('ny400_08', 6)	# 101-106
    sprite('ny400_09', 6)	# 107-112
    loopRest()
    gotoLabel(9)
    label(1)
    clearUponHandler(3)
    SLOT_51 = 0
    sprite('ny400_04', 3)	# 113-115
    GFX_0('SummonDmc', -1)
    GFX_0('NY_TripleSword', -1)
    ScreenShake(12000, 0)
    sprite('ny400_05', 5)	# 116-120
    sprite('ny400_06', 5)	# 121-125
    sprite('ny400_07', 5)	# 126-130
    WhiffCancelEnable(1)
    sprite('ny400_08', 5)	# 131-135
    sprite('ny400_09', 5)	# 136-140
    label(9)
    sprite('ny400_10', 5)	# 141-145
    WhiffCancelEnable(0)
    sprite('ny400_11', 5)	# 146-150
    Unknown12046(0)
    sprite('ny400_12', 5)	# 151-155

@State
def LargeShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_STATE_END():
            Unknown12046(0)
    sprite('ny400_00', 3)	# 1-3
    sprite('ny400_00', 1)	# 4-4
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 5-8
    sprite('ny400_02', 3)	# 9-11
    Unknown12046(50)
    sprite('ny400_03', 5)	# 12-16
    Unknown7006('bny202_0', 100, 846818914, 828322352, 0, 0, 100, 846818914, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 17-21
    SLOT_51 = 1
    sprite('ny400_03', 5)	# 22-26
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_04', 3)	# 27-29
    ScreenShake(12000, 0)
    sprite('ny400_05', 5)	# 30-34
    GFX_0('SummonDmc', -1)
    GFX_0('TripleSwordA', -1)
    sprite('ny400_06', 10)	# 35-44
    sprite('ny400_07', 6)	# 45-50
    WhiffCancelEnable(1)
    sprite('ny400_08', 6)	# 51-56
    sprite('ny400_09', 6)	# 57-62
    sprite('ny400_10', 6)	# 63-68
    WhiffCancelEnable(0)
    sprite('ny400_11', 6)	# 69-74
    Unknown12046(0)
    sprite('ny400_12', 5)	# 75-79

@State
def LargeShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_STATE_END():
            Unknown12046(0)
    sprite('ny400_00', 3)	# 1-3
    sprite('ny400_00', 1)	# 4-4
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 5-8
    sprite('ny400_02', 3)	# 9-11
    Unknown12046(50)
    sprite('ny400_03', 5)	# 12-16
    Unknown7006('bny202_0', 100, 846818914, 828322352, 0, 0, 100, 846818914, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 17-21
    SLOT_51 = 1
    sprite('ny400_03', 10)	# 22-31
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 10)	# 32-41
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(2000, 0)
    sprite('ny400_03', 10)	# 42-51
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(4000, 0)
    sprite('ny400_03', 10)	# 52-61
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    ScreenShake(8000, 0)
    sprite('ny400_04', 3)	# 62-64
    clearUponHandler(3)
    SLOT_51 = 0
    ScreenShake(16000, 0)
    sprite('ny400_05', 4)	# 65-68
    GFX_0('SummonDmc', -1)
    GFX_0('TripleSwordB', -1)
    sprite('ny400_06', 4)	# 69-72
    sprite('ny400_07', 4)	# 73-76
    sprite('ny400_08', 4)	# 77-80
    sprite('ny400_09', 4)	# 81-84
    sprite('ny400_10', 5)	# 85-89
    sprite('ny400_11', 5)	# 90-94
    Unknown12046(0)
    sprite('ny400_12', 5)	# 95-99

@State
def LargeShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_STATE_END():
            Unknown12046(0)
    sprite('ny400_00', 3)	# 1-3
    sprite('ny400_00', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    GFX_0('SummonDmc', -1)
    sprite('ny400_01', 4)	# 5-8
    sprite('ny400_02', 3)	# 9-11
    Unknown12046(50)
    sprite('ny400_03', 5)	# 12-16
    Unknown7006('bny202_0', 100, 846818914, 828322352, 0, 0, 100, 846818914, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_03', 5)	# 17-21
    sprite('ny400_03', 5)	# 22-26
    GFX_0('NY_SlowHand', 0)
    SFX_0('015_blaze_1')
    sprite('ny400_04', 3)	# 27-29
    ScreenShake(12000, 0)
    sprite('ny400_05', 4)	# 30-33
    GFX_0('SummonDmc', -1)
    GFX_0('TripleSwordC', -1)
    sprite('ny400_06', 4)	# 34-37
    sprite('ny400_07', 4)	# 38-41
    sprite('ny400_08', 4)	# 42-45
    sprite('ny400_09', 4)	# 46-49
    sprite('ny400_10', 5)	# 50-54
    sprite('ny400_11', 5)	# 55-59
    Unknown12046(0)
    sprite('ny400_12', 5)	# 60-64

@State
def SlowFieldA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2003(1)
        WhiffCancelEnable(1)
        WhiffCancel('SpecialDashF')
        WhiffCancel('SpecialDashB')
    sprite('ny403_00', 2)	# 1-2
    sprite('ny403_01', 2)	# 3-4
    sprite('ny403_02', 2)	# 5-6
    sprite('ny403_03', 2)	# 7-8
    sprite('ny403_07', 2)	# 9-10
    Unknown7006('bny201_0', 100, 846818914, 828322096, 0, 0, 100, 846818914, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny403_08', 2)	# 11-12
    sprite('ny403_09', 3)	# 13-15	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    Unknown23029(5, 4034, 0)
    GFX_0('SummonSlowArea', -1)
    Unknown38(5, 1)
    Unknown23029(5, 4031, 0)
    GFX_0('NY_SlowHand', 0)
    SLOT_31 = 0
    WhiffCancelEnable(1)
    sprite('ny403_10', 3)	# 16-18
    sprite('ny403_11', 6)	# 19-24
    sprite('ny403_12', 6)	# 25-30
    sprite('ny403_13', 6)	# 31-36
    sprite('ny403_14', 3)	# 37-39
    sprite('ny403_14', 3)	# 40-42
    WhiffCancelEnable(0)

@State
def SlowFieldB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2003(1)
        WhiffCancelEnable(1)
        WhiffCancel('SpecialDashF')
        WhiffCancel('SpecialDashB')
    sprite('ny403_00', 2)	# 1-2
    sprite('ny403_01', 2)	# 3-4
    sprite('ny403_02', 2)	# 5-6
    sprite('ny403_03', 2)	# 7-8
    sprite('ny403_07', 2)	# 9-10
    Unknown7006('bny201_0', 100, 846818914, 828322096, 0, 0, 100, 846818914, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny403_08', 2)	# 11-12
    sprite('ny403_09', 3)	# 13-15	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    Unknown23029(5, 4034, 0)
    GFX_0('SummonSlowArea', -1)
    Unknown38(5, 1)
    Unknown23029(5, 4032, 0)
    GFX_0('NY_SlowHand', 0)
    SLOT_31 = 0
    WhiffCancelEnable(1)
    sprite('ny403_10', 3)	# 16-18
    sprite('ny403_11', 6)	# 19-24
    sprite('ny403_12', 6)	# 25-30
    sprite('ny403_13', 6)	# 31-36
    sprite('ny403_14', 3)	# 37-39
    sprite('ny403_14', 3)	# 40-42
    WhiffCancelEnable(0)

@State
def SlowFieldC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2003(1)
        WhiffCancel('SpecialDashF')
        WhiffCancel('SpecialDashB')
    sprite('ny403_00', 2)	# 1-2
    sprite('ny403_01', 2)	# 3-4
    sprite('ny403_02', 2)	# 5-6
    sprite('ny403_03', 2)	# 7-8
    sprite('ny403_07', 2)	# 9-10
    Unknown7006('bny201_0', 100, 846818914, 828322096, 0, 0, 100, 846818914, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny403_08', 2)	# 11-12
    sprite('ny403_09', 3)	# 13-15	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    Unknown23029(5, 4034, 0)
    GFX_0('SummonSlowArea', -1)
    Unknown38(5, 1)
    Unknown23029(5, 4033, 0)
    GFX_0('NY_SlowHand', 0)
    SLOT_31 = 0
    WhiffCancelEnable(1)
    sprite('ny403_10', 3)	# 16-18
    sprite('ny403_11', 6)	# 19-24
    sprite('ny403_12', 6)	# 25-30
    sprite('ny403_13', 6)	# 31-36
    sprite('ny403_14', 3)	# 37-39
    sprite('ny403_14', 3)	# 40-42
    WhiffCancelEnable(0)

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ny402_00', 3)	# 1-3
    Unknown1019(10)
    YAccel(10)
    Unknown1051(10)
    setGravity(0)
    physicsYImpulse(1100)
    Unknown7006('bny203_0', 100, 846818914, 828322608, 0, 0, 100, 846818914, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny402_01', 3)	# 4-6
    sprite('ny402_02', 3)	# 7-9
    GFX_0('AirSummonDmc', 0)
    GFX_0('AirSword', -1)
    Unknown23029(1, 4021, 0)
    sprite('ny402_03', 3)	# 10-12
    sprite('ny402_04', 1)	# 13-13
    Unknown22004(10, 1)
    sprite('ny402_04', 1)	# 14-14
    sprite('ny402_05', 5)	# 15-19
    sprite('ny402_06', 5)	# 20-24
    sprite('ny402_07', 5)	# 25-29
    sprite('ny402_08', 5)	# 30-34
    sprite('ny402_09', 5)	# 35-39
    sprite('ny020_04', 5)	# 40-44
    setGravity(2500)
    Unknown1021(-3000)
    sprite('ny020_05', 5)	# 45-49
    sprite('ny020_06', 5)	# 50-54
    sprite('ny020_07', 5)	# 55-59

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ny402_00', 3)	# 1-3
    Unknown1019(10)
    YAccel(10)
    Unknown1051(10)
    setGravity(0)
    physicsYImpulse(1100)
    Unknown7006('bny203_0', 100, 846818914, 828322608, 0, 0, 100, 846818914, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny402_01', 3)	# 4-6
    sprite('ny402_02', 3)	# 7-9
    GFX_0('AirSummonDmc', 0)
    GFX_0('AirSword', -1)
    sprite('ny402_03', 3)	# 10-12
    sprite('ny402_04', 1)	# 13-13
    Unknown22004(10, 1)
    sprite('ny402_04', 1)	# 14-14
    Unknown26('AirSword')
    sprite('ny402_05', 5)	# 15-19
    sprite('ny402_06', 4)	# 20-23
    sprite('ny402_07', 4)	# 24-27
    GFX_0('AirSword', -1)
    Unknown23029(1, 4022, 0)
    sprite('ny402_08', 4)	# 28-31
    setGravity(1700)
    sprite('ny402_09', 4)	# 32-35
    sprite('ny020_04', 5)	# 36-40
    setGravity(2500)
    Unknown1021(-3000)
    sprite('ny020_05', 5)	# 41-45
    sprite('ny020_06', 5)	# 46-50
    sprite('ny020_07', 5)	# 51-55

@State
def AirShotC():

    def upon_IMMEDIATE():
        Unknown17003()

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ny402_00', 3)	# 1-3
    Unknown1019(10)
    YAccel(10)
    Unknown1051(10)
    setGravity(0)
    physicsYImpulse(1100)
    Unknown7006('bny203_0', 100, 846818914, 828322608, 0, 0, 100, 846818914, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny402_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ny402_02', 3)	# 7-9
    GFX_0('AirSummonDmc', 0)
    GFX_0('AirSword', -1)
    Unknown23029(1, 4023, 0)
    sprite('ny402_03', 3)	# 10-12
    sprite('ny402_04', 1)	# 13-13
    Unknown22004(10, 1)
    sprite('ny402_04', 1)	# 14-14
    sprite('ny402_05', 5)	# 15-19
    sprite('ny402_06', 5)	# 20-24
    sprite('ny402_07', 5)	# 25-29
    sprite('ny402_08', 5)	# 30-34
    sprite('ny402_09', 5)	# 35-39
    sprite('ny020_04', 5)	# 40-44
    setGravity(2500)
    Unknown1021(-3000)
    sprite('ny020_05', 5)	# 45-49
    sprite('ny020_06', 5)	# 50-54
    sprite('ny020_07', 5)	# 55-59

@State
def UltimateMultiSword():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown23027()
        setInvincible(1)
        Unknown22022(0)
        Unknown22036(0)
    sprite('ny430_00', 5)	# 1-5
    sprite('ny430_01', 5)	# 6-10
    sprite('ny430_02', 5)	# 11-15
    sprite('ny430_02', 19)	# 16-34
    Unknown2036(41, -1, 0)
    Unknown2058(-10000)
    Unknown7006('bny250_0', 100, 846818914, 828321845, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown22022(1)
    Unknown22036(1)
    Unknown30080('')
    sprite('ny430_02', 1)	# 35-35
    Unknown22022(0)
    Unknown22036(0)
    sprite('ny430_02', 10)	# 36-45
    GFX_0('DDMultiSwordMaster', -1)
    GFX_0('SummonDmc', -1)
    sprite('ny430_02', 5)	# 46-50
    sprite('ny430_03', 5)	# 51-55
    sprite('ny430_04', 5)	# 56-60
    sprite('ny430_05', 2)	# 61-62
    setInvincible(0)
    sprite('ny430_06', 3)	# 63-65
    sprite('ny430_07', 3)	# 66-68
    sprite('ny430_08', 3)	# 69-71
    sprite('ny430_09', 3)	# 72-74
    sprite('ny430_06', 3)	# 75-77
    sprite('ny430_07', 3)	# 78-80
    sprite('ny430_08', 3)	# 81-83
    sprite('ny430_09', 3)	# 84-86
    sprite('ny430_06', 3)	# 87-89
    sprite('ny430_07', 3)	# 90-92
    sprite('ny430_08', 3)	# 93-95
    sprite('ny430_09', 3)	# 96-98
    sprite('ny430_10', 4)	# 99-102
    sprite('ny430_11', 4)	# 103-106
    sprite('ny430_12', 4)	# 107-110

@State
def UltimateMultiSwordOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown23027()
        setInvincible(1)
    sprite('ny430_00', 5)	# 1-5
    sprite('ny430_01', 5)	# 6-10
    sprite('ny430_02', 5)	# 11-15
    sprite('ny430_02', 19)	# 16-34
    Unknown2036(41, -1, 0)
    Unknown2058(-10000)
    Unknown7006('bny250_0', 100, 846818914, 828321845, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown22022(1)
    Unknown22036(1)
    Unknown30080('')
    sprite('ny430_02', 1)	# 35-35
    Unknown22022(0)
    Unknown22036(0)
    sprite('ny430_02', 10)	# 36-45
    GFX_0('DDMultiSwordMasterOD', -1)
    GFX_0('SummonDmc', -1)
    sprite('ny430_02', 5)	# 46-50
    sprite('ny430_03', 5)	# 51-55
    sprite('ny430_04', 5)	# 56-60
    sprite('ny430_05', 2)	# 61-62
    setInvincible(0)
    sprite('ny430_06', 3)	# 63-65
    sprite('ny430_07', 3)	# 66-68
    sprite('ny430_08', 3)	# 69-71
    sprite('ny430_09', 3)	# 72-74
    sprite('ny430_06', 3)	# 75-77
    sprite('ny430_07', 3)	# 78-80
    sprite('ny430_08', 3)	# 81-83
    sprite('ny430_09', 3)	# 84-86
    sprite('ny430_10', 4)	# 87-90
    sprite('ny430_11', 4)	# 91-94
    sprite('ny430_12', 4)	# 95-98

@State
def UltimateLargeSwordLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown23027()
        setInvincible(1)
    sprite('ny431_00', 4)	# 1-4
    sprite('ny431_01', 5)	# 5-9
    sprite('ny431_02', 5)	# 10-14
    Unknown2036(52, -1, 0)
    Unknown2058(-10000)
    GFX_0('SummonDmc', -1)
    Unknown7006('bny251_0', 100, 846818914, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    sprite('ny431_03', 5)	# 15-19
    sprite('ny431_04', 5)	# 20-24
    SFX_3('nyse_26')
    GFX_0('DDBigSwordMaster', -1)
    sprite('ny431_05', 30)	# 25-54
    sprite('ny431_06', 2)	# 55-56
    sprite('ny431_07', 2)	# 57-58
    sprite('ny431_08', 2)	# 59-60
    sprite('ny431_09', 3)	# 61-63
    sprite('ny431_10', 3)	# 64-66
    setInvincible(0)
    sprite('ny431_11', 3)	# 67-69
    sprite('ny431_12', 3)	# 70-72
    sprite('ny431_09', 4)	# 73-76
    sprite('ny431_10', 4)	# 77-80
    sprite('ny431_11', 4)	# 81-84
    sprite('ny431_12', 4)	# 85-88
    sprite('ny431_09', 4)	# 89-92
    sprite('ny431_10', 4)	# 93-96
    sprite('ny431_11', 4)	# 97-100
    sprite('ny431_12', 4)	# 101-104
    sprite('ny431_09', 4)	# 105-108
    sprite('ny431_10', 4)	# 109-112
    sprite('ny431_11', 4)	# 113-116
    sprite('ny431_12', 4)	# 117-120
    sprite('ny431_13', 4)	# 121-124
    sprite('ny431_14', 4)	# 125-128
    sprite('ny431_15', 4)	# 129-132
    sprite('ny431_16', 4)	# 133-136

@State
def UltimateLargeSwordLandOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown23027()
        setInvincible(1)
    sprite('ny431_00', 4)	# 1-4
    sprite('ny431_01', 5)	# 5-9
    sprite('ny431_02', 5)	# 10-14
    Unknown2036(52, -1, 0)
    Unknown2058(-10000)
    GFX_0('SummonDmc', -1)
    Unknown7006('bny251_0', 100, 846818914, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    sprite('ny431_03', 5)	# 15-19
    sprite('ny431_04', 5)	# 20-24
    SFX_3('nyse_26')
    GFX_0('DDBigSwordODMaster', -1)
    sprite('ny431_05', 30)	# 25-54
    sprite('ny431_06', 2)	# 55-56
    sprite('ny431_07', 2)	# 57-58
    sprite('ny431_08', 2)	# 59-60
    sprite('ny431_09', 3)	# 61-63
    sprite('ny431_10', 3)	# 64-66
    setInvincible(0)
    sprite('ny431_11', 3)	# 67-69
    sprite('ny431_12', 3)	# 70-72
    sprite('ny431_09', 4)	# 73-76
    sprite('ny431_10', 4)	# 77-80
    sprite('ny431_11', 4)	# 81-84
    sprite('ny431_12', 4)	# 85-88
    sprite('ny431_09', 4)	# 89-92
    sprite('ny431_10', 4)	# 93-96
    sprite('ny431_11', 4)	# 97-100
    sprite('ny431_12', 4)	# 101-104
    sprite('ny431_09', 4)	# 105-108
    sprite('ny431_10', 4)	# 109-112
    sprite('ny431_11', 4)	# 113-116
    sprite('ny431_12', 4)	# 117-120
    sprite('ny431_09', 4)	# 121-124
    sprite('ny431_10', 4)	# 125-128
    sprite('ny431_11', 4)	# 129-132
    sprite('ny431_12', 4)	# 133-136
    sprite('ny431_09', 4)	# 137-140
    sprite('ny431_10', 4)	# 141-144
    sprite('ny431_11', 4)	# 145-148
    sprite('ny431_12', 4)	# 149-152
    sprite('ny431_13', 4)	# 153-156
    sprite('ny431_14', 4)	# 157-160
    sprite('ny431_15', 4)	# 161-164
    sprite('ny431_16', 4)	# 165-168

@State
def UltimateLargeSwordAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown23027()
        setInvincible(1)
    sprite('ny020_03', 2)	# 1-2
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1045(0)
    physicsYImpulse(800)
    Unknown22004(6, 1)
    sprite('ny020_02', 2)	# 3-4
    sprite('ny431_air00', 3)	# 5-7
    sprite('ny431_air01', 4)	# 8-11
    Unknown2036(42, -1, 0)
    Unknown2058(-10000)
    GFX_1('nyef_sumDDmc', -1)
    GFX_0('AirSummonDmc', 0)
    Unknown7006('bny251_0', 100, 846818914, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    sprite('ny431_air02', 4)	# 12-15
    SFX_3('nyse_26')
    GFX_0('DDBigSwordMaster', -1)
    sprite('ny431_air03', 4)	# 16-19
    sprite('ny431_air04', 30)	# 20-49
    physicsYImpulse(0)
    sprite('ny431_air05', 2)	# 50-51
    setInvincible(0)
    sprite('ny431_air06', 2)	# 52-53
    sprite('ny431_air07', 2)	# 54-55
    sprite('ny431_air08', 3)	# 56-58
    sprite('ny431_air09', 3)	# 59-61
    sprite('ny431_air10', 3)	# 62-64
    sprite('ny431_air11', 3)	# 65-67
    sprite('ny431_air08', 4)	# 68-71
    sprite('ny431_air09', 4)	# 72-75
    sprite('ny431_air10', 4)	# 76-79
    GFX_1('nyef_sumDDmcend', -1)
    sprite('ny431_air08', 4)	# 80-83
    sprite('ny431_air09', 4)	# 84-87
    sprite('ny431_air10', 4)	# 88-91
    sprite('ny431_air08', 4)	# 92-95
    sprite('ny431_air09', 4)	# 96-99
    sprite('ny431_air10', 4)	# 100-103
    sprite('ny431_air11', 4)	# 104-107
    sprite('ny431_air12', 2)	# 108-109
    sprite('ny431_air13', 2)	# 110-111
    Unknown1043()
    physicsYImpulse(10000)
    sprite('ny020_02', 2)	# 112-113
    sprite('ny020_04', 3)	# 114-116
    sprite('ny020_05', 3)	# 117-119
    label(0)
    sprite('ny020_06', 3)	# 120-122
    sprite('ny020_07', 3)	# 123-125
    loopRest()
    gotoLabel(0)

@State
def UltimateLargeSwordAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        Unknown23027()
        setInvincible(1)
    sprite('ny020_03', 2)	# 1-2
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    Unknown1045(0)
    physicsYImpulse(800)
    Unknown22004(6, 1)
    sprite('ny020_02', 2)	# 3-4
    sprite('ny431_air00', 3)	# 5-7
    sprite('ny431_air01', 4)	# 8-11
    Unknown2036(42, -1, 0)
    Unknown2058(-10000)
    GFX_1('nyef_sumDDmc', -1)
    GFX_0('AirSummonDmc', 0)
    Unknown7006('bny251_0', 100, 846818914, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30080('')
    sprite('ny431_air02', 4)	# 12-15
    SFX_3('nyse_26')
    GFX_0('DDBigSwordODMaster', -1)
    sprite('ny431_air03', 4)	# 16-19
    sprite('ny431_air04', 30)	# 20-49
    physicsYImpulse(0)
    sprite('ny431_air05', 2)	# 50-51
    setInvincible(0)
    sprite('ny431_air06', 2)	# 52-53
    sprite('ny431_air07', 2)	# 54-55
    sprite('ny431_air08', 3)	# 56-58
    sprite('ny431_air09', 3)	# 59-61
    sprite('ny431_air10', 3)	# 62-64
    sprite('ny431_air11', 3)	# 65-67
    sprite('ny431_air08', 4)	# 68-71
    sprite('ny431_air09', 4)	# 72-75
    sprite('ny431_air10', 4)	# 76-79
    GFX_1('nyef_sumDDmcend', -1)
    sprite('ny431_air08', 4)	# 80-83
    sprite('ny431_air09', 4)	# 84-87
    sprite('ny431_air10', 4)	# 88-91
    sprite('ny431_air08', 4)	# 92-95
    sprite('ny431_air09', 4)	# 96-99
    sprite('ny431_air10', 4)	# 100-103
    sprite('ny431_air11', 4)	# 104-107
    sprite('ny431_air12', 2)	# 108-109
    sprite('ny321_10', 1)	# 110-110
    sprite('ny321_11', 1)	# 111-111
    sprite('ny321_12', 3)	# 112-114
    physicsXImpulse(-8000)
    physicsYImpulse(20000)
    setGravity(500)
    Unknown2005()
    Unknown22004(10, 1)
    sprite('ny321_13', 3)	# 115-117
    sprite('ny321_14', 3)	# 118-120
    sprite('ny321_15', 3)	# 121-123
    sprite('ny321_16', 3)	# 124-126
    sprite('ny020_02', 2)	# 127-128
    Unknown1019(50)
    Unknown1043()
    Unknown2006()
    sprite('ny020_04', 3)	# 129-131
    sprite('ny020_05', 3)	# 132-134
    label(0)
    sprite('ny020_06', 3)	# 135-137
    sprite('ny020_07', 3)	# 138-140
    loopRest()
    gotoLabel(0)

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(0)
        PushbackX(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(210)
        Unknown9142(200)
        Hitstop(0)
        Unknown11072(1, 200000, 0)
        Unknown11064(1)
        Unknown30048(1)
        Unknown11069('AstralHeatCatch')
        Unknown28(12, 'AstralHeatCatch')
        Unknown2054(1)
    sprite('ny450_00', 4)	# 1-4
    setInvincible(1)
    Unknown22019('0000000000000000000000000000000000000000')
    tag_voice(1, 'bny290_0', 'bny290_1', '', '')
    sprite('ny450_01', 4)	# 5-8
    sprite('ny450_02', 4)	# 9-12
    sprite('ny450_03', 3)	# 13-15
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    Unknown2036(101, -1, 2)
    Unknown23147()
    GFX_0('EMB_NY_AH', -1)
    GFX_1('nyef_ashstart', -1)
    GFX_1('nyef_ashstartmc', -1)
    sprite('ny450_04', 3)	# 16-18
    sprite('ny450_02', 3)	# 19-21
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('013_thunder_0')
    sprite('ny450_03', 3)	# 22-24
    sprite('ny450_04', 3)	# 25-27
    sprite('ny450_02', 3)	# 28-30
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('013_thunder_0')
    SFX_0('019_quake_1')
    sprite('ny450_03', 3)	# 31-33
    sprite('ny450_04', 3)	# 34-36
    sprite('ny450_02', 3)	# 37-39
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('013_thunder_0')
    SFX_0('019_quake_0')
    sprite('ny450_03', 3)	# 40-42
    sprite('ny450_04', 3)	# 43-45
    sprite('ny450_02', 3)	# 46-48
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('019_quake_1')
    SFX_0('013_thunder_0')
    sprite('ny450_03', 3)	# 49-51
    sprite('ny450_04', 3)	# 52-54
    sprite('ny450_02', 3)	# 55-57
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('013_thunder_0')
    sprite('ny450_03', 3)	# 58-60
    sprite('ny450_04', 3)	# 61-63
    sprite('ny450_02', 3)	# 64-66
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('013_thunder_0')
    sprite('ny450_03', 3)	# 67-69
    sprite('ny450_04', 3)	# 70-72
    sprite('ny450_02', 3)	# 73-75
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    SFX_0('013_thunder_0')
    sprite('ny450_03', 3)	# 76-78
    sprite('ny450_04', 3)	# 79-81
    sprite('ny450_02', 3)	# 82-84
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    sprite('ny450_03', 3)	# 85-87
    sprite('ny450_04', 3)	# 88-90
    sprite('ny450_02', 3)	# 91-93
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    sprite('ny450_03', 3)	# 94-96
    sprite('ny450_04', 3)	# 97-99
    sprite('ny450_02', 3)	# 100-102
    GFX_1('nyef_ash_front', 0)
    GFX_1('nyef_ash', 1)
    sprite('ny450_03', 3)	# 103-105
    sprite('ny450_04', 3)	# 106-108
    sprite('ny450_02', 3)	# 109-111
    sprite('ny450_03', 3)	# 112-114
    sprite('ny450_04', 3)	# 115-117
    sprite('ny450_05', 3)	# 118-120
    sprite('ny450_06', 3)	# 121-123	 **attackbox here**
    SFX_3('nyse_30')
    sprite('ny450_07', 3)	# 124-126	 **attackbox here**
    sprite('ny450_08', 3)	# 127-129	 **attackbox here**
    sprite('ny450_06', 3)	# 130-132	 **attackbox here**
    setInvincible(0)
    Unknown23027()
    sprite('ny450_07', 3)	# 133-135	 **attackbox here**
    sprite('ny450_08', 3)	# 136-138	 **attackbox here**
    sprite('ny450_09', 4)	# 139-142
    sprite('ny450_10', 4)	# 143-146
    sprite('ny450_11', 4)	# 147-150
    sprite('ny450_12', 4)	# 151-154

@State
def AstralHeatCatch():

    def upon_IMMEDIATE():
        Unknown17011('AstralHeatExe', 6, 0, 0)
        setInvincible(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown11045(0)
        AttackLevel_(0)
        Damage(0)
        Unknown11084(1)
        Unknown23088(1, 1)
        Unknown11023(1)
        Unknown2054(1)
        Unknown11064(1)
        Unknown2019(-500)
        Unknown13024(0)
        Unknown30061(0)
    sprite('ny450_06', 3)	# 1-3	 **attackbox here**
    sprite('ny450_07', 3)	# 4-6	 **attackbox here**
    sprite('ny450_08', 3)	# 7-9	 **attackbox here**
    sprite('ny450_06', 3)	# 10-12	 **attackbox here**
    setInvincible(0)
    sprite('ny450_07', 3)	# 13-15	 **attackbox here**
    sprite('ny450_08', 3)	# 16-18	 **attackbox here**
    sprite('ny450_09', 4)	# 19-22
    sprite('ny450_10', 4)	# 23-26
    sprite('ny450_11', 4)	# 27-30
    sprite('ny450_12', 4)	# 31-34

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        AttackLevel_(0)
        Damage(0)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        AirPushbackX(100)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(5)
        Hitstop(0)
        Unknown11001(1000, 1000, 1000)
        AirUntechableTime(1000)
        Unknown11069('AstralHeatExe')
    sprite('ny450_06', 25)	# 1-25	 **attackbox here**
    Unknown23027()
    Unknown5000(8, 0)
    Unknown5001('0200000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('ny450_06', 3)	# 26-28	 **attackbox here**
    Unknown23157(0)
    RefreshMultihit()
    GFX_1('nyef_ashlock', 0)
    GFX_1('nyef_ashmc', 2)
    GFX_1('nyef_whitelight', 101)
    sprite('ny450_07', 3)	# 29-31	 **attackbox here**
    tag_voice(0, 'bny291_0', 'bny291_1', '', '')
    sprite('ny450_08', 3)	# 32-34	 **attackbox here**
    sprite('ny450_06', 3)	# 35-37	 **attackbox here**
    sprite('ny450_07', 3)	# 38-40	 **attackbox here**
    sprite('ny450_08', 3)	# 41-43	 **attackbox here**
    SFX_0('015_blaze_1')
    sprite('ny450_06', 3)	# 44-46	 **attackbox here**
    SFX_0('015_blaze_1')
    sprite('ny450_07', 3)	# 47-49	 **attackbox here**
    sprite('ny450_08', 3)	# 50-52	 **attackbox here**
    sprite('ny450_06', 3)	# 53-55	 **attackbox here**
    sprite('ny450_07', 3)	# 56-58	 **attackbox here**
    sprite('ny450_08', 3)	# 59-61	 **attackbox here**
    sprite('ny450_06', 3)	# 62-64	 **attackbox here**
    sprite('ny450_07', 3)	# 65-67	 **attackbox here**
    sprite('ny450_08', 3)	# 68-70	 **attackbox here**
    sprite('ny450_06', 3)	# 71-73	 **attackbox here**
    SFX_0('015_blaze_1')
    sprite('ny450_07', 3)	# 74-76	 **attackbox here**
    SFX_0('015_blaze_1')
    sprite('ny450_08', 3)	# 77-79	 **attackbox here**
    sprite('ny450_06', 3)	# 80-82	 **attackbox here**
    sprite('ny450_07', 3)	# 83-85	 **attackbox here**
    sprite('ny450_08', 3)	# 86-88	 **attackbox here**
    sprite('ny450_06', 3)	# 89-91	 **attackbox here**
    sprite('ny450_07', 3)	# 92-94	 **attackbox here**
    sprite('ny450_08', 3)	# 95-97	 **attackbox here**
    sprite('ny450_06', 3)	# 98-100	 **attackbox here**
    sprite('ny450_07', 3)	# 101-103	 **attackbox here**
    SFX_0('015_blaze_1')
    sprite('ny450_08', 3)	# 104-106	 **attackbox here**
    SFX_0('015_blaze_1')
    sprite('ny450_06', 3)	# 107-109	 **attackbox here**
    sprite('ny450_07', 3)	# 110-112	 **attackbox here**
    sprite('ny450_08', 3)	# 113-115	 **attackbox here**
    sprite('null', 10)	# 116-125
    GFX_0('StartWhite', -1)
    Unknown23084(1)
    sprite('null', 10)	# 126-135
    Unknown1007(2800000)
    Unknown20001(1)
    sprite('null', 562)	# 136-697
    Unknown23024(3)
    GFX_0('NY_AHAnime', -1)
    Unknown23088(1, 1)
    sprite('vrnyef_astdamagedmy', 130)	# 698-827	 **attackbox here**
    Unknown13(1)
    GFX_0('FinishWhite', -1)
    Unknown23024(2)
    GFX_0('AstralLookAtMeDummy', -1)
    Unknown38(5, 1)
    SFX_0('025_cleanhit_slash')
    RefreshMultihit()
    Damage(56000)
    Unknown11064(3)
    Unknown11056(3)
    Unknown11023(1)
    YImpluseBeforeWallbounce(2000)
    Hitstop(20)
    Unknown11001(0, 0, 0)
    GFX_0('AstrakFinishPtc', -1)
    sprite('ny020_06', 3)	# 828-830
    teleportRelativeX(-128000)
    setGravity(1000)
    sendToLabelUpon(2, 17)
    sprite('ny020_07', 3)	# 831-833
    sprite('ny020_06', 3)	# 834-836
    sprite('ny020_07', 3)	# 837-839
    sprite('ny020_06', 3)	# 840-842
    sprite('ny020_07', 3)	# 843-845
    sprite('ny020_06', 3)	# 846-848
    sprite('ny020_07', 3)	# 849-851
    sprite('ny020_06', 3)	# 852-854
    sprite('ny020_07', 3)	# 855-857
    sprite('ny020_06', 3)	# 858-860
    sprite('ny020_07', 3)	# 861-863
    sprite('ny020_06', 3)	# 864-866
    sprite('ny020_07', 3)	# 867-869
    sprite('ny020_06', 3)	# 870-872
    sprite('ny020_07', 3)	# 873-875
    sprite('ny020_06', 3)	# 876-878
    sprite('ny020_07', 3)	# 879-881
    sprite('ny020_06', 3)	# 882-884
    sprite('ny020_07', 32767)	# 885-33651
    label(17)
    sprite('ny024_00', 4)	# 33652-33655
    SFX_0('205_runjump_garden_0')
    Unknown13(5)
    Unknown2001()
    SLOT_61 = 1
    Unknown20000(1)
    Unknown20004(1)
    Unknown20001(0)
    sprite('ny024_01', 4)	# 33656-33659
    sprite('ny024_02', 4)	# 33660-33663
    sprite('ny024_03', 4)	# 33664-33667
    sprite('ny024_04', 4)	# 33668-33671

@Subroutine
def MouthTableInit():
    Unknown18011('bny000', 12641, 25392, 24885, 12337, 13667, 12641, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny500', 12643, 12641, 25392, 12337, 12641, 25392, 12337, 12641, 25392, 12339, 12641, 25392, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny501', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13923, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny502', 12643, 14433, 14435, 14433, 14435, 14433, 14179, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny503', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 12643, 14385, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny504', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13667, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny505', 12643, 14433, 14435, 14433, 13923, 24888, 25400, 24888, 25400, 14393, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny520', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13923, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny521', 12643, 12641, 25392, 24885, 12337, 13667, 12641, 25392, 13619, 14433, 14435, 14433, 14435, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny522', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 12643, 14385, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny523', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13667, 24888, 25400, 24888, 25400, 12849, 24888, 25400, 24888, 25400, 14392, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny524', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 24883, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 14387, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny525', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13923, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny402_0', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny402_1', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny403_0', 12641, 25392, 24885, 12337, 13667, 12641, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny403_1', 12641, 25392, 24885, 12337, 13667, 12641, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny601bes', 12643, 14177, 14179, 12641, 25394, 14135, 14433, 14435, 14433, 14435, 14433, 14179, 24888, 13361, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13155, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600bhz', 12643, 14433, 14435, 14433, 14435, 24888, 25400, 24888, 25400, 12337, 24888, 12849, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600bno', 12643, 14433, 14435, 14433, 13411, 24888, 25400, 24888, 25400, 14390, 14433, 14435, 14433, 13411, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600brg', 12643, 14433, 14435, 14433, 12643, 14384, 14433, 14435, 14433, 14435, 12641, 25396, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 12337, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600pla', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 24880, 13617, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600pmi', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny601rwi', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 24880, 25400, 24888, 25400, 24888, 25400, 14387, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600umi', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny600uva', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny602bno', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny602uva', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny701bes', 12643, 14433, 14435, 14433, 14435, 14433, 13667, 24888, 13361, 14435, 14433, 12899, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700bhz', 12643, 14433, 14435, 14433, 14435, 24888, 25400, 24888, 25400, 12337, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700bno', 12643, 14433, 14435, 14433, 13667, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700brg', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 24884, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 14390, 12641, 25396, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700pla', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13923, 24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700pmi', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700rwi', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13667, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700umi', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 12643, 12336, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bny700uva', 12643, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14179, 24888, 25400, 24888, 25400, 24888, 25400, 14387, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
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
    PartnerChar('brg')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bhz')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('bno')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uva')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(180)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('ny300_00', 4)	# 2-5	 **attackbox here**
    sprite('ny300_01', 4)	# 6-9	 **attackbox here**
    if random_(2, 0, 66):
        Unknown7006('bny501', 100, 897150562, 13360, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        Unknown2037(1)
    sprite('ny300_02', 6)	# 10-15	 **attackbox here**
    sprite('ny300_03', 6)	# 16-21	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 22-41	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 42-61	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 62-81	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 82-101	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 102-121	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 122-141	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    if SLOT_2:
        SFX_1('bny500')
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 142-161	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 162-181	 **attackbox here**
    sprite('ny300_04', 1)	# 182-182	 **attackbox here**
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 183-188	 **attackbox here**
    sprite('ny300_06', 6)	# 189-194	 **attackbox here**
    sprite('ny300_07', 6)	# 195-200	 **attackbox here**
    sprite('ny300_08', 8)	# 201-208	 **attackbox here**
    sprite('ny300_09', 20)	# 209-228	 **attackbox here**
    Unknown23018(1)
    sprite('ny300_10', 4)	# 229-232	 **attackbox here**
    sprite('ny300_11', 4)	# 233-236	 **attackbox here**
    loopRest()
    label(1)
    sprite('ny000_00', 6)	# 237-242
    sprite('ny000_01', 6)	# 243-248
    sprite('ny000_02', 6)	# 249-254
    sprite('ny000_03', 6)	# 255-260
    sprite('ny000_04', 6)	# 261-266
    sprite('ny000_05', 6)	# 267-272
    sprite('ny000_06', 6)	# 273-278
    sprite('ny000_07', 6)	# 279-284
    sprite('ny000_08', 6)	# 285-290
    sprite('ny000_09', 6)	# 291-296
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ny600_00', 6)	# 297-302
    teleportRelativeY(640000)
    setGravity(57)
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 303-308
    sprite('ny600_02', 6)	# 309-314
    sprite('ny600_00', 6)	# 315-320
    sprite('ny600_01', 6)	# 321-326
    sprite('ny600_02', 6)	# 327-332
    sprite('ny600_00', 6)	# 333-338
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 339-344
    sprite('ny600_02', 6)	# 345-350
    sprite('ny600_00', 6)	# 351-356
    sprite('ny600_01', 6)	# 357-362
    sprite('ny600_02', 6)	# 363-368
    sprite('ny600_00', 6)	# 369-374
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 375-380
    sprite('ny600_02', 6)	# 381-386
    sprite('ny600_00', 6)	# 387-392
    sprite('ny600_01', 6)	# 393-398
    sprite('ny600_02', 6)	# 399-404
    sprite('ny600_00', 6)	# 405-410
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 411-416
    sprite('ny600_02', 6)	# 417-422
    sprite('ny600_00', 6)	# 423-428
    sprite('ny600_01', 6)	# 429-434
    sprite('ny600_02', 6)	# 435-440
    sprite('ny600_03', 6)	# 441-446
    SFX_0('019_cloth_a')
    sprite('ny600_04', 6)	# 447-452
    SFX_0('201_walk_garden_0')
    sprite('ny600_05', 6)	# 453-458
    Unknown1084(1)
    Unknown8000(0, 1, 1)
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny600_06', 6)	# 459-464
    sprite('ny600_07', 6)	# 465-470
    sprite('ny600_08', 6)	# 471-476
    sprite('ny600_09', 6)	# 477-482
    sprite('ny600_10', 6)	# 483-488
    sprite('ny600_11', 6)	# 489-494
    sprite('ny600_12', 6)	# 495-500
    sprite('ny600_13', 6)	# 501-506
    sprite('ny600_14', 6)	# 507-512
    sprite('ny600_11', 6)	# 513-518
    Unknown7006('bny502', 100, 897150562, 13104, 0, 0, 100, 897150562, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ny600_12', 6)	# 519-524
    sprite('ny600_13', 6)	# 525-530
    sprite('ny600_14', 6)	# 531-536
    label(11)
    sprite('ny600_11', 6)	# 537-542
    sprite('ny600_12', 6)	# 543-548
    sprite('ny600_13', 6)	# 549-554
    sprite('ny600_14', 6)	# 555-560
    if SLOT_97:
        _gotolabel(11)
    sprite('ny600_11', 6)	# 561-566
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('ny600_12', 6)	# 567-572
    sprite('ny600_13', 3)	# 573-575
    sprite('ny600_13', 3)	# 576-578
    SFX_3('nyse_28')
    sprite('ny600_14', 6)	# 579-584
    sprite('ny600_11', 6)	# 585-590
    sprite('ny600_12', 6)	# 591-596
    sprite('ny600_13', 6)	# 597-602
    sprite('ny600_14', 6)	# 603-608
    sprite('ny600_15', 6)	# 609-614
    Unknown23118(0)
    Unknown23117(16777215, 30)
    GFX_1('nyef_entrylightA', 0)
    SFX_0('019_cloth_a')
    SFX_3('nyse_03')
    sprite('ny600_16', 12)	# 615-626
    sprite('ny600_17', 6)	# 627-632
    GFX_1('nyef_entrylightB', 0)
    sprite('ny600_18', 6)	# 633-638
    sprite('ny600_19', 6)	# 639-644
    SFX_0('022_magiccircle_a')
    sprite('ny600_20', 6)	# 645-650
    sprite('ny600_21', 6)	# 651-656
    sprite('ny600_22', 6)	# 657-662
    sprite('ny600_23', 6)	# 663-668
    Unknown21011(120)
    label(12)
    sprite('ny000_00', 6)	# 669-674
    sprite('ny000_01', 6)	# 675-680
    sprite('ny000_02', 6)	# 681-686
    sprite('ny000_03', 6)	# 687-692
    sprite('ny000_04', 6)	# 693-698
    sprite('ny000_05', 6)	# 699-704
    sprite('ny000_06', 6)	# 705-710
    sprite('ny000_07', 6)	# 711-716
    sprite('ny000_08', 6)	# 717-722
    sprite('ny000_09', 6)	# 723-728
    gotoLabel(12)
    loopRest()
    ExitState()
    label(20)
    sprite('ny000_00', 1)	# 729-729
    SFX_1('bny700pmi')
    label(21)
    sprite('ny000_00', 6)	# 730-735
    sprite('ny000_01', 6)	# 736-741
    sprite('ny000_02', 6)	# 742-747
    sprite('ny000_03', 6)	# 748-753
    sprite('ny000_04', 6)	# 754-759
    sprite('ny000_05', 6)	# 760-765
    sprite('ny000_06', 6)	# 766-771
    sprite('ny000_07', 6)	# 772-777
    sprite('ny000_08', 6)	# 778-783
    sprite('ny000_09', 6)	# 784-789
    gotoLabel(21)
    ExitState()
    label(100)
    sprite('ny600_11', 6)	# 790-795
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ny600_12', 6)	# 796-801
    sprite('ny600_13', 6)	# 802-807
    sprite('ny600_14', 6)	# 808-813
    sprite('ny600_11', 6)	# 814-819
    sprite('ny600_12', 6)	# 820-825
    sprite('ny600_13', 6)	# 826-831
    sprite('ny600_14', 6)	# 832-837
    sprite('ny600_11', 6)	# 838-843
    SFX_1('bny600brg')
    sprite('ny600_12', 6)	# 844-849
    sprite('ny600_13', 6)	# 850-855
    sprite('ny600_14', 6)	# 856-861
    label(101)
    sprite('ny600_11', 6)	# 862-867
    sprite('ny600_12', 6)	# 868-873
    sprite('ny600_13', 6)	# 874-879
    sprite('ny600_14', 6)	# 880-885
    if SLOT_97:
        _gotolabel(101)
    sprite('ny600_11', 6)	# 886-891
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('ny600_12', 6)	# 892-897
    sprite('ny600_13', 3)	# 898-900
    sprite('ny600_13', 3)	# 901-903
    SFX_3('nyse_28')
    sprite('ny600_14', 6)	# 904-909
    sprite('ny600_11', 6)	# 910-915
    sprite('ny600_12', 6)	# 916-921
    sprite('ny600_13', 6)	# 922-927
    sprite('ny600_14', 6)	# 928-933
    sprite('ny600_15', 6)	# 934-939
    Unknown23118(0)
    Unknown23117(16777215, 30)
    GFX_1('nyef_entrylightA', 0)
    SFX_0('019_cloth_a')
    SFX_3('nyse_03')
    sprite('ny600_16', 12)	# 940-951
    sprite('ny600_17', 6)	# 952-957
    GFX_1('nyef_entrylightB', 0)
    sprite('ny600_18', 6)	# 958-963
    sprite('ny600_19', 6)	# 964-969
    SFX_0('022_magiccircle_a')
    sprite('ny600_20', 6)	# 970-975
    sprite('ny600_21', 6)	# 976-981
    sprite('ny600_22', 6)	# 982-987
    sprite('ny600_23', 6)	# 988-993
    Unknown21007(24, 40)
    Unknown21011(120)
    label(102)
    sprite('ny000_00', 6)	# 994-999
    sprite('ny000_01', 6)	# 1000-1005
    sprite('ny000_02', 6)	# 1006-1011
    sprite('ny000_03', 6)	# 1012-1017
    sprite('ny000_04', 6)	# 1018-1023
    sprite('ny000_05', 6)	# 1024-1029
    sprite('ny000_06', 6)	# 1030-1035
    sprite('ny000_07', 6)	# 1036-1041
    sprite('ny000_08', 6)	# 1042-1047
    sprite('ny000_09', 6)	# 1048-1053
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('ny000_00', 1)	# 1054-1054

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ny000_00', 6)	# 1055-1060
    sprite('ny000_01', 6)	# 1061-1066
    sprite('ny000_02', 6)	# 1067-1072
    sprite('ny000_03', 6)	# 1073-1078
    sprite('ny000_04', 6)	# 1079-1084
    sprite('ny000_05', 6)	# 1085-1090
    sprite('ny000_06', 6)	# 1091-1096
    sprite('ny000_07', 6)	# 1097-1102
    sprite('ny000_08', 6)	# 1103-1108
    sprite('ny000_09', 6)	# 1109-1114
    gotoLabel(111)
    label(112)
    sprite('ny300_04', 1)	# 1115-1115	 **attackbox here**
    SFX_1('bny601bes')
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 1116-1121	 **attackbox here**
    sprite('ny300_06', 6)	# 1122-1127	 **attackbox here**
    sprite('ny300_07', 6)	# 1128-1133	 **attackbox here**
    sprite('ny300_08', 8)	# 1134-1141	 **attackbox here**
    sprite('ny300_09', 60)	# 1142-1201	 **attackbox here**
    sprite('ny300_10', 4)	# 1202-1205	 **attackbox here**
    sprite('ny300_11', 4)	# 1206-1209	 **attackbox here**
    label(113)
    sprite('ny000_00', 6)	# 1210-1215
    sprite('ny000_01', 6)	# 1216-1221
    sprite('ny000_02', 6)	# 1222-1227
    sprite('ny000_03', 6)	# 1228-1233
    sprite('ny000_04', 6)	# 1234-1239
    sprite('ny000_05', 6)	# 1240-1245
    sprite('ny000_06', 6)	# 1246-1251
    sprite('ny000_07', 6)	# 1252-1257
    sprite('ny000_08', 6)	# 1258-1263
    sprite('ny000_09', 6)	# 1264-1269
    if SLOT_97:
        _gotolabel(113)
    sprite('ny000_00', 1)	# 1270-1270
    Unknown21007(24, 40)
    Unknown21011(120)
    label(114)
    sprite('ny000_00', 6)	# 1271-1276
    sprite('ny000_01', 6)	# 1277-1282
    sprite('ny000_02', 6)	# 1283-1288
    sprite('ny000_03', 6)	# 1289-1294
    sprite('ny000_04', 6)	# 1295-1300
    sprite('ny000_05', 6)	# 1301-1306
    sprite('ny000_06', 6)	# 1307-1312
    sprite('ny000_07', 6)	# 1313-1318
    sprite('ny000_08', 6)	# 1319-1324
    sprite('ny000_09', 6)	# 1325-1330
    gotoLabel(114)
    ExitState()
    label(120)
    sprite('ny064_02', 1)	# 1331-1331
    SFX_1('bny600bhz')
    label(121)
    sprite('ny064_02', 1)	# 1332-1332
    if SLOT_97:
        _gotolabel(121)
    sprite('ny064_02', 30)	# 1333-1362
    sprite('ny064_02', 32767)	# 1363-34129
    Unknown21007(24, 40)
    Unknown21011(120)
    ExitState()
    label(130)
    sprite('ny000_00', 1)	# 34130-34130

    def upon_40():
        clearUponHandler(40)
        SFX_1('bny601rwi')
        Unknown21011(280)
    label(131)
    sprite('ny000_00', 6)	# 34131-34136
    sprite('ny000_01', 6)	# 34137-34142
    sprite('ny000_02', 6)	# 34143-34148
    sprite('ny000_03', 6)	# 34149-34154
    sprite('ny000_04', 6)	# 34155-34160
    sprite('ny000_05', 6)	# 34161-34166
    sprite('ny000_06', 6)	# 34167-34172
    sprite('ny000_07', 6)	# 34173-34178
    sprite('ny000_08', 6)	# 34179-34184
    sprite('ny000_09', 6)	# 34185-34190
    gotoLabel(131)
    ExitState()
    label(140)
    sprite('ny600_00', 6)	# 34191-34196
    if SLOT_158:
        Unknown1000(-1465000)
    teleportRelativeY(640000)
    setGravity(57)
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 34197-34202
    sprite('ny600_02', 6)	# 34203-34208
    sprite('ny600_00', 6)	# 34209-34214
    sprite('ny600_01', 6)	# 34215-34220
    sprite('ny600_02', 6)	# 34221-34226
    sprite('ny600_00', 6)	# 34227-34232
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 34233-34238
    sprite('ny600_02', 6)	# 34239-34244
    sprite('ny600_00', 6)	# 34245-34250
    sprite('ny600_01', 6)	# 34251-34256
    sprite('ny600_02', 6)	# 34257-34262
    sprite('ny600_00', 6)	# 34263-34268
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 34269-34274
    sprite('ny600_02', 6)	# 34275-34280
    sprite('ny600_00', 6)	# 34281-34286
    sprite('ny600_01', 6)	# 34287-34292
    sprite('ny600_02', 6)	# 34293-34298
    sprite('ny600_00', 6)	# 34299-34304
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 34305-34310
    sprite('ny600_02', 6)	# 34311-34316
    sprite('ny600_00', 6)	# 34317-34322
    sprite('ny600_01', 6)	# 34323-34328
    sprite('ny600_02', 6)	# 34329-34334
    sprite('ny600_03', 6)	# 34335-34340
    SFX_0('019_cloth_a')
    sprite('ny600_04', 6)	# 34341-34346
    SFX_0('201_walk_garden_0')
    sprite('ny600_05', 6)	# 34347-34352
    Unknown1084(1)
    Unknown8000(0, 1, 1)
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny600_06', 6)	# 34353-34358
    sprite('ny600_07', 6)	# 34359-34364
    sprite('ny600_08', 6)	# 34365-34370
    sprite('ny600_09', 6)	# 34371-34376
    sprite('ny600_10', 6)	# 34377-34382
    sprite('ny600_11', 6)	# 34383-34388
    sprite('ny600_12', 6)	# 34389-34394
    sprite('ny600_13', 6)	# 34395-34400
    sprite('ny600_14', 6)	# 34401-34406
    sprite('ny600_11', 6)	# 34407-34412
    SFX_1('bny600bno')
    sprite('ny600_12', 6)	# 34413-34418
    sprite('ny600_13', 6)	# 34419-34424
    sprite('ny600_14', 6)	# 34425-34430
    label(141)
    sprite('ny600_11', 6)	# 34431-34436
    sprite('ny600_12', 6)	# 34437-34442
    sprite('ny600_13', 6)	# 34443-34448
    sprite('ny600_14', 6)	# 34449-34454
    if SLOT_97:
        _gotolabel(141)
    sprite('ny600_11', 6)	# 34455-34460
    sprite('ny600_12', 6)	# 34461-34466
    sprite('ny600_13', 6)	# 34467-34472
    sprite('ny600_14', 6)	# 34473-34478
    sprite('ny600_11', 6)	# 34479-34484
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    Unknown21007(24, 40)
    sprite('ny600_12', 6)	# 34485-34490
    sprite('ny600_13', 3)	# 34491-34493
    sprite('ny600_13', 3)	# 34494-34496
    SFX_3('nyse_28')
    sprite('ny600_14', 6)	# 34497-34502
    sprite('ny600_11', 6)	# 34503-34508
    sprite('ny600_12', 6)	# 34509-34514
    sprite('ny600_13', 6)	# 34515-34520
    sprite('ny600_14', 6)	# 34521-34526
    sprite('ny600_15', 6)	# 34527-34532
    Unknown23118(0)
    Unknown23117(16777215, 30)
    GFX_1('nyef_entrylightA', 0)
    SFX_0('019_cloth_a')
    SFX_3('nyse_03')
    sprite('ny600_16', 12)	# 34533-34544
    sprite('ny600_17', 6)	# 34545-34550
    GFX_1('nyef_entrylightB', 0)
    sprite('ny600_18', 6)	# 34551-34556
    sprite('ny600_19', 6)	# 34557-34562
    SFX_0('022_magiccircle_a')
    sprite('ny600_20', 6)	# 34563-34568
    sprite('ny600_21', 6)	# 34569-34574
    sprite('ny600_22', 6)	# 34575-34580
    sprite('ny600_23', 6)	# 34581-34586
    sprite('ny000_00', 6)	# 34587-34592
    Unknown21007(24, 39)
    SFX_1('bny602bno')
    sprite('ny000_01', 6)	# 34593-34598
    sprite('ny000_02', 6)	# 34599-34604
    sprite('ny000_03', 6)	# 34605-34610
    sprite('ny000_04', 6)	# 34611-34616
    sprite('ny000_05', 6)	# 34617-34622
    sprite('ny000_06', 6)	# 34623-34628
    sprite('ny000_07', 6)	# 34629-34634
    sprite('ny000_08', 6)	# 34635-34640
    sprite('ny000_09', 6)	# 34641-34646
    Unknown21011(120)
    label(142)
    sprite('ny000_00', 6)	# 34647-34652
    sprite('ny000_01', 6)	# 34653-34658
    sprite('ny000_02', 6)	# 34659-34664
    sprite('ny000_03', 6)	# 34665-34670
    sprite('ny000_04', 6)	# 34671-34676
    sprite('ny000_05', 6)	# 34677-34682
    sprite('ny000_06', 6)	# 34683-34688
    sprite('ny000_07', 6)	# 34689-34694
    sprite('ny000_08', 6)	# 34695-34700
    sprite('ny000_09', 6)	# 34701-34706
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('ny633_00', 1)	# 34707-34707	 **attackbox here**
    Unknown1000(-1230000)
    Unknown2019(100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(153)
    sprite('ny633_00', 6)	# 34708-34713	 **attackbox here**
    SFX_1('bny600uva')
    sprite('ny633_01', 6)	# 34714-34719	 **attackbox here**
    sprite('ny633_02', 6)	# 34720-34725	 **attackbox here**
    label(151)
    sprite('ny633_00', 6)	# 34726-34731	 **attackbox here**
    sprite('ny633_01', 6)	# 34732-34737	 **attackbox here**
    sprite('ny633_02', 6)	# 34738-34743	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('ny633_00', 6)	# 34744-34749	 **attackbox here**
    sprite('ny633_01', 6)	# 34750-34755	 **attackbox here**
    sprite('ny633_02', 6)	# 34756-34761	 **attackbox here**
    sprite('ny633_00', 6)	# 34762-34767	 **attackbox here**
    sprite('ny633_01', 6)	# 34768-34773	 **attackbox here**
    sprite('ny633_02', 6)	# 34774-34779	 **attackbox here**
    Unknown21007(24, 40)
    label(152)
    sprite('ny633_00', 6)	# 34780-34785	 **attackbox here**
    sprite('ny633_01', 6)	# 34786-34791	 **attackbox here**
    sprite('ny633_02', 6)	# 34792-34797	 **attackbox here**
    gotoLabel(152)
    label(153)
    sprite('ny633_03', 4)	# 34798-34801	 **attackbox here**
    sprite('ny633_04', 6)	# 34802-34807	 **attackbox here**
    sprite('ny633_05', 6)	# 34808-34813	 **attackbox here**
    SFX_1('bny602uva')
    sprite('ny633_06', 6)	# 34814-34819	 **attackbox here**
    Unknown23018(1)
    label(154)
    sprite('ny633_07', 6)	# 34820-34825	 **attackbox here**
    sprite('ny633_08', 6)	# 34826-34831	 **attackbox here**
    sprite('ny633_09', 6)	# 34832-34837	 **attackbox here**
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('ny000_00', 6)	# 34838-34843
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ny000_01', 6)	# 34844-34849
    sprite('ny000_02', 6)	# 34850-34855
    sprite('ny000_03', 6)	# 34856-34861
    sprite('ny300_04', 1)	# 34862-34862	 **attackbox here**
    SFX_1('bny600umi')
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 34863-34868	 **attackbox here**
    sprite('ny300_06', 6)	# 34869-34874	 **attackbox here**
    sprite('ny300_07', 6)	# 34875-34880	 **attackbox here**
    sprite('ny300_08', 8)	# 34881-34888	 **attackbox here**
    sprite('ny300_09', 90)	# 34889-34978	 **attackbox here**
    sprite('ny300_10', 4)	# 34979-34982	 **attackbox here**
    sprite('ny300_11', 4)	# 34983-34986	 **attackbox here**
    label(161)
    sprite('ny000_00', 6)	# 34987-34992
    sprite('ny000_01', 6)	# 34993-34998
    sprite('ny000_02', 6)	# 34999-35004
    sprite('ny000_03', 6)	# 35005-35010
    sprite('ny000_04', 6)	# 35011-35016
    sprite('ny000_05', 6)	# 35017-35022
    sprite('ny000_06', 6)	# 35023-35028
    sprite('ny000_07', 6)	# 35029-35034
    sprite('ny000_08', 6)	# 35035-35040
    sprite('ny000_09', 6)	# 35041-35046
    if SLOT_97:
        _gotolabel(161)
    sprite('ny000_00', 1)	# 35047-35047
    Unknown21007(24, 40)
    Unknown21011(120)
    label(162)
    sprite('ny000_00', 6)	# 35048-35053
    sprite('ny000_01', 6)	# 35054-35059
    sprite('ny000_02', 6)	# 35060-35065
    sprite('ny000_03', 6)	# 35066-35071
    sprite('ny000_04', 6)	# 35072-35077
    sprite('ny000_05', 6)	# 35078-35083
    sprite('ny000_06', 6)	# 35084-35089
    sprite('ny000_07', 6)	# 35090-35095
    sprite('ny000_08', 6)	# 35096-35101
    sprite('ny000_09', 6)	# 35102-35107
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('ny000_00', 6)	# 35108-35113
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ny000_01', 6)	# 35114-35119
    sprite('ny000_02', 6)	# 35120-35125
    sprite('ny000_03', 6)	# 35126-35131
    sprite('ny300_04', 1)	# 35132-35132	 **attackbox here**
    SFX_1('bny600pla')
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 35133-35138	 **attackbox here**
    sprite('ny300_06', 6)	# 35139-35144	 **attackbox here**
    sprite('ny300_07', 6)	# 35145-35150	 **attackbox here**
    sprite('ny300_08', 8)	# 35151-35158	 **attackbox here**
    sprite('ny300_09', 90)	# 35159-35248	 **attackbox here**
    sprite('ny300_10', 4)	# 35249-35252	 **attackbox here**
    sprite('ny300_11', 4)	# 35253-35256	 **attackbox here**
    label(171)
    sprite('ny000_00', 6)	# 35257-35262
    sprite('ny000_01', 6)	# 35263-35268
    sprite('ny000_02', 6)	# 35269-35274
    sprite('ny000_03', 6)	# 35275-35280
    sprite('ny000_04', 6)	# 35281-35286
    sprite('ny000_05', 6)	# 35287-35292
    sprite('ny000_06', 6)	# 35293-35298
    sprite('ny000_07', 6)	# 35299-35304
    sprite('ny000_08', 6)	# 35305-35310
    sprite('ny000_09', 6)	# 35311-35316
    if SLOT_97:
        _gotolabel(171)
    sprite('ny000_00', 1)	# 35317-35317
    Unknown21007(24, 40)
    Unknown21011(260)
    label(172)
    sprite('ny000_00', 6)	# 35318-35323
    sprite('ny000_01', 6)	# 35324-35329
    sprite('ny000_02', 6)	# 35330-35335
    sprite('ny000_03', 6)	# 35336-35341
    sprite('ny000_04', 6)	# 35342-35347
    sprite('ny000_05', 6)	# 35348-35353
    sprite('ny000_06', 6)	# 35354-35359
    sprite('ny000_07', 6)	# 35360-35365
    sprite('ny000_08', 6)	# 35366-35371
    sprite('ny000_09', 6)	# 35372-35377
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('ny000_00', 6)	# 35378-35383
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ny000_01', 6)	# 35384-35389
    sprite('ny000_02', 6)	# 35390-35395
    sprite('ny000_03', 6)	# 35396-35401
    sprite('ny300_00', 4)	# 35402-35405	 **attackbox here**
    sprite('ny300_01', 4)	# 35406-35409	 **attackbox here**
    sprite('ny300_02', 6)	# 35410-35415	 **attackbox here**
    sprite('ny300_03', 6)	# 35416-35421	 **attackbox here**
    sprite('ny300_04', 10)	# 35422-35431	 **attackbox here**
    SFX_1('bny600pmi')
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 35432-35437	 **attackbox here**
    sprite('ny300_06', 6)	# 35438-35443	 **attackbox here**
    sprite('ny300_07', 6)	# 35444-35449	 **attackbox here**
    sprite('ny300_08', 8)	# 35450-35457	 **attackbox here**
    sprite('ny300_09', 90)	# 35458-35547	 **attackbox here**
    sprite('ny300_10', 4)	# 35548-35551	 **attackbox here**
    sprite('ny300_11', 4)	# 35552-35555	 **attackbox here**
    label(181)
    sprite('ny000_00', 6)	# 35556-35561
    sprite('ny000_01', 6)	# 35562-35567
    sprite('ny000_02', 6)	# 35568-35573
    sprite('ny000_03', 6)	# 35574-35579
    sprite('ny000_04', 6)	# 35580-35585
    sprite('ny000_05', 6)	# 35586-35591
    sprite('ny000_06', 6)	# 35592-35597
    sprite('ny000_07', 6)	# 35598-35603
    sprite('ny000_08', 6)	# 35604-35609
    sprite('ny000_09', 6)	# 35610-35615
    if SLOT_97:
        _gotolabel(181)
    sprite('ny000_00', 1)	# 35616-35616
    Unknown21007(24, 40)
    Unknown21011(300)
    label(182)
    sprite('ny000_00', 6)	# 35617-35622
    sprite('ny000_01', 6)	# 35623-35628
    sprite('ny000_02', 6)	# 35629-35634
    sprite('ny000_03', 6)	# 35635-35640
    sprite('ny000_04', 6)	# 35641-35646
    sprite('ny000_05', 6)	# 35647-35652
    sprite('ny000_06', 6)	# 35653-35658
    sprite('ny000_07', 6)	# 35659-35664
    sprite('ny000_08', 6)	# 35665-35670
    sprite('ny000_09', 6)	# 35671-35676
    gotoLabel(182)
    ExitState()
    label(991)
    sprite('ny000_00', 1)	# 35677-35677
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ny000_00', 6)	# 35678-35683
    sprite('ny000_01', 6)	# 35684-35689
    sprite('ny000_02', 6)	# 35690-35695
    sprite('ny000_03', 6)	# 35696-35701
    sprite('ny000_04', 6)	# 35702-35707
    sprite('ny000_05', 6)	# 35708-35713
    sprite('ny000_06', 6)	# 35714-35719
    sprite('ny000_07', 6)	# 35720-35725
    sprite('ny000_08', 6)	# 35726-35731
    sprite('ny000_09', 6)	# 35732-35737
    gotoLabel(992)
    label(993)
    sprite('ny410_02', 4)	# 35738-35741

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(995)

    def upon_STATE_END():
        Unknown2019(0)
        Unknown3038(1)
        Unknown3001(255)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown3001(255)
    Unknown3004(-20)
    physicsXImpulse(-51000)
    physicsYImpulse(18800)
    setGravity(1500)
    Unknown8002()
    sprite('ny410_03', 4)	# 35742-35745
    label(994)
    sprite('ny410_04', 3)	# 35746-35748
    sprite('ny410_05', 3)	# 35749-35751
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 35752-35754
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

    def upon_3():
        SLOT_58 = 1
        Unknown48('19000000020000003400000018000000020000003a000000')
        if SLOT_52:
            if PartnerChar('brg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('ny610_00', 5)	# 4-8
    sprite('ny610_01', 5)	# 9-13
    sprite('ny610_02', 5)	# 14-18
    sprite('ny610_03', 5)	# 19-23
    sprite('ny610_04', 4)	# 24-27
    sprite('ny610_05', 4)	# 28-31
    sprite('ny610_06', 4)	# 32-35
    sprite('ny610_07', 4)	# 36-39
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bny524', 100, 897150562, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bny402_0', 100, 880373346, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bny520', 100, 897150562, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny610_08', 4)	# 40-43
    sprite('ny610_09', 4)	# 44-47
    sprite('ny610_10', 5)	# 48-52
    GFX_1('nyef_entrymc', -1)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny610_11', 5)	# 53-57
    sprite('ny610_12', 5)	# 58-62
    sprite('ny610_13', 5)	# 63-67
    Unknown23018(1)
    label(1)
    sprite('ny610_11', 5)	# 68-72
    GFX_1('nyef_entrymc', -1)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny610_12', 5)	# 73-77
    sprite('ny610_13', 5)	# 78-82
    sprite('ny610_11', 5)	# 83-87
    sprite('ny610_12', 5)	# 88-92
    sprite('ny610_13', 5)	# 93-97
    loopRest()
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ny611_00', 6)	# 98-103
    sprite('ny611_01', 6)	# 104-109
    sprite('ny611_02', 6)	# 110-115
    sprite('ny611_03', 6)	# 116-121
    sprite('ny611_04', 6)	# 122-127
    sprite('ny611_05', 6)	# 128-133
    sprite('ny611_06', 6)	# 134-139
    sprite('ny611_07', 6)	# 140-145
    sprite('ny611_08', 6)	# 146-151
    sprite('ny611_09', 6)	# 152-157
    sprite('ny611_10', 6)	# 158-163
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bny524', 100, 897150562, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bny402_0', 100, 880373346, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bny522', 100, 897150562, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ny611_11', 7)	# 164-170
    GFX_1('nyef_entrymc', 0)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 171-177
    sprite('ny611_13', 7)	# 178-184
    sprite('ny611_14', 7)	# 185-191
    GFX_1('nyef_entrymc', 0)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny611_15', 7)	# 192-198
    sprite('ny611_16', 7)	# 199-205
    sprite('ny611_17', 7)	# 206-212
    GFX_1('nyef_entrymc', 0)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny611_14', 7)	# 213-219
    sprite('ny611_15', 7)	# 220-226
    sprite('ny611_16', 7)	# 227-233
    GFX_1('nyef_entrymc', 0)
    Unknown23018(1)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny611_17', 7)	# 234-240
    label(11)
    sprite('ny611_14', 7)	# 241-247
    sprite('ny611_15', 7)	# 248-254
    GFX_1('nyef_entrymc', 0)
    if SLOT_158:
        SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 255-261
    sprite('ny611_17', 7)	# 262-268
    loopRest()
    gotoLabel(11)
    ExitState()
    label(100)
    sprite('ny615_00', 6)	# 269-274	 **attackbox here**
    sprite('ny615_01', 6)	# 275-280	 **attackbox here**
    sprite('ny615_02', 6)	# 281-286	 **attackbox here**
    sprite('ny615_03', 8)	# 287-294	 **attackbox here**
    sprite('ny615_04', 6)	# 295-300	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 6)	# 301-306	 **attackbox here**
    sprite('ny615_06', 6)	# 307-312	 **attackbox here**
    sprite('ny615_07', 6)	# 313-318	 **attackbox here**
    sprite('ny615_08', 6)	# 319-324	 **attackbox here**
    sprite('ny615_09', 5)	# 325-329	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 330-334	 **attackbox here**
    sprite('ny615_11', 5)	# 335-339	 **attackbox here**
    SFX_1('bny700brg')
    sprite('ny615_09', 5)	# 340-344	 **attackbox here**
    sprite('ny615_10', 5)	# 345-349	 **attackbox here**
    sprite('ny615_11', 5)	# 350-354	 **attackbox here**
    label(101)
    sprite('ny615_09', 5)	# 355-359	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 360-364	 **attackbox here**
    sprite('ny615_11', 5)	# 365-369	 **attackbox here**
    sprite('ny615_09', 5)	# 370-374	 **attackbox here**
    sprite('ny615_10', 5)	# 375-379	 **attackbox here**
    sprite('ny615_11', 5)	# 380-384	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('ny615_09', 5)	# 385-389	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 390-394	 **attackbox here**
    sprite('ny615_11', 5)	# 395-399	 **attackbox here**
    sprite('ny615_09', 5)	# 400-404	 **attackbox here**
    sprite('ny615_10', 5)	# 405-409	 **attackbox here**
    sprite('ny615_11', 5)	# 410-414	 **attackbox here**
    Unknown21011(180)
    Unknown21007(24, 40)
    label(102)
    sprite('ny615_09', 5)	# 415-419	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 420-424	 **attackbox here**
    sprite('ny615_11', 5)	# 425-429	 **attackbox here**
    sprite('ny615_09', 5)	# 430-434	 **attackbox here**
    sprite('ny615_10', 5)	# 435-439	 **attackbox here**
    sprite('ny615_11', 5)	# 440-444	 **attackbox here**
    gotoLabel(102)
    label(110)
    sprite('ny611_00', 6)	# 445-450
    sprite('ny611_01', 6)	# 451-456
    sprite('ny611_02', 6)	# 457-462
    sprite('ny611_03', 6)	# 463-468
    sprite('ny611_04', 6)	# 469-474
    sprite('ny611_05', 6)	# 475-480
    sprite('ny611_06', 6)	# 481-486
    sprite('ny611_07', 6)	# 487-492
    sprite('ny611_08', 6)	# 493-498
    sprite('ny611_09', 6)	# 499-504
    sprite('ny611_10', 6)	# 505-510
    SFX_1('bny700bno')
    sprite('ny611_11', 7)	# 511-517
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 518-524
    sprite('ny611_13', 7)	# 525-531
    label(111)
    sprite('ny611_14', 7)	# 532-538
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_15', 7)	# 539-545
    sprite('ny611_16', 7)	# 546-552
    sprite('ny611_17', 7)	# 553-559
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_14', 7)	# 560-566
    sprite('ny611_15', 7)	# 567-573
    sprite('ny611_16', 7)	# 574-580
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_17', 7)	# 581-587
    if SLOT_97:
        _gotolabel(111)
    sprite('ny611_14', 1)	# 588-588
    Unknown21007(24, 40)
    Unknown21011(500)
    label(112)
    sprite('ny611_14', 7)	# 589-595
    sprite('ny611_15', 7)	# 596-602
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 603-609
    sprite('ny611_17', 7)	# 610-616
    loopRest()
    gotoLabel(112)
    label(120)
    sprite('ny000_00', 1)	# 617-617

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ny000_00', 6)	# 618-623
    sprite('ny000_01', 6)	# 624-629
    sprite('ny000_02', 6)	# 630-635
    sprite('ny000_03', 6)	# 636-641
    sprite('ny000_04', 6)	# 642-647
    sprite('ny000_05', 6)	# 648-653
    sprite('ny000_06', 6)	# 654-659
    sprite('ny000_07', 6)	# 660-665
    sprite('ny000_08', 6)	# 666-671
    sprite('ny000_09', 6)	# 672-677
    gotoLabel(121)
    label(122)
    sprite('ny615_00', 6)	# 678-683	 **attackbox here**
    sprite('ny615_01', 6)	# 684-689	 **attackbox here**
    sprite('ny615_02', 6)	# 690-695	 **attackbox here**
    SFX_1('bny701bes')
    sprite('ny615_03', 8)	# 696-703	 **attackbox here**
    sprite('ny615_04', 6)	# 704-709	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 6)	# 710-715	 **attackbox here**
    sprite('ny615_06', 6)	# 716-721	 **attackbox here**
    sprite('ny615_07', 6)	# 722-727	 **attackbox here**
    sprite('ny615_08', 6)	# 728-733	 **attackbox here**
    sprite('ny615_09', 5)	# 734-738	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 739-743	 **attackbox here**
    sprite('ny615_11', 5)	# 744-748	 **attackbox here**
    Unknown23018(1)
    label(123)
    sprite('ny615_09', 5)	# 749-753	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 754-758	 **attackbox here**
    sprite('ny615_11', 5)	# 759-763	 **attackbox here**
    sprite('ny615_09', 5)	# 764-768	 **attackbox here**
    sprite('ny615_10', 5)	# 769-773	 **attackbox here**
    sprite('ny615_11', 5)	# 774-778	 **attackbox here**
    gotoLabel(123)
    label(130)
    sprite('ny615_00', 6)	# 779-784	 **attackbox here**
    sprite('ny615_01', 6)	# 785-790	 **attackbox here**
    sprite('ny615_02', 6)	# 791-796	 **attackbox here**
    SFX_1('bny700bhz')
    sprite('ny615_03', 8)	# 797-804	 **attackbox here**
    sprite('ny615_04', 6)	# 805-810	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 6)	# 811-816	 **attackbox here**
    sprite('ny615_06', 6)	# 817-822	 **attackbox here**
    sprite('ny615_07', 6)	# 823-828	 **attackbox here**
    sprite('ny615_08', 6)	# 829-834	 **attackbox here**
    sprite('ny615_09', 5)	# 835-839	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 840-844	 **attackbox here**
    sprite('ny615_11', 5)	# 845-849	 **attackbox here**
    sprite('ny615_09', 5)	# 850-854	 **attackbox here**
    sprite('ny615_10', 5)	# 855-859	 **attackbox here**
    sprite('ny615_11', 5)	# 860-864	 **attackbox here**
    label(131)
    sprite('ny615_09', 5)	# 865-869	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 870-874	 **attackbox here**
    sprite('ny615_11', 5)	# 875-879	 **attackbox here**
    sprite('ny615_09', 5)	# 880-884	 **attackbox here**
    sprite('ny615_10', 5)	# 885-889	 **attackbox here**
    sprite('ny615_11', 5)	# 890-894	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('ny615_09', 1)	# 895-895	 **attackbox here**
    Unknown21011(330)
    Unknown21007(24, 40)
    label(132)
    sprite('ny615_09', 5)	# 896-900	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 901-905	 **attackbox here**
    sprite('ny615_11', 5)	# 906-910	 **attackbox here**
    sprite('ny615_09', 5)	# 911-915	 **attackbox here**
    sprite('ny615_10', 5)	# 916-920	 **attackbox here**
    sprite('ny615_11', 5)	# 921-925	 **attackbox here**
    gotoLabel(132)
    label(140)
    sprite('ny611_00', 6)	# 926-931
    sprite('ny611_01', 6)	# 932-937
    sprite('ny611_02', 6)	# 938-943
    sprite('ny611_03', 6)	# 944-949
    sprite('ny611_04', 6)	# 950-955
    sprite('ny611_05', 6)	# 956-961
    sprite('ny611_06', 6)	# 962-967
    sprite('ny611_07', 6)	# 968-973
    sprite('ny611_08', 6)	# 974-979
    sprite('ny611_09', 6)	# 980-985
    sprite('ny611_10', 6)	# 986-991
    sprite('ny611_11', 7)	# 992-998
    SFX_1('bny700rwi')
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 999-1005
    sprite('ny611_13', 7)	# 1006-1012
    sprite('ny611_14', 7)	# 1013-1019
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_15', 7)	# 1020-1026
    sprite('ny611_16', 7)	# 1027-1033
    sprite('ny611_17', 7)	# 1034-1040
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    label(141)
    sprite('ny611_14', 7)	# 1041-1047
    sprite('ny611_15', 7)	# 1048-1054
    sprite('ny611_16', 7)	# 1055-1061
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_17', 7)	# 1062-1068
    if SLOT_97:
        _gotolabel(141)
    sprite('ny611_14', 1)	# 1069-1069
    Unknown21007(24, 40)
    Unknown21011(180)
    label(142)
    sprite('ny611_14', 7)	# 1070-1076
    sprite('ny611_15', 7)	# 1077-1083
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 1084-1090
    sprite('ny611_17', 7)	# 1091-1097
    loopRest()
    gotoLabel(142)
    label(150)
    sprite('ny610_00', 5)	# 1098-1102
    sprite('ny610_01', 5)	# 1103-1107
    sprite('ny610_02', 5)	# 1108-1112
    sprite('ny610_03', 5)	# 1113-1117
    sprite('ny610_04', 4)	# 1118-1121
    sprite('ny610_05', 4)	# 1122-1125
    sprite('ny610_06', 4)	# 1126-1129
    sprite('ny610_07', 4)	# 1130-1133
    SFX_1('bny700uva')
    sprite('ny610_08', 4)	# 1134-1137
    sprite('ny610_09', 4)	# 1138-1141
    sprite('ny610_10', 5)	# 1142-1146
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny610_11', 5)	# 1147-1151
    sprite('ny610_12', 5)	# 1152-1156
    sprite('ny610_13', 5)	# 1157-1161
    label(151)
    sprite('ny610_11', 5)	# 1162-1166
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny610_12', 5)	# 1167-1171
    sprite('ny610_13', 5)	# 1172-1176
    sprite('ny610_11', 5)	# 1177-1181
    sprite('ny610_12', 5)	# 1182-1186
    sprite('ny610_13', 5)	# 1187-1191
    if SLOT_97:
        _gotolabel(151)
    sprite('ny610_11', 1)	# 1192-1192
    Unknown21007(24, 40)
    Unknown21011(280)
    label(152)
    sprite('ny610_11', 5)	# 1193-1197
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny610_12', 5)	# 1198-1202
    sprite('ny610_13', 5)	# 1203-1207
    sprite('ny610_11', 5)	# 1208-1212
    sprite('ny610_12', 5)	# 1213-1217
    sprite('ny610_13', 5)	# 1218-1222
    loopRest()
    gotoLabel(152)
    label(160)
    sprite('ny611_00', 6)	# 1223-1228
    Unknown2019(1000)
    sprite('ny611_01', 6)	# 1229-1234
    sprite('ny611_02', 6)	# 1235-1240
    sprite('ny611_03', 6)	# 1241-1246
    sprite('ny611_04', 6)	# 1247-1252
    sprite('ny611_05', 6)	# 1253-1258
    sprite('ny611_06', 6)	# 1259-1264
    sprite('ny611_07', 6)	# 1265-1270
    sprite('ny611_08', 6)	# 1271-1276
    sprite('ny611_09', 6)	# 1277-1282
    sprite('ny611_10', 6)	# 1283-1288
    sprite('ny611_11', 7)	# 1289-1295
    SFX_1('bny700umi')
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 1296-1302
    sprite('ny611_13', 7)	# 1303-1309
    sprite('ny611_14', 7)	# 1310-1316
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_15', 7)	# 1317-1323
    sprite('ny611_16', 7)	# 1324-1330
    sprite('ny611_17', 7)	# 1331-1337
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    label(161)
    sprite('ny611_14', 7)	# 1338-1344
    sprite('ny611_15', 7)	# 1345-1351
    sprite('ny611_16', 7)	# 1352-1358
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_17', 7)	# 1359-1365
    if SLOT_97:
        _gotolabel(161)
    sprite('ny611_14', 1)	# 1366-1366
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('ny611_14', 7)	# 1367-1373
    sprite('ny611_15', 7)	# 1374-1380
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 1381-1387
    sprite('ny611_17', 7)	# 1388-1394
    loopRest()
    gotoLabel(162)
    label(170)
    sprite('ny615_00', 6)	# 1395-1400	 **attackbox here**
    sprite('ny615_01', 6)	# 1401-1406	 **attackbox here**
    sprite('ny615_02', 6)	# 1407-1412	 **attackbox here**
    sprite('ny615_03', 8)	# 1413-1420	 **attackbox here**
    sprite('ny615_04', 6)	# 1421-1426	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 6)	# 1427-1432	 **attackbox here**
    sprite('ny615_06', 6)	# 1433-1438	 **attackbox here**
    sprite('ny615_07', 6)	# 1439-1444	 **attackbox here**
    sprite('ny615_08', 6)	# 1445-1450	 **attackbox here**
    sprite('ny615_09', 5)	# 1451-1455	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1456-1460	 **attackbox here**
    sprite('ny615_11', 5)	# 1461-1465	 **attackbox here**
    SFX_1('bny700pla')
    sprite('ny615_09', 5)	# 1466-1470	 **attackbox here**
    sprite('ny615_10', 5)	# 1471-1475	 **attackbox here**
    sprite('ny615_11', 5)	# 1476-1480	 **attackbox here**
    label(171)
    sprite('ny615_09', 5)	# 1481-1485	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1486-1490	 **attackbox here**
    sprite('ny615_11', 5)	# 1491-1495	 **attackbox here**
    sprite('ny615_09', 5)	# 1496-1500	 **attackbox here**
    sprite('ny615_10', 5)	# 1501-1505	 **attackbox here**
    sprite('ny615_11', 5)	# 1506-1510	 **attackbox here**
    if SLOT_97:
        _gotolabel(171)
    sprite('ny615_09', 5)	# 1511-1515	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1516-1520	 **attackbox here**
    Unknown21011(320)
    Unknown21007(24, 40)
    sprite('ny615_11', 5)	# 1521-1525	 **attackbox here**
    sprite('ny615_09', 5)	# 1526-1530	 **attackbox here**
    sprite('ny615_10', 5)	# 1531-1535	 **attackbox here**
    sprite('ny615_11', 5)	# 1536-1540	 **attackbox here**
    label(172)
    sprite('ny615_09', 5)	# 1541-1545	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1546-1550	 **attackbox here**
    sprite('ny615_11', 5)	# 1551-1555	 **attackbox here**
    sprite('ny615_09', 5)	# 1556-1560	 **attackbox here**
    sprite('ny615_10', 5)	# 1561-1565	 **attackbox here**
    sprite('ny615_11', 5)	# 1566-1570	 **attackbox here**
    gotoLabel(172)
    label(180)
    sprite('ny615_00', 6)	# 1571-1576	 **attackbox here**
    sprite('ny615_01', 6)	# 1577-1582	 **attackbox here**
    sprite('ny615_02', 6)	# 1583-1588	 **attackbox here**
    sprite('ny615_03', 8)	# 1589-1596	 **attackbox here**
    sprite('ny615_04', 6)	# 1597-1602	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 6)	# 1603-1608	 **attackbox here**
    sprite('ny615_06', 6)	# 1609-1614	 **attackbox here**
    sprite('ny615_07', 6)	# 1615-1620	 **attackbox here**
    sprite('ny615_08', 6)	# 1621-1626	 **attackbox here**
    sprite('ny615_09', 5)	# 1627-1631	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1632-1636	 **attackbox here**
    sprite('ny615_11', 5)	# 1637-1641	 **attackbox here**
    SFX_1('bny700pmi')
    sprite('ny615_09', 5)	# 1642-1646	 **attackbox here**
    sprite('ny615_10', 5)	# 1647-1651	 **attackbox here**
    sprite('ny615_11', 5)	# 1652-1656	 **attackbox here**
    label(181)
    sprite('ny615_09', 5)	# 1657-1661	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1662-1666	 **attackbox here**
    sprite('ny615_11', 5)	# 1667-1671	 **attackbox here**
    sprite('ny615_09', 5)	# 1672-1676	 **attackbox here**
    sprite('ny615_10', 5)	# 1677-1681	 **attackbox here**
    sprite('ny615_11', 5)	# 1682-1686	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('ny615_09', 5)	# 1687-1691	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    Unknown21007(24, 40)
    Unknown21011(260)
    sprite('ny615_10', 5)	# 1692-1696	 **attackbox here**
    sprite('ny615_11', 5)	# 1697-1701	 **attackbox here**
    sprite('ny615_09', 5)	# 1702-1706	 **attackbox here**
    sprite('ny615_10', 5)	# 1707-1711	 **attackbox here**
    sprite('ny615_11', 5)	# 1712-1716	 **attackbox here**
    label(182)
    sprite('ny615_09', 5)	# 1717-1721	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 1722-1726	 **attackbox here**
    sprite('ny615_11', 5)	# 1727-1731	 **attackbox here**
    sprite('ny615_09', 5)	# 1732-1736	 **attackbox here**
    sprite('ny615_10', 5)	# 1737-1741	 **attackbox here**
    sprite('ny615_11', 5)	# 1742-1746	 **attackbox here**
    gotoLabel(182)

@State
def CmnActLose():
    sprite('ny620_00', 6)	# 1-6
    if random_(2, 0, 50):
        SFX_1('bny403_0')
    else:
        SFX_1('bny403_1')
    sprite('ny620_01', 6)	# 7-12
    sprite('ny620_02', 6)	# 13-18
    sprite('ny620_03', 6)	# 19-24
    sprite('ny620_04', 6)	# 25-30
    sprite('ny620_05', 6)	# 31-36
    sprite('ny620_06', 6)	# 37-42
    sprite('ny620_07', 6)	# 43-48
    sprite('ny620_08', 6)	# 49-54
    Unknown23018(1)
    label(0)
    sprite('ny620_08ex01', 1)	# 55-55
    GFX_1('nyef_timeupptc', -1)
    if random_(2, 0, 20):
        SFX_0('014_electric_s')
    sprite('ny620_08ex02', 1)	# 56-56
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryWait():
    label(0)
    sprite('ny000_00', 6)	# 1-6
    sprite('ny000_01', 6)	# 7-12
    sprite('ny000_02', 6)	# 13-18
    sprite('ny000_03', 6)	# 19-24
    sprite('ny000_04', 6)	# 25-30
    sprite('ny000_05', 6)	# 31-36
    sprite('ny000_06', 6)	# 37-42
    sprite('ny000_07', 6)	# 43-48
    sprite('ny000_08', 6)	# 49-54
    sprite('ny000_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryStand():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefWin():
    sprite('keep', 2)	# 1-2
    loopRest()
    enterState('CmnActStand')

@State
def EventDefLose():
    label(0)
    sprite('ny620_08ex01', 1)	# 1-1
    GFX_1('nyef_timeupptc', -1)
    if random_(2, 0, 20):
        SFX_0('014_electric_s')
    sprite('ny620_08ex02', 1)	# 2-2
    loopRest()
    gotoLabel(0)

@State
def EventDown():
    Unknown2004(1, 0)
    sprite('ny070_00', 2)	# 1-2
    sprite('ny070_01', 2)	# 3-4
    sprite('ny070_02', 4)	# 5-8
    SFX_0('205_runjump_garden_0')
    sprite('ny070_03', 4)	# 9-12
    sprite('ny070_04', 4)	# 13-16
    sprite('ny070_05', 4)	# 17-20
    sprite('ny070_06', 4)	# 21-24
    sprite('ny070_07', 5)	# 25-29
    sprite('ny070_08', 5)	# 30-34
    sprite('ny070_09', 2)	# 35-36
    Unknown1004()
    sprite('ny063_11', 32767)	# 37-32803
    Unknown1005()
    loopRest()

@State
def EventEntryFall():
    Unknown1000(-260000)
    teleportRelativeY(640000)
    setGravity(57)

    def upon_3():
        if (SLOT_23 < 120000):
            sendToLabel(1)
    sprite('ny600_00', 1)	# 1-1
    label(0)
    sprite('ny600_00', 6)	# 2-7
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 8-13
    sprite('ny600_02', 6)	# 14-19
    sprite('ny600_00', 6)	# 20-25
    sprite('ny600_01', 6)	# 26-31
    sprite('ny600_02', 6)	# 32-37
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sendToLabelUpon(2, 3)
    label(2)
    sprite('ny600_03', 15)	# 38-52
    YAccel(60)
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    SFX_0('019_cloth_a')
    sprite('ny600_03', 15)	# 53-67
    YAccel(60)
    sprite('ny600_03', 15)	# 68-82
    YAccel(60)
    gotoLabel(2)
    label(3)
    clearUponHandler(2)
    sprite('ny600_03', 6)	# 83-88
    Unknown1084(1)
    SFX_0('019_cloth_a')
    sprite('ny600_04', 6)	# 89-94
    SFX_0('201_walk_garden_0')
    sprite('ny600_05', 6)	# 95-100
    Unknown8000(0, 1, 1)
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny600_06', 6)	# 101-106
    sprite('ny600_07', 6)	# 107-112
    sprite('ny600_08', 6)	# 113-118
    sprite('ny600_09', 6)	# 119-124
    sprite('ny600_10', 6)	# 125-130
    label(4)
    sprite('ny600_11', 6)	# 131-136
    sprite('ny600_12', 6)	# 137-142
    sprite('ny600_13', 6)	# 143-148
    sprite('ny600_14', 6)	# 149-154
    gotoLabel(4)

@State
def EventEntryBootMurakumo():
    sprite('ny600_11', 6)	# 1-6
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('ny600_12', 6)	# 7-12
    sprite('ny600_13', 3)	# 13-15
    sprite('ny600_13', 3)	# 16-18
    SFX_3('nyse_28')
    sprite('ny600_14', 6)	# 19-24
    sprite('ny600_11', 6)	# 25-30
    sprite('ny600_12', 6)	# 31-36
    sprite('ny600_13', 6)	# 37-42
    sprite('ny600_14', 6)	# 43-48
    sprite('ny600_15', 6)	# 49-54
    Unknown23118(0)
    Unknown23117(16777215, 30)
    GFX_1('nyef_entrylightA', 0)
    SFX_0('019_cloth_a')
    SFX_3('nyse_03')
    sprite('ny600_16', 12)	# 55-66
    sprite('ny600_17', 6)	# 67-72
    GFX_1('nyef_entrylightB', 0)
    sprite('ny600_18', 6)	# 73-78
    Unknown23117(0, 10)
    sprite('ny600_19', 6)	# 79-84
    SFX_0('022_magiccircle_a')
    sprite('ny600_20', 6)	# 85-90
    sprite('ny600_21', 6)	# 91-96
    sprite('ny600_22', 6)	# 97-102
    sprite('ny600_23', 6)	# 103-108
    loopRest()
    enterState('CmnActStand')

@State
def EventGoStand():
    sprite('ny620_08', 5)	# 1-5
    sprite('ny620_07', 5)	# 6-10
    sprite('ny620_06', 5)	# 11-15
    sprite('ny620_05', 5)	# 16-20
    sprite('ny620_04', 5)	# 21-25
    sprite('ny620_03', 5)	# 26-30
    sprite('ny620_02', 5)	# 31-35
    sprite('ny620_01', 5)	# 36-40
    sprite('ny620_00', 5)	# 41-45
    loopRest()
    enterState('CmnActStand')

@State
def EventChouhatu():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    loopRest()
    sprite('ny300_04', 20)	# 41-60	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    loopRest()
    sprite('ny300_04', 20)	# 61-80	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    loopRest()
    sprite('ny300_04', 12)	# 81-92	 **attackbox here**
    sprite('ny300_04', 1)	# 93-93	 **attackbox here**
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 94-99	 **attackbox here**
    sprite('ny300_06', 6)	# 100-105	 **attackbox here**
    sprite('ny300_07', 6)	# 106-111	 **attackbox here**
    sprite('ny300_08', 8)	# 112-119	 **attackbox here**
    sprite('ny300_09', 20)	# 120-139	 **attackbox here**
    sprite('ny300_10', 4)	# 140-143	 **attackbox here**
    sprite('ny300_11', 4)	# 144-147	 **attackbox here**
    enterState('CmnActStand')

@State
def EventWarpOutSimple():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown2034(0)
        Unknown3032()
    sprite('keep', 26)	# 1-26
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('keep', 1)	# 27-27
    Unknown1000(-500000)
    sprite('null', 32767)	# 28-32794
    loopRest()

@State
def EventCrouch():
    label(0)
    sprite('ny010_02', 6)	# 1-6
    sprite('ny010_03', 6)	# 7-12
    sprite('ny010_04', 6)	# 13-18
    sprite('ny010_05', 6)	# 19-24
    sprite('ny010_06', 6)	# 25-30
    sprite('ny010_07', 6)	# 31-36
    sprite('ny010_08', 6)	# 37-42
    sprite('ny010_09', 6)	# 43-48
    sprite('ny010_10', 6)	# 49-54
    sprite('ny010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventCrouchToStand():
    sprite('ny010_01', 4)	# 1-4
    sprite('ny010_00', 4)	# 5-8
    loopRest()
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventWarpIn():
    Unknown2019(-500)
    Unknown3032()
    Unknown2034(0)
    sprite('ny331_00', 2)	# 1-2
    Unknown3001(0)
    sprite('ny331_04', 4)	# 3-6
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(10)
    sprite('ny331_05', 6)	# 7-12
    sprite('ny331_06', 6)	# 13-18
    sprite('ny331_07', 6)	# 19-24
    sprite('ny331_05', 6)	# 25-30
    sprite('ny331_06', 6)	# 31-36
    sprite('ny331_07', 6)	# 37-42
    Unknown3001(255)
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 103)
    label(0)
    sprite('ny331_05', 6)	# 43-48
    sprite('ny331_06', 6)	# 49-54
    sprite('ny331_07', 6)	# 55-60
    gotoLabel(0)

@State
def EventWarpInToStand():
    sprite('ny331_08', 6)	# 1-6
    sprite('ny331_09', 6)	# 7-12
    sprite('ny331_10', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def EventWarpOut():
    Unknown2019(-500)
    Unknown3032()
    Unknown2034(0)
    sprite('ny331_00', 2)	# 1-2
    sprite('ny331_01', 15)	# 3-17
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ny331_02', 15)	# 18-32
    sprite('ny331_03', 15)	# 33-47
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_0')
    sprite('ny331_01', 15)	# 48-62
    sprite('ny331_02', 15)	# 63-77
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ny331_03', 15)	# 78-92
    sprite('ny331_01', 15)	# 93-107
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_0')
    sprite('ny331_02', 15)	# 108-122
    sprite('ny331_04', 4)	# 123-126
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('ny331_05', 6)	# 127-132
    sprite('ny331_06', 6)	# 133-138
    sprite('ny331_07', 6)	# 139-144
    GFX_1('haef_event_lose_end', 103)
    sprite('ny331_05', 6)	# 145-150
    Unknown1000(-900000)
    sprite('ny331_06', 6)	# 151-156
    sprite('ny331_07', 6)	# 157-162
    sprite('ny331_05', 6)	# 163-168
    sprite('ny331_06', 6)	# 169-174
    sprite('ny331_07', 6)	# 175-180
    sprite('ny331_08', 2)	# 181-182
    sprite('ny331_09', 2)	# 183-184
    sprite('ny331_10', 2)	# 185-186

@State
def EventLoseDownLoop():
    sprite('ny063_11', 32767)	# 1-32767
    loopRest()

@State
def EventLoseDown2WorpWait():
    sprite('ny064_00', 8)	# 1-8
    sprite('ny064_01', 8)	# 9-16
    sprite('ny064_02', 8)	# 17-24
    label(1)
    sprite('ny064_03', 90)	# 25-114
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_3('nyse_28')
    loopRest()
    gotoLabel(1)

@State
def EventLoseWorpout():
    sprite('ny064_03', 25)	# 1-25
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    sprite('null', 32767)	# 26-32792
    Unknown3038(1)
    loopRest()

@State
def EventRGVsNY_FallSword():
    sprite('null', 1)	# 1-1
    GFX_0('EntryFallSword_RGVsNY', 0)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    loopRest()

@State
def EventRGVsNY_Transform():
    sprite('ny600_15', 6)	# 1-6
    Unknown23118(0)
    Unknown23117(16777215, 30)
    GFX_1('nyef_entrylightA', 0)
    SFX_0('019_cloth_a')
    SFX_3('nyse_03')
    sprite('ny600_16', 12)	# 7-18
    Unknown21007(1, 32)
    sprite('ny600_17', 6)	# 19-24
    GFX_1('nyef_entrylightB', 0)
    sprite('ny600_18', 6)	# 25-30
    Unknown23117(0, 10)
    sprite('ny600_19', 6)	# 31-36
    SFX_0('022_magiccircle_a')
    sprite('ny600_20', 6)	# 37-42
    sprite('ny600_21', 6)	# 43-48
    sprite('ny600_22', 6)	# 49-54
    sprite('ny600_23', 6)	# 55-60
    enterState('CmnActStand')

@State
def EventRGVsNY_Attack():
    Unknown1000(-260000)
    AttackDefaults_StandingDD()
    AttackLevel_(4)
    setInvincible(1)
    sendToLabelUpon(32, 1)
    label(0)
    sprite('ny000_00', 6)	# 1-6
    sprite('ny000_01', 6)	# 7-12
    sprite('ny000_02', 6)	# 13-18
    sprite('ny000_03', 6)	# 19-24
    sprite('ny000_04', 6)	# 25-30
    sprite('ny000_05', 6)	# 31-36
    sprite('ny000_06', 6)	# 37-42
    sprite('ny000_07', 6)	# 43-48
    sprite('ny000_08', 6)	# 49-54
    sprite('ny000_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(32)
    sprite('ny232_00', 3)	# 61-63
    sprite('ny232_01', 2)	# 64-65
    sprite('ny232_02', 3)	# 66-68	 **attackbox here**
    SFX_0('010_swing_sword_2')
    sprite('ny232_03', 1)	# 69-69	 **attackbox here**
    sprite('ny232_03', 1)	# 70-70	 **attackbox here**
    sprite('ny232_04', 1)	# 71-71	 **attackbox here**
    GFX_0('2CZanzo', -1)
    SFX_0('010_swing_sword_2')
    sprite('ny232_04', 1)	# 72-72	 **attackbox here**
    sprite('ny232_04ex01', 1)	# 73-73	 **attackbox here**
    sprite('ny232_04ex01', 1)	# 74-74	 **attackbox here**
    sprite('ny232_05', 2)	# 75-76	 **attackbox here**
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_2')
    ScreenShake(2000, 6000)
    sprite('ny232_05ex01', 2)	# 77-78	 **attackbox here**
    sprite('ny232_05ex02', 2)	# 79-80
    sprite('ny232_06', 3)	# 81-83
    sprite('ny232_07', 3)	# 84-86
    sprite('ny232_08', 3)	# 87-89
    sprite('ny232_09', 3)	# 90-92
    sprite('ny010_01', 3)	# 93-95
    sprite('ny010_00', 3)	# 96-98
    loopRest()
    sendToLabelUpon(32, 3)
    label(2)
    sprite('ny000_00', 6)	# 99-104
    sprite('ny000_01', 6)	# 105-110
    sprite('ny000_02', 6)	# 111-116
    sprite('ny000_03', 6)	# 117-122
    sprite('ny000_04', 6)	# 123-128
    sprite('ny000_05', 6)	# 129-134
    sprite('ny000_06', 6)	# 135-140
    sprite('ny000_07', 6)	# 141-146
    sprite('ny000_08', 6)	# 147-152
    sprite('ny000_09', 6)	# 153-158
    loopRest()
    gotoLabel(2)
    label(3)
    clearUponHandler(32)
    sprite('ny213_00', 3)	# 159-161
    sprite('ny213_01', 3)	# 162-164
    sprite('ny213_02', 3)	# 165-167
    sprite('ny213_03', 3)	# 168-170
    sprite('ny213_04', 3)	# 171-173
    sprite('ny213_05', 3)	# 174-176
    SFX_0('011_spin_0')
    sprite('ny213_06', 3)	# 177-179
    sprite('ny213_07', 1)	# 180-180	 **attackbox here**
    RefreshMultihit()
    GFX_0('6CZanzo', -1)
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_2')
    ScreenShake(8000, 4000)
    sprite('ny213_07', 1)	# 181-181	 **attackbox here**
    sprite('ny213_08', 1)	# 182-182	 **attackbox here**
    sprite('ny213_08', 1)	# 183-183	 **attackbox here**
    sprite('ny213_09', 1)	# 184-184	 **attackbox here**
    SFX_0('011_spin_0')
    sprite('ny213_09', 1)	# 185-185	 **attackbox here**
    sprite('ny213_10', 1)	# 186-186	 **attackbox here**
    sprite('ny213_10', 1)	# 187-187	 **attackbox here**
    sprite('ny213_11', 6)	# 188-193	 **attackbox here**
    sprite('ny213_12', 2)	# 194-195
    sprite('ny213_12', 4)	# 196-199
    sprite('ny213_13', 6)	# 200-205
    sprite('ny213_14', 6)	# 206-211
    loopRest()
    enterState('CmnActStand')

@State
def EventNYAttack5D():
    sprite('ny203_00', 4)	# 1-4
    sprite('ny203_01', 4)	# 5-8
    sprite('ny203_02', 4)	# 9-12
    sprite('ny203_03', 4)	# 13-16
    sprite('ny203_04', 4)	# 17-20
    sprite('ny203_05', 4)	# 21-24
    sprite('ny203_06', 4)	# 25-28
    sprite('ny203_07', 4)	# 29-32
    sprite('ny203_08', 4)	# 33-36
    sprite('ny203_09', 4)	# 37-40
    sprite('ny203_10', 4)	# 41-44
    sprite('ny203_11', 4)	# 45-48
    sprite('ny203_12', 4)	# 49-52
    sprite('ny203_13', 4)	# 53-56
    sprite('ny203_14', 4)	# 57-60
    sprite('ny203_15', 4)	# 61-64
    sprite('ny203_16', 4)	# 65-68
    sprite('ny203_17', 4)	# 69-72
    enterState('CmnActStand')

@State
def EventNYStanding():
    sprite('ny450_00', 6)	# 1-6
    sprite('ny450_01', 6)	# 7-12
    label(0)
    sprite('ny450_02', 6)	# 13-18
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny450_03', 6)	# 19-24
    sprite('ny450_04', 6)	# 25-30
    gotoLabel(0)
    enterState('CmnActStand')

@State
def EventNYStandingEnd():
    sprite('ny450_01', 6)	# 1-6
    sprite('ny450_00', 6)	# 7-12
    enterState('CmnActStand')

@State
def EventDown2():
    sprite('ny620_08', 32767)	# 1-32767

@State
def EventChouhatuLoop():
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    label(0)
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 41-60	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def EventChouhatuLoopEnd():
    sprite('ny300_04', 12)	# 1-12	 **attackbox here**
    sprite('ny300_04', 1)	# 13-13	 **attackbox here**
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 14-19	 **attackbox here**
    sprite('ny300_06', 6)	# 20-25	 **attackbox here**
    sprite('ny300_07', 6)	# 26-31	 **attackbox here**
    sprite('ny300_08', 8)	# 32-39	 **attackbox here**
    sprite('ny300_09', 20)	# 40-59	 **attackbox here**
    sprite('ny300_10', 4)	# 60-63	 **attackbox here**
    sprite('ny300_11', 4)	# 64-67	 **attackbox here**
    enterState('CmnActStand')

@State
def EventDashScreenOut():
    sprite('ny032_00', 2)	# 1-2
    Unknown2005()
    Unknown2034(0)
    Unknown2017(0)
    GFX_0('EventRL', 0)
    sprite('ny032_00', 2)	# 3-4
    physicsXImpulse(32000)
    sprite('ny032_01', 4)	# 5-8
    sprite('ny032_02', 4)	# 9-12
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 13-16
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 17-20
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 21-24
    sprite('ny032_02', 4)	# 25-28
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 29-32
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 33-36
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 37-40
    sprite('ny032_02', 4)	# 41-44
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 45-48
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 49-52
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 53-56
    sprite('ny032_02', 4)	# 57-60
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 61-64
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 65-68
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 69-72
    sprite('ny032_02', 4)	# 73-76
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 77-80
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 81-84
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 85-88
    sprite('ny032_02', 4)	# 89-92
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 93-96
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 97-100
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    Unknown3038(1)
    loopRest()

@State
def EventLargeSwordLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23027()
    sprite('ny431_00', 4)	# 1-4
    sprite('ny431_01', 5)	# 5-9
    sprite('ny431_02', 5)	# 10-14
    Unknown2036(52, -1, 0)
    GFX_0('EMB_NY', -1)
    GFX_0('NY_SummonDmc', -1)
    sprite('ny431_03', 5)	# 15-19
    sprite('ny431_04', 5)	# 20-24
    SFX_3('nyse_26')
    GFX_0('SummonDDBigSword', -1)
    sprite('ny431_05', 30)	# 25-54
    sprite('ny431_06', 2)	# 55-56
    sprite('ny431_07', 2)	# 57-58
    sprite('ny431_08', 2)	# 59-60
    sprite('ny431_09', 3)	# 61-63
    Unknown21007(22, 32)
    sprite('ny431_10', 3)	# 64-66
    sprite('ny431_11', 3)	# 67-69
    sprite('ny431_12', 3)	# 70-72
    sprite('ny431_09', 4)	# 73-76
    sprite('ny431_10', 4)	# 77-80
    sprite('ny431_11', 4)	# 81-84
    sprite('ny431_12', 4)	# 85-88
    sprite('ny431_13', 4)	# 89-92
    sprite('ny431_14', 4)	# 93-96
    sprite('ny431_15', 4)	# 97-100
    sprite('ny431_16', 4)	# 101-104

@State
def EventLoseDown():
    sprite('ny064_00', 8)	# 1-8
    sprite('ny064_01', 8)	# 9-16
    sprite('ny064_02', 8)	# 17-24
    label(1)
    sprite('ny064_03', 90)	# 25-114
    SFX_0('electric_s')
    loopRest()
    gotoLabel(1)

@State
def Act2Event_Chouhatsu():
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    label(0)
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 41-60	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act2Event_ChouhatsuEnd():
    sprite('ny300_04', 12)	# 1-12	 **attackbox here**
    sprite('ny300_04', 1)	# 13-13	 **attackbox here**
    GFX_0('EF_ny300', 0)
    sprite('ny300_05', 6)	# 14-19	 **attackbox here**
    sprite('ny300_06', 6)	# 20-25	 **attackbox here**
    sprite('ny300_07', 6)	# 26-31	 **attackbox here**
    sprite('ny300_08', 8)	# 32-39	 **attackbox here**
    sprite('ny300_09', 20)	# 40-59	 **attackbox here**
    sprite('ny300_10', 4)	# 60-63	 **attackbox here**
    sprite('ny300_11', 4)	# 64-67	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Chouhatsu2():
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    GFX_0('Event_EF_ny300', 0)
    label(0)
    sprite('ny300_04', 20)	# 41-60	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 20)	# 61-80	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Chouhatsu2End():
    sprite('ny300_04', 1)	# 1-1	 **attackbox here**
    sprite('ny300_04', 10)	# 2-11	 **attackbox here**
    sprite('ny300_05', 6)	# 12-17	 **attackbox here**
    sprite('ny300_06', 6)	# 18-23	 **attackbox here**
    sprite('ny300_07', 6)	# 24-29	 **attackbox here**
    Unknown21012('4576656e745f45465f6e7933303000000000000000000000000000000000000020000000')
    sprite('ny300_08', 8)	# 30-37	 **attackbox here**
    sprite('ny300_09', 20)	# 38-57	 **attackbox here**
    sprite('ny300_10', 4)	# 58-61	 **attackbox here**
    sprite('ny300_11', 4)	# 62-65	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Damage():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('ny070_00', 15)	# 1-15
    Unknown4045('707465665f6869745f6d6964646c65000000000000000000000000000000000067000000')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('ny070_01', 4)	# 16-19
    sprite('ny070_02', 4)	# 20-23
    sprite('ny070_03', 32767)	# 24-32790
    loopRest()

@State
def Act2Event_DamageEnd():
    sprite('ny070_10', 5)	# 1-5
    sprite('ny070_11', 5)	# 6-10
    sprite('ny070_12', 5)	# 11-15
    sprite('ny070_13', 5)	# 16-20
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_TimeUp():
    sprite('ny611_00', 6)	# 1-6
    sprite('ny611_01', 6)	# 7-12
    sprite('ny611_02', 6)	# 13-18
    sprite('ny611_03', 6)	# 19-24
    sprite('ny611_04', 6)	# 25-30
    sprite('ny611_05', 6)	# 31-36
    sprite('ny611_06', 6)	# 37-42
    sprite('ny611_07', 6)	# 43-48
    sprite('ny611_08', 6)	# 49-54
    sprite('ny611_09', 6)	# 55-60
    sprite('ny611_10', 6)	# 61-66
    sprite('ny611_11', 7)	# 67-73
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 74-80
    sprite('ny611_13', 7)	# 81-87
    label(0)
    sprite('ny611_14', 7)	# 88-94
    sprite('ny611_15', 7)	# 95-101
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 102-108
    sprite('ny611_17', 7)	# 109-115
    sprite('ny611_14', 7)	# 116-122
    sprite('ny611_15', 7)	# 123-129
    GFX_1('nyef_entrymc', 0)
    sprite('ny611_16', 7)	# 130-136
    sprite('ny611_17', 7)	# 137-143
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Warp():
    sprite('ny611_00', 6)	# 1-6
    sprite('ny611_01', 6)	# 7-12
    sprite('ny611_02', 6)	# 13-18
    sprite('ny611_03', 6)	# 19-24
    sprite('ny611_04', 6)	# 25-30
    sprite('ny611_05', 6)	# 31-36
    sprite('ny611_06', 6)	# 37-42
    sprite('ny611_07', 6)	# 43-48
    sprite('ny611_08', 6)	# 49-54
    sprite('ny611_09', 6)	# 55-60
    sprite('ny611_10', 6)	# 61-66
    sprite('ny611_11', 7)	# 67-73
    Unknown3004(-12)
    GFX_1('nyef_entrymc', 0)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('022_magiccircle_c')
    SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 74-80
    sprite('ny611_13', 7)	# 81-87
    sprite('ny611_14', 7)	# 88-94
    sprite('ny611_15', 7)	# 95-101
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 102-108
    sprite('ny611_17', 7)	# 109-115
    sprite('ny611_14', 7)	# 116-122
    sprite('ny611_15', 7)	# 123-129
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 130-136
    sprite('ny611_17', 7)	# 137-143
    sprite('ny611_14', 7)	# 144-150
    sprite('ny611_15', 7)	# 151-157
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 158-164
    sprite('ny611_17', 7)	# 165-171
    Unknown3001(0)
    Unknown3004(0)
    Unknown3038(1)
    sprite('null', 32767)	# 172-32938
    loopRest()

@State
def Act2Event_RoundWin():
    sprite('ny615_00', 6)	# 1-6	 **attackbox here**
    sprite('ny615_01', 6)	# 7-12	 **attackbox here**
    sprite('ny615_02', 6)	# 13-18	 **attackbox here**
    sprite('ny615_03', 8)	# 19-26	 **attackbox here**
    sprite('ny615_04', 6)	# 27-32	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_05', 6)	# 33-38	 **attackbox here**
    sprite('ny615_06', 6)	# 39-44	 **attackbox here**
    sprite('ny615_07', 6)	# 45-50	 **attackbox here**
    sprite('ny615_08', 6)	# 51-56	 **attackbox here**
    sprite('ny615_09', 5)	# 57-61	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 62-66	 **attackbox here**
    sprite('ny615_11', 5)	# 67-71	 **attackbox here**
    sprite('ny615_09', 5)	# 72-76	 **attackbox here**
    sprite('ny615_10', 5)	# 77-81	 **attackbox here**
    sprite('ny615_11', 5)	# 82-86	 **attackbox here**
    label(0)
    sprite('ny615_09', 5)	# 87-91	 **attackbox here**
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny615_10', 5)	# 92-96	 **attackbox here**
    sprite('ny615_11', 5)	# 97-101	 **attackbox here**
    sprite('ny615_09', 5)	# 102-106	 **attackbox here**
    sprite('ny615_10', 5)	# 107-111	 **attackbox here**
    sprite('ny615_11', 5)	# 112-116	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act2Event_RoundWinEnd():
    sprite('keep', 2)	# 1-2
    sprite('ny615_08', 6)	# 3-8	 **attackbox here**
    sprite('ny615_07', 6)	# 9-14	 **attackbox here**
    sprite('ny615_06', 6)	# 15-20	 **attackbox here**
    sprite('ny615_05', 6)	# 21-26	 **attackbox here**
    sprite('ny615_04', 6)	# 27-32	 **attackbox here**
    sprite('ny615_03', 6)	# 33-38	 **attackbox here**
    sprite('ny615_02', 6)	# 39-44	 **attackbox here**
    sprite('ny615_01', 6)	# 45-50	 **attackbox here**
    sprite('ny615_00', 6)	# 51-56	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_OverDrive():
    sprite('ny333_00', 6)	# 1-6
    sprite('ny333_01', 6)	# 7-12
    sprite('ny333_02', 6)	# 13-18
    sprite('ny333_03', 32767)	# 19-32785
    loopRest()

@State
def Act2Event_OverDriveActivate():
    sprite('keep', 2)	# 1-2
    sprite('ny333_04', 4)	# 3-6
    SFX_0('302_spsys_drivemotion')
    SFX_0('302_spsys_burst')
    ScreenShake(30000, 60000)
    sprite('ny333_05', 5)	# 7-11
    sprite('ny333_06', 5)	# 12-16
    sprite('ny333_07', 5)	# 17-21
    sprite('ny333_05', 5)	# 22-26
    sprite('ny333_06', 5)	# 27-31
    sprite('ny333_07', 5)	# 32-36
    sprite('ny333_05', 5)	# 37-41
    sprite('ny333_06', 5)	# 42-46
    sprite('ny333_07', 5)	# 47-51
    loopRest()
    enterState('Act2Event_OverDriveEnd')

@State
def Act2Event_OverDriveEnd():
    sprite('ny333_08', 4)	# 1-4
    sprite('ny333_09', 4)	# 5-8
    sprite('ny333_10', 4)	# 9-12
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_5D():
    sprite('ny203_00', 5)	# 1-5
    sprite('ny203_01', 5)	# 6-10
    sprite('ny203_02', 5)	# 11-15
    sprite('ny203_03', 5)	# 16-20
    sprite('ny203_04', 20)	# 21-40
    sprite('ny203_03', 5)	# 41-45
    sprite('ny203_02', 5)	# 46-50
    sprite('ny203_01', 5)	# 51-55
    sprite('ny203_00', 5)	# 56-60
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_rlvsny_01():
    label(0)
    sprite('ny600_11', 6)	# 1-6
    sprite('ny600_12', 6)	# 7-12
    sprite('ny600_13', 6)	# 13-18
    sprite('ny600_14', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def Act2Event_bnvsny_00():

    def upon_IMMEDIATE():
        Unknown1000(-60000)
    sprite('keep', 1)	# 1-1
    GFX_0('Act2Event_Nirvana', -1)
    Unknown38(4, 1)
    GFX_0('Act2Event_Carl', -1)
    Unknown38(5, 1)
    Unknown2005()
    loopRest()
    label(0)
    sprite('ny000_00', 6)	# 2-7
    sprite('ny000_01', 6)	# 8-13
    sprite('ny000_02', 6)	# 14-19
    sprite('ny000_03', 6)	# 20-25
    sprite('ny000_04', 6)	# 26-31
    sprite('ny000_05', 6)	# 32-37
    sprite('ny000_06', 6)	# 38-43
    sprite('ny000_07', 6)	# 44-49
    sprite('ny000_08', 6)	# 50-55
    sprite('ny000_09', 6)	# 56-61
    loopRest()
    gotoLabel(0)

@State
def Act2Event_bnvsny_01():
    sprite('keep', 2)	# 1-2
    sprite('ny003_02', 3)	# 3-5
    Unknown2005()
    sprite('ny003_01', 3)	# 6-8
    sprite('ny003_00', 3)	# 9-11
    Unknown21007(5, 32)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_bnvsny_02():
    sprite('keep', 2)	# 1-2
    Unknown21007(4, 41)
    Unknown21007(5, 41)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_rmvsny_00():
    sprite('keep', 2)	# 1-2
    sprite('ny615_08', 7)	# 3-9	 **attackbox here**
    sprite('ny615_07', 7)	# 10-16	 **attackbox here**
    sprite('ny615_06', 7)	# 17-23	 **attackbox here**
    sprite('ny333_01', 6)	# 24-29
    sprite('ny333_02', 6)	# 30-35
    sprite('ny333_03', 120)	# 36-155
    label(0)
    sprite('ny333_03', 10)	# 156-165
    ScreenShake(3000, 3000)
    SFX_0('019_quake_0')
    loopRest()
    gotoLabel(0)

@State
def Act2Event_rmvsny_01():
    sprite('keep', 2)	# 1-2
    sprite('ny333_04', 4)	# 3-6
    sprite('ny333_05', 5)	# 7-11
    sprite('ny333_06', 5)	# 12-16
    sprite('ny333_07', 5)	# 17-21
    sprite('ny333_05', 5)	# 22-26
    sprite('ny333_06', 5)	# 27-31
    sprite('ny333_07', 5)	# 32-36
    sprite('ny333_05', 5)	# 37-41
    sprite('ny333_06', 5)	# 42-46
    sprite('ny333_07', 5)	# 47-51
    loopRest()
    enterState('Act2Event_OverDriveEnd')

@State
def Act2Event_rmvsny_02():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('ny070_00', 15)	# 1-15
    Unknown4052()
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_1')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('ny070_01', 4)	# 16-19
    sprite('ny070_02', 4)	# 20-23
    sprite('ny070_03', 32767)	# 24-32790
    loopRest()

@State
def Act2Event_rmvsny_03():
    sprite('ny611_00', 6)	# 1-6
    sprite('ny611_01', 6)	# 7-12
    sprite('ny611_02', 6)	# 13-18
    sprite('ny611_03', 6)	# 19-24
    sprite('ny611_04', 6)	# 25-30
    sprite('ny611_05', 6)	# 31-36
    sprite('ny611_06', 6)	# 37-42
    sprite('ny611_07', 6)	# 43-48
    sprite('ny611_08', 6)	# 49-54
    sprite('ny611_09', 6)	# 55-60
    sprite('ny611_10', 6)	# 61-66
    sprite('ny611_11', 7)	# 67-73
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_12', 7)	# 74-80
    sprite('ny611_13', 7)	# 81-87
    label(0)
    sprite('ny611_14', 7)	# 88-94
    sprite('ny611_15', 7)	# 95-101
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 102-108
    sprite('ny611_17', 7)	# 109-115
    loopRest()
    gotoLabel(0)

@State
def Act2Event_rmvsny_04():
    sprite('keep', 2)	# 1-2
    Unknown3004(-12)
    GFX_1('nyef_entrymc', 0)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('022_magiccircle_c')
    sprite('ny611_14', 7)	# 3-9
    sprite('ny611_15', 7)	# 10-16
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 17-23
    sprite('ny611_17', 7)	# 24-30
    sprite('ny611_14', 7)	# 31-37
    GFX_0('Act2Event_Yure', -1)
    sprite('ny611_15', 7)	# 38-44
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 45-51
    sprite('ny611_17', 7)	# 52-58
    Unknown3001(0)
    Unknown3004(0)
    Unknown3038(1)
    sprite('null', 32767)	# 59-32825
    loopRest()

@State
def Act2Event_rmvsny_05():
    sprite('keep', 2)	# 1-2
    sprite('ny032_00', 2)	# 3-4
    Unknown2005()
    Unknown2034(0)
    Unknown2017(0)
    sprite('ny032_00', 2)	# 5-6
    physicsXImpulse(32000)
    sprite('ny032_01', 4)	# 7-10
    sprite('ny032_02', 4)	# 11-14
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 19-22
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 23-26
    GFX_0('Act2Event_Yure', -1)
    sprite('ny032_02', 4)	# 27-30
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 31-34
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 35-38
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 39-42
    sprite('ny032_02', 4)	# 43-46
    sprite('ny032_03', 4)	# 47-50
    sprite('ny032_04', 4)	# 51-54
    sprite('ny032_01', 4)	# 55-58
    sprite('ny032_02', 4)	# 59-62
    sprite('ny032_03', 4)	# 63-66
    sprite('ny032_04', 4)	# 67-70
    Unknown3038(1)
    Unknown1084(1)
    sprite('null', 32767)	# 71-32837
    loopRest()

@State
def Act2Event_azvsny_00():

    def upon_IMMEDIATE():
        Unknown1000(-60000)
        Unknown2005()
    label(0)
    sprite('ny000_00', 6)	# 1-6
    sprite('ny000_01', 6)	# 7-12
    sprite('ny000_02', 6)	# 13-18
    sprite('ny000_03', 6)	# 19-24
    sprite('ny000_04', 6)	# 25-30
    sprite('ny000_05', 6)	# 31-36
    sprite('ny000_06', 6)	# 37-42
    sprite('ny000_07', 6)	# 43-48
    sprite('ny000_08', 6)	# 49-54
    sprite('ny000_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def Act2Event_azvsny_01():
    sprite('keep', 2)	# 1-2
    sprite('ny003_02', 3)	# 3-5
    Unknown2005()
    sprite('ny003_01', 3)	# 6-8
    sprite('ny003_00', 3)	# 9-11
    Unknown21007(22, 33)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_azvsny_02():
    sprite('keep', 2)	# 1-2
    Unknown21007(22, 34)
    sprite('ny003_02', 3)	# 3-5
    Unknown2005()
    sprite('ny003_01', 3)	# 6-8
    sprite('ny003_00', 3)	# 9-11
    sprite('ny032_00', 2)	# 12-13
    physicsXImpulse(21000)
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    sprite('ny032_01', 4)	# 14-17
    sprite('ny032_02', 4)	# 18-21
    SFX_3('nyse_21')
    physicsXImpulse(0)
    Unknown1047(10000)
    sprite('ny310_00', 3)	# 22-24
    sprite('ny310_01', 3)	# 25-27
    SFX_0('010_swing_sword_0')
    sprite('ny310_02', 3)	# 28-30	 **attackbox here**
    sprite('ny310_03', 16)	# 31-46
    Unknown1084(1)
    Unknown1000(260000)
    sprite('ny310_04', 5)	# 47-51
    sprite('ny310_05', 5)	# 52-56
    sprite('ny310_06', 5)	# 57-61
    label(0)
    sprite('ny000_00', 6)	# 62-67
    sprite('ny000_01', 6)	# 68-73
    sprite('ny000_02', 6)	# 74-79
    sprite('ny000_03', 6)	# 80-85
    sprite('ny000_04', 6)	# 86-91
    sprite('ny000_05', 6)	# 92-97
    sprite('ny000_06', 6)	# 98-103
    sprite('ny000_07', 6)	# 104-109
    sprite('ny000_08', 6)	# 110-115
    sprite('ny000_09', 6)	# 116-121
    loopRest()
    gotoLabel(0)

@State
def Act2Event_azvsny_03():
    sprite('keep', 2)	# 1-2
    sprite('ny003_02', 2)	# 3-4
    Unknown2005()
    sprite('ny003_01', 2)	# 5-6
    sprite('ny003_00', 2)	# 7-8
    sprite('ny431_00', 4)	# 9-12
    sprite('ny431_01', 4)	# 13-16
    sprite('ny431_02', 4)	# 17-20
    sprite('ny431_03', 4)	# 21-24
    sprite('ny431_04', 4)	# 25-28
    SFX_3('nyse_26')
    GFX_0('Event_SummonDDBigSword', -1)
    sprite('ny431_05', 4)	# 29-32
    sprite('ny431_06', 2)	# 33-34
    sprite('ny431_07', 2)	# 35-36
    sprite('ny431_08', 2)	# 37-38
    sprite('ny431_09', 3)	# 39-41
    sprite('ny431_10', 3)	# 42-44
    sprite('ny431_11', 3)	# 45-47
    sprite('ny431_12', 3)	# 48-50
    sprite('ny431_09', 4)	# 51-54
    sprite('ny431_10', 4)	# 55-58
    sprite('ny431_11', 4)	# 59-62
    sprite('ny431_12', 4)	# 63-66
    sprite('ny431_09', 5)	# 67-71
    sprite('ny431_10', 5)	# 72-76
    sprite('ny431_11', 5)	# 77-81
    sprite('ny431_12', 5)	# 82-86
    sprite('ny431_13', 5)	# 87-91
    sprite('ny431_14', 5)	# 92-96
    sprite('ny431_15', 5)	# 97-101
    sprite('ny431_16', 5)	# 102-106
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_CameraCreate():
    sprite('keep', 1)	# 1-1
    GFX_0('Act2Event_Camera_nyvspt', 100)
    enterState('CmnActStand')

@State
def Act2Event_Legacy():
    sprite('ny430_00', 5)	# 1-5
    sprite('ny430_01', 5)	# 6-10
    sprite('ny430_02', 5)	# 11-15
    sprite('ny430_03', 5)	# 16-20
    sprite('ny430_04', 5)	# 21-25
    sprite('ny430_05', 1)	# 26-26
    GFX_0('Act2AZvsNY_SumDDMultiSword', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    sprite('ny430_05', 1)	# 27-27
    GFX_0('NY_SummonDmc', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    sprite('ny430_06', 3)	# 28-30
    sprite('ny430_07', 3)	# 31-33
    sprite('ny430_08', 3)	# 34-36
    sprite('ny430_09', 3)	# 37-39
    sprite('ny430_06', 3)	# 40-42
    sprite('ny430_07', 3)	# 43-45
    sprite('ny430_08', 3)	# 46-48
    sprite('ny430_09', 3)	# 49-51
    sprite('ny430_10', 4)	# 52-55
    sprite('ny430_11', 4)	# 56-59
    sprite('ny430_12', 4)	# 60-63
    enterState('CmnActStand')

@State
def Act2EventWait_azvsny():
    sprite('keep', 1)	# 1-1
    teleportRelativeX(-55000)
    sprite('keep', 1)	# 2-2
    enterState('CmnActStand')

@State
def Act2Event_azvsny00():
    sprite('ny000_00', 6)	# 1-6
    sprite('ny000_01', 6)	# 7-12
    sprite('ny000_02', 6)	# 13-18
    sprite('ny000_03', 6)	# 19-24
    sprite('ny003_02', 3)	# 25-27
    Unknown2005()
    sprite('ny003_01', 3)	# 28-30
    sprite('ny003_00', 3)	# 31-33
    label(0)
    sprite('ny000_00', 6)	# 34-39
    sprite('ny000_01', 6)	# 40-45
    sprite('ny000_02', 6)	# 46-51
    sprite('ny000_03', 6)	# 52-57
    sprite('ny000_04', 6)	# 58-63
    sprite('ny000_05', 6)	# 64-69
    sprite('ny000_06', 6)	# 70-75
    sprite('ny000_07', 6)	# 76-81
    sprite('ny000_08', 6)	# 82-87
    sprite('ny000_09', 6)	# 88-93
    loopRest()
    gotoLabel(0)

@State
def Act2Event_azvsny01():
    sprite('ny032_00', 2)	# 1-2
    Unknown2034(0)
    Unknown2017(0)
    sprite('ny032_00', 2)	# 3-4
    physicsXImpulse(32000)
    sprite('ny032_01', 4)	# 5-8
    sprite('ny032_02', 4)	# 9-12
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 13-16
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 17-20
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 21-24
    sprite('ny032_02', 4)	# 25-28
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 29-32
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 33-36
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 37-40
    sprite('ny032_02', 4)	# 41-44
    sprite('ny032_03', 4)	# 45-48
    sprite('ny032_04', 4)	# 49-52
    sprite('ny032_01', 4)	# 53-56
    sprite('ny032_02', 4)	# 57-60
    sprite('ny032_03', 4)	# 61-64
    sprite('ny032_04', 4)	# 65-68
    sprite('ny032_01', 4)	# 69-72
    sprite('ny032_02', 4)	# 73-76
    sprite('ny032_03', 4)	# 77-80
    sprite('ny032_04', 4)	# 81-84
    sprite('ny032_02', 4)	# 85-88
    sprite('ny032_03', 4)	# 89-92
    sprite('ny032_04', 4)	# 93-96
    Unknown3038(1)
    loopRest()

@State
def Event_Act2EntryFall():
    Unknown1000(-260000)
    teleportRelativeY(640000)
    setGravity(57)

    def upon_3():
        if (SLOT_23 < 120000):
            sendToLabel(1)
    sprite('ny600_00', 1)	# 1-1
    label(0)
    sprite('ny600_00', 6)	# 2-7
    SFX_0('019_cloth_a')
    sprite('ny600_01', 6)	# 8-13
    sprite('ny600_02', 6)	# 14-19
    sprite('ny600_00', 6)	# 20-25
    sprite('ny600_01', 6)	# 26-31
    sprite('ny600_02', 6)	# 32-37
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sendToLabelUpon(2, 3)
    label(2)
    sprite('ny600_03', 15)	# 38-52
    YAccel(60)
    SFX_3('nyse_28')
    SFX_0('019_cloth_a')
    sprite('ny600_03', 15)	# 53-67
    YAccel(60)
    sprite('ny600_03', 15)	# 68-82
    YAccel(60)
    gotoLabel(2)
    label(3)
    clearUponHandler(2)
    sprite('ny600_03', 6)	# 83-88
    Unknown1084(1)
    SFX_0('019_cloth_a')
    sprite('ny600_04', 6)	# 89-94
    SFX_0('201_walk_garden_0')
    sprite('ny600_05', 6)	# 95-100
    Unknown8000(0, 1, 1)
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny600_06', 6)	# 101-106
    sprite('ny600_07', 6)	# 107-112
    sprite('ny600_08', 6)	# 113-118
    sprite('ny600_09', 6)	# 119-124
    sprite('ny600_10', 6)	# 125-130
    label(4)
    sprite('ny600_11', 6)	# 131-136
    sprite('ny600_12', 6)	# 137-142
    sprite('ny600_13', 6)	# 143-148
    sprite('ny600_14', 6)	# 149-154
    gotoLabel(4)

@State
def EventAct2EntryBootMurakumo():
    sprite('ny600_11', 6)	# 1-6
    GFX_0('EntryFallSword', -1)
    SFX_0('011_spin_0')
    SFX_0('005_swing_grap_2_2')
    sprite('ny600_12', 6)	# 7-12
    sprite('ny600_13', 3)	# 13-15
    sprite('ny600_13', 3)	# 16-18
    SFX_3('nyse_28')
    sprite('ny600_14', 6)	# 19-24
    sprite('ny600_11', 6)	# 25-30
    sprite('ny600_12', 6)	# 31-36
    sprite('ny600_13', 6)	# 37-42
    sprite('ny600_14', 6)	# 43-48
    sprite('ny600_15', 6)	# 49-54
    Unknown23118(0)
    Unknown23117(16777215, 30)
    GFX_1('nyef_entrylightA', 0)
    SFX_0('019_cloth_a')
    SFX_3('nyse_03')
    sprite('ny600_16', 12)	# 55-66
    sprite('ny600_17', 6)	# 67-72
    GFX_1('nyef_entrylightB', 0)
    sprite('ny600_18', 6)	# 73-78
    Unknown23117(0, 10)
    sprite('ny600_19', 6)	# 79-84
    SFX_0('022_magiccircle_a')
    sprite('ny600_20', 6)	# 85-90
    sprite('ny600_21', 6)	# 91-96
    sprite('ny600_22', 6)	# 97-102
    sprite('ny600_23', 6)	# 103-108
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventARvsNY():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        Unknown1000(-10000)
    label(0)
    sprite('ny620_08ex01', 4)	# 1-4
    GFX_1('nyef_timeupptc', -1)
    if random_(2, 0, 10):
        SFX_0('014_electric_s')
    sprite('ny620_08ex02', 1)	# 5-5
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('null', 32767)	# 6-32772
    Unknown3038(1)
    Unknown1000(-900000)

@State
def Act2Event_ny_bn():

    def upon_IMMEDIATE():
        Unknown2003(1)

        def upon_32():
            Unknown21007(4, 35)
            Unknown21012('416374324576656e745f6d6f79616d6f7961000000000000000000000000000020000000')
            sendToLabel(1)
    sprite('ny403_00', 2)	# 1-2
    sprite('ny403_01', 2)	# 3-4
    sprite('ny403_02', 2)	# 5-6
    sprite('ny403_03', 2)	# 7-8
    sprite('ny403_07', 2)	# 9-10
    sprite('ny403_08', 2)	# 11-12
    sprite('ny403_09', 3)	# 13-15	 **attackbox here**
    SFX_0('005_swing_grap_2_1')
    Unknown21007(4, 35)
    GFX_0('Act2EventSummonSlowArea', -1)
    Unknown38(4, 1)
    Unknown21007(4, 32)
    GFX_0('NY_SlowHand', 0)
    SLOT_31 = 0
    GFX_0('Act2Event_moyamoya', 0)
    sprite('ny403_10', 3)	# 16-18
    sprite('ny403_11', 6)	# 19-24
    sprite('ny403_12', 6)	# 25-30
    label(0)
    sprite('ny403_09', 3)	# 31-33	 **attackbox here**
    sprite('ny403_10', 3)	# 34-36
    sprite('ny403_11', 6)	# 37-42
    sprite('ny403_12', 6)	# 43-48
    gotoLabel(0)
    label(1)
    sprite('ny403_13', 6)	# 49-54
    sprite('ny403_14', 3)	# 55-57
    sprite('ny403_14', 3)	# 58-60
    enterState('CmnActStand')

@State
def Act2Event_Shake_nyvsbn():

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 8):
            ScreenShake(3000, 2000)
            Unknown2038(-8)
            SFX_0('019_quake_0')
    sprite('keep', 2)	# 1-2
    sprite('ny615_08', 6)	# 3-8	 **attackbox here**
    sprite('ny615_07', 6)	# 9-14	 **attackbox here**
    sprite('ny615_06', 6)	# 15-20	 **attackbox here**
    sprite('ny615_05', 6)	# 21-26	 **attackbox here**
    sprite('ny615_04', 6)	# 27-32	 **attackbox here**
    sprite('ny615_03', 6)	# 33-38	 **attackbox here**
    sprite('ny615_02', 6)	# 39-44	 **attackbox here**
    sprite('ny615_01', 6)	# 45-50	 **attackbox here**
    sprite('ny615_00', 6)	# 51-56	 **attackbox here**
    loopRest()
    label(0)
    sprite('ny000_00', 6)	# 57-62
    sprite('ny000_01', 6)	# 63-68
    sprite('ny000_02', 6)	# 69-74
    sprite('ny000_03', 6)	# 75-80
    sprite('ny000_04', 6)	# 81-86
    sprite('ny000_05', 6)	# 87-92
    sprite('ny000_06', 6)	# 93-98
    sprite('ny000_07', 6)	# 99-104
    sprite('ny000_08', 6)	# 105-110
    sprite('ny000_09', 6)	# 111-116
    loopRest()
    gotoLabel(0)

@State
def Act2EventNYvsCA00():

    def upon_IMMEDIATE():

        def upon_32():
            GFX_0('Act2EventSumDDMultiSword', -1)
            Unknown3029(1)
            Unknown3069(2)
            Unknown3071(3)
            Unknown3074('00000000ff000000000000007f000000')
            Unknown3075('000000007f00000000000000ff000000')
            Unknown3076(1030)
            Unknown3077(1050)
            sendToLabel(0)
        sendToLabelUpon(33, 1)
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    Unknown21007(22, 32)
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    label(2)
    sprite('ny300_04', 40)	# 21-60	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    label(0)
    sprite('ny300_04', 8)	# 61-68	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ny300_04', 8)	# 69-76	 **attackbox here**
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ny300_04', 8)	# 77-84	 **attackbox here**
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ny300_04', 8)	# 85-92	 **attackbox here**
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ny300_04', 8)	# 93-100	 **attackbox here**
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    gotoLabel(0)
    label(1)
    sprite('ny300_04', 3)	# 101-103	 **attackbox here**
    Unknown21012('416374324576656e74456666426172726965720000000000000000000000000020000000')
    Unknown21007(22, 33)
    sprite('ny300_05', 3)	# 104-106	 **attackbox here**
    sprite('ny300_06', 3)	# 107-109	 **attackbox here**
    sprite('ny300_07', 3)	# 110-112	 **attackbox here**
    label(5)
    sprite('ny300_08', 40)	# 113-152	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    loopRest()
    gotoLabel(5)

@State
def Act2EventNYvsCA00End():
    sprite('ny300_10', 4)	# 1-4	 **attackbox here**
    sprite('ny300_11', 4)	# 5-8	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventNYvsCA02():
    sprite('null', 32767)	# 1-32767
    Unknown21007(22, 34)
    Unknown3038(1)

@State
def Act2EventNYvsCA03():
    Unknown2019(-500)
    Unknown3032()
    Unknown2034(0)
    sprite('ny331_00', 2)	# 1-2
    Unknown3001(0)
    Unknown21007(22, 35)
    sprite('ny331_04', 4)	# 3-6
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(10)
    sprite('ny331_05', 6)	# 7-12
    sprite('ny331_06', 6)	# 13-18
    sprite('ny331_07', 6)	# 19-24
    sprite('ny331_05', 6)	# 25-30
    sprite('ny331_06', 6)	# 31-36
    sprite('ny331_07', 6)	# 37-42
    Unknown3001(255)
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 103)
    label(0)
    sprite('ny331_05', 6)	# 43-48
    sprite('ny331_06', 6)	# 49-54
    sprite('ny331_07', 6)	# 55-60
    gotoLabel(0)

@State
def Act2EventNYvsCA04():
    sprite('keep', 2)	# 1-2
    Unknown1084(1)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_RoundWinEnd2():
    sprite('ny615_08', 6)	# 1-6	 **attackbox here**
    sprite('ny615_07', 6)	# 7-12	 **attackbox here**
    sprite('ny615_06', 6)	# 13-18	 **attackbox here**
    sprite('ny615_05', 6)	# 19-24	 **attackbox here**
    sprite('ny615_00', 6)	# 25-30	 **attackbox here**
    loopRest()
    enterState('EventDefEntryWait')

@State
def Act2Event_Signal0():
    sprite('keep', 2)	# 1-2
    Unknown21007(22, 32)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Signal1():
    sprite('keep', 2)	# 1-2
    Unknown21007(22, 33)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Signal2():
    sprite('keep', 2)	# 1-2
    Unknown21007(22, 34)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_BDash():

    def upon_IMMEDIATE():
        Unknown2017(0)
        Unknown2034(0)
    sprite('ny033_00', 3)	# 1-3
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3076(1000)
    Unknown3077(950)
    sprite('ny033_00', 3)	# 4-6
    SFX_3('nyse_22')
    physicsXImpulse(-36000)
    sprite('ny033_01', 2)	# 7-8
    GFX_1('nyef_ny033', 106)
    sprite('ny033_02', 2)	# 9-10
    GFX_1('nyef_ny033', 106)
    sprite('ny033_03', 2)	# 11-12
    sprite('ny033_04', 2)	# 13-14
    sprite('ny033_01', 4)	# 15-18
    sprite('ny033_05', 4)	# 19-22
    sprite('ny033_06', 5)	# 23-27
    sprite('null', 2)	# 28-29
    Unknown1084(1)
    Unknown3038(1)
    sprite('null', 32767)	# 30-32796
    loopRest()

@State
def Act2Event_Down():
    Unknown2004(1, 0)
    sprite('ny070_00', 2)	# 1-2
    sprite('ny070_01', 2)	# 3-4
    sprite('ny070_02', 4)	# 5-8
    sprite('ny070_03', 4)	# 9-12
    sprite('ny070_04', 4)	# 13-16
    sprite('ny070_05', 6)	# 17-22
    Unknown8003(100, 1, 1)
    sprite('ny070_06', 7)	# 23-29
    sprite('ny070_07', 5)	# 30-34
    sprite('ny070_08', 5)	# 35-39
    sprite('ny070_09', 4)	# 40-43
    Unknown8003(100, 1, 1)
    Unknown1004()
    sprite('ny063_11', 32767)	# 44-32810
    Unknown1005()
    loopRest()

@State
def Act3Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act3Event_novsny_00():

    def upon_IMMEDIATE():
        Unknown1000(-960000)
        Unknown2034(0)
    sprite('null', 20)	# 1-20
    sprite('ny430_05', 1)	# 21-21
    GFX_0('Act3Event_NY_SumDDMultiSword', -1)
    Unknown36(1)
    teleportRelativeX(-120000)
    Unknown35()
    sprite('ny430_05', 1)	# 22-22
    sprite('ny430_06', 3)	# 23-25
    sprite('ny430_07', 3)	# 26-28
    Unknown21007(22, 32)
    sprite('ny430_08', 3)	# 29-31
    sprite('ny430_09', 3)	# 32-34
    sprite('ny430_06', 3)	# 35-37
    sprite('ny430_07', 3)	# 38-40
    sprite('ny430_08', 3)	# 41-43
    sprite('ny430_09', 3)	# 44-46
    sprite('ny430_10', 4)	# 47-50
    sprite('ny430_11', 4)	# 51-54
    sprite('ny430_12', 32767)	# 55-32821

@State
def Act3Event_novsny_01():

    def upon_IMMEDIATE():
        Unknown1000(-960000)
        Unknown2034(0)

        def upon_3():
            if SLOT_38:
                if (SLOT_22 < 360000):
                    clearUponHandler(3)
                    sendToLabel(0)
                    physicsXImpulse(0)
                    Unknown1045(10000)
            elif (SLOT_22 > (-360000)):
                clearUponHandler(3)
                sendToLabel(0)
                physicsXImpulse(0)
                Unknown1045(10000)
    sprite('ny032_00', 2)	# 1-2
    physicsXImpulse(24000)
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    label(9)
    sprite('ny032_01', 4)	# 3-6
    sprite('ny032_02', 4)	# 7-10
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 11-14
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ny032_05', 6)	# 19-24
    SFX_3('nyse_22')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_06', 6)	# 25-30
    loopRest()
    Unknown1084(1)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def Act3Event_novsny_02():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('ny000_00', 7)	# 1-7
    sprite('ny070_00', 17)	# 8-24
    GFX_1('ef_hitmd', 103)
    SFX_0('100_hit_grap_1')
    ScreenShake(1000, 20000)
    sprite('ny070_01', 4)	# 25-28
    Unknown1047(-11000)
    sprite('ny070_02', 4)	# 29-32
    sprite('ny070_03', 32767)	# 33-32799
    loopRest()

@State
def Act3Event_novsny_03():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('ny032_00', 2)	# 1-2
    physicsXImpulse(12000)
    Unknown1028(1000)
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    Unknown2037(5)
    label(9)
    sprite('ny032_01', 4)	# 3-6
    Unknown2038(-1)
    sprite('ny032_02', 4)	# 7-10
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 11-14
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    if SLOT_2:
        _gotolabel(9)
    label(0)
    sprite('null', 32767)	# 19-32785
    Unknown1084(1)
    Unknown3038(1)

@State
def Act3Event_novsny_04():
    sprite('ny070_10', 5)	# 1-5
    sprite('ny070_11', 5)	# 6-10
    sprite('ny070_12', 5)	# 11-15
    sprite('ny070_13', 5)	# 16-20
    sprite('ny000_00', 6)	# 21-26
    sprite('ny000_01', 6)	# 27-32
    sprite('ny000_02', 6)	# 33-38
    sprite('ny003_02', 3)	# 39-41
    Unknown2005()
    sprite('ny003_01', 3)	# 42-44
    sprite('ny003_00', 3)	# 45-47
    sprite('ny000_00', 6)	# 48-53
    sprite('ny000_01', 6)	# 54-59
    sprite('ny000_02', 6)	# 60-65
    sprite('ny003_02', 3)	# 66-68
    Unknown2005()
    sprite('ny003_01', 3)	# 69-71
    sprite('ny003_00', 3)	# 72-74
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_havsny_00():
    sprite('ny064_00', 8)	# 1-8
    sprite('ny064_01', 8)	# 9-16
    sprite('ny064_02', 8)	# 17-24
    sprite('ny064_03', 32767)	# 25-32791

@State
def Act3Event_havsny_01():
    sprite('ny064_03', 4)	# 1-4
    GFX_0('Act3Event_TeniObj', -1)
    Unknown3004(-4)
    sprite('ny064_03', 4)	# 5-8
    sprite('ny064_03', 5)	# 9-13
    sprite('ny064_03', 5)	# 14-18
    sprite('ny064_03', 32767)	# 19-32785
    Unknown3038(1)

@State
def Act3Event_havsny_02():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('ny010_01', 3)	# 1-3
    sprite('ny010_00', 3)	# 4-6
    sprite('ny003_02', 3)	# 7-9
    Unknown2005()
    sprite('ny003_01', 3)	# 10-12
    sprite('ny003_00', 3)	# 13-15
    sprite('ny032_00', 2)	# 16-17
    physicsXImpulse(12000)
    Unknown1028(1000)
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    Unknown2037(5)
    label(9)
    sprite('ny032_01', 4)	# 18-21
    Unknown2038(-1)
    sprite('ny032_02', 4)	# 22-25
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 26-29
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 30-33
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    if SLOT_2:
        _gotolabel(9)
    label(0)
    sprite('null', 32767)	# 34-32800
    Unknown1084(1)
    Unknown3038(1)

@State
def Act3Event_nyvsha_00():

    def upon_IMMEDIATE():
        Unknown2034(0)

        def upon_32():
            sendToLabel(1)
    sprite('ny030_00', 7)	# 1-7
    physicsXImpulse(1650)
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
    sprite('ny030_01', 7)	# 78-84
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny030', -1)
    sprite('ny030_02', 7)	# 85-91
    GFX_1('nyef_ny030', -1)
    sprite('ny030_03', 7)	# 92-98
    GFX_1('nyef_ny030', -1)
    sprite('ny030_04', 7)	# 99-105
    GFX_1('nyef_ny030', -1)
    sprite('ny000_00', 6)	# 106-111
    Unknown1084(1)
    label(0)
    sprite('ny000_01', 6)	# 112-117
    sprite('ny000_02', 6)	# 118-123
    sprite('ny000_03', 6)	# 124-129
    sprite('ny000_04', 6)	# 130-135
    sprite('ny000_05', 6)	# 136-141
    sprite('ny000_06', 6)	# 142-147
    sprite('ny000_07', 6)	# 148-153
    sprite('ny000_08', 6)	# 154-159
    sprite('ny000_09', 6)	# 160-165
    sprite('ny000_00', 6)	# 166-171
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ny090_00', 10)	# 172-181
    Unknown1084(1)
    sprite('ny090_00', 10)	# 182-191
    Unknown4045('65665f67697264627265616b000000000000000000000000000000000000000067000000')
    SFX_0('104_guard_grap_1')
    SFX_0('106_guard_crush')
    ScreenShake(3000, 18000)
    Unknown1047(-60000)
    sprite('ny090_01', 4)	# 192-195
    sprite('ny090_02', 6)	# 196-201
    Unknown20000(1)
    sprite('ny090_03', 60)	# 202-261
    sprite('ny090_04', 6)	# 262-267
    Unknown21007(22, 32)
    sprite('ny000_00', 6)	# 268-273
    sprite('ny032_00', 2)	# 274-275
    physicsXImpulse(32000)
    sprite('ny032_01', 4)	# 276-279
    sprite('ny032_02', 4)	# 280-283
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 284-287
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 288-291
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_01', 4)	# 292-295
    sprite('ny032_02', 4)	# 296-299
    SFX_3('nyse_21')
    sprite('ny032_05', 5)	# 300-304
    Unknown1047(10000)
    physicsXImpulse(0)
    sprite('ny032_06', 5)	# 305-309
    sprite('ny032_06', 1)	# 310-310
    Unknown1084(1)
    loopRest()
    gotoLabel(0)

@State
def Act3Event_nyvsha_01():
    sprite('ny203_00', 6)	# 1-6
    sprite('ny203_01', 6)	# 7-12
    sprite('ny203_02', 6)	# 13-18
    sprite('ny203_03', 8)	# 19-26
    sprite('ny203_04', 12)	# 27-38
    sprite('ny203_05', 6)	# 39-44
    sprite('ny203_06', 6)	# 45-50
    sprite('ny203_01', 6)	# 51-56
    sprite('ny203_00', 6)	# 57-62
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_nyvsrm_00():
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 32767)	# 21-32787	 **attackbox here**

@State
def Act3Event_nyvsrm_01():
    sprite('keep', 2)	# 1-2
    sprite('ny300_03', 6)	# 3-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_01', 6)	# 15-20	 **attackbox here**
    sprite('ny300_00', 6)	# 21-26	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_nyvsrm_02():
    label(0)
    sprite('ny611_14', 7)	# 1-7
    sprite('ny611_15', 7)	# 8-14
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_16', 7)	# 15-21
    sprite('ny611_17', 7)	# 22-28
    loopRest()
    sprite('ny611_14', 7)	# 29-35
    sprite('ny611_15', 7)	# 36-42
    sprite('ny611_16', 7)	# 43-49
    sprite('ny611_17', 7)	# 50-56
    loopRest()
    sprite('ny611_14', 7)	# 57-63
    sprite('ny611_15', 7)	# 64-70
    sprite('ny611_16', 7)	# 71-77
    sprite('ny611_17', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def Act3Event_nyvsrm_03():
    sprite('ny611_13', 6)	# 1-6
    GFX_1('nyef_entrymc', 0)
    SFX_3('nyse_28')
    sprite('ny611_10', 6)	# 7-12
    sprite('ny611_09', 6)	# 13-18
    sprite('ny611_08', 6)	# 19-24
    sprite('ny611_07', 6)	# 25-30
    sprite('ny611_06', 6)	# 31-36
    sprite('ny611_05', 6)	# 37-42
    sprite('ny611_04', 6)	# 43-48
    sprite('ny611_03', 6)	# 49-54
    sprite('ny611_02', 7)	# 55-61
    sprite('ny611_01', 7)	# 62-68
    sprite('ny611_00', 7)	# 69-75
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_nyvsrm_04():
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    GFX_0('Event_EF_ny300', 0)
    label(0)
    sprite('ny300_04', 20)	# 41-60	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    sprite('ny300_04', 80)	# 61-140	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Act3Event_nyvsrc_01():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown2017(0)
    sprite('ny032_00', 2)	# 1-2
    physicsXImpulse(12000)
    Unknown1028(1000)
    SFX_3('nyse_20')
    GFX_1('nyef_ny030', -1)
    Unknown2037(5)
    label(9)
    sprite('ny032_01', 4)	# 3-6
    Unknown2038(-1)
    sprite('ny032_02', 4)	# 7-10
    SFX_3('nyse_21')
    sprite('ny032_03', 4)	# 11-14
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    sprite('ny032_04', 4)	# 15-18
    SFX_3('nyse_21')
    GFX_1('nyef_ny032', 106)
    loopRest()
    if SLOT_2:
        _gotolabel(9)
    label(0)
    sprite('null', 32767)	# 19-32785
    Unknown1084(1)
    Unknown3038(1)

@State
def Act3Event_nyvsmu_00():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ny409_00', 3)	# 1-3
    sprite('ny409_01', 1)	# 4-4
    Unknown4004('4775617264437275736857696e64000000000000000000000000000000000000ffff0000')
    sprite('ny409_01', 2)	# 5-6
    sprite('ny409_02', 3)	# 7-9	 **attackbox here**
    sprite('ny409_03', 3)	# 10-12	 **attackbox here**
    sprite('ny409_04', 3)	# 13-15	 **attackbox here**
    sprite('ny409_05', 5)	# 16-20	 **attackbox here**
    SFX_0('006_swing_blade_2')
    sprite('ny409_06', 2)	# 21-22	 **attackbox here**
    sprite('ny409_06', 1)	# 23-23	 **attackbox here**
    Unknown21007(22, 32)
    sprite('ny409_07', 3)	# 24-26	 **attackbox here**
    sprite('ny409_08', 4)	# 27-30	 **attackbox here**
    sprite('ny409_09', 3)	# 31-33	 **attackbox here**
    sprite('ny409_10', 3)	# 34-36
    sprite('ny409_11', 3)	# 37-39
    sprite('ny409_12', 3)	# 40-42
    sprite('ny409_13', 3)	# 43-45
    sprite('ny409_14', 3)	# 46-48
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_nyvsmu_01():
    sprite('ny450_00', 6)	# 1-6
    sprite('ny450_01', 6)	# 7-12
    label(0)
    sprite('ny450_02', 6)	# 13-18
    sprite('ny450_03', 6)	# 19-24
    sprite('ny450_04', 6)	# 25-30
    loopRest()
    gotoLabel(0)

@State
def Act3Event_cevsny_00():
    sprite('ny300_04', 1)	# 1-1	 **attackbox here**
    Unknown21007(22, 32)
    sprite('ny300_04', 10)	# 2-11	 **attackbox here**
    sprite('ny300_05', 6)	# 12-17	 **attackbox here**
    sprite('ny300_06', 6)	# 18-23	 **attackbox here**
    sprite('ny300_07', 6)	# 24-29	 **attackbox here**
    Unknown21012('4576656e745f45465f6e7933303000000000000000000000000000000000000020000000')
    sprite('ny300_08', 8)	# 30-37	 **attackbox here**
    sprite('ny300_09', 20)	# 38-57	 **attackbox here**
    sprite('ny300_10', 4)	# 58-61	 **attackbox here**
    sprite('ny300_11', 4)	# 62-65	 **attackbox here**
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_cevsny_01():

    def upon_3():
        Unknown61(0, 1, 0, 30, 0, 0, 0, 9999, 0, 9999, 0, 9999)
        SLOT_51 = SLOT_0
        if (SLOT_51 > 15):
            if random_(2, 0, 10):
                SFX_0('014_electric_s')
            GFX_1('nyef_timeupptc', -1)
    label(0)
    sprite('ny010_02', 6)	# 1-6
    sprite('ny010_03', 6)	# 7-12
    sprite('ny010_04', 6)	# 13-18
    sprite('ny010_05', 6)	# 19-24
    sprite('ny010_06', 6)	# 25-30
    sprite('ny010_07', 6)	# 31-36
    sprite('ny010_08', 6)	# 37-42
    sprite('ny010_09', 6)	# 43-48
    sprite('ny010_10', 6)	# 49-54
    sprite('ny010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def Act3Event_cevsny_02():

    def upon_IMMEDIATE():
        Unknown2019(-500)
        Unknown2034(0)
        Unknown3032()
    sprite('keep', 26)	# 1-26
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    Unknown3004(-10)
    GFX_0('Act3Event_teni', -1)
    Unknown36(1)
    teleportRelativeX(-20000)
    Unknown1007(120000)
    Unknown35()
    sprite('keep', 1)	# 27-27
    Unknown1000(-500000)
    sprite('null', 32767)	# 28-32794
    loopRest()

@State
def Act3Event_cevsny_03():
    sprite('ny300_00', 4)	# 1-4	 **attackbox here**
    sprite('ny300_01', 4)	# 5-8	 **attackbox here**
    sprite('ny300_02', 6)	# 9-14	 **attackbox here**
    sprite('ny300_03', 6)	# 15-20	 **attackbox here**
    sprite('ny300_04', 20)	# 21-40	 **attackbox here**
    GFX_0('Event_EF_ny300', 0)
    label(0)
    sprite('ny300_04', 100)	# 41-140	 **attackbox here**
    GFX_1('nyef_entrymc', -1)
    SFX_3('nyse_28')
    loopRest()
    gotoLabel(0)