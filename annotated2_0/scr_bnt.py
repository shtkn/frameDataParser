@Subroutine
def PreInit():
    Unknown12019('626e7400000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Unknown12024(2)
    Unknown13039(0)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 350000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 250000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 350000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown14015(-50000, 450000, -200000, 100000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15021(2000)
    Unknown14015(-50000, 100000, -200000, 700000, 200, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown15013(200)
    Unknown15021(2000)
    Unknown14015(-50000, 200000, -100000, 300000, 500, 10)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 350000, -200000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15021(250)
    Unknown14015(0, 400000, -100000, 200000, 1000, 10)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(2000)
    Unknown14015(-50000, 250000, -300000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(-50000, 250000, -300000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15013(500)
    Unknown15015(100, 100)
    Unknown14015(0, 400000, -450000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-100000, 250000, -300000, 250000, 500, 1)
    Move_EndRegister()
    Move_Register('ShortDash', 0x1)
    Move_AirGround_(0x2000)
    Move_Input_(0xda)
    Unknown14005(1)
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
    Move_Register('Assault_cancel_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 150, 0)
    Move_EndRegister()
    Move_Register('Assault_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14004(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 150, 0)
    Move_EndRegister()
    Move_Register('Assault_2nd_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 300000, 300, 0)
    Move_EndRegister()
    Move_Register('Assault_3rdYoko', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 300, 0)
    Move_EndRegister()
    Move_Register('Assault_cancel_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 100, 0)
    Move_EndRegister()
    Move_Register('Assault_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14004(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 300, 0)
    Move_EndRegister()
    Move_Register('Assault_2nd_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 300000, 300, 0)
    Move_EndRegister()
    Move_Register('Assault_3rdTate', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 300, 0)
    Move_EndRegister()
    Move_Register('Dodge_cancel', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(2000)
    Unknown15021(2000)
    Unknown14015(-50000, 50000, -200000, 250000, 30, 0)
    Move_EndRegister()
    Move_Register('Dodge', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14004(1)
    Unknown15014(2000)
    Unknown15021(2000)
    Unknown14015(100000, 200000, -200000, 250000, 30, 0)
    Move_EndRegister()
    Move_Register('DodgeThrow', INPUT_SPECIALMOVE)
    Move_Input_(0x2)
    Unknown14005(1)
    Unknown15010()
    Unknown15021(4000)
    Unknown15014(2000)
    Unknown14015(-250000, 250000, -200000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('DodgeThrow_B', INPUT_SPECIALMOVE)
    Move_Input_(0xb)
    Unknown14005(1)
    Unknown14013('DodgeThrow')
    Move_EndRegister()
    Move_Register('DodgeThrow_C', INPUT_SPECIALMOVE)
    Move_Input_(0x14)
    Unknown14005(1)
    Unknown14013('DodgeThrow')
    Move_EndRegister()
    Move_Register('EdgeAssault_cancel', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown14015(0, 450000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('EdgeAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14004(1)
    Unknown15013(1)
    Unknown14015(0, 400000, -200000, 150000, 250, 0)
    Move_EndRegister()
    Move_Register('AN_CmnActInvincibleAttack_cance', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14004(1)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 400000, -200000, 250000, 250, 5)
    Move_EndRegister()
    Move_Register('AN_CmnActInvincibleAttackAir_ca', 0x65)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14004(1)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 400000, -200000, 250000, 250, 5)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown14015(-50000, 300000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('Assault_cancel_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15011(10000)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(250000, 750000, -200000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('Assault_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14004(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 150, 0)
    Move_EndRegister()
    Move_Register('Assault_2nd_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 300000, 300, 0)
    Move_EndRegister()
    Move_Register('Assault_3rdYoko_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 300, 0)
    Move_EndRegister()
    Move_Register('Assault_3rdTate_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15000(0)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(0, 700000, -200000, 250000, 300, 0)
    Move_EndRegister()
    Move_Register('EdgeAssault_cancel_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(1)
    Unknown14015(0, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('EdgeAssault_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14004(1)
    Unknown15013(1)
    Unknown14015(0, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_cancel', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown14024('CheckCancelSkill')
    Unknown15012(1)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD_cancel', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown14024('CheckCancelSkill')
    Unknown15012(1)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateEdgeAssault_cancel', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateEdgeAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown14024('CheckCancelSkill')
    Unknown15014(2000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateEdgeAssaultOD_cancel', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateEdgeAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown14024('CheckCancelSkill')
    Unknown15014(2000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssault_cancel', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(1500)
    Unknown14015(0, 500000, -400000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssault', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown14024('CheckCancelSkill')
    Unknown15012(1)
    Unknown15014(1500)
    Unknown14015(0, 500000, -400000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssaultOD_cancel', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(1500)
    Unknown14015(0, 500000, -400000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssaultOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14004(1)
    Unknown14024('CheckCancelSkill')
    Unknown15012(1)
    Unknown15014(1500)
    Unknown14015(0, 500000, -400000, -200000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2C', 'Assault_cancel_A', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5B', 'EdgeAssault_cancel', 10000000)
    Unknown15024('NmlAtk5B', 'EdgeAssault_cancel_EX', 10000000)
    Unknown15024('NmlAtk5BB', 'Assault_cancel_B', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'AN_CmnActInvincibleAttackAir_ca', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5C', 'FJump', 10000000)
    Unknown15024('Assault_A', 'Assault_2nd_A', 10000000)
    Unknown15024('Assault_cancel_A', 'Assault_2nd_A', 10000000)
    Unknown15024('Assault_2nd_A', 'Assault_3rdYoko', 10000000)
    Unknown15024('Assault_B', 'Assault_2nd_B', 10000000)
    Unknown15024('Assault_cancel_B', 'Assault_2nd_B', 10000000)
    Unknown15024('Assault_2nd_B', 'Assault_3rdTate', 10000000)
    Unknown15024('Assault_3rdTate', 'FHighJump', 10000000)
    Unknown15024('Assault_EX', 'Assault_2nd_EX', 10000000)
    Unknown15024('Assault_cancel_EX', 'Assault_2nd_EX', 10000000)
    Unknown15024('Assault_2nd_EX', 'Assault_3rdYoko_EX', 10000000)
    Unknown15024('Dodge_cancel', 'DodgeThrow', 10000000)
    Unknown15024('Dodge', 'DodgeThrow', 10000000)
    Unknown15024('CmnActInvincibleAttack', 'AntiAir2nd', 10000000)
    Unknown15024('AN_CmnActInvincibleAttack_cance', 'AntiAir2nd', 10000000)
    Unknown15024('CmnActInvincibleAttackAir', 'AntiAir2nd', 10000000)
    Unknown15024('AN_CmnActInvincibleAttackAir_ca', 'AntiAir2nd', 10000000)
    Unknown12018(0, 'nt062_01')
    Unknown12018(1, 'nt062_03')
    Unknown12018(2, 'nt062_04')
    Unknown12018(3, 'nt062_05')
    Unknown12018(4, 'nt062_05')
    Unknown12018(5, 'nt062_06')
    Unknown12018(6, 'nt062_07')
    Unknown12018(7, 'nt041_02')
    Unknown12018(8, 'nt040_02')
    Unknown12018(9, 'nt045_02')
    Unknown12018(10, 'nt060_00')
    Unknown12018(11, 'nt060_01')
    Unknown12018(12, 'nt060_03')
    Unknown12018(13, 'nt060_05')
    Unknown12018(14, 'nt060_07')
    Unknown12018(15, 'nt060_14')
    Unknown12018(16, 'nt050_00')
    Unknown12018(17, 'nt052_00')
    Unknown12018(18, 'nt054_00')
    Unknown12018(19, 'nt000_00')
    Unknown12018(20, 'nt000_00')
    Unknown12018(25, 'nt063_00')
    Unknown12018(26, 'nt063_01')
    Unknown12018(27, 'nt063_02')
    Unknown12018(28, 'nt063_04')
    Unknown12018(29, 'nt063_10')
    Unknown12018(24, 'nt073_01')
    Unknown7010(0, 'bnt000')
    Unknown7010(1, 'bnt001')
    Unknown7010(2, 'bnt002')
    Unknown7010(3, 'bnt003')
    Unknown7010(4, 'bnt004')
    Unknown7010(5, 'bnt005')
    Unknown7010(6, 'bnt006')
    Unknown7010(7, 'bnt007')
    Unknown7010(8, 'bnt008')
    Unknown7010(9, 'bnt009')
    Unknown7010(10, 'bnt010')
    Unknown7010(15, 'bnt011')
    Unknown7010(16, 'bnt012')
    Unknown7010(17, 'bnt013')
    Unknown7010(18, 'bnt014')
    Unknown7010(19, 'bnt015')
    Unknown7010(20, 'bnt016')
    Unknown7010(21, 'bnt017')
    Unknown7010(22, 'bnt018')
    Unknown7010(23, 'bnt019')
    Unknown7010(24, 'bnt020')
    Unknown7010(25, 'bnt021')
    Unknown7010(28, 'bnt022')
    Unknown7010(29, 'bnt023')
    Unknown7010(30, 'bnt024')
    Unknown7010(31, 'bnt025')
    Unknown7010(32, 'bnt026')
    Unknown7010(33, 'bnt027')
    Unknown7010(34, 'bnt028')
    Unknown7010(35, 'bnt029')
    Unknown7010(36, 'bnt030')
    Unknown7010(37, 'bnt031')
    Unknown7010(39, 'bnt032')
    Unknown7010(42, 'bnt033')
    Unknown7010(43, 'bnt034')
    Unknown7010(44, 'bnt035')
    Unknown7010(45, 'bnt036')
    Unknown7010(46, 'bnt037')
    Unknown7010(47, 'bnt038')
    Unknown7010(48, 'bnt039')
    Unknown7010(49, 'bnt040')
    Unknown7010(50, 'bnt041')
    Unknown7010(52, 'bnt042')
    Unknown7010(53, 'bnt043')
    Unknown7010(54, 'bnt100_0')
    Unknown7010(55, 'bnt100_1')
    Unknown7010(56, 'bnt100_2')
    Unknown7010(63, 'bnt101_0')
    Unknown7010(64, 'bnt101_1')
    Unknown7010(65, 'bnt101_2')
    Unknown7010(57, 'bnt102_0')
    Unknown7010(58, 'bnt102_1')
    Unknown7010(59, 'bnt102_2')
    Unknown7010(66, 'bnt103_0')
    Unknown7010(67, 'bnt103_1')
    Unknown7010(68, 'bnt103_2')
    Unknown7010(60, 'bnt104_0')
    Unknown7010(61, 'bnt104_1')
    Unknown7010(62, 'bnt104_2')
    Unknown7010(69, 'bnt105_0')
    Unknown7010(70, 'bnt105_1')
    Unknown7010(71, 'bnt105_2')
    Unknown7010(72, 'bnt150')
    Unknown7010(73, 'bnt151')
    Unknown7010(74, 'bnt152')
    Unknown7010(85, 'bnt153')
    Unknown7010(87, 'bnt154')
    Unknown7010(88, 'bnt155')
    Unknown7010(96, 'bnt161_0')
    Unknown7010(97, 'bnt161_1')
    Unknown7010(92, 'bnt162_0')
    Unknown7010(93, 'bnt162_1')
    Unknown7010(98, 'bnt163_0')
    Unknown7010(99, 'bnt163_1')
    Unknown7010(100, 'bnt164_0')
    Unknown7010(101, 'bnt164_1')
    Unknown7010(105, 'bnt165_0')
    Unknown7010(106, 'bnt165_1')
    Unknown7010(102, 'bnt166_0')
    Unknown7010(103, 'bnt166_1')
    Unknown7010(90, 'bnt167_0')
    Unknown7010(91, 'bnt167_1')
    Unknown7010(107, 'bnt168_0')
    Unknown7010(108, 'bnt168_1')
    Unknown7010(110, 'bnt169_0')
    Unknown7010(111, 'bnt169_1')
    Unknown7010(112, 'bnt159_0')
    Unknown7010(113, 'bnt159_1')
    Unknown7010(94, 'bnt401_0')
    Unknown7010(95, 'bnt400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174654564676541737361756c7400000000000000000000000000')
    Unknown12059('05000000556c74696d6174654564676541737361756c744f440000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def CheckCancelSkill():
    SLOT_47 = 0
    if (SLOT_4 == 0):
        SLOT_47 = 1

@Subroutine
def OnFrameStep():
    if SLOT_21:
        if (not SLOT_109):
            SLOT_66 = 0

@Subroutine
def OnPreDraw():
    Unknown23030('4e545f5261676e615377697463680000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@State
def CmnActStand():
    label(0)
    sprite('nt000_00', 7)	# 1-7
    sprite('nt000_01', 7)	# 8-14
    sprite('nt000_02', 7)	# 15-21
    sprite('nt000_03', 7)	# 22-28
    sprite('nt000_04', 7)	# 29-35
    sprite('nt000_05', 7)	# 36-42
    sprite('nt000_06', 7)	# 43-49
    sprite('nt000_07', 7)	# 50-56
    sprite('nt000_08', 7)	# 57-63
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('nt001_00', 7)	# 64-70
    SLOT_88 = 960
    SFX_1('bnt000')
    sprite('nt001_01', 7)	# 71-77
    sprite('nt001_02', 7)	# 78-84
    sprite('nt001_03', 7)	# 85-91
    sprite('nt001_04', 7)	# 92-98
    sprite('nt001_05', 7)	# 99-105
    sprite('nt001_06', 7)	# 106-112
    sprite('nt001_07', 7)	# 113-119
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('nt003_00', 3)	# 1-3
    sprite('nt003_01', 3)	# 4-6
    sprite('nt003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('nt010_00', 4)	# 1-4
    sprite('nt010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('nt010_02', 6)	# 1-6
    sprite('nt010_03', 6)	# 7-12
    sprite('nt010_04', 6)	# 13-18
    sprite('nt010_05', 6)	# 19-24
    sprite('nt010_06', 6)	# 25-30
    sprite('nt010_07', 6)	# 31-36
    sprite('nt010_08', 6)	# 37-42
    sprite('nt010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('nt013_00', 3)	# 1-3
    sprite('nt013_01', 3)	# 4-6
    sprite('nt013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('nt010_01', 4)	# 1-4
    sprite('nt010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('nt023_00', 2)	# 1-2
    sprite('nt023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('nt020_00', 4)	# 1-4
    sprite('nt020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('nt020_02', 3)	# 1-3
    sprite('nt020_03', 3)	# 4-6
    sprite('nt020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('nt020_05', 3)	# 1-3
    sprite('nt020_06', 3)	# 4-6
    label(0)
    sprite('nt020_07', 4)	# 7-10
    sprite('nt020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('nt024_00', 3)	# 1-3
    sprite('nt024_01', 3)	# 4-6
    sprite('nt024_02', 3)	# 7-9
    sprite('nt024_03', 3)	# 10-12
    sprite('nt024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('nt024_00', 2)	# 1-2
    sprite('nt024_01', 2)	# 3-4
    sprite('nt024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('nt024_03', 3)	# 1-3
    sprite('nt024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('nt030_00', 8)	# 1-8
    label(0)
    sprite('nt030_01', 8)	# 9-16
    sprite('nt030_02', 8)	# 17-24
    sprite('nt030_03', 8)	# 25-32
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_04', 8)	# 33-40
    sprite('nt030_05', 8)	# 41-48
    sprite('nt030_06', 8)	# 49-56
    sprite('nt030_07', 8)	# 57-64
    sprite('nt030_08', 8)	# 65-72
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt030_09', 8)	# 73-80
    sprite('nt030_10', 8)	# 81-88
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('nt031_00', 8)	# 1-8
    label(0)
    sprite('nt031_01', 8)	# 9-16
    sprite('nt031_02', 8)	# 17-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt031_03', 8)	# 25-32
    sprite('nt031_04', 8)	# 33-40
    sprite('nt031_05', 8)	# 41-48
    sprite('nt031_06', 8)	# 49-56
    sprite('nt031_07', 8)	# 57-64
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('nt031_08', 8)	# 65-72
    sprite('nt031_09', 8)	# 73-80
    sprite('nt031_10', 8)	# 81-88
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('nt032_00', 2)	# 1-2
    label(0)
    sprite('nt032_01', 3)	# 3-5
    sprite('nt032_02', 3)	# 6-8
    sprite('nt032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('nt032_04', 3)	# 13-15
    sprite('nt032_05', 3)	# 16-18
    sprite('nt032_06', 3)	# 19-21
    Unknown8006(100, 1, 1)
    sprite('nt032_07', 4)	# 22-25
    sprite('nt032_08', 3)	# 26-28
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('nt032_09', 3)	# 1-3
    sprite('nt032_10', 3)	# 4-6
    sprite('nt032_11', 3)	# 7-9
    sprite('nt032_12', 3)	# 10-12

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
    sprite('nt033_00', 1)	# 1-1
    sprite('nt033_01', 3)	# 2-4
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('nt033_02', 3)	# 5-7
    loopRest()
    label(0)
    sprite('nt033_01', 3)	# 8-10
    sprite('nt033_02', 3)	# 11-13
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt033_03', 1)	# 14-14
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('nt033_04', 2)	# 15-16
    sprite('nt033_05', 2)	# 17-18
    sprite('nt033_06', 2)	# 19-20
    sprite('nt033_07', 2)	# 21-22

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('nt035_00', 3)	# 1-3
    label(0)
    sprite('nt035_01', 3)	# 4-6
    sprite('nt035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('nt036_00', 3)	# 1-3
    label(0)
    sprite('nt036_01', 3)	# 4-6
    sprite('nt036_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('nt050_00', 1)	# 1-1
    sprite('nt050_01', 1)	# 2-2
    sprite('nt050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('nt050_01', 1)	# 1-1
    sprite('nt050_02', 1)	# 2-2
    sprite('nt050_01', 2)	# 3-4
    sprite('nt050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('nt050_02', 1)	# 1-1
    sprite('nt050_03', 1)	# 2-2
    sprite('nt050_02', 2)	# 3-4
    sprite('nt050_01', 2)	# 5-6
    sprite('nt050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('nt050_03', 1)	# 1-1
    sprite('nt050_04', 1)	# 2-2
    sprite('nt050_03', 2)	# 3-4
    sprite('nt050_02', 2)	# 5-6
    sprite('nt050_01', 2)	# 7-8
    sprite('nt050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('nt050_04', 1)	# 1-1
    sprite('nt050_04', 1)	# 2-2
    sprite('nt050_04', 2)	# 3-4
    sprite('nt050_03', 2)	# 5-6
    sprite('nt050_02', 2)	# 7-8
    sprite('nt050_01', 2)	# 9-10
    sprite('nt050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('nt052_00', 1)	# 1-1
    sprite('nt052_01', 1)	# 2-2
    sprite('nt052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('nt052_01', 1)	# 1-1
    sprite('nt052_02', 1)	# 2-2
    sprite('nt052_01', 2)	# 3-4
    sprite('nt052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('nt052_02', 1)	# 1-1
    sprite('nt052_03', 1)	# 2-2
    sprite('nt052_02', 2)	# 3-4
    sprite('nt052_01', 2)	# 5-6
    sprite('nt052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('nt052_03', 1)	# 1-1
    sprite('nt052_04', 1)	# 2-2
    sprite('nt052_03', 2)	# 3-4
    sprite('nt052_02', 2)	# 5-6
    sprite('nt052_01', 2)	# 7-8
    sprite('nt052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('nt052_04', 1)	# 1-1
    sprite('nt052_04', 1)	# 2-2
    sprite('nt052_04', 2)	# 3-4
    sprite('nt052_03', 2)	# 5-6
    sprite('nt052_02', 2)	# 7-8
    sprite('nt052_01', 2)	# 9-10
    sprite('nt052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('nt054_00', 1)	# 1-1
    sprite('nt054_01', 1)	# 2-2
    sprite('nt054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('nt054_01', 1)	# 1-1
    sprite('nt054_02', 1)	# 2-2
    sprite('nt054_01', 2)	# 3-4
    sprite('nt054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('nt054_02', 1)	# 1-1
    sprite('nt054_03', 1)	# 2-2
    sprite('nt054_02', 2)	# 3-4
    sprite('nt054_01', 2)	# 5-6
    sprite('nt054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('nt054_03', 1)	# 1-1
    sprite('nt054_04', 1)	# 2-2
    sprite('nt054_03', 2)	# 3-4
    sprite('nt054_02', 2)	# 5-6
    sprite('nt054_01', 2)	# 7-8
    sprite('nt054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('nt054_04', 1)	# 1-1
    sprite('nt054_04', 1)	# 2-2
    sprite('nt054_04', 2)	# 3-4
    sprite('nt054_03', 2)	# 5-6
    sprite('nt054_02', 2)	# 7-8
    sprite('nt054_01', 2)	# 9-10
    sprite('nt054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('nt060_00', 4)	# 1-4
    label(0)
    sprite('nt060_01', 4)	# 5-8
    sprite('nt060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('nt060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('nt060_04', 4)	# 1-4
    label(0)
    sprite('nt060_05', 4)	# 5-8
    sprite('nt060_06', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('nt060_07', 2)	# 1-2
    sprite('nt060_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('nt060_09', 3)	# 1-3
    sprite('nt060_10', 3)	# 4-6
    sprite('nt060_11', 3)	# 7-9
    sprite('nt060_12', 3)	# 10-12
    sprite('nt060_13', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('nt060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('nt061_00', 4)	# 1-4
    sprite('nt061_01', 3)	# 5-7
    sprite('nt061_02', 3)	# 8-10
    sprite('nt061_03', 3)	# 11-13
    sprite('nt061_04', 3)	# 14-16
    sprite('nt061_05', 3)	# 17-19
    sprite('nt061_06', 3)	# 20-22
    sprite('nt061_07', 3)	# 23-25
    sprite('nt061_08', 3)	# 26-28

@State
def CmnActFDownUpper():
    sprite('nt063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('nt063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('nt063_02', 3)	# 1-3
    sprite('nt063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('nt063_04', 3)	# 1-3
    sprite('nt063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('nt063_06', 2)	# 1-2
    sprite('nt063_07', 2)	# 3-4
    sprite('nt063_08', 3)	# 5-7
    sprite('nt063_09', 3)	# 8-10
    sprite('nt063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('nt063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('nt064_00', 2)	# 1-2
    sprite('nt064_01', 2)	# 3-4
    sprite('nt064_02', 2)	# 5-6
    sprite('nt064_03', 2)	# 7-8
    sprite('nt064_04', 2)	# 9-10
    sprite('nt064_05', 2)	# 11-12
    sprite('nt064_06', 2)	# 13-14
    sprite('nt064_07', 2)	# 15-16
    sprite('nt064_08', 2)	# 17-18
    sprite('nt064_09', 2)	# 19-20
    sprite('nt064_10', 2)	# 21-22
    sprite('nt064_11', 2)	# 23-24

@State
def CmnActVDownUpper():
    sprite('nt062_00', 3)	# 1-3
    label(0)
    sprite('nt062_01', 3)	# 4-6
    sprite('nt062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('nt062_03', 3)	# 1-3
    sprite('nt062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('nt062_05', 3)	# 1-3
    sprite('nt062_06', 3)	# 4-6
    label(0)
    sprite('nt062_07', 3)	# 7-9
    sprite('nt062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('nt062_09', 2)	# 1-2
    sprite('nt062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('nt072_00', 3)	# 1-3
    sprite('nt072_01', 3)	# 4-6
    sprite('nt072_02', 3)	# 7-9
    label(0)
    sprite('nt072_01', 3)	# 10-12
    sprite('nt072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('nt074_00', 3)	# 1-3
    sprite('nt074_01', 3)	# 4-6
    sprite('nt074_02', 3)	# 7-9
    sprite('nt074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('nt082_00', 2)	# 1-2
    sprite('nt082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('nt070_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('nt073_00', 3)	# 1-3
    sprite('nt073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('nt073_02', 3)	# 1-3
    label(0)
    sprite('nt073_03', 3)	# 4-6
    sprite('nt073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('nt070_00', 2)	# 1-2
    sprite('nt070_01', 2)	# 3-4
    label(0)
    sprite('nt070_02', 5)	# 5-9
    sprite('nt070_03', 5)	# 10-14
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('nt070_04', 4)	# 1-4
    sprite('nt070_05', 4)	# 5-8
    sprite('nt070_06', 4)	# 9-12
    sprite('nt070_07', 4)	# 13-16
    sprite('nt070_08', 4)	# 17-20
    sprite('nt070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('nt070_10', 2)	# 1-2
    sprite('nt070_11', 2)	# 3-4
    sprite('nt070_12', 2)	# 5-6
    sprite('nt070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('nt113_00', 3)	# 1-3
    sprite('nt113_01', 3)	# 4-6
    sprite('nt113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('nt113_00', 3)	# 1-3
    sprite('nt113_01', 3)	# 4-6
    sprite('nt113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('nt113_00', 3)	# 1-3
    sprite('nt113_01', 3)	# 4-6
    sprite('nt113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('nt110_00', 2)	# 1-2
    sprite('nt110_01', 2)	# 3-4
    sprite('nt110_02', 2)	# 5-6
    sprite('nt110_03', 2)	# 7-8
    sprite('nt110_04', 2)	# 9-10
    sprite('nt110_05', 2)	# 11-12
    sprite('nt110_06', 2)	# 13-14
    sprite('nt110_07', 2)	# 15-16
    sprite('nt110_08', 2)	# 17-18
    sprite('nt110_09', 2)	# 19-20

@State
def CmnActUkemiLandB():
    sprite('nt111_00', 2)	# 1-2
    sprite('nt111_01', 2)	# 3-4
    sprite('nt111_02', 2)	# 5-6
    sprite('nt111_03', 2)	# 7-8
    sprite('nt111_04', 2)	# 9-10
    sprite('nt111_05', 2)	# 11-12
    sprite('nt111_06', 2)	# 13-14
    sprite('nt111_07', 2)	# 15-16
    sprite('nt111_08', 2)	# 17-18
    sprite('nt111_09', 2)	# 19-20

@State
def CmnActUkemiLandN():
    sprite('nt112_00', 2)	# 1-2
    sprite('nt112_01', 2)	# 3-4
    sprite('nt112_02', 2)	# 5-6
    sprite('nt112_03', 2)	# 7-8
    sprite('nt112_04', 2)	# 9-10
    sprite('nt112_05', 2)	# 11-12
    sprite('nt112_06', 3)	# 13-15
    sprite('nt112_07', 3)	# 16-18
    sprite('nt112_08', 2)	# 19-20

@State
def CmnActUkemiLandNLanding():
    sprite('nt024_00', 3)	# 1-3
    sprite('nt024_01', 3)	# 4-6
    sprite('nt024_02', 3)	# 7-9
    sprite('nt024_03', 3)	# 10-12
    sprite('nt024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('nt040_00', 3)	# 1-3
    sprite('nt040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('nt040_02', 4)	# 1-4
    sprite('nt040_03', 4)	# 5-8
    sprite('nt040_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('nt040_01', 3)	# 1-3
    sprite('nt040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('nt040_05', 3)	# 1-3
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('nt040_01', 3)	# 1-3
    sprite('nt040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('nt041_00', 3)	# 1-3
    sprite('nt041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('nt041_02', 4)	# 1-4
    sprite('nt041_03', 4)	# 5-8
    sprite('nt041_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('nt041_01', 3)	# 1-3
    sprite('nt041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('nt041_05', 3)	# 1-3

@State
def CmnActHighHeavyGuardEnd():
    sprite('nt041_01', 3)	# 1-3
    sprite('nt041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('nt043_00', 3)	# 1-3
    sprite('nt043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('nt043_02', 3)	# 1-3
    sprite('nt043_03', 3)	# 4-6
    sprite('nt043_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('nt043_01', 3)	# 1-3
    sprite('nt043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('nt043_05', 3)	# 1-3

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('nt043_01', 3)	# 1-3
    sprite('nt043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('nt045_00', 3)	# 1-3
    sprite('nt045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('nt045_02', 3)	# 1-3
    sprite('nt045_03', 3)	# 4-6
    sprite('nt045_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('nt045_01', 3)	# 1-3
    sprite('nt045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('nt045_05', 3)	# 1-3

@State
def CmnActAirHeavyGuardEnd():
    sprite('nt045_01', 3)	# 1-3
    sprite('nt045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('nt090_00', 2)	# 1-2
    sprite('nt090_01', 2)	# 3-4
    sprite('nt090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('nt090_03', 6)	# 6-11
    sprite('nt090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('nt091_00', 2)	# 1-2
    sprite('nt091_01', 2)	# 3-4
    sprite('nt091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('nt091_03', 6)	# 6-11
    sprite('nt091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('nt092_00', 2)	# 1-2
    sprite('nt092_01', 2)	# 3-4
    sprite('nt092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('nt092_03', 6)	# 6-11
    sprite('nt092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('nt025_00', 4)	# 1-4
    sprite('nt025_01', 4)	# 5-8
    sprite('nt025_00ex01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('nt040_02', 1)	# 1-1
    sprite('nt040_01', 3)	# 2-4
    sprite('nt040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('nt312_00', 2)	# 1-2
    sprite('nt312_01', 2)	# 3-4
    sprite('nt312_02', 2)	# 5-6
    sprite('nt312_03', 8)	# 7-14	 **attackbox here**
    sprite('nt312_04', 4)	# 15-18
    sprite('nt312_05', 3)	# 19-21
    sprite('nt312_06', 4)	# 22-25

@State
def CmnActAirLockWait():
    sprite('nt045_02', 1)	# 1-1
    sprite('nt045_01', 3)	# 2-4
    sprite('nt045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('nt322_00', 2)	# 1-2
    sprite('nt322_01', 2)	# 3-4
    sprite('nt322_02', 8)	# 5-12
    sprite('nt322_03', 2)	# 13-14	 **attackbox here**
    sprite('nt322_04', 3)	# 15-17
    sprite('nt322_05', 3)	# 18-20
    sprite('nt322_06', 3)	# 21-23

@State
def CmnActLandSpin():
    sprite('nt071_00', 4)	# 1-4
    sprite('nt071_01', 4)	# 5-8
    label(0)
    sprite('nt071_02', 2)	# 9-10
    sprite('nt071_03', 2)	# 11-12
    sprite('nt071_04', 2)	# 13-14
    sprite('nt071_05', 2)	# 15-16
    sprite('nt071_06', 2)	# 17-18
    sprite('nt071_07', 2)	# 19-20
    sprite('nt071_08', 2)	# 21-22
    sprite('nt071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('nt071_10', 6)	# 1-6
    sprite('nt071_11', 5)	# 7-11
    sprite('nt071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('nt071_02', 2)	# 1-2
    sprite('nt071_03', 2)	# 3-4
    sprite('nt071_04', 2)	# 5-6
    sprite('nt071_05', 2)	# 7-8
    sprite('nt071_06', 2)	# 9-10
    sprite('nt071_07', 2)	# 11-12
    sprite('nt071_08', 2)	# 13-14
    sprite('nt071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('nt077_00', 2)	# 1-2
    sprite('nt077_01', 2)	# 3-4
    sprite('nt077_00ex01', 2)	# 5-6
    sprite('nt077_01ex01', 2)	# 7-8
    sprite('nt077_00ex02', 2)	# 9-10
    sprite('nt077_01ex02', 2)	# 11-12
    sprite('nt077_00ex03', 2)	# 13-14
    sprite('nt077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('nt077_02', 4)	# 1-4
    label(0)
    sprite('nt077_03', 3)	# 5-7
    sprite('nt077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('nt077_05', 5)	# 1-5
    sprite('nt077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('nt060_07', 3)	# 1-3
    sprite('nt060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('nt060_11', 4)	# 1-4
    sprite('nt060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('nt331_00', 2)	# 1-2
    sprite('nt331_01', 2)	# 3-4
    label(0)
    sprite('nt331_02', 3)	# 5-7
    sprite('nt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('nt331_04', 2)	# 1-2
    sprite('nt331_05', 2)	# 3-4
    label(0)
    sprite('nt331_06', 3)	# 5-7
    sprite('nt331_07', 3)	# 8-10
    sprite('nt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('nt331_09', 3)	# 1-3
    sprite('nt331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('nt331_11', 2)	# 1-2
    sprite('nt331_12', 2)	# 3-4
    label(0)
    sprite('nt331_02', 3)	# 5-7
    sprite('nt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('nt331_04', 2)	# 1-2
    sprite('nt331_05', 2)	# 3-4
    label(0)
    sprite('nt331_06', 3)	# 5-7
    sprite('nt331_07', 3)	# 8-10
    sprite('nt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('nt331_13', 3)	# 1-3
    sprite('nt331_14', 3)	# 4-6
    sprite('nt020_05', 3)	# 7-9
    sprite('nt020_06', 3)	# 10-12
    label(0)
    sprite('nt020_07', 4)	# 13-16
    sprite('nt020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('nt333_00', 3)	# 1-3
    sprite('nt333_01', 3)	# 4-6
    sprite('nt333_02', 3)	# 7-9
    Unknown4054(11)
    GFX_1('ntef_333_kyushu', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt333_03', 32767)	# 10-32776
    GFX_0('EMB_NT_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():

    def upon_IMMEDIATE():
        SLOT_66 = 1
    sprite('nt333_04', 3)	# 1-3
    label(0)
    sprite('nt333_05', 3)	# 4-6
    GFX_0('ntef_OverDrive', 0)
    GFX_1('ntef_333_kaiho', 0)
    GFX_1('ntef_333_kyushu_tub', 0)
    sprite('nt333_06', 3)	# 7-9
    sprite('nt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('nt333_08', 6)	# 1-6
    sprite('nt333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('nt333_10', 3)	# 1-3
    sprite('nt333_11', 3)	# 4-6
    sprite('nt333_12', 3)	# 7-9
    Unknown4054(11)
    GFX_1('ntef_333_kyushu', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt333_13', 32767)	# 10-32776
    GFX_0('EMB_NT_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():

    def upon_IMMEDIATE():
        SLOT_66 = 1
    sprite('nt333_14', 3)	# 1-3
    label(0)
    sprite('nt333_05', 3)	# 4-6
    GFX_0('ntef_OverDrive', 0)
    GFX_1('ntef_333_kaiho', 0)
    GFX_1('ntef_333_kyushu_tub', 0)
    sprite('nt333_06', 3)	# 7-9
    sprite('nt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('nt333_15', 3)	# 1-3
    sprite('nt333_16', 3)	# 4-6
    sprite('nt020_05', 3)	# 7-9
    sprite('nt020_06', 3)	# 10-12
    label(0)
    sprite('nt020_07', 4)	# 13-16
    sprite('nt020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('nt333_00', 3)	# 1-3
    sprite('nt333_01', 3)	# 4-6
    sprite('nt333_02', 3)	# 7-9
    Unknown4054(11)
    GFX_1('ntef_333_kyushu', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt333_03', 32767)	# 10-32776
    GFX_0('EMB_NT_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('nt333_04', 3)	# 1-3
    label(0)
    sprite('nt333_05', 3)	# 4-6
    GFX_0('ntef_OverDrive', 0)
    GFX_1('ntef_333_kaiho', 0)
    GFX_1('ntef_333_kyushu_tub', 0)
    sprite('nt333_06', 3)	# 7-9
    sprite('nt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('nt333_08', 6)	# 1-6
    sprite('nt333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('nt333_10', 3)	# 1-3
    sprite('nt333_11', 3)	# 4-6
    sprite('nt333_12', 3)	# 7-9
    Unknown4054(11)
    GFX_1('ntef_333_kyushu', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt333_13', 32767)	# 10-32776
    GFX_0('EMB_NT_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('nt333_14', 3)	# 1-3
    label(0)
    sprite('nt333_05', 3)	# 4-6
    GFX_0('ntef_OverDrive', 0)
    GFX_1('ntef_333_kaiho', 0)
    GFX_1('ntef_333_kyushu_tub', 0)
    sprite('nt333_06', 3)	# 7-9
    sprite('nt333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('nt333_15', 3)	# 1-3
    sprite('nt333_16', 3)	# 4-6
    sprite('nt020_05', 3)	# 7-9
    sprite('nt020_06', 3)	# 10-12
    label(0)
    sprite('nt020_07', 4)	# 13-16
    sprite('nt020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('nt331_00', 2)	# 1-2
    sprite('nt331_01', 2)	# 3-4
    label(0)
    sprite('nt331_02', 3)	# 5-7
    sprite('nt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('nt331_04', 2)	# 1-2
    sprite('nt331_05', 2)	# 3-4
    label(0)
    sprite('nt331_06', 3)	# 5-7
    sprite('nt331_07', 3)	# 8-10
    sprite('nt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('nt331_09', 3)	# 1-3
    sprite('nt331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('nt331_11', 2)	# 1-2
    sprite('nt331_12', 2)	# 3-4
    label(0)
    sprite('nt331_02', 3)	# 5-7
    sprite('nt331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('nt331_04', 2)	# 1-2
    sprite('nt331_05', 2)	# 3-4
    label(0)
    sprite('nt331_06', 3)	# 5-7
    sprite('nt331_07', 3)	# 8-10
    sprite('nt331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('nt331_13', 3)	# 1-3
    sprite('nt331_14', 3)	# 4-6
    sprite('nt020_05', 3)	# 7-9
    sprite('nt020_06', 3)	# 10-12
    label(0)
    sprite('nt020_07', 4)	# 13-16
    sprite('nt020_08', 4)	# 17-20
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

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_CLEAR_OR_EXIT():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('nt300_00', 5)	# 1-5
    sprite('nt300_01', 5)	# 6-10
    sprite('nt300_02', 5)	# 11-15
    sprite('nt300_03', 5)	# 16-20
    sprite('nt300_04', 6)	# 21-26
    sprite('nt300_05', 6)	# 27-32
    sprite('nt300_06', 6)	# 33-38
    sprite('nt300_07', 5)	# 39-43
    sprite('nt300_08', 5)	# 44-48
    sprite('nt300_09', 6)	# 49-54
    sprite('nt300_10', 4)	# 55-58
    sprite('nt300_11', 2)	# 59-60
    sprite('nt300_12', 2)	# 61-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_CLEAR_OR_EXIT():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('nt045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('nt045_00', 1)	# 2-2
    sprite('nt045_01', 4)	# 3-6
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    SFX_0('301_overdrive_end')
    label(0)
    sprite('nt045_02', 3)	# 7-9
    sprite('nt045_03', 3)	# 10-12
    sprite('nt045_04', 4)	# 13-16
    loopRest()
    Unknown2038(1)
    if (SLOT_2 == 5):
        Unknown1018()
        Unknown1023()
        Unknown1038()
        Unknown1019(40)
        YAccel(40)
    (SLOT_2 >= 6)
    if SLOT_ReturnVal:
        _gotolabel(1)
    gotoLabel(0)
    label(1)
    sprite('nt045_01', 6)	# 17-22
    sprite('nt045_00', 6)	# 23-28

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
    sprite('null', 28)	# 603-630
    sprite('nt253_04', 1)	# 631-631
    Unknown1086(22)
    teleportRelativeX(-250000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    physicsXImpulse(300000)
    physicsYImpulse(-200000)
    sendToLabelUpon(2, 9)
    sprite('nt253_07', 30)	# 632-661
    SFX_3('ntse_05')
    label(9)
    sprite('nt253_08', 3)	# 662-664	 **attackbox here**
    Unknown1019(30)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    GFX_1('ntef_D_aura', 6)
    GFX_1('ntef_D_aura', 7)
    sprite('nt024_00', 6)	# 665-670
    GFX_0('ntef_253_b', -1)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('nt024_01', 3)	# 671-673
    sprite('nt024_02', 3)	# 674-676
    sprite('nt024_03', 6)	# 677-682
    sprite('nt024_04', 4)	# 683-686

@State
def CmnActChangePartnerQuickIn():
    sprite('nt032_09', 8)	# 1-8
    sprite('nt032_10', 7)	# 9-15
    sprite('nt032_11', 7)	# 16-22
    sprite('nt032_12', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('nt033_01', 3)	# 1-3
    sprite('nt033_02', 3)	# 4-6
    sprite('nt033_01', 3)	# 7-9
    sprite('nt033_02', 3)	# 10-12
    sprite('nt033_01', 3)	# 13-15
    sprite('nt033_02', 3)	# 16-18
    sprite('nt033_01', 3)	# 19-21
    sprite('nt033_02', 3)	# 22-24
    sprite('nt033_01', 3)	# 25-27
    sprite('nt033_02', 3)	# 28-30
    sprite('nt033_01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('nt033_00', 1)	# 1-1
    sprite('nt033_01', 2)	# 2-3
    sprite('nt033_02', 2)	# 4-5
    sprite('nt033_02', 4)	# 6-9
    loopRest()
    label(0)
    sprite('nt033_01', 3)	# 10-12
    sprite('nt033_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt033_03', 1)	# 16-16
    sprite('nt033_04', 1)	# 17-17
    sprite('nt033_05', 1)	# 18-18
    sprite('nt033_06', 1)	# 19-19
    sprite('nt033_07', 2)	# 20-21

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('nt300_00', 5)	# 1-5
    sprite('nt300_01', 5)	# 6-10
    sprite('nt300_02', 5)	# 11-15
    sprite('nt300_03', 5)	# 16-20
    sprite('nt300_04', 6)	# 21-26
    sprite('nt300_05', 6)	# 27-32
    sprite('nt300_06', 6)	# 33-38
    sprite('nt300_07', 5)	# 39-43
    sprite('nt300_08', 5)	# 44-48
    sprite('nt300_09', 6)	# 49-54
    sprite('nt300_08', 4)	# 55-58
    sprite('nt300_07', 3)	# 59-61
    sprite('nt300_10', 7)	# 62-68
    sprite('nt300_11', 4)	# 69-72
    sprite('nt300_12', 4)	# 73-76

@State
def CmnActAComboFinalBlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)

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
    sprite('nt253_05', 2)	# 32-33
    SFX_3('ntse_05')
    sprite('nt253_07', 2)	# 34-35
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt253_08', 30)	# 36-65	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    label(1)
    sprite('nt253_08', 1)	# 66-66	 **attackbox here**
    sprite('nt024_00', 5)	# 67-71
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt024_01', 12)	# 72-83
    sprite('nt024_02', 5)	# 84-88
    sprite('nt024_03', 4)	# 89-92
    sprite('nt024_04', 4)	# 93-96

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('nt024_00', 2)	# 2-3
    sprite('nt024_01', 3)	# 4-6
    sprite('nt024_02', 3)	# 7-9
    sprite('nt024_03', 3)	# 10-12
    sprite('nt024_04', 3)	# 13-15
    sprite('nt404_00', 4)	# 16-19
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_01', 5)	# 20-24
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt404_02', 5)	# 25-29
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown7009(2)
    sprite('nt404_03', 5)	# 30-34
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_04', 3)	# 35-37	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt404_05', 8)	# 38-45
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 5)	# 46-50
    sprite('nt404_07', 7)	# 51-57
    sprite('nt404_08', 7)	# 58-64
    sprite('nt404_09', 5)	# 65-69
    Unknown3029(0)
    sprite('nt402_10', 4)	# 70-73
    sprite('nt402_11', 2)	# 74-75

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(10000)
        Unknown1112('')
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('nt200_06', 2)	# 1-2
    sprite('nt200_08', 2)	# 3-4
    physicsXImpulse(5000)
    Unknown8006(100, 1, 1)
    sprite('nt200_09', 3)	# 5-7
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    physicsXImpulse(55000)
    sprite('nt200_10', 5)	# 8-12	 **attackbox here**
    Unknown1019(5)
    sprite('nt200_11', 4)	# 13-16
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('nt200_12', 5)	# 17-21
    sprite('nt200_13', 5)	# 22-26
    sprite('nt200_14', 4)	# 27-30

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(14000)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('nt201_00', 5)	# 1-5
    sprite('nt201_01', 3)	# 6-8
    physicsXImpulse(5000)
    Unknown7009(1)
    SFX_0('004_swing_grap_1_1')
    sprite('nt201_02', 3)	# 9-11
    StartMultihit()
    Unknown1019(150)
    sprite('nt201_03', 3)	# 12-14	 **attackbox here**
    Unknown1019(80)
    sprite('nt201_04', 4)	# 15-18
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('nt201_05', 3)	# 19-21
    sprite('nt201_06', 4)	# 22-25
    sprite('nt201_07', 4)	# 26-29
    sprite('nt201_08', 3)	# 30-32
    SFX_FOOTSTEP_(100, 1, 1)

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(18000)
        hitstun(21)
        AirUntechableTime(21)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('nt340_00', 3)	# 1-3
    sprite('nt340_01', 1)	# 4-4
    sprite('nt340_02', 1)	# 5-5
    sprite('nt340_06', 3)	# 6-8
    sprite('nt340_07', 3)	# 9-11
    Unknown2016(250)
    sprite('nt340_08', 3)	# 12-14
    physicsXImpulse(18000)
    Unknown8003(100, 1, 1)
    Unknown7009(2)
    sprite('nt340_09', 2)	# 15-16	 **attackbox here**
    GFX_0('ntef_340', -1)
    Unknown2016(-1)
    sprite('nt340_09', 2)	# 17-18	 **attackbox here**
    Unknown1019(0)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('nt340_10', 3)	# 19-21
    sprite('nt340_11', 3)	# 22-24
    sprite('nt340_12', 3)	# 25-27
    teleportRelativeX(10000)
    sprite('nt340_13', 3)	# 28-30
    teleportRelativeX(5000)
    sprite('nt340_14', 3)	# 31-33
    teleportRelativeX(5000)
    sprite('nt340_15', 3)	# 34-36
    teleportRelativeX(5000)
    sprite('nt340_16', 3)	# 37-39
    teleportRelativeX(10000)
    sprite('nt340_17', 3)	# 40-42

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(2500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(30)
        Hitstop(15)
        AirPushbackX(46000)
        AirPushbackY(11000)
        PushbackX(19800)
        sendToLabelUpon(2, 9)
        JumpCancel_(0)
        Unknown11044(1)
        Unknown30088(1)
    sprite('nt211_00', 4)	# 1-4
    sprite('nt211_01', 3)	# 5-7
    sprite('nt211_02', 3)	# 8-10
    physicsXImpulse(20000)
    physicsYImpulse(20000)
    setGravity(2500)
    Unknown1051(50)
    Unknown8001(0, 0)
    sprite('nt211_03', 3)	# 11-13
    SFX_0('004_swing_grap_1_2')
    Unknown7006('bnt111_0', 100, 829714018, 828322097, 0, 0, 100, 829714018, 845099313, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('nt211_04', 2)	# 14-15
    sprite('nt211_05', 5)	# 16-20
    sprite('nt211_06', 4)	# 21-24	 **attackbox here**
    Unknown1019(50)
    sprite('nt211_07', 2)	# 25-26
    Recovery()
    Unknown2063()
    sprite('nt211_08', 32767)	# 27-32793
    loopRest()
    label(9)
    sprite('nt211_09', 8)	# 32794-32801
    Unknown8000(100, 1, 1)
    Unknown1019(20)
    sprite('nt211_10', 4)	# 32802-32805
    Unknown1019(50)
    sprite('nt211_11', 4)	# 32806-32809
    Unknown1019(0)
    sprite('nt211_12', 4)	# 32810-32813
    sprite('nt211_13', 4)	# 32814-32817
    sprite('nt211_14', 4)	# 32818-32821

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        AirPushbackY(12000)
        PushbackX(12000)
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('nt200_00', 2)	# 1-2
    Unknown1051(60)
    sprite('nt200_01', 2)	# 3-4
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('nt200_02', 1)	# 5-5
    sprite('nt200_03', 3)	# 6-8	 **attackbox here**
    sprite('nt200_04', 3)	# 9-11
    Recovery()
    Unknown2063()
    sprite('nt200_05', 3)	# 12-14
    sprite('nt200_06', 3)	# 15-17
    sprite('nt200_07', 3)	# 18-20

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1800)
        AirPushbackX(28000)
        AirPushbackY(10000)
        AirUntechableTime(30)
        Unknown9202(10)
        PushbackX(24800)
        Hitstop(15)
        Unknown9016(1)
        Unknown1112('')
        ChipDamagePct(5)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        SLOT_60 = 0
    sprite('nt203_00', 3)	# 1-3
    sprite('nt203_01', 3)	# 4-6
    Unknown14070('ShortDash')

    def upon_24():
        clearUponHandler(24)
        sendToLabel(1)
    Unknown14072('ShortDash')
    sprite('nt203_02', 3)	# 7-9
    GFX_0('ntef_D_bodyaura', 1)
    GFX_0('ntef_D_handaura_3D', 0)
    GFX_0('ntef_D_handaura', 0)
    GFX_1('ntef_D_aura', 2)
    sprite('nt203_03', 2)	# 10-11
    sprite('nt203_03', 1)	# 12-12
    loopRest()
    sprite('nt203_04ex01', 3)	# 13-15
    GFX_1('ntef_D_aura', 2)
    sprite('nt203_02ex01', 3)	# 16-18
    ScreenShake(3000, 9000)
    Unknown8000(-1, 1, 0)
    sprite('nt203_03ex01', 2)	# 19-20
    sprite('nt203_03ex01', 1)	# 21-21
    sprite('nt203_04ex01', 3)	# 22-24
    GFX_1('ntef_D_aura', 1)
    sprite('nt203_02ex01', 3)	# 25-27
    sprite('nt203_03ex01', 3)	# 28-30
    loopRest()
    label(0)
    sprite('nt203_05ex01', 1)	# 31-31
    clearUponHandler(24)
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    GFX_1('ntef_D_aura', 0)
    sprite('nt203_06ex01', 1)	# 32-32
    sprite('nt203_07ex01', 2)	# 33-34
    SFX_3('ntse_04')
    GFX_1('ntef_D_aura', 0)
    Unknown7007('626e743130395f30000000000000000064000000626e743130395f31000000000000000064000000626e743130395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('nt203_08ex01', 3)	# 35-37	 **attackbox here**
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000000000000')
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000001000000')
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000002000000')
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000003000000')
    Damage(2100)
    ChipDamagePct(20)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(12)
    AirPushbackX(42000)
    AirPushbackY(15000)
    Unknown9130(35)
    Unknown9142(28)
    AirUntechableTime(40)
    Hitstop(20)
    blockstun(23)

    def upon_11():
        ScreenShake(3000, 3000)
    sprite('nt203_09ex01', 2)	# 38-39	 **attackbox here**
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000000000000')
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000001000000')
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000002000000')
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000003000000')
    sprite('nt203_10ex01', 3)	# 40-42
    Unknown4049(750)
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000000000000')
    Unknown4049(750)
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000001000000')
    Unknown4049(750)
    Unknown4045('6e7465665f445f6175726100000000000000000000000000000000000000000002000000')
    Recovery()
    Unknown2063()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt203_05', 1)	# 43-43
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    sprite('nt203_06', 1)	# 44-44
    sprite('nt203_07', 1)	# 45-45
    Unknown7007('626e743130395f30000000000000000064000000626e743130395f31000000000000000064000000626e743130395f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ntse_05')
    sprite('nt203_08', 3)	# 46-48	 **attackbox here**
    Unknown9202(0)
    Unknown14073('ShortDash')
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt203_09', 2)	# 49-50	 **attackbox here**
    sprite('nt203_10', 8)	# 51-58
    Recovery()
    Unknown2063()
    label(9)
    sprite('nt203_11', 4)	# 59-62
    sprite('nt203_12', 5)	# 63-67
    sprite('nt203_13', 5)	# 68-72
    sprite('nt203_14', 5)	# 73-77
    ExitState()
    label(9)
    sprite('nt203_11', 3)	# 78-80
    sprite('nt203_12', 4)	# 81-84
    sprite('nt203_13', 4)	# 85-88
    sprite('nt203_14', 4)	# 89-92

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1800)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(25)
        AirPushbackX(12000)
        AirPushbackY(25000)
        Hitstop(15)
        Unknown9016(1)
        ChipDamagePct(5)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        SLOT_60 = 0
    sprite('nt213_00', 3)	# 1-3
    sprite('nt213_01', 3)	# 4-6
    Unknown14070('ShortDash')
    GFX_0('ntef_D_bodyaura', 1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt213_02', 3)	# 7-9

    def upon_24():
        clearUponHandler(24)
        sendToLabel(1)
    Unknown14072('ShortDash')
    sprite('nt213_03', 2)	# 10-11
    sprite('nt213_03', 1)	# 12-12
    loopRest()
    sprite('nt213_01ex01', 3)	# 13-15	 **attackbox here**
    sprite('nt213_02ex01', 3)	# 16-18	 **attackbox here**
    ScreenShake(3000, 9000)
    Unknown8000(-1, 1, 0)
    sprite('nt213_03ex01', 3)	# 19-21	 **attackbox here**
    loopRest()
    label(0)
    sprite('nt213_04ex01', 1)	# 22-22
    clearUponHandler(24)
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    sprite('nt213_05ex01', 1)	# 23-23	 **attackbox here**
    sprite('nt213_06ex01', 2)	# 24-25	 **attackbox here**
    SFX_3('ntse_04')
    SFX_1('bnt300')
    sprite('nt213_07ex01', 3)   # active	# 26-28	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    GFX_1('ntef_D_aura', 6)
    GFX_1('ntef_D_aura', 7)
    GFX_1('ntef_D_aura', 8)
    GFX_1('ntef_D_aura', 9)
    GFX_1('ntef_D_aura', 10)
    Damage(2100)
    AirPushbackX(22000)
    AirPushbackY(36000)
    AirUntechableTime(60)
    ChipDamagePct(20)
    Hitstop(20)
    blockstun(23)

    def upon_11():
        ScreenShake(3000, 3000)
    sprite('nt213_08ex01', 3)	# 29-31	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt213_09ex01', 3)	# 32-34	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('nt213_10ex01', 3)	# 35-37	 **attackbox here**
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt213_04', 1)	# 38-38	 **attackbox here**
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    sprite('nt213_05', 1)	# 39-39	 **attackbox here**
    sprite('nt213_06', 1)	# 40-40	 **attackbox here**
    Unknown7007('626e743131305f30000000000000000064000000626e743131305f31000000000000000064000000626e743131305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ntse_05')
    sprite('nt213_07', 3)	# 41-43	 **attackbox here**
    Unknown14073('ShortDash')
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt213_08', 3)	# 44-46	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    sprite('nt213_09', 3)	# 47-49	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('nt213_10', 3)	# 50-52
    label(9)
    sprite('nt213_11', 3)	# 53-55
    sprite('nt213_12', 4)	# 56-59
    sprite('nt213_13', 4)	# 60-63

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        PushbackX(12000)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockCancel('CmnActCrushAttack')
    Unknown23145('NmlAtk2A')
    if SLOT_ReturnVal:
        _gotolabel(1)
    sprite('nt230_00', 2)	# 1-2
    Unknown1051(60)
    sprite('nt230_01', 2)	# 3-4
    SFX_0('004_swing_grap_1_0')
    sprite('nt230_02', 2)	# 5-6
    Unknown7009(0)
    sprite('nt230_03', 2)	# 7-8	 **attackbox here**
    gotoLabel(9)
    label(1)
    sprite('nt230_01', 3)	# 9-11
    sprite('nt230_02', 3)	# 12-14
    SFX_0('004_swing_grap_1_0')
    Unknown7009(0)
    sprite('nt230_03', 2)	# 15-16	 **attackbox here**
    label(9)
    sprite('nt230_04', 3)	# 17-19
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('nt230_02', 3)	# 20-22
    sprite('nt230_01', 4)	# 23-26
    sprite('nt230_00', 4)	# 27-30

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirUntechableTime(22)
        AirPushbackX(3000)
        AirPushbackY(27000)
        AirHitstunAnimation(10)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
        Unknown11058('0000000001000000000000000000000000000000')
    sprite('nt232_00', 4)	# 1-4
    sprite('nt232_01', 2)	# 5-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_2')
    sprite('nt232_02', 2)	# 7-8
    Unknown7009(2)
    sprite('nt232_03', 2)	# 9-10
    sprite('nt232_04', 3)	# 11-13	 **attackbox here**
    sprite('nt232_04', 3)	# 14-16	 **attackbox here**
    sprite('nt232_05', 4)	# 17-20
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('nt232_06', 5)	# 21-25
    sprite('nt232_07', 5)	# 26-30
    sprite('nt232_08', 5)	# 31-35
    sprite('nt232_09', 3)	# 36-38

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        Unknown2004(1, 0)
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirUntechableTime(40)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(13000)
        HitLow(2)
        Unknown2004(1, 0)
    sprite('nt234_00', 2)	# 1-2
    sprite('nt234_01', 3)	# 3-5
    SFX_0('004_swing_grap_1_2')
    sprite('nt234_02', 2)	# 6-7
    Unknown7007('626e743130375f30000000000000000064000000626e743130375f31000000000000000064000000626e743130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('nt234_03', 3)	# 8-10
    sprite('nt234_04', 2)	# 11-12	 **attackbox here**
    sprite('nt234_05', 2)	# 13-14	 **attackbox here**
    sprite('nt234_06', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('nt234_07', 3)	# 18-20
    sprite('nt234_08', 3)	# 21-23
    sprite('nt234_09', 2)	# 24-25
    sprite('nt234_10', 3)	# 26-28
    sprite('nt234_11', 3)	# 29-31

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('nt251_00', 3)	# 1-3
    sprite('nt251_01', 3)	# 4-6
    SFX_0('004_swing_grap_1_1')
    sprite('nt251_02', 4)	# 7-10
    Unknown7009(1)
    sprite('nt251_03', 4)	# 11-14	 **attackbox here**
    sprite('nt251_04', 2)	# 15-16	 **attackbox here**
    sprite('nt251_05', 2)	# 17-18
    Recovery()
    Unknown2063()
    sprite('nt251_06', 4)	# 19-22
    sprite('nt251_07', 4)	# 23-26
    sprite('nt251_08', 3)	# 27-29

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('nt252_00', 2)	# 1-2
    sprite('nt252_01', 2)	# 3-4
    SFX_0('004_swing_grap_1_2')
    sprite('nt252_02', 2)	# 5-6
    Unknown7009(2)
    sprite('nt252_03', 2)	# 7-8
    sprite('nt252_04', 3)	# 9-11	 **attackbox here**
    sprite('nt252_05', 3)	# 12-14	 **attackbox here**
    sprite('nt252_06', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('nt252_07', 3)	# 18-20
    sprite('nt252_08', 3)	# 21-23
    sprite('nt252_09', 3)	# 24-26

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1800)
        AirPushbackX(12000)
        AirPushbackY(-75000)
        AirUntechableTime(40)
        Hitstop(15)
        Unknown9016(1)
        ChipDamagePct(5)

        def upon_24():
            clearUponHandler(24)
            sendToLabel(1)
            Unknown1043()
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('nt253_00', 3)	# 1-3
    sprite('nt253_01', 3)	# 4-6
    GFX_0('ntef_D_bodyaura', 1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    Unknown22004(6, 1)
    sprite('nt253_02', 3)	# 7-9
    sprite('nt253_03', 2)	# 10-11
    sprite('nt253_03', 1)	# 12-12
    loopRest()
    sprite('nt253_01', 3)	# 13-15
    sprite('nt253_02', 3)	# 16-18
    ScreenShake(5000, 5000)
    Unknown1019(20)
    YAccel(0)
    Unknown1039(0)
    Unknown1034(0)
    Unknown1051(0)
    sprite('nt253_03', 3)	# 19-21
    sprite('nt253_01', 3)	# 22-24
    loopRest()
    label(0)
    sprite('nt253_04', 3)	# 25-27
    clearUponHandler(24)
    setGravity(-200)
    GFX_1('ntef_D_aura', 0)
    sprite('nt253_05ex01', 3)	# 28-30
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    Unknown7007('626e743130385f30000000000000000064000000626e743130385f31000000000000000064000000626e743130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('nt253_06ex01', 6)	# 31-36
    Unknown1043()
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt253_07ex01', 3)	# 37-39
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt253_08ex01', 3)	# 40-42	 **attackbox here**
    AttackLevel_(4)
    Damage(2100)
    GroundedHitstunAnimation(1)
    AirPushbackY(-82000)
    YImpluseBeforeWallbounce(0)
    AirUntechableTime(60)
    Hitstop(20)
    ChipDamagePct(20)
    Unknown9190(1)
    Unknown9118(35)
    blockstun(23)

    def upon_11():
        ScreenShake(3000, 3000)
    Unknown22004(12, 1)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    GFX_1('ntef_D_aura', 6)
    GFX_1('ntef_D_aura', 7)
    sprite('nt253_09ex01', 2)	# 43-44	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    sprite('nt253_10', 3)	# 45-47
    GFX_0('ntef_253_b', -1)
    Recovery()
    Unknown2063()
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt253_04', 1)	# 48-48
    GFX_1('ntef_D_aura', 0)
    sprite('nt253_05', 2)	# 49-50
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    GFX_1('ntef_D_aura', 0)
    sprite('nt253_06', 2)	# 51-52
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown7007('626e743131305f30000000000000000064000000626e743131305f31000000000000000064000000626e743131305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ntse_05')
    sprite('nt253_07', 2)	# 53-54
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt253_08', 3)	# 55-57	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    sprite('nt253_09', 2)	# 58-59	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    sprite('nt253_10', 3)	# 60-62
    GFX_0('ntef_253_a', -1)
    Recovery()
    Unknown2063()
    label(9)
    sprite('nt253_11', 3)	# 63-65
    sprite('nt253_12', 4)	# 66-69
    sprite('nt253_13', 4)	# 70-73
    sprite('nt253_14', 4)	# 74-77

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirUntechableTime(20)
        PushbackX(15000)
        AirPushbackY(20000)
        HitOrBlockJumpCancel(1)
    sprite('nt212_03', 3)	# 1-3
    sprite('nt212_04', 3)	# 4-6
    sprite('nt212_05', 3)	# 7-9
    SFX_0('004_swing_grap_1_2')
    Unknown7009(5)
    sprite('nt212_06', 3)	# 10-12
    sprite('nt212_07', 3)	# 13-15	 **attackbox here**
    sprite('nt212_08', 3)	# 16-18	 **attackbox here**
    sprite('nt212_09', 2)	# 19-20
    Recovery()
    Unknown2063()
    sprite('nt212_10', 1)	# 21-21
    sprite('nt212_11', 1)	# 22-22
    sprite('nt212_12', 10)	# 23-32

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('nt210_00', 5)	# 1-5
    sprite('nt210_01', 5)	# 6-10
    tag_voice(1, 'bnt156_0', 'bnt156_1', '', '')
    sprite('nt210_02', 3)	# 11-13
    sprite('nt210_03', 3)	# 14-16
    Unknown8007(100, 1, 1)
    physicsXImpulse(16000)
    Unknown1028(2000)
    sprite('nt210_04', 3)	# 17-19
    sprite('nt210_05', 3)	# 20-22
    SFX_0('004_swing_grap_1_1')
    sprite('nt210_06', 3)	# 23-25
    Unknown8000(100, 1, 1)
    Unknown1019(40)
    sprite('nt210_07', 3)	# 26-28	 **attackbox here**
    sprite('nt210_08', 4)	# 29-32
    Unknown1084(1)
    sprite('nt210_09', 3)	# 33-35
    sprite('nt210_10', 3)	# 36-38
    sprite('nt210_11', 3)	# 39-41
    sprite('nt210_12', 3)	# 42-44
    sprite('nt210_13', 2)	# 45-46

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)
    sprite('nt210_08', 3)	# 1-3
    Unknown1084(1)
    sprite('nt210_09', 3)	# 4-6
    sprite('nt210_10', 3)	# 7-9
    sprite('nt210_11', 3)	# 10-12
    sprite('nt210_12', 2)	# 13-14
    sprite('nt210_13', 2)	# 15-16
    sprite('nt340_00', 2)	# 17-18
    sprite('nt340_01', 1)	# 19-19
    sprite('nt340_02', 1)	# 20-20
    sprite('nt340_03', 1)	# 21-21
    sprite('nt340_04', 1)	# 22-22
    sprite('nt340_05', 1)	# 23-23
    sprite('nt340_06', 2)	# 24-25
    sprite('nt340_07', 2)	# 26-27
    tag_voice(0, 'bnt157_0', 'bnt157_1', '', '')
    sprite('nt340_08', 2)	# 28-29
    Unknown8003(100, 1, 1)
    sprite('nt340_09', 1)	# 30-30	 **attackbox here**
    sprite('nt340_09', 2)	# 31-32	 **attackbox here**
    sprite('nt340_10', 3)	# 33-35
    sprite('nt340_11', 3)	# 36-38
    sprite('nt340_12', 3)	# 39-41
    sprite('nt340_13', 3)	# 42-44
    sprite('nt340_14', 3)	# 45-47
    sprite('nt340_15', 3)	# 48-50
    sprite('nt340_16', 3)	# 51-53
    sprite('nt340_17', 2)	# 54-55
    sprite('nt000_00', 7)	# 56-62
    sprite('nt000_01', 7)	# 63-69
    sprite('nt000_02', 7)	# 70-76
    sprite('nt000_03', 7)	# 77-83
    sprite('nt000_04', 7)	# 84-90
    sprite('nt000_05', 7)	# 91-97
    sprite('nt000_06', 7)	# 98-104
    sprite('nt000_07', 7)	# 105-111
    sprite('nt000_08', 7)	# 112-118
    label(10)
    sprite('nt000_00', 7)	# 119-125
    sprite('nt000_01', 7)	# 126-132
    sprite('nt000_02', 7)	# 133-139
    sprite('nt000_03', 7)	# 140-146
    sprite('nt000_04', 7)	# 147-153
    sprite('nt000_05', 7)	# 154-160
    sprite('nt000_06', 7)	# 161-167
    sprite('nt000_07', 7)	# 168-174
    sprite('nt000_08', 7)	# 175-181
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 182-182

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown2004(1, 0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('nt403_01', 4)	# 1-4
    sprite('nt403_02', 5)	# 5-9
    SFX_3('ntse_03')
    Unknown8010(100, 1, 1)
    sprite('nt403_03', 5)	# 10-14
    GFX_0('ntef_403', -1)
    sprite('nt403_04', 3)	# 15-17	 **attackbox here**
    Unknown8003(100, 1, 1)
    sprite('nt403_05', 5)	# 18-22
    sprite('nt403_06', 6)	# 23-28
    sprite('nt403_07', 5)	# 29-33
    sprite('nt403_08', 5)	# 34-38
    teleportRelativeX(-40000)
    sprite('nt403_09', 5)	# 39-43
    teleportRelativeX(-40000)
    sprite('nt403_10', 4)	# 44-47
    teleportRelativeX(-40000)
    sprite('nt403_11', 4)	# 48-51
    teleportRelativeX(-40000)
    sprite('nt000_00', 1)	# 52-52
    teleportRelativeX(160000)
    sprite('nt000_00', 7)	# 53-59
    sprite('nt000_01', 7)	# 60-66
    sprite('nt000_02', 7)	# 67-73
    sprite('nt000_03', 7)	# 74-80
    sprite('nt000_04', 7)	# 81-87
    sprite('nt000_05', 7)	# 88-94
    sprite('nt000_06', 7)	# 95-101
    sprite('nt000_07', 7)	# 102-108
    sprite('nt000_08', 7)	# 109-115
    label(0)
    sprite('nt000_00', 7)	# 116-122
    sprite('nt000_01', 7)	# 123-129
    sprite('nt000_02', 7)	# 130-136
    sprite('nt000_03', 7)	# 137-143
    sprite('nt000_04', 7)	# 144-150
    sprite('nt000_05', 7)	# 151-157
    sprite('nt000_06', 7)	# 158-164
    sprite('nt000_07', 7)	# 165-171
    sprite('nt000_08', 7)	# 172-178
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 179-179

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('nt404_00', 4)	# 1-4
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_01', 5)	# 5-9
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt404_02', 5)	# 10-14
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_03', 5)	# 15-19
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_04', 3)	# 20-22	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    tag_voice(0, 'bnt158_0', 'bnt158_1', '', '')
    sprite('nt404_05', 8)	# 23-30
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 5)	# 31-35
    sprite('nt404_07', 7)	# 36-42
    sprite('nt404_08', 7)	# 43-49
    sprite('nt404_09', 5)	# 50-54
    Unknown3029(0)
    sprite('nt402_10', 4)	# 55-58
    sprite('nt402_11', 2)	# 59-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('nt000_00', 7)	# 1-7
    sprite('nt000_01', 7)	# 8-14
    sprite('nt000_02', 7)	# 15-21
    sprite('nt000_03', 7)	# 22-28
    sprite('nt000_04', 7)	# 29-35
    sprite('nt000_05', 7)	# 36-42
    sprite('nt000_06', 7)	# 43-49
    sprite('nt000_07', 7)	# 50-56
    sprite('nt000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt404_00', 4)	# 64-67
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_01', 5)	# 68-72
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt404_02', 5)	# 73-77
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_03', 5)	# 78-82
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_04', 3)	# 83-85	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    tag_voice(0, 'bnt158_0', 'bnt158_1', '', '')
    sprite('nt404_05', 8)	# 86-93
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 5)	# 94-98
    sprite('nt404_07', 7)	# 99-105
    sprite('nt404_08', 7)	# 106-112
    sprite('nt404_09', 5)	# 113-117
    Unknown3029(0)
    sprite('nt402_10', 4)	# 118-121
    sprite('nt402_11', 2)	# 122-123

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 27)	# 1-27
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 28-28
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('nt251_00', 1)	# 29-29
    physicsXImpulse(46000)
    physicsYImpulse(-15000)
    setGravity(2500)
    Unknown8001(0, 100)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('nt251_00', 4)	# 30-33
    sprite('nt251_01', 4)	# 34-37
    SFX_0('004_swing_grap_1_1')
    sprite('nt251_02', 4)	# 38-41
    Unknown1019(80)
    sprite('nt251_03', 2)	# 42-43	 **attackbox here**
    sprite('nt251_04', 2)	# 44-45	 **attackbox here**
    sprite('nt251_05', 2)	# 46-47
    sprite('nt251_06', 7)	# 48-54
    sprite('nt251_07', 7)	# 55-61
    sprite('nt251_08', 6)	# 62-67
    label(1)
    sprite('nt024_00', 3)	# 68-70
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Unknown23087(-1)
    sprite('nt024_01', 3)	# 71-73
    sprite('nt024_02', 8)	# 74-81
    sprite('nt024_03', 3)	# 82-84
    sprite('nt024_04', 3)	# 85-87
    sprite('nt000_00', 7)	# 88-94
    sprite('nt000_01', 7)	# 95-101
    sprite('nt000_02', 7)	# 102-108
    sprite('nt000_03', 7)	# 109-115
    sprite('nt000_04', 7)	# 116-122
    sprite('nt000_05', 7)	# 123-129
    sprite('nt000_06', 7)	# 130-136
    sprite('nt000_07', 7)	# 137-143
    sprite('nt000_08', 7)	# 144-150

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('nt406_00', 2)	# 1-2
    sprite('nt406_01', 2)	# 3-4
    sprite('nt406_02', 3)	# 5-7
    sprite('nt406_03', 2)	# 8-9
    SFX_0('004_swing_grap_1_2')
    sprite('nt406_04', 2)	# 10-11
    sprite('nt406_05', 3)	# 12-14	 **attackbox here**
    sprite('nt406_06', 3)	# 15-17	 **attackbox here**
    sprite('nt406_07', 3)	# 18-20
    sprite('nt406_08', 3)	# 21-23
    sprite('nt406_09', 3)	# 24-26
    sprite('nt406_10', 3)	# 27-29
    sprite('nt000_00', 7)	# 30-36
    sprite('nt000_01', 7)	# 37-43
    sprite('nt000_02', 7)	# 44-50
    sprite('nt000_03', 7)	# 51-57
    sprite('nt000_04', 7)	# 58-64
    sprite('nt000_05', 7)	# 65-71
    sprite('nt000_06', 7)	# 72-78
    sprite('nt000_07', 7)	# 79-85
    sprite('nt000_08', 7)	# 86-92

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('nt404_00', 4)	# 1-4
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_01', 5)	# 5-9
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt404_02', 5)	# 10-14
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_03', 5)	# 15-19
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_04', 3)	# 20-22	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt404_05', 8)	# 23-30
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 5)	# 31-35
    sprite('nt404_07', 7)	# 36-42
    sprite('nt404_08', 7)	# 43-49
    sprite('nt404_09', 5)	# 50-54
    Unknown3029(0)
    sprite('nt402_10', 4)	# 55-58
    sprite('nt402_11', 2)	# 59-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('nt000_00', 7)	# 1-7
    sprite('nt000_01', 7)	# 8-14
    sprite('nt000_02', 7)	# 15-21
    sprite('nt000_03', 7)	# 22-28
    sprite('nt000_04', 7)	# 29-35
    sprite('nt000_05', 7)	# 36-42
    sprite('nt000_06', 7)	# 43-49
    sprite('nt000_07', 7)	# 50-56
    sprite('nt000_08', 7)	# 57-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt404_00', 4)	# 64-67
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_01', 5)	# 68-72
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt404_02', 5)	# 73-77
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_03', 5)	# 78-82
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_04', 3)	# 83-85	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt404_05', 8)	# 86-93
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 5)	# 94-98
    sprite('nt404_07', 7)	# 99-105
    sprite('nt404_08', 7)	# 106-112
    sprite('nt404_09', 5)	# 113-117
    Unknown3029(0)
    sprite('nt402_10', 4)	# 118-121
    sprite('nt402_11', 2)	# 122-123

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
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
    sprite('nt032_00', 2)	# 1-2
    label(0)
    sprite('nt032_01', 3)	# 3-5
    sprite('nt032_02', 3)	# 6-8
    sprite('nt032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('nt032_04', 3)	# 13-15
    sprite('nt032_05', 3)	# 16-18
    sprite('nt032_06', 3)	# 19-21
    Unknown8006(100, 1, 1)
    sprite('nt032_07', 4)	# 22-25
    sprite('nt032_08', 3)	# 26-28
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt310_00', 1)	# 29-29
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('nt310_01', 2)	# 30-31
    SFX_0('010_swing_sword_0')
    sprite('nt310_02', 3)	# 32-34	 **attackbox here**
    Unknown1084(1)
    sprite('nt310_03', 3)	# 35-37
    SFX_4('bnt154')
    sprite('nt310_04', 3)	# 38-40
    sprite('nt310_05', 11)	# 41-51
    sprite('nt310_06', 3)	# 52-54
    sprite('nt310_07', 3)	# 55-57

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirUntechableTime(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown9178(1)
        AirHitstunAfterWallbounce(60)
        Unknown9362(1)
        Unknown9364(30)
        AirPushbackY(40000)
        AirPushbackX(10000)
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
    sprite('nt310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('nt311_00', 3)	# 4-6
    SFX_1('bnt153')
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('nt311_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('nt311_02', 3)	# 10-12
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('nt311_03', 3)	# 13-15
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('nt311_04', 4)	# 16-19	 **attackbox here**
    teleportRelativeX(60000)
    physicsXImpulse(12000)
    physicsYImpulse(20000)
    Unknown1043()
    EnableCollision(1)
    Unknown8001(0, 0)
    sprite('nt311_05', 4)	# 20-23	 **attackbox here**
    sprite('nt311_06', 4)	# 24-27
    sprite('nt311_07', 4)	# 28-31
    sprite('nt311_08', 32767)	# 32-32798
    label(0)
    sprite('nt024_00', 2)	# 32799-32800
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt024_01', 2)	# 32801-32802
    Unknown13014(1)
    Unknown13003(1)
    sprite('nt024_02', 2)	# 32803-32804
    sprite('nt024_03', 2)	# 32805-32806
    sprite('nt024_04', 2)	# 32807-32808

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_CLEAR_OR_EXIT():
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
    sprite('nt032_00', 2)	# 1-2
    label(0)
    sprite('nt032_01', 3)	# 3-5
    sprite('nt032_02', 3)	# 6-8
    sprite('nt032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('nt032_04', 3)	# 13-15
    sprite('nt032_05', 3)	# 16-18
    sprite('nt032_06', 3)	# 19-21
    Unknown8006(100, 1, 1)
    sprite('nt032_07', 4)	# 22-25
    sprite('nt032_08', 3)	# 26-28
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('nt310_00', 1)	# 29-29
    clearUponHandler(3)
    Unknown1019(10)
    SFX_0('010_swing_sword_0')
    sprite('nt310_01', 2)	# 30-31
    sprite('nt310_02', 3)	# 32-34	 **attackbox here**
    Unknown1084(1)
    sprite('nt310_03', 3)	# 35-37
    SFX_4('bnt154')
    sprite('nt310_04', 3)	# 38-40
    sprite('nt310_05', 11)	# 41-51
    sprite('nt310_06', 3)	# 52-54
    sprite('nt310_07', 3)	# 55-57

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(50)
        Unknown11092(1)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        hitstun(25)
        PushbackX(-4000)
        Hitstop(0)
        Unknown11069('BackThrowExe')
        JumpCancel_(0)
        Unknown13024(0)
    sprite('nt310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('nt313_00', 1)	# 4-4	 **attackbox here**
    SFX_1('bnt153')
    EnableCollision(0)
    Unknown2015(40)
    sprite('nt313_00', 4)	# 5-8	 **attackbox here**
    physicsXImpulse(60000)
    Unknown8007(100, 1, 1)
    sprite('nt313_01', 4)	# 9-12
    Unknown1019(50)
    sprite('nt313_02', 4)	# 13-16
    Unknown1019(50)
    GFX_0('BackThrow_DashStop', 0)
    sprite('nt313_03', 4)	# 17-20
    EnableCollision(1)
    Unknown1019(50)
    sprite('nt313_03', 4)	# 21-24
    Unknown1084(1)
    sprite('nt313_04', 3)	# 25-27
    physicsXImpulse(-50000)
    sprite('nt313_05', 2)	# 28-29	 **attackbox here**
    Unknown2005()
    Unknown1019(50)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown9142(30)
    Unknown9215()
    Hitstop(20)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')

    def upon_12():
        ScreenShake(8000, 0)
        JumpCancel_(1)
        Unknown13024(1)
    sprite('nt313_06', 2)	# 30-31
    Unknown1084(1)
    sprite('nt313_07', 2)	# 32-33
    sprite('nt313_08', 3)	# 34-36
    sprite('nt313_09', 3)	# 37-39
    sprite('nt340_16', 3)	# 40-42
    sprite('nt340_17', 3)	# 43-45

@Subroutine
def Dash_AfterImage():
    Unknown3029(1)
    Unknown3069(1)
    Unknown3072('ff0000000000000000000000ff000000')
    Unknown3070(3)
    Unknown3071(5)

@State
def ShortDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        physicsXImpulse(30000)
        Unknown1047(50000)
        Unknown3029(1)
        Unknown3069(1)
        Unknown8009(0)
        Unknown13015(1)
        if SLOT_60:
            callSubroutine('ExEff')
            if SLOT_59:
                Unknown13014(1)
        if SLOT_123:
            if Unknown23145('Dodge_cancel'):
                Unknown30070('53686f7274446173685f446f6467650000000000000000000000000000000000')
        loopRelated(17, 2)

        def upon_17():
            Unknown26('ntef_D_bodyaura')
            Unknown26('ntef_D_handaura_3D')
            Unknown26('ntef_D_handaura')
    sprite('nt032_02', 4)	# 1-4
    sprite('nt032_03', 4)	# 5-8
    sprite('nt032_04', 4)	# 9-12
    sprite('nt032_10', 4)	# 13-16
    Unknown1019(50)
    sprite('nt032_11', 4)	# 17-20

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(44000)
        AirPushbackX(15000)
        Unknown1112('')
        sendToLabelUpon(2, 9)
        SLOT_59 = 1
        callSubroutine('Dash_AfterImage')

        def upon_78():
            clearUponHandler(78)
            Unknown14070('AntiAir2nd')
    sprite('nt405_00', 3)	# 1-3
    sprite('nt405_01', 2)	# 4-5
    tag_voice(1, 'bnt205_0', 'bnt205_1', '', '')
    Unknown8007(100, 1, 1)
    sprite('nt405_02', 2)	# 6-7
    sprite('nt405_03', 2)	# 8-9
    SFX_3('ntse_00')
    sprite('nt405_04ex', 3)	# 10-12	 **attackbox here**
    physicsXImpulse(10000)
    GFX_0('ntef_405Test', 0)
    Unknown8001(3, 100)
    sprite('nt405_05ex', 3)	# 13-15	 **attackbox here**
    physicsXImpulse(18000)
    physicsYImpulse(40000)
    Unknown1043()
    Damage(500)
    Hitstop(3)
    YAccel(80)
    RefreshMultihit()
    sprite('nt405_06ex', 3)	# 16-18	 **attackbox here**
    physicsXImpulse(20000)
    RefreshMultihit()
    sprite('nt405_05ex', 2)	# 19-20	 **attackbox here**
    Hitstop(3)
    setInvincible(0)
    RefreshMultihit()
    sprite('nt405_06ex', 2)	# 21-22	 **attackbox here**
    AirPushbackY(32000)
    RefreshMultihit()
    sprite('nt405_07', 2)	# 23-24
    Unknown21015('6e7465665f343035546573740000000000000000000000000000000000000000ec03000000000000')
    sprite('nt405_08', 3)	# 25-27
    Unknown14072('AntiAir2nd')
    sprite('nt405_09', 2)	# 28-29
    sprite('nt405_10', 2)	# 30-31
    sprite('nt405_11', 2)	# 32-33
    sprite('nt405_12', 3)	# 34-36
    sprite('nt405_13', 2)	# 37-38
    Unknown14073('AntiAir2nd')
    sprite('nt405_14', 3)	# 39-41
    Unknown3029(0)
    label(0)
    sprite('nt020_07', 4)	# 42-45
    sprite('nt020_08', 4)	# 46-49
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)	# 50-51
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown3029(0)
    sprite('nt024_01', 8)	# 52-59
    sprite('nt024_02', 2)	# 60-61
    sprite('nt024_03', 2)	# 62-63
    sprite('nt024_04', 2)	# 64-65

@State
def AN_CmnActInvincibleAttack_cance():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(44000)
        physicsXImpulse(20000)
        sendToLabelUpon(2, 9)
        SLOT_59 = 0

        def upon_78():
            clearUponHandler(78)
            Unknown14070('AntiAir2nd')
        Unknown30070('436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
        Unknown23159('AN_CmnActInvincibleAttack_cance')
    sprite('nt405_00', 3)	# 1-3
    sprite('nt405_01', 2)	# 4-5
    tag_voice(1, 'bnt205_0', 'bnt205_1', '', '')
    Unknown1019(50)
    Unknown8007(100, 1, 1)
    sprite('nt405_02', 2)	# 6-7
    sprite('nt405_03', 2)	# 8-9
    SFX_3('ntse_00')
    Unknown1019(50)
    sprite('nt405_04ex', 3)	# 10-12	 **attackbox here**
    GFX_0('ntef_405Test', 0)
    Unknown8001(3, 100)
    sprite('nt405_05ex', 3)	# 13-15	 **attackbox here**
    Unknown1019(50)
    physicsYImpulse(40000)
    Unknown1043()
    RefreshMultihit()
    sprite('nt405_06ex', 3)	# 16-18	 **attackbox here**
    sprite('nt405_05ex', 2)	# 19-20	 **attackbox here**
    setInvincible(0)
    sprite('nt405_06ex', 2)	# 21-22	 **attackbox here**
    AirPushbackY(32000)
    sprite('nt405_07', 2)	# 23-24
    Unknown21015('6e7465665f343035546573740000000000000000000000000000000000000000ec03000000000000')
    sprite('nt405_08', 3)	# 25-27
    Unknown14072('AntiAir2nd')
    sprite('nt405_09', 2)	# 28-29
    sprite('nt405_10', 2)	# 30-31
    sprite('nt405_11', 2)	# 32-33
    sprite('nt405_12', 3)	# 34-36
    sprite('nt405_13', 2)	# 37-38
    Unknown14073('AntiAir2nd')
    sprite('nt405_14', 2)	# 39-40
    Unknown3029(0)
    sprite('nt405_14', 1)	# 41-41
    label(0)
    sprite('nt020_07', 4)	# 42-45
    sprite('nt020_08', 4)	# 46-49
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)	# 50-51
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown3029(0)
    sprite('nt024_01', 8)	# 52-59
    sprite('nt024_02', 2)	# 60-61
    sprite('nt024_03', 2)	# 62-63
    sprite('nt024_04', 2)	# 64-65

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(23000)
        AirPushbackY(38000)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown1007(80000)
        Unknown1019(0)
        YAccel(0)
        Unknown1039(0)
        SLOT_59 = 1
        callSubroutine('Dash_AfterImage')

        def upon_78():
            clearUponHandler(78)
            Unknown14070('AntiAir2nd')
    sprite('nt405_01', 2)	# 1-2
    tag_voice(1, 'bnt207_0', 'bnt207_1', '', '')
    sprite('nt405_02', 2)	# 3-4
    physicsXImpulse(25000)
    sprite('nt405_03', 2)	# 5-6
    SFX_3('ntse_00')
    Unknown1019(50)
    sprite('nt405_04ex', 2)	# 7-8	 **attackbox here**
    GFX_0('ntef_405AirTest', 0)
    Unknown1019(50)
    physicsYImpulse(40000)
    Unknown1043()
    sprite('nt405_05ex', 2)	# 9-10	 **attackbox here**
    Damage(400)
    Hitstop(3)
    Unknown1019(300)
    YAccel(80)
    RefreshMultihit()
    sprite('nt405_06ex', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    sprite('nt405_05ex', 2)	# 13-14	 **attackbox here**
    Unknown1019(80)
    setInvincible(0)
    RefreshMultihit()
    sprite('nt405_06ex', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('nt405_07', 2)	# 17-18
    Unknown21015('6e7465665f343035416972546573740000000000000000000000000000000000ed03000000000000')
    sprite('nt405_08', 3)	# 19-21
    Unknown14072('AntiAir2nd')
    sprite('nt405_09', 2)	# 22-23
    sprite('nt405_10', 2)	# 24-25
    sprite('nt405_11', 2)	# 26-27
    sprite('nt405_12', 3)	# 28-30
    sprite('nt405_13', 2)	# 31-32
    Unknown14073('AntiAir2nd')
    sprite('nt405_14', 3)	# 33-35
    label(0)
    sprite('nt020_07', 4)	# 36-39
    sprite('nt020_08', 4)	# 40-43
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)	# 44-45
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt024_01', 8)	# 46-53
    sprite('nt024_02', 2)	# 54-55
    sprite('nt024_03', 2)	# 56-57
    sprite('nt024_04', 2)	# 58-59

@State
def AN_CmnActInvincibleAttackAir_ca():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        AirUntechableTime(45)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(44000)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        Unknown1007(80000)
        Unknown1019(0)
        YAccel(0)
        Unknown1039(0)
        SLOT_59 = 0

        def upon_78():
            clearUponHandler(78)
            Unknown14070('AntiAir2nd')
        Unknown30070('436d6e416374496e76696e6369626c6541747461636b41697200000000000000')
        Unknown23159('AN_CmnActInvincibleAttackAir_ca')
    sprite('nt405_01', 2)	# 1-2
    tag_voice(1, 'bnt207_0', 'bnt207_1', '', '')
    sprite('nt405_02', 2)	# 3-4
    physicsXImpulse(20000)
    sprite('nt405_03', 2)	# 5-6
    SFX_3('ntse_00')
    Unknown1019(50)
    sprite('nt405_04ex', 2)	# 7-8	 **attackbox here**
    GFX_0('ntef_405AirTest', 0)
    Unknown1019(50)
    physicsYImpulse(40000)
    Unknown1043()
    sprite('nt405_05ex', 2)	# 9-10	 **attackbox here**
    sprite('nt405_06ex', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    sprite('nt405_05ex', 2)	# 13-14	 **attackbox here**
    setInvincible(0)
    sprite('nt405_06ex', 2)	# 15-16	 **attackbox here**
    sprite('nt405_07', 2)	# 17-18
    Unknown21015('6e7465665f343035416972546573740000000000000000000000000000000000ed03000000000000')
    sprite('nt405_08', 3)	# 19-21
    Unknown14072('AntiAir2nd')
    sprite('nt405_09', 2)	# 22-23
    sprite('nt405_10', 2)	# 24-25
    sprite('nt405_11', 2)	# 26-27
    sprite('nt405_12', 3)	# 28-30
    sprite('nt405_13', 2)	# 31-32
    Unknown14073('AntiAir2nd')
    sprite('nt405_14', 3)	# 33-35
    label(0)
    sprite('nt020_07', 4)	# 36-39
    sprite('nt020_08', 4)	# 40-43
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 2)	# 44-45
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt024_01', 8)	# 46-53
    sprite('nt024_02', 2)	# 54-55
    sprite('nt024_03', 2)	# 56-57
    sprite('nt024_04', 2)	# 58-59

@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1300)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(40)
        AttackP1(48)
        AttackP2(100)
        AirPushbackY(-40000)
        Unknown9310(1)
        Unknown30087(0)
        setInvincible(0)
        Unknown30068(1)
        Unknown14083(0)
        Unknown11056(0)
        Unknown1045(0)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
            Unknown1015(3000)
            Unknown1028(-400)
            Unknown1021(12000)
            setGravity(1800)
            AirPushbackX(15000)
        else:
            Unknown1015(8000)
            Unknown1028(-400)
            physicsYImpulse(22000)
            setGravity(1800)

        def upon_12():
            Unknown22004(17, 1)
    sprite('nt406_00', 2)	# 1-2
    sprite('nt406_01', 2)	# 3-4
    sprite('nt406_02', 2)	# 5-6
    sprite('nt406_03', 2)	# 7-8
    SFX_0('004_swing_grap_1_2')
    sprite('nt406_04', 2)	# 9-10
    sprite('nt406_05', 3)	# 11-13	 **attackbox here**
    tag_voice(0, 'bnt206_0', 'bnt206_1', '', '')
    sprite('nt406_06', 3)	# 14-16	 **attackbox here**
    sprite('nt406_07', 3)	# 17-19
    Unknown1028(0)
    Recovery()
    sprite('nt406_08', 3)	# 20-22
    sprite('nt406_09', 3)	# 23-25
    sprite('nt406_10', 3)	# 26-28
    Unknown3029(0)
    label(0)
    sprite('nt020_07', 3)	# 29-31
    sprite('nt020_08', 3)	# 32-34
    loopRest()
    gotoLabel(0)

@State
def Assault_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1300)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Hitstop(15)
        PushbackX(24800)
        Unknown11056(0)
        WhiffCancel('Assault_2nd_A')
        HitOrBlockCancel('Assault_2nd_A')
        Hitstop(15)
        physicsXImpulse(40000)
        callSubroutine('Dash_AfterImage')
        SLOT_59 = 1
        SLOT_60 = 0
    sprite('nt400_00', 2)	# 1-2
    Unknown2016(300)
    sprite('nt400_01', 1)	# 3-3
    Unknown1019(120)
    sprite('nt400_01', 2)	# 4-5
    Unknown8007(100, 1, 1)
    if (not Unknown23145('ShortDash')):
        Unknown8009(0)
    tag_voice(1, 'bnt200_0', 'bnt200_1', 'bnt200_2', '')
    sprite('nt400_02', 3)	# 6-8
    SFX_0('004_swing_grap_1_1')
    sprite('nt400_03', 3)	# 9-11
    GFX_0('ntef_400_aura', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('nt400_04', 3)	# 12-14	 **attackbox here**
    Unknown2016(-1)
    sprite('nt400_05', 2)	# 15-16
    WhiffCancelEnable(1)
    Recovery()
    Unknown1019(10)
    sprite('nt400_06', 3)	# 17-19
    Unknown3029(0)
    sprite('nt400_07', 3)	# 20-22
    Unknown14077(0)
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    WhiffCancelEnable(0)
    sprite('nt400_10', 3)	# 29-31

@State
def Assault_cancel_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Hitstop(15)
        PushbackX(24800)
        Unknown11056(0)
        WhiffCancel('Assault_2nd_A')
        HitOrBlockCancel('Assault_2nd_A')
        physicsXImpulse(20000)
        SLOT_59 = 0
        SLOT_60 = 0
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('nt400_00', 2)	# 1-2
    Unknown2016(300)
    sprite('nt400_01', 1)	# 3-3
    sprite('nt400_01', 2)	# 4-5
    Unknown8007(100, 1, 1)
    tag_voice(1, 'bnt200_0', 'bnt200_1', 'bnt200_2', '')
    sprite('nt400_02', 3)	# 6-8
    SFX_0('004_swing_grap_1_1')
    sprite('nt400_03', 3)	# 9-11
    GFX_0('ntef_400_aura', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('nt400_04', 3)	# 12-14	 **attackbox here**
    Unknown2016(-1)
    sprite('nt400_05', 2)	# 15-16
    WhiffCancelEnable(1)
    Recovery()
    Unknown1019(10)
    sprite('nt400_06', 3)	# 17-19
    Unknown3029(0)
    sprite('nt400_07', 3)	# 20-22
    Unknown14077(0)
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    WhiffCancelEnable(0)
    sprite('nt400_10', 3)	# 29-31

@State
def Assault_2nd_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AirPushbackX(15000)
        AirPushbackY(-30000)
        AttackP1(64)
        AttackP2(100)
        AirUntechableTime(28)
        Hitstop(15)
        Unknown9202(5)
        Unknown11056(0)
        Unknown30068(1)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
            Damage(1300)
        WhiffCancel('Assault_3rdYoko')
        HitOrBlockCancel('Assault_3rdYoko')
        sendToLabelUpon(2, 9)
    sprite('nt401_00', 2)	# 1-2
    physicsXImpulse(50000)
    physicsYImpulse(6000)
    setGravity(2500)
    Unknown2016(300)
    Unknown8007(100, 1, 1)
    sprite('nt401_00', 2)	# 3-4
    Unknown1019(50)
    sprite('nt401_01', 2)	# 5-6
    tag_voice(0, 'bnt201_0', 'bnt201_1', 'bnt201_2', '')
    SFX_3('ntse_02')
    GFX_0('ntef_401_aura1', -1)
    Unknown1019(50)
    sprite('nt401_01', 32767)	# 7-32773
    Unknown1019(50)
    loopRest()
    label(9)
    sprite('nt401_02', 3)	# 32774-32776	 **attackbox here**
    Unknown26('ntef_401_aura1')
    GFX_0('ntef_401_aura2', -1)
    Unknown2015(150)
    teleportRelativeX(100000)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt401_03', 3)	# 32777-32779	 **attackbox here**
    Unknown2016(-1)
    WhiffCancelEnable(1)
    Unknown3029(0)
    sprite('nt401_04', 5)	# 32780-32784
    Recovery()
    Unknown14077(0)
    sprite('nt401_05', 4)	# 32785-32788
    sprite('nt401_06', 3)	# 32789-32791
    sprite('nt401_06', 2)	# 32792-32793
    WhiffCancelEnable(0)
    sprite('nt401_07', 4)	# 32794-32797

@State
def Assault_3rdYoko():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(80)
        AirUntechableTime(40)
        GroundedHitstunAnimation(1)
        AirPushbackX(42000)
        AirPushbackY(16000)
        Unknown11056(0)
        Unknown30068(1)
        if SLOT_59:
            GroundedHitstunAnimation(18)
            AirHitstunAnimation(18)
            Damage(2000)

            def upon_78():
                Unknown14070('ShortDash')
            callSubroutine('Dash_AfterImage')
    sprite('nt402_00', 2)	# 1-2
    sprite('nt402_01', 2)	# 3-4
    sprite('nt402_02', 3)	# 5-7
    physicsXImpulse(4000)
    if SLOT_59:
        Unknown1015(1000)
    sprite('nt402_03', 3)	# 8-10
    Unknown1019(200)
    Unknown8006(100, 1, 1)
    sprite('nt402_04', 3)	# 11-13
    SFX_3('ntse_03')
    GFX_0('ntef_402', -1)
    Unknown1019(300)
    Unknown2015(150)
    Unknown8006(100, 1, 1)
    sprite('nt402_05', 3)	# 14-16	 **attackbox here**
    tag_voice(0, 'bnt202_0', 'bnt202_1', 'bnt202_2', '')
    Unknown1019(150)
    Unknown2015(200)
    Unknown8007(100, 1, 1)
    sprite('nt402_06', 4)	# 17-20	 **attackbox here**
    sprite('nt402_07', 3)	# 21-23
    Unknown2015(-1)
    Recovery()
    loopRest()
    label(9)
    sprite('nt402_08', 4)	# 24-27
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    Unknown14072('ShortDash')
    Unknown3029(0)
    sprite('nt402_09', 4)	# 28-31
    Unknown1084(1)
    WhiffCancelEnable(0)
    sprite('nt402_10', 7)	# 32-38
    sprite('nt402_11', 4)	# 39-42
    Unknown14073('ShortDash')

@State
def Assault_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1300)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Hitstop(15)
        PushbackX(24800)
        Unknown11056(0)
        WhiffCancel('Assault_2nd_B')
        HitOrBlockCancel('Assault_2nd_B')
        Hitstop(15)
        callSubroutine('Dash_AfterImage')
        SLOT_59 = 1
        SLOT_60 = 0
    sprite('nt032_00', 3)	# 1-3
    Unknown2016(300)
    sprite('nt400_00', 3)	# 4-6
    tag_voice(1, 'bnt200_0', 'bnt200_1', 'bnt200_2', '')
    Unknown8007(100, 1, 1)
    physicsXImpulse(40000)
    if (not Unknown23145('ShortDash')):
        Unknown8009(0)
    sprite('nt400_01', 4)	# 7-10
    Unknown1019(120)
    sprite('nt400_02', 4)	# 11-14
    SFX_0('004_swing_grap_1_1')
    sprite('nt400_03', 3)	# 15-17
    GFX_0('ntef_400_aura', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('nt400_04', 3)	# 18-20	 **attackbox here**
    Unknown2016(-1)
    sprite('nt400_05', 2)	# 21-22
    WhiffCancelEnable(1)
    Recovery()
    Unknown1019(10)
    sprite('nt400_06', 3)	# 23-25
    Unknown3029(0)
    sprite('nt400_07', 3)	# 26-28
    Unknown14077(0)
    sprite('nt400_08', 3)	# 29-31
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 32-34
    WhiffCancelEnable(0)
    sprite('nt400_10', 3)	# 35-37

@State
def Assault_cancel_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Hitstop(15)
        PushbackX(24800)
        Unknown11056(0)
        WhiffCancel('Assault_2nd_B')
        HitOrBlockCancel('Assault_2nd_B')
        SLOT_59 = 0
        SLOT_60 = 0
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('nt032_00', 3)	# 1-3
    Unknown2016(300)
    sprite('nt400_00', 3)	# 4-6
    tag_voice(1, 'bnt200_0', 'bnt200_1', 'bnt200_2', '')
    Unknown8007(100, 1, 1)
    physicsXImpulse(20000)
    sprite('nt400_01', 4)	# 7-10
    sprite('nt400_02', 4)	# 11-14
    SFX_0('004_swing_grap_1_1')
    sprite('nt400_03', 3)	# 15-17
    GFX_0('ntef_400_aura', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('nt400_04', 3)	# 18-20	 **attackbox here**
    Unknown2016(-1)
    sprite('nt400_05', 2)	# 21-22
    WhiffCancelEnable(1)
    Recovery()
    Unknown1019(10)
    sprite('nt400_06', 3)	# 23-25
    Unknown3029(0)
    sprite('nt400_07', 3)	# 26-28
    Unknown14077(0)
    sprite('nt400_08', 3)	# 29-31
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 32-34
    WhiffCancelEnable(0)
    sprite('nt400_10', 3)	# 35-37

@State
def Assault_2nd_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AirPushbackX(15000)
        AirPushbackY(-30000)
        AttackP1(64)
        AttackP2(100)
        AirUntechableTime(28)
        Hitstop(15)
        Unknown9202(5)
        Unknown11056(0)
        Unknown30068(1)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
            Damage(1300)
        WhiffCancel('Assault_3rdTate')
        HitOrBlockCancel('Assault_3rdTate')
        sendToLabelUpon(2, 9)
    sprite('nt401_00', 2)	# 1-2
    physicsXImpulse(50000)
    physicsYImpulse(6000)
    setGravity(2500)
    Unknown2016(300)
    Unknown8007(100, 1, 1)
    sprite('nt401_00', 2)	# 3-4
    Unknown1019(50)
    sprite('nt401_01', 2)	# 5-6
    tag_voice(0, 'bnt201_0', 'bnt201_1', 'bnt201_2', '')
    SFX_3('ntse_02')
    GFX_0('ntef_401_aura1', -1)
    Unknown1019(50)
    sprite('nt401_01', 32767)	# 7-32773
    Unknown1019(50)
    loopRest()
    label(9)
    sprite('nt401_02', 3)	# 32774-32776	 **attackbox here**
    Unknown26('ntef_401_aura1')
    GFX_0('ntef_401_aura2', -1)
    Unknown2015(150)
    teleportRelativeX(100000)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt401_03', 3)	# 32777-32779	 **attackbox here**
    Unknown2016(-1)
    WhiffCancelEnable(1)
    Unknown3029(0)
    sprite('nt401_04', 5)	# 32780-32784
    Recovery()
    Unknown14077(0)
    sprite('nt401_05', 4)	# 32785-32788
    sprite('nt401_06', 3)	# 32789-32791
    sprite('nt401_06', 2)	# 32792-32793
    WhiffCancelEnable(0)
    sprite('nt401_07', 4)	# 32794-32797

@State
def Assault_3rdTate():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(80)
        AttackP2(75)
        AirUntechableTime(17)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(32000)
        Hitstop(18)
        Unknown30068(1)
        HitJumpCancel(1)
        Unknown2004(1, 0)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
            Damage(2000)
            HitOrBlockJumpCancel(1)
            AirUntechableTime(25)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('nt403_00', 2)	# 2-3
    physicsXImpulse(2000)
    Unknown1019(200)
    sprite('nt403_01', 2)	# 4-5
    Unknown1019(200)
    Unknown8007(100, 1, 1)
    sprite('nt403_01', 2)	# 6-7
    Unknown1019(300)
    Unknown8007(100, 1, 1)
    sprite('nt403_01', 2)	# 8-9
    Unknown1019(400)
    sprite('nt403_02', 1)	# 10-10
    tag_voice(0, 'bnt203_0', 'bnt203_1', 'bnt203_2', '')
    Unknown1019(50)
    sprite('nt403_02', 1)	# 11-11
    SFX_3('ntse_03')
    Unknown8010(100, 1, 1)
    Unknown1019(50)
    sprite('nt403_03', 2)	# 12-13
    GFX_0('ntef_403', -1)
    Unknown1019(20)
    sprite('nt403_04', 8)	# 14-21	 **attackbox here**
    Unknown8003(100, 1, 1)
    ScreenShake(5000, 10000)
    Unknown1084(1)
    Unknown3029(0)
    sprite('nt403_05', 3)	# 22-24
    Recovery()
    sprite('nt403_06', 7)	# 25-31
    sprite('nt403_07', 4)	# 32-35
    sprite('nt403_08', 4)	# 36-39
    sprite('nt403_09', 4)	# 40-43
    sprite('nt403_10', 4)	# 44-47
    sprite('nt403_11', 4)	# 48-51

@State
def Assault_cancel_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Hitstop(15)
        PushbackX(24800)
        MinimumDamagePct(10)
        Unknown11056(0)
        Unknown30065(0)
        WhiffCancel('Assault_2nd_EX')
        HitOrBlockCancel('Assault_2nd_EX')
        Hitstop(15)
        physicsXImpulse(40000)
        callSubroutine('Dash_AfterImage')
        SLOT_59 = 0
        SLOT_60 = 1
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('nt400_00', 2)	# 1-2
    Unknown2016(300)
    sprite('nt400_01', 1)	# 3-3
    Unknown1019(120)
    sprite('nt400_01', 2)	# 4-5
    Unknown8007(100, 1, 1)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    tag_voice(1, 'bnt200_0', 'bnt200_1', 'bnt200_2', '')
    if (not Unknown23145('ShortDash')):
        Unknown8009(0)
    sprite('nt400_02', 3)	# 6-8
    SFX_0('004_swing_grap_1_1')
    sprite('nt400_03', 3)	# 9-11
    GFX_0('ntef_400_aura', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('nt400_04', 3)	# 12-14	 **attackbox here**
    Unknown2016(-1)
    sprite('nt400_05', 2)	# 15-16
    WhiffCancelEnable(1)
    Recovery()
    Unknown1019(10)
    sprite('nt400_06', 3)	# 17-19
    Unknown3029(0)
    sprite('nt400_07', 3)	# 20-22
    Unknown14077(0)
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    WhiffCancelEnable(0)
    sprite('nt400_10', 3)	# 29-31

@State
def Assault_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1300)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(5000)
        Hitstop(15)
        PushbackX(24800)
        MinimumDamagePct(10)
        Unknown11056(0)
        Unknown30065(0)
        WhiffCancel('Assault_2nd_EX')
        HitOrBlockCancel('Assault_2nd_EX')
        Hitstop(15)
        physicsXImpulse(40000)
        callSubroutine('Dash_AfterImage')
        SLOT_59 = 1
        SLOT_60 = 1
    sprite('nt400_00', 2)	# 1-2
    Unknown2016(300)
    sprite('nt400_01', 1)	# 3-3
    Unknown1019(150)
    sprite('nt400_01', 2)	# 4-5
    Unknown8007(100, 1, 1)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    tag_voice(1, 'bnt200_0', 'bnt200_1', 'bnt200_2', '')
    callSubroutine('Dash_AfterImage')
    if (not Unknown23145('ShortDash')):
        Unknown8009(0)
    sprite('nt400_02', 3)	# 6-8
    SFX_0('004_swing_grap_1_1')
    sprite('nt400_03', 3)	# 9-11
    GFX_0('ntef_400_aura', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 1)
    sprite('nt400_04', 3)	# 12-14	 **attackbox here**
    Unknown2016(-1)
    sprite('nt400_05', 2)	# 15-16
    WhiffCancelEnable(1)
    Recovery()
    Unknown1019(10)
    sprite('nt400_06', 3)	# 17-19
    Unknown3029(0)
    sprite('nt400_07', 3)	# 20-22
    Unknown14077(0)
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    WhiffCancelEnable(0)
    sprite('nt400_10', 3)	# 29-31

@Subroutine
def ExEff():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown3074('000000000400000032000000a0000000')
    Unknown3075('00000000000000000000000010000000')
    Unknown3076(1010)
    Unknown3077(900)

@State
def Assault_2nd_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1100)
        AirPushbackX(15000)
        AirPushbackY(-30000)
        AttackP1(64)
        AttackP2(100)
        AirUntechableTime(28)
        Hitstop(15)
        Unknown9202(5)
        MinimumDamagePct(10)
        Unknown11056(0)
        Unknown30068(1)
        Unknown30065(0)
        callSubroutine('ExEff')
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
            Damage(1300)
        WhiffCancel('Assault_3rdYoko_EX')
        HitOrBlockCancel('Assault_3rdYoko_EX')
        sendToLabelUpon(2, 9)
    sprite('nt401_00', 2)	# 1-2
    physicsXImpulse(50000)
    physicsYImpulse(6000)
    setGravity(2500)
    Unknown2016(300)
    Unknown8007(100, 1, 1)
    sprite('nt401_00', 2)	# 3-4
    Unknown1019(50)
    sprite('nt401_01', 2)	# 5-6
    tag_voice(0, 'bnt201_0', 'bnt201_1', 'bnt201_2', '')
    SFX_3('ntse_02')
    GFX_0('ntef_401_aura1', -1)
    Unknown1019(50)
    sprite('nt401_01', 32767)	# 7-32773
    Unknown1019(50)
    loopRest()
    label(9)
    sprite('nt401_02', 3)	# 32774-32776	 **attackbox here**
    Unknown26('ntef_401_aura1')
    GFX_0('ntef_401_aura2', -1)
    Unknown2015(150)
    teleportRelativeX(100000)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt401_03', 3)	# 32777-32779	 **attackbox here**
    Unknown2016(-1)
    WhiffCancelEnable(1)
    Unknown3029(0)
    sprite('nt401_04', 5)	# 32780-32784
    Recovery()
    Unknown14077(0)
    sprite('nt401_05', 4)	# 32785-32788
    sprite('nt401_06', 3)	# 32789-32791
    sprite('nt401_06', 2)	# 32792-32793
    WhiffCancelEnable(0)
    sprite('nt401_07', 4)	# 32794-32797

@State
def Assault_3rdYoko_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AttackP2(85)
        AirUntechableTime(40)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(42000)
        AirPushbackY(16000)
        MinimumDamagePct(10)
        Unknown11056(0)
        Unknown30068(1)
        Unknown30065(0)
        callSubroutine('ExEff')
        if SLOT_59:
            AirPushbackX(85000)
            AirPushbackY(5000)
            YImpluseBeforeWallbounce(300)
            AirUntechableTime(70)
            GroundedHitstunAnimation(12)
            AirHitstunAnimation(12)
            WallbounceReboundTime(1)
            Damage(2300)
            callSubroutine('Dash_AfterImage')

        def upon_11():
            Unknown14070('ShortDash')
    sprite('nt402_00', 2)	# 1-2
    sprite('nt402_01', 2)	# 3-4
    sprite('nt402_02', 3)	# 5-7
    physicsXImpulse(4000)
    Unknown1015(1000)
    sprite('nt402_03', 3)	# 8-10
    Unknown1019(200)
    Unknown8006(100, 1, 1)
    sprite('nt402_04', 3)	# 11-13
    SFX_3('ntse_03')
    GFX_0('ntef_402', -1)
    Unknown1019(300)
    Unknown2015(150)
    Unknown8006(100, 1, 1)
    sprite('nt402_05', 3)	# 14-16	 **attackbox here**
    tag_voice(0, 'bnt202_0', 'bnt202_1', 'bnt202_2', '')
    Unknown1019(150)
    Unknown2015(200)
    Unknown8007(100, 1, 1)
    sprite('nt402_06', 4)	# 17-20	 **attackbox here**
    sprite('nt402_07', 3)	# 21-23
    Unknown2015(-1)
    Recovery()
    loopRest()
    label(9)
    sprite('nt402_08', 4)	# 24-27
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    Unknown14072('ShortDash')
    Unknown3029(0)
    sprite('nt402_09', 4)	# 28-31
    Unknown1084(1)
    sprite('nt402_10', 7)	# 32-38
    sprite('nt402_11', 4)	# 39-42
    Unknown14073('ShortDash')

@State
def Assault_3rdTate_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        AirUntechableTime(30)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(30000)
        Hitstop(18)
        MinimumDamagePct(10)
        Unknown30068(1)
        Unknown30065(0)
        HitJumpCancel(1)
        Unknown2004(1, 0)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        callSubroutine('ExEff')
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('nt403_00', 2)	# 2-3
    physicsXImpulse(2000)
    Unknown1019(200)
    sprite('nt403_01', 2)	# 4-5
    Unknown1019(200)
    Unknown8007(100, 1, 1)
    sprite('nt403_01', 2)	# 6-7
    Unknown1019(300)
    Unknown8007(100, 1, 1)
    sprite('nt403_01', 2)	# 8-9
    Unknown1019(400)
    sprite('nt403_02', 1)	# 10-10
    tag_voice(0, 'bnt203_0', 'bnt203_1', 'bnt203_2', '')
    Unknown1019(50)
    sprite('nt403_02', 1)	# 11-11
    SFX_3('ntse_03')
    Unknown8010(100, 1, 1)
    Unknown1019(50)
    sprite('nt403_03', 2)	# 12-13
    GFX_0('ntef_403', -1)
    Unknown1019(20)
    sprite('nt403_04', 8)	# 14-21	 **attackbox here**
    Unknown8003(100, 1, 1)
    ScreenShake(5000, 10000)
    Unknown1084(1)
    Unknown3029(0)
    sprite('nt403_05', 3)	# 22-24
    Recovery()
    sprite('nt403_06', 7)	# 25-31
    sprite('nt403_07', 4)	# 32-35
    sprite('nt403_08', 4)	# 36-39
    sprite('nt403_09', 4)	# 40-43
    sprite('nt403_10', 4)	# 44-47
    sprite('nt403_11', 4)	# 48-51

@State
def EdgeAssault_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        blockstun(17)
        AirHitstunAnimation(13)
        AirPushbackY(33000)
        AirPushbackX(16000)
        AirUntechableTime(25)
        Hitstop(7)
        Unknown9016(1)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
    sprite('nt404_00', 4)	# 1-4
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_01', 4)	# 5-8
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt404_02', 2)	# 9-10
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown7007('626e743230345f30000000000000000064000000626e743230345f31000000000000000064000000626e743230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('nt404_03', 2)	# 11-12
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt404_04', 3)	# 13-15	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt404_05', 3)	# 16-18
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 3)	# 19-21
    sprite('nt404_07', 4)	# 22-25
    Unknown1019(30)
    EnableCollision(1)
    sprite('nt404_08', 4)	# 26-29
    Unknown1019(30)
    sprite('nt404_09', 4)	# 30-33
    Unknown3029(0)
    Unknown1019(30)
    sprite('nt402_10', 3)	# 34-36
    Unknown1019(30)
    sprite('nt402_11', 2)	# 37-38
    Unknown1019(0)

@State
def EdgeAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2300)
        AttackP1(80)
        AttackP2(75)
        blockstun(21)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9130(19)
        Unknown9142(18)
        AirPushbackY(28000)
        AirPushbackX(16000)
        PushbackX(12000)
        AirUntechableTime(27)
        Hitstop(12)
        Unknown9016(1)
        Unknown11001(0, 3, 8)
        callSubroutine('Dash_AfterImage')
    sprite('nt032_00', 4)	# 1-4
    sprite('nt404_00', 5)	# 5-9
    physicsXImpulse(4000)
    GFX_1('ntef_D_aura', 0)
    Unknown8010(100, 1, 0)
    sprite('nt404_01', 5)	# 10-14
    SFX_3('ntse_04')
    GFX_1('ntef_D_aura', 0)
    Unknown1019(120)
    sprite('nt404_02', 3)	# 15-17
    Unknown7006('bnt204_0', 100, 846491234, 828322864, 0, 0, 100, 846491234, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown1019(300)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown8007(100, 1, 1)
    sprite('nt404_03', 2)	# 18-19
    Unknown1019(400)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown8009(0)
    sprite('nt404_04', 3)	# 20-22	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    if (SLOT_19 <= 200000):
        Unknown48('190000000200000033000000160000000200000025000000')
    sprite('nt404_05', 1)	# 23-23
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 1)	# 24-24
    Unknown1019(70)
    Unknown3029(0)
    loopRest()
    sprite('nt404_07', 3)	# 25-27
    Unknown1019(50)
    EnableCollision(1)
    sprite('nt404_08', 3)	# 28-30
    Unknown1019(50)
    sprite('nt404_09', 3)	# 31-33
    Unknown3029(0)
    Unknown1019(30)
    sprite('nt402_10', 3)	# 34-36
    Unknown1019(30)
    sprite('nt402_11', 2)	# 37-38
    Unknown1019(0)

@State
def EdgeAssault_cancel_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2300)
        AttackP1(80)
        AttackP2(75)
        blockstun(21)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9130(19)
        Unknown9142(18)
        AirPushbackY(28000)
        AirPushbackX(16000)
        PushbackX(12000)
        AirUntechableTime(27)
        Hitstop(12)
        Unknown9016(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11001(0, 3, 8)
    SLOT_4 = 1

    def upon_STATE_END():
        SLOT_4 = 0
sprite('nt032_00', 3)	# 1-3
sprite('nt404_00', 4)	# 4-7
physicsXImpulse(4000)
GFX_1('ntef_D_aura', 0)
Unknown8010(100, 1, 0)
Unknown23125('')
ConsumeSuperMeter(-5000)
sprite('nt404_01', 4)	# 8-11
SFX_3('ntse_04')
GFX_1('ntef_D_aura', 0)
Unknown1019(120)
sprite('nt404_02', 2)	# 12-13
Unknown7007('626e743230345f30000000000000000064000000626e743230345f31000000000000000064000000626e743230345f320000000000000000640000000000000000000000000000000000000000000000')
Unknown1019(300)
GFX_1('ntef_D_aura', 0)
GFX_1('ntef_D_aura', 1)
Unknown8007(100, 1, 1)
sprite('nt404_03', 2)	# 14-15
Unknown1019(400)
GFX_1('ntef_D_aura', 0)
GFX_1('ntef_D_aura', 1)
Unknown8009(0)
sprite('nt404_04', 3)	# 16-18	 **attackbox here**
GFX_1('ntef_D_aura', 0)
GFX_1('ntef_D_aura', 1)
GFX_1('ntef_D_aura', 2)
GFX_1('ntef_D_aura', 3)
GFX_1('ntef_D_aura', 4)
GFX_1('ntef_D_aura', 5)
if (SLOT_19 <= 200000):
    Unknown48('190000000200000033000000160000000200000025000000')
sprite('nt404_05', 1)	# 19-19
GFX_1('ntef_D_aura', 0)
GFX_1('ntef_D_aura', 1)
GFX_1('ntef_D_aura', 2)
GFX_1('ntef_D_aura', 3)
Recovery()
sprite('nt404_06', 1)	# 20-20
Unknown1019(70)
Unknown3029(0)
loopRest()
sprite('nt404_07', 3)	# 21-23
Unknown1019(50)
EnableCollision(1)
sprite('nt404_08', 3)	# 24-26
Unknown1019(50)
sprite('nt404_09', 3)	# 27-29
Unknown3029(0)
Unknown1019(30)
sprite('nt402_10', 3)	# 30-32
Unknown1019(30)
sprite('nt402_11', 2)	# 33-34
Unknown1019(0)
endState()

@State
def EdgeAssault_EX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2600)
        AttackP1(80)
        AttackP2(75)
        blockstun(21)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9130(36)
        Unknown9142(35)
        AirPushbackY(33000)
        AirPushbackX(10000)
        PushbackX(12000)
        AirUntechableTime(38)
        Hitstop(7)
        Unknown9016(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown11001(0, 3, 8)
        callSubroutine('Dash_AfterImage')
    sprite('nt404_00', 4)	# 1-4
    physicsXImpulse(4000)
    GFX_1('ntef_D_aura', 0)
    Unknown8010(100, 1, 0)
    sprite('nt404_01', 4)	# 5-8
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    SFX_3('ntse_04')
    GFX_1('ntef_D_aura', 0)
    Unknown1019(120)
    callSubroutine('Dash_AfterImage')
    sprite('nt404_02', 2)	# 9-10
    Unknown7007('626e743230345f30000000000000000064000000626e743230345f31000000000000000064000000626e743230345f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1019(300)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown8007(100, 1, 1)
    sprite('nt404_03', 2)	# 11-12
    Unknown1019(400)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown8009(0)
    sprite('nt404_04', 3)	# 13-15	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    if (SLOT_19 <= 200000):
        Unknown48('190000000200000033000000160000000200000025000000')
    sprite('nt404_05', 1)	# 16-16
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 1)	# 17-17
    Unknown1019(70)
    Unknown3029(0)
    loopRest()
    label(9)
    sprite('nt404_07', 3)	# 18-20
    Unknown1019(50)
    EnableCollision(1)
    sprite('nt404_08', 3)	# 21-23
    Unknown1019(50)
    sprite('nt404_09', 3)	# 24-26
    Unknown3029(0)
    Unknown1019(30)
    sprite('nt402_10', 3)	# 27-29
    Unknown1019(30)
    sprite('nt402_11', 2)	# 30-31
    Unknown1019(0)

@State
def Dodge_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2018(0, 60)
        Unknown14070('ShortDash')
        SLOT_59 = 0

        def upon_CLEAR_OR_EXIT():
            if (SLOT_41 <= 150000):
                if SLOT_38:
                    if (SLOT_40 >= 0):
                        clearUponHandler(3)
                        Unknown1019(40)
                elif (SLOT_40 <= 0):
                    clearUponHandler(3)
                    Unknown1019(40)
        SLOT_4 = 1

        def upon_STATE_END():
            SLOT_4 = 0
        SLOT_60 = 0
    sprite('nt407_00', 4)	# 1-4
    Unknown1084(1)
    Unknown3029(1)
    Unknown3069(1)
    sprite('nt407_01', 4)	# 5-8
    Unknown14070('DodgeThrow')
    Unknown14070('DodgeThrow_B')
    Unknown14070('DodgeThrow_C')
    setInvincible(1)
    Unknown22019('0100000000000000000000000100000000000000')
    Unknown7007('626e743230385f30000000000000000064000000626e743230385f31000000000000000064000000626e743230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('nt407_02', 4)	# 9-12
    Unknown14072('ShortDash')
    Unknown14072('DodgeThrow')
    Unknown14072('DodgeThrow_B')
    Unknown14072('DodgeThrow_C')
    sprite('nt407_03', 18)	# 13-30
    EnableCollision(0)
    sprite('nt407_02', 8)	# 31-38
    setInvincible(0)
    Unknown2018(1, 60)
    EnableCollision(1)
    Unknown3029(0)
    sprite('nt407_04', 6)	# 39-44
    sprite('nt407_05', 5)	# 45-49
    Unknown14073('ShortDash')
    Unknown14073('DodgeThrow')
    Unknown14073('DodgeThrow_B')
    Unknown14073('DodgeThrow_C')
    loopRest()
    sprite('keep', 1)	# 50-50

@State
def Dodge():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11063(1)
        Unknown2018(0, 60)
        SLOT_59 = 1
        SLOT_60 = 0
        Unknown14070('ShortDash')

        def upon_CLEAR_OR_EXIT():
            if (SLOT_41 <= 150000):
                if SLOT_38:
                    if (SLOT_40 >= 0):
                        clearUponHandler(3)
                        Unknown1019(40)
                elif (SLOT_40 <= 0):
                    clearUponHandler(3)
                    Unknown1019(40)
    sprite('nt408_00', 1)	# 1-1
    EnableCollision(0)
    Unknown2015(40)
    physicsXImpulse(5000)
    callSubroutine('Dash_AfterImage')
    sprite('nt408_00', 3)	# 2-4
    Unknown1019(200)
    sprite('nt408_01', 4)	# 5-8
    SFX_3('ntse_12')
    Unknown7007('626e743231305f30000000000000000064000000626e743231305f31000000000000000064000000626e743231305f320000000000000000640000000000000000000000000000000000000000000000')
    setInvincible(1)
    Unknown22019('0100000000000000000000000100000000000000')
    Unknown14070('DodgeThrow')
    Unknown14070('DodgeThrow_B')
    Unknown14070('DodgeThrow_C')

    def upon_STATE_END():
        Unknown2005()
        Unknown3001(255)
        Unknown3004(0)
    sprite('nt408_02', 4)	# 9-12
    Unknown3001(200)
    Unknown3004(-10)
    sprite('nt408_02', 4)	# 13-16
    Unknown1019(600)
    sprite('nt408_03', 4)	# 17-20
    Unknown1019(50)
    Unknown14072('DodgeThrow')
    Unknown14072('DodgeThrow_B')
    Unknown14072('DodgeThrow_C')
    sprite('nt408_04', 3)	# 21-23
    Unknown1019(50)
    sprite('nt408_05', 3)	# 24-26
    Unknown1019(50)
    Unknown3001(160)
    Unknown3004(20)
    sprite('nt408_06', 3)	# 27-29
    setInvincible(0)
    EnableCollision(1)
    Unknown2015(-1)
    Unknown1084(1)
    Unknown2018(1, 60)
    Unknown3029(0)
    sprite('nt408_07', 4)	# 30-33
    Unknown14073('DodgeThrow')
    Unknown14073('DodgeThrow_B')
    Unknown14073('DodgeThrow_C')
    sprite('nt408_08', 3)	# 34-36
    sprite('keep', 1)	# 37-37

@State
def DodgeThrow():

    def upon_IMMEDIATE():
        Unknown17011('DodgeThrowExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(80000)
        Unknown11002(-1)
        AttackP1(100)
        AttackP2(100)
        Unknown11045(0)
        Unknown11082(1)
        Unknown11061(1)
        Unknown30061(0)
        Unknown30068(1)
        setInvincible(1)
        Unknown22019('0100000000000000000000000100000000000000')
        if SLOT_59:
            Unknown2006()
    if SLOT_59:
        _gotolabel(0)
    sprite('nt409_00', 2)	# 1-2
    sprite('nt409_01', 2)	# 3-4
    sprite('nt409_02', 3)	# 5-7
    physicsXImpulse(30000)
    Unknown8006(100, 1, 1)
    sprite('nt409_03', 3)	# 8-10
    Unknown1019(20)
    loopRest()
    label(0)
    sprite('nt409_04', 2)	# 11-12
    Unknown8007(100, 1, 1)
    Unknown1019(0)
    sprite('nt409_05', 2)	# 13-14
    SFX_0('004_swing_grap_1_2')
    sprite('nt409_06', 5)	# 15-19	 **attackbox here**
    GFX_0('ntef_409', -1)
    Unknown3029(0)
    sprite('nt409_17', 5)	# 20-24
    SFX_1('nt155')
    setInvincible(0)
    sprite('nt409_18', 5)	# 25-29
    sprite('nt409_19', 5)	# 30-34
    sprite('nt402_10', 8)	# 35-42
    sprite('nt402_11', 5)	# 43-47

@State
def DodgeThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(1800)
        AttackP2(100)
        MinimumDamagePct(5)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(9000)
        AirUntechableTime(60)
        Unknown11066(1)
        Unknown11084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
        Unknown23022(1)
        Unknown11069('DodgeThrowExe')
        Unknown14083(0)
    sprite('nt409_06', 1)	# 1-1	 **attackbox here**
    if SLOT_59:
        Unknown7007('626e743231315f30000000000000000064000000626e743231315f31000000000000000064000000626e743231315f320000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown7007('626e743230395f30000000000000000064000000626e743230395f31000000000000000064000000626e743230395f320000000000000000640000000000000000000000000000000000000000000000')
    GFX_0('ntef_409', -1)
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    StartMultihit()
    sprite('nt409_07', 3)	# 2-4	 **attackbox here**
    Unknown5000(25, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    sprite('nt409_08', 3)	# 5-7
    sprite('nt409_09', 3)	# 8-10
    physicsXImpulse(12000)
    physicsYImpulse(24000)
    Unknown1043()
    Unknown8001(0, 0)
    sprite('nt409_10', 3)	# 11-13
    sprite('nt409_11', 3)	# 14-16	 **attackbox here**
    GFX_0('ntef_410', -1)
    RefreshMultihit()
    AttackP2(75)
    AirPushbackY(32000)
    Unknown11068(0)
    Unknown1019(50)
    Unknown11069('')
    Unknown14083(1)
    sprite('nt409_12', 3)	# 17-19
    sprite('nt409_13', 3)	# 20-22
    sprite('nt409_14', 3)	# 23-25
    sprite('nt409_15', 3)	# 26-28
    sprite('nt409_16', 32767)	# 29-32795
    loopRest()
    label(0)
    sprite('nt033_03', 1)	# 32796-32796
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt033_04', 2)	# 32797-32798
    sprite('nt033_05', 2)	# 32799-32800
    sprite('nt033_06', 2)	# 32801-32802
    sprite('nt033_07', 2)	# 32803-32804

@State
def UltimateAssault_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(4300)
        MinimumDamagePct(35)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Unknown11056(0)
        setInvincible(1)
        Unknown1084(1)

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
            Hitstop(20)

        def upon_77():
            sendToLabel(1)
            Hitstop(20)
        Unknown23159('UltimateAssault_TC')
    sprite('nt430_00', 2)	# 1-2
    sprite('nt430_01', 2)	# 3-4
    sprite('nt430_02', 2)	# 5-6
    tag_voice(1, 'bnt250_0', 'bnt250_1', '', '')
    GFX_0('ntef_430atk', -1)
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    Unknown1084(1)
    sprite('nt430_03', 3)	# 7-9
    sprite('nt430_04', 3)	# 10-12
    sprite('nt430_05', 3)	# 13-15
    GFX_0('ntef_430_bloodMatome', -1)
    sprite('nt430_03', 3)	# 16-18
    sprite('nt430_04', 3)	# 19-21
    sprite('nt430_05', 3)	# 22-24
    sprite('nt430_06', 4)	# 25-28
    Unknown3029(1)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d107000000000000')
    sprite('nt430_07', 4)	# 29-32
    sprite('nt430_08', 4)	# 33-36
    sprite('nt430_09', 4)	# 37-40
    sprite('nt430_10', 4)	# 41-44
    sprite('nt430_11', 6)	# 45-50
    sprite('nt430_12', 3)	# 51-53
    sprite('nt430_13', 3)	# 54-56
    physicsXImpulse(5000)
    Unknown8007(100, 1, 0)
    tag_voice(0, 'bnt251_0', 'bnt251_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    sprite('nt430_14_2', 2)	# 57-58	 **attackbox here**
    Unknown1019(800)
    Unknown1028(7000)
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 59-60	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 61-62	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 63-64	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 65-66	 **attackbox here**
    Unknown8006(100, 1, 0)
    setInvincible(0)
    gotoLabel(2)
    label(1)
    sprite('nt430_15', 2)	# 67-68	 **attackbox here**
    Unknown8006(100, 1, 0)
    DisableAttackRestOfMove()
    physicsXImpulse(50000)
    Unknown1028(7000)
    sprite('nt430_14', 2)	# 69-70	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_15', 2)	# 71-72	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_14', 2)	# 73-74	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    label(2)
    sprite('nt430_16', 3)	# 75-77
    EnableCollision(1)
    setInvincible(0)
    Unknown1019(30)
    Unknown1034(0)
    Unknown8010(100, 1, 0)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d207000000000000')
    sprite('nt430_17', 3)	# 78-80
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 3)	# 81-83
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 3)	# 84-86
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_20', 8)	# 87-94
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 95-97
    Unknown3029(0)

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(5200)
        MinimumDamagePct(31)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Unknown11056(0)
        setInvincible(1)
        Unknown1084(1)
        callSubroutine('Dash_AfterImage')

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
            Hitstop(20)

        def upon_77():
            sendToLabel(1)
            Hitstop(20)
        Unknown23159('UltimateAssault_TC')
    sprite('nt430_00', 2)	# 1-2
    sprite('nt430_01', 2)	# 3-4
    sprite('nt430_02', 2)	# 5-6
    tag_voice(1, 'bnt250_0', 'bnt250_1', '', '')
    GFX_0('ntef_430atk', -1)
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    Unknown1084(1)
    sprite('nt430_03', 3)	# 7-9
    sprite('nt430_04', 3)	# 10-12
    sprite('nt430_05', 3)	# 13-15
    GFX_0('ntef_430_bloodMatome', -1)
    sprite('nt430_03', 3)	# 16-18
    sprite('nt430_04', 3)	# 19-21
    sprite('nt430_05', 3)	# 22-24
    sprite('nt430_06', 4)	# 25-28
    Unknown3029(1)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d107000000000000')
    sprite('nt430_07', 4)	# 29-32
    sprite('nt430_08', 4)	# 33-36
    sprite('nt430_09', 4)	# 37-40
    sprite('nt430_10', 4)	# 41-44
    sprite('nt430_11', 6)	# 45-50
    sprite('nt430_12', 3)	# 51-53
    sprite('nt430_13', 3)	# 54-56
    physicsXImpulse(5000)
    Unknown8007(100, 1, 0)
    tag_voice(0, 'bnt251_0', 'bnt251_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    sprite('nt430_14_2', 2)	# 57-58	 **attackbox here**
    Unknown1019(800)
    Unknown1028(7000)
    Unknown1019(120)
    Unknown1034(150)
    Unknown8001(3, 100)
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 59-60	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 61-62	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 63-64	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 65-66	 **attackbox here**
    Unknown8006(100, 1, 0)
    setInvincible(0)
    gotoLabel(2)
    label(1)
    sprite('nt430_15', 2)	# 67-68	 **attackbox here**
    Unknown8006(100, 1, 0)
    DisableAttackRestOfMove()
    physicsXImpulse(50000)
    Unknown1028(7000)
    sprite('nt430_14', 2)	# 69-70	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_15', 2)	# 71-72	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_14', 2)	# 73-74	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    label(2)
    sprite('nt430_16', 3)	# 75-77
    EnableCollision(1)
    setInvincible(0)
    Unknown1019(30)
    Unknown1034(0)
    Unknown8010(100, 1, 0)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d207000000000000')
    sprite('nt430_17', 3)	# 78-80
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 3)	# 81-83
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 3)	# 84-86
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_20', 8)	# 87-94
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 95-97
    Unknown3029(0)

@State
def UltimateAssaultOD_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(4300)
        MinimumDamagePct(20)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Unknown11001(0, 0, 0)
        Unknown11056(0)
        Unknown11084(1)
        setInvincible(1)
        Unknown1084(1)
        SLOT_59 = 0

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
            SLOT_53 = 1
            Unknown13024(0)
            Unknown11069('UltimateAssaultOD_2nd')
            Hitstop(20)
            Unknown11064(1)

        def upon_77():
            sendToLabel(1)
            Hitstop(20)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_19 <= 170000):
                if SLOT_52:
                    sendToLabel(2)
        SLOT_61 = 0

        def upon_82():
            SLOT_61 = 1
        Unknown23159('UltimateAssaultOD_TC')
    sprite('nt430_00', 2)	# 1-2
    sprite('nt430_01', 2)	# 3-4
    sprite('nt430_02', 2)	# 5-6
    tag_voice(1, 'bnt250_0', 'bnt250_1', '', '')
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430atk', -1)
    sprite('nt430_03', 3)	# 7-9
    sprite('nt430_04', 3)	# 10-12
    sprite('nt430_05', 3)	# 13-15
    GFX_0('ntef_430_bloodMatome', -1)
    sprite('nt430_03', 3)	# 16-18
    sprite('nt430_04', 3)	# 19-21
    sprite('nt430_05', 3)	# 22-24
    sprite('nt430_06', 4)	# 25-28
    Unknown3029(1)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d107000000000000')
    sprite('nt430_07', 4)	# 29-32
    sprite('nt430_08', 4)	# 33-36
    sprite('nt430_09', 4)	# 37-40
    sprite('nt430_10', 4)	# 41-44
    sprite('nt430_11', 6)	# 45-50
    sprite('nt430_12', 3)	# 51-53
    sprite('nt430_13', 3)	# 54-56
    physicsXImpulse(5000)
    Unknown8007(100, 1, 0)
    tag_voice(0, 'bnt251_0', 'bnt251_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    sprite('nt430_14_2', 2)	# 57-58	 **attackbox here**
    Unknown1019(800)
    Unknown1028(7000)
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 59-60	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 61-62	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 63-64	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 65-66	 **attackbox here**
    Unknown8006(100, 1, 0)
    setInvincible(0)
    gotoLabel(2)
    label(1)
    sprite('nt430_15', 2)	# 67-68	 **attackbox here**
    Unknown8006(100, 1, 0)
    DisableAttackRestOfMove()
    physicsXImpulse(50000)
    Unknown1028(7000)
    sprite('nt430_14', 2)	# 69-70	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_15', 2)	# 71-72	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_14', 1)	# 73-73	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_14', 1)	# 74-74	 **attackbox here**
    SLOT_52 = 1
    sprite('nt430_15', 2)	# 75-76	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 77-78	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 79-80	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 81-82	 **attackbox here**
    Unknown8006(100, 1, 0)
    label(2)
    sprite('nt430_16', 3)	# 83-85
    clearUponHandler(3)
    EnableCollision(1)
    if (not SLOT_53):
        setInvincible(0)
    Unknown1019(30)
    Unknown1034(0)
    Unknown8010(100, 1, 0)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d207000000000000')
    sprite('nt430_17', 3)	# 86-88
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    if SLOT_53:
        enterState('UltimateAssaultOD_2nd')
    sprite('nt430_18', 3)	# 89-91
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 3)	# 92-94
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_20', 8)	# 95-102
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 103-105
    Unknown3029(0)

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(5200)
        MinimumDamagePct(20)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Unknown11001(0, 0, 0)
        Unknown11056(0)
        Unknown11084(1)
        setInvincible(1)
        Unknown1084(1)
        callSubroutine('Dash_AfterImage')
        SLOT_59 = 1

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
            SLOT_53 = 1
            Unknown13024(0)
            Unknown11069('UltimateAssaultOD_2nd')
            Hitstop(20)
            Unknown11064(1)

        def upon_77():
            Hitstop(20)
            sendToLabel(1)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_19 <= 170000):
                if SLOT_52:
                    sendToLabel(2)
        SLOT_61 = 0

        def upon_82():
            SLOT_61 = 1
        Unknown23159('UltimateAssaultOD_TC')
    sprite('nt430_00', 2)	# 1-2
    sprite('nt430_01', 2)	# 3-4
    sprite('nt430_02', 2)	# 5-6
    tag_voice(1, 'bnt250_0', 'bnt250_1', '', '')
    Unknown2036(50, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430atk', -1)
    sprite('nt430_03', 3)	# 7-9
    sprite('nt430_04', 3)	# 10-12
    sprite('nt430_05', 3)	# 13-15
    GFX_0('ntef_430_bloodMatome', -1)
    sprite('nt430_03', 3)	# 16-18
    sprite('nt430_04', 3)	# 19-21
    sprite('nt430_05', 3)	# 22-24
    sprite('nt430_06', 4)	# 25-28
    Unknown3029(1)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d107000000000000')
    sprite('nt430_07', 4)	# 29-32
    sprite('nt430_08', 4)	# 33-36
    sprite('nt430_09', 4)	# 37-40
    sprite('nt430_10', 4)	# 41-44
    sprite('nt430_11', 6)	# 45-50
    sprite('nt430_12', 3)	# 51-53
    sprite('nt430_13', 3)	# 54-56
    physicsXImpulse(5000)
    Unknown8007(100, 1, 0)
    tag_voice(0, 'bnt251_0', 'bnt251_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    sprite('nt430_14_2', 2)	# 57-58	 **attackbox here**
    Unknown1019(800)
    Unknown1028(7000)
    Unknown1019(120)
    Unknown1034(150)
    Unknown8001(3, 100)
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 59-60	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 61-62	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 63-64	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 65-66	 **attackbox here**
    Unknown8006(100, 1, 0)
    setInvincible(0)
    gotoLabel(2)
    label(1)
    sprite('nt430_15', 2)	# 67-68	 **attackbox here**
    Unknown8006(100, 1, 0)
    DisableAttackRestOfMove()
    physicsXImpulse(50000)
    Unknown1028(7000)
    sprite('nt430_14', 2)	# 69-70	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_15', 2)	# 71-72	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_14', 1)	# 73-73	 **attackbox here**
    Unknown8006(100, 1, 0)
    Unknown1019(90)
    sprite('nt430_14', 1)	# 74-74	 **attackbox here**
    SLOT_52 = 1
    sprite('nt430_15', 2)	# 75-76	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 77-78	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_15', 2)	# 79-80	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('nt430_14', 2)	# 81-82	 **attackbox here**
    Unknown8006(100, 1, 0)
    label(2)
    sprite('nt430_16', 3)	# 83-85
    clearUponHandler(3)
    EnableCollision(1)
    if (not SLOT_53):
        setInvincible(0)
    Unknown1019(30)
    Unknown1034(0)
    Unknown8010(100, 1, 0)
    Unknown21015('6e7465665f34333061746b000000000000000000000000000000000000000000d207000000000000')
    sprite('nt430_17', 3)	# 86-88
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    if SLOT_53:
        enterState('UltimateAssaultOD_2nd')
    sprite('nt430_18', 3)	# 89-91
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 3)	# 92-94
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_20', 8)	# 95-102
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 103-105
    Unknown3029(0)

@State
def UltimateAssaultOD_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(2700)
        AttackP1(48)
        AttackP2(100)
        MinimumDamagePct(30)
        AirPushbackY(60000)
        YImpluseBeforeWallbounce(4000)
        AirUntechableTime(80)
        Unknown9310(15)
        Hitstop(20)
        Unknown11056(0)
        Unknown11108('03000000')
        Unknown13024(0)
        setInvincible(1)
        sendToLabelUpon(2, 9)

        def upon_STATE_END():
            SLOT_59 = 0
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        else:
            Unknown3029(1)
            Unknown3069(1)
            Unknown3070(3)
            Unknown3071(5)
        if (SLOT_25 <= 250000):
            Unknown1000(1615000)
        if Unknown23145('UltimateAirAssaultOD'):
            SLOT_51 = 1
    sprite('nt430_17', 3)	# 1-3
    if SLOT_51:
        Unknown2006()
        physicsXImpulse(30000)
    GFX_0('ntef_430_moya', -1)
    Unknown8010(100, 1, 0)
    sprite('nt430_31', 3)	# 4-6
    Unknown36(22)
    Unknown1019(20)
    YAccel(20)
    Unknown1039(20)
    Unknown35()
    if SLOT_61:
        Unknown36(23)
        Unknown1019(20)
        YAccel(20)
        Unknown1039(20)
        Unknown35()
    Unknown8010(100, 1, 0)
    Unknown2036(35, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('nt430_32', 25)	# 7-31
    Unknown1084(1)
    Unknown18009(1)
    Unknown23024(2)
    if SLOT_21:
        Unknown20000(1)
        Unknown20003(1)
    sprite('nt430_33', 8)	# 32-39
    physicsXImpulse(5000)
    sprite('nt430_34', 4)	# 40-43
    Unknown7006('bnt254_0', 100, 846491234, 828322869, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown1019(200)
    sprite('nt430_34', 4)	# 44-47
    sprite('nt430_35', 6)	# 48-53
    SFX_3('ntse_07')
    Unknown1019(200)
    physicsYImpulse(16000)
    setGravity(800)
    Unknown18009(0)
    Unknown8001(3, 100)
    sprite('nt430_36ex', 3)	# 54-56	 **attackbox here**
    RefreshMultihit()
    Unknown1019(50)
    GFX_0('ntef_430atkOD', -1)
    SFX_0('025_cleanhit_grap')
    Unknown21015('6e7465665f3433305f6d6f796100000000000000000000000000000000000000d307000000000000')
    sprite('nt430_37', 4)	# 57-60
    Unknown1019(50)
    sprite('nt430_38', 4)	# 61-64
    Unknown1019(50)
    sprite('nt430_39', 4)	# 65-68
    Unknown1019(50)
    sprite('nt430_40', 4)	# 69-72
    label(0)
    sprite('nt020_07', 4)	# 73-76
    sprite('nt020_08', 4)	# 77-80
    gotoLabel(0)
    label(9)
    sprite('nt024_00', 3)	# 81-83
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('nt024_01', 15)	# 84-98
    setInvincible(0)
    sprite('nt024_02', 3)	# 99-101
    Unknown13024(1)
    sprite('nt024_03', 3)	# 102-104
    sprite('nt024_04', 3)	# 105-107

@State
def UltimateAirAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(5200)
        MinimumDamagePct(32)
        Hitstop(20)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(-160000)
        Unknown9202(20)
        Unknown11056(0)
        setInvincible(1)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        SLOT_59 = 1
        callSubroutine('Dash_AfterImage')

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
        Unknown23159('UltimateAirAssault_TC')
    sprite('nt430_22', 2)	# 1-2
    sprite('nt430_23', 2)	# 3-4
    sprite('nt430_24', 3)	# 5-7
    tag_voice(1, 'bnt252_0', 'bnt252_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_AirbloodMatome', -1)
    sprite('nt430_22', 3)	# 8-10
    GFX_0('ntef_Air430atk', -1)
    sprite('nt430_23', 3)	# 11-13
    sprite('nt430_24', 3)	# 14-16
    sprite('nt430_22', 3)	# 17-19
    sprite('nt430_23', 3)	# 20-22
    sprite('nt430_24', 3)	# 23-25
    sprite('nt430_25', 3)	# 26-28
    Unknown3029(1)
    physicsXImpulse(-18000)
    physicsYImpulse(30000)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d407000000000000')
    sprite('nt430_25', 3)	# 29-31
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_26', 8)	# 32-39
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 40-42
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 43-45
    Unknown1019(0)
    YAccel(0)
    sprite('nt430_28', 3)	# 46-48
    physicsXImpulse(5000)
    physicsYImpulse(-5000)
    sprite('nt430_28', 3)	# 49-51
    tag_voice(0, 'bnt253_0', 'bnt253_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    Unknown1019(300)
    YAccel(300)
    sprite('nt430_29_2', 2)	# 52-53	 **attackbox here**
    Unknown1019(300)
    YAccel(300)
    Unknown1028(2000)
    setGravity(2000)
    sprite('nt430_30_2', 2)	# 54-55	 **attackbox here**
    label(0)
    sprite('nt430_29', 2)	# 56-57	 **attackbox here**
    sprite('nt430_30', 2)	# 58-59	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('nt430_17', 2)	# 60-61
    setInvincible(0)
    Unknown1019(60)
    YAccel(0)
    Unknown1034(0)
    Unknown1039(0)
    Unknown8010(100, 1, 0)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d507000000000000')
    sprite('nt430_17', 2)	# 62-63
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 64-65
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 66-67
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 2)	# 68-69
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_19', 2)	# 70-71
    Unknown8010(100, 1, 0)
    sprite('nt430_20', 10)	# 72-81
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 82-84
    Unknown3029(0)

@State
def UltimateAirAssault_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(4200)
        MinimumDamagePct(35)
        Hitstop(20)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(-160000)
        Unknown9202(20)
        Unknown11056(0)
        setInvincible(1)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        SLOT_59 = 0

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
        Unknown23159('UltimateAirAssault_TC')
    sprite('nt430_22', 2)	# 1-2
    sprite('nt430_23', 2)	# 3-4
    sprite('nt430_24', 3)	# 5-7
    tag_voice(1, 'bnt252_0', 'bnt252_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_AirbloodMatome', -1)
    sprite('nt430_22', 3)	# 8-10
    GFX_0('ntef_Air430atk', -1)
    sprite('nt430_23', 3)	# 11-13
    sprite('nt430_24', 3)	# 14-16
    sprite('nt430_22', 3)	# 17-19
    sprite('nt430_23', 3)	# 20-22
    sprite('nt430_24', 3)	# 23-25
    sprite('nt430_25', 3)	# 26-28
    Unknown3029(1)
    physicsXImpulse(-18000)
    physicsYImpulse(30000)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d407000000000000')
    sprite('nt430_25', 3)	# 29-31
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_26', 8)	# 32-39
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 40-42
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 43-45
    Unknown1019(0)
    YAccel(0)
    sprite('nt430_28', 3)	# 46-48
    physicsXImpulse(5000)
    physicsYImpulse(-5000)
    sprite('nt430_28', 3)	# 49-51
    tag_voice(0, 'bnt253_0', 'bnt253_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    Unknown1019(300)
    YAccel(300)
    sprite('nt430_29_2', 2)	# 52-53	 **attackbox here**
    Unknown1019(300)
    YAccel(300)
    Unknown1028(2000)
    setGravity(2000)
    sprite('nt430_30_2', 2)	# 54-55	 **attackbox here**
    label(0)
    sprite('nt430_29', 2)	# 56-57	 **attackbox here**
    sprite('nt430_30', 2)	# 58-59	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('nt430_17', 2)	# 60-61
    setInvincible(0)
    Unknown1019(60)
    YAccel(0)
    Unknown1034(0)
    Unknown1039(0)
    Unknown8010(100, 1, 0)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d507000000000000')
    sprite('nt430_17', 2)	# 62-63
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 64-65
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 66-67
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 2)	# 68-69
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_19', 2)	# 70-71
    Unknown8010(100, 1, 0)
    sprite('nt430_20', 10)	# 72-81
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 82-84
    Unknown3029(0)

@State
def UltimateAirAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(5200)
        MinimumDamagePct(20)
        Hitstop(20)
        Unknown11001(0, -2, -2)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(-160000)
        Unknown9202(22)
        Unknown11056(0)
        Unknown11084(1)
        setInvincible(1)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        SLOT_59 = 1
        callSubroutine('Dash_AfterImage')

        def upon_78():
            DisableAttackRestOfMove()
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
            SLOT_53 = 1
            Unknown13024(0)
            Unknown11069('UltimateAssaultOD_2nd')
            Hitstop(20)
            Unknown11064(1)

        def upon_77():
            Hitstop(20)
        SLOT_61 = 0

        def upon_82():
            SLOT_61 = 1
        Unknown23159('UltimateAirAssaultOD_TC')
    sprite('nt430_22', 2)	# 1-2
    sprite('nt430_23', 2)	# 3-4
    sprite('nt430_24', 3)	# 5-7
    tag_voice(1, 'bnt252_0', 'bnt252_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_AirbloodMatome', -1)
    sprite('nt430_22', 3)	# 8-10
    GFX_0('ntef_Air430atk', -1)
    sprite('nt430_23', 3)	# 11-13
    sprite('nt430_24', 3)	# 14-16
    sprite('nt430_22', 3)	# 17-19
    sprite('nt430_23', 3)	# 20-22
    sprite('nt430_24', 3)	# 23-25
    sprite('nt430_25', 3)	# 26-28
    Unknown3029(1)
    physicsXImpulse(-18000)
    physicsYImpulse(30000)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d407000000000000')
    sprite('nt430_25', 3)	# 29-31
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_26', 8)	# 32-39
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 40-42
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 43-45
    Unknown1019(0)
    YAccel(0)
    sprite('nt430_28', 3)	# 46-48
    physicsXImpulse(6000)
    physicsYImpulse(-6000)
    sprite('nt430_28', 3)	# 49-51
    tag_voice(0, 'bnt253_0', 'bnt253_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    Unknown1019(300)
    YAccel(300)
    sprite('nt430_29_2', 2)	# 52-53	 **attackbox here**
    Unknown1019(300)
    YAccel(300)
    Unknown1028(2000)
    setGravity(2000)
    sprite('nt430_30_2', 2)	# 54-55	 **attackbox here**
    label(0)
    sprite('nt430_29', 2)	# 56-57	 **attackbox here**
    sprite('nt430_30', 2)	# 58-59	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('nt430_17', 2)	# 60-61
    EnableCollision(1)
    setInvincible(0)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d507000000000000')
    Unknown1019(60)
    YAccel(0)
    Unknown1034(0)
    Unknown1039(0)
    Unknown8010(100, 1, 0)
    if SLOT_53:
        enterState('UltimateAssaultOD_2nd')
    sprite('nt430_17', 2)	# 62-63
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 64-65
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 66-67
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 2)	# 68-69
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_19', 2)	# 70-71
    Unknown8010(100, 1, 0)
    sprite('nt430_20', 10)	# 72-81
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 82-84
    Unknown3029(0)

@State
def UltimateAirAssaultOD_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(4300)
        MinimumDamagePct(20)
        Hitstop(20)
        Unknown11001(0, -2, -2)
        AirUntechableTime(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(-160000)
        Unknown9202(22)
        Unknown11056(0)
        Unknown11084(1)
        setInvincible(1)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        SLOT_59 = 0

        def upon_78():
            DisableAttackRestOfMove()
            Unknown22019('0100000001000000010000000100000001000000')
            EnableCollision(0)
            SLOT_53 = 1
            Unknown13024(0)
            Unknown11069('UltimateAssaultOD_2nd')
            Hitstop(20)
            Unknown11064(1)

        def upon_77():
            Hitstop(20)
        SLOT_61 = 0

        def upon_82():
            SLOT_61 = 1
        Unknown23159('UltimateAirAssaultOD_TC')
    sprite('nt430_22', 2)	# 1-2
    sprite('nt430_23', 2)	# 3-4
    sprite('nt430_24', 3)	# 5-7
    tag_voice(1, 'bnt252_0', 'bnt252_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_AirbloodMatome', -1)
    sprite('nt430_22', 3)	# 8-10
    GFX_0('ntef_Air430atk', -1)
    sprite('nt430_23', 3)	# 11-13
    sprite('nt430_24', 3)	# 14-16
    sprite('nt430_22', 3)	# 17-19
    sprite('nt430_23', 3)	# 20-22
    sprite('nt430_24', 3)	# 23-25
    sprite('nt430_25', 3)	# 26-28
    Unknown3029(1)
    physicsXImpulse(-18000)
    physicsYImpulse(30000)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d407000000000000')
    sprite('nt430_25', 3)	# 29-31
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_26', 8)	# 32-39
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 40-42
    Unknown1019(50)
    YAccel(50)
    sprite('nt430_27', 3)	# 43-45
    Unknown1019(0)
    YAccel(0)
    sprite('nt430_28', 3)	# 46-48
    physicsXImpulse(6000)
    physicsYImpulse(-6000)
    sprite('nt430_28', 3)	# 49-51
    tag_voice(0, 'bnt253_0', 'bnt253_1', '', '')
    SFX_3('ntse_06')
    SFX_3('ntse_07')
    Unknown1019(300)
    YAccel(300)
    sprite('nt430_29_2', 2)	# 52-53	 **attackbox here**
    Unknown1019(300)
    YAccel(300)
    Unknown1028(2000)
    setGravity(2000)
    sprite('nt430_30_2', 2)	# 54-55	 **attackbox here**
    label(0)
    sprite('nt430_29', 2)	# 56-57	 **attackbox here**
    sprite('nt430_30', 2)	# 58-59	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('nt430_17', 2)	# 60-61
    EnableCollision(1)
    setInvincible(0)
    Unknown21015('6e7465665f41697234333061746b000000000000000000000000000000000000d507000000000000')
    Unknown1019(60)
    YAccel(0)
    Unknown1034(0)
    Unknown1039(0)
    Unknown8010(100, 1, 0)
    if SLOT_53:
        enterState('UltimateAssaultOD_2nd')
    sprite('nt430_17', 2)	# 62-63
    Unknown1019(60)
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 64-65
    Unknown8010(100, 1, 0)
    sprite('nt430_18', 2)	# 66-67
    Unknown8010(100, 1, 0)
    sprite('nt430_19', 2)	# 68-69
    Unknown8010(100, 1, 0)
    Unknown18009(1)
    sprite('nt430_19', 2)	# 70-71
    Unknown8010(100, 1, 0)
    sprite('nt430_20', 10)	# 72-81
    Unknown1084(1)
    Unknown8000(100, 1, 0)
    sprite('nt430_21', 3)	# 82-84
    Unknown3029(0)

@State
def UltimateEdgeAssault_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2200)
        MinimumDamagePct(25)
        Hitstop(3)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(58000)
        AirUntechableTime(300)
        Unknown11056(0)
        Unknown11084(1)
        Unknown11064(1)
        SLOT_59 = 0
        Unknown2073(1)
        setInvincible(1)
        Unknown1084(1)

        def upon_78():
            clearUponHandler(78)
            Hitstop(20)
            Unknown11001(0, 0, 0)
            enterState('UltimateEdgeAssault_Exe')
            Unknown21015('6e7465665f343331000000000000000000000000000000000000000000000000b90b000000000000')
            Unknown20000(1)
            Unknown11069('UltimateEdgeAssault_Exe')
            Unknown13024(0)
        Unknown23159('UltimateEdgeAssault_TC')
    sprite('nt431_00', 3)	# 1-3
    sprite('nt431_01', 3)	# 4-6
    tag_voice(1, 'bnt255_0', 'bnt255_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_bloodMatome', -1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    Unknown36(1)
    Unknown1096(3000)
    Unknown35()
    sprite('nt431_02', 3)	# 7-9
    sprite('nt431_03', 3)	# 10-12
    sprite('nt431_01', 3)	# 13-15
    sprite('nt431_02', 3)	# 16-18
    sprite('nt431_03', 3)	# 19-21
    sprite('nt431_01', 3)	# 22-24
    sprite('nt431_02', 3)	# 25-27
    sprite('nt431_04', 5)	# 28-32
    sprite('nt431_05', 5)	# 33-37
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    sprite('nt431_06', 5)	# 38-42
    if SLOT_2:
        physicsXImpulse(3000)
    sprite('nt431_07', 5)	# 43-47
    sprite('nt431_08', 5)	# 48-52
    GFX_0('ntef_431', -1)
    SFX_3('ntse_07')
    SFX_3('ntse_07')
    sprite('nt431_09', 1)	# 53-53	 **attackbox here**
    Unknown1019(0)
    sprite('nt431_09', 5)	# 54-58	 **attackbox here**
    clearUponHandler(78)
    DisableAttackRestOfMove()
    sprite('nt431_09', 9)	# 59-67	 **attackbox here**
    SFX_3('ntse_08')
    sprite('nt431_10', 7)	# 68-74
    setInvincible(0)
    Unknown3029(0)
    sprite('nt431_11', 9)	# 75-83
    sprite('nt431_12', 9)	# 84-92
    sprite('nt203_14', 9)	# 93-101

@State
def UltimateEdgeAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(3000)
        MinimumDamagePct(25)
        Hitstop(3)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(58000)
        AirUntechableTime(300)
        Unknown11056(0)
        Unknown11084(1)
        Unknown11064(1)
        SLOT_59 = 1
        Unknown2073(1)
        setInvincible(1)
        Unknown1084(1)
        callSubroutine('Dash_AfterImage')

        def upon_78():
            clearUponHandler(78)
            Hitstop(20)
            Unknown11001(0, 0, 0)
            enterState('UltimateEdgeAssault_Exe')
            Unknown21015('6e7465665f343331000000000000000000000000000000000000000000000000b90b000000000000')
            Unknown20000(1)
            Unknown11069('UltimateEdgeAssault_Exe')
            Unknown13024(0)
        Unknown23159('UltimateEdgeAssault_TC')
    sprite('nt431_00', 3)	# 1-3
    sprite('nt431_01', 3)	# 4-6
    tag_voice(1, 'bnt255_0', 'bnt255_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_bloodMatome', -1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    Unknown36(1)
    Unknown1096(3000)
    Unknown35()
    sprite('nt431_02', 3)	# 7-9
    sprite('nt431_03', 3)	# 10-12
    sprite('nt431_01', 3)	# 13-15
    sprite('nt431_02', 3)	# 16-18
    sprite('nt431_03', 3)	# 19-21
    sprite('nt431_01', 3)	# 22-24
    sprite('nt431_02', 3)	# 25-27
    sprite('nt431_04', 5)	# 28-32
    sprite('nt431_05', 5)	# 33-37
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    sprite('nt431_06', 5)	# 38-42
    physicsXImpulse(3000)
    sprite('nt431_07', 5)	# 43-47
    Unknown1019(200)
    Unknown8007(100, 1, 1)
    sprite('nt431_08', 5)	# 48-52
    Unknown1019(400)
    GFX_0('ntef_431', -1)
    Unknown23029(1, 3003, 0)
    SFX_3('ntse_07')
    SFX_3('ntse_07')
    sprite('nt431_09', 1)	# 53-53	 **attackbox here**
    Unknown1019(0)
    sprite('nt431_09', 5)	# 54-58	 **attackbox here**
    clearUponHandler(78)
    DisableAttackRestOfMove()
    sprite('nt431_09', 9)	# 59-67	 **attackbox here**
    SFX_3('ntse_08')
    sprite('nt431_10', 7)	# 68-74
    setInvincible(0)
    Unknown3029(0)
    sprite('nt431_11', 9)	# 75-83
    sprite('nt431_12', 9)	# 84-92
    sprite('nt203_14', 9)	# 93-101

@State
def UltimateEdgeAssault_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(7200)
        AttackP1(48)
        AttackP2(100)
        MinimumDamagePct(18)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(160000)
        AirPushbackY(15000)
        AirUntechableTime(100)
        Unknown9202(30)
        Unknown9310(25)
        Unknown11057(0)
        Unknown13024(0)
        Unknown23086(1)
        Unknown11108('03000000')
        Unknown11084(1)
        Unknown30048(1)
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        else:
            Unknown3029(1)
            Unknown3069(1)
            Unknown3070(3)
            Unknown3071(5)
        Unknown23022(1)
        Unknown20000(1)
        EnableCollision(0)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('nt431_09', 5)	# 1-5	 **attackbox here**
    StartMultihit()
    sprite('nt431_10', 6)	# 6-11
    sprite('nt431_11', 6)	# 12-17
    sprite('nt431_12', 6)	# 18-23
    loopRest()
    sprite('nt203_14', 3)	# 24-26
    Unknown23024(2)
    Unknown36(22)
    Unknown1086(22)
    teleportRelativeX(-250000)
    teleportRelativeY(2100000)
    physicsYImpulse(-50000)
    setGravity(0)
    Unknown35()
    sprite('nt340_01', 5)	# 27-31
    tag_voice(0, 'bnt256_0', 'bnt256_1', '', '')
    sprite('nt340_02', 5)	# 32-36
    sprite('nt340_03', 2)	# 37-38
    sprite('nt340_04', 2)	# 39-40
    sprite('nt340_05', 2)	# 41-42
    sprite('nt340_03', 2)	# 43-44
    sprite('nt340_04', 2)	# 45-46
    sprite('nt340_05', 2)	# 47-48
    sprite('nt340_03', 2)	# 49-50
    sprite('nt340_04', 2)	# 51-52
    sprite('nt340_05', 2)	# 53-54
    sprite('nt340_06', 5)	# 55-59
    sprite('nt340_07', 2)	# 60-61
    Unknown12046(200)
    sprite('nt340_08', 2)	# 62-63
    physicsXImpulse(100000)
    Unknown8003(100, 1, 1)
    sprite('nt340_09', 6)	# 64-69	 **attackbox here**
    Unknown1084(1)
    ScreenShake(20000, 4000)
    GFX_0('ntef_431AddAtk', -1)
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    sprite('nt340_10', 3)	# 70-72
    Unknown12046(0)
    EnableCollision(1)
    Unknown20000(0)
    sprite('nt340_11', 3)	# 73-75
    sprite('nt340_12', 3)	# 76-78
    sprite('nt340_13', 3)	# 79-81
    Unknown13024(1)
    sprite('nt340_14', 3)	# 82-84
    sprite('nt340_15', 3)	# 85-87
    sprite('nt340_16', 3)	# 88-90
    sprite('nt340_17', 3)	# 91-93
    sprite('nt615_00', 5)	# 94-98
    sprite('nt615_01', 5)	# 99-103
    tag_voice(0, 'bnt257_0', 'bnt257_1', '', '')
    sprite('nt615_02', 5)	# 104-108
    sprite('nt615_03', 10)	# 109-118
    sprite('nt615_04', 3)	# 119-121
    sprite('nt615_05', 10)	# 122-131
    sprite('nt615_05', 10)	# 132-141
    Unknown23024(0)
    sprite('nt615_04', 3)	# 142-144
    sprite('nt615_03', 3)	# 145-147
    sprite('nt615_02', 3)	# 148-150
    sprite('nt615_01', 3)	# 151-153
    sprite('nt615_00', 3)	# 154-156

@State
def UltimateEdgeAssaultOD_cancel():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2200)
        Hitstop(3)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(58000)
        AirUntechableTime(300)
        Unknown11056(0)
        Unknown11084(1)
        Unknown11064(1)
        SLOT_59 = 0
        Unknown2073(1)
        setInvincible(1)
        Unknown1084(1)

        def upon_78():
            clearUponHandler(78)
            Hitstop(20)
            Unknown11001(0, 0, 0)
            Unknown11069('UltimateEdgeAssault_Exe_OD')
            Unknown13024(0)
            enterState('UltimateEdgeAssault_Exe_OD')
            Unknown21015('6e7465665f3433315f4f44000000000000000000000000000000000000000000ba0b000000000000')
            Unknown13024(0)
        Unknown23159('UltimateEdgeAssault_TC')
    sprite('nt431_00', 3)	# 1-3
    sprite('nt431_01', 3)	# 4-6
    tag_voice(1, 'bnt255_0', 'bnt255_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_bloodMatome', -1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    Unknown36(1)
    Unknown1096(3000)
    Unknown35()
    sprite('nt431_02', 3)	# 7-9
    sprite('nt431_03', 3)	# 10-12
    sprite('nt431_01', 3)	# 13-15
    sprite('nt431_02', 3)	# 16-18
    sprite('nt431_03', 3)	# 19-21
    sprite('nt431_01', 3)	# 22-24
    sprite('nt431_02', 3)	# 25-27
    sprite('nt431_04', 5)	# 28-32
    sprite('nt431_05', 5)	# 33-37
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    sprite('nt431_06', 5)	# 38-42
    sprite('nt431_07', 5)	# 43-47
    sprite('nt431_08', 5)	# 48-52
    GFX_0('ntef_431_OD', -1)
    SFX_3('ntse_07')
    SFX_3('ntse_07')
    sprite('nt431_09', 1)	# 53-53	 **attackbox here**
    Unknown1019(0)
    sprite('nt431_09', 5)	# 54-58	 **attackbox here**
    clearUponHandler(78)
    DisableAttackRestOfMove()
    sprite('nt431_09', 9)	# 59-67	 **attackbox here**
    SFX_3('ntse_08')
    sprite('nt431_10', 7)	# 68-74
    setInvincible(0)
    Unknown3029(0)
    sprite('nt431_11', 9)	# 75-83
    sprite('nt431_12', 9)	# 84-92
    sprite('nt203_14', 9)	# 93-101

@State
def UltimateEdgeAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2800)
        Hitstop(3)
        MinimumDamagePct(10)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(58000)
        AirUntechableTime(300)
        Unknown11056(0)
        Unknown11084(1)
        Unknown11064(1)
        SLOT_59 = 1
        Unknown2073(1)
        setInvincible(1)
        Unknown1084(1)
        callSubroutine('Dash_AfterImage')

        def upon_78():
            clearUponHandler(78)
            Hitstop(20)
            Unknown11001(0, 0, 0)
            Unknown11069('UltimateEdgeAssault_Exe_OD')
            Unknown13024(0)
            enterState('UltimateEdgeAssault_Exe_OD')
            Unknown21015('6e7465665f3433315f4f44000000000000000000000000000000000000000000ba0b000000000000')
            Unknown13024(0)
        Unknown23159('UltimateEdgeAssault_TC')
    sprite('nt431_00', 3)	# 1-3
    sprite('nt431_01', 3)	# 4-6
    tag_voice(1, 'bnt255_0', 'bnt255_1', '', '')
    Unknown2036(40, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    GFX_0('ntef_430_bloodMatome', -1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    Unknown36(1)
    Unknown1096(3000)
    Unknown35()
    sprite('nt431_02', 3)	# 7-9
    sprite('nt431_03', 3)	# 10-12
    sprite('nt431_01', 3)	# 13-15
    sprite('nt431_02', 3)	# 16-18
    sprite('nt431_03', 3)	# 19-21
    sprite('nt431_01', 3)	# 22-24
    sprite('nt431_02', 3)	# 25-27
    sprite('nt431_04', 5)	# 28-32
    sprite('nt431_05', 5)	# 33-37
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    sprite('nt431_06', 5)	# 38-42
    physicsXImpulse(3000)
    sprite('nt431_07', 5)	# 43-47
    Unknown1019(200)
    Unknown8007(100, 1, 1)
    sprite('nt431_08', 5)	# 48-52
    Unknown1019(400)
    GFX_0('ntef_431_OD', -1)
    Unknown23029(1, 3004, 0)
    SFX_3('ntse_07')
    SFX_3('ntse_07')
    sprite('nt431_09', 1)	# 53-53	 **attackbox here**
    Unknown1019(0)
    sprite('nt431_09', 5)	# 54-58	 **attackbox here**
    clearUponHandler(78)
    DisableAttackRestOfMove()
    sprite('nt431_09', 9)	# 59-67	 **attackbox here**
    SFX_3('ntse_08')
    sprite('nt431_10', 7)	# 68-74
    setInvincible(0)
    Unknown3029(0)
    sprite('nt431_11', 9)	# 75-83
    sprite('nt431_12', 9)	# 84-92
    sprite('nt203_14', 9)	# 93-101

@State
def UltimateEdgeAssault_Exe_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(5500)
        AttackP1(48)
        AttackP2(100)
        MinimumDamagePct(18)
        Hitstop(45)
        GroundedHitstunAnimation(1)
        AirPushbackX(2000)
        AirPushbackY(54000)
        AirUntechableTime(100)
        Unknown9016(1)
        Unknown11064(1)
        Unknown11084(1)
        Unknown13024(0)
        Unknown30048(1)
        Unknown11069('ntef_431OdLastSubMato')
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        else:
            Unknown3029(1)
            Unknown3069(1)
            Unknown3070(3)
            Unknown3071(5)
        Unknown23022(1)
        EnableCollision(0)
        Unknown20000(1)
        Unknown20003(1)
        Unknown2053(0)
        Unknown2034(0)
    sprite('nt431_09', 5)	# 1-5	 **attackbox here**
    StartMultihit()
    sprite('nt431_10', 6)	# 6-11
    sprite('nt431_11', 6)	# 12-17
    sprite('nt431_12', 6)	# 18-23
    Unknown12046(250)
    sprite('nt431_13', 4)	# 24-27
    Unknown36(22)
    Unknown1086(22)
    teleportRelativeX(-300000)
    teleportRelativeY(1750000)
    physicsYImpulse(-50000)
    setGravity(0)
    Unknown35()
    Unknown23024(2)
    sprite('nt431_14', 4)	# 28-31
    sprite('nt431_15', 4)	# 32-35
    GFX_0('ntef_431OD', -1)
    sprite('nt431_16', 4)	# 36-39
    sprite('nt431_17', 4)	# 40-43
    SFX_3('ntse_04')
    sprite('nt431_18', 4)	# 44-47
    sprite('nt431_19', 4)	# 48-51
    sprite('nt431_20', 2)	# 52-53
    tag_voice(0, 'bnt258_0', 'bnt258_1', '', '')
    sprite('nt431_21', 2)	# 54-55
    Unknown20000(0)
    Unknown20003(0)
    Unknown2053(1)
    Unknown2034(1)
    Unknown2004(1, 0)
    sprite('nt431_22', 2)	# 56-57	 **attackbox here**
    RefreshMultihit()
    Hitstop(45)
    SFX_0('025_cleanhit_slash')
    sprite('nt431_23', 5)	# 58-62
    GFX_0('ntef_431OdLastSubMato', -1)
    Unknown12046(0)
    SFX_0('025_cleanhit_slash')
    sprite('nt431_24', 5)	# 63-67
    sprite('nt431_25', 5)	# 68-72
    sprite('nt431_26', 5)	# 73-77
    sprite('nt431_27', 5)	# 78-82
    sprite('nt431_28', 35)	# 83-117
    Unknown13024(1)
    sprite('nt431_28', 10)	# 118-127
    Unknown23024(0)
    sprite('nt431_29', 6)	# 128-133
    sprite('nt431_30', 6)	# 134-139

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11069('AstralHeat')
        AttackLevel_(5)
        Unknown11064(1)
        Damage(0)
        hitstun(20)
        Unknown9016(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(220)
        Unknown9142(200)
        hitstun(200)
        Unknown11057(1500)
        Unknown11084(1)
        Unknown11068(1)
        Unknown11078(1)
        MinimumDamagePct(100)

        def upon_12():
            clearUponHandler(12)
            Hitstop(0)
            sendToLabel(0)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown11023(1)
            Unknown2053(0)
            Unknown2034(0)
            Unknown2006()
            Unknown1084(1)
            PushbackX(19800)
            Unknown20000(1)
            Unknown20003(1)
            Unknown20004(1)
            Unknown23084(1)
            Unknown2004(1, 0)
            Unknown36(22)
            Unknown2053(0)
            Unknown2034(0)
            Unknown35()
        setInvincible(1)
        SLOT_66 = 1
    sprite('nt451_00', 3)	# 1-3
    sprite('nt451_01', 3)	# 4-6
    tag_voice(1, 'bnt290_0', 'bnt290_1', '', '')
    Unknown2036(54, -1, 1)
    Unknown23147()
    GFX_0('EMB_NT_AH', -1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    GFX_0('ntef_451aura', -1)
    GFX_0('ntef_430_aura00', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(-600)
    Unknown35()
    sprite('nt451_02', 3)	# 7-9
    sprite('nt451_03', 3)	# 10-12
    sprite('nt451_01', 3)	# 13-15
    GFX_0('ntef_451aura', -1)
    sprite('nt451_02', 3)	# 16-18
    sprite('nt451_03', 3)	# 19-21
    sprite('nt451_01', 3)	# 22-24
    GFX_0('ntef_451aura', -1)
    sprite('nt451_02', 3)	# 25-27
    sprite('nt451_03', 3)	# 28-30
    sprite('nt451_01', 3)	# 31-33
    GFX_0('ntef_451aura', -1)
    GFX_0('ntef_430_aura00', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(-600)
    Unknown35()
    sprite('nt451_02', 3)	# 34-36
    sprite('nt451_03', 3)	# 37-39
    sprite('nt451_01', 3)	# 40-42
    Unknown4054(11)
    GFX_0('ntef_451aura', -1)
    sprite('nt451_02', 3)	# 43-45
    sprite('nt451_03', 3)	# 46-48
    sprite('nt451_01', 3)	# 49-51
    GFX_0('ntef_451aura', -1)
    GFX_0('ntef_430_aura00', -1)
    Unknown36(1)
    Unknown1007(200000)
    Unknown1097(-600)
    Unknown35()
    sprite('nt451_02', 3)	# 52-54
    sprite('nt451_03', 3)	# 55-57
    sprite('nt451_01', 3)	# 58-60
    sprite('nt451_04', 4)	# 61-64
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    sprite('nt451_05', 4)	# 65-68
    SFX_3('ntse_04')
    sprite('nt451_06', 6)	# 69-74	 **attackbox here**
    sprite('nt451_07', 15)	# 75-89
    GFX_0('ntef_451', -1)
    setInvincible(0)
    sprite('nt451_50', 4)	# 90-93
    sprite('nt203_12', 3)	# 94-96
    sprite('nt203_13', 3)	# 97-99
    sprite('nt203_14', 3)	# 100-102
    loopRest()
    ExitState()
    label(0)
    sprite('nt451_07', 4)	# 103-106
    GFX_0('ntef_451_hit', -1)
    clearUponHandler(1)
    GFX_0('ntef_451_BG', -1)
    sprite('nt451_07', 2)	# 107-108
    Unknown2015(300)
    sprite('nt451_07', 2)	# 109-110
    Unknown2015(350)
    sprite('nt451_07', 2)	# 111-112
    Unknown2015(400)
    sprite('nt451_07', 2)	# 113-114
    Unknown2015(450)
    sprite('nt451_07', 2)	# 115-116
    Unknown2015(500)
    sprite('nt451_07', 2)	# 117-118
    Unknown2015(550)
    sprite('nt451_07', 2)	# 119-120
    Unknown2015(600)
    sprite('nt451_07', 2)	# 121-122
    Unknown2015(650)
    sprite('nt451_07', 2)	# 123-124
    Unknown2015(700)
    sprite('nt451_07', 2)	# 125-126
    Unknown2015(750)
    sprite('nt451_07', 5)	# 127-131
    Unknown2015(800)
    sprite('nt451_08', 6)	# 132-137
    Unknown2015(-1)
    sprite('nt451_09', 4)	# 138-141
    Unknown20009(800)
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 142-144
    tag_voice(0, 'bnt291_0', 'bnt291_1', '', '')
    GFX_0('ntef_451_2', -1)
    sprite('nt451_11', 3)	# 145-147
    sprite('nt451_12', 3)	# 148-150
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 151-153
    sprite('nt451_11', 3)	# 154-156
    sprite('nt451_12', 3)	# 157-159
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 160-162
    sprite('nt451_11', 3)	# 163-165
    sprite('nt451_12', 3)	# 166-168
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 169-171
    sprite('nt451_11', 3)	# 172-174
    sprite('nt451_12', 3)	# 175-177
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 178-180
    sprite('nt451_11', 3)	# 181-183
    sprite('nt451_12', 3)	# 184-186
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 187-189
    sprite('nt451_11', 3)	# 190-192
    sprite('nt451_12', 3)	# 193-195
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 196-198
    sprite('nt451_11', 3)	# 199-201
    sprite('nt451_12', 3)	# 202-204
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 205-207
    sprite('nt451_11', 3)	# 208-210
    sprite('nt451_12', 3)	# 211-213
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 214-216
    sprite('nt451_11', 3)	# 217-219
    sprite('nt451_12', 3)	# 220-222
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 223-225
    sprite('nt451_11', 3)	# 226-228
    sprite('nt451_12', 3)	# 229-231
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 232-234
    sprite('nt451_11', 3)	# 235-237
    sprite('nt451_12', 3)	# 238-240
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 241-243
    sprite('nt451_11', 3)	# 244-246
    sprite('nt451_12', 3)	# 247-249
    SFX_3('ntse_01')
    if SLOT_43:
        _gotolabel(1)
    sprite('nt451_10', 3)	# 250-252
    sprite('nt451_11', 3)	# 253-255
    sprite('nt451_12', 3)	# 256-258
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 259-261
    sprite('nt451_11', 3)	# 262-264
    sprite('nt451_12', 3)	# 265-267
    SFX_3('ntse_01')
    sprite('nt451_10', 3)	# 268-270
    sprite('nt451_11', 3)	# 271-273
    sprite('nt451_12', 3)	# 274-276
    SFX_3('ntse_01')
    label(1)
    sprite('nt451_13', 4)	# 277-280
    Unknown20009(1000)
    Unknown21015('6e7465665f3435315f3200000000000000000000000000000000000000000000a10f000000000000')
    sprite('nt451_14', 5)	# 281-285
    sprite('nt451_15', 6)	# 286-291
    SFX_3('ntse_04')
    sprite('nt451_16', 5)	# 292-296
    sprite('nt451_17', 5)	# 297-301	 **attackbox here**
    RefreshMultihit()
    Damage(2100)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(2500)
    hitstun(300)
    Hitstop(1)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    teleportRelativeX(350000)
    Unknown35()
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(10000, 10000)
    sprite('nt451_18', 8)	# 302-309
    sprite('nt451_19', 4)	# 310-313
    SFX_3('ntse_04')
    sprite('nt451_20', 6)	# 314-319
    sprite('nt451_21', 3)	# 320-322	 **attackbox here**
    GFX_0('ntef_451slash2', 0)
    RefreshMultihit()
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    teleportRelativeX(350000)
    Unknown35()
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_22', 6)	# 323-328
    sprite('nt451_23', 6)	# 329-334
    sprite('nt451_24', 4)	# 335-338
    SFX_3('ntse_04')
    sprite('nt451_25', 4)	# 339-342
    sprite('nt451_26', 3)	# 343-345	 **attackbox here**
    GFX_0('ntef_451slash', 0)
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(10000)
    ScreenShake(0, 5000)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    teleportRelativeX(350000)
    Unknown35()
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_27', 7)	# 346-352
    sprite('nt451_51', 4)	# 353-356
    sprite('nt451_52', 4)	# 357-360
    sprite('nt451_16', 5)	# 361-365
    tag_voice(0, 'bnt292_0', 'bnt292_1', '', '')
    SFX_3('ntse_04')
    sprite('nt451_17', 5)	# 366-370	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    PushbackX(5000)
    hitstun(300)
    Hitstop(1)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    teleportRelativeX(350000)
    Unknown35()
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_18', 8)	# 371-378
    sprite('nt451_19', 4)	# 379-382
    SFX_3('ntse_04')
    sprite('nt451_20', 6)	# 383-388
    sprite('nt451_21', 3)	# 389-391	 **attackbox here**
    GFX_0('ntef_451slash2', 0)
    RefreshMultihit()
    AirHitstunAnimation(4)
    GroundedHitstunAnimation(4)
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_22', 6)	# 392-397
    sprite('nt451_23', 6)	# 398-403
    sprite('nt451_24', 4)	# 404-407
    SFX_3('ntse_04')
    sprite('nt451_25', 4)	# 408-411
    sprite('nt451_26', 3)	# 412-414	 **attackbox here**
    GFX_0('ntef_451slash', 0)
    RefreshMultihit()
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    ScreenShake(0, 5000)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    teleportRelativeX(350000)
    Unknown35()
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_27', 7)	# 415-421
    sprite('nt451_28', 4)	# 422-425
    sprite('nt451_29', 5)	# 426-430
    SFX_3('ntse_04')
    sprite('nt451_30', 4)	# 431-434
    sprite('nt451_31', 5)	# 435-439	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    PushbackX(0)
    Unknown11072(1, 400000, 0)
    GFX_0('ntef_431OdLastSub', 1)
    Unknown36(1)
    teleportRelativeX(350000)
    Unknown35()
    SFX_0('103_hit_counter_slash_2')
    ScreenShake(20000, 20000)
    sprite('nt451_32', 3)	# 440-442
    sprite('nt451_33', 3)	# 443-445
    sprite('nt451_34', 4)	# 446-449
    sprite('nt451_35', 4)	# 450-453
    sprite('nt451_36', 3)	# 454-456
    Unknown21015('6e7465665f3435315f3200000000000000000000000000000000000000000000a20f000000000000')
    sprite('nt451_37', 3)	# 457-459
    sprite('nt451_38', 3)	# 460-462
    sprite('nt451_36', 3)	# 463-465
    sprite('nt451_37', 3)	# 466-468
    sprite('nt451_38', 3)	# 469-471
    sprite('nt451_36', 3)	# 472-474
    sprite('nt451_37', 3)	# 475-477
    sprite('nt451_38', 3)	# 478-480
    sprite('nt451_36', 3)	# 481-483
    sprite('nt451_37', 3)	# 484-486
    sprite('nt451_38', 3)	# 487-489
    sprite('nt451_36', 3)	# 490-492
    sprite('nt451_37', 3)	# 493-495
    sprite('nt451_38', 3)	# 496-498
    sprite('nt451_36', 3)	# 499-501
    sprite('nt451_37', 3)	# 502-504
    sprite('nt451_38', 3)	# 505-507
    sprite('nt451_36', 3)	# 508-510
    sprite('nt451_37', 3)	# 511-513
    sprite('nt451_38', 3)	# 514-516
    sprite('nt451_36', 3)	# 517-519
    sprite('nt451_37', 3)	# 520-522
    sprite('nt451_38', 3)	# 523-525
    sprite('nt451_36', 3)	# 526-528
    sprite('nt451_37', 3)	# 529-531
    sprite('nt451_38', 3)	# 532-534
    sprite('nt451_36', 3)	# 535-537
    if SLOT_43:
        _gotolabel(2)
    sprite('nt451_37', 3)	# 538-540
    sprite('nt451_38', 3)	# 541-543
    sprite('nt451_36', 3)	# 544-546
    sprite('nt451_37', 3)	# 547-549
    sprite('nt451_38', 3)	# 550-552
    sprite('nt451_36', 3)	# 553-555
    sprite('nt451_37', 3)	# 556-558
    sprite('nt451_38', 3)	# 559-561
    SFX_3('ntse_04')
    label(2)
    sprite('nt451_39', 3)	# 562-564
    tag_voice(0, 'bnt293_0', 'bnt293_1', '', '')
    Unknown21015('6e7465665f343531736c6173685f6b7975736875000000000000000000000000a40f000000000000')
    GFX_0('ntef_451_BG', -1)
    sprite('nt451_40', 10)	# 565-574	 **attackbox here**
    Unknown21015('6e7465665f3435315f3200000000000000000000000000000000000000000000a30f000000000000')
    RefreshMultihit()
    Damage(5300)
    PushbackX(0)
    Hitstop(20)
    AirHitstunAnimation(5)
    GroundedHitstunAnimation(5)
    Unknown11072(0, 0, 0)
    SFX_0('025_cleanhit_slash')
    sprite('nt451_40', 10)	# 575-584	 **attackbox here**
    GFX_1('tef_451_end', -1)
    sprite('nt451_40', 1)	# 585-585	 **attackbox here**
    RefreshMultihit()
    Damage(10000)
    Unknown11064(3)
    AirPushbackY(30000)
    AirPushbackX(100000)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Hitstop(0)

    def upon_11():
        Unknown36(22)
        Unknown3001(0)
        Unknown35()
    sprite('nt451_41', 3)	# 586-588
    sprite('nt451_42', 3)	# 589-591
    GFX_0('ntef_451SubMato', -1)
    sprite('nt451_43', 3)	# 592-594
    sprite('nt451_41', 3)	# 595-597
    sprite('nt451_42', 3)	# 598-600
    sprite('nt451_43', 3)	# 601-603
    sprite('nt451_41', 3)	# 604-606
    sprite('nt451_42', 3)	# 607-609
    sprite('nt451_43', 3)	# 610-612
    sprite('nt451_41', 3)	# 613-615
    sprite('nt451_42', 3)	# 616-618
    sprite('nt451_43', 3)	# 619-621
    sprite('nt451_41', 3)	# 622-624
    sprite('nt451_42', 3)	# 625-627
    sprite('nt451_43', 3)	# 628-630
    sprite('nt451_41', 3)	# 631-633
    sprite('nt451_42', 3)	# 634-636
    sprite('nt451_43', 3)	# 637-639
    sprite('nt451_41', 3)	# 640-642
    sprite('nt451_42', 3)	# 643-645
    sprite('nt451_43', 3)	# 646-648
    sprite('nt451_41', 3)	# 649-651
    sprite('nt451_42', 3)	# 652-654
    sprite('nt451_43', 3)	# 655-657
    sprite('nt451_41', 3)	# 658-660
    sprite('nt451_42', 3)	# 661-663
    sprite('nt451_43', 3)	# 664-666
    sprite('nt451_44', 5)	# 667-671
    sprite('nt451_45', 5)	# 672-676
    sprite('nt451_46', 5)	# 677-681
    sprite('nt451_47', 65)	# 682-746
    Unknown1000(260000)
    SLOT_64 = 1
    Unknown26('ntef_451_BG')
    sprite('nt451_48', 8)	# 747-754
    sprite('nt451_49', 8)	# 755-762

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
    sprite('nt020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('nt020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('nt024_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        Hitstop(16)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11042(1)
        Unknown30040(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('nt212_00', 2)	# 1-2
    sprite('nt212_01', 4)	# 3-6
    Unknown7006('bnt111_0', 100, 829714018, 828322097, 0, 0, 100, 829714018, 845099313, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('nt212_02', 2)	# 7-8
    sprite('nt212_03', 6)	# 9-14
    physicsYImpulse(36000)
    setGravity(2200)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    if (SLOT_12 <= 17500):
        SLOT_12 = 17500
    if (SLOT_12 >= 37500):
        SLOT_12 = 37500
    Unknown8001(0, 0)
    SFX_0('000_airdash_1')
    sprite('nt212_04', 15)	# 15-29
    sendToLabelUpon(2, 9)
    Unknown23087(-100000)
    label(0)
    sprite('nt212_05', 3)	# 30-32
    SFX_0('004_swing_grap_1_2')
    sprite('nt212_06', 3)	# 33-35
    Unknown1019(80)
    Unknown1039(120)
    sprite('nt212_07', 2)	# 36-37	 **attackbox here**
    Unknown23087(-1)
    Unknown1019(60)
    sprite('nt212_08', 2)	# 38-39	 **attackbox here**
    sprite('nt212_09', 2)	# 40-41
    Recovery()
    Unknown2063()
    sprite('nt212_10', 1)	# 42-42
    sprite('nt212_11', 1)	# 43-43
    sprite('nt212_12', 20)	# 44-63
    label(9)
    sprite('nt212_13', 5)	# 64-68
    clearUponHandler(2)
    Unknown1084(1)
    Unknown3029(0)
    Unknown8000(100, 1, 1)
    JumpCancel_(1)
    sprite('nt212_14', 5)	# 69-73
    sprite('nt212_15', 5)	# 74-78
    sprite('nt212_16', 5)	# 79-83

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        Damage(2000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(3000)
        AirPushbackY(40000)
        AirUntechableTime(60)
        PushbackX(12000)
        Hitstop(16)
        Unknown9016(1)
        Unknown11042(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('nt213_00', 2)	# 1-2
    sprite('nt213_01', 2)	# 3-4
    GFX_0('ntef_D_bodyaura', 1)
    GFX_0('ntef_D_handaura', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt213_02', 1)	# 5-5
    sprite('nt213_03', 1)	# 6-6
    sprite('nt213_04ex01', 1)	# 7-7
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    sprite('nt213_05ex01', 1)	# 8-8	 **attackbox here**
    sprite('nt213_06ex01', 1)	# 9-9	 **attackbox here**
    Unknown7006('bnt110_0', 100, 829714018, 828321841, 0, 0, 100, 829714018, 845099057, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('ntse_04')
    sprite('nt213_07ex01', 3)	# 10-12	 **attackbox here**
    Unknown14073('ShortDash')
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    GFX_1('ntef_D_aura', 6)
    GFX_1('ntef_D_aura', 7)
    GFX_1('ntef_D_aura', 8)
    GFX_1('ntef_D_aura', 9)
    GFX_1('ntef_D_aura', 10)
    sprite('nt213_08ex01', 3)	# 13-15	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt213_09ex01', 5)	# 16-20	 **attackbox here**
    Recovery()
    sprite('nt213_10ex01', 5)	# 21-25	 **attackbox here**
    sprite('nt213_11', 5)	# 26-30
    sprite('nt213_12', 6)	# 31-36
    sprite('nt213_13', 6)	# 37-42

@State
def CmnActChangePartnerAssistAtk_C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(50)
        AttackP1(70)
        Hitstop(12)
        AirPushbackX(10000)
        AirPushbackY(33000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown1084(1)
        Unknown9016(1)
        Unknown11056(0)
        Unknown11042(1)
        Unknown2006()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('nt404_00', 4)	# 1-4
    physicsXImpulse(4000)
    GFX_1('ntef_D_aura', 0)
    Unknown8010(100, 1, 0)
    sprite('nt404_01', 4)	# 5-8
    Unknown7006('bnt204_0', 100, 846491234, 828322864, 0, 0, 100, 846491234, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('ntse_04')
    GFX_1('ntef_D_aura', 0)
    sprite('nt404_02', 2)	# 9-10
    Unknown1019(300)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown8007(100, 1, 1)
    sprite('nt404_03', 2)	# 11-12
    Unknown1019(400)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    Unknown8009(0)
    sprite('nt404_04', 3)	# 13-15	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    if (SLOT_19 <= 200000):
        Unknown48('190000000200000033000000160000000200000025000000')
    sprite('nt404_05', 3)	# 16-18
    Unknown1019(80)
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    Recovery()
    sprite('nt404_06', 3)	# 19-21
    Unknown1019(50)
    Unknown3029(0)
    loopRest()
    Unknown19(9, 2, 52)
    sprite('nt404_10', 2)	# 22-23
    Unknown2015(-1)
    EnableCollision(1)
    Unknown2005()
    Unknown1019(80)
    sprite('nt404_11', 3)	# 24-26
    Unknown3029(0)
    Unknown8000(100, 1, 0)
    Unknown1019(60)
    sprite('nt404_11', 4)	# 27-30
    Unknown8010(0, 1, 1)
    sprite('nt404_12', 3)	# 31-33
    Unknown1019(60)
    Unknown8010(0, 1, 0)
    sprite('nt404_12', 4)	# 34-37
    Unknown8010(0, 1, 0)
    sprite('nt210_11ex01', 2)	# 38-39
    Unknown1019(0)
    sprite('nt210_12ex01', 2)	# 40-41
    Unknown1019(0)
    sprite('nt210_13ex01', 3)	# 42-44
    ExitState()
    label(9)
    sprite('nt404_07', 4)	# 45-48
    Unknown1019(30)
    EnableCollision(1)
    sprite('nt404_08', 4)	# 49-52
    Unknown1019(30)
    sprite('nt404_09', 4)	# 53-56
    Unknown3029(0)
    Unknown1019(30)
    sprite('nt402_10', 4)	# 57-60
    Unknown1019(30)
    sprite('nt402_11', 4)	# 61-64
    Unknown1019(0)

@State
def CmnActChangePartnerAttackIn():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerDD():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown30063(1)
        if SLOT_162:
            SLOT_58 = 1

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)	# 1-1
    Unknown2036(71, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('nt020_07', 4)	# 3-6
    sprite('nt020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('AN_CmnActChangePartnerDDODExe')
    else:
        enterState('AN_CmnActChangePartnerDDExe')

@State
def AN_CmnActChangePartnerDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(4)
        Damage(400)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(28000)
        AirUntechableTime(100)
        Unknown9310(20)
        Unknown11056(2)
        Unknown11064(1)
        Unknown11062(1)
        Unknown1084(1)
        Unknown30019('0000000001000000')

        def upon_STATE_END():
            EnableCollision(1)
            Unknown23087(0)
            Unknown12046(0)
    sprite('nt440_00', 2)	# 1-2
    setInvincible(1)
    Unknown1084(1)
    sprite('nt312_01ex01', 33)	# 3-35
    sprite('nt440_01', 2)	# 36-37
    sprite('nt440_04', 3)	# 38-40
    physicsXImpulse(4000)
    sprite('nt440_05', 3)	# 41-43
    Unknown1019(200)
    sprite('nt440_06', 3)	# 44-46
    sprite('nt440_07', 3)	# 47-49	 **attackbox here**
    Unknown23087(150000)
    Unknown1019(200)
    Unknown8001(3, 100)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('nt440_08', 1)	# 50-50
    Unknown7006('bnt281_0', 100, 846491234, 828322104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    setInvincible(0)
    Unknown12046(10)
    sprite('nt440_08', 1)	# 51-51
    Unknown12046(20)
    sprite('nt440_09', 1)	# 52-52
    Unknown12046(30)
    sprite('nt440_09', 1)	# 53-53
    Unknown12046(40)
    sprite('nt440_09', 1)	# 54-54
    Unknown12046(50)
    sprite('nt440_10', 1)	# 55-55
    Unknown12046(60)
    sprite('nt440_10', 1)	# 56-56
    Unknown12046(70)
    sprite('nt440_10', 1)	# 57-57
    Unknown12046(80)
    sprite('nt440_11', 1)	# 58-58
    Unknown12046(90)
    sprite('nt440_11', 1)	# 59-59
    Unknown12046(100)
    sprite('nt440_11', 1)	# 60-60
    sprite('nt440_12', 3)	# 61-63
    GFX_1('ntef_611_end', 0)
    GFX_1('ntef_611_end', 1)
    SFX_3('ntse_09')
    sprite('nt440_13', 3)	# 64-66
    sprite('nt440_14', 3)	# 67-69
    YAccel(150)
    SFX_3('ntse_04')
    sprite('nt440_15', 3)	# 70-72
    YAccel(150)
    sprite('nt440_16', 3)	# 73-75
    YAccel(150)
    sendToLabelUpon(2, 1)
    sprite('nt440_16', 30)	# 76-105
    Unknown1019(150)
    YAccel(200)
    label(1)
    sprite('nt440_17', 2)	# 106-107	 **attackbox here**
    clearUponHandler(2)
    Unknown1084(1)
    Damage(800)
    Hitstop(8)
    Unknown11001(-5, -5, -5)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-200000)
    Unknown11072(1, 350000, 0)
    Unknown9016(1)
    RefreshMultihit()
    sprite('nt440_18', 3)	# 108-110	 **attackbox here**
    GFX_0('ntef_440Axe', -1)
    Unknown8000(100, 1, 1)
    Unknown12046(0)
    Damage(800)
    Hitstop(9)
    Unknown11001(-1, -1, -1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(28000)
    AirPushbackY(35000)
    Unknown11072(0, 0, 0)
    Unknown11064(0)
    Unknown9310(10)
    Unknown23086(1)
    RefreshMultihit()
    sprite('nt440_19', 3)	# 111-113	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown12046(0)
    sprite('nt440_20', 3)	# 114-116	 **attackbox here**
    sprite('nt440_19', 3)	# 117-119	 **attackbox here**
    sprite('nt440_20', 3)	# 120-122	 **attackbox here**
    sprite('nt440_19', 3)	# 123-125	 **attackbox here**
    sprite('nt440_20', 3)	# 126-128	 **attackbox here**
    sprite('nt440_19', 3)	# 129-131	 **attackbox here**
    Unknown26('BurstDD_Camera')
    sprite('nt440_20', 3)	# 132-134	 **attackbox here**
    sprite('nt440_21', 4)	# 135-138
    sprite('nt440_22', 4)	# 139-142
    sprite('nt440_23', 4)	# 143-146
    sprite('nt440_24', 4)	# 147-150
    sprite('nt403_09ex01', 4)	# 151-154
    sprite('nt403_10ex01', 4)	# 155-158
    sprite('nt403_11ex01', 4)	# 159-162
    sprite('nt601_06ex01', 5)	# 163-167
    sprite('nt601_07ex01', 5)	# 168-172
    sprite('nt601_08ex01', 8)	# 173-180
    SFX_0('019_cloth_a')
    sprite('nt601_09ex01', 5)	# 181-185

@State
def AN_CmnActChangePartnerDDODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(4)
        Damage(400)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(20000)
        AirPushbackY(28000)
        AirUntechableTime(100)
        Unknown9310(20)
        Unknown11056(2)
        Unknown11064(1)
        Unknown11062(1)
        Unknown1084(1)
        Unknown30019('0000000001000000')

        def upon_STATE_END():
            EnableCollision(1)
            Unknown23087(0)
            Unknown12046(0)
    sprite('nt440_00', 2)	# 1-2
    setInvincible(1)
    Unknown1084(1)
    sprite('nt312_01ex01', 33)	# 3-35
    sprite('nt440_01', 2)	# 36-37
    sprite('nt440_04', 3)	# 38-40
    physicsXImpulse(4000)
    sprite('nt440_05', 3)	# 41-43
    Unknown1019(200)
    sprite('nt440_06', 3)	# 44-46
    sprite('nt440_07', 3)	# 47-49	 **attackbox here**
    Unknown23087(150000)
    Unknown1019(200)
    Unknown8001(3, 100)
    physicsYImpulse(30000)
    setGravity(1800)
    sprite('nt440_08', 1)	# 50-50
    Unknown7006('bnt281_0', 100, 846491234, 828322104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    setInvincible(0)
    Unknown12046(10)
    sprite('nt440_08', 1)	# 51-51
    Unknown12046(20)
    sprite('nt440_09', 1)	# 52-52
    Unknown12046(30)
    sprite('nt440_09', 1)	# 53-53
    Unknown12046(40)
    sprite('nt440_09', 1)	# 54-54
    Unknown12046(50)
    sprite('nt440_10', 1)	# 55-55
    Unknown12046(60)
    sprite('nt440_10', 1)	# 56-56
    Unknown12046(70)
    sprite('nt440_10', 1)	# 57-57
    Unknown12046(80)
    sprite('nt440_11', 1)	# 58-58
    Unknown12046(90)
    sprite('nt440_11', 1)	# 59-59
    Unknown12046(100)
    sprite('nt440_11', 1)	# 60-60
    sprite('nt440_12', 3)	# 61-63
    GFX_1('ntef_611_end', 0)
    GFX_1('ntef_611_end', 1)
    SFX_3('ntse_09')
    sprite('nt440_13', 3)	# 64-66
    sprite('nt440_14', 3)	# 67-69
    YAccel(150)
    SFX_3('ntse_04')
    sprite('nt440_15', 3)	# 70-72
    YAccel(150)
    sprite('nt440_16', 3)	# 73-75
    YAccel(150)
    sendToLabelUpon(2, 1)
    sprite('nt440_16', 30)	# 76-105
    Unknown1019(150)
    YAccel(200)
    label(1)
    sprite('nt440_17', 2)	# 106-107	 **attackbox here**
    clearUponHandler(2)
    Unknown1084(1)
    Damage(350)
    Hitstop(13)
    Unknown11001(-10, -10, -10)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    AirPushbackX(0)
    AirPushbackY(-200000)
    Unknown11072(1, 300000, 0)
    Unknown9016(1)
    RefreshMultihit()
    sprite('nt440_18', 3)	# 108-110	 **attackbox here**
    GFX_0('ntef_440Axe', -1)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    Damage(350)
    Hitstop(1)
    Unknown11001(4, 4, 4)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(70000)
    AirPushbackY(30000)
    Unknown11072(0, 0, 0)
    Unknown11055(1)
    Unknown11057(700)
    Unknown23086(1)
    RefreshMultihit()
    GFX_0('ntef_440LastEx', -1)
    sprite('nt440_19', 3)	# 111-113	 **attackbox here**
    sprite('nt440_20', 3)	# 114-116	 **attackbox here**
    RefreshMultihit()
    sprite('nt440_19', 3)	# 117-119	 **attackbox here**
    sprite('nt440_20', 3)	# 120-122	 **attackbox here**
    RefreshMultihit()
    sprite('nt440_19', 3)	# 123-125	 **attackbox here**
    sprite('nt440_20', 3)	# 126-128	 **attackbox here**
    RefreshMultihit()
    sprite('nt440_19', 3)	# 129-131	 **attackbox here**
    sprite('nt440_20', 3)	# 132-134	 **attackbox here**
    Unknown12046(0)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(28000)
    AirPushbackY(35000)
    Hitstop(0)
    Unknown11001(20, 20, 20)
    Unknown9310(10)
    Unknown11057(1000)
    Unknown11064(0)
    RefreshMultihit()
    sprite('nt440_19', 3)	# 135-137	 **attackbox here**
    sprite('nt440_20', 3)	# 138-140	 **attackbox here**
    sprite('nt440_19', 3)	# 141-143	 **attackbox here**
    sprite('nt440_20', 3)	# 144-146	 **attackbox here**
    sprite('nt440_19', 3)	# 147-149	 **attackbox here**
    sprite('nt440_20', 3)	# 150-152	 **attackbox here**
    sprite('nt440_19', 3)	# 153-155	 **attackbox here**
    sprite('nt440_20', 3)	# 156-158	 **attackbox here**
    sprite('nt440_19', 3)	# 159-161	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown12046(0)
    sprite('nt440_20', 3)	# 162-164	 **attackbox here**
    sprite('nt440_19', 3)	# 165-167	 **attackbox here**
    sprite('nt440_20', 3)	# 168-170	 **attackbox here**
    sprite('nt440_19', 3)	# 171-173	 **attackbox here**
    sprite('nt440_20', 3)	# 174-176	 **attackbox here**
    sprite('nt440_19', 3)	# 177-179	 **attackbox here**
    Unknown26('BurstDD_Camera')
    sprite('nt440_20', 3)	# 180-182	 **attackbox here**
    sprite('nt440_21', 4)	# 183-186
    sprite('nt440_22', 4)	# 187-190
    sprite('nt440_23', 4)	# 191-194
    sprite('nt440_24', 4)	# 195-198
    sprite('nt403_09ex01', 4)	# 199-202
    sprite('nt403_10ex01', 4)	# 203-206
    sprite('nt403_11ex01', 4)	# 207-210
    sprite('nt601_06ex01', 5)	# 211-215
    sprite('nt601_07ex01', 5)	# 216-220
    sprite('nt601_08ex01', 8)	# 221-228
    SFX_0('019_cloth_a')
    sprite('nt601_09ex01', 5)	# 229-233

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
    sprite('null', 5)	# 121-125
    sprite('nt251_00', 3)	# 126-128
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    Unknown1007(1000000)
    physicsXImpulse(60000)
    physicsYImpulse(-40000)
    sprite('nt251_01', 3)	# 129-131
    sprite('nt251_02', 2)	# 132-133
    SFX_0('004_swing_grap_1_1')
    SFX_0('000_airdash_2')
    label(1)
    sprite('nt251_03', 3)	# 134-136	 **attackbox here**
    sprite('nt251_04', 3)	# 137-139	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 140-142
    Unknown1084(1)
    sprite('nt024_00', 5)	# 143-147
    sprite('nt024_01', 18)	# 148-165
    Unknown8000(100, 1, 1)
    sprite('nt024_02', 5)	# 166-170

@State
def CmnActChangeReturnAppealBurst():
    sprite('nt111_07', 50)	# 1-50
    sprite('nt111_08', 5)	# 51-55
    sprite('nt111_09', 30)	# 56-85

@Subroutine
def MouthTableInit():
    Unknown18011('bnt000', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt520', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt520', '001')
    Unknown18011('bnt521', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt521', '002')
    Unknown18011('bnt522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt522', '003')
    Unknown18011('bnt523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt523', '004')
    Unknown30092('bnt524', '005')
    Unknown30092('bnt525', '006')
    Unknown18011('bnt540', 12643, 12336, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt540', '007')
    Unknown18011('bnt541', 12643, 12336, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt541', '008')
    Unknown18011('bnt542', 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24885, 25397, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt542', '009')
    Unknown18011('bnt543', 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt543', '010')
    Unknown18011('bnt544', 13665, 13667, 13665, 13667, 13665, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt544', '011')
    Unknown18011('bnt545', 12643, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt545', '012')
    Unknown18011('bnt402_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt402_1', 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt403_0', 14177, 14691, 12641, 25394, 12338, 14689, 14435, 14433, 14435, 14177, 13923, 14689, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt403_1', 14689, 14179, 14177, 13667, 13665, 13667, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13665, 13667, 12641, 25394, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt600brg', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 13667, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600brg', '017')
    Unknown18011('bnt601brc', 14433, 14435, 12641, 25392, 12341, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601brc', '018')
    Unknown18011('bnt601bny', 12641, 25392, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 13621, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601bny', '019')
    Unknown18011('bnt600bhz', 13665, 13667, 13665, 13667, 13665, 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600bhz', '020')
    Unknown18011('bnt601bes', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 13621, 14177, 14179, 14177, 14179, 14177, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601bes', '021')
    Unknown18011('bnt601bma', 12641, 25394, 13875, 12641, 25397, 14385, 13921, 13923, 14433, 14435, 14433, 14179, 24888, 12849, 12643, 24882, 25400, 24888, 25400, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601bma', '022')
    Unknown18011('bnt600pyo', 12897, 25396, 13362, 14433, 14435, 14433, 14435, 14177, 13923, 24880, 25398, 12849, 14433, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600pyo', '023')
    Unknown18011('bnt602pyo', 12641, 25400, 14385, 12641, 25394, 12849, 12641, 25398, 14385, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt602pyo', '024')
    Unknown18011('bnt601pna', 12641, 25400, 14388, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601pna', '025')
    Unknown18011('bnt601pla', 14689, 14691, 14689, 14691, 14689, 13411, 24888, 12849, 12643, 24882, 25398, 24886, 25400, 24888, 25400, 24888, 25401, 24889, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601pla', '026')
    Unknown18011('bnt601uca', 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 12337, 12641, 25394, 14388, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 24887, 13361, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601uca', '027')
    Unknown18011('bnt600ugo', 14433, 14435, 12641, 25392, 12337, 12641, 25392, 12337, 14433, 14179, 24882, 25400, 24888, 25400, 24888, 25400, 24888, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600ugo', '028')
    Unknown18011('bnt601uyu', 12641, 25395, 13105, 12641, 25395, 13620, 14433, 14435, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601uyu', '029')
    Unknown18011('bnt600ryn', 14433, 14435, 14433, 14435, 14433, 13411, 24885, 25400, 24888, 25400, 12849, 12641, 25392, 12337, 12641, 25394, 12337, 12641, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600ryn', '030')
    Unknown18011('bnt600uak', 12641, 25392, 24886, 25400, 24886, 25400, 12851, 14433, 14435, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14435, 14177, 14435, 14433, 13923, 13921, 13923, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600uak', '031')
    Unknown18011('bnt600kym', 13409, 25392, 24886, 25400, 24888, 25400, 13620, 13921, 13923, 13921, 13923, 13921, 12899, 24884, 25400, 24888, 25400, 24886, 25400, 24886, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt600kym', '032')
    Unknown18011('bnt601pku', 14433, 13923, 14433, 14435, 14433, 14435, 14433, 13411, 24885, 25401, 24889, 25401, 13873, 13921, 13923, 13921, 13923, 13921, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt601pku', '033')
    Unknown18011('bnt700brg', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13155, 13921, 13155, 13921, 13155, 13409, 13667, 13665, 13667, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700brg', '034')
    Unknown18011('bnt700brc', 14433, 14435, 14433, 13411, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700brc', '035')
    Unknown18011('bnt700bny', 12899, 24885, 25399, 12340, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700bny', '036')
    Unknown18011('bnt701bhz', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701bhz', '037')
    Unknown18011('bnt701bes', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25398, 24886, 25398, 24886, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701bes', '038')
    Unknown18011('bnt701bma', 14433, 13155, 24880, 13618, 14435, 24888, 12337, 12643, 24880, 12337, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701bma', '039')
    Unknown18011('bnt701pyo', 14433, 14435, 12641, 25394, 12340, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 12643, 24882, 25400, 24888, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701pyo', '040')
    Unknown18011('bnt700pna', 12641, 25397, 14389, 12641, 25396, 13361, 14177, 14179, 13921, 13923, 13921, 13923, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700pna', '041')
    Unknown18011('bnt700pla', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 12337, 12641, 25392, 12853, 14433, 13923, 13921, 14435, 14433, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700pla', '042')
    Unknown18011('bnt700uca', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700uca', '043')
    Unknown18011('bnt700ugo', 14435, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700ugo', '044')
    Unknown18011('bnt702ugo', 12641, 25394, 12849, 12641, 25394, 13619, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt702ugo', '045')
    Unknown18011('bnt700uyu', 13665, 13411, 24880, 25401, 24889, 12337, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt700uyu', '046')
    Unknown18011('bnt701ryn', 12641, 25392, 12339, 14689, 14691, 14177, 14179, 14177, 14179, 13921, 13923, 14433, 14435, 12641, 25392, 24888, 12849, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701ryn', '047')
    Unknown18011('bnt701uak', 14433, 14435, 14689, 14691, 14689, 14691, 14177, 14179, 14689, 14691, 14433, 14435, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701uak', '048')
    Unknown18011('bnt701kym', 14433, 14435, 14433, 13923, 14177, 13923, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 13923, 13921, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701kym', '049')
    Unknown18011('bnt701pku', 12897, 25392, 24886, 12849, 12643, 24882, 12337, 12643, 24880, 12337, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bnt701pku', '050')
    if SLOT_172:
        Unknown18011('bnt000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt520', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt521', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 12897, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt522', 12643, 14177, 14179, 14177, 14179, 13665, 12899, 24884, 25399, 24887, 25395, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt523', 12643, 14177, 14179, 14177, 14179, 14433, 14179, 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt540', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt541', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 24888, 25399, 24887, 25399, 25393, 24883, 25399, 24887, 25399, 24887, 25399, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt542', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 24889, 25393, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24884, 25399, 24887, 25397, 24881, 25399, 24887, 25399, 24887, 25396, 24881, 25397, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt543', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 24883, 25399, 24887, 25397, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt544', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 13921, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt545', 12643, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24883, 25399, 24887, 25399, 24887, 25399, 25397, 24883, 25399, 24887, 25396, 12337, 14177, 14179, 14177, 14179, 13409, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt402_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt402_1', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 24882, 25399, 24887, 25399, 24887, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt403_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt403_1', 12643, 12899, 14177, 14179, 14177, 12643, 13155, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600brg', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 24884, 25399, 24887, 25399, 25396, 24882, 25399, 24887, 25399, 24887, 25398, 24889, 25399, 24887, 25399, 24887, 25399, 25399, 24884, 25399, 24887, 25399, 24887, 25398, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601brc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 12643, 13411, 14177, 13155, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601bny', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 13667, 14177, 13155, 24886, 25399, 24887, 25399, 24887, 25399, 25396, 13873, 14177, 14179, 14177, 12899, 14177, 14179, 14177, 13667, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 25397, 12593, 14177, 13411, 13667, 14177, 14179, 14177, 13411, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601bes', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 24888, 25399, 25399, 24884, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 13923, 13921, 13155, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601bma', 12643, 12643, 14177, 14179, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24887, 25399, 12595, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 14177, 12643, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600pyo', 12643, 12643, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 13923, 14177, 14179, 14177, 13411, 13411, 14177, 14179, 14177, 12899, 14177, 13667, 12899, 24885, 25399, 24887, 25395, 12851, 14177, 14179, 12641, 25395, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt602pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13155, 24880, 25399, 25393, 24883, 25399, 25393, 24882, 25399, 25399, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601pla', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 24887, 25399, 25394, 24882, 25399, 24887, 25399, 25399, 24883, 25399, 24887, 25399, 24887, 25399, 25396, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601uca', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 24883, 25399, 24887, 25399, 25394, 24885, 25399, 24887, 25396, 13873, 14177, 14179, 14177, 12643, 13155, 14177, 14179, 14689, 14179, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601uyu', 12643, 12899, 14177, 14179, 13921, 13155, 14177, 14179, 14177, 12643, 14179, 14177, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600ryn', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 24882, 25399, 24887, 25399, 25396, 24886, 25399, 24887, 25393, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600uak', 12643, 12899, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 24880, 25399, 24887, 25398, 24882, 25399, 24887, 25399, 24887, 25399, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt600kym', 12643, 12643, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 14179, 12641, 13155, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt601pku', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13411, 14177, 14179, 14177, 14179, 14177, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700brg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700brc', 12643, 12899, 14177, 14179, 14177, 13155, 12643, 14177, 13667, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13411, 14177, 14179, 14177, 13155, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700bny', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701bhz', 12643, 12643, 14177, 13923, 13411, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701bes', 12643, 12643, 14177, 14179, 14177, 14179, 14433, 14179, 13155, 24883, 25399, 24887, 24887, 25399, 24887, 25399, 25395, 24883, 25399, 24887, 25399, 24887, 25399, 25393, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701bma', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 24887, 25399, 25394, 24881, 25399, 25396, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701pyo', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13411, 14177, 14179, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700pna', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700pla', 12643, 12643, 14177, 12643, 12643, 14177, 14179, 13411, 14177, 14179, 12643, 14177, 14179, 14177, 12899, 14177, 14179, 13665, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700uca', 12643, 12643, 14177, 13667, 12899, 14177, 14179, 14177, 13411, 12643, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 12897, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700ugo', 12643, 12643, 14177, 14179, 14177, 12899, 13155, 24889, 25399, 24887, 25399, 24887, 25399, 25395, 24881, 25399, 24887, 25399, 24887, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt702ugo', 12643, 12643, 14177, 14179, 14433, 14179, 12899, 24886, 25399, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt700uyu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701ryn', 12643, 12643, 14177, 14179, 13665, 12643, 24883, 25399, 24887, 25399, 24887, 25395, 24881, 25399, 24887, 25399, 24887, 25393, 24883, 25399, 24887, 25399, 25399, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701uak', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701kym', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 14179, 13923, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bnt701pku', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24882, 25393, 24883, 25399, 24887, 25395, 24882, 25399, 24887, 25399, 25396, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bny')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('bhz')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bes')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('bma')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('pyo')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('pna')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('pla')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('uca')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('ugo')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('ryn')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('uak')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('pku')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('kym')
    if SLOT_ReturnVal:
        _gotolabel(240)
    PartnerChar('brc')
    if SLOT_ReturnVal:
        _gotolabel(250)
    Unknown19(991, 2, 158)
    random_(2, 0, 25)
    if SLOT_ReturnVal:
        _gotolabel(3)
    random_(2, 0, 33)
    if SLOT_ReturnVal:
        _gotolabel(1)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(2)
    label(0)
    sprite('nt600_00', 6)	# 2-7
    sprite('nt600_01', 7)	# 8-14
    sprite('nt600_02', 7)	# 15-21
    sprite('nt600_03', 7)	# 22-28
    sprite('nt600_04', 7)	# 29-35
    sprite('nt600_03', 7)	# 36-42
    sprite('nt600_02', 7)	# 43-49
    sprite('nt600_01', 7)	# 50-56
    sprite('nt600_02', 7)	# 57-63
    sprite('nt600_03', 7)	# 64-70
    sprite('nt600_04', 14)	# 71-84
    SFX_1('bnt520')
    sprite('nt600_03', 7)	# 85-91
    sprite('nt600_02', 7)	# 92-98
    sprite('nt600_01', 7)	# 99-105
    sprite('nt600_05', 7)	# 106-112
    sprite('nt600_06', 7)	# 113-119
    sprite('nt600_07', 7)	# 120-126
    sprite('nt600_06', 7)	# 127-133
    sprite('nt600_05', 7)	# 134-140
    sprite('nt600_06', 7)	# 141-147
    sprite('nt600_07', 14)	# 148-161
    sprite('nt600_06', 7)	# 162-168
    sprite('nt600_05', 7)	# 169-175
    sprite('nt600_01', 6)	# 176-181
    sprite('nt600_00', 8)	# 182-189
    sprite('nt600_08', 8)	# 190-197
    sprite('nt600_09', 8)	# 198-205
    sprite('nt600_10', 8)	# 206-213
    sprite('nt600_11', 8)	# 214-221
    sprite('nt600_12', 8)	# 222-229
    Unknown23018(1)
    loopRest()
    ExitState()
    label(1)
    sprite('nt600_00', 6)	# 230-235
    sprite('nt600_01', 6)	# 236-241
    SFX_1('bnt521')
    sprite('nt600_13', 6)	# 242-247
    sprite('nt600_14', 6)	# 248-253
    sprite('nt600_15', 20)	# 254-273
    sprite('nt600_01', 6)	# 274-279
    sprite('nt600_16', 6)	# 280-285
    sprite('nt600_17', 6)	# 286-291
    sprite('nt600_18', 20)	# 292-311
    sprite('nt600_01', 6)	# 312-317
    sprite('nt600_00', 8)	# 318-325
    sprite('nt600_08', 8)	# 326-333
    sprite('nt600_09', 8)	# 334-341
    sprite('nt600_10', 8)	# 342-349
    sprite('nt600_11', 8)	# 350-357
    sprite('nt600_12', 8)	# 358-365
    Unknown23018(1)
    loopRest()
    ExitState()
    label(2)
    sprite('nt300_00', 7)	# 366-372
    sprite('nt300_01', 7)	# 373-379
    sprite('nt300_02', 7)	# 380-386
    sprite('nt300_03', 7)	# 387-393
    sprite('nt300_04', 8)	# 394-401
    SFX_1('bnt521')
    sprite('nt300_03', 7)	# 402-408
    sprite('nt300_02', 7)	# 409-415
    sprite('nt300_03', 7)	# 416-422
    sprite('nt300_04', 8)	# 423-430
    sprite('nt300_03', 7)	# 431-437
    sprite('nt300_02', 7)	# 438-444
    sprite('nt300_05', 7)	# 445-451
    sprite('nt300_06', 7)	# 452-458
    sprite('nt300_07', 6)	# 459-464
    sprite('nt300_08', 6)	# 465-470
    sprite('nt300_09', 7)	# 471-477
    sprite('nt300_08', 6)	# 478-483
    sprite('nt300_07', 6)	# 484-489
    sprite('nt300_08', 6)	# 490-495
    sprite('nt300_09', 7)	# 496-502
    sprite('nt300_08', 6)	# 503-508
    sprite('nt300_07', 6)	# 509-514
    sprite('nt300_10', 7)	# 515-521
    sprite('nt300_11', 6)	# 522-527
    sprite('nt300_12', 6)	# 528-533
    Unknown23018(1)
    loopRest()
    ExitState()
    label(3)
    sprite('nt601_01', 8)	# 534-541
    sprite('nt601_02', 8)	# 542-549
    sprite('nt601_01', 8)	# 550-557
    sprite('nt601_00', 8)	# 558-565
    sprite('nt601_01', 8)	# 566-573
    sprite('nt601_02', 14)	# 574-587
    sprite('nt601_03', 7)	# 588-594
    sprite('nt601_04', 7)	# 595-601
    sprite('nt601_05', 80)	# 602-681
    Unknown7006('bnt522', 100, 896822882, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('nt601_05', 70)	# 682-751
    sprite('nt601_06', 9)	# 752-760
    sprite('nt601_07', 9)	# 761-769
    sprite('nt601_08', 9)	# 770-778
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 779-783
    Unknown23018(1)
    loopRest()
    ExitState()
    label(100)
    sprite('nt602_00', 20)	# 784-803
    Unknown1000(-1356000)
    Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabelUpon(2, 104)
        sendToLabel(102)
    sprite('nt602_00', 1)	# 804-804
    SFX_1('bnt600brg')
    label(101)
    sprite('nt602_00', 1)	# 805-805
    if SLOT_97:
        _gotolabel(101)
    sprite('nt602_00', 60)	# 806-865
    sprite('nt602_00', 1)	# 866-866
    Unknown21007(24, 40)
    sprite('nt602_00', 32767)	# 867-33633
    label(102)
    sprite('nt033_00', 1)	# 33634-33634
    sprite('nt033_01', 3)	# 33635-33637
    physicsXImpulse(-10000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('nt033_02', 3)	# 33638-33640
    loopRest()
    label(103)
    sprite('nt033_01', 3)	# 33641-33643
    sprite('nt033_02', 3)	# 33644-33646
    loopRest()
    gotoLabel(103)
    label(104)
    sprite('nt033_03', 1)	# 33647-33647
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('nt033_04', 2)	# 33648-33649
    sprite('nt033_05', 2)	# 33650-33651
    sprite('nt033_06', 2)	# 33652-33653
    sprite('nt033_07', 2)	# 33654-33655
    sprite('nt601_06', 9)	# 33656-33664
    sprite('nt601_07', 9)	# 33665-33673
    sprite('nt601_08', 9)	# 33674-33682
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 33683-33687
    Unknown18008()
    label(105)
    sprite('nt000_00', 7)	# 33688-33694
    sprite('nt000_01', 7)	# 33695-33701
    sprite('nt000_02', 7)	# 33702-33708
    sprite('nt000_03', 7)	# 33709-33715
    sprite('nt000_04', 7)	# 33716-33722
    sprite('nt000_05', 7)	# 33723-33729
    sprite('nt000_06', 7)	# 33730-33736
    sprite('nt000_07', 7)	# 33737-33743
    sprite('nt000_08', 7)	# 33744-33750
    gotoLabel(105)
    ExitState()
    label(110)
    sprite('nt603_00', 1)	# 33751-33751
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(111)
    sprite('nt603_00', 32767)	# 33752-66518
    label(111)
    sprite('nt603_00', 6)	# 66519-66524
    sprite('nt603_01', 6)	# 66525-66530
    sprite('nt603_02', 6)	# 66531-66536
    sprite('nt603_03', 6)	# 66537-66542
    sprite('nt603_04', 6)	# 66543-66548
    sprite('nt603_05', 6)	# 66549-66554
    sprite('nt603_06', 6)	# 66555-66560
    sprite('nt603_07', 6)	# 66561-66566
    sprite('nt603_08', 12)	# 66567-66578
    sprite('nt603_07', 6)	# 66579-66584
    sprite('nt603_04', 1)	# 66585-66585
    SFX_1('bnt601bny')
    label(112)
    sprite('nt603_04', 1)	# 66586-66586
    if SLOT_97:
        _gotolabel(112)
    sprite('nt603_04', 45)	# 66587-66631
    sprite('nt603_09', 6)	# 66632-66637
    sprite('nt603_10', 6)	# 66638-66643
    Unknown21011(30)
    label(113)
    sprite('nt000_00', 7)	# 66644-66650
    sprite('nt000_01', 7)	# 66651-66657
    sprite('nt000_02', 7)	# 66658-66664
    sprite('nt000_03', 7)	# 66665-66671
    sprite('nt000_04', 7)	# 66672-66678
    sprite('nt000_05', 7)	# 66679-66685
    sprite('nt000_06', 7)	# 66686-66692
    sprite('nt000_07', 7)	# 66693-66699
    sprite('nt000_08', 7)	# 66700-66706
    loopRest()
    gotoLabel(113)
    label(120)
    sprite('nt601_01', 8)	# 66707-66714
    sprite('nt601_02', 8)	# 66715-66722
    sprite('nt601_01', 8)	# 66723-66730
    sprite('nt601_00', 8)	# 66731-66738
    sprite('nt601_01', 8)	# 66739-66746
    sprite('nt601_02', 14)	# 66747-66760
    sprite('nt601_03', 7)	# 66761-66767
    sprite('nt601_04', 7)	# 66768-66774
    sprite('nt601_05', 1)	# 66775-66775
    SFX_1('bnt600bhz')
    label(121)
    sprite('nt601_05', 1)	# 66776-66776
    if SLOT_97:
        _gotolabel(121)
    sprite('nt601_05', 24)	# 66777-66800
    sprite('nt601_06', 9)	# 66801-66809
    sprite('nt601_07', 9)	# 66810-66818
    sprite('nt601_08', 9)	# 66819-66827
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 66828-66832
    Unknown21007(24, 40)
    Unknown21011(120)
    label(122)
    sprite('nt000_00', 7)	# 66833-66839
    sprite('nt000_01', 7)	# 66840-66846
    sprite('nt000_02', 7)	# 66847-66853
    sprite('nt000_03', 7)	# 66854-66860
    sprite('nt000_04', 7)	# 66861-66867
    sprite('nt000_05', 7)	# 66868-66874
    sprite('nt000_06', 7)	# 66875-66881
    sprite('nt000_07', 7)	# 66882-66888
    sprite('nt000_08', 7)	# 66889-66895
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('nt000_00', 7)	# 66896-66902

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('nt000_01', 7)	# 66903-66909
    sprite('nt000_02', 7)	# 66910-66916
    sprite('nt000_03', 7)	# 66917-66923
    sprite('nt000_04', 7)	# 66924-66930
    sprite('nt000_05', 7)	# 66931-66937
    sprite('nt000_06', 7)	# 66938-66944
    sprite('nt000_07', 7)	# 66945-66951
    sprite('nt000_08', 7)	# 66952-66958
    sprite('nt000_00', 7)	# 66959-66965
    gotoLabel(131)
    label(132)
    sprite('nt615_00', 6)	# 66966-66971
    sprite('nt615_01', 6)	# 66972-66977
    sprite('nt615_02', 6)	# 66978-66983
    sprite('nt615_03', 12)	# 66984-66995
    sprite('nt615_04', 6)	# 66996-67001
    SFX_3('ntse_10')
    sprite('nt615_05', 20)	# 67002-67021
    sprite('nt615_06', 8)	# 67022-67029
    sprite('nt615_07', 32767)	# 67030-99796
    SFX_1('bnt601bes')
    Unknown23018(1)
    loopRest()
    label(140)
    sprite('nt601_00', 32767)	# 99797-132563
    Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(141)
    label(141)
    sprite('nt601_01', 5)	# 132564-132568
    sprite('nt601_02', 8)	# 132569-132576
    sprite('nt601_01', 5)	# 132577-132581
    sprite('nt601_00', 8)	# 132582-132589
    sprite('nt601_01', 5)	# 132590-132594
    sprite('nt601_02', 14)	# 132595-132608
    sprite('nt601_03', 7)	# 132609-132615
    sprite('nt601_04', 7)	# 132616-132622
    sprite('nt601_05', 1)	# 132623-132623
    SFX_1('bnt601bma')
    label(142)
    sprite('nt601_05', 1)	# 132624-132624
    if SLOT_97:
        _gotolabel(142)
    sprite('nt601_05', 30)	# 132625-132654
    sprite('nt601_06', 9)	# 132655-132663
    sprite('nt601_07', 9)	# 132664-132672
    sprite('nt601_08', 9)	# 132673-132681
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 132682-132686
    Unknown21011(30)
    label(143)
    sprite('nt000_00', 7)	# 132687-132693
    sprite('nt000_01', 7)	# 132694-132700
    sprite('nt000_02', 7)	# 132701-132707
    sprite('nt000_03', 7)	# 132708-132714
    sprite('nt000_04', 7)	# 132715-132721
    sprite('nt000_05', 7)	# 132722-132728
    sprite('nt000_06', 7)	# 132729-132735
    sprite('nt000_07', 7)	# 132736-132742
    sprite('nt000_08', 7)	# 132743-132749
    loopRest()
    gotoLabel(143)
    label(150)
    sprite('nt615_00', 6)	# 132750-132755
    Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    sprite('nt615_01', 6)	# 132756-132761
    sprite('nt615_02', 6)	# 132762-132767
    sprite('nt615_03', 12)	# 132768-132779
    sprite('nt615_04', 6)	# 132780-132785
    SFX_3('ntse_10')
    sprite('nt615_05', 20)	# 132786-132805
    sprite('nt615_06', 8)	# 132806-132813
    sprite('nt615_07', 1)	# 132814-132814
    SFX_1('bnt600pyo')
    label(151)
    sprite('nt615_07', 1)	# 132815-132815
    if SLOT_97:
        _gotolabel(151)
    sprite('nt615_07', 30)	# 132816-132845
    sprite('nt615_07', 32767)	# 132846-165612
    Unknown21007(24, 40)
    label(152)
    sprite('nt408_00', 1)	# 165613-165613
    physicsXImpulse(3000)
    callSubroutine('Dash_AfterImage')
    sprite('nt408_00', 3)	# 165614-165616
    Unknown1019(200)
    sprite('nt408_01', 4)	# 165617-165620
    SFX_3('ntse_12')
    sprite('nt408_02', 4)	# 165621-165624
    Unknown3001(200)
    Unknown3004(-10)
    sprite('nt408_02', 4)	# 165625-165628
    Unknown1019(600)
    sprite('nt408_03', 4)	# 165629-165632
    Unknown1019(50)
    sprite('nt408_04', 3)	# 165633-165635
    Unknown1019(50)
    sprite('nt408_05', 3)	# 165636-165638
    Unknown1019(50)
    Unknown3001(160)
    Unknown3004(20)
    sprite('nt408_06', 3)	# 165639-165641
    Unknown2018(1, 60)
    Unknown3029(0)
    sprite('nt408_07', 4)	# 165642-165645
    sprite('nt408_08', 3)	# 165646-165648
    sprite('nt620_00', 60)	# 165649-165708
    Unknown2005()
    Unknown3001(255)
    Unknown3004(0)
    physicsXImpulse(0)
    sprite('nt032_00', 1)	# 165709-165709
    Unknown2053(0)
    Unknown2034(0)
    physicsXImpulse(20000)
    Unknown2037(2)
    SFX_1('bnt602pyo')
    sprite('nt032_00', 1)	# 165710-165710
    Unknown23018(1)
    label(153)
    sprite('nt032_01', 3)	# 165711-165713
    SLOT_2 = (SLOT_2 + (-1))
    sprite('nt032_02', 3)	# 165714-165716
    sprite('nt032_03', 4)	# 165717-165720
    Unknown8006(100, 1, 1)
    sprite('nt032_04', 3)	# 165721-165723
    sprite('nt032_05', 3)	# 165724-165726
    sprite('nt032_06', 3)	# 165727-165729
    Unknown8006(100, 1, 1)
    sprite('nt032_07', 4)	# 165730-165733
    sprite('nt032_08', 3)	# 165734-165736
    loopRest()
    if SLOT_2:
        _gotolabel(153)
    label(154)
    sprite('nt032_01', 3)	# 165737-165739
    sprite('nt032_02', 3)	# 165740-165742
    sprite('nt032_03', 4)	# 165743-165746
    sprite('nt032_04', 3)	# 165747-165749
    sprite('nt032_05', 3)	# 165750-165752
    sprite('nt032_06', 3)	# 165753-165755
    sprite('nt032_07', 4)	# 165756-165759
    sprite('nt032_08', 3)	# 165760-165762
    loopRest()
    gotoLabel(154)
    label(160)
    sprite('nt600_00', 6)	# 165763-165768
    sprite('nt600_01', 7)	# 165769-165775
    sprite('nt600_02', 7)	# 165776-165782
    sprite('nt600_03', 7)	# 165783-165789
    sprite('nt600_04', 7)	# 165790-165796
    sprite('nt600_03', 7)	# 165797-165803
    sprite('nt600_02', 10)	# 165804-165813
    sprite('nt600_03', 7)	# 165814-165820
    sprite('nt600_04', 21)	# 165821-165841
    sprite('nt600_03', 7)	# 165842-165848
    sprite('nt600_02', 7)	# 165849-165855
    sprite('nt600_01', 11)	# 165856-165866
    sprite('nt600_05', 7)	# 165867-165873
    sprite('nt600_06', 7)	# 165874-165880
    sprite('nt600_07', 7)	# 165881-165887
    sprite('nt600_06', 7)	# 165888-165894
    sprite('nt600_05', 10)	# 165895-165904
    sprite('nt600_06', 7)	# 165905-165911
    sprite('nt600_07', 21)	# 165912-165932
    sprite('nt600_06', 7)	# 165933-165939
    sprite('nt600_05', 7)	# 165940-165946
    sprite('nt600_01', 6)	# 165947-165952
    sprite('nt600_13', 6)	# 165953-165958
    sprite('nt600_14', 6)	# 165959-165964
    sprite('nt600_15', 25)	# 165965-165989
    sprite('nt600_01', 6)	# 165990-165995
    sprite('nt600_16', 6)	# 165996-166001
    sprite('nt600_17', 6)	# 166002-166007
    sprite('nt600_18', 25)	# 166008-166032
    sprite('nt600_01', 6)	# 166033-166038
    sprite('nt600_00', 8)	# 166039-166046
    sprite('nt600_08', 8)	# 166047-166054
    sprite('nt600_09', 8)	# 166055-166062
    sprite('nt600_10', 8)	# 166063-166070
    sprite('nt600_11', 8)	# 166071-166078
    sprite('nt600_12', 8)	# 166079-166086
    sprite('nt000_00', 7)	# 166087-166093
    SFX_1('bnt601pna')
    Unknown23018(1)
    label(161)
    sprite('nt000_01', 7)	# 166094-166100
    sprite('nt000_02', 7)	# 166101-166107
    sprite('nt000_03', 7)	# 166108-166114
    sprite('nt000_04', 7)	# 166115-166121
    sprite('nt000_05', 7)	# 166122-166128
    sprite('nt000_06', 7)	# 166129-166135
    sprite('nt000_07', 7)	# 166136-166142
    sprite('nt000_08', 7)	# 166143-166149
    sprite('nt000_00', 7)	# 166150-166156
    gotoLabel(161)
    label(170)
    sprite('nt603_00', 1)	# 166157-166157

    def upon_40():
        clearUponHandler(40)
        sendToLabel(171)
    sprite('nt603_00', 32767)	# 166158-198924
    label(171)
    sprite('nt603_00', 6)	# 198925-198930
    sprite('nt603_01', 6)	# 198931-198936
    sprite('nt603_02', 6)	# 198937-198942
    sprite('nt603_03', 6)	# 198943-198948
    sprite('nt603_04', 6)	# 198949-198954
    sprite('nt603_05', 6)	# 198955-198960
    sprite('nt603_06', 6)	# 198961-198966
    sprite('nt603_07', 6)	# 198967-198972
    sprite('nt603_08', 12)	# 198973-198984
    sprite('nt603_07', 6)	# 198985-198990
    sprite('nt603_04ex02', 1)	# 198991-198991
    SFX_1('bnt601pla')
    label(172)
    sprite('nt603_04ex02', 1)	# 198992-198992
    if SLOT_97:
        _gotolabel(172)
    sprite('nt603_04ex02', 15)	# 198993-199007
    sprite('nt603_04ex01', 40)	# 199008-199047
    sprite('nt603_09', 6)	# 199048-199053
    sprite('nt603_10', 6)	# 199054-199059
    Unknown21011(30)
    label(173)
    sprite('nt000_00', 7)	# 199060-199066
    sprite('nt000_01', 7)	# 199067-199073
    sprite('nt000_02', 7)	# 199074-199080
    sprite('nt000_03', 7)	# 199081-199087
    sprite('nt000_04', 7)	# 199088-199094
    sprite('nt000_05', 7)	# 199095-199101
    sprite('nt000_06', 7)	# 199102-199108
    sprite('nt000_07', 7)	# 199109-199115
    sprite('nt000_08', 7)	# 199116-199122
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('nt601_00', 32767)	# 199123-231889
    Unknown1000(-1465000)
    Unknown2019(-100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(181)
    label(181)
    sprite('nt601_01', 5)	# 231890-231894
    sprite('nt601_02', 8)	# 231895-231902
    sprite('nt601_01', 5)	# 231903-231907
    sprite('nt601_00', 8)	# 231908-231915
    sprite('nt601_01', 5)	# 231916-231920
    sprite('nt601_02', 14)	# 231921-231934
    sprite('nt601_03', 7)	# 231935-231941
    sprite('nt601_04', 7)	# 231942-231948
    sprite('nt601_05', 1)	# 231949-231949
    SFX_1('bnt601uca')
    label(182)
    sprite('nt601_05', 1)	# 231950-231950
    if SLOT_97:
        _gotolabel(182)
    sprite('nt601_05', 30)	# 231951-231980
    sprite('nt601_06', 9)	# 231981-231989
    sprite('nt601_07', 9)	# 231990-231998
    sprite('nt601_08', 9)	# 231999-232007
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 232008-232012
    Unknown21011(30)
    label(183)
    sprite('nt000_00', 7)	# 232013-232019
    sprite('nt000_01', 7)	# 232020-232026
    sprite('nt000_02', 7)	# 232027-232033
    sprite('nt000_03', 7)	# 232034-232040
    sprite('nt000_04', 7)	# 232041-232047
    sprite('nt000_05', 7)	# 232048-232054
    sprite('nt000_06', 7)	# 232055-232061
    sprite('nt000_07', 7)	# 232062-232068
    sprite('nt000_08', 7)	# 232069-232075
    loopRest()
    gotoLabel(183)
    label(190)
    sprite('nt601_01', 5)	# 232076-232080
    Unknown1000(-1465000)
    Unknown2019(-100)
    sprite('nt601_02', 8)	# 232081-232088
    sprite('nt601_01', 5)	# 232089-232093
    sprite('nt601_00', 8)	# 232094-232101
    sprite('nt601_01', 5)	# 232102-232106
    sprite('nt601_02', 14)	# 232107-232120
    sprite('nt601_03', 7)	# 232121-232127
    sprite('nt601_04', 7)	# 232128-232134
    sprite('nt601_05', 1)	# 232135-232135
    SFX_1('bnt600ugo')
    label(191)
    sprite('nt601_05', 1)	# 232136-232136
    if SLOT_97:
        _gotolabel(191)
    sprite('nt601_05', 80)	# 232137-232216
    sprite('nt601_06', 9)	# 232217-232225
    sprite('nt601_07', 9)	# 232226-232234
    sprite('nt601_08', 9)	# 232235-232243
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 232244-232248
    Unknown21007(24, 40)
    Unknown21011(30)
    label(192)
    sprite('nt000_00', 7)	# 232249-232255
    sprite('nt000_01', 7)	# 232256-232262
    sprite('nt000_02', 7)	# 232263-232269
    sprite('nt000_03', 7)	# 232270-232276
    sprite('nt000_04', 7)	# 232277-232283
    sprite('nt000_05', 7)	# 232284-232290
    sprite('nt000_06', 7)	# 232291-232297
    sprite('nt000_07', 7)	# 232298-232304
    sprite('nt000_08', 7)	# 232305-232311
    loopRest()
    gotoLabel(192)
    label(210)
    sprite('nt600_00', 6)	# 232312-232317
    sprite('nt600_01', 7)	# 232318-232324
    sprite('nt600_02', 7)	# 232325-232331
    sprite('nt600_03', 7)	# 232332-232338
    sprite('nt600_04', 21)	# 232339-232359
    sprite('nt600_03', 7)	# 232360-232366
    sprite('nt600_02', 7)	# 232367-232373
    sprite('nt600_01', 11)	# 232374-232384
    sprite('nt600_05', 7)	# 232385-232391
    sprite('nt600_06', 7)	# 232392-232398
    sprite('nt600_07', 21)	# 232399-232419
    sprite('nt600_06', 7)	# 232420-232426
    sprite('nt600_05', 7)	# 232427-232433
    sprite('nt600_01', 6)	# 232434-232439
    sprite('nt600_00', 8)	# 232440-232447
    sprite('nt600_08', 8)	# 232448-232455
    sprite('nt600_09', 8)	# 232456-232463
    sprite('nt600_10', 8)	# 232464-232471
    sprite('nt600_11', 8)	# 232472-232479
    sprite('nt600_12', 8)	# 232480-232487
    sprite('nt000_00', 7)	# 232488-232494
    SFX_1('bnt600ryn')
    label(211)
    sprite('nt000_01', 7)	# 232495-232501
    sprite('nt000_02', 7)	# 232502-232508
    sprite('nt000_03', 7)	# 232509-232515
    sprite('nt000_04', 7)	# 232516-232522
    sprite('nt000_05', 7)	# 232523-232529
    sprite('nt000_06', 7)	# 232530-232536
    sprite('nt000_07', 7)	# 232537-232543
    sprite('nt000_08', 7)	# 232544-232550
    sprite('nt000_00', 7)	# 232551-232557
    loopRest()
    if SLOT_97:
        _gotolabel(211)
    sprite('nt000_01', 7)	# 232558-232564
    Unknown21007(24, 40)
    Unknown21011(120)
    label(212)
    sprite('nt000_02', 7)	# 232565-232571
    sprite('nt000_03', 7)	# 232572-232578
    sprite('nt000_04', 7)	# 232579-232585
    sprite('nt000_05', 7)	# 232586-232592
    sprite('nt000_06', 7)	# 232593-232599
    sprite('nt000_07', 7)	# 232600-232606
    sprite('nt000_08', 7)	# 232607-232613
    sprite('nt000_00', 7)	# 232614-232620
    sprite('nt000_01', 7)	# 232621-232627
    loopRest()
    gotoLabel(212)
    label(220)
    sprite('nt601_01', 5)	# 232628-232632
    sprite('nt601_02', 8)	# 232633-232640
    sprite('nt601_01', 5)	# 232641-232645
    sprite('nt601_00', 8)	# 232646-232653
    sprite('nt601_01', 5)	# 232654-232658
    sprite('nt601_02', 14)	# 232659-232672
    sprite('nt601_03', 7)	# 232673-232679
    sprite('nt601_04', 7)	# 232680-232686
    sprite('nt601_05', 1)	# 232687-232687
    SFX_1('bnt600uak')
    label(221)
    sprite('nt601_05', 1)	# 232688-232688
    if SLOT_97:
        _gotolabel(221)
    sprite('nt601_05', 30)	# 232689-232718
    sprite('nt601_06', 9)	# 232719-232727
    sprite('nt601_07', 9)	# 232728-232736
    sprite('nt601_08', 9)	# 232737-232745
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 232746-232750
    sprite('nt000_00', 7)	# 232751-232757
    sprite('nt000_01', 7)	# 232758-232764
    sprite('nt000_02', 7)	# 232765-232771
    sprite('nt000_03', 7)	# 232772-232778
    sprite('nt000_04', 7)	# 232779-232785
    Unknown21007(24, 40)
    Unknown21011(30)
    sprite('nt000_05', 7)	# 232786-232792
    sprite('nt000_06', 7)	# 232793-232799
    sprite('nt000_07', 7)	# 232800-232806
    sprite('nt000_08', 7)	# 232807-232813
    label(222)
    sprite('nt000_00', 7)	# 232814-232820
    sprite('nt000_01', 7)	# 232821-232827
    sprite('nt000_02', 7)	# 232828-232834
    sprite('nt000_03', 7)	# 232835-232841
    sprite('nt000_04', 7)	# 232842-232848
    sprite('nt000_05', 7)	# 232849-232855
    sprite('nt000_06', 7)	# 232856-232862
    sprite('nt000_07', 7)	# 232863-232869
    sprite('nt000_08', 7)	# 232870-232876
    loopRest()
    gotoLabel(222)
    label(230)
    sprite('nt603_00', 1)	# 232877-232877

    def upon_40():
        clearUponHandler(40)
        sendToLabel(231)
    sprite('nt603_00', 32767)	# 232878-265644
    label(231)
    sprite('nt603_00', 6)	# 265645-265650
    sprite('nt603_01', 6)	# 265651-265656
    sprite('nt603_02', 6)	# 265657-265662
    sprite('nt603_03', 6)	# 265663-265668
    sprite('nt603_04', 6)	# 265669-265674
    sprite('nt603_05', 6)	# 265675-265680
    sprite('nt603_06', 6)	# 265681-265686
    sprite('nt603_07', 6)	# 265687-265692
    sprite('nt603_08', 12)	# 265693-265704
    sprite('nt603_07', 6)	# 265705-265710
    sprite('nt603_04ex02', 1)	# 265711-265711
    SFX_1('bnt601pku')
    label(232)
    sprite('nt603_04ex02', 1)	# 265712-265712
    if SLOT_97:
        _gotolabel(232)
    sprite('nt603_04ex02', 30)	# 265713-265742
    sprite('nt603_09', 6)	# 265743-265748
    sprite('nt603_10', 6)	# 265749-265754
    Unknown21007(24, 40)
    Unknown21011(120)
    label(233)
    sprite('nt000_00', 7)	# 265755-265761
    sprite('nt000_01', 7)	# 265762-265768
    sprite('nt000_02', 7)	# 265769-265775
    sprite('nt000_03', 7)	# 265776-265782
    sprite('nt000_04', 7)	# 265783-265789
    sprite('nt000_05', 7)	# 265790-265796
    sprite('nt000_06', 7)	# 265797-265803
    sprite('nt000_07', 7)	# 265804-265810
    sprite('nt000_08', 7)	# 265811-265817
    loopRest()
    gotoLabel(233)
    label(240)
    sprite('nt603_00', 6)	# 265818-265823
    sprite('nt603_01', 6)	# 265824-265829
    sprite('nt603_02', 6)	# 265830-265835
    sprite('nt603_03', 6)	# 265836-265841
    sprite('nt603_04', 6)	# 265842-265847
    sprite('nt603_05', 6)	# 265848-265853
    sprite('nt603_06', 6)	# 265854-265859
    sprite('nt603_07', 6)	# 265860-265865
    sprite('nt603_08', 12)	# 265866-265877
    sprite('nt603_07', 6)	# 265878-265883
    sprite('nt603_04ex02', 1)	# 265884-265884
    SFX_1('bnt600kym')
    label(241)
    sprite('nt603_04ex02', 1)	# 265885-265885
    if SLOT_97:
        _gotolabel(241)
    sprite('nt603_04ex02', 30)	# 265886-265915
    sprite('nt603_04ex01', 32767)	# 265916-298682
    Unknown21007(24, 40)
    Unknown21011(120)
    label(250)
    sprite('nt603_00', 1)	# 298683-298683
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(251)
    sprite('nt603_00', 32767)	# 298684-331450
    label(251)
    sprite('nt603_00', 6)	# 331451-331456
    sprite('nt603_01', 6)	# 331457-331462
    sprite('nt603_02', 6)	# 331463-331468
    sprite('nt603_03', 6)	# 331469-331474
    sprite('nt603_04', 6)	# 331475-331480
    sprite('nt603_05', 6)	# 331481-331486
    sprite('nt603_06', 6)	# 331487-331492
    sprite('nt603_07', 6)	# 331493-331498
    sprite('nt603_08', 12)	# 331499-331510
    sprite('nt603_07', 6)	# 331511-331516
    sprite('nt603_04', 1)	# 331517-331517
    SFX_1('bnt601brc')
    label(252)
    sprite('nt603_04', 1)	# 331518-331518
    if SLOT_97:
        _gotolabel(252)
    sprite('nt603_04', 20)	# 331519-331538
    sprite('nt603_09', 6)	# 331539-331544
    sprite('nt603_10', 6)	# 331545-331550
    Unknown21007(24, 40)
    Unknown21011(75)
    label(253)
    sprite('nt000_00', 7)	# 331551-331557
    sprite('nt000_01', 7)	# 331558-331564
    sprite('nt000_02', 7)	# 331565-331571
    sprite('nt000_03', 7)	# 331572-331578
    sprite('nt000_04', 7)	# 331579-331585
    sprite('nt000_05', 7)	# 331586-331592
    sprite('nt000_06', 7)	# 331593-331599
    sprite('nt000_07', 7)	# 331600-331606
    sprite('nt000_08', 7)	# 331607-331613
    loopRest()
    gotoLabel(253)
    label(991)
    sprite('nt000_00', 1)	# 331614-331614
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('nt000_00', 7)	# 331615-331621
    sprite('nt000_01', 7)	# 331622-331628
    sprite('nt000_02', 7)	# 331629-331635
    sprite('nt000_03', 7)	# 331636-331642
    sprite('nt000_04', 7)	# 331643-331649
    sprite('nt000_05', 7)	# 331650-331656
    sprite('nt000_06', 7)	# 331657-331663
    sprite('nt000_07', 7)	# 331664-331670
    sprite('nt000_08', 7)	# 331671-331677
    gotoLabel(992)
    ExitState()

@State
def CmnActRoundWin():
    sprite('nt615_00', 6)	# 1-6
    sprite('nt615_01', 6)	# 7-12
    sprite('nt615_02', 6)	# 13-18
    sprite('nt615_03', 12)	# 19-30
    sprite('nt615_04', 6)	# 31-36
    SFX_3('ntse_10')
    sprite('nt615_05', 20)	# 37-56
    sprite('nt615_06', 8)	# 57-64
    sprite('nt615_07', 32767)	# 65-32831
    Unknown7007('6e743430300000000000000000000000640000006e7434303100000000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown23018(1)
    loopRest()

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
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bes'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('uak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('pku'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('kym'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
            if PartnerChar('brc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(250)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if SLOT_64:
        _gotolabel(2)
    if (not SLOT_108):
        random_(2, 0, 50)
        if SLOT_ReturnVal:
            _gotolabel(2)
    label(1)
    sprite('nt610_00', 6)	# 4-9
    sprite('nt610_01', 6)	# 10-15
    sprite('nt610_02', 6)	# 16-21
    sprite('nt610_03', 6)	# 22-27
    sprite('nt610_04', 6)	# 28-33
    sprite('nt610_05', 55)	# 34-88
    if SLOT_158:
        if (not SLOT_52):
            if (not SLOT_108):
                Unknown7006('bnt542', 100, 896822882, 13108, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    GFX_1('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)	# 89-96
    if SLOT_158:
        if SLOT_52:
            SFX_1('bnt544')
        elif SLOT_108:
            Unknown7006('bnt402_0', 100, 880045666, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('nt610_07', 8)	# 97-104
    sprite('nt610_08', 8)	# 105-112
    sprite('nt610_09', 32767)	# 113-32879
    Unknown23018(1)
    label(2)
    sprite('nt611_00', 4)	# 32880-32883
    sprite('nt611_01', 4)	# 32884-32887
    sprite('nt611_02', 4)	# 32888-32891
    if SLOT_158:
        if SLOT_52:
            SFX_1('bnt545')
        else:
            Unknown7006('bnt540', 100, 896822882, 12596, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('nt611_03', 4)	# 32892-32895
    sprite('nt611_01', 4)	# 32896-32899
    sprite('nt611_02', 4)	# 32900-32903
    sprite('nt611_03', 4)	# 32904-32907
    sprite('nt611_01', 4)	# 32908-32911
    sprite('nt611_02', 4)	# 32912-32915
    sprite('nt611_03', 4)	# 32916-32919
    sprite('nt611_01', 4)	# 32920-32923
    sprite('nt611_02', 4)	# 32924-32927
    sprite('nt611_03', 4)	# 32928-32931
    sprite('nt611_01', 4)	# 32932-32935
    sprite('nt611_02', 4)	# 32936-32939
    sprite('nt611_03', 4)	# 32940-32943
    sprite('nt611_01', 4)	# 32944-32947
    sprite('nt611_02', 4)	# 32948-32951
    sprite('nt611_03', 4)	# 32952-32955
    sprite('nt611_01', 4)	# 32956-32959
    sprite('nt611_02', 4)	# 32960-32963
    sprite('nt611_03', 4)	# 32964-32967
    sprite('nt611_01', 4)	# 32968-32971
    sprite('nt611_02', 4)	# 32972-32975
    sprite('nt611_03', 4)	# 32976-32979
    sprite('nt611_01', 4)	# 32980-32983
    sprite('nt611_04', 4)	# 32984-32987
    GFX_0('ntef_611', -1)
    SFX_3('ntse_11')
    sprite('nt611_05', 4)	# 32988-32991
    sprite('nt611_06', 4)	# 32992-32995
    sprite('nt611_07', 4)	# 32996-32999
    sprite('nt611_08', 4)	# 33000-33003
    sprite('nt611_09', 32767)	# 33004-65770
    Unknown23018(1)
    label(100)
    sprite('nt611_00', 7)	# 65771-65777
    Unknown2019(-500)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(103)
    sprite('nt611_01', 4)	# 65778-65781
    SFX_1('bnt700brg')
    sprite('nt611_02', 4)	# 65782-65785
    sprite('nt611_03', 4)	# 65786-65789
    label(101)
    sprite('nt611_01', 4)	# 65790-65793
    sprite('nt611_02', 4)	# 65794-65797
    sprite('nt611_03', 4)	# 65798-65801
    if SLOT_97:
        _gotolabel(101)
    sprite('nt611_01', 4)	# 65802-65805
    Unknown21007(24, 40)
    sprite('nt611_02', 4)	# 65806-65809
    sprite('nt611_03', 4)	# 65810-65813
    label(102)
    sprite('nt611_01', 4)	# 65814-65817
    sprite('nt611_02', 4)	# 65818-65821
    sprite('nt611_03', 4)	# 65822-65825
    gotoLabel(102)
    label(103)
    sprite('nt611_04', 2)	# 65826-65827
    sprite('nt611_04', 4)	# 65828-65831
    GFX_0('ntef_611', -1)
    SFX_3('ntse_11')
    sprite('nt611_05', 4)	# 65832-65835
    sprite('nt611_06', 4)	# 65836-65839
    sprite('nt611_07', 4)	# 65840-65843
    sprite('nt611_08', 4)	# 65844-65847
    sprite('nt611_09', 32767)	# 65848-98614
    Unknown23018(1)
    label(110)
    sprite('nt610_00', 6)	# 98615-98620
    sprite('nt610_01', 6)	# 98621-98626
    sprite('nt610_02', 6)	# 98627-98632
    sprite('nt610_03', 6)	# 98633-98638
    sprite('nt610_04', 6)	# 98639-98644
    sprite('nt610_05', 1)	# 98645-98645
    SFX_1('bnt700bny')
    GFX_1('ntef_610_tameiki', 0)
    sprite('nt610_05', 30)	# 98646-98675
    sprite('nt610_06', 8)	# 98676-98683
    sprite('nt610_07', 8)	# 98684-98691
    sprite('nt610_08', 8)	# 98692-98699
    label(111)
    sprite('nt610_09', 1)	# 98700-98700
    if SLOT_97:
        _gotolabel(111)
    sprite('nt610_09', 32767)	# 98701-131467
    Unknown21007(24, 40)
    Unknown21011(290)
    label(120)
    sprite('keep', 1)	# 131468-131468
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(123)
        elif (SLOT_38 == 1):
            sendToLabel(123)
    label(121)
    sprite('nt603_10', 6)	# 131469-131474
    sprite('nt603_09', 6)	# 131475-131480
    sprite('nt603_08', 12)	# 131481-131492
    sprite('nt603_07', 6)	# 131493-131498
    sprite('nt603_06', 6)	# 131499-131504
    sprite('nt603_05', 6)	# 131505-131510
    sprite('nt603_04ex02', 32767)	# 131511-164277

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(122)
    sprite('nt603_04ex01', 32767)	# 164278-197044
    SFX_1('bnt701bhz')
    Unknown23018(1)
    label(123)
    sprite('nt003_00', 4)	# 197045-197048
    Unknown2005()
    sprite('nt003_01', 4)	# 197049-197052
    gotoLabel(121)
    label(130)
    sprite('keep', 1)	# 197053-197053
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(133)
        elif (SLOT_38 == 1):
            sendToLabel(133)
    label(131)
    sprite('nt603_10', 6)	# 197054-197059
    sprite('nt603_09', 6)	# 197060-197065
    sprite('nt603_08', 12)	# 197066-197077
    sprite('nt603_07', 6)	# 197078-197083
    sprite('nt603_06', 6)	# 197084-197089
    sprite('nt603_05', 6)	# 197090-197095
    sprite('nt603_04ex02', 32767)	# 197096-229862

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(132)
    sprite('nt603_04ex01', 32767)	# 229863-262629
    SFX_1('bnt701bes')
    Unknown23018(1)
    label(133)
    sprite('nt003_00', 4)	# 262630-262633
    Unknown2005()
    sprite('nt003_01', 4)	# 262634-262637
    gotoLabel(131)
    label(140)
    sprite('nt603_10', 6)	# 262638-262643
    sprite('nt603_09', 6)	# 262644-262649
    sprite('nt603_08', 12)	# 262650-262661
    sprite('nt603_07', 6)	# 262662-262667
    sprite('nt603_06', 6)	# 262668-262673
    sprite('nt603_05', 6)	# 262674-262679
    sprite('nt603_04ex02', 32767)	# 262680-295446

    def upon_40():
        clearUponHandler(40)
        sendToLabel(141)
    label(141)
    sprite('nt603_04ex01', 32767)	# 295447-328213
    SFX_1('bnt701bma')
    Unknown23018(1)
    label(150)
    sprite('nt000_00', 7)	# 328214-328220

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('nt000_01', 7)	# 328221-328227
    sprite('nt000_02', 7)	# 328228-328234
    sprite('nt000_03', 7)	# 328235-328241
    sprite('nt000_04', 7)	# 328242-328248
    sprite('nt000_05', 7)	# 328249-328255
    sprite('nt000_06', 7)	# 328256-328262
    sprite('nt000_07', 7)	# 328263-328269
    sprite('nt000_08', 7)	# 328270-328276
    sprite('nt000_00', 7)	# 328277-328283
    gotoLabel(151)
    label(152)
    sprite('nt603_10', 6)	# 328284-328289
    Unknown2013(24)
    sprite('nt603_09', 6)	# 328290-328295
    sprite('nt603_08', 12)	# 328296-328307
    sprite('nt603_07', 6)	# 328308-328313
    sprite('nt603_06', 6)	# 328314-328319
    sprite('nt603_05', 6)	# 328320-328325
    sprite('nt603_04ex02', 12)	# 328326-328337
    sprite('nt603_04ex01', 32767)	# 328338-361104
    SFX_1('bnt701pyo')
    Unknown23018(1)
    label(160)
    sprite('nt615_00', 6)	# 361105-361110
    sprite('nt615_01', 6)	# 361111-361116
    sprite('nt615_02', 6)	# 361117-361122
    sprite('nt615_03', 12)	# 361123-361134
    sprite('nt615_04', 6)	# 361135-361140
    SFX_3('ntse_10')
    sprite('nt615_05', 20)	# 361141-361160
    sprite('nt615_06', 8)	# 361161-361168
    sprite('nt615_07', 1)	# 361169-361169
    SFX_1('bnt700pna')
    label(161)
    sprite('nt615_07', 1)	# 361170-361170
    if SLOT_97:
        _gotolabel(161)
    sprite('nt615_07', 20)	# 361171-361190
    sprite('nt615_07', 32767)	# 361191-393957
    Unknown21007(24, 40)
    Unknown21011(180)
    label(170)
    sprite('nt615_00', 6)	# 393958-393963
    sprite('nt615_01', 6)	# 393964-393969
    sprite('nt615_02', 6)	# 393970-393975
    sprite('nt615_03', 12)	# 393976-393987
    sprite('nt615_04', 6)	# 393988-393993
    SFX_3('ntse_10')
    sprite('nt615_05', 20)	# 393994-394013
    sprite('nt615_06', 8)	# 394014-394021
    sprite('nt615_07', 1)	# 394022-394022
    SFX_1('bnt700pla')
    label(171)
    sprite('nt615_07', 1)	# 394023-394023
    if SLOT_97:
        _gotolabel(171)
    sprite('nt615_07', 60)	# 394024-394083
    sprite('nt615_07', 32767)	# 394084-426850
    Unknown21007(24, 40)
    Unknown21011(150)
    label(180)
    sprite('nt611_00', 4)	# 426851-426854
    sprite('nt611_01', 4)	# 426855-426858
    sprite('nt611_02', 4)	# 426859-426862
    SFX_1('bnt700uca')
    sprite('nt611_03', 4)	# 426863-426866
    Unknown2037(8)
    label(181)
    sprite('nt611_01', 4)	# 426867-426870
    SLOT_2 = (SLOT_2 + (-1))
    sprite('nt611_02', 3)	# 426871-426873
    sprite('nt611_03', 3)	# 426874-426876
    if SLOT_2:
        _gotolabel(181)
    sprite('nt611_04', 4)	# 426877-426880
    GFX_0('ntef_611', -1)
    SFX_3('ntse_11')
    sprite('nt611_05', 4)	# 426881-426884
    sprite('nt611_06', 4)	# 426885-426888
    sprite('nt611_07', 4)	# 426889-426892
    sprite('nt611_08', 4)	# 426893-426896
    label(182)
    sprite('nt611_09', 1)	# 426897-426897
    if SLOT_97:
        _gotolabel(182)
    sprite('nt611_09', 32767)	# 426898-459664
    Unknown21007(24, 40)
    Unknown21011(210)
    label(190)
    sprite('nt000_00', 7)	# 459665-459671

    def upon_40():
        clearUponHandler(40)
        sendToLabel(193)
    SFX_1('bnt700ugo')
    label(191)
    sprite('nt000_01', 7)	# 459672-459678
    sprite('nt000_02', 7)	# 459679-459685
    sprite('nt000_03', 7)	# 459686-459692
    sprite('nt000_04', 7)	# 459693-459699
    sprite('nt000_05', 7)	# 459700-459706
    sprite('nt000_06', 7)	# 459707-459713
    sprite('nt000_07', 7)	# 459714-459720
    sprite('nt000_08', 7)	# 459721-459727
    sprite('nt000_00', 7)	# 459728-459734
    if SLOT_97:
        _gotolabel(191)
    sprite('nt000_01', 7)	# 459735-459741
    Unknown21007(24, 40)
    label(192)
    sprite('nt000_02', 7)	# 459742-459748
    sprite('nt000_03', 7)	# 459749-459755
    sprite('nt000_04', 7)	# 459756-459762
    sprite('nt000_05', 7)	# 459763-459769
    sprite('nt000_06', 7)	# 459770-459776
    sprite('nt000_07', 7)	# 459777-459783
    sprite('nt000_08', 7)	# 459784-459790
    sprite('nt000_00', 7)	# 459791-459797
    sprite('nt000_01', 7)	# 459798-459804
    gotoLabel(192)
    label(193)
    sprite('nt603_00', 6)	# 459805-459810
    sprite('nt603_01', 6)	# 459811-459816
    sprite('nt603_02', 6)	# 459817-459822
    sprite('nt603_03', 6)	# 459823-459828
    sprite('nt603_04', 6)	# 459829-459834
    sprite('nt603_05', 6)	# 459835-459840
    sprite('nt603_06', 6)	# 459841-459846
    sprite('nt603_07', 6)	# 459847-459852
    sprite('nt603_08', 12)	# 459853-459864
    sprite('nt603_07', 6)	# 459865-459870
    sprite('nt603_04ex01', 32767)	# 459871-492637
    SFX_1('bnt702ugo')
    Unknown23018(1)
    label(210)
    sprite('nt000_00', 7)	# 492638-492644

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('nt000_01', 7)	# 492645-492651
    sprite('nt000_02', 7)	# 492652-492658
    sprite('nt000_03', 7)	# 492659-492665
    sprite('nt000_04', 7)	# 492666-492672
    sprite('nt000_05', 7)	# 492673-492679
    sprite('nt000_06', 7)	# 492680-492686
    sprite('nt000_07', 7)	# 492687-492693
    sprite('nt000_08', 7)	# 492694-492700
    sprite('nt000_00', 7)	# 492701-492707
    gotoLabel(211)
    label(212)
    sprite('nt610_00', 6)	# 492708-492713
    sprite('nt610_01', 6)	# 492714-492719
    sprite('nt610_02', 6)	# 492720-492725
    sprite('nt610_03', 6)	# 492726-492731
    sprite('nt610_04', 6)	# 492732-492737
    sprite('nt610_05', 24)	# 492738-492761
    GFX_1('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)	# 492762-492769
    sprite('nt610_07', 8)	# 492770-492777
    sprite('nt610_08', 8)	# 492778-492785
    sprite('nt610_09', 1)	# 492786-492786
    SFX_1('bnt701ryn')
    label(213)
    sprite('nt610_09', 1)	# 492787-492787
    if SLOT_97:
        _gotolabel(213)
    sprite('nt610_09', 32767)	# 492788-525554
    Unknown23018(1)
    label(220)
    sprite('nt000_00', 7)	# 525555-525561

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('nt000_01', 7)	# 525562-525568
    sprite('nt000_02', 7)	# 525569-525575
    sprite('nt000_03', 7)	# 525576-525582
    sprite('nt000_04', 7)	# 525583-525589
    sprite('nt000_05', 7)	# 525590-525596
    sprite('nt000_06', 7)	# 525597-525603
    sprite('nt000_07', 7)	# 525604-525610
    sprite('nt000_08', 7)	# 525611-525617
    sprite('nt000_00', 7)	# 525618-525624
    gotoLabel(221)
    label(222)
    sprite('nt610_00', 6)	# 525625-525630
    sprite('nt610_01', 6)	# 525631-525636
    sprite('nt610_02', 6)	# 525637-525642
    sprite('nt610_03', 6)	# 525643-525648
    sprite('nt610_04', 6)	# 525649-525654
    sprite('nt610_05', 24)	# 525655-525678
    GFX_1('ntef_610_tameiki', 0)
    sprite('nt610_06', 8)	# 525679-525686
    sprite('nt610_07', 8)	# 525687-525694
    sprite('nt610_08', 8)	# 525695-525702
    sprite('nt610_09', 1)	# 525703-525703
    SFX_1('bnt701uak')
    label(223)
    sprite('nt610_09', 1)	# 525704-525704
    if SLOT_97:
        _gotolabel(223)
    sprite('nt610_09', 32767)	# 525705-558471
    Unknown23018(1)
    label(230)
    sprite('keep', 1)	# 558472-558472
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(233)
        elif (SLOT_38 == 1):
            sendToLabel(233)
    label(231)
    sprite('nt603_10', 6)	# 558473-558478
    sprite('nt603_09', 6)	# 558479-558484
    sprite('nt603_08', 12)	# 558485-558496
    sprite('nt603_07', 6)	# 558497-558502
    sprite('nt603_06', 6)	# 558503-558508
    sprite('nt603_05', 6)	# 558509-558514
    sprite('nt603_04ex02', 32767)	# 558515-591281

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(232)
    sprite('nt603_04ex01', 32767)	# 591282-624048
    SFX_1('bnt701pku')
    Unknown23018(1)
    label(233)
    sprite('nt003_00', 4)	# 624049-624052
    Unknown2005()
    sprite('nt003_01', 4)	# 624053-624056
    gotoLabel(231)
    label(240)
    sprite('nt000_00', 7)	# 624057-624063

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    label(241)
    sprite('nt000_01', 7)	# 624064-624070
    sprite('nt000_02', 7)	# 624071-624077
    sprite('nt000_03', 7)	# 624078-624084
    sprite('nt000_04', 7)	# 624085-624091
    sprite('nt000_05', 7)	# 624092-624098
    sprite('nt000_06', 7)	# 624099-624105
    sprite('nt000_07', 7)	# 624106-624112
    sprite('nt000_08', 7)	# 624113-624119
    sprite('nt000_00', 7)	# 624120-624126
    gotoLabel(241)
    label(242)
    sprite('nt603_00', 6)	# 624127-624132
    sprite('nt603_01', 6)	# 624133-624138
    sprite('nt603_02', 6)	# 624139-624144
    sprite('nt603_03', 6)	# 624145-624150
    sprite('nt603_04', 6)	# 624151-624156
    sprite('nt603_05', 6)	# 624157-624162
    sprite('nt603_06', 6)	# 624163-624168
    sprite('nt603_07', 6)	# 624169-624174
    sprite('nt603_08', 12)	# 624175-624186
    sprite('nt603_07', 6)	# 624187-624192
    sprite('nt603_04ex02', 1)	# 624193-624193
    SFX_1('bnt701kym')
    label(243)
    sprite('nt603_04ex02', 1)	# 624194-624194
    if SLOT_97:
        _gotolabel(243)
    sprite('nt603_04ex02', 15)	# 624195-624209
    sprite('nt603_04ex02', 32767)	# 624210-656976
    Unknown21011(30)
    label(250)
    sprite('nt615_00', 6)	# 656977-656982
    sprite('nt615_01', 6)	# 656983-656988
    sprite('nt615_02', 6)	# 656989-656994
    sprite('nt615_03', 12)	# 656995-657006
    sprite('nt615_04', 6)	# 657007-657012
    SFX_3('ntse_10')
    sprite('nt615_05', 20)	# 657013-657032
    sprite('nt615_06', 8)	# 657033-657040
    sprite('nt615_07', 1)	# 657041-657041
    SFX_1('bnt700brc')
    label(251)
    sprite('nt615_07', 1)	# 657042-657042
    if SLOT_97:
        _gotolabel(251)
    sprite('nt615_07', 30)	# 657043-657072
    sprite('nt615_07', 32767)	# 657073-689839
    Unknown21007(24, 40)
    Unknown21011(180)

@State
def CmnActLose():
    sprite('nt620_00', 8)	# 1-8
    sprite('nt620_01', 8)	# 9-16
    sprite('nt620_02', 8)	# 17-24
    Unknown8000(100, 1, 1)
    sprite('nt620_03', 8)	# 25-32
    sprite('nt620_04', 8)	# 33-40
    sprite('nt620_05', 8)	# 41-48
    sprite('nt620_06', 8)	# 49-56
    sprite('nt620_07', 8)	# 57-64
    sprite('nt620_08', 8)	# 65-72
    sprite('nt620_09', 8)	# 73-80
    sprite('nt620_10', 32767)	# 81-32847
    Unknown7006('bnt403_0', 100, 880045666, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    GFX_1('ntef_620_tameiki', 0)