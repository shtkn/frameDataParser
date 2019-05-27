@Subroutine
def PreInit():
    Unknown12019('706e6100000000000000000000000000')

@Subroutine
def MatchInit():
    Health(14000)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('KamaeCancel', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0x5f)
    Move_EndRegister()
    Move_Register('KamaeEX', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xda)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown14015(2000, 452000, -117000, 143000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(-3000, 204000, -91000, 127000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A2nd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4A3rd', 0x6)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4A4th', 0x1)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Move_Input_(0x5e)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('NmlAtk5A4th')
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown15012(100)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    Unknown15009()
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(-67000, 467000, -81000, 212000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    MoveMaxChainRepeat(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(66000, 621000, -58000, 218000, 500, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(20000, 430000, -219000, -66000, 1000, 10)
    Unknown15014(0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(-10000, 400000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 300000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    MoveMaxChainRepeat(3)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2ndex', 0x22)
    Unknown14005(1)
    MoveMaxChainRepeat(3)
    Unknown14013('NmlAtkAIR5A2nd')
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(-1000, 446000, -434000, -51000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(233000, 767000, -143000, 150000, 100, 50)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(16000, 130000, -112000, 132000, 100, 10)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(16000, 130000, -112000, 132000, 100, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rdEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('NmlAtk5A3rd')
    Unknown14027('NmlAtk5A3rd')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk5A4thEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('NmlAtk5A4th')
    Unknown14027('NmlAtk5A4th')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk5BEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('NmlAtk5B')
    Unknown14027('NmlAtk5B')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk2BEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Move_Input_(0x45)
    Unknown14013('NmlAtk2B')
    Unknown14027('NmlAtk2B')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttackEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('CmnActCrushAttack')
    Unknown14027('CmnActCrushAttack')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtk2CEx', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Move_Input_(0x45)
    Unknown14013('NmlAtk2C')
    Unknown14027('NmlAtk2C')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtkThrowEX', 0x1)
    Move_Input_(0xd3)
    Unknown14005(1)
    Unknown14013('NmlAtkThrow')
    Unknown14027('NmlAtkThrow')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AN_NmlAtkBackThrowEX', 0x1)
    Move_Input_(0xd3)
    Unknown14005(1)
    Unknown14013('NmlAtkBackThrow')
    Unknown14027('NmlAtkBackThrow')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('KamaeA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('KamaeCancelA_EX', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('KamaeCancelcheck')
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('ShagekiA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x1)
    Unknown14015(507000, 1466000, -223000, 355000, 2000, 50)
    Unknown15016(0, 100, 1000)
    Move_EndRegister()
    Move_Register('ShagekiB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xa)
    Unknown14015(507000, 1466000, 77000, 655000, 100, 50)
    Unknown15016(1, 100, 1000)
    Move_EndRegister()
    Move_Register('ShagekiC', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0x13)
    Unknown14015(507000, 1466000, 77000, 655000, 100, 50)
    Unknown15016(2, 100, 1000)
    Move_EndRegister()
    Move_Register('BanditRevolverB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-90000, 666000, -207000, 285000, 100, 50)
    Move_EndRegister()
    Move_Register('WalkingShotEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(7000, 1466000, -123000, 255000, 1000, 50)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('WalkingShotKickEX', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(-173000, 286000, -123000, 255000, 1000, 50)
    Unknown15014(3000)
    Move_EndRegister()
    Move_Register('TrapA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('TrapB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('TrapEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('AirBanditRevolverA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-3000, 560000, -158000, 170000, 100, 50)
    Move_EndRegister()
    Move_Register('AirBanditRevolverB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-90000, 666000, -207000, 285000, 100, 50)
    Move_EndRegister()
    Move_Register('AirBanditRevolverEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(310000, 1066000, -207000, 285000, 100, 50)
    Move_EndRegister()
    Move_Register('AirTrapA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('AirTrapB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('AirTrapEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(707000, 1466000, -223000, 355000, 10, 10)
    Move_EndRegister()
    Move_Register('BanditRevolverB_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14013('BanditRevolverB')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('WalkingShotEX_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14013('WalkingShotEX')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('TrapA_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14013('TrapA')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('TrapB_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14013('TrapB')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('TrapEX_EX', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14005(1)
    Unknown14013('TrapEX')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(-3000, 204000, -91000, 127000, 100, 10)
    Move_EndRegister()
    Move_Register('SecretGunA', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 200, 50)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('SecretGunB', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 10, 10)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('SecretGunOD', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(307000, 1466000, -223000, 355000, 10, 10)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('UltimateKill', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown14015(342000, 861000, -198000, 116000, 10, 10)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('UltimateKillOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown14015(342000, 861000, -198000, 116000, 10, 10)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('UltimateKillAir', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown14015(233000, 1007000, -143000, 150000, 100, 50)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('UltimateKillAirOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15000(0)
    Unknown14015(233000, 1007000, -143000, 150000, 100, 50)
    Unknown15022('030000000500000032000000e8030000')
    Move_EndRegister()
    Move_Register('SecretGunB_EX', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('SecretGunB')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('SecretGunOD_EX', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('SecretGunOD')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('UltimateKill_EX', 0x68)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('UltimateKill')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('UltimateKillOD_EX', 0x68)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14005(1)
    Unknown14013('UltimateKillOD')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4A2nd', 10000000)
    Unknown15024('NmlAtk4A2nd', 'NmlAtk4A3rd', 10000000)
    Unknown15024('NmlAtk4A3rd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown7010(0, 'pna000')
    Unknown7010(1, 'pna001')
    Unknown7010(2, 'pna002')
    Unknown7010(3, 'pna003')
    Unknown7010(4, 'pna004')
    Unknown7010(5, 'pna005')
    Unknown7010(6, 'pna006')
    Unknown7010(7, 'pna007')
    Unknown7010(8, 'pna008')
    Unknown7010(9, 'pna009')
    Unknown7010(10, 'pna010')
    Unknown7010(15, 'pna015')
    Unknown7010(16, 'pna016')
    Unknown7010(17, 'pna017')
    Unknown7010(18, 'pna018')
    Unknown7010(19, 'pna019')
    Unknown7010(20, 'pna020')
    Unknown7010(21, 'pna021')
    Unknown7010(22, 'pna022')
    Unknown7010(23, 'pna023')
    Unknown7010(24, 'pna024')
    Unknown7010(25, 'pna025')
    Unknown7010(28, 'pna028')
    Unknown7010(29, 'pna029')
    Unknown7010(30, 'pna030')
    Unknown7010(31, 'pna031')
    Unknown7010(32, 'pna032')
    Unknown7010(33, 'pna033')
    Unknown7010(34, 'pna034')
    Unknown7010(35, 'pna035')
    Unknown7010(36, 'pna036')
    Unknown7010(37, 'pna037')
    Unknown7010(39, 'pna039')
    Unknown7010(42, 'pna042')
    Unknown7010(43, 'pna043')
    Unknown7010(44, 'pna044')
    Unknown7010(45, 'pna045')
    Unknown7010(46, 'pna046')
    Unknown7010(47, 'pna047')
    Unknown7010(48, 'pna048')
    Unknown7010(49, 'pna049')
    Unknown7010(50, 'pna050')
    Unknown7010(52, 'pna052')
    Unknown7010(53, 'pna053')
    Unknown7010(54, 'pna100_0')
    Unknown7010(55, 'pna100_1')
    Unknown7010(56, 'pna100_2')
    Unknown7010(63, 'pna101_0')
    Unknown7010(64, 'pna101_1')
    Unknown7010(65, 'pna101_2')
    Unknown7010(57, 'pna102_0')
    Unknown7010(58, 'pna102_1')
    Unknown7010(59, 'pna102_2')
    Unknown7010(66, 'pna103_0')
    Unknown7010(67, 'pna103_1')
    Unknown7010(68, 'pna103_2')
    Unknown7010(60, 'pna104_0')
    Unknown7010(61, 'pna104_1')
    Unknown7010(62, 'pna104_2')
    Unknown7010(69, 'pna105_0')
    Unknown7010(70, 'pna105_1')
    Unknown7010(71, 'pna105_2')
    Unknown7010(72, 'pna150')
    Unknown7010(73, 'pna151')
    Unknown7010(74, 'pna152')
    Unknown7010(85, 'pna153')
    Unknown7010(87, 'pna154')
    Unknown7010(88, 'pna155')
    Unknown7010(96, 'pna161_0')
    Unknown7010(97, 'pna161_1')
    Unknown7010(92, 'pna162_0')
    Unknown7010(93, 'pna162_1')
    Unknown7010(98, 'pna163_0')
    Unknown7010(99, 'pna163_1')
    Unknown7010(100, 'pna164_0')
    Unknown7010(101, 'pna164_1')
    Unknown7010(105, 'pna165_0')
    Unknown7010(106, 'pna165_1')
    Unknown7010(102, 'pna166_0')
    Unknown7010(103, 'pna166_1')
    Unknown7010(90, 'pna167_0')
    Unknown7010(91, 'pna167_1')
    Unknown7010(107, 'pna168_0')
    Unknown7010(108, 'pna168_1')
    Unknown7010(110, 'pna169_0')
    Unknown7010(111, 'pna169_1')
    Unknown7010(94, 'pna400_0')
    Unknown7010(95, 'pna400_1')
    Unknown12018(0, 'na060_00')
    Unknown12018(1, 'na060_01')
    Unknown12018(2, 'na060_02')
    Unknown12018(3, 'na060_03')
    Unknown12018(4, 'na060_04')
    Unknown12018(5, 'na060_05')
    Unknown12018(6, 'na060_06')
    Unknown12018(7, 'na041_02')
    Unknown12018(8, 'na040_02')
    Unknown12018(9, 'na045_02')
    Unknown12018(10, 'na060_00')
    Unknown12018(11, 'na060_01')
    Unknown12018(12, 'na060_03')
    Unknown12018(13, 'na060_05')
    Unknown12018(14, 'na060_07')
    Unknown12018(15, 'na125_00')
    Unknown12018(16, 'na050_00')
    Unknown12018(17, 'na052_00')
    Unknown12018(18, 'na054_00')
    Unknown12018(25, 'na063_00')
    Unknown12018(26, 'na063_01')
    Unknown12018(27, 'na063_02')
    Unknown12018(28, 'na063_05')
    Unknown12018(29, 'na060_12')
    Unknown12018(24, 'na072_03')
    Unknown30036('504e415f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown23003(0, 1, 1, 1, 300, 0, -49152, -65281)
    Unknown23008(0, 0)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('0200000053656372657447756e4100000000000000000000000000000000000000000000')
    Unknown12059('0300000053656372657447756e4f44000000000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174654b696c6c0000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174654b696c6c4f44000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnMainEnemyComboBreak():
    SLOT_4 = 0
    SLOT_5 = 0
    Unknown48('19000000020000000400000016000000020000005f000000')
    SLOT_4 = (SLOT_4 + 1)
    if (SLOT_4 == 1):
        if (SLOT_63 == 1):
            SLOT_63 = 2
            SLOT_5 = 1
    if (SLOT_4 == 2):
        if (SLOT_64 == 1):
            SLOT_64 = 2
            SLOT_5 = 1
    if (SLOT_4 == 3):
        if (SLOT_65 == 1):
            SLOT_65 = 2
            SLOT_5 = 1
    if (SLOT_4 == 4):
        if (SLOT_66 == 1):
            SLOT_66 = 2
            SLOT_5 = 1
    if SLOT_5:
        Unknown48('19000000020000002000000016000000020000004b000000')
        if SLOT_32:
            if (not Unknown46(10)):
                if (SLOT_95 == 0):
                    GFX_0('destinyzero_Cutin_main1_3Naoto', 1)
                    Unknown38(9, 1)
                    GFX_0('destinyzero_Cutin_main1_3dokuro', 1)
                if (SLOT_95 == 2):
                    GFX_0('destinyzero_Cutin_main1_3Naoto', 1)
                    Unknown38(9, 1)
                    GFX_0('destinyzero_Cutin_main1_3dokuro', 1)
                if (SLOT_95 == 1):
                    GFX_0('destinyzero_Cutin_main2_4Naoto', 1)
                    Unknown38(9, 1)
                    GFX_0('destinyzero_Cutin_main2_4dokuro', 1)
                if (SLOT_95 == 3):
                    GFX_0('destinyzero_Cutin_main2_4Naoto', 1)
                    Unknown38(9, 1)
                    GFX_0('destinyzero_Cutin_main2_4dokuro', 1)
                Unknown7007('706e613330365f30000000000000000064000000706e613330365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            GFX_0('destinyzero_main', -1)

@Subroutine
def OnSubEnemyComboBreak():
    SLOT_4 = 0
    SLOT_5 = 0
    Unknown48('19000000020000000400000017000000020000005f000000')
    SLOT_4 = (SLOT_4 + 1)
    if (SLOT_4 == 1):
        if (SLOT_63 == 1):
            SLOT_63 = 2
            SLOT_5 = 1
    if (SLOT_4 == 2):
        if (SLOT_64 == 1):
            SLOT_64 = 2
            SLOT_5 = 1
    if (SLOT_4 == 3):
        if (SLOT_65 == 1):
            SLOT_65 = 2
            SLOT_5 = 1
    if (SLOT_4 == 4):
        if (SLOT_66 == 1):
            SLOT_66 = 2
            SLOT_5 = 1
    if SLOT_5:
        Unknown48('19000000020000002100000017000000020000004b000000')
        if SLOT_33:
            if (not Unknown46(9)):
                if (SLOT_95 == 0):
                    GFX_0('destinyzero_Cutin_sub1_3Naoto', 1)
                    Unknown38(10, 1)
                    GFX_0('destinyzero_Cutin_sub1_3dokuro', 1)
                if (SLOT_95 == 2):
                    GFX_0('destinyzero_Cutin_sub1_3Naoto', 1)
                    Unknown38(10, 1)
                    GFX_0('destinyzero_Cutin_sub1_3dokuro', 1)
                if (SLOT_95 == 1):
                    GFX_0('destinyzero_Cutin_sub2_4Naoto', 1)
                    Unknown38(10, 1)
                    GFX_0('destinyzero_Cutin_sub2_4dokuro', 1)
                if (SLOT_95 == 3):
                    GFX_0('destinyzero_Cutin_sub2_4Naoto', 1)
                    Unknown38(10, 1)
                    GFX_0('destinyzero_Cutin_sub2_4dokuro', 1)
                Unknown7007('706e613330365f30000000000000000064000000706e613330365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            GFX_0('destinyzero_sub', -1)

@Subroutine
def OnFrameStep():
    SLOT_6 = 0
    if SLOT_158:
        Unknown48('19000000020000000700000016000000020000005f000000')
        SLOT_7 = (SLOT_7 + 1)
        if (SLOT_7 == 1):
            if (SLOT_63 == 2):
                SLOT_6 = 1
        if (SLOT_7 == 2):
            if (SLOT_64 == 2):
                SLOT_6 = 1
        if (SLOT_7 == 3):
            if (SLOT_65 == 2):
                SLOT_6 = 1
        if (SLOT_7 == 4):
            if (SLOT_66 == 2):
                SLOT_6 = 1
    if (not SLOT_81):
        if SLOT_90:
            Unknown58('TRI_PNADeathFlg', 2, 67)
            if (SLOT_67 == 1):
                SLOT_6 = 0
                SLOT_63 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_66 = 0
            if (SLOT_67 == 2):
                SLOT_6 = 1
                SLOT_63 = 2
                SLOT_64 = 2
                SLOT_65 = 2
                SLOT_66 = 2
        if SLOT_122:
            Unknown58('TRI_PNADeathFlg', 2, 67)
            if (SLOT_67 == 1):
                SLOT_6 = 0
                SLOT_63 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_66 = 0
            if (SLOT_67 == 2):
                SLOT_6 = 1
                SLOT_63 = 2
                SLOT_64 = 2
                SLOT_65 = 2
                SLOT_66 = 2
        if SLOT_123:
            Unknown58('TRI_PNADeathFlg', 2, 67)
            if (SLOT_67 == 1):
                SLOT_6 = 0
                SLOT_63 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_66 = 0
            if (SLOT_67 == 2):
                SLOT_6 = 1
                SLOT_63 = 2
                SLOT_64 = 2
                SLOT_65 = 2
                SLOT_66 = 2
    if SLOT_170:
        SLOT_6 = 0
    if SLOT_9:
        if (not SLOT_30):
            Unknown2017(0)
        else:
            SLOT_9 = 0

@Subroutine
def HaikyouEx0():
    if SLOT_59:
        SLOT_59 = (SLOT_59 + (-1))
        GFX_0('Yakkyo', 0)

@Subroutine
def ShagekiFlexChain():
    WhiffCancel('ShagekiA')
    WhiffCancel('ShagekiB')
    WhiffCancel('ShagekiC')
    WhiffCancel('KamaeCancel')
    WhiffCancel('KamaeEX')

@Subroutine
def SpecialCancelmanagement_DeriveI():
    Unknown14070('BanditRevolverB_EX')
    Unknown14070('WalkingShotEX_EX')
    Unknown14070('TrapA_EX')
    Unknown14070('TrapB_EX')
    Unknown14070('TrapEX_EX')
    Unknown14070('SecretGunB_EX')
    Unknown14070('SecretGunOD_EX')
    Unknown14070('UltimateKill_EX')
    Unknown14070('UltimateKillOD_EX')

@Subroutine
def SpecialCancelmanagement_DeriveT():
    Unknown14072('BanditRevolverB_EX')
    Unknown14072('WalkingShotEX_EX')
    Unknown14072('TrapA_EX')
    Unknown14072('TrapB_EX')
    Unknown14072('TrapEX_EX')
    Unknown14072('SecretGunB_EX')
    Unknown14072('SecretGunOD_EX')
    Unknown14072('UltimateKill_EX')
    Unknown14072('UltimateKillOD_EX')

@Subroutine
def SpecialCancelmanagement_DeriveC():
    Unknown14074('BanditRevolverB_EX')
    Unknown14074('WalkingShotEX_EX')
    Unknown14074('TrapA_EX')
    Unknown14074('TrapB_EX')
    Unknown14074('TrapEX_EX')
    Unknown14074('SecretGunB_EX')
    Unknown14074('SecretGunOD_EX')
    Unknown14074('UltimateKill_EX')
    Unknown14074('UltimateKillOD_EX')

@Subroutine
def KamaeCancelcheck():
    SLOT_47 = 1
    if Unknown23145('BanditRevolverB'):
        SLOT_47 = 0

@Subroutine
def Shot_Stack():
    Unknown23029(5, 3002, 0)
    if Unknown46(4):
        Unknown38(5, 4)

@Subroutine
def Shot_Stack2():
    Unknown23029(8, 3003, 0)
    if Unknown46(7):
        Unknown38(8, 7)

@State
def CmnActStand():
    label(0)
    sprite('na000_00', 6)	# 1-6
    sprite('na000_01', 6)	# 7-12
    sprite('na000_02', 6)	# 13-18
    sprite('na000_03', 6)	# 19-24
    sprite('na000_04', 6)	# 25-30
    sprite('na000_05', 6)	# 31-36
    sprite('na000_06', 6)	# 37-42
    sprite('na000_07', 6)	# 43-48
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('na001_00', 7)	# 49-55
    SLOT_88 = 960
    SFX_1('pna000')
    sprite('na001_01', 7)	# 56-62
    sprite('na001_02', 7)	# 63-69
    sprite('na001_03', 10)	# 70-79
    sprite('na001_04', 7)	# 80-86
    sprite('na001_05', 7)	# 87-93
    sprite('na001_06', 10)	# 94-103
    sprite('na001_01', 7)	# 104-110
    sprite('na001_00', 7)	# 111-117
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('na003_00', 4)	# 1-4
    sprite('na003_01', 4)	# 5-8
    sprite('na003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('na010_00', 4)	# 1-4
    sprite('na010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('na010_02', 6)	# 1-6
    sprite('na010_03', 6)	# 7-12
    sprite('na010_04', 6)	# 13-18
    sprite('na010_05', 6)	# 19-24
    sprite('na010_06', 6)	# 25-30
    sprite('na010_07', 6)	# 31-36
    sprite('na010_08', 6)	# 37-42
    sprite('na010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('na013_00', 4)	# 1-4
    sprite('na013_01', 4)	# 5-8
    sprite('na013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('na010_01', 4)	# 1-4
    sprite('na010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    if SLOT_37:
        if SLOT_93:
            if SLOT_16:
                Unknown1045(15000)
    sprite('na010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('na020_00', 4)	# 1-4
    sprite('na020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('na020_02', 3)	# 1-3
    sprite('na020_03', 3)	# 4-6
    sprite('na020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('na020_05', 3)	# 1-3
    sprite('na020_06', 3)	# 4-6
    label(0)
    sprite('na020_07', 4)	# 7-10
    sprite('na020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('na010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('na211_00', 2)	# 1-2
    sprite('na211_01', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('na211_01', 3)	# 1-3
    sprite('na211_00', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('na030_00', 5)	# 1-5
    sprite('na030_01', 5)	# 6-10
    label(0)
    sprite('na030_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na030_03', 5)	# 16-20
    sprite('na030_04', 5)	# 21-25
    sprite('na030_05', 5)	# 26-30
    sprite('na030_06', 5)	# 31-35
    sprite('na030_07', 5)	# 36-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na030_08', 5)	# 41-45
    sprite('na030_09', 5)	# 46-50
    sprite('na030_10', 5)	# 51-55
    sprite('na030_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)
    sprite('na030_00', 3)	# 61-63

@State
def CmnActBWalk():
    sprite('na031_00', 6)	# 1-6
    sprite('na031_01', 6)	# 7-12
    label(0)
    sprite('na031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na031_03', 6)	# 19-24
    sprite('na031_04', 6)	# 25-30
    sprite('na031_05', 6)	# 31-36
    sprite('na031_06', 6)	# 37-42
    sprite('na031_07', 6)	# 43-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na031_08', 6)	# 49-54
    sprite('na031_09', 6)	# 55-60
    sprite('na031_10', 6)	# 61-66
    sprite('na031_11', 6)	# 67-72
    loopRest()
    gotoLabel(0)
    sprite('na031_00', 3)	# 73-75

@State
def CmnActFDash():
    sprite('na030_00', 4)	# 1-4
    sprite('na032_00', 2)	# 5-6
    label(0)
    sprite('na032_01', 4)	# 7-10
    sprite('na032_02', 4)	# 11-14
    sprite('na032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('na032_04', 4)	# 19-22
    sprite('na032_05', 4)	# 23-26
    sprite('na032_06', 4)	# 27-30
    sprite('na032_07', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('na032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('na032_09', 4)	# 1-4
    sprite('na032_10', 4)	# 5-8

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('na033_00', 2)	# 1-2
    sprite('na033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('na033_02', 3)	# 6-8
    sprite('na033_01', 3)	# 9-11
    sprite('na033_02', 3)	# 12-14
    label(0)
    sprite('na033_01', 3)	# 15-17
    sprite('na033_02', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('na033_03', 3)	# 21-23
    setInvincible(0)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('na033_04', 3)	# 24-26

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('na025_02', 1)	# 1-1
    Unknown2005()
    sprite('na025_01', 2)	# 2-3
    sprite('na025_02', 1)	# 4-4
    Unknown2005()

@State
def CmnActAirFDash():
    sprite('na035_00', 3)	# 1-3
    label(0)
    sprite('na035_01', 3)	# 4-6
    sprite('na035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    sprite('na035_00', 4)	# 10-13

@State
def CmnActAirBDash():
    sprite('na033_00', 2)	# 1-2
    physicsYImpulse(12000)
    sprite('na033_02', 3)	# 3-5
    sprite('na033_01', 3)	# 6-8
    sprite('na033_02', 3)	# 9-11
    sprite('na033_01', 3)	# 12-14
    sprite('na033_02', 3)	# 15-17
    sprite('na033_01', 3)	# 18-20
    sprite('na033_02', 3)	# 21-23
    sprite('na020_05', 3)	# 24-26
    sprite('na020_06', 3)	# 27-29
    label(0)
    sprite('na020_07', 4)	# 30-33
    sprite('na020_08', 4)	# 34-37
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('na050_00', 1)	# 1-1
    sprite('na050_01', 1)	# 2-2
    sprite('na050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('na050_01', 1)	# 1-1
    sprite('na050_02', 1)	# 2-2
    sprite('na050_01', 2)	# 3-4
    sprite('na050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('na050_02', 1)	# 1-1
    sprite('na050_03', 1)	# 2-2
    sprite('na050_02', 2)	# 3-4
    sprite('na050_01', 2)	# 5-6
    sprite('na050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('na050_03', 1)	# 1-1
    sprite('na050_04', 1)	# 2-2
    sprite('na050_03', 2)	# 3-4
    sprite('na050_02', 2)	# 5-6
    sprite('na050_01', 2)	# 7-8
    sprite('na050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('na050_04', 1)	# 1-1
    sprite('na050_04', 1)	# 2-2
    sprite('na050_04', 2)	# 3-4
    sprite('na050_03', 2)	# 5-6
    sprite('na050_02', 2)	# 7-8
    sprite('na050_01', 2)	# 9-10
    sprite('na050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('na052_00', 1)	# 1-1
    sprite('na052_01', 1)	# 2-2
    sprite('na052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('na052_01', 1)	# 1-1
    sprite('na052_02', 1)	# 2-2
    sprite('na052_01', 2)	# 3-4
    sprite('na052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('na052_02', 1)	# 1-1
    sprite('na052_03', 1)	# 2-2
    sprite('na052_02', 2)	# 3-4
    sprite('na052_01', 2)	# 5-6
    sprite('na052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('na052_03', 1)	# 1-1
    sprite('na052_04', 1)	# 2-2
    sprite('na052_03', 2)	# 3-4
    sprite('na052_02', 2)	# 5-6
    sprite('na052_01', 2)	# 7-8
    sprite('na052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('na052_04', 1)	# 1-1
    sprite('na052_04', 1)	# 2-2
    sprite('na052_04', 2)	# 3-4
    sprite('na052_03', 2)	# 5-6
    sprite('na052_02', 2)	# 7-8
    sprite('na052_01', 2)	# 9-10
    sprite('na052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('na054_00', 1)	# 1-1
    sprite('na054_01', 1)	# 2-2
    sprite('na054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('na054_01', 1)	# 1-1
    sprite('na054_02', 1)	# 2-2
    sprite('na054_01', 2)	# 3-4
    sprite('na054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('na054_02', 1)	# 1-1
    sprite('na054_03', 1)	# 2-2
    sprite('na054_02', 2)	# 3-4
    sprite('na054_01', 2)	# 5-6
    sprite('na054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('na054_03', 1)	# 1-1
    sprite('na054_04', 1)	# 2-2
    sprite('na054_03', 2)	# 3-4
    sprite('na054_02', 2)	# 5-6
    sprite('na054_01', 2)	# 7-8
    sprite('na054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('na054_04', 1)	# 1-1
    sprite('na054_04', 1)	# 2-2
    sprite('na054_04', 2)	# 3-4
    sprite('na054_03', 2)	# 5-6
    sprite('na054_02', 2)	# 7-8
    sprite('na054_01', 2)	# 9-10
    sprite('na054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('na060_00', 4)	# 1-4
    label(0)
    sprite('na060_01', 4)	# 5-8
    sprite('na060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('na060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('na060_04', 8)	# 1-8
    label(1)
    sprite('na060_05', 4)	# 9-12
    sprite('na060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('na063_05', 6)	# 1-6

@State
def CmnActBDownBound():
    sprite('na060_08', 2)	# 1-2
    sprite('na060_09', 2)	# 3-4
    sprite('na060_10', 2)	# 5-6
    sprite('na060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('na060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('na064_00', 6)	# 1-6
    sprite('na064_01', 6)	# 7-12
    sprite('na064_02', 6)	# 13-18
    sprite('na064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('na063_00', 4)	# 1-4

@State
def CmnActFDownUpperEnd():
    sprite('na063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(1)
    sprite('na063_03', 4)	# 1-4
    sprite('na063_04', 4)	# 5-8
    loopRest()
    gotoLabel(1)

@State
def CmnActFDownCrash():
    sprite('na063_05', 4)	# 1-4

@State
def CmnActFDownBound():
    sprite('na060_08', 2)	# 1-2
    sprite('na060_09', 2)	# 3-4
    sprite('na060_10', 2)	# 5-6
    sprite('na060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('na060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('na064_00', 4)	# 1-4
    sprite('na064_01', 4)	# 5-8
    sprite('na064_02', 4)	# 9-12
    sprite('na064_03', 4)	# 13-16

@State
def CmnActVDownUpper():
    sprite('na060_00', 4)	# 1-4
    label(0)
    sprite('na060_01', 4)	# 5-8
    sprite('na060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('na060_03', 4)	# 1-4
    sprite('na060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('na060_04', 8)	# 1-8
    label(0)
    sprite('na060_05', 4)	# 9-12
    sprite('na060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('na060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('na072_00', 3)	# 1-3
    label(0)
    sprite('na072_01', 3)	# 4-6
    sprite('na072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('na074_00', 2)	# 1-2
    sprite('na074_01', 2)	# 3-4
    sprite('na074_02', 2)	# 5-6
    sprite('na074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('na072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('na063_00', 3)	# 1-3
    label(0)
    sprite('na063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('na082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('na052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('na070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('na070_01', 4)	# 1-4
    sprite('na070_02', 4)	# 5-8
    sprite('na070_03', 4)	# 9-12
    sprite('na070_04', 4)	# 13-16
    sprite('na070_05', 4)	# 17-20
    sprite('na070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('na040_03', 2)	# 1-2
    sprite('na040_02', 2)	# 3-4
    sprite('na040_01', 2)	# 5-6
    sprite('na040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('na020_02', 3)	# 1-3
    sprite('na020_03', 3)	# 4-6
    sprite('na020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('na020_02', 3)	# 1-3
    sprite('na020_03', 3)	# 4-6
    sprite('na020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('na020_02', 3)	# 1-3
    sprite('na020_03', 3)	# 4-6
    sprite('na020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('na112_00', 3)	# 1-3
    sprite('na112_01', 3)	# 4-6
    sprite('na112_02', 3)	# 7-9
    sprite('na112_03', 3)	# 10-12
    sprite('na112_04', 3)	# 13-15
    sprite('na112_05', 3)	# 16-18
    sprite('na020_07', 4)	# 19-22
    sprite('na020_08', 4)	# 23-26
    sprite('na020_07', 4)	# 27-30
    sprite('na020_08', 4)	# 31-34

@State
def CmnActUkemiLandF():
    sprite('na112_00', 3)	# 1-3
    sprite('na112_01', 3)	# 4-6
    sprite('na112_02', 3)	# 7-9
    sprite('na112_03', 3)	# 10-12
    sprite('na112_04', 3)	# 13-15
    sprite('na112_05', 3)	# 16-18
    sprite('na020_07', 4)	# 19-22
    sprite('na020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('na112_00', 3)	# 1-3
    sprite('na112_01', 3)	# 4-6
    sprite('na112_02', 3)	# 7-9
    sprite('na112_03', 3)	# 10-12
    sprite('na112_04', 3)	# 13-15
    sprite('na112_05', 3)	# 16-18
    sprite('na020_07', 4)	# 19-22
    sprite('na020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('na010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('na040_00', 3)	# 1-3
    sprite('na040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('na040_02', 5)	# 1-5
    sprite('na040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('na040_01', 3)	# 1-3
    sprite('na040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('na040_04', 1)	# 1-1
    label(0)
    sprite('na040_02', 5)	# 2-6
    sprite('na040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('na040_01', 3)	# 1-3
    sprite('na040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('na040_00', 3)	# 1-3
    sprite('na040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('na040_02', 5)	# 1-5
    sprite('na040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('na040_01', 3)	# 1-3
    sprite('na040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('na040_04', 1)	# 1-1
    label(0)
    sprite('na040_02', 5)	# 2-6
    sprite('na040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('na040_01', 3)	# 1-3
    sprite('na040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('na043_00', 3)	# 1-3
    sprite('na043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('na043_02', 5)	# 1-5
    sprite('na043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('na043_01', 3)	# 1-3
    sprite('na043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('na043_04', 1)	# 1-1
    label(0)
    sprite('na043_02', 5)	# 2-6
    sprite('na043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('na043_01', 3)	# 1-3
    sprite('na043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('na045_00', 3)	# 1-3
    sprite('na045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('na045_02', 5)	# 1-5
    sprite('na045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('na045_01', 3)	# 1-3
    sprite('na045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('na045_04', 1)	# 1-1
    label(0)
    sprite('na045_02', 5)	# 2-6
    sprite('na045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('na045_01', 3)	# 1-3
    sprite('na045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('na040_04', 2)	# 1-2
    sprite('na040_04', 2)	# 3-4
    sprite('na040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('na040_02', 4)	# 6-9
    sprite('na040_01', 4)	# 10-13
    sprite('na040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    pass

@State
def CmnActGuardBreakAir():
    pass

@State
def CmnActLockWait():
    sprite('na040_04', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('na200_00', 4)	# 1-4
    sprite('na200_01', 5)	# 5-9
    sprite('na200_02', 11)	# 10-20	 **attackbox here**
    RefreshMultihit()
    sprite('na200_03', 3)	# 21-23
    sprite('na200_04', 3)	# 24-26
    sprite('na200_05', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('na045_02', 1)	# 1-1
    sprite('na045_01', 3)	# 2-4
    sprite('na045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('na251_00', 3)	# 1-3
    sprite('na251_01', 3)	# 4-6
    sprite('na251_03', 3)	# 7-9	 **attackbox here**
    sprite('na251_03', 7)	# 10-16	 **attackbox here**
    Unknown23027()
    sprite('na251_04', 5)	# 17-21
    sprite('na251_05', 4)	# 22-25
    Unknown2001()

@State
def CmnActLandSpin():
    sprite('na071_00', 2)	# 1-2
    label(0)
    sprite('na071_01', 2)	# 3-4
    sprite('na071_02', 2)	# 5-6
    sprite('na071_03', 2)	# 7-8
    sprite('na071_04', 2)	# 9-10
    sprite('na071_05', 2)	# 11-12
    sprite('na071_06', 2)	# 13-14
    sprite('na071_07', 2)	# 15-16
    sprite('na071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('na040_02', 3)	# 1-3
    sprite('na040_01', 3)	# 4-6
    sprite('na040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('na071_00', 2)	# 1-2
    label(0)
    sprite('na071_01', 2)	# 3-4
    sprite('na071_02', 2)	# 5-6
    sprite('na071_03', 2)	# 7-8
    sprite('na071_04', 2)	# 9-10
    sprite('na071_05', 2)	# 11-12
    sprite('na071_06', 2)	# 13-14
    sprite('na071_07', 2)	# 15-16
    sprite('na071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('na124_00', 2)	# 1-2
    label(0)
    sprite('na124_01', 2)	# 3-4
    sprite('na124_02', 2)	# 5-6
    sprite('na124_03', 2)	# 7-8
    sprite('na124_04', 2)	# 9-10
    sprite('na124_05', 2)	# 11-12
    sprite('na124_06', 2)	# 13-14
    sprite('na124_07', 2)	# 15-16
    sprite('na124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('na077_02', 4)	# 1-4
    label(0)
    sprite('na077_03', 3)	# 5-7
    sprite('na077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('na077_05', 5)	# 1-5
    sprite('na077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    pass

@State
def CmnActAomukeSlideEnd():
    pass

@State
def CmnActBurstBegin():
    pass

@State
def CmnActBurstLoop():
    pass

@State
def CmnActBurstEnd():
    pass

@State
def CmnActAirBurstBegin():
    pass

@State
def CmnActAirBurstLoop():
    pass

@State
def CmnActAirBurstEnd():
    pass

@State
def CmnActOverDriveBegin():
    sprite('na121_00', 2)	# 1-2
    sprite('na121_01', 2)	# 3-4
    sprite('na121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('na121_02', 1)	# 7-7
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('na121_03', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('na121_04', 2)	# 4-5
    sprite('na121_05', 2)	# 6-7
    sprite('na121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActOverDriveEnd():
    sprite('na121_07', 6)	# 1-6
    sprite('na010_00', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('na121_00', 2)	# 1-2
    sprite('na121_01', 2)	# 3-4
    sprite('na121_02', 2)	# 5-6
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    sprite('na121_02', 1)	# 7-7
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('na121_03', 3)	# 1-3
    label(1)
    sprite('na121_04', 2)	# 4-5
    sprite('na121_05', 2)	# 6-7
    sprite('na121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirOverDriveEnd():
    sprite('na121_07', 2)	# 1-2
    sprite('na121_08', 2)	# 3-4
    sprite('na020_04', 3)	# 5-7
    sprite('na020_05', 3)	# 8-10
    sprite('na020_06', 2)	# 11-12
    label(0)
    sprite('na020_07', 4)	# 13-16
    sprite('na020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        pass
    sprite('na121_00', 3)	# 1-3
    sprite('na121_01', 3)	# 4-6
    sprite('na121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    Unknown36(28)
    Unknown23148('PNA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 3017, 0)
    sprite('na121_02', 32767)	# 10-32776
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('na121_03', 3)	# 1-3
    label(0)
    sprite('na121_04', 2)	# 4-5
    sprite('na121_05', 2)	# 6-7
    sprite('na121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('na121_07', 6)	# 1-6
    sprite('na010_00', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        pass
    sprite('na121_00', 3)	# 1-3
    sprite('na121_01', 3)	# 4-6
    sprite('na121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    Unknown36(28)
    Unknown23148('PNA_PersonaWait')
    Unknown48('030000000200000033000000190000000200000000000000')
    Unknown35()
    if (not SLOT_51):
        Unknown23029(11, 3017, 0)
    sprite('na121_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('na121_03', 3)	# 1-3
    label(0)
    sprite('na121_04', 2)	# 4-5
    sprite('na121_05', 2)	# 6-7
    sprite('na121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('na121_07', 6)	# 1-6
    sprite('na121_08', 6)	# 7-12
    sprite('na020_04', 3)	# 13-15
    sprite('na020_05', 3)	# 16-18
    sprite('na020_06', 3)	# 19-21
    label(0)
    sprite('na020_07', 4)	# 22-25
    sprite('na020_08', 4)	# 26-29
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PNA_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 3017, 0)
    sprite('na121_00', 3)	# 1-3
    sprite('na121_01', 3)	# 4-6
    sprite('na121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('na121_02', 32767)	# 10-32776
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('na121_03', 3)	# 1-3
    label(0)
    sprite('na121_04', 2)	# 4-5
    sprite('na121_05', 2)	# 6-7
    sprite('na121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('na121_07', 6)	# 1-6
    sprite('na121_08', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PNA_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 3017, 0)
    sprite('na121_00', 3)	# 1-3
    sprite('na121_01', 3)	# 4-6
    sprite('na121_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('na121_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('na121_03', 3)	# 1-3
    label(0)
    sprite('na121_04', 2)	# 4-5
    sprite('na121_05', 2)	# 6-7
    sprite('na121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('na121_07', 6)	# 1-6
    sprite('na121_08', 6)	# 7-12
    sprite('na020_04', 3)	# 13-15
    sprite('na020_05', 3)	# 16-18
    sprite('na020_06', 3)	# 19-21
    label(0)
    sprite('na020_07', 4)	# 22-25
    sprite('na020_08', 4)	# 26-29
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
    label(0)
    sprite('null', 1)	# 1-1
    gotoLabel(0)

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('na000_00', 20)	# 1-20

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('na000_00', 20)	# 1-20

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('na407_09', 3)	# 26-28
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    label(1)
    sprite('na407_09', 3)	# 29-31
    sprite('na407_09', 3)	# 32-34
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('na407_10', 3)	# 35-37	 **attackbox here**
    sprite('na407_11ex', 2)	# 38-39
    Unknown8000(100, 1, 1)
    sprite('na211_00', 3)	# 40-42
    Unknown18009(1)
    sprite('na211_01', 17)	# 43-59

@State
def CmnActChangePartnerQuickIn():
    sprite('na032_05', 3)	# 1-3
    sprite('na032_06', 5)	# 4-8
    sprite('na032_09', 7)	# 9-15
    sprite('na032_09', 7)	# 16-22
    sprite('na032_10', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('na033_01', 3)	# 1-3
    sprite('na033_02', 3)	# 4-6
    sprite('na033_01', 3)	# 7-9
    sprite('na033_02', 3)	# 10-12
    sprite('na033_01', 3)	# 13-15
    sprite('na033_02', 3)	# 16-18
    sprite('na033_01', 3)	# 19-21
    sprite('na033_02', 3)	# 22-24
    sprite('na033_01', 3)	# 25-27
    sprite('na033_02', 3)	# 28-30
    sprite('na033_01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('na033_00', 1)	# 1-1
    sprite('na033_01', 4)	# 2-5
    sprite('na033_02', 4)	# 6-9
    loopRest()
    label(0)
    sprite('na033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('na033_03', 3)	# 13-15
    sprite('na033_04', 3)	# 16-18

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('na611_00', 4)	# 1-4
    sprite('na611_01', 4)	# 5-8
    sprite('na611_02', 4)	# 9-12
    sprite('na611_03', 4)	# 13-16
    sprite('na611_04', 4)	# 17-20
    sprite('na611_05', 11)	# 21-31
    sprite('na611_06', 6)	# 32-37
    sprite('na611_07', 7)	# 38-44
    sprite('na611_08', 6)	# 45-50
    sprite('na611_09', 6)	# 51-56
    sprite('na611_10', 4)	# 57-60
    sprite('na611_09', 4)	# 61-64
    sprite('na611_08', 4)	# 65-68
    sprite('na611_07', 4)	# 69-72
    sprite('na611_06', 4)	# 73-76

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
    sprite('na020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('na020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('na010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown1084(1)
        SLOT_60 = 5
        SLOT_61 = 0
        Unknown11063(1)
        Unknown14083(0)
        Unknown30068(1)
    sprite('na401_00', 3)	# 1-3
    sprite('na401_01', 1)	# 4-4
    sprite('na401_01', 1)	# 5-5
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 6-6
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 7-7
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 8-8
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 9-9
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 10-10
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 11-11
    sprite('na401_03', 27)	# 12-38
    sprite('na401_03', 2)	# 39-40
    loopRest()
    gotoLabel(16)
    label(16)
    (SLOT_60 <= 1)
    if SLOT_0:
        _gotolabel(17)
    sprite('na401_52', 1)	# 41-41
    sprite('na404_00', 2)	# 42-43
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('Dangan_PS', 1)
    Unknown23029(1, 3010, 0)
    SFX_3('na001')
    sprite('na404_01', 2)	# 44-45
    sprite('na404_00', 1)	# 46-46
    sendToLabel(16)
    sprite('na404_00', 3)	# 47-49
    sprite('na401_03', 3)	# 50-52
    sprite('na401_03', 3)	# 53-55
    WhiffCancelEnable(0)
    sprite('na401_03', 32767)	# 56-32822
    enterState('KamaeBase')
    loopRest()
    ExitState()
    label(17)
    sprite('na404_00', 1)	# 32823-32823
    sprite('na404_00', 2)	# 32824-32825
    GFX_0('DanganLastA_PS', 1)
    Unknown7007('706e613230375f30000000000000000064000000706e613230375f31000000000000000064000000706e613230375f320000000000000000640000000000000000000000000000000000000000000000')
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    SFX_3('na002')
    sprite('na404_02', 6)	# 32826-32831
    sprite('na404_03', 6)	# 32832-32837
    sprite('na404_04', 14)	# 32838-32851
    sprite('na404_05', 7)	# 32852-32858
    sprite('na404_06', 6)	# 32859-32864
    sprite('na401_03', 3)	# 32865-32867
    enterState('KamaeCancel')
    loopRest()

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('na410_00', 5)	# 1-5
    sprite('na410_01', 4)	# 6-9
    sprite('na410_01', 1)	# 10-10
    Unknown23029(11, 402, 0)
    GFX_1('persona_enter_ply', 0)
    tag_voice(1, 'pna217_0', 'pna217_1', 'pna217_2', '')
    sprite('na410_02', 4)	# 11-14
    sprite('na410_03', 4)	# 15-18
    sprite('na410_02', 4)	# 19-22
    sprite('na410_03', 4)	# 23-26
    sprite('na410_02', 4)	# 27-30
    sprite('na410_03', 4)	# 31-34
    sprite('na410_02', 4)	# 35-38
    Recovery()
    sprite('na410_03', 4)	# 39-42
    sprite('na410_02', 4)	# 43-46
    sprite('na410_03', 4)	# 47-50
    sprite('na410_02', 4)	# 51-54
    sprite('na410_03', 4)	# 55-58
    sprite('na410_02', 4)	# 59-62
    sprite('na410_03', 4)	# 63-66
    sprite('na410_02', 4)	# 67-70
    sprite('na410_03', 4)	# 71-74
    sprite('na410_02', 4)	# 75-78
    sprite('na410_03', 4)	# 79-82
    sprite('na410_04', 6)	# 83-88

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_10 = 0
        Unknown11042(1)

        def upon_43():
            if (SLOT_48 == 3020):
                Recovery()
    sprite('na205_00', 2)	# 1-2
    sprite('na205_01', 2)	# 3-4
    sprite('na205_02', 2)	# 5-6
    clearUponHandler(3)
    sprite('na205_02', 2)	# 7-8
    Unknown23029(11, 405, 0)
    Unknown7007('706e613132305f30000000000000000064000000706e613132305f31000000000000000064000000706e613132305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na205_03', 3)	# 9-11
    GFX_1('persona_enter_ply', 0)
    sprite('na205_04', 3)	# 12-14
    Unknown14077(0)
    JumpCancel_(0)
    sprite('na205_05', 4)	# 15-18
    sprite('na205_01', 3)	# 19-21
    sprite('na403_00', 3)	# 22-24
    sprite('na403_01', 2)	# 25-26
    physicsXImpulse(35000)
    sprite('na403_02', 1)	# 27-27
    Unknown1019(160)
    sprite('na403_03', 1)	# 28-28
    sprite('na403_04', 2)	# 29-30
    sprite('na403_05', 2)	# 31-32
    sprite('na403_06', 1)	# 33-33
    sprite('na403_06', 1)	# 34-34
    Unknown1084(1)
    Unknown1045(32000)
    sprite('na403_07', 1)	# 35-35
    callSubroutine('HaikyouEx0')
    sprite('na403_08', 1)	# 36-36
    Unknown2017(1)
    callSubroutine('HaikyouEx0')
    sprite('na403_09', 1)	# 37-37
    Unknown2006()
    sprite('na403_09', 1)	# 38-38
    sprite('na403_09', 1)	# 39-39
    callSubroutine('HaikyouEx0')
    sprite('na403_10', 1)	# 40-40
    callSubroutine('HaikyouEx0')
    sprite('na403_10', 1)	# 41-41
    sprite('na403_11', 1)	# 42-42
    callSubroutine('HaikyouEx0')
    setInvincible(0)
    Unknown1051(50)
    sprite('na403_11', 1)	# 43-43
    callSubroutine('HaikyouEx0')
    sprite('na403_12', 1)	# 44-44
    sprite('na401_03', 20)	# 45-64
    if SLOT_10:
        SLOT_10 = 0

        def upon_3():
            if (SLOT_20 < 400000):
                clearUponHandler(3)
                sendToLabel(0)
    else:
        Recovery()
    loopRest()
    sprite('na401_02', 5)	# 65-69
    Unknown1084(1)
    sprite('na401_01', 1)	# 70-70
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 71-71
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 72-72
    sprite('na401_01', 1)	# 73-73
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 74-74
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 75-75
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 76-76
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 77-77
    ExitState()
    label(0)
    sprite('na404_00', 1)	# 78-78
    Unknown2016(450)
    sprite('na404_02', 6)	# 79-84
    GFX_0('DanganD_Ex', 1)
    Unknown7007('706e613130355f30000000000000000064000000706e613130355f31000000000000000064000000706e613130355f320000000000000000640000000000000000000000000000000000000000000000')
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    SFX_3('na002')
    sprite('na404_03', 6)	# 85-90
    sprite('na404_04', 14)	# 91-104
    Recovery()
    sprite('na404_05', 7)	# 105-111
    sprite('na401_00', 1)	# 112-112
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 113-113
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 114-114
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 3)	# 115-117

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
    Unknown2036(103, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-290000)
    Unknown1019(4)
    label(0)
    sprite('na020_07', 4)	# 3-6
    Unknown1019(103)
    sprite('na020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateWalkingShotKickOD')
    else:
        enterState('UltimateWalkingShotKick')

@State
def UltimateWalkingShotKick():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        Unknown11091(100)
        AttackP2(100)
        Hitstop(30)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(70)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(40)
        Unknown9178(3)
        Unknown9346(0)
        Unknown9215()
        AirPushbackX(550000)
        AirPushbackY(40000)
        Unknown11068(1)
        Unknown11069('UltimateWalkingShotKick')

        def upon_12():
            ScreenShake(50000, 0)
        Unknown13024(0)
        setInvincible(1)
    sprite('na433_13', 4)	# 1-4
    sprite('na433_14', 4)	# 5-8
    sprite('na433_15', 10)	# 9-18
    sprite('na433_15', 10)	# 19-28
    ScreenShake(5000, 0)
    sprite('na433_15', 10)	# 29-38
    ScreenShake(7500, 0)
    sprite('na433_15', 10)	# 39-48
    ScreenShake(10000, 0)
    sprite('na433_15', 10)	# 49-58
    ScreenShake(12500, 0)
    sprite('na433_15', 14)	# 59-72
    sprite('na433_16', 2)	# 73-74
    sprite('na433_17', 2)	# 75-76
    GFX_0('Kick_line', 100)
    SFX_3('slash_blade_middle')
    sprite('na433_18', 2)	# 77-78
    sprite('na433_20', 2)	# 79-80	 **attackbox here**
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('6e613433335f313900000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    tag_voice(0, 'pna258_0', 'pna258_1', '', '')
    sprite('na433_20', 35)	# 81-115	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    sprite('na433_21', 6)	# 116-121
    Unknown2004(1, 0)
    sprite('na433_22', 6)	# 122-127
    sprite('na433_23', 5)	# 128-132
    sprite('na433_24', 4)	# 133-136
    sprite('na433_25', 4)	# 137-140

@State
def UltimateWalkingShotKickOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2500)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Hitstop(30)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(70)
        AirHitstunAfterWallbounce(50)
        WallbounceReboundTime(40)
        Unknown9178(3)
        Unknown9346(0)
        Unknown9215()
        AirPushbackX(550000)
        AirPushbackY(40000)
        Unknown11068(1)
        Unknown11069('UltimateWalkingShotKickOD')

        def upon_12():
            ScreenShake(50000, 0)
        Unknown13024(0)
        setInvincible(1)
    sprite('na433_13', 4)	# 1-4
    sprite('na433_14', 4)	# 5-8
    sprite('na433_15', 10)	# 9-18
    sprite('na433_15', 10)	# 19-28
    ScreenShake(5000, 0)
    sprite('na433_15', 10)	# 29-38
    ScreenShake(7500, 0)
    sprite('na433_15', 10)	# 39-48
    ScreenShake(10000, 0)
    sprite('na433_15', 10)	# 49-58
    ScreenShake(12500, 0)
    sprite('na433_15', 14)	# 59-72
    sprite('na433_16', 2)	# 73-74
    sprite('na433_17', 2)	# 75-76
    GFX_0('Kick_line', 100)
    SFX_3('slash_blade_middle')
    sprite('na433_18', 2)	# 77-78
    sprite('na433_20', 2)	# 79-80	 **attackbox here**
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('6e613433335f313900000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    tag_voice(0, 'pna258_0', 'pna258_1', '', '')
    sprite('na433_20', 35)	# 81-115	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    sprite('na433_21', 6)	# 116-121
    Unknown2004(1, 0)
    sprite('na433_22', 6)	# 122-127
    sprite('na433_23', 5)	# 128-132
    sprite('na433_24', 4)	# 133-136
    sprite('na433_25', 4)	# 137-140

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17015()
    sprite('na001_00', 7)	# 1-7
    sprite('na001_01', 7)	# 8-14
    sprite('na001_02', 7)	# 15-21
    sprite('na001_03', 9)	# 22-30
    sprite('na001_04', 5)	# 31-35
    sprite('na001_05', 5)	# 36-40
    sprite('na001_06', 10)	# 41-50
    sprite('na001_01', 5)	# 51-55
    sprite('na001_00', 5)	# 56-60
    loopRest()
    label(1)
    sprite('na600_12', 1)	# 61-61
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('na600_13', 3)	# 62-64
    sprite('na600_14', 3)	# 65-67
    sprite('na600_15', 3)	# 68-70
    sprite('na600_16', 3)	# 71-73

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('na407_10', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    SFX_3('hit_l_slow')
    label(1)
    sprite('na407_10', 3)	# 124-126	 **attackbox here**
    sprite('na407_10', 3)	# 127-129	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('na407_11ex', 1)	# 130-130
    sprite('na211_00', 3)	# 131-133
    Unknown18009(1)
    sprite('na211_01', 27)	# 134-160

@State
def CmnActChangeReturnAppealBurst():
    sprite('na064_01', 30)	# 1-30
    sprite('na064_02', 5)	# 31-35
    sprite('na064_03', 5)	# 36-40
    sprite('na010_02', 5)	# 41-45
    sprite('na010_01', 5)	# 46-50
    sprite('na010_00', 5)	# 51-55
    sprite('na000_00', 30)	# 56-85

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown1112('')
    sprite('na203_00', 4)	# 1-4
    sprite('na203_01', 4)	# 5-8
    SFX_3('hit_l_middle')
    sprite('na203_50', 4)	# 9-12	 **attackbox here**
    Unknown23054('6e613230335f303200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    physicsXImpulse(20000)
    Unknown7009(1)
    sprite('na203_50', 2)	# 13-14	 **attackbox here**
    Recovery()
    Unknown2063()
    Unknown23027()
    Unknown1019(30)
    sprite('na203_50', 2)	# 15-16	 **attackbox here**
    Unknown1019(80)
    sprite('na203_50', 2)	# 17-18	 **attackbox here**
    Unknown1019(80)
    sprite('na203_03', 5)	# 19-23
    Unknown1019(0)
    sprite('na203_04', 5)	# 24-28

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(1300)
        AttackP1(90)
        AirPushbackX(10000)
        AirPushbackY(14000)
        PushbackX(12000)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        HitOrBlockCancel('NmlAtk5A3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_STATE_END():
            Unknown1084(1)
    sprite('na207_00', 2)	# 1-2
    sprite('na207_01', 4)	# 3-6
    SFX_3('hit_l_middle')
    physicsXImpulse(20000)
    sprite('na207_02', 2)	# 7-8	 **attackbox here**
    StartMultihit()
    Unknown1045(20000)
    sprite('na207_03', 2)	# 9-10	 **attackbox here**
    Unknown23054('6e613230375f303200000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    Unknown7009(1)
    Unknown1019(0)
    sprite('na207_03', 2)	# 11-12	 **attackbox here**
    Recovery()
    Unknown2063()
    Unknown1051(50)
    sprite('na207_04', 4)	# 13-16
    Unknown8010(100, 1, 0)
    sprite('na207_05', 5)	# 17-21
    sprite('na207_06', 5)	# 22-26

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 12):
                HitOrBlockCancel('NmlAtk5A4th')
                HitOrBlockCancel('NmlAtk5B')
                HitOrBlockCancel('NmlAtk2B')
                HitOrBlockCancel('NmlAtk2C')
                HitOrBlockCancel('CmnActCrushAttack')
                JumpCancel_(1)
                HitJumpCancel(1)
            if (SLOT_48 == 3020):
                Recovery()
                Unknown2063()
    sprite('na205_00', 2)	# 1-2
    sprite('na205_01', 2)	# 3-4
    sprite('na205_02', 4)	# 5-8
    Unknown23029(11, 103, 0)
    sprite('na205_03', 3)	# 9-11
    tag_voice(0, 'pna121_0', 'pna121_1', 'pna121_2', '')
    GFX_1('persona_enter_ply', 0)
    sprite('na205_04', 3)	# 12-14
    sprite('na205_05', 3)	# 15-17
    sprite('na205_03', 3)	# 18-20
    sprite('na205_04', 3)	# 21-23
    sprite('na205_05', 3)	# 24-26
    sprite('na205_03', 4)	# 27-30
    sprite('na205_04', 4)	# 31-34
    sprite('na205_05', 4)	# 35-38
    sprite('na205_01', 4)	# 39-42
    sprite('na205_00', 4)	# 43-46

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('na404_00', 3)	# 1-3
    sprite('na404_00', 3)	# 4-6
    sprite('na404_02', 6)	# 7-12
    GFX_0('DanganD', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    SFX_3('na002')
    tag_voice(1, 'pna210_0', 'pna210_1', 'pna210_2', '')

    def upon_43():
        if (SLOT_48 == 3020):
            Recovery()
    sprite('na404_03', 6)	# 13-18
    sprite('na404_04', 14)	# 19-32
    sprite('na404_05', 7)	# 33-39
    sprite('na401_00', 6)	# 40-45

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
    sprite('na204_00', 3)	# 1-3
    sprite('na204_01', 3)	# 4-6
    sprite('na204_01', 2)	# 7-8
    Unknown23029(11, 102, 0)
    sprite('na204_02', 5)	# 9-13
    GFX_1('persona_enter_ply', 0)
    tag_voice(1, 'pna120_0', 'pna120_1', 'pna120_2', '')
    sprite('na204_03', 5)	# 14-18
    sprite('na204_04', 1)	# 19-19
    sprite('na204_04', 4)	# 20-23
    Recovery()
    Unknown2063()
    sprite('na204_03', 6)	# 24-29
    sprite('na204_04', 6)	# 30-35
    sprite('na204_03', 6)	# 36-41
    sprite('na204_00', 4)	# 42-45

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('na205_00', 4)	# 1-4
    sprite('na205_01', 3)	# 5-7
    Unknown23029(11, 201, 0)
    sprite('na205_02', 3)	# 8-10
    GFX_1('persona_enter_ply', 0)
    sprite('na205_03', 3)	# 11-13
    sprite('na205_04', 3)	# 14-16
    sprite('na205_05', 3)	# 17-19
    sprite('na205_03', 3)	# 20-22
    sprite('na205_04', 3)	# 23-25
    Recovery()
    Unknown2063()
    sprite('na205_05', 3)	# 26-28
    sprite('na205_03', 4)	# 29-32
    sprite('na205_04', 4)	# 33-36
    sprite('na205_05', 4)	# 37-40
    sprite('na205_01', 4)	# 41-44
    sprite('na205_00', 4)	# 45-48

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(15000)
        HitOrBlockCancel('NmlAtk4A2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('na200_00', 3)	# 1-3
    SFX_3('hair')
    sprite('na200_01', 2)	# 4-5
    sprite('na200_50', 3)	# 6-8	 **attackbox here**
    Unknown23054('6e613230305f303200000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    Unknown7009(0)
    SFX_3('hit_l_fast')
    sprite('na200_50', 3)	# 9-11	 **attackbox here**
    Recovery()
    Unknown2063()
    Unknown23027()
    sprite('na200_03', 4)	# 12-15
    sprite('na200_04', 4)	# 16-19
    sprite('na200_05', 4)	# 20-23

@State
def NmlAtk4A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk4A3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown2004(1, 0)
    sprite('na201_00', 3)	# 1-3
    sprite('na201_01', 4)	# 4-7
    SFX_3('hit_l_middle')
    sprite('na201_02', 3)	# 8-10	 **attackbox here**
    Unknown7009(1)
    sprite('na201_03', 4)	# 11-14
    Recovery()
    Unknown2063()
    sprite('na201_04', 4)	# 15-18
    sprite('na201_05', 4)	# 19-22
    sprite('na201_06', 4)	# 23-26
    sprite('na201_07', 4)	# 27-30

@State
def NmlAtk4A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(70)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(30)
        AirPushbackX(12000)
        AirPushbackY(20000)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown14070('NmlAtk4A4th')
            Unknown14070('NmlAtk5BEx')
            Unknown14070('NmlAtk2BEx')
            Unknown14070('NmlAtk2CEx')
            Unknown14070('CmnActCrushAttackEx')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        HitOrBlockCancel('NmlAtk4A4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        JumpCancel_(0)
    sprite('na202_00', 1)	# 1-1
    sprite('na202_01', 4)	# 2-5
    physicsXImpulse(13500)
    physicsYImpulse(14000)
    setGravity(2000)
    sprite('na202_02', 8)	# 6-13
    SFX_3('hit_m_slow')
    sprite('na202_03', 4)	# 14-17	 **attackbox here**
    RefreshMultihit()
    Unknown7009(2)
    sprite('na202_04', 32767)	# 18-32784
    Recovery()
    label(1)
    sprite('na202_05', 3)	# 32785-32787
    Unknown14072('NmlAtk4A4th')
    Unknown14072('NmlAtk5BEx')
    Unknown14072('NmlAtk2BEx')
    Unknown14072('NmlAtk2CEx')
    Unknown14072('CmnActCrushAttackEx')
    JumpCancel_(1)
    Unknown1084(1)
    Unknown23027()
    sprite('na202_06', 5)	# 32788-32792
    Unknown2063()
    Unknown14074('NmlAtk4A4th')
    Unknown14074('NmlAtk5BEx')
    Unknown14074('NmlAtk2BEx')
    Unknown14074('NmlAtk2CEx')
    Unknown14074('CmnActCrushAttackEx')
    sprite('na202_07', 5)	# 32793-32797
    sprite('na202_08', 3)	# 32798-32800

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        HitLow(2)
        AttackP1(90)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('na230_01', 3)	# 1-3
    sprite('na230_02', 3)	# 4-6
    Unknown1051(80)
    sprite('na230_04', 3)	# 7-9	 **attackbox here**
    Unknown23054('6e613233305f303300000000000000000000000000000000000000000000000003000000')
    SFX_3('hit_l_fast')
    RefreshMultihit()
    Unknown7009(0)
    sprite('na230_04', 2)	# 10-11	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('na230_02', 3)	# 12-14
    sprite('na230_01', 3)	# 15-17
    sprite('na230_00', 3)	# 18-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('na232_00', 2)	# 1-2
    sprite('na232_01', 2)	# 3-4
    sprite('na232_02', 3)	# 5-7
    Unknown23029(11, 104, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('na232_03', 3)	# 8-10
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('na232_04', 3)	# 11-13
    sprite('na232_05', 3)	# 14-16
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('na232_03', 3)	# 17-19
    sprite('na232_04', 3)	# 20-22
    sprite('na232_05', 3)	# 23-25
    sprite('na232_03', 3)	# 26-28
    sprite('na232_04', 3)	# 29-31
    sprite('na232_05', 3)	# 32-34
    sprite('na232_00', 5)	# 35-39

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(15000)
        AirUntechableTime(22)
    sprite('na211_00', 2)	# 1-2
    sprite('na211_01', 2)	# 3-4
    sprite('na211_02', 2)	# 5-6
    sprite('na211_03', 3)	# 7-9
    sprite('na211_04', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    Unknown7007('706e613130375f30000000000000000064000000706e613130375f31000000000000000064000000706e613130375f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('hit_l_middle')
    sprite('na211_04', 4)	# 13-16	 **attackbox here**
    Recovery()
    Unknown2063()
    Unknown23027()
    sprite('na211_05', 4)	# 17-20
    sprite('na211_06', 4)	# 21-24
    Unknown2001()
    sprite('na211_01', 3)	# 25-27
    sprite('na211_00', 3)	# 28-30

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5A2ndex')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            Unknown23029(11, 302, 0)

        def upon_STATE_END():
            Unknown23029(11, 303, 0)
        Unknown4009(11)
sprite('na254_00', 3)	# 1-3
sprite('na254_01', 3)	# 4-6
Unknown23029(11, 301, 0)
sprite('na254_02', 6)	# 7-12
GFX_1('persona_enter_ply', 0)
Unknown7007('706e613130335f30000000000000000064000000706e613130335f31000000000000000064000000706e613130335f320000000000000000640000000000000000000000000000000000000000000000')
sprite('na254_03', 5)	# 13-17
sprite('na254_04', 5)	# 18-22
Recovery()
Unknown2063()
sprite('na254_05', 5)	# 23-27
sprite('na254_00', 4)	# 28-31
endState()

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(20)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('na251_00', 2)	# 1-2
    sprite('na251_01', 3)	# 3-5
    sprite('na251_03', 4)	# 6-9	 **attackbox here**
    Unknown23054('6e613235315f303200000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    Unknown7009(1)
    SFX_3('hit_l_slow')
    sprite('na251_03', 4)	# 10-13	 **attackbox here**
    Recovery()
    Unknown2063()
    Unknown23027()
    sprite('na251_04', 3)	# 14-16
    sprite('na251_05', 3)	# 17-19
    Unknown2001()
    sprite('na251_00', 2)	# 20-21

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            Unknown23029(11, 302, 0)

        def upon_STATE_END():
            Unknown23029(11, 303, 0)
        Unknown4009(11)
sprite('na254_00', 3)	# 1-3
sprite('na254_01', 3)	# 4-6
Unknown23029(11, 305, 0)
sprite('na254_02', 6)	# 7-12
GFX_1('persona_enter_ply', 0)
Unknown7007('706e613130335f30000000000000000064000000706e613130335f31000000000000000064000000706e613130335f320000000000000000640000000000000000000000000000000000000000000000')
sprite('na254_03', 5)	# 13-17
sprite('na254_04', 5)	# 18-22
Recovery()
Unknown2063()
sprite('na254_05', 5)	# 23-27
sprite('na254_00', 4)	# 28-31
Unknown2001()
endState()

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 12):
                JumpCancel_(1)
        Unknown22004(9, 1)
    sprite('na255_00', 3)	# 1-3
    sprite('na255_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('na255_02', 12)	# 7-18
    Unknown23029(11, 304, 0)
    Unknown7007('706e613130345f30000000000000000064000000706e613130345f31000000000000000064000000706e613130345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na255_03', 4)	# 19-22
    GFX_1('persona_enter_ply', 0)
    sprite('na255_04', 5)	# 23-27
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    sprite('na255_05', 5)	# 28-32
    Unknown2001()
    Recovery()
    Unknown2063()
    sprite('na255_01', 4)	# 33-36
    sprite('na255_00', 4)	# 37-40

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown2004(1, 0)
    sprite('na210_00', 2)	# 1-2
    sprite('na210_01', 2)	# 3-4
    sprite('na210_02', 2)	# 5-6
    tag_voice(1, 'pna156_0', 'pna156_1', '', '')
    sprite('na210_03', 5)	# 7-11
    sprite('na210_04', 6)	# 12-17
    sprite('na210_05', 2)	# 18-19
    sprite('na210_06', 2)	# 20-21
    SFX_3('hit_m_slow')
    sprite('na210_07', 3)	# 22-24	 **attackbox here**
    RefreshMultihit()
    sprite('na210_08', 2)	# 25-26
    sprite('na210_09', 2)	# 27-28
    sprite('na210_10', 7)	# 29-35
    sprite('na210_11', 6)	# 36-41
    sprite('na210_12', 7)	# 42-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(10)
    sprite('na210_10', 7)	# 1-7
    sprite('na210_11', 7)	# 8-14
    sprite('na210_12', 8)	# 15-22
    sprite('na201_00', 3)	# 23-25
    sprite('na201_01', 4)	# 26-29
    SFX_3('hit_l_middle')
    sprite('na201_02', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    tag_voice(1, 'pna157_0', 'pna157_1', '', '')
    sprite('na201_03', 3)	# 32-34
    sprite('na201_04', 3)	# 35-37
    sprite('na201_05', 3)	# 38-40
    Unknown2001()
    sprite('na201_06', 3)	# 41-43
    sprite('na201_07', 2)	# 44-45
    sprite('na000_00', 6)	# 46-51
    sprite('na000_01', 6)	# 52-57
    sprite('na000_02', 6)	# 58-63
    sprite('na000_03', 6)	# 64-69
    sprite('na000_04', 6)	# 70-75
    sprite('na000_05', 6)	# 76-81
    sprite('na000_06', 6)	# 82-87
    sprite('na000_07', 6)	# 88-93
    label(10)
    sprite('na000_00', 6)	# 94-99
    sprite('na000_01', 6)	# 100-105
    sprite('na000_02', 6)	# 106-111
    sprite('na000_03', 6)	# 112-117
    sprite('na000_04', 6)	# 118-123
    sprite('na000_05', 6)	# 124-129
    sprite('na000_06', 6)	# 130-135
    sprite('na000_07', 6)	# 136-141
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 142-142

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('na400_00', 3)	# 1-3
    teleportRelativeX(-25000)
    RefreshMultihit()
    Unknown23029(11, 403, 0)
    sprite('na400_00', 4)	# 4-7
    sprite('na400_01', 4)	# 8-11
    sprite('na400_02', 3)	# 12-14
    sprite('na400_03', 4)	# 15-18
    GFX_0('ImpactReversal_CA', 1)
    Unknown4020(1)
    Unknown36(1)
    Unknown30048(1)
    Unknown35()
    SFX_3('na003')
    ScreenShake(20000, 0)
    sprite('na400_05', 2)	# 19-20
    Unknown4020(0)
    sprite('na400_06', 2)	# 21-22
    sprite('na400_04', 4)	# 23-26
    sprite('na400_05', 4)	# 27-30
    sprite('na400_06', 4)	# 31-34
    sprite('na400_07', 3)	# 35-37
    sprite('na400_08', 3)	# 38-40
    sprite('na000_00', 6)	# 41-46
    sprite('na000_01', 6)	# 47-52
    sprite('na000_02', 6)	# 53-58
    sprite('na000_03', 6)	# 59-64
    sprite('na000_04', 6)	# 65-70
    sprite('na000_05', 6)	# 71-76
    sprite('na000_06', 6)	# 77-82
    sprite('na000_07', 6)	# 83-88
    label(10)
    sprite('na000_00', 6)	# 89-94
    sprite('na000_01', 6)	# 95-100
    sprite('na000_02', 6)	# 101-106
    sprite('na000_03', 6)	# 107-112
    sprite('na000_04', 6)	# 113-118
    sprite('na000_05', 6)	# 119-124
    sprite('na000_06', 6)	# 125-130
    sprite('na000_07', 6)	# 131-136
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('keep', 1)	# 137-137

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('na433_13', 3)	# 1-3
    sprite('na433_14', 3)	# 4-6
    sprite('na433_15', 7)	# 7-13
    sprite('na433_16', 2)	# 14-15
    sprite('na433_17', 2)	# 16-17
    GFX_0('Kick_line', 100)
    SFX_3('slash_blade_middle')
    sprite('na433_18', 2)	# 18-19
    sprite('na433_20', 2)	# 20-21	 **attackbox here**
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('6e613433335f313900000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    tag_voice(1, 'pna158_0', 'pna158_1', '', '')
    sprite('na433_20', 35)	# 22-56	 **attackbox here**
    Unknown23027()
    sprite('na433_21', 6)	# 57-62
    Unknown2004(1, 0)
    sprite('na433_22', 6)	# 63-68
    sprite('na433_23', 5)	# 69-73
    sprite('na433_24', 4)	# 74-77
    sprite('na433_25', 4)	# 78-81

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 19)	# 1-19
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 20-20
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('na407_02', 3)	# 21-23
    physicsXImpulse(35000)
    physicsYImpulse(23000)
    setGravity(2000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(0)
    sprite('na407_02', 2)	# 24-25
    sprite('na407_02', 2)	# 26-27
    Unknown2016(310)
    teleportRelativeX(65000)
    sprite('na407_03', 2)	# 28-29	 **attackbox here**
    StartMultihit()
    GFX_0('Tossin_atk1', 0)
    physicsXImpulse(22000)
    physicsYImpulse(17000)
    setGravity(3000)
    SFX_3('runjump_stone_light')
    SFX_3('hit_l_slow')
    sprite('na407_04', 2)	# 30-31
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)	# 32-33
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)	# 34-35
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)	# 36-37
    callSubroutine('HaikyouEx0')
    Unknown1019(70)
    sprite('na407_08', 2)	# 38-39
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)	# 40-41
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_slow')
    sprite('na407_11ex', 32767)	# 44-32810
    label(0)
    sprite('na211_00', 3)	# 32811-32813
    Unknown1084(1)
    Unknown18009(1)
    sprite('na211_01', 3)	# 32814-32816
    sprite('na010_01', 4)	# 32817-32820
    sprite('na010_00', 4)	# 32821-32824
    sprite('na000_00', 6)	# 32825-32830
    sprite('na000_01', 6)	# 32831-32836
    sprite('na000_02', 6)	# 32837-32842
    sprite('na000_03', 6)	# 32843-32848
    sprite('na000_04', 6)	# 32849-32854
    sprite('na000_05', 6)	# 32855-32860
    sprite('na000_06', 6)	# 32861-32866
    sprite('na000_07', 6)	# 32867-32872
    label(10)
    sprite('na000_00', 6)	# 32873-32878
    sprite('na000_01', 6)	# 32879-32884
    sprite('na000_02', 6)	# 32885-32890
    sprite('na000_03', 6)	# 32891-32896
    sprite('na000_04', 6)	# 32897-32902
    sprite('na000_05', 6)	# 32903-32908
    sprite('na000_06', 6)	# 32909-32914
    sprite('na000_07', 6)	# 32915-32920
    loopRest()
    gotoLabel(10)

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('na404_00', 5)	# 1-5
    sprite('na404_00', 6)	# 6-11
    sprite('na404_02', 6)	# 12-17
    Unknown23029(11, 101, 0)
    GFX_0('DanganDASS', 1)
    Unknown4020(1)
    ScreenShake(10000, 0)
    SFX_3('na002')
    sprite('na404_03', 6)	# 18-23
    Unknown4020(0)
    sprite('na404_04', 6)	# 24-29
    sprite('na404_05', 7)	# 30-36
    sprite('na401_00', 1)	# 37-37
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 38-38
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 39-39
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 3)	# 40-42
    sprite('na000_00', 6)	# 43-48
    sprite('na000_01', 6)	# 49-54
    sprite('na000_02', 6)	# 55-60
    sprite('na000_03', 6)	# 61-66
    sprite('na000_04', 6)	# 67-72
    sprite('na000_05', 6)	# 73-78
    sprite('na000_06', 6)	# 79-84
    sprite('na000_07', 6)	# 85-90
    label(10)
    sprite('na000_00', 6)	# 91-96
    sprite('na000_01', 6)	# 97-102
    sprite('na000_02', 6)	# 103-108
    sprite('na000_03', 6)	# 109-114
    sprite('na000_04', 6)	# 115-120
    sprite('na000_05', 6)	# 121-126
    sprite('na000_06', 6)	# 127-132
    sprite('na000_07', 6)	# 133-138
    loopRest()
    gotoLabel(10)

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('na433_13', 3)	# 1-3
    sprite('na433_14', 3)	# 4-6
    sprite('na433_15', 7)	# 7-13
    sprite('na433_16', 2)	# 14-15
    sprite('na433_17', 2)	# 16-17
    GFX_0('Kick_line', 100)
    SFX_3('slash_blade_middle')
    sprite('na433_18', 2)	# 18-19
    sprite('na433_20', 2)	# 20-21	 **attackbox here**
    GFX_0('Zanzoh_kick', 100)
    Unknown23054('6e613433335f313900000000000000000000000000000000000000000000000003000000')
    RefreshMultihit()
    sprite('na433_20', 35)	# 22-56	 **attackbox here**
    Unknown23027()
    sprite('na433_21', 6)	# 57-62
    Unknown2004(1, 0)
    sprite('na433_22', 6)	# 63-68
    sprite('na433_23', 5)	# 69-73
    sprite('na433_24', 4)	# 74-77
    sprite('na433_25', 4)	# 78-81

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(18000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('na030_00', 7)	# 1-7
    sprite('na032_00', 2)	# 8-9
    label(0)
    sprite('na032_01', 4)	# 10-13
    physicsXImpulse(20000)
    sprite('na032_02', 4)	# 14-17
    Unknown1019(120)
    sprite('na032_03', 4)	# 18-21
    Unknown8006(100, 1, 1)
    sprite('na032_04', 4)	# 22-25
    Unknown1019(120)
    sprite('na032_05', 4)	# 26-29
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('na310_00', 1)	# 30-30
    Unknown1084(1)
    sprite('na310_01', 1)	# 31-31
    sprite('na310_01', 1)	# 32-32
    Unknown1051(50)
    sprite('na310_02', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    sprite('na310_03', 3)	# 36-38
    SFX_1('pna154')
    sprite('na310_04', 5)	# 39-43
    sprite('na310_03', 5)	# 44-48
    sprite('na310_01', 5)	# 49-53
    sprite('na310_00', 5)	# 54-58

@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Unknown9154(70)
        AirUntechableTime(70)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9142(70)
        Unknown9130(70)
        PushbackX(-3000)
        Hitstop(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(0)
        Unknown11069('PNA_PersonaThrow')
        Unknown2004(1, 0)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 12):
                JumpCancel_(1)
    sprite('na310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('na311_00', 3)	# 5-7
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('na311_50', 7)	# 8-14	 **attackbox here**
    Unknown23054('6e613331315f303100000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('na204_02', 1)	# 15-15
    sprite('na204_02', 4)	# 16-19
    GFX_1('persona_enter_ply', 3)
    Unknown7007('706e613135330000000000000000000064000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23029(11, 105, 0)
    sprite('na204_03', 4)	# 20-23
    sprite('na204_04', 4)	# 24-27
    sprite('na204_03', 4)	# 28-31
    sprite('na204_04', 4)	# 32-35
    sprite('na204_03', 4)	# 36-39
    sprite('na204_04', 4)	# 40-43
    sprite('na204_03', 4)	# 44-47
    sprite('na204_04', 4)	# 48-51
    sprite('na204_00', 4)	# 52-55

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkBackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(18000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('na030_00', 7)	# 1-7
    sprite('na032_00', 2)	# 8-9
    label(0)
    sprite('na032_01', 4)	# 10-13
    physicsXImpulse(20000)
    sprite('na032_02', 4)	# 14-17
    Unknown1019(120)
    sprite('na032_03', 4)	# 18-21
    Unknown8006(100, 1, 1)
    sprite('na032_04', 4)	# 22-25
    Unknown1019(120)
    sprite('na032_05', 4)	# 26-29
    loopRest()
    gotoLabel(0)
    label(1)
    clearUponHandler(3)
    sprite('na310_00', 1)	# 30-30
    Unknown1084(1)
    sprite('na310_01', 1)	# 31-31
    sprite('na310_01', 1)	# 32-32
    Unknown1051(50)
    sprite('na310_02', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    sprite('na310_03', 3)	# 36-38
    SFX_1('pna154')
    sprite('na310_04', 5)	# 39-43
    sprite('na310_03', 5)	# 44-48
    sprite('na310_01', 5)	# 49-53
    sprite('na310_00', 5)	# 54-58

@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AttackP1(100)
        AttackP2(100)
        Unknown9154(70)
        AirUntechableTime(70)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9142(70)
        Unknown9130(70)
        PushbackX(-40000)
        Hitstop(0)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11023(0)
        Unknown11069('PNA_PersonaThrow')
        Unknown2004(1, 0)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 12):
                JumpCancel_(1)
    sprite('na310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('na311_00', 3)	# 5-7
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('na311_50', 10)	# 8-17	 **attackbox here**
    Unknown23054('6e613331315f303100000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('na311_50', 6)	# 18-23	 **attackbox here**
    Unknown2006()
    StartMultihit()
    sprite('na311_50', 1)	# 24-24	 **attackbox here**
    Unknown2006()
    sprite('na204_02', 1)	# 25-25
    sprite('na204_02', 4)	# 26-29
    GFX_1('persona_enter_ply', 3)
    Unknown7007('706e613135330000000000000000000064000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23029(11, 105, 0)
    sprite('na204_03', 4)	# 30-33
    sprite('na204_04', 4)	# 34-37
    sprite('na204_03', 4)	# 38-41
    sprite('na204_04', 4)	# 42-45
    sprite('na204_03', 4)	# 46-49
    sprite('na204_04', 4)	# 50-53
    sprite('na204_03', 4)	# 54-57
    sprite('na204_04', 4)	# 58-61
    sprite('na204_00', 4)	# 62-65

@State
def KamaeBase():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('ShagekiFlexChain')
        SFX_3('na000')
        Unknown11063(1)
        Unknown14083(0)
        Unknown30068(1)
        if SLOT_62:
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)

        def upon_3():
            if (not SLOT_158):
                SLOT_52 = 1
            if (not SLOT_21):
                SLOT_52 = 1
            if SLOT_52:
                if SLOT_53:
                    enterState('KamaeCancel')
    SLOT_51 = SLOT_61
    (SLOT_51 == 1)
    if SLOT_0:
        _gotolabel(1)
    (SLOT_51 == 2)
    if SLOT_0:
        _gotolabel(2)
    label(0)
    sprite('na401_52', 10)	# 1-10
    WhiffCancelEnable(1)
    GFX_0('GunKira', 2)
    sprite('keep', 70)	# 11-80
    SLOT_53 = 1
    sprite('keep', 32767)	# 81-32847
    enterState('KamaeCancel')
    loopRest()
    ExitState()
    label(1)
    sprite('na401_53', 10)	# 32848-32857
    WhiffCancelEnable(1)
    GFX_0('GunKira', 2)
    sprite('keep', 70)	# 32858-32927
    SLOT_53 = 1
    sprite('keep', 32767)	# 32928-65694
    enterState('KamaeCancel')
    loopRest()
    ExitState()
    label(2)
    sprite('na401_54', 10)	# 65695-65704
    WhiffCancelEnable(1)
    GFX_0('GunKira', 2)
    sprite('keep', 70)	# 65705-65774
    SLOT_53 = 1
    sprite('keep', 32767)	# 65775-98541
    enterState('KamaeCancel')
    loopRest()
    ExitState()

@State
def KamaeA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown1084(1)
        SLOT_62 = 0
        SLOT_60 = 5
        SLOT_61 = 0
        Unknown11063(1)
    sprite('na401_00', 3)	# 1-3
    sprite('na401_01', 1)	# 4-4
    Unknown7007('706e613230335f30000000000000000064000000706e613230335f31000000000000000064000000706e613230335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na401_01', 1)	# 5-5
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 6-6
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 7-7
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 8-8
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 9-9
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 10-10
    callSubroutine('HaikyouEx0')
    sprite('na401_02', 1)	# 11-11
    sprite('na401_03', 3)	# 12-14
    sprite('na401_03', 32767)	# 15-32781
    enterState('KamaeBase')

@State
def ShagekiA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown14083(0)
        Unknown30068(1)

        def upon_43():
            if (SLOT_48 == 4001):
                Unknown14083(1)
            if (SLOT_48 == 3008):
                SLOT_52 = 1
            if (SLOT_48 == 3016):
                SLOT_52 = 0
        if SLOT_62:
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)
    SLOT_51 = SLOT_61
    SLOT_61 = 3
    (SLOT_51 == 1)
    if SLOT_0:
        _gotolabel(1)
    (SLOT_51 == 2)
    if SLOT_0:
        _gotolabel(2)
    (SLOT_51 == 3)
    if SLOT_0:
        _gotolabel(3)
    sprite('na401_03', 2)	# 1-2
    loopRest()
    gotoLabel(16)
    label(1)
    sprite('na401_50', 2)	# 3-4
    sprite('na401_03', 4)	# 5-8
    sprite('na401_52', 2)	# 9-10
    loopRest()
    gotoLabel(16)
    label(2)
    sprite('na401_51', 2)	# 11-12
    sprite('na401_03', 4)	# 13-16
    sprite('na401_52', 2)	# 17-18
    loopRest()
    gotoLabel(16)
    label(3)
    sprite('na401_03', 2)	# 19-20
    loopRest()
    gotoLabel(16)
    label(16)
    (SLOT_60 <= 1)
    if SLOT_0:
        _gotolabel(17)
    sprite('na401_52', 1)	# 21-21
    if (SLOT_60 == 5):
        Unknown7007('706e613230375f30000000000000000064000000706e613230375f31000000000000000064000000706e613230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na404_00', 2)	# 22-23
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('Dangan', 1)
    Unknown23029(1, 3010, 0)
    SFX_3('na001')
    sprite('na404_01', 2)	# 24-25
    WhiffCancelEnable(1)
    WhiffCancel('ShagekiA')
    sprite('na404_00', 1)	# 26-26
    if (not SLOT_52):
        gotoLabel(16)
    sprite('na404_00', 3)	# 27-29
    sprite('na401_03', 3)	# 30-32
    sprite('na401_03', 3)	# 33-35
    WhiffCancelEnable(0)
    sprite('na401_03', 32767)	# 36-32802
    enterState('KamaeBase')
    loopRest()
    ExitState()
    label(17)
    WhiffCancelEnable(0)
    sprite('na404_00', 1)	# 32803-32803
    sprite('na404_00', 2)	# 32804-32805
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('DanganLastA', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    SFX_3('na002')
    sprite('na404_02', 3)	# 32806-32808
    sprite('na404_03', 3)	# 32809-32811
    sprite('na404_04', 8)	# 32812-32819
    sprite('na404_05', 4)	# 32820-32823
    sprite('na404_06', 4)	# 32824-32827
    sprite('na401_03', 3)	# 32828-32830
    enterState('KamaeCancel')
    loopRest()
    ExitState()

@State
def ShagekiB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown14083(0)
        Unknown30068(1)

        def upon_43():
            if (SLOT_48 == 4001):
                Unknown14083(1)
            if (SLOT_48 == 3008):
                SLOT_52 = 1
        if SLOT_62:
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)
    SLOT_51 = SLOT_61
    SLOT_61 = 1
    (SLOT_51 == 1)
    if SLOT_0:
        _gotolabel(1)
    (SLOT_51 == 2)
    if SLOT_0:
        _gotolabel(2)
    (SLOT_51 == 3)
    if SLOT_0:
        _gotolabel(3)
    sprite('na401_50', 2)	# 1-2
    loopRest()
    gotoLabel(16)
    label(1)
    sprite('na405_00', 2)	# 3-4	 **attackbox here**
    loopRest()
    gotoLabel(16)
    label(2)
    sprite('na401_50', 2)	# 5-6
    sprite('na405_00', 4)	# 7-10	 **attackbox here**
    sprite('na401_53', 2)	# 11-12
    loopRest()
    gotoLabel(16)
    label(3)
    sprite('na401_50', 2)	# 13-14
    sprite('na405_00', 4)	# 15-18	 **attackbox here**
    sprite('na401_53', 2)	# 19-20
    loopRest()
    gotoLabel(16)
    label(16)
    (SLOT_60 <= 1)
    if SLOT_0:
        _gotolabel(17)
    sprite('na401_53', 1)	# 21-21
    if (SLOT_60 == 5):
        Unknown7007('706e613230385f30000000000000000064000000706e613230385f31000000000000000064000000706e613230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na405_01', 2)	# 22-23
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('Dangan', 1)
    Unknown23029(1, 3011, 0)
    SFX_3('na001')
    sprite('na405_02', 2)	# 24-25
    WhiffCancelEnable(1)
    WhiffCancel('ShagekiB')
    sprite('na405_00', 1)	# 26-26	 **attackbox here**
    if (not SLOT_52):
        gotoLabel(16)
    sprite('na405_00', 3)	# 27-29	 **attackbox here**
    sprite('na405_00', 3)	# 30-32	 **attackbox here**
    sprite('na405_00', 3)	# 33-35	 **attackbox here**
    WhiffCancelEnable(0)
    sprite('na405_00', 32767)	# 36-32802	 **attackbox here**
    enterState('KamaeBase')
    ExitState()
    label(17)
    WhiffCancelEnable(0)
    sprite('na405_01', 1)	# 32803-32803
    sprite('na405_01', 2)	# 32804-32805
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('DanganLastB', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    SFX_3('na002')
    sprite('na404_02', 3)	# 32806-32808
    sprite('na404_03', 3)	# 32809-32811
    sprite('na404_04', 10)	# 32812-32821
    sprite('na404_05', 5)	# 32822-32826
    sprite('na404_06', 5)	# 32827-32831
    sprite('na401_03', 3)	# 32832-32834
    enterState('KamaeCancel')
    loopRest()
    ExitState()

@State
def ShagekiC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown14083(0)
        Unknown30068(1)

        def upon_43():
            if (SLOT_48 == 4001):
                Unknown14083(1)
            if (SLOT_48 == 3008):
                SLOT_52 = 1
        if SLOT_62:
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)
    SLOT_51 = SLOT_61
    SLOT_61 = 2
    (SLOT_51 == 1)
    if SLOT_0:
        _gotolabel(1)
    (SLOT_51 == 2)
    if SLOT_0:
        _gotolabel(2)
    (SLOT_51 == 3)
    if SLOT_0:
        _gotolabel(3)
    sprite('na401_51', 2)	# 1-2
    loopRest()
    gotoLabel(16)
    label(1)
    sprite('na401_51', 2)	# 3-4
    sprite('na406_00', 4)	# 5-8
    sprite('na401_54', 2)	# 9-10
    loopRest()
    gotoLabel(16)
    label(2)
    sprite('na406_00', 2)	# 11-12
    loopRest()
    gotoLabel(16)
    label(3)
    sprite('na401_51', 2)	# 13-14
    sprite('na406_00', 4)	# 15-18
    sprite('na401_54', 2)	# 19-20
    loopRest()
    gotoLabel(16)
    label(16)
    (SLOT_60 <= 1)
    if SLOT_0:
        _gotolabel(17)
    sprite('na401_54', 1)	# 21-21
    if (SLOT_60 == 5):
        Unknown7007('706e613230385f30000000000000000064000000706e613230385f31000000000000000064000000706e613230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na406_01', 2)	# 22-23
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('Dangan', 1)
    Unknown23029(1, 3019, 0)
    SFX_3('na001')
    sprite('na406_02', 2)	# 24-25
    WhiffCancelEnable(1)
    WhiffCancel('ShagekiC')
    sprite('na406_00', 1)	# 26-26
    if (not SLOT_52):
        gotoLabel(16)
    sprite('na406_00', 3)	# 27-29
    sprite('na406_00', 3)	# 30-32
    sprite('na406_00', 3)	# 33-35
    WhiffCancelEnable(0)
    sprite('na406_00', 32767)	# 36-32802
    enterState('KamaeBase')
    ExitState()
    label(17)
    WhiffCancelEnable(0)
    sprite('na406_01', 1)	# 32803-32803
    sprite('na406_01', 2)	# 32804-32805
    SLOT_60 = (SLOT_60 + (-1))
    SLOT_59 = (SLOT_59 + 1)
    GFX_0('DanganLastC', 1)
    ScreenShake(10000, 0)
    Unknown1047(-10000)
    SFX_3('na002')
    sprite('na404_02', 3)	# 32806-32808
    sprite('na404_03', 3)	# 32809-32811
    sprite('na404_04', 7)	# 32812-32818
    sprite('na404_05', 4)	# 32819-32822
    sprite('na404_06', 4)	# 32823-32826
    sprite('na401_03', 3)	# 32827-32829
    enterState('KamaeCancel')
    loopRest()
    ExitState()

@State
def KamaeCancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown14083(0)
        Unknown30068(1)
        Unknown11063(1)
        if SLOT_62:
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)

        def upon_STATE_END():
            SLOT_62 = 0
    sprite('na401_02', 5)	# 1-5
    Unknown7007('706e613231315f30000000000000000064000000706e613231315f31000000000000000064000000706e613231315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na401_01', 1)	# 6-6
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 7-7
    callSubroutine('HaikyouEx0')
    sprite('na401_01', 1)	# 8-8
    sprite('na401_01', 1)	# 9-9
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 10-10
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 11-11
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 12-12
    callSubroutine('HaikyouEx0')
    sprite('na401_00', 1)	# 13-13

@State
def KamaeEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_61 = 0
        Unknown14083(0)
        Unknown30068(1)
        Unknown11063(1)
        if SLOT_62:
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)
    sprite('na403_00', 3)	# 1-3
    sprite('na403_01', 2)	# 4-5
    Unknown7007('706e613230355f30000000000000000064000000706e613230355f31000000000000000064000000706e613230355f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(30000)
    Unknown2017(0)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('na403_02', 1)	# 6-6
    Unknown1019(160)
    sprite('na403_03', 1)	# 7-7
    sprite('na403_04', 2)	# 8-9
    sprite('na403_05', 2)	# 10-11
    sprite('na403_06', 1)	# 12-12
    sprite('na403_06', 1)	# 13-13
    Unknown1084(1)
    Unknown1045(32000)
    sprite('na403_07', 2)	# 14-15
    callSubroutine('HaikyouEx0')
    sprite('na403_08', 2)	# 16-17
    Unknown2017(1)
    callSubroutine('HaikyouEx0')
    sprite('na403_09', 2)	# 18-19
    Unknown2006()
    sprite('na403_09', 1)	# 20-20
    callSubroutine('HaikyouEx0')
    sprite('na403_10', 2)	# 21-22
    callSubroutine('HaikyouEx0')
    sprite('na403_11', 1)	# 23-23
    callSubroutine('HaikyouEx0')
    setInvincible(0)
    sprite('na403_11', 1)	# 24-24
    callSubroutine('HaikyouEx0')
    Unknown1084(1)
    sprite('na403_12', 2)	# 25-26
    WhiffCancelEnable(1)
    SLOT_60 = 5
    sprite('na401_03', 32767)	# 27-32793
    enterState('KamaeBase')

@State
def BanditRevolverB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(24000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown2004(1, 0)
        SLOT_60 = 5
        sendToLabelUpon(2, 9)
        SLOT_62 = 0
    sprite('na407_00', 5)	# 1-5
    sprite('na407_01', 5)	# 6-10
    sprite('na407_02', 3)	# 11-13
    GFX_0('Jumpsmoke', 0)
    teleportRelativeX(65000)
    ScreenShake(10000, 0)
    Unknown7007('706e613231335f30000000000000000064000000706e613231335f31000000000000000064000000706e613231335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na407_03', 6)	# 14-19	 **attackbox here**
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    physicsXImpulse(31000)
    physicsYImpulse(22000)
    setGravity(2000)
    SFX_3('runjump_stone_light')
    SFX_3('hit_l_slow')
    Unknown23087(30000)
    sprite('na407_04', 2)	# 20-21
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)	# 22-23
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)	# 24-25
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)	# 26-27
    callSubroutine('HaikyouEx0')
    sprite('na407_08', 2)	# 28-29
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)	# 30-31
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 3)	# 32-34	 **attackbox here**
    SLOT_61 = 0
    RefreshMultihit()
    AirPushbackX(19000)
    AirPushbackY(-90000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown9118(20)
    AirHitstunAfterWallbounce(60)
    Unknown11001(0, -4, 5)
    Unknown11058('0100000000000000000000000000000000000000')
    HitOverhead(2)
    SFX_3('hit_l_slow')
    sprite('na407_11', 3)	# 35-37
    Recovery()
    sprite('na402_05', 32767)	# 38-32804
    label(9)
    sprite('na402_06', 4)	# 32805-32808
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown2006()
    Unknown23087(-1)
    sprite('na401_03', 32767)	# 32809-65575
    enterState('KamaeBase')

@State
def AirBanditRevolverA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(30)
        AirPushbackX(21000)
        AirPushbackY(16000)
        clearUponHandler(2)
        SLOT_62 = 0
    sprite('na407_02', 4)	# 1-4
    sprite('na407_03', 4)	# 5-8	 **attackbox here**
    StartMultihit()
    physicsXImpulse(22000)
    physicsYImpulse(20000)
    setGravity(2000)
    SFX_3('runjump_stone_light')
    SFX_3('hit_l_slow')
    Unknown7007('706e613231325f30000000000000000064000000706e613231325f31000000000000000064000000706e613231325f320000000000000000640000000000000000000000000000000000000000000000')
    sendToLabelUpon(2, 9)
    sprite('na407_03', 3)	# 9-11	 **attackbox here**
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    sprite('na407_04', 2)	# 12-13
    GFX_0('Tossin_atk2', 100)
    sprite('na407_05', 2)	# 14-15
    sprite('na407_06', 2)	# 16-17
    sprite('na407_07', 2)	# 18-19
    Unknown1019(80)
    sprite('na407_08', 2)	# 20-21
    sprite('na407_09', 2)	# 22-23
    sprite('na407_10', 6)	# 24-29	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(29000)
    AirPushbackY(-71000)
    Unknown9310(1)
    HitOverhead(2)
    SFX_3('hit_l_slow')
    sprite('na407_11ex', 32767)	# 30-32796
    Recovery()
    label(9)
    sprite('na211_00', 4)	# 32797-32800
    Unknown8000(100, 1, 1)
    Recovery()
    Unknown1084(1)
    Unknown18009(1)
    sprite('na211_01', 12)	# 32801-32812

@State
def AirBanditRevolverB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(24000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown2004(1, 0)
        SLOT_60 = 5
        clearUponHandler(2)
        SLOT_62 = 0
    sprite('na407_02', 4)	# 1-4
    sprite('na407_02', 4)	# 5-8
    Unknown1084(1)
    sprite('na407_03', 4)	# 9-12	 **attackbox here**
    StartMultihit()
    physicsXImpulse(22000)
    physicsYImpulse(28000)
    setGravity(2000)
    SFX_3('runjump_stone_light')
    SFX_3('hit_l_slow')
    Unknown7007('706e613231325f30000000000000000064000000706e613231325f31000000000000000064000000706e613231325f320000000000000000640000000000000000000000000000000000000000000000')
    sendToLabelUpon(2, 9)
    sprite('na407_03', 6)	# 13-18	 **attackbox here**
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    sprite('na407_04', 2)	# 19-20
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)	# 21-22
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)	# 23-24
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)	# 25-26
    callSubroutine('HaikyouEx0')
    sprite('na407_08', 2)	# 27-28
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)	# 29-30
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 6)	# 31-36	 **attackbox here**
    SLOT_61 = 0
    RefreshMultihit()
    AirPushbackX(29000)
    AirPushbackY(-90000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown9118(20)
    AirHitstunAfterWallbounce(60)
    Unknown11001(0, -4, 5)
    Unknown11058('0100000000000000000000000000000000000000')
    HitOverhead(2)
    SFX_3('hit_l_slow')
    sprite('na407_11', 3)	# 37-39
    Recovery()
    sprite('na402_05', 32767)	# 40-32806
    label(9)
    sprite('na402_06', 4)	# 32807-32810
    Unknown8000(100, 1, 1)
    Recovery()
    Unknown1084(1)
    Unknown2006()
    sprite('na401_03', 32767)	# 32811-65577
    enterState('KamaeBase')

@State
def AirBanditRevolverEX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown17003()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(80)
        Unknown11092(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(24000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        Unknown11091(10)
        Unknown30065(0)
        Unknown2004(1, 0)
        SLOT_60 = 5
        clearUponHandler(2)
        SLOT_62 = 0
    sprite('na407_02', 4)	# 1-4
    sprite('na407_03', 4)	# 5-8	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    SLOT_62 = 1
    StartMultihit()
    physicsXImpulse(25000)
    physicsYImpulse(28000)
    setGravity(2000)
    SFX_3('runjump_stone_light')
    SFX_3('hit_l_slow')
    Unknown7007('706e613231325f30000000000000000064000000706e613231325f31000000000000000064000000706e613231325f320000000000000000640000000000000000000000000000000000000000000000')
    sendToLabelUpon(2, 9)
    sprite('na407_03', 6)	# 9-14	 **attackbox here**
    GFX_0('Tossin_atk1', 0)
    RefreshMultihit()
    sprite('na407_04', 2)	# 15-16
    callSubroutine('HaikyouEx0')
    sprite('na407_05', 2)	# 17-18
    callSubroutine('HaikyouEx0')
    sprite('na407_06', 2)	# 19-20
    GFX_0('Tossin_atk2', 100)
    callSubroutine('HaikyouEx0')
    sprite('na407_07', 2)	# 21-22
    callSubroutine('HaikyouEx0')
    sprite('na407_08', 2)	# 23-24
    callSubroutine('HaikyouEx0')
    sprite('na407_09', 2)	# 25-26
    callSubroutine('HaikyouEx0')
    sprite('na407_10', 6)	# 27-32	 **attackbox here**
    SLOT_61 = 0
    RefreshMultihit()
    AirPushbackX(29000)
    AirPushbackY(-71000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown9118(50)
    AirHitstunAfterWallbounce(60)
    Unknown11001(0, 0, 5)
    Unknown11058('0100000000000000000000000000000000000000')
    HitOverhead(2)
    SFX_3('hit_l_slow')
    sprite('na407_11', 32767)	# 33-32799
    Recovery()
    label(9)
    sprite('na211_00', 2)	# 32800-32801
    Unknown8000(100, 1, 1)
    Recovery()
    Unknown1084(1)
    Unknown18009(1)
    sprite('na211_01', 11)	# 32802-32812

@State
def WalkingShotEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown14083(1)
        SLOT_62 = 1
        WhiffCancel('WalkingShotKickEX')
        WhiffCancel('KamaeEX')

        def upon_3():
            if SLOT_51:
                if SLOT_52:
                    SLOT_52 = (SLOT_52 + (-1))
                else:
                    if CheckInput(0x1):
                        if (not (SLOT_53 >= 5)):
                            SLOT_52 = 8
                            SLOT_53 = (SLOT_53 + 1)
                            SLOT_59 = (SLOT_59 + 1)
                            GFX_0('DanganUltimate', 1)
                            ScreenShake(10000, 0)
                    if CheckInput(0xa):
                        if (not (SLOT_53 >= 5)):
                            SLOT_52 = 8
                            SLOT_53 = (SLOT_53 + 1)
                            SLOT_59 = (SLOT_59 + 1)
                            GFX_0('DanganUltimate', 1)
                            ScreenShake(10000, 0)
            if SLOT_54:
                if (SLOT_18 == 240):
                    sendToLabel(9)
                if (not SLOT_158):
                    clearUponHandler(3)
                    sendToLabel(9)
                if (not SLOT_21):
                    clearUponHandler(3)
                    sendToLabel(9)
    sprite('na433_00', 3)	# 1-3
    sprite('na433_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'pna219_0', 'pna219_1', '', '')
    sprite('na433_02', 3)	# 7-9
    WhiffCancelEnable(1)
    sprite('na433_03', 5)	# 10-14
    physicsXImpulse(7000)
    label(0)
    sprite('na433_04', 7)	# 15-21
    SLOT_51 = 1
    SLOT_54 = 1
    sprite('na433_05', 7)	# 22-28
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na433_06', 7)	# 29-35
    sprite('na433_07', 7)	# 36-42
    sprite('na433_08', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('na433_09', 7)	# 50-56
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('na433_10', 6)	# 57-62
    Unknown1084(1)
    clearUponHandler(3)
    WhiffCancelEnable(0)
    SLOT_51 = 0
    SLOT_54 = 0
    sprite('na433_11', 1)	# 63-63
    sprite('na433_11', 1)	# 64-64
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)	# 65-65
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)	# 66-66
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)	# 67-67
    callSubroutine('HaikyouEx0')
    sprite('na433_11', 1)	# 68-68
    callSubroutine('HaikyouEx0')
    sprite('na433_12', 6)	# 69-74

@State
def WalkingShotKickEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2500)
        AttackP1(80)
        AttackP2(80)
        Hitstop(30)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirUntechableTime(70)
        AirPushbackX(75000)
        AirPushbackY(35000)
        WallbounceReboundTime(20)
        Unknown9362(1)
        Unknown9364(45)
        AirHitstunAfterWallbounce(70)
        Unknown11091(10)
        Unknown30065(0)
        Unknown30068(1)
        Unknown2006()
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)

        def upon_12():
            ScreenShake(50000, 0)
        setInvincible(1)
    sprite('na433_13', 1)	# 1-1
    sprite('na433_14', 2)	# 2-3
    tag_voice(0, 'pna220_0', 'pna220_1', '', '')
    sprite('na433_15', 4)	# 4-7
    sprite('na433_16', 1)	# 8-8
    sprite('na433_17', 1)	# 9-9
    GFX_0('Kick_line', 100)
    SFX_3('slash_blade_middle')
    sprite('na433_18', 1)	# 10-10
    sprite('na433_20', 2)	# 11-12	 **attackbox here**
    GFX_0('Zanzoh_kick', 100)
    RefreshMultihit()
    sprite('na433_20', 10)	# 13-22	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    sprite('na433_21', 6)	# 23-28
    Unknown2004(1, 0)
    sprite('na433_22', 6)	# 29-34
    sprite('na433_23', 5)	# 35-39
    sprite('na433_24', 1)	# 40-40
    sprite('na433_24', 1)	# 41-41
    sprite('na433_24', 1)	# 42-42
    sprite('na433_25', 1)	# 43-43
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)	# 44-44
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)	# 45-45
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)	# 46-46
    callSubroutine('HaikyouEx0')
    sprite('na433_25', 1)	# 47-47
    callSubroutine('HaikyouEx0')

@State
def TrapA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na408_00', 4)	# 1-4
    sprite('na408_01', 4)	# 5-8
    sprite('na408_02', 4)	# 9-12
    SFX_3('na004')
    sprite('na408_03', 7)	# 13-19
    Unknown23029(11, 401, 0)
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    Unknown38(4, 1)
    sprite('na408_02', 7)	# 20-26
    Recovery()
    sprite('na408_01', 5)	# 27-31
    sprite('na408_00', 5)	# 32-36

@State
def TrapB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
    sprite('na408_00', 4)	# 1-4
    sprite('na408_01', 4)	# 5-8
    sprite('na408_02', 4)	# 9-12
    SFX_3('na004')
    sprite('na408_03', 7)	# 13-19
    Unknown23029(11, 401, 0)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    Unknown38(7, 1)
    sprite('na408_02', 7)	# 20-26
    Recovery()
    sprite('na408_01', 5)	# 27-31
    sprite('na408_00', 5)	# 32-36

@State
def TrapEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na408_00', 3)	# 1-3
    sprite('na408_01', 3)	# 4-6
    sprite('na408_02', 3)	# 7-9
    Unknown23029(11, 401, 0)
    Unknown23125('')
    Unknown2058(-5000)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    Unknown38(7, 1)
    Unknown23029(7, 3004, 0)
    SFX_3('na004')
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    Unknown38(4, 1)
    Unknown23029(4, 3004, 0)
    sprite('na408_03', 7)	# 10-16
    Recovery()
    sprite('na408_02', 7)	# 17-23
    sprite('na408_01', 5)	# 24-28
    sprite('na408_00', 6)	# 29-34

@State
def AirTrapA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na409_00', 3)	# 1-3
    sprite('na409_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(5, 1)
    sprite('na409_02', 3)	# 7-9
    sprite('na409_03', 7)	# 10-16
    Unknown23029(11, 401, 0)
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    Unknown38(4, 1)
    sprite('na409_03', 4)	# 17-20
    sprite('na409_04', 4)	# 21-24
    Recovery()
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    sprite('na409_05', 4)	# 25-28

@State
def AirTrapB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)
    sprite('na409_00', 3)	# 1-3
    sprite('na409_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(5, 1)
    sprite('na409_02', 3)	# 7-9
    sprite('na409_03', 6)	# 10-15
    Unknown23029(11, 401, 0)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    Unknown38(7, 1)
    sprite('na409_03', 4)	# 16-19
    sprite('na409_04', 4)	# 20-23
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    Recovery()
    sprite('na409_05', 5)	# 24-28

@State
def AirTrapEX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown11063(1)

        def upon_STATE_END():
            SLOT_8 = 0
    sprite('na409_00', 3)	# 1-3
    sprite('na409_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown22004(5, 1)
    sprite('na409_02', 5)	# 7-11
    Unknown23029(11, 401, 0)
    Unknown23125('')
    Unknown2058(-5000)
    callSubroutine('Shot_Stack2')
    GFX_0('TrapMatome', 103)
    Unknown38(7, 1)
    Unknown23029(7, 3004, 0)
    SLOT_8 = 1
    callSubroutine('Shot_Stack')
    GFX_0('TrapMatome', 103)
    Unknown38(4, 1)
    Unknown23029(4, 3004, 0)
    sprite('na409_03', 2)	# 12-13
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    Recovery()
    sprite('na409_04', 2)	# 14-15
    sprite('na409_05', 2)	# 16-17

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
    sprite('na400_00', 2)	# 1-2
    GFX_0('BarrierJizoku', 0)
    GuardPoint_(1)
    Unknown22031(4, 14)
    Unknown7007('706e613230305f30000000000000000064000000706e613230305f31000000000000000064000000706e613230305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('na005')

    def upon_52():
        clearUponHandler(52)
        if (SLOT_19 <= 350000):
            sendToLabel(1)
        else:
            sendToLabel(0)
    sprite('na400_00', 1)	# 3-3
    Unknown23029(11, 403, 0)
    sprite('na400_01', 3)	# 4-6
    sprite('na400_02', 3)	# 7-9
    sprite('na400_00', 3)	# 10-12
    sprite('na400_01', 3)	# 13-15
    sprite('na400_02', 3)	# 16-18
    Unknown21015('426172726965724a697a6f6b7500000000000000000000000000000000000000c40b000000000000')
    clearUponHandler(52)
    setInvincible(0)
    sprite('na400_00', 3)	# 19-21
    sprite('na400_01', 3)	# 22-24
    sprite('na400_02', 3)	# 25-27
    sprite('na400_00', 3)	# 28-30
    sprite('na400_01', 3)	# 31-33
    sprite('na400_02', 3)	# 34-36
    sprite('na400_06', 3)	# 37-39
    sprite('na400_07', 3)	# 40-42
    sprite('na400_08', 3)	# 43-45
    ExitState()
    label(1)
    clearUponHandler(52)
    sprite('na400_00', 4)	# 46-49
    sprite('na400_01', 3)	# 50-52
    sprite('na400_02', 2)	# 53-54
    sprite('na400_03', 4)	# 55-58
    GFX_0('ImpactReversal', 1)
    SLOT_51 = 0
    SFX_3('na003')
    ScreenShake(20000, 0)
    Unknown7007('706e613230315f30000000000000000064000000706e613230315f31000000000000000064000000706e613230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na400_05', 2)	# 59-60
    setInvincible(0)
    sprite('na400_06', 2)	# 61-62
    sprite('na400_04', 4)	# 63-66
    sprite('na400_05', 4)	# 67-70
    sprite('na400_06', 4)	# 71-74
    Unknown21015('426172726965724a697a6f6b7500000000000000000000000000000000000000c40b000000000000')
    sprite('na400_04', 6)	# 75-80
    sprite('na400_05', 6)	# 81-86
    sprite('na400_07', 6)	# 87-92
    sprite('na400_08', 6)	# 93-98
    ExitState()
    label(0)
    clearUponHandler(52)
    sprite('na400_00', 4)	# 99-102
    sprite('na400_01', 3)	# 103-105
    sprite('na400_02', 2)	# 106-107
    sprite('na400_03', 4)	# 108-111
    GFX_0('DanganReversal', 3)
    SLOT_51 = 0
    SFX_3('na002')
    Unknown7007('706e613230325f30000000000000000064000000706e613230325f31000000000000000064000000706e613230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('na400_04', 4)	# 112-115
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('na400_05', 4)	# 116-119
    sprite('na400_06', 4)	# 120-123
    sprite('na400_04', 4)	# 124-127
    Unknown21015('426172726965724a697a6f6b7500000000000000000000000000000000000000c40b000000000000')
    sprite('na400_05', 6)	# 128-133
    sprite('na400_06', 6)	# 134-139
    sprite('na400_04', 6)	# 140-145
    sprite('na400_07', 6)	# 146-151
    sprite('na400_08', 6)	# 152-157
    ExitState()

@State
def SecretGunA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)

        def upon_LANDING():
            sendToLabel(3)
    sprite('na430_00', 3)	# 1-3
    Unknown1084(1)
    sprite('na430_00', 3)	# 4-6
    tag_voice(1, 'pna252_0', 'pna252_1', '', '')
    sprite('na430_01', 4)	# 7-10
    physicsXImpulse(-15000)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('na430_02', 3)	# 11-13
    Unknown2036(42, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('na430_03', 3)	# 14-16
    sprite('na430_04', 3)	# 17-19
    sprite('na430_05', 3)	# 20-22
    sprite('na430_06', 2)	# 23-24
    sprite('na430_07', 2)	# 25-26
    sprite('na430_08', 2)	# 27-28
    sprite('na430_09', 25)	# 29-53
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_09', 2)	# 54-55
    GFX_0('DanganKakushiA', 1)
    Unknown21007(1, 32)
    physicsXImpulse(-300)
    physicsYImpulse(300)
    tag_voice(0, 'pna251_0', 'pna251_1', '', '')
    SFX_3('na008')
    sprite('na430_09', 1)	# 56-56
    setInvincible(0)
    sprite('na430_10', 2)	# 57-58
    sprite('na430_08', 2)	# 59-60
    sprite('na430_09', 2)	# 61-62
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 63-64
    sprite('na430_08', 2)	# 65-66
    sprite('na430_09', 2)	# 67-68
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 69-70
    sprite('na430_08', 2)	# 71-72
    sprite('na430_09', 2)	# 73-74
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 75-76
    sprite('na430_08', 2)	# 77-78
    sprite('na430_09', 2)	# 79-80
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 81-82
    sprite('na430_08', 2)	# 83-84
    sprite('na430_09', 2)	# 85-86
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 87-88
    sprite('na430_08', 2)	# 89-90
    sprite('na430_09', 2)	# 91-92
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 93-94
    sprite('na430_08', 2)	# 95-96
    sprite('na430_09', 2)	# 97-98
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 99-100
    sprite('na430_08', 2)	# 101-102
    sprite('na430_09', 2)	# 103-104
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 105-106
    sprite('na430_08', 2)	# 107-108
    sprite('na430_09', 2)	# 109-110
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 111-112
    sprite('na430_08', 2)	# 113-114
    sprite('na430_09', 2)	# 115-116
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 117-118
    sprite('na430_08', 2)	# 119-120
    sprite('na430_09', 2)	# 121-122
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 123-124
    sprite('na430_11', 4)	# 125-128
    physicsXImpulse(-7000)
    physicsYImpulse(15000)
    setGravity(1800)
    sprite('na430_12', 5)	# 129-133
    sprite('na430_13', 5)	# 134-138
    sprite('na430_14', 5)	# 139-143
    sprite('na430_15', 5)	# 144-148
    sprite('na430_16', 5)	# 149-153
    label(2)
    sprite('na020_07', 4)	# 154-157
    sprite('na020_08', 4)	# 158-161
    gotoLabel(2)
    label(3)
    sprite('na010_00', 3)	# 162-164
    Unknown1084(1)
    sprite('na211_00', 4)	# 165-168
    sprite('na010_01', 4)	# 169-172
    sprite('na010_00', 4)	# 173-176

@State
def SecretGunB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)

        def upon_LANDING():
            sendToLabel(3)

        def upon_43():
            if (SLOT_48 == 9001):
                if (not SLOT_63):
                    SLOT_63 = 1
            if (SLOT_48 == 9002):
                if (not SLOT_64):
                    SLOT_64 = 1
            if (SLOT_48 == 9003):
                if (not SLOT_65):
                    SLOT_65 = 1
            if (SLOT_48 == 9004):
                if (not SLOT_66):
                    SLOT_66 = 1
    label(0)
    sprite('na430_01', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(-17000)
    physicsYImpulse(36000)
    setGravity(2800)
    sprite('na430_02', 1)	# 4-4
    tag_voice(1, 'pna250_0', 'pna250_1', '', '')
    sprite('na430_03', 3)	# 5-7
    sprite('na430_04', 3)	# 8-10
    sprite('na430_05', 3)	# 11-13
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('na430_30', 3)	# 14-16
    sprite('na430_31', 3)	# 17-19
    sprite('na430_32', 3)	# 20-22
    sprite('na430_33', 29)	# 23-51
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_17', 4)	# 52-55
    GFX_0('DanganKakushiB', 0)
    physicsXImpulse(0)
    physicsYImpulse(0)
    tag_voice(0, 'pna253_0', 'pna253_1', '', '')
    SFX_3('na009')
    sprite('na430_18', 4)	# 56-59
    physicsXImpulse(-10000)
    physicsYImpulse(18000)
    setGravity(1800)
    sprite('na430_19', 8)	# 60-67
    sprite('na430_20', 6)	# 68-73
    setInvincible(0)
    sprite('na430_14', 6)	# 74-79
    sprite('na430_15', 5)	# 80-84
    sprite('na430_16', 5)	# 85-89
    label(2)
    sprite('na020_07', 4)	# 90-93
    sprite('na020_08', 4)	# 94-97
    gotoLabel(2)
    label(3)
    sprite('na010_00', 3)	# 98-100
    Unknown1084(1)
    sprite('na211_00', 4)	# 101-104
    sprite('na010_01', 4)	# 105-108
    sprite('na010_00', 4)	# 109-112

@State
def SecretGunOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        Unknown13024(0)
        Unknown23055('')

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown13024(1)
            if (SLOT_48 == 9001):
                if (not SLOT_63):
                    SLOT_63 = 1
            if (SLOT_48 == 9002):
                if (not SLOT_64):
                    SLOT_64 = 1
            if (SLOT_48 == 9003):
                if (not SLOT_65):
                    SLOT_65 = 1
            if (SLOT_48 == 9004):
                if (not SLOT_66):
                    SLOT_66 = 1

        def upon_LANDING():
            sendToLabel(3)
    if SLOT_36:
        _gotolabel(0)
    sprite('na430_00', 3)	# 1-3
    Unknown1084(1)
    sprite('na430_00', 3)	# 4-6
    tag_voice(1, 'pna252_0', 'pna252_1', '', '')
    sprite('na430_01', 4)	# 7-10
    physicsXImpulse(-15000)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('na430_02', 3)	# 11-13
    Unknown2036(42, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('na430_03', 3)	# 14-16
    sprite('na430_04', 3)	# 17-19
    sprite('na430_05', 3)	# 20-22
    sprite('na430_06', 2)	# 23-24
    sprite('na430_07', 2)	# 25-26
    sprite('na430_08', 2)	# 27-28
    sprite('na430_09', 25)	# 29-53
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('na430_01', 3)	# 54-56
    Unknown1084(1)
    physicsXImpulse(-17000)
    physicsYImpulse(36000)
    setGravity(2800)
    sprite('na430_02', 1)	# 57-57
    tag_voice(1, 'pna250_0', 'pna250_1', '', '')
    sprite('na430_03', 3)	# 58-60
    sprite('na430_04', 3)	# 61-63
    sprite('na430_05', 3)	# 64-66
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('na430_06', 3)	# 67-69
    sprite('na430_07', 3)	# 70-72
    sprite('na430_08', 3)	# 73-75
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_09', 29)	# 76-104
    loopRest()
    gotoLabel(1)
    label(1)
    sprite('na430_09', 2)	# 105-106
    GFX_0('DanganKakushiA', 1)
    Unknown21007(1, 32)
    physicsXImpulse(-300)
    physicsYImpulse(300)
    tag_voice(0, 'pna251_0', 'pna251_1', '', '')
    SFX_3('na008')
    sprite('na430_10', 2)	# 107-108
    sprite('na430_08', 2)	# 109-110
    sprite('na430_09', 2)	# 111-112
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 113-114
    sprite('na430_08', 2)	# 115-116
    sprite('na430_09', 2)	# 117-118
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 119-120
    sprite('na430_08', 2)	# 121-122
    sprite('na430_09', 2)	# 123-124
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 125-126
    sprite('na430_08', 2)	# 127-128
    sprite('na430_09', 2)	# 129-130
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 131-132
    sprite('na430_08', 2)	# 133-134
    sprite('na430_09', 2)	# 135-136
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 137-138
    sprite('na430_08', 2)	# 139-140
    sprite('na430_09', 2)	# 141-142
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 143-144
    sprite('na430_08', 2)	# 145-146
    sprite('na430_09', 2)	# 147-148
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 149-150
    sprite('na430_08', 2)	# 151-152
    sprite('na430_09', 2)	# 153-154
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 155-156
    sprite('na430_08', 2)	# 157-158
    sprite('na430_09', 2)	# 159-160
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 161-162
    sprite('na430_08', 2)	# 163-164
    sprite('na430_09', 2)	# 165-166
    GFX_0('DanganKakushiA', 1)
    SFX_3('na008')
    sprite('na430_10', 2)	# 167-168
    sprite('na430_08', 2)	# 169-170
    sprite('na430_09', 2)	# 171-172
    GFX_0('DanganKakushiA', 1)
    Unknown23029(1, 3013, 0)
    SFX_3('na008')
    sprite('na430_10', 2)	# 173-174
    sprite('na430_11', 3)	# 175-177
    sprite('na430_12', 3)	# 178-180
    sprite('na430_02', 4)	# 181-184
    sprite('na430_03', 4)	# 185-188
    sprite('na430_04', 4)	# 189-192
    sprite('na430_05', 4)	# 193-196
    sprite('na430_30', 3)	# 197-199
    sprite('na430_31', 5)	# 200-204
    sprite('na430_32', 5)	# 205-209
    sprite('na430_33', 48)	# 210-257
    Unknown2036(50, -1, 0)
    physicsXImpulse(-500)
    physicsYImpulse(-500)
    setGravity(0)
    sprite('na430_17', 4)	# 258-261
    GFX_0('DanganKakushiB', 0)
    Unknown36(1)
    Unknown11091(15)
    AttackP1(48)
    AttackP2(100)
    Unknown35()
    physicsXImpulse(0)
    physicsYImpulse(0)
    tag_voice(0, 'pna253_0', 'pna253_1', '', '')
    SFX_3('na009')
    sprite('na430_18', 4)	# 262-265
    physicsXImpulse(-15000)
    physicsYImpulse(18000)
    setGravity(1800)
    sprite('na430_19', 8)	# 266-273
    sprite('na430_20', 6)	# 274-279
    setInvincible(0)
    sprite('na430_14', 6)	# 280-285
    sprite('na430_15', 5)	# 286-290
    sprite('na430_16', 5)	# 291-295
    label(2)
    sprite('na020_07', 4)	# 296-299
    sprite('na020_08', 4)	# 300-303
    gotoLabel(2)
    label(3)
    sprite('na010_00', 3)	# 304-306
    Unknown1084(1)
    sprite('na211_00', 4)	# 307-310
    sprite('na010_01', 4)	# 311-314
    sprite('na010_00', 4)	# 315-318

@State
def UltimateKill():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        setInvincible(1)
        Unknown23055('')

        def upon_12():
            if SLOT_6:
                Unknown13024(0)
    sprite('na432_00', 4)	# 1-4
    Unknown1084(1)
    sprite('na432_01', 36)	# 5-40
    Unknown2036(72, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pna254_0', 'pna254_1', '', '')
    sprite('na432_02', 3)	# 41-43
    sprite('na432_03', 3)	# 44-46
    sprite('na432_04', 3)	# 47-49
    sprite('na432_05', 3)	# 50-52
    sprite('na432_06', 3)	# 53-55
    sprite('na432_07', 3)	# 56-58
    sprite('na432_08', 4)	# 59-62
    Unknown23029(11, 502, 0)
    sprite('na432_09', 4)	# 63-66
    sprite('na432_10', 4)	# 67-70
    sprite('na432_11', 2)	# 71-72
    sprite('na432_11', 2)	# 73-74
    setInvincible(0)
    sprite('na432_09', 4)	# 75-78
    sprite('na432_10', 2)	# 79-80
    sprite('na432_10', 2)	# 81-82
    tag_voice(0, 'pna255_0', 'pna255_1', '', '')
    sprite('na432_11', 3)	# 83-85
    sprite('na432_12', 3)	# 86-88
    sprite('na432_13', 3)	# 89-91
    sprite('na432_14', 3)	# 92-94
    sprite('na432_15', 3)	# 95-97
    sprite('na432_16', 3)	# 98-100

@State
def UltimateKillOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)

        def upon_12():
            if SLOT_6:
                Unknown13024(0)
    sprite('na432_00', 4)	# 1-4
    Unknown1084(1)
    sprite('na432_01', 36)	# 5-40
    Unknown2036(72, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'pna254_0', 'pna254_1', '', '')
    sprite('na432_02', 3)	# 41-43
    sprite('na432_03', 3)	# 44-46
    sprite('na432_04', 3)	# 47-49
    sprite('na432_05', 3)	# 50-52
    sprite('na432_06', 3)	# 53-55
    sprite('na432_07', 3)	# 56-58
    sprite('na432_08', 4)	# 59-62
    Unknown23029(11, 503, 0)
    sprite('na432_09', 4)	# 63-66
    sprite('na432_10', 4)	# 67-70
    sprite('na432_11', 2)	# 71-72
    sprite('na432_11', 2)	# 73-74
    setInvincible(0)
    sprite('na432_09', 4)	# 75-78
    sprite('na432_10', 2)	# 79-80
    sprite('na432_10', 2)	# 81-82
    tag_voice(1, 'pna255_0', 'pna255_1', '', '')
    sprite('na432_11', 3)	# 83-85
    sprite('na432_12', 3)	# 86-88
    sprite('na432_13', 3)	# 89-91
    sprite('na432_14', 3)	# 92-94
    sprite('na432_15', 3)	# 95-97
    sprite('na432_16', 3)	# 98-100

@State
def UltimateKillAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        setInvincible(1)
        Unknown23055('')

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown13024(0)
        Unknown2003(1)
        SLOT_34 = 0
    sprite('na254_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('na254_01', 3)	# 4-6
    tag_voice(1, 'pna256_0', 'pna256_1', '', '')
    sprite('na254_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 504, 0)
    clearUponHandler(2)
    sprite('na254_03', 5)	# 10-14
    Unknown2036(30, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('na254_04', 5)	# 15-19
    sprite('na254_05', 5)	# 20-24
    sprite('na254_03', 5)	# 25-29
    sprite('na254_04', 5)	# 30-34
    sprite('na254_05', 5)	# 35-39
    sprite('na255_00', 4)	# 40-43
    sprite('na255_01', 3)	# 44-46
    sprite('na255_02', 15)	# 47-61
    setInvincible(0)
    sprite('na255_03', 3)	# 62-64
    sprite('na255_04', 3)	# 65-67
    sprite('na255_05', 3)	# 68-70
    sprite('na255_01', 3)	# 71-73
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    physicsYImpulse(8000)
    sprite('na255_00', 3)	# 74-76

@State
def UltimateKillAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        setInvincible(1)
        Unknown23055('')

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown13024(0)
        SLOT_34 = 1
    sprite('na254_00', 3)	# 1-3
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('na254_01', 3)	# 4-6
    tag_voice(1, 'pna256_0', 'pna256_1', '', '')
    sprite('na254_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 504, 0)
    clearUponHandler(2)
    sprite('na254_03', 5)	# 10-14
    Unknown2036(30, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('na254_04', 5)	# 15-19
    sprite('na254_05', 5)	# 20-24
    sprite('na254_03', 5)	# 25-29
    sprite('na254_04', 5)	# 30-34
    sprite('na254_05', 5)	# 35-39
    sprite('na255_00', 4)	# 40-43
    sprite('na255_01', 3)	# 44-46
    sprite('na255_02', 15)	# 47-61
    setInvincible(0)
    sprite('na255_03', 3)	# 62-64
    sprite('na255_04', 3)	# 65-67
    sprite('na255_05', 3)	# 68-70
    sprite('na255_01', 3)	# 71-73
    Unknown1018()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    physicsYImpulse(8000)
    sprite('na255_00', 3)	# 74-76

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()

        def upon_STATE_END():
            Unknown2017(1)

        def upon_43():
            if (SLOT_48 == 9501):
                setInvincible(1)
                Unknown2017(0)
                Unknown23084(1)
                Unknown23088(1, 1)
                GFX_0('Ichigeki_RedRay', 100)
                Unknown23157(1)
                Unknown36(22)
                DashFMaxVelocity(18000)
                Unknown23169(0)
                Unknown23168(1)
                Unknown23164(0)
                Unknown23161(0)
                Unknown35()
            if (SLOT_48 == 9503):
                sendToLabel(10)
            if (SLOT_48 == 9502):
                sendToLabel(0)
    sprite('na450_00', 4)	# 1-4
    Unknown1084(1)
    Unknown22008(160)
    Unknown11063(1)
    tag_voice(1, 'pna290_0', 'pna290_1', '', '')
    sprite('na450_01', 4)	# 5-8
    sprite('na450_02', 4)	# 9-12
    sprite('na450_03', 6)	# 13-18
    Unknown2036(96, -1, 2)
    Unknown23147()
    GFX_0('RotateGun', 0)
    GFX_0('P4U_Cutin_Parent', 100)
    sprite('na450_04', 6)	# 19-24
    sprite('na450_05', 4)	# 25-28
    sprite('na450_06', 4)	# 29-32
    sprite('na450_07', 4)	# 33-36
    sprite('na450_08', 6)	# 37-42
    sprite('na450_09', 6)	# 43-48
    SFX_0('cloth_l')
    sprite('na450_10', 6)	# 49-54
    sprite('na450_11', 6)	# 55-60
    SFX_0('cloth_l')
    sprite('na450_12', 4)	# 61-64
    sprite('na450_13', 4)	# 65-68
    SFX_0('grip_fast')
    sprite('na450_14', 4)	# 69-72
    SFX_0('cloth_l')
    sprite('na450_15', 6)	# 73-78
    GFX_1('elef_cardlight_add2', 0)
    GFX_1('persona_summon', 0)
    sprite('na450_16', 6)	# 79-84
    SFX_0('cloth_l')
    sprite('na450_17', 6)	# 85-90
    clearUponHandler(3)
    if SLOT_38:
        op(2, 2, 51, 0, -1)
    Unknown23029(11, 950, 0)
    sprite('na450_15', 6)	# 91-96
    SFX_0('cloth_l')
    sprite('na450_16', 6)	# 97-102
    sprite('na450_17', 6)	# 103-108
    SFX_0('cloth_l')
    label(1)
    sprite('na450_15', 6)	# 109-114
    sprite('na450_16', 6)	# 115-120
    sprite('na450_17', 6)	# 121-126
    SFX_0('cloth_l')
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('null', 16)	# 127-142
    Unknown26('SCEF_Usugurai')
    Unknown26('Ichigeki_Marker')
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('null', 60)	# 143-202
    Unknown23024(0)
    GFX_0('Ichigeki_Scope', 100)
    GFX_0('Ichigeki_Scope2', 100)
    GFX_0('Ichigeki_Scope3', 100)
    sprite('null', 120)	# 203-322
    Unknown36(22)
    enterState('CmnActStand')
    teleportRelativeY(0)
    Unknown35()
    GFX_0('IchigekiCamera', 100)
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown4004('534345465f55737567757261690000000000000000000000000000000000000064000000')
    Unknown26('Ichigeki_Marker')
    SFX_3('na000')
    sprite('null', 12)	# 323-334
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    sprite('null', 4)	# 335-338
    Unknown21015('4963686967656b695f53636f70650000000000000000000000000000000000003d25000000000000')
    Unknown21015('4963686967656b695f53636f70653200000000000000000000000000000000003d25000000000000')
    Unknown21015('4963686967656b695f53636f70653300000000000000000000000000000000003d25000000000000')
    sprite('null', 40)	# 339-378
    Unknown26('SCEF_Usugurai')
    sprite('null', 1)	# 379-379
    GFX_0('IchigekiCutin', 103)
    tag_voice(0, 'pna291_0', 'pna291_1', '', '')
    Unknown4004('534345465f46616465426c61636b3132496e000000000000000000000000000064000000')
    Unknown36(22)
    enterState('CmnActStand')
    Unknown23168(0)
    Unknown23169(1)
    Unknown35()
    sprite('null', 79)	# 380-458
    Unknown36(22)
    Unknown51(1)
    Unknown35()
    sprite('null', 30)	# 459-488
    Unknown26('SCEF_FadeBlack12In')
    Unknown4004('534345465f46616465426c61636b31324f75740000000000000000000000000064000000')
    Unknown4004('534345465f55737567757261690000000000000000000000000000000000000064000000')
    GFX_0('Ichigeki_Scope', 100)
    GFX_0('Ichigeki_Scope2', 100)
    GFX_0('Ichigeki_Scope3', 100)
    GFX_0('IchigekiBlack', 100)
    Unknown36(22)
    Unknown51(0)
    Unknown35()
    sprite('null', 10)	# 489-498
    GFX_0('Ichigeki_shot', 103)
    sprite('null', 15)	# 499-513
    GFX_0('IchigekiTame_Atk', 100)
    Unknown21015('4963686967656b695f53636f70650000000000000000000000000000000000003e25000000000000')
    Unknown21015('4963686967656b695f53636f70653200000000000000000000000000000000003d25000000000000')
    Unknown21015('4963686967656b695f53636f70653300000000000000000000000000000000003d25000000000000')
    sprite('null', 15)	# 514-528
    GFX_0('IchigekiExplosion', 100)
    Unknown26('SCEF_Usugurai')
    sprite('null', 30)	# 529-558
    GFX_0('Ichigekiwhite', 100)
    sprite('null', 30)	# 559-588
    GFX_0('Ichigeki_Atk', 100)
    sprite('na000_00', 30)	# 589-618
    Unknown21015('4963686967656b6943616d6572610000000000000000000000000000000000003125000000000000')
    Unknown20000(1)
    sprite('na000_01', 6)	# 619-624
    sprite('na000_02', 6)	# 625-630
    sprite('na000_03', 6)	# 631-636
    sprite('na000_04', 6)	# 637-642
    sprite('na000_05', 6)	# 643-648
    sprite('na000_06', 6)	# 649-654
    sprite('na000_07', 6)	# 655-660
    sprite('na000_00', 6)	# 661-666
    sprite('na000_01', 6)	# 667-672
    sprite('na000_02', 6)	# 673-678
    sprite('na000_03', 6)	# 679-684
    sprite('na000_04', 6)	# 685-690
    tag_voice(1, 'pna292_0', 'pna292_1', '', '')
    sprite('na000_05', 6)	# 691-696
    sprite('na000_06', 6)	# 697-702
    sprite('na000_07', 6)	# 703-708
    sprite('na000_00', 6)	# 709-714
    sprite('na000_01', 6)	# 715-720
    sprite('na000_02', 6)	# 721-726
    sprite('na000_03', 6)	# 727-732
    sprite('na000_04', 6)	# 733-738
    sprite('na000_05', 6)	# 739-744
    sprite('na000_06', 6)	# 745-750
    sprite('na000_07', 6)	# 751-756
    sprite('na000_00', 6)	# 757-762
    sprite('na000_01', 6)	# 763-768
    sprite('na000_02', 6)	# 769-774
    sprite('na000_03', 6)	# 775-780
    sprite('na000_04', 6)	# 781-786
    sprite('na000_05', 6)	# 787-792
    sprite('na000_06', 6)	# 793-798
    sprite('na000_07', 6)	# 799-804
    loopRest()
    ExitState()
    label(0)
    sprite('na450_15', 6)	# 805-810
    setInvincible(0)
    Unknown23084(0)
    sprite('na450_16', 6)	# 811-816
    sprite('na450_17', 6)	# 817-822
    SFX_0('cloth_l')
    sprite('na450_15', 6)	# 823-828
    sprite('na450_16', 6)	# 829-834
    sprite('na450_17', 6)	# 835-840
    SFX_0('cloth_l')
    sprite('na450_15', 6)	# 841-846
    sprite('na450_16', 6)	# 847-852
    sprite('na450_17', 6)	# 853-858
    SFX_0('cloth_l')
    setInvincible(0)
    sprite('na450_18', 6)	# 859-864
    sprite('na450_19', 6)	# 865-870
    sprite('na450_20', 6)	# 871-876
    sprite('keep', 1)	# 877-877

@Subroutine
def MouthTableInit():
    Unknown18011('pna000', 14177, 14179, 14177, 14179, 14177, 12899, 24884, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna500', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna504', 12643, 13409, 13411, 13409, 14691, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna505', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna506', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna507', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24882, 25399, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna525', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 14128, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna403_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna403_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna600biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna600bno', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna600pbc', 12643, 13665, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna600rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14435, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601bes', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601bhz', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601pka', 12643, 13409, 13411, 13409, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601uhy', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601ume', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna601uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna700bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna700pmi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701bes', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25397, 24885, 25397, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701bno', 12643, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701pbc', 12643, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701rwi', 12643, 12641, 25394, 12344, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701uhy', 12643, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pna701uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bno')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bes')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bhz')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('ume')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('na600_00', 6)	# 2-7
    sprite('na600_01', 6)	# 8-13
    sprite('na600_02', 6)	# 14-19
    sprite('na600_03', 5)	# 20-24
    sprite('na600_04', 12)	# 25-36
    SFX_3('cloth_l')
    sprite('na600_05', 8)	# 37-44
    sprite('na600_06', 20)	# 45-64
    Unknown7006('pna500', 100, 895577712, 12592, 0, 0, 100, 895577712, 12848, 0, 0, 100, 895577712, 13872, 0, 0, 100)
    sprite('na600_07', 30)	# 65-94
    sprite('na600_08', 6)	# 95-100
    SFX_3('slash_rapier_fast')
    sprite('na600_09', 4)	# 101-104
    SFX_3('slash_rapier_fast')
    sprite('na600_10', 4)	# 105-108
    SFX_3('grip_fast')
    label(1)
    sprite('na600_11', 1)	# 109-109
    if SLOT_97:
        _gotolabel(1)
    sprite('na600_11', 30)	# 110-139
    sprite('na600_12', 6)	# 140-145
    Unknown23018(1)
    label(2)
    sprite('na000_00', 6)	# 146-151
    sprite('na000_01', 6)	# 152-157
    sprite('na000_02', 6)	# 158-163
    sprite('na000_03', 6)	# 164-169
    sprite('na000_04', 6)	# 170-175
    sprite('na000_05', 6)	# 176-181
    sprite('na000_06', 6)	# 182-187
    sprite('na000_07', 6)	# 188-193
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('na601_00', 6)	# 194-199
    sprite('na601_50', 3)	# 200-202
    sprite('na601_51', 3)	# 203-205
    sprite('na601_52', 3)	# 206-208
    sprite('na601_53', 75)	# 209-283
    Unknown7006('pna503', 100, 895577712, 13360, 0, 0, 100, 895577712, 13616, 0, 0, 100, 895577712, 14128, 0, 0, 100)
    sprite('na601_01', 6)	# 284-289
    sprite('na601_02', 3)	# 290-292
    sprite('na601_54', 14)	# 293-306
    SFX_3('walk_marble_heavy')
    sprite('na601_03', 6)	# 307-312
    sprite('na601_04', 6)	# 313-318
    sprite('na601_05', 6)	# 319-324
    sprite('na601_06', 4)	# 325-328
    sprite('na601_07', 4)	# 329-332
    sprite('na601_08', 6)	# 333-338
    sprite('na601_09', 6)	# 339-344
    sprite('na601_10', 6)	# 345-350
    sprite('na601_11', 6)	# 351-356
    SFX_3('hair')
    sprite('na601_12', 6)	# 357-362
    sprite('na601_13', 8)	# 363-370
    sprite('na601_14', 7)	# 371-377
    Unknown23018(1)
    label(11)
    sprite('na000_00', 6)	# 378-383
    sprite('na000_01', 6)	# 384-389
    sprite('na000_02', 6)	# 390-395
    sprite('na000_03', 6)	# 396-401
    sprite('na000_04', 6)	# 402-407
    sprite('na000_05', 6)	# 408-413
    sprite('na000_06', 6)	# 414-419
    sprite('na000_07', 6)	# 420-425
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('na000_00', 1)	# 426-426
    SFX_1('pna701ume')
    label(21)
    sprite('na000_00', 6)	# 427-432
    sprite('na000_01', 6)	# 433-438
    sprite('na000_02', 6)	# 439-444
    sprite('na000_03', 6)	# 445-450
    sprite('na000_04', 6)	# 451-456
    sprite('na000_05', 6)	# 457-462
    sprite('na000_06', 6)	# 463-468
    sprite('na000_07', 6)	# 469-474
    gotoLabel(21)
    label(100)
    sprite('na600_00', 6)	# 475-480
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('na600_01', 6)	# 481-486
    sprite('na600_02', 6)	# 487-492
    sprite('na600_03', 5)	# 493-497
    sprite('na600_04', 12)	# 498-509
    SFX_3('cloth_l')
    sprite('na600_05', 8)	# 510-517
    sprite('na600_06', 20)	# 518-537
    SFX_1('pna600bno')
    sprite('na600_07', 30)	# 538-567
    sprite('na600_08', 6)	# 568-573
    SFX_3('slash_rapier_fast')
    sprite('na600_09', 4)	# 574-577
    SFX_3('slash_rapier_fast')
    sprite('na600_10', 4)	# 578-581
    SFX_3('grip_fast')
    label(101)
    sprite('na600_11', 1)	# 582-582
    if SLOT_97:
        _gotolabel(101)
    sprite('na600_11', 30)	# 583-612
    sprite('na600_12', 6)	# 613-618
    Unknown21011(240)
    Unknown21007(24, 40)
    label(102)
    sprite('na000_00', 6)	# 619-624
    sprite('na000_01', 6)	# 625-630
    sprite('na000_02', 6)	# 631-636
    sprite('na000_03', 6)	# 637-642
    sprite('na000_04', 6)	# 643-648
    sprite('na000_05', 6)	# 649-654
    sprite('na000_06', 6)	# 655-660
    sprite('na000_07', 6)	# 661-666
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('na000_00', 1)	# 667-667
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1515000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('na000_00', 6)	# 668-673
    sprite('na000_01', 6)	# 674-679
    sprite('na000_02', 6)	# 680-685
    sprite('na000_03', 6)	# 686-691
    sprite('na000_04', 6)	# 692-697
    sprite('na000_05', 6)	# 698-703
    sprite('na000_06', 6)	# 704-709
    sprite('na000_07', 6)	# 710-715
    gotoLabel(111)
    label(112)
    sprite('na001_00', 7)	# 716-722
    SFX_1('pna601bes')
    sprite('na001_01', 7)	# 723-729
    sprite('na001_02', 7)	# 730-736
    sprite('na001_03', 10)	# 737-746
    sprite('na001_04', 7)	# 747-753
    sprite('na001_05', 7)	# 754-760
    sprite('na001_06', 10)	# 761-770
    sprite('na001_01', 7)	# 771-777
    sprite('na001_00', 7)	# 778-784
    Unknown23018(1)
    label(113)
    sprite('na000_00', 6)	# 785-790
    sprite('na000_01', 6)	# 791-796
    sprite('na000_02', 6)	# 797-802
    sprite('na000_03', 6)	# 803-808
    sprite('na000_04', 6)	# 809-814
    sprite('na000_05', 6)	# 815-820
    sprite('na000_06', 6)	# 821-826
    sprite('na000_07', 6)	# 827-832
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('na601_00', 6)	# 833-838
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('na601_50', 3)	# 839-841
    sprite('na601_51', 3)	# 842-844
    sprite('na601_52', 3)	# 845-847
    sprite('na601_53', 75)	# 848-922
    SFX_1('pna600pbc')
    sprite('na601_01', 6)	# 923-928
    sprite('na601_02', 3)	# 929-931
    sprite('na601_54', 14)	# 932-945
    SFX_3('walk_marble_heavy')
    sprite('na601_03', 6)	# 946-951
    sprite('na601_04', 6)	# 952-957
    sprite('na601_05', 6)	# 958-963
    sprite('na601_06', 4)	# 964-967
    sprite('na601_07', 4)	# 968-971
    sprite('na601_08', 6)	# 972-977
    sprite('na601_09', 6)	# 978-983
    sprite('na601_10', 6)	# 984-989
    sprite('na601_11', 6)	# 990-995
    SFX_3('hair')
    sprite('na601_12', 6)	# 996-1001
    sprite('na601_13', 8)	# 1002-1009
    sprite('na601_14', 7)	# 1010-1016
    label(121)
    sprite('na000_00', 6)	# 1017-1022
    sprite('na000_01', 6)	# 1023-1028
    sprite('na000_02', 6)	# 1029-1034
    sprite('na000_03', 6)	# 1035-1040
    sprite('na000_04', 6)	# 1041-1046
    sprite('na000_05', 6)	# 1047-1052
    sprite('na000_06', 6)	# 1053-1058
    sprite('na000_07', 6)	# 1059-1064
    if SLOT_97:
        _gotolabel(121)
    sprite('na000_00', 1)	# 1065-1065
    Unknown21007(24, 40)
    Unknown21011(300)
    label(122)
    sprite('na000_00', 6)	# 1066-1071
    sprite('na000_01', 6)	# 1072-1077
    sprite('na000_02', 6)	# 1078-1083
    sprite('na000_03', 6)	# 1084-1089
    sprite('na000_04', 6)	# 1090-1095
    sprite('na000_05', 6)	# 1096-1101
    sprite('na000_06', 6)	# 1102-1107
    sprite('na000_07', 6)	# 1108-1113
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('na000_00', 1)	# 1114-1114
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('na000_00', 6)	# 1115-1120
    sprite('na000_01', 6)	# 1121-1126
    sprite('na000_02', 6)	# 1127-1132
    sprite('na000_03', 6)	# 1133-1138
    sprite('na000_04', 6)	# 1139-1144
    sprite('na000_05', 6)	# 1145-1150
    sprite('na000_06', 6)	# 1151-1156
    sprite('na000_07', 6)	# 1157-1162
    gotoLabel(131)
    label(132)
    sprite('na001_00', 7)	# 1163-1169
    SFX_1('pna601bhz')
    sprite('na001_01', 7)	# 1170-1176
    sprite('na001_02', 7)	# 1177-1183
    sprite('na001_03', 10)	# 1184-1193
    sprite('na001_04', 7)	# 1194-1200
    sprite('na001_05', 7)	# 1201-1207
    sprite('na001_06', 10)	# 1208-1217
    sprite('na001_01', 7)	# 1218-1224
    sprite('na001_00', 7)	# 1225-1231
    Unknown23018(1)
    label(133)
    sprite('na000_00', 6)	# 1232-1237
    sprite('na000_01', 6)	# 1238-1243
    sprite('na000_02', 6)	# 1244-1249
    sprite('na000_03', 6)	# 1250-1255
    sprite('na000_04', 6)	# 1256-1261
    sprite('na000_05', 6)	# 1262-1267
    sprite('na000_06', 6)	# 1268-1273
    sprite('na000_07', 6)	# 1274-1279
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('na601_00', 32767)	# 1280-34046
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(141)
    label(141)
    sprite('na601_50', 3)	# 34047-34049
    sprite('na601_51', 3)	# 34050-34052
    sprite('na601_52', 3)	# 34053-34055
    sprite('na601_53', 75)	# 34056-34130
    SFX_1('pna601uhy')
    sprite('na601_01', 6)	# 34131-34136
    sprite('na601_02', 3)	# 34137-34139
    sprite('na601_54', 14)	# 34140-34153
    SFX_3('walk_marble_heavy')
    sprite('na601_03', 6)	# 34154-34159
    sprite('na601_04', 6)	# 34160-34165
    sprite('na601_05', 6)	# 34166-34171
    sprite('na601_06', 4)	# 34172-34175
    sprite('na601_07', 4)	# 34176-34179
    sprite('na601_08', 6)	# 34180-34185
    sprite('na601_09', 6)	# 34186-34191
    sprite('na601_10', 6)	# 34192-34197
    sprite('na601_11', 6)	# 34198-34203
    SFX_3('hair')
    sprite('na601_12', 6)	# 34204-34209
    sprite('na601_13', 8)	# 34210-34217
    sprite('na601_14', 7)	# 34218-34224
    Unknown23018(1)
    label(142)
    sprite('na000_00', 6)	# 34225-34230
    sprite('na000_01', 6)	# 34231-34236
    sprite('na000_02', 6)	# 34237-34242
    sprite('na000_03', 6)	# 34243-34248
    sprite('na000_04', 6)	# 34249-34254
    sprite('na000_05', 6)	# 34255-34260
    sprite('na000_06', 6)	# 34261-34266
    sprite('na000_07', 6)	# 34267-34272
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('na601_00', 6)	# 34273-34278
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)
    sprite('na601_50', 3)	# 34279-34281
    sprite('na601_51', 3)	# 34282-34284
    sprite('na601_52', 3)	# 34285-34287
    sprite('na601_53', 75)	# 34288-34362
    SFX_1('pna600rwi')
    sprite('na601_01', 6)	# 34363-34368
    sprite('na601_02', 3)	# 34369-34371
    sprite('na601_54', 14)	# 34372-34385
    SFX_3('walk_marble_heavy')
    sprite('na601_03', 6)	# 34386-34391
    sprite('na601_04', 6)	# 34392-34397
    sprite('na601_05', 6)	# 34398-34403
    sprite('na601_06', 4)	# 34404-34407
    sprite('na601_07', 4)	# 34408-34411
    sprite('na601_08', 6)	# 34412-34417
    sprite('na601_09', 6)	# 34418-34423
    sprite('na601_10', 6)	# 34424-34429
    sprite('na601_11', 6)	# 34430-34435
    SFX_3('hair')
    sprite('na601_12', 6)	# 34436-34441
    sprite('na601_13', 8)	# 34442-34449
    sprite('na601_14', 7)	# 34450-34456
    label(151)
    sprite('na000_00', 6)	# 34457-34462
    sprite('na000_01', 6)	# 34463-34468
    sprite('na000_02', 6)	# 34469-34474
    sprite('na000_03', 6)	# 34475-34480
    sprite('na000_04', 6)	# 34481-34486
    sprite('na000_05', 6)	# 34487-34492
    sprite('na000_06', 6)	# 34493-34498
    sprite('na000_07', 6)	# 34499-34504
    if SLOT_97:
        _gotolabel(151)
    sprite('na000_00', 1)	# 34505-34505
    Unknown21007(24, 40)
    Unknown21011(240)
    label(152)
    sprite('na000_00', 6)	# 34506-34511
    sprite('na000_01', 6)	# 34512-34517
    sprite('na000_02', 6)	# 34518-34523
    sprite('na000_03', 6)	# 34524-34529
    sprite('na000_04', 6)	# 34530-34535
    sprite('na000_05', 6)	# 34536-34541
    sprite('na000_06', 6)	# 34542-34547
    sprite('na000_07', 6)	# 34548-34553
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('na600_00', 1)	# 34554-34554
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1505000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('na600_00', 6)	# 34555-34560
    sprite('na600_01', 6)	# 34561-34566
    sprite('na600_02', 6)	# 34567-34572
    gotoLabel(161)
    label(162)
    sprite('na600_03', 5)	# 34573-34577
    SFX_1('pna601pka')
    sprite('na600_04', 12)	# 34578-34589
    SFX_3('cloth_l')
    sprite('na600_05', 8)	# 34590-34597
    sprite('na600_06', 20)	# 34598-34617
    sprite('na600_07', 30)	# 34618-34647
    sprite('na600_08', 6)	# 34648-34653
    SFX_3('slash_rapier_fast')
    sprite('na600_09', 4)	# 34654-34657
    SFX_3('slash_rapier_fast')
    sprite('na600_10', 4)	# 34658-34661
    SFX_3('grip_fast')
    label(163)
    sprite('na600_11', 1)	# 34662-34662
    if SLOT_97:
        _gotolabel(163)
    sprite('na600_11', 30)	# 34663-34692
    sprite('na600_12', 6)	# 34693-34698
    Unknown23018(1)
    label(164)
    sprite('na000_00', 6)	# 34699-34704
    sprite('na000_01', 6)	# 34705-34710
    sprite('na000_02', 6)	# 34711-34716
    sprite('na000_03', 6)	# 34717-34722
    sprite('na000_04', 6)	# 34723-34728
    sprite('na000_05', 6)	# 34729-34734
    sprite('na000_06', 6)	# 34735-34740
    sprite('na000_07', 6)	# 34741-34746
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('na601_00', 32767)	# 34747-67513
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(171)
    label(171)
    sprite('na601_50', 3)	# 67514-67516
    sprite('na601_51', 3)	# 67517-67519
    sprite('na601_52', 3)	# 67520-67522
    sprite('na601_53', 75)	# 67523-67597
    SFX_1('pna601uor')
    sprite('na601_01', 6)	# 67598-67603
    sprite('na601_02', 3)	# 67604-67606
    sprite('na601_54', 14)	# 67607-67620
    SFX_3('walk_marble_heavy')
    sprite('na601_03', 6)	# 67621-67626
    sprite('na601_04', 6)	# 67627-67632
    sprite('na601_05', 6)	# 67633-67638
    sprite('na601_06', 4)	# 67639-67642
    sprite('na601_07', 4)	# 67643-67646
    sprite('na601_08', 6)	# 67647-67652
    sprite('na601_09', 6)	# 67653-67658
    sprite('na601_10', 6)	# 67659-67664
    sprite('na601_11', 6)	# 67665-67670
    SFX_3('hair')
    sprite('na601_12', 6)	# 67671-67676
    sprite('na601_13', 8)	# 67677-67684
    sprite('na601_14', 7)	# 67685-67691
    Unknown23018(1)
    label(172)
    sprite('na000_00', 6)	# 67692-67697
    sprite('na000_01', 6)	# 67698-67703
    sprite('na000_02', 6)	# 67704-67709
    sprite('na000_03', 6)	# 67710-67715
    sprite('na000_04', 6)	# 67716-67721
    sprite('na000_05', 6)	# 67722-67727
    sprite('na000_06', 6)	# 67728-67733
    sprite('na000_07', 6)	# 67734-67739
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('na000_00', 1)	# 67740-67740
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('na000_00', 6)	# 67741-67746
    sprite('na000_01', 6)	# 67747-67752
    sprite('na000_02', 6)	# 67753-67758
    sprite('na000_03', 6)	# 67759-67764
    sprite('na000_04', 6)	# 67765-67770
    sprite('na000_05', 6)	# 67771-67776
    sprite('na000_06', 6)	# 67777-67782
    sprite('na000_07', 6)	# 67783-67788
    gotoLabel(181)
    label(182)
    sprite('na001_00', 7)	# 67789-67795
    SFX_1('pna601pmi')
    sprite('na001_01', 7)	# 67796-67802
    sprite('na001_02', 7)	# 67803-67809
    sprite('na001_03', 10)	# 67810-67819
    sprite('na001_04', 7)	# 67820-67826
    sprite('na001_05', 7)	# 67827-67833
    sprite('na001_06', 10)	# 67834-67843
    sprite('na001_01', 7)	# 67844-67850
    sprite('na001_00', 7)	# 67851-67857
    Unknown23018(1)
    label(183)
    sprite('na000_00', 6)	# 67858-67863
    sprite('na000_01', 6)	# 67864-67869
    sprite('na000_02', 6)	# 67870-67875
    sprite('na000_03', 6)	# 67876-67881
    sprite('na000_04', 6)	# 67882-67887
    sprite('na000_05', 6)	# 67888-67893
    sprite('na000_06', 6)	# 67894-67899
    sprite('na000_07', 6)	# 67900-67905
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('na600_00', 6)	# 67906-67911
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('na600_01', 6)	# 67912-67917
    SFX_1('pna600biz')
    sprite('na600_02', 6)	# 67918-67923
    sprite('na600_03', 5)	# 67924-67928
    sprite('na600_04', 12)	# 67929-67940
    SFX_3('cloth_l')
    sprite('na600_05', 8)	# 67941-67948
    sprite('na600_06', 20)	# 67949-67968
    sprite('na600_07', 30)	# 67969-67998
    sprite('na600_08', 6)	# 67999-68004
    SFX_3('slash_rapier_fast')
    sprite('na600_09', 4)	# 68005-68008
    SFX_3('slash_rapier_fast')
    sprite('na600_10', 4)	# 68009-68012
    SFX_3('grip_fast')
    label(191)
    sprite('na600_11', 1)	# 68013-68013
    if SLOT_97:
        _gotolabel(191)
    sprite('na600_12', 6)	# 68014-68019
    Unknown21011(240)
    Unknown21007(24, 40)
    label(192)
    sprite('na000_00', 6)	# 68020-68025
    sprite('na000_01', 6)	# 68026-68031
    sprite('na000_02', 6)	# 68032-68037
    sprite('na000_03', 6)	# 68038-68043
    sprite('na000_04', 6)	# 68044-68049
    sprite('na000_05', 6)	# 68050-68055
    sprite('na000_06', 6)	# 68056-68061
    sprite('na000_07', 6)	# 68062-68067
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('na600_00', 1)	# 68068-68068
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('na600_00', 6)	# 68069-68074
    sprite('na600_01', 6)	# 68075-68080
    sprite('na600_02', 6)	# 68081-68086
    gotoLabel(201)
    label(202)
    sprite('na600_03', 5)	# 68087-68091
    SFX_1('pna601ume')
    sprite('na600_04', 12)	# 68092-68103
    SFX_3('cloth_l')
    sprite('na600_05', 8)	# 68104-68111
    sprite('na600_06', 20)	# 68112-68131
    sprite('na600_07', 30)	# 68132-68161
    sprite('na600_08', 6)	# 68162-68167
    SFX_3('slash_rapier_fast')
    sprite('na600_09', 4)	# 68168-68171
    SFX_3('slash_rapier_fast')
    sprite('na600_10', 4)	# 68172-68175
    SFX_3('grip_fast')
    label(203)
    sprite('na600_11', 1)	# 68176-68176
    if SLOT_97:
        _gotolabel(203)
    sprite('na600_11', 30)	# 68177-68206
    sprite('na600_12', 6)	# 68207-68212
    Unknown23018(1)
    label(204)
    sprite('na000_00', 6)	# 68213-68218
    sprite('na000_01', 6)	# 68219-68224
    sprite('na000_02', 6)	# 68225-68230
    sprite('na000_03', 6)	# 68231-68236
    sprite('na000_04', 6)	# 68237-68242
    sprite('na000_05', 6)	# 68243-68248
    sprite('na000_06', 6)	# 68249-68254
    sprite('na000_07', 6)	# 68255-68260
    gotoLabel(204)
    ExitState()
    label(991)
    sprite('na000_00', 1)	# 68261-68261
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('na000_00', 6)	# 68262-68267
    sprite('na000_01', 6)	# 68268-68273
    sprite('na000_02', 6)	# 68274-68279
    sprite('na000_03', 6)	# 68280-68285
    sprite('na000_04', 6)	# 68286-68291
    sprite('na000_05', 6)	# 68292-68297
    sprite('na000_06', 6)	# 68298-68303
    sprite('na000_07', 6)	# 68304-68309
    gotoLabel(992)
    label(993)
    sprite('na033_00', 2)	# 68310-68311

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
    sprite('na033_01', 3)	# 68312-68314
    label(994)
    sprite('na033_01', 3)	# 68315-68317
    sprite('na033_02', 3)	# 68318-68320
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 68321-68323
    ExitState()

@State
def CmnActRoundWin():
    sprite('keep', 32767)	# 1-32767

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
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
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
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('ume'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('na610_00', 3)	# 4-6
    sprite('na610_01', 3)	# 7-9
    sprite('na610_02', 5)	# 10-14
    sprite('na610_03', 3)	# 15-17
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 18-20
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 21-24
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 25-31
    sprite('na610_05', 7)	# 32-38
    sprite('na610_06', 7)	# 39-45
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pna524', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pna402_0', 100, 878800496, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pna520', 100, 895577712, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('na610_07', 6)	# 46-51
    sprite('na610_08', 6)	# 52-57
    sprite('na610_07', 6)	# 58-63
    sprite('na610_08', 10)	# 64-73
    sprite('na610_09', 5)	# 74-78
    sprite('na610_10', 3)	# 79-81
    sprite('na610_11', 4)	# 82-85
    sprite('na610_12', 10)	# 86-95
    sprite('na610_13', 4)	# 96-99
    sprite('na610_14', 7)	# 100-106
    sprite('na610_15', 8)	# 107-114
    sprite('na610_16', 6)	# 115-120
    sprite('na610_17', 6)	# 121-126
    sprite('na610_18', 6)	# 127-132
    Unknown23018(1)
    label(1)
    sprite('na610_16', 6)	# 133-138
    sprite('na610_17', 6)	# 139-144
    sprite('na610_18', 6)	# 145-150
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('na611_00', 6)	# 151-156
    Unknown36(24)
    Unknown2034(0)
    Unknown2053(0)
    Unknown35()
    Unknown2004(1, 0)
    Unknown23029(11, 6001, 0)
    sprite('na611_01', 6)	# 157-162
    sprite('na611_02', 6)	# 163-168
    sprite('na611_03', 6)	# 169-174
    sprite('na611_04', 6)	# 175-180
    sprite('na611_05', 6)	# 181-186
    sprite('na611_06', 6)	# 187-192
    sprite('na611_07', 6)	# 193-198
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pna525', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pna402_0', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pna522', 100, 895577712, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('na611_08', 3)	# 199-201
    sprite('na611_09', 6)	# 202-207
    sprite('na611_10', 6)	# 208-213
    sprite('na611_08', 3)	# 214-216
    sprite('na611_09', 6)	# 217-222
    sprite('na611_10', 6)	# 223-228
    sprite('na611_08', 3)	# 229-231
    sprite('na611_09', 6)	# 232-237
    sprite('na611_10', 6)	# 238-243
    sprite('na611_08', 3)	# 244-246
    sprite('na611_09', 6)	# 247-252
    sprite('na611_10', 6)	# 253-258
    sprite('na611_08', 6)	# 259-264
    sprite('na611_09', 6)	# 265-270
    Unknown23018(1)
    label(11)
    sprite('na611_50', 3)	# 271-273
    sprite('na611_51', 6)	# 274-279
    sprite('na611_52', 6)	# 280-285
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('na000_00', 1)	# 286-286

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('na000_00', 6)	# 287-292
    sprite('na000_01', 6)	# 293-298
    sprite('na000_02', 6)	# 299-304
    sprite('na000_03', 6)	# 305-310
    sprite('na000_04', 6)	# 311-316
    sprite('na000_05', 6)	# 317-322
    sprite('na000_06', 6)	# 323-328
    sprite('na000_07', 6)	# 329-334
    gotoLabel(101)
    label(102)
    sprite('na611_00', 6)	# 335-340
    Unknown2004(1, 0)
    Unknown23029(11, 6001, 0)
    sprite('na611_01', 6)	# 341-346
    sprite('na611_02', 6)	# 347-352
    sprite('na611_03', 6)	# 353-358
    sprite('na611_04', 6)	# 359-364
    sprite('na611_05', 6)	# 365-370
    sprite('na611_06', 6)	# 371-376
    sprite('na611_07', 6)	# 377-382
    SFX_1('pna701bno')
    sprite('na611_08', 3)	# 383-385
    sprite('na611_09', 6)	# 386-391
    sprite('na611_10', 6)	# 392-397
    sprite('na611_08', 3)	# 398-400
    sprite('na611_09', 6)	# 401-406
    sprite('na611_10', 6)	# 407-412
    sprite('na611_08', 3)	# 413-415
    sprite('na611_09', 6)	# 416-421
    sprite('na611_10', 6)	# 422-427
    sprite('na611_08', 3)	# 428-430
    sprite('na611_09', 6)	# 431-436
    sprite('na611_10', 6)	# 437-442
    sprite('na611_08', 6)	# 443-448
    sprite('na611_09', 6)	# 449-454
    Unknown23018(1)
    label(103)
    sprite('na611_50', 3)	# 455-457
    sprite('na611_51', 6)	# 458-463
    sprite('na611_52', 6)	# 464-469
    loopRest()
    gotoLabel(103)
    label(110)
    sprite('na000_00', 1)	# 470-470

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('na000_00', 6)	# 471-476
    sprite('na000_01', 6)	# 477-482
    sprite('na000_02', 6)	# 483-488
    sprite('na000_03', 6)	# 489-494
    sprite('na000_04', 6)	# 495-500
    sprite('na000_05', 6)	# 501-506
    sprite('na000_06', 6)	# 507-512
    sprite('na000_07', 6)	# 513-518
    gotoLabel(111)
    label(112)
    sprite('na610_00', 3)	# 519-521
    sprite('na610_01', 3)	# 522-524
    sprite('na610_02', 5)	# 525-529
    sprite('na610_03', 3)	# 530-532
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 533-535
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 536-539
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 540-546
    sprite('na610_05', 7)	# 547-553
    sprite('na610_06', 7)	# 554-560
    sprite('na610_07', 6)	# 561-566
    SFX_1('pna701bhz')
    sprite('na610_08', 6)	# 567-572
    sprite('na610_07', 6)	# 573-578
    sprite('na610_08', 10)	# 579-588
    sprite('na610_09', 5)	# 589-593
    sprite('na610_10', 3)	# 594-596
    sprite('na610_11', 4)	# 597-600
    sprite('na610_12', 10)	# 601-610
    sprite('na610_13', 4)	# 611-614
    sprite('na610_14', 7)	# 615-621
    sprite('na610_15', 8)	# 622-629
    sprite('na610_16', 6)	# 630-635
    sprite('na610_17', 6)	# 636-641
    sprite('na610_18', 6)	# 642-647
    Unknown23018(1)
    label(113)
    sprite('na610_16', 6)	# 648-653
    sprite('na610_17', 6)	# 654-659
    sprite('na610_18', 6)	# 660-665
    loopRest()
    gotoLabel(113)
    label(120)
    sprite('na000_00', 1)	# 666-666

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('na000_00', 6)	# 667-672
    sprite('na000_01', 6)	# 673-678
    sprite('na000_02', 6)	# 679-684
    sprite('na000_03', 6)	# 685-690
    sprite('na000_04', 6)	# 691-696
    sprite('na000_05', 6)	# 697-702
    sprite('na000_06', 6)	# 703-708
    sprite('na000_07', 6)	# 709-714
    gotoLabel(121)
    label(122)
    sprite('na610_00', 3)	# 715-717
    sprite('na610_01', 3)	# 718-720
    sprite('na610_02', 5)	# 721-725
    sprite('na610_03', 3)	# 726-728
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 729-731
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 732-735
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 736-742
    sprite('na610_05', 7)	# 743-749
    sprite('na610_06', 7)	# 750-756
    sprite('na610_07', 6)	# 757-762
    SFX_1('pna701bes')
    sprite('na610_08', 6)	# 763-768
    sprite('na610_07', 6)	# 769-774
    sprite('na610_08', 10)	# 775-784
    sprite('na610_09', 5)	# 785-789
    sprite('na610_10', 3)	# 790-792
    sprite('na610_11', 4)	# 793-796
    sprite('na610_12', 10)	# 797-806
    sprite('na610_13', 4)	# 807-810
    sprite('na610_14', 7)	# 811-817
    sprite('na610_15', 8)	# 818-825
    sprite('na610_16', 6)	# 826-831
    sprite('na610_17', 6)	# 832-837
    sprite('na610_18', 6)	# 838-843
    Unknown23018(1)
    label(123)
    sprite('na610_16', 6)	# 844-849
    sprite('na610_17', 6)	# 850-855
    sprite('na610_18', 6)	# 856-861
    loopRest()
    gotoLabel(123)
    label(130)
    sprite('na000_00', 1)	# 862-862

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('na000_00', 6)	# 863-868
    sprite('na000_01', 6)	# 869-874
    sprite('na000_02', 6)	# 875-880
    sprite('na000_03', 6)	# 881-886
    sprite('na000_04', 6)	# 887-892
    sprite('na000_05', 6)	# 893-898
    sprite('na000_06', 6)	# 899-904
    sprite('na000_07', 6)	# 905-910
    gotoLabel(131)
    label(132)
    sprite('na611_00', 6)	# 911-916
    Unknown2004(1, 0)
    Unknown23029(11, 6001, 0)
    sprite('na611_01', 6)	# 917-922
    sprite('na611_02', 6)	# 923-928
    sprite('na611_03', 6)	# 929-934
    sprite('na611_04', 6)	# 935-940
    sprite('na611_05', 6)	# 941-946
    sprite('na611_06', 6)	# 947-952
    sprite('na611_07', 6)	# 953-958
    SFX_1('pna701pbc')
    sprite('na611_08', 3)	# 959-961
    sprite('na611_09', 6)	# 962-967
    sprite('na611_10', 6)	# 968-973
    sprite('na611_08', 3)	# 974-976
    sprite('na611_09', 6)	# 977-982
    sprite('na611_10', 6)	# 983-988
    sprite('na611_08', 3)	# 989-991
    sprite('na611_09', 6)	# 992-997
    sprite('na611_10', 6)	# 998-1003
    sprite('na611_08', 3)	# 1004-1006
    sprite('na611_09', 6)	# 1007-1012
    sprite('na611_10', 6)	# 1013-1018
    sprite('na611_08', 6)	# 1019-1024
    sprite('na611_09', 6)	# 1025-1030
    Unknown23018(1)
    label(133)
    sprite('na611_50', 3)	# 1031-1033
    sprite('na611_51', 6)	# 1034-1039
    sprite('na611_52', 6)	# 1040-1045
    loopRest()
    gotoLabel(133)
    label(140)
    sprite('na000_00', 1)	# 1046-1046

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('na000_00', 6)	# 1047-1052
    sprite('na000_01', 6)	# 1053-1058
    sprite('na000_02', 6)	# 1059-1064
    sprite('na000_03', 6)	# 1065-1070
    sprite('na000_04', 6)	# 1071-1076
    sprite('na000_05', 6)	# 1077-1082
    sprite('na000_06', 6)	# 1083-1088
    sprite('na000_07', 6)	# 1089-1094
    gotoLabel(141)
    label(142)
    sprite('na610_00', 3)	# 1095-1097
    sprite('na610_01', 3)	# 1098-1100
    sprite('na610_02', 5)	# 1101-1105
    sprite('na610_03', 3)	# 1106-1108
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 1109-1111
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 1112-1115
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 1116-1122
    sprite('na610_05', 7)	# 1123-1129
    sprite('na610_06', 7)	# 1130-1136
    SFX_1('pna701pka')
    sprite('na610_07', 6)	# 1137-1142
    sprite('na610_08', 6)	# 1143-1148
    sprite('na610_07', 6)	# 1149-1154
    sprite('na610_08', 10)	# 1155-1164
    sprite('na610_09', 5)	# 1165-1169
    sprite('na610_10', 3)	# 1170-1172
    sprite('na610_11', 4)	# 1173-1176
    sprite('na610_12', 10)	# 1177-1186
    sprite('na610_13', 4)	# 1187-1190
    sprite('na610_14', 7)	# 1191-1197
    sprite('na610_15', 8)	# 1198-1205
    sprite('na610_16', 6)	# 1206-1211
    sprite('na610_17', 6)	# 1212-1217
    sprite('na610_18', 6)	# 1218-1223
    Unknown23018(1)
    label(143)
    sprite('na610_16', 6)	# 1224-1229
    sprite('na610_17', 6)	# 1230-1235
    sprite('na610_18', 6)	# 1236-1241
    loopRest()
    gotoLabel(143)
    label(150)
    sprite('na000_00', 1)	# 1242-1242

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('na000_00', 6)	# 1243-1248
    sprite('na000_01', 6)	# 1249-1254
    sprite('na000_02', 6)	# 1255-1260
    sprite('na000_03', 6)	# 1261-1266
    sprite('na000_04', 6)	# 1267-1272
    sprite('na000_05', 6)	# 1273-1278
    sprite('na000_06', 6)	# 1279-1284
    sprite('na000_07', 6)	# 1285-1290
    gotoLabel(151)
    label(152)
    sprite('na610_00', 3)	# 1291-1293
    sprite('na610_01', 3)	# 1294-1296
    sprite('na610_02', 5)	# 1297-1301
    sprite('na610_03', 3)	# 1302-1304
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 1305-1307
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 1308-1311
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 1312-1318
    sprite('na610_05', 7)	# 1319-1325
    sprite('na610_06', 7)	# 1326-1332
    SFX_1('pna701uhy')
    sprite('na610_07', 6)	# 1333-1338
    sprite('na610_08', 6)	# 1339-1344
    sprite('na610_07', 6)	# 1345-1350
    sprite('na610_08', 10)	# 1351-1360
    sprite('na610_09', 5)	# 1361-1365
    sprite('na610_10', 3)	# 1366-1368
    sprite('na610_11', 4)	# 1369-1372
    sprite('na610_12', 10)	# 1373-1382
    sprite('na610_13', 4)	# 1383-1386
    sprite('na610_14', 7)	# 1387-1393
    sprite('na610_15', 8)	# 1394-1401
    sprite('na610_16', 6)	# 1402-1407
    sprite('na610_17', 6)	# 1408-1413
    sprite('na610_18', 6)	# 1414-1419
    Unknown23018(1)
    label(153)
    sprite('na610_16', 6)	# 1420-1425
    sprite('na610_17', 6)	# 1426-1431
    sprite('na610_18', 6)	# 1432-1437
    loopRest()
    gotoLabel(153)
    label(160)
    sprite('na000_00', 1)	# 1438-1438

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('na000_00', 6)	# 1439-1444
    sprite('na000_01', 6)	# 1445-1450
    sprite('na000_02', 6)	# 1451-1456
    sprite('na000_03', 6)	# 1457-1462
    sprite('na000_04', 6)	# 1463-1468
    sprite('na000_05', 6)	# 1469-1474
    sprite('na000_06', 6)	# 1475-1480
    sprite('na000_07', 6)	# 1481-1486
    gotoLabel(161)
    label(162)
    sprite('na610_00', 3)	# 1487-1489
    sprite('na610_01', 3)	# 1490-1492
    sprite('na610_02', 5)	# 1493-1497
    sprite('na610_03', 3)	# 1498-1500
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 1501-1503
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 1504-1507
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 1508-1514
    sprite('na610_05', 7)	# 1515-1521
    sprite('na610_06', 7)	# 1522-1528
    SFX_1('pna701rwi')
    sprite('na610_07', 6)	# 1529-1534
    sprite('na610_08', 6)	# 1535-1540
    sprite('na610_07', 6)	# 1541-1546
    sprite('na610_08', 10)	# 1547-1556
    sprite('na610_09', 5)	# 1557-1561
    sprite('na610_10', 3)	# 1562-1564
    sprite('na610_11', 4)	# 1565-1568
    sprite('na610_12', 10)	# 1569-1578
    sprite('na610_13', 4)	# 1579-1582
    sprite('na610_14', 7)	# 1583-1589
    sprite('na610_15', 8)	# 1590-1597
    sprite('na610_16', 6)	# 1598-1603
    sprite('na610_17', 6)	# 1604-1609
    sprite('na610_18', 6)	# 1610-1615
    Unknown23018(1)
    label(163)
    sprite('na610_16', 6)	# 1616-1621
    sprite('na610_17', 6)	# 1622-1627
    sprite('na610_18', 6)	# 1628-1633
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('na000_00', 1)	# 1634-1634

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('na000_00', 6)	# 1635-1640
    sprite('na000_01', 6)	# 1641-1646
    sprite('na000_02', 6)	# 1647-1652
    sprite('na000_03', 6)	# 1653-1658
    sprite('na000_04', 6)	# 1659-1664
    sprite('na000_05', 6)	# 1665-1670
    sprite('na000_06', 6)	# 1671-1676
    sprite('na000_07', 6)	# 1677-1682
    gotoLabel(171)
    label(172)
    sprite('na610_00', 3)	# 1683-1685
    sprite('na610_01', 3)	# 1686-1688
    sprite('na610_02', 5)	# 1689-1693
    sprite('na610_03', 3)	# 1694-1696
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 1697-1699
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 1700-1703
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 1704-1710
    sprite('na610_05', 7)	# 1711-1717
    sprite('na610_06', 7)	# 1718-1724
    SFX_1('pna701uor')
    sprite('na610_07', 6)	# 1725-1730
    sprite('na610_08', 6)	# 1731-1736
    sprite('na610_07', 6)	# 1737-1742
    sprite('na610_08', 10)	# 1743-1752
    sprite('na610_09', 5)	# 1753-1757
    sprite('na610_10', 3)	# 1758-1760
    sprite('na610_11', 4)	# 1761-1764
    sprite('na610_12', 10)	# 1765-1774
    sprite('na610_13', 4)	# 1775-1778
    sprite('na610_14', 7)	# 1779-1785
    sprite('na610_15', 8)	# 1786-1793
    sprite('na610_16', 6)	# 1794-1799
    sprite('na610_17', 6)	# 1800-1805
    sprite('na610_18', 6)	# 1806-1811
    Unknown23018(1)
    label(173)
    sprite('na610_16', 6)	# 1812-1817
    sprite('na610_17', 6)	# 1818-1823
    sprite('na610_18', 6)	# 1824-1829
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('na610_00', 3)	# 1830-1832
    sprite('na610_01', 3)	# 1833-1835
    sprite('na610_02', 5)	# 1836-1840
    sprite('na610_03', 3)	# 1841-1843
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 1844-1846
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 1847-1850
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 1851-1857
    sprite('na610_05', 7)	# 1858-1864
    sprite('na610_06', 7)	# 1865-1871
    sprite('na610_07', 6)	# 1872-1877
    SFX_1('pna700pmi')
    sprite('na610_08', 6)	# 1878-1883
    sprite('na610_07', 6)	# 1884-1889
    sprite('na610_08', 10)	# 1890-1899
    sprite('na610_09', 5)	# 1900-1904
    sprite('na610_10', 3)	# 1905-1907
    sprite('na610_11', 4)	# 1908-1911
    sprite('na610_12', 10)	# 1912-1921
    sprite('na610_13', 4)	# 1922-1925
    sprite('na610_14', 7)	# 1926-1932
    sprite('na610_15', 8)	# 1933-1940
    sprite('na610_16', 6)	# 1941-1946
    sprite('na610_17', 6)	# 1947-1952
    sprite('na610_18', 6)	# 1953-1958
    label(181)
    sprite('na610_16', 6)	# 1959-1964
    sprite('na610_17', 6)	# 1965-1970
    sprite('na610_18', 6)	# 1971-1976
    loopRest()
    if SLOT_97:
        _gotolabel(181)
    sprite('na610_16', 1)	# 1977-1977
    Unknown21007(24, 40)
    Unknown21011(320)
    label(182)
    sprite('na610_16', 6)	# 1978-1983
    sprite('na610_17', 6)	# 1984-1989
    sprite('na610_18', 6)	# 1990-1995
    loopRest()
    gotoLabel(182)
    label(190)
    sprite('na000_00', 1)	# 1996-1996

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('na000_00', 6)	# 1997-2002
    sprite('na000_01', 6)	# 2003-2008
    sprite('na000_02', 6)	# 2009-2014
    sprite('na000_03', 6)	# 2015-2020
    sprite('na000_04', 6)	# 2021-2026
    sprite('na000_05', 6)	# 2027-2032
    sprite('na000_06', 6)	# 2033-2038
    sprite('na000_07', 6)	# 2039-2044
    gotoLabel(191)
    label(192)
    sprite('na610_00', 3)	# 2045-2047
    sprite('na610_01', 3)	# 2048-2050
    sprite('na610_02', 5)	# 2051-2055
    sprite('na610_03', 3)	# 2056-2058
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 3)	# 2059-2061
    GFX_0('WinYakkyo', 0)
    sprite('na610_03', 4)	# 2062-2065
    GFX_0('WinYakkyo', 0)
    sprite('na610_04', 7)	# 2066-2072
    sprite('na610_05', 7)	# 2073-2079
    sprite('na610_06', 7)	# 2080-2086
    SFX_1('pna701ume')
    sprite('na610_07', 6)	# 2087-2092
    sprite('na610_08', 6)	# 2093-2098
    sprite('na610_07', 6)	# 2099-2104
    sprite('na610_08', 10)	# 2105-2114
    sprite('na610_09', 5)	# 2115-2119
    sprite('na610_10', 3)	# 2120-2122
    sprite('na610_11', 4)	# 2123-2126
    sprite('na610_12', 10)	# 2127-2136
    sprite('na610_13', 4)	# 2137-2140
    sprite('na610_14', 7)	# 2141-2147
    sprite('na610_15', 8)	# 2148-2155
    sprite('na610_16', 6)	# 2156-2161
    sprite('na610_17', 6)	# 2162-2167
    sprite('na610_18', 6)	# 2168-2173
    Unknown23018(1)
    label(193)
    sprite('na610_16', 6)	# 2174-2179
    sprite('na610_17', 6)	# 2180-2185
    sprite('na610_18', 6)	# 2186-2191
    loopRest()
    gotoLabel(193)

@State
def CmnActLose():
    sprite('na070_00', 15)	# 1-15
    if SLOT_158:
        Unknown7006('pna403_0', 100, 878800496, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('na070_01', 6)	# 16-21
    sprite('na070_02', 2)	# 22-23
    Unknown23018(1)
    sprite('na070_03', 32767)	# 24-32790
