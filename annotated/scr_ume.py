@Subroutine
def PreInit():
    Unknown12019('756d6500000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Unknown12011(1500)
    DoubleJumpCount(0)
    AirDashCount(0)
    Unknown12024(3)
    Unknown13039(0)
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
    Unknown14015(-50000, 300000, -150000, 400000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(5000)
    Unknown14015(-50000, 300000, -150000, 400000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15015(70, 75)
    Unknown15013(5000)
    Unknown14015(-50000, 300000, -150000, 400000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15013(5000)
    Unknown14015(-50000, 300000, -150000, 400000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(300000, 600000, -200000, 100000, 1500, 0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(300000, 600000, -200000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown14015(300000, 600000, -200000, 100000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 100, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(6000, 213000, -172000, -24000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(100000, 700000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtkAIR5A2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(-100000, 400000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(100000, 700000, -500000, -250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(50000, 350000, -600000, -200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('Flying_Start', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0xd9)
    Move_AirGround_(0x3008)
    Move_AirGround_(0x3009)
    Unknown14015(0, 450000, -200000, 300000, 0, 10)
    Move_EndRegister()
    Move_Register('Airdash', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0xda)
    Move_AirGround_(0x3009)
    Unknown14015(0, 450000, -200000, 300000, 0, 10)
    Move_EndRegister()
    Move_Register('Airdash_Ex', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3009)
    Unknown14013('Airdash')
    Unknown14015(0, 450000, -200000, 300000, 0, 10)
    Move_EndRegister()
    Move_Register('AirBackdash', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0xdb)
    Move_AirGround_(0x3009)
    Unknown14015(0, 450000, -200000, 300000, 0, 10)
    Move_EndRegister()
    Move_Register('AirBackdash_Ex', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0x5f)
    Move_Input_(INPUT_PRESS_A)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x3009)
    Unknown14013('AirBackdash')
    Unknown14015(0, 450000, -200000, 300000, 0, 10)
    Move_EndRegister()
    Move_Register('RushA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(200000, 500000, -200000, 200000, 100, 20)
    Move_EndRegister()
    Move_Register('RushB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(300000, 700000, -200000, 200000, 100, 20)
    Move_EndRegister()
    Move_Register('Rush_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(300000, 700000, -200000, 200000, 100, 20)
    Move_EndRegister()
    Move_Register('CaptureA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(600000, 1500000, -200000, 200000, 300, 10)
    Move_EndRegister()
    Move_Register('CaptureB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(600000, 2000000, 250000, 400000, 0, 10)
    Move_EndRegister()
    Move_Register('Capture_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(600000, 1500000, -200000, 200000, 200, 10)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(500000, 200000, -600000, -200000, 200, 50)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(500000, 1500000, -600000, -200000, 200, 50)
    Move_EndRegister()
    Move_Register('AirShot_Ex', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown14015(500000, 1500000, -600000, -200000, 200, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(7000, 266000, -123000, 655000, 100, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown14015(7000, 266000, -123000, 655000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(-200000, 500000, -35000, 450000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(-200000, 500000, -35000, 450000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateCapture', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(300000, 700000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateCapture_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(300000, 700000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('AirUltimateCapture', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(500000, 200000, -600000, -200000, 50, 0)
    Move_EndRegister()
    Move_Register('AirUltimateCapture_OD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(500000, 200000, -600000, -200000, 50, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15000(0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
    Unknown15024('NmlAtk5B3rd', 'RushB', 10000000)
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
    Unknown12018(16, 'Action_303_00')
    Unknown12018(17, 'Action_304_00')
    Unknown12018(18, 'Action_305_00')
    Unknown12018(19, 'Action_000_00')
    Unknown12018(20, 'Action_000_00')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_02')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_351_05')
    Unknown12018(29, 'Action_292_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'ume000')
    Unknown7010(1, 'ume001')
    Unknown7010(2, 'ume002')
    Unknown7010(3, 'ume003')
    Unknown7010(4, 'ume004')
    Unknown7010(5, 'ume005')
    Unknown7010(6, 'ume006')
    Unknown7010(7, 'ume007')
    Unknown7010(8, 'ume008')
    Unknown7010(9, 'ume009')
    Unknown7010(10, 'ume010')
    Unknown7010(15, 'ume011')
    Unknown7010(16, 'ume012')
    Unknown7010(17, 'ume013')
    Unknown7010(18, 'ume014')
    Unknown7010(19, 'ume015')
    Unknown7010(20, 'ume016')
    Unknown7010(21, 'ume017')
    Unknown7010(22, 'ume018')
    Unknown7010(23, 'ume019')
    Unknown7010(24, 'ume020')
    Unknown7010(25, 'ume021')
    Unknown7010(28, 'ume022')
    Unknown7010(29, 'ume023')
    Unknown7010(30, 'ume024')
    Unknown7010(31, 'ume025')
    Unknown7010(32, 'ume026')
    Unknown7010(33, 'ume027')
    Unknown7010(34, 'ume028')
    Unknown7010(35, 'ume029')
    Unknown7010(36, 'ume030')
    Unknown7010(37, 'ume031')
    Unknown7010(39, 'ume032')
    Unknown7010(42, 'ume033')
    Unknown7010(43, 'ume034')
    Unknown7010(44, 'ume035')
    Unknown7010(45, 'ume036')
    Unknown7010(46, 'ume037')
    Unknown7010(47, 'ume038')
    Unknown7010(48, 'ume039')
    Unknown7010(49, 'ume040')
    Unknown7010(50, 'ume041')
    Unknown7010(52, 'ume042')
    Unknown7010(53, 'ume043')
    Unknown7010(54, 'ume100_0')
    Unknown7010(55, 'ume100_1')
    Unknown7010(56, 'ume100_2')
    Unknown7010(63, 'ume101_0')
    Unknown7010(64, 'ume101_1')
    Unknown7010(65, 'ume101_2')
    Unknown7010(57, 'ume102_0')
    Unknown7010(58, 'ume102_1')
    Unknown7010(59, 'ume102_2')
    Unknown7010(66, 'ume103_0')
    Unknown7010(67, 'ume103_1')
    Unknown7010(68, 'ume103_2')
    Unknown7010(60, 'ume104_0')
    Unknown7010(61, 'ume104_1')
    Unknown7010(62, 'ume104_2')
    Unknown7010(69, 'ume105_0')
    Unknown7010(70, 'ume105_1')
    Unknown7010(71, 'ume105_2')
    Unknown7010(72, 'ume150')
    Unknown7010(73, 'ume151')
    Unknown7010(74, 'ume152')
    Unknown7010(85, 'ume153')
    Unknown7010(87, 'ume154')
    Unknown7010(88, 'ume155')
    Unknown7010(96, 'ume161_0')
    Unknown7010(97, 'ume161_1')
    Unknown7010(92, 'ume162_0')
    Unknown7010(93, 'ume162_1')
    Unknown7010(98, 'ume163_0')
    Unknown7010(99, 'ume163_1')
    Unknown7010(100, 'ume164_0')
    Unknown7010(101, 'ume164_1')
    Unknown7010(105, 'ume165_0')
    Unknown7010(106, 'ume165_1')
    Unknown7010(102, 'ume166_0')
    Unknown7010(103, 'ume166_1')
    Unknown7010(90, 'ume167_0')
    Unknown7010(91, 'ume167_1')
    Unknown7010(107, 'ume168_0')
    Unknown7010(108, 'ume168_1')
    Unknown7010(110, 'ume169_0')
    Unknown7010(111, 'ume169_1')
    Unknown7010(94, 'ume400_0')
    Unknown7010(95, 'ume400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('04000000556c74696d617465436170747572650000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465436170747572655f4f440000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnPreDraw():
    Unknown23030('554d455f4c696e65416e696d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def OnFrameStep():
    if SLOT_37:
        SLOT_4 = 0
        SLOT_5 = 0

@State
def CmnActStand():
    label(0)
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_000_01', 4)	# 5-8
    sprite('Action_000_02', 4)	# 9-12
    sprite('Action_000_03', 4)	# 13-16
    sprite('Action_000_04', 4)	# 17-20
    sprite('Action_000_05', 4)	# 21-24
    sprite('Action_000_06', 4)	# 25-28
    sprite('Action_000_07', 4)	# 29-32
    sprite('Action_000_08', 4)	# 33-36
    sprite('Action_000_09', 4)	# 37-40
    sprite('Action_000_10', 4)	# 41-44
    sprite('Action_000_11', 4)	# 45-48
    sprite('Action_000_12', 4)	# 49-52
    sprite('Action_000_13', 4)	# 53-56
    sprite('Action_000_14', 4)	# 57-60
    sprite('Action_000_15', 4)	# 61-64
    sprite('Action_000_16', 4)	# 65-68
    sprite('Action_000_17', 4)	# 69-72
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('Action_000_00', 1)	# 73-73	 **attackbox here**
    SLOT_88 = 960
    SFX_1('ume000')
    loopRest()
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
    sprite('Action_012_03', 2)	# 9-10

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 2)	# 1-2
    sprite('Action_013_01', 4)	# 3-6
    sprite('Action_013_02', 4)	# 7-10
    sprite('Action_013_03', 4)	# 11-14
    sprite('Action_013_04', 4)	# 15-18
    sprite('Action_013_05', 4)	# 19-22
    sprite('Action_013_06', 4)	# 23-26
    sprite('Action_013_07', 4)	# 27-30
    sprite('Action_013_08', 4)	# 31-34
    sprite('Action_013_09', 4)	# 35-38
    sprite('Action_013_10', 4)	# 39-42
    sprite('Action_013_11', 4)	# 43-46
    sprite('Action_013_12', 4)	# 47-50
    sprite('Action_013_13', 4)	# 51-54
    sprite('Action_013_14', 4)	# 55-58
    sprite('Action_013_15', 4)	# 59-62
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 3)	# 1-3
    sprite('Action_016_01', 3)	# 4-6

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 3)	# 1-3
    sprite('Action_014_01', 5)	# 4-8
    sprite('Action_014_02', 6)	# 9-14

@State
def CmnActJumpPre():
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_039_00', 3)	# 1-3
    sprite('Action_039_01', 3)	# 4-6
    ExitState()
    label(0)
    sprite('Action_038_00', 3)	# 7-9
    sprite('Action_038_01', 3)	# 10-12
    ExitState()
    label(1)
    sprite('Action_037_00', 6)	# 13-18
    ExitState()

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_039_02', 3)	# 1-3
    sprite('Action_039_03', 2)	# 4-5
    sprite('Action_039_04', 4)	# 6-9
    sprite('Action_039_05', 4)	# 10-13
    ExitState()
    label(0)
    sprite('Action_038_02', 3)	# 14-16
    sprite('Action_038_03', 2)	# 17-18
    sprite('Action_038_04', 4)	# 19-22
    sprite('Action_038_05', 4)	# 23-26
    ExitState()
    label(1)
    sprite('Action_037_01', 4)	# 27-30
    sprite('Action_037_02', 4)	# 31-34
    ExitState()

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    sprite('Action_039_06', 4)	# 1-4
    sprite('Action_039_07', 4)	# 5-8
    ExitState()
    label(0)
    sprite('Action_038_06', 4)	# 9-12
    sprite('Action_038_07', 4)	# 13-16
    ExitState()
    label(1)
    sprite('Action_037_03', 3)	# 17-19
    sprite('Action_037_04', 3)	# 20-22
    sprite('Action_037_05', 4)	# 23-26
    ExitState()

@State
def CmnActJumpDown():
    if SLOT_16:
        _gotolabel(0)
    if SLOT_15:
        _gotolabel(1)
    label(2)
    label(20)
    sprite('Action_020_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_020_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_020_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_020_03', 4)	# 13-16	 **attackbox here**
    gotoLabel(20)
    label(0)
    label(10)
    sprite('Action_020_00', 4)	# 17-20	 **attackbox here**
    sprite('Action_020_01', 4)	# 21-24	 **attackbox here**
    sprite('Action_020_02', 4)	# 25-28	 **attackbox here**
    sprite('Action_020_03', 4)	# 29-32	 **attackbox here**
    gotoLabel(10)
    label(1)
    sprite('Action_037_06', 3)	# 33-35
    sprite('Action_037_07', 3)	# 36-38
    gotoLabel(1)

@State
def CmnActJumpLanding():
    if SLOT_15:
        _gotolabel(1)
    sprite('Action_021_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_021_01', 3)	# 3-5
    sprite('Action_021_02', 3)	# 6-8
    sprite('Action_021_03', 3)	# 9-11
    sprite('Action_021_04', 5)	# 12-16
    ExitState()
    label(1)
    sprite('Action_037_08', 5)	# 17-21

@State
def CmnActLandingStiffLoop():
    sprite('Action_021_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_021_01', 3)	# 3-5
    sprite('Action_021_02', 3)	# 6-8
    sprite('Action_021_03', 32767)	# 9-32775

@State
def CmnActLandingStiffEnd():
    sprite('Action_021_04', 5)	# 1-5

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 7)	# 1-7
    sprite('Action_010_01', 7)	# 8-14
    sprite('Action_010_02', 7)	# 15-21
    sprite('Action_010_03', 7)	# 22-28
    sprite('Action_010_04', 7)	# 29-35
    sprite('Action_010_05', 7)	# 36-42
    sprite('Action_010_06', 7)	# 43-49
    sprite('Action_010_07', 7)	# 50-56
    sprite('Action_010_08', 7)	# 57-63
    sprite('Action_010_09', 7)	# 64-70
    sprite('Action_010_10', 7)	# 71-77
    sprite('Action_010_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    label(0)
    sprite('Action_011_00', 8)	# 1-8
    sprite('Action_011_01', 8)	# 9-16
    sprite('Action_011_02', 8)	# 17-24
    sprite('Action_011_03', 8)	# 25-32
    sprite('Action_011_04', 8)	# 33-40
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_05', 8)	# 41-48
    sprite('Action_011_06', 8)	# 49-56
    sprite('Action_011_07', 8)	# 57-64
    sprite('Action_011_08', 8)	# 65-72
    sprite('Action_011_09', 8)	# 73-80
    sprite('Action_011_10', 8)	# 81-88
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_11', 8)	# 89-96
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_010_00', 4)	# 1-4
    sprite('Action_010_01', 4)	# 5-8
    label(0)
    sprite('Action_045_01', 1)	# 9-9
    sprite('Action_045_02', 1)	# 10-10
    sprite('Action_045_03', 1)	# 11-11
    sprite('Action_045_04', 1)	# 12-12
    sprite('Action_045_05', 1)	# 13-13
    sprite('Action_045_06', 1)	# 14-14
    sprite('Action_045_07', 1)	# 15-15
    sprite('Action_045_08', 1)	# 16-16
    sprite('Action_045_09', 1)	# 17-17
    sprite('Action_045_10', 1)	# 18-18
    sprite('Action_045_11', 1)	# 19-19
    sprite('Action_045_12', 1)	# 20-20
    sprite('Action_045_13', 1)	# 21-21
    sprite('Action_045_14', 1)	# 22-22
    sprite('Action_045_15', 1)	# 23-23
    sprite('Action_045_16', 1)	# 24-24
    sprite('Action_045_17', 1)	# 25-25
    sprite('Action_045_18', 1)	# 26-26
    sprite('Action_045_19', 1)	# 27-27
    sprite('Action_045_20', 1)	# 28-28
    sprite('Action_045_21', 1)	# 29-29
    sprite('Action_045_22', 1)	# 30-30
    sprite('Action_045_23', 1)	# 31-31
    sprite('Action_045_24', 1)	# 32-32
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_25', 4)	# 1-4
    sprite('Action_045_26', 4)	# 5-8
    sprite('Action_045_27', 4)	# 9-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincible(1)
        Unknown1084(1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('Action_046_00', 1)	# 1-1
    sprite('Action_046_01', 1)	# 2-2
    physicsXImpulse(-20000)
    sprite('Action_046_02', 1)	# 3-3
    Unknown8007(100, 1, 1)
    sprite('Action_046_03', 1)	# 4-4
    sprite('Action_046_04', 1)	# 5-5
    sprite('Action_046_05', 1)	# 6-6
    sprite('Action_046_06', 1)	# 7-7
    sprite('Action_046_07', 1)	# 8-8
    setInvincible(0)
    sprite('Action_046_08', 1)	# 9-9
    sprite('Action_046_09', 1)	# 10-10
    sprite('Action_046_10', 1)	# 11-11
    sprite('Action_046_11', 1)	# 12-12
    sprite('Action_046_12', 1)	# 13-13
    sprite('Action_046_13', 1)	# 14-14
    sprite('Action_046_14', 1)	# 15-15
    sprite('Action_046_15', 1)	# 16-16
    sprite('Action_046_16', 1)	# 17-17
    sprite('Action_046_17', 1)	# 18-18
    sprite('Action_046_18', 1)	# 19-19
    sprite('Action_046_19', 1)	# 20-20
    sprite('Action_046_20', 1)	# 21-21
    sprite('Action_046_21', 1)	# 22-22
    sprite('Action_046_22', 1)	# 23-23
    sprite('Action_046_23', 1)	# 24-24
    sprite('Action_046_24', 1)	# 25-25
    sprite('Action_046_25', 4)	# 26-29
    Unknown1019(5)
    sprite('Action_046_26', 4)	# 30-33
    sprite('Action_046_27', 4)	# 34-37
    Unknown1084(1)

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    pass

@State
def CmnActAirBDash():
    pass

@State
def CmnActAirTurn():
    sprite('Action_038_02', 3)	# 1-3
    sprite('Action_038_03', 2)	# 4-5
    sprite('Action_038_04', 4)	# 6-9
    sprite('Action_038_05', 4)	# 10-13

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
    sprite('Action_320_00', 5)	# 1-5
    label(0)
    sprite('Action_320_01', 5)	# 6-10
    sprite('Action_320_01', 5)	# 11-15
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('Action_320_02', 5)	# 1-5

@State
def CmnActBDownDown():
    sprite('Action_330_07', 4)	# 1-4
    label(0)
    sprite('Action_330_08', 4)	# 5-8
    sprite('Action_330_09', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('Action_351_00', 2)	# 1-2
    sprite('Action_331_01', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('Action_351_01', 3)	# 1-3
    sprite('Action_351_02', 3)	# 4-6
    sprite('Action_351_03', 3)	# 7-9
    sprite('Action_351_04', 3)	# 10-12
    sprite('Action_351_05', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('Action_356_04', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('Action_294_11', 4)	# 1-4
    sprite('Action_294_12', 4)	# 5-8
    sprite('Action_294_13', 3)	# 9-11
    sprite('Action_294_14', 3)	# 12-14
    sprite('Action_294_15', 4)	# 15-18
    sprite('Action_294_16', 4)	# 19-22
    sprite('Action_294_17', 4)	# 23-26

@State
def CmnActFDownUpper():
    label(0)
    sprite('Action_326_00', 6)	# 1-6
    sprite('Action_326_01', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActFDownUpperEnd():
    sprite('Action_326_02', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('Action_326_03', 3)	# 1-3
    sprite('Action_326_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('Action_351_00', 3)	# 1-3
    sprite('Action_351_01', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('Action_354_00', 4)	# 1-4
    sprite('Action_354_01', 4)	# 5-8
    sprite('Action_354_02', 4)	# 9-12
    sprite('Action_354_03', 4)	# 13-16

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
    sprite('Action_330_00', 4)	# 1-4
    label(0)
    sprite('Action_330_01', 4)	# 5-8
    sprite('Action_330_02', 4)	# 9-12
    sprite('Action_330_03', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('Action_330_04', 4)	# 1-4
    sprite('Action_330_05', 4)	# 5-8
    sprite('Action_330_06', 4)	# 9-12

@State
def CmnActVDownDown():
    sprite('Action_330_07', 4)	# 1-4
    label(0)
    sprite('Action_330_08', 4)	# 5-8
    sprite('Action_330_09', 4)	# 9-12
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
    sprite('Action_327_01', 4)	# 1-4
    sprite('Action_327_02', 3)	# 5-7
    sprite('Action_327_03', 5)	# 8-12
    sprite('Action_327_04', 6)	# 13-18
    sprite('Action_328_00', 2)	# 19-20
    sprite('Action_328_01', 2)	# 21-22

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
    sprite('Action_032_05', 1)	# 9-9	 **attackbox here**

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 4)	# 1-4
    sprite('Action_032_01', 4)	# 5-8
    sprite('Action_032_02', 4)	# 9-12
    sprite('Action_032_03', 4)	# 13-16
    sprite('Action_032_04', 4)	# 17-20
    sprite('Action_032_05', 3)	# 21-23	 **attackbox here**

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 4)	# 1-4
    sprite('Action_032_01', 4)	# 5-8
    sprite('Action_032_02', 4)	# 9-12
    sprite('Action_032_03', 4)	# 13-16
    sprite('Action_032_04', 4)	# 17-20
    sprite('Action_032_05', 3)	# 21-23	 **attackbox here**
    sprite('Action_032_06', 3)	# 24-26	 **attackbox here**
    sprite('Action_032_07', 3)	# 27-29	 **attackbox here**

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_041_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_041_07', 2)	# 15-16	 **attackbox here**

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_041_06', 2)	# 13-14	 **attackbox here**
    sprite('Action_041_07', 2)	# 15-16	 **attackbox here**

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 4)	# 7-10
    sprite('Action_041_04', 4)	# 11-14
    sprite('Action_041_05', 4)	# 15-18	 **attackbox here**
    sprite('Action_041_06', 4)	# 19-22	 **attackbox here**
    sprite('Action_041_07', 4)	# 23-26	 **attackbox here**
    sprite('Action_041_08', 40)	# 27-66	 **attackbox here**

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_09', 2)	# 1-2
    sprite('Action_041_10', 4)	# 3-6
    sprite('Action_041_11', 6)	# 7-12
    sprite('Action_041_12', 3)	# 13-15

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
    sprite('Action_017_05', 3)	# 1-3
    sprite('Action_017_06', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_05', 3)	# 1-3
    sprite('Action_017_06', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('Action_017_05', 3)	# 1-3
    sprite('Action_017_06', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_05', 3)	# 1-3
    sprite('Action_017_06', 3)	# 4-6

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
    sprite('Action_018_16', 3)	# 1-3
    sprite('Action_018_17', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('Action_018_01', 3)	# 1-3
    sprite('Action_018_02', 3)	# 4-6
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_16', 3)	# 1-3
    sprite('Action_018_17', 3)	# 4-6

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
    sprite('Action_019_16', 3)	# 1-3
    sprite('Action_019_17', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('Action_019_02', 3)	# 1-3
    sprite('Action_019_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_16', 3)	# 1-3
    sprite('Action_019_17', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('Action_017_00', 2)	# 1-2
    sprite('Action_017_01', 2)	# 3-4
    sprite('Action_017_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_017_05', 6)	# 6-11
    sprite('Action_017_06', 6)	# 12-17

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
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_412_00', 7)	# 1-7	 **attackbox here**
    sprite('Action_412_01', 4)	# 8-11	 **attackbox here**
    sprite('Action_412_02', 4)	# 12-15	 **attackbox here**
    sprite('Action_412_03', 4)	# 16-19
    sprite('Action_412_04', 4)	# 20-23
    sprite('Action_412_05', 4)	# 24-27

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1
    sprite('Action_019_03', 3)	# 2-4
    sprite('Action_019_00', 3)	# 5-7

@State
def CmnActLandSpin():
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**

@State
def CmnActLandSpinDown():
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**

@State
def CmnActVertSpin():
    sprite('Action_000_00', 4)	# 1-4	 **attackbox here**

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
    sprite('Action_262_00', 4)	# 1-4
    label(0)
    sprite('Action_262_01', 5)	# 5-9
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
    sprite('Action_262_07', 5)	# 1-5
    sprite('Action_262_08', 5)	# 6-10
    sprite('Action_262_09', 4)	# 11-14
    label(0)
    sprite('Action_262_10', 4)	# 15-18	 **attackbox here**
    sprite('Action_262_11', 4)	# 19-22	 **attackbox here**
    sprite('Action_262_12', 4)	# 23-26	 **attackbox here**
    sprite('Action_262_13', 4)	# 27-30	 **attackbox here**
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
    sprite('Action_262_10', 3)	# 16-18	 **attackbox here**
    sprite('Action_262_11', 3)	# 19-21	 **attackbox here**
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
    sprite('Action_262_10', 3)	# 10-12	 **attackbox here**
    sprite('Action_262_11', 3)	# 13-15	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def Flying_Start():

    def upon_IMMEDIATE():
        Unknown17015()
        Unknown13014(1)
        Unknown13015(1)
        Unknown13019(1)
        Unknown2006()
        SLOT_4 = 1

        def upon_STATE_END():
            Unknown1043()

        def upon_LANDING():
            sendToLabel(2)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            SLOT_52 = 1
        physicsYImpulse(32500)
        Unknown1043()
        if CheckInput(0x85):
            physicsXImpulse(-8400)
        if CheckInput(0x92):
            physicsXImpulse(0)
        if CheckInput(0x9f):
            physicsXImpulse(8400)

        def upon_3():
            if (not SLOT_158):
                sendToLabel(1)
                clearUponHandler(17)
            if SLOT_51:
                Unknown2006()
                if (SLOT_12 >= 10000):
                    physicsXImpulse(10000)
                if (SLOT_12 <= (-10000)):
                    physicsXImpulse(-10000)
                if (SLOT_13 >= 10000):
                    physicsYImpulse(10000)
                if CheckInput(0x85):
                    Unknown1015(-500)
                    setGravity(0)
                    if (SLOT_23 <= 400000):
                        Unknown1021(500)
                    if (SLOT_23 >= 460000):
                        Unknown1021(-100)
                if CheckInput(0x92):
                    setGravity(0)
                    if (SLOT_23 <= 400000):
                        Unknown1021(500)
                    if (SLOT_23 >= 460000):
                        Unknown1021(-100)
                if CheckInput(0x9f):
                    setGravity(0)
                    Unknown1015(500)
                    if (SLOT_23 <= 400000):
                        Unknown1021(500)
                    if (SLOT_23 >= 460000):
                        Unknown1021(-100)
                if CheckInput(0x6b):
                    setGravity(0)
                    if (SLOT_23 >= 460000):
                        physicsYImpulse(-10000)
                    if (SLOT_12 < (-1500)):
                        Unknown1015(1500)
                    if (SLOT_12 > 1500):
                        Unknown1015(-1500)
                    if (SLOT_13 < (-1500)):
                        Unknown1021(1500)
                    if (SLOT_13 > 1500):
                        Unknown1021(-1500)
                if CheckInput(0x5e):
                    Unknown1015(-500)
                    setGravity(0)
                    if (SLOT_23 >= 460000):
                        Unknown1021(-100)
                    else:
                        physicsYImpulse(0)
                if CheckInput(0x78):
                    Unknown1015(500)
                    setGravity(0)
                    if (SLOT_23 >= 460000):
                        Unknown1021(-100)
                    else:
                        physicsYImpulse(0)
                if CheckInput(0x37):
                    setGravity(0)
                    Unknown1015(-500)
                    Unknown1021(-500)
                if CheckInput(0x44):
                    setGravity(0)
                    Unknown1021(-500)
                if CheckInput(0x51):
                    setGravity(0)
                    Unknown1015(500)
                    Unknown1021(-500)
    sprite('Action_145_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_145_01', 6)	# 5-10
    sprite('Action_145_02', 4)	# 11-14
    sprite('Action_145_03', 3)	# 15-17	 **attackbox here**
    SFX_3('015_blaze_0')
    sprite('Action_145_04', 6)	# 18-23	 **attackbox here**
    sprite('Action_145_05', 6)	# 24-29	 **attackbox here**
    SLOT_51 = 1
    Unknown1045(0)
    sprite('Action_145_06', 4)	# 30-33	 **attackbox here**
    label(0)
    sprite('Action_145_00', 4)	# 34-37	 **attackbox here**
    sprite('Action_145_01', 6)	# 38-43
    sprite('Action_145_02', 4)	# 44-47
    sprite('Action_145_03', 3)	# 48-50	 **attackbox here**
    SFX_3('015_blaze_0')
    sprite('Action_145_04', 6)	# 51-56	 **attackbox here**
    sprite('Action_145_05', 6)	# 57-62	 **attackbox here**
    sprite('Action_145_06', 4)	# 63-66	 **attackbox here**
    if SLOT_52:
        sendToLabel(1)
    gotoLabel(0)
    label(1)
    sprite('Action_145_00', 4)	# 67-70	 **attackbox here**
    physicsYImpulse(16250)
    Unknown1043()
    SLOT_5 = 1
    clearUponHandler(3)
    sprite('Action_145_01', 6)	# 71-76
    sprite('Action_145_02', 4)	# 77-80
    sprite('Action_145_03', 3)	# 81-83	 **attackbox here**
    SFX_3('015_blaze_0')
    sprite('Action_145_04', 6)	# 84-89	 **attackbox here**
    sprite('Action_145_05', 6)	# 90-95	 **attackbox here**
    sprite('Action_145_06', 4)	# 96-99	 **attackbox here**
    label(10)
    sprite('Action_145_00', 4)	# 100-103	 **attackbox here**
    sprite('Action_145_01', 6)	# 104-109
    sprite('Action_145_02', 4)	# 110-113
    sprite('Action_145_03', 3)	# 114-116	 **attackbox here**
    SFX_3('015_blaze_0')
    sprite('Action_145_04', 6)	# 117-122	 **attackbox here**
    sprite('Action_145_05', 6)	# 123-128	 **attackbox here**
    sprite('Action_145_06', 4)	# 129-132	 **attackbox here**
    gotoLabel(10)
    label(2)
    sprite('Action_145_09', 2)	# 133-134	 **attackbox here**
    Unknown1084(1)
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown8000(100, 1, 1)
    sprite('Action_145_10', 3)	# 135-137
    sprite('Action_145_11', 3)	# 138-140
    sprite('Action_145_12', 3)	# 141-143
    sprite('Action_145_13', 5)	# 144-148

@State
def Airdash():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(80)
        AirUntechableTime(30)
        AirPushbackX(40000)
        AirPushbackY(20000)
        AirHitstunAnimation(9)
        Unknown11056(0)
        Unknown9016(1)
        HitOverhead(0)
        Unknown11032('801a060001000000ffffffffffffffff')
        SLOT_4 = 1
        SLOT_5 = 1

        def upon_STATE_END():
            Unknown2006()
            Unknown1019(80)
            Unknown1028(0)
            Unknown1043()
            Unknown2015(-1)
            Unknown2016(-1)
        Unknown2003(1)
    sprite('Action_147_00', 6)	# 1-6	 **attackbox here**
    if (SLOT_13 >= 0):
        if (SLOT_23 <= 100000):
            physicsXImpulse(2500)
            physicsYImpulse(32500)
            Unknown1043()
    else:
        Unknown1084(1)
        physicsXImpulse(2500)
    clearUponHandler(2)
    sprite('Action_147_01', 3)	# 7-9
    Unknown7007('756d653030360000000000000000000064000000756d653330315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown8009(1)
    Unknown2015(150)
    Unknown2016(250)
    physicsXImpulse(15000)
    physicsYImpulse(-8000)
    Unknown1028(1000)
    setGravity(500)

    def upon_3():
        Unknown23073()
        if (SLOT_23 <= 100000):
            YAccel(0)
            teleportRelativeY(100000)
        if (SLOT_12 >= 41000):
            physicsXImpulse(41000)
            Unknown1028(0)
        if (SLOT_19 < 300000):
            Unknown2003(0)
    sprite('Action_147_02', 5)	# 10-14
    sprite('Action_147_03', 5)	# 15-19
    Unknown1028(3000)
    sprite('Action_147_04', 4)	# 20-23	 **attackbox here**
    YAccel(50)
    Unknown13014(1)
    Unknown13015(1)
    sprite('Action_147_05', 4)	# 24-27	 **attackbox here**
    sprite('Action_147_04', 4)	# 28-31	 **attackbox here**
    sprite('Action_147_05', 4)	# 32-35	 **attackbox here**
    sprite('Action_147_04', 4)	# 36-39	 **attackbox here**
    sprite('Action_147_05', 4)	# 40-43	 **attackbox here**
    sprite('Action_147_06', 6)	# 44-49
    Unknown2015(-1)
    Unknown2016(-1)
    Unknown1019(80)
    sendToLabelUpon(2, 1)
    clearUponHandler(3)
    Unknown1043()
    Recovery()
    sprite('Action_147_07', 5)	# 50-54
    Unknown1019(80)
    ExitState()
    label(1)
    sprite('Action_147_08', 5)	# 55-59	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    sprite('Action_147_09', 3)	# 60-62
    sprite('Action_147_10', 3)	# 63-65
    sprite('Action_147_11', 3)	# 66-68
    sprite('Action_147_12', 2)	# 69-70

@State
def AirBackdash():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1500)
        AttackP2(80)
        AirUntechableTime(30)
        AirPushbackX(40000)
        AirPushbackY(20000)
        AirHitstunAnimation(9)
        Unknown11056(0)
        Unknown9016(1)
        HitOverhead(0)
        Unknown11032('801a060001000000ffffffffffffffff')
        Unknown2005()
        SLOT_4 = 1
        SLOT_5 = 1

        def upon_STATE_END():
            Unknown2006()
            Unknown1019(80)
            Unknown1028(0)
            Unknown1043()
            Unknown2015(-1)
            Unknown2016(-1)
    sprite('Action_147_00', 6)	# 1-6	 **attackbox here**
    if (SLOT_13 >= 0):
        if (SLOT_23 <= 100000):
            physicsXImpulse(2500)
            physicsYImpulse(32500)
            Unknown1043()
    else:
        Unknown1084(1)
        physicsXImpulse(2500)
    clearUponHandler(2)
    sprite('Action_147_01', 3)	# 7-9
    Unknown7007('756d653030360000000000000000000064000000756d653330315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown8009(1)
    Unknown2015(150)
    Unknown2016(250)
    physicsXImpulse(15000)
    physicsYImpulse(-8000)
    Unknown1028(1000)
    setGravity(500)

    def upon_3():
        Unknown23073()
        if (SLOT_23 <= 100000):
            YAccel(0)
            teleportRelativeY(100000)
        if (SLOT_12 >= 32000):
            physicsXImpulse(32000)
            Unknown1028(0)
    sprite('Action_147_02', 5)	# 10-14
    sprite('Action_147_03', 5)	# 15-19
    Unknown1028(3000)
    sprite('Action_147_04', 4)	# 20-23	 **attackbox here**
    YAccel(50)
    Unknown13014(1)
    Unknown13015(1)
    sprite('Action_147_05', 4)	# 24-27	 **attackbox here**
    sprite('Action_147_04', 4)	# 28-31	 **attackbox here**
    sprite('Action_147_05', 4)	# 32-35	 **attackbox here**
    sprite('Action_147_06', 6)	# 36-41
    Unknown2015(-1)
    Unknown2016(-1)
    Unknown1019(80)
    sendToLabelUpon(2, 1)
    clearUponHandler(3)
    Unknown1043()
    Recovery()
    sprite('Action_147_07', 5)	# 42-46
    Unknown1019(80)
    ExitState()
    label(1)
    sprite('Action_147_08', 5)	# 47-51	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    sprite('Action_147_09', 3)	# 52-54
    sprite('Action_147_10', 3)	# 55-57
    sprite('Action_147_11', 3)	# 58-60
    sprite('Action_147_12', 2)	# 61-62

@Subroutine
def ChainRoot():
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    HitJumpCancel(1)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirHitstunAnimation(11)
        AirPushbackY(-50000)
        Unknown9310(1)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_101_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_101_01', 2)	# 5-6
    Unknown7009(1)
    sprite('Action_101_01', 1)	# 7-7
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_101_02', 2)	# 8-9
    sprite('Action_101_03', 2)	# 10-11	 **attackbox here**
    SFX_3('SE042')
    GFX_0('Mer_088', -1)
    sprite('Action_101_04', 3)	# 12-14	 **attackbox here**
    setInvincible(0)
    sprite('Action_101_05', 9)	# 15-23
    Recovery()
    Unknown2063()
    sprite('Action_101_06', 7)	# 24-30
    sprite('Action_101_07', 8)	# 31-38

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_001_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_001_01', 3)	# 5-7
    Unknown7009(0)
    sprite('Action_001_02', 4)	# 8-11	 **attackbox here**
    SFX_3('SE041')
    GFX_0('Mer_085', -1)
    sprite('Action_001_03', 10)	# 12-21
    Recovery()
    Unknown2063()
    sprite('Action_001_04', 5)	# 22-26
    sprite('Action_001_05', 5)	# 27-31

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(70)
        Unknown11044(1)
        Unknown2073(1)

        def upon_78():
            JumpCancel_(0)
            enterState('AN_NmlAtk5A_3rdPlus')
        Unknown11064(1)
    sprite('Action_165_00', 3)	# 1-3
    sprite('Action_165_01', 2)	# 4-5
    Unknown7009(2)
    physicsXImpulse(40000)
    sprite('Action_165_02', 2)	# 6-7
    SFX_3('SE042')
    physicsXImpulse(40000)
    sprite('Action_165_03', 3)	# 8-10	 **attackbox here**
    Unknown1084(1)
    sprite('Action_165_03', 7)	# 11-17	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('Action_165_04', 7)	# 18-24
    sprite('Action_165_05', 5)	# 25-29
    sprite('Action_165_06', 5)	# 30-34
    sprite('Action_165_07', 5)	# 35-39

@State
def AN_NmlAtk5A_3rdPlus():

    def upon_IMMEDIATE():
        Unknown17011('AN_NmlAtk5A_3rdExe', 1, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown11044(1)
        Hitstop(0)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11045(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11064(1)
        Unknown11023(1)
        JumpCancel_(0)
    sprite('Action_165_03', 3)	# 1-3	 **attackbox here**
    Unknown1084(1)
    sprite('Action_165_04', 7)	# 4-10
    Recovery()
    Unknown2063()
    sprite('Action_165_05', 5)	# 11-15
    sprite('Action_165_06', 5)	# 16-20
    sprite('Action_165_07', 5)	# 21-25

@State
def AN_NmlAtk5A_3rdExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(500)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP2(100)
        AirPushbackX(20000)
        AirPushbackY(20000)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown30079(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11091(0)
        Unknown2034(0)

        def upon_STATE_END():
            Unknown2034(1)
        Unknown20000(1)
        JumpCancel_(0)
    sprite('Action_167_00', 4)	# 1-4
    Unknown7007('756d653130395f30000000000000000064000000756d653130395f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_167_01', 5)	# 5-9
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_167_02', 5)	# 10-14
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_167_03', 6)	# 15-20
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_167_04', 5)	# 21-25
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_167_05', 4)	# 26-29
    GFX_0('Mer_076', -1)
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_167_06', 4)	# 30-33	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_167_07', 5)	# 34-38
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_01', 3)	# 39-41
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_02', 2)	# 42-43
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_03', 3)	# 44-46	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_04', 3)	# 47-49
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_05', 3)	# 50-52
    GFX_0('Mer_076', -1)
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_06', 3)	# 53-55
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_169_07', 3)	# 56-58	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown14070('AN_NmlAtk5A_4th')
    sprite('Action_169_08', 3)	# 59-61
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_172_00', 4)	# 62-65
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_172_01', 2)	# 66-67
    Unknown5000(17, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_172_02', 2)	# 68-69	 **attackbox here**
    RefreshMultihit()
    Unknown30079(0)
    Unknown20000(0)
    Unknown11072(1, 500000, 300000)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    JumpCancel_(1)
    Unknown11064(0)
    SFX_3('SE043')
    sprite('Action_172_03', 4)	# 70-73
    Unknown14072('AN_NmlAtk5A_4th')
    sprite('Action_172_04', 6)	# 74-79
    sprite('Action_172_05', 7)	# 80-86
    Unknown14074('AN_NmlAtk5A_4th')
    sprite('Action_172_06', 5)	# 87-91
    sprite('Action_172_07', 6)	# 92-97
    sprite('Action_172_08', 6)	# 98-103

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(2400)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        JumpCancel_(0)
    sprite('Action_172_05', 4)	# 1-4
    sprite('Action_172_06', 3)	# 5-7
    sprite('Action_172_07', 3)	# 8-10
    sprite('Action_130_00', 2)	# 11-12
    sprite('Action_130_01', 2)	# 13-14
    sprite('Action_130_05', 2)	# 15-16
    Unknown7007('756d653130365f30000000000000000064000000756d653130365f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('Action_130_06', 1)	# 17-17
    SFX_3('SE043')
    GFX_0('Mer_078', 0)
    Unknown36(1)
    Unknown1072(-20000)
    Unknown35()
    GFX_0('Mer_079', 1)
    Unknown36(1)
    Unknown1072(-16500)
    Unknown35()
    sprite('Action_130_07', 6)	# 18-23	 **attackbox here**
    sprite('Action_130_08', 5)	# 24-28	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_130_09', 6)	# 29-34
    sprite('Action_130_10', 6)	# 35-40
    sprite('Action_130_11', 6)	# 41-46
    sprite('Action_130_12', 6)	# 47-52

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        AttackLevel_(3)
        PushbackX(15300)
        AirPushbackY(12000)
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
        callSubroutine('ChainRoot')
    sprite('Action_002_00', 8)	# 1-8	 **attackbox here**
    sprite('Action_002_01', 4)	# 9-12
    Unknown7007('756d653130325f30000000000000000064000000756d653130325f31000000000000000064000000756d653130325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_002_02ex', 2)	# 13-14	 **attackbox here**
    SFX_3('SE042')
    GFX_0('Mer_084', -1)
    sprite('Action_002_03', 4)	# 15-18
    Recovery()
    Unknown2063()
    sprite('Action_002_04', 5)	# 19-23
    sprite('Action_002_05', 5)	# 24-28
    sprite('Action_002_06', 4)	# 29-32
    sprite('Action_002_07', 4)	# 33-36

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(15300)
        AirPushbackX(12000)
        AirPushbackY(16000)
        HitOrBlockCancel('AN_NmlAtk5B_3rd')
        callSubroutine('ChainRoot')
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 2)	# 3-4
    sprite('Action_003_02', 3)	# 5-7
    Unknown7007('756d653130335f30000000000000000064000000756d653130335f31000000000000000064000000756d653130335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_003_03', 3)	# 8-10
    sprite('Action_003_04', 3)	# 11-13
    sprite('Action_003_05', 1)	# 14-14
    GFX_0('Mer_078', 0)
    GFX_0('Mer_079', 1)
    SFX_3('SE043')
    sprite('Action_003_06', 5)	# 15-19	 **attackbox here**
    sprite('Action_003_07', 6)	# 20-25
    Recovery()
    Unknown2063()
    sprite('Action_003_08', 6)	# 26-31
    sprite('Action_003_09', 6)	# 32-37
    sprite('Action_003_10', 5)	# 38-42

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        PushbackX(15300)
        AirPushbackX(9000)
        AirPushbackY(-50000)
        Unknown9310(1)
        callSubroutine('ChainRoot')
    sprite('Action_131_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_131_01', 2)	# 4-5
    Unknown7007('756d653130365f30000000000000000064000000756d653130365f31000000000000000064000000756d653130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_131_02', 3)	# 6-8
    sprite('Action_131_03', 2)	# 9-10
    sprite('Action_131_06', 3)	# 11-13
    sprite('Action_131_07', 3)	# 14-16
    sprite('Action_131_08', 2)	# 17-18	 **attackbox here**
    Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
    GFX_0('Mer_083', -1)
    SFX_3('016_explode_0')
    sprite('Action_131_09', 7)	# 19-25
    Recovery()
    Unknown2063()
    sprite('Action_131_10', 5)	# 26-30
    sprite('Action_131_11', 5)	# 31-35
    sprite('Action_131_12', 4)	# 36-39
    sprite('Action_131_13', 4)	# 40-43
    sprite('Action_131_14', 4)	# 44-47

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        PushbackX(12000)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_004_00', 6)	# 1-6
    sprite('Action_004_01', 3)	# 7-9	 **attackbox here**
    GFX_0('Mer_093', -1)
    Unknown7007('756d653130315f30000000000000000064000000756d653130315f31000000000000000064000000756d653130315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('SE041')
    SFX_3('210_down_garden_0')
    sprite('Action_004_02', 2)	# 10-11
    WhiffCancelEnable(1)
    sprite('Action_004_03', 2)	# 12-13
    sprite('Action_004_04', 2)	# 14-15
    sprite('Action_004_05', 2)	# 16-17	 **attackbox here**
    GFX_0('Mer_094', -1)
    SFX_3('SE041')
    SFX_3('210_down_garden_0')
    RefreshMultihit()
    sprite('Action_004_06', 7)	# 18-24
    Recovery()
    Unknown2063()
    sprite('Action_004_07', 7)	# 25-31

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        PushbackX(12000)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_004_00', 5)	# 1-5
    sprite('Action_004_01', 3)	# 6-8	 **attackbox here**
    GFX_0('Mer_093', -1)
    Unknown7007('756d653130315f30000000000000000064000000756d653130315f31000000000000000064000000756d653130315f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('SE041')
    SFX_3('210_down_garden_0')
    sprite('Action_004_02', 2)	# 9-10
    WhiffCancelEnable(1)
    sprite('Action_004_03', 2)	# 11-12
    sprite('Action_004_04', 2)	# 13-14
    sprite('Action_004_05', 2)	# 15-16	 **attackbox here**
    GFX_0('Mer_094', -1)
    SFX_3('SE041')
    SFX_3('210_down_garden_0')
    RefreshMultihit()
    sprite('Action_004_06', 7)	# 17-23
    Recovery()
    Unknown2063()
    sprite('Action_004_07', 7)	# 24-30

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackY(16000)
        HitLow(2)
        Unknown9016(1)
        callSubroutine('ChainRoot')

        def upon_12():
            if (not SLOT_2):
                Unknown2037(1)
                GFX_0('Mer_071', 0)
    sprite('Action_005_00', 7)	# 1-7
    sprite('Action_005_01', 5)	# 8-12
    Unknown7007('756d653130345f30000000000000000064000000756d653130345f31000000000000000064000000756d653130345f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('SE042')
    sprite('Action_005_02', 2)	# 13-14	 **attackbox here**
    sprite('Action_005_03', 3)	# 15-17
    Unknown2037(0)
    sprite('Action_005_04', 3)	# 18-20
    sprite('Action_005_05', 4)	# 21-24	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(-2500)
    PushbackX(-8000)
    sprite('Action_005_06', 8)	# 25-32
    Recovery()
    Unknown2063()
    sprite('Action_005_07', 8)	# 33-40

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(90)
        AttackP2(75)
        Unknown11092(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(2000)
        AirPushbackY(15000)
        AirUntechableTime(22)
        PushbackX(12000)
        HitLow(2)
        Unknown9016(1)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            sendToLabel(0)

        def upon_12():
            if (not SLOT_2):
                Unknown2037(1)
                GFX_0('Mer_071', 0)
    sprite('Action_006_00', 4)	# 1-4
    sprite('Action_006_01', 3)	# 5-7
    sprite('Action_006_02', 2)	# 8-9
    SFX_3('SE042')
    physicsXImpulse(40000)
    Unknown8006(100, 1, 1)
    Unknown7007('756d653130375f30000000000000000064000000756d653130375f31000000000000000064000000756d653130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_006_03', 2)	# 10-11
    Unknown1028(-1000)
    sprite('Action_006_04', 7)	# 12-18	 **attackbox here**
    label(0)
    sprite('Action_132_00', 6)	# 19-24
    clearUponHandler(10)
    clearUponHandler(12)
    physicsXImpulse(12000)
    Unknown8000(100, 1, 1)
    sprite('Action_132_01', 6)	# 25-30
    Unknown1084(1)
    sprite('Action_132_02', 2)	# 31-32	 **attackbox here**
    physicsXImpulse(25000)
    Unknown1028(-5000)

    def upon_3():
        if (not SLOT_12):
            Unknown1084(1)
            clearUponHandler(3)
    SFX_3('SE042')
    sprite('Action_132_03', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    Unknown9083()
    HitLow(0)
    Unknown9016(0)
    sprite('Action_132_04', 8)	# 36-43	 **attackbox here**
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('Action_132_05', 5)	# 44-48
    sprite('Action_132_06', 5)	# 49-53
    sprite('Action_132_07', 6)	# 54-59

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOrBlockCancel('AN_NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Flying_Start')
    sprite('Action_008_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_008_01', 4)	# 4-7
    sprite('Action_008_02', 2)	# 8-9
    SFX_3('SE042')
    GFX_0('Mer_089', -1)
    Unknown7007('756d653130335f30000000000000000064000000756d653130335f31000000000000000064000000756d653130335f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown14070('Flying_Start')
    sprite('Action_008_03', 2)	# 10-11	 **attackbox here**
    sprite('Action_008_03', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    sprite('Action_008_04', 9)	# 13-21
    Recovery()
    Unknown2063()
    sprite('Action_008_05', 8)	# 22-29
    sprite('Action_008_06', 10)	# 30-39

@State
def AN_NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Flying_Start')
    sprite('Action_007_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_007_01', 3)	# 4-6
    Unknown7007('756d653130305f30000000000000000064000000756d653130305f31000000000000000064000000756d653130305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_007_02', 2)	# 7-8
    Unknown14070('Flying_Start')
    sprite('Action_007_03', 2)	# 9-10	 **attackbox here**
    SFX_3('SE041')
    GFX_0('Mer_082', -1)
    sprite('Action_007_04', 4)	# 11-14
    Recovery()
    Unknown2063()
    sprite('Action_007_05', 5)	# 15-19
    sprite('Action_007_06', 4)	# 20-23
    sprite('Action_007_07', 4)	# 24-27

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('Flying_Start')
    sprite('Action_009_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_009_01', 4)	# 5-8
    Unknown7007('756d653130345f30000000000000000064000000756d653130345f31000000000000000064000000756d653130345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_009_02', 3)	# 9-11
    sprite('Action_009_03', 2)	# 12-13
    sprite('Action_009_04', 1)	# 14-14
    SFX_3('SE043')
    GFX_0('Mer_077', -1)
    Unknown14070('Flying_Start')
    sprite('Action_009_05', 1)	# 15-15	 **attackbox here**
    sprite('Action_009_06', 3)	# 16-18	 **attackbox here**
    sprite('Action_009_07', 8)	# 19-26
    Recovery()
    Unknown2063()
    sprite('Action_009_08', 5)	# 27-31
    sprite('Action_009_09', 4)	# 32-35
    sprite('Action_009_10', 4)	# 36-39
    sprite('Action_009_11', 3)	# 40-42

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        PushbackX(12000)
        AirPushbackX(20000)
        AirPushbackY(-50000)
        AirUntechableTime(40)
        Unknown11065(1)
        Unknown9310(1)
        GroundedHitstunAnimation(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown1017()
        Unknown1022()
        Unknown1032()
        Unknown1037()

        def upon_STATE_END():
            Unknown1018()
            Unknown1023()
            Unknown1033()
            Unknown1038()
    sprite('Action_098_00', 4)	# 1-4	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(-6000)
    physicsYImpulse(12000)
    sprite('Action_098_01', 6)	# 5-10
    clearUponHandler(1)
    Unknown7007('756d653330345f30000000000000000064000000756d653330345f31000000000000000064000000756d653330365f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_098_02', 3)	# 11-13	 **attackbox here**
    SFX_3('SE043')
    GFX_0('Mer_086', -1)
    StartMultihit()
    Unknown1084(1)
    sprite('Action_098_03', 3)	# 14-16	 **attackbox here**
    physicsXImpulse(30000)
    physicsYImpulse(-45000)
    Unknown1028(600)
    setGravity(900)
    sprite('Action_098_04', 3)	# 17-19	 **attackbox here**
    label(0)
    sprite('Action_098_03', 3)	# 20-22	 **attackbox here**
    sprite('Action_098_04', 3)	# 23-25	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_098_05', 10)	# 26-35
    Recovery()
    Unknown2063()
    Unknown26('Mer_086')
    GFX_0('Mer_087', -1)
    physicsXImpulse(10000)
    Unknown1028(-1000)
    Unknown8000(100, 1, 1)

    def upon_3():
        if (not SLOT_12):
            Unknown1084(1)
            clearUponHandler(3)
    sprite('Action_098_06', 6)	# 36-41
    sprite('Action_098_07', 6)	# 42-47
    Unknown1084(1)

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
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_068_03', 3)	# 8-10
    tag_voice(1, 'ume156_0', 'ume156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 3)	# 14-16
    sprite('Action_068_06', 2)	# 17-18
    sprite('Action_007_00', 2)	# 19-20	 **attackbox here**
    sprite('Action_007_01', 3)	# 21-23
    sprite('Action_007_02', 2)	# 24-25
    sprite('Action_007_03ex', 3)	# 26-28	 **attackbox here**
    SFX_3('SE041')
    GFX_0('Mer_082', -1)
    sprite('Action_007_04', 4)	# 29-32
    sprite('Action_007_05', 5)	# 33-37
    sprite('Action_007_06', 4)	# 38-41
    sprite('Action_007_07', 4)	# 42-45
    label(0)
    sprite('Action_236_15', 3)	# 46-48	 **attackbox here**
    sprite('Action_236_16', 3)	# 49-51	 **attackbox here**
    sprite('Action_236_17', 3)	# 52-54	 **attackbox here**
    sprite('Action_236_18', 3)	# 55-57	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 2)	# 58-59	 **attackbox here**
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_021_01', 3)	# 60-62
    sprite('Action_021_02', 3)	# 63-65
    sprite('Action_021_03', 2)	# 66-67
    sprite('Action_021_04', 3)	# 68-70

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 18)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_007_04', 4)	# 1-4
    sprite('Action_007_05', 5)	# 5-9
    sprite('Action_007_06', 4)	# 10-13
    sprite('Action_007_07', 4)	# 14-17
    label(0)
    sprite('Action_236_15', 3)	# 18-20	 **attackbox here**
    sprite('Action_236_16', 3)	# 21-23	 **attackbox here**
    sprite('Action_236_17', 3)	# 24-26	 **attackbox here**
    sprite('Action_236_18', 3)	# 27-29	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 2)	# 30-31	 **attackbox here**
    Unknown1084(1)
    clearUponHandler(2)
    sprite('Action_021_01', 3)	# 32-34
    sprite('Action_021_02', 3)	# 35-37
    sprite('Action_021_03', 2)	# 38-39
    sprite('Action_021_04', 5)	# 40-44
    label(2)
    sprite('Action_005_00', 3)	# 45-47
    sprite('Action_005_01', 2)	# 48-49
    SFX_3('SE042')
    sprite('Action_005_02', 2)	# 50-51	 **attackbox here**
    StartMultihit()
    sprite('Action_005_03', 2)	# 52-53
    tag_voice(1, 'ume157_0', 'ume157_1', '', '')
    sprite('Action_005_04', 2)	# 54-55
    sprite('Action_005_05', 4)	# 56-59	 **attackbox here**
    sprite('Action_005_06', 7)	# 60-66
    sprite('Action_005_07', 7)	# 67-73
    sprite('Action_013_00', 1)	# 74-74
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    sprite('Action_013_01', 4)	# 75-78
    sprite('Action_013_02', 4)	# 79-82
    sprite('Action_013_03', 4)	# 83-86
    sprite('Action_013_04', 4)	# 87-90
    sprite('Action_013_05', 4)	# 91-94
    sprite('Action_013_06', 4)	# 95-98
    sprite('Action_013_07', 4)	# 99-102
    sprite('Action_013_08', 4)	# 103-106
    sprite('Action_013_09', 4)	# 107-110
    sprite('Action_013_10', 4)	# 111-114
    sprite('Action_013_11', 4)	# 115-118
    sprite('Action_013_12', 4)	# 119-122
    sprite('Action_013_13', 4)	# 123-126
    sprite('Action_013_14', 4)	# 127-130
    sprite('Action_013_15', 4)	# 131-134
    loopRest()
    label(10)
    sprite('Action_013_00', 2)	# 135-136
    sprite('Action_013_01', 4)	# 137-140
    sprite('Action_013_02', 4)	# 141-144
    sprite('Action_013_03', 4)	# 145-148
    sprite('Action_013_04', 4)	# 149-152
    sprite('Action_013_05', 4)	# 153-156
    sprite('Action_013_06', 4)	# 157-160
    sprite('Action_013_07', 4)	# 161-164
    sprite('Action_013_08', 4)	# 165-168
    sprite('Action_013_09', 4)	# 169-172
    sprite('Action_013_10', 4)	# 173-176
    sprite('Action_013_11', 4)	# 177-180
    sprite('Action_013_12', 4)	# 181-184
    sprite('Action_013_13', 4)	# 185-188
    sprite('Action_013_14', 4)	# 189-192
    sprite('Action_013_15', 4)	# 193-196
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 197-197

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_132_00', 6)	# 1-6
    sprite('Action_132_01', 6)	# 7-12
    sprite('Action_132_02', 2)	# 13-14	 **attackbox here**
    SFX_3('SE042')
    sprite('Action_132_03', 3)	# 15-17	 **attackbox here**
    sprite('Action_132_04', 8)	# 18-25	 **attackbox here**
    sprite('Action_039_00', 4)	# 26-29
    sprite('Action_039_01', 2)	# 30-31
    sprite('Action_039_02', 3)	# 32-34
    physicsYImpulse(32500)
    Unknown1043()
    sprite('Action_145_00', 4)	# 35-38	 **attackbox here**
    Unknown1084(1)
    sprite('Action_145_01', 6)	# 39-44
    sprite('Action_145_02', 4)	# 45-48
    sprite('Action_145_03', 3)	# 49-51	 **attackbox here**
    sprite('Action_145_04', 6)	# 52-57	 **attackbox here**
    sprite('Action_145_05', 6)	# 58-63	 **attackbox here**
    sprite('Action_145_06', 4)	# 64-67	 **attackbox here**
    label(0)
    sprite('Action_145_00', 4)	# 68-71	 **attackbox here**
    sprite('Action_145_01', 6)	# 72-77
    sprite('Action_145_02', 4)	# 78-81
    sprite('Action_145_03', 3)	# 82-84	 **attackbox here**
    sprite('Action_145_04', 6)	# 85-90	 **attackbox here**
    sprite('Action_145_05', 6)	# 91-96	 **attackbox here**
    sprite('Action_145_06', 4)	# 97-100	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 101-101

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown11032('ffffffffffffffff00093d00c0f2fcff')
    sprite('Action_009_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_009_01', 5)	# 6-10
    sprite('Action_009_02', 4)	# 11-14
    tag_voice(0, 'ume158_0', 'ume158_1', '', '')
    sprite('Action_009_03', 3)	# 15-17
    sprite('Action_009_04', 1)	# 18-18
    sprite('Action_009_04', 1)	# 19-19
    SFX_3('SE043')
    GFX_0('Mer_077', -1)
    sprite('Action_009_05', 1)	# 20-20	 **attackbox here**
    sprite('Action_009_06', 3)	# 21-23	 **attackbox here**
    setGravity(500)
    Unknown2003(1)
    sprite('Action_009_07', 8)	# 24-31
    sprite('Action_009_08', 5)	# 32-36
    sprite('Action_009_09', 2)	# 37-38
    sprite('Action_009_10', 4)	# 39-42
    sprite('Action_009_11', 3)	# 43-45
    sprite('Action_021_00', 2)	# 46-47	 **attackbox here**
    sprite('Action_021_01', 3)	# 48-50
    sprite('Action_021_02', 3)	# 51-53
    sprite('Action_021_03', 3)	# 54-56
    sprite('Action_021_04', 5)	# 57-61

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        sendToLabelUpon(2, 1)
        Unknown23027()
        Unknown9016(1)
    sprite('null', 27)	# 1-27
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 28-28
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(300000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_147_01', 3)	# 29-31
    physicsXImpulse(46000)
    physicsYImpulse(-15000)
    setGravity(1000)
    sprite('Action_147_02', 5)	# 32-36
    sprite('Action_147_03', 5)	# 37-41
    sprite('Action_147_04', 6)	# 42-47	 **attackbox here**
    RefreshMultihit()
    sprite('Action_147_05', 6)	# 48-53	 **attackbox here**
    sprite('Action_147_06', 6)	# 54-59
    sprite('Action_147_07', 5)	# 60-64
    label(1)
    sprite('Action_147_08', 5)	# 65-69	 **attackbox here**
    Unknown1084(1)
    sprite('Action_147_09', 3)	# 70-72
    sprite('Action_147_10', 3)	# 73-75
    sprite('Action_147_11', 3)	# 76-78
    sprite('Action_147_12', 2)	# 79-80
    sprite('Action_000_01', 5)	# 81-85
    sprite('Action_000_02', 5)	# 86-90
    sprite('Action_000_03', 5)	# 91-95
    sprite('Action_000_04', 5)	# 96-100
    sprite('Action_000_05', 5)	# 101-105
    sprite('Action_000_06', 5)	# 106-110
    sprite('Action_000_07', 5)	# 111-115
    sprite('Action_000_08', 5)	# 116-120
    sprite('Action_000_09', 5)	# 121-125
    sprite('Action_000_10', 5)	# 126-130
    sprite('Action_000_11', 5)	# 131-135
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('Action_101_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_101_01', 4)	# 6-9
    sprite('Action_101_02', 2)	# 10-11
    sprite('Action_101_03', 2)	# 12-13	 **attackbox here**
    SFX_3('SE042')
    GFX_0('Mer_088', -1)
    sprite('Action_101_04', 3)	# 14-16	 **attackbox here**
    Unknown2003(1)
    sprite('Action_039_00', 4)	# 17-20
    sprite('Action_039_01', 2)	# 21-22
    sprite('Action_039_02', 3)	# 23-25
    physicsYImpulse(32500)
    Unknown1043()
    sprite('Action_145_00', 4)	# 26-29	 **attackbox here**
    Unknown1084(1)
    sprite('Action_145_01', 6)	# 30-35
    sprite('Action_145_02', 4)	# 36-39
    sprite('Action_145_03', 3)	# 40-42	 **attackbox here**
    sprite('Action_145_04', 6)	# 43-48	 **attackbox here**
    sprite('Action_145_05', 6)	# 49-54	 **attackbox here**
    sprite('Action_145_06', 4)	# 55-58	 **attackbox here**
    label(0)
    sprite('Action_145_00', 4)	# 59-62	 **attackbox here**
    sprite('Action_145_01', 6)	# 63-68
    sprite('Action_145_02', 4)	# 69-72
    sprite('Action_145_03', 3)	# 73-75	 **attackbox here**
    sprite('Action_145_04', 6)	# 76-81	 **attackbox here**
    sprite('Action_145_05', 6)	# 82-87	 **attackbox here**
    sprite('Action_145_06', 4)	# 88-91	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 92-92

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown11032('ffffffffffffffff00093d00c0f2fcff')
    sprite('Action_009_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_009_01', 5)	# 6-10
    sprite('Action_009_02', 4)	# 11-14
    sprite('Action_009_03', 3)	# 15-17
    sprite('Action_009_04', 1)	# 18-18
    sprite('Action_009_04', 1)	# 19-19
    SFX_3('SE043')
    GFX_0('Mer_077', -1)
    sprite('Action_009_05', 1)	# 20-20	 **attackbox here**
    sprite('Action_009_06', 3)	# 21-23	 **attackbox here**
    Unknown2003(1)
    setGravity(500)
    sprite('Action_009_07', 8)	# 24-31
    sprite('Action_009_08', 5)	# 32-36
    sprite('Action_009_09', 2)	# 37-38
    sprite('Action_009_10', 4)	# 39-42
    sprite('Action_009_11', 3)	# 43-45
    sprite('Action_021_00', 2)	# 46-47	 **attackbox here**
    sprite('Action_021_01', 3)	# 48-50
    sprite('Action_021_02', 3)	# 51-53
    sprite('Action_021_03', 3)	# 54-56
    sprite('Action_021_04', 5)	# 57-61

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
                if (SLOT_19 <= 180000):
                    sendToLabel(1)
    sprite('Action_010_00', 6)	# 1-6
    sprite('Action_010_01', 6)	# 7-12
    label(0)
    sprite('Action_045_01', 1)	# 13-13
    sprite('Action_045_02', 1)	# 14-14
    sprite('Action_045_03', 1)	# 15-15
    sprite('Action_045_04', 1)	# 16-16
    sprite('Action_045_05', 1)	# 17-17
    sprite('Action_045_06', 1)	# 18-18
    sprite('Action_045_07', 1)	# 19-19
    sprite('Action_045_08', 1)	# 20-20
    sprite('Action_045_09', 1)	# 21-21
    sprite('Action_045_10', 1)	# 22-22
    sprite('Action_045_11', 1)	# 23-23
    sprite('Action_045_12', 1)	# 24-24
    sprite('Action_045_13', 1)	# 25-25
    sprite('Action_045_14', 1)	# 26-26
    sprite('Action_045_15', 1)	# 27-27
    sprite('Action_045_16', 1)	# 28-28
    sprite('Action_045_17', 1)	# 29-29
    sprite('Action_045_18', 1)	# 30-30
    sprite('Action_045_19', 1)	# 31-31
    sprite('Action_045_20', 1)	# 32-32
    sprite('Action_045_21', 1)	# 33-33
    sprite('Action_045_22', 1)	# 34-34
    sprite('Action_045_23', 1)	# 35-35
    sprite('Action_045_24', 1)	# 36-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 37-39
    clearUponHandler(3)
    Unknown1084(1)
    sprite('Action_055_01', 3)	# 40-42	 **attackbox here**
    SFX_0('010_swing_sword_0')
    sprite('Action_055_02', 2)	# 43-44
    SFX_4('ume154')
    sprite('Action_055_03', 4)	# 45-48
    sprite('Action_055_04', 4)	# 49-52
    sprite('Action_055_05', 4)	# 53-56
    sprite('Action_055_06', 3)	# 57-59
    sprite('Action_055_07', 3)	# 60-62
    sprite('Action_055_08', 3)	# 63-65

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(500)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP2(50)
        Unknown11092(1)
        AirPushbackX(15000)
        AirPushbackY(20000)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown9310(20)
        Unknown20000(1)
        JumpCancel_(0)
        Unknown11064(1)
        Unknown2034(0)

        def upon_STATE_END():
            Unknown2034(1)
    sprite('Action_057_00', 2)	# 1-2
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_01', 2)	# 3-4
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 2)	# 5-6
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 2)	# 7-8
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume153')
    sprite('Action_057_05', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 8000)
    Unknown30079(1)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 6)	# 12-17	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_07', 3)	# 18-20	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_01', 2)	# 21-22
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 2)	# 23-24
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 2)	# 25-26
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume153')
    sprite('Action_057_05', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 8000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 6)	# 30-35	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 3)	# 36-38	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_01', 2)	# 39-40
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 2)	# 41-42
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 2)	# 43-44
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume153')
    sprite('Action_057_05', 3)	# 45-47	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 8000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 6)	# 48-53	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 3)	# 54-56	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_09', 5)	# 57-61
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_10', 4)	# 62-65
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_11', 4)	# 66-69
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume105_1')
    sprite('Action_057_12', 2)	# 70-71	 **attackbox here**
    RefreshMultihit()
    Unknown30079(0)
    Unknown11072(1, 450000, 400000)
    Unknown20000(0)
    JumpCancel_(1)
    Unknown11064(0)
    Unknown9016(1)
    sprite('Action_057_13', 6)	# 72-77
    sprite('Action_057_14', 7)	# 78-84
    sprite('Action_057_15', 3)	# 85-87
    sprite('Action_057_16', 4)	# 88-91
    sprite('Action_057_17', 5)	# 92-96

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
    sprite('Action_010_00', 6)	# 1-6
    sprite('Action_010_01', 6)	# 7-12
    label(0)
    sprite('Action_045_01', 1)	# 13-13
    sprite('Action_045_02', 1)	# 14-14
    sprite('Action_045_03', 1)	# 15-15
    sprite('Action_045_04', 1)	# 16-16
    sprite('Action_045_05', 1)	# 17-17
    sprite('Action_045_06', 1)	# 18-18
    sprite('Action_045_07', 1)	# 19-19
    sprite('Action_045_08', 1)	# 20-20
    sprite('Action_045_09', 1)	# 21-21
    sprite('Action_045_10', 1)	# 22-22
    sprite('Action_045_11', 1)	# 23-23
    sprite('Action_045_12', 1)	# 24-24
    sprite('Action_045_13', 1)	# 25-25
    sprite('Action_045_14', 1)	# 26-26
    sprite('Action_045_15', 1)	# 27-27
    sprite('Action_045_16', 1)	# 28-28
    sprite('Action_045_17', 1)	# 29-29
    sprite('Action_045_18', 1)	# 30-30
    sprite('Action_045_19', 1)	# 31-31
    sprite('Action_045_20', 1)	# 32-32
    sprite('Action_045_21', 1)	# 33-33
    sprite('Action_045_22', 1)	# 34-34
    sprite('Action_045_23', 1)	# 35-35
    sprite('Action_045_24', 1)	# 36-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 37-39
    clearUponHandler(3)
    Unknown1084(1)
    sprite('Action_055_01', 3)	# 40-42	 **attackbox here**
    SFX_0('010_swing_sword_0')
    sprite('Action_055_02', 2)	# 43-44
    SFX_4('ume154')
    sprite('Action_055_03', 4)	# 45-48
    sprite('Action_055_04', 4)	# 49-52
    sprite('Action_055_05', 4)	# 53-56
    sprite('Action_055_06', 3)	# 57-59
    sprite('Action_055_07', 3)	# 60-62
    sprite('Action_055_08', 3)	# 63-65

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(300)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP2(50)
        Unknown11092(1)
        AirPushbackX(15000)
        AirPushbackY(20000)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown9310(20)
        Unknown20000(1)
        JumpCancel_(0)
        Unknown11064(1)
        Unknown2034(0)

        def upon_STATE_END():
            Unknown2034(1)
    sprite('Action_057_00', 2)	# 1-2
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_01', 1)	# 3-3
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 1)	# 4-4
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 1)	# 5-5
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume153')
    sprite('Action_057_05', 2)	# 6-7	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 5000)
    Unknown30079(1)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 4)	# 8-11	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_07', 2)	# 12-13	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_01', 1)	# 14-14
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 1)	# 15-15
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 1)	# 16-16
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 5000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 4)	# 19-22	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 2)	# 23-24	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_01', 1)	# 25-25
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 1)	# 26-26
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 1)	# 27-27
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume107_1')
    sprite('Action_057_05', 2)	# 28-29	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 5000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 4)	# 30-33	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 2)	# 34-35	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_01', 1)	# 36-36
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 1)	# 37-37
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 1)	# 38-38
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_05', 2)	# 39-40	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 5000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 4)	# 41-44	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 2)	# 45-46	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_01', 1)	# 47-47
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 1)	# 48-48
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 1)	# 49-49
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume107_1')
    sprite('Action_057_05', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 5000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 4)	# 52-55	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 2)	# 56-57	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_01', 1)	# 58-58
    teleportRelativeX(90000)
    Unknown2005()
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_02', 1)	# 59-59
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 1)	# 60-60
    Unknown5000(16, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_05', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    ScreenShake(5000, 5000)
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    GFX_0('Mer_073', 0)
    sprite('Action_057_06', 6)	# 63-68	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_07', 3)	# 69-71	 **attackbox here**
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000008000000')
    sprite('Action_057_09', 5)	# 72-76
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_10', 4)	# 77-80
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_11', 4)	# 81-84
    Unknown5000(14, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_1('ume105_1')
    sprite('Action_057_12', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    Damage(200)
    Unknown30079(0)
    Unknown11072(1, 450000, 400000)
    Unknown20000(0)
    JumpCancel_(1)
    Unknown11064(0)
    Unknown9016(1)
    sprite('Action_057_13', 6)	# 87-92
    sprite('Action_057_14', 7)	# 93-99
    sprite('Action_057_15', 3)	# 100-102
    sprite('Action_057_16', 4)	# 103-106
    sprite('Action_057_17', 5)	# 107-111

@State
def RushA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(400)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        AirPushbackX(20000)
        AirPushbackY(15000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        Hitstop(2)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('Action_110_00', 3)	# 1-3
    sprite('Action_110_01', 3)	# 4-6
    sprite('Action_110_02', 3)	# 7-9
    Unknown7007('756d653230305f30000000000000000064000000756d653230305f31000000000000000064000000756d653230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_110_03', 3)	# 10-12
    sprite('Action_110_04', 2)	# 13-14	 **attackbox here**
    Unknown12046(100)
    RefreshMultihit()
    SFX_3('SE041')
    sprite('Action_110_05', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_06', 2)	# 17-18	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_07', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_08', 2)	# 21-22	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_09', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_10', 2)	# 25-26	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_11', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_12', 3)	# 29-31
    Recovery()
    Unknown12046(0)
    sprite('Action_110_13', 4)	# 32-35
    sprite('Action_110_14', 3)	# 36-38
    sprite('Action_110_15', 3)	# 39-41
    sprite('Action_110_16', 3)	# 42-44
    sprite('Action_110_17', 3)	# 45-47

@State
def RushB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(450)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        Hitstop(2)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('Action_110_00', 4)	# 1-4
    sprite('Action_110_01', 4)	# 5-8
    sprite('Action_110_02', 4)	# 9-12
    Unknown7007('756d653230305f30000000000000000064000000756d653230305f31000000000000000064000000756d653230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_110_03', 4)	# 13-16
    sprite('Action_110_04', 2)	# 17-18	 **attackbox here**
    physicsXImpulse(30000)
    Unknown12046(100)
    RefreshMultihit()
    SFX_3('SE041')
    sprite('Action_110_05', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_06', 2)	# 21-22	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_07', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_08', 2)	# 25-26	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_09', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_10', 2)	# 29-30	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_11', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_12', 3)	# 33-35
    Recovery()
    Unknown1019(60)
    Unknown12046(0)
    sprite('Action_110_13', 8)	# 36-43
    Unknown1084(1)
    sprite('Action_110_14', 5)	# 44-48
    sprite('Action_110_15', 5)	# 49-53
    sprite('Action_110_16', 5)	# 54-58
    sprite('Action_110_17', 5)	# 59-63

@State
def Rush_Ex():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(350)
        AttackP1(80)
        AttackP2(80)
        Unknown11092(1)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown11091(10)
        Unknown30065(0)

        def upon_STATE_END():
            Unknown12046(0)
    sprite('Action_110_00', 3)	# 1-3
    sprite('Action_110_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_110_02', 3)	# 7-9
    Unknown7007('756d653230315f30000000000000000064000000756d653230315f31000000000000000064000000756d653230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_110_03', 3)	# 10-12
    sprite('Action_110_04', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(40000)
    Unknown12046(100)
    RefreshMultihit()
    SFX_3('SE041')
    sprite('Action_110_05', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_06', 2)	# 17-18	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_07', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_08', 2)	# 21-22	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_09', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_10', 2)	# 25-26	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_11', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_04', 2)	# 29-30	 **attackbox here**
    Unknown1019(60)
    RefreshMultihit()
    SFX_3('SE041')
    sprite('Action_110_05', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_06', 2)	# 33-34	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_07', 2)	# 35-36	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_08', 2)	# 37-38	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_09', 2)	# 39-40	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_10', 2)	# 41-42	 **attackbox here**
    Unknown1019(60)
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_110_11', 2)	# 43-44	 **attackbox here**
    RefreshMultihit()
    sprite('Action_110_12', 3)	# 45-47
    Recovery()
    Unknown1019(60)
    Unknown12046(0)
    sprite('Action_110_13', 6)	# 48-53
    Unknown1084(1)
    sprite('Action_110_14', 4)	# 54-57
    sprite('Action_110_15', 4)	# 58-61
    sprite('Action_110_16', 4)	# 62-65
    sprite('Action_110_17', 4)	# 66-69

@State
def CaptureA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11044(1)
        Unknown28(78, 'CaptureAPlus')
        Unknown11064(1)
        Unknown11057(0)
        Unknown2073(1)

        def upon_78():
            GFX_0('Mer_071', 0)
    sprite('Action_281_00', 3)	# 1-3
    sprite('Action_281_00', 3)	# 4-6
    Unknown7007('756d653230345f30000000000000000064000000756d653230345f31000000000000000064000000756d653230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_281_01', 6)	# 7-12
    sprite('Action_281_02', 2)	# 13-14
    SFX_3('SE042')
    GFX_0('Mer_096', 0)
    sprite('Action_281_06', 2)	# 15-16	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(0)
    sprite('Action_281_11', 2)	# 17-18	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(1)
    sprite('Action_281_16', 2)	# 19-20	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(2)
    sprite('Action_281_21', 2)	# 21-22	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(3)
    sprite('Action_281_26', 2)	# 23-24	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(4)
    sprite('Action_281_31', 2)	# 25-26	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(5)
    sprite('Action_281_36', 2)	# 27-28	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(6)
    sprite('Action_281_38', 3)	# 29-31	 **attackbox here**
    clearUponHandler(80)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    sprite('Action_281_39', 4)	# 32-35	 **attackbox here**
    sprite('Action_281_40', 4)	# 36-39	 **attackbox here**
    sprite('Action_281_41', 4)	# 40-43	 **attackbox here**
    sprite('Action_281_42', 4)	# 44-47	 **attackbox here**
    sprite('Action_281_43', 4)	# 48-51	 **attackbox here**
    label(6)
    sprite('Action_281_37', 1)	# 52-52	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(5)
    sprite('Action_281_32', 1)	# 53-53	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(4)
    sprite('Action_281_27', 1)	# 54-54	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(3)
    sprite('Action_281_22', 1)	# 55-55	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(2)
    sprite('Action_281_17', 1)	# 56-56	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(1)
    sprite('Action_281_12', 1)	# 57-57	 **attackbox here**
    Recovery()
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Unknown23027()
    label(0)
    sprite('Action_281_07', 1)	# 58-58	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(9)
    sprite('Action_281_44', 6)	# 59-64
    sprite('Action_281_45', 5)	# 65-69
    sprite('Action_281_46', 5)	# 70-74

@State
def CaptureAPlus():

    def upon_IMMEDIATE():
        Unknown17011('CaptureExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11045(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11064(1)
        Unknown11023(1)
        Unknown20007(1)
        Unknown11044(1)
        Unknown30048(1)
        Unknown30068(1)
    sprite('keep', 1)	# 1-1
    sprite('Action_281_44', 6)	# 2-7
    Recovery()
    sprite('Action_281_45', 5)	# 8-12
    sprite('Action_281_46', 5)	# 13-17

@State
def CaptureB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11046(1)
        Unknown11044(1)
        Unknown28(78, 'CaptureBPlus')
        Unknown11064(1)
        Unknown11057(0)
        Unknown2073(1)

        def upon_78():
            GFX_0('Mer_071', 0)
    sprite('Action_282_00', 3)	# 1-3
    sprite('Action_282_00', 3)	# 4-6
    Unknown7007('756d653230345f30000000000000000064000000756d653230345f31000000000000000064000000756d653230345f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_282_01', 6)	# 7-12
    sprite('Action_282_02', 2)	# 13-14
    SFX_3('SE042')
    GFX_0('Mer_096', 0)
    Unknown36(1)
    Unknown1072(-22000)
    Unknown35()
    sprite('Action_282_06', 1)	# 15-15	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(0)
    sprite('Action_282_11', 1)	# 16-16	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(1)
    sprite('Action_282_16', 1)	# 17-17	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(2)
    sprite('Action_282_21', 1)	# 18-18	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(3)
    sprite('Action_282_26', 1)	# 19-19	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(4)
    sprite('Action_282_31', 1)	# 20-20	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(5)
    sprite('Action_282_36', 1)	# 21-21	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(6)
    sprite('Action_282_38', 3)	# 22-24	 **attackbox here**
    clearUponHandler(80)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    sprite('Action_282_39', 3)	# 25-27	 **attackbox here**
    sprite('Action_282_40', 3)	# 28-30	 **attackbox here**
    sprite('Action_282_41', 3)	# 31-33	 **attackbox here**
    sprite('Action_282_42', 3)	# 34-36	 **attackbox here**
    sprite('Action_282_43', 3)	# 37-39	 **attackbox here**
    label(6)
    sprite('Action_282_37', 1)	# 40-40	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(5)
    sprite('Action_282_32', 1)	# 41-41	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(4)
    sprite('Action_282_27', 1)	# 42-42	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(3)
    sprite('Action_282_22', 1)	# 43-43	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(2)
    sprite('Action_282_17', 1)	# 44-44	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(1)
    sprite('Action_282_12', 1)	# 45-45	 **attackbox here**
    Recovery()
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Unknown23027()
    label(0)
    sprite('Action_282_07', 1)	# 46-46	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(9)
    sprite('Action_282_44', 4)	# 47-50
    sprite('Action_282_45', 3)	# 51-53
    sprite('Action_282_46', 3)	# 54-56

@State
def CaptureBPlus():

    def upon_IMMEDIATE():
        Unknown17011('CaptureExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11045(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11064(1)
        Unknown11023(1)
        Unknown20007(1)
        Unknown11044(1)
        Unknown30048(1)
        Unknown30068(1)
    sprite('keep', 1)	# 1-1
    sprite('Action_282_44', 6)	# 2-7
    Recovery()
    sprite('Action_282_45', 5)	# 8-12
    sprite('Action_282_46', 5)	# 13-17

@State
def Capture_Ex():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(80)
        Unknown11044(1)
        Unknown11091(10)
        Unknown30065(0)
        Unknown28(78, 'CaptureEXPlus')
        Unknown11064(1)
        Unknown11057(0)
        Unknown2073(1)

        def upon_78():
            GFX_0('Mer_071', 0)
    sprite('Action_281_00', 3)	# 1-3
    sprite('Action_281_00', 3)	# 4-6
    Unknown7007('756d653230345f30000000000000000064000000756d653230345f31000000000000000064000000756d653230345f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_281_01', 6)	# 7-12
    sprite('Action_281_02', 2)	# 13-14
    SFX_3('SE042')
    GFX_0('Mer_096', 0)
    sprite('Action_281_06', 1)	# 15-15	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(0)
    sprite('Action_281_11', 1)	# 16-16	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(1)
    sprite('Action_281_16', 1)	# 17-17	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(2)
    sprite('Action_281_21', 1)	# 18-18	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(3)
    sprite('Action_281_26', 1)	# 19-19	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(4)
    sprite('Action_281_31', 1)	# 20-20	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(5)
    sprite('Action_281_36', 1)	# 21-21	 **attackbox here**

    def upon_80():
        clearUponHandler(80)
        Unknown2037(1)
        sendToLabel(6)
    sprite('Action_281_38', 3)	# 22-24	 **attackbox here**
    clearUponHandler(80)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    sprite('Action_281_39', 4)	# 25-28	 **attackbox here**
    sprite('Action_281_40', 4)	# 29-32	 **attackbox here**
    sprite('Action_281_41', 4)	# 33-36	 **attackbox here**
    sprite('Action_281_42', 4)	# 37-40	 **attackbox here**
    sprite('Action_281_43', 4)	# 41-44	 **attackbox here**
    label(6)
    sprite('Action_281_37', 1)	# 45-45	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(5)
    sprite('Action_281_32', 1)	# 46-46	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(4)
    sprite('Action_281_27', 1)	# 47-47	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(3)
    sprite('Action_281_22', 1)	# 48-48	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(2)
    sprite('Action_281_17', 1)	# 49-49	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(1)
    sprite('Action_281_12', 1)	# 50-50	 **attackbox here**
    Recovery()
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Unknown23027()
    label(0)
    sprite('Action_281_07', 1)	# 51-51	 **attackbox here**
    Unknown20(10, 2, 2)
    Unknown2037(0)
    Recovery()
    Unknown23027()
    label(9)
    sprite('Action_281_44', 6)	# 52-57
    sprite('Action_281_45', 5)	# 58-62
    sprite('Action_281_46', 5)	# 63-67

@State
def CaptureEXPlus():

    def upon_IMMEDIATE():
        Unknown17011('CaptureExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11045(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11064(1)
        Unknown11023(1)
        Unknown20007(1)
        Unknown11044(1)
        Unknown30048(1)
        Unknown11091(10)
        Unknown30065(0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
        Unknown30068(1)
    sprite('keep', 1)	# 1-1
    sprite('Action_283_44', 5)	# 2-6
    Recovery()
    sprite('Action_283_45', 4)	# 7-10
    sprite('Action_283_46', 4)	# 11-14

@State
def CaptureExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(500)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AttackP2(100)
        AirPushbackX(1000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Hitstop(2)
        Unknown30079(1)
        Unknown11064(1)
        Unknown11091(5)
        Unknown30048(1)
        Unknown1086(22)
        teleportRelativeX(-100000)
        Unknown1007(300000)
        Unknown20007(1)
        if Unknown23145('CaptureEXPlus'):
            Damage(500)
            Unknown11091(10)
            Unknown30065(0)
            Unknown2037(2)
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)

        def upon_LANDING():
            sendToLabel(9)
        Unknown11050('080000000000000000000000000000000000000000000000000000000000000000000000')

        def upon_78():
            GFX_0('Mer_071', 0)
    sprite('Action_234_00', 2)	# 1-2
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_00', 3)	# 3-5	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_01', 3)	# 6-8	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_02', 3)	# 9-11	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_03', 3)	# 12-14	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_04', 3)	# 15-17	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(0)
    sprite('Action_236_05', 5)	# 18-22	 **attackbox here**
    ScreenShake(3000, 3000)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    SFX_3('SE008')
    sprite('Action_236_03', 3)	# 23-25	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_04', 2)	# 26-27	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_04', 1)	# 28-28	 **attackbox here**
    if SLOT_2:
        Unknown2038(-1)
        sendToLabel(0)
    sprite('Action_236_05', 7)	# 29-35	 **attackbox here**
    ScreenShake(3000, 3000)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    SFX_3('SE008')
    sprite('Action_236_06', 2)	# 36-37	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_07', 3)	# 38-40	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_08', 3)	# 41-43	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_236_09', 3)	# 44-46	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown7007('756d653230355f30000000000000000064000000756d653230355f31000000000000000064000000756d653230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_236_10', 3)	# 47-49	 **attackbox here**
    ScreenShake(3000, 3000)
    Unknown5000(1, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Hitstop(12)
    Unknown11064(0)
    Unknown20007(0)
    Unknown1007(-200000)
    teleportRelativeX(-180000)
    Unknown11072(1, 250000, 0)
    Unknown30079(0)
    SFX_3('SE202_BladeC')
    clearUponHandler(78)

    def upon_78():
        GFX_0('Mer_071', 1)
    sprite('Action_236_11', 4)	# 50-53
    sprite('Action_236_12', 4)	# 54-57
    physicsXImpulse(-7000)
    physicsYImpulse(30000)
    setGravity(2500)
    sprite('Action_236_13', 4)	# 58-61
    sprite('Action_236_14', 4)	# 62-65
    label(1)
    sprite('Action_236_15', 3)	# 66-68	 **attackbox here**
    sprite('Action_236_16', 3)	# 69-71	 **attackbox here**
    sprite('Action_236_17', 3)	# 72-74	 **attackbox here**
    sprite('Action_236_18', 3)	# 75-77	 **attackbox here**
    gotoLabel(1)
    label(9)
    sprite('Action_021_00', 2)	# 78-79	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_021_01', 3)	# 80-82
    sprite('Action_021_02', 3)	# 83-85
    sprite('Action_021_03', 2)	# 86-87
    sprite('Action_021_04', 5)	# 88-92

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(8, 1)
    sprite('Action_174_00', 2)	# 1-2	 **attackbox here**
    Unknown1084(1)
    sprite('Action_174_01', 2)	# 3-4
    sprite('Action_174_02', 3)	# 5-7
    Unknown7007('756d653230365f30000000000000000064000000756d653230365f31000000000000000064000000756d653230365f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1007(50000)
    sprite('Action_174_03', 6)	# 8-13
    sprite('Action_174_04', 5)	# 14-18
    sprite('Action_174_05', 5)	# 19-23
    physicsXImpulse(-1250)
    physicsYImpulse(16000)
    Unknown1043()
    GFX_0('Atk_Shot_Mer_178', 0)
    GFX_0('Mer_179', 0)
    SFX_3('SE221')
    sprite('Action_174_06', 5)	# 24-28
    sprite('Action_174_07', 5)	# 29-33
    sprite('Action_174_08', 5)	# 34-38
    sprite('Action_174_09', 4)	# 39-42
    sprite('Action_174_10', 4)	# 43-46
    sprite('Action_174_11', 3)	# 47-49

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(4, 1)
    sprite('Action_175_00', 2)	# 1-2	 **attackbox here**
    Unknown1084(1)
    sprite('Action_175_01', 2)	# 3-4
    sprite('Action_175_02', 3)	# 5-7
    Unknown7007('756d653230365f30000000000000000064000000756d653230365f31000000000000000064000000756d653230365f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown1007(50000)
    sprite('Action_175_03', 10)	# 8-17
    sprite('Action_175_04', 5)	# 18-22
    sprite('Action_175_05', 5)	# 23-27
    physicsXImpulse(-1600)
    physicsYImpulse(18000)
    Unknown1043()
    GFX_0('Mer_179B', 0)
    GFX_0('Atk_Shot_Mer_178B', 0)
    SFX_3('SE221')
    sprite('Action_175_06', 5)	# 28-32
    sprite('Action_175_07', 5)	# 33-37
    sprite('Action_175_08', 5)	# 38-42
    sprite('Action_175_09', 4)	# 43-46
    sprite('Action_175_10', 4)	# 47-50
    sprite('Action_175_11', 3)	# 51-53

@State
def AirShot_Ex():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown22004(4, 1)
    sprite('Action_174_00', 2)	# 1-2	 **attackbox here**
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('Action_174_01', 1)	# 3-3
    sprite('Action_174_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('756d653230375f30000000000000000064000000756d653230375f31000000000000000064000000756d653230375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_174_02', 3)	# 5-7
    Unknown1007(50000)
    sprite('Action_175_03', 9)	# 8-16
    sprite('Action_174_04', 5)	# 17-21
    sprite('Action_174_05', 3)	# 22-24
    GFX_0('Atk_Shot_Mer_184_1', 0)
    GFX_0('Atk_Shot_Mer_184_2', 0)
    GFX_0('Atk_Shot_Mer_184_3', 0)
    GFX_0('Mer_179', 0)
    SFX_3('SE221')
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(60)
    YAccel(60)
    sprite('Action_174_06', 3)	# 25-27
    sprite('Action_174_07', 3)	# 28-30
    sprite('Action_174_08', 3)	# 31-33
    sprite('Action_174_09', 3)	# 34-36
    sprite('Action_174_10', 3)	# 37-39
    sprite('Action_174_11', 3)	# 40-42

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(500)
        Unknown11092(1)
        Hitstop(4)
        AirUntechableTime(40)
        AirPushbackX(15000)
        AirPushbackY(20000)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown11056(2)
        Unknown11110(85)

        def upon_LANDING():
            sendToLabel(1)
    sprite('Action_121_00', 4)	# 1-4
    Unknown1084(1)
    sprite('Action_121_01', 3)	# 5-7
    Unknown7007('756d653230325f30000000000000000064000000756d653230325f31000000000000000064000000756d653230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_121_02', 3)	# 8-10
    physicsXImpulse(5500)
    physicsYImpulse(30000)
    setGravity(2000)
    sprite('Action_121_03', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    Unknown30055('e09304005000000050000000')
    Unknown30056('204e00005000000050000000')
    sprite('Action_121_04', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_121_05', 2)	# 15-16	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_121_06', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('Action_121_07', 2)	# 19-20	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_121_08', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    sprite('Action_121_09', 2)	# 23-24	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_121_10', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    sprite('Action_121_11', 2)	# 27-28	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_121_12', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    Unknown30055('e09304000000000000000000')
    Unknown30056('204e00000000000000000000')
    sprite('Action_121_18', 3)	# 31-33
    sprite('Action_121_19', 3)	# 34-36
    sprite('Action_121_20', 3)	# 37-39
    label(0)
    sprite('Action_022_00', 3)	# 40-42	 **attackbox here**
    sprite('Action_022_01', 3)	# 43-45	 **attackbox here**
    sprite('Action_022_02', 3)	# 46-48	 **attackbox here**
    sprite('Action_022_03', 3)	# 49-51	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 3)	# 52-54	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_021_01', 4)	# 55-58
    sprite('Action_021_02', 4)	# 59-62
    sprite('Action_021_03', 9)	# 63-71
    sprite('Action_021_04', 6)	# 72-77

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(800)
        Unknown11092(1)
        Hitstop(4)
        AirUntechableTime(40)
        AirPushbackX(15000)
        AirPushbackY(20000)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown11056(2)
        clearUponHandler(2)

        def upon_LANDING():
            sendToLabel(1)
    sprite('Action_037_02', 4)	# 1-4
    Unknown1084(1)
    sprite('Action_037_04', 7)	# 5-11
    Unknown7007('756d653230335f30000000000000000064000000756d653230335f31000000000000000064000000756d653230335f320000000000000000640000000000000000000000000000000000000000000000')
    physicsXImpulse(5500)
    physicsYImpulse(15000)
    setGravity(2000)
    sprite('Action_120_03', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    Unknown30055('e09304005000000050000000')
    Unknown30056('204e00005000000050000000')
    sprite('Action_120_04', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_120_05', 2)	# 16-17	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    sprite('Action_120_06', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_120_07', 2)	# 20-21	 **attackbox here**
    SFX_3('SE041')
    RefreshMultihit()
    Unknown30055('e09304000000000000000000')
    Unknown30056('204e00000000000000000000')
    sprite('Action_120_08', 2)	# 22-23	 **attackbox here**
    StartMultihit()
    setInvincible(0)
    sprite('Action_120_09', 2)	# 24-25	 **attackbox here**
    StartMultihit()
    sprite('Action_120_10', 4)	# 26-29
    sprite('Action_120_11', 3)	# 30-32
    sprite('Action_120_12', 3)	# 33-35
    sprite('Action_120_13', 3)	# 36-38
    label(0)
    sprite('Action_022_00', 3)	# 39-41	 **attackbox here**
    sprite('Action_022_01', 3)	# 42-44	 **attackbox here**
    sprite('Action_022_02', 3)	# 45-47	 **attackbox here**
    sprite('Action_022_03', 3)	# 48-50	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 4)	# 51-54	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_021_01', 5)	# 55-59
    sprite('Action_021_02', 5)	# 60-64
    sprite('Action_021_03', 9)	# 65-73
    sprite('Action_021_04', 7)	# 74-80

@State
def UltimateCapture():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        AirPushbackX(10000)
        AirPushbackY(10000)
        Hitstop(4)
        AirHitstunAnimation(13)
        AirUntechableTime(80)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11064(1)
        Unknown11069('UltimateCapturePlus')
        Unknown11084(1)
        Unknown2073(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        Unknown1084(1)
        setInvincible(1)

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
            enterState('UltimateCapturePlus')
            Unknown1084(1)
    sprite('Action_190_00', 5)	# 1-5
    Unknown2036(24, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    physicsXImpulse(-3000)
    Unknown1028(100)
    physicsYImpulse(28000)
    Unknown1043()
    sprite('Action_190_01', 5)	# 6-10
    tag_voice(1, 'ume252_0', 'ume252_1', 'ume252_2', '')
    sprite('Action_190_02', 5)	# 11-15
    sprite('Action_190_03', 5)	# 16-20
    sprite('Action_190_04', 14)	# 21-34
    Unknown1084(1)
    sprite('Action_190_05', 2)	# 35-36	 **attackbox here**
    physicsXImpulse(50000)
    physicsYImpulse(-18000)
    Unknown1028(1500)
    Unknown1043()
    label(0)
    sprite('Action_190_06', 2)	# 37-38	 **attackbox here**
    setInvincible(0)
    sprite('Action_190_07', 2)	# 39-40	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_190_08', 17)	# 41-57
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    physicsXImpulse(30000)
    Unknown1028(-1500)

    def upon_3():
        if (not SLOT_12):
            Unknown1084(1)
            clearUponHandler(3)
    sprite('Action_190_09', 11)	# 58-68
    sprite('Action_190_10', 11)	# 69-79

@State
def UltimateCapturePlus():

    def upon_IMMEDIATE():
        Unknown17011('UltimateCaptureExe', 3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        Unknown30048(1)
        Unknown30061(0)
        Unknown11045(0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11064(1)
        Unknown11023(1)
        Unknown11044(1)
        Unknown13024(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    Unknown1084(1)
    label(0)
    sprite('Action_190_06', 2)	# 2-3	 **attackbox here**
    physicsXImpulse(50000)
    physicsYImpulse(-18000)
    setGravity(200)
    sprite('Action_190_07', 2)	# 4-5	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_190_08', 7)	# 6-12
    Unknown1084(1)
    physicsXImpulse(30000)
    Unknown1028(-1500)

    def upon_3():
        if (not SLOT_12):
            Unknown1084(1)
            clearUponHandler(3)
    sprite('Action_190_09', 9)	# 13-21
    sprite('Action_190_10', 9)	# 22-30

    @State
    def UltimateCaptureExe():

        def upon_IMMEDIATE():
            Unknown17012(3, 0, 0)
            Unknown23056('')
            AttackLevel_(4)
            Damage(400)
            AttackP2(100)
            Unknown11091(20)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            AirUntechableTime(100)
            AirPushbackX(15000)
            AirPushbackY(35000)
            Hitstop(1)
            Unknown30061(0)
            setInvincible(1)
            Unknown13024(0)
            Unknown11064(1)

            def upon_LANDING():
                clearUponHandler(2)
                sendToLabel(1)
            physicsXImpulse(50000)
            physicsYImpulse(-54000)
            Unknown1028(1500)
            Unknown1043()
            Unknown30079(1)
        label(0)
        sprite('Action_191_00', 1)	# 1-1
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        gotoLabel(0)
        label(1)
        sprite('Action_191_01', 2)	# 2-3
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown1028(-2000)
        sprite('Action_191_02', 2)	# 4-5
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(600)
        Unknown1064(600)
        Unknown35()
        sprite('Action_191_03', 2)	# 6-7	 **attackbox here**
        RefreshMultihit()
        ScreenShake(3500, 500)
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(450)
        Unknown1064(450)
        Unknown35()
        sprite('Action_191_03', 2)	# 8-9	 **attackbox here**
        RefreshMultihit()
        ScreenShake(3500, 500)
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(400)
        Unknown1064(400)
        Unknown35()
        sprite('Action_191_03', 2)	# 10-11	 **attackbox here**
        RefreshMultihit()
        ScreenShake(3500, 500)
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(350)
        Unknown1064(350)
        Unknown35()
        sprite('Action_191_03', 2)	# 12-13	 **attackbox here**
        RefreshMultihit()
        ScreenShake(3500, 500)
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(300)
        Unknown1064(300)
        Unknown35()
        sprite('Action_191_03', 2)	# 14-15	 **attackbox here**
        RefreshMultihit()
        ScreenShake(3500, 500)
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(250)
        Unknown1064(250)
        Unknown35()
        sprite('Action_191_04', 2)	# 16-17
        Unknown1084(1)
        Unknown5000(15, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        sprite('Action_191_05', 5)	# 18-22
        tag_voice(0, 'ume253_0', 'ume253_1', '', '')
        teleportRelativeX(-100000)
        Unknown5000(15, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        sprite('Action_191_06', 4)	# 23-26
        teleportRelativeX(-100000)
        Unknown5000(15, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        sprite('Action_191_07', 3)	# 27-29
        tag_voice(0, '', '', 'ume253_2', '')
        teleportRelativeX(-100000)
        Unknown5000(15, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        sprite('Action_191_08', 3)	# 30-32
        teleportRelativeX(-100000)
        Unknown5000(3, 0)
        Unknown5001('0000000001000000010000000000000000000000')
        sprite('Action_191_09', 4)	# 33-36	 **attackbox here**
        Damage(1500)
        ScreenShake(15000, 15000)
        teleportRelativeX(-50000)
        RefreshMultihit()
        Hitstop(16)
        Unknown5000(14, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        GFX_0('DDcamera', -1)
        Unknown4004('6566666563745f3236310000000000000000000000000000000000000000000000000000')
        sprite('Action_191_10', 4)	# 37-40
        Unknown5000(15, 0)
        Unknown5001('0000000000000000000000000000000000000000')
        sprite('Action_191_11', 5)	# 41-45
        physicsYImpulse(300000)
        setGravity(3000)
        Unknown5000(3, 0)
        Unknown5001('0000000001000000010000000000000000000000')
        Unknown4004('6566666563745f32323600000000000000000000000000000000000000000000ffff0000')
        sprite('Action_191_12', 5)	# 46-50
        Unknown5000(3, 0)
        Unknown5001('0000000001000000010000000000000000000000')
        sprite('Action_191_13', 5)	# 51-55
        Unknown5000(3, 0)
        Unknown5001('0000000001000000010000000000000000000000')
        sprite('Action_191_14', 5)	# 56-60
        Unknown5000(3, 0)
        Unknown5001('0000000001000000010000000000000000000000')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(3)
        label(2)
        sprite('Action_191_15', 1)	# 61-61
        physicsYImpulse(-200000)
        Unknown5000(14, 0)
        Unknown5001('0000000001000000010000000000000000000000')
        gotoLabel(2)
        label(3)
        sprite('Action_191_16', 1)	# 62-62	 **attackbox here**
        tag_voice(0, 'ume254_0', 'ume254_1', 'ume254_2', '')
        RefreshMultihit()
        Damage(3100)
        AttackP2(60)
        Unknown11091(34)
        Hitstop(21)
        Unknown5000(14, 0)
        Unknown5001('0000000001000000010000000000000000000000')
        ScreenShake(65000, 40000)
        SFX_3('SE_BigBomb_Short')
        Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
        Unknown36(1)
        Unknown1056(700)
        Unknown1064(700)
        Unknown2019(-1000)
        Unknown35()
        GFX_0('Mer_224', -1)
        Unknown30079(0)
        Unknown21015('444463616d657261000000000000000000000000000000000000000000000000b80b000000000000')
        Unknown20000(1)
        Unknown13024(1)
        Unknown11064(0)
        sprite('Action_191_17', 1)	# 63-63
        sprite('Action_191_18', 1)	# 64-64
        sprite('Action_191_19', 1)	# 65-65
        sprite('Action_191_20', 1)	# 66-66
        sprite('Action_191_21', 3)	# 67-69
        sprite('Action_191_22', 3)	# 70-72
        sprite('Action_191_23', 3)	# 73-75
        Unknown20000(0)
        physicsXImpulse(-20000)
        physicsYImpulse(10000)
        setGravity(2000)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(5)
        label(4)
        sprite('Action_191_24', 3)	# 76-78
        gotoLabel(4)
        label(5)
        sprite('Action_191_25', 8)	# 79-86
        Unknown1084(1)
        Unknown8000(100, 1, 1)

    @State
    def UltimateCapture_OD():

        def upon_IMMEDIATE():
            AttackDefaults_StandingDD()
            Unknown23055('')
            AttackLevel_(4)
            Damage(1000)
            AttackP2(100)
            AirPushbackX(10000)
            AirPushbackY(10000)
            Hitstop(4)
            AirHitstunAnimation(13)
            AirUntechableTime(80)
            Unknown11058('0100000000000000000000000000000000000000')
            Unknown11064(1)
            Unknown11069('UltimateCaptureODPlus')
            Unknown11084(1)
            Unknown2073(1)

            def upon_LANDING():
                clearUponHandler(2)
                sendToLabel(1)
            Unknown1084(1)
            setInvincible(1)

            def upon_78():
                clearUponHandler(78)
                Unknown13024(0)
                enterState('UltimateCaptureODPlus')
                Unknown1084(1)
        sprite('Action_190_00', 5)	# 1-5
        Unknown2036(24, -1, 0)
        Unknown2058(-10000)
        Unknown30080('')
        physicsXImpulse(-3000)
        Unknown1028(100)
        physicsYImpulse(28000)
        Unknown1043()
        sprite('Action_190_01', 5)	# 6-10
        tag_voice(1, 'ume252_0', 'ume252_1', 'ume252_2', '')
        sprite('Action_190_02', 5)	# 11-15
        sprite('Action_190_03', 5)	# 16-20
        sprite('Action_190_04', 14)	# 21-34
        Unknown1084(1)
        sprite('Action_190_05', 2)	# 35-36	 **attackbox here**
        physicsXImpulse(50000)
        physicsYImpulse(-18000)
        Unknown1043()
        Unknown1028(1500)
        label(0)
        sprite('Action_190_06', 2)	# 37-38	 **attackbox here**
        setInvincible(0)
        sprite('Action_190_07', 2)	# 39-40	 **attackbox here**
        gotoLabel(0)
        label(1)
        sprite('Action_190_08', 17)	# 41-57
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        physicsXImpulse(30000)
        Unknown1028(-1500)

        def upon_3():
            if (not SLOT_12):
                Unknown1084(1)
                clearUponHandler(3)
        sprite('Action_190_09', 11)	# 58-68
        sprite('Action_190_10', 11)	# 69-79

    @State
    def UltimateCaptureODPlus():

        def upon_IMMEDIATE():
            Unknown17011('UltimateCaptureODExe', 3, 0, 0)
            Unknown23056('')
            Unknown11032('ffffffffffffffffffffffffffffffff')
            Unknown11054(-1)
            Unknown11002(-1)
            Unknown30048(1)
            Unknown30061(0)
            Unknown11045(0)
            Unknown11068(1)
            Unknown11078(1)
            Unknown11064(1)
            Unknown11023(1)
            Unknown11044(1)
            Unknown13024(0)

            def upon_LANDING():
                clearUponHandler(2)
                sendToLabel(1)
        sprite('keep', 1)	# 1-1
        Unknown1084(1)
        label(0)
        sprite('Action_190_06', 2)	# 2-3	 **attackbox here**
        physicsXImpulse(50000)
        physicsYImpulse(-18000)
        setGravity(200)
        sprite('Action_190_07', 2)	# 4-5	 **attackbox here**
        gotoLabel(0)
        label(1)
        sprite('Action_190_08', 7)	# 6-12
        Unknown1084(1)
        physicsXImpulse(30000)
        Unknown1028(-1500)

        def upon_3():
            if (not SLOT_12):
                Unknown1084(1)
                clearUponHandler(3)
        sprite('Action_190_09', 9)	# 13-21
        sprite('Action_190_10', 9)	# 22-30

        @State
        def UltimateCaptureODExe():

            def upon_IMMEDIATE():
                Unknown17012(3, 0, 0)
                Unknown23056('')
                AttackLevel_(4)
                Damage(400)
                AttackP2(100)
                Unknown11091(20)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(100)
                AirPushbackX(15000)
                AirPushbackY(35000)
                Hitstop(1)
                Unknown30061(0)
                setInvincible(1)
                Unknown13024(0)
                Unknown11064(1)

                def upon_LANDING():
                    clearUponHandler(2)
                    sendToLabel(1)
                physicsXImpulse(50000)
                physicsYImpulse(-54000)
                Unknown1028(1500)
                Unknown1043()
                Unknown30079(1)
            label(0)
            sprite('Action_191_00', 5)	# 1-5
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            gotoLabel(0)
            label(1)
            sprite('Action_191_01', 2)	# 6-7
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown1028(-2000)
            sprite('Action_191_02', 2)	# 8-9
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(600)
            Unknown1064(600)
            Unknown35()
            sprite('Action_191_03', 2)	# 10-11	 **attackbox here**
            RefreshMultihit()
            ScreenShake(3500, 500)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(450)
            Unknown1064(450)
            Unknown35()
            sprite('Action_191_03', 2)	# 12-13	 **attackbox here**
            RefreshMultihit()
            ScreenShake(3500, 500)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(400)
            Unknown1064(400)
            Unknown35()
            sprite('Action_191_03', 2)	# 14-15	 **attackbox here**
            RefreshMultihit()
            ScreenShake(3500, 500)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(350)
            Unknown1064(350)
            Unknown35()
            sprite('Action_191_03', 2)	# 16-17	 **attackbox here**
            RefreshMultihit()
            ScreenShake(3500, 500)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(300)
            Unknown1064(300)
            Unknown35()
            sprite('Action_191_03', 2)	# 18-19	 **attackbox here**
            RefreshMultihit()
            ScreenShake(3500, 500)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3337390000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(250)
            Unknown1064(250)
            Unknown35()
            sprite('Action_191_04', 2)	# 20-21
            Unknown1084(1)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_05', 5)	# 22-26
            tag_voice(0, 'ume253_0', 'ume253_1', '', '')
            teleportRelativeX(-100000)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_06', 4)	# 27-30
            teleportRelativeX(-100000)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_07', 3)	# 31-33
            tag_voice(0, '', '', 'ume255_2', '')
            teleportRelativeX(-100000)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_08', 3)	# 34-36
            teleportRelativeX(-100000)
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            sprite('Action_191_09', 4)	# 37-40	 **attackbox here**
            Damage(1000)
            ScreenShake(15000, 15000)
            Hitstop(16)
            teleportRelativeX(-50000)
            RefreshMultihit()
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3236310000000000000000000000000000000000000000000000000000')
            sprite('Action_191_10', 4)	# 41-44
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            tag_voice(0, '', '', 'ume253_2', '')
            sprite('Action_191_05', 5)	# 45-49
            Unknown1084(1)
            teleportRelativeX(-100000)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_06', 4)	# 50-53
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_07', 3)	# 54-56
            teleportRelativeX(-100000)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_08', 3)	# 57-59
            teleportRelativeX(-100000)
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            sprite('Action_191_09', 4)	# 60-63	 **attackbox here**
            teleportRelativeX(-50000)
            RefreshMultihit()
            ScreenShake(15000, 15000)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3236310000000000000000000000000000000000000000000000000000')
            sprite('Action_191_10', 4)	# 64-67
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_05', 5)	# 68-72
            teleportRelativeX(-100000)
            Unknown1084(1)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_06', 4)	# 73-76
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_07', 3)	# 77-79
            tag_voice(0, '', '', 'ume256_2', '')
            teleportRelativeX(-100000)
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_08', 3)	# 80-82
            teleportRelativeX(-100000)
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            sprite('Action_191_09', 4)	# 83-86	 **attackbox here**
            teleportRelativeX(-100000)
            RefreshMultihit()
            ScreenShake(15000, 15000)
            Unknown5000(14, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            Unknown4004('6566666563745f3236310000000000000000000000000000000000000000000000000000')
            GFX_0('DDcamera', -1)
            Unknown38(4, 1)
            sprite('Action_191_10', 4)	# 87-90
            Unknown5000(15, 0)
            Unknown5001('0000000000000000000000000000000000000000')
            sprite('Action_191_11', 5)	# 91-95
            Unknown4004('6566666563745f32323600000000000000000000000000000000000000000000ffff0000')
            physicsXImpulse(37500)
            physicsYImpulse(200000)
            setGravity(3000)
            Unknown36(4)
            physicsXImpulse(37500)
            Unknown35()
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            sprite('Action_191_12', 5)	# 96-100
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            sprite('Action_191_13', 5)	# 101-105
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            sprite('Action_191_14', 5)	# 106-110
            Unknown5000(3, 0)
            Unknown5001('0000000001000000010000000000000000000000')

            def upon_LANDING():
                clearUponHandler(2)
                sendToLabel(3)
            label(2)
            sprite('Action_191_15', 1)	# 111-111
            physicsXImpulse(0)
            physicsYImpulse(-200000)
            Unknown36(4)
            physicsXImpulse(0)
            Unknown35()
            Unknown5000(14, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            gotoLabel(2)
            label(3)
            sprite('Action_191_16', 1)	# 112-112	 **attackbox here**
            tag_voice(0, 'ume254_0', 'ume254_1', 'ume254_2', '')
            RefreshMultihit()
            Damage(3200)
            AttackP2(60)
            Unknown11091(29)
            Hitstop(21)
            Unknown5000(14, 0)
            Unknown5001('0000000001000000010000000000000000000000')
            ScreenShake(65000, 40000)
            SFX_3('SE_BigBomb_Short')
            Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
            Unknown36(1)
            Unknown1056(700)
            Unknown1064(700)
            Unknown2019(-1000)
            Unknown35()
            GFX_0('Mer_224', -1)
            Unknown30079(0)
            Unknown21015('444463616d657261000000000000000000000000000000000000000000000000b80b000000000000')
            Unknown20000(1)
            Unknown13024(1)
            Unknown11064(0)
            sprite('Action_191_17', 1)	# 113-113
            sprite('Action_191_18', 1)	# 114-114
            sprite('Action_191_19', 1)	# 115-115
            sprite('Action_191_20', 1)	# 116-116
            sprite('Action_191_21', 3)	# 117-119
            sprite('Action_191_22', 3)	# 120-122
            sprite('Action_191_23', 3)	# 123-125
            Unknown20000(0)
            physicsXImpulse(-20000)
            physicsYImpulse(10000)
            setGravity(2000)

            def upon_LANDING():
                clearUponHandler(2)
                sendToLabel(5)
            label(4)
            sprite('Action_191_24', 3)	# 126-128
            gotoLabel(4)
            label(5)
            sprite('Action_191_25', 8)	# 129-136
            Unknown1084(1)
            Unknown8000(100, 1, 1)

        @Subroutine
        def UltimateAssault_LandShake():

            def upon_3():
                if SLOT_2:
                    SLOT_52 = (SLOT_52 + 1)
                    if (SLOT_52 == 2):
                        SFX_3('SE015_BoundWall')
                        Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
                        Unknown36(1)
                        Unknown1096(250)
                        Unknown1010(50000, 150000)
                        Unknown35()
                    elif (SLOT_52 == 4):
                        Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
                        Unknown36(1)
                        Unknown1096(250)
                        Unknown1010(-150000, -50000)
                        Unknown35()
                    elif (SLOT_52 == 6):
                        Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
                        Unknown36(1)
                        Unknown1096(250)
                        Unknown1010(250000, 350000)
                        Unknown35()
                    elif (SLOT_52 == 8):
                        SLOT_52 = 0
                        Unknown4004('6566666563745f3338300000000000000000000000000000000000000000000000000000')
                        Unknown36(1)
                        Unknown1096(250)
                        Unknown1010(-350000, -250000)
                        Unknown35()

            def upon_ON_HIT_OR_BLOCK():
                ScreenShake(5000, 5000)

        @State
        def UltimateAssault():

            def upon_IMMEDIATE():
                AttackDefaults_StandingDD()
                Unknown23055('')
                AttackLevel_(5)
                Damage(670)
                AttackP1(80)
                AttackP2(60)
                Unknown11092(1)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(100)
                Unknown11091(14)
                Unknown9190(1)
                Hitstop(1)
                Unknown11056(0)
                Unknown30055('e09304001400000014000000')
                callSubroutine('UltimateAssault_LandShake')
            sprite('Action_200_00', 25)	# 1-25
            GFX_0('Mer_202', -1)
            setInvincible(1)
            Unknown2036(60, -1, 0)
            Unknown2058(-10000)
            Unknown30080('')
            tag_voice(1, 'ume250_0', 'ume250_1', '', '')
            sprite('Action_200_01', 10)	# 26-35
            sprite('Action_200_02', 10)	# 36-45
            sprite('Action_200_03', 10)	# 46-55
            sprite('Action_200_04', 10)	# 56-65
            sprite('Action_200_05', 6)	# 66-71
            sprite('Action_200_06', 2)	# 72-73	 **attackbox here**
            GFX_0('Mer_201', -1)
            GFX_0('Mer_203', -1)
            Unknown3029(1)
            Unknown3070(2)
            SLOT_52 = 2
            Unknown2037(1)
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 74-75	 **attackbox here**
            tag_voice(0, 'ume251_0', '', '', '')
            sprite('Action_200_08', 2)	# 76-77	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 78-79	 **attackbox here**
            sprite('Action_200_10', 2)	# 80-81	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 82-83	 **attackbox here**
            sprite('Action_200_12', 2)	# 84-85	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            setInvincible(0)
            sprite('Action_200_13', 2)	# 86-87	 **attackbox here**
            sprite('Action_200_14', 2)	# 88-89	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 90-91	 **attackbox here**
            sprite('Action_200_16', 2)	# 92-93	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            tag_voice(0, '', 'ume251_1', '', '')
            sprite('Action_200_17', 2)	# 94-95	 **attackbox here**
            sprite('Action_200_06', 2)	# 96-97	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 98-99	 **attackbox here**
            sprite('Action_200_08', 2)	# 100-101	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 102-103	 **attackbox here**
            sprite('Action_200_10', 2)	# 104-105	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 106-107	 **attackbox here**
            sprite('Action_200_12', 2)	# 108-109	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 110-111	 **attackbox here**
            sprite('Action_200_14', 2)	# 112-113	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 114-115	 **attackbox here**
            sprite('Action_200_16', 2)	# 116-117	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 118-119	 **attackbox here**
            sprite('Action_200_06', 2)	# 120-121	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 122-123	 **attackbox here**
            sprite('Action_200_08', 2)	# 124-125	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 126-127	 **attackbox here**
            sprite('Action_200_10', 2)	# 128-129	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 130-131	 **attackbox here**
            sprite('Action_200_12', 2)	# 132-133	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 134-135	 **attackbox here**
            sprite('Action_200_14', 2)	# 136-137	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 138-139	 **attackbox here**
            sprite('Action_200_16', 2)	# 140-141	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 142-143	 **attackbox here**
            sprite('Action_200_06', 2)	# 144-145	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 146-147	 **attackbox here**
            sprite('Action_200_08', 2)	# 148-149	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(10000)
            AirPushbackY(40000)
            Unknown9215()
            Unknown9190(0)
            clearUponHandler(10)
            sprite('Action_200_09', 2)	# 150-151	 **attackbox here**
            sprite('Action_200_10', 3)	# 152-154	 **attackbox here**
            Unknown3029(0)
            Unknown26('Mer_201')
            Unknown26('Mer_203')
            Unknown23027()
            Unknown2037(0)
            clearUponHandler(3)
            sprite('Action_200_11', 3)	# 155-157	 **attackbox here**
            sprite('Action_200_12', 4)	# 158-161	 **attackbox here**
            sprite('Action_200_13', 4)	# 162-165	 **attackbox here**
            sprite('Action_200_14', 5)	# 166-170	 **attackbox here**
            sprite('Action_200_15', 5)	# 171-175	 **attackbox here**
            sprite('Action_200_16', 6)	# 176-181	 **attackbox here**
            sprite('Action_200_17', 6)	# 182-187	 **attackbox here**
            sprite('Action_199_12', 6)	# 188-193
            sprite('Action_199_13', 6)	# 194-199
            sprite('Action_199_14', 6)	# 200-205

        @State
        def UltimateAssault_OD():

            def upon_IMMEDIATE():
                AttackDefaults_StandingDD()
                Unknown23055('')
                AttackLevel_(5)
                Damage(640)
                AttackP1(80)
                AttackP2(60)
                Unknown11092(1)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(100)
                Unknown11091(13)
                Unknown9190(1)
                Hitstop(1)
                Unknown11056(0)
                Unknown30055('e09304001400000014000000')
                Unknown11110(76)
                callSubroutine('UltimateAssault_LandShake')
            sprite('Action_200_00', 25)	# 1-25
            GFX_0('Mer_202', -1)
            setInvincible(1)
            Unknown2036(60, -1, 0)
            Unknown2058(-10000)
            Unknown30080('')
            tag_voice(1, 'ume250_0', 'ume250_1', '', '')
            sprite('Action_200_01', 10)	# 26-35
            sprite('Action_200_02', 10)	# 36-45
            sprite('Action_200_03', 10)	# 46-55
            sprite('Action_200_04', 10)	# 56-65
            sprite('Action_200_05', 6)	# 66-71
            sprite('Action_200_06', 2)	# 72-73	 **attackbox here**
            GFX_0('Mer_201', -1)
            GFX_0('Mer_203', -1)
            Unknown3029(1)
            Unknown3070(2)
            SLOT_52 = 2
            Unknown2037(1)
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 74-75	 **attackbox here**
            tag_voice(0, 'ume251_0', '', '', '')
            sprite('Action_200_08', 2)	# 76-77	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 78-79	 **attackbox here**
            sprite('Action_200_10', 2)	# 80-81	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 82-83	 **attackbox here**
            sprite('Action_200_12', 2)	# 84-85	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            setInvincible(0)
            sprite('Action_200_13', 2)	# 86-87	 **attackbox here**
            sprite('Action_200_14', 2)	# 88-89	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 90-91	 **attackbox here**
            sprite('Action_200_16', 2)	# 92-93	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            tag_voice(0, '', 'ume251_1', '', '')
            sprite('Action_200_17', 2)	# 94-95	 **attackbox here**
            sprite('Action_200_06', 2)	# 96-97	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 98-99	 **attackbox here**
            sprite('Action_200_08', 2)	# 100-101	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 102-103	 **attackbox here**
            sprite('Action_200_10', 2)	# 104-105	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 106-107	 **attackbox here**
            sprite('Action_200_12', 2)	# 108-109	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 110-111	 **attackbox here**
            sprite('Action_200_14', 2)	# 112-113	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 114-115	 **attackbox here**
            sprite('Action_200_16', 2)	# 116-117	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 118-119	 **attackbox here**
            sprite('Action_200_06', 2)	# 120-121	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 122-123	 **attackbox here**
            sprite('Action_200_08', 2)	# 124-125	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 126-127	 **attackbox here**
            sprite('Action_200_10', 2)	# 128-129	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 130-131	 **attackbox here**
            sprite('Action_200_12', 2)	# 132-133	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 134-135	 **attackbox here**
            sprite('Action_200_14', 2)	# 136-137	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 138-139	 **attackbox here**
            sprite('Action_200_16', 2)	# 140-141	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 142-143	 **attackbox here**
            sprite('Action_200_06', 2)	# 144-145	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 146-147	 **attackbox here**
            sprite('Action_200_08', 2)	# 148-149	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 150-151	 **attackbox here**
            sprite('Action_200_10', 2)	# 152-153	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 154-155	 **attackbox here**
            sprite('Action_200_12', 2)	# 156-157	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 158-159	 **attackbox here**
            sprite('Action_200_14', 2)	# 160-161	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 162-163	 **attackbox here**
            sprite('Action_200_16', 2)	# 164-165	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 166-167	 **attackbox here**
            sprite('Action_200_06', 2)	# 168-169	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(10000)
            AirPushbackY(40000)
            Unknown9215()
            Unknown9190(0)
            clearUponHandler(10)
            sprite('Action_200_07', 2)	# 170-171	 **attackbox here**
            sprite('Action_200_08', 2)	# 172-173	 **attackbox here**
            Unknown3029(0)
            Unknown26('Mer_201')
            Unknown26('Mer_203')
            Unknown23027()
            Unknown2037(0)
            clearUponHandler(3)
            sprite('Action_200_09', 2)	# 174-175	 **attackbox here**
            sprite('Action_200_10', 2)	# 176-177	 **attackbox here**
            sprite('Action_200_11', 3)	# 178-180	 **attackbox here**
            sprite('Action_200_12', 3)	# 181-183	 **attackbox here**
            sprite('Action_200_13', 3)	# 184-186	 **attackbox here**
            sprite('Action_200_14', 4)	# 187-190	 **attackbox here**
            sprite('Action_200_15', 5)	# 191-195	 **attackbox here**
            sprite('Action_200_16', 6)	# 196-201	 **attackbox here**
            sprite('Action_200_17', 6)	# 202-207	 **attackbox here**
            sprite('Action_199_12', 6)	# 208-213
            sprite('Action_199_13', 6)	# 214-219
            sprite('Action_199_14', 6)	# 220-225

        @State
        def AirUltimateCapture():

            def upon_IMMEDIATE():
                AttackDefaults_AirDD()
                Unknown23055('')
                AttackLevel_(4)
                Damage(1000)
                AttackP2(100)
                AirPushbackX(10000)
                AirPushbackY(10000)
                Hitstop(4)
                AirHitstunAnimation(13)
                AirUntechableTime(80)
                Unknown11058('0100000000000000000000000000000000000000')
                Unknown11064(1)
                Unknown11069('UltimateCapturePlus')

                def upon_LANDING():
                    clearUponHandler(2)
                    sendToLabel(1)
                Unknown1084(1)
                setInvincible(1)

                def upon_78():
                    clearUponHandler(78)
                    Unknown13024(0)
                    enterState('UltimateCapturePlus')
                    Unknown1084(1)
            sprite('Action_037_01', 5)	# 1-5
            Unknown2036(24, -1, 0)
            Unknown2058(-10000)
            Unknown30080('')
            physicsXImpulse(-3000)
            Unknown1028(100)
            physicsYImpulse(28000)
            Unknown1043()
            sprite('Action_190_01', 5)	# 6-10
            tag_voice(1, 'ume252_0', 'ume252_1', 'ume252_2', '')
            sprite('Action_190_02', 5)	# 11-15
            sprite('Action_190_03', 5)	# 16-20
            sprite('Action_190_04', 14)	# 21-34
            Unknown1084(1)
            sprite('Action_190_05', 2)	# 35-36	 **attackbox here**
            physicsXImpulse(50000)
            physicsYImpulse(-18000)
            Unknown1043()
            Unknown1028(1500)
            label(0)
            sprite('Action_190_06', 2)	# 37-38	 **attackbox here**
            setInvincible(0)
            sprite('Action_190_07', 2)	# 39-40	 **attackbox here**
            gotoLabel(0)
            label(1)
            sprite('Action_190_08', 7)	# 41-47
            Unknown1084(1)
            physicsXImpulse(30000)
            Unknown1028(-1500)

            def upon_3():
                if (not SLOT_12):
                    Unknown1084(1)
                    clearUponHandler(3)
            sprite('Action_190_09', 9)	# 48-56
            sprite('Action_190_10', 9)	# 57-65

        @State
        def AirUltimateCapture_OD():

            def upon_IMMEDIATE():
                AttackDefaults_AirDD()
                Unknown23055('')
                AttackLevel_(4)
                Damage(1000)
                AttackP2(100)
                AirPushbackX(10000)
                AirPushbackY(10000)
                Hitstop(4)
                AirHitstunAnimation(13)
                AirUntechableTime(80)
                Unknown11058('0100000000000000000000000000000000000000')
                Unknown11064(1)
                Unknown11069('UltimateCaptureODPlus')

                def upon_LANDING():
                    clearUponHandler(2)
                    sendToLabel(1)
                Unknown1084(1)
                setInvincible(1)

                def upon_78():
                    clearUponHandler(78)
                    Unknown13024(0)
                    enterState('UltimateCaptureODPlus')
                    Unknown1084(1)
            sprite('Action_037_01', 5)	# 1-5
            Unknown2036(24, -1, 0)
            Unknown2058(-10000)
            Unknown30080('')
            physicsXImpulse(-3000)
            Unknown1028(100)
            physicsYImpulse(28000)
            Unknown1043()
            sprite('Action_190_01', 5)	# 6-10
            tag_voice(1, 'ume252_0', 'ume252_1', 'ume252_2', '')
            sprite('Action_190_02', 5)	# 11-15
            sprite('Action_190_03', 5)	# 16-20
            sprite('Action_190_04', 14)	# 21-34
            Unknown1084(1)
            sprite('Action_190_05', 2)	# 35-36	 **attackbox here**
            physicsXImpulse(50000)
            physicsYImpulse(-18000)
            Unknown1043()
            Unknown1028(1500)
            label(0)
            sprite('Action_190_06', 2)	# 37-38	 **attackbox here**
            setInvincible(0)
            sprite('Action_190_07', 2)	# 39-40	 **attackbox here**
            gotoLabel(0)
            label(1)
            sprite('Action_190_08', 7)	# 41-47
            Unknown1084(1)
            physicsXImpulse(30000)
            Unknown1028(-1500)

            def upon_3():
                if (not SLOT_12):
                    Unknown1084(1)
                    clearUponHandler(3)
            sprite('Action_190_09', 9)	# 48-56
            sprite('Action_190_10', 9)	# 57-65

        @State
        def AstralHeat():

            def upon_IMMEDIATE():
                AttackDefaults_Astral()
                AttackLevel_(5)
                Damage(6666)
                YImpluseBeforeWallbounce(0)
                AirPushbackX(0)
                AirPushbackY(1)
                Hitstop(0)
                Unknown11001(17, 0, 0)
                Unknown11091(100)
                GroundedHitstunAnimation(10)
                AirHitstunAnimation(10)
                AirUntechableTime(99999)
                Unknown9154(99999)
                PushbackX(1500)
                Unknown11072(1, 635000, 30000)
                Unknown11064(1)

                def upon_78():
                    clearUponHandler(78)
                    GFX_0('IWEXIST_Camera', 100)
                    setInvincible(1)
                    Unknown23157(1)
                    Unknown23088(1, 1)
                    Unknown23084(1)
                    Unknown36(22)
                    Unknown2034(0)
                    Unknown2053(0)
                    Unknown35()
                    sendToLabel(666)

                def upon_43():
                    if (SLOT_48 == 5001):
                        Unknown2019(0)
                        Unknown3038(1)
                        Unknown1000(-260000)
                        Unknown36(22)
                        Unknown3038(1)
                        Unknown1000(-260000)
                        Unknown35()
                    if (SLOT_48 == 5002):
                        clearUponHandler(45)
                        Unknown23024(0)
                        sendToLabel(668)
                Unknown2019(-500)

                def upon_STATE_END():
                    Unknown2019(0)
                    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
            sprite('Action_370_00', 5)	# 1-5
            Unknown2036(76, -1, 2)
            Unknown23147()
            setInvincible(1)
            Unknown1084(1)
            Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
            SFX_1('ume290')
            sprite('Action_370_00', 65)	# 6-70
            GFX_0('IWEXIST_CutIn2', 100)
            sprite('Action_370_01', 4)	# 71-74
            sprite('Action_370_02', 4)	# 75-78
            sprite('Action_370_03', 4)	# 79-82
            sprite('Action_370_04', 4)	# 83-86
            sprite('Action_370_05ex01', 4)	# 87-90	 **attackbox here**
            sprite('Action_370_06', 4)	# 91-94	 **attackbox here**
            setInvincible(0)
            sprite('Action_370_07', 4)	# 95-98	 **attackbox here**
            sprite('Action_370_08', 4)	# 99-102	 **attackbox here**
            sprite('Action_370_09', 4)	# 103-106	 **attackbox here**
            sprite('Action_370_10', 4)	# 107-110	 **attackbox here**
            sprite('Action_370_07', 4)	# 111-114	 **attackbox here**
            sprite('Action_370_08', 4)	# 115-118	 **attackbox here**
            sprite('Action_110_16', 6)	# 119-124
            teleportRelativeX(-35000)
            sprite('Action_110_17', 6)	# 125-130
            loopRest()
            ExitState()
            label(666)
            sprite('Action_370_07', 4)	# 131-134	 **attackbox here**
            setInvincible(1)
            SFX_1('ume291')
            Unknown20003(1)

            def upon_45():
                Unknown36(22)
                Unknown23178(0)
                Unknown35()
            sprite('Action_370_08', 4)	# 135-138	 **attackbox here**
            sprite('Action_370_09', 4)	# 139-142	 **attackbox here**
            sprite('Action_370_10', 4)	# 143-146	 **attackbox here**
            sprite('Action_370_07', 4)	# 147-150	 **attackbox here**
            sprite('Action_370_08', 4)	# 151-154	 **attackbox here**
            sprite('Action_370_09', 4)	# 155-158	 **attackbox here**
            sprite('Action_370_10', 4)	# 159-162	 **attackbox here**
            sprite('Action_370_07', 4)	# 163-166	 **attackbox here**
            sprite('Action_370_08', 4)	# 167-170	 **attackbox here**
            sprite('Action_370_09', 4)	# 171-174	 **attackbox here**
            sprite('Action_370_10', 4)	# 175-178	 **attackbox here**
            sprite('Action_370_07', 4)	# 179-182	 **attackbox here**
            sprite('Action_370_08', 4)	# 183-186	 **attackbox here**
            sprite('Action_370_09', 4)	# 187-190	 **attackbox here**
            sprite('Action_370_10', 4)	# 191-194	 **attackbox here**
            sprite('Action_370_07', 4)	# 195-198	 **attackbox here**
            sprite('Action_370_08', 4)	# 199-202	 **attackbox here**
            sprite('Action_370_09', 4)	# 203-206	 **attackbox here**
            sprite('Action_370_10', 4)	# 207-210	 **attackbox here**
            sprite('Action_370_07', 4)	# 211-214	 **attackbox here**
            sprite('Action_370_08', 4)	# 215-218	 **attackbox here**
            sprite('Action_370_09', 4)	# 219-222	 **attackbox here**
            sprite('Action_370_10', 4)	# 223-226	 **attackbox here**
            sprite('Action_370_07', 4)	# 227-230	 **attackbox here**
            sprite('Action_370_08', 4)	# 231-234	 **attackbox here**
            sprite('Action_370_09', 4)	# 235-238	 **attackbox here**
            sprite('Action_370_10', 4)	# 239-242	 **attackbox here**
            sprite('Action_370_07', 4)	# 243-246	 **attackbox here**
            sprite('Action_370_08', 4)	# 247-250	 **attackbox here**
            sprite('Action_370_09', 4)	# 251-254	 **attackbox here**
            sprite('Action_370_10', 4)	# 255-258	 **attackbox here**
            sprite('Action_370_07', 4)	# 259-262	 **attackbox here**
            GFX_0('IWEXIST_Black', 100)
            sprite('Action_370_08', 4)	# 263-266	 **attackbox here**
            sprite('Action_370_09', 4)	# 267-270	 **attackbox here**
            sprite('Action_370_10', 4)	# 271-274	 **attackbox here**
            sprite('Action_370_07', 4)	# 275-278	 **attackbox here**
            sprite('Action_370_08', 4)	# 279-282	 **attackbox here**
            sprite('Action_370_09', 4)	# 283-286	 **attackbox here**
            sprite('Action_370_10', 4)	# 287-290	 **attackbox here**
            Unknown21015('495745584953545f43616d6572610000000000000000000000000000000000008b13000000000000')
            sprite('Action_370_09', 4)	# 291-294	 **attackbox here**
            sprite('Action_370_10', 4)	# 295-298	 **attackbox here**
            sprite('Action_370_07', 4)	# 299-302	 **attackbox here**
            sprite('Action_370_08', 4)	# 303-306	 **attackbox here**
            Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
            label(667)
            sprite('Action_370_09', 4)	# 307-310	 **attackbox here**
            sprite('Action_370_10', 4)	# 311-314	 **attackbox here**
            sprite('Action_370_07', 4)	# 315-318	 **attackbox here**
            sprite('Action_370_08', 4)	# 319-322	 **attackbox here**
            gotoLabel(667)
            label(668)
            sprite('Action_369_01', 3)	# 323-325
            Unknown3038(0)
            Unknown21015('495745584953545f43616d6572610000000000000000000000000000000000008c13000000000000')
            Unknown36(22)
            teleportRelativeY(850000)
            Unknown35()
            sprite('Action_369_01', 3)	# 326-328
            Unknown1007(750000)
            setGravity(500)
            sprite('Action_369_02', 3)	# 329-331
            sendToLabelUpon(2, 670)
            label(669)
            sprite('Action_369_01', 3)	# 332-334
            sprite('Action_369_02', 3)	# 335-337
            gotoLabel(669)
            label(670)
            sprite('Action_369_03', 4)	# 338-341
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sprite('Action_369_04', 3)	# 342-344
            sprite('Action_369_05', 3)	# 345-347
            sprite('Action_369_06', 3)	# 348-350
            sprite('Action_369_07', 5)	# 351-355
            sprite('Action_369_08', 15)	# 356-370
            sprite('Action_369_09', 5)	# 371-375
            sprite('Action_369_10', 5)	# 376-380
            sprite('Action_369_11', 5)	# 381-385
            sprite('Action_369_12', 5)	# 386-390
            sprite('Action_369_13', 5)	# 391-395
            sprite('Action_369_14', 5)	# 396-400

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

            def upon_IMMEDIATE():
                AttackDefaults_StandingNormal()
            sprite('Action_261_00', 5)	# 1-5
            sprite('Action_261_01', 5)	# 6-10
            sprite('Action_261_02', 5)	# 11-15
            sprite('Action_261_03', 5)	# 16-20
            sprite('Action_261_04', 4)	# 21-24
            sprite('Action_261_05', 4)	# 25-28
            sprite('Action_261_07', 4)	# 29-32
            sprite('Action_261_08', 4)	# 33-36
            sprite('Action_261_09', 4)	# 37-40
            sprite('Action_261_11', 3)	# 41-43
            sprite('Action_261_12', 3)	# 44-46

        @State
        def CmnActChangePartnerAppealAir():

            def upon_IMMEDIATE():
                AttackDefaults_AirNormal()
            sprite('Action_019_17', 2)	# 1-2
            Unknown1017()
            Unknown1022()
            Unknown1037()
            Unknown1084(1)
            sprite('Action_019_16', 2)	# 3-4
            label(0)
            sprite('Action_019_15', 5)	# 5-9
            sprite('Action_019_14', 5)	# 10-14
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
            loopRest()
            gotoLabel(0)
            label(1)
            sprite('Action_019_16', 6)	# 15-20
            sprite('Action_019_17', 6)	# 21-26

        @State
        def CmnActChangePartnerOut():

            def upon_IMMEDIATE():
                Unknown17013()
            sprite('Action_050_06', 2)	# 1-2
            Unknown1084(1)
            Unknown3004(0)
            sprite('Action_050_05', 2)	# 3-4
            sprite('Action_050_04', 2)	# 5-6
            sprite('Action_050_03', 2)	# 7-8
            sprite('Action_050_02', 3)	# 9-11
            Unknown1084(1)
            sprite('Action_092_03', 2)	# 12-13
            sprite('Action_092_02', 3)	# 14-16
            Unknown3004(-17)
            Unknown1019(0)
            physicsYImpulse(60000)
            setGravity(0)
            sprite('Action_092_01', 30)	# 17-46

        @State
        def CmnActChangeRequest():

            def upon_IMMEDIATE():
                AttackDefaults_StandingNormal()
            sprite('Action_000_19', 4)	# 1-4
            Unknown1084(1)
            Unknown2034(0)
            Unknown2017(0)
            Unknown2053(0)
            Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
            sprite('Action_000_20', 8)	# 5-12
            sprite('Action_000_21', 11)	# 13-23
            label(1)
            sprite('Action_000_22', 5)	# 24-28
            Unknown30042(24)
            if SLOT_0:
                _gotolabel(2)
            loopRest()
            gotoLabel(1)
            label(2)
            sprite('Action_000_23', 12)	# 29-40
            sprite('Action_000_24', 6)	# 41-46

        @State
        def CmnActChangeReturnAppeal():

            def upon_IMMEDIATE():
                Unknown17013()
            sprite('Action_050_17', 5)	# 1-5
            sprite('Action_050_16', 5)	# 6-10
            sprite('Action_050_15', 5)	# 11-15
            sprite('Action_050_14', 5)	# 16-20
            sprite('Action_050_13', 5)	# 21-25
            sprite('Action_050_12', 5)	# 26-30
            sprite('Action_050_11', 30)	# 31-60
            sprite('Action_050_07', 5)	# 61-65
            sprite('Action_050_08', 30)	# 66-95

        @State
        def CmnActChangePartnerIn():

            def upon_IMMEDIATE():
                Unknown17021('')
                Unknown9015(1)

                def upon_LANDING():
                    clearUponHandler(2)
                    sendToLabel(9)
            sprite('null', 25)	# 1-25
            sprite('Action_403_09', 4)	# 26-29
            GFX_0('Mer_074', -1)
            Unknown1086(22)
            teleportRelativeX(-150000)
            teleportRelativeY(2000000)
            physicsYImpulse(-200000)
            setGravity(0)
            Unknown2053(1)
            Unknown2017(1)
            label(1)
            sprite('Action_403_10', 3)	# 30-32	 **attackbox here**
            sprite('Action_403_11', 3)	# 33-35	 **attackbox here**
            gotoLabel(1)
            label(9)
            sprite('keep', 3)	# 36-38
            Unknown2017(1)
            Unknown2053(1)
            Unknown1019(30)
            sprite('Action_403_12', 4)	# 39-42
            Unknown8000(0, 1, 1)
            Unknown1084(1)
            sprite('Action_403_13', 5)	# 43-47
            sprite('Action_403_14', 5)	# 48-52
            sprite('Action_403_15', 5)	# 53-57
            sprite('Action_403_16', 3)	# 58-60

        @State
        def CmnActChangeReturnAppealBurst():
            sprite('Action_312_03', 3)	# 1-3
            sprite('Action_312_04', 3)	# 4-6
            sprite('Action_312_05', 30)	# 7-36
            sprite('Action_312_06', 3)	# 37-39
            sprite('Action_312_07', 3)	# 40-42
            sprite('Action_312_08', 30)	# 43-72

        @State
        def CmnActChangePartnerQuickIn():
            sprite('Action_045_03', 3)	# 1-3
            sprite('Action_045_04', 3)	# 4-6
            sprite('Action_045_05', 3)	# 7-9
            sprite('Action_045_06', 3)	# 10-12
            sprite('Action_045_07', 5)	# 13-17
            sprite('Action_045_26', 3)	# 18-20
            sprite('Action_045_26', 4)	# 21-24
            sprite('Action_045_27', 4)	# 25-28

        @State
        def CmnActChangePartnerQuickOut():

            def upon_IMMEDIATE():
                Unknown17013()

                def upon_LANDING():
                    clearUponHandler(2)
                    Unknown1084(1)
                    sendToLabel(1)
            sprite('Action_011_00', 1)	# 1-1
            sprite('Action_046_01', 2)	# 2-3
            sprite('Action_046_01', 2)	# 4-5
            sprite('Action_046_02', 1)	# 6-6
            sprite('Action_046_03', 2)	# 7-8
            sprite('Action_046_03', 1)	# 9-9
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
            sprite('Action_022_00', 4)	# 3-6	 **attackbox here**
            Unknown1019(95)
            sprite('Action_022_01', 4)	# 7-10	 **attackbox here**
            Unknown1019(95)
            loopRest()
            gotoLabel(0)
            label(99)
            sprite('Action_023_04', 2)	# 11-12
            Unknown8000(100, 1, 1)
            sprite('keep', 100)	# 13-112

        @State
        def CmnActChangePartnerAssistAtk_A():

            def upon_IMMEDIATE():
                AttackDefaults_StandingSpecial()
                Unknown11042(1)
                clearUponHandler(2)
                sendToLabelUpon(2, 1)
            sprite('Action_038_00', 2)	# 1-2
            sprite('Action_038_01', 2)	# 3-4
            sprite('Action_038_02', 3)	# 5-7
            physicsXImpulse(8400)
            physicsYImpulse(40500)
            Unknown1043()
            sprite('Action_038_03', 2)	# 8-9
            sprite('Action_038_04', 4)	# 10-13
            sprite('Action_038_05', 2)	# 14-15
            sprite('Action_175_00', 2)	# 16-17	 **attackbox here**
            Unknown1084(1)
            sprite('Action_175_01', 2)	# 18-19
            sprite('Action_175_02', 3)	# 20-22
            Unknown7007('756d653230365f30000000000000000064000000756d653230365f31000000000000000064000000756d653230365f320000000000000000640000000000000000000000000000000000000000000000')
            sprite('Action_175_03', 8)	# 23-30
            sprite('Action_175_04', 5)	# 31-35
            sprite('Action_175_05', 5)	# 36-40
            physicsXImpulse(-1600)
            physicsYImpulse(18000)
            Unknown1043()
            GFX_0('Mer_179', 0)
            GFX_0('Atk_Shot_Mer_178PS_1', 0)
            GFX_0('Atk_Shot_Mer_178PS_2', 0)
            GFX_0('Atk_Shot_Mer_178PS_3', 0)
            SFX_3('SE221')
            sprite('Action_175_06', 6)	# 41-46
            sprite('Action_175_07', 6)	# 47-52
            sprite('Action_175_08', 5)	# 53-57
            sprite('Action_175_09', 4)	# 58-61
            sprite('Action_175_10', 4)	# 62-65
            sprite('Action_175_11', 3)	# 66-68
            label(0)
            sprite('Action_037_06', 3)	# 69-71
            sprite('Action_037_07', 3)	# 72-74
            gotoLabel(0)
            label(1)
            sprite('Action_021_00', 2)	# 75-76	 **attackbox here**
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sprite('Action_021_01', 3)	# 77-79
            sprite('Action_021_02', 3)	# 80-82
            sprite('Action_021_03', 3)	# 83-85
            sprite('Action_021_04', 5)	# 86-90

        @State
        def CmnActChangePartnerAssistAtk_B():

            def upon_IMMEDIATE():
                AttackDefaults_StandingSpecial()
                AttackLevel_(3)
                GroundedHitstunAnimation(11)
                AirHitstunAnimation(11)
                AttackP1(70)
                AirPushbackY(-50000)
                Unknown9310(24)
                Unknown11042(1)
            sprite('Action_101_00', 4)	# 1-4	 **attackbox here**
            sprite('Action_101_01', 4)	# 5-8
            Unknown7009(1)
            sprite('Action_101_02', 3)	# 9-11
            sprite('Action_101_03', 2)	# 12-13	 **attackbox here**
            SFX_3('SE042')
            GFX_0('Mer_088', -1)
            sprite('Action_101_04', 3)	# 14-16	 **attackbox here**
            sprite('Action_101_05', 8)	# 17-24
            Recovery()
            sprite('Action_101_06', 5)	# 25-29
            sprite('Action_101_07', 6)	# 30-35

        @State
        def CmnActChangePartnerAssistAtk_D():

            def upon_IMMEDIATE():
                AttackDefaults_StandingSpecial()
                AttackLevel_(3)
                Damage(550)
                AttackP1(70)
                Unknown11092(1)
                Hitstop(4)
                Unknown11001(-1, -1, -1)
                AirUntechableTime(80)
                GroundedHitstunAnimation(13)
                AirHitstunAnimation(13)
                AirPushbackX(20000)
                AirPushbackY(20000)
                Unknown11042(1)
            sprite('Action_111_00', 3)	# 1-3
            sprite('Action_111_01', 3)	# 4-6
            Unknown7007('756d653230305f30000000000000000064000000756d653230305f31000000000000000064000000756d653230305f320000000000000000640000000000000000000000000000000000000000000000')
            sprite('Action_111_02', 3)	# 7-9
            sprite('Action_111_03', 3)	# 10-12
            sprite('Action_111_04', 1)	# 13-13	 **attackbox here**
            physicsXImpulse(32000)
            RefreshMultihit()
            SFX_3('SE041')
            sprite('Action_111_05', 1)	# 14-14	 **attackbox here**
            RefreshMultihit()
            SFX_3('SE041')
            sprite('Action_111_06', 1)	# 15-15	 **attackbox here**
            RefreshMultihit()
            SFX_3('SE041')
            sprite('Action_111_07', 1)	# 16-16	 **attackbox here**
            RefreshMultihit()
            SFX_3('SE041')
            sprite('Action_111_08', 1)	# 17-17	 **attackbox here**
            RefreshMultihit()
            SFX_3('SE041')
            sprite('Action_111_09', 1)	# 18-18	 **attackbox here**
            RefreshMultihit()
            SFX_3('SE041')
            sprite('Action_111_10', 1)	# 19-19	 **attackbox here**
            Unknown2003(1)
            Recovery()
            sprite('Action_111_11', 1)	# 20-20	 **attackbox here**
            sprite('Action_111_12', 3)	# 21-23
            physicsXImpulse(10000)
            Unknown1028(-1000)

            def upon_3():
                if (not SLOT_12):
                    Unknown1084(1)
                    clearUponHandler(3)
            sprite('Action_111_13', 6)	# 24-29
            sprite('Action_111_14', 1)	# 30-30
            sprite('Action_111_14', 4)	# 31-34
            Unknown1084(1)
            sprite('Action_111_15', 5)	# 35-39
            sprite('Action_111_16', 5)	# 40-44
            sprite('Action_111_17', 5)	# 45-49

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
            Unknown2036(96, -1, 0)
            sprite('null', 1)	# 2-2
            teleportRelativeX(-1500000)
            teleportRelativeY(240000)
            setGravity(0)
            physicsYImpulse(-9600)
            SLOT_12 = SLOT_19
            teleportRelativeX(-145000)
            Unknown1019(4)
            label(0)
            sprite('Action_022_00', 4)	# 3-6	 **attackbox here**
            sprite('Action_022_01', 4)	# 7-10	 **attackbox here**
            loopRest()
            gotoLabel(0)
            label(1)
            sprite('keep', 10)	# 11-20
            if SLOT_58:
                enterState('UltimateShotDDDOD')
            else:
                enterState('UltimateShotDDD')

        @State
        def UltimateShotDDD():

            def upon_IMMEDIATE():
                AttackDefaults_StandingDD()
                Unknown23056('')
                AttackLevel_(5)
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(100)
                Unknown11091(100)
                Unknown9190(1)
                Hitstop(1)
                Unknown11056(0)
                Unknown30055('e09304001400000014000000')
                Unknown13024(0)
                callSubroutine('UltimateAssault_LandShake')
            sprite('Action_200_00', 25)	# 1-25
            GFX_0('Mer_202', -1)
            setInvincible(1)
            sprite('Action_200_01', 10)	# 26-35
            sprite('Action_200_02', 10)	# 36-45
            sprite('Action_200_03', 10)	# 46-55
            sprite('Action_200_04', 10)	# 56-65
            sprite('Action_200_05', 6)	# 66-71
            sprite('Action_200_06', 2)	# 72-73	 **attackbox here**
            GFX_0('Mer_201', -1)
            GFX_0('Mer_203', -1)
            Unknown3029(1)
            Unknown3070(2)
            SLOT_52 = 2
            Unknown2037(1)
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 74-75	 **attackbox here**
            tag_voice(1, 'ume251_0', 'ume251_1', '', '')
            sprite('Action_200_08', 2)	# 76-77	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 78-79	 **attackbox here**
            sprite('Action_200_10', 2)	# 80-81	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 82-83	 **attackbox here**
            sprite('Action_200_12', 2)	# 84-85	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            setInvincible(0)
            sprite('Action_200_13', 2)	# 86-87	 **attackbox here**
            sprite('Action_200_14', 2)	# 88-89	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 90-91	 **attackbox here**
            sprite('Action_200_16', 2)	# 92-93	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 94-95	 **attackbox here**
            sprite('Action_200_06', 2)	# 96-97	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 98-99	 **attackbox here**
            sprite('Action_200_08', 2)	# 100-101	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 102-103	 **attackbox here**
            sprite('Action_200_10', 2)	# 104-105	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 106-107	 **attackbox here**
            sprite('Action_200_12', 2)	# 108-109	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 110-111	 **attackbox here**
            sprite('Action_200_14', 2)	# 112-113	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 114-115	 **attackbox here**
            sprite('Action_200_16', 2)	# 116-117	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 118-119	 **attackbox here**
            sprite('Action_200_06', 2)	# 120-121	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 122-123	 **attackbox here**
            sprite('Action_200_08', 2)	# 124-125	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 126-127	 **attackbox here**
            sprite('Action_200_10', 2)	# 128-129	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 130-131	 **attackbox here**
            sprite('Action_200_12', 2)	# 132-133	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 134-135	 **attackbox here**
            sprite('Action_200_14', 2)	# 136-137	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 138-139	 **attackbox here**
            sprite('Action_200_16', 2)	# 140-141	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 142-143	 **attackbox here**
            sprite('Action_200_06', 2)	# 144-145	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 146-147	 **attackbox here**
            sprite('Action_200_08', 2)	# 148-149	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(10000)
            AirPushbackY(40000)
            Unknown9215()
            Unknown9190(0)
            clearUponHandler(10)
            sprite('Action_200_09', 2)	# 150-151	 **attackbox here**
            sprite('Action_200_10', 3)	# 152-154	 **attackbox here**
            Unknown3029(0)
            Unknown26('Mer_201')
            Unknown26('Mer_203')
            Unknown23027()
            Unknown2037(0)
            clearUponHandler(3)
            sprite('Action_200_11', 3)	# 155-157	 **attackbox here**
            sprite('Action_200_12', 4)	# 158-161	 **attackbox here**
            sprite('Action_200_13', 4)	# 162-165	 **attackbox here**
            sprite('Action_200_14', 5)	# 166-170	 **attackbox here**
            sprite('Action_200_15', 5)	# 171-175	 **attackbox here**
            sprite('Action_200_16', 6)	# 176-181	 **attackbox here**
            sprite('Action_200_17', 6)	# 182-187	 **attackbox here**
            sprite('Action_199_12', 6)	# 188-193
            sprite('Action_199_13', 6)	# 194-199
            sprite('Action_199_14', 6)	# 200-205

        @State
        def UltimateShotDDDOD():

            def upon_IMMEDIATE():
                AttackDefaults_StandingDD()
                Unknown23056('')
                AttackLevel_(5)
                Damage(100)
                AttackP1(100)
                AttackP2(100)
                Unknown11092(1)
                AirHitstunAnimation(13)
                GroundedHitstunAnimation(13)
                AirUntechableTime(100)
                Unknown11091(100)
                Unknown9190(1)
                Hitstop(1)
                Unknown11056(0)
                Unknown30055('e09304001400000014000000')
                Unknown13024(0)
                callSubroutine('UltimateAssault_LandShake')
            sprite('Action_200_00', 25)	# 1-25
            GFX_0('Mer_202', -1)
            setInvincible(1)
            sprite('Action_200_01', 10)	# 26-35
            sprite('Action_200_02', 10)	# 36-45
            sprite('Action_200_03', 10)	# 46-55
            sprite('Action_200_04', 10)	# 56-65
            sprite('Action_200_05', 6)	# 66-71
            sprite('Action_200_06', 2)	# 72-73	 **attackbox here**
            GFX_0('Mer_201', -1)
            GFX_0('Mer_203', -1)
            Unknown3029(1)
            Unknown3070(2)
            SLOT_52 = 2
            Unknown2037(1)
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 74-75	 **attackbox here**
            tag_voice(1, 'ume251_0', 'ume251_1', '', '')
            sprite('Action_200_08', 2)	# 76-77	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 78-79	 **attackbox here**
            sprite('Action_200_10', 2)	# 80-81	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 82-83	 **attackbox here**
            sprite('Action_200_12', 2)	# 84-85	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            setInvincible(0)
            sprite('Action_200_13', 2)	# 86-87	 **attackbox here**
            sprite('Action_200_14', 2)	# 88-89	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 90-91	 **attackbox here**
            sprite('Action_200_16', 2)	# 92-93	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 94-95	 **attackbox here**
            sprite('Action_200_06', 2)	# 96-97	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 98-99	 **attackbox here**
            sprite('Action_200_08', 2)	# 100-101	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 102-103	 **attackbox here**
            sprite('Action_200_10', 2)	# 104-105	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 106-107	 **attackbox here**
            sprite('Action_200_12', 2)	# 108-109	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 110-111	 **attackbox here**
            sprite('Action_200_14', 2)	# 112-113	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 114-115	 **attackbox here**
            sprite('Action_200_16', 2)	# 116-117	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 118-119	 **attackbox here**
            sprite('Action_200_06', 2)	# 120-121	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 122-123	 **attackbox here**
            sprite('Action_200_08', 2)	# 124-125	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 126-127	 **attackbox here**
            sprite('Action_200_10', 2)	# 128-129	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 130-131	 **attackbox here**
            sprite('Action_200_12', 2)	# 132-133	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 134-135	 **attackbox here**
            sprite('Action_200_14', 2)	# 136-137	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 138-139	 **attackbox here**
            sprite('Action_200_16', 2)	# 140-141	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 142-143	 **attackbox here**
            sprite('Action_200_06', 2)	# 144-145	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_07', 2)	# 146-147	 **attackbox here**
            sprite('Action_200_08', 2)	# 148-149	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_09', 2)	# 150-151	 **attackbox here**
            sprite('Action_200_10', 2)	# 152-153	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_11', 2)	# 154-155	 **attackbox here**
            sprite('Action_200_12', 2)	# 156-157	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_13', 2)	# 158-159	 **attackbox here**
            sprite('Action_200_14', 2)	# 160-161	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(-4000)
            AirPushbackY(30000)
            PushbackX(-12000)
            Unknown9190(0)
            sprite('Action_200_15', 2)	# 162-163	 **attackbox here**
            sprite('Action_200_16', 2)	# 164-165	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(3000)
            AirPushbackY(-30000)
            PushbackX(8000)
            Unknown9190(1)
            sprite('Action_200_17', 2)	# 166-167	 **attackbox here**
            sprite('Action_200_06', 2)	# 168-169	 **attackbox here**
            RefreshMultihit()
            AirPushbackX(10000)
            AirPushbackY(40000)
            Unknown9215()
            Unknown9190(0)
            clearUponHandler(10)
            sprite('Action_200_07', 2)	# 170-171	 **attackbox here**
            sprite('Action_200_08', 2)	# 172-173	 **attackbox here**
            Unknown3029(0)
            Unknown26('Mer_201')
            Unknown26('Mer_203')
            Unknown23027()
            Unknown2037(0)
            clearUponHandler(3)
            sprite('Action_200_09', 2)	# 174-175	 **attackbox here**
            sprite('Action_200_10', 2)	# 176-177	 **attackbox here**
            sprite('Action_200_11', 3)	# 178-180	 **attackbox here**
            sprite('Action_200_12', 3)	# 181-183	 **attackbox here**
            sprite('Action_200_13', 3)	# 184-186	 **attackbox here**
            sprite('Action_200_14', 4)	# 187-190	 **attackbox here**
            sprite('Action_200_15', 5)	# 191-195	 **attackbox here**
            sprite('Action_200_16', 6)	# 196-201	 **attackbox here**
            sprite('Action_200_17', 6)	# 202-207	 **attackbox here**
            sprite('Action_199_12', 6)	# 208-213
            sprite('Action_199_13', 6)	# 214-219
            sprite('Action_199_14', 6)	# 220-225

        @State
        def CmnActChangePartnerBurst():

            def upon_IMMEDIATE():
                Unknown17021('')

                def upon_41():
                    clearUponHandler(41)
                    sendToLabel(0)
            sprite('null', 120)	# 1-120
            label(0)
            sprite('null', 2)	# 121-122
            sprite('null', 4)	# 123-126
            Unknown1086(22)
            teleportRelativeX(-150000)
            teleportRelativeX(-500000)
            Unknown1007(2400000)
            physicsXImpulse(20000)
            physicsYImpulse(-96000)
            setGravity(0)
            sendToLabelUpon(2, 9)
            sprite('Action_403_09', 4)	# 127-130
            GFX_0('Mer_074', -1)
            label(1)
            sprite('Action_403_10', 3)	# 131-133	 **attackbox here**
            sprite('Action_403_11', 3)	# 134-136	 **attackbox here**
            gotoLabel(1)
            label(9)
            clearUponHandler(2)
            sprite('keep', 3)	# 137-139
            sprite('Action_403_12', 6)	# 140-145
            Unknown8000(0, 1, 1)
            Unknown1084(1)
            sprite('Action_403_13', 7)	# 146-152
            sprite('Action_403_14', 7)	# 153-159
            sprite('Action_403_15', 6)	# 160-165
            sprite('Action_403_16', 5)	# 166-170

        @Subroutine
        def MouthTableInit():
            Unknown18011('ume000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume500', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume501', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume502', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume503', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume504', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume505', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume520', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume521', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume522', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume523', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume524', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume525', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume402_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume402_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume403_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume403_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume601bha', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume600bhz', 13411, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume600bjb', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume600bma', 13411, 12345, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume600pna', 13155, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume601rbl', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume600uca', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume601uva', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700bha', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700bhz', 13667, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700bjb', 13155, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700bma', 13155, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700pna', 13155, 12342, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700rbl', 13667, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume701uca', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            Unknown18011('ume700uva', 13155, 12345, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
            PartnerChar('bhz')
            if SLOT_0:
                _gotolabel(100)
            PartnerChar('bjb')
            if SLOT_0:
                _gotolabel(110)
            PartnerChar('bma')
            if SLOT_0:
                _gotolabel(120)
            PartnerChar('pna')
            if SLOT_0:
                _gotolabel(130)
            PartnerChar('rbl')
            if SLOT_0:
                _gotolabel(140)
            PartnerChar('uca')
            if SLOT_0:
                _gotolabel(150)
            PartnerChar('uva')
            if SLOT_0:
                _gotolabel(160)
            PartnerChar('bha')
            if SLOT_0:
                _gotolabel(170)
            label(482)
            Unknown19(991, 2, 158)
            sprite('Action_050_00', 1)	# 2-2
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)
            sprite('Action_050_01', 2)	# 3-4
            sendToLabelUpon(2, 2)
            Unknown3038(0)
            physicsYImpulse(-15000)
            if random_(2, 0, 50):
                Unknown7006('ume500', 100, 895839605, 12592, 0, 0, 100, 895839605, 12848, 0, 0, 100, 0, 0, 0, 0, 0)
            else:
                Unknown7006('ume503', 100, 895839605, 13360, 0, 0, 100, 895839605, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
            label(1)
            sprite('Action_050_00', 4)	# 5-8
            sprite('Action_050_01', 4)	# 9-12
            gotoLabel(1)
            label(2)
            sprite('Action_050_02', 4)	# 13-16
            sprite('Action_050_03', 3)	# 17-19
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 20-22
            sprite('Action_050_05', 3)	# 23-25
            sprite('Action_050_06', 5)	# 26-30
            sprite('Action_050_07', 20)	# 31-50
            sprite('Action_050_08', 5)	# 51-55
            sprite('Action_050_09', 15)	# 56-70
            sprite('Action_050_10', 5)	# 71-75
            sprite('Action_050_11', 25)	# 76-100
            sprite('Action_050_12', 5)	# 101-105
            sprite('Action_050_13', 15)	# 106-120
            sprite('Action_050_14', 5)	# 121-125
            sprite('Action_050_15', 5)	# 126-130
            sprite('Action_050_16', 5)	# 131-135
            sprite('Action_050_17', 5)	# 136-140
            Unknown23018(1)
            label(3)
            sprite('Action_000_00', 4)	# 141-144	 **attackbox here**
            sprite('Action_000_01', 4)	# 145-148
            sprite('Action_000_02', 4)	# 149-152
            sprite('Action_000_03', 4)	# 153-156
            sprite('Action_000_04', 4)	# 157-160
            sprite('Action_000_05', 4)	# 161-164
            sprite('Action_000_06', 4)	# 165-168
            sprite('Action_000_07', 4)	# 169-172
            sprite('Action_000_08', 4)	# 173-176
            sprite('Action_000_09', 4)	# 177-180
            sprite('Action_000_10', 4)	# 181-184
            sprite('Action_000_11', 4)	# 185-188
            sprite('Action_000_12', 4)	# 189-192
            sprite('Action_000_13', 4)	# 193-196
            sprite('Action_000_14', 4)	# 197-200
            sprite('Action_000_15', 4)	# 201-204
            sprite('Action_000_16', 4)	# 205-208
            sprite('Action_000_17', 4)	# 209-212
            loopRest()
            gotoLabel(3)
            label(991)
            sprite('Action_000_00', 1)	# 213-213	 **attackbox here**
            Unknown2019(1000)
            Unknown21011(120)
            label(992)
            sprite('Action_000_00', 4)	# 214-217	 **attackbox here**
            sprite('Action_000_01', 4)	# 218-221
            sprite('Action_000_02', 4)	# 222-225
            sprite('Action_000_03', 4)	# 226-229
            sprite('Action_000_04', 4)	# 230-233
            sprite('Action_000_05', 4)	# 234-237
            sprite('Action_000_06', 4)	# 238-241
            sprite('Action_000_07', 4)	# 242-245
            sprite('Action_000_08', 4)	# 246-249
            sprite('Action_000_09', 4)	# 250-253
            sprite('Action_000_10', 4)	# 254-257
            sprite('Action_000_11', 4)	# 258-261
            sprite('Action_000_12', 4)	# 262-265
            sprite('Action_000_13', 4)	# 266-269
            sprite('Action_000_14', 4)	# 270-273
            sprite('Action_000_15', 4)	# 274-277
            sprite('Action_000_16', 4)	# 278-281
            sprite('Action_000_17', 4)	# 282-285
            loopRest()
            gotoLabel(992)
            ExitState()
            label(100)
            sprite('Action_050_00', 1)	# 286-286
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)
            sprite('Action_050_01', 2)	# 287-288
            sendToLabelUpon(2, 102)
            Unknown3038(0)
            physicsYImpulse(-15000)
            SFX_1('ume600bhz')
            label(101)
            sprite('Action_050_00', 4)	# 289-292
            sprite('Action_050_01', 4)	# 293-296
            gotoLabel(101)
            label(102)
            sprite('Action_050_02', 4)	# 297-300
            sprite('Action_050_03', 3)	# 301-303
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 304-306
            sprite('Action_050_05', 3)	# 307-309
            sprite('Action_050_06', 5)	# 310-314
            sprite('Action_050_07', 20)	# 315-334
            sprite('Action_050_08', 5)	# 335-339
            sprite('Action_050_09', 15)	# 340-354
            sprite('Action_050_10', 5)	# 355-359
            sprite('Action_050_11', 25)	# 360-384
            sprite('Action_050_12', 5)	# 385-389
            sprite('Action_050_13', 15)	# 390-404
            sprite('Action_050_14', 5)	# 405-409
            sprite('Action_050_15', 5)	# 410-414
            sprite('Action_050_16', 5)	# 415-419
            sprite('Action_050_17', 5)	# 420-424
            Unknown2037(3)
            Unknown21011(530)
            label(103)
            sprite('Action_000_00', 4)	# 425-428	 **attackbox here**
            sprite('Action_000_01', 4)	# 429-432
            sprite('Action_000_02', 4)	# 433-436
            sprite('Action_000_03', 4)	# 437-440
            sprite('Action_000_04', 4)	# 441-444
            sprite('Action_000_05', 4)	# 445-448
            sprite('Action_000_06', 4)	# 449-452
            sprite('Action_000_07', 4)	# 453-456
            sprite('Action_000_08', 4)	# 457-460
            if (not SLOT_2):
                Unknown21007(24, 40)
            sprite('Action_000_09', 4)	# 461-464
            sprite('Action_000_10', 4)	# 465-468
            sprite('Action_000_11', 4)	# 469-472
            sprite('Action_000_12', 4)	# 473-476
            sprite('Action_000_13', 4)	# 477-480
            sprite('Action_000_14', 4)	# 481-484
            sprite('Action_000_15', 4)	# 485-488
            sprite('Action_000_16', 4)	# 489-492
            sprite('Action_000_17', 4)	# 493-496
            Unknown2038(-1)
            loopRest()
            gotoLabel(103)
            ExitState()
            label(110)
            sprite('Action_050_00', 1)	# 497-497
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)
            sprite('Action_050_01', 2)	# 498-499
            sendToLabelUpon(2, 112)
            Unknown3038(0)
            physicsYImpulse(-15000)
            SFX_1('ume600bhz')
            label(111)
            sprite('Action_050_00', 4)	# 500-503
            sprite('Action_050_01', 4)	# 504-507
            gotoLabel(111)
            label(112)
            sprite('Action_050_02', 4)	# 508-511
            sprite('Action_050_03', 3)	# 512-514
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 515-517
            sprite('Action_050_05', 3)	# 518-520
            sprite('Action_050_06', 5)	# 521-525
            sprite('Action_050_07', 20)	# 526-545
            sprite('Action_050_08', 5)	# 546-550
            sprite('Action_050_09', 15)	# 551-565
            sprite('Action_050_10', 5)	# 566-570
            sprite('Action_050_11', 25)	# 571-595
            sprite('Action_050_12', 5)	# 596-600
            sprite('Action_050_13', 15)	# 601-615
            sprite('Action_050_14', 5)	# 616-620
            sprite('Action_050_15', 5)	# 621-625
            sprite('Action_050_16', 5)	# 626-630
            sprite('Action_050_17', 5)	# 631-635
            Unknown2037(3)
            Unknown21011(500)
            label(113)
            sprite('Action_000_00', 4)	# 636-639	 **attackbox here**
            sprite('Action_000_01', 4)	# 640-643
            sprite('Action_000_02', 4)	# 644-647
            sprite('Action_000_03', 4)	# 648-651
            sprite('Action_000_04', 4)	# 652-655
            sprite('Action_000_05', 4)	# 656-659
            sprite('Action_000_06', 4)	# 660-663
            sprite('Action_000_07', 4)	# 664-667
            sprite('Action_000_08', 4)	# 668-671
            if (not SLOT_2):
                Unknown21007(24, 40)
            sprite('Action_000_09', 4)	# 672-675
            sprite('Action_000_10', 4)	# 676-679
            sprite('Action_000_11', 4)	# 680-683
            sprite('Action_000_12', 4)	# 684-687
            sprite('Action_000_13', 4)	# 688-691
            sprite('Action_000_14', 4)	# 692-695
            sprite('Action_000_15', 4)	# 696-699
            sprite('Action_000_16', 4)	# 700-703
            sprite('Action_000_17', 4)	# 704-707
            Unknown2038(-1)
            loopRest()
            gotoLabel(113)
            ExitState()
            label(120)
            sprite('Action_050_00', 1)	# 708-708
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)
            sprite('Action_050_01', 2)	# 709-710
            sendToLabelUpon(2, 122)
            Unknown3038(0)
            physicsYImpulse(-15000)
            SFX_1('ume600bma')
            label(121)
            sprite('Action_050_00', 4)	# 711-714
            sprite('Action_050_01', 4)	# 715-718
            gotoLabel(121)
            label(122)
            sprite('Action_050_02', 4)	# 719-722
            sprite('Action_050_03', 3)	# 723-725
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 726-728
            sprite('Action_050_05', 3)	# 729-731
            sprite('Action_050_06', 5)	# 732-736
            sprite('Action_050_07', 20)	# 737-756
            sprite('Action_050_08', 5)	# 757-761
            sprite('Action_050_09', 15)	# 762-776
            sprite('Action_050_10', 5)	# 777-781
            sprite('Action_050_11', 25)	# 782-806
            sprite('Action_050_12', 5)	# 807-811
            sprite('Action_050_13', 15)	# 812-826
            sprite('Action_050_14', 5)	# 827-831
            sprite('Action_050_15', 5)	# 832-836
            sprite('Action_050_16', 5)	# 837-841
            sprite('Action_050_17', 5)	# 842-846
            label(123)
            sprite('Action_000_00', 4)	# 847-850	 **attackbox here**
            sprite('Action_000_01', 4)	# 851-854
            sprite('Action_000_02', 4)	# 855-858
            sprite('Action_000_03', 4)	# 859-862
            sprite('Action_000_04', 4)	# 863-866
            sprite('Action_000_05', 4)	# 867-870
            sprite('Action_000_06', 4)	# 871-874
            sprite('Action_000_07', 4)	# 875-878
            sprite('Action_000_08', 4)	# 879-882
            sprite('Action_000_09', 4)	# 883-886
            sprite('Action_000_10', 4)	# 887-890
            sprite('Action_000_11', 4)	# 891-894
            sprite('Action_000_12', 4)	# 895-898
            sprite('Action_000_13', 4)	# 899-902
            sprite('Action_000_14', 4)	# 903-906
            sprite('Action_000_15', 4)	# 907-910
            sprite('Action_000_16', 4)	# 911-914
            sprite('Action_000_17', 4)	# 915-918
            loopRest()
            if SLOT_97:
                _gotolabel(123)
            sprite('Action_000_00', 1)	# 919-919	 **attackbox here**
            Unknown21007(24, 40)
            Unknown21011(300)
            label(124)
            sprite('Action_000_00', 4)	# 920-923	 **attackbox here**
            sprite('Action_000_01', 4)	# 924-927
            sprite('Action_000_02', 4)	# 928-931
            sprite('Action_000_03', 4)	# 932-935
            sprite('Action_000_04', 4)	# 936-939
            sprite('Action_000_05', 4)	# 940-943
            sprite('Action_000_06', 4)	# 944-947
            sprite('Action_000_07', 4)	# 948-951
            sprite('Action_000_08', 4)	# 952-955
            sprite('Action_000_09', 4)	# 956-959
            sprite('Action_000_10', 4)	# 960-963
            sprite('Action_000_11', 4)	# 964-967
            sprite('Action_000_12', 4)	# 968-971
            sprite('Action_000_13', 4)	# 972-975
            sprite('Action_000_14', 4)	# 976-979
            sprite('Action_000_15', 4)	# 980-983
            sprite('Action_000_16', 4)	# 984-987
            sprite('Action_000_17', 4)	# 988-991
            loopRest()
            gotoLabel(124)
            ExitState()
            label(130)
            sprite('Action_050_00', 1)	# 992-992
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)
            sprite('Action_050_01', 2)	# 993-994
            sendToLabelUpon(2, 132)
            Unknown3038(0)
            physicsYImpulse(-15000)
            SFX_1('ume600pna')
            label(131)
            sprite('Action_050_00', 4)	# 995-998
            sprite('Action_050_01', 4)	# 999-1002
            gotoLabel(131)
            label(132)
            sprite('Action_050_02', 4)	# 1003-1006
            sprite('Action_050_03', 3)	# 1007-1009
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 1010-1012
            sprite('Action_050_05', 3)	# 1013-1015
            sprite('Action_050_06', 5)	# 1016-1020
            sprite('Action_050_07', 20)	# 1021-1040
            sprite('Action_050_08', 5)	# 1041-1045
            sprite('Action_050_09', 15)	# 1046-1060
            sprite('Action_050_10', 5)	# 1061-1065
            sprite('Action_050_11', 25)	# 1066-1090
            sprite('Action_050_12', 5)	# 1091-1095
            sprite('Action_050_13', 15)	# 1096-1110
            sprite('Action_050_14', 5)	# 1111-1115
            sprite('Action_050_15', 5)	# 1116-1120
            sprite('Action_050_16', 5)	# 1121-1125
            sprite('Action_050_17', 5)	# 1126-1130
            label(133)
            sprite('Action_000_00', 4)	# 1131-1134	 **attackbox here**
            sprite('Action_000_01', 4)	# 1135-1138
            sprite('Action_000_02', 4)	# 1139-1142
            sprite('Action_000_03', 4)	# 1143-1146
            sprite('Action_000_04', 4)	# 1147-1150
            sprite('Action_000_05', 4)	# 1151-1154
            sprite('Action_000_06', 4)	# 1155-1158
            sprite('Action_000_07', 4)	# 1159-1162
            sprite('Action_000_08', 4)	# 1163-1166
            sprite('Action_000_09', 4)	# 1167-1170
            sprite('Action_000_10', 4)	# 1171-1174
            sprite('Action_000_11', 4)	# 1175-1178
            sprite('Action_000_12', 4)	# 1179-1182
            sprite('Action_000_13', 4)	# 1183-1186
            sprite('Action_000_14', 4)	# 1187-1190
            sprite('Action_000_15', 4)	# 1191-1194
            sprite('Action_000_16', 4)	# 1195-1198
            sprite('Action_000_17', 4)	# 1199-1202
            loopRest()
            if SLOT_97:
                _gotolabel(133)
            sprite('Action_000_00', 1)	# 1203-1203	 **attackbox here**
            Unknown21007(24, 40)
            Unknown21011(380)
            label(134)
            sprite('Action_000_00', 4)	# 1204-1207	 **attackbox here**
            sprite('Action_000_01', 4)	# 1208-1211
            sprite('Action_000_02', 4)	# 1212-1215
            sprite('Action_000_03', 4)	# 1216-1219
            sprite('Action_000_04', 4)	# 1220-1223
            sprite('Action_000_05', 4)	# 1224-1227
            sprite('Action_000_06', 4)	# 1228-1231
            sprite('Action_000_07', 4)	# 1232-1235
            sprite('Action_000_08', 4)	# 1236-1239
            sprite('Action_000_09', 4)	# 1240-1243
            sprite('Action_000_10', 4)	# 1244-1247
            sprite('Action_000_11', 4)	# 1248-1251
            sprite('Action_000_12', 4)	# 1252-1255
            sprite('Action_000_13', 4)	# 1256-1259
            sprite('Action_000_14', 4)	# 1260-1263
            sprite('Action_000_15', 4)	# 1264-1267
            sprite('Action_000_16', 4)	# 1268-1271
            sprite('Action_000_17', 4)	# 1272-1275
            loopRest()
            gotoLabel(134)
            ExitState()
            label(140)
            sprite('Action_000_00', 1)	# 1276-1276	 **attackbox here**
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)

            def upon_40():
                clearUponHandler(40)
                sendToLabel(142)
            label(141)
            sprite('Action_000_00', 4)	# 1277-1280	 **attackbox here**
            sprite('Action_000_01', 4)	# 1281-1284
            sprite('Action_000_02', 4)	# 1285-1288
            sprite('Action_000_03', 4)	# 1289-1292
            sprite('Action_000_04', 4)	# 1293-1296
            sprite('Action_000_05', 4)	# 1297-1300
            sprite('Action_000_06', 4)	# 1301-1304
            sprite('Action_000_07', 4)	# 1305-1308
            sprite('Action_000_08', 4)	# 1309-1312
            sprite('Action_000_09', 4)	# 1313-1316
            sprite('Action_000_10', 4)	# 1317-1320
            sprite('Action_000_11', 4)	# 1321-1324
            sprite('Action_000_12', 4)	# 1325-1328
            sprite('Action_000_13', 4)	# 1329-1332
            sprite('Action_000_14', 4)	# 1333-1336
            sprite('Action_000_15', 4)	# 1337-1340
            sprite('Action_000_16', 4)	# 1341-1344
            sprite('Action_000_17', 4)	# 1345-1348
            loopRest()
            gotoLabel(141)
            label(142)
            sprite('Action_053_00', 2)	# 1349-1350	 **attackbox here**
            sprite('Action_053_01', 3)	# 1351-1353
            sprite('Action_053_02', 3)	# 1354-1356
            sprite('Action_053_03', 3)	# 1357-1359
            sprite('Action_053_04', 5)	# 1360-1364
            sprite('Action_053_05', 7)	# 1365-1371
            sprite('Action_053_06', 8)	# 1372-1379
            sprite('Action_053_07', 3)	# 1380-1382
            SFX_1('ume601rbl')
            Unknown23018(1)
            label(143)
            sprite('Action_053_08', 2)	# 1383-1384
            sprite('Action_053_09', 2)	# 1385-1386
            sprite('Action_053_10', 2)	# 1387-1388
            sprite('Action_053_11', 2)	# 1389-1390
            gotoLabel(143)
            ExitState()
            label(150)
            sprite('Action_050_00', 1)	# 1391-1391
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)
            sprite('Action_050_01', 2)	# 1392-1393
            sendToLabelUpon(2, 152)
            Unknown3038(0)
            physicsYImpulse(-15000)
            SFX_1('ume600uca')
            label(151)
            sprite('Action_050_00', 4)	# 1394-1397
            sprite('Action_050_01', 4)	# 1398-1401
            gotoLabel(151)
            label(152)
            sprite('Action_050_02', 4)	# 1402-1405
            sprite('Action_050_03', 3)	# 1406-1408
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 1409-1411
            sprite('Action_050_05', 3)	# 1412-1414
            sprite('Action_050_06', 5)	# 1415-1419
            sprite('Action_050_07', 20)	# 1420-1439
            sprite('Action_050_08', 5)	# 1440-1444
            sprite('Action_050_09', 15)	# 1445-1459
            sprite('Action_050_10', 5)	# 1460-1464
            sprite('Action_050_11', 25)	# 1465-1489
            sprite('Action_050_12', 5)	# 1490-1494
            sprite('Action_050_13', 15)	# 1495-1509
            sprite('Action_050_14', 5)	# 1510-1514
            sprite('Action_050_15', 5)	# 1515-1519
            sprite('Action_050_16', 5)	# 1520-1524
            sprite('Action_050_17', 5)	# 1525-1529
            Unknown2037(1)
            Unknown21011(340)
            label(153)
            sprite('Action_000_00', 4)	# 1530-1533	 **attackbox here**
            sprite('Action_000_01', 4)	# 1534-1537
            sprite('Action_000_02', 4)	# 1538-1541
            sprite('Action_000_03', 4)	# 1542-1545
            sprite('Action_000_04', 4)	# 1546-1549
            sprite('Action_000_05', 4)	# 1550-1553
            sprite('Action_000_06', 4)	# 1554-1557
            sprite('Action_000_07', 4)	# 1558-1561
            if (not SLOT_2):
                Unknown21007(24, 40)
            sprite('Action_000_08', 4)	# 1562-1565
            sprite('Action_000_09', 4)	# 1566-1569
            sprite('Action_000_10', 4)	# 1570-1573
            sprite('Action_000_11', 4)	# 1574-1577
            sprite('Action_000_12', 4)	# 1578-1581
            sprite('Action_000_13', 4)	# 1582-1585
            sprite('Action_000_14', 4)	# 1586-1589
            sprite('Action_000_15', 4)	# 1590-1593
            sprite('Action_000_16', 4)	# 1594-1597
            sprite('Action_000_17', 4)	# 1598-1601
            Unknown2038(-1)
            loopRest()
            gotoLabel(153)
            ExitState()
            label(160)
            sprite('Action_000_00', 1)	# 1602-1602	 **attackbox here**
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)

            def upon_40():
                clearUponHandler(40)
                sendToLabel(162)
            label(161)
            sprite('Action_000_00', 4)	# 1603-1606	 **attackbox here**
            sprite('Action_000_01', 4)	# 1607-1610
            sprite('Action_000_02', 4)	# 1611-1614
            sprite('Action_000_03', 4)	# 1615-1618
            sprite('Action_000_04', 4)	# 1619-1622
            sprite('Action_000_05', 4)	# 1623-1626
            sprite('Action_000_06', 4)	# 1627-1630
            sprite('Action_000_07', 4)	# 1631-1634
            sprite('Action_000_08', 4)	# 1635-1638
            sprite('Action_000_09', 4)	# 1639-1642
            sprite('Action_000_10', 4)	# 1643-1646
            sprite('Action_000_11', 4)	# 1647-1650
            sprite('Action_000_12', 4)	# 1651-1654
            sprite('Action_000_13', 4)	# 1655-1658
            sprite('Action_000_14', 4)	# 1659-1662
            sprite('Action_000_15', 4)	# 1663-1666
            sprite('Action_000_16', 4)	# 1667-1670
            sprite('Action_000_17', 4)	# 1671-1674
            loopRest()
            gotoLabel(161)
            label(162)
            sprite('Action_053_00', 2)	# 1675-1676	 **attackbox here**
            sprite('Action_053_01', 3)	# 1677-1679
            sprite('Action_053_02', 3)	# 1680-1682
            sprite('Action_053_03', 3)	# 1683-1685
            sprite('Action_053_04', 5)	# 1686-1690
            sprite('Action_053_05', 7)	# 1691-1697
            sprite('Action_053_06', 8)	# 1698-1705
            sprite('Action_053_07', 3)	# 1706-1708
            SFX_1('ume601uva')
            Unknown23018(1)
            label(163)
            sprite('Action_053_08', 2)	# 1709-1710
            sprite('Action_053_09', 2)	# 1711-1712
            sprite('Action_053_10', 2)	# 1713-1714
            sprite('Action_053_11', 2)	# 1715-1716
            gotoLabel(163)
            ExitState()
            label(170)
            sprite('Action_050_00', 32767)	# 1717-34483
            if SLOT_158:
                Unknown1000(-1230000)
            else:
                Unknown1000(-1465000)
            Unknown3038(1)
            teleportRelativeY(600000)
            setGravity(0)

            def upon_40():
                clearUponHandler(40)
                sendToLabel(171)
            label(171)
            sprite('Action_050_01', 2)	# 34484-34485
            sendToLabelUpon(2, 173)
            Unknown3038(0)
            physicsYImpulse(-15000)
            SFX_1('ume601bha')
            label(172)
            sprite('Action_050_00', 4)	# 34486-34489
            sprite('Action_050_01', 4)	# 34490-34493
            gotoLabel(172)
            label(173)
            sprite('Action_050_02', 4)	# 34494-34497
            sprite('Action_050_03', 3)	# 34498-34500
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            sprite('Action_050_04', 3)	# 34501-34503
            sprite('Action_050_05', 3)	# 34504-34506
            sprite('Action_050_06', 5)	# 34507-34511
            label(174)
            sprite('Action_050_07', 1)	# 34512-34512
            if SLOT_97:
                _gotolabel(174)
            sprite('Action_050_12', 5)	# 34513-34517
            sprite('Action_050_13', 15)	# 34518-34532
            sprite('Action_050_14', 5)	# 34533-34537
            sprite('Action_050_15', 5)	# 34538-34542
            sprite('Action_050_16', 5)	# 34543-34547
            sprite('Action_050_17', 5)	# 34548-34552
            Unknown23018(1)
            label(175)
            sprite('Action_000_00', 4)	# 34553-34556	 **attackbox here**
            sprite('Action_000_01', 4)	# 34557-34560
            sprite('Action_000_02', 4)	# 34561-34564
            sprite('Action_000_03', 4)	# 34565-34568
            sprite('Action_000_04', 4)	# 34569-34572
            sprite('Action_000_05', 4)	# 34573-34576
            sprite('Action_000_06', 4)	# 34577-34580
            sprite('Action_000_07', 4)	# 34581-34584
            sprite('Action_000_08', 4)	# 34585-34588
            sprite('Action_000_09', 4)	# 34589-34592
            sprite('Action_000_10', 4)	# 34593-34596
            sprite('Action_000_11', 4)	# 34597-34600
            sprite('Action_000_12', 4)	# 34601-34604
            sprite('Action_000_13', 4)	# 34605-34608
            sprite('Action_000_14', 4)	# 34609-34612
            sprite('Action_000_15', 4)	# 34613-34616
            sprite('Action_000_16', 4)	# 34617-34620
            sprite('Action_000_17', 4)	# 34621-34624
            loopRest()
            gotoLabel(175)
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
                    if PartnerChar('bhz'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(100)
                            clearUponHandler(3)
                    if PartnerChar('bjb'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(110)
                            clearUponHandler(3)
                    if PartnerChar('bma'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(120)
                            clearUponHandler(3)
                    if PartnerChar('pna'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(130)
                            clearUponHandler(3)
                    if PartnerChar('rbl'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(140)
                            clearUponHandler(3)
                    if PartnerChar('uca'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(150)
                            clearUponHandler(3)
                    if PartnerChar('uva'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(160)
                            clearUponHandler(3)
                    if PartnerChar('bha'):
                        if (SLOT_145 <= 500000):
                            sendToLabel(170)
                            clearUponHandler(3)
            label(482)
            sprite('keep', 1)	# 3-3
            clearUponHandler(3)
            SLOT_58 = 0
            label(0)
            sprite('Action_053_00', 2)	# 4-5	 **attackbox here**
            sprite('Action_053_01', 3)	# 6-8
            sprite('Action_053_02', 3)	# 9-11
            sprite('Action_053_03', 3)	# 12-14
            sprite('Action_053_04', 5)	# 15-19
            sprite('Action_053_05', 7)	# 20-26
            sprite('Action_053_06', 8)	# 27-34
            sprite('Action_053_07', 3)	# 35-37
            if SLOT_158:
                if SLOT_52:
                    Unknown7006('ume524', 100, 895839605, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                elif SLOT_108:
                    Unknown7006('ume402_0', 100, 879062389, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                else:
                    Unknown7006('ume520', 100, 895839605, 12594, 0, 0, 100, 895839605, 12850, 0, 0, 100, 895839605, 13106, 0, 0, 100)
            Unknown23018(1)
            label(1)
            sprite('Action_053_08', 2)	# 38-39
            sprite('Action_053_09', 2)	# 40-41
            sprite('Action_053_10', 2)	# 42-43
            sprite('Action_053_11', 2)	# 44-45
            gotoLabel(1)
            label(100)
            sprite('Action_053_00', 2)	# 46-47	 **attackbox here**
            sprite('Action_053_01', 3)	# 48-50
            sprite('Action_053_02', 3)	# 51-53
            sprite('Action_053_03', 3)	# 54-56
            sprite('Action_053_04', 5)	# 57-61
            sprite('Action_053_05', 7)	# 62-68
            sprite('Action_053_06', 8)	# 69-76
            sprite('Action_053_07', 3)	# 77-79
            SFX_1('ume700bhz')
            label(101)
            sprite('Action_053_08', 2)	# 80-81
            sprite('Action_053_09', 2)	# 82-83
            sprite('Action_053_10', 2)	# 84-85
            sprite('Action_053_11', 2)	# 86-87
            if SLOT_97:
                _gotolabel(101)
            sprite('Action_053_08', 1)	# 88-88
            Unknown21007(24, 40)
            Unknown21011(420)
            label(102)
            sprite('Action_053_08', 2)	# 89-90
            sprite('Action_053_09', 2)	# 91-92
            sprite('Action_053_10', 2)	# 93-94
            sprite('Action_053_11', 2)	# 95-96
            gotoLabel(102)
            label(110)
            sprite('Action_053_00', 2)	# 97-98	 **attackbox here**
            sprite('Action_053_01', 3)	# 99-101
            sprite('Action_053_02', 3)	# 102-104
            sprite('Action_053_03', 3)	# 105-107
            sprite('Action_053_04', 5)	# 108-112
            sprite('Action_053_05', 7)	# 113-119
            sprite('Action_053_06', 8)	# 120-127
            sprite('Action_053_07', 3)	# 128-130
            SFX_1('ume700bjb')
            label(111)
            sprite('Action_053_08', 2)	# 131-132
            sprite('Action_053_09', 2)	# 133-134
            sprite('Action_053_10', 2)	# 135-136
            sprite('Action_053_11', 2)	# 137-138
            if SLOT_97:
                _gotolabel(111)
            sprite('Action_053_08', 1)	# 139-139
            Unknown2034(0)
            Unknown2053(0)
            Unknown21007(24, 40)
            Unknown21011(360)
            label(112)
            sprite('Action_053_08', 2)	# 140-141
            sprite('Action_053_09', 2)	# 142-143
            sprite('Action_053_10', 2)	# 144-145
            sprite('Action_053_11', 2)	# 146-147
            gotoLabel(112)
            label(120)
            sprite('Action_053_00', 2)	# 148-149	 **attackbox here**
            sprite('Action_053_01', 3)	# 150-152
            sprite('Action_053_02', 3)	# 153-155
            sprite('Action_053_03', 3)	# 156-158
            sprite('Action_053_04', 5)	# 159-163
            sprite('Action_053_05', 7)	# 164-170
            sprite('Action_053_06', 8)	# 171-178
            sprite('Action_053_07', 3)	# 179-181
            SFX_1('ume700bma')
            label(121)
            sprite('Action_053_08', 2)	# 182-183
            sprite('Action_053_09', 2)	# 184-185
            sprite('Action_053_10', 2)	# 186-187
            sprite('Action_053_11', 2)	# 188-189
            if SLOT_97:
                _gotolabel(121)
            sprite('Action_053_08', 1)	# 190-190
            Unknown21007(24, 40)
            Unknown21011(240)
            label(122)
            sprite('Action_053_08', 2)	# 191-192
            sprite('Action_053_09', 2)	# 193-194
            sprite('Action_053_10', 2)	# 195-196
            sprite('Action_053_11', 2)	# 197-198
            gotoLabel(122)
            label(130)
            sprite('Action_053_00', 2)	# 199-200	 **attackbox here**
            sprite('Action_053_01', 3)	# 201-203
            sprite('Action_053_02', 3)	# 204-206
            sprite('Action_053_03', 3)	# 207-209
            sprite('Action_053_04', 5)	# 210-214
            sprite('Action_053_05', 7)	# 215-221
            sprite('Action_053_06', 8)	# 222-229
            sprite('Action_053_07', 3)	# 230-232
            SFX_1('ume700pna')
            label(131)
            sprite('Action_053_08', 2)	# 233-234
            sprite('Action_053_09', 2)	# 235-236
            sprite('Action_053_10', 2)	# 237-238
            sprite('Action_053_11', 2)	# 239-240
            if SLOT_97:
                _gotolabel(131)
            sprite('Action_053_08', 1)	# 241-241
            Unknown21007(24, 40)
            Unknown21011(320)
            label(132)
            sprite('Action_053_08', 2)	# 242-243
            sprite('Action_053_09', 2)	# 244-245
            sprite('Action_053_10', 2)	# 246-247
            sprite('Action_053_11', 2)	# 248-249
            gotoLabel(132)
            label(140)
            sprite('Action_053_00', 2)	# 250-251	 **attackbox here**
            sprite('Action_053_01', 3)	# 252-254
            sprite('Action_053_02', 3)	# 255-257
            sprite('Action_053_03', 3)	# 258-260
            sprite('Action_053_04', 5)	# 261-265
            sprite('Action_053_05', 7)	# 266-272
            sprite('Action_053_06', 8)	# 273-280
            sprite('Action_053_07', 3)	# 281-283
            SFX_1('ume700rbl')
            label(141)
            sprite('Action_053_08', 2)	# 284-285
            sprite('Action_053_09', 2)	# 286-287
            sprite('Action_053_10', 2)	# 288-289
            sprite('Action_053_11', 2)	# 290-291
            if SLOT_97:
                _gotolabel(141)
            sprite('Action_053_08', 1)	# 292-292
            Unknown21007(24, 40)
            Unknown21011(150)
            label(142)
            sprite('Action_053_08', 2)	# 293-294
            sprite('Action_053_09', 2)	# 295-296
            sprite('Action_053_10', 2)	# 297-298
            sprite('Action_053_11', 2)	# 299-300
            gotoLabel(142)
            label(150)
            sprite('Action_000_00', 1)	# 301-301	 **attackbox here**

            def upon_40():
                clearUponHandler(40)
                sendToLabel(152)
            label(151)
            sprite('Action_000_00', 4)	# 302-305	 **attackbox here**
            sprite('Action_000_01', 4)	# 306-309
            sprite('Action_000_02', 4)	# 310-313
            sprite('Action_000_03', 4)	# 314-317
            sprite('Action_000_04', 4)	# 318-321
            sprite('Action_000_05', 4)	# 322-325
            sprite('Action_000_06', 4)	# 326-329
            sprite('Action_000_07', 4)	# 330-333
            sprite('Action_000_08', 4)	# 334-337
            sprite('Action_000_09', 4)	# 338-341
            sprite('Action_000_10', 4)	# 342-345
            sprite('Action_000_11', 4)	# 346-349
            sprite('Action_000_12', 4)	# 350-353
            sprite('Action_000_13', 4)	# 354-357
            sprite('Action_000_14', 4)	# 358-361
            sprite('Action_000_15', 4)	# 362-365
            sprite('Action_000_16', 4)	# 366-369
            sprite('Action_000_17', 4)	# 370-373
            loopRest()
            gotoLabel(151)
            label(152)
            sprite('Action_053_00', 2)	# 374-375	 **attackbox here**
            sprite('Action_053_01', 3)	# 376-378
            sprite('Action_053_02', 3)	# 379-381
            sprite('Action_053_03', 3)	# 382-384
            sprite('Action_053_04', 5)	# 385-389
            sprite('Action_053_05', 7)	# 390-396
            sprite('Action_053_06', 8)	# 397-404
            sprite('Action_053_07', 3)	# 405-407
            SFX_1('ume701uca')
            Unknown23018(1)
            label(153)
            sprite('Action_053_08', 2)	# 408-409
            sprite('Action_053_09', 2)	# 410-411
            sprite('Action_053_10', 2)	# 412-413
            sprite('Action_053_11', 2)	# 414-415
            gotoLabel(153)
            label(160)
            sprite('Action_053_00', 2)	# 416-417	 **attackbox here**
            sprite('Action_053_01', 3)	# 418-420
            sprite('Action_053_02', 3)	# 421-423
            sprite('Action_053_03', 3)	# 424-426
            sprite('Action_053_04', 5)	# 427-431
            sprite('Action_053_05', 7)	# 432-438
            sprite('Action_053_06', 8)	# 439-446
            sprite('Action_053_07', 3)	# 447-449
            SFX_1('ume700uva')
            label(161)
            sprite('Action_053_08', 2)	# 450-451
            sprite('Action_053_09', 2)	# 452-453
            sprite('Action_053_10', 2)	# 454-455
            sprite('Action_053_11', 2)	# 456-457
            if SLOT_97:
                _gotolabel(161)
            sprite('Action_053_08', 1)	# 458-458
            Unknown21007(24, 40)
            Unknown21011(370)
            label(162)
            sprite('Action_053_08', 2)	# 459-460
            sprite('Action_053_09', 2)	# 461-462
            sprite('Action_053_10', 2)	# 463-464
            sprite('Action_053_11', 2)	# 465-466
            gotoLabel(162)
            label(170)
            sprite('Action_053_00', 2)	# 467-468	 **attackbox here**
            sprite('Action_053_01', 3)	# 469-471
            sprite('Action_053_02', 3)	# 472-474
            sprite('Action_053_03', 3)	# 475-477
            sprite('Action_053_04', 5)	# 478-482
            sprite('Action_053_05', 7)	# 483-489
            sprite('Action_053_06', 8)	# 490-497
            sprite('Action_053_07', 3)	# 498-500
            SFX_1('ume700bha')
            label(171)
            sprite('Action_053_08', 2)	# 501-502
            sprite('Action_053_09', 2)	# 503-504
            sprite('Action_053_10', 2)	# 505-506
            sprite('Action_053_11', 2)	# 507-508
            if SLOT_97:
                _gotolabel(171)
            sprite('Action_053_08', 1)	# 509-509
            Unknown21007(24, 40)
            Unknown21011(320)
            label(172)
            sprite('Action_053_08', 2)	# 510-511
            sprite('Action_053_09', 2)	# 512-513
            sprite('Action_053_10', 2)	# 514-515
            sprite('Action_053_11', 2)	# 516-517
            gotoLabel(172)

        @State
        def CmnActLose():
            sprite('Action_248_00', 5)	# 1-5
            sprite('Action_248_01', 4)	# 6-9
            if SLOT_158:
                Unknown7006('ume403_0', 100, 879062389, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            sprite('Action_248_02', 3)	# 10-12
            sprite('Action_248_03', 6)	# 13-18
            sprite('Action_248_04', 4)	# 19-22
            teleportRelativeX(5000)
            sprite('Action_248_05', 5)	# 23-27
            teleportRelativeX(5000)
            sprite('Action_248_06', 3)	# 28-30
            teleportRelativeX(5000)
            sprite('Action_248_07', 7)	# 31-37
            teleportRelativeX(4800)
            sprite('Action_248_08', 6)	# 38-43
            Unknown23018(1)
            sprite('Action_248_09', 32767)	# 44-32810
