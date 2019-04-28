@Subroutine
def PreInit():
    Unknown12019('62706800000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    WalkFSpeed(10000)
    WalkBSpeed(8000)
    JumpYVelocity(28000)
    SuperJumpYVelocity(30000)
    Unknown12007(12500)
    Unknown12009(7500)
    Unknown12008(20000)
    Unknown12010(12000)
    Unknown12011(1200)
    AirDashCount(0)
    Unknown12024(2)
    Unknown13039(2)
    Unknown2049(1)
    Unknown23003(0, 1, 17, 2, 10000, 0, -6908226, -65536)
    Unknown23041(0, 1)
    Move_Register('2ndDash66', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xe5)
    Unknown15013(4000)
    Unknown15014(4000)
    Unknown14015(0, 1500000, -400000, 400000, 200, 50)
    Move_EndRegister()
    Move_Register('2ndDash44', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xe4)
    Unknown15012(4000)
    Unknown15014(4000)
    Unknown14015(0, 400000, -400000, 400000, 200, 50)
    Move_EndRegister()
    Move_Register('2ndDash88', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xe7)
    Unknown15014(4000)
    Unknown14015(0, 400000, -400000, 400000, 200, 0)
    Move_EndRegister()
    Move_Register('2ndDash22', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_Input_(0xe2)
    Unknown14015(0, 400000, -400000, 400000, 200, 0)
    Move_EndRegister()
    Move_Register('SpDashF_Air', INPUT_SPECIALMOVE)
    Unknown14004(1)
    Move_AirGround_(0x2001)
    Move_Input_(0xda)
    Move_AirGround_(0x3037)
    Unknown14024('CheckEnableAirDash')
    Unknown15013(5000)
    Unknown14015(400000, 1000000, -400000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('SpDashB_Air', INPUT_SPECIALMOVE)
    Unknown14004(1)
    Move_AirGround_(0x2001)
    Move_Input_(0xdb)
    Move_AirGround_(0x3037)
    Unknown14024('CheckEnableAirDash')
    Unknown15014(4000)
    Unknown14015(400000, 1000000, -400000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('Swoop', INPUT_SPECIALMOVE)
    Unknown14004(1)
    Move_AirGround_(0x2001)
    Move_Input_(0xe2)
    Move_AirGround_(0x3037)
    Unknown14024('CheckEnableAirDash')
    Unknown15014(4000)
    Unknown14015(400000, 1000000, -400000, 200000, 200, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA_Lv1', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA_Lv2', 0x7)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv2')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA_Lv3', 0x7)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv3')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAAA_Lv1', 0x7)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAAA_Lv2', 0x7)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv2')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAAA_Lv3', 0x7)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv3')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown15021(2000)
    Unknown14015(0, 500000, 200000, 600000, 750, 10)
    Move_EndRegister()
    Move_Register('NmlAtk4AA', 0x6)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4AAA_Lv1', 0x6)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4AAA_Lv2', 0x6)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv2')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk4AAA_Lv3', 0x6)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv3')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(100000, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown15013(1500)
    Unknown14015(300000, 800000, -200000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB_Lv1', 0x19)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5BB_Lv2', 0x19)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv2')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk5BB_Lv3', 0x19)
    Unknown14005(1)
    Unknown14024('CheckActivateMagicLv3')
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown15009()
    Unknown15021(2000)
    Unknown14015(300000, 550000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 100, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(250)
    Unknown14015(200000, 550000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 500000, -100000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(-100000, 300000, -450000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5BB', 0x22)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(500000, 200000, -600000, -200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_Lv2', 0x34)
    Unknown14015(500000, 200000, -600000, -200000, 1000, 50)
    Unknown14024('CheckActivateMagicLv2')
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C_Lv3', 0x34)
    Unknown14015(500000, 200000, -600000, -200000, 1000, 50)
    Unknown14024('CheckActivateMagicLv3')
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('SpDashF_AirButtonInput', 0x1)
    Unknown14004(1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3037)
    Unknown14024('CheckEnableAirDash')
    Unknown14013('SpDashF_Air')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('SpDashB_AirButtonInput', 0x1)
    Unknown14004(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3037)
    Unknown14024('CheckEnableAirDash')
    Unknown14013('SpDashB_Air')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('SwoopButtonInput', 0x1)
    Unknown14004(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3037)
    Unknown14024('CheckEnableAirDash')
    Unknown14013('Swoop')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('2ndDash66ButtonInput', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('2ndDash66')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('2ndDash44ButtonInput', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('2ndDash44')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('2ndDash88ButtonInput', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x93)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('2ndDash88')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('2ndDash22ButtonInput', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2001)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('2ndDash22')
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('MagicActivateA_Lv0', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14013('MagicActivate_Lv0')
    Unknown14015(0, 500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateA_Lv1', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('CheckActivateMagicLv1')
    Unknown14015(800000, 1500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateA_Lv2', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('CheckActivateMagicLv2')
    Unknown14015(800000, 1500000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('MagicActivateA_Lv3', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('CheckActivateMagicLv3')
    Unknown14015(0, 1500000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('MagicActivateB_Lv0', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('MagicActivate_Lv0')
    Unknown14015(0, 500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateB_Lv1', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('CheckActivateMagicLv1')
    Unknown14015(0, 500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateB_Lv2', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('CheckActivateMagicLv2')
    Unknown14015(0, 500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateB_Lv3', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14024('CheckActivateMagicLv3')
    Unknown14015(0, 500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateEX_Lv0', INPUT_SPECIALMOVE)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('MagicActivate_Lv0')
    Unknown14015(0, 500000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('MagicActivateEX_Lv1', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14024('CheckActivateMagicLv1')
    Unknown14015(0, 500000, -200000, 200000, 0, 1)
    Move_EndRegister()
    Move_Register('MagicActivateEX_Lv2', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14024('CheckActivateMagicLv2')
    Unknown14015(0, 500000, -200000, 200000, 0, 1)
    Move_EndRegister()
    Move_Register('MagicActivateEX_Lv3', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14024('CheckActivateMagicLv3')
    Unknown14015(0, 500000, -200000, 200000, 0, 1)
    Move_EndRegister()
    Move_Register('MagicActivateEX_Special', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14024('CheckActivateMagicSpecial')
    Unknown14015(0, 500000, -200000, 200000, 0, 1)
    Move_EndRegister()
    Move_Register('LandAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 400000, -150000, 250000, 300, 50)
    Move_EndRegister()
    Move_Register('LandAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 500000, 200000, 600000, 100, 0)
    Move_EndRegister()
    Move_Register('LandAssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(0, 400000, -150000, 250000, 500, 50)
    Move_EndRegister()
    Move_Register('AirAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14024('CheckEnableAssaultAir')
    Unknown14015(0, 650000, -200000, 200000, 100, 1)
    Move_EndRegister()
    Move_Register('AirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 650000, -200000, 200000, 100, 1)
    Move_EndRegister()
    Move_Register('AirAssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(0, 400000, -150000, 250000, 100, 1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(-200000, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14015(-200000, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(2000)
    Unknown15011(10000)
    Unknown14015(400000, 1500000, 50000, 500000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateShotSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(2000)
    Unknown15011(10000)
    Unknown14015(400000, 1500000, 50000, 500000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateLock', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(2500)
    Unknown14015(0, 550000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateLockSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(2500)
    Unknown14015(0, 550000, -200000, 600000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15013(2000)
    Unknown14015(400000, 1500000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA_Lv1', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA_Lv2', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA_Lv3', 10000000)
    Unknown15024('NmlAtk5AAAA_Lv1', 'NmlAtk5AAAAA', 10000000)
    Unknown15024('NmlAtk5AAAA_Lv2', 'NmlAtk5AAAAA', 10000000)
    Unknown15024('NmlAtk5AAAA_Lv3', 'NmlAtk5AAAAA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB_Lv1', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB_Lv2', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB_Lv3', 10000000)
    Unknown15024('NmlAtk5BB_Lv1', 'LandAssaultA', 10000000)
    Unknown15024('NmlAtk5BB_Lv2', 'LandAssaultA', 10000000)
    Unknown15024('NmlAtk5BB_Lv3', 'LandAssaultA', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4AA', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk4AAA_Lv1', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk4AAA_Lv2', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk4AAA_Lv3', 10000000)
    Unknown15024('NmlAtk4AAA_Lv1', 'LandAssaultA', 10000000)
    Unknown15024('NmlAtk4AAA_Lv2', 'LandAssaultA', 10000000)
    Unknown15024('NmlAtk4AAA_Lv3', 'LandAssaultA', 10000000)
    Unknown12018(0, 'ph062_01')
    Unknown12018(1, 'ph062_03')
    Unknown12018(2, 'ph062_04')
    Unknown12018(3, 'ph062_05')
    Unknown12018(4, 'ph062_05')
    Unknown12018(5, 'ph062_06')
    Unknown12018(6, 'ph062_07')
    Unknown12018(7, 'ph041_02')
    Unknown12018(8, 'ph040_02')
    Unknown12018(9, 'ph045_02')
    Unknown12018(10, 'ph060_00')
    Unknown12018(11, 'ph060_01')
    Unknown12018(12, 'ph060_03')
    Unknown12018(13, 'ph060_05')
    Unknown12018(14, 'ph060_07')
    Unknown12018(15, 'ph060_14')
    Unknown12018(16, 'ph050_00')
    Unknown12018(17, 'ph052_00')
    Unknown12018(18, 'ph054_00')
    Unknown12018(19, 'ph000_00')
    Unknown12018(20, 'ph000_00')
    Unknown12018(25, 'ph063_00')
    Unknown12018(26, 'ph063_01')
    Unknown12018(27, 'ph063_02')
    Unknown12018(28, 'ph063_04')
    Unknown12018(29, 'ph063_11')
    Unknown12018(24, 'ph073_01')
    Unknown7010(0, 'bph000')
    Unknown7010(1, 'bph001')
    Unknown7010(2, 'bph002')
    Unknown7010(4, 'bph004')
    Unknown7010(5, 'bph005')
    Unknown7010(6, 'bph006')
    Unknown7010(8, 'bph008')
    Unknown7010(9, 'bph009')
    Unknown7010(10, 'bph010')
    Unknown7010(15, 'bph011')
    Unknown7010(16, 'bph012')
    Unknown7010(17, 'bph013')
    Unknown7010(18, 'bph014')
    Unknown7010(19, 'bph015')
    Unknown7010(20, 'bph016')
    Unknown7010(21, 'bph017')
    Unknown7010(22, 'bph018')
    Unknown7010(23, 'bph019')
    Unknown7010(24, 'bph020')
    Unknown7010(25, 'bph021')
    Unknown7010(28, 'bph022')
    Unknown7010(29, 'bph023')
    Unknown7010(30, 'bph024')
    Unknown7010(31, 'bph025')
    Unknown7010(32, 'bph026')
    Unknown7010(33, 'bph027')
    Unknown7010(34, 'bph028')
    Unknown7010(35, 'bph029')
    Unknown7010(36, 'bph030')
    Unknown7010(37, 'bph031')
    Unknown7010(39, 'bph032')
    Unknown7010(42, 'bph033')
    Unknown7010(43, 'bph034')
    Unknown7010(44, 'bph035')
    Unknown7010(45, 'bph036')
    Unknown7010(46, 'bph037')
    Unknown7010(47, 'bph038')
    Unknown7010(48, 'bph039')
    Unknown7010(49, 'bph040')
    Unknown7010(50, 'bph041')
    Unknown7010(52, 'bph042')
    Unknown7010(53, 'bph043')
    Unknown7010(54, 'bph100_0')
    Unknown7010(55, 'bph100_1')
    Unknown7010(56, 'bph100_2')
    Unknown7010(63, 'bph101_0')
    Unknown7010(64, 'bph101_1')
    Unknown7010(65, 'bph101_2')
    Unknown7010(57, 'bph102_0')
    Unknown7010(58, 'bph102_1')
    Unknown7010(59, 'bph102_2')
    Unknown7010(66, 'bph103_0')
    Unknown7010(67, 'bph103_1')
    Unknown7010(68, 'bph103_2')
    Unknown7010(60, 'bph104_0')
    Unknown7010(61, 'bph104_1')
    Unknown7010(62, 'bph104_2')
    Unknown7010(69, 'bph105_0')
    Unknown7010(70, 'bph105_1')
    Unknown7010(71, 'bph105_2')
    Unknown7010(72, 'bph150')
    Unknown7010(73, 'bph307_1')
    Unknown7010(74, 'bph152')
    Unknown7010(85, 'bph153')
    Unknown7010(87, 'bph154')
    Unknown7010(88, 'bph155')
    Unknown7010(96, 'bph161_0')
    Unknown7010(97, 'bph161_1')
    Unknown7010(92, 'bph162_0')
    Unknown7010(93, 'bph162_1')
    Unknown7010(98, 'bph163_0')
    Unknown7010(99, 'bph163_1')
    Unknown7010(100, 'bph164_0')
    Unknown7010(101, 'bph164_1')
    Unknown7010(105, 'bph165_0')
    Unknown7010(106, 'bph165_1')
    Unknown7010(102, 'bph166_0')
    Unknown7010(103, 'bph166_1')
    Unknown7010(90, 'bph167_0')
    Unknown7010(91, 'bph167_1')
    Unknown7010(107, 'bph168_0')
    Unknown7010(108, 'bph168_1')
    Unknown7010(110, 'bph169_0')
    Unknown7010(111, 'bph169_1')
    Unknown7010(94, 'bph400_0')
    Unknown7010(95, 'bph400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745350000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174654c6f636b0000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174654c6f636b5350000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def ActiveMagicAllDelete():
    Unknown21015('447269766541746b5f42524e00000000000000000000000000000000000000008913000000000000')
    Unknown23029(8, 5012, 0)
    Unknown21015('447269766541746b5f4747425f41544b4d6173746572000000000000000000009313000000000000')
    Unknown21015('447269766541746b5f42425200000000000000000000000000000000000000009d13000000000000')
    Unknown21015('447269766541746b5f47524e0000000000000000000000000000000000000000ed13000000000000')
    Unknown21015('447269766541746b5f5252470000000000000000000000000000000000000000f713000000000000')
    Unknown21015('447269766541746b5f47475200000000000000000000000000000000000000000114000000000000')
    Unknown21012('447269766541746b5f4747525f4300000000000000000000000000000000000020000000')
    Unknown21012('447269766541746b5f4747525f4c00000000000000000000000000000000000020000000')
    Unknown21012('447269766541746b5f4747525f4c4c000000000000000000000000000000000020000000')
    Unknown21012('447269766541746b5f4747525f5200000000000000000000000000000000000020000000')
    Unknown21012('447269766541746b5f4747525f5252000000000000000000000000000000000020000000')
    Unknown23029(7, 5201, 0)
    Unknown21015('447269766541746b5f52524200000000000000000000000000000000000000002923000000000000')

@Subroutine
def CheckEnableAirDash():
    SLOT_47 = 0
    op(7, 2, 4, 0, 1)
    if op(15, 2, 0, 0, 1):
        SLOT_47 = 1

@Subroutine
def CheckEnableAssaultAir():
    SLOT_47 = 0
    op(7, 2, 4, 0, 2)
    if op(15, 2, 0, 0, 2):
        SLOT_47 = 1

@Subroutine
def CheckActivateMagicLv1():
    SLOT_47 = 0
    if (SLOT_31 > 0):
        SLOT_47 = 1

@Subroutine
def CheckActivateMagicLv2():
    SLOT_47 = 0
    if (SLOT_31 >= 5000):
        SLOT_47 = 1

@Subroutine
def CheckActivateMagicLv3():
    SLOT_47 = 0
    if (SLOT_31 >= 10000):
        SLOT_47 = 1

@Subroutine
def CheckActivateMagicSpecial():
    SLOT_47 = 0
    if Unknown46(7):
        if (not SLOT_7):
            SLOT_47 = 1

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_90:
            Unknown58('TRI_BPHMagicPoint', 2, 67)
            if SLOT_67:
                Unknown47('02000000020000004300000000000000e8030000020000001f000000')
                callSubroutine('MagicIconUpDate')
        if SLOT_123:
            if SLOT_90:
                Unknown58('TRI_BPHMagicPoint', 2, 67)
                if SLOT_67:
                    Unknown47('02000000020000004300000000000000e8030000020000001f000000')
                    callSubroutine('MagicIconUpDate')
    if (not SLOT_21):
        callSubroutine('ActiveMagicAllDelete')
    if SLOT_37:
        if SLOT_4:
            SLOT_4 = 0

@Subroutine
def OnActionBegin():
    callSubroutine('MagicIconUpDate')
    if Unknown23148('CmnActTagBattleWait'):
        callSubroutine('ActiveMagicAllDelete')
        if SLOT_170:
            Unknown23008(0, 0)

@Subroutine
def OnPreDraw():
    Unknown23030('50485f4c696768740000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def CmnActStand():
    label(0)
    sprite('ph000_00', 7)	# 1-7
    sprite('ph000_01', 7)	# 8-14
    sprite('ph000_02', 7)	# 15-21
    sprite('ph000_03', 7)	# 22-28
    sprite('ph000_04', 7)	# 29-35
    sprite('ph000_05', 7)	# 36-42
    sprite('ph000_06', 7)	# 43-49
    sprite('ph000_07', 7)	# 50-56
    sprite('ph000_08', 7)	# 57-63
    sprite('ph000_09', 7)	# 64-70
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('ph001_00', 7)	# 71-77
    sprite('ph001_01', 7)	# 78-84
    sprite('ph001_02', 7)	# 85-91	 **attackbox here**
    SLOT_88 = 960
    SFX_1('bph000')
    GFX_0('ph001Eff', -1)
    SFX_0('015_blaze_2')
    sprite('ph001_03', 7)	# 92-98	 **attackbox here**
    sprite('ph001_04', 7)	# 99-105	 **attackbox here**
    sprite('ph001_05', 7)	# 106-112	 **attackbox here**
    sprite('ph001_06', 7)	# 113-119	 **attackbox here**
    label(1)
    sprite('ph001_02ex01', 7)	# 120-126	 **attackbox here**
    sprite('ph001_03ex01', 7)	# 127-133	 **attackbox here**
    sprite('ph001_04ex01', 7)	# 134-140	 **attackbox here**
    sprite('ph001_05ex01', 7)	# 141-147	 **attackbox here**
    sprite('ph001_06ex01', 7)	# 148-154	 **attackbox here**
    sprite('ph001_02', 7)	# 155-161	 **attackbox here**
    sprite('ph001_03', 7)	# 162-168	 **attackbox here**
    sprite('ph001_04', 7)	# 169-175	 **attackbox here**
    sprite('ph001_05', 7)	# 176-182	 **attackbox here**
    sprite('ph001_06', 7)	# 183-189	 **attackbox here**
    loopRest()
    gotoLabel(1)

@State
def CmnActStandTurn():
    sprite('ph003_00', 3)	# 1-3
    sprite('ph003_01', 3)	# 4-6
    sprite('ph003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('ph010_00', 4)	# 1-4
    sprite('ph010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ph010_02', 6)	# 1-6
    sprite('ph010_03', 6)	# 7-12
    sprite('ph010_04', 6)	# 13-18
    sprite('ph010_05', 6)	# 19-24
    sprite('ph010_06', 6)	# 25-30
    sprite('ph010_07', 6)	# 31-36
    sprite('ph010_08', 6)	# 37-42
    sprite('ph010_09', 6)	# 43-48
    sprite('ph010_10', 6)	# 49-54
    sprite('ph010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ph013_00', 3)	# 1-3
    sprite('ph013_01', 3)	# 4-6
    sprite('ph013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ph010_01', 4)	# 1-4
    sprite('ph010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    Unknown1045(0)
    sprite('ph023_00', 2)	# 1-2
    sprite('ph023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ph020_00', 4)	# 1-4
    sprite('ph020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ph020_02', 3)	# 1-3
    sprite('ph020_03', 3)	# 4-6
    sprite('ph020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ph020_05', 3)	# 1-3
    sprite('ph020_06', 3)	# 4-6
    label(0)
    sprite('ph020_07', 4)	# 7-10
    sprite('ph020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ph024_00', 3)	# 1-3
    sprite('ph024_01', 3)	# 4-6
    sprite('ph024_02', 3)	# 7-9
    sprite('ph024_03', 3)	# 10-12
    sprite('ph024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('ph024_00', 2)	# 1-2
    sprite('ph024_01', 2)	# 3-4
    sprite('ph024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('ph024_03', 3)	# 1-3
    sprite('ph024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ph030_00', 6)	# 1-6
    label(0)
    sprite('ph030_01', 6)	# 7-12
    sprite('ph030_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 6)	# 19-24
    sprite('ph030_04', 6)	# 25-30
    sprite('ph030_05', 6)	# 31-36
    sprite('ph030_06', 6)	# 37-42
    sprite('ph030_07', 6)	# 43-48
    sprite('ph030_08', 6)	# 49-54
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 6)	# 55-60
    sprite('ph030_10', 6)	# 61-66
    sprite('ph030_11', 6)	# 67-72
    sprite('ph030_12', 6)	# 73-78
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('ph031_00', 6)	# 1-6
    label(0)
    sprite('ph031_01', 6)	# 7-12
    sprite('ph031_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph031_03', 6)	# 19-24
    sprite('ph031_04', 6)	# 25-30
    sprite('ph031_05', 6)	# 31-36
    sprite('ph031_06', 6)	# 37-42
    sprite('ph031_07', 6)	# 43-48
    sprite('ph031_08', 6)	# 49-54
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph031_09', 6)	# 55-60
    sprite('ph031_10', 6)	# 61-66
    sprite('ph031_11', 6)	# 67-72
    sprite('ph031_12', 6)	# 73-78
    loopRest()
    gotoLabel(0)

@Subroutine
def DashEndFunc():
    Unknown3001(0)
    Unknown3004(42)
    Unknown2017(1)
    Unknown2015(-1)
    Unknown1084(1)

@Subroutine
def __2ndDashInputFB():
    Unknown14070('2ndDash66')
    Unknown14070('2ndDash44')
    Unknown14070('2ndDash66ButtonInput')
    Unknown14070('2ndDash44ButtonInput')

@Subroutine
def __2ndDashInputUD():
    Unknown14070('2ndDash22')
    Unknown14070('2ndDash88')
    Unknown14070('2ndDash22ButtonInput')
    Unknown14070('2ndDash88ButtonInput')

@Subroutine
def __2ndDashBegin():
    Unknown14072('2ndDash66')
    Unknown14072('2ndDash44')
    Unknown14072('2ndDash22')
    Unknown14072('2ndDash88')
    Unknown14072('2ndDash66ButtonInput')
    Unknown14072('2ndDash44ButtonInput')
    Unknown14072('2ndDash22ButtonInput')
    Unknown14072('2ndDash88ButtonInput')

@Subroutine
def __2ndDashClear():
    setInvincible(0)
    Unknown14074('2ndDash66')
    Unknown14074('2ndDash44')
    Unknown14074('2ndDash22')
    Unknown14074('2ndDash88')
    Unknown14074('2ndDash66ButtonInput')
    Unknown14074('2ndDash44ButtonInput')
    Unknown14074('2ndDash22ButtonInput')
    Unknown14074('2ndDash88ButtonInput')

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ph032_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    callSubroutine('2ndDashInputUD')
    sprite('ph032_01', 3)	# 4-6
    sprite('ph032_02', 3)	# 7-9
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph032_03', 3)	# 10-12
    sprite('ph032_04', 3)	# 13-15
    callSubroutine('2ndDashInputFB')
    sprite('null', 10)	# 16-25
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsXImpulse(60000)
    sprite('ph032_04', 3)	# 26-28
    callSubroutine('DashEndFunc')
    GFX_0('ph032FireEff2', -1)
    sprite('ph032_02', 3)	# 29-31
    sprite('ph032_03', 3)	# 32-34
    callSubroutine('2ndDashBegin')
    sprite('ph032_04', 3)	# 35-37
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('2ndDashClear')
    sprite('ph032_05', 3)	# 38-40
    sprite('ph032_06', 2)	# 41-42

@State
def CmnActFDashStop():
    pass

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown23076()
        Unknown28(8, '_NEUTRAL')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ph032_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    callSubroutine('2ndDashInputUD')
    sprite('ph032_01', 3)	# 4-6
    sprite('ph032_02', 3)	# 7-9
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph032_03', 3)	# 10-12
    sprite('ph032_04', 3)	# 13-15
    callSubroutine('2ndDashInputFB')
    sprite('null', 10)	# 16-25
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsXImpulse(-50000)
    sprite('ph032_04', 3)	# 26-28
    callSubroutine('DashEndFunc')
    GFX_0('ph032FireEff2', -1)
    sprite('ph032_02', 3)	# 29-31
    sprite('ph032_03', 3)	# 32-34
    callSubroutine('2ndDashBegin')
    sprite('ph032_04', 3)	# 35-37
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('2ndDashClear')
    sprite('ph032_05', 3)	# 38-40
    sprite('ph032_06', 2)	# 41-42

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    pass

@State
def SpDashF_Air():

    def upon_IMMEDIATE():
        Unknown28(8, '_NEUTRAL')
        Unknown22003(-1)
        Unknown22001(-1)
        ModifyVar_(8, 2, 4, 0, 1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ph035_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown1084(1)
    callSubroutine('2ndDashInputUD')
    sprite('ph035_01', 3)	# 4-6
    sprite('ph035_02', 3)	# 7-9
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 10-12
    sprite('ph035_04', 3)	# 13-15
    sprite('null', 5)	# 16-20
    callSubroutine('2ndDashInputFB')
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsXImpulse(80000)
    sprite('ph035_03', 3)	# 21-23
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    sprite('ph035_04', 3)	# 24-26
    callSubroutine('2ndDashBegin')
    sprite('ph035_05', 3)	# 27-29
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('2ndDashClear')
    Unknown1043()
    sprite('ph035_06', 2)	# 30-31

@State
def CmnActAirBDash():
    pass

@State
def SpDashB_Air():

    def upon_IMMEDIATE():
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22003(-1)
        Unknown22001(-1)
        ModifyVar_(8, 2, 4, 0, 1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ph035_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown1084(1)
    callSubroutine('2ndDashInputUD')
    sprite('ph035_01', 3)	# 4-6
    sprite('ph035_02', 3)	# 7-9
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 10-12
    sprite('ph035_04', 3)	# 13-15
    sprite('null', 5)	# 16-20
    callSubroutine('2ndDashInputFB')
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsXImpulse(-80000)
    sprite('ph035_03', 3)	# 21-23
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    sprite('ph035_04', 3)	# 24-26
    callSubroutine('2ndDashBegin')
    sprite('ph035_05', 3)	# 27-29
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('2ndDashClear')
    Unknown1043()
    sprite('ph035_06', 2)	# 30-31

@State
def Swoop():

    def upon_IMMEDIATE():
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22003(-1)
        Unknown22001(-1)
        ModifyVar_(8, 2, 4, 0, 1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ph035_00', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    Unknown1084(1)
    callSubroutine('2ndDashInputFB')
    sprite('ph035_01', 3)	# 4-6
    sprite('ph035_02', 3)	# 7-9
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 10-12
    sprite('ph035_04', 3)	# 13-15
    sprite('null', 4)	# 16-19
    callSubroutine('2ndDashInputUD')
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsYImpulse(-80000)
    sprite('null', 1)	# 20-20
    Unknown1084(1)
    Unknown1007(-80000)
    if SLOT_37:
        _gotolabel(1)
    sprite('ph035_03', 3)	# 21-23
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    sprite('ph035_04', 3)	# 24-26
    callSubroutine('2ndDashBegin')
    sprite('ph035_05', 3)	# 27-29
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('2ndDashClear')
    Unknown1043()
    sprite('ph035_06', 2)	# 30-31
    ExitState()
    label(1)
    sprite('ph032_02', 3)	# 32-34
    callSubroutine('DashEndFunc')
    GFX_0('ph032FireEff2', -1)
    sprite('ph032_03', 3)	# 35-37
    callSubroutine('2ndDashBegin')
    sprite('ph032_04', 3)	# 38-40
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('2ndDashClear')
    sprite('ph032_05', 3)	# 41-43
    sprite('ph032_06', 3)	# 44-46
    ExitState()

@State
def __2ndDash66():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22003(-1)
        Unknown22001(-1)
        Unknown1084(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        setInvincible(1)
    if SLOT_36:
        _gotolabel(100)
    sprite('ph032_02', 3)	# 1-3
    Unknown26('ph032FireEff2')
    GFX_0('ph032FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph032_03', 3)	# 4-6
    sprite('ph032_04', 3)	# 7-9
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph032_02', 3)	# 10-12
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph032_03', 3)	# 13-15
    sprite('null', 10)	# 16-25
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    if Unknown23145('CmnActFDash'):
        physicsXImpulse(60000)
        Unknown1019(75)
    else:
        physicsXImpulse(50000)
    sprite('ph032_04', 3)	# 26-28
    callSubroutine('DashEndFunc')
    GFX_0('ph032FireEff2', -1)
    setInvincible(0)
    sprite('ph032_02', 3)	# 29-31
    sprite('ph032_04', 3)	# 32-34
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph032_05', 3)	# 35-37
    sprite('ph032_06', 3)	# 38-40
    ExitState()
    label(100)
    sprite('ph035_02', 3)	# 41-43
    Unknown26('ph035FireEff2')
    GFX_0('ph035FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph035_03', 3)	# 44-46
    sprite('ph035_04', 3)	# 47-49
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph035_02', 3)	# 50-52
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 53-55
    sprite('null', 10)	# 56-65
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsXImpulse(40000)
    sprite('ph035_02', 3)	# 66-68
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)	# 69-71
    sprite('ph035_04', 3)	# 72-74
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    Unknown1043()
    sprite('ph035_05', 3)	# 75-77
    sprite('ph035_06', 3)	# 78-80

@State
def __2ndDash44():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22003(-1)
        Unknown22001(-1)
        Unknown1084(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        setInvincible(1)
    if SLOT_36:
        _gotolabel(100)
    sprite('ph032_02', 3)	# 1-3
    Unknown26('ph032FireEff2')
    GFX_0('ph032FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph032_03', 3)	# 4-6
    sprite('ph032_04', 3)	# 7-9
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph032_02', 3)	# 10-12
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph032_03', 3)	# 13-15
    sprite('null', 10)	# 16-25
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    if Unknown23145('CmnActBDash'):
        physicsXImpulse(-50000)
        Unknown1019(75)
    else:
        physicsXImpulse(-60000)
    sprite('ph032_04', 3)	# 26-28
    callSubroutine('DashEndFunc')
    GFX_0('ph032FireEff2', -1)
    setInvincible(0)
    sprite('ph032_02', 3)	# 29-31
    sprite('ph032_04', 3)	# 32-34
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph032_05', 3)	# 35-37
    sprite('ph032_06', 3)	# 38-40
    ExitState()
    label(100)
    sprite('ph035_02', 3)	# 41-43
    Unknown26('ph035FireEff2')
    GFX_0('ph035FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph035_03', 3)	# 44-46
    sprite('ph035_04', 3)	# 47-49
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph035_02', 3)	# 50-52
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 53-55
    sprite('null', 10)	# 56-65
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsXImpulse(-40000)
    sprite('ph035_02', 3)	# 66-68
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)	# 69-71
    sprite('ph035_04', 3)	# 72-74
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    Unknown1043()
    sprite('ph035_05', 3)	# 75-77
    sprite('ph035_06', 3)	# 78-80

@State
def __2ndDash22():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22003(-1)
        Unknown22001(-1)
        Unknown1084(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
        setInvincible(1)
    if SLOT_36:
        _gotolabel(100)
    sprite('ph032_02', 3)	# 1-3
    Unknown26('ph032FireEff2')
    GFX_0('ph032FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph032_03', 3)	# 4-6
    sprite('ph032_04', 3)	# 7-9
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph032_02', 3)	# 10-12
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph032_03', 3)	# 13-15
    sprite('null', 5)	# 16-20
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    label(1)
    sprite('ph032_02', 3)	# 21-23
    callSubroutine('DashEndFunc')
    GFX_0('ph032FireEff2', -1)
    setInvincible(0)
    sprite('ph032_03', 3)	# 24-26
    sprite('ph032_04', 3)	# 27-29
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    physicsXImpulse(0)
    sprite('ph032_05', 3)	# 30-32
    sprite('ph032_06', 3)	# 33-35
    ExitState()
    label(100)
    sprite('ph035_02', 3)	# 36-38
    Unknown26('ph035FireEff2')
    GFX_0('ph035FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    clearUponHandler(2)
    sprite('ph035_03', 3)	# 39-41
    sprite('ph035_04', 3)	# 42-44
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph035_02', 3)	# 45-47
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 48-50
    sprite('null', 4)	# 51-54
    physicsYImpulse(-80000)
    sprite('null', 1)	# 55-55
    Unknown1084(1)
    Unknown1007(-80000)
    if SLOT_37:
        _gotolabel(1)
    sprite('ph035_02', 3)	# 56-58
    Unknown2006()
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)	# 59-61
    sprite('ph035_04', 3)	# 62-64
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph035_05', 3)	# 65-67
    Unknown1043()
    sprite('ph035_06', 3)	# 68-70

@State
def __2ndDash88():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        Unknown28(8, '_NEUTRAL')
        Unknown23076()
        Unknown22003(-1)
        Unknown22001(-1)
        ModifyVar_(8, 2, 4, 0, 1)
        Unknown1084(1)
        Unknown2061(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown22003(-1)
            Unknown22001(-1)
            ModifyVar_(8, 2, 4, 0, 1)
        setInvincible(1)
    if SLOT_36:
        _gotolabel(100)
    sprite('ph032_02', 3)	# 1-3
    Unknown26('ph032FireEff2')
    GFX_0('ph032FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph032_03', 3)	# 4-6
    sprite('ph032_04', 3)	# 7-9
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph032_02', 3)	# 10-12
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph032_03', 3)	# 13-15
    sprite('null', 5)	# 16-20
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsYImpulse(75200)
    loopRest()
    gotoLabel(101)
    label(100)
    sprite('ph035_02', 3)	# 21-23
    Unknown26('ph035FireEff2')
    GFX_0('ph035FireEff2', -1)
    Unknown3001(255)
    Unknown3004(0)
    Unknown1084(1)
    sprite('ph035_03', 3)	# 24-26
    sprite('ph035_04', 3)	# 27-29
    GFX_0('ph035FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph035_02', 3)	# 30-32
    Unknown3001(255)
    Unknown3004(-42)
    sprite('ph035_03', 3)	# 33-35
    sprite('null', 5)	# 36-40
    Unknown3001(0)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2015(40)
    physicsYImpulse(40000)
    label(101)
    sprite('ph035_02', 3)	# 41-43
    Unknown2006()
    callSubroutine('DashEndFunc')
    GFX_0('ph035FireEff2', -1)
    setInvincible(0)
    sprite('ph035_03', 3)	# 44-46
    sprite('ph035_04', 3)	# 47-49
    SFX_4('ph005')
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph035_05', 3)	# 50-52
    Unknown1043()
    sprite('ph035_06', 3)	# 53-55

@State
def CmnActHitStandLv1():
    sprite('ph050_00', 1)	# 1-1
    sprite('ph050_01', 1)	# 2-2
    sprite('ph050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ph050_01', 1)	# 1-1
    sprite('ph050_02', 1)	# 2-2
    sprite('ph050_01', 2)	# 3-4
    sprite('ph050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ph050_02', 1)	# 1-1
    sprite('ph050_03', 1)	# 2-2
    sprite('ph050_02', 2)	# 3-4
    sprite('ph050_01', 2)	# 5-6
    sprite('ph050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ph050_03', 1)	# 1-1
    sprite('ph050_04', 1)	# 2-2
    sprite('ph050_03', 2)	# 3-4
    sprite('ph050_02', 2)	# 5-6
    sprite('ph050_01', 2)	# 7-8
    sprite('ph050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ph050_04', 1)	# 1-1
    sprite('ph050_04', 1)	# 2-2
    sprite('ph050_04', 2)	# 3-4
    sprite('ph050_03', 2)	# 5-6
    sprite('ph050_02', 2)	# 7-8
    sprite('ph050_01', 2)	# 9-10
    sprite('ph050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ph052_00', 1)	# 1-1
    sprite('ph052_01', 1)	# 2-2
    sprite('ph052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ph052_01', 1)	# 1-1
    sprite('ph052_02', 1)	# 2-2
    sprite('ph052_01', 2)	# 3-4
    sprite('ph052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ph052_02', 1)	# 1-1
    sprite('ph052_03', 1)	# 2-2
    sprite('ph052_02', 2)	# 3-4
    sprite('ph052_01', 2)	# 5-6
    sprite('ph052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ph052_03', 1)	# 1-1
    sprite('ph052_04', 1)	# 2-2
    sprite('ph052_03', 2)	# 3-4
    sprite('ph052_02', 2)	# 5-6
    sprite('ph052_01', 2)	# 7-8
    sprite('ph052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ph052_04', 1)	# 1-1
    sprite('ph052_04', 1)	# 2-2
    sprite('ph052_04', 2)	# 3-4
    sprite('ph052_03', 2)	# 5-6
    sprite('ph052_02', 2)	# 7-8
    sprite('ph052_01', 2)	# 9-10
    sprite('ph052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ph054_00', 1)	# 1-1
    sprite('ph054_01', 1)	# 2-2
    sprite('ph054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ph054_01', 1)	# 1-1
    sprite('ph054_02', 1)	# 2-2
    sprite('ph054_01', 2)	# 3-4
    sprite('ph054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ph054_02', 1)	# 1-1
    sprite('ph054_03', 1)	# 2-2
    sprite('ph054_02', 2)	# 3-4
    sprite('ph054_01', 2)	# 5-6
    sprite('ph054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ph054_03', 1)	# 1-1
    sprite('ph054_04', 1)	# 2-2
    sprite('ph054_03', 2)	# 3-4
    sprite('ph054_02', 2)	# 5-6
    sprite('ph054_01', 2)	# 7-8
    sprite('ph054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ph054_04', 1)	# 1-1
    sprite('ph054_04', 1)	# 2-2
    sprite('ph054_04', 2)	# 3-4
    sprite('ph054_03', 2)	# 5-6
    sprite('ph054_02', 2)	# 7-8
    sprite('ph054_01', 2)	# 9-10
    sprite('ph054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ph060_00', 4)	# 1-4
    label(0)
    sprite('ph060_01', 4)	# 5-8
    sprite('ph060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ph060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ph060_04', 4)	# 1-4
    label(0)
    sprite('ph060_05', 4)	# 5-8
    sprite('ph060_06', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ph060_07', 2)	# 1-2
    sprite('ph060_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('ph060_09', 3)	# 1-3
    sprite('ph060_10', 3)	# 4-6
    sprite('ph060_11', 3)	# 7-9
    sprite('ph060_12', 3)	# 10-12
    sprite('ph060_13', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('ph060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('ph061_00', 3)	# 1-3
    sprite('ph061_01', 3)	# 4-6
    sprite('ph061_02', 3)	# 7-9
    sprite('ph061_03', 3)	# 10-12
    sprite('ph061_04', 3)	# 13-15
    sprite('ph061_05', 3)	# 16-18
    sprite('ph061_06', 2)	# 19-20
    sprite('ph061_07', 2)	# 21-22
    sprite('ph061_08', 2)	# 23-24
    sprite('ph061_09', 2)	# 25-26

@State
def CmnActFDownUpper():
    sprite('ph063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ph063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ph063_02', 3)	# 1-3
    sprite('ph063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ph063_04', 3)	# 1-3
    sprite('ph063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('ph063_06', 2)	# 1-2
    sprite('ph063_07', 2)	# 3-4
    sprite('ph063_08', 3)	# 5-7
    sprite('ph063_09', 3)	# 8-10
    sprite('ph063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('ph063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ph064_00', 2)	# 1-2
    sprite('ph064_01', 2)	# 3-4
    sprite('ph064_02', 2)	# 5-6
    sprite('ph061_02', 2)	# 7-8
    sprite('ph061_03', 2)	# 9-10
    sprite('ph061_04', 2)	# 11-12
    sprite('ph061_05', 2)	# 13-14
    sprite('ph061_06', 2)	# 15-16
    sprite('ph061_07', 2)	# 17-18
    sprite('ph061_08', 2)	# 19-20
    sprite('ph061_09', 2)	# 21-22

@State
def CmnActVDownUpper():
    sprite('ph062_00', 3)	# 1-3
    label(0)
    sprite('ph062_01', 3)	# 4-6
    sprite('ph062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ph062_03', 3)	# 1-3
    sprite('ph062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('ph062_05', 3)	# 1-3
    sprite('ph062_06', 3)	# 4-6
    label(0)
    sprite('ph062_07', 3)	# 7-9
    sprite('ph062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ph062_09', 2)	# 1-2
    sprite('ph062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('ph072_00', 3)	# 1-3
    sprite('ph072_01', 3)	# 4-6
    sprite('ph072_02', 3)	# 7-9
    label(0)
    sprite('ph072_01', 3)	# 10-12
    sprite('ph072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ph074_00', 3)	# 1-3
    sprite('ph074_01', 3)	# 4-6
    sprite('ph074_02', 3)	# 7-9
    sprite('ph074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('ph082_00', 2)	# 1-2
    sprite('ph082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('ph071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ph073_00', 3)	# 1-3
    sprite('ph073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ph073_02', 3)	# 1-3
    label(0)
    sprite('ph073_03', 3)	# 4-6
    sprite('ph073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ph070_00', 3)	# 1-3
    sprite('ph070_01', 3)	# 4-6
    label(0)
    sprite('ph070_02', 4)	# 7-10
    sprite('ph070_03', 4)	# 11-14
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ph070_04', 4)	# 1-4
    sprite('ph070_05', 4)	# 5-8
    sprite('ph070_06', 4)	# 9-12
    sprite('ph070_07', 4)	# 13-16
    sprite('ph070_08', 4)	# 17-20
    sprite('ph070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ph070_10', 2)	# 1-2
    sprite('ph070_11', 2)	# 3-4
    sprite('ph070_12', 2)	# 5-6
    sprite('ph070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ph113_00', 3)	# 1-3
    sprite('ph113_01', 3)	# 4-6
    sprite('ph113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('ph113_00', 3)	# 1-3
    sprite('ph113_01', 3)	# 4-6
    sprite('ph113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('ph113_00', 3)	# 1-3
    sprite('ph113_01', 3)	# 4-6
    sprite('ph113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('ph110_00', 2)	# 1-2
    sprite('ph110_01', 2)	# 3-4
    sprite('ph110_02', 2)	# 5-6
    sprite('ph110_03', 2)	# 7-8
    sprite('ph110_04', 2)	# 9-10
    sprite('ph110_05', 2)	# 11-12
    sprite('ph110_06', 2)	# 13-14
    sprite('ph110_07', 200)	# 15-214
    sprite('ph110_08', 3)	# 215-217
    sprite('ph110_09', 3)	# 218-220

@State
def CmnActUkemiLandB():
    sprite('ph111_00', 2)	# 1-2
    sprite('ph111_01', 2)	# 3-4
    sprite('ph111_02', 2)	# 5-6
    sprite('ph111_03', 2)	# 7-8
    sprite('ph111_04', 2)	# 9-10
    sprite('ph111_05', 2)	# 11-12
    sprite('ph111_06', 2)	# 13-14
    sprite('ph111_07', 200)	# 15-214
    sprite('ph111_08', 3)	# 215-217
    sprite('ph111_09', 3)	# 218-220

@State
def CmnActUkemiLandN():
    sprite('ph112_00', 2)	# 1-2
    sprite('ph112_01', 2)	# 3-4
    sprite('ph112_02', 3)	# 5-7
    sprite('ph112_03', 3)	# 8-10
    sprite('ph112_04', 3)	# 11-13
    sprite('ph112_05', 3)	# 14-16
    sprite('ph112_06', 3)	# 17-19
    sprite('ph112_07', 3)	# 20-22
    sprite('ph112_08', 3)	# 23-25
    sprite('ph112_09', 3)	# 26-28

@State
def CmnActUkemiLandNLanding():
    sprite('ph024_00', 3)	# 1-3
    sprite('ph024_01', 3)	# 4-6
    sprite('ph024_02', 3)	# 7-9
    sprite('ph024_03', 3)	# 10-12
    sprite('ph024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('ph040_00', 3)	# 1-3
    sprite('ph040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ph040_02', 3)	# 1-3
    sprite('ph040_03', 3)	# 4-6
    sprite('ph040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ph040_01', 3)	# 1-3
    sprite('ph040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ph040_05', 3)	# 1-3
    label(0)
    sprite('ph040_02', 3)	# 4-6
    sprite('ph040_03', 3)	# 7-9
    sprite('ph040_04', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ph040_01', 3)	# 1-3
    sprite('ph040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ph041_00', 3)	# 1-3
    sprite('ph041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ph041_02', 3)	# 1-3
    sprite('ph041_03', 3)	# 4-6
    sprite('ph041_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ph041_01', 3)	# 1-3
    sprite('ph041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ph041_05', 3)	# 1-3
    label(0)
    sprite('ph041_02', 3)	# 4-6
    sprite('ph041_03', 3)	# 7-9
    sprite('ph041_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ph041_01', 3)	# 1-3
    sprite('ph041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ph043_00', 3)	# 1-3
    sprite('ph043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ph043_02', 3)	# 1-3
    sprite('ph043_03', 3)	# 4-6
    sprite('ph043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ph043_01', 3)	# 1-3
    sprite('ph043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ph043_05', 3)	# 1-3
    label(0)
    sprite('ph043_02', 3)	# 4-6
    sprite('ph043_03', 3)	# 7-9
    sprite('ph043_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ph043_01', 3)	# 1-3
    sprite('ph043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ph045_00', 3)	# 1-3
    sprite('ph045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ph045_02', 3)	# 1-3
    sprite('ph045_03', 3)	# 4-6
    sprite('ph045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ph045_01', 3)	# 1-3
    sprite('ph045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ph045_05', 3)	# 1-3
    label(0)
    sprite('ph045_02', 3)	# 4-6
    sprite('ph045_03', 3)	# 7-9
    sprite('ph045_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ph045_01', 3)	# 1-3
    sprite('ph045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ph090_00', 2)	# 1-2
    sprite('ph090_01', 2)	# 3-4
    sprite('ph090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ph090_03', 6)	# 6-11
    sprite('ph090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('ph091_00', 2)	# 1-2
    sprite('ph091_01', 2)	# 3-4
    sprite('ph091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ph091_03', 6)	# 6-11
    sprite('ph091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('ph092_00', 2)	# 1-2
    sprite('ph092_01', 2)	# 3-4
    sprite('ph092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('ph092_03', 6)	# 6-11
    sprite('ph092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('ph025_00', 4)	# 1-4
    sprite('ph025_01', 4)	# 5-8
    sprite('ph025_00ex01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('ph040_02', 1)	# 1-1
    sprite('ph040_01', 3)	# 2-4
    sprite('ph040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('ph312_00', 3)	# 1-3
    sprite('ph312_01', 5)	# 4-8
    sprite('ph312_02', 5)	# 9-13
    sprite('ph312_03', 3)	# 14-16	 **attackbox here**
    sprite('ph312_04', 3)	# 17-19
    sprite('ph312_05', 3)	# 20-22
    sprite('ph312_06', 2)	# 23-24
    sprite('ph312_07', 2)	# 25-26
    sprite('ph312_08', 2)	# 27-28
    sprite('ph312_09', 2)	# 29-30

@State
def CmnActAirLockWait():
    sprite('ph045_02', 1)	# 1-1
    sprite('ph045_01', 3)	# 2-4
    sprite('ph045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ph322_00', 4)	# 1-4
    sprite('ph322_01', 4)	# 5-8
    sprite('ph322_02', 4)	# 9-12
    sprite('ph322_03', 3)	# 13-15	 **attackbox here**
    sprite('ph322_04', 3)	# 16-18
    sprite('ph322_05', 3)	# 19-21
    sprite('ph322_06', 2)	# 22-23
    sprite('ph322_07', 2)	# 24-25
    sprite('ph322_08', 2)	# 26-27
    sprite('ph322_09', 3)	# 28-30

@State
def CmnActLandSpin():
    sprite('ph071_00', 4)	# 1-4
    sprite('ph071_01', 4)	# 5-8
    label(0)
    sprite('ph071_02', 2)	# 9-10
    sprite('ph071_03', 2)	# 11-12
    sprite('ph071_04', 2)	# 13-14
    sprite('ph071_05', 2)	# 15-16
    sprite('ph071_06', 2)	# 17-18
    sprite('ph071_07', 2)	# 19-20
    sprite('ph071_08', 2)	# 21-22
    sprite('ph071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ph071_10', 6)	# 1-6
    sprite('ph071_11', 5)	# 7-11
    sprite('ph071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('ph071_02', 2)	# 1-2
    sprite('ph071_03', 2)	# 3-4
    sprite('ph071_04', 2)	# 5-6
    sprite('ph071_05', 2)	# 7-8
    sprite('ph071_06', 2)	# 9-10
    sprite('ph071_07', 2)	# 11-12
    sprite('ph071_08', 2)	# 13-14
    sprite('ph071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('ph077_00', 2)	# 1-2
    sprite('ph077_01', 2)	# 3-4
    sprite('ph077_00ex01', 2)	# 5-6
    sprite('ph077_01ex01', 2)	# 7-8
    sprite('ph077_00ex02', 2)	# 9-10
    sprite('ph077_01ex02', 2)	# 11-12
    sprite('ph077_00ex03', 2)	# 13-14
    sprite('ph077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ph077_02', 4)	# 1-4
    label(0)
    sprite('ph077_03', 3)	# 5-7
    sprite('ph077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ph077_05', 5)	# 1-5
    sprite('ph077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('ph060_07', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ph060_12', 4)	# 1-4
    sprite('ph060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('ph331_00', 2)	# 1-2
    sprite('ph331_01', 2)	# 3-4
    label(0)
    sprite('ph331_02', 3)	# 5-7
    sprite('ph331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ph331_04', 2)	# 1-2
    sprite('ph331_05', 2)	# 3-4
    label(0)
    sprite('ph331_06', 3)	# 5-7
    sprite('ph331_07', 3)	# 8-10
    sprite('ph331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ph331_09', 3)	# 1-3
    sprite('ph331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('ph331_11', 2)	# 1-2
    sprite('ph331_12', 2)	# 3-4
    label(0)
    sprite('ph331_02', 3)	# 5-7
    sprite('ph331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ph331_04', 2)	# 1-2
    sprite('ph331_05', 2)	# 3-4
    label(0)
    sprite('ph331_06', 3)	# 5-7
    sprite('ph331_07', 3)	# 8-10
    sprite('ph331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ph331_13', 3)	# 1-3
    sprite('ph331_14', 3)	# 4-6
    label(0)
    sprite('ph020_07', 4)	# 7-10
    sprite('ph020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ph333_00', 3)	# 1-3
    sprite('ph333_01', 3)	# 4-6
    sprite('ph333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_0('ph333_arm', 100)
    Unknown38(4, 1)
    sprite('ph333_03', 32767)	# 10-32776
    GFX_0('EMB_PH_OD', 0)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ph333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    Unknown23029(4, 3331, 0)
    sprite('ph333_05', 3)	# 4-6
    sprite('ph333_06', 3)	# 7-9
    sprite('ph333_07', 3)	# 10-12
    label(0)
    sprite('ph333_05', 3)	# 13-15
    sprite('ph333_06', 3)	# 16-18
    sprite('ph333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ph333_08', 6)	# 1-6
    Unknown23029(4, 3332, 0)
    sprite('ph333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('ph333_10', 3)	# 1-3
    sprite('ph333_11', 3)	# 4-6	 **attackbox here**
    sprite('ph333_12', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_0('ph333_arm', 100)
    Unknown38(4, 1)
    sprite('ph333_13', 32767)	# 10-32776
    GFX_0('EMB_PH_OD', 0)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ph333_14', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    Unknown23029(4, 3331, 0)
    sprite('ph333_05', 3)	# 4-6
    sprite('ph333_06', 3)	# 7-9
    sprite('ph333_07', 3)	# 10-12
    label(0)
    sprite('ph333_05', 3)	# 13-15
    sprite('ph333_06', 3)	# 16-18
    sprite('ph333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ph333_15', 6)	# 1-6
    Unknown23029(4, 3332, 0)
    sprite('ph333_16', 6)	# 7-12
    sprite('ph020_04', 3)	# 13-15
    sprite('ph020_05', 3)	# 16-18
    sprite('ph020_06', 3)	# 19-21
    label(0)
    sprite('ph020_07', 3)	# 22-24
    sprite('ph020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ph333_00', 3)	# 1-3
    sprite('ph333_01', 3)	# 4-6
    sprite('ph333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_0('ph333_arm', 100)
    Unknown38(4, 1)
    sprite('ph333_03', 32767)	# 10-32776
    GFX_0('EMB_PH_OD', 0)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ph333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    Unknown23029(4, 3331, 0)
    sprite('ph333_05', 3)	# 4-6
    sprite('ph333_06', 3)	# 7-9
    sprite('ph333_07', 3)	# 10-12
    label(0)
    sprite('ph333_05', 3)	# 13-15
    sprite('ph333_06', 3)	# 16-18
    sprite('ph333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ph333_08', 6)	# 1-6
    Unknown23029(4, 3332, 0)
    sprite('ph333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('ph333_10', 3)	# 1-3
    sprite('ph333_11', 3)	# 4-6	 **attackbox here**
    sprite('ph333_12', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    GFX_0('ph333_arm', 100)
    Unknown38(4, 1)
    sprite('ph333_13', 32767)	# 10-32776
    GFX_0('EMB_PH_OD', 0)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ph333_14', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    Unknown23029(4, 3331, 0)
    sprite('ph333_05', 3)	# 4-6
    sprite('ph333_06', 3)	# 7-9
    sprite('ph333_07', 3)	# 10-12
    label(0)
    sprite('ph333_05', 3)	# 13-15
    sprite('ph333_06', 3)	# 16-18
    sprite('ph333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ph333_15', 6)	# 1-6
    Unknown23029(4, 3332, 0)
    sprite('ph333_16', 6)	# 7-12
    sprite('ph020_04', 3)	# 13-15
    sprite('ph020_05', 3)	# 16-18
    sprite('ph020_06', 3)	# 19-21
    label(0)
    sprite('ph020_07', 3)	# 22-24
    sprite('ph020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('ph333_00', 3)	# 1-3
    sprite('ph333_01', 3)	# 4-6
    sprite('ph333_02', 3)	# 7-9
    GFX_0('ph333_arm', 100)
    Unknown38(4, 1)
    sprite('ph333_03', 32767)	# 10-32776
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ph333_04', 3)	# 1-3
    Unknown23029(4, 3331, 0)
    sprite('ph333_05', 3)	# 4-6
    sprite('ph333_06', 3)	# 7-9
    sprite('ph333_07', 3)	# 10-12
    label(0)
    sprite('ph333_05', 3)	# 13-15
    sprite('ph333_06', 3)	# 16-18
    sprite('ph333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ph333_08', 6)	# 1-6
    Unknown23029(4, 3332, 0)
    sprite('ph333_09', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():
    sprite('ph333_10', 3)	# 1-3
    sprite('ph333_11', 3)	# 4-6	 **attackbox here**
    sprite('ph333_12', 3)	# 7-9
    GFX_0('ph333_arm', 100)
    Unknown38(4, 1)
    sprite('ph333_13', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ph333_14', 3)	# 1-3
    Unknown23029(4, 3331, 0)
    sprite('ph333_05', 3)	# 4-6
    sprite('ph333_06', 3)	# 7-9
    sprite('ph333_07', 3)	# 10-12
    label(0)
    sprite('ph333_05', 3)	# 13-15
    sprite('ph333_06', 3)	# 16-18
    sprite('ph333_07', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ph333_15', 6)	# 1-6
    Unknown23029(4, 3332, 0)
    sprite('ph333_16', 6)	# 7-12
    sprite('ph020_04', 3)	# 13-15
    sprite('ph020_05', 3)	# 16-18
    sprite('ph020_06', 3)	# 19-21
    label(0)
    sprite('ph020_07', 3)	# 22-24
    sprite('ph020_08', 3)	# 25-27
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
    pass

@State
def CmnActChangePartnerAppealAir():
    pass

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9266(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 7)	# 1-7
    label(0)
    sprite('null', 14)	# 8-21
    sprite('ph035_03', 2)	# 22-23
    Unknown1086(22)
    teleportRelativeX(-200000)
    teleportRelativeY(30000)
    GFX_0('ph035FireEff2', -1)
    SFX_0('000_airdash_0')
    sprite('ph035_04', 2)	# 24-25
    sprite('ph035_05', 2)	# 26-27
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph035_06', 2)	# 28-29
    sprite('ph252_00', 2)	# 30-31
    sprite('ph252_01', 2)	# 32-33
    sprite('ph252_02', 2)	# 34-35
    GFX_0('CrossBurst_Bomb', -1)
    sprite('ph252_03ex01', 3)	# 36-38	 **attackbox here**
    physicsXImpulse(-2500)
    physicsYImpulse(5000)
    setGravity(1800)
    sprite('ph252_04', 5)	# 39-43
    sprite('ph252_05', 5)	# 44-48
    sprite('ph252_06', 5)	# 49-53
    sprite('ph252_07', 5)	# 54-58
    sprite('ph252_08', 5)	# 59-63
    sprite('ph020_05', 3)	# 64-66
    sprite('ph020_06', 3)	# 67-69
    label(0)
    sprite('ph020_07', 4)	# 70-73
    sprite('ph020_08', 4)	# 74-77
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 78-80
    sprite('ph024_01', 3)	# 81-83
    sprite('ph024_02', 3)	# 84-86
    sprite('ph024_03', 3)	# 87-89
    sprite('ph024_04', 3)	# 90-92
    ExitState()

@State
def CmnActChangePartnerQuickIn():
    sprite('ph032_02', 5)	# 1-5
    Unknown3004(0)
    Unknown3038(1)
    sprite('ph032_03', 5)	# 6-10
    sprite('ph032_04', 5)	# 11-15
    GFX_0('phChangeFireEff2', -1)
    Unknown3001(0)
    Unknown3004(42)
    Unknown3038(0)
    sprite('ph032_05', 7)	# 16-22
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph032_06', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ph032_00', 3)	# 1-3
    Unknown1019(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('ph032_01', 3)	# 4-6
    sprite('ph032_02', 3)	# 7-9
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    Unknown3001(0)
    sprite('ph032_03', 3)	# 10-12
    sprite('ph032_04', 3)	# 13-15
    sprite('ph032_02', 3)	# 16-18
    sprite('ph032_03', 3)	# 19-21
    sprite('ph032_04', 3)	# 22-24
    sprite('ph032_05', 3)	# 25-27
    sprite('ph032_06', 3)	# 28-30
    sprite('ph032_06', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('ph032_00', 1)	# 1-1
    sprite('ph032_01', 1)	# 2-2
    sprite('ph032_02', 1)	# 3-3
    sprite('ph032_02', 1)	# 4-4
    GFX_0('ph032FireEff', -1)
    SFX_0('000_airdash_0')
    sprite('ph032_02', 1)	# 5-5
    Unknown3001(0)
    sprite('ph032_03', 3)	# 6-8
    sprite('ph032_04', 3)	# 9-11
    label(0)
    sprite('ph032_02', 3)	# 12-14
    sprite('ph032_03', 3)	# 15-17
    sprite('ph032_04', 3)	# 18-20
    gotoLabel(0)
    label(1)
    sprite('ph032_05', 3)	# 21-23
    sprite('ph032_06', 2)	# 24-25

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ph300_00', 4)	# 1-4
    sprite('ph300_01', 4)	# 5-8
    sprite('ph300_02', 5)	# 9-13
    sprite('ph300_03', 5)	# 14-18
    sprite('ph300_04', 5)	# 19-23
    sprite('ph300_05', 5)	# 24-28
    sprite('ph300_06', 5)	# 29-33
    sprite('ph300_07', 5)	# 34-38
    sprite('ph300_02', 5)	# 39-43
    sprite('ph300_03', 5)	# 44-48
    sprite('ph300_04', 5)	# 49-53
    sprite('ph300_05', 5)	# 54-58
    sprite('ph300_06', 5)	# 59-63
    sprite('ph300_07', 5)	# 64-68
    sprite('ph300_01', 4)	# 69-72
    sprite('ph300_00', 4)	# 73-76

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2042(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('ph032_02', 1)	# 1-1
    Unknown3001(0)
    Unknown3004(0)
    sprite('ph032_02', 2)	# 2-3
    Unknown1086(24)
    teleportRelativeX(-61520)
    teleportRelativeY(0)
    Unknown2006()
    sprite('ph032_03', 3)	# 4-6
    sprite('ph032_04', 5)	# 7-11
    GFX_0('phChangeFireEff2', -1)
    Unknown3001(0)
    Unknown3004(42)
    sprite('ph032_05', 3)	# 12-14
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph032_06', 3)	# 15-17
    sprite('keep', 100)	# 18-117

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ph440_13', 6)	# 1-6
    sprite('ph440_14', 6)	# 7-12
    tag_voice(1, 'bph307_0', 'bph156_1', '', '')
    sprite('ph440_15', 9)	# 13-21
    sprite('ph440_15', 3)	# 22-24
    GFX_0('BurstDDMaster', -1)
    Unknown23029(1, 4401, 0)
    sprite('ph440_16', 12)	# 25-36
    sprite('ph440_17', 2)	# 37-38
    sprite('ph440_18', 2)	# 39-40
    sprite('ph440_19', 3)	# 41-43
    ScreenShake(25000, 10000)
    sprite('ph440_20', 3)	# 44-46
    sprite('ph440_21', 3)	# 47-49
    sprite('ph440_19', 3)	# 50-52
    sprite('ph440_20', 3)	# 53-55
    sprite('ph440_21', 3)	# 56-58
    sprite('ph440_19', 3)	# 59-61
    sprite('ph440_20', 3)	# 62-64
    sprite('ph440_21', 3)	# 65-67
    sprite('ph440_22', 5)	# 68-72
    sprite('ph440_23', 5)	# 73-77
    sprite('ph440_24', 5)	# 78-82

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
        Unknown2004(1, 0)
    sprite('ph401_00', 3)	# 1-3
    sprite('ph401_01', 3)	# 4-6
    tag_voice(1, 'bph201_0', 'bph201_1', 'bph201_2', '')
    Unknown18009(1)
    sprite('ph401_02', 6)	# 7-12
    GFX_0('Eff_401', -1)
    Unknown23029(1, 4101, 0)
    SFX_0('016_explode_1')
    SFX_3('phse_02')
    sprite('ph401_03', 3)	# 13-15
    physicsXImpulse(30000)
    SFX_0('004_swing_grap_1_2')
    sprite('ph401_04', 3)	# 16-18
    Unknown1019(50)
    sprite('ph401_05', 6)	# 19-24
    Recovery()
    Unknown1019(25)
    sprite('ph401_06', 6)	# 25-30
    Unknown1019(0)
    sprite('ph401_07', 6)	# 31-36
    physicsXImpulse(-2000)
    sprite('ph401_08', 6)	# 37-42
    Unknown1019(50)
    sprite('ph401_09', 6)	# 43-48
    Unknown18009(0)
    Unknown1019(50)
    sprite('ph401_10', 6)	# 49-54
    Unknown1019(50)
    sprite('ph401_11', 6)	# 55-60
    Unknown1019(50)

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1500)
        AttackP1(70)
        AirUntechableTime(30)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(10000)
        PushbackX(8000)
        Unknown11042(1)
        Unknown11032('400d0300c0f2fcff400d0300c0f2fcff')
        Unknown23027()
        Unknown9310(1)

        def upon_11():
            clearUponHandler(11)
            physicsXImpulse(80000)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown1019(25)
    sprite('ph400_00', 3)	# 1-3
    tag_voice(1, 'bph200_0', 'bph200_1', 'bph200_2', '')
    physicsXImpulse(2050)
    sprite('ph400_01', 3)	# 4-6
    Unknown1019(150)
    sprite('ph400_02', 2)	# 7-8	 **attackbox here**
    Unknown1019(150)
    SFX_0('000_airdash_0')
    sprite('ph400_03', 2)	# 9-10	 **attackbox here**
    Unknown1019(400)
    GFX_0('pheff_400', -1)
    Unknown38(5, 1)
    SFX_0('015_blaze_0')
    sprite('ph400_04', 2)	# 11-12	 **attackbox here**
    Unknown1019(800)
    sprite('ph400_02', 3)	# 13-15	 **attackbox here**
    Unknown1019(50)
    Unknown3038(1)
    RefreshMultihit()
    Unknown23029(5, 4001, 0)
    sprite('ph400_03', 3)	# 16-18	 **attackbox here**
    Unknown1019(25)
    sprite('ph400_04', 3)	# 19-21	 **attackbox here**
    Unknown1019(25)
    label(1)
    sprite('ph400_05', 6)	# 22-27	 **attackbox here**
    clearUponHandler(11)
    Unknown2006()
    Unknown1019(25)
    Unknown9310(-1)
    sprite('ph400_05', 1)	# 28-28	 **attackbox here**
    Unknown3038(0)
    physicsXImpulse(-15000)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AirPushbackX(10000)
    AirPushbackY(25000)
    AirUntechableTime(60)
    Unknown9215()
    Unknown9017(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown11032('90d00300702ffcffe0930400206cfbff')
    SFX_0('016_explode_0')
    SFX_0('016_explode_1')
    sprite('ph400_05', 5)	# 29-33	 **attackbox here**
    StartMultihit()
    sprite('ph400_06', 5)	# 34-38
    Unknown1019(25)
    Recovery()
    sprite('ph400_07', 5)	# 39-43
    Unknown1019(25)
    sprite('ph400_08', 5)	# 44-48
    Unknown1019(25)
    sprite('ph400_09', 5)	# 49-53
    Unknown1019(25)
    sprite('ph400_10', 5)	# 54-58
    Unknown1019(0)

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
    Unknown2036(128, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-200000)
    Unknown1019(4)
    label(0)
    sprite('ph020_07', 3)	# 3-5
    sprite('ph020_08', 3)	# 6-8
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
        Unknown30063(1)
    sprite('ph431_00', 6)	# 1-6
    sprite('ph431_01', 6)	# 7-12
    GFX_0('Eff_431_obi', -1)
    sprite('ph431_02', 6)	# 13-18
    sprite('ph431_03', 6)	# 19-24
    sprite('ph431_04', 8)	# 25-32
    teleportRelativeX(-90000)
    sprite('ph431_05', 6)	# 33-38
    sprite('ph431_06', 6)	# 39-44
    sprite('ph431_07', 6)	# 45-50
    physicsXImpulse(5000)
    sprite('ph431_08', 8)	# 51-58
    Unknown1019(50)
    GFX_0('Eff_431_mc', -1)
    sprite('ph431_09', 8)	# 59-66
    Unknown1019(50)
    sprite('ph431_10', 8)	# 67-74
    GFX_0('Eff_431_mc_sub1', -1)
    GFX_0('Eff_431_BomBall', -1)
    Unknown1019(0)
    SFX_3('phse_02')
    sprite('ph431_11', 8)	# 75-82
    Unknown21012('4566665f3433315f426f6d42616c6c000000000000000000000000000000000020000000')
    sprite('ph431_12', 8)	# 83-90
    sprite('ph431_13', 4)	# 91-94
    Unknown21012('4566665f3433315f6d630000000000000000000000000000000000000000000020000000')
    Unknown21012('4566665f3433315f6d635f73756231000000000000000000000000000000000020000000')
    Unknown21012('4566665f3433315f426f6d42616c6c000000000000000000000000000000000021000000')
    sprite('ph431_14', 4)	# 95-98
    Unknown21012('4566665f3433315f426f6d42616c6c000000000000000000000000000000000022000000')
    SFX_1('bph254')
    GFX_0('Eff_431_bomb', -1)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('ph431_15', 3)	# 99-101	 **attackbox here**
    Unknown23027()
    sprite('ph431_16', 2)	# 102-103
    sprite('ph431_17', 2)	# 104-105
    GFX_0('UltimateChargeAtk', -1)
    sprite('ph431_18', 2)	# 106-107
    setInvincible(0)
    sprite('ph431_16', 3)	# 108-110
    sprite('ph431_17', 3)	# 111-113
    sprite('ph431_18', 3)	# 114-116
    sprite('ph431_16', 4)	# 117-120
    GFX_0('bphef_DDD_Particle', -1)
    sprite('ph431_17', 4)	# 121-124
    sprite('ph431_18', 4)	# 125-128
    sprite('ph431_19', 5)	# 129-133
    sprite('ph431_20', 5)	# 134-138
    sprite('ph431_21', 5)	# 139-143
    sprite('ph431_22', 5)	# 144-148
    sprite('ph431_23', 15)	# 149-163
    sprite('ph431_24', 6)	# 164-169

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 4311):
                Unknown2037(1)
    sprite('ph431_00', 6)	# 1-6
    sprite('ph431_01', 6)	# 7-12
    GFX_0('Eff_431_obi', -1)
    sprite('ph431_02', 6)	# 13-18
    sprite('ph431_03', 6)	# 19-24
    sprite('ph431_04', 8)	# 25-32
    teleportRelativeX(-90000)
    sprite('ph431_05', 6)	# 33-38
    sprite('ph431_06', 6)	# 39-44
    sprite('ph431_07', 6)	# 45-50
    physicsXImpulse(5000)
    sprite('ph431_08', 8)	# 51-58
    Unknown1019(50)
    GFX_0('Eff_431_mc', -1)
    sprite('ph431_09', 8)	# 59-66
    Unknown1019(50)
    sprite('ph431_10', 8)	# 67-74
    GFX_0('Eff_431_mc_sub1', -1)
    GFX_0('Eff_431_BomBall', -1)
    Unknown1019(0)
    SFX_3('phse_02')
    sprite('ph431_11', 8)	# 75-82
    Unknown21012('4566665f3433315f426f6d42616c6c000000000000000000000000000000000020000000')
    sprite('ph431_12', 8)	# 83-90
    sprite('ph431_13', 4)	# 91-94
    Unknown21012('4566665f3433315f6d630000000000000000000000000000000000000000000020000000')
    Unknown21012('4566665f3433315f6d635f73756231000000000000000000000000000000000020000000')
    Unknown21012('4566665f3433315f426f6d42616c6c000000000000000000000000000000000021000000')
    sprite('ph431_14', 4)	# 95-98
    Unknown21012('4566665f3433315f426f6d42616c6c000000000000000000000000000000000022000000')
    SFX_1('bph254')
    GFX_0('Eff_431_bomb', -1)
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('ph431_15', 3)	# 99-101	 **attackbox here**
    Unknown23027()
    sprite('ph431_16', 2)	# 102-103
    sprite('ph431_17', 2)	# 104-105
    GFX_0('UltimateChargeAtk', -1)
    sprite('ph431_18', 2)	# 106-107
    setInvincible(0)
    sprite('ph431_16', 3)	# 108-110
    if SLOT_2:
        GFX_0('UltimateChargeSPAddAtk', 100)
    sprite('ph431_17', 3)	# 111-113
    sprite('ph431_18', 3)	# 114-116
    sprite('ph431_16', 3)	# 117-119
    GFX_0('bphef_DDD_Particle', -1)
    sprite('ph431_17', 3)	# 120-122
    sprite('ph431_18', 2)	# 123-124
    sprite('keep', 1)	# 125-125
    if (not SLOT_2):
        sendToLabel(100)
    sprite('ph431_16', 4)	# 126-129
    sprite('ph431_17', 4)	# 130-133
    sprite('ph431_18', 4)	# 134-137
    sprite('ph431_16', 5)	# 138-142
    sprite('ph431_17', 5)	# 143-147
    sprite('ph431_18', 5)	# 148-152
    sprite('ph431_16', 6)	# 153-158
    sprite('ph431_17', 6)	# 159-164
    sprite('ph431_18', 6)	# 165-170
    sprite('ph431_16', 7)	# 171-177
    sprite('ph431_17', 7)	# 178-184
    sprite('ph431_18', 7)	# 185-191
    label(1)
    sprite('ph431_19', 5)	# 192-196
    sprite('ph431_20', 5)	# 197-201
    sprite('ph431_21', 5)	# 202-206
    sprite('ph431_22', 5)	# 207-211
    sprite('ph431_23', 15)	# 212-226
    sprite('ph431_24', 6)	# 227-232
    ExitState()
    label(100)
    sprite('keep', 2)	# 233-234
    sprite('keep', 10)	# 235-244
    sendToLabel(1)

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('rg600_16', 5)	# 1-5
    Unknown1084(1)
    Unknown2034(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('rg600_15', 5)	# 6-10
    sprite('rg600_14', 5)	# 11-15
    sprite('rg600_04', 5)	# 16-20
    sprite('rg600_05', 5)	# 21-25
    sprite('rg600_06', 12)	# 26-37
    sprite('rg600_07', 4)	# 38-41
    sprite('rg600_08', 4)	# 42-45
    SFX_0('006_swing_blade_2')
    sprite('rg600_09', 6)	# 46-51
    sprite('rg600_10', 5)	# 52-56
    sprite('rg600_11', 6)	# 57-62
    sprite('rg600_12', 10)	# 63-72
    SFX_3('rgse_00')
    label(1)
    sprite('rg600_12', 1)	# 73-73
    Unknown30042(24)
    if SLOT_0:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rg600_13', 3)	# 74-76
    sprite('rg600_14', 3)	# 77-79
    sprite('rg600_15', 3)	# 80-82
    sprite('rg600_16', 3)	# 83-85

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9266(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 14)	# 121-134
    sprite('ph035_03', 2)	# 135-136
    Unknown1086(22)
    teleportRelativeX(-200000)
    Unknown1007(30000)
    GFX_0('ph035FireEff2', -1)
    SFX_0('000_airdash_0')
    sprite('ph035_04', 2)	# 137-138
    sprite('ph035_05', 2)	# 139-140
    Unknown3001(255)
    Unknown3004(0)
    sprite('ph035_06', 2)	# 141-142
    sprite('ph252_00', 2)	# 143-144
    sprite('ph252_01', 2)	# 145-146
    sprite('ph252_02', 2)	# 147-148
    GFX_0('CrossBurst_Bomb', -1)
    sprite('ph252_03ex01', 3)	# 149-151	 **attackbox here**
    physicsXImpulse(-2500)
    physicsYImpulse(13000)
    setGravity(1800)
    sprite('ph252_04', 5)	# 152-156
    sprite('ph252_05', 5)	# 157-161
    sprite('ph252_06', 5)	# 162-166
    sprite('ph252_07', 5)	# 167-171
    sprite('ph252_08', 5)	# 172-176
    sprite('ph020_05', 3)	# 177-179
    sprite('ph020_06', 3)	# 180-182
    label(0)
    sprite('ph020_07', 4)	# 183-186
    sprite('ph020_08', 4)	# 187-190
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 191-193
    sprite('ph024_01', 3)	# 194-196
    sprite('ph024_02', 3)	# 197-199
    sprite('ph024_03', 3)	# 200-202
    sprite('ph024_04', 3)	# 203-205
    ExitState()

@State
def CmnActChangeReturnAppealBurst():
    sprite('ph111_05', 6)	# 1-6
    sprite('ph111_06', 6)	# 7-12
    sprite('ph111_07', 6)	# 13-18
    sprite('ph111_08', 12)	# 19-30
    sprite('ph111_09', 6)	# 31-36
    sprite('ph010_02', 6)	# 37-42
    sprite('ph010_01', 6)	# 43-48
    sprite('ph010_00', 6)	# 49-54
    sprite('ph000_00', 6)	# 55-60
    sprite('ph000_00', 30)	# 61-90

@Subroutine
def MagicIconUpDate():
    Unknown23038(0, -6908226)
    if (SLOT_31 >= 5000):
        Unknown23038(0, -256)
    if (SLOT_31 >= 10000):
        Unknown23038(0, -60191)

@Subroutine
def MagicNormalAtkInit():
    Unknown11033(1)
    Unknown11084(1)

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        SLOT_31 = (SLOT_31 + 1200)
        callSubroutine('MagicIconUpDate')

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(1200)
        Unknown9017(1)
        PushbackX(12000)
        AirPushbackY(12500)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph216_00', 2)	# 1-2
    sprite('ph216_01', 3)	# 3-5
    sprite('ph216_02', 2)	# 6-7
    Unknown7009(0)
    sprite('ph216_03', 3)	# 8-10	 **attackbox here**
    SLOT_6 = 300
    GFX_0('ph216_eff', -1)
    SFX_3('phse_02')
    sprite('ph216_04', 3)	# 11-13	 **attackbox here**
    sprite('ph216_05', 6)	# 14-19
    Recovery()
    Unknown2063()
    sprite('ph216_06', 6)	# 20-25

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9017(1)
        AirPushbackY(13000)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph202_00', 3)	# 1-3
    sprite('ph202_01', 4)	# 4-7
    sprite('ph202_02', 4)	# 8-11
    Unknown7009(1)
    sprite('ph202_03', 3)	# 12-14	 **attackbox here**
    SLOT_6 = 300
    GFX_0('ph202_eff', -1)
    SFX_3('phse_02')
    sprite('ph202_03', 2)	# 15-16	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ph202_04', 5)	# 17-21
    sprite('ph202_05', 5)	# 22-26
    sprite('ph202_06', 5)	# 27-31
    sprite('ph202_07', 5)	# 32-36

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9016(1)
        AirPushbackY(13000)
        HitOrBlockCancel('NmlAtk5AAAA_Lv1')
        HitOrBlockCancel('NmlAtk5AAAA_Lv2')
        HitOrBlockCancel('NmlAtk5AAAA_Lv3')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph200_00', 3)	# 1-3
    sprite('ph200_01', 3)	# 4-6
    sprite('ph200_02', 2)	# 7-8
    Unknown7009(1)
    sprite('ph200_03', 3)	# 9-11	 **attackbox here**
    SLOT_6 = 100
    GFX_0('ph200_eff', -1)
    SFX_3('phse_00')
    sprite('ph200_03', 3)	# 12-14	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ph200_04', 5)	# 15-19
    sprite('ph200_05', 5)	# 20-24
    sprite('ph200_06', 5)	# 25-29
    sprite('ph200_07', 5)	# 30-34

@Subroutine
def NormalMagicInitialize():
    if SLOT_36:
        AttackDefaults_AirNormal()
        Unknown1084(1)
        GFX_0('Eff_DriveMagicCircle', -1)
    else:
        AttackDefaults_StandingNormal()

    def upon_STATE_END():
        Unknown1019(0)

@Subroutine
def MagicPointRankDown():
    if (SLOT_31 >= 10000):
        pass
    elif (SLOT_31 >= 5000):
        callSubroutine('MagicIconUpDate')
    else:
        callSubroutine('MagicIconUpDate')

@Subroutine
def MagicPointReset():
    SLOT_31 = 0

@State
def NmlAtk5AAAA_Lv1():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv1')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv2')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv3')
    sprite('ph203_01', 3)	# 1-3
    sprite('ph203_04', 2)	# 4-5
    SFX_4('bph207')
    sprite('ph203_05', 2)	# 6-7
    sprite('ph203_06', 2)	# 8-9
    sprite('ph203_07', 3)	# 10-12
    SLOT_6 = 100
    GFX_0('DriveAtk_BNN', -1)
    callSubroutine('MagicPointRankDown')
    sprite('ph203_08', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('ph203_09', 5)	# 16-20
    sprite('ph203_11', 5)	# 21-25
    sprite('ph203_12', 5)	# 26-30
    sprite('ph203_13', 5)	# 31-35

@State
def NmlAtk5AAAA_Lv2():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv1')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv2')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv3')
    sprite('ph204_01', 3)	# 1-3
    sprite('ph204_02', 2)	# 4-5
    SFX_4('bph210')
    sprite('ph204_05', 2)	# 6-7
    sprite('ph204_06', 2)	# 8-9
    sprite('ph204_07', 3)	# 10-12
    SLOT_6 = 100
    GFX_0('DriveAtk_BBN', -1)
    callSubroutine('MagicPointRankDown')
    physicsXImpulse(-7500)
    Unknown8000(100, 1, 0)
    sprite('ph204_08', 3)	# 13-15
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ph204_09', 3)	# 16-18
    Unknown1019(50)
    sprite('ph204_10', 3)	# 19-21
    sprite('ph204_11', 3)	# 22-24
    Unknown1019(50)
    sprite('ph204_12', 3)	# 25-27
    Unknown1019(0)
    sprite('ph212_11', 4)	# 28-31
    sprite('ph212_12', 4)	# 32-35

@State
def NmlAtk5AAAA_Lv3():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv1')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv2')
        HitOrBlockCancel('NmlAtk5AAAAA_Lv3')
    sprite('ph205_01', 3)	# 1-3
    sprite('ph205_02', 2)	# 4-5
    SFX_4('bph216')
    sprite('ph205_04', 2)	# 6-7
    sprite('ph205_05', 2)	# 8-9
    sprite('ph205_06', 3)	# 10-12
    SLOT_6 = 100
    GFX_0('DriveAtk_BBB', -1)
    callSubroutine('MagicPointRankDown')
    physicsXImpulse(-10000)
    Unknown8000(100, 1, 0)
    sprite('ph205_07', 3)	# 13-15
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ph205_08', 3)	# 16-18
    sprite('ph205_09', 3)	# 19-21
    sprite('ph205_10', 3)	# 22-24
    Unknown1019(50)
    sprite('ph205_11', 3)	# 25-27
    Unknown1019(0)
    sprite('ph205_12', 4)	# 28-31
    sprite('ph205_13', 4)	# 32-35

@State
def NmlAtk5AAAAA_Lv1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        JumpCancel_(0)
    sprite('ph610_00', 3)	# 1-3
    sprite('ph610_01', 5)	# 4-8
    sprite('ph610_02', 5)	# 9-13
    sprite('ph610_03', 2)	# 14-15
    sprite('ph610_04', 6)	# 16-21	 **attackbox here**
    GFX_0('Eff_432_AtkFire', -1)
    GFX_0('Atk5AAAAA_Lv1', -1)
    SLOT_6 = 300
    sprite('ph610_05', 12)	# 22-33
    Recovery()
    Unknown2063()
    sprite('ph610_06', 6)	# 34-39
    sprite('ph432_14', 6)	# 40-45

@State
def NmlAtk5AAAAA_Lv2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        JumpCancel_(0)
    sprite('ph610_00', 3)	# 1-3
    sprite('ph610_01', 5)	# 4-8
    sprite('ph610_02', 5)	# 9-13
    sprite('ph610_03', 2)	# 14-15
    sprite('ph610_04', 6)	# 16-21	 **attackbox here**
    GFX_0('Eff_432_AtkFire', -1)
    GFX_0('Atk5AAAAA_Lv2', -1)
    SLOT_6 = 300
    sprite('ph610_05', 12)	# 22-33
    Recovery()
    Unknown2063()
    sprite('ph610_06', 6)	# 34-39
    sprite('ph432_14', 6)	# 40-45

@State
def NmlAtk5AAAAA_Lv3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        JumpCancel_(0)
    sprite('ph610_00', 3)	# 1-3
    sprite('ph610_01', 5)	# 4-8
    sprite('ph610_02', 5)	# 9-13
    sprite('ph610_03', 2)	# 14-15
    sprite('ph610_04', 6)	# 16-21	 **attackbox here**
    GFX_0('Eff_432_AtkFire', -1)
    GFX_0('Atk5AAAAA_Lv3', -1)
    SLOT_6 = 300
    sprite('ph610_05', 12)	# 22-33
    Recovery()
    Unknown2063()
    sprite('ph610_06', 6)	# 34-39
    sprite('ph432_14', 6)	# 40-45

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        AirPushbackX(10000)
        AirPushbackY(22000)
        GroundedHitstunAnimation(9)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk4AA')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('MagicNormalAtkInit')
    sprite('ph210_00', 2)	# 1-2
    sprite('ph210_01', 2)	# 3-4
    sprite('ph210_02', 2)	# 5-6
    sprite('ph210_03', 2)	# 7-8
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ph210_04', 2)	# 9-10
    Unknown7009(2)
    sprite('ph210_05', 4)	# 11-14	 **attackbox here**
    SLOT_6 = 100
    GFX_0('ph210_eff', -1)
    SFX_3('phse_00')
    sprite('ph210_06', 4)	# 15-18
    setInvincible(0)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ph210_07', 4)	# 19-22
    sprite('ph210_08', 5)	# 23-27
    sprite('ph210_09', 5)	# 28-32
    sprite('ph210_10', 5)	# 33-37
    sprite('ph210_11', 5)	# 38-42
    sprite('ph210_12', 5)	# 43-47

@State
def NmlAtk4AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(10000)
        AirPushbackY(23000)
        Unknown9017(1)
        GroundedHitstunAnimation(9)
        HitOrBlockCancel('NmlAtk4AAA_Lv1')
        HitOrBlockCancel('NmlAtk4AAA_Lv2')
        HitOrBlockCancel('NmlAtk4AAA_Lv3')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('MagicNormalAtkInit')
    sprite('ph212_00', 3)	# 1-3
    sprite('ph212_01', 3)	# 4-6
    sprite('ph212_02', 2)	# 7-8
    sprite('ph212_03', 2)	# 9-10
    sprite('ph212_04', 2)	# 11-12
    sprite('ph212_05', 4)	# 13-16	 **attackbox here**
    SLOT_6 = 300
    GFX_0('ph212_eff', -1)
    SFX_3('phse_02')
    sprite('ph212_06', 4)	# 17-20
    Recovery()
    Unknown2063()
    sprite('ph212_07', 4)	# 21-24
    sprite('ph212_08', 4)	# 25-28
    sprite('ph212_09', 4)	# 29-32
    sprite('ph212_10', 3)	# 33-35
    sprite('ph212_11', 3)	# 36-38
    sprite('ph212_12', 3)	# 39-41

@State
def NmlAtk4AAA_Lv1():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')
    sprite('ph203_01', 3)	# 1-3
    sprite('ph203_02', 3)	# 4-6
    SFX_4('bph206')
    sprite('ph203_04', 2)	# 7-8
    sprite('ph203_05', 2)	# 9-10
    sprite('ph203_06', 2)	# 11-12
    sprite('ph203_07', 3)	# 13-15
    SLOT_6 = 300
    GFX_0('DriveAtk_RNN', -1)
    callSubroutine('MagicPointRankDown')
    sprite('ph203_08', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('ph203_09', 5)	# 19-23
    sprite('ph203_10', 5)	# 24-28
    sprite('ph203_11', 5)	# 29-33
    sprite('ph203_12', 5)	# 34-38
    sprite('ph203_13', 5)	# 39-43

@State
def NmlAtk4AAA_Lv2():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')
    sprite('ph204_01', 3)	# 1-3
    sprite('ph204_02', 3)	# 4-6
    SFX_4('bph209')
    sprite('ph204_03', 2)	# 7-8
    sprite('ph204_05', 2)	# 9-10
    sprite('ph204_06', 2)	# 11-12
    sprite('ph204_07', 3)	# 13-15
    SLOT_6 = 300
    GFX_0('DriveAtk_RRN', -1)
    callSubroutine('MagicPointRankDown')
    physicsXImpulse(-7500)
    Unknown8000(100, 1, 0)
    sprite('ph204_08', 4)	# 16-19
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ph204_09', 4)	# 20-23
    Unknown1019(50)
    sprite('ph204_10', 4)	# 24-27
    sprite('ph204_11', 4)	# 28-31
    Unknown1019(50)
    sprite('ph204_12', 4)	# 32-35
    Unknown1019(0)
    sprite('ph212_11', 4)	# 36-39
    sprite('ph212_12', 4)	# 40-43

@State
def NmlAtk4AAA_Lv3():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')
    sprite('ph205_01', 3)	# 1-3
    sprite('ph205_02', 3)	# 4-6
    SFX_4('bph215')
    sprite('ph205_03', 2)	# 7-8
    sprite('ph205_04', 2)	# 9-10
    sprite('ph205_05', 2)	# 11-12
    sprite('ph205_06', 3)	# 13-15
    SLOT_6 = 300
    GFX_0('DriveAtk_RRR', -1)
    callSubroutine('MagicPointRankDown')
    physicsXImpulse(-10000)
    Unknown8000(100, 1, 0)
    sprite('ph205_07', 4)	# 16-19
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ph205_08', 4)	# 20-23
    sprite('ph205_09', 4)	# 24-27
    sprite('ph205_10', 4)	# 28-31
    Unknown1019(50)
    sprite('ph205_11', 4)	# 32-35
    Unknown1019(0)
    sprite('ph205_12', 4)	# 36-39
    sprite('ph205_13', 4)	# 40-43

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5BB_Lv1')
        HitOrBlockCancel('NmlAtk5BB_Lv2')
        HitOrBlockCancel('NmlAtk5BB_Lv3')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph201_00', 3)	# 1-3
    sprite('ph201_01', 3)	# 4-6
    sprite('ph201_02', 3)	# 7-9
    sprite('ph201_03', 2)	# 10-11
    Unknown7006('bph108_0', 100, 828928098, 828323888, 0, 0, 100, 828928098, 845101104, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ph201_04', 3)	# 12-14	 **attackbox here**
    SLOT_6 = 200
    GFX_0('ph201_eff', -1)
    SFX_3('phse_01')
    sprite('ph201_05', 3)	# 15-17	 **attackbox here**
    sprite('ph201_06', 6)	# 18-23
    Recovery()
    Unknown2063()
    sprite('ph201_07', 5)	# 24-28
    sprite('ph201_08', 5)	# 29-33
    sprite('ph201_09', 5)	# 34-38

@State
def NmlAtk5BB_Lv1():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')

        def upon_43():
            if (SLOT_48 == 6001):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ph203_01', 3)	# 1-3
    sprite('ph203_02', 3)	# 4-6
    SFX_4('bph208')
    GFX_0('Wind_Herald', -1)
    sprite('ph203_04', 2)	# 7-8
    sprite('ph203_05', 2)	# 9-10
    sprite('ph203_06', 2)	# 11-12
    sprite('ph203_07', 3)	# 13-15
    SLOT_6 = 200
    GFX_0('DriveAtk_GNN', -1)
    callSubroutine('MagicPointRankDown')
    sprite('ph203_08', 5)	# 16-20
    sprite('ph203_09', 5)	# 21-25
    sprite('ph203_10', 5)	# 26-30
    sprite('ph203_11', 5)	# 31-35
    sprite('ph203_12', 5)	# 36-40
    sprite('ph203_13', 5)	# 41-45

@State
def NmlAtk5BB_Lv2():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')

        def upon_43():
            if (SLOT_48 == 6001):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ph204_01', 3)	# 1-3
    sprite('ph204_02', 3)	# 4-6
    SFX_4('bph211')
    GFX_0('Wind_Herald', -1)
    sprite('ph204_03', 2)	# 7-8
    sprite('ph204_05', 2)	# 9-10
    sprite('ph204_06', 2)	# 11-12
    sprite('ph204_07', 3)	# 13-15
    SLOT_6 = 200
    GFX_0('DriveAtk_GGN', -1)
    callSubroutine('MagicPointRankDown')
    physicsXImpulse(-7500)
    Unknown8000(100, 1, 0)
    sprite('ph204_07', 2)	# 16-17
    StartMultihit()
    sprite('ph204_08', 4)	# 18-21
    Unknown1019(50)
    sprite('ph204_09', 4)	# 22-25
    Unknown1019(50)
    sprite('ph204_10', 4)	# 26-29
    sprite('ph204_11', 4)	# 30-33
    Unknown1019(50)
    sprite('ph204_12', 4)	# 34-37
    Unknown1019(0)
    sprite('ph212_11', 4)	# 38-41
    sprite('ph212_12', 4)	# 42-45

@State
def NmlAtk5BB_Lv3():

    def upon_IMMEDIATE():
        callSubroutine('NormalMagicInitialize')

        def upon_43():
            if (SLOT_48 == 6001):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ph205_01', 3)	# 1-3
    sprite('ph205_02', 3)	# 4-6
    SFX_4('bph217')
    GFX_0('Wind_Herald', -1)
    sprite('ph205_03', 2)	# 7-8
    sprite('ph205_04', 2)	# 9-10
    sprite('ph205_05', 2)	# 11-12
    sprite('ph205_06', 3)	# 13-15
    SLOT_6 = 200
    GFX_0('DriveAtk_GGG', -1)
    callSubroutine('MagicPointRankDown')
    physicsXImpulse(-10000)
    Unknown8000(100, 1, 0)
    sprite('ph205_06', 2)	# 16-17
    StartMultihit()
    sprite('ph205_07', 4)	# 18-21
    Unknown1019(50)
    sprite('ph205_08', 4)	# 22-25
    sprite('ph205_09', 4)	# 26-29
    sprite('ph205_10', 4)	# 30-33
    Unknown1019(50)
    sprite('ph205_11', 4)	# 34-37
    Unknown1019(0)
    sprite('ph205_12', 4)	# 38-41
    sprite('ph205_13', 4)	# 42-45

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        Unknown9016(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('MagicNormalAtkInit')
    sprite('ph230_00', 3)	# 1-3
    sprite('ph230_01', 3)	# 4-6
    sprite('ph230_02', 3)	# 7-9
    Unknown7009(0)
    sprite('ph230_03', 3)	# 10-12	 **attackbox here**
    SLOT_6 = 100
    GFX_0('ph230_eff', -1)
    SFX_3('phse_00')
    sprite('ph230_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('ph230_05', 4)	# 17-20
    sprite('ph230_06', 4)	# 21-24
    sprite('ph230_07', 4)	# 25-28
    sprite('ph230_08', 4)	# 29-32

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Unknown9016(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        callSubroutine('MagicNormalAtkInit')
    sprite('ph231_00', 3)	# 1-3
    sprite('ph231_00', 1)	# 4-4
    sprite('ph231_01', 3)	# 5-7
    sprite('ph231_02', 3)	# 8-10
    Unknown7006('bph108_0', 100, 828928098, 828323888, 0, 0, 100, 828928098, 845101104, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ph231_03', 3)	# 11-13	 **attackbox here**
    SLOT_6 = 200
    GFX_0('ph231_eff', -1)
    SFX_3('phse_01')
    sprite('ph231_04', 3)	# 14-16	 **attackbox here**
    sprite('ph231_05', 6)	# 17-22
    Recovery()
    Unknown2063()
    sprite('ph231_06', 5)	# 23-27
    sprite('ph231_07', 5)	# 28-32
    sprite('ph231_08', 5)	# 33-37

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(1500)
        AirPushbackY(18000)
        AirUntechableTime(40)
        Unknown9017(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph235_00', 4)	# 1-4
    sprite('ph235_01', 4)	# 5-8
    sprite('ph235_02', 4)	# 9-12
    tag_voice(1, 'bph107_0', 'bph107_1', 'bph107_2', '')
    sprite('ph235_03', 5)	# 13-17	 **attackbox here**
    SLOT_6 = 300
    GFX_0('ph235_eff', -1)
    SFX_3('phse_02')
    sprite('ph235_04', 5)	# 18-22
    Recovery()
    Unknown2063()
    sprite('ph235_05', 5)	# 23-27
    sprite('ph235_06', 5)	# 28-32
    sprite('ph235_07', 5)	# 33-37
    sprite('ph235_08', 5)	# 38-42

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        AirUntechableTime(22)
        AirPushbackX(6000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5C_Lv2')
        HitOrBlockCancel('NmlAtkAIR5C_Lv3')
        HitOrBlockJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph250_00', 3)	# 1-3
    sprite('ph250_01', 2)	# 4-5
    sprite('ph250_02', 2)	# 6-7
    Unknown7009(1)
    sprite('ph250_03', 3)	# 8-10	 **attackbox here**
    SLOT_6 = 100
    GFX_0('ph250_eff', -1)
    SFX_3('phse_00')
    sprite('ph250_04', 6)	# 11-16
    Recovery()
    Unknown2063()
    sprite('ph250_05', 6)	# 17-22
    sprite('ph250_06', 6)	# 23-28
    sprite('ph250_07', 6)	# 29-34
    sprite('ph250_08', 6)	# 35-40

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        AirUntechableTime(22)
        AirPushbackX(6000)
        AirHitstunAnimation(10)
        Unknown9017(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5C_Lv2')
        HitOrBlockCancel('NmlAtkAIR5C_Lv3')
        HitOrBlockJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph252_00', 3)	# 1-3
    sprite('ph252_00', 1)	# 4-4
    sprite('ph252_01', 4)	# 5-8
    sprite('ph252_02', 2)	# 9-10
    Unknown7009(1)
    sprite('ph252_03', 3)	# 11-13	 **attackbox here**
    SLOT_6 = 300
    GFX_0('ph252_eff', -1)
    SFX_3('phse_02')
    sprite('ph252_04', 5)	# 14-18
    Recovery()
    Unknown2063()
    sprite('ph252_05', 5)	# 19-23
    sprite('ph252_06', 5)	# 24-28
    sprite('ph252_07', 5)	# 29-33
    sprite('ph252_08', 5)	# 34-38

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(80)
        Unknown9016(1)
        AirPushbackY(22000)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5BB')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5C_Lv2')
        HitOrBlockCancel('NmlAtkAIR5C_Lv3')
        HitOrBlockJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph253_00', 3)	# 1-3
    sprite('ph253_00', 3)	# 4-6
    sprite('ph253_01', 3)	# 7-9
    sprite('ph253_02', 3)	# 10-12
    Unknown7009(1)
    sprite('ph253_03', 3)	# 13-15	 **attackbox here**
    SLOT_6 = 100
    GFX_0('ph253_eff', -1)
    SFX_3('phse_00')
    sprite('ph253_04', 7)	# 16-22
    Recovery()
    Unknown2063()
    sprite('ph253_05', 7)	# 23-29
    sprite('ph253_06', 7)	# 30-36
    sprite('ph253_07', 7)	# 37-43
    sprite('ph253_08', 7)	# 44-50

@State
def NmlAtkAIR5BB():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(80)
        AirUntechableTime(22)
        AirPushbackX(6000)
        AirHitstunAnimation(10)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockCancel('NmlAtkAIR5C_Lv2')
        HitOrBlockCancel('NmlAtkAIR5C_Lv3')
        HitOrBlockJumpCancel(1)
        callSubroutine('MagicNormalAtkInit')
    sprite('ph251_00', 3)	# 1-3
    sprite('ph251_01', 3)	# 4-6
    sprite('ph251_02', 3)	# 7-9
    Unknown7006('bph108_0', 100, 828928098, 828323888, 0, 0, 100, 828928098, 845101104, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ph251_03', 3)	# 10-12	 **attackbox here**
    SLOT_6 = 200
    GFX_0('ph251_eff', -1)
    SFX_3('phse_01')
    sprite('ph251_04', 3)	# 13-15	 **attackbox here**
    sprite('ph251_04', 3)	# 16-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ph251_05', 6)	# 19-24
    sprite('ph251_06', 6)	# 25-30
    sprite('ph251_07', 6)	# 31-36
    sprite('ph251_08', 6)	# 37-42

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)
        Unknown14082(1)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 6003):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ph205_00', 3)	# 1-3
    sprite('ph205_01', 3)	# 4-6
    Unknown1084(1)
    SFX_4('bph218')
    Unknown21015('447269766541746b5f52524200000000000000000000000000000000000000002923000000000000')
    Unknown21015('447269766541746b5f5252425f4c7632000000000000000000000000000000002923000000000000')
    Unknown21015('447269766541746b5f5252425f4c7633000000000000000000000000000000002923000000000000')
    GFX_1('phef_rrn_mc', 103)
    GFX_0('DriveAtk_RRB', -1)
    GFX_0('Eff_DriveMagicCircle', -1)
    callSubroutine('MagicPointRankDown')
    sprite('ph205_04', 3)	# 7-9
    sprite('ph205_05', 3)	# 10-12
    sprite('ph205_06', 3)	# 13-15
    sprite('ph205_07', 3)	# 16-18
    sprite('ph205_08', 3)	# 19-21
    sprite('ph205_10', 3)	# 22-24
    Unknown1043()
    sprite('ph205_11', 3)	# 25-27
    sprite('ph205_15', 3)	# 28-30
    sprite('ph205_16', 3)	# 31-33
    sprite('ph020_05', 3)	# 34-36
    sprite('ph020_06', 3)	# 37-39
    label(0)
    sprite('ph020_07', 4)	# 40-43
    sprite('ph020_08', 4)	# 44-47
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 48-50
    Unknown1084(1)
    sprite('ph024_01', 3)	# 51-53
    sprite('ph024_02', 3)	# 54-56
    sprite('ph024_03', 3)	# 57-59
    sprite('ph024_04', 3)	# 60-62
    ExitState()

@State
def NmlAtkAIR5C_Lv2():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)
        Unknown14082(1)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 6003):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ph205_00', 3)	# 1-3
    sprite('ph205_01', 3)	# 4-6
    Unknown1084(1)
    SFX_4('bph218')
    Unknown21015('447269766541746b5f52524200000000000000000000000000000000000000002923000000000000')
    Unknown21015('447269766541746b5f5252425f4c7632000000000000000000000000000000002923000000000000')
    Unknown21015('447269766541746b5f5252425f4c7633000000000000000000000000000000002923000000000000')
    GFX_1('phef_rrn_mc', 103)
    GFX_0('DriveAtk_RRB_Lv2', -1)
    GFX_0('Eff_DriveMagicCircle', -1)
    callSubroutine('MagicPointRankDown')
    sprite('ph205_04', 3)	# 7-9
    sprite('ph205_05', 3)	# 10-12
    sprite('ph205_06', 3)	# 13-15
    sprite('ph205_07', 3)	# 16-18
    sprite('ph205_08', 3)	# 19-21
    sprite('ph205_10', 3)	# 22-24
    Unknown1043()
    sprite('ph205_11', 3)	# 25-27
    sprite('ph205_15', 3)	# 28-30
    sprite('ph205_16', 3)	# 31-33
    sprite('ph020_05', 3)	# 34-36
    sprite('ph020_06', 3)	# 37-39
    label(0)
    sprite('ph020_07', 4)	# 40-43
    sprite('ph020_08', 4)	# 44-47
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 48-50
    Unknown1084(1)
    sprite('ph024_01', 3)	# 51-53
    sprite('ph024_02', 3)	# 54-56
    sprite('ph024_03', 3)	# 57-59
    sprite('ph024_04', 3)	# 60-62
    ExitState()

@State
def NmlAtkAIR5C_Lv3():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)
        Unknown14082(1)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 6003):
                clearUponHandler(43)
                Recovery()
                Unknown2063()
    sprite('ph205_00', 3)	# 1-3
    sprite('ph205_01', 3)	# 4-6
    Unknown1084(1)
    SFX_4('bph218')
    Unknown21015('447269766541746b5f52524200000000000000000000000000000000000000002923000000000000')
    Unknown21015('447269766541746b5f5252425f4c7632000000000000000000000000000000002923000000000000')
    Unknown21015('447269766541746b5f5252425f4c7633000000000000000000000000000000002923000000000000')
    GFX_1('phef_rrn_mc', 103)
    GFX_0('DriveAtk_RRB_Lv3', -1)
    GFX_0('Eff_DriveMagicCircle', -1)
    callSubroutine('MagicPointRankDown')
    sprite('ph205_04', 3)	# 7-9
    sprite('ph205_05', 3)	# 10-12
    sprite('ph205_06', 3)	# 13-15
    sprite('ph205_07', 3)	# 16-18
    sprite('ph205_08', 3)	# 19-21
    sprite('ph205_10', 3)	# 22-24
    Unknown1043()
    sprite('ph205_11', 3)	# 25-27
    sprite('ph205_15', 3)	# 28-30
    sprite('ph205_16', 3)	# 31-33
    sprite('ph020_05', 3)	# 34-36
    sprite('ph020_06', 3)	# 37-39
    label(0)
    sprite('ph020_07', 4)	# 40-43
    sprite('ph020_08', 4)	# 44-47
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 48-50
    Unknown1084(1)
    sprite('ph024_01', 3)	# 51-53
    sprite('ph024_02', 3)	# 54-56
    sprite('ph024_03', 3)	# 57-59
    sprite('ph024_04', 3)	# 60-62
    ExitState()

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9266(1)

        def upon_STATE_END():
            Unknown4020(0)
    sprite('ph402_00', 3)	# 1-3
    sprite('ph402_01', 3)	# 4-6
    tag_voice(1, 'bph202_2', 'bph202_1', '', '')
    sprite('ph402_02', 3)	# 7-9
    sprite('ph402_03', 3)	# 10-12
    sprite('ph402_04', 3)	# 13-15
    GFX_0('MidAssault_Atk', -1)
    Unknown38(6, 1)
    Unknown4020(6)
    sprite('ph402_02', 3)	# 16-18
    sprite('ph402_05', 3)	# 19-21
    SFX_0('004_swing_grap_1_1')
    sprite('ph402_06', 2)	# 22-23
    sprite('ph402_07', 2)	# 24-25
    GFX_0('Eff_402Fire_PL', -1)
    sprite('ph402_08', 3)	# 26-28
    sprite('ph402_08', 2)	# 29-30
    Unknown23027()
    sprite('ph402_09', 4)	# 31-34
    ScreenShake(5000, 20000)
    sprite('ph402_10', 4)	# 35-38
    sprite('ph402_11', 4)	# 39-42
    sprite('ph402_12', 4)	# 43-46

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9017(1)
        Unknown23027()
        callSubroutine('ActiveMagicAllDelete')
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('ph402_09', 3)	# 2-4
    ScreenShake(5000, 20000)
    sprite('ph402_10', 2)	# 5-6
    sprite('ph402_11', 2)	# 7-8
    sprite('ph402_12', 2)	# 9-10
    sprite('ph400_00', 2)	# 11-12
    physicsXImpulse(3000)
    sprite('ph400_01', 2)	# 13-14
    Unknown1019(150)
    sprite('ph400_02', 3)	# 15-17	 **attackbox here**
    Unknown1019(150)
    SFX_0('000_airdash_0')
    sprite('ph400_03', 3)	# 18-20	 **attackbox here**
    Unknown1019(200)
    GFX_0('pheff_400', -1)
    Unknown38(5, 1)
    SFX_0('015_blaze_0')
    sprite('ph400_04', 3)	# 21-23	 **attackbox here**
    Unknown1019(200)
    Unknown3038(1)
    Unknown23029(5, 4002, 0)
    tag_voice(0, 'bph157_0', 'bph157_1', '', '')
    sprite('ph400_05', 6)	# 24-29	 **attackbox here**
    Unknown2006()
    Unknown1019(25)
    sprite('ph400_05', 1)	# 30-30	 **attackbox here**
    Unknown3038(0)
    physicsXImpulse(-15000)
    RefreshMultihit()
    SFX_0('016_explode_0')
    SFX_0('016_explode_1')
    sprite('ph400_05', 3)	# 31-33	 **attackbox here**
    StartMultihit()
    sprite('ph400_06', 3)	# 34-36
    Unknown1019(25)
    Recovery()
    sprite('ph400_07', 3)	# 37-39
    Unknown1019(25)
    sprite('ph400_08', 3)	# 40-42
    Unknown1019(25)
    sprite('ph400_09', 3)	# 43-45
    Unknown1019(25)
    sprite('ph400_10', 3)	# 46-48
    Unknown1019(0)
    label(0)
    sprite('ph000_00', 7)	# 49-55
    sprite('ph000_01', 7)	# 56-62
    sprite('ph000_02', 7)	# 63-69
    sprite('ph000_03', 7)	# 70-76
    sprite('ph000_04', 7)	# 77-83
    sprite('ph000_05', 7)	# 84-90
    sprite('ph000_06', 7)	# 91-97
    sprite('ph000_07', 7)	# 98-104
    sprite('ph000_08', 7)	# 105-111
    sprite('ph000_09', 7)	# 112-118
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 119-119

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9266(1)
        Unknown23027()

        def upon_STATE_END():
            Unknown4020(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ph401_00', 4)	# 1-4
    sprite('ph401_01', 4)	# 5-8
    sprite('ph401_02', 6)	# 9-14
    GFX_0('Eff_401', -1)
    Unknown38(6, 1)
    Unknown4020(6)
    SFX_0('016_explode_1')
    SFX_3('phse_02')
    sprite('ph401_03', 3)	# 15-17
    RefreshMultihit()
    physicsXImpulse(10000)
    SFX_0('004_swing_grap_1_2')
    sprite('ph401_04', 3)	# 18-20
    Unknown1019(25)
    sprite('ph401_05', 4)	# 21-24
    Unknown1019(25)
    sprite('ph401_06', 4)	# 25-28
    Unknown1019(0)
    sprite('ph401_07', 4)	# 29-32
    physicsXImpulse(-2000)
    sprite('ph401_08', 4)	# 33-36
    Unknown1019(50)
    sprite('ph401_09', 4)	# 37-40
    Unknown1019(50)
    sprite('ph401_10', 4)	# 41-44
    Unknown1019(50)
    sprite('ph401_11', 4)	# 45-48
    Unknown1019(50)
    label(0)
    sprite('ph000_00', 7)	# 49-55
    sprite('ph000_01', 7)	# 56-62
    sprite('ph000_02', 7)	# 63-69
    sprite('ph000_03', 7)	# 70-76
    sprite('ph000_04', 7)	# 77-83
    sprite('ph000_05', 7)	# 84-90
    sprite('ph000_06', 7)	# 91-97
    sprite('ph000_07', 7)	# 98-104
    sprite('ph000_08', 7)	# 105-111
    sprite('ph000_09', 7)	# 112-118
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 119-119

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9266(1)

        def upon_STATE_END():
            Unknown4020(0)
    sprite('ph440_13', 4)	# 1-4
    sprite('ph440_14', 4)	# 5-8
    sprite('ph440_15', 4)	# 9-12
    sprite('ph440_16', 3)	# 13-15
    GFX_0('BurstDDMaster', -1)
    Unknown38(6, 1)
    Unknown4020(6)
    sprite('ph440_17', 2)	# 16-17
    tag_voice(0, 'bph158_0', 'bph158_1', '', '')
    sprite('ph440_18', 2)	# 18-19
    sprite('ph440_19', 3)	# 20-22
    sprite('ph440_20', 3)	# 23-25
    sprite('ph440_21', 3)	# 26-28
    sprite('ph440_19', 3)	# 29-31
    sprite('ph440_20', 3)	# 32-34
    sprite('ph440_21', 3)	# 35-37
    sprite('ph440_19', 3)	# 38-40
    sprite('ph440_20', 3)	# 41-43
    sprite('ph440_21', 3)	# 44-46
    sprite('ph440_22', 5)	# 47-51
    sprite('ph440_23', 5)	# 52-56
    sprite('ph440_24', 5)	# 57-61
    sprite('ph000_00', 60)	# 62-121

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9017(1)
        Unknown23027()
    sprite('null', 10)	# 1-10
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 11-11
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(1)
    sprite('ph400_00', 3)	# 12-14
    sprite('ph400_01', 3)	# 15-17
    Unknown1019(150)
    sprite('ph400_02', 3)	# 18-20	 **attackbox here**
    Unknown1019(150)
    SFX_0('000_airdash_0')
    sprite('ph400_03', 3)	# 21-23	 **attackbox here**
    Unknown1019(200)
    GFX_0('pheff_400', -1)
    Unknown38(5, 1)
    SFX_0('015_blaze_0')
    sprite('ph400_04', 3)	# 24-26	 **attackbox here**
    Unknown1019(200)
    sprite('ph400_02', 3)	# 27-29	 **attackbox here**
    Unknown1019(50)
    Unknown3038(1)
    Unknown23029(5, 4001, 0)
    sprite('ph400_03', 3)	# 30-32	 **attackbox here**
    Unknown1019(25)
    sprite('ph400_04', 3)	# 33-35	 **attackbox here**
    Unknown1019(25)
    sprite('ph400_05', 6)	# 36-41	 **attackbox here**
    clearUponHandler(11)
    Unknown2006()
    Unknown1019(25)
    sprite('ph400_05', 1)	# 42-42	 **attackbox here**
    Unknown3038(0)
    physicsXImpulse(-15000)
    RefreshMultihit()
    SFX_0('016_explode_1')
    sprite('ph400_05', 3)	# 43-45	 **attackbox here**
    StartMultihit()
    sprite('ph400_06', 3)	# 46-48
    Unknown1019(25)
    Recovery()
    sprite('ph400_07', 3)	# 49-51
    Unknown1019(25)
    sprite('ph400_08', 3)	# 52-54
    Unknown1019(25)
    sprite('ph400_09', 3)	# 55-57
    Unknown1019(25)
    sprite('ph400_10', 3)	# 58-60
    Unknown1019(0)
    label(0)
    sprite('ph000_00', 7)	# 61-67
    sprite('ph000_01', 7)	# 68-74
    sprite('ph000_02', 7)	# 75-81
    sprite('ph000_03', 7)	# 82-88
    sprite('ph000_04', 7)	# 89-95
    sprite('ph000_05', 7)	# 96-102
    sprite('ph000_06', 7)	# 103-109
    sprite('ph000_07', 7)	# 110-116
    sprite('ph000_08', 7)	# 117-123
    sprite('ph000_09', 7)	# 124-130
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 131-131

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9017(1)
        Unknown23027()

        def upon_STATE_END():
            Unknown4020(0)
    sprite('ph340_00', 3)	# 1-3
    Unknown2004(1, 0)
    sprite('ph340_04', 2)	# 4-5
    sprite('ph340_05', 2)	# 6-7
    sprite('ph340_06', 2)	# 8-9
    sprite('ph340_07', 2)	# 10-11
    GFX_0('phef_340_fire', 100)
    SFX_0('004_swing_grap_1_2')
    SFX_3('phse_02')
    sprite('ph340_08', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('ph340_09', 2)	# 15-16
    sprite('ph340_10', 2)	# 17-18
    sprite('ph340_11', 2)	# 19-20
    sprite('ph340_12', 2)	# 21-22
    sprite('ph340_13', 3)	# 23-25
    sprite('ph340_14', 3)	# 26-28
    sprite('ph340_15', 3)	# 29-31
    sprite('ph340_16', 3)	# 32-34
    sprite('ph340_17', 2)	# 35-36
    sprite('ph340_18', 2)	# 37-38
    sprite('ph000_00', 7)	# 39-45
    sprite('ph000_01', 7)	# 46-52
    sprite('ph000_02', 7)	# 53-59
    sprite('ph000_03', 7)	# 60-66
    sprite('ph000_04', 7)	# 67-73
    sprite('ph000_05', 7)	# 74-80
    sprite('ph000_06', 7)	# 81-87
    sprite('ph000_07', 7)	# 88-94
    sprite('ph000_08', 7)	# 95-101
    sprite('ph000_09', 7)	# 102-108

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9266(1)

        def upon_STATE_END():
            Unknown4020(0)
    sprite('ph440_13', 4)	# 1-4
    sprite('ph440_14', 4)	# 5-8
    sprite('ph440_15', 4)	# 9-12
    sprite('ph440_16', 3)	# 13-15
    GFX_0('BurstDDMaster', -1)
    Unknown38(6, 1)
    Unknown4020(6)
    sprite('ph440_17', 2)	# 16-17
    sprite('ph440_18', 2)	# 18-19
    sprite('ph440_19', 3)	# 20-22
    sprite('ph440_20', 3)	# 23-25
    sprite('ph440_21', 3)	# 26-28
    sprite('ph440_19', 3)	# 29-31
    sprite('ph440_20', 3)	# 32-34
    sprite('ph440_21', 3)	# 35-37
    sprite('ph440_19', 3)	# 38-40
    sprite('ph440_20', 3)	# 41-43
    sprite('ph440_21', 3)	# 44-46
    sprite('ph440_22', 5)	# 47-51
    sprite('ph440_23', 5)	# 52-56
    sprite('ph440_24', 5)	# 57-61
    sprite('ph000_00', 60)	# 62-121

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ph030_00', 6)	# 1-6
    physicsXImpulse(10000)
    label(0)
    sprite('ph030_01', 6)	# 7-12
    sprite('ph030_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 6)	# 19-24
    sprite('ph030_04', 6)	# 25-30
    sprite('ph030_05', 6)	# 31-36
    sprite('ph030_06', 6)	# 37-42
    sprite('ph030_07', 6)	# 43-48
    sprite('ph030_08', 6)	# 49-54
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 6)	# 55-60
    sprite('ph030_10', 6)	# 61-66
    sprite('ph030_11', 6)	# 67-72
    sprite('ph030_12', 6)	# 73-78
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph310_00', 1)	# 79-79
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ph310_01', 2)	# 80-81
    sprite('ph310_02', 3)	# 82-84	 **attackbox here**
    SFX_0('007_swing_knife_0')
    Unknown1084(1)
    sprite('ph310_03', 3)	# 85-87
    sprite('ph310_04', 5)	# 88-92
    SFX_1('bph155')
    sprite('ph310_05', 5)	# 93-97
    sprite('ph310_06', 5)	# 98-102
    sprite('ph310_07', 5)	# 103-107

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        AttackP2(100)
        PushbackX(35000)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(50)
        Unknown9142(90)
        Unknown11064(1)
        JumpCancel_(0)
        Unknown11069('ThrowExeFinish')
    sprite('ph310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ph311_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    SFX_1('bph153')
    sprite('ph311_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph311_02', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('keep', 10)	# 13-22
    enterState('ThrowExeFinish')

@State
def ThrowExeFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(30)
        AirHitstunAfterWallbounce(40)
        Unknown9362(1)
        Unknown9364(42)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(55000)
        AirPushbackY(18000)
        Unknown9178(1)
        WallbounceReboundTime(45)
        Unknown11091(100)
        Unknown11044(1)
        Unknown13045(0)
        setInvincible(1)
        Unknown30048(1)
    sprite('ph311_03', 8)	# 1-8
    sprite('ph311_04', 8)	# 9-16
    sprite('ph311_05', 8)	# 17-24
    sprite('ph311_06', 8)	# 25-32
    sprite('ph311_07', 8)	# 33-40
    sprite('ph311_08', 20)	# 41-60
    sprite('ph311_09', 3)	# 61-63	 **attackbox here**
    RefreshMultihit()
    sprite('ph311_10', 4)	# 64-67
    sprite('ph311_11', 4)	# 68-71
    sprite('ph311_12', 4)	# 72-75
    sprite('ph311_13', 4)	# 76-79
    sprite('ph311_14', 4)	# 80-83
    sprite('ph311_15', 4)	# 84-87

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ph030_00', 6)	# 1-6
    physicsXImpulse(10000)
    label(0)
    sprite('ph030_01', 6)	# 7-12
    sprite('ph030_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_03', 6)	# 19-24
    sprite('ph030_04', 6)	# 25-30
    sprite('ph030_05', 6)	# 31-36
    sprite('ph030_06', 6)	# 37-42
    sprite('ph030_07', 6)	# 43-48
    sprite('ph030_08', 6)	# 49-54
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ph030_09', 6)	# 55-60
    sprite('ph030_10', 6)	# 61-66
    sprite('ph030_11', 6)	# 67-72
    sprite('ph030_12', 6)	# 73-78
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph310_00', 1)	# 79-79
    clearUponHandler(3)
    Unknown1019(10)
    sprite('ph310_01', 2)	# 80-81
    sprite('ph310_02', 3)	# 82-84	 **attackbox here**
    SFX_0('007_swing_knife_0')
    Unknown1084(1)
    sprite('ph310_03', 3)	# 85-87
    sprite('ph310_04', 5)	# 88-92
    SFX_1('bph155')
    sprite('ph310_05', 5)	# 93-97
    sprite('ph310_06', 5)	# 98-102
    sprite('ph310_07', 5)	# 103-107

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(0)
        AttackP2(100)
        PushbackX(35000)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(50)
        Unknown9142(90)
        Unknown11064(1)
        Unknown13021(1)
        JumpCancel_(0)
        Unknown21005(1)
        Unknown11069('ThrowExeFinish')
    sprite('ph310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ph313_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph313_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph313_02', 3)	# 10-12
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph313_03', 3)	# 13-15
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('ph313_04', 3)	# 16-18
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph313_05', 3)	# 19-21
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph313_06', 3)	# 22-24
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph311_00', 3)	# 25-27
    Unknown2005()
    SFX_1('bph153')
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph311_01', 3)	# 28-30
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ph311_02', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    sprite('keep', 10)	# 34-43
    enterState('ThrowExeFinish')

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(3)
        Damage(2000)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(25000)
        AirUntechableTime(60)
        Unknown23027()
    sprite('ph404_00', 3)	# 1-3
    sprite('ph404_01', 3)	# 4-6
    tag_voice(1, 'bph204_0', 'bph204_1', 'bph204_2', '')
    sprite('ph404_03', 3)	# 7-9
    if (SLOT_6 == 0):
        GFX_1('phef_buf_red', 103)
        GFX_0('Eff_BuffAtkR', -1)
    if (SLOT_6 == 100):
        GFX_1('phef_buf_blue', 103)
        GFX_0('Eff_BuffAtkB', -1)
    if (SLOT_6 == 200):
        GFX_1('phef_buf_green', 103)
        GFX_0('Eff_BuffAtkG', -1)
    if (SLOT_6 == 300):
        GFX_1('phef_buf_red', 103)
        GFX_0('Eff_BuffAtkR', -1)
    sprite('ph404_04', 3)	# 10-12
    sprite('ph404_02', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 30000)
    SFX_3('phse_09')
    sprite('ph404_03', 3)	# 16-18
    Unknown23027()
    setInvincible(0)
    sprite('ph404_04', 3)	# 19-21
    sprite('ph404_02', 3)	# 22-24	 **attackbox here**
    sprite('ph404_03', 3)	# 25-27
    sprite('ph404_04', 3)	# 28-30
    sprite('ph404_02', 3)	# 31-33	 **attackbox here**
    sprite('ph404_03', 3)	# 34-36
    sprite('ph404_04', 3)	# 37-39
    sprite('ph404_02', 3)	# 40-42	 **attackbox here**
    sprite('ph404_03', 3)	# 43-45
    sprite('ph404_04', 3)	# 46-48
    sprite('ph404_01', 5)	# 49-53
    sprite('ph404_00', 6)	# 54-59

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown1084(1)
        AttackLevel_(3)
        Damage(2000)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(25000)
        AirUntechableTime(60)
        Unknown23027()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('ph404_00', 3)	# 1-3
    sprite('ph404_01ex01', 3)	# 4-6
    tag_voice(1, 'bph204_0', 'bph204_1', 'bph204_2', '')
    sprite('ph404_03ex01', 3)	# 7-9
    if (SLOT_6 == 0):
        GFX_1('phef_buf_red', 103)
        GFX_0('Eff_BuffAtkR', -1)
    if (SLOT_6 == 100):
        GFX_1('phef_buf_blue', 103)
        GFX_0('Eff_BuffAtkB', -1)
    if (SLOT_6 == 200):
        GFX_1('phef_buf_green', 103)
        GFX_0('Eff_BuffAtkG', -1)
    if (SLOT_6 == 300):
        GFX_1('phef_buf_red', 103)
        GFX_0('Eff_BuffAtkR', -1)
    sprite('ph404_04ex01', 3)	# 10-12
    sprite('ph404_02ex01', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 30000)
    SFX_3('phse_09')
    sprite('ph404_03ex01', 3)	# 16-18
    Unknown23027()
    setInvincible(0)
    sprite('ph404_04ex01', 3)	# 19-21
    sprite('ph404_02ex01', 3)	# 22-24	 **attackbox here**
    sprite('ph404_03ex01', 3)	# 25-27
    sprite('ph404_04ex01', 3)	# 28-30
    sprite('ph404_01ex01', 3)	# 31-33
    Unknown1043()
    sprite('ph020_06', 4)	# 34-37
    label(0)
    sprite('ph020_07', 4)	# 38-41
    sprite('ph020_08', 4)	# 42-45
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 46-48
    sprite('ph024_01', 3)	# 49-51
    sprite('ph024_02', 3)	# 52-54
    sprite('ph024_03', 3)	# 55-57
    sprite('ph024_04', 3)	# 58-60
    ExitState()

@Subroutine
def SpecialMagicInitialize():
    if SLOT_36:
        Unknown17003()
        Unknown1084(1)
        GFX_0('Eff_DriveMagicCircle', -1)
    else:
        AttackDefaults_StandingSpecial()
    Unknown11063(1)

@State
def MagicActivate_Lv0():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
        Unknown11063(0)
    sprite('ph203_00', 2)	# 1-2
    sprite('ph203_01', 2)	# 3-4
    sprite('ph203_05', 2)	# 5-6
    SFX_4('bph205')
    sprite('ph203_06', 2)	# 7-8
    sprite('ph203_07', 3)	# 9-11
    GFX_0('DriveAtk_NNN', -1)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph203_08', 5)	# 12-16
    sprite('ph203_09', 5)	# 17-21
    sprite('ph203_10', 5)	# 22-26
    sprite('ph203_11', 5)	# 27-31
    Unknown1043()
    sprite('ph203_12', 5)	# 32-36
    Unknown23183('70683230335f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    sprite('ph203_13', 5)	# 37-41
    Unknown23183('70683230335f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateA_Lv1():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
        Unknown11063(0)
    sprite('ph203_00', 3)	# 1-3
    sprite('ph203_01', 3)	# 4-6
    SFX_4('bph213')
    sprite('ph203_02', 3)	# 7-9
    sprite('ph203_06', 3)	# 10-12
    sprite('ph203_07', 3)	# 13-15
    sprite('ph203_08', 3)	# 16-18
    Unknown21015('447269766541746b5f42524e00000000000000000000000000000000000000008913000000000000')
    GFX_0('DriveAtk_BRN', -1)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph203_09', 3)	# 19-21
    sprite('ph203_10', 3)	# 22-24
    sprite('ph203_08', 3)	# 25-27
    sprite('ph203_09', 3)	# 28-30
    sprite('ph203_10', 3)	# 31-33
    sprite('ph203_08', 3)	# 34-36
    sprite('ph203_09', 3)	# 37-39
    sprite('ph203_10', 3)	# 40-42
    sprite('ph203_11', 4)	# 43-46
    sprite('ph203_12', 3)	# 47-49
    Unknown23183('70683230335f3135000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1043()
    sprite('ph203_13', 3)	# 50-52
    Unknown23183('70683230335f3136000000000000000000000000000000000000000000000000030000000200000024000000')

@State
def MagicActivateA_Lv2():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
        Unknown2037(0)

        def upon_3():
            if CheckInput(0x5):
                SLOT_53 = 1
            if SLOT_2:
                if SLOT_53:
                    if (SLOT_18 >= 35):
                        clearUponHandler(3)
                        Unknown23029(8, 5014, 0)
                        sendToLabel(9)
                    else:
                        clearUponHandler(3)
                        Unknown23029(8, 5013, 0)
                        sendToLabel(1)
            if (SLOT_18 >= 65):
                clearUponHandler(3)
                Unknown23029(8, 5014, 0)
                sendToLabel(9)

        def upon_43():
            if (SLOT_48 == 5015):
                clearUponHandler(43)
                clearUponHandler(3)
                sendToLabel(1)
    sprite('ph204_01', 3)	# 1-3
    sprite('ph204_02', 3)	# 4-6
    SFX_4('bph223')
    sprite('ph204_05', 3)	# 7-9
    sprite('ph204_06', 3)	# 10-12
    sprite('ph204_07', 3)	# 13-15
    Unknown21015('447269766541746b5f4747425f41544b4d6173746572000000000000000000009313000000000000')
    Unknown23029(8, 5012, 0)
    GFX_1('phef_ggb_mc', 103)
    GFX_0('DriveAtk_GGB', -1)
    Unknown38(8, 1)
    callSubroutine('MagicPointReset')
    sprite('ph204_08', 4)	# 16-19
    Unknown2037(1)
    sprite('ph204_09', 4)	# 20-23
    sprite('ph204_10', 4)	# 24-27
    label(0)
    sprite('ph204_08', 4)	# 28-31
    sprite('ph204_09', 4)	# 32-35
    sprite('ph204_10', 4)	# 36-39
    gotoLabel(0)
    label(1)
    sprite('ph204_08', 4)	# 40-43
    sprite('ph204_09', 4)	# 44-47
    sprite('ph204_10', 4)	# 48-51
    sprite('ph204_08', 4)	# 52-55
    sprite('ph204_09', 4)	# 56-59
    sprite('ph204_10', 4)	# 60-63
    sprite('ph204_08', 4)	# 64-67
    sprite('ph204_09', 4)	# 68-71
    sprite('ph204_10', 4)	# 72-75
    sprite('ph204_08', 4)	# 76-79
    label(9)
    sprite('ph204_09', 4)	# 80-83
    sprite('ph204_10', 4)	# 84-87
    sprite('ph212_11', 4)	# 88-91
    Unknown23183('70683230345f3135000000000000000000000000000000000000000000000000040000000200000024000000')
    Unknown1043()
    sprite('ph212_12', 4)	# 92-95
    Unknown23183('70683230345f3136000000000000000000000000000000000000000000000000040000000200000024000000')

@State
def MagicActivateA_Lv3():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
    sprite('ph205_00', 3)	# 1-3
    sprite('ph205_01', 3)	# 4-6
    GFX_1('phef_rrn_mc', 103)
    SFX_4('bph220')
    sprite('ph205_04', 3)	# 7-9
    sprite('ph205_05', 3)	# 10-12
    sprite('ph205_06', 3)	# 13-15
    Unknown21015('447269766541746b5f42425200000000000000000000000000000000000000009d13000000000000')
    GFX_0('DriveAtk_BBR', -1)
    callSubroutine('MagicPointReset')
    sprite('ph205_07', 5)	# 16-20
    sprite('ph205_10', 5)	# 21-25
    sprite('ph205_11', 5)	# 26-30
    sprite('ph205_12', 5)	# 31-35
    Unknown23183('70683230355f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    Unknown1043()
    sprite('ph205_13', 5)	# 36-40
    Unknown23183('70683230355f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateB_Lv1():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
        Unknown11063(0)
    sprite('ph203_00', 3)	# 1-3
    sprite('ph203_01', 3)	# 4-6
    SFX_4('bph212')
    sprite('ph203_02', 3)	# 7-9
    sprite('ph203_06', 3)	# 10-12
    sprite('ph203_07', 3)	# 13-15
    sprite('ph203_08', 3)	# 16-18
    Unknown21015('447269766541746b5f47524e0000000000000000000000000000000000000000ed13000000000000')
    GFX_0('DriveAtk_GRN', -1)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph203_09', 3)	# 19-21
    sprite('ph203_10', 3)	# 22-24
    sprite('ph203_08', 3)	# 25-27
    sprite('ph203_09', 3)	# 28-30
    sprite('ph203_10', 3)	# 31-33
    sprite('ph203_08', 3)	# 34-36
    sprite('ph203_09', 3)	# 37-39
    sprite('ph203_10', 3)	# 40-42
    sprite('ph203_11', 4)	# 43-46
    sprite('ph203_12', 3)	# 47-49
    Unknown23183('70683230335f3135000000000000000000000000000000000000000000000000030000000200000024000000')
    Unknown1043()
    sprite('ph203_13', 3)	# 50-52
    Unknown23183('70683230335f3136000000000000000000000000000000000000000000000000030000000200000024000000')

@State
def MagicActivateB_Lv2():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
    sprite('ph204_01', 3)	# 1-3
    Unknown23183('70683230345f3134000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph204_02', 3)	# 4-6
    SFX_4('bph219')
    sprite('ph204_05', 3)	# 7-9
    sprite('ph204_06', 3)	# 10-12
    sprite('ph204_07', 3)	# 13-15
    Unknown21015('447269766541746b5f5252470000000000000000000000000000000000000000f713000000000000')
    GFX_0('DriveAtk_RRG', -1)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph204_08', 5)	# 16-20
    sprite('ph204_09', 5)	# 21-25
    sprite('ph204_10', 5)	# 26-30
    sprite('ph212_11', 5)	# 31-35
    Unknown23183('70683230345f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    Unknown1043()
    sprite('ph212_12', 5)	# 36-40
    Unknown23183('70683230345f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateB_Lv3():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
    sprite('ph205_00', 3)	# 1-3
    sprite('ph205_01', 3)	# 4-6
    SFX_4('bph222')
    sprite('ph205_04', 3)	# 7-9
    sprite('ph205_05', 3)	# 10-12
    sprite('ph205_06', 3)	# 13-15
    Unknown21015('447269766541746b5f47475200000000000000000000000000000000000000000114000000000000')
    GFX_0('DriveAtk_GGR', -1)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph205_07', 5)	# 16-20
    sprite('ph205_10', 5)	# 21-25
    sprite('ph205_11', 5)	# 26-30
    sprite('ph205_12', 5)	# 31-35
    Unknown23183('70683230355f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    Unknown1043()
    sprite('ph205_13', 5)	# 36-40
    Unknown23183('70683230355f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateEX_Lv1():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
    sprite('ph203_00', 3)	# 1-3
    sprite('ph203_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    GFX_1('phef_rgb_mc', 103)
    SFX_4('bph224')
    sprite('ph203_06', 3)	# 7-9
    sprite('ph203_07', 3)	# 10-12
    sprite('ph203_08', 3)	# 13-15
    Unknown23029(7, 5201, 0)
    GFX_0('DriveAtk_BGR', -1)
    Unknown38(7, 1)
    Unknown23029(7, 5202, 0)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph203_09', 3)	# 16-18
    sprite('ph203_10', 3)	# 19-21
    sprite('ph203_08', 3)	# 22-24
    sprite('ph203_09', 3)	# 25-27
    sprite('ph203_11', 3)	# 28-30
    sprite('ph203_12', 5)	# 31-35
    Unknown23183('70683230335f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    Unknown1043()
    sprite('ph203_13', 5)	# 36-40
    Unknown23183('70683230335f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateEX_Lv2():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
    sprite('ph204_01', 3)	# 1-3
    Unknown23183('70683230345f3134000000000000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph204_02', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    GFX_1('phef_rgb_mc', 103)
    SFX_4('bph224')
    sprite('ph204_05', 3)	# 7-9
    sprite('ph204_06', 3)	# 10-12
    sprite('ph204_07', 3)	# 13-15
    Unknown23029(7, 5201, 0)
    GFX_0('DriveAtk_BGR', -1)
    Unknown38(7, 1)
    Unknown23029(7, 5203, 0)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph204_08', 5)	# 16-20
    sprite('ph204_09', 5)	# 21-25
    sprite('ph204_10', 5)	# 26-30
    sprite('ph212_11', 5)	# 31-35
    Unknown23183('70683230345f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    Unknown1043()
    sprite('ph212_12', 5)	# 36-40
    Unknown23183('70683230345f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateEX_Lv3():

    def upon_IMMEDIATE():
        callSubroutine('SpecialMagicInitialize')
    sprite('ph205_00', 3)	# 1-3
    sprite('ph205_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    GFX_1('phef_rgb_mc', 103)
    SFX_4('bph224')
    sprite('ph205_04', 3)	# 7-9
    sprite('ph205_05', 3)	# 10-12
    sprite('ph205_06', 3)	# 13-15
    Unknown23029(7, 5201, 0)
    GFX_0('DriveAtk_BGR', -1)
    Unknown38(7, 1)
    Unknown23029(7, 5204, 0)
    callSubroutine('MagicPointReset')
    if SLOT_37:
        Unknown8000(100, 1, 0)
    sprite('ph205_07', 5)	# 16-20
    sprite('ph205_10', 5)	# 21-25
    sprite('ph205_11', 5)	# 26-30
    sprite('ph205_12', 5)	# 31-35
    Unknown23183('70683230355f3135000000000000000000000000000000000000000000000000050000000200000024000000')
    Unknown1043()
    sprite('ph205_13', 5)	# 36-40
    Unknown23183('70683230355f3136000000000000000000000000000000000000000000000000050000000200000024000000')

@State
def MagicActivateEX_Special():

    def upon_IMMEDIATE():
        if SLOT_36:
            Unknown17003()
        else:
            AttackDefaults_StandingSpecial()
    sprite('ph403_00', 3)	# 1-3
    sprite('ph403_01', 2)	# 4-5
    Unknown23183('70683430335f3031657830310000000000000000000000000000000000000000020000000200000024000000')
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'bph106_0', 'bph106_1', 'bph106_2', '')
    Unknown23029(7, 5205, 0)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    sprite('ph403_02', 2)	# 6-7
    Unknown23183('70683430335f3032657830310000000000000000000000000000000000000000020000000200000024000000')
    sprite('ph403_03', 3)	# 8-10
    Unknown23183('70683430335f3033657830310000000000000000000000000000000000000000030000000200000024000000')
    GFX_0('Eff_MagicConv', 0)
    sprite('ph403_04', 3)	# 11-13
    Unknown23183('70683430335f3034657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_05', 3)	# 14-16
    Unknown23183('70683430335f3035657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_03', 3)	# 17-19
    Unknown23183('70683430335f3033657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_04', 3)	# 20-22
    Unknown23183('70683430335f3034657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_05', 3)	# 23-25
    Unknown23183('70683430335f3035657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_03', 3)	# 26-28
    Unknown23183('70683430335f3033657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_04', 3)	# 29-31
    Unknown23183('70683430335f3034657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_05', 3)	# 32-34
    Unknown23183('70683430335f3035657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_03', 3)	# 35-37
    Unknown23183('70683430335f3033657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_04', 3)	# 38-40
    Unknown23183('70683430335f3034657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_05', 3)	# 41-43
    Unknown23183('70683430335f3035657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_03', 3)	# 44-46
    Unknown23183('70683430335f3033657830310000000000000000000000000000000000000000030000000200000024000000')
    sprite('ph403_02', 3)	# 47-49
    Unknown23183('70683430335f3032657830310000000000000000000000000000000000000000030000000200000024000000')
    if SLOT_36:
        Unknown1018()
        Unknown1043()
    sprite('ph403_01', 2)	# 50-51
    Unknown23183('70683430335f3031657830310000000000000000000000000000000000000000020000000200000024000000')
    sprite('keep', 1)	# 52-52
    if SLOT_36:
        sendToLabel(1)
    sprite('ph403_00', 3)	# 53-55
    ExitState()
    label(1)
    sprite('ph020_04', 3)	# 56-58
    ExitState()

@State
def LandAssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(90)
        AirUntechableTime(40)
        GroundedHitstunAnimation(9)
        AirPushbackX(15000)
        AirPushbackY(10000)
        PushbackX(8000)
        Unknown11032('400d0300c0f2fcff400d0300c0f2fcff')
        Unknown23027()
        Unknown9310(1)
        SLOT_54 = 0

        def upon_11():
            clearUponHandler(11)
            SLOT_54 = 1
            physicsXImpulse(80000)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown1019(25)
    sprite('ph400_00', 3)	# 1-3
    tag_voice(1, 'bph200_0', 'bph200_1', 'bph200_2', '')
    physicsXImpulse(2500)
    sprite('ph400_01', 3)	# 4-6
    Unknown1019(150)
    sprite('ph400_02', 2)	# 7-8	 **attackbox here**
    Unknown1019(150)
    SFX_0('000_airdash_0')
    sprite('ph400_03', 2)	# 9-10	 **attackbox here**
    Unknown1019(400)
    GFX_0('pheff_400', -1)
    Unknown38(5, 1)
    SFX_0('015_blaze_0')
    sprite('ph400_04', 2)	# 11-12	 **attackbox here**
    Unknown1019(800)
    sprite('ph400_02', 3)	# 13-15	 **attackbox here**
    Unknown1019(50)
    Unknown3038(1)
    RefreshMultihit()
    Unknown23029(5, 4001, 0)
    sprite('ph400_03', 3)	# 16-18	 **attackbox here**
    Unknown1019(25)
    sprite('ph400_04', 3)	# 19-21	 **attackbox here**
    Unknown1019(25)
    label(1)
    sprite('ph400_05', 6)	# 22-27	 **attackbox here**
    clearUponHandler(11)
    Unknown2006()
    Unknown1019(25)
    Unknown9310(-1)
    sprite('ph400_05', 1)	# 28-28	 **attackbox here**
    Unknown3038(0)
    physicsXImpulse(-15000)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AirPushbackX(7500)
    AirPushbackY(-30000)
    PushbackX(12000)
    Unknown9017(1)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown11032('90d00300702ffcffe0930400206cfbff')
    if SLOT_54:
        Unknown11032('ffffffffffffffffffffffffffffffff')
    Unknown11080(1)
    Unknown9190(1)
    Unknown9118(30)

    def upon_11():
        clearUponHandler(11)
        SLOT_54 = 1
    SFX_0('016_explode_0')
    SFX_0('016_explode_1')
    sprite('ph400_05', 3)	# 29-31	 **attackbox here**
    StartMultihit()
    sprite('ph400_06', 5)	# 32-36
    Unknown23183('70683430305f3036000000000000000000000000000000000000000000000000040000000200000036000000')
    Unknown1019(25)
    Recovery()
    sprite('ph400_07', 5)	# 37-41
    Unknown23183('70683430305f3037000000000000000000000000000000000000000000000000040000000200000036000000')
    Unknown1019(25)
    sprite('ph400_08', 5)	# 42-46
    Unknown23183('70683430305f3038000000000000000000000000000000000000000000000000040000000200000036000000')
    Unknown1019(25)
    sprite('ph400_09', 5)	# 47-51
    Unknown23183('70683430305f3039000000000000000000000000000000000000000000000000040000000200000036000000')
    Unknown1019(25)
    sprite('ph400_10', 5)	# 52-56
    Unknown23183('70683430305f3130000000000000000000000000000000000000000000000000040000000200000036000000')
    Unknown1019(0)

@State
def LandAssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
        Unknown2004(1, 0)
    sprite('ph401_00', 3)	# 1-3
    sprite('ph401_01', 3)	# 4-6
    tag_voice(1, 'bph201_0', 'bph201_1', 'bph201_2', '')
    Unknown18009(1)
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ph401_02', 6)	# 7-12
    GFX_0('Eff_401', -1)
    SFX_0('016_explode_1')
    SFX_3('phse_02')
    sprite('ph401_03', 3)	# 13-15
    physicsXImpulse(10000)
    SFX_0('004_swing_grap_1_2')
    sprite('ph401_04', 3)	# 16-18
    Unknown1019(25)
    sprite('ph401_05', 5)	# 19-23
    Recovery()
    setInvincible(0)
    Unknown1019(25)
    sprite('ph401_06', 5)	# 24-28
    Unknown1019(0)
    sprite('ph401_07', 5)	# 29-33
    physicsXImpulse(-2000)
    sprite('ph401_08', 5)	# 34-38
    Unknown1019(50)
    sprite('ph401_09', 5)	# 39-43
    Unknown18009(0)
    Unknown1019(50)
    sprite('ph401_10', 5)	# 44-48
    Unknown1019(50)
    sprite('ph401_11', 5)	# 49-53
    Unknown1019(50)

@State
def LandAssaultEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()

        def upon_43():
            if (SLOT_48 == 4403):
                sendToLabel(1)
            if (SLOT_48 == 4405):
                clearUponHandler(43)
                setInvincible(0)
                Recovery()
    sprite('ph440_13', 3)	# 1-3
    sprite('ph440_13', 3)	# 4-6
    tag_voice(1, 'bph280_0', 'bph280_1', '', '')
    Unknown23125('')
    Unknown2058(-5000)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('ph440_14', 6)	# 7-12
    GFX_0('BurstDDMaster', -1)
    Unknown38(5, 1)
    Unknown23029(5, 4402, 0)
    sprite('ph440_15', 6)	# 13-18
    sprite('ph440_16', 3)	# 19-21
    sprite('ph440_17', 2)	# 22-23
    sprite('ph440_18', 2)	# 24-25
    sprite('ph440_19', 3)	# 26-28
    ScreenShake(25000, 10000)
    sprite('ph440_20', 3)	# 29-31
    sprite('ph440_21', 3)	# 32-34
    sprite('ph440_19', 3)	# 35-37
    sprite('ph440_20', 3)	# 38-40
    sprite('ph440_21', 3)	# 41-43
    sprite('ph440_19', 4)	# 44-47
    sprite('ph440_20', 4)	# 48-51
    sprite('ph440_21', 4)	# 52-55
    sprite('ph440_22', 5)	# 56-60
    sprite('ph440_23', 5)	# 61-65
    sprite('ph440_24', 5)	# 66-70
    ExitState()
    label(1)
    sprite('ph440_19', 3)	# 71-73
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000001000000')
    GFX_0('BurstDDBomb', -1)
    clearUponHandler(43)
    sprite('ph440_20', 3)	# 74-76
    sprite('ph440_21', 3)	# 77-79
    sprite('ph440_19', 3)	# 80-82
    sprite('ph440_20', 3)	# 83-85
    sprite('ph440_21', 3)	# 86-88
    sprite('ph440_19', 3)	# 89-91
    sprite('ph440_20', 3)	# 92-94
    sprite('ph440_21', 3)	# 95-97
    sprite('ph440_19', 4)	# 98-101
    sprite('ph440_20', 4)	# 102-105
    sprite('ph440_21', 4)	# 106-109
    sprite('ph440_19', 4)	# 110-113
    sprite('ph440_20', 4)	# 114-117
    sprite('ph440_21', 4)	# 118-121
    sprite('ph440_19', 4)	# 122-125
    tag_voice(0, 'bph281_0', 'bph281_1', '', '')
    sprite('ph440_20', 4)	# 126-129
    sprite('ph440_21', 4)	# 130-133
    sprite('ph440_19', 4)	# 134-137
    setInvincible(0)
    sprite('ph440_20', 4)	# 138-141
    sprite('ph440_21', 4)	# 142-145
    sprite('ph440_19', 4)	# 146-149
    sprite('ph440_20', 4)	# 150-153
    sprite('ph440_21', 4)	# 154-157
    sprite('ph440_22', 4)	# 158-161
    sprite('ph440_23', 4)	# 162-165
    sprite('ph440_24', 4)	# 166-169
    ExitState()

@State
def AirAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        AttackLevel_(3)
        Damage(950)
        AttackP1(90)
        AirUntechableTime(40)
        AirPushbackX(15000)
        AirPushbackY(7500)
        PushbackX(8000)
        GroundedHitstunAnimation(9)
        Unknown11032('90d00300c0f2fcffe0930400c0f2fcff')
        Unknown23027()
        SLOT_54 = 0

        def upon_11():
            clearUponHandler(11)
            SLOT_54 = (SLOT_54 + 1)
            physicsXImpulse(80000)
            physicsYImpulse(0)
            sendToLabel(1)

        def upon_3():
            SLOT_51 = 0
            SLOT_13 = 0
            if SLOT_2:
                Unknown48('030000000200000033000000160000000200000017000000')
                Unknown47('01000000020000001700000002000000330000000200000033000000')
                Unknown47('03000000020000003300000000000000f6ffffff020000000d000000')
                if (SLOT_13 <= 0):
                    SLOT_13 = 0
                Unknown47('03000000020000001300000000000000320000000200000034000000')
                SLOT_12 = (SLOT_12 + SLOT_52)

        def upon_STATE_END():
            Unknown1019(25)
    sprite('ph400_11', 3)	# 1-3
    tag_voice(1, 'bph200_0', 'bph200_1', 'bph200_2', '')
    physicsXImpulse(1100)
    ModifyVar_(8, 2, 4, 0, 2)
    sprite('ph400_01', 3)	# 4-6
    Unknown1019(150)
    sprite('ph400_02', 2)	# 7-8	 **attackbox here**
    Unknown1019(150)
    SFX_0('000_airdash_0')
    sprite('ph400_03', 2)	# 9-10	 **attackbox here**
    GFX_0('pheff_400Air', -1)
    Unknown38(5, 1)
    SFX_0('015_blaze_0')
    Unknown1019(400)
    sprite('ph400_04', 2)	# 11-12	 **attackbox here**
    Unknown2037(1)
    Unknown1019(800)
    sprite('ph400_02', 3)	# 13-15	 **attackbox here**
    if (SLOT_13 < 0):
        Unknown23029(5, 4003, 0)
    if (SLOT_13 > 0):
        Unknown23029(5, 4004, 0)
    Unknown1019(50)
    Unknown3038(1)
    RefreshMultihit()
    Unknown23029(5, 4001, 0)
    sprite('ph400_03', 3)	# 16-18	 **attackbox here**
    Unknown2037(0)
    Unknown1019(25)
    sprite('ph400_04', 3)	# 19-21	 **attackbox here**
    Unknown1019(25)
    label(1)
    sprite('ph400_05', 3)	# 22-24	 **attackbox here**
    clearUponHandler(11)
    clearUponHandler(3)
    Unknown2006()
    Unknown2016(-1)
    Unknown1019(25)
    sprite('ph400_05', 3)	# 25-27	 **attackbox here**
    Unknown23029(5, 4005, 0)
    sprite('ph400_05', 1)	# 28-28	 **attackbox here**
    Unknown3038(0)
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    Unknown1043()
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1250)
    AirPushbackX(30000)
    AirPushbackY(-30000)
    PushbackX(12000)
    Unknown9310(10)
    Unknown9017(1)
    Unknown11032('e0930400206cfbffe0930400206cfbff')
    if SLOT_54:
        Unknown11032('ffffffffffffffffffffffffffffffff')

    def upon_11():
        clearUponHandler(11)
        SLOT_54 = (SLOT_54 + 1)
    SFX_0('016_explode_0')
    SFX_0('016_explode_1')
    sprite('ph400_05', 2)	# 29-30	 **attackbox here**
    StartMultihit()
    sprite('ph400_06', 5)	# 31-35
    Recovery()
    Unknown1019(50)
    sprite('ph400_12', 4)	# 36-39
    Unknown1019(50)
    sprite('ph400_13', 4)	# 40-43
    Unknown1019(50)
    sprite('ph400_14', 4)	# 44-47
    Unknown1019(50)
    sprite('ph400_15', 1)	# 48-48
    Unknown1019(50)
    if (not SLOT_54):
        sendToLabel(2)
    sprite('ph400_15', 3)	# 49-51
    ExitState()
    label(2)
    sprite('ph400_15', 3)	# 52-54
    sprite('ph020_05', 3)	# 55-57
    sprite('ph020_06', 3)	# 58-60
    label(3)
    sprite('ph020_07', 4)	# 61-64
    sprite('ph020_08', 4)	# 65-68
    gotoLabel(3)
    ExitState()

@State
def AirAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()
        Unknown2004(1, 0)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 4103):
                pass
    sprite('ph020_02', 3)	# 1-3
    sprite('ph401_01', 3)	# 4-6
    tag_voice(1, 'bph201_0', 'bph201_1', 'bph201_2', '')
    Unknown1084(1)
    GFX_0('Eff_DriveMagicCircle', -1)
    sprite('ph401_02', 6)	# 7-12
    GFX_0('Eff_401', -1)
    Unknown23029(1, 4102, 0)
    SFX_0('016_explode_1')
    SFX_3('phse_02')
    sprite('ph401_03', 3)	# 13-15
    physicsXImpulse(2500)
    physicsYImpulse(15000)
    Unknown1043()
    SFX_0('004_swing_grap_1_2')
    sprite('ph401_04', 3)	# 16-18
    sprite('ph401_05', 3)	# 19-21
    Recovery()
    sprite('ph020_03', 3)	# 22-24
    sprite('ph020_04', 3)	# 25-27
    sprite('ph020_05', 2)	# 28-29
    sprite('ph020_05', 1)	# 30-30
    if SLOT_2:
        sendToLabel(2)
    sprite('ph020_06', 3)	# 31-33
    label(0)
    sprite('ph020_07', 4)	# 34-37
    sprite('ph020_08', 4)	# 38-41
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 42-44
    sprite('ph024_01', 3)	# 45-47
    sprite('ph024_02', 3)	# 48-50
    sprite('ph024_03', 3)	# 51-53
    sprite('ph024_04', 3)	# 54-56
    ExitState()
    label(2)
    sprite('ph020_06', 3)	# 57-59
    ExitState()

@State
def AirAssaultEx():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23027()

        def upon_43():
            if (SLOT_48 == 4405):
                clearUponHandler(43)
                Recovery()
                setInvincible(0)
    sprite('ph320_00', 3)	# 1-3
    sprite('ph320_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    tag_voice(1, 'bph307_0', 'bph156_1', '', '')
    Unknown23125('')
    Unknown2058(-5000)
    setInvincible(1)
    Unknown22019('0000000000000000000000000100000000000000')
    GFX_0('BurstDDMaster', -1)
    Unknown38(5, 1)
    Unknown23029(5, 4404, 0)
    sprite('ph320_02', 3)	# 7-9	 **attackbox here**
    sprite('ph321_00', 3)	# 10-12	 **attackbox here**
    sprite('ph321_01', 3)	# 13-15	 **attackbox here**
    sprite('ph321_02', 6)	# 16-21	 **attackbox here**
    ScreenShake(25000, 10000)
    sprite('ph321_03', 6)	# 22-27	 **attackbox here**
    sprite('ph321_04', 5)	# 28-32	 **attackbox here**
    sprite('ph321_05', 5)	# 33-37	 **attackbox here**
    sprite('ph321_04', 5)	# 38-42	 **attackbox here**
    Unknown1018()
    Unknown1023()
    YAccel(50)
    Unknown1043()
    sprite('ph321_05', 5)	# 43-47	 **attackbox here**
    sprite('ph321_06', 3)	# 48-50
    sprite('ph321_07', 3)	# 51-53
    sprite('ph321_08', 3)	# 54-56
    sprite('ph020_05', 3)	# 57-59
    sprite('ph020_06', 3)	# 60-62
    label(0)
    sprite('ph020_07', 4)	# 63-66
    sprite('ph020_08', 4)	# 67-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 71-73
    sprite('ph024_01', 3)	# 74-76
    sprite('ph024_02', 3)	# 77-79
    sprite('ph024_03', 3)	# 80-82
    sprite('ph024_04', 3)	# 83-85
    ExitState()

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 4309):
                Unknown2064(1)
    sprite('ph430_00', 4)	# 1-4
    Unknown30080('')
    Unknown2036(52, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    setInvincible(1)
    sprite('ph430_01', 4)	# 5-8
    sprite('ph430_02', 20)	# 9-28
    GFX_0('Eff_430_cap', 0)
    sprite('ph430_03', 8)	# 29-36
    sprite('ph430_04', 8)	# 37-44
    sprite('ph430_05', 13)	# 45-57
    tag_voice(1, 'bph250_0', 'bph250_1', '', '')
    sprite('ph430_06', 6)	# 58-63
    sprite('ph430_07', 6)	# 64-69
    sprite('ph430_08', 2)	# 70-71
    sprite('ph430_09', 2)	# 72-73
    GFX_0('UltimateShotAtk1st', -1)
    Unknown1045(-20000)
    sprite('ph430_10', 3)	# 74-76
    setInvincible(0)
    sprite('ph430_11', 3)	# 77-79
    sprite('ph430_12', 3)	# 80-82
    sprite('ph430_10', 3)	# 83-85
    sprite('ph430_11', 3)	# 86-88
    sprite('ph430_12', 3)	# 89-91
    sprite('ph430_10', 3)	# 92-94
    sprite('ph430_11', 3)	# 95-97
    sprite('ph430_12', 3)	# 98-100
    sprite('ph430_10', 3)	# 101-103
    sprite('ph430_11', 3)	# 104-106
    sprite('ph430_12', 3)	# 107-109
    sprite('ph430_13', 4)	# 110-113
    sprite('ph430_14', 4)	# 114-117
    sprite('ph430_15', 4)	# 118-121
    sprite('ph430_16', 4)	# 122-125
    sprite('ph430_17', 4)	# 126-129
    tag_voice(0, 'bph251_0', 'bph251_1', '', '')
    sprite('ph430_18', 3)	# 130-132
    GFX_0('UltimateShotAtk2nd', -1)
    Unknown1045(-40000)
    sprite('ph430_19', 3)	# 133-135
    sprite('ph430_20', 3)	# 136-138
    sprite('ph430_21', 3)	# 139-141
    sprite('ph430_19', 3)	# 142-144
    sprite('ph430_20', 3)	# 145-147
    sprite('ph430_21', 3)	# 148-150
    sprite('ph430_19', 3)	# 151-153
    sprite('ph430_20', 3)	# 154-156
    sprite('ph430_21', 3)	# 157-159
    sprite('ph430_19', 3)	# 160-162
    sprite('ph430_20', 3)	# 163-165
    sprite('ph430_21', 3)	# 166-168
    sprite('ph430_19', 3)	# 169-171
    sprite('ph430_20', 3)	# 172-174
    sprite('ph430_21', 3)	# 175-177
    sprite('ph430_19', 3)	# 178-180
    sprite('ph430_20', 3)	# 181-183
    sprite('ph430_21', 3)	# 184-186
    sprite('ph430_19', 3)	# 187-189
    sprite('ph430_20', 3)	# 190-192
    sprite('ph430_21', 3)	# 193-195
    sprite('ph430_22', 6)	# 196-201
    sprite('ph430_23', 6)	# 202-207
    sprite('ph430_24', 6)	# 208-213
    sprite('ph430_25', 6)	# 214-219
    GFX_0('Eff_430_capFire', -1)
    sprite('ph430_26', 6)	# 220-225
    sprite('ph430_27', 6)	# 226-231

@State
def UltimateShotSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown2037(0)
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 4309):
                Unknown2064(1)
            if (SLOT_48 == 4305):
                Unknown2037(1)
    sprite('ph430_00', 4)	# 1-4
    Unknown30080('')
    Unknown2036(52, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    setInvincible(1)
    sprite('ph430_01', 4)	# 5-8
    sprite('ph430_02', 20)	# 9-28
    GFX_0('Eff_430_cap', 0)
    sprite('ph430_03', 8)	# 29-36
    sprite('ph430_04', 8)	# 37-44
    sprite('ph430_05', 13)	# 45-57
    tag_voice(1, 'bph250_0', 'bph250_1', '', '')
    sprite('ph430_06', 6)	# 58-63
    sprite('ph430_07', 6)	# 64-69
    sprite('ph430_08', 2)	# 70-71
    sprite('ph430_09', 2)	# 72-73
    GFX_0('UltimateShotAtk1st', -1)
    Unknown23029(1, 4304, 0)
    Unknown1045(-20000)
    sprite('ph430_10', 3)	# 74-76
    setInvincible(0)
    sprite('ph430_11', 3)	# 77-79
    sprite('ph430_12', 3)	# 80-82
    sprite('ph430_10', 3)	# 83-85
    sprite('ph430_11', 3)	# 86-88
    sprite('ph430_12', 3)	# 89-91
    sprite('ph430_10', 3)	# 92-94
    sprite('ph430_11', 3)	# 95-97
    sprite('ph430_12', 3)	# 98-100
    sprite('ph430_10', 3)	# 101-103
    sprite('ph430_11', 3)	# 104-106
    sprite('ph430_12', 3)	# 107-109
    sprite('ph430_13', 4)	# 110-113
    sprite('ph430_14', 4)	# 114-117
    sprite('ph430_15', 4)	# 118-121
    sprite('ph430_16', 4)	# 122-125
    sprite('ph430_17', 4)	# 126-129
    tag_voice(0, 'bph251_0', 'bph251_1', '', '')
    sprite('ph430_18', 3)	# 130-132
    GFX_0('UltimateShotAtk2nd', -1)
    Unknown23029(1, 4304, 0)
    Unknown1045(-40000)
    sprite('ph430_19', 3)	# 133-135
    sprite('ph430_20', 3)	# 136-138
    sprite('ph430_21', 3)	# 139-141
    sprite('ph430_19', 3)	# 142-144
    sprite('ph430_20', 3)	# 145-147
    sprite('ph430_21', 3)	# 148-150
    sprite('ph430_19', 3)	# 151-153
    sprite('ph430_20', 3)	# 154-156
    sprite('ph430_21', 3)	# 157-159
    sprite('ph430_19', 3)	# 160-162
    sprite('ph430_20', 3)	# 163-165
    sprite('ph430_21', 3)	# 166-168
    sprite('ph430_19', 3)	# 169-171
    sprite('ph430_20', 3)	# 172-174
    sprite('ph430_21', 3)	# 175-177
    sprite('ph430_19', 3)	# 178-180
    sprite('ph430_20', 3)	# 181-183
    sprite('ph430_21', 3)	# 184-186
    sprite('ph430_19', 3)	# 187-189
    sprite('ph430_20', 3)	# 190-192
    sprite('ph430_21', 2)	# 193-194
    sprite('keep', 1)	# 195-195
    if SLOT_2:
        sendToLabel(0)
    sprite('ph430_22', 6)	# 196-201
    sprite('ph430_23', 6)	# 202-207
    sprite('ph430_24', 6)	# 208-213
    sprite('ph430_25', 6)	# 214-219
    GFX_0('Eff_430_capFire', -1)
    sprite('ph430_26', 6)	# 220-225
    sprite('ph430_27', 6)	# 226-231
    ExitState()
    label(0)
    sprite('ph430_19', 3)	# 232-234
    sprite('ph430_20', 3)	# 235-237
    sprite('ph430_28', 5)	# 238-242
    sprite('ph430_29', 5)	# 243-247
    sprite('ph430_30', 5)	# 248-252
    Unknown2036(50, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('ph430_31', 5)	# 253-257
    GFX_0('UltimateShotHinokagutsuchi', -1)
    sprite('ph430_32', 5)	# 258-262
    sprite('ph430_33', 5)	# 263-267
    sprite('ph430_31', 5)	# 268-272
    sprite('ph430_32', 5)	# 273-277
    sprite('ph430_33', 5)	# 278-282
    sprite('ph430_31', 5)	# 283-287
    sprite('ph430_32', 5)	# 288-292
    sprite('ph430_33', 5)	# 293-297
    sprite('ph430_34', 3)	# 298-300
    sprite('ph430_35', 3)	# 301-303
    Unknown1045(-10000)
    tag_voice(0, 'bph252_0', 'bph252_1', '', '')
    sprite('ph430_36', 3)	# 304-306
    sprite('ph430_37', 3)	# 307-309
    sprite('ph430_38', 3)	# 310-312
    sprite('ph430_36', 3)	# 313-315
    sprite('ph430_37', 3)	# 316-318
    sprite('ph430_38', 3)	# 319-321
    sprite('ph430_36', 3)	# 322-324
    sprite('ph430_37', 3)	# 325-327
    sprite('ph430_38', 3)	# 328-330
    sprite('ph430_36', 3)	# 331-333
    sprite('ph430_37', 3)	# 334-336
    sprite('ph430_38', 3)	# 337-339
    sprite('ph430_36', 3)	# 340-342
    sprite('ph430_37', 3)	# 343-345
    sprite('ph430_38', 3)	# 346-348
    sprite('ph430_36', 3)	# 349-351
    sprite('ph430_37', 3)	# 352-354
    sprite('ph430_38', 3)	# 355-357
    sprite('ph430_36', 3)	# 358-360
    sprite('ph430_37', 3)	# 361-363
    sprite('ph430_38', 3)	# 364-366
    sprite('ph430_36', 3)	# 367-369
    sprite('ph430_37', 3)	# 370-372
    sprite('ph430_38', 3)	# 373-375
    sprite('ph430_39', 6)	# 376-381
    sprite('ph430_40', 6)	# 382-387
    sprite('ph430_41', 6)	# 388-393
    sprite('ph430_25', 6)	# 394-399
    GFX_0('Eff_430_capFire', -1)
    sprite('ph430_26', 6)	# 400-405
    sprite('ph430_27', 6)	# 406-411

@State
def UltimateLock():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(2)
        Damage(100)
        Unknown11091(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(70)
        Unknown9142(60)
        Unknown30048(1)
        Unknown11064(1)
        Unknown9017(1)
        Unknown13024(0)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown2037(0)

        def upon_78():
            clearUponHandler(78)
            Unknown2037(1)
            PushbackX(0)
            Hitstop(0)
            callSubroutine('ActiveMagicAllDelete')
            sendToLabel(1)
        SLOT_5 = 0
    sprite('ph432_00', 4)	# 1-4
    Unknown30080('')
    Unknown2036(15, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bph255_0', 'bph255_1', '', '')
    setInvincible(1)
    sprite('ph432_01', 4)	# 5-8
    sprite('ph432_02', 4)	# 9-12
    sprite('ph432_03', 4)	# 13-16
    sprite('ph432_04', 3)	# 17-19
    sprite('ph432_05', 3)	# 20-22
    sprite('ph432_06', 3)	# 23-25
    sprite('ph432_07', 3)	# 26-28
    SFX_0('003_swing_grap_0_2')
    sprite('ph432_08ex2', 5)	# 29-33	 **attackbox here**
    ScreenShake(0, 10000)
    GFX_0('Eff_432_AtkFire', -1)
    SFX_0('016_explode_0')
    sprite('ph432_09', 2)	# 34-35
    clearUponHandler(78)
    setInvincible(0)
    Unknown13024(1)
    sprite('ph432_09', 3)	# 36-38
    sprite('ph432_10', 3)	# 39-41
    sprite('ph432_11', 3)	# 42-44
    sprite('ph432_09', 3)	# 45-47
    sprite('ph432_10', 3)	# 48-50
    sprite('ph432_11', 3)	# 51-53
    sprite('ph432_12', 6)	# 54-59
    sprite('ph432_13', 6)	# 60-65
    sprite('ph432_14', 6)	# 66-71
    ExitState()
    label(1)
    sprite('ph432_08', 2)	# 72-73	 **attackbox here**
    sprite('ph432_08', 2)	# 74-75	 **attackbox here**
    clearUponHandler(78)
    RefreshMultihit()
    Damage(0)
    Hitstop(10)
    AttackP2(100)
    Unknown9215()
    Unknown11023(1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    if (not SLOT_2):
        setInvincible(0)
    Unknown11069('UltimateLock_Atk1stLv1')
    if (SLOT_31 >= 5000):
        Unknown11069('UltimateLock_Atk1stLv2')
    if (SLOT_31 >= 10000):
        Unknown11069('UltimateLock_Atk1stLv3')
    if (not SLOT_2):
        Unknown13024(1)
    sprite('ph432_09', 3)	# 76-78
    sprite('ph432_10', 3)	# 79-81
    sprite('ph432_11', 3)	# 82-84
    sprite('ph432_12', 4)	# 85-88
    sprite('ph432_13', 4)	# 89-92
    sprite('ph432_14', 3)	# 93-95
    sprite('keep', 1)	# 96-96
    enterState('UltimateLock_1stSelect')
    ExitState()

@State
def UltimateLockSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(2)
        Damage(100)
        Unknown11091(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(70)
        Unknown9142(60)
        Unknown30048(1)
        Unknown11064(1)
        Unknown9017(1)
        Unknown13024(0)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown2037(0)

        def upon_78():
            clearUponHandler(78)
            Unknown2037(1)
            PushbackX(0)
            Hitstop(0)
            callSubroutine('ActiveMagicAllDelete')
            sendToLabel(1)
        SLOT_5 = 1
    sprite('ph432_00', 4)	# 1-4
    Unknown30080('')
    Unknown2036(15, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'bph255_0', 'bph255_1', '', '')
    setInvincible(1)
    sprite('ph432_01', 4)	# 5-8
    sprite('ph432_02', 4)	# 9-12
    sprite('ph432_03', 4)	# 13-16
    sprite('ph432_04', 3)	# 17-19
    sprite('ph432_05', 3)	# 20-22
    sprite('ph432_06', 3)	# 23-25
    sprite('ph432_07', 3)	# 26-28
    SFX_0('003_swing_grap_0_2')
    sprite('ph432_08ex2', 5)	# 29-33	 **attackbox here**
    ScreenShake(0, 10000)
    GFX_0('Eff_432_AtkFire', -1)
    SFX_0('016_explode_0')
    sprite('ph432_09', 2)	# 34-35
    clearUponHandler(78)
    setInvincible(0)
    Unknown13024(1)
    sprite('ph432_09', 3)	# 36-38
    sprite('ph432_10', 3)	# 39-41
    sprite('ph432_11', 3)	# 42-44
    sprite('ph432_09', 3)	# 45-47
    sprite('ph432_10', 3)	# 48-50
    sprite('ph432_11', 3)	# 51-53
    sprite('ph432_12', 6)	# 54-59
    sprite('ph432_13', 6)	# 60-65
    sprite('ph432_14', 6)	# 66-71
    ExitState()
    label(1)
    sprite('ph432_08', 2)	# 72-73	 **attackbox here**
    sprite('ph432_08', 2)	# 74-75	 **attackbox here**
    clearUponHandler(78)
    RefreshMultihit()
    Damage(0)
    Hitstop(10)
    AttackP2(100)
    Unknown9215()
    Unknown11023(1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    if (not SLOT_2):
        setInvincible(0)
    Unknown11069('UltimateLock_Atk1stLv1')
    if (SLOT_31 >= 5000):
        Unknown11069('UltimateLock_Atk1stLv2')
    if (SLOT_31 >= 10000):
        Unknown11069('UltimateLock_Atk1stLv3')
    if (not SLOT_2):
        Unknown13024(1)
    sprite('ph432_09', 3)	# 76-78
    sprite('ph432_10', 3)	# 79-81
    sprite('ph432_11', 3)	# 82-84
    sprite('ph432_12', 4)	# 85-88
    sprite('ph432_13', 4)	# 89-92
    sprite('ph432_14', 3)	# 93-95
    sprite('keep', 1)	# 96-96
    enterState('UltimateLock_1stSelect')
    ExitState()

@State
def UltimateLock_1stSelect():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
    sprite('ph000_00', 10)	# 1-10
    if (SLOT_31 > 0):
        if (SLOT_31 >= 5000):
            if (SLOT_31 >= 10000):
                enterState('UltimateLock_1stLv3')
            else:
                enterState('UltimateLock_1stLv2')
        else:
            enterState('UltimateLock_1stLv1')
    else:
        enterState('UltimateLock_1stLv1')

@State
def UltimateLock_1stLv1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        setInvincible(1)
        Unknown2006()
        Unknown13024(0)
    sprite('ph000_00', 6)	# 1-6
    sprite('ph214_00', 4)	# 7-10
    sprite('ph214_01', 4)	# 11-14
    sprite('ph214_02', 4)	# 15-18	 **attackbox here**
    GFX_0('UltimateLock_Atk1stLv1', -1)
    SFX_0('024_getset_b')
    sprite('ph214_03', 6)	# 19-24	 **attackbox here**
    sprite('ph214_04', 6)	# 25-30
    sprite('ph214_05', 6)	# 31-36
    sprite('keep', 1)	# 37-37
    enterState('UltimateLock_2ndSelect')

@State
def UltimateLock_1stLv2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        setInvincible(1)
        Unknown2006()
        Unknown13024(0)
    sprite('ph202_00', 5)	# 1-5
    sprite('ph202_01', 5)	# 6-10
    sprite('ph202_02', 5)	# 11-15
    sprite('ph202_03', 3)	# 16-18	 **attackbox here**
    GFX_0('UltimateLock_Atk1stLv2', -1)
    SFX_0('024_getset_b')
    SFX_0('016_explode_0')
    SFX_0('016_explode_1')
    sprite('ph202_04', 6)	# 19-24
    sprite('ph202_05', 6)	# 25-30
    sprite('ph202_06', 6)	# 31-36
    sprite('ph202_07', 6)	# 37-42
    sprite('keep', 1)	# 43-43
    enterState('UltimateLock_2ndSelect')

@State
def UltimateLock_1stLv3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        setInvincible(1)
        Unknown2006()
        Unknown13024(0)
    sprite('ph216_00', 3)	# 1-3
    sprite('ph216_01', 8)	# 4-11
    sprite('ph216_02', 3)	# 12-14
    sprite('ph216_03', 7)	# 15-21	 **attackbox here**
    GFX_0('UltimateLock_Atk1stLv3', -1)
    SFX_0('024_getset_b')
    SFX_3('phse_02')
    SFX_3('phse_02')
    sprite('ph216_04', 7)	# 22-28	 **attackbox here**
    sprite('ph216_05', 5)	# 29-33
    sprite('ph216_06', 5)	# 34-38
    sprite('keep', 1)	# 39-39
    enterState('UltimateLock_2ndSelect')

@State
def UltimateLock_2ndSelect():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
    sprite('ph000_00', 10)	# 1-10
    tag_voice(0, 'bph256_0', 'bph256_1', '', '')
    if (SLOT_31 > 0):
        if (SLOT_31 >= 5000):
            if (SLOT_31 >= 10000):
                enterState('UltimateLock_2ndLv3')
            else:
                enterState('UltimateLock_2ndLv2')
        else:
            enterState('UltimateLock_2ndLv1')
    else:
        enterState('UltimateLock_2ndLv1')

@State
def UltimateLock_2ndLv1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('ph203_00', 4)	# 1-4
    sprite('ph203_01', 4)	# 5-8
    physicsYImpulse(10000)
    sprite('ph203_02', 4)	# 9-12
    YAccel(50)
    sprite('ph203_03', 4)	# 13-16
    YAccel(50)
    sprite('ph203_01', 4)	# 17-20
    YAccel(0)
    sprite('ph203_02', 4)	# 21-24
    sprite('ph203_04', 5)	# 25-29
    sprite('ph203_05', 5)	# 30-34
    sprite('ph203_06', 5)	# 35-39
    sprite('ph203_07', 5)	# 40-44
    physicsXImpulse(-12500)
    GFX_0('UltimateLock_Atk2ndLv2', -1)
    if SLOT_5:
        Unknown23029(1, 4321, 0)
    callSubroutine('MagicPointReset')
    sprite('ph203_08', 5)	# 45-49
    Unknown1019(50)
    sprite('ph203_09', 6)	# 50-55
    Unknown1019(50)
    sprite('ph203_10', 6)	# 56-61
    Unknown1019(50)
    sprite('ph203_08', 6)	# 62-67
    Unknown1019(0)
    sprite('ph203_09', 6)	# 68-73
    sprite('ph203_10', 4)	# 74-77
    sprite('ph203_11', 3)	# 78-80
    sprite('ph203_15', 3)	# 81-83
    sprite('ph203_16', 3)	# 84-86
    sprite('keep', 1)	# 87-87
    physicsYImpulse(15000)
    Unknown1043()
    if SLOT_5:
        enterState('UltimateLockSP_AddAttack')
    sprite('ph020_05', 3)	# 88-90
    Unknown13024(1)
    sprite('ph020_06', 3)	# 91-93
    label(0)
    sprite('ph020_07', 4)	# 94-97
    sprite('ph020_08', 4)	# 98-101
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 102-104
    sprite('ph024_01', 3)	# 105-107
    sprite('ph024_02', 3)	# 108-110
    sprite('ph024_03', 3)	# 111-113
    sprite('ph024_04', 3)	# 114-116

@State
def UltimateLock_2ndLv2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('ph204_00', 4)	# 1-4
    sprite('ph204_01', 4)	# 5-8
    sprite('ph204_02', 4)	# 9-12
    physicsYImpulse(10000)
    sprite('ph204_03', 4)	# 13-16
    YAccel(50)
    sprite('ph204_04', 4)	# 17-20
    YAccel(50)
    sprite('ph204_02', 4)	# 21-24
    YAccel(0)
    sprite('ph204_03', 4)	# 25-28
    sprite('ph204_04', 4)	# 29-32
    sprite('ph204_05', 4)	# 33-36
    sprite('ph204_06', 4)	# 37-40
    sprite('ph204_07', 4)	# 41-44
    physicsXImpulse(-15000)
    GFX_0('UltimateLock_Atk2ndLv3', -1)
    if SLOT_5:
        Unknown23029(1, 4321, 0)
    callSubroutine('MagicPointReset')
    sprite('ph204_08', 5)	# 45-49
    Unknown1019(50)
    sprite('ph204_09', 6)	# 50-55
    Unknown1019(50)
    sprite('ph204_10', 6)	# 56-61
    Unknown1019(50)
    sprite('ph204_08', 6)	# 62-67
    Unknown1019(0)
    sprite('ph204_08', 6)	# 68-73
    sprite('ph204_09', 6)	# 74-79
    sprite('ph204_10', 6)	# 80-85
    sprite('ph204_08', 6)	# 86-91
    sprite('ph204_09', 6)	# 92-97
    sprite('ph204_10', 6)	# 98-103
    sprite('ph204_08', 2)	# 104-105
    sprite('ph204_11', 3)	# 106-108
    sprite('ph204_12', 3)	# 109-111
    sprite('ph204_15', 3)	# 112-114
    sprite('ph204_16', 3)	# 115-117
    sprite('keep', 1)	# 118-118
    physicsYImpulse(15000)
    Unknown1043()
    if SLOT_5:
        enterState('UltimateLockSP_AddAttack')
    sprite('ph020_05', 3)	# 119-121
    Unknown13024(1)
    sprite('ph020_06', 3)	# 122-124
    label(0)
    sprite('ph020_07', 4)	# 125-128
    sprite('ph020_08', 4)	# 129-132
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 133-135
    sprite('ph024_01', 3)	# 136-138
    sprite('ph024_02', 3)	# 139-141
    sprite('ph024_03', 3)	# 142-144
    sprite('ph024_04', 3)	# 145-147

@State
def UltimateLock_2ndLv3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('ph205_00', 5)	# 1-5
    sprite('ph205_01', 5)	# 6-10
    sprite('ph205_02', 4)	# 11-14
    physicsYImpulse(10000)
    sprite('ph205_03', 4)	# 15-18
    YAccel(50)
    sprite('ph205_04', 4)	# 19-22
    YAccel(50)
    sprite('ph205_02', 4)	# 23-26
    YAccel(0)
    sprite('ph205_03', 4)	# 27-30
    sprite('ph205_04', 4)	# 31-34
    sprite('ph205_05', 5)	# 35-39
    sprite('ph205_06', 5)	# 40-44
    physicsXImpulse(-20000)
    GFX_0('UltimateLock_Atk2ndLv4', -1)
    if SLOT_5:
        Unknown23029(1, 4321, 0)
    callSubroutine('MagicPointReset')
    sprite('ph205_07', 5)	# 45-49
    Unknown1019(50)
    sprite('ph205_08', 6)	# 50-55
    Unknown1019(50)
    sprite('ph205_09', 6)	# 56-61
    Unknown1019(50)
    sprite('ph205_07', 6)	# 62-67
    Unknown1019(0)
    sprite('ph205_08', 6)	# 68-73
    sprite('ph205_09', 6)	# 74-79
    sprite('ph205_07', 6)	# 80-85
    sprite('ph205_08', 6)	# 86-91
    sprite('ph205_09', 6)	# 92-97
    sprite('ph205_07', 6)	# 98-103
    sprite('ph205_08', 6)	# 104-109
    sprite('ph205_09', 6)	# 110-115
    sprite('ph205_07', 6)	# 116-121
    sprite('ph205_10', 4)	# 122-125
    sprite('ph205_11', 3)	# 126-128
    sprite('ph205_15', 3)	# 129-131
    sprite('ph205_16', 3)	# 132-134
    sprite('keep', 1)	# 135-135
    physicsYImpulse(15000)
    Unknown1043()
    if SLOT_5:
        enterState('UltimateLockSP_AddAttack')
    sprite('ph020_05', 3)	# 136-138
    Unknown13024(1)
    sprite('ph020_06', 3)	# 139-141
    label(0)
    sprite('ph020_07', 4)	# 142-145
    sprite('ph020_08', 4)	# 146-149
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 150-152
    sprite('ph024_01', 3)	# 153-155
    sprite('ph024_02', 3)	# 156-158
    sprite('ph024_03', 3)	# 159-161
    sprite('ph024_04', 3)	# 162-164

@State
def UltimateLockSP_AddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown2003(1)
        Unknown13024(0)
        setInvincible(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('ph320_00', 6)	# 1-6
    sprite('ph320_01', 6)	# 7-12
    Unknown2036(25, -1, 0)
    sprite('ph320_02', 6)	# 13-18	 **attackbox here**
    sprite('ph321_00', 3)	# 19-21	 **attackbox here**
    sprite('ph321_01', 3)	# 22-24	 **attackbox here**
    sprite('ph321_02', 3)	# 25-27	 **attackbox here**
    sprite('ph321_00', 10)	# 28-37	 **attackbox here**
    tag_voice(0, 'bph257_0', 'bph257_1', '', '')
    sprite('ph321_02', 8)	# 38-45	 **attackbox here**
    sprite('ph321_03', 6)	# 46-51	 **attackbox here**
    GFX_0('UltimateLock_AtkSPAdd', -1)
    sprite('ph321_04', 6)	# 52-57	 **attackbox here**
    sprite('ph321_05', 10)	# 58-67	 **attackbox here**
    sprite('ph321_05', 10)	# 68-77	 **attackbox here**
    Unknown13024(1)
    sprite('ph321_06', 6)	# 78-83
    sprite('ph321_07', 6)	# 84-89
    sprite('ph321_08', 6)	# 90-95
    sprite('ph020_05', 3)	# 96-98
    Unknown1043()
    sprite('ph020_06', 3)	# 99-101
    label(0)
    sprite('ph020_07', 4)	# 102-105
    sprite('ph020_08', 4)	# 106-109
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ph024_00', 3)	# 110-112
    sprite('ph024_01', 3)	# 113-115
    sprite('ph024_02', 3)	# 116-118
    sprite('ph024_03', 3)	# 119-121
    sprite('ph024_04', 3)	# 122-124

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()

        def upon_43():
            if (SLOT_48 == 4501):
                enterState('AstralHeatExe')
        setInvincible(1)
    sprite('ph450_00', 3)	# 1-3
    sprite('ph450_01', 3)	# 4-6
    tag_voice(1, 'bph290_0', 'bph290_1', '', '')
    sprite('ph450_02', 3)	# 7-9
    Unknown2036(54, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_PH_AH', -1)
    sprite('ph450_02', 5)	# 10-14
    sprite('ph450_03', 5)	# 15-19
    sprite('ph450_04', 5)	# 20-24
    sprite('ph450_02', 5)	# 25-29
    sprite('ph450_03', 5)	# 30-34
    sprite('ph450_04', 5)	# 35-39
    sprite('ph450_02', 5)	# 40-44
    sprite('ph450_03', 5)	# 45-49
    sprite('ph450_04', 5)	# 50-54
    sprite('ph450_05', 5)	# 55-59
    sprite('ph450_06', 5)	# 60-64
    sprite('ph450_07', 5)	# 65-69
    sprite('ph450_08', 5)	# 70-74
    sprite('ph450_09', 3)	# 75-77
    GFX_0('AstralHeatAtk', -1)
    GFX_0('Eff_450_EyeBurning', 0)
    sprite('ph450_10', 3)	# 78-80
    sprite('ph450_11', 3)	# 81-83
    sprite('ph450_09', 3)	# 84-86
    sprite('ph450_10', 3)	# 87-89
    sprite('ph450_11', 3)	# 90-92
    sprite('ph450_09', 3)	# 93-95
    sprite('ph450_10', 3)	# 96-98
    sprite('ph450_11', 3)	# 99-101
    sprite('ph450_12', 6)	# 102-107
    Unknown26('Eff_450_EyeBurning')
    setInvincible(0)
    sprite('ph450_13', 6)	# 108-113
    sprite('ph450_14', 6)	# 114-119
    tag_voice(0, 'bph294_0', 'bph294_1', '', '')
    sprite('ph450_15', 6)	# 120-125
    sprite('ph450_16', 6)	# 126-131
    sprite('ph450_17', 6)	# 132-137
    sprite('ph450_18', 6)	# 138-143

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown36(22)
        Unknown23169(1)
        Unknown35()
        Unknown23084(1)
        Unknown23088(1, 1)
        Unknown23157(1)
        GFX_0('Eff_450_EyeBurning', 0)
        callSubroutine('ActiveMagicAllDelete')
        setInvincible(1)
    sprite('ph450_09', 3)	# 1-3
    sprite('ph450_10', 3)	# 4-6
    sprite('ph450_11', 3)	# 7-9
    sprite('ph450_09', 3)	# 10-12
    GFX_0('AstralHeat_Hinokagutsuchi', -1)
    sprite('ph450_10', 3)	# 13-15
    sprite('ph450_11', 3)	# 16-18
    sprite('ph450_09', 3)	# 19-21
    sprite('ph450_10', 3)	# 22-24
    sprite('ph450_11', 3)	# 25-27
    sprite('ph450_09', 3)	# 28-30
    sprite('ph450_10', 3)	# 31-33
    sprite('ph450_11', 3)	# 34-36
    tag_voice(0, 'bph291_0', 'bph291_1', '', '')
    sprite('ph450_09', 3)	# 37-39
    sprite('ph450_10', 3)	# 40-42
    sprite('ph450_11', 3)	# 43-45
    sprite('ph450_09', 3)	# 46-48
    sprite('ph450_10', 3)	# 49-51
    sprite('ph450_11', 3)	# 52-54
    sprite('ph450_09', 3)	# 55-57
    sprite('ph450_10', 3)	# 58-60
    sprite('ph450_11', 3)	# 61-63
    sprite('ph450_09', 3)	# 64-66
    sprite('ph450_10', 3)	# 67-69
    sprite('ph450_11', 3)	# 70-72
    GFX_0('AstralHeatAtk2nd', -1)
    sprite('ph450_09', 3)	# 73-75
    sprite('ph450_10', 3)	# 76-78
    sprite('ph450_11', 3)	# 79-81
    sprite('ph450_09', 3)	# 82-84
    sprite('ph450_10', 3)	# 85-87
    sprite('ph450_09', 3)	# 88-90
    sprite('ph450_10', 3)	# 91-93
    sprite('ph450_11', 3)	# 94-96
    sprite('ph450_09', 3)	# 97-99
    sprite('ph450_10', 3)	# 100-102
    sprite('ph450_11', 3)	# 103-105
    sprite('ph450_09', 3)	# 106-108
    sprite('ph450_10', 3)	# 109-111
    sprite('ph450_11', 3)	# 112-114
    sprite('ph450_09', 3)	# 115-117
    sprite('ph450_10', 3)	# 118-120
    sprite('ph450_09', 3)	# 121-123
    sprite('ph450_10', 3)	# 124-126
    sprite('ph450_11', 3)	# 127-129
    sprite('ph450_09', 3)	# 130-132
    sprite('ph450_10', 3)	# 133-135
    sprite('ph450_09', 3)	# 136-138
    sprite('ph450_10', 3)	# 139-141
    sprite('ph450_11', 3)	# 142-144
    sprite('ph450_09', 3)	# 145-147
    sprite('ph450_10', 3)	# 148-150
    sprite('ph450_11', 3)	# 151-153
    sprite('ph450_09', 3)	# 154-156
    sprite('ph450_10', 3)	# 157-159
    sprite('ph450_11', 3)	# 160-162
    sprite('ph450_09', 3)	# 163-165
    sprite('ph450_10', 3)	# 166-168
    sprite('ph450_09', 3)	# 169-171
    sprite('ph450_10', 3)	# 172-174
    sprite('ph450_11', 3)	# 175-177
    sprite('ph450_09', 3)	# 178-180
    sprite('ph450_10', 3)	# 181-183
    sprite('ph450_11', 20)	# 184-203
    GFX_0('Eff_450_Terepo', -1)
    SFX_0('000_airdash_0')
    Unknown26('Eff_450_EyeBurning')
    Unknown3038(1)
    sprite('ph450_11', 20)	# 204-223
    Unknown3038(1)
    GFX_0('phAst_ShaSha00', -1)
    sprite('null', 4)	# 224-227
    Unknown23024(3)
    Unknown20010(0, -10000000, 10000000)
    teleportRelativeY(800000)
    Unknown1000(800000)
    Unknown1096(500)
    Unknown2007()
    Unknown36(22)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown3038(1)
    Unknown35()
    GFX_0('AstralHeat_Camera', -1)
    sprite('ph450_19', 3)	# 228-230
    sprite('ph450_20', 3)	# 231-233
    sprite('ph450_21', 3)	# 234-236
    sprite('ph450_19', 3)	# 237-239
    sprite('ph450_20', 3)	# 240-242
    sprite('ph450_21', 3)	# 243-245
    tag_voice(0, 'bph292_0', 'bph292_1', '', '')
    sprite('ph450_19', 3)	# 246-248
    sprite('ph450_20', 3)	# 249-251
    sprite('ph450_21', 3)	# 252-254
    sprite('ph450_19', 3)	# 255-257
    sprite('ph450_20', 3)	# 258-260
    sprite('ph450_21', 3)	# 261-263
    sprite('ph450_19', 3)	# 264-266
    Unknown3038(0)
    GFX_1('phef450_terepo', -1)
    GFX_0('Eff_450_circle', -1)
    Unknown36(1)
    Unknown1007(-150000)
    Unknown1097(-600)
    Unknown35()
    SFX_0('000_airdash_0')
    sprite('ph450_20', 3)	# 267-269
    sprite('ph450_21', 3)	# 270-272
    sprite('ph450_19', 3)	# 273-275
    sprite('ph450_20', 3)	# 276-278
    sprite('ph450_21', 3)	# 279-281
    sprite('ph450_19', 3)	# 282-284
    sprite('ph450_20', 3)	# 285-287
    sprite('ph450_21', 3)	# 288-290
    SFX_0('022_magiccircle_b')
    sprite('ph450_19', 3)	# 291-293
    sprite('ph450_20', 3)	# 294-296
    sprite('ph450_21', 3)	# 297-299
    SFX_3('phse_04')
    sprite('ph450_19', 3)	# 300-302
    sprite('ph450_20', 3)	# 303-305
    sprite('ph450_21', 3)	# 306-308
    sprite('ph450_19', 3)	# 309-311
    sprite('ph450_20', 3)	# 312-314
    sprite('ph450_21', 3)	# 315-317
    sprite('ph450_19', 3)	# 318-320
    sprite('ph450_20', 3)	# 321-323
    sprite('ph450_21', 3)	# 324-326
    sprite('ph450_19', 3)	# 327-329
    sprite('ph450_20', 3)	# 330-332
    sprite('ph450_21', 3)	# 333-335
    sprite('ph450_19', 3)	# 336-338
    sprite('ph450_20', 3)	# 339-341
    sprite('ph450_21', 3)	# 342-344
    sprite('ph450_19', 3)	# 345-347
    sprite('ph450_20', 3)	# 348-350
    sprite('ph450_21', 3)	# 351-353
    sprite('ph450_19', 3)	# 354-356
    sprite('ph450_20', 3)	# 357-359
    sprite('ph450_21', 3)	# 360-362
    sprite('ph450_19', 3)	# 363-365
    sprite('ph450_20', 3)	# 366-368
    sprite('ph450_21', 3)	# 369-371
    sprite('ph450_19', 3)	# 372-374
    sprite('ph450_20', 3)	# 375-377
    sprite('ph450_21', 3)	# 378-380
    sprite('ph450_22', 3)	# 381-383
    tag_voice(0, 'bph293_0', 'bph293_1', '', '')
    sprite('ph450_23', 3)	# 384-386
    sprite('ph450_24', 3)	# 387-389
    sprite('ph450_25', 3)	# 390-392
    sprite('ph450_23', 3)	# 393-395
    sprite('ph450_24', 3)	# 396-398
    sprite('ph450_25', 3)	# 399-401
    sprite('ph450_23', 3)	# 402-404
    sprite('ph450_24', 3)	# 405-407
    sprite('ph450_23', 3)	# 408-410
    sprite('ph450_24', 3)	# 411-413
    sprite('ph450_25', 3)	# 414-416
    sprite('ph450_23', 3)	# 417-419
    SFX_3('phse_10')
    sprite('ph450_24', 3)	# 420-422
    sprite('ph450_25', 3)	# 423-425
    sprite('ph450_23', 3)	# 426-428
    sprite('ph450_24', 3)	# 429-431
    sprite('ph450_25', 3)	# 432-434
    sprite('ph450_23', 3)	# 435-437
    sprite('ph450_24', 3)	# 438-440
    sprite('ph450_25', 3)	# 441-443
    sprite('ph450_23', 3)	# 444-446
    sprite('ph450_24', 3)	# 447-449
    sprite('ph450_25', 3)	# 450-452
    sprite('ph450_23', 3)	# 453-455
    sprite('ph450_24', 3)	# 456-458
    sprite('ph450_25', 3)	# 459-461
    sprite('ph450_23', 3)	# 462-464
    sprite('ph450_24', 3)	# 465-467
    sprite('ph450_25', 3)	# 468-470
    sprite('ph450_23', 3)	# 471-473
    sprite('ph450_24', 3)	# 474-476
    sprite('ph450_25', 3)	# 477-479
    sprite('ph450_23', 3)	# 480-482
    sprite('ph450_24', 3)	# 483-485
    Unknown23024(2)
    sprite('ph450_23', 3)	# 486-488
    sprite('ph450_24', 3)	# 489-491
    sprite('ph450_25', 3)	# 492-494
    Unknown3038(1)
    sprite('ph450_23', 3)	# 495-497
    sprite('ph450_24', 3)	# 498-500
    sprite('ph450_25', 3)	# 501-503
    sprite('ph450_23', 3)	# 504-506
    sprite('ph450_24', 3)	# 507-509
    sprite('ph450_25', 3)	# 510-512
    sprite('ph450_23', 3)	# 513-515
    sprite('ph450_24', 3)	# 516-518
    sprite('ph450_25', 130)	# 519-648
    GFX_0('AstralHeatEff_MeteoMato', -1)
    sprite('ph450_23', 3)	# 649-651
    GFX_0('AstralHeatLastAtk', -1)
    Unknown36(22)
    Unknown3001(0)
    Unknown35()
    sprite('ph450_24', 3)	# 652-654
    sprite('ph450_25', 3)	# 655-657
    sprite('ph450_23', 3)	# 658-660
    sprite('ph450_24', 3)	# 661-663
    sprite('ph450_25', 150)	# 664-813
    Unknown1000(0)
    teleportRelativeY(0)
    sprite('ph450_23', 3)	# 814-816
    Unknown18010()
    Unknown21011(120)
    Unknown23018(1)
    sprite('ph450_24', 3)	# 817-819
    sprite('ph450_25', 180)	# 820-999
    Unknown18008()
    sprite('ph450_25', 32767)	# 1000-33766
    Unknown23018(1)

@Subroutine
def MouthTableInit():
    Unknown18011('bph000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph500', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph503', 12643, 13153, 25392, 12341, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph520', 12643, 12641, 25395, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph524', 12643, 13153, 25392, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph525', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph402_0', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph403_0', 12643, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph403_1', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph600', 12643, 12641, 25392, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph600bjb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph600brc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 14129, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph600pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph600rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph601pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph601pyo', 12643, 14177, 12643, 24885, 25397, 24885, 25397, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 13617, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph601uca', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph601ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph700bjb', 12643, 12641, 25394, 24887, 25399, 13618, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph700pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph700uca', 12643, 12897, 25392, 12340, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph700ugo', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph701brc', 12643, 12641, 25394, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph701pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bph701pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('62706800000000000000000000000000626a62000000000000000000000000006268610000000000000000000000000062707400000000000000000000000000'):
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
    PartnerChar('bjb')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('brc')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pag')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(170)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(20)
    sprite('ph600_00', 6)	# 2-7
    sprite('ph600_01', 6)	# 8-13
    sprite('ph600_02', 6)	# 14-19
    sprite('ph600_00', 6)	# 20-25
    GFX_0('phef_600_Fire', -1)
    GFX_0('phef_600_bg', -1)
    Unknown3025(-12648448, 30)
    sprite('ph600_01', 6)	# 26-31
    sprite('ph600_02', 6)	# 32-37
    GFX_0('phef_600_Fire2', -1)
    SFX_3('phse_02')
    SFX_0('016_explode_0')
    SFX_0('015_blaze_2')
    sprite('ph600_00', 6)	# 38-43
    GFX_0('phef_600_FireWall', -1)
    sprite('ph600_01', 6)	# 44-49
    sprite('ph600_02', 6)	# 50-55
    sprite('ph600_00', 6)	# 56-61
    Unknown3004(-8)
    sprite('ph600_01', 6)	# 62-67
    sprite('ph600_02', 6)	# 68-73
    sprite('ph600_03', 6)	# 74-79
    Unknown3001(0)
    Unknown3004(8)
    sprite('ph600_04', 6)	# 80-85
    sprite('ph600_03', 6)	# 86-91
    sprite('ph600_04', 6)	# 92-97
    sprite('ph600_03', 6)	# 98-103
    sprite('ph600_04', 6)	# 104-109
    sprite('ph600_03', 6)	# 110-115
    sprite('ph600_04', 6)	# 116-121
    Unknown3025(-1, 20)
    sprite('ph600_03', 6)	# 122-127
    sprite('ph600_04', 6)	# 128-133
    sprite('ph600_05', 6)	# 134-139
    GFX_1('phef_340mant2', 0)
    GFX_1('phef_340mant2', 1)
    sprite('ph600_06', 6)	# 140-145
    GFX_1('phef_340mant2', 0)
    GFX_1('phef_340mant2', 1)
    sprite('ph600_07', 6)	# 146-151
    GFX_1('phef_340mant', 0)
    GFX_1('phef_340mant', 1)
    sprite('ph600_08', 6)	# 152-157
    GFX_1('phef_340mant', 0)
    GFX_1('phef_340mant', 1)
    sprite('ph600_09', 6)	# 158-163
    GFX_1('phef_340mant', 0)
    sprite('ph600_10', 6)	# 164-169
    GFX_1('phef_340mant', 0)
    sprite('ph600_11', 6)	# 170-175
    GFX_1('phef_340mant', 0)
    sprite('ph600_12', 6)	# 176-181
    GFX_1('phef_340mant', 0)
    sprite('ph600_13', 6)	# 182-187
    GFX_1('phef_340mant', 0)
    sprite('ph600_14', 6)	# 188-193
    GFX_1('phef_340mant', 0)
    GFX_0('phef_600_Hat', -1)
    GFX_0('phef_600_HatFire', -1)
    SFX_0('015_blaze_0')
    sprite('ph600_15', 6)	# 194-199
    GFX_1('phef_340mant', 0)
    sprite('ph600_16', 6)	# 200-205
    Unknown7006('bph500', 100, 896036962, 12592, 0, 0, 100, 896036962, 13360, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ph600_17', 6)	# 206-211
    label(1)
    sprite('ph600_15', 6)	# 212-217
    sprite('ph600_16', 6)	# 218-223
    sprite('ph600_17', 6)	# 224-229
    sprite('ph600_15', 6)	# 230-235
    sprite('ph600_16', 6)	# 236-241
    sprite('ph600_17', 6)	# 242-247
    sprite('ph600_15', 6)	# 248-253
    sprite('ph600_16', 6)	# 254-259
    sprite('ph600_17', 6)	# 260-265
    sprite('ph600_15', 6)	# 266-271
    sprite('ph600_16', 6)	# 272-277
    sprite('ph600_17', 6)	# 278-283
    if SLOT_97:
        _gotolabel(1)
    sprite('ph600_18', 6)	# 284-289
    Unknown23018(1)
    label(2)
    sprite('ph000_00', 7)	# 290-296
    sprite('ph000_01', 7)	# 297-303
    sprite('ph000_02', 7)	# 304-310
    sprite('ph000_03', 7)	# 311-317
    sprite('ph000_04', 7)	# 318-324
    sprite('ph000_05', 7)	# 325-331
    sprite('ph000_06', 7)	# 332-338
    sprite('ph000_07', 7)	# 339-345
    sprite('ph000_08', 7)	# 346-352
    sprite('ph000_09', 7)	# 353-359
    gotoLabel(2)
    ExitState()
    label(10)
    sprite('ph601_00ex01', 6)	# 360-365	 **attackbox here**
    GFX_0('Entry_HinoEff', -1)
    Unknown21012('456e7472795f48696e6f4566660000000000000000000000000000000000000021000000')
    sprite('ph601_00ex02', 6)	# 366-371	 **attackbox here**
    sprite('ph601_00ex03', 6)	# 372-377	 **attackbox here**
    sprite('ph601_00ex04', 6)	# 378-383	 **attackbox here**
    sprite('ph601_00ex05', 6)	# 384-389	 **attackbox here**
    sprite('ph601_00ex06', 6)	# 390-395	 **attackbox here**
    sprite('ph601_00ex07', 6)	# 396-401	 **attackbox here**
    sprite('ph601_00ex08', 6)	# 402-407	 **attackbox here**
    sprite('ph601_00ex09', 6)	# 408-413	 **attackbox here**
    sprite('ph601_00ex10', 6)	# 414-419	 **attackbox here**
    sprite('ph601_00ex01', 6)	# 420-425	 **attackbox here**
    sprite('ph601_00ex02', 6)	# 426-431	 **attackbox here**
    sprite('ph601_00ex03', 6)	# 432-437	 **attackbox here**
    sprite('ph601_00ex04', 6)	# 438-443	 **attackbox here**
    sprite('ph601_00ex05', 6)	# 444-449	 **attackbox here**
    sprite('ph601_00ex06', 6)	# 450-455	 **attackbox here**
    sprite('ph601_00ex07', 6)	# 456-461	 **attackbox here**
    sprite('ph601_00ex08', 6)	# 462-467	 **attackbox here**
    sprite('ph601_00ex09', 6)	# 468-473	 **attackbox here**
    sprite('ph601_00ex10', 6)	# 474-479	 **attackbox here**
    sprite('ph601_00', 15)	# 480-494
    sendToLabelUpon(2, 13)
    GFX_0('Entry_Hinokagutsuchi', -1)
    Unknown21012('456e7472795f48696e6f4566660000000000000000000000000000000000000020000000')
    physicsYImpulse(4000)
    setGravity(250)
    SFX_3('phse_02')
    SFX_0('016_explode_0')
    SFX_0('015_blaze_2')
    label(12)
    sprite('ph601_01', 6)	# 495-500
    sprite('ph601_02', 6)	# 501-506
    sprite('ph601_03', 6)	# 507-512
    gotoLabel(12)
    label(13)
    sprite('ph601_04', 8)	# 513-520
    sprite('ph601_05', 8)	# 521-528
    sprite('ph601_06', 8)	# 529-536
    Unknown21011(60)
    label(14)
    sprite('ph000_00', 7)	# 537-543
    sprite('ph000_01', 7)	# 544-550
    sprite('ph000_02', 7)	# 551-557
    sprite('ph000_03', 7)	# 558-564
    sprite('ph000_04', 7)	# 565-571
    sprite('ph000_05', 7)	# 572-578
    sprite('ph000_06', 7)	# 579-585
    sprite('ph000_07', 7)	# 586-592
    sprite('ph000_08', 7)	# 593-599
    sprite('ph000_09', 7)	# 600-606
    gotoLabel(14)
    ExitState()
    label(20)
    sprite('ph602_00', 30)	# 607-636
    sprite('ph602_00', 1)	# 637-637
    Unknown7006('bph502', 100, 896036962, 13104, 0, 0, 100, 896036962, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    label(21)
    sprite('ph602_00', 1)	# 638-638
    if SLOT_97:
        _gotolabel(21)
    sprite('ph602_00', 6)	# 639-644
    sprite('ph602_00', 6)	# 645-650
    sprite('ph602_00', 6)	# 651-656
    GFX_1('phef_602hinoko', 100)
    sprite('ph602_00', 6)	# 657-662
    GFX_0('phef_600_bg', -1)
    GFX_0('phef_602_Fire', -1)
    sprite('ph602_00', 6)	# 663-668
    sprite('ph602_00', 6)	# 669-674
    GFX_0('phef_602_Fire2', -1)
    SFX_3('phse_02')
    SFX_0('016_explode_0')
    SFX_0('015_blaze_2')
    sprite('ph602_01', 6)	# 675-680
    GFX_0('phef_602_FireWall', -1)
    sprite('ph602_02', 6)	# 681-686
    sprite('ph602_03', 6)	# 687-692
    sprite('ph602_04', 6)	# 693-698
    sprite('ph602_02', 6)	# 699-704
    sprite('ph602_03', 6)	# 705-710
    sprite('ph602_04', 6)	# 711-716
    sprite('ph602_02', 6)	# 717-722
    sprite('ph602_03', 6)	# 723-728
    sprite('ph602_04', 6)	# 729-734
    sprite('ph602_02', 6)	# 735-740
    Unknown3025(-3657166, 18)
    sprite('ph602_03', 6)	# 741-746
    sprite('ph602_04', 6)	# 747-752
    sprite('ph602_02', 6)	# 753-758
    sprite('ph602_03', 6)	# 759-764
    sprite('ph602_04', 6)	# 765-770
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(4)
    sprite('ph602_05', 7)	# 771-777
    Unknown3025(-1, 24)
    GFX_1('phef_602add', 100)
    sprite('ph331_10', 7)	# 778-784
    Unknown3029(0)
    Unknown23018(1)
    label(22)
    sprite('ph000_00', 7)	# 785-791
    sprite('ph000_01', 7)	# 792-798
    sprite('ph000_02', 7)	# 799-805
    sprite('ph000_03', 7)	# 806-812
    sprite('ph000_04', 7)	# 813-819
    sprite('ph000_05', 7)	# 820-826
    sprite('ph000_06', 7)	# 827-833
    sprite('ph000_07', 7)	# 834-840
    sprite('ph000_08', 7)	# 841-847
    sprite('ph000_09', 7)	# 848-854
    gotoLabel(22)
    ExitState()
    label(30)
    sprite('ph000_00', 1)	# 855-855
    SFX_1('bph600')
    label(31)
    sprite('ph000_00', 7)	# 856-862
    sprite('ph000_01', 7)	# 863-869
    sprite('ph000_02', 7)	# 870-876
    sprite('ph000_03', 7)	# 877-883
    sprite('ph000_04', 7)	# 884-890
    sprite('ph000_05', 7)	# 891-897
    sprite('ph000_06', 7)	# 898-904
    sprite('ph000_07', 7)	# 905-911
    sprite('ph000_08', 7)	# 912-918
    sprite('ph000_09', 7)	# 919-925
    gotoLabel(31)
    label(991)
    sprite('ph000_00', 1)	# 926-926
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ph000_00', 7)	# 927-933
    sprite('ph000_01', 7)	# 934-940
    sprite('ph000_02', 7)	# 941-947
    sprite('ph000_03', 7)	# 948-954
    sprite('ph000_04', 7)	# 955-961
    sprite('ph000_05', 7)	# 962-968
    sprite('ph000_06', 7)	# 969-975
    sprite('ph000_07', 7)	# 976-982
    sprite('ph000_08', 7)	# 983-989
    sprite('ph000_09', 7)	# 990-996
    gotoLabel(992)
    ExitState()
    label(100)
    sprite('ph638_00', 1)	# 997-997
    Unknown1000(-1375000)
    Unknown2005()
    Unknown2019(-500)
    SFX_1('bph600bjb')
    label(101)
    sprite('ph638_00', 9)	# 998-1006
    sprite('ph638_01', 9)	# 1007-1015
    sprite('ph638_02', 9)	# 1016-1024
    sprite('ph638_01', 9)	# 1025-1033
    if SLOT_97:
        _gotolabel(101)
    sprite('ph638_00', 9)	# 1034-1042
    sprite('ph638_01', 9)	# 1043-1051
    sprite('ph638_02', 9)	# 1052-1060
    sprite('ph638_01', 9)	# 1061-1069
    Unknown21007(24, 40)
    Unknown21011(270)
    label(102)
    sprite('ph638_00', 9)	# 1070-1078
    sprite('ph638_01', 9)	# 1079-1087
    sprite('ph638_02', 9)	# 1088-1096
    sprite('ph638_01', 9)	# 1097-1105
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('ph601_00ex01', 6)	# 1106-1111	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('Entry_HinoEff', -1)
    Unknown21012('456e7472795f48696e6f4566660000000000000000000000000000000000000021000000')
    sprite('ph601_00ex02', 6)	# 1112-1117	 **attackbox here**
    sprite('ph601_00ex03', 6)	# 1118-1123	 **attackbox here**
    SFX_1('bph600brc')
    sprite('ph601_00ex04', 6)	# 1124-1129	 **attackbox here**
    sprite('ph601_00ex05', 6)	# 1130-1135	 **attackbox here**
    sprite('ph601_00ex06', 6)	# 1136-1141	 **attackbox here**
    sprite('ph601_00ex07', 6)	# 1142-1147	 **attackbox here**
    sprite('ph601_00ex08', 6)	# 1148-1153	 **attackbox here**
    sprite('ph601_00ex09', 6)	# 1154-1159	 **attackbox here**
    sprite('ph601_00ex10', 6)	# 1160-1165	 **attackbox here**
    sprite('ph601_00ex01', 6)	# 1166-1171	 **attackbox here**
    sprite('ph601_00ex02', 6)	# 1172-1177	 **attackbox here**
    sprite('ph601_00ex03', 6)	# 1178-1183	 **attackbox here**
    sprite('ph601_00ex04', 6)	# 1184-1189	 **attackbox here**
    sprite('ph601_00ex05', 6)	# 1190-1195	 **attackbox here**
    sprite('ph601_00ex06', 6)	# 1196-1201	 **attackbox here**
    sprite('ph601_00ex07', 6)	# 1202-1207	 **attackbox here**
    sprite('ph601_00ex08', 6)	# 1208-1213	 **attackbox here**
    sprite('ph601_00ex09', 6)	# 1214-1219	 **attackbox here**
    sprite('ph601_00ex10', 6)	# 1220-1225	 **attackbox here**
    sprite('ph601_00', 15)	# 1226-1240
    sendToLabelUpon(2, 112)
    GFX_0('Entry_Hinokagutsuchi', -1)
    Unknown21012('456e7472795f48696e6f4566660000000000000000000000000000000000000020000000')
    physicsYImpulse(4000)
    setGravity(250)
    SFX_3('phse_02')
    SFX_0('016_explode_0')
    SFX_0('015_blaze_2')
    label(111)
    sprite('ph601_01', 6)	# 1241-1246
    sprite('ph601_02', 6)	# 1247-1252
    sprite('ph601_03', 6)	# 1253-1258
    gotoLabel(111)
    label(112)
    sprite('ph601_04', 8)	# 1259-1266
    sprite('ph601_05', 8)	# 1267-1274
    sprite('ph601_06', 8)	# 1275-1282
    label(113)
    sprite('ph000_00', 7)	# 1283-1289
    sprite('ph000_01', 7)	# 1290-1296
    sprite('ph000_02', 7)	# 1297-1303
    sprite('ph000_03', 7)	# 1304-1310
    sprite('ph000_04', 7)	# 1311-1317
    sprite('ph000_05', 7)	# 1318-1324
    sprite('ph000_06', 7)	# 1325-1331
    sprite('ph000_07', 7)	# 1332-1338
    sprite('ph000_08', 7)	# 1339-1345
    sprite('ph000_09', 7)	# 1346-1352
    if SLOT_97:
        _gotolabel(113)
    sprite('ph000_00', 1)	# 1353-1353
    Unknown21007(24, 40)
    Unknown21011(300)
    label(114)
    sprite('ph000_00', 7)	# 1354-1360
    sprite('ph000_01', 7)	# 1361-1367
    sprite('ph000_02', 7)	# 1368-1374
    sprite('ph000_03', 7)	# 1375-1381
    sprite('ph000_04', 7)	# 1382-1388
    sprite('ph000_05', 7)	# 1389-1395
    sprite('ph000_06', 7)	# 1396-1402
    sprite('ph000_07', 7)	# 1403-1409
    sprite('ph000_08', 7)	# 1410-1416
    sprite('ph000_09', 7)	# 1417-1423
    gotoLabel(114)
    ExitState()
    label(120)
    sprite('ph602_00', 30)	# 1424-1453
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ph602_00', 1)	# 1454-1454
    SFX_1('bph600pyu')
    label(121)
    sprite('ph602_00', 1)	# 1455-1455
    if SLOT_97:
        _gotolabel(121)
    sprite('ph602_00', 6)	# 1456-1461
    sprite('ph602_00', 6)	# 1462-1467
    sprite('ph602_00', 6)	# 1468-1473
    GFX_1('phef_602hinoko', 100)
    sprite('ph602_00', 6)	# 1474-1479
    GFX_0('phef_600_bg', -1)
    GFX_0('phef_602_Fire', -1)
    sprite('ph602_00', 6)	# 1480-1485
    sprite('ph602_00', 6)	# 1486-1491
    GFX_0('phef_602_Fire2', -1)
    SFX_3('phse_02')
    SFX_0('016_explode_0')
    SFX_0('015_blaze_2')
    sprite('ph602_01', 6)	# 1492-1497
    GFX_0('phef_602_FireWall', -1)
    sprite('ph602_02', 6)	# 1498-1503
    sprite('ph602_03', 6)	# 1504-1509
    sprite('ph602_04', 6)	# 1510-1515
    sprite('ph602_02', 6)	# 1516-1521
    sprite('ph602_03', 6)	# 1522-1527
    sprite('ph602_04', 6)	# 1528-1533
    sprite('ph602_02', 6)	# 1534-1539
    sprite('ph602_03', 6)	# 1540-1545
    sprite('ph602_04', 6)	# 1546-1551
    sprite('ph602_02', 6)	# 1552-1557
    Unknown3025(-3657166, 18)
    sprite('ph602_03', 6)	# 1558-1563
    sprite('ph602_04', 6)	# 1564-1569
    sprite('ph602_02', 6)	# 1570-1575
    sprite('ph602_03', 6)	# 1576-1581
    sprite('ph602_04', 6)	# 1582-1587
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(4)
    sprite('ph602_05', 7)	# 1588-1594
    Unknown3025(-1, 24)
    GFX_1('phef_602add', 100)
    sprite('ph331_10', 7)	# 1595-1601
    Unknown3029(0)
    Unknown21007(24, 40)
    Unknown21011(270)
    label(122)
    sprite('ph000_00', 7)	# 1602-1608
    sprite('ph000_01', 7)	# 1609-1615
    sprite('ph000_02', 7)	# 1616-1622
    sprite('ph000_03', 7)	# 1623-1629
    sprite('ph000_04', 7)	# 1630-1636
    sprite('ph000_05', 7)	# 1637-1643
    sprite('ph000_06', 7)	# 1644-1650
    sprite('ph000_07', 7)	# 1651-1657
    sprite('ph000_08', 7)	# 1658-1664
    sprite('ph000_09', 7)	# 1665-1671
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('ph602_00', 30)	# 1672-1701
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ph602_00', 1)	# 1702-1702
    SFX_1('bph600rwi')
    label(131)
    sprite('ph602_00', 1)	# 1703-1703
    if SLOT_97:
        _gotolabel(131)
    sprite('ph602_00', 6)	# 1704-1709
    sprite('ph602_00', 6)	# 1710-1715
    sprite('ph602_00', 6)	# 1716-1721
    GFX_1('phef_602hinoko', 100)
    sprite('ph602_00', 6)	# 1722-1727
    GFX_0('phef_600_bg', -1)
    GFX_0('phef_602_Fire', -1)
    sprite('ph602_00', 6)	# 1728-1733
    sprite('ph602_00', 6)	# 1734-1739
    GFX_0('phef_602_Fire2', -1)
    SFX_3('phse_02')
    SFX_0('016_explode_0')
    SFX_0('015_blaze_2')
    sprite('ph602_01', 6)	# 1740-1745
    GFX_0('phef_602_FireWall', -1)
    sprite('ph602_02', 6)	# 1746-1751
    sprite('ph602_03', 6)	# 1752-1757
    sprite('ph602_04', 6)	# 1758-1763
    sprite('ph602_02', 6)	# 1764-1769
    sprite('ph602_03', 6)	# 1770-1775
    sprite('ph602_04', 6)	# 1776-1781
    sprite('ph602_02', 6)	# 1782-1787
    sprite('ph602_03', 6)	# 1788-1793
    sprite('ph602_04', 6)	# 1794-1799
    sprite('ph602_02', 6)	# 1800-1805
    Unknown3025(-3657166, 18)
    sprite('ph602_03', 6)	# 1806-1811
    sprite('ph602_04', 6)	# 1812-1817
    sprite('ph602_02', 6)	# 1818-1823
    sprite('ph602_03', 6)	# 1824-1829
    sprite('ph602_04', 6)	# 1830-1835
    Unknown3029(1)
    Unknown3070(2)
    Unknown3071(4)
    sprite('ph602_05', 7)	# 1836-1842
    Unknown3025(-1, 24)
    GFX_1('phef_602add', 100)
    sprite('ph331_10', 7)	# 1843-1849
    Unknown3029(0)
    Unknown21007(24, 40)
    Unknown21011(200)
    label(132)
    sprite('ph000_00', 7)	# 1850-1856
    sprite('ph000_01', 7)	# 1857-1863
    sprite('ph000_02', 7)	# 1864-1870
    sprite('ph000_03', 7)	# 1871-1877
    sprite('ph000_04', 7)	# 1878-1884
    sprite('ph000_05', 7)	# 1885-1891
    sprite('ph000_06', 7)	# 1892-1898
    sprite('ph000_07', 7)	# 1899-1905
    sprite('ph000_08', 7)	# 1906-1912
    sprite('ph000_09', 7)	# 1913-1919
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('ph000_00', 1)	# 1920-1920
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ph000_00', 7)	# 1921-1927
    sprite('ph000_01', 7)	# 1928-1934
    sprite('ph000_02', 7)	# 1935-1941
    sprite('ph000_03', 7)	# 1942-1948
    sprite('ph000_04', 7)	# 1949-1955
    sprite('ph000_05', 7)	# 1956-1962
    sprite('ph000_06', 7)	# 1963-1969
    sprite('ph000_07', 7)	# 1970-1976
    sprite('ph000_08', 7)	# 1977-1983
    sprite('ph000_09', 7)	# 1984-1990
    gotoLabel(141)
    label(142)
    sprite('ph615_00', 5)	# 1991-1995
    sprite('ph615_01', 5)	# 1996-2000
    sprite('ph615_02', 5)	# 2001-2005
    SFX_1('bph601pag')
    sprite('ph615_03', 5)	# 2006-2010
    sprite('ph615_04', 5)	# 2011-2015
    label(143)
    sprite('ph615_05', 5)	# 2016-2020
    sprite('ph615_06', 5)	# 2021-2025
    sprite('ph615_07', 5)	# 2026-2030
    sprite('ph615_08', 5)	# 2031-2035
    sprite('ph615_09', 5)	# 2036-2040
    sprite('ph615_10', 5)	# 2041-2045
    if SLOT_97:
        _gotolabel(143)
    sprite('ph615_05', 6)	# 2046-2051
    sprite('ph615_04', 6)	# 2052-2057
    sprite('ph615_03', 6)	# 2058-2063
    sprite('ph615_02', 6)	# 2064-2069
    sprite('ph615_01', 6)	# 2070-2075
    sprite('ph615_00', 6)	# 2076-2081
    Unknown23018(1)
    label(144)
    sprite('ph000_00', 7)	# 2082-2088
    sprite('ph000_01', 7)	# 2089-2095
    sprite('ph000_02', 7)	# 2096-2102
    sprite('ph000_03', 7)	# 2103-2109
    sprite('ph000_04', 7)	# 2110-2116
    sprite('ph000_05', 7)	# 2117-2123
    sprite('ph000_06', 7)	# 2124-2130
    sprite('ph000_07', 7)	# 2131-2137
    sprite('ph000_08', 7)	# 2138-2144
    sprite('ph000_09', 7)	# 2145-2151
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('ph000_00', 1)	# 2152-2152
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ph000_00', 7)	# 2153-2159
    sprite('ph000_01', 7)	# 2160-2166
    sprite('ph000_02', 7)	# 2167-2173
    sprite('ph000_03', 7)	# 2174-2180
    sprite('ph000_04', 7)	# 2181-2187
    sprite('ph000_05', 7)	# 2188-2194
    sprite('ph000_06', 7)	# 2195-2201
    sprite('ph000_07', 7)	# 2202-2208
    sprite('ph000_08', 7)	# 2209-2215
    sprite('ph000_09', 7)	# 2216-2222
    gotoLabel(151)
    label(152)
    sprite('ph615_00', 5)	# 2223-2227
    sprite('ph615_01', 5)	# 2228-2232
    sprite('ph615_02', 5)	# 2233-2237
    SFX_1('bph601pyo')
    sprite('ph615_03', 5)	# 2238-2242
    sprite('ph615_04', 5)	# 2243-2247
    label(153)
    sprite('ph615_05', 5)	# 2248-2252
    sprite('ph615_06', 5)	# 2253-2257
    sprite('ph615_07', 5)	# 2258-2262
    sprite('ph615_08', 5)	# 2263-2267
    sprite('ph615_09', 5)	# 2268-2272
    sprite('ph615_10', 5)	# 2273-2277
    if SLOT_97:
        _gotolabel(153)
    sprite('ph615_05', 6)	# 2278-2283
    sprite('ph615_04', 6)	# 2284-2289
    sprite('ph615_03', 6)	# 2290-2295
    sprite('ph615_02', 6)	# 2296-2301
    sprite('ph615_01', 6)	# 2302-2307
    sprite('ph615_00', 6)	# 2308-2313
    Unknown23018(1)
    label(154)
    sprite('ph000_00', 7)	# 2314-2320
    sprite('ph000_01', 7)	# 2321-2327
    sprite('ph000_02', 7)	# 2328-2334
    sprite('ph000_03', 7)	# 2335-2341
    sprite('ph000_04', 7)	# 2342-2348
    sprite('ph000_05', 7)	# 2349-2355
    sprite('ph000_06', 7)	# 2356-2362
    sprite('ph000_07', 7)	# 2363-2369
    sprite('ph000_08', 7)	# 2370-2376
    sprite('ph000_09', 7)	# 2377-2383
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('ph000_00', 1)	# 2384-2384
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ph000_00', 7)	# 2385-2391
    sprite('ph000_01', 7)	# 2392-2398
    sprite('ph000_02', 7)	# 2399-2405
    sprite('ph000_03', 7)	# 2406-2412
    sprite('ph000_04', 7)	# 2413-2419
    sprite('ph000_05', 7)	# 2420-2426
    sprite('ph000_06', 7)	# 2427-2433
    sprite('ph000_07', 7)	# 2434-2440
    sprite('ph000_08', 7)	# 2441-2447
    sprite('ph000_09', 7)	# 2448-2454
    gotoLabel(161)
    label(162)
    sprite('ph615_00', 5)	# 2455-2459
    sprite('ph615_01', 5)	# 2460-2464
    sprite('ph615_02', 5)	# 2465-2469
    SFX_1('bph601uca')
    sprite('ph615_03', 5)	# 2470-2474
    sprite('ph615_04', 5)	# 2475-2479
    label(163)
    sprite('ph615_05', 5)	# 2480-2484
    sprite('ph615_06', 5)	# 2485-2489
    sprite('ph615_07', 5)	# 2490-2494
    sprite('ph615_08', 5)	# 2495-2499
    sprite('ph615_09', 5)	# 2500-2504
    sprite('ph615_10', 5)	# 2505-2509
    if SLOT_97:
        _gotolabel(163)
    sprite('ph615_05', 6)	# 2510-2515
    sprite('ph615_04', 6)	# 2516-2521
    sprite('ph615_03', 6)	# 2522-2527
    sprite('ph615_02', 6)	# 2528-2533
    sprite('ph615_01', 6)	# 2534-2539
    sprite('ph615_00', 6)	# 2540-2545
    Unknown23018(1)
    label(164)
    sprite('ph000_00', 7)	# 2546-2552
    sprite('ph000_01', 7)	# 2553-2559
    sprite('ph000_02', 7)	# 2560-2566
    sprite('ph000_03', 7)	# 2567-2573
    sprite('ph000_04', 7)	# 2574-2580
    sprite('ph000_05', 7)	# 2581-2587
    sprite('ph000_06', 7)	# 2588-2594
    sprite('ph000_07', 7)	# 2595-2601
    sprite('ph000_08', 7)	# 2602-2608
    sprite('ph000_09', 7)	# 2609-2615
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('ph000_00', 1)	# 2616-2616
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ph000_00', 7)	# 2617-2623
    sprite('ph000_01', 7)	# 2624-2630
    sprite('ph000_02', 7)	# 2631-2637
    sprite('ph000_03', 7)	# 2638-2644
    sprite('ph000_04', 7)	# 2645-2651
    sprite('ph000_05', 7)	# 2652-2658
    sprite('ph000_06', 7)	# 2659-2665
    sprite('ph000_07', 7)	# 2666-2672
    sprite('ph000_08', 7)	# 2673-2679
    sprite('ph000_09', 7)	# 2680-2686
    gotoLabel(171)
    label(172)
    sprite('ph615_00', 5)	# 2687-2691
    sprite('ph615_01', 5)	# 2692-2696
    sprite('ph615_02', 5)	# 2697-2701
    SFX_1('bph601ugo')
    sprite('ph615_03', 5)	# 2702-2706
    sprite('ph615_04', 5)	# 2707-2711
    label(173)
    sprite('ph615_05', 5)	# 2712-2716
    sprite('ph615_06', 5)	# 2717-2721
    sprite('ph615_07', 5)	# 2722-2726
    sprite('ph615_08', 5)	# 2727-2731
    sprite('ph615_09', 5)	# 2732-2736
    sprite('ph615_10', 5)	# 2737-2741
    if SLOT_97:
        _gotolabel(173)
    sprite('ph615_05', 6)	# 2742-2747
    sprite('ph615_04', 6)	# 2748-2753
    sprite('ph615_03', 6)	# 2754-2759
    sprite('ph615_02', 6)	# 2760-2765
    sprite('ph615_01', 6)	# 2766-2771
    sprite('ph615_00', 6)	# 2772-2777
    Unknown23018(1)
    label(174)
    sprite('ph000_00', 7)	# 2778-2784
    sprite('ph000_01', 7)	# 2785-2791
    sprite('ph000_02', 7)	# 2792-2798
    sprite('ph000_03', 7)	# 2799-2805
    sprite('ph000_04', 7)	# 2806-2812
    sprite('ph000_05', 7)	# 2813-2819
    sprite('ph000_06', 7)	# 2820-2826
    sprite('ph000_07', 7)	# 2827-2833
    sprite('ph000_08', 7)	# 2834-2840
    sprite('ph000_09', 7)	# 2841-2847
    gotoLabel(174)
    ExitState()
    label(1000)
    sprite('ph650_00', 1)	# 2848-2848
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)
    SFX_1('bph600')
    label(1001)
    sprite('ph650_00', 1)	# 2849-2849
    if SLOT_97:
        _gotolabel(1001)
    sprite('ph650_00', 20)	# 2850-2869
    sprite('ph650_00', 32767)	# 2870-35636
    Unknown23029(24, 10001, 0)
    Unknown23029(22, 10001, 0)
    Unknown23029(23, 10001, 0)

    def upon_43():
        if (SLOT_48 == 10004):
            clearUponHandler(43)
            Unknown18008()
        if (SLOT_48 == 10005):
            sendToLabel(1002)
    label(1002)
    sprite('ph600_15', 6)	# 35637-35642
    sprite('ph000_00', 6)	# 35643-35648
    sprite('ph611_00', 6)	# 35649-35654
    sprite('ph611_01', 6)	# 35655-35660
    sprite('ph611_02', 590)	# 35661-36250
    sprite('ph611_01', 6)	# 36251-36256
    sprite('ph611_00', 6)	# 36257-36262
    sprite('ph615_00', 5)	# 36263-36267
    sprite('ph615_01', 5)	# 36268-36272
    sprite('ph615_02', 5)	# 36273-36277
    sprite('ph615_03', 5)	# 36278-36282
    sprite('ph615_04', 5)	# 36283-36287
    Unknown18008()
    label(1003)
    sprite('ph615_05', 5)	# 36288-36292
    sprite('ph615_06', 5)	# 36293-36297
    sprite('ph615_07', 5)	# 36298-36302
    sprite('ph615_08', 5)	# 36303-36307
    sprite('ph615_09', 5)	# 36308-36312
    sprite('ph615_10', 5)	# 36313-36317
    gotoLabel(1003)

@State
def CmnActRoundWin():
    sprite('ph615_00', 5)	# 1-5
    sprite('ph615_01', 5)	# 6-10
    sprite('ph615_02', 5)	# 11-15
    if random_(2, 0, 50):
        pass
    else:
        pass
    Unknown23018(1)
    sprite('ph615_03', 5)	# 16-20
    sprite('ph615_04', 5)	# 21-25
    label(0)
    sprite('ph615_05', 5)	# 26-30
    sprite('ph615_06', 5)	# 31-35
    sprite('ph615_07', 5)	# 36-40
    sprite('ph615_08', 5)	# 41-45
    sprite('ph615_09', 5)	# 46-50
    sprite('ph615_10', 5)	# 51-55
    gotoLabel(0)

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
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('ph611_00', 6)	# 4-9
    sprite('ph611_01', 6)	# 10-15
    sprite('ph611_02', 6)	# 16-21
    sprite('ph611_03', 15)	# 22-36
    sprite('ph611_04', 6)	# 37-42
    sprite('ph611_05', 6)	# 43-48
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bph524', 100, 896036962, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bph402_0', 100, 879259746, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bph520', 100, 896036962, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ph611_06', 6)	# 49-54
    sprite('ph611_07', 6)	# 55-60
    sprite('ph611_08', 15)	# 61-75
    sprite('ph611_09', 5)	# 76-80
    SFX_0('019_cloth_c')
    sprite('ph611_10', 5)	# 81-85
    sprite('ph611_11', 5)	# 86-90
    GFX_1('phef_611fire', 0)
    GFX_1('phef_611fire', 1)
    sprite('ph611_12', 5)	# 91-95
    sprite('ph611_13', 5)	# 96-100
    sprite('ph611_14', 5)	# 101-105
    sprite('ph611_15', 8)	# 106-113
    label(1)
    sprite('ph611_16', 8)	# 114-121
    sprite('ph611_17', 8)	# 122-129
    sprite('ph611_18', 8)	# 130-137
    gotoLabel(1)
    label(10)
    sprite('ph615_00', 5)	# 138-142
    sprite('ph615_01', 5)	# 143-147
    sprite('ph615_02', 5)	# 148-152
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bph524', 100, 896036962, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bph402_0', 100, 879259746, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bph521', 100, 896036962, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ph615_03', 5)	# 153-157
    sprite('ph615_04', 5)	# 158-162
    label(11)
    sprite('ph615_05', 5)	# 163-167
    sprite('ph615_06', 5)	# 168-172
    sprite('ph615_07', 5)	# 173-177
    sprite('ph615_08', 5)	# 178-182
    sprite('ph615_09', 5)	# 183-187
    sprite('ph615_10', 5)	# 188-192
    gotoLabel(11)
    label(100)
    sprite('ph611_00', 6)	# 193-198
    sprite('ph611_01', 6)	# 199-204
    sprite('ph611_02', 6)	# 205-210
    sprite('ph611_03', 15)	# 211-225
    sprite('ph611_04', 6)	# 226-231
    sprite('ph611_05', 6)	# 232-237
    SFX_1('bph700bjb')
    sprite('ph611_06', 6)	# 238-243
    sprite('ph611_07', 6)	# 244-249
    sprite('ph611_08', 15)	# 250-264
    sprite('ph611_09', 5)	# 265-269
    SFX_0('019_cloth_c')
    sprite('ph611_10', 5)	# 270-274
    sprite('ph611_11', 5)	# 275-279
    GFX_1('phef_611fire', 0)
    GFX_1('phef_611fire', 1)
    sprite('ph611_12', 5)	# 280-284
    sprite('ph611_13', 5)	# 285-289
    sprite('ph611_14', 5)	# 290-294
    sprite('ph611_15', 8)	# 295-302
    label(101)
    sprite('ph611_16', 8)	# 303-310
    sprite('ph611_17', 8)	# 311-318
    sprite('ph611_18', 8)	# 319-326
    if SLOT_97:
        _gotolabel(101)
    sprite('ph611_16', 1)	# 327-327
    Unknown21007(24, 40)
    Unknown21011(360)
    label(102)
    sprite('ph611_16', 8)	# 328-335
    sprite('ph611_17', 8)	# 336-343
    sprite('ph611_18', 8)	# 344-351
    gotoLabel(102)
    label(110)
    sprite('ph611_00', 6)	# 352-357
    sprite('ph611_01', 6)	# 358-363
    sprite('ph611_02', 6)	# 364-369
    sprite('ph611_03', 15)	# 370-384
    sprite('ph611_04', 6)	# 385-390
    sprite('ph611_05', 6)	# 391-396
    SFX_1('bph700pyo')
    sprite('ph611_06', 6)	# 397-402
    sprite('ph611_07', 6)	# 403-408
    sprite('ph611_08', 15)	# 409-423
    sprite('ph611_09', 5)	# 424-428
    SFX_0('019_cloth_c')
    sprite('ph611_10', 5)	# 429-433
    sprite('ph611_11', 5)	# 434-438
    GFX_1('phef_611fire', 0)
    GFX_1('phef_611fire', 1)
    sprite('ph611_12', 5)	# 439-443
    sprite('ph611_13', 5)	# 444-448
    sprite('ph611_14', 5)	# 449-453
    sprite('ph611_15', 8)	# 454-461
    label(111)
    sprite('ph611_16', 8)	# 462-469
    sprite('ph611_17', 8)	# 470-477
    sprite('ph611_18', 8)	# 478-485
    if SLOT_97:
        _gotolabel(111)
    sprite('ph611_16', 1)	# 486-486
    Unknown21007(24, 40)
    Unknown21011(360)
    label(112)
    sprite('ph611_16', 8)	# 487-494
    sprite('ph611_17', 8)	# 495-502
    sprite('ph611_18', 8)	# 503-510
    gotoLabel(112)
    label(120)
    sprite('ph615_00', 5)	# 511-515
    sprite('ph615_01', 5)	# 516-520
    sprite('ph615_02', 5)	# 521-525
    SFX_1('bph700rwi')
    sprite('ph615_03', 5)	# 526-530
    sprite('ph615_04', 5)	# 531-535
    label(121)
    sprite('ph615_05', 5)	# 536-540
    sprite('ph615_06', 5)	# 541-545
    sprite('ph615_07', 5)	# 546-550
    sprite('ph615_08', 5)	# 551-555
    sprite('ph615_09', 5)	# 556-560
    sprite('ph615_10', 5)	# 561-565
    if SLOT_97:
        _gotolabel(121)
    sprite('ph615_05', 1)	# 566-566
    Unknown21007(24, 40)
    Unknown21011(270)
    label(122)
    sprite('ph615_05', 5)	# 567-571
    sprite('ph615_06', 5)	# 572-576
    sprite('ph615_07', 5)	# 577-581
    sprite('ph615_08', 5)	# 582-586
    sprite('ph615_09', 5)	# 587-591
    sprite('ph615_10', 5)	# 592-596
    gotoLabel(122)
    label(130)
    sprite('ph611_00', 6)	# 597-602
    sprite('ph611_01', 6)	# 603-608
    sprite('ph611_02', 6)	# 609-614
    sprite('ph611_03', 15)	# 615-629
    sprite('ph611_04', 6)	# 630-635
    sprite('ph611_05', 6)	# 636-641
    SFX_1('bph700uca')
    sprite('ph611_06', 6)	# 642-647
    sprite('ph611_07', 6)	# 648-653
    sprite('ph611_08', 15)	# 654-668
    sprite('ph611_09', 5)	# 669-673
    SFX_0('019_cloth_c')
    sprite('ph611_10', 5)	# 674-678
    sprite('ph611_11', 5)	# 679-683
    GFX_1('phef_611fire', 0)
    GFX_1('phef_611fire', 1)
    sprite('ph611_12', 5)	# 684-688
    sprite('ph611_13', 5)	# 689-693
    sprite('ph611_14', 5)	# 694-698
    sprite('ph611_15', 8)	# 699-706
    label(131)
    sprite('ph611_16', 8)	# 707-714
    sprite('ph611_17', 8)	# 715-722
    sprite('ph611_18', 8)	# 723-730
    if SLOT_97:
        _gotolabel(131)
    sprite('ph611_16', 1)	# 731-731
    Unknown21007(24, 40)
    Unknown21011(240)
    label(132)
    sprite('ph611_16', 8)	# 732-739
    sprite('ph611_17', 8)	# 740-747
    sprite('ph611_18', 8)	# 748-755
    gotoLabel(132)
    label(140)
    sprite('ph615_00', 5)	# 756-760
    sprite('ph615_01', 5)	# 761-765
    sprite('ph615_02', 5)	# 766-770
    SFX_1('bph700ugo')
    sprite('ph615_03', 5)	# 771-775
    sprite('ph615_04', 5)	# 776-780
    label(141)
    sprite('ph615_05', 5)	# 781-785
    sprite('ph615_06', 5)	# 786-790
    sprite('ph615_07', 5)	# 791-795
    sprite('ph615_08', 5)	# 796-800
    sprite('ph615_09', 5)	# 801-805
    sprite('ph615_10', 5)	# 806-810
    if SLOT_97:
        _gotolabel(141)
    sprite('ph615_05', 1)	# 811-811
    Unknown21007(24, 40)
    Unknown21011(300)
    label(142)
    sprite('ph615_05', 5)	# 812-816
    sprite('ph615_06', 5)	# 817-821
    sprite('ph615_07', 5)	# 822-826
    sprite('ph615_08', 5)	# 827-831
    sprite('ph615_09', 5)	# 832-836
    sprite('ph615_10', 5)	# 837-841
    gotoLabel(142)
    label(150)
    sprite('ph000_00', 1)	# 842-842

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    if (not SLOT_158):
        Unknown2019(1000)
    label(151)
    sprite('ph000_00', 7)	# 843-849
    sprite('ph000_01', 7)	# 850-856
    sprite('ph000_02', 7)	# 857-863
    sprite('ph000_03', 7)	# 864-870
    sprite('ph000_04', 7)	# 871-877
    sprite('ph000_05', 7)	# 878-884
    sprite('ph000_06', 7)	# 885-891
    sprite('ph000_07', 7)	# 892-898
    sprite('ph000_08', 7)	# 899-905
    sprite('ph000_09', 7)	# 906-912
    gotoLabel(151)
    label(152)
    sprite('ph611_00', 6)	# 913-918
    sprite('ph611_01', 6)	# 919-924
    sprite('ph611_02', 6)	# 925-930
    sprite('ph611_03', 15)	# 931-945
    sprite('ph611_04', 6)	# 946-951
    sprite('ph611_05', 6)	# 952-957
    SFX_1('bph701brc')
    sprite('ph611_06', 6)	# 958-963
    sprite('ph611_07', 6)	# 964-969
    sprite('ph611_08', 15)	# 970-984
    sprite('ph611_09', 5)	# 985-989
    SFX_0('019_cloth_c')
    sprite('ph611_10', 5)	# 990-994
    sprite('ph611_11', 5)	# 995-999
    GFX_1('phef_611fire', 0)
    GFX_1('phef_611fire', 1)
    sprite('ph611_12', 5)	# 1000-1004
    sprite('ph611_13', 5)	# 1005-1009
    sprite('ph611_14', 5)	# 1010-1014
    sprite('ph611_15', 8)	# 1015-1022
    Unknown23018(1)
    label(153)
    sprite('ph611_16', 8)	# 1023-1030
    sprite('ph611_17', 8)	# 1031-1038
    sprite('ph611_18', 8)	# 1039-1046
    gotoLabel(153)
    label(160)
    sprite('ph000_00', 1)	# 1047-1047

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ph000_00', 7)	# 1048-1054
    sprite('ph000_01', 7)	# 1055-1061
    sprite('ph000_02', 7)	# 1062-1068
    sprite('ph000_03', 7)	# 1069-1075
    sprite('ph000_04', 7)	# 1076-1082
    sprite('ph000_05', 7)	# 1083-1089
    sprite('ph000_06', 7)	# 1090-1096
    sprite('ph000_07', 7)	# 1097-1103
    sprite('ph000_08', 7)	# 1104-1110
    sprite('ph000_09', 7)	# 1111-1117
    gotoLabel(161)
    label(162)
    sprite('ph615_00', 5)	# 1118-1122
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
    sprite('ph615_01', 5)	# 1123-1127
    sprite('ph615_02', 5)	# 1128-1132
    SFX_1('bph701pag')
    sprite('ph615_03', 5)	# 1133-1137
    sprite('ph615_04', 5)	# 1138-1142
    Unknown23018(1)
    label(163)
    sprite('ph615_05', 5)	# 1143-1147
    sprite('ph615_06', 5)	# 1148-1152
    sprite('ph615_07', 5)	# 1153-1157
    sprite('ph615_08', 5)	# 1158-1162
    sprite('ph615_09', 5)	# 1163-1167
    sprite('ph615_10', 5)	# 1168-1172
    gotoLabel(163)
    label(170)
    sprite('ph000_00', 1)	# 1173-1173

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ph000_00', 7)	# 1174-1180
    sprite('ph000_01', 7)	# 1181-1187
    sprite('ph000_02', 7)	# 1188-1194
    sprite('ph000_03', 7)	# 1195-1201
    sprite('ph000_04', 7)	# 1202-1208
    sprite('ph000_05', 7)	# 1209-1215
    sprite('ph000_06', 7)	# 1216-1222
    sprite('ph000_07', 7)	# 1223-1229
    sprite('ph000_08', 7)	# 1230-1236
    sprite('ph000_09', 7)	# 1237-1243
    gotoLabel(171)
    label(172)
    sprite('ph620_00', 6)	# 1244-1249
    sprite('ph620_01', 6)	# 1250-1255
    sprite('ph620_02', 6)	# 1256-1261
    sprite('ph620_03', 6)	# 1262-1267
    sprite('ph620_04', 6)	# 1268-1273
    sprite('ph620_05', 6)	# 1274-1279
    sprite('ph620_06', 5)	# 1280-1284
    SFX_1('bph701pyu')
    sprite('ph620_07', 5)	# 1285-1289
    sprite('ph620_08', 8)	# 1290-1297
    Unknown23018(1)
    label(173)
    sprite('ph620_09', 8)	# 1298-1305
    sprite('ph620_10', 8)	# 1306-1313
    sprite('ph620_11', 8)	# 1314-1321
    gotoLabel(173)

@State
def CmnActLose():
    sprite('ph620_00', 30)	# 1-30
    if SLOT_158:
        Unknown7006('bph403_0', 100, 879259746, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ph620_01', 6)	# 31-36
    sprite('ph620_02', 6)	# 37-42
    sprite('ph620_03', 6)	# 43-48
    sprite('ph620_04', 6)	# 49-54
    sprite('ph620_05', 6)	# 55-60
    sprite('ph620_06', 5)	# 61-65
    sprite('ph620_07', 5)	# 66-70
    sprite('ph620_08', 8)	# 71-78
    Unknown23018(1)
    label(0)
    sprite('ph620_09', 8)	# 79-86
    sprite('ph620_10', 8)	# 87-94
    sprite('ph620_11', 8)	# 95-102
    gotoLabel(0)