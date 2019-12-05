@Subroutine
def PreInit():
    Unknown12019('62686100000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(18000)
    WalkFSpeed(10000)
    WalkBSpeed(8000)
    DashFInitialVelocity(9000)
    DashFAccel(0)
    Unknown12024(4)
    Unknown13039(0)
    Unknown2049(1)
    Unknown15018(10)
    Move_Register('NmlAtk5A', 0x7)
    Unknown15013(2000)
    Unknown14015(-50000, 450000, -100000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown14015(0, 350000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 650000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown15013(4000)
    Unknown14015(0, 500000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown15009()
    Unknown14015(0, 400000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown15021(1)
    Unknown14015(400000, 750000, -200000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown14015(-1500000, 800000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B3rd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 450000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15021(1500)
    Unknown14015(-100000, 450000, 150000, 600000, 750, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 350000, -140000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown15013(3000)
    Unknown14015(0, 550000, -100000, 200000, 750, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(2000)
    Unknown14015(0, 350000, -300000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown15013(2000)
    Unknown14015(0, 400000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(0, 320000, -270000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15014(1200)
    Unknown15006(1)
    Unknown15013(0)
    Unknown14015(0, 300000, 0, 450000, 250, 0)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Renka', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown14015(0, 350000, -200000, 230000, 250, 0)
    Move_EndRegister()
    Move_Register('Renka_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('Renka')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14013('Renka')
    Unknown15009()
    Unknown15015(10, 11)
    Unknown15022('f4010000e803000000000000e8030000')
    Unknown14015(0, 350000, -200000, 230000, 250, 0)
    Move_EndRegister()
    Move_Register('Zantetu', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown14015(0, 350000, -100000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Zantetu_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('Zantetu')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14013('Zantetu')
    Unknown15008()
    Unknown15015(70, 73)
    Unknown15022('f4010000e803000000000000e8030000')
    Unknown14015(0, 350000, -100000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('RenkaEx', INPUT_SPECIALMOVE)
    Unknown14027('Renka')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15009()
    Unknown14015(0, 350000, -200000, 230000, 250, 0)
    Move_EndRegister()
    Move_Register('RenkaEx_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('Renka')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3089)
    Unknown14005(1)
    Unknown14013('RenkaEx')
    Unknown15009()
    Unknown15015(10, 11)
    Unknown15022('f4010000e803000000000000e8030000')
    Unknown14015(0, 350000, -200000, 230000, 250, 0)
    Move_EndRegister()
    Move_Register('Guren', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15012(0)
    Unknown14015(0, 500000, -200000, 230000, 150, 50)
    Move_EndRegister()
    Move_Register('Guren_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('Guren')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14013('Guren')
    Unknown15006(3000)
    Unknown15012(0)
    Unknown15022('77010000e803000000000000e8030000')
    Unknown14015(0, 500000, -200000, 230000, 150, 50)
    Move_EndRegister()
    Move_Register('GurenB', INPUT_SPECIALMOVE)
    Unknown14027('Guren')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15012(0)
    Unknown14015(0, 800000, -200000, 230000, 150, 50)
    Move_EndRegister()
    Move_Register('GurenB_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('Guren')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14013('GurenB')
    Unknown15006(3000)
    Unknown15012(0)
    Unknown15022('77010000e803000000000000e8030000')
    Unknown14015(0, 800000, -200000, 230000, 150, 50)
    Move_EndRegister()
    Move_Register('Yanagi', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15015(50, 50)
    Unknown15013(1)
    Unknown15014(2000)
    Unknown14015(450000, 1000000, -200000, 150000, 100, 0)
    Move_EndRegister()
    Move_Register('Yanagi_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('Yanagi')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3089)
    Unknown14005(1)
    Unknown14013('Yanagi')
    Unknown15015(50, 50)
    Unknown15013(1)
    Unknown15014(2000)
    Unknown14015(450000, 1000000, -200000, 150000, 100, 0)
    Move_EndRegister()
    Move_Register('Agito', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-50000, 250000, -500000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('Tubaki', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15006(1)
    Unknown15013(0)
    Unknown14015(0, 350000, -300000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('TubakiEx', INPUT_SPECIALMOVE)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15008()
    Unknown15006(1)
    Unknown15013(0)
    Unknown14015(0, 350000, -300000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 400000, -200000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('UltimateAssault_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('UltimateAssault')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x308b)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('UltimateAssault')
    Unknown15005(1)
    Unknown15012(1)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 400000, -200000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Unknown14027('UltimateAssault')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 400000, -200000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('UltimateAssault')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x308b)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('UltimateAssault_OD')
    Unknown15005(1)
    Unknown15012(1)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 400000, -200000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('UltimateGrip', 0x68)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15006(1)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(4000)
    Unknown15011(10000)
    Unknown15015(600, 600)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(-100000, 300000, -200000, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateGrip_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('UltimateGrip')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x308b)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('UltimateGrip')
    Unknown15006(1)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(4000)
    Unknown15011(10000)
    Unknown15015(600, 600)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(-100000, 300000, -200000, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateGrip_OD', 0x68)
    Unknown14027('UltimateGrip')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15006(1)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(4000)
    Unknown15011(10000)
    Unknown15015(600, 600)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(-100000, 300000, -200000, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateGrip_OD_Hasei', INPUT_SPECIALMOVE)
    Unknown14027('UltimateGrip')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x308b)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('UltimateGrip_OD')
    Unknown15006(1)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(4000)
    Unknown15011(10000)
    Unknown15015(600, 600)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(-100000, 300000, -200000, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateAirAssault', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(1500)
    Unknown14015(0, 400000, -500000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssaultOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(1500)
    Unknown14015(0, 400000, -500000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeatGrip', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown14024('AstralCheck')
    Unknown15013(3000)
    Unknown15014(3000)
    Unknown14015(-100000, 500000, -200000, 500000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk2A', 'Guren', 10000000)
    Unknown15024('NmlAtk2B', 'FHighJump', 10000000)
    Unknown15024('NmlAtk2C', 'Renka', 10000000)
    Unknown15024('NmlAtk2C', 'Zantetu', 10000000)
    Unknown15024('NmlAtk2C', 'RenkaEx', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
    Unknown15024('NmlAtk5B3rd', 'Renka', 10000000)
    Unknown15024('NmlAtk5B3rd', 'Zantetu', 10000000)
    Unknown15024('NmlAtk5B3rd', 'RenkaEx', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'UltimateAirAssault', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'UltimateAirAssaultOD', 10000000)
    Unknown15024('RenkaEx', 'FJump', 10000000)
    Unknown12018(0, 'ha062_01')
    Unknown12018(1, 'ha062_03')
    Unknown12018(2, 'ha062_04')
    Unknown12018(3, 'ha062_05')
    Unknown12018(4, 'ha062_05')
    Unknown12018(5, 'ha062_06')
    Unknown12018(6, 'ha062_07')
    Unknown12018(7, 'ha041_02')
    Unknown12018(8, 'ha040_02')
    Unknown12018(9, 'ha045_02')
    Unknown12018(10, 'ha060_00')
    Unknown12018(11, 'ha060_01')
    Unknown12018(12, 'ha060_03')
    Unknown12018(13, 'ha060_05')
    Unknown12018(14, 'ha060_07')
    Unknown12018(15, 'ha060_14')
    Unknown12018(16, 'ha050_00')
    Unknown12018(17, 'ha052_00')
    Unknown12018(18, 'ha054_00')
    Unknown12018(19, 'ha000_00')
    Unknown12018(20, 'ha000_00')
    Unknown12018(25, 'ha063_00')
    Unknown12018(26, 'ha063_01')
    Unknown12018(27, 'ha063_02')
    Unknown12018(28, 'ha063_04')
    Unknown12018(29, 'ha063_10')
    Unknown12018(24, 'ha073_01')
    Unknown7010(0, 'bha000')
    Unknown7010(1, 'bha001')
    Unknown7010(2, 'bha002')
    Unknown7010(3, 'bha003')
    Unknown7010(4, 'bha004')
    Unknown7010(5, 'bha005')
    Unknown7010(6, 'bha006')
    Unknown7010(7, 'bha007')
    Unknown7010(8, 'bha008')
    Unknown7010(9, 'bha009')
    Unknown7010(10, 'bha010')
    Unknown7010(15, 'bha011')
    Unknown7010(16, 'bha012')
    Unknown7010(17, 'bha013')
    Unknown7010(18, 'bha014')
    Unknown7010(19, 'bha015')
    Unknown7010(20, 'bha016')
    Unknown7010(21, 'bha017')
    Unknown7010(22, 'bha018')
    Unknown7010(23, 'bha019')
    Unknown7010(24, 'bha020')
    Unknown7010(25, 'bha021')
    Unknown7010(28, 'bha022')
    Unknown7010(29, 'bha023')
    Unknown7010(30, 'bha024')
    Unknown7010(31, 'bha025')
    Unknown7010(32, 'bha026')
    Unknown7010(33, 'bha027')
    Unknown7010(34, 'bha028')
    Unknown7010(35, 'bha029')
    Unknown7010(36, 'bha030')
    Unknown7010(37, 'bha031')
    Unknown7010(39, 'bha032')
    Unknown7010(42, 'bha033')
    Unknown7010(43, 'bha034')
    Unknown7010(44, 'bha035')
    Unknown7010(45, 'bha036')
    Unknown7010(46, 'bha037')
    Unknown7010(47, 'bha038')
    Unknown7010(48, 'bha039')
    Unknown7010(49, 'bha040')
    Unknown7010(50, 'bha041')
    Unknown7010(52, 'bha042')
    Unknown7010(53, 'bha043')
    Unknown7010(54, 'bha100_0')
    Unknown7010(55, 'bha100_1')
    Unknown7010(56, 'bha100_2')
    Unknown7010(63, 'bha101_0')
    Unknown7010(64, 'bha101_1')
    Unknown7010(65, 'bha101_2')
    Unknown7010(57, 'bha102_0')
    Unknown7010(58, 'bha102_1')
    Unknown7010(59, 'bha102_2')
    Unknown7010(66, 'bha103_0')
    Unknown7010(67, 'bha103_1')
    Unknown7010(68, 'bha103_2')
    Unknown7010(60, 'bha104_0')
    Unknown7010(61, 'bha104_1')
    Unknown7010(62, 'bha104_2')
    Unknown7010(69, 'bha105_0')
    Unknown7010(70, 'bha105_1')
    Unknown7010(71, 'bha105_2')
    Unknown7010(72, 'bha150')
    Unknown7010(73, 'bha151')
    Unknown7010(74, 'bha152')
    Unknown7010(85, 'bha153')
    Unknown7010(87, 'bha154')
    Unknown7010(88, 'bha155')
    Unknown7010(96, 'bha161_0')
    Unknown7010(97, 'bha161_1')
    Unknown7010(92, 'bha162_0')
    Unknown7010(93, 'bha162_1')
    Unknown7010(98, 'bha163_0')
    Unknown7010(99, 'bha163_1')
    Unknown7010(100, 'bha164_0')
    Unknown7010(101, 'bha164_1')
    Unknown7010(105, 'bha165_0')
    Unknown7010(106, 'bha165_1')
    Unknown7010(102, 'bha166_0')
    Unknown7010(103, 'bha166_1')
    Unknown7010(90, 'bha167_0')
    Unknown7010(91, 'bha167_1')
    Unknown7010(107, 'bha168_0')
    Unknown7010(108, 'bha168_1')
    Unknown7010(110, 'bha169_0')
    Unknown7010(111, 'bha169_1')
    Unknown7010(112, 'bha159_0')
    Unknown7010(113, 'bha159_1')
    Unknown7010(94, 'bha400_0')
    Unknown7010(95, 'bha400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('04000000556c74696d617465477269700000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465477269705f4f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnActionBegin():
    if Unknown23177():
        SLOT_59 = 1

@Subroutine
def OnDamage():
    if (not SLOT_59):
        SLOT_59 = 1

@Subroutine
def OnFrameStep():
    if SLOT_37:
        SLOT_65 = 0

@Subroutine
def HakumenShotDelete():
    SLOT_57 = 1

    def upon_42():
        if SLOT_57:
            ConsumeSuperMeter(1250)
            SLOT_57 = (SLOT_57 + (-1))
            Unknown23090(8)
            GFX_0('ShotDelete', 102)
            Unknown38(8, 1)
    GuardPoint_(1)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown22031(0, 0)
    Unknown22032(1)

@Subroutine
def CheckAirAssault2Available():
    if (not SLOT_65):
        SLOT_47 = 1

@Subroutine
def AstralCheck():
    SLOT_47 = 0
    if (not Unknown48('19000000020000000000000016000000020000004b000000')):
        SLOT_47 = 1
    else:
        Unknown36(22)
        Unknown23148('CmnActChangePartnerIn')
        random_(1, 2, 0)
        Unknown48('16000000020000002f000000190000000200000000000000')
        Unknown35()

@State
def CmnActStand():
    label(0)
    sprite('ha000_00', 7)	# 1-7
    sprite('ha000_01', 7)	# 8-14
    sprite('ha000_02', 7)	# 15-21
    sprite('ha000_03', 7)	# 22-28
    sprite('ha000_04', 7)	# 29-35
    sprite('ha000_05', 7)	# 36-42
    sprite('ha000_06', 7)	# 43-49
    sprite('ha000_07', 7)	# 50-56
    sprite('ha000_08', 7)	# 57-63
    sprite('ha000_09', 7)	# 64-70
    sprite('ha000_10', 7)	# 71-77
    sprite('ha000_11', 7)	# 78-84
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('ha001_00', 6)	# 85-90
    SFX_4('bha000')
    SLOT_88 = 960
    sprite('ha001_01', 6)	# 91-96
    sprite('ha001_02', 6)	# 97-102
    sprite('ha001_03', 6)	# 103-108
    sprite('ha001_04', 6)	# 109-114
    sprite('ha001_05', 6)	# 115-120
    sprite('ha001_06', 6)	# 121-126
    sprite('ha001_07', 6)	# 127-132
    SFX_3('hase_22')
    sprite('ha001_08', 6)	# 133-138
    sprite('ha001_09', 6)	# 139-144
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ha003_01ex01', 3)	# 1-3
    sprite('ha003_00', 3)	# 4-6
    sprite('ha003_01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('ha010_00', 4)	# 1-4
    sprite('ha010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ha010_02', 6)	# 1-6
    sprite('ha010_03', 6)	# 7-12
    sprite('ha010_04', 6)	# 13-18
    sprite('ha010_05', 6)	# 19-24
    sprite('ha010_06', 6)	# 25-30
    sprite('ha010_07', 6)	# 31-36
    sprite('ha010_08', 6)	# 37-42
    sprite('ha010_09', 6)	# 43-48
    sprite('ha010_10', 6)	# 49-54
    sprite('ha010_11', 6)	# 55-60
    sprite('ha010_12', 6)	# 61-66
    sprite('ha010_13', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ha013_01ex01', 3)	# 1-3
    sprite('ha013_00', 3)	# 4-6
    sprite('ha013_01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ha010_01', 4)	# 1-4
    sprite('ha010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    SLOT_59 = 1
    sprite('ha023_00', 2)	# 1-2
    sprite('ha023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ha020_00', 4)	# 1-4
    sprite('ha020_01', 4)	# 5-8
    SFX_4('ha002')
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ha020_02', 3)	# 1-3
    sprite('ha020_03', 3)	# 4-6

@State
def CmnActJumpDown():
    sprite('ha020_04', 3)	# 1-3
    sprite('ha020_05', 3)	# 4-6
    label(0)
    sprite('ha020_06', 3)	# 7-9
    sprite('ha020_07', 4)	# 10-13
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ha024_00', 3)	# 1-3
    sprite('ha024_01', 3)	# 4-6
    sprite('ha024_02', 3)	# 7-9
    sprite('ha024_03', 3)	# 10-12
    sprite('ha024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('ha024_00', 2)	# 1-2
    sprite('ha024_01', 2)	# 3-4
    sprite('ha024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('ha024_03', 3)	# 1-3
    sprite('ha024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ha030_00', 7)	# 1-7
    label(0)
    sprite('ha030_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('ha030_02', 7)	# 15-21
    sprite('ha030_03', 7)	# 22-28
    sprite('ha030_04', 7)	# 29-35
    sprite('ha030_05', 7)	# 36-42
    sprite('ha030_06', 7)	# 43-49
    sprite('ha030_07', 7)	# 50-56
    sprite('ha030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('ha031_00', 7)	# 1-7
    label(0)
    sprite('ha031_01', 7)	# 8-14
    sprite('ha031_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('ha031_03', 7)	# 22-28
    sprite('ha031_04', 7)	# 29-35
    sprite('ha031_05', 7)	# 36-42
    sprite('ha031_06', 7)	# 43-49
    sprite('ha031_07', 7)	# 50-56
    sprite('ha031_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        sendToLabelUpon(2, 1)
        Unknown1084(1)
        Unknown23001(100, 0)
        SLOT_56 = 1
        if (not SLOT_IsUnlimitedCharacter):
            WhiffCancel('CmnActInvincibleAttack')
            WhiffCancel('Guren')
            WhiffCancel('GurenB')
            WhiffCancel('Yanagi')
            WhiffCancel('Renka')
            WhiffCancel('RenkaEx')
            WhiffCancel('Zantetu')
            WhiffCancel('Agito')
            WhiffCancel('Tubaki')
            WhiffCancel('TubakiEx')
            WhiffCancel('UltimateAssault')
            WhiffCancel('UltimateAssault_OD')
            WhiffCancel('UltimateGrip_OD')
            WhiffCancel('AstralHeatGrip')
    sprite('ha032_00', 2)	# 1-2
    Unknown13008(1)
    Unknown1051(50)
    Unknown1047(17360)
    Unknown1052(1)
    sprite('ha032_01', 2)	# 3-4
    Unknown8006(100, 0, 1)
    physicsXImpulse(25000)
    sprite('ha032_02', 1)	# 5-5
    Unknown1045(9920)
    teleportRelativeX(50000)
    Unknown13008(0)
    physicsXImpulse(30000)
    physicsYImpulse(5000)
    setGravity(2000)
    label(0)
    sprite('ha032_03', 3)	# 6-8
    WhiffCancelEnable(1)
    sprite('ha032_04', 3)	# 9-11
    sprite('ha032_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    sprite('ha032_05', 1)	# 15-15
    Unknown1052(0)
    Unknown13015(1)
    Unknown13014(1)
    Unknown13008(1)
    Unknown13002(1)
    Unknown13003(1)
    Unknown13019(1)
    Unknown8000(100, 1, 1)
    Unknown1019(0)
    Unknown1051(30)
    sprite('ha032_06', 2)	# 16-17
    sprite('ha032_07', 1)	# 18-18

@State
def CmnActFDashStop():
    sprite('ha000_00', 3)	# 1-3

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        sendToLabelUpon(2, 1)
        setInvincibleFor(7)
        Unknown1084(1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('ha033_00', 2)	# 1-2
    sprite('ha033_01', 2)	# 3-4
    Unknown8006(100, 0, 1)
    sprite('ha033_02', 3)	# 5-7
    physicsXImpulse(-36000)
    physicsYImpulse(3000)
    setGravity(2000)
    Unknown1028(3000)
    label(0)
    sprite('ha033_02ex01', 3)	# 8-10
    WhiffCancelEnable(1)
    sprite('ha033_02ex02', 3)	# 11-13
    sprite('ha033_02', 3)	# 14-16
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(2)
    sprite('ha033_03', 1)	# 17-17
    sprite('ha033_04', 2)	# 18-19
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ha033_05', 2)	# 20-21

@State
def CmnActBDashLanding():
    sprite('ha000_00', 3)	# 1-3

@State
def CmnActAirFDash():
    sprite('ha035_00', 3)	# 1-3
    label(0)
    sprite('ha035_01', 3)	# 4-6
    sprite('ha035_01ex01', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ha036_00', 3)	# 1-3
    label(0)
    sprite('ha036_01', 3)	# 4-6
    sprite('ha036_01ex01', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ha050_00', 1)	# 1-1
    sprite('ha050_01', 7)	# 2-8
    sprite('ha050_00', 2)	# 9-10

@State
def CmnActHitStandLv2():
    sprite('ha050_01', 1)	# 1-1
    sprite('ha050_02', 7)	# 2-8
    sprite('ha050_01', 2)	# 9-10
    sprite('ha050_00', 2)	# 11-12

@State
def CmnActHitStandLv3():
    sprite('ha050_02', 1)	# 1-1
    sprite('ha050_03', 7)	# 2-8
    sprite('ha050_02', 2)	# 9-10
    sprite('ha050_01', 2)	# 11-12
    sprite('ha050_00', 2)	# 13-14

@State
def CmnActHitStandLv4():
    sprite('ha050_03', 1)	# 1-1
    sprite('ha050_04', 8)	# 2-9
    sprite('ha050_03', 2)	# 10-11
    sprite('ha050_02', 2)	# 12-13
    sprite('ha050_01', 2)	# 14-15
    sprite('ha050_00', 2)	# 16-17

@State
def CmnActHitStandLv5():
    sprite('ha050_04', 1)	# 1-1
    sprite('ha050_04', 8)	# 2-9
    sprite('ha050_03', 2)	# 10-11
    sprite('ha050_02', 2)	# 12-13
    sprite('ha050_01', 2)	# 14-15
    sprite('ha050_00', 4)	# 16-19

@State
def CmnActHitStandLowLv1():
    sprite('ha052_00', 1)	# 1-1
    sprite('ha052_01', 7)	# 2-8
    sprite('ha052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv2():
    sprite('ha052_01', 1)	# 1-1
    sprite('ha052_02', 7)	# 2-8
    sprite('ha052_01', 2)	# 9-10
    sprite('ha052_00', 2)	# 11-12

@State
def CmnActHitStandLowLv3():
    sprite('ha052_02', 1)	# 1-1
    sprite('ha052_03', 7)	# 2-8
    sprite('ha052_02', 2)	# 9-10
    sprite('ha052_01', 2)	# 11-12
    sprite('ha052_00', 2)	# 13-14

@State
def CmnActHitStandLowLv4():
    sprite('ha052_03', 1)	# 1-1
    sprite('ha052_04', 8)	# 2-9
    sprite('ha052_03', 2)	# 10-11
    sprite('ha052_02', 2)	# 12-13
    sprite('ha052_01', 2)	# 14-15
    sprite('ha052_00', 2)	# 16-17

@State
def CmnActHitStandLowLv5():
    sprite('ha052_04', 1)	# 1-1
    sprite('ha052_04', 23)	# 2-24
    sprite('ha052_04', 2)	# 25-26
    sprite('ha052_03', 2)	# 27-28
    sprite('ha052_02', 2)	# 29-30
    sprite('ha052_01', 2)	# 31-32
    sprite('ha052_00', 2)	# 33-34

@State
def CmnActHitCrouchLv1():
    sprite('ha054_00', 1)	# 1-1
    sprite('ha054_01', 9)	# 2-10
    sprite('ha054_00', 2)	# 11-12

@State
def CmnActHitCrouchLv2():
    sprite('ha054_01', 1)	# 1-1
    sprite('ha054_02', 11)	# 2-12
    sprite('ha054_01', 2)	# 13-14
    sprite('ha054_00', 2)	# 15-16

@State
def CmnActHitCrouchLv3():
    sprite('ha054_02', 1)	# 1-1
    sprite('ha054_03', 12)	# 2-13
    sprite('ha054_02', 2)	# 14-15
    sprite('ha054_01', 2)	# 16-17
    sprite('ha054_00', 2)	# 18-19

@State
def CmnActHitCrouchLv4():
    sprite('ha054_03', 1)	# 1-1
    sprite('ha054_04', 12)	# 2-13
    sprite('ha054_03', 2)	# 14-15
    sprite('ha054_02', 2)	# 16-17
    sprite('ha054_01', 2)	# 18-19
    sprite('ha054_00', 2)	# 20-21

@State
def CmnActHitCrouchLv5():
    sprite('ha054_04', 1)	# 1-1
    sprite('ha054_04', 25)	# 2-26
    sprite('ha054_04', 2)	# 27-28
    sprite('ha054_03', 2)	# 29-30
    sprite('ha054_02', 2)	# 31-32
    sprite('ha054_01', 2)	# 33-34
    sprite('ha054_00', 2)	# 35-36

@State
def CmnActBDownUpper():
    sprite('ha060_00', 4)	# 1-4
    label(0)
    sprite('ha060_01', 4)	# 5-8
    sprite('ha060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ha062_03', 3)	# 1-3

@State
def CmnActBDownDown():
    sprite('ha062_05', 3)	# 1-3
    label(0)
    sprite('ha062_06', 3)	# 4-6
    sprite('ha062_06ex00', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ha062_07', 2)	# 1-2
    sprite('ha062_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('ha063_06', 2)	# 1-2
    sprite('ha063_07', 2)	# 3-4
    sprite('ha063_08', 3)	# 5-7
    sprite('ha063_09', 3)	# 8-10
    sprite('ha063_10', 2)	# 11-12

@State
def CmnActBDownLoop():
    sprite('ha063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('ha064_00', 2)	# 1-2
    sprite('ha064_01', 2)	# 3-4
    sprite('ha064_02', 2)	# 5-6
    sprite('ha064_03', 2)	# 7-8
    sprite('ha064_04', 2)	# 9-10
    sprite('ha064_05', 2)	# 11-12
    sprite('ha064_06', 2)	# 13-14
    sprite('ha064_07', 2)	# 15-16
    sprite('ha064_08', 2)	# 17-18
    sprite('ha064_09', 2)	# 19-20
    sprite('ha064_10', 2)	# 21-22

@State
def CmnActFDownUpper():
    sprite('ha063_00', 4)	# 1-4

@State
def CmnActFDownUpperEnd():
    sprite('ha063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ha063_02', 3)	# 1-3
    sprite('ha063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ha063_04', 3)	# 1-3
    sprite('ha063_05', 1)	# 4-4

@State
def CmnActFDownBound():
    sprite('ha063_06', 2)	# 1-2
    sprite('ha063_07', 2)	# 3-4
    sprite('ha063_08', 3)	# 5-7
    sprite('ha063_09', 3)	# 8-10
    sprite('ha063_10', 2)	# 11-12

@State
def CmnActFDownLoop():
    sprite('ha063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ha064_00', 2)	# 1-2
    sprite('ha064_01', 2)	# 3-4
    sprite('ha064_02', 2)	# 5-6
    sprite('ha064_03', 2)	# 7-8
    sprite('ha064_04', 2)	# 9-10
    sprite('ha064_05', 2)	# 11-12
    sprite('ha064_06', 2)	# 13-14
    sprite('ha064_07', 2)	# 15-16
    sprite('ha064_08', 2)	# 17-18
    sprite('ha064_09', 2)	# 19-20
    sprite('ha064_10', 2)	# 21-22

@State
def CmnActVDownUpper():
    sprite('ha062_00', 3)	# 1-3
    label(0)
    sprite('ha062_01', 3)	# 4-6
    sprite('ha062_01ex00', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ha062_02', 3)	# 1-3
    sprite('ha062_03', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('ha062_05', 3)	# 1-3
    label(0)
    sprite('ha062_06', 3)	# 4-6
    sprite('ha062_06ex00', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ha062_07', 2)	# 1-2
    sprite('ha062_08', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('ha072_00', 3)	# 1-3
    sprite('ha072_01', 3)	# 4-6
    sprite('ha072_02', 3)	# 7-9
    label(0)
    sprite('ha072_01', 3)	# 10-12
    sprite('ha072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ha074_00', 3)	# 1-3
    sprite('ha074_01', 3)	# 4-6
    sprite('ha074_02', 3)	# 7-9
    sprite('ha074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    pass

@State
def CmnActFreeze():
    sprite('ha071_05', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ha073_00', 3)	# 1-3
    sprite('ha073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ha073_02', 3)	# 1-3
    label(0)
    sprite('ha073_03', 3)	# 4-6
    sprite('ha073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ha070_00', 4)	# 1-4
    sprite('ha070_01', 4)	# 5-8
    label(0)
    sprite('ha070_02', 4)	# 9-12
    sprite('ha070_03', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ha070_04', 3)	# 1-3
    sprite('ha070_05', 3)	# 4-6
    sprite('ha070_06', 3)	# 7-9
    sprite('ha070_07', 3)	# 10-12
    sprite('ha070_08', 3)	# 13-15
    sprite('ha070_09', 3)	# 16-18
    sprite('ha070_10', 3)	# 19-21

@State
def CmnActUkemiStagger():
    sprite('ha070_11', 2)	# 1-2
    sprite('ha070_12', 3)	# 3-5
    sprite('ha070_13', 3)	# 6-8

@State
def CmnActUkemiAirF():
    sprite('ha113_00', 3)	# 1-3
    sprite('ha113_01', 3)	# 4-6
    sprite('ha113_02', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('ha113_00', 3)	# 1-3
    sprite('ha113_01', 3)	# 4-6
    sprite('ha113_02', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('ha113_00', 3)	# 1-3
    sprite('ha113_01', 3)	# 4-6
    sprite('ha113_02', 9)	# 7-15

@State
def CmnActUkemiLandF():
    sprite('ha110_00', 2)	# 1-2
    sprite('ha110_01', 2)	# 3-4
    sprite('ha110_02', 2)	# 5-6
    sprite('ha110_03', 2)	# 7-8
    sprite('ha110_04', 2)	# 9-10
    sprite('ha110_05', 2)	# 11-12
    sprite('ha110_06', 2)	# 13-14
    sprite('ha110_07', 2)	# 15-16
    sprite('ha110_08', 200)	# 17-216
    sprite('ha110_09', 2)	# 217-218
    sprite('ha110_10', 2)	# 219-220
    sprite('ha110_11', 2)	# 221-222

@State
def CmnActUkemiLandB():
    sprite('ha111_00', 3)	# 1-3
    sprite('ha111_01', 3)	# 4-6
    sprite('ha111_02', 3)	# 7-9
    sprite('ha111_03', 3)	# 10-12
    sprite('ha111_04', 3)	# 13-15
    sprite('ha111_05', 3)	# 16-18
    sprite('ha111_06', 3)	# 19-21
    sprite('ha111_07', 200)	# 22-221
    sprite('ha111_08', 2)	# 222-223
    sprite('ha111_09', 2)	# 224-225
    sprite('ha111_10', 2)	# 226-227

@State
def CmnActUkemiLandN():
    sprite('ha112_00', 2)	# 1-2
    sprite('ha112_01', 2)	# 3-4
    sprite('ha112_02', 2)	# 5-6
    sprite('ha112_03', 2)	# 7-8
    sprite('ha112_04', 2)	# 9-10
    sprite('ha112_05', 2)	# 11-12
    sprite('ha112_06', 2)	# 13-14
    sprite('ha112_07', 3)	# 15-17
    sprite('ha112_08', 14)	# 18-31

@State
def CmnActUkemiLandNLanding():
    sprite('ha024_00', 3)	# 1-3
    sprite('ha024_01', 3)	# 4-6
    sprite('ha024_02', 3)	# 7-9
    sprite('ha024_03', 3)	# 10-12
    sprite('ha024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('ha040_00', 3)	# 1-3
    sprite('ha040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ha040_02', 3)	# 1-3
    sprite('ha040_02ex01', 3)	# 4-6
    sprite('ha040_02ex02', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ha040_01', 3)	# 1-3
    sprite('ha040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ha040_03', 3)	# 1-3
    sprite('ha040_02', 3)	# 4-6

@State
def CmnActMidHeavyGuardEnd():
    sprite('ha040_01', 3)	# 1-3
    sprite('ha040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ha041_00', 3)	# 1-3
    sprite('ha041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('ha041_02', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('ha041_01', 3)	# 1-3
    sprite('ha041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ha041_03', 3)	# 1-3
    sprite('ha041_02', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('ha041_01', 3)	# 1-3
    sprite('ha041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ha043_00', 3)	# 1-3
    sprite('ha043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ha043_02', 3)	# 1-3
    sprite('ha043_02ex01', 3)	# 4-6
    sprite('ha043_02ex02', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ha043_01', 3)	# 1-3
    sprite('ha043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ha043_03', 3)	# 1-3
    sprite('ha043_02', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ha043_01', 3)	# 1-3
    sprite('ha043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ha045_00', 3)	# 1-3
    sprite('ha045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ha045_02', 3)	# 1-3
    sprite('ha045_02ex01', 3)	# 4-6
    sprite('ha045_02ex02', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ha045_01', 3)	# 1-3
    sprite('ha045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ha045_03', 3)	# 1-3
    sprite('ha045_02', 3)	# 4-6

@State
def CmnActAirHeavyGuardEnd():
    sprite('ha045_01', 3)	# 1-3
    sprite('ha045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ha090_00', 2)	# 1-2
    sprite('ha090_01', 2)	# 3-4
    sprite('ha090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ha090_03', 6)	# 6-11
    sprite('ha090_04', 5)	# 12-16

@State
def CmnActGuardBreakCrouch():
    sprite('ha091_00', 2)	# 1-2
    sprite('ha091_01', 2)	# 3-4
    sprite('ha091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ha091_03', 6)	# 6-11
    sprite('ha091_04', 5)	# 12-16

@State
def CmnActGuardBreakAir():
    sprite('ha092_00', 2)	# 1-2
    sprite('ha092_01', 2)	# 3-4
    sprite('ha092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ha092_03', 6)	# 6-11
    sprite('ha092_04', 5)	# 12-16

@State
def CmnActAirTurn():
    sprite('ha025_01ex01', 4)	# 1-4
    sprite('ha025_00', 4)	# 5-8
    sprite('ha025_01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('ha040_02', 1)	# 1-1
    sprite('ha040_01', 3)	# 2-4
    sprite('ha040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('ha312_00', 3)	# 1-3
    sprite('ha312_01', 3)	# 4-6
    sprite('ha312_02', 4)	# 7-10
    sprite('ha312_03', 6)	# 11-16	 **attackbox here**
    sprite('ha312_04', 5)	# 17-21
    sprite('ha312_05', 4)	# 22-25
    sprite('ha312_06', 4)	# 26-29

@State
def CmnActAirLockWait():
    sprite('ha045_02', 1)	# 1-1
    sprite('ha045_01', 3)	# 2-4
    sprite('ha045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ha322_00', 2)	# 1-2
    sprite('ha322_01', 2)	# 3-4
    sprite('ha322_02', 8)	# 5-12
    sprite('ha322_03', 2)	# 13-14
    sprite('ha322_04', 3)	# 15-17	 **attackbox here**
    sprite('ha322_05', 3)	# 18-20
    sprite('ha322_06', 9)	# 21-29

@State
def CmnActLandSpin():
    sprite('ha071_00', 4)	# 1-4
    sprite('ha071_01', 4)	# 5-8
    label(0)
    sprite('ha071_02', 2)	# 9-10
    sprite('ha071_03', 2)	# 11-12
    sprite('ha071_04', 2)	# 13-14
    sprite('ha071_05', 2)	# 15-16
    sprite('ha071_06', 2)	# 17-18
    sprite('ha071_07', 2)	# 19-20
    sprite('ha071_08', 2)	# 21-22
    sprite('ha071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ha071_10', 6)	# 1-6
    sprite('ha071_11', 5)	# 7-11
    sprite('ha071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('ha071_02', 2)	# 1-2
    sprite('ha071_03', 2)	# 3-4
    sprite('ha071_04', 2)	# 5-6
    sprite('ha071_05', 2)	# 7-8
    sprite('ha071_06', 2)	# 9-10
    sprite('ha071_07', 2)	# 11-12
    sprite('ha071_08', 2)	# 13-14
    sprite('ha071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('ha077_00', 2)	# 1-2
    sprite('ha077_01', 2)	# 3-4
    sprite('ha077_00ex01', 2)	# 5-6
    sprite('ha077_01ex01', 2)	# 7-8
    sprite('ha077_00ex02', 2)	# 9-10
    sprite('ha077_01ex02', 2)	# 11-12
    sprite('ha077_00ex03', 2)	# 13-14
    sprite('ha077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ha077_02', 4)	# 1-4
    label(0)
    sprite('ha077_03', 3)	# 5-7
    sprite('ha077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ha077_05', 3)	# 1-3
    sprite('ha077_06', 3)	# 4-6
    sprite('ha077_07', 3)	# 7-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('ha060_07', 4)	# 1-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ha060_11', 5)	# 1-5
    sprite('ha060_12', 4)	# 6-9

@State
def CmnActBurstBegin():
    sprite('ha331_00', 2)	# 1-2
    sprite('ha331_01', 2)	# 3-4
    label(0)
    sprite('ha331_02', 3)	# 5-7
    sprite('ha331_03', 3)	# 8-10
    sprite('ha331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ha331_05', 3)	# 1-3
    label(0)
    sprite('ha331_06', 3)	# 4-6
    sprite('ha331_07', 3)	# 7-9
    sprite('ha331_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ha331_09', 2)	# 1-2
    sprite('ha331_10', 2)	# 3-4
    sprite('ha331_11', 2)	# 5-6

@State
def CmnActAirBurstBegin():
    sprite('ha332_00', 3)	# 1-3
    label(0)
    sprite('ha332_01', 3)	# 4-6
    sprite('ha332_02', 3)	# 7-9
    sprite('ha332_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ha332_04', 3)	# 1-3
    label(0)
    sprite('ha332_05', 3)	# 4-6
    sprite('ha332_06', 3)	# 7-9
    sprite('ha332_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ha332_08', 3)	# 1-3
    sprite('ha332_09', 3)	# 4-6
    sprite('ha020_04', 3)	# 7-9
    sprite('ha020_05', 3)	# 10-12
    label(0)
    sprite('ha020_06', 4)	# 13-16
    sprite('ha020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ha450_00', 3)	# 1-3
    sprite('ha450_01', 3)	# 4-6
    sprite('ha450_02', 3)	# 7-9
    sprite('ha450_03', 32767)	# 10-32776
    GFX_0('EMB_HA_OD', -1)
    SLOT_58 = 1
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ha450_07', 2)	# 1-2
    SLOT_58 = 1
    sprite('ha450_08', 2)	# 3-4
    sprite('ha450_09', 2)	# 5-6
    sprite('ha450_10', 2)	# 7-8
    sprite('ha450_11', 3)	# 9-11
    sprite('ha450_12', 3)	# 12-14
    sprite('ha450_13', 3)	# 15-17
    sprite('ha450_14', 3)	# 18-20
    sprite('ha450_15', 3)	# 21-23
    sprite('ha450_16', 3)	# 24-26
    sprite('ha450_17', 32767)	# 27-32793

@State
def CmnActOverDriveEnd():
    sprite('ha450_20', 3)	# 1-3
    sprite('ha450_21', 3)	# 4-6
    sprite('ha450_22', 3)	# 7-9
    sprite('ha450_23', 3)	# 10-12

@State
def CmnActAirOverDriveBegin():
    sprite('ha333_00', 3)	# 1-3
    sprite('ha333_01', 3)	# 4-6
    sprite('ha333_02', 3)	# 7-9
    sprite('ha333_03', 32767)	# 10-32776
    GFX_0('EMB_HA_OD', -1)
    SLOT_58 = 1
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ha333_04', 3)	# 1-3
    SLOT_58 = 1
    sprite('ha333_05', 3)	# 4-6
    sprite('ha333_06', 3)	# 7-9
    sprite('ha333_07', 3)	# 10-12
    sprite('ha333_08', 32767)	# 13-32779
    loopRest()

@State
def CmnActAirOverDriveEnd():
    sprite('ha333_09', 2)	# 1-2
    sprite('ha333_10', 2)	# 3-4
    sprite('ha333_11', 2)	# 5-6
    sprite('ha020_04', 3)	# 7-9
    sprite('ha020_05', 3)	# 10-12
    label(0)
    sprite('ha020_06', 4)	# 13-16
    sprite('ha020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ha450_00', 3)	# 1-3
    sprite('ha450_01', 3)	# 4-6
    sprite('ha450_02', 3)	# 7-9
    sprite('ha450_03', 32767)	# 10-32776
    GFX_0('EMB_HA_OD', -1)
    SLOT_58 = 1
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ha450_07', 2)	# 1-2
    SLOT_58 = 1
    sprite('ha450_08', 2)	# 3-4
    sprite('ha450_09', 2)	# 5-6
    sprite('ha450_10', 2)	# 7-8
    sprite('ha450_11', 3)	# 9-11
    sprite('ha450_12', 3)	# 12-14
    sprite('ha450_13', 3)	# 15-17
    sprite('ha450_14', 3)	# 18-20
    sprite('ha450_15', 3)	# 21-23
    sprite('ha450_16', 3)	# 24-26
    sprite('ha450_17', 32767)	# 27-32793

@State
def CmnActCrossRushEnd():
    sprite('ha450_20', 3)	# 1-3
    sprite('ha450_21', 3)	# 4-6
    sprite('ha450_22', 3)	# 7-9
    Unknown3060('000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ha450_23', 3)	# 10-12

@State
def CmnActAirCrossRushBegin():
    sprite('ha333_00', 3)	# 1-3
    sprite('ha333_01', 3)	# 4-6
    sprite('ha333_02', 3)	# 7-9
    sprite('ha333_03', 32767)	# 10-32776
    GFX_0('EMB_HA_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ha333_04', 3)	# 1-3
    SLOT_58 = 1
    sprite('ha333_05', 3)	# 4-6
    sprite('ha333_06', 3)	# 7-9
    sprite('ha333_07', 3)	# 10-12
    sprite('ha333_08', 32767)	# 13-32779
    loopRest()

@State
def CmnActAirCrossRushEnd():
    sprite('ha333_09', 2)	# 1-2
    sprite('ha333_10', 2)	# 3-4
    sprite('ha333_11', 2)	# 5-6
    sprite('ha020_04', 3)	# 7-9
    sprite('ha020_05', 3)	# 10-12
    label(0)
    sprite('ha020_06', 4)	# 13-16
    sprite('ha020_07', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('ha331_00', 2)	# 1-2
    sprite('ha331_01', 2)	# 3-4
    label(0)
    sprite('ha331_02', 3)	# 5-7
    sprite('ha331_03', 3)	# 8-10
    sprite('ha331_04', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('ha331_05', 3)	# 1-3
    label(0)
    sprite('ha331_06', 3)	# 4-6
    sprite('ha331_07', 3)	# 7-9
    sprite('ha331_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ha331_09', 2)	# 1-2
    sprite('ha331_10', 2)	# 3-4
    sprite('ha331_11', 2)	# 5-6

@State
def CmnActAirCrossChangeBegin():
    sprite('ha332_00', 3)	# 1-3
    label(0)
    sprite('ha332_01', 3)	# 4-6
    sprite('ha332_02', 3)	# 7-9
    sprite('ha332_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('ha332_04', 3)	# 1-3
    label(0)
    sprite('ha332_05', 3)	# 4-6
    sprite('ha332_06', 3)	# 7-9
    sprite('ha332_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ha332_08', 3)	# 1-3
    sprite('ha332_09', 3)	# 4-6
    sprite('ha020_04', 3)	# 7-9
    sprite('ha020_05', 3)	# 10-12
    label(0)
    sprite('ha020_06', 4)	# 13-16
    sprite('ha020_07', 4)	# 17-20
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

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 27)	# 603-629
    sprite('ha404_04', 1)	# 630-630
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    Unknown1007(30000)
    physicsXImpulse(375000)
    physicsYImpulse(-250000)
    sprite('ha404_05', 1)	# 631-631
    sprite('ha404_06', 1)	# 632-632
    sprite('ha404_07', 1)	# 633-633
    sprite('ha404_08', 2)	# 634-635
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown2053(1)
    EnableCollision(1)
    sendToLabelUpon(2, 9)
    sprite('ha404_09', 3)	# 636-638	 **attackbox here**
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 639-640
    sprite('ha404_11', 2)	# 641-642
    sprite('ha404_12', 2)	# 643-644
    sprite('ha404_13', 3)	# 645-647
    Unknown1043()
    sprite('ha404_14', 3)	# 648-650
    sprite('ha404_15', 3)	# 651-653
    sprite('ha404_16', 3)	# 654-656
    sprite('ha020_03', 3)	# 657-659
    sprite('ha020_04', 3)	# 660-662
    sprite('ha020_05', 3)	# 663-665
    label(1)
    sprite('ha020_06', 3)	# 666-668
    sprite('ha020_07', 3)	# 669-671
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ha024_00', 2)	# 672-673
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ha024_01', 2)	# 674-675
    sprite('ha024_02', 2)	# 676-677
    sprite('ha024_03', 2)	# 678-679
    sprite('ha024_04', 1)	# 680-680

@State
def CmnActChangePartnerQuickIn():
    sprite('ha403_04', 4)	# 1-4
    sprite('ha403_03', 4)	# 5-8
    sprite('ha403_02', 7)	# 9-15
    sprite('ha403_01', 7)	# 16-22
    sprite('ha403_00', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ha033_02', 3)	# 1-3
    sprite('ha033_02ex01', 3)	# 4-6
    sprite('ha033_02ex02', 3)	# 7-9
    sprite('ha033_02', 3)	# 10-12
    sprite('ha033_02ex01', 3)	# 13-15
    sprite('ha033_02ex02', 3)	# 16-18
    sprite('ha033_02', 3)	# 19-21
    sprite('ha033_02ex01', 3)	# 22-24
    sprite('ha033_02ex02', 3)	# 25-27
    sprite('ha033_02', 3)	# 28-30
    sprite('ha033_02', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('ha033_00', 2)	# 1-2
    sprite('ha033_01', 2)	# 3-4
    loopRest()
    label(0)
    sprite('ha033_02', 3)	# 5-7
    sprite('ha033_02ex01', 3)	# 8-10
    sprite('ha033_02ex02', 3)	# 11-13
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha033_03', 3)	# 14-16
    physicsXImpulse(0)
    sprite('ha033_04', 3)	# 17-19

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ha300_00', 5)	# 1-5
    sprite('ha300_01', 5)	# 6-10
    sprite('ha300_02', 6)	# 11-16
    sprite('ha300_03', 6)	# 17-22
    sprite('ha300_04', 6)	# 23-28
    sprite('ha300_05', 6)	# 29-34
    sprite('ha300_06', 6)	# 35-40
    sprite('ha300_07', 6)	# 41-46
    sprite('ha300_08', 6)	# 47-52
    sprite('ha300_09', 6)	# 53-58
    sprite('ha300_10', 6)	# 59-64
    sprite('ha300_11', 6)	# 65-70
    sprite('ha300_12', 30)	# 71-100

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
    sprite('ha020_06', 4)	# 3-6
    Unknown1019(95)
    sprite('ha020_07', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ha010_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(3900)
        AttackP1(70)
        AttackP2(80)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(50)
        AirPushbackX(45900)
        AirPushbackY(36000)
        Hitstop(25)
        Unknown9310(1)
        Unknown11056(0)
        Unknown9015(1)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()
        Unknown2004(1, 0)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ha430_00', 3)	# 1-3
    sprite('ha430_01', 3)	# 4-6
    sprite('ha430_02', 3)	# 7-9
    sprite('ha430_03', 3)	# 10-12
    sprite('ha430_04', 3)	# 13-15
    sprite('ha430_05', 3)	# 16-18
    sprite('ha430_06', 3)	# 19-21
    sprite('ha430_07', 3)	# 22-24
    sprite('ha430_08', 3)	# 25-27
    sprite('ha430_09', 3)	# 28-30
    sprite('ha430_10', 3)	# 31-33
    sprite('ha430_11', 4)	# 34-37
    sprite('ha430_12', 4)	# 38-41
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 4)	# 42-45
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 46-49
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_13', 4)	# 50-53
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_14', 4)	# 54-57
    sprite('ha430_13', 4)	# 58-61
    sprite('ha430_14', 4)	# 62-65
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 4)	# 66-69
    sprite('ha430_14', 4)	# 70-73
    sprite('ha430_13', 4)	# 74-77
    sprite('ha430_15', 4)	# 78-81
    GFX_1('haef_DD_1_ring', 0)
    physicsXImpulse(5000)
    sprite('ha430_16', 2)	# 82-83
    SFX_0('006_swing_blade_2')
    sprite('ha430_16', 2)	# 84-85
    sprite('ha430_17', 4)	# 86-89
    Unknown7009(5)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('011_spin_0')
    sprite('ha430_18', 4)	# 90-93	 **attackbox here**
    GFX_0('ha430_col_dmy', 100)
    SFX_3('hase_20')
    ScreenShake(0, 16000)
    GFX_1('haef_DD_1_blast', 0)
    Unknown2015(200)
    physicsXImpulse(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21007(9, 32)
        clearUponHandler(10)
    GFX_0('ha_TAG_1_shot', 0)
    Unknown38(9, 1)
    sprite('ha430_19', 5)	# 94-98
    sprite('ha430_20', 5)	# 99-103
    sprite('ha430_21', 5)	# 104-108
    sprite('ha430_22', 5)	# 109-113
    sprite('ha430_23', 5)	# 114-118
    Unknown2015(-1)
    sprite('ha430_24', 4)	# 119-122
    sprite('ha430_25', 4)	# 123-126
    sprite('ha430_26', 4)	# 127-130
    sprite('ha430_27', 4)	# 131-134

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Hitstop(16)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ha403_00', 2)	# 1-2
    sprite('ha403_01', 2)	# 3-4
    physicsXImpulse(40000)
    Unknown3029(1)
    Unknown3069(0)
    Unknown8007(-1, 1, 1)
    sprite('ha403_02', 2)	# 5-6
    Unknown1019(90)
    SFX_0('004_swing_grap_1_2')
    SFX_0('000_airdash_2')
    sprite('ha403_03', 2)	# 7-8
    Unknown3029(1)
    Unknown3069(0)
    physicsXImpulse(15000)
    Unknown1019(90)
    sprite('ha403_05', 3)	# 9-11
    Unknown1019(80)
    sprite('ha403_06', 1)	# 12-12	 **attackbox here**
    Unknown1019(60)
    SFX_0('005_swing_grap_2_2')
    Unknown7007('6268613230345f300000000000000000640000006268613230345f310000000000000000640000006268613230345f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ha_FastEnma', 0)
    sprite('ha403_06', 1)	# 13-13	 **attackbox here**
    Unknown1019(60)
    sprite('ha403_06', 1)	# 14-14	 **attackbox here**
    Unknown1019(60)
    sprite('ha403_07', 4)	# 15-18	 **attackbox here**
    physicsXImpulse(0)
    sprite('ha403_08', 2)	# 19-20
    Recovery()
    sprite('ha403_09', 2)	# 21-22
    sprite('ha403_10', 2)	# 23-24
    sprite('ha403_11', 2)	# 25-26
    sprite('ha403_12', 2)	# 27-28
    sprite('ha403_13', 2)	# 29-30
    sprite('ha403_14', 2)	# 31-32
    sprite('ha403_15', 2)	# 33-34
    sprite('ha403_16', 2)	# 35-36
    sprite('ha403_17', 2)	# 37-38
    sprite('ha403_18', 2)	# 39-40
    sprite('ha403_19', 2)	# 41-42
    Unknown3029(0)
    sprite('ha403_20', 2)	# 43-44
    sprite('ha403_21', 2)	# 45-46
    SFX_3('hase_22')

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirUntechableTime(60)
        AirPushbackX(72000)
        AirPushbackY(4000)
        YImpluseBeforeWallbounce(0)
        WallbounceReboundTime(24)
        PushbackX(12000)
        Unknown11056(0)
        Unknown9015(1)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ha400_00', 3)	# 1-3
    sprite('ha400_01', 3)	# 4-6
    Unknown7007('6268613230305f300000000000000000640000006268613230305f310000000000000000640000006268613230305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_02', 2)	# 7-8
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_03', 4)	# 9-12
    physicsXImpulse(55000)
    Unknown2015(150)
    sprite('ha400_04', 8)	# 13-20

    def upon_CLEAR_OR_EXIT():
        if (SLOT_19 < 300000):
            sendToLabel(0)
    label(0)
    sprite('ha400_05', 3)	# 21-23	 **attackbox here**
    clearUponHandler(3)
    physicsXImpulse(0)
    setGravity(0)
    sprite('ha400_06', 4)	# 24-27
    SFX_0('208_brake_normal')
    Recovery()
    Unknown2015(-1)
    sprite('ha400_07', 4)	# 28-31
    sprite('ha400_08', 4)	# 32-35
    sprite('ha400_09', 4)	# 36-39
    sprite('ha400_10', 4)	# 40-43
    SFX_3('hase_22')

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
        SLOT_4 = 1
    sprite('null', 1)	# 1-1
    Unknown2036(84, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-580000)
    Unknown1019(4)
    label(0)
    sprite('ha020_06', 4)	# 3-6
    sprite('ha020_07', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('ChangePartnerDDOD_Exe')
    else:
        enterState('ChangePartnerDD_Exe')

@State
def ChangePartnerDD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5000)
        AirPushbackY(45000)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(10, 30, 30)
        Unknown11084(1)
        Unknown11066(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        setInvincible(1)
        Unknown23072()

        def upon_78():
            sendToLabel(0)
    sprite('ha431_00', 4)	# 1-4
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 4)	# 5-8
    sprite('ha431_02', 4)	# 9-12
    sprite('ha431_03', 4)	# 13-16
    sprite('ha431_04', 4)	# 17-20
    sprite('ha431_05', 4)	# 21-24
    sprite('ha431_06', 4)	# 25-28
    sprite('ha431_07', 4)	# 29-32
    sprite('ha431_08', 3)	# 33-35
    sprite('ha431_09', 3)	# 36-38
    sprite('ha431_10', 3)	# 39-41
    sprite('ha431_11', 3)	# 42-44
    sprite('ha431_12', 3)	# 45-47
    sprite('ha431_13', 3)	# 48-50
    sprite('ha431_14', 3)	# 51-53
    sprite('ha431_15', 3)	# 54-56
    sprite('ha431_16', 3)	# 57-59	 **attackbox here**
    StartMultihit()
    SFX_4('bha157_0')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(1696000)
    sprite('ha431_16', 12)	# 60-71	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ha431_16', 40)	# 72-111	 **attackbox here**
    StartMultihit()
    clearUponHandler(78)
    loopRest()
    label(9)
    sprite('ha431_17', 4)	# 112-115
    setInvincible(0)
    sprite('ha431_18', 4)	# 116-119
    sprite('ha431_19', 4)	# 120-123
    sprite('ha431_20', 4)	# 124-127
    sprite('ha431_21', 4)	# 128-131
    sprite('ha431_22', 4)	# 132-135
    sprite('ha431_23', 4)	# 136-139
    sprite('ha431_24', 4)	# 140-143
    sprite('ha431_25', 4)	# 144-147
    sprite('ha431_26', 4)	# 148-151
    sprite('ha431_27', 4)	# 152-155
    sprite('ha431_28', 4)	# 156-159
    sprite('ha431_29', 3)	# 160-162
    sprite('ha000_00', 1)	# 163-163
    Unknown2005()

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown23056('')
        AttackLevel_(4)
        Damage(200)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5000)
        AirPushbackY(45000)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(10, 70, 75)
        Unknown11084(1)
        Unknown11066(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11057(0)
        Unknown9016(1)
        Unknown11064(1)
        setInvincible(1)
        Unknown23072()
        Unknown11069('ChangePartnerDDOD_Exe')

        def upon_78():
            sendToLabel(0)
    sprite('ha431_00', 4)	# 1-4
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 4)	# 5-8
    sprite('ha431_02', 4)	# 9-12
    sprite('ha431_03', 4)	# 13-16
    sprite('ha431_04', 4)	# 17-20
    sprite('ha431_05', 4)	# 21-24
    sprite('ha431_06', 4)	# 25-28
    sprite('ha431_07', 4)	# 29-32
    sprite('ha431_08', 3)	# 33-35
    sprite('ha431_09', 3)	# 36-38
    sprite('ha431_10', 3)	# 39-41
    sprite('ha431_11', 3)	# 42-44
    sprite('ha431_12', 3)	# 45-47
    sprite('ha431_13', 3)	# 48-50
    sprite('ha431_14', 3)	# 51-53
    sprite('ha431_15', 3)	# 54-56
    sprite('ha431_16', 3)	# 57-59	 **attackbox here**
    StartMultihit()
    SFX_4('bha157_0')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(1696000)
    sprite('ha431_16', 12)	# 60-71	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ha431_16', 60)	# 72-131	 **attackbox here**
    StartMultihit()
    clearUponHandler(78)
    AttackLevel_(1)
    Damage(100)
    Hitstop(1)
    Unknown11057(700)
    Unknown11023(1)
    SLOT_52 = 4
    label(1)
    sprite('ha431_16', 1)	# 132-132	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    Unknown4045('686165665f44445f32000000000000000000000000000000000000000000000000000000')
    Unknown4053(-40000, 40000)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    ScreenShake(0, 16000)
    sprite('ha431_16', 1)	# 133-133	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    sprite('ha431_16', 1)	# 134-134	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    sprite('ha431_16', 1)	# 135-135	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    SLOT_52 = (SLOT_52 + (-1))
    Unknown19(2, 2, 52)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ha431_16', 1)	# 136-136	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    sprite('ha431_16', 1)	# 137-137	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(40)
    sprite('ha431_16', 11)	# 138-148	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AttackLevel_(5)
    Damage(500)
    Hitstop(30)
    Unknown11001(0, 0, 0)
    Unknown11057(1000)
    Unknown11064(0)
    Unknown11069('')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 32000)

    def upon_77():
        Unknown13024(1)
        Unknown14077(1)
        clearUponHandler(77)
    loopRest()
    label(9)
    sprite('ha431_17', 4)	# 149-152
    setInvincible(0)
    sprite('ha431_18', 4)	# 153-156
    sprite('ha431_19', 4)	# 157-160
    sprite('ha431_20', 4)	# 161-164
    sprite('ha431_21', 4)	# 165-168
    sprite('ha431_22', 4)	# 169-172
    sprite('ha431_23', 4)	# 173-176
    sprite('ha431_24', 4)	# 177-180
    sprite('ha431_25', 4)	# 181-184
    sprite('ha431_26', 4)	# 185-188
    sprite('ha431_27', 4)	# 189-192
    sprite('ha431_28', 4)	# 193-196
    sprite('ha431_29', 3)	# 197-199
    sprite('ha000_00', 1)	# 200-200
    Unknown2005()

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('ha300_00', 5)	# 1-5
    Unknown1084(1)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('ha300_01', 5)	# 6-10
    sprite('ha300_02', 6)	# 11-16
    sprite('ha300_03', 6)	# 17-22
    sprite('ha300_04', 6)	# 23-28
    sprite('ha300_05', 6)	# 29-34
    sprite('ha300_06', 6)	# 35-40
    sprite('ha300_07', 6)	# 41-46
    sprite('ha300_08', 6)	# 47-52
    sprite('ha300_09', 6)	# 53-58
    sprite('ha300_10', 6)	# 59-64
    label(1)
    sprite('keep', 1)	# 65-65
    Unknown30042(24)
    if SLOT_ReturnVal:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ha300_11', 6)	# 66-71
    sprite('ha300_12', 6)	# 72-77

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('ha404_00', 3)	# 121-123
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    Unknown1007(1000000)
    physicsXImpulse(55555)
    physicsYImpulse(-37037)
    sprite('ha404_01', 3)	# 124-126
    sprite('ha404_02', 3)	# 127-129
    sprite('ha404_03', 3)	# 130-132
    sprite('ha404_04', 3)	# 133-135
    sprite('ha404_05', 3)	# 136-138
    sprite('ha404_06', 3)	# 139-141
    sprite('ha404_07', 3)	# 142-144
    sprite('ha404_08', 3)	# 145-147
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown2053(1)
    EnableCollision(1)
    sprite('ha404_09', 3)	# 148-150	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(10000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 151-152
    sprite('ha404_11', 2)	# 153-154
    sprite('ha404_12', 2)	# 155-156
    sprite('ha404_13', 3)	# 157-159
    Unknown1043()
    sprite('ha404_14', 3)	# 160-162
    sprite('ha404_15', 3)	# 163-165
    sprite('ha404_16', 3)	# 166-168
    sprite('ha020_03', 3)	# 169-171
    sprite('ha020_04', 3)	# 172-174
    sprite('ha020_05', 3)	# 175-177
    label(1)
    sprite('ha020_06', 3)	# 178-180
    sprite('ha020_07', 3)	# 181-183
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('ha024_00', 3)	# 184-186
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ha024_01', 3)	# 187-189
    sprite('ha024_02', 9)	# 190-198
    sprite('ha024_03', 3)	# 199-201
    sprite('ha024_04', 3)	# 202-204

@State
def CmnActChangeReturnAppealBurst():
    sprite('ha111_08', 6)	# 1-6
    sprite('ha111_09', 6)	# 7-12
    sprite('ha111_10', 6)	# 13-18
    sprite('ha111_11', 18)	# 19-36
    sprite('ha111_12', 6)	# 37-42
    sprite('ha010_02', 6)	# 43-48
    sprite('ha010_01', 6)	# 49-54
    sprite('ha010_00', 6)	# 55-60
    sprite('ha000_00', 30)	# 61-90

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
    sprite('ha440_03', 2)	# 32-33
    sprite('ha440_04', 3)	# 34-36
    sprite('ha440_05', 30)	# 37-66	 **attackbox here**
    label(1)
    sprite('ha440_05', 1)	# 67-67	 **attackbox here**
    sprite('ha407_05', 5)	# 68-72
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ha024_01', 4)	# 73-76
    sprite('ha024_02', 12)	# 77-88
    sprite('ha024_03', 5)	# 89-93
    sprite('ha024_04', 4)	# 94-97

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('ha024_01', 3)	# 2-4
    sprite('ha024_02', 3)	# 5-7
    sprite('ha024_03', 4)	# 8-11
    sprite('ha024_04', 4)	# 12-15
    sprite('ha212_00', 2)	# 16-17
    sprite('ha212_01', 2)	# 18-19
    sprite('ha212_02', 3)	# 20-22
    sprite('ha212_03', 3)	# 23-25
    sprite('ha212_04', 3)	# 26-28
    sprite('ha212_05', 2)	# 29-30
    SFX_0('005_swing_grap_2_2')
    sprite('ha212_06', 2)	# 31-32
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha212_07', 2)	# 33-34
    Unknown7009(2)
    sprite('ha212_08', 3)	# 35-37	 **attackbox here**
    RefreshMultihit()
    GFX_0('ha_212', -1)
    sprite('ha212_09', 4)	# 38-41
    sprite('ha212_10', 4)	# 42-45
    sprite('ha212_11', 4)	# 46-49
    sprite('ha212_12', 4)	# 50-53
    sprite('ha212_13', 4)	# 54-57
    sprite('ha212_14', 3)	# 58-60
    sprite('ha212_15', 3)	# 61-63
    sprite('ha212_16', 3)	# 64-66
    sprite('ha212_17', 3)	# 67-69
    sprite('ha212_18', 3)	# 70-72
    sprite('ha212_19', 2)	# 73-74
    sprite('ha212_19', 1)	# 75-75
    SFX_3('hase_22')

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ha201_00', 2)	# 1-2
    sprite('ha201_01', 3)	# 3-5
    sprite('ha201_02', 4)	# 6-9
    SFX_0('004_swing_grap_1_1')
    Unknown7009(3)
    sprite('ha201_03', 2)	# 10-11	 **attackbox here**
    sprite('ha201_04', 2)	# 12-13
    Recovery()
    Unknown2063()
    sprite('ha201_05', 2)	# 14-15
    sprite('ha201_06', 2)	# 16-17
    sprite('ha201_07', 2)	# 18-19
    sprite('ha201_08', 2)	# 20-21
    sprite('ha201_09', 2)	# 22-23
    sprite('ha201_10', 3)	# 24-26

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2000)
        Unknown9310(1)
        Unknown9016(1)
        AirPushbackX(18000)
        AirPushbackY(-56000)
        YImpluseBeforeWallbounce(0)
        PushbackX(19800)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown2004(1, 0)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha202_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha202_00', 1)	# 1-1
    sprite('ha202_01', 1)	# 2-2
    sprite('ha202_02', 4)	# 3-6
    sprite('ha202_03', 1)	# 7-7
    sprite('ha202_04', 1)	# 8-8
    sprite('ha202_05', 4)	# 9-12
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown7009(2)
    sprite('ha202_06', 1)	# 13-13
    GFX_0('ha202_col_dmy', 0)
    sprite('ha202_07', 2)	# 14-15	 **attackbox here**
    GFX_0('ha_202', -1)
    sprite('ha202_08', 1)	# 16-16
    Recovery()
    Unknown2063()
    sprite('ha202_09', 2)	# 17-18
    sprite('ha202_10', 3)	# 19-21
    sprite('ha202_11', 3)	# 22-24
    sprite('ha202_12', 3)	# 25-27
    sprite('ha202_13', 2)	# 28-29
    sprite('ha202_14', 2)	# 30-31
    sprite('ha202_15', 2)	# 32-33
    sprite('ha202_16', 2)	# 34-35

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(20000)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ha210_00', 3)	# 1-3
    sprite('ha210_01', 5)	# 4-8
    Unknown7009(4)
    sprite('ha210_02', 3)	# 9-11
    SFX_0('004_swing_grap_1_2')
    sprite('ha210_03', 3)	# 12-14
    physicsXImpulse(26000)
    Unknown1045(40000)
    Unknown8000(100, 1, 1)
    sprite('ha210_04', 5)	# 15-19	 **attackbox here**
    Unknown1019(150)
    Unknown8010(0, 1, 1)
    sprite('ha210_05', 3)	# 20-22
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ha210_06', 3)	# 23-25
    Unknown1019(50)
    sprite('ha210_07', 3)	# 26-28
    Unknown1019(50)
    sprite('ha210_08', 4)	# 29-32
    Unknown1084(1)
    sprite('ha210_09', 4)	# 33-36
    sprite('ha210_10', 3)	# 37-39
    sprite('ha210_10', 1)	# 40-40
    SFX_3('hase_22')

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        AirPushbackX(-1000)
        AirUntechableTime(24)
        HitOrBlockCancel('NmlAtk5A4th')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
    sprite('ha408_00', 1)	# 1-1
    sprite('ha408_01', 2)	# 2-3
    sprite('ha408_02', 2)	# 4-5
    Unknown7009(1)
    sprite('ha408_05', 2)	# 6-7
    sprite('ha408_06', 2)	# 8-9
    sprite('ha408_07', 2)	# 10-11
    sprite('ha408_08', 2)	# 12-13
    sprite('ha408_09', 1)	# 14-14
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha408_10', 3)	# 15-17	 **attackbox here**
    GFX_0('GuardCrash', -1)
    Unknown1084(1)
    sprite('ha408_11', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('ha408_12', 3)	# 21-23
    sprite('ha408_13', 3)	# 24-26
    sprite('ha408_14', 3)	# 27-29
    sprite('ha408_15', 3)	# 30-32
    sprite('ha408_16', 3)	# 33-35
    sprite('ha408_17', 3)	# 36-38
    sprite('ha408_18', 3)	# 39-41

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(2200)
        AttackP2(90)
        AirUntechableTime(36)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(16000)
        AirPushbackY(22000)
        PushbackX(30400)
        Unknown9016(1)
        JumpCancel_(0)
        Unknown11044(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha212_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha212_00', 2)	# 1-2
    sprite('ha212_01', 2)	# 3-4
    sprite('ha212_02', 2)	# 5-6
    sprite('ha212_03', 2)	# 7-8
    sprite('ha212_04', 2)	# 9-10
    sprite('ha212_05', 2)	# 11-12
    SFX_0('005_swing_grap_2_2')
    Unknown7007('6268613130385f300000000000000000640000006268613130385f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ha212_06', 2)	# 13-14
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha212_07', 2)	# 15-16
    GFX_0('ha212_col_dmy', 0)
    sprite('ha212_08', 3)	# 17-19	 **attackbox here**
    GFX_0('ha_212', -1)
    Unknown30088(1)
    sprite('ha212_09', 4)	# 20-23
    Recovery()
    Unknown2063()
    sprite('ha212_10', 3)	# 24-26
    sprite('ha212_11', 3)	# 27-29
    sprite('ha212_12', 3)	# 30-32
    sprite('ha212_13', 2)	# 33-34
    sprite('ha212_14', 2)	# 35-36
    sprite('ha212_15', 2)	# 37-38
    sprite('ha212_16', 2)	# 39-40
    sprite('ha212_17', 2)	# 41-42
    sprite('ha212_18', 2)	# 43-44
    sprite('ha212_19', 2)	# 45-46
    SFX_3('hase_22')

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackX(16000)
        AirPushbackY(12000)
        AirUntechableTime(36)
        PushbackX(19800)
        Unknown9016(1)
        Unknown11001(0, 0, 9)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha214_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
        SLOT_60 = 0

        def upon_77():
            clearUponHandler(77)
            SLOT_60 = 1
    sprite('ha214_00', 3)	# 1-3
    sprite('ha214_01', 3)	# 4-6
    sprite('ha214_02', 3)	# 7-9
    sprite('ha214_03', 3)	# 10-12
    Unknown7009(4)
    sprite('ha214_04', 1)	# 13-13
    GFX_0('ha214_col_dmy', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha214_05', 1)	# 14-14
    GFX_0('ha_214', -1)
    sprite('ha214_06', 3)	# 15-17	 **attackbox here**
    sprite('ha214_07', 5)	# 18-22
    Recovery()
    Unknown2063()
    sprite('ha214_08', 5)	# 23-27
    sprite('ha214_09', 4)	# 28-31
    sprite('ha214_10', 4)	# 32-35
    sprite('ha214_11', 4)	# 36-39
    SFX_3('hase_22')

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        if SLOT_60:
            Unknown2016(350)
    sprite('ha403_00', 2)	# 1-2
    sprite('ha403_01', 1)	# 3-3
    sprite('ha403_01', 1)	# 4-4
    Unknown7007('6268613230335f300000000000000000640000006268613230335f310000000000000000640000006268613230335f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(30000)
    Unknown3029(1)
    Unknown3069(0)
    Unknown8007(-1, 1, 1)
    sprite('ha403_02', 2)	# 5-6
    Unknown1019(120)
    SFX_0('004_swing_grap_1_2')
    SFX_0('000_airdash_2')
    sprite('ha403_02', 2)	# 7-8
    Unknown14070('NmlAtk5B3rd')
    sprite('ha403_03', 2)	# 9-10
    Unknown1019(130)
    sprite('ha403_04', 2)	# 11-12
    sprite('ha403_04', 2)	# 13-14
    Unknown14072('NmlAtk5B3rd')
    sprite('ha403_03', 2)	# 15-16
    Unknown1019(130)
    sprite('ha403_04', 2)	# 17-18
    sprite('ha403_02', 2)	# 19-20
    Unknown1019(80)
    Unknown14074('NmlAtk5B3rd')
    if SLOT_60:
        Unknown2016(-1)
    sprite('ha403_01', 2)	# 21-22
    Unknown3029(0)
    Unknown1019(80)
    sprite('ha403_00', 2)	# 23-24
    physicsXImpulse(0)

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(75)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(40)
        Hitstop(16)
        if SLOT_60:
            Unknown2016(350)
        Unknown2015(200)
    sprite('ha403_04', 2)	# 1-2
    Unknown3029(1)
    Unknown3069(0)
    physicsXImpulse(45000)
    sprite('ha403_05', 3)	# 3-5
    sprite('ha403_06', 3)	# 6-8	 **attackbox here**
    Unknown1019(30)
    SFX_0('005_swing_grap_2_2')
    Unknown7007('6268613230345f300000000000000000640000006268613230345f310000000000000000640000006268613230345f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ha_FastEnma', 0)
    sprite('ha403_07', 4)	# 9-12	 **attackbox here**
    physicsXImpulse(0)
    sprite('ha403_08', 2)	# 13-14
    Recovery()
    if SLOT_60:
        Unknown2016(-1)
    Unknown2015(-1)
    sprite('ha403_09', 2)	# 15-16
    sprite('ha403_10', 2)	# 17-18
    sprite('ha403_11', 2)	# 19-20
    sprite('ha403_12', 2)	# 21-22
    sprite('ha403_13', 2)	# 23-24
    sprite('ha403_19', 3)	# 25-27
    Unknown3029(0)
    sprite('ha403_20', 3)	# 28-30
    sprite('ha403_21', 2)	# 31-32
    sprite('ha403_21', 1)	# 33-33
    SFX_3('hase_22')

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ha231_00', 2)	# 1-2
    sprite('ha231_01', 1)	# 3-3
    sprite('ha231_01', 1)	# 4-4
    Unknown7009(0)
    SFX_0('004_swing_grap_1_1')
    sprite('ha231_02', 2)	# 5-6
    sprite('ha231_03', 1)	# 7-7
    sprite('ha231_04', 6)	# 8-13	 **attackbox here**
    sprite('ha231_05', 2)	# 14-15
    Recovery()
    Unknown2063()
    sprite('ha231_06', 2)	# 16-17
    sprite('ha231_07', 3)	# 18-20
    sprite('ha231_08', 4)	# 21-24
    sprite('ha231_09', 4)	# 25-28

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(23)
        AirPushbackY(30000)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)

        def upon_32():
            Unknown22019('0100000000000000000000000100000000000000')
            if SLOT_2:
                setInvincible(1)
                Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha232_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                Unknown22019('0100000000000000000000000000000000000000')
                if SLOT_2:
                    setInvincible(0)
                    Unknown22019('0000000000000000000000000000000000000000')
    sprite('ha232_00', 2)	# 1-2
    sprite('ha232_01', 2)	# 3-4
    sprite('ha232_02', 2)	# 5-6
    Unknown7007('6268613130365f300000000000000000640000006268613130365f310000000000000000640000006268613130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha232_03', 2)	# 7-8
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha232_04', 1)	# 9-9
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ha232_05', 3)	# 10-12
    GFX_0('ha232_col_dmy', 0)
    sprite('ha232_08', 3)	# 13-15	 **attackbox here**
    GFX_0('ha_232', -1)
    sprite('ha232_09', 3)	# 16-18
    Unknown2037(1)
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ha232_10', 3)	# 19-21
    sprite('ha232_11', 3)	# 22-24
    sprite('ha232_12', 4)	# 25-28
    sprite('ha232_13', 4)	# 29-32
    sprite('ha232_14', 4)	# 33-36
    sprite('ha232_15', 4)	# 37-40
    sprite('ha232_16', 4)	# 41-44
    sprite('ha232_17', 4)	# 45-48
    SFX_3('hase_22')

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        Unknown9016(1)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(1)
        Unknown11065(1)
        Unknown11001(0, 0, 8)
        AirPushbackX(-1000)
        AirPushbackY(15000)
        AirUntechableTime(36)
        Unknown2004(1, 0)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha234_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha234_00', 2)	# 1-2
    sprite('ha234_01', 2)	# 3-4
    sprite('ha234_02', 1)	# 5-5
    sprite('ha234_03', 1)	# 6-6
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown7007('6268613130375f300000000000000000640000006268613130375f310000000000000000640000006268613130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha234_04', 1)	# 7-7
    sprite('ha234_05', 1)	# 8-8
    GFX_0('ha234_col_dmy', 0)
    sprite('ha234_06', 3)	# 9-11	 **attackbox here**
    GFX_0('ha_234', -1)
    sprite('ha234_07', 4)	# 12-15
    Recovery()
    sprite('ha234_08', 3)	# 16-18
    sprite('ha234_09', 6)	# 19-24
    sprite('ha234_10', 4)	# 25-28
    sprite('ha234_11', 4)	# 29-32
    sprite('ha234_12', 4)	# 33-36
    sprite('ha234_13', 4)	# 37-40
    sprite('ha234_14', 4)	# 41-44
    SFX_3('hase_22')

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1500)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha252_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha252_00', 1)	# 1-1
    sprite('ha252_01', 2)	# 2-3
    sprite('ha252_02', 2)	# 4-5
    sprite('ha252_03', 2)	# 6-7
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown7009(5)
    sprite('ha252_04', 2)	# 8-9
    sprite('ha252_05', 2)	# 10-11
    GFX_0('ha252_col_dmy', 0)
    GFX_0('ha_252', -1)
    sprite('ha252_06', 3)	# 12-14	 **attackbox here**
    sprite('ha252_07', 1)	# 15-15	 **attackbox here**
    sprite('ha252_08', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('ha252_09', 3)	# 19-21
    sprite('ha252_10', 4)	# 22-25
    sprite('ha252_11', 4)	# 26-29
    sprite('ha252_12', 4)	# 30-33
    sprite('ha020_04', 3)	# 34-36
    sprite('ha020_05', 3)	# 37-39
    sprite('ha020_06', 3)	# 40-42
    sprite('ha020_07', 3)	# 43-45

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirHitstunAnimation(10)
        AirPushbackY(20000)
        AirUntechableTime(21)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            setGravity(500)
            sendToLabel(0)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha260_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha260_00', 1)	# 1-1
    sprite('ha260_01', 1)	# 2-2
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown3029(1)
    sprite('ha260_02', 1)	# 3-3
    Unknown7009(2)
    sprite('ha260_03', 1)	# 4-4
    sprite('ha260_04', 6)	# 5-10
    GFX_0('ha260_col_dmy', 0)
    sprite('ha260_05', 4)	# 11-14	 **attackbox here**
    GFX_0('ha_260', -1)
    sprite('ha260_06', 4)	# 15-18	 **attackbox here**
    sprite('ha260_07', 4)	# 19-22	 **attackbox here**
    label(0)
    sprite('ha260_08', 4)	# 23-26
    Unknown3029(0)
    Recovery()
    sprite('ha260_09', 4)	# 27-30
    Unknown1043()
    sprite('ha260_10', 4)	# 31-34

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1800)
        AirPushbackX(35000)
        AirHitstunAnimation(13)
        AirUntechableTime(30)
        Unknown9178(1)
        Unknown9346(1)
        Unknown9362(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha406_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
        HitJumpCancel(1)
    sprite('ha406_00', 2)	# 1-2
    sprite('ha406_01', 7)	# 3-9
    sprite('ha406_02', 2)	# 10-11
    GFX_0('ha406_col_dmy', 0)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown7009(5)
    sprite('ha406_03', 2)	# 12-13	 **attackbox here**
    GFX_0('ha_406', -1)
    Unknown36(1)
    teleportRelativeX(90000)
    Unknown35()
    Unknown22004(4, 1)
    sprite('ha406_04', 6)	# 14-19	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ha406_05', 6)	# 20-25
    sprite('ha406_06', 5)	# 26-30
    sprite('ha406_07', 5)	# 31-35
    sprite('ha406_08', 5)	# 36-40
    sprite('ha406_09', 5)	# 41-45
    SFX_3('hase_22')

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(25)
        AirPushbackY(30000)
        HitOverhead(0)
        HitOrBlockJumpCancel(1)
    sprite('ha405_00', 2)	# 1-2
    physicsXImpulse(5000)
    physicsYImpulse(1000)
    setGravity(150)
    sprite('ha405_01', 2)	# 3-4
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha405_02', 2)	# 5-6
    sprite('ha405_03', 2)	# 7-8
    Unknown7007('6268613230365f300000000000000000640000006268613230365f310000000000000000640000006268613230365f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(5000)
    physicsYImpulse(15000)
    sprite('ha405_04', 2)	# 9-10
    SFX_0('004_swing_grap_1_2')
    SFX_0('004_swing_grap_1_2')
    sprite('ha405_05ex01', 3)	# 11-13	 **attackbox here**
    GFX_0('ha_air_kick', -1)
    GFX_0('ha_air_kick_b', -1)
    GFX_1('haef_kick_drop', 0)
    sprite('ha405_06', 4)	# 14-17
    Unknown1019(60)
    YAccel(60)
    Unknown1043()
    Recovery()
    Unknown2063()
    sprite('ha405_07', 4)	# 18-21
    Unknown1019(60)
    physicsYImpulse(0)
    sprite('ha405_08', 4)	# 22-25
    Unknown1019(60)
    sprite('ha405_09', 4)	# 26-29
    physicsXImpulse(0)
    sprite('ha405_10', 4)	# 30-33
    sprite('ha405_11', 4)	# 34-37
    Unknown3029(0)

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
        Unknown1051(30)

        def upon_42():
            Unknown23022(1)
            ScreenShake(8000, 2000)
            GFX_0('ha_D_usui', 0)
            Unknown21012('68615f354400000000000000000000000000000000000000000000000000000021000000')
            enterState('Atk5DGrip')
        GuardPoint_(1)
        Unknown22031(-1, 17)
    sprite('ha203_00', 2)	# 1-2
    GFX_0('ha_5D', 0)
    GFX_0('ha_D_usui', 0)
    SFX_3('hase_23')
    sprite('ha203_01', 3)	# 3-5
    sprite('ha203_02', 5)	# 6-10
    sprite('ha203_17', 7)	# 11-17
    sprite('ha203_18', 7)	# 18-24
    GFX_0('ha_D_usui', 0)
    sprite('ha203_19', 1)	# 25-25
    sprite('ha203_19', 6)	# 26-31
    Unknown21012('68615f354400000000000000000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('ha203_20', 5)	# 32-36
    sprite('ha203_21', 5)	# 37-41
    sprite('ha203_22', 4)	# 42-45
    SFX_3('hase_22')

@State
def Atk5DGrip():

    def upon_IMMEDIATE():
        Unknown17011('Atk5DExe', 2, 0, 0)
        AttackP1(80)
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11045(0)
        Unknown11058('0000000001000000000000000000000001000000')
        HitLow(0)
        HitOverhead(0)
        Hitstop(8)
        PushbackX(32000)
        Unknown30065(100)

        def upon_12():
            Hitstop(0)
        EnableCollision(0)
        Unknown23022(1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('keep', 10)	# 1-10
    sprite('ha203_03', 5)	# 11-15
    sprite('ha203_04', 10)	# 16-25	 **attackbox here**
    sprite('ha203_21', 5)	# 26-30
    EnableCollision(1)
    sprite('ha203_22', 5)	# 31-35

@State
def Atk5DExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(3300)
        MinimumDamagePct(5)
        AttackP2(60)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(-8000)
        AirPushbackY(-320000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(42)
        Hitstop(0)
        Unknown9310(10)
        Unknown11108('03000000')
        Unknown30065(100)
        Unknown23022(1)
        Unknown13024(0)
        Unknown14083(0)
        Unknown13045(0)
        Unknown30068(1)
        Unknown23072()
        Unknown21005(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ha203_05', 3)	# 1-3
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha203_06', 3)	# 4-6
    Unknown5000(11, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha203_07', 3)	# 7-9
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha203_08', 3)	# 10-12
    Unknown5000(13, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha203_09', 1)	# 13-13	 **attackbox here**
    Unknown5000(13, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    StartMultihit()
    sprite('ha203_09', 2)	# 14-15	 **attackbox here**
    Unknown7009(3)
    StartMultihit()
    sprite('ha203_10', 1)	# 16-16	 **attackbox here**
    Unknown5000(13, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    StartMultihit()
    sprite('ha203_10', 4)	# 17-20	 **attackbox here**
    sprite('ha203_11', 5)	# 21-25
    sprite('ha203_12', 5)	# 26-30
    sprite('ha203_13', 5)	# 31-35
    sprite('ha203_14', 5)	# 36-40
    sprite('ha203_15', 5)	# 41-45
    sprite('ha203_16', 6)	# 46-51

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
        Unknown1084(1)
        Unknown1007(1)
        clearUponHandler(2)

        def upon_42():
            Unknown23022(1)
            ScreenShake(8000, 2000)
            GFX_0('ha_D_usui', 0)
            Unknown1084(1)
            EnableCollision(0)
            enterState('AtkAIR5DGrip')
        GuardPoint_(1)
        Unknown22031(-1, 15)
    sprite('ha253_00', 2)	# 1-2
    GFX_0('ha_5D', 0)
    GFX_0('ha_D_usui', 0)
    SFX_3('hase_23')
    sprite('ha253_01', 3)	# 3-5
    sprite('ha253_12', 5)	# 6-10
    sprite('ha253_13', 5)	# 11-15
    sprite('ha253_14', 5)	# 16-20
    Unknown21012('68615f354400000000000000000000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('ha253_15', 4)	# 21-24
    sprite('ha253_15', 1)	# 25-25
    SFX_3('hase_22')
    Unknown1043()
    sendToLabelUpon(2, 1)
    label(0)
    sprite('ha020_06', 4)	# 26-29
    sprite('ha020_07', 4)	# 30-33
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha024_00', 2)	# 34-35
    Unknown21012('68615f354400000000000000000000000000000000000000000000000000000020000000')
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ha024_01', 2)	# 36-37
    sprite('ha024_02', 8)	# 38-45
    sprite('ha024_03', 4)	# 46-49
    sprite('ha024_04', 4)	# 50-53

@State
def AtkAIR5DGrip():

    def upon_IMMEDIATE():
        Unknown17011('AtkAIR5DExe', 2, 0, 0)
        AttackP1(80)
        Unknown11002(-1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11045(0)
        Unknown11058('0000000001000000000000000000000001000000')
        HitLow(0)
        HitOverhead(0)
        HitAirUnblockable(0)
        Hitstop(8)
        PushbackX(32000)
        Unknown30065(100)

        def upon_77():
            clearUponHandler(77)
            sendToLabel(9)

        def upon_12():
            Hitstop(0)
        EnableCollision(0)
        Unknown23022(1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('keep', 10)	# 1-10
    sprite('ha253_02', 3)	# 11-13
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    setGravity(0)
    sprite('ha253_03', 10)	# 14-23	 **attackbox here**
    sprite('ha253_14', 3)	# 24-26
    EnableCollision(1)
    sprite('ha253_15', 3)	# 27-29
    Unknown1043()
    clearUponHandler(2)
    Unknown28(2, 'CmnActJumpLanding')
    label(0)
    sprite('ha020_06', 4)	# 30-33
    sprite('ha020_07', 4)	# 34-37
    loopRest()
    gotoLabel(0)
    ExitState()
    label(9)
    sprite('ha253_03', 3)	# 38-40	 **attackbox here**
    physicsXImpulse(600)
    physicsYImpulse(1000)
    setGravity(0)
    sprite('ha253_04', 3)	# 41-43
    sprite('ha253_05', 3)	# 44-46
    sprite('ha253_06', 3)	# 47-49
    sprite('ha253_07', 3)	# 50-52	 **attackbox here**
    DisableAttackRestOfMove()
    physicsXImpulse(-4500)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('ha253_08', 4)	# 53-56
    sprite('ha253_09', 4)	# 57-60
    sprite('ha253_10', 4)	# 61-64
    sprite('ha253_11', 4)	# 65-68

@State
def AtkAIR5DExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(3300)
        MinimumDamagePct(5)
        AttackP2(60)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(33000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11108('03000000')
        Unknown11072(1, 150000, 200000)
        Unknown30065(100)
        sendToLabelUpon(2, 1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown30068(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ha253_03', 4)	# 1-4	 **attackbox here**
    physicsXImpulse(600)
    physicsYImpulse(1000)
    setGravity(0)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    sprite('ha253_04', 4)	# 5-8
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha253_05', 4)	# 9-12
    Unknown7007('6268613130365f300000000000000000640000006268613130385f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha253_06', 4)	# 13-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha253_07', 4)	# 17-20	 **attackbox here**
    physicsXImpulse(-4500)
    physicsYImpulse(39000)
    setGravity(2000)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha253_08', 4)	# 21-24
    Unknown2018(1, 80)
    sprite('ha253_09', 4)	# 25-28
    sprite('ha253_10', 4)	# 29-32
    sprite('ha253_11', 4)	# 33-36
    label(0)
    sprite('ha020_06', 4)	# 37-40
    sprite('ha020_07', 4)	# 41-44
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha024_00', 2)	# 45-46
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('ha024_01', 2)	# 47-48
    sprite('ha024_02', 3)	# 49-51
    sprite('ha024_03', 3)	# 52-54
    sprite('ha024_04', 2)	# 55-56

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('ha211_00', 3)	# 1-3
    sprite('ha211_01', 3)	# 4-6
    sprite('ha211_02', 3)	# 7-9
    tag_voice(1, 'bha156_0', 'bha156_1', '', '')
    sprite('ha211_03add3', 6)	# 10-15
    sprite('ha211_03add4', 3)	# 16-18
    sprite('ha211_03', 3)	# 19-21	 **attackbox here**
    StartMultihit()
    sprite('ha211_04', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    SFX_0('004_swing_grap_1_2')
    Unknown8000(0, 1, 1)
    ScreenShake(0, 5000)
    sprite('ha211_05', 3)	# 25-27	 **attackbox here**
    DisableAttackRestOfMove()
    SFX_0('209_down_normal_0')
    sprite('ha211_06', 3)	# 28-30
    sprite('ha211_07', 3)	# 31-33
    sprite('ha211_08', 3)	# 34-36
    sprite('ha211_09', 2)	# 37-38
    sprite('ha211_10', 4)	# 39-42
    sprite('ha211_11', 3)	# 43-45
    sprite('ha211_12', 2)	# 46-47
    sprite('ha211_12', 1)	# 48-48
    SFX_3('hase_22')

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('ha211_05', 2)	# 2-3	 **attackbox here**
    SFX_0('209_down_normal_0')
    sprite('ha211_06', 2)	# 4-5
    sprite('ha211_07', 2)	# 6-7
    sprite('ha211_08', 2)	# 8-9
    sprite('ha211_09', 2)	# 10-11
    sprite('ha211_10', 2)	# 12-13
    sprite('ha211_11', 2)	# 14-15
    sprite('ha211_12', 2)	# 16-17
    SFX_3('hase_22')
    sprite('ha210_00', 3)	# 18-20
    sprite('ha210_01', 3)	# 21-23
    sprite('ha210_01', 2)	# 24-25
    sprite('ha210_02', 2)	# 26-27
    SFX_0('004_swing_grap_1_2')
    sprite('ha210_03', 2)	# 28-29
    Unknown1015(15000)
    Unknown8000(100, 1, 1)
    sprite('ha210_04', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    Unknown8010(0, 1, 1)
    sprite('ha210_05', 3)	# 33-35
    sprite('ha210_06', 3)	# 36-38
    sprite('ha210_07', 3)	# 39-41
    sprite('ha210_08', 4)	# 42-45
    sprite('ha210_09', 4)	# 46-49
    sprite('ha210_10', 3)	# 50-52
    sprite('ha210_10', 1)	# 53-53
    SFX_3('hase_22')
    label(0)
    sprite('ha000_00', 7)	# 54-60
    sprite('ha000_01', 7)	# 61-67
    sprite('ha000_02', 7)	# 68-74
    sprite('ha000_03', 7)	# 75-81
    sprite('ha000_04', 7)	# 82-88
    sprite('ha000_05', 7)	# 89-95
    sprite('ha000_06', 7)	# 96-102
    sprite('ha000_07', 7)	# 103-109
    sprite('ha000_08', 7)	# 110-116
    sprite('ha000_09', 7)	# 117-123
    sprite('ha000_10', 7)	# 124-130
    sprite('ha000_11', 7)	# 131-137
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 138-138

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ha010_00', 1)	# 1-1
    sprite('ha010_01', 1)	# 2-2
    sprite('ha232_00', 2)	# 3-4
    sprite('ha232_01', 2)	# 5-6
    sprite('ha232_02', 2)	# 7-8
    sprite('ha232_03', 2)	# 9-10
    tag_voice(0, 'bha304_0', 'bha157_1', '', '')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha232_04', 1)	# 11-11
    sprite('ha232_05', 3)	# 12-14
    sprite('ha232_08', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    GFX_0('ha_232', -1)
    sprite('ha232_09', 3)	# 18-20
    sprite('ha232_10', 3)	# 21-23
    sprite('ha232_11', 3)	# 24-26
    sprite('ha232_12', 3)	# 27-29
    sprite('ha232_13', 3)	# 30-32
    sprite('ha232_14', 3)	# 33-35
    sprite('ha232_15', 3)	# 36-38
    sprite('ha232_16', 3)	# 39-41
    sprite('ha232_17', 3)	# 42-44
    sprite('ha010_01', 2)	# 45-46
    sprite('ha010_00', 2)	# 47-48
    label(0)
    sprite('ha000_00', 7)	# 49-55
    sprite('ha000_01', 7)	# 56-62
    sprite('ha000_02', 7)	# 63-69
    sprite('ha000_03', 7)	# 70-76
    sprite('ha000_04', 7)	# 77-83
    sprite('ha000_05', 7)	# 84-90
    sprite('ha000_06', 7)	# 91-97
    sprite('ha000_07', 7)	# 98-104
    sprite('ha000_08', 7)	# 105-111
    sprite('ha000_09', 7)	# 112-118
    sprite('ha000_10', 7)	# 119-125
    sprite('ha000_11', 7)	# 126-132
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 133-133

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('ha212_00', 2)	# 1-2
    sprite('ha212_01', 2)	# 3-4
    sprite('ha212_02', 3)	# 5-7
    sprite('ha212_03', 3)	# 8-10
    sprite('ha212_04', 3)	# 11-13
    sprite('ha212_05', 2)	# 14-15
    SFX_0('005_swing_grap_2_2')
    sprite('ha212_06', 2)	# 16-17
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha212_07', 2)	# 18-19
    tag_voice(0, 'bha158_0', 'bha158_1', '', '')
    sprite('ha212_08', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    GFX_0('ha_212', -1)
    sprite('ha212_09', 4)	# 23-26
    sprite('ha212_10', 4)	# 27-30
    sprite('ha212_11', 4)	# 31-34
    sprite('ha212_12', 4)	# 35-38
    sprite('ha212_13', 4)	# 39-42
    sprite('ha212_14', 3)	# 43-45
    sprite('ha212_15', 3)	# 46-48
    sprite('ha212_16', 3)	# 49-51
    sprite('ha212_17', 3)	# 52-54
    sprite('ha212_18', 3)	# 55-57
    sprite('ha212_19', 2)	# 58-59
    sprite('ha212_19', 1)	# 60-60
    SFX_3('hase_22')
    ExitState()
    label(1)
    sprite('ha431_00', 2)	# 61-62
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 2)	# 63-64
    sprite('ha431_02', 2)	# 65-66
    sprite('ha431_03', 2)	# 67-68
    sprite('ha431_04', 2)	# 69-70
    sprite('ha431_05', 1)	# 71-71
    sprite('ha431_06', 1)	# 72-72
    sprite('ha431_07', 1)	# 73-73
    sprite('ha431_08', 1)	# 74-74
    sprite('ha431_09', 1)	# 75-75
    sprite('ha431_10', 1)	# 76-76
    sprite('ha431_11', 1)	# 77-77
    sprite('ha431_12', 1)	# 78-78
    sprite('ha431_15', 1)	# 79-79
    sprite('ha431_16', 9)	# 80-88	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(600000)
    sprite('ha431_17', 3)	# 89-91
    sprite('ha431_18', 3)	# 92-94
    sprite('ha431_19', 3)	# 95-97
    sprite('ha431_20', 3)	# 98-100
    sprite('ha431_21', 3)	# 101-103
    sprite('ha431_22', 2)	# 104-105
    sprite('ha431_23', 2)	# 106-107
    sprite('ha431_24', 2)	# 108-109
    sprite('ha431_25', 2)	# 110-111
    sprite('ha431_26', 2)	# 112-113
    sprite('ha431_27', 2)	# 114-115
    sprite('ha431_28', 2)	# 116-117
    sprite('ha431_29', 2)	# 118-119
    sprite('ha000_00', 1)	# 120-120

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('ha000_00', 7)	# 1-7
    sprite('ha000_01', 7)	# 8-14
    sprite('ha000_02', 7)	# 15-21
    sprite('ha000_03', 7)	# 22-28
    sprite('ha000_04', 7)	# 29-35
    sprite('ha000_05', 7)	# 36-42
    sprite('ha000_06', 7)	# 43-49
    sprite('ha000_07', 7)	# 50-56
    sprite('ha000_08', 7)	# 57-63
    sprite('ha000_09', 7)	# 64-70
    sprite('ha000_10', 7)	# 71-77
    sprite('ha000_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha212_00', 2)	# 85-86
    sprite('ha212_01', 2)	# 87-88
    sprite('ha212_02', 3)	# 89-91
    sprite('ha212_03', 3)	# 92-94
    sprite('ha212_04', 3)	# 95-97
    sprite('ha212_05', 2)	# 98-99
    SFX_0('005_swing_grap_2_2')
    sprite('ha212_06', 2)	# 100-101
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha212_07', 2)	# 102-103
    tag_voice(0, 'bha158_0', 'bha158_1', '', '')
    sprite('ha212_08', 3)	# 104-106	 **attackbox here**
    RefreshMultihit()
    GFX_0('ha_212', -1)
    sprite('ha212_09', 4)	# 107-110
    sprite('ha212_10', 4)	# 111-114
    sprite('ha212_11', 4)	# 115-118
    sprite('ha212_12', 4)	# 119-122
    sprite('ha212_13', 4)	# 123-126
    sprite('ha212_14', 3)	# 127-129
    sprite('ha212_15', 3)	# 130-132
    sprite('ha212_16', 3)	# 133-135
    sprite('ha212_17', 3)	# 136-138
    sprite('ha212_18', 3)	# 139-141
    sprite('ha212_19', 2)	# 142-143
    sprite('ha212_19', 1)	# 144-144
    SFX_3('hase_22')

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 22)	# 1-22
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 23-23
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('ha251_00', 10)	# 24-33
    physicsXImpulse(35000)
    physicsYImpulse(25000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    sprite('ha251_01', 4)	# 34-37
    SFX_0('004_swing_grap_1_1')
    sprite('ha251_02', 4)	# 38-41
    sprite('ha251_03', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    Unknown1019(15)
    sprite('ha251_04', 4)	# 45-48
    sprite('ha251_05', 4)	# 49-52
    sprite('ha251_06', 4)	# 53-56
    sprite('ha251_07', 4)	# 57-60
    sprite('ha251_08', 32767)	# 61-32827
    label(2)
    sprite('ha024_00', 3)	# 32828-32830
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('ha024_01', 3)	# 32831-32833
    sprite('ha024_02', 3)	# 32834-32836
    sprite('ha024_03', 3)	# 32837-32839
    sprite('ha024_04', 3)	# 32840-32842
    sprite('ha000_00', 7)	# 32843-32849
    sprite('ha000_01', 7)	# 32850-32856
    sprite('ha000_02', 7)	# 32857-32863
    sprite('ha000_03', 7)	# 32864-32870
    sprite('ha000_04', 7)	# 32871-32877
    sprite('ha000_05', 7)	# 32878-32884
    sprite('ha000_06', 7)	# 32885-32891
    sprite('ha000_07', 7)	# 32892-32898
    sprite('ha000_08', 7)	# 32899-32905
    sprite('ha000_09', 7)	# 32906-32912
    sprite('ha000_10', 7)	# 32913-32919
    sprite('ha000_11', 7)	# 32920-32926

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('ha202_00', 1)	# 1-1
    sprite('ha202_01', 1)	# 2-2
    sprite('ha202_02', 2)	# 3-4
    sprite('ha202_03', 1)	# 5-5
    sprite('ha202_04', 1)	# 6-6
    sprite('ha202_05', 4)	# 7-10
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha202_06', 1)	# 11-11
    sprite('ha202_07', 2)	# 12-13	 **attackbox here**
    GFX_0('ha_202', -1)
    sprite('ha202_08', 1)	# 14-14
    Recovery()
    Unknown2063()
    sprite('ha202_09', 2)	# 15-16
    sprite('ha202_10', 3)	# 17-19
    sprite('ha202_11', 3)	# 20-22
    sprite('ha202_12', 3)	# 23-25
    sprite('ha202_13', 2)	# 26-27
    sprite('ha202_14', 2)	# 28-29
    sprite('ha202_15', 2)	# 30-31
    sprite('ha202_16', 2)	# 32-33
    sprite('ha000_00', 7)	# 34-40
    sprite('ha000_01', 7)	# 41-47
    sprite('ha000_02', 7)	# 48-54
    sprite('ha000_03', 7)	# 55-61
    sprite('ha000_04', 7)	# 62-68
    sprite('ha000_05', 7)	# 69-75
    sprite('ha000_06', 7)	# 76-82
    sprite('ha000_07', 7)	# 83-89
    sprite('ha000_08', 7)	# 90-96
    sprite('ha000_09', 7)	# 97-103
    sprite('ha000_10', 7)	# 104-110
    sprite('ha000_11', 7)	# 111-117

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
    sprite('ha212_00', 2)	# 1-2
    sprite('ha212_01', 2)	# 3-4
    sprite('ha212_02', 3)	# 5-7
    sprite('ha212_03', 3)	# 8-10
    sprite('ha212_04', 3)	# 11-13
    sprite('ha212_05', 2)	# 14-15
    SFX_0('005_swing_grap_2_2')
    sprite('ha212_06', 2)	# 16-17
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha212_07', 2)	# 18-19
    sprite('ha212_08', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    GFX_0('ha_212', -1)
    sprite('ha212_09', 4)	# 23-26
    sprite('ha212_10', 4)	# 27-30
    sprite('ha212_11', 4)	# 31-34
    sprite('ha212_12', 4)	# 35-38
    sprite('ha212_13', 4)	# 39-42
    sprite('ha212_14', 3)	# 43-45
    sprite('ha212_15', 3)	# 46-48
    sprite('ha212_16', 3)	# 49-51
    sprite('ha212_17', 3)	# 52-54
    sprite('ha212_18', 3)	# 55-57
    sprite('ha212_19', 2)	# 58-59
    sprite('ha212_19', 1)	# 60-60
    SFX_3('hase_22')
    ExitState()
    label(1)
    sprite('ha431_00', 2)	# 61-62
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 2)	# 63-64
    sprite('ha431_02', 2)	# 65-66
    sprite('ha431_03', 2)	# 67-68
    sprite('ha431_04', 2)	# 69-70
    sprite('ha431_05', 1)	# 71-71
    sprite('ha431_06', 1)	# 72-72
    sprite('ha431_07', 1)	# 73-73
    sprite('ha431_08', 1)	# 74-74
    sprite('ha431_09', 1)	# 75-75
    sprite('ha431_10', 1)	# 76-76
    sprite('ha431_11', 1)	# 77-77
    sprite('ha431_12', 1)	# 78-78
    sprite('ha431_15', 1)	# 79-79
    sprite('ha431_16', 9)	# 80-88	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(600000)
    sprite('ha431_17', 3)	# 89-91
    sprite('ha431_18', 3)	# 92-94
    sprite('ha431_19', 3)	# 95-97
    sprite('ha431_20', 3)	# 98-100
    sprite('ha431_21', 3)	# 101-103
    sprite('ha431_22', 2)	# 104-105
    sprite('ha431_23', 2)	# 106-107
    sprite('ha431_24', 2)	# 108-109
    sprite('ha431_25', 2)	# 110-111
    sprite('ha431_26', 2)	# 112-113
    sprite('ha431_27', 2)	# 114-115
    sprite('ha431_28', 2)	# 116-117
    sprite('ha431_29', 2)	# 118-119
    sprite('ha000_00', 1)	# 120-120

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('ha000_00', 7)	# 1-7
    sprite('ha000_01', 7)	# 8-14
    sprite('ha000_02', 7)	# 15-21
    sprite('ha000_03', 7)	# 22-28
    sprite('ha000_04', 7)	# 29-35
    sprite('ha000_05', 7)	# 36-42
    sprite('ha000_06', 7)	# 43-49
    sprite('ha000_07', 7)	# 50-56
    sprite('ha000_08', 7)	# 57-63
    sprite('ha000_09', 7)	# 64-70
    sprite('ha000_10', 7)	# 71-77
    sprite('ha000_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha212_00', 2)	# 85-86
    sprite('ha212_01', 2)	# 87-88
    sprite('ha212_02', 3)	# 89-91
    sprite('ha212_03', 3)	# 92-94
    sprite('ha212_04', 3)	# 95-97
    sprite('ha212_05', 2)	# 98-99
    SFX_0('005_swing_grap_2_2')
    sprite('ha212_06', 2)	# 100-101
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha212_07', 2)	# 102-103
    sprite('ha212_08', 3)	# 104-106	 **attackbox here**
    RefreshMultihit()
    GFX_0('ha_212', -1)
    sprite('ha212_09', 4)	# 107-110
    sprite('ha212_10', 4)	# 111-114
    sprite('ha212_11', 4)	# 115-118
    sprite('ha212_12', 4)	# 119-122
    sprite('ha212_13', 4)	# 123-126
    sprite('ha212_14', 3)	# 127-129
    sprite('ha212_15', 3)	# 130-132
    sprite('ha212_16', 3)	# 133-135
    sprite('ha212_17', 3)	# 136-138
    sprite('ha212_18', 3)	# 139-141
    sprite('ha212_19', 2)	# 142-143
    sprite('ha212_19', 1)	# 144-144
    SFX_3('hase_22')

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ha030_00', 7)	# 1-7
    physicsXImpulse(10000)
    label(0)
    sprite('ha030_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('ha030_02', 7)	# 15-21
    sprite('ha030_03', 7)	# 22-28
    sprite('ha030_04', 7)	# 29-35
    sprite('ha030_05', 7)	# 36-42
    sprite('ha030_06', 7)	# 43-49
    sprite('ha030_07', 7)	# 50-56
    sprite('ha030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha310_00', 1)	# 64-64
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ha310_01', 2)	# 65-66
    sprite('ha310_02', 3)	# 67-69	 **attackbox here**
    Unknown1084(1)
    sprite('ha310_03', 4)	# 70-73
    SFX_4('bha154')
    SFX_0('004_swing_grap_1_0')
    sprite('ha310_04', 5)	# 74-78
    StartMultihit()
    sprite('ha310_05', 8)	# 79-86
    sprite('ha310_06', 3)	# 87-89
    sprite('ha310_07', 3)	# 90-92

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2018(0, 80)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        PushbackX(9800)
        Unknown9016(0)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(54)
        Unknown9142(45)
    sprite('ha310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ha311_00', 3)	# 4-6
    SFX_4('bha153')
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ha311_01', 4)	# 7-10
    sprite('ha311_02', 4)	# 11-14
    sprite('ha311_03', 5)	# 15-19
    sprite('ha311_04', 5)	# 20-24
    sprite('ha311_05', 6)	# 25-30
    sprite('ha311_06', 6)	# 31-36
    sprite('ha311_07', 4)	# 37-40	 **attackbox here**
    Unknown8004(100, 1, 1)
    sprite('ha311_08', 4)	# 41-44
    sprite('ha311_09', 4)	# 45-48
    sprite('ha311_10', 4)	# 49-52
    sprite('ha311_11', 4)	# 53-56
    sprite('ha311_12', 4)	# 57-60
    sprite('ha311_13', 4)	# 61-64
    sprite('ha311_14', 4)	# 65-68

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ha030_00', 7)	# 1-7
    physicsXImpulse(10000)
    label(0)
    sprite('ha030_01', 7)	# 8-14
    SFX_FOOTSTEP_(100, 0, 1)
    sprite('ha030_02', 7)	# 15-21
    sprite('ha030_03', 7)	# 22-28
    sprite('ha030_04', 7)	# 29-35
    sprite('ha030_05', 7)	# 36-42
    sprite('ha030_06', 7)	# 43-49
    sprite('ha030_07', 7)	# 50-56
    sprite('ha030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha310_00', 1)	# 64-64
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ha310_01', 2)	# 65-66
    sprite('ha310_02', 3)	# 67-69	 **attackbox here**
    Unknown1084(1)
    sprite('ha310_03', 4)	# 70-73
    SFX_4('bha154')
    SFX_0('004_swing_grap_1_0')
    sprite('ha310_04', 5)	# 74-78
    StartMultihit()
    sprite('ha310_05', 8)	# 79-86
    sprite('ha310_06', 3)	# 87-89
    sprite('ha310_07', 3)	# 90-92

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Unknown2018(0, 80)
        Unknown13021(1)
        Unknown21005(1)
        AttackLevel_(2)
        Damage(500)
        Unknown11099(1)
        AirPushbackX(20000)
        AirPushbackY(18000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(60)
        Hitstop(0)
        AttackP2(100)
        JumpCancel_(0)
        Unknown11069('BackThrowExe')
    sprite('ha310_02', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('ha313_00', 3)	# 4-6
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha313_01', 3)	# 7-9
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha313_02', 3)	# 10-12
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha313_03', 3)	# 13-15	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('ha313_04', 3)	# 16-18
    SFX_1('bha153')
    SFX_0('005_swing_grap_2_1')
    sprite('ha313_05', 3)	# 19-21
    sprite('ha313_06', 3)	# 22-24
    sprite('ha313_07', 3)	# 25-27
    sprite('ha313_08', 3)	# 28-30
    sprite('ha313_09', 3)	# 31-33	 **attackbox here**
    AttackLevel_(4)
    Damage(1500)
    AttackP2(50)
    AirUntechableTime(60)
    Hitstop(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    WallbounceReboundTime(50)
    Unknown9178(1)
    AirHitstunAfterWallbounce(50)
    Unknown9362(1)
    Unknown9364(30)
    Unknown11072(1, -380000, 82000)
    Unknown11069('')
    RefreshMultihit()

    def upon_12():
        JumpCancel_(1)
    sprite('ha313_10', 3)	# 34-36
    EnableCollision(1)
    sprite('ha313_11', 3)	# 37-39
    sprite('ha313_12', 3)	# 40-42
    sprite('ha313_13', 6)	# 43-48
    Unknown8000(100, 1, 1)
    sprite('ha313_14', 6)	# 49-54
    sprite('ha313_15', 6)	# 55-60

@Subroutine
def SkillInit():
    HitOrBlockCancel('Guren_Hasei')
    HitOrBlockCancel('GurenB_Hasei')
    HitOrBlockCancel('Yanagi_Hasei')
    HitOrBlockCancel('Renka_Hasei')
    HitOrBlockCancel('Zantetu_Hasei')
    HitOrBlockCancel('RenkaEx_Hasei')
    if (not SLOT_59):
        Unknown30068(1)
        SFX_3('hase_25')
        GFX_0('ha_power_circle', -1)
        GFX_0('ha_power_light', -1)
        GFX_0('ha_power_bluelight', -1)
        if Unknown23148('RenkaEx'):
            GFX_0('ha_power_2', -1)
        elif Unknown23148('Yanagi'):
            GFX_0('ha_power_2', -1)
        else:
            GFX_0('ha_power_1', -1)
        ConsumeSuperMeter(-5000)
        AttackP2(100)
    SLOT_59 = 0

    def upon_85():
        SLOT_59 = 1

@State
def Guren():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        AttackP1(80)
        AttackP2(75)
        AirUntechableTime(60)
        AirPushbackX(16000)
        AirPushbackY(16000)
        hitstun(26)
        PushbackX(12000)
        Unknown11056(0)
        Unknown9015(1)
        Unknown1084(0)
        Unknown3029(1)
        Unknown3069(0)
        callSubroutine('SkillInit')
    sprite('ha400_00', 2)	# 1-2
    sprite('ha400_01', 1)	# 3-3
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_01', 1)	# 4-4
    Unknown7007('6268613230305f300000000000000000640000006268613230305f310000000000000000640000006268613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha400_02', 2)	# 5-6
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_03', 4)	# 7-10
    physicsXImpulse(55000)
    Unknown2015(150)
    sprite('ha400_04', 3)	# 11-13
    sprite('ha400_05', 3)	# 14-16	 **attackbox here**
    physicsXImpulse(0)
    setGravity(0)
    sprite('ha400_06', 4)	# 17-20
    SFX_0('208_brake_normal')
    Recovery()
    Unknown2063()
    Unknown2015(-1)
    sprite('ha400_07', 4)	# 21-24
    sprite('ha400_08', 4)	# 25-28
    Unknown3029(0)
    sprite('ha400_09', 4)	# 29-32
    sprite('ha400_10', 4)	# 33-36
    SFX_3('hase_22')

@State
def GurenB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(2)
        AirUntechableTime(60)
        AirPushbackX(16000)
        AirPushbackY(16000)
        hitstun(26)
        PushbackX(12000)
        Unknown11056(0)
        Unknown9015(1)
        Unknown1084(0)
        Unknown3029(1)
        Unknown3069(0)
        callSubroutine('SkillInit')
    sprite('ha400_00', 2)	# 1-2
    sprite('ha400_01', 1)	# 3-3
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_01', 1)	# 4-4
    Unknown7007('6268613230305f300000000000000000640000006268613230305f310000000000000000640000006268613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha400_02', 2)	# 5-6
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_1')
    sprite('ha400_03', 4)	# 7-10
    physicsXImpulse(55000)
    Unknown2015(150)
    sprite('ha400_04', 8)	# 11-18
    sprite('ha400_05', 3)	# 19-21	 **attackbox here**
    physicsXImpulse(0)
    setGravity(0)
    sprite('ha400_06', 6)	# 22-27
    SFX_0('208_brake_normal')
    Recovery()
    Unknown2063()
    Unknown2015(-1)
    sprite('ha400_07', 5)	# 28-32
    sprite('ha400_08', 5)	# 33-37
    Unknown3029(0)
    Unknown14077(1)
    sprite('ha400_09', 5)	# 38-42
    sprite('ha400_10', 4)	# 43-46
    SFX_3('hase_22')

@State
def Renka():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(4)
        Damage(1300)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        Unknown9142(39)
        Unknown9130(49)
        AirUntechableTime(30)
        PushbackX(19800)
        AirPushbackY(12000)
        Unknown9310(1)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Hitstop(15)
        Unknown2004(1, 0)

        def upon_12():
            clearUponHandler(12)
            PushbackX(0)
        callSubroutine('SkillInit')
    sprite('ha401_00', 1)	# 1-1
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha401_01', 1)	# 2-2
    sprite('ha401_02', 1)	# 3-3
    sprite('ha401_02', 1)	# 4-4
    Unknown7007('6268613230315f300000000000000000640000006268613230315f310000000000000000640000006268613230315f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(10000)
    sprite('ha401_03', 2)	# 5-6
    sprite('ha401_04', 2)	# 7-8
    SFX_0('004_swing_grap_1_1')
    sprite('ha401_05', 3)	# 9-11	 **attackbox here**
    GFX_0('ha_kick', -1)
    GFX_0('ha_kick_b', -1)
    GFX_1('haef_kick_drop', 0)
    physicsXImpulse(0)
    sprite('ha401_06', 2)	# 12-13
    GFX_0('ha_kick2', -1)
    GFX_0('ha_kick2b', -1)
    sprite('ha401_07', 2)	# 14-15
    physicsXImpulse(10000)
    sprite('ha401_08', 2)	# 16-17
    GFX_0('ha_kick3', -1)
    GFX_0('ha_kick3b', -1)
    sprite('ha401_09', 2)	# 18-19
    sprite('ha401_10', 2)	# 20-21
    SFX_0('004_swing_grap_1_2')
    sprite('ha401_11', 3)	# 22-24	 **attackbox here**
    GFX_0('ha_kick4', -1)
    GFX_0('ha_kick4b', -1)
    GFX_1('haef_kick_drop', 0)
    physicsXImpulse(0)
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackX(20000)
    AirPushbackY(20000)
    PushbackX(39900)
    Unknown9310(0)
    HitLow(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Hitstop(12)
    sprite('ha401_12', 4)	# 25-28
    Recovery()
    Unknown2063()
    sprite('ha401_13', 4)	# 29-32
    sprite('ha401_14', 4)	# 33-36
    Unknown3029(0)
    Unknown14077(1)
    sprite('ha401_15', 4)	# 37-40
    sprite('ha401_16', 4)	# 41-44
    SFX_3('hase_22')

@State
def RenkaEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(0)
        AttackLevel_(4)
        Damage(1400)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(2)
        Unknown9142(39)
        Unknown9130(49)
        AirUntechableTime(30)
        PushbackX(4800)
        AirPushbackY(12000)
        Unknown9310(1)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        Hitstop(15)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown2004(1, 0)

        def upon_12():
            clearUponHandler(12)
            PushbackX(0)
        callSubroutine('SkillInit')
    sprite('ha401_00ex02', 1)	# 1-1
    sprite('ha401_01ex02', 1)	# 2-2
    Unknown3029(1)
    Unknown3069(0)
    physicsXImpulse(20000)
    sprite('ha401_02ex01', 1)	# 3-3
    sprite('ha401_02ex01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown7007('6268613230315f300000000000000000640000006268613230315f310000000000000000640000006268613230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha401_03ex02', 2)	# 5-6
    sprite('ha401_04ex02', 2)	# 7-8
    physicsXImpulse(0)
    SFX_0('004_swing_grap_1_1')
    sprite('ha401_05ex03', 3)	# 9-11	 **attackbox here**
    GFX_0('haef410_kick', -1)
    sprite('ha401_06ex02', 3)	# 12-14
    sprite('ha410_00', 2)	# 15-16
    sprite('ha410_01', 2)	# 17-18
    sprite('ha410_02', 2)	# 19-20
    physicsXImpulse(70000)
    sprite('ha410_03', 3)	# 21-23
    SFX_0('004_swing_grap_1_2')
    Unknown1019(0)
    sprite('ha410_04', 3)	# 24-26	 **attackbox here**
    GFX_0('haef410_kick2', -1)
    physicsXImpulse(0)
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(30000)
    PushbackX(39800)
    Unknown9310(0)
    HitLow(0)
    Unknown11058('0000000001000000000000000000000000000000')
    Hitstop(12)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockJumpCancel(1)
    sprite('ha410_05', 5)	# 27-31
    Recovery()
    Unknown2063()
    sprite('ha410_06', 4)	# 32-35
    sprite('ha410_07', 4)	# 36-39
    Unknown3029(0)
    sprite('ha410_08', 4)	# 40-43
    sprite('ha410_09', 4)	# 44-47
    SFX_3('hase_22')

@State
def Zantetu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(80)
        AttackP2(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(30)
        AirPushbackX(10000)
        AirPushbackY(-60000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(20)
        Unknown9310(11)
        PushbackX(19800)
        Hitstop(15)
        HitOverhead(2)
        Unknown11056(0)
        Unknown9016(1)
        Unknown2004(1, 0)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_52 = 1
            Unknown26('ha402_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_52 = 0
                setInvincible(0)
        callSubroutine('SkillInit')
        if Unknown23145('CmnActJumpPre'):
            Unknown23159('Zantetu_JumpCancel')
    sprite('ha402_00', 2)	# 1-2
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha402_01', 2)	# 3-4
    sprite('ha402_02', 2)	# 5-6
    sprite('ha402_03', 3)	# 7-9
    physicsXImpulse(10000)
    sprite('ha402_04', 4)	# 10-13
    sprite('ha402_05', 4)	# 14-17
    sprite('ha402_06', 4)	# 18-21
    physicsXImpulse(0)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    Unknown7007('6268613230325f300000000000000000640000006268613230325f310000000000000000640000006268613230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha402_07', 3)	# 22-24	 **attackbox here**
    GFX_0('ha402_col_dmy', 0)
    GFX_0('ha_402a', -1)
    sprite('ha402_08', 2)	# 25-26
    sprite('ha402_09', 2)	# 27-28
    sprite('ha402_10', 2)	# 29-30
    sprite('ha402_11', 2)	# 31-32
    physicsXImpulse(12000)
    sprite('ha402_12', 2)	# 33-34
    sprite('ha402_13', 2)	# 35-36
    sprite('ha402_14', 2)	# 37-38
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha402_15', 3)	# 39-41	 **attackbox here**
    physicsXImpulse(0)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(1500)
    AirPushbackX(-3000)
    AirPushbackY(5)
    Unknown9095()
    Unknown9190(0)
    Unknown9215()
    Hitstop(13)
    Unknown11058('0000000000000000010000000000000000000000')
    HitOverhead(0)
    HitLow(2)
    GFX_0('ha_402b', -1)
    sprite('ha402_16', 6)	# 42-47
    Recovery()
    Unknown2063()
    sprite('ha402_17', 6)	# 48-53
    sprite('ha402_18', 6)	# 54-59
    Unknown3029(0)
    sprite('ha402_19', 4)	# 60-63
    sprite('ha402_20', 4)	# 64-67

@State
def Agito():

    def upon_IMMEDIATE():
        Unknown17003()
        SLOT_66 = 1
    sprite('ha407_00', 3)	# 1-3
    Unknown1015(6000)
    physicsYImpulse(4000)
    setGravity(0)
    sprite('ha407_01', 3)	# 4-6
    Unknown1019(60)
    setGravity(1650)
    sprite('ha407_02', 3)	# 7-9
    Unknown1019(60)
    sprite('ha407_03', 2)	# 10-11
    physicsYImpulse(20000)
    Unknown1015(1000)
    Unknown1019(50)
    Unknown1043()
    SFX_0('004_swing_grap_1_2')
    SFX_0('004_swing_grap_1_2')
    Unknown7007('6268613230375f300000000000000000640000006268613230375f310000000000000000640000006268613230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha407_04', 4)	# 12-15
    GFX_0('ha_407', -1)
    GFX_0('ha_407_b', -1)
    GFX_1('haef_kick_drop', 0)
    sprite('ha407_05', 3)	# 16-18
    Unknown1019(30)
    Recovery()
    sprite('ha407_06', 3)	# 19-21
    sprite('ha407_05', 3)	# 22-24
    sprite('ha407_06', 3)	# 25-27
    sprite('ha407_07', 3)	# 28-30
    sprite('ha407_08', 3)	# 31-33
    sprite('ha407_09', 3)	# 34-36

@State
def Tubaki():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        AirPushbackX(3000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(2000)
        PushbackX(12000)
        Hitstop(8)
        HitOverhead(2)
        Unknown9310(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        Unknown1017()
        Unknown1022()
        Unknown1037()
        Unknown1084(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha404_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('ha404_00', 2)	# 1-2
    Unknown1018()
    physicsXImpulse(100)
    physicsYImpulse(600)
    setGravity(50)
    sprite('ha404_01', 2)	# 3-4
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha404_02', 2)	# 5-6
    sprite('ha404_03', 2)	# 7-8
    Unknown7007('6268613230355f300000000000000000640000006268613230355f310000000000000000640000006268613230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha404_04', 2)	# 9-10
    sprite('ha404_05', 2)	# 11-12
    sprite('ha404_06', 2)	# 13-14
    sprite('ha404_07', 2)	# 15-16
    sprite('ha404_08', 2)	# 17-18
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha404_09', 3)	# 19-21	 **attackbox here**
    GFX_0('ha404_col_dmy', 0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 22-23
    Recovery()
    sprite('ha404_11', 2)	# 24-25
    sprite('ha404_12', 2)	# 26-27
    Unknown3029(0)
    Unknown14077(1)
    sprite('ha404_13', 3)	# 28-30
    Unknown1043()
    sprite('ha404_14', 3)	# 31-33
    sprite('ha404_15', 3)	# 34-36
    sprite('ha404_16', 3)	# 37-39
    sprite('ha020_03', 3)	# 40-42
    sprite('ha020_04', 3)	# 43-45
    sprite('ha020_05', 3)	# 46-48
    label(0)
    sprite('ha020_06', 3)	# 49-51
    sprite('ha020_07', 3)	# 52-54
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('ha024_00', 2)	# 55-56
    Unknown8000(0, 1, 1)
    sprite('ha024_01', 2)	# 57-58
    sprite('ha024_02', 3)	# 59-61
    sprite('ha024_03', 2)	# 62-63

@State
def TubakiEx():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(2500)
        AttackP1(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(60)
        AirPushbackX(3000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(2000)
        PushbackX(12000)
        Hitstop(8)
        HitOverhead(2)
        Unknown9310(17)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown22004(5, 1)
        Unknown1017()
        Unknown1022()
        Unknown1037()
        Unknown1084(1)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha404_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha404_00', 2)	# 1-2
    Unknown1018()
    physicsXImpulse(100)
    physicsYImpulse(600)
    setGravity(50)
    sprite('ha404_01', 1)	# 3-3
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha404_01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ha404_02', 2)	# 5-6
    sprite('ha404_03', 2)	# 7-8
    Unknown7007('6268613230355f300000000000000000640000006268613230355f310000000000000000640000006268613230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ha404_04', 1)	# 9-9
    sprite('ha404_05', 1)	# 10-10
    sprite('ha404_06', 1)	# 11-11
    sprite('ha404_07', 1)	# 12-12
    sprite('ha404_08', 2)	# 13-14
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha404_09', 3)	# 15-17	 **attackbox here**
    GFX_0('ha404_col_dmy', 0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 18-19
    Recovery()
    sprite('ha404_11', 2)	# 20-21
    sprite('ha404_12', 2)	# 22-23
    Unknown3029(0)
    Unknown14077(1)
    sprite('ha404_13', 3)	# 24-26
    Unknown1043()
    sprite('ha404_14', 3)	# 27-29
    sprite('ha404_15', 3)	# 30-32
    sprite('ha404_16', 3)	# 33-35
    sprite('ha020_03', 4)	# 36-39

@State
def Yanagi():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        AttackP2(75)
        AirHitstunAnimation(5)
        GroundedHitstunAnimation(5)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11064(1)
        Unknown28(78, 'Assault5Grip')
        Unknown14077(0)

        def upon_42():
            Unknown2037(1)
            GuardPoint_(0)
            ScreenShake(8000, 2000)
        callSubroutine('SkillInit')
    sprite('ha409_00', 3)	# 1-3
    sprite('ha409_01', 3)	# 4-6
    tag_voice(1, 'bha208_0', 'bha208_1', 'bha208_2', '')
    GFX_0('ha_409', 0)
    setInvincible(1)
    GuardPoint_(1)
    Unknown22031(15, 15)
    Unknown3029(1)
    Unknown3069(0)
    Unknown3070(1)
    Unknown8007(-1, 1, 1)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ha409_02', 3)	# 7-9
    sprite('ha409_03', 3)	# 10-12
    physicsXImpulse(10000)
    SFX_0('004_swing_grap_1_2')
    SFX_0('000_airdash_2')
    GFX_0('ha_409_dash', 0)
    SFX_3('hase_23')
    sprite('ha409_04', 3)	# 13-15
    Unknown1019(700)
    sprite('ha409_03', 3)	# 16-18
    Unknown1019(80)
    sprite('ha409_04', 3)	# 19-21
    Unknown1019(80)
    sprite('ha409_03', 3)	# 22-24
    Unknown1019(80)
    sprite('ha409_04', 3)	# 25-27
    Unknown1019(50)
    sprite('ha409_05', 2)	# 28-29
    if (not SLOT_2):
        setInvincible(0)
    Unknown1019(50)
    sprite('ha409_06', 3)	# 30-32	 **attackbox here**
    if (not SLOT_2):
        StartMultihit()
    Unknown3029(0)
    Unknown1019(25)
    Unknown26('ha_409_dash')
    Unknown8006(100, 1, 0)
    sprite('ha409_16', 3)	# 33-35
    physicsXImpulse(0)
    sprite('ha409_17', 3)	# 36-38
    sprite('ha409_18', 3)	# 39-41

@State
def Assault5Grip():

    def upon_IMMEDIATE():
        Unknown17011('Assault5Exe', 2, 0, 0)
        Unknown11023(1)
        Unknown11054(1000000)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11002(-1)
        Unknown11045(0)
        Unknown30061(0)
        Unknown11025(0)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown11064(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        HitLow(0)
        HitOverhead(0)
        HitAirUnblockable(0)
        Unknown13024(0)
        Unknown13045(0)
        Unknown30068(1)
    sprite('ha409_06', 3)	# 1-3	 **attackbox here**
    sprite('ha409_16', 3)	# 4-6
    physicsXImpulse(0)
    sprite('ha409_17', 3)	# 7-9
    sprite('ha409_18', 3)	# 10-12

@State
def Assault5Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(3500)
        MinimumDamagePct(0)
        AttackP2(100)
        Hitstop(0)
        Unknown9310(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(5000)
        AirPushbackY(-20000)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown11072(1, 150000, 0)
        Unknown11108('03000000')
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown23022(1)
        HitOrBlockCancel('Guren_Hasei')
        HitOrBlockCancel('GurenB_Hasei')
        HitOrBlockCancel('Renka_Hasei')
        HitOrBlockCancel('Zantetu_Hasei')
        HitOrBlockCancel('RenkaEx_Hasei')

        def upon_12():
            ScreenShake(5000, 15000)
    sprite('ha409_07', 1)	# 1-1	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    StartMultihit()
    sprite('ha409_07', 2)	# 2-3	 **attackbox here**
    tag_voice(0, 'bha209_0', 'bha209_1', 'bha209_2', '')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    StartMultihit()
    sprite('ha409_08', 3)	# 4-6
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha409_09', 10)	# 7-16
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha409_10', 3)	# 17-19
    Unknown5000(2, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha409_11', 3)	# 20-22
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha409_12', 2)	# 23-24
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha409_13', 20)	# 25-44	 **attackbox here**
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ha409_14', 3)	# 45-47
    sprite('ha409_15', 3)	# 48-50
    sprite('ha409_16', 3)	# 51-53
    sprite('ha409_17', 3)	# 54-56
    sprite('ha409_18', 3)	# 57-59

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5800)
        MinimumDamagePct(33)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(50)
        AirPushbackX(45900)
        AirPushbackY(36000)
        Hitstop(25)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11089(1)
        Unknown2004(1, 0)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha430_col_dmy')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha430_00', 4)	# 1-4
    setInvincible(1)
    sprite('ha430_01', 4)	# 5-8
    sprite('ha430_02', 4)	# 9-12
    sprite('ha430_02', 1)	# 13-13
    Unknown2036(47, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    tag_voice(1, 'bha250_0', 'bha250_1', '', '')
    sprite('ha430_03', 3)	# 14-16
    sprite('ha430_04', 3)	# 17-19
    sprite('ha430_05', 3)	# 20-22
    sprite('ha430_06', 3)	# 23-25
    sprite('ha430_07', 3)	# 26-28
    sprite('ha430_08', 3)	# 29-31
    sprite('ha430_09', 3)	# 32-34
    sprite('ha430_10', 3)	# 35-37
    sprite('ha430_11', 4)	# 38-41
    sprite('ha430_12', 4)	# 42-45
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 4)	# 46-49
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 50-53
    GFX_0('ha_DD_1_aura', 0)
    loopRest()
    sendToLabelUpon(24, 0)
    sendToLabelUpon(25, 0)
    SLOT_52 = 10
    label(99)
    sprite('ha430_13', 4)	# 54-57
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 3)	# 58-60
    sprite('ha430_14', 1)	# 61-61
    SLOT_52 = (SLOT_52 + (-1))
    if (SLOT_52 == 8):
        GFX_1('haef_DD_1_ring', 0)
        setInvincible(0)
    if (SLOT_52 == 4):
        GFX_1('haef_DD_1_ring', 0)
    if (SLOT_52 == 1):
        Unknown10000(200)
    Unknown19(0, 2, 52)
    gotoLabel(99)
    label(0)
    clearUponHandler(24)
    clearUponHandler(25)
    sprite('ha430_15', 4)	# 62-65
    GFX_1('haef_DD_1_ring', 0)
    physicsXImpulse(5000)
    sprite('ha430_16', 2)	# 66-67
    SFX_0('006_swing_blade_2')
    sprite('ha430_16', 2)	# 68-69
    sprite('ha430_17', 4)	# 70-73
    tag_voice(0, 'bha251_0', 'bha251_1', '', '')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('011_spin_0')
    sprite('ha430_18', 4)	# 74-77	 **attackbox here**
    GFX_0('ha430_col_dmy', 100)
    SFX_3('hase_20')
    ScreenShake(0, 16000)
    GFX_1('haef_DD_1_blast', 0)
    Unknown2015(200)
    physicsXImpulse(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21007(9, 32)
        clearUponHandler(10)
    GFX_0('ha_DD_1_shot', 0)
    Unknown38(9, 1)
    sprite('ha430_19', 5)	# 78-82
    setInvincible(0)
    sprite('ha430_20', 5)	# 83-87
    sprite('ha430_21', 5)	# 88-92
    sprite('ha430_22', 5)	# 93-97
    sprite('ha430_23', 5)	# 98-102
    Unknown14077(1)
    Unknown2015(-1)
    sprite('ha430_24', 4)	# 103-106
    sprite('ha430_25', 4)	# 107-110
    sprite('ha430_26', 4)	# 111-114
    sprite('ha430_27', 4)	# 115-118

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5000)
        MinimumDamagePct(31)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(50)
        AirPushbackX(45900)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2600)
        Hitstop(25)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11089(1)
        Unknown11064(1)
        Unknown2004(1, 0)

        def upon_32():
            setInvincible(1)
            Unknown22019('0000000000000000000000000100000000000000')
            SLOT_51 = 1
            Unknown26('ha430_col_dmy_OD')

        def upon_CLEAR_OR_EXIT():
            if SLOT_51:
                SLOT_51 = 0
                setInvincible(0)
    sprite('ha430_00', 4)	# 1-4
    setInvincible(1)
    sprite('ha430_01', 4)	# 5-8
    sprite('ha430_02', 4)	# 9-12
    sprite('ha430_02', 1)	# 13-13
    Unknown2036(47, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    tag_voice(1, 'bha250_0', 'bha250_1', '', '')
    sprite('ha430_03', 3)	# 14-16
    sprite('ha430_04', 3)	# 17-19
    sprite('ha430_05', 3)	# 20-22
    sprite('ha430_06', 3)	# 23-25
    sprite('ha430_07', 3)	# 26-28
    sprite('ha430_08', 3)	# 29-31
    sprite('ha430_09', 3)	# 32-34
    sprite('ha430_10', 3)	# 35-37
    sprite('ha430_11', 4)	# 38-41
    sprite('ha430_12', 4)	# 42-45
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 4)	# 46-49
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 50-53
    GFX_0('ha_DD_1_aura', 0)
    loopRest()
    sendToLabelUpon(24, 0)
    sendToLabelUpon(25, 0)
    SLOT_52 = 10
    label(99)
    sprite('ha430_13', 4)	# 54-57
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 3)	# 58-60
    sprite('ha430_14', 1)	# 61-61
    SLOT_52 = (SLOT_52 + (-1))
    if (SLOT_52 == 8):
        GFX_1('haef_DD_1_ring', 0)
        setInvincible(0)
    if (SLOT_52 == 4):
        GFX_1('haef_DD_1_ring', 0)
    if (SLOT_52 == 1):
        Unknown10000(250)
        MinimumDamagePct(31)
    Unknown19(0, 2, 52)
    gotoLabel(99)
    label(0)
    clearUponHandler(24)
    clearUponHandler(25)
    sprite('ha430_15', 4)	# 62-65
    GFX_1('haef_DD_1_ring', 0)
    physicsXImpulse(5000)
    sprite('ha430_16', 2)	# 66-67
    SFX_0('006_swing_blade_2')
    sprite('ha430_16', 2)	# 68-69
    sprite('ha430_17', 4)	# 70-73
    tag_voice(0, 'bha251_0', 'bha251_1', '', '')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('011_spin_0')
    sprite('ha430_18', 4)	# 74-77	 **attackbox here**
    GFX_0('ha430_col_dmy_OD', 100)
    SFX_3('hase_20')
    ScreenShake(0, 16000)
    GFX_1('haef_DD_1_blast', 0)
    Unknown2015(200)
    physicsXImpulse(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21007(9, 32)
        clearUponHandler(10)

    def upon_78():
        SLOT_56 = 1
        if SLOT_56:
            Unknown13024(0)
            Unknown9310(1)
            sendToLabel(1)
            setInvincible(1)
            Unknown11069('UltimateAssault_DamyAtk')
        clearUponHandler(78)

    def upon_43():
        if (SLOT_48 == 1000):
            pass
    GFX_0('ha_DD_1_shotSP', 0)
    Unknown38(9, 1)
    sprite('ha430_19', 5)	# 78-82
    setInvincible(0)
    sprite('ha430_20', 5)	# 83-87
    sprite('ha430_21', 5)	# 88-92
    sprite('ha430_22', 5)	# 93-97
    sprite('ha430_23', 5)	# 98-102
    Unknown14077(1)
    Unknown2015(-1)
    sprite('ha430_24', 4)	# 103-106
    sprite('ha430_25', 4)	# 107-110
    sprite('ha430_26', 4)	# 111-114
    sprite('ha430_27', 4)	# 115-118
    ExitState()
    label(1)
    sprite('ha430_18', 5)	# 119-123	 **attackbox here**
    GFX_0('UltimateAssault_DamyAtk', 100)
    sprite('ha430_19', 5)	# 124-128
    sprite('ha430_20', 5)	# 129-133
    sprite('ha430_19', 5)	# 134-138
    sprite('ha430_20', 5)	# 139-143
    sprite('ha430_19', 5)	# 144-148
    sprite('ha430_20', 5)	# 149-153
    label(2)
    sprite('ha430_19', 3)	# 154-156
    sprite('ha430_20', 3)	# 157-159
    sprite('ha430_19', 3)	# 160-162
    sprite('ha430_20', 3)	# 163-165
    sprite('ha430_19', 3)	# 166-168
    sprite('ha430_20', 3)	# 169-171
    sprite('ha430_19', 3)	# 172-174
    sprite('ha430_20', 3)	# 175-177
    sprite('ha430_19', 3)	# 178-180
    sprite('ha430_20', 3)	# 181-183
    sprite('ha430_19', 3)	# 184-186
    sprite('ha430_20', 3)	# 187-189
    sprite('ha430_19', 4)	# 190-193
    sprite('ha430_20', 4)	# 194-197
    sprite('ha430_19', 4)	# 198-201
    sprite('ha430_20', 4)	# 202-205
    sprite('ha430_19', 5)	# 206-210
    sprite('ha430_20', 5)	# 211-215
    sprite('ha430_19', 6)	# 216-221
    sprite('ha430_20', 6)	# 222-227
    sprite('ha430_19', 4)	# 228-231
    sprite('ha430_20', 4)	# 232-235
    sprite('ha430_19', 5)	# 236-240
    sprite('ha430_20', 5)	# 241-245
    sprite('ha430_19', 6)	# 246-251
    sprite('ha430_20', 6)	# 252-257
    sprite('ha430_19', 6)	# 258-263
    sprite('ha430_20', 5)	# 264-268
    sprite('ha430_21', 5)	# 269-273
    sprite('ha430_22', 5)	# 274-278
    sprite('ha430_23', 5)	# 279-283
    Unknown14077(1)
    Unknown2015(-1)
    sprite('ha430_24', 4)	# 284-287
    sprite('ha430_25', 4)	# 288-291
    Unknown13024(1)
    sprite('ha430_26', 4)	# 292-295
    sprite('ha430_27', 4)	# 296-299

@State
def UltimateGrip():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)
        Unknown1051(30)

        def upon_42():
            Unknown23022(1)
            enterState('UltimateGrip2')
        setInvincible(1)
        GuardPoint_(1)
        Unknown22026(1)
        Unknown22031(4, 48)
    sprite('ha203_00ex', 4)	# 1-4
    SFX_3('hase_21')
    SFX_3('hase_21')
    GFX_0('ha_DD_2_ex', 0)
    ConsumeSuperMeter(-10000)
    ScreenShake(12000, 0)
    sprite('ha203_01ex', 4)	# 5-8
    sprite('ha203_02ex', 4)	# 9-12
    sprite('ha203_17ex', 5)	# 13-17
    sprite('ha203_18ex', 5)	# 18-22
    sprite('ha203_19ex', 5)	# 23-27
    sprite('ha203_20ex', 3)	# 28-30
    setInvincible(0)
    sprite('ha203_21', 6)	# 31-36
    sprite('ha203_22', 4)	# 37-40
    sprite('ha203_22', 4)	# 41-44

@State
def UltimateGrip2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(6000)
        AttackP2(60)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5000)
        AirPushbackY(45000)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(10, 30, 35)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30048(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown23072()
        setInvincible(1)

        def upon_78():
            sendToLabel(0)
    sprite('keep', 20)	# 1-20
    Unknown2036(36, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    tag_voice(1, 'bha252_0', 'bha252_1', '', '')
    ScreenShake(0, 16000)
    Unknown8004(100, 1, 1)
    sprite('ha431_00', 4)	# 21-24
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 4)	# 25-28
    sprite('ha431_02', 4)	# 29-32
    sprite('ha431_03', 4)	# 33-36
    sprite('ha431_04', 4)	# 37-40
    sprite('ha431_05', 4)	# 41-44
    sprite('ha431_06', 4)	# 45-48
    sprite('ha431_07', 4)	# 49-52
    sprite('ha431_08', 3)	# 53-55
    sprite('ha431_09', 3)	# 56-58
    sprite('ha431_10', 3)	# 59-61
    sprite('ha431_11', 3)	# 62-64
    sprite('ha431_12', 3)	# 65-67
    sprite('ha431_13', 3)	# 68-70
    sprite('ha431_14', 3)	# 71-73
    sprite('ha431_15', 3)	# 74-76
    sprite('ha431_16', 3)	# 77-79	 **attackbox here**
    StartMultihit()
    tag_voice(0, 'bha253_0', 'bha253_1', '', '')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(1696000)
    sprite('ha431_16', 12)	# 80-91	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ha431_16', 30)	# 92-121	 **attackbox here**
    StartMultihit()
    clearUponHandler(78)
    loopRest()
    label(9)
    sprite('ha431_17', 4)	# 122-125
    sprite('ha431_18', 4)	# 126-129
    sprite('ha431_19', 4)	# 130-133
    sprite('ha431_20', 4)	# 134-137
    sprite('ha431_21', 4)	# 138-141
    sprite('ha431_22', 4)	# 142-145
    sprite('ha431_23', 4)	# 146-149
    sprite('ha431_24', 4)	# 150-153
    sprite('ha431_25', 4)	# 154-157
    sprite('ha431_26', 4)	# 158-161
    sprite('ha431_27', 4)	# 162-165
    sprite('ha431_28', 4)	# 166-169
    Unknown14077(1)
    sprite('ha431_29', 3)	# 170-172
    sprite('ha000_00', 1)	# 173-173
    Unknown2005()

@State
def UltimateGrip_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown11063(1)
        Unknown1051(30)

        def upon_42():
            Unknown23022(1)
            enterState('UltimateGrip2_OD')
        setInvincible(1)
        GuardPoint_(1)
        Unknown22026(1)
        Unknown22031(4, 48)
    sprite('ha203_00ex', 4)	# 1-4
    SFX_3('hase_21')
    SFX_3('hase_21')
    GFX_0('ha_DD_2_ex', 0)
    ConsumeSuperMeter(-10000)
    ScreenShake(12000, 0)
    sprite('ha203_01ex', 4)	# 5-8
    sprite('ha203_02ex', 4)	# 9-12
    sprite('ha203_17ex', 5)	# 13-17
    sprite('ha203_18ex', 5)	# 18-22
    sprite('ha203_19ex', 5)	# 23-27
    sprite('ha203_20ex', 3)	# 28-30
    setInvincible(0)
    sprite('ha203_21', 6)	# 31-36
    sprite('ha203_22', 4)	# 37-40
    sprite('ha203_22', 4)	# 41-44

@State
def UltimateGrip2_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2500)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(5000)
        AirPushbackY(45000)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(30, 70, 75)
        Unknown11084(1)
        Unknown11066(1)
        Unknown30048(1)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11057(0)
        Unknown9016(1)
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown11064(1)
        Unknown23072()
        Unknown11069('UltimateGrip2_OD')
        Unknown13024(0)
        setInvincible(1)

        def upon_78():
            sendToLabel(0)
    sprite('keep', 20)	# 1-20
    Unknown2036(36, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    tag_voice(1, 'bha252_0', 'bha252_1', '', '')
    ScreenShake(0, 16000)
    Unknown8004(100, 1, 1)
    sprite('ha431_00', 4)	# 21-24
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 4)	# 25-28
    sprite('ha431_02', 4)	# 29-32
    sprite('ha431_03', 4)	# 33-36
    sprite('ha431_04', 4)	# 37-40
    sprite('ha431_05', 4)	# 41-44
    sprite('ha431_06', 4)	# 45-48
    sprite('ha431_07', 4)	# 49-52
    sprite('ha431_08', 3)	# 53-55
    sprite('ha431_09', 3)	# 56-58
    sprite('ha431_10', 3)	# 59-61
    sprite('ha431_11', 3)	# 62-64
    sprite('ha431_12', 3)	# 65-67
    sprite('ha431_13', 3)	# 68-70
    sprite('ha431_14', 3)	# 71-73
    sprite('ha431_15', 3)	# 74-76
    sprite('ha431_16', 3)	# 77-79	 **attackbox here**
    StartMultihit()
    tag_voice(0, 'bha253_0', 'bha253_1', '', '')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(1696000)
    sprite('ha431_16', 12)	# 80-91	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('ha431_16', 60)	# 92-151	 **attackbox here**
    StartMultihit()
    clearUponHandler(78)
    AttackLevel_(1)
    Damage(100)
    Hitstop(1)
    Unknown11057(700)
    Unknown11023(1)
    SLOT_52 = 4
    label(1)
    sprite('ha431_16', 1)	# 152-152	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    Unknown4045('686165665f44445f32000000000000000000000000000000000000000000000000000000')
    Unknown4053(-40000, 40000)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    ScreenShake(0, 16000)
    sprite('ha431_16', 1)	# 153-153	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    sprite('ha431_16', 1)	# 154-154	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    sprite('ha431_16', 1)	# 155-155	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    SLOT_52 = (SLOT_52 + (-1))
    Unknown19(2, 2, 52)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ha431_16', 1)	# 156-156	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    sprite('ha431_16', 1)	# 157-157	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(40)
    sprite('ha431_16', 1)	# 158-158	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AttackLevel_(5)
    Damage(5000)
    AttackP2(60)
    Hitstop(30)
    Unknown11001(0, 0, 0)
    Unknown11057(1000)
    Unknown11064(0)
    Unknown11069('')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 32000)

    def upon_78():
        Unknown13024(1)
        Unknown14077(1)
        clearUponHandler(78)
    loopRest()
    label(9)
    sprite('ha431_17', 4)	# 159-162
    sprite('ha431_18', 4)	# 163-166
    sprite('ha431_19', 4)	# 167-170
    sprite('ha431_20', 4)	# 171-174
    sprite('ha431_21', 4)	# 175-178
    sprite('ha431_22', 4)	# 179-182
    sprite('ha431_23', 4)	# 183-186
    sprite('ha431_24', 4)	# 187-190
    sprite('ha431_25', 4)	# 191-194
    sprite('ha431_26', 4)	# 195-198
    sprite('ha431_27', 4)	# 199-202
    sprite('ha431_28', 4)	# 203-206
    Unknown14077(1)
    sprite('ha431_29', 3)	# 207-209
    sprite('ha000_00', 1)	# 210-210
    Unknown2005()

@State
def UltimateAirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5600)
        MinimumDamagePct(31)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(24)
        AirPushbackX(14000)
        AirPushbackY(-100000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(40)
        Unknown9310(1)
        AirUntechableTime(90)
        Unknown9016(1)
        Unknown11056(0)
        Unknown11001(20, 0, 0)
        setInvincible(1)
        Unknown1084(1)
        clearUponHandler(2)
    sprite('ha440_08', 4)	# 1-4
    Unknown1084(1)
    physicsYImpulse(3500)
    setGravity(100)
    sendToLabelUpon(2, 1)
    sprite('ha440_08', 35)	# 5-39
    Unknown2036(35, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    tag_voice(1, 'bha280_0', 'bha280_1', '', '')
    sprite('ha440_09', 2)	# 40-41
    sprite('ha440_10', 2)	# 42-43
    sprite('ha440_11', 3)	# 44-46
    setGravity(30000)
    GFX_1('haef_440fall', 103)
    SFX_3('hase_24')
    sprite('ha440_12', 3)	# 47-49
    sprite('ha440_11', 3)	# 50-52
    sprite('ha440_12', 3)	# 53-55
    sprite('ha440_11', 3)	# 56-58
    sprite('ha440_12', 60)	# 59-118
    label(1)
    sprite('ha440_13', 3)	# 119-121	 **attackbox here**
    GFX_1('haef_440clash', -1)
    clearUponHandler(2)
    clearUponHandler(12)
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(4)
    Unknown3070(10)
    SFX_0('025_cleanhit_slash')
    ScreenShake(50000, 100000)

    def upon_78():
        sendToLabel(2)
    sprite('ha440_14', 3)	# 122-124
    setInvincible(0)
    DisableAttackRestOfMove()
    Unknown2003(1)
    sprite('ha440_15', 3)	# 125-127
    sprite('ha440_13', 3)	# 128-130	 **attackbox here**
    sprite('ha440_14', 3)	# 131-133
    sprite('ha440_15', 3)	# 134-136
    sprite('ha440_13', 3)	# 137-139	 **attackbox here**
    sprite('ha440_14', 3)	# 140-142
    sprite('ha440_15', 3)	# 143-145
    gotoLabel(10)
    label(2)
    sprite('ha440_14', 3)	# 146-148
    setInvincible(0)
    DisableAttackRestOfMove()
    Unknown2003(1)
    sprite('ha440_15', 3)	# 149-151
    sprite('ha440_13', 3)	# 152-154	 **attackbox here**
    sprite('ha440_14', 3)	# 155-157
    sprite('ha440_15', 3)	# 158-160
    sprite('ha440_13', 3)	# 161-163	 **attackbox here**
    sprite('ha440_14', 3)	# 164-166
    sprite('ha440_15', 3)	# 167-169
    sprite('ha440_13', 3)	# 170-172	 **attackbox here**
    sprite('ha440_14', 3)	# 173-175
    sprite('ha440_15', 3)	# 176-178
    sprite('ha440_13', 3)	# 179-181	 **attackbox here**
    sprite('ha440_14', 3)	# 182-184
    tag_voice(0, 'bha281_0', 'bha281_1', '', '')
    sprite('ha440_15', 3)	# 185-187
    sprite('ha440_13', 3)	# 188-190	 **attackbox here**
    sprite('ha440_14', 3)	# 191-193
    sprite('ha440_15', 3)	# 194-196
    sprite('ha440_13', 3)	# 197-199	 **attackbox here**
    sprite('ha440_14', 3)	# 200-202
    sprite('ha440_15', 3)	# 203-205
    sprite('ha440_13', 3)	# 206-208	 **attackbox here**
    gotoLabel(10)
    label(10)
    sprite('ha430_23', 6)	# 209-214
    sprite('ha430_24', 6)	# 215-220
    sprite('ha430_25', 6)	# 221-226
    sprite('ha430_26', 6)	# 227-232
    sprite('ha430_27', 6)	# 233-238

@State
def UltimateAirAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(6600)
        MinimumDamagePct(30)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(54)
        AirPushbackX(14000)
        AirPushbackY(-100000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(40)
        AirUntechableTime(90)
        Unknown9310(12)
        Unknown9016(1)
        Unknown11056(0)
        Unknown11001(20, 0, 0)
        setInvincible(1)
        Unknown1084(1)
        clearUponHandler(2)
    sprite('ha440_08', 4)	# 1-4
    Unknown1084(1)
    physicsYImpulse(3500)
    setGravity(100)
    sendToLabelUpon(2, 1)
    sprite('ha440_08', 35)	# 5-39
    Unknown2036(35, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    tag_voice(1, 'bha280_0', 'bha280_1', '', '')
    sprite('ha440_09', 2)	# 40-41
    sprite('ha440_10', 2)	# 42-43
    sprite('ha440_11', 3)	# 44-46
    setGravity(30000)
    GFX_1('haef_440fall', 103)
    SFX_3('hase_24')
    sprite('ha440_12', 3)	# 47-49
    sprite('ha440_11', 3)	# 50-52
    sprite('ha440_12', 3)	# 53-55
    sprite('ha440_11', 3)	# 56-58
    sprite('ha440_12', 60)	# 59-118
    label(1)
    sprite('ha440_13', 3)	# 119-121	 **attackbox here**
    Unknown4049(1380)
    Unknown4045('686165665f343430636c61736800000000000000000000000000000000000000ffffffff')
    clearUponHandler(2)
    clearUponHandler(12)
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(4)
    Unknown3070(10)
    SFX_0('025_cleanhit_slash')
    ScreenShake(150000, 150000)

    def upon_78():
        sendToLabel(2)
    sprite('ha440_14', 3)	# 122-124
    setInvincible(0)
    DisableAttackRestOfMove()
    Unknown2003(1)
    sprite('ha440_15', 3)	# 125-127
    sprite('ha440_13', 3)	# 128-130	 **attackbox here**
    sprite('ha440_14', 3)	# 131-133
    sprite('ha440_15', 3)	# 134-136
    sprite('ha440_13', 3)	# 137-139	 **attackbox here**
    sprite('ha440_14', 3)	# 140-142
    sprite('ha440_15', 3)	# 143-145
    gotoLabel(10)
    label(2)
    sprite('ha440_14', 3)	# 146-148
    setInvincible(0)
    DisableAttackRestOfMove()
    Unknown2003(1)
    sprite('ha440_15', 3)	# 149-151
    sprite('ha440_13', 3)	# 152-154	 **attackbox here**
    sprite('ha440_14', 3)	# 155-157
    sprite('ha440_15', 3)	# 158-160
    sprite('ha440_13', 3)	# 161-163	 **attackbox here**
    sprite('ha440_14', 3)	# 164-166
    sprite('ha440_15', 3)	# 167-169
    sprite('ha440_13', 3)	# 170-172	 **attackbox here**
    sprite('ha440_14', 3)	# 173-175
    sprite('ha440_15', 3)	# 176-178
    sprite('ha440_13', 3)	# 179-181	 **attackbox here**
    sprite('ha440_14', 3)	# 182-184
    tag_voice(0, 'bha281_0', 'bha281_1', '', '')
    sprite('ha440_15', 3)	# 185-187
    sprite('ha440_13', 3)	# 188-190	 **attackbox here**
    sprite('ha440_14', 3)	# 191-193
    sprite('ha440_15', 3)	# 194-196
    sprite('ha440_13', 3)	# 197-199	 **attackbox here**
    sprite('ha440_14', 3)	# 200-202
    sprite('ha440_15', 3)	# 203-205
    gotoLabel(10)
    label(10)
    sprite('ha430_23', 6)	# 206-211
    sprite('ha430_24', 6)	# 212-217
    sprite('ha430_25', 6)	# 218-223
    sprite('ha430_26', 6)	# 224-229
    sprite('ha430_27', 6)	# 230-235

@State
def AstralHeatGrip():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11063(1)
        setInvincible(1)
        Unknown2003(1)
        Unknown2004(1, 0)
        Damage(0)
        Unknown11057(0)
        Hitstop(0)
        Unknown11001(1800, 1800, 1800)
        hitstun(600)
        Unknown11058('0100000001000000010000000000000001000000')
        HitOverhead(4)
        HitLow(4)
        HitAirUnblockable(4)
        Unknown11084(1)
        PushbackX(0)
        AirPushbackX(0)
        AirPushbackY(0)
        Unknown11085(1)
        Unknown11042(1)
        Unknown11107(1)

        def upon_STATE_END():
            SLOT_80 = 0

        def upon_12():
            Unknown11083(1)
            enterState('AstralHeatGrip2')
    sprite('ha451_00', 4)	# 1-4
    Unknown2036(60, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_HA_AH', -1)
    sprite('ha451_01', 4)	# 5-8
    sprite('ha451_02', 4)	# 9-12
    sprite('ha451_03', 4)	# 13-16	 **attackbox here**
    sprite('ha451_04', 4)	# 17-20	 **attackbox here**
    GFX_1('haef_AH_2', 0)
    SFX_4('bha290')
    sprite('ha451_05', 4)	# 21-24	 **attackbox here**
    sprite('ha451_03', 4)	# 25-28	 **attackbox here**
    sprite('ha451_04', 4)	# 29-32	 **attackbox here**
    sprite('ha451_05', 4)	# 33-36	 **attackbox here**
    sprite('ha451_03', 4)	# 37-40	 **attackbox here**
    sprite('ha451_04', 4)	# 41-44	 **attackbox here**
    sprite('ha451_05', 4)	# 45-48	 **attackbox here**
    sprite('ha451_03', 4)	# 49-52	 **attackbox here**
    sprite('ha451_04', 4)	# 53-56	 **attackbox here**
    sprite('ha451_05', 4)	# 57-60	 **attackbox here**
    sprite('ha451_03', 4)	# 61-64	 **attackbox here**
    GuardPoint_(1)
    Unknown22019('0100000001000000010000000000000001000000')
    Unknown22036(0)
    Unknown22031(15, 16)
    Unknown2003(0)

    def upon_42():
        Unknown23022(1)
        sendToLabel(10)
    sprite('ha451_04', 4)	# 65-68	 **attackbox here**
    sprite('ha451_05', 4)	# 69-72	 **attackbox here**
    sprite('ha451_03', 4)	# 73-76	 **attackbox here**
    sprite('ha451_04', 4)	# 77-80	 **attackbox here**
    loopRest()
    gotoLabel(99)
    label(10)
    sprite('ha451_03', 3)	# 81-83	 **attackbox here**
    Unknown2003(0)
    Unknown11107(0)
    Unknown11023(1)
    sprite('ha451_04', 4)	# 84-87	 **attackbox here**
    sprite('ha451_05', 4)	# 88-91	 **attackbox here**
    sprite('ha451_03', 4)	# 92-95	 **attackbox here**
    sprite('ha451_04', 4)	# 96-99	 **attackbox here**
    sprite('ha451_05', 4)	# 100-103	 **attackbox here**
    sprite('ha451_03', 4)	# 104-107	 **attackbox here**
    sprite('ha451_04', 4)	# 108-111	 **attackbox here**
    sprite('ha451_05', 4)	# 112-115	 **attackbox here**
    sprite('ha451_03', 4)	# 116-119	 **attackbox here**
    sprite('ha451_04', 4)	# 120-123	 **attackbox here**
    sprite('ha451_05', 4)	# 124-127	 **attackbox here**
    sprite('ha451_03', 4)	# 128-131	 **attackbox here**
    sprite('ha451_04', 4)	# 132-135	 **attackbox here**
    sprite('ha451_05', 4)	# 136-139	 **attackbox here**
    sprite('ha451_03', 4)	# 140-143	 **attackbox here**
    sprite('ha451_04', 4)	# 144-147	 **attackbox here**
    sprite('ha451_05', 4)	# 148-151	 **attackbox here**
    sprite('ha451_03', 4)	# 152-155	 **attackbox here**
    sprite('ha451_04', 4)	# 156-159	 **attackbox here**
    sprite('ha451_05', 4)	# 160-163	 **attackbox here**
    sprite('ha451_03', 4)	# 164-167	 **attackbox here**
    sprite('ha451_04', 4)	# 168-171	 **attackbox here**
    sprite('ha451_05', 4)	# 172-175	 **attackbox here**
    sprite('ha451_03', 4)	# 176-179	 **attackbox here**
    sprite('ha451_04', 4)	# 180-183	 **attackbox here**
    sprite('ha451_05', 4)	# 184-187	 **attackbox here**
    sprite('ha451_03', 4)	# 188-191	 **attackbox here**
    sprite('ha451_04', 4)	# 192-195	 **attackbox here**
    sprite('ha451_05', 4)	# 196-199	 **attackbox here**
    sprite('ha451_03', 4)	# 200-203	 **attackbox here**
    sprite('ha451_04', 4)	# 204-207	 **attackbox here**
    sprite('ha451_05', 4)	# 208-211	 **attackbox here**
    sprite('ha451_03', 4)	# 212-215	 **attackbox here**
    sprite('ha451_04', 4)	# 216-219	 **attackbox here**
    sprite('ha451_05', 4)	# 220-223	 **attackbox here**
    sprite('ha451_03', 4)	# 224-227	 **attackbox here**
    sprite('ha451_04', 4)	# 228-231	 **attackbox here**
    sprite('ha451_05', 4)	# 232-235	 **attackbox here**
    sprite('ha451_03', 4)	# 236-239	 **attackbox here**
    sprite('ha451_04', 4)	# 240-243	 **attackbox here**
    sprite('ha451_05', 4)	# 244-247	 **attackbox here**
    sprite('ha451_03', 4)	# 248-251	 **attackbox here**
    sprite('ha451_04', 4)	# 252-255	 **attackbox here**
    sprite('ha451_05', 4)	# 256-259	 **attackbox here**
    sprite('ha451_03', 4)	# 260-263	 **attackbox here**
    sprite('ha451_04', 4)	# 264-267	 **attackbox here**
    sprite('ha451_05', 4)	# 268-271	 **attackbox here**
    sprite('ha451_03', 4)	# 272-275	 **attackbox here**
    sprite('ha451_04', 4)	# 276-279	 **attackbox here**
    sprite('ha451_05', 4)	# 280-283	 **attackbox here**
    sprite('ha451_03', 4)	# 284-287	 **attackbox here**
    sprite('ha451_04', 4)	# 288-291	 **attackbox here**
    sprite('ha451_05', 4)	# 292-295	 **attackbox here**
    sprite('ha451_03', 4)	# 296-299	 **attackbox here**
    sprite('ha451_04', 4)	# 300-303	 **attackbox here**
    sprite('ha451_05', 4)	# 304-307	 **attackbox here**
    loopRest()
    label(99)
    sprite('ha451_03', 4)	# 308-311	 **attackbox here**
    setInvincible(0)
    Unknown23022(0)
    Unknown2003(1)
    Unknown11023(0)
    sprite('ha451_02', 4)	# 312-315
    sprite('ha451_01', 4)	# 316-319
    sprite('ha451_00', 3)	# 320-322
    sprite('ha451_00', 1)	# 323-323
    SFX_3('hase_22')

@State
def AstralHeatGrip2():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)
        Unknown23084(1)
        Unknown3029(1)
        Unknown3069(4)
        Unknown3071(6)
        Unknown3074('00000000ff000000ff000000ff000000')
        Unknown3075('0000000000000000ff000000ff000000')
        Unknown3076(1000)
        Unknown3077(1150)
        Unknown23088(1, 1)
        Unknown23157(1)
        Unknown23025(1)
        Unknown11067(1)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20004(1)
        Unknown20006(1)
    sprite('ha451_05', 1)	# 1-1	 **attackbox here**
    StartMultihit()
    Unknown3026(-16777216)
    GFX_0('HaAstBG_Start', -1)
    sprite('ha451_05', 24)	# 2-25	 **attackbox here**
    StartMultihit()
    Unknown36(22)
    Unknown3026(-16777216)
    Unknown35()
    sprite('ha451_06', 3)	# 26-28
    sprite('ha451_07', 3)	# 29-31
    sprite('ha451_08', 3)	# 32-34
    sprite('ha451_09', 3)	# 35-37
    sprite('ha451_10', 3)	# 38-40
    SFX_0('006_swing_blade_1')
    sprite('ha451_11', 3)	# 41-43
    sprite('ha451_12', 3)	# 44-46
    sprite('ha451_13', 3)	# 47-49
    sprite('ha451_14', 3)	# 50-52
    sprite('ha451_15', 3)	# 53-55
    sprite('ha451_16', 3)	# 56-58
    sprite('ha451_17', 3)	# 59-61
    sprite('ha451_18', 3)	# 62-64
    sprite('ha451_19', 3)	# 65-67
    sprite('ha451_20', 3)	# 68-70
    sprite('ha451_21', 220)	# 71-290
    GFX_1('haef_AH_enemy_drop', 104)
    GFX_0('ha_AH_fude', -1)
    SFX_0('015_blaze_2')
    SFX_0('015_blaze_1')
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_4('bha291')
    sprite('ha451_21', 1)	# 291-291
    GFX_0('ha_451_finish', -1)
    sprite('ha451_22', 120)	# 292-411
    Unknown3029(0)
    Unknown3025(-1, 120)
    Unknown36(22)
    Unknown3026(-1)
    Unknown35()
    sprite('ha451_23', 8)	# 412-419
    GFX_0('HaAstBG_Finish', -1)
    sprite('ha451_24', 8)	# 420-427
    sprite('ha451_25', 8)	# 428-435
    sprite('ha451_26', 8)	# 436-443
    sprite('ha451_27', 8)	# 444-451
    sprite('ha451_28', 6)	# 452-457
    sprite('ha451_29', 6)	# 458-463
    sprite('ha451_30', 6)	# 464-469
    sprite('ha451_31', 6)	# 470-475
    sprite('ha451_32', 30)	# 476-505
    sprite('ha451_33', 2)	# 506-507
    sprite('ha451_34', 15)	# 508-522
    SFX_3('hase_00')
    sprite('ha451_35', 5)	# 523-527
    sprite('ha451_36', 5)	# 528-532
    sprite('ha451_37', 5)	# 533-537
    sprite('ha451_38', 5)	# 538-542
    sprite('ha451_39', 5)	# 543-547
    sprite('ha451_40', 5)	# 548-552
    sprite('ha451_41', 5)	# 553-557
    sprite('ha451_42', 5)	# 558-562
    sprite('ha451_39', 5)	# 563-567
    sprite('ha451_40', 5)	# 568-572
    sprite('ha451_41', 5)	# 573-577
    sprite('ha451_42', 5)	# 578-582
    sprite('ha451_39', 5)	# 583-587
    sprite('ha451_40', 5)	# 588-592
    sprite('ha451_41', 5)	# 593-597
    sprite('ha451_42', 5)	# 598-602
    sprite('ha451_39', 5)	# 603-607
    sprite('ha451_40', 5)	# 608-612
    sprite('ha451_41', 5)	# 613-617
    sprite('ha451_42', 5)	# 618-622
    sprite('ha451_39', 5)	# 623-627
    sprite('ha451_40', 5)	# 628-632
    sprite('ha451_41', 5)	# 633-637
    sprite('ha451_42', 5)	# 638-642
    loopRest()
    random_(1, 2, 87)
    Unknown19(50, 2, 0)
    sprite('ha451_39', 5)	# 643-647
    sprite('ha451_40', 5)	# 648-652
    sprite('ha451_41', 5)	# 653-657
    sprite('ha451_42', 5)	# 658-662
    loopRest()
    Unknown18010()
    Unknown21011(60)
    sprite('ha451_39', 4)	# 663-666
    sprite('ha451_40', 4)	# 667-670
    sprite('ha451_41', 4)	# 671-674
    sprite('ha451_42', 4)	# 675-678
    label(51)
    sprite('ha451_39', 4)	# 679-682
    sprite('ha451_40', 4)	# 683-686
    sprite('ha451_41', 4)	# 687-690
    sprite('ha451_42', 4)	# 691-694
    loopRest()
    gotoLabel(51)
    ExitState()
    label(50)
    sprite('ha451_43', 5)	# 695-699
    Unknown2004(1, 0)
    Unknown2005()
    sprite('ha451_44', 5)	# 700-704
    setInvincible(0)
    sprite('ha451_45', 5)	# 705-709
    sprite('ha451_46', 5)	# 710-714
    sprite('ha451_47', 5)	# 715-719
    sprite('ha000_00', 1)	# 720-720
    teleportRelativeX(-158000)
    Unknown2005()

@Subroutine
def MouthTableInit():
    Unknown18011('bha000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha500', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13409, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha500', '001')
    Unknown18011('bha501', 12643, 14177, 14179, 13921, 25399, 24887, 14131, 14179, 14689, 25399, 24887, 14137, 14179, 13409, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha501', '002')
    Unknown18011('bha502', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 14689, 25399, 24887, 14137, 14179, 13409, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha502', '003')
    Unknown18011('bha503', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13921, 25399, 24887, 14133, 14179, 24931, 14130, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha503', '004')
    Unknown18011('bha504', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13409, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha504', '005')
    Unknown18011('bha505', 12643, 14177, 14179, 13921, 25399, 24887, 14132, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha505', '006')
    Unknown18011('bha520', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13153, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha520', '007')
    Unknown18011('bha521', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13409, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha521', '008')
    Unknown18011('bha522', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13921, 25399, 24887, 14134, 14179, 24931, 14129, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha522', '009')
    Unknown18011('bha523', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13409, 25399, 24887, 14131, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha523', '010')
    Unknown18011('bha524', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13409, 25399, 24887, 14129, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha524', '011')
    Unknown18011('bha525', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13409, 25399, 24887, 14131, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha525', '012')
    Unknown18011('bha402_0', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha402_1', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha403_0', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha403_1', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600brc', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 14689, 25399, 24887, 14137, 14179, 13665, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600brg', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13665, 25399, 24887, 14133, 14179, 13665, 25399, 24887, 25399, 24887, 25399, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600btg', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13153, 25399, 24887, 14133, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600pak', 12643, 14177, 14179, 14689, 25399, 24887, 14137, 14179, 13921, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600rwi', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13921, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600ume', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 14689, 25399, 24887, 14137, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600uyu', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 12897, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha601bes', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 14177, 14179, 13153, 25399, 24887, 14133, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha601biz', 12643, 14177, 14179, 14689, 25399, 24887, 14137, 14179, 13921, 25399, 24887, 14131, 14179, 12897, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha601pbc', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13665, 25399, 24887, 14133, 14179, 13153, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha601uli', 12643, 14177, 14179, 14689, 25399, 24887, 14137, 14179, 13921, 25399, 24887, 14131, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha602uyu', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha603', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13921, 25399, 24887, 14134, 14179, 13921, 25399, 14134, 13921, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha600bsu', 12643, 13153, 12340, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha602bsu', 12643, 12641, 12336, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha604bsu', 12643, 14177, 25392, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha601pad', 12643, 12897, 12337, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha600brc', '017')
    Unknown30092('bha600brg', '018')
    Unknown30092('bha600btg', '019')
    Unknown30092('bha600pak', '020')
    Unknown30092('bha600rwi', '021')
    Unknown30092('bha600ume', '022')
    Unknown30092('bha600uyu', '023')
    Unknown30092('bha601bes', '024')
    Unknown30092('bha601biz', '025')
    Unknown30092('bha601pbc', '026')
    Unknown30092('bha601uli', '027')
    Unknown30092('bha602uyu', '028')
    Unknown30092('bha603', '029')
    Unknown30092('bha600bsu', '030')
    Unknown30092('bha602bsu', '031')
    Unknown30092('bha604bsu', '032')
    Unknown30092('bha601pad', '033')
    Unknown18011('bha700biz', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13153, 25399, 24887, 14131, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700brg', 12643, 14177, 14179, 14689, 25399, 24887, 14137, 14179, 13921, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700btg', 12643, 14177, 14179, 14689, 25399, 24887, 14137, 14179, 13921, 25399, 24887, 14130, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700rwi', 12643, 14177, 14179, 14689, 25399, 24887, 25399, 24887, 25399, 24887, 14130, 14179, 13409, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700uli', 12643, 14177, 14179, 13921, 25399, 24887, 14134, 14179, 13921, 25399, 24887, 14131, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700uyu', 12643, 14177, 14179, 13153, 25399, 24887, 25399, 24887, 14134, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha701bes', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13921, 25399, 24887, 14134, 14179, 13921, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha701brc', 12643, 14177, 14179, 13665, 25399, 24887, 14133, 14179, 13665, 25399, 24887, 25399, 24887, 12851, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha701pak', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13153, 25399, 24887, 14133, 14179, 12641, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha701pbc', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13921, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha701ume', 12643, 14177, 14179, 13153, 25399, 24887, 14131, 14179, 13665, 25399, 24887, 14133, 14179, 13153, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700bsu', 12643, 12897, 12344, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bha700pad', 12643, 12641, 12337, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bha700biz', '034')
    Unknown30092('bha700brg', '035')
    Unknown30092('bha700btg', '036')
    Unknown30092('bha700rwi', '037')
    Unknown30092('bha700uli', '038')
    Unknown30092('bha700uyu', '039')
    Unknown30092('bha701bes', '040')
    Unknown30092('bha701brc', '041')
    Unknown30092('bha701pak', '042')
    Unknown30092('bha701pbc', '043')
    Unknown30092('bha701ume', '044')
    Unknown30092('bha700bsu', '045')
    Unknown30092('bha700pad', '046')
    if SLOT_172:
        Unknown18011('bha000', 13923, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24882, 25393, 13874, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha501', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha502', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 13618, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha503', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12595, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha504', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha505', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 12897, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 14642, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha521', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13411, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 13618, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha522', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 13106, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha523', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 24884, 25399, 24887, 25399, 25394, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha524', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 13107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha525', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12899, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha402_0', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha402_1', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha403_0', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha403_1', 12643, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600brc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600brg', 12643, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600btg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 12641, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600pak', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 13107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600rwi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600ume', 12643, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600uyu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha601bes', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 24882, 25395, 13107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha601biz', 12643, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha601pbc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha601uli', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 12641, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 14386, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha602uyu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 12897, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha603', 12643, 13409, 13874, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha600bsu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24881, 25393, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha602bsu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13155, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha604bsu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha601pad', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700biz', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 12850, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700brg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700btg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700rwi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700uli', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 14386, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700uyu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha701bes', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 13107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha701brc', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 13362, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha701pak', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 12851, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha701pbc', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha701ume', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700bsu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bha700pad', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('62706800000000000000000000000000626a62000000000000000000000000006268610000000000000000000000000062707400000000000000000000000000'):
        SLOT_171 = 1
    if SLOT_169:
        _gotolabel(482)
    if SLOT_122:
        _gotolabel(482)
    if SLOT_123:
        _gotolabel(482)
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    if SLOT_171:
        _gotolabel(1000)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('brc')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('btg')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bes')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('uli')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('rwi')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('uyu')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('biz')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('pak')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('ume')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('bsu')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('pad')
    if SLOT_ReturnVal:
        _gotolabel(220)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('ha600_00', 7)	# 2-8
    sprite('ha600_01', 7)	# 9-15
    sprite('ha600_00', 7)	# 16-22
    sprite('ha600_01', 7)	# 23-29
    sprite('ha600_00', 7)	# 30-36
    Unknown7006('bha500', 100, 895576162, 12592, 0, 0, 100, 895576162, 13360, 0, 0, 100, 895576162, 13104, 0, 0, 0)
    sprite('ha600_01', 7)	# 37-43
    sprite('ha600_00', 7)	# 44-50
    sprite('ha600_01', 7)	# 51-57
    sprite('ha600_00', 7)	# 58-64
    sprite('ha600_01', 7)	# 65-71
    sprite('ha600_00', 7)	# 72-78
    sprite('ha600_01', 7)	# 79-85
    sprite('ha600_00', 7)	# 86-92
    sprite('ha600_01', 7)	# 93-99
    sprite('ha600_00', 7)	# 100-106
    sprite('ha600_01', 7)	# 107-113
    sprite('ha600_02', 7)	# 114-120
    sprite('ha600_03', 7)	# 121-127
    sprite('ha600_04', 7)	# 128-134
    sprite('ha600_05', 7)	# 135-141
    sprite('ha600_06', 7)	# 142-148
    sprite('ha600_07', 7)	# 149-155
    sprite('ha600_08', 6)	# 156-161
    sprite('ha600_09', 6)	# 162-167
    sprite('ha600_10', 6)	# 168-173
    sprite('ha600_11', 6)	# 174-179
    sprite('ha600_12', 6)	# 180-185
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 6)	# 186-191
    sprite('ha600_14', 6)	# 192-197
    sprite('ha600_15', 6)	# 198-203
    sprite('ha600_16', 6)	# 204-209
    sprite('ha600_17', 6)	# 210-215
    sprite('ha600_18', 6)	# 216-221
    sprite('ha600_19', 6)	# 222-227
    Unknown23018(1)
    sprite('ha600_20', 6)	# 228-233
    sprite('ha600_21', 6)	# 234-239
    sprite('ha600_22', 6)	# 240-245
    label(1)
    sprite('ha000_00', 7)	# 246-252
    sprite('ha000_01', 7)	# 253-259
    sprite('ha000_02', 7)	# 260-266
    sprite('ha000_03', 7)	# 267-273
    sprite('ha000_04', 7)	# 274-280
    sprite('ha000_05', 7)	# 281-287
    sprite('ha000_06', 7)	# 288-294
    sprite('ha000_07', 7)	# 295-301
    sprite('ha000_08', 7)	# 302-308
    sprite('ha000_09', 7)	# 309-315
    sprite('ha000_10', 7)	# 316-322
    sprite('ha000_11', 7)	# 323-329
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ha601_00', 6)	# 330-335
    sprite('ha601_01', 6)	# 336-341
    sprite('ha601_02', 6)	# 342-347
    sprite('ha601_03', 6)	# 348-353
    sprite('ha601_00', 6)	# 354-359
    Unknown7006('bha502', 100, 895576162, 13104, 0, 0, 100, 895576162, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ha601_01', 6)	# 360-365
    sprite('ha601_02', 6)	# 366-371
    sprite('ha601_03', 6)	# 372-377
    sprite('ha601_00', 6)	# 378-383
    sprite('ha601_01', 6)	# 384-389
    sprite('ha601_02', 6)	# 390-395
    sprite('ha601_03', 6)	# 396-401
    sprite('ha601_01', 6)	# 402-407
    sprite('ha601_02', 6)	# 408-413
    sprite('ha601_03', 6)	# 414-419
    sprite('ha601_00', 6)	# 420-425
    sprite('ha601_01', 6)	# 426-431
    sprite('ha601_02', 6)	# 432-437
    sprite('ha601_03', 6)	# 438-443
    sprite('ha601_00', 6)	# 444-449
    sprite('ha601_01', 6)	# 450-455
    sprite('ha601_02', 6)	# 456-461
    sprite('ha601_03', 6)	# 462-467
    sprite('ha601_00', 6)	# 468-473
    sprite('ha601_01', 6)	# 474-479
    sprite('ha601_02', 6)	# 480-485
    sprite('ha601_03', 6)	# 486-491
    sprite('ha601_04', 6)	# 492-497
    sprite('ha601_05', 6)	# 498-503
    sprite('ha601_06', 6)	# 504-509
    sprite('ha601_07', 6)	# 510-515
    sprite('ha601_08', 6)	# 516-521
    sprite('ha601_09', 6)	# 522-527
    sprite('ha601_10', 6)	# 528-533
    sprite('ha601_11', 6)	# 534-539
    sprite('ha601_12', 6)	# 540-545
    sprite('ha601_13', 7)	# 546-552
    sprite('ha601_14', 7)	# 553-559
    sprite('ha601_15', 7)	# 560-566
    sprite('ha601_16', 7)	# 567-573
    sprite('ha601_17', 7)	# 574-580
    sprite('ha601_18', 7)	# 581-587
    sprite('ha601_19', 7)	# 588-594
    sprite('ha601_20', 7)	# 595-601
    sprite('ha601_21', 7)	# 602-608
    sprite('ha601_22', 7)	# 609-615
    Unknown23018(1)
    label(11)
    sprite('ha000_00', 7)	# 616-622
    sprite('ha000_01', 7)	# 623-629
    sprite('ha000_02', 7)	# 630-636
    sprite('ha000_03', 7)	# 637-643
    sprite('ha000_04', 7)	# 644-650
    sprite('ha000_05', 7)	# 651-657
    sprite('ha000_06', 7)	# 658-664
    sprite('ha000_07', 7)	# 665-671
    sprite('ha000_08', 7)	# 672-678
    sprite('ha000_09', 7)	# 679-685
    sprite('ha000_10', 7)	# 686-692
    sprite('ha000_11', 7)	# 693-699
    gotoLabel(11)
    ExitState()
    label(100)
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ha600_23', 7)	# 700-706
    sprite('ha600_24', 7)	# 707-713
    sprite('ha600_25', 7)	# 714-720
    sprite('ha600_26', 7)	# 721-727
    SFX_1('bha600brg')
    sprite('ha600_27', 7)	# 728-734
    sprite('ha600_28', 7)	# 735-741
    sprite('ha600_23', 7)	# 742-748
    sprite('ha600_24', 7)	# 749-755
    sprite('ha600_25', 7)	# 756-762
    sprite('ha600_26', 7)	# 763-769
    sprite('ha600_27', 7)	# 770-776
    sprite('ha600_28', 7)	# 777-783
    sprite('ha600_29', 8)	# 784-791
    sprite('ha600_30', 8)	# 792-799
    sprite('ha600_00', 8)	# 800-807
    sprite('ha600_01', 8)	# 808-815
    sprite('ha600_02', 8)	# 816-823
    sprite('ha600_03', 8)	# 824-831
    sprite('ha600_04', 8)	# 832-839
    sprite('ha600_05', 8)	# 840-847
    sprite('ha600_06', 8)	# 848-855
    sprite('ha600_07', 8)	# 856-863
    sprite('ha600_08', 5)	# 864-868
    sprite('ha600_09', 5)	# 869-873
    sprite('ha600_10', 5)	# 874-878
    sprite('ha600_11', 5)	# 879-883
    sprite('ha600_12', 5)	# 884-888
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 5)	# 889-893
    sprite('ha600_14', 5)	# 894-898
    sprite('ha600_15', 5)	# 899-903
    sprite('ha600_16', 5)	# 904-908
    sprite('ha600_17', 5)	# 909-913
    sprite('ha600_18', 5)	# 914-918
    sprite('ha600_19', 5)	# 919-923
    sprite('ha600_20', 5)	# 924-928
    sprite('ha600_21', 5)	# 929-933
    sprite('ha600_22', 5)	# 934-938
    label(101)
    sprite('ha000_00', 7)	# 939-945
    sprite('ha000_01', 7)	# 946-952
    sprite('ha000_02', 7)	# 953-959
    sprite('ha000_03', 7)	# 960-966
    sprite('ha000_04', 7)	# 967-973
    sprite('ha000_05', 7)	# 974-980
    sprite('ha000_06', 7)	# 981-987
    sprite('ha000_07', 7)	# 988-994
    sprite('ha000_08', 7)	# 995-1001
    sprite('ha000_09', 7)	# 1002-1008
    sprite('ha000_10', 7)	# 1009-1015
    sprite('ha000_11', 7)	# 1016-1022
    if SLOT_97:
        _gotolabel(101)
    sprite('ha000_00', 7)	# 1023-1029
    sprite('ha000_01', 7)	# 1030-1036
    sprite('ha000_02', 7)	# 1037-1043
    sprite('ha000_03', 7)	# 1044-1050
    sprite('ha000_04', 7)	# 1051-1057
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('ha000_05', 7)	# 1058-1064
    sprite('ha000_06', 7)	# 1065-1071
    sprite('ha000_07', 7)	# 1072-1078
    sprite('ha000_08', 7)	# 1079-1085
    sprite('ha000_09', 7)	# 1086-1092
    sprite('ha000_10', 7)	# 1093-1099
    sprite('ha000_11', 7)	# 1100-1106
    label(102)
    sprite('ha000_00', 7)	# 1107-1113
    sprite('ha000_01', 7)	# 1114-1120
    sprite('ha000_02', 7)	# 1121-1127
    sprite('ha000_03', 7)	# 1128-1134
    sprite('ha000_04', 7)	# 1135-1141
    sprite('ha000_05', 7)	# 1142-1148
    sprite('ha000_06', 7)	# 1149-1155
    sprite('ha000_07', 7)	# 1156-1162
    sprite('ha000_08', 7)	# 1163-1169
    sprite('ha000_09', 7)	# 1170-1176
    sprite('ha000_10', 7)	# 1177-1183
    sprite('ha000_11', 7)	# 1184-1190
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('ha600_23', 7)	# 1191-1197
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ha600_24', 7)	# 1198-1204
    sprite('ha600_25', 7)	# 1205-1211
    sprite('ha600_26', 7)	# 1212-1218
    SFX_1('bha600brc')
    sprite('ha600_27', 7)	# 1219-1225
    sprite('ha600_28', 7)	# 1226-1232
    sprite('ha600_23', 7)	# 1233-1239
    sprite('ha600_24', 7)	# 1240-1246
    sprite('ha600_25', 7)	# 1247-1253
    sprite('ha600_26', 7)	# 1254-1260
    sprite('ha600_27', 7)	# 1261-1267
    sprite('ha600_28', 7)	# 1268-1274
    sprite('ha600_28', 7)	# 1275-1281
    sprite('ha600_29', 8)	# 1282-1289
    sprite('ha600_30', 8)	# 1290-1297
    sprite('ha600_00', 8)	# 1298-1305
    sprite('ha600_01', 8)	# 1306-1313
    sprite('ha600_02', 8)	# 1314-1321
    sprite('ha600_03', 8)	# 1322-1329
    sprite('ha600_04', 8)	# 1330-1337
    sprite('ha600_05', 8)	# 1338-1345
    sprite('ha600_06', 8)	# 1346-1353
    sprite('ha600_07', 8)	# 1354-1361
    sprite('ha600_08', 5)	# 1362-1366
    sprite('ha600_09', 5)	# 1367-1371
    sprite('ha600_10', 5)	# 1372-1376
    sprite('ha600_11', 5)	# 1377-1381
    sprite('ha600_12', 5)	# 1382-1386
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 5)	# 1387-1391
    sprite('ha600_14', 5)	# 1392-1396
    sprite('ha600_15', 5)	# 1397-1401
    sprite('ha600_16', 5)	# 1402-1406
    sprite('ha600_17', 5)	# 1407-1411
    sprite('ha600_18', 5)	# 1412-1416
    sprite('ha600_19', 5)	# 1417-1421
    sprite('ha600_20', 5)	# 1422-1426
    sprite('ha600_21', 5)	# 1427-1431
    sprite('ha600_22', 5)	# 1432-1436
    label(111)
    sprite('ha000_00', 7)	# 1437-1443
    sprite('ha000_01', 7)	# 1444-1450
    sprite('ha000_02', 7)	# 1451-1457
    sprite('ha000_03', 7)	# 1458-1464
    sprite('ha000_04', 7)	# 1465-1471
    sprite('ha000_05', 7)	# 1472-1478
    sprite('ha000_06', 7)	# 1479-1485
    sprite('ha000_07', 7)	# 1486-1492
    sprite('ha000_08', 7)	# 1493-1499
    sprite('ha000_09', 7)	# 1500-1506
    sprite('ha000_10', 7)	# 1507-1513
    sprite('ha000_11', 7)	# 1514-1520
    if SLOT_97:
        _gotolabel(111)
    sprite('ha000_00', 1)	# 1521-1521
    Unknown21007(24, 40)
    Unknown21011(240)
    label(112)
    sprite('ha000_00', 7)	# 1522-1528
    sprite('ha000_01', 7)	# 1529-1535
    sprite('ha000_02', 7)	# 1536-1542
    sprite('ha000_03', 7)	# 1543-1549
    sprite('ha000_04', 7)	# 1550-1556
    sprite('ha000_05', 7)	# 1557-1563
    sprite('ha000_06', 7)	# 1564-1570
    sprite('ha000_07', 7)	# 1571-1577
    sprite('ha000_08', 7)	# 1578-1584
    sprite('ha000_09', 7)	# 1585-1591
    sprite('ha000_10', 7)	# 1592-1598
    sprite('ha000_11', 7)	# 1599-1605
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('ha601_00', 1)	# 1606-1606
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1515000)
    sprite('ha601_00', 6)	# 1607-1612
    sprite('ha601_01', 6)	# 1613-1618
    sprite('ha601_02', 6)	# 1619-1624
    SFX_1('bha600btg')
    sprite('ha601_03', 6)	# 1625-1630
    label(121)
    sprite('ha601_00', 6)	# 1631-1636
    sprite('ha601_01', 6)	# 1637-1642
    sprite('ha601_02', 6)	# 1643-1648
    sprite('ha601_03', 6)	# 1649-1654
    if SLOT_97:
        _gotolabel(121)
    sprite('ha601_04', 6)	# 1655-1660
    sprite('ha601_05', 6)	# 1661-1666
    sprite('ha601_06', 6)	# 1667-1672
    sprite('ha601_07', 6)	# 1673-1678
    sprite('ha601_08', 6)	# 1679-1684
    sprite('ha601_09', 6)	# 1685-1690
    sprite('ha601_10', 6)	# 1691-1696
    sprite('ha601_11', 6)	# 1697-1702
    sprite('ha601_12', 6)	# 1703-1708
    sprite('ha601_13', 7)	# 1709-1715
    sprite('ha601_14', 7)	# 1716-1722
    sprite('ha601_15', 7)	# 1723-1729
    sprite('ha601_16', 7)	# 1730-1736
    sprite('ha601_17', 7)	# 1737-1743
    sprite('ha601_18', 7)	# 1744-1750
    sprite('ha601_19', 7)	# 1751-1757
    sprite('ha601_20', 7)	# 1758-1764
    sprite('ha601_21', 7)	# 1765-1771
    sprite('ha601_22', 7)	# 1772-1778
    Unknown21007(24, 40)
    sprite('ha000_00', 1)	# 1779-1779
    Unknown21011(180)
    label(122)
    sprite('ha000_00', 7)	# 1780-1786
    sprite('ha000_01', 7)	# 1787-1793
    sprite('ha000_02', 7)	# 1794-1800
    sprite('ha000_03', 7)	# 1801-1807
    sprite('ha000_04', 7)	# 1808-1814
    sprite('ha000_05', 7)	# 1815-1821
    sprite('ha000_06', 7)	# 1822-1828
    sprite('ha000_07', 7)	# 1829-1835
    sprite('ha000_08', 7)	# 1836-1842
    sprite('ha000_09', 7)	# 1843-1849
    sprite('ha000_10', 7)	# 1850-1856
    sprite('ha000_11', 7)	# 1857-1863
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('ha601_00', 1)	# 1864-1864
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1515000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ha601_00', 6)	# 1865-1870
    sprite('ha601_01', 6)	# 1871-1876
    sprite('ha601_02', 6)	# 1877-1882
    sprite('ha601_03', 6)	# 1883-1888
    gotoLabel(131)
    label(132)
    sprite('ha601_00', 6)	# 1889-1894
    SFX_1('bha601bes')
    sprite('ha601_01', 6)	# 1895-1900
    sprite('ha601_02', 6)	# 1901-1906
    sprite('ha601_03', 6)	# 1907-1912
    sprite('ha601_00', 6)	# 1913-1918
    sprite('ha601_01', 6)	# 1919-1924
    sprite('ha601_02', 6)	# 1925-1930
    sprite('ha601_03', 6)	# 1931-1936
    sprite('ha601_04', 6)	# 1937-1942
    sprite('ha601_05', 6)	# 1943-1948
    sprite('ha601_06', 6)	# 1949-1954
    sprite('ha601_07', 6)	# 1955-1960
    sprite('ha601_08', 6)	# 1961-1966
    sprite('ha601_09', 6)	# 1967-1972
    sprite('ha601_10', 6)	# 1973-1978
    sprite('ha601_11', 6)	# 1979-1984
    sprite('ha601_12', 6)	# 1985-1990
    sprite('ha601_13', 7)	# 1991-1997
    sprite('ha601_14', 7)	# 1998-2004
    sprite('ha601_15', 7)	# 2005-2011
    sprite('ha601_16', 7)	# 2012-2018
    sprite('ha601_17', 7)	# 2019-2025
    sprite('ha601_18', 7)	# 2026-2032
    sprite('ha601_19', 7)	# 2033-2039
    sprite('ha601_20', 7)	# 2040-2046
    sprite('ha601_21', 7)	# 2047-2053
    sprite('ha601_22', 7)	# 2054-2060
    Unknown23018(1)
    label(133)
    sprite('ha000_00', 7)	# 2061-2067
    sprite('ha000_01', 7)	# 2068-2074
    sprite('ha000_02', 7)	# 2075-2081
    sprite('ha000_03', 7)	# 2082-2088
    sprite('ha000_04', 7)	# 2089-2095
    sprite('ha000_05', 7)	# 2096-2102
    sprite('ha000_06', 7)	# 2103-2109
    sprite('ha000_07', 7)	# 2110-2116
    sprite('ha000_08', 7)	# 2117-2123
    sprite('ha000_09', 7)	# 2124-2130
    sprite('ha000_10', 7)	# 2131-2137
    sprite('ha000_11', 7)	# 2138-2144
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('ha600_00', 1)	# 2145-2145
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ha600_00', 7)	# 2146-2152
    sprite('ha600_01', 7)	# 2153-2159
    gotoLabel(141)
    label(142)
    sprite('ha600_02', 7)	# 2160-2166
    SFX_1('bha601pbc')
    sprite('ha600_03', 7)	# 2167-2173
    sprite('ha600_04', 7)	# 2174-2180
    sprite('ha600_05', 7)	# 2181-2187
    sprite('ha600_06', 7)	# 2188-2194
    sprite('ha600_07', 7)	# 2195-2201
    sprite('ha600_08', 6)	# 2202-2207
    sprite('ha600_09', 6)	# 2208-2213
    sprite('ha600_10', 6)	# 2214-2219
    sprite('ha600_11', 6)	# 2220-2225
    sprite('ha600_12', 6)	# 2226-2231
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 6)	# 2232-2237
    sprite('ha600_14', 6)	# 2238-2243
    sprite('ha600_15', 6)	# 2244-2249
    sprite('ha600_16', 6)	# 2250-2255
    sprite('ha600_17', 6)	# 2256-2261
    sprite('ha600_18', 6)	# 2262-2267
    sprite('ha600_19', 6)	# 2268-2273
    sprite('ha600_20', 6)	# 2274-2279
    sprite('ha600_21', 6)	# 2280-2285
    sprite('ha600_22', 6)	# 2286-2291
    Unknown23018(1)
    label(143)
    sprite('ha000_00', 7)	# 2292-2298
    sprite('ha000_01', 7)	# 2299-2305
    sprite('ha000_02', 7)	# 2306-2312
    sprite('ha000_03', 7)	# 2313-2319
    sprite('ha000_04', 7)	# 2320-2326
    sprite('ha000_05', 7)	# 2327-2333
    sprite('ha000_06', 7)	# 2334-2340
    sprite('ha000_07', 7)	# 2341-2347
    sprite('ha000_08', 7)	# 2348-2354
    sprite('ha000_09', 7)	# 2355-2361
    sprite('ha000_10', 7)	# 2362-2368
    sprite('ha000_11', 7)	# 2369-2375
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('ha000_00', 1)	# 2376-2376
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ha000_00', 7)	# 2377-2383
    sprite('ha000_01', 7)	# 2384-2390
    sprite('ha000_02', 7)	# 2391-2397
    sprite('ha000_03', 7)	# 2398-2404
    sprite('ha000_04', 7)	# 2405-2411
    sprite('ha000_05', 7)	# 2412-2418
    sprite('ha000_06', 7)	# 2419-2425
    sprite('ha000_07', 7)	# 2426-2432
    sprite('ha000_08', 7)	# 2433-2439
    sprite('ha000_09', 7)	# 2440-2446
    sprite('ha000_10', 7)	# 2447-2453
    sprite('ha000_11', 7)	# 2454-2460
    gotoLabel(151)
    label(152)
    sprite('ha450_00', 8)	# 2461-2468
    sprite('ha450_01', 8)	# 2469-2476
    SFX_1('bha601uli')
    sprite('ha450_02', 8)	# 2477-2484
    sprite('ha450_03', 8)	# 2485-2492
    sprite('ha450_04', 10)	# 2493-2502
    label(153)
    sprite('ha450_05', 1)	# 2503-2503
    if SLOT_97:
        _gotolabel(153)
    sprite('ha450_05', 20)	# 2504-2523
    sprite('ha450_18', 4)	# 2524-2527
    sprite('ha450_19', 5)	# 2528-2532
    sprite('ha450_20', 5)	# 2533-2537
    sprite('ha450_21', 5)	# 2538-2542
    sprite('ha450_22', 5)	# 2543-2547
    sprite('ha450_23', 5)	# 2548-2552
    Unknown23018(1)
    label(154)
    sprite('ha000_00', 7)	# 2553-2559
    sprite('ha000_01', 7)	# 2560-2566
    sprite('ha000_02', 7)	# 2567-2573
    sprite('ha000_03', 7)	# 2574-2580
    sprite('ha000_04', 7)	# 2581-2587
    sprite('ha000_05', 7)	# 2588-2594
    sprite('ha000_06', 7)	# 2595-2601
    sprite('ha000_07', 7)	# 2602-2608
    sprite('ha000_08', 7)	# 2609-2615
    sprite('ha000_09', 7)	# 2616-2622
    sprite('ha000_10', 7)	# 2623-2629
    sprite('ha000_11', 7)	# 2630-2636
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('ha300_00', 1)	# 2637-2637
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1505000)
    sprite('ha300_00', 6)	# 2638-2643
    SFX_1('bha600rwi')
    sprite('ha300_01', 6)	# 2644-2649
    sprite('ha300_02', 6)	# 2650-2655
    sprite('ha300_03', 6)	# 2656-2661
    sprite('ha300_04', 6)	# 2662-2667
    sprite('ha300_05', 6)	# 2668-2673
    sprite('ha300_06', 6)	# 2674-2679
    sprite('ha300_07', 6)	# 2680-2685
    sprite('ha300_08', 6)	# 2686-2691
    label(161)
    sprite('ha300_09', 1)	# 2692-2692
    if SLOT_97:
        _gotolabel(161)
    sprite('ha300_10', 8)	# 2693-2700
    sprite('ha300_11', 8)	# 2701-2708
    sprite('ha300_12', 8)	# 2709-2716
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('ha000_00', 7)	# 2717-2723
    sprite('ha000_01', 7)	# 2724-2730
    sprite('ha000_02', 7)	# 2731-2737
    sprite('ha000_03', 7)	# 2738-2744
    sprite('ha000_04', 7)	# 2745-2751
    sprite('ha000_05', 7)	# 2752-2758
    sprite('ha000_06', 7)	# 2759-2765
    sprite('ha000_07', 7)	# 2766-2772
    sprite('ha000_08', 7)	# 2773-2779
    sprite('ha000_09', 7)	# 2780-2786
    sprite('ha000_10', 7)	# 2787-2793
    sprite('ha000_11', 7)	# 2794-2800
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('ha450_00', 1)	# 2801-2801
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    sprite('ha450_00', 3)	# 2802-2804
    sprite('ha450_01', 3)	# 2805-2807
    SFX_1('bha600uyu')
    sprite('ha450_02', 3)	# 2808-2810
    label(171)
    sprite('ha450_03', 1)	# 2811-2811
    if SLOT_97:
        _gotolabel(171)
    sprite('ha450_03', 32767)	# 2812-35578
    Unknown21007(24, 40)
    label(172)
    sprite('ha450_07', 4)	# 35579-35582
    Unknown21007(24, 39)
    SFX_1('bha602uyu')
    sprite('ha450_08', 4)	# 35583-35586
    sprite('ha450_09', 4)	# 35587-35590
    sprite('ha450_10', 4)	# 35591-35594
    sprite('ha450_11', 4)	# 35595-35598
    sprite('ha450_12', 4)	# 35599-35602
    sprite('ha450_13', 4)	# 35603-35606
    sprite('ha450_14', 4)	# 35607-35610
    sprite('ha450_15', 4)	# 35611-35614
    sprite('ha450_16', 4)	# 35615-35618
    sprite('ha450_17', 4)	# 35619-35622
    sprite('ha450_18', 40)	# 35623-35662
    sprite('ha450_20', 4)	# 35663-35666
    sprite('ha450_21', 4)	# 35667-35670
    sprite('ha450_22', 4)	# 35671-35674
    sprite('ha450_23', 4)	# 35675-35678
    Unknown23018(1)
    label(173)
    sprite('ha000_00', 7)	# 35679-35685
    sprite('ha000_01', 7)	# 35686-35692
    sprite('ha000_02', 7)	# 35693-35699
    sprite('ha000_03', 7)	# 35700-35706
    sprite('ha000_04', 7)	# 35707-35713
    sprite('ha000_05', 7)	# 35714-35720
    sprite('ha000_06', 7)	# 35721-35727
    sprite('ha000_07', 7)	# 35728-35734
    sprite('ha000_08', 7)	# 35735-35741
    sprite('ha000_09', 7)	# 35742-35748
    sprite('ha000_10', 7)	# 35749-35755
    sprite('ha000_11', 7)	# 35756-35762
    gotoLabel(173)
    ExitState()
    label(180)
    sprite('ha000_00', 1)	# 35763-35763
    if SLOT_158:
        Unknown1000(-1200000)
        Unknown2019(500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ha000_00', 7)	# 35764-35770
    sprite('ha000_01', 7)	# 35771-35777
    sprite('ha000_02', 7)	# 35778-35784
    sprite('ha000_03', 7)	# 35785-35791
    sprite('ha000_04', 7)	# 35792-35798
    sprite('ha000_05', 7)	# 35799-35805
    sprite('ha000_06', 7)	# 35806-35812
    sprite('ha000_07', 7)	# 35813-35819
    sprite('ha000_08', 7)	# 35820-35826
    sprite('ha000_09', 7)	# 35827-35833
    sprite('ha000_10', 7)	# 35834-35840
    sprite('ha000_11', 7)	# 35841-35847
    gotoLabel(181)
    label(182)
    sprite('ha300_00', 6)	# 35848-35853
    SFX_1('bha601biz')
    sprite('ha300_01', 6)	# 35854-35859
    sprite('ha300_02', 6)	# 35860-35865
    sprite('ha300_03', 6)	# 35866-35871
    sprite('ha300_04', 6)	# 35872-35877
    sprite('ha300_05', 6)	# 35878-35883
    sprite('ha300_06', 6)	# 35884-35889
    sprite('ha300_07', 6)	# 35890-35895
    sprite('ha300_08', 6)	# 35896-35901
    label(183)
    sprite('ha300_09', 1)	# 35902-35902
    if SLOT_97:
        _gotolabel(183)
    sprite('ha300_10', 8)	# 35903-35910
    sprite('ha300_11', 8)	# 35911-35918
    sprite('ha300_12', 8)	# 35919-35926
    Unknown23018(1)
    label(184)
    sprite('ha000_00', 7)	# 35927-35933
    sprite('ha000_01', 7)	# 35934-35940
    sprite('ha000_02', 7)	# 35941-35947
    sprite('ha000_03', 7)	# 35948-35954
    sprite('ha000_04', 7)	# 35955-35961
    sprite('ha000_05', 7)	# 35962-35968
    sprite('ha000_06', 7)	# 35969-35975
    sprite('ha000_07', 7)	# 35976-35982
    sprite('ha000_08', 7)	# 35983-35989
    sprite('ha000_09', 7)	# 35990-35996
    sprite('ha000_10', 7)	# 35997-36003
    sprite('ha000_11', 7)	# 36004-36010
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('ha600_23', 7)	# 36011-36017
    if SLOT_158:
        Unknown1000(-1180000)
    else:
        Unknown1000(-1515000)
    sprite('ha600_24', 7)	# 36018-36024
    sprite('ha600_25', 7)	# 36025-36031
    sprite('ha600_26', 7)	# 36032-36038
    SFX_1('bha600pak')
    sprite('ha600_27', 7)	# 36039-36045
    sprite('ha600_28', 7)	# 36046-36052
    sprite('ha600_23', 7)	# 36053-36059
    sprite('ha600_24', 7)	# 36060-36066
    sprite('ha600_25', 7)	# 36067-36073
    sprite('ha600_26', 7)	# 36074-36080
    sprite('ha600_27', 7)	# 36081-36087
    sprite('ha600_28', 7)	# 36088-36094
    sprite('ha600_29', 8)	# 36095-36102
    sprite('ha600_30', 8)	# 36103-36110
    sprite('ha600_00', 8)	# 36111-36118
    sprite('ha600_01', 8)	# 36119-36126
    sprite('ha600_02', 8)	# 36127-36134
    sprite('ha600_03', 8)	# 36135-36142
    sprite('ha600_04', 8)	# 36143-36150
    sprite('ha600_05', 8)	# 36151-36158
    sprite('ha600_06', 8)	# 36159-36166
    sprite('ha600_07', 8)	# 36167-36174
    sprite('ha600_08', 5)	# 36175-36179
    sprite('ha600_09', 5)	# 36180-36184
    sprite('ha600_10', 5)	# 36185-36189
    sprite('ha600_11', 5)	# 36190-36194
    sprite('ha600_12', 5)	# 36195-36199
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 5)	# 36200-36204
    sprite('ha600_14', 5)	# 36205-36209
    sprite('ha600_15', 5)	# 36210-36214
    sprite('ha600_16', 5)	# 36215-36219
    sprite('ha600_17', 5)	# 36220-36224
    sprite('ha600_18', 5)	# 36225-36229
    sprite('ha600_19', 5)	# 36230-36234
    sprite('ha600_20', 5)	# 36235-36239
    sprite('ha600_21', 5)	# 36240-36244
    sprite('ha600_22', 5)	# 36245-36249
    label(191)
    sprite('ha000_00', 7)	# 36250-36256
    sprite('ha000_01', 7)	# 36257-36263
    sprite('ha000_02', 7)	# 36264-36270
    sprite('ha000_03', 7)	# 36271-36277
    sprite('ha000_04', 7)	# 36278-36284
    sprite('ha000_05', 7)	# 36285-36291
    sprite('ha000_06', 7)	# 36292-36298
    sprite('ha000_07', 7)	# 36299-36305
    sprite('ha000_08', 7)	# 36306-36312
    sprite('ha000_09', 7)	# 36313-36319
    sprite('ha000_10', 7)	# 36320-36326
    sprite('ha000_11', 7)	# 36327-36333
    if SLOT_97:
        _gotolabel(191)
    sprite('ha000_00', 7)	# 36334-36340
    sprite('ha000_01', 7)	# 36341-36347
    sprite('ha000_02', 7)	# 36348-36354
    sprite('ha000_03', 7)	# 36355-36361
    sprite('ha000_04', 7)	# 36362-36368
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('ha000_05', 7)	# 36369-36375
    sprite('ha000_06', 7)	# 36376-36382
    sprite('ha000_07', 7)	# 36383-36389
    sprite('ha000_08', 7)	# 36390-36396
    sprite('ha000_09', 7)	# 36397-36403
    sprite('ha000_10', 7)	# 36404-36410
    sprite('ha000_11', 7)	# 36411-36417
    label(192)
    sprite('ha000_00', 7)	# 36418-36424
    sprite('ha000_01', 7)	# 36425-36431
    sprite('ha000_02', 7)	# 36432-36438
    sprite('ha000_03', 7)	# 36439-36445
    sprite('ha000_04', 7)	# 36446-36452
    sprite('ha000_05', 7)	# 36453-36459
    sprite('ha000_06', 7)	# 36460-36466
    sprite('ha000_07', 7)	# 36467-36473
    sprite('ha000_08', 7)	# 36474-36480
    sprite('ha000_09', 7)	# 36481-36487
    sprite('ha000_10', 7)	# 36488-36494
    sprite('ha000_11', 7)	# 36495-36501
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('ha600_00', 7)	# 36502-36508
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ha600_01', 7)	# 36509-36515
    SFX_1('bha600ume')
    sprite('ha600_00', 7)	# 36516-36522
    sprite('ha600_01', 7)	# 36523-36529
    sprite('ha600_00', 7)	# 36530-36536
    sprite('ha600_01', 7)	# 36537-36543
    sprite('ha600_00', 7)	# 36544-36550
    sprite('ha600_01', 7)	# 36551-36557
    sprite('ha600_00', 7)	# 36558-36564
    sprite('ha600_01', 7)	# 36565-36571
    sprite('ha600_00', 7)	# 36572-36578
    sprite('ha600_01', 7)	# 36579-36585
    sprite('ha600_00', 7)	# 36586-36592
    sprite('ha600_01', 7)	# 36593-36599
    sprite('ha600_00', 7)	# 36600-36606
    sprite('ha600_01', 7)	# 36607-36613
    sprite('ha600_02', 7)	# 36614-36620
    sprite('ha600_03', 7)	# 36621-36627
    sprite('ha600_04', 7)	# 36628-36634
    sprite('ha600_05', 7)	# 36635-36641
    sprite('ha600_06', 7)	# 36642-36648
    sprite('ha600_07', 7)	# 36649-36655
    sprite('ha600_08', 6)	# 36656-36661
    sprite('ha600_09', 6)	# 36662-36667
    sprite('ha600_10', 6)	# 36668-36673
    sprite('ha600_11', 6)	# 36674-36679
    sprite('ha600_12', 6)	# 36680-36685
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 6)	# 36686-36691
    sprite('ha600_14', 6)	# 36692-36697
    sprite('ha600_15', 6)	# 36698-36703
    sprite('ha600_16', 6)	# 36704-36709
    sprite('ha600_17', 6)	# 36710-36715
    sprite('ha600_18', 6)	# 36716-36721
    sprite('ha600_19', 6)	# 36722-36727
    sprite('ha600_20', 6)	# 36728-36733
    sprite('ha600_21', 6)	# 36734-36739
    sprite('ha600_22', 6)	# 36740-36745
    Unknown21011(360)
    label(201)
    sprite('ha000_00', 7)	# 36746-36752
    sprite('ha000_01', 7)	# 36753-36759
    sprite('ha000_02', 7)	# 36760-36766
    sprite('ha000_03', 7)	# 36767-36773
    sprite('ha000_04', 7)	# 36774-36780
    sprite('ha000_05', 7)	# 36781-36787
    sprite('ha000_06', 7)	# 36788-36794
    sprite('ha000_07', 7)	# 36795-36801
    sprite('ha000_08', 7)	# 36802-36808
    sprite('ha000_09', 7)	# 36809-36815
    sprite('ha000_10', 7)	# 36816-36822
    Unknown21007(24, 40)
    sprite('ha000_11', 7)	# 36823-36829
    gotoLabel(201)
    ExitState()
    label(210)
    sprite('ha658_00', 5)	# 36830-36834
    Unknown1000(-1230000)
    Unknown2019(-500)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    sprite('ha658_01', 5)	# 36835-36839
    sprite('ha658_02', 5)	# 36840-36844
    sprite('ha658_00', 5)	# 36845-36849
    sprite('ha658_01', 5)	# 36850-36854
    sprite('ha658_02', 5)	# 36855-36859
    sprite('ha658_00', 5)	# 36860-36864
    sprite('ha658_01', 5)	# 36865-36869
    sprite('ha658_02', 5)	# 36870-36874
    sprite('ha658_03', 5)	# 36875-36879
    sprite('ha658_04', 5)	# 36880-36884
    sprite('ha450_01', 5)	# 36885-36889
    SFX_1('bha600bsu')
    sprite('ha450_02', 8)	# 36890-36897
    sprite('ha450_03', 8)	# 36898-36905
    sprite('ha450_04', 10)	# 36906-36915
    label(211)
    sprite('ha450_05', 1)	# 36916-36916
    if SLOT_97:
        _gotolabel(211)
    sprite('ha450_05', 30)	# 36917-36946
    sprite('ha450_05', 32767)	# 36947-69713
    Unknown21007(24, 40)
    label(212)
    sprite('ha450_05', 1)	# 69714-69714
    SFX_1('bha602bsu')

    def upon_40():
        clearUponHandler(40)
        Unknown2037(0)
        sendToLabel(214)
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
    label(213)
    sprite('ha450_05', 6)	# 69715-69720
    ScreenShake(0, 1500)
    SFX_0('019_quake_0')
    gotoLabel(213)
    label(214)
    sprite('ha450_06', 6)	# 69721-69726
    GFX_0('ha_AH', -1)
    ScreenShake(0, 1500)
    SFX_0('019_quake_0')
    sprite('ha450_07', 6)	# 69727-69732
    ScreenShake(0, 1500)
    SFX_0('019_quake_0')
    sprite('ha450_08', 6)	# 69733-69738
    ScreenShake(0, 1500)
    SFX_0('019_quake_0')
    sprite('ha450_09', 2)	# 69739-69740
    ScreenShake(0, 1500)
    SFX_0('019_quake_0')
    sprite('ha450_09', 4)	# 69741-69744
    SFX_1('bha604bsu')
    SFX_0('303_tag_r_blaze')
    sprite('ha450_10', 6)	# 69745-69750
    ScreenShake(1000, 3000)
    SFX_0('019_quake_0')
    sprite('ha450_11', 6)	# 69751-69756
    sprite('ha450_12', 6)	# 69757-69762
    sprite('ha450_13', 6)	# 69763-69768
    sprite('ha450_14', 6)	# 69769-69774
    sprite('ha450_15', 6)	# 69775-69780
    sprite('ha450_16', 6)	# 69781-69786
    sprite('ha450_17', 6)	# 69787-69792
    sprite('ha450_18', 6)	# 69793-69798
    sprite('ha450_19', 32767)	# 69799-102565
    Unknown23018(1)
    label(220)
    sprite('ha600_00', 1)	# 102566-102566
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('ha600_00', 7)	# 102567-102573
    sprite('ha600_01', 7)	# 102574-102580
    gotoLabel(221)
    label(222)
    sprite('ha600_02', 7)	# 102581-102587
    SFX_1('bha601pad')
    sprite('ha600_03', 7)	# 102588-102594
    sprite('ha600_04', 7)	# 102595-102601
    sprite('ha600_05', 7)	# 102602-102608
    sprite('ha600_06', 7)	# 102609-102615
    sprite('ha600_07', 7)	# 102616-102622
    sprite('ha600_08', 6)	# 102623-102628
    sprite('ha600_09', 6)	# 102629-102634
    sprite('ha600_10', 6)	# 102635-102640
    sprite('ha600_11', 6)	# 102641-102646
    sprite('ha600_12', 6)	# 102647-102652
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 6)	# 102653-102658
    sprite('ha600_14', 6)	# 102659-102664
    sprite('ha600_15', 6)	# 102665-102670
    sprite('ha600_16', 6)	# 102671-102676
    sprite('ha600_17', 6)	# 102677-102682
    sprite('ha600_18', 6)	# 102683-102688
    sprite('ha600_19', 6)	# 102689-102694
    sprite('ha600_20', 6)	# 102695-102700
    sprite('ha600_21', 6)	# 102701-102706
    sprite('ha600_22', 6)	# 102707-102712
    Unknown23018(1)
    label(223)
    sprite('ha000_00', 7)	# 102713-102719
    sprite('ha000_01', 7)	# 102720-102726
    sprite('ha000_02', 7)	# 102727-102733
    sprite('ha000_03', 7)	# 102734-102740
    sprite('ha000_04', 7)	# 102741-102747
    sprite('ha000_05', 7)	# 102748-102754
    sprite('ha000_06', 7)	# 102755-102761
    sprite('ha000_07', 7)	# 102762-102768
    sprite('ha000_08', 7)	# 102769-102775
    sprite('ha000_09', 7)	# 102776-102782
    sprite('ha000_10', 7)	# 102783-102789
    sprite('ha000_11', 7)	# 102790-102796
    gotoLabel(223)
    ExitState()
    label(991)
    sprite('ha000_00', 1)	# 102797-102797
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ha000_00', 7)	# 102798-102804
    sprite('ha000_01', 7)	# 102805-102811
    sprite('ha000_02', 7)	# 102812-102818
    sprite('ha000_03', 7)	# 102819-102825
    sprite('ha000_04', 7)	# 102826-102832
    sprite('ha000_05', 7)	# 102833-102839
    sprite('ha000_06', 7)	# 102840-102846
    sprite('ha000_07', 7)	# 102847-102853
    sprite('ha000_08', 7)	# 102854-102860
    sprite('ha000_09', 7)	# 102861-102867
    sprite('ha000_10', 7)	# 102868-102874
    sprite('ha000_11', 7)	# 102875-102881
    gotoLabel(992)
    label(993)
    sprite('ha033_00', 2)	# 102882-102883

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
    sprite('ha033_01', 3)	# 102884-102886
    label(994)
    sprite('ha033_02', 3)	# 102887-102889
    sprite('ha033_01', 3)	# 102890-102892
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 102893-102895
    ExitState()
    label(1000)
    sprite('ha000_00', 7)	# 102896-102902
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 10003):
            clearUponHandler(43)
            sendToLabel(1001)
    sprite('ha000_01', 7)	# 102903-102909
    sprite('ha000_02', 7)	# 102910-102916
    sprite('ha000_03', 7)	# 102917-102923
    sprite('ha000_04', 7)	# 102924-102930
    sprite('ha000_05', 7)	# 102931-102937
    sprite('ha000_06', 7)	# 102938-102944
    sprite('ha000_07', 7)	# 102945-102951
    sprite('ha000_08', 7)	# 102952-102958
    sprite('ha000_09', 7)	# 102959-102965
    sprite('ha000_10', 7)	# 102966-102972
    sprite('ha000_11', 7)	# 102973-102979
    gotoLabel(1000)
    label(1001)
    sprite('ha300_00', 6)	# 102980-102985
    SFX_1('bha603')
    sprite('ha300_01', 6)	# 102986-102991
    sprite('ha300_02', 6)	# 102992-102997
    sprite('ha300_03', 6)	# 102998-103003
    sprite('ha300_04', 6)	# 103004-103009
    sprite('ha300_05', 6)	# 103010-103015
    sprite('ha300_06', 6)	# 103016-103021
    sprite('ha300_07', 6)	# 103022-103027
    sprite('ha300_08', 6)	# 103028-103033
    sprite('ha300_09', 200)	# 103034-103233
    sprite('ha300_10', 8)	# 103234-103241
    sprite('ha300_11', 8)	# 103242-103249
    sprite('ha300_12', 8)	# 103250-103257
    sprite('ha000_00', 7)	# 103258-103264
    sprite('ha000_01', 7)	# 103265-103271
    sprite('ha000_02', 7)	# 103272-103278
    sprite('ha000_03', 7)	# 103279-103285
    sprite('ha000_04', 7)	# 103286-103292
    sprite('ha000_05', 7)	# 103293-103299
    sprite('ha000_06', 7)	# 103300-103306
    sprite('ha000_07', 7)	# 103307-103313
    sprite('ha000_08', 7)	# 103314-103320
    sprite('ha000_09', 7)	# 103321-103327
    sprite('ha000_10', 7)	# 103328-103334
    sprite('ha000_11', 7)	# 103335-103341
    sprite('ha601_22', 7)	# 103342-103348
    Unknown23029(24, 10004, 0)
    Unknown23029(22, 10004, 0)
    Unknown23029(23, 10004, 0)
    sprite('ha601_21', 7)	# 103349-103355
    sprite('ha601_20', 7)	# 103356-103362
    sprite('ha601_19', 7)	# 103363-103369
    sprite('ha601_18', 7)	# 103370-103376
    sprite('ha601_17', 7)	# 103377-103383
    sprite('ha601_16', 7)	# 103384-103390
    sprite('ha601_15', 7)	# 103391-103397
    sprite('ha601_14', 7)	# 103398-103404
    sprite('ha601_15', 7)	# 103405-103411
    sprite('ha601_16', 7)	# 103412-103418
    sprite('ha601_17', 7)	# 103419-103425
    sprite('ha601_18', 7)	# 103426-103432
    sprite('ha601_19', 7)	# 103433-103439
    sprite('ha601_20', 7)	# 103440-103446
    sprite('ha601_21', 7)	# 103447-103453
    sprite('ha601_22', 7)	# 103454-103460
    Unknown23018(1)
    label(1002)
    sprite('ha000_00', 7)	# 103461-103467
    sprite('ha000_01', 7)	# 103468-103474
    sprite('ha000_02', 7)	# 103475-103481
    sprite('ha000_03', 7)	# 103482-103488
    sprite('ha000_04', 7)	# 103489-103495
    sprite('ha000_05', 7)	# 103496-103502
    sprite('ha000_06', 7)	# 103503-103509
    sprite('ha000_07', 7)	# 103510-103516
    sprite('ha000_08', 7)	# 103517-103523
    sprite('ha000_09', 7)	# 103524-103530
    sprite('ha000_10', 7)	# 103531-103537
    sprite('ha000_11', 7)	# 103538-103544
    gotoLabel(1002)

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
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('biz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('ume'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('bsu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('pad'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('ha610_00', 3)	# 4-6
    sprite('ha610_00', 4)	# 7-10
    sprite('ha610_01', 6)	# 11-16
    sprite('ha610_02', 6)	# 17-22
    sprite('ha610_03', 6)	# 23-28
    sprite('ha610_04', 6)	# 29-34
    sprite('ha610_05', 6)	# 35-40
    sprite('ha610_06', 6)	# 41-46
    sprite('ha610_07', 6)	# 47-52
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bha524', 100, 895576162, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bha402_0', 100, 878798946, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bha520', 100, 895576162, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ha610_08', 6)	# 53-58
    sprite('ha610_09', 6)	# 59-64
    sprite('ha610_10', 6)	# 65-70
    sprite('ha610_11', 6)	# 71-76
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 77-82
    Unknown23018(1)
    label(1)
    sprite('ha610_13', 6)	# 83-88
    sprite('ha610_14', 6)	# 89-94
    sprite('ha610_15', 6)	# 95-100
    sprite('ha610_16', 6)	# 101-106
    sprite('ha610_17', 6)	# 107-112
    sprite('ha610_18', 6)	# 113-118
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ha611_00', 1)	# 119-119
    sprite('ha611_00', 5)	# 120-124
    sprite('ha611_01', 6)	# 125-130
    sprite('ha611_02', 6)	# 131-136
    sprite('ha611_03', 6)	# 137-142
    sprite('ha611_04', 6)	# 143-148
    sprite('ha611_05', 7)	# 149-155
    sprite('ha611_06', 7)	# 156-162
    sprite('ha611_07', 7)	# 163-169
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bha524', 100, 895576162, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bha402_0', 100, 878798946, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bha522', 100, 895576162, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ha611_08', 7)	# 170-176
    sprite('ha611_09', 7)	# 177-183
    sprite('ha611_10', 7)	# 184-190
    sprite('ha611_11', 7)	# 191-197
    Unknown23018(1)
    label(11)
    sprite('ha611_12', 8)	# 198-205
    sprite('ha611_13', 8)	# 206-213
    sprite('ha611_14', 8)	# 214-221
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('ha611_00', 1)	# 222-222
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
    sprite('ha611_00', 5)	# 223-227
    sprite('ha611_01', 6)	# 228-233
    sprite('ha611_02', 6)	# 234-239
    sprite('ha611_03', 6)	# 240-245
    sprite('ha611_04', 6)	# 246-251
    sprite('ha611_05', 7)	# 252-258
    sprite('ha611_06', 7)	# 259-265
    sprite('ha611_07', 7)	# 266-272
    SFX_1('bha700brg')
    sprite('ha611_08', 7)	# 273-279
    sprite('ha611_09', 7)	# 280-286
    sprite('ha611_10', 7)	# 287-293
    sprite('ha611_11', 7)	# 294-300
    label(101)
    sprite('ha611_12', 8)	# 301-308
    sprite('ha611_13', 8)	# 309-316
    sprite('ha611_14', 8)	# 317-324
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('ha611_12', 1)	# 325-325
    Unknown21007(24, 40)
    Unknown21011(240)
    label(102)
    sprite('ha611_12', 8)	# 326-333
    sprite('ha611_13', 8)	# 334-341
    sprite('ha611_14', 8)	# 342-349
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('ha000_00', 1)	# 350-350

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ha000_00', 7)	# 351-357
    sprite('ha000_01', 7)	# 358-364
    sprite('ha000_02', 7)	# 365-371
    sprite('ha000_03', 7)	# 372-378
    sprite('ha000_04', 7)	# 379-385
    sprite('ha000_05', 7)	# 386-392
    sprite('ha000_06', 7)	# 393-399
    sprite('ha000_07', 7)	# 400-406
    sprite('ha000_08', 7)	# 407-413
    sprite('ha000_09', 7)	# 414-420
    sprite('ha000_10', 7)	# 421-427
    sprite('ha000_11', 7)	# 428-434
    gotoLabel(111)
    label(112)
    sprite('ha611_00', 1)	# 435-435
    sprite('ha611_00', 5)	# 436-440
    sprite('ha611_01', 6)	# 441-446
    sprite('ha611_02', 6)	# 447-452
    sprite('ha611_03', 6)	# 453-458
    sprite('ha611_04', 6)	# 459-464
    sprite('ha611_05', 7)	# 465-471
    sprite('ha611_06', 7)	# 472-478
    sprite('ha611_07', 7)	# 479-485
    SFX_1('bha701brc')
    sprite('ha611_08', 7)	# 486-492
    sprite('ha611_09', 7)	# 493-499
    sprite('ha611_10', 7)	# 500-506
    sprite('ha611_11', 7)	# 507-513
    Unknown23018(1)
    label(113)
    sprite('ha611_12', 8)	# 514-521
    sprite('ha611_13', 8)	# 522-529
    sprite('ha611_14', 8)	# 530-537
    loopRest()
    gotoLabel(113)
    label(120)
    sprite('ha610_00', 3)	# 538-540
    sprite('ha610_00', 4)	# 541-544
    sprite('ha610_01', 6)	# 545-550
    sprite('ha610_02', 6)	# 551-556
    sprite('ha610_03', 6)	# 557-562
    sprite('ha610_04', 6)	# 563-568
    sprite('ha610_05', 6)	# 569-574
    sprite('ha610_06', 6)	# 575-580
    sprite('ha610_07', 6)	# 581-586
    SFX_1('bha700btg')
    sprite('ha610_08', 6)	# 587-592
    sprite('ha610_09', 6)	# 593-598
    sprite('ha610_10', 6)	# 599-604
    sprite('ha610_11', 6)	# 605-610
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 611-616
    Unknown2037(6)
    label(121)
    sprite('ha610_13', 6)	# 617-622
    sprite('ha610_14', 6)	# 623-628
    sprite('ha610_15', 6)	# 629-634
    sprite('ha610_16', 6)	# 635-640
    sprite('ha610_17', 6)	# 641-646
    if (not SLOT_2):
        Unknown21007(24, 40)
        Unknown21011(240)
    sprite('ha610_18', 6)	# 647-652
    Unknown2038(-1)
    loopRest()
    gotoLabel(121)
    sprite('ha610_13', 1)	# 653-653
    label(130)
    sprite('ha000_00', 1)	# 654-654

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ha000_00', 7)	# 655-661
    sprite('ha000_01', 7)	# 662-668
    sprite('ha000_02', 7)	# 669-675
    sprite('ha000_03', 7)	# 676-682
    sprite('ha000_04', 7)	# 683-689
    sprite('ha000_05', 7)	# 690-696
    sprite('ha000_06', 7)	# 697-703
    sprite('ha000_07', 7)	# 704-710
    sprite('ha000_08', 7)	# 711-717
    sprite('ha000_09', 7)	# 718-724
    sprite('ha000_10', 7)	# 725-731
    sprite('ha000_11', 7)	# 732-738
    gotoLabel(131)
    label(132)
    sprite('ha610_00', 3)	# 739-741
    sprite('ha610_00', 4)	# 742-745
    sprite('ha610_01', 6)	# 746-751
    sprite('ha610_02', 6)	# 752-757
    sprite('ha610_03', 6)	# 758-763
    sprite('ha610_04', 6)	# 764-769
    sprite('ha610_05', 6)	# 770-775
    sprite('ha610_06', 6)	# 776-781
    sprite('ha610_07', 6)	# 782-787
    SFX_1('bha701bes')
    sprite('ha610_08', 6)	# 788-793
    sprite('ha610_09', 6)	# 794-799
    sprite('ha610_10', 6)	# 800-805
    sprite('ha610_11', 6)	# 806-811
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 812-817
    Unknown23018(1)
    label(133)
    sprite('ha610_13', 6)	# 818-823
    sprite('ha610_14', 6)	# 824-829
    sprite('ha610_15', 6)	# 830-835
    sprite('ha610_16', 6)	# 836-841
    sprite('ha610_17', 6)	# 842-847
    sprite('ha610_18', 6)	# 848-853
    loopRest()
    gotoLabel(133)
    label(140)
    sprite('ha000_00', 1)	# 854-854

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ha000_00', 7)	# 855-861
    sprite('ha000_01', 7)	# 862-868
    sprite('ha000_02', 7)	# 869-875
    sprite('ha000_03', 7)	# 876-882
    sprite('ha000_04', 7)	# 883-889
    sprite('ha000_05', 7)	# 890-896
    sprite('ha000_06', 7)	# 897-903
    sprite('ha000_07', 7)	# 904-910
    sprite('ha000_08', 7)	# 911-917
    sprite('ha000_09', 7)	# 918-924
    sprite('ha000_10', 7)	# 925-931
    sprite('ha000_11', 7)	# 932-938
    gotoLabel(141)
    label(142)
    sprite('ha611_00', 1)	# 939-939
    sprite('ha611_00', 5)	# 940-944
    sprite('ha611_01', 6)	# 945-950
    sprite('ha611_02', 6)	# 951-956
    sprite('ha611_03', 6)	# 957-962
    sprite('ha611_04', 6)	# 963-968
    sprite('ha611_05', 7)	# 969-975
    sprite('ha611_06', 7)	# 976-982
    sprite('ha611_07', 7)	# 983-989
    SFX_1('bha701pbc')
    sprite('ha611_08', 7)	# 990-996
    sprite('ha611_09', 7)	# 997-1003
    sprite('ha611_10', 7)	# 1004-1010
    sprite('ha611_11', 7)	# 1011-1017
    Unknown23018(1)
    label(143)
    sprite('ha611_12', 8)	# 1018-1025
    sprite('ha611_13', 8)	# 1026-1033
    sprite('ha611_14', 8)	# 1034-1041
    loopRest()
    gotoLabel(143)
    label(150)
    sprite('ha611_00', 1)	# 1042-1042
    sprite('ha611_00', 5)	# 1043-1047
    sprite('ha611_01', 6)	# 1048-1053
    sprite('ha611_02', 6)	# 1054-1059
    sprite('ha611_03', 6)	# 1060-1065
    sprite('ha611_04', 6)	# 1066-1071
    sprite('ha611_05', 7)	# 1072-1078
    sprite('ha611_06', 7)	# 1079-1085
    sprite('ha611_07', 7)	# 1086-1092
    SFX_1('bha700uli')
    sprite('ha611_08', 7)	# 1093-1099
    sprite('ha611_09', 7)	# 1100-1106
    sprite('ha611_10', 7)	# 1107-1113
    sprite('ha611_11', 7)	# 1114-1120
    label(151)
    sprite('ha611_12', 8)	# 1121-1128
    sprite('ha611_13', 8)	# 1129-1136
    sprite('ha611_14', 8)	# 1137-1144
    loopRest()
    if SLOT_97:
        _gotolabel(151)
    sprite('ha611_12', 1)	# 1145-1145
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('ha611_12', 8)	# 1146-1153
    sprite('ha611_13', 8)	# 1154-1161
    sprite('ha611_14', 8)	# 1162-1169
    loopRest()
    gotoLabel(152)
    label(160)
    sprite('ha610_00', 3)	# 1170-1172
    sprite('ha610_00', 4)	# 1173-1176
    sprite('ha610_01', 6)	# 1177-1182
    sprite('ha610_02', 6)	# 1183-1188
    sprite('ha610_03', 6)	# 1189-1194
    sprite('ha610_04', 6)	# 1195-1200
    sprite('ha610_05', 6)	# 1201-1206
    sprite('ha610_06', 6)	# 1207-1212
    sprite('ha610_07', 6)	# 1213-1218
    SFX_1('bha700rwi')
    sprite('ha610_08', 6)	# 1219-1224
    sprite('ha610_09', 6)	# 1225-1230
    sprite('ha610_10', 6)	# 1231-1236
    sprite('ha610_11', 6)	# 1237-1242
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 1243-1248
    label(161)
    sprite('ha610_13', 6)	# 1249-1254
    sprite('ha610_14', 6)	# 1255-1260
    sprite('ha610_15', 6)	# 1261-1266
    sprite('ha610_16', 6)	# 1267-1272
    sprite('ha610_17', 6)	# 1273-1278
    sprite('ha610_18', 6)	# 1279-1284
    loopRest()
    if SLOT_97:
        _gotolabel(161)
    sprite('ha610_13', 1)	# 1285-1285
    Unknown21007(24, 40)
    Unknown21011(240)
    label(162)
    sprite('ha610_13', 6)	# 1286-1291
    sprite('ha610_14', 6)	# 1292-1297
    sprite('ha610_15', 6)	# 1298-1303
    sprite('ha610_16', 6)	# 1304-1309
    sprite('ha610_17', 6)	# 1310-1315
    sprite('ha610_18', 6)	# 1316-1321
    loopRest()
    gotoLabel(162)
    label(170)
    sprite('ha611_00', 1)	# 1322-1322
    sprite('ha611_00', 5)	# 1323-1327
    sprite('ha611_01', 6)	# 1328-1333
    sprite('ha611_02', 6)	# 1334-1339
    sprite('ha611_03', 6)	# 1340-1345
    sprite('ha611_04', 6)	# 1346-1351
    sprite('ha611_05', 7)	# 1352-1358
    sprite('ha611_06', 7)	# 1359-1365
    sprite('ha611_07', 7)	# 1366-1372
    SFX_1('bha700uyu')
    sprite('ha611_08', 7)	# 1373-1379
    sprite('ha611_09', 7)	# 1380-1386
    sprite('ha611_10', 7)	# 1387-1393
    sprite('ha611_11', 7)	# 1394-1400
    label(171)
    sprite('ha611_12', 8)	# 1401-1408
    sprite('ha611_13', 8)	# 1409-1416
    sprite('ha611_14', 8)	# 1417-1424
    loopRest()
    if SLOT_97:
        _gotolabel(171)
    sprite('ha611_12', 8)	# 1425-1432
    sprite('ha611_13', 8)	# 1433-1440
    sprite('ha611_14', 8)	# 1441-1448
    Unknown21007(24, 40)
    Unknown21011(200)
    label(172)
    sprite('ha611_12', 8)	# 1449-1456
    sprite('ha611_13', 8)	# 1457-1464
    sprite('ha611_14', 8)	# 1465-1472
    loopRest()
    gotoLabel(172)
    label(180)
    sprite('ha610_00', 3)	# 1473-1475
    sprite('ha610_00', 4)	# 1476-1479
    sprite('ha610_01', 6)	# 1480-1485
    sprite('ha610_02', 6)	# 1486-1491
    sprite('ha610_03', 6)	# 1492-1497
    sprite('ha610_04', 6)	# 1498-1503
    sprite('ha610_05', 6)	# 1504-1509
    sprite('ha610_06', 6)	# 1510-1515
    sprite('ha610_07', 6)	# 1516-1521
    SFX_1('bha700biz')
    sprite('ha610_08', 6)	# 1522-1527
    sprite('ha610_09', 6)	# 1528-1533
    sprite('ha610_10', 6)	# 1534-1539
    sprite('ha610_11', 6)	# 1540-1545
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 1546-1551
    label(181)
    sprite('ha610_13', 6)	# 1552-1557
    sprite('ha610_14', 6)	# 1558-1563
    sprite('ha610_15', 6)	# 1564-1569
    sprite('ha610_16', 6)	# 1570-1575
    sprite('ha610_17', 6)	# 1576-1581
    sprite('ha610_18', 6)	# 1582-1587
    loopRest()
    if SLOT_97:
        _gotolabel(181)
    sprite('ha610_13', 1)	# 1588-1588
    Unknown21007(24, 40)
    Unknown21011(270)
    label(182)
    sprite('ha610_13', 6)	# 1589-1594
    sprite('ha610_14', 6)	# 1595-1600
    sprite('ha610_15', 6)	# 1601-1606
    sprite('ha610_16', 6)	# 1607-1612
    sprite('ha610_17', 6)	# 1613-1618
    sprite('ha610_18', 6)	# 1619-1624
    loopRest()
    gotoLabel(182)
    label(190)
    sprite('ha000_00', 1)	# 1625-1625

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ha000_00', 7)	# 1626-1632
    sprite('ha000_01', 7)	# 1633-1639
    sprite('ha000_02', 7)	# 1640-1646
    sprite('ha000_03', 7)	# 1647-1653
    sprite('ha000_04', 7)	# 1654-1660
    sprite('ha000_05', 7)	# 1661-1667
    sprite('ha000_06', 7)	# 1668-1674
    sprite('ha000_07', 7)	# 1675-1681
    sprite('ha000_08', 7)	# 1682-1688
    sprite('ha000_09', 7)	# 1689-1695
    sprite('ha000_10', 7)	# 1696-1702
    sprite('ha000_11', 7)	# 1703-1709
    gotoLabel(191)
    label(192)
    sprite('ha615_00', 6)	# 1710-1715
    sprite('ha615_01', 6)	# 1716-1721
    sprite('ha615_02', 6)	# 1722-1727
    sprite('ha615_03', 6)	# 1728-1733
    sprite('ha615_04', 6)	# 1734-1739
    sprite('ha615_05', 6)	# 1740-1745
    SFX_1('bha701pak')
    Unknown23018(1)
    label(193)
    sprite('ha615_06', 7)	# 1746-1752
    sprite('ha615_07', 7)	# 1753-1759
    sprite('ha615_08', 7)	# 1760-1766
    sprite('ha615_09', 7)	# 1767-1773
    loopRest()
    gotoLabel(193)
    label(200)
    sprite('ha000_00', 1)	# 1774-1774

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ha000_00', 7)	# 1775-1781
    sprite('ha000_01', 7)	# 1782-1788
    sprite('ha000_02', 7)	# 1789-1795
    sprite('ha000_03', 7)	# 1796-1802
    sprite('ha000_04', 7)	# 1803-1809
    sprite('ha000_05', 7)	# 1810-1816
    sprite('ha000_06', 7)	# 1817-1823
    sprite('ha000_07', 7)	# 1824-1830
    sprite('ha000_08', 7)	# 1831-1837
    sprite('ha000_09', 7)	# 1838-1844
    sprite('ha000_10', 7)	# 1845-1851
    sprite('ha000_11', 7)	# 1852-1858
    gotoLabel(201)
    label(202)
    sprite('ha611_00', 1)	# 1859-1859
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
    sprite('ha611_00', 5)	# 1860-1864
    sprite('ha611_01', 6)	# 1865-1870
    sprite('ha611_02', 6)	# 1871-1876
    sprite('ha611_03', 6)	# 1877-1882
    sprite('ha611_04', 6)	# 1883-1888
    sprite('ha611_05', 7)	# 1889-1895
    sprite('ha611_06', 7)	# 1896-1902
    sprite('ha611_07', 7)	# 1903-1909
    SFX_1('bha701ume')
    sprite('ha611_08', 7)	# 1910-1916
    sprite('ha611_09', 7)	# 1917-1923
    sprite('ha611_10', 7)	# 1924-1930
    sprite('ha611_11', 7)	# 1931-1937
    Unknown23018(1)
    label(203)
    sprite('ha611_12', 8)	# 1938-1945
    sprite('ha611_13', 8)	# 1946-1953
    sprite('ha611_14', 8)	# 1954-1961
    loopRest()
    gotoLabel(203)
    label(210)
    sprite('ha615_00', 6)	# 1962-1967
    sprite('ha615_01', 6)	# 1968-1973
    sprite('ha615_02', 6)	# 1974-1979
    sprite('ha615_03', 6)	# 1980-1985
    sprite('ha615_04', 6)	# 1986-1991
    sprite('ha615_05', 6)	# 1992-1997
    SFX_1('bha700bsu')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(240)
    label(211)
    sprite('ha615_06', 7)	# 1998-2004
    sprite('ha615_07', 7)	# 2005-2011
    sprite('ha615_08', 7)	# 2012-2018
    sprite('ha615_09', 7)	# 2019-2025
    gotoLabel(211)
    label(220)
    sprite('ha610_00', 3)	# 2026-2028
    sprite('ha610_00', 4)	# 2029-2032
    sprite('ha610_01', 6)	# 2033-2038
    sprite('ha610_02', 6)	# 2039-2044
    sprite('ha610_03', 6)	# 2045-2050
    sprite('ha610_04', 6)	# 2051-2056
    sprite('ha610_05', 6)	# 2057-2062
    sprite('ha610_06', 6)	# 2063-2068
    sprite('ha610_07', 6)	# 2069-2074
    SFX_1('bha700pad')
    sprite('ha610_08', 6)	# 2075-2080
    sprite('ha610_09', 6)	# 2081-2086
    sprite('ha610_10', 6)	# 2087-2092
    sprite('ha610_11', 6)	# 2093-2098
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 2099-2104
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(210)
    label(221)
    sprite('ha610_13', 6)	# 2105-2110
    sprite('ha610_14', 6)	# 2111-2116
    sprite('ha610_15', 6)	# 2117-2122
    sprite('ha610_16', 6)	# 2123-2128
    sprite('ha610_17', 6)	# 2129-2134
    sprite('ha610_18', 6)	# 2135-2140
    loopRest()
    gotoLabel(221)

@State
def CmnActLose():
    sprite('ha620_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('bha403_0', 100, 878798946, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ha620_01', 6)	# 7-12
    sprite('ha620_02', 6)	# 13-18
    sprite('ha620_03', 6)	# 19-24
    sprite('ha620_04', 6)	# 25-30
    sprite('ha620_05', 6)	# 31-36
    sprite('ha620_06', 6)	# 37-42
    Unknown23018(1)
    sprite('ha620_07', 32767)	# 43-32809

@State
def EventDefEntryWait():
    label(0)
    sprite('ha000_00', 7)	# 1-7
    sprite('ha000_01', 7)	# 8-14
    sprite('ha000_02', 7)	# 15-21
    sprite('ha000_03', 7)	# 22-28
    sprite('ha000_04', 7)	# 29-35
    sprite('ha000_05', 7)	# 36-42
    sprite('ha000_06', 7)	# 43-49
    sprite('ha000_07', 7)	# 50-56
    sprite('ha000_08', 7)	# 57-63
    sprite('ha000_09', 7)	# 64-70
    sprite('ha000_10', 7)	# 71-77
    sprite('ha000_11', 7)	# 78-84
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
def EventWin615Start():
    sprite('ha615_00', 6)	# 1-6
    sprite('ha615_01', 6)	# 7-12
    sprite('ha615_02', 6)	# 13-18
    sprite('ha615_03', 6)	# 19-24
    sprite('ha615_04', 6)	# 25-30
    sprite('ha615_05', 6)	# 31-36
    loopRest()
    enterState('EventWin615Loop')

@State
def EventWin615Loop():
    label(0)
    sprite('ha615_06', 7)	# 1-7
    sprite('ha615_07', 7)	# 8-14
    sprite('ha615_08', 7)	# 15-21
    sprite('ha615_09', 7)	# 22-28
    loopRest()
    gotoLabel(0)

@State
def EventQuakeLoop():
    label(0)
    sprite('keep', 10)	# 1-10
    ScreenShake(3000, 6000)
    sprite('keep', 10)	# 11-20
    ScreenShake(-3000, 6000)
    loopRest()
    gotoLabel(0)

@State
def EventDefLose():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown3069(0)
        Unknown1084(0)
        Unknown3032()
    sprite('ha620_00', 6)	# 1-6
    Unknown3029(1)
    sprite('ha620_01', 6)	# 7-12
    sprite('ha620_02', 6)	# 13-18
    sprite('ha620_03', 6)	# 19-24
    sprite('ha620_04', 6)	# 25-30
    sprite('ha620_05', 6)	# 31-36
    sprite('ha620_06', 6)	# 37-42
    sprite('ha620_07', 30)	# 43-72
    Unknown3029(0)
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha620_07', 30)	# 73-102
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_1')
    sprite('ha620_07', 30)	# 103-132
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha620_07', 30)	# 133-162
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_1')
    sprite('ha620_07', 30)	# 163-192
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha620_07', 30)	# 193-222
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('001_airbackdash_1')
    sprite('ha620_07', 30)	# 223-252
    GFX_1('haef_event_lose', 0)
    Unknown3004(-5)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha620_07', 30)	# 253-282
    GFX_1('haef_event_lose', 0)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    sprite('ha620_07', 30)	# 283-312
    GFX_1('haef_event_lose_end', 0)
    sprite('null', 60)	# 313-372
    sprite('null', 32767)	# 373-33139
    Unknown3004(0)
    Unknown3001(255)

@State
def EventDefLoseNonWarpEffect():
    sprite('ha620_06', 32767)	# 1-32767
    loopRest()

@State
def EventDefEntry():
    label(0)
    sprite('ha600_00', 7)	# 1-7
    sprite('ha600_01', 7)	# 8-14
    gotoLabel(0)

@State
def EventDefEntryEx():
    label(0)
    sprite('ha600_00', 7)	# 1-7
    gotoLabel(0)

@State
def EventDefEntryToStart():
    sprite('ha600_00', 7)	# 1-7
    sprite('ha600_01', 7)	# 8-14
    sprite('ha600_02', 4)	# 15-18
    sprite('ha600_03', 4)	# 19-22
    sprite('ha600_04', 4)	# 23-26
    sprite('ha600_05', 4)	# 27-30
    sprite('ha600_06', 3)	# 31-33
    sprite('ha600_07', 3)	# 34-36
    sprite('ha600_08', 5)	# 37-41
    sprite('ha600_09', 5)	# 42-46
    sprite('ha600_10', 5)	# 47-51
    sprite('ha600_11', 5)	# 52-56
    sprite('ha600_12', 5)	# 57-61
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 5)	# 62-66
    sprite('ha600_14', 5)	# 67-71
    sprite('ha600_15', 5)	# 72-76
    sprite('ha600_16', 5)	# 77-81
    sprite('ha600_17', 5)	# 82-86
    sprite('ha600_18', 5)	# 87-91
    sprite('ha600_19', 5)	# 92-96
    sprite('ha600_20', 5)	# 97-101
    sprite('ha600_21', 5)	# 102-106
    sprite('ha600_22', 5)	# 107-111
    sprite('ha000_00', 1)	# 112-112
    enterState('CmnActStand')

@State
def EventDefEntry2():
    label(0)
    sprite('ha601_00', 6)	# 1-6
    sprite('ha601_01', 6)	# 7-12
    sprite('ha601_02', 6)	# 13-18
    sprite('ha601_03', 6)	# 19-24
    gotoLabel(0)

@State
def EventDefEntry2ToStart():
    sprite('ha601_00', 6)	# 1-6
    sprite('ha601_01', 6)	# 7-12
    sprite('ha601_02', 6)	# 13-18
    sprite('ha601_03', 6)	# 19-24
    sprite('ha601_04', 6)	# 25-30
    sprite('ha601_05', 6)	# 31-36
    sprite('ha601_06', 6)	# 37-42
    sprite('ha601_07', 6)	# 43-48
    sprite('ha601_08', 6)	# 49-54
    sprite('ha601_09', 6)	# 55-60
    sprite('ha601_10', 6)	# 61-66
    sprite('ha601_11', 6)	# 67-72
    sprite('ha601_12', 6)	# 73-78
    sprite('ha601_13', 7)	# 79-85
    sprite('ha601_14', 7)	# 86-92
    sprite('ha601_15', 7)	# 93-99
    sprite('ha601_16', 7)	# 100-106
    sprite('ha601_17', 7)	# 107-113
    sprite('ha601_18', 7)	# 114-120
    sprite('ha601_19', 7)	# 121-127
    sprite('ha601_20', 7)	# 128-134
    sprite('ha601_21', 7)	# 135-141
    sprite('ha601_22', 7)	# 142-148
    sprite('ha000_00', 1)	# 149-149
    enterState('CmnActStand')

@State
def EventDefNoDisp():
    sprite('null', 1)	# 1-1
    teleportRelativeX(-700000)
    Unknown2034(0)

@State
def EventDefWalk():
    sprite('ha030_00', 7)	# 1-7
    Unknown2034(0)
    physicsXImpulse(4000)
    sprite('ha030_01', 7)	# 8-14
    SFX_0('200_walk_normal_1')
    sprite('ha030_02', 7)	# 15-21
    sprite('ha030_03', 7)	# 22-28
    sprite('ha030_04', 7)	# 29-35
    sprite('ha030_05', 7)	# 36-42
    sprite('ha030_06', 7)	# 43-49
    sprite('ha030_07', 7)	# 50-56
    sprite('ha030_08', 7)	# 57-63
    sprite('ha030_01', 7)	# 64-70
    SFX_0('200_walk_normal_1')
    sprite('ha030_02', 7)	# 71-77
    sprite('ha030_03', 7)	# 78-84
    sprite('ha030_04', 7)	# 85-91
    sprite('ha030_05', 7)	# 92-98
    sprite('ha030_06', 7)	# 99-105
    sprite('ha030_07', 7)	# 106-112
    sprite('ha030_08', 7)	# 113-119
    sprite('ha030_01', 7)	# 120-126
    SFX_0('200_walk_normal_1')
    sprite('ha030_02', 7)	# 127-133
    sprite('ha030_03', 7)	# 134-140
    sprite('ha030_04', 7)	# 141-147
    sprite('ha030_05', 7)	# 148-154
    sprite('ha030_06', 7)	# 155-161
    sprite('ha030_07', 7)	# 162-168
    sprite('ha030_08', 7)	# 169-175
    sprite('ha030_01', 7)	# 176-182
    SFX_0('200_walk_normal_1')
    physicsXImpulse(0)
    Unknown1000(-260000)
    sprite('ha000_00', 1)	# 183-183
    enterState('CmnActStand')

@State
def EventExciteStart():
    sprite('ha300_00', 6)	# 1-6
    sprite('ha300_01', 6)	# 7-12
    sprite('ha300_02', 6)	# 13-18
    sprite('ha300_03', 6)	# 19-24
    sprite('ha300_04', 6)	# 25-30
    sprite('ha300_05', 6)	# 31-36
    sprite('ha300_06', 6)	# 37-42
    sprite('ha300_07', 6)	# 43-48
    sprite('ha300_08', 6)	# 49-54
    label(0)
    sprite('ha300_09', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def EventExciteStop():
    sprite('ha300_10', 8)	# 1-8
    sprite('ha300_11', 8)	# 9-16
    sprite('ha300_12', 8)	# 17-24
    sprite('ha000_00', 1)	# 25-25
    enterState('CmnActStand')

@State
def EventExcite():
    sprite('ha300_00', 6)	# 1-6
    sprite('ha300_01', 6)	# 7-12
    sprite('ha300_02', 6)	# 13-18
    sprite('ha300_03', 6)	# 19-24
    sprite('ha300_04', 6)	# 25-30
    sprite('ha300_05', 6)	# 31-36
    sprite('ha300_06', 6)	# 37-42
    sprite('ha300_07', 6)	# 43-48
    sprite('ha300_08', 6)	# 49-54
    sprite('ha300_09', 6)	# 55-60
    sprite('ha300_10', 8)	# 61-68
    sprite('ha300_11', 8)	# 69-76
    sprite('ha300_12', 8)	# 77-84
    sprite('ha000_00', 1)	# 85-85
    enterState('CmnActStand')

@State
def EventMugenStart():
    sprite('ha450_00', 5)	# 1-5
    sprite('ha450_01', 5)	# 6-10
    sprite('ha450_02', 8)	# 11-18
    sprite('ha450_03', 8)	# 19-26
    sprite('ha450_04', 10)	# 27-36
    label(0)
    sprite('ha450_05', 1)	# 37-37
    loopRest()
    gotoLabel(0)

@State
def EventMugenStop():
    sprite('ha450_18', 4)	# 1-4
    sprite('ha450_19', 5)	# 5-9
    sprite('ha450_20', 5)	# 10-14
    sprite('ha450_21', 5)	# 15-19
    sprite('ha450_22', 5)	# 20-24
    sprite('ha450_23', 5)	# 25-29
    sprite('ha000_00', 1)	# 30-30
    enterState('CmnActStand')

@State
def EventMugenNewTemplate():
    sprite('ha450_00', 6)	# 1-6
    sprite('ha450_01', 6)	# 7-12
    sprite('ha450_02', 6)	# 13-18
    sprite('ha450_03', 6)	# 19-24
    sprite('ha450_04', 6)	# 25-30
    sprite('ha450_05', 50)	# 31-80
    sprite('ha450_05', 90)	# 81-170
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 90)	# 171-260
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 60)	# 261-320
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 321-330
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 331-340
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 341-350
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 351-360
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 361-370
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 371-380
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 381-390
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 391-400
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 401-410
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 411-420
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 421-430
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 431-440
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 441-450
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 451-460
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 461-470
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 471-480
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 481-490
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 491-500
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 501-510
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 511-520
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 521-530
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 531-540
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 541-550
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 551-560
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 561-570
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 571-580
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 581-590
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 591-600
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 601-610
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 611-620
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 621-630
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 631-640
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 641-650
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 651-660
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 661-670
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_06', 6)	# 671-676
    GFX_0('ha_AH', -1)
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_07', 6)	# 677-682
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_08', 6)	# 683-688
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_09', 6)	# 689-694
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_10', 6)	# 695-700
    SFX_0('019_cloth_a')
    ScreenShake(0, 30000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_11', 6)	# 701-706
    sprite('ha450_12', 6)	# 707-712
    sprite('ha450_13', 6)	# 713-718
    sprite('ha450_14', 6)	# 719-724
    sprite('ha450_15', 6)	# 725-730
    sprite('ha450_16', 6)	# 731-736
    sprite('ha450_17', 6)	# 737-742
    sprite('ha450_18', 6)	# 743-748
    sprite('ha450_19', 6)	# 749-754
    sprite('ha450_20', 6)	# 755-760
    sprite('ha450_21', 6)	# 761-766
    sprite('ha450_22', 6)	# 767-772
    sprite('ha450_23', 6)	# 773-778
    loopRest()
    enterState('CmnActStand')

@State
def EventAssault3():
    AttackDefaults_StandingSpecial()
    Unknown2034(0)
    Unknown1084(0)
    AttackLevel_(4)
    Unknown9016(1)
    Unknown2004(1, 0)
    sprite('ha402_00', 2)	# 1-2
    callSubroutine('SpecialChainCancel_Land')
    SFX_3('hase_25')
    sprite('ha402_01', 2)	# 3-4
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha402_02', 2)	# 5-6
    sprite('ha402_03', 2)	# 7-8
    physicsXImpulse(20000)
    sprite('ha402_04', 4)	# 9-12
    sprite('ha402_05', 4)	# 13-16
    sprite('ha402_06', 4)	# 17-20
    physicsXImpulse(0)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha402_07', 3)	# 21-23	 **attackbox here**
    StartMultihit()
    GFX_0('ha_402a', -1)
    sprite('ha402_08', 2)	# 24-25
    sprite('ha402_09', 2)	# 26-27
    sprite('ha402_10', 2)	# 28-29
    sprite('ha402_11', 2)	# 30-31
    physicsXImpulse(35000)
    sprite('ha402_12', 2)	# 32-33
    sprite('ha402_13', 2)	# 34-35
    sprite('ha402_14', 2)	# 36-37
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha402_15', 3)	# 38-40	 **attackbox here**
    physicsXImpulse(0)
    StartMultihit()
    GFX_0('ha_402b', -1)
    sprite('ha402_16', 8)	# 41-48
    sprite('ha402_17', 8)	# 49-56
    sprite('ha402_18', 8)	# 57-64
    Unknown3029(0)
    Unknown2001()
    Unknown14077(1)
    sprite('ha402_19', 8)	# 65-72
    sprite('ha402_20', 8)	# 73-80
    loopRest()
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventMugenTemplate():
    sprite('ha450_00', 6)	# 1-6
    sprite('ha450_01', 6)	# 7-12
    sprite('ha450_02', 6)	# 13-18
    sprite('ha450_03', 6)	# 19-24
    sprite('ha450_04', 6)	# 25-30
    sprite('ha450_05', 50)	# 31-80
    sprite('ha450_05', 120)	# 81-200
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 130)	# 201-330
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 60)	# 331-390
    ScreenShake(0, 5000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 391-400
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 401-410
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 411-420
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 421-430
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 431-440
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 441-450
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 451-460
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 461-470
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 471-480
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 481-490
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 491-500
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 501-510
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 511-520
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 521-530
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 531-540
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 541-550
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 551-560
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 561-570
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 571-580
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 581-590
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 591-600
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 601-610
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 611-620
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 621-630
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 631-640
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 641-650
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 651-660
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 661-670
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 671-680
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 681-690
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 691-700
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 701-710
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 711-720
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 721-730
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 731-740
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_06', 6)	# 741-746
    GFX_0('ha_AH', -1)
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_07', 6)	# 747-752
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_08', 6)	# 753-758
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_09', 6)	# 759-764
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_10', 6)	# 765-770
    SFX_0('019_cloth_a')
    SFX_0('019_cloth_a')
    ScreenShake(0, 30000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_11', 6)	# 771-776
    sprite('ha450_12', 6)	# 777-782
    sprite('ha450_13', 6)	# 783-788
    sprite('ha450_14', 6)	# 789-794
    sprite('ha450_15', 6)	# 795-800
    sprite('ha450_16', 6)	# 801-806
    sprite('ha450_17', 6)	# 807-812
    sprite('ha450_18', 6)	# 813-818
    sprite('ha450_19', 6)	# 819-824
    sprite('ha450_20', 6)	# 825-830
    sprite('ha450_21', 6)	# 831-836
    sprite('ha450_22', 6)	# 837-842
    sprite('ha450_23', 6)	# 843-848
    loopRest()
    enterState('CmnActStand')

@State
def EventNoDisp():
    sprite('keep', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventWarpIn():
    Unknown2019(-500)
    Unknown3032()
    Unknown2034(0)
    sprite('ha300_08', 60)	# 1-60
    Unknown3001(0)
    Unknown3004(10)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    sprite('ha300_09', 6)	# 61-66
    sprite('ha300_10', 6)	# 67-72
    sprite('ha300_11', 6)	# 73-78
    sprite('ha300_12', 6)	# 79-84
    Unknown3001(255)
    Unknown3004(0)
    GFX_1('haef_event_lose_end', 103)
    loopRest()
    enterState('CmnActStand')

@State
def EventStartWithRC():
    Unknown2005()
    Unknown13(7)
    Unknown1000(-260000)
    GFX_0('EventRCStand', -1)
    Unknown38(7, 1)
    Unknown2005()
    Unknown1000(-260000)
    sprite('ha300_09', 32767)	# 1-32767
    loopRest()

@State
def EventWorpOutRC():
    sprite('keep', 60)	# 1-60
    Unknown23029(7, 10, 0)
    sprite('keep', 32767)	# 61-32827
    Unknown13(7)
    loopRest()

@State
def EventStandUpToRCCreate():
    sprite('ha620_07', 6)	# 1-6
    sprite('ha620_06', 6)	# 7-12
    sprite('ha620_05', 6)	# 13-18
    sprite('ha620_04', 6)	# 19-24
    sprite('ha620_03', 6)	# 25-30
    sprite('ha620_02', 6)	# 31-36
    sprite('ha620_01', 6)	# 37-42
    sprite('ha620_00', 6)	# 43-48
    Unknown13(7)
    teleportRelativeX(200000)
    GFX_0('EventRCWarpIn', -1)
    Unknown38(7, 1)
    teleportRelativeX(-200000)
    loopRest()
    enterState('EventDefEntryWait')

@State
def EventExciteWorpOutWithRC():
    sprite('ha300_00', 6)	# 1-6
    Unknown23029(7, 10, 0)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha300_01', 6)	# 7-12
    sprite('ha300_02', 6)	# 13-18
    sprite('ha300_03', 6)	# 19-24
    sprite('ha300_04', 6)	# 25-30
    Unknown3038(1)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha300_05', 6)	# 31-36
    sprite('ha300_06', 6)	# 37-42
    sprite('ha300_07', 6)	# 43-48
    sprite('ha300_08', 32767)	# 49-32815
    Unknown13(7)
    loopRest()

@State
def EventMotionKeepRCCreate():
    sprite('keep', 32767)	# 1-32767
    Unknown13(7)
    teleportRelativeX(200000)
    GFX_0('EventRCWarpIn', -1)
    Unknown38(7, 1)
    teleportRelativeX(-200000)
    loopRest()

@State
def EventMotionKeepWorpOutWithRC():
    sprite('keep', 6)	# 1-6
    Unknown23029(7, 10, 0)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('keep', 6)	# 7-12
    sprite('keep', 6)	# 13-18
    sprite('keep', 6)	# 19-24
    sprite('keep', 6)	# 25-30
    Unknown3038(1)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('keep', 6)	# 31-36
    sprite('keep', 6)	# 37-42
    sprite('keep', 6)	# 43-48
    sprite('keep', 32767)	# 49-32815
    Unknown13(7)
    loopRest()

@State
def EventHAEntry01():
    label(0)
    sprite('ha600_23', 7)	# 1-7
    sprite('ha600_24', 7)	# 8-14
    sprite('ha600_25', 7)	# 15-21
    sprite('ha600_26', 7)	# 22-28
    sprite('ha600_27', 7)	# 29-35
    sprite('ha600_28', 7)	# 36-42
    loopRest()
    gotoLabel(0)

@State
def EventHAEntry01ToStand():
    sprite('ha600_29', 8)	# 1-8
    sprite('ha600_30', 8)	# 9-16
    sprite('ha600_00', 8)	# 17-24
    sprite('ha600_01', 8)	# 25-32
    sprite('ha600_02', 8)	# 33-40
    sprite('ha600_03', 8)	# 41-48
    sprite('ha600_04', 8)	# 49-56
    sprite('ha600_05', 8)	# 57-64
    sprite('ha600_06', 8)	# 65-72
    sprite('ha600_07', 8)	# 73-80
    sprite('ha600_08', 5)	# 81-85
    sprite('ha600_09', 5)	# 86-90
    sprite('ha600_10', 5)	# 91-95
    sprite('ha600_11', 5)	# 96-100
    sprite('ha600_12', 5)	# 101-105
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 5)	# 106-110
    sprite('ha600_14', 5)	# 111-115
    sprite('ha600_15', 5)	# 116-120
    sprite('ha600_16', 5)	# 121-125
    sprite('ha600_17', 5)	# 126-130
    sprite('ha600_18', 5)	# 131-135
    sprite('ha600_19', 5)	# 136-140
    sprite('ha600_20', 5)	# 141-145
    sprite('ha600_21', 5)	# 146-150
    sprite('ha600_22', 5)	# 151-155
    loopRest()
    enterState('CmnActStand')

@State
def EventHAWin00():
    sprite('ha610_00', 6)	# 1-6
    sprite('ha610_01', 6)	# 7-12
    sprite('ha610_02', 6)	# 13-18
    sprite('ha610_03', 6)	# 19-24
    sprite('ha610_04', 6)	# 25-30
    sprite('ha610_05', 6)	# 31-36
    sprite('ha610_06', 6)	# 37-42
    sprite('ha610_07', 6)	# 43-48
    sprite('ha610_08', 6)	# 49-54
    sprite('ha610_09', 6)	# 55-60
    sprite('ha610_10', 6)	# 61-66
    sprite('ha610_11', 6)	# 67-72
    SFX_3('hase_00')
    sprite('ha610_12', 6)	# 73-78
    sprite('ha610_13', 6)	# 79-84
    sprite('ha610_14', 6)	# 85-90
    sprite('ha610_15', 6)	# 91-96
    sprite('ha610_16', 6)	# 97-102
    sprite('ha610_17', 6)	# 103-108
    sprite('ha610_18', 6)	# 109-114
    loopRest()
    enterState('EventHAWin01')

@State
def EventHAWin01():
    label(0)
    sprite('ha610_13', 6)	# 1-6
    sprite('ha610_14', 6)	# 7-12
    sprite('ha610_15', 6)	# 13-18
    sprite('ha610_16', 6)	# 19-24
    sprite('ha610_17', 6)	# 25-30
    sprite('ha610_18', 6)	# 31-36
    loopRest()
    gotoLabel(0)

@State
def EventHAWin01Warp():
    sprite('ha610_13', 6)	# 1-6
    Unknown3004(-10)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('ha610_14', 6)	# 7-12
    sprite('ha610_15', 6)	# 13-18
    sprite('ha610_16', 6)	# 19-24
    sprite('ha610_17', 6)	# 25-30
    Unknown3038(1)
    SFX_0('001_airbackdash_0')
    sprite('ha610_18', 6)	# 31-36
    sprite('null', 32767)	# 37-32803
    loopRest()

@State
def EventHAvsRGEntryWait():
    sprite('ha000_00', 1)	# 1-1
    Unknown1000(-400000)
    label(0)
    sprite('ha000_00', 7)	# 2-8
    sprite('ha000_01', 7)	# 9-15
    sprite('ha000_02', 7)	# 16-22
    sprite('ha000_03', 7)	# 23-29
    sprite('ha000_04', 7)	# 30-36
    sprite('ha000_05', 7)	# 37-43
    sprite('ha000_06', 7)	# 44-50
    sprite('ha000_07', 7)	# 51-57
    sprite('ha000_08', 7)	# 58-64
    sprite('ha000_09', 7)	# 65-71
    sprite('ha000_10', 7)	# 72-78
    sprite('ha000_11', 7)	# 79-85
    loopRest()
    gotoLabel(0)

@State
def EventHAvsRGEntry():
    AttackDefaults_StandingSpecial()
    Unknown1084(0)
    AttackLevel_(4)
    Unknown2004(1, 0)
    Unknown23022(1)
    sprite('ha000_00', 3)	# 1-3
    sprite('ha401_00', 1)	# 4-4
    callSubroutine('SpecialChainCancel_Land')
    SFX_3('hase_25')
    sprite('ha401_01', 1)	# 5-5
    Unknown3029(1)
    Unknown3069(0)
    physicsXImpulse(500)
    sprite('ha401_02', 2)	# 6-7
    sprite('ha401_03', 2)	# 8-9
    sprite('ha401_04', 2)	# 10-11
    physicsXImpulse(0)
    SFX_0('004_swing_grap_1_1')
    sprite('ha401_05', 3)	# 12-14	 **attackbox here**
    GFX_0('ha_kick', -1)
    GFX_0('ha_kick_b', -1)
    GFX_1('haef_kick_drop', 0)
    sprite('ha401_06', 3)	# 15-17
    GFX_0('ha_kick2', -1)
    GFX_0('ha_kick2b', -1)
    sprite('ha401_07', 3)	# 18-20
    sprite('ha401_08', 3)	# 21-23
    GFX_0('ha_kick3', -1)
    GFX_0('ha_kick3b', -1)
    sprite('ha401_09', 3)	# 24-26
    sprite('ha401_10', 3)	# 27-29
    SFX_0('004_swing_grap_1_2')
    sprite('ha401_11', 3)	# 30-32	 **attackbox here**
    GFX_0('ha_kick4', -1)
    GFX_0('ha_kick4b', -1)
    GFX_1('haef_kick_drop', 0)
    RefreshMultihit()
    sprite('ha404_00', 4)	# 33-36
    Unknown1000(-260000)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    AttackLevel_(4)
    RefreshMultihit()
    sendToLabelUpon(2, 92)
    callSubroutine('SpecialChainCancel_Air')
    physicsYImpulse(600)
    setGravity(50)
    SFX_3('hase_25')
    sprite('ha404_01', 2)	# 37-38
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha404_02', 2)	# 39-40
    sprite('ha404_03', 2)	# 41-42
    sprite('ha404_04', 1)	# 43-43
    sprite('ha404_05', 1)	# 44-44
    sprite('ha404_06', 1)	# 45-45
    sprite('ha404_07', 1)	# 46-46
    sprite('ha404_08', 2)	# 47-48
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha404_09', 3)	# 49-51	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(0)
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 52-53
    sprite('ha404_11', 2)	# 54-55
    sprite('ha404_12', 2)	# 56-57
    Unknown3029(0)
    Unknown2001()
    Unknown14077(1)
    sprite('ha404_13', 3)	# 58-60
    Unknown1043()
    sprite('ha404_14', 3)	# 61-63
    sprite('ha404_15', 3)	# 64-66
    sprite('ha404_16', 3)	# 67-69
    label(91)
    sprite('ha020_03', 4)	# 70-73
    loopRest()
    gotoLabel(91)
    label(92)
    sprite('ha024_00', 3)	# 74-76
    Unknown8000(0, 1, 1)
    clearUponHandler(2)
    sprite('ha024_01', 3)	# 77-79
    sprite('ha024_02', 3)	# 80-82
    sprite('ha024_03', 3)	# 83-85
    sprite('ha024_04', 3)	# 86-88
    loopRest()
    enterState('CmnActStand')

@State
def EventHAvsHZEntry():
    label(0)
    sprite('ha001_00', 1)	# 1-1
    Unknown1000(-800000)
    Unknown2034(0)
    loopRest()
    gotoLabel(0)

@State
def EventChouhatuEntryWait():
    label(0)
    sprite('ha300_09', 6)	# 1-6
    loopRest()
    gotoLabel(0)

@State
def EventChouhatuEntry():
    sprite('ha300_10', 6)	# 1-6
    sprite('ha300_11', 6)	# 7-12
    sprite('ha300_12', 6)	# 13-18
    loopRest()
    enterState('CmnActStand')

@State
def EventHAvsMUWarpKeep():
    sprite('keep', 6)	# 1-6
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    label(0)
    sprite('keep', 6)	# 7-12
    GFX_1('haef_event_lose', 103)
    gotoLabel(0)

@State
def EventHAvsMUWarpOut():
    sprite('keep', 6)	# 1-6
    GFX_1('haef_event_lose', 103)
    Unknown3004(-10)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')
    sprite('keep', 30)	# 7-36
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_s')
    SFX_0('000_airdash_2')
    sprite('keep', 30)	# 37-66
    GFX_1('haef_event_lose_end', 103)
    sprite('null', 60)	# 67-126
    sprite('null', 32767)	# 127-32893
    Unknown3004(0)
    Unknown3001(255)

@State
def EventMUvsHAMugenStart():
    sprite('ha450_00', 5)	# 1-5
    sprite('ha450_01', 5)	# 6-10
    sprite('ha450_02', 8)	# 11-18
    sprite('ha450_03', 8)	# 19-26
    sprite('ha450_04', 10)	# 27-36
    label(0)
    sprite('ha450_05', 1)	# 37-37
    loopRest()
    gotoLabel(0)

@State
def EventMUvsHAMugenStop():
    sprite('ha450_06', 6)	# 1-6
    GFX_0('ha_AH', -1)
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_07', 6)	# 7-12
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_08', 6)	# 13-18
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_09', 6)	# 19-24
    SFX_0('019_cloth_a')
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_10', 6)	# 25-30
    ScreenShake(0, 30000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_11', 6)	# 31-36
    sprite('ha450_12', 6)	# 37-42
    sprite('ha450_13', 6)	# 43-48
    sprite('ha450_14', 6)	# 49-54
    sprite('ha450_15', 6)	# 55-60
    sprite('ha450_16', 6)	# 61-66
    sprite('ha450_17', 6)	# 67-72
    sprite('ha450_18', 6)	# 73-78
    sprite('ha450_19', 6)	# 79-84
    sprite('ha450_20', 6)	# 85-90
    sprite('ha450_21', 6)	# 91-96
    sprite('ha450_22', 6)	# 97-102
    sprite('ha450_23', 6)	# 103-108
    loopRest()
    enterState('CmnActStand')

@State
def EventHAvsVHStandUp():
    sprite('ha010_01', 7)	# 1-7
    sprite('ha010_00', 7)	# 8-14
    sprite('ha000_00', 1)	# 15-15
    enterState('CmnActStand')

@State
def EventRGvsHA_CreateTB():
    sprite('keep', 1)	# 1-1
    GFX_0('EventEffectHAVsRG_TB', 0)
    loopRest()
    enterState('CmnActStand')

@State
def EventRGvsHA_TBGoOut():
    sprite('keep', 1)	# 1-1
    Unknown21007(1, 32)
    loopRest()
    enterState('CmnActStand')

@State
def EventNoise():
    sprite('keep', 2)	# 1-2
    GFX_0('NOISE', -1)
    SFX_0('023_noize')
    enterState('EventHAWin01')

@State
def EventHANoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def SummonTrinity():
    sprite('keep', 2)	# 1-2
    GFX_0('SummonTrinity', 0)
    SFX_0('022_magiccircle_a')
    Unknown38(4, 1)
    loopRest()

@State
def DeleteTrinity():
    sprite('null', 120)	# 1-120
    Unknown36(4)
    Unknown3004(-5)
    SFX_0('022_magiccircle_b')
    Unknown35()
    sprite('null', 32767)	# 121-32887
    Unknown13(4)
    Unknown3038(1)

@State
def EventHAAppear():
    sprite('ha601_00', 6)	# 1-6
    Unknown3001(0)
    Unknown3004(5)
    SFX_0('000_airdash_0')
    sprite('ha601_01', 6)	# 7-12
    sprite('ha601_02', 6)	# 13-18
    sprite('ha601_03', 6)	# 19-24
    label(0)
    sprite('ha601_00', 6)	# 25-30
    sprite('ha601_01', 6)	# 31-36
    sprite('ha601_02', 6)	# 37-42
    sprite('ha601_03', 6)	# 43-48
    gotoLabel(0)

@State
def EventHAWinReverse():
    label(0)
    sprite('ha610_13', 6)	# 1-6
    sprite('ha610_14', 6)	# 7-12
    sprite('ha610_15', 6)	# 13-18
    sprite('ha610_16', 6)	# 19-24
    sprite('ha610_17', 6)	# 25-30
    sprite('ha610_18', 6)	# 31-36
    loopRest()
    gotoLabel(0)

@State
def EventHAWinReverseEnd():
    sprite('ha610_12', 6)	# 1-6
    sprite('ha610_11', 6)	# 7-12
    sprite('ha610_10', 6)	# 13-18
    sprite('ha610_09', 6)	# 19-24
    sprite('ha610_08', 6)	# 25-30
    sprite('ha610_07', 6)	# 31-36
    sprite('ha610_06', 6)	# 37-42
    sprite('ha610_05', 6)	# 43-48
    sprite('ha610_04', 6)	# 49-54
    sprite('ha610_03', 6)	# 55-60
    sprite('ha610_02', 6)	# 61-66
    sprite('ha610_01', 6)	# 67-72
    sprite('ha610_00', 6)	# 73-78
    enterState('CmnActStand')

@State
def EventExciteWorpOut():
    sprite('ha331_00', 6)	# 1-6
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    sprite('ha331_01', 6)	# 7-12
    sprite('ha331_02', 6)	# 13-18
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    sprite('ha331_03', 6)	# 19-24
    sprite('ha331_04', 6)	# 25-30
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    sprite('ha331_05', 6)	# 31-36
    sprite('ha331_06', 6)	# 37-42
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    label(0)
    sprite('ha331_07', 6)	# 43-48
    sprite('ha331_08', 6)	# 49-54
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    loopRest()
    gotoLabel(0)

@State
def EventExciteWorpOutEnd():
    sprite('ha331_07', 6)	# 1-6
    sprite('ha331_08', 6)	# 7-12
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    sprite('ha331_07', 6)	# 13-18
    sprite('ha331_08', 6)	# 19-24
    Unknown3038(1)
    GFX_1('haef_event_lose', 103)
    SFX_0('014_electric_m')
    SFX_0('001_airbackdash_0')

@State
def EventTMLose():
    sprite('ha620_00', 6)	# 1-6
    sprite('ha620_01', 6)	# 7-12
    sprite('ha620_02', 6)	# 13-18
    sprite('ha620_03', 6)	# 19-24
    sprite('ha620_04', 6)	# 25-30
    sprite('ha620_05', 6)	# 31-36
    sprite('ha620_06', 6)	# 37-42
    sprite('ha620_07', 32767)	# 43-32809

@State
def EventTMLoseToStand():
    sprite('ha620_07', 6)	# 1-6
    sprite('ha620_06', 6)	# 7-12
    sprite('ha620_03', 6)	# 13-18
    sprite('ha620_02', 6)	# 19-24
    sprite('ha620_01', 6)	# 25-30
    sprite('ha620_00', 6)	# 31-36
    loopRest()
    enterState('CmnActStand')

@State
def EventMugenNewTemplate2():
    sprite('ha450_00', 6)	# 1-6
    sprite('ha450_01', 6)	# 7-12
    sprite('ha450_02', 6)	# 13-18
    sprite('ha450_03', 6)	# 19-24
    sprite('ha450_04', 6)	# 25-30
    sprite('ha450_05', 25)	# 31-55
    sprite('ha450_05', 120)	# 56-175
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 120)	# 176-295
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 60)	# 296-355
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 356-365
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 366-375
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 376-385
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 386-395
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 396-405
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 406-415
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 416-425
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 426-435
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 436-445
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 446-455
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 456-465
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 466-475
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 476-485
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 486-495
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 496-505
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 506-515
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 516-525
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 526-535
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 536-545
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 546-555
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 556-565
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 566-575
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 576-585
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 586-595
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 596-605
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 606-615
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 616-625
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 626-635
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 636-645
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 646-655
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 656-665
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 666-675
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 676-685
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 686-695
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_05', 10)	# 696-705
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    sprite('ha450_06', 6)	# 706-711
    GFX_0('ha_AH', -1)
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_07', 6)	# 712-717
    SFX_0('019_cloth_a')
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_08', 6)	# 718-723
    SFX_0('019_cloth_a')
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_09', 6)	# 724-729
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_10', 6)	# 730-735
    ScreenShake(0, 60000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_11', 6)	# 736-741
    sprite('ha450_12', 6)	# 742-747
    sprite('ha450_13', 6)	# 748-753
    sprite('ha450_14', 6)	# 754-759
    sprite('ha450_15', 6)	# 760-765
    sprite('ha450_16', 6)	# 766-771
    sprite('ha450_17', 6)	# 772-777
    sprite('ha450_18', 6)	# 778-783
    sprite('ha450_19', 6)	# 784-789
    sprite('ha450_20', 6)	# 790-795
    sprite('ha450_21', 6)	# 796-801
    sprite('ha450_22', 6)	# 802-807
    sprite('ha450_23', 6)	# 808-813
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Entry():
    label(0)
    sprite('ha600_00', 7)	# 1-7
    sprite('ha600_01', 7)	# 8-14
    loopRest()
    gotoLabel(0)

@State
def Act2Event_EntryEnd():
    sprite('keep', 2)	# 1-2
    sprite('ha600_02', 4)	# 3-6
    sprite('ha600_03', 4)	# 7-10
    sprite('ha600_04', 4)	# 11-14
    sprite('ha600_05', 4)	# 15-18
    sprite('ha600_06', 3)	# 19-21
    sprite('ha600_07', 3)	# 22-24
    sprite('ha600_08', 5)	# 25-29
    sprite('ha600_09', 5)	# 30-34
    sprite('ha600_10', 5)	# 35-39
    sprite('ha600_11', 5)	# 40-44
    sprite('ha600_12', 5)	# 45-49
    SFX_0('006_swing_blade_2')
    sprite('ha600_13', 5)	# 50-54
    sprite('ha600_14', 5)	# 55-59
    sprite('ha600_15', 5)	# 60-64
    sprite('ha600_16', 5)	# 65-69
    sprite('ha600_17', 5)	# 70-74
    sprite('ha600_18', 5)	# 75-79
    sprite('ha600_19', 5)	# 80-84
    sprite('ha600_20', 5)	# 85-89
    sprite('ha600_21', 5)	# 90-94
    sprite('ha600_22', 5)	# 95-99
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_NoDisp():

    def upon_IMMEDIATE():
        Unknown3038(1)

        def upon_STATE_END():
            Unknown3038(0)
    sprite('null', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_Entry2():
    label(0)
    sprite('ha601_00', 6)	# 1-6
    sprite('ha601_01', 6)	# 7-12
    sprite('ha601_02', 6)	# 13-18
    sprite('ha601_03', 6)	# 19-24
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Entry2End():
    sprite('keep', 2)	# 1-2
    sprite('ha601_04', 6)	# 3-8
    sprite('ha601_05', 6)	# 9-14
    sprite('ha601_06', 6)	# 15-20
    sprite('ha601_07', 6)	# 21-26
    sprite('ha601_08', 6)	# 27-32
    sprite('ha601_09', 6)	# 33-38
    sprite('ha601_10', 6)	# 39-44
    sprite('ha601_11', 6)	# 45-50
    sprite('ha601_12', 6)	# 51-56
    sprite('ha601_13', 7)	# 57-63
    sprite('ha601_14', 7)	# 64-70
    sprite('ha601_15', 7)	# 71-77
    sprite('ha601_16', 7)	# 78-84
    sprite('ha601_17', 7)	# 85-91
    sprite('ha601_18', 7)	# 92-98
    sprite('ha601_19', 7)	# 99-105
    sprite('ha601_20', 7)	# 106-112
    sprite('ha601_21', 7)	# 113-119
    sprite('ha601_22', 7)	# 120-126
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Mugen():
    sprite('ha450_00', 5)	# 1-5
    sprite('ha450_01', 5)	# 6-10
    sprite('ha450_02', 8)	# 11-18
    sprite('ha450_03', 8)	# 19-26
    sprite('ha450_04', 10)	# 27-36
    sprite('ha450_05', 32767)	# 37-32803

@State
def Act2Event_MugenEnd():
    sprite('ha450_18', 4)	# 1-4
    sprite('ha450_19', 5)	# 5-9
    sprite('ha450_20', 5)	# 10-14
    sprite('ha450_21', 5)	# 15-19
    sprite('ha450_22', 5)	# 20-24
    sprite('ha450_23', 5)	# 25-29
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_MugenEnd2():
    sprite('ha450_05', 120)	# 1-120
    Unknown2037(12)
    label(0)
    sprite('ha450_05', 10)	# 121-130
    Unknown2038(-1)
    ScreenShake(0, 3000)
    SFX_0('019_quake_0')
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    Unknown2037(12)
    label(1)
    sprite('ha450_05', 10)	# 131-140
    Unknown2038(-1)
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    sprite('ha450_06', 5)	# 141-145
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    sprite('ha450_07', 5)	# 146-150
    SFX_3('hase_21')
    ScreenShake(30000, 52000)
    Unknown8000(0, 1, 1)
    sprite('ha450_08', 5)	# 151-155
    sprite('ha450_09', 5)	# 156-160
    sprite('ha450_10', 5)	# 161-165
    SFX_3('hase_21')
    sprite('ha450_11', 5)	# 166-170
    sprite('ha450_12', 4)	# 171-174
    sprite('ha450_13', 4)	# 175-178
    SFX_3('hase_21')
    sprite('ha450_14', 4)	# 179-182
    sprite('ha450_15', 4)	# 183-186
    sprite('ha450_16', 4)	# 187-190
    sprite('ha450_17', 4)	# 191-194
    sprite('ha450_18', 4)	# 195-198
    sprite('ha450_19', 5)	# 199-203
    sprite('ha450_20', 5)	# 204-208
    sprite('ha450_21', 5)	# 209-213
    sprite('ha450_22', 5)	# 214-218
    sprite('ha450_23', 5)	# 219-223
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Yoin():
    sprite('ha212_05', 3)	# 1-3
    sprite('ha212_06', 3)	# 4-6
    sprite('ha212_07', 3)	# 7-9
    sprite('ha212_08', 18)	# 10-27	 **attackbox here**
    sprite('ha212_09', 3)	# 28-30
    sprite('ha212_10', 4)	# 31-34
    sprite('ha212_11', 4)	# 35-38
    sprite('ha212_12', 4)	# 39-42
    sprite('ha212_13', 4)	# 43-46
    sprite('ha212_14', 4)	# 47-50
    sprite('ha212_15', 4)	# 51-54
    sprite('ha212_16', 4)	# 55-58
    sprite('ha212_17', 4)	# 59-62
    sprite('ha212_18', 4)	# 63-66
    sprite('ha212_19', 4)	# 67-70
    SFX_3('hase_22')
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Semuke():
    sprite('keep', 2)	# 1-2
    sprite('ha451_47', 6)	# 3-8
    Unknown2005()
    teleportRelativeX(120000)
    sprite('ha451_46', 6)	# 9-14
    sprite('ha451_45', 6)	# 15-20
    sprite('ha451_44', 6)	# 21-26
    sprite('ha451_43', 6)	# 27-32
    sprite('ha451_22', 32767)	# 33-32799
    loopRest()

@State
def Act2Event_SemukeHalf():
    sprite('ha451_22', 8)	# 1-8
    sprite('ha451_23', 8)	# 9-16
    sprite('ha451_24', 8)	# 17-24
    sprite('ha451_25', 8)	# 25-32
    sprite('ha451_26', 8)	# 33-40
    sprite('ha451_27', 8)	# 41-48
    sprite('ha451_28', 6)	# 49-54
    sprite('ha451_29', 6)	# 55-60
    sprite('ha451_30', 6)	# 61-66
    sprite('ha451_31', 6)	# 67-72
    sprite('ha451_32', 30)	# 73-102
    sprite('ha451_33', 2)	# 103-104
    sprite('ha451_34', 15)	# 105-119
    SFX_3('hase_00')
    sprite('ha451_35', 32767)	# 120-32886
    loopRest()

@State
def Act2Event_SemukeEnd():
    sprite('ha451_36', 6)	# 1-6
    sprite('ha451_37', 6)	# 7-12
    sprite('ha451_38', 6)	# 13-18
    sprite('ha451_39', 6)	# 19-24
    sprite('ha451_40', 6)	# 25-30
    sprite('ha451_41', 6)	# 31-36
    sprite('ha451_42', 6)	# 37-42
    label(0)
    sprite('ha451_39', 6)	# 43-48
    sprite('ha451_40', 6)	# 49-54
    sprite('ha451_41', 6)	# 55-60
    sprite('ha451_42', 6)	# 61-66
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Noutou():
    sprite('ha610_00', 6)	# 1-6
    sprite('ha610_01', 6)	# 7-12
    sprite('ha610_02', 6)	# 13-18
    sprite('ha610_03', 6)	# 19-24
    sprite('ha610_04', 6)	# 25-30
    sprite('ha610_05', 6)	# 31-36
    sprite('ha610_06', 6)	# 37-42
    sprite('ha610_07', 6)	# 43-48
    sprite('ha610_08', 6)	# 49-54
    sprite('ha610_09', 6)	# 55-60
    sprite('ha610_10', 6)	# 61-66
    sprite('ha610_11', 6)	# 67-72
    SFX_3('hase_22')
    sprite('ha610_12', 6)	# 73-78
    label(0)
    sprite('ha610_13', 6)	# 79-84
    sprite('ha610_14', 6)	# 85-90
    sprite('ha610_15', 6)	# 91-96
    sprite('ha610_16', 6)	# 97-102
    sprite('ha610_17', 6)	# 103-108
    sprite('ha610_18', 6)	# 109-114
    loopRest()
    gotoLabel(0)
    enterState('CmnActStand')

@State
def Act2Event_Chouhatsu():
    sprite('ha300_00', 6)	# 1-6
    sprite('ha300_01', 6)	# 7-12
    sprite('ha300_02', 6)	# 13-18
    sprite('ha300_03', 6)	# 19-24
    sprite('ha300_04', 6)	# 25-30
    sprite('ha300_05', 6)	# 31-36
    sprite('ha300_06', 6)	# 37-42
    sprite('ha300_07', 6)	# 43-48
    sprite('ha300_08', 6)	# 49-54
    sprite('ha300_09', 6)	# 55-60
    sprite('ha300_10', 6)	# 61-66
    sprite('ha300_11', 6)	# 67-72
    sprite('ha300_12', 6)	# 73-78
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_QuakeLoop():
    label(0)
    sprite('keep', 10)	# 1-10
    SFX_0('019_quake_1')
    ScreenShake(3000, 6000)
    sprite('keep', 10)	# 11-20
    ScreenShake(-3000, 6000)
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Walkin():
    Unknown2034(0)
    teleportRelativeX(-720000)

    def upon_CLEAR_OR_EXIT():
        if SLOT_38:
            if (SLOT_22 < 260000):
                clearUponHandler(3)
                Unknown1000(-260000)
                Unknown1084(1)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            clearUponHandler(3)
            Unknown1000(-260000)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ha030_00', 7)	# 1-7
    physicsXImpulse(4000)
    label(0)
    sprite('ha030_01', 7)	# 8-14
    SFX_0('200_walk_normal_1')
    sprite('ha030_02', 7)	# 15-21
    sprite('ha030_03', 7)	# 22-28
    sprite('ha030_04', 7)	# 29-35
    sprite('ha030_05', 7)	# 36-42
    sprite('ha030_06', 7)	# 43-49
    sprite('ha030_07', 7)	# 50-56
    sprite('ha030_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha000_00', 1)	# 64-64
    enterState('CmnActStand')

@State
def Act2Event_havstb_00():
    sprite('ha611_00', 6)	# 1-6
    sprite('ha611_01', 6)	# 7-12
    sprite('ha611_02', 6)	# 13-18
    sprite('ha611_03', 6)	# 19-24
    sprite('ha611_04', 6)	# 25-30
    sprite('ha611_05', 7)	# 31-37
    sprite('ha611_06', 7)	# 38-44
    sprite('ha611_07', 7)	# 45-51
    sprite('ha611_08', 7)	# 52-58
    sprite('ha611_09', 7)	# 59-65
    sprite('ha611_10', 7)	# 66-72
    sprite('ha611_11', 7)	# 73-79
    label(0)
    sprite('ha611_12', 8)	# 80-87
    sprite('ha611_13', 8)	# 88-95
    sprite('ha611_14', 8)	# 96-103
    loopRest()
    gotoLabel(0)

@State
def Act2Event_havstb_01():
    sprite('ha611_04', 6)	# 1-6
    sprite('ha611_03', 6)	# 7-12
    sprite('ha611_02', 6)	# 13-18
    sprite('ha611_01', 6)	# 19-24
    sprite('ha611_00', 6)	# 25-30
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_phvsha_00():
    sprite('ha450_05', 10)	# 1-10
    sprite('ha450_06', 3)	# 11-13
    GFX_0('ha_AH', -1)
    sprite('ha450_07', 3)	# 14-16
    SFX_3('hase_21')
    ScreenShake(30000, 60000)
    Unknown8000(0, 1, 1)
    sprite('ha450_08', 3)	# 17-19
    sprite('ha450_09', 3)	# 20-22
    sprite('ha450_10', 4)	# 23-26
    SFX_3('hase_21')
    sprite('ha450_11', 4)	# 27-30
    sprite('ha450_12', 4)	# 31-34
    sprite('ha450_13', 4)	# 35-38
    SFX_3('hase_21')
    sprite('ha450_14', 4)	# 39-42
    sprite('ha450_15', 4)	# 43-46
    sprite('ha450_16', 4)	# 47-50
    sprite('ha450_17', 4)	# 51-54
    sprite('ha450_18', 4)	# 55-58
    sprite('ha450_19', 5)	# 59-63
    sprite('ha450_20', 5)	# 64-68
    sprite('ha450_21', 5)	# 69-73
    sprite('ha450_22', 5)	# 74-78
    sprite('ha450_23', 5)	# 79-83
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_muvsha_00():

    def upon_IMMEDIATE():
        Unknown1000(-200000)
    sprite('keep', 1)	# 1-1
    loopRest()
    enterState('Act2Event_Yoin')

@State
def Act2Event_SlashFinish():
    sprite('ha202_00', 2)	# 1-2
    Unknown2019(-500)
    DisableAttackRestOfMove()
    sprite('ha202_01', 2)	# 3-4
    sprite('ha202_02', 4)	# 5-8
    sprite('ha202_03', 2)	# 9-10
    sprite('ha202_04', 2)	# 11-12
    sprite('ha202_05', 4)	# 13-16
    sprite('ha202_06', 1)	# 17-17
    sprite('ha202_07', 12)	# 18-29	 **attackbox here**
    sprite('ha202_08', 1)	# 30-30
    sprite('ha202_09', 2)	# 31-32
    sprite('ha202_10', 3)	# 33-35
    sprite('ha202_11', 3)	# 36-38
    sprite('ha202_12', 3)	# 39-41
    sprite('ha202_13', 2)	# 42-43
    sprite('ha202_14', 2)	# 44-45
    sprite('ha202_15', 2)	# 46-47
    sprite('ha202_16', 2)	# 48-49
    loopRest()
    enterState('CmnActStand')

@State
def Act2EventEntryWait_tgvsha():
    sprite('null', 1)	# 1-1
    Unknown21007(22, 32)
    sprite('null', 2)	# 2-3
    enterState('Act2Event_Entry')
    loopRest()

@State
def Act2EventBattle_tgvsha():

    def upon_IMMEDIATE():
        Unknown23022(1)
        teleportRelativeX(67000)
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
    sprite('keep', 15)	# 1-15
    sprite('ha401_00', 3)	# 16-18
    callSubroutine('SpecialChainCancel_Land')
    SFX_3('hase_25')
    sprite('ha401_01', 3)	# 19-21
    Unknown3029(1)
    Unknown3069(0)
    physicsXImpulse(500)
    sprite('ha401_02', 3)	# 22-24
    sprite('ha401_03', 3)	# 25-27
    sprite('ha401_04', 3)	# 28-30
    physicsXImpulse(0)
    SFX_0('004_swing_grap_1_1')
    sprite('ha401_05', 4)	# 31-34	 **attackbox here**
    sprite('ha401_06', 5)	# 35-39
    sprite('ha401_07', 4)	# 40-43
    sprite('ha401_08', 4)	# 44-47
    sprite('ha401_09', 5)	# 48-52
    sprite('ha404_00', 4)	# 53-56
    Unknown1000(-193000)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    AttackLevel_(4)
    RefreshMultihit()
    sendToLabelUpon(2, 1)
    callSubroutine('SpecialChainCancel_Air')
    physicsYImpulse(600)
    setGravity(50)
    SFX_3('hase_25')
    sprite('ha404_01', 2)	# 57-58
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha404_02', 2)	# 59-60
    sprite('ha404_03', 2)	# 61-62
    sprite('ha404_04', 1)	# 63-63
    sprite('ha404_05', 1)	# 64-64
    sprite('ha404_06', 1)	# 65-65
    sprite('ha404_07', 1)	# 66-66
    sprite('ha404_08', 2)	# 67-68
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha404_09', 3)	# 69-71	 **attackbox here**
    physicsXImpulse(0)
    physicsYImpulse(0)
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 72-73
    sprite('ha404_11', 2)	# 74-75
    sprite('ha404_12', 2)	# 76-77
    Unknown3029(0)
    Unknown2001()
    Unknown14077(1)
    sprite('ha404_13', 3)	# 78-80
    Unknown1043()
    sprite('ha404_14', 3)	# 81-83
    sprite('ha404_15', 3)	# 84-86
    sprite('ha404_16', 3)	# 87-89
    label(0)
    sprite('ha020_03', 4)	# 90-93
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha024_00', 3)	# 94-96
    Unknown8000(0, 1, 1)
    clearUponHandler(2)
    sprite('ha024_01', 3)	# 97-99
    sprite('ha024_02', 3)	# 100-102
    sprite('ha024_03', 3)	# 103-105
    sprite('ha024_04', 3)	# 106-108
    sprite('ha430_00', 2)	# 109-110
    callSubroutine('SpecialChainCancel_Land')
    sprite('ha430_00', 2)	# 111-112
    sprite('ha430_01', 3)	# 113-115
    sprite('ha430_02', 2)	# 116-117
    sprite('ha430_02', 1)	# 118-118
    sprite('ha430_03', 2)	# 119-120
    sprite('ha430_04', 2)	# 121-122
    sprite('ha430_05', 2)	# 123-124
    sprite('ha430_06', 2)	# 125-126
    sprite('ha430_07', 2)	# 127-128
    sprite('ha430_08', 2)	# 129-130
    sprite('ha430_09', 2)	# 131-132
    sprite('ha430_10', 2)	# 133-134
    sprite('ha430_11', 2)	# 135-136
    sprite('ha430_12', 2)	# 137-138
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 2)	# 139-140
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 2)	# 141-142
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_15', 2)	# 143-144
    GFX_1('haef_DD_1_ring', 0)
    physicsXImpulse(8500)
    sprite('ha430_16', 2)	# 145-146
    SFX_0('006_swing_blade_2')
    sprite('ha430_16', 2)	# 147-148
    sprite('ha430_17', 4)	# 149-152
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('011_spin_0')
    sprite('ha430_18', 4)	# 153-156	 **attackbox here**
    GFX_0('ha430_col_dmy', 100)
    SFX_3('hase_20')
    ScreenShake(0, 16000)
    GFX_1('haef_DD_1_blast', 0)
    Unknown2015(200)
    physicsXImpulse(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21007(9, 32)
        clearUponHandler(10)
    GFX_0('ha_DD_1_shot', 0)
    Unknown38(9, 1)
    sprite('ha430_19', 5)	# 157-161
    sprite('ha430_20', 5)	# 162-166
    sprite('ha430_21', 5)	# 167-171
    sprite('ha430_22', 5)	# 172-176
    sprite('ha430_23', 5)	# 177-181
    Unknown14077(1)
    Unknown2015(-1)
    sprite('ha430_24', 4)	# 182-185
    sprite('ha430_25', 4)	# 186-189
    sprite('ha430_26', 4)	# 190-193
    sprite('ha430_27', 4)	# 194-197
    loopRest()
    enterState('Act2Event_Semuke')

@State
def Act2Event_Battou():
    sprite('ha610_10', 6)	# 1-6
    SFX_3('hase_22')
    sprite('ha610_09', 6)	# 7-12
    sprite('ha610_08', 6)	# 13-18
    sprite('ha610_07', 6)	# 19-24
    sprite('ha610_06', 6)	# 25-30
    sprite('ha610_05', 6)	# 31-36
    sprite('ha610_04', 6)	# 37-42
    sprite('ha610_03', 6)	# 43-48
    sprite('ha610_02', 6)	# 49-54
    sprite('ha610_01', 6)	# 55-60
    sprite('ha610_00', 6)	# 61-66

@State
def Act3Event_ntvsha_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
        Unknown1000(-900000)
        Unknown3029(1)
        Unknown3069(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_19 <= 420000):
                Unknown21007(22, 33)
                physicsXImpulse(0)
                setGravity(0)
                clearUponHandler(3)
                sendToLabel(1)
    sprite('ha400_03', 4)	# 1-4
    SFX_0('004_swing_grap_1_2')
    SFX_0('005_swing_grap_2_1')
    physicsXImpulse(42000)
    sprite('ha400_04', 3)	# 5-7
    sprite('ha400_05', 32767)	# 8-32774	 **attackbox here**
    label(1)
    sprite('ha400_05', 10)	# 32775-32784	 **attackbox here**
    teleportRelativeX(5000)
    sprite('ha400_06', 3)	# 32785-32787
    teleportRelativeX(5000)
    SFX_0('208_brake_normal')
    Recovery()
    sprite('ha400_07', 3)	# 32788-32790
    sprite('ha400_08', 3)	# 32791-32793
    Unknown3029(0)
    Unknown14077(1)
    sprite('ha400_09', 3)	# 32794-32796
    sprite('ha400_10', 3)	# 32797-32799
    SFX_3('hase_22')
    enterState('CmnActStand')

@State
def Act3Event_ntvsha_01():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 5)
    sprite('ha450_00', 5)	# 1-5
    sprite('ha450_01', 5)	# 6-10
    sprite('ha450_02', 5)	# 11-15
    sprite('ha450_03', 5)	# 16-20
    sprite('ha450_04', 5)	# 21-25
    sprite('ha450_05', 58)	# 26-83
    sprite('ha450_05', 110)	# 84-193
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 130)	# 194-323
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 130)	# 324-453
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    Unknown2037(16)
    label(1)
    sprite('ha450_05', 10)	# 454-463
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    Unknown2037(16)
    label(2)
    sprite('ha450_05', 10)	# 464-473
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(2)
    Unknown2037(13)
    label(3)
    sprite('ha450_05', 10)	# 474-483
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(3)
    Unknown2037(9)
    label(4)
    sprite('ha450_05', 10)	# 484-493
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(4)
    label(5)
    sprite('ha450_06', 6)	# 494-499
    clearUponHandler(32)
    GFX_0('ha_AH', -1)
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_07', 6)	# 500-505
    SFX_0('019_cloth_a')
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_08', 6)	# 506-511
    SFX_0('019_cloth_a')
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_09', 6)	# 512-517
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_10', 6)	# 518-523
    ScreenShake(0, 60000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_11', 6)	# 524-529
    sprite('ha450_12', 6)	# 530-535
    sprite('ha450_13', 6)	# 536-541
    sprite('ha450_14', 6)	# 542-547
    sprite('ha450_15', 6)	# 548-553
    sprite('ha450_16', 6)	# 554-559
    sprite('ha450_17', 6)	# 560-565
    sprite('ha450_18', 6)	# 566-571
    sprite('ha450_19', 6)	# 572-577
    sprite('ha450_20', 6)	# 578-583
    sprite('ha450_21', 6)	# 584-589
    sprite('ha450_22', 6)	# 590-595
    sprite('ha450_23', 6)	# 596-601
    loopRest()
    sprite('ha450_23', 2)	# 602-603
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ntvsha_02():
    sprite('keep', 2)	# 1-2
    teleportRelativeX(50000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_ntvsha_03():
    sprite('ha430_00', 5)	# 1-5
    sprite('ha430_01', 4)	# 6-9
    sprite('ha430_02', 5)	# 10-14
    sprite('ha430_03', 3)	# 15-17
    sprite('ha430_04', 3)	# 18-20
    sprite('ha430_05', 3)	# 21-23
    sprite('ha430_06', 3)	# 24-26
    sprite('ha430_07', 3)	# 27-29
    sprite('ha430_08', 3)	# 30-32
    sprite('ha430_09', 3)	# 33-35
    sprite('ha430_10', 3)	# 36-38
    sprite('ha430_11', 4)	# 39-42
    sprite('ha430_12', 4)	# 43-46
    SFX_0('302_spsys_drivemotion')
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 4)	# 47-50
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 51-54
    GFX_0('ha_DD_1_aura', 0)
    label(99)
    sprite('ha430_13', 4)	# 55-58
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 59-62
    gotoLabel(99)

@State
def Act3Event_ntvsha_04():
    sprite('ha430_13', 4)	# 1-4
    Unknown21007(22, 32)
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 5-8
    sprite('ha430_15', 4)	# 9-12
    GFX_1('haef_DD_1_ring', 0)
    physicsXImpulse(5000)
    sprite('ha430_16', 2)	# 13-14
    SFX_0('006_swing_blade_2')
    sprite('ha430_16', 2)	# 15-16
    sprite('ha430_17', 4)	# 17-20
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('011_spin_0')
    sprite('ha430_18', 4)	# 21-24	 **attackbox here**
    GFX_0('ha430_col_dmy', 100)
    SFX_3('hase_20')
    ScreenShake(0, 16000)
    GFX_1('haef_DD_1_blast', 0)
    Unknown2015(200)
    physicsXImpulse(0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown21007(9, 32)
        clearUponHandler(10)
    GFX_0('ha_DD_1_shot', 0)
    Unknown38(9, 1)
    sprite('ha430_19', 5)	# 25-29
    sprite('ha430_20', 5)	# 30-34
    sprite('ha430_21', 5)	# 35-39
    sprite('ha430_22', 5)	# 40-44
    sprite('ha430_23', 5)	# 45-49
    sprite('ha430_24', 4)	# 50-53
    sprite('ha430_25', 4)	# 54-57
    sprite('ha430_26', 4)	# 58-61
    sprite('ha430_27', 4)	# 62-65
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_havsno_00():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown23022(1)
    sprite('ha431_00', 4)	# 1-4
    Unknown3029(1)
    Unknown3069(0)
    Unknown3071(20)
    Unknown3070(10)
    sprite('ha431_01', 4)	# 5-8
    sprite('ha431_02', 4)	# 9-12
    sprite('ha431_03', 4)	# 13-16
    sprite('ha431_04', 4)	# 17-20
    sprite('ha431_05', 4)	# 21-24
    sprite('ha431_06', 4)	# 25-28
    sprite('ha431_07', 4)	# 29-32
    sprite('ha431_08', 3)	# 33-35
    sprite('ha431_09', 3)	# 36-38
    sprite('ha431_10', 3)	# 39-41
    sprite('ha431_11', 3)	# 42-44
    sprite('ha431_12', 3)	# 45-47
    sprite('ha431_13', 3)	# 48-50
    sprite('ha431_14', 3)	# 51-53
    sprite('ha431_15', 3)	# 54-56
    sprite('ha431_16', 3)	# 57-59	 **attackbox here**
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_3('hase_24')
    GFX_1('haef_DD_2', 0)
    ScreenShake(0, 16000)
    Unknown3029(0)
    teleportRelativeX(1696000)
    sprite('ha431_16', 3)	# 60-62	 **attackbox here**
    Unknown21007(22, 32)
    GFX_0('Act3Event_havsno_01', 0)
    sprite('ha431_16', 3)	# 63-65	 **attackbox here**
    sprite('ha431_16', 3)	# 66-68	 **attackbox here**
    sprite('ha431_16', 3)	# 69-71	 **attackbox here**
    loopRest()
    label(0)
    sprite('ha431_17', 20)	# 72-91
    sprite('ha431_18', 3)	# 92-94
    sprite('ha431_19', 3)	# 95-97
    sprite('ha431_20', 3)	# 98-100
    sprite('ha431_21', 3)	# 101-103
    sprite('ha431_22', 3)	# 104-106
    sprite('ha431_23', 3)	# 107-109
    sprite('ha431_24', 3)	# 110-112
    sprite('ha431_25', 3)	# 113-115
    sprite('ha431_26', 3)	# 116-118
    sprite('ha431_27', 3)	# 119-121
    sprite('ha431_28', 3)	# 122-124
    sprite('ha431_29', 2)	# 125-126
    sprite('ha000_00', 1)	# 127-127
    Unknown2005()
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_havsvh_00():

    def upon_IMMEDIATE():
        EnableCollision(0)
        Unknown23022(1)
        sendToLabelUpon(2, 1)
    sprite('ha404_00', 4)	# 1-4
    Unknown1000(-60000)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    physicsYImpulse(600)
    setGravity(50)
    sprite('ha404_01', 2)	# 5-6
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha404_02', 2)	# 7-8
    sprite('ha404_03', 2)	# 9-10
    sprite('ha404_04', 1)	# 11-11
    sprite('ha404_05', 1)	# 12-12
    sprite('ha404_06', 1)	# 13-13
    sprite('ha404_07', 1)	# 14-14
    sprite('ha404_08', 2)	# 15-16
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha404_09', 3)	# 17-19	 **attackbox here**
    Unknown21007(22, 32)
    physicsXImpulse(0)
    physicsYImpulse(0)
    GFX_0('ha_404', -1)
    sprite('ha404_10', 2)	# 20-21
    sprite('ha404_11', 2)	# 22-23
    sprite('ha404_12', 2)	# 24-25
    Unknown3029(0)
    Unknown2001()
    Unknown14077(1)
    sprite('ha404_13', 3)	# 26-28
    Unknown1043()
    sprite('ha404_14', 3)	# 29-31
    sprite('ha404_15', 3)	# 32-34
    sprite('ha404_16', 3)	# 35-37
    label(0)
    sprite('ha020_03', 4)	# 38-41
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ha024_00', 3)	# 42-44
    Unknown8000(0, 1, 1)
    clearUponHandler(2)
    sprite('ha024_01', 3)	# 45-47
    sprite('ha024_02', 3)	# 48-50
    sprite('ha024_03', 3)	# 51-53
    sprite('ha024_04', 3)	# 54-56
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_havsvh_01():
    sprite('keep', 2)	# 1-2
    sprite('ha451_47', 6)	# 3-8
    Unknown2005()
    teleportRelativeX(120000)
    sprite('ha451_46', 6)	# 9-14
    sprite('ha451_45', 6)	# 15-20
    sprite('ha451_44', 6)	# 21-26
    sprite('ha451_43', 6)	# 27-32
    sprite('ha451_22', 8)	# 33-40
    sprite('ha451_22', 8)	# 41-48
    sprite('ha451_23', 8)	# 49-56
    sprite('ha451_24', 8)	# 57-64
    sprite('ha451_25', 8)	# 65-72
    sprite('ha451_26', 8)	# 73-80
    sprite('ha451_27', 8)	# 81-88
    sprite('ha451_28', 6)	# 89-94
    sprite('ha451_29', 6)	# 95-100
    sprite('ha451_30', 6)	# 101-106
    sprite('ha451_31', 6)	# 107-112
    sprite('ha451_32', 30)	# 113-142
    sprite('ha451_33', 2)	# 143-144
    sprite('ha451_34', 15)	# 145-159
    SFX_3('hase_00')
    sprite('ha451_36', 6)	# 160-165
    sprite('ha451_37', 6)	# 166-171
    sprite('ha451_38', 6)	# 172-177
    sprite('ha451_39', 6)	# 178-183
    sprite('ha451_40', 6)	# 184-189
    sprite('ha451_41', 6)	# 190-195
    sprite('ha451_42', 6)	# 196-201
    label(0)
    sprite('ha451_39', 6)	# 202-207
    sprite('ha451_40', 6)	# 208-213
    sprite('ha451_41', 6)	# 214-219
    sprite('ha451_42', 6)	# 220-225
    loopRest()
    gotoLabel(0)

@State
def Act3Event_havsvh_04():
    sprite('ha450_05', 40)	# 1-40
    sprite('ha450_05', 110)	# 41-150
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 100)	# 151-250
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    sprite('ha450_05', 60)	# 251-310
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_0')
    Unknown2037(4)
    label(1)
    sprite('ha450_05', 10)	# 311-320
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    Unknown2037(4)
    label(2)
    sprite('ha450_05', 10)	# 321-330
    ScreenShake(0, 1000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(2)
    Unknown2037(4)
    label(3)
    sprite('ha450_05', 10)	# 331-340
    ScreenShake(0, 4000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(3)
    Unknown2037(4)
    label(4)
    sprite('ha450_05', 10)	# 341-350
    ScreenShake(0, 6000)
    SFX_0('019_quake_0')
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(4)
    sprite('ha450_06', 6)	# 351-356
    GFX_0('ha_AH', -1)
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_07', 6)	# 357-362
    SFX_0('019_cloth_a')
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_08', 6)	# 363-368
    SFX_0('019_cloth_a')
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_09', 6)	# 369-374
    ScreenShake(0, 10000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_10', 6)	# 375-380
    ScreenShake(0, 60000)
    SFX_0('019_quake_0')
    SFX_0('019_quake_1')
    sprite('ha450_11', 6)	# 381-386
    sprite('ha450_12', 6)	# 387-392
    sprite('ha450_13', 6)	# 393-398
    sprite('ha450_14', 6)	# 399-404
    sprite('ha450_15', 6)	# 405-410
    sprite('ha450_16', 6)	# 411-416
    sprite('ha450_17', 6)	# 417-422
    sprite('ha450_18', 6)	# 423-428
    sprite('ha450_19', 6)	# 429-434
    sprite('ha450_20', 6)	# 435-440
    sprite('ha450_21', 6)	# 441-446
    sprite('ha450_22', 6)	# 447-452
    sprite('ha450_23', 6)	# 453-458
    loopRest()
    sprite('ha450_23', 2)	# 459-460
    loopRest()
    enterState('CmnActStand')

@State
def EventCrouch():
    label(0)
    sprite('ha010_02', 6)	# 1-6
    sprite('ha010_03', 6)	# 7-12
    sprite('ha010_04', 6)	# 13-18
    sprite('ha010_05', 6)	# 19-24
    sprite('ha010_06', 6)	# 25-30
    sprite('ha010_07', 6)	# 31-36
    sprite('ha010_08', 6)	# 37-42
    sprite('ha010_09', 6)	# 43-48
    sprite('ha010_10', 6)	# 49-54
    sprite('ha010_11', 6)	# 55-60
    sprite('ha010_12', 6)	# 61-66
    sprite('ha010_13', 6)	# 67-72
    loopRest()
    gotoLabel(0)

@State
def Act3Event_nyvsha_00():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(32, 1)
        Unknown2004(1, 0)
    sprite('ha010_01', 4)	# 1-4
    sprite('ha010_00', 4)	# 5-8
    sprite('ha430_00', 3)	# 9-11
    sprite('ha430_00', 3)	# 12-14
    sprite('ha430_01', 3)	# 15-17
    sprite('ha430_02', 3)	# 18-20
    sprite('ha430_02', 3)	# 21-23
    Unknown2036(47, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_HA', -1)
    sprite('ha430_03', 3)	# 24-26
    sprite('ha430_04', 3)	# 27-29
    sprite('ha430_05', 3)	# 30-32
    sprite('ha430_06', 3)	# 33-35
    sprite('ha430_07', 3)	# 36-38
    sprite('ha430_08', 3)	# 39-41
    sprite('ha430_09', 3)	# 42-44
    sprite('ha430_10', 3)	# 45-47
    sprite('ha430_11', 3)	# 48-50
    sprite('ha430_12', 3)	# 51-53
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    sprite('ha430_13', 4)	# 54-57
    GFX_0('ha_DD_1_aura', 0)
    sprite('ha430_14', 4)	# 58-61
    GFX_0('ha_DD_1_aura', 0)
    GFX_1('haef_DD_1_ring', 0)
    GFX_1('haef_DD_1_ring', 0)
    label(0)
    sprite('ha430_15', 4)	# 62-65
    GFX_1('haef_DD_1_ring', 0)
    physicsXImpulse(5000)
    sprite('ha430_16', 2)	# 66-67
    SFX_0('006_swing_blade_2')
    sprite('ha430_16', 2)	# 68-69
    sprite('ha430_17', 4)	# 70-73
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    SFX_0('011_spin_0')
    sprite('ha430_18', 4)	# 74-77	 **attackbox here**
    SFX_3('hase_20')
    ScreenShake(0, 16000)
    GFX_1('haef_DD_1_blast', 0)
    physicsXImpulse(0)
    GFX_0('Act3Event_ha_DD_1_shot', 0)
    Unknown21007(22, 32)
    sprite('ha430_19', 5)	# 78-82
    sprite('ha430_20', 5)	# 83-87
    sprite('ha430_21', 5)	# 88-92
    sprite('ha430_22', 5)	# 93-97
    sprite('ha430_23', 5)	# 98-102
    Unknown2015(-1)
    Unknown23024(0)
    sprite('ha430_24', 4)	# 103-106
    sprite('ha430_25', 4)	# 107-110
    sprite('ha430_26', 4)	# 111-114
    sprite('ha430_27', 4)	# 115-118
    loopRest()
    label(2)
    sprite('ha000_00', 7)	# 119-125
    sprite('ha000_01', 7)	# 126-132
    sprite('ha000_02', 7)	# 133-139
    sprite('ha000_03', 7)	# 140-146
    sprite('ha000_04', 7)	# 147-153
    sprite('ha000_05', 7)	# 154-160
    sprite('ha000_06', 7)	# 161-167
    sprite('ha000_07', 7)	# 168-174
    sprite('ha000_08', 7)	# 175-181
    sprite('ha000_09', 7)	# 182-188
    sprite('ha000_10', 7)	# 189-195
    sprite('ha000_11', 7)	# 196-202
    loopRest()
    gotoLabel(2)
    label(1)
    sprite('null', 32767)	# 203-32969
    Unknown3038(1)

@State
def Act3Event_amvsha_00():

    def upon_IMMEDIATE():
        Unknown23022(1)
        sendToLabelUpon(32, 0)
        Unknown1000(-360000)
    sprite('ha402_00', 2)	# 1-2
    sprite('ha402_01', 2)	# 3-4
    Unknown3029(1)
    Unknown3069(0)
    sprite('ha402_02', 2)	# 5-6
    sprite('ha402_03', 2)	# 7-8
    physicsXImpulse(10000)
    sprite('ha402_04', 4)	# 9-12
    sprite('ha402_05', 4)	# 13-16
    sprite('ha402_06', 4)	# 17-20
    physicsXImpulse(0)
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha402_07', 16)	# 21-36	 **attackbox here**
    GFX_0('ha402_col_dmy', 0)
    GFX_0('ha_402a', -1)
    sprite('ha402_08', 2)	# 37-38
    sprite('ha402_09', 2)	# 39-40
    sprite('ha402_10', 2)	# 41-42
    sprite('ha402_11', 2)	# 43-44
    physicsXImpulse(12000)
    sprite('ha402_12', 2)	# 45-46
    sprite('ha402_13', 2)	# 47-48
    sprite('ha402_14', 2)	# 49-50
    SFX_0('006_swing_blade_2')
    SFX_0('006_swing_blade_1')
    sprite('ha402_15', 16)	# 51-66	 **attackbox here**
    physicsXImpulse(0)
    GFX_0('ha_402b', -1)
    sprite('ha402_16', 4)	# 67-70
    sprite('ha402_17', 4)	# 71-74
    sprite('ha402_18', 4)	# 75-78
    sprite('ha402_19', 3)	# 79-81
    sprite('ha402_20', 3)	# 82-84
    label(0)
    sprite('ha040_00', 3)	# 85-87
    sprite('ha040_01', 3)	# 88-90
    Unknown1047(-15000)
    SFX_0('104_guard_grap_1')
    ScreenShake(3000, 18000)
    sprite('ha040_02', 3)	# 91-93
    sprite('ha040_03', 20)	# 94-113
    sprite('ha040_02', 3)	# 114-116
    sprite('ha040_01', 3)	# 117-119
    sprite('ha040_00', 3)	# 120-122
    Unknown3029(0)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_izvsha_00():
    sprite('ha450_18', 4)	# 1-4
    sprite('ha450_19', 5)	# 5-9
    sprite('ha450_20', 5)	# 10-14
    sprite('ha450_21', 5)	# 15-19
    sprite('ha450_22', 5)	# 20-24
    sprite('ha450_23', 5)	# 25-29
    sprite('ha611_00', 6)	# 30-35
    sprite('ha611_01', 6)	# 36-41
    sprite('ha611_02', 6)	# 42-47
    sprite('ha611_03', 6)	# 48-53
    sprite('ha611_04', 6)	# 54-59
    sprite('ha611_05', 7)	# 60-66
    sprite('ha611_06', 60)	# 67-126
    sprite('ha611_07', 7)	# 127-133
    sprite('ha611_08', 7)	# 134-140
    sprite('ha611_09', 7)	# 141-147
    sprite('ha611_10', 7)	# 148-154
    sprite('ha611_11', 7)	# 155-161
    label(0)
    sprite('ha611_12', 8)	# 162-169
    sprite('ha611_13', 8)	# 170-177
    sprite('ha611_14', 8)	# 178-185
    loopRest()
    gotoLabel(0)