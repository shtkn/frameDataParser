@Subroutine
def PreInit():
    Unknown12019('75636100000000000000000000000000')

@Subroutine
def MatchInit():
    Health(18000)
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
    Unknown14015(0, 450000, -150000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -150000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -150000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -150000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 280000, -100000, 100000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 280000, -100000, 100000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 1500000, -100000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Unknown14005(1)
    Unknown14015(0, 1500000, -100000, 200000, 100, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(2000)
    Unknown15013(250)
    Unknown14015(0, 400000, 0, 300000, 750, 10)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 700000, -100000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(-150000, 450000, -150000, 170000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(-100000, 450000, -150000, 170000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-100000, 700000, -600000, 100000, 50, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B2nd', 0x22)
    Unknown14005(1)
    Unknown14015(-100000, 700000, -600000, 100000, 50, 20)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 200000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('RotationShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 750000, -150000, 250000, 100, 50)
    Move_EndRegister()
    Move_Register('RotationShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(600000, 1100000, -150000, 250000, 100, 50)
    Move_EndRegister()
    Move_Register('RotationShotEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(200000, 800000, -200000, 400000, 50, 20)
    Move_EndRegister()
    Move_Register('PushUpShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown14015(150000, 450000, -200000, 100000, 100, 50)
    Move_EndRegister()
    Move_Register('PushUpShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15009()
    Unknown14015(450000, 750000, -200000, 100000, 100, 50)
    Move_EndRegister()
    Move_Register('PushUpShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15009()
    Unknown14015(750000, 1050000, -200000, 100000, 100, 50)
    Move_EndRegister()
    Move_Register('AirRotationShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(300000, 750000, -150000, 250000, 100, 50)
    Move_EndRegister()
    Move_Register('AirRotationShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(600000, 1100000, -150000, 250000, 100, 50)
    Move_EndRegister()
    Move_Register('AirRotationShotEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3008)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(200000, 800000, -200000, 400000, 50, 20)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown14015(-350000, 350000, -100000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(100000, 1200000, -200000, 400000, 10, 0)
    Move_EndRegister()
    Move_Register('UltimateShot_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown14015(100000, 1200000, -200000, 400000, 10, 0)
    Move_EndRegister()
    Move_Register('PushUpShotDD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x300f)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(100000, 1200000, -200000, 100000, 10, 0)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('PushUpShotDD_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x300f)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown14015(100000, 1200000, -200000, 100000, 10, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5C', 'NmlAtkAIR5B', 10000000)
    Unknown12018(0, 'Action_330_00')
    Unknown12018(1, 'Action_330_01')
    Unknown12018(2, 'Action_330_04')
    Unknown12018(3, 'Action_330_05')
    Unknown12018(4, 'Action_330_06')
    Unknown12018(5, 'Action_330_07')
    Unknown12018(6, 'Action_330_08')
    Unknown12018(7, 'Action_017_00')
    Unknown12018(8, 'Action_017_00ex00')
    Unknown12018(9, 'Action_019_00')
    Unknown12018(10, 'Action_330_00')
    Unknown12018(11, 'Action_330_01')
    Unknown12018(12, 'Action_330_05')
    Unknown12018(13, 'Action_330_08')
    Unknown12018(14, 'Action_351_00')
    Unknown12018(15, 'Action_290_00')
    Unknown12018(16, 'Action_300_01')
    Unknown12018(17, 'Action_301_01')
    Unknown12018(18, 'Action_302_01')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_01')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_351_05')
    Unknown12018(29, 'Action_292_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'uca000')
    Unknown7010(1, 'uca001')
    Unknown7010(2, 'uca002')
    Unknown7010(3, 'uca003')
    Unknown7010(4, 'uca004')
    Unknown7010(5, 'uca005')
    Unknown7010(6, 'uca006')
    Unknown7010(7, 'uca007')
    Unknown7010(8, 'uca008')
    Unknown7010(9, 'uca009')
    Unknown7010(10, 'uca010')
    Unknown7010(15, 'uca011')
    Unknown7010(16, 'uca012')
    Unknown7010(17, 'uca013')
    Unknown7010(18, 'uca014')
    Unknown7010(19, 'uca015')
    Unknown7010(20, 'uca016')
    Unknown7010(21, 'uca017')
    Unknown7010(22, 'uca018')
    Unknown7010(23, 'uca019')
    Unknown7010(24, 'uca020')
    Unknown7010(25, 'uca021')
    Unknown7010(28, 'uca022')
    Unknown7010(29, 'uca023')
    Unknown7010(30, 'uca024')
    Unknown7010(31, 'uca025')
    Unknown7010(32, 'uca026')
    Unknown7010(33, 'uca027')
    Unknown7010(34, 'uca028')
    Unknown7010(35, 'uca029')
    Unknown7010(36, 'uca030')
    Unknown7010(37, 'uca031')
    Unknown7010(39, 'uca032')
    Unknown7010(42, 'uca033')
    Unknown7010(43, 'uca034')
    Unknown7010(44, 'uca035')
    Unknown7010(45, 'uca036')
    Unknown7010(46, 'uca037')
    Unknown7010(47, 'uca038')
    Unknown7010(48, 'uca039')
    Unknown7010(49, 'uca040')
    Unknown7010(50, 'uca041')
    Unknown7010(52, 'uca042')
    Unknown7010(53, 'uca043')
    Unknown7010(54, 'uca100_0')
    Unknown7010(55, 'uca100_1')
    Unknown7010(56, 'uca100_2')
    Unknown7010(63, 'uca101_0')
    Unknown7010(64, 'uca101_1')
    Unknown7010(65, 'uca101_2')
    Unknown7010(57, 'uca102_0')
    Unknown7010(58, 'uca102_1')
    Unknown7010(59, 'uca102_2')
    Unknown7010(66, 'uca103_0')
    Unknown7010(67, 'uca103_1')
    Unknown7010(68, 'uca103_2')
    Unknown7010(60, 'uca104_0')
    Unknown7010(61, 'uca104_1')
    Unknown7010(62, 'uca104_2')
    Unknown7010(69, 'uca105_0')
    Unknown7010(70, 'uca105_1')
    Unknown7010(71, 'uca105_2')
    Unknown7010(72, 'uca150')
    Unknown7010(73, 'uca151')
    Unknown7010(74, 'uca152')
    Unknown7010(85, 'uca153')
    Unknown7010(87, 'uca154')
    Unknown7010(88, 'uca155')
    Unknown7010(96, 'uca161_0')
    Unknown7010(97, 'uca161_1')
    Unknown7010(92, 'uca162_0')
    Unknown7010(93, 'uca162_1')
    Unknown7010(98, 'uca163_0')
    Unknown7010(99, 'uca163_1')
    Unknown7010(100, 'uca164_0')
    Unknown7010(101, 'uca164_1')
    Unknown7010(105, 'uca165_0')
    Unknown7010(106, 'uca165_1')
    Unknown7010(102, 'uca166_0')
    Unknown7010(103, 'uca166_1')
    Unknown7010(90, 'uca167_0')
    Unknown7010(91, 'uca167_1')
    Unknown7010(107, 'uca168_0')
    Unknown7010(108, 'uca168_1')
    Unknown7010(110, 'uca169_0')
    Unknown7010(111, 'uca169_1')
    Unknown7010(94, 'uca400_0')
    Unknown7010(95, 'uca400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745f4f440000000000000000000000000000000000')
    Unknown12059('0400000050757368557053686f7444440000000000000000000000000000000000000000')
    Unknown12059('0500000050757368557053686f7444445f4f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if (not SLOT_75):
            callSubroutine('DissolveAllDelete')

@Subroutine
def OnLanding():
    Unknown21015('4a425f4566660000000000000000000000000000000000000000000000000000fd26000000000000')
    Unknown21015('4a435f4566660000000000000000000000000000000000000000000000000000fd26000000000000')

@Subroutine
def OnEnemyComboBreak():
    if SLOT_62:
        SLOT_62 = 0

@Subroutine
def LifeDrain():
    if (not SLOT_62):
        op(3, 2, 161, 0, 100)
        op(2, 2, 0, 0, 35)
        if (SLOT_0 <= 500):
            Unknown21000(500)
            Unknown30030(500)
        else:
            Unknown30086(35)
    else:
        op(3, 2, 161, 0, 100)
        op(2, 2, 0, 0, 15)
        if (SLOT_0 <= 500):
            Unknown30078(500)
        else:
            Unknown30086(15)
    SLOT_62 = (SLOT_62 + 1)

@State
def CmnActStand():
    Unknown23145('CmnActBDash')
    if SLOT_0:
        _gotolabel(1)
    if (not 
    if (not 
    if (not 
    if (not 
    if (not Unknown23145('CmnActChangePartnerIn')):
        Unknown23145('CmnActChangePartnerBurst')):
        Unknown23145('CmnActCrushAttack')):
        Unknown23145('NmlAtkAIR5B')):
        Unknown23145('AirRotationShotA')):
        Unknown23145('AirRotationShotB')
    if SLOT_0:
        _gotolabel(2)
    label(0)
    sprite('Action_000_00', 7)	# 1-7	 **attackbox here**
    sprite('Action_000_01', 7)	# 8-14	 **attackbox here**
    sprite('Action_000_02', 8)	# 15-22	 **attackbox here**
    sprite('Action_000_03', 8)	# 23-30	 **attackbox here**
    sprite('Action_000_04', 10)	# 31-40	 **attackbox here**
    sprite('Action_000_05', 9)	# 41-49	 **attackbox here**
    sprite('Action_000_06', 11)	# 50-60	 **attackbox here**
    sprite('Action_000_07', 8)	# 61-68	 **attackbox here**
    sprite('Action_000_08', 7)	# 69-75	 **attackbox here**
    sprite('Action_000_09', 6)	# 76-81	 **attackbox here**
    sprite('Action_000_10', 7)	# 82-88	 **attackbox here**
    sprite('Action_000_11', 7)	# 89-95	 **attackbox here**
    sprite('Action_000_12', 8)	# 96-103	 **attackbox here**
    sprite('Action_000_13', 7)	# 104-110	 **attackbox here**
    sprite('Action_000_14', 7)	# 111-117	 **attackbox here**
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
    sprite('Action_000_16', 6)	# 118-123
    SLOT_88 = 960
    sprite('Action_000_17', 7)	# 124-130
    SFX_1('uca000')
    sprite('Action_000_18', 4)	# 131-134
    sprite('Action_000_19', 5)	# 135-139
    sprite('Action_000_20', 9)	# 140-148
    sprite('Action_000_21', 7)	# 149-155
    sprite('Action_000_22', 4)	# 156-159
    sprite('Action_000_23', 5)	# 160-164
    sprite('Action_000_24', 6)	# 165-170
    sprite('Action_000_25', 7)	# 171-177
    sprite('Action_000_26', 5)	# 178-182
    sprite('Action_000_27', 4)	# 183-186
    sprite('Action_000_28', 4)	# 187-190
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_221_00', 3)	# 191-193
    loopRest()
    label(2)
    sprite('Action_222_00', 3)	# 194-196
    sprite('Action_223_00', 3)	# 197-199
    sprite('Action_224_00', 3)	# 200-202
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 5)	# 1-5
    sprite('Action_015_01', 4)	# 6-9

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 2)	# 1-2
    sprite('Action_012_01', 3)	# 3-5
    sprite('Action_012_02', 3)	# 6-8

@State
def CmnActCrouch():
    sprite('Action_013_00', 30)	# 1-30
    label(0)
    sprite('Action_013_01', 5)	# 31-35
    sprite('Action_013_02', 10)	# 36-45
    sprite('Action_013_03', 10)	# 46-55
    sprite('Action_013_04', 15)	# 56-70
    sprite('Action_013_05', 3)	# 71-73
    sprite('Action_013_06', 5)	# 74-78
    sprite('Action_013_07', 5)	# 79-83
    sprite('Action_013_08', 5)	# 84-88
    sprite('Action_013_09', 10)	# 89-98
    sprite('Action_013_10', 10)	# 99-108
    sprite('Action_013_11', 15)	# 109-123
    sprite('Action_013_12', 7)	# 124-130
    sprite('Action_013_13', 5)	# 131-135
    sprite('Action_013_14', 5)	# 136-140
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 5)	# 1-5
    sprite('Action_016_01', 4)	# 6-9

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 3)	# 1-3
    sprite('Action_014_01', 3)	# 4-6
    sprite('Action_014_02', 3)	# 7-9
    sprite('Action_014_03', 3)	# 10-12
    sprite('Action_222_00', 3)	# 13-15
    sprite('Action_223_00', 3)	# 16-18
    sprite('Action_224_00', 3)	# 19-21

@State
def CmnActJumpPre():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_00', 4)	# 1-4
    ExitState()
    label(1)
    sprite('Action_035_00', 4)	# 5-8
    ExitState()
    label(2)
    sprite('Action_037_00', 4)	# 9-12
    ExitState()

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_01', 3)	# 1-3
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_01', 3)	# 4-6
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('Action_037_01', 3)	# 7-9
    loopRest()
    gotoLabel(2)

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_02', 3)	# 1-3
    sprite('Action_036_03', 3)	# 4-6
    sprite('Action_036_04', 3)	# 7-9
    sprite('Action_036_05', 3)	# 10-12
    loopRest()
    ExitState()
    label(1)
    sprite('Action_035_02', 3)	# 13-15
    sprite('Action_035_03', 3)	# 16-18
    sprite('Action_035_04', 3)	# 19-21
    sprite('Action_035_05', 3)	# 22-24
    loopRest()
    ExitState()
    label(2)
    sprite('Action_037_02', 3)	# 25-27
    sprite('Action_037_03', 3)	# 28-30
    sprite('Action_037_04', 3)	# 31-33
    sprite('Action_037_05', 3)	# 34-36
    loopRest()
    ExitState()

@State
def CmnActJumpDown():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_06', 3)	# 1-3
    loopRest()
    gotoLabel(3)
    label(1)
    sprite('Action_035_06', 3)	# 4-6
    loopRest()
    gotoLabel(3)
    label(2)
    sprite('Action_037_06', 3)	# 7-9
    loopRest()
    gotoLabel(3)
    label(3)
    sprite('Action_022_00', 3)	# 10-12
    sprite('Action_022_01', 3)	# 13-15
    loopRest()
    gotoLabel(3)

@State
def CmnActJumpLanding():
    sprite('Action_023_00', 2)	# 1-2
    sprite('Action_023_01', 3)	# 3-5
    sprite('Action_023_02', 5)	# 6-10
    sprite('Action_023_03', 5)	# 11-15
    sprite('Action_222_00', 3)	# 16-18
    sprite('Action_223_00', 3)	# 19-21
    sprite('Action_224_00', 3)	# 22-24

@State
def CmnActLandingStiffLoop():
    sprite('Action_023_00', 2)	# 1-2
    sprite('Action_023_01', 2)	# 3-4
    sprite('Action_023_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('Action_023_02', 3)	# 1-3
    sprite('Action_023_03', 3)	# 4-6
    sprite('Action_222_00', 3)	# 7-9
    sprite('Action_223_00', 3)	# 10-12
    sprite('Action_224_00', 3)	# 13-15

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 5)	# 1-5
    sprite('Action_010_01', 5)	# 6-10
    sprite('Action_010_02', 5)	# 11-15
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_03', 5)	# 16-20
    sprite('Action_010_04', 5)	# 21-25
    sprite('Action_010_05', 5)	# 26-30
    sprite('Action_010_06', 5)	# 31-35
    sprite('Action_010_07', 5)	# 36-40
    sprite('Action_010_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_09', 5)	# 46-50
    sprite('Action_010_10', 5)	# 51-55
    sprite('Action_010_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    label(0)
    sprite('Action_011_00', 5)	# 1-5
    sprite('Action_011_01', 5)	# 6-10
    sprite('Action_011_02', 5)	# 11-15
    sprite('Action_011_03', 5)	# 16-20
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_04', 5)	# 21-25
    sprite('Action_011_05', 5)	# 26-30
    sprite('Action_011_06', 5)	# 31-35
    sprite('Action_011_07', 5)	# 36-40
    sprite('Action_011_08', 5)	# 41-45
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_09', 5)	# 46-50
    sprite('Action_011_10', 5)	# 51-55
    sprite('Action_011_11', 5)	# 56-60
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_010_00', 2)	# 1-2
    sprite('Action_010_01', 2)	# 3-4
    sprite('Action_045_00', 2)	# 5-6
    sprite('Action_045_01', 2)	# 7-8
    label(0)
    sprite('Action_045_02', 4)	# 9-12
    sprite('Action_045_03', 4)	# 13-16
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 4)	# 17-20
    sprite('Action_045_05', 4)	# 21-24
    sprite('Action_045_06', 4)	# 25-28
    sprite('Action_045_07', 4)	# 29-32
    Unknown8006(100, 1, 1)
    sprite('Action_045_08', 4)	# 33-36
    sprite('Action_045_09', 4)	# 37-40
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_11', 2)	# 1-2
    sprite('Action_045_12', 2)	# 3-4
    sprite('Action_045_13', 3)	# 5-7
    sprite('Action_045_14', 5)	# 8-12
    sprite('Action_045_15', 3)	# 13-15
    sprite('Action_045_16', 2)	# 16-17

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
    sprite('Action_046_00', 3)	# 1-3
    sprite('Action_046_01', 3)	# 4-6
    physicsXImpulse(-18000)
    physicsYImpulse(6300)
    setGravity(1550)
    Unknown8002()
    sprite('Action_046_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('Action_046_03', 2)	# 10-11
    sprite('Action_046_04', 2)	# 12-13
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05', 2)	# 14-15
    sprite('Action_046_06', 4)	# 16-19
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_046_07', 2)	# 20-21
    sprite('Action_046_08', 4)	# 22-25
    sprite('Action_046_09', 3)	# 26-28

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('Action_068_01', 3)	# 1-3
    sprite('Action_068_01', 3)	# 4-6
    sprite('Action_068_02', 3)	# 7-9
    sprite('Action_068_03', 3)	# 10-12
    sprite('Action_068_04', 3)	# 13-15
    sprite('Action_068_05', 3)	# 16-18
    sprite('Action_068_06', 3)	# 19-21
    sprite('Action_068_07', 3)	# 22-24
    sprite('keep', 1)	# 25-25
    enterState('AirFDashRigor')

@State
def AirFDashRigor():

    def upon_IMMEDIATE():
        Unknown13014(1)
        Unknown13015(1)
        Unknown13031(1)
        Unknown13019(1)
        Unknown28(2, 'CmnActJumpLanding')
    sprite('Action_068_08', 3)	# 1-3
    sprite('Action_068_09', 3)	# 4-6
    sprite('Action_068_10', 32767)	# 7-32773

@State
def CmnActAirBDash():
    sprite('Action_046_00', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('Action_046_01', 3)	# 4-6
    sprite('Action_046_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('Action_046_03', 2)	# 10-11
    sprite('Action_046_04', 2)	# 12-13
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('Action_300_00', 1)	# 1-1
    sprite('Action_300_00', 1)	# 2-2
    sprite('Action_300_01', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('Action_300_00', 1)	# 1-1
    sprite('Action_300_00', 1)	# 2-2
    sprite('Action_300_01', 2)	# 3-4
    sprite('Action_300_01', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_01', 1)	# 2-2
    sprite('Action_303_02', 3)	# 3-5
    sprite('Action_303_03', 3)	# 6-8

@State
def CmnActHitStandLv4():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_01', 1)	# 2-2
    sprite('Action_303_02', 4)	# 3-6
    sprite('Action_303_03', 4)	# 7-10

@State
def CmnActHitStandLv5():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_01', 1)	# 2-2
    sprite('Action_303_02', 5)	# 3-7
    sprite('Action_303_03', 5)	# 8-12

@State
def CmnActHitStandLowLv1():
    sprite('Action_301_00', 1)	# 1-1
    sprite('Action_301_00', 1)	# 2-2
    sprite('Action_301_01', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('Action_301_00', 1)	# 1-1
    sprite('Action_301_00', 1)	# 2-2
    sprite('Action_301_01', 2)	# 3-4
    sprite('Action_301_01', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_01', 1)	# 2-2
    sprite('Action_304_02', 3)	# 3-5
    sprite('Action_304_03', 3)	# 6-8

@State
def CmnActHitStandLowLv4():
    sprite('Action_304_00', 1)	# 1-1
    sprite('Action_304_01', 1)	# 2-2
    sprite('Action_304_02', 4)	# 3-6
    sprite('Action_304_03', 4)	# 7-10

@State
def CmnActHitStandLowLv5():
    sprite('Action_303_00', 1)	# 1-1
    sprite('Action_303_01', 1)	# 2-2
    sprite('Action_303_02', 5)	# 3-7
    sprite('Action_303_03', 5)	# 8-12

@State
def CmnActHitCrouchLv1():
    sprite('Action_302_00', 1)	# 1-1
    sprite('Action_302_00', 1)	# 2-2
    sprite('Action_302_01', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('Action_302_00', 1)	# 1-1
    sprite('Action_302_00', 1)	# 2-2
    sprite('Action_302_01', 2)	# 3-4
    sprite('Action_302_01', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_01', 1)	# 2-2
    sprite('Action_305_02', 3)	# 3-5
    sprite('Action_305_03', 3)	# 6-8

@State
def CmnActHitCrouchLv4():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_01', 1)	# 2-2
    sprite('Action_305_02', 4)	# 3-6
    sprite('Action_305_03', 4)	# 7-10

@State
def CmnActHitCrouchLv5():
    sprite('Action_305_00', 1)	# 1-1
    sprite('Action_305_01', 1)	# 2-2
    sprite('Action_305_02', 5)	# 3-7
    sprite('Action_305_03', 5)	# 8-12

@State
def CmnActBDownUpper():
    sprite('Action_330_00', 3)	# 1-3
    label(0)
    sprite('Action_330_01', 3)	# 4-6
    sprite('Action_330_02', 3)	# 7-9
    sprite('Action_330_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('Action_330_04', 3)	# 1-3
    sprite('Action_330_05', 3)	# 4-6

@State
def CmnActBDownDown():
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_07', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 3)	# 7-9
    sprite('Action_330_09', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('Action_351_00', 2)	# 1-2
    sprite('Action_351_01', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('Action_351_02', 2)	# 1-2
    sprite('Action_351_03', 2)	# 3-4
    sprite('Action_351_04', 2)	# 5-6
    sprite('Action_351_05', 2)	# 7-8
    sprite('Action_352_00', 2)	# 9-10
    sprite('Action_352_01', 2)	# 11-12

@State
def CmnActBDownLoop():
    sprite('Action_352_02', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('Action_294_11', 3)	# 1-3
    sprite('Action_294_12', 3)	# 4-6
    sprite('Action_294_13', 3)	# 7-9
    sprite('Action_294_14', 3)	# 10-12
    sprite('Action_294_15', 3)	# 13-15
    sprite('Action_294_16', 3)	# 16-18
    sprite('Action_294_17', 2)	# 19-20

@State
def CmnActFDownUpper():
    sprite('Action_326_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('Action_326_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('Action_326_03', 3)	# 1-3
    sprite('Action_326_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('Action_354_00', 3)	# 1-3

@State
def CmnActFDownBound():
    sprite('Action_354_01', 3)	# 1-3
    sprite('Action_354_02', 3)	# 4-6
    sprite('Action_354_03', 3)	# 7-9

@State
def CmnActFDownLoop():
    sprite('Action_292_00', 2)	# 1-2

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
    sprite('Action_330_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('Action_330_04', 3)	# 1-3
    sprite('Action_330_05', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_07', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 3)	# 7-9
    sprite('Action_330_09', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('Action_351_00', 3)	# 1-3
    sprite('Action_351_01', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('Action_331_00', 3)	# 1-3
    label(0)
    sprite('Action_331_02', 3)	# 4-6
    sprite('Action_331_03', 3)	# 7-9
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
    sprite('Action_330_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('Action_340_00', 3)	# 1-3
    sprite('Action_340_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('Action_340_02', 3)	# 1-3
    label(0)
    sprite('Action_340_03', 3)	# 4-6
    sprite('Action_340_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    label(0)
    sprite('Action_327_00', 3)	# 1-3
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('Action_327_01', 5)	# 1-5
    sprite('Action_327_02', 5)	# 6-10
    sprite('Action_327_03', 3)	# 11-13
    sprite('Action_327_04', 3)	# 14-16
    sprite('Action_328_00', 4)	# 17-20
    sprite('Action_328_01', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('Action_327_00', 4)	# 1-4
    sprite('Action_306_03', 4)	# 5-8

@State
def CmnActUkemiAirF():
    sprite('Action_032_00', 3)	# 1-3
    sprite('Action_032_01', 2)	# 4-5
    sprite('Action_032_02', 2)	# 6-7
    sprite('Action_032_03', 3)	# 8-10
    sprite('Action_032_04', 3)	# 11-13
    sprite('Action_032_05', 2)	# 14-15
    sprite('Action_032_06', 2)	# 16-17

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 3)	# 1-3
    sprite('Action_032_01', 2)	# 4-5
    sprite('Action_032_02', 2)	# 6-7
    sprite('Action_032_03', 3)	# 8-10
    sprite('Action_032_04', 3)	# 11-13
    sprite('Action_032_05', 2)	# 14-15
    sprite('Action_032_06', 2)	# 16-17

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 3)	# 1-3
    sprite('Action_032_01', 2)	# 4-5
    sprite('Action_032_02', 2)	# 6-7
    sprite('Action_032_03', 3)	# 8-10
    sprite('Action_032_04', 3)	# 11-13
    sprite('Action_032_05', 2)	# 14-15
    sprite('Action_032_06', 2)	# 16-17

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14
    sprite('Action_041_07', 2)	# 15-16

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14
    sprite('Action_041_07', 2)	# 15-16

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14
    sprite('Action_041_07', 2)	# 15-16

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_08', 3)	# 1-3
    sprite('Action_041_09', 3)	# 4-6
    sprite('Action_041_10', 3)	# 7-9
    sprite('Action_041_11', 2)	# 10-11
    sprite('Action_041_12', 2)	# 12-13
    sprite('Action_041_13', 2)	# 14-15

@State
def CmnActMidGuardPre():
    sprite('Action_017_07', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_01', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('Action_017_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_01', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighGuardPre():
    sprite('Action_017_07', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_01', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('Action_017_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('Action_017_04', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_05', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_07', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('Action_018_02', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_03', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('Action_018_04', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_05', 3)	# 4-6	 **attackbox here**
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirGuardPre():
    sprite('Action_019_07', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_06', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('Action_019_02', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_03', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('Action_019_04', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_05', 3)	# 4-6	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActGuardBreakStand():
    sprite('Action_017_06', 2)	# 1-2	 **attackbox here**
    sprite('Action_017_00', 2)	# 3-4	 **attackbox here**
    sprite('Action_017_01', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_017_00', 4)	# 6-9	 **attackbox here**
    sprite('Action_017_06', 4)	# 10-13	 **attackbox here**
    sprite('Action_017_07', 4)	# 14-17	 **attackbox here**

@State
def CmnActGuardBreakCrouch():
    sprite('Action_018_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_018_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_018_00', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_018_01', 6)	# 6-11	 **attackbox here**
    sprite('Action_018_00', 6)	# 12-17	 **attackbox here**

@State
def CmnActGuardBreakAir():
    sprite('Action_019_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_019_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_019_00', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_019_01', 6)	# 6-11	 **attackbox here**
    sprite('Action_019_00', 6)	# 12-17	 **attackbox here**

@State
def CmnActAirTurn():
    sprite('Action_036_01', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_017_06', 3)	# 4-6	 **attackbox here**
    sprite('Action_017_07', 3)	# 7-9	 **attackbox here**

@State
def CmnActLockReject():
    sprite('Action_402_00', 3)	# 1-3
    sprite('Action_402_01', 3)	# 4-6
    sprite('Action_402_05', 3)	# 7-9	 **attackbox here**
    sprite('Action_402_06', 3)	# 10-12	 **attackbox here**
    sprite('Action_402_07', 3)	# 13-15
    sprite('Action_402_08', 3)	# 16-18
    sprite('Action_402_09', 3)	# 19-21
    sprite('Action_402_10', 3)	# 22-24
    sprite('Action_402_11', 3)	# 25-27

@State
def CmnActAirLockWait():
    sprite('Action_019_05', 3)	# 1-3	 **attackbox here**
    sprite('Action_019_06', 3)	# 4-6	 **attackbox here**
    sprite('Action_019_07', 3)	# 7-9	 **attackbox here**

@State
def CmnActLandSpin():
    sprite('jb071_00', 4)	# 1-4
    sprite('jb071_01', 4)	# 5-8
    label(0)
    sprite('jb071_02', 2)	# 9-10
    sprite('jb071_03', 2)	# 11-12
    sprite('jb071_04', 2)	# 13-14
    sprite('jb071_05', 2)	# 15-16
    sprite('jb071_06', 2)	# 17-18
    sprite('jb071_07', 2)	# 19-20
    sprite('jb071_08', 2)	# 21-22
    sprite('jb071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('jb071_10', 6)	# 1-6
    sprite('jb071_11', 5)	# 7-11
    sprite('jb071_12', 5)	# 12-16

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
    label(0)
    sprite('jb060_07', 3)	# 1-3
    sprite('jb060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('jb060_13', 4)	# 1-4
    sprite('jb060_14', 5)	# 5-9

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
    sprite('Action_022_00', 3)	# 13-15
    sprite('Action_022_01', 3)	# 16-18
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
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

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
    sprite('Action_022_00', 3)	# 13-15
    sprite('Action_022_01', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('Action_262_00', 4)	# 1-4
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

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
    sprite('Action_262_05', 6)	# 1-6
    sprite('Action_262_06', 6)	# 7-12

@State
def CmnActAirCrossChangeBegin():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
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
    sprite('Action_262_07', 6)	# 1-6
    sprite('Action_262_08', 6)	# 7-12
    label(0)
    sprite('Action_022_00', 3)	# 13-15
    sprite('Action_022_01', 3)	# 16-18
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
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('Action_009_14', 3)	# 26-28
    Unknown1086(22)
    teleportRelativeX(-120000)
    teleportRelativeY(2000000)
    physicsYImpulse(-200000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    sprite('Action_009_15', 2)	# 29-30
    sprite('Action_009_16', 1)	# 31-31
    sprite('Action_009_17', 1)	# 32-32
    sprite('Action_009_18', 2)	# 33-34	 **attackbox here**
    GFX_0('JC_Eff', -1)
    SFX_3('SE043')
    sprite('Action_009_19', 32767)	# 35-32801	 **attackbox here**
    label(9)
    sprite('Action_009_19', 1)	# 32802-32802	 **attackbox here**
    sprite('keep', 2)	# 32803-32804
    Unknown1084(1)
    sprite('Action_021_00', 5)	# 32805-32809
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_021_01', 6)	# 32810-32815
    sprite('Action_021_02', 6)	# 32816-32821
    Unknown18009(0)
    sprite('Action_021_03', 5)	# 32822-32826

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_03', 3)	# 1-3
    sprite('Action_045_04', 4)	# 4-7
    sprite('Action_045_05', 5)	# 8-12
    sprite('Action_045_11', 2)	# 13-14
    sprite('Action_045_12', 2)	# 15-16
    sprite('Action_045_13', 3)	# 17-19
    sprite('Action_045_14', 5)	# 20-24
    sprite('Action_045_15', 3)	# 25-27
    sprite('Action_045_16', 2)	# 28-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('Action_046_00', 3)	# 1-3
    sprite('Action_046_01', 3)	# 4-6
    sprite('Action_046_02', 3)	# 7-9
    label(0)
    sprite('Action_046_03', 2)	# 10-11
    sprite('Action_046_04', 2)	# 12-13
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_05', 2)	# 14-15
    sprite('Action_046_06', 2)	# 16-17
    sprite('Action_046_07', 2)	# 18-19
    sprite('Action_046_08', 2)	# 20-21
    sprite('Action_046_09', 2)	# 22-23

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
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
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_000_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_053_19', 5)	# 3-7
    sprite('Action_053_20', 6)	# 8-13
    sprite('Action_053_21', 5)	# 14-18
    sprite('Action_053_22', 6)	# 19-24
    sprite('Action_053_23', 5)	# 25-29
    sprite('Action_053_24', 5)	# 30-34
    sprite('Action_053_25', 4)	# 35-38
    sprite('Action_053_26', 5)	# 39-43
    sprite('Action_053_27', 4)	# 44-47
    sprite('Action_053_26', 5)	# 48-52
    sprite('Action_053_27', 4)	# 53-56
    sprite('Action_053_26', 5)	# 57-61
    sprite('Action_053_25', 4)	# 62-65
    sprite('Action_053_24', 5)	# 66-70
    sprite('Action_053_19', 4)	# 71-74
    sprite('Action_000_00', 22)	# 75-96	 **attackbox here**

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
    sprite('Action_022_00', 4)	# 3-6
    Unknown1019(95)
    sprite('Action_022_01', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('Action_023_02', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@Subroutine
def DissolveActivate5B2nd_PS():
    if Unknown46(4):
        GFX_0('6BB_PS_Eff', -1)
        Unknown1087(1, 4)
        Unknown36(1)
        teleportRelativeX(90000)
        Unknown35()
    if Unknown46(5):
        GFX_0('6BB_PS_Eff', -1)
        Unknown1087(1, 5)
        Unknown36(1)
        teleportRelativeX(90000)
        Unknown35()
    if Unknown46(6):
        GFX_0('6BB_PS_Eff', -1)
        Unknown1087(1, 6)
        Unknown36(1)
        teleportRelativeX(90000)
        Unknown35()
    if Unknown46(7):
        GFX_0('6BB_PS_Eff', -1)
        Unknown1087(1, 7)
        Unknown36(1)
        teleportRelativeX(90000)
        Unknown35()
    if Unknown46(8):
        GFX_0('6BB_PS_Eff', -1)
        Unknown1087(1, 8)
        Unknown36(1)
        teleportRelativeX(90000)
        Unknown35()

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_130_00', 6)	# 1-6
    sprite('Action_130_01', 8)	# 7-14
    Unknown7007('7563613230305f300000000000000000640000007563613230305f310000000000000000640000007563613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_130_02', 1)	# 15-15
    Unknown21015('526f746174696f6e53686f744c616e64410000000000000000000000000000001c05000000000000')
    Unknown21015('526f746174696f6e53686f744c616e64420000000000000000000000000000001c05000000000000')
    Unknown21015('526f746174696f6e53686f744c616e64430000000000000000000000000000001c05000000000000')
    Unknown21015('526f746174696f6e53686f7441697241000000000000000000000000000000001c05000000000000')
    Unknown21015('526f746174696f6e53686f7441697242000000000000000000000000000000001c05000000000000')
    Unknown21015('526f746174696f6e53686f7441697243000000000000000000000000000000001c05000000000000')
    Unknown21015('526f746174696f6e53686f744c616e64415f50530000000000000000000000001c05000000000000')
    callSubroutine('DissolveActivateRS_PS')
    GFX_0('RotationShot_Eff', -1)
    Unknown23029(1, 1307, 0)
    Unknown38(5, 1)
    selfDamage(500)
    SFX_3('SE045')
    sprite('Action_130_03', 3)	# 16-18
    sprite('Action_130_04', 6)	# 19-24
    sprite('Action_130_05', 8)	# 25-32
    sprite('Action_130_06', 7)	# 33-39
    sprite('Action_130_07', 4)	# 40-43

@Subroutine
def DissolveActivateRS_PS():
    if Unknown46(4):
        Unknown23029(4, 9993, 0)
    if Unknown46(5):
        Unknown23029(5, 9993, 0)
    if Unknown46(6):
        Unknown23029(6, 9993, 0)
    if Unknown46(7):
        Unknown23029(7, 9993, 0)
    if Unknown46(8):
        Unknown23029(8, 9993, 0)

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2004(1, 0)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('Action_150_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_150_12', 3)	# 5-7	 **attackbox here**
    Unknown7007('7563613230365f300000000000000000640000007563613230365f310000000000000000640000007563613230365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_150_13', 1)	# 8-8	 **attackbox here**
    sprite('Action_150_13', 1)	# 9-9	 **attackbox here**
    GFX_0('DoubleShot1st_Eff', -1)
    Unknown23029(1, 1491, 0)
    SFX_3('SE042')
    sprite('Action_150_14', 7)	# 10-16
    sprite('Action_150_15', 5)	# 17-21
    sprite('Action_150_16', 7)	# 22-28
    sprite('Action_150_17', 1)	# 29-29
    sprite('Action_150_17', 1)	# 30-30
    GFX_0('DoubleShot2nd_Eff', -1)
    Unknown23029(1, 1493, 0)
    SFX_3('SE043')
    sprite('Action_150_18', 4)	# 31-34
    sprite('Action_150_19', 11)	# 35-45
    sprite('Action_150_20', 10)	# 46-55
    sprite('Action_150_21', 10)	# 56-65
    sprite('Action_150_22', 8)	# 66-73

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirPushbackX(12000)
        AirPushbackY(-80000)
        Unknown9190(1)
        Unknown9118(30)
        AirUntechableTime(60)
        Unknown9016(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown11056(2)
        Unknown11042(1)
        Unknown30040(1)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
            Unknown2015(-1)
    sprite('Action_045_00', 2)	# 1-2
    sprite('Action_045_01', 2)	# 3-4
    sprite('Action_045_02', 2)	# 5-6
    Unknown8006(100, 1, 1)
    physicsXImpulse(40000)
    sprite('Action_045_03', 2)	# 7-8
    sprite('Action_094_18', 2)	# 9-10
    sprite('Action_094_19', 2)	# 11-12
    sprite('Action_094_20', 1)	# 13-13
    Unknown1019(50)
    sprite('Action_094_21', 1)	# 14-14
    Unknown2015(150)
    sprite('Action_094_22', 1)	# 15-15
    Unknown1019(30)
    GFX_0('5AAA_Eff_NPS', -1)
    SFX_3('SE043')
    sprite('Action_094_23', 1)	# 16-16
    sprite('Action_094_24', 1)	# 17-17
    Unknown7009(5)
    sprite('Action_094_25', 7)	# 18-24	 **attackbox here**
    Unknown1019(0)
    sprite('Action_094_26', 2)	# 25-26
    sprite('Action_094_27', 5)	# 27-31
    sprite('Action_094_28', 5)	# 32-36
    sprite('Action_094_29', 4)	# 37-40
    sprite('Action_094_30', 3)	# 41-43
    Unknown2015(-1)
    sprite('Action_222_00', 4)	# 44-47
    sprite('Action_223_00', 4)	# 48-51
    sprite('Action_224_00', 4)	# 52-55

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
    Unknown2036(95, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-260000)
    Unknown1019(4)
    label(0)
    sprite('Action_022_00', 4)	# 3-6
    sprite('Action_022_01', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    Unknown1084(1)
    if SLOT_58:
        enterState('ChangePartnerDDOD_Exe')
    else:
        enterState('ChangePartnerDD_Exe')

@State
def ChangePartnerDD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 2501):
                clearUponHandler(43)
                Unknown2037(1)
        Unknown2021(1)

        def upon_STATE_END():
            Unknown23029(11, 2502, 0)
    sprite('Action_250_00', 3)	# 1-3
    sprite('Action_250_00', 12)	# 4-15
    sprite('Action_250_00', 5)	# 16-20
    sprite('Action_250_01', 7)	# 21-27
    sprite('Action_250_02', 7)	# 28-34
    sprite('Action_250_03', 7)	# 35-41
    sprite('Action_250_04', 7)	# 42-48
    sprite('Action_250_05', 3)	# 49-51	 **attackbox here**
    SFX_3('SE012')
    sprite('Action_250_06', 3)	# 52-54	 **attackbox here**
    sprite('Action_250_07', 3)	# 55-57	 **attackbox here**
    sprite('Action_250_08', 2)	# 58-59	 **attackbox here**
    sprite('Action_250_08', 1)	# 60-60	 **attackbox here**
    GFX_0('UltimateShotEffMaster', -1)
    Unknown23029(1, 2504, 0)
    sprite('Action_250_09', 2)	# 61-62
    SFX_3('SE045')
    sprite('Action_250_10', 3)	# 63-65
    sprite('Action_250_11', 3)	# 66-68
    GFX_0('UltimateShotFootEff', -1)
    Unknown38(11, 1)
    Unknown23029(1, 2504, 0)
    sprite('Action_250_12', 2)	# 69-70
    sprite('Action_250_13', 3)	# 71-73
    sprite('Action_250_14', 3)	# 74-76
    sprite('Action_250_15', 3)	# 77-79
    sprite('Action_250_16', 3)	# 80-82
    sprite('Action_250_17', 3)	# 83-85
    sprite('Action_250_18', 2)	# 86-87	 **attackbox here**
    StartMultihit()
    sprite('Action_250_18', 1)	# 88-88	 **attackbox here**
    StartMultihit()
    if SLOT_2:
        sendToLabel(1)
    sprite('Action_250_20', 3)	# 89-91
    setInvincible(0)
    sprite('Action_250_21', 3)	# 92-94
    sprite('Action_250_22', 3)	# 95-97
    sprite('Action_250_20', 3)	# 98-100
    sprite('Action_250_21', 3)	# 101-103
    sprite('Action_250_22', 3)	# 104-106
    sprite('Action_250_20', 3)	# 107-109
    sprite('Action_250_21', 3)	# 110-112
    sprite('Action_250_22', 3)	# 113-115
    sprite('Action_250_20', 3)	# 116-118
    sprite('Action_250_21', 3)	# 119-121
    sprite('Action_250_22', 3)	# 122-124
    sprite('Action_250_23', 3)	# 125-127
    sprite('Action_250_24', 5)	# 128-132
    Unknown23029(11, 2502, 0)
    sprite('Action_250_25', 5)	# 133-137
    ExitState()
    label(1)
    sprite('Action_250_27', 3)	# 138-140
    sprite('Action_250_28', 3)	# 141-143
    sprite('Action_250_29', 3)	# 144-146
    sprite('Action_250_27', 3)	# 147-149
    GFX_0('UltimateShotAtkExe', -1)
    Unknown23029(1, 2504, 0)
    SFX_4('uca251_0')
    sprite('Action_250_28', 3)	# 150-152
    sprite('Action_250_29', 3)	# 153-155
    sprite('Action_250_30', 3)	# 156-158
    sprite('Action_250_31', 3)	# 159-161
    sprite('Action_250_32', 3)	# 162-164
    sprite('Action_250_33', 3)	# 165-167
    sprite('Action_250_34', 3)	# 168-170
    sprite('Action_250_35', 3)	# 171-173
    sprite('Action_250_36', 3)	# 174-176
    sprite('Action_250_37', 3)	# 177-179
    sprite('Action_250_38', 3)	# 180-182
    sprite('Action_250_39', 3)	# 183-185
    sprite('Action_250_40', 3)	# 186-188
    sprite('Action_250_41', 3)	# 189-191
    sprite('Action_250_42', 3)	# 192-194
    sprite('Action_250_43', 3)	# 195-197
    sprite('Action_250_44', 3)	# 198-200
    sprite('Action_250_45', 3)	# 201-203
    sprite('Action_250_46', 3)	# 204-206
    sprite('Action_250_47', 3)	# 207-209
    sprite('Action_250_48', 3)	# 210-212
    sprite('Action_250_49', 3)	# 213-215
    sprite('Action_250_50', 3)	# 216-218
    sprite('Action_250_48', 3)	# 219-221
    sprite('Action_250_49', 3)	# 222-224
    sprite('Action_250_50', 3)	# 225-227
    sprite('Action_250_51', 3)	# 228-230
    sprite('Action_250_52', 2)	# 231-232
    sprite('Action_250_53', 2)	# 233-234
    sprite('Action_250_54', 5)	# 235-239
    sprite('Action_250_55', 9)	# 240-248
    sprite('Action_250_56', 15)	# 249-263
    GFX_0('WinEff1', -1)
    sprite('Action_250_57', 4)	# 264-267
    GFX_0('UltimateShotAtkFinish', -1)
    Unknown23029(1, 2504, 0)
    sprite('Action_250_58', 3)	# 268-270
    GFX_0('WinEff2', -1)
    sprite('Action_250_59', 3)	# 271-273
    sprite('Action_250_60', 3)	# 274-276
    SFX_4('uca252_0')
    sprite('Action_250_61', 3)	# 277-279
    sprite('Action_250_60', 3)	# 280-282
    sprite('Action_250_61', 3)	# 283-285
    sprite('Action_250_60', 3)	# 286-288
    sprite('Action_250_61', 3)	# 289-291
    sprite('Action_250_60', 3)	# 292-294
    sprite('Action_250_61', 3)	# 295-297
    sprite('Action_250_60', 3)	# 298-300
    sprite('Action_250_61', 3)	# 301-303
    sprite('Action_250_60', 3)	# 304-306
    sprite('Action_250_61', 3)	# 307-309
    sprite('Action_250_60', 3)	# 310-312
    sprite('Action_250_61', 3)	# 313-315
    sprite('Action_250_60', 3)	# 316-318
    sprite('Action_250_61', 3)	# 319-321
    sprite('Action_250_62', 3)	# 322-324
    sprite('Action_250_63', 6)	# 325-330
    Unknown23029(11, 2502, 0)
    sprite('Action_250_64', 4)	# 331-334

@State
def ChangePartnerDDOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 2501):
                clearUponHandler(43)
                Unknown2037(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown2021(1)

        def upon_STATE_END():
            Unknown23029(11, 2502, 0)
    sprite('Action_250_00', 3)	# 1-3
    sprite('Action_250_00', 12)	# 4-15
    sprite('Action_250_00', 5)	# 16-20
    sprite('Action_250_01', 7)	# 21-27
    sprite('Action_250_02', 7)	# 28-34
    sprite('Action_250_03', 7)	# 35-41
    sprite('Action_250_04', 7)	# 42-48
    sprite('Action_250_05', 3)	# 49-51	 **attackbox here**
    SFX_3('SE012')
    sprite('Action_250_06', 3)	# 52-54	 **attackbox here**
    sprite('Action_250_07', 3)	# 55-57	 **attackbox here**
    sprite('Action_250_08', 2)	# 58-59	 **attackbox here**
    sprite('Action_250_08', 1)	# 60-60	 **attackbox here**
    GFX_0('UltimateShotEffMaster', -1)
    Unknown23029(1, 2506, 0)
    sprite('Action_250_09', 2)	# 61-62
    SFX_3('SE045')
    sprite('Action_250_10', 3)	# 63-65
    sprite('Action_250_11', 3)	# 66-68
    GFX_0('UltimateShotFootEff', -1)
    Unknown38(11, 1)
    Unknown23029(1, 2506, 0)
    sprite('Action_250_12', 2)	# 69-70
    sprite('Action_250_13', 3)	# 71-73
    sprite('Action_250_14', 3)	# 74-76
    sprite('Action_250_15', 3)	# 77-79
    sprite('Action_250_16', 3)	# 80-82
    sprite('Action_250_17', 3)	# 83-85
    sprite('Action_250_18', 2)	# 86-87	 **attackbox here**
    StartMultihit()
    sprite('Action_250_18', 1)	# 88-88	 **attackbox here**
    StartMultihit()
    if SLOT_2:
        sendToLabel(1)
    sprite('Action_250_20', 3)	# 89-91
    setInvincible(0)
    sprite('Action_250_21', 3)	# 92-94
    sprite('Action_250_22', 3)	# 95-97
    sprite('Action_250_20', 3)	# 98-100
    sprite('Action_250_21', 3)	# 101-103
    sprite('Action_250_22', 3)	# 104-106
    sprite('Action_250_20', 3)	# 107-109
    sprite('Action_250_21', 3)	# 110-112
    sprite('Action_250_22', 3)	# 113-115
    sprite('Action_250_20', 3)	# 116-118
    sprite('Action_250_21', 3)	# 119-121
    sprite('Action_250_22', 3)	# 122-124
    sprite('Action_250_23', 3)	# 125-127
    sprite('Action_250_24', 5)	# 128-132
    Unknown23029(11, 2502, 0)
    sprite('Action_250_25', 5)	# 133-137
    ExitState()
    label(1)
    sprite('Action_250_27', 3)	# 138-140
    sprite('Action_250_28', 3)	# 141-143
    sprite('Action_250_29', 3)	# 144-146
    sprite('Action_250_27', 3)	# 147-149
    GFX_0('UltimateShotAtkExe', -1)
    Unknown23029(1, 2506, 0)
    SFX_4('uca251_0')
    sprite('Action_250_28', 3)	# 150-152
    sprite('Action_250_29', 3)	# 153-155
    sprite('Action_250_30', 3)	# 156-158
    sprite('Action_250_31', 3)	# 159-161
    sprite('Action_250_32', 3)	# 162-164
    sprite('Action_250_33', 3)	# 165-167
    sprite('Action_250_34', 3)	# 168-170
    sprite('Action_250_35', 3)	# 171-173
    sprite('Action_250_36', 3)	# 174-176
    sprite('Action_250_37', 3)	# 177-179
    sprite('Action_250_38', 3)	# 180-182
    sprite('Action_250_39', 3)	# 183-185
    sprite('Action_250_40', 3)	# 186-188
    sprite('Action_250_41', 3)	# 189-191
    sprite('Action_250_42', 3)	# 192-194
    sprite('Action_250_43', 3)	# 195-197
    sprite('Action_250_44', 3)	# 198-200
    sprite('Action_250_45', 3)	# 201-203
    sprite('Action_250_46', 3)	# 204-206
    sprite('Action_250_47', 3)	# 207-209
    sprite('Action_250_48', 3)	# 210-212
    sprite('Action_250_49', 3)	# 213-215
    sprite('Action_250_50', 3)	# 216-218
    sprite('Action_250_51', 3)	# 219-221
    sprite('Action_250_52', 2)	# 222-223
    sprite('Action_260_00', 9)	# 224-232
    sprite('Action_260_01', 3)	# 233-235
    sprite('Action_260_02', 2)	# 236-237
    sprite('Action_260_03', 5)	# 238-242
    sprite('Action_260_04', 5)	# 243-247
    sprite('Action_260_05', 5)	# 248-252
    sprite('Action_260_06', 5)	# 253-257
    sprite('Action_260_07', 5)	# 258-262
    sprite('Action_260_08', 5)	# 263-267
    sprite('Action_260_09', 3)	# 268-270
    sprite('Action_260_10', 3)	# 271-273
    sprite('Action_260_11', 3)	# 274-276
    sprite('Action_260_12', 3)	# 277-279
    sprite('Action_250_53', 2)	# 280-281
    sprite('Action_250_54', 5)	# 282-286
    sprite('Action_250_55', 9)	# 287-295
    sprite('Action_250_56', 15)	# 296-310
    GFX_0('WinEff1', -1)
    sprite('Action_250_57', 4)	# 311-314
    GFX_0('UltimateShotAtkFinish', -1)
    Unknown23029(1, 2506, 0)
    SFX_4('uca252_0')
    sprite('Action_250_58', 3)	# 315-317
    GFX_0('WinEff2', -1)
    sprite('Action_250_59', 3)	# 318-320
    sprite('Action_250_60', 3)	# 321-323
    sprite('Action_250_61', 3)	# 324-326
    sprite('Action_250_60', 3)	# 327-329
    sprite('Action_250_61', 3)	# 330-332
    sprite('Action_250_60', 3)	# 333-335
    sprite('Action_250_61', 3)	# 336-338
    sprite('Action_250_60', 3)	# 339-341
    sprite('Action_250_61', 3)	# 342-344
    sprite('Action_250_60', 3)	# 345-347
    sprite('Action_250_61', 3)	# 348-350
    sprite('Action_250_60', 3)	# 351-353
    sprite('Action_250_61', 3)	# 354-356
    sprite('Action_250_60', 3)	# 357-359
    sprite('Action_250_61', 3)	# 360-362
    sprite('Action_250_60', 3)	# 363-365
    sprite('Action_250_61', 3)	# 366-368
    sprite('Action_250_60', 3)	# 369-371
    sprite('Action_250_61', 3)	# 372-374
    sprite('Action_250_62', 3)	# 375-377
    sprite('Action_250_63', 6)	# 378-383
    Unknown23029(11, 2502, 0)
    sprite('Action_250_64', 3)	# 384-386

@State
def CmnActChangeRequest():
    pass

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
    sprite('Action_022_00', 4)	# 121-124
    Unknown1086(22)
    teleportRelativeX(-120000)
    Unknown1007(2400000)
    physicsYImpulse(-85714)
    setGravity(0)
    Unknown2053(1)
    sprite('Action_022_01', 4)	# 125-128
    sprite('Action_022_00', 4)	# 129-132
    sprite('Action_022_01', 3)	# 133-135
    sprite('Action_009_14', 3)	# 136-138
    sprite('Action_009_15', 2)	# 139-140
    sprite('Action_009_16', 1)	# 141-141
    sprite('Action_009_17', 1)	# 142-142
    sprite('Action_009_18', 2)	# 143-144	 **attackbox here**
    GFX_0('JC_Burst_Eff', -1)
    SFX_3('SE043')
    sprite('Action_009_19', 32767)	# 145-32911	 **attackbox here**
    label(9)
    sprite('keep', 3)	# 32912-32914
    Unknown1084(1)
    Unknown21015('4a435f42757273745f4566660000000000000000000000000000000000000000fd26000000000000')
    sprite('Action_021_00', 6)	# 32915-32920
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_021_01', 9)	# 32921-32929
    sprite('Action_021_02', 7)	# 32930-32936
    Unknown18009(0)
    sprite('Action_021_03', 7)	# 32937-32943

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_031_00', 3)	# 1-3
    sprite('Action_031_01', 3)	# 4-6
    sprite('Action_031_02', 44)	# 7-50
    sprite('Action_031_04', 5)	# 51-55
    sprite('Action_000_00', 25)	# 56-80	 **attackbox here**

@Subroutine
def PassingLink():
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1100)
        AttackP2(85)
        AirPushbackX(7500)
        AirPushbackY(15000)
        Unknown11050('0200000065665f6869746d6d5f7465737400000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A2nd')
        callSubroutine('PassingLink')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown2015(150)

        def upon_STATE_END():
            Unknown2015(-1)
    sprite('Action_002_00', 1)	# 1-1
    sprite('Action_002_01', 2)	# 2-3
    sprite('Action_002_02', 2)	# 4-5
    Unknown7009(0)
    sprite('Action_002_03', 1)	# 6-6
    GFX_0('5B_Eff', -1)
    SFX_3('SE042')
    sprite('Action_002_04', 1)	# 7-7
    sprite('Action_002_05', 1)	# 8-8
    sprite('Action_002_06', 3)	# 9-11	 **attackbox here**
    sprite('Action_002_07', 6)	# 12-17
    Recovery()
    Unknown2063()
    sprite('Action_002_08', 7)	# 18-24
    sprite('Action_002_09', 6)	# 25-30
    sprite('Action_002_10', 6)	# 31-36

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1100)
        AttackP2(85)
        AirPushbackX(7500)
        AirPushbackY(15000)
        Unknown11050('0200000065665f6869746d6d5f7465737400000000000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5A3rd')
        callSubroutine('PassingLink')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitJumpCancel(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown2015(150)

        def upon_STATE_END():
            Unknown2015(-1)
    sprite('Action_097_00', 2)	# 1-2
    sprite('Action_097_01', 3)	# 3-5
    sprite('Action_097_02', 5)	# 6-10
    Unknown7009(3)
    sprite('Action_097_03', 1)	# 11-11
    GFX_0('5BB_Eff', -1)
    SFX_3('SE042')
    sprite('Action_097_04', 2)	# 12-13
    sprite('Action_097_05', 7)	# 14-20	 **attackbox here**
    sprite('Action_097_06', 7)	# 21-27
    Recovery()
    Unknown2063()
    sprite('Action_097_07', 5)	# 28-32
    sprite('Action_097_08', 4)	# 33-36

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1300)
        AttackP2(90)
        AirPushbackX(4000)
        AirPushbackY(20000)
        Unknown11050('0200000065665f6869746c6d5f7465737400000000000000000000000000000000000000')
        PushbackX(19800)
        HitOrBlockCancel('NmlAtk5A4th')
        callSubroutine('PassingLink')
        HitOrBlockCancel('CmnActCrushAttack')
        HitJumpCancel(1)
        Unknown9016(1)
    sprite('Action_003_00', 3)	# 1-3
    sprite('Action_003_01', 4)	# 4-7
    teleportRelativeX(60000)
    Unknown7009(1)
    Unknown2015(150)
    sprite('Action_003_02', 3)	# 8-10
    sprite('Action_003_03', 2)	# 11-12
    sprite('Action_003_04', 2)	# 13-14
    GFX_0('5C_Eff', -1)
    SFX_3('SE045')
    sprite('Action_003_05', 3)	# 15-17	 **attackbox here**
    teleportRelativeX(30000)
    sprite('Action_003_06', 6)	# 18-23
    Recovery()
    Unknown2063()
    sprite('Action_003_07', 5)	# 24-28
    sprite('Action_003_08', 4)	# 29-32
    sprite('Action_003_09', 4)	# 33-36
    teleportRelativeX(-40000)
    Unknown2015(-1)
    sprite('Action_003_10', 5)	# 37-41
    sprite('Action_223_00', 3)	# 42-44
    sprite('Action_224_00', 3)	# 45-47

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(0)
        AttackP2(100)
        Hitstop(3)
        JumpCancel_(0)
        Unknown2004(1, 0)
        Unknown11044(1)

        def upon_78():
            enterState('NmlAtk5A4thPlus')
    sprite('Action_125_01', 4)	# 1-4
    teleportRelativeX(20000)
    sprite('Action_125_02', 4)	# 5-8
    sprite('Action_125_03', 3)	# 9-11
    sprite('Action_125_04', 1)	# 12-12	 **attackbox here**
    physicsXImpulse(30000)
    sprite('Action_125_05', 1)	# 13-13	 **attackbox here**
    sprite('Action_125_06', 1)	# 14-14
    Unknown1084(1)
    Recovery()
    Unknown7007('7563613231325f300000000000000000640000007563613231325f310000000000000000640000007563613231325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_125_07', 3)	# 15-17
    sprite('Action_125_08', 8)	# 18-25
    sprite('Action_125_09', 4)	# 26-29
    sprite('Action_125_10', 4)	# 30-33
    sprite('Action_125_11', 4)	# 34-37
    sprite('Action_125_12', 4)	# 38-41
    sprite('Action_125_13', 4)	# 42-45

@State
def NmlAtk5A4thPlus():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk5A4thExe', 1, 0, 0)
        Unknown2018(0, 80)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackP2(100)
        Hitstop(0)
        setInvincible(1)
        Unknown11045(0)
        Unknown11025(0)
        Unknown11064(1)
        Unknown30061(1)
        JumpCancel_(0)
        Unknown2004(1, 0)
    sprite('Action_125_05', 1)	# 1-1	 **attackbox here**
    teleportRelativeX(-130000)
    sprite('Action_125_06', 1)	# 2-2
    Recovery()
    setInvincible(0)
    sprite('Action_125_07', 3)	# 3-5
    sprite('Action_125_08', 4)	# 6-9
    sprite('Action_125_09', 3)	# 10-12
    sprite('Action_125_10', 3)	# 13-15
    sprite('Action_125_11', 4)	# 16-19
    sprite('Action_125_12', 3)	# 20-22
    sprite('Action_125_13', 2)	# 23-24

@State
def NmlAtk5A4thExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(800)
        Unknown11092(1)
        Unknown11091(0)
        AirUntechableTime(30)
        PushbackX(0)
        Hitstop(0)
        Unknown30079(1)
        Unknown11064(1)
        Unknown9016(1)
        Unknown23027()
        JumpCancel_(0)
        Unknown2004(1, 0)
    sprite('Action_126_00', 7)	# 1-7
    tag_voice(1, 'uca210_0', 'uca210_1', 'uca210_2', '')
    teleportRelativeX(65000)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_01', 8)	# 8-15
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_02', 8)	# 16-23
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_03', 5)	# 24-28
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_04', 5)	# 29-33
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_05', 27)	# 34-60
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_06', 8)	# 61-68
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_07', 5)	# 69-73
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_08', 2)	# 74-75	 **attackbox here**
    GFX_0('UltimateCommandThrowEff', 0)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_09', 1)	# 76-76	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_09', 3)	# 77-79	 **attackbox here**
    RefreshMultihit()
    tag_voice(0, 'uca211_0', 'uca211_1', 'uca211_2', '')
    callSubroutine('LifeDrain')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_09', 4)	# 80-83	 **attackbox here**
    RefreshMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_10', 3)	# 84-86	 **attackbox here**
    RefreshMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_11', 6)	# 87-92
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_12', 5)	# 93-97
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_126_13', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    Unknown30079(0)
    Unknown11064(0)
    Damage(100)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackX(-30000)
    AirPushbackY(0)
    Unknown9202(3)
    Unknown11072(1, 110000, 50000)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_126_14', 5)	# 100-104
    sprite('Action_126_15', 7)	# 105-111
    sprite('Action_126_16', 4)	# 112-115
    sprite('Action_126_17', 5)	# 116-120
    sprite('Action_126_18', 5)	# 121-125
    sprite('Action_126_19', 4)	# 126-129

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        WhiffCancel('NmlAtk5B2nd')
        Unknown11050('0200000065665f6869746c6d5f7465737400000000000000000000000000000000000000')
        Unknown1112('')

        def upon_43():
            if (SLOT_48 == 1941):
                clearUponHandler(43)
                GFX_0('BloodPool_B', -1)
                Unknown1087(1, 4)
                Unknown36(1)
                teleportRelativeY(0)
                teleportRelativeX(100000)
                Unknown35()
                Unknown38(4, 1)
                WhiffCancelEnable(1)
                SLOT_51 = 10

                def upon_45():
                    if SLOT_51:
                        SLOT_51 = (SLOT_51 + (-1))
                    else:
                        Unknown14084('NmlAtk5B2nd')
    sprite('Action_190_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_190_01', 3)	# 4-6	 **attackbox here**
    SFX_4('uca105_1')
    sprite('Action_190_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_190_03', 2)	# 9-10	 **attackbox here**
    sprite('Action_190_04', 2)	# 11-12	 **attackbox here**
    SFX_3('SE042')
    sprite('Action_190_05', 4)	# 13-16
    Unknown23029(4, 9999, 0)
    GFX_0('6B_Eff', -1)
    Unknown38(4, 1)
    selfDamage(500)
    sprite('Action_190_06', 8)	# 17-24
    sprite('Action_190_07', 7)	# 25-31
    sprite('Action_190_08', 6)	# 32-37
    sprite('Action_190_09', 5)	# 38-42

@Subroutine
def DissolveActivate5B2nd():
    if Unknown46(4):
        if (not Unknown48('19000000020000000000000004000000020000003a000000')):
            GFX_0('6BB_Eff', -1)
            Unknown1087(1, 4)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(5):
        if (not Unknown48('19000000020000000000000005000000020000003a000000')):
            GFX_0('6BB_Eff', -1)
            Unknown1087(1, 5)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(6):
        if (not Unknown48('19000000020000000000000006000000020000003a000000')):
            GFX_0('6BB_Eff', -1)
            Unknown1087(1, 6)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(7):
        if (not Unknown48('19000000020000000000000007000000020000003a000000')):
            GFX_0('6BB_Eff', -1)
            Unknown1087(1, 7)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(8):
        if (not Unknown48('19000000020000000000000008000000020000003a000000')):
            GFX_0('6BB_Eff', -1)
            Unknown1087(1, 8)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()

@Subroutine
def DissolveAllDelete():
    if Unknown46(4):
        Unknown23029(4, 9999, 0)
    if Unknown46(5):
        Unknown23029(5, 9999, 0)
    if Unknown46(6):
        Unknown23029(6, 9999, 0)
    if Unknown46(7):
        Unknown23029(7, 9999, 0)
    if Unknown46(8):
        Unknown23029(8, 9999, 0)

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown11063(1)
        Unknown11050('0200000065665f6869746c6d5f7465737400000000000000000000000000000000000000')
        HitJumpCancel(1)
    sprite('Action_189_00', 4)	# 1-4
    sprite('Action_189_01', 5)	# 5-9
    SFX_4('uca102_1')
    sprite('Action_189_02', 3)	# 10-12
    callSubroutine('DissolveActivate5B2nd')
    callSubroutine('DissolveAllDelete')
    SFX_3('SE042')
    sprite('Action_189_03', 4)	# 13-16
    sprite('Action_189_04', 5)	# 17-21
    sprite('Action_189_05', 5)	# 22-26
    sprite('Action_189_06', 5)	# 27-31
    sprite('Action_189_07', 5)	# 32-36

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(800)
        AttackP2(80)
        HitLow(2)
        AttackP1(90)
        AirPushbackY(15000)
        callSubroutine('PassingLink')
        HitOrBlockCancel('CmnActCrushAttack')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_005_00', 1)	# 1-1
    sprite('Action_005_01', 2)	# 2-3
    sprite('Action_005_02', 2)	# 4-5
    Unknown7009(1)
    sprite('Action_005_03', 1)	# 6-6
    SFX_3('SE042')
    sprite('Action_005_04', 5)	# 7-11	 **attackbox here**
    sprite('Action_005_05', 4)	# 12-15
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_005_05', 4)	# 16-19
    sprite('Action_005_07', 5)	# 20-24

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(800)
        AttackP2(80)
        HitLow(2)
        AttackP1(90)
        AirPushbackY(15000)
        callSubroutine('PassingLink')
        HitOrBlockCancel('CmnActCrushAttack')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_005_00', 1)	# 1-1
    sprite('Action_005_01', 2)	# 2-3
    sprite('Action_005_02', 2)	# 4-5
    Unknown7009(1)
    sprite('Action_005_03', 1)	# 6-6
    SFX_3('SE042')
    sprite('Action_005_04', 5)	# 7-11	 **attackbox here**
    sprite('Action_005_05', 4)	# 12-15
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_005_05', 4)	# 16-19
    sprite('Action_005_07', 5)	# 20-24

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Damage(1100)
        AttackP1(90)
        AttackP2(85)
        AirPushbackY(25000)
        AirUntechableTime(25)
        Unknown11058('0000000001000000000000000000000000000000')
        HitJumpCancel(1)
        Unknown28(8, 'CmnActStand')
        callSubroutine('PassingLink')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_093_00', 4)	# 1-4
    sprite('Action_093_01', 2)	# 5-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown7007('7563613130365f300000000000000000640000007563613130365f310000000000000000640000007563613130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_093_02', 1)	# 7-7
    SFX_3('SE045')
    sprite('Action_093_03', 2)	# 8-9	 **attackbox here**
    sprite('Action_093_04', 3)	# 10-12
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('Action_093_05', 5)	# 13-17
    sprite('Action_093_06', 3)	# 18-20
    sprite('Action_093_07', 3)	# 21-23
    sprite('Action_093_08', 4)	# 24-27
    sprite('Action_093_09', 3)	# 28-30
    sprite('Action_222_00', 3)	# 31-33
    sprite('Action_223_00', 3)	# 34-36
    sprite('Action_224_00', 3)	# 37-39

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1300)
        AttackP1(90)
        AttackP2(80)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3500)
        AirPushbackY(18000)
        AirUntechableTime(30)
        Unknown9016(1)
        HitJumpCancel(1)
        callSubroutine('PassingLink')
        Unknown2004(1, 0)
    sprite('Action_006_00', 3)	# 1-3
    sprite('Action_006_01', 4)	# 4-7
    Unknown7007('7563613130375f300000000000000000640000007563613130375f310000000000000000640000007563613130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_006_02', 1)	# 8-8
    GFX_0('2C_Eff', -1)
    sprite('Action_006_03', 2)	# 9-10
    sprite('Action_006_04', 2)	# 11-12	 **attackbox here**
    SFX_3('SE043')
    sprite('Action_006_05', 6)	# 13-18
    Recovery()
    Unknown2063()
    sprite('Action_006_06', 9)	# 19-27
    sprite('Action_006_07', 5)	# 28-32
    sprite('Action_006_08', 5)	# 33-37
    sprite('Action_006_09', 4)	# 38-41

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP2(85)
        Unknown11092(1)
        AirPushbackY(22000)
        Unknown9016(1)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_14', 2)	# 1-2
    sprite('Action_009_15', 1)	# 3-3
    sprite('Action_009_15', 1)	# 4-4
    Unknown7009(5)
    sprite('Action_009_16', 2)	# 5-6
    sprite('Action_009_17', 2)	# 7-8
    sprite('Action_009_18', 2)	# 9-10	 **attackbox here**
    sprite('Action_009_19', 2)	# 11-12	 **attackbox here**
    GFX_0('JC_Eff', -1)
    SFX_3('SE043')
    sprite('Action_009_19', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_20', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('Action_009_21', 4)	# 18-21
    sprite('Action_009_22', 4)	# 22-25
    sprite('Action_009_25', 4)	# 26-29
    sprite('Action_009_26', 3)	# 30-32

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1100)
        AttackP2(85)
        AirUntechableTime(22)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_008_00', 1)	# 1-1
    sprite('Action_008_01', 1)	# 2-2
    sprite('Action_008_02', 1)	# 3-3
    sprite('Action_008_02', 1)	# 4-4
    Unknown7009(4)
    sprite('Action_008_03', 2)	# 5-6
    GFX_0('JB_Eff', -1)
    SFX_3('SE042')
    sprite('Action_008_04', 2)	# 7-8	 **attackbox here**
    sprite('Action_008_05', 1)	# 9-9	 **attackbox here**
    sprite('Action_008_06', 7)	# 10-16
    Recovery()
    Unknown2063()
    sprite('Action_008_07', 6)	# 17-22
    sprite('Action_008_08', 5)	# 23-27

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        WhiffCancel('NmlAtkAIR5B2nd')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 1911):
                clearUponHandler(43)
                GFX_0('BloodPool_B', -1)
                Unknown1087(1, 4)
                Unknown36(1)
                teleportRelativeY(0)
                teleportRelativeX(100000)
                Unknown35()
                Unknown38(4, 1)
                WhiffCancelEnable(1)
                SLOT_51 = 10

                def upon_45():
                    if SLOT_51:
                        SLOT_51 = (SLOT_51 + (-1))
                    else:
                        Unknown14084('NmlAtkAIR5B2nd')
                        Unknown2037(1)
    sprite('Action_191_00', 1)	# 1-1
    sprite('Action_191_00', 3)	# 2-4
    YAccel(50)
    sprite('Action_191_01', 3)	# 5-7
    SFX_4('uca105_1')
    Unknown1084(1)
    sprite('Action_191_02', 4)	# 8-11
    sprite('Action_191_03', 5)	# 12-16
    sprite('Action_191_04', 2)	# 17-18
    SFX_3('SE042')
    sprite('Action_191_05', 5)	# 19-23
    Unknown23029(4, 9999, 0)
    GFX_0('J6B_Eff', -1)
    Unknown38(4, 1)
    setGravity(3000)
    selfDamage(500)
    sprite('Action_191_06', 4)	# 24-27
    sprite('Action_191_07', 3)	# 28-30
    sprite('Action_191_08', 3)	# 31-33
    loopRest()
    Recovery()
    label(0)
    sprite('Action_191_09', 3)	# 34-36
    sprite('Action_191_10', 3)	# 37-39
    gotoLabel(0)
    label(1)
    sprite('Action_191_11', 2)	# 40-41
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown14084('NmlAtkAIR5B2nd')
    Unknown14085('NmlAtkAIR5C')
    WhiffCancel('NmlAtk5B2nd')

    def upon_3():
        if SLOT_2:
            clearUponHandler(3)
            Unknown14084('NmlAtk5B2nd')
    sprite('Action_191_12', 3)	# 42-44
    sprite('Action_191_13', 6)	# 45-50
    sprite('Action_191_14', 5)	# 51-55

@Subroutine
def DissolveActivateJB2nd():
    if Unknown46(4):
        if (not Unknown48('19000000020000000000000004000000020000003a000000')):
            GFX_0('J6BB_Eff', -1)
            Unknown1087(1, 4)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(5):
        if (not Unknown48('19000000020000000000000005000000020000003a000000')):
            GFX_0('J6BB_Eff', -1)
            Unknown1087(1, 5)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(6):
        if (not Unknown48('19000000020000000000000006000000020000003a000000')):
            GFX_0('J6BB_Eff', -1)
            Unknown1087(1, 6)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(7):
        if (not Unknown48('19000000020000000000000007000000020000003a000000')):
            GFX_0('J6BB_Eff', -1)
            Unknown1087(1, 7)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()
    if Unknown46(8):
        if (not Unknown48('19000000020000000000000008000000020000003a000000')):
            GFX_0('J6BB_Eff', -1)
            Unknown1087(1, 8)
            Unknown36(1)
            teleportRelativeX(90000)
            Unknown35()

@State
def NmlAtkAIR5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown11063(1)
        Unknown23026(-10000)

        def upon_STATE_END():
            Unknown23026(0)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_192_00', 4)	# 1-4
    sprite('Action_192_01', 5)	# 5-9
    physicsXImpulse(2000)
    physicsYImpulse(3000)
    SFX_4('uca102_0')
    sprite('Action_192_02', 2)	# 10-11
    physicsXImpulse(5000)
    physicsYImpulse(33000)
    setGravity(2300)
    callSubroutine('DissolveActivateJB2nd')
    callSubroutine('DissolveAllDelete')
    Unknown23026(0)
    SFX_3('SE042')
    sprite('Action_192_03', 10)	# 12-21
    sprite('Action_192_04', 7)	# 22-28
    sprite('Action_192_05', 4)	# 29-32
    sprite('Action_192_06', 4)	# 33-36
    sprite('Action_192_07', 3)	# 37-39
    label(0)
    sprite('Action_192_08', 3)	# 40-42
    sprite('Action_192_09', 3)	# 43-45
    gotoLabel(0)

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        AirPushbackX(3000)
        AirPushbackY(-70000)
        Hitstop(7)
        AirUntechableTime(22)
        HitOverhead(0)
        Unknown9016(1)
        JumpCancel_(0)
        Unknown9310(1)
        Unknown9202(1)
        Unknown23026(-10000)

        def upon_STATE_END():
            Unknown23026(0)
    sprite('Action_151_01', 3)	# 1-3
    sprite('Action_151_01', 6)	# 4-9

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    GFX_0('DoubleShotC', -1)
    Unknown1084(1)
    physicsYImpulse(30000)
    setGravity(2800)
    Unknown23026(0)
    sprite('Action_151_02', 4)	# 10-13
    Unknown7009(2)
    sprite('Action_151_03', 2)	# 14-15	 **attackbox here**
    SFX_3('SE043')
    sprite('Action_151_04', 1)	# 16-16
    sprite('Action_151_05', 1)	# 17-17
    Unknown1043()
    sprite('Action_151_05', 4)	# 18-21
    Unknown23029(7, 9999, 0)
    GFX_0('DoubleShotC_Ground', -1)
    Unknown38(7, 1)
    selfDamage(500)
    Unknown23029(8, 9999, 0)
    GFX_0('DoubleShotC_Eff', -1)
    Unknown38(8, 1)
    selfDamage(500)
    sprite('Action_151_06', 5)	# 22-26
    sprite('Action_151_07', 4)	# 27-30
    sprite('Action_151_08', 4)	# 31-34
    label(0)
    sprite('Action_151_09', 4)	# 35-38
    sprite('Action_151_10', 4)	# 39-42
    gotoLabel(0)
    label(1)
    sprite('Action_151_11', 3)	# 43-45
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_151_12', 5)	# 46-50
    sprite('Action_151_13', 4)	# 51-54
    sprite('Action_151_14', 4)	# 55-58

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)
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
    tag_voice(1, 'uca156_0', 'uca156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 3)	# 14-16
    sprite('Action_009_14', 3)	# 17-19
    sprite('Action_009_15', 2)	# 20-21
    sprite('Action_009_16', 1)	# 22-22
    sprite('Action_009_17', 1)	# 23-23
    sprite('Action_009_18', 2)	# 24-25	 **attackbox here**
    GFX_0('JC_Eff', -1)
    SFX_3('SE043')
    sprite('Action_009_19', 3)	# 26-28	 **attackbox here**
    sprite('Action_009_20', 6)	# 29-34
    sprite('Action_068_08', 3)	# 35-37
    sprite('Action_068_09', 3)	# 38-40
    label(0)
    sprite('Action_068_10', 1)	# 41-41
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 2)	# 42-43
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_021_01', 5)	# 44-48
    sprite('Action_021_02', 3)	# 49-51
    Unknown18009(0)
    sprite('Action_021_03', 3)	# 52-54

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        Unknown23027()
        setGravity(4000)
        sendToLabelUpon(2, 2)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 1)	# 1-1
    sprite('Action_009_20', 32767)	# 2-32768
    label(2)
    sprite('Action_021_00', 2)	# 32769-32770
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_021_01', 4)	# 32771-32774
    sprite('Action_021_02', 2)	# 32775-32776
    sprite('Action_021_03', 2)	# 32777-32778
    sprite('Action_200_00', 2)	# 32779-32780
    sprite('Action_200_01', 3)	# 32781-32783
    sprite('Action_200_02', 3)	# 32784-32786
    sprite('Action_200_03', 2)	# 32787-32788
    sprite('Action_200_04', 2)	# 32789-32790	 **attackbox here**
    RefreshMultihit()
    GFX_0('InvincibleAttack_Eff', -1)
    SFX_3('SE045')
    sprite('Action_200_05', 4)	# 32791-32794	 **attackbox here**
    StartMultihit()
    tag_voice(0, 'uca157_0', 'uca157_1', '', '')
    sprite('Action_200_06', 20)	# 32795-32814
    sprite('Action_200_07', 6)	# 32815-32820
    sprite('Action_200_08', 6)	# 32821-32826
    sprite('Action_000_16', 6)	# 32827-32832
    sprite('Action_000_17', 7)	# 32833-32839
    sprite('Action_000_18', 4)	# 32840-32843
    sprite('Action_000_19', 5)	# 32844-32848
    sprite('Action_000_20', 9)	# 32849-32857
    sprite('Action_000_21', 7)	# 32858-32864
    sprite('Action_000_22', 4)	# 32865-32868
    sprite('Action_000_23', 5)	# 32869-32873
    sprite('Action_000_24', 6)	# 32874-32879
    sprite('Action_000_25', 7)	# 32880-32886
    sprite('Action_000_26', 5)	# 32887-32891
    sprite('Action_000_27', 4)	# 32892-32895
    sprite('Action_000_28', 4)	# 32896-32899
    label(0)
    sprite('Action_000_00', 7)	# 32900-32906	 **attackbox here**
    sprite('Action_000_01', 7)	# 32907-32913	 **attackbox here**
    sprite('Action_000_02', 8)	# 32914-32921	 **attackbox here**
    sprite('Action_000_03', 8)	# 32922-32929	 **attackbox here**
    sprite('Action_000_04', 10)	# 32930-32939	 **attackbox here**
    sprite('Action_000_05', 9)	# 32940-32948	 **attackbox here**
    sprite('Action_000_06', 11)	# 32949-32959	 **attackbox here**
    sprite('Action_000_07', 8)	# 32960-32967	 **attackbox here**
    sprite('Action_000_08', 7)	# 32968-32974	 **attackbox here**
    sprite('Action_000_09', 6)	# 32975-32980	 **attackbox here**
    sprite('Action_000_10', 7)	# 32981-32987	 **attackbox here**
    sprite('Action_000_11', 7)	# 32988-32994	 **attackbox here**
    sprite('Action_000_12', 8)	# 32995-33002	 **attackbox here**
    sprite('Action_000_13', 7)	# 33003-33009	 **attackbox here**
    sprite('Action_000_14', 7)	# 33010-33016	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 33017-33017

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        Unknown23027()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_012_00', 1)	# 1-1
    sprite('Action_012_01', 1)	# 2-2
    sprite('Action_095_00', 2)	# 3-4
    sprite('Action_095_01', 3)	# 5-7
    sprite('Action_095_02', 2)	# 8-9
    sprite('Action_095_03', 2)	# 10-11
    sprite('Action_095_04', 2)	# 12-13
    sprite('Action_095_05', 1)	# 14-14
    GFX_0('3C_Eff', -1)
    SFX_3('SE045')
    sprite('Action_095_06', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_095_07', 3)	# 17-19	 **attackbox here**
    sprite('Action_095_08', 8)	# 20-27
    sprite('Action_095_09', 5)	# 28-32
    sprite('Action_095_10', 4)	# 33-36
    sprite('Action_095_11', 3)	# 37-39
    sprite('Action_000_16', 6)	# 40-45
    sprite('Action_000_17', 7)	# 46-52
    sprite('Action_000_18', 4)	# 53-56
    sprite('Action_000_19', 5)	# 57-61
    sprite('Action_000_20', 9)	# 62-70
    sprite('Action_000_21', 7)	# 71-77
    sprite('Action_000_22', 4)	# 78-81
    sprite('Action_000_23', 5)	# 82-86
    sprite('Action_000_24', 6)	# 87-92
    sprite('Action_000_25', 7)	# 93-99
    sprite('Action_000_26', 5)	# 100-104
    sprite('Action_000_27', 4)	# 105-108
    sprite('Action_000_28', 4)	# 109-112
    label(0)
    sprite('Action_000_00', 7)	# 113-119	 **attackbox here**
    sprite('Action_000_01', 7)	# 120-126	 **attackbox here**
    sprite('Action_000_02', 8)	# 127-134	 **attackbox here**
    sprite('Action_000_03', 8)	# 135-142	 **attackbox here**
    sprite('Action_000_04', 10)	# 143-152	 **attackbox here**
    sprite('Action_000_05', 9)	# 153-161	 **attackbox here**
    sprite('Action_000_06', 11)	# 162-172	 **attackbox here**
    sprite('Action_000_07', 8)	# 173-180	 **attackbox here**
    sprite('Action_000_08', 7)	# 181-187	 **attackbox here**
    sprite('Action_000_09', 6)	# 188-193	 **attackbox here**
    sprite('Action_000_10', 7)	# 194-200	 **attackbox here**
    sprite('Action_000_11', 7)	# 201-207	 **attackbox here**
    sprite('Action_000_12', 8)	# 208-215	 **attackbox here**
    sprite('Action_000_13', 7)	# 216-222	 **attackbox here**
    sprite('Action_000_14', 7)	# 223-229	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 230-230

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('Action_094_18', 3)	# 1-3
    teleportRelativeX(-30000)
    sprite('Action_094_19', 11)	# 4-14
    teleportRelativeX(-30000)
    sprite('Action_094_20', 1)	# 15-15
    teleportRelativeX(-30000)
    sprite('Action_094_21', 1)	# 16-16
    teleportRelativeX(-30000)
    sprite('Action_094_22', 1)	# 17-17
    GFX_0('5AAA_Eff', -1)
    SFX_3('SE043')
    sprite('Action_094_23', 1)	# 18-18
    sprite('Action_094_24', 1)	# 19-19
    tag_voice(0, 'uca158_0', 'uca158_1', '', '')
    sprite('Action_094_25', 3)	# 20-22	 **attackbox here**
    sprite('Action_094_26', 6)	# 23-28
    teleportRelativeX(20000)
    sprite('Action_094_27', 5)	# 29-33
    teleportRelativeX(20000)
    sprite('Action_094_28', 5)	# 34-38
    teleportRelativeX(20000)
    sprite('Action_094_29', 4)	# 39-42
    teleportRelativeX(40000)
    sprite('Action_094_30', 3)	# 43-45
    teleportRelativeX(20000)
    sprite('Action_222_00', 4)	# 46-49
    sprite('Action_223_00', 4)	# 50-53
    sprite('Action_224_00', 4)	# 54-57
    sprite('Action_000_00', 3)	# 58-60	 **attackbox here**

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 15)	# 1-15
    sprite('null', 10)	# 16-25
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 26-26
    teleportRelativeX(-1000000)
    Unknown1007(500000)
    setGravity(0)
    sprite('null', 3)	# 27-29
    sprite('Action_008_00', 3)	# 30-32
    physicsXImpulse(48000)
    physicsYImpulse(-18000)
    setGravity(3000)
    sprite('Action_009_14', 3)	# 33-35
    sprite('Action_009_15', 2)	# 36-37
    sprite('Action_009_16', 1)	# 38-38
    sprite('Action_009_17', 1)	# 39-39
    sprite('Action_009_18', 2)	# 40-41	 **attackbox here**
    GFX_0('JC_Eff', -1)
    SFX_3('SE043')
    sprite('Action_009_19', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    sprite('Action_009_20', 4)	# 44-47
    sprite('Action_009_21', 5)	# 48-52
    sprite('Action_009_22', 5)	# 53-57
    sprite('Action_009_23', 5)	# 58-62
    sprite('Action_009_24', 5)	# 63-67
    sprite('Action_009_25', 5)	# 68-72
    sprite('Action_009_26', 32767)	# 73-32839
    loopRest()
    label(1)
    sprite('Action_021_00', 2)	# 32840-32841
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_021_01', 4)	# 32842-32845
    sprite('Action_021_02', 2)	# 32846-32847
    sprite('Action_021_03', 2)	# 32848-32849
    sprite('Action_222_00', 3)	# 32850-32852
    sprite('Action_223_00', 3)	# 32853-32855
    sprite('Action_224_00', 3)	# 32856-32858
    sprite('Action_000_00', 7)	# 32859-32865	 **attackbox here**
    sprite('Action_000_01', 7)	# 32866-32872	 **attackbox here**
    sprite('Action_000_02', 8)	# 32873-32880	 **attackbox here**
    sprite('Action_000_03', 8)	# 32881-32888	 **attackbox here**
    sprite('Action_000_04', 10)	# 32889-32898	 **attackbox here**
    sprite('Action_000_05', 9)	# 32899-32907	 **attackbox here**
    sprite('Action_000_06', 11)	# 32908-32918	 **attackbox here**
    sprite('Action_000_07', 8)	# 32919-32926	 **attackbox here**
    sprite('Action_000_08', 7)	# 32927-32933	 **attackbox here**
    sprite('Action_000_09', 6)	# 32934-32939	 **attackbox here**
    sprite('Action_000_10', 7)	# 32940-32946	 **attackbox here**
    sprite('Action_000_11', 7)	# 32947-32953	 **attackbox here**
    sprite('Action_000_12', 8)	# 32954-32961	 **attackbox here**
    sprite('Action_000_13', 7)	# 32962-32968	 **attackbox here**
    sprite('Action_000_14', 7)	# 32969-32975	 **attackbox here**

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 2)	# 3-4
    Unknown2015(150)
    sprite('Action_003_02', 3)	# 5-7
    Unknown2015(200)
    sprite('Action_003_03', 2)	# 8-9
    sprite('Action_003_04', 2)	# 10-11
    GFX_0('5C_Eff', -1)
    SFX_3('SE045')
    sprite('Action_003_05', 3)	# 12-14	 **attackbox here**
    Unknown2015(100)
    sprite('Action_003_06', 6)	# 15-20
    Recovery()
    Unknown2063()
    sprite('Action_003_07', 5)	# 21-25
    sprite('Action_003_08', 4)	# 26-29
    sprite('Action_003_09', 4)	# 30-33
    sprite('Action_003_10', 5)	# 34-38
    sprite('Action_000_16', 6)	# 39-44
    sprite('Action_000_17', 7)	# 45-51
    sprite('Action_000_18', 4)	# 52-55
    sprite('Action_000_19', 5)	# 56-60
    sprite('Action_000_20', 9)	# 61-69
    sprite('Action_000_21', 7)	# 70-76
    sprite('Action_000_22', 4)	# 77-80
    sprite('Action_000_23', 5)	# 81-85
    sprite('Action_000_24', 6)	# 86-91
    sprite('Action_000_25', 7)	# 92-98
    sprite('Action_000_26', 5)	# 99-103
    sprite('Action_000_27', 4)	# 104-107
    sprite('Action_000_28', 4)	# 108-111
    sprite('Action_000_00', 7)	# 112-118	 **attackbox here**
    sprite('Action_000_01', 7)	# 119-125	 **attackbox here**
    sprite('Action_000_02', 8)	# 126-133	 **attackbox here**
    sprite('Action_000_03', 8)	# 134-141	 **attackbox here**
    sprite('Action_000_04', 10)	# 142-151	 **attackbox here**
    sprite('Action_000_05', 9)	# 152-160	 **attackbox here**
    sprite('Action_000_06', 11)	# 161-171	 **attackbox here**
    sprite('Action_000_07', 8)	# 172-179	 **attackbox here**
    sprite('Action_000_08', 7)	# 180-186	 **attackbox here**
    sprite('Action_000_09', 6)	# 187-192	 **attackbox here**
    sprite('Action_000_10', 7)	# 193-199	 **attackbox here**
    sprite('Action_000_11', 7)	# 200-206	 **attackbox here**
    sprite('Action_000_12', 8)	# 207-214	 **attackbox here**
    sprite('Action_000_13', 7)	# 215-221	 **attackbox here**
    sprite('Action_000_14', 7)	# 222-228	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
    sprite('Action_094_18', 3)	# 1-3
    teleportRelativeX(-30000)
    sprite('Action_094_19', 11)	# 4-14
    teleportRelativeX(-30000)
    sprite('Action_094_20', 1)	# 15-15
    teleportRelativeX(-30000)
    sprite('Action_094_21', 1)	# 16-16
    teleportRelativeX(-30000)
    sprite('Action_094_22', 1)	# 17-17
    GFX_0('5AAA_Eff', -1)
    SFX_3('SE043')
    sprite('Action_094_23', 1)	# 18-18
    sprite('Action_094_24', 1)	# 19-19
    sprite('Action_094_25', 3)	# 20-22	 **attackbox here**
    sprite('Action_094_26', 6)	# 23-28
    teleportRelativeX(20000)
    sprite('Action_094_27', 5)	# 29-33
    teleportRelativeX(20000)
    sprite('Action_094_28', 5)	# 34-38
    teleportRelativeX(20000)
    sprite('Action_094_29', 4)	# 39-42
    teleportRelativeX(40000)
    sprite('Action_094_30', 3)	# 43-45
    teleportRelativeX(20000)
    sprite('Action_222_00', 4)	# 46-49
    sprite('Action_223_00', 4)	# 50-53
    sprite('Action_224_00', 4)	# 54-57
    sprite('Action_000_00', 3)	# 58-60	 **attackbox here**

@Subroutine
def MyCreateHitEffect():
    Unknown4052()
    Unknown4049(1200)
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000000000000')
    SFX_0('101_hit_slash_3')

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
    sprite('Action_010_00', 2)	# 1-2
    sprite('Action_010_01', 2)	# 3-4
    sprite('Action_045_00', 2)	# 5-6
    sprite('Action_045_01', 2)	# 7-8
    label(0)
    sprite('Action_045_02', 3)	# 9-11
    sprite('Action_045_03', 3)	# 12-14
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    sprite('Action_045_06', 3)	# 21-23
    sprite('Action_045_07', 3)	# 24-26
    Unknown8006(100, 1, 1)
    sprite('Action_045_08', 3)	# 27-29
    sprite('Action_045_09', 3)	# 30-32
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 33-33
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 1)	# 34-34
    sprite('Action_055_02', 1)	# 35-35
    sprite('Action_055_03', 3)	# 36-38	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_04', 4)	# 39-42
    SFX_4('uca154')
    sprite('Action_055_05', 5)	# 43-47
    sprite('Action_055_06', 6)	# 48-53
    sprite('Action_055_07', 4)	# 54-57
    sprite('Action_055_08', 4)	# 58-61

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(10)
        Unknown9142(999)
        Unknown11072(1, 250000, 0)
        PushbackX(0)
        Unknown9016(1)
        JumpCancel_(0)
    sprite('Action_056_01ex00', 2)	# 1-2
    Unknown5003(1)
    Unknown5000(8, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_056_01', 2)	# 3-4
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_056_02', 4)	# 5-8
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_056_03', 4)	# 9-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_056_04', 2)	# 13-14
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_00', 2)	# 15-16
    GFX_0('ThrowExe_Eff', 0)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_01', 3)	# 17-19
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    callSubroutine('LifeDrain')
    SFX_4('uca153')
    sprite('Action_057_02', 3)	# 20-22
    callSubroutine('MyCreateHitEffect')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 7)	# 23-29	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
    sprite('Action_057_04', 6)	# 30-35
    sprite('Action_057_05', 2)	# 36-37
    sprite('Action_057_06', 6)	# 38-43
    sprite('Action_057_07', 7)	# 44-50

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
    sprite('Action_010_00', 2)	# 1-2
    sprite('Action_010_01', 2)	# 3-4
    sprite('Action_045_00', 2)	# 5-6
    sprite('Action_045_01', 2)	# 7-8
    label(0)
    sprite('Action_045_02', 3)	# 9-11
    sprite('Action_045_03', 3)	# 12-14
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    sprite('Action_045_06', 3)	# 21-23
    sprite('Action_045_07', 3)	# 24-26
    Unknown8006(100, 1, 1)
    sprite('Action_045_08', 3)	# 27-29
    sprite('Action_045_09', 3)	# 30-32
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 33-33
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 1)	# 34-34
    sprite('Action_055_02', 1)	# 35-35
    sprite('Action_055_03', 3)	# 36-38	 **attackbox here**
    Unknown1084(1)
    SFX_0('010_swing_sword_0')
    sprite('Action_055_04', 4)	# 39-42
    SFX_4('uca154')
    sprite('Action_055_05', 5)	# 43-47
    sprite('Action_055_06', 6)	# 48-53
    sprite('Action_055_07', 4)	# 54-57
    sprite('Action_055_08', 4)	# 58-61

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(10)
        Unknown9142(999)
        Unknown11072(1, 250000, 0)
        PushbackX(0)
        Unknown9016(1)
        JumpCancel_(0)
    sprite('Action_056_01ex00', 2)	# 1-2
    Unknown5003(1)
    Unknown5000(8, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_056_01', 2)	# 3-4
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000001000000')
    sprite('Action_056_02', 4)	# 5-8
    Unknown2005()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_056_03', 4)	# 9-12
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_056_04', 2)	# 13-14
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_00', 2)	# 15-16
    GFX_0('ThrowExe_Eff', 0)
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_01', 3)	# 17-19
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    callSubroutine('LifeDrain')
    SFX_4('uca153')
    sprite('Action_057_02', 3)	# 20-22
    callSubroutine('MyCreateHitEffect')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_03', 7)	# 23-29	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')

    def upon_ON_HIT_OR_BLOCK():
        JumpCancel_(1)
    sprite('Action_057_04', 6)	# 30-35
    sprite('Action_057_05', 2)	# 36-37
    sprite('Action_057_06', 6)	# 38-43
    sprite('Action_057_07', 7)	# 44-50

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(3)
        Damage(500)
        Unknown11092(1)
        AirUntechableTime(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(15000)
        AirPushbackY(35000)
        Unknown23086(1)
        Hitstop(1)
        Unknown11001(0, 1, 3)
        Unknown9016(1)
        Unknown11057(600)

        def upon_11():
            Unknown2037(1)

        def upon_3():
            if SLOT_2:
                pass
    sprite('Action_200_00', 2)	# 1-2
    sprite('Action_200_01', 3)	# 3-5
    sprite('Action_200_02', 4)	# 6-9
    Unknown7007('7563613230355f300000000000000000640000007563613230355f310000000000000000640000007563613230355f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_200_03', 2)	# 10-11
    sprite('Action_200_04', 1)	# 12-12	 **attackbox here**
    GFX_0('InvincibleAttackEX_Eff', -1)
    SFX_3('SE045')
    sprite('Action_200_05', 1)	# 13-13	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 14-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 15-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 19-19	 **attackbox here**
    RefreshMultihit()
    Hitstop(5)
    sprite('Action_200_05', 1)	# 20-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 21-21	 **attackbox here**
    RefreshMultihit()
    sprite('Action_200_05', 1)	# 22-22	 **attackbox here**
    RefreshMultihit()
    Hitstop(8)
    sprite('Action_200_06', 22)	# 23-44
    setInvincible(0)
    sprite('Action_200_07', 11)	# 45-55
    sprite('Action_200_08', 10)	# 56-65

@Subroutine
def DissolveActivateRS():
    if Unknown46(4):
        Unknown23029(4, 9991, 0)
    if Unknown46(5):
        Unknown23029(5, 9991, 0)
    if Unknown46(6):
        Unknown23029(6, 9991, 0)
    if Unknown46(7):
        Unknown23029(7, 9991, 0)
    if Unknown46(8):
        Unknown23029(8, 9991, 0)

@State
def RotationShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_130_00', 3)	# 1-3
    sprite('Action_130_01', 6)	# 4-9
    Unknown7007('7563613230305f300000000000000000640000007563613230305f310000000000000000640000007563613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_130_02', 1)	# 10-10
    callSubroutine('DissolveActivateRS')
    GFX_0('RotationShot_Eff', -1)
    Unknown23029(1, 1301, 0)
    Unknown38(5, 1)
    selfDamage(500)
    SFX_3('SE045')
    sprite('Action_130_03', 5)	# 11-15
    sprite('Action_130_04', 8)	# 16-23
    sprite('Action_130_05', 10)	# 24-33
    sprite('Action_130_06', 9)	# 34-42
    sprite('Action_130_07', 6)	# 43-48

@State
def RotationShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_131_00', 3)	# 1-3
    sprite('Action_131_01', 6)	# 4-9
    Unknown7007('7563613230305f300000000000000000640000007563613230305f310000000000000000640000007563613230305f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_131_02', 1)	# 10-10
    callSubroutine('DissolveActivateRS')
    GFX_0('RotationShot_Eff', -1)
    Unknown23029(1, 1302, 0)
    Unknown38(5, 1)
    selfDamage(500)
    SFX_3('SE045')
    sprite('Action_131_03', 5)	# 11-15
    sprite('Action_131_04', 8)	# 16-23
    sprite('Action_131_05', 10)	# 24-33
    sprite('Action_131_06', 9)	# 34-42
    sprite('Action_131_07', 6)	# 43-48

@State
def RotationShotEX():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_132_00', 3)	# 1-3
    sprite('Action_132_01', 6)	# 4-9
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('7563613230325f300000000000000000640000007563613230325f310000000000000000640000007563613230325f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_132_02', 1)	# 10-10
    callSubroutine('DissolveActivateRS')
    GFX_0('RotationShotEx_Eff', -1)
    Unknown23029(1, 1303, 0)
    Unknown38(5, 1)
    selfDamage(500)
    SFX_3('SE045')
    sprite('Action_132_03', 3)	# 11-13
    sprite('Action_132_04', 6)	# 14-19
    sprite('Action_132_05', 8)	# 20-27
    sprite('Action_132_06', 7)	# 28-34
    sprite('Action_132_07', 4)	# 35-38

@State
def AirRotationShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown23026(-10000)

        def upon_STATE_END():
            Unknown23026(0)
    sprite('Action_170_00', 2)	# 1-2
    sprite('Action_170_00', 3)	# 3-5
    Unknown1084(1)
    sprite('Action_170_01', 5)	# 6-10
    Unknown7007('7563613230315f300000000000000000640000007563613230315f310000000000000000640000007563613230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_170_02', 2)	# 11-12
    SFX_3('SE045')
    sprite('Action_170_03', 7)	# 13-19
    callSubroutine('DissolveActivateRS')
    GFX_0('RotationShot_Eff', -1)
    Unknown23029(1, 1304, 0)
    Unknown38(5, 1)
    physicsXImpulse(-7500)
    physicsYImpulse(15000)
    Unknown1043()
    selfDamage(500)
    Unknown23026(0)
    sprite('Action_170_04', 7)	# 20-26
    sprite('Action_170_05', 6)	# 27-32
    sprite('Action_170_06', 5)	# 33-37
    sprite('Action_170_07', 3)	# 38-40
    ExitState()
    label(1)
    sprite('Action_170_09', 2)	# 41-42
    Unknown1084(1)
    sprite('Action_170_10', 3)	# 43-45
    sprite('Action_170_11', 5)	# 46-50
    sprite('Action_170_12', 5)	# 51-55

@State
def AirRotationShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown23026(-10000)

        def upon_STATE_END():
            Unknown23026(0)
    sprite('Action_171_00', 2)	# 1-2
    sprite('Action_171_00', 3)	# 3-5
    Unknown1084(1)
    sprite('Action_171_01', 5)	# 6-10
    Unknown7007('7563613230315f300000000000000000640000007563613230315f310000000000000000640000007563613230315f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_171_02', 2)	# 11-12
    SFX_3('SE045')
    sprite('Action_171_03', 7)	# 13-19
    callSubroutine('DissolveActivateRS')
    GFX_0('RotationShot_Eff', -1)
    Unknown23029(1, 1305, 0)
    Unknown38(5, 1)
    physicsXImpulse(-7500)
    physicsYImpulse(15000)
    Unknown1043()
    selfDamage(500)
    Unknown23026(0)
    sprite('Action_171_04', 7)	# 20-26
    sprite('Action_171_05', 6)	# 27-32
    sprite('Action_171_06', 5)	# 33-37
    sprite('Action_171_07', 3)	# 38-40
    ExitState()
    label(1)
    sprite('Action_171_09', 2)	# 41-42
    Unknown1084(1)
    sprite('Action_171_10', 3)	# 43-45
    sprite('Action_171_11', 5)	# 46-50
    sprite('Action_171_12', 5)	# 51-55

@State
def AirRotationShotEX():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown23026(-10000)

        def upon_STATE_END():
            Unknown23026(0)
    sprite('Action_172_00', 3)	# 1-3
    sprite('Action_172_00', 2)	# 4-5
    Unknown1084(1)
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7007('7563613230335f300000000000000000640000007563613230335f310000000000000000640000007563613230335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_172_01', 5)	# 6-10
    sprite('Action_172_02', 2)	# 11-12
    SFX_3('SE045')
    sprite('Action_172_03', 7)	# 13-19
    callSubroutine('DissolveActivateRS')
    GFX_0('RotationShotEx_Eff', -1)
    Unknown23029(1, 1306, 0)
    Unknown38(5, 1)
    physicsXImpulse(-7500)
    physicsYImpulse(15000)
    Unknown1043()
    selfDamage(500)
    Unknown23026(0)
    sprite('Action_172_04', 7)	# 20-26
    sprite('Action_172_05', 6)	# 27-32
    sprite('Action_172_06', 5)	# 33-37

@Subroutine
def DissolveActivatePU():
    if Unknown46(4):
        Unknown23029(4, 9992, 0)
    if Unknown46(5):
        Unknown23029(5, 9992, 0)
    if Unknown46(6):
        Unknown23029(6, 9992, 0)
    if Unknown46(7):
        Unknown23029(7, 9992, 0)
    if Unknown46(8):
        Unknown23029(8, 9992, 0)

@State
def PushUpShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_179_00', 5)	# 1-5
    sprite('Action_179_01', 5)	# 6-10
    Unknown7007('7563613230385f300000000000000000640000007563613230385f310000000000000000640000007563613230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_179_02', 1)	# 11-11
    sprite('Action_179_02', 2)	# 12-13
    callSubroutine('DissolveActivatePU')
    GFX_0('PushUpShot_Eff', -1)
    Unknown23029(1, 1791, 0)
    Unknown38(6, 1)
    selfDamage(500)
    sprite('Action_179_03', 8)	# 14-21
    sprite('Action_179_04', 7)	# 22-28
    sprite('Action_179_05', 6)	# 29-34
    sprite('Action_179_06', 6)	# 35-40
    sprite('Action_179_07', 6)	# 41-46

@State
def PushUpShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_180_00', 5)	# 1-5
    sprite('Action_180_01', 5)	# 6-10
    Unknown7007('7563613230385f300000000000000000640000007563613230385f310000000000000000640000007563613230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_180_02', 1)	# 11-11
    sprite('Action_180_02', 2)	# 12-13
    callSubroutine('DissolveActivatePU')
    GFX_0('PushUpShot_Eff', -1)
    Unknown23029(1, 1792, 0)
    Unknown38(6, 1)
    selfDamage(500)
    sprite('Action_180_03', 8)	# 14-21
    sprite('Action_180_04', 7)	# 22-28
    sprite('Action_180_05', 6)	# 29-34
    sprite('Action_180_06', 6)	# 35-40
    sprite('Action_180_07', 6)	# 41-46

@State
def PushUpShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_180_00', 5)	# 1-5
    sprite('Action_180_01', 5)	# 6-10
    Unknown7007('7563613230385f300000000000000000640000007563613230385f310000000000000000640000007563613230385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('Action_180_02', 1)	# 11-11
    sprite('Action_180_02', 2)	# 12-13
    callSubroutine('DissolveActivatePU')
    GFX_0('PushUpShot_Eff', -1)
    Unknown23029(1, 1793, 0)
    Unknown38(6, 1)
    selfDamage(500)
    sprite('Action_180_03', 8)	# 14-21
    sprite('Action_180_04', 7)	# 22-28
    sprite('Action_180_05', 6)	# 29-34
    sprite('Action_180_06', 6)	# 35-40
    sprite('Action_180_07', 6)	# 41-46

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 2501):
                Unknown13024(0)
                Unknown2037(1)
            if (SLOT_48 == 2503):
                Unknown13024(1)
        Unknown2021(1)

        def upon_STATE_END():
            Unknown23029(11, 2502, 0)
    sprite('Action_250_00', 3)	# 1-3
    sprite('Action_250_00', 12)	# 4-15
    Unknown2036(59, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uca250_0', 'uca250_1', '', '')
    sprite('Action_250_00', 5)	# 16-20
    sprite('Action_250_01', 7)	# 21-27
    sprite('Action_250_02', 7)	# 28-34
    sprite('Action_250_03', 7)	# 35-41
    sprite('Action_250_04', 7)	# 42-48
    sprite('Action_250_05', 3)	# 49-51	 **attackbox here**
    SFX_3('SE012')
    sprite('Action_250_06', 3)	# 52-54	 **attackbox here**
    sprite('Action_250_07', 3)	# 55-57	 **attackbox here**
    sprite('Action_250_08', 2)	# 58-59	 **attackbox here**
    sprite('Action_250_08', 1)	# 60-60	 **attackbox here**
    GFX_0('UltimateShotEffMaster', -1)
    sprite('Action_250_09', 2)	# 61-62
    SFX_3('SE045')
    sprite('Action_250_10', 3)	# 63-65
    sprite('Action_250_11', 3)	# 66-68
    GFX_0('UltimateShotFootEff', -1)
    Unknown38(11, 1)
    sprite('Action_250_12', 2)	# 69-70
    sprite('Action_250_13', 3)	# 71-73
    sprite('Action_250_14', 3)	# 74-76
    sprite('Action_250_15', 3)	# 77-79
    sprite('Action_250_16', 3)	# 80-82
    sprite('Action_250_17', 3)	# 83-85
    sprite('Action_250_18', 2)	# 86-87	 **attackbox here**
    StartMultihit()
    sprite('Action_250_18', 1)	# 88-88	 **attackbox here**
    StartMultihit()
    if SLOT_2:
        sendToLabel(1)
    sprite('Action_250_20', 3)	# 89-91
    setInvincible(0)
    sprite('Action_250_21', 3)	# 92-94
    sprite('Action_250_22', 3)	# 95-97
    sprite('Action_250_20', 3)	# 98-100
    sprite('Action_250_21', 3)	# 101-103
    sprite('Action_250_22', 3)	# 104-106
    sprite('Action_250_20', 3)	# 107-109
    sprite('Action_250_21', 3)	# 110-112
    sprite('Action_250_22', 3)	# 113-115
    sprite('Action_250_20', 3)	# 116-118
    sprite('Action_250_21', 3)	# 119-121
    sprite('Action_250_22', 3)	# 122-124
    sprite('Action_250_20', 3)	# 125-127
    sprite('Action_250_21', 3)	# 128-130
    sprite('Action_250_22', 3)	# 131-133
    sprite('Action_250_20', 3)	# 134-136
    sprite('Action_250_21', 3)	# 137-139
    sprite('Action_250_22', 3)	# 140-142
    sprite('Action_250_23', 3)	# 143-145
    sprite('Action_250_24', 5)	# 146-150
    Unknown23029(11, 2502, 0)
    sprite('Action_250_25', 5)	# 151-155
    ExitState()
    label(1)
    sprite('Action_250_27', 3)	# 156-158
    sprite('Action_250_28', 3)	# 159-161
    sprite('Action_250_29', 3)	# 162-164
    sprite('Action_250_27', 3)	# 165-167
    GFX_0('UltimateShotAtkExe', -1)
    tag_voice(0, 'uca251_0', 'uca251_1', '', '')
    sprite('Action_250_28', 3)	# 168-170
    sprite('Action_250_29', 3)	# 171-173
    sprite('Action_250_30', 3)	# 174-176
    sprite('Action_250_31', 3)	# 177-179
    sprite('Action_250_32', 3)	# 180-182
    sprite('Action_250_33', 3)	# 183-185
    sprite('Action_250_34', 3)	# 186-188
    sprite('Action_250_35', 3)	# 189-191
    sprite('Action_250_36', 3)	# 192-194
    sprite('Action_250_37', 3)	# 195-197
    sprite('Action_250_38', 3)	# 198-200
    sprite('Action_250_39', 3)	# 201-203
    sprite('Action_250_40', 3)	# 204-206
    sprite('Action_250_41', 3)	# 207-209
    sprite('Action_250_42', 3)	# 210-212
    sprite('Action_250_43', 3)	# 213-215
    sprite('Action_250_44', 3)	# 216-218
    sprite('Action_250_45', 3)	# 219-221
    sprite('Action_250_46', 3)	# 222-224
    sprite('Action_250_47', 3)	# 225-227
    sprite('Action_250_48', 3)	# 228-230
    sprite('Action_250_49', 3)	# 231-233
    sprite('Action_250_50', 3)	# 234-236
    sprite('Action_250_48', 3)	# 237-239
    sprite('Action_250_49', 3)	# 240-242
    sprite('Action_250_50', 3)	# 243-245
    sprite('Action_250_51', 3)	# 246-248
    sprite('Action_250_52', 2)	# 249-250
    sprite('Action_250_53', 2)	# 251-252
    sprite('Action_250_54', 5)	# 253-257
    sprite('Action_250_55', 9)	# 258-266
    sprite('Action_250_56', 15)	# 267-281
    GFX_0('WinEff1', -1)
    sprite('Action_250_57', 4)	# 282-285
    GFX_0('UltimateShotAtkFinish', -1)
    sprite('Action_250_58', 3)	# 286-288
    GFX_0('WinEff2', -1)
    sprite('Action_250_59', 3)	# 289-291
    sprite('Action_250_60', 3)	# 292-294
    tag_voice(0, 'uca252_0', 'uca252_1', '', '')
    sprite('Action_250_61', 3)	# 295-297
    sprite('Action_250_60', 3)	# 298-300
    sprite('Action_250_61', 3)	# 301-303
    sprite('Action_250_60', 3)	# 304-306
    sprite('Action_250_61', 3)	# 307-309
    sprite('Action_250_60', 3)	# 310-312
    sprite('Action_250_61', 3)	# 313-315
    sprite('Action_250_60', 3)	# 316-318
    sprite('Action_250_61', 3)	# 319-321
    sprite('Action_250_60', 3)	# 322-324
    sprite('Action_250_61', 3)	# 325-327
    sprite('Action_250_60', 3)	# 328-330
    sprite('Action_250_61', 3)	# 331-333
    sprite('Action_250_60', 3)	# 334-336
    sprite('Action_250_61', 3)	# 337-339
    sprite('Action_250_62', 3)	# 340-342
    sprite('Action_250_63', 6)	# 343-348
    Unknown23029(11, 2502, 0)
    sprite('Action_250_64', 4)	# 349-352

@State
def UltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        Unknown2037(0)

        def upon_43():
            if (SLOT_48 == 2501):
                Unknown13024(0)
                Unknown2037(1)
            if (SLOT_48 == 2503):
                Unknown13024(1)
        Unknown2021(1)

        def upon_STATE_END():
            Unknown23029(11, 2502, 0)
    sprite('Action_250_00', 3)	# 1-3
    sprite('Action_250_00', 12)	# 4-15
    Unknown2036(59, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uca250_0', 'uca250_1', '', '')
    sprite('Action_250_00', 5)	# 16-20
    sprite('Action_250_01', 7)	# 21-27
    sprite('Action_250_02', 7)	# 28-34
    sprite('Action_250_03', 7)	# 35-41
    sprite('Action_250_04', 7)	# 42-48
    sprite('Action_250_05', 3)	# 49-51	 **attackbox here**
    SFX_3('SE012')
    sprite('Action_250_06', 3)	# 52-54	 **attackbox here**
    sprite('Action_250_07', 3)	# 55-57	 **attackbox here**
    sprite('Action_250_08', 2)	# 58-59	 **attackbox here**
    sprite('Action_250_08', 1)	# 60-60	 **attackbox here**
    GFX_0('UltimateShotEffMaster', -1)
    Unknown23029(1, 2505, 0)
    sprite('Action_250_09', 2)	# 61-62
    SFX_3('SE045')
    sprite('Action_250_10', 3)	# 63-65
    sprite('Action_250_11', 3)	# 66-68
    GFX_0('UltimateShotFootEff', -1)
    Unknown38(11, 1)
    Unknown23029(1, 2505, 0)
    sprite('Action_250_12', 2)	# 69-70
    sprite('Action_250_13', 3)	# 71-73
    sprite('Action_250_14', 3)	# 74-76
    sprite('Action_250_15', 3)	# 77-79
    sprite('Action_250_16', 3)	# 80-82
    sprite('Action_250_17', 3)	# 83-85
    sprite('Action_250_18', 2)	# 86-87	 **attackbox here**
    StartMultihit()
    sprite('Action_250_18', 1)	# 88-88	 **attackbox here**
    StartMultihit()
    if SLOT_2:
        sendToLabel(1)
    sprite('Action_250_20', 3)	# 89-91
    setInvincible(0)
    sprite('Action_250_21', 3)	# 92-94
    sprite('Action_250_22', 3)	# 95-97
    sprite('Action_250_20', 3)	# 98-100
    sprite('Action_250_21', 3)	# 101-103
    sprite('Action_250_22', 3)	# 104-106
    sprite('Action_250_20', 3)	# 107-109
    sprite('Action_250_21', 3)	# 110-112
    sprite('Action_250_22', 3)	# 113-115
    sprite('Action_250_20', 3)	# 116-118
    sprite('Action_250_21', 3)	# 119-121
    sprite('Action_250_22', 3)	# 122-124
    sprite('Action_250_20', 3)	# 125-127
    sprite('Action_250_21', 3)	# 128-130
    sprite('Action_250_22', 3)	# 131-133
    sprite('Action_250_20', 3)	# 134-136
    sprite('Action_250_21', 3)	# 137-139
    sprite('Action_250_22', 3)	# 140-142
    sprite('Action_250_23', 3)	# 143-145
    sprite('Action_250_24', 5)	# 146-150
    Unknown23029(11, 2502, 0)
    sprite('Action_250_25', 5)	# 151-155
    ExitState()
    label(1)
    sprite('Action_250_27', 3)	# 156-158
    sprite('Action_250_28', 3)	# 159-161
    sprite('Action_250_29', 3)	# 162-164
    sprite('Action_250_27', 3)	# 165-167
    GFX_0('UltimateShotAtkExe', -1)
    Unknown23029(1, 2505, 0)
    tag_voice(0, 'uca251_0', 'uca251_1', '', '')
    sprite('Action_250_28', 3)	# 168-170
    sprite('Action_250_29', 3)	# 171-173
    sprite('Action_250_30', 3)	# 174-176
    sprite('Action_250_31', 3)	# 177-179
    sprite('Action_250_32', 3)	# 180-182
    sprite('Action_250_33', 3)	# 183-185
    sprite('Action_250_34', 3)	# 186-188
    sprite('Action_250_35', 3)	# 189-191
    sprite('Action_250_36', 3)	# 192-194
    sprite('Action_250_37', 3)	# 195-197
    sprite('Action_250_38', 3)	# 198-200
    sprite('Action_250_39', 3)	# 201-203
    sprite('Action_250_40', 3)	# 204-206
    sprite('Action_250_41', 3)	# 207-209
    sprite('Action_250_42', 3)	# 210-212
    sprite('Action_250_43', 3)	# 213-215
    sprite('Action_250_44', 3)	# 216-218
    sprite('Action_250_45', 3)	# 219-221
    sprite('Action_250_46', 3)	# 222-224
    sprite('Action_250_47', 3)	# 225-227
    sprite('Action_250_48', 3)	# 228-230
    sprite('Action_250_49', 3)	# 231-233
    sprite('Action_250_50', 3)	# 234-236
    sprite('Action_250_51', 3)	# 237-239
    sprite('Action_250_52', 2)	# 240-241
    sprite('Action_260_00', 9)	# 242-250
    sprite('Action_260_01', 3)	# 251-253
    sprite('Action_260_02', 2)	# 254-255
    sprite('Action_260_03', 5)	# 256-260
    sprite('Action_260_04', 5)	# 261-265
    sprite('Action_260_05', 5)	# 266-270
    sprite('Action_260_06', 5)	# 271-275
    sprite('Action_260_07', 5)	# 276-280
    sprite('Action_260_08', 5)	# 281-285
    sprite('Action_260_09', 3)	# 286-288
    sprite('Action_260_10', 3)	# 289-291
    sprite('Action_260_11', 3)	# 292-294
    sprite('Action_260_12', 3)	# 295-297
    sprite('Action_250_53', 2)	# 298-299
    sprite('Action_250_54', 5)	# 300-304
    sprite('Action_250_55', 9)	# 305-313
    sprite('Action_250_56', 15)	# 314-328
    GFX_0('WinEff1', -1)
    sprite('Action_250_57', 4)	# 329-332
    GFX_0('UltimateShotAtkFinish', -1)
    Unknown23029(1, 2505, 0)
    tag_voice(0, 'uca252_0', 'uca252_1', '', '')
    sprite('Action_250_58', 3)	# 333-335
    GFX_0('WinEff2', -1)
    sprite('Action_250_59', 3)	# 336-338
    sprite('Action_250_60', 3)	# 339-341
    sprite('Action_250_61', 3)	# 342-344
    sprite('Action_250_60', 3)	# 345-347
    sprite('Action_250_61', 3)	# 348-350
    sprite('Action_250_60', 3)	# 351-353
    sprite('Action_250_61', 3)	# 354-356
    sprite('Action_250_60', 3)	# 357-359
    sprite('Action_250_61', 3)	# 360-362
    sprite('Action_250_60', 3)	# 363-365
    sprite('Action_250_61', 3)	# 366-368
    sprite('Action_250_60', 3)	# 369-371
    sprite('Action_250_61', 3)	# 372-374
    sprite('Action_250_60', 3)	# 375-377
    sprite('Action_250_61', 3)	# 378-380
    sprite('Action_250_60', 3)	# 381-383
    sprite('Action_250_61', 3)	# 384-386
    sprite('Action_250_60', 3)	# 387-389
    sprite('Action_250_61', 3)	# 390-392
    sprite('Action_250_62', 3)	# 393-395
    sprite('Action_250_63', 6)	# 396-401
    Unknown23029(11, 2502, 0)
    sprite('Action_250_64', 3)	# 402-404

@Subroutine
def DissolveActivatePU_DS():
    if Unknown46(4):
        Unknown23029(4, 9994, 0)
    if Unknown46(5):
        Unknown23029(5, 9994, 0)
    if Unknown46(6):
        Unknown23029(6, 9994, 0)
    if Unknown46(7):
        Unknown23029(7, 9994, 0)
    if Unknown46(8):
        Unknown23029(8, 9994, 0)

@State
def PushUpShotDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 1794):
                clearUponHandler(43)
                setInvincible(1)
                Unknown2037(1)
    sprite('Action_261_01', 4)	# 1-4
    tag_voice(1, 'uca253_0', 'uca253_1', '', '')
    sprite('Action_261_02', 3)	# 5-7
    sprite('Action_261_03', 4)	# 8-11
    sprite('Action_261_04', 4)	# 12-15
    Unknown2036(37, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_261_05', 4)	# 16-19
    sprite('Action_261_06', 4)	# 20-23
    sprite('Action_261_08', 4)	# 24-27
    sprite('Action_261_09', 4)	# 28-31
    sprite('Action_261_10', 4)	# 32-35
    sprite('Action_261_12', 3)	# 36-38
    sprite('Action_261_13', 3)	# 39-41
    sprite('Action_000_00', 3)	# 42-44	 **attackbox here**
    sprite('Action_181_00', 3)	# 45-47
    sprite('Action_181_00', 2)	# 48-49
    sprite('Action_181_01', 5)	# 50-54
    sprite('Action_181_02', 1)	# 55-55
    sprite('Action_181_02', 4)	# 56-59
    callSubroutine('DissolveActivatePU_DS')
    GFX_0('PushUpShotTypeEx', -1)
    sprite('Action_181_03', 7)	# 60-66
    sprite('Action_181_03', 3)	# 67-69
    tag_voice(0, 'uca254_0', 'uca254_1', '', '')
    sprite('Action_181_04', 11)	# 70-80
    if (not SLOT_2):
        setInvincible(0)
    sprite('Action_181_05', 9)	# 81-89
    sprite('Action_181_06', 8)	# 90-97
    sprite('Action_181_07', 9)	# 98-106

@State
def PushUpShotDD_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 1794):
                clearUponHandler(43)
                setInvincible(1)
                Unknown2037(1)
    sprite('Action_261_01', 4)	# 1-4
    tag_voice(1, 'uca253_0', 'uca253_1', '', '')
    sprite('Action_261_02', 3)	# 5-7
    sprite('Action_261_03', 4)	# 8-11
    sprite('Action_261_04', 4)	# 12-15
    Unknown2036(37, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_261_05', 4)	# 16-19
    sprite('Action_261_06', 4)	# 20-23
    sprite('Action_261_08', 4)	# 24-27
    sprite('Action_261_09', 4)	# 28-31
    sprite('Action_261_10', 4)	# 32-35
    sprite('Action_261_12', 3)	# 36-38
    sprite('Action_261_13', 3)	# 39-41
    sprite('Action_000_00', 3)	# 42-44	 **attackbox here**
    sprite('Action_181_00', 3)	# 45-47
    sprite('Action_181_00', 2)	# 48-49
    sprite('Action_181_01', 5)	# 50-54
    sprite('Action_181_02', 1)	# 55-55
    sprite('Action_181_02', 4)	# 56-59
    callSubroutine('DissolveActivatePU_DS')
    GFX_0('PushUpShotTypeEx_OD', -1)
    sprite('Action_181_03', 7)	# 60-66
    sprite('Action_181_03', 3)	# 67-69
    tag_voice(0, 'uca254_0', 'uca254_1', '', '')
    sprite('Action_181_04', 11)	# 70-80
    if (not SLOT_2):
        setInvincible(0)
    sprite('Action_181_05', 9)	# 81-89
    sprite('Action_181_06', 8)	# 90-97
    sprite('Action_181_07', 9)	# 98-106

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 2611):
                Unknown2037(1)
            if (SLOT_48 == 2612):
                Unknown21015('41485f43616d6572610000000000000000000000000000000000000000000000330a000000000000')
            if (SLOT_48 == 2619):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_261_00', 5)	# 1-5
    Unknown2036(80, -1, 1)
    Unknown23147()
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_261_01', 4)	# 6-9
    SFX_4('uca290')
    sprite('Action_261_02', 3)	# 10-12
    GFX_0('DDCutIn', 100)
    sprite('Action_261_03', 4)	# 13-16
    sprite('Action_261_04', 4)	# 17-20
    sprite('Action_261_05', 4)	# 21-24
    sprite('Action_261_06', 4)	# 25-28
    sprite('Action_261_05', 4)	# 29-32
    sprite('Action_261_06', 4)	# 33-36
    sprite('Action_261_08', 4)	# 37-40
    sprite('Action_261_09', 4)	# 41-44
    sprite('Action_261_10', 4)	# 45-48
    sprite('Action_261_08', 4)	# 49-52
    sprite('Action_261_09', 4)	# 53-56
    sprite('Action_261_10', 4)	# 57-60
    sprite('Action_261_12', 3)	# 61-63
    sprite('Action_261_13', 3)	# 64-66
    sprite('Action_000_00', 3)	# 67-69	 **attackbox here**
    sprite('Action_000_31', 3)	# 70-72
    sprite('Action_000_30', 3)	# 73-75
    sprite('Action_380_00', 4)	# 76-79
    sprite('Action_380_01', 4)	# 80-83
    sprite('Action_380_02', 5)	# 84-88
    sprite('Action_380_03', 4)	# 89-92
    sprite('Action_380_04', 4)	# 93-96
    GFX_0('AH_Attack1', -1)
    sprite('Action_380_05', 7)	# 97-103
    sprite('Action_380_06', 4)	# 104-107

    def upon_3():
        if SLOT_2:
            sendToLabel(0)
    sprite('Action_380_06', 56)	# 108-163
    setInvincible(0)
    loopRest()
    clearUponHandler(3)
    sprite('Action_380_07', 5)	# 164-168
    sprite('Action_380_08', 4)	# 169-172
    sprite('Action_380_09', 6)	# 173-178
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_380_10', 4)	# 179-182
    sprite('Action_380_11', 4)	# 183-186
    sprite('Action_380_12', 6)	# 187-192
    sprite('Action_380_13', 20)	# 193-212
    sprite('Action_380_14', 20)	# 213-232
    sprite('Action_000_27', 7)	# 233-239
    sprite('Action_000_28', 5)	# 240-244
    ExitState()
    label(0)
    sprite('Action_380_06', 20)	# 245-264
    clearUponHandler(3)
    Unknown23083(1)
    Unknown23157(1)
    Unknown23084(1)
    Unknown23088(1, 1)
    GFX_0('AH_White', -1)
    GFX_0('AH_Camera', -1)
    SFX_4('uca291')
    sprite('Action_380_06', 50)	# 265-314
    Unknown20003(1)
    if SLOT_38:
        Unknown1001(300000)
    else:
        Unknown1001(-300000)
    Unknown36(22)
    Unknown20003(1)
    physicsYImpulse(2000)
    Unknown1000(-300000)
    teleportRelativeY(50000)
    Unknown35()
    sprite('Action_380_06', 90)	# 315-404
    Unknown36(22)
    physicsYImpulse(1)
    Unknown35()
    sprite('Action_380_07', 5)	# 405-409
    sprite('Action_380_08', 4)	# 410-413
    GFX_0('AH_Attack3', -1)
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_380_09', 6)	# 414-419
    Unknown3025(0, 30)
    GFX_0('AH_Attack2', -1)
    GFX_0('AH_BG', 100)
    sprite('Action_380_10', 4)	# 420-423
    sprite('Action_380_11', 4)	# 424-427
    GFX_0('AH_Attack4', 0)
    sprite('Action_380_12', 6)	# 428-433
    sprite('Action_380_13', 10)	# 434-443
    GFX_0('AH_Wave_Matome', 100)
    sprite('Action_380_13', 10)	# 444-453
    sprite('Action_380_14', 60)	# 454-513
    sprite('Action_380_15', 170)	# 514-683
    sprite('Action_380_15', 32767)	# 684-33450
    SFX_4('uca292')
    Unknown3026(-1)
    label(1)
    sprite('Action_250_60', 3)	# 33451-33453
    Unknown2054(1)
    sprite('Action_250_61', 3)	# 33454-33456
    sprite('Action_250_60', 3)	# 33457-33459
    sprite('Action_250_61', 3)	# 33460-33462
    sprite('Action_250_60', 3)	# 33463-33465
    sprite('Action_250_61', 3)	# 33466-33468
    sprite('Action_250_60', 3)	# 33469-33471
    sprite('Action_250_61', 3)	# 33472-33474
    sprite('Action_250_60', 3)	# 33475-33477
    sprite('Action_250_61', 3)	# 33478-33480
    sprite('Action_250_60', 3)	# 33481-33483
    sprite('Action_250_61', 3)	# 33484-33486
    sprite('Action_250_60', 3)	# 33487-33489
    sprite('Action_250_61', 3)	# 33490-33492
    sprite('Action_250_60', 3)	# 33493-33495
    sprite('Action_250_61', 3)	# 33496-33498
    sprite('Action_250_60', 3)	# 33499-33501
    sprite('Action_250_61', 3)	# 33502-33504
    sprite('Action_250_60', 3)	# 33505-33507
    sprite('Action_250_61', 3)	# 33508-33510
    sprite('Action_250_60', 3)	# 33511-33513
    sprite('Action_250_61', 3)	# 33514-33516
    sprite('Action_250_60', 3)	# 33517-33519
    sprite('Action_250_61', 3)	# 33520-33522
    sprite('Action_250_60', 3)	# 33523-33525
    sprite('Action_250_61', 3)	# 33526-33528
    sprite('Action_250_60', 3)	# 33529-33531
    sprite('Action_250_61', 3)	# 33532-33534
    sprite('Action_250_60', 3)	# 33535-33537
    sprite('Action_250_61', 3)	# 33538-33540
    sprite('Action_250_60', 3)	# 33541-33543
    sprite('Action_250_61', 3)	# 33544-33546
    sprite('Action_250_60', 3)	# 33547-33549
    sprite('Action_250_61', 3)	# 33550-33552
    sprite('Action_250_60', 3)	# 33553-33555
    sprite('Action_250_61', 3)	# 33556-33558
    sprite('Action_250_60', 3)	# 33559-33561
    sprite('Action_250_61', 3)	# 33562-33564
    sprite('Action_250_60', 3)	# 33565-33567
    sprite('Action_250_61', 3)	# 33568-33570
    sprite('Action_250_62', 3)	# 33571-33573
    sprite('Action_250_63', 6)	# 33574-33579
    sprite('Action_250_64', 4)	# 33580-33583

@Subroutine
def MouthTableInit():
    Unknown18011('uca000', 12643, 14177, 14179, 12641, 25394, 14129, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca500', 12643, 12641, 25397, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25397, 24885, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca502', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca503', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca504', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca505', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca520', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca521', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca522', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca523', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca524', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca525', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca402_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca402_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca403_0', 12643, 13153, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca403_1', 12643, 13665, 13667, 13665, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca600bph', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 13155, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca600pak', 12643, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 12337, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca600ryn', 12643, 14177, 13411, 24885, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca600ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 12641, 25397, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601bmk', 12643, 14177, 12643, 24885, 25399, 12337, 14177, 12643, 24880, 25399, 13621, 14177, 12643, 24882, 25399, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601pka', 12643, 12897, 25392, 24887, 13617, 13923, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601pyu', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601ume', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca601uwa', 12643, 12641, 25397, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca700baz', 12643, 12641, 25397, 24887, 25399, 24887, 25399, 14130, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13617, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca700bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca700pak', 12643, 12897, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca700ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701bmk', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701bph', 12643, 14177, 13667, 24885, 25399, 24887, 25399, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14435, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701pka', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701pyu', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701ryn', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701ugo', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uca701uwa', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('ume')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    sprite('Action_050_02', 7)	# 2-8
    sprite('Action_050_03', 5)	# 9-13
    sprite('Action_050_04', 5)	# 14-18
    sprite('Action_050_05', 5)	# 19-23
    sprite('Action_050_06', 3)	# 24-26
    if random_(2, 0, 50):
        Unknown7006('uca500', 100, 895574901, 12592, 0, 0, 100, 895574901, 12848, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('uca503', 100, 895574901, 13360, 0, 0, 100, 895574901, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_1('uca503')
    sprite('Action_050_07', 7)	# 27-33
    sprite('Action_050_08', 10)	# 34-43
    sprite('Action_050_09', 11)	# 44-54
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 55-68
    sprite('Action_050_11', 9)	# 69-77	 **attackbox here**
    sprite('Action_050_12', 6)	# 78-83	 **attackbox here**
    sprite('Action_050_13', 5)	# 84-88	 **attackbox here**
    sprite('Action_050_14', 5)	# 89-93	 **attackbox here**
    sprite('Action_050_15', 4)	# 94-97	 **attackbox here**
    sprite('Action_050_16', 4)	# 98-101	 **attackbox here**
    sprite('Action_050_17', 3)	# 102-104	 **attackbox here**
    sprite('Action_050_18', 3)	# 105-107	 **attackbox here**
    sprite('Action_050_19', 8)	# 108-115	 **attackbox here**
    sprite('Action_050_20', 12)	# 116-127	 **attackbox here**
    sprite('Action_050_21', 15)	# 128-142	 **attackbox here**
    sprite('Action_050_22', 8)	# 143-150
    sprite('Action_050_23', 5)	# 151-155
    Unknown23018(1)
    label(1)
    sprite('Action_000_00', 7)	# 156-162	 **attackbox here**
    sprite('Action_000_01', 7)	# 163-169	 **attackbox here**
    sprite('Action_000_02', 8)	# 170-177	 **attackbox here**
    sprite('Action_000_03', 8)	# 178-185	 **attackbox here**
    sprite('Action_000_04', 10)	# 186-195	 **attackbox here**
    sprite('Action_000_05', 9)	# 196-204	 **attackbox here**
    sprite('Action_000_06', 11)	# 205-215	 **attackbox here**
    sprite('Action_000_07', 8)	# 216-223	 **attackbox here**
    sprite('Action_000_08', 7)	# 224-230	 **attackbox here**
    sprite('Action_000_09', 6)	# 231-236	 **attackbox here**
    sprite('Action_000_10', 7)	# 237-243	 **attackbox here**
    sprite('Action_000_11', 7)	# 244-250	 **attackbox here**
    sprite('Action_000_12', 8)	# 251-258	 **attackbox here**
    sprite('Action_000_13', 7)	# 259-265	 **attackbox here**
    sprite('Action_000_14', 7)	# 266-272	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('Action_248_00', 5)	# 273-277
    sprite('Action_248_01', 3)	# 278-280
    sprite('Action_248_07', 5)	# 281-285
    sprite('Action_248_08', 5)	# 286-290
    sprite('Action_248_09', 30)	# 291-320
    sprite('Action_248_10', 32767)	# 321-33087	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_000_00', 1)	# 33088-33088	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_000_00', 7)	# 33089-33095	 **attackbox here**
    sprite('Action_000_01', 7)	# 33096-33102	 **attackbox here**
    sprite('Action_000_02', 8)	# 33103-33110	 **attackbox here**
    sprite('Action_000_03', 8)	# 33111-33118	 **attackbox here**
    sprite('Action_000_04', 10)	# 33119-33128	 **attackbox here**
    sprite('Action_000_05', 9)	# 33129-33137	 **attackbox here**
    sprite('Action_000_06', 11)	# 33138-33148	 **attackbox here**
    sprite('Action_000_07', 8)	# 33149-33156	 **attackbox here**
    sprite('Action_000_08', 7)	# 33157-33163	 **attackbox here**
    sprite('Action_000_09', 6)	# 33164-33169	 **attackbox here**
    sprite('Action_000_10', 7)	# 33170-33176	 **attackbox here**
    sprite('Action_000_11', 7)	# 33177-33183	 **attackbox here**
    sprite('Action_000_12', 8)	# 33184-33191	 **attackbox here**
    sprite('Action_000_13', 7)	# 33192-33198	 **attackbox here**
    sprite('Action_000_14', 7)	# 33199-33205	 **attackbox here**
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('Action_052_00', 2)	# 33206-33207
    sprite('Action_052_01', 6)	# 33208-33213
    sprite('Action_052_02', 7)	# 33214-33220
    sprite('Action_052_03', 4)	# 33221-33224
    SFX_1('uca601bhz')
    sprite('Action_052_04', 5)	# 33225-33229
    sprite('Action_052_05', 9)	# 33230-33238
    sprite('Action_052_06', 15)	# 33239-33253
    sprite('Action_052_07', 4)	# 33254-33257
    sprite('Action_052_08', 4)	# 33258-33261
    Unknown23018(1)
    label(103)
    sprite('Action_052_09', 4)	# 33262-33265
    sprite('Action_052_10', 4)	# 33266-33269
    loopRest()
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('Action_050_02', 1)	# 33270-33270
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_050_02', 5)	# 33271-33275
    sprite('Action_050_03', 5)	# 33276-33280
    sprite('Action_050_04', 5)	# 33281-33285
    sprite('Action_050_05', 5)	# 33286-33290
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('Action_050_06', 3)	# 33291-33293
    SFX_1('uca601bmk')
    sprite('Action_050_07', 7)	# 33294-33300
    sprite('Action_050_08', 10)	# 33301-33310
    sprite('Action_050_09', 11)	# 33311-33321
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 33322-33335
    sprite('Action_050_11', 9)	# 33336-33344	 **attackbox here**
    sprite('Action_050_12', 6)	# 33345-33350	 **attackbox here**
    sprite('Action_050_13', 5)	# 33351-33355	 **attackbox here**
    sprite('Action_050_14', 5)	# 33356-33360	 **attackbox here**
    sprite('Action_050_15', 4)	# 33361-33364	 **attackbox here**
    sprite('Action_050_16', 4)	# 33365-33368	 **attackbox here**
    sprite('Action_050_17', 3)	# 33369-33371	 **attackbox here**
    sprite('Action_050_18', 3)	# 33372-33374	 **attackbox here**
    sprite('Action_050_19', 8)	# 33375-33382	 **attackbox here**
    sprite('Action_050_20', 12)	# 33383-33394	 **attackbox here**
    sprite('Action_050_21', 15)	# 33395-33409	 **attackbox here**
    sprite('Action_050_22', 8)	# 33410-33417
    sprite('Action_050_23', 5)	# 33418-33422
    Unknown23018(1)
    label(113)
    sprite('Action_000_00', 7)	# 33423-33429	 **attackbox here**
    sprite('Action_000_01', 7)	# 33430-33436	 **attackbox here**
    sprite('Action_000_02', 8)	# 33437-33444	 **attackbox here**
    sprite('Action_000_03', 8)	# 33445-33452	 **attackbox here**
    sprite('Action_000_04', 10)	# 33453-33462	 **attackbox here**
    sprite('Action_000_05', 9)	# 33463-33471	 **attackbox here**
    sprite('Action_000_06', 11)	# 33472-33482	 **attackbox here**
    sprite('Action_000_07', 8)	# 33483-33490	 **attackbox here**
    sprite('Action_000_08', 7)	# 33491-33497	 **attackbox here**
    sprite('Action_000_09', 6)	# 33498-33503	 **attackbox here**
    sprite('Action_000_10', 7)	# 33504-33510	 **attackbox here**
    sprite('Action_000_11', 7)	# 33511-33517	 **attackbox here**
    sprite('Action_000_12', 8)	# 33518-33525	 **attackbox here**
    sprite('Action_000_13', 7)	# 33526-33532	 **attackbox here**
    sprite('Action_000_14', 7)	# 33533-33539	 **attackbox here**
    loopRest()
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('Action_050_02', 1)	# 33540-33540
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('Action_050_02', 5)	# 33541-33545
    sprite('Action_050_03', 5)	# 33546-33550
    sprite('Action_050_04', 5)	# 33551-33555
    sprite('Action_050_05', 5)	# 33556-33560
    loopRest()
    gotoLabel(121)
    label(122)
    sprite('Action_050_06', 3)	# 33561-33563
    SFX_1('uca601baz')
    sprite('Action_050_07', 7)	# 33564-33570
    sprite('Action_050_08', 10)	# 33571-33580
    sprite('Action_050_09', 11)	# 33581-33591
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 33592-33605
    sprite('Action_050_11', 9)	# 33606-33614	 **attackbox here**
    sprite('Action_050_12', 6)	# 33615-33620	 **attackbox here**
    sprite('Action_050_13', 5)	# 33621-33625	 **attackbox here**
    sprite('Action_050_14', 5)	# 33626-33630	 **attackbox here**
    sprite('Action_050_15', 4)	# 33631-33634	 **attackbox here**
    sprite('Action_050_16', 4)	# 33635-33638	 **attackbox here**
    sprite('Action_050_17', 3)	# 33639-33641	 **attackbox here**
    sprite('Action_050_18', 3)	# 33642-33644	 **attackbox here**
    sprite('Action_050_19', 8)	# 33645-33652	 **attackbox here**
    sprite('Action_050_20', 12)	# 33653-33664	 **attackbox here**
    sprite('Action_050_21', 15)	# 33665-33679	 **attackbox here**
    sprite('Action_050_22', 8)	# 33680-33687
    sprite('Action_050_23', 5)	# 33688-33692
    Unknown23018(1)
    label(123)
    sprite('Action_000_00', 7)	# 33693-33699	 **attackbox here**
    sprite('Action_000_01', 7)	# 33700-33706	 **attackbox here**
    sprite('Action_000_02', 8)	# 33707-33714	 **attackbox here**
    sprite('Action_000_03', 8)	# 33715-33722	 **attackbox here**
    sprite('Action_000_04', 10)	# 33723-33732	 **attackbox here**
    sprite('Action_000_05', 9)	# 33733-33741	 **attackbox here**
    sprite('Action_000_06', 11)	# 33742-33752	 **attackbox here**
    sprite('Action_000_07', 8)	# 33753-33760	 **attackbox here**
    sprite('Action_000_08', 7)	# 33761-33767	 **attackbox here**
    sprite('Action_000_09', 6)	# 33768-33773	 **attackbox here**
    sprite('Action_000_10', 7)	# 33774-33780	 **attackbox here**
    sprite('Action_000_11', 7)	# 33781-33787	 **attackbox here**
    sprite('Action_000_12', 8)	# 33788-33795	 **attackbox here**
    sprite('Action_000_13', 7)	# 33796-33802	 **attackbox here**
    sprite('Action_000_14', 7)	# 33803-33809	 **attackbox here**
    loopRest()
    gotoLabel(123)
    ExitState()
    label(130)
    sprite('Action_000_00', 1)	# 33810-33810	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('Action_000_00', 7)	# 33811-33817	 **attackbox here**
    sprite('Action_000_01', 7)	# 33818-33824	 **attackbox here**
    sprite('Action_000_02', 8)	# 33825-33832	 **attackbox here**
    sprite('Action_000_03', 8)	# 33833-33840	 **attackbox here**
    sprite('Action_000_04', 10)	# 33841-33850	 **attackbox here**
    sprite('Action_000_05', 9)	# 33851-33859	 **attackbox here**
    sprite('Action_000_06', 11)	# 33860-33870	 **attackbox here**
    sprite('Action_000_07', 8)	# 33871-33878	 **attackbox here**
    sprite('Action_000_08', 7)	# 33879-33885	 **attackbox here**
    sprite('Action_000_09', 6)	# 33886-33891	 **attackbox here**
    sprite('Action_000_10', 7)	# 33892-33898	 **attackbox here**
    sprite('Action_000_11', 7)	# 33899-33905	 **attackbox here**
    sprite('Action_000_12', 8)	# 33906-33913	 **attackbox here**
    sprite('Action_000_13', 7)	# 33914-33920	 **attackbox here**
    sprite('Action_000_14', 7)	# 33921-33927	 **attackbox here**
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('Action_248_00', 5)	# 33928-33932
    SFX_1('uca601pyu')
    sprite('Action_248_01', 3)	# 33933-33935
    sprite('Action_248_02', 13)	# 33936-33948
    sprite('Action_248_03', 60)	# 33949-34008
    sprite('Action_248_04', 11)	# 34009-34019
    sprite('Action_248_05', 9)	# 34020-34028
    sprite('Action_248_06', 6)	# 34029-34034
    sprite('Action_248_07', 5)	# 34035-34039
    sprite('Action_248_08', 5)	# 34040-34044
    sprite('Action_248_09', 30)	# 34045-34074
    Unknown23018(1)
    sprite('Action_248_10', 32767)	# 34075-66841	 **attackbox here**
    ExitState()
    label(140)
    sprite('Action_000_00', 1)	# 66842-66842	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('Action_000_00', 7)	# 66843-66849	 **attackbox here**
    sprite('Action_000_01', 7)	# 66850-66856	 **attackbox here**
    sprite('Action_000_02', 8)	# 66857-66864	 **attackbox here**
    sprite('Action_000_03', 8)	# 66865-66872	 **attackbox here**
    sprite('Action_000_04', 10)	# 66873-66882	 **attackbox here**
    sprite('Action_000_05', 9)	# 66883-66891	 **attackbox here**
    sprite('Action_000_06', 11)	# 66892-66902	 **attackbox here**
    sprite('Action_000_07', 8)	# 66903-66910	 **attackbox here**
    sprite('Action_000_08', 7)	# 66911-66917	 **attackbox here**
    sprite('Action_000_09', 6)	# 66918-66923	 **attackbox here**
    sprite('Action_000_10', 7)	# 66924-66930	 **attackbox here**
    sprite('Action_000_11', 7)	# 66931-66937	 **attackbox here**
    sprite('Action_000_12', 8)	# 66938-66945	 **attackbox here**
    sprite('Action_000_13', 7)	# 66946-66952	 **attackbox here**
    sprite('Action_000_14', 7)	# 66953-66959	 **attackbox here**
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('Action_052_00', 2)	# 66960-66961
    sprite('Action_052_01', 6)	# 66962-66967
    sprite('Action_052_02', 7)	# 66968-66974
    sprite('Action_052_03', 4)	# 66975-66978
    sprite('Action_052_04', 5)	# 66979-66983
    SFX_1('uca601pka')
    sprite('Action_052_05', 9)	# 66984-66992
    sprite('Action_052_06', 45)	# 66993-67037
    sprite('Action_052_07', 4)	# 67038-67041
    sprite('Car643_00', 7)	# 67042-67048
    sprite('Car643_01', 7)	# 67049-67055
    Unknown23018(1)
    sprite('Car643_02', 32767)	# 67056-99822	 **attackbox here**
    ExitState()
    label(150)
    sprite('Action_050_02', 1)	# 99823-99823
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Action_050_02', 5)	# 99824-99828
    sprite('Action_050_03', 5)	# 99829-99833
    sprite('Action_050_04', 5)	# 99834-99838
    sprite('Action_050_05', 5)	# 99839-99843
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('Action_050_06', 3)	# 99844-99846
    SFX_1('uca601uwa')
    sprite('Action_050_07', 7)	# 99847-99853
    sprite('Action_050_08', 10)	# 99854-99863
    sprite('Action_050_09', 11)	# 99864-99874
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 99875-99888
    sprite('Action_050_11', 9)	# 99889-99897	 **attackbox here**
    sprite('Action_050_12', 6)	# 99898-99903	 **attackbox here**
    sprite('Action_050_13', 5)	# 99904-99908	 **attackbox here**
    sprite('Action_050_14', 5)	# 99909-99913	 **attackbox here**
    sprite('Action_050_15', 4)	# 99914-99917	 **attackbox here**
    sprite('Action_050_16', 4)	# 99918-99921	 **attackbox here**
    sprite('Action_050_17', 3)	# 99922-99924	 **attackbox here**
    sprite('Action_050_18', 3)	# 99925-99927	 **attackbox here**
    sprite('Action_050_19', 8)	# 99928-99935	 **attackbox here**
    sprite('Action_050_20', 12)	# 99936-99947	 **attackbox here**
    sprite('Action_050_21', 15)	# 99948-99962	 **attackbox here**
    sprite('Action_050_22', 8)	# 99963-99970
    sprite('Action_050_23', 5)	# 99971-99975
    Unknown23018(1)
    label(153)
    sprite('Action_000_00', 7)	# 99976-99982	 **attackbox here**
    sprite('Action_000_01', 7)	# 99983-99989	 **attackbox here**
    sprite('Action_000_02', 8)	# 99990-99997	 **attackbox here**
    sprite('Action_000_03', 8)	# 99998-100005	 **attackbox here**
    sprite('Action_000_04', 10)	# 100006-100015	 **attackbox here**
    sprite('Action_000_05', 9)	# 100016-100024	 **attackbox here**
    sprite('Action_000_06', 11)	# 100025-100035	 **attackbox here**
    sprite('Action_000_07', 8)	# 100036-100043	 **attackbox here**
    sprite('Action_000_08', 7)	# 100044-100050	 **attackbox here**
    sprite('Action_000_09', 6)	# 100051-100056	 **attackbox here**
    sprite('Action_000_10', 7)	# 100057-100063	 **attackbox here**
    sprite('Action_000_11', 7)	# 100064-100070	 **attackbox here**
    sprite('Action_000_12', 8)	# 100071-100078	 **attackbox here**
    sprite('Action_000_13', 7)	# 100079-100085	 **attackbox here**
    sprite('Action_000_14', 7)	# 100086-100092	 **attackbox here**
    loopRest()
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('Action_050_02', 7)	# 100093-100099
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_03', 5)	# 100100-100104
    SFX_1('uca600ugo')
    sprite('Action_050_04', 5)	# 100105-100109
    sprite('Action_050_05', 5)	# 100110-100114
    sprite('Action_050_06', 3)	# 100115-100117
    sprite('Action_050_07', 7)	# 100118-100124
    sprite('Action_050_08', 10)	# 100125-100134
    sprite('Action_050_09', 11)	# 100135-100145
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 100146-100159
    sprite('Action_050_11', 9)	# 100160-100168	 **attackbox here**
    sprite('Action_050_12', 6)	# 100169-100174	 **attackbox here**
    sprite('Action_050_13', 5)	# 100175-100179	 **attackbox here**
    sprite('Action_050_14', 5)	# 100180-100184	 **attackbox here**
    sprite('Action_050_15', 4)	# 100185-100188	 **attackbox here**
    sprite('Action_050_16', 4)	# 100189-100192	 **attackbox here**
    sprite('Action_050_17', 3)	# 100193-100195	 **attackbox here**
    sprite('Action_050_18', 3)	# 100196-100198	 **attackbox here**
    sprite('Action_050_19', 8)	# 100199-100206	 **attackbox here**
    sprite('Action_050_20', 12)	# 100207-100218	 **attackbox here**
    sprite('Action_050_21', 15)	# 100219-100233	 **attackbox here**
    sprite('Action_050_22', 8)	# 100234-100241
    sprite('Action_050_23', 5)	# 100242-100246
    Unknown21011(410)
    label(161)
    sprite('Action_000_00', 7)	# 100247-100253	 **attackbox here**
    sprite('Action_000_01', 7)	# 100254-100260	 **attackbox here**
    sprite('Action_000_02', 8)	# 100261-100268	 **attackbox here**
    sprite('Action_000_03', 8)	# 100269-100276	 **attackbox here**
    sprite('Action_000_04', 10)	# 100277-100286	 **attackbox here**
    sprite('Action_000_05', 9)	# 100287-100295	 **attackbox here**
    sprite('Action_000_06', 11)	# 100296-100306	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_07', 8)	# 100307-100314	 **attackbox here**
    sprite('Action_000_08', 7)	# 100315-100321	 **attackbox here**
    sprite('Action_000_09', 6)	# 100322-100327	 **attackbox here**
    sprite('Action_000_10', 7)	# 100328-100334	 **attackbox here**
    sprite('Action_000_11', 7)	# 100335-100341	 **attackbox here**
    sprite('Action_000_12', 8)	# 100342-100349	 **attackbox here**
    sprite('Action_000_13', 7)	# 100350-100356	 **attackbox here**
    sprite('Action_000_14', 7)	# 100357-100363	 **attackbox here**
    loopRest()
    gotoLabel(161)
    ExitState()
    label(170)
    sprite('Action_050_02', 7)	# 100364-100370
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_03', 5)	# 100371-100375
    SFX_1('uca600ryn')
    sprite('Action_050_04', 5)	# 100376-100380
    sprite('Action_050_05', 5)	# 100381-100385
    sprite('Action_050_06', 3)	# 100386-100388
    sprite('Action_050_07', 7)	# 100389-100395
    sprite('Action_050_08', 10)	# 100396-100405
    sprite('Action_050_09', 11)	# 100406-100416
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 100417-100430
    sprite('Action_050_11', 9)	# 100431-100439	 **attackbox here**
    sprite('Action_050_12', 6)	# 100440-100445	 **attackbox here**
    sprite('Action_050_13', 5)	# 100446-100450	 **attackbox here**
    sprite('Action_050_14', 5)	# 100451-100455	 **attackbox here**
    sprite('Action_050_15', 4)	# 100456-100459	 **attackbox here**
    sprite('Action_050_16', 4)	# 100460-100463	 **attackbox here**
    sprite('Action_050_17', 3)	# 100464-100466	 **attackbox here**
    sprite('Action_050_18', 3)	# 100467-100469	 **attackbox here**
    sprite('Action_050_19', 8)	# 100470-100477	 **attackbox here**
    sprite('Action_050_20', 12)	# 100478-100489	 **attackbox here**
    sprite('Action_050_21', 15)	# 100490-100504	 **attackbox here**
    sprite('Action_050_22', 8)	# 100505-100512
    sprite('Action_050_23', 5)	# 100513-100517
    Unknown21011(410)
    label(171)
    sprite('Action_000_00', 7)	# 100518-100524	 **attackbox here**
    sprite('Action_000_01', 7)	# 100525-100531	 **attackbox here**
    sprite('Action_000_02', 8)	# 100532-100539	 **attackbox here**
    sprite('Action_000_03', 8)	# 100540-100547	 **attackbox here**
    sprite('Action_000_04', 10)	# 100548-100557	 **attackbox here**
    sprite('Action_000_05', 9)	# 100558-100566	 **attackbox here**
    sprite('Action_000_06', 11)	# 100567-100577	 **attackbox here**
    sprite('Action_000_07', 8)	# 100578-100585	 **attackbox here**
    sprite('Action_000_08', 7)	# 100586-100592	 **attackbox here**
    sprite('Action_000_09', 6)	# 100593-100598	 **attackbox here**
    sprite('Action_000_10', 7)	# 100599-100605	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_11', 7)	# 100606-100612	 **attackbox here**
    sprite('Action_000_12', 8)	# 100613-100620	 **attackbox here**
    sprite('Action_000_13', 7)	# 100621-100627	 **attackbox here**
    sprite('Action_000_14', 7)	# 100628-100634	 **attackbox here**
    loopRest()
    gotoLabel(171)
    ExitState()
    label(180)
    sprite('Action_050_02', 7)	# 100635-100641
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_050_03', 5)	# 100642-100646
    SFX_1('uca600bph')
    sprite('Action_050_04', 5)	# 100647-100651
    sprite('Action_050_05', 5)	# 100652-100656
    sprite('Action_050_06', 3)	# 100657-100659
    sprite('Action_050_07', 7)	# 100660-100666
    sprite('Action_050_08', 10)	# 100667-100676
    sprite('Action_050_09', 11)	# 100677-100687
    SFX_3('SE239_Concentration_In')
    sprite('Action_050_10', 14)	# 100688-100701
    sprite('Action_050_11', 9)	# 100702-100710	 **attackbox here**
    sprite('Action_050_12', 6)	# 100711-100716	 **attackbox here**
    sprite('Action_050_13', 5)	# 100717-100721	 **attackbox here**
    sprite('Action_050_14', 5)	# 100722-100726	 **attackbox here**
    sprite('Action_050_15', 4)	# 100727-100730	 **attackbox here**
    sprite('Action_050_16', 4)	# 100731-100734	 **attackbox here**
    sprite('Action_050_17', 3)	# 100735-100737	 **attackbox here**
    sprite('Action_050_18', 3)	# 100738-100740	 **attackbox here**
    sprite('Action_050_19', 8)	# 100741-100748	 **attackbox here**
    sprite('Action_050_20', 12)	# 100749-100760	 **attackbox here**
    sprite('Action_050_21', 15)	# 100761-100775	 **attackbox here**
    sprite('Action_050_22', 8)	# 100776-100783
    sprite('Action_050_23', 5)	# 100784-100788
    Unknown2037(1)
    Unknown21011(410)
    label(181)
    sprite('Action_000_00', 7)	# 100789-100795	 **attackbox here**
    sprite('Action_000_01', 7)	# 100796-100802	 **attackbox here**
    sprite('Action_000_02', 8)	# 100803-100810	 **attackbox here**
    sprite('Action_000_03', 8)	# 100811-100818	 **attackbox here**
    sprite('Action_000_04', 10)	# 100819-100828	 **attackbox here**
    sprite('Action_000_05', 9)	# 100829-100837	 **attackbox here**
    sprite('Action_000_06', 11)	# 100838-100848	 **attackbox here**
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('Action_000_07', 8)	# 100849-100856	 **attackbox here**
    sprite('Action_000_08', 7)	# 100857-100863	 **attackbox here**
    sprite('Action_000_09', 6)	# 100864-100869	 **attackbox here**
    sprite('Action_000_10', 7)	# 100870-100876	 **attackbox here**
    sprite('Action_000_11', 7)	# 100877-100883	 **attackbox here**
    sprite('Action_000_12', 8)	# 100884-100891	 **attackbox here**
    sprite('Action_000_13', 7)	# 100892-100898	 **attackbox here**
    sprite('Action_000_14', 7)	# 100899-100905	 **attackbox here**
    Unknown2038(-1)
    loopRest()
    gotoLabel(181)
    ExitState()
    label(190)
    sprite('Action_248_00', 5)	# 100906-100910
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_248_01', 3)	# 100911-100913
    sprite('Action_248_07', 5)	# 100914-100918
    sprite('Action_248_08', 5)	# 100919-100923
    sprite('Action_248_09', 30)	# 100924-100953
    sprite('Action_248_10', 1)	# 100954-100954	 **attackbox here**
    SFX_1('uca600pak')
    label(191)
    sprite('Action_248_10', 1)	# 100955-100955	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_248_10', 35)	# 100956-100990	 **attackbox here**
    sprite('Action_248_10', 32767)	# 100991-133757	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    ExitState()
    label(200)
    sprite('Action_000_00', 1)	# 133758-133758	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 7)	# 133759-133765	 **attackbox here**
    sprite('Action_000_01', 7)	# 133766-133772	 **attackbox here**
    sprite('Action_000_02', 8)	# 133773-133780	 **attackbox here**
    sprite('Action_000_03', 8)	# 133781-133788	 **attackbox here**
    sprite('Action_000_04', 10)	# 133789-133798	 **attackbox here**
    sprite('Action_000_05', 9)	# 133799-133807	 **attackbox here**
    sprite('Action_000_06', 11)	# 133808-133818	 **attackbox here**
    sprite('Action_000_07', 8)	# 133819-133826	 **attackbox here**
    sprite('Action_000_08', 7)	# 133827-133833	 **attackbox here**
    sprite('Action_000_09', 6)	# 133834-133839	 **attackbox here**
    sprite('Action_000_10', 7)	# 133840-133846	 **attackbox here**
    sprite('Action_000_11', 7)	# 133847-133853	 **attackbox here**
    sprite('Action_000_12', 8)	# 133854-133861	 **attackbox here**
    sprite('Action_000_13', 7)	# 133862-133868	 **attackbox here**
    sprite('Action_000_14', 7)	# 133869-133875	 **attackbox here**
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('Action_000_16', 6)	# 133876-133881
    sprite('Action_000_17', 7)	# 133882-133888
    SFX_1('uca601ume')
    sprite('Action_000_18', 4)	# 133889-133892
    sprite('Action_000_19', 5)	# 133893-133897
    sprite('Action_000_20', 9)	# 133898-133906
    sprite('Action_000_21', 7)	# 133907-133913
    sprite('Action_000_22', 4)	# 133914-133917
    sprite('Car643_00', 7)	# 133918-133924
    sprite('Car643_01', 7)	# 133925-133931
    sprite('Car643_02', 32767)	# 133932-166698	 **attackbox here**
    Unknown23018(1)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 166699-166699	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 7)	# 166700-166706	 **attackbox here**
    sprite('Action_000_01', 7)	# 166707-166713	 **attackbox here**
    sprite('Action_000_02', 8)	# 166714-166721	 **attackbox here**
    sprite('Action_000_03', 8)	# 166722-166729	 **attackbox here**
    sprite('Action_000_04', 10)	# 166730-166739	 **attackbox here**
    sprite('Action_000_05', 9)	# 166740-166748	 **attackbox here**
    sprite('Action_000_06', 11)	# 166749-166759	 **attackbox here**
    sprite('Action_000_07', 8)	# 166760-166767	 **attackbox here**
    sprite('Action_000_08', 7)	# 166768-166774	 **attackbox here**
    sprite('Action_000_09', 6)	# 166775-166780	 **attackbox here**
    sprite('Action_000_10', 7)	# 166781-166787	 **attackbox here**
    sprite('Action_000_11', 7)	# 166788-166794	 **attackbox here**
    sprite('Action_000_12', 8)	# 166795-166802	 **attackbox here**
    sprite('Action_000_13', 7)	# 166803-166809	 **attackbox here**
    sprite('Action_000_14', 7)	# 166810-166816	 **attackbox here**
    loopRest()
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 166817-166818

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
    label(994)
    sprite('Action_046_01', 2)	# 166819-166820
    sprite('Action_046_02', 1)	# 166821-166821
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 166822-166824
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
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('bph'):
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
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('Action_052_00', 2)	# 4-5
    sprite('Action_052_01', 6)	# 6-11
    sprite('Action_052_02', 7)	# 12-18
    sprite('Action_052_03', 4)	# 19-22
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uca524', 100, 895574901, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uca402_0', 100, 878797685, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uca520', 100, 895574901, 12594, 0, 0, 100, 895574901, 12850, 0, 0, 100, 895574901, 13106, 0, 0, 100)
    sprite('Action_052_04', 5)	# 23-27
    sprite('Action_052_05', 9)	# 28-36
    sprite('Action_052_06', 15)	# 37-51
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 52-55
    sprite('Action_052_08', 4)	# 56-59
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    Unknown23018(1)
    label(1)
    sprite('Action_052_09', 4)	# 60-63
    sprite('Action_052_10', 4)	# 64-67
    gotoLabel(1)
    label(10)
    sprite('Action_053_00', 5)	# 68-72
    sprite('Action_053_01', 2)	# 73-74
    sprite('Action_053_02', 4)	# 75-78
    sprite('Action_053_03', 2)	# 79-80
    sprite('Action_053_04', 5)	# 81-85
    sprite('Action_053_05', 2)	# 86-87
    sprite('Action_053_06', 4)	# 88-91
    sprite('Action_053_07', 2)	# 92-93
    sprite('Action_053_08', 4)	# 94-97
    sprite('Action_053_09', 2)	# 98-99
    sprite('Action_053_10', 5)	# 100-104
    sprite('Action_053_11', 2)	# 105-106
    sprite('Action_053_12', 4)	# 107-110
    sprite('Action_053_13', 2)	# 111-112
    sprite('Action_053_14', 5)	# 113-117
    sprite('Action_053_15', 2)	# 118-119
    sprite('Action_053_16', 4)	# 120-123
    sprite('Action_053_17', 2)	# 124-125
    sprite('Action_053_18', 4)	# 126-129
    sprite('Action_053_19', 2)	# 130-131
    sprite('Action_053_20', 5)	# 132-136
    sprite('Action_053_21', 2)	# 137-138
    sprite('Action_053_22', 4)	# 139-142
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uca524', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uca402_0', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uca524', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_053_23', 2)	# 143-144
    sprite('Action_053_24', 5)	# 145-149
    sprite('Action_053_25', 2)	# 150-151
    sprite('Action_053_26', 4)	# 152-155
    sprite('Action_053_27', 2)	# 156-157
    sprite('Action_053_28', 5)	# 158-162
    sprite('Action_053_29', 6)	# 163-168
    Unknown23018(1)
    label(11)
    sprite('Action_053_30', 4)	# 169-172
    sprite('Action_053_31', 2)	# 173-174
    sprite('Action_053_32', 4)	# 175-178
    sprite('Action_053_33', 2)	# 179-180
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('Action_052_00', 2)	# 181-182
    sprite('Action_052_01', 6)	# 183-188
    sprite('Action_052_02', 7)	# 189-195
    sprite('Action_052_03', 4)	# 196-199
    SFX_1('uca700bhz')
    sprite('Action_052_04', 5)	# 200-204
    sprite('Action_052_05', 9)	# 205-213
    sprite('Action_052_06', 15)	# 214-228
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 229-232
    sprite('Action_052_08', 4)	# 233-236
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    label(101)
    sprite('Action_052_09', 4)	# 237-240
    sprite('Action_052_10', 4)	# 241-244
    loopRest()
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_052_09', 4)	# 245-248
    sprite('Action_052_10', 4)	# 249-252
    sprite('Action_052_09', 4)	# 253-256
    sprite('Action_052_10', 4)	# 257-260
    sprite('Action_052_09', 4)	# 261-264
    sprite('Action_052_10', 4)	# 265-268
    sprite('Action_052_09', 4)	# 269-272
    sprite('Action_052_10', 4)	# 273-276
    Unknown21007(24, 40)
    Unknown21011(360)
    label(102)
    sprite('Action_052_09', 4)	# 277-280
    sprite('Action_052_10', 4)	# 281-284
    loopRest()
    gotoLabel(102)
    label(110)
    sprite('Action_000_00', 1)	# 285-285	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 7)	# 286-292	 **attackbox here**
    sprite('Action_000_01', 7)	# 293-299	 **attackbox here**
    sprite('Action_000_02', 8)	# 300-307	 **attackbox here**
    sprite('Action_000_03', 8)	# 308-315	 **attackbox here**
    sprite('Action_000_04', 10)	# 316-325	 **attackbox here**
    sprite('Action_000_05', 9)	# 326-334	 **attackbox here**
    sprite('Action_000_06', 11)	# 335-345	 **attackbox here**
    sprite('Action_000_07', 8)	# 346-353	 **attackbox here**
    sprite('Action_000_08', 7)	# 354-360	 **attackbox here**
    sprite('Action_000_09', 6)	# 361-366	 **attackbox here**
    sprite('Action_000_10', 7)	# 367-373	 **attackbox here**
    sprite('Action_000_11', 7)	# 374-380	 **attackbox here**
    sprite('Action_000_12', 8)	# 381-388	 **attackbox here**
    sprite('Action_000_13', 7)	# 389-395	 **attackbox here**
    sprite('Action_000_14', 7)	# 396-402	 **attackbox here**
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('Action_052_00', 2)	# 403-404
    sprite('Action_052_01', 6)	# 405-410
    sprite('Action_052_02', 7)	# 411-417
    sprite('Action_052_03', 4)	# 418-421
    SFX_1('uca701bmk')
    sprite('Action_052_04', 5)	# 422-426
    sprite('Action_052_05', 9)	# 427-435
    sprite('Action_052_06', 15)	# 436-450
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 451-454
    sprite('Action_052_08', 4)	# 455-458
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    Unknown23018(1)
    label(113)
    sprite('Action_052_09', 4)	# 459-462
    sprite('Action_052_10', 4)	# 463-466
    gotoLabel(113)
    label(120)
    sprite('Action_053_00', 5)	# 467-471
    Unknown2034(0)
    Unknown2053(0)
    sprite('Action_053_01', 2)	# 472-473
    sprite('Action_053_02', 4)	# 474-477
    sprite('Action_053_03', 2)	# 478-479
    sprite('Action_053_04', 5)	# 480-484
    sprite('Action_053_05', 2)	# 485-486
    sprite('Action_053_06', 4)	# 487-490
    sprite('Action_053_07', 2)	# 491-492
    sprite('Action_053_08', 4)	# 493-496
    sprite('Action_053_09', 2)	# 497-498
    sprite('Action_053_10', 5)	# 499-503
    sprite('Action_053_11', 2)	# 504-505
    sprite('Action_053_12', 4)	# 506-509
    sprite('Action_053_13', 2)	# 510-511
    sprite('Action_053_14', 5)	# 512-516
    sprite('Action_053_15', 2)	# 517-518
    sprite('Action_053_16', 4)	# 519-522
    sprite('Action_053_17', 2)	# 523-524
    sprite('Action_053_18', 4)	# 525-528
    sprite('Action_053_19', 2)	# 529-530
    sprite('Action_053_20', 5)	# 531-535
    sprite('Action_053_21', 2)	# 536-537
    sprite('Action_053_22', 4)	# 538-541
    SFX_1('uca700baz')
    sprite('Action_053_23', 2)	# 542-543
    sprite('Action_053_24', 5)	# 544-548
    sprite('Action_053_25', 2)	# 549-550
    sprite('Action_053_26', 4)	# 551-554
    sprite('Action_053_27', 2)	# 555-556
    sprite('Action_053_28', 5)	# 557-561
    sprite('Action_053_29', 6)	# 562-567
    label(121)
    sprite('Action_053_30', 4)	# 568-571
    sprite('Action_053_31', 2)	# 572-573
    sprite('Action_053_32', 4)	# 574-577
    sprite('Action_053_33', 2)	# 578-579
    loopRest()
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_053_30', 1)	# 580-580
    Unknown21007(24, 40)
    Unknown21011(420)
    label(122)
    sprite('Action_053_30', 4)	# 581-584
    sprite('Action_053_31', 2)	# 585-586
    sprite('Action_053_32', 4)	# 587-590
    sprite('Action_053_33', 2)	# 591-592
    loopRest()
    gotoLabel(122)
    label(130)
    sprite('Action_000_00', 1)	# 593-593	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('Action_000_00', 7)	# 594-600	 **attackbox here**
    sprite('Action_000_01', 7)	# 601-607	 **attackbox here**
    sprite('Action_000_02', 8)	# 608-615	 **attackbox here**
    sprite('Action_000_03', 8)	# 616-623	 **attackbox here**
    sprite('Action_000_04', 10)	# 624-633	 **attackbox here**
    sprite('Action_000_05', 9)	# 634-642	 **attackbox here**
    sprite('Action_000_06', 11)	# 643-653	 **attackbox here**
    sprite('Action_000_07', 8)	# 654-661	 **attackbox here**
    sprite('Action_000_08', 7)	# 662-668	 **attackbox here**
    sprite('Action_000_09', 6)	# 669-674	 **attackbox here**
    sprite('Action_000_10', 7)	# 675-681	 **attackbox here**
    sprite('Action_000_11', 7)	# 682-688	 **attackbox here**
    sprite('Action_000_12', 8)	# 689-696	 **attackbox here**
    sprite('Action_000_13', 7)	# 697-703	 **attackbox here**
    sprite('Action_000_14', 7)	# 704-710	 **attackbox here**
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('Action_052_00', 2)	# 711-712
    sprite('Action_052_01', 6)	# 713-718
    sprite('Action_052_02', 7)	# 719-725
    sprite('Action_052_03', 4)	# 726-729
    SFX_1('uca701pyu')
    sprite('Action_052_04', 5)	# 730-734
    sprite('Action_052_05', 9)	# 735-743
    sprite('Action_052_06', 15)	# 744-758
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 759-762
    sprite('Action_052_08', 4)	# 763-766
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    Unknown23018(1)
    label(133)
    sprite('Action_052_09', 4)	# 767-770
    sprite('Action_052_10', 4)	# 771-774
    gotoLabel(133)
    label(140)
    sprite('Action_000_00', 1)	# 775-775	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('Action_000_00', 7)	# 776-782	 **attackbox here**
    sprite('Action_000_01', 7)	# 783-789	 **attackbox here**
    sprite('Action_000_02', 8)	# 790-797	 **attackbox here**
    sprite('Action_000_03', 8)	# 798-805	 **attackbox here**
    sprite('Action_000_04', 10)	# 806-815	 **attackbox here**
    sprite('Action_000_05', 9)	# 816-824	 **attackbox here**
    sprite('Action_000_06', 11)	# 825-835	 **attackbox here**
    sprite('Action_000_07', 8)	# 836-843	 **attackbox here**
    sprite('Action_000_08', 7)	# 844-850	 **attackbox here**
    sprite('Action_000_09', 6)	# 851-856	 **attackbox here**
    sprite('Action_000_10', 7)	# 857-863	 **attackbox here**
    sprite('Action_000_11', 7)	# 864-870	 **attackbox here**
    sprite('Action_000_12', 8)	# 871-878	 **attackbox here**
    sprite('Action_000_13', 7)	# 879-885	 **attackbox here**
    sprite('Action_000_14', 7)	# 886-892	 **attackbox here**
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('Action_052_00', 2)	# 893-894
    sprite('Action_052_01', 6)	# 895-900
    sprite('Action_052_02', 7)	# 901-907
    sprite('Action_052_03', 4)	# 908-911
    SFX_1('uca701pka')
    sprite('Action_052_04', 5)	# 912-916
    sprite('Action_052_05', 9)	# 917-925
    sprite('Action_052_06', 15)	# 926-940
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 941-944
    sprite('Action_052_08', 4)	# 945-948
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    Unknown23018(1)
    label(143)
    sprite('Action_052_09', 4)	# 949-952
    sprite('Action_052_10', 4)	# 953-956
    gotoLabel(143)
    label(150)
    sprite('Action_000_00', 1)	# 957-957	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Action_000_00', 7)	# 958-964	 **attackbox here**
    sprite('Action_000_01', 7)	# 965-971	 **attackbox here**
    sprite('Action_000_02', 8)	# 972-979	 **attackbox here**
    sprite('Action_000_03', 8)	# 980-987	 **attackbox here**
    sprite('Action_000_04', 10)	# 988-997	 **attackbox here**
    sprite('Action_000_05', 9)	# 998-1006	 **attackbox here**
    sprite('Action_000_06', 11)	# 1007-1017	 **attackbox here**
    sprite('Action_000_07', 8)	# 1018-1025	 **attackbox here**
    sprite('Action_000_08', 7)	# 1026-1032	 **attackbox here**
    sprite('Action_000_09', 6)	# 1033-1038	 **attackbox here**
    sprite('Action_000_10', 7)	# 1039-1045	 **attackbox here**
    sprite('Action_000_11', 7)	# 1046-1052	 **attackbox here**
    sprite('Action_000_12', 8)	# 1053-1060	 **attackbox here**
    sprite('Action_000_13', 7)	# 1061-1067	 **attackbox here**
    sprite('Action_000_14', 7)	# 1068-1074	 **attackbox here**
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('Action_052_00', 2)	# 1075-1076
    sprite('Action_052_01', 6)	# 1077-1082
    sprite('Action_052_02', 7)	# 1083-1089
    sprite('Action_052_03', 4)	# 1090-1093
    SFX_1('uca701ugo')
    sprite('Action_052_04', 5)	# 1094-1098
    sprite('Action_052_05', 9)	# 1099-1107
    sprite('Action_052_06', 15)	# 1108-1122
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 1123-1126
    sprite('Action_052_08', 4)	# 1127-1130
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    Unknown23018(1)
    label(153)
    sprite('Action_052_09', 4)	# 1131-1134
    sprite('Action_052_10', 4)	# 1135-1138
    gotoLabel(153)
    label(160)
    sprite('Action_000_00', 1)	# 1139-1139	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 7)	# 1140-1146	 **attackbox here**
    sprite('Action_000_01', 7)	# 1147-1153	 **attackbox here**
    sprite('Action_000_02', 8)	# 1154-1161	 **attackbox here**
    sprite('Action_000_03', 8)	# 1162-1169	 **attackbox here**
    sprite('Action_000_04', 10)	# 1170-1179	 **attackbox here**
    sprite('Action_000_05', 9)	# 1180-1188	 **attackbox here**
    sprite('Action_000_06', 11)	# 1189-1199	 **attackbox here**
    sprite('Action_000_07', 8)	# 1200-1207	 **attackbox here**
    sprite('Action_000_08', 7)	# 1208-1214	 **attackbox here**
    sprite('Action_000_09', 6)	# 1215-1220	 **attackbox here**
    sprite('Action_000_10', 7)	# 1221-1227	 **attackbox here**
    sprite('Action_000_11', 7)	# 1228-1234	 **attackbox here**
    sprite('Action_000_12', 8)	# 1235-1242	 **attackbox here**
    sprite('Action_000_13', 7)	# 1243-1249	 **attackbox here**
    sprite('Action_000_14', 7)	# 1250-1256	 **attackbox here**
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('Action_053_00', 5)	# 1257-1261
    sprite('Action_053_01', 2)	# 1262-1263
    sprite('Action_053_02', 4)	# 1264-1267
    sprite('Action_053_03', 2)	# 1268-1269
    sprite('Action_053_04', 5)	# 1270-1274
    sprite('Action_053_05', 2)	# 1275-1276
    sprite('Action_053_06', 4)	# 1277-1280
    sprite('Action_053_07', 2)	# 1281-1282
    sprite('Action_053_08', 4)	# 1283-1286
    sprite('Action_053_09', 2)	# 1287-1288
    sprite('Action_053_10', 5)	# 1289-1293
    sprite('Action_053_11', 2)	# 1294-1295
    sprite('Action_053_12', 4)	# 1296-1299
    sprite('Action_053_13', 2)	# 1300-1301
    sprite('Action_053_14', 5)	# 1302-1306
    sprite('Action_053_15', 2)	# 1307-1308
    sprite('Action_053_16', 4)	# 1309-1312
    sprite('Action_053_17', 2)	# 1313-1314
    sprite('Action_053_18', 4)	# 1315-1318
    sprite('Action_053_19', 2)	# 1319-1320
    sprite('Action_053_20', 5)	# 1321-1325
    sprite('Action_053_21', 2)	# 1326-1327
    sprite('Action_053_22', 4)	# 1328-1331
    SFX_1('uca701uwa')
    sprite('Action_053_23', 2)	# 1332-1333
    sprite('Action_053_24', 5)	# 1334-1338
    sprite('Action_053_25', 2)	# 1339-1340
    sprite('Action_053_26', 4)	# 1341-1344
    sprite('Action_053_27', 2)	# 1345-1346
    sprite('Action_053_28', 5)	# 1347-1351
    sprite('Action_053_29', 6)	# 1352-1357
    Unknown23018(1)
    label(163)
    sprite('Action_053_30', 4)	# 1358-1361
    sprite('Action_053_31', 2)	# 1362-1363
    sprite('Action_053_32', 4)	# 1364-1367
    sprite('Action_053_33', 2)	# 1368-1369
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('Action_000_00', 1)	# 1370-1370	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_00', 7)	# 1371-1377	 **attackbox here**
    sprite('Action_000_01', 7)	# 1378-1384	 **attackbox here**
    sprite('Action_000_02', 8)	# 1385-1392	 **attackbox here**
    sprite('Action_000_03', 8)	# 1393-1400	 **attackbox here**
    sprite('Action_000_04', 10)	# 1401-1410	 **attackbox here**
    sprite('Action_000_05', 9)	# 1411-1419	 **attackbox here**
    sprite('Action_000_06', 11)	# 1420-1430	 **attackbox here**
    sprite('Action_000_07', 8)	# 1431-1438	 **attackbox here**
    sprite('Action_000_08', 7)	# 1439-1445	 **attackbox here**
    sprite('Action_000_09', 6)	# 1446-1451	 **attackbox here**
    sprite('Action_000_10', 7)	# 1452-1458	 **attackbox here**
    sprite('Action_000_11', 7)	# 1459-1465	 **attackbox here**
    sprite('Action_000_12', 8)	# 1466-1473	 **attackbox here**
    sprite('Action_000_13', 7)	# 1474-1480	 **attackbox here**
    sprite('Action_000_14', 7)	# 1481-1487	 **attackbox here**
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('Action_052_00', 2)	# 1488-1489
    sprite('Action_052_01', 6)	# 1490-1495
    sprite('Action_052_02', 7)	# 1496-1502
    sprite('Action_052_03', 4)	# 1503-1506
    SFX_1('uca701ryn')
    sprite('Action_052_04', 5)	# 1507-1511
    sprite('Action_052_05', 9)	# 1512-1520
    sprite('Action_052_06', 15)	# 1521-1535
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 1536-1539
    sprite('Action_052_08', 4)	# 1540-1543
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    Unknown23018(1)
    label(173)
    sprite('Action_052_09', 4)	# 1544-1547
    sprite('Action_052_10', 4)	# 1548-1551
    gotoLabel(173)
    label(180)
    sprite('Action_000_00', 1)	# 1552-1552	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('Action_000_00', 7)	# 1553-1559	 **attackbox here**
    sprite('Action_000_01', 7)	# 1560-1566	 **attackbox here**
    sprite('Action_000_02', 8)	# 1567-1574	 **attackbox here**
    sprite('Action_000_03', 8)	# 1575-1582	 **attackbox here**
    sprite('Action_000_04', 10)	# 1583-1592	 **attackbox here**
    sprite('Action_000_05', 9)	# 1593-1601	 **attackbox here**
    sprite('Action_000_06', 11)	# 1602-1612	 **attackbox here**
    sprite('Action_000_07', 8)	# 1613-1620	 **attackbox here**
    sprite('Action_000_08', 7)	# 1621-1627	 **attackbox here**
    sprite('Action_000_09', 6)	# 1628-1633	 **attackbox here**
    sprite('Action_000_10', 7)	# 1634-1640	 **attackbox here**
    sprite('Action_000_11', 7)	# 1641-1647	 **attackbox here**
    sprite('Action_000_12', 8)	# 1648-1655	 **attackbox here**
    sprite('Action_000_13', 7)	# 1656-1662	 **attackbox here**
    sprite('Action_000_14', 7)	# 1663-1669	 **attackbox here**
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('Action_248_00', 5)	# 1670-1674
    SFX_1('uca701bph')
    sprite('Action_248_01', 3)	# 1675-1677
    sprite('Action_248_07', 5)	# 1678-1682
    sprite('Action_248_08', 5)	# 1683-1687
    sprite('Action_248_09', 30)	# 1688-1717
    Unknown23018(1)
    sprite('Action_248_10', 32767)	# 1718-34484	 **attackbox here**
    label(190)
    sprite('Action_052_00', 2)	# 34485-34486
    sprite('Action_052_01', 6)	# 34487-34492
    sprite('Action_052_02', 7)	# 34493-34499
    sprite('Action_052_03', 4)	# 34500-34503
    SFX_1('uca700pak')
    sprite('Action_052_04', 5)	# 34504-34508
    sprite('Action_052_05', 9)	# 34509-34517
    sprite('Action_052_06', 15)	# 34518-34532
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 34533-34536
    sprite('Action_052_08', 4)	# 34537-34540
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    label(191)
    sprite('Action_052_09', 4)	# 34541-34544
    sprite('Action_052_10', 4)	# 34545-34548
    loopRest()
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_052_09', 4)	# 34549-34552
    sprite('Action_052_10', 4)	# 34553-34556
    sprite('Action_052_09', 4)	# 34557-34560
    sprite('Action_052_10', 4)	# 34561-34564
    Unknown21007(24, 40)
    Unknown21011(180)
    label(192)
    sprite('Action_052_09', 4)	# 34565-34568
    sprite('Action_052_10', 4)	# 34569-34572
    loopRest()
    gotoLabel(192)
    label(200)
    sprite('Action_052_00', 2)	# 34573-34574
    sprite('Action_052_01', 6)	# 34575-34580
    sprite('Action_052_02', 7)	# 34581-34587
    sprite('Action_052_03', 4)	# 34588-34591
    SFX_1('uca700ume')
    sprite('Action_052_04', 5)	# 34592-34596
    sprite('Action_052_05', 9)	# 34597-34605
    sprite('Action_052_06', 15)	# 34606-34620
    SFX_3('SE008')
    GFX_0('Win1', -1)
    sprite('Action_052_07', 4)	# 34621-34624
    sprite('Action_052_08', 4)	# 34625-34628
    SFX_3('SE051')
    GFX_0('Win2', -1)
    ScreenShake(10000, 10000)
    label(201)
    sprite('Action_052_09', 4)	# 34629-34632
    sprite('Action_052_10', 4)	# 34633-34636
    loopRest()
    if SLOT_97:
        _gotolabel(201)
    sprite('Action_052_09', 1)	# 34637-34637
    Unknown21007(24, 40)
    Unknown21011(210)
    label(202)
    sprite('Action_052_09', 4)	# 34638-34641
    sprite('Action_052_10', 4)	# 34642-34645
    loopRest()
    gotoLabel(202)

@State
def CmnActLose():
    sprite('Action_248_00', 5)	# 1-5
    sprite('Action_248_01', 3)	# 6-8
    sprite('Action_248_02', 13)	# 9-21
    if SLOT_158:
        Unknown7006('uca403_0', 100, 878797685, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_248_03', 20)	# 22-41
    sprite('Action_248_04', 11)	# 42-52
    sprite('Action_248_05', 9)	# 53-61
    sprite('Action_248_06', 6)	# 62-67
    sprite('Action_248_07', 5)	# 68-72
    sprite('Action_248_08', 5)	# 73-77
    sprite('Action_248_09', 30)	# 78-107
    sprite('Action_248_10', 32767)	# 108-32874	 **attackbox here**
    Unknown23018(1)