@Subroutine
def PreInit():
    Unknown12019('75687900000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Unknown12038(23000)
    Unknown12034(33)
    SuperFreezeDuration(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
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
    Unknown14020(1)
    Unknown14015(-2000, 464000, -248000, 114000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(1000, 500000, -258000, 168000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15015(30, 40)
    Unknown14015(0, 548000, -203000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 548000, -203000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 322000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 322000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 519000, -200000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 552000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 702000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(2000)
    Unknown14015(-200000, 200000, 200000, 600000, 500, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 450000, -200000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 432000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(-2000, 298000, -353000, 128000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-249000, 211000, -320000, 122000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(-161000, 132000, -353000, 34000, 1000, 50)
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
    Move_Register('ShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3008)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('ShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3008)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Shot_Explode', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_AirGround_(0x3000)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_PRESS_A)
    Unknown15012(6000)
    Unknown14015(14000, 1800000, -200000, 150000, 250, 25)
    Move_EndRegister()
    Move_Register('Shot_SlashB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3000)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(6000)
    Unknown14015(14000, 1800000, -200000, 200000, 250, 25)
    Move_EndRegister()
    Move_Register('AssultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(18000, 450000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('AssultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown14015(18000, 700000, -200000, 200000, 150, 50)
    Move_EndRegister()
    Move_Register('AirAssultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(18000, 450000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('AirAssultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown14015(18000, 550000, -200000, 200000, 150, 5)
    Move_EndRegister()
    Move_Register('Assult_2nd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(3000)
    Unknown14015(-150000, 450000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('Assult_3rd', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Unknown15013(3000)
    Unknown14015(-150000, 450000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('AssultEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15005(10)
    Unknown15014(5000)
    Unknown14015(18000, 790000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('ShotEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3008)
    Move_AirGround_(0x3009)
    Unknown15013(1)
    Unknown15012(2500)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Shot_SlashC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_AirGround_(0x3000)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(14000, 1800000, -200000, 200000, 250, 50)
    Move_EndRegister()
    Move_Register('AirAssultEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15005(10)
    Unknown15014(5000)
    Unknown14015(18000, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(7000, 266000, -123000, 755000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(7000, 266000, -123000, 755000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-300000, 300000, -200000, 755000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-300000, 300000, -200000, 755000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateBaleBringer', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(300000, 1000000, -200000, 100000, 250, 50)
    Move_EndRegister()
    Move_Register('UltimateBaleBringerOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(300000, 1000000, -200000, 100000, 250, 50)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(-350000, 850000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'AssultB', 10000000)
    Unknown14048('AntiAir', 0x4, 0xed)
    Unknown14048('Assault_C', 0x4, 0x79)
    Unknown14048('UltimateAssault2', 0x4, 0x5f)
    Unknown14048('UltimateAssault2_OD', 0x4, 0x5f)
    Unknown14048('BunshinAssault_A', 0x4, 0x45)
    Unknown14048('AirAssault', 0x4, 0xed)
    Unknown14049('NmlAtk5A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk5B', 'NmlAtk2C', 12, 0)
    Unknown14049('NmlAtk5D', 'BunshinAssault_A', 0, 0)
    Unknown14049('NmlAtk5D', 'BunshinAssault_B', 1, 600000)
    Unknown14049('NmlAtk5D', 'UltimateAssault', 6, 0)
    Unknown14049('NmlAtk5D', 'UltimateAssault_OD', 6, 0)
    Unknown14049('NmlAtk2A', 'NmlAtk5B', 0, 0)
    Unknown14049('NmlAtk2C', 'FHighJump', 12, 0)
    Unknown14049('NmlAtk2C', 'NmlAtk5D', 13, 0)
    Unknown14049('NmlAtk2D', 'BunshinAssault_A', 0, 0)
    Unknown14049('NmlAtk2D', 'BunshinAssault_B', 1, 600000)
    Unknown14049('NmlAtkAIR5A', 'NmlAtkAIR5B', 0, 0)
    Unknown14049('NmlAtkAIR5B', 'NmlAtkAIR5C', 0, 0)
    Unknown14049('NmlAtkAIR5C', 'AirAssault', 3, 0)
    Unknown14049('NmlAtkAIR5C', 'FJump', 12, 0)
    Unknown14049('NmlAtkAIR6D', 'AirAssault', 3, 0)
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
    Unknown7010(0, 'uhy000')
    Unknown7010(1, 'uhy001')
    Unknown7010(2, 'uhy002')
    Unknown7010(3, 'uhy003')
    Unknown7010(4, 'uhy004')
    Unknown7010(5, 'uhy005')
    Unknown7010(6, 'uhy006')
    Unknown7010(7, 'uhy007')
    Unknown7010(8, 'uhy008')
    Unknown7010(9, 'uhy009')
    Unknown7010(10, 'uhy010')
    Unknown7010(11, 'uhy011')
    Unknown7010(12, 'uhy012')
    Unknown7010(13, 'uhy013')
    Unknown7010(14, 'uhy014')
    Unknown7010(15, 'uhy015')
    Unknown7010(16, 'uhy016')
    Unknown7010(17, 'uhy017')
    Unknown7010(18, 'uhy018')
    Unknown7010(19, 'uhy019')
    Unknown7010(20, 'uhy020')
    Unknown7010(21, 'uhy021')
    Unknown7010(22, 'uhy022')
    Unknown7010(23, 'uhy023')
    Unknown7010(24, 'uhy024')
    Unknown7010(25, 'uhy025')
    Unknown7010(26, 'uhy026')
    Unknown7010(27, 'uhy027')
    Unknown7010(28, 'uhy028')
    Unknown7010(29, 'uhy029')
    Unknown7010(30, 'uhy030')
    Unknown7010(31, 'uhy031')
    Unknown7010(32, 'uhy032')
    Unknown7010(33, 'uhy033')
    Unknown7010(34, 'uhy034')
    Unknown7010(35, 'uhy035')
    Unknown7010(36, 'uhy036')
    Unknown7010(37, 'uhy037')
    Unknown7010(38, 'uhy038')
    Unknown7010(39, 'uhy039')
    Unknown7010(40, 'Hyd500')
    Unknown7010(41, 'uhy041')
    Unknown7010(42, 'uhy042')
    Unknown7010(43, 'uhy043')
    Unknown7010(44, 'uhy044')
    Unknown7010(45, 'uhy045')
    Unknown7010(46, 'uhy046')
    Unknown7010(47, 'uhy047')
    Unknown7010(48, 'uhy048')
    Unknown7010(49, 'uhy049')
    Unknown7010(50, 'uhy050')
    Unknown7010(51, 'uhy051')
    Unknown7010(52, 'uhy052')
    Unknown7010(53, 'uhy053')
    Unknown7010(54, 'uhy100_0')
    Unknown7010(55, 'uhy100_1')
    Unknown7010(56, 'uhy100_2')
    Unknown7010(63, 'uhy101_0')
    Unknown7010(64, 'uhy101_1')
    Unknown7010(65, 'uhy101_2')
    Unknown7010(57, 'uhy102_0')
    Unknown7010(58, 'uhy102_1')
    Unknown7010(59, 'uhy102_2')
    Unknown7010(66, 'uhy103_0')
    Unknown7010(67, 'uhy103_1')
    Unknown7010(68, 'uhy103_2')
    Unknown7010(60, 'uhy104_0')
    Unknown7010(61, 'uhy104_1')
    Unknown7010(62, 'uhy104_2')
    Unknown7010(69, 'uhy105_0')
    Unknown7010(70, 'uhy105_1')
    Unknown7010(71, 'uhy105_2')
    Unknown7010(72, 'uhy150')
    Unknown7010(73, 'uhy151')
    Unknown7010(74, 'uhy152')
    Unknown7010(85, 'uhy153')
    Unknown7010(94, 'uhy400')
    Unknown7010(95, 'uhy401')
    Unknown7010(96, 'uhy161_0')
    Unknown7010(97, 'uhy161_1')
    Unknown7010(98, 'uhy163_0')
    Unknown7010(99, 'uhy163_1')
    Unknown7010(100, 'uhy164_0')
    Unknown7010(101, 'uhy164_1')
    Unknown7010(102, 'uhy166_0')
    Unknown7010(103, 'uhy166_1')
    Unknown7010(92, 'uhy162_0')
    Unknown7010(93, 'uhy162_1')
    Unknown7010(90, 'uhy167_0')
    Unknown7010(91, 'uhy167_1')
    Unknown7010(105, 'uhy165_0')
    Unknown7010(106, 'uhy165_1')
    Unknown7010(107, 'uhy168_0')
    Unknown7010(108, 'uhy168_1')
    Unknown7010(110, 'uhy169_0')
    Unknown7010(111, 'uhy169_1')
    Unknown7010(112, 'uhy159_0')
    Unknown7010(113, 'uhy159_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746542616c654272696e67657200000000000000000000000000')
    Unknown12059('05000000556c74696d61746542616c654272696e6765724f440000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MatchInit2():
    SLOT_64 = 600
    SLOT_65 = 100
    SLOT_66 = 100

@Subroutine
def InsulatorInit():
    Unknown9016(1)
    Unknown11057(0)
    Unknown11050('020000004879645f35303100000000000000000000000000000000000000000000000000')
    ChipDamagePct(20)

@Subroutine
def InsulatorSpecialInit():
    Unknown9016(1)
    Unknown11057(0)
    Unknown11050('020000004879645f35303100000000000000000000000000000000000000000000000000')
    Unknown9266(11)
    ChipDamagePct(30)

@State
def CmnActStand():
    sprite('Action_000_00', 1)	# 1-1	 **attackbox here**
    label(0)
    sprite('Action_000_00', 7)	# 2-8	 **attackbox here**
    sprite('Action_000_01', 7)	# 9-15	 **attackbox here**
    sprite('Action_000_02', 6)	# 16-21	 **attackbox here**
    sprite('Action_000_03', 6)	# 22-27	 **attackbox here**
    sprite('Action_000_04', 5)	# 28-32	 **attackbox here**
    sprite('Action_000_05', 5)	# 33-37	 **attackbox here**
    sprite('Action_000_06', 5)	# 38-42	 **attackbox here**
    sprite('Action_000_07', 6)	# 43-48	 **attackbox here**
    sprite('Action_000_08', 6)	# 49-54	 **attackbox here**
    sprite('Action_000_09', 7)	# 55-61	 **attackbox here**
    sprite('Action_000_10', 7)	# 62-68	 **attackbox here**
    sprite('Action_000_11', 6)	# 69-74	 **attackbox here**
    sprite('Action_000_12', 6)	# 75-80	 **attackbox here**
    sprite('Action_000_13', 5)	# 81-85	 **attackbox here**
    sprite('Action_000_14', 5)	# 86-90	 **attackbox here**
    sprite('Action_000_15', 5)	# 91-95	 **attackbox here**
    sprite('Action_000_16', 6)	# 96-101	 **attackbox here**
    sprite('Action_000_17', 6)	# 102-107	 **attackbox here**
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    label(1)
    sprite('Action_000_19', 4)	# 108-111
    SLOT_88 = 960
    sprite('Action_000_20', 8)	# 112-119
    SFX_1('uhy000')
    sprite('Action_000_21', 11)	# 120-130
    sprite('Action_000_22', 5)	# 131-135	 **attackbox here**
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffEntryBlade01', 100)
    sprite('Action_000_23', 12)	# 136-147	 **attackbox here**
    sprite('Action_000_24', 6)	# 148-153	 **attackbox here**
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

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 5)	# 1-5
    sprite('Action_013_01', 5)	# 6-10
    sprite('Action_013_02', 5)	# 11-15
    sprite('Action_013_03', 5)	# 16-20
    sprite('Action_013_04', 5)	# 21-25
    sprite('Action_013_05', 5)	# 26-30
    sprite('Action_013_06', 5)	# 31-35
    sprite('Action_013_07', 5)	# 36-40
    sprite('Action_013_08', 5)	# 41-45
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
    sprite('Action_014_03', 3)	# 10-12

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
    label(0)
    sprite('Action_036_01', 4)	# 1-4
    sprite('Action_036_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_01', 4)	# 9-12
    sprite('Action_035_01', 4)	# 13-16
    gotoLabel(1)

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        _gotolabel(1)
    label(0)
    sprite('Action_036_02', 3)	# 1-3
    sprite('Action_036_03', 3)	# 4-6
    sprite('Action_036_04', 2)	# 7-8
    sprite('Action_036_05', 2)	# 9-10
    ExitState()
    label(1)
    sprite('Action_035_02', 3)	# 11-13
    sprite('Action_035_03', 3)	# 14-16
    sprite('Action_035_04', 2)	# 17-18
    sprite('Action_035_05', 2)	# 19-20
    ExitState()

@State
def CmnActJumpDown():
    label(0)
    sprite('Action_022_00', 3)	# 1-3
    sprite('Action_022_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('Action_021_00', 3)	# 1-3
    sprite('Action_021_01', 4)	# 4-7
    sprite('Action_021_02', 4)	# 8-11
    sprite('Action_021_03', 3)	# 12-14
    sprite('Action_021_04', 3)	# 15-17

@State
def CmnActLandingStiffLoop():
    sprite('Action_023_00', 2)	# 1-2
    sprite('Action_023_01', 2)	# 3-4
    sprite('Action_023_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('Action_023_03', 3)	# 1-3
    sprite('Action_023_04', 3)	# 4-6

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
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_08', 5)	# 41-45
    sprite('Action_010_09', 5)	# 46-50
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
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_045_00', 6)	# 1-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 3)	# 10-12
    label(0)
    sprite('Action_045_03', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 16-18
    sprite('Action_045_05', 3)	# 19-21
    sprite('Action_045_06', 3)	# 22-24
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 25-27
    sprite('Action_045_08', 3)	# 28-30
    sprite('Action_045_09', 3)	# 31-33
    sprite('Action_045_02', 3)	# 34-36
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_12', 6)	# 1-6
    sprite('Action_045_13', 6)	# 7-12

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

        def upon_CLEAR_OR_EXIT():
            Unknown1019(90)
    sprite('Action_046_00', 4)	# 1-4
    sprite('Action_046_01', 2)	# 5-6
    physicsXImpulse(-43000)
    Unknown8002()
    sprite('Action_046_02', 2)	# 7-8
    sprite('Action_046_03', 3)	# 9-11
    sprite('Action_046_04', 3)	# 12-14
    sprite('Action_046_05', 4)	# 15-18
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    Unknown1019(10)
    sprite('Action_046_06', 4)	# 19-22

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('Hyd405_00', 3)	# 1-3
    sprite('Action_068_01', 3)	# 4-6
    sprite('Action_068_02', 3)	# 7-9
    sprite('Action_068_03', 3)	# 10-12
    sprite('Action_068_04', 3)	# 13-15
    sprite('Action_068_05', 3)	# 16-18
    sprite('Action_068_06', 3)	# 19-21
    sprite('Action_068_07', 3)	# 22-24
    sprite('Action_068_08', 3)	# 25-27
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
    label(0)
    sprite('Action_068_10', 3)	# 4-6
    sprite('Action_068_11', 3)	# 7-9
    sprite('Action_068_12', 3)	# 10-12
    loopRest()
    gotoLabel(0)

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
    sprite('Action_032_06', 3)	# 24-26
    sprite('Action_032_07', 3)	# 27-29

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
    sprite('Action_041_08', 4)	# 1-4
    sprite('Action_041_09', 4)	# 5-8
    sprite('Action_041_10', 4)	# 9-12
    sprite('Action_041_11', 3)	# 13-15

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
    sprite('Action_036_01', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_402_00', 2)	# 1-2
    sprite('Action_402_01', 2)	# 3-4
    sprite('Action_402_02', 2)	# 5-6
    sprite('Action_402_03', 2)	# 7-8	 **attackbox here**
    sprite('Action_402_04', 3)	# 9-11
    sprite('Action_402_05', 5)	# 12-16
    sprite('Action_402_06', 4)	# 17-20
    sprite('Action_402_07', 3)	# 21-23
    sprite('Action_402_08', 3)	# 24-26

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
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4
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
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('Action_262_07', 3)	# 1-3
    sprite('Action_262_08', 3)	# 4-6
    label(0)
    sprite('Action_022_00', 4)	# 7-10
    sprite('Action_022_01', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('Action_262_00', 4)	# 1-4
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4
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
    sprite('Action_262_01', 32767)	# 5-32771
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('Action_262_02', 4)	# 1-4
    label(0)
    sprite('Action_262_03', 5)	# 5-9
    sprite('Action_262_04', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('Action_262_07', 3)	# 1-3
    sprite('Action_262_08', 3)	# 4-6
    label(0)
    sprite('Action_022_00', 4)	# 7-10
    sprite('Action_022_01', 4)	# 11-14
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
    sprite('Action_262_09', 4)	# 7-10
    sprite('Action_262_10', 4)	# 11-14
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
    sprite('Action_276_23', 32767)	# 32-32798	 **attackbox here**
    label(1)
    sprite('Action_276_23ex', 1)	# 32799-32799	 **attackbox here**
    sprite('Action_021_00', 5)	# 32800-32804
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_021_01', 12)	# 32805-32816
    sprite('Action_021_02', 5)	# 32817-32821
    sprite('Action_021_03', 4)	# 32822-32825
    sprite('Action_021_04', 4)	# 32826-32829

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('InsulatorInit')
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('Action_021_00', 2)	# 2-3
    sprite('Action_021_01', 3)	# 4-6
    sprite('Action_021_02', 3)	# 7-9
    sprite('Action_021_03', 3)	# 10-12
    sprite('Action_021_04', 3)	# 13-15
    sprite('Action_222_17', 4)	# 16-19
    sprite('Action_222_18', 4)	# 20-23
    sprite('Action_222_19', 4)	# 24-27
    sprite('Action_222_20', 4)	# 28-31
    sprite('Action_222_21', 3)	# 32-34
    Unknown7009(2)
    GFX_0('EffNmlAtk6CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_222_22ex', 2)	# 35-36	 **attackbox here**
    sprite('Action_222_23', 3)	# 37-39
    sprite('Action_222_24', 3)	# 40-42
    sprite('Action_222_23', 3)	# 43-45
    sprite('Action_222_24', 3)	# 46-48
    sprite('Action_222_23', 3)	# 49-51
    sprite('Action_222_24', 3)	# 52-54
    sprite('Action_222_25', 3)	# 55-57
    sprite('Action_222_26', 3)	# 58-60
    sprite('Action_222_27', 3)	# 61-63
    sprite('Action_222_28', 3)	# 64-66
    sprite('Action_222_29', 3)	# 67-69
    sprite('Action_222_30', 3)	# 70-72
    sprite('Action_222_31', 3)	# 73-75

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        PushbackX(12000)
        callSubroutine('InsulatorInit')
        Unknown11050('020000004879645f35303000000000000000000000000000000000000000000000000000')
        Unknown1112('')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_001_00', 4)	# 1-4
    sprite('Action_001_01', 2)	# 5-6
    GFX_0('EffNmlAtk5ABlade', 100)
    Unknown7009(0)
    SFX_3('SE_InsulatorSwingA')
    sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_001_03', 7)	# 9-15
    Recovery()
    Unknown2063()
    sprite('Action_001_04', 2)	# 16-17
    sprite('Action_001_05', 2)	# 18-19
    sprite('Action_001_06', 5)	# 20-24
    sprite('Action_001_07', 2)	# 25-26

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(0)
        callSubroutine('InsulatorInit')
        HitJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_002_00', 3)	# 1-3
    sprite('Action_002_01', 3)	# 4-6
    sprite('Action_002_02', 2)	# 7-8
    Unknown7009(0)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_002_03', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk5AA', 100)
    sprite('Action_002_04', 2)	# 11-12	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_002_05', 6)	# 13-18
    DisableAttackRestOfMove()
    sprite('Action_002_06', 4)	# 19-22
    sprite('Action_002_07', 2)	# 23-24
    sprite('Action_002_08', 3)	# 25-27
    sprite('Action_002_09', 3)	# 28-30

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(70)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(18000)
        AirUntechableTime(22)
        callSubroutine('InsulatorInit')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_192_00', 5)	# 1-5
    sprite('Action_192_01', 2)	# 6-7
    Unknown7009(1)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_192_02', 2)	# 8-9	 **attackbox here**
    teleportRelativeX(7000)
    GFX_0('EffNmlAtk5BBlade00', 100)
    sprite('Action_192_03', 3)	# 10-12
    sprite('Action_192_04', 2)	# 13-14
    sprite('Action_192_05', 5)	# 15-19
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_192_06', 2)	# 20-21	 **attackbox here**
    teleportRelativeX(40000)
    GFX_0('EffNmlAtk5BBlade01', 100)
    RefreshMultihit()
    AirPushbackX(-6000)
    PushbackX(-6000)

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('AN_NmlAtk5A_4th')
    sprite('Action_192_07', 6)	# 22-27
    Recovery()
    Unknown2063()
    sprite('Action_192_08', 6)	# 28-33
    sprite('Action_192_09', 4)	# 34-37
    sprite('Action_192_10', 4)	# 38-41
    sprite('Action_192_11', 4)	# 42-45

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(23000)
        AirPushbackY(-32000)
        YImpluseBeforeWallbounce(800)
        PushbackX(19800)
        Unknown9310(1)
        AirUntechableTime(32)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('InsulatorInit')
        Unknown11044(1)
        JumpCancel_(0)
        sendToLabelUpon(2, 0)
    sprite('Action_196_00', 1)	# 1-1
    sprite('Action_196_01', 1)	# 2-2
    sprite('Action_196_02', 2)	# 3-4
    Unknown8001(0, 100)
    physicsXImpulse(36000)
    physicsYImpulse(12000)
    setGravity(2300)
    Unknown2016(350)
    sprite('Action_196_03', 2)	# 5-6
    sprite('Action_196_04', 2)	# 7-8
    sprite('Action_196_05', 2)	# 9-10
    tag_voice(1, 'uhy203_0', 'uhy203_1', 'uhy203_2', '')
    sprite('Action_196_06', 300)	# 11-310
    label(0)
    sprite('Action_196_07', 2)	# 311-312	 **attackbox here**
    Unknown1019(10)
    GFX_0('EffShotSlashBlade', 100)
    SFX_3('SE043')
    Unknown2016(-1)
    Unknown30088(1)
    sprite('Action_196_08', 10)	# 313-322
    Unknown8000(100, 1, 1)
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('Action_196_09', 5)	# 323-327
    sprite('Action_196_10', 5)	# 328-332
    sprite('Action_196_11', 5)	# 333-337
    sprite('Action_196_12', 5)	# 338-342

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(8000)
        AirPushbackY(20000)
        callSubroutine('InsulatorInit')
        Unknown1112('')
        HitJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 2)	# 3-4
    teleportRelativeX(25000)
    sprite('Action_003_02', 4)	# 5-8
    teleportRelativeX(50000)
    label(10)
    sprite('Action_003_14', 1)	# 9-9
    sprite('Action_003_15', 1)	# 10-10
    sprite('Action_003_16', 1)	# 11-11
    physicsXImpulse(35000)
    Unknown1030(-9000)
    sprite('Action_003_17', 1)	# 12-12
    Unknown7009(2)
    SFX_3('SE_InsulatorSwingC')
    GFX_0('EffNmlAtk5CBlade', 100)
    sprite('Action_003_18', 5)	# 13-17	 **attackbox here**
    Unknown1084(1)
    sprite('Action_003_19', 2)	# 18-19
    Recovery()
    Unknown2063()
    sprite('Action_003_20', 4)	# 20-23
    sprite('Action_003_20', 3)	# 24-26
    sprite('Action_003_21', 5)	# 27-31
    sprite('Action_003_22', 5)	# 32-36

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(1700)
        AirPushbackX(28000)
        AirPushbackY(12000)
        AirUntechableTime(30)
        callSubroutine('InsulatorInit')

        def upon_STATE_END():
            Unknown12046(0)
        HitJumpCancel(1)
        HitOrBlockCancel('AN_NmlAtk5B_3rd')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_222_17', 3)	# 1-3
    sprite('Action_222_18', 3)	# 4-6
    teleportRelativeX(30000)
    sprite('Action_222_19', 3)	# 7-9
    sprite('Action_222_20', 3)	# 10-12
    teleportRelativeX(20000)
    Unknown12046(50)
    sprite('Action_222_21', 2)	# 13-14
    tag_voice(1, 'uhy108_0', 'uhy108_1', 'uhy108_2', '')
    GFX_0('EffNmlAtk6CBlade', 100)
    Unknown12046(100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_222_22', 2)	# 15-16	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_222_23', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('Action_222_24', 4)	# 20-23
    sprite('Action_222_25', 4)	# 24-27
    sprite('Action_222_26', 4)	# 28-31
    sprite('Action_222_27', 4)	# 32-35
    Unknown12046(0)
    sprite('Action_222_28', 5)	# 36-40
    teleportRelativeX(-10000)
    sprite('Action_222_29', 4)	# 41-44
    teleportRelativeX(-30000)
    sprite('Action_222_30', 4)	# 45-48
    teleportRelativeX(-30000)
    sprite('Action_222_31', 3)	# 49-51

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        DisableAttackRestOfMove()
        JumpCancel_(0)
    sprite('Action_180_00', 3)	# 1-3
    sprite('Action_180_00', 3)	# 4-6
    GFX_0('EffChnageBlade00', 0)
    sprite('Action_180_01', 2)	# 7-8
    sprite('Action_180_02', 2)	# 9-10
    sprite('Action_180_03', 1)	# 11-11
    teleportRelativeX(50000)
    sprite('Action_180_03', 1)	# 12-12
    teleportRelativeX(50000)
    sprite('Action_180_04', 2)	# 13-14	 **attackbox here**
    SFX_3('SE043')
    GFX_0('EffChnageBlade01', 100)
    GFX_0('EffChnageBlade02', 100)
    tag_voice(0, 'uhy210_0', 'uhy210_1', 'uhy210_2', '')
    sprite('Action_180_05', 3)	# 15-17
    sprite('Action_180_05', 6)	# 18-23
    GFX_0('EdgeShot', 0)
    Unknown4004('6566666563745f33383000000000000000000000000000000000000000000000ffff0000')
    Unknown36(1)
    teleportRelativeX(400000)
    Unknown1056(500)
    Unknown1064(500)
    Unknown35()
    sprite('Action_180_05', 6)	# 24-29
    JumpCancel_(1)
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_180_06', 4)	# 30-33
    Recovery()
    Unknown2063()
    sprite('Action_180_07', 5)	# 34-38
    teleportRelativeX(-25000)
    sprite('Action_180_08', 5)	# 39-43
    teleportRelativeX(-25000)
    sprite('Action_180_09', 4)	# 44-47
    teleportRelativeX(-25000)
    sprite('Action_180_10', 3)	# 48-50
    teleportRelativeX(-25000)
    sprite('Action_180_11', 3)	# 51-53

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockJumpCancel(1)
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 3)	# 1-3
    Unknown1051(60)
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(0)
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    SFX_3('SE041')
    sprite('Action_004_03', 3)	# 9-11
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 12-16
    Unknown2001()
    sprite('Action_004_05', 4)	# 17-20
    sprite('Action_004_06', 4)	# 21-24

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        HitOrBlockJumpCancel(1)
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 3)	# 1-3
    Unknown1051(60)
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(0)
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    SFX_3('SE041')
    sprite('Action_004_03', 3)	# 9-11
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 12-16
    Unknown2001()
    sprite('Action_004_05', 4)	# 17-20
    sprite('Action_004_06', 4)	# 21-24

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirPushbackY(28000)
        AirUntechableTime(24)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('InsulatorInit')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_190_00', 2)	# 1-2
    sprite('Action_190_01', 2)	# 3-4
    teleportRelativeX(30000)
    sprite('Action_190_01', 3)	# 5-7
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_190_02', 3)	# 8-10
    tag_voice(1, 'uhy106_0', 'uhy106_1', 'uhy106_2', '')
    sprite('Action_190_03', 2)	# 11-12	 **attackbox here**
    GFX_0('EffNmlAtk2CBlade', 100)
    teleportRelativeX(30000)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_190_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('Action_190_05', 2)	# 17-18
    Unknown2001()
    sprite('Action_190_06', 6)	# 19-24
    sprite('Action_190_07', 5)	# 25-29
    sprite('Action_190_08', 6)	# 30-35

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(16000)
        AirUntechableTime(26)
        Unknown11058('0000000000000000010000000000000000000000')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
    sprite('Action_006_00', 5)	# 1-5
    sprite('Action_006_01', 2)	# 6-7
    sprite('Action_006_02', 2)	# 8-9
    sprite('Action_006_03', 2)	# 10-11
    tag_voice(1, 'uhy107_0', 'uhy107_1', 'uhy107_2', '')
    physicsXImpulse(40000)
    Unknown1028(-10000)
    SFX_3('SE043')
    sprite('Action_006_04', 5)	# 12-16	 **attackbox here**
    Unknown1084(1)
    sprite('Action_006_05', 4)	# 17-20
    Recovery()
    Unknown2063()
    DisableAttackRestOfMove()
    sprite('Action_006_06', 4)	# 21-24
    sprite('Action_006_07', 4)	# 25-28
    sprite('Action_006_08', 5)	# 29-33

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        callSubroutine('InsulatorInit')
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_00', 3)	# 1-3
    sprite('Action_009_12', 4)	# 4-7
    sprite('Action_009_13', 1)	# 8-8
    sprite('Action_009_14', 2)	# 9-10
    Unknown7009(4)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_009_15', 3)	# 11-13	 **attackbox here**
    GFX_0('EffNmlAtkAir5BBlade', 100)
    sprite('Action_009_16', 5)	# 14-18
    Recovery()
    Unknown2063()
    sprite('Action_009_17', 4)	# 19-22
    sprite('Action_009_18', 3)	# 23-25
    sprite('Action_009_19', 3)	# 26-28
    sprite('Action_009_20', 4)	# 29-32

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(15000)
        callSubroutine('InsulatorInit')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_191_00', 8)	# 1-8
    sprite('Action_191_01', 3)	# 9-11
    Unknown7009(5)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_191_02', 3)	# 12-14	 **attackbox here**
    GFX_0('EffNmlAtkAir5CBlade', 100)
    sprite('Action_191_03', 8)	# 15-22
    Recovery()
    Unknown2063()
    sprite('Action_191_04', 6)	# 23-28
    sprite('Action_191_05', 5)	# 29-33

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1100)
        Unknown11092(1)
        Hitstop(7)
        callSubroutine('InsulatorInit')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_240_00', 2)	# 1-2
    sprite('Action_240_01', 1)	# 3-3
    sprite('Action_240_02', 1)	# 4-4
    sprite('Action_240_03', 2)	# 5-6
    sprite('Action_240_04', 2)	# 7-8
    sprite('Action_240_05', 2)	# 9-10
    sprite('Action_240_06', 1)	# 11-11
    sprite('Action_240_07', 2)	# 12-13
    GFX_0('Hyd_244', 0)
    Unknown7009(5)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_240_08', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_08', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_240_09', 8)	# 18-25
    Recovery()
    Unknown2063()
    sprite('Action_240_10', 4)	# 26-29
    sprite('Action_240_11', 4)	# 30-33
    sprite('Action_240_12', 3)	# 34-36
    sprite('Action_240_13', 4)	# 37-40

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1000)
        AttackP2(85)
        Unknown11092(1)
        AirPushbackX(-4000)
        AirPushbackY(-20000)
        PushbackX(-12000)
        Unknown9310(1)
        HitOverhead(0)
        callSubroutine('InsulatorInit')
        JumpCancel_(0)
        Unknown22004(10, 1)
    sprite('Action_230_00', 3)	# 1-3
    sprite('Action_230_00', 3)	# 4-6
    Unknown1084(1)
    sprite('Action_230_01', 2)	# 7-8
    GFX_0('FloatShot_Blade00', 100)
    sprite('Action_230_02', 3)	# 9-11	 **attackbox here**
    tag_voice(1, 'uhy212_0', 'uhy212_1', 'uhy212_2', '')
    SFX_3('SE_InsulatorSwingA')
    sprite('Action_230_03', 2)	# 12-13
    sprite('Action_230_04', 2)	# 14-15
    sprite('Action_230_05', 2)	# 16-17
    sprite('Action_230_06', 3)	# 18-20
    physicsXImpulse(-6000)
    physicsYImpulse(24000)
    Unknown1043()
    if CheckInput(0x79):
        Unknown1019(-100)
        Unknown23159('AN_NmlAtkAIR5C_FrontMove')
    GFX_0('FloatShot_Blade01', 100)
    GFX_0('FloatShot', 100)
    sprite('Action_230_05', 3)	# 21-23
    sprite('Action_230_06', 3)	# 24-26
    sprite('Action_230_05', 3)	# 27-29
    sprite('Action_230_06', 3)	# 30-32
    sprite('Action_230_05', 3)	# 33-35
    sprite('Action_230_06', 3)	# 36-38
    sprite('Action_230_05', 3)	# 39-41
    sprite('Action_230_06', 3)	# 42-44
    sprite('Action_230_08', 3)	# 45-47
    Recovery()
    Unknown2063()
    sprite('Action_230_09', 3)	# 48-50

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('InsulatorInit')
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
    tag_voice(1, 'uhy156_0', 'uhy156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 2)	# 14-15
    sprite('Action_009_00', 3)	# 16-18
    sprite('Action_009_12', 4)	# 19-22
    sprite('Action_009_13', 1)	# 23-23
    sprite('Action_009_14', 2)	# 24-25
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_009_15', 3)	# 26-28	 **attackbox here**
    GFX_0('EffNmlAtkAir5BBlade', 100)
    sprite('Action_009_16', 5)	# 29-33
    sprite('Action_009_17', 4)	# 34-37
    sprite('Action_009_18', 3)	# 38-40
    sprite('Action_009_19', 3)	# 41-43
    sprite('Action_009_20', 4)	# 44-47
    label(0)
    sprite('Action_068_09', 3)	# 48-50
    sprite('Action_068_10', 2)	# 51-52
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_138_00', 2)	# 53-54
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_138_01', 6)	# 55-60
    sprite('Action_138_02', 2)	# 61-62
    Unknown18009(0)
    sprite('Action_138_03', 2)	# 63-64
    sprite('Action_138_04', 1)	# 65-65

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        callSubroutine('InsulatorInit')
        loopRelated(17, 16)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_009_16', 5)	# 1-5
    sprite('Action_009_17', 4)	# 6-9
    sprite('Action_009_18', 3)	# 10-12
    sprite('Action_009_19', 3)	# 13-15
    sprite('Action_009_20', 4)	# 16-19
    sprite('Action_068_09', 3)	# 20-22
    sprite('Action_068_10', 2)	# 23-24
    label(1)
    sprite('Action_138_00', 1)	# 25-25
    Unknown8000(100, 1, 1)
    sprite('Action_138_01', 2)	# 26-27
    sprite('Action_138_02', 1)	# 28-28
    sprite('Action_138_03', 1)	# 29-29
    sprite('Action_138_04', 1)	# 30-30
    sprite('Action_000_00', 7)	# 31-37	 **attackbox here**
    label(2)
    sprite('Action_192_03', 3)	# 38-40
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('Action_192_04', 4)	# 41-44
    tag_voice(0, 'uhy157_0', 'uhy157_1', '', '')
    sprite('Action_192_05', 6)	# 45-50
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_192_06', 3)	# 51-53	 **attackbox here**
    GFX_0('EffNmlAtk5BBlade01', 100)
    RefreshMultihit()
    sprite('Action_192_07', 3)	# 54-56
    sprite('Action_192_08', 3)	# 57-59
    sprite('Action_192_09', 3)	# 60-62
    sprite('Action_192_10', 3)	# 63-65
    sprite('Action_192_11', 3)	# 66-68
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('Action_000_00', 7)	# 69-75	 **attackbox here**
    sprite('Action_000_01', 7)	# 76-82	 **attackbox here**
    sprite('Action_000_02', 6)	# 83-88	 **attackbox here**
    sprite('Action_000_03', 6)	# 89-94	 **attackbox here**
    sprite('Action_000_04', 5)	# 95-99	 **attackbox here**
    sprite('Action_000_05', 5)	# 100-104	 **attackbox here**
    sprite('Action_000_06', 5)	# 105-109	 **attackbox here**
    sprite('Action_000_07', 6)	# 110-115	 **attackbox here**
    sprite('Action_000_08', 6)	# 116-121	 **attackbox here**
    sprite('Action_000_09', 7)	# 122-128	 **attackbox here**
    sprite('Action_000_10', 7)	# 129-135	 **attackbox here**
    sprite('Action_000_11', 6)	# 136-141	 **attackbox here**
    sprite('Action_000_12', 6)	# 142-147	 **attackbox here**
    sprite('Action_000_13', 5)	# 148-152	 **attackbox here**
    sprite('Action_000_14', 5)	# 153-157	 **attackbox here**
    sprite('Action_000_15', 5)	# 158-162	 **attackbox here**
    sprite('Action_000_16', 6)	# 163-168	 **attackbox here**
    sprite('Action_000_17', 6)	# 169-174	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 175-175

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        callSubroutine('InsulatorInit')
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_012_00', 2)	# 1-2
    sprite('Action_012_01', 2)	# 3-4
    sprite('Action_190_00', 3)	# 5-7
    sprite('Action_190_01', 4)	# 8-11
    sprite('Action_190_02', 3)	# 12-14
    sprite('Action_190_03', 2)	# 15-16	 **attackbox here**
    GFX_0('EffNmlAtk2CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_190_04', 4)	# 17-20
    sprite('Action_190_05', 2)	# 21-22
    sprite('Action_190_06', 5)	# 23-27
    sprite('Action_190_07', 5)	# 28-32
    sprite('Action_190_08', 6)	# 33-38
    sprite('Action_012_01', 2)	# 39-40
    sprite('Action_012_00', 2)	# 41-42
    label(0)
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
    sprite('Action_000_14', 6)	# 127-132	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 133-133

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        callSubroutine('InsulatorInit')
    sprite('Action_222_17', 4)	# 1-4
    sprite('Action_222_18', 4)	# 5-8
    sprite('Action_222_19', 4)	# 9-12
    sprite('Action_222_20', 4)	# 13-16
    sprite('Action_222_21', 3)	# 17-19
    tag_voice(0, 'uhy158_0', 'uhy158_1', '', '')
    GFX_0('EffNmlAtk6CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_222_22ex', 2)	# 20-21	 **attackbox here**
    sprite('Action_222_23', 3)	# 22-24
    sprite('Action_222_24', 3)	# 25-27
    sprite('Action_222_23', 3)	# 28-30
    sprite('Action_222_24', 3)	# 31-33
    sprite('Action_222_23', 3)	# 34-36
    sprite('Action_222_24', 3)	# 37-39
    sprite('Action_222_25', 3)	# 40-42
    sprite('Action_222_26', 3)	# 43-45
    sprite('Action_222_27', 3)	# 46-48
    sprite('Action_222_28', 3)	# 49-51
    sprite('Action_222_29', 3)	# 52-54
    sprite('Action_222_30', 3)	# 55-57
    sprite('Action_222_31', 3)	# 58-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        callSubroutine('InsulatorInit')
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('Action_000_00', 7)	# 1-7	 **attackbox here**
    sprite('Action_000_01', 7)	# 8-14	 **attackbox here**
    sprite('Action_000_02', 6)	# 15-20	 **attackbox here**
    sprite('Action_000_03', 6)	# 21-26	 **attackbox here**
    sprite('Action_000_04', 8)	# 27-34	 **attackbox here**
    sprite('Action_000_05', 5)	# 35-39	 **attackbox here**
    sprite('Action_000_06', 5)	# 40-44	 **attackbox here**
    sprite('Action_000_07', 5)	# 45-49	 **attackbox here**
    sprite('Action_000_08', 6)	# 50-55	 **attackbox here**
    sprite('Action_000_09', 5)	# 56-60	 **attackbox here**
    sprite('Action_000_10', 6)	# 61-66	 **attackbox here**
    sprite('Action_000_11', 8)	# 67-74	 **attackbox here**
    sprite('Action_000_12', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_13', 5)	# 80-84	 **attackbox here**
    sprite('Action_000_14', 6)	# 85-90	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_222_17', 4)	# 91-94
    sprite('Action_222_18', 4)	# 95-98
    sprite('Action_222_19', 4)	# 99-102
    sprite('Action_222_20', 4)	# 103-106
    sprite('Action_222_21', 3)	# 107-109
    tag_voice(0, 'uhy158_0', 'uhy158_1', '', '')
    GFX_0('EffNmlAtk6CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_222_22ex', 2)	# 110-111	 **attackbox here**
    sprite('Action_222_23', 3)	# 112-114
    sprite('Action_222_24', 3)	# 115-117
    sprite('Action_222_23', 3)	# 118-120
    sprite('Action_222_24', 3)	# 121-123
    sprite('Action_222_23', 3)	# 124-126
    sprite('Action_222_24', 3)	# 127-129
    sprite('Action_222_25', 3)	# 130-132
    sprite('Action_222_26', 3)	# 133-135
    sprite('Action_222_27', 3)	# 136-138
    sprite('Action_222_28', 3)	# 139-141
    sprite('Action_222_29', 3)	# 142-144
    sprite('Action_222_30', 3)	# 145-147
    sprite('Action_222_31', 3)	# 148-150

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        callSubroutine('InsulatorInit')
    sprite('null', 22)	# 1-22
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 23-23
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_196_01', 3)	# 24-26
    sprite('Action_196_02', 2)	# 27-28
    Unknown8001(0, 100)
    physicsXImpulse(23000)
    physicsYImpulse(20000)
    setGravity(3500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('Action_196_03', 3)	# 29-31
    sprite('Action_196_04', 4)	# 32-35
    sprite('Action_196_05', 4)	# 36-39
    sprite('Action_196_06', 5)	# 40-44
    label(1)
    sprite('Action_196_07', 2)	# 45-46	 **attackbox here**
    Unknown1019(0)
    GFX_0('EffShotSlashBlade', 100)
    SFX_3('SE043')
    sprite('Action_196_08', 3)	# 47-49
    Unknown8000(100, 1, 1)
    sprite('Action_196_09', 3)	# 50-52
    sprite('Action_196_10', 3)	# 53-55
    sprite('Action_196_11', 3)	# 56-58
    sprite('Action_196_12', 3)	# 59-61
    sprite('Action_000_00', 7)	# 62-68	 **attackbox here**
    sprite('Action_000_01', 7)	# 69-75	 **attackbox here**
    sprite('Action_000_02', 6)	# 76-81	 **attackbox here**
    sprite('Action_000_03', 6)	# 82-87	 **attackbox here**
    sprite('Action_000_04', 8)	# 88-95	 **attackbox here**
    sprite('Action_000_05', 5)	# 96-100	 **attackbox here**
    sprite('Action_000_06', 5)	# 101-105	 **attackbox here**
    sprite('Action_000_07', 5)	# 106-110	 **attackbox here**
    sprite('Action_000_08', 6)	# 111-116	 **attackbox here**
    sprite('Action_000_09', 5)	# 117-121	 **attackbox here**
    sprite('Action_000_10', 6)	# 122-127	 **attackbox here**
    sprite('Action_000_11', 8)	# 128-135	 **attackbox here**
    sprite('Action_000_12', 5)	# 136-140	 **attackbox here**
    sprite('Action_000_13', 5)	# 141-145	 **attackbox here**
    sprite('Action_000_14', 6)	# 146-151	 **attackbox here**

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        callSubroutine('InsulatorInit')
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 2)	# 3-4
    sprite('Action_003_02', 4)	# 5-8
    sprite('Action_003_03', 1)	# 9-9
    sprite('Action_003_04', 1)	# 10-10
    sprite('Action_003_05', 1)	# 11-11
    GFX_0('EffNmlAtk5CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_003_06', 5)	# 12-16	 **attackbox here**
    sprite('Action_003_07', 2)	# 17-18
    sprite('Action_003_08', 8)	# 19-26
    sprite('Action_003_09', 6)	# 27-32
    sprite('Action_003_10', 6)	# 33-38
    loopRest()
    sprite('Action_000_00', 7)	# 39-45	 **attackbox here**
    sprite('Action_000_01', 7)	# 46-52	 **attackbox here**
    sprite('Action_000_02', 6)	# 53-58	 **attackbox here**
    sprite('Action_000_03', 6)	# 59-64	 **attackbox here**
    sprite('Action_000_04', 8)	# 65-72	 **attackbox here**
    sprite('Action_000_05', 5)	# 73-77	 **attackbox here**
    sprite('Action_000_06', 5)	# 78-82	 **attackbox here**
    sprite('Action_000_07', 5)	# 83-87	 **attackbox here**
    sprite('Action_000_08', 6)	# 88-93	 **attackbox here**
    sprite('Action_000_09', 5)	# 94-98	 **attackbox here**
    sprite('Action_000_10', 6)	# 99-104	 **attackbox here**
    sprite('Action_000_11', 8)	# 105-112	 **attackbox here**
    sprite('Action_000_12', 5)	# 113-117	 **attackbox here**
    sprite('Action_000_13', 5)	# 118-122	 **attackbox here**
    sprite('Action_000_14', 6)	# 123-128	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        callSubroutine('InsulatorInit')
    sprite('Action_222_17', 4)	# 1-4
    sprite('Action_222_18', 4)	# 5-8
    sprite('Action_222_19', 4)	# 9-12
    sprite('Action_222_20', 4)	# 13-16
    sprite('Action_222_21', 3)	# 17-19
    GFX_0('EffNmlAtk6CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_222_22ex', 2)	# 20-21	 **attackbox here**
    sprite('Action_222_23', 3)	# 22-24
    sprite('Action_222_24', 3)	# 25-27
    sprite('Action_222_23', 3)	# 28-30
    sprite('Action_222_24', 3)	# 31-33
    sprite('Action_222_23', 3)	# 34-36
    sprite('Action_222_24', 3)	# 37-39
    sprite('Action_222_25', 3)	# 40-42
    sprite('Action_222_26', 3)	# 43-45
    sprite('Action_222_27', 3)	# 46-48
    sprite('Action_222_28', 3)	# 49-51
    sprite('Action_222_29', 3)	# 52-54
    sprite('Action_222_30', 3)	# 55-57
    sprite('Action_222_31', 3)	# 58-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        callSubroutine('InsulatorInit')
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('Action_000_00', 7)	# 1-7	 **attackbox here**
    sprite('Action_000_01', 7)	# 8-14	 **attackbox here**
    sprite('Action_000_02', 6)	# 15-20	 **attackbox here**
    sprite('Action_000_03', 6)	# 21-26	 **attackbox here**
    sprite('Action_000_04', 8)	# 27-34	 **attackbox here**
    sprite('Action_000_05', 5)	# 35-39	 **attackbox here**
    sprite('Action_000_06', 5)	# 40-44	 **attackbox here**
    sprite('Action_000_07', 5)	# 45-49	 **attackbox here**
    sprite('Action_000_08', 6)	# 50-55	 **attackbox here**
    sprite('Action_000_09', 5)	# 56-60	 **attackbox here**
    sprite('Action_000_10', 6)	# 61-66	 **attackbox here**
    sprite('Action_000_11', 8)	# 67-74	 **attackbox here**
    sprite('Action_000_12', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_13', 5)	# 80-84	 **attackbox here**
    sprite('Action_000_14', 6)	# 85-90	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_222_17', 4)	# 91-94
    sprite('Action_222_18', 4)	# 95-98
    sprite('Action_222_19', 4)	# 99-102
    sprite('Action_222_20', 4)	# 103-106
    sprite('Action_222_21', 3)	# 107-109
    GFX_0('EffNmlAtk6CBlade', 100)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_222_22ex', 2)	# 110-111	 **attackbox here**
    sprite('Action_222_23', 3)	# 112-114
    sprite('Action_222_24', 3)	# 115-117
    sprite('Action_222_23', 3)	# 118-120
    sprite('Action_222_24', 3)	# 121-123
    sprite('Action_222_23', 3)	# 124-126
    sprite('Action_222_24', 3)	# 127-129
    sprite('Action_222_25', 3)	# 130-132
    sprite('Action_222_26', 3)	# 133-135
    sprite('Action_222_27', 3)	# 136-138
    sprite('Action_222_28', 3)	# 139-141
    sprite('Action_222_29', 3)	# 142-144
    sprite('Action_222_30', 3)	# 145-147
    sprite('Action_222_31', 3)	# 148-150

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
    sprite('Action_045_00', 6)	# 1-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 3)	# 10-12
    label(0)
    sprite('Action_045_03', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 16-18
    sprite('Action_045_05', 3)	# 19-21
    sprite('Action_045_06', 3)	# 22-24
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 25-27
    sprite('Action_045_08', 3)	# 28-30
    sprite('Action_045_09', 3)	# 31-33
    sprite('Action_045_02', 3)	# 34-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 37-39
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 40-42	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_01', 2)	# 43-44	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('Action_055_02', 2)	# 45-46
    sprite('Action_055_03', 3)	# 47-49
    SFX_4('uhy154')
    sprite('Action_055_04', 8)	# 50-57
    sprite('Action_055_05', 4)	# 58-61
    sprite('Action_055_06', 4)	# 62-65

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(30000)
        AirUntechableTime(60)
    sprite('Action_056_01', 8)	# 1-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 2)	# 9-10
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_01', 7)	# 11-17
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_02', 2)	# 18-19
    SFX_4('uhy153')
    SFX_0('004_swing_grap_1_2')
    sprite('Action_057_03', 6)	# 20-25	 **attackbox here**
    sprite('Action_057_04', 6)	# 26-31
    sprite('Action_057_05', 5)	# 32-36
    sprite('Action_057_06', 3)	# 37-39

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
    sprite('Action_045_00', 6)	# 1-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 3)	# 10-12
    label(0)
    sprite('Action_045_03', 3)	# 13-15
    Unknown8006(100, 1, 1)
    sprite('Action_045_04', 3)	# 16-18
    sprite('Action_045_05', 3)	# 19-21
    sprite('Action_045_06', 3)	# 22-24
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 25-27
    sprite('Action_045_08', 3)	# 28-30
    sprite('Action_045_09', 3)	# 31-33
    sprite('Action_045_02', 3)	# 34-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 37-39
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_056_00', 3)	# 40-42	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_056_01', 2)	# 43-44
    sprite('Action_055_02', 2)	# 45-46
    sprite('Action_055_03', 3)	# 47-49
    SFX_4('uhy154')
    sprite('Action_055_04', 8)	# 50-57
    sprite('Action_055_05', 4)	# 58-61
    sprite('Action_055_06', 4)	# 62-65

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(12000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown13021(1)
        Unknown21005(1)
    sprite('Action_056_01', 8)	# 1-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00ex', 2)	# 9-10
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('Action_057_01', 7)	# 11-17
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_057_02', 2)	# 18-19
    SFX_4('uhy153')
    SFX_0('004_swing_grap_1_2')
    sprite('Action_057_03', 6)	# 20-25	 **attackbox here**
    sprite('Action_057_04', 6)	# 26-31
    sprite('Action_057_05', 5)	# 32-36
    sprite('Action_057_06', 3)	# 37-39

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(680)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(35000)
        AirPushbackX(8000)
        AirUntechableTime(52)
        Unknown9266(11)
        Unknown11110(63)
        Unknown1084(0)
        sendToLabelUpon(2, 1)

        def upon_4():
            setGravity(1700)
    sprite('Action_270_00', 4)	# 1-4
    sprite('Action_270_01', 4)	# 5-8
    tag_voice(1, 'uhy200_0', 'uhy200_1', 'uhy200_2', '')
    sprite('Action_270_02', 1)	# 9-9	 **attackbox here**
    teleportRelativeX(-10000)
    StartMultihit()
    sprite('Action_270_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_270_03', 2)	# 13-14	 **attackbox here**
    Unknown8001(0, 100)
    Unknown9016(1)
    Unknown9266(11)
    GFX_0('EffNmlReversalAction', 100)
    physicsYImpulse(36000)
    physicsXImpulse(5120)
    setGravity(1500)
    teleportRelativeX(50000)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_270_03', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    callSubroutine('InsulatorSpecialInit')
    Hitstop(10)
    sprite('Action_270_06', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    Hitstop(3)
    sprite('Action_270_07', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_08', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_09', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_09', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_10', 2)	# 27-28
    RefreshMultihit()
    sprite('Action_270_11', 2)	# 29-30
    setInvincible(0)
    sprite('Action_270_12', 4)	# 31-34
    sprite('Action_270_13', 5)	# 35-39
    sprite('Action_270_14', 4)	# 40-43
    sprite('Action_270_15', 4)	# 44-47
    sprite('Action_270_16', 4)	# 48-51
    sprite('Action_270_17', 4)	# 52-55
    label(0)
    sprite('Action_020_00', 3)	# 56-58
    sprite('Action_020_01', 3)	# 59-61
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 5)	# 62-66
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_021_01', 7)	# 67-73
    sprite('Action_021_02', 4)	# 74-77
    Unknown18009(0)
    sprite('Action_021_03', 3)	# 78-80
    sprite('Action_021_04', 3)	# 81-83

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(680)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(48000)
        AirPushbackX(12000)
        AirUntechableTime(52)
        Hitstop(10)
        callSubroutine('InsulatorSpecialInit')
        Unknown1084(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)

        def upon_4():
            setGravity(2200)
    sprite('Action_270_00ex00', 3)	# 1-3
    sprite('Action_270_01ex00', 3)	# 4-6
    tag_voice(1, 'uhy200_0', 'uhy200_1', 'uhy200_2', '')
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_270_03', 2)	# 7-8	 **attackbox here**
    Unknown9016(1)
    GFX_0('EffNmlReversalAction', 100)
    physicsYImpulse(36000)
    physicsXImpulse(5120)
    setGravity(1500)
    teleportRelativeX(50000)
    Unknown1007(75000)
    sprite('Action_270_03', 2)	# 9-10	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_06', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    Hitstop(3)
    sprite('Action_270_07', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_08', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_09', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_09', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_270_10', 2)	# 21-22
    RefreshMultihit()
    sprite('Action_270_11', 2)	# 23-24
    setInvincible(0)
    sprite('Action_270_12', 4)	# 25-28
    sprite('Action_270_13', 5)	# 29-33
    sprite('Action_270_14', 4)	# 34-37
    sprite('Action_270_15', 4)	# 38-41
    sprite('Action_270_16', 4)	# 42-45
    sprite('Action_270_17', 4)	# 46-49
    label(0)
    sprite('Action_020_00', 3)	# 50-52
    sprite('Action_020_01', 3)	# 53-55
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 3)	# 56-58
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_021_01', 4)	# 59-62
    sprite('Action_021_02', 4)	# 63-66
    Unknown18009(0)
    sprite('Action_021_03', 3)	# 67-69
    sprite('Action_021_04', 3)	# 70-72

@State
def ShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        DisableAttackRestOfMove()

        def upon_14():
            SLOT_4 = 0
    sprite('Action_160_00', 4)	# 1-4
    sprite('Action_160_01', 4)	# 5-8
    sprite('Action_160_02', 2)	# 9-10
    sprite('Action_160_03', 1)	# 11-11
    SFX_3('SE045')
    Unknown14070('Shot_Explode')
    Unknown14070('Shot_SlashB')
    Unknown14070('Shot_SlashC')
    SLOT_4 = 1
    tag_voice(1, 'uhy201_0', 'uhy201_1', 'uhy201_2', '')
    GFX_0('ShotA', 0)
    Unknown38(4, 1)
    GFX_0('EffShotBlade', 100)
    sprite('Action_160_03', 2)	# 12-13
    Unknown14072('Shot_Explode')
    Unknown14072('Shot_SlashB')
    Unknown14072('Shot_SlashC')
    sprite('Action_160_04', 6)	# 14-19
    sprite('Action_160_05', 9)	# 20-28
    sprite('Action_160_06', 6)	# 29-34
    sprite('Action_160_07', 6)	# 35-40
    sprite('Action_160_08', 6)	# 41-46

@State
def ShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        DisableAttackRestOfMove()
        if SLOT_4:
            enterState('Shot_SlashB')
    sprite('Action_161_00', 3)	# 1-3
    sprite('Action_161_01', 3)	# 4-6
    sprite('Action_161_02', 2)	# 7-8
    sprite('Action_161_03', 1)	# 9-9
    SFX_3('SE045')
    Unknown14070('Shot_Explode')
    Unknown14070('Shot_SlashB')
    Unknown14070('Shot_SlashC')
    SLOT_4 = 1
    tag_voice(1, 'uhy201_0', 'uhy201_1', 'uhy201_2', '')
    GFX_0('ShotB', 0)
    Unknown38(4, 1)
    GFX_0('EffShotBlade', 100)
    sprite('Action_161_03', 2)	# 10-11
    Unknown14072('Shot_Explode')
    Unknown14072('Shot_SlashB')
    Unknown14072('Shot_SlashC')
    sprite('Action_161_04', 6)	# 12-17
    sprite('Action_161_05', 10)	# 18-27
    sprite('Action_161_06', 8)	# 28-35
    sprite('Action_161_07', 7)	# 36-42
    sprite('Action_161_08', 6)	# 43-48

@State
def Shot_Explode():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        DisableAttackRestOfMove()
        Unknown30068(1)
    sprite('Action_195_00', 3)	# 1-3
    sprite('Action_195_01', 3)	# 4-6
    Unknown23029(4, 20, 0)
    sprite('Action_195_02', 3)	# 7-9
    sprite('Action_195_03', 4)	# 10-13
    sprite('Action_195_04', 5)	# 14-18
    tag_voice(1, 'uhy202_0', 'uhy202_1', 'uhy202_2', '')
    sprite('Action_195_05', 5)	# 19-23
    sprite('Action_195_06', 6)	# 24-29
    GFX_0('UHY_Request_ExplodeBladeEffect', 100)
    teleportRelativeX(7000)
    Unknown1045(-15000)
    sprite('Action_195_07', 2)	# 30-31
    sprite('Action_195_08', 3)	# 32-34
    sprite('Action_195_09', 3)	# 35-37
    sprite('Action_195_08', 3)	# 38-40
    sprite('Action_195_09', 3)	# 41-43
    sprite('Action_195_08', 3)	# 44-46
    sprite('Action_195_09', 3)	# 47-49
    Unknown1019(80)
    sprite('Action_195_08', 3)	# 50-52
    Unknown1019(80)
    sprite('Action_195_09', 3)	# 53-55
    Unknown1019(80)
    sprite('Action_195_10', 4)	# 56-59
    Unknown1084(1)
    sprite('Action_195_11', 3)	# 60-62

@State
def Shot_SlashB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(23000)
        AirPushbackY(-32000)
        YImpluseBeforeWallbounce(800)
        PushbackX(19800)
        Unknown9310(1)
        AirUntechableTime(32)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('InsulatorSpecialInit')
        Unknown30068(1)
        sendToLabelUpon(2, 0)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_52:
                if SLOT_51:
                    Unknown2016(350)
                else:
                    Unknown2016(-1)
    sprite('Action_196_00', 3)	# 1-3
    sprite('Action_196_01', 3)	# 4-6
    sprite('Action_196_02', 2)	# 7-8
    SLOT_52 = 1
    Unknown8001(0, 100)
    physicsXImpulse(70000)
    physicsYImpulse(16000)
    setGravity(2300)
    sprite('Action_196_03', 5)	# 9-13
    sprite('Action_196_04', 3)	# 14-16
    sprite('Action_196_05', 3)	# 17-19
    tag_voice(1, 'uhy203_0', 'uhy203_1', 'uhy203_2', '')
    sprite('Action_196_06', 300)	# 20-319
    label(0)
    sprite('Action_196_07', 2)	# 320-321	 **attackbox here**
    Unknown1019(10)
    GFX_0('EffShotSlashBlade', 100)
    SFX_3('SE043')
    Unknown2016(-1)
    SLOT_52 = 0
    sprite('Action_196_08', 10)	# 322-331
    Unknown8000(100, 1, 1)
    Unknown1019(0)
    Recovery()
    sprite('Action_196_09', 7)	# 332-338
    sprite('Action_196_10', 5)	# 339-343
    sprite('Action_196_11', 5)	# 344-348
    sprite('Action_196_12', 4)	# 349-352

@Subroutine
def Assult_Init():
    AttackLevel_(4)
    AttackP1(80)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Unknown11056(2)
    callSubroutine('InsulatorSpecialInit')
    Unknown1084(1)
    clearUponHandler(2)

    def upon_LANDING():
        WhiffCancelEnable(0)
        Unknown14077(0)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(9)

@Subroutine
def Assult1st_Init():
    callSubroutine('Assult_Init')
    AirUntechableTime(24)
    HitOrBlockCancel('Assult_2nd')
    WhiffCancel('Assult_2nd')

@State
def AssultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assult1st_Init')
        Damage(1100)
        AirPushbackY(20000)
    sprite('Action_134_00', 5)	# 1-5
    sprite('Action_134_01', 4)	# 6-9
    SFX_0('002_highjump_0')
    Unknown8001(0, 100)
    physicsXImpulse(35000)
    physicsYImpulse(18000)
    setGravity(1200)
    Unknown1028(-500)
    sprite('Action_134_02', 3)	# 10-12
    sprite('Action_134_03', 2)	# 13-14
    Unknown1019(30)
    Unknown1028(0)
    tag_voice(1, 'uhy205_0', 'uhy205_1', 'uhy205_2', '')
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_134_04', 4)	# 15-18	 **attackbox here**
    GFX_0('EffAssult1st', 100)
    sprite('Action_134_05', 6)	# 19-24
    WhiffCancelEnable(1)
    Recovery()
    Unknown1043()
    sprite('Action_134_06', 2)	# 25-26
    sprite('Action_134_07', 2)	# 27-28
    sprite('Action_134_08', 2)	# 29-30
    sprite('Action_134_09', 2)	# 31-32
    sprite('Action_134_10', 2)	# 33-34
    label(0)
    sprite('Action_022_00', 3)	# 35-37
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('Action_022_01', 3)	# 38-40
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_023_00', 2)	# 41-42
    sprite('Action_023_01', 3)	# 43-45
    sprite('Action_023_02', 2)	# 46-47

@State
def AssultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        callSubroutine('Assult1st_Init')
        Damage(1300)
        AirPushbackY(20000)
    sprite('Action_134_00', 5)	# 1-5
    Unknown1084(1)
    sprite('Action_134_01', 4)	# 6-9
    SFX_0('002_highjump_0')
    Unknown8001(0, 100)
    physicsXImpulse(60000)
    physicsYImpulse(12000)
    setGravity(-1000)
    sprite('Action_134_02', 4)	# 10-13
    sprite('Action_134_03', 4)	# 14-17
    Unknown1019(20)
    Unknown1028(0)
    YAccel(80)
    tag_voice(1, 'uhy205_0', 'uhy205_1', 'uhy205_2', '')
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_134_04', 4)	# 18-21	 **attackbox here**
    GFX_0('EffAssult1st', 100)
    Unknown1019(50)
    Unknown1043()
    sprite('Action_134_05', 6)	# 22-27
    WhiffCancelEnable(1)
    Recovery()
    sprite('Action_134_06', 5)	# 28-32
    sprite('Action_134_07', 3)	# 33-35
    sprite('Action_134_08', 3)	# 36-38
    sprite('Action_134_09', 3)	# 39-41
    sprite('Action_134_10', 3)	# 42-44
    label(0)
    sprite('Action_022_00', 3)	# 45-47
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('Action_022_01', 3)	# 48-50
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_023_00', 2)	# 51-52
    sprite('Action_023_01', 3)	# 53-55
    sprite('Action_023_02', 2)	# 56-57
    sprite('Action_023_03', 2)	# 58-59

@State
def AirAssultA():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Assult1st_Init')
        Damage(1100)
        AirPushbackX(7000)
        AirPushbackY(22000)
    sprite('Action_134_01', 3)	# 1-3
    Unknown1045(0)
    physicsXImpulse(15000)
    physicsYImpulse(25000)
    setGravity(1000)
    Unknown1028(-250)
    sprite('Action_134_01', 3)	# 4-6
    sprite('Action_134_02', 3)	# 7-9
    sprite('Action_134_03', 2)	# 10-11
    tag_voice(1, 'uhy205_0', 'uhy205_1', 'uhy205_2', '')
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_134_04', 4)	# 12-15	 **attackbox here**
    GFX_0('EffAssult1st', 100)
    Unknown1019(50)
    Unknown1028(0)
    sprite('Action_134_05', 6)	# 16-21
    WhiffCancelEnable(1)
    Recovery()
    Unknown1043()
    sprite('Action_134_06', 5)	# 22-26
    sprite('Action_134_07', 3)	# 27-29
    sprite('Action_134_08', 3)	# 30-32
    sprite('Action_134_09', 3)	# 33-35
    sprite('Action_134_10', 3)	# 36-38
    label(0)
    sprite('Action_022_00', 3)	# 39-41
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('Action_022_01', 3)	# 42-44
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_023_00', 2)	# 45-46
    sprite('Action_023_01', 3)	# 47-49
    sprite('Action_023_02', 2)	# 50-51
    sprite('Action_023_03', 2)	# 52-53

@State
def AirAssultB():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Assult1st_Init')
        Damage(1300)
        AirPushbackX(15000)
        AirPushbackY(25000)
    sprite('Action_134_01', 3)	# 1-3
    Unknown1045(0)
    physicsXImpulse(20000)
    physicsYImpulse(31000)
    setGravity(1000)
    Unknown1028(-250)
    sprite('Action_134_01', 3)	# 4-6
    sprite('Action_134_02', 3)	# 7-9
    sprite('Action_134_03', 2)	# 10-11
    tag_voice(1, 'uhy205_0', 'uhy205_1', 'uhy205_2', '')
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_134_04', 4)	# 12-15	 **attackbox here**
    GFX_0('EffAssult1st', 100)
    Unknown1019(50)
    Unknown1028(0)
    sprite('Action_134_05', 6)	# 16-21
    WhiffCancelEnable(1)
    Recovery()
    Unknown1043()
    sprite('Action_134_06', 5)	# 22-26
    sprite('Action_134_07', 3)	# 27-29
    sprite('Action_134_08', 3)	# 30-32
    sprite('Action_134_09', 3)	# 33-35
    sprite('Action_134_10', 3)	# 36-38
    label(0)
    sprite('Action_022_00', 3)	# 39-41
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('Action_022_01', 3)	# 42-44
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_023_00', 2)	# 45-46
    sprite('Action_023_01', 3)	# 47-49
    sprite('Action_023_02', 2)	# 50-51
    sprite('Action_023_03', 2)	# 52-53

@State
def Assult_2nd():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Assult_Init')
        Damage(1100)
        AttackP1(64)
        AttackP2(100)
        AirUntechableTime(28)
        if Unknown23145('AssultB'):
            Damage(1300)
        if Unknown23145('AirAssultB'):
            Damage(1300)
        HitOrBlockCancel('Assult_3rd')
        WhiffCancel('Assult_3rd')
        Unknown30068(1)
    sprite('Action_134_14', 3)	# 1-3
    physicsXImpulse(9000)
    physicsYImpulse(15000)
    Unknown1043()
    Unknown23087(50000)
    sprite('Action_134_15', 3)	# 4-6
    sprite('Action_134_16', 2)	# 7-8
    sprite('Action_134_17', 2)	# 9-10
    sprite('Action_134_18', 2)	# 11-12
    GFX_0('EffAssult2nd', 100)
    tag_voice(0, 'uhy206_0', 'uhy206_1', 'uhy206_2', '')
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_134_19', 3)	# 13-15	 **attackbox here**
    sprite('Action_134_20', 6)	# 16-21
    WhiffCancelEnable(1)
    Unknown1043()
    Recovery()
    sprite('Action_134_21', 5)	# 22-26
    sprite('Action_134_22', 4)	# 27-30
    sprite('Action_134_23', 3)	# 31-33
    sprite('Action_134_24', 3)	# 34-36
    label(0)
    sprite('Action_022_00', 3)	# 37-39
    WhiffCancelEnable(0)
    Unknown14077(0)
    sprite('Action_022_01', 3)	# 40-42
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_023_00', 3)	# 43-45
    sprite('Action_023_01', 6)	# 46-51
    sprite('Action_023_02', 3)	# 52-54
    sprite('Action_023_03', 3)	# 55-57

@State
def Assult_3rd():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('Assult_Init')
        AttackP2(75)
        AirPushbackX(24000)
        AirPushbackY(-40000)
        AirUntechableTime(60)
        Unknown9310(15)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown30068(1)
    sprite('Action_134_26', 3)	# 1-3
    physicsXImpulse(9000)
    physicsYImpulse(18000)
    setGravity(1200)
    sprite('Action_134_27', 4)	# 4-7
    sprite('Action_134_28', 4)	# 8-11
    Unknown1019(50)
    sprite('Action_134_29', 3)	# 12-14
    tag_voice(0, 'uhy207_0', 'uhy207_1', 'uhy207_2', '')
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_134_30', 4)	# 15-18	 **attackbox here**
    GFX_0('EffAssult3rd', 100)
    sprite('Action_134_31', 4)	# 19-22
    Unknown1043()
    Recovery()
    sprite('Action_134_32', 4)	# 23-26
    sprite('Action_134_33', 3)	# 27-29
    sprite('Action_134_34', 3)	# 30-32
    Unknown1039(150)
    sprite('Action_134_35', 4)	# 33-36
    sprite('Action_134_36', 3)	# 37-39
    label(0)
    sprite('Action_022_00', 3)	# 40-42
    Unknown1039(110)
    sprite('Action_022_01', 3)	# 43-45
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('Action_023_00', 3)	# 46-48
    sprite('Action_023_01', 9)	# 49-57
    sprite('Action_023_02', 3)	# 58-60
    sprite('Action_023_03', 3)	# 61-63

@State
def AssultEX():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(5)
        Damage(800)
        AttackP1(80)
        Unknown30065(0)
        AirPushbackX(17000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        MinimumDamagePct(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11056(2)
        Unknown11064(1)
        Unknown30055('400d03003200000000000000')
        Unknown30056('20bf02003200000000000000')
        clearUponHandler(2)
        sendToLabelUpon(2, 12)

        def upon_12():
            Unknown2038(1)
            setInvincible(1)
        Unknown11044(1)
        Unknown11069('AssultEX')
    sprite('Action_136_00', 3)	# 1-3
    sprite('Action_136_01', 2)	# 4-5
    Unknown8001(0, 100)
    physicsXImpulse(45500)
    physicsYImpulse(15000)
    setGravity(0)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    SFX_3('SE043')
    sprite('Action_136_02', 2)	# 6-7	 **attackbox here**
    tag_voice(1, 'uhy208_0', 'uhy208_1', 'uhy208_2', '')
    Unknown1019(90)
    sprite('Action_136_03', 2)	# 8-9	 **attackbox here**
    Unknown1019(90)
    sprite('Action_136_04', 1)	# 10-10
    sprite('Action_136_04', 3)	# 11-13
    sprite('Action_136_05', 4)	# 14-17
    physicsXImpulse(8000)
    physicsYImpulse(13000)
    sprite('Action_136_06', 2)	# 18-19
    sprite('Action_136_07', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffAssult1st', 100)
    SFX_3('SE_InsulatorSwingB')
    Hitstop(8)
    AirPushbackX(10000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(2000)
    Unknown11001(0, 0, 0)
    callSubroutine('InsulatorSpecialInit')
    sprite('Action_136_08', 1)	# 22-22
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    sprite('Action_134_05', 6)	# 23-28
    Recovery()
    Unknown1043()
    sprite('Action_134_06', 5)	# 29-33
    sprite('Action_134_07', 3)	# 34-36
    sprite('Action_134_08', 3)	# 37-39
    sprite('Action_134_09', 3)	# 40-42
    sprite('Action_134_10', 3)	# 43-45
    label(0)
    sprite('Action_022_00', 3)	# 46-48
    sprite('Action_022_01', 3)	# 49-51
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_136_09', 1)	# 52-52
    sprite('Action_136_10', 1)	# 53-53
    sprite('Action_136_11', 1)	# 54-54
    sprite('Action_136_12', 1)	# 55-55
    sprite('Action_136_13', 1)	# 56-56
    GFX_0('EffAssult2nd', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_136_14', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_136_15', 2)	# 59-60
    sprite('Action_136_16', 1)	# 61-61
    sprite('Action_136_17', 2)	# 62-63
    sprite('Action_136_18', 2)	# 64-65
    sprite('Action_136_19', 2)	# 66-67	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffAssult3rd', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_136_20', 3)	# 68-70
    tag_voice(0, 'uhy209_0', 'uhy209_1', 'uhy209_2', '')
    sprite('Action_136_21', 2)	# 71-72
    sprite('Action_136_22', 2)	# 73-74
    sprite('Action_136_23', 1)	# 75-75
    sprite('Action_136_24', 1)	# 76-76
    sprite('Action_136_25', 1)	# 77-77
    GFX_0('EffAssult2nd', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_136_26', 2)	# 78-79	 **attackbox here**
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    sprite('Action_136_27', 3)	# 80-82
    sprite('Action_136_28', 2)	# 83-84
    sprite('Action_136_29', 4)	# 85-88
    physicsXImpulse(15000)
    physicsYImpulse(24000)
    sprite('Action_136_30', 8)	# 89-96
    setGravity(2400)
    sprite('Action_136_31', 4)	# 97-100
    sprite('Action_136_32', 2)	# 101-102
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_136_33', 4)	# 103-106	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    AirPushbackX(24000)
    AirPushbackY(-48000)
    AirUntechableTime(40)
    Hitstop(14)
    Unknown9310(15)
    Unknown9016(1)
    Unknown11064(0)
    GFX_0('EffAssult3rd', 100)
    Unknown11069('')
    Unknown11044(0)
    sprite('Action_136_34', 4)	# 107-110
    Recovery()
    setInvincible(0)
    sprite('Action_136_35', 4)	# 111-114
    sprite('Action_136_36', 3)	# 115-117
    label(10)
    sprite('Action_136_37', 3)	# 118-120
    sprite('Action_136_38', 4)	# 121-124
    label(11)
    sprite('Action_136_39', 3)	# 125-127
    sprite('Action_136_40', 3)	# 128-130
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('Action_138_00', 3)	# 131-133
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_138_01', 9)	# 134-142
    sprite('Action_138_02', 3)	# 143-145
    sprite('Action_138_03', 3)	# 146-148

@State
def AirAssultEX():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(5)
        Damage(800)
        AttackP1(80)
        Unknown30065(0)
        AirPushbackX(17000)
        AirPushbackY(35000)
        AirUntechableTime(60)
        MinimumDamagePct(10)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11056(2)
        Unknown11064(1)
        Unknown30055('400d03003200000000000000')
        Unknown30056('20bf02003200000000000000')
        clearUponHandler(2)
        sendToLabelUpon(2, 12)

        def upon_12():
            Unknown2038(1)
            setInvincible(1)
        Unknown11044(1)
        Unknown11069('AirAssultEX')
    sprite('Action_136_01', 3)	# 1-3
    Unknown1084(1)
    sprite('Action_136_01', 2)	# 4-5
    physicsXImpulse(39000)
    physicsYImpulse(20500)
    setGravity(0)
    Unknown1045(0)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    SFX_3('SE043')
    sprite('Action_136_02', 2)	# 6-7	 **attackbox here**
    tag_voice(1, 'uhy208_0', 'uhy208_1', 'uhy208_2', '')
    Unknown1019(90)
    sprite('Action_136_03', 2)	# 8-9	 **attackbox here**
    Unknown1019(90)
    sprite('Action_136_04', 1)	# 10-10
    sprite('Action_136_04', 3)	# 11-13
    sprite('Action_136_05', 4)	# 14-17
    physicsXImpulse(8000)
    physicsYImpulse(13000)
    sprite('Action_136_06', 2)	# 18-19
    sprite('Action_136_07', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffAssult1st', 100)
    SFX_3('SE_InsulatorSwingB')
    Hitstop(8)
    AirPushbackX(10000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(2000)
    Unknown11001(0, 0, 0)
    callSubroutine('InsulatorSpecialInit')
    sprite('Action_136_08', 1)	# 22-22
    loopRest()
    if SLOT_2:
        _gotolabel(1)
    sprite('Action_134_05', 6)	# 23-28
    Recovery()
    Unknown1043()
    sprite('Action_134_06', 5)	# 29-33
    sprite('Action_134_07', 3)	# 34-36
    sprite('Action_134_08', 3)	# 37-39
    sprite('Action_134_09', 3)	# 40-42
    sprite('Action_134_10', 3)	# 43-45
    label(0)
    sprite('Action_022_00', 3)	# 46-48
    sprite('Action_022_01', 3)	# 49-51
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_136_09', 1)	# 52-52
    sprite('Action_136_10', 1)	# 53-53
    sprite('Action_136_11', 1)	# 54-54
    sprite('Action_136_12', 1)	# 55-55
    sprite('Action_136_13', 1)	# 56-56
    GFX_0('EffAssult2nd', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_136_14', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('Action_136_15', 2)	# 59-60
    sprite('Action_136_16', 1)	# 61-61
    sprite('Action_136_17', 2)	# 62-63
    sprite('Action_136_18', 2)	# 64-65
    sprite('Action_136_19', 2)	# 66-67	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffAssult3rd', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_136_20', 3)	# 68-70
    tag_voice(0, 'uhy209_0', 'uhy209_1', 'uhy209_2', '')
    sprite('Action_136_21', 2)	# 71-72
    sprite('Action_136_22', 2)	# 73-74
    sprite('Action_136_23', 1)	# 75-75
    sprite('Action_136_24', 1)	# 76-76
    sprite('Action_136_25', 1)	# 77-77
    GFX_0('EffAssult2nd', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_136_26', 2)	# 78-79	 **attackbox here**
    RefreshMultihit()
    Unknown30055('000000000000000000000000')
    Unknown30056('000000000000000000000000')
    sprite('Action_136_27', 3)	# 80-82
    sprite('Action_136_28', 2)	# 83-84
    sprite('Action_136_29', 4)	# 85-88
    physicsXImpulse(15000)
    physicsYImpulse(24000)
    sprite('Action_136_30', 8)	# 89-96
    setGravity(2400)
    sprite('Action_136_31', 4)	# 97-100
    sprite('Action_136_32', 2)	# 101-102
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_136_33', 4)	# 103-106	 **attackbox here**
    RefreshMultihit()
    Damage(2000)
    AirPushbackX(24000)
    AirPushbackY(-48000)
    AirUntechableTime(40)
    Hitstop(14)
    Unknown9310(15)
    Unknown9016(1)
    Unknown11064(0)
    GFX_0('EffAssult3rd', 100)
    Unknown11069('')
    Unknown11044(0)
    sprite('Action_136_34', 4)	# 107-110
    Recovery()
    sprite('Action_136_35', 4)	# 111-114
    sprite('Action_136_36', 3)	# 115-117
    label(10)
    sprite('Action_136_37', 3)	# 118-120
    sprite('Action_136_38', 4)	# 121-124
    label(11)
    sprite('Action_136_39', 3)	# 125-127
    sprite('Action_136_40', 3)	# 128-130
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('Action_138_00', 3)	# 131-133
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_138_01', 9)	# 134-142
    sprite('Action_138_02', 3)	# 143-145
    sprite('Action_138_03', 3)	# 146-148

@State
def ShotEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        DisableAttackRestOfMove()

        def upon_14():
            SLOT_4 = 0
    sprite('Action_162_00', 2)	# 1-2
    sprite('Action_162_01', 1)	# 3-3
    sprite('Action_162_01', 2)	# 4-5
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('Action_162_02', 2)	# 6-7
    tag_voice(1, 'uhy204_0', 'uhy204_1', 'uhy204_2', '')
    sprite('Action_162_03', 3)	# 8-10
    SFX_3('SE045')
    SLOT_4 = 1
    SLOT_5 = 1
    GFX_0('ShotEx', 0)
    GFX_0('EffShotBlade', 100)
    Unknown38(4, 1)
    sprite('Action_162_04', 6)	# 11-16
    sprite('Action_160_05', 14)	# 17-30
    sprite('Action_160_06', 8)	# 31-38
    sprite('Action_160_07', 7)	# 39-45
    sprite('Action_160_08', 6)	# 46-51

@State
def Shot_SlashC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2500)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AttackP2(80)
        AirPushbackX(6000)
        AirPushbackY(-40000)
        YImpluseBeforeWallbounce(800)
        PushbackX(19800)
        Unknown9310(1)
        AirUntechableTime(50)
        Unknown9310(0)
        Unknown9190(1)
        Unknown9118(70)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown11058('0100000000000000000000000000000000000000')
        callSubroutine('InsulatorSpecialInit')
        setInvincible(1)
        Unknown22019('0000000000000000000000000100000000000000')
        Unknown30068(1)
        sendToLabelUpon(2, 0)

        def upon_CLEAR_OR_EXIT():
            Unknown48('19000000020000003300000016000000020000001e000000')
            if SLOT_52:
                if SLOT_51:
                    Unknown2016(350)
                else:
                    Unknown2016(-1)
    sprite('Action_196_00', 3)	# 1-3
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('Action_196_01', 3)	# 4-6
    sprite('Action_196_02', 2)	# 7-8
    SLOT_52 = 1
    Unknown8001(0, 100)
    physicsXImpulse(70000)
    physicsYImpulse(16000)
    setGravity(2300)
    sprite('Action_196_03', 5)	# 9-13
    sprite('Action_196_04', 3)	# 14-16
    sprite('Action_196_05', 3)	# 17-19
    tag_voice(1, 'uhy203_0', 'uhy203_1', 'uhy203_2', '')
    sprite('Action_196_06', 300)	# 20-319
    label(0)
    sprite('Action_196_07', 2)	# 320-321	 **attackbox here**
    Unknown1019(10)
    GFX_0('EffShotSlashBlade', 100)
    SFX_3('SE043')
    Unknown2016(-1)
    SLOT_52 = 0
    sprite('Action_196_08', 10)	# 322-331
    setInvincible(0)
    Unknown8000(100, 1, 1)
    Unknown1019(0)
    Recovery()
    sprite('Action_196_09', 3)	# 332-334
    sprite('Action_196_10', 3)	# 335-337
    sprite('Action_196_11', 3)	# 338-340
    sprite('Action_196_12', 4)	# 341-344

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        MinimumDamagePct(30)
        AttackP2(90)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(20000)
        PushbackX(4500)
        AirUntechableTime(40)
        Unknown30055('a08601006400000000000000')
        Unknown11064(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown9016(1)
        setInvincible(1)
        Unknown1084(1)
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 == 2):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('Action_200_00', 3)	# 1-3
    Unknown23024(1)
    Unknown2036(62, -1, 0)
    ConsumeSuperMeter(-10000)
    setInvincible(1)
    Unknown30080('')
    tag_voice(1, 'uhy250_0', 'uhy250_1', '', '')
    sprite('Action_200_01', 3)	# 4-6
    sprite('Action_200_02', 4)	# 7-10
    sprite('Action_200_03', 6)	# 11-16
    GFX_0('EffConcentration', 100)
    label(0)
    sprite('Action_200_04', 4)	# 17-20
    sprite('Action_200_05', 4)	# 21-24
    Unknown2038(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_200_06', 4)	# 25-28
    sprite('Action_200_04', 4)	# 29-32
    sprite('Action_200_05', 4)	# 33-36
    sprite('Action_200_06', 4)	# 37-40
    sprite('Action_210_00', 4)	# 41-44
    Unknown26('EffConcentration')
    sprite('Action_210_01', 5)	# 45-49
    GFX_0('EffIWBlade00', 0)
    sprite('Action_210_02', 8)	# 50-57
    sprite('Action_210_03', 10)	# 58-67
    sprite('Action_210_04', 5)	# 68-72	 **attackbox here**
    SFX_3('SE043')
    SFX_3('SE221')
    GFX_0('ObjIWMatome', 100)
    sprite('Action_210_05', 5)	# 73-77
    sprite('Action_210_08', 3)	# 78-80
    sprite('Action_210_06', 3)	# 81-83
    sprite('Action_210_07', 3)	# 84-86
    tag_voice(0, 'uhy251_0', 'uhy251_1', '', '')
    sprite('Action_210_08', 3)	# 87-89
    setInvincible(0)
    sprite('Action_210_07', 3)	# 90-92
    sprite('Action_210_08', 3)	# 93-95
    sprite('Action_210_09', 3)	# 96-98
    sprite('Action_210_07', 3)	# 99-101
    sprite('Action_210_08', 3)	# 102-104
    sprite('Action_210_09', 3)	# 105-107
    sprite('Action_210_07', 3)	# 108-110
    sprite('Action_210_08', 3)	# 111-113
    sprite('Action_211_00', 6)	# 114-119
    sprite('Action_211_01', 8)	# 120-127
    sprite('Action_211_02', 7)	# 128-134
    sprite('Action_211_03', 6)	# 135-140
    GFX_0('IWEndEff', -1)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_211_04', 7)	# 141-147
    sprite('Action_211_05', 18)	# 148-165
    sprite('Action_211_06', 5)	# 166-170

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        MinimumDamagePct(30)
        AttackP2(90)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(20000)
        PushbackX(4500)
        AirUntechableTime(40)
        Unknown30055('a08601006400000000000000')
        Unknown11064(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown9016(1)
        setInvincible(1)
        Unknown1084(1)
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 == 2):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('Action_200_00', 3)	# 1-3
    Unknown23024(1)
    Unknown2036(62, -1, 0)
    ConsumeSuperMeter(-10000)
    setInvincible(1)
    Unknown30080('')
    tag_voice(1, 'uhy250_0', 'uhy250_1', '', '')
    sprite('Action_200_01', 3)	# 4-6
    sprite('Action_200_02', 4)	# 7-10
    sprite('Action_200_03', 6)	# 11-16
    GFX_0('EffConcentration', 100)
    label(0)
    sprite('Action_200_04', 4)	# 17-20
    sprite('Action_200_05', 4)	# 21-24
    Unknown2038(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_200_06', 4)	# 25-28
    sprite('Action_200_04', 4)	# 29-32
    sprite('Action_200_05', 4)	# 33-36
    sprite('Action_200_06', 4)	# 37-40
    sprite('Action_210_00', 4)	# 41-44
    Unknown26('EffConcentration')
    sprite('Action_210_01', 5)	# 45-49
    GFX_0('EffIWBlade00', 0)
    sprite('Action_210_02', 8)	# 50-57
    sprite('Action_210_03', 10)	# 58-67
    sprite('Action_210_04', 5)	# 68-72	 **attackbox here**
    SFX_3('SE043')
    SFX_3('SE221')
    GFX_0('ObjIWMatomeOD', 100)
    sprite('Action_210_05', 5)	# 73-77
    sprite('Action_210_08', 3)	# 78-80
    sprite('Action_210_06', 3)	# 81-83
    sprite('Action_210_07', 3)	# 84-86
    tag_voice(0, 'uhy251_0', 'uhy251_1', '', '')
    sprite('Action_210_08', 3)	# 87-89
    setInvincible(0)
    sprite('Action_210_09', 3)	# 90-92
    sprite('Action_210_07', 3)	# 93-95
    sprite('Action_210_08', 3)	# 96-98
    sprite('Action_210_09', 3)	# 99-101
    sprite('Action_210_07', 3)	# 102-104
    sprite('Action_210_08', 3)	# 105-107
    sprite('Action_210_09', 3)	# 108-110
    sprite('Action_210_07', 3)	# 111-113
    sprite('Action_210_08', 3)	# 114-116
    sprite('Action_210_09', 3)	# 117-119
    sprite('Action_210_07', 3)	# 120-122
    sprite('Action_210_08', 3)	# 123-125
    sprite('Action_211_00', 6)	# 126-131
    sprite('Action_211_01', 8)	# 132-139
    sprite('Action_211_02', 7)	# 140-146
    sprite('Action_211_03', 6)	# 147-152
    GFX_0('IWEndEff', -1)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_211_04', 7)	# 153-159
    sprite('Action_211_05', 18)	# 160-177
    sprite('Action_211_06', 5)	# 178-182

@State
def UltimateBaleBringer():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown11072(1, 200000, 0)
        Unknown11056(0)
        Unknown11064(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown2073(1)
        Unknown2037(15)

        def upon_78():
            sendToLabel(0)
            Unknown20000(1)
            Unknown20009(900)
            Unknown13024(0)

        def upon_80():
            sendToLabel(100)
        sendToLabelUpon(2, 9)
    sprite('Action_262_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_262_01', 25)	# 6-30
    Unknown23024(1)
    Unknown2036(60, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    tag_voice(1, 'uhy254_0', 'uhy254_1', 'uhy254_2', 'uhy252_2')
    sprite('Action_262_02', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_03', 3)	# 40-42
    sprite('Action_262_04', 3)	# 43-45
    sprite('Action_262_03', 3)	# 46-48
    sprite('Action_262_04', 3)	# 49-51
    sprite('Action_262_03', 3)	# 52-54
    sprite('Action_262_04', 3)	# 55-57
    sprite('Action_262_05', 5)	# 58-62
    sprite('Action_276_00', 4)	# 63-66
    sprite('Action_276_01', 2)	# 67-68
    tag_voice(0, 'uhy252_0', 'uhy252_1', 'uhy252_0', '')
    sprite('Action_276_02', 15)	# 69-83	 **attackbox here**
    SFX_3('SE038')
    physicsXImpulse(60000)
    Unknown1028(1000)
    Unknown8006(100, 1, 0)
    GFX_0('EffTagAssistBlade00', 100)
    label(100)
    sprite('Action_276_03', 5)	# 84-88
    physicsXImpulse(40000)
    Unknown1028(0)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    clearUponHandler(80)
    sprite('Action_276_04', 5)	# 89-93	 **attackbox here**
    RefreshMultihit()
    AttackP2(60)
    Unknown11092(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(8)
    Unknown11072(0, 0, 0)
    Unknown11064(0)
    Unknown2073(0)
    Unknown1084(1)
    setInvincible(0)
    sprite('Action_276_05', 2)	# 94-95
    GFX_0('EffTagAssistBlade01', 100)
    physicsXImpulse(8000)
    physicsYImpulse(46000)
    setGravity(2200)
    SFX_0('002_highjump_0')
    sprite('Action_276_06', 2)	# 96-97	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(30000)
    AirPushbackX(3000)
    Hitstop(0)
    Unknown1019(90)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_276_07', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 100-101
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_07', 2)	# 102-103	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 104-105
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_07', 2)	# 106-107	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 108-109
    RefreshMultihit()
    sprite('Action_276_11', 2)	# 110-111
    sprite('Action_276_12', 5)	# 112-116
    sprite('Action_276_13', 4)	# 117-120
    sprite('Action_276_14', 4)	# 121-124
    sprite('Action_276_15', 4)	# 125-128
    sprite('Action_276_16', 3)	# 129-131
    sprite('Action_276_17', 3)	# 132-134
    sprite('Action_276_18', 32767)	# 135-32901
    label(109)
    sprite('Action_138_00', 3)	# 32902-32904
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_138_01', 8)	# 32905-32912
    sprite('Action_138_02', 4)	# 32913-32916
    sprite('Action_138_03', 3)	# 32917-32919
    sprite('Action_138_04', 3)	# 32920-32922
    ExitState()
    label(0)
    sprite('Action_276_02', 4)	# 32923-32926	 **attackbox here**
    clearUponHandler(78)
    clearUponHandler(80)
    physicsXImpulse(90000)
    RefreshMultihit()
    Damage(50)
    PushbackX(60000)
    Hitstop(0)
    Unknown11057(800)
    Unknown30048(1)
    Unknown11023(1)
    Unknown11072(0, 0, 0)
    Unknown2038(-1)
    MinimumDamagePct(23)
    sprite('Action_276_02', 1)	# 32927-32927	 **attackbox here**
    if SLOT_2:
        if (SLOT_25 < 300000):
            sendToLabel(1)
        else:
            sendToLabel(0)
    else:
        sendToLabel(1)
    loopRest()
    label(1)
    sprite('Action_276_03', 5)	# 32928-32932
    clearUponHandler(78)
    physicsXImpulse(40000)
    Unknown1028(0)
    Unknown20009(1000)
    sprite('Action_276_04', 5)	# 32933-32937	 **attackbox here**
    RefreshMultihit()
    Damage(960)
    MinimumDamagePct(20)
    AttackP2(60)
    Unknown11092(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(20)
    Unknown9215()
    sprite('Action_276_05', 2)	# 32938-32939
    physicsXImpulse(4000)
    Unknown1028(-100)
    physicsYImpulse(54000)
    Unknown1043()
    SFX_0('002_highjump_0')
    sprite('Action_276_06', 2)	# 32940-32941	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(30000)
    AirPushbackX(3000)
    Hitstop(0)
    SFX_3('SE_InsulatorSwingC')
    GFX_0('EffTagAssistBlade02', 100)
    sprite('Action_276_07', 2)	# 32942-32943	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 2)	# 32944-32945
    sprite('Action_276_07', 2)	# 32946-32947	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 2)	# 32948-32949
    sprite('Action_276_07', 2)	# 32950-32951	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 2)	# 32952-32953
    sprite('Action_276_07', 2)	# 32954-32955	 **attackbox here**
    RefreshMultihit()
    tag_voice(0, 'uhy253_0', 'uhy253_1', 'uhy253_0', 'uhy253_2')
    sprite('Action_276_08', 2)	# 32956-32957
    sprite('Action_276_07', 2)	# 32958-32959	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 2)	# 32960-32961
    sprite('Action_276_07', 2)	# 32962-32963	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    Unknown9310(1)
    Unknown11064(0)
    sprite('Action_276_08', 2)	# 32964-32965
    Unknown13024(1)
    sprite('Action_276_11', 2)	# 32966-32967
    sprite('Action_276_12', 5)	# 32968-32972
    sprite('Action_276_13', 4)	# 32973-32976
    sprite('Action_276_14', 4)	# 32977-32980
    sprite('Action_276_15', 4)	# 32981-32984
    sprite('Action_276_16', 3)	# 32985-32987
    sprite('Action_276_17', 3)	# 32988-32990
    sprite('Action_276_18', 32767)	# 32991-65757
    label(9)
    sprite('Action_138_00', 3)	# 65758-65760
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_138_01', 16)	# 65761-65776
    sprite('Action_138_02', 4)	# 65777-65780
    sprite('Action_138_03', 3)	# 65781-65783
    sprite('Action_138_04', 3)	# 65784-65786

@State
def UltimateBaleBringerOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown11072(1, 200000, 0)
        Unknown11056(0)
        Unknown11064(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown2073(1)
        Unknown2037(15)

        def upon_78():
            sendToLabel(0)
            Unknown20000(1)
            Unknown20009(900)
            Unknown13024(0)

        def upon_80():
            sendToLabel(100)
        sendToLabelUpon(2, 9)
    sprite('Action_262_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_262_01', 25)	# 6-30
    Unknown23024(1)
    Unknown2036(60, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    tag_voice(1, 'uhy254_0', 'uhy254_1', 'uhy254_2', 'uhy252_2')
    sprite('Action_262_02', 3)	# 31-33
    sprite('Action_262_03', 3)	# 34-36
    sprite('Action_262_04', 3)	# 37-39
    sprite('Action_262_03', 3)	# 40-42
    sprite('Action_262_04', 3)	# 43-45
    sprite('Action_262_03', 3)	# 46-48
    sprite('Action_262_04', 3)	# 49-51
    sprite('Action_262_03', 3)	# 52-54
    sprite('Action_262_04', 3)	# 55-57
    sprite('Action_262_05', 5)	# 58-62
    sprite('Action_276_00', 4)	# 63-66
    sprite('Action_276_01', 2)	# 67-68
    tag_voice(0, 'uhy252_0', 'uhy252_1', 'uhy252_0', '')
    sprite('Action_276_02', 15)	# 69-83	 **attackbox here**
    SFX_3('SE038')
    physicsXImpulse(60000)
    Unknown1028(1000)
    Unknown8006(100, 1, 0)
    GFX_0('EffTagAssistBlade00', 100)
    label(100)
    sprite('Action_276_03', 5)	# 84-88
    physicsXImpulse(40000)
    Unknown1028(0)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    clearUponHandler(80)
    sprite('Action_276_04', 5)	# 89-93	 **attackbox here**
    RefreshMultihit()
    AttackP2(60)
    Unknown11092(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(8)
    Unknown11072(0, 0, 0)
    Unknown11064(0)
    Unknown2073(0)
    Unknown1084(1)
    setInvincible(0)
    sprite('Action_276_05', 2)	# 94-95
    GFX_0('EffTagAssistBlade01', 100)
    physicsXImpulse(8000)
    physicsYImpulse(46000)
    setGravity(2200)
    SFX_0('002_highjump_0')
    sprite('Action_276_06', 2)	# 96-97	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(30000)
    AirPushbackX(3000)
    Hitstop(0)
    Unknown1019(90)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_276_07', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 100-101
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_07', 2)	# 102-103	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 104-105
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_07', 2)	# 106-107	 **attackbox here**
    RefreshMultihit()
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 108-109
    RefreshMultihit()
    sprite('Action_276_11', 2)	# 110-111
    sprite('Action_276_12', 5)	# 112-116
    sprite('Action_276_13', 4)	# 117-120
    sprite('Action_276_14', 4)	# 121-124
    sprite('Action_276_15', 4)	# 125-128
    sprite('Action_276_16', 3)	# 129-131
    sprite('Action_276_17', 3)	# 132-134
    sprite('Action_276_18', 32767)	# 135-32901
    label(109)
    sprite('Action_138_00', 3)	# 32902-32904
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_138_01', 8)	# 32905-32912
    sprite('Action_138_02', 4)	# 32913-32916
    sprite('Action_138_03', 3)	# 32917-32919
    sprite('Action_138_04', 3)	# 32920-32922
    ExitState()
    label(0)
    sprite('Action_276_02', 4)	# 32923-32926	 **attackbox here**
    clearUponHandler(78)
    clearUponHandler(80)
    physicsXImpulse(90000)
    RefreshMultihit()
    Damage(50)
    AttackP2(100)
    PushbackX(60000)
    Hitstop(0)
    Unknown11057(800)
    MinimumDamagePct(21)
    Unknown30048(1)
    Unknown11023(1)
    Unknown11072(0, 0, 0)
    Unknown2038(-1)
    sprite('Action_276_02', 1)	# 32927-32927	 **attackbox here**
    if SLOT_2:
        if (SLOT_25 < 300000):
            sendToLabel(1)
        else:
            sendToLabel(0)
    else:
        sendToLabel(1)
    loopRest()
    label(1)
    sprite('Action_276_03', 5)	# 32928-32932
    clearUponHandler(78)
    physicsXImpulse(40000)
    Unknown1028(0)
    Unknown20009(1000)
    sprite('Action_276_04', 5)	# 32933-32937	 **attackbox here**
    RefreshMultihit()
    Damage(600)
    MinimumDamagePct(17)
    AttackP2(60)
    Unknown11092(1)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    Hitstop(20)
    Unknown9215()
    sprite('Action_276_05', 2)	# 32938-32939
    physicsXImpulse(4000)
    Unknown1028(-100)
    physicsYImpulse(54000)
    Unknown1043()
    SFX_0('002_highjump_0')
    sprite('Action_276_06', 2)	# 32940-32941	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(36000)
    AirPushbackX(3000)
    Hitstop(0)
    SFX_3('SE_InsulatorSwingC')
    GFX_0('EffTagAssistBlade02', 100)
    sprite('Action_276_07', 1)	# 32942-32942	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32943-32943
    sprite('Action_276_07', 1)	# 32944-32944	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32945-32945
    sprite('Action_276_07', 1)	# 32946-32946	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32947-32947
    sprite('Action_276_07', 1)	# 32948-32948	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32949-32949
    sprite('Action_276_07', 1)	# 32950-32950	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32951-32951
    sprite('Action_276_07', 1)	# 32952-32952	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32953-32953
    sprite('Action_276_07', 1)	# 32954-32954	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32955-32955
    sprite('Action_276_07', 1)	# 32956-32956	 **attackbox here**
    RefreshMultihit()
    tag_voice(0, 'uhy253_0', 'uhy253_1', 'uhy253_0', 'uhy253_2')
    sprite('Action_276_08', 1)	# 32957-32957
    sprite('Action_276_07', 1)	# 32958-32958	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32959-32959
    sprite('Action_276_07', 1)	# 32960-32960	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32961-32961
    sprite('Action_276_07', 1)	# 32962-32962	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32963-32963
    sprite('Action_276_07', 1)	# 32964-32964	 **attackbox here**
    RefreshMultihit()
    sprite('Action_276_08', 1)	# 32965-32965
    sprite('Action_276_20', 5)	# 32966-32970
    Unknown1084(1)
    clearUponHandler(3)
    Unknown20009(800)
    sprite('Action_276_21', 6)	# 32971-32976
    sprite('Action_276_22', 2)	# 32977-32978
    SFX_3('SE043')
    sprite('Action_276_23', 3)	# 32979-32981	 **attackbox here**
    RefreshMultihit()
    Damage(2150)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    AirPushbackY(-60000)
    YImpluseBeforeWallbounce(0)
    Unknown9190(1)
    Unknown9118(30)
    Hitstop(20)
    Unknown9310(1)
    Unknown9016(0)
    Unknown11057(1000)
    Unknown11050('010000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11064(0)
    Unknown13024(1)
    sprite('Action_276_24', 10)	# 32982-32991
    physicsXImpulse(-1000)
    setGravity(1500)
    Unknown20000(0)
    Unknown20009(1000)
    sprite('Action_276_25', 2)	# 32992-32993
    sprite('Action_276_26', 4)	# 32994-32997
    sprite('Action_276_27', 5)	# 32998-33002
    label(51)
    sprite('Action_276_28', 3)	# 33003-33005
    sprite('Action_276_29', 3)	# 33006-33008
    loopRest()
    gotoLabel(51)
    label(9)
    sprite('Action_138_00', 3)	# 33009-33011
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_138_01', 12)	# 33012-33023
    sprite('Action_138_02', 4)	# 33024-33027
    sprite('Action_138_03', 3)	# 33028-33030
    sprite('Action_138_04', 3)	# 33031-33033

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(2000)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9130(999)
        Unknown9142(999)
        AirPushbackX(0)
        AirPushbackY(1)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(999)
        Unknown11072(1, 800000, 0)
        Unknown11067(1)
        Unknown9016(1)
        Unknown11057(0)
        Unknown9266(11)
        Unknown11050('020000004879645f35303300000000000000000000000000000000000000000000000000')
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11058('0000000000000000000000000100000000000000')

        def upon_78():
            PushbackX(0)
            GFX_0('Hyd_361', 100)
            clearUponHandler(78)
            setInvincible(1)
            Unknown23088(1, 1)
            Unknown23157(1)
            EnableCollision(0)
            Unknown2053(0)
            Unknown2034(0)
            Unknown23084(1)
            Unknown20003(1)
            Unknown20004(1)
            SFX_3('SE_BombInsulator')
            sendToLabel(100)
        setInvincible(1)
    sprite('Action_261_00', 5)	# 1-5
    Unknown2036(90, -1, 1)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    SFX_1('uhy290')
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_261_01', 5)	# 6-10
    sprite('Action_261_02', 5)	# 11-15
    sprite('Action_261_03', 5)	# 16-20
    sprite('Action_261_04', 4)	# 21-24
    GFX_0('Hyd_999', 100)
    sprite('Action_261_05', 4)	# 25-28
    sprite('Action_261_07', 4)	# 29-32
    sprite('Action_261_04', 4)	# 33-36
    sprite('Action_261_05', 4)	# 37-40
    sprite('Action_261_07', 4)	# 41-44
    sprite('Action_261_04', 4)	# 45-48
    sprite('Action_261_05', 4)	# 49-52
    sprite('Action_261_07', 4)	# 53-56
    sprite('Action_261_04', 4)	# 57-60
    sprite('Action_261_05', 4)	# 61-64
    sprite('Action_261_07', 4)	# 65-68
    sprite('Action_261_04', 4)	# 69-72
    sprite('Action_261_05', 4)	# 73-76
    sprite('Action_261_11', 4)	# 77-80
    sprite('Action_261_12', 4)	# 81-84
    sprite('Action_195_00', 5)	# 85-89
    sprite('Action_195_01', 5)	# 90-94
    sprite('Action_195_02', 5)	# 95-99
    SFX_1('uhy291')
    sprite('Action_195_03', 5)	# 100-104
    sprite('Action_195_04', 5)	# 105-109
    sprite('Action_195_05ex00', 2)	# 110-111	 **attackbox here**
    GFX_0('Hyd_360', 100)
    sprite('Action_195_05ex01', 2)	# 112-113	 **attackbox here**
    sprite('Action_195_05ex02', 2)	# 114-115	 **attackbox here**
    sprite('Action_195_06', 6)	# 116-121
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    setInvincible(0)
    sprite('Action_195_07', 2)	# 122-123
    sprite('Action_195_08', 3)	# 124-126
    sprite('Action_195_09', 3)	# 127-129
    sprite('Action_195_08', 3)	# 130-132
    sprite('Action_195_09', 3)	# 133-135
    sprite('Action_195_08', 3)	# 136-138
    sprite('Action_195_09', 3)	# 139-141
    Unknown1019(80)
    sprite('Action_195_08', 3)	# 142-144
    Unknown1019(80)
    sprite('Action_195_09', 3)	# 145-147
    Unknown1019(80)
    sprite('Action_195_10', 4)	# 148-151
    Unknown1084(1)
    sprite('Action_195_11', 3)	# 152-154
    ExitState()
    label(100)
    sprite('Action_195_05', 5)	# 155-159
    GFX_0('Astral_Camera', 100)
    sprite('Action_195_06', 6)	# 160-165
    sprite('Action_195_07', 2)	# 166-167
    sprite('Action_195_08', 3)	# 168-170
    sprite('Action_195_09', 3)	# 171-173
    sprite('Action_195_08', 3)	# 174-176
    sprite('Action_195_09', 3)	# 177-179
    sprite('Action_195_08', 3)	# 180-182
    sprite('Action_195_09', 3)	# 183-185
    sprite('Action_195_08', 3)	# 186-188
    sprite('Action_195_09', 3)	# 189-191
    sprite('Action_195_10', 4)	# 192-195
    sprite('Action_365_00', 5)	# 196-200	 **attackbox here**
    Unknown21012('41737472616c5f43616d6572610000000000000000000000000000000000000020000000')
    sprite('Action_365_01', 5)	# 201-205	 **attackbox here**
    sprite('Action_365_02', 5)	# 206-210	 **attackbox here**
    sprite('Action_365_03', 7)	# 211-217	 **attackbox here**
    SFX_1('uhy292')
    sprite('Action_365_04', 7)	# 218-224	 **attackbox here**
    SFX_3('SE_ChargeUp')
    sprite('Action_365_05', 7)	# 225-231	 **attackbox here**
    sprite('Action_365_06', 7)	# 232-238	 **attackbox here**
    sprite('Action_365_04', 7)	# 239-245	 **attackbox here**
    sprite('Action_365_05', 7)	# 246-252	 **attackbox here**
    sprite('Action_365_06', 7)	# 253-259	 **attackbox here**
    sprite('Action_365_04', 7)	# 260-266	 **attackbox here**
    sprite('Action_365_05', 7)	# 267-273	 **attackbox here**
    sprite('Action_365_06', 7)	# 274-280	 **attackbox here**
    sprite('Action_365_04', 7)	# 281-287	 **attackbox here**
    sprite('Action_365_05', 7)	# 288-294	 **attackbox here**
    sprite('Action_365_06', 7)	# 295-301	 **attackbox here**
    sprite('Action_365_13', 6)	# 302-307	 **attackbox here**
    sprite('Action_365_14', 3)	# 308-310	 **attackbox here**
    SFX_3('SE_BombSlash')
    SFX_1('uhy292b')
    GFX_0('Hyd_362', 100)
    Unknown21012('41737472616c5f43616d6572610000000000000000000000000000000000000021000000')
    RefreshMultihit()
    Damage(1000)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    Unknown11072(3, 0, 200000)
    Unknown11023(1)
    Unknown9016(1)

    def upon_78():
        ScreenShake(8000, 8000)
    sprite('Action_365_15', 4)	# 311-314	 **attackbox here**
    sprite('Action_365_16', 3)	# 315-317	 **attackbox here**
    sprite('Action_365_17', 2)	# 318-319	 **attackbox here**
    SFX_3('SE_SpecialBombLong')
    RefreshMultihit()
    Hitstop(0)
    Unknown11072(3, 10000, 10000)
    sprite('Action_365_18', 2)	# 320-321	 **attackbox here**
    sprite('Action_365_19', 2)	# 322-323	 **attackbox here**
    Unknown2037(20)
    label(101)
    sprite('Action_365_17', 2)	# 324-325	 **attackbox here**
    RefreshMultihit()
    sprite('Action_365_18', 2)	# 326-327	 **attackbox here**
    sprite('Action_365_19', 2)	# 328-329	 **attackbox here**
    loopRest()
    if SLOT_2:
        Unknown2038(-1)
        gotoLabel(101)
    else:
        gotoLabel(102)
    label(102)
    sprite('Action_365_20', 120)	# 330-449	 **attackbox here**
    SFX_3('SE_BigBomb')
    RefreshMultihit()
    Damage(17000)
    AirPushbackY(30000)
    AirPushbackX(30000)
    Unknown11064(3)
    Unknown30058('')
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_365_21', 3)	# 450-452	 **attackbox here**
    sprite('Action_365_22', 3)	# 453-455	 **attackbox here**
    sprite('Action_365_23', 3)	# 456-458	 **attackbox here**
    sprite('Action_365_24', 3)	# 459-461
    enterState('AstralHeatEnd')

@State
def AstralHeatEnd():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown20000(1)
        Unknown1000(0)
        Unknown23024(0)
    sprite('Action_366_00', 5)	# 1-5
    sprite('Action_366_01', 5)	# 6-10
    SFX_1('uhy293')
    sprite('Action_366_02', 8)	# 11-18
    sprite('Action_366_03', 5)	# 19-23
    sprite('Action_366_04', 15)	# 24-38
    sprite('Action_366_05', 5)	# 39-43
    sprite('Action_366_06', 12)	# 44-55
    sprite('Action_366_07', 5)	# 56-60
    sprite('Action_366_04', 15)	# 61-75
    sprite('Action_366_05', 5)	# 76-80
    sprite('Action_366_06', 12)	# 81-92
    sprite('Action_366_07', 5)	# 93-97
    sprite('Action_366_04', 17)	# 98-114
    sprite('Action_366_05', 6)	# 115-120
    sprite('Action_366_06', 14)	# 121-134
    sprite('Action_366_07', 6)	# 135-140
    sprite('Action_366_08', 13)	# 141-153
    sprite('Action_366_09', 5)	# 154-158
    sprite('Action_366_10', 4)	# 159-162
    sprite('Action_366_11', 3)	# 163-165

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
    if SLOT_ReturnVal:
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
    sprite('Action_046_01', 3)	# 7-9
    sprite('Action_046_02', 3)	# 10-12
    sprite('Action_046_01', 3)	# 13-15
    sprite('Action_046_02', 3)	# 16-18
    sprite('Action_046_01', 3)	# 19-21
    sprite('Action_046_02', 3)	# 22-24
    sprite('Action_046_01', 3)	# 25-27
    sprite('Action_046_02', 3)	# 28-30
    sprite('Action_046_01', 30)	# 31-60

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_000_19', 4)	# 1-4
    Unknown1084(1)
    Unknown2034(0)
    EnableCollision(0)
    Unknown2053(0)
    Unknown4045('65665f62626f5f636972636c653032000000000000000000000000000000000067000000')
    sprite('Action_000_20', 8)	# 5-12
    sprite('Action_000_21', 11)	# 13-23
    label(1)
    sprite('Action_000_22', 5)	# 24-28	 **attackbox here**
    Unknown30042(24)
    if SLOT_ReturnVal:
        _gotolabel(2)
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('Action_000_23', 12)	# 29-40	 **attackbox here**
    sprite('Action_000_24', 6)	# 41-46	 **attackbox here**

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_000_19', 7)	# 1-7
    sprite('Action_000_20', 8)	# 8-15
    sprite('Action_000_21', 11)	# 16-26
    sprite('Action_000_22', 8)	# 27-34	 **attackbox here**
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffEntryBlade01', 100)
    sprite('Action_000_23', 36)	# 35-70	 **attackbox here**
    sprite('Action_000_24', 6)	# 71-76	 **attackbox here**

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
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
    sprite('null', 28)	# 603-630
    sprite('Action_276_22', 2)	# 631-632
    Unknown1086(22)
    teleportRelativeX(-300000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    physicsXImpulse(300000)
    physicsYImpulse(-200000)
    setGravity(0)
    sprite('Action_276_23', 32767)	# 633-33399	 **attackbox here**
    label(9)
    sprite('Action_276_23', 3)	# 33400-33402	 **attackbox here**
    Unknown1019(30)
    sprite('Action_021_00', 3)	# 33403-33405
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_021_01', 12)	# 33406-33417
    sprite('Action_021_02', 4)	# 33418-33421
    sprite('Action_021_03', 3)	# 33422-33424

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_03', 2)	# 1-2
    sprite('Action_312_04', 26)	# 3-28
    sprite('Action_312_05', 4)	# 29-32
    sprite('Action_312_06', 4)	# 33-36
    sprite('Action_312_07', 4)	# 37-40
    sprite('Action_312_08', 4)	# 41-44
    sprite('Action_014_00', 4)	# 45-48
    sprite('Action_014_01', 4)	# 49-52
    sprite('Action_014_02', 4)	# 53-56
    sprite('Action_014_03', 4)	# 57-60
    sprite('Action_000_00', 30)	# 61-90	 **attackbox here**

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_03', 3)	# 1-3
    sprite('Action_045_04', 5)	# 4-8
    sprite('Action_045_05', 7)	# 9-15
    sprite('Action_045_12', 7)	# 16-22
    sprite('Action_045_13', 7)	# 23-29

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
    sprite('Action_022_00', 4)	# 3-6
    Unknown1019(95)
    sprite('Action_022_01', 4)	# 7-10
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
        DisableAttackRestOfMove()

        def upon_14():
            SLOT_4 = 0
    sprite('Action_162_00', 3)	# 1-3
    sprite('Action_162_01', 3)	# 4-6
    sprite('Action_162_02', 3)	# 7-9
    tag_voice(1, 'uhy204_0', 'uhy204_1', 'uhy204_2', '')
    sprite('Action_162_03', 3)	# 10-12
    SFX_3('SE045')
    GFX_0('ShotEx_Assist', 0)
    GFX_0('EffShotBlade', 100)
    Unknown38(4, 1)
    sprite('Action_162_04', 6)	# 13-18
    sprite('Action_160_05', 14)	# 19-32
    sprite('Action_160_06', 8)	# 33-40
    sprite('Action_160_07', 7)	# 41-47
    sprite('Action_160_08', 6)	# 48-53

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        DisableAttackRestOfMove()
        Unknown30068(1)
    sprite('Action_195_00', 3)	# 1-3
    sprite('Action_195_01', 2)	# 4-5
    GFX_0('UHY_Request_ShotExplodeASS', 100)
    Unknown36(1)
    teleportRelativeX(100000)
    Unknown1007(250000)
    Unknown35()
    sprite('Action_195_02', 2)	# 6-7
    sprite('Action_195_03', 3)	# 8-10
    sprite('Action_195_04', 4)	# 11-14
    tag_voice(1, 'uhy202_0', 'uhy202_1', 'uhy202_2', '')
    sprite('Action_195_05', 3)	# 15-17
    sprite('Action_195_06', 6)	# 18-23
    GFX_0('UHY_Request_ExplodeBladeEffect', 100)
    teleportRelativeX(7000)
    Unknown1045(-15000)
    sprite('Action_195_07', 2)	# 24-25
    sprite('Action_195_08', 3)	# 26-28
    sprite('Action_195_09', 3)	# 29-31
    sprite('Action_195_08', 3)	# 32-34
    sprite('Action_195_09', 4)	# 35-38
    sprite('Action_195_08', 4)	# 39-42
    sprite('Action_195_09', 4)	# 43-46
    Unknown1019(80)
    sprite('Action_195_08', 4)	# 47-50
    Unknown1019(80)
    sprite('Action_195_09', 4)	# 51-54
    Unknown1019(80)
    sprite('Action_195_10', 5)	# 55-59
    Unknown1084(1)
    sprite('Action_195_11', 4)	# 60-63

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        AirUntechableTime(40)
        GroundedHitstunAnimation(10)
        PushbackX(19800)
        Unknown9016(1)
        Unknown1084(1)
        Unknown11056(2)
        Unknown11042(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown2006()

        def upon_11():
            sendToLabel(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('keep', 1)	# 1-1
    sprite('Action_276_00', 6)	# 2-7
    Unknown8000(100, 1, 1)
    EnableCollision(1)
    Unknown2053(1)
    Unknown2034(1)
    sprite('Action_276_01', 3)	# 8-10
    physicsXImpulse(60000)
    Unknown8006(100, 1, 0)
    Unknown7006('uhy214_0', 100, 846817397, 828322865, 0, 0, 100, 846817397, 811545905, 0, 0, 100, 846817397, 828323121, 0, 0, 100)
    sprite('Action_276_02', 2)	# 11-12	 **attackbox here**
    SFX_3('SE038')
    StartMultihit()
    GFX_0('EffTagAssistBlade00', 100)
    sprite('Action_276_02', 2)	# 13-14	 **attackbox here**
    Unknown1019(90)
    sprite('Action_276_02', 2)	# 15-16	 **attackbox here**
    Unknown1019(90)
    sprite('Action_276_02', 2)	# 17-18	 **attackbox here**
    Unknown1019(90)
    sprite('Action_276_02', 2)	# 19-20	 **attackbox here**
    Unknown1019(90)
    label(1)
    sprite('Action_276_02', 2)	# 21-22	 **attackbox here**
    StartMultihit()
    sprite('Action_276_03', 5)	# 23-27
    clearUponHandler(11)
    physicsXImpulse(8000)
    sprite('Action_276_04', 5)	# 28-32	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown1084(1)
    sprite('Action_276_05', 2)	# 33-34
    GFX_0('EffTagAssistBlade01', 100)
    physicsXImpulse(8000)
    physicsYImpulse(36000)
    setGravity(2200)
    clearUponHandler(2)
    sendToLabelUpon(2, 9)
    Hitstop(0)
    SFX_0('002_highjump_0')
    sprite('Action_276_06', 2)	# 35-36	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(30000)
    Unknown1019(90)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_276_07', 2)	# 37-38	 **attackbox here**
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 39-40
    Unknown1019(90)
    sprite('Action_276_07', 2)	# 41-42	 **attackbox here**
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 43-44
    Unknown1019(90)
    sprite('Action_276_07', 2)	# 45-46	 **attackbox here**
    Unknown1019(90)
    sprite('Action_276_08', 2)	# 47-48
    loopRest()
    sprite('Action_276_11', 2)	# 49-50
    sprite('Action_276_12', 5)	# 51-55
    YAccel(0)
    sprite('Action_276_13', 4)	# 56-59
    sprite('Action_276_14', 4)	# 60-63
    sprite('Action_276_15', 4)	# 64-67
    sprite('Action_276_16', 3)	# 68-70
    sprite('Action_276_17', 3)	# 71-73
    sprite('Action_276_18', 32767)	# 74-32840
    label(9)
    sprite('Action_138_00', 3)	# 32841-32843
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_138_01', 4)	# 32844-32847
    sprite('Action_138_02', 4)	# 32848-32851
    sprite('Action_138_03', 3)	# 32852-32854
    sprite('Action_138_04', 3)	# 32855-32857

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
    Unknown2036(89, -1, 0)
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
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateAssaultDDDOD')
    else:
        enterState('UltimateAssaultDDD')

@State
def UltimateAssaultDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(5)
        Damage(600)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(20000)
        PushbackX(4500)
        AirUntechableTime(40)
        Hitstop(12)
        Unknown30055('a08601006400000000000000')
        Unknown11064(1)
        Unknown11062(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown9016(1)
        Unknown1084(1)
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 == 2):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('Action_200_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('Action_200_01', 3)	# 4-6
    sprite('Action_200_02', 4)	# 7-10
    sprite('Action_200_03', 6)	# 11-16
    GFX_0('EffConcentration', 100)
    label(0)
    sprite('Action_200_04', 4)	# 17-20
    sprite('Action_200_05', 4)	# 21-24
    Unknown2038(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_200_06', 4)	# 25-28
    sprite('Action_200_04', 4)	# 29-32
    sprite('Action_210_00', 4)	# 33-36
    Unknown26('EffConcentration')
    sprite('Action_210_01', 5)	# 37-41
    GFX_0('EffIWBlade00', 0)
    sprite('Action_210_02', 8)	# 42-49
    sprite('Action_210_03', 10)	# 50-59
    sprite('Action_210_04', 5)	# 60-64	 **attackbox here**
    SFX_3('SE043')
    SFX_3('SE221')
    GFX_0('ObjIWMatome', 100)
    Unknown23029(1, 5000, 0)
    sprite('Action_210_05', 5)	# 65-69
    sprite('Action_210_08', 3)	# 70-72
    sprite('Action_210_06', 3)	# 73-75
    sprite('Action_210_07', 3)	# 76-78
    Unknown7006('uhy251_0', 100, 846817397, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_210_08', 3)	# 79-81
    setInvincible(0)
    GFX_0('DDD_Particle', -1)
    loopRest()
    sprite('Action_210_07', 3)	# 82-84
    sprite('Action_210_08', 3)	# 85-87
    sprite('Action_210_09', 3)	# 88-90
    sprite('Action_210_07', 3)	# 91-93
    sprite('Action_210_08', 3)	# 94-96
    sprite('Action_210_09', 3)	# 97-99
    sprite('Action_210_07', 3)	# 100-102
    sprite('Action_210_08', 3)	# 103-105
    sprite('Action_211_00', 6)	# 106-111
    sprite('Action_211_01', 8)	# 112-119
    sprite('Action_211_02', 7)	# 120-126
    sprite('Action_211_03', 6)	# 127-132
    GFX_0('IWEndEff', -1)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_211_04', 7)	# 133-139
    sprite('Action_211_05', 18)	# 140-157
    sprite('Action_211_06', 5)	# 158-162

@State
def UltimateAssaultDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown30063(1)
        AttackLevel_(5)
        Damage(700)
        MinimumDamagePct(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(3000)
        AirPushbackY(20000)
        AirUntechableTime(40)
        Hitstop(12)
        Unknown30055('a08601006400000000000000')
        Unknown11064(1)
        callSubroutine('InsulatorSpecialInit')
        Unknown2037(0)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_2 == 2):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('Action_200_00', 3)	# 1-3
    Unknown1084(1)
    setInvincible(1)
    sprite('Action_200_01', 3)	# 4-6
    sprite('Action_200_02', 4)	# 7-10
    sprite('Action_200_03', 6)	# 11-16
    GFX_0('EffConcentration', 100)
    label(0)
    sprite('Action_200_04', 4)	# 17-20
    sprite('Action_200_05', 4)	# 21-24
    Unknown2038(1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_200_06', 4)	# 25-28
    sprite('Action_200_04', 4)	# 29-32
    sprite('Action_210_00', 4)	# 33-36
    Unknown26('EffConcentration')
    sprite('Action_210_01', 5)	# 37-41
    GFX_0('EffIWBlade00', 0)
    sprite('Action_210_02', 8)	# 42-49
    sprite('Action_210_03', 10)	# 50-59
    sprite('Action_210_04', 5)	# 60-64	 **attackbox here**
    SFX_3('SE043')
    SFX_3('SE221')
    GFX_0('ObjIWMatomeOD', 100)
    Unknown23029(1, 5000, 0)
    sprite('Action_210_05', 5)	# 65-69
    sprite('Action_210_08', 3)	# 70-72
    sprite('Action_210_06', 3)	# 73-75
    sprite('Action_210_07', 3)	# 76-78
    Unknown7006('uhy251_0', 100, 846817397, 828322101, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_210_08', 3)	# 79-81
    setInvincible(0)
    loopRest()
    sprite('Action_210_09', 3)	# 82-84
    sprite('Action_210_07', 3)	# 85-87
    sprite('Action_210_08', 3)	# 88-90
    sprite('Action_210_09', 3)	# 91-93
    sprite('Action_210_07', 3)	# 94-96
    sprite('Action_210_08', 3)	# 97-99
    sprite('Action_210_09', 3)	# 100-102
    GFX_0('DDD_Particle', -1)
    sprite('Action_210_07', 3)	# 103-105
    sprite('Action_210_08', 3)	# 106-108
    sprite('Action_210_09', 3)	# 109-111
    sprite('Action_210_07', 3)	# 112-114
    sprite('Action_210_08', 3)	# 115-117
    sprite('Action_211_00', 6)	# 118-123
    sprite('Action_211_01', 8)	# 124-131
    sprite('Action_211_02', 7)	# 132-138
    sprite('Action_211_03', 6)	# 139-144
    GFX_0('IWEndEff', -1)
    SFX_3('SE_InsulatorSwingC')
    sprite('Action_211_04', 7)	# 145-151
    sprite('Action_211_05', 18)	# 152-169
    sprite('Action_211_06', 5)	# 170-174

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
    sprite('Action_009_00', 6)	# 127-132
    sprite('Action_009_12', 6)	# 133-138
    sprite('Action_009_13', 6)	# 139-144
    sprite('Action_009_14', 3)	# 145-147
    SFX_3('SE_InsulatorSwingC')
    Unknown2053(1)
    sprite('Action_009_15', 3)	# 148-150	 **attackbox here**
    GFX_0('EffNmlAtkAir5BBlade', 100)
    sprite('Action_009_16', 5)	# 151-155
    sendToLabelUpon(2, 9)
    sprite('Action_009_17', 4)	# 156-159
    sprite('Action_009_18', 3)	# 160-162
    sprite('Action_009_19', 3)	# 163-165
    sprite('Action_009_20', 4)	# 166-169
    label(1)
    sprite('Action_022_00', 3)	# 170-172
    sprite('Action_022_01', 3)	# 173-175
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_021_00', 5)	# 176-180
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_021_01', 12)	# 181-192
    sprite('Action_021_02', 5)	# 193-197
    sprite('Action_021_03', 4)	# 198-201
    sprite('Action_021_04', 4)	# 202-205

@Subroutine
def MouthTableInit():
    Unknown18011('uhy000', 12643, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy500', 12643, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 12337, 13667, 12641, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy500', '001')
    Unknown18011('uhy501', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy501', '002')
    Unknown18011('uhy502', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy502', '003')
    Unknown18011('uhy503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy503', '004')
    Unknown18011('uhy504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy504', '005')
    Unknown18011('uhy505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy505', '006')
    Unknown18011('uhy520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy520', '007')
    Unknown18011('uhy521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy521', '008')
    Unknown18011('uhy522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy522', '009')
    Unknown18011('uhy523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy523', '010')
    Unknown18011('uhy524', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy524', '011')
    Unknown18011('uhy525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy525', '012')
    Unknown18011('uhy402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy403_0', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600bma', 12643, 13665, 13667, 13665, 12643, 24880, 25397, 24885, 25397, 13107, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 12641, 25392, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601brg', 12643, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600btg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600pag', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 12849, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy602pag', 12643, 24880, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy602rrb', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 12641, 25392, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600uli', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601uor', 12643, 14177, 14179, 14177, 14179, 12641, 25393, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy600uva', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601uwa', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 12641, 25392, 12849, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601uyu', 12643, 13665, 13667, 13665, 13667, 12641, 25394, 13362, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601use', 12643, 12897, 25395, 24887, 12593, 14179, 14177, 12899, 24883, 25399, 14641, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601ahe', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601pad', 12899, 13153, 25397, 14386, 12641, 25394, 13873, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25397, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601uhi', 12643, 24888, 25399, 24887, 12337, 14179, 14177, 14179, 12641, 25394, 24889, 12849, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601uak', 12643, 12897, 25392, 24887, 12593, 12899, 24888, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy601kym', 12899, 14689, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24885, 25400, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy600bma', '017')
    Unknown30092('uhy600btg', '018')
    Unknown30092('uhy600pag', '019')
    Unknown30092('uhy600pbc', '020')
    Unknown30092('uhy600pna', '021')
    Unknown30092('uhy600rrb', '022')
    Unknown30092('uhy600uli', '023')
    Unknown30092('uhy600uva', '024')
    Unknown30092('uhy601bno', '025')
    Unknown30092('uhy601brg', '026')
    Unknown30092('uhy601rbl', '027')
    Unknown30092('uhy601uor', '028')
    Unknown30092('uhy601uwa', '029')
    Unknown30092('uhy601uyu', '030')
    Unknown30092('uhy602pag', '031')
    Unknown30092('uhy602rrb', '032')
    Unknown30092('uhy601use', '033')
    Unknown30092('uhy601ahe', '034')
    Unknown30092('uhy601pad', '035')
    Unknown30092('uhy601uhi', '036')
    Unknown30092('uhy601uak', '037')
    Unknown30092('uhy601kym', '038')
    Unknown18011('uhy701bma', 12643, 14177, 14179, 12641, 25392, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 12338, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700brg', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700btg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701pag', 12643, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700pna', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 12849, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701rrb', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701uor', 12643, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700uva', 12643, 14177, 14179, 14177, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700uwa', 12643, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701uyu', 12643, 14177, 12643, 24882, 25397, 24885, 25397, 24885, 25397, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy700use', 12643, 12897, 25400, 24887, 12337, 12643, 24882, 12337, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701ahe', 12899, 12641, 25401, 24887, 25399, 24887, 25399, 24887, 12849, 14435, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701pad', 12899, 12641, 25395, 24887, 13105, 12643, 24882, 25399, 24887, 12849, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701uhi', 12643, 12641, 25393, 24887, 12593, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701uak', 12643, 24880, 12337, 14179, 12641, 25392, 12595, 14177, 12899, 24885, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhy701kym', 12643, 12641, 25393, 12593, 13921, 13923, 13921, 14179, 12897, 25395, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhy700brg', '039')
    Unknown30092('uhy700btg', '040')
    Unknown30092('uhy700pbc', '041')
    Unknown30092('uhy700pna', '042')
    Unknown30092('uhy700rbl', '043')
    Unknown30092('uhy700uva', '044')
    Unknown30092('uhy700uwa', '045')
    Unknown30092('uhy701bma', '046')
    Unknown30092('uhy701bno', '047')
    Unknown30092('uhy701pag', '048')
    Unknown30092('uhy701rrb', '049')
    Unknown30092('uhy701uli', '050')
    Unknown30092('uhy701uor', '051')
    Unknown30092('uhy701uyu', '052')
    Unknown30092('uhy700use', '053')
    Unknown30092('uhy701ahe', '054')
    Unknown30092('uhy701pad', '055')
    Unknown30092('uhy701uhi', '056')
    Unknown30092('uhy701uak', '057')
    Unknown30092('uhy701kym', '058')
    if SLOT_172:
        Unknown18011('uhy000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy500', 12643, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 12337, 13667, 12641, 25392, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy501', 12643, 12643, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 13409, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13361, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy502', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy503', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12594, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy504', 12643, 12643, 13153, 25397, 13620, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 25393, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy505', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 25393, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 25393, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy522', 12899, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 25393, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 24887, 25399, 12594, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy524', 12643, 13921, 13923, 13921, 13923, 13921, 13667, 24882, 25399, 24887, 25399, 24887, 12337, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy525', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 25398, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy403_0', 12643, 13155, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 12641, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600bma', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601bno', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 12641, 25392, 24887, 25399, 13364, 14177, 14179, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601brg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14129, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600btg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600pag', 12643, 13155, 14177, 14179, 14177, 12899, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 14388, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy602pag', 12643, 24880, 25399, 24887, 25399, 24887, 25399, 13875, 12641, 25399, 24886, 25398, 12594, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600pbc', 12643, 14177, 14179, 13665, 12643, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 14177, 14179, 14177, 14179, 13921, 13155, 14177, 14179, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600pna', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 13361, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy602rrb', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14435, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13361, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600uli', 12643, 12643, 14177, 14179, 14177, 14179, 13921, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601uor', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy600uva', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 13105, 12899, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601uwa', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 12641, 25392, 12849, 14177, 14179, 14177, 14179, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601uyu', 12643, 12643, 14177, 14179, 14177, 14435, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25400, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601use', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 14177, 13667, 12899, 24883, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 24887, 25398, 24883, 25399, 25393, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601ahe', 12643, 12643, 14177, 14179, 14177, 14179, 12897, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601pad', 12643, 12643, 14177, 14179, 14177, 14179, 12643, 24881, 25396, 24887, 25399, 24887, 25395, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601uhi', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 12643, 12897, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24883, 25397, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601uak', 12643, 12643, 14177, 14179, 14177, 14179, 12899, 24882, 25399, 25394, 13105, 14177, 14179, 13665, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy601kym', 12643, 12643, 13153, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 13411, 24880, 25399, 24887, 25395, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701bma', 12643, 14177, 14179, 12641, 25392, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701bno', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700brg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 25398, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700btg', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 24880, 25399, 24887, 25399, 25398, 24881, 25399, 24887, 25396, 24881, 25399, 24887, 25399, 24887, 25396, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701pag', 12643, 14177, 14179, 14177, 13155, 12899, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 24881, 25399, 24887, 25399, 25397, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700pbc', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 25399, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700pna', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13411, 14179, 24887, 25399, 25394, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25401, 25399, 25398, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700rbl', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701rrb', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 24881, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701uli', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701uor', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700uva', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24881, 25399, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700uwa', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 12643, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701uyu', 12643, 12899, 14177, 13411, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 13411, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy700use', 12643, 12643, 14177, 14179, 14177, 13667, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701ahe', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701pad', 12643, 12643, 14177, 14179, 12897, 13667, 14177, 14179, 13921, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701uhi', 12643, 12643, 14177, 14179, 13153, 12643, 24887, 25399, 24887, 25399, 25393, 24883, 25399, 24887, 25399, 24887, 25399, 25399, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701uak', 12643, 12643, 14177, 13923, 13667, 13153, 14435, 13665, 12899, 13921, 12643, 24880, 25399, 25393, 24887, 25399, 24887, 25399, 25396, 24881, 25395, 12337, 14177, 14179, 13665, 14179, 14177, 14179, 12641, 25394, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhy701kym', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 14179, 13667, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bno')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('btg')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('uli')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('uwa')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('rrb')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('pna')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('rbl')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uor')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('pag')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('uva')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('uyu')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('bma')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('ahe')
    if SLOT_ReturnVal:
        _gotolabel(240)
    PartnerChar('uak')
    if SLOT_ReturnVal:
        _gotolabel(250)
    PartnerChar('uhi')
    if SLOT_ReturnVal:
        _gotolabel(260)
    PartnerChar('pad')
    if SLOT_ReturnVal:
        _gotolabel(270)
    PartnerChar('kym')
    if SLOT_ReturnVal:
        _gotolabel(280)
    PartnerChar('use')
    if SLOT_ReturnVal:
        _gotolabel(290)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('Action_050_01', 5)	# 2-6
    if SLOT_158:
        Unknown7006('uhy500', 100, 897149045, 13360, 0, 0, 100, 897149045, 12848, 0, 0, 100, 897149045, 13104, 0, 0, 100)
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 7-11
    sprite('Action_050_03', 5)	# 12-16
    sprite('Action_050_01', 5)	# 17-21
    sprite('Action_050_02', 5)	# 22-26
    sprite('Action_050_03', 5)	# 27-31
    sprite('Action_050_04', 5)	# 32-36
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 37-40
    sprite('Action_050_06', 4)	# 41-44
    sprite('Action_050_07', 3)	# 45-47	 **attackbox here**
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 48-50	 **attackbox here**
    sprite('Action_050_09', 3)	# 51-53	 **attackbox here**
    sprite('Action_050_10', 3)	# 54-56	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 57-58	 **attackbox here**
    sprite('Action_050_12', 2)	# 59-60	 **attackbox here**
    sprite('Action_050_13', 4)	# 61-64	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 65-67	 **attackbox here**
    sprite('Action_050_15', 3)	# 68-70	 **attackbox here**
    sprite('Action_050_16', 4)	# 71-74	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 75-78	 **attackbox here**
    sprite('Action_050_18', 4)	# 79-82	 **attackbox here**
    sprite('Action_050_19', 5)	# 83-87	 **attackbox here**
    sprite('Action_050_20', 7)	# 88-94
    sprite('Action_050_21', 8)	# 95-102
    sprite('Action_050_22', 11)	# 103-113
    sprite('Action_050_23', 5)	# 114-118	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_050_24', 12)	# 119-130	 **attackbox here**
    label(1)
    sprite('Action_050_24', 1)	# 131-131	 **attackbox here**
    if SLOT_97:
        _gotolabel(1)
    sprite('Action_050_25', 6)	# 132-137	 **attackbox here**
    Unknown21007(24, 41)
    Unknown23018(1)
    sprite('Action_000_00', 7)	# 138-144	 **attackbox here**
    sprite('Action_000_01', 7)	# 145-151	 **attackbox here**
    sprite('Action_000_02', 6)	# 152-157	 **attackbox here**
    sprite('Action_000_03', 6)	# 158-163	 **attackbox here**
    sprite('Action_000_04', 5)	# 164-168	 **attackbox here**
    sprite('Action_000_05', 5)	# 169-173	 **attackbox here**
    sprite('Action_000_06', 5)	# 174-178	 **attackbox here**
    sprite('Action_000_07', 6)	# 179-184	 **attackbox here**
    sprite('Action_000_08', 6)	# 185-190	 **attackbox here**
    sprite('Action_000_09', 7)	# 191-197	 **attackbox here**
    sprite('Action_000_10', 7)	# 198-204	 **attackbox here**
    sprite('Action_000_11', 6)	# 205-210	 **attackbox here**
    sprite('Action_000_12', 6)	# 211-216	 **attackbox here**
    sprite('Action_000_13', 5)	# 217-221	 **attackbox here**
    sprite('Action_000_14', 5)	# 222-226	 **attackbox here**
    sprite('Action_000_15', 5)	# 227-231	 **attackbox here**
    sprite('Action_000_16', 6)	# 232-237	 **attackbox here**
    sprite('Action_000_17', 6)	# 238-243	 **attackbox here**
    loopRest()
    ExitState()
    label(10)
    sprite('Hyd901_00', 4)	# 244-247
    sprite('Hyd901_01', 4)	# 248-251
    Unknown7006('uhy505', 100, 897149045, 13360, 0, 0, 100, 897149045, 12592, 0, 0, 100, 897149045, 13104, 0, 0, 100)
    sprite('Hyd901_02', 4)	# 252-255
    sprite('Hyd901_00', 4)	# 256-259
    sprite('Hyd901_01', 4)	# 260-263
    sprite('Hyd901_02', 4)	# 264-267
    sprite('Hyd901_00', 4)	# 268-271
    sprite('Hyd901_01', 4)	# 272-275
    sprite('Hyd901_02', 4)	# 276-279
    sprite('Hyd901_00', 4)	# 280-283
    sprite('Hyd901_01', 4)	# 284-287
    sprite('Hyd901_02', 4)	# 288-291
    sprite('Hyd901_03', 5)	# 292-296
    sprite('Hyd901_04', 6)	# 297-302
    sprite('Hyd901_05', 2)	# 303-304
    sprite('Hyd901_06', 5)	# 305-309
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 70)	# 310-379
    sprite('Hyd901_08', 8)	# 380-387
    Unknown23018(1)
    Unknown21007(24, 41)
    sprite('Hyd901_09', 5)	# 388-392
    sprite('Hyd901_10', 5)	# 393-397
    sprite('Hyd901_11', 5)	# 398-402
    sprite('Hyd901_12', 4)	# 403-406
    Unknown21011(60)
    ExitState()
    label(20)
    sprite('Action_000_00', 1)	# 407-407	 **attackbox here**
    SFX_1('uhy701uyu')
    label(21)
    sprite('Action_000_00', 7)	# 408-414	 **attackbox here**
    sprite('Action_000_01', 7)	# 415-421	 **attackbox here**
    sprite('Action_000_02', 6)	# 422-427	 **attackbox here**
    sprite('Action_000_03', 6)	# 428-433	 **attackbox here**
    sprite('Action_000_04', 5)	# 434-438	 **attackbox here**
    sprite('Action_000_05', 5)	# 439-443	 **attackbox here**
    sprite('Action_000_06', 5)	# 444-448	 **attackbox here**
    sprite('Action_000_07', 6)	# 449-454	 **attackbox here**
    sprite('Action_000_08', 6)	# 455-460	 **attackbox here**
    sprite('Action_000_09', 7)	# 461-467	 **attackbox here**
    sprite('Action_000_10', 7)	# 468-474	 **attackbox here**
    sprite('Action_000_11', 6)	# 475-480	 **attackbox here**
    sprite('Action_000_12', 6)	# 481-486	 **attackbox here**
    sprite('Action_000_13', 5)	# 487-491	 **attackbox here**
    sprite('Action_000_14', 5)	# 492-496	 **attackbox here**
    sprite('Action_000_15', 5)	# 497-501	 **attackbox here**
    sprite('Action_000_16', 6)	# 502-507	 **attackbox here**
    sprite('Action_000_17', 6)	# 508-513	 **attackbox here**
    gotoLabel(21)
    label(100)
    sprite('Hyd901_00', 1)	# 514-514
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Hyd901_00', 4)	# 515-518
    sprite('Hyd901_01', 4)	# 519-522
    sprite('Hyd901_02', 4)	# 523-526
    gotoLabel(101)
    label(102)
    sprite('Hyd901_00', 4)	# 527-530
    sprite('Hyd901_01', 4)	# 531-534
    sprite('Hyd901_02', 4)	# 535-538
    sprite('Hyd901_03', 5)	# 539-543
    sprite('Hyd901_04', 6)	# 544-549
    sprite('Hyd901_05', 2)	# 550-551
    sprite('Hyd901_06', 5)	# 552-556
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 1)	# 557-557
    SFX_1('uhy601brg')
    label(103)
    sprite('Hyd901_07', 1)	# 558-558
    if SLOT_97:
        _gotolabel(103)
    sprite('Hyd901_08', 8)	# 559-566
    sprite('Hyd901_09', 5)	# 567-571
    sprite('Hyd901_10', 5)	# 572-576
    sprite('Hyd901_11', 5)	# 577-581
    sprite('Hyd901_12', 4)	# 582-585
    Unknown23018(1)
    label(103)
    sprite('Action_000_00', 7)	# 586-592	 **attackbox here**
    sprite('Action_000_01', 7)	# 593-599	 **attackbox here**
    sprite('Action_000_02', 6)	# 600-605	 **attackbox here**
    sprite('Action_000_03', 6)	# 606-611	 **attackbox here**
    sprite('Action_000_04', 5)	# 612-616	 **attackbox here**
    sprite('Action_000_05', 5)	# 617-621	 **attackbox here**
    sprite('Action_000_06', 5)	# 622-626	 **attackbox here**
    sprite('Action_000_07', 6)	# 627-632	 **attackbox here**
    sprite('Action_000_08', 6)	# 633-638	 **attackbox here**
    sprite('Action_000_09', 7)	# 639-645	 **attackbox here**
    sprite('Action_000_10', 7)	# 646-652	 **attackbox here**
    sprite('Action_000_11', 6)	# 653-658	 **attackbox here**
    sprite('Action_000_12', 6)	# 659-664	 **attackbox here**
    sprite('Action_000_13', 5)	# 665-669	 **attackbox here**
    sprite('Action_000_14', 5)	# 670-674	 **attackbox here**
    sprite('Action_000_15', 5)	# 675-679	 **attackbox here**
    sprite('Action_000_16', 6)	# 680-685	 **attackbox here**
    sprite('Action_000_17', 6)	# 686-691	 **attackbox here**
    gotoLabel(103)
    ExitState()
    label(110)
    sprite('Hyd901_00', 1)	# 692-692
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Hyd901_00', 4)	# 693-696
    sprite('Hyd901_01', 4)	# 697-700
    sprite('Hyd901_02', 4)	# 701-704
    gotoLabel(111)
    label(112)
    sprite('Hyd901_00', 4)	# 705-708
    SFX_1('uhy601bno')
    sprite('Hyd901_01', 4)	# 709-712
    sprite('Hyd901_02', 4)	# 713-716
    Unknown2037(6)
    label(113)
    sprite('Hyd901_00', 4)	# 717-720
    sprite('Hyd901_01', 4)	# 721-724
    sprite('Hyd901_02', 4)	# 725-728
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(113)
    sprite('Hyd901_03', 5)	# 729-733
    sprite('Hyd901_04', 6)	# 734-739
    sprite('Hyd901_05', 2)	# 740-741
    sprite('Hyd901_06', 5)	# 742-746
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 70)	# 747-816
    sprite('Hyd901_08', 8)	# 817-824
    sprite('Hyd901_09', 5)	# 825-829
    sprite('Hyd901_10', 5)	# 830-834
    sprite('Hyd901_11', 5)	# 835-839
    sprite('Hyd901_12', 4)	# 840-843
    Unknown23018(1)
    label(114)
    sprite('Action_000_00', 7)	# 844-850	 **attackbox here**
    sprite('Action_000_01', 7)	# 851-857	 **attackbox here**
    sprite('Action_000_02', 6)	# 858-863	 **attackbox here**
    sprite('Action_000_03', 6)	# 864-869	 **attackbox here**
    sprite('Action_000_04', 5)	# 870-874	 **attackbox here**
    sprite('Action_000_05', 5)	# 875-879	 **attackbox here**
    sprite('Action_000_06', 5)	# 880-884	 **attackbox here**
    sprite('Action_000_07', 6)	# 885-890	 **attackbox here**
    sprite('Action_000_08', 6)	# 891-896	 **attackbox here**
    sprite('Action_000_09', 7)	# 897-903	 **attackbox here**
    sprite('Action_000_10', 7)	# 904-910	 **attackbox here**
    sprite('Action_000_11', 6)	# 911-916	 **attackbox here**
    sprite('Action_000_12', 6)	# 917-922	 **attackbox here**
    sprite('Action_000_13', 5)	# 923-927	 **attackbox here**
    sprite('Action_000_14', 5)	# 928-932	 **attackbox here**
    sprite('Action_000_15', 5)	# 933-937	 **attackbox here**
    sprite('Action_000_16', 6)	# 938-943	 **attackbox here**
    sprite('Action_000_17', 6)	# 944-949	 **attackbox here**
    gotoLabel(114)
    ExitState()
    label(120)
    sprite('Action_050_01', 5)	# 950-954
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-500)
    else:
        Unknown1000(-1465000)
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 955-959
    sprite('Action_050_03', 5)	# 960-964
    sprite('Action_050_01', 5)	# 965-969
    sprite('Action_050_02', 5)	# 970-974
    sprite('Action_050_03', 5)	# 975-979
    sprite('Action_050_04', 5)	# 980-984
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 985-988
    sprite('Action_050_06', 4)	# 989-992
    sprite('Action_050_07', 3)	# 993-995	 **attackbox here**
    SFX_1('uhy600btg')
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 996-998	 **attackbox here**
    sprite('Action_050_09', 3)	# 999-1001	 **attackbox here**
    sprite('Action_050_10', 3)	# 1002-1004	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 1005-1006	 **attackbox here**
    sprite('Action_050_12', 2)	# 1007-1008	 **attackbox here**
    sprite('Action_050_13', 4)	# 1009-1012	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 1013-1015	 **attackbox here**
    sprite('Action_050_15', 3)	# 1016-1018	 **attackbox here**
    sprite('Action_050_16', 4)	# 1019-1022	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 1023-1026	 **attackbox here**
    sprite('Action_050_18', 4)	# 1027-1030	 **attackbox here**
    sprite('Action_050_19', 5)	# 1031-1035	 **attackbox here**
    sprite('Action_050_20', 7)	# 1036-1042
    sprite('Action_050_21', 8)	# 1043-1050
    sprite('Action_050_22', 11)	# 1051-1061
    sprite('Action_050_23', 5)	# 1062-1066	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_050_24', 12)	# 1067-1078	 **attackbox here**
    label(121)
    sprite('Action_050_24', 1)	# 1079-1079	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_050_24', 20)	# 1080-1099	 **attackbox here**
    sprite('Action_050_25', 6)	# 1100-1105	 **attackbox here**
    sprite('Action_000_00', 7)	# 1106-1112	 **attackbox here**
    sprite('Action_000_01', 7)	# 1113-1119	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(60)
    sprite('Action_000_02', 6)	# 1120-1125	 **attackbox here**
    sprite('Action_000_03', 6)	# 1126-1131	 **attackbox here**
    sprite('Action_000_04', 5)	# 1132-1136	 **attackbox here**
    sprite('Action_000_05', 5)	# 1137-1141	 **attackbox here**
    sprite('Action_000_06', 5)	# 1142-1146	 **attackbox here**
    sprite('Action_000_07', 6)	# 1147-1152	 **attackbox here**
    sprite('Action_000_08', 6)	# 1153-1158	 **attackbox here**
    sprite('Action_000_09', 7)	# 1159-1165	 **attackbox here**
    sprite('Action_000_10', 7)	# 1166-1172	 **attackbox here**
    sprite('Action_000_11', 6)	# 1173-1178	 **attackbox here**
    sprite('Action_000_12', 6)	# 1179-1184	 **attackbox here**
    sprite('Action_000_13', 5)	# 1185-1189	 **attackbox here**
    sprite('Action_000_14', 5)	# 1190-1194	 **attackbox here**
    sprite('Action_000_15', 5)	# 1195-1199	 **attackbox here**
    sprite('Action_000_16', 6)	# 1200-1205	 **attackbox here**
    sprite('Action_000_17', 6)	# 1206-1211	 **attackbox here**
    label(122)
    sprite('Action_000_00', 7)	# 1212-1218	 **attackbox here**
    sprite('Action_000_01', 7)	# 1219-1225	 **attackbox here**
    sprite('Action_000_02', 6)	# 1226-1231	 **attackbox here**
    sprite('Action_000_03', 6)	# 1232-1237	 **attackbox here**
    sprite('Action_000_04', 5)	# 1238-1242	 **attackbox here**
    sprite('Action_000_05', 5)	# 1243-1247	 **attackbox here**
    sprite('Action_000_06', 5)	# 1248-1252	 **attackbox here**
    sprite('Action_000_07', 6)	# 1253-1258	 **attackbox here**
    sprite('Action_000_08', 6)	# 1259-1264	 **attackbox here**
    sprite('Action_000_09', 7)	# 1265-1271	 **attackbox here**
    sprite('Action_000_10', 7)	# 1272-1278	 **attackbox here**
    sprite('Action_000_11', 6)	# 1279-1284	 **attackbox here**
    sprite('Action_000_12', 6)	# 1285-1290	 **attackbox here**
    sprite('Action_000_13', 5)	# 1291-1295	 **attackbox here**
    sprite('Action_000_14', 5)	# 1296-1300	 **attackbox here**
    sprite('Action_000_15', 5)	# 1301-1305	 **attackbox here**
    sprite('Action_000_16', 6)	# 1306-1311	 **attackbox here**
    sprite('Action_000_17', 6)	# 1312-1317	 **attackbox here**
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('Action_050_01', 5)	# 1318-1322
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 1323-1327
    sprite('Action_050_03', 5)	# 1328-1332
    sprite('Action_050_01', 5)	# 1333-1337
    sprite('Action_050_02', 5)	# 1338-1342
    sprite('Action_050_03', 5)	# 1343-1347
    sprite('Action_050_04', 5)	# 1348-1352
    SFX_1('uhy600pbc')
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 1353-1356
    sprite('Action_050_06', 4)	# 1357-1360
    sprite('Action_050_07', 3)	# 1361-1363	 **attackbox here**
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 1364-1366	 **attackbox here**
    sprite('Action_050_09', 3)	# 1367-1369	 **attackbox here**
    sprite('Action_050_10', 3)	# 1370-1372	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 1373-1374	 **attackbox here**
    sprite('Action_050_12', 2)	# 1375-1376	 **attackbox here**
    sprite('Action_050_13', 4)	# 1377-1380	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 1381-1383	 **attackbox here**
    sprite('Action_050_15', 3)	# 1384-1386	 **attackbox here**
    sprite('Action_050_16', 4)	# 1387-1390	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 1391-1394	 **attackbox here**
    sprite('Action_050_18', 4)	# 1395-1398	 **attackbox here**
    sprite('Action_050_19', 5)	# 1399-1403	 **attackbox here**
    sprite('Action_050_20', 7)	# 1404-1410
    sprite('Action_050_21', 8)	# 1411-1418
    sprite('Action_050_22', 11)	# 1419-1429
    sprite('Action_050_23', 5)	# 1430-1434	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_050_24', 12)	# 1435-1446	 **attackbox here**
    label(131)
    sprite('Action_050_24', 1)	# 1447-1447	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_050_24', 30)	# 1448-1477	 **attackbox here**
    sprite('Action_050_25', 6)	# 1478-1483	 **attackbox here**
    Unknown21007(24, 40)
    Unknown23018(1)
    label(132)
    sprite('Action_000_00', 7)	# 1484-1490	 **attackbox here**
    sprite('Action_000_01', 7)	# 1491-1497	 **attackbox here**
    sprite('Action_000_02', 6)	# 1498-1503	 **attackbox here**
    sprite('Action_000_03', 6)	# 1504-1509	 **attackbox here**
    sprite('Action_000_04', 5)	# 1510-1514	 **attackbox here**
    sprite('Action_000_05', 5)	# 1515-1519	 **attackbox here**
    sprite('Action_000_06', 5)	# 1520-1524	 **attackbox here**
    sprite('Action_000_07', 6)	# 1525-1530	 **attackbox here**
    sprite('Action_000_08', 6)	# 1531-1536	 **attackbox here**
    sprite('Action_000_09', 7)	# 1537-1543	 **attackbox here**
    sprite('Action_000_10', 7)	# 1544-1550	 **attackbox here**
    sprite('Action_000_11', 6)	# 1551-1556	 **attackbox here**
    sprite('Action_000_12', 6)	# 1557-1562	 **attackbox here**
    sprite('Action_000_13', 5)	# 1563-1567	 **attackbox here**
    sprite('Action_000_14', 5)	# 1568-1572	 **attackbox here**
    sprite('Action_000_15', 5)	# 1573-1577	 **attackbox here**
    sprite('Action_000_16', 6)	# 1578-1583	 **attackbox here**
    sprite('Action_000_17', 6)	# 1584-1589	 **attackbox here**
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('Hyd901_00', 4)	# 1590-1593
    Unknown1000(-1340000)
    SFX_1('uhy600uli')
    Unknown2037(30)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
    label(141)
    sprite('Hyd901_00', 4)	# 1594-1597
    sprite('Hyd901_01', 4)	# 1598-1601
    sprite('Hyd901_02', 4)	# 1602-1605
    gotoLabel(141)
    label(142)
    sprite('Hyd901_03', 4)	# 1606-1609
    sprite('Hyd901_04', 6)	# 1610-1615
    sprite('Hyd901_05', 2)	# 1616-1617
    sprite('Hyd901_06', 4)	# 1618-1621
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 60)	# 1622-1681
    sprite('Hyd901_08', 8)	# 1682-1689
    sprite('Hyd901_09', 5)	# 1690-1694
    sprite('Hyd901_10', 5)	# 1695-1699
    sprite('Hyd901_11', 5)	# 1700-1704
    sprite('Hyd901_12', 4)	# 1705-1708
    Unknown23018(1)
    label(143)
    sprite('Action_000_00', 7)	# 1709-1715	 **attackbox here**
    sprite('Action_000_01', 7)	# 1716-1722	 **attackbox here**
    sprite('Action_000_02', 6)	# 1723-1728	 **attackbox here**
    sprite('Action_000_03', 6)	# 1729-1734	 **attackbox here**
    sprite('Action_000_04', 5)	# 1735-1739	 **attackbox here**
    sprite('Action_000_05', 5)	# 1740-1744	 **attackbox here**
    sprite('Action_000_06', 5)	# 1745-1749	 **attackbox here**
    sprite('Action_000_07', 6)	# 1750-1755	 **attackbox here**
    sprite('Action_000_08', 6)	# 1756-1761	 **attackbox here**
    sprite('Action_000_09', 7)	# 1762-1768	 **attackbox here**
    sprite('Action_000_10', 7)	# 1769-1775	 **attackbox here**
    sprite('Action_000_11', 6)	# 1776-1781	 **attackbox here**
    sprite('Action_000_12', 6)	# 1782-1787	 **attackbox here**
    sprite('Action_000_13', 5)	# 1788-1792	 **attackbox here**
    sprite('Action_000_14', 5)	# 1793-1797	 **attackbox here**
    sprite('Action_000_15', 5)	# 1798-1802	 **attackbox here**
    sprite('Action_000_16', 6)	# 1803-1808	 **attackbox here**
    sprite('Action_000_17', 6)	# 1809-1814	 **attackbox here**
    gotoLabel(143)
    label(150)
    sprite('Hyd901_00', 1)	# 1815-1815
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-500)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('Hyd901_00', 4)	# 1816-1819
    sprite('Hyd901_01', 4)	# 1820-1823
    sprite('Hyd901_02', 4)	# 1824-1827
    gotoLabel(151)
    label(152)
    sprite('Hyd901_03', 5)	# 1828-1832
    sprite('Hyd901_04', 6)	# 1833-1838
    sprite('Hyd901_05', 2)	# 1839-1840
    sprite('Hyd901_06', 5)	# 1841-1845
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 1)	# 1846-1846
    SFX_1('uhy601uwa')
    label(153)
    sprite('Hyd901_07', 1)	# 1847-1847
    if SLOT_97:
        _gotolabel(153)
    sprite('Hyd901_08', 8)	# 1848-1855
    Unknown23018(1)
    sprite('Hyd901_09', 5)	# 1856-1860
    sprite('Hyd901_10', 5)	# 1861-1865
    sprite('Hyd901_11', 5)	# 1866-1870
    sprite('Hyd901_12', 4)	# 1871-1874
    Unknown21011(120)
    label(154)
    sprite('Action_000_00', 7)	# 1875-1881	 **attackbox here**
    sprite('Action_000_01', 7)	# 1882-1888	 **attackbox here**
    sprite('Action_000_02', 6)	# 1889-1894	 **attackbox here**
    sprite('Action_000_03', 6)	# 1895-1900	 **attackbox here**
    sprite('Action_000_04', 5)	# 1901-1905	 **attackbox here**
    sprite('Action_000_05', 5)	# 1906-1910	 **attackbox here**
    sprite('Action_000_06', 5)	# 1911-1915	 **attackbox here**
    sprite('Action_000_07', 6)	# 1916-1921	 **attackbox here**
    sprite('Action_000_08', 6)	# 1922-1927	 **attackbox here**
    sprite('Action_000_09', 7)	# 1928-1934	 **attackbox here**
    sprite('Action_000_10', 7)	# 1935-1941	 **attackbox here**
    sprite('Action_000_11', 6)	# 1942-1947	 **attackbox here**
    sprite('Action_000_12', 6)	# 1948-1953	 **attackbox here**
    sprite('Action_000_13', 5)	# 1954-1958	 **attackbox here**
    sprite('Action_000_14', 5)	# 1959-1963	 **attackbox here**
    sprite('Action_000_15', 5)	# 1964-1968	 **attackbox here**
    sprite('Action_000_16', 6)	# 1969-1974	 **attackbox here**
    sprite('Action_000_17', 6)	# 1975-1980	 **attackbox here**
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('Hyd901_00', 4)	# 1981-1984
    if (not SLOT_158):
        Unknown1000(-1230000)
    sprite('Hyd901_01', 4)	# 1985-1988
    sprite('Hyd901_02', 4)	# 1989-1992
    sprite('Hyd901_00', 4)	# 1993-1996
    sprite('Hyd901_01', 4)	# 1997-2000
    sprite('Hyd901_02', 4)	# 2001-2004
    sprite('Hyd901_00', 4)	# 2005-2008
    sprite('Hyd901_01', 4)	# 2009-2012
    sprite('Hyd901_02', 4)	# 2013-2016
    sprite('Hyd901_00', 4)	# 2017-2020
    sprite('Hyd901_01', 4)	# 2021-2024
    sprite('Hyd901_02', 4)	# 2025-2028
    sprite('Hyd901_03', 5)	# 2029-2033
    sprite('Hyd901_04', 6)	# 2034-2039
    sprite('Hyd901_05', 2)	# 2040-2041
    sprite('Hyd901_06', 5)	# 2042-2046
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 120)	# 2047-2166
    SFX_1('uhy600rrb')
    sprite('Hyd901_08', 8)	# 2167-2174
    sprite('Hyd901_09', 5)	# 2175-2179
    sprite('Hyd901_10', 5)	# 2180-2184
    sprite('Hyd901_11', 5)	# 2185-2189
    sprite('Hyd901_12', 4)	# 2190-2193
    Unknown21007(24, 40)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 7)	# 2194-2200	 **attackbox here**
    sprite('Action_000_01', 7)	# 2201-2207	 **attackbox here**
    sprite('Action_000_02', 6)	# 2208-2213	 **attackbox here**
    sprite('Action_000_03', 6)	# 2214-2219	 **attackbox here**
    sprite('Action_000_04', 5)	# 2220-2224	 **attackbox here**
    sprite('Action_000_05', 5)	# 2225-2229	 **attackbox here**
    sprite('Action_000_06', 5)	# 2230-2234	 **attackbox here**
    sprite('Action_000_07', 6)	# 2235-2240	 **attackbox here**
    sprite('Action_000_08', 6)	# 2241-2246	 **attackbox here**
    sprite('Action_000_09', 7)	# 2247-2253	 **attackbox here**
    sprite('Action_000_10', 7)	# 2254-2260	 **attackbox here**
    sprite('Action_000_11', 6)	# 2261-2266	 **attackbox here**
    sprite('Action_000_12', 6)	# 2267-2272	 **attackbox here**
    sprite('Action_000_13', 5)	# 2273-2277	 **attackbox here**
    sprite('Action_000_14', 5)	# 2278-2282	 **attackbox here**
    sprite('Action_000_15', 5)	# 2283-2287	 **attackbox here**
    sprite('Action_000_16', 6)	# 2288-2293	 **attackbox here**
    sprite('Action_000_17', 6)	# 2294-2299	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Action_000_19', 4)	# 2300-2303
    SFX_1('uhy602rrb')
    sprite('Action_000_20', 8)	# 2304-2311
    sprite('Action_000_21', 11)	# 2312-2322
    sprite('Action_000_22', 5)	# 2323-2327	 **attackbox here**
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffEntryBlade01', 100)
    sprite('Action_000_23', 150)	# 2328-2477	 **attackbox here**
    sprite('Action_000_24', 6)	# 2478-2483	 **attackbox here**
    Unknown23018(1)
    label(163)
    sprite('Action_000_00', 7)	# 2484-2490	 **attackbox here**
    sprite('Action_000_01', 7)	# 2491-2497	 **attackbox here**
    sprite('Action_000_02', 6)	# 2498-2503	 **attackbox here**
    sprite('Action_000_03', 6)	# 2504-2509	 **attackbox here**
    sprite('Action_000_04', 5)	# 2510-2514	 **attackbox here**
    sprite('Action_000_05', 5)	# 2515-2519	 **attackbox here**
    sprite('Action_000_06', 5)	# 2520-2524	 **attackbox here**
    sprite('Action_000_07', 6)	# 2525-2530	 **attackbox here**
    sprite('Action_000_08', 6)	# 2531-2536	 **attackbox here**
    sprite('Action_000_09', 7)	# 2537-2543	 **attackbox here**
    sprite('Action_000_10', 7)	# 2544-2550	 **attackbox here**
    sprite('Action_000_11', 6)	# 2551-2556	 **attackbox here**
    sprite('Action_000_12', 6)	# 2557-2562	 **attackbox here**
    sprite('Action_000_13', 5)	# 2563-2567	 **attackbox here**
    sprite('Action_000_14', 5)	# 2568-2572	 **attackbox here**
    sprite('Action_000_15', 5)	# 2573-2577	 **attackbox here**
    sprite('Action_000_16', 6)	# 2578-2583	 **attackbox here**
    sprite('Action_000_17', 6)	# 2584-2589	 **attackbox here**
    gotoLabel(163)
    ExitState()
    label(170)
    sprite('Action_050_01', 5)	# 2590-2594
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('uhy600pna')
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 2595-2599
    sprite('Action_050_03', 5)	# 2600-2604
    sprite('Action_050_01', 5)	# 2605-2609
    sprite('Action_050_02', 5)	# 2610-2614
    sprite('Action_050_03', 5)	# 2615-2619
    sprite('Action_050_04', 5)	# 2620-2624
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 2625-2628
    sprite('Action_050_06', 4)	# 2629-2632
    sprite('Action_050_07', 3)	# 2633-2635	 **attackbox here**
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 2636-2638	 **attackbox here**
    sprite('Action_050_09', 3)	# 2639-2641	 **attackbox here**
    sprite('Action_050_10', 3)	# 2642-2644	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 2645-2646	 **attackbox here**
    sprite('Action_050_12', 2)	# 2647-2648	 **attackbox here**
    sprite('Action_050_13', 4)	# 2649-2652	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 2653-2655	 **attackbox here**
    sprite('Action_050_15', 3)	# 2656-2658	 **attackbox here**
    sprite('Action_050_16', 4)	# 2659-2662	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 2663-2666	 **attackbox here**
    sprite('Action_050_18', 4)	# 2667-2670	 **attackbox here**
    sprite('Action_050_19', 5)	# 2671-2675	 **attackbox here**
    sprite('Action_050_20', 7)	# 2676-2682
    sprite('Action_050_21', 8)	# 2683-2690
    sprite('Action_050_22', 11)	# 2691-2701
    sprite('Action_050_23', 5)	# 2702-2706	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_050_24', 12)	# 2707-2718	 **attackbox here**
    label(171)
    sprite('Action_050_24', 1)	# 2719-2719	 **attackbox here**
    if SLOT_97:
        _gotolabel(171)
    sprite('Action_050_24', 20)	# 2720-2739	 **attackbox here**
    sprite('Action_050_25', 6)	# 2740-2745	 **attackbox here**
    Unknown21007(24, 40)
    Unknown23018(1)
    label(172)
    sprite('Action_000_00', 7)	# 2746-2752	 **attackbox here**
    sprite('Action_000_01', 7)	# 2753-2759	 **attackbox here**
    sprite('Action_000_02', 6)	# 2760-2765	 **attackbox here**
    sprite('Action_000_03', 6)	# 2766-2771	 **attackbox here**
    sprite('Action_000_04', 5)	# 2772-2776	 **attackbox here**
    sprite('Action_000_05', 5)	# 2777-2781	 **attackbox here**
    sprite('Action_000_06', 5)	# 2782-2786	 **attackbox here**
    sprite('Action_000_07', 6)	# 2787-2792	 **attackbox here**
    sprite('Action_000_08', 6)	# 2793-2798	 **attackbox here**
    sprite('Action_000_09', 7)	# 2799-2805	 **attackbox here**
    sprite('Action_000_10', 7)	# 2806-2812	 **attackbox here**
    sprite('Action_000_11', 6)	# 2813-2818	 **attackbox here**
    sprite('Action_000_12', 6)	# 2819-2824	 **attackbox here**
    sprite('Action_000_13', 5)	# 2825-2829	 **attackbox here**
    sprite('Action_000_14', 5)	# 2830-2834	 **attackbox here**
    sprite('Action_000_15', 5)	# 2835-2839	 **attackbox here**
    sprite('Action_000_16', 6)	# 2840-2845	 **attackbox here**
    sprite('Action_000_17', 6)	# 2846-2851	 **attackbox here**
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('Hyd901_00', 1)	# 2852-2852
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('Hyd901_00', 4)	# 2853-2856
    sprite('Hyd901_01', 4)	# 2857-2860
    sprite('Hyd901_02', 4)	# 2861-2864
    gotoLabel(181)
    label(182)
    sprite('Hyd901_00', 4)	# 2865-2868
    sprite('Hyd901_01', 4)	# 2869-2872
    sprite('Hyd901_02', 4)	# 2873-2876
    sprite('Hyd901_03', 5)	# 2877-2881
    sprite('Hyd901_04', 6)	# 2882-2887
    sprite('Hyd901_05', 2)	# 2888-2889
    sprite('Hyd901_06', 5)	# 2890-2894
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 1)	# 2895-2895
    SFX_1('uhy601rbl')
    label(183)
    sprite('Hyd901_07', 1)	# 2896-2896
    if SLOT_97:
        _gotolabel(183)
    sprite('Hyd901_08', 8)	# 2897-2904
    sprite('Hyd901_09', 5)	# 2905-2909
    sprite('Hyd901_10', 5)	# 2910-2914
    sprite('Hyd901_11', 5)	# 2915-2919
    sprite('Hyd901_12', 4)	# 2920-2923
    Unknown23018(1)
    label(184)
    sprite('Action_000_00', 7)	# 2924-2930	 **attackbox here**
    sprite('Action_000_01', 7)	# 2931-2937	 **attackbox here**
    sprite('Action_000_02', 6)	# 2938-2943	 **attackbox here**
    sprite('Action_000_03', 6)	# 2944-2949	 **attackbox here**
    sprite('Action_000_04', 5)	# 2950-2954	 **attackbox here**
    sprite('Action_000_05', 5)	# 2955-2959	 **attackbox here**
    sprite('Action_000_06', 5)	# 2960-2964	 **attackbox here**
    sprite('Action_000_07', 6)	# 2965-2970	 **attackbox here**
    sprite('Action_000_08', 6)	# 2971-2976	 **attackbox here**
    sprite('Action_000_09', 7)	# 2977-2983	 **attackbox here**
    sprite('Action_000_10', 7)	# 2984-2990	 **attackbox here**
    sprite('Action_000_11', 6)	# 2991-2996	 **attackbox here**
    sprite('Action_000_12', 6)	# 2997-3002	 **attackbox here**
    sprite('Action_000_13', 5)	# 3003-3007	 **attackbox here**
    sprite('Action_000_14', 5)	# 3008-3012	 **attackbox here**
    sprite('Action_000_15', 5)	# 3013-3017	 **attackbox here**
    sprite('Action_000_16', 6)	# 3018-3023	 **attackbox here**
    sprite('Action_000_17', 6)	# 3024-3029	 **attackbox here**
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('Hyd901_00', 1)	# 3030-3030
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Hyd901_00', 4)	# 3031-3034
    sprite('Hyd901_01', 4)	# 3035-3038
    sprite('Hyd901_02', 4)	# 3039-3042
    gotoLabel(191)
    label(192)
    sprite('Hyd901_00', 4)	# 3043-3046
    sprite('Hyd901_01', 4)	# 3047-3050
    sprite('Hyd901_02', 4)	# 3051-3054
    sprite('Hyd901_03', 5)	# 3055-3059
    sprite('Hyd901_04', 6)	# 3060-3065
    sprite('Hyd901_05', 2)	# 3066-3067
    sprite('Hyd901_06', 5)	# 3068-3072
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 1)	# 3073-3073
    SFX_1('uhy601uor')
    label(193)
    sprite('Hyd901_07', 1)	# 3074-3074
    if SLOT_97:
        _gotolabel(193)
    sprite('Hyd901_08', 8)	# 3075-3082
    sprite('Hyd901_09', 5)	# 3083-3087
    sprite('Hyd901_10', 5)	# 3088-3092
    sprite('Hyd901_11', 5)	# 3093-3097
    sprite('Hyd901_12', 4)	# 3098-3101
    Unknown21011(120)
    label(194)
    sprite('Action_000_00', 7)	# 3102-3108	 **attackbox here**
    sprite('Action_000_01', 7)	# 3109-3115	 **attackbox here**
    sprite('Action_000_02', 6)	# 3116-3121	 **attackbox here**
    sprite('Action_000_03', 6)	# 3122-3127	 **attackbox here**
    sprite('Action_000_04', 5)	# 3128-3132	 **attackbox here**
    sprite('Action_000_05', 5)	# 3133-3137	 **attackbox here**
    sprite('Action_000_06', 5)	# 3138-3142	 **attackbox here**
    sprite('Action_000_07', 6)	# 3143-3148	 **attackbox here**
    sprite('Action_000_08', 6)	# 3149-3154	 **attackbox here**
    sprite('Action_000_09', 7)	# 3155-3161	 **attackbox here**
    sprite('Action_000_10', 7)	# 3162-3168	 **attackbox here**
    sprite('Action_000_11', 6)	# 3169-3174	 **attackbox here**
    sprite('Action_000_12', 6)	# 3175-3180	 **attackbox here**
    sprite('Action_000_13', 5)	# 3181-3185	 **attackbox here**
    sprite('Action_000_14', 5)	# 3186-3190	 **attackbox here**
    sprite('Action_000_15', 5)	# 3191-3195	 **attackbox here**
    sprite('Action_000_16', 6)	# 3196-3201	 **attackbox here**
    sprite('Action_000_17', 6)	# 3202-3207	 **attackbox here**
    gotoLabel(194)
    ExitState()
    label(200)
    sprite('Action_050_01', 5)	# 3208-3212
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2037(1)
    else:
        Unknown1000(-1465000)
    SFX_1('uhy600pag')
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 3213-3217
    sprite('Action_050_03', 5)	# 3218-3222
    sprite('Action_050_01', 5)	# 3223-3227
    sprite('Action_050_02', 5)	# 3228-3232
    sprite('Action_050_03', 5)	# 3233-3237
    sprite('Action_050_04', 5)	# 3238-3242
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 3243-3246
    sprite('Action_050_06', 4)	# 3247-3250
    sprite('Action_050_07', 3)	# 3251-3253	 **attackbox here**
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 3254-3256	 **attackbox here**
    sprite('Action_050_09', 3)	# 3257-3259	 **attackbox here**
    sprite('Action_050_10', 3)	# 3260-3262	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 3263-3264	 **attackbox here**
    sprite('Action_050_12', 2)	# 3265-3266	 **attackbox here**
    sprite('Action_050_13', 4)	# 3267-3270	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 3271-3273	 **attackbox here**
    sprite('Action_050_15', 3)	# 3274-3276	 **attackbox here**
    sprite('Action_050_16', 4)	# 3277-3280	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 3281-3284	 **attackbox here**
    sprite('Action_050_18', 4)	# 3285-3288	 **attackbox here**
    sprite('Action_050_19', 5)	# 3289-3293	 **attackbox here**
    sprite('Action_050_20', 7)	# 3294-3300
    sprite('Action_050_21', 8)	# 3301-3308
    sprite('Action_050_22', 11)	# 3309-3319
    sprite('Action_050_23', 5)	# 3320-3324	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    label(201)
    sprite('Action_050_24', 1)	# 3325-3325	 **attackbox here**
    if SLOT_97:
        _gotolabel(201)
    sprite('Action_050_24', 30)	# 3326-3355	 **attackbox here**
    sprite('Action_050_25', 6)	# 3356-3361	 **attackbox here**
    Unknown21007(24, 40)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(203)
    label(202)
    sprite('Action_000_00', 7)	# 3362-3368	 **attackbox here**
    sprite('Action_000_01', 7)	# 3369-3375	 **attackbox here**
    sprite('Action_000_02', 6)	# 3376-3381	 **attackbox here**
    sprite('Action_000_03', 6)	# 3382-3387	 **attackbox here**
    sprite('Action_000_04', 5)	# 3388-3392	 **attackbox here**
    sprite('Action_000_05', 5)	# 3393-3397	 **attackbox here**
    sprite('Action_000_06', 5)	# 3398-3402	 **attackbox here**
    sprite('Action_000_07', 6)	# 3403-3408	 **attackbox here**
    sprite('Action_000_08', 6)	# 3409-3414	 **attackbox here**
    sprite('Action_000_09', 7)	# 3415-3421	 **attackbox here**
    sprite('Action_000_10', 7)	# 3422-3428	 **attackbox here**
    sprite('Action_000_11', 6)	# 3429-3434	 **attackbox here**
    sprite('Action_000_12', 6)	# 3435-3440	 **attackbox here**
    sprite('Action_000_13', 5)	# 3441-3445	 **attackbox here**
    sprite('Action_000_14', 5)	# 3446-3450	 **attackbox here**
    sprite('Action_000_15', 5)	# 3451-3455	 **attackbox here**
    sprite('Action_000_16', 6)	# 3456-3461	 **attackbox here**
    sprite('Action_000_17', 6)	# 3462-3467	 **attackbox here**
    gotoLabel(202)
    label(203)
    sprite('keep', 1)	# 3468-3468
    if (not SLOT_2):
        sendToLabel(204)
    sprite('Action_015_00', 3)	# 3469-3471
    Unknown2005()
    sprite('Action_015_01', 3)	# 3472-3474
    label(204)
    sprite('Action_248_00', 6)	# 3475-3480
    SFX_1('uhy602pag')
    sprite('Action_248_01', 5)	# 3481-3485
    sprite('Action_248_02', 5)	# 3486-3490
    sprite('Action_248_03', 5)	# 3491-3495
    sprite('Action_248_04', 4)	# 3496-3499	 **attackbox here**
    Unknown23018(1)
    label(205)
    sprite('Action_248_04', 6)	# 3500-3505	 **attackbox here**
    sprite('Action_248_05', 6)	# 3506-3511	 **attackbox here**
    sprite('Action_248_06', 6)	# 3512-3517	 **attackbox here**
    loopRest()
    gotoLabel(205)
    ExitState()
    label(210)
    sprite('Action_050_01', 5)	# 3518-3522
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('uhy600uva')
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 3523-3527
    sprite('Action_050_03', 5)	# 3528-3532
    sprite('Action_050_01', 5)	# 3533-3537
    sprite('Action_050_02', 5)	# 3538-3542
    sprite('Action_050_03', 5)	# 3543-3547
    sprite('Action_050_04', 5)	# 3548-3552
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 3553-3556
    sprite('Action_050_06', 4)	# 3557-3560
    sprite('Action_050_07', 3)	# 3561-3563	 **attackbox here**
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 3564-3566	 **attackbox here**
    sprite('Action_050_09', 3)	# 3567-3569	 **attackbox here**
    sprite('Action_050_10', 3)	# 3570-3572	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 3573-3574	 **attackbox here**
    sprite('Action_050_12', 2)	# 3575-3576	 **attackbox here**
    sprite('Action_050_13', 4)	# 3577-3580	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 3581-3583	 **attackbox here**
    sprite('Action_050_15', 3)	# 3584-3586	 **attackbox here**
    sprite('Action_050_16', 4)	# 3587-3590	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 3591-3594	 **attackbox here**
    sprite('Action_050_18', 4)	# 3595-3598	 **attackbox here**
    sprite('Action_050_19', 5)	# 3599-3603	 **attackbox here**
    sprite('Action_050_20', 7)	# 3604-3610
    sprite('Action_050_21', 8)	# 3611-3618
    sprite('Action_050_22', 11)	# 3619-3629
    sprite('Action_050_23', 5)	# 3630-3634	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_050_24', 12)	# 3635-3646	 **attackbox here**
    label(211)
    sprite('Action_050_24', 1)	# 3647-3647	 **attackbox here**
    if SLOT_97:
        _gotolabel(211)
    sprite('Action_050_24', 20)	# 3648-3667	 **attackbox here**
    sprite('Action_050_25', 6)	# 3668-3673	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(212)
    sprite('Action_000_00', 7)	# 3674-3680	 **attackbox here**
    sprite('Action_000_01', 7)	# 3681-3687	 **attackbox here**
    sprite('Action_000_02', 6)	# 3688-3693	 **attackbox here**
    sprite('Action_000_03', 6)	# 3694-3699	 **attackbox here**
    sprite('Action_000_04', 5)	# 3700-3704	 **attackbox here**
    sprite('Action_000_05', 5)	# 3705-3709	 **attackbox here**
    sprite('Action_000_06', 5)	# 3710-3714	 **attackbox here**
    sprite('Action_000_07', 6)	# 3715-3720	 **attackbox here**
    sprite('Action_000_08', 6)	# 3721-3726	 **attackbox here**
    sprite('Action_000_09', 7)	# 3727-3733	 **attackbox here**
    sprite('Action_000_10', 7)	# 3734-3740	 **attackbox here**
    sprite('Action_000_11', 6)	# 3741-3746	 **attackbox here**
    sprite('Action_000_12', 6)	# 3747-3752	 **attackbox here**
    sprite('Action_000_13', 5)	# 3753-3757	 **attackbox here**
    sprite('Action_000_14', 5)	# 3758-3762	 **attackbox here**
    sprite('Action_000_15', 5)	# 3763-3767	 **attackbox here**
    sprite('Action_000_16', 6)	# 3768-3773	 **attackbox here**
    sprite('Action_000_17', 6)	# 3774-3779	 **attackbox here**
    gotoLabel(212)
    ExitState()
    label(220)
    sprite('Hyd901_00', 1)	# 3780-3780
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('Hyd901_00', 4)	# 3781-3784
    sprite('Hyd901_01', 4)	# 3785-3788
    sprite('Hyd901_02', 4)	# 3789-3792
    gotoLabel(221)
    label(222)
    sprite('Hyd901_00', 4)	# 3793-3796
    sprite('Hyd901_01', 4)	# 3797-3800
    sprite('Hyd901_02', 4)	# 3801-3804
    sprite('Hyd901_03', 5)	# 3805-3809
    sprite('Hyd901_04', 6)	# 3810-3815
    sprite('Hyd901_05', 2)	# 3816-3817
    sprite('Hyd901_06', 5)	# 3818-3822
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 1)	# 3823-3823
    SFX_1('uhy601uyu')
    label(223)
    sprite('Hyd901_07', 1)	# 3824-3824
    if SLOT_97:
        _gotolabel(223)
    sprite('Hyd901_08', 8)	# 3825-3832
    sprite('Hyd901_09', 5)	# 3833-3837
    sprite('Hyd901_10', 5)	# 3838-3842
    sprite('Hyd901_11', 5)	# 3843-3847
    sprite('Hyd901_12', 4)	# 3848-3851
    Unknown23018(1)
    label(224)
    sprite('Action_000_00', 7)	# 3852-3858	 **attackbox here**
    sprite('Action_000_01', 7)	# 3859-3865	 **attackbox here**
    sprite('Action_000_02', 6)	# 3866-3871	 **attackbox here**
    sprite('Action_000_03', 6)	# 3872-3877	 **attackbox here**
    sprite('Action_000_04', 5)	# 3878-3882	 **attackbox here**
    sprite('Action_000_05', 5)	# 3883-3887	 **attackbox here**
    sprite('Action_000_06', 5)	# 3888-3892	 **attackbox here**
    sprite('Action_000_07', 6)	# 3893-3898	 **attackbox here**
    sprite('Action_000_08', 6)	# 3899-3904	 **attackbox here**
    sprite('Action_000_09', 7)	# 3905-3911	 **attackbox here**
    sprite('Action_000_10', 7)	# 3912-3918	 **attackbox here**
    sprite('Action_000_11', 6)	# 3919-3924	 **attackbox here**
    sprite('Action_000_12', 6)	# 3925-3930	 **attackbox here**
    sprite('Action_000_13', 5)	# 3931-3935	 **attackbox here**
    sprite('Action_000_14', 5)	# 3936-3940	 **attackbox here**
    sprite('Action_000_15', 5)	# 3941-3945	 **attackbox here**
    sprite('Action_000_16', 6)	# 3946-3951	 **attackbox here**
    sprite('Action_000_17', 6)	# 3952-3957	 **attackbox here**
    gotoLabel(224)
    ExitState()
    label(230)
    sprite('Action_050_01', 5)	# 3958-3962
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)
    SFX_1('uhy600bma')
    GFX_0('EffEntryBlade_Summon1', 100)
    sprite('Action_050_02', 5)	# 3963-3967
    sprite('Action_050_03', 5)	# 3968-3972
    sprite('Action_050_01', 5)	# 3973-3977
    sprite('Action_050_02', 5)	# 3978-3982
    sprite('Action_050_03', 5)	# 3983-3987
    sprite('Action_050_04', 5)	# 3988-3992
    SFX_3('SE_ApperLightBlade')
    sprite('Action_050_05', 4)	# 3993-3996
    sprite('Action_050_06', 4)	# 3997-4000
    sprite('Action_050_07', 3)	# 4001-4003	 **attackbox here**
    Unknown26('EffEntryBlade_Summon1')
    GFX_0('EffEntryBlade_Summon2', 100)
    sprite('Action_050_08', 3)	# 4004-4006	 **attackbox here**
    sprite('Action_050_09', 3)	# 4007-4009	 **attackbox here**
    sprite('Action_050_10', 3)	# 4010-4012	 **attackbox here**
    Unknown26('EffEntryBlade_Summon2')
    GFX_0('EffEntryBlade_Summon3', 100)
    sprite('Action_050_11', 2)	# 4013-4014	 **attackbox here**
    sprite('Action_050_12', 2)	# 4015-4016	 **attackbox here**
    sprite('Action_050_13', 4)	# 4017-4020	 **attackbox here**
    Unknown26('EffEntryBlade_Summon3')
    GFX_0('EffEntryBlade_Summon4', 100)
    sprite('Action_050_14', 3)	# 4021-4023	 **attackbox here**
    sprite('Action_050_15', 3)	# 4024-4026	 **attackbox here**
    sprite('Action_050_16', 4)	# 4027-4030	 **attackbox here**
    Unknown26('EffEntryBlade_Summon4')
    GFX_0('EffEntryBlade_Summon5', 100)
    sprite('Action_050_17', 4)	# 4031-4034	 **attackbox here**
    sprite('Action_050_18', 4)	# 4035-4038	 **attackbox here**
    sprite('Action_050_19', 5)	# 4039-4043	 **attackbox here**
    sprite('Action_050_20', 7)	# 4044-4050
    sprite('Action_050_21', 8)	# 4051-4058
    sprite('Action_050_22', 11)	# 4059-4069
    sprite('Action_050_23', 5)	# 4070-4074	 **attackbox here**
    GFX_0('EffEntryBlade01', 100)
    SFX_3('SE_InsulatorSwingB')
    sprite('Action_050_24', 12)	# 4075-4086	 **attackbox here**
    label(231)
    sprite('Action_050_24', 1)	# 4087-4087	 **attackbox here**
    if SLOT_97:
        _gotolabel(231)
    sprite('Action_050_25', 6)	# 4088-4093	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(360)
    label(232)
    sprite('Action_000_00', 7)	# 4094-4100	 **attackbox here**
    sprite('Action_000_01', 7)	# 4101-4107	 **attackbox here**
    sprite('Action_000_02', 6)	# 4108-4113	 **attackbox here**
    sprite('Action_000_03', 6)	# 4114-4119	 **attackbox here**
    sprite('Action_000_04', 5)	# 4120-4124	 **attackbox here**
    sprite('Action_000_05', 5)	# 4125-4129	 **attackbox here**
    sprite('Action_000_06', 5)	# 4130-4134	 **attackbox here**
    sprite('Action_000_07', 6)	# 4135-4140	 **attackbox here**
    sprite('Action_000_08', 6)	# 4141-4146	 **attackbox here**
    sprite('Action_000_09', 7)	# 4147-4153	 **attackbox here**
    sprite('Action_000_10', 7)	# 4154-4160	 **attackbox here**
    sprite('Action_000_11', 6)	# 4161-4166	 **attackbox here**
    sprite('Action_000_12', 6)	# 4167-4172	 **attackbox here**
    sprite('Action_000_13', 5)	# 4173-4177	 **attackbox here**
    sprite('Action_000_14', 5)	# 4178-4182	 **attackbox here**
    sprite('Action_000_15', 5)	# 4183-4187	 **attackbox here**
    sprite('Action_000_16', 6)	# 4188-4193	 **attackbox here**
    sprite('Action_000_17', 6)	# 4194-4199	 **attackbox here**
    gotoLabel(232)
    ExitState()
    label(240)
    sprite('Action_000_00', 1)	# 4200-4200	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    label(241)
    sprite('Action_000_00', 7)	# 4201-4207	 **attackbox here**
    sprite('Action_000_01', 7)	# 4208-4214	 **attackbox here**
    sprite('Action_000_02', 6)	# 4215-4220	 **attackbox here**
    sprite('Action_000_03', 6)	# 4221-4226	 **attackbox here**
    sprite('Action_000_04', 5)	# 4227-4231	 **attackbox here**
    sprite('Action_000_05', 5)	# 4232-4236	 **attackbox here**
    sprite('Action_000_06', 5)	# 4237-4241	 **attackbox here**
    sprite('Action_000_07', 6)	# 4242-4247	 **attackbox here**
    sprite('Action_000_08', 6)	# 4248-4253	 **attackbox here**
    sprite('Action_000_09', 7)	# 4254-4260	 **attackbox here**
    sprite('Action_000_10', 7)	# 4261-4267	 **attackbox here**
    sprite('Action_000_11', 6)	# 4268-4273	 **attackbox here**
    sprite('Action_000_12', 6)	# 4274-4279	 **attackbox here**
    sprite('Action_000_13', 5)	# 4280-4284	 **attackbox here**
    sprite('Action_000_14', 5)	# 4285-4289	 **attackbox here**
    sprite('Action_000_15', 5)	# 4290-4294	 **attackbox here**
    sprite('Action_000_16', 6)	# 4295-4300	 **attackbox here**
    sprite('Action_000_17', 6)	# 4301-4306	 **attackbox here**
    gotoLabel(241)
    label(242)
    sprite('keep', 1)	# 4307-4307
    if (not SLOT_158):
        sendToLabel(243)
    sprite('Action_015_00', 3)	# 4308-4310
    Unknown2005()
    sprite('Action_015_01', 3)	# 4311-4313
    label(243)
    sprite('Action_248_00', 6)	# 4314-4319
    sprite('Action_248_01', 5)	# 4320-4324
    sprite('Action_248_02', 5)	# 4325-4329
    sprite('Action_248_03', 5)	# 4330-4334
    sprite('Action_248_04', 4)	# 4335-4338	 **attackbox here**
    SFX_1('uhy601ahe')
    Unknown23018(1)
    label(245)
    sprite('Action_248_04', 6)	# 4339-4344	 **attackbox here**
    sprite('Action_248_05', 6)	# 4345-4350	 **attackbox here**
    sprite('Action_248_06', 6)	# 4351-4356	 **attackbox here**
    sprite('Action_248_05', 6)	# 4357-4362	 **attackbox here**
    loopRest()
    gotoLabel(245)
    ExitState()
    label(250)
    sprite('Hyd901_00', 1)	# 4363-4363
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(-1000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(252)
    label(251)
    sprite('Hyd901_00', 4)	# 4364-4367
    sprite('Hyd901_01', 4)	# 4368-4371
    sprite('Hyd901_02', 4)	# 4372-4375
    gotoLabel(251)
    label(252)
    sprite('Hyd901_00', 4)	# 4376-4379
    sprite('Hyd901_01', 4)	# 4380-4383
    sprite('Hyd901_02', 4)	# 4384-4387
    sprite('Hyd901_03', 5)	# 4388-4392
    sprite('Hyd901_04', 6)	# 4393-4398
    sprite('Hyd901_05', 2)	# 4399-4400
    sprite('Hyd901_06', 5)	# 4401-4405
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 53)	# 4406-4458
    SFX_1('uhy601uak')
    sprite('Hyd901_08', 8)	# 4459-4466
    sprite('Hyd901_09', 5)	# 4467-4471
    sprite('Hyd901_10', 5)	# 4472-4476
    sprite('Hyd901_11', 5)	# 4477-4481
    sprite('Hyd901_12', 4)	# 4482-4485
    Unknown23018(1)
    label(253)
    sprite('Action_000_00', 7)	# 4486-4492	 **attackbox here**
    sprite('Action_000_01', 7)	# 4493-4499	 **attackbox here**
    sprite('Action_000_02', 6)	# 4500-4505	 **attackbox here**
    sprite('Action_000_03', 6)	# 4506-4511	 **attackbox here**
    sprite('Action_000_04', 5)	# 4512-4516	 **attackbox here**
    sprite('Action_000_05', 5)	# 4517-4521	 **attackbox here**
    sprite('Action_000_06', 5)	# 4522-4526	 **attackbox here**
    sprite('Action_000_07', 6)	# 4527-4532	 **attackbox here**
    sprite('Action_000_08', 6)	# 4533-4538	 **attackbox here**
    sprite('Action_000_09', 7)	# 4539-4545	 **attackbox here**
    sprite('Action_000_10', 7)	# 4546-4552	 **attackbox here**
    sprite('Action_000_11', 6)	# 4553-4558	 **attackbox here**
    sprite('Action_000_12', 6)	# 4559-4564	 **attackbox here**
    sprite('Action_000_13', 5)	# 4565-4569	 **attackbox here**
    sprite('Action_000_14', 5)	# 4570-4574	 **attackbox here**
    sprite('Action_000_15', 5)	# 4575-4579	 **attackbox here**
    sprite('Action_000_16', 6)	# 4580-4585	 **attackbox here**
    sprite('Action_000_17', 6)	# 4586-4591	 **attackbox here**
    gotoLabel(253)
    ExitState()
    label(260)
    sprite('Hyd901_00', 1)	# 4592-4592
    Unknown1000(-1230000)
    Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(262)
    label(261)
    sprite('Hyd901_00', 4)	# 4593-4596
    sprite('Hyd901_01', 4)	# 4597-4600
    sprite('Hyd901_02', 4)	# 4601-4604
    gotoLabel(261)
    label(262)
    sprite('Hyd901_00', 4)	# 4605-4608
    sprite('Hyd901_01', 4)	# 4609-4612
    sprite('Hyd901_02', 4)	# 4613-4616
    sprite('Hyd901_03', 5)	# 4617-4621
    sprite('Hyd901_04', 6)	# 4622-4627
    sprite('Hyd901_05', 2)	# 4628-4629
    sprite('Hyd901_06', 5)	# 4630-4634
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 78)	# 4635-4712
    SFX_1('uhy601uhi')
    sprite('Hyd901_08', 8)	# 4713-4720
    sprite('Hyd901_09', 5)	# 4721-4725
    sprite('Hyd901_10', 5)	# 4726-4730
    sprite('Hyd901_11', 5)	# 4731-4735
    sprite('Hyd901_12', 4)	# 4736-4739
    Unknown23018(1)
    label(263)
    sprite('Action_000_00', 7)	# 4740-4746	 **attackbox here**
    sprite('Action_000_01', 7)	# 4747-4753	 **attackbox here**
    sprite('Action_000_02', 6)	# 4754-4759	 **attackbox here**
    sprite('Action_000_03', 6)	# 4760-4765	 **attackbox here**
    sprite('Action_000_04', 5)	# 4766-4770	 **attackbox here**
    sprite('Action_000_05', 5)	# 4771-4775	 **attackbox here**
    sprite('Action_000_06', 5)	# 4776-4780	 **attackbox here**
    sprite('Action_000_07', 6)	# 4781-4786	 **attackbox here**
    sprite('Action_000_08', 6)	# 4787-4792	 **attackbox here**
    sprite('Action_000_09', 7)	# 4793-4799	 **attackbox here**
    sprite('Action_000_10', 7)	# 4800-4806	 **attackbox here**
    sprite('Action_000_11', 6)	# 4807-4812	 **attackbox here**
    sprite('Action_000_12', 6)	# 4813-4818	 **attackbox here**
    sprite('Action_000_13', 5)	# 4819-4823	 **attackbox here**
    sprite('Action_000_14', 5)	# 4824-4828	 **attackbox here**
    sprite('Action_000_15', 5)	# 4829-4833	 **attackbox here**
    sprite('Action_000_16', 6)	# 4834-4839	 **attackbox here**
    sprite('Action_000_17', 6)	# 4840-4845	 **attackbox here**
    gotoLabel(263)
    ExitState()
    label(270)
    sprite('Hyd901_00', 1)	# 4846-4846
    Unknown1000(-1230000)
    Unknown2019(-1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(272)
    label(271)
    sprite('Hyd901_00', 4)	# 4847-4850
    sprite('Hyd901_01', 4)	# 4851-4854
    sprite('Hyd901_02', 4)	# 4855-4858
    gotoLabel(271)
    label(272)
    sprite('Hyd901_00', 4)	# 4859-4862
    sprite('Hyd901_01', 4)	# 4863-4866
    sprite('Hyd901_02', 4)	# 4867-4870
    sprite('Hyd901_03', 5)	# 4871-4875
    sprite('Hyd901_04', 6)	# 4876-4881
    sprite('Hyd901_05', 2)	# 4882-4883
    sprite('Hyd901_06', 5)	# 4884-4888
    SFX_3('SE_InsulatorSwingB')
    sprite('Hyd901_07', 28)	# 4889-4916
    SFX_1('uhy601pad')
    Unknown23018(1)
    sprite('Hyd901_08', 8)	# 4917-4924
    sprite('Hyd901_09', 5)	# 4925-4929
    sprite('Hyd901_10', 5)	# 4930-4934
    sprite('Hyd901_11', 5)	# 4935-4939
    sprite('Hyd901_12', 4)	# 4940-4943
    label(273)
    sprite('Action_000_00', 7)	# 4944-4950	 **attackbox here**
    sprite('Action_000_01', 7)	# 4951-4957	 **attackbox here**
    sprite('Action_000_02', 6)	# 4958-4963	 **attackbox here**
    sprite('Action_000_03', 6)	# 4964-4969	 **attackbox here**
    sprite('Action_000_04', 5)	# 4970-4974	 **attackbox here**
    sprite('Action_000_05', 5)	# 4975-4979	 **attackbox here**
    sprite('Action_000_06', 5)	# 4980-4984	 **attackbox here**
    sprite('Action_000_07', 6)	# 4985-4990	 **attackbox here**
    sprite('Action_000_08', 6)	# 4991-4996	 **attackbox here**
    sprite('Action_000_09', 7)	# 4997-5003	 **attackbox here**
    sprite('Action_000_10', 7)	# 5004-5010	 **attackbox here**
    sprite('Action_000_11', 6)	# 5011-5016	 **attackbox here**
    sprite('Action_000_12', 6)	# 5017-5022	 **attackbox here**
    sprite('Action_000_13', 5)	# 5023-5027	 **attackbox here**
    sprite('Action_000_14', 5)	# 5028-5032	 **attackbox here**
    sprite('Action_000_15', 5)	# 5033-5037	 **attackbox here**
    sprite('Action_000_16', 6)	# 5038-5043	 **attackbox here**
    sprite('Action_000_17', 6)	# 5044-5049	 **attackbox here**
    gotoLabel(273)
    ExitState()
    label(280)
    sprite('Action_000_00', 1)	# 5050-5050	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(282)
    label(281)
    sprite('Action_000_00', 7)	# 5051-5057	 **attackbox here**
    sprite('Action_000_01', 7)	# 5058-5064	 **attackbox here**
    sprite('Action_000_02', 6)	# 5065-5070	 **attackbox here**
    sprite('Action_000_03', 6)	# 5071-5076	 **attackbox here**
    sprite('Action_000_04', 5)	# 5077-5081	 **attackbox here**
    sprite('Action_000_05', 5)	# 5082-5086	 **attackbox here**
    sprite('Action_000_06', 5)	# 5087-5091	 **attackbox here**
    sprite('Action_000_07', 6)	# 5092-5097	 **attackbox here**
    sprite('Action_000_08', 6)	# 5098-5103	 **attackbox here**
    sprite('Action_000_09', 7)	# 5104-5110	 **attackbox here**
    sprite('Action_000_10', 7)	# 5111-5117	 **attackbox here**
    sprite('Action_000_11', 6)	# 5118-5123	 **attackbox here**
    sprite('Action_000_12', 6)	# 5124-5129	 **attackbox here**
    sprite('Action_000_13', 5)	# 5130-5134	 **attackbox here**
    sprite('Action_000_14', 5)	# 5135-5139	 **attackbox here**
    sprite('Action_000_15', 5)	# 5140-5144	 **attackbox here**
    sprite('Action_000_16', 6)	# 5145-5150	 **attackbox here**
    sprite('Action_000_17', 6)	# 5151-5156	 **attackbox here**
    gotoLabel(281)
    label(282)
    sprite('Action_000_19', 4)	# 5157-5160
    sprite('Action_000_20', 8)	# 5161-5168
    SFX_1('uhy601kym')
    sprite('Action_000_21', 11)	# 5169-5179
    sprite('Action_000_22', 5)	# 5180-5184	 **attackbox here**
    sprite('Action_000_23', 12)	# 5185-5196	 **attackbox here**
    sprite('Action_000_24', 6)	# 5197-5202	 **attackbox here**
    sprite('Action_000_00', 7)	# 5203-5209	 **attackbox here**
    sprite('Action_000_01', 7)	# 5210-5216	 **attackbox here**
    sprite('Action_000_02', 6)	# 5217-5222	 **attackbox here**
    sprite('Action_000_03', 6)	# 5223-5228	 **attackbox here**
    sprite('Action_000_04', 5)	# 5229-5233	 **attackbox here**
    sprite('Action_000_05', 5)	# 5234-5238	 **attackbox here**
    sprite('Action_000_06', 5)	# 5239-5243	 **attackbox here**
    sprite('Action_000_07', 6)	# 5244-5249	 **attackbox here**
    sprite('Action_000_08', 6)	# 5250-5255	 **attackbox here**
    if (not SLOT_158):
        sendToLabel(283)
    sprite('Action_015_00', 3)	# 5256-5258
    Unknown2005()
    sprite('Action_015_01', 3)	# 5259-5261
    label(283)
    sprite('Action_248_00', 6)	# 5262-5267
    sprite('Action_248_01', 5)	# 5268-5272
    sprite('Action_248_02', 5)	# 5273-5277
    sprite('Action_248_03', 5)	# 5278-5282
    sprite('Action_248_04', 4)	# 5283-5286	 **attackbox here**
    Unknown23018(1)
    label(284)
    sprite('Action_248_04', 6)	# 5287-5292	 **attackbox here**
    sprite('Action_248_05', 6)	# 5293-5298	 **attackbox here**
    sprite('Action_248_06', 6)	# 5299-5304	 **attackbox here**
    sprite('Action_248_05', 6)	# 5305-5310	 **attackbox here**
    loopRest()
    gotoLabel(284)
    ExitState()
    label(290)
    sprite('Hyd654_00', 6)	# 5311-5316	 **attackbox here**
    Unknown1000(-1230000)
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(292)
    label(291)
    sprite('Hyd654_01', 6)	# 5317-5322	 **attackbox here**
    sprite('Hyd654_02', 6)	# 5323-5328	 **attackbox here**
    sprite('Hyd654_03', 6)	# 5329-5334	 **attackbox here**
    sprite('Hyd654_00', 6)	# 5335-5340	 **attackbox here**
    gotoLabel(291)
    label(292)
    sprite('Hyd654_04', 6)	# 5341-5346
    SFX_1('uhy601use')
    Unknown23018(1)
    label(293)
    sprite('Hyd654_05', 6)	# 5347-5352	 **attackbox here**
    sprite('Hyd654_06', 6)	# 5353-5358	 **attackbox here**
    sprite('Hyd654_07', 6)	# 5359-5364	 **attackbox here**
    sprite('Hyd654_08', 6)	# 5365-5370	 **attackbox here**
    gotoLabel(293)
    label(991)
    sprite('Action_000_00', 1)	# 5371-5371	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 7)	# 5372-5378	 **attackbox here**
    sprite('Action_000_01', 7)	# 5379-5385	 **attackbox here**
    sprite('Action_000_02', 6)	# 5386-5391	 **attackbox here**
    sprite('Action_000_03', 6)	# 5392-5397	 **attackbox here**
    sprite('Action_000_04', 5)	# 5398-5402	 **attackbox here**
    sprite('Action_000_05', 5)	# 5403-5407	 **attackbox here**
    sprite('Action_000_06', 5)	# 5408-5412	 **attackbox here**
    sprite('Action_000_07', 6)	# 5413-5418	 **attackbox here**
    sprite('Action_000_08', 6)	# 5419-5424	 **attackbox here**
    sprite('Action_000_09', 7)	# 5425-5431	 **attackbox here**
    sprite('Action_000_10', 7)	# 5432-5438	 **attackbox here**
    sprite('Action_000_11', 6)	# 5439-5444	 **attackbox here**
    sprite('Action_000_12', 6)	# 5445-5450	 **attackbox here**
    sprite('Action_000_13', 5)	# 5451-5455	 **attackbox here**
    sprite('Action_000_14', 5)	# 5456-5460	 **attackbox here**
    sprite('Action_000_15', 5)	# 5461-5465	 **attackbox here**
    sprite('Action_000_16', 6)	# 5466-5471	 **attackbox here**
    sprite('Action_000_17', 6)	# 5472-5477	 **attackbox here**
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 5478-5479

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
    label(994)
    sprite('Action_046_01', 2)	# 5480-5481
    sprite('Action_046_02', 1)	# 5482-5482
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 5483-5485
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
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('pag'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('uyu'):
                if (SLOT_145 <= 900000):
                    if (SLOT_145 >= 100000):
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
            if PartnerChar('uak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(250)
                    clearUponHandler(3)
            if PartnerChar('uhi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(260)
                    clearUponHandler(3)
            if PartnerChar('pad'):
                if (SLOT_145 <= 500000):
                    sendToLabel(270)
                    clearUponHandler(3)
            if PartnerChar('kym'):
                if (SLOT_145 <= 500000):
                    sendToLabel(280)
                    clearUponHandler(3)
            if PartnerChar('use'):
                if (SLOT_145 <= 500000):
                    sendToLabel(290)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    sprite('Action_052_00', 5)	# 4-8
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 9-13
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 14-18
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 19-26
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uhy524', 100, 897149045, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uhy402_0', 100, 880371829, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uhy520', 100, 897149045, 12594, 0, 0, 100, 897149045, 12850, 0, 0, 100, 897149045, 13106, 0, 0, 100)
    sprite('Action_052_04', 7)	# 27-33
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 34-38
    sprite('Action_052_06', 15)	# 39-53
    sprite('Action_052_07', 7)	# 54-60
    sprite('Action_052_08', 3)	# 61-63
    sprite('Action_052_09', 8)	# 64-71	 **attackbox here**
    sprite('Action_052_10', 3)	# 72-74	 **attackbox here**
    Unknown23018(1)
    sprite('Action_052_11', 8)	# 75-82	 **attackbox here**
    label(998)
    sprite('Action_052_12', 5)	# 83-87	 **attackbox here**
    loopRest()
    gotoLabel(998)
    label(10)
    sprite('Hyd960_00', 5)	# 88-92
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uhy524', 100, 897149045, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uhy402_0', 100, 880371829, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uhy520', 100, 897149045, 12850, 0, 0, 100, 897149045, 13106, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Hyd960_01', 7)	# 93-99
    sprite('Hyd960_02', 7)	# 100-106	 **attackbox here**
    sprite('Hyd960_03', 9)	# 107-115	 **attackbox here**
    sprite('Hyd960_04', 4)	# 116-119	 **attackbox here**
    SFX_3('SE010')
    Unknown23018(1)
    label(11)
    sprite('Hyd960_05', 5)	# 120-124	 **attackbox here**
    sprite('Hyd960_06', 5)	# 125-129	 **attackbox here**
    sprite('Hyd960_07', 5)	# 130-134	 **attackbox here**
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('Action_052_00', 5)	# 135-139
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 140-144
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 145-149
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 150-157
    SFX_1('uhy700brg')
    sprite('Action_052_04', 7)	# 158-164
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 165-169
    sprite('Action_052_06', 15)	# 170-184
    sprite('Action_052_07', 7)	# 185-191
    sprite('Action_052_08', 3)	# 192-194
    sprite('Action_052_09', 8)	# 195-202	 **attackbox here**
    sprite('Action_052_10', 3)	# 203-205	 **attackbox here**
    sprite('Action_052_11', 8)	# 206-213	 **attackbox here**
    label(101)
    sprite('Action_052_12', 1)	# 214-214	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_052_12', 32767)	# 215-32981	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(250)
    label(110)
    sprite('Action_000_00', 1)	# 32982-32982	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 7)	# 32983-32989	 **attackbox here**
    sprite('Action_000_01', 7)	# 32990-32996	 **attackbox here**
    sprite('Action_000_02', 6)	# 32997-33002	 **attackbox here**
    sprite('Action_000_03', 6)	# 33003-33008	 **attackbox here**
    sprite('Action_000_04', 5)	# 33009-33013	 **attackbox here**
    sprite('Action_000_05', 5)	# 33014-33018	 **attackbox here**
    sprite('Action_000_06', 5)	# 33019-33023	 **attackbox here**
    sprite('Action_000_07', 6)	# 33024-33029	 **attackbox here**
    sprite('Action_000_08', 6)	# 33030-33035	 **attackbox here**
    sprite('Action_000_09', 7)	# 33036-33042	 **attackbox here**
    sprite('Action_000_10', 7)	# 33043-33049	 **attackbox here**
    sprite('Action_000_11', 6)	# 33050-33055	 **attackbox here**
    sprite('Action_000_12', 6)	# 33056-33061	 **attackbox here**
    sprite('Action_000_13', 5)	# 33062-33066	 **attackbox here**
    sprite('Action_000_14', 5)	# 33067-33071	 **attackbox here**
    sprite('Action_000_15', 5)	# 33072-33076	 **attackbox here**
    sprite('Action_000_16', 6)	# 33077-33082	 **attackbox here**
    sprite('Action_000_17', 6)	# 33083-33088	 **attackbox here**
    gotoLabel(111)
    label(112)
    sprite('Action_052_00', 5)	# 33089-33093
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 33094-33098
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 33099-33103
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 33104-33111
    SFX_1('uhy701bno')
    sprite('Action_052_04', 7)	# 33112-33118
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 33119-33123
    sprite('Action_052_06', 15)	# 33124-33138
    sprite('Action_052_07', 7)	# 33139-33145
    sprite('Action_052_08', 3)	# 33146-33148
    sprite('Action_052_09', 8)	# 33149-33156	 **attackbox here**
    sprite('Action_052_10', 3)	# 33157-33159	 **attackbox here**
    sprite('Action_052_11', 8)	# 33160-33167	 **attackbox here**
    Unknown23018(1)
    label(113)
    sprite('Action_052_12', 5)	# 33168-33172	 **attackbox here**
    gotoLabel(113)
    label(120)
    sprite('Action_052_00', 5)	# 33173-33177
    Unknown2019(-500)
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 33178-33182
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 33183-33187
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 33188-33195
    SFX_1('uhy700btg')
    sprite('Action_052_04', 7)	# 33196-33202
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 33203-33207
    sprite('Action_052_06', 15)	# 33208-33222
    sprite('Action_052_07', 7)	# 33223-33229
    sprite('Action_052_08', 3)	# 33230-33232
    sprite('Action_052_09', 8)	# 33233-33240	 **attackbox here**
    sprite('Action_052_10', 3)	# 33241-33243	 **attackbox here**
    sprite('Action_052_11', 8)	# 33244-33251	 **attackbox here**
    label(121)
    sprite('Action_052_12', 1)	# 33252-33252	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_052_12', 30)	# 33253-33282	 **attackbox here**
    sprite('Action_052_12', 32767)	# 33283-66049	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(160)
    label(130)
    sprite('Action_052_00', 5)	# 66050-66054
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 66055-66059
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 66060-66064
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 66065-66072
    SFX_1('uhy700pbc')
    sprite('Action_052_04', 7)	# 66073-66079
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 66080-66084
    sprite('Action_052_06', 15)	# 66085-66099
    sprite('Action_052_07', 7)	# 66100-66106
    sprite('Action_052_08', 3)	# 66107-66109
    sprite('Action_052_09', 8)	# 66110-66117	 **attackbox here**
    sprite('Action_052_10', 3)	# 66118-66120	 **attackbox here**
    sprite('Action_052_11', 8)	# 66121-66128	 **attackbox here**
    label(131)
    sprite('Action_052_12', 1)	# 66129-66129	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_052_12', 30)	# 66130-66159	 **attackbox here**
    sprite('Action_052_12', 32767)	# 66160-98926	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(280)
    label(140)
    sprite('Hyd960_00', 5)	# 98927-98931
    SFX_1('uhy700pna')
    sprite('Hyd960_01', 7)	# 98932-98938
    sprite('Hyd960_02', 7)	# 98939-98945	 **attackbox here**
    sprite('Hyd960_03', 9)	# 98946-98954	 **attackbox here**
    sprite('Hyd960_04', 4)	# 98955-98958	 **attackbox here**
    SFX_3('SE010')
    label(141)
    sprite('Hyd960_05', 5)	# 98959-98963	 **attackbox here**
    sprite('Hyd960_06', 5)	# 98964-98968	 **attackbox here**
    sprite('Hyd960_07', 5)	# 98969-98973	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('Hyd960_07', 1)	# 98974-98974	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(360)
    label(142)
    sprite('Hyd960_05', 5)	# 98975-98979	 **attackbox here**
    sprite('Hyd960_06', 5)	# 98980-98984	 **attackbox here**
    sprite('Hyd960_07', 5)	# 98985-98989	 **attackbox here**
    gotoLabel(142)
    label(150)
    sprite('Action_052_00', 5)	# 98990-98994
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 98995-98999
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 99000-99004
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 99005-99012
    SFX_1('uhy700uwa')
    sprite('Action_052_04', 7)	# 99013-99019
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 99020-99024
    sprite('Action_052_06', 15)	# 99025-99039
    sprite('Action_052_07', 7)	# 99040-99046
    sprite('Action_052_08', 3)	# 99047-99049
    sprite('Action_052_09', 8)	# 99050-99057	 **attackbox here**
    sprite('Action_052_10', 3)	# 99058-99060	 **attackbox here**
    sprite('Action_052_11', 8)	# 99061-99068	 **attackbox here**
    label(151)
    sprite('Action_052_12', 1)	# 99069-99069	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('Action_052_12', 30)	# 99070-99099	 **attackbox here**
    sprite('Action_052_12', 32767)	# 99100-131866	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(260)
    label(160)
    sprite('Action_000_00', 1)	# 131867-131867	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 7)	# 131868-131874	 **attackbox here**
    sprite('Action_000_01', 7)	# 131875-131881	 **attackbox here**
    sprite('Action_000_02', 6)	# 131882-131887	 **attackbox here**
    sprite('Action_000_03', 6)	# 131888-131893	 **attackbox here**
    sprite('Action_000_04', 5)	# 131894-131898	 **attackbox here**
    sprite('Action_000_05', 5)	# 131899-131903	 **attackbox here**
    sprite('Action_000_06', 5)	# 131904-131908	 **attackbox here**
    sprite('Action_000_07', 6)	# 131909-131914	 **attackbox here**
    sprite('Action_000_08', 6)	# 131915-131920	 **attackbox here**
    sprite('Action_000_09', 7)	# 131921-131927	 **attackbox here**
    sprite('Action_000_10', 7)	# 131928-131934	 **attackbox here**
    sprite('Action_000_11', 6)	# 131935-131940	 **attackbox here**
    sprite('Action_000_12', 6)	# 131941-131946	 **attackbox here**
    sprite('Action_000_13', 5)	# 131947-131951	 **attackbox here**
    sprite('Action_000_14', 5)	# 131952-131956	 **attackbox here**
    sprite('Action_000_15', 5)	# 131957-131961	 **attackbox here**
    sprite('Action_000_16', 6)	# 131962-131967	 **attackbox here**
    sprite('Action_000_17', 6)	# 131968-131973	 **attackbox here**
    gotoLabel(161)
    label(162)
    sprite('Hyd960_00', 5)	# 131974-131978
    SFX_1('uhy701uli')
    sprite('Hyd960_01', 7)	# 131979-131985
    sprite('Hyd960_02', 7)	# 131986-131992	 **attackbox here**
    sprite('Hyd960_03', 9)	# 131993-132001	 **attackbox here**
    sprite('Hyd960_04', 4)	# 132002-132005	 **attackbox here**
    SFX_3('SE010')
    Unknown23018(1)
    label(163)
    sprite('Hyd960_05', 5)	# 132006-132010	 **attackbox here**
    sprite('Hyd960_06', 5)	# 132011-132015	 **attackbox here**
    sprite('Hyd960_07', 5)	# 132016-132020	 **attackbox here**
    loopRest()
    gotoLabel(163)
    label(170)
    sprite('Action_000_00', 1)	# 132021-132021	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_00', 7)	# 132022-132028	 **attackbox here**
    sprite('Action_000_01', 7)	# 132029-132035	 **attackbox here**
    sprite('Action_000_02', 6)	# 132036-132041	 **attackbox here**
    sprite('Action_000_03', 6)	# 132042-132047	 **attackbox here**
    sprite('Action_000_04', 5)	# 132048-132052	 **attackbox here**
    sprite('Action_000_05', 5)	# 132053-132057	 **attackbox here**
    sprite('Action_000_06', 5)	# 132058-132062	 **attackbox here**
    sprite('Action_000_07', 6)	# 132063-132068	 **attackbox here**
    sprite('Action_000_08', 6)	# 132069-132074	 **attackbox here**
    sprite('Action_000_09', 7)	# 132075-132081	 **attackbox here**
    sprite('Action_000_10', 7)	# 132082-132088	 **attackbox here**
    sprite('Action_000_11', 6)	# 132089-132094	 **attackbox here**
    sprite('Action_000_12', 6)	# 132095-132100	 **attackbox here**
    sprite('Action_000_13', 5)	# 132101-132105	 **attackbox here**
    sprite('Action_000_14', 5)	# 132106-132110	 **attackbox here**
    sprite('Action_000_15', 5)	# 132111-132115	 **attackbox here**
    sprite('Action_000_16', 6)	# 132116-132121	 **attackbox here**
    sprite('Action_000_17', 6)	# 132122-132127	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_052_00', 5)	# 132128-132132
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 132133-132137
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 132138-132142
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 132143-132150
    SFX_1('uhy701rrb')
    sprite('Action_052_04', 7)	# 132151-132157
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 132158-132162
    sprite('Action_052_06', 15)	# 132163-132177
    sprite('Action_052_07', 7)	# 132178-132184
    sprite('Action_052_08', 3)	# 132185-132187
    sprite('Action_052_09', 8)	# 132188-132195	 **attackbox here**
    sprite('Action_052_10', 3)	# 132196-132198	 **attackbox here**
    sprite('Action_052_11', 8)	# 132199-132206	 **attackbox here**
    Unknown23018(1)
    label(173)
    sprite('Action_052_12', 5)	# 132207-132211	 **attackbox here**
    gotoLabel(173)
    label(180)
    sprite('Action_052_00', 5)	# 132212-132216
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 132217-132221
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 132222-132226
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 132227-132234
    SFX_1('uhy700rbl')
    sprite('Action_052_04', 7)	# 132235-132241
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 132242-132246
    sprite('Action_052_06', 15)	# 132247-132261
    sprite('Action_052_07', 7)	# 132262-132268
    sprite('Action_052_08', 3)	# 132269-132271
    sprite('Action_052_09', 8)	# 132272-132279	 **attackbox here**
    sprite('Action_052_10', 3)	# 132280-132282	 **attackbox here**
    sprite('Action_052_11', 8)	# 132283-132290	 **attackbox here**
    label(181)
    sprite('Action_052_12', 1)	# 132291-132291	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_052_12', 30)	# 132292-132321	 **attackbox here**
    sprite('Action_052_12', 32767)	# 132322-165088	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(150)
    label(190)
    sprite('Action_000_00', 1)	# 165089-165089	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_000_00', 7)	# 165090-165096	 **attackbox here**
    sprite('Action_000_01', 7)	# 165097-165103	 **attackbox here**
    sprite('Action_000_02', 6)	# 165104-165109	 **attackbox here**
    sprite('Action_000_03', 6)	# 165110-165115	 **attackbox here**
    sprite('Action_000_04', 5)	# 165116-165120	 **attackbox here**
    sprite('Action_000_05', 5)	# 165121-165125	 **attackbox here**
    sprite('Action_000_06', 5)	# 165126-165130	 **attackbox here**
    sprite('Action_000_07', 6)	# 165131-165136	 **attackbox here**
    sprite('Action_000_08', 6)	# 165137-165142	 **attackbox here**
    sprite('Action_000_09', 7)	# 165143-165149	 **attackbox here**
    sprite('Action_000_10', 7)	# 165150-165156	 **attackbox here**
    sprite('Action_000_11', 6)	# 165157-165162	 **attackbox here**
    sprite('Action_000_12', 6)	# 165163-165168	 **attackbox here**
    sprite('Action_000_13', 5)	# 165169-165173	 **attackbox here**
    sprite('Action_000_14', 5)	# 165174-165178	 **attackbox here**
    sprite('Action_000_15', 5)	# 165179-165183	 **attackbox here**
    sprite('Action_000_16', 6)	# 165184-165189	 **attackbox here**
    sprite('Action_000_17', 6)	# 165190-165195	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('Action_052_00', 5)	# 165196-165200
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 165201-165205
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 165206-165210
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 165211-165218
    SFX_1('uhy701uor')
    sprite('Action_052_04', 7)	# 165219-165225
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 165226-165230
    sprite('Action_052_06', 15)	# 165231-165245
    sprite('Action_052_07', 7)	# 165246-165252
    sprite('Action_052_08', 3)	# 165253-165255
    sprite('Action_052_09', 8)	# 165256-165263	 **attackbox here**
    sprite('Action_052_10', 3)	# 165264-165266	 **attackbox here**
    sprite('Action_052_11', 8)	# 165267-165274	 **attackbox here**
    Unknown23018(1)
    label(193)
    sprite('Action_052_12', 5)	# 165275-165279	 **attackbox here**
    gotoLabel(193)
    label(200)
    sprite('Action_000_00', 1)	# 165280-165280	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 7)	# 165281-165287	 **attackbox here**
    sprite('Action_000_01', 7)	# 165288-165294	 **attackbox here**
    sprite('Action_000_02', 6)	# 165295-165300	 **attackbox here**
    sprite('Action_000_03', 6)	# 165301-165306	 **attackbox here**
    sprite('Action_000_04', 5)	# 165307-165311	 **attackbox here**
    sprite('Action_000_05', 5)	# 165312-165316	 **attackbox here**
    sprite('Action_000_06', 5)	# 165317-165321	 **attackbox here**
    sprite('Action_000_07', 6)	# 165322-165327	 **attackbox here**
    sprite('Action_000_08', 6)	# 165328-165333	 **attackbox here**
    sprite('Action_000_09', 7)	# 165334-165340	 **attackbox here**
    sprite('Action_000_10', 7)	# 165341-165347	 **attackbox here**
    sprite('Action_000_11', 6)	# 165348-165353	 **attackbox here**
    sprite('Action_000_12', 6)	# 165354-165359	 **attackbox here**
    sprite('Action_000_13', 5)	# 165360-165364	 **attackbox here**
    sprite('Action_000_14', 5)	# 165365-165369	 **attackbox here**
    sprite('Action_000_15', 5)	# 165370-165374	 **attackbox here**
    sprite('Action_000_16', 6)	# 165375-165380	 **attackbox here**
    sprite('Action_000_17', 6)	# 165381-165386	 **attackbox here**
    gotoLabel(201)
    label(202)
    sprite('Hyd960_00', 5)	# 165387-165391
    SFX_1('uhy701pag')
    sprite('Hyd960_01', 7)	# 165392-165398
    sprite('Hyd960_02', 7)	# 165399-165405	 **attackbox here**
    sprite('Hyd960_03', 9)	# 165406-165414	 **attackbox here**
    sprite('Hyd960_04', 4)	# 165415-165418	 **attackbox here**
    SFX_3('SE010')
    Unknown23018(1)
    label(203)
    sprite('Hyd960_05', 5)	# 165419-165423	 **attackbox here**
    sprite('Hyd960_06', 5)	# 165424-165428	 **attackbox here**
    sprite('Hyd960_07', 5)	# 165429-165433	 **attackbox here**
    loopRest()
    gotoLabel(203)
    label(210)
    sprite('Action_052_00', 5)	# 165434-165438
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 165439-165443
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 165444-165448
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 165449-165456
    SFX_1('uhy700uva')
    sprite('Action_052_04', 7)	# 165457-165463
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 165464-165468
    sprite('Action_052_06', 15)	# 165469-165483
    sprite('Action_052_07', 7)	# 165484-165490
    sprite('Action_052_08', 3)	# 165491-165493
    sprite('Action_052_09', 8)	# 165494-165501	 **attackbox here**
    sprite('Action_052_10', 3)	# 165502-165504	 **attackbox here**
    label(211)
    sprite('Action_052_12', 1)	# 165505-165505	 **attackbox here**
    if SLOT_97:
        _gotolabel(211)
    sprite('Action_052_12', 32767)	# 165506-198272	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(220)
    sprite('Action_000_00', 1)	# 198273-198273	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)

    def upon_39():
        clearUponHandler(39)
        SFX_1('uhy701uyu')
        Unknown23018(1)
    Unknown48('190000000200000035000000180000000200000027000000')
    if (SLOT_53 == SLOT_39):
        if (not SLOT_39):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                sendToLabel(221)
            else:
                SLOT_54 = 1
        else:
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                sendToLabel(221)
            else:
                SLOT_54 = 1
    elif (not SLOT_39):
        Unknown48('190000000200000033000000180000000200000016000000')
        Unknown47('01000000020000003300000002000000160000000200000033000000')
        if (SLOT_51 >= 0):
            pass
        else:
            sendToLabel(221)
    else:
        Unknown48('190000000200000033000000180000000200000016000000')
        Unknown47('01000000020000003300000002000000160000000200000033000000')
        if (SLOT_51 <= 0):
            pass
        else:
            sendToLabel(221)
    sprite('Action_015_00', 3)	# 198274-198276
    Unknown2005()
    sprite('Action_015_01', 3)	# 198277-198279
    label(221)
    sprite('Action_000_00', 7)	# 198280-198286	 **attackbox here**
    sprite('Action_000_01', 7)	# 198287-198293	 **attackbox here**
    sprite('Action_000_02', 6)	# 198294-198299	 **attackbox here**
    sprite('Action_000_03', 6)	# 198300-198305	 **attackbox here**
    sprite('Action_000_04', 5)	# 198306-198310	 **attackbox here**
    sprite('Action_000_05', 5)	# 198311-198315	 **attackbox here**
    sprite('Action_000_06', 5)	# 198316-198320	 **attackbox here**
    sprite('Action_000_07', 6)	# 198321-198326	 **attackbox here**
    sprite('Action_000_08', 6)	# 198327-198332	 **attackbox here**
    sprite('Action_000_09', 7)	# 198333-198339	 **attackbox here**
    sprite('Action_000_10', 7)	# 198340-198346	 **attackbox here**
    sprite('Action_000_11', 6)	# 198347-198352	 **attackbox here**
    sprite('Action_000_12', 6)	# 198353-198358	 **attackbox here**
    sprite('Action_000_13', 5)	# 198359-198363	 **attackbox here**
    sprite('Action_000_14', 5)	# 198364-198368	 **attackbox here**
    sprite('Action_000_15', 5)	# 198369-198373	 **attackbox here**
    sprite('Action_000_16', 6)	# 198374-198379	 **attackbox here**
    sprite('Action_000_17', 6)	# 198380-198385	 **attackbox here**
    gotoLabel(221)
    label(222)
    sprite('Hyd646_00', 6)	# 198386-198391
    sprite('Hyd646_01', 6)	# 198392-198397	 **attackbox here**
    label(223)
    sprite('Hyd646_02', 6)	# 198398-198403	 **attackbox here**
    sprite('Hyd646_03', 6)	# 198404-198409	 **attackbox here**
    sprite('Hyd646_04', 6)	# 198410-198415	 **attackbox here**
    sprite('Hyd646_03', 6)	# 198416-198421	 **attackbox here**
    gotoLabel(223)
    label(230)
    sprite('Action_000_00', 1)	# 198422-198422	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('Action_000_00', 7)	# 198423-198429	 **attackbox here**
    sprite('Action_000_01', 7)	# 198430-198436	 **attackbox here**
    sprite('Action_000_02', 6)	# 198437-198442	 **attackbox here**
    sprite('Action_000_03', 6)	# 198443-198448	 **attackbox here**
    sprite('Action_000_04', 5)	# 198449-198453	 **attackbox here**
    sprite('Action_000_05', 5)	# 198454-198458	 **attackbox here**
    sprite('Action_000_06', 5)	# 198459-198463	 **attackbox here**
    sprite('Action_000_07', 6)	# 198464-198469	 **attackbox here**
    sprite('Action_000_08', 6)	# 198470-198475	 **attackbox here**
    sprite('Action_000_09', 7)	# 198476-198482	 **attackbox here**
    sprite('Action_000_10', 7)	# 198483-198489	 **attackbox here**
    sprite('Action_000_11', 6)	# 198490-198495	 **attackbox here**
    sprite('Action_000_12', 6)	# 198496-198501	 **attackbox here**
    sprite('Action_000_13', 5)	# 198502-198506	 **attackbox here**
    sprite('Action_000_14', 5)	# 198507-198511	 **attackbox here**
    sprite('Action_000_15', 5)	# 198512-198516	 **attackbox here**
    sprite('Action_000_16', 6)	# 198517-198522	 **attackbox here**
    sprite('Action_000_17', 6)	# 198523-198528	 **attackbox here**
    gotoLabel(231)
    label(232)
    sprite('Action_052_00', 5)	# 198529-198533
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 198534-198538
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 198539-198543
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 198544-198551
    SFX_1('uhy701bma')
    sprite('Action_052_04', 7)	# 198552-198558
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 198559-198563
    sprite('Action_052_06', 15)	# 198564-198578
    sprite('Action_052_07', 7)	# 198579-198585
    sprite('Action_052_08', 3)	# 198586-198588
    sprite('Action_052_09', 8)	# 198589-198596	 **attackbox here**
    sprite('Action_052_10', 3)	# 198597-198599	 **attackbox here**
    sprite('Action_052_11', 8)	# 198600-198607	 **attackbox here**
    Unknown23018(1)
    sprite('Action_052_12', 32767)	# 198608-231374	 **attackbox here**
    label(240)
    sprite('Action_000_00', 1)	# 231375-231375	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(242)
    label(241)
    sprite('Action_000_00', 7)	# 231376-231382	 **attackbox here**
    sprite('Action_000_01', 7)	# 231383-231389	 **attackbox here**
    sprite('Action_000_02', 6)	# 231390-231395	 **attackbox here**
    sprite('Action_000_03', 6)	# 231396-231401	 **attackbox here**
    sprite('Action_000_04', 5)	# 231402-231406	 **attackbox here**
    sprite('Action_000_05', 5)	# 231407-231411	 **attackbox here**
    sprite('Action_000_06', 5)	# 231412-231416	 **attackbox here**
    sprite('Action_000_07', 6)	# 231417-231422	 **attackbox here**
    sprite('Action_000_08', 6)	# 231423-231428	 **attackbox here**
    sprite('Action_000_09', 7)	# 231429-231435	 **attackbox here**
    sprite('Action_000_10', 7)	# 231436-231442	 **attackbox here**
    sprite('Action_000_11', 6)	# 231443-231448	 **attackbox here**
    sprite('Action_000_12', 6)	# 231449-231454	 **attackbox here**
    sprite('Action_000_13', 5)	# 231455-231459	 **attackbox here**
    sprite('Action_000_14', 5)	# 231460-231464	 **attackbox here**
    sprite('Action_000_15', 5)	# 231465-231469	 **attackbox here**
    sprite('Action_000_16', 6)	# 231470-231475	 **attackbox here**
    sprite('Action_000_17', 6)	# 231476-231481	 **attackbox here**
    gotoLabel(241)
    label(242)
    sprite('Hyd960_00', 5)	# 231482-231486
    SFX_1('uhy701ahe')
    sprite('Hyd960_01', 7)	# 231487-231493
    sprite('Hyd960_02', 7)	# 231494-231500	 **attackbox here**
    sprite('Hyd960_03', 9)	# 231501-231509	 **attackbox here**
    sprite('Hyd960_04', 4)	# 231510-231513	 **attackbox here**
    SFX_3('SE010')
    Unknown23018(1)
    label(243)
    sprite('Hyd960_06', 5)	# 231514-231518	 **attackbox here**
    sprite('Hyd960_07', 5)	# 231519-231523	 **attackbox here**
    sprite('Hyd960_05', 5)	# 231524-231528	 **attackbox here**
    loopRest()
    gotoLabel(243)
    label(250)
    sprite('keep', 1)	# 231529-231529
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(254)
        elif (SLOT_38 == 1):
            sendToLabel(254)

    def upon_40():
        clearUponHandler(40)
        SFX_1('uhy701uak')
        Unknown2037(37)

        def upon_CLEAR_OR_EXIT():
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                sendToLabel(252)
    label(251)
    sprite('Action_000_00', 7)	# 231530-231536	 **attackbox here**
    sprite('Action_000_01', 7)	# 231537-231543	 **attackbox here**
    sprite('Action_000_02', 6)	# 231544-231549	 **attackbox here**
    sprite('Action_000_03', 6)	# 231550-231555	 **attackbox here**
    sprite('Action_000_04', 5)	# 231556-231560	 **attackbox here**
    sprite('Action_000_05', 5)	# 231561-231565	 **attackbox here**
    sprite('Action_000_06', 5)	# 231566-231570	 **attackbox here**
    sprite('Action_000_07', 6)	# 231571-231576	 **attackbox here**
    sprite('Action_000_08', 6)	# 231577-231582	 **attackbox here**
    sprite('Action_000_09', 7)	# 231583-231589	 **attackbox here**
    sprite('Action_000_10', 7)	# 231590-231596	 **attackbox here**
    sprite('Action_000_11', 6)	# 231597-231602	 **attackbox here**
    sprite('Action_000_12', 6)	# 231603-231608	 **attackbox here**
    sprite('Action_000_13', 5)	# 231609-231613	 **attackbox here**
    sprite('Action_000_14', 5)	# 231614-231618	 **attackbox here**
    sprite('Action_000_15', 5)	# 231619-231623	 **attackbox here**
    sprite('Action_000_16', 6)	# 231624-231629	 **attackbox here**
    sprite('Action_000_17', 6)	# 231630-231635	 **attackbox here**
    gotoLabel(251)
    label(252)
    sprite('Action_248_00', 6)	# 231636-231641
    sprite('Action_248_01', 5)	# 231642-231646
    sprite('Action_248_02', 5)	# 231647-231651
    sprite('Action_248_03', 5)	# 231652-231656
    sprite('Action_248_04', 4)	# 231657-231660	 **attackbox here**
    Unknown23018(1)
    label(253)
    sprite('Action_248_05', 6)	# 231661-231666	 **attackbox here**
    sprite('Action_248_06', 6)	# 231667-231672	 **attackbox here**
    sprite('Action_248_04', 6)	# 231673-231678	 **attackbox here**
    gotoLabel(253)
    label(254)
    sprite('Action_015_00', 3)	# 231679-231681
    sprite('Action_015_01', 3)	# 231682-231684
    Unknown2005()
    gotoLabel(251)
    label(260)
    sprite('Action_000_00', 1)	# 231685-231685	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(262)
    label(261)
    sprite('Action_000_00', 7)	# 231686-231692	 **attackbox here**
    sprite('Action_000_01', 7)	# 231693-231699	 **attackbox here**
    sprite('Action_000_02', 6)	# 231700-231705	 **attackbox here**
    sprite('Action_000_03', 6)	# 231706-231711	 **attackbox here**
    sprite('Action_000_04', 5)	# 231712-231716	 **attackbox here**
    sprite('Action_000_05', 5)	# 231717-231721	 **attackbox here**
    sprite('Action_000_06', 5)	# 231722-231726	 **attackbox here**
    sprite('Action_000_07', 6)	# 231727-231732	 **attackbox here**
    sprite('Action_000_08', 6)	# 231733-231738	 **attackbox here**
    sprite('Action_000_09', 7)	# 231739-231745	 **attackbox here**
    sprite('Action_000_10', 7)	# 231746-231752	 **attackbox here**
    sprite('Action_000_11', 6)	# 231753-231758	 **attackbox here**
    sprite('Action_000_12', 6)	# 231759-231764	 **attackbox here**
    sprite('Action_000_13', 5)	# 231765-231769	 **attackbox here**
    sprite('Action_000_14', 5)	# 231770-231774	 **attackbox here**
    sprite('Action_000_15', 5)	# 231775-231779	 **attackbox here**
    sprite('Action_000_16', 6)	# 231780-231785	 **attackbox here**
    sprite('Action_000_17', 6)	# 231786-231791	 **attackbox here**
    gotoLabel(261)
    label(262)
    sprite('keep', 1)	# 231792-231792
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                Unknown2005()
        elif (SLOT_38 == 1):
            Unknown2005()
    sprite('Action_052_00', 5)	# 231793-231797
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 231798-231802
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 231803-231807
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 231808-231815
    SFX_1('uhy701uhi')
    sprite('Action_052_04', 7)	# 231816-231822
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 231823-231827
    sprite('Action_052_06', 15)	# 231828-231842
    sprite('Action_052_07', 7)	# 231843-231849
    sprite('Action_052_08', 3)	# 231850-231852
    sprite('Action_052_09', 8)	# 231853-231860	 **attackbox here**
    sprite('Action_052_10', 3)	# 231861-231863	 **attackbox here**
    sprite('Action_052_11', 8)	# 231864-231871	 **attackbox here**
    Unknown23018(1)
    sprite('Action_052_12', 32767)	# 231872-264638	 **attackbox here**
    label(270)
    sprite('Action_000_00', 1)	# 264639-264639	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(272)
    label(271)
    sprite('Action_000_00', 7)	# 264640-264646	 **attackbox here**
    sprite('Action_000_01', 7)	# 264647-264653	 **attackbox here**
    sprite('Action_000_02', 6)	# 264654-264659	 **attackbox here**
    sprite('Action_000_03', 6)	# 264660-264665	 **attackbox here**
    sprite('Action_000_04', 5)	# 264666-264670	 **attackbox here**
    sprite('Action_000_05', 5)	# 264671-264675	 **attackbox here**
    sprite('Action_000_06', 5)	# 264676-264680	 **attackbox here**
    sprite('Action_000_07', 6)	# 264681-264686	 **attackbox here**
    sprite('Action_000_08', 6)	# 264687-264692	 **attackbox here**
    sprite('Action_000_09', 7)	# 264693-264699	 **attackbox here**
    sprite('Action_000_10', 7)	# 264700-264706	 **attackbox here**
    sprite('Action_000_11', 6)	# 264707-264712	 **attackbox here**
    sprite('Action_000_12', 6)	# 264713-264718	 **attackbox here**
    sprite('Action_000_13', 5)	# 264719-264723	 **attackbox here**
    sprite('Action_000_14', 5)	# 264724-264728	 **attackbox here**
    sprite('Action_000_15', 5)	# 264729-264733	 **attackbox here**
    sprite('Action_000_16', 6)	# 264734-264739	 **attackbox here**
    sprite('Action_000_17', 6)	# 264740-264745	 **attackbox here**
    gotoLabel(271)
    label(272)
    sprite('keep', 1)	# 264746-264746
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                Unknown2005()
        elif (SLOT_38 == 1):
            Unknown2005()
    sprite('Action_052_00', 5)	# 264747-264751
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 264752-264756
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 264757-264761
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 264762-264769
    SFX_1('uhy701pad')
    sprite('Action_052_04', 7)	# 264770-264776
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 264777-264781
    sprite('Action_052_06', 15)	# 264782-264796
    sprite('Action_052_07', 7)	# 264797-264803
    sprite('Action_052_08', 3)	# 264804-264806
    sprite('Action_052_09', 8)	# 264807-264814	 **attackbox here**
    sprite('Action_052_10', 3)	# 264815-264817	 **attackbox here**
    sprite('Action_052_11', 8)	# 264818-264825	 **attackbox here**
    Unknown23018(1)
    label(273)
    sprite('Action_052_12', 1)	# 264826-264826	 **attackbox here**
    gotoLabel(273)
    label(280)
    sprite('Action_000_00', 1)	# 264827-264827	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(282)
    label(281)
    sprite('Action_000_00', 7)	# 264828-264834	 **attackbox here**
    sprite('Action_000_01', 7)	# 264835-264841	 **attackbox here**
    sprite('Action_000_02', 6)	# 264842-264847	 **attackbox here**
    sprite('Action_000_03', 6)	# 264848-264853	 **attackbox here**
    sprite('Action_000_04', 5)	# 264854-264858	 **attackbox here**
    sprite('Action_000_05', 5)	# 264859-264863	 **attackbox here**
    sprite('Action_000_06', 5)	# 264864-264868	 **attackbox here**
    sprite('Action_000_07', 6)	# 264869-264874	 **attackbox here**
    sprite('Action_000_08', 6)	# 264875-264880	 **attackbox here**
    sprite('Action_000_09', 7)	# 264881-264887	 **attackbox here**
    sprite('Action_000_10', 7)	# 264888-264894	 **attackbox here**
    sprite('Action_000_11', 6)	# 264895-264900	 **attackbox here**
    sprite('Action_000_12', 6)	# 264901-264906	 **attackbox here**
    sprite('Action_000_13', 5)	# 264907-264911	 **attackbox here**
    sprite('Action_000_14', 5)	# 264912-264916	 **attackbox here**
    sprite('Action_000_15', 5)	# 264917-264921	 **attackbox here**
    sprite('Action_000_16', 6)	# 264922-264927	 **attackbox here**
    sprite('Action_000_17', 6)	# 264928-264933	 **attackbox here**
    gotoLabel(281)
    label(282)
    sprite('keep', 1)	# 264934-264934
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                Unknown2005()
        elif (SLOT_38 == 1):
            Unknown2005()
    sprite('Action_052_00', 5)	# 264935-264939
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 264940-264944
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 264945-264949
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 264950-264957
    SFX_1('uhy701kym')
    sprite('Action_052_04', 7)	# 264958-264964
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 264965-264969
    sprite('Action_052_06', 15)	# 264970-264984
    sprite('Action_052_07', 7)	# 264985-264991
    sprite('Action_052_08', 3)	# 264992-264994
    sprite('Action_052_09', 8)	# 264995-265002	 **attackbox here**
    sprite('Action_052_10', 3)	# 265003-265005	 **attackbox here**
    sprite('Action_052_11', 8)	# 265006-265013	 **attackbox here**
    Unknown23018(1)
    sprite('Action_052_12', 32767)	# 265014-297780	 **attackbox here**
    label(290)
    sprite('Action_052_00', 5)	# 297781-297785
    teleportRelativeX(-40000)
    sprite('Action_052_01', 5)	# 297786-297790
    teleportRelativeX(-40000)
    sprite('Action_052_02', 5)	# 297791-297795
    teleportRelativeX(-40000)
    sprite('Action_052_03', 8)	# 297796-297803
    sprite('Action_052_04', 7)	# 297804-297810
    SFX_3('SE_InsulatorSwingB')
    GFX_0('EffWinBlade01', 100)
    sprite('Action_052_05', 5)	# 297811-297815
    sprite('Action_052_06', 15)	# 297816-297830
    sprite('Action_052_07', 7)	# 297831-297837
    sprite('Action_052_08', 3)	# 297838-297840
    sprite('Action_052_09', 8)	# 297841-297848	 **attackbox here**
    sprite('Action_052_10', 3)	# 297849-297851	 **attackbox here**
    sprite('Action_052_11', 8)	# 297852-297859	 **attackbox here**
    SFX_1('uhy700use')
    label(291)
    sprite('Action_052_12', 1)	# 297860-297860	 **attackbox here**
    if SLOT_97:
        _gotolabel(291)
    sprite('Action_052_12', 30)	# 297861-297890	 **attackbox here**
    sprite('Action_052_12', 32767)	# 297891-330657	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(200)

@State
def CmnActLose():
    sprite('Action_248_00', 6)	# 1-6
    sprite('Action_248_01', 5)	# 7-11
    sprite('Action_248_02', 5)	# 12-16
    sprite('Action_248_03', 5)	# 17-21
    sprite('Action_248_04', 4)	# 22-25	 **attackbox here**
    if SLOT_158:
        Unknown7006('uhy403_0', 100, 880371829, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(0)
    sprite('Action_248_04', 6)	# 26-31	 **attackbox here**
    sprite('Action_248_05', 6)	# 32-37	 **attackbox here**
    sprite('Action_248_06', 6)	# 38-43	 **attackbox here**
    loopRest()
    gotoLabel(0)

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

    def upon_CLEAR_OR_EXIT():
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

    def upon_CLEAR_OR_EXIT():
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

    def upon_CLEAR_OR_EXIT():
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