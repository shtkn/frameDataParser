@Subroutine
def PreInit():
    Unknown12019('72726200000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFAccel(1000)
    DashFMaxVelocity(32000)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Unknown15018(2000)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 350000, -200000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown14013('NmlAtk5A')
    Unknown14015(0, 350000, -200000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 550000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    Unknown14005(1)
    Unknown14015(0, 800000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown14015(0, 450000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 550000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 550000, -200000, 500000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 300000, -100000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15021(2000)
    Unknown14015(0, 400000, 150000, 450000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(0, 450000, -100000, 100000, 500, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-100000, 400000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2nd', 0x10)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5B')
    Unknown14015(-100000, 350000, -400000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2A', 0xd)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(-100000, 350000, -400000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_2nd', 0x22)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5A')
    Unknown14015(-100000, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-100000, 350000, -200000, 150000, 1000, 50)
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
    Move_Register('SpDash_Back', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    MoveMaxChainRepeat(3)
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('SpDash_Front', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14027('SpDash_Back')
    Unknown15013(1)
    Unknown14015(0, 0, 0, 0, 500, 100)
    Move_EndRegister()
    Move_Register('SpDash_AntiAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14027('SpDash_Back')
    Unknown14015(0, 0, 0, 0, 500, 100)
    Unknown15013(1)
    Move_EndRegister()
    Move_Register('AirSpDash_Back', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14027('SpDash_Back')
    Move_AirGround_(0x3000)
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('AirSpDash_Front', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14027('SpDash_Back')
    Move_AirGround_(0x3000)
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('AirSpDash_AntiLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14027('SpDash_Back')
    Move_AirGround_(0x3000)
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('Hasei_SpDash_Back', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14027('SpDash_Back')
    Unknown14013('SpDash_Back')
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 200, 60)
    Move_EndRegister()
    Move_Register('Hasei_SpDash_Front', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14027('SpDash_Back')
    Unknown14013('SpDash_Front')
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 100, 10)
    Move_EndRegister()
    Move_Register('Hasei_SpDash_AntiAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14027('SpDash_Back')
    Unknown14013('SpDash_AntiAir')
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 100, 10)
    Move_EndRegister()
    Move_Register('Hasei_AirSpDash_Back', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Unknown14005(1)
    Unknown14027('SpDash_Back')
    Unknown14013('AirSpDash_Back')
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 200, 60)
    Move_EndRegister()
    Move_Register('Hasei_AirSpDash_Front', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Unknown14027('SpDash_Back')
    Unknown14013('AirSpDash_Front')
    Unknown15013(1)
    Unknown14015(0, 450000, -200000, 200000, 100, 10)
    Move_EndRegister()
    Move_Register('Hasei_AirSpDash_AntiLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_C)
    Unknown14005(1)
    Unknown14027('SpDash_Back')
    Unknown14013('AirSpDash_AntiLand')
    Unknown14015(0, 450000, -200000, 200000, 100, 10)
    Unknown15013(1)
    Move_EndRegister()
    Move_Register('AttackAndShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown14015(800000, 2000000, -100000, 200000, 150, 0)
    Move_EndRegister()
    Move_Register('AttackAndShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(0, 450000, -200000, 300000, 300, 20)
    Move_EndRegister()
    Move_Register('AttackAndShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('MultiAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(0, 450000, -200000, 250000, 200, 1)
    Move_EndRegister()
    Move_Register('AirRolling_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-100000, 400000, -100000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('AirRolling_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-100000, 400000, -100000, 200000, 500, 50)
    Move_EndRegister()
    Move_Register('AirRolling_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(-100000, 350000, -400000, 150000, 100, 20)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(1)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-150000, 150000, -100000, 300000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(6000)
    Unknown14015(150000, 750000, -200000, 150000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateDance', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(6000)
    Unknown14015(50000, 300000, -200000, 300000, 150, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown15013(1)
    Unknown14015(150000, 750000, -200000, 150000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateDanceOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown14015(50000, 300000, -200000, 300000, 150, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A_2nd', 10000000)
    Unknown15024('NmlAtkAIR5A_2nd', 'AirRolling_A', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('SpDash_Back', 'Hasei_SpDash_Front', 10000000)
    Unknown15024('SpDash_Back', 'Hasei_SpDash_AntiAir', 10000000)
    Unknown15024('SpDash_Front', 'Hasei_SpDash_Back', 10000000)
    Unknown15024('SpDash_Front', 'Hasei_SpDash_AntiAir', 10000000)
    Unknown15024('SpDash_AntiAir', 'Hasei_AirSpDash_Back', 10000000)
    Unknown15024('SpDash_AntiAir', 'Hasei_AirSpDash_Front', 10000000)
    Unknown15024('SpDash_AntiAir', 'Hasei_AirSpDash_AntiLand', 10000000)
    Unknown15024('AirSpDash_Back', 'Hasei_AirSpDash_Front', 10000000)
    Unknown15024('AirSpDash_Back', 'Hasei_AirSpDash_AntiLand', 10000000)
    Unknown15024('AirSpDash_Front', 'Hasei_AirSpDash_Back', 10000000)
    Unknown15024('AirSpDash_Front', 'Hasei_AirSpDash_AntiLand', 10000000)
    Unknown15024('Hasei_SpDash_Front', 'Hasei_SpDash_Back', 10000000)
    Unknown15024('Hasei_SpDash_Front', 'Hasei_SpDash_AntiAir', 10000000)
    Unknown15024('Hasei_SpDash_Back', 'Hasei_SpDash_Front', 10000000)
    Unknown15024('Hasei_SpDash_Back', 'Hasei_SpDash_AntiAir', 10000000)
    Unknown15024('Hasei_SpDash_AntiAir', 'Hasei_AirSpDash_Back', 10000000)
    Unknown15024('Hasei_SpDash_AntiAir', 'Hasei_AirSpDash_Front', 10000000)
    Unknown15024('Hasei_SpDash_AntiAir', 'Hasei_AirSpDash_AntiLand', 10000000)
    Unknown15024('Hasei_AirSpDash_AntiLand', 'Hasei_SpDash_Front', 10000000)
    Unknown15024('Hasei_AirSpDash_AntiLand', 'Hasei_SpDash_Back', 10000000)
    Unknown15024('Hasei_AirSpDash_AntiLand', 'Hasei_SpDash_AntiAir', 10000000)
    Unknown14048('BackAssault', 0x4, 0xed)
    Unknown14048('GedanShot', 0x4, 0x79)
    Unknown14048('UltimateLargeSwordLand', 0x4, 0x5f)
    Unknown14048('UltimateLargeSwordLandOD', 0x4, 0x5f)
    Unknown14048('TimelagShot', 0x4, 0x45)
    Unknown14048('BackAssault_Air', 0x4, 0xed)
    Unknown14048('UltimateLargeSwordAir', 0x4, 0x5f)
    Unknown14048('UltimateLargeSwordAirOD', 0x4, 0x5f)
    Unknown14048('ChudanShot', 0x4, 0x45)
    Unknown12018(0, 'rrb062_01')
    Unknown12018(1, 'rrb062_02')
    Unknown12018(2, 'rrb062_03')
    Unknown12018(3, 'rrb062_04')
    Unknown12018(4, 'rrb062_05')
    Unknown12018(5, 'rrb062_06')
    Unknown12018(6, 'rrb062_07')
    Unknown12018(7, 'rrb040_00')
    Unknown12018(8, 'rrb040_00')
    Unknown12018(9, 'rrb045_00')
    Unknown12018(10, 'rrb062_01')
    Unknown12018(11, 'rrb062_02')
    Unknown12018(12, 'rrb062_05')
    Unknown12018(13, 'rrb062_06')
    Unknown12018(14, 'rrb062_09')
    Unknown12018(15, 'rrb073_01ex')
    Unknown12018(16, 'rrb050_00')
    Unknown12018(17, 'rrb052_00')
    Unknown12018(18, 'rrb054_00')
    Unknown12018(19, 'rrb072_01')
    Unknown12018(20, 'rrb062_08')
    Unknown12018(25, 'rrb063_00')
    Unknown12018(26, 'rrb063_01')
    Unknown12018(27, 'rrb063_02')
    Unknown12018(28, 'rrb063_05')
    Unknown12018(29, 'rrb063_09')
    Unknown12018(24, 'rrb073_01')
    Unknown7010(0, 'rrb000')
    Unknown7010(1, 'rrb001')
    Unknown7010(2, 'rrb002')
    Unknown7010(3, 'rrb003')
    Unknown7010(4, 'rrb004')
    Unknown7010(5, 'rrb005')
    Unknown7010(6, 'rrb006')
    Unknown7010(7, 'rrb007')
    Unknown7010(8, 'rrb008')
    Unknown7010(9, 'rrb009')
    Unknown7010(10, 'rrb010')
    Unknown7010(15, 'rrb015')
    Unknown7010(16, 'rrb016')
    Unknown7010(17, 'rrb017')
    Unknown7010(18, 'rrb018')
    Unknown7010(19, 'rrb019')
    Unknown7010(20, 'rrb020')
    Unknown7010(21, 'rrb021')
    Unknown7010(22, 'rrb022')
    Unknown7010(23, 'rrb023')
    Unknown7010(24, 'rrb024')
    Unknown7010(25, 'rrb025')
    Unknown7010(28, 'rrb028')
    Unknown7010(29, 'rrb029')
    Unknown7010(30, 'rrb030')
    Unknown7010(31, 'rrb031')
    Unknown7010(32, 'rrb032')
    Unknown7010(33, 'rrb033')
    Unknown7010(34, 'rrb034')
    Unknown7010(35, 'rrb035')
    Unknown7010(36, 'rrb036')
    Unknown7010(37, 'rrb037')
    Unknown7010(39, 'rrb039')
    Unknown7010(42, 'rrb042')
    Unknown7010(43, 'rrb043')
    Unknown7010(44, 'rrb044')
    Unknown7010(45, 'rrb045')
    Unknown7010(46, 'rrb046')
    Unknown7010(47, 'rrb047')
    Unknown7010(48, 'rrb048')
    Unknown7010(49, 'rrb049')
    Unknown7010(50, 'rrb050')
    Unknown7010(52, 'rrb052')
    Unknown7010(53, 'rrb053')
    Unknown7010(54, 'rrb100_0')
    Unknown7010(55, 'rrb100_1')
    Unknown7010(56, 'rrb100_2')
    Unknown7010(63, 'rrb101_0')
    Unknown7010(64, 'rrb101_1')
    Unknown7010(65, 'rrb101_2')
    Unknown7010(57, 'rrb102_0')
    Unknown7010(58, 'rrb102_1')
    Unknown7010(59, 'rrb102_2')
    Unknown7010(66, 'rrb103_0')
    Unknown7010(67, 'rrb103_1')
    Unknown7010(68, 'rrb103_2')
    Unknown7010(60, 'rrb104_0')
    Unknown7010(61, 'rrb104_1')
    Unknown7010(62, 'rrb104_2')
    Unknown7010(69, 'rrb105_0')
    Unknown7010(70, 'rrb105_1')
    Unknown7010(71, 'rrb105_2')
    Unknown7010(72, 'rrb150')
    Unknown7010(73, 'rrb151')
    Unknown7010(74, 'rrb152')
    Unknown7010(85, 'rrb153')
    Unknown7010(87, 'rrb155')
    Unknown7010(88, 'rrb156_0')
    Unknown7010(96, 'rrb162_0')
    Unknown7010(97, 'rrb162_1')
    Unknown7010(92, 'rrb163_0')
    Unknown7010(93, 'rrb163_1')
    Unknown7010(98, 'rrb164_0')
    Unknown7010(99, 'rrb164_2')
    Unknown7010(100, 'rrb165_0')
    Unknown7010(101, 'rrb165_1')
    Unknown7010(105, 'rrb166_0')
    Unknown7010(106, 'rrb166_1')
    Unknown7010(102, 'rrb167_0')
    Unknown7010(103, 'rrb167_1')
    Unknown7010(90, 'rrb168_0')
    Unknown7010(91, 'rrb168_1')
    Unknown7010(107, 'rrb169_0')
    Unknown7010(108, 'rrb169_1')
    Unknown7010(110, 'rrb170_0')
    Unknown7010(111, 'rrb170_1')
    Unknown7010(112, 'rrb160_0')
    Unknown7010(113, 'rrb160_1')
    Unknown7010(94, 'rrb400_0')
    Unknown7010(95, 'rrb400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746544616e636500000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746544616e63654f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnActionBegin():
    if SLOT_37:
        SLOT_4 = 1

@State
def CmnActStand():
    label(0)
    sprite('rrb000_00', 7)	# 1-7
    sprite('rrb000_01', 7)	# 8-14
    sprite('rrb000_02', 7)	# 15-21
    sprite('rrb000_03', 7)	# 22-28
    sprite('rrb000_04', 7)	# 29-35
    sprite('rrb000_05', 7)	# 36-42
    sprite('rrb000_06', 7)	# 43-49
    sprite('rrb000_07', 7)	# 50-56
    sprite('rrb000_08', 7)	# 57-63
    sprite('rrb000_09', 7)	# 64-70
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('rrb001_00', 5)	# 71-75
    SFX_1('rrb000')
    SLOT_88 = 960
    sprite('rrb001_01', 5)	# 76-80
    sprite('rrb001_02', 8)	# 81-88
    sprite('rrb001_03', 8)	# 89-96
    sprite('rrb001_04', 8)	# 97-104
    sprite('rrb001_05', 8)	# 105-112
    sprite('rrb001_06', 8)	# 113-120
    sprite('rrb001_07', 8)	# 121-128
    sprite('rrb001_08', 8)	# 129-136
    sprite('rrb001_09', 8)	# 137-144
    sprite('rrb001_02', 8)	# 145-152
    sprite('rrb001_03', 8)	# 153-160
    sprite('rrb001_04', 8)	# 161-168
    sprite('rrb001_05', 8)	# 169-176
    sprite('rrb001_06', 8)	# 177-184
    sprite('rrb001_07', 8)	# 185-192
    sprite('rrb001_08', 8)	# 193-200
    sprite('rrb001_09', 8)	# 201-208
    sprite('rrb001_01', 5)	# 209-213
    sprite('rrb001_00', 5)	# 214-218
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('rrb003_01', 5)	# 1-5
    sprite('rrb003_00', 4)	# 6-9

@State
def CmnActStand2Crouch():
    sprite('rrb010_00', 2)	# 1-2
    sprite('rrb010_01', 3)	# 3-5
    sprite('rrb010_02', 3)	# 6-8

@State
def CmnActCrouch():
    label(0)
    sprite('rrb010_03', 7)	# 1-7
    sprite('rrb010_04', 7)	# 8-14
    sprite('rrb010_05', 7)	# 15-21
    sprite('rrb010_06', 7)	# 22-28
    sprite('rrb010_07', 7)	# 29-35
    sprite('rrb010_08', 7)	# 36-42
    sprite('rrb010_09', 7)	# 43-49
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('rrb013_01', 3)	# 1-3
    sprite('rrb013_00', 3)	# 4-6

@State
def CmnActCrouch2Stand():
    sprite('rrb010_02', 3)	# 1-3
    sprite('rrb010_01', 3)	# 4-6
    sprite('rrb010_00', 3)	# 7-9

@State
def CmnActJumpPre():
    sprite('rrb010_00', 2)	# 1-2
    sprite('rrb010_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    sprite('rrb020_00', 4)	# 1-4
    sprite('rrb020_01', 4)	# 5-8

@State
def CmnActJumpUpperEnd():
    sprite('rrb020_02', 3)	# 1-3
    sprite('rrb020_03', 3)	# 4-6
    sprite('rrb020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('rrb020_05', 3)	# 1-3
    sprite('rrb020_06', 3)	# 4-6
    label(0)
    sprite('rrb020_07', 4)	# 7-10
    sprite('rrb020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('rrb010_01', 4)	# 1-4
    sprite('rrb010_02', 4)	# 5-8
    sprite('rrb010_03', 3)	# 9-11
    sprite('rrb010_01', 3)	# 12-14
    sprite('rrb010_00', 1)	# 15-15

@State
def CmnActLandingStiffLoop():
    sprite('rrb010_01', 3)	# 1-3
    sprite('rrb010_02', 32767)	# 4-32770

@State
def CmnActLandingStiffEnd():
    sprite('rrb010_02', 3)	# 1-3
    sprite('rrb010_03', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('rrb032_14', 3)	# 1-3
    sprite('rrb032_00', 4)	# 4-7
    sprite('rrb032_01', 6)	# 8-13
    label(0)
    sprite('rrb032_02', 4)	# 14-17
    sprite('rrb032_03', 4)	# 18-21
    sprite('rrb032_04', 4)	# 22-25
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rrb032_05', 4)	# 26-29
    sprite('rrb032_06', 4)	# 30-33
    sprite('rrb032_07', 4)	# 34-37
    sprite('rrb032_08', 4)	# 38-41
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rrb032_09', 4)	# 42-45
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('rrb031_00', 7)	# 1-7
    sprite('rrb031_01', 7)	# 8-14
    label(0)
    sprite('rrb031_02', 7)	# 15-21
    sprite('rrb031_03', 7)	# 22-28
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rrb031_04', 7)	# 29-35
    sprite('rrb031_05', 7)	# 36-42
    sprite('rrb031_06', 7)	# 43-49
    sprite('rrb031_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rrb031_08', 7)	# 57-63
    sprite('rrb031_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('rrb032_14', 3)	# 1-3
    sprite('rrb032_00', 4)	# 4-7
    sprite('rrb032_01', 6)	# 8-13
    label(0)
    sprite('rrb032_02', 4)	# 14-17
    sprite('rrb032_03', 4)	# 18-21
    sprite('rrb032_04', 4)	# 22-25
    Unknown8006(100, 1, 1)
    sprite('rrb032_05', 4)	# 26-29
    sprite('rrb032_06', 4)	# 30-33
    sprite('rrb032_07', 4)	# 34-37
    sprite('rrb032_08', 4)	# 38-41
    Unknown8006(100, 1, 1)
    sprite('rrb032_09', 4)	# 42-45
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('rrb032_10', 2)	# 1-2
    sprite('rrb032_11', 3)	# 3-5
    sprite('rrb032_12', 3)	# 6-8
    sprite('rrb032_13', 5)	# 9-13
    sprite('rrb032_14', 3)	# 14-16

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
    sprite('rrb033_00', 1)	# 1-1
    sprite('rrb033_01', 2)	# 2-3
    SFX_3('rgse_00')
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rrb033_02', 2)	# 4-5
    sprite('rrb033_02', 1)	# 6-6
    sprite('rrb033_01', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rrb033_02', 3)	# 10-12
    sprite('rrb033_01', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb033_03', 3)	# 16-18
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('rrb033_04', 3)	# 19-21

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        pass
    sprite('rrb035_00', 3)	# 1-3
    label(0)
    sprite('rrb035_01', 3)	# 4-6
    sprite('rrb035_02', 3)	# 7-9
    sprite('rrb035_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('rrb033_00', 3)	# 1-3
    loopRest()
    label(0)
    sprite('rrb033_01', 3)	# 4-6
    sprite('rrb033_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('rrb050_00', 1)	# 1-1
    sprite('rrb050_01', 1)	# 2-2
    sprite('rrb050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('rrb050_00', 1)	# 1-1
    sprite('rrb050_02', 1)	# 2-2
    sprite('rrb050_01', 2)	# 3-4
    sprite('rrb050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('rrb050_02', 1)	# 1-1
    sprite('rrb050_02', 1)	# 2-2
    sprite('rrb050_02', 2)	# 3-4
    sprite('rrb050_01', 2)	# 5-6
    sprite('rrb050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('rrb050_02', 1)	# 1-1
    sprite('rrb050_03', 1)	# 2-2
    sprite('rrb050_02', 2)	# 3-4
    sprite('rrb050_02', 2)	# 5-6
    sprite('rrb050_01', 2)	# 7-8
    sprite('rrb050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('rrb050_03', 1)	# 1-1
    sprite('rrb050_03', 1)	# 2-2
    sprite('rrb050_03', 2)	# 3-4
    sprite('rrb050_02', 2)	# 5-6
    sprite('rrb050_02', 2)	# 7-8
    sprite('rrb050_01', 2)	# 9-10
    sprite('rrb050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('rrb052_00', 1)	# 1-1
    sprite('rrb052_01', 1)	# 2-2
    sprite('rrb052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('rrb052_01', 1)	# 1-1
    sprite('rrb052_02', 1)	# 2-2
    sprite('rrb052_01', 2)	# 3-4
    sprite('rrb052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('rrb052_02', 1)	# 1-1
    sprite('rrb052_02', 1)	# 2-2
    sprite('rrb052_02', 2)	# 3-4
    sprite('rrb052_01', 2)	# 5-6
    sprite('rrb052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('rrb052_02', 1)	# 1-1
    sprite('rrb052_03', 1)	# 2-2
    sprite('rrb052_02', 2)	# 3-4
    sprite('rrb052_02', 2)	# 5-6
    sprite('rrb052_01', 2)	# 7-8
    sprite('rrb052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('rrb052_03', 1)	# 1-1
    sprite('rrb052_03', 1)	# 2-2
    sprite('rrb052_03', 2)	# 3-4
    sprite('rrb052_02', 2)	# 5-6
    sprite('rrb052_02', 2)	# 7-8
    sprite('rrb052_01', 2)	# 9-10
    sprite('rrb052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('rrb054_00', 1)	# 1-1
    sprite('rrb054_01', 1)	# 2-2
    sprite('rrb054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('rrb054_01', 1)	# 1-1
    sprite('rrb054_02', 1)	# 2-2
    sprite('rrb054_01', 2)	# 3-4
    sprite('rrb054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('rrb054_02', 1)	# 1-1
    sprite('rrb054_02', 1)	# 2-2
    sprite('rrb054_02', 2)	# 3-4
    sprite('rrb054_01', 2)	# 5-6
    sprite('rrb054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('rrb054_02', 1)	# 1-1
    sprite('rrb054_03', 1)	# 2-2
    sprite('rrb054_02', 2)	# 3-4
    sprite('rrb054_02', 2)	# 5-6
    sprite('rrb054_01', 2)	# 7-8
    sprite('rrb054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('rrb054_03', 1)	# 1-1
    sprite('rrb054_03', 1)	# 2-2
    sprite('rrb054_03', 2)	# 3-4
    sprite('rrb054_02', 2)	# 5-6
    sprite('rrb054_02', 2)	# 7-8
    sprite('rrb054_01', 2)	# 9-10
    sprite('rrb054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('rrb062_00', 3)	# 1-3
    label(0)
    sprite('rrb062_01', 3)	# 4-6
    sprite('rrb062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('rrb062_03', 3)	# 1-3
    sprite('rrb062_04', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('rrb062_05', 3)	# 1-3
    sprite('rrb062_06', 3)	# 4-6
    label(0)
    sprite('rrb062_07', 3)	# 7-9
    sprite('rrb062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('rrb062_09', 2)	# 1-2
    sprite('rrb062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('rrb063_06', 3)	# 1-3
    sprite('rrb063_07', 3)	# 4-6
    sprite('rrb063_08', 3)	# 7-9
    sprite('rrb063_09', 4)	# 10-13

@State
def CmnActBDownLoop():
    sprite('rrb063_09', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('rrb064_00', 4)	# 1-4
    sprite('rrb064_01', 4)	# 5-8
    sprite('rrb064_02', 4)	# 9-12
    sprite('rrb064_03', 4)	# 13-16
    sprite('rrb064_04', 4)	# 17-20

@State
def CmnActFDownUpper():
    sprite('rrb063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('rrb063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('rrb063_02', 3)	# 1-3
    sprite('rrb063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('rrb063_04', 3)	# 1-3
    sprite('rrb063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('rrb063_06', 3)	# 1-3
    sprite('rrb063_07', 3)	# 4-6
    sprite('rrb063_08', 3)	# 7-9
    sprite('rrb063_09', 4)	# 10-13

@State
def CmnActFDownLoop():
    sprite('rrb063_09', 1)	# 1-1

@State
def CmnActFDown2Stand():
    sprite('rrb064_00', 4)	# 1-4
    sprite('rrb064_01', 4)	# 5-8
    sprite('rrb064_02', 4)	# 9-12
    sprite('rrb064_03', 4)	# 13-16
    sprite('rrb064_04', 4)	# 17-20

@State
def CmnActVDownUpper():
    sprite('rrb062_00', 3)	# 1-3
    label(0)
    sprite('rrb062_01', 3)	# 4-6
    sprite('rrb062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('rrb062_03', 3)	# 1-3
    sprite('rrb062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('rrb062_05', 3)	# 1-3
    sprite('rrb062_06', 3)	# 4-6
    label(0)
    sprite('rrb062_07', 3)	# 7-9
    sprite('rrb062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('rrb062_09', 2)	# 1-2
    sprite('rrb062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('rrb072_00', 3)	# 1-3
    sprite('rrb072_01', 3)	# 4-6
    sprite('rrb072_02', 3)	# 7-9
    label(0)
    sprite('rrb072_01', 3)	# 10-12
    sprite('rrb072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('rrb074_00', 3)	# 1-3
    sprite('rrb074_01', 3)	# 4-6
    sprite('rrb074_02', 3)	# 7-9
    sprite('rrb074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('Action_327_00', 2)	# 1-2
    sprite('Action_327_00', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('rrb050_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('rrb073_00', 3)	# 1-3
    sprite('rrb073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('rrb073_02', 3)	# 1-3
    label(0)
    sprite('rrb073_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('rrb070_00', 2)	# 1-2
    label(0)
    sprite('rrb070_01', 4)	# 3-6
    sprite('rrb070_02', 4)	# 7-10
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('rrb070_03', 5)	# 1-5
    sprite('rrb070_04', 6)	# 6-11
    sprite('rrb070_05', 7)	# 12-18
    sprite('rrb070_06', 2)	# 19-20
    sprite('rrb070_07', 2)	# 21-22
    sprite('rrb070_08', 2)	# 23-24

@State
def CmnActUkemiStagger():
    sprite('rrb070_09', 2)	# 1-2
    sprite('rrb070_10', 3)	# 3-5
    sprite('rrb070_11', 3)	# 6-8

@State
def CmnActUkemiAirF():
    sprite('rrb113_00', 3)	# 1-3
    sprite('rrb113_01', 3)	# 4-6
    sprite('rrb113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('rrb113_00', 3)	# 1-3
    sprite('rrb113_01', 3)	# 4-6
    sprite('rrb113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('rrb113_00', 3)	# 1-3
    sprite('rrb113_01', 3)	# 4-6
    sprite('rrb113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandB():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandN():
    sprite('rrb112_00', 2)	# 1-2
    sprite('rrb112_01', 2)	# 3-4
    sprite('rrb112_02', 2)	# 5-6
    sprite('rrb112_03', 2)	# 7-8
    sprite('rrb112_04', 2)	# 9-10
    sprite('rrb112_05', 2)	# 11-12
    sprite('rrb112_06', 3)	# 13-15
    sprite('rrb112_07', 3)	# 16-18

@State
def CmnActUkemiLandNLanding():
    sprite('rrb020_07', 2)	# 1-2
    sprite('rrb020_08', 2)	# 3-4
    sprite('rrb010_00', 2)	# 5-6
    sprite('rrb010_01', 3)	# 7-9
    sprite('rrb010_02', 3)	# 10-12
    sprite('rrb010_03', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('rrb040_00', 3)	# 1-3
    sprite('rrb040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('rrb040_02', 3)	# 1-3
    sprite('rrb040_03', 3)	# 4-6
    sprite('rrb040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('rrb040_01', 3)	# 1-3
    sprite('rrb040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('rrb040_02', 3)	# 1-3
    sprite('rrb040_03', 3)	# 4-6
    sprite('rrb040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('rrb040_01', 3)	# 1-3
    sprite('rrb040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('rrb040_00', 3)	# 1-3
    sprite('rrb040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('rrb040_02', 3)	# 1-3
    sprite('rrb040_03', 3)	# 4-6
    sprite('rrb040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('rrb040_01', 3)	# 1-3
    sprite('rrb040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('rrb040_02', 3)	# 1-3
    sprite('rrb040_03', 3)	# 4-6
    sprite('rrb040_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('rrb040_01', 3)	# 1-3
    sprite('rrb040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('rrb043_00', 3)	# 1-3
    sprite('rrb043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('rrb043_02', 3)	# 1-3
    sprite('rrb043_03', 3)	# 4-6
    sprite('rrb043_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('rrb043_01', 3)	# 1-3
    sprite('rrb043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('rrb043_02', 3)	# 1-3
    sprite('rrb043_03', 3)	# 4-6
    sprite('rrb043_04', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('rrb043_01', 3)	# 1-3
    sprite('rrb043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('rrb045_00', 3)	# 1-3
    sprite('rrb045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('rrb045_02', 3)	# 1-3
    sprite('rrb045_03', 3)	# 4-6
    sprite('rrb045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('rrb045_01', 3)	# 1-3
    sprite('rrb045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('rrb045_02', 3)	# 1-3
    sprite('rrb045_03', 3)	# 4-6
    sprite('rrb045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('rrb045_01', 3)	# 1-3
    sprite('rrb045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('rrb040_02', 2)	# 1-2
    sprite('rrb040_03', 2)	# 3-4
    sprite('rrb040_03', 1)	# 5-5
    Unknown2042(1)
    sprite('rrb040_01', 6)	# 6-11
    sprite('rrb040_00', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('rrb025_01', 3)	# 1-3
    sprite('rrb025_00', 3)	# 4-6

@State
def CmnActLockWait():
    sprite('rrb040_02', 1)	# 1-1
    sprite('rrb040_01', 3)	# 2-4
    sprite('rrb040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('rrb312_00', 3)	# 1-3
    sprite('rrb312_01', 3)	# 4-6
    sprite('rrb312_02', 4)	# 7-10	 **attackbox here**
    GFX_0('rrb312Eff', 0)
    SFX_3('rrbse_13')
    sprite('rrb312_03', 4)	# 11-14
    sprite('rrb312_04', 3)	# 15-17
    sprite('rrb312_05', 3)	# 18-20
    sprite('rrb312_06', 3)	# 21-23
    sprite('rrb312_07', 3)	# 24-26
    sprite('rrb312_08', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('rrb045_02', 3)	# 1-3
    sprite('rrb045_03', 3)	# 4-6
    sprite('rrb045_04', 3)	# 7-9

@State
def CmnActLandSpin():
    sprite('null', 60)	# 1-60

@State
def CmnActLandSpinDown():
    sprite('null', 60)	# 1-60

@State
def CmnActVertSpin():
    sprite('rrb062_00', 3)	# 1-3
    label(0)
    sprite('rrb062_01', 3)	# 4-6
    sprite('rrb062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('rrb077_00', 3)	# 1-3
    sprite('rrb077_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('rrb077_02', 3)	# 1-3
    label(0)
    sprite('rrb077_03', 3)	# 4-6
    sprite('rrb077_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('rrb077_05', 4)	# 1-4
    sprite('rrb077_06', 5)	# 5-9

@State
def CmnActAomukeSlideKeep():
    sprite('null', 60)	# 1-60

@State
def CmnActAomukeSlideEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstBegin():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstLoop():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActAirBurstBegin():
    sprite('null', 60)	# 1-60

@State
def CmnActAirBurstLoop():
    sprite('null', 60)	# 1-60

@State
def CmnActAirBurstEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActOverDriveBegin():
    sprite('rrb333_00', 3)	# 1-3
    sprite('rrb333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('rrb333_02', 3)	# 1-3
    label(0)
    sprite('rrb333_03', 3)	# 4-6
    sprite('rrb333_04', 3)	# 7-9
    sprite('rrb333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('rrb333_06', 6)	# 1-6
    sprite('rrb333_07', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('rrb333_08', 3)	# 1-3
    sprite('rrb333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('rrb333_02', 4)	# 1-4
    label(0)
    sprite('rrb333_03', 3)	# 5-7
    sprite('rrb333_04', 3)	# 8-10
    sprite('rrb333_05', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('rrb333_09', 3)	# 1-3
    sprite('rrb333_10', 3)	# 4-6
    sprite('rrb020_05', 3)	# 7-9
    sprite('rrb020_06', 3)	# 10-12
    label(0)
    sprite('rrb020_07', 4)	# 13-16
    sprite('rrb020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('rrb333_00', 3)	# 1-3
    sprite('rrb333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('rrb333_02', 3)	# 1-3
    label(0)
    sprite('rrb333_04', 3)	# 4-6
    sprite('rrb333_05', 3)	# 7-9
    sprite('rrb333_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('rrb333_06', 6)	# 1-6
    sprite('rrb333_07', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('rrb333_08', 9)	# 1-9
    sprite('rrb333_08', 32767)	# 10-32776
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('rrb333_08', 3)	# 1-3
    label(0)
    sprite('rrb333_04', 3)	# 4-6
    sprite('rrb333_05', 3)	# 7-9
    sprite('rrb333_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('rrb333_09', 3)	# 1-3
    sprite('rrb333_10', 3)	# 4-6
    sprite('rrb020_05', 3)	# 7-9
    sprite('rrb020_06', 3)	# 10-12
    label(0)
    sprite('rrb020_07', 4)	# 13-16
    sprite('rrb020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('rrb333_00', 3)	# 1-3
    sprite('rrb333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('rrb333_02', 3)	# 1-3
    label(0)
    sprite('rrb333_04', 3)	# 4-6
    sprite('rrb333_05', 3)	# 7-9
    sprite('rrb333_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('rrb333_06', 3)	# 1-3
    sprite('rrb333_07', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('rrb333_08', 3)	# 1-3
    sprite('rrb333_08', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('rrb333_08', 3)	# 1-3
    label(0)
    sprite('rrb333_04', 3)	# 4-6
    sprite('rrb333_05', 3)	# 7-9
    sprite('rrb333_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('rrb333_09', 3)	# 1-3
    sprite('rrb333_10', 3)	# 4-6
    sprite('rrb020_05', 3)	# 7-9
    sprite('rrb020_06', 3)	# 10-12
    label(0)
    sprite('rrb020_07', 4)	# 13-16
    sprite('rrb020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

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
    sprite('rrb250_03', 32767)	# 32-32798	 **attackbox here**
    label(1)
    sprite('rrb250_03ex', 1)	# 32799-32799	 **attackbox here**
    sprite('rrb010_01', 4)	# 32800-32803
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rrb010_02', 9)	# 32804-32812
    Unknown23022(0)
    sprite('rrb010_03', 9)	# 32813-32821
    sprite('rrb010_01', 4)	# 32822-32825
    sprite('rrb010_00', 4)	# 32826-32829

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    sprite('rrb010_01', 3)	# 1-3
    sprite('rrb010_02', 3)	# 4-6
    sprite('rrb010_03', 3)	# 7-9
    sprite('rrb010_01', 3)	# 10-12
    sprite('rrb010_00', 3)	# 13-15
    sprite('rrb320_00', 4)	# 16-19
    sprite('rrb320_01', 5)	# 20-24
    sprite('rrb320_02', 5)	# 25-29
    GFX_0('rrb320MuzzleEff', 0)
    SFX_3('rrbse_05')
    Unknown7009(2)
    sprite('rrb320_03', 5)	# 30-34
    SFX_3('rrbse_01')
    sprite('rrb320_04', 3)	# 35-37	 **attackbox here**
    GFX_0('rrb320Eff', 0)
    sprite('rrb320_05', 4)	# 38-41
    sprite('rrb320_06', 4)	# 42-45
    sprite('rrb320_07', 5)	# 46-50
    sprite('rrb320_08', 5)	# 51-55
    sprite('rrb320_09', 5)	# 56-60
    sprite('rrb320_10', 5)	# 61-65
    sprite('rrb320_11', 5)	# 66-70
    sprite('rrb320_12', 5)	# 71-75

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(1200)
        AirPushbackY(15000)
        PushbackX(12000)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('rrb200_00', 2)	# 1-2
    sprite('rrb200_01', 3)	# 3-5
    sprite('rrb200_02', 3)	# 6-8	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    Unknown7009(0)
    sprite('rrb200_03', 4)	# 9-12
    Recovery()
    Unknown2063()
    sprite('rrb200_04', 5)	# 13-17
    sprite('rrb200_05', 5)	# 18-22

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(17000)
        Unknown9015(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
    sprite('rrb270_00', 4)	# 1-4
    sprite('rrb270_01', 4)	# 5-8
    GFX_0('rrb270Eff', 0)
    SFX_3('rrbse_12')
    sprite('rrb270_02', 2)	# 9-10
    Unknown7009(1)
    sprite('rrb270_03', 3)	# 11-13	 **attackbox here**
    sprite('rrb270_04', 3)	# 14-16
    Recovery()
    Unknown2063()
    sprite('rrb270_05', 3)	# 17-19
    sprite('rrb270_06', 3)	# 20-22
    sprite('rrb270_07', 3)	# 23-25
    sprite('rrb270_08', 3)	# 26-28
    sprite('rrb270_09', 3)	# 29-31

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(-30000)
        PushbackX(19800)
        Unknown9310(1)
        Unknown9015(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        HitOrBlockCancel('AN_NmlAtk5A_4th')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('rrb271_00', 4)	# 1-4
    sprite('rrb271_01', 6)	# 5-10
    SFX_3('rrbse_13')
    sprite('rrb271_02', 4)	# 11-14
    GFX_0('rrb271Eff', 0)
    Unknown7009(2)
    sprite('rrb271_03', 6)	# 15-20	 **attackbox here**
    sprite('rrb271_03', 6)	# 21-26	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('rrb271_04', 4)	# 27-30
    sprite('rrb271_05', 4)	# 31-34
    sprite('rrb271_06', 4)	# 35-38
    sprite('rrb271_07', 4)	# 39-42
    sprite('rrb271_08', 4)	# 43-46
    sprite('rrb271_09', 4)	# 47-50

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(10000)
        AirPushbackY(35000)
        AirUntechableTime(40)
        Hitstop(0)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11099(1)
        Unknown11044(1)
        Unknown30088(1)
        JumpCancel_(0)

        def upon_77():
            Hitstop(8)
            Unknown23151(22, 104)
            teleportRelativeX(10000)
            sendToLabel(0)

        def upon_78():
            ScreenShake(10000, 0)
            GFX_0('rrb405_Issen', 0)
            GFX_0('rrbHitPetal_Add', 102)
            GFX_0('rrbHitPetal_Burst', 102)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            EnableCollision(1)
            Unknown2015(-1)
    sprite('rrb405_00', 3)	# 1-3
    sprite('rrb405_01', 3)	# 4-6
    Unknown1084(1)
    sprite('rrb405_02', 3)	# 7-9
    SFX_3('rrbse_06')
    sprite('rrb405_03', 3)	# 10-12
    Unknown7007('7272623230395f310000000000000000640000007272623230395f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rrb405_04', 12)	# 13-24	 **attackbox here**
    GFX_0('rrb405Eff', 0)
    physicsXImpulse(60000)
    Unknown8003(100, 1, 1)
    Unknown3004(-30)
    EnableCollision(0)
    Unknown2015(40)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('rrb405_04', 6)	# 25-30	 **attackbox here**
    clearUponHandler(77)
    loopRest()
    label(9)
    sprite('rrb405_05', 6)	# 31-36
    clearUponHandler(77)
    Unknown1019(50)
    Unknown3001(128)
    Unknown3004(20)
    EnableCollision(1)
    Unknown2015(-1)
    Recovery()
    Unknown2063()
    sprite('rrb405_06', 6)	# 37-42
    Unknown8007(100, 1, 1)
    Unknown1019(50)
    sprite('rrb405_07', 6)	# 43-48
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown1019(50)
    sprite('rrb405_08', 10)	# 49-58
    Unknown1019(0)

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('rrb201_00', 3)	# 1-3
    sprite('rrb201_01', 3)	# 4-6
    sprite('rrb201_02', 3)	# 7-9
    Unknown7009(1)
    SFX_3('rrbse_03')
    sprite('rrb201_03', 6)	# 10-15	 **attackbox here**
    GFX_0('rrb201Eff', 100)
    sprite('rrb201_04', 6)	# 16-21
    Recovery()
    Unknown2063()
    sprite('rrb201_05', 3)	# 22-24
    sprite('rrb201_06', 3)	# 25-27
    sprite('rrb201_07', 3)	# 28-30
    sprite('rrb201_08', 3)	# 31-33

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(11)
        AirPushbackX(-3000)
        AirPushbackY(16000)
        PushbackX(12000)
        Unknown30055('e09304003200000000000000')
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        HitOrBlockCancel('AN_NmlAtk5B_3rd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('rrb202_00', 3)	# 1-3
    sprite('rrb202_01', 3)	# 4-6
    sprite('rrb202_02', 3)	# 7-9
    SFX_3('rrbse_04')
    sprite('rrb202_03', 3)	# 10-12
    Unknown7009(2)
    sprite('rrb202_04', 4)	# 13-16	 **attackbox here**
    GFX_0('rrb202Eff', 100)
    sprite('rrb202_05', 4)	# 17-20
    Recovery()
    Unknown2063()
    sprite('rrb202_06', 4)	# 21-24
    sprite('rrb202_07', 4)	# 25-28
    sprite('rrb202_08', 4)	# 29-32
    sprite('rrb202_09', 4)	# 33-36
    sprite('rrb202_10', 4)	# 37-40

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(24)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('rrb203_00', 2)	# 1-2
    sprite('rrb203_01', 2)	# 3-4
    sprite('rrb203_02', 2)	# 5-6
    sprite('rrb203_03', 2)	# 7-8
    sprite('rrb203_04', 2)	# 9-10
    sprite('rrb203_05', 2)	# 11-12
    sprite('rrb203_06', 2)	# 13-14
    Unknown7009(3)
    SFX_3('rrbse_03')
    sprite('rrb203_07', 3)	# 15-17	 **attackbox here**
    GFX_0('rrb203Eff', 0)
    sprite('rrb203_08', 3)	# 18-20
    Recovery()
    Unknown2063()
    sprite('rrb203_09', 3)	# 21-23
    sprite('rrb203_10', 3)	# 24-26
    sprite('rrb203_11', 3)	# 27-29
    sprite('rrb203_12', 3)	# 30-32
    sprite('rrb203_13', 3)	# 33-35
    sprite('rrb203_14', 3)	# 36-38
    sprite('rrb203_15', 3)	# 39-41
    sprite('rrb203_16', 3)	# 42-44
    sprite('rrb203_17', 3)	# 45-47
    sprite('rrb203_18', 3)	# 48-50
    sprite('rrb203_19', 3)	# 51-53
    sprite('rrb203_20', 3)	# 54-56

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('rrb230_00', 1)	# 1-1
    Unknown23145('NmlAtk2A')
    Unknown23183('7272623233305f30350000000000000000000000000000000000000000000000010000000200000000000000')
    sprite('rrb230_01', 2)	# 2-3
    sprite('rrb230_02', 2)	# 4-5
    sprite('rrb230_03', 1)	# 6-6
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb230_04', 2)	# 7-8	 **attackbox here**
    sprite('rrb230_03', 3)	# 9-11
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('rrb230_02', 3)	# 12-14
    sprite('rrb230_01', 3)	# 15-17
    sprite('rrb230_00', 3)	# 18-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('rrb231_00', 4)	# 1-4
    sprite('rrb231_01', 3)	# 5-7
    sprite('rrb231_02', 3)	# 8-10
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown7009(1)
    SFX_3('rrbse_03')
    sprite('rrb231_03', 4)	# 11-14	 **attackbox here**
    GFX_0('rrb231Eff', 0)
    sprite('rrb231_04', 4)	# 15-18
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('rrb231_05', 5)	# 19-23
    sprite('rrb231_06', 5)	# 24-28
    sprite('rrb231_07', 5)	# 29-33
    sprite('rrb231_08', 6)	# 34-39

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackY(15000)
        AirUntechableTime(30)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HitLow(2)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
    sprite('rrb232_00', 3)	# 1-3
    sprite('rrb232_01', 3)	# 4-6
    sprite('rrb232_02', 3)	# 7-9
    SFX_3('rrbse_05')
    sprite('rrb232_03', 3)	# 10-12
    Unknown7009(2)
    sprite('rrb232_04', 3)	# 13-15	 **attackbox here**
    GFX_0('rrb232Eff', 0)
    sprite('rrb232_05', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('rrb232_06', 3)	# 19-21
    sprite('rrb232_07', 3)	# 22-24
    sprite('rrb232_08', 3)	# 25-27
    sprite('rrb232_09', 3)	# 28-30
    sprite('rrb232_10', 3)	# 31-33

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        AirUntechableTime(19)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rrb251_00', 2)	# 1-2
    sprite('rrb251_01', 3)	# 3-5
    sprite('rrb251_02', 3)	# 6-8
    Unknown7009(3)
    SFX_3('rrbse_03')
    sprite('rrb251_03', 3)	# 9-11	 **attackbox here**
    GFX_0('rrb251Eff', 0)
    sprite('rrb251_04', 3)	# 12-14
    Recovery()
    Unknown2063()
    sprite('rrb251_05', 3)	# 15-17
    sprite('rrb251_06', 3)	# 18-20
    sprite('rrb251_07', 3)	# 21-23
    sprite('rrb251_08', 3)	# 24-26

@State
def NmlAtkAIR2A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AirPushbackY(11000)
    sprite('rrb250_00', 2)	# 1-2
    sprite('rrb250_01', 2)	# 3-4
    sprite('rrb250_02', 2)	# 5-6
    label(1)
    sprite('rrb250_03', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('rrb250_04', 2)	# 9-10
    sprite('rrb250_05', 1)	# 11-11
    sprite('rrb250_01', 1)	# 12-12
    sprite('rrb250_02', 1)	# 13-13
    sprite('rrb250_06', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    loopRest()
    if CheckInput(0x1):
        sendToLabel(0)
    else:
        sendToLabel(9)
    label(0)
    sprite('rrb250_07', 1)	# 16-16
    sprite('rrb250_08', 1)	# 17-17
    sprite('rrb250_01', 1)	# 18-18
    sprite('rrb250_02', 1)	# 19-19
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('rrb250_07', 1)	# 20-20
    Recovery()
    Unknown2063()
    sprite('rrb250_08', 4)	# 21-24
    sprite('rrb250_01', 4)	# 25-28

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        AirUntechableTime(19)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtkAIR5B_2nd')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rrb252_00', 3)	# 1-3
    sprite('rrb252_01', 3)	# 4-6
    sprite('rrb252_02', 2)	# 7-8
    SFX_3('rrbse_05')
    sprite('rrb252_03', 2)	# 9-10
    Unknown7009(4)
    sprite('rrb252_04', 5)	# 11-15	 **attackbox here**
    GFX_0('rrb252Eff', 0)
    sprite('rrb252_05', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('rrb252_06', 3)	# 19-21
    sprite('rrb252_07', 3)	# 22-24
    sprite('rrb252_08', 3)	# 25-27
    sprite('rrb252_09', 3)	# 28-30
    sprite('rrb252_10', 3)	# 31-33

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11065(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    sprite('rrb253_00', 3)	# 1-3
    physicsYImpulse(16000)
    setGravity(1600)
    sprite('rrb253_01', 3)	# 4-6
    sprite('rrb253_02', 4)	# 7-10
    sprite('rrb204_04', 3)	# 11-13
    sprite('rrb204_05', 4)	# 14-17
    Unknown7009(5)
    sprite('rrb204_06', 3)	# 18-20	 **attackbox here**
    GFX_0('rrb204MuzzleEff', 0)
    loopRest()
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    label(0)
    sprite('rrb204_07', 3)	# 21-23
    Recovery()
    Unknown2063()
    sprite('rrb204_08', 3)	# 24-26
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rrb204_09', 3)	# 27-29
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rrb204_10', 7)	# 30-36
    SFX_3('rrbse_13')
    sprite('rrb204_11', 4)	# 37-40
    sprite('rrb204_12', 3)	# 41-43
    sprite('rrb204_13', 3)	# 44-46
    sprite('rrb204_14', 3)	# 47-49
    sprite('rrb204_15', 5)	# 50-54

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
                Unknown1015(1000)
                if (SLOT_12 >= 32000):
                    SLOT_12 = 32000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rrb032_14', 3)	# 1-3
    sprite('rrb032_00', 4)	# 4-7
    sprite('rrb032_01', 6)	# 8-13
    label(0)
    sprite('rrb032_02', 4)	# 14-17
    sprite('rrb032_03', 4)	# 18-21
    sprite('rrb032_04', 4)	# 22-25
    Unknown8006(100, 1, 1)
    sprite('rrb032_05', 4)	# 26-29
    sprite('rrb032_06', 4)	# 30-33
    sprite('rrb032_07', 4)	# 34-37
    sprite('rrb032_08', 4)	# 38-41
    Unknown8006(100, 1, 1)
    sprite('rrb032_09', 4)	# 42-45
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb310_00', 1)	# 46-46
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rrb310_01', 2)	# 47-48
    sprite('rrb310_02', 3)	# 49-51	 **attackbox here**
    Unknown1084(1)
    sprite('rrb310_03', 4)	# 52-55
    SFX_0('010_swing_sword_0')
    sprite('rrb310_04', 4)	# 56-59
    Unknown7006('rrb155_0', 100, 828535410, 828323125, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('rrb310_05', 4)	# 60-63
    sprite('rrb310_06', 4)	# 64-67
    sprite('rrb310_07', 4)	# 68-71
    sprite('rrb310_08', 3)	# 72-74

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9071()
        AirPushbackY(36000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
    sprite('rrb310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rrb311_00', 4)	# 4-7
    tag_voice(1, 'rrb153_0', 'rrb153_1', '', '')
    sprite('rrb311_01', 4)	# 8-11
    sprite('rrb311_02', 4)	# 12-15
    sprite('rrb311_03', 12)	# 16-27
    sprite('rrb311_04', 4)	# 28-31
    sprite('rrb311_05', 4)	# 32-35	 **attackbox here**
    physicsYImpulse(15000)
    physicsXImpulse(10000)
    Unknown1028(-400)
    Unknown1043()
    JumpCancel_(1)
    GFX_0('rrb311Eff', 0)
    SFX_3('rrbse_03')
    SFX_0('001_airbackdash_1')
    tag_voice(0, 'rrb154_0', 'rrb154_1', '', '')
    sprite('rrb311_06', 4)	# 36-39
    sprite('rrb311_07', 4)	# 40-43
    sprite('rrb311_08', 4)	# 44-47
    sprite('rrb311_09', 32767)	# 48-32814
    sendToLabelUpon(2, 1)
    label(1)
    sprite('rrb601_03', 2)	# 32815-32816
    Unknown1084(1)
    GFX_0('rrb311EndEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb601_04', 2)	# 32817-32818
    sprite('rrb601_05', 2)	# 32819-32820
    sprite('rrb601_06', 2)	# 32821-32822
    sprite('rrb601_07', 2)	# 32823-32824
    sprite('rrb601_08', 2)	# 32825-32826

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
                Unknown1015(1000)
                if (SLOT_12 >= 32000):
                    SLOT_12 = 32000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rrb032_14', 3)	# 1-3
    sprite('rrb032_00', 4)	# 4-7
    sprite('rrb032_01', 6)	# 8-13
    label(0)
    sprite('rrb032_02', 4)	# 14-17
    sprite('rrb032_03', 4)	# 18-21
    sprite('rrb032_04', 4)	# 22-25
    Unknown8006(100, 1, 1)
    sprite('rrb032_05', 4)	# 26-29
    sprite('rrb032_06', 4)	# 30-33
    sprite('rrb032_07', 4)	# 34-37
    sprite('rrb032_08', 4)	# 38-41
    Unknown8006(100, 1, 1)
    sprite('rrb032_09', 4)	# 42-45
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb310_00', 1)	# 46-46
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rrb310_01', 2)	# 47-48
    sprite('rrb310_02', 3)	# 49-51	 **attackbox here**
    Unknown1084(1)
    sprite('rrb310_03', 4)	# 52-55
    SFX_0('010_swing_sword_0')
    sprite('rrb310_04', 4)	# 56-59
    Unknown7006('rrb155_0', 100, 828535410, 828323125, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('rrb310_05', 4)	# 60-63
    sprite('rrb310_06', 4)	# 64-67
    sprite('rrb310_07', 4)	# 68-71
    sprite('rrb310_08', 3)	# 72-74

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(50)
        Unknown11092(1)
        AirHitstunAnimation(5)
        GroundedHitstunAnimation(5)
        hitstun(60)
        AirUntechableTime(60)
        PushbackX(55000)
        Hitstop(0)
        Unknown11057(0)
        Unknown11050('060000007272624869744566660000000000000000000000000000000000000000000000')
        Unknown11099(1)
        Unknown11080(1)
        Unknown11069('BackThrowExe')
        JumpCancel_(0)
    sprite('rrb310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rrb310_02', 1)	# 4-4	 **attackbox here**
    EnableCollision(0)
    tag_voice(1, 'rrb153_0', 'rrb153_1', '', '')
    sprite('rrb313_00', 4)	# 5-8
    sprite('rrb313_01', 4)	# 9-12
    sprite('rrb313_02', 4)	# 13-16
    sprite('rrb311_02', 4)	# 17-20
    Unknown2005()
    sprite('rrb311_03', 8)	# 21-28
    sprite('rrb311_04', 4)	# 29-32
    sprite('rrb311_05', 4)	# 33-36	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2000)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    Unknown9071()
    AirPushbackY(36000)
    Hitstop(16)
    Unknown9016(1)
    Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
    Unknown11099(0)
    Unknown11080(0)
    Unknown11069('')
    physicsYImpulse(15000)
    physicsXImpulse(10000)
    Unknown1028(-400)
    Unknown1043()
    GFX_0('rrb311Eff', 0)
    SFX_3('rrbse_03')
    SFX_0('001_airbackdash_1')
    tag_voice(0, 'rrb154_0', 'rrb154_1', '', '')
    clearUponHandler(10)

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
    sprite('rrb311_06', 4)	# 37-40
    sprite('rrb311_07', 4)	# 41-44
    sprite('rrb311_08', 4)	# 45-48
    sprite('rrb311_09', 32767)	# 49-32815
    sendToLabelUpon(2, 1)
    label(1)
    sprite('rrb601_03', 2)	# 32816-32817
    Unknown1084(1)
    GFX_0('rrb311EndEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb601_04', 2)	# 32818-32819
    sprite('rrb601_05', 2)	# 32820-32821
    sprite('rrb601_06', 2)	# 32822-32823
    sprite('rrb601_07', 2)	# 32824-32825
    sprite('rrb601_08', 2)	# 32826-32827

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1250)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(36000)
        AirUntechableTime(60)
        Hitstop(4)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
    sprite('rrb320_00', 3)	# 1-3
    Unknown7006('rrb200_1', 100, 845312626, 845099056, 0, 0, 100, 845312626, 811544624, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rrb320_01', 3)	# 4-6
    sprite('rrb320_02', 3)	# 7-9
    GFX_0('rrb320MuzzleEff', 0)
    SFX_3('rrbse_05')
    sprite('rrb320_03', 3)	# 10-12
    SFX_3('rrbse_01')
    sprite('rrb320_04', 2)	# 13-14	 **attackbox here**
    GFX_0('rrb320Eff', 0)
    sprite('rrb320_04', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('rrb320_04', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('rrb320_05', 5)	# 19-23
    setInvincible(0)
    sprite('rrb320_06', 5)	# 24-28
    sprite('rrb320_07', 8)	# 29-36
    sprite('rrb320_08', 9)	# 37-45
    sprite('rrb320_09', 5)	# 46-50
    sprite('rrb320_10', 5)	# 51-55
    sprite('rrb320_11', 5)	# 56-60
    sprite('rrb320_12', 5)	# 61-65

@Subroutine
def SpDashInit():
    AttackLevel_(4)
    Damage(1200)
    AttackP2(75)
    Unknown9015(1)
    Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    Unknown2037(0)
    if Unknown23145('SpDash_Front'):
        Unknown2037(1)
        Unknown30068(1)
    if Unknown23145('SpDash_Back'):
        Unknown2037(1)
        Unknown30068(1)
    if Unknown23145('SpDash_AntiAir'):
        Unknown2037(1)
        Unknown30068(1)
    if Unknown23145('AirSpDash_Front'):
        Unknown2037(1)
        Unknown30068(1)
    if Unknown23145('AirSpDash_Back'):
        Unknown2037(1)
        Unknown30068(1)
    if Unknown23145('AirSpDash_AntiLand'):
        Unknown2037(1)
        Unknown30068(1)

    def upon_STATE_END():
        Unknown3001(255)
        Unknown3004(0)
        Unknown22001(-1)
        Unknown22003(-1)

@Subroutine
def SpDash_Hasei():

    def upon_12():
        HitOrBlockCancel('SpDash_Front')
        HitOrBlockCancel('SpDash_Back')
        HitOrBlockCancel('SpDash_AntiAir')
        HitOrBlockCancel('AirSpDash_Front')
        HitOrBlockCancel('AirSpDash_Back')
        HitOrBlockCancel('AirSpDash_AntiLand')

@Subroutine
def SpDash_ShotHIT():

    def upon_43():
        if (SLOT_48 == 3001):
            HitOrBlockCancel('SpDash_Front')
            HitOrBlockCancel('SpDash_Back')
            HitOrBlockCancel('SpDash_AntiAir')
            HitOrBlockCancel('AirSpDash_Front')
            HitOrBlockCancel('AirSpDash_Back')
            HitOrBlockCancel('AirSpDash_AntiLand')

@Subroutine
def SpDash_DoNotBeginCancel():
    if Unknown23145('Shot'):
        Unknown30068(1)
    if Unknown23145('AttackAndShotB'):
        Unknown30068(1)
    if Unknown23145('MultiAssault'):
        Unknown30068(1)
    if Unknown23145('AirRolling_A'):
        Unknown30068(1)
    if Unknown23145('AirRolling_B'):
        Unknown30068(1)
    if Unknown23145('AirRolling_Ex'):
        Unknown30068(1)

@Subroutine
def DeriveInput_Hasei_SpDash():
    Unknown14070('Hasei_SpDash_Back')
    Unknown14070('Hasei_SpDash_Front')
    Unknown14070('Hasei_SpDash_AntiAir')
    Unknown14070('Hasei_AirSpDash_Back')
    Unknown14070('Hasei_AirSpDash_Front')
    Unknown14070('Hasei_AirSpDash_AntiLand')

@Subroutine
def DeriveTiming_Hasei_SpDash():
    Unknown14072('Hasei_SpDash_Back')
    Unknown14072('Hasei_SpDash_Front')
    Unknown14072('Hasei_SpDash_AntiAir')
    Unknown14072('Hasei_AirSpDash_Back')
    Unknown14072('Hasei_AirSpDash_Front')
    Unknown14072('Hasei_AirSpDash_AntiLand')

@Subroutine
def DeriveClear_Hasei_SpDash():
    Unknown14074('Hasei_SpDash_Back')
    Unknown14074('Hasei_SpDash_Front')
    Unknown14074('Hasei_SpDash_AntiAir')
    Unknown14074('Hasei_AirSpDash_Back')
    Unknown14074('Hasei_AirSpDash_Front')
    Unknown14074('Hasei_AirSpDash_AntiLand')

@State
def SpDash_Front():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SpDashInit')
        callSubroutine('SpDash_DoNotBeginCancel')
        AttackP1(80)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(10000)
        WallbounceReboundTime(10)
        AirUntechableTime(50)
        Unknown11099(1)
        Unknown11056(0)
    sprite('rrb400_00', 4)	# 1-4
    sprite('rrb400_01', 4)	# 5-8
    GFX_0('rrb400PetalEff', 0)
    if (not SLOT_2):
        Unknown7006('rrb201_1', 100, 845312626, 845099312, 0, 0, 100, 845312626, 811544880, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rrb400_02ex', 3)	# 9-11	 **attackbox here**
    Unknown8007(100, 1, 0)
    GFX_0('rrb400MuzzleEff', 0)
    physicsXImpulse(10000)
    EnableCollision(0)
    callSubroutine('DeriveInput_Hasei_SpDash')
    sprite('rrb400_03', 2)	# 12-13
    Unknown1019(600)
    Unknown3001(128)
    Unknown3004(-20)
    SFX_3('rrbse_08')
    sprite('rrb400_02', 2)	# 14-15
    sprite('rrb400_03', 2)	# 16-17
    sprite('rrb400_04', 2)	# 18-19
    physicsXImpulse(20000)
    EnableCollision(1)
    Unknown3001(128)
    Unknown3004(20)
    sprite('rrb400_05', 3)	# 20-22
    sprite('rrb400_06', 2)	# 23-24
    Unknown8007(100, 1, 1)
    Unknown3001(255)
    Unknown3004(0)
    callSubroutine('DeriveTiming_Hasei_SpDash')
    sprite('rrb400_06', 2)	# 25-26
    Unknown21012('727262343030506574616c45666600000000000000000000000000000000000020000000')
    Unknown1019(80)
    SFX_3('rrbse_01')
    sprite('rrb400_07', 2)	# 27-28
    Unknown1019(80)
    callSubroutine('DeriveClear_Hasei_SpDash')
    sprite('rrb400_07', 2)	# 29-30
    GFX_0('rrbCaseEff', 0)
    Unknown1019(80)
    sprite('rrb400_08', 2)	# 31-32
    Unknown1019(80)
    Unknown8010(100, 1, 1)
    sprite('rrb400_08', 2)	# 33-34
    Unknown1084(1)

@State
def SpDash_Back():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SpDashInit')
        callSubroutine('SpDash_DoNotBeginCancel')
        AttackP1(80)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(10000)
        WallbounceReboundTime(10)
        AirUntechableTime(50)
        Unknown11056(0)
    sprite('rrb401_00', 4)	# 1-4
    sprite('rrb401_01', 4)	# 5-8
    GFX_0('rrb401PetalEff', 0)
    if (not SLOT_2):
        Unknown7006('rrb203_1', 100, 845312626, 845099824, 0, 0, 100, 845312626, 811545392, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rrb401_02ex', 3)	# 9-11	 **attackbox here**
    GFX_0('rrb401MuzzleEff', 0)
    physicsXImpulse(-5000)
    EnableCollision(0)
    callSubroutine('DeriveInput_Hasei_SpDash')
    sprite('rrb401_03', 2)	# 12-13
    Unknown1019(600)
    Unknown3001(128)
    Unknown3004(-20)
    SFX_3('rrbse_08')
    sprite('rrb401_02', 2)	# 14-15
    sprite('rrb401_03', 2)	# 16-17
    sprite('rrb401_04', 2)	# 18-19
    physicsXImpulse(-6000)
    physicsYImpulse(8000)
    setGravity(2000)
    EnableCollision(1)
    Unknown3001(128)
    Unknown3004(20)
    callSubroutine('DeriveTiming_Hasei_SpDash')
    sprite('rrb401_05', 3)	# 20-22
    Unknown21012('727262343031506574616c45666600000000000000000000000000000000000020000000')
    SFX_3('rrbse_01')
    sprite('rrb401_06', 3)	# 23-25
    sprite('rrb401_07', 32767)	# 26-32792
    sendToLabelUpon(2, 9)
    label(9)
    sprite('rrb401_08', 4)	# 32793-32796
    callSubroutine('DeriveClear_Hasei_SpDash')
    Unknown1019(80)
    Unknown8000(100, 1, 1)
    sprite('rrb401_09', 4)	# 32797-32800
    GFX_0('rrbCaseEff', 0)
    Unknown1019(80)

@State
def SpDash_AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SpDashInit')
        callSubroutine('SpDash_DoNotBeginCancel')
        AttackP1(80)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(1000)
        AirPushbackY(-30000)
        AirUntechableTime(50)
        Unknown9190(1)
        Unknown11099(1)
        Unknown11056(0)
    sprite('rrb402_00', 2)	# 1-2
    sprite('rrb402_01', 2)	# 3-4
    Unknown8003(100, 1, 1)
    sprite('rrb402_02', 3)	# 5-7
    GFX_0('rrb402PetalEff', 0)
    sprite('rrb402_03ex', 3)	# 8-10	 **attackbox here**
    GFX_0('rrb402MuzzleEff', 0)
    physicsXImpulse(5000)
    physicsYImpulse(4000)
    EnableCollision(0)
    Unknown2061(1)
    if (not SLOT_2):
        Unknown7006('rrb205_1', 100, 845312626, 845100336, 0, 0, 100, 845312626, 811545904, 0, 0, 100, 0, 0, 0, 0, 0)
    callSubroutine('DeriveInput_Hasei_SpDash')
    Unknown14074('Hasei_SpDash_AntiAir')
    sprite('rrb402_03', 5)	# 11-15
    Unknown1019(650)
    YAccel(650)
    Unknown3001(128)
    Unknown3004(-20)
    SFX_3('rrbse_08')
    sprite('rrb402_04', 3)	# 16-18
    Unknown1019(80)
    Unknown1028(-400)
    YAccel(80)
    setGravity(1600)
    EnableCollision(1)
    Unknown3001(128)
    Unknown3004(20)
    sprite('rrb402_05', 3)	# 19-21
    Unknown1019(80)
    YAccel(80)
    callSubroutine('DeriveTiming_Hasei_SpDash')
    sprite('rrb402_06', 3)	# 22-24
    Unknown21012('727262343032506574616c45666600000000000000000000000000000000000020000000')
    Unknown1019(80)
    YAccel(80)
    SFX_3('rrbse_01')
    sprite('rrb402_07', 2)	# 25-26
    callSubroutine('DeriveClear_Hasei_SpDash')
    Unknown1019(80)
    YAccel(80)
    sprite('rrb402_08', 2)	# 27-28
    Unknown1019(80)
    YAccel(80)
    sprite('rrb402_09', 2)	# 29-30
    GFX_0('rrbCaseEff', 0)
    Unknown1019(80)
    YAccel(80)

@State
def AirSpDash_Front():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('SpDashInit')
        callSubroutine('SpDash_DoNotBeginCancel')
        AttackP1(80)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(10000)
        WallbounceReboundTime(10)
        AirUntechableTime(50)
        Unknown11099(1)
        Unknown11056(0)
    sprite('rrb400_09', 3)	# 1-3
    sprite('rrb400_09', 1)	# 4-4
    SLOT_4 = 0
    sprite('rrb400_10', 4)	# 5-8
    GFX_0('rrb400PetalEff', 0)
    if (not SLOT_2):
        Unknown7006('rrb202_1', 100, 845312626, 845099568, 0, 0, 100, 845312626, 811545136, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown1084(1)
    Unknown2061(1)
    sprite('rrb400_02ex', 3)	# 9-11	 **attackbox here**
    GFX_0('rrb400MuzzleEff', 0)
    physicsXImpulse(6000)
    EnableCollision(0)
    callSubroutine('DeriveInput_Hasei_SpDash')
    sprite('rrb400_03', 2)	# 12-13
    Unknown1019(600)
    Unknown3001(128)
    Unknown3004(-20)
    SFX_3('rrbse_08')
    sprite('rrb400_02', 2)	# 14-15
    sprite('rrb400_03', 2)	# 16-17
    sprite('rrb400_04', 2)	# 18-19
    physicsXImpulse(20000)
    physicsYImpulse(8000)
    setGravity(1600)
    EnableCollision(1)
    Unknown3001(128)
    Unknown3004(20)
    sprite('rrb400_11', 3)	# 20-22
    sprite('rrb400_12', 3)	# 23-25
    Unknown3001(255)
    Unknown3004(0)
    Unknown1019(80)
    callSubroutine('DeriveTiming_Hasei_SpDash')
    sprite('rrb400_13', 3)	# 26-28
    callSubroutine('DeriveClear_Hasei_SpDash')
    GFX_0('rrbCaseEff', 0)
    Unknown21012('727262343030506574616c45666600000000000000000000000000000000000020000000')
    SFX_3('rrbse_01')
    Unknown1019(80)
    sprite('rrb400_14', 3)	# 29-31
    Unknown1019(80)

@State
def AirSpDash_Back():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('SpDashInit')
        callSubroutine('SpDash_DoNotBeginCancel')
        AttackP1(80)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(10000)
        WallbounceReboundTime(10)
        AirUntechableTime(50)
        Unknown11056(0)
    sprite('rrb401_10', 3)	# 1-3
    sprite('rrb401_10', 3)	# 4-6
    SLOT_4 = 0
    GFX_0('rrb401PetalEff', 0)
    if (not SLOT_2):
        Unknown7006('rrb204_1', 100, 845312626, 845100080, 0, 0, 100, 845312626, 811545648, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown1084(1)
    Unknown2061(1)
    sprite('rrb401_02ex', 3)	# 7-9	 **attackbox here**
    GFX_0('rrb401MuzzleEff', 0)
    physicsXImpulse(-5000)
    EnableCollision(0)
    callSubroutine('DeriveInput_Hasei_SpDash')
    sprite('rrb401_03', 2)	# 10-11
    Unknown1019(600)
    Unknown3001(128)
    Unknown3004(-20)
    SFX_3('rrbse_08')
    sprite('rrb401_02', 2)	# 12-13
    sprite('rrb401_03', 2)	# 14-15
    sprite('rrb401_04', 5)	# 16-20
    physicsXImpulse(-4000)
    physicsYImpulse(12000)
    setGravity(2000)
    EnableCollision(1)
    Unknown3001(128)
    Unknown3004(20)
    callSubroutine('DeriveTiming_Hasei_SpDash')
    sprite('rrb401_05', 3)	# 21-23
    Unknown21012('727262343031506574616c45666600000000000000000000000000000000000020000000')
    SFX_3('rrbse_01')
    sprite('rrb401_06', 3)	# 24-26
    sprite('rrb401_11', 3)	# 27-29
    callSubroutine('DeriveClear_Hasei_SpDash')
    sprite('rrb401_12', 3)	# 30-32
    sprite('rrb401_13', 3)	# 33-35
    GFX_0('rrbCaseEff', 0)

@State
def AirSpDash_AntiLand():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('SpDashInit')
        callSubroutine('SpDash_DoNotBeginCancel')
        AttackP1(80)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(36000)
        AirUntechableTime(50)
        Unknown11099(1)
        Unknown11056(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            Unknown1028(500)
            setGravity(400)
    sprite('rrb403_00', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(-5000)
    physicsYImpulse(4000)
    sprite('rrb403_01', 3)	# 4-6
    SLOT_4 = 0
    if (not SLOT_2):
        Unknown7006('rrb206_1', 100, 845312626, 845100592, 0, 0, 100, 845312626, 811546160, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rrb403_02', 3)	# 7-9
    Unknown1084(1)
    sprite('rrb403_03ex', 3)	# 10-12	 **attackbox here**
    GFX_0('rrb403PetalEff', 0)
    GFX_0('rrb403MuzzleEff', 0)
    physicsXImpulse(5000)
    physicsYImpulse(-4000)
    EnableCollision(0)
    callSubroutine('DeriveInput_Hasei_SpDash')
    Unknown14074('Hasei_AirSpDash_AntiLand')
    sprite('rrb403_04', 3)	# 13-15
    Unknown1019(1100)
    YAccel(1100)
    Unknown3001(128)
    Unknown3004(-20)
    SFX_3('rrbse_08')
    label(0)
    sprite('rrb403_03', 3)	# 16-18
    sprite('rrb403_04', 3)	# 19-21
    gotoLabel(0)
    label(9)
    sprite('rrb403_05', 6)	# 22-27
    Unknown1019(20)
    YAccel(0)
    Unknown1039(0)
    EnableCollision(1)
    Unknown3001(128)
    Unknown3004(20)
    Unknown8000(100, 1, 1)
    callSubroutine('DeriveTiming_Hasei_SpDash')
    sprite('rrb403_06', 2)	# 28-29
    callSubroutine('DeriveClear_Hasei_SpDash')
    GFX_0('rrbCaseEff', 0)
    Unknown21012('727262343033506574616c45666600000000000000000000000000000000000020000000')
    SFX_3('rrbse_01')
    Unknown1019(80)
    sprite('rrb403_07', 2)	# 30-31
    Unknown1019(80)
    sprite('rrb403_08', 2)	# 32-33
    Unknown1019(80)
    Unknown8010(100, 1, 1)

@State
def AttackAndShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        PushbackX(44800)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
    sprite('rrb404_00', 3)	# 1-3
    sprite('rrb404_01', 3)	# 4-6
    sprite('rrb404_02', 3)	# 7-9
    GFX_0('rrb404Eff', 0)
    SFX_3('rrbse_13')
    Unknown7006('rrb207_1', 100, 845312626, 845100848, 0, 0, 100, 845312626, 811546416, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rrb404_03', 3)	# 10-12
    sprite('rrb404_04', 4)	# 13-16	 **attackbox here**
    Unknown8004(0, 1, 1)
    Unknown1084(1)
    sprite('rrb404_05', 4)	# 17-20
    sprite('rrb404_06', 4)	# 21-24
    sprite('rrb404_07', 4)	# 25-28
    sprite('rrb404_08', 3)	# 29-31
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotA', 0)
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 32-34
    sprite('rrb404_10', 3)	# 35-37
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 38-40
    sprite('rrb404_12', 6)	# 41-46
    sprite('rrb404_13', 3)	# 47-49
    sprite('rrb404_14', 3)	# 50-52
    Unknown12046(0)
    sprite('rrb404_15', 3)	# 53-55
    GFX_0('rrb404EndEff', 0)
    SFX_3('rrbse_13')
    sprite('rrb404_16', 3)	# 56-58
    sprite('rrb404_17', 3)	# 59-61
    sprite('rrb404_18', 3)	# 62-64
    sprite('rrb404_19', 3)	# 65-67

@State
def AttackAndShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirUntechableTime(30)
        PushbackX(44800)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        callSubroutine('SpDash_Hasei')
        callSubroutine('SpDash_ShotHIT')
    sprite('rrb404_00', 3)	# 1-3
    sprite('rrb404_01', 3)	# 4-6
    sprite('rrb404_02', 3)	# 7-9
    GFX_0('rrb404Eff', 0)
    SFX_3('rrbse_03')
    tag_voice(1, 'rrb207_1', 'rrb207_2', 'rrb207_0', '')
    sprite('rrb404_03', 3)	# 10-12
    sprite('rrb404_04', 6)	# 13-18	 **attackbox here**
    Unknown8004(0, 1, 1)
    Unknown1084(1)
    sprite('rrb404_05', 6)	# 19-24
    sprite('rrb404_06', 6)	# 25-30
    sprite('rrb404_07', 6)	# 31-36
    sprite('rrb404_08', 3)	# 37-39
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotB', 0)
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 40-42
    sprite('rrb404_10', 3)	# 43-45
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 46-48
    sprite('rrb404_12', 9)	# 49-57
    sprite('rrb404_08', 3)	# 58-60
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotB', 0)
    tag_voice(0, 'rrb208_1', 'rrb208_2', 'rrb208_0', '')
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 61-63
    sprite('rrb404_10', 3)	# 64-66
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 67-69
    sprite('rrb404_12', 9)	# 70-78
    sprite('rrb404_13', 3)	# 79-81
    sprite('rrb404_14', 3)	# 82-84
    sprite('rrb404_15', 3)	# 85-87
    GFX_0('rrb404EndEff', 0)
    SFX_3('rrbse_13')
    sprite('rrb404_16', 3)	# 88-90
    sprite('rrb404_17', 3)	# 91-93
    sprite('rrb404_18', 3)	# 94-96
    sprite('rrb404_19', 3)	# 97-99

@State
def AttackAndShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        AirUntechableTime(30)
        PushbackX(44800)
        Unknown30065(0)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
    sprite('rrb404_00', 3)	# 1-3
    sprite('rrb404_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rrb404_02', 3)	# 7-9
    GFX_0('rrb404Eff', 0)
    SFX_3('rrbse_13')
    tag_voice(1, 'rrb207_1', 'rrb207_2', '', '')
    sprite('rrb404_03', 3)	# 10-12
    sprite('rrb404_04', 4)	# 13-16	 **attackbox here**
    Unknown8004(0, 1, 1)
    Unknown1084(1)
    sprite('rrb404_05', 4)	# 17-20
    sprite('rrb404_06', 4)	# 21-24
    sprite('rrb404_07', 4)	# 25-28
    sprite('rrb404_08', 3)	# 29-31
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotEx', 0)
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 32-34
    sprite('rrb404_10', 3)	# 35-37
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 38-40
    sprite('rrb404_12', 9)	# 41-49
    sprite('rrb404_08', 3)	# 50-52
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotEx', 0)
    tag_voice(0, 'rrb208_1', 'rrb208_2', '', '')
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 53-55
    sprite('rrb404_10', 3)	# 56-58
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 59-61
    sprite('rrb404_12', 9)	# 62-70
    sprite('rrb404_08', 3)	# 71-73
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotEx', 0)
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 74-76
    sprite('rrb404_10', 3)	# 77-79
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 80-82
    sprite('rrb404_12', 9)	# 83-91
    sprite('rrb404_08', 3)	# 92-94
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('RifleShotEx', 0)
    ScreenShake(9000, 3000)
    sprite('rrb404_09', 3)	# 95-97
    sprite('rrb404_10', 3)	# 98-100
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb404_11', 3)	# 101-103
    sprite('rrb404_12', 6)	# 104-109
    sprite('rrb404_13', 3)	# 110-112
    sprite('rrb404_14', 3)	# 113-115
    sprite('rrb404_15', 3)	# 116-118
    GFX_0('rrb404EndEff', 0)
    SFX_3('rrbse_13')
    sprite('rrb404_16', 3)	# 119-121
    sprite('rrb404_17', 3)	# 122-124
    sprite('rrb404_18', 3)	# 125-127
    sprite('rrb404_19', 3)	# 128-130

@State
def AirRolling_A():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(200)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(-20000)
        AirUntechableTime(30)
        Unknown9310(1)
        Hitstop(2)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown30055('400d03003200000000000000')
        Unknown11068(1)
        clearUponHandler(2)
    sprite('rrb408_00', 3)	# 1-3
    sprite('rrb408_01', 3)	# 4-6
    physicsXImpulse(5000)
    physicsYImpulse(20000)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('rrb408_02', 3)	# 7-9
    sprite('rrb408_03', 3)	# 10-12
    SFX_3('rrbse_04')
    sprite('rrb408_04', 3)	# 13-15
    GFX_0('rrb408PetalEff', 0)
    Unknown7006('rrb213_1', 100, 845312626, 845099825, 0, 0, 100, 845312626, 811545393, 0, 0, 100, 0, 0, 0, 0, 0)
    label(0)
    sprite('rrb408_05', 4)	# 16-19	 **attackbox here**
    RefreshMultihit()
    GFX_0('rrb408Eff', 0)
    SFX_3('rrbse_12')
    sprite('rrb408_06', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('rrb408_07', 4)	# 24-27	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rrb409_00', 4)	# 28-31	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1300)
    AttackP2(80)
    GroundedHitstunAnimation(9)
    Hitstop(12)
    Unknown1084(1)
    Unknown2006()
    Unknown8004(0, 1, 1)
    GFX_0('rrb409Eff', 0)
    Unknown26('rrb408PetalEff')
    Unknown26('rrb408Eff')
    Unknown30068(1)
    callSubroutine('SpDash_Hasei')
    callSubroutine('SpDash_ShotHIT')
    sprite('rrb409_01', 4)	# 32-35
    sprite('rrb409_02', 4)	# 36-39
    sprite('rrb409_03', 4)	# 40-43
    Unknown7007('7272623231355f310000000000000000640000007272623231355f320000000000000000640000007272623231355f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('rrb409_04', 6)	# 44-49
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('AirRollingShot', 0)
    GFX_0('rrbCaseEff', 1)
    SFX_3('rrbse_01')
    ScreenShake(9000, 3000)
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    Unknown1043()
    sendToLabelUpon(2, 99)
    sprite('rrb409_05', 6)	# 50-55
    sprite('rrb409_06', 6)	# 56-61
    sprite('rrb409_07', 32767)	# 62-32828
    label(99)
    sprite('rrb409_08', 3)	# 32829-32831
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rrb409_09', 3)	# 32832-32834

@State
def AirRolling_B():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(220)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(-20000)
        AirUntechableTime(30)
        Unknown9310(1)
        Hitstop(2)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown30055('400d03003200000000000000')
        Unknown11068(1)
        clearUponHandler(2)
    sprite('rrb408_00', 3)	# 1-3
    sprite('rrb408_01', 3)	# 4-6
    physicsXImpulse(5000)
    physicsYImpulse(22000)
    Unknown1028(400)
    Unknown1043()
    sendToLabelUpon(2, 9)
    sprite('rrb408_02', 3)	# 7-9
    sprite('rrb408_03', 3)	# 10-12
    SFX_3('rrbse_04')
    sprite('rrb408_04', 3)	# 13-15
    GFX_0('rrb408PetalEff', 0)
    Unknown7006('rrb213_1', 100, 845312626, 845099825, 0, 0, 100, 845312626, 811545393, 0, 0, 100, 0, 0, 0, 0, 0)
    label(0)
    sprite('rrb408_05', 4)	# 16-19	 **attackbox here**
    RefreshMultihit()
    GFX_0('rrb408Eff', 0)
    SFX_3('rrbse_12')
    sprite('rrb408_06', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('rrb408_07', 4)	# 24-27	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rrb409_00', 4)	# 28-31	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1300)
    AttackP2(80)
    GroundedHitstunAnimation(9)
    Hitstop(12)
    Unknown1084(1)
    Unknown2006()
    Unknown8004(0, 1, 1)
    GFX_0('rrb409Eff', 0)
    Unknown26('rrb408PetalEff')
    Unknown26('rrb408Eff')
    Unknown30068(1)
    callSubroutine('SpDash_Hasei')
    callSubroutine('SpDash_ShotHIT')
    sprite('rrb409_01', 4)	# 32-35
    sprite('rrb409_02', 4)	# 36-39
    sprite('rrb409_03', 4)	# 40-43
    Unknown7007('7272623231355f310000000000000000640000007272623231355f320000000000000000640000007272623231355f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('rrb409_04', 6)	# 44-49
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('AirRollingShot', 0)
    GFX_0('rrbCaseEff', 1)
    SFX_3('rrbse_01')
    ScreenShake(9000, 3000)
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    Unknown1043()
    sendToLabelUpon(2, 99)
    sprite('rrb409_05', 6)	# 50-55
    sprite('rrb409_06', 6)	# 56-61
    sprite('rrb409_07', 32767)	# 62-32828
    label(99)
    sprite('rrb409_08', 3)	# 32829-32831
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rrb409_09', 3)	# 32832-32834

@State
def AirRolling_Ex():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(280)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(-20000)
        AirUntechableTime(30)
        Unknown9310(1)
        Hitstop(2)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown30055('400d03003200000000000000')
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11068(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)
    sprite('rrb408_00', 3)	# 1-3
    Unknown1084(1)
    sprite('rrb408_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    physicsXImpulse(5000)
    physicsYImpulse(20000)
    Unknown1028(400)
    Unknown1043()
    sprite('rrb408_02', 3)	# 7-9
    sprite('rrb408_03', 3)	# 10-12
    SFX_3('rrbse_04')
    sprite('rrb408_04', 3)	# 13-15
    GFX_0('rrb408PetalEff', 0)
    Unknown7006('rrb214_1', 100, 845312626, 845100081, 0, 0, 100, 845312626, 811545649, 0, 0, 100, 0, 0, 0, 0, 0)
    label(0)
    sprite('rrb408_05', 4)	# 16-19	 **attackbox here**
    RefreshMultihit()
    GFX_0('rrb408Eff', 0)
    SFX_3('rrbse_12')
    sprite('rrb408_06', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('rrb408_07', 4)	# 24-27	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rrb409_00', 4)	# 28-31	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1300)
    AttackP2(80)
    GroundedHitstunAnimation(9)
    Hitstop(12)
    Unknown1084(1)
    Unknown2006()
    Unknown8004(0, 1, 1)
    GFX_0('rrb409Eff', 0)
    Unknown26('rrb408PetalEff')
    Unknown26('rrb408Eff')
    Unknown30068(1)
    callSubroutine('SpDash_Hasei')
    callSubroutine('SpDash_ShotHIT')
    sprite('rrb409_01', 4)	# 32-35
    sprite('rrb409_02', 4)	# 36-39
    sprite('rrb409_03', 4)	# 40-43
    Unknown7007('7272623231355f310000000000000000640000007272623231355f320000000000000000640000007272623231355f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('rrb409_04', 6)	# 44-49
    GFX_0('rrb404MuzzleEff', 0)
    GFX_0('AirRollingShotEx', 0)
    GFX_0('rrbCaseEff', 1)
    SFX_3('rrbse_01')
    ScreenShake(9000, 3000)
    physicsXImpulse(-10000)
    physicsYImpulse(12000)
    Unknown1043()
    sendToLabelUpon(2, 99)
    sprite('rrb409_05', 6)	# 50-55
    sprite('rrb409_06', 6)	# 56-61
    sprite('rrb409_07', 32767)	# 62-32828
    label(99)
    sprite('rrb409_08', 3)	# 32829-32831
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rrb409_09', 3)	# 32832-32834

@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('SpDash_ShotHIT')
    sprite('rrb407_00', 3)	# 1-3
    sprite('rrb407_01', 3)	# 4-6
    sprite('rrb407_02', 4)	# 7-10
    Unknown7007('7272623231325f310000000000000000640000007272623231325f320000000000000000640000007272623231325f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('rrb407_03', 4)	# 11-14
    GFX_0('rrb407MuzzleEff', 0)
    GFX_0('ShotAtk', 0)
    ScreenShake(9000, 3000)
    sprite('rrb407_04', 4)	# 15-18
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb407_05', 8)	# 19-26
    sprite('rrb407_06', 4)	# 27-30
    sprite('rrb601_03', 4)	# 31-34
    GFX_0('rrb407EndEff', 0)
    sprite('rrb601_04', 4)	# 35-38
    sprite('rrb601_05', 4)	# 39-42
    sprite('rrb601_06', 4)	# 43-46
    sprite('rrb601_07', 4)	# 47-50
    sprite('rrb601_08', 4)	# 51-54

@State
def MultiAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(800)
        AttackP1(80)
        Unknown11092(1)
        AirPushbackY(12000)
        AirUntechableTime(40)
        Hitstop(7)
        Unknown11001(5, 5, 10)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        Unknown30065(0)
        MinimumDamagePct(10)
        sendToLabelUpon(2, 9)
        callSubroutine('SpDash_Hasei')
        callSubroutine('SpDash_ShotHIT')
    sprite('rrb406_00', 2)	# 1-2
    teleportRelativeX(30000)
    sprite('rrb406_01', 1)	# 3-3
    teleportRelativeX(30000)
    sprite('rrb406_01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('rrb406_02', 2)	# 5-6
    GFX_0('rrb406aEff', 0)
    teleportRelativeX(50000)
    tag_voice(1, 'rrb210_1', 'rrb210_2', 'rrb210_0', '')
    SFX_3('rrbse_03')
    sprite('rrb406_03', 4)	# 7-10	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(10000)
    sprite('rrb406_04', 2)	# 11-12
    teleportRelativeX(20000)
    sprite('rrb406_05', 2)	# 13-14
    teleportRelativeX(20000)
    sprite('rrb406_06', 2)	# 15-16
    teleportRelativeX(20000)
    SFX_3('rrbse_03')
    sprite('rrb406_07', 2)	# 17-18
    teleportRelativeX(30000)
    sprite('rrb406_08', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    GFX_0('rrb406bEff', 0)
    teleportRelativeX(10000)
    sprite('rrb406_09', 3)	# 22-24
    sprite('rrb406_10', 3)	# 25-27
    sprite('rrb406_11', 3)	# 28-30
    sprite('rrb406_12', 3)	# 31-33	 **attackbox here**
    StartMultihit()
    sprite('rrb406_13', 3)	# 34-36
    sprite('rrb406_14', 3)	# 37-39
    GFX_0('rrb406MuzzleEff', 0)
    GFX_0('RollingShot', 0)
    tag_voice(0, 'rrb211_1', '', 'rrb211_2', '')
    sprite('rrb406_15', 2)	# 40-41	 **attackbox here**
    GFX_0('rrb406cEff', 0)
    RefreshMultihit()
    Damage(400)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    Unknown9083()
    Unknown9016(1)
    Unknown9015(0)
    Unknown9215()
    Hitstop(3)
    physicsYImpulse(20000)
    Unknown1043()
    SFX_3('rrbse_05')
    sprite('rrb406_15', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    sprite('rrb406_16', 2)	# 44-45	 **attackbox here**
    RefreshMultihit()
    sprite('rrb406_16', 2)	# 46-47	 **attackbox here**
    RefreshMultihit()
    sprite('rrb406_17', 6)	# 48-53
    Recovery()
    SFX_3('rrbse_01')
    sprite('rrb406_18', 6)	# 54-59
    sprite('rrb406_19', 32767)	# 60-32826
    label(9)
    sprite('rrb406_20', 3)	# 32827-32829
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rrb406_21', 3)	# 32830-32832
    sprite('rrb406_22', 3)	# 32833-32835
    sprite('rrb406_23', 3)	# 32836-32838

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2000)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        Unknown11001(0, 40, 40)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateAssault_AddAtk')
        Unknown2073(1)
        Unknown1084(1)

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(1)
            teleportRelativeY(0)
            Unknown2015(40)
            DisableAttackRestOfMove()
            setInvincible(1)
            Unknown3001(200)
            Unknown3004(-20)
            Unknown13024(0)
            sendToLabel(0)
            Unknown21012('727262343331456666000000000000000000000000000000000000000000000021000000')
            GFX_0('rrb431Hit', 22)

        def upon_43():
            if (SLOT_48 == 4311):
                Unknown13024(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2005()
            Unknown2015(-1)
            EnableCollision(1)
    sprite('rrb431_00', 4)	# 1-4
    setInvincible(1)
    sprite('rrb431_01', 20)	# 5-24
    Unknown2036(72, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown20000(1)
    tag_voice(1, 'rrb253_1', 'rrb253_2', 'rrb253_0', '')
    sprite('rrb431_02', 8)	# 25-32
    sprite('rrb431_03', 24)	# 33-56
    GFX_0('rrb431Eff', 0)
    sprite('rrb431_04', 8)	# 57-64
    SFX_3('rrbse_08')
    sprite('rrb431_05', 3)	# 65-67
    physicsXImpulse(4000)
    physicsYImpulse(4000)
    setGravity(0)
    SFX_0('000_airdash_1')
    Unknown20000(0)
    SFX_3('rrbse_09')
    sprite('rrb431_06', 3)	# 68-70
    sprite('rrb431_07', 3)	# 71-73
    sprite('rrb431_08', 3)	# 74-76	 **attackbox here**
    DisableAttackRestOfMove()
    physicsYImpulse(0)
    Unknown1028(1000)
    SFX_0('000_airdash_1')
    tag_voice(0, 'rrb254_1', 'rrb254_2', 'rrb254_0', '')
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000023000000')
    sprite('rrb431_09', 3)	# 77-79	 **attackbox here**
    sprite('rrb431_10', 3)	# 80-82	 **attackbox here**
    sprite('rrb431_08', 2)	# 83-84	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 85-86	 **attackbox here**
    sprite('rrb431_10', 2)	# 87-88	 **attackbox here**
    sprite('rrb431_08', 2)	# 89-90	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    physicsXImpulse(80000)
    EnableCollision(0)
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 91-92	 **attackbox here**
    sprite('rrb431_10', 2)	# 93-94	 **attackbox here**
    sprite('rrb431_08', 2)	# 95-96	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 97-98	 **attackbox here**
    sprite('rrb431_10', 2)	# 99-100	 **attackbox here**
    sprite('rrb431_11', 4)	# 101-104
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000020000000')
    teleportRelativeY(25000)
    Unknown1043()
    physicsXImpulse(15000)
    setInvincible(0)
    EnableCollision(1)
    Unknown2015(-1)
    sprite('rrb431_12', 4)	# 105-108
    sprite('rrb431_13', 4)	# 109-112
    Unknown8000(100, 1, 1)
    physicsXImpulse(30000)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    sprite('rrb431_14', 3)	# 113-115
    sprite('rrb431_15', 3)	# 116-118
    sprite('rrb431_16', 3)	# 119-121
    sprite('rrb431_14', 3)	# 122-124
    sprite('rrb431_15', 3)	# 125-127
    sprite('rrb431_16', 3)	# 128-130
    sprite('rrb431_14', 3)	# 131-133
    sprite('rrb431_15', 3)	# 134-136
    sprite('rrb431_16', 3)	# 137-139
    sprite('rrb431_17', 4)	# 140-143
    Unknown1019(0)
    clearUponHandler(3)
    sprite('rrb431_18', 3)	# 144-146
    ExitState()
    label(0)
    sprite('rrb431_08', 2)	# 147-148	 **attackbox here**
    Unknown1019(30)
    sprite('rrb431_09', 2)	# 149-150	 **attackbox here**
    sprite('rrb431_10', 2)	# 151-152	 **attackbox here**
    sprite('rrb431_08', 2)	# 153-154	 **attackbox here**
    sprite('rrb431_09', 2)	# 155-156	 **attackbox here**
    sprite('rrb431_10', 2)	# 157-158	 **attackbox here**
    sprite('rrb431_08', 1)	# 159-159	 **attackbox here**
    sprite('rrb431_09', 1)	# 160-160	 **attackbox here**
    sprite('rrb431_10', 1)	# 161-161	 **attackbox here**
    sprite('rrb431_08', 1)	# 162-162	 **attackbox here**
    sprite('rrb431_09', 1)	# 163-163	 **attackbox here**
    sprite('rrb431_10', 1)	# 164-164	 **attackbox here**
    sprite('rrb431_11', 4)	# 165-168
    Unknown1086(22)
    teleportRelativeX(300000)
    teleportRelativeY(25000)
    physicsXImpulse(30000)
    Unknown3001(128)
    Unknown3004(20)
    setGravity(1000)
    sprite('rrb431_12', 4)	# 169-172
    sprite('rrb431_13', 4)	# 173-176
    Unknown8000(100, 1, 1)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    Unknown2015(150)
    EnableCollision(1)
    sprite('rrb431_14', 2)	# 177-178
    sprite('rrb431_15', 2)	# 179-180
    sprite('rrb431_16', 2)	# 181-182
    GFX_0('UltimateAssault_AddAtk', -1)
    sprite('rrb431_14', 2)	# 183-184
    sprite('rrb431_15', 2)	# 185-186
    sprite('rrb431_16', 2)	# 187-188
    sprite('rrb431_14', 2)	# 189-190
    sprite('rrb431_15', 2)	# 191-192
    sprite('rrb431_16', 2)	# 193-194
    sprite('rrb431_14', 2)	# 195-196
    sprite('rrb431_15', 2)	# 197-198
    sprite('rrb431_16', 2)	# 199-200
    sprite('rrb431_14', 2)	# 201-202
    sprite('rrb431_15', 2)	# 203-204
    sprite('rrb431_16', 2)	# 205-206
    sprite('rrb431_14', 2)	# 207-208
    sprite('rrb431_15', 2)	# 209-210
    sprite('rrb431_16', 2)	# 211-212
    sprite('rrb431_14', 2)	# 213-214
    sprite('rrb431_15', 2)	# 215-216
    sprite('rrb431_16', 2)	# 217-218
    sprite('rrb431_14', 2)	# 219-220
    sprite('rrb431_15', 2)	# 221-222
    sprite('rrb431_16', 2)	# 223-224
    sprite('rrb431_14', 4)	# 225-228
    sprite('rrb431_15', 4)	# 229-232
    sprite('rrb431_16', 4)	# 233-236
    sprite('rrb431_14', 4)	# 237-240
    sprite('rrb431_15', 4)	# 241-244
    sprite('rrb431_16', 4)	# 245-248
    sprite('rrb431_17', 4)	# 249-252
    Unknown1019(0)
    clearUponHandler(3)
    Unknown2015(-1)
    sprite('rrb431_18', 4)	# 253-256
    sprite('rrb003_00', 3)	# 257-259
    sprite('rrb003_01', 3)	# 260-262
    sprite('rrb601_04', 6)	# 263-268
    sprite('rrb601_05', 6)	# 269-274
    sprite('rrb601_06', 6)	# 275-280
    sprite('rrb601_07', 6)	# 281-286
    sprite('rrb601_08', 6)	# 287-292

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2000)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        Unknown11001(0, 40, 40)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateAssaultOD_AddAtk')
        Unknown9001(5)
        Unknown2073(1)
        Unknown1084(1)

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(1)
            teleportRelativeY(0)
            Unknown2015(40)
            DisableAttackRestOfMove()
            setInvincible(1)
            Unknown3001(200)
            Unknown3004(-20)
            Unknown13024(0)
            sendToLabel(0)
            Unknown21012('727262343331456666000000000000000000000000000000000000000000000021000000')
            GFX_0('rrb431Hit', 22)

        def upon_43():
            if (SLOT_48 == 4311):
                Unknown13024(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2005()
            Unknown2015(-1)
            EnableCollision(1)
    sprite('rrb431_00', 4)	# 1-4
    setInvincible(1)
    sprite('rrb431_01', 20)	# 5-24
    Unknown2036(72, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown20000(1)
    tag_voice(1, 'rrb253_1', 'rrb253_2', 'rrb253_0', '')
    sprite('rrb431_02', 8)	# 25-32
    sprite('rrb431_03', 24)	# 33-56
    GFX_0('rrb431Eff', 0)
    sprite('rrb431_04', 8)	# 57-64
    SFX_3('rrbse_08')
    sprite('rrb431_05', 3)	# 65-67
    physicsXImpulse(4000)
    physicsYImpulse(4000)
    setGravity(0)
    SFX_0('000_airdash_1')
    Unknown20000(0)
    SFX_3('rrbse_09')
    sprite('rrb431_06', 3)	# 68-70
    sprite('rrb431_07', 3)	# 71-73
    sprite('rrb431_08', 3)	# 74-76	 **attackbox here**
    DisableAttackRestOfMove()
    physicsYImpulse(0)
    Unknown1028(1000)
    SFX_0('000_airdash_1')
    tag_voice(0, 'rrb254_1', 'rrb254_2', 'rrb254_0', '')
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000023000000')
    sprite('rrb431_09', 3)	# 77-79	 **attackbox here**
    sprite('rrb431_10', 3)	# 80-82	 **attackbox here**
    sprite('rrb431_08', 2)	# 83-84	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 85-86	 **attackbox here**
    sprite('rrb431_10', 2)	# 87-88	 **attackbox here**
    sprite('rrb431_08', 2)	# 89-90	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    physicsXImpulse(80000)
    EnableCollision(0)
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 91-92	 **attackbox here**
    sprite('rrb431_10', 2)	# 93-94	 **attackbox here**
    sprite('rrb431_08', 2)	# 95-96	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 97-98	 **attackbox here**
    sprite('rrb431_10', 2)	# 99-100	 **attackbox here**
    sprite('rrb431_11', 4)	# 101-104
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000020000000')
    teleportRelativeY(25000)
    Unknown1043()
    physicsXImpulse(15000)
    setInvincible(0)
    EnableCollision(1)
    Unknown2015(-1)
    sprite('rrb431_12', 4)	# 105-108
    sprite('rrb431_13', 4)	# 109-112
    Unknown8000(100, 1, 1)
    physicsXImpulse(30000)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    sprite('rrb431_14', 3)	# 113-115
    sprite('rrb431_15', 3)	# 116-118
    sprite('rrb431_16', 3)	# 119-121
    sprite('rrb431_14', 3)	# 122-124
    sprite('rrb431_15', 3)	# 125-127
    sprite('rrb431_16', 3)	# 128-130
    sprite('rrb431_14', 3)	# 131-133
    sprite('rrb431_15', 3)	# 134-136
    sprite('rrb431_16', 3)	# 137-139
    sprite('rrb431_17', 4)	# 140-143
    Unknown1019(0)
    clearUponHandler(3)
    sprite('rrb431_18', 3)	# 144-146
    ExitState()
    label(0)
    sprite('rrb431_08', 2)	# 147-148	 **attackbox here**
    Unknown1019(30)
    sprite('rrb431_09', 2)	# 149-150	 **attackbox here**
    sprite('rrb431_10', 2)	# 151-152	 **attackbox here**
    sprite('rrb431_08', 2)	# 153-154	 **attackbox here**
    sprite('rrb431_09', 2)	# 155-156	 **attackbox here**
    sprite('rrb431_10', 2)	# 157-158	 **attackbox here**
    sprite('rrb431_08', 1)	# 159-159	 **attackbox here**
    sprite('rrb431_09', 1)	# 160-160	 **attackbox here**
    sprite('rrb431_10', 1)	# 161-161	 **attackbox here**
    sprite('rrb431_08', 1)	# 162-162	 **attackbox here**
    sprite('rrb431_09', 1)	# 163-163	 **attackbox here**
    sprite('rrb431_10', 1)	# 164-164	 **attackbox here**
    sprite('rrb431_11', 4)	# 165-168
    Unknown1086(22)
    teleportRelativeX(300000)
    teleportRelativeY(25000)
    physicsXImpulse(30000)
    Unknown3001(128)
    Unknown3004(20)
    setGravity(1000)
    sprite('rrb431_12', 4)	# 169-172
    sprite('rrb431_13', 4)	# 173-176
    Unknown8000(100, 1, 1)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    Unknown2015(150)
    EnableCollision(1)
    sprite('rrb431_14', 2)	# 177-178
    sprite('rrb431_15', 2)	# 179-180
    sprite('rrb431_16', 2)	# 181-182
    GFX_0('UltimateAssaultOD_AddAtk', -1)
    sprite('rrb431_14', 2)	# 183-184
    sprite('rrb431_15', 2)	# 185-186
    sprite('rrb431_16', 2)	# 187-188
    sprite('rrb431_14', 2)	# 189-190
    sprite('rrb431_15', 2)	# 191-192
    sprite('rrb431_16', 2)	# 193-194
    sprite('rrb431_14', 2)	# 195-196
    sprite('rrb431_15', 2)	# 197-198
    sprite('rrb431_16', 2)	# 199-200
    sprite('rrb431_14', 2)	# 201-202
    sprite('rrb431_15', 2)	# 203-204
    sprite('rrb431_16', 2)	# 205-206
    sprite('rrb431_14', 2)	# 207-208
    sprite('rrb431_15', 2)	# 209-210
    sprite('rrb431_16', 2)	# 211-212
    sprite('rrb431_14', 2)	# 213-214
    sprite('rrb431_15', 2)	# 215-216
    sprite('rrb431_16', 2)	# 217-218
    sprite('rrb431_14', 2)	# 219-220
    sprite('rrb431_15', 2)	# 221-222
    sprite('rrb431_16', 2)	# 223-224
    sprite('rrb431_14', 4)	# 225-228
    sprite('rrb431_15', 4)	# 229-232
    sprite('rrb431_16', 4)	# 233-236
    sprite('rrb431_14', 4)	# 237-240
    sprite('rrb431_15', 4)	# 241-244
    sprite('rrb431_16', 4)	# 245-248
    sprite('rrb431_17', 4)	# 249-252
    Unknown1019(0)
    clearUponHandler(3)
    Unknown2015(-1)
    sprite('rrb431_18', 4)	# 253-256
    sprite('rrb003_00', 3)	# 257-259
    sprite('rrb003_01', 3)	# 260-262
    sprite('rrb601_04', 6)	# 263-268
    sprite('rrb601_05', 6)	# 269-274
    sprite('rrb601_06', 6)	# 275-280
    sprite('rrb601_07', 6)	# 281-286
    sprite('rrb601_08', 6)	# 287-292

@State
def UltimateDance():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1200)
        MinimumDamagePct(14)
        AttackP2(60)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(1200)
        AirUntechableTime(90)
        PushbackX(12000)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11056(0)
        Unknown11064(1)
        Hitstop(6)
        Unknown1084(1)

        def upon_78():
            Unknown2037(1)
            setInvincible(0)
            setInvincibleFor(60)
    sprite('rrb430_00', 4)	# 1-4
    setInvincible(1)
    Unknown1045(10000)
    sprite('rrb430_01', 4)	# 5-8
    sprite('rrb430_02', 4)	# 9-12
    sprite('rrb430_03', 50)	# 13-62
    tag_voice(1, 'rrb250_1', 'rrb250_2', 'rrb250_0', '')
    Unknown1084(1)
    Unknown2036(60, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('rrb430_04', 4)	# 63-66
    sprite('rrb430_05', 4)	# 67-70
    physicsXImpulse(8000)
    sprite('rrb430_06', 4)	# 71-74
    GFX_0('rrb430Eff', 0)
    Unknown1019(300)
    SFX_3('rrbse_05')
    sprite('rrb430_07', 4)	# 75-78	 **attackbox here**
    tag_voice(0, 'rrb251_1', 'rrb251_2', 'rrb251_0', '')
    Unknown1019(30)
    RefreshMultihit()
    sprite('rrb430_08', 4)	# 79-82	 **attackbox here**
    Unknown1084(1)
    sprite('rrb430_09', 4)	# 83-86
    if (not SLOT_2):
        setInvincible(0)
    teleportRelativeX(40000)
    SFX_3('rrbse_03')
    sprite('rrb430_10', 4)	# 87-90	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    sprite('rrb430_11', 3)	# 91-93
    teleportRelativeX(20000)
    sprite('rrb430_12', 3)	# 94-96
    teleportRelativeX(40000)
    SFX_3('rrbse_03')
    sprite('rrb430_13', 2)	# 97-98	 **attackbox here**
    teleportRelativeX(40000)
    Unknown1084(1)
    RefreshMultihit()
    AirPushbackX(2000)
    AirPushbackY(3000)
    Hitstop(2)
    PushbackX(0)
    sprite('rrb430_14', 2)	# 99-100
    sprite('rrb430_15', 3)	# 101-103
    SFX_3('rrbse_05')
    sprite('rrb430_16', 2)	# 104-105	 **attackbox here**
    RefreshMultihit()
    sprite('rrb430_17', 2)	# 106-107
    sprite('rrb430_19', 3)	# 108-110
    SFX_3('rrbse_05')
    sprite('rrb430_13', 2)	# 111-112	 **attackbox here**
    RefreshMultihit()
    sprite('rrb430_14', 2)	# 113-114
    sprite('rrb430_15', 3)	# 115-117
    Unknown13024(0)
    SFX_3('rrbse_05')
    sprite('rrb430_16', 2)	# 118-119	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirPushbackX(8000)
    AirPushbackY(32000)
    Unknown11072(1, 120000, 0)
    clearUponHandler(78)

    def upon_78():
        clearUponHandler(78)
        sendToLabel(0)
        Unknown11069('UltimateDance')
        Unknown2037(1)
        setInvincible(1)
    sprite('rrb430_17', 5)	# 120-124
    clearUponHandler(78)
    Unknown21012('727262343330456666000000000000000000000000000000000000000000000029000000')
    Unknown13024(1)
    sprite('rrb430_18', 5)	# 125-129
    sprite('rrb430_33', 5)	# 130-134
    sprite('rrb430_34', 5)	# 135-139
    SFX_3('rrbse_04')
    sprite('rrb312_02', 5)	# 140-144	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    Hitstop(12)
    Unknown9215()
    Unknown11064(0)
    GFX_0('rrb312Eff', 0)
    sprite('rrb312_03', 5)	# 145-149
    sprite('rrb312_04', 5)	# 150-154
    sprite('rrb312_05', 5)	# 155-159
    SFX_3('rrbse_01')
    sprite('rrb312_06', 5)	# 160-164
    sprite('rrb312_07', 5)	# 165-169
    sprite('rrb312_08', 5)	# 170-174
    ExitState()
    label(0)
    sprite('keep', 2)	# 175-176
    Unknown20000(1)
    Unknown21012('727262343330456666000000000000000000000000000000000000000000000020000000')
    sprite('rrb430_17', 3)	# 177-179
    SFX_3('rrbse_01')
    sprite('rrb430_18', 3)	# 180-182
    sprite('rrb430_20', 3)	# 183-185
    physicsXImpulse(3000)
    Unknown23024(2)
    Unknown2015(200)
    sprite('rrb430_21', 3)	# 186-188
    Unknown1019(300)
    Unknown2015(400)
    sprite('rrb430_22', 5)	# 189-193
    Unknown1019(400)
    Unknown2015(600)
    sprite('rrb430_23', 5)	# 194-198
    Unknown1019(10)
    Unknown2015(700)
    sprite('rrb430_24', 6)	# 199-204
    Unknown1084(1)
    Unknown2015(800)
    sprite('rrb430_25', 6)	# 205-210
    sprite('rrb430_26', 6)	# 211-216
    sprite('rrb430_27', 6)	# 217-222
    SFX_3('rrbse_07')
    sprite('rrb430_28', 4)	# 223-226	 **attackbox here**
    tag_voice(0, 'rrb252_1', 'rrb252_2', 'rrb252_0', '')
    Unknown2015(-1)
    RefreshMultihit()
    Damage(4700)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(2000)
    Unknown9083()
    Unknown9095()
    Hitstop(30)
    ScreenShake(32000, 32000)
    Unknown11064(0)
    Unknown11072(0, 120000, 0)
    Unknown21012('727262343330456666000000000000000000000000000000000000000000000021000000')
    Unknown11069('')
    sprite('rrb430_29', 7)	# 227-233
    sprite('rrb430_30', 8)	# 234-241
    sprite('rrb430_31', 12)	# 242-253
    Unknown20000(0)
    Unknown23024(1)
    Unknown13024(1)
    sprite('rrb430_32', 4)	# 254-257
    sprite('rrb404_14', 4)	# 258-261
    sprite('rrb404_15', 4)	# 262-265
    sprite('rrb404_16', 4)	# 266-269
    sprite('rrb404_17', 4)	# 270-273
    sprite('rrb404_18', 4)	# 274-277
    sprite('rrb404_19', 4)	# 278-281

@State
def UltimateDanceOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1200)
        MinimumDamagePct(13)
        AttackP2(60)
        Unknown11092(1)
        AirPushbackX(10000)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(1200)
        AirUntechableTime(90)
        PushbackX(12000)
        Hitstop(6)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11056(0)
        Unknown11064(1)

        def upon_78():
            Unknown4047(9, 9, 9)
            Unknown4045('72726265663433305f6869745f706574616c000000000000000000000000000066000000')
            Unknown2037(1)
            setInvincible(0)
            setInvincibleFor(60)
        Unknown1084(1)
    sprite('rrb430_00', 4)	# 1-4
    setInvincible(1)
    Unknown1045(10000)
    sprite('rrb430_01', 4)	# 5-8
    sprite('rrb430_02', 4)	# 9-12
    sprite('rrb430_03', 50)	# 13-62
    tag_voice(1, 'rrb250_1', 'rrb250_2', 'rrb250_0', '')
    Unknown1084(1)
    Unknown2036(60, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('rrb430_04', 4)	# 63-66
    sprite('rrb430_05', 4)	# 67-70
    physicsXImpulse(8000)
    sprite('rrb430_06', 4)	# 71-74
    GFX_0('rrb430EffOD', 0)
    Unknown1019(300)
    SFX_3('rrbse_05')
    sprite('rrb430_07', 4)	# 75-78	 **attackbox here**
    tag_voice(0, 'rrb251_1', 'rrb251_2', 'rrb251_0', '')
    Unknown1019(30)
    RefreshMultihit()
    sprite('rrb430_08', 4)	# 79-82	 **attackbox here**
    Unknown1084(1)
    sprite('rrb430_09', 4)	# 83-86
    if (not SLOT_2):
        setInvincible(0)
    teleportRelativeX(40000)
    SFX_3('rrbse_03')
    sprite('rrb430_10', 4)	# 87-90	 **attackbox here**
    teleportRelativeX(20000)
    RefreshMultihit()
    sprite('rrb430_11', 3)	# 91-93
    teleportRelativeX(20000)
    sprite('rrb430_12', 3)	# 94-96
    teleportRelativeX(40000)
    SFX_3('rrbse_03')
    sprite('rrb430_13', 2)	# 97-98	 **attackbox here**
    teleportRelativeX(40000)
    Unknown1084(1)
    RefreshMultihit()
    Damage(1000)
    AirPushbackX(500)
    AirPushbackY(3000)
    Hitstop(2)
    PushbackX(0)
    sprite('rrb430_14', 2)	# 99-100
    sprite('rrb430_15', 3)	# 101-103
    SFX_3('rrbse_05')
    sprite('rrb430_16', 2)	# 104-105	 **attackbox here**
    RefreshMultihit()
    sprite('rrb430_17', 2)	# 106-107
    sprite('rrb430_19', 3)	# 108-110
    SFX_3('rrbse_05')
    sprite('rrb430_13', 2)	# 111-112	 **attackbox here**
    RefreshMultihit()
    Hitstop(1)
    sprite('rrb430_14', 2)	# 113-114
    sprite('rrb430_15', 3)	# 115-117
    SFX_3('rrbse_05')
    sprite('rrb430_16', 2)	# 118-119	 **attackbox here**
    RefreshMultihit()
    sprite('rrb430_17', 2)	# 120-121
    sprite('rrb430_19', 3)	# 122-124
    SFX_3('rrbse_05')
    sprite('rrb430_13', 2)	# 125-126	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    sprite('rrb430_14', 2)	# 127-128
    sprite('rrb430_15', 3)	# 129-131
    SFX_3('rrbse_05')
    sprite('rrb430_16', 2)	# 132-133	 **attackbox here**
    RefreshMultihit()
    sprite('rrb430_17', 2)	# 134-135
    sprite('rrb430_19', 3)	# 136-138
    SFX_3('rrbse_05')
    sprite('rrb430_13', 2)	# 139-140	 **attackbox here**
    RefreshMultihit()
    sprite('rrb430_14', 2)	# 141-142
    sprite('rrb430_15', 3)	# 143-145
    Unknown13024(0)
    SFX_3('rrbse_05')
    sprite('rrb430_16', 2)	# 146-147	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirPushbackX(8000)
    AirPushbackY(42000)
    Unknown11072(1, 120000, 0)
    clearUponHandler(78)

    def upon_78():
        clearUponHandler(78)
        sendToLabel(0)
        Unknown11069('UltimateDanceOD')
        Unknown2037(1)
        setInvincible(1)
    sprite('rrb430_17', 5)	# 148-152
    clearUponHandler(78)
    Unknown21012('7272623433304566664f4400000000000000000000000000000000000000000029000000')
    Unknown13024(1)
    sprite('rrb430_18', 5)	# 153-157
    sprite('rrb430_33', 5)	# 158-162
    sprite('rrb430_34', 5)	# 163-167
    SFX_3('rrbse_04')
    sprite('rrb312_02', 5)	# 168-172	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    Hitstop(12)
    Unknown9215()
    Unknown11064(0)
    GFX_0('rrb312Eff', 0)
    sprite('rrb312_03', 5)	# 173-177
    sprite('rrb312_04', 5)	# 178-182
    sprite('rrb312_05', 5)	# 183-187
    SFX_3('rrbse_01')
    sprite('rrb312_06', 5)	# 188-192
    sprite('rrb312_07', 5)	# 193-197
    sprite('rrb312_08', 5)	# 198-202
    ExitState()
    label(0)
    sprite('keep', 2)	# 203-204
    Unknown21012('7272623433304566664f4400000000000000000000000000000000000000000020000000')
    Unknown20000(1)
    sprite('rrb430_17', 5)	# 205-209
    sprite('rrb430_18', 5)	# 210-214
    sprite('rrb430_20', 5)	# 215-219
    physicsXImpulse(3000)
    Unknown23024(2)
    Unknown2015(200)
    sprite('rrb430_21', 5)	# 220-224
    Unknown1019(300)
    Unknown2015(400)
    sprite('rrb430_22', 5)	# 225-229
    Unknown1019(400)
    Unknown2015(600)
    sprite('rrb430_23', 5)	# 230-234
    Unknown1019(10)
    Unknown2015(700)
    sprite('rrb430_24', 9)	# 235-243
    Unknown1084(1)
    Unknown2015(800)
    sprite('rrb430_25', 9)	# 244-252
    sprite('rrb430_26', 9)	# 253-261
    sprite('rrb430_27', 9)	# 262-270
    SFX_3('rrbse_07')
    sprite('rrb430_28', 4)	# 271-274	 **attackbox here**
    tag_voice(0, 'rrb252_1', 'rrb252_2', 'rrb252_0', '')
    Unknown2015(-1)
    RefreshMultihit()
    Damage(4100)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(2000)
    Unknown9083()
    Unknown9095()
    Hitstop(60)
    ScreenShake(32000, 32000)
    Unknown11064(0)
    Unknown11072(0, 120000, 0)
    Unknown21012('7272623433304566664f4400000000000000000000000000000000000000000021000000')
    Unknown11069('')
    sprite('rrb430_29', 5)	# 275-279
    sprite('rrb430_30', 5)	# 280-284
    sprite('rrb430_31', 12)	# 285-296
    Unknown20000(0)
    Unknown23024(1)
    Unknown13024(1)
    sprite('rrb430_32', 4)	# 297-300
    sprite('rrb404_14', 4)	# 301-304
    sprite('rrb404_15', 4)	# 305-308
    sprite('rrb404_16', 4)	# 309-312
    sprite('rrb404_17', 4)	# 313-316
    sprite('rrb404_18', 4)	# 317-320
    sprite('rrb404_19', 4)	# 321-324

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(9999)
        Unknown9142(9999)
        AirUntechableTime(9999)
        Unknown11086(1)
        Unknown11064(1)
        Unknown11067(1)
        setInvincible(1)
        Unknown2004(1, 1)
        sendToLabelUpon(2, 0)
        Unknown2037(0)

        def upon_78():
            clearUponHandler(78)
            Unknown23157(1)
            EnableCollision(0)
            Unknown2053(0)
            Unknown2034(0)
            Unknown20000(1)
            Unknown20003(1)
            Unknown20004(1)
            Unknown23084(1)
            Unknown2037(1)
    sprite('rrb450_00', 3)	# 1-3
    Unknown2036(60, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    tag_voice(1, 'rrb290_1', 'rrb290_2', 'rrb290_0', '')
    sprite('rrb450_01', 3)	# 4-6
    GFX_0('rrb450', -1)
    sprite('rrb450_02', 3)	# 7-9
    sprite('rrb450_03', 3)	# 10-12
    sprite('rrb450_01', 3)	# 13-15
    sprite('rrb450_02', 3)	# 16-18
    sprite('rrb450_03', 3)	# 19-21
    sprite('rrb450_01', 3)	# 22-24
    sprite('rrb450_02', 3)	# 25-27
    sprite('rrb450_03', 3)	# 28-30
    sprite('rrb450_01', 3)	# 31-33
    sprite('rrb450_02', 3)	# 34-36
    sprite('rrb450_03', 3)	# 37-39
    sprite('rrb450_01', 3)	# 40-42
    sprite('rrb450_02', 3)	# 43-45
    sprite('rrb450_03', 3)	# 46-48
    sprite('rrb450_01', 3)	# 49-51
    sprite('rrb450_02', 3)	# 52-54
    sprite('rrb450_03', 3)	# 55-57
    sprite('rrb450_04', 3)	# 58-60
    Unknown23087(200000)
    teleportRelativeX(40000)
    sprite('rrb450_05', 3)	# 61-63
    sprite('rrb450_06', 3)	# 64-66
    sprite('rrb450_07', 3)	# 67-69
    sprite('rrb450_08', 3)	# 70-72
    sprite('rrb450_09', 3)	# 73-75
    sprite('rrb450_10', 32767)	# 76-32842	 **attackbox here**
    teleportRelativeY(120000)
    physicsXImpulse(45000)
    physicsYImpulse(-30000)
    label(0)
    sprite('rrb450_11', 6)	# 32843-32848
    if (not SLOT_2):
        setInvincible(0)
    Unknown8000(100, 1, 1)
    Unknown1019(30)
    sprite('rrb450_12', 3)	# 32849-32851
    Unknown1019(30)
    sprite('rrb450_12', 3)	# 32852-32854
    Unknown1084(1)
    if SLOT_2:
        _gotolabel(100)
    sprite('rrb450_29', 3)	# 32855-32857
    sprite('rrb450_30', 3)	# 32858-32860
    sprite('rrb450_31', 30)	# 32861-32890
    sprite('rrb064_01', 6)	# 32891-32896
    sprite('rrb064_02', 6)	# 32897-32902
    sprite('rrb064_03', 6)	# 32903-32908
    sprite('rrb064_04', 6)	# 32909-32914
    Unknown21012('727262343530000000000000000000000000000000000000000000000000000029000000')
    loopRest()
    ExitState()
    label(100)
    sprite('rrb450_13', 6)	# 32915-32920
    sprite('rrb450_14', 6)	# 32921-32926
    sprite('rrb450_15', 6)	# 32927-32932
    Unknown21012('727262343530000000000000000000000000000000000000000000000000000020000000')
    SFX_3('rrbse_02')
    sprite('rrb450_16', 6)	# 32933-32938	 **attackbox here**
    RefreshMultihit()
    Damage(0)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(0)
    AirPushbackY(1)
    YImpluseBeforeWallbounce(0)
    Hitstop(0)
    Unknown11023(1)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown36(22)
    Unknown3001(0)
    Unknown35()
    Unknown23088(1, 1)
    SFX_3('rrbse_08')
    sprite('null', 30)	# 32939-32968
    sprite('rrb450_17', 3)	# 32969-32971
    tag_voice(0, 'rrb291_1', 'rrb291_2', 'rrb291_0', '')
    Unknown23024(3)
    Unknown1000(0)
    teleportRelativeY(1000000)
    Unknown20009(2000)
    Unknown20001(1)
    Unknown36(22)
    Unknown1086(22)
    teleportRelativeX(150000)
    Unknown1007(-250000)
    Unknown35()
    GFX_0('rrb450MuzzleEff', 0)
    Unknown21012('727262343530000000000000000000000000000000000000000000000000000021000000')
    sprite('rrb450_17', 3)	# 32972-32974
    Unknown36(22)
    Unknown3001(255)
    Unknown35()
    sprite('rrb450_18', 3)	# 32975-32977
    sprite('rrb450_19', 3)	# 32978-32980
    Unknown2037(0)

    def upon_CLEAR_OR_EXIT():
        Unknown2038(1)
        if (SLOT_2 == 130):
            Unknown20009(1200)
        if (SLOT_2 == 190):
            clearUponHandler(3)
            sendToLabel(102)
    SFX_3('rrbse_14')
    label(101)
    sprite('rrb450_17', 3)	# 32981-32983
    sprite('rrb450_18', 3)	# 32984-32986
    sprite('rrb450_19', 3)	# 32987-32989
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('rrb450_20', 6)	# 32990-32995
    Unknown21012('727262343530466c61726500000000000000000000000000000000000000000020000000')
    sprite('rrb450_21', 6)	# 32996-33001
    sprite('rrb450_22', 10)	# 33002-33011
    sprite('rrb450_23', 10)	# 33012-33021
    sprite('rrb450_24', 10)	# 33022-33031
    sprite('rrb450_25', 10)	# 33032-33041
    sprite('rrb450_25', 10)	# 33042-33051
    tag_voice(0, 'rrb292_1', 'rrb292_2', 'rrb292_0', '')
    Unknown21012('727262343530000000000000000000000000000000000000000000000000000022000000')
    SFX_3('rrbse_07')
    sprite('rrb450_26', 4)	# 33052-33055	 **attackbox here**
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    RefreshMultihit()
    Unknown11064(3)
    Damage(40000)
    MinimumDamagePct(100)
    sprite('rrb450_27', 4)	# 33056-33059	 **attackbox here**
    sprite('rrb450_28', 4)	# 33060-33063	 **attackbox here**
    sprite('rrb450_26', 4)	# 33064-33067	 **attackbox here**
    sprite('rrb450_27', 4)	# 33068-33071	 **attackbox here**
    sprite('rrb450_28', 4)	# 33072-33075	 **attackbox here**
    sprite('rrb450_26', 4)	# 33076-33079	 **attackbox here**
    sprite('rrb450_27', 4)	# 33080-33083	 **attackbox here**
    sprite('rrb450_28', 4)	# 33084-33087	 **attackbox here**
    sprite('rrb450_26', 4)	# 33088-33091	 **attackbox here**
    sprite('rrb450_27', 4)	# 33092-33095	 **attackbox here**
    sprite('rrb450_28', 4)	# 33096-33099	 **attackbox here**
    sprite('rrb450_26', 4)	# 33100-33103	 **attackbox here**
    sprite('rrb450_27', 4)	# 33104-33107	 **attackbox here**
    sprite('rrb450_28', 4)	# 33108-33111	 **attackbox here**
    sprite('rrb450_26', 4)	# 33112-33115	 **attackbox here**
    sprite('rrb450_27', 4)	# 33116-33119	 **attackbox here**
    sprite('rrb450_28', 4)	# 33120-33123	 **attackbox here**
    sprite('rrb450_26', 4)	# 33124-33127	 **attackbox here**
    sprite('rrb450_27', 4)	# 33128-33131	 **attackbox here**
    sprite('rrb450_28', 4)	# 33132-33135	 **attackbox here**
    sprite('null', 24)	# 33136-33159
    Unknown30057('')
    Unknown23024(0)
    sprite('rrb610_00', 4)	# 33160-33163
    GFX_0('rrb610Eff', -1)
    GFX_0('rrb450WinPetal', -1)
    Unknown20009(1000)
    Unknown1000(0)
    teleportRelativeY(0)
    sprite('rrb610_01', 4)	# 33164-33167
    sprite('rrb610_02', 4)	# 33168-33171
    sprite('rrb610_03', 4)	# 33172-33175
    sprite('rrb610_04', 4)	# 33176-33179
    sprite('rrb610_05', 4)	# 33180-33183
    sprite('rrb610_06', 4)	# 33184-33187
    sprite('rrb610_07', 4)	# 33188-33191
    Unknown18010()
    Unknown21011(500)
    sprite('rrb610_02', 4)	# 33192-33195
    sprite('rrb610_03', 4)	# 33196-33199
    sprite('rrb610_04', 4)	# 33200-33203
    sprite('rrb610_05', 4)	# 33204-33207
    sprite('rrb610_06', 4)	# 33208-33211
    sprite('rrb610_07', 4)	# 33212-33215
    sprite('rrb610_02', 4)	# 33216-33219
    sprite('rrb610_03', 4)	# 33220-33223
    sprite('rrb610_04', 4)	# 33224-33227
    sprite('rrb610_05', 4)	# 33228-33231
    sprite('rrb610_06', 4)	# 33232-33235
    sprite('rrb610_07', 4)	# 33236-33239
    sprite('rrb610_02', 4)	# 33240-33243
    sprite('rrb610_03', 4)	# 33244-33247
    sprite('rrb610_04', 4)	# 33248-33251
    sprite('rrb610_05', 4)	# 33252-33255
    sprite('rrb610_06', 4)	# 33256-33259
    sprite('rrb610_07', 4)	# 33260-33263
    SFX_4('rrb522')
    label(999)
    sprite('rrb610_02', 4)	# 33264-33267
    sprite('rrb610_03', 4)	# 33268-33271
    sprite('rrb610_04', 4)	# 33272-33275
    sprite('rrb610_05', 4)	# 33276-33279
    sprite('rrb610_06', 4)	# 33280-33283
    sprite('rrb610_07', 4)	# 33284-33287
    loopRest()
    gotoLabel(999)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
    label(0)
    sprite('null', 1)	# 1-1
    EnableCollision(0)
    Unknown2034(0)
    teleportRelativeY(0)
    gotoLabel(0)

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
    sprite('rrb350_00', 4)	# 1-4
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    sprite('rrb350_01', 4)	# 5-8
    sprite('rrb350_02', 4)	# 9-12
    sprite('rrb350_03', 4)	# 13-16
    sprite('rrb350_04', 4)	# 17-20
    sprite('rrb350_05', 4)	# 21-24
    sprite('rrb350_03', 4)	# 25-28
    sprite('rrb350_04', 4)	# 29-32
    sprite('rrb350_05', 4)	# 33-36
    sprite('rrb350_03', 4)	# 37-40
    sprite('rrb350_04', 4)	# 41-44
    sprite('rrb350_05', 4)	# 45-48
    sprite('rrb350_03', 4)	# 49-52
    sprite('rrb350_04', 4)	# 53-56
    sprite('rrb350_06', 4)	# 57-60
    sprite('rrb350_07', 4)	# 61-64
    sprite('rrb350_08', 4)	# 65-68

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    sprite('rrb350_09', 2)	# 1-2
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('rrb350_10', 2)	# 3-4
    label(0)
    sprite('rrb350_03', 3)	# 5-7
    sprite('rrb350_04', 3)	# 8-10
    sprite('rrb350_05', 3)	# 11-13
    Unknown2038(1)
    if (SLOT_2 == 17):
        Unknown1018()
        Unknown1023()
        Unknown1038()
        Unknown1019(40)
        YAccel(40)
    (SLOT_2 >= 18)
    if SLOT_ReturnVal:
        _gotolabel(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb350_11', 4)	# 14-17
    sprite('rrb350_12', 4)	# 18-21
    sprite('rrb350_13', 4)	# 22-25

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rrb033_01', 3)	# 1-3
    sprite('rrb033_02', 3)	# 4-6
    sprite('rrb033_01', 3)	# 7-9
    sprite('rrb033_02', 3)	# 10-12
    sprite('rrb033_01', 3)	# 13-15
    sprite('rrb033_02', 3)	# 16-18
    sprite('rrb033_01', 3)	# 19-21
    sprite('rrb033_02', 3)	# 22-24
    sprite('rrb033_01', 3)	# 25-27
    sprite('rrb033_02', 3)	# 28-30
    sprite('rrb033_01', 30)	# 31-60

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17013()
        Unknown1084(1)
        Unknown2034(0)
        EnableCollision(0)
        Unknown2053(0)
        Unknown2067(2500, 240)

        def upon_STATE_END():
            Unknown2034(1)
            EnableCollision(1)
            Unknown2053(1)
    sprite('rrb610_00', 4)	# 1-4
    Unknown1084(1)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('rrb610_01', 4)	# 5-8
    sprite('rrb610_02', 4)	# 9-12
    sprite('rrb610_03', 4)	# 13-16
    sprite('rrb610_04', 4)	# 17-20
    sprite('rrb610_05', 4)	# 21-24
    sprite('rrb610_06', 4)	# 25-28
    sprite('rrb610_07', 4)	# 29-32
    label(1)
    sprite('rrb610_02', 4)	# 33-36
    sprite('rrb610_03', 4)	# 37-40
    sprite('rrb610_04', 4)	# 41-44
    sprite('rrb610_05', 4)	# 45-48
    sprite('rrb610_06', 4)	# 49-52
    sprite('rrb610_07', 4)	# 53-56
    Unknown30042(24)
    if SLOT_ReturnVal:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('rrb610_02', 4)	# 57-60
    sprite('rrb610_01', 4)	# 61-64
    sprite('rrb610_00', 4)	# 65-68

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rrb350_00', 6)	# 1-6
    sprite('rrb350_01', 6)	# 7-12
    sprite('rrb350_02', 6)	# 13-18
    sprite('rrb350_03', 6)	# 19-24
    sprite('rrb350_04', 6)	# 25-30
    sprite('rrb350_05', 6)	# 31-36
    sprite('rrb350_03', 6)	# 37-42
    sprite('rrb350_04', 6)	# 43-48
    sprite('rrb350_05', 6)	# 49-54
    sprite('rrb350_03', 6)	# 55-60
    sprite('rrb350_06', 5)	# 61-65
    sprite('rrb350_07', 5)	# 66-70
    sprite('rrb350_08', 5)	# 71-75
    sprite('rrb000_00', 30)	# 76-105

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        Unknown9015(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('keep', 28)	# 603-630
    sprite('rrb204_05', 3)	# 631-633
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(1500000)
    physicsYImpulse(-300000)
    setGravity(0)
    EnableCollision(1)
    Unknown2053(1)
    sprite('rrb204_06', 32767)	# 634-33400	 **attackbox here**
    GFX_0('rrb204MuzzleEff', 0)
    label(9)
    sprite('keep', 3)	# 33401-33403
    Unknown1084(1)
    sprite('rrb204_09', 2)	# 33404-33405
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown8000(100, 1, 1)
    sprite('rrb204_10', 4)	# 33406-33409
    sprite('rrb204_11', 4)	# 33410-33413
    sprite('rrb204_12', 4)	# 33414-33417
    SFX_3('rrbse_13')
    sprite('rrb204_13', 3)	# 33418-33420
    sprite('rrb204_14', 3)	# 33421-33423
    sprite('rrb204_15', 2)	# 33424-33425

@State
def CmnActChangeReturnAppealBurst():
    sprite('rrb064_00', 35)	# 1-35
    sprite('rrb064_01', 6)	# 36-41
    sprite('rrb064_02', 6)	# 42-47
    sprite('rrb064_03', 6)	# 48-53
    sprite('rrb064_04', 6)	# 54-59
    sprite('rrb000_00', 30)	# 60-89

@State
def CmnActChangePartnerQuickIn():
    sprite('rrb032_10', 3)	# 1-3
    sprite('rrb032_11', 5)	# 4-8
    sprite('rrb032_12', 7)	# 9-15
    sprite('rrb032_13', 7)	# 16-22
    sprite('rrb032_14', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('rrb033_00', 1)	# 1-1
    sprite('rrb033_01', 2)	# 2-3
    sprite('rrb033_02', 2)	# 4-5
    sprite('rrb033_02', 1)	# 6-6
    sprite('rrb033_01', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rrb033_02', 3)	# 10-12
    sprite('rrb033_01', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb033_04', 3)	# 16-18
    sprite('rrb033_04', 3)	# 19-21

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
    sprite('rrb020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('rrb020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('rrb010_03', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('rrb407_00', 3)	# 1-3
    sprite('rrb407_01', 3)	# 4-6
    sprite('rrb407_02', 4)	# 7-10
    Unknown7007('7272623231325f310000000000000000640000007272623231325f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rrb407_03', 4)	# 11-14
    GFX_0('rrb407MuzzleEff', 0)
    GFX_0('ShotAtk_Assist', 0)
    ScreenShake(9000, 3000)
    sprite('rrb407_04', 4)	# 15-18
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    sprite('rrb407_05', 8)	# 19-26
    sprite('rrb407_06', 4)	# 27-30
    sprite('rrb601_03', 4)	# 31-34
    GFX_0('rrb407EndEff', 0)
    sprite('rrb601_04', 4)	# 35-38
    sprite('rrb601_05', 4)	# 39-42
    sprite('rrb601_06', 4)	# 43-46
    sprite('rrb601_07', 4)	# 47-50
    sprite('rrb601_08', 4)	# 51-54

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(-2000)
        AirPushbackY(40000)
        AirUntechableTime(50)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11042(1)
        Unknown2004(1, 0)
    sprite('rrb203_00', 1)	# 1-1
    teleportRelativeX(-25000)
    sprite('rrb203_01', 1)	# 2-2
    sprite('rrb203_02', 1)	# 3-3
    sprite('rrb203_03', 1)	# 4-4
    sprite('rrb203_04', 1)	# 5-5
    sprite('rrb203_05', 2)	# 6-7
    sprite('rrb203_06', 2)	# 8-9
    Unknown7009(3)
    SFX_3('rrbse_03')
    sprite('rrb203_07', 3)	# 10-12	 **attackbox here**
    GFX_0('rrb203Eff', 0)
    sprite('rrb203_08', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('rrb203_09', 3)	# 16-18
    sprite('rrb203_10', 3)	# 19-21
    sprite('rrb203_11', 3)	# 22-24
    sprite('rrb203_12', 3)	# 25-27
    sprite('rrb203_13', 3)	# 28-30
    sprite('rrb203_14', 3)	# 31-33
    sprite('rrb203_15', 3)	# 34-36
    sprite('rrb203_16', 3)	# 37-39
    sprite('rrb203_17', 3)	# 40-42
    sprite('rrb203_18', 3)	# 43-45
    sprite('rrb203_19', 3)	# 46-48
    sprite('rrb203_20', 3)	# 49-51

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
        AttackP1(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(0)
        AirPushbackY(35000)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11042(1)
        Unknown11099(1)

        def upon_80():
            Hitstop(8)
            Unknown11099(0)
            EnableCollision(1)

        def upon_78():
            ScreenShake(10000, 0)
            GFX_0('rrb405_Issen', 0)
            GFX_0('rrbHitPetal_Add', 102)
            GFX_0('rrbHitPetal_Burst', 102)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            EnableCollision(1)
            Unknown2015(-1)
    sprite('rrb405_00', 3)	# 1-3
    sprite('rrb405_01', 3)	# 4-6
    Unknown1084(1)
    sprite('rrb405_02', 3)	# 7-9
    sprite('rrb405_03', 3)	# 10-12
    Unknown7007('7272623230395f310000000000000000640000007272623230395f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('rrb405_04', 12)	# 13-24	 **attackbox here**
    GFX_0('rrb405Eff', 0)
    physicsXImpulse(60000)
    Unknown8003(100, 1, 1)
    Unknown3004(-30)
    EnableCollision(0)
    Unknown2015(40)
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('rrb405_04', 6)	# 25-30	 **attackbox here**
    clearUponHandler(77)
    loopRest()
    label(9)
    sprite('rrb405_05', 6)	# 31-36
    clearUponHandler(77)
    Unknown1019(50)
    Unknown3001(128)
    Unknown3004(20)
    EnableCollision(1)
    Unknown2015(-1)
    Recovery()
    Unknown2063()
    sprite('rrb405_06', 6)	# 37-42
    Unknown8007(100, 1, 1)
    Unknown1019(50)
    sprite('rrb405_07', 6)	# 43-48
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown1019(50)
    sprite('rrb405_08', 10)	# 49-58
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
        if SLOT_162:
            SLOT_58 = 1

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('null', 1)	# 1-1
    Unknown2036(109, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-290000)
    Unknown1019(4)
    label(0)
    sprite('rrb020_07', 4)	# 3-6
    sprite('rrb020_08', 4)	# 7-10
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
        Unknown23056('')
        AttackLevel_(4)
        Damage(250)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        Unknown11001(0, 40, 40)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateAssault_AddAtk')
        Unknown30063(1)
        Unknown2073(1)
        Unknown1084(1)

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(1)
            teleportRelativeY(0)
            Unknown2015(40)
            DisableAttackRestOfMove()
            setInvincible(1)
            Unknown3001(200)
            Unknown3004(-20)
            Unknown13024(0)
            sendToLabel(0)
            Unknown21012('727262343331456666000000000000000000000000000000000000000000000021000000')
            GFX_0('rrb431Hit', 22)

        def upon_43():
            if (SLOT_48 == 4311):
                Unknown13024(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2005()
            Unknown2015(-1)
            EnableCollision(1)
    sprite('rrb431_00', 4)	# 1-4
    setInvincible(1)
    sprite('rrb431_01', 20)	# 5-24
    sprite('rrb431_02', 8)	# 25-32
    sprite('rrb431_03', 20)	# 33-52
    GFX_0('rrb431Eff', 0)
    sprite('rrb431_04', 8)	# 53-60
    SFX_3('rrbse_08')
    sprite('rrb431_05', 3)	# 61-63
    physicsXImpulse(4000)
    physicsYImpulse(4000)
    setGravity(0)
    SFX_0('000_airdash_1')
    SFX_3('rrbse_09')
    sprite('rrb431_06', 3)	# 64-66
    sprite('rrb431_07', 3)	# 67-69
    sprite('rrb431_08', 3)	# 70-72	 **attackbox here**
    DisableAttackRestOfMove()
    physicsYImpulse(0)
    Unknown1028(1000)
    Unknown20000(0)
    SFX_0('000_airdash_1')
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000023000000')
    sprite('rrb431_09', 3)	# 73-75	 **attackbox here**
    sprite('rrb431_10', 3)	# 76-78	 **attackbox here**
    sprite('rrb431_08', 2)	# 79-80	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 81-82	 **attackbox here**
    sprite('rrb431_10', 2)	# 83-84	 **attackbox here**
    sprite('rrb431_08', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    physicsXImpulse(80000)
    EnableCollision(0)
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 87-88	 **attackbox here**
    sprite('rrb431_10', 2)	# 89-90	 **attackbox here**
    sprite('rrb431_08', 2)	# 91-92	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 93-94	 **attackbox here**
    sprite('rrb431_10', 2)	# 95-96	 **attackbox here**
    sprite('rrb431_11', 4)	# 97-100
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000020000000')
    teleportRelativeY(25000)
    Unknown1043()
    physicsXImpulse(15000)
    setInvincible(0)
    EnableCollision(1)
    Unknown2015(-1)
    sprite('rrb431_12', 4)	# 101-104
    sprite('rrb431_13', 4)	# 105-108
    Unknown8000(100, 1, 1)
    physicsXImpulse(30000)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    sprite('rrb431_14', 3)	# 109-111
    sprite('rrb431_15', 3)	# 112-114
    sprite('rrb431_16', 3)	# 115-117
    sprite('rrb431_14', 3)	# 118-120
    sprite('rrb431_15', 3)	# 121-123
    sprite('rrb431_16', 3)	# 124-126
    sprite('rrb431_17', 3)	# 127-129
    Unknown1019(0)
    clearUponHandler(3)
    sprite('rrb431_18', 3)	# 130-132
    ExitState()
    label(0)
    sprite('rrb431_08', 2)	# 133-134	 **attackbox here**
    Unknown1019(30)
    sprite('rrb431_09', 2)	# 135-136	 **attackbox here**
    sprite('rrb431_10', 2)	# 137-138	 **attackbox here**
    sprite('rrb431_08', 2)	# 139-140	 **attackbox here**
    sprite('rrb431_09', 2)	# 141-142	 **attackbox here**
    sprite('rrb431_10', 2)	# 143-144	 **attackbox here**
    sprite('rrb431_08', 1)	# 145-145	 **attackbox here**
    sprite('rrb431_09', 1)	# 146-146	 **attackbox here**
    sprite('rrb431_10', 1)	# 147-147	 **attackbox here**
    sprite('rrb431_08', 1)	# 148-148	 **attackbox here**
    sprite('rrb431_09', 1)	# 149-149	 **attackbox here**
    sprite('rrb431_10', 1)	# 150-150	 **attackbox here**
    sprite('rrb431_11', 4)	# 151-154
    Unknown1086(22)
    teleportRelativeX(300000)
    teleportRelativeY(25000)
    physicsXImpulse(30000)
    Unknown3001(128)
    Unknown3004(20)
    setGravity(1000)
    sprite('rrb431_12', 4)	# 155-158
    sprite('rrb431_13', 4)	# 159-162
    Unknown8000(100, 1, 1)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    Unknown2015(150)
    EnableCollision(1)
    sprite('rrb431_14', 2)	# 163-164
    sprite('rrb431_15', 2)	# 165-166
    sprite('rrb431_16', 2)	# 167-168
    GFX_0('UltimateAssault_AddAtk', -1)
    Unknown23029(1, 4312, 0)
    sprite('rrb431_14', 2)	# 169-170
    sprite('rrb431_15', 2)	# 171-172
    sprite('rrb431_16', 2)	# 173-174
    sprite('rrb431_14', 2)	# 175-176
    sprite('rrb431_15', 2)	# 177-178
    sprite('rrb431_16', 2)	# 179-180
    sprite('rrb431_14', 2)	# 181-182
    sprite('rrb431_15', 2)	# 183-184
    sprite('rrb431_16', 2)	# 185-186
    sprite('rrb431_14', 2)	# 187-188
    sprite('rrb431_15', 2)	# 189-190
    sprite('rrb431_16', 2)	# 191-192
    sprite('rrb431_14', 2)	# 193-194
    sprite('rrb431_15', 2)	# 195-196
    sprite('rrb431_16', 2)	# 197-198
    sprite('rrb431_14', 2)	# 199-200
    sprite('rrb431_15', 2)	# 201-202
    sprite('rrb431_16', 2)	# 203-204
    sprite('rrb431_14', 2)	# 205-206
    sprite('rrb431_15', 2)	# 207-208
    sprite('rrb431_16', 2)	# 209-210
    sprite('rrb431_14', 4)	# 211-214
    sprite('rrb431_15', 4)	# 215-218
    sprite('rrb431_16', 4)	# 219-222
    sprite('rrb431_14', 4)	# 223-226
    sprite('rrb431_15', 4)	# 227-230
    sprite('rrb431_16', 4)	# 231-234
    sprite('rrb431_17', 4)	# 235-238
    Unknown1019(0)
    clearUponHandler(3)
    Unknown2015(-1)
    sprite('rrb431_18', 4)	# 239-242
    sprite('rrb003_00', 3)	# 243-245
    sprite('rrb003_01', 3)	# 246-248
    GFX_0('rrb431Petal_DDD', -1)
    sprite('rrb601_04', 6)	# 249-254
    sprite('rrb601_05', 6)	# 255-260
    sprite('rrb601_06', 6)	# 261-266
    sprite('rrb601_07', 6)	# 267-272
    sprite('rrb601_08', 6)	# 273-278

@State
def AN_CmnActChangePartnerDDODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(300)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        AirUntechableTime(120)
        Unknown11001(0, 40, 40)
        PushbackX(0)
        Unknown11062(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566665f536c6173680000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateAssaultOD_AddAtk')
        Unknown9001(5)
        Unknown30063(1)
        Unknown2073(1)
        Unknown1084(1)

        def upon_78():
            clearUponHandler(78)
            clearUponHandler(1)
            teleportRelativeY(0)
            Unknown2015(40)
            DisableAttackRestOfMove()
            setInvincible(1)
            Unknown3001(200)
            Unknown3004(-20)
            Unknown13024(0)
            sendToLabel(0)
            Unknown21012('727262343331456666000000000000000000000000000000000000000000000021000000')
            GFX_0('rrb431Hit', 22)

        def upon_43():
            if (SLOT_48 == 4311):
                Unknown13024(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2005()
            Unknown2015(-1)
            EnableCollision(1)
    sprite('rrb431_00', 4)	# 1-4
    setInvincible(1)
    sprite('rrb431_01', 20)	# 5-24
    sprite('rrb431_02', 8)	# 25-32
    sprite('rrb431_03', 20)	# 33-52
    GFX_0('rrb431Eff', 0)
    sprite('rrb431_04', 8)	# 53-60
    SFX_3('rrbse_08')
    sprite('rrb431_05', 3)	# 61-63
    physicsXImpulse(4000)
    physicsYImpulse(4000)
    setGravity(0)
    SFX_0('000_airdash_1')
    SFX_3('rrbse_09')
    sprite('rrb431_06', 3)	# 64-66
    sprite('rrb431_07', 3)	# 67-69
    sprite('rrb431_08', 3)	# 70-72	 **attackbox here**
    DisableAttackRestOfMove()
    physicsYImpulse(0)
    Unknown1028(1000)
    Unknown20000(0)
    SFX_0('000_airdash_1')
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000023000000')
    sprite('rrb431_09', 3)	# 73-75	 **attackbox here**
    sprite('rrb431_10', 3)	# 76-78	 **attackbox here**
    sprite('rrb431_08', 2)	# 79-80	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 81-82	 **attackbox here**
    sprite('rrb431_10', 2)	# 83-84	 **attackbox here**
    sprite('rrb431_08', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    physicsXImpulse(80000)
    EnableCollision(0)
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 87-88	 **attackbox here**
    sprite('rrb431_10', 2)	# 89-90	 **attackbox here**
    sprite('rrb431_08', 2)	# 91-92	 **attackbox here**
    SFX_0('000_airdash_1')
    sprite('rrb431_09', 2)	# 93-94	 **attackbox here**
    sprite('rrb431_10', 2)	# 95-96	 **attackbox here**
    sprite('rrb431_11', 4)	# 97-100
    Unknown21012('727262343331456666000000000000000000000000000000000000000000000020000000')
    teleportRelativeY(25000)
    Unknown1043()
    physicsXImpulse(15000)
    setInvincible(0)
    EnableCollision(1)
    Unknown2015(-1)
    sprite('rrb431_12', 4)	# 101-104
    sprite('rrb431_13', 4)	# 105-108
    Unknown8000(100, 1, 1)
    physicsXImpulse(30000)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    sprite('rrb431_14', 3)	# 109-111
    sprite('rrb431_15', 3)	# 112-114
    sprite('rrb431_16', 3)	# 115-117
    sprite('rrb431_14', 3)	# 118-120
    sprite('rrb431_15', 3)	# 121-123
    sprite('rrb431_16', 3)	# 124-126
    sprite('rrb431_17', 3)	# 127-129
    Unknown1019(0)
    clearUponHandler(3)
    sprite('rrb431_18', 3)	# 130-132
    ExitState()
    label(0)
    sprite('rrb431_08', 2)	# 133-134	 **attackbox here**
    Unknown1019(30)
    sprite('rrb431_09', 2)	# 135-136	 **attackbox here**
    sprite('rrb431_10', 2)	# 137-138	 **attackbox here**
    sprite('rrb431_08', 2)	# 139-140	 **attackbox here**
    sprite('rrb431_09', 2)	# 141-142	 **attackbox here**
    sprite('rrb431_10', 2)	# 143-144	 **attackbox here**
    sprite('rrb431_08', 1)	# 145-145	 **attackbox here**
    sprite('rrb431_09', 1)	# 146-146	 **attackbox here**
    sprite('rrb431_10', 1)	# 147-147	 **attackbox here**
    sprite('rrb431_08', 1)	# 148-148	 **attackbox here**
    sprite('rrb431_09', 1)	# 149-149	 **attackbox here**
    sprite('rrb431_10', 1)	# 150-150	 **attackbox here**
    sprite('rrb431_11', 4)	# 151-154
    Unknown1086(22)
    teleportRelativeX(300000)
    teleportRelativeY(25000)
    physicsXImpulse(30000)
    Unknown3001(128)
    Unknown3004(20)
    setGravity(1000)
    sprite('rrb431_12', 4)	# 155-158
    sprite('rrb431_13', 4)	# 159-162
    Unknown8000(100, 1, 1)

    def upon_CLEAR_OR_EXIT():
        Unknown1019(95)
        Unknown8010(100, 1, 0)
    Unknown2015(150)
    EnableCollision(1)
    sprite('rrb431_14', 2)	# 163-164
    sprite('rrb431_15', 2)	# 165-166
    sprite('rrb431_16', 2)	# 167-168
    GFX_0('UltimateAssaultOD_AddAtk', -1)
    Unknown23029(1, 4312, 0)
    sprite('rrb431_14', 2)	# 169-170
    sprite('rrb431_15', 2)	# 171-172
    sprite('rrb431_16', 2)	# 173-174
    sprite('rrb431_14', 2)	# 175-176
    sprite('rrb431_15', 2)	# 177-178
    sprite('rrb431_16', 2)	# 179-180
    sprite('rrb431_14', 2)	# 181-182
    sprite('rrb431_15', 2)	# 183-184
    sprite('rrb431_16', 2)	# 185-186
    sprite('rrb431_14', 2)	# 187-188
    sprite('rrb431_15', 2)	# 189-190
    sprite('rrb431_16', 2)	# 191-192
    sprite('rrb431_14', 2)	# 193-194
    sprite('rrb431_15', 2)	# 195-196
    sprite('rrb431_16', 2)	# 197-198
    sprite('rrb431_14', 2)	# 199-200
    sprite('rrb431_15', 2)	# 201-202
    sprite('rrb431_16', 2)	# 203-204
    sprite('rrb431_14', 2)	# 205-206
    sprite('rrb431_15', 2)	# 207-208
    sprite('rrb431_16', 2)	# 209-210
    sprite('rrb431_14', 4)	# 211-214
    sprite('rrb431_15', 4)	# 215-218
    sprite('rrb431_16', 4)	# 219-222
    sprite('rrb431_14', 4)	# 223-226
    sprite('rrb431_15', 4)	# 227-230
    sprite('rrb431_16', 4)	# 231-234
    sprite('rrb431_17', 4)	# 235-238
    Unknown1019(0)
    clearUponHandler(3)
    Unknown2015(-1)
    sprite('rrb431_18', 4)	# 239-242
    sprite('rrb003_00', 3)	# 243-245
    sprite('rrb003_01', 3)	# 246-248
    GFX_0('rrb431Petal_DDD', -1)
    sprite('rrb601_04', 6)	# 249-254
    sprite('rrb601_05', 6)	# 255-260
    sprite('rrb601_06', 6)	# 261-266
    sprite('rrb601_07', 6)	# 267-272
    sprite('rrb601_08', 6)	# 273-278

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('keep', 13)	# 121-133
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-840000)
    Unknown1007(2400000)
    physicsXImpulse(30000)
    physicsYImpulse(-85714)
    setGravity(0)
    sprite('rrb253_00', 3)	# 134-136
    sprite('rrb253_01', 3)	# 137-139
    sprite('rrb253_02', 3)	# 140-142
    sprite('rrb204_04', 3)	# 143-145
    sprite('rrb204_05', 3)	# 146-148
    Unknown2053(1)
    sprite('rrb204_06', 3)	# 149-151	 **attackbox here**
    GFX_0('rrb204MuzzleEff', 0)
    label(1)
    sprite('rrb204_07', 3)	# 152-154
    sprite('rrb204_08', 3)	# 155-157
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 158-160
    Unknown1084(1)
    sprite('rrb204_09', 3)	# 161-163
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown8000(100, 1, 1)
    sprite('rrb204_10', 5)	# 164-168
    sprite('rrb204_11', 5)	# 169-173
    sprite('rrb204_12', 5)	# 174-178
    SFX_3('rrbse_13')
    sprite('rrb204_13', 4)	# 179-182
    sprite('rrb204_14', 4)	# 183-186
    sprite('rrb204_15', 3)	# 187-189

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        Unknown1084(1)
    sprite('rrb010_00', 2)	# 1-2
    sprite('rrb010_01', 2)	# 3-4
    sprite('rrb204_00', 3)	# 5-7
    tag_voice(1, 'rrb157_0', 'rrb157_1', '', '')
    SLOT_12 = SLOT_19
    Unknown1019(5)
    physicsYImpulse(25000)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    setGravity(1800)
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    Unknown23087(100000)
    sprite('rrb204_01', 3)	# 8-10
    sprite('rrb204_00', 3)	# 11-13
    sprite('rrb204_02', 3)	# 14-16
    sprite('rrb204_03', 3)	# 17-19
    sprite('rrb204_04', 3)	# 20-22
    sprite('rrb204_05', 3)	# 23-25
    sprite('rrb204_06', 3)	# 26-28	 **attackbox here**
    GFX_0('rrb204MuzzleEff', 0)
    loopRest()
    label(0)
    sprite('rrb204_08', 4)	# 29-32
    sprite('rrb204_07', 4)	# 33-36
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('rrb204_09', 3)	# 37-39
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown23087(-1)
    sprite('rrb204_10', 3)	# 40-42
    sprite('rrb204_11', 3)	# 43-45
    sprite('rrb204_12', 2)	# 46-47
    SFX_3('rrbse_13')
    sprite('rrb204_12', 1)	# 48-48
    Unknown13002(1)
    Unknown13003(1)
    Unknown13005(1)
    Unknown13006(1)
    Unknown13008(1)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13017(1)
    Unknown13021(1)
    Unknown13019(1)
    Unknown13026(1)
    Unknown13029(1)
    Unknown13031(1)
    Recovery()
    sprite('rrb204_13', 3)	# 49-51
    sprite('rrb204_14', 3)	# 52-54
    sprite('rrb204_15', 3)	# 55-57

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        Unknown9016(1)
        loopRelated(17, 18)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('rrb204_07', 4)	# 1-4
    sprite('rrb204_08', 4)	# 5-8
    sprite('rrb204_07', 4)	# 9-12
    label(1)
    sprite('rrb204_09', 2)	# 13-14
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    Unknown8000(100, 1, 1)
    sprite('rrb204_10', 2)	# 15-16
    sprite('rrb204_11', 2)	# 17-18
    sprite('rrb204_12', 3)	# 19-21
    sprite('rrb204_13', 3)	# 22-24
    sprite('rrb204_14', 3)	# 25-27
    sprite('rrb204_15', 3)	# 28-30
    label(2)
    sprite('rrb202_00', 2)	# 31-32
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('rrb202_01', 3)	# 33-35
    sprite('rrb202_02', 3)	# 36-38
    SFX_3('rrbse_04')
    sprite('rrb202_03', 3)	# 39-41
    tag_voice(0, 'rrb158_0', 'rrb158_1', '', '')
    sprite('rrb202_04', 4)	# 42-45	 **attackbox here**
    GFX_0('rrb202Eff', 100)
    sprite('rrb202_05', 3)	# 46-48
    sprite('rrb202_06', 3)	# 49-51
    sprite('rrb202_07', 3)	# 52-54
    sprite('rrb202_08', 3)	# 55-57
    sprite('rrb202_09', 4)	# 58-61
    sprite('rrb202_10', 4)	# 62-65
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('rrb000_00', 5)	# 66-70
    sprite('rrb000_01', 5)	# 71-75
    sprite('rrb000_02', 5)	# 76-80
    sprite('rrb000_03', 5)	# 81-85
    sprite('rrb000_04', 5)	# 86-90
    sprite('rrb000_05', 5)	# 91-95
    sprite('rrb000_06', 5)	# 96-100
    sprite('rrb000_07', 5)	# 101-105
    sprite('rrb000_08', 5)	# 106-110
    sprite('rrb000_09', 5)	# 111-115
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 116-116

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown9016(1)
    sprite('rrb311_00', 2)	# 1-2
    sprite('rrb311_01', 3)	# 3-5
    sprite('rrb311_02', 3)	# 6-8
    sprite('rrb311_03', 3)	# 9-11
    sprite('rrb311_04', 3)	# 12-14
    SFX_3('rrbse_03')
    sprite('rrb311_05', 2)	# 15-16	 **attackbox here**
    physicsYImpulse(23000)
    physicsXImpulse(2000)
    setGravity(2100)
    GFX_0('rrb311Eff', 0)
    sprite('rrb311_06', 3)	# 17-19
    sprite('rrb311_07', 3)	# 20-22
    sprite('rrb311_08', 3)	# 23-25
    label(0)
    sprite('rrb311_09', 3)	# 26-28
    sendToLabelUpon(2, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb311_10', 3)	# 29-31
    Unknown1084(1)
    clearUponHandler(2)
    sprite('rrb010_00', 1)	# 32-32
    sprite('rrb010_01', 3)	# 33-35
    sprite('rrb010_02', 3)	# 36-38
    label(0)
    sprite('rrb000_00', 5)	# 39-43
    sprite('rrb000_01', 5)	# 44-48
    sprite('rrb000_02', 5)	# 49-53
    sprite('rrb000_03', 5)	# 54-58
    sprite('rrb000_04', 5)	# 59-63
    sprite('rrb000_05', 5)	# 64-68
    sprite('rrb000_06', 5)	# 69-73
    sprite('rrb000_07', 5)	# 74-78
    sprite('rrb000_08', 5)	# 79-83
    sprite('rrb000_09', 5)	# 84-88
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 89-89

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    sprite('rrb320_00', 4)	# 1-4
    sprite('rrb320_01', 5)	# 5-9
    tag_voice(0, 'rrb159_0', 'rrb159_1', '', '')
    sprite('rrb320_02', 5)	# 10-14
    GFX_0('rrb320MuzzleEff', 0)
    SFX_3('rrbse_05')
    sprite('rrb320_03', 5)	# 15-19
    SFX_3('rrbse_01')
    sprite('rrb320_04', 3)	# 20-22	 **attackbox here**
    GFX_0('rrb320Eff', 0)
    sprite('rrb320_05', 4)	# 23-26
    sprite('rrb320_06', 4)	# 27-30
    sprite('rrb320_07', 5)	# 31-35
    sprite('rrb320_08', 5)	# 36-40
    sprite('rrb320_09', 5)	# 41-45
    sprite('rrb320_10', 5)	# 46-50
    sprite('rrb320_11', 5)	# 51-55
    sprite('rrb320_12', 5)	# 56-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('rrb000_00', 5)	# 1-5
    sprite('rrb000_01', 5)	# 6-10
    sprite('rrb000_02', 5)	# 11-15
    sprite('rrb000_03', 5)	# 16-20
    sprite('rrb000_04', 5)	# 21-25
    sprite('rrb000_05', 5)	# 26-30
    sprite('rrb000_06', 5)	# 31-35
    sprite('rrb000_07', 5)	# 36-40
    sprite('rrb000_08', 5)	# 41-45
    sprite('rrb000_09', 5)	# 46-50
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb320_00', 4)	# 51-54
    sprite('rrb320_01', 5)	# 55-59
    tag_voice(0, 'rrb159_0', 'rrb159_1', '', '')
    sprite('rrb320_02', 5)	# 60-64
    GFX_0('rrb320MuzzleEff', 0)
    SFX_3('rrbse_05')
    sprite('rrb320_03', 5)	# 65-69
    SFX_3('rrbse_01')
    sprite('rrb320_04', 3)	# 70-72	 **attackbox here**
    GFX_0('rrb320Eff', 0)
    sprite('rrb320_05', 4)	# 73-76
    sprite('rrb320_06', 4)	# 77-80
    sprite('rrb320_07', 5)	# 81-85
    sprite('rrb320_08', 5)	# 86-90
    sprite('rrb320_09', 5)	# 91-95
    sprite('rrb320_10', 5)	# 96-100
    sprite('rrb320_11', 5)	# 101-105
    sprite('rrb320_12', 5)	# 106-110

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    sprite('null', 28)	# 1-28
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 29-29
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('rrb204_00', 2)	# 30-31
    physicsXImpulse(7500)
    physicsYImpulse(-6500)
    setGravity(0)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rrb204_01', 2)	# 32-33
    physicsXImpulse(50000)
    physicsYImpulse(-39000)
    sprite('rrb204_02', 2)	# 34-35
    sprite('rrb204_03', 2)	# 36-37
    sprite('rrb204_04', 2)	# 38-39
    sprite('rrb204_05', 2)	# 40-41
    sprite('rrb204_06', 3)	# 42-44	 **attackbox here**
    GFX_0('rrb204MuzzleEff', 0)
    sprite('rrb204_07', 4)	# 45-48
    label(0)
    sprite('rrb204_08', 4)	# 49-52
    sprite('rrb204_07', 4)	# 53-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb204_09', 4)	# 57-60
    GFX_0('rrbCaseEff', 0)
    SFX_3('rrbse_01')
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rrb204_10', 4)	# 61-64
    sprite('rrb204_11', 4)	# 65-68
    sprite('rrb204_12', 4)	# 69-72
    sprite('rrb204_13', 4)	# 73-76
    sprite('rrb204_14', 4)	# 77-80
    sprite('rrb204_15', 4)	# 81-84
    sprite('rrb000_00', 5)	# 85-89
    sprite('rrb000_01', 5)	# 90-94
    sprite('rrb000_02', 5)	# 95-99
    sprite('rrb000_03', 5)	# 100-104
    sprite('rrb000_04', 5)	# 105-109
    sprite('rrb000_05', 5)	# 110-114
    sprite('rrb000_06', 5)	# 115-119
    sprite('rrb000_07', 5)	# 120-124
    sprite('rrb000_08', 5)	# 125-129
    sprite('rrb000_09', 5)	# 130-134

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    sprite('rrb408_00', 2)	# 1-2
    sprite('rrb408_01', 3)	# 3-5
    sprite('rrb408_03', 3)	# 6-8
    SFX_3('rrbse_05')
    sprite('rrb408_04', 3)	# 9-11
    sprite('rrb408_05', 2)	# 12-13	 **attackbox here**
    GFX_0('rrb408Eff_Assist', 0)
    sprite('rrb408_06ex', 2)	# 14-15
    sprite('rrb408_07ex', 2)	# 16-17
    sprite('rrb408_08', 3)	# 18-20
    sprite('rrb408_09', 3)	# 21-23
    sprite('rrb408_10', 3)	# 24-26
    sprite('rrb408_11', 3)	# 27-29
    sprite('rrb408_12', 2)	# 30-31
    sprite('rrb010_00', 2)	# 32-33
    loopRest()
    sprite('rrb000_00', 5)	# 34-38
    sprite('rrb000_01', 5)	# 39-43
    sprite('rrb000_02', 5)	# 44-48
    sprite('rrb000_03', 5)	# 49-53
    sprite('rrb000_04', 5)	# 54-58
    sprite('rrb000_05', 5)	# 59-63
    sprite('rrb000_06', 5)	# 64-68
    sprite('rrb000_07', 5)	# 69-73
    sprite('rrb000_08', 5)	# 74-78
    sprite('rrb000_09', 5)	# 79-83

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
    sprite('rrb320_00', 4)	# 1-4
    sprite('rrb320_01', 5)	# 5-9
    sprite('rrb320_02', 5)	# 10-14
    GFX_0('rrb320MuzzleEff', 0)
    SFX_3('rrbse_05')
    sprite('rrb320_03', 5)	# 15-19
    SFX_3('rrbse_01')
    sprite('rrb320_04', 3)	# 20-22	 **attackbox here**
    GFX_0('rrb320Eff', 0)
    sprite('rrb320_05', 4)	# 23-26
    sprite('rrb320_06', 4)	# 27-30
    sprite('rrb320_07', 5)	# 31-35
    sprite('rrb320_08', 5)	# 36-40
    sprite('rrb320_09', 5)	# 41-45
    sprite('rrb320_10', 5)	# 46-50
    sprite('rrb320_11', 5)	# 51-55
    sprite('rrb320_12', 5)	# 56-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        Unknown9016(1)
        Unknown11050('020000007272624869744566660000000000000000000000000000000000000000000000')
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('rrb000_00', 5)	# 1-5
    sprite('rrb000_01', 5)	# 6-10
    sprite('rrb000_02', 5)	# 11-15
    sprite('rrb000_03', 5)	# 16-20
    sprite('rrb000_04', 5)	# 21-25
    sprite('rrb000_05', 5)	# 26-30
    sprite('rrb000_06', 5)	# 31-35
    sprite('rrb000_07', 5)	# 36-40
    sprite('rrb000_08', 5)	# 41-45
    sprite('rrb000_09', 5)	# 46-50
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rrb320_00', 4)	# 51-54
    sprite('rrb320_01', 5)	# 55-59
    sprite('rrb320_02', 5)	# 60-64
    GFX_0('rrb320MuzzleEff', 0)
    SFX_3('rrbse_05')
    sprite('rrb320_03', 5)	# 65-69
    SFX_3('rrbse_01')
    sprite('rrb320_04', 3)	# 70-72	 **attackbox here**
    GFX_0('rrb320Eff', 0)
    sprite('rrb320_05', 4)	# 73-76
    sprite('rrb320_06', 4)	# 77-80
    sprite('rrb320_07', 5)	# 81-85
    sprite('rrb320_08', 5)	# 86-90
    sprite('rrb320_09', 5)	# 91-95
    sprite('rrb320_10', 5)	# 96-100
    sprite('rrb320_11', 5)	# 101-105
    sprite('rrb320_12', 5)	# 106-110

@Subroutine
def MouthTableInit():
    Unknown18011('rrb000', 13921, 13923, 13921, 13155, 24881, 25399, 24887, 25401, 24887, 25401, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb500', 13921, 13923, 13921, 13155, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb500', '001')
    Unknown18011('rrb501', 13921, 13923, 13921, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb501', '002')
    Unknown18011('rrb502', 13921, 13923, 13921, 14691, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb502', '003')
    Unknown18011('rrb503', 13665, 12643, 24880, 25398, 12342, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 13619, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb503', '004')
    Unknown18011('rrb504', 12643, 12641, 25397, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb504', '005')
    Unknown18011('rrb505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb505', '006')
    Unknown18011('rrb520', 13665, 13667, 12641, 25399, 12853, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25392, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb520', '007')
    Unknown18011('rrb521', 13921, 13923, 12641, 25397, 12595, 14177, 14179, 12641, 25397, 12850, 13665, 13667, 13665, 13667, 12641, 25393, 24886, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb521', '008')
    Unknown18011('rrb522', 14177, 14179, 14177, 13923, 13921, 13923, 12641, 25393, 12849, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb522', '009')
    Unknown18011('rrb523', 12897, 25397, 13620, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb523', '010')
    Unknown18011('rrb524', 13921, 13923, 13921, 14691, 13921, 13923, 13921, 12643, 24885, 25398, 24886, 25398, 24886, 13617, 13923, 13921, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb524', '011')
    Unknown18011('rrb525', 14177, 13667, 14177, 13667, 12641, 25394, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb525', '012')
    Unknown18011('rrb402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb403_0', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb403_1', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb601bes', 12643, 12897, 25392, 13367, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600bma', 12643, 13153, 25397, 24887, 25399, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 12337, 13665, 13667, 13665, 13155, 24882, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600brc', 12643, 13409, 13411, 12641, 25394, 14133, 12641, 25392, 24887, 25399, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600brg', 12643, 12897, 25397, 14132, 14177, 14179, 14177, 14179, 14177, 12643, 24881, 25399, 24887, 12849, 13155, 24880, 25401, 24887, 25401, 13362, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600pag', 12643, 14177, 14179, 13665, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600pbc_1', 12643, 12897, 25397, 12854, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600pbc_2', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb601pla', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600rbl', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600', 12643, 14177, 12643, 24880, 12338, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb601rwi', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb601ryn', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 12852, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb601ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25393, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb601uhy', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600uva', 12643, 12897, 25397, 14134, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14134, 14177, 13411, 24887, 25397, 24885, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb604', 12643, 12641, 25397, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600ahe', 12899, 14177, 14179, 14689, 13155, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb602ahe', 12899, 13665, 25393, 12596, 13921, 14179, 13921, 14179, 13921, 14179, 13921, 14179, 12641, 25398, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600bsu', 12643, 13665, 25395, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25399, 13107, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 12337, 14179, 14689, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600pad', 12643, 12897, 25392, 24887, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb602pad', 14177, 14179, 14177, 14179, 14689, 14435, 14177, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600rne', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb600kym', 12643, 13409, 25397, 13619, 13921, 13923, 13921, 13923, 12641, 25400, 24887, 12849, 12643, 24888, 12594, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb602kym', 13411, 12641, 25394, 24889, 25399, 24887, 25399, 24887, 25399, 12593, 12641, 25398, 12337, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb600', '017')
    Unknown30092('rrb600bma', '018')
    Unknown30092('rrb600brc', '019')
    Unknown30092('rrb600brg', '020')
    Unknown30092('rrb600pag', '021')
    Unknown30092('rrb600pbc_1', '022')
    Unknown30092('rrb600pbc_2', '023')
    Unknown30092('rrb600rbl', '024')
    Unknown30092('rrb600uva', '025')
    Unknown30092('rrb600uyu', '026')
    Unknown30092('rrb601bes', '027')
    Unknown30092('rrb601pla', '028')
    Unknown30092('rrb601rwi', '029')
    Unknown30092('rrb601ryn', '030')
    Unknown30092('rrb601ugo', '031')
    Unknown30092('rrb601uhy', '032')
    Unknown30092('rrb604', '033')
    Unknown30092('rrb600ahe', '034')
    Unknown30092('rrb602ahe', '035')
    Unknown30092('rrb600bsu', '036')
    Unknown30092('rrb600pad', '037')
    Unknown30092('rrb602pad', '038')
    Unknown30092('rrb600rne', '039')
    Unknown30092('rrb600kym', '040')
    Unknown30092('rrb602kym', '041')
    Unknown18011('rrb700bes', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701bma', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700brc', 12643, 13409, 13411, 13409, 13667, 24884, 12337, 14179, 14177, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700brg', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 13923, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700pag', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 12338, 13409, 13411, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701pbc', 12643, 14177, 12643, 24882, 25399, 12849, 12641, 25396, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24889, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701pla', 12643, 13665, 13667, 13665, 13667, 13665, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 12339, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700rbl', 12643, 14177, 14691, 12641, 25396, 12340, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 13361, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701ryn', 12643, 13665, 13667, 12641, 25396, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700ugo', 12643, 12897, 25397, 12340, 12641, 25397, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700uhy', 12643, 13665, 13667, 14177, 13411, 24880, 12337, 14179, 14177, 14179, 14177, 13667, 24884, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701uva', 12643, 24887, 13361, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700uyu', 12643, 13665, 13667, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700ahe', 12643, 14177, 14179, 14689, 13155, 24889, 25400, 24887, 25399, 24885, 25399, 24886, 25399, 24887, 25399, 24887, 13361, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701bsu', 12897, 25394, 24887, 14386, 13155, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 12897, 25395, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700pad', 12643, 12641, 25400, 12596, 12897, 25396, 24887, 25398, 24887, 25398, 24888, 14386, 14179, 12897, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb700rne', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24881, 12338, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rrb701kym', 12643, 13153, 25396, 14643, 12641, 25399, 14385, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('rrb700bes', '042')
    Unknown30092('rrb700brc', '043')
    Unknown30092('rrb700brg', '044')
    Unknown30092('rrb700pag', '045')
    Unknown30092('rrb700rbl', '046')
    Unknown30092('rrb700rwi', '047')
    Unknown30092('rrb700ugo', '048')
    Unknown30092('rrb700uhy', '049')
    Unknown30092('rrb700uyu', '050')
    Unknown30092('rrb701bma', '051')
    Unknown30092('rrb701pbc', '052')
    Unknown30092('rrb701pla', '053')
    Unknown30092('rrb701ryn', '054')
    Unknown30092('rrb701uva', '055')
    Unknown30092('rrb700ahe', '056')
    Unknown30092('rrb701bsu', '057')
    Unknown30092('rrb700pad', '058')
    Unknown30092('rrb700rne', '059')
    Unknown30092('rrb701kym', '060')
    if SLOT_172:
        Unknown18011('rrb000', 12643, 13667, 14177, 14179, 13667, 14177, 14179, 12897, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 25395, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb500', 12643, 12643, 14177, 14179, 14177, 13667, 14177, 13923, 12899, 13409, 12643, 24883, 25399, 24887, 25399, 24887, 25394, 24881, 25399, 24887, 25399, 24887, 25396, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb501', 12643, 12899, 14177, 14179, 13665, 13155, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24881, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb502', 12643, 12899, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb503', 12643, 12643, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb504', 12643, 14177, 14179, 14177, 13155, 12643, 13665, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb505', 12643, 13667, 14177, 14179, 13921, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 24883, 25399, 25394, 24881, 25398, 24882, 25399, 24887, 25399, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb520', 12643, 13155, 14177, 14435, 14177, 13923, 12643, 24883, 25399, 24887, 25399, 25394, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb521', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 12641, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb522', 12643, 13155, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 13411, 12899, 14177, 14179, 13665, 12899, 14177, 12899, 12643, 24881, 25399, 24887, 25396, 24887, 25399, 25396, 12593, 14177, 14179, 14177, 14179, 14177, 13411, 14691, 14177, 14179, 14177, 14179, 13921, 12643, 24880, 25396, 24884, 25396, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb523', 12643, 14177, 14179, 14177, 14179, 13409, 13155, 24886, 25399, 25397, 24881, 25399, 24887, 25399, 24887, 25396, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb525', 12643, 14177, 14179, 12643, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 13667, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb402_0', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 13155, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb402_1', 12643, 12643, 14177, 14179, 12641, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24883, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb403_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb403_1', 12643, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb601bes', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 25399, 25394, 25398, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600bma', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24882, 25399, 24887, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600brc', 12899, 13409, 25399, 24887, 13874, 14179, 14177, 14179, 14433, 12643, 24880, 12337, 14179, 13153, 25396, 25399, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600brg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14435, 14177, 14179, 13153, 13667, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 14691, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 24886, 25399, 24887, 25396, 24882, 25399, 25399, 24881, 25399, 24881, 25399, 25397, 24881, 25399, 24887, 25393, 12849, 14177, 14179, 14177, 12643, 14435, 14177, 14179, 14177, 14179, 12897, 13667, 0, 0)
        Unknown18011('rrb600pag', 12643, 12643, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 14177, 14179, 14177, 13923, 14177, 14179, 13409, 12899, 14177, 12643, 14177, 13667, 12643, 14177, 14179, 14177, 13667, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600pbc_1', 12643, 12899, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 12899, 14177, 13923, 12643, 14177, 13411, 13155, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 24881, 25399, 25397, 24883, 25399, 24887, 25399, 25397, 24881, 25399, 24887, 25399, 25397, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600pbc_2', 12643, 12899, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 12899, 14177, 13923, 12643, 14177, 13411, 13155, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 24881, 25399, 25397, 24883, 25399, 24887, 25399, 25397, 24881, 25399, 24887, 25399, 25397, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb601pla', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 12641, 25394, 25395, 25395, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600rbl', 12643, 12643, 14177, 14179, 14177, 14179, 13409, 13411, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 12899, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600', 12643, 12641, 25396, 24887, 12594, 14177, 14179, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 24882, 25399, 24887, 25399, 24887, 25399, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb601rwi', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14435, 14177, 14179, 14177, 14179, 14433, 14179, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb601ryn', 12643, 12643, 14177, 12643, 14177, 14179, 14177, 14179, 12641, 12643, 24884, 25399, 24887, 25398, 24881, 25399, 24887, 25399, 24887, 12849, 14179, 13155, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb601ugo', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 13921, 13155, 14177, 13155, 12643, 14177, 14179, 12641, 25396, 25399, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb601uhy', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 12899, 24888, 25399, 24887, 25399, 25396, 24882, 24887, 25399, 24888, 12337, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 25399, 25397, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600uva', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 13921, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 25394, 25394, 25397, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600uyu', 12643, 12643, 14177, 14179, 14177, 13411, 13411, 14177, 13155, 13155, 12641, 25392, 25399, 24883, 25399, 24887, 25399, 25398, 12853, 14177, 14179, 14177, 13155, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 25399, 25396, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb604', 12643, 12643, 14177, 14179, 12641, 25393, 25395, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600ahe', 12643, 12643, 14177, 14179, 13153, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24883, 25399, 24887, 25399, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb602ahe', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 24888, 25399, 24887, 25397, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600bsu', 12643, 13153, 25400, 12594, 13921, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14179, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600pad', 12643, 12643, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 12643, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb602pad', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 24884, 14644, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600rne', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 25399, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb600kym', 12643, 12643, 13153, 25393, 25399, 25396, 25399, 25399, 25399, 25395, 24883, 25399, 24887, 24887, 25399, 12593, 14177, 14179, 14177, 13923, 12899, 14177, 13667, 13923, 14177, 14179, 13665, 13667, 14177, 14179, 14177, 14179, 14433, 14179, 12899, 14177, 14179, 14177, 14179, 13921, 14179, 14177, 14179, 14177, 12899, 13155, 14177, 14179, 12641, 25394, 25399, 25395, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb602kym', 12643, 12643, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700bes', 12643, 13667, 14177, 13155, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13411, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 13923, 12643, 14177, 12643, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701bma', 12643, 12643, 14177, 14179, 13153, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 13667, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700brc', 12643, 12643, 12641, 25396, 13874, 14177, 13411, 14177, 14179, 12641, 25395, 24885, 25399, 24887, 25399, 24887, 13361, 14179, 13923, 13667, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700brg', 12643, 14177, 14179, 12641, 25396, 24887, 13105, 12643, 24881, 25399, 24887, 25397, 24885, 13361, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 12849, 13667, 14179, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700pag', 12643, 14177, 14179, 12641, 25396, 24887, 25397, 12594, 12641, 25401, 25399, 25399, 13361, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701pbc', 12643, 12641, 25398, 25399, 25399, 14130, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24886, 25399, 24887, 25399, 24887, 12849, 12643, 25392, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701pla', 12643, 12643, 14177, 14179, 14689, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25401, 25399, 25398, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700rbl', 12643, 14177, 14691, 12641, 25396, 12340, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 25399, 25395, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701ryn', 12643, 14435, 12897, 25393, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700ugo', 12643, 13667, 12897, 25400, 24887, 14386, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 12337, 13667, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700uhy', 12643, 12643, 14177, 14179, 14177, 14179, 14689, 13411, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25396, 24887, 25399, 24887, 25399, 25398, 13620, 14177, 14179, 12641, 12643, 14177, 13411, 14435, 14177, 14179, 14177, 13155, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701uva', 12643, 14691, 12641, 25396, 14387, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700uyu', 12643, 12643, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14689, 14179, 13923, 14433, 14179, 13667, 14177, 13923, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700ahe', 12643, 12643, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 14177, 14179, 12641, 25396, 25397, 25397, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701bsu', 12643, 12643, 14177, 14179, 12641, 13923, 14177, 14179, 13153, 14179, 12897, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 12641, 25394, 25399, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700pad', 12643, 12643, 12641, 25396, 24887, 12594, 12643, 13155, 24882, 25399, 24887, 25399, 25398, 24883, 25399, 24887, 25399, 24887, 13361, 14179, 13411, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb700rne', 12643, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14689, 14179, 13155, 24880, 25399, 24887, 25399, 25398, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 25399, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('rrb701kym', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 14179, 13155, 14177, 14179, 14177, 14179, 12641, 25394, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('brc')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bes')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('uhy')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('ugo')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('rwi')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('rbl')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('pag')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uva')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('uyu')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('ryn')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('pla')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('bma')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('ahe')
    if SLOT_ReturnVal:
        _gotolabel(240)
    PartnerChar('bsu')
    if SLOT_ReturnVal:
        _gotolabel(250)
    PartnerChar('pad')
    if SLOT_ReturnVal:
        _gotolabel(260)
    PartnerChar('rne')
    if SLOT_ReturnVal:
        _gotolabel(270)
    PartnerChar('kym')
    if SLOT_ReturnVal:
        _gotolabel(280)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('rrb600_00', 10)	# 2-11
    GFX_0('rrb600Eff', 0)
    sprite('rrb600_00', 2)	# 12-13
    random_(2, 0, 25)
    SLOT_51 = SLOT_0
    if SLOT_51:
        SFX_1('rrb501')
    Unknown20(87, 2, 51)
    sprite('rrb600_00', 18)	# 14-31
    if (not SLOT_51):
        Unknown7006('rrb500', 100, 895644274, 13360, 0, 0, 100, 895644274, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rrb600_01', 6)	# 32-37
    SFX_0('019_cloth_b')
    Unknown21012('727262363030456666000000000000000000000000000000000000000000000020000000')
    sprite('rrb600_02', 6)	# 38-43
    sprite('rrb600_03', 6)	# 44-49
    sprite('rrb600_04', 6)	# 50-55
    sprite('rrb600_05', 6)	# 56-61
    sprite('rrb600_06', 6)	# 62-67
    sprite('rrb600_07', 6)	# 68-73
    sprite('rrb600_08', 6)	# 74-79
    loopRest()
    gotoLabel(99)
    label(10)
    sprite('rrb601_00', 15)	# 80-94
    sprite('rrb601_01', 6)	# 95-100
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 101-106
    sprite('rrb601_03', 6)	# 107-112
    Unknown7006('rrb502', 100, 895644274, 13104, 0, 0, 100, 895644274, 13360, 0, 0, 100, 895644274, 13616, 0, 0, 100)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 113-118
    sprite('rrb601_05', 6)	# 119-124
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 125-130
    sprite('rrb601_07', 6)	# 131-136
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 137-142
    loopRest()
    gotoLabel(99)
    label(99)
    sprite('rrb000_00', 7)	# 143-149
    sprite('rrb000_01', 7)	# 150-156
    sprite('rrb000_02', 7)	# 157-163
    sprite('rrb000_03', 7)	# 164-170
    sprite('rrb000_04', 7)	# 171-177
    sprite('rrb000_05', 7)	# 178-184
    sprite('rrb000_06', 7)	# 185-191
    sprite('rrb000_07', 7)	# 192-198
    sprite('rrb000_08', 7)	# 199-205
    sprite('rrb000_09', 7)	# 206-212
    if SLOT_97:
        _gotolabel(99)
    sprite('rrb000_00', 7)	# 213-219
    Unknown21007(24, 41)
    sprite('rrb000_01', 7)	# 220-226
    sprite('rrb000_02', 7)	# 227-233
    sprite('rrb000_03', 7)	# 234-240
    sprite('rrb000_04', 7)	# 241-247
    sprite('rrb000_05', 7)	# 248-254
    sprite('rrb000_06', 7)	# 255-261
    sprite('rrb000_07', 7)	# 262-268
    sprite('rrb000_08', 7)	# 269-275
    sprite('rrb000_09', 7)	# 276-282
    loopRest()
    ExitState()
    label(20)
    sprite('rrb000_00', 1)	# 283-283
    SFX_1('rrb604')
    label(21)
    sprite('rrb000_00', 7)	# 284-290
    sprite('rrb000_01', 7)	# 291-297
    sprite('rrb000_02', 7)	# 298-304
    sprite('rrb000_03', 7)	# 305-311
    sprite('rrb000_04', 7)	# 312-318
    sprite('rrb000_05', 7)	# 319-325
    sprite('rrb000_06', 7)	# 326-332
    sprite('rrb000_07', 7)	# 333-339
    sprite('rrb000_08', 7)	# 340-346
    sprite('rrb000_09', 7)	# 347-353
    gotoLabel(21)
    label(100)
    sprite('rrb613_00', 6)	# 354-359
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rrb613_01', 6)	# 360-365
    sprite('rrb613_02', 6)	# 366-371
    sprite('rrb613_03', 20)	# 372-391
    sprite('rrb613_04', 6)	# 392-397
    sprite('rrb613_05', 6)	# 398-403
    SFX_1('rrb600brc')
    sprite('rrb613_06', 6)	# 404-409
    label(101)
    sprite('rrb613_07', 1)	# 410-410
    if SLOT_97:
        _gotolabel(101)
    sprite('rrb613_07', 30)	# 411-440
    sprite('rrb613_04', 6)	# 441-446
    Unknown21007(24, 40)
    sprite('rrb613_02', 6)	# 447-452
    sprite('rrb613_01', 6)	# 453-458
    sprite('rrb613_00', 6)	# 459-464
    Unknown21011(180)
    label(102)
    sprite('rrb000_00', 7)	# 465-471
    sprite('rrb000_01', 7)	# 472-478
    sprite('rrb000_02', 7)	# 479-485
    sprite('rrb000_03', 7)	# 486-492
    sprite('rrb000_04', 7)	# 493-499
    sprite('rrb000_05', 7)	# 500-506
    sprite('rrb000_06', 7)	# 507-513
    sprite('rrb000_07', 7)	# 514-520
    sprite('rrb000_08', 7)	# 521-527
    sprite('rrb000_09', 7)	# 528-534
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('rrb601_00', 1)	# 535-535

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('rrb601_00', 5)	# 536-540
    gotoLabel(111)
    label(112)
    sprite('rrb601_00', 15)	# 541-555
    sprite('rrb601_01', 6)	# 556-561
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 562-567
    sprite('rrb601_03', 6)	# 568-573
    SFX_1('rrb601bes')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 574-579
    sprite('rrb601_05', 6)	# 580-585
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 586-591
    sprite('rrb601_07', 6)	# 592-597
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 598-603
    Unknown23018(1)
    label(113)
    sprite('rrb000_00', 7)	# 604-610
    sprite('rrb000_01', 7)	# 611-617
    sprite('rrb000_02', 7)	# 618-624
    sprite('rrb000_03', 7)	# 625-631
    sprite('rrb000_04', 7)	# 632-638
    sprite('rrb000_05', 7)	# 639-645
    sprite('rrb000_06', 7)	# 646-652
    sprite('rrb000_07', 7)	# 653-659
    sprite('rrb000_08', 7)	# 660-666
    sprite('rrb000_09', 7)	# 667-673
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('rrb601_00', 15)	# 674-688
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rrb601_01', 6)	# 689-694
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 695-700
    sprite('rrb601_03', 6)	# 701-706
    SFX_1('rrb600pbc_1')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 707-712
    sprite('rrb601_05', 6)	# 713-718
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 719-724
    sprite('rrb601_07', 6)	# 725-730
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 731-736
    Unknown2037(4)
    label(121)
    sprite('rrb000_00', 7)	# 737-743
    sprite('rrb000_01', 7)	# 744-750
    sprite('rrb000_02', 7)	# 751-757
    sprite('rrb000_03', 7)	# 758-764
    sprite('rrb000_04', 7)	# 765-771
    sprite('rrb000_05', 7)	# 772-778
    sprite('rrb000_06', 7)	# 779-785
    sprite('rrb000_07', 7)	# 786-792
    sprite('rrb000_08', 7)	# 793-799
    sprite('rrb000_09', 7)	# 800-806
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(121)
    sprite('rrb000_00', 1)	# 807-807
    Unknown21011(360)
    label(122)
    sprite('rrb000_00', 7)	# 808-814
    sprite('rrb000_01', 7)	# 815-821
    sprite('rrb000_02', 7)	# 822-828
    sprite('rrb000_03', 7)	# 829-835
    sprite('rrb000_04', 7)	# 836-842
    sprite('rrb000_05', 7)	# 843-849
    Unknown21007(24, 40)
    sprite('rrb000_06', 7)	# 850-856
    sprite('rrb000_07', 7)	# 857-863
    sprite('rrb000_08', 7)	# 864-870
    sprite('rrb000_09', 7)	# 871-877
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('rrb600_00', 1)	# 878-878
    GFX_0('rrb600Eff', 0)
    if SLOT_158:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('rrb600_00', 1)	# 879-879
    gotoLabel(131)
    label(132)
    sprite('rrb600_00', 10)	# 880-889
    sprite('rrb600_00', 2)	# 890-891
    SLOT_51 = SLOT_0
    if SLOT_51:
        SFX_1('rrb601uhy')
    Unknown20(40, 2, 51)
    sprite('rrb600_01', 6)	# 892-897
    SFX_0('019_cloth_b')
    Unknown21012('727262363030456666000000000000000000000000000000000000000000000020000000')
    sprite('rrb600_02', 6)	# 898-903
    sprite('rrb600_03', 6)	# 904-909
    sprite('rrb600_04', 6)	# 910-915
    sprite('rrb600_05', 6)	# 916-921
    sprite('rrb600_06', 6)	# 922-927
    sprite('rrb600_07', 6)	# 928-933
    sprite('rrb600_08', 6)	# 934-939
    label(133)
    sprite('rrb000_00', 7)	# 940-946
    sprite('rrb000_01', 7)	# 947-953
    sprite('rrb000_02', 7)	# 954-960
    sprite('rrb000_03', 7)	# 961-967
    sprite('rrb000_04', 7)	# 968-974
    sprite('rrb000_05', 7)	# 975-981
    sprite('rrb000_06', 7)	# 982-988
    sprite('rrb000_07', 7)	# 989-995
    sprite('rrb000_08', 7)	# 996-1002
    sprite('rrb000_09', 7)	# 1003-1009
    if SLOT_97:
        _gotolabel(133)
    sprite('rrb000_00', 1)	# 1010-1010
    Unknown21007(24, 40)
    Unknown21011(240)
    label(134)
    sprite('rrb000_00', 7)	# 1011-1017
    sprite('rrb000_01', 7)	# 1018-1024
    sprite('rrb000_02', 7)	# 1025-1031
    sprite('rrb000_03', 7)	# 1032-1038
    sprite('rrb000_04', 7)	# 1039-1045
    sprite('rrb000_05', 7)	# 1046-1052
    sprite('rrb000_06', 7)	# 1053-1059
    sprite('rrb000_07', 7)	# 1060-1066
    sprite('rrb000_08', 7)	# 1067-1073
    sprite('rrb000_09', 7)	# 1074-1080
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('rrb601_00', 1)	# 1081-1081
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('rrb601_00', 5)	# 1082-1086
    gotoLabel(141)
    label(142)
    sprite('rrb601_00', 15)	# 1087-1101
    sprite('rrb601_01', 6)	# 1102-1107
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 1108-1113
    sprite('rrb601_03', 6)	# 1114-1119
    SFX_1('rrb601ugo')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 1120-1125
    sprite('rrb601_05', 6)	# 1126-1131
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 1132-1137
    sprite('rrb601_07', 6)	# 1138-1143
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 1144-1149
    Unknown2037(2)
    label(143)
    sprite('rrb000_00', 7)	# 1150-1156
    sprite('rrb000_01', 7)	# 1157-1163
    sprite('rrb000_02', 7)	# 1164-1170
    sprite('rrb000_03', 7)	# 1171-1177
    sprite('rrb000_04', 7)	# 1178-1184
    sprite('rrb000_05', 7)	# 1185-1191
    sprite('rrb000_06', 7)	# 1192-1198
    sprite('rrb000_07', 7)	# 1199-1205
    if (not SLOT_2):
        Unknown21007(24, 40)
        Unknown21011(240)
    sprite('rrb000_08', 7)	# 1206-1212
    sprite('rrb000_09', 7)	# 1213-1219
    Unknown2038(-1)
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('rrb601_00', 1)	# 1220-1220
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('rrb601_00', 5)	# 1221-1225
    gotoLabel(151)
    label(152)
    sprite('rrb601_00', 15)	# 1226-1240
    sprite('rrb601_01', 6)	# 1241-1246
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 1247-1252
    sprite('rrb601_03', 6)	# 1253-1258
    SFX_1('rrb601rwi')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 1259-1264
    sprite('rrb601_05', 6)	# 1265-1270
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 1271-1276
    sprite('rrb601_07', 6)	# 1277-1282
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 1283-1288
    Unknown23018(1)
    label(153)
    sprite('rrb000_00', 7)	# 1289-1295
    sprite('rrb000_01', 7)	# 1296-1302
    sprite('rrb000_02', 7)	# 1303-1309
    sprite('rrb000_03', 7)	# 1310-1316
    sprite('rrb000_04', 7)	# 1317-1323
    sprite('rrb000_05', 7)	# 1324-1330
    sprite('rrb000_06', 7)	# 1331-1337
    sprite('rrb000_07', 7)	# 1338-1344
    sprite('rrb000_08', 7)	# 1345-1351
    sprite('rrb000_09', 7)	# 1352-1358
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('rrb000_00', 7)	# 1359-1365
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rrb300_00', 6)	# 1366-1371
    sprite('rrb300_01', 6)	# 1372-1377
    sprite('rrb300_02', 6)	# 1378-1383
    sprite('rrb300_03', 6)	# 1384-1389
    SFX_1('rrb600rbl')
    label(161)
    sprite('rrb300_04', 1)	# 1390-1390
    if SLOT_97:
        _gotolabel(161)
    sprite('rrb300_04', 30)	# 1391-1420
    sprite('rrb300_05', 6)	# 1421-1426
    sprite('rrb300_06', 6)	# 1427-1432
    Unknown21007(24, 40)
    Unknown21011(180)
    label(162)
    sprite('rrb000_00', 7)	# 1433-1439
    sprite('rrb000_01', 7)	# 1440-1446
    sprite('rrb000_02', 7)	# 1447-1453
    sprite('rrb000_03', 7)	# 1454-1460
    sprite('rrb000_04', 7)	# 1461-1467
    sprite('rrb000_05', 7)	# 1468-1474
    sprite('rrb000_06', 7)	# 1475-1481
    sprite('rrb000_07', 7)	# 1482-1488
    sprite('rrb000_08', 7)	# 1489-1495
    sprite('rrb000_09', 7)	# 1496-1502
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('rrb631_00', 40)	# 1503-1542
    GFX_0('rrbef_kakeai_brg', -1)
    Unknown2019(100)
    Unknown23015(12)
    Unknown1000(-1365000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(171)
    sprite('rrb631_01', 7)	# 1543-1549
    SFX_1('rrb600brg')
    sprite('rrb631_02', 7)	# 1550-1556
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 20)	# 1557-1576
    sprite('rrb631_00', 30)	# 1577-1606
    GFX_0('rrbef_kakeai_brg_smoke02', -1)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 1607-1613
    sprite('rrb631_02', 7)	# 1614-1620
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 40)	# 1621-1660
    sprite('rrb631_00', 30)	# 1661-1690
    GFX_0('rrbef_kakeai_brg_smoke02', -1)
    Unknown2019(100)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 1691-1697
    sprite('rrb631_02', 7)	# 1698-1704
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 40)	# 1705-1744
    sprite('rrb631_00', 40)	# 1745-1784
    GFX_0('rrbef_kakeai_brg_smoke02', -1)
    Unknown2019(100)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 1785-1791
    sprite('rrb631_02', 7)	# 1792-1798
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 30)	# 1799-1828
    sprite('rrb631_03', 32767)	# 1829-34595
    Unknown21007(24, 40)
    label(171)
    sprite('rrb631_04', 1)	# 34596-34596
    sprite('rrb631_04', 1)	# 34597-34597
    sprite('rrb631_04', 1)	# 34598-34598
    sprite('rrb631_04', 1)	# 34599-34599
    sprite('rrb631_04', 1)	# 34600-34600
    sprite('rrb631_05', 3)	# 34601-34603
    Unknown1000(-1065000)
    sprite('rrb631_06', 3)	# 34604-34606
    Unknown21011(120)
    label(172)
    sprite('rrb631_05', 3)	# 34607-34609
    Unknown1000(-1065000)
    sprite('rrb631_06', 3)	# 34610-34612
    sprite('rrb631_07', 3)	# 34613-34615
    loopRest()
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('rrb631_00', 40)	# 34616-34655
    GFX_0('rrbef_kakeai_brg', -1)
    Unknown2019(100)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 34656-34662
    SFX_1('rrb600pag')
    sprite('rrb631_02', 7)	# 34663-34669
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 40)	# 34670-34709
    sprite('rrb631_00', 30)	# 34710-34739
    GFX_0('rrbef_kakeai_brg_smoke02', -1)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 34740-34746
    sprite('rrb631_02', 7)	# 34747-34753
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 40)	# 34754-34793
    sprite('rrb631_00', 30)	# 34794-34823
    GFX_0('rrbef_kakeai_brg_smoke02', -1)
    Unknown2019(100)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 34824-34830
    sprite('rrb631_02', 7)	# 34831-34837
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 40)	# 34838-34877
    sprite('rrb631_00', 40)	# 34878-34917
    GFX_0('rrbef_kakeai_brg_smoke02', -1)
    Unknown2019(100)
    Unknown1000(-1365000)
    sprite('rrb631_01', 7)	# 34918-34924
    sprite('rrb631_02', 7)	# 34925-34931
    GFX_0('rrbef_kakeai_brg_smoke01', -1)
    Unknown1000(-1105000)
    sprite('rrb631_03', 30)	# 34932-34961
    sprite('rrb631_03', 32767)	# 34962-67728
    Unknown21007(24, 40)
    Unknown21011(330)
    ExitState()
    label(190)
    sprite('rrb001_00', 5)	# 67729-67733
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('rrb001_02', 8)	# 67734-67741
    SFX_1('rrb600uva')
    sprite('rrb001_03', 8)	# 67742-67749
    sprite('rrb001_04', 8)	# 67750-67757
    sprite('rrb001_05', 8)	# 67758-67765
    sprite('rrb001_06', 8)	# 67766-67773
    sprite('rrb001_07', 8)	# 67774-67781
    sprite('rrb001_08', 8)	# 67782-67789
    sprite('rrb001_09', 8)	# 67790-67797
    sprite('rrb001_02', 8)	# 67798-67805
    sprite('rrb001_03', 8)	# 67806-67813
    sprite('rrb001_04', 8)	# 67814-67821
    sprite('rrb001_05', 8)	# 67822-67829
    sprite('rrb001_06', 8)	# 67830-67837
    sprite('rrb001_07', 8)	# 67838-67845
    sprite('rrb001_08', 8)	# 67846-67853
    sprite('rrb001_09', 8)	# 67854-67861
    sprite('rrb001_01', 5)	# 67862-67866
    sprite('rrb001_00', 5)	# 67867-67871
    label(191)
    sprite('rrb000_00', 7)	# 67872-67878
    sprite('rrb000_01', 7)	# 67879-67885
    sprite('rrb000_02', 7)	# 67886-67892
    sprite('rrb000_03', 7)	# 67893-67899
    sprite('rrb000_04', 7)	# 67900-67906
    sprite('rrb000_05', 7)	# 67907-67913
    sprite('rrb000_06', 7)	# 67914-67920
    sprite('rrb000_07', 7)	# 67921-67927
    sprite('rrb000_08', 7)	# 67928-67934
    sprite('rrb000_09', 7)	# 67935-67941
    if SLOT_97:
        _gotolabel(191)
    sprite('rrb000_00', 1)	# 67942-67942
    Unknown21007(24, 40)
    Unknown21011(420)
    label(192)
    sprite('rrb000_00', 7)	# 67943-67949
    sprite('rrb000_01', 7)	# 67950-67956
    sprite('rrb000_02', 7)	# 67957-67963
    sprite('rrb000_03', 7)	# 67964-67970
    sprite('rrb000_04', 7)	# 67971-67977
    sprite('rrb000_05', 7)	# 67978-67984
    sprite('rrb000_06', 7)	# 67985-67991
    sprite('rrb000_07', 7)	# 67992-67998
    sprite('rrb000_08', 7)	# 67999-68005
    sprite('rrb000_09', 7)	# 68006-68012
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('rrb601_00', 15)	# 68013-68027
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rrb601_01', 6)	# 68028-68033
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 68034-68039
    sprite('rrb601_03', 6)	# 68040-68045
    SFX_1('rrb600uyu')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 68046-68051
    sprite('rrb601_05', 6)	# 68052-68057
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 68058-68063
    sprite('rrb601_07', 6)	# 68064-68069
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 68070-68075
    label(201)
    sprite('rrb000_00', 7)	# 68076-68082
    sprite('rrb000_01', 7)	# 68083-68089
    sprite('rrb000_02', 7)	# 68090-68096
    sprite('rrb000_03', 7)	# 68097-68103
    sprite('rrb000_04', 7)	# 68104-68110
    sprite('rrb000_05', 7)	# 68111-68117
    sprite('rrb000_06', 7)	# 68118-68124
    sprite('rrb000_07', 7)	# 68125-68131
    sprite('rrb000_08', 7)	# 68132-68138
    sprite('rrb000_09', 7)	# 68139-68145
    if SLOT_97:
        _gotolabel(201)
    sprite('rrb000_00', 1)	# 68146-68146
    Unknown21007(24, 40)
    Unknown21011(420)
    label(202)
    sprite('rrb000_00', 7)	# 68147-68153
    sprite('rrb000_01', 7)	# 68154-68160
    sprite('rrb000_02', 7)	# 68161-68167
    sprite('rrb000_03', 7)	# 68168-68174
    sprite('rrb000_04', 7)	# 68175-68181
    sprite('rrb000_05', 7)	# 68182-68188
    sprite('rrb000_06', 7)	# 68189-68195
    sprite('rrb000_07', 7)	# 68196-68202
    sprite('rrb000_08', 7)	# 68203-68209
    sprite('rrb000_09', 7)	# 68210-68216
    gotoLabel(202)
    ExitState()
    label(210)
    sprite('rrb601_00', 1)	# 68217-68217
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('rrb601_00', 1)	# 68218-68218
    gotoLabel(211)
    label(212)
    sprite('rrb601_00', 15)	# 68219-68233
    sprite('rrb601_01', 6)	# 68234-68239
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 68240-68245
    sprite('rrb601_03', 6)	# 68246-68251
    SFX_1('rrb601ryn')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 68252-68257
    sprite('rrb601_05', 6)	# 68258-68263
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 68264-68269
    sprite('rrb601_07', 6)	# 68270-68275
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 68276-68281
    Unknown23018(1)
    label(213)
    sprite('rrb000_00', 7)	# 68282-68288
    sprite('rrb000_01', 7)	# 68289-68295
    sprite('rrb000_02', 7)	# 68296-68302
    sprite('rrb000_03', 7)	# 68303-68309
    sprite('rrb000_04', 7)	# 68310-68316
    sprite('rrb000_05', 7)	# 68317-68323
    sprite('rrb000_06', 7)	# 68324-68330
    sprite('rrb000_07', 7)	# 68331-68337
    sprite('rrb000_08', 7)	# 68338-68344
    sprite('rrb000_09', 7)	# 68345-68351
    gotoLabel(213)
    ExitState()
    label(220)
    sprite('rrb000_00', 1)	# 68352-68352
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('rrb000_00', 7)	# 68353-68359
    sprite('rrb000_01', 7)	# 68360-68366
    sprite('rrb000_02', 7)	# 68367-68373
    sprite('rrb000_03', 7)	# 68374-68380
    sprite('rrb000_04', 7)	# 68381-68387
    sprite('rrb000_05', 7)	# 68388-68394
    sprite('rrb000_06', 7)	# 68395-68401
    sprite('rrb000_07', 7)	# 68402-68408
    sprite('rrb000_08', 7)	# 68409-68415
    sprite('rrb000_09', 7)	# 68416-68422
    gotoLabel(221)
    label(222)
    sprite('rrb001_00', 5)	# 68423-68427
    SFX_1('rrb601pla')
    sprite('rrb001_01', 5)	# 68428-68432
    sprite('rrb001_02', 8)	# 68433-68440
    sprite('rrb001_03', 8)	# 68441-68448
    sprite('rrb001_04', 8)	# 68449-68456
    sprite('rrb001_05', 8)	# 68457-68464
    sprite('rrb001_06', 8)	# 68465-68472
    sprite('rrb001_07', 8)	# 68473-68480
    sprite('rrb001_08', 8)	# 68481-68488
    sprite('rrb001_09', 8)	# 68489-68496
    sprite('rrb001_02', 8)	# 68497-68504
    sprite('rrb001_03', 8)	# 68505-68512
    sprite('rrb001_04', 8)	# 68513-68520
    sprite('rrb001_05', 8)	# 68521-68528
    sprite('rrb001_06', 8)	# 68529-68536
    sprite('rrb001_07', 8)	# 68537-68544
    sprite('rrb001_08', 8)	# 68545-68552
    sprite('rrb001_09', 8)	# 68553-68560
    sprite('rrb001_01', 5)	# 68561-68565
    sprite('rrb001_00', 5)	# 68566-68570
    Unknown23018(1)
    label(223)
    sprite('rrb000_00', 7)	# 68571-68577
    sprite('rrb000_01', 7)	# 68578-68584
    sprite('rrb000_02', 7)	# 68585-68591
    sprite('rrb000_03', 7)	# 68592-68598
    sprite('rrb000_04', 7)	# 68599-68605
    sprite('rrb000_05', 7)	# 68606-68612
    sprite('rrb000_06', 7)	# 68613-68619
    sprite('rrb000_07', 7)	# 68620-68626
    sprite('rrb000_08', 7)	# 68627-68633
    sprite('rrb000_09', 7)	# 68634-68640
    gotoLabel(223)
    ExitState()
    label(230)
    sprite('rrb000_00', 7)	# 68641-68647
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('rrb300_00', 6)	# 68648-68653
    sprite('rrb300_01', 6)	# 68654-68659
    sprite('rrb300_02', 6)	# 68660-68665
    sprite('rrb300_03', 6)	# 68666-68671
    SFX_1('rrb600bma')
    label(231)
    sprite('rrb300_04', 1)	# 68672-68672
    if SLOT_97:
        _gotolabel(231)
    sprite('rrb300_04', 30)	# 68673-68702
    sprite('rrb300_04', 32767)	# 68703-101469
    Unknown21007(24, 40)
    Unknown21011(180)
    ExitState()
    label(240)
    sprite('rrb001_00', 5)	# 101470-101474

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    if SLOT_158:
        Unknown2005()
    SFX_1('rrb600ahe')
    sprite('rrb001_01', 5)	# 101475-101479
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
    label(241)
    sprite('rrb001_02', 8)	# 101480-101487
    sprite('rrb001_03', 8)	# 101488-101495
    sprite('rrb001_04', 8)	# 101496-101503
    sprite('rrb001_05', 8)	# 101504-101511
    sprite('rrb001_06', 8)	# 101512-101519
    sprite('rrb001_07', 8)	# 101520-101527
    sprite('rrb001_08', 8)	# 101528-101535
    sprite('rrb001_09', 8)	# 101536-101543
    gotoLabel(241)
    sprite('rrb001_02', 8)	# 101544-101551
    Unknown21007(24, 40)
    label(242)
    sprite('rrb631_02', 7)	# 101552-101558
    Unknown2005()
    SFX_1('rrb602ahe')
    GFX_0('rrbef_kakeai_brg', -1)
    sprite('rrb631_03', 32767)	# 101559-134325
    Unknown23018(1)
    label(250)
    sprite('rrb631_03', 30)	# 134326-134355
    Unknown1000(-1180000)
    Unknown2019(-100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
    sprite('rrb631_03', 1)	# 134356-134356
    GFX_0('rrbef_kakeai_brg', -1)
    SFX_1('rrb600bsu')
    label(251)
    sprite('rrb631_03', 1)	# 134357-134357
    if SLOT_97:
        _gotolabel(251)
    sprite('rrb631_03', 30)	# 134358-134387
    sprite('rrb631_03', 32767)	# 134388-167154
    Unknown21007(24, 40)
    label(252)
    sprite('rrb631_04', 5)	# 167155-167159
    Unknown21011(30)
    label(253)
    sprite('rrb631_05', 3)	# 167160-167162
    sprite('rrb631_06', 3)	# 167163-167165
    sprite('rrb631_07', 3)	# 167166-167168
    loopRest()
    gotoLabel(253)
    label(260)
    sprite('rrb601_00', 15)	# 167169-167183

    def upon_40():
        clearUponHandler(40)
        sendToLabel(262)
    sprite('rrb601_01', 6)	# 167184-167189
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 167190-167195
    sprite('rrb601_03', 6)	# 167196-167201
    SFX_1('rrb600pad')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 167202-167207
    sprite('rrb601_05', 6)	# 167208-167213
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 167214-167219
    sprite('rrb601_07', 6)	# 167220-167225
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 167226-167231
    Unknown2037(20)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
    label(261)
    sprite('rrb000_00', 7)	# 167232-167238
    sprite('rrb000_01', 7)	# 167239-167245
    sprite('rrb000_02', 7)	# 167246-167252
    sprite('rrb000_03', 7)	# 167253-167259
    sprite('rrb000_04', 7)	# 167260-167266
    sprite('rrb000_05', 7)	# 167267-167273
    sprite('rrb000_06', 7)	# 167274-167280
    sprite('rrb000_07', 7)	# 167281-167287
    sprite('rrb000_08', 7)	# 167288-167294
    sprite('rrb000_09', 7)	# 167295-167301
    gotoLabel(261)
    label(262)
    sprite('rrb613_01', 6)	# 167302-167307
    sprite('rrb613_02', 6)	# 167308-167313
    sprite('rrb613_03', 20)	# 167314-167333
    sprite('rrb613_04', 6)	# 167334-167339
    sprite('rrb613_05', 6)	# 167340-167345
    SFX_1('rrb602pad')
    sprite('rrb613_06', 6)	# 167346-167351
    sprite('rrb613_07', 1)	# 167352-167352
    GFX_0('rrbef_kakeai_brg', -1)
    label(263)
    sprite('rrb613_07', 1)	# 167353-167353
    if SLOT_97:
        _gotolabel(263)
    sprite('rrb613_07', 30)	# 167354-167383
    sprite('rrb613_07', 32767)	# 167384-200150
    Unknown21007(24, 40)
    Unknown21011(200)
    label(270)
    sprite('rrb601_00', 15)	# 200151-200165
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('rrb601_01', 6)	# 200166-200171
    GFX_0('rrb601Eff', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_02', 6)	# 200172-200177
    sprite('rrb601_03', 6)	# 200178-200183
    SFX_1('rrb600rne')
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_04', 6)	# 200184-200189
    sprite('rrb601_05', 6)	# 200190-200195
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_06', 6)	# 200196-200201
    sprite('rrb601_07', 6)	# 200202-200207
    SFX_0('004_swing_grap_1_0')
    sprite('rrb601_08', 6)	# 200208-200213
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(120)
    label(271)
    sprite('rrb000_00', 7)	# 200214-200220
    sprite('rrb000_01', 7)	# 200221-200227
    sprite('rrb000_02', 7)	# 200228-200234
    sprite('rrb000_03', 7)	# 200235-200241
    sprite('rrb000_04', 7)	# 200242-200248
    sprite('rrb000_05', 7)	# 200249-200255
    sprite('rrb000_06', 7)	# 200256-200262
    sprite('rrb000_07', 7)	# 200263-200269
    sprite('rrb000_08', 7)	# 200270-200276
    sprite('rrb000_09', 7)	# 200277-200283
    gotoLabel(271)
    ExitState()
    label(280)
    sprite('rrb000_00', 7)	# 200284-200290
    if SLOT_158:
        Unknown2005()

    def upon_40():
        clearUponHandler(40)
        sendToLabel(282)
    sprite('rrb300_00', 6)	# 200291-200296
    sprite('rrb300_01', 6)	# 200297-200302
    sprite('rrb300_02', 6)	# 200303-200308
    sprite('rrb300_03', 6)	# 200309-200314
    GFX_0('rrbef_kakeai_brg', -1)
    SFX_1('rrb600kym')
    label(281)
    sprite('rrb300_04', 1)	# 200315-200315
    if SLOT_97:
        _gotolabel(281)
    sprite('rrb300_04', 30)	# 200316-200345
    sprite('rrb300_04', 32767)	# 200346-233112
    Unknown21007(24, 40)
    label(282)
    sprite('rrb300_05', 6)	# 233113-233118
    sprite('rrb300_06', 6)	# 233119-233124
    sprite('rrb000_00', 6)	# 233125-233130
    sprite('rrb613_00', 6)	# 233131-233136
    sprite('rrb613_01', 6)	# 233137-233142
    sprite('rrb613_02', 6)	# 233143-233148
    sprite('rrb613_03', 20)	# 233149-233168
    sprite('rrb613_04', 6)	# 233169-233174
    sprite('rrb613_05', 6)	# 233175-233180
    SFX_1('rrb602kym')
    sprite('rrb613_06', 6)	# 233181-233186
    sprite('rrb613_07', 32767)	# 233187-265953
    Unknown23018(1)
    label(991)
    sprite('rrb000_00', 1)	# 265954-265954
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('rrb000_00', 7)	# 265955-265961
    sprite('rrb000_01', 7)	# 265962-265968
    sprite('rrb000_02', 7)	# 265969-265975
    sprite('rrb000_03', 7)	# 265976-265982
    sprite('rrb000_04', 7)	# 265983-265989
    sprite('rrb000_05', 7)	# 265990-265996
    sprite('rrb000_06', 7)	# 265997-266003
    sprite('rrb000_07', 7)	# 266004-266010
    sprite('rrb000_08', 7)	# 266011-266017
    sprite('rrb000_09', 7)	# 266018-266024
    gotoLabel(992)
    label(993)
    sprite('rrb033_00', 2)	# 266025-266026

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
    sprite('rrb033_01', 2)	# 266027-266028
    label(994)
    sprite('rrb033_02', 3)	# 266029-266031
    sprite('rrb033_01', 3)	# 266032-266034
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 266035-266037
    ExitState()
    label(1000)
    sprite('rrb000_00', 7)	# 266038-266044
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)
    sprite('rrb300_00', 6)	# 266045-266050
    sprite('rrb300_01', 6)	# 266051-266056
    sprite('rrb300_02', 6)	# 266057-266062
    sprite('rrb300_03', 6)	# 266063-266068
    sprite('rrb300_04', 1)	# 266069-266069
    SFX_1('rrb600')
    label(1001)
    sprite('rrb300_04', 1)	# 266070-266070
    if SLOT_97:
        _gotolabel(1001)
    sprite('rrb300_04', 20)	# 266071-266090
    sprite('rrb300_04', 3)	# 266091-266093
    Unknown23029(24, 8001, 0)
    Unknown23029(22, 8001, 0)
    Unknown23029(23, 8001, 0)

    def upon_43():
        if (SLOT_48 == 8004):
            clearUponHandler(43)
            SFX_1('rrb604')
            Unknown23018(1)
        if (SLOT_48 == 8005):
            sendToLabel(1003)
        if (SLOT_48 == 8006):
            sendToLabel(1005)
    label(1002)
    sprite('rrb300_04', 1)	# 266094-266094
    gotoLabel(1002)
    label(1003)
    sprite('rrb300_05', 6)	# 266095-266100
    sprite('rrb300_06', 6)	# 266101-266106
    sprite('rrb000_00', 6)	# 266107-266112
    sprite('rrb001_00', 6)	# 266113-266118
    sprite('rrb001_01', 6)	# 266119-266124
    label(1004)
    sprite('rrb001_02', 6)	# 266125-266130
    sprite('rrb001_03', 6)	# 266131-266136
    sprite('rrb001_04', 6)	# 266137-266142
    sprite('rrb001_05', 6)	# 266143-266148
    sprite('rrb001_06', 6)	# 266149-266154
    sprite('rrb001_07', 6)	# 266155-266160
    sprite('rrb001_08', 6)	# 266161-266166
    gotoLabel(1004)
    label(1005)
    sprite('rrb001_01', 6)	# 266167-266172
    sprite('rrb001_00', 6)	# 266173-266178
    label(1006)
    sprite('rrb000_00', 7)	# 266179-266185
    sprite('rrb000_01', 7)	# 266186-266192
    sprite('rrb000_02', 7)	# 266193-266199
    sprite('rrb000_03', 7)	# 266200-266206
    sprite('rrb000_04', 7)	# 266207-266213
    sprite('rrb000_05', 7)	# 266214-266220
    sprite('rrb000_06', 7)	# 266221-266227
    sprite('rrb000_07', 7)	# 266228-266234
    sprite('rrb000_08', 7)	# 266235-266241
    sprite('rrb000_09', 7)	# 266242-266248
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
                    clearUponHandler(3)
                    sendToLabel(100)
            if PartnerChar('brc'):
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
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('bma'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('ahe'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
            if PartnerChar('bsu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(250)
                    clearUponHandler(3)
            if PartnerChar('pad'):
                if (SLOT_145 <= 500000):
                    sendToLabel(260)
                    clearUponHandler(3)
            if PartnerChar('rne'):
                if (SLOT_145 <= 500000):
                    sendToLabel(270)
                    clearUponHandler(3)
            if PartnerChar('kym'):
                if (SLOT_145 <= 500000):
                    sendToLabel(280)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 33)
    if SLOT_ReturnVal:
        _gotolabel(20)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(30)
    label(10)
    sprite('rrb610_00', 6)	# 4-9
    GFX_0('rrb610Eff', 0)
    sprite('rrb610_01', 6)	# 10-15
    sprite('rrb610_02', 6)	# 16-21
    sprite('rrb610_03', 6)	# 22-27
    sprite('rrb610_04', 6)	# 28-33
    sprite('rrb610_05', 6)	# 34-39
    sprite('rrb610_06', 6)	# 40-45
    sprite('rrb610_07', 6)	# 46-51
    if SLOT_158:
        if SLOT_108:
            Unknown7006('rrb402_0', 100, 878867058, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rrb520', 100, 895644274, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(11)
    sprite('rrb610_02', 6)	# 52-57
    sprite('rrb610_03', 6)	# 58-63
    sprite('rrb610_04', 6)	# 64-69
    sprite('rrb610_05', 6)	# 70-75
    sprite('rrb610_06', 6)	# 76-81
    sprite('rrb610_07', 6)	# 82-87
    Unknown23018(1)
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('rrb611_00', 6)	# 88-93
    sprite('rrb611_01', 6)	# 94-99
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 100-105
    sprite('rrb611_03', 6)	# 106-111
    sprite('rrb611_04', 6)	# 112-117
    sprite('rrb611_05', 6)	# 118-123
    sprite('rrb611_06', 6)	# 124-129
    sprite('rrb611_07', 6)	# 130-135
    sprite('rrb611_08', 6)	# 136-141
    if SLOT_158:
        if SLOT_108:
            Unknown7006('rrb402_0', 100, 878867058, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rrb522', 100, 895644274, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('rrb611_09', 32767)	# 142-32908
    Unknown23018(1)
    label(30)
    sprite('rrb300_00', 6)	# 32909-32914
    sprite('rrb300_01', 6)	# 32915-32920
    sprite('rrb300_02', 6)	# 32921-32926
    sprite('rrb300_03', 6)	# 32927-32932
    sprite('rrb300_04', 6)	# 32933-32938
    if SLOT_158:
        if SLOT_108:
            Unknown7006('rrb402_0', 100, 878867058, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rrb524', 100, 895644274, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(31)
    sprite('rrb300_04', 6)	# 32939-32944
    if SLOT_97:
        _gotolabel(31)
    sprite('rrb300_05', 6)	# 32945-32950
    sprite('rrb300_06', 6)	# 32951-32956
    sprite('rrb000_00', 3)	# 32957-32959
    sprite('rrb612_00', 6)	# 32960-32965
    SFX_0('019_cloth_b')
    sprite('rrb612_01', 6)	# 32966-32971
    sprite('rrb612_02', 6)	# 32972-32977
    GFX_0('rrb612Eff', 0)
    sprite('rrb612_03', 3)	# 32978-32980
    sprite('rrb612_04', 3)	# 32981-32983
    sprite('rrb612_05', 3)	# 32984-32986
    sprite('rrb612_06', 3)	# 32987-32989
    SFX_0('000_airdash_0')
    sprite('rrb612_07', 3)	# 32990-32992
    sprite('null', 32767)	# 32993-65759
    Unknown23018(1)
    label(40)
    sprite('rrb613_00', 6)	# 65760-65765
    sprite('rrb613_01', 6)	# 65766-65771
    sprite('rrb613_02', 6)	# 65772-65777
    sprite('rrb613_03', 20)	# 65778-65797
    sprite('rrb613_04', 6)	# 65798-65803
    sprite('rrb613_05', 6)	# 65804-65809
    sprite('rrb613_06', 6)	# 65810-65815
    sprite('rrb613_07', 32767)	# 65816-98582
    Unknown18008()
    label(100)
    sprite('rrb300_00', 6)	# 98583-98588
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
    sprite('rrb300_01', 6)	# 98589-98594
    sprite('rrb300_02', 6)	# 98595-98600
    sprite('rrb300_03', 6)	# 98601-98606
    SFX_1('rrb700brg')
    label(101)
    sprite('rrb300_04', 1)	# 98607-98607
    if SLOT_97:
        _gotolabel(101)
    sprite('rrb300_04', 30)	# 98608-98637
    sprite('rrb300_04', 32767)	# 98638-131404
    Unknown21007(24, 40)
    Unknown21011(200)
    label(110)
    sprite('rrb613_00', 6)	# 131405-131410
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('rrb613_01', 6)	# 131411-131416
    sprite('rrb613_02', 6)	# 131417-131422
    sprite('rrb613_03', 20)	# 131423-131442
    sprite('rrb613_04', 6)	# 131443-131448
    sprite('rrb613_05', 6)	# 131449-131454
    SFX_1('rrb700brc')
    sprite('rrb613_06', 6)	# 131455-131460
    label(111)
    sprite('rrb613_07', 1)	# 131461-131461
    if SLOT_97:
        _gotolabel(111)
    sprite('rrb613_07', 30)	# 131462-131491
    sprite('rrb613_07', 32767)	# 131492-164258
    Unknown21007(24, 40)
    Unknown21011(240)
    label(120)
    sprite('rrb300_00', 6)	# 164259-164264
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
    sprite('rrb300_01', 6)	# 164265-164270
    sprite('rrb300_02', 6)	# 164271-164276
    sprite('rrb300_03', 6)	# 164277-164282
    SFX_1('rrb700bes')
    label(121)
    sprite('rrb300_04', 1)	# 164283-164283
    if SLOT_97:
        _gotolabel(121)
    sprite('rrb300_04', 30)	# 164284-164313
    sprite('rrb300_04', 32767)	# 164314-197080
    Unknown21007(24, 40)
    Unknown21011(120)
    label(130)
    sprite('rrb000_00', 1)	# 197081-197081

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('rrb000_00', 7)	# 197082-197088
    sprite('rrb000_01', 7)	# 197089-197095
    sprite('rrb000_02', 7)	# 197096-197102
    sprite('rrb000_03', 7)	# 197103-197109
    sprite('rrb000_04', 7)	# 197110-197116
    sprite('rrb000_05', 7)	# 197117-197123
    sprite('rrb000_06', 7)	# 197124-197130
    sprite('rrb000_07', 7)	# 197131-197137
    sprite('rrb000_08', 7)	# 197138-197144
    sprite('rrb000_09', 7)	# 197145-197151
    gotoLabel(131)
    label(132)
    sprite('rrb611_00', 6)	# 197152-197157
    sprite('rrb611_01', 6)	# 197158-197163
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 197164-197169
    sprite('rrb611_03', 6)	# 197170-197175
    sprite('rrb611_04', 6)	# 197176-197181
    sprite('rrb611_05', 6)	# 197182-197187
    sprite('rrb611_06', 6)	# 197188-197193
    sprite('rrb611_07', 6)	# 197194-197199
    sprite('rrb611_08', 6)	# 197200-197205
    SFX_1('rrb701pbc')
    label(133)
    sprite('rrb611_09', 1)	# 197206-197206
    if SLOT_97:
        _gotolabel(133)
    sprite('rrb611_09', 32767)	# 197207-229973
    Unknown23018(1)
    label(140)
    sprite('rrb611_00', 6)	# 229974-229979
    sprite('rrb611_01', 6)	# 229980-229985
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 229986-229991
    sprite('rrb611_03', 6)	# 229992-229997
    sprite('rrb611_04', 6)	# 229998-230003
    sprite('rrb611_05', 6)	# 230004-230009
    sprite('rrb611_06', 6)	# 230010-230015
    sprite('rrb611_07', 6)	# 230016-230021
    sprite('rrb611_08', 6)	# 230022-230027
    SFX_1('rrb700uhy')
    label(141)
    sprite('rrb611_09', 1)	# 230028-230028
    if SLOT_97:
        _gotolabel(141)
    sprite('rrb611_09', 30)	# 230029-230058
    sprite('rrb611_09', 32767)	# 230059-262825
    Unknown21007(24, 40)
    Unknown21011(270)
    label(150)
    sprite('rrb613_00', 6)	# 262826-262831
    sprite('rrb613_01', 6)	# 262832-262837
    sprite('rrb613_02', 6)	# 262838-262843
    sprite('rrb613_03', 20)	# 262844-262863
    sprite('rrb613_04', 6)	# 262864-262869
    SFX_1('rrb700ugo')
    sprite('rrb613_05', 6)	# 262870-262875
    sprite('rrb613_06', 6)	# 262876-262881
    label(151)
    sprite('rrb613_07', 1)	# 262882-262882
    if SLOT_97:
        _gotolabel(151)
    sprite('rrb613_07', 32767)	# 262883-295649
    Unknown21007(24, 40)
    Unknown21011(120)
    label(160)
    sprite('rrb613_00', 6)	# 295650-295655
    sprite('rrb613_01', 6)	# 295656-295661
    sprite('rrb613_02', 6)	# 295662-295667
    sprite('rrb613_03', 20)	# 295668-295687
    sprite('rrb613_04', 6)	# 295688-295693
    SFX_1('rrb700rwi')
    sprite('rrb613_05', 6)	# 295694-295699
    sprite('rrb613_06', 6)	# 295700-295705
    label(161)
    sprite('rrb613_07', 1)	# 295706-295706
    if SLOT_97:
        _gotolabel(161)
    sprite('rrb613_07', 10)	# 295707-295716
    sprite('rrb613_07', 32767)	# 295717-328483
    Unknown21007(24, 40)
    Unknown21011(120)
    label(170)
    sprite('rrb613_00', 6)	# 328484-328489
    sprite('rrb613_01', 6)	# 328490-328495
    sprite('rrb613_02', 6)	# 328496-328501
    sprite('rrb613_03', 20)	# 328502-328521
    sprite('rrb613_04', 6)	# 328522-328527
    SFX_1('rrb700pag')
    sprite('rrb613_05', 6)	# 328528-328533
    sprite('rrb613_06', 6)	# 328534-328539
    label(171)
    sprite('rrb613_07', 1)	# 328540-328540
    if SLOT_97:
        _gotolabel(171)
    sprite('rrb613_07', 30)	# 328541-328570
    sprite('rrb613_07', 32767)	# 328571-361337
    Unknown21007(24, 40)
    Unknown21011(120)
    label(180)
    sprite('rrb000_00', 1)	# 361338-361338

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('rrb000_00', 7)	# 361339-361345
    sprite('rrb000_01', 7)	# 361346-361352
    sprite('rrb000_02', 7)	# 361353-361359
    sprite('rrb000_03', 7)	# 361360-361366
    sprite('rrb000_04', 7)	# 361367-361373
    sprite('rrb000_05', 7)	# 361374-361380
    sprite('rrb000_06', 7)	# 361381-361387
    sprite('rrb000_07', 7)	# 361388-361394
    sprite('rrb000_08', 7)	# 361395-361401
    sprite('rrb000_09', 7)	# 361402-361408
    gotoLabel(181)
    label(182)
    sprite('rrb611_00', 6)	# 361409-361414
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
    sprite('rrb611_01', 6)	# 361415-361420
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 361421-361426
    sprite('rrb611_03', 6)	# 361427-361432
    sprite('rrb611_04', 6)	# 361433-361438
    sprite('rrb611_05', 6)	# 361439-361444
    sprite('rrb611_06', 6)	# 361445-361450
    sprite('rrb611_07', 6)	# 361451-361456
    sprite('rrb611_08', 6)	# 361457-361462
    SFX_1('rrb701uva')
    sprite('rrb611_09', 32767)	# 361463-394229
    Unknown23018(1)
    label(190)
    sprite('rrb613_00', 6)	# 394230-394235
    sprite('rrb613_01', 6)	# 394236-394241
    sprite('rrb613_02', 6)	# 394242-394247
    sprite('rrb613_03', 20)	# 394248-394267
    sprite('rrb613_04', 6)	# 394268-394273
    sprite('rrb613_05', 6)	# 394274-394279
    SFX_1('rrb700rbl')
    sprite('rrb613_06', 6)	# 394280-394285
    label(191)
    sprite('rrb613_07', 1)	# 394286-394286
    if SLOT_97:
        _gotolabel(191)
    sprite('rrb613_07', 30)	# 394287-394316
    sprite('rrb613_07', 32767)	# 394317-427083
    Unknown21007(24, 40)
    Unknown21011(120)
    label(200)
    sprite('rrb611_00', 6)	# 427084-427089
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
    sprite('rrb611_01', 6)	# 427090-427095
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 427096-427101
    sprite('rrb611_03', 6)	# 427102-427107
    sprite('rrb611_04', 6)	# 427108-427113
    sprite('rrb611_05', 6)	# 427114-427119
    sprite('rrb611_06', 6)	# 427120-427125
    sprite('rrb611_07', 6)	# 427126-427131
    sprite('rrb611_08', 6)	# 427132-427137
    SFX_1('rrb700uyu')
    label(201)
    sprite('rrb611_09', 1)	# 427138-427138
    if SLOT_97:
        _gotolabel(201)
    sprite('rrb611_09', 32767)	# 427139-459905
    Unknown21007(24, 40)
    Unknown21011(240)
    label(210)
    sprite('rrb000_00', 1)	# 459906-459906

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('rrb000_00', 7)	# 459907-459913
    sprite('rrb000_01', 7)	# 459914-459920
    sprite('rrb000_02', 7)	# 459921-459927
    sprite('rrb000_03', 7)	# 459928-459934
    sprite('rrb000_04', 7)	# 459935-459941
    sprite('rrb000_05', 7)	# 459942-459948
    sprite('rrb000_06', 7)	# 459949-459955
    sprite('rrb000_07', 7)	# 459956-459962
    sprite('rrb000_08', 7)	# 459963-459969
    sprite('rrb000_09', 7)	# 459970-459976
    gotoLabel(211)
    label(212)
    sprite('rrb613_00', 6)	# 459977-459982
    sprite('rrb613_01', 6)	# 459983-459988
    sprite('rrb613_02', 6)	# 459989-459994
    sprite('rrb613_03', 20)	# 459995-460014
    sprite('rrb613_04', 6)	# 460015-460020
    SFX_1('rrb701ryn')
    sprite('rrb613_05', 6)	# 460021-460026
    sprite('rrb613_06', 6)	# 460027-460032
    Unknown23018(1)
    sprite('rrb613_07', 32767)	# 460033-492799
    label(220)
    sprite('rrb000_00', 1)	# 492800-492800

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('rrb000_00', 7)	# 492801-492807
    sprite('rrb000_01', 7)	# 492808-492814
    sprite('rrb000_02', 7)	# 492815-492821
    sprite('rrb000_03', 7)	# 492822-492828
    sprite('rrb000_04', 7)	# 492829-492835
    sprite('rrb000_05', 7)	# 492836-492842
    sprite('rrb000_06', 7)	# 492843-492849
    sprite('rrb000_07', 7)	# 492850-492856
    sprite('rrb000_08', 7)	# 492857-492863
    sprite('rrb000_09', 7)	# 492864-492870
    gotoLabel(221)
    label(222)
    sprite('rrb611_00', 6)	# 492871-492876
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
    sprite('rrb611_01', 6)	# 492877-492882
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 492883-492888
    sprite('rrb611_03', 6)	# 492889-492894
    sprite('rrb611_04', 6)	# 492895-492900
    sprite('rrb611_05', 6)	# 492901-492906
    sprite('rrb611_06', 6)	# 492907-492912
    sprite('rrb611_07', 6)	# 492913-492918
    sprite('rrb611_08', 6)	# 492919-492924
    SFX_1('rrb701pla')
    sprite('rrb611_09', 32767)	# 492925-525691
    Unknown23018(1)
    label(230)
    sprite('rrb000_00', 1)	# 525692-525692

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('rrb000_00', 7)	# 525693-525699
    sprite('rrb000_01', 7)	# 525700-525706
    sprite('rrb000_02', 7)	# 525707-525713
    sprite('rrb000_03', 7)	# 525714-525720
    sprite('rrb000_04', 7)	# 525721-525727
    sprite('rrb000_05', 7)	# 525728-525734
    sprite('rrb000_06', 7)	# 525735-525741
    sprite('rrb000_07', 7)	# 525742-525748
    sprite('rrb000_08', 7)	# 525749-525755
    sprite('rrb000_09', 7)	# 525756-525762
    gotoLabel(231)
    label(232)
    sprite('rrb300_00', 6)	# 525763-525768
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
    sprite('rrb300_01', 6)	# 525769-525774
    sprite('rrb300_02', 6)	# 525775-525780
    sprite('rrb300_03', 6)	# 525781-525786
    SFX_1('rrb701bma')
    sprite('rrb300_04', 32767)	# 525787-558553
    Unknown21007(24, 40)
    Unknown23018(1)
    label(240)
    sprite('rrb613_00', 6)	# 558554-558559
    sprite('rrb613_01', 6)	# 558560-558565
    sprite('rrb613_02', 6)	# 558566-558571
    sprite('rrb613_03', 20)	# 558572-558591
    sprite('rrb613_04', 6)	# 558592-558597
    sprite('rrb613_05', 6)	# 558598-558603
    SFX_1('rrb700ahe')
    sprite('rrb613_06', 6)	# 558604-558609
    label(241)
    sprite('rrb613_07', 1)	# 558610-558610
    if SLOT_97:
        _gotolabel(241)
    sprite('rrb613_07', 30)	# 558611-558640
    sprite('rrb613_07', 32767)	# 558641-591407
    Unknown21007(24, 40)
    Unknown21011(120)
    label(250)
    sprite('rrb000_00', 1)	# 591408-591408
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

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
    label(251)
    sprite('rrb000_00', 7)	# 591409-591415
    sprite('rrb000_01', 7)	# 591416-591422
    sprite('rrb000_02', 7)	# 591423-591429
    sprite('rrb000_03', 7)	# 591430-591436
    sprite('rrb000_04', 7)	# 591437-591443
    sprite('rrb000_05', 7)	# 591444-591450
    sprite('rrb000_06', 7)	# 591451-591457
    sprite('rrb000_07', 7)	# 591458-591464
    sprite('rrb000_08', 7)	# 591465-591471
    sprite('rrb000_09', 7)	# 591472-591478
    gotoLabel(251)
    label(252)
    sprite('rrb300_00', 6)	# 591479-591484
    sprite('rrb300_01', 6)	# 591485-591490
    sprite('rrb300_02', 6)	# 591491-591496
    sprite('rrb300_03', 6)	# 591497-591502
    SFX_1('rrb701bsu')
    Unknown23018(1)
    sprite('rrb300_04', 32767)	# 591503-624269
    label(260)
    sprite('rrb613_00', 6)	# 624270-624275
    sprite('rrb613_01', 6)	# 624276-624281
    sprite('rrb613_02', 6)	# 624282-624287
    sprite('rrb613_03', 20)	# 624288-624307
    sprite('rrb613_04', 6)	# 624308-624313
    SFX_1('rrb700pad')
    sprite('rrb613_05', 6)	# 624314-624319
    sprite('rrb613_06', 6)	# 624320-624325
    label(261)
    sprite('rrb613_07', 1)	# 624326-624326
    if SLOT_97:
        _gotolabel(261)
    sprite('rrb613_07', 20)	# 624327-624346
    sprite('rrb613_07', 32767)	# 624347-657113
    Unknown21007(24, 40)
    Unknown21011(270)
    label(270)
    sprite('keep', 1)	# 657114-657114
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                Unknown2005()
        elif (SLOT_38 == 1):
            Unknown2005()
    sprite('rrb611_00', 6)	# 657115-657120
    sprite('rrb611_01', 6)	# 657121-657126
    SFX_3('rrbse_01')
    sprite('rrb611_02', 6)	# 657127-657132
    sprite('rrb611_03', 6)	# 657133-657138
    sprite('rrb611_04', 6)	# 657139-657144
    sprite('rrb611_05', 6)	# 657145-657150
    sprite('rrb611_06', 6)	# 657151-657156
    sprite('rrb611_07', 6)	# 657157-657162
    sprite('rrb611_08', 6)	# 657163-657168
    SFX_1('rrb700rne')
    label(271)
    sprite('rrb611_09', 1)	# 657169-657169
    if SLOT_97:
        _gotolabel(271)
    sprite('rrb611_09', 20)	# 657170-657189
    sprite('rrb611_09', 32767)	# 657190-689956
    Unknown21007(24, 40)
    Unknown21011(120)
    label(280)
    sprite('rrb000_00', 1)	# 689957-689957

    def upon_40():
        clearUponHandler(40)
        sendToLabel(282)
    label(281)
    sprite('rrb000_00', 7)	# 689958-689964
    sprite('rrb000_01', 7)	# 689965-689971
    sprite('rrb000_02', 7)	# 689972-689978
    sprite('rrb000_03', 7)	# 689979-689985
    sprite('rrb000_04', 7)	# 689986-689992
    sprite('rrb000_05', 7)	# 689993-689999
    sprite('rrb000_06', 7)	# 690000-690006
    sprite('rrb000_07', 7)	# 690007-690013
    sprite('rrb000_08', 7)	# 690014-690020
    sprite('rrb000_09', 7)	# 690021-690027
    gotoLabel(281)
    label(282)
    sprite('rrb613_00', 6)	# 690028-690033
    sprite('rrb613_01', 6)	# 690034-690039
    sprite('rrb613_02', 6)	# 690040-690045
    sprite('rrb613_03', 20)	# 690046-690065
    sprite('rrb613_04', 6)	# 690066-690071
    SFX_1('rrb701kym')
    sprite('rrb613_05', 6)	# 690072-690077
    sprite('rrb613_06', 6)	# 690078-690083
    sprite('rrb613_07', 32767)	# 690084-722850
    Unknown23018(1)

@State
def CmnActLose():
    sprite('rrb620_00', 6)	# 1-6
    sprite('rrb620_01', 6)	# 7-12
    Unknown7006('rrb403_0', 100, 878867058, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('rrb620_02', 6)	# 13-18
    sprite('rrb620_03', 6)	# 19-24
    sprite('rrb620_04', 6)	# 25-30
    sprite('rrb620_05', 6)	# 31-36
    sprite('rrb620_06', 32767)	# 37-32803
    Unknown21011(30)