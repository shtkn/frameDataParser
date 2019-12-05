@Subroutine
def PreInit():
    Unknown12019('75736500000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(14000)
    WalkFSpeed(3000)
    WalkBSpeed(5200)
    DashFInitialVelocity(23000)
    DashFMaxVelocity(41000)
    Unknown12038(23000)
    Unknown12034(33)
    Unknown12036(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
    Unknown13039(1)
    Unknown2049(1)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-50000, 250000, -200000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(-50000, 350000, -200000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(-50000, 500000, -200000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(-50000, 500000, -200000, 350000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown15013(3000)
    Unknown14015(0, 300000, -100000, 250000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 300000, -100000, 250000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15013(250)
    Unknown14015(50000, 400000, -200000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 550000, -200000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 600000, -200000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_4th', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(0)
    Unknown14015(-500000, 500000, -400000, 300000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15013(200)
    Unknown15021(4000)
    Unknown14015(-36000, 300000, 150000, 450000, 250, 10)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 450000, 50000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown15013(250)
    Unknown14015(0, 300000, -100000, 250000, 1000, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(-200000, 300000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5A_2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(-200000, 350000, -250000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-250000, 300000, -320000, 122000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(150000, 400000, -500000, -250000, 500, 10)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
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
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(500)
    Unknown15013(500)
    Unknown15012(500)
    Unknown15014(500)
    Unknown15006(0)
    Unknown14015(100000, 450000, -200000, 600000, 150, 10)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(500)
    Unknown15012(500)
    Unknown15013(2500)
    Unknown15014(500)
    Unknown15006(0)
    Unknown14015(100000, 450000, -200000, 600000, 150, 10)
    Move_EndRegister()
    Move_Register('ShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(500)
    Unknown15012(500)
    Unknown15014(500)
    Unknown15006(0)
    Unknown15022('58020000e803000000000000e8030000')
    Unknown14015(100000, 450000, -200000, 600000, 100, 10)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(500)
    Unknown15012(500)
    Unknown15014(500)
    Unknown14015(600000, 1500000, -600000, 300000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(500)
    Unknown15012(500)
    Unknown15014(500)
    Unknown14015(600000, 1500000, -600000, 300000, 250, 10)
    Move_EndRegister()
    Move_Register('AirShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(500)
    Unknown15012(500)
    Unknown15014(500)
    Unknown15022('58020000e803000000000000e8030000')
    Unknown14015(600000, 1500000, -600000, 300000, 100, 10)
    Move_EndRegister()
    Move_Register('AssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(500)
    Unknown14015(0, 500000, -200000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(500)
    Unknown14015(650000, 1500000, -200000, 150000, 50, 10)
    Move_EndRegister()
    Move_Register('AssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15021(500)
    Unknown14015(0, 500000, -200000, 150000, 100, 10)
    Move_EndRegister()
    Move_Register('AirAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 350000, -500000, 80000, 150, 1)
    Move_EndRegister()
    Move_Register('AirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15010()
    Unknown15021(500)
    Unknown14015(0, 350000, -500000, 80000, 150, 1)
    Move_EndRegister()
    Move_Register('AirAssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(0, 350000, -500000, 80000, 100, 1)
    Move_EndRegister()
    Move_Register('AirAssaultA_AddAttack', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(3000)
    Unknown14015(0, 350000, -500000, 80000, 150, 1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(6000)
    Unknown15020(800, 1000, 10, 1000)
    Unknown14015(-50000, 250000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateRush', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(5000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(-450000, 450000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateRushOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(5000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(-450000, 450000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateThrow', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15021(0)
    Unknown15012(0)
    Unknown15013(0)
    Unknown14015(-50000, 200000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('UltimateThrowOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15021(0)
    Unknown15012(0)
    Unknown15013(0)
    Unknown14015(-50000, 200000, -200000, 200000, 1500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AssaultA', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'NmlAtk5B', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2B', 'FHighJump', 10000000)
    Unknown15024('NmlAtk2C', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'AN_NmlAtk5B_4th', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'AirAssaultA', 10000000)
    Unknown15024('AN_NmlAtk5B_4th', 'AssaultA', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'AirAssaultA', 10000000)
    Unknown15024('NmlAtkAIR5B', 'AirAssaultA', 10000000)
    Unknown15024('AirAssaultA', 'AirAssaultA_AddAttack', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AirAssaultA', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AirShotA', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AirShotB', 10000000)
    Unknown12018(0, 'Action_330_01')
    Unknown12018(1, 'Action_330_04')
    Unknown12018(2, 'Action_330_05')
    Unknown12018(3, 'Action_330_06')
    Unknown12018(4, 'Action_330_07')
    Unknown12018(5, 'Action_330_07')
    Unknown12018(6, 'Action_330_08')
    Unknown12018(7, 'Action_017_01')
    Unknown12018(8, 'Action_017_01')
    Unknown12018(9, 'Action_019_01')
    Unknown12018(10, 'Action_331_00')
    Unknown12018(11, 'Action_331_00')
    Unknown12018(12, 'Action_320_02')
    Unknown12018(13, 'Action_330_08')
    Unknown12018(14, 'Action_351_00')
    Unknown12018(15, 'Action_290_00')
    Unknown12018(16, 'Action_300_00')
    Unknown12018(17, 'Action_304_02')
    Unknown12018(18, 'Action_305_03')
    Unknown12018(19, 'Action_000_00')
    Unknown12018(20, 'Action_000_00')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_02')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_351_05')
    Unknown12018(29, 'Action_292_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'use000')
    Unknown7010(1, 'use001')
    Unknown7010(2, 'use002')
    Unknown7010(3, 'use003')
    Unknown7010(4, 'use004')
    Unknown7010(5, 'use005')
    Unknown7010(6, 'use006')
    Unknown7010(7, 'use007')
    Unknown7010(8, 'use008')
    Unknown7010(9, 'use009')
    Unknown7010(10, 'use010')
    Unknown7010(15, 'use011')
    Unknown7010(16, 'use012')
    Unknown7010(17, 'use013')
    Unknown7010(18, 'use014')
    Unknown7010(19, 'use015')
    Unknown7010(20, 'use016')
    Unknown7010(21, 'use017')
    Unknown7010(22, 'use018')
    Unknown7010(23, 'use019')
    Unknown7010(24, 'use020')
    Unknown7010(25, 'use021')
    Unknown7010(28, 'use022')
    Unknown7010(29, 'use023')
    Unknown7010(30, 'use024')
    Unknown7010(31, 'use025')
    Unknown7010(32, 'use026')
    Unknown7010(33, 'use027')
    Unknown7010(34, 'use028')
    Unknown7010(35, 'use029')
    Unknown7010(36, 'use030')
    Unknown7010(37, 'use031')
    Unknown7010(41, 'use032')
    Unknown7010(42, 'use033')
    Unknown7010(43, 'use034')
    Unknown7010(44, 'use035')
    Unknown7010(45, 'use036')
    Unknown7010(46, 'use037')
    Unknown7010(47, 'use038')
    Unknown7010(48, 'use039')
    Unknown7010(49, 'use040')
    Unknown7010(50, 'use041')
    Unknown7010(52, 'use042')
    Unknown7010(53, 'use043')
    Unknown7010(54, 'use100_0')
    Unknown7010(55, 'use100_1')
    Unknown7010(56, 'use100_2')
    Unknown7010(63, 'use101_0')
    Unknown7010(64, 'use101_1')
    Unknown7010(65, 'use101_2')
    Unknown7010(57, 'use102_0')
    Unknown7010(58, 'use102_1')
    Unknown7010(59, 'use102_2')
    Unknown7010(66, 'use103_0')
    Unknown7010(67, 'use103_1')
    Unknown7010(68, 'use103_2')
    Unknown7010(60, 'use104_0')
    Unknown7010(61, 'use104_1')
    Unknown7010(62, 'use104_2')
    Unknown7010(69, 'use105_0')
    Unknown7010(70, 'use105_1')
    Unknown7010(71, 'use105_2')
    Unknown7010(72, 'use150')
    Unknown7010(73, 'use151')
    Unknown7010(74, 'use152')
    Unknown7010(85, 'use153')
    Unknown7010(88, 'use155')
    Unknown7010(94, 'use400_0')
    Unknown7010(95, 'use401_0')
    Unknown7010(96, 'use161_0')
    Unknown7010(97, 'use161_1')
    Unknown7010(98, 'use163_0')
    Unknown7010(99, 'use163_1')
    Unknown7010(100, 'use164_0')
    Unknown7010(101, 'use164_1')
    Unknown7010(102, 'use166_0')
    Unknown7010(103, 'use166_1')
    Unknown7010(92, 'use162_0')
    Unknown7010(93, 'use162_1')
    Unknown7010(90, 'use167_0')
    Unknown7010(91, 'use167_1')
    Unknown7010(105, 'use165_0')
    Unknown7010(106, 'use165_1')
    Unknown7010(107, 'use168_0')
    Unknown7010(108, 'use168_1')
    Unknown7010(110, 'use169_0')
    Unknown7010(111, 'use169_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d617465527573684f44000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174655468726f7700000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174655468726f774f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if SLOT_37:
        SLOT_4 = 0

@Subroutine
def OnPreDraw():
    Unknown23030('5553455f526576436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def OnEnemyComboBreak():
    Unknown26('Shot_HitEffSub')

@State
def CmnActStand():
    label(0)
    sprite('Action_000_00', 5)	# 1-5
    sprite('Action_000_01', 5)	# 6-10
    sprite('Action_000_02', 5)	# 11-15
    sprite('Action_000_03', 5)	# 16-20
    sprite('Action_000_04', 5)	# 21-25
    sprite('Action_000_05', 5)	# 26-30
    sprite('Action_000_06', 5)	# 31-35
    sprite('Action_000_07', 5)	# 36-40
    sprite('Action_000_08', 5)	# 41-45
    sprite('Action_000_09', 5)	# 46-50
    sprite('Action_000_10', 5)	# 51-55
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    label(1)
    sprite('Action_000_00', 1)	# 56-56
    SLOT_88 = 960
    SFX_1('use000')
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 3)	# 1-3
    sprite('Action_015_01', 3)	# 4-6

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 3)	# 1-3
    sprite('Action_012_01', 3)	# 4-6
    sprite('Action_012_02', 2)	# 7-8

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 4)	# 1-4
    sprite('Action_013_01', 4)	# 5-8
    sprite('Action_013_02', 4)	# 9-12
    sprite('Action_013_03', 4)	# 13-16
    sprite('Action_013_04', 4)	# 17-20
    sprite('Action_013_05', 4)	# 21-24
    sprite('Action_013_06', 4)	# 25-28
    sprite('Action_013_07', 4)	# 29-32
    sprite('Action_013_08', 4)	# 33-36
    sprite('Action_013_09', 4)	# 37-40
    sprite('Action_013_10', 4)	# 41-44
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 3)	# 1-3
    sprite('Action_016_01', 3)	# 4-6

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 3)	# 1-3
    sprite('Action_014_01', 3)	# 4-6
    sprite('Action_014_02', 3)	# 7-9

@State
def CmnActJumpPre():
    if SLOT_16:
        _gotolabel(1)
    label(0)
    sprite('Action_036_00', 4)	# 1-4
    ExitState()
    label(1)
    sprite('Action_035_00', 4)	# 5-8

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_01', 4)	# 1-4
    sprite('Action_036_02', 32767)	# 5-32771
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_01', 4)	# 32772-32775
    sprite('Action_035_02', 32767)	# 32776-65542
    gotoLabel(1)
    label(2)
    sprite('Action_037_01', 4)	# 65543-65546
    sprite('Action_037_02', 32767)	# 65547-98313

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_03', 3)	# 1-3
    sprite('Action_036_04', 3)	# 4-6
    sprite('Action_036_05', 2)	# 7-8
    sprite('Action_036_06', 2)	# 9-10
    ExitState()
    label(1)
    sprite('Action_035_03', 4)	# 11-14
    sprite('Action_035_04', 6)	# 15-20
    sprite('Action_035_05', 4)	# 21-24
    ExitState()
    label(2)
    sprite('Action_037_03', 3)	# 25-27
    sprite('Action_037_04', 3)	# 28-30
    sprite('Action_037_05', 2)	# 31-32
    sprite('Action_037_06', 2)	# 33-34
    ExitState()

@State
def CmnActJumpDown():
    Unknown23145('CmnActAirBDash')
    if SLOT_0:
        _gotolabel(44)
    Unknown23145('NmlAtkAIR5A')
    if SLOT_0:
        _gotolabel(90)
    Unknown23145('NmlAtkAIR5B')
    if SLOT_0:
        _gotolabel(91)
    Unknown23145('NmlAtkAIR5C')
    if SLOT_0:
        _gotolabel(92)
    Unknown23145('CmnActUkemiAirB')
    if SLOT_0:
        _gotolabel(0)
    Unknown23145('CmnActUkemiAirF')
    if SLOT_0:
        _gotolabel(0)
    Unknown23145('CmnActUkemiAirN')
    if SLOT_0:
        _gotolabel(0)
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_07', 3)	# 1-3
    sprite('Action_036_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_06', 3)	# 7-9
    sprite('Action_035_07', 3)	# 10-12
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('Action_037_07', 3)	# 13-15
    sprite('Action_037_08', 3)	# 16-18
    loopRest()
    gotoLabel(2)
    label(44)
    sprite('Action_131_15', 2)	# 19-20
    sprite('Action_131_16', 3)	# 21-23
    sprite('Action_131_17', 4)	# 24-27
    sprite('Action_131_18', 4)	# 28-31
    sprite('Action_131_19', 6)	# 32-37
    sprite('Action_131_20', 4)	# 38-41
    sprite('Action_131_21', 3)	# 42-44
    label(45)
    sprite('Action_131_22', 3)	# 45-47
    sprite('Action_131_23', 3)	# 48-50
    loopRest()
    gotoLabel(45)
    label(90)
    sprite('Action_008_08', 3)	# 51-53
    sprite('Action_008_09', 3)	# 54-56
    gotoLabel(90)
    label(91)
    sprite('Action_009_11', 3)	# 57-59
    sprite('Action_009_12', 3)	# 60-62
    gotoLabel(91)
    label(92)
    sprite('Action_131_13', 2)	# 63-64
    Unknown22004(6, 1)
    sprite('Action_131_14', 2)	# 65-66
    sprite('Action_131_15', 2)	# 67-68
    sprite('Action_131_16', 3)	# 69-71
    sprite('Action_131_17', 4)	# 72-75
    sprite('Action_131_18', 4)	# 76-79
    sprite('Action_131_19', 4)	# 80-83
    sprite('Action_131_20', 4)	# 84-87
    label(93)
    sprite('Action_131_21', 3)	# 88-90
    sprite('Action_131_22', 3)	# 91-93
    loopRest()
    gotoLabel(93)

@State
def CmnActJumpLanding():
    sprite('Action_021_00', 3)	# 1-3
    sprite('Action_021_01', 3)	# 4-6
    sprite('Action_021_02', 3)	# 7-9
    sprite('Action_021_03', 3)	# 10-12
    sprite('Action_021_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('Action_131_03', 3)	# 1-3
    sprite('Action_131_04', 32767)	# 4-32770

@State
def CmnActLandingStiffEnd():
    sprite('Action_131_05', 3)	# 1-3
    sprite('Action_131_06', 3)	# 4-6

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 7)	# 1-7
    sprite('Action_010_01', 7)	# 8-14
    sprite('Action_010_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_03', 7)	# 22-28
    sprite('Action_010_04', 7)	# 29-35
    sprite('Action_010_05', 7)	# 36-42
    sprite('Action_010_06', 7)	# 43-49
    sprite('Action_010_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_08', 7)	# 57-63
    sprite('Action_010_09', 7)	# 64-70
    sprite('Action_010_10', 7)	# 71-77
    sprite('Action_010_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    label(0)
    sprite('Action_011_00', 7)	# 1-7
    sprite('Action_011_01', 7)	# 8-14
    sprite('Action_011_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_03', 7)	# 22-28
    sprite('Action_011_04', 7)	# 29-35
    sprite('Action_011_05', 7)	# 36-42
    sprite('Action_011_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_07', 7)	# 50-56
    sprite('Action_011_08', 7)	# 57-63
    sprite('Action_011_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_010_00', 3)	# 1-3
    sprite('Action_045_00', 3)	# 4-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 2)	# 10-11
    label(0)
    sprite('Action_045_03', 2)	# 12-13
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 2)	# 14-15
    sprite('Action_045_05', 2)	# 16-17
    sprite('Action_045_06', 2)	# 18-19
    sprite('Action_045_07', 2)	# 20-21
    Unknown8006(100, 1, 1)
    sprite('Action_045_08', 2)	# 22-23
    sprite('Action_045_09', 2)	# 24-25
    sprite('Action_045_10', 2)	# 26-27
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_11', 6)	# 1-6
    sprite('Action_045_12', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown22008(7)
        Unknown1084(1)
        Unknown23001(100, 0)
        Unknown23076()

        def upon_3():
            Unknown1019(92)
            if SLOT_51:
                if CheckInput(0x79):
                    SLOT_51 = 0
                    SLOT_57 = 1
                if CheckInput(0x45):
                    SLOT_51 = 0
                    SLOT_53 = 1
                    SLOT_57 = 0
    sprite('Action_046_00', 3)	# 1-3
    sprite('Action_046_01', 2)	# 4-5
    physicsXImpulse(-23000)
    physicsYImpulse(25000)
    setGravity(5000)
    SFX_1('use005')
    sprite('Action_046_02', 2)	# 6-7
    SLOT_51 = 1
    sprite('Action_046_03', 3)	# 8-10
    sprite('Action_046_04', 2)	# 11-12
    sprite('Action_046_05', 6)	# 13-18
    sprite('Action_046_06', 2)	# 19-20
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    if SLOT_53:
        _gotolabel(0)
    sprite('Action_046_07', 2)	# 21-22
    physicsXImpulse(-22000)
    physicsYImpulse(35000)
    setGravity(2500)
    Unknown22001(-1)
    Unknown22003(-1)
    if SLOT_57:
        Unknown1019(60)
        Unknown1028(2000)
        if SLOT_123:
            Unknown30070('42446173685f46726f6e74000000000000000000000000000000000000000000')
    else:
        Unknown1015(-3000)
        if SLOT_123:
            Unknown30070('42446173685f4e65757472616c00000000000000000000000000000000000000')
    sprite('Action_046_08', 2)	# 23-24
    sprite('Action_046_09', 2)	# 25-26
    sprite('Action_046_10', 2)	# 27-28
    sprite('Action_046_11', 3)	# 29-31
    sprite('Action_046_12', 4)	# 32-35
    ExitState()
    label(0)
    sprite('Action_047_00', 1)	# 36-36
    if SLOT_123:
        Unknown30070('42446173685f4c616e64696e6700000000000000000000000000000000000000')
    sprite('Action_047_01', 4)	# 37-40
    physicsXImpulse(-35000)
    physicsYImpulse(8000)
    setGravity(3000)
    sprite('Action_047_02', 4)	# 41-44
    sprite('Action_047_03', 4)	# 45-48
    Unknown8000(100, 1, 1)
    physicsXImpulse(-15000)
    Unknown1028(1500)
    sprite('Action_047_04', 5)	# 49-53
    sprite('Action_047_05', 3)	# 54-56
    Unknown1084(1)

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('Action_068_01', 3)	# 1-3
    sprite('Action_068_02', 3)	# 4-6
    sprite('Action_068_03', 3)	# 7-9
    sprite('Action_068_04', 3)	# 10-12
    sprite('Action_068_05', 3)	# 13-15
    sprite('Action_068_06', 3)	# 16-18
    sprite('Action_068_07', 3)	# 19-21
    sprite('Action_068_08', 3)	# 22-24
    loopRest()
    enterState('AirFDashRigor')

@State
def AirFDashRigor():

    def upon_IMMEDIATE():
        Unknown13014(1)
        Unknown13015(1)
        Unknown13031(1)
        Unknown13019(1)
        Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_068_09', 3)	# 1-3
    sprite('Action_068_10', 3)	# 4-6
    label(0)
    sprite('Action_068_11', 3)	# 7-9
    sprite('Action_068_12', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('Action_131_09', 3)	# 1-3
    physicsYImpulse(12000)
    GFX_0('EffAirBackDash', 100)
    sprite('Action_131_10', 3)	# 4-6
    sprite('Action_131_11', 3)	# 7-9
    sprite('Action_131_12', 2)	# 10-11
    sprite('Action_131_13', 2)	# 12-13
    sprite('Action_131_14', 2)	# 14-15

@State
def CmnActHitStandLv1():
    sprite('Action_300_00', 1)	# 1-1
    sprite('Action_300_00', 1)	# 2-2
    sprite('Action_300_01', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('Action_300_00', 1)	# 1-1
    sprite('Action_300_00', 2)	# 2-3
    sprite('Action_300_01', 3)	# 4-6

@State
def CmnActHitStandLv3():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_00', 2)	# 2-3
    sprite('Action_303_01', 2)	# 4-5
    sprite('Action_303_02', 2)	# 6-7
    sprite('Action_303_03', 2)	# 8-9

@State
def CmnActHitStandLv4():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_00', 1)	# 2-2
    sprite('Action_303_01', 3)	# 3-5
    sprite('Action_303_02', 3)	# 6-8
    sprite('Action_303_03', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_00', 3)	# 2-4
    sprite('Action_303_01', 4)	# 5-8
    sprite('Action_303_02', 4)	# 9-12
    sprite('Action_303_03', 4)	# 13-16

@State
def CmnActHitStandLowLv1():
    sprite('Action_304_02', 1)	# 1-1
    sprite('Action_304_02', 1)	# 2-2
    sprite('Action_304_03', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('Action_304_02', 1)	# 1-1
    sprite('Action_304_02', 2)	# 2-3
    sprite('Action_304_03', 3)	# 4-6

@State
def CmnActHitStandLowLv3():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_00', 1)	# 2-2
    sprite('Action_304_01', 2)	# 3-4
    sprite('Action_304_02', 2)	# 5-6
    sprite('Action_304_03', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_00', 1)	# 2-2
    sprite('Action_304_01', 3)	# 3-5
    sprite('Action_304_02', 3)	# 6-8
    sprite('Action_304_03', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_00', 3)	# 2-4
    sprite('Action_304_01', 4)	# 5-8
    sprite('Action_304_02', 4)	# 9-12
    sprite('Action_304_03', 4)	# 13-16

@State
def CmnActHitCrouchLv1():
    sprite('Action_305_02', 1)	# 1-1
    sprite('Action_305_02', 1)	# 2-2
    sprite('Action_305_03', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('Action_305_02', 1)	# 1-1
    sprite('Action_305_02', 2)	# 2-3
    sprite('Action_305_03', 3)	# 4-6

@State
def CmnActHitCrouchLv3():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_00', 2)	# 2-3
    sprite('Action_305_01', 2)	# 4-5
    sprite('Action_305_02', 2)	# 6-7
    sprite('Action_305_03', 2)	# 8-9

@State
def CmnActHitCrouchLv4():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_00', 1)	# 2-2
    sprite('Action_305_01', 3)	# 3-5
    sprite('Action_305_02', 3)	# 6-8
    sprite('Action_305_03', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_00', 3)	# 2-4
    sprite('Action_305_01', 4)	# 5-8
    sprite('Action_305_02', 4)	# 9-12
    sprite('Action_305_03', 4)	# 13-16

@State
def CmnActBDownUpper():
    sprite('Action_320_00', 4)	# 1-4
    label(0)
    sprite('Action_320_01', 4)	# 5-8
    sprite('Action_320_01', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('Action_330_04', 3)	# 1-3
    sprite('Action_330_05', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('Action_330_06', 2)	# 1-2
    sprite('Action_330_07', 2)	# 3-4
    label(0)
    sprite('Action_330_08', 4)	# 5-8
    sprite('Action_330_09', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('Action_351_00', 2)	# 1-2
    sprite('Action_351_01', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('Action_350_01', 3)	# 1-3
    sprite('Action_350_02', 3)	# 4-6
    sprite('Action_350_03', 3)	# 7-9
    sprite('Action_350_04', 3)	# 10-12
    sprite('Action_350_05', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('Action_354_04', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('Action_293_11', 4)	# 1-4
    sprite('Action_293_12', 4)	# 5-8
    sprite('Action_293_13', 3)	# 9-11
    sprite('Action_293_14', 3)	# 12-14
    sprite('Action_293_15', 4)	# 15-18
    sprite('Action_293_16', 4)	# 19-22
    sprite('Action_293_17', 4)	# 23-26

@State
def CmnActFDownUpper():
    sprite('Action_326_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('Action_326_02', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('Action_326_03', 4)	# 1-4
    sprite('Action_326_04', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('Action_354_00', 3)	# 1-3

@State
def CmnActFDownBound():
    sprite('Action_354_01', 4)	# 1-4
    sprite('Action_354_02', 4)	# 5-8
    sprite('Action_354_03', 4)	# 9-12

@State
def CmnActFDownLoop():
    sprite('Action_292_00', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('Action_294_11', 3)	# 1-3
    sprite('Action_294_12', 3)	# 4-6
    sprite('Action_294_13', 3)	# 7-9
    sprite('Action_294_14', 3)	# 10-12
    sprite('Action_294_15', 3)	# 13-15
    sprite('Action_294_16', 3)	# 16-18
    sprite('Action_294_17', 2)	# 19-20

@State
def CmnActVDownUpper():
    sprite('Action_330_00', 3)	# 1-3
    label(0)
    sprite('Action_330_01', 3)	# 4-6
    sprite('Action_330_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('Action_330_03', 2)	# 1-2
    sprite('Action_330_04', 2)	# 3-4
    sprite('Action_330_05', 2)	# 5-6

@State
def CmnActVDownDown():
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_06', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 4)	# 7-10
    sprite('Action_330_09', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('Action_351_00', 3)	# 1-3
    sprite('Action_351_01', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('Action_331_00', 2)	# 1-2
    label(0)
    sprite('Action_331_02', 3)	# 3-5
    sprite('Action_331_03', 3)	# 6-8
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    sprite('Action_333_06', 2)	# 13-14
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
    sprite('Action_327_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('Action_340_00', 2)	# 1-2
    sprite('Action_340_01', 2)	# 3-4
    sprite('Action_340_02', 2)	# 5-6

@State
def CmnActWallBoundDown():
    sprite('Action_340_03', 3)	# 1-3
    sprite('Action_340_04', 3)	# 4-6
    label(0)
    sprite('Action_340_05', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('Action_327_00', 14)	# 1-14

@State
def CmnActStaggerDown():
    sprite('Action_327_02', 5)	# 1-5
    sprite('Action_327_03', 5)	# 6-10
    sprite('Action_327_04', 4)	# 11-14
    sprite('Action_328_00', 4)	# 15-18
    sprite('Action_328_01', 4)	# 19-22

@State
def CmnActUkemiStagger():
    sprite('Action_327_00', 8)	# 1-8

@State
def CmnActUkemiAirF():
    sprite('Action_032_00', 2)	# 1-2
    sprite('Action_032_01', 2)	# 3-4
    sprite('Action_032_02', 2)	# 5-6
    sprite('Action_032_03', 1)	# 7-7
    sprite('Action_032_04', 1)	# 8-8
    sprite('Action_032_05', 1)	# 9-9

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 4)	# 1-4
    sprite('Action_032_01', 4)	# 5-8
    sprite('Action_032_02', 4)	# 9-12
    sprite('Action_032_03', 4)	# 13-16
    sprite('Action_032_04', 4)	# 17-20
    sprite('Action_032_05', 3)	# 21-23

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 4)	# 1-4
    sprite('Action_032_01', 4)	# 5-8
    sprite('Action_032_02', 4)	# 9-12
    sprite('Action_032_03', 4)	# 13-16
    sprite('Action_032_04', 4)	# 17-20
    sprite('Action_032_05', 3)	# 21-23

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_04', 2)	# 13-14
    sprite('Action_041_05', 2)	# 15-16

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_04', 2)	# 13-14
    sprite('Action_041_05', 2)	# 15-16

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 3)	# 1-3
    sprite('Action_041_01', 3)	# 4-6
    sprite('Action_041_02', 4)	# 7-10
    sprite('Action_041_03', 4)	# 11-14
    label(0)
    sprite('Action_041_04', 3)	# 15-17
    sprite('Action_041_05', 3)	# 18-20
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_06', 7)	# 1-7
    sprite('Action_041_07', 4)	# 8-11
    sprite('Action_041_08', 4)	# 12-15

@State
def CmnActMidGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('Action_017_00', 3)	# 1-3

@State
def CmnActHighGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_00', 3)	# 1-3
    sprite('Action_018_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('Action_018_02', 3)	# 1-3
    sprite('Action_018_03', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('Action_018_01', 3)	# 1-3
    sprite('Action_018_02', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_06', 3)	# 1-3
    sprite('Action_018_07', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('Action_019_00', 3)	# 1-3
    sprite('Action_019_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('Action_019_02', 3)	# 1-3
    sprite('Action_019_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('Action_019_02', 3)	# 1-3
    sprite('Action_019_03', 3)	# 4-6

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('Action_017_00', 2)	# 1-2
    sprite('Action_017_01', 2)	# 3-4
    sprite('Action_017_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_017_06', 6)	# 6-11
    sprite('Action_017_07', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('Action_018_00', 2)	# 1-2
    sprite('Action_018_01', 2)	# 3-4
    sprite('Action_018_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_018_01', 6)	# 6-11
    sprite('Action_018_00', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('Action_019_00', 2)	# 1-2
    sprite('Action_019_01', 2)	# 3-4
    sprite('Action_019_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_019_01', 6)	# 6-11
    sprite('Action_019_00', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('Action_036_02', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_002_00', 2)	# 1-2
    sprite('Action_002_01', 3)	# 3-5
    sprite('Action_002_02', 2)	# 6-7
    sprite('Action_002_03', 6)	# 8-13	 **attackbox here**
    GFX_0('EffNmlAtk5A_2nd', 100)
    sprite('Action_002_04', 6)	# 14-19
    sprite('Action_002_05', 4)	# 20-23
    sprite('Action_002_06', 4)	# 24-27

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1
    sprite('Action_019_03', 3)	# 2-4
    sprite('Action_019_00', 3)	# 5-7

@State
def CmnActLandSpin():
    sprite('hb071_00', 4)	# 1-4
    sprite('hb071_01', 4)	# 5-8
    label(0)
    sprite('hb071_02', 2)	# 9-10
    sprite('hb071_03', 2)	# 11-12
    sprite('hb071_04', 2)	# 13-14
    sprite('hb071_05', 2)	# 15-16
    sprite('hb071_06', 2)	# 17-18
    sprite('hb071_07', 2)	# 19-20
    sprite('hb071_08', 2)	# 21-22
    sprite('hb071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('hb071_10', 6)	# 1-6
    sprite('hb071_11', 5)	# 7-11
    sprite('hb071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('Action_351_00', 1)	# 1-1
    label(0)
    sprite('Action_351_01', 3)	# 2-4
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('Action_351_02', 3)	# 1-3
    sprite('Action_351_03', 2)	# 4-5
    sprite('Action_351_04', 2)	# 6-7
    sprite('Action_351_05', 2)	# 8-9

@State
def CmnActAomukeSlideKeep():
    sprite('Action_351_04', 1)	# 1-1
    label(0)
    sprite('Action_351_04', 3)	# 2-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('Action_351_02', 3)	# 1-3
    sprite('Action_351_03', 2)	# 4-5
    sprite('Action_351_04', 2)	# 6-7
    sprite('Action_351_05', 2)	# 8-9

@State
def CmnActBurstBegin():
    sprite('Action_262_00', 4)	# 1-4
    label(0)
    sprite('Action_262_01', 5)	# 5-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('Action_262_05', 3)	# 1-3
    sprite('Action_262_06', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    label(0)
    sprite('Action_262_07', 4)	# 1-4
    sprite('Action_262_08', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('Action_262_05', 6)	# 1-6
    sprite('Action_262_06', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('Action_262_07', 6)	# 1-6
    sprite('Action_262_08', 6)	# 7-12
    label(0)
    sprite('Action_262_09', 3)	# 13-15
    sprite('Action_262_10', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('Action_262_05', 6)	# 1-6
    sprite('Action_262_06', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('Action_262_07', 6)	# 1-6
    sprite('Action_262_08', 6)	# 7-12
    label(0)
    sprite('Action_262_09', 3)	# 13-15
    sprite('Action_262_10', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4
    label(0)
    sprite('Action_262_01', 5)	# 5-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('Action_262_05', 3)	# 1-3
    sprite('Action_262_06', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4
    label(0)
    sprite('Action_262_01', 5)	# 5-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('Action_262_07', 3)	# 1-3
    sprite('Action_262_08', 3)	# 4-6
    label(0)
    sprite('Action_262_09', 3)	# 7-9
    sprite('Action_262_10', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@Subroutine
def ChainRoot():
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    HitJumpCancel(1)

@Subroutine
def NormalAtkDeriveInputBegin():
    Unknown14070('NmlAtk5A')
    Unknown14070('NmlAtk2A')
    Unknown14070('NmlAtk5B')
    Unknown14070('NmlAtk2B')
    Unknown14070('NmlAtk2C')
    Unknown14070('CmnActCrushAttack')

@Subroutine
def NormalAtkDeriveTimingBegin():
    Unknown14072('NmlAtk5A')
    Unknown14072('NmlAtk2A')
    Unknown14072('NmlAtk5B')
    Unknown14072('NmlAtk2B')
    Unknown14072('NmlAtk2C')
    Unknown14072('CmnActCrushAttack')

@Subroutine
def NormalAtkDeriveClear():
    Unknown14074('NmlAtk5A')
    Unknown14074('NmlAtk2A')
    Unknown14074('NmlAtk5B')
    Unknown14074('NmlAtk2B')
    Unknown14074('NmlAtk2C')
    Unknown14074('CmnActCrushAttack')

@Subroutine
def SkillDeriveInputBegin():
    Unknown14070('CmnActInvincibleAttack')
    Unknown14070('AssaultA')
    Unknown14070('AssaultB')
    Unknown14070('AssaultEx')
    Unknown14070('ShotA')
    Unknown14070('ShotB')
    Unknown14070('ShotEx')
    Unknown14070('AirShotA')
    Unknown14070('AirShotB')
    Unknown14070('AirShotEx')
    Unknown14070('AirAssaultA')
    Unknown14070('AirAssaultB')
    Unknown14070('AirAssaultEx')
    Unknown14070('UltimateRush')
    Unknown14070('UltimateRushOD')
    Unknown14070('UltimateThrow')
    Unknown14070('UltimateThrowOD')
    Unknown14070('AstralHeat')

@Subroutine
def SkillDeriveTimingBegin():
    Unknown14072('CmnActInvincibleAttack')
    Unknown14072('AssaultA')
    Unknown14072('AssaultB')
    Unknown14072('AssaultEx')
    Unknown14072('ShotA')
    Unknown14072('ShotB')
    Unknown14072('ShotEx')
    Unknown14072('AirShotA')
    Unknown14072('AirShotB')
    Unknown14072('AirShotEx')
    Unknown14072('AirAssaultA')
    Unknown14072('AirAssaultB')
    Unknown14072('AirAssaultEx')
    Unknown14072('UltimateRush')
    Unknown14072('UltimateRushOD')
    Unknown14072('UltimateThrow')
    Unknown14072('UltimateThrowOD')
    Unknown14072('AstralHeat')

@Subroutine
def SkillDeriveClear():
    Unknown14074('CmnActInvincibleAttack')
    Unknown14074('AssaultA')
    Unknown14074('AssaultB')
    Unknown14074('AssaultEx')
    Unknown14074('ShotA')
    Unknown14074('ShotB')
    Unknown14074('ShotEx')
    Unknown14074('AirShotA')
    Unknown14074('AirShotB')
    Unknown14074('AirShotEx')
    Unknown14074('AirAssaultA')
    Unknown14074('AirAssaultB')
    Unknown14074('AirAssaultEx')
    Unknown14074('UltimateRush')
    Unknown14074('UltimateRushOD')
    Unknown14074('UltimateThrow')
    Unknown14074('UltimateThrowOD')
    Unknown14074('AstralHeat')

@Subroutine
def Confuse():
    Hitstop(4)
    Unknown9016(1)
    Unknown11057(750)
    Unknown9266(16)
    Unknown11056(2)

    def upon_77():
        Unknown2038(1)
        GFX_0('EffConfuse_AtkMatome', 104)
        Unknown23029(1, 100, 0)

    def upon_81():
        Unknown2038(1)
        GFX_0('EffConfuse_AtkMatome', 104)
        Unknown23029(1, 101, 0)

    def upon_78():
        SLOT_51 = 1

    def upon_STATE_END():
        Unknown1051(0)
        Unknown3004(0)
        Unknown3001(255)
        Unknown2035(0)
        if SLOT_59:
            Unknown1019(16)
            YAccel(33)
            SLOT_59 = 0

@Subroutine
def SethAtk():
    Hitstop(7)
    Unknown9016(1)
    Unknown9266(16)

    def upon_77():
        Unknown1019(50)
        GFX_0('EffConfuse_AtkEff', 100)
        Unknown36(1)
        Unknown1086(22)
        Unknown1007(200000)
        Unknown35()

    def upon_81():
        GFX_0('EffConfuse_AtkEff', 100)
        Unknown36(1)
        Unknown1086(23)
        Unknown1007(200000)
        Unknown35()

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(15000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_001_00', 5)	# 1-5
    sprite('Action_001_01', 2)	# 6-7	 **attackbox here**
    Unknown7009(3)
    GFX_0('EffNmlAtk5A', 100)
    SFX_3('SE041')
    sprite('Action_001_02', 3)	# 8-10
    Recovery()
    Unknown2063()
    sprite('Action_001_03', 6)	# 11-16
    sprite('Action_001_04', 6)	# 17-22

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(800)
        Unknown11092(1)
        AirPushbackX(7500)
        AirPushbackY(5500)
        PushbackX(12000)
        Hitstop(5)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_402_00', 2)	# 1-2
    Unknown1047(5000)
    sprite('Action_402_01', 2)	# 3-4
    sprite('Action_402_02', 2)	# 5-6	 **attackbox here**
    SFX_3('SE042')
    Unknown7009(1)
    sprite('Action_402_03', 1)	# 7-7
    sprite('Action_402_04', 1)	# 8-8
    sprite('Action_402_05', 1)	# 9-9
    sprite('Action_402_06', 1)	# 10-10
    SFX_3('SE042')
    sprite('Action_402_07', 4)	# 11-14	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
    Damage(1000)
    Hitstop(10)
    AirPushbackY(12500)
    Unknown9016(1)
    sprite('Action_402_08', 6)	# 15-20
    HitOrBlockCancel('AN_NmlAtk5A_3rd')
    Recovery()
    Unknown2063()
    sprite('Action_402_09', 6)	# 21-26
    sprite('Action_402_10', 4)	# 27-30

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(11000)
        AirPushbackY(8000)
        Unknown9016(1)
        HitOrBlockCancel('AN_NmlAtk5A_4th')
        callSubroutine('ChainRoot')
    sprite('Action_003_00', 3)	# 1-3
    sprite('Action_003_01', 4)	# 4-7
    teleportRelativeX(50000)
    physicsXImpulse(30000)
    Unknown1028(-5000)
    sprite('Action_003_02', 2)	# 8-9
    teleportRelativeX(30000)
    SFX_3('SE043')
    Unknown7009(5)
    sprite('Action_003_03', 4)	# 10-13	 **attackbox here**
    GFX_0('EffNmlAtk5A_3rd', 100)
    Unknown1084(1)
    sprite('Action_003_04', 7)	# 14-20
    Recovery()
    Unknown2063()
    sprite('Action_003_05', 5)	# 21-25
    sprite('Action_003_06', 5)	# 26-30

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Confuse')
        AttackLevel_(4)
        Damage(1000)
        Unknown11092(1)
        AirPushbackX(-7500)
        AirPushbackY(12500)
        PushbackX(19800)
        Unknown11028(26)
        Unknown11001(0, 10, 10)
        Unknown11099(1)
        Unknown11057(750)
        Unknown9154(60)
        AirUntechableTime(60)
        JumpCancel_(0)
    sprite('Action_364_00', 2)	# 1-2
    sprite('Action_364_01', 2)	# 3-4
    sprite('Action_364_02', 2)	# 5-6	 **attackbox here**
    GFX_0('EffNmlAtk5B_3rd_Zanzo2', 100)
    physicsXImpulse(13000)
    physicsYImpulse(37000)
    setGravity(1900)
    Unknown3004(-65)
    sprite('Action_364_03', 2)	# 7-8	 **attackbox here**
    GFX_0('EffNmlAtk5A_4th_AirShadow', 100)
    sprite('Action_364_04', 2)	# 9-10	 **attackbox here**
    Unknown1019(200)
    sprite('Action_364_05', 2)	# 11-12	 **attackbox here**
    Unknown3001(0)
    Unknown3004(0)
    Unknown2035(1)
    Unknown7007('7573653230395f300000000000000000640000007573653230395f310000000000000000640000007573653231305f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_364_07ex01', 32767)	# 13-32779	 **attackbox here**
    Unknown2017(0)
    physicsXImpulse(100000)
    physicsYImpulse(-148000)
    SLOT_59 = 1
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_367_01', 1)	# 32780-32780
    Unknown1019(30)
    sprite('Action_367_01', 5)	# 32781-32785
    Unknown1084(1)
    Unknown1045(25000)
    Unknown2017(1)
    Unknown2015(50)
    Unknown3004(60)
    SFX_3('SE050_SlideDash')
    SLOT_59 = 0
    sprite('Action_367_02', 2)	# 32786-32787
    Unknown2006()
    Unknown2005()
    Unknown2015(-1)
    Unknown2035(0)
    sprite('Action_367_03', 3)	# 32788-32790
    sprite('Action_367_04', 3)	# 32791-32793
    sprite('Action_367_05', 4)	# 32794-32797
    sprite('Action_367_06', 3)	# 32798-32800
    sprite('Action_367_07', 2)	# 32801-32802
    GFX_0('EffNmlAtk5A_4th_LandZanzo', 100)
    GFX_0('EffNmlAtk5A_4th_AtkSub', 100)
    physicsXImpulse(-80000)
    SLOT_59 = 1
    Unknown2017(0)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown2005()
    teleportRelativeX(455000)
    Unknown35()
    sprite('Action_367_07ex01', 2)	# 32803-32804	 **attackbox here**
    SFX_3('SE242')
    Unknown3001(255)
    Unknown3004(0)
    RefreshMultihit()
    Damage(1300)
    Hitstop(5)
    Unknown11001(0, -4, -4)
    Unknown9130(16)
    Unknown9142(100)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(13)
    PushbackX(0)
    Unknown11028(18)
    clearUponHandler(77)
    clearUponHandler(81)
    callSubroutine('SethAtk')
    sprite('Action_367_12', 2)	# 32805-32806	 **attackbox here**
    sprite('Action_367_10', 2)	# 32807-32808
    Recovery()
    sprite('Action_367_11', 2)	# 32809-32810
    Unknown1019(70)
    SLOT_59 = 0
    sprite('Action_367_10', 2)	# 32811-32812
    sprite('Action_367_13', 4)	# 32813-32816
    Unknown1019(50)
    sprite('Action_367_14', 7)	# 32817-32823
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('Action_367_15', 9)	# 32824-32832
    Unknown1084(1)
    Unknown1045(-7000)
    sprite('Action_367_16', 7)	# 32833-32839
    sprite('Action_367_17', 6)	# 32840-32845

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(28000)
        AirPushbackY(15000)
        PushbackX(46000)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')

        def upon_77():
            Unknown1019(70)
            Unknown1034(70)

        def upon_80():
            Unknown2015(210)

        def upon_STATE_END():
            Unknown2015(-1)
    sprite('Action_403_00', 4)	# 1-4
    sprite('Action_403_01', 3)	# 5-7
    Unknown8007(100, 1, 1)
    Unknown7007('7573653130385f320000000000000000640000007573653130345f310000000000000000640000007573653130355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_403_02', 2)	# 8-9
    physicsXImpulse(8000)
    Unknown1051(50)
    SFX_3('SE043')
    Unknown7009(3)
    sprite('Action_127_02', 2)	# 10-11	 **attackbox here**
    GFX_0('EffNmlAtk5B', 100)
    physicsXImpulse(58000)
    Unknown1028(-4000)
    sprite('Action_403_04ex01', 2)	# 12-13	 **attackbox here**
    sprite('Action_127_02', 1)	# 14-14	 **attackbox here**
    sprite('Action_127_02', 1)	# 15-15	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_403_03', 2)	# 16-17	 **attackbox here**
    StartMultihit()
    sprite('Action_403_04', 2)	# 18-19
    sprite('Action_403_03', 2)	# 20-21	 **attackbox here**
    StartMultihit()
    sprite('Action_403_05', 5)	# 22-26
    Unknown1084(1)
    Unknown1045(8000)
    sprite('Action_403_06', 5)	# 27-31
    sprite('Action_403_07', 5)	# 32-36

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Confuse')
        AttackLevel_(3)
        Damage(1700)
        AirPushbackX(3000)
        AirPushbackY(15500)
        Unknown9154(20)
        AirUntechableTime(20)
        PushbackX(15500)
        Unknown11028(17)
        Unknown11001(5, 5, 5)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(11)
        Unknown30055('90d003003c0000003c000000')
        Unknown30056('a08601003c0000003c000000')
        JumpCancel_(0)

        def upon_12():
            SLOT_53 = 1
    sprite('Action_362_00', 2)	# 1-2
    sprite('Action_362_01', 1)	# 3-3
    sprite('Action_362_01', 2)	# 4-5
    GFX_0('EffNmlAtk5B_2nd_Zanzo2', 100)
    Unknown7007('7573653230375f300000000000000000640000007573653230385f320000000000000000640000007573653230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_362_02', 2)	# 6-7	 **attackbox here**
    Unknown8007(100, 1, 1)
    Unknown2035(1)
    SFX_3('SE028_RunDash')
    physicsXImpulse(140000)
    Unknown3004(-40)
    Unknown2016(250)
    SLOT_59 = 1
    sprite('Action_362_02', 1)	# 8-8	 **attackbox here**

    def upon_3():
        if (SLOT_19 <= 170000):
            Unknown1019(5)
    sprite('Action_362_03', 2)	# 9-10	 **attackbox here**
    GFX_0('EffNmlAtk5B_2nd_LandShadow', 100)
    sprite('Action_365_00', 1)	# 11-11
    Unknown3004(15)
    sprite('Action_365_00ex01', 2)	# 12-13	 **attackbox here**
    callSubroutine('NormalAtkDeriveInputBegin')
    callSubroutine('SkillDeriveInputBegin')
    Unknown14070('AN_NmlAtk5B_3rd')
    clearUponHandler(3)
    Unknown1084(1)
    Unknown1045(-36000)
    Unknown2016(-1)
    SFX_3('SE050_SlideDash')
    SLOT_59 = 0
    sprite('Action_365_00', 2)	# 14-15
    Recovery()
    sprite('Action_365_01', 3)	# 16-18
    sprite('Action_365_02', 3)	# 19-21
    Unknown2035(0)
    Unknown3001(255)
    if SLOT_2:
        callSubroutine('NormalAtkDeriveTimingBegin')
        callSubroutine('SkillDeriveTimingBegin')
        Unknown14072('AN_NmlAtk5B_3rd')
    if SLOT_53:
        Unknown13008(1)
    sprite('Action_365_03', 4)	# 22-25
    Unknown2063()
    sprite('Action_365_04', 4)	# 26-29
    callSubroutine('NormalAtkDeriveClear')
    Unknown14074('AN_NmlAtk5B_3rd')
    sprite('Action_365_05', 5)	# 30-34
    sprite('Action_365_06', 5)	# 35-39
    sprite('Action_365_06', 2)	# 40-41

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('Confuse')
        AttackLevel_(3)
        Damage(1700)
        PushbackX(0)
        AirPushbackX(2500)
        AirPushbackY(18500)
        PushbackX(15500)
        AirUntechableTime(33)
        Unknown11028(17)
        Unknown11001(5, 5, 5)
        Unknown30055('b0ad01006400000064000000')
        Unknown30056('20bf02006400000064000000')
        Unknown11056(2)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        JumpCancel_(0)
    sprite('Action_363_00', 2)	# 1-2
    sprite('Action_363_01', 4)	# 3-6
    GFX_0('EffNmlAtk5B_3rd_Zanzo2', 100)
    sprite('Action_363_02', 2)	# 7-8
    Unknown8001(0, 100)
    SFX_3('SE028_RunDash')
    physicsXImpulse(24000)
    physicsYImpulse(6000)
    Unknown3004(-40)
    Unknown2006()
    Unknown2035(1)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_363_03', 2)	# 9-10
    Unknown7007('7573653230375f310000000000000000640000007573653230385f310000000000000000640000007573653230395f320000000000000000640000000000000000000000000000000000000000000000')
    SLOT_59 = 1
    sprite('Action_366_00ex01', 3)	# 11-13	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(126000)
    physicsYImpulse(66000)
    SFX_3('SE050_SlideDash')
    Unknown14070('AN_NmlAtk5B_4th')
    callSubroutine('SkillDeriveInputBegin')
    sprite('Action_366_00', 1)	# 14-14
    Unknown2005()
    Unknown23072()
    Unknown1019(-120)
    Unknown3004(45)
    sprite('Action_366_00', 1)	# 15-15
    sprite('Action_366_01', 3)	# 16-18
    Unknown2035(0)
    Unknown2017(1)
    Unknown1084(1)
    Unknown1045(10000)
    physicsYImpulse(10000)
    setGravity(1800)
    SLOT_59 = 0
    sprite('Action_366_02', 3)	# 19-21
    Recovery()
    Unknown3001(255)
    if SLOT_2:
        callSubroutine('SkillDeriveTimingBegin')
    Unknown22004(6, 1)
    sprite('Action_366_02', 3)	# 22-24
    sprite('Action_366_03', 4)	# 25-28
    if SLOT_2:
        Unknown14072('AN_NmlAtk5B_4th')
    sprite('Action_366_04', 4)	# 29-32
    Unknown2063()
    sprite('Action_366_05', 3)	# 33-35
    Unknown14074('AN_NmlAtk5B_4th')
    sprite('Action_366_06', 3)	# 36-38
    Unknown2006()
    sprite('Action_366_07', 3)	# 39-41
    label(0)
    sprite('Action_366_06', 3)	# 42-44
    sprite('Action_366_07', 3)	# 45-47
    gotoLabel(0)

@State
def AN_NmlAtk5B_4th():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(100)
        AttackP2(75)
        AirUntechableTime(19)
        AirPushbackX(5500)
        AirPushbackY(21000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOverhead(0)
        clearUponHandler(2)
        Unknown2006()
        HitJumpCancel(1)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_220_00', 3)	# 1-3
    Unknown1084(1)
    physicsYImpulse(-2560)
    sprite('Action_220_01', 32767)	# 4-32770
    physicsYImpulse(-280000)
    GFX_0('EffNmlAtk5B_4th_AirZanzo', 100)
    SFX_3('SE038')
    sendToLabelUpon(2, 0)
    SLOT_51 = SLOT_38
    label(0)
    sprite('Action_220_02', 2)	# 32771-32772
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_220_03', 2)	# 32773-32774
    sprite('Action_222_00', 2)	# 32775-32776
    GFX_0('EffNmlAtk5B_4th_LandZanzo1', 100)
    GFX_0('EffNmlAtk5B_4th_LandZanzo2', 100)
    sprite('Action_222_00', 3)	# 32777-32779
    Unknown3001(0)
    physicsXImpulse(150000)
    Unknown2035(1)
    SFX_3('SE050')
    sprite('Action_222_00', 2)	# 32780-32781

    def upon_3():
        if (SLOT_19 <= 150000):
            Unknown1019(35)
            if (SLOT_25 <= 110000):
                Unknown1084(1)
                teleportRelativeX(-55000)
    sprite('Action_222_06', 2)	# 32782-32783
    clearUponHandler(3)
    Unknown2006()
    Unknown2016(250)
    Unknown3004(60)
    physicsXImpulse(15000)
    Unknown1028(1500)
    if (not (SLOT_38 == SLOT_51)):
        Unknown7007('7573653130395f320000000000000000640000007573653130345f300000000000000000640000007573653231355f300000000000000000640000000000000000000000000000000000000000000000')
    else:
        Unknown7007('7573653130395f310000000000000000640000007573653130395f310000000000000000640000007573653130345f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_222_06', 2)	# 32784-32785
    Unknown2035(0)
    sprite('Action_222_07', 4)	# 32786-32789	 **attackbox here**
    GFX_0('EffNmlAtk5B_3rd_Kick', 100)
    SFX_3('SE043')
    Unknown1084(1)
    Unknown2016(-1)
    sprite('Action_222_08', 6)	# 32790-32795
    Recovery()
    sprite('Action_222_09', 4)	# 32796-32799
    sprite('Action_222_10', 4)	# 32800-32803
    sprite('Action_222_11', 4)	# 32804-32807
    sprite('Action_222_12', 4)	# 32808-32811
    sprite('Action_222_13', 4)	# 32812-32815
    sprite('Action_222_14', 3)	# 32816-32818

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    SFX_3('SE041')
    Unknown7009(0)
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_004_03', 5)	# 9-13
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 14-18
    sprite('Action_004_05', 4)	# 19-22

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    SFX_3('SE041')
    Unknown7009(0)
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_004_03', 5)	# 9-13
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 14-18
    sprite('Action_004_05', 4)	# 19-22

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirUntechableTime(20)
        Unknown9016(1)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('ChainRoot')
    sprite('Action_133_00', 4)	# 1-4
    teleportRelativeX(40000)
    sprite('Action_133_01', 1)	# 5-5
    sprite('Action_133_01', 2)	# 6-7
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_133_02', 1)	# 8-8
    Unknown7007('7573653130365f310000000000000000640000007573653130365f3200000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_133_02', 1)	# 9-9
    teleportRelativeX(40000)
    sprite('Action_133_03', 3)	# 10-12	 **attackbox here**
    teleportRelativeX(40000)
    GFX_0('EffNmlAtk2B', 100)
    SFX_3('SE043')
    sprite('Action_133_04', 5)	# 13-17
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('Action_133_05', 5)	# 18-22
    sprite('Action_133_06', 5)	# 23-27
    sprite('Action_133_07', 4)	# 28-31
    sprite('Action_133_08', 4)	# 32-35
    sprite('Action_133_09', 4)	# 36-39

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1000)
        Hitstop(5)
        AttackP1(90)
        AttackP2(75)
        Unknown11092(1)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(10000)
        AirUntechableTime(23)
        callSubroutine('ChainRoot')
        Unknown14085('CmnActCrushAttack')
    sprite('Action_006_00', 2)	# 1-2
    sprite('Action_006_01', 2)	# 3-4
    sprite('Action_006_02', 2)	# 5-6
    sprite('Action_006_03', 2)	# 7-8
    SFX_3('SE043')
    Unknown7007('7573653130375f300000000000000000640000007573653131305f3000000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_006_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_006_05', 2)	# 11-12
    sprite('Action_006_06', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    sprite('Action_006_07', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('Action_006_08', 3)	# 18-20
    sprite('Action_006_09', 3)	# 21-23
    sprite('Action_006_10', 4)	# 24-27
    sprite('Action_006_11', 4)	# 28-31
    sprite('Action_006_12', 4)	# 32-35

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AirPushbackY(24000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_008_00', 2)	# 1-2
    sprite('Action_008_01', 2)	# 3-4
    sprite('Action_008_02', 2)	# 5-6
    sprite('Action_008_03', 2)	# 7-8
    SFX_3('SE042')
    Unknown7007('7573653130325f300000000000000000640000007573653130325f310000000000000000640000007573653130365f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_008_04ex01', 2)	# 9-10	 **attackbox here**
    GFX_0('EffNmlAtkAIR5A', 100)
    sprite('Action_008_04', 1)	# 11-11	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_008_05', 9)	# 12-20
    sprite('Action_008_06', 7)	# 21-27
    sprite('Action_008_07', 6)	# 28-33

@State
def AN_NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(24000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_007_00', 6)	# 1-6
    sprite('Action_007_01ex01', 4)	# 7-10	 **attackbox here**
    SFX_3('SE041')
    sprite('Action_007_02', 2)	# 11-12
    Recovery()
    Unknown2063()
    sprite('Action_007_03', 5)	# 13-17
    sprite('Action_007_04', 5)	# 18-22

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_009_00', 2)	# 1-2
    sprite('Action_009_01', 3)	# 3-5
    sprite('Action_009_02', 2)	# 6-7
    sprite('Action_009_03', 2)	# 8-9
    sprite('Action_009_04', 1)	# 10-10
    sprite('Action_009_05', 1)	# 11-11
    SFX_3('SE043')
    Unknown7009(2)
    sprite('Action_009_06', 3)	# 12-14	 **attackbox here**
    GFX_0('EffNmlAtkAIR5B', 100)
    sprite('Action_009_07', 5)	# 15-19
    Recovery()
    Unknown2063()
    sprite('Action_009_08', 7)	# 20-26
    sprite('Action_009_09', 5)	# 27-31
    sprite('Action_009_10', 5)	# 32-36

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1700)
        AirPushbackX(17500)
        AirPushbackY(24000)
        YImpluseBeforeWallbounce(2000)
        Hitstop(12)
        AirUntechableTime(32)
        HitOverhead(0)
        JumpCancel_(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            clearUponHandler(2)
            Unknown22004(6, 1)
            sendToLabel(0)
    sprite('Action_046_13', 3)	# 1-3
    sprite('Action_046_14', 3)	# 4-6
    Unknown1084(1)
    sprite('Action_131_00', 5)	# 7-11
    callSubroutine('SkillDeriveInputBegin')
    Unknown7007('7573653130345f300000000000000000640000007573653330355f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_131_00', 2)	# 12-13
    SFX_3('SE043')
    sprite('Action_131_01ex01', 5)	# 14-18	 **attackbox here**
    GFX_0('EffNmlAtkAIR5C_Shadow', 100)
    physicsXImpulse(30000)
    physicsYImpulse(-45000)
    setGravity(500)
    sprite('Action_131_02', 32767)	# 19-32785	 **attackbox here**
    label(0)
    sprite('Action_131_08', 1)	# 32786-32786
    Recovery()
    Unknown1084(1)
    if CheckInput(0x5f):
        SLOT_55 = 1
        SLOT_57 = 0
    if CheckInput(0x79):
        SLOT_55 = 0
        SLOT_57 = 1
    sprite('Action_131_09', 2)	# 32787-32788
    Unknown28(2, 'CmnActJumpLanding')
    physicsXImpulse(-2560)
    physicsYImpulse(41000)
    setGravity(3000)
    if SLOT_55:
        Unknown1028(-500)
    if SLOT_57:
        Unknown1028(1100)
    sprite('Action_131_09', 2)	# 32789-32790
    if SLOT_2:
        callSubroutine('SkillDeriveTimingBegin')
    sprite('Action_131_10', 3)	# 32791-32793
    sprite('Action_131_11', 3)	# 32794-32796
    sprite('Action_131_12', 3)	# 32797-32799
    sprite('Action_131_13', 3)	# 32800-32802
    loopRest()
    ExitState()
    label(1)
    sprite('Action_131_03', 3)	# 32803-32805
    Recovery()
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_131_04', 3)	# 32806-32808
    sprite('Action_131_05', 3)	# 32809-32811
    sprite('Action_131_06', 3)	# 32812-32814

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_068_00', 4)	# 1-4
    sprite('Action_068_02', 3)	# 5-7
    Unknown1084(1)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    physicsYImpulse(23000)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    setGravity(1800)
    Unknown23087(38000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_068_03', 3)	# 8-10
    tag_voice(1, 'use156_0', 'use156_1', '', '')
    sprite('Action_068_04', 2)	# 11-12
    sprite('Action_130_00', 3)	# 13-15
    sprite('Action_130_01', 3)	# 16-18
    sprite('Action_130_02', 3)	# 19-21
    sprite('Action_130_03', 2)	# 22-23
    sprite('Action_130_04', 2)	# 24-25
    GFX_0('EffNmlAtk5C', 100)
    SFX_3('SE043')
    sprite('Action_130_05ex01', 3)	# 26-28	 **attackbox here**
    sprite('Action_130_05ex01', 2)	# 29-30	 **attackbox here**
    StartMultihit()
    sprite('Action_130_06', 4)	# 31-34
    sprite('Action_130_07', 4)	# 35-38
    label(0)
    sprite('Action_130_08', 3)	# 39-41
    sprite('Action_130_09', 3)	# 42-44
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_130_10', 2)	# 45-46
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_130_11', 5)	# 47-51
    sprite('Action_130_12', 3)	# 52-54
    sprite('Action_130_13', 3)	# 55-57
    Unknown18009(0)

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 16)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_130_06', 4)	# 1-4
    sprite('Action_130_07', 4)	# 5-8
    label(0)
    sprite('Action_130_08', 3)	# 9-11
    sprite('Action_130_09', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_130_10', 2)	# 15-16
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_130_11', 3)	# 17-19
    sprite('Action_130_12', 1)	# 20-20
    sprite('Action_130_13', 1)	# 21-21
    sprite('Action_000_00', 7)	# 22-28
    label(2)
    sprite('Action_403_00', 7)	# 29-35
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('Action_403_01', 3)	# 36-38
    teleportRelativeX(50000)
    tag_voice(0, 'use157_0', 'use157_1', '', '')
    sprite('Action_403_02', 3)	# 39-41
    teleportRelativeX(30000)
    sprite('Action_403_03', 6)	# 42-47	 **attackbox here**
    GFX_0('EffNmlAtk5B', 100)
    sprite('Action_403_04', 3)	# 48-50
    RefreshMultihit()
    sprite('Action_403_05', 3)	# 51-53
    sprite('Action_403_06', 3)	# 54-56
    sprite('Action_403_07', 3)	# 57-59
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('Action_000_00', 5)	# 60-64
    sprite('Action_000_01', 5)	# 65-69
    sprite('Action_000_02', 5)	# 70-74
    sprite('Action_000_03', 5)	# 75-79
    sprite('Action_000_04', 5)	# 80-84
    sprite('Action_000_05', 5)	# 85-89
    sprite('Action_000_06', 5)	# 90-94
    sprite('Action_000_07', 5)	# 95-99
    sprite('Action_000_08', 5)	# 100-104
    sprite('Action_000_09', 5)	# 105-109
    sprite('Action_000_10', 5)	# 110-114
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 115-115

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_403_07', 2)	# 1-2
    sprite('Action_012_00', 2)	# 3-4
    sprite('Action_012_01', 2)	# 5-6
    sprite('Action_132_00', 2)	# 7-8
    sprite('Action_132_01', 3)	# 9-11
    sprite('Action_132_02', 3)	# 12-14
    sprite('Action_132_03', 3)	# 15-17	 **attackbox here**
    SFX_3('SE042')
    GFX_0('EffNmlAtk5C_Chace2nd', 100)
    sprite('Action_132_04', 4)	# 18-21
    sprite('Action_132_05', 5)	# 22-26
    sprite('Action_132_06', 4)	# 27-30
    sprite('Action_132_07', 4)	# 31-34
    sprite('Action_014_00', 3)	# 35-37
    sprite('Action_014_01', 3)	# 38-40
    sprite('Action_014_02', 3)	# 41-43
    label(0)
    sprite('Action_000_00', 5)	# 44-48
    sprite('Action_000_01', 5)	# 49-53
    sprite('Action_000_02', 5)	# 54-58
    sprite('Action_000_03', 5)	# 59-63
    sprite('Action_000_04', 5)	# 64-68
    sprite('Action_000_05', 5)	# 69-73
    sprite('Action_000_06', 5)	# 74-78
    sprite('Action_000_07', 5)	# 79-83
    sprite('Action_000_08', 5)	# 84-88
    sprite('Action_000_09', 5)	# 89-93
    sprite('Action_000_10', 5)	# 94-98
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 99-99

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9266(16)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2035(0)
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_364_00', 1)	# 1-1
    Unknown3004(-5)
    sprite('Action_364_01', 1)	# 2-2
    Unknown3004(-10)
    GFX_0('EffNmlAtk5B_3rd_Zanzo2', 100)
    sprite('Action_364_02', 2)	# 3-4	 **attackbox here**
    Unknown3004(-20)
    physicsXImpulse(13000)
    physicsYImpulse(15000)
    setGravity(1900)
    sprite('Action_364_03', 2)	# 5-6	 **attackbox here**
    Unknown3004(-40)
    GFX_0('EffNmlAtk5A_4th_AirShadow', 100)
    sprite('Action_364_04', 1)	# 7-7	 **attackbox here**
    Unknown2035(1)
    Unknown3001(0)
    Unknown3004(0)
    sprite('Action_367_00', 1)	# 8-8
    Unknown1084(1)
    Unknown1086(22)
    teleportRelativeX(250000)
    teleportRelativeY(0)
    Unknown3001(255)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    sprite('Action_367_01', 1)	# 9-9
    sprite('Action_367_02', 1)	# 10-10
    sprite('Action_367_04', 1)	# 11-11
    sprite('Action_367_05', 1)	# 12-12
    sprite('Action_367_06', 1)	# 13-13
    sprite('Action_367_07', 2)	# 14-15
    physicsXImpulse(-65000)
    Unknown2035(0)
    GFX_0('EffNmlAtk5A_4th_AtkSub', 100)
    GFX_0('EffAssalut_Zanzo', 100)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown2005()
    teleportRelativeX(250000)
    Unknown35()
    sprite('Action_367_09', 2)	# 16-17
    Unknown3001(255)
    sprite('Action_367_10', 2)	# 18-19
    tag_voice(0, 'use158_0', 'use158_1', '', '')
    SFX_3('SE242')
    GFX_0('EffNmlAtk5A_4th_LandZanzo', 100)
    sprite('Action_367_12', 2)	# 20-21	 **attackbox here**
    Unknown2017(1)
    Unknown2053(1)
    Unknown2034(1)
    physicsXImpulse(-15000)
    Unknown1028(150)
    GFX_0('EffConfuse_AtkMatome', 104)
    Unknown23029(1, 100, 0)
    sprite('Action_367_11', 2)	# 22-23
    physicsXImpulse(-2560)
    sprite('Action_367_10', 2)	# 24-25
    sprite('Action_367_11', 2)	# 26-27
    sprite('Action_367_13', 4)	# 28-31
    physicsXImpulse(-5000)
    Unknown1028(50)
    sprite('Action_367_14', 7)	# 32-38
    Unknown8010(100, 1, 1)
    sprite('Action_367_15', 9)	# 39-47
    sprite('Action_367_16', 6)	# 48-53
    Unknown1084(1)
    sprite('Action_367_17', 5)	# 54-58

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
        Unknown9266(16)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('null', 22)	# 1-22
    sprite('null', 1)	# 23-23
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    sprite('Action_362_02', 3)	# 24-26	 **attackbox here**
    sprite('Action_362_03', 3)	# 27-29	 **attackbox here**
    Unknown3004(-15)
    sprite('Action_362_04', 3)	# 30-32	 **attackbox here**
    sprite('Action_362_05', 3)	# 33-35	 **attackbox here**
    GFX_0('EffNmlAtk5B_2nd_Zanzo2', 100)
    sprite('Action_362_06', 3)	# 36-38	 **attackbox here**
    sprite('Action_362_07', 3)	# 39-41	 **attackbox here**
    Unknown2035(1)
    Unknown3001(0)
    Unknown3004(0)
    sprite('Action_365_00ex01', 1)	# 42-42	 **attackbox here**
    Unknown1084(1)
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1045(-36000)
    GFX_0('EffConfuse_AtkMatome', 104)
    Unknown23029(1, 100, 0)
    sprite('Action_365_00ex01', 2)	# 43-44	 **attackbox here**
    Unknown3004(30)
    sprite('Action_365_00', 3)	# 45-47
    sprite('Action_365_00', 2)	# 48-49
    sprite('Action_365_00', 1)	# 50-50
    sprite('Action_365_01', 2)	# 51-52
    Unknown3001(255)
    Unknown2035(0)
    sprite('Action_365_02', 2)	# 53-54
    sprite('Action_365_03', 2)	# 55-56
    sprite('Action_365_04', 2)	# 57-58
    sprite('Action_365_05', 2)	# 59-60
    sprite('Action_365_06', 2)	# 61-62
    sprite('Action_000_00', 5)	# 63-67
    sprite('Action_000_01', 5)	# 68-72
    sprite('Action_000_02', 5)	# 73-77
    sprite('Action_000_03', 5)	# 78-82
    sprite('Action_000_04', 5)	# 83-87
    sprite('Action_000_05', 5)	# 88-92
    sprite('Action_000_06', 5)	# 93-97
    sprite('Action_000_07', 5)	# 98-102
    sprite('Action_000_08', 5)	# 103-107
    sprite('Action_000_09', 5)	# 108-112
    sprite('Action_000_10', 5)	# 113-117
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('Action_003_00', 3)	# 1-3
    sprite('Action_003_01', 4)	# 4-7
    teleportRelativeX(50000)
    sprite('Action_003_02', 4)	# 8-11
    teleportRelativeX(30000)
    physicsXImpulse(25000)
    Unknown1028(-5000)
    sprite('Action_003_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffNmlAtk5A_3rd', 100)
    Unknown1084(1)
    sprite('Action_003_04', 7)	# 16-22
    Recovery()
    Unknown2063()
    sprite('Action_003_05', 5)	# 23-27
    sprite('Action_003_06', 5)	# 28-32
    loopRest()
    sprite('Action_000_00', 5)	# 33-37
    sprite('Action_000_01', 5)	# 38-42
    sprite('Action_000_02', 5)	# 43-47
    sprite('Action_000_03', 5)	# 48-52
    sprite('Action_000_04', 5)	# 53-57
    sprite('Action_000_05', 5)	# 58-62
    sprite('Action_000_06', 5)	# 63-67
    sprite('Action_000_07', 5)	# 68-72
    sprite('Action_000_08', 5)	# 73-77
    sprite('Action_000_09', 5)	# 78-82
    sprite('Action_000_10', 5)	# 83-87

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9266(16)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2035(0)
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_364_00', 1)	# 1-1
    Unknown3004(-5)
    sprite('Action_364_01', 1)	# 2-2
    Unknown3004(-10)
    GFX_0('EffNmlAtk5B_3rd_Zanzo2', 100)
    sprite('Action_364_02', 2)	# 3-4	 **attackbox here**
    Unknown3004(-20)
    physicsXImpulse(13000)
    physicsYImpulse(15000)
    setGravity(1900)
    sprite('Action_364_03', 2)	# 5-6	 **attackbox here**
    Unknown3004(-40)
    GFX_0('EffNmlAtk5A_4th_AirShadow', 100)
    sprite('Action_364_04', 1)	# 7-7	 **attackbox here**
    Unknown2035(1)
    Unknown3001(0)
    Unknown3004(0)
    sprite('Action_367_00', 1)	# 8-8
    Unknown1084(1)
    Unknown1086(22)
    teleportRelativeX(250000)
    teleportRelativeY(0)
    Unknown3001(255)
    Unknown3004(0)
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    sprite('Action_367_01', 1)	# 9-9
    sprite('Action_367_02', 1)	# 10-10
    sprite('Action_367_04', 1)	# 11-11
    sprite('Action_367_05', 1)	# 12-12
    sprite('Action_367_06', 1)	# 13-13
    sprite('Action_367_07', 2)	# 14-15
    physicsXImpulse(-65000)
    Unknown2035(0)
    GFX_0('EffNmlAtk5A_4th_LandZanzo', 100)
    GFX_0('EffNmlAtk5A_4th_AtkSub', 100)
    GFX_0('EffAssalut_Zanzo', 100)
    Unknown36(1)
    Unknown2005()
    Unknown35()
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    Unknown36(1)
    Unknown2005()
    teleportRelativeX(250000)
    Unknown35()
    sprite('Action_367_09', 2)	# 16-17
    SFX_3('SE242')
    Unknown3001(255)
    sprite('Action_367_10', 2)	# 18-19
    SFX_3('SE242')
    GFX_0('EffNmlAtk5A_4th_LandZanzo', 100)
    sprite('Action_367_12', 2)	# 20-21	 **attackbox here**
    Unknown2017(1)
    Unknown2053(1)
    Unknown2034(1)
    physicsXImpulse(-15000)
    Unknown1028(150)
    GFX_0('EffConfuse_AtkMatome', 104)
    Unknown23029(1, 100, 0)
    sprite('Action_367_11', 2)	# 22-23
    physicsXImpulse(-2560)
    sprite('Action_367_10', 2)	# 24-25
    sprite('Action_367_11', 2)	# 26-27
    sprite('Action_367_13', 4)	# 28-31
    physicsXImpulse(-5000)
    Unknown1028(50)
    sprite('Action_367_14', 7)	# 32-38
    Unknown8010(100, 1, 1)
    sprite('Action_367_15', 9)	# 39-47
    sprite('Action_367_16', 6)	# 48-53
    Unknown1084(1)
    sprite('Action_367_17', 5)	# 54-58

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(3000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(23000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 41000):
                    SLOT_12 = 41000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('Action_010_00', 3)	# 1-3
    sprite('Action_045_00', 3)	# 4-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 2)	# 10-11
    label(0)
    sprite('Action_045_03', 2)	# 12-13
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 2)	# 14-15
    sprite('Action_045_05', 2)	# 16-17
    sprite('Action_045_06', 2)	# 18-19
    sprite('Action_045_07', 2)	# 20-21
    Unknown8006(100, 1, 1)
    sprite('Action_045_08', 2)	# 22-23
    sprite('Action_045_09', 2)	# 24-25
    sprite('Action_045_10', 2)	# 26-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 28-30
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 31-33	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_01', 2)	# 34-35	 **attackbox here**
    Unknown23027()
    sprite('Action_055_02', 4)	# 36-39
    SFX_3('SE042')
    SFX_4('use154')
    sprite('Action_055_03', 7)	# 40-46
    sprite('Action_055_04', 5)	# 47-51
    sprite('Action_055_05', 5)	# 52-56

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        Unknown11001(0, -2, -2)
        Hitstop(10)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(11500)
        AirPushbackY(38000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown9016(1)
        Unknown11072(1, 200000, -80000)
    sprite('Action_056_00', 8)	# 1-8	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('Action_057_00', 5)	# 9-13
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5004()
    sprite('Action_057_01', 4)	# 14-17
    SFX_1('use153')
    Unknown5000(17, 0)
    Unknown36(22)
    Unknown1045(-9000)
    Unknown8007(100, 1, 1)
    Unknown35()
    sprite('Action_057_02', 2)	# 18-19
    sprite('Action_057_03', 2)	# 20-21
    physicsXImpulse(10000)
    Unknown1028(2500)
    physicsYImpulse(35000)
    setGravity(2200)
    Unknown22004(9, 1)
    Unknown4004('6566666563745f3338360000000000000000000000000000000000000000000064000000')
    sprite('Action_057_04', 2)	# 22-23
    SFX_3('SE043')
    sprite('Action_057_05', 2)	# 24-25	 **attackbox here**
    sendToLabelUpon(2, 1)
    GFX_0('EffNmlAtkThow', 100)
    physicsXImpulse(20000)
    Unknown1028(-650)
    setGravity(3000)
    sprite('Action_057_06', 8)	# 26-33
    sprite('Action_057_07', 5)	# 34-38
    sprite('Action_057_08', 4)	# 39-42
    sprite('Action_057_09', 4)	# 43-46
    label(0)
    sprite('Action_057_10', 3)	# 47-49
    sprite('Action_057_11', 3)	# 50-52
    gotoLabel(0)
    label(1)
    sprite('Action_057_12', 3)	# 53-55
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_057_13', 4)	# 56-59
    sprite('Action_057_14', 3)	# 60-62
    sprite('Action_057_15', 2)	# 63-64

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(3000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(23000)
            if (SLOT_18 >= 7):
                Unknown1015(440)
                if (SLOT_12 >= 41000):
                    SLOT_12 = 41000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('Action_010_00', 3)	# 1-3
    sprite('Action_045_00', 3)	# 4-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 2)	# 10-11
    label(0)
    sprite('Action_045_03', 2)	# 12-13
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 2)	# 14-15
    sprite('Action_045_05', 2)	# 16-17
    sprite('Action_045_06', 2)	# 18-19
    sprite('Action_045_07', 2)	# 20-21
    Unknown8006(100, 1, 1)
    sprite('Action_045_08', 2)	# 22-23
    sprite('Action_045_09', 2)	# 24-25
    sprite('Action_045_10', 2)	# 26-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 28-30
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 31-33	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_01', 2)	# 34-35	 **attackbox here**
    Unknown23027()
    sprite('Action_055_02', 4)	# 36-39
    SFX_3('SE042')
    sprite('Action_055_03', 9)	# 40-48
    SFX_4('use154')
    sprite('Action_055_04', 5)	# 49-53
    sprite('Action_055_05', 5)	# 54-58

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        Unknown11001(0, -2, -2)
        Hitstop(10)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(11500)
        AirPushbackY(38000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown9016(1)
        Unknown11072(1, 200000, -80000)
    sprite('Action_056_00', 8)	# 1-8	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    Unknown2018(0, 80)
    sprite('Action_057_00ex01', 2)	# 9-10
    Unknown5000(25, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('Action_057_00', 3)	# 11-13
    Unknown2005()
    Unknown5000(25, 0)
    Unknown5004()
    sprite('Action_057_01', 4)	# 14-17
    SFX_1('use153')
    Unknown5000(17, 0)
    Unknown36(22)
    Unknown1045(-9000)
    Unknown8007(100, 1, 1)
    Unknown35()
    sprite('Action_057_02', 2)	# 18-19
    sprite('Action_057_03', 2)	# 20-21
    physicsXImpulse(10000)
    Unknown1028(2500)
    physicsYImpulse(35000)
    setGravity(2200)
    Unknown22004(9, 1)
    Unknown4004('6566666563745f3338360000000000000000000000000000000000000000000064000000')
    sprite('Action_057_04', 2)	# 22-23
    SFX_3('SE043')
    sprite('Action_057_05', 2)	# 24-25	 **attackbox here**
    sendToLabelUpon(2, 1)
    GFX_0('EffNmlAtkThow', 100)
    physicsXImpulse(20000)
    Unknown1028(-650)
    setGravity(3000)
    sprite('Action_057_06', 8)	# 26-33
    sprite('Action_057_07', 5)	# 34-38
    sprite('Action_057_08', 4)	# 39-42
    sprite('Action_057_09', 4)	# 43-46
    label(0)
    sprite('Action_057_10', 3)	# 47-49
    sprite('Action_057_11', 3)	# 50-52
    gotoLabel(0)
    label(1)
    sprite('Action_057_12', 3)	# 53-55
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_057_13', 4)	# 56-59
    sprite('Action_057_14', 3)	# 60-62
    sprite('Action_057_15', 2)	# 63-64

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        Hitstop(4)
        Unknown11001(0, -2, -2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackX(8000)
        AirPushbackY(32000)
        Unknown9016(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown2035(0)
    sprite('Action_363_00', 2)	# 1-2
    sprite('Action_363_01', 4)	# 3-6
    sprite('Action_363_02', 2)	# 7-8
    SFX_3('SE028_RunDash')
    GFX_0('EffReversal_Zanzo', 100)
    physicsXImpulse(8000)
    physicsYImpulse(6000)
    Unknown3004(-40)
    Unknown2035(1)
    Unknown7006('use302_1', 100, 828732277, 845101104, 0, 0, 100, 828732277, 828321841, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_363_03', 2)	# 9-10
    sprite('Action_366_01', 1)	# 11-11
    Unknown1084(1)
    physicsXImpulse(12000)
    physicsYImpulse(12000)
    sprite('Action_366_00', 1)	# 12-12
    Unknown3004(60)
    sprite('Action_057_04', 1)	# 13-13
    Unknown1084(1)
    physicsXImpulse(7000)
    physicsYImpulse(32000)
    setGravity(2500)
    Unknown1028(-100)
    clearUponHandler(2)
    SFX_3('SE050_SlideDash')
    Unknown3004(40)
    SFX_3('SE043')
    Unknown2035(0)
    sprite('Action_057_05ex02', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sendToLabelUpon(2, 1)
    GFX_0('EffNmlAtkThow', 100)
    sprite('Action_057_05ex03', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_057_05ex03', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_057_05ex04', 1)	# 17-17	 **attackbox here**
    sprite('Action_057_06', 4)	# 18-21
    setInvincible(0)
    sprite('Action_057_07', 5)	# 22-26
    sprite('Action_057_08', 4)	# 27-30
    sprite('Action_057_09', 4)	# 31-34
    label(0)
    sprite('Action_057_10', 3)	# 35-37
    sprite('Action_057_11', 3)	# 38-40
    gotoLabel(0)
    label(1)
    sprite('Action_057_12', 2)	# 41-42
    setInvincible(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_057_13ex01', 18)	# 43-60
    sprite('Action_057_14ex01', 5)	# 61-65
    sprite('Action_057_15', 4)	# 66-69

@State
def AssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(80)
        Hitstop(4)
        Unknown11001(3, 3, 3)
        Unknown11028(20)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(20000)
        AirUntechableTime(45)
        PushbackX(19800)
        Unknown9016(1)

        def upon_11():
            Unknown2017(0)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
            Unknown2006()

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('Action_210_00', 3)	# 1-3
    sprite('Action_210_01', 3)	# 4-6
    sprite('Action_210_02', 2)	# 7-8
    sprite('Action_210_03', 1)	# 9-9
    physicsXImpulse(5000)
    Unknown3004(-50)
    sprite('Action_210_04', 1)	# 10-10
    sprite('Action_210_05', 1)	# 11-11
    SFX_3('SE242')
    Unknown7006('use204_1', 100, 845509493, 811545392, 0, 0, 100, 845509493, 828322608, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_210_06', 2)	# 12-13	 **attackbox here**
    physicsXImpulse(150000)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    GFX_0('EffAssalut_Blade', 100)
    Unknown2035(1)
    sprite('Action_210_07', 3)	# 14-16	 **attackbox here**
    sprite('Action_210_08', 1)	# 17-17	 **attackbox here**
    Unknown3004(80)
    physicsXImpulse(8000)
    Unknown1028(-400)
    GFX_0('EffAssalut_Zanzo', 100)
    Unknown4004('6566666563745f3033380000000000000000000000000000000000000000000064000000')
    sprite('Action_210_09', 2)	# 18-19	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('Action_210_10', 3)	# 20-22
    Unknown2035(0)
    Unknown2017(1)
    sprite('Action_210_11', 4)	# 23-26
    sprite('Action_210_12', 4)	# 27-30
    sprite('Action_210_11', 4)	# 31-34
    sprite('Action_210_12', 4)	# 35-38
    sprite('Action_210_13', 4)	# 39-42
    Unknown1084(1)
    sprite('Action_210_14', 3)	# 43-45
    Unknown2006()

@State
def AssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2400)
        AttackP1(70)
        Hitstop(4)
        Unknown11028(20)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(38000)
        AirUntechableTime(60)
        PushbackX(19800)
        Unknown9016(1)

        def upon_11():
            Unknown2017(0)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
            Unknown2006()

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('Action_211_00', 6)	# 1-6
    sprite('Action_211_01', 6)	# 7-12
    sprite('Action_211_02', 5)	# 13-17
    sprite('Action_211_03', 1)	# 18-18
    physicsXImpulse(5000)
    Unknown3004(-50)
    sprite('Action_211_04', 1)	# 19-19
    sprite('Action_211_05', 1)	# 20-20
    SFX_3('SE242')
    Unknown7006('use204_0', 100, 845509493, 845099824, 0, 0, 100, 845509493, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_211_06', 3)	# 21-23	 **attackbox here**
    Unknown2035(1)
    physicsXImpulse(180000)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    GFX_0('EffAssalut_Blade', 100)
    sprite('Action_211_07', 3)	# 24-26	 **attackbox here**
    sprite('Action_211_08', 1)	# 27-27	 **attackbox here**
    Unknown3004(80)
    physicsXImpulse(8000)
    Unknown1028(-400)
    GFX_0('EffAssalut_Zanzo', 100)
    Unknown4004('6566666563745f3033380000000000000000000000000000000000000000000064000000')
    sprite('Action_211_09', 2)	# 28-29	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('Action_211_10', 3)	# 30-32
    Unknown2035(0)
    Unknown2017(1)
    sprite('Action_211_11', 3)	# 33-35
    sprite('Action_211_12', 3)	# 36-38
    sprite('Action_211_11', 3)	# 39-41
    sprite('Action_211_13', 3)	# 42-44
    Unknown1084(1)
    sprite('Action_211_14', 3)	# 45-47
    sprite('Action_211_15', 3)	# 48-50
    Unknown2006()

@State
def AssaultEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(600)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(4)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        AirPushbackX(8000)
        AirPushbackY(38000)
        AirUntechableTime(60)
        PushbackX(19800)
        Unknown9016(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown11064(1)
        Unknown11068(1)
        Unknown11056(4)
        Unknown11069('AssaultEx')
        Unknown2073(1)

        def upon_78():
            Unknown14083(0)
            Unknown11044(1)
            sendToLabel(10)

        def upon_11():
            Unknown2017(0)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
            Unknown2006()

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('Action_210_00', 2)	# 1-2
    sprite('Action_210_01', 1)	# 3-3
    sprite('Action_210_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_210_02', 1)	# 5-5
    sprite('Action_210_03', 1)	# 6-6
    physicsXImpulse(5000)
    Unknown3004(-50)
    sprite('Action_210_04', 1)	# 7-7
    sprite('Action_210_05', 1)	# 8-8
    SFX_3('SE242')
    Unknown7006('use205_0', 100, 845509493, 811546160, 0, 0, 100, 845509493, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_210_06', 2)	# 9-10	 **attackbox here**
    Unknown2035(1)
    physicsXImpulse(250000)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    GFX_0('EffAssalut_BladeEx', 100)
    sprite('Action_210_07', 3)	# 11-13	 **attackbox here**
    sprite('Action_210_08', 1)	# 14-14	 **attackbox here**
    Unknown3004(80)
    physicsXImpulse(8000)
    Unknown1028(-400)
    GFX_0('EffAssalut_Zanzo', 100)
    Unknown4004('6566666563745f3033380000000000000000000000000000000000000000000064000000')
    sprite('Action_210_09', 2)	# 15-16	 **attackbox here**
    Unknown23027()
    Recovery()
    sprite('Action_210_10', 3)	# 17-19
    Unknown2035(0)
    Unknown2017(1)
    sprite('Action_210_11', 4)	# 20-23
    sprite('Action_210_12', 4)	# 24-27
    sprite('Action_210_13', 4)	# 28-31
    Unknown1084(1)
    sprite('Action_210_14', 3)	# 32-34
    Unknown2006()
    ExitState()
    label(10)
    sprite('Action_213_00', 4)	# 35-38
    clearUponHandler(11)
    clearUponHandler(78)
    Unknown3004(80)
    Unknown1084(1)
    setInvincible(1)
    Unknown2017(0)
    Unknown2035(1)
    Unknown1086(22)
    teleportRelativeX(250000)
    Damage(300)
    Unknown11057(600)
    Hitstop(0)
    Unknown11001(0, 60, 60)
    PushbackX(0)
    Unknown30048(1)
    Unknown11023(1)
    label(11)
    sprite('Action_213_01', 1)	# 39-39	 **attackbox here**
    Unknown1086(22)
    Unknown1084(1)
    sprite('Action_213_02', 1)	# 40-40
    Unknown2035(0)
    Unknown1045(26000)
    teleportRelativeX(250000)
    sprite('Action_213_03', 1)	# 41-41
    sprite('Action_213_04', 1)	# 42-42
    sprite('Action_213_05', 2)	# 43-44
    sprite('Action_213_06', 1)	# 45-45
    sprite('Action_213_06', 1)	# 46-46
    Unknown2038(1)
    Unknown2005()
    Unknown11099(1)
    RefreshMultihit()
    (SLOT_2 <= 1)
    if SLOT_0:
        _gotolabel(11)
    label(12)
    sprite('Action_210_08', 1)	# 47-47	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(250000)
    Unknown1084(1)
    Unknown1045(26000)
    RefreshMultihit()
    Unknown11099(0)
    Unknown2035(0)
    sprite('Action_213_08', 3)	# 48-50
    sprite('Action_213_09', 3)	# 51-53
    sprite('Action_213_10', 8)	# 54-61
    sprite('Action_213_11', 3)	# 62-64
    sprite('Action_213_12', 4)	# 65-68
    sprite('Action_213_13', 1)	# 69-69
    sprite('Action_213_01', 5)	# 70-74	 **attackbox here**
    RefreshMultihit()
    Unknown11057(800)
    Unknown1086(22)
    Unknown2005()
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    GFX_0('EffAssalut_Blade', 100)
    Unknown11099(1)
    sprite('Action_213_14', 1)	# 75-75
    Unknown2035(1)
    physicsXImpulse(30000)
    SFX_3('SE242')
    sprite('Action_213_14ex01', 6)	# 76-81	 **attackbox here**
    RefreshMultihit()
    sprite('Action_213_14ex01', 1)	# 82-82	 **attackbox here**
    RefreshMultihit()
    Damage(1000)
    sprite('Action_213_15', 5)	# 83-87
    physicsXImpulse(20000)
    Unknown1028(-1000)
    GFX_0('EffAssalut_Zanzo', 100)
    sprite('Action_213_16', 6)	# 88-93
    Unknown2035(0)
    Unknown4004('6566666563745f3033380000000000000000000000000000000000000000000064000000')
    sprite('Action_213_17', 6)	# 94-99
    sprite('Action_213_16', 6)	# 100-105
    Unknown1084(1)
    Unknown1045(6000)
    Unknown23073()
    sprite('Action_213_17', 6)	# 106-111
    sprite('Action_213_16', 6)	# 112-117
    Unknown7006('use205_1', 100, 845509493, 845100592, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_213_17', 6)	# 118-123
    sprite('Action_213_18', 6)	# 124-129	 **attackbox here**
    RefreshMultihit()
    Damage(1800)
    Unknown11057(1200)
    Hitstop(0)
    Unknown11001(0, 3, 3)
    PushbackX(0)
    Unknown9130(16)
    Unknown9142(100)
    GroundedHitstunAnimation(2)
    Unknown11064(0)
    Unknown11069('')
    Unknown11044(0)

    def upon_78():
        Unknown14083(1)
    sprite('Action_213_17', 6)	# 130-135
    sprite('Action_213_16', 6)	# 136-141
    setInvincible(0)
    sprite('Action_213_17', 6)	# 142-147
    sprite('Action_213_16', 6)	# 148-153
    sprite('Action_213_17', 6)	# 154-159
    sprite('Action_213_16', 6)	# 160-165
    sprite('Action_213_17', 6)	# 166-171
    sprite('Action_213_19', 7)	# 172-178
    sprite('Action_213_20', 4)	# 179-182
    Unknown2006()

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_135_00', 4)	# 1-4
    sprite('Action_135_01', 4)	# 5-8
    sprite('Action_135_02', 1)	# 9-9
    Unknown7006('use200_0', 100, 845509493, 828321840, 0, 0, 100, 845509493, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('Shot_Zanzo', 0)
    sprite('Action_135_02', 2)	# 10-11
    Unknown23029(4, 212, 0)
    sprite('Action_135_03', 3)	# 12-14
    GFX_0('Shot_Charge', 0)
    Unknown38(4, 1)
    Unknown23029(4, 200, 0)
    sprite('Action_135_04', 4)	# 15-18
    sprite('Action_135_05', 5)	# 19-23
    sprite('Action_135_06', 4)	# 24-27
    Recovery()
    sprite('Action_135_07', 4)	# 28-31

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_137_00', 4)	# 1-4
    sprite('Action_137_01', 4)	# 5-8
    sprite('Action_137_02', 1)	# 9-9
    Unknown7006('use200_0', 100, 845509493, 828321840, 0, 0, 100, 845509493, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('Shot_Zanzo', 0)
    sprite('Action_137_02', 2)	# 10-11
    Unknown23029(4, 212, 0)
    sprite('Action_137_03', 3)	# 12-14
    GFX_0('Shot_Charge', 0)
    Unknown38(4, 1)
    Unknown23029(4, 201, 0)
    sprite('Action_137_04', 4)	# 15-18
    sprite('Action_137_05', 5)	# 19-23
    sprite('Action_137_09', 4)	# 24-27
    Recovery()
    sprite('Action_137_10', 4)	# 28-31

@State
def ShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_137_00', 3)	# 1-3
    sprite('Action_136_00', 1)	# 4-4
    sprite('Action_137_01', 4)	# 5-8
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7006('use202_0', 100, 845509493, 828322352, 0, 0, 100, 845509493, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_137_02', 1)	# 9-9
    GFX_0('Shot_Zanzo', 0)
    sprite('Action_137_02', 2)	# 10-11
    Unknown23029(5, 212, 0)
    sprite('Action_137_03', 3)	# 12-14
    GFX_0('ShotEx_Charge', 0)
    Unknown38(5, 1)
    Unknown23029(5, 202, 0)
    sprite('Action_137_04', 4)	# 15-18
    sprite('Action_137_05', 5)	# 19-23
    sprite('Action_137_09', 4)	# 24-27
    Recovery()
    sprite('Action_137_10', 4)	# 28-31

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('Action_145_00', 3)	# 1-3
    sprite('Action_145_01', 2)	# 4-5
    SLOT_4 = 1
    Unknown28(2, 'CmnActJumpLanding')
    Unknown1084(1)
    sprite('Action_145_02', 2)	# 6-7
    Unknown7006('use201_0', 100, 845509493, 828322096, 0, 0, 100, 845509493, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('Shot_Zanzo', 0)
    physicsXImpulse(-5120)
    physicsYImpulse(18000)
    Unknown1043()
    Unknown23029(4, 212, 0)
    sprite('Action_145_03', 3)	# 8-10
    GFX_0('Shot_Charge', 0)
    Unknown38(4, 1)
    Unknown23029(4, 203, 0)
    sprite('Action_145_04', 3)	# 11-13
    Recovery()
    sprite('Action_145_05', 4)	# 14-17
    sprite('Action_145_06', 4)	# 18-21
    sprite('Action_145_07', 2)	# 22-23

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('Action_146_00', 3)	# 1-3
    sprite('Action_146_01', 2)	# 4-5
    SLOT_4 = 1
    Unknown28(2, 'CmnActJumpLanding')
    Unknown1084(1)
    sprite('Action_146_02', 2)	# 6-7
    Unknown7006('use201_0', 100, 845509493, 828322096, 0, 0, 100, 845509493, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('Shot_Zanzo', 0)
    physicsXImpulse(9000)
    physicsYImpulse(18000)
    Unknown1043()
    Unknown23029(4, 212, 0)
    sprite('Action_146_03', 3)	# 8-10
    GFX_0('Shot_Charge', 0)
    Unknown38(4, 1)
    Unknown23029(4, 204, 0)
    sprite('Action_146_04', 3)	# 11-13
    sprite('Action_146_05', 4)	# 14-17
    Recovery()
    sprite('Action_146_06', 4)	# 18-21
    sprite('Action_146_07', 2)	# 22-23

@State
def AirShotEx():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('Action_145_00', 3)	# 1-3
    sprite('Action_145_01', 2)	# 4-5
    SLOT_4 = 1
    Unknown28(2, 'CmnActJumpLanding')
    Unknown1084(1)
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7006('use202_0', 100, 845509493, 828322352, 0, 0, 100, 845509493, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_145_02', 2)	# 6-7
    GFX_0('Shot_Zanzo', 0)
    physicsXImpulse(-9000)
    physicsYImpulse(23000)
    Unknown1043()
    Unknown23029(5, 212, 0)
    sprite('Action_145_03', 3)	# 8-10
    GFX_0('ShotEx_Charge', 0)
    Unknown38(5, 1)
    Unknown23029(5, 205, 0)
    sprite('Action_145_04', 3)	# 11-13
    sprite('Action_145_05', 4)	# 14-17
    Recovery()
    sprite('Action_145_06', 4)	# 18-21
    sprite('Action_145_07', 2)	# 22-23

@State
def AirAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(750)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(2)
        Unknown11001(0, -1, -1)
        AirPushbackX(55000)
        AirPushbackY(-55000)
        Unknown30055('701101005000000000000000')
        Unknown30056('204e00005000000000000000')
        AirUntechableTime(61)
        Unknown9190(1)
        Unknown9118(10)
        AirHitstunAfterWallbounce(28)
        PushbackX(19800)
        Unknown11056(2)
        Unknown9016(1)
        clearUponHandler(2)

        def upon_STATE_END():
            Unknown2006()

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('Action_278_00', 3)	# 1-3
    sprite('Action_278_00', 1)	# 4-4
    Unknown1084(1)
    physicsXImpulse(-640)
    physicsYImpulse(640)
    setGravity(0)
    sprite('Action_278_01', 2)	# 5-6
    Unknown7006('use212_0', 100, 845509493, 828322353, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_278_02', 4)	# 7-10
    sprite('Action_278_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(55000)
    physicsYImpulse(-60000)
    SFX_3('SE038')
    sprite('Action_278_04', 32767)	# 12-32778	 **attackbox here**
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_278_05', 2)	# 32779-32780	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown14070('AirAssaultA_AddAttack')
    RefreshMultihit()
    physicsXImpulse(15000)
    Unknown1028(-1000)
    physicsYImpulse(0)
    Hitstop(8)
    AirUntechableTime(19)
    Unknown9190(0)
    Unknown11068(1)
    AirPushbackX(3000)
    AirPushbackY(30000)
    PushbackX(30400)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)

    def upon_78():
        Unknown14072('AirAssaultA_AddAttack')
    sprite('Action_278_06', 4)	# 32781-32784
    Recovery()
    sprite('Action_278_07', 5)	# 32785-32789
    Unknown14074('AirAssaultA_AddAttack')
    sprite('Action_278_08', 5)	# 32790-32794
    Unknown1084(1)
    sprite('Action_278_09', 3)	# 32795-32797
    sprite('Action_278_10', 3)	# 32798-32800
    sprite('Action_278_11', 3)	# 32801-32803

@State
def AirAssaultA_AddAttack():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Confuse')
        AttackLevel_(3)
        Damage(500)
        AttackP2(85)
        Unknown11092(1)
        PushbackX(0)
        AirPushbackX(8000)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(40)
        Hitstop(4)
        Unknown11001(0, 10, 10)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown30068(1)
        Unknown11056(2)
    sprite('Action_363_00', 2)	# 1-2
    sprite('Action_363_01', 4)	# 3-6
    sprite('Action_363_02', 2)	# 7-8
    SFX_3('SE028_RunDash')
    GFX_0('EffNmlAtk5B_3rd_Zanzo', 100)
    physicsXImpulse(24000)
    physicsYImpulse(6000)
    Unknown3004(-40)
    Unknown2035(1)
    Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_363_03', 2)	# 9-10
    Unknown2017(0)
    Unknown7006('use110_2', 100, 828732277, 828323888, 0, 0, 100, 828732277, 828323632, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_366_00ex01', 3)	# 11-13	 **attackbox here**
    Unknown1084(1)
    Unknown22004(12, 1)
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    sprite('Action_366_00', 2)	# 14-15
    Unknown3004(60)
    if (SLOT_25 <= 150000):
        Unknown1019(-100)
        Unknown2005()
    Unknown1086(22)
    teleportRelativeY(250000)
    teleportRelativeX(50000)
    sprite('Action_368_01', 2)	# 16-17
    Unknown2017(1)
    Unknown2006()
    Unknown1084(1)
    Unknown1045(6000)
    physicsYImpulse(10000)
    setGravity(1800)
    clearUponHandler(2)
    SFX_3('SE050_SlideDash')
    Unknown3004(40)
    sprite('Action_368_02', 2)	# 18-19
    sprite('Action_368_03', 2)	# 20-21
    Unknown2035(0)
    sprite('Action_368_04', 4)	# 22-25
    sprite('Action_368_05', 2)	# 26-27
    sprite('Action_368_06', 2)	# 28-29
    GFX_0('EffAirAssalut_Add', 100)
    SFX_3('SE043')
    physicsYImpulse(-50000)
    setGravity(2500)
    sendToLabelUpon(2, 1)
    sprite('Action_368_07ex01', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    AirPushbackX(1500)
    AirPushbackY(-70000)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown11001(-3, -3, 2)
    Hitstop(9)
    Unknown9310(17)
    Unknown9266(0)
    Unknown9016(0)
    clearUponHandler(77)
    clearUponHandler(81)
    sprite('Action_368_08', 3)	# 33-35
    Recovery()
    label(0)
    sprite('Action_368_09', 3)	# 36-38
    sprite('Action_368_10', 3)	# 39-41
    gotoLabel(0)
    label(1)
    sprite('Action_368_11', 5)	# 42-46
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_368_12', 5)	# 47-51
    sprite('Action_368_13', 13)	# 52-64
    sprite('Action_368_14', 5)	# 65-69

@State
def AirAssaultB():

    def upon_IMMEDIATE():
        Unknown17011('AirAssaultB_Exe', 2, 1, 0)
        AttackLevel_(5)
        Unknown11046(0)
        Unknown11045(1)
        Unknown30061(1)
        Unknown11002(-1)
        Unknown11032('e093040000000000400d0300c0f2fcff')
        Unknown23027()
        clearUponHandler(2)
    sprite('Action_279_00', 3)	# 1-3
    sprite('Action_279_00', 4)	# 4-7
    Unknown1084(1)
    physicsXImpulse(-640)
    physicsYImpulse(640)
    setGravity(0)
    sprite('Action_279_01', 10)	# 8-17
    sprite('Action_279_02', 12)	# 18-29
    Unknown7006('use213_0', 100, 845509493, 828322609, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_279_03', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(75000)
    physicsYImpulse(-70000)
    SFX_3('SE038')
    sprite('Action_279_04', 32767)	# 32-32798	 **attackbox here**
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_279_05', 2)	# 32799-32800
    Unknown8000(100, 1, 1)
    physicsXImpulse(20000)
    Unknown1028(-1500)
    physicsYImpulse(0)
    Recovery()
    sprite('Action_279_06', 4)	# 32801-32804
    sprite('Action_279_07', 4)	# 32805-32808
    sprite('Action_279_08', 4)	# 32809-32812
    Unknown1084(1)
    sprite('Action_279_09', 3)	# 32813-32815
    sprite('Action_279_10', 3)	# 32816-32818
    sprite('Action_279_11', 3)	# 32819-32821

@State
def AirAssaultB_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(3000)
        AttackP2(50)
        Unknown11091(5)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(6000)
        AirPushbackY(41000)
        Unknown9310(1)
        Unknown9016(1)
        AirUntechableTime(80)
        Hitstop(5)
        Unknown30068(1)
        Unknown11056(2)
        sendToLabelUpon(2, 1)
        Unknown48('190000000200000034000000160000000200000025000000')
    sprite('Action_280_00', 12)	# 1-12
    if SLOT_52:
        Unknown5000(17, 0)
    else:
        Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 15)	# 13-27
    sprite('Action_280_02', 6)	# 28-33	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(-9000)
    physicsYImpulse(30000)
    setGravity(2500)
    SFX_1('use215_1')
    sprite('Action_280_03', 4)	# 34-37
    sprite('Action_280_04', 3)	# 38-40
    sprite('Action_280_05', 3)	# 41-43
    sprite('Action_280_06', 3)	# 44-46
    label(0)
    sprite('Action_280_07', 3)	# 47-49
    sprite('Action_280_08', 3)	# 50-52
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 53-55
    Unknown14083(1)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 56-60
    Recovery()
    sprite('Action_280_11', 3)	# 61-63

@State
def AirAssaultEx():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(750)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(2)
        Unknown11001(0, -1, -1)
        AirPushbackX(48000)
        AirPushbackY(-50000)
        AirUntechableTime(60)
        Unknown9190(1)
        Unknown11056(0)
        Unknown9016(1)
        Unknown9118(10)
        AirHitstunAfterWallbounce(25)
        Unknown30065(0)
        Unknown11091(10)
        PushbackX(19800)
        Unknown2073(1)
        clearUponHandler(2)
        Unknown11044(1)

        def upon_78():
            clearUponHandler(2)
            Hitstop(0)
            Unknown9016(0)
            Unknown11064(1)
            Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
            Unknown13024(0)
            enterState('AirAssaultEx_catch1')
            Unknown11069('AirAssaultEx_catch1')

        def upon_STATE_END():
            Unknown2006()

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('Action_278_00', 3)	# 1-3
    sprite('Action_278_00', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    Unknown1084(1)
    physicsXImpulse(-640)
    physicsYImpulse(640)
    setGravity(0)
    sprite('Action_278_01', 2)	# 5-6
    Unknown7006('use212_0', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_278_02', 4)	# 7-10
    sprite('Action_278_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(80000)
    physicsYImpulse(-65000)
    SFX_3('SE038')
    sprite('Action_279_04', 32767)	# 12-32778	 **attackbox here**
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_278_05', 1)	# 32779-32779	 **attackbox here**
    clearUponHandler(78)
    Unknown8000(100, 1, 1)
    RefreshMultihit()
    Unknown11064(0)
    physicsXImpulse(30000)
    Unknown1028(-1500)
    physicsYImpulse(0)
    Unknown9016(1)
    Hitstop(6)
    AirUntechableTime(20)
    Unknown9190(0)
    AirPushbackX(3000)
    AirPushbackY(32000)
    PushbackX(30400)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    sprite('Action_278_05', 1)	# 32780-32780	 **attackbox here**
    sprite('Action_278_06', 2)	# 32781-32782
    Recovery()
    sprite('Action_278_07', 4)	# 32783-32786
    sprite('Action_278_08', 4)	# 32787-32790
    Unknown1084(1)
    sprite('Action_278_09', 3)	# 32791-32793
    sprite('Action_278_10', 2)	# 32794-32795
    sprite('Action_278_11', 2)	# 32796-32797

@State
def AirAssaultEx_catch1():

    def upon_IMMEDIATE():
        Unknown17011('AirAssaultEx_Exe1', 2, 1, 0)
        Unknown11023(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        Unknown30065(0)
        Unknown11091(10)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown30068(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11108('03000000')
        Unknown11069('AirAssaultEx_Exe1')
        Unknown11064(1)
        Unknown11023(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
        Unknown48('190000000200000034000000160000000200000025000000')
    sprite('Action_279_04', 1)	# 1-1	 **attackbox here**
    if SLOT_52:
        Unknown5000(17, 0)
    else:
        Unknown5000(0, 0)
    clearUponHandler(2)
    Unknown7006('use214_0', 100, 845509493, 828322865, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_279_04', 32767)	# 2-32768	 **attackbox here**
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_278_05', 2)	# 32769-32770	 **attackbox here**
    clearUponHandler(78)
    RefreshMultihit()
    physicsXImpulse(30000)
    Unknown1028(-1500)
    physicsYImpulse(0)
    Unknown9016(1)
    AirUntechableTime(20)
    Unknown9190(0)
    AirPushbackX(3000)
    AirPushbackY(32000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    sprite('Action_278_06', 3)	# 32771-32773
    setInvincible(0)
    sprite('Action_278_07', 4)	# 32774-32777
    sprite('Action_278_08', 4)	# 32778-32781
    Unknown1084(1)
    sprite('Action_278_09', 2)	# 32782-32783
    sprite('Action_278_10', 2)	# 32784-32785
    sprite('Action_278_11', 2)	# 32786-32787

@State
def AirAssaultEx_Exe1():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(2500)
        AttackP2(100)
        Unknown30065(0)
        Unknown11091(10)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(-9500)
        AirPushbackY(41000)
        Unknown9310(1)
        Unknown9016(1)
        AirUntechableTime(80)
        Unknown11064(1)
        Hitstop(0)
        Unknown30068(1)
        Unknown13045(0)
        Unknown11072(1, -9000, 0)
        sendToLabelUpon(2, 1)
        Unknown14083(0)

        def upon_78():
            enterState('AirAssaultEx_catch2')
            Hitstop(0)
            Unknown13024(0)
            Unknown11069('AirAssaultEx_catch2')
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
        Unknown48('190000000200000034000000160000000200000025000000')
    sprite('Action_280_00', 3)	# 1-3
    if SLOT_52:
        Unknown5000(17, 0)
    else:
        Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 8)	# 4-11
    sprite('Action_280_02', 4)	# 12-15	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(-8000)
    physicsYImpulse(42000)
    setGravity(2500)
    sprite('Action_280_03', 4)	# 16-19
    sprite('Action_280_04', 3)	# 20-22
    sprite('Action_280_05', 2)	# 23-24
    sprite('Action_280_06', 2)	# 25-26
    label(0)
    sprite('Action_280_07', 3)	# 27-29
    sprite('Action_280_08', 3)	# 30-32
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 33-35
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 36-40
    sprite('Action_280_11', 3)	# 41-43
    loopRest()

@State
def AirAssaultEx_catch2():

    def upon_IMMEDIATE():
        Unknown17011('AirAssaultEx_Exe2', 2, 1, 0)
        Unknown11023(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        Unknown30065(0)
        Unknown11091(10)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown30068(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown11108('03000000')
        Unknown11069('AirAssaultEx_Exe2')
        Unknown11064(1)
        Unknown11023(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('Action_280_03', 4)	# 1-4
    sprite('Action_280_04', 3)	# 5-7
    sprite('Action_280_05', 2)	# 8-9
    sprite('Action_280_06', 2)	# 10-11
    sprite('Action_282_07', 2)	# 12-13
    Unknown2005()
    sprite('Action_282_08', 2)	# 14-15
    sprite('Action_282_09', 3)	# 16-18	 **attackbox here**
    sprite('Action_280_07', 3)	# 19-21
    setInvincible(0)
    sprite('Action_280_08', 3)	# 22-24
    label(0)
    sprite('Action_280_07', 3)	# 25-27
    sprite('Action_280_08', 3)	# 28-30
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 31-33
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 34-38
    sprite('Action_280_11', 3)	# 39-41

@State
def AirAssaultEx_Exe2():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(2500)
        AttackP2(100)
        Unknown30065(0)
        Unknown11091(10)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(900)
        AirPushbackY(42000)
        YImpluseBeforeWallbounce(2600)
        Unknown9310(1)
        Unknown9016(1)
        AirUntechableTime(80)
        Hitstop(2)
        sendToLabelUpon(2, 1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('Action_280_00ex01', 3)	# 1-3
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 5)	# 4-8
    sprite('Action_280_02', 4)	# 9-12	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(-9000)
    physicsYImpulse(36000)
    setGravity(2500)
    sprite('Action_280_03', 2)	# 13-14
    Unknown14083(1)
    Unknown13045(1)
    sprite('Action_280_04', 2)	# 15-16
    sprite('Action_280_05', 2)	# 17-18
    sprite('Action_280_06', 4)	# 19-22
    label(0)
    sprite('Action_280_07', 3)	# 23-25
    sprite('Action_280_08', 3)	# 26-28
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 5)	# 29-33
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 10)	# 34-43
    sprite('Action_280_11', 5)	# 44-48

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(100)
        AttackP1(80)
        AttackP2(60)
        Unknown9154(25)
        Hitstop(4)
        PushbackX(4900)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown9016(1)
        Unknown13024(0)
        Unknown11072(1, 18000, 0)
        Unknown11069('UltimateRush_Exe1')
        Unknown2073(1)

        def upon_80():
            clearUponHandler(3)
            clearUponHandler(78)
            clearUponHandler(80)
            sendToLabel(5)

        def upon_78():
            clearUponHandler(3)
            clearUponHandler(78)
            clearUponHandler(80)
            enterState('UltimateRush_Exe1')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)

        def upon_3():
            if (SLOT_19 <= 250000):
                Unknown2038(1)
            if SLOT_51:
                if SLOT_2:
                    setInvincible(0)
                    sendToLabel(0)
    sprite('Action_154_00', 64)	# 1-64
    Unknown2036(64, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown1084(1)
    setInvincible(1)
    tag_voice(1, 'use250_0', 'use250_1', '', '')
    sprite('Action_154_01', 4)	# 65-68
    sprite('Action_154_02', 4)	# 69-72
    sprite('Action_154_03ex01', 2)	# 73-74	 **attackbox here**
    physicsXImpulse(100000)
    sprite('Action_154_04', 2)	# 75-76	 **attackbox here**
    sprite('Action_154_05', 2)	# 77-78	 **attackbox here**
    sprite('Action_154_06', 2)	# 79-80	 **attackbox here**
    SLOT_51 = 1
    sprite('Action_154_07', 2)	# 81-82	 **attackbox here**
    sprite('Action_154_08', 2)	# 83-84	 **attackbox here**
    sprite('Action_154_09', 2)	# 85-86	 **attackbox here**
    setInvincible(0)
    sprite('Action_154_10', 2)	# 87-88	 **attackbox here**
    sprite('Action_154_11', 2)	# 89-90	 **attackbox here**
    sprite('Action_154_03', 2)	# 91-92	 **attackbox here**
    sprite('Action_154_04', 2)	# 93-94	 **attackbox here**
    sprite('Action_154_05', 2)	# 95-96	 **attackbox here**
    sprite('Action_154_06', 2)	# 97-98	 **attackbox here**
    sprite('Action_154_07', 2)	# 99-100	 **attackbox here**
    sprite('Action_154_08', 2)	# 101-102	 **attackbox here**
    sprite('Action_154_09', 2)	# 103-104	 **attackbox here**
    sprite('Action_154_10', 2)	# 105-106	 **attackbox here**
    sprite('Action_154_11', 2)	# 107-108	 **attackbox here**
    label(0)
    sprite('Action_154_12', 6)	# 109-114
    clearUponHandler(3)
    physicsXImpulse(20000)
    Unknown1028(-2000)
    sprite('Action_154_12', 9)	# 115-123
    Unknown1084(1)
    sprite('Action_154_13', 9)	# 124-132
    loopRest()
    ExitState()
    label(5)
    sprite('Action_155_00', 4)	# 133-136
    setInvincible(0)
    Unknown1084(1)
    physicsXImpulse(10000)
    sprite('Action_155_01', 2)	# 137-138	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    Unknown13024(1)
    Unknown2073(0)
    sprite('Action_155_02', 2)	# 139-140	 **attackbox here**
    sprite('Action_155_03', 2)	# 141-142
    sprite('Action_155_04', 2)	# 143-144
    sprite('Action_155_05', 1)	# 145-145
    sprite('Action_155_06', 5)	# 146-150	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    sprite('Action_155_07', 3)	# 151-153
    sprite('Action_155_08', 4)	# 154-157
    sprite('Action_155_09', 4)	# 158-161	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk2B', 100)
    sprite('Action_155_10', 5)	# 162-166
    sprite('Action_155_11', 3)	# 167-169
    sprite('Action_155_12', 2)	# 170-171
    sprite('Action_155_13', 4)	# 172-175	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_3rd', 100)
    sprite('Action_155_14', 7)	# 176-182
    sprite('Action_155_15', 4)	# 183-186
    physicsXImpulse(25000)
    sprite('Action_155_16', 2)	# 187-188
    sprite('Action_155_17', 6)	# 189-194	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5B_3rd_Kick', 100)
    Unknown1084(1)
    Hitstop(13)
    PushbackX(19800)
    AirPushbackX(6500)
    AirPushbackY(31500)
    Unknown9016(0)
    GroundedHitstunAnimation(13)
    sprite('Action_155_18', 6)	# 195-200
    sprite('Action_155_19', 7)	# 201-207
    sprite('Action_155_20', 4)	# 208-211
    sprite('Action_155_21', 5)	# 212-216
    sprite('Action_155_22', 6)	# 217-222
    sprite('Action_155_23', 6)	# 223-228
    sprite('Action_155_24', 6)	# 229-234

@State
def UltimateRush_Exe1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(262)
        AttackP1(48)
        AttackP2(100)
        AirPushbackX(3000)
        AirPushbackY(3500)
        YImpluseBeforeWallbounce(350)
        AirUntechableTime(90)
        Unknown9154(90)
        Unknown9310(1)
        Hitstop(0)
        PushbackX(5500)
        Unknown11091(8)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11057(600)
        Unknown11023(1)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        Unknown13024(0)
        Unknown23027()
        setInvincible(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown3025(-1, 1)
    sprite('Action_156_00', 4)	# 1-4
    Unknown1045(15000)
    Unknown1084(1)
    GFX_0('UltimateRush_Camera', 100)
    Unknown38(9, 1)
    sprite('Action_156_01', 3)	# 5-7	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A', 100)
    sprite('Action_156_02', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_03', 4)	# 11-14
    sprite('Action_156_04', 3)	# 15-17
    sprite('Action_156_05', 5)	# 18-22
    sprite('Action_156_06', 6)	# 23-28	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    sprite('Action_156_07', 5)	# 29-33	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_08', 3)	# 34-36
    sprite('Action_156_09', 3)	# 37-39	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_10', 7)	# 40-46	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_11', 2)	# 47-48
    sprite('Action_156_12', 3)	# 49-51
    sprite('Action_156_13', 3)	# 52-54
    teleportRelativeX(50000)
    physicsXImpulse(30000)
    Unknown1028(-5000)
    sprite('Action_156_14', 2)	# 55-56
    sprite('Action_156_15', 1)	# 57-57	 **attackbox here**
    RefreshMultihit()
    Unknown9016(1)
    GFX_0('EffNmlAtk5A_3rd', 100)
    GroundedHitstunAnimation(4)
    AirHitstunAnimation(4)
    sprite('Action_156_16', 1)	# 58-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_17', 1)	# 59-59
    Unknown1084(1)
    physicsXImpulse(25000)
    PushbackX(2500)
    sprite('Action_156_18', 2)	# 60-61
    sprite('Action_156_19', 3)	# 62-64	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5B', 100)
    Unknown1084(1)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_20', 3)	# 65-67	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_21', 2)	# 68-69
    sprite('Action_156_22', 1)	# 70-70
    sprite('Action_156_23', 2)	# 71-72
    sprite('Action_156_24', 2)	# 73-74	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A', 100)
    GroundedHitstunAnimation(4)
    AirHitstunAnimation(4)
    sprite('Action_156_25', 2)	# 75-76	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_26', 2)	# 77-78
    sprite('Action_156_27', 1)	# 79-79
    sprite('Action_156_28', 1)	# 80-80
    sprite('Action_156_29', 3)	# 81-83	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    sprite('Action_156_30', 2)	# 84-85	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_31', 2)	# 86-87
    sprite('Action_156_32', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk2B', 100)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    sprite('Action_156_33', 3)	# 91-93	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_34', 2)	# 94-95
    sprite('Action_156_35', 2)	# 96-97
    sprite('Action_156_36', 1)	# 98-98
    sprite('Action_156_37', 2)	# 99-100
    sprite('Action_156_38', 1)	# 101-101
    sprite('Action_156_39', 1)	# 102-102
    sprite('Action_156_40', 2)	# 103-104	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_41', 2)	# 105-106	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_42', 1)	# 107-107
    sprite('Action_156_43', 2)	# 108-109	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk2B', 100)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    sprite('Action_156_44', 6)	# 110-115	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_45', 2)	# 116-117
    Unknown1084(1)
    physicsXImpulse(40000)
    PushbackX(2500)
    sprite('Action_156_46', 1)	# 118-118
    sprite('Action_156_47', 2)	# 119-120	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5B', 100)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_48', 3)	# 121-123	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_49', 2)	# 124-125
    physicsXImpulse(25000)
    sprite('Action_156_50', 1)	# 126-126
    tag_voice(0, 'use251_0', 'use251_1', '', '')
    sprite('Action_156_51', 2)	# 127-128	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    Unknown9016(0)
    Hitstop(13)
    AirUntechableTime(90)
    PushbackX(19800)
    AirPushbackX(3500)
    AirPushbackY(21500)
    YImpluseBeforeWallbounce(800)
    Unknown9016(0)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    Unknown11069('UltimateRush_AtkDmy')
    sprite('Action_156_52', 10)	# 129-138
    Unknown3025(-16777216, 10)
    sprite('Action_156_53', 10)	# 139-148	 **attackbox here**
    Unknown3026(-16777216)
    Unknown3004(-50)
    sprite('Action_156_54', 1)	# 149-149	 **attackbox here**
    enterState('UltimateRush_Exe2')

@State
def UltimateRush_Exe2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(2400)
        Unknown11091(27)
        AttackP1(48)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(90)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        Unknown30048(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown23027()
        setInvincible(1)
        Unknown3038(1)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 1000):
                GFX_0('UltimateRush_FinishShadow', 100)
                sendToLabel(10)

        def upon_STATE_END():
            Unknown3038(0)
            Unknown3001(255)
            Unknown3004(0)

        def upon_45():
            if (not SLOT_158):
                Unknown23029(9, 1001, 0)
    sprite('keep', 300)	# 1-300
    GFX_0('UltimateRush_Shadow', 100)
    GFX_0('UltimateRush_AtkDmy', 100)
    ExitState()
    label(10)
    sprite('Action_160_00ex01', 3)	# 301-303	 **attackbox here**
    RefreshMultihit()
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(250000)
    physicsXImpulse(-50000)
    physicsYImpulse(-50000)
    Unknown3038(0)
    Unknown3001(0)
    SFX_3('SE_BigBomb')
    tag_voice(0, 'use252_0', 'use252_1', '', '')
    sprite('Action_160_00ex01', 2)	# 304-305	 **attackbox here**
    Unknown3004(96)
    sprite('Action_160_01ex01', 5)	# 306-310
    Unknown1084(1)
    sprite('Action_160_02ex01', 5)	# 311-315
    Unknown13024(1)
    sprite('Action_160_03ex01', 5)	# 316-320
    sprite('Action_160_04ex01', 5)	# 321-325
    sprite('Action_160_05ex01', 15)	# 326-340
    sprite('Action_160_06ex01', 7)	# 341-347
    sprite('Action_160_07ex01', 7)	# 348-354
    Unknown23029(9, 1001, 0)
    sprite('Action_160_08ex01', 7)	# 355-361
    sprite('Action_160_09ex01', 5)	# 362-366

@State
def UltimateRushOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(100)
        AttackP1(80)
        AttackP2(60)
        Unknown9154(25)
        Hitstop(4)
        PushbackX(4900)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        Unknown13024(0)
        Unknown11072(1, 18000, 0)
        Unknown11069('UltimateRushOD_Exe1')
        Unknown2073(1)

        def upon_80():
            clearUponHandler(3)
            clearUponHandler(78)
            clearUponHandler(80)
            sendToLabel(5)

        def upon_78():
            clearUponHandler(3)
            clearUponHandler(78)
            clearUponHandler(80)
            enterState('UltimateRushOD_Exe1')

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)

        def upon_3():
            if (SLOT_19 <= 250000):
                Unknown2038(1)
            if SLOT_51:
                if SLOT_2:
                    setInvincible(0)
                    sendToLabel(0)
    sprite('Action_154_00', 64)	# 1-64
    Unknown2036(64, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    Unknown1084(1)
    setInvincible(1)
    tag_voice(1, 'use250_0', 'use250_1', '', '')
    sprite('Action_154_01', 4)	# 65-68
    sprite('Action_154_02', 4)	# 69-72
    sprite('Action_154_03ex01', 2)	# 73-74	 **attackbox here**
    physicsXImpulse(100000)
    sprite('Action_154_04', 2)	# 75-76	 **attackbox here**
    sprite('Action_154_05', 2)	# 77-78	 **attackbox here**
    sprite('Action_154_06', 2)	# 79-80	 **attackbox here**
    SLOT_51 = 1
    sprite('Action_154_07', 2)	# 81-82	 **attackbox here**
    sprite('Action_154_08', 2)	# 83-84	 **attackbox here**
    sprite('Action_154_09', 2)	# 85-86	 **attackbox here**
    setInvincible(0)
    sprite('Action_154_10', 2)	# 87-88	 **attackbox here**
    sprite('Action_154_11', 2)	# 89-90	 **attackbox here**
    sprite('Action_154_03', 2)	# 91-92	 **attackbox here**
    sprite('Action_154_04', 2)	# 93-94	 **attackbox here**
    sprite('Action_154_05', 2)	# 95-96	 **attackbox here**
    sprite('Action_154_06', 2)	# 97-98	 **attackbox here**
    sprite('Action_154_07', 2)	# 99-100	 **attackbox here**
    sprite('Action_154_08', 2)	# 101-102	 **attackbox here**
    sprite('Action_154_09', 2)	# 103-104	 **attackbox here**
    sprite('Action_154_10', 2)	# 105-106	 **attackbox here**
    sprite('Action_154_11', 2)	# 107-108	 **attackbox here**
    label(0)
    sprite('Action_154_12', 6)	# 109-114
    clearUponHandler(3)
    physicsXImpulse(20000)
    Unknown1028(-2000)
    sprite('Action_154_12', 9)	# 115-123
    Unknown1084(1)
    sprite('Action_154_13', 9)	# 124-132
    loopRest()
    ExitState()
    label(5)
    sprite('Action_155_00', 4)	# 133-136
    setInvincible(0)
    Unknown1084(1)
    physicsXImpulse(10000)
    sprite('Action_155_01', 2)	# 137-138	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    Unknown13024(1)
    Unknown2073(0)
    sprite('Action_155_02', 2)	# 139-140	 **attackbox here**
    sprite('Action_155_03', 2)	# 141-142
    sprite('Action_155_04', 2)	# 143-144
    sprite('Action_155_05', 1)	# 145-145
    sprite('Action_155_06', 5)	# 146-150	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    sprite('Action_155_07', 3)	# 151-153
    sprite('Action_155_08', 4)	# 154-157
    sprite('Action_155_09', 4)	# 158-161	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk2B', 100)
    sprite('Action_155_10', 5)	# 162-166
    sprite('Action_155_11', 3)	# 167-169
    sprite('Action_155_12', 2)	# 170-171
    sprite('Action_155_13', 4)	# 172-175	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_3rd', 100)
    sprite('Action_155_14', 7)	# 176-182
    sprite('Action_155_15', 4)	# 183-186
    physicsXImpulse(25000)
    sprite('Action_155_16', 2)	# 187-188
    sprite('Action_155_17', 6)	# 189-194	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5B_3rd_Kick', 100)
    Unknown1084(1)
    Hitstop(13)
    PushbackX(19800)
    AirPushbackX(6500)
    AirPushbackY(31500)
    Unknown9016(0)
    GroundedHitstunAnimation(13)
    sprite('Action_155_18', 6)	# 195-200
    sprite('Action_155_19', 7)	# 201-207
    sprite('Action_155_20', 4)	# 208-211
    sprite('Action_155_21', 5)	# 212-216
    sprite('Action_155_22', 6)	# 217-222
    sprite('Action_155_23', 6)	# 223-228
    sprite('Action_155_24', 6)	# 229-234

@State
def UltimateRushOD_Exe1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(262)
        AttackP1(48)
        AttackP2(100)
        AirPushbackX(3000)
        AirPushbackY(3500)
        YImpluseBeforeWallbounce(350)
        AirUntechableTime(90)
        Unknown9154(90)
        Unknown9310(1)
        Hitstop(0)
        PushbackX(5500)
        Unknown11091(8)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11057(600)
        Unknown11023(1)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        Unknown13024(0)
        Unknown23027()
        setInvincible(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown3025(-1, 1)
    sprite('Action_156_00', 4)	# 1-4
    Unknown1045(15000)
    Unknown1084(1)
    GFX_0('UltimateRush_Camera', 100)
    Unknown38(9, 1)
    sprite('Action_156_01', 3)	# 5-7	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A', 100)
    sprite('Action_156_02', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_03', 4)	# 11-14
    sprite('Action_156_04', 3)	# 15-17
    sprite('Action_156_05', 5)	# 18-22
    sprite('Action_156_06', 6)	# 23-28	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    sprite('Action_156_07', 5)	# 29-33	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_08', 3)	# 34-36
    sprite('Action_156_09', 3)	# 37-39	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_10', 7)	# 40-46	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_11', 2)	# 47-48
    sprite('Action_156_12', 3)	# 49-51
    sprite('Action_156_13', 3)	# 52-54
    teleportRelativeX(50000)
    physicsXImpulse(30000)
    Unknown1028(-5000)
    sprite('Action_156_14', 2)	# 55-56
    sprite('Action_156_15', 1)	# 57-57	 **attackbox here**
    RefreshMultihit()
    Unknown9016(1)
    GFX_0('EffNmlAtk5A_3rd', 100)
    GroundedHitstunAnimation(4)
    AirHitstunAnimation(4)
    sprite('Action_156_16', 1)	# 58-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_17', 1)	# 59-59
    Unknown1084(1)
    physicsXImpulse(25000)
    PushbackX(2500)
    sprite('Action_156_18', 2)	# 60-61
    sprite('Action_156_19', 3)	# 62-64	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5B', 100)
    Unknown1084(1)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_20', 3)	# 65-67	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_21', 2)	# 68-69
    sprite('Action_156_22', 1)	# 70-70
    sprite('Action_156_23', 2)	# 71-72
    sprite('Action_156_24', 2)	# 73-74	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A', 100)
    GroundedHitstunAnimation(4)
    AirHitstunAnimation(4)
    sprite('Action_156_25', 2)	# 75-76	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_26', 2)	# 77-78
    sprite('Action_156_27', 1)	# 79-79
    sprite('Action_156_28', 1)	# 80-80
    sprite('Action_156_29', 3)	# 81-83	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    sprite('Action_156_30', 2)	# 84-85	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_31', 2)	# 86-87
    sprite('Action_156_32', 3)	# 88-90	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk2B', 100)
    GroundedHitstunAnimation(11)
    AirHitstunAnimation(11)
    sprite('Action_156_33', 3)	# 91-93	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_34', 2)	# 94-95
    sprite('Action_156_35', 2)	# 96-97
    sprite('Action_156_36', 1)	# 98-98
    sprite('Action_156_37', 2)	# 99-100
    sprite('Action_156_38', 1)	# 101-101
    sprite('Action_156_39', 1)	# 102-102
    sprite('Action_156_40', 2)	# 103-104	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5A_2nd', 100)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_41', 2)	# 105-106	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_42', 1)	# 107-107
    sprite('Action_156_43', 2)	# 108-109	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk2B', 100)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    sprite('Action_156_44', 6)	# 110-115	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_45', 2)	# 116-117
    Unknown1084(1)
    physicsXImpulse(40000)
    PushbackX(2500)
    sprite('Action_156_46', 1)	# 118-118
    sprite('Action_156_47', 2)	# 119-120	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5B', 100)
    GroundedHitstunAnimation(5)
    AirHitstunAnimation(5)
    sprite('Action_156_48', 3)	# 121-123	 **attackbox here**
    RefreshMultihit()
    sprite('Action_156_49', 2)	# 124-125
    physicsXImpulse(25000)
    sprite('Action_156_50', 1)	# 126-126
    tag_voice(0, 'use251_0', 'use251_1', '', '')
    sprite('Action_156_51', 2)	# 127-128	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    Unknown9016(0)
    Hitstop(13)
    AirUntechableTime(90)
    PushbackX(19800)
    AirPushbackX(3500)
    AirPushbackY(21500)
    YImpluseBeforeWallbounce(800)
    Unknown9016(0)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    Unknown11069('UltimateRushOD_AtkDmy')
    sprite('Action_156_52', 10)	# 129-138
    Unknown3025(-16777216, 10)
    sprite('Action_156_53', 10)	# 139-148	 **attackbox here**
    Unknown3026(-16777216)
    Unknown3004(-50)
    sprite('Action_156_54', 1)	# 149-149	 **attackbox here**
    enterState('UltimateRushOD_Exe2')

@State
def UltimateRushOD_Exe2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(3000)
        Unknown11091(19)
        AttackP1(48)
        AttackP2(100)
        Hitstop(0)
        AirUntechableTime(90)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        Unknown30048(1)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        Unknown23027()
        setInvincible(1)
        Unknown3038(1)
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 1000):
                GFX_0('UltimateRushOD_FinishShadow', 100)
                sendToLabel(10)

        def upon_STATE_END():
            Unknown3038(0)
            Unknown3001(255)
            Unknown3004(0)

        def upon_45():
            if (not SLOT_158):
                Unknown23029(9, 1001, 0)
    sprite('Action_160_00ex01', 300)	# 1-300	 **attackbox here**
    GFX_0('UltimateRushOD_Shadow', 100)
    GFX_0('UltimateRushOD_AtkDmy', 100)
    ExitState()
    label(10)
    sprite('Action_160_00ex01', 3)	# 301-303	 **attackbox here**
    RefreshMultihit()
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(250000)
    physicsXImpulse(-50000)
    physicsYImpulse(-50000)
    Unknown3038(0)
    Unknown3001(0)
    SFX_3('SE_BigBomb')
    tag_voice(0, 'use252_0', 'use252_1', '', '')
    sprite('Action_160_00ex01', 2)	# 304-305	 **attackbox here**
    Unknown3004(96)
    sprite('Action_160_01ex01', 5)	# 306-310
    Unknown1084(1)
    sprite('Action_160_02ex01', 5)	# 311-315
    Unknown13024(1)
    sprite('Action_160_03ex01', 5)	# 316-320
    sprite('Action_160_04ex01', 5)	# 321-325
    sprite('Action_160_05ex01', 15)	# 326-340
    sprite('Action_160_06ex01', 7)	# 341-347
    sprite('Action_160_07ex01', 7)	# 348-354
    Unknown23029(9, 1001, 0)
    sprite('Action_160_08ex01', 7)	# 355-361
    sprite('Action_160_09ex01', 5)	# 362-366

@State
def UltimateThrow():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowExe', 3, 0, 0)
        Unknown23055('')
        Unknown11054(100000)
        Unknown11032('20bf020001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(50)
        Unknown11002(-1)
        Unknown30061(0)

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
                Unknown11054(320000)
                Unknown11032('80ee360001000000ffffffffffffffff')
            else:
                Unknown11045(1)
                Unknown11054(100000)
                Unknown11032('20bf020001000000ffffffffffffffff')
    sprite('Action_262_00', 5)	# 1-5
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 2)	# 11-12
    sprite('Action_262_02', 3)	# 13-15
    Unknown2036(36, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('Action_262_03', 5)	# 16-20
    sprite('Action_262_04', 5)	# 21-25
    sprite('Action_262_03', 5)	# 26-30
    sprite('Action_262_04', 5)	# 31-35
    sprite('Action_262_05', 5)	# 36-40
    sprite('Action_262_06', 5)	# 41-45
    sprite('Action_239_00', 3)	# 46-48
    sprite('Action_239_01', 1)	# 49-49	 **attackbox here**
    sprite('Action_239_02', 1)	# 50-50
    sprite('Action_239_03', 2)	# 51-52
    setInvincible(0)
    sprite('Action_239_04', 9)	# 53-61
    SFX_3('SE042')
    SFX_4('use154')
    GFX_0('Shot_Zanzo', 0)
    Unknown36(1)
    Unknown1072(-35000)
    Unknown35()
    sprite('Action_239_05', 20)	# 62-81
    sprite('Action_239_06', 7)	# 82-88
    sprite('Action_239_07', 7)	# 89-95

@State
def UltimateThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(10)
        Unknown11064(1)
        AttackP2(100)
        Hitstop(0)
        AirPushbackX(-9500)
        AirPushbackY(45000)
        Unknown11057(500)
        PushbackX(0)
        Unknown9016(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown30048(1)
        sendToLabelUpon(2, 1)
        Unknown30068(1)
        Unknown14083(0)
        Unknown13024(0)

        def upon_78():
            enterState('UltimateThrow_Catch1')
            Unknown11069('UltimateThrow_Catch1')
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_245_00', 3)	# 1-3
    tag_voic2e(1, 'use253_0', 'use253_1', '', '')
    Unknown38(11, 1)
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('Action_245_01', 4)	# 4-7
    GFX_0('UltimateThrow_Camera', 100)
    Unknown5000(17, 0)
    sprite('Action_45_02', 4)	# 8-11
    Unknown5000(17, 0)
    sprite('Action_245_03', 3)	# 12-14
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    physicsXImpulse(10000)
    Unknown1028(-1000)
    Unknown5004()
    Unknown2018(0, 80)
    sprite('Action_245_04', 3)	# 15-17
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_05', 3)	# 18-20
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_06', 6)	# 21-26
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_245_07', 6)	# 27-32
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_08', 5)	# 33-37
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_09', 4)	# 38-41
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_10', 17)	# 42-58
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_11', 5)	# 59-63	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(-8000)
    physicsYImpulse(55000)
    setGravity(4500)
    sprite('Action_245_12', 4)	# 64-67
    sprite('Action_245_13', 2)	# 68-69
    sprite('Action_245_14', 2)	# 70-71
    sprite('Action_245_15', 2)	# 72-73
    label(0)
    sprite('Action_245_16', 3)	# 74-76
    sprite('Action_245_17', 3)	# 77-79
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)	# 80-84
    Unknown1084(1)
    sprite('Action_245_19', 5)	# 85-89
    sprite('Action_245_20', 4)	# 90-93

@State
def UltimateThrow_Catch1():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrow_Exe2', 3, 1, 0)
        Unknown23056('')
        Unknown11023(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        Unknown11064(1)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown30068(1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown11108('03000000')
        Unknown11023(1)
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_245_12', 4)	# 1-4
    sprite('Action_245_13', 2)	# 5-6
    sprite('Action_245_14', 2)	# 7-8
    sprite('Action_245_15', 2)	# 9-10
    sprite('Action_282_08', 2)	# 11-12
    sprite('Action_282_09', 3)	# 13-15	 **attackbox here**
    tag_voice(0, 'use254_0', '', '', '')
    label(0)
    sprite('Action_280_07', 3)	# 16-18
    sprite('Action_280_08', 3)	# 19-21
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 22-24
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 25-29
    sprite('Action_280_11', 3)	# 30-32

@State
def UltimateThrow_Exe2():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(10)
        Unknown11064(1)
        AttackP2(100)
        Hitstop(0)
        AirPushbackX(12500)
        AirPushbackY(15000)
        Unknown11057(500)
        PushbackX(0)
        Unknown9016(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown30048(1)
        Unknown30068(1)
        Unknown13024(0)
        sendToLabelUpon(2, 1)

        def upon_78():
            enterState('UltimateThrow_Catch2')
            Unknown11069('UltimateThrow_Catch2')
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_280_00ex01', 1)	# 1-1
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 1)	# 2-2
    sprite('Action_280_02', 4)	# 3-6	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(8000)
    physicsYImpulse(28000)
    setGravity(4500)
    sprite('Action_280_03', 2)	# 7-8
    Unknown2005()
    sprite('Action_245_13', 2)	# 9-10
    sprite('Action_245_14', 2)	# 11-12
    sprite('Action_245_15', 2)	# 13-14
    label(0)
    sprite('Action_245_16', 3)	# 15-17
    sprite('Action_245_17', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)	# 21-25
    Unknown1084(1)
    sprite('Action_245_19', 5)	# 26-30
    sprite('Action_245_20', 4)	# 31-34

@State
def UltimateThrow_Catch2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrow_Exe3', 3, 1, 0)
        Unknown23056('')
        Unknown11023(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        Unknown11064(1)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown30068(1)
        Unknown13024(0)
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_245_12', 4)	# 1-4
    Unknown2005()
    sprite('Action_245_13', 2)	# 5-6
    sprite('Action_245_14', 2)	# 7-8
    sprite('Action_245_15', 2)	# 9-10
    sprite('Action_282_08', 2)	# 11-12
    sprite('Action_282_09', 3)	# 13-15	 **attackbox here**
    label(0)
    sprite('Action_280_07', 3)	# 16-18
    sprite('Action_280_08', 3)	# 19-21
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 22-24
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 25-29
    sprite('Action_280_11', 3)	# 30-32

@State
def UltimateThrow_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(10)
        Unknown11064(1)
        AttackP2(100)
        Hitstop(0)
        AirPushbackX(-100)
        AirPushbackY(9000)
        YImpluseBeforeWallbounce(150)
        AirUntechableTime(150)
        PushbackX(0)
        Unknown11057(500)
        Unknown9016(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown30048(1)
        Unknown30068(1)
        Unknown13024(0)
        Unknown2034(0)
        Unknown2053(0)
        Unknown11069('UltimateThrow_FinishAtkDmy')

        def upon_45():
            if (not SLOT_158):
                clearUponHandler(45)
                Unknown26('UltimateThrow_Camera')

        def upon_STATE_END():
            Unknown26('UltimateThrow_Camera')
            Unknown3001(255)
            Unknown3004(0)
            Unknown3038(0)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_280_00ex01', 1)	# 1-1
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 1)	# 2-2
    sprite('Action_280_02', 4)	# 3-6	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsYImpulse(2500)
    physicsXImpulse(12500)
    sprite('Action_278_00', 4)	# 7-10
    Unknown1007(-125000)
    Unknown2005()
    Unknown13045(1)
    Unknown3004(-40)
    sprite('Action_278_01', 5)	# 11-15
    sprite('Action_278_02', 5)	# 16-20
    sprite('Action_364_07ex01', 20)	# 21-40	 **attackbox here**
    Unknown1084(1)
    setGravity(0)
    Unknown3038(1)
    sprite('Action_220_01', 12)	# 41-52
    GFX_0('UltimateThrow_FinishBlade', 100)
    Unknown1086(22)
    teleportRelativeX(-55000)
    Unknown13(11)
    Unknown3038(0)
    tag_voice(0, 'use255_0', 'use255_1', '', '')
    sprite('Action_220_01', 32767)	# 53-32819
    physicsYImpulse(-80000)
    Unknown3001(255)
    Unknown3004(0)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_220_02', 3)	# 32820-32822
    sprite('Action_220_03', 20)	# 32823-32842
    Unknown13024(1)
    sprite('Action_220_04', 6)	# 32843-32848
    sprite('Action_220_05', 4)	# 32849-32852

@State
def UltimateThrowOD():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe', 3, 0, 0)
        Unknown23055('')
        Unknown11054(100000)
        Unknown11032('20bf020001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(50)
        Unknown11002(-1)
        Unknown30061(0)

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
                Unknown11054(320000)
                Unknown11032('80ee360001000000ffffffffffffffff')
            else:
                Unknown11045(1)
                Unknown11054(100000)
                Unknown11032('20bf020001000000ffffffffffffffff')
    sprite('Action_262_00', 5)	# 1-5
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 2)	# 11-12
    sprite('Action_262_02', 3)	# 13-15
    Unknown2036(36, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('Action_262_03', 5)	# 16-20
    sprite('Action_262_04', 5)	# 21-25
    sprite('Action_262_03', 5)	# 26-30
    sprite('Action_262_04', 5)	# 31-35
    sprite('Action_262_05', 5)	# 36-40
    sprite('Action_262_06', 5)	# 41-45
    sprite('Action_239_00', 3)	# 46-48
    sprite('Action_239_01', 1)	# 49-49	 **attackbox here**
    sprite('Action_239_02', 1)	# 50-50
    sprite('Action_239_03', 2)	# 51-52
    setInvincible(0)
    sprite('Action_239_04', 9)	# 53-61
    SFX_3('SE042')
    SFX_4('use154')
    GFX_0('Shot_Zanzo', 0)
    Unknown36(1)
    Unknown1072(-35000)
    Unknown35()
    sprite('Action_239_05', 20)	# 62-81
    sprite('Action_239_06', 7)	# 82-88
    sprite('Action_239_07', 7)	# 89-95

@State
def UltimateThrowODExe():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(10)
        Unknown11064(1)
        AttackP2(100)
        Hitstop(0)
        AirPushbackX(-9500)
        AirPushbackY(25000)
        Unknown11057(500)
        PushbackX(0)
        Unknown9016(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown30048(1)
        Unknown30068(1)
        Unknown14083(0)
        Unknown13024(0)
        sendToLabelUpon(2, 1)

        def upon_78():
            enterState('UltimateThrowOD_Catch1')
            Unknown11069('UltimateThrowOD_Catch1')
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_245_00', 3)	# 1-3
    tag_voice(1, 'use253_0', 'use253_1', '', '')
    Unknown38(11, 1)
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('Action_245_01', 4)	# 4-7
    GFX_0('UltimateThrow_Camera', 100)
    Unknown5000(17, 0)
    sprite('Action_245_02', 4)	# 8-11
    Unknown5000(17, 0)
    sprite('Action_245_03', 3)	# 12-14
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    physicsXImpulse(10000)
    Unknown1028(-1000)
    Unknown5004()
    Unknown2018(0, 80)
    sprite('Action_245_04', 3)	# 15-17
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_05', 3)	# 18-20
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_06', 6)	# 21-26
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_245_07', 6)	# 27-32
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_08', 5)	# 33-37
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_09', 4)	# 38-41
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_10', 17)	# 42-58
    Unknown5001('0000000000000000000000006400000004000000')
    sprite('Action_245_11', 5)	# 59-63	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(-8000)
    physicsYImpulse(28000)
    setGravity(4500)
    sprite('Action_245_12', 4)	# 64-67
    sprite('Action_245_13', 2)	# 68-69
    sprite('Action_245_14', 2)	# 70-71
    sprite('Action_245_15', 2)	# 72-73
    label(0)
    sprite('Action_245_16', 3)	# 74-76
    sprite('Action_245_17', 3)	# 77-79
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)	# 80-84
    Unknown1084(1)
    sprite('Action_245_19', 5)	# 85-89
    sprite('Action_245_20', 4)	# 90-93

@State
def UltimateThrowOD_Catch1():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowOD_Exe2', 2, 1, 0)
        Unknown23056('')
        Unknown11023(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        Unknown11064(1)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown30068(1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_245_12', 4)	# 1-4
    GFX_0('UltimateThrow_MirrorShadow1', 100)
    sprite('Action_245_13', 2)	# 5-6
    sprite('Action_245_14', 2)	# 7-8
    sprite('Action_245_15', 2)	# 9-10
    sprite('Action_282_08', 2)	# 11-12
    sprite('Action_282_09', 3)	# 13-15	 **attackbox here**
    label(0)
    sprite('Action_280_07', 3)	# 16-18
    sprite('Action_280_08', 3)	# 19-21
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 22-24
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 25-29
    sprite('Action_280_11', 3)	# 30-32

@State
def UltimateThrowOD_Exe2():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(10)
        AttackP2(100)
        Unknown11064(1)
        Hitstop(0)
        AirPushbackX(12500)
        AirPushbackY(25000)
        Unknown11057(500)
        PushbackX(0)
        Unknown9016(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown30048(1)
        Unknown30068(1)
        Unknown14083(0)
        sendToLabelUpon(2, 1)

        def upon_78():
            enterState('UltimateThrowOD_Catch2')
            Unknown13024(0)
            Unknown11069('UltimateThrowOD_Catch2')
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_280_00ex01', 1)	# 1-1
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 1)	# 2-2
    sprite('Action_280_02', 4)	# 3-6	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(8000)
    physicsYImpulse(28000)
    setGravity(4500)
    sprite('Action_280_03', 2)	# 7-8
    Unknown2005()
    sprite('Action_245_13', 2)	# 9-10
    sprite('Action_245_14', 2)	# 11-12
    sprite('Action_245_15', 2)	# 13-14
    label(0)
    sprite('Action_245_16', 3)	# 15-17
    sprite('Action_245_17', 3)	# 18-20
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_245_18', 5)	# 21-25
    Unknown1084(1)
    sprite('Action_245_19', 5)	# 26-30
    sprite('Action_245_20', 4)	# 31-34

@State
def UltimateThrowOD_Catch2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowOD_Exe3', 2, 1, 0)
        Unknown23056('')
        Unknown11023(1)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(0)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown30068(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown13045(0)
        Unknown11064(1)
        Unknown11069('UltimateThrowOD_Exe3')
        Unknown2034(0)
        Unknown2053(0)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_245_12', 4)	# 1-4
    Unknown2005()
    GFX_0('UltimateThrow_MirrorShadow2', 100)
    sprite('Action_245_13', 2)	# 5-6
    sprite('Action_245_14', 2)	# 7-8
    sprite('Action_245_15', 2)	# 9-10
    sprite('Action_282_08', 2)	# 11-12
    sprite('Action_282_09', 3)	# 13-15	 **attackbox here**
    label(0)
    sprite('Action_280_07', 3)	# 16-18
    sprite('Action_280_08', 3)	# 19-21
    gotoLabel(0)
    label(1)
    sprite('Action_280_09', 3)	# 22-24
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_280_10', 5)	# 25-29
    sprite('Action_280_11', 3)	# 30-32

@State
def UltimateThrowOD_Exe3():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(10)
        AttackP2(100)
        Unknown11064(1)
        Hitstop(0)
        AirPushbackX(-100)
        AirPushbackY(6000)
        YImpluseBeforeWallbounce(150)
        AirUntechableTime(150)
        PushbackX(0)
        Unknown11057(500)
        Unknown9016(1)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown30048(1)
        Unknown30068(1)
        Unknown13024(0)
        Unknown2034(1)
        Unknown2053(1)
        Unknown11069('UltimateThrowOD_Shot')

        def upon_45():
            if (not SLOT_158):
                clearUponHandler(45)
                Unknown26('UltimateThrow_Camera')

        def upon_STATE_END():
            Unknown26('UltimateThrow_Camera')
            Unknown3001(255)
            Unknown3004(0)
            Unknown3038(0)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_280_00ex01', 1)	# 1-1
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000006400000004000000')
    Unknown1084(1)
    sprite('Action_280_01', 1)	# 2-2
    tag_voice(0, 'use256', '', '', '')
    sprite('Action_280_02', 4)	# 3-6	 **attackbox here**
    GFX_0('EffAirAssalut_GripSlush', 100)
    GFX_0('EffAirAssalut_GripAtkEff', 100)
    physicsXImpulse(18000)
    physicsYImpulse(8000)
    setGravity(1500)
    sprite('Action_280_03', 2)	# 7-8
    Unknown2005()
    GFX_0('UltimateThrow_MirrorShadow3', 100)
    sprite('Action_280_04', 2)	# 9-10
    sprite('Action_280_05', 2)	# 11-12
    sprite('Action_280_06', 4)	# 13-16
    Unknown3004(-15)
    sprite('Action_280_07', 3)	# 17-19
    sprite('Action_280_08', 3)	# 20-22
    sprite('Action_280_06', 100)	# 23-122
    Unknown1084(1)
    setGravity(0)
    Unknown3038(1)
    sprite('Action_220_01', 12)	# 123-134
    GFX_0('UltimateThrow_FinishBlade', 100)
    Unknown1086(22)
    teleportRelativeX(-55000)
    Unknown13(11)
    Unknown3038(0)
    tag_voice(0, 'use255_0', 'use255_1', '', '')
    sprite('Action_220_01', 32767)	# 135-32901
    physicsYImpulse(-80000)
    Unknown3001(255)
    Unknown3004(0)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_220_02', 3)	# 32902-32904
    sprite('Action_220_03', 21)	# 32905-32925
    Unknown13024(1)
    sprite('Action_220_04', 6)	# 32926-32931
    sprite('Action_220_05', 4)	# 32932-32935

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(500)
        PushbackX(19800)
        Hitstop(0)
        Unknown11091(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9016(1)
        AirPushbackX(0)
        AirPushbackY(300)
        YImpluseBeforeWallbounce(0)
        Unknown11056(0)
        AirUntechableTime(999)
        setInvincible(1)
        Unknown11086(1)
        Unknown11058('0100000000000000000000000000000000000000')

        def upon_78():
            Unknown2038(1)
            Unknown11099(1)
            Unknown23029(10, 5000, 0)
            enterState('AstralHeatExe')

        def upon_STATE_END():
            if (not SLOT_2):
                Unknown3001(255)
                Unknown3004(0)
    sprite('Action_261_00', 4)	# 1-4
    Unknown20001(1)
    Unknown2017(0)
    Unknown2036(108, -1, 2)
    Unknown23147()
    Unknown4004('617572610000000000000000000000000000000000000000000000000000000000000000')
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    Unknown38(9, 1)
    SFX_1('use290')
    sprite('Action_261_01', 4)	# 5-8
    sprite('Action_261_02', 4)	# 9-12
    sprite('Action_261_03', 4)	# 13-16
    sprite('Action_261_04', 4)	# 17-20
    sprite('Action_261_05', 4)	# 21-24
    GFX_0('AstralStartCutIn', 100)
    sprite('Action_261_03', 4)	# 25-28
    sprite('Action_261_04', 4)	# 29-32
    sprite('Action_261_05', 4)	# 33-36
    sprite('Action_261_03', 4)	# 37-40
    sprite('Action_261_04', 4)	# 41-44
    sprite('Action_261_05', 4)	# 45-48
    sprite('Action_261_03', 4)	# 49-52
    sprite('Action_261_04', 4)	# 53-56
    sprite('Action_261_05', 4)	# 57-60
    sprite('Action_261_03', 4)	# 61-64
    sprite('Action_261_04', 4)	# 65-68
    sprite('Action_261_05', 4)	# 69-72
    sprite('Action_261_12', 2)	# 73-74
    sprite('Action_261_13', 2)	# 75-76
    sprite('Action_431_00', 4)	# 77-80
    GFX_0('AstralStartCamera', -1)
    physicsXImpulse(-55000)
    physicsYImpulse(25000)
    setGravity(1500)
    sprite('Action_431_01', 4)	# 81-84
    sprite('Action_431_02', 4)	# 85-88
    sendToLabelUpon(7, 10)
    sprite('Action_431_03', 4)	# 89-92
    sprite('Action_431_04', 4)	# 93-96
    sprite('Action_431_05', 4)	# 97-100
    sendToLabelUpon(2, 1)
    label(0)
    sprite('Action_431_06', 3)	# 101-103
    sprite('Action_431_07', 3)	# 104-106
    gotoLabel(0)
    label(1)
    sprite('Action_431_08', 3)	# 107-109
    Unknown13(9)
    Unknown2017(1)
    Unknown20001(0)
    sprite('Action_431_09', 5)	# 110-114
    sprite('Action_431_10', 5)	# 115-119
    sprite('Action_431_11', 4)	# 120-123
    ExitState()
    label(10)
    sprite('Action_431_12', 3)	# 124-126
    clearUponHandler(2)
    clearUponHandler(7)
    Unknown1084(1)
    sprite('Action_431_13', 25)	# 127-151
    sprite('Action_431_13ex01', 8)	# 152-159	 **attackbox here**
    Unknown3004(-90)
    physicsXImpulse(125000)
    physicsYImpulse(-30000)
    GFX_0('AstralBlade_First', 100)
    Unknown38(10, 1)
    sprite('Action_431_13ex01', 32767)	# 160-32926	 **attackbox here**
    sendToLabelUpon(2, 11)
    label(11)
    sprite('Action_278_05', 20)	# 32927-32946	 **attackbox here**
    setInvincible(0)
    StartMultihit()
    Unknown1084(1)
    Unknown1045(25000)
    Unknown3004(20)
    Unknown2017(1)
    sprite('Action_278_06', 6)	# 32947-32952
    sprite('Action_278_08', 5)	# 32953-32957
    Unknown23024(0)
    Unknown3001(255)
    sprite('Action_278_09', 4)	# 32958-32961
    Unknown13(9)
    sprite('Action_278_10', 4)	# 32962-32965
    sprite('Action_278_11', 3)	# 32966-32968

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown2005()
        Unknown3038(1)
        Unknown2017(0)
        Unknown2003(1)
        Unknown30068(1)
        Unknown23088(1, 1)
        Unknown23157(1)
        Unknown23022(1)
        Unknown23084(1)

        def upon_43():
            if (SLOT_48 == 5002):
                sendToLabel(1)
            if (SLOT_48 == 5003):
                sendToLabel(2)
        loopRelated(17, 600)

        def upon_17():
            Unknown3038(0)
            Unknown3001(255)
            Unknown3004(0)
            Unknown13(11)
            Unknown26('AstralBG')
            Unknown26('AstralBlade')
            Unknown26('AstralBlade_First')
            Unknown26('AstralLastBlade')
            sendToLabel(2)
    label(0)
    sprite('keep', 60)	# 1-60
    GFX_0('AstralBlade_Matome', 100)
    GFX_0('AstralExeCamera', 100)
    Unknown38(11, 1)
    Unknown1084(1)
    sprite('keep', 105)	# 61-165
    SFX_1('use291')
    sprite('keep', 32767)	# 166-32932
    SFX_1('use292')
    label(1)
    sprite('keep', 25)	# 32933-32957
    sprite('keep', 20)	# 32958-32977
    Unknown1000(0)
    Unknown13(9)
    GFX_0('AstralFinishCutIn', 100)
    GFX_0('AstralBG', 100)
    Unknown13(9)
    sprite('keep', 32767)	# 32978-65744
    SFX_1('use293')
    label(2)
    sprite('Action_432_00', 5)	# 65745-65749
    Unknown3038(0)
    Unknown2017(1)
    Unknown3001(255)
    Unknown1000(-260000)
    teleportRelativeY(0)
    Unknown36(22)
    Unknown1000(-260000)
    teleportRelativeY(0)
    Unknown3026(-1)
    Unknown35()
    Unknown20006(1)
    Unknown23024(0)
    Unknown13(11)
    Unknown26('AstralBG')
    sprite('Action_432_01', 5)	# 65750-65754
    sprite('Action_432_02', 5)	# 65755-65759
    sprite('Action_432_03', 5)	# 65760-65764
    sprite('Action_432_04', 5)	# 65765-65769
    sprite('Action_432_01', 5)	# 65770-65774
    sprite('Action_432_02', 5)	# 65775-65779
    sprite('Action_432_03', 5)	# 65780-65784
    sprite('Action_432_04', 5)	# 65785-65789
    sprite('Action_432_01', 5)	# 65790-65794
    sprite('Action_432_02', 5)	# 65795-65799
    sprite('Action_432_03', 5)	# 65800-65804
    sprite('Action_432_04', 5)	# 65805-65809
    sprite('Action_432_01', 5)	# 65810-65814
    sprite('Action_432_02', 5)	# 65815-65819
    sprite('Action_432_03', 5)	# 65820-65824
    sprite('Action_432_04', 5)	# 65825-65829
    sprite('Action_432_01', 5)	# 65830-65834
    sprite('Action_432_02', 5)	# 65835-65839
    sprite('Action_432_03', 5)	# 65840-65844
    sprite('Action_432_04', 5)	# 65845-65849
    sprite('Action_432_01', 5)	# 65850-65854
    sprite('Action_432_02', 5)	# 65855-65859
    sprite('Action_432_03', 5)	# 65860-65864
    sprite('Action_432_04', 5)	# 65865-65869
    sprite('Action_432_05', 5)	# 65870-65874
    sprite('Action_432_06', 5)	# 65875-65879

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
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_046_01', 3)	# 1-3
    sprite('Action_046_02', 3)	# 4-6
    sprite('Action_046_03', 3)	# 7-9
    sprite('Action_046_04', 3)	# 10-12
    sprite('Action_046_05', 3)	# 13-15
    sprite('Action_046_06', 3)	# 16-18
    sprite('Action_046_07', 3)	# 19-21
    sprite('Action_046_08', 2)	# 22-23
    sprite('Action_046_09', 2)	# 24-25
    sprite('Action_046_10', 2)	# 26-27
    sprite('Action_046_11', 3)	# 28-30
    sprite('Action_046_01', 30)	# 31-60

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_432_06', 3)	# 1-3
    sprite('Action_432_05', 2)	# 4-5
    sprite('Action_432_04', 5)	# 6-10
    sprite('Action_432_01', 5)	# 11-15
    sprite('Action_432_02', 5)	# 16-20
    sprite('Action_432_03', 5)	# 21-25
    sprite('Action_432_04', 5)	# 26-30
    sprite('Action_432_01', 5)	# 31-35
    sprite('Action_432_02', 5)	# 36-40
    sprite('Action_432_03', 5)	# 41-45
    sprite('Action_432_04', 5)	# 46-50
    sprite('Action_432_01', 5)	# 51-55
    sprite('Action_432_02', 5)	# 56-60
    sprite('Action_432_03', 5)	# 61-65
    sprite('Action_432_05', 5)	# 66-70
    sprite('Action_432_06', 5)	# 71-75
    sprite('Action_000_05', 30)	# 76-105

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 25)	# 1-25
    label(0)
    sprite('Action_368_04', 5)	# 26-30
    Unknown1086(22)
    teleportRelativeX(-130000)
    Unknown1007(2400000)
    physicsYImpulse(-240000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sendToLabelUpon(2, 1)
    sprite('Action_368_05', 2)	# 31-32
    sprite('Action_368_06', 2)	# 33-34
    GFX_0('EffAirAssalut_Add', 100)
    sprite('Action_368_07', 32767)	# 35-32801	 **attackbox here**
    label(1)
    sprite('Action_368_07', 4)	# 32802-32805	 **attackbox here**
    sprite('Action_368_11', 3)	# 32806-32808
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_368_12', 3)	# 32809-32811
    sprite('Action_368_13', 11)	# 32812-32822
    sprite('Action_368_14', 4)	# 32823-32826

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_02', 2)	# 1-2
    sprite('Action_312_03', 2)	# 3-4
    sprite('Action_312_04', 24)	# 5-28
    sprite('Action_312_05', 4)	# 29-32
    sprite('Action_312_06', 4)	# 33-36
    sprite('Action_312_07', 4)	# 37-40
    sprite('Action_312_08', 4)	# 41-44
    sprite('Action_014_00', 4)	# 45-48
    sprite('Action_014_01', 4)	# 49-52
    sprite('Action_014_02', 4)	# 53-56
    sprite('Action_000_00', 30)	# 57-86

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_03', 3)	# 1-3
    sprite('Action_045_04', 4)	# 4-7
    sprite('Action_045_05', 4)	# 8-11
    sprite('Action_045_06', 4)	# 12-15
    sprite('Action_045_11', 7)	# 16-22
    sprite('Action_045_12', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('Action_046_00', 1)	# 1-1
    sprite('Action_046_01', 2)	# 2-3
    sprite('Action_046_01', 2)	# 4-5
    sprite('Action_046_02', 1)	# 6-6
    sprite('Action_046_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('Action_046_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05', 3)	# 13-15
    sprite('Action_046_06', 3)	# 16-18

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
    sprite('Action_035_06', 4)	# 3-6
    Unknown1019(95)
    sprite('Action_035_07', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('Action_013_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()

        def upon_STATE_END():
            Unknown13(9)
    sprite('Action_166_00', 3)	# 1-3
    Unknown1084(1)
    sprite('Action_166_01', 3)	# 4-6
    sprite('Action_166_02', 3)	# 7-9
    SFX_1('use301_0')
    SFX_3('SE_ApperLightWall')
    GFX_0('UltimateThrow_PauseShadow', 100)
    Unknown38(9, 1)
    sprite('Action_166_03', 3)	# 10-12
    sprite('Action_166_04', 3)	# 13-15
    sprite('Action_166_05', 3)	# 16-18
    sprite('Action_166_06', 3)	# 19-21
    sprite('Action_166_07', 3)	# 22-24
    sprite('Action_166_10', 2)	# 25-26
    sprite('Action_166_11', 2)	# 27-28
    sprite('Action_166_12', 2)	# 29-30
    sprite('Action_000_00', 2)	# 31-32
    sprite('Action_137_00', 4)	# 33-36
    Unknown13(9)
    sprite('Action_137_01', 4)	# 37-40
    sprite('Action_137_02', 1)	# 41-41
    GFX_0('Shot_Zanzo', 0)
    Unknown7006('use200_0', 100, 845509493, 828321840, 0, 0, 100, 845509493, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_137_02', 2)	# 42-43
    Unknown23090(4)
    sprite('Action_137_03', 3)	# 44-46
    GFX_0('Shot_Charge', 0)
    Unknown38(4, 1)
    Unknown23029(4, 207, 0)
    sprite('Action_137_04', 3)	# 47-49
    sprite('Action_137_05', 4)	# 50-53
    sprite('Action_137_06', 5)	# 54-58
    sprite('Action_137_09', 5)	# 59-63
    sprite('Action_137_10', 5)	# 64-68

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        Unknown11042(1)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(42000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_222_00', 3)	# 1-3
    GFX_0('EffNmlAtk5B_4th_LandZanzo1', 100)
    GFX_0('EffNmlAtk5B_4th_LandZanzo2', 100)
    sprite('Action_222_00', 2)	# 4-5
    Unknown2035(1)
    Unknown3001(0)
    Unknown2017(0)
    physicsXImpulse(15000)
    SFX_3('SE050')
    sprite('Action_222_06', 2)	# 6-7
    clearUponHandler(3)
    Unknown2017(1)
    Unknown2006()
    Unknown3004(60)
    physicsXImpulse(15000)
    Unknown1028(1500)
    sprite('Action_222_06', 2)	# 8-9
    Unknown2035(0)
    Unknown7006('use303_0', 100, 862286709, 845100336, 0, 0, 100, 828732277, 811545648, 0, 0, 100, 862286709, 828322608, 0, 0, 100)
    sprite('Action_222_07', 4)	# 10-13	 **attackbox here**
    GFX_0('EffNmlAtk5B_3rd_Kick', 100)
    SFX_3('SE043')
    RefreshMultihit()
    Unknown1084(1)
    sprite('Action_222_08', 6)	# 14-19
    sprite('Action_222_09', 4)	# 20-23
    sprite('Action_222_10', 4)	# 24-27
    sprite('Action_222_11', 4)	# 28-31
    sprite('Action_222_12', 4)	# 32-35
    sprite('Action_222_13', 4)	# 36-39
    sprite('Action_222_14', 3)	# 40-42

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2400)
        AttackP1(70)
        Unknown11042(1)
        Hitstop(4)
        Unknown11001(5, 5, 5)
        Unknown11028(20)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(38000)
        AirUntechableTime(60)
        PushbackX(19800)
        Unknown9016(1)

        def upon_11():
            Unknown2017(0)

        def upon_STATE_END():
            Unknown2035(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_210_00', 5)	# 1-5
    sprite('Action_210_01', 3)	# 6-8
    sprite('Action_210_02', 2)	# 9-10
    sprite('Action_210_03', 1)	# 11-11
    physicsXImpulse(5000)
    Unknown3004(-50)
    sprite('Action_210_04', 1)	# 12-12
    sprite('Action_210_05', 1)	# 13-13
    SFX_3('SE242')
    Unknown7006('use204_0', 100, 845509493, 845099824, 0, 0, 100, 845509493, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_210_06', 2)	# 14-15	 **attackbox here**
    Unknown2035(1)
    physicsXImpulse(150000)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    GFX_0('EffAssalut_Blade', 100)
    sprite('Action_210_07', 3)	# 16-18	 **attackbox here**
    sprite('Action_210_08', 1)	# 19-19	 **attackbox here**
    Unknown3004(80)
    physicsXImpulse(8000)
    Unknown1028(-400)
    GFX_0('EffAssalut_Zanzo', 100)
    Unknown4004('6566666563745f3033380000000000000000000000000000000000000000000064000000')
    sprite('Action_210_09', 2)	# 20-21	 **attackbox here**
    Unknown23027()
    sprite('Action_210_10', 3)	# 22-24
    Unknown2035(0)
    Recovery()
    Unknown2017(1)
    sprite('Action_210_11', 4)	# 25-28
    sprite('Action_210_12', 4)	# 29-32
    sprite('Action_210_11', 4)	# 33-36
    sprite('Action_210_12', 4)	# 37-40
    sprite('Action_210_13', 4)	# 41-44
    Unknown1084(1)
    sprite('Action_210_14', 3)	# 45-47
    Unknown2006()

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
    Unknown2036(53, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-100000)
    Unknown1019(4)
    label(0)
    sprite('Action_035_06', 4)	# 3-6
    sprite('Action_035_07', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateRushDDDOD')
    else:
        enterState('UltimateRushDDD')

@State
def UltimateRushDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown9154(90)
        Hitstop(13)
        AirUntechableTime(90)
        PushbackX(19800)
        AirPushbackX(3500)
        AirPushbackY(21500)
        YImpluseBeforeWallbounce(800)
        Unknown9016(0)
        Unknown11072(1, 65000, 0)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11069('UltimateRush_AtkDmy')
        Unknown30063(1)
        Unknown11064(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown3025(-1, 1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(1)
    sprite('Action_154_00', 20)	# 1-20
    Unknown1084(1)
    setInvincible(1)
    sprite('Action_154_01', 4)	# 21-24
    sprite('Action_222_06', 2)	# 25-26
    clearUponHandler(3)
    Unknown2006()
    Unknown3004(60)
    physicsXImpulse(2500)
    Unknown1028(1500)
    sprite('Action_222_06', 2)	# 27-28
    sprite('Action_222_07', 4)	# 29-32	 **attackbox here**
    GFX_0('EffNmlAtk5B_3rd_Kick', 100)
    RefreshMultihit()
    Unknown1084(1)
    sprite('Action_222_08', 6)	# 33-38
    setInvincible(0)
    sprite('Action_222_09', 7)	# 39-45
    sprite('Action_222_10', 4)	# 46-49
    sprite('Action_222_11', 5)	# 50-54
    sprite('Action_222_12', 6)	# 55-60
    sprite('Action_222_13', 6)	# 61-66
    sprite('Action_222_14', 6)	# 67-72
    ExitState()
    label(1)
    sprite('Action_156_52', 10)	# 73-82
    Unknown3025(-16777216, 10)
    GFX_0('UltimateRush_Camera', 100)
    Unknown38(9, 1)
    sprite('Action_156_53', 10)	# 83-92	 **attackbox here**
    Unknown3026(-16777216)
    Unknown3004(-50)
    sprite('Action_156_54', 1)	# 93-93	 **attackbox here**
    enterState('UltimateRushDDD_Exe')

@State
def UltimateRushDDD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(500)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Hitstop(0)
        AirUntechableTime(90)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        setInvincible(1)
        Unknown23027()
        Unknown3038(1)
        Unknown30063(1)

        def upon_43():
            if (SLOT_48 == 1000):
                GFX_0('UltimateRush_FinishShadow', 100)
                Unknown23029(1, 1002, 0)
                sendToLabel(10)

        def upon_STATE_END():
            Unknown3038(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_160_00ex01', 300)	# 1-300	 **attackbox here**
    GFX_0('UltimateRush_Shadow', 100)
    GFX_0('UltimateRush_AtkDmy', 100)
    Unknown23029(1, 1002, 0)
    ExitState()
    label(10)
    sprite('Action_160_00ex01', 3)	# 301-303	 **attackbox here**
    RefreshMultihit()
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(250000)
    physicsXImpulse(-50000)
    physicsYImpulse(-50000)
    Unknown3038(0)
    Unknown3001(0)
    SFX_3('SE_BigBomb')
    SFX_1('use252_0')
    sprite('Action_160_00ex01', 2)	# 304-305	 **attackbox here**
    Unknown3004(96)
    sprite('Action_160_01ex01', 5)	# 306-310
    Unknown1084(1)
    sprite('Action_160_02ex01', 5)	# 311-315
    sprite('Action_160_03ex01', 5)	# 316-320
    sprite('Action_160_04ex01', 5)	# 321-325
    sprite('Action_160_05ex01', 15)	# 326-340
    sprite('Action_160_06ex01', 7)	# 341-347
    sprite('Action_160_07ex01', 7)	# 348-354
    Unknown23029(9, 1001, 0)
    sprite('Action_160_08ex01', 7)	# 355-361
    sprite('Action_160_09ex01', 5)	# 362-366

@State
def UltimateRushDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown9154(90)
        Hitstop(13)
        AirUntechableTime(90)
        PushbackX(19800)
        AirPushbackX(3500)
        AirPushbackY(21500)
        YImpluseBeforeWallbounce(800)
        Unknown9016(0)
        Unknown11072(1, 65000, 0)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11069('UltimateRushOD_AtkDmy')
        Unknown30063(1)
        Unknown11064(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
            Unknown3025(-1, 1)

        def upon_78():
            clearUponHandler(78)
            sendToLabel(1)
    sprite('Action_154_00', 20)	# 1-20
    Unknown1084(1)
    setInvincible(1)
    sprite('Action_154_01', 4)	# 21-24
    sprite('Action_222_06', 2)	# 25-26
    clearUponHandler(3)
    Unknown2006()
    Unknown3004(60)
    physicsXImpulse(2500)
    Unknown1028(1500)
    sprite('Action_222_06', 2)	# 27-28
    sprite('Action_222_07', 4)	# 29-32	 **attackbox here**
    GFX_0('EffNmlAtk5B_3rd_Kick', 100)
    RefreshMultihit()
    Unknown1084(1)
    sprite('Action_222_08', 6)	# 33-38
    setInvincible(0)
    sprite('Action_222_09', 7)	# 39-45
    sprite('Action_222_10', 4)	# 46-49
    sprite('Action_222_11', 5)	# 50-54
    sprite('Action_222_12', 6)	# 55-60
    sprite('Action_222_13', 6)	# 61-66
    sprite('Action_222_14', 6)	# 67-72
    ExitState()
    label(1)
    sprite('Action_156_52', 10)	# 73-82
    Unknown3025(-16777216, 10)
    GFX_0('UltimateRush_Camera', 100)
    Unknown38(9, 1)
    sprite('Action_156_53', 10)	# 83-92	 **attackbox here**
    Unknown3026(-16777216)
    Unknown3004(-50)
    sprite('Action_156_54', 1)	# 93-93	 **attackbox here**
    enterState('UltimateRushDDDOD_Exe')

@State
def UltimateRushDDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(500)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Hitstop(0)
        AirUntechableTime(90)
        Unknown9310(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9016(1)
        setInvincible(1)
        Unknown23027()
        Unknown3038(1)
        Unknown30063(1)

        def upon_43():
            if (SLOT_48 == 1000):
                GFX_0('UltimateRushOD_FinishShadow', 100)
                Unknown23029(1, 1002, 0)
                sendToLabel(10)

        def upon_STATE_END():
            Unknown3038(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_160_00ex01', 300)	# 1-300	 **attackbox here**
    GFX_0('UltimateRushOD_Shadow', 100)
    GFX_0('UltimateRushOD_AtkDmy', 100)
    Unknown23029(1, 1002, 0)
    ExitState()
    label(10)
    sprite('Action_160_00ex01', 3)	# 301-303	 **attackbox here**
    RefreshMultihit()
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(250000)
    physicsXImpulse(-50000)
    physicsYImpulse(-50000)
    Unknown3038(0)
    Unknown3001(0)
    SFX_3('SE_BigBomb')
    SFX_1('use252_0')
    sprite('Action_160_00ex01', 2)	# 304-305	 **attackbox here**
    Unknown3004(96)
    sprite('Action_160_01ex01', 5)	# 306-310
    Unknown1084(1)
    sprite('Action_160_02ex01', 5)	# 311-315
    sprite('Action_160_03ex01', 5)	# 316-320
    sprite('Action_160_04ex01', 5)	# 321-325
    sprite('Action_160_05ex01', 15)	# 326-340
    sprite('Action_160_06ex01', 7)	# 341-347
    sprite('Action_160_07ex01', 7)	# 348-354
    Unknown23029(9, 1001, 0)
    sprite('Action_160_08ex01', 7)	# 355-361
    sprite('Action_160_09ex01', 5)	# 362-366

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 6)	# 121-126
    Unknown1086(22)
    teleportRelativeX(-130000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    Unknown2053(1)
    setGravity(0)
    sprite('Action_368_00', 3)	# 127-129
    sprite('Action_368_01', 3)	# 130-132
    sprite('Action_368_02', 3)	# 133-135
    sprite('Action_368_03', 4)	# 136-139
    sprite('Action_368_04', 5)	# 140-144
    sprite('Action_368_05', 2)	# 145-146
    sendToLabelUpon(2, 1)
    sprite('Action_368_06', 2)	# 147-148
    GFX_0('EffAirAssalut_Add', 100)
    sprite('Action_368_07', 32767)	# 149-32915	 **attackbox here**
    label(1)
    sprite('Action_368_11', 4)	# 32916-32919
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_368_12', 5)	# 32920-32924
    sprite('Action_368_13', 17)	# 32925-32941
    sprite('Action_368_14', 5)	# 32942-32946
Unknown18011('use520', 12643, 13153, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use521', 12643, 13409, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use522', 12643, 13153, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use523', 12643, 13409, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use540', 12643, 12897, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use541', 12643, 13153, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use542', 12643, 12897, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use543', 12643, 12641, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use544', 12643, 12641, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use545', 12643, 12641, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use402_0', 12643, 12641, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use402_1', 12643, 12641, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use403_0', 12643, 14689, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Unknown18011('use403_1', 12643, 14689, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    Unknown19(991, 2, 158)
    label(0)
    sprite('Action_050_02', 5)	# 2-6
    sprite('Action_050_03', 5)	# 7-11
    sprite('Action_050_04', 5)	# 12-16
    sprite('Action_050_05', 5)	# 17-21
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    label(1)
    loopRest()
    sprite('Action_050_02', 5)	# 22-26
    sprite('Action_050_03', 5)	# 27-31
    Unknown7006('use520', 100, 895841141, 12594, 0, 0, 100, 895841141, 12850, 0, 0, 100, 895841141, 13106, 0, 0, 100)
    sprite('Action_050_04', 5)	# 32-36
    sprite('Action_050_05', 5)	# 37-41
    sprite('Action_050_02', 5)	# 42-46
    sprite('Action_050_03', 5)	# 47-51
    sprite('Action_050_04', 5)	# 52-56
    sprite('Action_050_05', 5)	# 57-61
    sprite('Action_050_02', 5)	# 62-66
    sprite('Action_050_03', 5)	# 67-71
    sprite('Action_050_04', 5)	# 72-76
    sprite('Action_050_05', 5)	# 77-81
    sprite('Action_050_02', 5)	# 82-86
    sprite('Action_050_03', 5)	# 87-91
    sprite('Action_050_04', 5)	# 92-96
    sprite('Action_050_05', 5)	# 97-101
    sprite('Action_050_06', 6)	# 102-107
    sprite('Action_050_07', 5)	# 108-112
    sprite('Action_050_08', 7)	# 113-119
    sprite('Action_050_09', 8)	# 120-127
    sprite('Action_050_10', 9)	# 128-136
    sprite('Action_050_11', 2)	# 137-138
    SFX_3('SE043')
    sprite('Action_050_12', 2)	# 139-140
    sprite('Action_050_13', 15)	# 141-155
    Unknown23018(1)
    sprite('Action_050_14', 4)	# 156-159
    label(2)
    sprite('Action_000_00', 5)	# 160-164
    sprite('Action_000_01', 5)	# 165-169
    sprite('Action_000_02', 5)	# 170-174
    sprite('Action_000_03', 5)	# 175-179
    sprite('Action_000_04', 5)	# 180-184
    sprite('Action_000_05', 5)	# 185-189
    sprite('Action_000_06', 5)	# 190-194
    sprite('Action_000_07', 5)	# 195-199
    sprite('Action_000_08', 5)	# 200-204
    sprite('Action_000_09', 5)	# 205-209
    sprite('Action_000_10', 5)	# 210-214
    loopRest()
    if SLOT_97:
        _gotolabel(2)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 215-215
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 5)	# 216-220
    sprite('Action_000_01', 5)	# 221-225
    sprite('Action_000_02', 5)	# 226-230
    sprite('Action_000_03', 5)	# 231-235
    sprite('Action_000_04', 5)	# 236-240
    sprite('Action_000_05', 5)	# 241-245
    sprite('Action_000_06', 5)	# 246-250
    sprite('Action_000_07', 5)	# 251-255
    sprite('Action_000_08', 5)	# 256-260
    sprite('Action_000_09', 5)	# 261-265
    sprite('Action_000_10', 5)	# 266-270
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
    label(0)
    sprite('Action_053_00', 5)	# 4-8
    Unknown1084(1)
    GFX_0('Win_Knife', 0)
    sprite('Action_053_01', 4)	# 9-12
    if SLOT_158:
        if SLOT_52:
            Unknown7006('use544', 100, 895841141, 13620, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('use402_0', 100, 879063925, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('use540', 100, 895841141, 12596, 0, 0, 100, 895841141, 12852, 0, 0, 100, 895841141, 13108, 0, 0, 100)
    sprite('Action_053_01ex01', 2)	# 13-14
    sprite('Action_053_02', 5)	# 15-19
    sprite('Action_053_02ex01', 2)	# 20-21
    sprite('Action_053_03', 6)	# 22-27
    sprite('Action_053_03ex01', 2)	# 28-29
    sprite('Action_053_04', 15)	# 30-44
    sprite('Action_053_05', 6)	# 45-50
    SFX_3('SE043')
    GFX_0('Win_Knife_Equip', 100)
    sprite('Action_053_06', 8)	# 51-58
    sprite('Action_053_07', 7)	# 59-65
    sprite('Action_053_08', 6)	# 66-71
    sprite('Action_053_09', 5)	# 72-76
    Unknown23018(1)
    label(1)
    sprite('Action_053_10', 5)	# 77-81	 **attackbox here**
    sprite('Action_053_11', 5)	# 82-86	 **attackbox here**
    sprite('Action_053_12', 5)	# 87-91	 **attackbox here**
    sprite('Action_053_13', 5)	# 92-96	 **attackbox here**
    sprite('Action_053_14', 5)	# 97-101	 **attackbox here**
    sprite('Action_053_15', 5)	# 102-106	 **attackbox here**
    sprite('Action_053_16', 5)	# 107-111	 **attackbox here**
    sprite('Action_053_17', 5)	# 112-116	 **attackbox here**
    sprite('Action_053_18', 5)	# 117-121	 **attackbox here**
    sprite('Action_053_19', 5)	# 122-126	 **attackbox here**
    gotoLabel(1)

@State
def CmnActLose():
    sprite('Action_248_00', 6)	# 1-6
    sprite('Action_248_01', 4)	# 7-10	 **attackbox here**
    Unknown7006('use403_0', 100, 879063925, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_248_02', 4)	# 11-14	 **attackbox here**
    Unknown23018(1)
    sprite('Action_248_03', 5)	# 15-19
    sprite('Action_248_04', 5)	# 20-24
    sprite('Action_248_05', 3)	# 25-27
    sprite('Action_248_06', 4)	# 28-31
    sprite('Action_248_07', 32767)	# 32-32798
