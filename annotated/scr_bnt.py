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
    Unknown15013(1)
    Unknown15006(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown15006(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
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
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(4000)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(-50000, 250000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14004(1)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(4000)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('AN_CmnActInvincibleAttackAir_ca', 0x65)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(4000)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(-50000, 200000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14004(1)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(4000)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(-50000, 200000, -200000, 200000, 250, 0)
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
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
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
    if SLOT_0:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
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
        Unknown22008(7)
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
    Unknown23119(16639, 20, 1)
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
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
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
    Unknown23119(16639, 20, 1)
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
    sprite('nt333_15', 6)	# 1-6
    sprite('nt333_16', 6)	# 7-12
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
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    GFX_1('ntef_333_kyushu', 0)
    GFX_0('ntef_D_handaura_3D', 0)
    sprite('nt333_03', 32767)	# 10-32776
    GFX_0('EMB_NT_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('nt333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
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
    Unknown23119(16639, 20, 1)
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
    sprite('nt333_15', 6)	# 1-6
    sprite('nt333_16', 6)	# 7-12
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
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
    sprite('null', 32767)	# 1-32767

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
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

        def upon_3():
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
    if SLOT_0:
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
    sprite('null', 23)	# 1-23
    sprite('nt253_04', 2)	# 24-25
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    Unknown1007(30000)
    physicsXImpulse(150000)
    physicsYImpulse(-100000)
    sprite('nt253_05', 4)	# 26-29
    GFX_1('ntef_D_aura', 0)
    SFX_3('ntse_04')
    sprite('nt253_06', 4)	# 30-33
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    sprite('nt253_07', 2)	# 34-35
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown2053(1)
    Unknown2017(1)
    sendToLabelUpon(2, 9)
    sprite('nt253_08', 3)	# 36-38	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    GFX_1('ntef_D_aura', 6)
    GFX_1('ntef_D_aura', 7)
    sprite('nt253_09', 2)	# 39-40	 **attackbox here**
    Unknown1043()
    sprite('nt253_11', 3)	# 41-43
    sprite('nt253_12', 4)	# 44-47
    sprite('nt253_13', 4)	# 48-51
    label(1)
    sprite('nt253_14', 4)	# 52-55
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('nt024_00', 4)	# 56-59
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('nt024_01', 2)	# 60-61
    sprite('nt024_02', 2)	# 62-63
    sprite('nt024_03', 4)	# 64-67
    sprite('nt024_04', 3)	# 68-70

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
        Unknown9154(21)
        AirUntechableTime(21)
        Unknown2004(1, 0)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
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
    Unknown23027()
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
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(12)
    AirPushbackX(42000)
    AirPushbackY(15000)
    Unknown9130(35)
    Unknown9142(25)
    AirUntechableTime(40)
    Hitstop(20)
    Unknown11028(23)

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
    sprite('nt213_03', 2)	# 10-11
    Unknown14072('ShortDash')
    sprite('nt213_03', 1)	# 12-12
    loopRest()
    sprite('nt213_01ex01', 3)	# 13-15
    sprite('nt213_02ex01', 3)	# 16-18
    ScreenShake(3000, 9000)
    Unknown8000(-1, 1, 0)
    sprite('nt213_03ex01', 3)	# 19-21
    sprite('nt213_01ex01', 3)	# 22-24
    sprite('nt213_02ex01', 3)	# 25-27
    sprite('nt213_03ex01', 3)	# 28-30
    sprite('nt213_01ex01', 3)	# 31-33
    sprite('nt213_02ex01', 3)	# 34-36
    loopRest()
    label(0)
    sprite('nt213_04ex01', 1)	# 37-37
    clearUponHandler(24)
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    sprite('nt213_05ex01', 1)	# 38-38
    sprite('nt213_06ex01', 2)	# 39-40
    SFX_3('ntse_04')
    SFX_1('bnt300')
    sprite('nt213_07ex01', 3)	# 41-43	 **attackbox here**
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
    Hitstop(20)
    Unknown11028(23)

    def upon_11():
        ScreenShake(3000, 3000)
    sprite('nt213_08ex01', 3)	# 44-46	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt213_09ex01', 3)	# 47-49
    Recovery()
    Unknown2063()
    sprite('nt213_10ex01', 3)	# 50-52
    loopRest()
    gotoLabel(9)
    label(1)
    sprite('nt213_04', 1)	# 53-53
    Unknown21015('6e7465665f445f68616e64617572615f33440000000000000000000000000000e903000000000000')
    Unknown21015('6e7465665f445f68616e64617572610000000000000000000000000000000000ea03000000000000')
    Unknown21015('6e7465665f445f626f6479617572610000000000000000000000000000000000eb03000000000000')
    sprite('nt213_05', 1)	# 54-54
    sprite('nt213_06', 1)	# 55-55
    Unknown7007('626e743131305f30000000000000000064000000626e743131305f31000000000000000064000000626e743131305f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ntse_05')
    sprite('nt213_07', 3)	# 56-58	 **attackbox here**
    Unknown14073('ShortDash')
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    GFX_1('ntef_D_aura', 3)
    GFX_1('ntef_D_aura', 4)
    GFX_1('ntef_D_aura', 5)
    sprite('nt213_08', 3)	# 59-61	 **attackbox here**
    GFX_1('ntef_D_aura', 0)
    GFX_1('ntef_D_aura', 1)
    GFX_1('ntef_D_aura', 2)
    sprite('nt213_09', 3)	# 62-64	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('nt213_10', 3)	# 65-67
    label(9)
    sprite('nt213_11', 3)	# 68-70
    sprite('nt213_12', 4)	# 71-74
    sprite('nt213_13', 4)	# 75-78

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
    if SLOT_0:
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
    Unknown9190(1)
    Unknown9118(35)
    Unknown11028(23)

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
    sprite('nt210_00', 3)	# 1-3
    sprite('nt210_01', 3)	# 4-6
    tag_voice(1, 'bnt156_0', 'bnt156_1', '', '')
    sprite('nt210_02', 3)	# 7-9
    sprite('nt210_03', 3)	# 10-12
    Unknown8007(100, 1, 1)
    physicsXImpulse(18000)
    sprite('nt210_04', 3)	# 13-15
    sprite('nt210_05', 3)	# 16-18
    SFX_0('004_swing_grap_1_1')
    sprite('nt210_06', 3)	# 19-21
    Unknown8000(100, 1, 1)
    Unknown1019(30)
    sprite('nt210_07', 3)	# 22-24	 **attackbox here**
    sprite('nt210_08', 4)	# 25-28
    Unknown1084(1)
    sprite('nt210_09', 4)	# 29-32
    sprite('nt210_10', 4)	# 33-36
    sprite('nt210_11', 4)	# 37-40
    sprite('nt210_12', 4)	# 41-44
    sprite('nt210_13', 4)	# 45-48

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
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
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
    Unknown2017(1)
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
        Unknown9154(25)
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
    Unknown2017(0)
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
    Unknown2017(1)
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
        physicsXImpulse(40000)
        AirPushbackX(15000)
        sendToLabelUpon(2, 9)
        SLOT_59 = 1
        callSubroutine('Dash_AfterImage')

        def upon_78():
            clearUponHandler(78)
            Unknown14070('AntiAir2nd')
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
    Damage(500)
    Hitstop(3)
    Unknown1019(300)
    YAccel(80)
    RefreshMultihit()
    sprite('nt405_06ex', 3)	# 16-18	 **attackbox here**
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
        AirUntechableTime(40)
        AttackP1(48)
        AttackP2(100)
        AirPushbackY(-40000)
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
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    sprite('nt400_10', 3)	# 29-31
    Unknown14077(0)

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
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    sprite('nt400_10', 3)	# 29-31
    Unknown14077(0)

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
    sprite('nt401_05', 4)	# 32785-32788
    sprite('nt401_06', 5)	# 32789-32793
    sprite('nt401_07', 4)	# 32794-32797
    WhiffCancelEnable(0)
    Unknown14077(0)

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
    sprite('nt400_08', 3)	# 29-31
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 32-34
    sprite('nt400_10', 3)	# 35-37
    WhiffCancelEnable(0)
    Unknown14077(0)

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
    sprite('nt400_08', 3)	# 29-31
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 32-34
    sprite('nt400_10', 3)	# 35-37
    WhiffCancelEnable(0)
    Unknown14077(0)

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
    sprite('nt401_05', 4)	# 32785-32788
    sprite('nt401_06', 5)	# 32789-32793
    sprite('nt401_07', 4)	# 32794-32797
    WhiffCancelEnable(0)
    Unknown14077(0)

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
        Unknown11091(10)
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
    Unknown2058(-5000)
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
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    sprite('nt400_10', 3)	# 29-31
    WhiffCancelEnable(0)
    Unknown14077(0)

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
        Unknown11091(10)
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
    Unknown2058(-5000)
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
    sprite('nt400_08', 3)	# 23-25
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('nt400_09', 3)	# 26-28
    sprite('nt400_10', 3)	# 29-31
    WhiffCancelEnable(0)
    Unknown14077(0)

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
        Unknown11091(10)
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
    sprite('nt401_05', 4)	# 32785-32788
    sprite('nt401_06', 5)	# 32789-32793
    sprite('nt401_07', 4)	# 32794-32797
    WhiffCancelEnable(0)
    Unknown14077(0)

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
        Unknown11091(10)
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
        Unknown11091(10)
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
        Unknown11028(17)
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
    Unknown2017(1)
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
        Unknown11028(21)
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
    Unknown2017(1)
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
        Unknown11028(21)
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
        Unknown11091(10)
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
Unknown2058(-5000)
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
Unknown2017(1)
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
        Unknown11028(21)
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
        Unknown11091(10)
        Unknown30065(0)
        Unknown11001(0, 3, 8)
        callSubroutine('Dash_AfterImage')
    sprite('nt404_00', 4)	# 1-4
    physicsXImpulse(4000)
    GFX_1('ntef_D_aura', 0)
    Unknown8010(100, 1, 0)
    sprite('nt404_01', 4)	# 5-8
    Unknown23125('')
    Unknown2058(-5000)
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
    Unknown2017(1)
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

        def upon_3():
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
    Unknown2017(0)
    sprite('nt407_02', 8)	# 31-38
    setInvincible(0)
    Unknown2018(1, 60)
    Unknown2017(1)
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

        def upon_3():
            if (SLOT_41 <= 150000):
                if SLOT_38:
                    if (SLOT_40 >= 0):
                        clearUponHandler(3)
                        Unknown1019(40)
                elif (SLOT_40 <= 0):
                    clearUponHandler(3)
                    Unknown1019(40)
    sprite('nt408_00', 1)	# 1-1
    Unknown2017(0)
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
    Unknown2017(1)
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
        Unknown11091(5)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(9000)
        AirUntechableTime(60)
        Unknown11066(1)
        Unknown11084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
        Unknown23022(1)
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
        Unknown11091(35)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(55000)
        AirUntechableTime(80)
        Unknown11056(0)
        setInvincible(1)
        Unknown1084(1)

        def upon_78():
            Unknown22019('0100000001000000010000000100000001000000')
            Unknown2017(0)
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
    Unknown2058(-10000)
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
    Unknown23027()
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
    Unknown2017(1)
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
        Unknown11091(31)
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
            Unknown2017(0)
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
    Unknown2058(-10000)
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
    Unknown23027()
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
    Unknown2017(1)
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
        Unknown11091(20)
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
            Unknown2017(0)
            SLOT_53 = 1
            Unknown13024(0)
            Unknown11069('UltimateAssaultOD_2nd')
            Hitstop(20)
            Unknown11064(1)

        def upon_77():
            sendToLabel(1)
            Hitstop(20)

        def upon_3():
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
    Unknown2058(-10000)
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
    Unknown23027()
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
    Unknown2017(1)
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
        Unknown11091(20)
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
            Unknown2017(0)
            SLOT_53 = 1
            Unknown13024(0)
            Unknown11069('UltimateAssaultOD_2nd')
            Hitstop(20)
            Unknown11064(1)

        def upon_77():
            Hitstop(20)
            sendToLabel(1)

        def upon_3():
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
    Unknown2058(-10000)
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
    Unknown23027()
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
    Unknown2017(1)
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
        Unknown11091(30)
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
        Unknown11091(32)
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
            Unknown2017(0)
        Unknown23159('UltimateAirAssault_TC')
    sprite('nt430_22', 2)	# 1-2
    sprite('nt430_23', 2)	# 3-4
    sprite('nt430_24', 3)	# 5-7
    tag_voice(1, 'bnt252_0', 'bnt252_1', '', '')
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
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
        Unknown11091(35)
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
            Unknown2017(0)
        Unknown23159('UltimateAirAssault_TC')
    sprite('nt430_22', 2)	# 1-2
    sprite('nt430_23', 2)	# 3-4
    sprite('nt430_24', 3)	# 5-7
    tag_voice(1, 'bnt252_0', 'bnt252_1', '', '')
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
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
        Unknown11091(20)
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
            Unknown23027()
            Unknown22019('0100000001000000010000000100000001000000')
            Unknown2017(0)
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
    Unknown2058(-10000)
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
    Unknown2017(1)
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
        Unknown11091(20)
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
            Unknown23027()
            Unknown22019('0100000001000000010000000100000001000000')
            Unknown2017(0)
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
    Unknown2058(-10000)
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
    Unknown2017(1)
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
        Unknown11091(25)
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
            Unknown13024(0)
        Unknown23159('UltimateEdgeAssault_TC')
    sprite('nt431_00', 3)	# 1-3
    sprite('nt431_01', 3)	# 4-6
    tag_voice(1, 'bnt255_0', 'bnt255_1', '', '')
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
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
    Unknown23027()
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
        Unknown11091(25)
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
            Unknown13024(0)
        Unknown23159('UltimateEdgeAssault_TC')
    sprite('nt431_00', 3)	# 1-3
    sprite('nt431_01', 3)	# 4-6
    tag_voice(1, 'bnt255_0', 'bnt255_1', '', '')
    Unknown2036(40, -1, 0)
    Unknown2058(-10000)
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
    Unknown23027()
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
        Unknown11091(18)
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
        Unknown2017(0)

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
    Unknown2017(1)
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
        Unknown11091(10)
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
    Unknown2058(-10000)
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
    Unknown23027()
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
        Unknown11091(10)
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
    Unknown2058(-10000)
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
    Unknown23027()
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
        Unknown11091(18)
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
        if SLOT_59:
            callSubroutine('Dash_AfterImage')
        else:
            Unknown3029(1)
            Unknown3069(1)
            Unknown3070(3)
            Unknown3071(5)
        Unknown23022(1)
        Unknown2017(0)
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
        Unknown9154(20)
        Unknown9016(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(220)
        Unknown9142(200)
        Unknown9154(200)
        Unknown11057(1500)
        Unknown11084(1)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11091(100)

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
    Unknown9154(300)
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
    Unknown9154(300)
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
            Unknown2017(1)
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
        AirPushbackX(8000)
        AirPushbackY(38000)
        AirUntechableTime(60)
        PushbackX(12000)
        Hitstop(16)
        Unknown9016(1)
        Unknown11042(1)

        def upon_STATE_END():
            Unknown2017(1)
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
    sprite('nt213_05ex01', 1)	# 8-8
    sprite('nt213_06ex01', 1)	# 9-9
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
    sprite('nt213_09ex01', 5)	# 16-20
    Recovery()
    sprite('nt213_10ex01', 5)	# 21-25
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
            Unknown2017(1)
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
    Unknown2017(1)
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
    Unknown2017(1)
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
        Unknown11091(100)
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
            Unknown2017(1)
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
    Unknown23027()
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
        Unknown11091(100)
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
            Unknown2017(1)
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
    Unknown23027()
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
    Unknown18011('bnt521', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt540', 12643, 12336, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt541', 12643, 12336, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt542', 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 24885, 25397, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt543', 13923, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt544', 13665, 13667, 13665, 13667, 13665, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt545', 12643, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt402_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt402_1', 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt403_0', 14177, 14691, 12641, 25394, 12338, 14689, 14435, 14433, 14435, 14177, 13923, 14689, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bnt403_1', 14689, 14179, 14177, 13667, 13665, 13667, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13665, 13667, 12641, 25394, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    Unknown19(991, 2, 158)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(3)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(1)
    random_(2, 0, 25)
    if SLOT_0:
        _gotolabel(2)
    label(0)
    sprite('nt000_00', 7)	# 2-8
    sprite('nt000_01', 7)	# 9-15
    sprite('nt000_02', 7)	# 16-22
    sprite('nt000_03', 7)	# 23-29
    sprite('nt000_04', 7)	# 30-36
    sprite('nt000_05', 7)	# 37-43
    sprite('nt000_06', 7)	# 44-50
    sprite('nt000_07', 7)	# 51-57
    sprite('nt000_08', 7)	# 58-64
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    sprite('nt600_00', 6)	# 65-70
    sprite('nt600_01', 7)	# 71-77
    sprite('nt600_02', 7)	# 78-84
    sprite('nt600_03', 7)	# 85-91
    sprite('nt600_04', 7)	# 92-98
    sprite('nt600_03', 7)	# 99-105
    sprite('nt600_02', 7)	# 106-112
    sprite('nt600_01', 7)	# 113-119
    sprite('nt600_02', 7)	# 120-126
    sprite('nt600_03', 7)	# 127-133
    sprite('nt600_04', 14)	# 134-147
    SFX_1('bnt520')
    sprite('nt600_03', 7)	# 148-154
    sprite('nt600_02', 7)	# 155-161
    sprite('nt600_01', 7)	# 162-168
    sprite('nt600_05', 7)	# 169-175
    sprite('nt600_06', 7)	# 176-182
    sprite('nt600_07', 7)	# 183-189
    sprite('nt600_06', 7)	# 190-196
    sprite('nt600_05', 7)	# 197-203
    sprite('nt600_06', 7)	# 204-210
    sprite('nt600_07', 14)	# 211-224
    sprite('nt600_06', 7)	# 225-231
    sprite('nt600_05', 7)	# 232-238
    sprite('nt600_01', 6)	# 239-244
    sprite('nt600_00', 8)	# 245-252
    sprite('nt600_08', 8)	# 253-260
    sprite('nt600_09', 8)	# 261-268
    sprite('nt600_10', 8)	# 269-276
    sprite('nt600_11', 8)	# 277-284
    sprite('nt600_12', 8)	# 285-292
    Unknown23018(1)
    loopRest()
    ExitState()
    label(1)
    sprite('nt000_00', 7)	# 293-299
    sprite('nt000_01', 7)	# 300-306
    sprite('nt000_02', 7)	# 307-313
    sprite('nt000_03', 7)	# 314-320
    sprite('nt000_04', 7)	# 321-327
    sprite('nt000_05', 7)	# 328-334
    sprite('nt000_06', 7)	# 335-341
    sprite('nt000_07', 7)	# 342-348
    sprite('nt000_08', 7)	# 349-355
    loopRest()
    if SLOT_17:
        _gotolabel(1)
    sprite('nt600_00', 6)	# 356-361
    sprite('nt600_01', 6)	# 362-367
    SFX_1('bnt521')
    sprite('nt600_13', 6)	# 368-373
    sprite('nt600_14', 6)	# 374-379
    sprite('nt600_15', 20)	# 380-399
    sprite('nt600_01', 6)	# 400-405
    sprite('nt600_16', 6)	# 406-411
    sprite('nt600_17', 6)	# 412-417
    sprite('nt600_18', 20)	# 418-437
    sprite('nt600_01', 6)	# 438-443
    sprite('nt600_00', 8)	# 444-451
    sprite('nt600_08', 8)	# 452-459
    sprite('nt600_09', 8)	# 460-467
    sprite('nt600_10', 8)	# 468-475
    sprite('nt600_11', 8)	# 476-483
    sprite('nt600_12', 8)	# 484-491
    Unknown23018(1)
    loopRest()
    ExitState()
    label(2)
    sprite('nt000_00', 7)	# 492-498
    sprite('nt000_01', 7)	# 499-505
    sprite('nt000_02', 7)	# 506-512
    sprite('nt000_03', 7)	# 513-519
    sprite('nt000_04', 7)	# 520-526
    sprite('nt000_05', 7)	# 527-533
    sprite('nt000_06', 7)	# 534-540
    sprite('nt000_07', 7)	# 541-547
    sprite('nt000_08', 7)	# 548-554
    loopRest()
    if SLOT_17:
        _gotolabel(2)
    sprite('nt300_00', 7)	# 555-561
    sprite('nt300_01', 7)	# 562-568
    sprite('nt300_02', 7)	# 569-575
    sprite('nt300_03', 7)	# 576-582
    sprite('nt300_04', 8)	# 583-590
    SFX_1('bnt521')
    sprite('nt300_03', 7)	# 591-597
    sprite('nt300_02', 7)	# 598-604
    sprite('nt300_03', 7)	# 605-611
    sprite('nt300_04', 8)	# 612-619
    sprite('nt300_03', 7)	# 620-626
    sprite('nt300_02', 7)	# 627-633
    sprite('nt300_05', 7)	# 634-640
    sprite('nt300_06', 7)	# 641-647
    sprite('nt300_07', 6)	# 648-653
    sprite('nt300_08', 6)	# 654-659
    sprite('nt300_09', 7)	# 660-666
    sprite('nt300_08', 6)	# 667-672
    sprite('nt300_07', 6)	# 673-678
    sprite('nt300_08', 6)	# 679-684
    sprite('nt300_09', 7)	# 685-691
    sprite('nt300_08', 6)	# 692-697
    sprite('nt300_07', 6)	# 698-703
    sprite('nt300_10', 7)	# 704-710
    sprite('nt300_11', 6)	# 711-716
    sprite('nt300_12', 6)	# 717-722
    Unknown23018(1)
    loopRest()
    ExitState()
    label(3)
    sprite('nt601_00', 8)	# 723-730
    loopRest()
    if SLOT_17:
        _gotolabel(3)
    sprite('nt601_01', 8)	# 731-738
    sprite('nt601_02', 8)	# 739-746
    sprite('nt601_01', 8)	# 747-754
    sprite('nt601_00', 8)	# 755-762
    sprite('nt601_01', 8)	# 763-770
    sprite('nt601_02', 14)	# 771-784
    sprite('nt601_03', 7)	# 785-791
    sprite('nt601_04', 7)	# 792-798
    sprite('nt601_05', 80)	# 799-878
    Unknown7006('bnt522', 100, 896822882, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('nt601_05', 70)	# 879-948
    sprite('nt601_06', 9)	# 949-957
    sprite('nt601_07', 9)	# 958-966
    sprite('nt601_08', 9)	# 967-975
    SFX_0('019_cloth_a')
    sprite('nt601_09', 5)	# 976-980
    Unknown23018(1)
    loopRest()
    ExitState()
    label(991)
    sprite('nt000_00', 1)	# 981-981
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('nt000_00', 7)	# 982-988
    sprite('nt000_01', 7)	# 989-995
    sprite('nt000_02', 7)	# 996-1002
    sprite('nt000_03', 7)	# 1003-1009
    sprite('nt000_04', 7)	# 1010-1016
    sprite('nt000_05', 7)	# 1017-1023
    sprite('nt000_06', 7)	# 1024-1030
    sprite('nt000_07', 7)	# 1031-1037
    sprite('nt000_08', 7)	# 1038-1044
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

    def upon_3():
        SLOT_58 = 1
        Unknown48('19000000020000003400000018000000020000003a000000')
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if SLOT_64:
        _gotolabel(2)
    if (not SLOT_108):
        random_(2, 0, 50)
        if SLOT_0:
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