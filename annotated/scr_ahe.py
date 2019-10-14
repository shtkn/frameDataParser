@Subroutine
def ExSkillInit():
    Unknown11091(10)
    Unknown30065(0)

@Subroutine
def InvSkillInit():
    Unknown30065(100)

@Subroutine
def PartnerSkillInit():
    AttackP1(70)
    Unknown11042(1)

@Subroutine
def PreInit():
    Unknown12019('61686500000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
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
    MoveMaxChainRepeat(1)
    Unknown15013(1500)
    Unknown14015(0, 280000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 280000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 250000, -200000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 200000, -100000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 230000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15015(24, 30)
    Unknown14015(-50000, 450000, -200000, 700000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    Unknown14005(1)
    Unknown15009()
    Unknown15013(3000)
    Unknown14015(-50000, 450000, -200000, 700000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15013(1)
    Unknown15021(2000)
    Unknown15016(1, 15, 25)
    Unknown14015(-50000, 400000, 200000, 700000, 500, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CancelNmlAtk5BBB', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('NmlAtk5BBB')
    Unknown14015(-50000, 450000, -200000, 700000, 500, 0)
    Move_EndRegister()
    Move_Register('CancelNmlAtk2B', 0x1)
    Unknown14005(1)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_B)
    Unknown14013('NmlAtk2B')
    Unknown14015(-50000, 400000, 200000, 700000, 500, 0)
    Move_EndRegister()
    Move_Register('CancelCrushAttack', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('CmnActCrushAttack')
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('CancelNmlAtk2C', 0x1)
    Unknown14005(1)
    Move_Input_(0x45)
    Move_Input_(INPUT_PRESS_C)
    Unknown14013('NmlAtk2C')
    Unknown15009()
    Unknown15021(1)
    Unknown14015(0, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(4000)
    Unknown14015(-200000, 300000, -200000, 250000, 250, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(-200000, 300000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15013(4000)
    Unknown14015(-50000, 350000, -350000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5BB', 0x22)
    Unknown14005(1)
    Unknown14015(-50000, 350000, -400000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('HomingActionN', 0x34)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(250)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingActionN', 0x34)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingActionN')
    Unknown15005(100)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction2', 0x31)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(150)
    Unknown15014(500)
    Unknown15013(0)
    Move_EndRegister()
    Move_Register('CancelHomingAction2', 0x31)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction2')
    Unknown15005(10)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction4', 0x33)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(200)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction4', 0x33)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction4')
    Unknown15005(50)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction6', 0x35)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(250)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction6', 0x35)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction6')
    Unknown15005(100)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction8', 0x37)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(150)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction8', 0x37)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction8')
    Unknown15005(10)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction1', 0x30)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(150)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction1', 0x30)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction1')
    Unknown15005(10)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction3', 0x32)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(150)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction3', 0x32)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction3')
    Unknown15005(10)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction7', 0x36)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(200)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction7', 0x36)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction7')
    Unknown15005(50)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingAction9', 0x38)
    Unknown14004(1)
    Move_AirGround_(0x3009)
    Unknown15005(200)
    Unknown15014(500)
    Move_EndRegister()
    Move_Register('CancelHomingAction9', 0x38)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown14013('HomingAction9')
    Unknown15005(50)
    Unknown15014(500)
    Unknown15013(0)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingActionLandN', 0x2b)
    Unknown14005(1)
    Move_AirGround_(0x3086)
    Unknown15014(500)
    Unknown15005(100)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingActionLand4', 0x1)
    Unknown14005(1)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(500)
    Unknown15005(50)
    Unknown15022('58020000e803000000000000e8030000')
    Move_EndRegister()
    Move_Register('HomingActionLand6', 0x1)
    Unknown14005(1)
    Move_Input_(0x79)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(500)
    Unknown15005(50)
    Unknown15022('58020000e803000000000000e8030000')
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
    Move_Register('LandAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 500000, -300000, 220000, 150, 0)
    Move_EndRegister()
    Move_Register('LandAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(50)
    Unknown14015(0, 700000, -300000, 220000, 150, 0)
    Move_EndRegister()
    Move_Register('LandAssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(50)
    Unknown15022('58020000e803000000000000e8030000')
    Unknown14015(0, 700000, -300000, 220000, 100, 0)
    Move_EndRegister()
    Move_Register('LandShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown14015(700000, 1300000, -200000, 600000, 50, 10)
    Move_EndRegister()
    Move_Register('LandShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown14015(700000, 1300000, -200000, 600000, 50, 10)
    Move_EndRegister()
    Move_Register('LandShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(1)
    Unknown14015(700000, 1300000, -200000, 600000, 25, 0)
    Move_EndRegister()
    Move_Register('AirAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown14015(0, 250000, -500000, 50000, 250, 1)
    Move_EndRegister()
    Move_Register('AirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown14015(0, 350000, -500000, 50000, 250, 1)
    Move_EndRegister()
    Move_Register('AirAssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(1)
    Unknown15014(3000)
    Unknown15022('58020000e803000000000000e8030000')
    Unknown14015(0, 350000, -500000, 50000, 100, 1)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown14015(700000, 1300000, -350000, 350000, 50, 10)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown14015(700000, 1300000, -350000, 350000, 50, 10)
    Move_EndRegister()
    Move_Register('AirShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15013(1)
    Unknown14015(700000, 1300000, -200000, 200000, 25, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(0, 200000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(2500)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(0, 200000, -200000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('AntiAir2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('UltimateLandAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateLandAssaultSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateUpper', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(-50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateUpperSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(-50000, 280000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAirAssault', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(0, 350000, -500000, 80000, 500, 1)
    Move_EndRegister()
    Move_Register('UltimateAirAssaultSP', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(0, 350000, -500000, 80000, 500, 1)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(10000)
    Unknown15013(3000)
    Unknown14015(-50000, 400000, -200000, 350000, 250, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5AAA', 'AssaultA', 10000000)
    Unknown15024('NmlAtk2C', 'AssaultA', 10000000)
    Unknown15024('AssaultA', 'HomingActionLand6', 10000000)
    Unknown15024('NmlAtk5AAA', 'UltimateLandAssault', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateLandAssault', 10000000)
    Unknown15024('NmlAtk5AAA', 'UltimateLandAssaultSP', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateLandAssaultSP', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BB', 'CancelNmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BB', 'AirAssaultA', 10000000)
    Unknown15024('NmlAtk5BB', 'AirAssaultB', 10000000)
    Unknown15024('NmlAtk5BBB', 'LandAssaultA', 10000000)
    Unknown15024('NmlAtk5BBB', 'LandAssaultB', 10000000)
    Unknown15024('AssaultB', 'HomingActionLandN', 10000000)
    Unknown15024('NmlAtk5BBB', 'UltimateUpper', 10000000)
    Unknown15024('NmlAtk5BBB', 'UltimateUpperSP', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'AirAssaultA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'AirAssaultB', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'UltimateAirAssault', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'UltimateAirAssaultSP', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AirAssaultA', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5BB', 10000000)
    Unknown15024('NmlAtkAIR5BB', 'UltimateAirAssault', 10000000)
    Unknown15024('NmlAtkAIR5BB', 'UltimateAirAssaultSP', 10000000)
    Unknown12018(0, 'ahe062_01')
    Unknown12018(1, 'ahe062_03')
    Unknown12018(2, 'ahe062_04')
    Unknown12018(3, 'ahe062_05')
    Unknown12018(4, 'ahe062_06')
    Unknown12018(5, 'ahe062_07')
    Unknown12018(6, 'ahe062_09')
    Unknown12018(7, 'ahe040_02')
    Unknown12018(8, 'ahe040_02')
    Unknown12018(9, 'ahe045_02')
    Unknown12018(10, 'ahe062_00')
    Unknown12018(11, 'ahe062_01')
    Unknown12018(12, 'ahe062_03')
    Unknown12018(13, 'ahe062_05')
    Unknown12018(14, 'ahe062_09')
    Unknown12018(15, 'ahe073_01ex')
    Unknown12018(16, 'ahe050_00')
    Unknown12018(17, 'ahe052_00')
    Unknown12018(18, 'ahe054_00')
    Unknown12018(19, 'ahe000_00')
    Unknown12018(20, 'ahe000_00')
    Unknown12018(25, 'ahe063_00')
    Unknown12018(26, 'ahe063_01')
    Unknown12018(27, 'ahe063_02')
    Unknown12018(28, 'ahe063_04')
    Unknown12018(29, 'ahe063_09')
    Unknown12018(24, 'ahe073_01')
    Unknown7010(0, 'ahe000')
    Unknown7010(1, 'ahe001')
    Unknown7010(2, 'ahe002')
    Unknown7010(3, 'ahe003')
    Unknown7010(4, 'ahe004')
    Unknown7010(5, 'ahe005')
    Unknown7010(6, 'ahe006')
    Unknown7010(7, 'ahe007')
    Unknown7010(8, 'ahe008')
    Unknown7010(9, 'ahe009')
    Unknown7010(10, 'ahe010')
    Unknown7010(15, 'ahe015')
    Unknown7010(16, 'ahe016')
    Unknown7010(17, 'ahe017')
    Unknown7010(18, 'ahe018')
    Unknown7010(19, 'ahe019')
    Unknown7010(20, 'ahe020')
    Unknown7010(21, 'ahe021')
    Unknown7010(22, 'ahe022')
    Unknown7010(23, 'ahe023')
    Unknown7010(24, 'ahe024')
    Unknown7010(25, 'ahe025')
    Unknown7010(28, 'ahe028')
    Unknown7010(29, 'ahe029')
    Unknown7010(30, 'ahe030')
    Unknown7010(31, 'ahe031')
    Unknown7010(32, 'ahe032')
    Unknown7010(33, 'ahe033')
    Unknown7010(34, 'ahe034')
    Unknown7010(35, 'ahe035')
    Unknown7010(36, 'ahe036')
    Unknown7010(37, 'ahe037')
    Unknown7010(39, 'ahe039')
    Unknown7010(42, 'ahe042')
    Unknown7010(43, 'ahe043')
    Unknown7010(44, 'ahe044')
    Unknown7010(45, 'ahe045')
    Unknown7010(46, 'ahe046')
    Unknown7010(47, 'ahe047')
    Unknown7010(48, 'ahe048')
    Unknown7010(49, 'ahe049')
    Unknown7010(50, 'ahe050')
    Unknown7010(52, 'ahe052')
    Unknown7010(53, 'ahe053')
    Unknown7010(54, 'ahe100_0')
    Unknown7010(55, 'ahe100_1')
    Unknown7010(56, 'ahe100_2')
    Unknown7010(63, 'ahe101_0')
    Unknown7010(64, 'ahe101_1')
    Unknown7010(65, 'ahe101_2')
    Unknown7010(57, 'ahe102_0')
    Unknown7010(58, 'ahe102_1')
    Unknown7010(59, 'ahe102_2')
    Unknown7010(66, 'ahe103_0')
    Unknown7010(67, 'ahe103_1')
    Unknown7010(68, 'ahe103_2')
    Unknown7010(60, 'ahe104_0')
    Unknown7010(61, 'ahe104_1')
    Unknown7010(62, 'ahe104_2')
    Unknown7010(69, 'ahe105_0')
    Unknown7010(70, 'ahe105_1')
    Unknown7010(71, 'ahe105_2')
    Unknown7010(72, 'ahe150')
    Unknown7010(73, 'ahe151')
    Unknown7010(74, 'ahe152')
    Unknown7010(85, 'ahe153')
    Unknown7010(87, 'ahe154')
    Unknown7010(88, 'ahe155')
    Unknown7010(96, 'ahe161_0')
    Unknown7010(97, 'ahe161_1')
    Unknown7010(92, 'ahe162_0')
    Unknown7010(93, 'ahe162_1')
    Unknown7010(98, 'ahe163_0')
    Unknown7010(99, 'ahe163_1')
    Unknown7010(100, 'ahe164_0')
    Unknown7010(101, 'ahe164_1')
    Unknown7010(105, 'ahe165_0')
    Unknown7010(106, 'ahe165_1')
    Unknown7010(102, 'ahe166_0')
    Unknown7010(103, 'ahe166_1')
    Unknown7010(90, 'ahe167_0')
    Unknown7010(91, 'ahe167_1')
    Unknown7010(107, 'ahe168_0')
    Unknown7010(108, 'ahe168_1')
    Unknown7010(110, 'ahe169_0')
    Unknown7010(111, 'ahe169_1')
    Unknown7010(94, 'ahe400_0')
    Unknown7010(95, 'ahe400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654c616e6441737361756c7400000000000000000000000000')
    Unknown12059('03000000556c74696d6174654c616e6441737361756c7453500000000000000000000000')
    Unknown12059('04000000556c74696d617465557070657200000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465557070657253500000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFinalize():
    if SLOT_37:
        SLOT_5 = 0

@State
def CmnActStand():
    label(0)
    sprite('ahe000_00', 4)	# 1-4	 **attackbox here**
    sprite('ahe000_01', 4)	# 5-8	 **attackbox here**
    sprite('ahe000_02', 4)	# 9-12	 **attackbox here**
    sprite('ahe000_03', 4)	# 13-16	 **attackbox here**
    sprite('ahe000_04', 4)	# 17-20	 **attackbox here**
    sprite('ahe000_05', 4)	# 21-24	 **attackbox here**
    sprite('ahe000_06', 4)	# 25-28	 **attackbox here**
    sprite('ahe000_07', 4)	# 29-32	 **attackbox here**
    sprite('ahe000_08', 4)	# 33-36	 **attackbox here**
    sprite('ahe000_09', 4)	# 37-40	 **attackbox here**
    sprite('ahe000_10', 4)	# 41-44	 **attackbox here**
    sprite('ahe000_11', 4)	# 45-48	 **attackbox here**
    sprite('ahe000_12', 4)	# 49-52	 **attackbox here**
    sprite('ahe000_13', 4)	# 53-56	 **attackbox here**
    sprite('ahe000_14', 4)	# 57-60	 **attackbox here**
    sprite('ahe000_15', 4)	# 61-64	 **attackbox here**
    sprite('ahe000_16', 4)	# 65-68	 **attackbox here**
    sprite('ahe000_17', 4)	# 69-72	 **attackbox here**
    sprite('ahe000_18', 4)	# 73-76	 **attackbox here**
    sprite('ahe000_19', 4)	# 77-80	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ahe003_00', 3)	# 1-3
    sprite('ahe003_01', 3)	# 4-6
    sprite('ahe003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('ahe010_00', 4)	# 1-4
    sprite('ahe010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ahe010_02', 5)	# 1-5
    sprite('ahe010_03', 5)	# 6-10
    sprite('ahe010_04', 5)	# 11-15
    sprite('ahe010_05', 5)	# 16-20
    sprite('ahe010_06', 5)	# 21-25
    sprite('ahe010_07', 5)	# 26-30
    sprite('ahe010_08', 5)	# 31-35
    sprite('ahe010_09', 5)	# 36-40
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ahe013_00', 3)	# 1-3
    sprite('ahe013_01', 3)	# 4-6
    sprite('ahe013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ahe010_01', 4)	# 1-4
    sprite('ahe010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ahe010_00', 4)	# 1-4
    if SLOT_5:
        Unknown1045(0)

@State
def CmnActJumpUpper():
    sprite('ahe020_00', 3)	# 1-3
    sprite('ahe020_01', 3)	# 4-6
    label(0)
    sprite('ahe020_00', 3)	# 7-9
    sprite('ahe020_01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ahe020_02', 3)	# 1-3
    sprite('ahe020_03', 3)	# 4-6
    sprite('ahe020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ahe020_05', 3)	# 1-3
    sprite('ahe020_06', 3)	# 4-6
    label(0)
    sprite('ahe020_07', 3)	# 7-9
    sprite('ahe020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ahe010_01', 2)	# 1-2
    sprite('ahe010_00', 2)	# 3-4

@State
def CmnActLandingStiffLoop():
    sprite('ahe010_01', 4)	# 1-4
    sprite('ahe010_00', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('ahe010_00', 3)	# 1-3
    sprite('ahe010_00', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('null', 60)	# 1-60

@State
def CmnActBWalk():
    label(0)
    sprite('ahe031_00', 3)	# 1-3
    sprite('ahe031_00', 3)	# 4-6
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ahe031_01', 6)	# 7-12
    sprite('ahe031_02', 6)	# 13-18
    sprite('ahe031_03', 6)	# 19-24
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ahe031_04', 6)	# 25-30
    sprite('ahe031_05', 6)	# 31-36
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ahe032_00', 3)	# 1-3
    sprite('ahe032_01', 3)	# 4-6
    label(0)
    sprite('ahe032_02', 3)	# 7-9
    sprite('ahe032_03', 3)	# 10-12
    Unknown8006(100, 1, 0)
    sprite('ahe032_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ahe032_05', 3)	# 1-3
    sprite('ahe032_06', 3)	# 4-6
    sprite('ahe032_07', 3)	# 7-9
    sprite('ahe032_08', 3)	# 10-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown22008(7)
        Unknown1084(1)
        Unknown23001(100, 0)
        Unknown23076()
        sendToLabelUpon(2, 1)
        Unknown28(8, '_NEUTRAL')
    sprite('ahe010_00', 2)	# 1-2
    sprite('ahe033_00', 2)	# 3-4
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ahe033_01', 2)	# 5-6
    label(0)
    sprite('ahe033_00', 2)	# 7-8
    sprite('ahe033_01', 2)	# 9-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe033_02', 2)	# 11-12
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ahe032_05', 2)	# 13-14
    sprite('ahe010_00', 2)	# 15-16

@State
def CmnActBDashLanding():
    sprite('null', 60)	# 1-60

@State
def CmnActAirFDash():
    sprite('ahe035_00', 2)	# 1-2
    sprite('ahe035_01', 2)	# 3-4
    label(0)
    sprite('ahe032_02ex01', 2)	# 5-6
    sprite('ahe032_03ex01', 2)	# 7-8
    sprite('ahe032_04ex01', 2)	# 9-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ahe035_00', 2)	# 1-2
    label(0)
    sprite('ahe033_00ex01', 2)	# 3-4
    sprite('ahe033_01ex01', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ahe050_00', 1)	# 1-1
    sprite('ahe050_01', 1)	# 2-2
    sprite('ahe050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ahe050_01', 1)	# 1-1
    sprite('ahe050_02', 1)	# 2-2
    sprite('ahe050_01', 2)	# 3-4
    sprite('ahe050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ahe050_02', 1)	# 1-1
    sprite('ahe050_02', 1)	# 2-2
    sprite('ahe050_02', 2)	# 3-4
    sprite('ahe050_01', 2)	# 5-6
    sprite('ahe050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ahe050_02', 1)	# 1-1
    sprite('ahe050_03', 1)	# 2-2
    sprite('ahe050_02', 2)	# 3-4
    sprite('ahe050_02', 2)	# 5-6
    sprite('ahe050_01', 2)	# 7-8
    sprite('ahe050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ahe050_03', 1)	# 1-1
    sprite('ahe050_03', 1)	# 2-2
    sprite('ahe050_03', 2)	# 3-4
    sprite('ahe050_02', 2)	# 5-6
    sprite('ahe050_02', 2)	# 7-8
    sprite('ahe050_01', 2)	# 9-10
    sprite('ahe050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ahe052_00', 1)	# 1-1
    sprite('ahe052_01', 1)	# 2-2
    sprite('ahe052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ahe052_01', 1)	# 1-1
    sprite('ahe052_02', 1)	# 2-2
    sprite('ahe052_01', 2)	# 3-4
    sprite('ahe052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ahe052_02', 1)	# 1-1
    sprite('ahe052_02', 1)	# 2-2
    sprite('ahe052_02', 2)	# 3-4
    sprite('ahe052_01', 2)	# 5-6
    sprite('ahe052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ahe052_02', 1)	# 1-1
    sprite('ahe052_03', 1)	# 2-2
    sprite('ahe052_02', 2)	# 3-4
    sprite('ahe052_02', 2)	# 5-6
    sprite('ahe052_01', 2)	# 7-8
    sprite('ahe052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ahe052_03', 1)	# 1-1
    sprite('ahe052_03', 1)	# 2-2
    sprite('ahe052_03', 2)	# 3-4
    sprite('ahe052_02', 2)	# 5-6
    sprite('ahe052_02', 2)	# 7-8
    sprite('ahe052_01', 2)	# 9-10
    sprite('ahe052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ahe054_00', 1)	# 1-1
    sprite('ahe054_01', 1)	# 2-2
    sprite('ahe054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ahe054_01', 1)	# 1-1
    sprite('ahe054_02', 1)	# 2-2
    sprite('ahe054_01', 2)	# 3-4
    sprite('ahe054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ahe054_02', 1)	# 1-1
    sprite('ahe054_02', 1)	# 2-2
    sprite('ahe054_02', 2)	# 3-4
    sprite('ahe054_01', 2)	# 5-6
    sprite('ahe054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ahe054_02', 1)	# 1-1
    sprite('ahe054_03', 1)	# 2-2
    sprite('ahe054_02', 2)	# 3-4
    sprite('ahe054_02', 2)	# 5-6
    sprite('ahe054_01', 2)	# 7-8
    sprite('ahe054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ahe054_03', 1)	# 1-1
    sprite('ahe054_03', 1)	# 2-2
    sprite('ahe054_03', 2)	# 3-4
    sprite('ahe054_02', 2)	# 5-6
    sprite('ahe054_02', 2)	# 7-8
    sprite('ahe054_01', 2)	# 9-10
    sprite('ahe054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ahe062_00', 3)	# 1-3
    label(0)
    sprite('ahe062_01', 3)	# 4-6
    sprite('ahe062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ahe062_03', 2)	# 1-2
    sprite('ahe062_04', 2)	# 3-4

@State
def CmnActBDownDown():
    sprite('ahe062_05', 3)	# 1-3
    sprite('ahe062_06', 3)	# 4-6
    label(0)
    sprite('ahe062_07', 3)	# 7-9
    sprite('ahe062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ahe062_09', 2)	# 1-2
    sprite('ahe062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('null', 60)	# 1-60

@State
def CmnActBDownLoop():
    sprite('null', 60)	# 1-60

@State
def CmnActBDown2Stand():
    sprite('null', 60)	# 1-60

@State
def CmnActFDownUpper():
    sprite('ahe063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ahe063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ahe063_02', 3)	# 1-3
    sprite('ahe063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ahe063_04', 3)	# 1-3
    sprite('ahe063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('ahe063_06', 4)	# 1-4
    sprite('ahe063_07', 3)	# 5-7
    sprite('ahe063_08', 3)	# 8-10
    sprite('ahe063_09', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('ahe063_09', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ahe064_00', 5)	# 1-5
    sprite('ahe064_01', 5)	# 6-10
    sprite('ahe064_02', 5)	# 11-15
    sprite('ahe064_03', 5)	# 16-20

@State
def CmnActVDownUpper():
    sprite('ahe062_00', 3)	# 1-3
    label(0)
    sprite('ahe062_01', 3)	# 4-6
    sprite('ahe062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ahe062_03', 3)	# 1-3
    sprite('ahe062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('ahe062_05', 3)	# 1-3
    sprite('ahe062_06', 3)	# 4-6
    label(0)
    sprite('ahe062_07', 3)	# 7-9
    sprite('ahe062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ahe062_09', 2)	# 1-2
    sprite('ahe062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('ahe072_00', 3)	# 1-3
    label(0)
    sprite('ahe072_01', 3)	# 4-6
    sprite('ahe072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ahe074_00', 3)	# 1-3
    sprite('ahe074_01', 3)	# 4-6
    sprite('ahe074_02', 3)	# 7-9
    sprite('ahe074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('null', 60)	# 1-60

@State
def CmnActFreeze():
    sprite('ahe062_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ahe073_00', 3)	# 1-3
    sprite('ahe073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ahe073_02', 3)	# 1-3
    sprite('ahe073_03', 3)	# 4-6
    label(0)
    sprite('ahe063_02', 3)	# 7-9
    sprite('ahe063_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ahe070_00', 3)	# 1-3
    label(0)
    sprite('ahe070_01', 4)	# 4-7
    sprite('ahe070_02', 4)	# 8-11
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ahe070_03', 4)	# 1-4
    sprite('ahe070_04', 4)	# 5-8
    sprite('ahe070_05', 4)	# 9-12
    sprite('ahe070_06', 4)	# 13-16
    sprite('ahe070_07', 4)	# 17-20
    sprite('ahe070_08', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ahe070_09', 4)	# 1-4
    sprite('ahe070_10', 2)	# 5-6
    sprite('ahe070_11', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ahe113_00', 3)	# 1-3
    sprite('ahe113_01', 3)	# 4-6
    sprite('ahe113_02', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('ahe113_00', 3)	# 1-3
    sprite('ahe113_01', 3)	# 4-6
    sprite('ahe113_02', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('ahe113_00', 3)	# 1-3
    sprite('ahe113_01', 3)	# 4-6
    sprite('ahe113_02', 9)	# 7-15

@State
def CmnActUkemiLandF():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandB():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandN():
    sprite('ahe112_00', 2)	# 1-2
    sprite('ahe112_01', 2)	# 3-4
    sprite('ahe112_02', 2)	# 5-6
    sprite('ahe112_03', 2)	# 7-8
    sprite('ahe112_04', 3)	# 9-11
    sprite('ahe112_05', 3)	# 12-14
    sprite('ahe112_06', 3)	# 15-17
    sprite('ahe112_07', 3)	# 18-20
    label(0)
    sprite('ahe020_07', 3)	# 21-23
    sprite('ahe020_08', 3)	# 24-26
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('ahe010_00', 2)	# 1-2
    sprite('ahe010_01', 2)	# 3-4
    sprite('ahe010_02', 4)	# 5-8
    sprite('ahe010_01', 4)	# 9-12
    sprite('ahe010_00', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('ahe040_00', 3)	# 1-3
    sprite('ahe040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ahe040_02', 3)	# 1-3
    sprite('ahe040_03', 3)	# 4-6
    sprite('ahe040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ahe040_01', 3)	# 1-3
    sprite('ahe040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('ahe040_02', 3)	# 1-3
    sprite('ahe040_03', 3)	# 4-6
    sprite('ahe040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ahe040_01', 3)	# 1-3
    sprite('ahe040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ahe040_00', 3)	# 1-3
    sprite('ahe040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ahe040_02', 3)	# 1-3
    sprite('ahe040_03', 3)	# 4-6
    sprite('ahe040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ahe040_01', 3)	# 1-3
    sprite('ahe040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('ahe040_02', 3)	# 1-3
    sprite('ahe040_03', 3)	# 4-6
    sprite('ahe040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ahe040_01', 3)	# 1-3
    sprite('ahe040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ahe043_00', 3)	# 1-3
    sprite('ahe043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ahe043_02', 3)	# 1-3
    sprite('ahe043_03', 3)	# 4-6
    sprite('ahe043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ahe043_01', 3)	# 1-3
    sprite('ahe043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('ahe043_02', 3)	# 1-3
    sprite('ahe043_03', 3)	# 4-6
    sprite('ahe043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ahe043_01', 3)	# 1-3
    sprite('ahe043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ahe045_00', 3)	# 1-3
    sprite('ahe045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ahe045_02', 3)	# 1-3
    sprite('ahe045_03', 3)	# 4-6
    sprite('ahe045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ahe045_01', 3)	# 1-3
    sprite('ahe045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('ahe045_02', 3)	# 1-3
    sprite('ahe045_03', 3)	# 4-6
    sprite('ahe045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ahe045_01', 3)	# 1-3
    sprite('ahe045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ahe040_04', 2)	# 1-2
    sprite('ahe040_04', 2)	# 3-4
    sprite('ahe040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ahe040_02', 4)	# 6-9
    sprite('ahe040_01', 4)	# 10-13
    sprite('ahe040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ahe043_04', 2)	# 1-2
    sprite('ahe043_04', 2)	# 3-4
    sprite('ahe043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ahe043_02', 4)	# 6-9
    sprite('ahe043_01', 4)	# 10-13
    sprite('ahe043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ahe045_04', 2)	# 1-2
    sprite('ahe045_04', 2)	# 3-4
    sprite('ahe045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ahe045_02', 4)	# 6-9
    sprite('ahe045_01', 4)	# 10-13
    sprite('ahe045_00', 4)	# 14-17

@State
def CmnActGuardBreakStand():
    sprite('null', 60)	# 1-60

@State
def CmnActGuardBreakCrouch():
    sprite('null', 60)	# 1-60

@State
def CmnActGuardBreakAir():
    sprite('null', 60)	# 1-60

@State
def CmnActAirTurn():
    sprite('ahe025_00', 4)	# 1-4
    sprite('ahe025_01', 4)	# 5-8
    sprite('ahe025_00ex01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('ahe040_02', 1)	# 1-1
    sprite('ahe040_01', 3)	# 2-4
    sprite('ahe040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('ahe201_00', 3)	# 1-3
    sprite('ahe201_05', 3)	# 4-6
    sprite('ahe201_06', 3)	# 7-9
    sprite('ahe201_07', 3)	# 10-12	 **attackbox here**
    sprite('ahe201_08', 4)	# 13-16
    sprite('ahe201_09', 4)	# 17-20
    sprite('ahe201_10', 4)	# 21-24
    sprite('ahe201_11', 4)	# 25-28

@State
def CmnActAirLockWait():
    sprite('null', 60)	# 1-60

@State
def CmnActAirLockReject():
    sprite('null', 60)	# 1-60

@State
def CmnActLandSpin():
    sprite('null', 60)	# 1-60

@State
def CmnActLandSpinDown():
    sprite('null', 60)	# 1-60

@State
def CmnActVertSpin():
    sprite('null', 60)	# 1-60

@State
def CmnActSlideAir():
    label(0)
    sprite('ahe077_00', 2)	# 1-2
    sprite('ahe077_01', 2)	# 3-4
    sprite('ahe077_00ex00', 2)	# 5-6
    sprite('ahe077_01ex00', 2)	# 7-8
    sprite('ahe077_00ex01', 2)	# 9-10
    sprite('ahe077_01ex01', 2)	# 11-12
    sprite('ahe077_00ex02', 2)	# 13-14
    sprite('ahe077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ahe077_02', 4)	# 1-4
    label(0)
    sprite('ahe077_03', 3)	# 5-7
    sprite('ahe077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ahe077_05', 5)	# 1-5
    sprite('ahe077_06', 4)	# 6-9

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
    sprite('ahe333_00', 3)	# 1-3
    sprite('ahe333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ahe333_02', 3)	# 1-3
    label(0)
    sprite('ahe333_03', 3)	# 4-6
    sprite('ahe333_04', 3)	# 7-9
    sprite('ahe333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('ahe333_06', 4)	# 5-8
    sprite('ahe333_07', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('ahe333_08', 3)	# 1-3
    sprite('ahe333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ahe333_02', 3)	# 1-3
    label(0)
    sprite('ahe333_03', 3)	# 4-6
    sprite('ahe333_04', 3)	# 7-9
    sprite('ahe333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('ahe333_09', 4)	# 5-8
    sprite('ahe333_10', 4)	# 9-12
    sprite('ahe020_04', 3)	# 13-15
    sprite('ahe020_05', 3)	# 16-18
    sprite('ahe020_06', 3)	# 19-21
    label(0)
    sprite('ahe020_07', 3)	# 22-24
    sprite('ahe020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ahe333_00', 3)	# 1-3
    sprite('ahe333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ahe333_02', 3)	# 1-3
    label(0)
    sprite('ahe333_03', 3)	# 4-6
    sprite('ahe333_04', 3)	# 7-9
    sprite('ahe333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('ahe333_06', 4)	# 5-8
    sprite('ahe333_07', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('ahe333_08', 3)	# 1-3
    sprite('ahe333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ahe333_02', 3)	# 1-3
    label(0)
    sprite('ahe333_03', 3)	# 4-6
    sprite('ahe333_04', 3)	# 7-9
    sprite('ahe333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('ahe333_09', 4)	# 5-8
    sprite('ahe333_10', 4)	# 9-12
    sprite('ahe020_04', 3)	# 13-15
    sprite('ahe020_05', 3)	# 16-18
    sprite('ahe020_06', 3)	# 19-21
    label(0)
    sprite('ahe020_07', 3)	# 22-24
    sprite('ahe020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('ahe333_00', 3)	# 1-3
    sprite('ahe333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ahe333_02', 3)	# 1-3
    label(0)
    sprite('ahe333_03', 3)	# 4-6
    sprite('ahe333_04', 3)	# 7-9
    sprite('ahe333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ahe333_06', 3)	# 1-3
    sprite('ahe333_07', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('ahe333_08', 3)	# 1-3
    sprite('ahe333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ahe333_02', 3)	# 1-3
    label(0)
    sprite('ahe333_03', 3)	# 4-6
    sprite('ahe333_04', 3)	# 7-9
    sprite('ahe333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ahe333_09', 3)	# 1-3
    sprite('ahe333_10', 3)	# 4-6
    sprite('ahe020_04', 3)	# 7-9
    sprite('ahe020_05', 3)	# 10-12
    sprite('ahe020_06', 3)	# 13-15
    label(0)
    sprite('ahe020_07', 3)	# 16-18
    sprite('ahe020_08', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
    label(0)
    sprite('null', 1)	# 1-1
    Unknown2017(0)
    Unknown2034(0)
    teleportRelativeY(0)
    gotoLabel(0)

@State
def CmnActChangePartnerAppeal():
    sprite('null', 60)	# 1-60

@State
def CmnActChangePartnerAppealAir():
    sprite('null', 60)	# 1-60

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown23027()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 7)	# 1-7
    sprite('null', 1)	# 8-8
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sprite('ahe251_05', 4)	# 9-12
    sprite('ahe276_00', 4)	# 13-16
    sprite('ahe276_01', 5)	# 17-21
    sprite('ahe276_02', 5)	# 22-26
    sprite('ahe276_03', 2)	# 27-28
    sprite('ahe276_04', 3)	# 29-31	 **attackbox here**
    sprite('ahe276_04', 32767)	# 32-32798	 **attackbox here**
    label(1)
    sprite('keep', 2)	# 32799-32800
    Unknown1019(10)
    sprite('ahe406_05', 3)	# 32801-32803
    Unknown8000(100, 1, 1)
    sprite('ahe406_06', 5)	# 32804-32808	 **attackbox here**
    sprite('ahe406_07', 5)	# 32809-32813
    sprite('ahe010_02', 3)	# 32814-32816
    Unknown1084(1)
    sprite('ahe010_01', 3)	# 32817-32819
    sprite('ahe010_00', 3)	# 32820-32822

@State
def CmnActChangePartnerQuickIn():
    sprite('ahe032_02', 3)	# 1-3
    sprite('ahe032_03', 3)	# 4-6
    sprite('ahe032_04', 3)	# 7-9
    sprite('ahe032_05', 5)	# 10-14
    sprite('ahe032_06', 5)	# 15-19
    sprite('ahe032_07', 5)	# 20-24
    sprite('ahe032_08', 5)	# 25-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ahe033_00', 3)	# 1-3
    sprite('ahe033_01', 3)	# 4-6
    sprite('ahe033_00', 3)	# 7-9
    sprite('ahe033_01', 3)	# 10-12
    sprite('ahe033_00', 3)	# 13-15
    sprite('ahe033_01', 3)	# 16-18
    sprite('ahe033_00', 3)	# 19-21
    sprite('ahe033_01', 3)	# 22-24
    sprite('ahe033_00', 3)	# 25-27
    sprite('ahe033_01', 3)	# 28-30
    sprite('keep', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ahe010_00', 3)	# 1-3
    sprite('ahe033_00', 3)	# 4-6
    sprite('ahe033_01', 3)	# 7-9
    label(0)
    sprite('ahe033_00', 3)	# 10-12
    sprite('ahe033_01', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe033_02', 2)	# 16-17
    sprite('ahe032_05', 2)	# 18-19
    sprite('ahe010_00', 2)	# 20-21

@State
def CmnActChangeReturnAppeal():
    sprite('ahe350_00', 6)	# 1-6	 **attackbox here**
    sprite('ahe350_01', 6)	# 7-12	 **attackbox here**
    sprite('ahe350_02', 6)	# 13-18	 **attackbox here**
    sprite('ahe350_03', 6)	# 19-24	 **attackbox here**
    sprite('ahe350_04', 6)	# 25-30	 **attackbox here**
    sprite('ahe350_05', 6)	# 31-36	 **attackbox here**
    sprite('ahe350_06', 6)	# 37-42	 **attackbox here**
    sprite('ahe350_07', 6)	# 43-48	 **attackbox here**
    sprite('ahe350_03', 6)	# 49-54	 **attackbox here**
    sprite('ahe350_04', 6)	# 55-60	 **attackbox here**
    sprite('ahe350_01', 5)	# 61-65	 **attackbox here**
    sprite('ahe350_00', 5)	# 66-70	 **attackbox here**
    sprite('ahe000_00', 5)	# 71-75	 **attackbox here**
    sprite('ahe000_00', 30)	# 76-105	 **attackbox here**

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
    sprite('ahe020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ahe020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ahe010_01', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('PartnerSkillInit')
        loopRelated(17, 29)

        def upon_17():
            sendToLabel(1)

        def upon_STATE_END():
            Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
            Unknown21012('6168653430355f636972636c655f65666600000000000000000000000000000020000000')
            Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
    sprite('ahe403_00', 3)	# 1-3
    sprite('ahe403_01', 3)	# 4-6
    GFX_0('ahe403_footcircle_eff', 100)
    Unknown7006('ahe203_0', 100, 845506657, 828322608, 0, 0, 100, 845506657, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ahe403_02', 3)	# 7-9
    sprite('ahe403_03', 3)	# 10-12
    label(0)
    sprite('ahe403_01', 3)	# 13-15
    sprite('ahe403_02', 3)	# 16-18
    sprite('ahe403_03', 3)	# 19-21
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe403_04', 2)	# 22-23
    sprite('ahe403_05', 2)	# 24-25
    sprite('ahe403_06', 3)	# 26-28
    GFX_0('ShotEx_Obj', 0)
    Unknown23029(1, 4036, 0)
    GFX_0('ahe405_circle_eff', 0)
    GFX_0('ahe405_shot_eff', 0)
    sprite('ahe403_07', 3)	# 29-31
    sprite('ahe403_08', 3)	# 32-34
    sprite('ahe403_09', 3)	# 35-37
    sprite('ahe403_06', 3)	# 38-40
    sprite('ahe403_07', 3)	# 41-43
    sprite('ahe403_08', 3)	# 44-46
    sprite('ahe403_09', 3)	# 47-49
    sprite('ahe403_06', 3)	# 50-52
    Recovery()
    Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
    Unknown21012('6168653430355f636972636c655f65666600000000000000000000000000000020000000')
    Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
    sprite('ahe403_07', 3)	# 53-55
    sprite('ahe403_08', 3)	# 56-58
    sprite('ahe403_09', 3)	# 59-61
    sprite('ahe403_06', 3)	# 62-64
    sprite('ahe403_10', 3)	# 65-67
    sprite('ahe403_11', 3)	# 68-70

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Unknown11058('0000000001000000000000000000000000000000')
        AttackP2(80)
        GroundedHitstunAnimation(1)
        AirUntechableTime(70)
        AirPushbackY(38000)
        callSubroutine('PartnerSkillInit')
        Unknown48('19000000020000003400000016000000020000001e000000')
        if SLOT_52:
            Unknown2016(350)
        else:
            Unknown2016(-1)
        Unknown2004(1, 0)
    sprite('ahe010_02', 1)	# 1-1
    sprite('ahe231_00', 1)	# 2-2
    sprite('ahe231_01', 1)	# 3-3
    sprite('ahe231_04', 2)	# 4-5
    sprite('ahe231_05', 2)	# 6-7
    physicsXImpulse(20000)
    sprite('ahe231_06', 2)	# 8-9
    Unknown18009(0)
    Unknown1019(50)
    SFX_0('004_swing_grap_1_2')
    SFX_1('ahe107_0')
    sprite('ahe231_07ex', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('ahe231_08ex', 3)	# 13-15	 **attackbox here**
    Unknown1019(50)
    sprite('ahe231_08', 5)	# 16-20	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('ahe231_09', 6)	# 21-26
    Unknown1019(0)
    sprite('ahe231_10', 6)	# 27-32
    sprite('ahe231_11', 6)	# 33-38
    sprite('ahe000_00', 5)	# 39-43	 **attackbox here**
    ExitState()

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        Unknown9154(28)
        AirUntechableTime(70)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(32000)
        Hitstop(20)
        Unknown11056(0)
        callSubroutine('PartnerSkillInit')
        loopRelated(17, 6)

        def upon_17():
            sendToLabel(1)
        Unknown2004(1, 0)
    sprite('ahe400_00', 3)	# 1-3
    sprite('ahe400_01', 3)	# 4-6
    sprite('ahe400_02', 3)	# 7-9
    sprite('ahe400_03', 3)	# 10-12
    label(0)
    sprite('ahe400_01', 3)	# 13-15
    sprite('ahe400_02', 3)	# 16-18
    sprite('ahe400_03', 3)	# 19-21
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe400_04', 2)	# 22-23
    physicsXImpulse(25000)
    Unknown8009(0)
    SFX_3('ahese_03')
    Unknown2015(175)
    Unknown7006('ahe201_0', 100, 845506657, 828322096, 0, 0, 100, 845506657, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ahe400_04', 1)	# 24-24
    Unknown1019(150)
    Unknown8006(100, 1, 0)
    sprite('ahe400_05', 1)	# 25-25
    sprite('ahe400_05', 2)	# 26-27
    Unknown1019(200)
    sprite('ahe400_06', 2)	# 28-29	 **attackbox here**
    RefreshMultihit()
    GFX_0('ahe400_attack_eff', 100)
    Unknown38(8, 1)
    GFX_0('ahe400_dust_eff', 100)
    Unknown8006(100, 1, 0)

    def upon_ON_HIT_OR_BLOCK():
        Unknown2037(1)
        clearUponHandler(10)
        sendToLabel(2)

    def upon_12():
        SLOT_51 = 1
        clearUponHandler(12)
    sprite('ahe400_07', 2)	# 30-31	 **attackbox here**
    label(2)
    sprite('ahe200_06', 3)	# 32-34	 **attackbox here**
    if SLOT_2:
        Unknown23029(8, 5031, 0)
    clearUponHandler(10)
    clearUponHandler(12)
    StartMultihit()
    Recovery()
    Unknown1019(50)
    sprite('ahe200_07', 5)	# 35-39
    Unknown1019(50)
    sprite('ahe200_08', 5)	# 40-44
    Unknown1019(50)
    sprite('ahe200_09', 5)	# 45-49
    Unknown1019(50)
    Unknown14077(0)
    sprite('ahe200_10', 6)	# 50-55
    Unknown1019(50)
    sprite('ahe200_11', 6)	# 56-61
    Unknown1084(1)

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
    Unknown2036(93, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-250000)
    Unknown1019(4)
    label(0)
    sprite('ahe020_07', 3)	# 3-5
    sprite('ahe020_08', 3)	# 6-8
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
        AttackLevel_(5)
        Damage(2000)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(38000)
        AirUntechableTime(120)
        Hitstop(20)
        Unknown11001(0, -2, 3)
        Unknown11056(0)
        Unknown2016(250)
        loopRelated(17, 62)

        def upon_17():
            sendToLabel(1)
        Unknown2004(1, 0)
    sprite('ahe400_00', 3)	# 1-3
    setInvincible(1)
    sprite('ahe400_01', 3)	# 4-6
    GFX_0('ahe430_hold_eff', 100)
    sprite('ahe430_00', 3)	# 7-9
    sprite('ahe430_01', 3)	# 10-12
    sprite('ahe430_02', 3)	# 13-15
    sprite('ahe430_03', 3)	# 16-18
    sprite('ahe430_04', 3)	# 19-21
    sprite('ahe400_01', 3)	# 22-24
    sprite('ahe430_00', 3)	# 25-27
    sprite('ahe430_01', 3)	# 28-30
    sprite('ahe430_02', 3)	# 31-33
    sprite('ahe430_03', 3)	# 34-36
    sprite('ahe430_04', 3)	# 37-39
    label(0)
    sprite('ahe400_01', 2)	# 40-41
    sprite('ahe430_00', 2)	# 42-43
    sprite('ahe430_01', 2)	# 44-45
    sprite('ahe430_02', 2)	# 46-47
    sprite('ahe430_03', 2)	# 48-49
    sprite('ahe430_04', 2)	# 50-51
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe400_04', 2)	# 52-53
    physicsXImpulse(20000)
    Unknown8009(0)
    SFX_1('ahe251')
    sprite('ahe400_04', 1)	# 54-54
    Unknown1019(200)
    Unknown8006(100, 1, 0)
    sprite('ahe400_05', 1)	# 55-55
    sprite('ahe400_05', 2)	# 56-57
    Unknown1019(200)
    SFX_3('ahese_03')
    sprite('ahe430_05', 3)	# 58-60	 **attackbox here**
    RefreshMultihit()
    GFX_0('ahe430_attack_eff', 100)
    GFX_0('ahe430_magical_eff', 100)
    Unknown8006(100, 1, 0)
    GFX_0('ahe_DDD', 100)

    def upon_ON_HIT_OR_BLOCK():
        Unknown2037(1)
        clearUponHandler(10)
        sendToLabel(2)

    def upon_12():
        clearUponHandler(12)
        SFX_0('025_cleanhit_grap')
    sprite('ahe430_06', 3)	# 61-63	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('ahe430_07', 3)	# 64-66	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('ahe430_08', 3)	# 67-69	 **attackbox here**
    Unknown8006(100, 1, 0)
    label(2)
    sprite('keep', 3)	# 70-72
    StartMultihit()
    GFX_0('ahe_DDD_End', 100)
    sprite('ahe200_06', 6)	# 73-78	 **attackbox here**
    setInvincible(0)
    StartMultihit()
    Unknown1019(40)
    sprite('ahe200_07', 6)	# 79-84
    Unknown1019(40)
    sprite('ahe200_08', 6)	# 85-90
    Unknown1019(40)
    sprite('ahe200_09', 6)	# 91-96
    Unknown1019(40)
    sprite('ahe200_10', 6)	# 97-102
    Unknown1019(40)
    sprite('ahe200_11', 6)	# 103-108
    Unknown1084(1)

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2500)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirPushbackX(80000)
        AirPushbackY(45000)
        AirUntechableTime(120)
        Unknown9310(26)
        Hitstop(30)
        Unknown11001(0, -2, 3)
        Unknown11056(0)
        Unknown2016(250)
        loopRelated(17, 62)

        def upon_17():
            sendToLabel(1)
        Unknown2004(1, 0)
    sprite('ahe400_00', 3)	# 1-3
    setInvincible(1)
    sprite('ahe400_01', 3)	# 4-6
    GFX_0('ahe430_hold_eff', 100)
    sprite('ahe430_00', 3)	# 7-9
    sprite('ahe430_01', 3)	# 10-12
    sprite('ahe430_02', 3)	# 13-15
    sprite('ahe430_03', 3)	# 16-18
    sprite('ahe430_04', 3)	# 19-21
    sprite('ahe400_01', 3)	# 22-24
    sprite('ahe430_00', 3)	# 25-27
    sprite('ahe430_01', 3)	# 28-30
    sprite('ahe430_02', 3)	# 31-33
    sprite('ahe430_03', 3)	# 34-36
    sprite('ahe430_04', 3)	# 37-39
    sprite('ahe400_01', 2)	# 40-41
    sprite('ahe430_00', 2)	# 42-43
    sprite('ahe430_01', 2)	# 44-45
    sprite('ahe430_02', 2)	# 46-47
    sprite('ahe430_03', 2)	# 48-49
    sprite('ahe430_04', 2)	# 50-51
    sprite('ahe400_01', 2)	# 52-53
    sprite('ahe430_00', 2)	# 54-55
    sprite('ahe430_01', 2)	# 56-57
    sprite('ahe430_02', 2)	# 58-59
    sprite('ahe430_03', 2)	# 60-61
    sprite('ahe430_04', 2)	# 62-63
    label(0)
    sprite('ahe400_01', 1)	# 64-64
    sprite('ahe430_00', 1)	# 65-65
    sprite('ahe430_01', 1)	# 66-66
    sprite('ahe430_02', 1)	# 67-67
    sprite('ahe430_03', 1)	# 68-68
    sprite('ahe430_04', 1)	# 69-69
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe400_04', 2)	# 70-71
    physicsXImpulse(20000)
    Unknown8009(0)
    SFX_1('ahe251')
    sprite('ahe400_04', 1)	# 72-72
    Unknown1019(200)
    Unknown8006(100, 1, 0)
    sprite('ahe400_05', 1)	# 73-73
    sprite('ahe400_05', 2)	# 74-75
    Unknown1019(200)
    SFX_3('ahese_03')
    sprite('ahe430_05', 3)	# 76-78	 **attackbox here**
    RefreshMultihit()
    GFX_0('ahe430_attack_eff', 100)
    GFX_0('ahe430_magical_eff', 100)
    Unknown8006(100, 1, 0)

    def upon_12():
        clearUponHandler(12)
        Unknown2037(1)
        SFX_0('025_cleanhit_grap')

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        sendToLabel(2)
    sprite('ahe430_06', 3)	# 79-81	 **attackbox here**
    GFX_0('ahe_DDD', 100)
    Unknown8006(100, 1, 0)
    sprite('ahe430_07', 3)	# 82-84	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('ahe430_08', 3)	# 85-87	 **attackbox here**
    Unknown8006(100, 1, 0)
    label(2)
    sprite('keep', 3)	# 88-90
    StartMultihit()
    GFX_0('ahe_DDD_End', 100)
    if SLOT_2:
        sendToLabel(100)
    sprite('ahe200_06', 6)	# 91-96	 **attackbox here**
    setInvincible(0)
    StartMultihit()
    Unknown1019(40)
    sprite('ahe200_07', 6)	# 97-102
    Unknown1019(40)
    sprite('ahe200_08', 6)	# 103-108
    Unknown1019(40)
    sprite('ahe200_09', 6)	# 109-114
    Unknown1019(40)
    sprite('ahe200_10', 6)	# 115-120
    Unknown1019(40)
    sprite('ahe200_11', 6)	# 121-126
    Unknown1084(1)
    ExitState()
    label(100)
    sprite('ahe200_06', 5)	# 127-131	 **attackbox here**
    StartMultihit()
    setInvincible(1)
    sprite('ahe600_00', 5)	# 132-136
    Unknown8006(100, 1, 0)
    Unknown1019(50)
    sprite('ahe600_01', 5)	# 137-141
    sprite('ahe600_00', 5)	# 142-146
    Unknown1019(50)
    sprite('ahe600_01', 5)	# 147-151
    sprite('ahe600_00', 5)	# 152-156
    Unknown1019(50)
    sprite('ahe600_01', 5)	# 157-161
    sprite('ahe600_00', 5)	# 162-166
    Unknown1019(50)
    sprite('ahe600_01', 5)	# 167-171
    sprite('ahe032_06', 3)	# 172-174
    teleportRelativeX(20000)
    Unknown1084(1)
    Unknown1047(3000)
    sprite('ahe032_07', 3)	# 175-177
    sprite('ahe032_08', 3)	# 178-180
    sprite('ahe274_07', 4)	# 181-184
    sprite('ahe274_08', 4)	# 185-188
    sprite('ahe271_06', 4)	# 189-192
    sprite('ahe271_07', 6)	# 193-198
    sprite('ahe271_08', 6)	# 199-204
    sprite('ahe271_09', 6)	# 205-210
    ExitState()

@State
def CmnActChangeRequest():
    sprite('null', 60)	# 1-60

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 8)	# 121-128
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sprite('ahe251_05', 4)	# 129-132
    sprite('ahe276_00', 4)	# 133-136
    sprite('ahe276_01', 5)	# 137-141
    sprite('ahe276_02', 5)	# 142-146
    sprite('ahe276_03', 2)	# 147-148
    sprite('ahe276_04', 3)	# 149-151	 **attackbox here**
    sendToLabelUpon(2, 9)
    sprite('ahe276_04', 32767)	# 152-32918	 **attackbox here**
    label(9)
    sprite('keep', 2)	# 32919-32920
    Unknown1019(10)
    sprite('ahe406_05', 6)	# 32921-32926
    Unknown8000(100, 1, 1)
    sprite('ahe406_06', 6)	# 32927-32932	 **attackbox here**
    sprite('ahe406_07', 6)	# 32933-32938
    sprite('ahe010_02', 4)	# 32939-32942
    Unknown1084(1)
    sprite('ahe010_01', 4)	# 32943-32946
    sprite('ahe010_00', 4)	# 32947-32950

@State
def CmnActChangeReturnAppealBurst():
    sprite('ahe010_02', 3)	# 1-3
    sprite('ahe010_01', 3)	# 4-6
    sprite('ahe010_00', 3)	# 7-9
    sprite('ahe000_00', 3)	# 10-12	 **attackbox here**
    sprite('ahe300_00', 4)	# 13-16
    sprite('ahe300_01', 4)	# 17-20	 **attackbox here**
    sprite('ahe300_02', 4)	# 21-24
    sprite('ahe300_02ex', 4)	# 25-28
    sprite('ahe300_03', 4)	# 29-32
    sprite('ahe300_03ex', 4)	# 33-36
    sprite('ahe300_04', 4)	# 37-40
    sprite('ahe300_04ex1', 4)	# 41-44
    sprite('ahe300_04ex2', 8)	# 45-52	 **attackbox here**
    sprite('ahe300_05', 4)	# 53-56
    sprite('ahe300_06', 4)	# 57-60
    loopRest()

@Subroutine
def AHE_SousaiArmor():
    GuardPoint_(1)
    Unknown22019('0100000001000000000000000100000000000000')
    Unknown22039(1)
    Unknown22031(20, 20)

    def upon_52():
        if Unknown23036():
            Unknown4004('4f6666736574456666000000000000000000000000000000000000000000000066000000')
        elif Unknown23037():
            Unknown22031(0, -1)
            Unknown4004('53686f74536f757361694566660000000000000000000000000000000000000066000000')

@Subroutine
def AHE_SousaiArmorShotRef():
    AttackP1(90)
    GuardPoint_(1)
    Unknown22019('0100000001000000000000000100000000000000')
    Unknown22039(1)
    Unknown22031(20, 20)

    def upon_52():
        if Unknown23036():
            Unknown4004('4f6666736574456666000000000000000000000000000000000000000000000066000000')
        elif Unknown23037():
            Unknown22031(0, -1)
            Unknown4004('53686f74536f757361694566660000000000000000000000000000000000000066000000')
            GFX_0('Shot_Obj', 102)
            Unknown23029(1, 4035, 0)

@Subroutine
def InitArcanaBound():
    Unknown11056(0)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(80000)
    AirPushbackY(1000)
    YImpluseBeforeWallbounce(100)
    Unknown9178(1)
    WallbounceReboundTime(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(15000)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
        callSubroutine('HoseiPlus')
    sprite('ahe200_01', 2)	# 1-2
    sprite('ahe200_02', 2)	# 3-4
    sprite('ahe200_03', 2)	# 5-6
    physicsXImpulse(20000)
    sprite('ahe200_05', 1)	# 7-7
    Unknown1019(50)
    Unknown7009(1)
    SFX_0('004_swing_grap_1_0')
    sprite('ahe200_06', 5)	# 8-12	 **attackbox here**
    Unknown1019(50)
    sprite('ahe200_07', 3)	# 13-15
    Recovery()
    Unknown2063()
    Unknown1084(1)
    sprite('ahe200_08', 3)	# 16-18
    sprite('ahe200_09', 3)	# 19-21
    sprite('ahe200_10', 3)	# 22-24
    sprite('ahe200_11', 3)	# 25-27

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(-2500)
        AirPushbackY(15000)
        PushbackX(-19800)
        AirUntechableTime(21)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('ahe270_00', 2)	# 1-2
    sprite('ahe270_01', 2)	# 3-4
    sprite('ahe270_02', 2)	# 5-6
    SFX_0('004_swing_grap_1_1')
    Unknown7009(4)
    sprite('ahe270_03', 3)	# 7-9	 **attackbox here**
    sprite('ahe270_04', 2)	# 10-11
    Recovery()
    Unknown2063()
    sprite('ahe270_05', 3)	# 12-14
    sprite('ahe270_06', 3)	# 15-17
    SLOT_59 = 1
    sprite('ahe270_07', 5)	# 18-22
    sprite('ahe270_08', 5)	# 23-27

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(15000)
        AirUntechableTime(21)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        Unknown2004(1, 0)
    sprite('ahe270_05', 2)	# 1-2
    Unknown23183('6168653237305f3036000000000000000000000000000000000000000000000003000000020000003b000000')
    SLOT_59 = 0
    teleportRelativeX(-100000)
    sprite('ahe271_00', 2)	# 3-4
    sprite('ahe271_01', 3)	# 5-7
    sprite('ahe271_02', 2)	# 8-9
    Unknown7009(3)
    SFX_0('004_swing_grap_1_0')
    sprite('ahe271_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('ahe271_04', 3)	# 13-15
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ahe271_05', 5)	# 16-20
    sprite('ahe271_06', 5)	# 21-25
    sprite('ahe271_07', 5)	# 26-30
    sprite('ahe271_08', 5)	# 31-35
    sprite('ahe271_09', 5)	# 36-40

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2500)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(12000)
        AirPushbackY(32000)
        JumpCancel_(0)
        Unknown11001(0, -4, 1)
        Unknown2037(0)
    sprite('ahe271_05', 3)	# 1-3
    sprite('ahe000_00', 2)	# 4-5	 **attackbox here**
    sprite('ahe274_01', 2)	# 6-7
    sprite('ahe274_02', 2)	# 8-9
    physicsXImpulse(30000)
    SFX_0('005_swing_grap_2_0')
    SFX_1('ahe110')
    sprite('ahe274_03', 5)	# 10-14	 **attackbox here**
    Unknown1019(50)
    sprite('ahe274_04', 5)	# 15-19
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ahe274_04', 3)	# 20-22
    sprite('ahe274_05', 5)	# 23-27
    sprite('ahe274_06', 5)	# 28-32
    sprite('ahe274_07', 5)	# 33-37
    sprite('ahe274_08', 5)	# 38-42
    sprite('ahe271_09', 6)	# 43-48

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(1)
        AirPushbackY(15000)
        WhiffCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('HoseiPlus')
    sprite('ahe204_00', 2)	# 1-2
    sprite('ahe204_01', 1)	# 3-3
    sprite('ahe204_01', 2)	# 4-5
    SFX_0('003_swing_grap_0_1')
    Unknown7009(0)
    sprite('ahe204_02', 3)	# 6-8	 **attackbox here**
    sprite('ahe204_03', 4)	# 9-12
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ahe204_01', 4)	# 13-16
    sprite('ahe204_00', 4)	# 17-20

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackY(20000)
        PushbackX(15300)
        AirUntechableTime(24)
        Unknown11056(0)

        def upon_3():
            if SLOT_51:
                if SLOT_2:
                    clearUponHandler(3)
                    clearUponHandler(17)
                    sendToLabel(1)
            elif (not SLOT_112):
                if (not CheckInput(0xa)):
                    SLOT_51 = 1
                    setInvincible(0)
            Unknown48('19000000020000003500000016000000020000001e000000')
            if SLOT_53:
                Unknown2016(300)
            else:
                Unknown2016(-1)
        loopRelated(17, 36)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            AttackLevel_(5)
            Damage(2200)
            callSubroutine('InitArcanaBound')
            AirUntechableTime(29)
            AirHitstunAfterWallbounce(40)
            Hitstop(20)
            Unknown11001(0, 5, 10)
            SLOT_52 = 1
            Unknown23159('AN_NmlAtk5B_Tame')
            sendToLabel(1)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown2004(1, 0)
        callSubroutine('AHE_SousaiArmorShotRef')
        Unknown1112('')

        def upon_STATE_END():
            if Unknown46(4):
                Unknown13(4)
            if Unknown46(5):
                Unknown13(5)
        callSubroutine('HoseiPlus')
        if SLOT_112:
            Unknown48('19000000020000003a00000016000000020000001e000000')
            if (not SLOT_58):
                if random_(2, 0, 90):
                    SLOT_51 = 1
            else:
                SLOT_51 = 1
    sprite('ahe201_00', 3)	# 1-3
    sprite('ahe201_01', 2)	# 4-5
    sprite('ahe201_01', 1)	# 6-6
    SLOT_2 = 1
    sprite('ahe201_02', 3)	# 7-9
    GFX_0('ahe201_Charge_Loop_Eff', 100)
    Unknown38(4, 1)
    sprite('ahe201_03', 3)	# 10-12
    setInvincible(1)
    sprite('ahe201_04', 3)	# 13-15
    label(0)
    sprite('ahe201_02', 3)	# 16-18
    sprite('ahe201_03', 3)	# 19-21
    sprite('ahe201_04', 3)	# 22-24
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe201_05', 2)	# 25-26
    physicsXImpulse(20000)
    if SLOT_52:
        physicsXImpulse(30000)
    Unknown13(4)
    GFX_0('ahe201_move_dust_Eff', 100)
    Unknown38(5, 1)
    sprite('ahe201_06', 2)	# 27-28
    Unknown1019(200)
    SFX_0('004_swing_grap_1_2')
    if (not SLOT_52):
        SFX_1('ahe106_0')
    else:
        Unknown7006('ahe106_1', 100, 828729441, 845100592, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ahe201_07', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown13(5)
        sendToLabel(2)
    sprite('ahe201_07', 3)	# 32-34	 **attackbox here**
    setInvincible(0)
    if (not SLOT_52):
        Unknown1019(75)
    else:
        Unknown1019(90)
    Unknown13(5)
    label(2)
    sprite('ahe201_08', 6)	# 35-40
    Unknown23183('6168653230315f30380000000000000000000000000000000000000000000000080000000200000034000000')
    setInvincible(0)
    clearUponHandler(10)
    Recovery()
    Unknown2063()
    Unknown1019(25)
    sprite('ahe201_09', 6)	# 41-46
    Unknown23183('6168653230315f30390000000000000000000000000000000000000000000000080000000200000034000000')
    Unknown1019(50)
    sprite('ahe201_10', 6)	# 47-52
    Unknown23183('6168653230315f31300000000000000000000000000000000000000000000000080000000200000034000000')
    Unknown1019(0)
    sprite('ahe201_11', 6)	# 53-58
    Unknown23183('6168653230315f31310000000000000000000000000000000000000000000000080000000200000034000000')

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown11058('0100000000000000000000000000000000000000')
        GroundedHitstunAnimation(1)
        AirUntechableTime(24)
        AirPushbackY(-65000)
        Unknown9190(1)
        Unknown9118(25)
        Unknown2037(0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
            callSubroutine('DeriveHomingCancelTiming')

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(1)
        Unknown21015('6168653237335f61747461636b5f68616e645f65666600000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b5f62675f656666000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b315f6566660000000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b31625f65666600000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b325f6566660000000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b5f666c6173685f656666000000000000000000a913000000000000')

    def upon_STATE_END():
        Unknown21015('6168653237335f61747461636b5f68616e645f65666600000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b5f62675f656666000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b315f6566660000000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b31625f65666600000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b325f6566660000000000000000000000000000a913000000000000')
        Unknown21015('6168653237335f61747461636b5f666c6173685f656666000000000000000000a913000000000000')
sprite('ahe201_09', 3)	# 1-3
sprite('ahe273_00', 3)	# 4-6
Unknown7006('ahe109_0', 100, 828729441, 828324144, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
sprite('ahe273_01', 2)	# 7-8
Unknown47('030000000200000013000000000000000a000000020000000c000000')
if (SLOT_12 > 25000):
    physicsXImpulse(25000)
physicsYImpulse(8000)
setGravity(1000)
sprite('ahe273_02', 2)	# 9-10
Unknown14070('CancelNmlAtk5BBB')
Unknown14070('CancelNmlAtk2B')
callSubroutine('DeriveHomingCancelInput')
GFX_0('ahe273_attack_eff', 100)
sprite('ahe273_03', 2)	# 11-12
Unknown1019(75)
sprite('ahe273_04', 2)	# 13-14
SFX_0('004_swing_grap_1_0')
SFX_3('ahese_00')
sprite('ahe273_05', 3)	# 15-17	 **attackbox here**
sprite('ahe273_06', 3)	# 18-20	 **attackbox here**
Recovery()
Unknown2063()
sprite('ahe273_07', 3)	# 21-23
Unknown1019(50)
sprite('keep', 32767)	# 24-32790
label(1)
sprite('ahe010_02', 4)	# 32791-32794
callSubroutine('DeriveHomingCancelClear')
if SLOT_2:
    Unknown14072('CancelNmlAtk5BBB')
    Unknown14072('CancelNmlAtk2B')
sprite('ahe010_01', 4)	# 32795-32798
Unknown14071('CancelNmlAtk5BBB')
Unknown14071('CancelNmlAtk2B')
sprite('ahe010_00', 4)	# 32799-32802
endState()

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        GroundedHitstunAnimation(1)
        Damage(2000)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        Unknown9310(1)
        Unknown11058('0000000000000000010000000000000000000000')
        HitLow(2)
    sprite('ahe400_04', 3)	# 1-3
    physicsXImpulse(30000)
    sprite('ahe272_00', 2)	# 4-5
    Unknown1019(50)
    sprite('ahe272_01', 2)	# 6-7
    Unknown1019(50)
    sprite('ahe272_00', 2)	# 8-9
    Unknown1019(50)
    sprite('ahe272_01', 2)	# 10-11
    Unknown1019(50)
    sprite('ahe272_02', 3)	# 12-14	 **attackbox here**
    physicsXImpulse(20000)
    Unknown8003(100, 1, 1)
    Unknown7006('ahe108_0', 100, 828729441, 828323888, 0, 0, 100, 828729441, 845101104, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ahe272_03', 3)	# 15-17
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ahe272_03', 3)	# 18-20
    Unknown1019(50)
    sprite('ahe272_03', 2)	# 21-22
    Unknown1019(50)
    sprite('ahe064_00', 3)	# 23-25
    Unknown1084(1)
    sprite('ahe064_01', 3)	# 26-28
    sprite('ahe064_02', 3)	# 29-31
    sprite('ahe064_03', 3)	# 32-34

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        callSubroutine('HoseiPlus')
    sprite('ahe230_00', 3)	# 1-3
    sprite('ahe230_01', 3)	# 4-6
    SFX_0('003_swing_grap_0_0')
    Unknown7009(0)
    sprite('ahe230_02', 3)	# 7-9	 **attackbox here**
    sprite('ahe230_03', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('ahe230_04', 4)	# 13-16
    sprite('ahe230_05', 4)	# 17-20
    sprite('ahe230_06', 4)	# 21-24

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Unknown11058('0000000001000000000000000000000000000000')
        AttackP2(75)
        GroundedHitstunAnimation(1)
        AirUntechableTime(26)
        AirPushbackY(38000)

        def upon_3():
            if SLOT_51:
                if SLOT_2:
                    clearUponHandler(3)
                    clearUponHandler(17)
                    sendToLabel(1)
            elif (not SLOT_112):
                if (not CheckInput(0xa)):
                    SLOT_51 = 1
                    setInvincible(0)
            Unknown48('19000000020000003400000016000000020000001e000000')
            if SLOT_52:
                Unknown2016(350)
            else:
                Unknown2016(-1)
            callSubroutine('HoseiPlus')
            if SLOT_112:
                Unknown48('19000000020000003a00000016000000020000001e000000')
                if (not SLOT_58):
                    if random_(2, 0, 90):
                        SLOT_51 = 1
                else:
                    SLOT_51 = 1
        loopRelated(17, 25)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            AttackLevel_(4)
            Damage(2300)
            AttackP2(95)
            Hitstop(20)
            Unknown11001(0, 5, 10)
            AirPushbackY(45000)
            YImpluseBeforeWallbounce(1000)
            AirUntechableTime(55)
            HitJumpCancel(0)
            GroundedHitstunAnimation(13)
            AirHitstunAnimation(13)
            Unknown23159('AN_NmlAtk2B_Tame')
            sendToLabel(2)

        def upon_ON_HIT_OR_BLOCK():
            callSubroutine('DeriveHomingCancelTiming')

        def upon_STATE_END():
            if Unknown46(4):
                Unknown13(4)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        callSubroutine('AHE_SousaiArmorShotRef')
        Unknown2004(1, 0)
    sprite('ahe010_02', 2)	# 1-2
    sprite('ahe231_00', 2)	# 3-4
    sprite('ahe231_01', 2)	# 5-6
    SLOT_2 = 1
    sprite('ahe231_02', 3)	# 7-9
    setInvincible(1)
    GFX_0('ahe231_Charge_Loop_Eff', 100)
    Unknown38(4, 1)
    sprite('ahe231_03', 3)	# 10-12
    label(0)
    sprite('ahe231_01', 3)	# 13-15
    sprite('ahe231_02', 3)	# 16-18
    sprite('ahe231_03', 3)	# 19-21
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe231_04', 3)	# 22-24
    setInvincible(0)
    Unknown13(4)
    sprite('ahe231_05', 2)	# 25-26
    physicsXImpulse(20000)
    sprite('ahe231_06', 2)	# 27-28
    Unknown18009(0)
    Unknown1019(50)
    SFX_0('004_swing_grap_1_2')
    SFX_1('ahe107_0')
    sprite('ahe231_07', 3)	# 29-31	 **attackbox here**
    RefreshMultihit()
    sprite('ahe231_08', 3)	# 32-34	 **attackbox here**
    Unknown1019(50)
    sprite('ahe231_09', 5)	# 35-39
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ahe231_10', 5)	# 40-44
    sprite('ahe231_11', 5)	# 45-49
    sprite('ahe000_00', 3)	# 50-52	 **attackbox here**
    sprite('ahe010_00', 3)	# 53-55
    Unknown18009(1)
    sprite('ahe010_01', 3)	# 56-58
    ExitState()
    label(2)
    sprite('ahe231_04', 3)	# 59-61
    Unknown13(4)
    sprite('ahe231_05', 2)	# 62-63
    physicsXImpulse(20000)
    sprite('ahe231_06', 2)	# 64-65
    Unknown18009(0)
    Unknown1019(50)
    SFX_0('004_swing_grap_1_2')
    callSubroutine('DeriveHomingCancelInput')
    Unknown7006('ahe107_1', 100, 828729441, 845100848, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ahe231_07', 3)	# 66-68	 **attackbox here**
    RefreshMultihit()
    physicsYImpulse(1000)
    Unknown8001(0, 100)
    sprite('ahe231_08', 6)	# 69-74	 **attackbox here**
    Unknown1019(50)
    physicsYImpulse(8000)
    setGravity(1300)
    sendToLabelUpon(2, 3)
    sprite('ahe231_09', 5)	# 75-79
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ahe231_10', 32767)	# 80-32846
    label(3)
    sprite('ahe000_00', 5)	# 32847-32851	 **attackbox here**
    setInvincible(0)
    Unknown1019(0)
    callSubroutine('DeriveHomingCancelClear')
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ahe010_00', 5)	# 32852-32856
    Unknown18009(1)
    sprite('ahe010_01', 5)	# 32857-32861
    ExitState()

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(15000)
        AirUntechableTime(30)
        AttackP1(90)
        HitLow(2)
        callSubroutine('HoseiPlus')
    sprite('ahe232_00', 3)	# 1-3
    sprite('ahe232_01', 3)	# 4-6
    sprite('ahe232_02', 3)	# 7-9
    sprite('ahe232_03', 3)	# 10-12
    physicsXImpulse(10000)
    Unknown7009(5)
    sprite('ahe232_04', 3)	# 13-15	 **attackbox here**
    Unknown1019(50)
    SFX_0('004_swing_grap_1_1')
    sprite('ahe232_05', 4)	# 16-19
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('ahe232_06', 4)	# 20-23
    Unknown1019(50)
    sprite('ahe232_07', 4)	# 24-27
    Unknown1019(50)
    sprite('ahe232_08', 4)	# 28-31
    Unknown1084(1)
    sprite('ahe232_09', 4)	# 32-35
    sprite('ahe232_10', 4)	# 36-39

@Subroutine
def NoLanding():
    if Unknown23145('NHomingDash'):
        clearUponHandler(2)
    if Unknown23145('HomingDash'):
        clearUponHandler(2)

@Subroutine
def HoseiPlus():
    if (not SLOT_4):
        if Unknown23145('NHomingDash'):
            AttackP2(100)
        if Unknown23145('HomingDash'):
            AttackP2(100)
        if Unknown23145('HomingLandDash'):
            AttackP2(100)

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        loopRelated(17, 24)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        callSubroutine('HomingCancel')
        HitOrBlockJumpCancel(1)
        callSubroutine('NoLanding')
        callSubroutine('HoseiPlus')
    sprite('ahe250_00', 3)	# 1-3
    sprite('ahe250_01', 2)	# 4-5
    sprite('ahe250_02', 2)	# 6-7
    SFX_0('003_swing_grap_0_0')
    Unknown7009(3)
    sprite('ahe250_03', 6)	# 8-13	 **attackbox here**
    Unknown28(2, 'CmnActJumpLanding')
    sprite('ahe250_04', 3)	# 14-16
    Recovery()
    Unknown2063()
    label(0)
    sprite('ahe250_03', 3)	# 17-19	 **attackbox here**
    StartMultihit()
    sprite('ahe250_04', 3)	# 20-22
    StartMultihit()
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 3)	# 23-25
    StartMultihit()
    sprite('ahe250_05', 3)	# 26-28
    StartMultihit()

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(29)
        AirPushbackX(13000)
        AirPushbackY(15000)
        HitOrBlockCancel('NmlAtkAIR5B')
        callSubroutine('HomingCancel')
        loopRelated(17, 24)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        HitOrBlockJumpCancel(1)

        def upon_STATE_END():
            Unknown21015('6168653237335f61747461636b5f68616e645f65666600000000000000000000a913000000000000')
            Unknown21015('6168653237335f61747461636b5f62675f656666000000000000000000000000a913000000000000')
            Unknown21015('6168653237335f61747461636b315f6566660000000000000000000000000000a913000000000000')
            Unknown21015('6168653237335f61747461636b31625f65666600000000000000000000000000a913000000000000')
            Unknown21015('6168653237335f61747461636b325f6566660000000000000000000000000000a913000000000000')
            Unknown21015('6168653237335f61747461636b5f666c6173685f656666000000000000000000a913000000000000')
    sprite('ahe273_01', 3)	# 1-3
    sprite('ahe273_02', 2)	# 4-5
    GFX_0('ahe273_attack_eff', 100)
    sprite('ahe273_03', 2)	# 6-7
    sprite('ahe273_04', 2)	# 8-9
    SFX_0('004_swing_grap_1_0')
    Unknown7009(4)
    SFX_3('ahese_00')
    sprite('ahe273_05', 3)	# 10-12	 **attackbox here**
    sprite('ahe273_06', 3)	# 13-15	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('ahe273_07', 32767)	# 16-32782
    label(1)
    sprite('keep', 3)	# 32783-32785
    sprite('keep', 3)	# 32786-32788

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(12000)
        HitOrBlockCancel('NmlAtkAIR5BB')
        callSubroutine('HomingCancel')
        HitOrBlockJumpCancel(1)
        loopRelated(17, 28)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        callSubroutine('NoLanding')
        callSubroutine('HoseiPlus')
    sprite('ahe251_00', 3)	# 1-3
    sprite('ahe251_01', 3)	# 4-6
    sprite('ahe251_02', 2)	# 7-8
    Unknown7009(4)
    SFX_0('003_swing_grap_0_1')
    Unknown28(2, 'CmnActJumpLanding')
    sprite('ahe251_03', 10)	# 9-18	 **attackbox here**
    sprite('ahe251_04', 32767)	# 19-32785
    Recovery()
    Unknown2063()
    label(1)
    sprite('ahe251_05', 3)	# 32786-32788
    sprite('ahe251_06', 3)	# 32789-32791

@State
def NmlAtkAIR5BB():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirPushbackY(-40000)
        AirUntechableTime(40)
        callSubroutine('HomingCancel')
    sprite('ahe251_05', 3)	# 1-3
    sprite('ahe276_00', 2)	# 4-5
    sprite('ahe276_01', 2)	# 6-7
    sprite('ahe276_02', 2)	# 8-9
    sprite('ahe276_03', 2)	# 10-11
    SFX_0('004_swing_grap_1_2')
    Unknown7009(5)
    sprite('ahe276_04', 3)	# 12-14	 **attackbox here**
    sprite('ahe276_05', 6)	# 15-20
    Recovery()
    Unknown2063()
    sprite('ahe276_06', 6)	# 21-26
    sprite('ahe276_07', 6)	# 27-32
    sprite('ahe276_08', 6)	# 33-38

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown2004(1, 0)
    sprite('ahe200_00', 3)	# 1-3
    sprite('ahe202_00', 6)	# 4-9
    tag_voice(1, 'ahe156_0', 'ahe156_1', '', '')
    sprite('ahe202_01', 6)	# 10-15
    sprite('ahe202_02', 2)	# 16-17
    sprite('ahe202_03', 2)	# 18-19
    sprite('ahe202_04', 2)	# 20-21
    SFX_0('004_swing_grap_1_1')
    sprite('ahe202_05', 3)	# 22-24	 **attackbox here**
    sprite('ahe202_06', 3)	# 25-27
    sprite('ahe202_07', 3)	# 28-30
    sprite('ahe202_08', 3)	# 31-33
    sprite('ahe271_06', 3)	# 34-36
    sprite('ahe271_07', 4)	# 37-40
    sprite('ahe271_08', 4)	# 41-44
    sprite('ahe271_09', 4)	# 45-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ahe202_06', 3)	# 1-3
    sprite('ahe202_07', 3)	# 4-6
    sprite('ahe202_08', 3)	# 7-9
    sprite('ahe271_09', 3)	# 10-12
    sprite('ahe000_00', 3)	# 13-15	 **attackbox here**
    sprite('ahe200_00', 3)	# 16-18
    sprite('ahe200_01', 3)	# 19-21
    sprite('ahe200_02', 3)	# 22-24
    sprite('ahe200_03', 3)	# 25-27
    physicsXImpulse(15000)
    sprite('ahe200_05', 2)	# 28-29
    Unknown1019(50)
    tag_voice(0, 'ahe157_0', 'ahe157_1', '', '')
    sprite('ahe200_06', 5)	# 30-34	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('ahe200_07', 3)	# 35-37
    sprite('ahe200_08', 3)	# 38-40
    sprite('ahe200_09', 3)	# 41-43
    sprite('ahe200_10', 3)	# 44-46
    sprite('ahe200_11', 3)	# 47-49
    label(0)
    sprite('ahe000_00', 4)	# 50-53	 **attackbox here**
    sprite('ahe000_01', 4)	# 54-57	 **attackbox here**
    sprite('ahe000_02', 4)	# 58-61	 **attackbox here**
    sprite('ahe000_03', 4)	# 62-65	 **attackbox here**
    sprite('ahe000_04', 4)	# 66-69	 **attackbox here**
    sprite('ahe000_05', 4)	# 70-73	 **attackbox here**
    sprite('ahe000_06', 4)	# 74-77	 **attackbox here**
    sprite('ahe000_07', 4)	# 78-81	 **attackbox here**
    sprite('ahe000_08', 4)	# 82-85	 **attackbox here**
    sprite('ahe000_09', 4)	# 86-89	 **attackbox here**
    sprite('ahe000_10', 4)	# 90-93	 **attackbox here**
    sprite('ahe000_11', 4)	# 94-97	 **attackbox here**
    sprite('ahe000_12', 4)	# 98-101	 **attackbox here**
    sprite('ahe000_13', 4)	# 102-105	 **attackbox here**
    sprite('ahe000_14', 4)	# 106-109	 **attackbox here**
    sprite('ahe000_15', 4)	# 110-113	 **attackbox here**
    sprite('ahe000_16', 4)	# 114-117	 **attackbox here**
    sprite('ahe000_17', 4)	# 118-121	 **attackbox here**
    sprite('ahe000_18', 4)	# 122-125	 **attackbox here**
    sprite('ahe000_19', 4)	# 126-129	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 130-130

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ahe231_00', 2)	# 1-2
    sprite('ahe231_01', 2)	# 3-4
    sprite('ahe231_04', 3)	# 5-7
    sprite('ahe231_05', 2)	# 8-9
    physicsXImpulse(10000)
    sprite('ahe231_06', 2)	# 10-11
    Unknown1019(50)
    sprite('ahe231_07', 3)	# 12-14	 **attackbox here**
    sprite('ahe231_08', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    Unknown1019(50)
    sprite('ahe231_08', 2)	# 18-19	 **attackbox here**
    StartMultihit()
    sprite('ahe231_09', 5)	# 20-24
    Unknown1019(0)
    sprite('ahe231_10', 5)	# 25-29
    sprite('ahe231_11', 5)	# 30-34
    sprite('ahe000_00', 3)	# 35-37	 **attackbox here**
    label(0)
    sprite('ahe000_00', 4)	# 38-41	 **attackbox here**
    sprite('ahe000_01', 4)	# 42-45	 **attackbox here**
    sprite('ahe000_02', 4)	# 46-49	 **attackbox here**
    sprite('ahe000_03', 4)	# 50-53	 **attackbox here**
    sprite('ahe000_04', 4)	# 54-57	 **attackbox here**
    sprite('ahe000_05', 4)	# 58-61	 **attackbox here**
    sprite('ahe000_06', 4)	# 62-65	 **attackbox here**
    sprite('ahe000_07', 4)	# 66-69	 **attackbox here**
    sprite('ahe000_08', 4)	# 70-73	 **attackbox here**
    sprite('ahe000_09', 4)	# 74-77	 **attackbox here**
    sprite('ahe000_10', 4)	# 78-81	 **attackbox here**
    sprite('ahe000_11', 4)	# 82-85	 **attackbox here**
    sprite('ahe000_12', 4)	# 86-89	 **attackbox here**
    sprite('ahe000_13', 4)	# 90-93	 **attackbox here**
    sprite('ahe000_14', 4)	# 94-97	 **attackbox here**
    sprite('ahe000_15', 4)	# 98-101	 **attackbox here**
    sprite('ahe000_16', 4)	# 102-105	 **attackbox here**
    sprite('ahe000_17', 4)	# 106-109	 **attackbox here**
    sprite('ahe000_18', 4)	# 110-113	 **attackbox here**
    sprite('ahe000_19', 4)	# 114-117	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 118-118

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)

        def upon_11():
            GFX_0('XhitEff_Arcana', -1)
    sprite('ahe000_00', 5)	# 1-5	 **attackbox here**
    sprite('ahe271_05', 5)	# 6-10
    sprite('ahe274_01', 6)	# 11-16
    sprite('ahe274_02', 3)	# 17-19
    physicsXImpulse(15000)
    sprite('ahe274_03', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    tag_voice(0, 'ahe158_0', 'ahe158_1', '', '')
    sprite('ahe274_03', 2)	# 23-24	 **attackbox here**
    StartMultihit()
    sprite('ahe274_04', 5)	# 25-29
    sprite('ahe274_05', 3)	# 30-32
    sprite('ahe274_06', 3)	# 33-35
    sprite('ahe274_07', 3)	# 36-38
    sprite('ahe274_08', 3)	# 39-41
    sprite('ahe271_06', 5)	# 42-46
    sprite('ahe271_07', 5)	# 47-51
    sprite('ahe271_08', 5)	# 52-56
    sprite('ahe271_09', 4)	# 57-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown23027()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown2003(1)
            Unknown1084(1)
            sendToLabel(100)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    sprite('ahe406_00', 1)	# 26-26
    Unknown1086(22)
    teleportRelativeX(-300000)
    Unknown1007(1100000)
    Unknown1084(1)
    physicsXImpulse(7500)
    physicsYImpulse(-45000)
    Unknown1043()
    sprite('ahe406_02', 3)	# 27-29
    GFX_0('ahe406_attack_eff', 0)
    sprite('ahe406_03', 3)	# 30-32	 **attackbox here**
    sprite('ahe406_04', 3)	# 33-35	 **attackbox here**
    sprite('ahe406_03', 3)	# 36-38	 **attackbox here**
    Unknown1043()
    sprite('ahe406_04', 3)	# 39-41	 **attackbox here**
    sprite('ahe406_03', 3)	# 42-44	 **attackbox here**
    RefreshMultihit()
    sprite('ahe406_04', 32767)	# 45-32811	 **attackbox here**
    Unknown23027()
    label(100)
    sprite('ahe406_05', 3)	# 32812-32814
    Unknown21012('6168653430365f61747461636b5f65666600000000000000000000000000000020000000')
    sprite('ahe406_06', 3)	# 32815-32817	 **attackbox here**
    sprite('ahe406_07', 3)	# 32818-32820
    label(0)
    sprite('ahe000_00', 4)	# 32821-32824	 **attackbox here**
    sprite('ahe000_01', 4)	# 32825-32828	 **attackbox here**
    sprite('ahe000_02', 4)	# 32829-32832	 **attackbox here**
    sprite('ahe000_03', 4)	# 32833-32836	 **attackbox here**
    sprite('ahe000_04', 4)	# 32837-32840	 **attackbox here**
    sprite('ahe000_05', 4)	# 32841-32844	 **attackbox here**
    sprite('ahe000_06', 4)	# 32845-32848	 **attackbox here**
    sprite('ahe000_07', 4)	# 32849-32852	 **attackbox here**
    sprite('ahe000_08', 4)	# 32853-32856	 **attackbox here**
    sprite('ahe000_09', 4)	# 32857-32860	 **attackbox here**
    sprite('ahe000_10', 4)	# 32861-32864	 **attackbox here**
    sprite('ahe000_11', 4)	# 32865-32868	 **attackbox here**
    sprite('ahe000_12', 4)	# 32869-32872	 **attackbox here**
    sprite('ahe000_13', 4)	# 32873-32876	 **attackbox here**
    sprite('ahe000_14', 4)	# 32877-32880	 **attackbox here**
    sprite('ahe000_15', 4)	# 32881-32884	 **attackbox here**
    sprite('ahe000_16', 4)	# 32885-32888	 **attackbox here**
    sprite('ahe000_17', 4)	# 32889-32892	 **attackbox here**
    sprite('ahe000_18', 4)	# 32893-32896	 **attackbox here**
    sprite('ahe000_19', 4)	# 32897-32900	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 32901-32901

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ahe200_00', 3)	# 1-3
    sprite('ahe400_04', 2)	# 4-5
    sprite('ahe272_00', 3)	# 6-8
    sprite('ahe272_01', 3)	# 9-11
    sprite('ahe272_02', 3)	# 12-14	 **attackbox here**
    sprite('ahe272_03', 3)	# 15-17
    sprite('ahe272_03', 3)	# 18-20
    sprite('ahe272_03', 3)	# 21-23
    sprite('ahe064_00', 3)	# 24-26
    sprite('ahe064_01', 3)	# 27-29
    sprite('ahe064_02', 3)	# 30-32
    sprite('ahe064_03', 3)	# 33-35
    label(0)
    sprite('ahe000_00', 4)	# 36-39	 **attackbox here**
    sprite('ahe000_01', 4)	# 40-43	 **attackbox here**
    sprite('ahe000_02', 4)	# 44-47	 **attackbox here**
    sprite('ahe000_03', 4)	# 48-51	 **attackbox here**
    sprite('ahe000_04', 4)	# 52-55	 **attackbox here**
    sprite('ahe000_05', 4)	# 56-59	 **attackbox here**
    sprite('ahe000_06', 4)	# 60-63	 **attackbox here**
    sprite('ahe000_07', 4)	# 64-67	 **attackbox here**
    sprite('ahe000_08', 4)	# 68-71	 **attackbox here**
    sprite('ahe000_09', 4)	# 72-75	 **attackbox here**
    sprite('ahe000_10', 4)	# 76-79	 **attackbox here**
    sprite('ahe000_11', 4)	# 80-83	 **attackbox here**
    sprite('ahe000_12', 4)	# 84-87	 **attackbox here**
    sprite('ahe000_13', 4)	# 88-91	 **attackbox here**
    sprite('ahe000_14', 4)	# 92-95	 **attackbox here**
    sprite('ahe000_15', 4)	# 96-99	 **attackbox here**
    sprite('ahe000_16', 4)	# 100-103	 **attackbox here**
    sprite('ahe000_17', 4)	# 104-107	 **attackbox here**
    sprite('ahe000_18', 4)	# 108-111	 **attackbox here**
    sprite('ahe000_19', 4)	# 112-115	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 116-116

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)

        def upon_11():
            GFX_0('XhitEff_Arcana', -1)
    sprite('ahe000_00', 5)	# 1-5	 **attackbox here**
    sprite('ahe271_05', 5)	# 6-10
    sprite('ahe274_01', 6)	# 11-16
    sprite('ahe274_02', 3)	# 17-19
    physicsXImpulse(15000)
    sprite('ahe274_03', 3)	# 20-22	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    sprite('ahe274_03', 2)	# 23-24	 **attackbox here**
    StartMultihit()
    sprite('ahe274_04', 5)	# 25-29
    sprite('ahe274_05', 3)	# 30-32
    sprite('ahe274_06', 3)	# 33-35
    sprite('ahe274_07', 3)	# 36-38
    sprite('ahe274_08', 3)	# 39-41
    sprite('ahe271_06', 5)	# 42-46
    sprite('ahe271_07', 5)	# 47-51
    sprite('ahe271_08', 5)	# 52-56
    sprite('ahe271_09', 4)	# 57-60

@Subroutine
def ThrowApproachInit():
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

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ahe032_00', 3)	# 1-3
    sprite('ahe032_01', 3)	# 4-6
    label(0)
    sprite('ahe032_02', 3)	# 7-9
    sprite('ahe032_03', 3)	# 10-12
    Unknown8006(100, 1, 0)
    sprite('ahe032_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe310_00', 2)	# 16-17
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ahe310_01', 1)	# 18-18
    sprite('ahe310_02', 3)	# 19-21	 **attackbox here**
    Unknown1084(1)
    sprite('ahe310_03', 4)	# 22-25
    SFX_1('ahe154')
    sprite('ahe310_04', 4)	# 26-29
    sprite('ahe310_05', 7)	# 30-36
    sprite('ahe310_06', 4)	# 37-40
    sprite('ahe310_07', 4)	# 41-44

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(1000)
        AirUntechableTime(60)
        Unknown9154(30)
        AttackP2(50)
        Unknown11092(1)
        Unknown14077(0)
        PushbackX(12000)
        Unknown11069('ThrowExe')
    sprite('ahe310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ahe271_01', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ahe271_02', 2)	# 7-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ahe271_03', 3)	# 9-11	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ahe271_04', 2)	# 12-13
    sprite('ahe311_00', 2)	# 14-15
    sprite('ahe311_01', 2)	# 16-17
    sprite('ahe311_02', 2)	# 18-19
    sprite('ahe311_03', 2)	# 20-21
    sprite('ahe231_05', 2)	# 22-23
    physicsXImpulse(20000)
    sprite('ahe231_06', 2)	# 24-25
    Unknown1019(50)
    sprite('ahe231_07', 2)	# 26-27	 **attackbox here**
    StartMultihit()
    sprite('ahe231_08', 2)	# 28-29	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    AttackLevel_(4)
    Unknown11069('')
    GroundedHitstunAnimation(1)
    AirPushbackX(5000)
    AirPushbackY(30000)
    Unknown14077(1)
    SFX_1('ahe107_0')
    sprite('ahe231_09', 5)	# 30-34
    Unknown1019(0)
    sprite('ahe231_10', 5)	# 35-39
    sprite('ahe231_11', 5)	# 40-44
    sprite('ahe000_00', 5)	# 45-49	 **attackbox here**

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ahe032_00', 3)	# 1-3
    sprite('ahe032_01', 3)	# 4-6
    label(0)
    sprite('ahe032_02', 3)	# 7-9
    sprite('ahe032_03', 3)	# 10-12
    Unknown8006(100, 1, 0)
    sprite('ahe032_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe310_00', 2)	# 16-17
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ahe310_01', 1)	# 18-18
    sprite('ahe310_02', 3)	# 19-21	 **attackbox here**
    Unknown1084(1)
    sprite('ahe310_03', 4)	# 22-25
    SFX_1('ahe154')
    sprite('ahe310_04', 4)	# 26-29
    sprite('ahe310_05', 7)	# 30-36
    sprite('ahe310_06', 4)	# 37-40
    sprite('ahe310_07', 4)	# 41-44

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirUntechableTime(60)
        AirPushbackX(-10000)
        AirPushbackY(35000)
        Unknown9310(1)
        AirHitstunAnimation(11)
        Unknown11072(1, -5000, 50000)
        Hitstop(0)
        Unknown2004(1, 0)
        Unknown13021(1)
        Unknown21005(1)
    sprite('ahe310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ahe313_00', 4)	# 4-7
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ahe313_01', 4)	# 8-11
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    physicsXImpulse(-20000)
    sprite('ahe313_02', 2)	# 12-13
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1019(50)
    sprite('ahe313_02', 2)	# 14-15
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1019(50)
    SFX_1('ahe153')
    sprite('ahe313_03', 1)	# 16-16	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    Unknown1019(50)
    sprite('ahe313_03', 7)	# 17-23	 **attackbox here**
    Unknown1019(50)
    sprite('ahe313_04', 8)	# 24-31	 **attackbox here**
    Unknown1019(0)
    Unknown18009(1)
    sprite('ahe313_05', 5)	# 32-36
    sprite('ahe313_06', 5)	# 37-41
    sprite('ahe313_07', 5)	# 42-46

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11092(1)
        AirUntechableTime(60)
        PushbackX(12000)
        AirPushbackX(2500)
        clearUponHandler(2)

        def upon_78():
            SLOT_51 = 1

        def upon_14():
            Unknown21015('6168653332305f77696e675f6566660000000000000000000000000000000000c60f000000000000')
    sprite('ahe320_00', 3)	# 1-3
    sprite('ahe320_01', 3)	# 4-6
    sprite('ahe320_02', 3)	# 7-9
    GFX_0('ahe320_attack_eff', 0)
    Unknown7006('ahe200_0', 100, 845506657, 828321840, 0, 0, 100, 845506657, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ahe320_03', 2)	# 10-11	 **attackbox here**
    Unknown14070('AntiAir2nd')
    GFX_0('ahe320_attack2_eff', 0)
    sprite('ahe320_04', 2)	# 12-13
    sprite('ahe320_05', 2)	# 14-15
    sprite('ahe320_06', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    Damage(1500)
    AirPushbackY(40000)
    Unknown9215()
    physicsXImpulse(10000)
    physicsYImpulse(30000)
    setGravity(1300)
    GFX_0('ahe320_attack3_eff', 0)
    GFX_0('ahe320_wing_eff', 0)

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(10)
    sprite('ahe320_07', 3)	# 19-21	 **attackbox here**
    sprite('ahe320_08', 3)	# 22-24	 **attackbox here**
    sprite('ahe320_09', 3)	# 25-27	 **attackbox here**
    GFX_0('Invincible_Obj', 0)
    Unknown1019(25)
    if SLOT_51:
        Unknown14072('AntiAir2nd')
    sprite('ahe320_10', 6)	# 28-33
    Unknown14074('AntiAir2nd')
    setInvincible(0)
    GFX_0('ahe320_heart_eff', 0)
    SFX_3('ahese_00')
    sprite('ahe320_11', 6)	# 34-39
    sprite('ahe320_12', 6)	# 40-45
    sprite('ahe320_13', 6)	# 46-51
    sprite('ahe320_14', 6)	# 52-57
    label(0)
    sprite('ahe020_07', 3)	# 58-60
    sprite('ahe020_08', 3)	# 61-63
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('ahe010_02', 2)	# 64-65
    sprite('ahe010_01', 2)	# 66-67
    sprite('ahe010_00', 2)	# 68-69
    sprite('ahe000_00', 2)	# 70-71	 **attackbox here**
    ExitState()

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11092(1)
        AirUntechableTime(60)
        PushbackX(12000)
        AirPushbackX(2500)
        clearUponHandler(2)

        def upon_78():
            SLOT_51 = 1

        def upon_14():
            Unknown21015('6168653332305f77696e675f6566660000000000000000000000000000000000c60f000000000000')
    sprite('ahe320_15', 3)	# 1-3
    sprite('ahe320_16', 3)	# 4-6
    Unknown1084(1)
    GFX_0('ahe320_airattack_eff', 0)
    Unknown7006('ahe200_0', 100, 845506657, 828321840, 0, 0, 100, 845506657, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ahe320_17', 3)	# 7-9	 **attackbox here**
    Unknown14070('AntiAir2nd')
    GFX_0('ahe320_airattack2_eff', 0)
    sprite('ahe320_18', 3)	# 10-12
    sprite('ahe320_19', 3)	# 13-15
    sprite('ahe320_06', 3)	# 16-18	 **attackbox here**
    RefreshMultihit()
    Damage(1400)
    AirPushbackY(30000)
    Unknown9215()
    physicsXImpulse(5000)
    physicsYImpulse(25000)
    setGravity(1300)
    GFX_0('ahe320_attack3_eff', 0)
    GFX_0('ahe320_wing_eff', 0)

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(10)
    sprite('ahe320_07', 3)	# 19-21	 **attackbox here**
    sprite('ahe320_08', 3)	# 22-24	 **attackbox here**
    sprite('ahe320_09', 3)	# 25-27	 **attackbox here**
    GFX_0('Invincible_Obj', 0)
    Unknown1019(25)
    if SLOT_51:
        Unknown14072('AntiAir2nd')
    sprite('ahe320_10', 6)	# 28-33
    Unknown14074('AntiAir2nd')
    setInvincible(0)
    GFX_0('ahe320_airheart_eff', 0)
    SFX_3('ahese_00')
    sprite('ahe320_11', 6)	# 34-39
    sprite('ahe320_12', 6)	# 40-45
    sprite('ahe320_13', 6)	# 46-51
    sprite('ahe320_14', 6)	# 52-57
    label(0)
    sprite('ahe020_07', 3)	# 58-60
    sprite('ahe020_08', 3)	# 61-63
    loopRest()
    gotoLabel(0)
    label(10)
    sprite('ahe010_02', 2)	# 64-65
    sprite('ahe010_01', 2)	# 66-67
    sprite('ahe010_00', 2)	# 68-69
    sprite('ahe000_00', 2)	# 70-71	 **attackbox here**
    ExitState()

@State
def AntiAir2nd():

    def upon_IMMEDIATE():
        Unknown17025('')
        Unknown30087(0)
        setInvincible(0)
        AttackLevel_(3)
        Damage(1600)
        AttackP1(48)
        AttackP2(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(-30000)
        AirUntechableTime(42)
        Unknown9310(20)
        Unknown11068(1)
        Unknown11056(0)
        Unknown14083(0)
        Unknown30068(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        loopRelated(17, 24)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        SLOT_8 = 1
        YAccel(160)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
    sprite('ahe273_01', 3)	# 1-3
    sprite('ahe273_02', 2)	# 4-5
    GFX_0('ahe273_attack_eff', 100)
    sprite('ahe273_03', 2)	# 6-7
    sprite('ahe273_04', 2)	# 8-9
    SFX_3('ahese_00')
    sprite('ahe273_05ex', 3)	# 10-12	 **attackbox here**
    physicsXImpulse(-8000)
    Unknown1021(5000)
    sprite('ahe273_06', 3)	# 13-15	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    Unknown1043()
    sprite('ahe273_07', 32767)	# 16-32782
    label(2)
    sprite('keep', 3)	# 32783-32785
    sprite('keep', 3)	# 32786-32788
    sprite('ahe020_05', 3)	# 32789-32791
    sprite('ahe020_06', 3)	# 32792-32794
    label(0)
    sprite('ahe020_07', 3)	# 32795-32797
    sprite('ahe020_08', 3)	# 32798-32800
    gotoLabel(0)
    label(1)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ahe010_01', 8)	# 32801-32808
    sprite('ahe010_00', 6)	# 32809-32814

@Subroutine
def ExFlashColor():
    if (not SLOT_4):
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
        Unknown23118(20680)
        Unknown23108(-2)
        Unknown23114(-5)

@Subroutine
def HomingCancelLand():
    HitOrBlockCancel('HomingActionLandN')
    HitOrBlockCancel('HomingActionLand4')
    HitOrBlockCancel('HomingActionLand6')

@Subroutine
def FlexHomingCancelLand():
    WhiffCancel('HomingActionLandN')
    WhiffCancel('HomingActionLand4')
    WhiffCancel('HomingActionLand6')

@Subroutine
def DeriveHomingCancelInputLand():
    Unknown14070('HomingActionLandN')
    Unknown14070('HomingActionLand4')
    Unknown14070('HomingActionLand6')

@Subroutine
def DeriveHomingCancelTimingLand():
    Unknown14072('HomingActionLandN')
    Unknown14072('HomingActionLand4')
    Unknown14072('HomingActionLand6')

@Subroutine
def DeriveHomingCancelClear():
    Unknown14074('HomingActionLandN')
    Unknown14074('HomingActionLand4')
    Unknown14074('HomingActionLand6')

@Subroutine
def HomingLandInit():
    AttackDefaults_StandingNormal()
    Unknown11063(1)
    Unknown30068(1)
    Recovery()
    loopRelated(17, 4)

    def upon_17():
        Unknown23125('')
        Unknown2058(-5000)
        Unknown26('ahe403_circle_eff')
        Unknown26('ahe403_circle1_eff')
        Unknown26('ahe403_circle2_eff')
        Unknown26('ahe403_footcircle_eff')
        Unknown26('ahe403_footcircle1_eff')
        Unknown26('ahe403_footcircle2_eff')
        Unknown26('ahe403_footparticle_eff')
        Unknown26('ahe403_footparticle1_eff')
        Unknown26('ahe403_footparticle2_eff')
        Unknown26('ahe403_footparticle3_eff')
        Unknown26('ahe403_footparticle4_eff')
        Unknown26('ahe405_circle_eff')
        Unknown26('ahe405_circle1a_eff')
        Unknown26('ahe405_circle1b_eff')
        Unknown26('ahe405_circle2a_eff')
        Unknown26('ahe405_circle2b_eff')
        SFX_3('ahese_05')

@State
def HomingActionLandN():

    def upon_IMMEDIATE():
        callSubroutine('HomingLandInit')
    sprite('ahe252_00ex', 3)	# 1-3
    sprite('ahe252_01ex', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe252_02ex', 3)	# 7-9
    sprite('ahe252_03ex', 3)	# 10-12
    sprite('ahe252_01ex', 3)	# 13-15
    sprite('keep', 1)	# 16-16
    Unknown2006()
    sprite('keep', 100)	# 17-116
    Unknown1047(100000)
    enterState('NHomingDash')

@State
def HomingActionLand4():

    def upon_IMMEDIATE():
        callSubroutine('HomingLandInit')

        def upon_3():
            Unknown1019(88)
        setInvincible(1)
    sprite('ahe020_04', 3)	# 1-3
    sprite('ahe035_00', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe033_00ex01', 3)	# 7-9
    physicsXImpulse(-50000)
    sprite('ahe033_01ex01', 3)	# 10-12
    sprite('ahe033_00ex01', 3)	# 13-15
    sprite('ahe033_01ex01', 3)	# 16-18
    sprite('ahe033_00ex01', 2)	# 19-20
    sprite('ahe000_00', 100)	# 21-120	 **attackbox here**
    setInvincible(0)
    enterState('HomingLandDash')

@State
def HomingActionLand6():

    def upon_IMMEDIATE():
        callSubroutine('HomingLandInit')
    sprite('ahe000_00', 3)	# 1-3	 **attackbox here**
    sprite('ahe000_00', 3)	# 4-6	 **attackbox here**
    sprite('ahe000_00', 100)	# 7-106	 **attackbox here**
    enterState('HomingLandDash')

@State
def HomingLandDash():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        Unknown30068(1)
        Recovery()
        Unknown1052(1)
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_18 == 7):
                    Unknown13014(1)
                    Unknown13015(1)
                    Unknown8007(100, 1, 1)
                    physicsXImpulse(18000)
                    Unknown1045(18000)
                if (SLOT_18 >= 7):
                    Unknown1015(440)
                    Unknown1047(440)
                    if (SLOT_12 >= 28000):
                        SLOT_12 = 28000
                        Unknown1045(28000)
                Unknown59('19000000640000001600000064000000')
                if (SLOT_0 < 150000):
                    clearUponHandler(17)
                    clearUponHandler(3)
                    sendToLabel(100)
                if (SLOT_163 < (-50000)):
                    clearUponHandler(17)
                    clearUponHandler(3)
                    sendToLabel(100)
                loopRelated(17, 60)

                def upon_17():
                    clearUponHandler(17)
                    clearUponHandler(3)
                    sendToLabel(100)
        callSubroutine('ExFlashColor')
    sprite('ahe032_00', 3)	# 1-3
    physicsXImpulse(8000)
    sprite('ahe032_01', 3)	# 4-6
    sprite('ahe032_02', 3)	# 7-9
    Unknown2037(1)
    sprite('ahe032_03', 3)	# 10-12
    sprite('ahe032_04', 3)	# 13-15
    label(0)
    sprite('ahe032_02', 3)	# 16-18
    sprite('ahe032_03', 3)	# 19-21
    sprite('ahe032_04', 3)	# 22-24
    loopRest()
    gotoLabel(0)
    label(100)
    sprite('ahe032_05', 3)	# 25-27
    physicsXImpulse(0)
    Unknown1052(0)
    sprite('ahe032_06', 3)	# 28-30
    sprite('ahe032_07', 3)	# 31-33
    sprite('ahe032_08', 3)	# 34-36

@Subroutine
def HomingCancel():
    HitOrBlockCancel('CancelHomingActionN')
    HitOrBlockCancel('CancelHomingAction1')
    HitOrBlockCancel('CancelHomingAction2')
    HitOrBlockCancel('CancelHomingAction3')
    HitOrBlockCancel('CancelHomingAction4')
    HitOrBlockCancel('CancelHomingAction6')
    HitOrBlockCancel('CancelHomingAction7')
    HitOrBlockCancel('CancelHomingAction8')
    HitOrBlockCancel('CancelHomingAction9')

@Subroutine
def FlexHomingCancel():
    WhiffCancel('CancelHomingActionN')
    WhiffCancel('CancelHomingAction1')
    WhiffCancel('CancelHomingAction2')
    WhiffCancel('CancelHomingAction3')
    WhiffCancel('CancelHomingAction4')
    WhiffCancel('CancelHomingAction6')
    WhiffCancel('CancelHomingAction7')
    WhiffCancel('CancelHomingAction8')
    WhiffCancel('CancelHomingAction9')

@Subroutine
def DeriveHomingCancelInput():
    Unknown14070('CancelHomingActionN')
    Unknown14070('CancelHomingAction1')
    Unknown14070('CancelHomingAction2')
    Unknown14070('CancelHomingAction3')
    Unknown14070('CancelHomingAction4')
    Unknown14070('CancelHomingAction6')
    Unknown14070('CancelHomingAction7')
    Unknown14070('CancelHomingAction8')
    Unknown14070('CancelHomingAction9')

@Subroutine
def DeriveHomingCancelTiming():
    Unknown14072('CancelHomingActionN')
    Unknown14072('CancelHomingAction1')
    Unknown14072('CancelHomingAction2')
    Unknown14072('CancelHomingAction3')
    Unknown14072('CancelHomingAction4')
    Unknown14072('CancelHomingAction6')
    Unknown14072('CancelHomingAction7')
    Unknown14072('CancelHomingAction8')
    Unknown14072('CancelHomingAction9')

@Subroutine
def DeriveHomingCancelClear():
    Unknown14074('CancelHomingActionN')
    Unknown14074('CancelHomingAction1')
    Unknown14074('CancelHomingAction2')
    Unknown14074('CancelHomingAction3')
    Unknown14074('CancelHomingAction4')
    Unknown14074('CancelHomingAction6')
    Unknown14074('CancelHomingAction7')
    Unknown14074('CancelHomingAction8')
    Unknown14074('CancelHomingAction9')

@Subroutine
def HomingInit():
    AttackDefaults_AirNormal()
    Unknown11063(1)
    clearUponHandler(2)
    Recovery()
    Unknown22003(-1)
    SLOT_4 = 0
    if SLOT_93:
        SLOT_4 = 1
    else:
        Unknown30068(1)
        Unknown1084(1)
    loopRelated(17, 4)

    def upon_17():
        SFX_3('ahese_05')
        if SLOT_4:
            if Unknown23148('HomingActionN'):
                GFX_0('ahe_homing_eff', 103)
            if Unknown23148('HomingActionLandN'):
                GFX_0('ahe_homing_eff', 103)
            Unknown26('ahe403_circle_eff')
            Unknown26('ahe403_circle1_eff')
            Unknown26('ahe403_circle2_eff')
            Unknown26('ahe403_footcircle_eff')
            Unknown26('ahe403_footcircle1_eff')
            Unknown26('ahe403_footcircle2_eff')
            Unknown26('ahe403_footparticle_eff')
            Unknown26('ahe403_footparticle1_eff')
            Unknown26('ahe403_footparticle2_eff')
            Unknown26('ahe403_footparticle3_eff')
            Unknown26('ahe403_footparticle4_eff')
            Unknown26('ahe405_circle_eff')
            Unknown26('ahe405_circle1a_eff')
            Unknown26('ahe405_circle1b_eff')
            Unknown26('ahe405_circle2a_eff')
            Unknown26('ahe405_circle2b_eff')
        else:
            Unknown23125('')
            Unknown2058(-5000)
            Unknown26('ahe403_circle_eff')
            Unknown26('ahe403_circle1_eff')
            Unknown26('ahe403_circle2_eff')
            Unknown26('ahe403_footcircle_eff')
            Unknown26('ahe403_footcircle1_eff')
            Unknown26('ahe403_footcircle2_eff')
            Unknown26('ahe403_footparticle_eff')
            Unknown26('ahe403_footparticle1_eff')
            Unknown26('ahe403_footparticle2_eff')
            Unknown26('ahe403_footparticle3_eff')
            Unknown26('ahe403_footparticle4_eff')
            Unknown26('ahe405_circle_eff')
            Unknown26('ahe405_circle1a_eff')
            Unknown26('ahe405_circle1b_eff')
            Unknown26('ahe405_circle2a_eff')
            Unknown26('ahe405_circle2b_eff')
        loopRelated(17, 20)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

@State
def HomingActionN():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')
    sprite('ahe252_00', 3)	# 1-3
    sprite('ahe252_01', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe252_02', 3)	# 7-9
    sprite('ahe252_03', 3)	# 10-12
    sprite('ahe252_01', 3)	# 13-15
    label(1)
    sprite('keep', 1)	# 16-16
    Unknown2006()
    sprite('keep', 100)	# 17-116
    Unknown1047(100000)
    enterState('NHomingDash')

@State
def HomingAction1():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')
        SLOT_64 = 1

        def upon_3():
            Unknown1019(90)
            YAccel(90)
        setInvincible(1)
    sprite('ahe020_04', 3)	# 1-3
    sprite('ahe035_00', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe033_00ex01', 3)	# 7-9
    physicsXImpulse(-35000)
    physicsYImpulse(-30000)
    sprite('ahe033_01ex01', 3)	# 10-12
    label(0)
    sprite('ahe033_00ex01', 3)	# 13-15
    sprite('ahe033_01ex01', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe020_04', 100)	# 19-118
    setInvincible(0)
    Unknown48('19000000020000000600000019000000020000000c000000')
    Unknown48('19000000020000000700000019000000020000000d000000')
    if SLOT_36:
        Unknown1047(-30000)
        Unknown1036(25000)
        enterState('HomingDash')
    else:
        enterState('CmnActJumpLanding')

@State
def HomingAction2():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')
        SLOT_64 = 1

        def upon_3():
            YAccel(110)
    sprite('ahe020_04', 3)	# 1-3
    sprite('ahe020_06', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe020_07', 3)	# 7-9
    physicsYImpulse(-6000)
    sprite('ahe020_08', 3)	# 10-12
    label(0)
    sprite('ahe020_07', 3)	# 13-15
    sprite('ahe020_08', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe020_04', 100)	# 19-118
    Unknown48('19000000020000000600000019000000020000000c000000')
    Unknown48('19000000020000000700000019000000020000000d000000')
    if SLOT_36:
        Unknown1036(25000)
        enterState('HomingDash')
    else:
        enterState('CmnActJumpLanding')

@State
def HomingAction3():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')
        SLOT_64 = 1
        SLOT_65 = 1

        def upon_3():
            Unknown1019(98)
            YAccel(98)
            if (not (SLOT_163 > 0)):
                Unknown1019(90)
        if Unknown23145('CmnActAirFDash'):
            SLOT_51 = 1
    sprite('ahe020_04', 3)	# 1-3
    Unknown23183('6168653033325f30326578303100000000000000000000000000000000000000030000000200000033000000')
    sprite('ahe035_00', 3)	# 4-6
    Unknown23183('6168653033325f30326578303100000000000000000000000000000000000000030000000200000033000000')
    physicsYImpulse(0)
    setGravity(500)
    sprite('ahe252_12', 3)	# 7-9
    physicsXImpulse(15000)
    physicsYImpulse(-10000)
    Unknown1045(0)
    sprite('ahe252_13', 3)	# 10-12
    label(0)
    sprite('ahe252_12', 3)	# 13-15
    sprite('ahe252_13', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe252_12', 100)	# 19-118
    if (SLOT_163 > 0):
        Unknown48('19000000020000000600000019000000020000000c000000')
        Unknown1047(90000)
    if SLOT_36:
        Unknown1047(10000)
        enterState('HomingDash')
    else:
        enterState('CmnActJumpLanding')

@State
def HomingAction4():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')

        def upon_3():
            Unknown1019(88)
        setInvincible(1)
    sprite('ahe020_04', 3)	# 1-3
    sprite('ahe035_00', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe033_00ex01', 3)	# 7-9
    physicsXImpulse(-50000)
    sprite('ahe033_01ex01', 3)	# 10-12
    label(0)
    sprite('ahe033_00ex01', 3)	# 13-15
    sprite('ahe033_01ex01', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe020_04', 100)	# 19-118
    setInvincible(0)
    Unknown48('19000000020000000600000019000000020000000c000000')
    Unknown48('19000000020000000700000019000000020000000d000000')
    Unknown1047(-100000)
    Unknown1036(25000)
    enterState('HomingDash')

@State
def HomingAction6():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')

        def upon_3():
            Unknown1019(98)
            if (not (SLOT_163 > 0)):
                Unknown1019(90)
        if Unknown23145('CmnActAirFDash'):
            SLOT_51 = 1
    sprite('ahe020_04', 3)	# 1-3
    Unknown23183('6168653033325f30326578303100000000000000000000000000000000000000030000000200000033000000')
    sprite('ahe035_00', 3)	# 4-6
    Unknown23183('6168653033325f30336578303100000000000000000000000000000000000000030000000200000033000000')
    physicsYImpulse(0)
    setGravity(500)
    sprite('ahe032_02ex01', 3)	# 7-9
    physicsXImpulse(20000)
    Unknown1045(0)
    sprite('ahe032_03ex01', 3)	# 10-12
    label(0)
    sprite('ahe032_02ex01', 3)	# 13-15
    sprite('ahe032_03ex01', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe032_02ex01', 100)	# 19-118
    Unknown1047(40000)
    if (SLOT_163 > 0):
        Unknown48('19000000020000000600000019000000020000000c000000')
        Unknown1047(90000)
    enterState('HomingDash')

@State
def HomingAction7():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')

        def upon_3():
            Unknown1019(90)
            YAccel(90)
        setInvincible(1)
    sprite('ahe020_04', 3)	# 1-3
    sprite('ahe035_00', 3)	# 4-6
    Unknown1084(1)
    sprite('ahe033_00ex01', 3)	# 7-9
    physicsXImpulse(-35000)
    physicsYImpulse(30000)
    sprite('ahe033_01ex01', 3)	# 10-12
    label(0)
    sprite('ahe033_00ex01', 3)	# 13-15
    sprite('ahe033_01ex01', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe020_04', 100)	# 19-118
    setInvincible(0)
    Unknown48('19000000020000000600000019000000020000000c000000')
    Unknown1047(-30000)
    enterState('HomingDash')

@State
def HomingAction8():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')
    sprite('ahe020_00', 3)	# 1-3
    sprite('ahe020_01', 3)	# 4-6
    physicsYImpulse(30000)
    Unknown1043()
    label(0)
    sprite('ahe020_00', 3)	# 7-9
    sprite('ahe020_01', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe020_04', 100)	# 13-112
    Unknown48('19000000020000000600000019000000020000000c000000')
    enterState('HomingDash')

@State
def HomingAction9():

    def upon_IMMEDIATE():
        callSubroutine('HomingInit')
        if Unknown23145('CmnActAirFDash'):
            SLOT_51 = 1
        Unknown2057(0)

        def upon_3():
            Unknown1019(98)
            YAccel(98)
            if (not (SLOT_163 > 0)):
                Unknown1019(90)
    sprite('ahe020_04', 3)	# 1-3
    Unknown23183('6168653033325f30326578303100000000000000000000000000000000000000030000000200000033000000')
    sprite('ahe035_00', 3)	# 4-6
    Unknown23183('6168653033325f30336578303100000000000000000000000000000000000000030000000200000033000000')
    physicsXImpulse(10000)
    physicsYImpulse(30000)
    Unknown1043()
    label(0)
    sprite('ahe252_10', 3)	# 7-9
    sprite('ahe252_11', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ahe252_10', 100)	# 13-112
    if (SLOT_163 > 0):
        Unknown48('19000000020000000600000019000000020000000c000000')
        Unknown1047(90000)
    Unknown1047(10000)
    Unknown1036(120000)
    enterState('HomingDash')

@Subroutine
def CheckStartAnimAngle():
    Unknown1116('')
    ExitState()
    Unknown22('asdfasdf7')
    Unknown53(0)

    @State
    def asdfasdf9():
        sprite('asdfasdf10', 2)	# 1-2
        Unknown23('00000000a08601000400000002000000000000000b0000000e00000005000000380000000b0000000f0000003900000005000000280000000900000002000000')
        Unknown53(0)
        if sprite('asdfasdf12', 100000):	# 3-100002
            sendToLabel(14)
        else:
            sendToLabel(16)
    if (SLOT_53 == 3):
        if (SLOT_23 <= 100000):
            sendToLabel(14)
        else:
            sendToLabel(15)
    if (SLOT_53 == 4):
        sendToLabel(14)
    if (SLOT_53 == 5):
        sendToLabel(13)
    if (SLOT_53 == 6):
        sendToLabel(12)
    if (SLOT_53 == 7):
        sendToLabel(11)
    if (SLOT_53 == 8):
        sendToLabel(10)
    if (SLOT_53 == 9):
        sendToLabel(11)
    if (SLOT_53 == 10):
        sendToLabel(12)
    if (SLOT_53 == 11):
        sendToLabel(13)

@Subroutine
def CheckAnimAngle():
    Unknown1116('')
    ExitState()
    Unknown22('asdfasdf12')
    Unknown53(0)

    @State
    def asdfasdf14():
        sprite('asdfasdf16', 2)	# 1-2
        Unknown23('00000000a08601000400000002000000000000000b0000000300000005000000380000000b000000050000003900000005000000280000000900000002000000')
        Unknown53(0)
        if sprite('asdfasdf623', 100000):	# 3-100002
            sendToLabel(3)
        else:
            sendToLabel(6)
    if (SLOT_53 == 3):
        if (SLOT_23 <= 100000):
            sendToLabel(3)
        else:
            sendToLabel(5)
    if (SLOT_53 == 4):
        sendToLabel(4)
    if (SLOT_53 == 5):
        sendToLabel(3)
    if (SLOT_53 == 6):
        sendToLabel(2)
    if (SLOT_53 == 7):
        sendToLabel(1)
    if (SLOT_53 == 8):
        sendToLabel(0)
    if (SLOT_53 == 9):
        sendToLabel(1)
    if (SLOT_53 == 10):
        sendToLabel(2)
    if (SLOT_53 == 11):
        sendToLabel(3)

@Subroutine
def HomingSpeed():
    if (SLOT_13 >= 30000):
        SLOT_13 = 30000
    if (SLOT_13 <= (-30000)):
        SLOT_13 = (-30000)
    if (SLOT_12 >= 30000):
        SLOT_12 = 30000
    if (SLOT_12 <= (-30000)):
        SLOT_12 = (-30000)

@Subroutine
def HomingSE():
    SLOT_57 = (SLOT_57 + 1)
    if (SLOT_57 >= 13):
        SLOT_57 = 0
    if (SLOT_57 == 1):
        SFX_3('ahese_06')

@State
def NHomingDash():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        clearUponHandler(2)
        Unknown30068(1)
        Unknown11063(1)
        Unknown2061(0)
        Recovery()
        WhiffCancel('NmlAtkAIR5A')
        WhiffCancel('NmlAtkAIR5B')
        if SLOT_4:
            Unknown13019(1)
        if (SLOT_19 >= 200000):
            SLOT_11 = 1
        SLOT_5 = 1
        SLOT_55 = 0
        loopRelated(17, 4)

        def upon_17():
            SLOT_55 = 1
            WhiffCancelEnable(1)
            Unknown13015(1)
            Unknown28(2, 'CmnActJumpLanding')
            loopRelated(17, 8)

            def upon_17():
                SLOT_55 = 2
                loopRelated(17, 12)

                def upon_17():
                    SLOT_55 = 3
                    loopRelated(17, 60)

                    def upon_17():
                        sendToLabel(100)

        def upon_3():
            callSubroutine('HomingSE')
            Unknown1051(92)
            Unknown1039(102)
            if (SLOT_23 == 0):
                Unknown1007(10000)
            if (not CheckInput(0x93)):
                if (not CheckInput(0x45)):
                    if (not CheckInput(0x79)):
                        if (not CheckInput(0x5f)):
                            SLOT_60 = 0
                            SLOT_61 = 0
                            SLOT_62 = 0
                            SLOT_63 = 0
                            SLOT_9 = 0
                            SLOT_10 = 0
            if (SLOT_55 == 0):
                Unknown1114('')
                Unknown7500(22)
                Unknown1072(0)
                if (not (SLOT_19 < 10000)):
                    Unknown2006()
                if Unknown23145('HomingActionLandN'):
                    SLOT_56 = 1
                    if CheckInput(0x93):
                        Unknown1021(15000)
                callSubroutine('HomingSpeed')
            if (SLOT_55 == 1):
                Unknown1114('')
                Unknown15000(22)
                Unknown1072(0)
                if (not (SLOT_19 < 10000)):
                    Unknown2006()
                if CheckInput(0x93):
                    Unknown1021(7500)
                if CheckInput(0x45):
                    Unknown1021(-7500)
                    Unknown28(2, 'CmnActJumpLanding')
                if CheckInput(0x79):
                    Unknown1015(9000)
                    SLOT_62 = 1
                    SLOT_61 = 0
                if CheckInput(0x5f):
                    Unknown1015(-4500)
                    SLOT_62 = 0
                    if (SLOT_19 < 200000):
                        if (not SLOT_11):
                            if (not SLOT_9):
                                SLOT_61 = (SLOT_61 + 1)
                                if SLOT_61:
                                    physicsXImpulse(-5000)
                                    Unknown1015(-500)
                                    Unknown1045(-40000)
                                    YAccel(60)
                                    SLOT_9 = 1
                                if (SLOT_61 >= 10):
                                    SLOT_11 = 1
                callSubroutine('HomingSpeed')
                Unknown1019(110)
                YAccel(110)
            if (SLOT_55 == 2):
                Unknown1114('')
                Unknown22500(22)
                Unknown1072(0)
                if (not (SLOT_19 < 10000)):
                    Unknown2006()
                if CheckInput(0x93):
                    Unknown1021(11250)
                if CheckInput(0x45):
                    Unknown1021(-11250)
                    Unknown28(2, 'CmnActJumpLanding')
                if CheckInput(0x79):
                    Unknown1015(13500)
                    SLOT_62 = 1
                    SLOT_61 = 0
                if CheckInput(0x5f):
                    Unknown1015(-6750)
                    SLOT_62 = 0
                    if (SLOT_19 < 200000):
                        if (not SLOT_11):
                            if (not SLOT_9):
                                SLOT_61 = (SLOT_61 + 1)
                                if SLOT_61:
                                    physicsXImpulse(-5000)
                                    Unknown1015(-500)
                                    Unknown1045(-40000)
                                    YAccel(60)
                                    SLOT_9 = 1
                                if (SLOT_61 >= 10):
                                    SLOT_11 = 1
                callSubroutine('HomingSpeed')
                Unknown1019(120)
                YAccel(120)
            if (SLOT_55 == 3):
                Unknown1114('')
                Unknown30000()
                if (not Unknown22('0      (                '')):
                    Unknown2006()
                if CheckInput(0x93):
                    Unknown1021(15000)
                if CheckInput(0x45):
                    Unknown1021(-15000)
                    Unknown28(2, 'CmnActJumpLanding')
                if CheckInput(0x79):
                    Unknown1015(18000)
                    SLOT_62 = 1
                    SLOT_61 = 0
                if CheckInput(0x5f):
                    Unknown1015(-9000)
                    SLOT_62 = 0
                    SLOT_61 = 0
                callSubroutine('HomingSpeed')
                Unknown1019(130)
                YAccel(130)
            if (not CheckInput(0x79)):
                if (not CheckInput(0x5f)):
                    if (SLOT_19 < 10000):
                        physicsXImpulse(0)
                        Unknown1045(0)
            if (not SLOT_128):
                Unknown59('19000000640000001600000064000000')
                if (SLOT_0 < 150000):
                    sendToLabel(100)
            if (not SLOT_158):
                sendToLabel(100)
            if (not SLOT_21):
                sendToLabel(100)

        def upon_STATE_END():
            if SLOT_64:
                Unknown1045(0)
                Unknown1019(5)
            Unknown1043()
            SLOT_6 = 0
            SLOT_7 = 0
            SLOT_64 = 0
            SLOT_65 = 0
            SLOT_9 = 0
            SLOT_10 = 0
            SLOT_11 = 0
            Unknown28(2, 'CmnActJumpLanding')
            if (SLOT_12 < 0):
                Unknown1019(10)
                Unknown1045(0)
        callSubroutine('ExFlashColor')
    sprite('keep', 1)	# 1-1
    GFX_0('ahe_homing_add_eff', 103)
    if (SLOT_163 > 0):
        Unknown1051(50)
    Unknown48('190000000200000036000000160000000200000017000000')
    if (SLOT_23 < SLOT_54):
        Unknown1039(5)
    sprite('keep', 100)	# 2-101
    callSubroutine('CheckStartAnimAngle')
    ExitState()
    label(10)
    sprite('ahe252_05', 2)	# 102-103
    Unknown23183('6168653235325f30356578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(270000)
    Unknown35()
    sprite('ahe252_06', 2)	# 104-105
    Unknown23183('6168653235325f30366578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_07', 1)	# 106-106
    Unknown23183('6168653235325f30376578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 107-206
    callSubroutine('CheckLooAnimAngle')
    ExitState()
    label(11)
    sprite('ahe252_05', 2)	# 207-208
    Unknown23183('6168653235325f30356578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(300000)
    Unknown35()
    sprite('ahe252_08', 2)	# 209-210
    Unknown23183('6168653235325f30386578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_09', 1)	# 211-211
    Unknown23183('6168653235325f30396578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 212-311
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(12)
    sprite('ahe035_01', 2)	# 312-313
    Unknown23183('6168653033355f30316578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(330000)
    Unknown35()
    sprite('ahe252_10', 2)	# 314-315
    Unknown23183('6168653235325f31306578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_11', 1)	# 316-316
    Unknown23183('6168653235325f31316578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 317-416
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(13)
    sprite('ahe035_01', 2)	# 417-418
    Unknown23183('6168653033355f30316578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(0)
    Unknown35()
    sprite('ahe032_02ex01', 2)	# 419-420
    Unknown23183('6168653033325f30326578303200000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe032_03ex01', 1)	# 421-421
    Unknown23183('6168653033325f30336578303200000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 422-521
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(14)
    sprite('ahe035_01', 2)	# 522-523
    Unknown23183('6168653033355f30316578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(30000)
    Unknown35()
    sprite('ahe252_12', 2)	# 524-525
    Unknown23183('6168653235325f31326578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_13', 1)	# 526-526
    Unknown23183('6168653235325f31336578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 527-626
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(15)
    sprite('ahe252_14', 2)	# 627-628
    Unknown23183('6168653235325f31346578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(60000)
    Unknown35()
    sprite('ahe252_15', 2)	# 629-630
    Unknown23183('6168653235325f31356578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_16', 1)	# 631-631
    Unknown23183('6168653235325f31366578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 632-731
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(16)
    sprite('ahe252_14', 2)	# 732-733
    Unknown23183('6168653235325f31346578000000000000000000000000000000000000000000020000000200000038000000')
    GFX_0('ahe_homing_wind_eff', 103)
    Unknown36(1)
    Unknown1073(90000)
    Unknown35()
    sprite('ahe252_17', 2)	# 734-735
    Unknown23183('6168653235325f31376578000000000000000000000000000000000000000000020000000200000038000000')
    Unknown23183('6168653235325f3135000000000000000000000000000000000000000000000002000000020000003f000000')
    sprite('ahe252_18', 1)	# 736-736
    Unknown23183('6168653235325f31386578000000000000000000000000000000000000000000010000000200000038000000')
    Unknown23183('6168653235325f3136000000000000000000000000000000000000000000000001000000020000003f000000')
    sprite('keep', 100)	# 737-836
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(0)
    sprite('ahe252_06', 2)	# 837-838
    Unknown23183('6168653235325f30366578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_07', 1)	# 839-839
    Unknown23183('6168653235325f30376578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 840-939
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(1)
    sprite('ahe252_08', 2)	# 940-941
    Unknown23183('6168653235325f30386578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_09', 1)	# 942-942
    Unknown23183('6168653235325f30396578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 943-1042
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(2)
    sprite('ahe252_10', 2)	# 1043-1044
    Unknown23183('6168653235325f31306578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_11', 1)	# 1045-1045
    Unknown23183('6168653235325f31306578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 1046-1145
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(3)
    sprite('ahe032_02ex01', 2)	# 1146-1147
    Unknown23183('6168653033325f30326578303200000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe032_03ex01', 1)	# 1148-1148
    Unknown23183('6168653033325f30336578303200000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 1149-1248
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(4)
    sprite('ahe252_12', 2)	# 1249-1250
    Unknown23183('6168653235325f31326578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_13', 1)	# 1251-1251
    Unknown23183('6168653235325f31336578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 1252-1351
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(5)
    sprite('ahe252_15', 2)	# 1352-1353
    Unknown23183('6168653235325f31356578000000000000000000000000000000000000000000020000000200000038000000')
    sprite('ahe252_16', 1)	# 1354-1354
    Unknown23183('6168653235325f31366578000000000000000000000000000000000000000000010000000200000038000000')
    sprite('keep', 100)	# 1355-1454
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(6)
    sprite('ahe252_17', 2)	# 1455-1456
    Unknown23183('6168653235325f31376578000000000000000000000000000000000000000000020000000200000038000000')
    Unknown23183('6168653235325f3135000000000000000000000000000000000000000000000002000000020000003e000000')
    Unknown23183('6168653235325f3135657830310000000000000000000000000000000000000002000000020000003d000000')
    Unknown23183('6168653235325f3135000000000000000000000000000000000000000000000002000000020000003f000000')
    sprite('ahe252_18', 1)	# 1457-1457
    Unknown23183('6168653235325f31386578000000000000000000000000000000000000000000010000000200000038000000')
    Unknown23183('6168653235325f3136000000000000000000000000000000000000000000000001000000020000003e000000')
    Unknown23183('6168653235325f3136657830310000000000000000000000000000000000000001000000020000003d000000')
    Unknown23183('6168653235325f3136000000000000000000000000000000000000000000000001000000020000003f000000')
    sprite('keep', 100)	# 1458-1557
    callSubroutine('CheckAnimAngle')
    ExitState()
    label(100)
    sprite('keep', 100)	# 1558-1657
    clearUponHandler(3)
    Unknown1019(50)
    YAccel(25)
    Unknown1051(0)
    if (SLOT_13 >= 1):
        physicsYImpulse(10000)
    enterState('CmnActJumpDown')

@State
def HomingDash():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        clearUponHandler(2)
        Unknown30068(1)
        Unknown11063(1)
        Unknown2061(0)
        Recovery()
        WhiffCancel('NmlAtkAIR5A')
        WhiffCancel('NmlAtkAIR5B')
        if SLOT_4:
            Unknown13019(1)
        if (SLOT_19 >= 200000):
            SLOT_11 = 1
        SLOT_5 = 1
        SLOT_55 = 0
        loopRelated(17, 4)

        def upon_17():
            SLOT_55 = 1
            WhiffCancelEnable(1)
            Unknown13015(1)
            if (not SLOT_64):
                Unknown28(2, 'CmnActJumpLanding')
            loopRelated(17, 8)

            def upon_17():
                SLOT_55 = 2
                loopRelated(17, 12)

                def upon_17():
                    SLOT_55 = 3
                    loopRelated(17, 60)

                    def upon_17():
                        sendToLabel(100)

        def upon_3():
            Unknown1051(60)
            callSubroutine('HomingSE')
            if (SLOT_23 == 0):
                Unknown1007(5000)
            if (not CheckInput(0x93)):
                if (not CheckInput(0x45)):
                    if (not CheckInput(0x79)):
                        if (not CheckInput(0x5f)):
                            SLOT_60 = 0
                            SLOT_61 = 0
                            SLOT_62 = 0
                            SLOT_63 = 0
                            SLOT_9 = 0
                            SLOT_10 = 0
            if (SLOT_55 == 0):
                Unknown1114('')
                Unknown7500(22)
                if (SLOT_12 <= SLOT_6):
                    SLOT_12 = SLOT_6
                if SLOT_7:
                    if (SLOT_13 <= SLOT_7):
                        SLOT_13 = SLOT_7
                Unknown1072(0)
                if (not (SLOT_19 < 10000)):
                    Unknown2006()
                if Unknown23145('HomingActionLandN'):
                    SLOT_56 = 1
                    if CheckInput(0x93):
                        Unknown1021(7500)
                callSubroutine('HomingSpeed')
                Unknown48('19000000020000000600000019000000020000000c000000')
            if (SLOT_55 == 1):
                Unknown1114('')
                Unknown15000(22)
                if (SLOT_12 <= SLOT_6):
                    SLOT_12 = SLOT_6
                if SLOT_7:
                    if (SLOT_13 <= SLOT_7):
                        SLOT_13 = SLOT_7
                Unknown1072(0)
                if (not (SLOT_19 < 10000)):
                    Unknown2006()
                if CheckInput(0x93):
                    SLOT_60 = 0
                    SLOT_63 = 0
                    if (SLOT_19 < 300000):
                        if (not CheckInput(0x5f)):
                            Unknown1015(5000)
                    else:
                        Unknown1021(7500)
                if CheckInput(0x45):
                    SLOT_60 = 1
                    SLOT_63 = 0
                    Unknown1021(-7500)
                    Unknown28(2, 'CmnActJumpLanding')
                if CheckInput(0x79):
                    Unknown1015(9000)
                    SLOT_62 = 1
                    SLOT_61 = 0
                if CheckInput(0x5f):
                    if (not CheckInput(0x45)):
                        clearUponHandler(2)
                    Unknown59('19000000640000001600000064000000')
                    if (SLOT_0 < 300000):
                        Unknown1015(-4500)
                    elif (not CheckInput(0x93)):
                        if (not SLOT_125):
                            Unknown1019(20)
                            if (not (SLOT_23 < 10000)):
                                Unknown1021(-10000)
                    SLOT_62 = 0
                    if (SLOT_19 < 200000):
                        if (not SLOT_11):
                            if (not SLOT_9):
                                SLOT_61 = (SLOT_61 + 1)
                                if SLOT_61:
                                    physicsXImpulse(-5000)
                                    Unknown1015(-500)
                                    Unknown1045(-40000)
                                    YAccel(60)
                                    SLOT_9 = 1
                                if (SLOT_61 >= 10):
                                    SLOT_11 = 1
                callSubroutine('HomingSpeed')
                Unknown1019(80)
                YAccel(80)
            if (SLOT_55 == 2):
                Unknown1114('')
                Unknown22500(22)
                if (SLOT_12 <= SLOT_6):
                    SLOT_12 = SLOT_6
                if SLOT_7:
                    if (SLOT_13 <= SLOT_7):
                        SLOT_13 = SLOT_7
                Unknown1072(0)
                if (not (SLOT_19 < 10000)):
                    Unknown2006()
                if CheckInput(0x93):
                    SLOT_60 = 0
                    SLOT_63 = 0
                    if (SLOT_19 < 300000):
                        if (not CheckInput(0x5f)):
                            Unknown1015(5000)
                if CheckInput(0x45):
                    SLOT_60 = 1
                    SLOT_63 = 0
                    Unknown1021(-11250)
                    Unknown28(2, 'CmnActJumpLanding')
                if CheckInput(0x79):
                    Unknown1015(13500)
                    SLOT_62 = 1
                    SLOT_61 = 0
                if CheckInput(0x5f):
                    if (not CheckInput(0x45)):
                        clearUponHandler(2)
                    Unknown59('19000000640000001600000064000000')
                    if (SLOT_0 < 300000):
                        Unknown1015(-6750)
                    elif (not CheckInput(0x93)):
                        if (not SLOT_125):
                            if (not (SLOT_23 < 10000)):
                                Unknown1021(-20000)
                    SLOT_62 = 0
                    if (SLOT_19 < 200000):
                        if (not SLOT_11):
                            if (not SLOT_9):
                                SLOT_61 = (SLOT_61 + 1)
                                if SLOT_61:
                                    physicsXImpulse(-5000)
                                    Unknown1015(-500)
                                    Unknown1045(-40000)
                                    YAccel(60)
                                    SLOT_9 = 1
                                if (SLOT_61 >= 10):
                                    SLOT_11 = 1
                callSubroutine('HomingSpeed')
                Unknown1019(80)
                YAccel(80)
            if (SLOT_55 == 3):
                Unknown1114('')
                Unknown30000()
                Unknown22('(asdfasdf1')

                @State
                def asdfasdf2():
                    gotoLabel(40)
                    Unknown13(2)
                    Unknown13(2)
                    gotoLabel(4)
                    sprite('asdfasdf2', 1072)	# 1-1072

                    @State
                    def asdfasdf3():

                        @State
                        def asdfasdf4():
                            sprite('asdfasdf6', 40)	# 1-40
                            sendToLabel(2)
                            Unknown19(0, 300000, 4)
                            sprite('asdfasdf5', 55)	# 41-95
                    if CheckInput(0x45):
                        SLOT_60 = 1
                        SLOT_63 = 0
                        Unknown1021(-15000)
                        Unknown28(2, 'CmnActJumpLanding')
                    if CheckInput(0x79):
                        Unknown1015(18000)
                        SLOT_62 = 1
                        SLOT_61 = 0
                    if CheckInput(0x5f):
                        if (not CheckInput(0x45)):
                            clearUponHandler(2)
                        Unknown59('19000000640000001600000064000000')
                        if (SLOT_0 < 300000):
                            Unknown1015(-6750)
                        elif (not CheckInput(0x93)):
                            if (not SLOT_125):
                                if (not (SLOT_23 < 10000)):
                                    Unknown1021(-20000)
                        SLOT_62 = 0
                        SLOT_61 = 0
                    callSubroutine('HomingSpeed')
                    Unknown1019(80)
                    YAccel(80)
                if (SLOT_19 < 300000):
                    Unknown1019(80)
                if (not CheckInput(0x79)):
                    if (not CheckInput(0x5f)):
                        if (SLOT_19 < 10000):
                            physicsXImpulse(0)
                if (not SLOT_128):
                    Unknown59('19000000640000001600000064000000')
                    if (SLOT_0 < 150000):
                        sendToLabel(100)
                if (not SLOT_158):
                    sendToLabel(100)
                if (not SLOT_21):
                    sendToLabel(100)

            def upon_STATE_END():
                Unknown1043()
                SLOT_6 = 0
                SLOT_7 = 0
                SLOT_64 = 0
                SLOT_65 = 0
                SLOT_9 = 0
                SLOT_10 = 0
                SLOT_11 = 0
                Unknown28(2, 'CmnActJumpLanding')
            callSubroutine('ExFlashColor')
        sprite('keep', 1)	# 96-96
        GFX_0('ahe_homing_add_eff', 103)
        if (SLOT_163 > 0):
            Unknown1051(50)
        Unknown48('190000000200000036000000160000000200000017000000')
        if (SLOT_23 < SLOT_54):
            Unknown1039(5)
        sprite('keep', 100)	# 97-196
        callSubroutine('CheckStartAnimAngle')
        ExitState()
        label(10)
        sprite('ahe252_05', 2)	# 197-198
        Unknown23183('6168653235325f30356578000000000000000000000000000000000000000000020000000200000038000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(270000)
        Unknown35()
        sprite('ahe252_06', 2)	# 199-200
        Unknown23183('6168653235325f30366578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_07', 1)	# 201-201
        Unknown23183('6168653235325f30376578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 202-301
        callSubroutine('CheckLooAnimAngle')
        ExitState()
        label(11)
        sprite('ahe252_05', 2)	# 302-303
        Unknown23183('6168653235325f30356578000000000000000000000000000000000000000000020000000200000038000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(300000)
        Unknown35()
        sprite('ahe252_08', 2)	# 304-305
        Unknown23183('6168653235325f30386578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_09', 1)	# 306-306
        Unknown23183('6168653235325f30396578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 307-406
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(12)
        sprite('ahe035_01', 2)	# 407-408
        Unknown23183('6168653033355f30316578000000000000000000000000000000000000000000020000000200000038000000')
        Unknown23183('6168653235325f31320000000000000000000000000000000000000000000000020000000200000041000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(330000)
        Unknown35()
        sprite('ahe252_10', 2)	# 409-410
        Unknown23183('6168653235325f31306578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_11', 1)	# 411-411
        Unknown23183('6168653235325f31316578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 412-511
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(13)
        sprite('ahe035_01', 2)	# 512-513
        Unknown23183('6168653033355f30316578000000000000000000000000000000000000000000020000000200000038000000')
        Unknown23183('6168653235325f31320000000000000000000000000000000000000000000000020000000200000041000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(0)
        Unknown35()
        sprite('ahe032_02ex01', 2)	# 514-515
        Unknown23183('6168653033325f30326578303200000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe032_03ex01', 1)	# 516-516
        Unknown23183('6168653033325f30336578303200000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 517-616
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(14)
        sprite('ahe035_01', 2)	# 617-618
        Unknown23183('6168653033355f30316578000000000000000000000000000000000000000000020000000200000038000000')
        Unknown23183('6168653235325f31320000000000000000000000000000000000000000000000020000000200000041000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(30000)
        Unknown35()
        sprite('ahe252_12', 2)	# 619-620
        Unknown23183('6168653235325f31326578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_13', 1)	# 621-621
        Unknown23183('6168653235325f31336578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 622-721
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(15)
        sprite('ahe252_14', 2)	# 722-723
        Unknown23183('6168653235325f31346578000000000000000000000000000000000000000000020000000200000038000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(60000)
        Unknown35()
        sprite('ahe252_15', 2)	# 724-725
        Unknown23183('6168653235325f31356578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_16', 1)	# 726-726
        Unknown23183('6168653235325f31366578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 727-826
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(16)
        sprite('ahe252_14', 2)	# 827-828
        Unknown23183('6168653235325f31346578000000000000000000000000000000000000000000020000000200000038000000')
        GFX_0('ahe_homing_wind_eff', 103)
        Unknown36(1)
        Unknown1073(90000)
        Unknown35()
        sprite('ahe252_17', 2)	# 829-830
        Unknown23183('6168653235325f31376578000000000000000000000000000000000000000000020000000200000038000000')
        Unknown23183('6168653235325f3135000000000000000000000000000000000000000000000002000000020000003f000000')
        sprite('ahe252_18', 1)	# 831-831
        Unknown23183('6168653235325f31386578000000000000000000000000000000000000000000010000000200000038000000')
        Unknown23183('6168653235325f3136000000000000000000000000000000000000000000000001000000020000003f000000')
        sprite('keep', 100)	# 832-931
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(0)
        sprite('ahe252_06', 2)	# 932-933
        Unknown23183('6168653235325f30366578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_07', 1)	# 934-934
        Unknown23183('6168653235325f30376578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 935-1034
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(1)
        sprite('ahe252_08', 2)	# 1035-1036
        Unknown23183('6168653235325f30386578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_09', 1)	# 1037-1037
        Unknown23183('6168653235325f30396578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 1038-1137
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(2)
        sprite('ahe252_10', 2)	# 1138-1139
        Unknown23183('6168653235325f31306578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_11', 1)	# 1140-1140
        Unknown23183('6168653235325f31306578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 1141-1240
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(3)
        sprite('ahe032_02ex01', 2)	# 1241-1242
        Unknown23183('6168653033325f30326578303200000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe032_03ex01', 1)	# 1243-1243
        Unknown23183('6168653033325f30336578303200000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 1244-1343
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(4)
        sprite('ahe252_12', 2)	# 1344-1345
        Unknown23183('6168653235325f31326578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_13', 1)	# 1346-1346
        Unknown23183('6168653235325f31336578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 1347-1446
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(5)
        sprite('ahe252_15', 2)	# 1447-1448
        Unknown23183('6168653235325f31356578000000000000000000000000000000000000000000020000000200000038000000')
        sprite('ahe252_16', 1)	# 1449-1449
        Unknown23183('6168653235325f31366578000000000000000000000000000000000000000000010000000200000038000000')
        sprite('keep', 100)	# 1450-1549
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(6)
        sprite('ahe252_17', 2)	# 1550-1551
        Unknown23183('6168653235325f31376578000000000000000000000000000000000000000000020000000200000038000000')
        Unknown23183('6168653235325f3135000000000000000000000000000000000000000000000002000000020000003e000000')
        Unknown23183('6168653235325f3135657830310000000000000000000000000000000000000002000000020000003d000000')
        Unknown23183('6168653235325f3135000000000000000000000000000000000000000000000002000000020000003f000000')
        sprite('ahe252_18', 1)	# 1552-1552
        Unknown23183('6168653235325f31386578000000000000000000000000000000000000000000010000000200000038000000')
        Unknown23183('6168653235325f3136000000000000000000000000000000000000000000000001000000020000003e000000')
        Unknown23183('6168653235325f3136657830310000000000000000000000000000000000000001000000020000003d000000')
        Unknown23183('6168653235325f3136000000000000000000000000000000000000000000000001000000020000003f000000')
        sprite('keep', 100)	# 1553-1652
        callSubroutine('CheckAnimAngle')
        ExitState()
        label(100)
        sprite('keep', 100)	# 1653-1752
        clearUponHandler(3)
        Unknown1019(50)
        YAccel(25)
        Unknown1051(0)
        if SLOT_125:
            physicsYImpulse(1000)
        if (SLOT_13 >= 1):
            physicsYImpulse(10000)
        enterState('CmnActJumpDown')

    @State
    def LandAssaultA():

        def upon_IMMEDIATE():
            AttackDefaults_StandingSpecial()
            AttackLevel_(3)
            Damage(2000)
            AttackP1(80)
            Unknown9154(28)
            AirUntechableTime(30)
            AirPushbackX(15000)
            AirPushbackY(16000)
            Unknown11056(0)
            loopRelated(17, 6)

            def upon_17():
                sendToLabel(1)
            callSubroutine('HomingCancelLand')
            Unknown2004(1, 0)
            callSubroutine('HoseiPlus')

            def upon_3():
                Unknown23073()
        sprite('ahe400_00', 3)	# 1-3
        sprite('ahe400_01', 3)	# 4-6
        sprite('ahe400_02', 3)	# 7-9
        sprite('ahe400_03', 3)	# 10-12
        label(0)
        sprite('ahe400_01', 3)	# 13-15
        sprite('ahe400_02', 3)	# 16-18
        sprite('ahe400_03', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe400_04', 2)	# 22-23
        physicsXImpulse(15000)
        Unknown8009(0)
        SFX_3('ahese_03')
        Unknown2015(175)
        Unknown7006('ahe201_0', 100, 845506657, 828322096, 0, 0, 100, 845506657, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe400_04', 1)	# 24-24
        Unknown1019(150)
        Unknown8006(100, 1, 0)
        sprite('ahe400_05', 1)	# 25-25
        sprite('ahe400_05', 2)	# 26-27
        Unknown1019(200)
        sprite('ahe400_06', 2)	# 28-29	 **attackbox here**
        RefreshMultihit()
        GFX_0('ahe400_attack_eff', 100)
        Unknown38(8, 1)
        GFX_0('ahe400_dust_eff', 100)
        Unknown8006(100, 1, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
            clearUponHandler(10)
            sendToLabel(2)

        def upon_12():
            SLOT_51 = 1
            clearUponHandler(12)
        sprite('ahe400_07', 2)	# 30-31	 **attackbox here**
        label(2)
        sprite('ahe200_06', 3)	# 32-34	 **attackbox here**
        if SLOT_2:
            Unknown23029(8, 5031, 0)
        clearUponHandler(10)
        clearUponHandler(12)
        StartMultihit()
        Recovery()
        Unknown1019(50)
        sprite('ahe200_07', 3)	# 35-37
        Unknown23183('6168653230305f30370000000000000000000000000000000000000000000000040000000200000033000000')
        Unknown1019(50)
        sprite('ahe200_08', 3)	# 38-40
        Unknown23183('6168653230305f30380000000000000000000000000000000000000000000000040000000200000033000000')
        Unknown1019(50)
        sprite('ahe200_09', 3)	# 41-43
        Unknown23183('6168653230305f30390000000000000000000000000000000000000000000000040000000200000033000000')
        Unknown1019(50)
        Unknown14077(0)
        sprite('ahe200_10', 4)	# 44-47
        Unknown1019(50)
        sprite('ahe200_11', 4)	# 48-51
        Unknown1084(1)

    @State
    def LandAssaultB():

        def upon_IMMEDIATE():
            AttackDefaults_StandingSpecial()
            AttackLevel_(4)
            Damage(2300)
            AttackP1(80)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            AirUntechableTime(30)
            AirPushbackX(7000)
            AirPushbackY(24000)
            Hitstop(18)
            Unknown11056(0)
            Unknown11068(1)
            loopRelated(17, 18)

            def upon_17():
                sendToLabel(1)
            callSubroutine('AHE_SousaiArmor')
            callSubroutine('HomingCancelLand')
            Unknown2004(1, 0)
            callSubroutine('HoseiPlus')

            def upon_3():
                Unknown23073()
        sprite('ahe400_00', 3)	# 1-3
        sprite('ahe400_01', 3)	# 4-6
        sprite('ahe400_02', 3)	# 7-9
        setInvincible(1)
        sprite('ahe400_03', 3)	# 10-12
        label(0)
        sprite('ahe400_01', 3)	# 13-15
        sprite('ahe400_02', 3)	# 16-18
        sprite('ahe400_03', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe400_04', 2)	# 22-23
        setInvincible(0)
        physicsXImpulse(25000)
        Unknown8009(0)
        SFX_3('ahese_03')
        Unknown2015(175)
        Unknown7006('ahe201_0', 100, 845506657, 828322096, 0, 0, 100, 845506657, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe400_04', 1)	# 24-24
        Unknown1019(150)
        Unknown8006(100, 1, 0)
        sprite('ahe400_05', 1)	# 25-25
        sprite('ahe400_05', 2)	# 26-27
        Unknown1019(200)
        sprite('ahe400_06', 2)	# 28-29	 **attackbox here**
        RefreshMultihit()
        GFX_0('ahe400_attack_eff', 100)
        Unknown38(8, 1)
        GFX_0('ahe401_dust_eff', 100)
        Unknown8006(100, 1, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
            clearUponHandler(10)
            sendToLabel(2)

        def upon_12():
            SLOT_51 = 1
            clearUponHandler(12)
        sprite('ahe400_07', 2)	# 30-31	 **attackbox here**
        sprite('ahe400_08', 2)	# 32-33	 **attackbox here**
        Unknown8006(100, 1, 0)
        label(2)
        sprite('ahe200_06', 3)	# 34-36	 **attackbox here**
        if SLOT_2:
            Unknown23029(8, 5031, 0)
        clearUponHandler(10)
        clearUponHandler(12)
        StartMultihit()
        Recovery()
        Unknown1019(55)
        sprite('ahe200_07', 3)	# 37-39
        Unknown23183('6168653230305f30370000000000000000000000000000000000000000000000040000000200000033000000')
        Unknown1019(55)
        sprite('ahe200_08', 3)	# 40-42
        Unknown23183('6168653230305f30380000000000000000000000000000000000000000000000040000000200000033000000')
        Unknown1019(55)
        sprite('ahe200_09', 3)	# 43-45
        Unknown23183('6168653230305f30390000000000000000000000000000000000000000000000040000000200000033000000')
        Unknown1019(55)
        Unknown14077(0)
        sprite('ahe200_10', 4)	# 46-49
        Unknown1019(55)
        sprite('ahe200_11', 4)	# 50-53
        Unknown1084(1)

    @State
    def LandAssaultEx():

        def upon_IMMEDIATE():
            AttackDefaults_StandingSpecial()
            AttackLevel_(4)
            Damage(2600)
            AttackP1(80)
            callSubroutine('InitArcanaBound')
            AirUntechableTime(29)
            AirHitstunAfterWallbounce(40)
            Hitstop(20)
            Unknown11001(0, 5, 10)
            Unknown11056(0)
            loopRelated(17, 6)

            def upon_17():
                sendToLabel(1)
            callSubroutine('ExSkillInit')
            callSubroutine('HomingCancelLand')
            Unknown2004(1, 0)
            callSubroutine('HoseiPlus')

            def upon_3():
                Unknown23073()
        sprite('ahe400_00', 3)	# 1-3
        sprite('ahe400_01', 3)	# 4-6
        Unknown23125('')
        Unknown2058(-5000)
        sprite('ahe400_02', 3)	# 7-9
        sprite('ahe400_03', 3)	# 10-12
        label(0)
        sprite('ahe400_01', 3)	# 13-15
        sprite('ahe400_02', 3)	# 16-18
        sprite('ahe400_03', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe400_04', 2)	# 22-23
        physicsXImpulse(20000)
        Unknown8009(0)
        SFX_3('ahese_03')
        Unknown2015(175)
        Unknown7006('ahe201_0', 100, 845506657, 828322096, 0, 0, 100, 845506657, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe400_04', 2)	# 24-25
        Unknown1019(150)
        Unknown8006(100, 1, 0)
        sprite('ahe400_05', 2)	# 26-27
        Unknown1019(200)
        sprite('ahe400_06', 2)	# 28-29	 **attackbox here**
        RefreshMultihit()
        GFX_0('ahe400_attack_eff', 100)
        Unknown38(8, 1)
        GFX_0('ahe401_dust_eff', 100)
        GFX_0('ahe402_dust_eff', 100)
        Unknown38(9, 1)
        Unknown8006(100, 1, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
            clearUponHandler(10)
            sendToLabel(2)

        def upon_12():
            SLOT_51 = 1
            clearUponHandler(12)
        sprite('ahe400_07', 2)	# 30-31	 **attackbox here**
        sprite('ahe400_08', 2)	# 32-33	 **attackbox here**
        Unknown8006(100, 1, 0)
        sprite('ahe400_09', 2)	# 34-35	 **attackbox here**
        label(2)
        sprite('ahe200_06', 3)	# 36-38	 **attackbox here**
        if SLOT_2:
            Unknown23029(8, 5031, 0)
            Unknown23029(9, 5032, 0)
        clearUponHandler(10)
        StartMultihit()
        Recovery()
        Unknown1019(50)
        sprite('ahe200_07', 3)	# 39-41
        Unknown23183('6168653230305f30370000000000000000000000000000000000000000000000050000000200000033000000')
        Unknown1019(50)
        sprite('ahe200_08', 3)	# 42-44
        Unknown23183('6168653230305f30380000000000000000000000000000000000000000000000050000000200000033000000')
        Unknown1019(50)
        sprite('ahe200_09', 3)	# 45-47
        Unknown23183('6168653230305f30390000000000000000000000000000000000000000000000050000000200000033000000')
        Unknown1019(50)
        Unknown14077(0)
        sprite('ahe200_10', 4)	# 48-51
        Unknown1019(50)
        sprite('ahe200_11', 4)	# 52-55
        Unknown1084(1)

    @State
    def LandShotA():

        def upon_IMMEDIATE():
            AttackDefaults_StandingSpecial()
            loopRelated(17, 14)

            def upon_17():
                sendToLabel(1)

            def upon_3():
                Unknown23073()
        sprite('ahe403_00', 3)	# 1-3
        sprite('ahe403_01', 3)	# 4-6
        GFX_0('ahe403_footcircle_eff', 100)
        Unknown7006('ahe202_0', 100, 845506657, 828322352, 0, 0, 100, 845506657, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe403_02', 3)	# 7-9
        sprite('ahe403_03', 3)	# 10-12
        label(0)
        sprite('ahe403_01', 3)	# 13-15
        sprite('ahe403_02', 3)	# 16-18
        sprite('ahe403_03', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe403_04', 2)	# 22-23
        sprite('ahe403_05', 2)	# 24-25
        sprite('ahe403_06', 3)	# 26-28
        callSubroutine('DeriveHomingCancelInputLand')
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4031, 0)
        GFX_0('ahe403_circle_eff', 0)
        sprite('ahe403_07', 3)	# 29-31
        callSubroutine('DeriveHomingCancelTimingLand')
        sprite('ahe403_08', 3)	# 32-34
        sprite('ahe403_09', 3)	# 35-37
        sprite('ahe403_06', 3)	# 38-40
        callSubroutine('DeriveHomingCancelClear')
        Recovery()
        Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_07', 3)	# 41-43
        sprite('ahe403_08', 3)	# 44-46
        sprite('ahe403_09', 3)	# 47-49
        sprite('ahe403_06', 3)	# 50-52
        sprite('ahe403_10', 3)	# 53-55
        sprite('ahe403_11', 3)	# 56-58

    @State
    def LandShotB():

        def upon_IMMEDIATE():
            AttackDefaults_StandingSpecial()
            loopRelated(17, 24)

            def upon_17():
                sendToLabel(1)

            def upon_3():
                Unknown23073()
        sprite('ahe403_00', 3)	# 1-3
        sprite('ahe403_01', 3)	# 4-6
        GFX_0('ahe403_footcircle_eff', 100)
        Unknown7006('ahe202_0', 100, 845506657, 828322352, 0, 0, 100, 845506657, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe403_02', 3)	# 7-9
        sprite('ahe403_03', 3)	# 10-12
        label(0)
        sprite('ahe403_01', 3)	# 13-15
        sprite('ahe403_02', 3)	# 16-18
        sprite('ahe403_03', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe403_04', 2)	# 22-23
        sprite('ahe403_05', 2)	# 24-25
        sprite('ahe403_06', 3)	# 26-28
        callSubroutine('DeriveHomingCancelInputLand')
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4032, 0)
        GFX_0('ahe403_circle_eff', 0)
        sprite('ahe403_07', 3)	# 29-31
        sprite('ahe403_08', 3)	# 32-34
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4033, 0)
        sprite('ahe403_09', 3)	# 35-37
        sprite('ahe403_06', 3)	# 38-40
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4034, 0)
        sprite('ahe403_07', 3)	# 41-43
        callSubroutine('DeriveHomingCancelTimingLand')
        sprite('ahe403_08', 3)	# 44-46
        sprite('ahe403_09', 3)	# 47-49
        sprite('ahe403_06', 3)	# 50-52
        callSubroutine('DeriveHomingCancelClear')
        Recovery()
        Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_07', 3)	# 53-55
        sprite('ahe403_08', 3)	# 56-58
        sprite('ahe403_09', 3)	# 59-61
        sprite('ahe403_10', 3)	# 62-64
        sprite('ahe403_11', 3)	# 65-67

    @State
    def LandShotEx():

        def upon_IMMEDIATE():
            AttackDefaults_StandingSpecial()

            def upon_3():
                Unknown23073()

            def upon_STATE_END():
                Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
                Unknown21012('6168653430355f636972636c655f65666600000000000000000000000000000020000000')
                Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_00', 3)	# 1-3
        sprite('ahe403_01', 3)	# 4-6
        Unknown23125('')
        Unknown2058(-5000)
        GFX_0('ahe403_footcircle_eff', 100)
        Unknown7006('ahe203_0', 100, 845506657, 828322608, 0, 0, 100, 845506657, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe403_02', 3)	# 7-9
        sprite('ahe403_03', 3)	# 10-12
        sprite('ahe403_04', 2)	# 13-14
        sprite('ahe403_05', 2)	# 15-16
        sprite('ahe403_06', 3)	# 17-19
        callSubroutine('DeriveHomingCancelInputLand')
        GFX_0('ShotEx_Obj', 0)
        GFX_0('ahe405_circle_eff', 0)
        GFX_0('ahe405_shot_eff', 0)
        sprite('ahe403_07', 3)	# 20-22
        callSubroutine('DeriveHomingCancelTimingLand')
        sprite('ahe403_08', 3)	# 23-25
        sprite('ahe403_09', 3)	# 26-28
        sprite('ahe403_06', 3)	# 29-31
        callSubroutine('DeriveHomingCancelClear')
        Recovery()
        Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_07', 3)	# 32-34
        sprite('ahe403_08', 3)	# 35-37
        sprite('ahe403_09', 3)	# 38-40
        sprite('ahe403_10', 3)	# 41-43
        sprite('ahe403_11', 3)	# 44-46

    @Subroutine
    def AirShotPosYLimit():

        def upon_3():
            if (SLOT_23 < 15000):
                teleportRelativeY(15000)
                Unknown1084(1)
            Unknown23073()

    @State
    def AirShotA():

        def upon_IMMEDIATE():
            Unknown17003()
            clearUponHandler(2)
            callSubroutine('AirShotPosYLimit')
            loopRelated(17, 14)

            def upon_17():
                sendToLabel(1)
        sprite('ahe403_12', 3)	# 1-3
        sprite('ahe403_13', 3)	# 4-6
        Unknown1017()
        Unknown1022()
        Unknown1019(10)
        YAccel(10)
        setGravity(50)
        Unknown1051(0)
        GFX_0('ahe403_footcircle_eff', 100)
        Unknown7006('ahe202_0', 100, 845506657, 828322352, 0, 0, 100, 845506657, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe403_14', 3)	# 7-9
        sprite('ahe403_15', 3)	# 10-12
        label(0)
        sprite('ahe403_13', 3)	# 13-15
        sprite('ahe403_14', 3)	# 16-18
        sprite('ahe403_15', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe403_16', 2)	# 22-23
        sprite('ahe403_17', 2)	# 24-25
        sprite('ahe403_18', 3)	# 26-28
        callSubroutine('DeriveHomingCancelInput')
        Unknown1084(1)
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4031, 0)
        GFX_0('ahe403_circle_eff', 0)
        sprite('ahe403_19', 3)	# 29-31
        callSubroutine('DeriveHomingCancelTiming')
        sprite('ahe403_20', 3)	# 32-34
        sprite('ahe403_21', 3)	# 35-37
        sprite('ahe403_18', 3)	# 38-40
        callSubroutine('DeriveHomingCancelClear')
        Recovery()
        Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_19', 3)	# 41-43
        sprite('ahe403_20', 3)	# 44-46
        sprite('ahe403_21', 3)	# 47-49
        sprite('ahe403_18', 3)	# 50-52
        sprite('ahe403_22', 3)	# 53-55
        Unknown1043()
        clearUponHandler(3)
        Unknown28(2, 'CmnActJumpLanding')
        sprite('ahe403_23', 3)	# 56-58
        label(100)
        sprite('ahe020_07', 3)	# 59-61
        sprite('ahe020_08', 3)	# 62-64
        loopRest()
        gotoLabel(100)

    @State
    def AirShotB():

        def upon_IMMEDIATE():
            Unknown17003()
            clearUponHandler(2)
            callSubroutine('AirShotPosYLimit')
            loopRelated(17, 24)

            def upon_17():
                sendToLabel(1)
        sprite('ahe403_12', 3)	# 1-3
        sprite('ahe403_13', 3)	# 4-6
        Unknown1017()
        Unknown1022()
        Unknown1019(10)
        YAccel(10)
        setGravity(50)
        Unknown1051(0)
        GFX_0('ahe403_footcircle_eff', 100)
        Unknown7006('ahe202_0', 100, 845506657, 828322352, 0, 0, 100, 845506657, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe403_14', 3)	# 7-9
        sprite('ahe403_15', 3)	# 10-12
        label(0)
        sprite('ahe403_13', 3)	# 13-15
        sprite('ahe403_14', 3)	# 16-18
        sprite('ahe403_15', 3)	# 19-21
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe403_16', 2)	# 22-23
        sprite('ahe403_17', 2)	# 24-25
        sprite('ahe403_18', 3)	# 26-28
        callSubroutine('DeriveHomingCancelInput')
        Unknown1084(1)
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4032, 0)
        GFX_0('ahe403_circle_eff', 0)
        sprite('ahe403_19', 3)	# 29-31
        sprite('ahe403_20', 3)	# 32-34
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4033, 0)
        sprite('ahe403_21', 3)	# 35-37
        sprite('ahe403_18', 3)	# 38-40
        GFX_0('Shot_Obj', 0)
        Unknown23029(1, 4034, 0)
        sprite('ahe403_19', 3)	# 41-43
        callSubroutine('DeriveHomingCancelTiming')
        sprite('ahe403_20', 3)	# 44-46
        sprite('ahe403_21', 3)	# 47-49
        sprite('ahe403_18', 3)	# 50-52
        callSubroutine('DeriveHomingCancelClear')
        Recovery()
        Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_19', 3)	# 53-55
        sprite('ahe403_20', 3)	# 56-58
        sprite('ahe403_21', 3)	# 59-61
        sprite('ahe403_22', 3)	# 62-64
        Unknown1043()
        clearUponHandler(3)
        Unknown28(2, 'CmnActJumpLanding')
        sprite('ahe403_23', 3)	# 65-67
        label(100)
        sprite('ahe020_07', 3)	# 68-70
        sprite('ahe020_08', 3)	# 71-73
        loopRest()
        gotoLabel(100)

    @State
    def AirShotEx():

        def upon_IMMEDIATE():
            Unknown17003()
            clearUponHandler(2)
            callSubroutine('AirShotPosYLimit')

            def upon_STATE_END():
                Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
                Unknown21012('6168653430355f636972636c655f65666600000000000000000000000000000020000000')
                Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_12', 3)	# 1-3
        sprite('ahe403_13', 3)	# 4-6
        Unknown1017()
        Unknown1022()
        Unknown1019(25)
        YAccel(25)
        setGravity(250)
        Unknown23125('')
        Unknown2058(-5000)
        GFX_0('ahe403_footcircle_eff', 100)
        GFX_0('ahe403_footparticle_eff', 100)
        Unknown7006('ahe203_0', 100, 845506657, 828322608, 0, 0, 100, 845506657, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe403_14', 3)	# 7-9
        sprite('ahe403_15', 3)	# 10-12
        sprite('ahe403_16', 2)	# 13-14
        sprite('ahe403_17', 2)	# 15-16
        sprite('ahe403_18', 3)	# 17-19
        callSubroutine('DeriveHomingCancelInput')
        Unknown1084(1)
        GFX_0('ShotEx_Obj', 0)
        GFX_0('ahe405_circle_eff', 0)
        GFX_0('ahe405_shot_eff', 0)
        sprite('ahe403_19', 3)	# 20-22
        callSubroutine('DeriveHomingCancelTiming')
        sprite('ahe403_20', 3)	# 23-25
        sprite('ahe403_21', 3)	# 26-28
        sprite('ahe403_18', 3)	# 29-31
        callSubroutine('DeriveHomingCancelClear')
        Recovery()
        Unknown21012('6168653430335f636972636c655f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430335f666f6f74636972636c655f656666000000000000000000000020000000')
        sprite('ahe403_19', 3)	# 32-34
        sprite('ahe403_20', 3)	# 35-37
        sprite('ahe403_21', 3)	# 38-40
        sprite('ahe403_22', 3)	# 41-43
        Unknown1043()
        clearUponHandler(3)
        Unknown28(2, 'CmnActJumpLanding')
        sprite('ahe403_23', 3)	# 44-46
        label(100)
        sprite('ahe020_07', 3)	# 47-49
        sprite('ahe020_08', 3)	# 50-52
        loopRest()
        gotoLabel(100)

    @State
    def AirAssaultA():

        def upon_IMMEDIATE():
            Unknown17003()
            AttackLevel_(3)
            Damage(2200)
            AttackP1(80)
            AirUntechableTime(30)
            AirPushbackX(5000)
            AirPushbackY(-35000)
            HitOverhead(2)
            GroundedHitstunAnimation(1)
            Unknown11068(1)
            loopRelated(17, 9)

            def upon_17():
                sendToLabel(1)

            def upon_STATE_END():
                Unknown2006()
            callSubroutine('HomingCancel')
            clearUponHandler(2)
            callSubroutine('HoseiPlus')

            def upon_3():
                Unknown23073()
        sprite('ahe406_00', 3)	# 1-3
        sprite('ahe406_00ex01', 3)	# 4-6
        Unknown1084(1)
        physicsXImpulse(15000)
        physicsYImpulse(10000)
        setGravity(1000)
        sprite('ahe406_00ex02', 3)	# 7-9
        Unknown7006('ahe204_0', 100, 845506657, 828322864, 0, 0, 100, 845506657, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe406_00ex03', 3)	# 10-12
        label(0)
        sprite('ahe406_00', 3)	# 13-15
        sprite('ahe406_00ex01', 3)	# 16-18
        sprite('ahe406_00ex02', 3)	# 19-21
        sprite('ahe406_00ex03', 3)	# 22-24
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe406_01', 2)	# 25-26
        Unknown1019(50)
        SFX_3('ahese_01')
        sprite('ahe406_02', 2)	# 27-28
        GFX_0('ahe406_attack_eff', 0)
        GFX_0('ahe406_dust_eff', 100)
        sprite('ahe406_03', 3)	# 29-31	 **attackbox here**
        physicsYImpulse(-40000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown2003(1)
            Recovery()
            Unknown1084(1)
            sendToLabel(3)
        sprite('ahe406_04', 3)	# 32-34	 **attackbox here**
        label(2)
        sprite('ahe406_03', 3)	# 35-37	 **attackbox here**
        sprite('ahe406_04', 3)	# 38-40	 **attackbox here**
        loopRest()
        gotoLabel(2)
        label(3)
        sprite('ahe406_05', 3)	# 41-43
        callSubroutine('HomingCancelLand')
        Unknown21012('6168653430365f61747461636b5f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430365f647573745f656666000000000000000000000000000000000020000000')
        sprite('ahe406_06', 3)	# 44-46	 **attackbox here**
        sprite('ahe406_07', 3)	# 47-49
        sprite('ahe010_02', 3)	# 50-52
        sprite('ahe010_01', 3)	# 53-55
        sprite('ahe010_00', 3)	# 56-58

    @State
    def AirAssaultB():

        def upon_IMMEDIATE():
            Unknown17003()
            AttackLevel_(4)
            Damage(2500)
            AttackP1(80)
            AirUntechableTime(30)
            AirPushbackX(5000)
            AirPushbackY(-35000)
            Unknown9310(13)
            HitOverhead(2)
            GroundedHitstunAnimation(1)
            Unknown11068(1)
            loopRelated(17, 18)

            def upon_17():
                sendToLabel(1)

            def upon_STATE_END():
                Unknown2006()

            def upon_78():
                Unknown2037(1)

            def upon_3():
                Unknown23073()
            callSubroutine('HomingCancel')
            clearUponHandler(2)
            callSubroutine('HoseiPlus')
        sprite('ahe406_00', 3)	# 1-3
        sprite('ahe406_00ex01', 3)	# 4-6
        Unknown1084(1)
        physicsXImpulse(15000)
        physicsYImpulse(10000)
        setGravity(1000)
        sprite('ahe406_00ex02', 3)	# 7-9
        Unknown7006('ahe204_0', 100, 845506657, 828322864, 0, 0, 100, 845506657, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe406_00ex03', 3)	# 10-12
        label(0)
        sprite('ahe406_00', 3)	# 13-15
        sprite('ahe406_00ex01', 3)	# 16-18
        sprite('ahe406_00ex02', 3)	# 19-21
        sprite('ahe406_00ex03', 3)	# 22-24
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe406_01', 2)	# 25-26
        Unknown1019(50)
        SFX_3('ahese_01')
        sprite('ahe406_02', 2)	# 27-28
        GFX_0('ahe406_attack_eff', 0)
        GFX_0('ahe407_dust_eff', 100)
        sprite('ahe406_03', 3)	# 29-31	 **attackbox here**
        physicsYImpulse(-40000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown2003(1)
            Recovery()
            Unknown1084(1)
            sendToLabel(3)
        sprite('ahe406_04', 3)	# 32-34	 **attackbox here**
        label(2)
        sprite('ahe406_03', 3)	# 35-37	 **attackbox here**
        sprite('ahe406_04', 3)	# 38-40	 **attackbox here**
        loopRest()
        gotoLabel(2)
        label(3)
        sprite('ahe406_05', 3)	# 41-43
        callSubroutine('HomingCancelLand')
        Unknown21012('6168653430365f61747461636b5f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430375f647573745f656666000000000000000000000000000000000020000000')
        sprite('ahe406_06', 3)	# 44-46	 **attackbox here**
        Unknown23183('6168653430365f30360000000000000000000000000000000000000000000000040000000200000002000000')
        sprite('ahe406_07', 3)	# 47-49
        Unknown23183('6168653430365f30370000000000000000000000000000000000000000000000040000000200000002000000')
        sprite('ahe010_02', 4)	# 50-53
        Unknown23183('6168653031305f30320000000000000000000000000000000000000000000000050000000200000002000000')
        sprite('ahe010_01', 4)	# 54-57
        Unknown23183('6168653031305f30310000000000000000000000000000000000000000000000050000000200000002000000')
        sprite('ahe010_00', 4)	# 58-61
        Unknown23183('6168653031305f30300000000000000000000000000000000000000000000000050000000200000002000000')

    @State
    def AirAssaultEx():

        def upon_IMMEDIATE():
            Unknown17003()
            AttackLevel_(4)
            Damage(2800)
            AttackP1(80)
            AirUntechableTime(45)
            AirPushbackX(5000)
            AirPushbackY(-50000)
            Unknown9310(13)
            HitOverhead(2)
            GroundedHitstunAnimation(1)
            Unknown11068(1)
            callSubroutine('ExSkillInit')
            loopRelated(17, 9)

            def upon_17():
                sendToLabel(1)

            def upon_78():
                Unknown2037(1)

            def upon_STATE_END():
                Unknown2006()
            callSubroutine('HomingCancel')
            clearUponHandler(2)
            callSubroutine('HoseiPlus')

            def upon_3():
                Unknown23073()
        sprite('ahe406_00', 3)	# 1-3
        sprite('ahe406_00ex01', 3)	# 4-6
        Unknown1084(1)
        physicsXImpulse(15000)
        physicsYImpulse(10000)
        setGravity(1000)
        Unknown23125('')
        Unknown2058(-5000)
        sprite('ahe406_00ex02', 3)	# 7-9
        Unknown7006('ahe204_0', 100, 845506657, 828322864, 0, 0, 100, 845506657, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
        sprite('ahe406_00ex03', 3)	# 10-12
        label(0)
        sprite('ahe406_00', 3)	# 13-15
        sprite('ahe406_00ex01', 3)	# 16-18
        sprite('ahe406_00ex02', 3)	# 19-21
        sprite('ahe406_00ex03', 3)	# 22-24
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe406_01', 2)	# 25-26
        Unknown1019(50)
        SFX_3('ahese_01')
        sprite('ahe406_02', 2)	# 27-28
        GFX_0('ahe406_attack_eff', 0)
        GFX_0('ahe407_dust_eff', 100)
        GFX_0('ahe408_dust_eff', 100)
        sprite('ahe406_03', 3)	# 29-31	 **attackbox here**
        physicsYImpulse(-40000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown2003(1)
            Recovery()
            Unknown1084(1)
            sendToLabel(3)
        sprite('ahe406_04', 3)	# 32-34	 **attackbox here**
        label(2)
        sprite('ahe406_03', 3)	# 35-37	 **attackbox here**
        sprite('ahe406_04', 3)	# 38-40	 **attackbox here**
        loopRest()
        gotoLabel(2)
        label(3)
        sprite('ahe406_05', 3)	# 41-43
        callSubroutine('HomingCancelLand')
        Unknown21012('6168653430365f61747461636b5f65666600000000000000000000000000000020000000')
        Unknown21012('6168653430375f647573745f656666000000000000000000000000000000000020000000')
        Unknown21012('6168653430385f647573745f656666000000000000000000000000000000000020000000')
        sprite('ahe406_06', 3)	# 44-46	 **attackbox here**
        sprite('ahe406_07', 3)	# 47-49
        sprite('ahe010_02', 3)	# 50-52
        sprite('ahe010_01', 3)	# 53-55
        sprite('ahe010_00', 3)	# 56-58

    @Subroutine
    def Delete_Eff():
        Unknown26('ahe403_circle_eff')
        Unknown26('ahe403_circle1_eff')
        Unknown26('ahe403_circle2_eff')
        Unknown26('ahe403_footcircle_eff')
        Unknown26('ahe403_footcircle1_eff')
        Unknown26('ahe403_footcircle2_eff')
        Unknown26('ahe403_footparticle_eff')
        Unknown26('ahe403_footparticle1_eff')
        Unknown26('ahe403_footparticle2_eff')
        Unknown26('ahe403_footparticle3_eff')
        Unknown26('ahe403_footparticle4_eff')
        Unknown26('ahe405_circle_eff')
        Unknown26('ahe405_circle1a_eff')
        Unknown26('ahe405_circle1b_eff')
        Unknown26('ahe405_circle2a_eff')
        Unknown26('ahe405_circle2b_eff')

    @State
    def UltimateLandAssault():

        def upon_IMMEDIATE():
            AttackDefaults_StandingDD()
            Unknown23055('')
            AttackLevel_(5)
            Damage(5200)
            Unknown11091(31)
            GroundedHitstunAnimation(1)
            AirPushbackX(80000)
            AirPushbackY(38000)
            AirUntechableTime(120)
            Hitstop(20)
            Unknown11001(0, -2, 3)
            Unknown11056(0)
            Unknown2016(250)
            loopRelated(17, 80)

            def upon_17():
                sendToLabel(1)
            Unknown2004(1, 0)
            callSubroutine('Delete_Eff')
        sprite('ahe400_00', 3)	# 1-3
        setInvincible(1)
        sprite('ahe400_01', 3)	# 4-6
        GFX_0('ahe430_hold_eff', 100)
        sprite('ahe430_00', 3)	# 7-9
        Unknown2036(72, -1, 0)
        Unknown30080('')
        Unknown2058(-10000)
        Unknown7006('ahe250_0', 100, 845506657, 828321845, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        sprite('ahe430_01', 3)	# 10-12
        sprite('ahe430_02', 3)	# 13-15
        sprite('ahe430_03', 3)	# 16-18
        sprite('ahe430_04', 3)	# 19-21
        sprite('ahe400_01', 3)	# 22-24
        sprite('ahe430_00', 3)	# 25-27
        sprite('ahe430_01', 3)	# 28-30
        sprite('ahe430_02', 3)	# 31-33
        sprite('ahe430_03', 3)	# 34-36
        sprite('ahe430_04', 3)	# 37-39
        label(0)
        sprite('ahe400_01', 2)	# 40-41
        sprite('ahe430_00', 2)	# 42-43
        sprite('ahe430_01', 2)	# 44-45
        sprite('ahe430_02', 2)	# 46-47
        sprite('ahe430_03', 2)	# 48-49
        sprite('ahe430_04', 2)	# 50-51
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe400_04', 2)	# 52-53
        physicsXImpulse(20000)
        Unknown8009(0)
        SFX_1('ahe251')
        sprite('ahe400_04', 1)	# 54-54
        Unknown1019(200)
        Unknown8006(100, 1, 0)
        sprite('ahe400_05', 1)	# 55-55
        sprite('ahe400_05', 2)	# 56-57
        Unknown1019(200)
        SFX_3('ahese_03')
        sprite('ahe430_05', 3)	# 58-60	 **attackbox here**
        RefreshMultihit()
        GFX_0('ahe430_attack_eff', 100)
        GFX_0('ahe430_magical_eff', 100)
        Unknown8006(100, 1, 0)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2037(1)
            clearUponHandler(10)
            sendToLabel(2)

        def upon_12():
            clearUponHandler(12)
            SFX_0('025_cleanhit_grap')
        sprite('ahe430_06', 3)	# 61-63	 **attackbox here**
        setInvincible(0)
        Unknown8006(100, 1, 0)
        sprite('ahe430_07', 3)	# 64-66	 **attackbox here**
        Unknown8006(100, 1, 0)
        sprite('ahe430_08', 3)	# 67-69	 **attackbox here**
        Unknown8006(100, 1, 0)
        label(2)
        sprite('keep', 3)	# 70-72
        StartMultihit()
        setInvincible(0)
        sprite('ahe200_06', 6)	# 73-78	 **attackbox here**
        StartMultihit()
        Unknown1019(40)
        sprite('ahe200_07', 6)	# 79-84
        Unknown1019(40)
        sprite('ahe200_08', 6)	# 85-90
        Unknown1019(40)
        sprite('ahe200_09', 6)	# 91-96
        Unknown1019(40)
        sprite('ahe200_10', 6)	# 97-102
        Unknown1019(40)
        sprite('ahe200_11', 6)	# 103-108
        Unknown1084(1)

    @State
    def UltimateLandAssaultSP():

        def upon_IMMEDIATE():
            AttackDefaults_StandingDD()
            Unknown23055('')
            AttackLevel_(5)
            Damage(6200)
            Unknown11091(29)
            GroundedHitstunAnimation(1)
            AirPushbackX(80000)
            AirPushbackY(45000)
            AirUntechableTime(120)
            Unknown9310(26)
            Hitstop(30)
            Unknown11001(0, -2, 3)
            Unknown11056(0)
            Unknown2016(250)
            loopRelated(17, 80)

            def upon_17():
                sendToLabel(1)
            Unknown2004(1, 0)
            callSubroutine('Delete_Eff')
        sprite('ahe400_00', 3)	# 1-3
        setInvincible(1)
        sprite('ahe400_01', 3)	# 4-6
        GFX_0('ahe430_hold_eff', 100)
        sprite('ahe430_00', 3)	# 7-9
        Unknown2036(72, -1, 0)
        Unknown30080('')
        Unknown2058(-10000)
        Unknown7006('ahe250_0', 100, 845506657, 828321845, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        sprite('ahe430_01', 3)	# 10-12
        sprite('ahe430_02', 3)	# 13-15
        sprite('ahe430_03', 3)	# 16-18
        sprite('ahe430_04', 3)	# 19-21
        sprite('ahe400_01', 3)	# 22-24
        sprite('ahe430_00', 3)	# 25-27
        sprite('ahe430_01', 3)	# 28-30
        sprite('ahe430_02', 3)	# 31-33
        sprite('ahe430_03', 3)	# 34-36
        sprite('ahe430_04', 3)	# 37-39
        sprite('ahe400_01', 2)	# 40-41
        sprite('ahe430_00', 2)	# 42-43
        sprite('ahe430_01', 2)	# 44-45
        sprite('ahe430_02', 2)	# 46-47
        sprite('ahe430_03', 2)	# 48-49
        sprite('ahe430_04', 2)	# 50-51
        sprite('ahe400_01', 2)	# 52-53
        sprite('ahe430_00', 2)	# 54-55
        sprite('ahe430_01', 2)	# 56-57
        sprite('ahe430_02', 2)	# 58-59
        sprite('ahe430_03', 2)	# 60-61
        sprite('ahe430_04', 2)	# 62-63
        label(0)
        sprite('ahe400_01', 1)	# 64-64
        sprite('ahe430_00', 1)	# 65-65
        sprite('ahe430_01', 1)	# 66-66
        sprite('ahe430_02', 1)	# 67-67
        sprite('ahe430_03', 1)	# 68-68
        sprite('ahe430_04', 1)	# 69-69
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe400_04', 2)	# 70-71
        physicsXImpulse(20000)
        Unknown8009(0)
        SFX_1('ahe251')
        sprite('ahe400_04', 1)	# 72-72
        Unknown1019(200)
        Unknown8006(100, 1, 0)
        sprite('ahe400_05', 1)	# 73-73
        sprite('ahe400_05', 2)	# 74-75
        Unknown1019(200)
        SFX_3('ahese_03')
        sprite('ahe430_05', 3)	# 76-78	 **attackbox here**
        RefreshMultihit()
        GFX_0('ahe430_attack_eff', 100)
        GFX_0('ahe430_magical_eff', 100)
        Unknown8006(100, 1, 0)

        def upon_12():
            clearUponHandler(12)
            Unknown2037(1)
            SFX_0('025_cleanhit_grap')
            sendToLabel(100)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            sendToLabel(2)
        sprite('ahe430_06', 3)	# 79-81	 **attackbox here**
        if (not SLOT_2):
            setInvincible(0)
        Unknown8006(100, 1, 0)
        sprite('ahe430_07', 3)	# 82-84	 **attackbox here**
        Unknown8006(100, 1, 0)
        sprite('ahe430_08', 3)	# 85-87	 **attackbox here**
        Unknown8006(100, 1, 0)
        label(2)
        sprite('keep', 3)	# 88-90
        StartMultihit()
        setInvincible(0)
        if SLOT_2:
            sendToLabel(100)
        sprite('ahe200_06', 6)	# 91-96	 **attackbox here**
        StartMultihit()
        Unknown1019(40)
        sprite('ahe200_07', 6)	# 97-102
        Unknown1019(40)
        sprite('ahe200_08', 6)	# 103-108
        Unknown1019(40)
        sprite('ahe200_09', 6)	# 109-114
        Unknown1019(40)
        sprite('ahe200_10', 6)	# 115-120
        Unknown1019(40)
        sprite('ahe200_11', 6)	# 121-126
        Unknown1084(1)
        ExitState()
        label(100)
        sprite('ahe200_06', 5)	# 127-131	 **attackbox here**
        StartMultihit()
        setInvincible(1)
        sprite('ahe600_00', 5)	# 132-136
        Unknown8006(100, 1, 0)
        Unknown1019(50)
        sprite('ahe600_01', 5)	# 137-141
        sprite('ahe600_00', 5)	# 142-146
        Unknown1019(50)
        sprite('ahe600_01', 5)	# 147-151
        sprite('ahe600_00', 5)	# 152-156
        Unknown1019(50)
        sprite('ahe600_01', 5)	# 157-161
        sprite('ahe600_00', 5)	# 162-166
        Unknown1019(50)
        sprite('ahe600_01', 5)	# 167-171
        sprite('ahe032_06', 3)	# 172-174
        teleportRelativeX(20000)
        Unknown1084(1)
        Unknown1047(3000)
        sprite('ahe032_07', 3)	# 175-177
        sprite('ahe032_08', 3)	# 178-180
        sprite('ahe274_07', 4)	# 181-184
        sprite('ahe274_08', 4)	# 185-188
        sprite('ahe271_06', 4)	# 189-192
        sprite('ahe271_07', 6)	# 193-198
        sprite('ahe271_08', 6)	# 199-204
        sprite('ahe271_09', 6)	# 205-210
        ExitState()

    @State
    def UltimateUpper():

        def upon_IMMEDIATE():
            AttackDefaults_StandingDD()
            Unknown23055('')
            AttackLevel_(5)
            Damage(1500)
            Unknown11091(30)
            AirHitstunAnimation(10)
            GroundedHitstunAnimation(10)
            Unknown11092(1)
            AirUntechableTime(90)
            PushbackX(12000)
            AirPushbackX(2500)
            AirPushbackY(30000)
            Unknown11072(1, 10000, 25000)

            def upon_78():
                clearUponHandler(78)
                Hitstop(30)
                Unknown13024(0)
                sendToLabel(100)
                Unknown11069('UltimateUpper')
                Unknown11064(1)
                clearUponHandler(2)

                def upon_LANDING():
                    clearUponHandler(2)
                    Unknown1084(1)
                    Unknown8000(100, 1, 1)
                    Unknown13024(1)
                    sendToLabel(110)
                SFX_0('025_cleanhit_grap')
            callSubroutine('Delete_Eff')

            def upon_14():
                Unknown21015('6168653433315f77696e675f6566660000000000000000000000000000000000c60f000000000000')
        sprite('ahe320_00', 3)	# 1-3
        setInvincible(1)
        sprite('ahe320_01', 45)	# 4-48
        Unknown2036(44, -1, 0)
        Unknown30080('')
        Unknown2058(-10000)
        tag_voice(1, 'ahe252_0', 'ahe252_1', '', '')
        sprite('ahe320_02', 3)	# 49-51
        GFX_0('ahe320_attack_eff', 0)
        sprite('ahe320_03ex', 3)	# 52-54	 **attackbox here**
        GFX_0('ahe431_attack_eff', 0)
        sprite('ahe320_04', 2)	# 55-56
        sprite('ahe320_05', 2)	# 57-58
        sprite('ahe320_06', 3)	# 59-61	 **attackbox here**
        StartMultihit()
        clearUponHandler(78)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(10)
        physicsXImpulse(10000)
        physicsYImpulse(35000)
        setGravity(1300)
        AirPushbackY(40000)
        GFX_0('ahe320_attack3_eff', 0)
        GFX_0('ahe431_wing_eff', 0)
        sprite('ahe320_07', 3)	# 62-64	 **attackbox here**
        RefreshMultihit()
        Damage(3500)
        Unknown11091(30)
        Unknown9215()
        Unknown11072(0, 0, 0)
        setInvincible(0)
        sprite('ahe320_08', 3)	# 65-67	 **attackbox here**
        sprite('ahe320_09', 3)	# 68-70	 **attackbox here**
        GFX_0('UltimateUpper_Obj', 0)
        Unknown1019(25)
        sprite('ahe320_10', 6)	# 71-76
        GFX_0('ahe320_heart_eff', 0)
        SFX_3('ahese_00')
        sprite('ahe320_11', 6)	# 77-82
        sprite('ahe320_12', 6)	# 83-88
        sprite('ahe320_13', 6)	# 89-94
        sprite('ahe320_14', 6)	# 95-100
        label(0)
        sprite('ahe020_07', 3)	# 101-103
        sprite('ahe020_08', 3)	# 104-106
        loopRest()
        gotoLabel(0)
        label(10)
        sprite('ahe010_02', 2)	# 107-108
        sprite('ahe010_01', 2)	# 109-110
        sprite('ahe010_00', 2)	# 111-112
        sprite('ahe000_00', 2)	# 113-114	 **attackbox here**
        ExitState()
        label(100)
        sprite('ahe320_04', 3)	# 115-117
        StartMultihit()
        Unknown21012('6168653433315f61747461636b5f65666600000000000000000000000000000020000000')
        tag_voice(0, '', 'ahe253', '', '')
        sprite('ahe320_05', 3)	# 118-120
        sprite('ahe320_06', 3)	# 121-123	 **attackbox here**
        RefreshMultihit()
        Damage(800)
        Unknown11091(15)
        AirPushbackX(500)
        AirPushbackY(45000)
        Hitstop(1)
        Unknown11072(1, 125000, 150000)
        Unknown30048(1)
        Unknown11084(1)
        Unknown9310(1)
        physicsXImpulse(2500)
        physicsYImpulse(50000)
        setGravity(1300)
        GFX_0('ahe431_attack_upper_eff', 0)
        GFX_0('ahe431_hit_wing_eff', 0)
        tag_voice(0, 'ahe253', '', '', '')
        sprite('ahe320_07', 3)	# 124-126	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 3)	# 127-129	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 3)	# 130-132	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 3)	# 133-135	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 3)	# 136-138	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 3)	# 139-141	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 3)	# 142-144	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 3)	# 145-147	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 3)	# 148-150	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 3)	# 151-153	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 3)	# 154-156	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 3)	# 157-159	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 3)	# 160-162	 **attackbox here**
        RefreshMultihit()
        GFX_0('UltimateUpper_Obj', 0)
        Unknown11069('')
        Unknown11064(0)
        Unknown1019(25)
        sprite('ahe320_10', 6)	# 163-168
        GFX_0('ahe431_heart_eff', 0)
        SFX_3('ahese_00')
        sprite('ahe320_11', 6)	# 169-174
        sprite('ahe320_12', 6)	# 175-180
        sprite('ahe320_13', 6)	# 181-186
        sprite('ahe320_14', 6)	# 187-192
        loopRest()
        gotoLabel(0)
        label(110)
        sprite('ahe010_02', 2)	# 193-194
        sprite('ahe010_01', 2)	# 195-196
        sprite('ahe010_00', 2)	# 197-198
        sprite('ahe000_00', 2)	# 199-200	 **attackbox here**
        sprite('ahe300_00', 3)	# 201-203
        sprite('ahe300_01', 3)	# 204-206	 **attackbox here**
        sprite('ahe300_02', 3)	# 207-209
        sprite('ahe300_03', 3)	# 210-212
        sprite('ahe300_04', 3)	# 213-215
        sprite('ahe300_04ex2', 20)	# 216-235	 **attackbox here**
        sprite('ahe300_05', 4)	# 236-239
        sprite('ahe300_06', 4)	# 240-243

    @State
    def UltimateUpperSP():

        def upon_IMMEDIATE():
            AttackDefaults_StandingDD()
            Unknown23055('')
            AttackLevel_(5)
            Damage(1700)
            Unknown11091(20)
            AirHitstunAnimation(10)
            GroundedHitstunAnimation(10)
            Unknown11092(1)
            AirUntechableTime(90)
            PushbackX(12000)
            AirPushbackX(2500)
            AirPushbackY(30000)
            Unknown11072(1, 10000, 25000)

            def upon_78():
                clearUponHandler(78)
                Hitstop(30)
                Unknown13024(0)
                sendToLabel(100)
                Unknown11069('UltimateUpperSP')
                Unknown11064(1)
                clearUponHandler(2)

                def upon_LANDING():
                    clearUponHandler(2)
                    Unknown1084(1)
                    Unknown8000(100, 1, 1)
                    Unknown13024(1)
                    sendToLabel(110)
                SFX_0('025_cleanhit_grap')
            callSubroutine('Delete_Eff')

            def upon_14():
                Unknown21015('6168653433315f77696e675f6566660000000000000000000000000000000000c60f000000000000')
        sprite('ahe320_00', 3)	# 1-3
        setInvincible(1)
        sprite('ahe320_01', 60)	# 4-63
        Unknown2036(59, -1, 0)
        Unknown30080('')
        Unknown2058(-10000)
        tag_voice(1, 'ahe252_0', 'ahe252_1', '', '')
        sprite('ahe320_02', 3)	# 64-66
        GFX_0('ahe320_attack_eff', 0)
        sprite('ahe320_03ex', 3)	# 67-69	 **attackbox here**
        GFX_0('ahe431_attack_eff', 0)
        sprite('ahe320_04', 2)	# 70-71
        sprite('ahe320_05', 2)	# 72-73
        sprite('ahe320_06', 3)	# 74-76	 **attackbox here**
        StartMultihit()
        clearUponHandler(78)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(10)
        physicsXImpulse(10000)
        physicsYImpulse(35000)
        setGravity(1300)
        AirPushbackY(40000)
        GFX_0('ahe320_attack3_eff', 0)
        GFX_0('ahe431_wing_eff', 0)
        sprite('ahe320_07', 3)	# 77-79	 **attackbox here**
        RefreshMultihit()
        Damage(3500)
        Unknown11091(30)
        Unknown9215()
        Unknown11072(0, 0, 0)
        setInvincible(0)
        sprite('ahe320_08', 3)	# 80-82	 **attackbox here**
        GFX_0('ahe320_heart_eff', 0)
        SFX_3('ahese_00')
        sprite('ahe320_09', 3)	# 83-85	 **attackbox here**
        GFX_0('UltimateUpper_Obj', 0)
        Unknown1019(25)
        sprite('ahe320_10', 6)	# 86-91
        sprite('ahe320_11', 6)	# 92-97
        sprite('ahe320_12', 6)	# 98-103
        sprite('ahe320_13', 6)	# 104-109
        sprite('ahe320_14', 6)	# 110-115
        label(0)
        sprite('ahe020_07', 3)	# 116-118
        sprite('ahe020_08', 3)	# 119-121
        loopRest()
        gotoLabel(0)
        label(10)
        sprite('ahe010_02', 2)	# 122-123
        sprite('ahe010_01', 2)	# 124-125
        sprite('ahe010_00', 2)	# 126-127
        sprite('ahe000_00', 2)	# 128-129	 **attackbox here**
        ExitState()
        label(100)
        sprite('ahe320_04', 3)	# 130-132
        StartMultihit()
        Unknown21012('6168653433315f61747461636b5f65666600000000000000000000000000000020000000')
        tag_voice(0, '', 'ahe253', '', '')
        sprite('ahe320_05', 3)	# 133-135
        sprite('ahe320_06', 3)	# 136-138	 **attackbox here**
        RefreshMultihit()
        Damage(600)
        Unknown11091(15)
        AirPushbackX(500)
        AirPushbackY(42000)
        Hitstop(1)
        Unknown11072(1, 125000, 150000)
        Unknown30048(1)
        Unknown11084(1)
        Unknown9310(1)
        physicsXImpulse(2500)
        physicsYImpulse(60000)
        setGravity(1300)
        GFX_0('ahe431_attack_upper_eff', 0)
        GFX_0('ahe431_hit_wing_eff', 0)
        tag_voice(0, 'ahe253', '', '', '')
        sprite('ahe320_07', 3)	# 139-141	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 3)	# 142-144	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 3)	# 145-147	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 3)	# 148-150	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 3)	# 151-153	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 3)	# 154-156	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 3)	# 157-159	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 3)	# 160-162	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 3)	# 163-165	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 3)	# 166-168	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 3)	# 169-171	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 3)	# 172-174	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 3)	# 175-177	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 2)	# 178-179	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 2)	# 180-181	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 2)	# 182-183	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 2)	# 184-185	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_06', 1)	# 186-186	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_07', 1)	# 187-187	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_08', 1)	# 188-188	 **attackbox here**
        RefreshMultihit()
        sprite('ahe320_09', 1)	# 189-189	 **attackbox here**
        RefreshMultihit()
        GFX_0('UltimateUpper_Obj', 0)
        Unknown11069('')
        Unknown11064(0)
        Unknown1019(25)
        sprite('ahe320_10', 6)	# 190-195
        GFX_0('ahe431_heart_eff', 0)
        SFX_3('ahese_00')
        sprite('ahe320_11', 6)	# 196-201
        sprite('ahe320_12', 6)	# 202-207
        sprite('ahe320_13', 6)	# 208-213
        sprite('ahe320_14', 6)	# 214-219
        loopRest()
        gotoLabel(0)
        label(110)
        sprite('ahe010_02', 2)	# 220-221
        sprite('ahe010_01', 2)	# 222-223
        sprite('ahe010_00', 2)	# 224-225
        sprite('ahe000_00', 2)	# 226-227	 **attackbox here**
        sprite('ahe300_00', 3)	# 228-230
        sprite('ahe300_01', 3)	# 231-233	 **attackbox here**
        sprite('ahe300_02', 3)	# 234-236
        sprite('ahe300_03', 3)	# 237-239
        sprite('ahe300_04', 3)	# 240-242
        sprite('ahe300_04ex2', 20)	# 243-262	 **attackbox here**
        sprite('ahe300_05', 4)	# 263-266
        sprite('ahe300_06', 4)	# 267-270

    @State
    def UltimateAirAssault():

        def upon_IMMEDIATE():
            AttackDefaults_AirDD()
            Unknown23055('')
            AttackLevel_(5)
            Damage(5800)
            Unknown11091(33)
            GroundedHitstunAnimation(1)
            AirUntechableTime(60)
            AirPushbackX(2500)
            AirPushbackY(-70000)
            YImpluseBeforeWallbounce(1)
            Unknown9190(1)
            Unknown9118(20)
            HitOverhead(2)

            def upon_12():
                clearUponHandler(12)
                Hitstop(20)
                SFX_0('025_cleanhit_grap')
            loopRelated(17, 44)

            def upon_17():
                sendToLabel(1)
            clearUponHandler(2)
            callSubroutine('Delete_Eff')
        sprite('ahe406_00', 3)	# 1-3
        setInvincible(1)
        sprite('ahe406_00ex01', 3)	# 4-6
        Unknown2036(43, -1, 0)
        Unknown30080('')
        Unknown2058(-10000)
        Unknown1084(1)
        physicsXImpulse(5000)
        physicsYImpulse(7500)
        setGravity(250)
        SFX_1('ahe254')
        sprite('ahe406_00ex02', 3)	# 7-9
        sprite('ahe406_00ex03', 3)	# 10-12
        sprite('ahe406_00', 2)	# 13-14
        sprite('ahe406_00ex01', 2)	# 15-16
        sprite('ahe406_00ex02', 2)	# 17-18
        sprite('ahe406_00ex03', 2)	# 19-20
        sprite('ahe406_00', 2)	# 21-22
        sprite('ahe406_00ex01', 2)	# 23-24
        sprite('ahe406_00ex02', 2)	# 25-26
        sprite('ahe406_00ex03', 2)	# 27-28
        label(0)
        sprite('ahe406_00', 1)	# 29-29
        sprite('ahe406_00ex01', 1)	# 30-30
        sprite('ahe406_00ex02', 1)	# 31-31
        sprite('ahe406_00ex03', 1)	# 32-32
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe406_01', 2)	# 33-34
        Unknown1019(50)
        SFX_3('ahese_01')
        SFX_1('ahe255')
        sprite('ahe406_02', 2)	# 35-36
        GFX_0('ahe432_attack_eff', 0)
        GFX_0('ahe432_particle_eff', 100)
        GFX_0('ahe432_dust_eff', 100)
        sprite('ahe406_03', 3)	# 37-39	 **attackbox here**
        physicsYImpulse(-60000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            clearUponHandler(12)
            Unknown1084(1)
            setInvincible(0)
            sendToLabel(3)
        sprite('ahe406_04', 3)	# 40-42	 **attackbox here**
        setInvincible(0)
        label(2)
        sprite('ahe406_03', 3)	# 43-45	 **attackbox here**
        sprite('ahe406_04', 3)	# 46-48	 **attackbox here**
        loopRest()
        gotoLabel(2)
        label(3)
        sprite('ahe406_05', 3)	# 49-51
        AttackLevel_(4)
        Damage(3000)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown9191()
        PushbackX(19800)
        AirPushbackX(10000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(2000)
        Unknown11034(0)
        Unknown11033(2)
        AttackP1(80)
        AttackP2(80)
        Unknown11058('0000000000000000000000000100000000000000')
        HitOverhead(0)
        Unknown21012('6168653433325f61747461636b5f65666600000000000000000000000000000020000000')
        ScreenShake(0, 40000)
        sprite('ahe406_06', 3)	# 52-54	 **attackbox here**
        sprite('ahe406_07', 3)	# 55-57
        sprite('ahe010_02', 4)	# 58-61
        sprite('ahe010_01', 4)	# 62-65
        sprite('ahe010_00', 4)	# 66-69

    @State
    def UltimateAirAssaultSP():

        def upon_IMMEDIATE():
            AttackDefaults_AirDD()
            Unknown23055('')
            AttackLevel_(5)
            Damage(6800)
            Unknown11091(31)
            GroundedHitstunAnimation(1)
            AirUntechableTime(60)
            AirPushbackX(2500)
            AirPushbackY(-70000)
            YImpluseBeforeWallbounce(1)
            Unknown9190(1)
            Unknown9118(20)
            HitOverhead(2)

            def upon_12():
                clearUponHandler(12)
                Hitstop(20)
                SFX_0('025_cleanhit_grap')
            loopRelated(17, 44)

            def upon_17():
                sendToLabel(1)
            clearUponHandler(2)
            callSubroutine('Delete_Eff')
        sprite('ahe406_00', 3)	# 1-3
        setInvincible(1)
        sprite('ahe406_00ex01', 3)	# 4-6
        Unknown2036(43, -1, 0)
        Unknown30080('')
        Unknown2058(-10000)
        Unknown1084(1)
        physicsXImpulse(5000)
        physicsYImpulse(7500)
        setGravity(250)
        SFX_1('ahe254')
        sprite('ahe406_00ex02', 3)	# 7-9
        sprite('ahe406_00ex03', 3)	# 10-12
        sprite('ahe406_00', 2)	# 13-14
        sprite('ahe406_00ex01', 2)	# 15-16
        sprite('ahe406_00ex02', 2)	# 17-18
        sprite('ahe406_00ex03', 2)	# 19-20
        sprite('ahe406_00', 2)	# 21-22
        sprite('ahe406_00ex01', 2)	# 23-24
        sprite('ahe406_00ex02', 2)	# 25-26
        sprite('ahe406_00ex03', 2)	# 27-28
        label(0)
        sprite('ahe406_00', 1)	# 29-29
        sprite('ahe406_00ex01', 1)	# 30-30
        sprite('ahe406_00ex02', 1)	# 31-31
        sprite('ahe406_00ex03', 1)	# 32-32
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe406_01', 2)	# 33-34
        Unknown1019(50)
        SFX_3('ahese_01')
        SFX_1('ahe255')
        sprite('ahe406_02', 2)	# 35-36
        GFX_0('ahe432_attack_eff', 0)
        GFX_0('ahe432_particle_eff', 100)
        GFX_0('ahe432_dust_eff', 100)
        sprite('ahe406_03', 3)	# 37-39	 **attackbox here**
        physicsYImpulse(-60000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            clearUponHandler(12)
            Unknown1084(1)
            setInvincible(0)
            sendToLabel(3)
        sprite('ahe406_04', 3)	# 40-42	 **attackbox here**
        setInvincible(0)
        label(2)
        sprite('ahe406_03', 3)	# 43-45	 **attackbox here**
        sprite('ahe406_04', 3)	# 46-48	 **attackbox here**
        loopRest()
        gotoLabel(2)
        label(3)
        sprite('ahe406_05', 3)	# 49-51
        AttackLevel_(4)
        Damage(3000)
        Hitstop(0)
        AirUntechableTime(60)
        Unknown9191()
        PushbackX(19800)
        AirPushbackX(10000)
        AirPushbackY(30000)
        YImpluseBeforeWallbounce(2000)
        Unknown11034(0)
        Unknown11033(2)
        AttackP1(80)
        AttackP2(80)
        Unknown11058('0000000000000000000000000100000000000000')
        HitOverhead(0)
        Unknown21012('6168653433325f61747461636b5f65666600000000000000000000000000000020000000')
        ScreenShake(0, 40000)
        sprite('ahe406_06', 3)	# 52-54	 **attackbox here**
        sprite('ahe406_07', 3)	# 55-57
        sprite('ahe010_02', 4)	# 58-61
        sprite('ahe010_01', 4)	# 62-65
        sprite('ahe010_00', 4)	# 66-69

    @State
    def AstralHeat():

        def upon_IMMEDIATE():
            AttackDefaults_Astral()
            AttackLevel_(5)
            Damage(0)
            Hitstop(30)
            Unknown11066(1)
            Unknown11064(1)
            GroundedHitstunAnimation(1)
            AirPushbackX(5000)
            AirPushbackY(40000)
            AirUntechableTime(120)
            Unknown11072(1, 150000, 50000)
            Unknown11067(1)
            loopRelated(17, 80)

            def upon_17():
                sendToLabel(1)
            Unknown2004(1, 0)

            def upon_78():
                Unknown20007(1)
                Unknown20003(1)
                Unknown23088(1, 1)
                Unknown11069('AstralHeatExe')
                enterState('AstralHeatExe')
            callSubroutine('Delete_Eff')
        sprite('ahe450_00', 3)	# 1-3
        setInvincible(1)
        Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
        GFX_0('AstralHeatCutInObject', -1)
        Unknown2036(80, -1, 1)
        Unknown23147()
        GFX_0('ahe450_hold_eff', 100)
        SFX_1('ahe290')
        sprite('ahe450_01', 3)	# 4-6
        sprite('ahe450_02', 3)	# 7-9
        sprite('ahe450_03', 3)	# 10-12
        sprite('ahe450_04', 3)	# 13-15
        sprite('ahe450_05', 3)	# 16-18
        sprite('ahe450_06', 3)	# 19-21
        sprite('ahe450_01', 2)	# 22-23
        sprite('ahe450_02', 2)	# 24-25
        sprite('ahe450_03', 2)	# 26-27
        sprite('ahe450_04', 2)	# 28-29
        sprite('ahe450_05', 2)	# 30-31
        sprite('ahe450_06', 2)	# 32-33
        sprite('ahe450_01', 2)	# 34-35
        sprite('ahe450_02', 2)	# 36-37
        sprite('ahe450_03', 2)	# 38-39
        sprite('ahe450_04', 2)	# 40-41
        sprite('ahe450_05', 2)	# 42-43
        sprite('ahe450_06', 2)	# 44-45
        label(0)
        sprite('ahe450_01', 1)	# 46-46
        sprite('ahe450_02', 1)	# 47-47
        sprite('ahe450_03', 1)	# 48-48
        sprite('ahe450_04', 1)	# 49-49
        sprite('ahe450_05', 1)	# 50-50
        sprite('ahe450_06', 1)	# 51-51
        loopRest()
        gotoLabel(0)
        label(1)
        sprite('ahe450_07', 3)	# 52-54
        SFX_3('ahese_03')
        SFX_1('ahe291')
        sprite('ahe450_08', 3)	# 55-57	 **attackbox here**
        RefreshMultihit()
        physicsXImpulse(35000)
        physicsYImpulse(35000)
        Unknown1043()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(10)
        GFX_0('ahe450_punch_eff', 100)
        GFX_0('ahe450_impact_eff', 0)
        sprite('ahe450_09', 3)	# 58-60	 **attackbox here**
        sprite('ahe450_10', 3)	# 61-63	 **attackbox here**
        sprite('ahe450_11', 3)	# 64-66	 **attackbox here**
        sprite('ahe320_10', 6)	# 67-72
        setInvincible(0)
        Unknown1019(50)
        Unknown23024(0)
        GFX_0('ahe450_heart_eff', 0)
        sprite('ahe320_11', 6)	# 73-78
        sprite('ahe320_12', 6)	# 79-84
        sprite('ahe320_13', 6)	# 85-90
        sprite('ahe320_14', 6)	# 91-96
        label(2)
        sprite('ahe020_07', 3)	# 97-99
        sprite('ahe020_08', 3)	# 100-102
        loopRest()
        gotoLabel(2)
        label(10)
        sprite('ahe010_02', 2)	# 103-104
        sprite('ahe010_01', 2)	# 105-106
        sprite('ahe010_00', 2)	# 107-108
        sprite('ahe000_00', 2)	# 109-110	 **attackbox here**
        ExitState()

    @State
    def AstralHeatExe():

        def upon_IMMEDIATE():
            AttackDefaults_Astral()
            AttackLevel_(5)
            Damage(5000)
            Unknown11091(100)
            Hitstop(30)
            Unknown11064(1)
            Unknown11084(1)
            Unknown11066(1)
            Unknown11067(1)
            GroundedHitstunAnimation(1)
            AirPushbackX(0)
            AirPushbackY(1250)
            YImpluseBeforeWallbounce(5)
            AirUntechableTime(360)
            Unknown2004(1, 0)

            def upon_12():
                clearUponHandler(12)
                Unknown23029(1, 4501, 0)
                sendToLabel(100)

            def upon_LANDING():
                clearUponHandler(2)
                Unknown1084(1)
                Unknown8000(100, 1, 1)
                sendToLabel(10)
            Unknown2037(0)

            def upon_43():
                if (SLOT_48 == 4506):
                    Unknown2037(1)
            Unknown23027()
            setInvincible(1)
            Unknown2017(0)
            Unknown2034(0)
            Unknown2053(0)

            def upon_STATE_END():
                Unknown2017(1)
                Unknown2034(1)
                Unknown2053(1)
            GFX_0('AstralCameraObject', -1)
            Unknown38(6, 1)
            Unknown23084(1)
            Unknown23157(0)
        sprite('ahe450_09', 3)	# 1-3	 **attackbox here**
        physicsXImpulse(85000)
        physicsYImpulse(25000)
        Unknown21012('6168653435305f70756e63685f6566660000000000000000000000000000000020000000')
        sprite('ahe450_10', 3)	# 4-6	 **attackbox here**
        sprite('ahe450_11', 3)	# 7-9	 **attackbox here**
        sprite('ahe113_02', 2)	# 10-11
        Unknown2006()
        Unknown1084(1)
        sprite('ahe450_08ex', 3)	# 12-14	 **attackbox here**
        physicsXImpulse(85000)
        physicsYImpulse(25000)
        sprite('ahe450_09ex', 3)	# 15-17	 **attackbox here**
        RefreshMultihit()
        Unknown11023(1)
        Unknown23024(2)
        sprite('ahe450_09ex', 3)	# 18-20	 **attackbox here**
        sprite('ahe450_10ex', 3)	# 21-23	 **attackbox here**
        sprite('ahe450_11ex', 3)	# 24-26	 **attackbox here**
        sprite('ahe320_10', 6)	# 27-32
        Unknown23084(0)
        Unknown20003(0)
        setInvincible(0)
        Unknown1019(25)
        YAccel(25)
        Unknown1043()
        Unknown23024(0)
        Unknown23029(6, 4504, 0)
        sprite('ahe320_11', 6)	# 33-38
        sprite('ahe320_12', 6)	# 39-44
        sprite('ahe320_13', 6)	# 45-50
        sprite('ahe320_14', 6)	# 51-56
        label(1)
        sprite('ahe020_07', 3)	# 57-59
        sprite('ahe020_08', 3)	# 60-62
        loopRest()
        gotoLabel(1)
        label(10)
        sprite('ahe010_02', 2)	# 63-64
        sprite('ahe010_01', 2)	# 65-66
        sprite('ahe010_00', 2)	# 67-68
        sprite('ahe000_00', 2)	# 69-70	 **attackbox here**
        ExitState()
        label(100)
        sprite('ahe450_09', 3)	# 71-73	 **attackbox here**
        Unknown1019(80)
        YAccel(80)
        sprite('ahe450_10', 3)	# 74-76	 **attackbox here**
        Unknown1019(80)
        YAccel(80)
        sprite('ahe450_11', 3)	# 77-79	 **attackbox here**
        Unknown1019(80)
        YAccel(80)
        sprite('ahe450_12', 3)	# 80-82
        Unknown1019(80)
        YAccel(80)
        sprite('ahe450_13', 3)	# 83-85
        Unknown1019(80)
        YAccel(80)
        sprite('ahe450_14', 6)	# 86-91
        Unknown2036(60, -1, 2)
        Unknown23029(6, 4502, 0)
        sprite('ahe450_15', 6)	# 92-97
        Unknown1084(1)
        Unknown23024(3)
        Unknown20010(-70000, 0, 0)
        GFX_0('AstralHeatCutInLoveArcana', -1)
        Unknown38(7, 1)
        GFX_0('ahe450_circle_eff', 100)
        GFX_0('ahe450_tinkle_eff', 100)
        Unknown23118(6225920)
        sprite('ahe450_16', 6)	# 98-103
        sprite('ahe450_17', 6)	# 104-109
        sprite('ahe450_18', 40)	# 110-149
        sprite('ahe450_19', 6)	# 150-155
        sprite('ahe450_20', 6)	# 156-161
        Unknown23029(7, 4513, 0)
        sprite('ahe450_21', 6)	# 162-167
        sprite('ahe450_22', 6)	# 168-173
        Unknown23029(6, 4503, 0)
        sprite('ahe450_23', 3)	# 174-176
        GFX_0('AstralFinishAttackObject', -1)
        GFX_0('AstralHeatPal', -1)
        Unknown23015(7)
        loopRelated(17, 200)

        def upon_17():
            sendToLabel(102)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(106)
        sprite('ahe450_24', 3)	# 177-179
        sprite('ahe450_25', 3)	# 180-182
        SFX_1('ahe292')
        sprite('ahe450_26', 3)	# 183-185
        label(101)
        sprite('ahe450_24', 3)	# 186-188
        sprite('ahe450_25', 3)	# 189-191
        sprite('ahe450_26', 3)	# 192-194
        loopRest()
        gotoLabel(101)
        label(102)
        sprite('ahe450_27', 4)	# 195-198
        loopRelated(17, 490)

        def upon_17():
            sendToLabel(104)
        sprite('ahe450_28', 4)	# 199-202
        sprite('ahe450_29', 4)	# 203-206
        label(103)
        sprite('ahe450_30', 3)	# 207-209
        sprite('ahe450_31', 3)	# 210-212
        sprite('ahe450_32', 3)	# 213-215
        sprite('ahe450_33', 3)	# 216-218
        loopRest()
        gotoLabel(103)
        label(104)
        sprite('ahe450_34', 3)	# 219-221
        Unknown1000(260000)
        teleportRelativeY(1500000)
        Unknown1084(1)
        Unknown23029(6, 4505, 0)
        Unknown1043()
        Unknown23024(0)
        Unknown23015(0)
        Unknown26('ahe450_tinkle_eff')
        Unknown23118(-16777216)
        sprite('ahe450_35', 3)	# 222-224
        sprite('ahe020_07', 3)	# 225-227
        Unknown2006()
        sprite('ahe020_08', 3)	# 228-230
        label(105)
        sprite('ahe020_07', 3)	# 231-233
        sprite('ahe020_08', 3)	# 234-236
        loopRest()
        gotoLabel(105)
        label(106)
        sprite('ahe010_02', 3)	# 237-239
        Unknown23029(6, 4504, 0)
        Unknown23024(0)
        Unknown20010(0, 0, 0)
        if SLOT_2:
            Unknown20000(1)
            Unknown20004(1)
            Unknown20006(1)
            Unknown20003(1)
        else:
            Unknown23084(0)
            Unknown20003(0)
        sprite('ahe010_01', 3)	# 240-242
        sprite('ahe010_00', 3)	# 243-245
        sprite('ahe000_00', 3)	# 246-248	 **attackbox here**

    @Subroutine
    def MouthTableInit():
        Unknown18011('ahe520', 13921, 13923, 13921, 13155, 24881, 25399, 24887, 25401, 24887, 25401, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe521', 13921, 14179, 13921, 13667, 24888, 25401, 24889, 25401, 24889, 25399, 14385, 13921, 13923, 13921, 13923, 12641, 25394, 13617, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe522', 13921, 14179, 13921, 13155, 24880, 25401, 24889, 25401, 24889, 14385, 14179, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 12643, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe541', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe542', 13921, 13923, 13921, 13155, 24881, 25399, 24887, 25401, 24887, 25401, 12851, 12641, 25398, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe543', 13921, 13923, 13921, 13155, 24881, 25399, 24887, 25401, 24887, 25401, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe544', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 14179, 12641, 25394, 24887, 12849, 12899, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe545', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 14179, 12643, 24885, 25401, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe402_0', 14177, 14179, 13921, 13923, 13921, 13923, 13921, 13923, 13665, 13923, 13665, 13155, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe402_1', 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe403_0', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('ahe403_1', 12643, 13153, 25392, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    @State
    def CmnActEntry():
        label(0)
        sprite('null', 1)	# 1-1
        loopRest()
        if SLOT_17:
            _gotolabel(0)
        Unknown19(991, 2, 158)
        random_(2, 0, 50)
        if SLOT_0:
            _gotolabel(10)
        sprite('null', 60)	# 2-61
        SFX_1('ahe520')
        sprite('ahe032_02', 3)	# 62-64
        Unknown2034(0)
        Unknown2053(0)
        Unknown1000(-2000000)
        physicsXImpulse(20500)
        sprite('ahe032_03', 3)	# 65-67
        sprite('ahe032_04', 3)	# 68-70
        sprite('ahe032_02', 3)	# 71-73
        sprite('ahe032_03', 3)	# 74-76
        sprite('ahe032_04', 3)	# 77-79
        sprite('ahe032_02', 3)	# 80-82
        sprite('ahe032_03', 3)	# 83-85
        sprite('ahe032_04', 3)	# 86-88
        sprite('ahe600_00', 4)	# 89-92
        Unknown8006(100, 1, 0)
        Unknown1019(50)
        sprite('ahe600_01', 4)	# 93-96
        sprite('ahe600_00', 4)	# 97-100
        Unknown1019(50)
        sprite('ahe600_01', 4)	# 101-104
        sprite('ahe272_00', 4)	# 105-108
        Unknown1019(50)
        sprite('ahe272_01', 4)	# 109-112
        sprite('ahe272_00', 4)	# 113-116
        Unknown1019(50)
        sprite('ahe272_01', 4)	# 117-120
        sprite('ahe032_05', 3)	# 121-123
        teleportRelativeX(20000)
        Unknown1084(1)
        Unknown1047(3000)
        sprite('ahe032_06', 3)	# 124-126
        sprite('ahe032_07', 3)	# 127-129
        sprite('ahe032_08', 3)	# 130-132
        sprite('ahe000_00', 3)	# 133-135	 **attackbox here**
        Unknown1084(1)
        Unknown1000(-1230000)
        sprite('ahe300_00', 6)	# 136-141
        sprite('ahe300_01', 6)	# 142-147	 **attackbox here**
        sprite('ahe300_02', 6)	# 148-153
        sprite('ahe300_03', 6)	# 154-159
        sprite('ahe300_04', 6)	# 160-165
        sprite('ahe300_04ex2', 30)	# 166-195	 **attackbox here**
        sprite('ahe300_05', 6)	# 196-201
        sprite('ahe300_06', 6)	# 202-207
        Unknown21011(40)
        ExitState()
        label(10)
        sprite('ahe601_00', 5)	# 208-212	 **attackbox here**
        sprite('ahe601_01', 5)	# 213-217
        Unknown7006('ahe521', 100, 895838305, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        sprite('ahe601_02', 5)	# 218-222
        sprite('ahe601_03', 5)	# 223-227
        sprite('ahe601_04', 5)	# 228-232	 **attackbox here**
        sprite('ahe601_05', 5)	# 233-237	 **attackbox here**
        sprite('ahe601_06', 5)	# 238-242	 **attackbox here**
        sprite('ahe601_07', 5)	# 243-247	 **attackbox here**
        GFX_0('aheef601_eff', 100)
        sprite('ahe601_08', 5)	# 248-252	 **attackbox here**
        sprite('ahe601_09', 5)	# 253-257	 **attackbox here**
        sprite('ahe601_10', 5)	# 258-262
        sprite('ahe601_11', 5)	# 263-267
        sprite('ahe601_12', 5)	# 268-272
        sprite('ahe601_13', 5)	# 273-277
        label(11)
        sprite('ahe601_14', 6)	# 278-283	 **attackbox here**
        sprite('ahe601_14ex1', 6)	# 284-289	 **attackbox here**
        sprite('ahe601_14ex2', 6)	# 290-295	 **attackbox here**
        sprite('ahe601_14ex3', 6)	# 296-301	 **attackbox here**
        sprite('ahe601_14ex4', 6)	# 302-307	 **attackbox here**
        if SLOT_97:
            _gotolabel(11)
        sprite('ahe601_15', 3)	# 308-310
        Unknown21011(40)
        sprite('ahe601_15ex1', 3)	# 311-313
        ExitState()
        label(991)
        sprite('ahe000_00', 1)	# 314-314	 **attackbox here**
        Unknown2019(1000)
        Unknown21011(120)
        label(992)
        sprite('ahe000_00', 4)	# 315-318	 **attackbox here**
        sprite('ahe000_01', 4)	# 319-322	 **attackbox here**
        sprite('ahe000_02', 4)	# 323-326	 **attackbox here**
        sprite('ahe000_03', 4)	# 327-330	 **attackbox here**
        sprite('ahe000_04', 4)	# 331-334	 **attackbox here**
        sprite('ahe000_05', 4)	# 335-338	 **attackbox here**
        sprite('ahe000_06', 4)	# 339-342	 **attackbox here**
        sprite('ahe000_07', 4)	# 343-346	 **attackbox here**
        sprite('ahe000_08', 4)	# 347-350	 **attackbox here**
        sprite('ahe000_09', 4)	# 351-354	 **attackbox here**
        sprite('ahe000_10', 4)	# 355-358	 **attackbox here**
        sprite('ahe000_11', 4)	# 359-362	 **attackbox here**
        sprite('ahe000_12', 4)	# 363-366	 **attackbox here**
        sprite('ahe000_13', 4)	# 367-370	 **attackbox here**
        sprite('ahe000_14', 4)	# 371-374	 **attackbox here**
        sprite('ahe000_15', 4)	# 375-378	 **attackbox here**
        sprite('ahe000_16', 4)	# 379-382	 **attackbox here**
        sprite('ahe000_17', 4)	# 383-386	 **attackbox here**
        sprite('ahe000_18', 4)	# 387-390	 **attackbox here**
        sprite('ahe000_19', 4)	# 391-394	 **attackbox here**
        loopRest()
        gotoLabel(992)

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
        if (not SLOT_108):
            random_(2, 0, 50)
            if SLOT_0:
                _gotolabel(10)
        sprite('ahe610_00', 6)	# 4-9
        if SLOT_158:
            if SLOT_52:
                SFX_1('ahe544')
            elif SLOT_108:
                SFX_1('ahe402_1')
            else:
                Unknown7006('ahe402_0', 100, 895838305, 12596, 0, 0, 100, 895838305, 12596, 0, 0, 0, 0, 0, 0, 0, 0)
        sprite('ahe610_01', 6)	# 10-15
        sprite('ahe610_02', 6)	# 16-21	 **attackbox here**
        sprite('ahe610_03', 32767)	# 22-32788	 **attackbox here**
        Unknown23018(1)
        ExitState()
        label(10)
        sprite('ahe611_00', 6)	# 32789-32794
        sprite('ahe611_01', 6)	# 32795-32800
        if SLOT_158:
            if SLOT_52:
                SFX_1('ahe545')
            else:
                Unknown7006('ahe542', 100, 895838305, 13108, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        sprite('ahe611_02', 6)	# 32801-32806
        sprite('ahe611_03', 6)	# 32807-32812
        sprite('ahe611_04', 6)	# 32813-32818
        GFX_0('aheef611_eff', 100)
        SFX_3('ahese_55')
        sprite('ahe611_05', 6)	# 32819-32824
        sprite('ahe611_06', 6)	# 32825-32830
        sprite('ahe611_07', 6)	# 32831-32836
        sprite('ahe611_08', 6)	# 32837-32842	 **attackbox here**
        sprite('ahe611_09', 6)	# 32843-32848	 **attackbox here**
        sprite('ahe611_10', 6)	# 32849-32854	 **attackbox here**
        sprite('ahe611_11', 6)	# 32855-32860	 **attackbox here**
        sprite('ahe611_12', 32767)	# 32861-65627	 **attackbox here**
        Unknown23018(1)
        ExitState()

    @State
    def CmnActLose():
        label(0)
        sprite('ahe620_00', 6)	# 1-6
        sprite('ahe620_01', 6)	# 7-12
        Unknown7006('ahe403_0', 100, 879061089, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        sprite('ahe620_00', 6)	# 13-18
        sprite('ahe620_01', 6)	# 19-24
        sprite('ahe620_00', 6)	# 25-30
        sprite('ahe620_01', 6)	# 31-36
        sprite('ahe620_00', 6)	# 37-42
        sprite('ahe620_01', 6)	# 43-48
        sprite('ahe620_00', 6)	# 49-54
        sprite('ahe620_01', 6)	# 55-60
        sprite('ahe620_02', 6)	# 61-66
        sprite('ahe620_03', 6)	# 67-72
        sprite('ahe620_04', 6)	# 73-78
        sprite('ahe620_05', 6)	# 79-84
        sprite('ahe620_06', 6)	# 85-90
        sprite('ahe620_07', 32767)	# 91-32857
        Unknown21011(60)
        ExitState()