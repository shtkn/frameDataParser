@Subroutine
def PreInit():
    Unknown12019('75676f00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(18000)
    Unknown12038(23000)
    Unknown12034(33)
    Unknown12036(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
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
    Unknown14015(0, 250000, -120000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    Unknown14005(1)
    Unknown14015(50000, 300000, -120000, 200000, 2000, 0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    Unknown14005(1)
    Unknown14015(50000, 600000, -120000, 200000, 2000, 0)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    Unknown14005(1)
    Unknown14015(50000, 800000, -120000, 320000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 250000, -200000, 150000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown14015(0, 250000, -200000, 150000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14015(250000, 800000, -120000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 800000, -120000, 200000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 800000, -120000, 200000, 2000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown14015(0, 500000, -200000, 650000, 1500, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 500000, -200000, 150000, 500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown14015(0, 500000, -200000, 50000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 400000, -250000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 250000, -200000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 650000, -200000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 150000, 200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown14015(0, 500000, -200000, 150000, 200, 0)
    Move_EndRegister()
    Move_Register('AssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-50000, 800000, -100000, 350000, 400, 5)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-50000, 800000, -100000, 350000, 400, 5)
    Move_EndRegister()
    Move_Register('DrainA_LandThrow', INPUT_SPECIALMOVE)
    Unknown14027('NmlAtk5B_3rd')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15010()
    Unknown15021(1)
    Unknown14015(-50000, 180000, -100000, 200000, 400, 0)
    Move_EndRegister()
    Move_Register('DrainB_AirThrow', INPUT_SPECIALMOVE)
    Unknown14027('NmlAtk5B_3rd')
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(2500)
    Unknown14015(-50000, 250000, 100000, 300000, 400, 0)
    Move_EndRegister()
    Move_Register('AssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(-50000, 800000, -100000, 350000, 300, 0)
    Move_EndRegister()
    Move_Register('DrainEx', INPUT_SPECIALMOVE)
    Unknown14027('NmlAtk5B_3rd')
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15010()
    Unknown15021(1)
    Unknown14015(0, 380000, -100000, 200000, 400, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(6000)
    Unknown14015(-50000, 300000, -100000, 350000, 200, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15014(6000)
    Unknown14015(-50000, 300000, -100000, 350000, 200, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15014(2000)
    Unknown14015(0, 300000, -100000, 300000, 800, 30)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15014(2000)
    Unknown14015(0, 300000, -100000, 300000, 800, 30)
    Move_EndRegister()
    Move_Register('UltimateRanged', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(1)
    Unknown15014(2000)
    Unknown15013(3000)
    Unknown14015(0, 650000, -100000, 150000, 800, 50)
    Move_EndRegister()
    Move_Register('UltimateRangedOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15021(1)
    Unknown15014(2000)
    Unknown15013(3000)
    Unknown14015(0, 650000, -100000, 150000, 600, 50)
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
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AssaultA', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AssaultB', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AssaultEx', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('NmlAtk5B_2nd_Add', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('NmlAtk5B_2nd_Add', 'AssaultA', 10000000)
    Unknown15024('NmlAtk5B_2nd_Add', 'AssaultB', 10000000)
    Unknown15024('NmlAtk5B_2nd_Add', 'AssaultEx', 10000000)
    Unknown15024('NmlAtk5B_2nd_Add', 'UltimateRanged', 10000000)
    Unknown15024('NmlAtk5B_2nd_Add', 'UltimateRangedOD', 10000000)
    Unknown15024('NmlAtk2B', 'DrainB_AirThrow', 10000000)
    Unknown15024('NmlAtk2C', 'DrainB_AirThrow', 10000000)
    Unknown15024('NmlAtk2C', 'AssaultA', 10000000)
    Unknown15024('NmlAtk2C', 'DrainEx', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssault', 10000000)
    Unknown15024('NmlAtk2C', 'UltimateAssaultOD', 10000000)
    Unknown15024('NmlAtk2C', 'NmlAtkAIR5A', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5C', 'CmnActInvincibleAttackAir', 10000000)
    Unknown12018(0, 'Action_330_00')
    Unknown12018(1, 'Action_330_01')
    Unknown12018(2, 'Action_330_04')
    Unknown12018(3, 'Action_330_05')
    Unknown12018(4, 'Action_330_06')
    Unknown12018(5, 'Action_330_07')
    Unknown12018(6, 'Action_330_08')
    Unknown12018(7, 'Action_017_00')
    Unknown12018(8, 'Action_017_00')
    Unknown12018(9, 'Action_019_00')
    Unknown12018(10, 'Action_330_00')
    Unknown12018(11, 'Action_330_01')
    Unknown12018(12, 'Action_330_05')
    Unknown12018(13, 'Action_330_08')
    Unknown12018(14, 'Action_351_00')
    Unknown12018(15, 'Action_290_00')
    Unknown12018(16, 'Action_300_01')
    Unknown12018(17, 'Action_304_03')
    Unknown12018(18, 'Action_305_03')
    Unknown12018(19, 'Action_000_00')
    Unknown12018(20, 'Action_000_00')
    Unknown12018(25, 'Action_326_00')
    Unknown12018(26, 'Action_326_02')
    Unknown12018(27, 'Action_326_03')
    Unknown12018(28, 'Action_351_05')
    Unknown12018(29, 'Action_292_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'ugo000')
    Unknown7010(1, 'ugo001')
    Unknown7010(2, 'ugo002')
    Unknown7010(3, 'ugo003')
    Unknown7010(4, 'ugo004')
    Unknown7010(5, 'ugo005')
    Unknown7010(6, 'ugo006')
    Unknown7010(7, 'ugo007')
    Unknown7010(8, 'ugo008')
    Unknown7010(9, 'ugo009')
    Unknown7010(10, 'ugo010')
    Unknown7010(11, 'ugo011')
    Unknown7010(12, 'ugo012')
    Unknown7010(13, 'ugo013')
    Unknown7010(14, 'ugo014')
    Unknown7010(15, 'ugo015')
    Unknown7010(16, 'ugo016')
    Unknown7010(17, 'ugo017')
    Unknown7010(18, 'ugo018')
    Unknown7010(19, 'ugo019')
    Unknown7010(20, 'ugo020')
    Unknown7010(21, 'ugo021')
    Unknown7010(22, 'ugo022')
    Unknown7010(23, 'ugo023')
    Unknown7010(24, 'ugo024')
    Unknown7010(25, 'ugo025')
    Unknown7010(26, 'ugo026')
    Unknown7010(27, 'ugo027')
    Unknown7010(28, 'ugo028')
    Unknown7010(29, 'ugo029')
    Unknown7010(30, 'ugo030')
    Unknown7010(31, 'ugo031')
    Unknown7010(32, 'ugo032')
    Unknown7010(33, 'ugo033')
    Unknown7010(34, 'ugo034')
    Unknown7010(35, 'ugo035')
    Unknown7010(36, 'ugo036')
    Unknown7010(37, 'ugo037')
    Unknown7010(38, 'ugo038')
    Unknown7010(39, 'ugo039')
    Unknown7010(40, 'Hyd500')
    Unknown7010(41, 'ugo041')
    Unknown7010(42, 'ugo042')
    Unknown7010(43, 'ugo043')
    Unknown7010(44, 'ugo044')
    Unknown7010(45, 'ugo045')
    Unknown7010(46, 'ugo046')
    Unknown7010(47, 'ugo047')
    Unknown7010(48, 'ugo048')
    Unknown7010(49, 'ugo049')
    Unknown7010(50, 'ugo050')
    Unknown7010(51, 'ugo051')
    Unknown7010(52, 'ugo052')
    Unknown7010(53, 'ugo053')
    Unknown7010(54, 'ugo100_0')
    Unknown7010(55, 'ugo100_1')
    Unknown7010(56, 'ugo100_2')
    Unknown7010(63, 'ugo101_0')
    Unknown7010(64, 'ugo101_1')
    Unknown7010(65, 'ugo101_2')
    Unknown7010(57, 'ugo102_0')
    Unknown7010(58, 'ugo102_1')
    Unknown7010(59, 'ugo102_2')
    Unknown7010(66, 'ugo103_0')
    Unknown7010(67, 'ugo103_1')
    Unknown7010(68, 'ugo103_2')
    Unknown7010(60, 'ugo104_0')
    Unknown7010(61, 'ugo104_1')
    Unknown7010(62, 'ugo104_2')
    Unknown7010(69, 'ugo105_0')
    Unknown7010(70, 'ugo105_1')
    Unknown7010(71, 'ugo105_2')
    Unknown7010(72, 'ugo150')
    Unknown7010(73, 'ugo151')
    Unknown7010(74, 'ugo152')
    Unknown7010(85, 'ugo153')
    Unknown7010(87, 'ugo154')
    Unknown7010(88, 'ugo155')
    Unknown7010(94, 'ugo400')
    Unknown7010(95, 'ugo401')
    Unknown7010(96, 'ugo161_0')
    Unknown7010(97, 'ugo161_1')
    Unknown7010(98, 'ugo163_0')
    Unknown7010(99, 'ugo163_1')
    Unknown7010(100, 'ugo164_0')
    Unknown7010(101, 'ugo164_1')
    Unknown7010(102, 'ugo166_0')
    Unknown7010(103, 'ugo166_1')
    Unknown7010(92, 'ugo162_0')
    Unknown7010(93, 'ugo162_1')
    Unknown7010(90, 'ugo167_0')
    Unknown7010(91, 'ugo167_1')
    Unknown7010(105, 'ugo165_0')
    Unknown7010(106, 'ugo165_1')
    Unknown7010(107, 'ugo168_0')
    Unknown7010(108, 'ugo168_1')
    Unknown7010(110, 'ugo169_0')
    Unknown7010(111, 'ugo169_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746552616e676564000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746552616e6765644f4400000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnLanding():
    SLOT_59 = 0

@State
def CmnActStand():
    label(0)
    sprite('Action_000_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_000_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_000_02', 6)	# 11-16	 **attackbox here**
    sprite('Action_000_03', 7)	# 17-23	 **attackbox here**
    sprite('Action_000_04', 7)	# 24-30	 **attackbox here**
    sprite('Action_000_05', 7)	# 31-37	 **attackbox here**
    sprite('Action_000_06', 7)	# 38-44	 **attackbox here**
    sprite('Action_000_07', 7)	# 45-51	 **attackbox here**
    sprite('Action_000_08', 7)	# 52-58	 **attackbox here**
    sprite('Action_000_09', 7)	# 59-65	 **attackbox here**
    sprite('Action_000_10', 7)	# 66-72	 **attackbox here**
    sprite('Action_000_11', 6)	# 73-78	 **attackbox here**
    sprite('Action_000_12', 5)	# 79-83	 **attackbox here**
    sprite('Action_000_13', 5)	# 84-88	 **attackbox here**
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('Action_000_00', 1)	# 89-89	 **attackbox here**
    SLOT_88 = 960
    SFX_1('ugo000')
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 3)	# 1-3
    sprite('Action_015_01', 3)	# 4-6

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 2)	# 1-2
    sprite('Action_012_01', 4)	# 3-6
    sprite('Action_012_02', 3)	# 7-9

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 7)	# 1-7
    sprite('Action_013_01', 6)	# 8-13
    sprite('Action_013_02', 5)	# 14-18
    sprite('Action_013_03', 4)	# 19-22
    sprite('Action_013_04', 5)	# 23-27
    sprite('Action_013_05', 6)	# 28-33
    sprite('Action_013_06', 6)	# 34-39
    sprite('Action_013_07', 8)	# 40-47
    sprite('Action_013_08', 7)	# 48-54
    sprite('Action_013_09', 7)	# 55-61
    sprite('Action_013_10', 6)	# 62-67
    sprite('Action_013_11', 4)	# 68-71
    sprite('Action_013_12', 5)	# 72-76
    sprite('Action_013_13', 6)	# 77-82
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
    sprite('Action_036_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('Action_036_01', 4)	# 1-4
    sprite('Action_036_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('Action_036_02', 3)	# 1-3
    sprite('Action_036_03', 3)	# 4-6
    sprite('Action_036_04', 2)	# 7-8
    sprite('Action_036_05', 2)	# 9-10

@State
def CmnActJumpDown():
    label(0)
    sprite('Action_022_00', 3)	# 1-3
    sprite('Action_022_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('Action_021_00', 4)	# 1-4
    sprite('Action_021_01', 4)	# 5-8
    sprite('Action_021_02', 4)	# 9-12

@State
def CmnActLandingStiffLoop():
    sprite('Action_021_00', 4)	# 1-4
    sprite('Action_021_01', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('Action_021_02', 4)	# 1-4

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 6)	# 1-6
    sprite('Action_010_01', 6)	# 7-12
    sprite('Action_010_02', 6)	# 13-18
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_03', 6)	# 19-24
    sprite('Action_010_04', 6)	# 25-30
    sprite('Action_010_05', 6)	# 31-36
    sprite('Action_010_06', 6)	# 37-42
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_07', 6)	# 43-48
    sprite('Action_010_08', 6)	# 49-54
    sprite('Action_010_09', 6)	# 55-60
    sprite('Action_010_10', 6)	# 61-66
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_11', 6)	# 67-72
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
    sprite('Action_011_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_08', 7)	# 57-63
    sprite('Action_011_09', 7)	# 64-70
    sprite('Action_011_10', 7)	# 71-77
    sprite('Action_011_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_010_00', 4)	# 1-4
    sprite('Action_045_00', 3)	# 5-7
    sprite('Action_045_01', 2)	# 8-9
    sprite('Action_045_02', 2)	# 10-11
    SFX_0('000_airdash_1')
    label(0)
    sprite('Action_045_03', 3)	# 12-14
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    sprite('Action_045_06', 3)	# 21-23
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_07', 3)	# 24-26
    sprite('Action_045_08', 3)	# 27-29
    sprite('Action_045_09', 3)	# 30-32
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_01', 3)	# 33-35
    sprite('Action_045_02', 3)	# 36-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_10', 4)	# 1-4
    sprite('Action_045_11', 2)	# 5-6

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

        def upon_3():
            Unknown1019(90)
    sprite('Action_046_00', 2)	# 1-2
    sprite('Action_046_01', 4)	# 3-6
    physicsXImpulse(-42000)
    SFX_0('001_airbackdash_0')
    sprite('Action_046_02', 4)	# 7-10
    sprite('Action_046_03', 4)	# 11-14
    sprite('Action_046_04', 4)	# 15-18
    sprite('Action_046_05', 4)	# 19-22
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    Unknown1019(10)

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():

    def upon_IMMEDIATE():
        pass
    sprite('Action_068_01', 3)	# 1-3
    sprite('Action_068_02', 3)	# 4-6
    sprite('Action_068_03', 3)	# 7-9
    sprite('Action_068_02', 3)	# 10-12
    sprite('Action_068_04', 3)	# 13-15
    sprite('Action_068_05', 3)	# 16-18
    sprite('Action_068_06', 3)	# 19-21
    sprite('Action_068_07', 3)	# 22-24
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
    sprite('Action_068_08', 3)	# 1-3
    sprite('Action_068_09', 3)	# 4-6
    sprite('Action_068_10', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirBDash():
    sprite('Action_046_01', 4)	# 1-4
    physicsYImpulse(12000)
    sprite('Action_046_02', 4)	# 5-8
    label(0)
    sprite('Action_046_01', 4)	# 9-12
    sprite('Action_046_02', 4)	# 13-16
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
    sprite('null', 60)	# 1-60

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
    sprite('Action_352_00', 3)	# 1-3
    sprite('Action_352_01', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('Action_354_02', 2)	# 1-2
    sprite('Action_354_03', 3)	# 3-5
    sprite('Action_354_04', 3)	# 6-8
    sprite('Action_352_00', 2)	# 9-10
    sprite('Action_352_01', 2)	# 11-12

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
    sprite('Action_330_06', 2)	# 1-2
    sprite('Action_330_06', 2)	# 3-4
    sprite('Action_330_07', 2)	# 5-6
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
    sprite('Action_032_00', 5)	# 1-5
    sprite('Action_032_01', 5)	# 6-10
    sprite('Action_032_02', 5)	# 11-15
    sprite('Action_032_03', 5)	# 16-20
    sprite('Action_032_04', 3)	# 21-23
    sprite('Action_032_05', 3)	# 24-26

@State
def CmnActUkemiAirB():
    sprite('Action_032_00', 5)	# 1-5
    sprite('Action_032_01', 5)	# 6-10
    sprite('Action_032_02', 5)	# 11-15
    sprite('Action_032_03', 5)	# 16-20
    sprite('Action_032_04', 3)	# 21-23
    sprite('Action_032_05', 3)	# 24-26

@State
def CmnActUkemiAirN():
    sprite('Action_032_00', 5)	# 1-5
    sprite('Action_032_01', 5)	# 6-10
    sprite('Action_032_02', 5)	# 11-15
    sprite('Action_032_03', 5)	# 16-20
    sprite('Action_032_04', 3)	# 21-23
    sprite('Action_032_05', 3)	# 24-26

@State
def CmnActUkemiLandF():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandB():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 3)	# 1-3
    sprite('Action_041_01', 3)	# 4-6
    sprite('Action_041_02', 2)	# 7-8
    sprite('Action_041_03', 2)	# 9-10
    sprite('Action_041_04', 2)	# 11-12
    sprite('Action_041_05', 2)	# 13-14
    sprite('Action_041_06', 2)	# 15-16

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_07', 5)	# 1-5
    sprite('Action_041_08', 5)	# 6-10
    sprite('Action_041_09', 5)	# 11-15

@State
def CmnActMidGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6
    sprite('Action_017_02', 3)	# 7-9
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
    sprite('Action_018_01', 3)	# 7-9
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
    label(0)
    sprite('Action_019_02', 3)	# 1-3
    sprite('Action_019_03', 3)	# 4-6
    sprite('Action_019_01', 3)	# 7-9
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('Action_017_00', 2)	# 1-2
    sprite('Action_017_01', 2)	# 3-4
    sprite('Action_017_01', 1)	# 5-5
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

@State
def CmnActAirTurn():
    sprite('Action_036_01', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_402_00', 3)	# 1-3
    sprite('Action_402_01', 3)	# 4-6
    sprite('Action_402_02', 3)	# 7-9
    sprite('Action_402_03', 3)	# 10-12
    sprite('Action_402_04', 6)	# 13-18	 **attackbox here**
    SFX_3('SE045')
    sprite('Action_402_05', 5)	# 19-23
    sprite('Action_402_06', 4)	# 24-27

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1
    sprite('Action_019_03', 3)	# 2-4
    sprite('Action_019_00', 3)	# 5-7

@State
def CmnActLandSpin():
    sprite('null', 60)	# 1-60

@State
def CmnActLandSpinDown():
    sprite('null', 60)	# 1-60

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
    sprite('null', 60)	# 1-60

@State
def CmnActAomukeSlideEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771

@State
def CmnActBurstLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('Action_262_05', 6)	# 1-6
    sprite('Action_262_06', 6)	# 7-12

@State
def CmnActAirBurstBegin():
    sprite('Action_262_00', 4)	# 1-4
    Unknown23119(16639, 20, 1)
    sprite('Action_262_01', 32767)	# 5-32771

@State
def CmnActAirBurstLoop():
    sprite('Action_262_02', 4)	# 1-4
    Unknown23118(16534)
    Unknown23119(0, 20, 1)
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
    sprite('Action_022_00', 3)	# 13-15
    sprite('Action_022_01', 3)	# 16-18
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

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        AirPushbackY(12000)
    sprite('Action_002_00', 2)	# 1-2
    sprite('Action_002_01', 1)	# 3-3
    sprite('Action_002_01', 1)	# 4-4
    Unknown7009(1)
    teleportRelativeX(50000)
    sprite('Action_002_02', 4)	# 5-8
    teleportRelativeX(50000)
    physicsXImpulse(16000)
    Unknown1028(-2000)
    SFX_3('SE042')
    sprite('Action_002_03', 4)	# 9-12	 **attackbox here**
    Unknown1084(1)
    sprite('Action_002_04', 7)	# 13-19
    Recovery()
    Unknown2063()
    sprite('Action_002_05', 5)	# 20-24
    sprite('Action_002_06', 1)	# 25-25
    teleportRelativeX(30000)
    sprite('Action_002_06', 1)	# 26-26
    teleportRelativeX(30000)
    sprite('Action_002_07', 3)	# 27-29
    loopRest()

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(15000)
        AirPushbackY(16000)
        AirUntechableTime(19)
        Unknown9154(19)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_191_00', 3)	# 1-3
    sprite('Action_191_01', 3)	# 4-6
    Unknown7009(1)
    sprite('Action_191_02', 2)	# 7-8
    sprite('Action_191_03', 1)	# 9-9
    teleportRelativeX(50000)
    sprite('Action_191_04', 2)	# 10-11	 **attackbox here**
    SFX_3('SE043')
    RefreshMultihit()
    sprite('Action_191_05', 7)	# 12-18
    Recovery()
    Unknown2063()
    sprite('Action_191_06', 4)	# 19-22
    sprite('Action_191_07', 3)	# 23-25
    sprite('Action_191_08', 2)	# 26-27
    loopRest()

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(30)
        AirPushbackX(29000)
        AirPushbackY(16000)
        PushbackX(39900)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_4th')
        sendToLabelUpon(77, 9)
    sprite('Action_403_00', 7)	# 1-7
    sprite('Action_403_01', 5)	# 8-12
    Unknown8007(100, 1, 1)
    SFX_3('SE045')
    physicsXImpulse(30000)
    Unknown7006('ugo108_0', 100, 829384565, 828323888, 0, 0, 100, 829384565, 845101104, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_403_02', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    Unknown1019(80)
    sprite('Action_403_03', 4)	# 17-20	 **attackbox here**
    sprite('Action_403_04', 4)	# 21-24	 **attackbox here**
    label(9)
    sprite('Action_403_05', 4)	# 25-28
    clearUponHandler(77)
    Recovery()
    Unknown2063()
    Unknown1019(50)
    sprite('Action_403_06', 6)	# 29-34
    Unknown8010(100, 1, 1)
    Unknown1019(50)
    sprite('Action_403_07', 6)	# 35-40
    Unknown1019(50)
    sprite('Action_403_08', 6)	# 41-46
    Unknown1019(50)

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('Action_234_00', 2)	# 1-2	 **attackbox here**
    Unknown1084(1)
    sprite('Action_234_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_234_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_234_03', 6)	# 8-13	 **attackbox here**
    Unknown7006('ugo302', 100, 862938997, 13104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_234_04', 4)	# 14-17	 **attackbox here**
    sprite('Action_234_05', 3)	# 18-20	 **attackbox here**
    SFX_3('SE043')
    GFX_0('UGO_Scratch_AtkCol', 100)
    sprite('Action_234_06', 4)	# 21-24	 **attackbox here**
    sprite('Action_234_07', 4)	# 25-28	 **attackbox here**
    sprite('Action_234_08', 5)	# 29-33	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_234_09', 6)	# 34-39
    sprite('Action_234_10', 4)	# 40-43
    sprite('Action_234_11', 3)	# 44-46

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown9016(1)
        Unknown1112('')
        AirHitstunAnimation(11)
        AirUntechableTime(22)
        Unknown9310(1)
        AirPushbackX(20000)
        AirPushbackY(-25000)
        HitOrBlockCancel('NmlAtk5B_2nd')
        callSubroutine('ChainRoot')
    sprite('Action_003_00', 4)	# 1-4
    GFX_0('UGO_Nml5C_WeaponSummonIn', 100)
    sprite('Action_003_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_003_02', 3)	# 9-11	 **attackbox here**
    sprite('Action_003_03', 2)	# 12-13	 **attackbox here**
    sprite('Action_003_04', 2)	# 14-15	 **attackbox here**
    sprite('Action_003_05', 2)	# 16-17	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    Unknown7006('ugo104_1', 100, 829384565, 845100080, 0, 0, 100, 829384565, 811545904, 0, 0, 100, 829384565, 828323120, 0, 0, 100)
    sprite('Action_003_06', 1)	# 18-18	 **attackbox here**
    GFX_0('UGO_Nml5C_Zanzo', 100)
    sprite('Action_003_07', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 3500)
    Unknown4004('6566666563745f3434310000000000000000000000000000000000000000000000000000')
    Unknown2015(225)
    SFX_3('SE210')
    sprite('Action_003_08', 3)	# 22-24	 **attackbox here**
    Unknown23027()
    Unknown2015(-1)
    Recovery()
    Unknown2063()
    sprite('Action_003_08', 8)	# 25-32	 **attackbox here**
    Unknown23027()
    sprite('Action_003_09', 6)	# 33-38	 **attackbox here**
    sprite('Action_003_10', 6)	# 39-44	 **attackbox here**
    sprite('Action_003_11', 7)	# 45-51
    GFX_0('UGO_Nml5C_WeaponSummonOut', 100)
    sprite('Action_003_12', 6)	# 52-57
    sprite('Action_003_13', 6)	# 58-63

@State
def NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(75)
        AirPushbackY(10000)
        Unknown9016(1)
        Unknown28(77, 'NmlAtk5B_2nd_Add')
        Unknown23027()
    sprite('Action_461_01', 2)	# 1-2	 **attackbox here**
    tag_voice(1, 'ugo201_0', 'ugo201_1', 'ugo201_2', '')
    teleportRelativeX(10000)
    sprite('Action_461_02', 2)	# 3-4	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_461_03', 3)	# 5-7	 **attackbox here**
    teleportRelativeX(10100)
    sprite('Action_461_04', 2)	# 8-9	 **attackbox here**
    physicsXImpulse(23500)
    sprite('Action_461_05', 1)	# 10-10	 **attackbox here**
    SFX_3('SE042')
    sprite('Action_461_06', 1)	# 11-11	 **attackbox here**
    Unknown1084(1)
    sprite('Action_461_07', 1)	# 12-12	 **attackbox here**
    sprite('Action_461_08', 4)	# 13-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_461_09', 3)	# 17-19	 **attackbox here**
    clearUponHandler(77)
    GFX_0('UGO_Assault_Zanzou', 100)
    RefreshMultihit()
    AirUntechableTime(26)
    Hitstop(15)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackY(35000)
    AirPushbackX(7000)
    YImpluseBeforeWallbounce(2800)
    sprite('Action_461_10', 3)	# 20-22	 **attackbox here**
    sprite('Action_461_11', 3)	# 23-25	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_461_12', 4)	# 26-29	 **attackbox here**
    sprite('Action_461_13', 4)	# 30-33
    GFX_0('UGO_Assault_SummonOut', 100)
    sprite('Action_461_14', 3)	# 34-36
    sprite('Action_461_15', 3)	# 37-39

@State
def NmlAtk5B_2nd_Add():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(900)
        AttackP2(100)
        AttackP1(75)
        Unknown9016(1)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Hitstop(15)
        AirUntechableTime(35)
        PushbackX(-18000)
        AirPushbackY(21000)
        AirPushbackX(-18000)
        teleportRelativeX(62000)
        Unknown11108('03000000')
        callSubroutine('ChainRoot')

        def upon_78():
            Unknown2038(1)
            HitOrBlockCancel('NmlAtk5B_3rd')
    sprite('Action_465_00', 6)	# 1-6	 **attackbox here**
    sprite('Action_465_01', 2)	# 7-8	 **attackbox here**
    Unknown14070('NmlAtk5B_3rd')
    GFX_0('UGO_Assault2nd_Zanzou', 100)
    sprite('Action_465_02', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE045')
    sprite('Action_465_03', 3)	# 11-13	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_465_03', 2)	# 14-15	 **attackbox here**
    if SLOT_2:
        Unknown14072('NmlAtk5B_3rd')
    sprite('Action_465_04', 5)	# 16-20	 **attackbox here**
    sprite('Action_465_04', 3)	# 21-23	 **attackbox here**
    Unknown14074('NmlAtk5B_3rd')
    sprite('Action_465_05', 6)	# 24-29
    GFX_0('UGO_Assault2nd_SummonOut', 100)
    sprite('Action_465_06', 4)	# 30-33
    sprite('Action_465_07', 4)	# 34-37

@State
def NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk5B_3rd_Exe', 1, 0, 0)
        Damage(800)
        AttackP2(100)
        Unknown11091(0)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11054(-1)
        Unknown11045(0)
        Unknown11046(0)
        Unknown30068(1)
        JumpCancel_(0)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11032('20a1070001000000ffffffffffffffff')
        Unknown11056(2)
        Unknown9266(12)
    sprite('Action_470_00', 2)	# 1-2
    GFX_0('UGO_DrainThrow_AuraA', 0)
    sprite('Action_470_01', 3)	# 3-5
    sprite('Action_470_02', 5)	# 6-10
    sprite('Action_470_03', 3)	# 11-13
    sprite('Action_470_04', 2)	# 14-15
    SFX_3('SE042')
    GFX_0('UGO_DrainThrow_LandZanzou', 100)
    sprite('Action_470_05', 1)	# 16-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_470_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_470_07', 5)	# 20-24
    sprite('Action_470_08', 4)	# 25-28
    sprite('Action_470_09', 4)	# 29-32
    sprite('Action_470_10', 8)	# 33-40
    sprite('Action_470_11', 5)	# 41-45
    sprite('Action_470_12', 4)	# 46-49

@State
def NmlAtk5B_3rd_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1500)
        PushbackX(45000)
        AttackP2(100)
        Unknown11091(0)
        Unknown9016(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(1)
        Hitstop(1)
        Unknown9154(20)
        JumpCancel_(0)
        setInvincible(1)
        Unknown30068(1)
        Unknown30048(1)
        Unknown13045(0)
        Unknown11044(1)
        Unknown11068(1)
        Unknown9266(12)

        def upon_78():
            Unknown2058(500)
            Unknown36(22)
            Unknown2058(-1000)
            Unknown35()
    sprite('Action_198_00', 4)	# 1-4	 **attackbox here**
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    StartMultihit()
    sprite('Action_198_01', 10)	# 5-14
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    tag_voice(0, 'ugo203_0', 'ugo203_1', 'ugo203_2', '')
    sprite('Action_198_02', 8)	# 15-22
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_198_03', 7)	# 23-29
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('UGO_DrainThrow_HitAura', 0)
    sprite('Action_198_04', 4)	# 30-33	 **attackbox here**
    SFX_3('SE008')
    RefreshMultihit()
    GFX_0('UGO_Drain_Steal', 0)
    GFX_0('UGO_Drain_Yoin', 100)
    sprite('Action_198_05', 18)	# 34-51
    sprite('Action_198_06', 6)	# 52-57
    sprite('Action_198_07', 5)	# 58-62

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(0)
    SFX_3('SE041')
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_004_03', 6)	# 9-14
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 15-19
    sprite('Action_004_05', 5)	# 20-24
    loopRest()

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(0)
    SFX_3('SE041')
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_004_03', 6)	# 9-14
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 15-19
    sprite('Action_004_05', 5)	# 20-24
    loopRest()

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(90)
        PushbackX(15000)
        AirPushbackY(18000)
        HitLow(2)
        callSubroutine('ChainRoot')
    sprite('Action_006_00', 3)	# 1-3
    sprite('Action_006_01', 3)	# 4-6
    Unknown7006('ugo106_0', 100, 829384565, 828323376, 0, 0, 100, 829384565, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_006_02', 2)	# 7-8	 **attackbox here**
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_006_03', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    sprite('Action_006_04', 3)	# 12-14	 **attackbox here**
    HitJumpCancel(0)
    sprite('Action_006_05', 2)	# 15-16
    SFX_3('SE049_SpecialSwing')
    sprite('Action_006_06', 1)	# 17-17	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    AirPushbackY(27000)
    AirUntechableTime(24)
    Unknown9016(1)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    HitLow(0)
    Unknown11058('0000000001000000000000000000000000000000')

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown2038(1)
        HitJumpCancel(1)
        GFX_0('UGO_Nml2C_Zanzo', 100)
    sprite('Action_006_06', 1)	# 18-18	 **attackbox here**
    clearUponHandler(10)
    if (not SLOT_2):
        GFX_0('UGO_Nml2C_Zanzo', 100)
    sprite('Action_006_06', 4)	# 19-22	 **attackbox here**
    sprite('Action_006_07', 8)	# 23-30	 **attackbox here**
    Unknown23027()
    Unknown2063()
    Recovery()
    sprite('Action_006_08', 5)	# 31-35
    GFX_0('UGO_Nml2C_WeaponSummonOut', 100)
    sprite('Action_006_09', 5)	# 36-40
    sprite('Action_006_10', 4)	# 41-44
    loopRest()

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(12000)
        AirUntechableTime(26)
        Unknown11065(1)
        Unknown11058('0000000000000000010000000000000000000000')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitJumpCancel(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            sendToLabel(0)
        Unknown18009(1)
    sprite('Action_193_00', 5)	# 1-5
    sprite('Action_193_01', 5)	# 6-10
    Unknown7006('ugo107_0', 100, 829384565, 828323632, 0, 0, 100, 829384565, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_193_02', 2)	# 11-12
    physicsXImpulse(32500)
    Unknown1028(-1200)
    Unknown8006(100, 1, 0)
    Unknown8007(100, 1, 0)
    sprite('Action_193_03', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE043')
    sprite('Action_193_04', 2)	# 15-16	 **attackbox here**
    sprite('Action_193_05', 3)	# 17-19	 **attackbox here**
    sprite('Action_193_06', 3)	# 20-22	 **attackbox here**
    label(0)
    sprite('Action_193_07', 12)	# 23-34
    Unknown2063()
    Recovery()
    sprite('Action_193_08', 7)	# 35-41
    sprite('Action_193_09', 5)	# 42-46
    Unknown1084(1)
    sprite('Action_193_10', 3)	# 47-49
    sprite('Action_014_01', 3)	# 50-52
    Unknown18009(0)
    loopRest()

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1600)
        AirHitstunAnimation(10)
        HitOrBlockJumpCancel(1)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_008_00', 6)	# 1-6
    sprite('Action_008_01', 1)	# 7-7
    SFX_3('SE042')
    Unknown7009(4)
    sprite('Action_008_02', 2)	# 8-9	 **attackbox here**
    GFX_0('UGO_NmlAIR5B_Zanzo1', 100)
    RefreshMultihit()
    sprite('Action_008_03', 2)	# 10-11
    sprite('Action_008_04', 3)	# 12-14
    sprite('Action_008_05', 2)	# 15-16
    sprite('Action_008_06', 2)	# 17-18	 **attackbox here**
    SFX_3('SE043')
    GFX_0('UGO_NmlAIR5B_Zanzo2', 100)
    RefreshMultihit()
    sprite('Action_008_06', 3)	# 19-21	 **attackbox here**
    Unknown23027()
    Unknown2063()
    Recovery()
    sprite('Action_008_07', 7)	# 22-28
    sprite('Action_008_08', 5)	# 29-33
    loopRest()

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1800)
        AirPushbackX(11500)
        AirPushbackY(19000)
        HitOrBlockJumpCancel(1)
        AirHitstunAnimation(10)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('Action_009_12', 2)	# 1-2
    sprite('Action_009_13', 2)	# 3-4
    sprite('Action_009_14', 2)	# 5-6
    Unknown7009(2)
    sprite('Action_009_15', 2)	# 7-8
    sprite('Action_009_16', 1)	# 9-9
    sprite('Action_009_17', 4)	# 10-13	 **attackbox here**
    SFX_3('SE043')
    GFX_0('UGO_NmlAIR5C_Zanzo', 100)
    RefreshMultihit()
    sprite('Action_009_18', 4)	# 14-17
    Unknown2063()
    Recovery()
    sprite('Action_009_19', 8)	# 18-25
    sprite('Action_009_20', 10)	# 26-35
    loopRest()

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1900)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(12000)
        PushbackX(21000)
        Unknown2057(0)
        HitOverhead(0)
        SLOT_2 = SLOT_12
        Unknown1084(1)
    sprite('Action_180_00', 2)	# 1-2	 **attackbox here**
    if (SLOT_2 >= 8000):
        Unknown1019(0)
        physicsXImpulse(5000)
    if (SLOT_2 < (-8000)):
        physicsXImpulse(-5000)
    sprite('Action_180_01', 1)	# 3-3	 **attackbox here**
    physicsYImpulse(1500)
    setGravity(50)
    Unknown22004(13, 1)
    sprite('Action_180_02', 1)	# 4-4	 **attackbox here**
    Unknown7006('ugo204_0', 100, 846161781, 828322864, 0, 0, 100, 846161781, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    SFX_3('SE045')
    sprite('Action_180_03', 1)	# 5-5	 **attackbox here**
    Unknown23027()
    sprite('Action_180_04', 2)	# 6-7	 **attackbox here**
    sprite('Action_180_05', 3)	# 8-10	 **attackbox here**
    sprite('Action_180_06', 2)	# 11-12	 **attackbox here**
    GFX_0('UGO_AirAssaultA_AtkCol', 100)
    SFX_3('SE049_SpecialSwing')
    sprite('Action_180_07ex01', 2)	# 13-14	 **attackbox here**
    Unknown1021(7000)
    setGravity(700)
    RefreshMultihit()
    AttackLevel_(4)
    AirUntechableTime(37)
    Unknown9016(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(30000)
    YImpluseBeforeWallbounce(2000)
    PushbackX(21000)
    sprite('Action_180_07ex01', 1)	# 15-15	 **attackbox here**
    sprite('Action_180_08', 5)	# 16-20	 **attackbox here**
    Recovery()
    Unknown23027()
    setGravity(2000)
    sprite('Action_180_09', 9)	# 21-29	 **attackbox here**
    sprite('Action_180_10', 5)	# 30-34
    sprite('Action_180_11', 6)	# 35-40
    sprite('Action_180_12', 6)	# 41-46

@State
def NmlAtk6B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Unknown12051(2)
        HitOverhead(2)
        GroundedHitstunAnimation(3)
        AirHitstunAnimation(10)
        Unknown9154(25)
        AirUntechableTime(30)
        Unknown9202(30)
        Unknown11028(25)
        AirPushbackX(35000)
        AirPushbackY(-25000)
        PushbackX(15000)
    sprite('Action_190_00', 7)	# 1-7
    sprite('Action_190_01', 6)	# 8-13
    sprite('Action_190_02', 5)	# 14-18
    sprite('Action_190_03', 4)	# 19-22
    sprite('Action_190_04', 2)	# 23-24
    physicsXImpulse(43000)
    Unknown1047(-1500)
    sprite('Action_190_05', 2)	# 25-26
    sprite('Action_190_06', 5)	# 27-31	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    ScreenShake(8000, 3500)
    sprite('Action_190_07', 7)	# 32-38
    Recovery()
    Unknown2063()
    sprite('Action_190_08', 1)	# 39-39
    teleportRelativeX(88000)
    sprite('Action_190_08', 1)	# 40-40
    sprite('Action_190_08', 3)	# 41-43
    sprite('Action_190_09', 4)	# 44-47
    teleportRelativeX(75000)
    loopRest()

@State
def NmlAtk4B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk5C')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk6B')
        HitOrBlockCancel('NmlAtk6C')
        HitOrBlockCancel('NmlAtk3B')
        HitOrBlockJumpCancel(1)
    sprite('Action_191_00', 3)	# 1-3
    sprite('Action_191_01', 3)	# 4-6
    sprite('Action_191_02', 2)	# 7-8
    sprite('Action_191_03', 1)	# 9-9
    teleportRelativeX(50000)
    sprite('Action_191_04', 2)	# 10-11	 **attackbox here**
    RefreshMultihit()
    sprite('Action_191_05', 7)	# 12-18
    Recovery()
    Unknown2063()
    sprite('Action_191_06', 4)	# 19-22
    sprite('Action_191_07', 3)	# 23-25
    sprite('Action_191_08', 2)	# 26-27
    loopRest()

@State
def NmlAtk6C():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackY(1000)
        YImpluseBeforeWallbounce(100)
        AirPushbackX(65000)
        Unknown9178(1)
        AirHitstunAfterWallbounce(30)
        WallbounceReboundTime(10)
    sprite('Action_403_00', 12)	# 1-12
    sprite('Action_403_01', 3)	# 13-15
    sprite('Action_403_01', 3)	# 16-18
    physicsXImpulse(60000)
    Unknown1028(-3200)
    sprite('Action_403_02', 4)	# 19-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_03', 4)	# 23-26	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_403_04', 4)	# 27-30	 **attackbox here**
    sprite('Action_403_05', 3)	# 31-33
    sprite('Action_403_06', 3)	# 34-36
    physicsXImpulse(16000)
    Unknown1028(-3000)
    sprite('Action_403_07', 5)	# 37-41
    sprite('Action_403_08', 4)	# 42-45
    Unknown1084(1)
    loopRest()

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
    Unknown23087(38000)
    sprite('Action_068_03', 3)	# 8-10
    tag_voice(1, 'ugo156_0', 'ugo156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 2)	# 14-15
    sprite('Action_009_12', 2)	# 16-17
    sprite('Action_009_13', 3)	# 18-20
    sprite('Action_009_14', 2)	# 21-22
    sprite('Action_009_15', 2)	# 23-24
    sprite('Action_009_16', 1)	# 25-25
    sprite('Action_009_17', 3)	# 26-28	 **attackbox here**
    SFX_3('SE043')
    GFX_0('UGO_NmlAIR5C_Zanzo', 100)
    RefreshMultihit()
    sprite('Action_009_18', 4)	# 29-32
    sprite('Action_009_19', 8)	# 33-40
    label(0)
    sprite('Action_068_09', 3)	# 41-43
    sprite('Action_068_10', 2)	# 44-45
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_069_00', 3)	# 46-48
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_069_01', 6)	# 49-54
    sprite('Action_069_02', 2)	# 55-56
    Unknown18009(0)
    sprite('Action_069_03', 2)	# 57-58

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 19)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_009_18', 4)	# 1-4
    Recovery()
    sprite('Action_009_19', 8)	# 5-12
    label(0)
    sprite('Action_068_09', 3)	# 13-15
    sprite('Action_068_10', 2)	# 16-17
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_069_01', 3)	# 18-20
    sprite('Action_069_02', 3)	# 21-23
    sprite('Action_069_03', 30)	# 24-53
    label(2)
    sprite('Action_191_00', 3)	# 54-56
    clearUponHandler(17)
    teleportRelativeY(0)
    tag_voice(0, 'ugo157_0', 'ugo157_1', '', '')
    sprite('Action_191_01', 3)	# 57-59
    sprite('Action_191_02', 3)	# 60-62
    sprite('Action_191_03', 1)	# 63-63
    sprite('Action_191_04', 2)	# 64-65	 **attackbox here**
    SFX_3('SE043')
    RefreshMultihit()
    sprite('Action_191_05', 7)	# 66-72
    Unknown23027()
    sprite('Action_191_06', 4)	# 73-76
    sprite('Action_191_07', 3)	# 77-79
    sprite('Action_191_08', 2)	# 80-81
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('Action_000_00', 7)	# 82-88	 **attackbox here**
    sprite('Action_000_01', 7)	# 89-95	 **attackbox here**
    sprite('Action_000_02', 6)	# 96-101	 **attackbox here**
    sprite('Action_000_03', 6)	# 102-107	 **attackbox here**
    sprite('Action_000_04', 5)	# 108-112	 **attackbox here**
    sprite('Action_000_05', 5)	# 113-117	 **attackbox here**
    sprite('Action_000_06', 5)	# 118-122	 **attackbox here**
    sprite('Action_000_07', 6)	# 123-128	 **attackbox here**
    sprite('Action_000_08', 6)	# 129-134	 **attackbox here**
    sprite('Action_000_09', 7)	# 135-141	 **attackbox here**
    sprite('Action_000_10', 7)	# 142-148	 **attackbox here**
    sprite('Action_000_11', 6)	# 149-154	 **attackbox here**
    sprite('Action_000_12', 6)	# 155-160	 **attackbox here**
    sprite('Action_000_13', 5)	# 161-165	 **attackbox here**
    sprite('Action_000_14', 5)	# 166-170
    sprite('Action_000_15', 5)	# 171-175
    sprite('Action_000_16', 6)	# 176-181
    sprite('Action_000_17', 6)	# 182-187
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 188-188

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_012_00', 1)	# 1-1
    sprite('Action_012_01', 2)	# 2-3
    sprite('Action_012_02', 1)	# 4-4
    sprite('Action_006_00', 1)	# 5-5
    sprite('Action_006_01', 2)	# 6-7
    sprite('Action_006_02', 1)	# 8-8	 **attackbox here**
    sprite('Action_006_03', 2)	# 9-10	 **attackbox here**
    StartMultihit()
    sprite('Action_006_04', 2)	# 11-12	 **attackbox here**
    sprite('Action_006_05', 2)	# 13-14
    SFX_3('SE049_SpecialSwing')
    sprite('Action_006_06', 2)	# 15-16	 **attackbox here**
    GFX_0('UGO_Nml2C_Zanzo', 100)
    sprite('Action_006_06', 4)	# 17-20	 **attackbox here**
    sprite('Action_006_07', 8)	# 21-28	 **attackbox here**
    sprite('Action_006_08', 5)	# 29-33
    GFX_0('UGO_Nml2C_WeaponSummonOut', 100)
    sprite('Action_006_09', 5)	# 34-38
    sprite('Action_006_10', 4)	# 39-42
    loopRest()
    sprite('Action_000_00', 7)	# 43-49	 **attackbox here**
    sprite('Action_000_01', 7)	# 50-56	 **attackbox here**
    sprite('Action_000_02', 6)	# 57-62	 **attackbox here**
    sprite('Action_000_03', 6)	# 63-68	 **attackbox here**
    sprite('Action_000_04', 8)	# 69-76	 **attackbox here**
    sprite('Action_000_05', 5)	# 77-81	 **attackbox here**
    sprite('Action_000_06', 5)	# 82-86	 **attackbox here**
    sprite('Action_000_07', 5)	# 87-91	 **attackbox here**
    sprite('Action_000_08', 6)	# 92-97	 **attackbox here**
    sprite('Action_000_09', 5)	# 98-102	 **attackbox here**
    sprite('Action_000_10', 6)	# 103-108	 **attackbox here**
    sprite('Action_000_11', 8)	# 109-116	 **attackbox here**
    sprite('Action_000_12', 5)	# 117-121	 **attackbox here**
    sprite('Action_000_13', 5)	# 122-126	 **attackbox here**
    sprite('Action_000_14', 6)	# 127-132
    label(0)
    sprite('Action_000_00', 7)	# 133-139	 **attackbox here**
    sprite('Action_000_01', 7)	# 140-146	 **attackbox here**
    sprite('Action_000_02', 6)	# 147-152	 **attackbox here**
    sprite('Action_000_03', 6)	# 153-158	 **attackbox here**
    sprite('Action_000_04', 8)	# 159-166	 **attackbox here**
    sprite('Action_000_05', 5)	# 167-171	 **attackbox here**
    sprite('Action_000_06', 5)	# 172-176	 **attackbox here**
    sprite('Action_000_07', 5)	# 177-181	 **attackbox here**
    sprite('Action_000_08', 6)	# 182-187	 **attackbox here**
    sprite('Action_000_09', 5)	# 188-192	 **attackbox here**
    sprite('Action_000_10', 6)	# 193-198	 **attackbox here**
    sprite('Action_000_11', 8)	# 199-206	 **attackbox here**
    sprite('Action_000_12', 5)	# 207-211	 **attackbox here**
    sprite('Action_000_13', 5)	# 212-216	 **attackbox here**
    sprite('Action_000_14', 6)	# 217-222
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 223-223

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('Action_240_27', 4)	# 1-4
    GFX_0('UGO_UltimateAssault_Start_TAG1', 0)
    sprite('Action_240_28', 4)	# 5-8
    GFX_0('UGO_UltimateAssault_Start_TAG2', 0)
    sprite('Action_240_29', 5)	# 9-13
    sprite('Action_240_30', 4)	# 14-17
    sprite('Action_240_31', 2)	# 18-19	 **attackbox here**
    Unknown26('UGO_UltimateAssault_Start_TAG2')
    tag_voice(0, 'ugo158_0', 'ugo158_1', '', '')
    GFX_0('UGO_UltimateAssault_AtkEff_Fini', 100)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_32', 3)	# 20-22	 **attackbox here**
    teleportRelativeX(-50000)
    sprite('Action_240_33', 28)	# 23-50	 **attackbox here**
    sprite('Action_240_34', 5)	# 51-55
    teleportRelativeX(50000)
    sprite('Action_240_35', 5)	# 56-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 24)	# 1-24
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 25-25
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1100000)
    Unknown1007(200000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_180_02', 4)	# 26-29	 **attackbox here**
    sprite('Action_180_03', 3)	# 30-32	 **attackbox here**
    SFX_3('SE045')
    StartMultihit()
    Unknown8001(0, 100)
    physicsXImpulse(12000)
    physicsYImpulse(15000)
    setGravity(3500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('Action_180_04', 3)	# 33-35	 **attackbox here**
    sprite('Action_180_05', 3)	# 36-38	 **attackbox here**
    sprite('Action_180_02', 3)	# 39-41	 **attackbox here**
    sprite('Action_180_06ex01', 2)	# 42-43	 **attackbox here**
    GFX_0('UGO_AirAssaultA_AtkCol_TAG', 100)
    SFX_3('SE049_SpecialSwing')
    sprite('Action_180_07', 2)	# 44-45	 **attackbox here**
    sprite('Action_180_08', 5)	# 46-50	 **attackbox here**
    sprite('Action_180_09', 9)	# 51-59	 **attackbox here**
    sprite('Action_180_10', 4)	# 60-63
    sprite('Action_180_11', 5)	# 64-68
    sprite('Action_180_12', 32767)	# 69-32835
    label(1)
    sprite('Action_021_00', 4)	# 32836-32839
    Unknown1019(0)
    sprite('Action_021_01', 3)	# 32840-32842
    sprite('Action_021_02', 3)	# 32843-32845
    sprite('Action_000_00', 7)	# 32846-32852	 **attackbox here**
    sprite('Action_000_01', 7)	# 32853-32859	 **attackbox here**
    sprite('Action_000_02', 6)	# 32860-32865	 **attackbox here**
    sprite('Action_000_03', 6)	# 32866-32871	 **attackbox here**
    sprite('Action_000_04', 8)	# 32872-32879	 **attackbox here**
    sprite('Action_000_05', 5)	# 32880-32884	 **attackbox here**
    sprite('Action_000_06', 5)	# 32885-32889	 **attackbox here**
    sprite('Action_000_07', 5)	# 32890-32894	 **attackbox here**
    sprite('Action_000_08', 6)	# 32895-32900	 **attackbox here**
    sprite('Action_000_09', 5)	# 32901-32905	 **attackbox here**
    sprite('Action_000_10', 6)	# 32906-32911	 **attackbox here**
    sprite('Action_000_11', 8)	# 32912-32919	 **attackbox here**
    sprite('Action_000_12', 5)	# 32920-32924	 **attackbox here**
    sprite('Action_000_13', 5)	# 32925-32929	 **attackbox here**
    sprite('Action_000_14', 6)	# 32930-32935

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('Action_156_00', 2)	# 1-2
    sprite('Action_156_01', 3)	# 3-5
    GFX_0('UGO_Strike_SummonIn', 100)
    sprite('Action_156_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_156_03', 3)	# 9-11	 **attackbox here**
    SFX_3('SE043')
    sprite('Action_156_04', 3)	# 12-14	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    RefreshMultihit()
    ScreenShake(11000, 5000)
    GFX_0('UGO_StrikeA_Inpact', 0)
    sprite('Action_156_05', 10)	# 15-24	 **attackbox here**
    Recovery()
    sprite('Action_156_06', 5)	# 25-29
    GFX_0('UGO_StrikeA_SummonOut', 100)
    loopRest()
    sprite('Action_000_00', 7)	# 30-36	 **attackbox here**
    sprite('Action_000_01', 7)	# 37-43	 **attackbox here**
    sprite('Action_000_02', 6)	# 44-49	 **attackbox here**
    sprite('Action_000_03', 6)	# 50-55	 **attackbox here**
    sprite('Action_000_04', 8)	# 56-63	 **attackbox here**
    sprite('Action_000_05', 5)	# 64-68	 **attackbox here**
    sprite('Action_000_06', 5)	# 69-73	 **attackbox here**
    sprite('Action_000_07', 5)	# 74-78	 **attackbox here**
    sprite('Action_000_08', 6)	# 79-84	 **attackbox here**
    sprite('Action_000_09', 5)	# 85-89	 **attackbox here**
    sprite('Action_000_10', 6)	# 90-95	 **attackbox here**
    sprite('Action_000_11', 8)	# 96-103	 **attackbox here**
    sprite('Action_000_12', 5)	# 104-108	 **attackbox here**
    sprite('Action_000_13', 5)	# 109-113	 **attackbox here**
    sprite('Action_000_14', 6)	# 114-119

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('Action_240_27', 4)	# 1-4
    GFX_0('UGO_UltimateAssault_Start_TAG1', 0)
    sprite('Action_240_28', 4)	# 5-8
    GFX_0('UGO_UltimateAssault_Start_TAG2', 0)
    sprite('Action_240_29', 5)	# 9-13
    sprite('Action_240_30', 4)	# 14-17
    sprite('Action_240_31', 2)	# 18-19	 **attackbox here**
    Unknown26('UGO_UltimateAssault_Start_TAG2')
    GFX_0('UGO_UltimateAssault_AtkEff_Fini', 100)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_32', 3)	# 20-22	 **attackbox here**
    teleportRelativeX(-50000)
    sprite('Action_240_33', 28)	# 23-50	 **attackbox here**
    sprite('Action_240_34', 5)	# 51-55
    teleportRelativeX(50000)
    sprite('Action_240_35', 5)	# 56-60

@State
def NmlAtkExcite():

    def upon_IMMEDIATE():
        Unknown17013()
        loopRelated(17, 61)

        def upon_17():
            Unknown13019(1)
            Unknown13026(1)
            Unknown13015(1)
    sprite('keep', 1)	# 1-1
    loopRest()

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
    sprite('Action_010_00', 4)	# 1-4
    sprite('Action_045_00', 3)	# 5-7
    sprite('Action_045_01', 2)	# 8-9
    sprite('Action_045_02', 2)	# 10-11
    SFX_0('000_airdash_1')
    label(0)
    sprite('Action_045_03', 3)	# 12-14
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    sprite('Action_045_06', 3)	# 21-23
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_07', 3)	# 24-26
    sprite('Action_045_08', 3)	# 27-29
    sprite('Action_045_09', 3)	# 30-32
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_01', 3)	# 33-35
    sprite('Action_045_02', 3)	# 36-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 39-41
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 42-44	 **attackbox here**
    SFX_3('SE042')
    Unknown1084(1)
    sprite('Action_055_02', 2)	# 45-46
    SFX_1('ugo154')
    sprite('Action_055_03', 3)	# 47-49
    sprite('Action_055_04', 7)	# 50-56
    sprite('Action_055_05', 7)	# 57-63
    sprite('Action_055_06', 4)	# 64-67

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Damage(2000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP2(50)
        Unknown11092(1)
        Hitstop(0)
        AirUntechableTime(35)
        Unknown11064(1)
    sprite('Action_057_00', 5)	# 1-5
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    Unknown5003(1)
    sprite('Action_057_01', 8)	# 6-13
    SFX_1('ugo153_0')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_02', 3)	# 14-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_03', 1)	# 17-17	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(500)
    Unknown30079(1)
    sprite('Action_057_04', 5)	# 18-22
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_05', 4)	# 23-26
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_06', 3)	# 27-29
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_07', 2)	# 30-31
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_08', 1)	# 32-32
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_09', 4)	# 33-36
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_10', 4)	# 37-40
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('Action_057_11', 7)	# 41-47
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_12', 6)	# 48-53
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_13', 1)	# 54-54	 **attackbox here**
    SFX_1('ugo153_1')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    StartMultihit()
    SFX_3('SE045')
    sprite('Action_057_13', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    AttackLevel_(4)
    Damage(1500)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(1)
    YImpluseBeforeWallbounce(0)
    Hitstop(0)
    AirUntechableTime(60)
    Unknown9178(1)
    WallbounceReboundTime(28)
    AirHitstunAfterWallbounce(60)
    Unknown9362(1)
    Unknown9364(35)
    Unknown9016(1)
    Unknown30079(0)
    Unknown11064(0)
    sprite('Action_057_14', 7)	# 57-63
    sprite('Action_057_15', 4)	# 64-67
    sprite('Action_057_16', 4)	# 68-71
    sprite('Action_057_17', 3)	# 72-74

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
    sprite('Action_010_00', 4)	# 1-4
    sprite('Action_045_00', 3)	# 5-7
    sprite('Action_045_01', 2)	# 8-9
    sprite('Action_045_02', 2)	# 10-11
    SFX_0('000_airdash_1')
    label(0)
    sprite('Action_045_03', 3)	# 12-14
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_04', 3)	# 15-17
    sprite('Action_045_05', 3)	# 18-20
    sprite('Action_045_06', 3)	# 21-23
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_07', 3)	# 24-26
    sprite('Action_045_08', 3)	# 27-29
    sprite('Action_045_09', 3)	# 30-32
    SFX_0('019_cloth_a')
    Unknown8006(100, 1, 0)
    sprite('Action_045_01', 3)	# 33-35
    sprite('Action_045_02', 3)	# 36-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 39-41
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 42-44	 **attackbox here**
    SFX_3('SE042')
    Unknown1084(1)
    sprite('Action_055_02', 2)	# 45-46
    SFX_1('ugo154')
    sprite('Action_055_03', 3)	# 47-49
    sprite('Action_055_04', 7)	# 50-56
    sprite('Action_055_05', 7)	# 57-63
    sprite('Action_055_06', 4)	# 64-67

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        Damage(2000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP2(50)
        Unknown11092(1)
        Hitstop(0)
        AirUntechableTime(35)
        Unknown11064(1)
    sprite('Action_057_00', 5)	# 1-5
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    Unknown5003(1)
    sprite('Action_057_01', 8)	# 6-13
    Unknown2005()
    SFX_1('ugo153_0')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_02', 3)	# 14-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_03', 1)	# 17-17	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    RefreshMultihit()
    AttackLevel_(3)
    Damage(500)
    Unknown30079(1)
    sprite('Action_057_04', 5)	# 18-22
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_05', 4)	# 23-26
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_06', 3)	# 27-29
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_07', 2)	# 30-31
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_08', 1)	# 32-32
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_09', 4)	# 33-36
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_10', 4)	# 37-40
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('Action_057_11', 7)	# 41-47
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_12', 6)	# 48-53
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_057_13', 1)	# 54-54	 **attackbox here**
    SFX_1('ugo153_1')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    StartMultihit()
    SFX_3('SE045')
    sprite('Action_057_13', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    AttackLevel_(4)
    Damage(1500)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(100000)
    AirPushbackY(1)
    YImpluseBeforeWallbounce(0)
    Hitstop(0)
    AirUntechableTime(60)
    Unknown9178(1)
    WallbounceReboundTime(28)
    AirHitstunAfterWallbounce(60)
    Unknown9362(1)
    Unknown9364(35)
    Unknown9016(1)
    Unknown30079(0)
    Unknown11064(0)
    sprite('Action_057_14', 9)	# 57-65
    sprite('Action_057_15', 4)	# 66-69
    sprite('Action_057_16', 4)	# 70-73
    sprite('Action_057_17', 3)	# 74-76

@State
def ThowExe_Down():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(1500)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackY(-8000)
        Hitstop(8)
        Unknown9154(45)
        AirUntechableTime(25)
        Unknown12051(2)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
    sprite('Action_058_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_058_01', 4)	# 6-9	 **attackbox here**
    sprite('Action_058_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_058_03', 2)	# 13-14	 **attackbox here**
    sprite('Action_058_04', 1)	# 15-15	 **attackbox here**
    sprite('Action_058_05', 1)	# 16-16	 **attackbox here**
    sprite('Action_058_05', 4)	# 17-20	 **attackbox here**
    StartMultihit()
    sprite('Action_058_06', 10)	# 21-30
    sprite('Action_058_07', 3)	# 31-33
    sprite('Action_058_08', 3)	# 34-36

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        Hitstop(7)
        AirUntechableTime(28)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(2800)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown11056(2)

        def upon_78():
            Unknown2038(1)

        def upon_43():
            if (SLOT_48 == 201):
                Unknown2038(1)
    sprite('Action_160_00', 6)	# 1-6
    sprite('Action_160_01', 5)	# 7-11
    GFX_0('UGO_Strike_SummonIn', 100)
    sprite('Action_160_02', 6)	# 12-17	 **attackbox here**
    sprite('Action_160_03', 3)	# 18-20	 **attackbox here**
    sprite('Action_160_04ex01', 4)	# 21-24	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    Unknown8004(0, 1, 0)
    ScreenShake(8000, 3500)
    sprite('Action_160_05', 4)	# 25-28	 **attackbox here**
    sprite('Action_160_06ex01', 2)	# 29-30	 **attackbox here**
    teleportRelativeX(35000)
    Unknown7006('ugo213_0', 100, 846161781, 828322609, 0, 0, 100, 846161781, 845099825, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_160_07ex01', 1)	# 31-31	 **attackbox here**
    setInvincible(0)
    teleportRelativeX(25000)
    sprite('Action_160_07ex01', 2)	# 32-33	 **attackbox here**
    teleportRelativeX(30000)
    sprite('Action_160_08ex01', 2)	# 34-35	 **attackbox here**
    teleportRelativeX(-55000)
    GFX_0('UGO_StrikeB_AtkCol', 100)
    AttackLevel_(2)
    Damage(300)
    Hitstop(1)
    AirUntechableTime(30)
    Unknown9016(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(20000)
    AirPushbackY(15000)
    Unknown30055('a08601004600000000000000')
    Unknown30056('706408004600000000000000')
    Unknown11058('0100000000000000000000000000000000000000')
    HitAirUnblockable(0)
    Unknown8001(3, 100)
    physicsXImpulse(17500)
    Unknown1028(-150)
    physicsYImpulse(28000)
    setGravity(1640)
    Unknown2016(400)
    Unknown2015(290)
    RefreshMultihit()
    sprite('Action_160_08ex01', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_08ex01', 2)	# 38-39	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_08ex01', 1)	# 40-40	 **attackbox here**
    sprite('Action_160_09ex01', 1)	# 41-41	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_09ex01', 1)	# 42-42	 **attackbox here**
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_09ex01', 1)	# 43-43	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_09ex01', 3)	# 44-46	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_10ex01', 10)	# 47-56	 **attackbox here**
    Unknown23027()
    teleportRelativeX(-8000)
    sprite('Action_160_11ex01', 3)	# 57-59	 **attackbox here**
    teleportRelativeX(-10000)
    loopRest()
    if SLOT_2:
        _gotolabel(100)
    clearUponHandler(78)
    clearUponHandler(43)
    sprite('Action_160_12', 4)	# 60-63
    Unknown23027()
    Unknown26('UGO_StrikeB_AtkCol')
    GFX_0('UGO_StrikeB_WeaponSummonOut', 100)
    sendToLabelUpon(2, 1)
    sprite('Action_022_00', 3)	# 64-66
    teleportRelativeX(70000)
    Unknown2016(-1)
    Unknown2015(-1)
    label(0)
    sprite('Action_022_01', 3)	# 67-69
    sprite('Action_022_00', 3)	# 70-72
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 5)	# 73-77
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('Action_021_01', 11)	# 78-88
    sprite('Action_021_02', 6)	# 89-94
    ExitState()
    label(100)
    sprite('Action_161_00', 3)	# 95-97	 **attackbox here**
    Unknown26('UGO_StrikeB_AtkCol')
    sprite('Action_161_01', 20)	# 98-117	 **attackbox here**
    physicsYImpulse(-26000)

    def upon_3():
        if (SLOT_23 <= 200000):
            sendToLabel(101)
    label(101)
    sprite('Action_161_02', 32767)	# 118-32884	 **attackbox here**
    clearUponHandler(3)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown2004(1, 0)
    sendToLabelUpon(2, 102)
    label(102)
    sprite('Action_161_03', 1)	# 32885-32885	 **attackbox here**
    Unknown1084(1)
    SFX_3('SE049_SpecialSwing')
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 0)
    Unknown2016(-1)
    Unknown2015(-1)
    sprite('Action_161_04', 5)	# 32886-32890	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 3500)
    AttackLevel_(4)
    Damage(1800)
    AirUntechableTime(26)
    HitAirUnblockable(0)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-25000)
    AirPushbackX(29000)
    YImpluseBeforeWallbounce(2800)
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    Unknown9310(1)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_161_04', 10)	# 32891-32900	 **attackbox here**
    Unknown23027()
    sprite('Action_161_05', 8)	# 32901-32908	 **attackbox here**
    sprite('Action_161_06', 7)	# 32909-32915	 **attackbox here**
    sprite('Action_161_07', 7)	# 32916-32922
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 6)	# 32923-32928
    sprite('Action_161_09', 6)	# 32929-32934

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(2)
        Damage(700)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(1)
        AirUntechableTime(60)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(15000)
        YImpluseBeforeWallbounce(2000)
        Unknown30055('a08601004600000000000000')
        Unknown30056('706408004600000000000000')
        Unknown11058('0100000000000000000000000000000000000000')
        HitAirUnblockable(0)
        Unknown2004(1, 0)
        Unknown1084(1)
        SLOT_59 = 1
        clearUponHandler(2)
        Unknown11056(2)
    sprite('Action_160_06ex01', 2)	# 1-2	 **attackbox here**
    sprite('Action_160_07ex01', 3)	# 3-5	 **attackbox here**
    Unknown7006('ugo213_0', 100, 846161781, 828322609, 0, 0, 100, 846161781, 845099825, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_160_08ex01', 4)	# 6-9	 **attackbox here**
    StartMultihit()
    sprite('Action_160_08ex01', 2)	# 10-11	 **attackbox here**
    SFX_0('002_highjump_1')
    GFX_0('UGO_StrikeB_AtkCol', 100)
    Unknown38(4, 1)
    Unknown4020(4)
    physicsXImpulse(11500)
    Unknown1028(-60)
    physicsYImpulse(25000)
    setGravity(1440)
    Unknown2016(400)
    Unknown2015(290)

    def upon_4():
        clearUponHandler(4)
        Unknown1028(0)
        Unknown1019(110)
    sprite('Action_160_08ex01', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_08ex01', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    sprite('Action_160_08ex01', 1)	# 16-16	 **attackbox here**
    sprite('Action_160_09ex01', 1)	# 17-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_09ex01', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_09ex01', 4)	# 20-23	 **attackbox here**
    RefreshMultihit()
    sprite('Action_160_10ex01', 10)	# 24-33	 **attackbox here**
    Unknown23027()
    teleportRelativeX(-8000)
    sprite('Action_160_11ex01', 3)	# 34-36	 **attackbox here**
    teleportRelativeX(-10000)
    loopRest()
    sprite('Action_160_12', 4)	# 37-40
    Unknown23027()
    Unknown4020(0)
    Unknown13(4)
    GFX_0('UGO_StrikeB_WeaponSummonOut', 100)
    sendToLabelUpon(2, 1)
    sprite('Action_022_00', 3)	# 41-43
    teleportRelativeX(75000)
    Unknown1007(50000)
    Unknown2016(-1)
    Unknown2015(-1)
    label(0)
    sprite('Action_022_01', 3)	# 44-46
    sprite('Action_022_00', 3)	# 47-49
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 5)	# 50-54
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    sprite('Action_021_01', 7)	# 55-61
    sprite('Action_021_02', 4)	# 62-65
    ExitState()

@Subroutine
def Assault_Atk():
    AttackLevel_(4)
    Damage(800)
    AttackP1(80)
    Unknown11092(1)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(12000)
    AirPushbackY(12000)
    AirUntechableTime(60)
    Hitstop(1)
    Unknown9016(1)
    Unknown11056(2)
    PushbackX(12000)
    Unknown30055('e09304003200000000000000')

@Subroutine
def Assault_FinishAtk():
    Damage(1600)
    AirPushbackX(24000)
    AirPushbackY(24000)
    Hitstop(12)
    PushbackX(30400)
    Unknown30055('000000000000000000000000')

@State
def AssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Atk')
    sprite('Action_115_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_115_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_115_02', 2)	# 7-8	 **attackbox here**
    Unknown7006('ugo200_0', 100, 846161781, 828321840, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    teleportRelativeX(50000)
    sprite('Action_115_02', 2)	# 9-10	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 11-12	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 13-14	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 15-16	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    sprite('Action_115_05', 2)	# 17-18	 **attackbox here**
    sprite('Action_115_06', 2)	# 19-20	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 2)	# 21-22	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 2)	# 23-24	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 2)	# 25-26	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 2)	# 27-28	 **attackbox here**
    sprite('Action_115_11', 3)	# 29-31	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    callSubroutine('Assault_FinishAtk')
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 6)	# 32-37	 **attackbox here**
    Recovery()
    sprite('Action_115_13', 6)	# 38-43	 **attackbox here**
    sprite('Action_115_14', 6)	# 44-49	 **attackbox here**
    sprite('Action_115_15', 4)	# 50-53
    GFX_0('UGO_Invincible_SummonOut', 100)
    sprite('Action_115_16', 4)	# 54-57

@State
def AssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Atk')
    sprite('Action_115_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_115_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_115_02', 2)	# 11-12	 **attackbox here**
    Unknown7006('ugo200_0', 100, 846161781, 828321840, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    teleportRelativeX(50000)
    sprite('Action_115_02', 2)	# 13-14	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 15-16	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 17-18	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 19-20	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    sprite('Action_115_05', 2)	# 21-22	 **attackbox here**
    sprite('Action_115_06', 2)	# 23-24	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 2)	# 25-26	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 2)	# 27-28	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 2)	# 29-30	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 2)	# 31-32	 **attackbox here**
    sprite('Action_115_11', 3)	# 33-35	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 2)	# 36-37	 **attackbox here**
    sprite('Action_115_13', 2)	# 38-39	 **attackbox here**
    sprite('Action_115_03', 1)	# 40-40	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 41-42	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    teleportRelativeX(50000)
    RefreshMultihit()
    sprite('Action_115_05', 2)	# 43-44	 **attackbox here**
    sprite('Action_115_06', 2)	# 45-46	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 47-47	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 2)	# 48-49	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 2)	# 50-51	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 2)	# 52-53	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 2)	# 54-55	 **attackbox here**
    sprite('Action_115_11', 3)	# 56-58	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    callSubroutine('Assault_FinishAtk')
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 7)	# 59-65	 **attackbox here**
    Recovery()
    sprite('Action_115_13', 10)	# 66-75	 **attackbox here**
    sprite('Action_115_14', 7)	# 76-82	 **attackbox here**
    sprite('Action_115_15', 4)	# 83-86
    GFX_0('UGO_Invincible_SummonOut', 100)
    sprite('Action_115_16', 4)	# 87-90

@State
def DrainA_LandThrow():

    def upon_IMMEDIATE():
        Unknown17011('DrainA_LandThrow_Exe', 2, 0, 0)
        Damage(800)
        AttackP2(100)
        Unknown11091(5)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11054(-1)
        JumpCancel_(0)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11032('90d0030001000000ffffffffffffffff')
        Unknown9266(12)
    sprite('Action_197_00', 3)	# 1-3
    GFX_0('UGO_DrainThrow_AuraA', 0)
    sprite('Action_197_01', 3)	# 4-6
    sprite('Action_197_02', 2)	# 7-8
    sprite('Action_197_03', 2)	# 9-10
    SFX_3('SE042')
    GFX_0('UGO_DrainThrow_LandZanzou', 100)
    sprite('Action_197_04', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('Action_197_05', 1)	# 12-12	 **attackbox here**
    sprite('Action_197_06', 4)	# 13-16
    Unknown7006('ugo212_0', 100, 846161781, 828322353, 0, 0, 100, 846161781, 845099569, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_197_07', 5)	# 17-21
    sprite('Action_197_08', 3)	# 22-24
    sprite('Action_197_09', 11)	# 25-35
    sprite('Action_197_10', 5)	# 36-40
    sprite('Action_197_11', 5)	# 41-45

@State
def DrainA_LandThrow_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        PushbackX(45000)
        AttackP2(50)
        Unknown11091(5)
        Unknown9016(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(1)
        Hitstop(1)
        Unknown9154(20)
        Unknown30068(1)
        setInvincible(1)
        Unknown30048(1)
        Unknown13045(0)
        Unknown11044(1)
        Unknown9266(12)
        Unknown11068(1)

        def upon_78():
            Unknown2058(250)
            Unknown36(22)
            Unknown2058(-500)
            Unknown35()
    sprite('Action_198_00', 4)	# 1-4	 **attackbox here**
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    StartMultihit()
    sprite('Action_198_01', 10)	# 5-14
    Unknown7006('ugo209_0', 100, 846161781, 828324144, 0, 0, 100, 846161781, 845101360, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_198_02', 8)	# 15-22
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_198_03', 7)	# 23-29
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('UGO_DrainThrow_HitAura', 0)
    sprite('Action_198_04', 4)	# 30-33	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE008')
    GFX_0('UGO_Drain_Steal', 0)
    GFX_0('UGO_Drain_Yoin', 100)
    sprite('Action_198_05', 18)	# 34-51
    sprite('Action_198_06', 6)	# 52-57
    sprite('Action_198_07', 5)	# 58-62

@State
def DrainB_AirThrow():

    def upon_IMMEDIATE():
        Unknown17011('DrainB_AirThrow_Exe', 2, 0, 0)
        Unknown12051(2)
        Damage(1000)
        AttackP2(100)
        Unknown11091(5)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11054(-1)
        Unknown11045(0)
        Unknown11046(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11032('90d0030001000000ffffffffffffffff')
        Unknown9266(12)
    sprite('Action_195_00', 2)	# 1-2
    GFX_0('UGO_DrainThrow_AuraB', 0)
    sprite('Action_195_01', 2)	# 3-4
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_195_02', 2)	# 5-6
    SFX_3('SE042')
    GFX_0('UGO_DrainThrow_AntiAirZanzou', 100)
    sprite('Action_195_03', 4)	# 7-10	 **attackbox here**
    GFX_0('UGO_DrainThrow_AuraB_2', 0)
    RefreshMultihit()
    sprite('Action_195_04', 4)	# 11-14
    Unknown7006('ugo212_0', 100, 846161781, 828322353, 0, 0, 100, 846161781, 845099569, 0, 0, 100, 0, 0, 0, 0, 0)
    setInvincible(0)
    sprite('Action_195_05', 5)	# 15-19
    sprite('Action_195_06', 5)	# 20-24
    sprite('Action_195_07', 10)	# 25-34
    sprite('Action_195_08', 5)	# 35-39
    sprite('Action_195_09', 5)	# 40-44

@State
def DrainB_AirThrow_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1750)
        AttackP2(50)
        Unknown11091(5)
        Unknown9016(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Hitstop(1)
        AirUntechableTime(40)
        Unknown30068(1)
        setInvincible(1)
        Unknown30048(1)
        Unknown13045(0)
        Unknown11044(1)
        Unknown9266(12)
        Unknown11068(1)
        Unknown11072(1, 140000, 134000)

        def upon_78():
            Unknown2058(250)
            Unknown36(22)
            Unknown2058(-500)
            Unknown35()
    sprite('Action_196_00', 4)	# 1-4	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    StartMultihit()
    sprite('Action_196_01', 10)	# 5-14
    Unknown7006('ugo209_0', 100, 846161781, 828324144, 0, 0, 100, 846161781, 845101360, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_196_02', 8)	# 15-22
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_196_03', 7)	# 23-29
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('UGO_DrainThrow_HitAura', 0)
    sprite('Action_196_04', 4)	# 30-33	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE008')
    GFX_0('UGO_Drain_Steal', 0)
    GFX_0('UGO_Drain_Yoin', 100)
    sprite('Action_196_05', 14)	# 34-47
    sprite('Action_196_06', 7)	# 48-54
    sprite('Action_196_07', 6)	# 55-60

@State
def StrikeA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Unknown11028(20)
        AirUntechableTime(28)
        YImpluseBeforeWallbounce(2800)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
    sprite('Action_156_00', 6)	# 1-6
    sprite('Action_156_01', 5)	# 7-11
    GFX_0('UGO_Strike_SummonIn', 100)
    sprite('Action_156_02', 6)	# 12-17	 **attackbox here**
    sprite('Action_156_03', 3)	# 18-20	 **attackbox here**
    sprite('Action_156_04', 3)	# 21-23	 **attackbox here**
    RefreshMultihit()
    ScreenShake(11000, 5000)
    GFX_0('UGO_StrikeA_Inpact', 0)
    sprite('Action_156_05', 10)	# 24-33	 **attackbox here**
    Recovery()
    sprite('Action_156_06', 5)	# 34-38
    GFX_0('UGO_StrikeA_SummonOut', 100)

@State
def StrikeB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        Hitstop(7)
        AirUntechableTime(28)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(2800)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown2004(1, 0)
    sprite('Action_160_00', 3)	# 1-3
    sprite('Action_160_01', 5)	# 4-8
    GFX_0('UGO_Strike_SummonIn', 100)
    sprite('Action_160_02', 3)	# 9-11	 **attackbox here**
    sprite('Action_160_03', 2)	# 12-13	 **attackbox here**
    sprite('Action_160_04', 4)	# 14-17	 **attackbox here**
    ScreenShake(8000, 3500)
    sprite('Action_160_05', 4)	# 18-21	 **attackbox here**
    sprite('Action_160_06', 2)	# 22-23	 **attackbox here**
    sprite('Action_160_07', 3)	# 24-26	 **attackbox here**
    sprite('Action_160_08', 7)	# 27-33
    GFX_0('UGO_StrikeB_AtkCol', 100)
    Unknown8001(3, 100)
    physicsXImpulse(17000)
    Unknown1028(-100)
    physicsYImpulse(16000)
    setGravity(1140)
    Unknown2016(400)
    if CheckInput(0x79):
        Unknown1015(10000)
    if CheckInput(0x5f):
        Unknown1015(-5000)
    sprite('Action_160_09', 6)	# 34-39
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_10', 10)	# 40-49
    teleportRelativeX(-8000)
    sprite('Action_160_11', 3)	# 50-52
    teleportRelativeX(-10000)
    loopRest()
    sprite('Action_161_00', 3)	# 53-55	 **attackbox here**
    sprite('Action_161_01', 20)	# 56-75	 **attackbox here**
    sendToLabelUpon(2, 1)
    physicsYImpulse(-26000)
    label(1)
    sprite('Action_161_02', 3)	# 76-78	 **attackbox here**
    Unknown2016(-1)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    sprite('Action_161_03', 1)	# 79-79	 **attackbox here**
    sprite('Action_161_04', 5)	# 80-84	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 3500)
    Damage(1200)
    AirUntechableTime(26)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-25000)
    AirPushbackX(29000)
    YImpluseBeforeWallbounce(2800)
    Unknown9310(1)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_161_05', 8)	# 85-92	 **attackbox here**
    sprite('Action_161_06', 7)	# 93-99	 **attackbox here**
    sprite('Action_161_07', 7)	# 100-106
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 6)	# 107-112
    sprite('Action_161_09', 6)	# 113-118

@State
def AirAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AirUntechableTime(20)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        PushbackX(21000)
    sprite('Action_180_00', 3)	# 1-3	 **attackbox here**
    if (SLOT_12 >= 0):
        Unknown1019(0)
    physicsYImpulse(5000)
    setGravity(50)
    sprite('Action_180_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_180_02', 1)	# 6-6	 **attackbox here**
    sprite('Action_180_03', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_180_04', 3)	# 9-11	 **attackbox here**
    sprite('Action_180_05', 5)	# 12-16	 **attackbox here**
    sprite('Action_180_06', 2)	# 17-18	 **attackbox here**
    GFX_0('UGO_AirAssaultA_AtkCol', 100)
    sprite('Action_180_07', 3)	# 19-21	 **attackbox here**
    Unknown1021(16000)
    setGravity(2500)
    sprite('Action_180_08', 5)	# 22-26	 **attackbox here**
    sprite('Action_180_09', 9)	# 27-35	 **attackbox here**
    sprite('Action_180_10', 4)	# 36-39
    sprite('Action_180_11', 5)	# 40-44
    sprite('Action_180_12', 5)	# 45-49

@State
def AirAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AirUntechableTime(20)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        PushbackX(21000)
    sprite('Action_180_00', 3)	# 1-3	 **attackbox here**
    if (SLOT_12 >= 0):
        Unknown1019(0)
    physicsYImpulse(5000)
    setGravity(50)
    sprite('Action_180_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_180_02', 1)	# 6-6	 **attackbox here**
    sprite('Action_180_03', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    sprite('Action_180_04', 3)	# 9-11	 **attackbox here**
    sprite('Action_180_05', 5)	# 12-16	 **attackbox here**
    sprite('Action_180_06', 2)	# 17-18	 **attackbox here**
    GFX_0('UGO_AirAssaultA_AtkCol', 100)
    sprite('Action_180_07', 3)	# 19-21	 **attackbox here**
    if (SLOT_12 <= 0):
        Unknown1019(0)
    Unknown1015(-25000)
    Unknown1028(600)
    Unknown1021(28000)
    setGravity(2500)
    sprite('Action_180_08', 5)	# 22-26	 **attackbox here**
    sprite('Action_180_09', 9)	# 27-35	 **attackbox here**
    sprite('Action_180_10', 4)	# 36-39
    sprite('Action_180_11', 5)	# 40-44
    sprite('Action_180_12', 5)	# 45-49

@State
def AirStrikeA():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown1084(1)
        SLOT_59 = 1
    sprite('Action_160_06ex01', 2)	# 1-2	 **attackbox here**
    sprite('Action_160_07ex01', 3)	# 3-5	 **attackbox here**
    sprite('Action_160_08ex01', 7)	# 6-12	 **attackbox here**
    GFX_0('UGO_AirStrikeA_AtkCol', 100)
    physicsXImpulse(17000)
    Unknown1028(-100)
    physicsYImpulse(16000)
    setGravity(1140)
    Unknown2016(400)
    sprite('Action_160_09ex01', 6)	# 13-18	 **attackbox here**
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_10ex01', 10)	# 19-28	 **attackbox here**
    teleportRelativeX(-8000)
    sprite('Action_160_11ex01', 3)	# 29-31	 **attackbox here**
    teleportRelativeX(-10000)
    loopRest()

@State
def AirStrikeB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        AirUntechableTime(26)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackY(-25000)
        AirPushbackX(29000)
        YImpluseBeforeWallbounce(2800)
        Unknown9310(1)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown2004(1, 0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown1084(1)
        SLOT_59 = 1
    sprite('Action_160_06ex01', 4)	# 1-4	 **attackbox here**
    sprite('Action_160_07ex01', 6)	# 5-10	 **attackbox here**
    sprite('Action_160_08ex01', 4)	# 11-14	 **attackbox here**
    sprite('Action_160_08ex01', 7)	# 15-21	 **attackbox here**
    GFX_0('UGO_AirStrikeB_AtkCol', 100)
    physicsXImpulse(17000)
    Unknown1028(-100)
    physicsYImpulse(16000)
    setGravity(1140)
    Unknown2016(400)
    Unknown2015(200)
    sprite('Action_160_09ex01', 6)	# 22-27	 **attackbox here**
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_10ex01', 10)	# 28-37	 **attackbox here**
    teleportRelativeX(-8000)
    sprite('Action_160_11ex01', 3)	# 38-40	 **attackbox here**
    teleportRelativeX(-10000)
    loopRest()
    sprite('Action_161_00ex01', 3)	# 41-43
    sprite('Action_161_01ex01', 32767)	# 44-32810
    physicsYImpulse(-41000)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_161_02', 3)	# 32811-32813	 **attackbox here**
    Unknown2016(-1)
    Unknown2015(-1)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    sprite('Action_161_03', 1)	# 32814-32814	 **attackbox here**
    sprite('Action_161_04', 5)	# 32815-32819	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 3500)
    sprite('Action_161_05', 8)	# 32820-32827	 **attackbox here**
    sprite('Action_161_06', 7)	# 32828-32834	 **attackbox here**
    sprite('Action_161_07', 7)	# 32835-32841
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 6)	# 32842-32847
    sprite('Action_161_09', 6)	# 32848-32853

@State
def Scratch():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('Action_234_00', 3)	# 1-3	 **attackbox here**
    Unknown1084(1)
    sprite('Action_234_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_234_02', 4)	# 7-10	 **attackbox here**
    sprite('Action_234_03', 5)	# 11-15	 **attackbox here**
    sprite('Action_234_04', 4)	# 16-19	 **attackbox here**
    sprite('Action_234_05', 3)	# 20-22	 **attackbox here**
    GFX_0('UGO_Scratch_AtkCol', 100)
    sprite('Action_234_06', 4)	# 23-26	 **attackbox here**
    sprite('Action_234_07', 4)	# 27-30	 **attackbox here**
    sprite('Action_234_08', 5)	# 31-35	 **attackbox here**
    sprite('Action_234_09', 6)	# 36-41
    sprite('Action_234_10', 4)	# 42-45
    sprite('Action_234_11', 3)	# 46-48

@State
def AssaultEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assault_Atk')
        PushbackX(39900)
        Unknown30065(0)
        Unknown11091(10)
    sprite('Action_115_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_115_01', 3)	# 4-6	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_115_02', 2)	# 7-8	 **attackbox here**
    SFX_1('ugo200_2')
    teleportRelativeX(50000)
    sprite('Action_115_02', 2)	# 9-10	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 11-12	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 13-14	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    sprite('Action_115_05', 1)	# 15-15	 **attackbox here**
    sprite('Action_115_06', 1)	# 16-16	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 17-17	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 18-18	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 1)	# 19-19	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 1)	# 20-20	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 1)	# 21-21	 **attackbox here**
    sprite('Action_115_11', 3)	# 22-24	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 1)	# 25-25	 **attackbox here**
    sprite('Action_115_13', 1)	# 26-26	 **attackbox here**
    sprite('Action_115_03', 1)	# 27-27	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 28-29	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    teleportRelativeX(50000)
    RefreshMultihit()
    sprite('Action_115_05', 2)	# 30-31	 **attackbox here**
    sprite('Action_115_06', 2)	# 32-33	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 34-34	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 2)	# 35-36	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 2)	# 37-38	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 2)	# 39-40	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 2)	# 41-42	 **attackbox here**
    sprite('Action_115_11', 3)	# 43-45	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 1)	# 46-46	 **attackbox here**
    sprite('Action_115_13', 1)	# 47-47	 **attackbox here**
    sprite('Action_115_03', 1)	# 48-48	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 49-50	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    teleportRelativeX(50000)
    RefreshMultihit()
    sprite('Action_115_05', 2)	# 51-52	 **attackbox here**
    sprite('Action_115_06', 2)	# 53-54	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 55-55	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 2)	# 56-57	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 2)	# 58-59	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 2)	# 60-61	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 2)	# 62-63	 **attackbox here**
    sprite('Action_115_11', 3)	# 64-66	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    callSubroutine('Assault_FinishAtk')
    PushbackX(39900)
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 6)	# 67-72	 **attackbox here**
    Recovery()
    sprite('Action_115_13', 9)	# 73-81	 **attackbox here**
    sprite('Action_115_14', 6)	# 82-87	 **attackbox here**
    sprite('Action_115_15', 4)	# 88-91
    GFX_0('UGO_Invincible_SummonOut', 100)
    sprite('Action_115_16', 4)	# 92-95

@State
def DrainEx():

    def upon_IMMEDIATE():
        Unknown17011('DrainEx_Exe1', 2, 0, 0)
        Damage(800)
        AttackP2(100)
        Unknown30065(0)
        Unknown11091(10)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11045(1)
        Unknown11046(0)
        Unknown30048(1)
        Unknown11064(1)
        Unknown11032('00e2040001000000ffffffffffffffff')

        def upon_3():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_51:
                Unknown11045(0)
            else:
                Unknown11045(1)
    sprite('Action_204_00', 3)	# 1-3
    sprite('Action_204_01', 4)	# 4-7
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_204_02', 4)	# 8-11
    sprite('Action_204_03', 1)	# 12-12	 **attackbox here**
    RefreshMultihit()
    GFX_0('UGO_DrainThrow_Aura_Catch', 0)
    SFX_3('SE043')
    sprite('Action_204_04', 1)	# 13-13	 **attackbox here**
    sprite('Action_204_05', 8)	# 14-21
    clearUponHandler(3)
    Unknown7006('ugo212_0', 100, 846161781, 828322353, 0, 0, 100, 846161781, 845099569, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_204_06', 6)	# 22-27
    sprite('Action_204_07', 6)	# 28-33
    sprite('Action_204_08', 5)	# 34-38

@State
def DrainEx_Exe1():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Damage(0)
        AttackP2(100)
        Unknown11091(10)
        Unknown30065(0)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Hitstop(0)
        Unknown9154(50)
        Unknown28(78, 'DrainEx_Exe2')
        Unknown30068(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown13045(0)
        Unknown11068(1)
        Unknown11044(1)
        setInvincible(1)
    sprite('Action_205_00', 5)	# 1-5	 **attackbox here**
    tag_voice(1, 'ugo210_0', 'ugo210_1', 'ugo210_2', '')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    Unknown23027()
    sprite('Action_205_01', 5)	# 6-10
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_205_02', 5)	# 11-15
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_205_03', 5)	# 16-20
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_205_04', 20)	# 21-40
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(0, 80)
    GFX_0('UGO_DrainThrow_AuraEx', 1)
    sprite('Action_205_05', 5)	# 41-45
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('Action_205_06', 3)	# 46-48	 **attackbox here**
    teleportRelativeX(60000)
    RefreshMultihit()
    SFX_3('SE042')
    tag_voice(0, 'ugo211_0', 'ugo211_1', 'ugo211_2', '')
    GFX_0('UGO_DrainThrow_LandZanzou', 100)
    sprite('Action_205_06', 1)	# 49-49	 **attackbox here**

@State
def DrainEx_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('DrainEx_Exe3', 2, 0, 0)
        Damage(1000)
        AttackP2(100)
        Unknown11091(10)
        Unknown30065(0)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Hitstop(1)
        Unknown30068(1)
        setInvincible(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown13045(0)
        Unknown11044(1)
        Unknown9266(12)
        Unknown11068(1)
    sprite('Action_205_07', 4)	# 1-4	 **attackbox here**
    RefreshMultihit()
    loopRest()

@State
def DrainEx_Exe3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        PushbackX(45000)
        AttackP2(50)
        Unknown11091(10)
        Unknown30065(0)
        Unknown9016(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(1)
        Hitstop(1)
        Unknown9154(20)
        Unknown30068(1)
        setInvincible(1)
        Unknown30048(1)
        Unknown13045(0)
        Unknown11044(1)
        Unknown9266(12)
        Unknown11068(1)

        def upon_78():
            Unknown2058(1250)
            Unknown36(22)
            Unknown2058(-1000)
            Unknown35()
    sprite('Action_205_08', 10)	# 1-10	 **attackbox here**
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    StartMultihit()
    sprite('Action_205_09', 8)	# 11-18
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_205_10', 7)	# 19-25
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('UGO_DrainThrow_HitAura', 0)
    sprite('Action_205_11', 4)	# 26-29	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE008')
    GFX_0('UGO_Drain_Steal', 0)
    GFX_0('UGO_Drain_Yoin', 100)
    sprite('Action_205_12', 18)	# 30-47
    sprite('Action_205_13', 6)	# 48-53
    sprite('Action_205_14', 5)	# 54-58

@State
def StrikeEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        Hitstop(7)
        AirUntechableTime(28)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(2800)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown2004(1, 0)
    sprite('Action_160_00', 2)	# 1-2
    sprite('Action_160_01', 1)	# 3-3
    GFX_0('UGO_Strike_SummonIn', 100)
    sprite('Action_160_01', 2)	# 4-5
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_160_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_160_03', 2)	# 8-9	 **attackbox here**
    sprite('Action_160_04', 5)	# 10-14	 **attackbox here**
    ScreenShake(8000, 3500)
    sprite('Action_160_05', 8)	# 15-22	 **attackbox here**
    sprite('Action_160_06', 4)	# 23-26	 **attackbox here**
    sprite('Action_160_08', 3)	# 27-29
    GFX_0('UGO_StrikeEx_AtkCol', 100)
    Unknown8001(3, 100)
    physicsXImpulse(18000)
    Unknown1028(-90)
    physicsYImpulse(21000)
    setGravity(500)
    Unknown2016(400)
    if CheckInput(0x79):
        Unknown1015(10000)
    if CheckInput(0x5f):
        Unknown1015(-5000)
    sprite('Action_160_09', 11)	# 30-40
    if CheckInput(0x5f):
        Unknown1015(-5000)
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_10', 10)	# 41-50
    teleportRelativeX(-8000)
    sprite('Action_160_11', 6)	# 51-56
    teleportRelativeX(-10000)
    loopRest()
    sprite('Action_161_00', 3)	# 57-59	 **attackbox here**
    sprite('Action_161_01', 20)	# 60-79	 **attackbox here**
    sendToLabelUpon(2, 1)
    physicsYImpulse(-26000)
    label(1)
    sprite('Action_161_02', 3)	# 80-82	 **attackbox here**
    Unknown2016(-1)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    sprite('Action_161_03', 1)	# 83-83	 **attackbox here**
    sprite('Action_161_04', 5)	# 84-88	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 3500)
    Damage(1200)
    AirUntechableTime(26)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-25000)
    AirPushbackX(29000)
    YImpluseBeforeWallbounce(2800)
    Unknown9310(1)
    sprite('Action_161_05', 8)	# 89-96	 **attackbox here**
    sprite('Action_161_06', 7)	# 97-103	 **attackbox here**
    sprite('Action_161_07', 7)	# 104-110
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 6)	# 111-116
    sprite('Action_161_09', 6)	# 117-122

@State
def AirAssaultEx():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AirUntechableTime(20)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        callSubroutine('ExFlash')
    sprite('Action_180_00', 2)	# 1-2	 **attackbox here**
    Unknown1084(1)
    setGravity(0)
    sprite('Action_180_01', 1)	# 3-3	 **attackbox here**
    sprite('Action_180_01', 1)	# 4-4	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_180_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_180_03', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    sprite('Action_180_04', 2)	# 10-11	 **attackbox here**
    sprite('Action_180_05', 2)	# 12-13	 **attackbox here**
    sprite('Action_180_06', 1)	# 14-14	 **attackbox here**
    GFX_0('UGO_AirAssaultEx_AtkCol1', 100)
    sprite('Action_180_06', 1)	# 15-15	 **attackbox here**
    GFX_0('UGO_AirAssaultEx_AtkCol2', 100)
    sprite('Action_180_07', 3)	# 16-18	 **attackbox here**
    Unknown1015(-10000)
    Unknown1021(20000)
    setGravity(2500)
    sprite('Action_180_08', 5)	# 19-23	 **attackbox here**
    sprite('Action_180_09', 9)	# 24-32	 **attackbox here**
    sprite('Action_180_10', 4)	# 33-36
    sprite('Action_180_11', 5)	# 37-41
    sprite('Action_180_12', 5)	# 42-46

@State
def AirStrikeEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        Hitstop(7)
        AirUntechableTime(28)
        AirPushbackY(35000)
        YImpluseBeforeWallbounce(2800)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown2004(1, 0)
        Unknown1084(1)
        SLOT_59 = 1
        callSubroutine('ExFlash')
    sprite('Action_160_06ex01', 2)	# 1-2	 **attackbox here**
    sprite('Action_160_07ex01', 1)	# 3-3	 **attackbox here**
    sprite('Action_160_07ex01', 2)	# 4-5	 **attackbox here**
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_160_08ex01', 7)	# 6-12	 **attackbox here**
    GFX_0('UGO_AirStrikeEx_AtkCol', 100)
    physicsXImpulse(18000)
    Unknown1028(-90)
    physicsYImpulse(21000)
    setGravity(500)
    Unknown2016(400)
    Unknown2015(200)
    sprite('Action_160_09ex01', 11)	# 13-23	 **attackbox here**
    teleportRelativeX(-13000)
    loopRest()
    sprite('Action_160_10ex01', 10)	# 24-33	 **attackbox here**
    teleportRelativeX(-8000)
    sprite('Action_160_11ex01', 3)	# 34-36	 **attackbox here**
    teleportRelativeX(-10000)
    loopRest()
    sprite('Action_161_00ex01', 6)	# 37-42
    sprite('Action_161_01ex01', 32767)	# 43-32809
    physicsYImpulse(-41000)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_161_02', 3)	# 32810-32812	 **attackbox here**
    Unknown2016(-1)
    Unknown2015(-1)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown1084(1)
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    sprite('Action_161_03', 1)	# 32813-32813	 **attackbox here**
    sprite('Action_161_04', 5)	# 32814-32818	 **attackbox here**
    RefreshMultihit()
    ScreenShake(8000, 3500)
    Damage(1200)
    AirUntechableTime(26)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackY(-25000)
    AirPushbackX(29000)
    YImpluseBeforeWallbounce(2800)
    Unknown9310(1)
    sprite('Action_161_05', 8)	# 32819-32826	 **attackbox here**
    sprite('Action_161_06', 7)	# 32827-32833	 **attackbox here**
    sprite('Action_161_07', 7)	# 32834-32840
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 6)	# 32841-32846
    sprite('Action_161_09', 6)	# 32847-32852

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(10)
        AttackP2(60)
        Unknown11092(1)
        Unknown9016(1)
        setInvincible(1)
        Hitstop(5)
        Unknown11001(3, 3, 3)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        PushbackX(12500)
        Unknown11032('40420f0000000000ffffffffffffffff')

        def upon_78():
            Unknown13024(0)
        Unknown11064(1)
    sprite('Action_240_00', 7)	# 1-7
    Unknown2036(57, -1, 0)
    Unknown2058(-10000)
    GFX_0('UGO_UltimateAssault_Start', 100)
    Unknown30080('')
    sprite('Action_240_01', 5)	# 8-12
    tag_voice(1, 'ugo250_0', 'ugo250_1', '', '')
    sprite('Action_240_02', 5)	# 13-17
    sprite('Action_240_01', 5)	# 18-22
    sprite('Action_240_02', 5)	# 23-27
    sprite('Action_240_01', 5)	# 28-32
    sprite('Action_240_02', 5)	# 33-37
    sprite('Action_240_01', 5)	# 38-42
    sprite('Action_240_02', 5)	# 43-47
    sprite('Action_240_01', 5)	# 48-52
    sprite('Action_240_02', 5)	# 53-57
    sprite('Action_240_03', 4)	# 58-61	 **attackbox here**
    sprite('Action_240_04', 5)	# 62-66	 **attackbox here**
    Unknown21015('55474f5f556c74696d61746541737361756c745f537461727400000000000000f501000000000000')
    sprite('Action_240_05', 3)	# 67-69	 **attackbox here**
    sprite('Action_240_06', 2)	# 70-71	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff1', 100)
    sprite('Action_240_07', 3)	# 72-74	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 12000)
    AirPushbackX(9000)
    AirPushbackY(25000)
    Unknown2015(300)
    sprite('Action_240_08', 4)	# 75-78	 **attackbox here**
    sprite('Action_240_09', 5)	# 79-83	 **attackbox here**
    setInvincible(0)
    tag_voice(0, 'ugo251_0', 'ugo251_1', '', '')
    physicsXImpulse(5120)
    teleportRelativeX(30000)
    sprite('Action_240_10', 3)	# 84-86	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff2', 100)
    teleportRelativeX(40000)
    sprite('Action_240_11', 3)	# 87-89	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 9000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(3000)
    AirPushbackY(12000)
    sprite('Action_240_12', 4)	# 90-93	 **attackbox here**
    Unknown1084(1)
    sprite('Action_240_13', 5)	# 94-98	 **attackbox here**
    sprite('Action_240_14', 2)	# 99-100	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff3', 100)
    sprite('Action_240_15', 4)	# 101-104	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 120000)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(1)
    sprite('Action_240_16', 5)	# 105-109	 **attackbox here**
    sprite('Action_240_17', 5)	# 110-114	 **attackbox here**
    sprite('Action_240_18', 3)	# 115-117	 **attackbox here**
    sprite('Action_240_19', 2)	# 118-119	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff4', 100)
    sprite('Action_240_20', 6)	# 120-125	 **attackbox here**
    RefreshMultihit()
    Hitstop(13)
    Unknown11072(1, 400000, 200000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(6000)
    AirPushbackY(28000)
    sprite('Action_240_21', 11)	# 126-136	 **attackbox here**
    sprite('Action_240_22', 6)	# 137-142	 **attackbox here**
    sprite('Action_240_23', 5)	# 143-147	 **attackbox here**
    physicsXImpulse(22000)
    Unknown1028(3000)
    sprite('Action_240_24', 2)	# 148-149	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff5', 100)
    sprite('Action_240_25', 5)	# 150-154	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11072(0, -1, -1)
    Unknown11001(0, 0, 0)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    YImpluseBeforeWallbounce(200)
    AirPushbackX(0)
    AirPushbackY(5000)
    Unknown1084(1)
    sprite('Action_240_26', 5)	# 155-159	 **attackbox here**
    sprite('Action_240_27', 4)	# 160-163
    GFX_0('UGO_Ultimate_AtkCol_0', 0)
    physicsXImpulse(18000)
    sprite('Action_240_28ex01', 3)	# 164-166	 **attackbox here**
    RefreshMultihit()
    GFX_0('UGO_Ultimate_AtkCol_1', 0)
    AttackLevel_(4)
    Damage(1000)
    Unknown11091(10)
    Hitstop(1)
    Unknown11072(1, 250000, 327400)
    Unknown11001(-1, -1, -1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(9000)
    AirPushbackY(600)
    PushbackX(3000)
    YImpluseBeforeWallbounce(2000)
    Unknown2038(2)

    def upon_78():
        Unknown2038(-1)
        if (not SLOT_2):
            clearUponHandler(78)
            Unknown11072(0, -1, -1)
    sprite('Action_240_28ex01', 1)	# 167-167	 **attackbox here**
    sprite('Action_240_29ex01', 2)	# 168-169	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('Action_240_29ex01', 3)	# 170-172	 **attackbox here**
    sprite('Action_240_30ex01', 3)	# 173-175	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 7)	# 176-182	 **attackbox here**
    clearUponHandler(78)
    Unknown11072(0, -1, -1)
    Unknown23027()
    sprite('Action_240_30', 4)	# 183-186
    sprite('Action_240_31', 4)	# 187-190	 **attackbox here**
    Unknown26('UGO_Ultimate_AtkCol_1')
    tag_voice(0, 'ugo252_0', 'ugo252_1', '', '')
    GFX_0('UGO_UltimateAssault_AtkEff_Fini', 100)
    teleportRelativeX(-50000)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_32', 3)	# 191-193	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Damage(4000)
    Unknown11072(0, -1, -1)
    Unknown11091(20)
    Unknown11001(0, 0, 0)
    Hitstop(30)
    AirPushbackX(65000)
    AirPushbackY(500)
    YImpluseBeforeWallbounce(50)
    PushbackX(19800)
    Unknown11064(0)

    def upon_12():
        SFX_3('SE005')
        SFX_3('SE_BigBomb')
        Unknown13024(1)
    sprite('Action_240_33', 19)	# 194-212	 **attackbox here**
    Unknown2015(0)
    Unknown23027()
    Unknown13024(1)
    sprite('Action_240_34', 8)	# 213-220
    sprite('Action_240_35', 7)	# 221-227
    teleportRelativeX(-30000)
    loopRest()

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(1000)
        Unknown11091(10)
        AttackP2(60)
        Unknown11092(1)
        Unknown9016(1)
        setInvincible(1)
        Hitstop(5)
        Unknown11001(3, 3, 3)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        PushbackX(12500)
        Unknown11032('40420f0000000000ffffffffffffffff')

        def upon_78():
            Unknown13024(0)
        Unknown11064(1)
    sprite('Action_240_00', 7)	# 1-7
    Unknown2036(57, -1, 0)
    Unknown2058(-10000)
    GFX_0('UGO_UltimateAssault_Start', 100)
    Unknown30080('')
    sprite('Action_240_01', 5)	# 8-12
    tag_voice(1, 'ugo250_0', 'ugo250_1', '', '')
    sprite('Action_240_02', 5)	# 13-17
    sprite('Action_240_01', 5)	# 18-22
    sprite('Action_240_02', 5)	# 23-27
    sprite('Action_240_01', 5)	# 28-32
    sprite('Action_240_02', 5)	# 33-37
    sprite('Action_240_01', 5)	# 38-42
    sprite('Action_240_02', 5)	# 43-47
    sprite('Action_240_01', 5)	# 48-52
    sprite('Action_240_02', 5)	# 53-57
    sprite('Action_240_03', 4)	# 58-61	 **attackbox here**
    sprite('Action_240_04', 5)	# 62-66	 **attackbox here**
    Unknown21015('55474f5f556c74696d61746541737361756c745f537461727400000000000000f501000000000000')
    sprite('Action_240_05', 3)	# 67-69	 **attackbox here**
    sprite('Action_240_06', 2)	# 70-71	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff1', 100)
    sprite('Action_240_07', 3)	# 72-74	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 12000)
    AirPushbackX(9000)
    AirPushbackY(25000)
    Unknown2015(300)
    sprite('Action_240_08', 4)	# 75-78	 **attackbox here**
    sprite('Action_240_09', 5)	# 79-83	 **attackbox here**
    setInvincible(0)
    tag_voice(0, 'ugo251_0', 'ugo251_1', '', '')
    physicsXImpulse(5120)
    teleportRelativeX(30000)
    sprite('Action_240_10', 3)	# 84-86	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff2', 100)
    teleportRelativeX(40000)
    sprite('Action_240_11', 3)	# 87-89	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 9000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(3000)
    AirPushbackY(12000)
    sprite('Action_240_12', 4)	# 90-93	 **attackbox here**
    Unknown1084(1)
    sprite('Action_240_13', 5)	# 94-98	 **attackbox here**
    sprite('Action_240_14', 2)	# 99-100	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff3', 100)
    sprite('Action_240_15', 4)	# 101-104	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 120000)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(1)
    sprite('Action_240_16', 5)	# 105-109	 **attackbox here**
    sprite('Action_240_17', 5)	# 110-114	 **attackbox here**
    sprite('Action_240_18', 3)	# 115-117	 **attackbox here**
    sprite('Action_240_19', 2)	# 118-119	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff4', 100)
    sprite('Action_240_20', 6)	# 120-125	 **attackbox here**
    RefreshMultihit()
    Hitstop(13)
    Unknown11072(1, 400000, 200000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(6000)
    AirPushbackY(24000)
    sprite('Action_240_21', 11)	# 126-136	 **attackbox here**
    sprite('Action_240_22', 6)	# 137-142	 **attackbox here**
    sprite('Action_240_23', 5)	# 143-147	 **attackbox here**
    physicsXImpulse(22000)
    Unknown1028(3000)
    sprite('Action_240_24', 2)	# 148-149	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff5', 100)
    sprite('Action_240_25', 5)	# 150-154	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11072(0, -1, -1)
    Unknown11001(0, 0, 0)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    YImpluseBeforeWallbounce(200)
    AirPushbackX(0)
    AirPushbackY(5000)
    Unknown1084(1)
    sprite('Action_240_26', 5)	# 155-159	 **attackbox here**
    sprite('Action_240_27', 4)	# 160-163
    GFX_0('UGO_Ultimate_AtkCol_0', 0)
    physicsXImpulse(18000)
    sprite('Action_240_28ex01', 3)	# 164-166	 **attackbox here**
    GFX_0('UGO_Ultimate_AtkCol_1_OD', 0)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(500)
    Unknown11091(10)
    Hitstop(1)
    Unknown11072(1, 250000, 250000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(8000)
    AirPushbackY(600)
    PushbackX(3000)
    YImpluseBeforeWallbounce(2300)
    Unknown2038(2)

    def upon_78():
        Unknown2038(-1)
        if (not SLOT_2):
            clearUponHandler(78)
            Unknown11072(0, -1, -1)
    sprite('Action_240_28ex01', 1)	# 167-167	 **attackbox here**
    sprite('Action_240_29ex01', 2)	# 168-169	 **attackbox here**
    Unknown1084(1)
    sprite('Action_240_29ex01', 3)	# 170-172	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 6)	# 173-178	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 5)	# 179-183	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 184-187	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 188-191	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 192-195	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 196-199	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 200-203	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 5)	# 204-208	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30', 3)	# 209-211
    clearUponHandler(78)
    Unknown11072(0, -1, -1)
    Unknown23027()
    sprite('Action_240_31', 4)	# 212-215	 **attackbox here**
    Unknown26('UGO_Ultimate_AtkCol_1_OD')
    tag_voice(0, 'ugo252_0', 'ugo252_1', '', '')
    GFX_0('UGO_UltimateAssault_AtkEff_Fini', 100)
    teleportRelativeX(-50000)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_32', 1)	# 216-216	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Damage(1500)
    Unknown11091(20)
    Unknown11001(0, 0, 0)
    Hitstop(3)
    AirPushbackX(65000)
    AirPushbackY(500)
    YImpluseBeforeWallbounce(50)
    PushbackX(19800)
    sprite('Action_240_32', 1)	# 217-217	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_32', 1)	# 218-218	 **attackbox here**
    RefreshMultihit()
    Unknown11064(0)
    Hitstop(30)

    def upon_12():
        SFX_3('SE005')
        SFX_3('SE_BigBomb')
        Unknown13024(1)
    sprite('Action_240_33', 19)	# 219-237	 **attackbox here**
    Unknown2015(0)
    Unknown23027()
    Unknown13024(1)
    sprite('Action_240_34', 8)	# 238-245
    sprite('Action_240_35', 7)	# 246-252
    teleportRelativeX(-30000)
    loopRest()

@State
def UltimateRanged():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1000)
        PushbackX(20000)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        AttackP2(100)
        AirUntechableTime(70)
        Unknown9154(50)

        def upon_78():
            Unknown13024(0)
            Hitstop(5)
            Unknown11072(1, 700000, 0)
            Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4052()
            Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000000000000')
            SFX_0('107_throw_catch')
            setInvincible(1)
            enterState('UltimateRanged_Exe')
            Unknown11069('UltimateRanged_Exe')
        Unknown11068(1)
        Unknown11064(1)
        Unknown1084(1)
    sprite('Action_262_00', 5)	# 1-5
    setInvincible(1)
    Unknown2036(55, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_262_01', 5)	# 6-10
    SFX_1('ugo253')
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_05', 5)	# 40-44
    sprite('Action_262_06', 5)	# 45-49
    sprite('Action_460_00', 3)	# 50-52
    GFX_0('UGO_Assault_SummonIn', 100)
    tag_voice(1, 'ugo254_0', 'ugo254_1', 'ugo254_2', '')
    sprite('Action_460_01', 3)	# 53-55	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_460_02', 3)	# 56-58	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_460_03', 3)	# 59-61	 **attackbox here**
    teleportRelativeX(10100)
    sprite('Action_460_04', 3)	# 62-64	 **attackbox here**
    teleportRelativeX(9000)
    sprite('Action_460_05', 2)	# 65-66	 **attackbox here**
    teleportRelativeX(12000)
    sprite('Action_460_05', 1)	# 67-67	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    sprite('Action_460_06ex01', 2)	# 68-69	 **attackbox here**
    RefreshMultihit()
    sprite('Action_460_06', 2)	# 70-71	 **attackbox here**
    Unknown23027()
    sprite('Action_465_00', 2)	# 72-73	 **attackbox here**
    clearUponHandler(78)
    teleportRelativeX(62000)
    sprite('Action_465_01', 2)	# 74-75	 **attackbox here**
    setInvincible(0)
    sprite('Action_465_02', 2)	# 76-77	 **attackbox here**
    GFX_0('UGO_Assault2nd_Zanzou', 100)
    RefreshMultihit()
    Damage(2000)
    AttackP1(60)
    AttackP2(80)
    PushbackX(-73000)
    AirPushbackX(-14000)
    AirPushbackY(34000)
    Unknown9154(45)
    Hitstop(12)
    Unknown11072(0, -1, -1)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    AirHitstunAnimation(1)
    sprite('Action_465_03', 5)	# 78-82	 **attackbox here**
    sprite('Action_465_04', 11)	# 83-93	 **attackbox here**
    sprite('Action_465_05', 7)	# 94-100
    GFX_0('UGO_Assault2nd_SummonOut', 100)
    sprite('Action_465_06', 6)	# 101-106
    sprite('Action_465_07', 5)	# 107-111

@State
def UltimateRanged_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(1000)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        AirPushbackX(3500)
        AirPushbackY(23000)
        YImpluseBeforeWallbounce(1500)
        Unknown9016(1)
        Hitstop(5)
        Unknown9154(50)
        Unknown11068(1)
        setInvincible(1)
        Unknown20000(1)
        Unknown11069('UltimateRanged_Exe2')
        Unknown30068(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown13024(0)
        Unknown2021(1)
        Unknown2015(150)
        Unknown11108('03000000')
    sprite('Action_145_00', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    teleportRelativeX(62000)
    sprite('Action_145_01', 2)	# 3-4	 **attackbox here**
    GFX_0('UGO_Assault2nd_Zanzou', 100)
    sprite('Action_145_02', 2)	# 5-6	 **attackbox here**
    StartMultihit()
    Unknown5000(0, 0)
    Unknown36(22)
    SLOT_12 = SLOT_19
    Unknown1019(14)
    Unknown35()
    sprite('Action_145_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_145_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_145_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_145_06', 2)	# 13-14	 **attackbox here**
    physicsYImpulse(9000)
    Unknown8001(3, 100)
    sprite('Action_145_07', 2)	# 15-16	 **attackbox here**
    physicsYImpulse(25000)
    setGravity(2500)
    sprite('Action_145_08', 1)	# 17-17	 **attackbox here**
    sprite('Action_145_09', 2)	# 18-19	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    GFX_0('UGO_AssaultEx_Zanzou1', 100)
    sprite('Action_145_10', 2)	# 20-21	 **attackbox here**
    sprite('Action_145_11', 3)	# 22-24	 **attackbox here**
    sprite('Action_145_12', 3)	# 25-27	 **attackbox here**
    loopRest()
    enterState('UltimateRanged_Exe2')

@State
def UltimateRanged_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRanged_Exe3', 3, 0, 0)
        Unknown23056('')
        Damage(1000)
        AttackP2(100)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11045(0)
        Unknown11046(1)
        Unknown20000(1)
        Unknown11068(1)
        setInvincible(1)
        Unknown11069('UltimateRanged_Exe3')
        Unknown30068(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown13024(0)
        Unknown2021(1)
        Unknown11108('03000000')
        Unknown9266(12)
    sprite('Action_145_13', 2)	# 1-2
    GFX_0('UGO_DrainThrow_AntiAirZanzou', 100)
    SFX_3('SE042')
    sprite('Action_145_14', 5)	# 3-7	 **attackbox here**
    RefreshMultihit()
    sprite('Action_145_15', 5)	# 8-12
    setInvincible(0)
    sprite('Action_145_16', 5)	# 13-17
    setGravity(1200)
    sprite('Action_145_17', 5)	# 18-22
    sendToLabelUpon(2, 1)
    label(0)
    sprite('Action_022_00', 3)	# 23-25
    sprite('Action_022_01', 3)	# 26-28
    loopRest()
    gotoLabel(0)
    label(1)

@State
def UltimateRanged_Exe3():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(3500)
        AirPushbackY(3500)
        YImpluseBeforeWallbounce(300)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        Hitstop(15)
        Unknown20000(1)
        Unknown11068(1)
        setInvincible(1)
        Unknown30068(1)
        Unknown30048(1)
        Unknown11108('03000000')
        Unknown9266(12)

        def upon_78():
            Unknown2058(2500)
            Unknown36(22)
            Unknown2058(-1000)
            Unknown35()
        Unknown11064(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown13024(0)
    sprite('Action_146_00', 15)	# 1-15	 **attackbox here**
    tag_voice(0, 'ugo255_0', 'ugo255_1', 'ugo255_2', '')
    Unknown23011(1)
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_146_00', 9)	# 16-24	 **attackbox here**
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_146_02', 2)	# 25-26	 **attackbox here**
    GFX_0('UGO_AssaultEx_DrainYoin', 100)
    GFX_0('UGO_Drain_Steal', 0)
    RefreshMultihit()
    SFX_3('SE008')
    Hitstop(20)
    physicsXImpulse(2560)
    Unknown1028(-200)
    physicsYImpulse(15000)
    setGravity(1200)
    sprite('Action_146_03', 4)	# 27-30
    clearUponHandler(78)
    sprite('Action_146_04', 5)	# 31-35
    sprite('Action_146_05', 7)	# 36-42	 **attackbox here**
    SFX_3('SE043')
    RefreshMultihit()
    Unknown1015(-5120)
    Unknown1028(500)
    Unknown1021(2560)
    setGravity(300)
    AttackLevel_(5)
    AirPushbackX(8000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(2000)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    Hitstop(15)
    Unknown9016(0)
    Unknown9266(0)
    sprite('Action_146_06', 5)	# 43-47
    sprite('Action_146_07', 4)	# 48-51	 **attackbox here**
    tag_voice(0, 'ugo256_0', 'ugo256_1', 'ugo256_2', '')
    Unknown1015(-5120)
    Unknown1021(15000)
    setGravity(1600)
    sprite('Action_146_08', 2)	# 52-53	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    sprite('Action_146_09', 2)	# 54-55	 **attackbox here**
    GFX_0('UGO_AssaultEx_Zanzou2', 100)
    Unknown1028(300)
    Unknown1015(-5000)
    RefreshMultihit()
    Unknown20000(0)
    AttackLevel_(5)
    Damage(2000)
    AttackP2(60)
    AirPushbackX(25000)
    AirPushbackY(16000)
    YImpluseBeforeWallbounce(1600)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    Hitstop(15)
    Unknown9016(0)
    Unknown11069('')
    Unknown11064(0)

    def upon_12():
        SFX_3('SE_BigBomb')
        Unknown13024(1)
    sprite('Action_146_10', 4)	# 56-59	 **attackbox here**
    sprite('Action_146_11', 5)	# 60-64	 **attackbox here**
    sprite('Action_146_12', 3)	# 65-67
    sprite('Action_146_13', 4)	# 68-71
    sprite('Action_146_14', 5)	# 72-76
    setInvincible(0)
    label(0)
    sprite('Action_022_00', 3)	# 77-79
    sprite('Action_022_01', 3)	# 80-82
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_023_00', 5)	# 83-87
    sprite('Action_023_00', 3)	# 88-90
    Unknown13024(1)
    Unknown1084(1)
    sprite('Action_021_01', 4)	# 91-94
    sprite('Action_021_02', 4)	# 95-98

@State
def UltimateRangedOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1000)
        PushbackX(35000)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        Unknown9016(1)
        AttackP2(100)
        AirUntechableTime(70)
        Unknown9154(50)

        def upon_78():
            Hitstop(5)
            Unknown13024(0)
            Unknown11072(1, 700000, 0)
            Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            Unknown4052()
            Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000000000000')
            SFX_0('107_throw_catch')
            setInvincible(1)
            enterState('UltimateRangedOD_Exe')
            Unknown11069('UltimateRangedOD_Exe')
        Unknown11068(1)
        Unknown11064(1)
        Unknown1084(1)
    sprite('Action_262_00', 5)	# 1-5
    setInvincible(1)
    Unknown2036(55, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_262_01', 5)	# 6-10
    SFX_1('ugo253')
    sprite('Action_262_02', 5)	# 11-15
    sprite('Action_262_03', 3)	# 16-18
    sprite('Action_262_04', 3)	# 19-21
    sprite('Action_262_03', 3)	# 22-24
    sprite('Action_262_04', 3)	# 25-27
    sprite('Action_262_03', 3)	# 28-30
    sprite('Action_262_04', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_05', 5)	# 40-44
    sprite('Action_262_06', 5)	# 45-49
    sprite('Action_460_00', 3)	# 50-52
    GFX_0('UGO_Assault_SummonIn', 100)
    tag_voice(1, 'ugo254_0', 'ugo254_1', 'ugo254_2', '')
    sprite('Action_460_01', 3)	# 53-55	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_460_02', 3)	# 56-58	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_460_03', 3)	# 59-61	 **attackbox here**
    teleportRelativeX(10100)
    sprite('Action_460_04', 3)	# 62-64	 **attackbox here**
    teleportRelativeX(9000)
    sprite('Action_460_05', 2)	# 65-66	 **attackbox here**
    teleportRelativeX(12000)
    sprite('Action_460_05', 1)	# 67-67	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    sprite('Action_460_06ex01', 2)	# 68-69	 **attackbox here**
    RefreshMultihit()
    sprite('Action_460_06', 2)	# 70-71	 **attackbox here**
    Unknown23027()
    sprite('Action_465_00', 2)	# 72-73	 **attackbox here**
    clearUponHandler(78)
    teleportRelativeX(62000)
    sprite('Action_465_01', 2)	# 74-75	 **attackbox here**
    setInvincible(0)
    sprite('Action_465_02', 2)	# 76-77	 **attackbox here**
    GFX_0('UGO_Assault2nd_Zanzou', 100)
    RefreshMultihit()
    Damage(2500)
    AttackP1(60)
    AttackP2(80)
    PushbackX(-73000)
    AirPushbackX(-14000)
    AirPushbackY(34000)
    Unknown9154(45)
    Hitstop(12)
    Unknown11072(0, -1, -1)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    AirHitstunAnimation(1)
    sprite('Action_465_03', 5)	# 78-82	 **attackbox here**
    sprite('Action_465_04', 11)	# 83-93	 **attackbox here**
    sprite('Action_465_05', 7)	# 94-100
    GFX_0('UGO_Assault2nd_SummonOut', 100)
    sprite('Action_465_06', 6)	# 101-106
    sprite('Action_465_07', 5)	# 107-111

@State
def UltimateRangedOD_Exe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(500)
        PushbackX(15000)
        AttackP2(100)
        Unknown9016(1)
        Hitstop(5)
        Unknown9154(50)
        Unknown11068(1)
        setInvincible(1)
        Unknown20000(1)
        Unknown11069('UltimateRangedOD_Exe')
        Unknown30068(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown13024(0)
        Unknown2021(1)
        Unknown2015(150)
        Unknown11108('03000000')
    sprite('Action_145_00', 1)	# 1-1	 **attackbox here**
    StartMultihit()
    teleportRelativeX(31000)
    sprite('Action_145_00', 1)	# 2-2	 **attackbox here**
    StartMultihit()
    teleportRelativeX(31000)
    sprite('Action_145_01', 2)	# 3-4	 **attackbox here**
    GFX_0('UGO_Assault2nd_Zanzou', 100)
    sprite('Action_145_02', 2)	# 5-6	 **attackbox here**
    StartMultihit()
    Unknown5000(0, 0)
    Unknown36(22)
    SLOT_12 = SLOT_19
    Unknown1019(19)
    Unknown35()
    sprite('Action_145_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_145_04', 2)	# 9-10	 **attackbox here**
    sprite('Action_145_05', 2)	# 11-12	 **attackbox here**
    sprite('Action_115_00', 2)	# 13-14	 **attackbox here**
    sprite('Action_115_01', 2)	# 15-16	 **attackbox here**
    sprite('Action_115_02', 1)	# 17-17	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_02', 1)	# 18-18	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 19-20	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    GFX_0('UGO_Invincible_Zanzo1', 100)
    sprite('Action_115_03', 2)	# 21-22	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_04ex01', 1)	# 23-23	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    sprite('Action_115_05', 1)	# 24-24	 **attackbox here**
    sprite('Action_115_06', 1)	# 25-25	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 26-26	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 1)	# 27-27	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 1)	# 28-28	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 1)	# 29-29	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 1)	# 30-30	 **attackbox here**
    sprite('Action_115_11', 1)	# 31-31	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_13', 3)	# 32-34	 **attackbox here**
    sprite('Action_145_06', 2)	# 35-36	 **attackbox here**
    physicsYImpulse(9000)
    Unknown8001(3, 100)
    sprite('Action_145_07', 2)	# 37-38	 **attackbox here**
    physicsYImpulse(20000)
    setGravity(2500)
    RefreshMultihit()
    AttackLevel_(5)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    AirPushbackX(3500)
    AirPushbackY(26000)
    YImpluseBeforeWallbounce(1500)
    Unknown11069('UltimateRangedOD_Exe2')
    sprite('Action_145_08', 1)	# 39-39	 **attackbox here**
    sprite('Action_145_09', 2)	# 40-41	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    GFX_0('UGO_AssaultEx_Zanzou1', 100)
    sprite('Action_145_10', 2)	# 42-43	 **attackbox here**
    sprite('Action_145_11', 3)	# 44-46	 **attackbox here**
    sprite('Action_145_12', 3)	# 47-49	 **attackbox here**
    loopRest()
    enterState('UltimateRangedOD_Exe2')

@State
def UltimateRangedOD_Exe2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateRangedOD_Exe3', 3, 0, 0)
        Unknown23056('')
        Damage(1000)
        AttackP2(100)
        Unknown11002(-1)
        Unknown9016(1)
        Unknown30061(0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11045(0)
        Unknown11046(1)
        Unknown20000(1)
        Unknown11068(1)
        setInvincible(1)
        Unknown11069('UltimateRangedOD_Exe3')
        Unknown30068(1)
        Unknown30048(1)
        Unknown11064(1)
        Unknown13024(0)
        Unknown2021(1)
        Unknown11108('03000000')
        Unknown9266(12)
    sprite('Action_145_13', 2)	# 1-2
    GFX_0('UGO_DrainThrow_AntiAirZanzou', 100)
    SFX_3('SE042')
    sprite('Action_145_14', 5)	# 3-7	 **attackbox here**
    RefreshMultihit()
    sprite('Action_145_15', 5)	# 8-12
    setInvincible(0)
    sprite('Action_145_16', 5)	# 13-17
    setGravity(1200)
    sprite('Action_145_17', 5)	# 18-22
    sendToLabelUpon(2, 1)
    label(0)
    sprite('Action_022_00', 3)	# 23-25
    sprite('Action_022_01', 3)	# 26-28
    loopRest()
    gotoLabel(0)
    label(1)

@State
def UltimateRangedOD_Exe3():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(1000)
        AttackP2(100)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(3500)
        AirPushbackY(3500)
        YImpluseBeforeWallbounce(300)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        Hitstop(15)
        Unknown20000(1)
        Unknown11068(1)
        setInvincible(1)
        Unknown30068(1)
        Unknown30048(1)

        def upon_78():
            Unknown2058(2500)
            Unknown36(22)
            Unknown2058(-1000)
            Unknown35()
        Unknown11064(1)
        Unknown9266(12)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Unknown13024(0)
        Unknown11108('03000000')
    sprite('Action_146_00', 15)	# 1-15	 **attackbox here**
    tag_voice(0, 'ugo255_0', 'ugo255_1', 'ugo255_2', '')
    Unknown23011(1)
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_146_00', 9)	# 16-24	 **attackbox here**
    GFX_0('UGO_Drain_Yoin', 100)
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_146_01', 6)	# 25-30
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    GFX_0('UGO_DrainThrow_HitAura', 0)
    sprite('Action_146_02', 2)	# 31-32	 **attackbox here**
    GFX_0('UGO_Drain_Steal', 0)
    GFX_0('UGO_AssaultEx_DrainYoin', 100)
    RefreshMultihit()
    SFX_3('SE008')
    Hitstop(20)
    physicsXImpulse(2560)
    Unknown1028(-200)
    physicsYImpulse(15000)
    setGravity(1200)
    sprite('Action_146_03', 4)	# 33-36
    clearUponHandler(78)
    sprite('Action_146_04', 5)	# 37-41
    sprite('Action_146_05', 7)	# 42-48	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE043')
    Unknown1015(-5120)
    Unknown1028(500)
    Unknown1021(2560)
    setGravity(300)
    AttackLevel_(5)
    AirPushbackX(8000)
    AirPushbackY(20000)
    YImpluseBeforeWallbounce(1500)
    GroundedHitstunAnimation(1)
    AirHitstunAnimation(1)
    Hitstop(15)
    Unknown9016(0)
    Unknown9266(0)
    sprite('Action_146_06', 5)	# 49-53
    tag_voice(0, 'ugo257_0', 'ugo257_1', 'ugo257_2', '')
    sprite('Action_146_07', 4)	# 54-57	 **attackbox here**
    Unknown1015(-5120)
    Unknown1021(12000)
    setGravity(1200)
    sprite('Action_146_08', 2)	# 58-59	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    sprite('Action_146_09', 2)	# 60-61	 **attackbox here**
    GFX_0('UGO_AssaultEx_Zanzou2', 100)
    Unknown1028(300)
    setGravity(1900)
    RefreshMultihit()
    AttackLevel_(5)
    AirPushbackX(12000)
    AirPushbackY(19500)
    YImpluseBeforeWallbounce(2100)
    Unknown9310(30)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    Hitstop(10)
    Unknown9016(0)

    def upon_78():
        Unknown2038(1)
    sprite('Action_146_10', 2)	# 62-63	 **attackbox here**
    Unknown1015(-5000)
    Unknown1021(12000)
    sprite('Action_146_11', 2)	# 64-65	 **attackbox here**
    Unknown20000(0)
    sprite('Action_146_12', 1)	# 66-66
    sprite('Action_146_13', 2)	# 67-68
    sprite('Action_146_14', 1)	# 69-69
    if SLOT_2:
        sendToLabel(2)
    sprite('Action_146_14', 4)	# 70-73
    setInvincible(0)
    Unknown13024(1)
    label(0)
    sprite('Action_022_00', 3)	# 74-76
    sprite('Action_022_01', 3)	# 77-79
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_023_00', 2)	# 80-81
    Unknown1084(1)
    sprite('Action_021_01', 4)	# 82-85
    sprite('Action_021_02', 4)	# 86-89
    ExitState()
    label(2)
    clearUponHandler(2)
    clearUponHandler(78)
    Unknown2016(400)
    Unknown2015(290)
    sprite('Action_160_11ex01', 2)	# 90-91	 **attackbox here**
    sprite('Action_161_00', 2)	# 92-93	 **attackbox here**
    sprite('Action_161_01', 9)	# 94-102	 **attackbox here**
    physicsXImpulse(8000)
    physicsYImpulse(16000)
    setGravity(3500)
    sendToLabelUpon(2, 3)

    def upon_3():
        if (SLOT_19 < 250000):
            clearUponHandler(3)
            Unknown1019(75)
    sprite('Action_161_01', 32767)	# 103-32869	 **attackbox here**
    tag_voice(0, 'ugo258_0', 'ugo258_1', 'ugo258_2', '')
    label(3)
    sprite('Action_161_02', 2)	# 32870-32871	 **attackbox here**
    Unknown2004(1, 0)
    SFX_3('SE049_SpecialSwing')
    Unknown2016(-1)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown1084(1)
    Unknown2016(-1)
    Unknown2015(-1)
    sprite('Action_161_03', 1)	# 32872-32872	 **attackbox here**
    sprite('Action_161_04ex01', 3)	# 32873-32875	 **attackbox here**
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    SFX_3('SE060_BoundMetal')
    RefreshMultihit()
    ScreenShake(8000, 3500)
    Damage(2000)
    AttackP2(60)
    AirPushbackX(5000)
    AirPushbackY(-15000)
    YImpluseBeforeWallbounce(0)
    AirHitstunAnimation(9)
    Unknown9310(1)
    Unknown9190(1)
    Unknown11064(0)
    Unknown9016(1)
    Hitstop(25)
    Unknown11069('')
    Unknown11072(1, 400000, 0)

    def upon_12():
        SFX_3('SE_BigBomb')
        Unknown13024(1)
    sprite('Action_161_04ex01', 22)	# 32876-32897	 **attackbox here**
    Unknown23027()
    sprite('Action_161_05', 8)	# 32898-32905	 **attackbox here**
    sprite('Action_161_06', 7)	# 32906-32912	 **attackbox here**
    sprite('Action_161_07', 7)	# 32913-32919
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 6)	# 32920-32925
    sprite('Action_161_09', 6)	# 32926-32931

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(8000)
        PushbackX(5000)
        Hitstop(0)
        Unknown9154(600)
        Unknown9130(220)
        Unknown9142(200)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown11084(1)
        Unknown11042(1)
        Unknown30048(1)
        setInvincible(1)
        Unknown11072(1, 50000, 0)
        Unknown11086(1)

        def upon_78():
            GFX_0('AstralDrainYarare', 100)
            GFX_0('UGO_AstralBlade1', 100)
            GFX_0('UGO_AstralEff1', 100)
            GFX_0('UGO_AstralEff2', 100)
            GFX_0('UGO_AstralEff3', 100)
            enterState('AstralHeatExe')
        Unknown11056(2)
    sprite('Action_220_00', 3)	# 1-3	 **attackbox here**
    Unknown2036(92, -1, 1)
    Unknown23147()
    GFX_0('UGO_AstralCutIn', 100)
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_220_01', 3)	# 4-6	 **attackbox here**
    SFX_1('ugo291')
    sprite('Action_220_02', 3)	# 7-9	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_03', 3)	# 10-12	 **attackbox here**
    sprite('Action_220_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_220_05', 3)	# 16-18	 **attackbox here**
    sprite('Action_220_02', 3)	# 19-21	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_220_04', 3)	# 25-27	 **attackbox here**
    sprite('Action_220_05', 3)	# 28-30	 **attackbox here**
    sprite('Action_220_02', 3)	# 31-33	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_03', 3)	# 34-36	 **attackbox here**
    sprite('Action_220_04', 3)	# 37-39	 **attackbox here**
    sprite('Action_220_05', 3)	# 40-42	 **attackbox here**
    sprite('Action_220_02', 3)	# 43-45	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_03', 3)	# 46-48	 **attackbox here**
    sprite('Action_220_04', 3)	# 49-51	 **attackbox here**
    sprite('Action_220_05', 3)	# 52-54	 **attackbox here**
    sprite('Action_220_02', 3)	# 55-57	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_03', 3)	# 58-60	 **attackbox here**
    sprite('Action_220_04', 3)	# 61-63	 **attackbox here**
    sprite('Action_220_05', 3)	# 64-66	 **attackbox here**
    sprite('Action_220_02', 3)	# 67-69	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_03', 3)	# 70-72	 **attackbox here**
    sprite('Action_220_04', 3)	# 73-75	 **attackbox here**
    sprite('Action_220_05', 3)	# 76-78	 **attackbox here**
    sprite('Action_220_06', 3)	# 79-81	 **attackbox here**
    SFX_3('SE_ChargeUpEXLoop')
    sprite('Action_220_07', 3)	# 82-84	 **attackbox here**
    sprite('Action_220_08', 3)	# 85-87	 **attackbox here**
    sprite('Action_220_09', 2)	# 88-89	 **attackbox here**
    physicsXImpulse(25000)

    def upon_3():
        if (SLOT_19 < 120000):
            clearUponHandler(3)
            Unknown2038(1)
            Unknown1019(25)
    sprite('Action_220_10', 3)	# 90-92	 **attackbox here**
    teleportRelativeX(50000)
    if (not SLOT_2):
        physicsXImpulse(45000)
    else:
        physicsXImpulse(11250)
    sprite('Action_220_11', 3)	# 93-95	 **attackbox here**
    clearUponHandler(3)
    sprite('Action_220_12', 3)	# 96-98	 **attackbox here**
    sprite('Action_220_13', 6)	# 99-104	 **attackbox here**
    teleportRelativeX(16000)
    if (not SLOT_2):
        physicsXImpulse(12500)
    else:
        physicsXImpulse(3125)
    sprite('Action_220_14', 3)	# 105-107	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_220_15', 7)	# 108-114	 **attackbox here**
    teleportRelativeX(46000)
    if (not SLOT_2):
        physicsXImpulse(10000)
        Unknown1028(-1000)
    else:
        physicsXImpulse(2500)
        Unknown1028(-250)
    sprite('Action_220_16', 4)	# 115-118	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown1084(1)
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_220_17', 4)	# 119-122	 **attackbox here**
    sprite('Action_220_16', 4)	# 123-126	 **attackbox here**
    sprite('Action_220_17', 4)	# 127-130	 **attackbox here**
    sprite('Action_220_16', 4)	# 131-134	 **attackbox here**
    sprite('Action_220_17', 4)	# 135-138	 **attackbox here**
    sprite('Action_220_22', 4)	# 139-142
    physicsXImpulse(-48000)
    physicsYImpulse(10000)
    setGravity(1500)

    def upon_3():
        Unknown1019(90)

    def upon_STATE_END():
        teleportRelativeY(0)
    sprite('Action_220_23', 32767)	# 143-32909
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_220_24', 1)	# 32910-32910
    clearUponHandler(3)
    Unknown1084(1)
    teleportRelativeX(55000)
    sprite('Action_220_24', 3)	# 32911-32913
    teleportRelativeX(55000)
    sprite('Action_000_00', 3)	# 32914-32916	 **attackbox here**

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11091(100)
        Unknown23022(1)
        setInvincible(1)
        Unknown11068(1)
        Unknown11078(1)
        Unknown23088(1, 1)
        Unknown23157(1)
        Unknown23084(1)
        Unknown23024(3)
        Unknown20006(1)
        Unknown11086(1)
        Unknown11023(1)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20004(1)
        GFX_0('AstralCamera', 100)
        Unknown11056(2)
    sprite('Action_220_16', 4)	# 1-4	 **attackbox here**
    Unknown1084(1)
    sprite('Action_220_17', 4)	# 5-8	 **attackbox here**
    sprite('Action_220_18', 4)	# 9-12	 **attackbox here**
    SFX_3('SE_Drain')
    sprite('Action_220_19', 4)	# 13-16	 **attackbox here**
    sprite('Action_220_18', 4)	# 17-20	 **attackbox here**
    SFX_3('SE_Drain')
    sprite('Action_220_19', 4)	# 21-24	 **attackbox here**
    sprite('Action_220_18', 4)	# 25-28	 **attackbox here**
    SFX_3('SE_Drain')
    sprite('Action_220_19', 4)	# 29-32	 **attackbox here**
    sprite('Action_220_18', 4)	# 33-36	 **attackbox here**
    SFX_3('SE_Drain')
    sprite('Action_220_19', 4)	# 37-40	 **attackbox here**
    sprite('Action_220_18', 4)	# 41-44	 **attackbox here**
    SFX_3('SE_Drain')
    sprite('Action_220_19', 4)	# 45-48	 **attackbox here**
    sprite('Action_220_20', 4)	# 49-52	 **attackbox here**
    SFX_3('SE_Drain')
    sprite('Action_220_21', 2)	# 53-54	 **attackbox here**
    sprite('Action_220_22', 2)	# 55-56
    sprite('Action_221_00', 2)	# 57-58
    teleportRelativeX(54000)
    SFX_1('ugo292')
    sprite('Action_221_01', 2)	# 59-60	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(3)
    Damage(4000)
    PushbackX(0)
    Hitstop(10)
    Unknown9154(600)
    Unknown9130(220)
    Unknown9142(200)
    Unknown11072(1, 300000, 0)
    GroundedHitstunAnimation(2)
    AirHitstunAnimation(2)
    Unknown26('UGO_AstralEff2')
    GFX_0('AstralDrainYarare2', 100)
    sprite('Action_221_02', 2)	# 61-62
    sprite('Action_221_03', 3)	# 63-65
    sprite('Action_221_04', 1)	# 66-66
    teleportRelativeX(50000)
    sprite('Action_221_05', 1)	# 67-67	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(3)
    PushbackX(0)
    Hitstop(10)
    AirPushbackX(2500)
    AirPushbackY(100)
    YImpluseBeforeWallbounce(10)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirUntechableTime(600)
    Unknown9016(1)
    Unknown11072(1, 150000, 150000)
    GFX_0('UGO_AstralBlade2', 100)
    sprite('Action_221_06', 3)	# 68-70
    sprite('Action_221_07', 4)	# 71-74
    teleportRelativeX(-7000)
    sprite('Action_221_08', 3)	# 75-77
    physicsXImpulse(50000)
    Unknown1028(-5000)
    sprite('Action_221_09', 4)	# 78-81
    sprite('Action_221_10', 1)	# 82-82
    physicsXImpulse(25000)
    Unknown1028(-2500)
    sprite('Action_221_11', 4)	# 83-86	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(5)
    Unknown11067(1)
    Hitstop(3)
    AirPushbackX(21000)
    AirPushbackY(4500)
    YImpluseBeforeWallbounce(5)
    PushbackX(0)
    AirUntechableTime(1000)
    AirHitstunAnimation(18)
    Unknown9016(0)
    Unknown11072(1, 150000, 150000)
    Unknown21012('41737472616c43616d657261000000000000000000000000000000000000000021000000')
    sprite('Action_221_12', 3)	# 87-89
    Unknown2017(0)
    Unknown1084(1)
    sprite('Action_221_13', 2)	# 90-91
    sprite('Action_221_14', 2)	# 92-93
    sprite('Action_222_00', 5)	# 94-98	 **attackbox here**
    Unknown21012('41737472616c43616d657261000000000000000000000000000000000000000022000000')
    GFX_0('AstralShaker', 100)
    sprite('Action_222_01', 6)	# 99-104	 **attackbox here**
    sprite('Action_222_02', 6)	# 105-110	 **attackbox here**
    sprite('Action_222_03', 6)	# 111-116	 **attackbox here**
    sprite('Action_222_04', 5)	# 117-121	 **attackbox here**
    GFX_0('AstralBoundDummy', 100)
    sprite('Action_222_05', 2)	# 122-123	 **attackbox here**
    sprite('Action_222_06', 5)	# 124-128	 **attackbox here**
    sprite('Action_222_07', 5)	# 129-133	 **attackbox here**
    sprite('Action_222_08', 5)	# 134-138	 **attackbox here**
    sprite('Action_222_09', 5)	# 139-143	 **attackbox here**
    sprite('Action_222_10', 5)	# 144-148	 **attackbox here**
    sprite('Action_222_11', 5)	# 149-153	 **attackbox here**
    sprite('Action_222_09', 5)	# 154-158	 **attackbox here**
    sprite('Action_222_10', 5)	# 159-163	 **attackbox here**
    sprite('Action_222_11', 5)	# 164-168	 **attackbox here**
    sprite('Action_222_09', 5)	# 169-173	 **attackbox here**
    sprite('Action_222_10', 5)	# 174-178	 **attackbox here**
    sprite('Action_222_11', 5)	# 179-183	 **attackbox here**
    sprite('Action_222_09', 5)	# 184-188	 **attackbox here**
    sprite('Action_222_10', 5)	# 189-193	 **attackbox here**
    sprite('Action_222_11', 5)	# 194-198	 **attackbox here**
    SFX_1('ugo293')
    sprite('Action_222_09', 5)	# 199-203	 **attackbox here**
    sprite('Action_222_10', 5)	# 204-208	 **attackbox here**
    sprite('Action_222_11', 5)	# 209-213	 **attackbox here**
    sprite('Action_222_09', 5)	# 214-218	 **attackbox here**
    sprite('Action_222_10', 5)	# 219-223	 **attackbox here**
    sprite('Action_222_11', 5)	# 224-228	 **attackbox here**
    sprite('Action_222_09', 5)	# 229-233	 **attackbox here**
    sprite('Action_222_10', 5)	# 234-238	 **attackbox here**
    sprite('Action_222_11', 5)	# 239-243	 **attackbox here**
    sprite('Action_222_09', 5)	# 244-248	 **attackbox here**
    sprite('Action_222_10', 5)	# 249-253	 **attackbox here**
    sprite('Action_222_11', 5)	# 254-258	 **attackbox here**
    sprite('Action_222_09', 5)	# 259-263	 **attackbox here**
    sprite('Action_222_10', 5)	# 264-268	 **attackbox here**
    sprite('Action_222_11', 5)	# 269-273	 **attackbox here**
    sprite('Action_222_09', 5)	# 274-278	 **attackbox here**
    sprite('Action_222_10', 5)	# 279-283	 **attackbox here**
    sprite('Action_222_11', 5)	# 284-288	 **attackbox here**
    sprite('Action_222_12', 7)	# 289-295	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    Unknown21012('41737472616c43616d657261000000000000000000000000000000000000000023000000')
    sprite('Action_222_13', 7)	# 296-302	 **attackbox here**
    sprite('Action_222_14', 7)	# 303-309	 **attackbox here**
    sprite('Action_222_15', 5)	# 310-314	 **attackbox here**
    sprite('Action_222_16', 6)	# 315-320	 **attackbox here**
    sprite('Action_222_17', 6)	# 321-326	 **attackbox here**
    sprite('Action_222_18', 8)	# 327-334	 **attackbox here**
    sprite('Action_222_19', 5)	# 335-339	 **attackbox here**
    sprite('Action_222_20', 5)	# 340-344	 **attackbox here**
    RefreshMultihit()
    Unknown11091(100)
    Damage(30000)
    YImpluseBeforeWallbounce(0)
    Hitstop(1)
    Unknown11001(0, 19, 19)
    Unknown9016(1)
    Unknown11064(3)
    Unknown11072(1, 700000, 250000)

    def upon_78():
        SFX_3('SE_BigBomb')
        SFX_3('SE073_GroundBreak')
    GFX_0('UGO_AstralFinishBlade1', 100)
    sprite('Action_222_21', 19)	# 345-363	 **attackbox here**
    sprite('Action_222_21', 15)	# 364-378	 **attackbox here**
    GFX_0('UGO_AstralFinishImpact', 100)
    Unknown38(5, 1)
    sprite('Action_222_22', 4)	# 379-382
    sprite('Action_222_23', 2)	# 383-384
    sprite('Action_222_24', 2)	# 385-386
    sprite('keep', 5)	# 387-391
    GFX_0('UGO_WhiteDummy', 100)
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('keep', 60)	# 392-451
    Unknown36(22)
    Unknown2006()
    Unknown3038(1)
    Unknown3001(0)
    teleportRelativeY(0)
    setGravity(0)
    physicsYImpulse(1000)
    Unknown35()
    Unknown20000(1)
    Unknown20001(1)
    Unknown1000(0)
    Unknown36(5)
    Unknown1000(0)
    Unknown35()
    sprite('keep', 15)	# 452-466
    Unknown23024(0)
    Unknown26('AstralCamera')
    sprite('Action_230_01', 5)	# 467-471
    GFX_0('UGO_WhiteIn', 100)
    Unknown26('UGO_AstralBG')
    sprite('Action_230_02', 5)	# 472-476
    sprite('Action_230_03', 5)	# 477-481
    sprite('Action_230_04', 5)	# 482-486
    sprite('Action_230_05', 5)	# 487-491
    sprite('Action_230_02', 5)	# 492-496
    sprite('Action_230_03', 5)	# 497-501
    sprite('Action_230_04', 5)	# 502-506
    sprite('Action_230_05', 5)	# 507-511
    sprite('Action_230_02', 5)	# 512-516
    sprite('Action_230_03', 5)	# 517-521
    sprite('Action_230_04', 5)	# 522-526
    sprite('Action_230_05', 5)	# 527-531
    sprite('Action_230_02', 5)	# 532-536
    Unknown18010()
    SFX_1('ugo521')
    Unknown23018(1)
    sprite('Action_230_03', 5)	# 537-541
    sprite('Action_230_04', 5)	# 542-546
    sprite('Action_230_05', 5)	# 547-551
    sprite('Action_230_02', 5)	# 552-556
    label(999)
    sprite('Action_230_03', 5)	# 557-561
    sprite('Action_230_04', 5)	# 562-566
    sprite('Action_230_05', 5)	# 567-571
    sprite('Action_230_02', 5)	# 572-576
    gotoLabel(999)

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
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
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
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
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
    sprite('Action_046_01', 3)	# 1-3
    sprite('Action_046_02', 3)	# 4-6
    sprite('Action_046_03', 3)	# 7-9
    sprite('Action_046_04', 3)	# 10-12
    sprite('Action_046_01', 3)	# 13-15
    sprite('Action_046_02', 3)	# 16-18
    sprite('Action_046_03', 3)	# 19-21
    sprite('Action_046_04', 3)	# 22-24
    sprite('Action_046_01', 3)	# 25-27
    sprite('Action_046_02', 3)	# 28-30
    sprite('Action_046_03', 30)	# 31-60

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

        def upon_3():
            if (SLOT_18 == 57):
                clearUponHandler(3)
                sendToLabel(1)
        Unknown1084(1)
    sprite('Action_053_05', 7)	# 1-7
    sprite('Action_053_06', 5)	# 8-12
    sprite('Action_053_07', 5)	# 13-17
    sprite('Action_053_08', 32767)	# 18-32784	 **attackbox here**
    label(1)
    sprite('Action_053_07', 3)	# 32785-32787
    sprite('Action_053_06', 3)	# 32788-32790
    sprite('Action_053_05', 4)	# 32791-32794
    sprite('Action_053_04', 4)	# 32795-32798
    sprite('Action_000_00', 5)	# 32799-32803	 **attackbox here**

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
        Unknown2004(1, 0)
    sprite('null', 7)	# 1-7
    sprite('Action_161_00', 3)	# 8-10	 **attackbox here**
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-300000)
    Unknown1007(2000000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('Action_161_01', 32767)	# 11-32777	 **attackbox here**
    label(9)
    sprite('Action_161_02', 2)	# 32778-32779	 **attackbox here**
    GFX_0('UGO_StrikeB_Zanzou', 100)
    SFX_3('SE049_SpecialSwing')
    Unknown1084(1)
    sprite('Action_161_03', 1)	# 32780-32780	 **attackbox here**
    sprite('Action_161_04', 5)	# 32781-32785	 **attackbox here**
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(8000, 3500)
    sprite('Action_161_05', 6)	# 32786-32791	 **attackbox here**
    sprite('Action_161_06', 4)	# 32792-32795	 **attackbox here**
    sprite('Action_161_07', 4)	# 32796-32799
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 3)	# 32800-32802
    sprite('Action_161_09', 3)	# 32803-32805

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_02', 3)	# 1-3
    sprite('Action_045_01', 5)	# 4-8
    sprite('Action_045_00', 7)	# 9-15
    sprite('Action_045_10', 7)	# 16-22
    sprite('Action_045_11', 7)	# 23-29

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
    sprite('Action_046_02', 4)	# 6-9
    sprite('Action_046_03', 3)	# 10-12
    loopRest()
    label(0)
    sprite('Action_046_03', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_04', 3)	# 16-18
    sprite('Action_046_05', 3)	# 19-21

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
    sprite('Action_013_00', 2)	# 11-12
    Unknown1084(1)
    Unknown2017(1)
    Unknown2053(1)
    Unknown2034(1)
    clearUponHandler(2)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown12051(2)
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_234_00', 7)	# 1-7	 **attackbox here**
    Unknown1084(1)
    sprite('Action_234_01', 4)	# 8-11	 **attackbox here**
    sprite('Action_234_02', 6)	# 12-17	 **attackbox here**
    sprite('Action_234_03', 6)	# 18-23	 **attackbox here**
    Unknown7006('ugo302', 100, 862938997, 13104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_234_04', 6)	# 24-29	 **attackbox here**
    sprite('Action_234_05', 3)	# 30-32	 **attackbox here**
    SFX_3('SE043')
    GFX_0('UGO_Scratch_AtkCol_Assist', 100)
    sprite('Action_234_06', 4)	# 33-36	 **attackbox here**
    sprite('Action_234_07', 4)	# 37-40	 **attackbox here**
    sprite('Action_234_08', 5)	# 41-45	 **attackbox here**
    sprite('Action_234_09', 6)	# 46-51
    sprite('Action_234_08', 5)	# 52-56	 **attackbox here**
    sprite('Action_234_09', 6)	# 57-62
    Recovery()
    sprite('Action_234_10', 4)	# 63-66
    sprite('Action_234_11', 3)	# 67-69

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(40)
        Unknown9310(1)
        AirPushbackX(5000)
        AirPushbackY(-52000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(20)
        AirHitstunAfterWallbounce(20)
        Unknown9016(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        Unknown11042(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_156_00', 4)	# 1-4
    sprite('Action_156_01', 4)	# 5-8
    GFX_0('UGO_Strike_SummonIn', 100)
    sprite('Action_156_02', 4)	# 9-12	 **attackbox here**
    Unknown7006('ugo213_0', 100, 846161781, 828322609, 0, 0, 100, 846161781, 845099825, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_156_03', 2)	# 13-14	 **attackbox here**
    sprite('Action_156_04ex01', 3)	# 15-17	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    Unknown8004(0, 1, 1)
    RefreshMultihit()
    ScreenShake(11000, 5000)
    GFX_0('UGO_StrikeA_Inpact', 0)
    sprite('Action_156_04ex01', 10)	# 18-27	 **attackbox here**
    StartMultihit()
    Recovery()
    sprite('Action_156_05', 10)	# 28-37	 **attackbox here**
    Recovery()
    sprite('Action_156_06', 5)	# 38-42
    GFX_0('UGO_StrikeA_SummonOut', 100)

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1000)
        AttackP1(70)
        Unknown11092(1)
        AirUntechableTime(40)
        Hitstop(1)
        Unknown9016(1)
        AirPushbackX(10000)
        AirPushbackY(12000)
        PushbackX(12000)
        Unknown11056(2)
        Unknown11042(1)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown2006()

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_115_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_115_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_115_02', 2)	# 7-8	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_02', 2)	# 9-10	 **attackbox here**
    teleportRelativeX(50000)
    Unknown7006('ugo200_0', 100, 846161781, 828321840, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_115_03', 2)	# 11-12	 **attackbox here**
    GFX_0('UGO_Invincible_Zanzo1', 100)
    Unknown8006(100, 1, 1)
    teleportRelativeX(50000)
    sprite('Action_115_03', 2)	# 13-14	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_04', 2)	# 15-16	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    sprite('Action_115_05', 2)	# 17-18	 **attackbox here**
    sprite('Action_115_06', 2)	# 19-20	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_07', 2)	# 21-22	 **attackbox here**
    teleportRelativeX(50000)
    sprite('Action_115_08', 2)	# 23-24	 **attackbox here**
    teleportRelativeX(50000)
    Unknown8006(100, 1, 1)
    sprite('Action_115_09', 2)	# 25-26	 **attackbox here**
    Unknown8006(100, 1, 1)
    teleportRelativeX(10000)
    sprite('Action_115_10', 2)	# 27-28	 **attackbox here**
    sprite('Action_115_11', 3)	# 29-31	 **attackbox here**
    SFX_3('SE049_SpecialSwing')
    RefreshMultihit()
    Hitstop(12)
    Damage(1600)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackY(30000)
    AirPushbackX(25000)
    YImpluseBeforeWallbounce(2300)
    PushbackX(30400)
    PushbackX(30400)
    GFX_0('UGO_Invincible_Zanzo2', 100)
    Unknown8006(100, 1, 1)
    sprite('Action_115_12', 6)	# 32-37	 **attackbox here**
    sprite('Action_115_13', 8)	# 38-45	 **attackbox here**
    Recovery()
    sprite('Action_115_14', 6)	# 46-51	 **attackbox here**
    sprite('Action_115_15', 4)	# 52-55
    GFX_0('UGO_Invincible_SummonOut', 100)
    sprite('Action_115_16', 4)	# 56-59

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
    Unknown2036(98, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('Action_022_00', 4)	# 3-6
    sprite('Action_022_01', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_013_00', 2)	# 11-12
    sprite('keep', 10)	# 13-22
    if SLOT_58:
        enterState('UltimateAssault_ODDDD')
    else:
        enterState('UltimateAssault_DDD')

@State
def UltimateAssault_DDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(240)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown11092(1)
        Unknown9016(1)
        setInvincible(1)
        Hitstop(5)
        Unknown11001(3, 3, 3)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        PushbackX(12500)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11062(1)
        Unknown9016(1)
        Unknown1084(1)
        Unknown11064(1)
        Unknown2037(0)
    sprite('Action_240_00', 7)	# 1-7
    GFX_0('UGO_UltimateAssault_Start', 100)
    sprite('Action_240_01', 5)	# 8-12
    sprite('Action_240_02', 5)	# 13-17
    sprite('Action_240_01', 5)	# 18-22
    sprite('Action_240_02', 5)	# 23-27
    sprite('Action_240_01', 5)	# 28-32
    sprite('Action_240_02', 5)	# 33-37
    sprite('Action_240_01', 5)	# 38-42
    sprite('Action_240_02', 5)	# 43-47
    sprite('Action_240_01', 5)	# 48-52
    sprite('Action_240_02', 5)	# 53-57
    sprite('Action_240_03', 4)	# 58-61	 **attackbox here**
    sprite('Action_240_04', 5)	# 62-66	 **attackbox here**
    Unknown21015('55474f5f556c74696d61746541737361756c745f537461727400000000000000f501000000000000')
    sprite('Action_240_05', 3)	# 67-69	 **attackbox here**
    sprite('Action_240_06', 2)	# 70-71	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff1', 100)
    sprite('Action_240_07', 3)	# 72-74	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 12000)
    AirPushbackX(9000)
    AirPushbackY(25000)
    Unknown2015(300)
    sprite('Action_240_08', 4)	# 75-78	 **attackbox here**
    sprite('Action_240_09', 5)	# 79-83	 **attackbox here**
    setInvincible(0)
    tag_voice(1, 'ugo251_0', 'ugo251_1', '', '')
    physicsXImpulse(5120)
    teleportRelativeX(30000)
    sprite('Action_240_10', 3)	# 84-86	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff2', 100)
    teleportRelativeX(40000)
    sprite('Action_240_11', 3)	# 87-89	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 9000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(3000)
    AirPushbackY(12000)
    sprite('Action_240_12', 4)	# 90-93	 **attackbox here**
    Unknown1084(1)
    sprite('Action_240_13', 5)	# 94-98	 **attackbox here**
    sprite('Action_240_14', 2)	# 99-100	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff3', 100)
    sprite('Action_240_15', 4)	# 101-104	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 120000)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(1)
    sprite('Action_240_16', 5)	# 105-109	 **attackbox here**
    sprite('Action_240_17', 5)	# 110-114	 **attackbox here**
    sprite('Action_240_18', 3)	# 115-117	 **attackbox here**
    sprite('Action_240_19', 2)	# 118-119	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff4', 100)
    sprite('Action_240_20', 6)	# 120-125	 **attackbox here**
    RefreshMultihit()
    Hitstop(13)
    Unknown11072(1, 400000, 200000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(6000)
    AirPushbackY(24000)
    sprite('Action_240_21', 11)	# 126-136	 **attackbox here**
    sprite('Action_240_22', 6)	# 137-142	 **attackbox here**
    sprite('Action_240_23', 5)	# 143-147	 **attackbox here**
    physicsXImpulse(22000)
    Unknown1028(3000)
    sprite('Action_240_24', 2)	# 148-149	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff5', 100)
    sprite('Action_240_25', 5)	# 150-154	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11072(0, -1, -1)
    Unknown11001(-1, -1, -1)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    YImpluseBeforeWallbounce(200)
    AirPushbackX(0)
    AirPushbackY(5000)
    Unknown1084(1)
    sprite('Action_240_26', 5)	# 155-159	 **attackbox here**
    sprite('Action_240_27', 4)	# 160-163
    GFX_0('UGO_Ultimate_AtkCol_0', 0)
    physicsXImpulse(18000)
    sprite('Action_240_28ex01', 3)	# 164-166	 **attackbox here**
    RefreshMultihit()
    GFX_0('UGO_Ultimate_AtkCol_1', 0)
    AttackLevel_(4)
    Damage(40)
    Unknown11091(100)
    Hitstop(1)
    Unknown11072(1, 250000, 327400)
    Unknown11001(-1, -1, -1)
    Unknown9016(1)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(9000)
    AirPushbackY(600)
    PushbackX(3000)
    YImpluseBeforeWallbounce(2000)
    Unknown2038(2)

    def upon_78():
        Unknown2038(-1)
        if (not SLOT_2):
            clearUponHandler(78)
            Unknown11072(0, -1, -1)
    sprite('Action_240_28ex01', 1)	# 167-167	 **attackbox here**
    sprite('Action_240_29ex01', 2)	# 168-169	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('Action_240_29ex01', 3)	# 170-172	 **attackbox here**
    sprite('Action_240_30ex01', 3)	# 173-175	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 7)	# 176-182	 **attackbox here**
    clearUponHandler(78)
    Unknown11072(0, -1, -1)
    Unknown23027()
    sprite('Action_240_30', 4)	# 183-186
    sprite('Action_240_31', 4)	# 187-190	 **attackbox here**
    Unknown26('UGO_Ultimate_AtkCol_1')
    tag_voice(0, 'ugo252_0', 'ugo252_1', '', '')
    GFX_0('UGO_UltimateAssault_AtkEff_Fini', 100)
    teleportRelativeX(-50000)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_32', 3)	# 191-193	 **attackbox here**
    RefreshMultihit()
    Damage(680)
    Unknown11001(0, 0, 0)
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Hitstop(30)
    AirPushbackX(65000)
    AirPushbackY(500)
    YImpluseBeforeWallbounce(50)
    PushbackX(19900)
    Unknown11064(0)

    def upon_12():
        SFX_3('SE005')
        SFX_3('SE_BigBomb')
    sprite('Action_240_33', 19)	# 194-212	 **attackbox here**
    Unknown2015(0)
    Unknown23027()
    sprite('Action_240_34', 8)	# 213-220
    sprite('Action_240_35', 7)	# 221-227
    teleportRelativeX(-30000)
    loopRest()

@State
def UltimateAssault_ODDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(200)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown11092(1)
        Unknown9016(1)
        setInvincible(1)
        Hitstop(5)
        Unknown11001(3, 3, 3)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        PushbackX(12500)
        Unknown11064(1)
        Unknown11062(1)
        Unknown9016(1)
        Unknown1084(1)
        Unknown11032('40420f0000000000ffffffffffffffff')
    sprite('Action_240_00', 7)	# 1-7
    GFX_0('UGO_UltimateAssault_Start', 100)
    sprite('Action_240_01', 5)	# 8-12
    sprite('Action_240_02', 5)	# 13-17
    sprite('Action_240_01', 5)	# 18-22
    sprite('Action_240_02', 5)	# 23-27
    sprite('Action_240_01', 5)	# 28-32
    sprite('Action_240_02', 5)	# 33-37
    sprite('Action_240_01', 5)	# 38-42
    sprite('Action_240_02', 5)	# 43-47
    sprite('Action_240_01', 5)	# 48-52
    sprite('Action_240_02', 5)	# 53-57
    sprite('Action_240_03', 4)	# 58-61	 **attackbox here**
    sprite('Action_240_04', 5)	# 62-66	 **attackbox here**
    Unknown21015('55474f5f556c74696d61746541737361756c745f537461727400000000000000f501000000000000')
    sprite('Action_240_05', 3)	# 67-69	 **attackbox here**
    sprite('Action_240_06', 2)	# 70-71	 **attackbox here**
    GFX_0('UGO_UltimateAssault_AtkEff1', 100)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_07', 3)	# 72-74	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 12000)
    AirPushbackX(9000)
    AirPushbackY(25000)
    Unknown2015(300)
    sprite('Action_240_08', 4)	# 75-78	 **attackbox here**
    sprite('Action_240_09', 5)	# 79-83	 **attackbox here**
    setInvincible(0)
    tag_voice(1, 'ugo251_0', 'ugo251_1', '', '')
    physicsXImpulse(5120)
    teleportRelativeX(30000)
    sprite('Action_240_10', 3)	# 84-86	 **attackbox here**
    GFX_0('UGO_UltimateAssault_AtkEff2', 100)
    SFX_3('SE048_LongSwingC')
    teleportRelativeX(40000)
    sprite('Action_240_11', 3)	# 87-89	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 9000)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    AirPushbackX(3000)
    AirPushbackY(12000)
    sprite('Action_240_12', 4)	# 90-93	 **attackbox here**
    Unknown1084(1)
    sprite('Action_240_13', 5)	# 94-98	 **attackbox here**
    sprite('Action_240_14', 2)	# 99-100	 **attackbox here**
    GFX_0('UGO_UltimateAssault_AtkEff3', 100)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_15', 4)	# 101-104	 **attackbox here**
    RefreshMultihit()
    Unknown11072(1, 400000, 120000)
    AirHitstunAnimation(1)
    GroundedHitstunAnimation(1)
    sprite('Action_240_16', 5)	# 105-109	 **attackbox here**
    sprite('Action_240_17', 5)	# 110-114	 **attackbox here**
    sprite('Action_240_18', 3)	# 115-117	 **attackbox here**
    sprite('Action_240_19', 2)	# 118-119	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff4', 100)
    sprite('Action_240_20', 6)	# 120-125	 **attackbox here**
    RefreshMultihit()
    Hitstop(8)
    Unknown11072(1, 400000, 200000)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(6000)
    AirPushbackY(24000)
    sprite('Action_240_21', 11)	# 126-136	 **attackbox here**
    sprite('Action_240_22', 6)	# 137-142	 **attackbox here**
    sprite('Action_240_23', 5)	# 143-147	 **attackbox here**
    physicsXImpulse(22000)
    Unknown1028(3000)
    sprite('Action_240_24', 2)	# 148-149	 **attackbox here**
    SFX_3('SE048_LongSwingC')
    GFX_0('UGO_UltimateAssault_AtkEff5', 100)
    sprite('Action_240_25', 5)	# 150-154	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11072(0, -1, -1)
    Unknown11001(0, 0, 0)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    YImpluseBeforeWallbounce(200)
    AirPushbackX(0)
    AirPushbackY(5000)
    Unknown1084(1)
    sprite('Action_240_26', 5)	# 155-159	 **attackbox here**
    sprite('Action_240_27', 4)	# 160-163
    GFX_0('UGO_Ultimate_AtkCol_0', 0)
    physicsXImpulse(18000)
    sprite('Action_240_28ex01', 3)	# 164-166	 **attackbox here**
    GFX_0('UGO_Ultimate_AtkCol_1_OD', 0)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(35)
    Unknown11091(100)
    Hitstop(1)
    Unknown11072(1, 250000, 250000)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(8000)
    AirPushbackY(600)
    PushbackX(3000)
    YImpluseBeforeWallbounce(2000)
    Unknown2038(2)

    def upon_78():
        Unknown2038(-1)
        if (not SLOT_2):
            clearUponHandler(78)
            Unknown11072(0, -1, -1)
    sprite('Action_240_28ex01', 1)	# 167-167	 **attackbox here**
    sprite('Action_240_29ex01', 2)	# 168-169	 **attackbox here**
    Unknown1084(1)
    sprite('Action_240_29ex01', 3)	# 170-172	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 6)	# 173-178	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 5)	# 179-183	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 184-187	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 188-191	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 192-195	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 196-199	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 4)	# 200-203	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30ex01', 5)	# 204-208	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_30', 3)	# 209-211
    clearUponHandler(78)
    Unknown11072(0, -1, -1)
    Unknown23027()
    Unknown23027()
    sprite('Action_240_31', 4)	# 212-215	 **attackbox here**
    Unknown26('UGO_Ultimate_AtkCol_1_OD')
    tag_voice(0, 'ugo252_0', 'ugo252_1', '', '')
    GFX_0('UGO_UltimateAssault_AtkEff_Fini', 100)
    teleportRelativeX(-50000)
    SFX_3('SE048_LongSwingC')
    sprite('Action_240_32', 1)	# 216-216	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    Damage(200)
    Unknown11001(0, 0, 0)
    Hitstop(3)
    AirPushbackX(65000)
    AirPushbackY(500)
    YImpluseBeforeWallbounce(50)
    PushbackX(19800)
    sprite('Action_240_32', 1)	# 217-217	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_32', 1)	# 218-218	 **attackbox here**
    RefreshMultihit()
    Damage(750)
    Hitstop(30)
    Unknown11064(0)

    def upon_12():
        SFX_3('SE005')
        SFX_3('SE_BigBomb')
    sprite('Action_240_33', 19)	# 219-237	 **attackbox here**
    Unknown2015(0)
    Unknown23027()
    sprite('Action_240_34', 8)	# 238-245
    sprite('Action_240_35', 7)	# 246-252
    teleportRelativeX(-30000)
    loopRest()

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
        Unknown2004(1, 0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('Action_161_00', 3)	# 121-123	 **attackbox here**
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-300000)
    Unknown1007(2000000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('Action_161_01', 32767)	# 124-32890	 **attackbox here**
    label(9)
    sprite('Action_161_02', 2)	# 32891-32892	 **attackbox here**
    Unknown2016(-1)
    Unknown2015(-1)
    GFX_0('UGO_StrikeB_Zanzou', 100)
    Unknown1084(1)
    SFX_3('SE049_SpecialSwing')
    sprite('Action_161_03', 1)	# 32893-32893	 **attackbox here**
    sprite('Action_161_04', 5)	# 32894-32898	 **attackbox here**
    Unknown8000(-1, 1, 1)
    Unknown8004(100, 1, 1)
    ScreenShake(8000, 3500)
    sprite('Action_161_05', 7)	# 32899-32905	 **attackbox here**
    sprite('Action_161_06', 6)	# 32906-32911	 **attackbox here**
    sprite('Action_161_07', 6)	# 32912-32917
    GFX_0('UGO_StrikeB_SummonOut', 100)
    sprite('Action_161_08', 5)	# 32918-32922
    sprite('Action_161_09', 4)	# 32923-32926

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_03', 3)	# 1-3
    sprite('Action_312_04', 26)	# 4-29
    sprite('Action_312_05', 4)	# 30-33
    sprite('Action_312_06', 4)	# 34-37
    sprite('Action_312_07', 4)	# 38-41
    sprite('Action_312_08', 4)	# 42-45
    sprite('Action_014_00', 3)	# 46-48
    sprite('Action_014_01', 5)	# 49-53
    sprite('Action_014_02', 6)	# 54-59
    sprite('Action_000_00', 30)	# 60-89	 **attackbox here**

@Subroutine
def MouthTableInit():
    Unknown18011('ugo000', 12643, 12641, 25396, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo500', 12641, 14179, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo501', 14433, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo502', 12641, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo503', 12641, 14179, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo504', 12641, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo505', 12641, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo520', 12643, 14177, 14179, 12641, 25394, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo403_0', 12643, 12641, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo600bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo601bmk', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 13361, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo600bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo601btg', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo601pbc', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo600pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo601rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 14131, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo600rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo601uca', 12643, 14177, 14179, 14177, 14179, 12641, 25392, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo600uwa', 12643, 13153, 25398, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo601uyu', 12643, 14177, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo602rrb', 12643, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo701bhz', 12643, 14177, 14179, 14177, 14179, 12641, 25392, 24887, 25399, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo701bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 14135, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo701bph', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 13105, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo700btg', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 12849, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo700pyu', 12643, 24880, 25401, 24889, 25401, 14642, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo701rbl', 12899, 24880, 25399, 24887, 25399, 14131, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo701rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo700uca', 12643, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo701uwa', 12643, 14177, 14179, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14435, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ugo700uyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 14132, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('btg')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bhz')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('uyu')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('Action_051_02', 5)	# 2-6	 **attackbox here**
    sprite('Action_051_03', 5)	# 7-11	 **attackbox here**
    Unknown7006('ugo500', 100, 896493429, 13104, 0, 0, 100, 896493429, 13360, 0, 0, 100, 896493429, 13616, 0, 0, 100)
    sprite('Action_051_02', 5)	# 12-16	 **attackbox here**
    sprite('Action_051_03', 5)	# 17-21	 **attackbox here**
    sprite('Action_051_02', 5)	# 22-26	 **attackbox here**
    sprite('Action_051_03', 5)	# 27-31	 **attackbox here**
    sprite('Action_051_02', 5)	# 32-36	 **attackbox here**
    sprite('Action_051_03', 5)	# 37-41	 **attackbox here**
    sprite('Action_051_02', 5)	# 42-46	 **attackbox here**
    sprite('Action_051_03', 5)	# 47-51	 **attackbox here**
    sprite('Action_051_02', 5)	# 52-56	 **attackbox here**
    sprite('Action_051_03', 5)	# 57-61	 **attackbox here**
    sprite('Action_051_04', 5)	# 62-66	 **attackbox here**
    sprite('Action_051_05', 5)	# 67-71	 **attackbox here**
    sprite('Action_051_04', 5)	# 72-76	 **attackbox here**
    sprite('Action_051_05', 5)	# 77-81	 **attackbox here**
    sprite('Action_051_04', 5)	# 82-86	 **attackbox here**
    sprite('Action_051_05', 5)	# 87-91	 **attackbox here**
    sprite('Action_051_04', 5)	# 92-96	 **attackbox here**
    sprite('Action_051_05', 5)	# 97-101	 **attackbox here**
    sprite('Action_051_06', 5)	# 102-106	 **attackbox here**
    sprite('Action_051_07', 5)	# 107-111	 **attackbox here**
    sprite('Action_051_08', 6)	# 112-117	 **attackbox here**
    sprite('Action_051_09', 6)	# 118-123	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 124-131	 **attackbox here**
    Unknown23018(1)
    sprite('Action_051_11', 4)	# 132-135
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 136-139
    sprite('Action_051_13', 5)	# 140-144
    sprite('Action_051_14', 5)	# 145-149
    sprite('Action_051_15', 5)	# 150-154
    sprite('Action_051_16', 5)	# 155-159
    label(1)
    sprite('Action_000_00', 5)	# 160-164	 **attackbox here**
    sprite('Action_000_01', 5)	# 165-169	 **attackbox here**
    sprite('Action_000_02', 6)	# 170-175	 **attackbox here**
    sprite('Action_000_03', 7)	# 176-182	 **attackbox here**
    sprite('Action_000_04', 7)	# 183-189	 **attackbox here**
    sprite('Action_000_05', 7)	# 190-196	 **attackbox here**
    sprite('Action_000_06', 7)	# 197-203	 **attackbox here**
    sprite('Action_000_07', 7)	# 204-210	 **attackbox here**
    sprite('Action_000_08', 7)	# 211-217	 **attackbox here**
    sprite('Action_000_09', 7)	# 218-224	 **attackbox here**
    sprite('Action_000_10', 7)	# 225-231	 **attackbox here**
    sprite('Action_000_11', 6)	# 232-237	 **attackbox here**
    sprite('Action_000_12', 5)	# 238-242	 **attackbox here**
    sprite('Action_000_13', 5)	# 243-247	 **attackbox here**
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('Action_050_00', 5)	# 248-252
    sprite('Action_050_01', 5)	# 253-257
    Unknown7006('ugo501', 100, 896493429, 12848, 0, 0, 100, 896493429, 13360, 0, 0, 100, 896493429, 13616, 0, 0, 100)
    sprite('Action_050_02', 5)	# 258-262
    sprite('Action_050_03', 5)	# 263-267
    sprite('Action_050_04', 5)	# 268-272
    label(11)
    sprite('Action_050_01', 5)	# 273-277
    sprite('Action_050_02', 5)	# 278-282
    sprite('Action_050_03', 5)	# 283-287
    sprite('Action_050_04', 5)	# 288-292
    if SLOT_97:
        _gotolabel(11)
    sprite('Action_050_05', 4)	# 293-296
    sprite('Action_050_06', 4)	# 297-300
    sprite('Action_050_07', 4)	# 301-304
    sprite('Action_050_08', 3)	# 305-307
    sprite('Action_050_09', 5)	# 308-312
    sprite('Action_050_10', 5)	# 313-317
    sprite('Action_050_11', 5)	# 318-322
    Unknown23018(1)
    label(12)
    sprite('Action_000_00', 5)	# 323-327	 **attackbox here**
    sprite('Action_000_01', 5)	# 328-332	 **attackbox here**
    sprite('Action_000_02', 6)	# 333-338	 **attackbox here**
    sprite('Action_000_03', 7)	# 339-345	 **attackbox here**
    sprite('Action_000_04', 7)	# 346-352	 **attackbox here**
    sprite('Action_000_05', 7)	# 353-359	 **attackbox here**
    sprite('Action_000_06', 7)	# 360-366	 **attackbox here**
    sprite('Action_000_07', 7)	# 367-373	 **attackbox here**
    sprite('Action_000_08', 7)	# 374-380	 **attackbox here**
    sprite('Action_000_09', 7)	# 381-387	 **attackbox here**
    sprite('Action_000_10', 7)	# 388-394	 **attackbox here**
    sprite('Action_000_11', 6)	# 395-400	 **attackbox here**
    sprite('Action_000_12', 5)	# 401-405	 **attackbox here**
    sprite('Action_000_13', 5)	# 406-410	 **attackbox here**
    gotoLabel(12)
    ExitState()
    label(20)
    sprite('Action_000_00', 1)	# 411-411	 **attackbox here**
    SFX_1('ugo700uyu')
    label(21)
    sprite('Action_000_00', 5)	# 412-416	 **attackbox here**
    sprite('Action_000_01', 5)	# 417-421	 **attackbox here**
    sprite('Action_000_02', 6)	# 422-427	 **attackbox here**
    sprite('Action_000_03', 7)	# 428-434	 **attackbox here**
    sprite('Action_000_04', 7)	# 435-441	 **attackbox here**
    sprite('Action_000_05', 7)	# 442-448	 **attackbox here**
    sprite('Action_000_06', 7)	# 449-455	 **attackbox here**
    sprite('Action_000_07', 7)	# 456-462	 **attackbox here**
    sprite('Action_000_08', 7)	# 463-469	 **attackbox here**
    sprite('Action_000_09', 7)	# 470-476	 **attackbox here**
    sprite('Action_000_10', 7)	# 477-483	 **attackbox here**
    sprite('Action_000_11', 6)	# 484-489	 **attackbox here**
    sprite('Action_000_12', 5)	# 490-494	 **attackbox here**
    sprite('Action_000_13', 5)	# 495-499	 **attackbox here**
    gotoLabel(21)
    label(100)
    sprite('Action_051_02', 1)	# 500-500	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2019(0)
        Unknown2037(1)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_051_02', 5)	# 501-505	 **attackbox here**
    sprite('Action_051_03', 5)	# 506-510	 **attackbox here**
    gotoLabel(101)
    label(102)
    sprite('Action_051_02', 5)	# 511-515	 **attackbox here**
    sprite('Action_051_03', 5)	# 516-520	 **attackbox here**
    SFX_1('ugo601btg')
    sprite('Action_051_02', 5)	# 521-525	 **attackbox here**
    sprite('Action_051_03', 5)	# 526-530	 **attackbox here**
    sprite('Action_051_04', 5)	# 531-535	 **attackbox here**
    sprite('Action_051_05', 5)	# 536-540	 **attackbox here**
    sprite('Action_051_04', 5)	# 541-545	 **attackbox here**
    sprite('Action_051_05', 5)	# 546-550	 **attackbox here**
    sprite('Action_051_04', 5)	# 551-555	 **attackbox here**
    sprite('Action_051_05', 5)	# 556-560	 **attackbox here**
    sprite('Action_051_04', 5)	# 561-565	 **attackbox here**
    sprite('Action_051_05', 5)	# 566-570	 **attackbox here**
    sprite('Action_051_06', 5)	# 571-575	 **attackbox here**
    sprite('Action_051_07', 5)	# 576-580	 **attackbox here**
    sprite('Action_051_08', 6)	# 581-586	 **attackbox here**
    sprite('Action_051_09', 6)	# 587-592	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 593-600	 **attackbox here**
    if SLOT_2:
        Unknown2019(-500)
    sprite('Action_051_11', 4)	# 601-604
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 605-608
    sprite('Action_051_13', 5)	# 609-613
    sprite('Action_051_14', 5)	# 614-618
    sprite('Action_051_15', 5)	# 619-623
    sprite('Action_051_16', 5)	# 624-628
    label(103)
    sprite('Action_000_00', 5)	# 629-633	 **attackbox here**
    sprite('Action_000_01', 5)	# 634-638	 **attackbox here**
    sprite('Action_000_02', 6)	# 639-644	 **attackbox here**
    sprite('Action_000_03', 7)	# 645-651	 **attackbox here**
    sprite('Action_000_04', 7)	# 652-658	 **attackbox here**
    sprite('Action_000_05', 7)	# 659-665	 **attackbox here**
    sprite('Action_000_06', 7)	# 666-672	 **attackbox here**
    sprite('Action_000_07', 7)	# 673-679	 **attackbox here**
    sprite('Action_000_08', 7)	# 680-686	 **attackbox here**
    sprite('Action_000_09', 7)	# 687-693	 **attackbox here**
    sprite('Action_000_10', 7)	# 694-700	 **attackbox here**
    sprite('Action_000_11', 6)	# 701-706	 **attackbox here**
    sprite('Action_000_12', 5)	# 707-711	 **attackbox here**
    sprite('Action_000_13', 5)	# 712-716	 **attackbox here**
    if SLOT_97:
        _gotolabel(103)
    sprite('Action_000_00', 1)	# 717-717	 **attackbox here**
    Unknown21011(60)
    label(104)
    sprite('Action_000_00', 5)	# 718-722	 **attackbox here**
    sprite('Action_000_01', 5)	# 723-727	 **attackbox here**
    sprite('Action_000_02', 6)	# 728-733	 **attackbox here**
    sprite('Action_000_03', 7)	# 734-740	 **attackbox here**
    sprite('Action_000_04', 7)	# 741-747	 **attackbox here**
    sprite('Action_000_05', 7)	# 748-754	 **attackbox here**
    sprite('Action_000_06', 7)	# 755-761	 **attackbox here**
    sprite('Action_000_07', 7)	# 762-768	 **attackbox here**
    sprite('Action_000_08', 7)	# 769-775	 **attackbox here**
    sprite('Action_000_09', 7)	# 776-782	 **attackbox here**
    sprite('Action_000_10', 7)	# 783-789	 **attackbox here**
    sprite('Action_000_11', 6)	# 790-795	 **attackbox here**
    sprite('Action_000_12', 5)	# 796-800	 **attackbox here**
    sprite('Action_000_13', 5)	# 801-805	 **attackbox here**
    gotoLabel(104)
    ExitState()
    label(110)
    sprite('Action_051_02', 1)	# 806-806	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2019(1000)
    Unknown2037(8)
    sprite('Action_051_02', 5)	# 807-811	 **attackbox here**
    sprite('Action_051_03', 5)	# 812-816	 **attackbox here**
    SFX_1('ugo600bhz')
    label(111)
    sprite('Action_051_02', 5)	# 817-821	 **attackbox here**
    sprite('Action_051_03', 5)	# 822-826	 **attackbox here**
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(111)
    sprite('Action_051_04', 5)	# 827-831	 **attackbox here**
    sprite('Action_051_05', 5)	# 832-836	 **attackbox here**
    sprite('Action_051_04', 5)	# 837-841	 **attackbox here**
    sprite('Action_051_05', 5)	# 842-846	 **attackbox here**
    sprite('Action_051_04', 5)	# 847-851	 **attackbox here**
    sprite('Action_051_05', 5)	# 852-856	 **attackbox here**
    sprite('Action_051_04', 5)	# 857-861	 **attackbox here**
    sprite('Action_051_05', 5)	# 862-866	 **attackbox here**
    sprite('Action_051_06', 5)	# 867-871	 **attackbox here**
    sprite('Action_051_07', 5)	# 872-876	 **attackbox here**
    sprite('Action_051_08', 6)	# 877-882	 **attackbox here**
    sprite('Action_051_09', 6)	# 883-888	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 889-896	 **attackbox here**
    sprite('Action_051_11', 4)	# 897-900
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 901-904
    sprite('Action_051_13', 5)	# 905-909
    sprite('Action_051_14', 5)	# 910-914
    sprite('Action_051_15', 5)	# 915-919
    sprite('Action_051_16', 5)	# 920-924
    label(112)
    sprite('Action_000_00', 5)	# 925-929	 **attackbox here**
    sprite('Action_000_01', 5)	# 930-934	 **attackbox here**
    sprite('Action_000_02', 6)	# 935-940	 **attackbox here**
    sprite('Action_000_03', 7)	# 941-947	 **attackbox here**
    sprite('Action_000_04', 7)	# 948-954	 **attackbox here**
    sprite('Action_000_05', 7)	# 955-961	 **attackbox here**
    sprite('Action_000_06', 7)	# 962-968	 **attackbox here**
    sprite('Action_000_07', 7)	# 969-975	 **attackbox here**
    sprite('Action_000_08', 7)	# 976-982	 **attackbox here**
    sprite('Action_000_09', 7)	# 983-989	 **attackbox here**
    sprite('Action_000_10', 7)	# 990-996	 **attackbox here**
    sprite('Action_000_11', 6)	# 997-1002	 **attackbox here**
    sprite('Action_000_12', 5)	# 1003-1007	 **attackbox here**
    sprite('Action_000_13', 5)	# 1008-1012	 **attackbox here**
    if SLOT_97:
        _gotolabel(112)
    sprite('Action_000_00', 1)	# 1013-1013	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(113)
    sprite('Action_000_00', 5)	# 1014-1018	 **attackbox here**
    sprite('Action_000_01', 5)	# 1019-1023	 **attackbox here**
    sprite('Action_000_02', 6)	# 1024-1029	 **attackbox here**
    sprite('Action_000_03', 7)	# 1030-1036	 **attackbox here**
    sprite('Action_000_04', 7)	# 1037-1043	 **attackbox here**
    sprite('Action_000_05', 7)	# 1044-1050	 **attackbox here**
    sprite('Action_000_06', 7)	# 1051-1057	 **attackbox here**
    sprite('Action_000_07', 7)	# 1058-1064	 **attackbox here**
    sprite('Action_000_08', 7)	# 1065-1071	 **attackbox here**
    sprite('Action_000_09', 7)	# 1072-1078	 **attackbox here**
    sprite('Action_000_10', 7)	# 1079-1085	 **attackbox here**
    sprite('Action_000_11', 6)	# 1086-1091	 **attackbox here**
    sprite('Action_000_12', 5)	# 1092-1096	 **attackbox here**
    sprite('Action_000_13', 5)	# 1097-1101	 **attackbox here**
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('Action_050_00', 1)	# 1102-1102

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('Action_050_01', 5)	# 1103-1107
    sprite('Action_050_02', 5)	# 1108-1112
    sprite('Action_050_03', 5)	# 1113-1117
    sprite('Action_050_04', 5)	# 1118-1122
    gotoLabel(121)
    label(122)
    sprite('Action_050_01', 1)	# 1123-1123
    SFX_1('ugo601pbc')
    label(123)
    sprite('Action_050_01', 5)	# 1124-1128
    sprite('Action_050_02', 5)	# 1129-1133
    sprite('Action_050_03', 5)	# 1134-1138
    sprite('Action_050_04', 5)	# 1139-1143
    if SLOT_97:
        _gotolabel(123)
    sprite('Action_050_05', 4)	# 1144-1147
    sprite('Action_050_06', 4)	# 1148-1151
    sprite('Action_050_07', 4)	# 1152-1155
    sprite('Action_050_08', 3)	# 1156-1158
    sprite('Action_050_09', 5)	# 1159-1163
    sprite('Action_050_10', 5)	# 1164-1168
    sprite('Action_050_11', 5)	# 1169-1173
    Unknown21011(120)
    label(124)
    sprite('Action_000_00', 5)	# 1174-1178	 **attackbox here**
    sprite('Action_000_01', 5)	# 1179-1183	 **attackbox here**
    sprite('Action_000_02', 6)	# 1184-1189	 **attackbox here**
    sprite('Action_000_03', 7)	# 1190-1196	 **attackbox here**
    sprite('Action_000_04', 7)	# 1197-1203	 **attackbox here**
    sprite('Action_000_05', 7)	# 1204-1210	 **attackbox here**
    sprite('Action_000_06', 7)	# 1211-1217	 **attackbox here**
    sprite('Action_000_07', 7)	# 1218-1224	 **attackbox here**
    sprite('Action_000_08', 7)	# 1225-1231	 **attackbox here**
    sprite('Action_000_09', 7)	# 1232-1238	 **attackbox here**
    sprite('Action_000_10', 7)	# 1239-1245	 **attackbox here**
    sprite('Action_000_11', 6)	# 1246-1251	 **attackbox here**
    sprite('Action_000_12', 5)	# 1252-1256	 **attackbox here**
    sprite('Action_000_13', 5)	# 1257-1261	 **attackbox here**
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('Action_051_02', 1)	# 1262-1262	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1665000)
    Unknown2037(5)
    Unknown2019(1000)
    sprite('Action_051_02', 5)	# 1263-1267	 **attackbox here**
    sprite('Action_051_03', 5)	# 1268-1272	 **attackbox here**
    SFX_1('ugo600pyu')
    label(131)
    sprite('Action_051_02', 5)	# 1273-1277	 **attackbox here**
    sprite('Action_051_03', 5)	# 1278-1282	 **attackbox here**
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(131)
    sprite('Action_051_04', 5)	# 1283-1287	 **attackbox here**
    sprite('Action_051_05', 5)	# 1288-1292	 **attackbox here**
    sprite('Action_051_04', 5)	# 1293-1297	 **attackbox here**
    sprite('Action_051_05', 5)	# 1298-1302	 **attackbox here**
    sprite('Action_051_04', 5)	# 1303-1307	 **attackbox here**
    sprite('Action_051_05', 5)	# 1308-1312	 **attackbox here**
    sprite('Action_051_04', 5)	# 1313-1317	 **attackbox here**
    sprite('Action_051_05', 5)	# 1318-1322	 **attackbox here**
    sprite('Action_051_06', 5)	# 1323-1327	 **attackbox here**
    sprite('Action_051_07', 5)	# 1328-1332	 **attackbox here**
    sprite('Action_051_08', 6)	# 1333-1338	 **attackbox here**
    sprite('Action_051_09', 6)	# 1339-1344	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 1345-1352	 **attackbox here**
    sprite('Action_051_11', 4)	# 1353-1356
    GFX_0('UGO_Entry_SummonOut', 100)
    Unknown36(1)
    Unknown23015(2)
    Unknown35()
    sprite('Action_051_12', 4)	# 1357-1360
    sprite('Action_051_13', 5)	# 1361-1365
    sprite('Action_051_14', 5)	# 1366-1370
    sprite('Action_051_15', 5)	# 1371-1375
    sprite('Action_051_16', 5)	# 1376-1380
    Unknown21011(120)
    label(132)
    sprite('Action_000_00', 5)	# 1381-1385	 **attackbox here**
    sprite('Action_000_01', 5)	# 1386-1390	 **attackbox here**
    sprite('Action_000_02', 6)	# 1391-1396	 **attackbox here**
    sprite('Action_000_03', 7)	# 1397-1403	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_04', 7)	# 1404-1410	 **attackbox here**
    sprite('Action_000_05', 7)	# 1411-1417	 **attackbox here**
    sprite('Action_000_06', 7)	# 1418-1424	 **attackbox here**
    sprite('Action_000_07', 7)	# 1425-1431	 **attackbox here**
    sprite('Action_000_08', 7)	# 1432-1438	 **attackbox here**
    sprite('Action_000_09', 7)	# 1439-1445	 **attackbox here**
    sprite('Action_000_10', 7)	# 1446-1452	 **attackbox here**
    sprite('Action_000_11', 6)	# 1453-1458	 **attackbox here**
    sprite('Action_000_12', 5)	# 1459-1463	 **attackbox here**
    sprite('Action_000_13', 5)	# 1464-1468	 **attackbox here**
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('Action_051_02', 5)	# 1469-1473	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1220000)
    else:
        Unknown1000(-1495000)
    sprite('Action_051_03', 5)	# 1474-1478	 **attackbox here**
    sprite('Action_051_02', 5)	# 1479-1483	 **attackbox here**
    sprite('Action_051_03', 5)	# 1484-1488	 **attackbox here**
    sprite('Action_051_02', 5)	# 1489-1493	 **attackbox here**
    sprite('Action_051_03', 5)	# 1494-1498	 **attackbox here**
    SFX_1('ugo600uwa')
    sprite('Action_051_02', 5)	# 1499-1503	 **attackbox here**
    sprite('Action_051_03', 5)	# 1504-1508	 **attackbox here**
    sprite('Action_051_04', 5)	# 1509-1513	 **attackbox here**
    sprite('Action_051_05', 5)	# 1514-1518	 **attackbox here**
    sprite('Action_051_06', 5)	# 1519-1523	 **attackbox here**
    sprite('Action_051_07', 5)	# 1524-1528	 **attackbox here**
    sprite('Action_051_08', 6)	# 1529-1534	 **attackbox here**
    sprite('Action_051_09', 6)	# 1535-1540	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 1541-1548	 **attackbox here**
    sprite('Action_051_11', 4)	# 1549-1552
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 1553-1556
    sprite('Action_051_13', 5)	# 1557-1561
    sprite('Action_051_14', 5)	# 1562-1566
    sprite('Action_051_15', 5)	# 1567-1571
    sprite('Action_051_16', 5)	# 1572-1576
    label(141)
    sprite('Action_000_00', 5)	# 1577-1581	 **attackbox here**
    sprite('Action_000_01', 5)	# 1582-1586	 **attackbox here**
    sprite('Action_000_02', 6)	# 1587-1592	 **attackbox here**
    sprite('Action_000_03', 7)	# 1593-1599	 **attackbox here**
    sprite('Action_000_04', 7)	# 1600-1606	 **attackbox here**
    sprite('Action_000_05', 7)	# 1607-1613	 **attackbox here**
    sprite('Action_000_06', 7)	# 1614-1620	 **attackbox here**
    sprite('Action_000_07', 7)	# 1621-1627	 **attackbox here**
    sprite('Action_000_08', 7)	# 1628-1634	 **attackbox here**
    sprite('Action_000_09', 7)	# 1635-1641	 **attackbox here**
    sprite('Action_000_10', 7)	# 1642-1648	 **attackbox here**
    sprite('Action_000_11', 6)	# 1649-1654	 **attackbox here**
    sprite('Action_000_12', 5)	# 1655-1659	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_13', 5)	# 1660-1664	 **attackbox here**
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_000_00', 1)	# 1665-1665	 **attackbox here**
    Unknown21011(120)
    label(142)
    sprite('Action_000_00', 5)	# 1666-1670	 **attackbox here**
    sprite('Action_000_01', 5)	# 1671-1675	 **attackbox here**
    sprite('Action_000_02', 6)	# 1676-1681	 **attackbox here**
    sprite('Action_000_03', 7)	# 1682-1688	 **attackbox here**
    sprite('Action_000_04', 7)	# 1689-1695	 **attackbox here**
    sprite('Action_000_05', 7)	# 1696-1702	 **attackbox here**
    sprite('Action_000_06', 7)	# 1703-1709	 **attackbox here**
    sprite('Action_000_07', 7)	# 1710-1716	 **attackbox here**
    sprite('Action_000_08', 7)	# 1717-1723	 **attackbox here**
    sprite('Action_000_09', 7)	# 1724-1730	 **attackbox here**
    sprite('Action_000_10', 7)	# 1731-1737	 **attackbox here**
    sprite('Action_000_11', 6)	# 1738-1743	 **attackbox here**
    sprite('Action_000_12', 5)	# 1744-1748	 **attackbox here**
    sprite('Action_000_13', 5)	# 1749-1753	 **attackbox here**
    gotoLabel(142)
    ExitState()
    label(150)
    sprite('Action_051_02', 5)	# 1754-1758	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_051_03', 5)	# 1759-1763	 **attackbox here**
    SFX_1('ugo600rrb')
    sprite('Action_051_02', 5)	# 1764-1768	 **attackbox here**
    sprite('Action_051_03', 5)	# 1769-1773	 **attackbox here**
    sprite('Action_051_02', 5)	# 1774-1778	 **attackbox here**
    sprite('Action_051_03', 5)	# 1779-1783	 **attackbox here**
    sprite('Action_051_02', 5)	# 1784-1788	 **attackbox here**
    sprite('Action_051_03', 5)	# 1789-1793	 **attackbox here**
    sprite('Action_051_02', 5)	# 1794-1798	 **attackbox here**
    sprite('Action_051_03', 5)	# 1799-1803	 **attackbox here**
    sprite('Action_051_02', 5)	# 1804-1808	 **attackbox here**
    sprite('Action_051_03', 5)	# 1809-1813	 **attackbox here**
    sprite('Action_051_02', 5)	# 1814-1818	 **attackbox here**
    sprite('Action_051_03', 5)	# 1819-1823	 **attackbox here**
    sprite('Action_051_02', 5)	# 1824-1828	 **attackbox here**
    sprite('Action_051_03', 5)	# 1829-1833	 **attackbox here**
    sprite('Action_051_02', 5)	# 1834-1838	 **attackbox here**
    sprite('Action_051_03', 5)	# 1839-1843	 **attackbox here**
    sprite('Action_051_02', 5)	# 1844-1848	 **attackbox here**
    sprite('Action_051_03', 5)	# 1849-1853	 **attackbox here**
    sprite('Action_051_06', 5)	# 1854-1858	 **attackbox here**
    sprite('Action_051_07', 5)	# 1859-1863	 **attackbox here**
    sprite('Action_051_08', 6)	# 1864-1869	 **attackbox here**
    sprite('Action_051_09', 6)	# 1870-1875	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 1876-1883	 **attackbox here**
    sprite('Action_051_11', 4)	# 1884-1887
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 1888-1891
    sprite('Action_051_13', 5)	# 1892-1896
    sprite('Action_051_14', 5)	# 1897-1901
    sprite('Action_051_15', 5)	# 1902-1906
    sprite('Action_051_16', 5)	# 1907-1911

    def upon_40():
        clearUponHandler(40)
        SFX_1('ugo602rrb')
        Unknown23018(1)
    Unknown21007(24, 40)
    label(151)
    sprite('Action_000_00', 5)	# 1912-1916	 **attackbox here**
    sprite('Action_000_01', 5)	# 1917-1921	 **attackbox here**
    sprite('Action_000_02', 6)	# 1922-1927	 **attackbox here**
    sprite('Action_000_03', 7)	# 1928-1934	 **attackbox here**
    sprite('Action_000_04', 7)	# 1935-1941	 **attackbox here**
    sprite('Action_000_05', 7)	# 1942-1948	 **attackbox here**
    sprite('Action_000_06', 7)	# 1949-1955	 **attackbox here**
    sprite('Action_000_07', 7)	# 1956-1962	 **attackbox here**
    sprite('Action_000_08', 7)	# 1963-1969	 **attackbox here**
    sprite('Action_000_09', 7)	# 1970-1976	 **attackbox here**
    sprite('Action_000_10', 7)	# 1977-1983	 **attackbox here**
    sprite('Action_000_11', 6)	# 1984-1989	 **attackbox here**
    sprite('Action_000_12', 5)	# 1990-1994	 **attackbox here**
    sprite('Action_000_13', 5)	# 1995-1999	 **attackbox here**
    gotoLabel(151)
    ExitState()
    label(160)
    sprite('Action_050_00', 1)	# 2000-2000
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
        Unknown2037(2)
    label(161)
    sprite('Action_050_01', 5)	# 2001-2005
    sprite('Action_050_02', 5)	# 2006-2010
    sprite('Action_050_03', 5)	# 2011-2015
    sprite('Action_050_04', 5)	# 2016-2020
    gotoLabel(161)
    label(162)
    sprite('Action_050_01', 5)	# 2021-2025
    SFX_1('ugo601rbl')
    label(163)
    sprite('Action_050_01', 5)	# 2026-2030
    sprite('Action_050_02', 5)	# 2031-2035
    sprite('Action_050_03', 5)	# 2036-2040
    sprite('Action_050_04', 5)	# 2041-2045
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(163)
    sprite('Action_050_05', 4)	# 2046-2049
    sprite('Action_050_06', 4)	# 2050-2053
    sprite('Action_050_07', 4)	# 2054-2057
    sprite('Action_050_08', 3)	# 2058-2060
    sprite('Action_050_09', 5)	# 2061-2065
    sprite('Action_050_10', 5)	# 2066-2070
    sprite('Action_050_11', 5)	# 2071-2075
    Unknown21011(180)
    label(164)
    sprite('Action_000_00', 5)	# 2076-2080	 **attackbox here**
    sprite('Action_000_01', 5)	# 2081-2085	 **attackbox here**
    sprite('Action_000_02', 6)	# 2086-2091	 **attackbox here**
    sprite('Action_000_03', 7)	# 2092-2098	 **attackbox here**
    sprite('Action_000_04', 7)	# 2099-2105	 **attackbox here**
    sprite('Action_000_05', 7)	# 2106-2112	 **attackbox here**
    sprite('Action_000_06', 7)	# 2113-2119	 **attackbox here**
    sprite('Action_000_07', 7)	# 2120-2126	 **attackbox here**
    sprite('Action_000_08', 7)	# 2127-2133	 **attackbox here**
    sprite('Action_000_09', 7)	# 2134-2140	 **attackbox here**
    sprite('Action_000_10', 7)	# 2141-2147	 **attackbox here**
    sprite('Action_000_11', 6)	# 2148-2153	 **attackbox here**
    sprite('Action_000_12', 5)	# 2154-2158	 **attackbox here**
    sprite('Action_000_13', 5)	# 2159-2163	 **attackbox here**
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('Action_051_02', 1)	# 2164-2164	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_051_02', 5)	# 2165-2169	 **attackbox here**
    sprite('Action_051_03', 5)	# 2170-2174	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_051_02', 5)	# 2175-2179	 **attackbox here**
    sprite('Action_051_03', 5)	# 2180-2184	 **attackbox here**
    SFX_1('ugo601bmk')
    sprite('Action_051_02', 5)	# 2185-2189	 **attackbox here**
    sprite('Action_051_03', 5)	# 2190-2194	 **attackbox here**
    sprite('Action_051_04', 5)	# 2195-2199	 **attackbox here**
    sprite('Action_051_05', 5)	# 2200-2204	 **attackbox here**
    sprite('Action_051_04', 5)	# 2205-2209	 **attackbox here**
    sprite('Action_051_05', 5)	# 2210-2214	 **attackbox here**
    sprite('Action_051_04', 5)	# 2215-2219	 **attackbox here**
    sprite('Action_051_05', 5)	# 2220-2224	 **attackbox here**
    sprite('Action_051_04', 5)	# 2225-2229	 **attackbox here**
    sprite('Action_051_05', 5)	# 2230-2234	 **attackbox here**
    sprite('Action_051_06', 5)	# 2235-2239	 **attackbox here**
    sprite('Action_051_07', 5)	# 2240-2244	 **attackbox here**
    sprite('Action_051_08', 6)	# 2245-2250	 **attackbox here**
    sprite('Action_051_09', 6)	# 2251-2256	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 2257-2264	 **attackbox here**
    sprite('Action_051_11', 4)	# 2265-2268
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 2269-2272
    sprite('Action_051_13', 5)	# 2273-2277
    sprite('Action_051_14', 5)	# 2278-2282
    sprite('Action_051_15', 5)	# 2283-2287
    sprite('Action_051_16', 5)	# 2288-2292
    Unknown21011(120)
    label(173)
    sprite('Action_000_00', 5)	# 2293-2297	 **attackbox here**
    sprite('Action_000_01', 5)	# 2298-2302	 **attackbox here**
    sprite('Action_000_02', 6)	# 2303-2308	 **attackbox here**
    sprite('Action_000_03', 7)	# 2309-2315	 **attackbox here**
    sprite('Action_000_04', 7)	# 2316-2322	 **attackbox here**
    sprite('Action_000_05', 7)	# 2323-2329	 **attackbox here**
    sprite('Action_000_06', 7)	# 2330-2336	 **attackbox here**
    sprite('Action_000_07', 7)	# 2337-2343	 **attackbox here**
    sprite('Action_000_08', 7)	# 2344-2350	 **attackbox here**
    sprite('Action_000_09', 7)	# 2351-2357	 **attackbox here**
    sprite('Action_000_10', 7)	# 2358-2364	 **attackbox here**
    sprite('Action_000_11', 6)	# 2365-2370	 **attackbox here**
    sprite('Action_000_12', 5)	# 2371-2375	 **attackbox here**
    sprite('Action_000_13', 5)	# 2376-2380	 **attackbox here**
    gotoLabel(173)
    ExitState()
    label(180)
    sprite('Action_050_00', 1)	# 2381-2381
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
        SFX_1('ugo601uca')
        Unknown2037(7)
    label(181)
    sprite('Action_050_01', 5)	# 2382-2386
    sprite('Action_050_02', 5)	# 2387-2391
    sprite('Action_050_03', 5)	# 2392-2396
    sprite('Action_050_04', 5)	# 2397-2401
    gotoLabel(181)
    label(182)
    sprite('Action_050_01', 5)	# 2402-2406
    sprite('Action_050_02', 5)	# 2407-2411
    sprite('Action_050_03', 5)	# 2412-2416
    sprite('Action_050_04', 5)	# 2417-2421
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(182)
    sprite('Action_050_05', 4)	# 2422-2425
    sprite('Action_050_06', 4)	# 2426-2429
    sprite('Action_050_07', 4)	# 2430-2433
    sprite('Action_050_08', 3)	# 2434-2436
    sprite('Action_050_09', 5)	# 2437-2441
    sprite('Action_050_10', 5)	# 2442-2446
    sprite('Action_050_11', 5)	# 2447-2451
    Unknown23018(1)
    label(183)
    sprite('Action_000_00', 5)	# 2452-2456	 **attackbox here**
    sprite('Action_000_01', 5)	# 2457-2461	 **attackbox here**
    sprite('Action_000_02', 6)	# 2462-2467	 **attackbox here**
    sprite('Action_000_03', 7)	# 2468-2474	 **attackbox here**
    sprite('Action_000_04', 7)	# 2475-2481	 **attackbox here**
    sprite('Action_000_05', 7)	# 2482-2488	 **attackbox here**
    sprite('Action_000_06', 7)	# 2489-2495	 **attackbox here**
    sprite('Action_000_07', 7)	# 2496-2502	 **attackbox here**
    sprite('Action_000_08', 7)	# 2503-2509	 **attackbox here**
    sprite('Action_000_09', 7)	# 2510-2516	 **attackbox here**
    sprite('Action_000_10', 7)	# 2517-2523	 **attackbox here**
    sprite('Action_000_11', 6)	# 2524-2529	 **attackbox here**
    sprite('Action_000_12', 5)	# 2530-2534	 **attackbox here**
    sprite('Action_000_13', 5)	# 2535-2539	 **attackbox here**
    gotoLabel(183)
    ExitState()
    label(190)
    sprite('Action_051_02', 1)	# 2540-2540	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_051_02', 5)	# 2541-2545	 **attackbox here**
    sprite('Action_051_03', 5)	# 2546-2550	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('Action_051_02', 5)	# 2551-2555	 **attackbox here**
    sprite('Action_051_03', 5)	# 2556-2560	 **attackbox here**
    SFX_1('ugo601uyu')
    sprite('Action_051_02', 5)	# 2561-2565	 **attackbox here**
    sprite('Action_051_03', 5)	# 2566-2570	 **attackbox here**
    sprite('Action_051_04', 5)	# 2571-2575	 **attackbox here**
    sprite('Action_051_05', 5)	# 2576-2580	 **attackbox here**
    sprite('Action_051_04', 5)	# 2581-2585	 **attackbox here**
    sprite('Action_051_05', 5)	# 2586-2590	 **attackbox here**
    sprite('Action_051_04', 5)	# 2591-2595	 **attackbox here**
    sprite('Action_051_05', 5)	# 2596-2600	 **attackbox here**
    sprite('Action_051_04', 5)	# 2601-2605	 **attackbox here**
    sprite('Action_051_05', 5)	# 2606-2610	 **attackbox here**
    sprite('Action_051_06', 5)	# 2611-2615	 **attackbox here**
    sprite('Action_051_07', 5)	# 2616-2620	 **attackbox here**
    sprite('Action_051_08', 6)	# 2621-2626	 **attackbox here**
    sprite('Action_051_09', 6)	# 2627-2632	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 2633-2640	 **attackbox here**
    sprite('Action_051_11', 4)	# 2641-2644
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 2645-2648
    sprite('Action_051_13', 5)	# 2649-2653
    sprite('Action_051_14', 5)	# 2654-2658
    sprite('Action_051_15', 5)	# 2659-2663
    sprite('Action_051_16', 5)	# 2664-2668
    Unknown23018(1)
    label(193)
    sprite('Action_000_00', 5)	# 2669-2673	 **attackbox here**
    sprite('Action_000_01', 5)	# 2674-2678	 **attackbox here**
    sprite('Action_000_02', 6)	# 2679-2684	 **attackbox here**
    sprite('Action_000_03', 7)	# 2685-2691	 **attackbox here**
    sprite('Action_000_04', 7)	# 2692-2698	 **attackbox here**
    sprite('Action_000_05', 7)	# 2699-2705	 **attackbox here**
    sprite('Action_000_06', 7)	# 2706-2712	 **attackbox here**
    sprite('Action_000_07', 7)	# 2713-2719	 **attackbox here**
    sprite('Action_000_08', 7)	# 2720-2726	 **attackbox here**
    sprite('Action_000_09', 7)	# 2727-2733	 **attackbox here**
    sprite('Action_000_10', 7)	# 2734-2740	 **attackbox here**
    sprite('Action_000_11', 6)	# 2741-2746	 **attackbox here**
    sprite('Action_000_12', 5)	# 2747-2751	 **attackbox here**
    sprite('Action_000_13', 5)	# 2752-2756	 **attackbox here**
    gotoLabel(193)
    ExitState()
    label(200)
    sprite('Action_051_02', 1)	# 2757-2757	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2019(1000)
    Unknown2037(2)
    sprite('Action_051_02', 5)	# 2758-2762	 **attackbox here**
    sprite('Action_051_03', 5)	# 2763-2767	 **attackbox here**
    SFX_1('ugo600bph')
    label(201)
    sprite('Action_051_02', 5)	# 2768-2772	 **attackbox here**
    sprite('Action_051_03', 5)	# 2773-2777	 **attackbox here**
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(201)
    sprite('Action_051_04', 5)	# 2778-2782	 **attackbox here**
    sprite('Action_051_05', 5)	# 2783-2787	 **attackbox here**
    sprite('Action_051_04', 5)	# 2788-2792	 **attackbox here**
    sprite('Action_051_05', 5)	# 2793-2797	 **attackbox here**
    sprite('Action_051_04', 5)	# 2798-2802	 **attackbox here**
    sprite('Action_051_05', 5)	# 2803-2807	 **attackbox here**
    sprite('Action_051_04', 5)	# 2808-2812	 **attackbox here**
    sprite('Action_051_05', 5)	# 2813-2817	 **attackbox here**
    sprite('Action_051_06', 5)	# 2818-2822	 **attackbox here**
    sprite('Action_051_07', 5)	# 2823-2827	 **attackbox here**
    sprite('Action_051_08', 6)	# 2828-2833	 **attackbox here**
    sprite('Action_051_09', 6)	# 2834-2839	 **attackbox here**
    SFX_3('SE060_BoundMetal')
    sprite('Action_051_10', 8)	# 2840-2847	 **attackbox here**
    sprite('Action_051_11', 4)	# 2848-2851
    GFX_0('UGO_Entry_SummonOut', 100)
    sprite('Action_051_12', 4)	# 2852-2855
    sprite('Action_051_13', 5)	# 2856-2860
    sprite('Action_051_14', 5)	# 2861-2865
    sprite('Action_051_15', 5)	# 2866-2870
    sprite('Action_051_16', 5)	# 2871-2875
    label(202)
    sprite('Action_000_00', 5)	# 2876-2880	 **attackbox here**
    sprite('Action_000_01', 5)	# 2881-2885	 **attackbox here**
    sprite('Action_000_02', 6)	# 2886-2891	 **attackbox here**
    sprite('Action_000_03', 7)	# 2892-2898	 **attackbox here**
    sprite('Action_000_04', 7)	# 2899-2905	 **attackbox here**
    sprite('Action_000_05', 7)	# 2906-2912	 **attackbox here**
    sprite('Action_000_06', 7)	# 2913-2919	 **attackbox here**
    sprite('Action_000_07', 7)	# 2920-2926	 **attackbox here**
    sprite('Action_000_08', 7)	# 2927-2933	 **attackbox here**
    sprite('Action_000_09', 7)	# 2934-2940	 **attackbox here**
    sprite('Action_000_10', 7)	# 2941-2947	 **attackbox here**
    sprite('Action_000_11', 6)	# 2948-2953	 **attackbox here**
    sprite('Action_000_12', 5)	# 2954-2958	 **attackbox here**
    sprite('Action_000_13', 5)	# 2959-2963	 **attackbox here**
    if SLOT_97:
        _gotolabel(202)
    sprite('Action_000_00', 1)	# 2964-2964	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(270)
    label(203)
    sprite('Action_000_00', 5)	# 2965-2969	 **attackbox here**
    sprite('Action_000_01', 5)	# 2970-2974	 **attackbox here**
    sprite('Action_000_02', 6)	# 2975-2980	 **attackbox here**
    sprite('Action_000_03', 7)	# 2981-2987	 **attackbox here**
    sprite('Action_000_04', 7)	# 2988-2994	 **attackbox here**
    sprite('Action_000_05', 7)	# 2995-3001	 **attackbox here**
    sprite('Action_000_06', 7)	# 3002-3008	 **attackbox here**
    sprite('Action_000_07', 7)	# 3009-3015	 **attackbox here**
    sprite('Action_000_08', 7)	# 3016-3022	 **attackbox here**
    sprite('Action_000_09', 7)	# 3023-3029	 **attackbox here**
    sprite('Action_000_10', 7)	# 3030-3036	 **attackbox here**
    sprite('Action_000_11', 6)	# 3037-3042	 **attackbox here**
    sprite('Action_000_12', 5)	# 3043-3047	 **attackbox here**
    sprite('Action_000_13', 5)	# 3048-3052	 **attackbox here**
    gotoLabel(203)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 3053-3053	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 5)	# 3054-3058	 **attackbox here**
    sprite('Action_000_01', 5)	# 3059-3063	 **attackbox here**
    sprite('Action_000_02', 6)	# 3064-3069	 **attackbox here**
    sprite('Action_000_03', 7)	# 3070-3076	 **attackbox here**
    sprite('Action_000_04', 7)	# 3077-3083	 **attackbox here**
    sprite('Action_000_05', 7)	# 3084-3090	 **attackbox here**
    sprite('Action_000_06', 7)	# 3091-3097	 **attackbox here**
    sprite('Action_000_07', 7)	# 3098-3104	 **attackbox here**
    sprite('Action_000_08', 7)	# 3105-3111	 **attackbox here**
    sprite('Action_000_09', 7)	# 3112-3118	 **attackbox here**
    sprite('Action_000_10', 7)	# 3119-3125	 **attackbox here**
    sprite('Action_000_11', 6)	# 3126-3131	 **attackbox here**
    sprite('Action_000_12', 5)	# 3132-3136	 **attackbox here**
    sprite('Action_000_13', 5)	# 3137-3141	 **attackbox here**
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 3142-3143

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
    sprite('Action_046_01', 2)	# 3144-3145
    sprite('Action_046_02', 1)	# 3146-3146
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 3147-3149
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
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('bph'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    sprite('Action_052_00', 2)	# 4-5
    sprite('Action_052_01', 6)	# 6-11
    sprite('Action_052_02', 5)	# 12-16
    sprite('Action_052_03', 3)	# 17-19
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 20-29	 **attackbox here**
    sprite('Action_052_05', 5)	# 30-34	 **attackbox here**
    sprite('Action_052_06', 4)	# 35-38	 **attackbox here**
    sprite('Action_052_07', 3)	# 39-41	 **attackbox here**
    sprite('Action_052_08', 10)	# 42-51	 **attackbox here**
    sprite('Action_052_09', 7)	# 52-58	 **attackbox here**
    sprite('Action_052_10', 5)	# 59-63	 **attackbox here**
    sprite('Action_052_11', 5)	# 64-68	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('ugo524', 100, 896493429, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('ugo402_0', 100, 879716213, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('ugo520', 100, 896493429, 12594, 0, 0, 100, 896493429, 12850, 0, 0, 100, 896493429, 13106, 0, 0, 100)
    Unknown23018(1)
    sprite('Action_052_12', 5)	# 69-73	 **attackbox here**
    sprite('Action_052_13', 5)	# 74-78	 **attackbox here**
    label(1)
    sprite('Action_052_11', 5)	# 79-83	 **attackbox here**
    sprite('Action_052_12', 5)	# 84-88	 **attackbox here**
    sprite('Action_052_13', 5)	# 89-93	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(100)
    sprite('Action_053_00', 5)	# 94-98
    if (not SLOT_158):
        Unknown2019(-1000)
    sprite('Action_053_01', 7)	# 99-105
    SFX_1('ugo700btg')
    sprite('Action_053_02', 7)	# 106-112
    sprite('Action_053_03', 7)	# 113-119
    sprite('Action_053_04', 8)	# 120-127
    sprite('Action_053_05', 7)	# 128-134
    sprite('Action_053_06', 5)	# 135-139
    sprite('Action_053_07', 5)	# 140-144
    label(101)
    sprite('Action_053_08', 1)	# 145-145	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_053_08', 20)	# 146-165	 **attackbox here**
    sprite('Action_053_08', 32767)	# 166-32932	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(180)
    label(110)
    sprite('Action_000_00', 1)	# 32933-32933	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 5)	# 32934-32938	 **attackbox here**
    sprite('Action_000_01', 5)	# 32939-32943	 **attackbox here**
    sprite('Action_000_02', 6)	# 32944-32949	 **attackbox here**
    sprite('Action_000_03', 7)	# 32950-32956	 **attackbox here**
    sprite('Action_000_04', 7)	# 32957-32963	 **attackbox here**
    sprite('Action_000_05', 7)	# 32964-32970	 **attackbox here**
    sprite('Action_000_06', 7)	# 32971-32977	 **attackbox here**
    sprite('Action_000_07', 7)	# 32978-32984	 **attackbox here**
    sprite('Action_000_08', 7)	# 32985-32991	 **attackbox here**
    sprite('Action_000_09', 7)	# 32992-32998	 **attackbox here**
    sprite('Action_000_10', 7)	# 32999-33005	 **attackbox here**
    sprite('Action_000_11', 6)	# 33006-33011	 **attackbox here**
    sprite('Action_000_12', 5)	# 33012-33016	 **attackbox here**
    sprite('Action_000_13', 5)	# 33017-33021	 **attackbox here**
    gotoLabel(111)
    label(112)
    sprite('Action_052_00', 2)	# 33022-33023
    sprite('Action_052_01', 6)	# 33024-33029
    sprite('Action_052_02', 5)	# 33030-33034
    sprite('Action_052_03', 3)	# 33035-33037
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 33038-33047	 **attackbox here**
    sprite('Action_052_05', 5)	# 33048-33052	 **attackbox here**
    sprite('Action_052_06', 4)	# 33053-33056	 **attackbox here**
    sprite('Action_052_07', 3)	# 33057-33059	 **attackbox here**
    sprite('Action_052_08', 10)	# 33060-33069	 **attackbox here**
    sprite('Action_052_09', 7)	# 33070-33076	 **attackbox here**
    sprite('Action_052_10', 5)	# 33077-33081	 **attackbox here**
    sprite('Action_052_11', 5)	# 33082-33086	 **attackbox here**
    SFX_1('ugo701bhz')
    sprite('Action_052_12', 5)	# 33087-33091	 **attackbox here**
    sprite('Action_052_13', 5)	# 33092-33096	 **attackbox here**
    Unknown23018(1)
    label(113)
    sprite('Action_052_11', 5)	# 33097-33101	 **attackbox here**
    sprite('Action_052_12', 5)	# 33102-33106	 **attackbox here**
    sprite('Action_052_13', 5)	# 33107-33111	 **attackbox here**
    gotoLabel(113)
    label(120)
    sprite('Action_000_00', 1)	# 33112-33112	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('Action_000_00', 5)	# 33113-33117	 **attackbox here**
    sprite('Action_000_01', 5)	# 33118-33122	 **attackbox here**
    sprite('Action_000_02', 6)	# 33123-33128	 **attackbox here**
    sprite('Action_000_03', 7)	# 33129-33135	 **attackbox here**
    sprite('Action_000_04', 7)	# 33136-33142	 **attackbox here**
    sprite('Action_000_05', 7)	# 33143-33149	 **attackbox here**
    sprite('Action_000_06', 7)	# 33150-33156	 **attackbox here**
    sprite('Action_000_07', 7)	# 33157-33163	 **attackbox here**
    sprite('Action_000_08', 7)	# 33164-33170	 **attackbox here**
    sprite('Action_000_09', 7)	# 33171-33177	 **attackbox here**
    sprite('Action_000_10', 7)	# 33178-33184	 **attackbox here**
    sprite('Action_000_11', 6)	# 33185-33190	 **attackbox here**
    sprite('Action_000_12', 5)	# 33191-33195	 **attackbox here**
    sprite('Action_000_13', 5)	# 33196-33200	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('Action_052_00', 2)	# 33201-33202
    sprite('Action_052_01', 6)	# 33203-33208
    sprite('Action_052_02', 5)	# 33209-33213
    sprite('Action_052_03', 3)	# 33214-33216
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 33217-33226	 **attackbox here**
    sprite('Action_052_05', 5)	# 33227-33231	 **attackbox here**
    sprite('Action_052_06', 4)	# 33232-33235	 **attackbox here**
    sprite('Action_052_07', 3)	# 33236-33238	 **attackbox here**
    sprite('Action_052_08', 10)	# 33239-33248	 **attackbox here**
    sprite('Action_052_09', 7)	# 33249-33255	 **attackbox here**
    sprite('Action_052_10', 5)	# 33256-33260	 **attackbox here**
    sprite('Action_052_11', 5)	# 33261-33265	 **attackbox here**
    SFX_1('ugo701bmk')
    sprite('Action_052_12', 5)	# 33266-33270	 **attackbox here**
    sprite('Action_052_13', 5)	# 33271-33275	 **attackbox here**
    label(123)
    sprite('Action_052_11', 5)	# 33276-33280	 **attackbox here**
    sprite('Action_052_12', 5)	# 33281-33285	 **attackbox here**
    sprite('Action_052_13', 5)	# 33286-33290	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(123)
    sprite('Action_052_11', 1)	# 33291-33291	 **attackbox here**
    Unknown18008()
    label(124)
    sprite('Action_052_11', 5)	# 33292-33296	 **attackbox here**
    sprite('Action_052_12', 5)	# 33297-33301	 **attackbox here**
    sprite('Action_052_13', 5)	# 33302-33306	 **attackbox here**
    loopRest()
    gotoLabel(124)
    label(130)
    sprite('Action_052_00', 2)	# 33307-33308
    sprite('Action_052_01', 6)	# 33309-33314
    sprite('Action_052_02', 5)	# 33315-33319
    sprite('Action_052_03', 3)	# 33320-33322
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 33323-33332	 **attackbox here**
    sprite('Action_052_05', 5)	# 33333-33337	 **attackbox here**
    sprite('Action_052_06', 4)	# 33338-33341	 **attackbox here**
    sprite('Action_052_07', 3)	# 33342-33344	 **attackbox here**
    sprite('Action_052_08', 10)	# 33345-33354	 **attackbox here**
    sprite('Action_052_09', 7)	# 33355-33361	 **attackbox here**
    sprite('Action_052_10', 5)	# 33362-33366	 **attackbox here**
    sprite('Action_052_11', 5)	# 33367-33371	 **attackbox here**
    SFX_1('ugo700pbc')
    sprite('Action_052_12', 5)	# 33372-33376	 **attackbox here**
    sprite('Action_052_13', 5)	# 33377-33381	 **attackbox here**
    label(131)
    sprite('Action_052_11', 5)	# 33382-33386	 **attackbox here**
    sprite('Action_052_12', 5)	# 33387-33391	 **attackbox here**
    sprite('Action_052_13', 5)	# 33392-33396	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_052_11', 1)	# 33397-33397	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(150)
    label(132)
    sprite('Action_052_11', 5)	# 33398-33402	 **attackbox here**
    sprite('Action_052_12', 5)	# 33403-33407	 **attackbox here**
    sprite('Action_052_13', 5)	# 33408-33412	 **attackbox here**
    loopRest()
    gotoLabel(132)
    label(140)
    sprite('Action_052_00', 2)	# 33413-33414
    if SLOT_158:
        Unknown2019(-1000)
    sprite('Action_052_01', 6)	# 33415-33420
    sprite('Action_052_02', 5)	# 33421-33425
    sprite('Action_052_03', 3)	# 33426-33428
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 33429-33438	 **attackbox here**
    sprite('Action_052_05', 5)	# 33439-33443	 **attackbox here**
    sprite('Action_052_06', 4)	# 33444-33447	 **attackbox here**
    sprite('Action_052_07', 3)	# 33448-33450	 **attackbox here**
    sprite('Action_052_08', 10)	# 33451-33460	 **attackbox here**
    sprite('Action_052_09', 7)	# 33461-33467	 **attackbox here**
    sprite('Action_052_10', 5)	# 33468-33472	 **attackbox here**
    sprite('Action_052_11', 5)	# 33473-33477	 **attackbox here**
    SFX_1('ugo700pyu')
    sprite('Action_052_12', 5)	# 33478-33482	 **attackbox here**
    sprite('Action_052_13', 5)	# 33483-33487	 **attackbox here**
    label(141)
    sprite('Action_052_11', 5)	# 33488-33492	 **attackbox here**
    sprite('Action_052_12', 5)	# 33493-33497	 **attackbox here**
    sprite('Action_052_13', 5)	# 33498-33502	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_052_11', 5)	# 33503-33507	 **attackbox here**
    sprite('Action_052_12', 5)	# 33508-33512	 **attackbox here**
    sprite('Action_052_13', 5)	# 33513-33517	 **attackbox here**
    sprite('Action_052_11', 5)	# 33518-33522	 **attackbox here**
    sprite('Action_052_12', 5)	# 33523-33527	 **attackbox here**
    sprite('Action_052_13', 5)	# 33528-33532	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(142)
    sprite('Action_052_11', 5)	# 33533-33537	 **attackbox here**
    sprite('Action_052_12', 5)	# 33538-33542	 **attackbox here**
    sprite('Action_052_13', 5)	# 33543-33547	 **attackbox here**
    loopRest()
    gotoLabel(142)
    label(150)
    sprite('Action_000_00', 1)	# 33548-33548	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Action_000_00', 5)	# 33549-33553	 **attackbox here**
    sprite('Action_000_01', 5)	# 33554-33558	 **attackbox here**
    sprite('Action_000_02', 6)	# 33559-33564	 **attackbox here**
    sprite('Action_000_03', 7)	# 33565-33571	 **attackbox here**
    sprite('Action_000_04', 7)	# 33572-33578	 **attackbox here**
    sprite('Action_000_05', 7)	# 33579-33585	 **attackbox here**
    sprite('Action_000_06', 7)	# 33586-33592	 **attackbox here**
    sprite('Action_000_07', 7)	# 33593-33599	 **attackbox here**
    sprite('Action_000_08', 7)	# 33600-33606	 **attackbox here**
    sprite('Action_000_09', 7)	# 33607-33613	 **attackbox here**
    sprite('Action_000_10', 7)	# 33614-33620	 **attackbox here**
    sprite('Action_000_11', 6)	# 33621-33626	 **attackbox here**
    sprite('Action_000_12', 5)	# 33627-33631	 **attackbox here**
    sprite('Action_000_13', 5)	# 33632-33636	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('Action_052_00', 2)	# 33637-33638
    sprite('Action_052_01', 6)	# 33639-33644
    sprite('Action_052_02', 5)	# 33645-33649
    sprite('Action_052_03', 3)	# 33650-33652
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 33653-33662	 **attackbox here**
    sprite('Action_052_05', 5)	# 33663-33667	 **attackbox here**
    sprite('Action_052_06', 4)	# 33668-33671	 **attackbox here**
    sprite('Action_052_07', 3)	# 33672-33674	 **attackbox here**
    sprite('Action_052_08', 10)	# 33675-33684	 **attackbox here**
    sprite('Action_052_09', 7)	# 33685-33691	 **attackbox here**
    sprite('Action_052_10', 5)	# 33692-33696	 **attackbox here**
    sprite('Action_052_11', 5)	# 33697-33701	 **attackbox here**
    SFX_1('ugo701uwa')
    sprite('Action_052_12', 5)	# 33702-33706	 **attackbox here**
    sprite('Action_052_13', 5)	# 33707-33711	 **attackbox here**
    label(153)
    sprite('Action_052_11', 5)	# 33712-33716	 **attackbox here**
    sprite('Action_052_12', 5)	# 33717-33721	 **attackbox here**
    sprite('Action_052_13', 5)	# 33722-33726	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(153)
    sprite('Action_052_11', 1)	# 33727-33727	 **attackbox here**
    Unknown21011(120)
    label(154)
    sprite('Action_052_11', 5)	# 33728-33732	 **attackbox here**
    sprite('Action_052_12', 5)	# 33733-33737	 **attackbox here**
    sprite('Action_052_13', 5)	# 33738-33742	 **attackbox here**
    loopRest()
    gotoLabel(154)
    label(160)
    sprite('Action_000_00', 1)	# 33743-33743	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 5)	# 33744-33748	 **attackbox here**
    sprite('Action_000_01', 5)	# 33749-33753	 **attackbox here**
    sprite('Action_000_02', 6)	# 33754-33759	 **attackbox here**
    sprite('Action_000_03', 7)	# 33760-33766	 **attackbox here**
    sprite('Action_000_04', 7)	# 33767-33773	 **attackbox here**
    sprite('Action_000_05', 7)	# 33774-33780	 **attackbox here**
    sprite('Action_000_06', 7)	# 33781-33787	 **attackbox here**
    sprite('Action_000_07', 7)	# 33788-33794	 **attackbox here**
    sprite('Action_000_08', 7)	# 33795-33801	 **attackbox here**
    sprite('Action_000_09', 7)	# 33802-33808	 **attackbox here**
    sprite('Action_000_10', 7)	# 33809-33815	 **attackbox here**
    sprite('Action_000_11', 6)	# 33816-33821	 **attackbox here**
    sprite('Action_000_12', 5)	# 33822-33826	 **attackbox here**
    sprite('Action_000_13', 5)	# 33827-33831	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Action_052_00', 2)	# 33832-33833
    sprite('Action_052_01', 6)	# 33834-33839
    sprite('Action_052_02', 5)	# 33840-33844
    sprite('Action_052_03', 3)	# 33845-33847
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 33848-33857	 **attackbox here**
    sprite('Action_052_05', 5)	# 33858-33862	 **attackbox here**
    sprite('Action_052_06', 4)	# 33863-33866	 **attackbox here**
    sprite('Action_052_07', 3)	# 33867-33869	 **attackbox here**
    sprite('Action_052_08', 10)	# 33870-33879	 **attackbox here**
    sprite('Action_052_09', 7)	# 33880-33886	 **attackbox here**
    sprite('Action_052_10', 5)	# 33887-33891	 **attackbox here**
    sprite('Action_052_11', 5)	# 33892-33896	 **attackbox here**
    SFX_1('ugo701rrb')
    sprite('Action_052_12', 5)	# 33897-33901	 **attackbox here**
    sprite('Action_052_13', 5)	# 33902-33906	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('Action_052_11', 5)	# 33907-33911	 **attackbox here**
    sprite('Action_052_12', 5)	# 33912-33916	 **attackbox here**
    sprite('Action_052_13', 5)	# 33917-33921	 **attackbox here**
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('Action_000_00', 1)	# 33922-33922	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_00', 5)	# 33923-33927	 **attackbox here**
    sprite('Action_000_01', 5)	# 33928-33932	 **attackbox here**
    sprite('Action_000_02', 6)	# 33933-33938	 **attackbox here**
    sprite('Action_000_03', 7)	# 33939-33945	 **attackbox here**
    sprite('Action_000_04', 7)	# 33946-33952	 **attackbox here**
    sprite('Action_000_05', 7)	# 33953-33959	 **attackbox here**
    sprite('Action_000_06', 7)	# 33960-33966	 **attackbox here**
    sprite('Action_000_07', 7)	# 33967-33973	 **attackbox here**
    sprite('Action_000_08', 7)	# 33974-33980	 **attackbox here**
    sprite('Action_000_09', 7)	# 33981-33987	 **attackbox here**
    sprite('Action_000_10', 7)	# 33988-33994	 **attackbox here**
    sprite('Action_000_11', 6)	# 33995-34000	 **attackbox here**
    sprite('Action_000_12', 5)	# 34001-34005	 **attackbox here**
    sprite('Action_000_13', 5)	# 34006-34010	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_052_00', 2)	# 34011-34012
    sprite('Action_052_01', 6)	# 34013-34018
    sprite('Action_052_02', 5)	# 34019-34023
    sprite('Action_052_03', 3)	# 34024-34026
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 34027-34036	 **attackbox here**
    sprite('Action_052_05', 5)	# 34037-34041	 **attackbox here**
    sprite('Action_052_06', 4)	# 34042-34045	 **attackbox here**
    sprite('Action_052_07', 3)	# 34046-34048	 **attackbox here**
    sprite('Action_052_08', 10)	# 34049-34058	 **attackbox here**
    sprite('Action_052_09', 7)	# 34059-34065	 **attackbox here**
    sprite('Action_052_10', 5)	# 34066-34070	 **attackbox here**
    sprite('Action_052_11', 5)	# 34071-34075	 **attackbox here**
    SFX_1('ugo701rbl')
    sprite('Action_052_12', 5)	# 34076-34080	 **attackbox here**
    sprite('Action_052_13', 5)	# 34081-34085	 **attackbox here**
    label(173)
    sprite('Action_052_11', 5)	# 34086-34090	 **attackbox here**
    sprite('Action_052_12', 5)	# 34091-34095	 **attackbox here**
    sprite('Action_052_13', 5)	# 34096-34100	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(173)
    sprite('Action_052_11', 1)	# 34101-34101	 **attackbox here**
    Unknown21011(120)
    label(174)
    sprite('Action_052_11', 5)	# 34102-34106	 **attackbox here**
    sprite('Action_052_12', 5)	# 34107-34111	 **attackbox here**
    sprite('Action_052_13', 5)	# 34112-34116	 **attackbox here**
    loopRest()
    gotoLabel(174)
    label(180)
    sprite('Action_052_00', 2)	# 34117-34118
    sprite('Action_052_01', 6)	# 34119-34124
    SFX_1('ugo700uca')
    sprite('Action_052_02', 5)	# 34125-34129
    sprite('Action_052_03', 3)	# 34130-34132
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 34133-34142	 **attackbox here**
    sprite('Action_052_05', 5)	# 34143-34147	 **attackbox here**
    sprite('Action_052_06', 4)	# 34148-34151	 **attackbox here**
    sprite('Action_052_07', 3)	# 34152-34154	 **attackbox here**
    sprite('Action_052_08', 10)	# 34155-34164	 **attackbox here**
    sprite('Action_052_09', 7)	# 34165-34171	 **attackbox here**
    sprite('Action_052_10', 5)	# 34172-34176	 **attackbox here**
    label(181)
    sprite('Action_052_11', 5)	# 34177-34181	 **attackbox here**
    sprite('Action_052_12', 5)	# 34182-34186	 **attackbox here**
    sprite('Action_052_13', 5)	# 34187-34191	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_052_11', 5)	# 34192-34196	 **attackbox here**
    sprite('Action_052_12', 5)	# 34197-34201	 **attackbox here**
    sprite('Action_052_13', 5)	# 34202-34206	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(182)
    sprite('Action_052_11', 5)	# 34207-34211	 **attackbox here**
    sprite('Action_052_12', 5)	# 34212-34216	 **attackbox here**
    sprite('Action_052_13', 5)	# 34217-34221	 **attackbox here**
    gotoLabel(182)
    label(190)
    sprite('Action_053_00', 5)	# 34222-34226
    sprite('Action_053_01', 7)	# 34227-34233
    SFX_1('ugo700uyu')
    sprite('Action_053_02', 7)	# 34234-34240
    sprite('Action_053_03', 7)	# 34241-34247
    sprite('Action_053_04', 8)	# 34248-34255
    sprite('Action_053_05', 7)	# 34256-34262
    sprite('Action_053_06', 5)	# 34263-34267
    sprite('Action_053_07', 5)	# 34268-34272
    label(191)
    sprite('Action_053_08', 1)	# 34273-34273	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_053_08', 10)	# 34274-34283	 **attackbox here**
    sprite('Action_053_08', 32767)	# 34284-67050	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(300)
    label(200)
    sprite('Action_000_00', 1)	# 67051-67051	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 5)	# 67052-67056	 **attackbox here**
    sprite('Action_000_01', 5)	# 67057-67061	 **attackbox here**
    sprite('Action_000_02', 6)	# 67062-67067	 **attackbox here**
    sprite('Action_000_03', 7)	# 67068-67074	 **attackbox here**
    sprite('Action_000_04', 7)	# 67075-67081	 **attackbox here**
    sprite('Action_000_05', 7)	# 67082-67088	 **attackbox here**
    sprite('Action_000_06', 7)	# 67089-67095	 **attackbox here**
    sprite('Action_000_07', 7)	# 67096-67102	 **attackbox here**
    sprite('Action_000_08', 7)	# 67103-67109	 **attackbox here**
    sprite('Action_000_09', 7)	# 67110-67116	 **attackbox here**
    sprite('Action_000_10', 7)	# 67117-67123	 **attackbox here**
    sprite('Action_000_11', 6)	# 67124-67129	 **attackbox here**
    sprite('Action_000_12', 5)	# 67130-67134	 **attackbox here**
    sprite('Action_000_13', 5)	# 67135-67139	 **attackbox here**
    gotoLabel(201)
    label(202)
    sprite('Action_052_00', 2)	# 67140-67141
    sprite('Action_052_01', 6)	# 67142-67147
    sprite('Action_052_02', 5)	# 67148-67152
    sprite('Action_052_03', 3)	# 67153-67155
    SFX_3('SE045')
    GFX_0('UGO_MatchWin_SummonIn', 100)
    sprite('Action_052_04', 10)	# 67156-67165	 **attackbox here**
    sprite('Action_052_05', 5)	# 67166-67170	 **attackbox here**
    sprite('Action_052_06', 4)	# 67171-67174	 **attackbox here**
    sprite('Action_052_07', 3)	# 67175-67177	 **attackbox here**
    sprite('Action_052_08', 10)	# 67178-67187	 **attackbox here**
    sprite('Action_052_09', 7)	# 67188-67194	 **attackbox here**
    sprite('Action_052_10', 5)	# 67195-67199	 **attackbox here**
    sprite('Action_052_11', 5)	# 67200-67204	 **attackbox here**
    SFX_1('ugo701bph')
    sprite('Action_052_12', 5)	# 67205-67209	 **attackbox here**
    sprite('Action_052_13', 5)	# 67210-67214	 **attackbox here**
    Unknown23018(1)
    label(203)
    sprite('Action_052_11', 5)	# 67215-67219	 **attackbox here**
    sprite('Action_052_12', 5)	# 67220-67224	 **attackbox here**
    sprite('Action_052_13', 5)	# 67225-67229	 **attackbox here**
    loopRest()
    gotoLabel(203)

@State
def CmnActLose():
    sprite('Action_248_00', 1)	# 1-1	 **attackbox here**
    if random_(2, 0, 50):
        SFX_1('ugo403_0')
    else:
        SFX_1('ugo403_1')
    label(0)
    sprite('Action_248_00', 4)	# 2-5	 **attackbox here**
    Unknown2038(1)
    sprite('Action_248_01', 5)	# 6-10	 **attackbox here**
    loopRest()
    (SLOT_2 <= 13)
    if SLOT_0:
        _gotolabel(0)
    sprite('Action_248_03', 3)	# 11-13
    Unknown23018(1)
    sprite('Action_248_04', 3)	# 14-16
    sprite('Action_248_05', 3)	# 17-19
    sprite('Action_248_06', 3)	# 20-22
    sprite('Action_248_07', 3)	# 23-25
    sprite('Action_248_08', 3)	# 26-28
    sprite('Action_248_09', 3)	# 29-31
    sprite('Action_248_09', 32767)	# 32-32798

@State
def EventDefEntryWait():
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_05', 7)	# 50-56
    sprite('hb000_04', 7)	# 57-63
    sprite('hb000_03', 7)	# 64-70
    sprite('hb000_02', 7)	# 71-77
    sprite('hb000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def EventDefEntryWaitCameraON():

    def upon_IMMEDIATE():
        Unknown20000(1)
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_05', 7)	# 50-56
    sprite('hb000_04', 7)	# 57-63
    sprite('hb000_03', 7)	# 64-70
    sprite('hb000_02', 7)	# 71-77
    sprite('hb000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def EventYoroke():
    sprite('hb070_03', 32767)	# 1-32767

@State
def EventYorokeDown():
    sprite('hb070_04', 4)	# 1-4
    sprite('hb070_05', 4)	# 5-8
    sprite('hb070_06', 4)	# 9-12
    sprite('hb070_07', 4)	# 13-16
    sprite('hb070_08', 4)	# 17-20
    sprite('hb070_09', 4)	# 21-24
    sprite('hb063_11', 32767)	# 25-32791

@State
def EventDefCrouch():
    label(0)
    sprite('hb010_02', 6)	# 1-6
    sprite('hb010_03', 6)	# 7-12
    sprite('hb010_04', 6)	# 13-18
    sprite('hb010_05', 6)	# 19-24
    sprite('hb010_06', 6)	# 25-30
    sprite('hb010_07', 6)	# 31-36
    sprite('hb010_08', 6)	# 37-42
    sprite('hb010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def EventNoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def EventWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('hb030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('hb030_01', 7)	# 8-14
    sprite('hb030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_03', 7)	# 22-28
    sprite('hb030_04', 7)	# 29-35
    sprite('hb030_05', 7)	# 36-42
    sprite('hb030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_07', 7)	# 50-56
    sprite('hb030_08', 7)	# 57-63
    sprite('hb030_09', 7)	# 64-70
    sprite('hb030_10', 10)	# 71-80
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def EventDefChouhatsu():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 6)	# 19-24
    sprite('hb300_04', 6)	# 25-30
    sprite('hb300_05', 6)	# 31-36
    sprite('hb300_03', 25)	# 37-61
    sprite('hb300_06', 6)	# 62-67
    sprite('hb300_07', 6)	# 68-73
    sprite('hb300_08', 30)	# 74-103
    sprite('hb300_07', 6)	# 104-109
    sprite('hb300_06', 6)	# 110-115
    sprite('hb300_05', 6)	# 116-121
    sprite('hb300_02', 6)	# 122-127
    sprite('hb300_01', 6)	# 128-133
    sprite('hb300_00', 6)	# 134-139
    enterState('CmnActStand')

@State
def EventDefChouhatsu2():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 32767)	# 19-32785

@State
def EventDefChouhatsu2End():
    sprite('hb300_02', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_00', 6)	# 13-18
    enterState('CmnActStand')

@State
def EventNOVSHB():
    sprite('hb000_00', 8)	# 1-8
    sprite('hb000_01', 8)	# 9-16
    sprite('hb000_02', 8)	# 17-24
    sprite('hb000_03', 8)	# 25-32
    sprite('hb000_04', 8)	# 33-40
    sprite('hb000_05', 8)	# 41-48
    sprite('hb000_06', 8)	# 49-56
    sprite('hb000_05', 8)	# 57-64
    sprite('hb000_04', 8)	# 65-72
    sprite('hb000_03', 8)	# 73-80
    sprite('hb000_02', 8)	# 81-88
    sprite('hb000_01', 8)	# 89-96
    sprite('hb300_00', 8)	# 97-104
    sprite('hb300_01', 8)	# 105-112
    sprite('hb300_02', 8)	# 113-120
    sprite('hb300_03', 8)	# 121-128
    sprite('hb300_03', 280)	# 129-408
    sprite('hb300_05', 8)	# 409-416
    sprite('hb300_02', 8)	# 417-424
    sprite('hb300_01', 8)	# 425-432
    sprite('hb300_00', 8)	# 433-440
    loopRest()
    enterState('CmnActStand')

@State
def EventPause1():
    sprite('hb333_00', 6)	# 1-6
    sprite('hb333_01', 6)	# 7-12
    sprite('hb333_02', 6)	# 13-18
    sprite('hb333_03', 6)	# 19-24
    sprite('hb333_04', 6)	# 25-30
    label(0)
    sprite('hb333_05', 8)	# 31-38
    sprite('hb333_06', 8)	# 39-46
    sprite('hb333_07', 8)	# 47-54
    loopRest()
    gotoLabel(0)

@State
def EventPause1End():
    sprite('hb333_08', 8)	# 1-8
    sprite('hb333_09', 8)	# 9-16
    loopRest()
    enterState('CmnActStand')

@State
def EventStandDLoop():
    sprite('hb203_00', 6)	# 1-6
    sprite('hb203_01', 6)	# 7-12
    label(0)
    sprite('hb203_02', 6)	# 13-18
    sprite('hb203_03', 6)	# 19-24
    sprite('hb203_04', 6)	# 25-30
    sprite('hb203_05', 8)	# 31-38
    loopRest()
    gotoLabel(0)

@State
def EventStandDLoopEnd():
    sprite('hb203_01', 6)	# 1-6
    sprite('hb203_00', 6)	# 7-12
    loopRest()
    enterState('CmnActStand')

@State
def EventMemoLoop():
    sprite('hb610_00', 6)	# 1-6
    sprite('hb610_01', 6)	# 7-12
    sprite('hb610_02', 6)	# 13-18
    sprite('hb610_03', 6)	# 19-24
    sprite('hb610_04', 6)	# 25-30
    sprite('hb610_05', 8)	# 31-38
    sprite('hb610_06', 8)	# 39-46
    sprite('hb610_07', 8)	# 47-54
    label(0)
    sprite('hb610_08', 8)	# 55-62
    sprite('hb610_09', 8)	# 63-70
    loopRest()
    gotoLabel(0)

@State
def EventMemoLoopEnd():
    sprite('hb610_07', 8)	# 1-8
    sprite('hb610_06', 6)	# 9-14
    sprite('hb610_05', 6)	# 15-20
    sprite('hb610_04', 6)	# 21-26
    sprite('hb610_03', 6)	# 27-32
    sprite('hb610_02', 6)	# 33-38
    sprite('hb610_01', 8)	# 39-46
    sprite('hb610_00', 8)	# 47-54
    loopRest()
    enterState('CmnActStand')

@State
def EventMemoLoopCameraON():

    def upon_IMMEDIATE():
        Unknown20000(1)
    sprite('hb610_00', 6)	# 1-6
    sprite('hb610_01', 6)	# 7-12
    sprite('hb610_02', 6)	# 13-18
    sprite('hb610_03', 6)	# 19-24
    sprite('hb610_04', 6)	# 25-30
    sprite('hb610_05', 8)	# 31-38
    sprite('hb610_06', 8)	# 39-46
    sprite('hb610_07', 8)	# 47-54
    label(0)
    sprite('hb610_08', 8)	# 55-62
    sprite('hb610_09', 8)	# 63-70
    loopRest()
    gotoLabel(0)

@State
def EventWin01Wait():
    sprite('hb615_08', 32767)	# 1-32767
    loopRest()

@State
def EventWin01WaitToStand():
    sprite('hb615_08', 6)	# 1-6
    sprite('hb615_07', 6)	# 7-12
    sprite('hb615_06', 6)	# 13-18
    sprite('hb615_05', 6)	# 19-24
    sprite('hb615_04', 6)	# 25-30
    sprite('hb615_03', 6)	# 31-36
    sprite('hb615_02', 6)	# 37-42
    sprite('hb615_01', 6)	# 43-48
    sprite('hb615_00', 6)	# 49-54
    loopRest()
    enterState('CmnActStand')

@State
def EventWin02ToStand():
    sprite('hb603_06', 6)	# 1-6
    sprite('hb603_05', 6)	# 7-12
    sprite('hb603_04', 6)	# 13-18
    sprite('hb603_03', 6)	# 19-24
    sprite('hb603_02', 6)	# 25-30
    sprite('hb603_01', 8)	# 31-38
    sprite('hb603_00', 32767)	# 39-32805
    loopRest()

@State
def EventEntry01ToStand():
    sprite('null', 20)	# 1-20
    teleportRelativeX(-105000)
    Unknown3026(-13421773)
    sprite('hb600_00', 32767)	# 21-32787
    physicsYImpulse(-30000)
    setGravity(1800)
    Unknown3038(0)
    sendToLabelUpon(2, 1)
    GFX_0('hbef_600_feather', 100)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3072('7f000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    SFX_0('000_airdash_1')
    label(1)
    sprite('hb600_01', 6)	# 32788-32793
    Unknown26('hbef_600_feather')
    GFX_0('hbef_600_feather2', 100)
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    Unknown3025(-1, 16)
    sprite('hb600_02', 2)	# 32794-32795
    Unknown3029(0)
    sprite('hb600_02', 2)	# 32796-32797
    sprite('hb600_03', 6)	# 32798-32803
    SFX_0('019_cloth_b')
    sprite('hb600_04', 6)	# 32804-32809
    sprite('hb600_05', 6)	# 32810-32815
    sprite('hb600_06', 6)	# 32816-32821
    sprite('hb600_07', 6)	# 32822-32827
    sprite('hb600_08', 6)	# 32828-32833
    sprite('hb600_09', 6)	# 32834-32839
    sprite('hb600_10', 7)	# 32840-32846
    sprite('hb600_11', 7)	# 32847-32853
    sprite('hb600_12', 7)	# 32854-32860
    sprite('hb600_13', 20)	# 32861-32880
    sprite('hb600_14', 6)	# 32881-32886
    teleportRelativeX(10000)
    sprite('hb600_15', 6)	# 32887-32892
    teleportRelativeX(5000)
    sprite('hb600_16', 6)	# 32893-32898
    teleportRelativeX(45000)
    sprite('hb600_17', 6)	# 32899-32904
    teleportRelativeX(25000)
    sprite('hb000_00', 1)	# 32905-32905
    Unknown21011(100)
    teleportRelativeX(20000)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Event2DLoop():
    sprite('hb234_00', 3)	# 1-3
    sprite('hb234_01', 4)	# 4-7
    SFX_0('019_cloth_a')
    Unknown1084(1)
    physicsYImpulse(15000)
    sprite('hb234_02', 5)	# 8-12
    setGravity(3600)
    sprite('hb234_03', 4)	# 13-16
    sprite('hb234_04', 32767)	# 17-32783
    sendToLabelUpon(2, 0)
    label(0)
    sprite('hb234_05', 3)	# 32784-32786
    clearUponHandler(2)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    GFX_0('hbef_Drive', 103)
    GFX_0('hbef_2D_feather', 103)
    label(10)
    sprite('hb234_06', 6)	# 32787-32792
    sprite('hb234_07', 6)	# 32793-32798
    sprite('hb234_08', 6)	# 32799-32804
    sprite('hb234_09', 6)	# 32805-32810
    loopRest()
    gotoLabel(10)

@State
def Event2DLoopEnd():
    sprite('hb234_10', 4)	# 1-4
    sprite('hb234_11', 4)	# 5-8
    sprite('hb234_12', 4)	# 9-12
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_NoDisp():
    sprite('null', 32767)	# 1-32767
    Unknown3038(1)

@State
def Act2EventWalkFrameIn():
    Unknown2034(0)
    Unknown2037(1)
    Unknown1000(-900000)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 260000):
                Unknown2037(0)
                sendToLabel(1)
        elif (SLOT_22 > (-260000)):
            sendToLabel(1)
    sprite('hb030_00', 7)	# 1-7
    physicsXImpulse(4650)
    label(0)
    sprite('hb030_01', 7)	# 8-14
    sprite('hb030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_03', 7)	# 22-28
    sprite('hb030_04', 7)	# 29-35
    sprite('hb030_05', 7)	# 36-42
    sprite('hb030_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hb030_07', 7)	# 50-56
    sprite('hb030_08', 7)	# 57-63
    sprite('hb030_09', 7)	# 64-70
    sprite('hb030_10', 10)	# 71-80
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown1000(-260000)
    enterState('CmnActStand')

@State
def Act2Event_EntryA():

    def upon_IMMEDIATE():
        sendToLabelUpon(2, 0)
        Unknown3038(1)
        setGravity(0)
        teleportRelativeX(-105000)
    sprite('null', 2)	# 1-2
    teleportRelativeY(600000)
    sprite('null', 20)	# 3-22
    Unknown3026(-13421773)
    sprite('hb600_00', 32767)	# 23-32789
    physicsYImpulse(-30000)
    setGravity(1800)
    Unknown3038(0)
    GFX_0('hbef_600_feather', 100)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3072('7f000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    SFX_0('000_airdash_1')
    label(0)
    sprite('hb600_01', 6)	# 32790-32795
    Unknown26('hbef_600_feather')
    GFX_0('hbef_600_feather2', 100)
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    Unknown3025(-1, 16)
    sprite('hb600_02', 2)	# 32796-32797
    Unknown3029(0)
    sprite('hb600_02', 2)	# 32798-32799
    sprite('hb600_03', 6)	# 32800-32805
    SFX_0('019_cloth_b')
    sprite('hb600_04', 6)	# 32806-32811
    sprite('hb600_05', 6)	# 32812-32817
    sprite('hb600_06', 6)	# 32818-32823
    sprite('hb600_07', 6)	# 32824-32829
    sprite('hb600_08', 6)	# 32830-32835
    sprite('hb600_09', 6)	# 32836-32841
    sprite('hb600_10', 7)	# 32842-32848
    sprite('hb600_11', 7)	# 32849-32855
    sprite('hb600_12', 7)	# 32856-32862
    sprite('hb600_13', 20)	# 32863-32882
    sprite('hb600_14', 6)	# 32883-32888
    teleportRelativeX(10000)
    sprite('hb600_15', 6)	# 32889-32894
    teleportRelativeX(5000)
    sprite('hb600_16', 6)	# 32895-32900
    teleportRelativeX(45000)
    sprite('hb600_17', 6)	# 32901-32906
    teleportRelativeX(25000)
    sprite('hb000_00', 1)	# 32907-32907
    teleportRelativeX(20000)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_EntryB1():
    sprite('hb603_00', 32767)	# 1-32767
    loopRest()

@State
def Act2Event_EntryB2():
    sprite('hb603_00', 7)	# 1-7
    sprite('hb603_01', 7)	# 8-14
    sprite('hb603_02', 7)	# 15-21
    sprite('hb603_03', 10)	# 22-31
    sprite('hb603_04', 7)	# 32-38
    sprite('hb603_05', 6)	# 39-44
    sprite('hb603_06', 6)	# 45-50
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Reaction():
    sprite('hb001_00', 7)	# 1-7
    sprite('hb001_01', 7)	# 8-14
    sprite('hb001_02', 7)	# 15-21
    sprite('hb001_03', 8)	# 22-29
    sprite('hb001_04', 8)	# 30-37
    sprite('hb001_05', 8)	# 38-45
    sprite('hb001_06', 7)	# 46-52
    sprite('hb001_05', 5)	# 53-57
    sprite('hb001_04', 5)	# 58-62
    sprite('hb001_03', 5)	# 63-67
    sprite('hb001_02', 10)	# 68-77
    sprite('hb001_03', 8)	# 78-85
    sprite('hb001_04', 8)	# 86-93
    sprite('hb001_05', 8)	# 94-101
    sprite('hb001_06', 7)	# 102-108
    sprite('hb001_05', 5)	# 109-113
    sprite('hb001_04', 5)	# 114-118
    sprite('hb001_03', 5)	# 119-123
    sprite('hb001_01', 7)	# 124-130
    sprite('hb001_00', 7)	# 131-137
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Win1():
    sprite('hb611_00', 7)	# 1-7
    sprite('hb611_01', 7)	# 8-14
    label(0)
    sprite('hb611_02', 6)	# 15-20
    sprite('hb611_03', 6)	# 21-26
    sprite('hb611_04', 6)	# 27-32
    loopRest()
    gotoLabel(0)

@State
def Act2Event_Win2():
    sprite('keep', 1)	# 1-1
    sprite('hb611_05', 7)	# 2-8
    sprite('hb611_06', 7)	# 9-15
    sprite('hb611_07', 6)	# 16-21
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb611_08', 6)	# 22-27
    sprite('hb611_09', 6)	# 28-33
    sprite('hb611_07', 6)	# 34-39
    Unknown3038(1)
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('hbef_611_shadow_Event', 100)
    sprite('hb611_08', 6)	# 40-45
    Unknown3004(-10)
    sprite('hb611_09', 6)	# 46-51
    sprite('hb611_07', 6)	# 52-57
    Unknown21011(30)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb611_08', 6)	# 58-63
    sprite('hb611_09', 6)	# 64-69
    Unknown3038(1)
    sprite('hb611_07', 6)	# 70-75
    sprite('hb611_08', 6)	# 76-81
    sprite('hb611_09', 6)	# 82-87
    label(9)
    sprite('hb611_07', 6)	# 88-93
    sprite('hb611_08', 6)	# 94-99
    sprite('hb611_09', 6)	# 100-105
    loopRest()
    gotoLabel(9)

@State
def Act2Event_Chouhatsu():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 32767)	# 19-32785
    loopRest()

@State
def Act2Event_ChouhatsuEnd():
    sprite('keep', 2)	# 1-2
    sprite('hb300_02', 6)	# 3-8
    sprite('hb300_01', 6)	# 9-14
    sprite('hb300_00', 6)	# 15-20
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_Down():
    sprite('hb060_14', 32767)	# 1-32767
    loopRest()

@State
def Act2EventYorokeDown():
    sprite('hb070_04', 4)	# 1-4
    sprite('hb070_05', 4)	# 5-8
    sprite('hb070_06', 4)	# 9-12
    sprite('hb070_07', 4)	# 13-16
    sprite('hb070_08', 4)	# 17-20
    sprite('hb070_09', 4)	# 21-24
    GFX_1('ef_grndshock', 104)
    SFX_0('209_down_normal_0')
    sprite('hb063_11', 32767)	# 25-32791

@State
def Act2Event_DownEnd():
    sprite('keep', 2)	# 1-2
    sprite('hb061_00', 4)	# 3-6
    sprite('hb061_01', 4)	# 7-10
    sprite('hb061_02', 4)	# 11-14
    sprite('hb061_03', 4)	# 15-18
    sprite('hb061_04', 4)	# 19-22
    sprite('hb061_05', 4)	# 23-26
    sprite('hb061_06', 3)	# 27-29
    sprite('hb061_07', 3)	# 30-32
    sprite('hb061_08', 3)	# 33-35
    sprite('hb061_09', 3)	# 36-38
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvstb_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
    sprite('hb003_00', 3)	# 1-3
    sprite('hb003_01', 3)	# 4-6
    sprite('hb003_00ex01', 3)	# 7-9
    Unknown2005()
    sprite('hb032_00', 2)	# 10-11
    physicsXImpulse(24000)
    sprite('hb032_01', 2)	# 12-13
    sprite('hb032_02', 4)	# 14-17
    sprite('hb032_03', 4)	# 18-21
    Unknown8006(100, 1, 1)
    sprite('hb032_04', 4)	# 22-25
    sprite('hb032_05', 4)	# 26-29
    sprite('hb032_06', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('hb032_07', 4)	# 34-37
    sprite('hb032_08', 4)	# 38-41
    sprite('hb032_02', 4)	# 42-45
    sprite('hb032_03', 4)	# 46-49
    Unknown8006(100, 1, 1)
    sprite('hb032_04', 4)	# 50-53
    sprite('hb032_05', 4)	# 54-57
    sprite('hb032_06', 4)	# 58-61
    Unknown8006(100, 1, 1)
    sprite('hb032_07', 4)	# 62-65
    sprite('hb032_08', 4)	# 66-69
    sprite('null', 32767)	# 70-32836
    Unknown1084(1)
    loopRest()

@State
def Act2Event_hbvsaz_00():

    def upon_IMMEDIATE():
        Unknown1000(-900000)
        Unknown2034(0)
        sendToLabelUpon(2, 1)

    def upon_3():
        if SLOT_38:
            if (SLOT_22 < 160000):
                sendToLabel(0)
                clearUponHandler(3)
        elif (SLOT_22 > (-160000)):
            sendToLabel(0)
            clearUponHandler(3)
    sprite('hb032_00', 2)	# 1-2
    physicsXImpulse(24000)
    sprite('hb032_01', 2)	# 3-4
    label(9)
    sprite('hb032_02', 4)	# 5-8
    sprite('hb032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    sprite('hb032_04', 4)	# 13-16
    sprite('hb032_05', 4)	# 17-20
    sprite('hb032_06', 4)	# 21-24
    Unknown8006(100, 1, 1)
    sprite('hb032_07', 4)	# 25-28
    sprite('hb032_08', 4)	# 29-32
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('hb032_09', 3)	# 33-35
    physicsXImpulse(0)
    Unknown1045(5000)
    sprite('hb032_10', 3)	# 36-38
    sprite('hb032_11', 3)	# 39-41
    sprite('hb032_12', 3)	# 42-44
    sprite('hb033_00', 2)	# 45-46
    Unknown1084(1)
    sprite('hb033_01', 2)	# 47-48
    physicsXImpulse(-24000)
    physicsYImpulse(6800)
    setGravity(2000)
    Unknown8002()
    sprite('hb033_02', 2)	# 49-50
    sprite('hb033_03', 2)	# 51-52
    sprite('hb033_04', 32767)	# 53-32819
    label(1)
    sprite('hb033_05', 2)	# 32820-32821
    Unknown1084(1)
    Unknown1000(-260000)
    Unknown8000(100, 1, 1)
    sprite('hb033_06', 3)	# 32822-32824
    sprite('hb033_07', 3)	# 32825-32827
    sprite('hb033_08', 3)	# 32828-32830
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvsaz_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('hb090_00', 15)	# 1-15
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('hb090_01', 6)	# 16-21
    sprite('hb090_02', 6)	# 22-27
    sprite('hb090_03', 6)	# 28-33
    sprite('hb090_04', 6)	# 34-39
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_hbvsaz_02():
    sprite('hb070_13', 5)	# 1-5
    GFX_0('Act2Event_Yure', -1)
    sprite('hb070_12', 5)	# 6-10
    sprite('hb070_11', 5)	# 11-15
    sprite('hb070_10', 32767)	# 16-32782
    loopRest()

@State
def Act2Event_hzvshb_00():

    def upon_IMMEDIATE():
        Unknown2034(0)
    sprite('hb032_00', 2)	# 1-2
    physicsXImpulse(18000)
    sprite('hb032_01', 2)	# 3-4
    sprite('hb032_02', 4)	# 5-8
    sprite('hb032_03', 4)	# 9-12
    Unknown8006(100, 1, 1)
    physicsXImpulse(0)
    Unknown1047(10000)
    sprite('hb032_09', 5)	# 13-17
    sprite('hb032_10', 5)	# 18-22
    sprite('hb032_11', 5)	# 23-27
    sprite('hb032_12', 7)	# 28-34
    Unknown1084(1)
    sprite('hb000_00', 7)	# 35-41
    sprite('hb000_01', 7)	# 42-48
    sprite('hb000_02', 7)	# 49-55
    sprite('hb000_03', 7)	# 56-62
    sprite('hb000_04', 7)	# 63-69
    sprite('hb000_05', 7)	# 70-76
    sprite('hb000_06', 7)	# 77-83
    sprite('hb000_07', 7)	# 84-90
    sprite('hb000_08', 7)	# 91-97
    sprite('hb611_00', 6)	# 98-103
    sprite('hb611_01', 6)	# 104-109
    label(0)
    sprite('hb611_02', 6)	# 110-115
    sprite('hb611_03', 6)	# 116-121
    sprite('hb611_04', 6)	# 122-127
    loopRest()
    gotoLabel(0)

@State
def Act2Event_muvshb_00():

    def upon_IMMEDIATE():
        teleportRelativeY(700000)
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
    sprite('null', 1)	# 1-1
    SFX_3('hbse_02')
    SFX_0('007_swing_knife_0')
    teleportRelativeX(-105000)
    GFX_0('Kunai_Event', -1)
    Unknown21007(1, 32)
    sprite('null', 1)	# 2-2
    GFX_0('Kunai_Event', -1)
    Unknown21007(1, 33)
    sprite('null', 1)	# 3-3
    GFX_0('Kunai_Event', -1)
    Unknown21007(1, 34)
    sprite('null', 60)	# 4-63
    sprite('hb600_00', 32767)	# 64-32830
    Unknown3026(-13421773)
    physicsYImpulse(-30000)
    Unknown1043()
    Unknown3038(0)
    GFX_0('hbef_600_feather', 100)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3070(2)
    Unknown3071(3)
    Unknown3072('7f000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    SFX_0('000_airdash_1')
    label(0)
    sprite('hb600_01', 6)	# 32831-32836
    Unknown26('hbef_600_feather')
    GFX_0('hbef_600_feather2', 100)
    SFX_0('208_brake_normal')
    SFX_0('204_runjump_normal_1')
    Unknown3025(-1, 16)
    sprite('hb600_02', 2)	# 32837-32838
    Unknown3029(0)
    sprite('hb600_02', 2)	# 32839-32840
    sprite('hb600_03', 6)	# 32841-32846
    SFX_0('019_cloth_b')
    sprite('hb600_04', 6)	# 32847-32852
    sprite('hb600_05', 6)	# 32853-32858
    sprite('hb600_06', 6)	# 32859-32864
    sprite('hb600_07', 6)	# 32865-32870
    sprite('hb600_08', 6)	# 32871-32876
    sprite('hb600_09', 6)	# 32877-32882
    sprite('hb600_10', 7)	# 32883-32889
    sprite('hb600_11', 7)	# 32890-32896
    sprite('hb600_12', 7)	# 32897-32903
    sprite('hb600_13', 20)	# 32904-32923
    sprite('hb600_14', 6)	# 32924-32929
    teleportRelativeX(10000)
    sprite('hb600_15', 6)	# 32930-32935
    teleportRelativeX(5000)
    sprite('hb600_16', 6)	# 32936-32941
    teleportRelativeX(45000)
    sprite('hb600_17', 6)	# 32942-32947
    teleportRelativeX(25000)
    sprite('hb000_00', 1)	# 32948-32948
    teleportRelativeX(20000)
    Unknown1000(-260000)
    loopRest()
    enterState('CmnActStand')

@State
def Act2Event_muvshb_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('hb070_00', 15)	# 1-15
    Unknown4052()
    Unknown4045('65665f6869746d7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_1')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('hb070_01', 3)	# 16-18
    sprite('hb070_02', 4)	# 19-22
    sprite('hb070_03', 32767)	# 23-32789
    loopRest()

@State
def Act2Event_muvshb_02():
    sprite('hb070_04', 5)	# 1-5
    sprite('hb070_05', 5)	# 6-10
    sprite('hb070_06', 5)	# 11-15
    sprite('hb070_07', 5)	# 16-20
    sprite('hb070_08', 5)	# 21-25
    sprite('hb070_09', 5)	# 26-30
    sprite('hb063_11', 32767)	# 31-32797
    SFX_0('209_down_normal_0')
    loopRest()

@State
def Act2Event_hbvsmi_00():
    sprite('keep', 32767)	# 1-32767
    GFX_0('Act2Event_Fade', -1)
    SFX_0('022_magiccircle_c')
    Unknown3004(-4)
    Unknown36(22)
    Unknown3004(-4)
    Unknown35()
    loopRest()

@State
def Act3Event_muvshb_00():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('hb202_00', 3)	# 1-3
    sprite('hb202_01', 4)	# 4-7
    sprite('hb202_02', 2)	# 8-9
    sprite('hb202_03', 3)	# 10-12
    GFX_0('hbef_202_slash', 100)
    SFX_0('009_swing_rapier_1')
    sprite('hb202_04', 5)	# 13-17
    sprite('hb202_05', 5)	# 18-22
    sprite('hb202_06', 5)	# 23-27
    sprite('hb202_07', 5)	# 28-32
    sprite('hb202_08', 4)	# 33-36
    sprite('hb202_09', 4)	# 37-40
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_muvshb_01():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb070_00', 19)	# 8-26
    Unknown4052()
    Unknown4045('65665f6869746c7a00000000000000000000000000000000000000000000000067000000')
    SFX_0('101_hit_slash_2')
    ScreenShake(1000, 20000)
    sprite('hb070_00', 4)	# 27-30
    Unknown1047(-11000)
    sprite('hb070_01', 4)	# 31-34
    sprite('hb070_02', 4)	# 35-38
    sprite('hb070_03', 32767)	# 39-32805
    loopRest()

@State
def Act3Event_muvshb_02():
    sprite('hb070_04', 5)	# 1-5
    sprite('hb070_05', 5)	# 6-10
    sprite('hb070_06', 5)	# 11-15
    sprite('hb070_07', 5)	# 16-20
    sprite('hb070_08', 5)	# 21-25
    sprite('hb070_09', 5)	# 26-30
    sprite('hb063_11', 32767)	# 31-32797
    Unknown8000(100, 1, 1)
    SFX_0('209_down_normal_0')

@State
def Act3Event_muvshb_03():
    sprite('hb064_00', 3)	# 1-3
    sprite('hb064_01', 3)	# 4-6
    sprite('hb064_02', 3)	# 7-9
    sprite('hb064_03', 3)	# 10-12
    sprite('hb064_04', 3)	# 13-15
    sprite('hb064_05', 3)	# 16-18
    sprite('hb064_06', 3)	# 19-21
    sprite('hb064_07', 3)	# 22-24
    sprite('hb064_08', 3)	# 25-27
    sprite('hb064_09', 3)	# 28-30
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_00():
    sprite('hb001_00', 7)	# 1-7
    sprite('hb001_01', 7)	# 8-14
    sprite('hb001_02', 7)	# 15-21
    label(0)
    sprite('hb001_03', 8)	# 22-29
    sprite('hb001_04', 8)	# 30-37
    sprite('hb001_05', 8)	# 38-45
    sprite('hb001_06', 7)	# 46-52
    sprite('hb001_05', 5)	# 53-57
    sprite('hb001_04', 5)	# 58-62
    sprite('hb001_03', 5)	# 63-67
    sprite('hb001_02', 20)	# 68-87
    loopRest()
    gotoLabel(0)

@State
def Act3Event_hbvstb_01():
    sprite('hb001_01', 7)	# 1-7
    sprite('hb001_00', 7)	# 8-14
    loopRest()
    enterState('CmnActStand')
endState()

@State
def Act3Event_hbvstb_02():
    sprite('hb615_00', 4)	# 1-4
    sprite('hb615_01', 4)	# 5-8
    sprite('hb615_02', 7)	# 9-15
    SFX_3('hbse_07')
    sprite('hb615_03', 7)	# 16-22
    GFX_0('hbef_615_hibana', 0)
    sprite('hb615_04', 7)	# 23-29
    sprite('hb615_05', 7)	# 30-36
    sprite('hb615_06', 7)	# 37-43
    sprite('hb615_07', 7)	# 44-50
    sprite('hb615_08', 32767)	# 51-32817

@State
def Act3Event_hbvstb_03():

    def upon_IMMEDIATE():

        def upon_STATE_END():
            teleportRelativeX(120000)
    sprite('hb211_19', 4)	# 1-4
    teleportRelativeX(-120000)
    SFX_0('011_spin_1')
    sprite('hb211_20', 4)	# 5-8
    sprite('hb211_21', 4)	# 9-12
    sprite('hb211_22', 4)	# 13-16
    sprite('hb211_23', 5)	# 17-21
    sprite('hb211_24', 5)	# 22-26
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_04():

    def upon_IMMEDIATE():
        Unknown2003(1)
    sprite('hb202_00', 2)	# 1-2
    sprite('hb202_01', 3)	# 3-5
    sprite('hb202_02', 2)	# 6-7
    sprite('hb202_03', 16)	# 8-23
    GFX_0('hbef_202_slash', 100)
    SFX_0('009_swing_rapier_1')
    sprite('hb202_04', 5)	# 24-28
    sprite('hb202_05', 5)	# 29-33
    sprite('hb202_06', 5)	# 34-38
    sprite('hb202_07', 5)	# 39-43
    sprite('hb202_08', 4)	# 44-47
    sprite('hb202_09', 4)	# 48-51
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_05():
    sprite('keep', 2)	# 1-2
    sprite('hb611_01', 7)	# 3-9
    sprite('hb611_00', 7)	# 10-16
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvstb_06():
    sprite('hb611_00', 7)	# 1-7
    sprite('hb611_01', 7)	# 8-14
    sprite('hb611_05', 7)	# 15-21
    sprite('hb611_06', 7)	# 22-28
    sprite('hb611_07', 6)	# 29-34
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb611_08', 6)	# 35-40
    sprite('hb611_09', 6)	# 41-46
    sprite('hb611_07', 6)	# 47-52
    Unknown3038(1)
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('hbef_611_shadow_Event', 100)
    sprite('hb611_08', 6)	# 53-58
    Unknown3004(-10)
    sprite('hb611_09', 6)	# 59-64
    sprite('hb611_07', 6)	# 65-70
    Unknown21011(30)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb611_08', 6)	# 71-76
    sprite('hb611_09', 6)	# 77-82
    Unknown3038(1)
    sprite('hb611_07', 6)	# 83-88
    sprite('hb611_08', 6)	# 89-94
    sprite('hb611_09', 6)	# 95-100
    label(9)
    sprite('hb611_07', 6)	# 101-106
    sprite('hb611_08', 6)	# 107-112
    sprite('hb611_09', 6)	# 113-118
    loopRest()
    gotoLabel(9)

@State
def Act3Event_hbvsno_00():
    sprite('hb203_00', 5)	# 1-5
    sprite('hb203_01', 5)	# 6-10
    sprite('hb203_02', 5)	# 11-15
    label(0)
    sprite('hb203_03', 5)	# 16-20
    sprite('hb203_04', 5)	# 21-25
    sprite('hb203_05', 5)	# 26-30
    loopRest()
    gotoLabel(0)

@State
def Act3Event_hbvsno_01():
    sprite('hb203_01', 5)	# 1-5
    sprite('hb203_00', 5)	# 6-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_hbvshz_00():
    sprite('hb333_00', 5)	# 1-5
    sprite('hb333_01', 5)	# 6-10
    sprite('hb333_02', 5)	# 11-15
    sprite('hb333_03', 32767)	# 16-32782

@State
def Act3Event_hbvshz_01():
    sprite('keep', 2)	# 1-2
    sprite('hb333_04', 3)	# 3-5
    Unknown4049(1500)
    Unknown4004('4775617264437275736857696e64000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    Unknown1096(1200)
    Unknown35()
    SFX_0('302_spsys_drivemotion')
    SFX_0('302_spsys_burst')
    ScreenShake(3000, 60000)
    Unknown2037(3)
    label(0)
    sprite('hb333_05', 5)	# 6-10
    Unknown2038(-1)
    sprite('hb333_06', 5)	# 11-15
    sprite('hb333_07', 5)	# 16-20
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('hb333_08', 5)	# 21-25
    sprite('hb333_09', 5)	# 26-30
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_5DLoop():
    sprite('hb203_00', 5)	# 1-5
    sprite('hb203_01', 5)	# 6-10
    sprite('hb203_02', 5)	# 11-15
    label(0)
    sprite('hb203_03', 5)	# 16-20
    sprite('hb203_04', 5)	# 21-25
    sprite('hb203_05', 5)	# 26-30
    loopRest()
    gotoLabel(0)

@State
def Act3Event_5DLoopEnd():
    sprite('hb203_01', 5)	# 1-5
    sprite('hb203_00', 5)	# 6-10
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_kgvshb_00():

    def upon_IMMEDIATE():
        Unknown1000(-160000)
        sendToLabelUpon(32, 1)
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_07', 7)	# 50-56
    sprite('hb000_08', 7)	# 57-63
    sprite('hb000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb052_03', 17)	# 71-87
    Unknown4049(1500)
    Unknown4045('65665f6869746d6400000000000000000000000000000000000000000000000067000000')
    SFX_0('100_hit_grap_3')
    ScreenShake(1000, 20000)
    sprite('hb052_03', 32767)	# 88-32854
    Unknown1047(-11000)
    loopRest()

@State
def Act3Event_kgvshb_01():
    sprite('hb052_03', 6)	# 1-6
    sprite('hb052_02', 6)	# 7-12
    sprite('hb052_01', 6)	# 13-18
    sprite('hb052_00', 6)	# 19-24
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_DownWait():
    sprite('hb060_14', 32767)	# 1-32767

@State
def Act3Event_DownToStand():
    sprite('hb061_00', 4)	# 1-4
    sprite('hb061_01', 4)	# 5-8
    sprite('hb061_02', 4)	# 9-12
    sprite('hb061_03', 4)	# 13-16
    sprite('hb061_04', 4)	# 17-20
    sprite('hb061_05', 4)	# 21-24
    sprite('hb061_06', 3)	# 25-27
    sprite('hb061_07', 3)	# 28-30
    sprite('hb061_08', 3)	# 31-33
    sprite('hb061_09', 3)	# 34-36
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_Smile():
    sprite('hb300_00', 6)	# 1-6
    sprite('hb300_01', 6)	# 7-12
    sprite('hb300_02', 6)	# 13-18
    sprite('hb300_03', 6)	# 19-24
    sprite('hb300_04', 6)	# 25-30
    sprite('hb300_05', 6)	# 31-36
    sprite('hb300_06', 6)	# 37-42
    sprite('hb300_07', 6)	# 43-48
    sprite('hb300_08', 32767)	# 49-32815
    loopRest()

@State
def Act3Event_blvshb_00():
    sprite('keep', 2)	# 1-2
    teleportRelativeX(90000)
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_blvshb_01():
    sprite('keep', 2)	# 1-2
    sendToLabelUpon(32, 1)
    sprite('hb300_02', 6)	# 3-8
    sprite('hb300_01', 6)	# 9-14
    sprite('hb300_00', 6)	# 15-20
    loopRest()
    label(0)
    sprite('hb000_00', 7)	# 21-27
    sprite('hb000_01', 7)	# 28-34
    sprite('hb000_02', 7)	# 35-41
    sprite('hb000_03', 7)	# 42-48
    sprite('hb000_04', 7)	# 49-55
    sprite('hb000_05', 7)	# 56-62
    sprite('hb000_06', 7)	# 63-69
    sprite('hb000_07', 7)	# 70-76
    sprite('hb000_08', 7)	# 77-83
    sprite('hb000_09', 7)	# 84-90
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb033_00', 2)	# 91-92
    sprite('hb033_01', 2)	# 93-94
    physicsXImpulse(-12000)
    physicsYImpulse(4800)
    setGravity(2000)
    Unknown8002()
    sendToLabelUpon(2, 2)
    sprite('hb033_02', 2)	# 95-96
    setInvincible(0)
    sprite('hb033_03', 2)	# 97-98
    sprite('hb033_04', 32767)	# 99-32865
    label(2)
    sprite('hb033_05', 2)	# 32866-32867
    clearUponHandler(2)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('hb033_06', 3)	# 32868-32870
    sprite('hb033_07', 3)	# 32871-32873
    sprite('hb033_08', 2)	# 32874-32875
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsHB00():

    def upon_IMMEDIATE():
        Unknown3001(0)
        Unknown1000(-50000)
    sprite('hb603_00', 6)	# 1-6
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb603_00', 6)	# 7-12
    sprite('hb603_00', 6)	# 13-18
    sprite('hb603_00', 6)	# 19-24
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('Act3Event_BNvsHB00shadow', 100)
    sprite('hb603_00', 6)	# 25-30
    Unknown3004(10)
    sprite('hb603_00', 6)	# 31-36
    sprite('hb603_00', 6)	# 37-42
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb603_00', 6)	# 43-48
    Unknown13044(0)
    Unknown3026(0)
    Unknown3025(-1, 10)
    GFX_0('hbef_D_feather', 100)
    sprite('hb603_00', 32767)	# 49-32815
    loopRest()

@State
def Act3Event_BNvsHB01():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 0)
    sprite('hb603_00', 32767)	# 1-32767
    loopRest()
    label(0)
    sprite('hb603_00', 6)	# 32768-32773
    SFX_3('hbse_08')
    Unknown3004(-10)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb603_00', 6)	# 32774-32779
    sprite('hb603_00', 6)	# 32780-32785
    sprite('hb603_00', 6)	# 32786-32791
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb603_00', 6)	# 32792-32797
    sprite('hb603_00', 6)	# 32798-32803
    sprite('hb603_00', 6)	# 32804-32809
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb603_00', 6)	# 32810-32815
    Unknown13044(0)
    sprite('null', 32767)	# 32816-65582
    Unknown3038(1)
    Unknown1000(-260000)
    loopRest()

@State
def Act3Event_2DLoopEnd():
    sprite('hb234_10', 6)	# 1-6
    sprite('hb234_11', 6)	# 7-12
    sprite('hb234_12', 6)	# 13-18
    sprite('hb010_01', 4)	# 19-22
    sprite('hb010_00', 4)	# 23-26
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsHB02():

    def upon_IMMEDIATE():
        sendToLabelUpon(32, 1)
        Unknown1000(-160000)
    label(0)
    sprite('hb000_00', 7)	# 1-7
    sprite('hb000_01', 7)	# 8-14
    sprite('hb000_02', 7)	# 15-21
    sprite('hb000_03', 7)	# 22-28
    sprite('hb000_04', 7)	# 29-35
    sprite('hb000_05', 7)	# 36-42
    sprite('hb000_06', 7)	# 43-49
    sprite('hb000_05', 7)	# 50-56
    sprite('hb000_04', 7)	# 57-63
    sprite('hb000_03', 7)	# 64-70
    sprite('hb000_02', 7)	# 71-77
    sprite('hb000_01', 7)	# 78-84
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hb090_00', 15)	# 85-99
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('104_guard_grap_2')
    Unknown1047(-11000)
    ScreenShake(5000, 20000)
    sprite('hb090_01', 6)	# 100-105
    sprite('hb090_02', 6)	# 106-111
    sprite('hb090_03', 6)	# 112-117
    sprite('hb090_04', 6)	# 118-123
    loopRest()
    enterState('CmnActStand')

@State
def Act3Event_BNvsHB03():
    sprite('hb611_00', 7)	# 1-7
    Unknown2004(1, 0)
    sprite('hb611_01', 7)	# 8-14
    sprite('hb611_02', 6)	# 15-20
    sprite('hb611_03', 6)	# 21-26
    sprite('hb611_04', 6)	# 27-32
    sprite('hb611_02', 6)	# 33-38
    sprite('hb611_03', 6)	# 39-44
    sprite('hb611_04', 6)	# 45-50
    sprite('hb611_02', 6)	# 51-56
    sprite('hb611_03', 6)	# 57-62
    sprite('hb611_04', 6)	# 63-68
    sprite('hb611_05', 7)	# 69-75
    sprite('hb611_06', 7)	# 76-82
    sprite('hb611_07', 6)	# 83-88
    SFX_3('hbse_08')
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    Unknown3025(0, 18)
    sprite('hb611_08', 6)	# 89-94
    sprite('hb611_09', 6)	# 95-100
    sprite('hb611_07', 6)	# 101-106
    Unknown3038(1)
    Unknown13044(1)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    GFX_0('hbef_611_shadow', 100)
    sprite('hb611_08', 6)	# 107-112
    Unknown3004(-10)
    sprite('hb611_09', 6)	# 113-118
    sprite('hb611_07', 6)	# 119-124
    Unknown21011(30)
    GFX_0('hbef_crow', 100)
    Unknown36(1)
    teleportRelativeX(-10000)
    Unknown1007(20000)
    Unknown35()
    sprite('hb611_08', 6)	# 125-130
    sprite('hb611_09', 6)	# 131-136
    Unknown3038(1)
    sprite('hb611_07', 6)	# 137-142
    sprite('hb611_08', 6)	# 143-148
    sprite('hb611_09', 6)	# 149-154
    label(2)
    sprite('hb611_07', 6)	# 155-160
    sprite('hb611_08', 6)	# 161-166
    sprite('hb611_09', 6)	# 167-172
    loopRest()
    gotoLabel(2)

@State
def Act3Event_tbvshb_01():

    def upon_IMMEDIATE():
        Unknown1000(-60000)
        sendToLabelUpon(32, 1)
    sprite('hb312_02', 32767)	# 1-32767
    label(1)
    sprite('hb090_00', 20)	# 32768-32787
    Unknown4046(-16744193, -16764673, -16776961)
    Unknown4045('65665f676972646d00000000000000000000000000000000000000000000000067000000')
    SFX_0('105_guard_slash_2')
    Unknown1047(-20000)
    ScreenShake(5000, 20000)
    sprite('hb090_01', 6)	# 32788-32793
    sprite('hb090_02', 6)	# 32794-32799
    sprite('hb090_03', 6)	# 32800-32805
    sprite('hb090_04', 6)	# 32806-32811
    loopRest()
    enterState('CmnActStand')