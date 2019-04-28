@Subroutine
def PreInit():
    Unknown12019('756f7200000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    JumpYVelocity(36000)
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
    Unknown14015(0, 400000, -200000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 550000, -100000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 700000, -100000, 50000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 250000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A_Renda', 0x4)
    Unknown14005(1)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown14015(0, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 450000, -200000, 200000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 250000, -200000, 250000, 2000, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(5000)
    Unknown15013(50)
    Unknown14015(120000, 650000, 0, 600000, 500, 1)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 400000, -100000, 100000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown15008()
    Unknown14015(-100000, 450000, -250000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15008()
    Unknown14015(-100000, 250000, -300000, 100000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown15008()
    Unknown14015(-100000, 200000, -100000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown15008()
    Unknown14015(-100000, 200000, -300000, 300000, 2000, 50)
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
    Move_Register('AssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(100)
    Unknown14015(120000, 650000, -200000, 200000, 1500, 1)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(100)
    Unknown15014(500)
    Unknown14015(120000, 1100000, -200000, 200000, 1000, 1)
    Move_EndRegister()
    Move_Register('CommandOrderA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown15021(100)
    Unknown15014(500)
    Unknown14015(120000, 700000, -200000, 200000, 1000, 1)
    Move_EndRegister()
    Move_Register('CommandOrderB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(500)
    Unknown14015(120000, 650000, -200000, 450000, 1000, 1)
    Move_EndRegister()
    Move_Register('CommandOrderAdd_A', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15013(2000)
    Unknown14015(120000, 1100000, -200000, 200000, 2000, 1)
    Move_EndRegister()
    Move_Register('CommandOrderAdd_B', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(0xed)
    Unknown15013(2000)
    Unknown14015(120000, 1100000, -200000, 200000, 2000, 1)
    Move_EndRegister()
    Move_Register('CommandOrderAirA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15009()
    Unknown14015(120000, 700000, -200000, 100000, 1000, 1)
    Move_EndRegister()
    Move_Register('CommandOrderAirB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15009()
    Unknown14015(120000, 700000, -200000, 100000, 1000, 1)
    Move_EndRegister()
    Move_Register('AssaultEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(120000, 1300000, -200000, 200000, 250, 1)
    Move_EndRegister()
    Move_Register('CommandOrderEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Unknown15014(500)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(120000, 850000, -200000, 350000, 250, 1)
    Move_EndRegister()
    Move_Register('CommandOrderAirEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(1500)
    Unknown15021(750)
    Unknown14015(0, 550000, -400000, 350000, 250, 1)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15014(3000)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15014(3000)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-50000, 300000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 250000, -200000, 500000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShotOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 250000, -200000, 500000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15005(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 500000, -200000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Move_EndRegister()
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2A_Renda', 10000000)
    Unknown15024('NmlAtk2A_Renda', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2C', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'CommandOrderA', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'AssaultA', 10000000)
    Unknown15024('NmlAtk2B', 'FrontJump', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('CommandOrderA', 'CommandOrderAdd_A', 10000000)
    Unknown15024('CommandOrderB', 'CommandOrderAdd_B', 10000000)
    Unknown15024('ThrowExe', 'AssaultB', 10000000)
    Unknown15024('BackThrowExe', 'AssaultB', 10000000)
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
    Unknown12018(1, 'Action_330_02')
    Unknown12018(2, 'Action_330_04')
    Unknown12018(3, 'Action_330_05')
    Unknown12018(4, 'Action_330_06')
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
    Unknown12018(16, 'Action_300_01')
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
    Unknown7010(0, 'uor000')
    Unknown7010(1, 'uor001')
    Unknown7010(2, 'uor002')
    Unknown7010(3, 'uor003')
    Unknown7010(4, 'uor004')
    Unknown7010(5, 'uor005')
    Unknown7010(6, 'uor006')
    Unknown7010(7, 'uor007')
    Unknown7010(8, 'uor008')
    Unknown7010(9, 'uor009')
    Unknown7010(10, 'uor010')
    Unknown7010(15, 'uor011')
    Unknown7010(16, 'uor012')
    Unknown7010(17, 'uor013')
    Unknown7010(18, 'uor014')
    Unknown7010(19, 'uor015')
    Unknown7010(20, 'uor016')
    Unknown7010(21, 'uor017')
    Unknown7010(22, 'uor018')
    Unknown7010(23, 'uor019')
    Unknown7010(24, 'uor020')
    Unknown7010(25, 'uor021')
    Unknown7010(28, 'uor022')
    Unknown7010(29, 'uor023')
    Unknown7010(30, 'uor024')
    Unknown7010(31, 'uor025')
    Unknown7010(32, 'uor026')
    Unknown7010(33, 'uor027')
    Unknown7010(34, 'uor028')
    Unknown7010(35, 'uor029')
    Unknown7010(36, 'uor030')
    Unknown7010(37, 'uor031')
    Unknown7010(39, 'uor032')
    Unknown7010(42, 'uor033')
    Unknown7010(43, 'uor034')
    Unknown7010(44, 'uor035')
    Unknown7010(45, 'uor036')
    Unknown7010(46, 'uor037')
    Unknown7010(47, 'uor038')
    Unknown7010(48, 'uor039')
    Unknown7010(49, 'uor040')
    Unknown7010(50, 'uor041')
    Unknown7010(52, 'uor042')
    Unknown7010(53, 'uor043')
    Unknown7010(54, 'uor100_0')
    Unknown7010(55, 'uor100_1')
    Unknown7010(56, 'uor100_2')
    Unknown7010(63, 'uor101_0')
    Unknown7010(64, 'uor101_1')
    Unknown7010(65, 'uor101_2')
    Unknown7010(57, 'uor102_0')
    Unknown7010(58, 'uor102_1')
    Unknown7010(59, 'uor102_2')
    Unknown7010(66, 'uor103_0')
    Unknown7010(67, 'uor103_1')
    Unknown7010(68, 'uor103_2')
    Unknown7010(60, 'uor104_0')
    Unknown7010(61, 'uor104_1')
    Unknown7010(62, 'uor104_2')
    Unknown7010(69, 'uor105_0')
    Unknown7010(70, 'uor105_1')
    Unknown7010(71, 'uor105_2')
    Unknown7010(72, 'uor150')
    Unknown7010(73, 'uor151')
    Unknown7010(74, 'uor152')
    Unknown7010(85, 'uor153')
    Unknown7010(87, 'uor154')
    Unknown7010(88, 'uor155')
    Unknown7010(96, 'uor161_0')
    Unknown7010(97, 'uor161_1')
    Unknown7010(92, 'uor162_0')
    Unknown7010(93, 'uor162_1')
    Unknown7010(98, 'uor163_0')
    Unknown7010(99, 'uor163_1')
    Unknown7010(100, 'uor164_0')
    Unknown7010(101, 'uor164_1')
    Unknown7010(105, 'uor165_0')
    Unknown7010(106, 'uor165_1')
    Unknown7010(102, 'uor166_0')
    Unknown7010(103, 'uor166_1')
    Unknown7010(90, 'uor167_0')
    Unknown7010(91, 'uor167_1')
    Unknown7010(107, 'uor168_0')
    Unknown7010(108, 'uor168_1')
    Unknown7010(110, 'uor169_0')
    Unknown7010(111, 'uor169_1')
    Unknown7010(94, 'uor400_0')
    Unknown7010(95, 'uor400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746553686f744f44000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@State
def CmnActStand():
    label(0)
    sprite('Action_000_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_000_01', 6)	# 4-9	 **attackbox here**
    sprite('Action_000_02', 6)	# 10-15	 **attackbox here**
    sprite('Action_000_03', 6)	# 16-21	 **attackbox here**
    sprite('Action_000_04', 6)	# 22-27	 **attackbox here**
    sprite('Action_000_05', 6)	# 28-33	 **attackbox here**
    sprite('Action_000_06', 6)	# 34-39	 **attackbox here**
    sprite('Action_000_07', 6)	# 40-45	 **attackbox here**
    sprite('Action_000_08', 6)	# 46-51	 **attackbox here**
    sprite('Action_000_09', 6)	# 52-57	 **attackbox here**
    sprite('Action_000_10', 6)	# 58-63	 **attackbox here**
    sprite('Action_000_11', 6)	# 64-69	 **attackbox here**
    sprite('Action_000_12', 6)	# 70-75	 **attackbox here**
    sprite('Action_000_13', 6)	# 76-81	 **attackbox here**
    sprite('Action_000_14', 6)	# 82-87	 **attackbox here**
    sprite('Action_000_15', 6)	# 88-93	 **attackbox here**
    sprite('Action_000_16', 6)	# 94-99	 **attackbox here**
    sprite('Action_000_17', 6)	# 100-105	 **attackbox here**
    sprite('Action_000_18', 6)	# 106-111
    sprite('Action_000_19', 6)	# 112-117
    sprite('Action_000_20', 6)	# 118-123
    sprite('Action_000_21', 6)	# 124-129
    sprite('Action_000_22', 6)	# 130-135
    sprite('Action_000_23', 6)	# 136-141
    sprite('Action_000_24', 3)	# 142-144
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    label(1)
    sprite('Action_000_26', 5)	# 145-149
    SLOT_88 = 960
    sprite('Action_000_27', 5)	# 150-154
    sprite('Action_000_28', 7)	# 155-161
    sprite('Action_000_29', 4)	# 162-165
    SFX_1('uor000')
    sprite('Action_000_30', 4)	# 166-169
    SFX_3('SE042')
    sprite('Action_000_31', 9)	# 170-178
    sprite('Action_000_32', 5)	# 179-183
    sprite('Action_000_33', 5)	# 184-188
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
    sprite('Action_013_09', 5)	# 46-50
    sprite('Action_013_10', 5)	# 51-55
    sprite('Action_013_11', 5)	# 56-60
    sprite('Action_013_12', 5)	# 61-65
    sprite('Action_013_13', 5)	# 66-70
    sprite('Action_013_14', 5)	# 71-75
    sprite('Action_013_15', 5)	# 76-80
    sprite('Action_013_16', 5)	# 81-85
    sprite('Action_013_17', 5)	# 86-90
    sprite('Action_013_18', 5)	# 91-95
    sprite('Action_013_19', 5)	# 96-100
    sprite('Action_013_20', 5)	# 101-105
    sprite('Action_013_21', 5)	# 106-110
    sprite('Action_013_22', 5)	# 111-115
    sprite('Action_013_23', 5)	# 116-120
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 3)	# 1-3
    sprite('Action_016_01', 3)	# 4-6

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 4)	# 1-4
    sprite('Action_014_01', 4)	# 5-8
    sprite('Action_014_02', 4)	# 9-12

@State
def CmnActJumpPre():
    if SLOT_16:
        _gotolabel(1)
    label(0)
    sprite('Action_035_00', 4)	# 1-4
    ExitState()
    label(1)
    sprite('Action_067_00', 4)	# 5-8
    ExitState()

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    label(0)
    sprite('Action_035_01', 4)	# 1-4
    sprite('Action_035_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_067_01', 4)	# 9-12
    sprite('Action_067_02', 4)	# 13-16
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('Action_035_02', 2)	# 1-2
    sprite('Action_035_03', 2)	# 3-4
    sprite('Action_035_04', 2)	# 5-6
    sprite('Action_035_05', 2)	# 7-8
    sprite('Action_035_06', 2)	# 9-10

@State
def CmnActJumpDown():
    label(0)
    sprite('Action_020_00', 3)	# 1-3
    sprite('Action_020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('Action_021_00', 5)	# 1-5
    sprite('Action_021_01', 4)	# 6-9
    sprite('Action_021_02', 4)	# 10-13
    sprite('Action_021_03', 4)	# 14-17

@State
def CmnActLandingStiffLoop():
    sprite('Action_246_00', 3)	# 1-3
    sprite('Action_246_01', 32767)	# 4-32770

@State
def CmnActLandingStiffEnd():
    sprite('Action_246_02', 3)	# 1-3
    sprite('Action_246_03', 3)	# 4-6

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 2)	# 1-2
    sprite('Action_010_01', 4)	# 3-6
    sprite('Action_010_02', 4)	# 7-10
    sprite('Action_010_03', 3)	# 11-13
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_04', 3)	# 14-16
    sprite('Action_010_05', 4)	# 17-20
    sprite('Action_010_06', 4)	# 21-24
    sprite('Action_010_07', 4)	# 25-28
    sprite('Action_010_08', 4)	# 29-32
    sprite('Action_010_09', 3)	# 33-35
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_10', 3)	# 36-38
    sprite('Action_010_11', 4)	# 39-42
    sprite('Action_010_12', 4)	# 43-46
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    label(0)
    sprite('Action_011_00', 6)	# 1-6
    sprite('Action_011_01', 6)	# 7-12
    sprite('Action_011_02', 4)	# 13-16
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_03', 4)	# 17-20
    sprite('Action_011_04', 6)	# 21-26
    sprite('Action_011_05', 6)	# 27-32
    sprite('Action_011_06', 6)	# 33-38
    sprite('Action_011_07', 6)	# 39-44
    sprite('Action_011_08', 4)	# 45-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_09', 4)	# 49-52
    sprite('Action_011_10', 6)	# 53-58
    sprite('Action_011_11', 6)	# 59-64
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_010_00', 3)	# 1-3
    sprite('Action_045_00', 5)	# 4-8
    Unknown8006(100, 1, 1)
    sprite('Action_045_01', 3)	# 9-11
    sprite('Action_045_02', 3)	# 12-14
    sprite('Action_045_03', 3)	# 15-17
    sprite('Action_045_04', 3)	# 18-20
    sprite('Action_045_05', 3)	# 21-23
    Unknown8006(100, 1, 1)
    sprite('Action_045_06', 3)	# 24-26
    sprite('Action_045_07', 3)	# 27-29
    sprite('Action_045_08', 3)	# 30-32
    label(0)
    sprite('Action_045_09', 3)	# 33-35
    Unknown8006(100, 1, 1)
    sprite('Action_045_10', 3)	# 36-38
    sprite('Action_045_11', 3)	# 39-41
    sprite('Action_045_12', 3)	# 42-44
    sprite('Action_045_13', 3)	# 45-47
    Unknown8006(100, 1, 1)
    sprite('Action_045_14', 3)	# 48-50
    sprite('Action_045_15', 3)	# 51-53
    sprite('Action_045_16', 3)	# 54-56
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_17', 6)	# 1-6
    sprite('Action_045_17', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincible(1)
        Unknown1084(1)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()

        def upon_3():
            Unknown1019(90)
    label(0)
    sprite('Action_046_00', 2)	# 1-2
    sprite('Action_046_01', 2)	# 3-4
    Unknown8002()
    physicsXImpulse(-47000)
    physicsYImpulse(32000)
    setGravity(6000)
    sprite('Action_046_02', 3)	# 5-7
    sprite('Action_046_03', 3)	# 8-10
    sprite('Action_046_04', 12)	# 11-22
    setInvincible(0)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_046_05', 2)	# 23-24
    teleportRelativeX(-50000)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_046_06', 5)	# 25-29
    sprite('Action_046_07', 2)	# 30-31
    physicsXImpulse(-35000)
    physicsYImpulse(12000)
    setGravity(4000)
    sprite('Action_046_08', 3)	# 32-34
    label(2)
    sprite('Action_046_09', 5)	# 35-39
    sprite('Action_046_10', 3)	# 40-42
    teleportRelativeX(-50000)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    physicsXImpulse(-10000)
    physicsYImpulse(0)
    setGravity(0)
    sprite('Action_046_11', 2)	# 43-44
    sprite('Action_046_12', 2)	# 45-46
    Unknown1084(1)
    loopRest()

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
    sprite('Action_046_00', 3)	# 1-3
    physicsYImpulse(12000)
    label(0)
    sprite('Action_046_01', 4)	# 4-7
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
    sprite('Action_330_06', 3)	# 1-3
    sprite('Action_330_07', 3)	# 4-6
    label(0)
    sprite('Action_330_08', 4)	# 7-10
    sprite('Action_330_09', 4)	# 11-14
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

@State
def CmnActUkemiLandF():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14

@State
def CmnActUkemiLandB():
    sprite('Action_041_00', 2)	# 1-2
    sprite('Action_041_01', 2)	# 3-4
    sprite('Action_041_02', 2)	# 5-6
    sprite('Action_041_03', 2)	# 7-8
    sprite('Action_041_04', 2)	# 9-10
    sprite('Action_041_05', 2)	# 11-12
    sprite('Action_041_06', 2)	# 13-14

@State
def CmnActUkemiLandN():
    sprite('Action_041_00', 3)	# 1-3
    sprite('Action_041_01', 3)	# 4-6
    sprite('Action_041_02', 4)	# 7-10
    sprite('Action_041_03', 4)	# 11-14
    sprite('Action_041_04', 4)	# 15-18
    label(0)
    sprite('Action_041_05', 4)	# 19-22
    sprite('Action_041_06', 4)	# 23-26
    gotoLabel(0)

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
def CmnActAirTurn():
    sprite('Action_036_01', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_412_00', 2)	# 1-2
    sprite('Action_412_01', 2)	# 3-4
    sprite('Action_412_02', 2)	# 5-6
    sprite('Action_412_03', 2)	# 7-8
    sprite('Action_412_04', 1)	# 9-9	 **attackbox here**
    sprite('Action_412_05', 2)	# 10-11	 **attackbox here**
    sprite('Action_412_06', 3)	# 12-14
    sprite('Action_412_07', 3)	# 15-17
    sprite('Action_412_08', 2)	# 18-19
    sprite('Action_412_09', 3)	# 20-22
    sprite('Action_412_10', 2)	# 23-24
    sprite('Action_412_11', 2)	# 25-26

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
        AttackLevel_(2)
        Unknown9016(1)
        AirPushbackY(17500)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_001_00', 3)	# 1-3
    sprite('Action_001_01', 3)	# 4-6
    Unknown7009(0)
    sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    GFX_0('EffNmlAtk5ABlade', 100)
    sprite('Action_001_03', 4)	# 9-12
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_001_04', 8)	# 13-20
    sprite('Action_001_05', 4)	# 21-24
    sprite('Action_001_06', 3)	# 25-27

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9016(1)
        AirPushbackY(15000)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_002_00', 5)	# 1-5
    sprite('Action_002_01', 3)	# 6-8
    Unknown7009(4)
    sprite('Action_002_02ex01', 2)	# 9-10	 **attackbox here**
    GFX_0('EffNmlAtk5BBlade', 100)
    SFX_3('SE042')
    RefreshMultihit()
    sprite('Action_002_03', 2)	# 11-12
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_002_04', 5)	# 13-17
    sprite('Action_002_05', 6)	# 18-23
    sprite('Action_002_06', 5)	# 24-28
    sprite('Action_002_07', 5)	# 29-33

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(170)
        Unknown11092(1)
        Unknown9016(1)
        Hitstop(1)
        Unknown9154(19)
        AirUntechableTime(22)
        Unknown30056('905f01003200000000000000')
        AirPushbackX(22000)
        AirPushbackY(15000)
        Unknown11056(0)
        Unknown11001(-1, -1, -1)
    sprite('Action_045_00', 2)	# 1-2
    sprite('Action_045_01', 2)	# 3-4
    physicsXImpulse(20000)
    Unknown8007(100, 1, 1)
    sprite('Action_403_00', 3)	# 5-7
    sprite('Action_403_01', 3)	# 8-10
    Unknown7009(5)
    sprite('Action_403_02', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade1', 100)
    SFX_3('SE041')
    sprite('Action_403_03', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_04', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade2', 100)
    SFX_3('SE041')
    sprite('Action_403_05', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    Unknown8006(0, 1, 1)
    callSubroutine('ChainRoot')
    sprite('Action_403_06', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_07', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_08', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    Unknown8006(0, 1, 1)
    GFX_0('Eff66CBlade3', 100)
    SFX_3('SE041')

    def upon_ON_HIT_OR_BLOCK():
        Unknown14070('AN_NmlAtk5A_4th')
    sprite('Action_403_09', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    sprite('Action_403_10', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    GFX_0('Eff66CBlade4', 100)
    sprite('Action_403_11', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    Unknown8006(0, 1, 1)
    sprite('Action_403_12', 2)	# 31-32	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade5', 100)
    SFX_3('SE041')
    sprite('Action_403_13', 2)	# 33-34	 **attackbox here**
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        Unknown14072('AN_NmlAtk5A_4th')
    sprite('Action_403_14', 4)	# 35-38	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    Unknown14072('AN_NmlAtk5A_4th')
    Unknown1019(50)
    sprite('Action_403_15', 4)	# 39-42	 **attackbox here**
    Unknown14074('AN_NmlAtk5A_4th')
    Unknown1019(50)
    sprite('Action_403_16', 9)	# 43-51
    Unknown8010(0, 1, 1)
    Unknown1019(50)
    sprite('Action_403_16', 6)	# 52-57
    Unknown1019(50)

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('Action_149_00', 3)	# 1-3
    sprite('Action_149_01', 3)	# 4-6
    GFX_0('Tan_SealingEx', 100)
    sprite('Action_149_02', 4)	# 7-10
    Unknown7006('uor209_0', 100, 846360437, 828324144, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_149_03', 5)	# 11-15
    sprite('Action_149_04', 5)	# 16-20
    sprite('Action_149_05', 19)	# 21-39
    sprite('Action_149_06', 8)	# 40-47
    Recovery()
    sprite('Action_149_07', 7)	# 48-54

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(80)
        Unknown9154(19)
        AirPushbackY(15000)
        Unknown2004(1, 0)
        Unknown1112('')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')
        callSubroutine('ChainRoot')
    sprite('Action_003_00', 1)	# 1-1
    sprite('Action_003_01', 1)	# 2-2
    sprite('Action_003_02', 1)	# 3-3
    sprite('Action_003_03', 2)	# 4-5
    sprite('Action_003_04', 2)	# 6-7
    Unknown1015(15000)
    Unknown1030(-1500)
    sprite('Action_003_05', 2)	# 8-9
    teleportRelativeX(50000)
    Unknown7009(2)
    sprite('Action_003_06', 1)	# 10-10
    teleportRelativeX(50000)
    sprite('Action_003_07', 1)	# 11-11
    teleportRelativeX(45000)
    Unknown1084(1)
    GFX_0('EffNmlAtk5CZanzo', 100)
    SFX_3('SE045')
    sprite('Action_003_08', 4)	# 12-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_003_09', 4)	# 16-19	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_003_10', 4)	# 20-23
    sprite('Action_003_11', 4)	# 24-27
    sprite('Action_003_12', 4)	# 28-31
    sprite('Action_003_13', 5)	# 32-36

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(80)
        AirPushbackX(8000)
        AirPushbackY(27500)
        Unknown9154(19)
        AirUntechableTime(23)
        AirHitstunAnimation(13)
        HitOrBlockCancel('AN_NmlAtk5B_3rd')
        callSubroutine('ChainRoot')
    sprite('Action_241_00', 2)	# 1-2
    sprite('Action_241_01', 2)	# 3-4
    teleportRelativeX(50000)
    sprite('Action_241_02', 3)	# 5-7
    teleportRelativeX(22000)
    sprite('Action_241_03', 5)	# 8-12
    Unknown7006('uor106_0', 100, 829583221, 828323376, 0, 0, 100, 829583221, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_241_04', 2)	# 13-14
    GFX_0('EffNmlAtk4CZanzo', 100)
    Unknown1015(25000)
    SFX_3('SE045')
    sprite('Action_241_05', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    sprite('Action_241_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_241_07', 3)	# 20-22
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_241_08', 3)	# 23-25
    sprite('Action_241_09', 3)	# 26-28
    sprite('Action_241_10', 3)	# 29-31
    sprite('Action_241_11', 2)	# 32-33
    sprite('Action_241_12', 2)	# 34-35

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(9000)
        AirPushbackY(-80000)
        YImpluseBeforeWallbounce(0)
        Unknown9154(19)
        AirUntechableTime(30)
        Unknown9310(1)
        callSubroutine('ChainRoot')
    sprite('Action_242_00', 1)	# 1-1
    sprite('Action_242_01', 2)	# 2-3
    sprite('Action_242_02', 2)	# 4-5
    teleportRelativeX(50000)
    sprite('Action_242_03', 2)	# 6-7
    teleportRelativeX(50000)
    sprite('Action_242_04', 2)	# 8-9
    teleportRelativeX(50000)
    physicsXImpulse(15000)
    sprite('Action_242_05', 2)	# 10-11
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_242_06', 2)	# 12-13
    teleportRelativeX(50000)
    SFX_3('SE040_Landing')
    sprite('Action_242_07', 2)	# 14-15
    sprite('Action_242_08', 2)	# 16-17
    Unknown7006('uor108_1', 100, 829583221, 845101104, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_242_09ex01', 1)	# 18-18	 **attackbox here**
    GFX_0('EffNmlAtk6BZanzo', 100)
    SFX_3('SE043')
    sprite('Action_242_10ex01', 3)	# 19-21	 **attackbox here**
    sprite('Action_242_11', 4)	# 22-25
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_242_12', 5)	# 26-30
    sprite('Action_242_13', 4)	# 31-34
    sprite('Action_242_14', 4)	# 35-38
    sprite('Action_242_15', 4)	# 39-42
    sprite('Action_242_16', 3)	# 43-45

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(3)
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    sprite('Action_004_03', 6)	# 9-14
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 5)	# 15-19
    sprite('Action_004_05', 4)	# 20-23

@State
def NmlAtk2A_Renda():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        HitOrBlockJumpCancel(1)
        callSubroutine('ChainRoot')
        WhiffCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtk2A_Renda')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_004_00', 3)	# 1-3
    sprite('Action_004_01', 3)	# 4-6
    Unknown7009(3)
    sprite('Action_004_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE041')
    sprite('Action_004_03', 5)	# 9-13
    WhiffCancelEnable(1)
    Recovery()
    Unknown2063()
    sprite('Action_004_04', 4)	# 14-17
    sprite('Action_004_05', 3)	# 18-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirUntechableTime(24)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitJumpCancel(1)
        callSubroutine('ChainRoot')
    sprite('Action_244_00', 3)	# 1-3
    sprite('Action_244_01', 1)	# 4-4
    sprite('Action_244_01', 2)	# 5-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_244_02', 2)	# 7-8
    Unknown7009(1)
    sprite('Action_244_03', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtk3BBlade', 100)
    SFX_3('SE042')
    sprite('Action_244_04', 12)	# 12-23
    setInvincible(0)
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_244_05', 6)	# 24-29
    sprite('Action_244_06', 6)	# 30-35

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
    sprite('Action_006_00', 3)	# 1-3
    sprite('Action_006_01', 4)	# 4-7
    sprite('Action_006_02', 3)	# 8-10
    teleportRelativeX(50000)
    Unknown7006('uor107_0', 100, 829583221, 828323632, 0, 0, 100, 829583221, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_006_03', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE043')
    sprite('Action_006_04', 3)	# 13-15	 **attackbox here**
    sprite('Action_006_05', 3)	# 16-18
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_006_06', 4)	# 19-22
    sprite('Action_006_07', 3)	# 23-25
    sprite('Action_006_08', 3)	# 26-28
    sprite('Action_006_09', 3)	# 29-31
    sprite('Action_006_10ex01', 3)	# 32-34
    sprite('Action_006_11ex01', 1)	# 35-35
    sprite('Action_006_11ex01', 1)	# 36-36
    loopRest()

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        AirPushbackY(18000)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_00', 3)	# 1-3
    sprite('Action_009_01', 3)	# 4-6
    sprite('Action_009_02', 3)	# 7-9
    Unknown7009(3)
    sprite('Action_009_03', 6)	# 10-15	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAIR5CBlade', 100)
    SFX_3('SE041')
    sprite('Action_009_04', 3)	# 16-18
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_009_05', 5)	# 19-23
    sprite('Action_009_06', 4)	# 24-27

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_007_00', 3)	# 1-3
    sprite('Action_007_01', 3)	# 4-6
    Unknown7009(0)
    sprite('Action_007_02', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAIR5ABlade', 100)
    SFX_3('SE041')
    sprite('Action_007_03', 2)	# 9-10
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_007_04', 8)	# 11-18
    sprite('Action_007_05', 7)	# 19-25

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1700)
        AirUntechableTime(22)
        AirPushbackX(8000)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_008_00', 5)	# 1-5
    sprite('Action_008_01', 4)	# 6-9
    Unknown7009(5)
    sprite('Action_008_02', 1)	# 10-10
    GFX_0('EffNmlAtkAIR5BZanzo', 100)
    SFX_3('SE042')
    sprite('Action_008_03', 5)	# 11-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_008_04', 6)	# 16-21
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_008_05', 5)	# 22-26
    sprite('Action_008_06', 5)	# 27-31

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(2000)
        AttackP2(85)
        AirPushbackX(15000)
        AirPushbackY(-85000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(45)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
    sprite('Action_245_00', 3)	# 1-3
    sprite('Action_245_01', 2)	# 4-5
    sprite('Action_245_02', 2)	# 6-7
    sprite('Action_245_03', 4)	# 8-11
    Unknown7006('uor304_1', 100, 863137653, 828323632, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_245_04', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAIR2CZanzo', 100)
    SFX_3('SE045')
    sprite('Action_245_05', 5)	# 14-18	 **attackbox here**
    sprite('Action_245_06', 3)	# 19-21
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_245_07', 5)	# 22-26
    sprite('Action_245_08', 4)	# 27-30
    sprite('Action_245_09', 4)	# 31-34

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
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
    tag_voice(1, 'uor156_0', 'uor156_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 3)	# 14-16
    sprite('Action_068_06', 2)	# 17-18
    sprite('Action_007_00', 3)	# 19-21
    sprite('Action_007_01', 4)	# 22-25
    sprite('Action_007_02', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAIR5ABlade', 100)
    SFX_3('SE041')
    sprite('Action_007_03', 2)	# 29-30
    sprite('Action_007_04', 8)	# 31-38
    sprite('Action_007_05', 7)	# 39-45
    label(0)
    sprite('Action_068_09', 3)	# 46-48
    sprite('Action_068_10', 2)	# 49-50
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_246_00', 2)	# 51-52
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_246_01', 6)	# 53-58
    sprite('Action_246_02', 3)	# 59-61
    Unknown18009(0)
    sprite('Action_246_03', 2)	# 62-63

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 20)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_007_03', 2)	# 1-2
    sprite('Action_007_04', 8)	# 3-10
    sprite('Action_007_05', 7)	# 11-17
    label(1)
    sprite('Action_246_00', 2)	# 18-19
    Unknown8000(100, 1, 1)
    sprite('Action_246_01', 6)	# 20-25
    sprite('Action_246_02', 3)	# 26-28
    Unknown18009(0)
    sprite('Action_246_03', 2)	# 29-30
    label(2)
    sprite('Action_402_00', 2)	# 31-32
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('Action_402_01', 2)	# 33-34
    sprite('Action_402_02', 3)	# 35-37
    teleportRelativeX(36000)
    tag_voice(0, 'uor157_0', 'uor157_1', '', '')
    sprite('Action_402_03', 2)	# 38-39
    sprite('Action_402_04', 2)	# 40-41	 **attackbox here**
    GFX_0('Eff66BZanzo1', 100)
    SFX_3('SE043')
    sprite('Action_402_05', 5)	# 42-46
    sprite('Action_402_06', 4)	# 47-50
    sprite('Action_402_07', 3)	# 51-53
    sprite('Action_402_08', 2)	# 54-55
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('Action_000_00', 7)	# 56-62	 **attackbox here**
    sprite('Action_000_01', 7)	# 63-69	 **attackbox here**
    sprite('Action_000_02', 6)	# 70-75	 **attackbox here**
    sprite('Action_000_03', 6)	# 76-81	 **attackbox here**
    sprite('Action_000_04', 5)	# 82-86	 **attackbox here**
    sprite('Action_000_05', 5)	# 87-91	 **attackbox here**
    sprite('Action_000_06', 5)	# 92-96	 **attackbox here**
    sprite('Action_000_07', 6)	# 97-102	 **attackbox here**
    sprite('Action_000_08', 6)	# 103-108	 **attackbox here**
    sprite('Action_000_09', 7)	# 109-115	 **attackbox here**
    sprite('Action_000_10', 7)	# 116-122	 **attackbox here**
    sprite('Action_000_11', 6)	# 123-128	 **attackbox here**
    sprite('Action_000_12', 6)	# 129-134	 **attackbox here**
    sprite('Action_000_13', 5)	# 135-139	 **attackbox here**
    sprite('Action_000_14', 5)	# 140-144	 **attackbox here**
    sprite('Action_000_15', 5)	# 145-149	 **attackbox here**
    sprite('Action_000_16', 6)	# 150-155	 **attackbox here**
    sprite('Action_000_17', 6)	# 156-161	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 162-162

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_241_00', 2)	# 1-2
    sprite('Action_241_01', 2)	# 3-4
    teleportRelativeX(50000)
    sprite('Action_241_02', 3)	# 5-7
    teleportRelativeX(22000)
    sprite('Action_241_03', 5)	# 8-12
    sprite('Action_241_04', 2)	# 13-14
    GFX_0('EffNmlAtk4CZanzo', 100)
    SFX_3('SE045')
    sprite('Action_241_05', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    sprite('Action_241_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_241_07', 4)	# 20-23
    sprite('Action_241_08', 4)	# 24-27
    sprite('Action_241_09', 4)	# 28-31
    sprite('Action_241_10', 3)	# 32-34
    sprite('Action_241_11', 3)	# 35-37
    sprite('Action_241_12', 3)	# 38-40
    label(0)
    sprite('Action_000_00', 7)	# 41-47	 **attackbox here**
    sprite('Action_000_01', 7)	# 48-54	 **attackbox here**
    sprite('Action_000_02', 6)	# 55-60	 **attackbox here**
    sprite('Action_000_03', 6)	# 61-66	 **attackbox here**
    sprite('Action_000_04', 8)	# 67-74	 **attackbox here**
    sprite('Action_000_05', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_06', 5)	# 80-84	 **attackbox here**
    sprite('Action_000_07', 5)	# 85-89	 **attackbox here**
    sprite('Action_000_08', 6)	# 90-95	 **attackbox here**
    sprite('Action_000_09', 5)	# 96-100	 **attackbox here**
    sprite('Action_000_10', 6)	# 101-106	 **attackbox here**
    sprite('Action_000_11', 8)	# 107-114	 **attackbox here**
    sprite('Action_000_12', 5)	# 115-119	 **attackbox here**
    sprite('Action_000_13', 5)	# 120-124	 **attackbox here**
    sprite('Action_000_14', 6)	# 125-130	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 131-131

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('Action_243_00', 5)	# 1-5
    sprite('Action_243_01', 6)	# 6-11
    physicsXImpulse(2250)
    physicsYImpulse(1500)
    setGravity(150)
    sprite('Action_243_02', 2)	# 12-13
    sprite('Action_243_03', 6)	# 14-19
    tag_voice(0, 'uor158_0', 'uor158_1', '', '')
    sprite('Action_243_04ex01', 4)	# 20-23	 **attackbox here**
    GFX_0('EffNmlAtk3CZanzo', 100)
    RefreshMultihit()
    Unknown1017()
    Unknown1022()
    Unknown1037()
    SFX_3('SE045')
    sprite('Action_243_04ex01', 9)	# 24-32	 **attackbox here**
    Unknown23027()
    sprite('Action_243_05', 5)	# 33-37
    Unknown1018()
    Unknown1023()
    Unknown1038()
    sprite('Action_243_06', 3)	# 38-40
    sprite('Action_243_07', 32767)	# 41-32807
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_246_00', 4)	# 32808-32811
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_246_01', 9)	# 32812-32820
    sprite('Action_246_02', 3)	# 32821-32823
    sprite('Action_246_03', 3)	# 32824-32826

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)
    sprite('null', 12)	# 1-12
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 13-13
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    sprite('Action_160_01', 2)	# 14-15
    Unknown8001(0, 100)
    physicsXImpulse(17000)
    physicsYImpulse(45000)
    setGravity(3100)

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        sendToLabel(1)
    GFX_0('EffFF', 100)
    Unknown36(1)
    Unknown1007(100000)
    Unknown35()
    sprite('Action_160_02', 3)	# 16-18
    GFX_0('EffFF', 100)
    sprite('Action_160_03', 3)	# 19-21
    GFX_0('EffFF', 100)
    Unknown36(1)
    teleportRelativeX(100000)
    Unknown35()
    sprite('Action_160_04', 3)	# 22-24
    GFX_0('EffFF', 100)
    Unknown36(1)
    teleportRelativeX(-100000)
    Unknown35()
    sprite('Action_160_05', 4)	# 25-28
    GFX_0('EffFF', 100)
    Unknown36(1)
    teleportRelativeX(100000)
    Unknown1007(-100000)
    Unknown35()
    sprite('Action_160_06', 2)	# 29-30
    GFX_0('EffFF', 100)
    Unknown36(1)
    teleportRelativeX(100000)
    Unknown1007(100000)
    Unknown35()
    sprite('Action_160_07', 3)	# 31-33
    GFX_0('EffFF', 100)
    Unknown36(1)
    teleportRelativeX(-200000)
    Unknown35()
    sprite('Action_160_08', 2)	# 34-35
    sprite('Action_009_00', 2)	# 36-37
    GFX_0('EffFF', 100)
    Unknown36(1)
    teleportRelativeX(200000)
    Unknown35()
    sprite('Action_009_01', 2)	# 38-39
    sprite('Action_009_02', 2)	# 40-41
    sprite('Action_009_03', 6)	# 42-47	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffNmlAtkAIR5CBlade', 100)
    SFX_3('SE043')
    sprite('Action_009_04', 3)	# 48-50
    sprite('Action_009_05', 3)	# 51-53
    sprite('Action_009_06', 3)	# 54-56
    label(1)
    sprite('Action_160_12', 2)	# 57-58
    sprite('Action_160_13', 3)	# 59-61
    sprite('Action_160_14', 3)	# 62-64
    sprite('Action_000_00', 7)	# 65-71	 **attackbox here**
    sprite('Action_000_01', 7)	# 72-78	 **attackbox here**
    sprite('Action_000_02', 6)	# 79-84	 **attackbox here**
    sprite('Action_000_03', 6)	# 85-90	 **attackbox here**
    sprite('Action_000_04', 8)	# 91-98	 **attackbox here**
    sprite('Action_000_05', 5)	# 99-103	 **attackbox here**
    sprite('Action_000_06', 5)	# 104-108	 **attackbox here**
    sprite('Action_000_07', 5)	# 109-113	 **attackbox here**
    sprite('Action_000_08', 6)	# 114-119	 **attackbox here**
    sprite('Action_000_09', 5)	# 120-124	 **attackbox here**
    sprite('Action_000_10', 6)	# 125-130	 **attackbox here**
    sprite('Action_000_11', 8)	# 131-138	 **attackbox here**
    sprite('Action_000_12', 5)	# 139-143	 **attackbox here**
    sprite('Action_000_13', 5)	# 144-148	 **attackbox here**
    sprite('Action_000_14', 6)	# 149-154	 **attackbox here**

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('Action_242_00', 1)	# 1-1
    sprite('Action_242_01', 1)	# 2-2
    sprite('Action_242_02', 1)	# 3-3
    teleportRelativeX(50000)
    sprite('Action_242_03', 1)	# 4-4
    teleportRelativeX(50000)
    sprite('Action_242_04', 1)	# 5-5
    teleportRelativeX(50000)
    sprite('Action_242_05', 2)	# 6-7
    sprite('Action_242_06', 2)	# 8-9
    sprite('Action_242_07', 1)	# 10-10
    sprite('Action_242_08', 1)	# 11-11
    sprite('Action_242_09', 1)	# 12-12	 **attackbox here**
    GFX_0('EffNmlAtk6BZanzo', 100)
    SFX_3('SE043')
    sprite('Action_242_10', 3)	# 13-15	 **attackbox here**
    sprite('Action_242_11', 4)	# 16-19
    sprite('Action_242_12', 4)	# 20-23
    sprite('Action_242_13', 3)	# 24-26
    sprite('Action_242_14', 3)	# 27-29
    sprite('Action_242_15', 3)	# 30-32
    sprite('Action_242_16', 3)	# 33-35
    loopRest()
    sprite('Action_000_00', 7)	# 36-42	 **attackbox here**
    sprite('Action_000_01', 7)	# 43-49	 **attackbox here**
    sprite('Action_000_02', 6)	# 50-55	 **attackbox here**
    sprite('Action_000_03', 6)	# 56-61	 **attackbox here**
    sprite('Action_000_04', 8)	# 62-69	 **attackbox here**
    sprite('Action_000_05', 5)	# 70-74	 **attackbox here**
    sprite('Action_000_06', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_07', 5)	# 80-84	 **attackbox here**
    sprite('Action_000_08', 6)	# 85-90	 **attackbox here**
    sprite('Action_000_09', 5)	# 91-95	 **attackbox here**
    sprite('Action_000_10', 6)	# 96-101	 **attackbox here**
    sprite('Action_000_11', 8)	# 102-109	 **attackbox here**
    sprite('Action_000_12', 5)	# 110-114	 **attackbox here**
    sprite('Action_000_13', 5)	# 115-119	 **attackbox here**
    sprite('Action_000_14', 6)	# 120-125	 **attackbox here**

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('Action_243_00', 5)	# 1-5
    sprite('Action_243_01', 6)	# 6-11
    physicsXImpulse(2250)
    physicsYImpulse(1500)
    setGravity(150)
    sprite('Action_243_02', 2)	# 12-13
    sprite('Action_243_03', 6)	# 14-19
    sprite('Action_243_04ex01', 4)	# 20-23	 **attackbox here**
    GFX_0('EffNmlAtk3CZanzo', 100)
    RefreshMultihit()
    Unknown1017()
    Unknown1022()
    Unknown1037()
    SFX_3('SE045')
    sprite('Action_243_04ex01', 9)	# 24-32	 **attackbox here**
    Unknown23027()
    sprite('Action_243_05', 5)	# 33-37
    Unknown1018()
    Unknown1023()
    Unknown1038()
    sprite('Action_243_06', 3)	# 38-40
    sprite('Action_243_07', 32767)	# 41-32807
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_246_00', 4)	# 32808-32811
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_246_01', 9)	# 32812-32820
    sprite('Action_246_02', 3)	# 32821-32823
    sprite('Action_246_03', 3)	# 32824-32826

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
    sprite('Action_010_00', 3)	# 1-3
    sprite('Action_045_00', 5)	# 4-8
    Unknown8006(100, 1, 1)
    sprite('Action_045_01', 3)	# 9-11
    sprite('Action_045_02', 3)	# 12-14
    sprite('Action_045_03', 3)	# 15-17
    sprite('Action_045_04', 3)	# 18-20
    sprite('Action_045_05', 3)	# 21-23
    Unknown8006(100, 1, 1)
    sprite('Action_045_06', 3)	# 24-26
    sprite('Action_045_07', 3)	# 27-29
    sprite('Action_045_08', 3)	# 30-32
    label(0)
    sprite('Action_045_09', 3)	# 33-35
    Unknown8006(100, 1, 1)
    sprite('Action_045_10', 3)	# 36-38
    sprite('Action_045_11', 3)	# 39-41
    sprite('Action_045_12', 3)	# 42-44
    sprite('Action_045_13', 3)	# 45-47
    Unknown8006(100, 1, 1)
    sprite('Action_045_14', 3)	# 48-50
    sprite('Action_045_15', 3)	# 51-53
    sprite('Action_045_16', 3)	# 54-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 57-57
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_00', 2)	# 58-59
    SFX_3('SE042')
    sprite('Action_055_01', 3)	# 60-62	 **attackbox here**
    Unknown1084(1)
    sprite('Action_055_02', 2)	# 63-64
    sprite('Action_055_03', 3)	# 65-67	 **attackbox here**
    SFX_4('uor154')
    sprite('Action_055_04', 8)	# 68-75
    sprite('Action_055_05', 5)	# 76-80
    sprite('Action_055_06', 5)	# 81-85

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(52000)
        AirPushbackY(20000)
        YImpluseBeforeWallbounce(1800)
        AirUntechableTime(60)
        Unknown11099(1)
    sprite('Action_056_00', 8)	# 1-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 3)	# 9-11
    Unknown2005()
    Unknown23073()
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_01', 4)	# 12-15
    SFX_1('uor153')
    Unknown5004()
    Unknown36(22)
    Unknown1047(-19000)
    Unknown8007(100, 1, 1)
    Unknown35()
    Unknown2018(0, 80)
    sprite('Action_057_02', 2)	# 16-17
    sprite('Action_057_03', 2)	# 18-19
    sprite('Action_057_04', 2)	# 20-21
    Unknown2018(1, 80)
    teleportRelativeX(-46000)
    Unknown1007(70000)
    physicsXImpulse(2560)
    physicsYImpulse(20000)
    setGravity(2000)
    SFX_3('SE038')
    sprite('Action_057_05', 2)	# 22-23
    teleportRelativeX(-24000)
    Unknown1007(-20000)
    sprite('Action_057_06', 2)	# 24-25
    sprite('Action_057_07', 2)	# 26-27
    sprite('Action_057_08', 2)	# 28-29
    sprite('Action_057_09', 2)	# 30-31
    setGravity(-750)
    Unknown1028(-750)
    sprite('Action_057_10', 6)	# 32-37
    physicsXImpulse(6400)
    physicsYImpulse(-6400)
    sprite('Action_057_11', 2)	# 38-39
    sprite('Action_057_12', 2)	# 40-41	 **attackbox here**
    SFX_3('SE043')
    physicsXImpulse(16000)
    physicsYImpulse(12000)
    Unknown1028(-550)
    setGravity(2800)

    def upon_STATE_END():
        Unknown1019(30)
    sprite('Action_057_13', 2)	# 42-43
    sprite('Action_057_14', 3)	# 44-46
    sprite('Action_057_15', 3)	# 47-49
    sprite('Action_057_16', 4)	# 50-53
    sprite('Action_057_17', 32767)	# 54-32820
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_057_18', 2)	# 32821-32822
    clearUponHandler(1)
    Unknown2005()
    physicsXImpulse(-7000)
    Unknown1028(1000)
    sprite('Action_057_19', 4)	# 32823-32826
    sprite('Action_057_20', 2)	# 32827-32828
    Unknown1084(1)
    sprite('Action_057_21', 2)	# 32829-32830

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
    sprite('Action_010_00', 3)	# 1-3
    sprite('Action_045_00', 5)	# 4-8
    Unknown8006(100, 1, 1)
    sprite('Action_045_01', 3)	# 9-11
    sprite('Action_045_02', 3)	# 12-14
    sprite('Action_045_03', 3)	# 15-17
    sprite('Action_045_04', 3)	# 18-20
    sprite('Action_045_05', 3)	# 21-23
    Unknown8006(100, 1, 1)
    sprite('Action_045_06', 3)	# 24-26
    sprite('Action_045_07', 3)	# 27-29
    sprite('Action_045_08', 3)	# 30-32
    label(0)
    sprite('Action_045_09', 3)	# 33-35
    Unknown8006(100, 1, 1)
    sprite('Action_045_10', 3)	# 36-38
    sprite('Action_045_11', 3)	# 39-41
    sprite('Action_045_12', 3)	# 42-44
    sprite('Action_045_13', 3)	# 45-47
    Unknown8006(100, 1, 1)
    sprite('Action_045_14', 3)	# 48-50
    sprite('Action_045_15', 3)	# 51-53
    sprite('Action_045_16', 3)	# 54-56
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 1)	# 57-57
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_00', 2)	# 58-59
    SFX_3('SE042')
    sprite('Action_055_01', 3)	# 60-62	 **attackbox here**
    Unknown1084(1)
    sprite('Action_055_02', 2)	# 63-64
    sprite('Action_055_03', 3)	# 65-67	 **attackbox here**
    SFX_4('uor154')
    sprite('Action_055_04', 8)	# 68-75
    sprite('Action_055_05', 5)	# 76-80
    sprite('Action_055_06', 5)	# 81-85

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(52000)
        AirPushbackY(20000)
        AirUntechableTime(60)
        Unknown11099(1)
    sprite('Action_056_00', 8)	# 1-8
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 3)	# 9-11
    Unknown5000(17, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_057_01', 4)	# 12-15
    SFX_1('uor153')
    Unknown5004()
    Unknown36(22)
    Unknown2005()
    Unknown1047(-19000)
    Unknown8007(100, 1, 1)
    Unknown35()
    Unknown2018(0, 80)
    sprite('Action_057_02', 2)	# 16-17
    sprite('Action_057_03', 2)	# 18-19
    sprite('Action_057_04', 2)	# 20-21
    Unknown2018(1, 80)
    teleportRelativeX(-46000)
    Unknown1007(70000)
    physicsXImpulse(2560)
    physicsYImpulse(20000)
    setGravity(2000)
    SFX_3('SE038')
    Unknown23073()
    sprite('Action_057_05', 2)	# 22-23
    teleportRelativeX(-24000)
    Unknown1007(-20000)
    sprite('Action_057_06', 2)	# 24-25
    sprite('Action_057_07', 2)	# 26-27
    sprite('Action_057_08', 2)	# 28-29
    sprite('Action_057_09', 2)	# 30-31
    setGravity(-750)
    Unknown1028(-750)
    sprite('Action_057_10', 6)	# 32-37
    physicsXImpulse(6400)
    physicsYImpulse(-6400)
    sprite('Action_057_11', 2)	# 38-39
    sprite('Action_057_12', 2)	# 40-41	 **attackbox here**
    SFX_3('SE043')
    physicsXImpulse(16000)
    physicsYImpulse(12000)
    Unknown1028(-550)
    setGravity(2800)

    def upon_STATE_END():
        Unknown1019(30)
    sprite('Action_057_13', 2)	# 42-43
    sprite('Action_057_14', 3)	# 44-46
    sprite('Action_057_15', 3)	# 47-49
    sprite('Action_057_16', 4)	# 50-53
    sprite('Action_057_17', 32767)	# 54-32820
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_057_18', 2)	# 32821-32822
    clearUponHandler(1)
    Unknown2005()
    physicsXImpulse(-7000)
    Unknown1028(1000)
    sprite('Action_057_19', 4)	# 32823-32826
    sprite('Action_057_20', 2)	# 32827-32828
    Unknown1084(1)
    sprite('Action_057_21', 2)	# 32829-32830

@State
def AN_NmlAtk2B__misiyou():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Unknown9016(1)
    sprite('Action_001_00', 4)	# 1-4
    sprite('Action_001_01', 3)	# 5-7
    sprite('Action_001_02', 3)	# 8-10	 **attackbox here**
    GFX_0('EffNmlAtk2BBlade', 100)
    sprite('Action_001_03', 7)	# 11-17
    sprite('Action_001_04', 4)	# 18-21
    sprite('Action_001_05', 3)	# 22-24

@State
def AN_NmlAtkAir5B__misiyou():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(15000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_008_00', 4)	# 1-4
    sprite('Action_008_01', 3)	# 5-7
    sprite('Action_008_02', 1)	# 8-8
    GFX_0('EffNmlAtkAIR5BZanzo', 100)
    sprite('Action_008_03', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    sprite('Action_008_04', 6)	# 12-17
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_008_05', 5)	# 18-22
    sprite('Action_008_06', 5)	# 23-27

@State
def AN_NmlAtk66B_misiyou():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Unknown9016(1)
    sprite('Action_402_00', 2)	# 1-2
    sprite('Action_402_01', 2)	# 3-4
    sprite('Action_402_02', 3)	# 5-7
    teleportRelativeX(36000)
    sprite('Action_402_03', 2)	# 8-9
    sprite('Action_402_04', 2)	# 10-11	 **attackbox here**
    GFX_0('Eff66BZanzo1', 100)
    sprite('Action_402_05', 5)	# 12-16
    sprite('Action_402_06', 4)	# 17-20
    sprite('Action_402_07', 3)	# 21-23
    sprite('Action_402_08', 2)	# 24-25

@State
def AN_NmlAtk3C_misiyou():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Unknown23027()
        JumpCancel_(0)
        callSubroutine('ChainRoot')
    sprite('Action_243_00', 3)	# 1-3
    sprite('Action_243_01', 4)	# 4-7
    physicsXImpulse(10500)
    physicsYImpulse(9000)
    setGravity(850)
    sprite('Action_243_02', 2)	# 8-9
    sprite('Action_243_03', 6)	# 10-15
    sprite('Action_243_04', 4)	# 16-19	 **attackbox here**
    GFX_0('EffNmlAtk3CZanzo', 100)
    RefreshMultihit()
    sprite('Action_243_05', 5)	# 20-24
    Recovery()
    Unknown2063()
    Unknown2001()
    sprite('Action_243_06', 3)	# 25-27
    sprite('Action_243_07', 32767)	# 28-32794
    sendToLabelUpon(2, 0)
    label(0)
    sprite('Action_243_08', 2)	# 32795-32796
    Unknown1084(1)
    Unknown18009(1)
    sprite('Action_243_09', 1)	# 32797-32797

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(800)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(5)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(40000)
        Unknown9016(1)
        sendToLabelUpon(2, 1)
    sprite('Action_111_00', 3)	# 1-3
    sprite('Action_111_01', 4)	# 4-7
    Unknown1084(1)
    sprite('Action_111_02', 2)	# 8-9
    Unknown7006('uor202_0', 100, 846360437, 828322608, 0, 0, 100, 846360437, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown8001(0, 100)
    physicsXImpulse(15000)
    Unknown1028(-600)
    physicsYImpulse(45000)
    setGravity(1500)
    sprite('Action_111_03', 2)	# 10-11	 **attackbox here**
    RefreshMultihit()
    GFX_0('InvincibleAttackBlade', 100)
    SFX_3('SE045')
    sprite('Action_111_04', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_05', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_06', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_07', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_08', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    setInvincible(0)
    sprite('Action_111_09', 4)	# 22-25
    Unknown1019(60)
    Unknown1028(0)
    physicsYImpulse(10240)
    setGravity(500)
    sprite('Action_111_10', 4)	# 26-29
    sprite('Action_111_11', 3)	# 30-32
    setGravity(2000)
    sprite('Action_111_12', 3)	# 33-35
    sprite('Action_111_13', 3)	# 36-38
    sprite('Action_111_14', 3)	# 39-41
    sprite('Action_111_15', 3)	# 42-44
    label(0)
    sprite('Action_111_16', 3)	# 45-47
    sprite('Action_111_17', 3)	# 48-50
    gotoLabel(0)
    label(1)
    sprite('Action_111_18', 4)	# 51-54
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_111_19', 5)	# 55-59
    sprite('Action_111_20', 3)	# 60-62
    Unknown18009(0)
    sprite('Action_111_21', 3)	# 63-65

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(800)
        Unknown11092(1)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Hitstop(5)
        AirUntechableTime(42)
        AirPushbackX(5000)
        AirPushbackY(40000)
        Unknown9016(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('Action_111_02', 9)	# 1-9
    Unknown1084(1)
    sprite('Action_111_02', 2)	# 10-11
    Unknown7006('uor202_0', 100, 846360437, 828322352, 0, 0, 100, 846360437, 845099568, 0, 0, 100, 0, 0, 0, 0, 0)
    physicsXImpulse(18000)
    Unknown1028(-700)
    physicsYImpulse(30000)
    setGravity(1200)
    sprite('Action_111_03ex01', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    GFX_0('InvincibleAttackBlade', 100)
    SFX_3('SE045')
    sprite('Action_111_04ex01', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_05ex01', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_06ex01', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_07ex01', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_08ex01', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('Action_111_09', 4)	# 24-27
    setInvincible(0)
    Unknown1019(60)
    Unknown1028(0)
    physicsYImpulse(10240)
    setGravity(500)
    sprite('Action_111_10', 4)	# 28-31
    sprite('Action_111_11', 3)	# 32-34
    setGravity(2000)
    sprite('Action_111_12', 3)	# 35-37
    sprite('Action_111_13', 3)	# 38-40
    sprite('Action_111_14', 3)	# 41-43
    sprite('Action_111_15', 3)	# 44-46
    label(0)
    sprite('Action_111_16', 3)	# 47-49
    sprite('Action_111_17', 3)	# 50-52
    gotoLabel(0)
    label(1)
    sprite('Action_111_18', 2)	# 53-54
    Unknown8000(100, 1, 1)
    Unknown18009(1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_111_19', 3)	# 55-57
    sprite('Action_111_20', 3)	# 58-60
    Unknown18009(0)
    sprite('Action_111_21', 3)	# 61-63

@State
def AssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        Unknown9016(1)
        Hitstop(9)
        AirUntechableTime(45)
        Unknown9154(25)
        AirPushbackX(23000)
        AirPushbackY(16000)
        AirHitstunAnimation(13)
        Unknown11028(20)
    sprite('Action_099_00', 4)	# 1-4
    sprite('Action_099_01', 4)	# 5-8
    Unknown7006('uor200_0', 100, 846360437, 828321840, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_099_02', 2)	# 9-10
    physicsXImpulse(80000)
    Unknown1028(-8400)
    GFX_0('Assault_Zanzo', 100)
    SFX_3('SE038')
    sprite('Action_099_02', 1)	# 11-11
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    GFX_0('Assault_Blade', 100)
    SFX_3('SE045')
    sprite('Action_099_03', 4)	# 12-15	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    Unknown1045(5000)
    sprite('Action_099_04', 4)	# 16-19
    Unknown23027()
    Recovery()
    sprite('Action_099_05', 5)	# 20-24
    sprite('Action_099_06', 4)	# 25-28
    sprite('Action_099_07', 4)	# 29-32
    sprite('Action_099_08', 4)	# 33-36

@State
def AssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(80)
        Unknown9016(1)
        AirUntechableTime(45)
        Hitstop(9)
        AirPushbackX(23000)
        AirPushbackY(16000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
    sprite('Action_100_00', 5)	# 1-5
    Unknown1084(1)
    sprite('Action_100_01', 3)	# 6-8
    sprite('Action_100_01', 4)	# 9-12
    sprite('Action_100_02', 6)	# 13-18
    Unknown7006('uor200_0', 100, 846360437, 845099056, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_100_03', 2)	# 19-20	 **attackbox here**
    StartMultihit()
    GFX_0('Assault_Zanzo', 100)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    physicsXImpulse(125000)
    Unknown1028(-8000)
    SFX_3('SE038')

    def upon_77():
        Unknown1019(5)
        Unknown1034(5)
        Unknown2038(1)
    GFX_0('Assault_Blade', 100)
    SFX_3('SE045')
    sprite('Action_100_05', 3)	# 21-23	 **attackbox here**
    sprite('Action_100_06ex01', 3)	# 24-26	 **attackbox here**
    sprite('Action_100_07', 2)	# 27-28
    Unknown23027()
    Recovery()
    Unknown1084(1)
    sprite('Action_100_08', 3)	# 29-31
    sprite('Action_100_10', 6)	# 32-37
    sprite('Action_100_11', 5)	# 38-42
    ExitState()

@State
def CommandOrderA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_147_00', 4)	# 1-4
    sprite('Action_147_01', 8)	# 5-12
    Unknown7006('uor306_0', 100, 863137653, 828323376, 0, 0, 100, 846360437, 811546416, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown23029(11, 0, 0)
    GFX_0('Tan_214A', 100)
    Unknown38(11, 1)
    sprite('Action_147_02', 6)	# 13-18
    Unknown14070('CommandOrderAdd_A')
    sprite('Action_147_03', 1)	# 19-19
    sprite('Action_147_03', 4)	# 20-23
    Recovery()
    Unknown14072('CommandOrderAdd_A')
    sprite('Action_147_04', 4)	# 24-27
    sprite('Action_147_04', 5)	# 28-32
    Unknown14074('CommandOrderAdd_A')
    sprite('Action_147_05', 4)	# 33-36
    sprite('Action_147_06', 3)	# 37-39

@State
def CommandOrderB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_148_00', 5)	# 1-5
    sprite('Action_148_01', 3)	# 6-8
    sprite('Action_148_01', 1)	# 9-9
    Unknown23029(11, 0, 0)
    GFX_0('Tan_214B', 100)
    Unknown38(11, 1)
    SFX_1('uor204_0')
    sprite('Action_148_02', 2)	# 10-11
    sprite('Action_148_03', 2)	# 12-13
    Unknown14070('CommandOrderAdd_B')
    sprite('Action_148_04', 5)	# 14-18
    sprite('Action_148_05', 3)	# 19-21
    sprite('Action_148_06', 5)	# 22-26
    sprite('Action_148_06', 8)	# 27-34
    Recovery()
    Unknown14072('CommandOrderAdd_B')
    sprite('Action_148_07', 5)	# 35-39
    Unknown14074('CommandOrderAdd_B')
    sprite('Action_148_08', 5)	# 40-44

@State
def CommandOrderAdd_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
    sprite('Action_152_00', 4)	# 1-4
    Unknown21007(11, 32)
    sprite('Action_152_01', 4)	# 5-8
    Unknown7006('uor205_0', 100, 846360437, 828323120, 0, 0, 100, 846360437, 845100336, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_152_02', 8)	# 9-16
    sprite('Action_152_03', 5)	# 17-21
    sprite('Action_152_04', 23)	# 22-44
    Recovery()
    sprite('Action_152_05', 9)	# 45-53
    sprite('Action_152_06', 9)	# 54-62

@State
def CommandOrderAdd_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
    sprite('Action_153_00', 2)	# 1-2
    Unknown21007(11, 33)
    sprite('Action_153_01', 2)	# 3-4
    Unknown7006('uor206_0', 100, 846360437, 828323376, 0, 0, 100, 846360437, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_153_02', 4)	# 5-8
    sprite('Action_153_03', 6)	# 9-14
    sprite('Action_153_04', 4)	# 15-18
    sprite('Action_153_04', 2)	# 19-20
    Recovery()
    sprite('Action_153_05', 10)	# 21-30
    sprite('Action_153_06', 8)	# 31-38
    sprite('Action_153_07', 7)	# 39-45

@State
def CommandOrderAirA():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('Action_078_00', 2)	# 1-2
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    sprite('Action_078_01', 2)	# 3-4
    sprite('Action_078_02', 3)	# 5-7
    Unknown22004(12, 1)
    Unknown23029(11, 0, 0)
    GFX_0('Tan_Air214A', 100)
    Unknown38(11, 1)
    SFX_1('uor204_1')
    sprite('Action_078_03', 3)	# 8-10
    sprite('Action_078_04', 4)	# 11-14
    sprite('Action_078_05', 4)	# 15-18
    sprite('Action_078_04', 1)	# 19-19
    Unknown1018()
    Unknown1023()
    Unknown1019(0)
    YAccel(0)
    Unknown1015(-8000)
    Unknown1021(15000)
    Unknown1043()
    sprite('Action_078_04', 3)	# 20-22
    Recovery()
    sprite('Action_078_06', 4)	# 23-26
    sprite('Action_078_07', 5)	# 27-31
    sprite('Action_078_08', 5)	# 32-36
    label(0)
    sprite('Action_078_09', 4)	# 37-40
    sprite('Action_078_10', 4)	# 41-44
    gotoLabel(0)
    label(10)
    sprite('Action_078_11', 4)	# 45-48
    Recovery()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_078_12', 6)	# 49-54
    sprite('Action_078_13', 4)	# 55-58
    sprite('Action_078_14', 3)	# 59-61

@State
def CommandOrderAirB():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('Action_079_00', 3)	# 1-3
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    sprite('Action_079_01', 3)	# 4-6
    Unknown22004(12, 1)
    sprite('Action_079_02', 3)	# 7-9
    sprite('Action_079_03', 3)	# 10-12
    SFX_1('uor204_2')
    sprite('Action_079_04', 3)	# 13-15
    Unknown23029(11, 0, 0)
    GFX_0('Tan_Air214B', 100)
    Unknown38(11, 1)
    sprite('Action_079_05', 3)	# 16-18
    sprite('Action_079_04', 3)	# 19-21
    sprite('Action_079_05', 3)	# 22-24
    sprite('Action_079_04', 3)	# 25-27
    sprite('Action_079_05', 3)	# 28-30
    sprite('Action_079_04', 3)	# 31-33
    sprite('Action_079_05', 1)	# 34-34
    Unknown1018()
    Unknown1023()
    Unknown1019(0)
    YAccel(0)
    Unknown1015(-1500)
    Unknown1021(10000)
    Unknown1043()
    Recovery()
    sprite('Action_079_06', 3)	# 35-37
    sprite('Action_079_07', 5)	# 38-42
    sprite('Action_079_08', 5)	# 43-47
    label(0)
    sprite('Action_079_09', 4)	# 48-51
    sprite('Action_079_10', 4)	# 52-55
    gotoLabel(0)
    label(10)
    sprite('Action_079_11', 4)	# 56-59
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_079_12', 6)	# 60-65
    sprite('Action_079_13', 4)	# 66-69
    sprite('Action_079_14', 3)	# 70-72

@State
def AssaultEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2200)
        AttackP1(80)
        AttackP2(80)
        GroundedHitstunAnimation(5)
        AirHitstunAnimation(5)
        Unknown9016(1)
        Hitstop(3)
        AirPushbackX(6000)
        AirPushbackY(15000)
        Unknown11001(20, 20, 20)
        Unknown11091(10)
        Unknown30065(0)

        def upon_77():
            clearUponHandler(77)
            Unknown2038(1)
            Unknown2017(0)
            Unknown2015(40)
            Unknown14083(0)
            sendToLabel(0)

        def upon_STATE_END():
            Unknown2006()
    sprite('Action_101_00', 3)	# 1-3
    sprite('Action_101_00', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_101_01', 6)	# 5-10
    StartMultihit()
    Unknown7006('uor201_0', 100, 846360437, 828322096, 0, 0, 100, 846360437, 845099312, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_101_02', 1)	# 11-11	 **attackbox here**
    GFX_0('Assault_Zanzo', 100)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    physicsXImpulse(105000)
    SFX_3('SE038')
    Unknown2015(200)
    sprite('Action_101_03', 7)	# 12-18	 **attackbox here**
    GFX_0('Assault_Blade', 100)
    SFX_3('SE045')
    sprite('Action_101_04', 4)	# 19-22
    Unknown23027()
    Recovery()
    clearUponHandler(77)
    sprite('Action_101_05', 4)	# 23-26
    Unknown1084(1)
    Unknown1045(3000)
    sprite('Action_101_06', 4)	# 27-30
    loopRest()
    gotoLabel(9)
    label(0)
    sprite('Action_101_04', 4)	# 31-34
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-1)
    Unknown1019(80)
    sprite('Action_101_05', 4)	# 35-38
    Unknown1019(50)
    Unknown2017(1)
    sprite('Action_101_06', 4)	# 39-42
    Unknown1019(50)
    sprite('Action_101_04', 4)	# 43-46
    Unknown1019(50)
    sprite('Action_101_05', 4)	# 47-50
    GFX_0('Assault_AddAtk', 100)
    Unknown1019(0)
    sprite('Action_101_06', 4)	# 51-54
    sprite('Action_101_04', 4)	# 55-58
    sprite('Action_101_05', 4)	# 59-62
    sprite('Action_101_06', 4)	# 63-66
    sprite('Action_101_04', 4)	# 67-70
    sprite('Action_101_05', 4)	# 71-74
    sprite('Action_101_06', 4)	# 75-78
    Unknown14083(1)
    sprite('Action_101_04', 4)	# 79-82
    sprite('Action_101_05', 4)	# 83-86
    sprite('Action_101_06', 4)	# 87-90
    label(9)
    sprite('Action_101_07', 4)	# 91-94
    Recovery()
    Unknown2017(1)
    Unknown2015(-1)
    sprite('Action_101_08', 4)	# 95-98
    sprite('Action_101_09', 4)	# 99-102
    sprite('Action_015_00', 2)	# 103-104
    sprite('Action_015_01', 2)	# 105-106

@State
def CommandOrderEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('Action_149_00', 4)	# 1-4
    sprite('Action_149_01', 6)	# 5-10
    Unknown23125('')
    Unknown2058(-5000)
    Unknown23029(11, 0, 0)
    GFX_0('Tan_214EX', 100)
    Unknown38(11, 1)
    Unknown7006('uor208_0', 100, 846360437, 828323888, 0, 0, 100, 846360437, 845101104, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_149_02', 5)	# 11-15
    sprite('Action_149_03', 6)	# 16-21
    sprite('Action_149_04', 11)	# 22-32
    sprite('Action_149_05', 3)	# 33-35
    sprite('Action_149_05', 16)	# 36-51
    Recovery()
    sprite('Action_149_06', 8)	# 52-59
    sprite('Action_149_07', 8)	# 60-67

@State
def CommandOrderAirEx():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('Action_080_00', 3)	# 1-3
    clearUponHandler(2)
    sendToLabelUpon(2, 10)
    Unknown2006()
    Unknown1084(1)
    physicsXImpulse(-9000)
    physicsYImpulse(24000)
    setGravity(800)
    sprite('Action_080_00', 4)	# 4-7
    Unknown23125('')
    Unknown2058(-5000)
    Unknown7006('uor207_0', 100, 846360437, 828323632, 0, 0, 100, 846360437, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_080_01', 6)	# 8-13
    sprite('Action_080_02', 6)	# 14-19
    Unknown23029(11, 0, 0)
    GFX_0('Tan_214AirEX', 100)
    Unknown38(11, 1)
    sprite('Action_080_03', 2)	# 20-21
    Unknown1036(1000)
    sprite('Action_080_04', 3)	# 22-24
    sprite('Action_080_05', 4)	# 25-28
    sprite('Action_080_06', 4)	# 29-32
    sprite('Action_080_07', 4)	# 33-36
    sprite('Action_080_08', 4)	# 37-40
    sprite('Action_080_09', 4)	# 41-44
    sprite('Action_080_10', 4)	# 45-48
    Recovery()
    sprite('Action_080_11', 5)	# 49-53
    sprite('Action_080_12', 5)	# 54-58
    label(0)
    sprite('Action_080_13', 4)	# 59-62
    sprite('Action_080_14', 4)	# 63-66
    gotoLabel(0)
    label(10)
    sprite('Action_079_11', 4)	# 67-70
    Recovery()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_079_12', 6)	# 71-76
    sprite('Action_079_13', 3)	# 77-79
    sprite('Action_079_14', 2)	# 80-81

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Unknown9266(13)
        Hitstop(3)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        Unknown2021(1)
    sprite('Action_120_00', 1)	# 1-1
    Unknown23029(11, 0, 0)
    setInvincible(1)
    Unknown1084(1)
    sprite('Action_120_00', 17)	# 2-18
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uor250_0', 'uor250_1', '', '')
    sprite('Action_120_01', 3)	# 19-21	 **attackbox here**
    sprite('Action_120_02', 3)	# 22-24	 **attackbox here**
    sprite('Action_120_03', 2)	# 25-26	 **attackbox here**
    sprite('Action_120_03', 1)	# 27-27	 **attackbox here**
    GFX_0('IW_Tan', 100)
    Unknown38(11, 1)
    sprite('Action_120_04', 3)	# 28-30	 **attackbox here**
    sprite('Action_120_05', 23)	# 31-53
    sprite('Action_120_06', 4)	# 54-57
    sprite('Action_120_07', 10)	# 58-67
    sprite('Action_120_08', 4)	# 68-71
    sprite('Action_120_09', 4)	# 72-75
    SFX_3('SE010')
    Unknown4004('6566666563745f3331390000000000000000000000000000000000000000000064000000')
    tag_voice(0, 'uor251_0', 'uor251_1', '', '')
    sprite('Action_120_10', 10)	# 76-85
    Unknown2021(0)
    setInvincible(0)
    sprite('Action_120_11', 45)	# 86-130
    sprite('Action_120_12', 6)	# 131-136
    sprite('Action_120_13', 4)	# 137-140
    sprite('Action_120_14', 4)	# 141-144
    sprite('Action_120_15', 8)	# 145-152
    sprite('Action_120_16', 6)	# 153-158
    sprite('Action_120_17', 4)	# 159-162

@State
def UltimateShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Unknown9266(13)
        Hitstop(3)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        PushbackX(0)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        Unknown2021(1)
        Unknown11091(15)

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown2038(1)
                setInvincible(1)
    sprite('Action_120_00', 1)	# 1-1
    Unknown23029(11, 0, 0)
    setInvincible(1)
    Unknown1084(1)
    sprite('Action_120_00', 17)	# 2-18
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'uor250_0', 'uor250_1', '', '')
    sprite('Action_120_01', 3)	# 19-21	 **attackbox here**
    sprite('Action_120_02', 3)	# 22-24	 **attackbox here**
    sprite('Action_120_03', 2)	# 25-26	 **attackbox here**
    sprite('Action_120_03', 1)	# 27-27	 **attackbox here**
    GFX_0('IW_Tan_OD', 100)
    Unknown38(11, 1)
    sprite('Action_120_04', 3)	# 28-30	 **attackbox here**
    sprite('Action_120_05', 23)	# 31-53
    sprite('Action_120_06', 4)	# 54-57
    sprite('Action_120_07', 10)	# 58-67
    sprite('Action_120_08', 4)	# 68-71
    sprite('Action_120_09', 4)	# 72-75
    SFX_3('SE010')
    Unknown4004('6566666563745f3331390000000000000000000000000000000000000000000064000000')
    tag_voice(0, 'uor251_0', 'uor251_1', '', '')
    sprite('Action_120_10', 10)	# 76-85
    Unknown2021(0)
    if (not SLOT_2):
        setInvincible(0)
    sprite('Action_120_11', 45)	# 86-130
    sprite('Action_120_12', 6)	# 131-136
    sprite('Action_120_13', 4)	# 137-140
    sprite('Action_120_14', 4)	# 141-144
    sprite('Action_120_15', 8)	# 145-152
    if SLOT_2:
        _gotolabel(100)
    sprite('Action_120_16', 6)	# 153-158
    sprite('Action_120_17', 4)	# 159-162
    ExitState()
    label(100)
    sprite('Action_100_00', 5)	# 163-167
    sprite('Action_100_00', 45)	# 168-212
    Unknown2036(45, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown1084(1)
    Damage(2800)
    Unknown9266(0)
    Hitstop(0)
    AirUntechableTime(180)
    Unknown9310(1)
    Unknown11001(0, 25, 25)
    Unknown2017(0)
    Unknown2015(200)
    tag_voice(0, 'uor252_0', 'uor252_1', '', '')
    sprite('Action_100_01', 3)	# 213-215
    sprite('Action_100_02', 6)	# 216-221
    tag_voice(0, 'uor253_0', 'uor253_1', '', '')
    sprite('Action_100_03', 3)	# 222-224	 **attackbox here**
    GFX_0('Assault_Zanzo', 100)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    physicsXImpulse(190000)
    Unknown1028(-7500)
    GFX_0('Ultimate_kirakira_matomeX', 100)
    SFX_3('SE038')

    def upon_78():
        clearUponHandler(78)
        SFX_3('SE_BigBomb')
        SFX_0('025_cleanhit_slash')
        SLOT_51 = 1

    def upon_82():
        clearUponHandler(82)
        SFX_0('025_cleanhit_slash')
    sprite('Action_100_03', 2)	# 225-226	 **attackbox here**
    GFX_0('UltimateShot_ODBlade', 100)
    GFX_0('Assault_Blade', 100)
    SFX_3('SE045')
    sprite('Action_100_04', 3)	# 227-229	 **attackbox here**
    sprite('Action_100_05', 4)	# 230-233	 **attackbox here**
    sprite('Action_100_06', 4)	# 234-237
    sprite('Action_100_07', 5)	# 238-242
    Unknown1084(1)
    Unknown2017(1)
    Unknown1045(10000)
    if (not SLOT_51):
        sendToLabel(102)
    label(101)
    sprite('Action_101_04', 5)	# 243-247
    sprite('Action_101_05', 5)	# 248-252
    sprite('Action_101_06', 5)	# 253-257
    sprite('Action_101_07', 5)	# 258-262
    sprite('Action_101_04', 5)	# 263-267
    sprite('Action_101_05', 5)	# 268-272
    sprite('Action_101_06', 5)	# 273-277
    sprite('Action_101_07', 5)	# 278-282
    label(102)
    sprite('Action_100_08', 5)	# 283-287
    sprite('Action_100_09', 7)	# 288-294
    sprite('Action_100_10', 6)	# 295-300
    sprite('Action_100_11', 6)	# 301-306

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(3)
        Damage(850)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(1)
        Unknown9016(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9154(10)
        Unknown9142(15)
        Unknown11056(0)
        Unknown11064(1)
        Unknown11072(1, 200000, 0)
        Unknown11091(10)

        def upon_78():
            SLOT_51 = 1
            setInvincible(1)
            clearUponHandler(78)
            Unknown13024(0)
        Unknown11069('UltimateAssault')
    sprite('Action_262_00', 5)	# 1-5
    setInvincible(1)
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 5)	# 11-15
    tag_voice(1, 'uor254_0', 'uor254_1', 'uor254_2', '')
    sprite('Action_262_03', 4)	# 16-19
    sprite('Action_262_04', 4)	# 20-23
    sprite('Action_262_03', 4)	# 24-27
    sprite('Action_262_04', 4)	# 28-31
    sprite('Action_262_03', 4)	# 32-35
    sprite('Action_262_04', 4)	# 36-39
    sprite('Action_262_03', 4)	# 40-43
    sprite('Action_262_04', 4)	# 44-47
    sprite('Action_262_05', 5)	# 48-52
    sprite('Action_262_06', 5)	# 53-57
    sprite('Action_117_00', 4)	# 58-61
    sprite('Action_117_01', 3)	# 62-64
    physicsXImpulse(42000)
    Unknown1028(-5000)
    sprite('Action_117_02', 2)	# 65-66	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(80000)
    Unknown1028(-2500)
    GFX_0('Eff66CBlade1', 100)
    SFX_3('SE041')
    sprite('Action_117_03', 2)	# 67-68	 **attackbox here**
    sprite('Action_117_04', 2)	# 69-70	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade2', 100)
    SFX_3('SE041')
    sprite('Action_117_05', 2)	# 71-72	 **attackbox here**
    if (not SLOT_51):
        setInvincible(0)
    sprite('Action_117_06', 2)	# 73-74	 **attackbox here**
    RefreshMultihit()
    sprite('Action_117_07', 2)	# 75-76	 **attackbox here**
    sprite('Action_117_08', 2)	# 77-78	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade3', 100)
    SFX_3('SE041')
    tag_voice(0, 'uor255_0', 'uor255_1', 'uor255_2', '')
    sprite('Action_117_09', 2)	# 79-80	 **attackbox here**
    sprite('Action_117_10', 2)	# 81-82	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade4', 100)
    SFX_3('SE041')
    sprite('Action_117_11', 2)	# 83-84	 **attackbox here**
    sprite('Action_117_12', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade5', 100)
    SFX_3('SE041')
    sprite('Action_117_13', 2)	# 87-88	 **attackbox here**
    loopRest()
    sprite('Action_117_14', 2)	# 89-90
    Unknown1084(1)
    sprite('Action_117_15', 2)	# 91-92
    sprite('Action_117_16', 1)	# 93-93
    physicsXImpulse(60000)
    Unknown1028(-10000)
    physicsYImpulse(90000)
    setGravity(15000)
    sprite('Action_117_17', 4)	# 94-97	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE045')
    GFX_0('InvincibleAttackBlade', 100)
    AttackLevel_(4)
    Damage(1400)
    AirPushbackX(1500)
    AirPushbackY(40000)
    YImpluseBeforeWallbounce(800)
    Unknown30048(1)
    PushbackX(30400)
    AirUntechableTime(150)
    Unknown11072(1, 50000, 0)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    clearUponHandler(78)

    def upon_78():
        clearUponHandler(78)
        setInvincible(1)
        Unknown2038(1)
        GFX_0('UltimateAssault_Camera', 100)
        Unknown38(4, 1)
        Unknown36(22)
        setGravity(800)
        physicsXImpulse(1500)
        Unknown35()
    sprite('Action_117_18', 2)	# 98-99
    physicsXImpulse(10000)
    Unknown1028(-500)
    physicsYImpulse(10240)
    setGravity(2500)

    def upon_LANDING():
        clearUponHandler(2)
        if SLOT_2:
            sendToLabel(10)
        else:
            sendToLabel(1)
    sprite('Action_117_19', 4)	# 100-103
    sprite('Action_117_20', 3)	# 104-106
    sprite('Action_117_21', 3)	# 107-109
    sprite('Action_117_22', 3)	# 110-112
    sprite('Action_117_23', 3)	# 113-115
    sprite('Action_117_24', 3)	# 116-118
    label(0)
    sprite('Action_117_25', 3)	# 119-121
    sprite('Action_117_26', 3)	# 122-124
    gotoLabel(0)
    label(1)
    sprite('Action_117_28', 5)	# 125-129
    Unknown1084(1)
    sprite('Action_117_29', 12)	# 130-141
    sprite('Action_117_30', 6)	# 142-147
    sprite('Action_117_31', 6)	# 148-153
    ExitState()
    label(10)
    sprite('Action_117_33', 5)	# 154-158
    Unknown1084(1)
    Unknown21007(4, 32)
    sprite('Action_117_34', 8)	# 159-166
    sprite('Action_117_34', 5)	# 167-171
    tag_voice(0, 'uor256_0', 'uor256_1', 'uor256_2', '')
    Unknown21007(4, 33)
    sprite('Action_117_35', 1)	# 172-172
    GFX_0('Ultimate_kirakira_matome', 100)
    physicsYImpulse(150000)
    setGravity(1900)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3071(4)
    Unknown3070(1)
    SFX_3('SE045')
    sprite('Action_117_36ex01', 1)	# 173-173	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(4200)
    Hitstop(20)
    AirPushbackX(1500)
    AirPushbackY(35000)
    YImpluseBeforeWallbounce(1800)
    Unknown11091(20)
    Unknown9310(1)
    Unknown11064(0)
    Unknown30048(1)
    Unknown2017(0)
    Unknown11069('')

    def upon_78():
        clearUponHandler(78)
        Unknown21012('556c74696d6174655f6b6972616b6972615f6d61746f6d65000000000000000020000000')
        SFX_3('SE_BigBomb')
        SFX_0('025_cleanhit_slash')
        Unknown13024(1)
    sprite('Action_117_36ex01', 15)	# 174-188	 **attackbox here**
    GFX_0('UltimateAssault_Blade1', 100)
    sprite('Action_117_36ex01', 1)	# 189-189	 **attackbox here**
    sprite('Action_117_37', 3)	# 190-192
    physicsYImpulse(350000)
    setGravity(40000)
    sprite('Action_117_37', 3)	# 193-195
    YAccel(0)
    setGravity(0)
    teleportRelativeY(1600000)
    Unknown21007(4, 34)
    sprite('Action_117_38', 2)	# 196-197
    physicsYImpulse(48000)
    setGravity(2500)
    sprite('Action_117_39', 4)	# 198-201
    physicsYImpulse(8000)
    sprite('Action_117_40', 4)	# 202-205
    sprite('Action_117_41', 4)	# 206-209
    sendToLabelUpon(2, 20)
    sprite('Action_117_42', 3)	# 210-212
    sprite('Action_117_43', 3)	# 213-215
    sprite('Action_117_44', 3)	# 216-218
    label(11)
    sprite('Action_117_45', 3)	# 219-221
    sprite('Action_117_46', 3)	# 222-224
    gotoLabel(11)
    label(20)
    sprite('Action_117_47', 3)	# 225-227
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    Unknown3029(0)
    Unknown1084(1)
    sprite('Action_117_48', 19)	# 228-246
    sprite('Action_117_49', 3)	# 247-249
    sprite('Action_117_50', 2)	# 250-251

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(3)
        Damage(850)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
        Hitstop(1)
        Unknown9016(1)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(2)
        Unknown9154(10)
        Unknown9142(15)
        Unknown11056(0)
        Unknown11064(1)
        Unknown11072(1, 200000, 0)
        Unknown11091(10)

        def upon_78():
            SLOT_51 = 1
            setInvincible(1)
            clearUponHandler(78)
            Unknown13024(0)
        Unknown11069('UltimateAssaultOD')
    sprite('Action_262_00', 5)	# 1-5
    setInvincible(1)
    Unknown2036(50, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    sprite('Action_262_01', 5)	# 6-10
    sprite('Action_262_02', 5)	# 11-15
    tag_voice(1, 'uor254_0', 'uor254_1', 'uor254_2', '')
    sprite('Action_262_03', 4)	# 16-19
    sprite('Action_262_04', 4)	# 20-23
    sprite('Action_262_03', 4)	# 24-27
    sprite('Action_262_04', 4)	# 28-31
    sprite('Action_262_03', 4)	# 32-35
    sprite('Action_262_04', 4)	# 36-39
    sprite('Action_262_03', 4)	# 40-43
    sprite('Action_262_04', 4)	# 44-47
    sprite('Action_262_05', 5)	# 48-52
    sprite('Action_262_06', 5)	# 53-57
    sprite('Action_117_00', 4)	# 58-61
    sprite('Action_117_01', 3)	# 62-64
    physicsXImpulse(42000)
    Unknown1028(-5000)
    sprite('Action_117_02', 2)	# 65-66	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(80000)
    Unknown1028(-2500)
    GFX_0('Eff66CBlade1', 100)
    SFX_3('SE041')
    sprite('Action_117_03', 2)	# 67-68	 **attackbox here**
    sprite('Action_117_04', 2)	# 69-70	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade2', 100)
    SFX_3('SE041')
    sprite('Action_117_05', 2)	# 71-72	 **attackbox here**
    sprite('Action_117_06', 2)	# 73-74	 **attackbox here**
    RefreshMultihit()
    sprite('Action_117_07', 2)	# 75-76	 **attackbox here**
    sprite('Action_117_08', 2)	# 77-78	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade3', 100)
    SFX_3('SE041')
    tag_voice(0, 'uor255_0', 'uor255_1', 'uor255_2', '')
    sprite('Action_117_09', 2)	# 79-80	 **attackbox here**
    sprite('Action_117_10', 2)	# 81-82	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade4', 100)
    SFX_3('SE041')
    sprite('Action_117_11', 2)	# 83-84	 **attackbox here**
    sprite('Action_117_12', 2)	# 85-86	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade5', 100)
    SFX_3('SE041')
    sprite('Action_117_13', 2)	# 87-88	 **attackbox here**
    loopRest()
    sprite('Action_117_14', 2)	# 89-90
    setInvincible(0)
    Unknown1084(1)
    sprite('Action_117_15', 2)	# 91-92
    sprite('Action_117_16', 1)	# 93-93
    physicsXImpulse(60000)
    Unknown1028(-10000)
    physicsYImpulse(90000)
    setGravity(15000)
    sprite('Action_117_17', 4)	# 94-97	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE045')
    GFX_0('InvincibleAttackBlade', 100)
    AttackLevel_(4)
    Damage(1400)
    AirPushbackX(1500)
    AirPushbackY(14000)
    YImpluseBeforeWallbounce(500)
    Unknown30048(1)
    PushbackX(30400)
    AirUntechableTime(150)
    Unknown11072(1, 50000, 0)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    clearUponHandler(78)

    def upon_78():
        clearUponHandler(78)
        setInvincible(1)
        Unknown2038(1)
        GFX_0('UltimateAssaultOD_Camera', 100)
        Unknown38(4, 1)
    Unknown11069('UltimateAssault_Tan_AtkCol')
    sprite('Action_117_18', 2)	# 98-99
    physicsXImpulse(10000)
    Unknown1028(-500)
    physicsYImpulse(10240)
    setGravity(2500)

    def upon_LANDING():
        clearUponHandler(2)
        if SLOT_2:
            sendToLabel(10)
        else:
            sendToLabel(1)
    sprite('Action_117_19', 4)	# 100-103
    sprite('Action_117_20', 3)	# 104-106
    sprite('Action_117_21', 3)	# 107-109
    sprite('Action_117_22', 3)	# 110-112
    sprite('Action_117_23', 3)	# 113-115
    sprite('Action_117_24', 3)	# 116-118
    label(0)
    sprite('Action_117_25', 3)	# 119-121
    sprite('Action_117_26', 3)	# 122-124
    gotoLabel(0)
    label(1)
    sprite('Action_117_28', 5)	# 125-129
    Unknown1084(1)
    sprite('Action_117_29', 12)	# 130-141
    sprite('Action_117_30', 6)	# 142-147
    sprite('Action_117_31', 6)	# 148-153
    ExitState()
    label(10)
    sprite('Action_117_28', 2)	# 154-155
    Unknown1084(1)
    Unknown21007(4, 32)
    sprite('Action_117_29', 3)	# 156-158
    sprite('Action_117_30', 2)	# 159-160
    sprite('Action_117_31', 2)	# 161-162
    sprite('Action_120_00', 2)	# 163-164
    sprite('Action_120_01', 2)	# 165-166	 **attackbox here**
    sprite('Action_120_02', 2)	# 167-168	 **attackbox here**
    Unknown23029(11, 0, 0)
    GFX_0('UltimateAssault_Tan', 100)
    Unknown38(11, 1)
    sprite('Action_120_03', 2)	# 169-170	 **attackbox here**
    sprite('Action_120_04', 2)	# 171-172	 **attackbox here**
    sprite('Action_120_05', 2)	# 173-174
    sprite('Action_120_06', 4)	# 175-178
    sprite('Action_120_07', 3)	# 179-181
    sprite('Action_120_08', 3)	# 182-184
    sprite('Action_120_09', 3)	# 185-187
    SFX_3('SE010')
    Unknown4004('6566666563745f3331390000000000000000000000000000000000000000000064000000')
    sprite('Action_120_10', 6)	# 188-193
    sprite('Action_120_11', 8)	# 194-201
    sprite('Action_117_33', 4)	# 202-205
    Unknown1084(1)
    sprite('Action_117_34', 11)	# 206-216
    sprite('Action_117_34', 5)	# 217-221
    tag_voice(0, 'uor256_0', 'uor256_1', 'uor256_2', '')
    sprite('Action_117_35', 1)	# 222-222
    GFX_0('Ultimate_kirakira_matome', 100)
    SFX_3('SE045')
    physicsYImpulse(100000)
    setGravity(1900)
    Unknown21007(4, 33)
    Unknown3029(1)
    Unknown3069(1)
    Unknown3071(4)
    Unknown3070(1)
    SLOT_2 = 0
    SLOT_2 = 5

    def upon_78():
        clearUponHandler(78)
        Unknown21012('556c74696d6174655f6b6972616b6972615f6d61746f6d65000000000000000020000000')
    label(11)
    sprite('Action_117_36ex01', 2)	# 223-224	 **attackbox here**
    Unknown2038(-1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(650)
    Hitstop(3)
    AirPushbackX(1500)
    AirPushbackY(35000)
    YImpluseBeforeWallbounce(1800)
    Unknown11091(20)
    Unknown11072(1, 120000, 0)
    Unknown2017(0)
    Unknown11069('')
    if (SLOT_2 > 0):
        sendToLabel(11)
    sprite('Action_117_36ex01', 15)	# 225-239	 **attackbox here**
    GFX_0('UltimateAssault_Blade1', 100)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(2800)
    Hitstop(30)
    AirPushbackX(1500)
    AirPushbackY(35000)
    YImpluseBeforeWallbounce(1800)
    Unknown11072(1, 200000, 0)
    Unknown9310(1)
    Unknown11064(0)
    Unknown30048(1)
    Unknown21007(4, 34)
    clearUponHandler(78)

    def upon_78():
        Unknown13024(1)
        SFX_3('SE_BigBomb')
        SFX_0('025_cleanhit_slash')
    sprite('Action_117_36ex01', 1)	# 240-240	 **attackbox here**
    sprite('Action_117_37', 3)	# 241-243
    physicsYImpulse(350000)
    setGravity(40000)
    sprite('Action_117_37', 3)	# 244-246
    YAccel(0)
    setGravity(0)
    teleportRelativeY(1600000)
    Unknown21007(4, 35)
    sprite('Action_117_38', 2)	# 247-248
    physicsYImpulse(48000)
    setGravity(2500)
    sprite('Action_117_39', 4)	# 249-252
    physicsYImpulse(8000)
    sprite('Action_117_40', 4)	# 253-256
    sprite('Action_117_41', 4)	# 257-260
    sendToLabelUpon(2, 20)
    sprite('Action_117_42', 3)	# 261-263
    sprite('Action_117_43', 3)	# 264-266
    sprite('Action_117_44', 3)	# 267-269
    label(12)
    sprite('Action_117_45', 3)	# 270-272
    sprite('Action_117_46', 3)	# 273-275
    gotoLabel(12)
    label(20)
    sprite('Action_117_47', 3)	# 276-278
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    Unknown13024(1)
    Unknown3029(0)
    Unknown1084(1)
    sprite('Action_117_48', 19)	# 279-297
    sprite('Action_117_49', 3)	# 298-300
    sprite('Action_117_50', 2)	# 301-302

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown2003(0)

        def upon_32():
            Unknown21007(11, 32)

        def upon_33():
            Unknown21007(11, 33)

        def upon_37():
            clearUponHandler(17)
            clearUponHandler(1)
            setInvincible(1)
            Unknown2038(1)
            Unknown23157(1)
            Unknown23088(1, 1)
            Unknown23084(1)

        def upon_40():
            Unknown23024(0)

        def upon_41():
            Unknown23088(1, 1)
            sendToLabel(50)
        loopRelated(17, 180)

        def upon_17():
            if (not SLOT_2):
                sendToLabel(1)

        def upon_STATE_END():
            Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_171_00', 4)	# 1-4
    Unknown22008(160)
    Unknown23029(11, 0, 0)
    sprite('Action_171_01', 4)	# 5-8
    Unknown2036(85, -1, 1)
    Unknown23147()
    GFX_0('Ori_CutIn', 100)
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    sprite('Action_171_02', 4)	# 9-12
    sprite('Action_171_03', 4)	# 13-16
    SFX_1('uor290')
    sprite('Action_171_04', 4)	# 17-20
    sprite('Action_171_05', 4)	# 21-24
    sprite('Action_171_03', 4)	# 25-28
    sprite('Action_171_04', 4)	# 29-32
    sprite('Action_171_05', 4)	# 33-36
    sprite('Action_171_03', 4)	# 37-40
    sprite('Action_171_04', 4)	# 41-44
    sprite('Action_171_05', 4)	# 45-48
    sprite('Action_171_03', 4)	# 49-52
    sprite('Action_171_04', 4)	# 53-56
    sprite('Action_171_05', 4)	# 57-60
    sprite('Action_171_03', 4)	# 61-64
    sprite('Action_171_04', 4)	# 65-68
    GFX_0('Astral_Tan', 100)
    Unknown38(11, 1)
    sprite('Action_171_05', 4)	# 69-72
    label(0)
    sprite('Action_171_03', 4)	# 73-76
    sprite('Action_171_04', 4)	# 77-80
    sprite('Action_171_05', 4)	# 81-84
    gotoLabel(0)
    label(1)
    sprite('Action_171_05', 4)	# 85-88
    clearUponHandler(1)
    Unknown23029(11, 0, 0)
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_171_00', 3)	# 89-91
    ExitState()
    label(50)
    sprite('Action_051_08', 5)	# 92-96
    Unknown13(11)
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_051_09', 6)	# 97-102
    sprite('Action_051_10', 6)	# 103-108
    sprite('Action_051_11', 6)	# 109-114
    sprite('Action_051_12', 6)	# 115-120
    sprite('Action_051_09', 6)	# 121-126
    sprite('Action_051_10', 6)	# 127-132
    sprite('Action_051_11', 6)	# 133-138
    sprite('Action_051_12', 6)	# 139-144
    sprite('Action_051_13', 3)	# 145-147
    sprite('Action_051_14', 2)	# 148-149
    sprite('Action_051_15', 3)	# 150-152
    sprite('Action_051_16', 4)	# 153-156
    sprite('Action_051_17', 2)	# 157-158

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
    sprite('keep', 68)	# 1-68

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    sprite('keep', 68)	# 1-68
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('Action_046_00', 2)	# 1-2
    sprite('Action_046_01', 2)	# 3-4
    sprite('Action_046_02', 1)	# 5-5
    label(0)
    sprite('Action_046_01', 2)	# 6-7
    sprite('Action_046_02', 1)	# 8-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_00', 6)	# 9-14

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 68)	# 1-68

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_051_13', 3)	# 1-3
    sprite('Action_051_08', 5)	# 4-8
    sprite('Action_051_09', 5)	# 9-13
    sprite('Action_051_10', 5)	# 14-18
    sprite('Action_051_11', 5)	# 19-23
    sprite('Action_051_12', 5)	# 24-28
    sprite('Action_051_08', 5)	# 29-33
    sprite('Action_051_09', 5)	# 34-38
    sprite('Action_051_10', 5)	# 39-43
    sprite('Action_051_11', 5)	# 44-48
    sprite('Action_051_12', 5)	# 49-53
    sprite('Action_051_13', 3)	# 54-56
    sprite('Action_051_14', 2)	# 57-58
    sprite('Action_051_15', 3)	# 59-61
    sprite('Action_051_16', 4)	# 62-65
    sprite('Action_051_17', 22)	# 66-87
    loopRest()

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 10)	# 1-10
    label(0)
    sprite('null', 1)	# 11-11
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-500000)
    Unknown1007(2400000)
    physicsXImpulse(18518)
    physicsYImpulse(-88888)
    setGravity(0)
    sprite('Action_245_00', 6)	# 12-17
    sprite('Action_245_01', 6)	# 18-23
    sprite('Action_245_02', 6)	# 24-29
    sprite('Action_245_03', 5)	# 30-34
    Unknown2053(1)
    sprite('Action_245_04', 4)	# 35-38	 **attackbox here**
    sprite('Action_245_05', 3)	# 39-41	 **attackbox here**
    sendToLabelUpon(2, 9)
    sprite('Action_245_06', 3)	# 42-44
    sprite('Action_245_07', 8)	# 45-52
    sprite('Action_245_08', 5)	# 53-57
    sprite('Action_245_09', 5)	# 58-62
    label(1)
    sprite('Action_022_00', 3)	# 63-65
    sprite('Action_022_01', 3)	# 66-68
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_246_00', 4)	# 69-72
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_246_01', 10)	# 73-82
    sprite('Action_246_02', 4)	# 83-86
    sprite('Action_246_03', 4)	# 87-90

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_313_02', 3)	# 1-3
    sprite('Action_312_03', 6)	# 4-9
    sprite('Action_312_04', 60)	# 10-69

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_02', 3)	# 1-3
    sprite('Action_045_03', 5)	# 4-8
    sprite('Action_045_17', 9)	# 9-17
    sprite('Action_045_00', 5)	# 18-22
    sprite('Action_046_00', 7)	# 23-29

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
        AttackLevel_(5)
        Damage(2200)
        AttackP1(70)
        Unknown9016(1)
        AirUntechableTime(60)
        PushbackX(19800)
        Hitstop(9)
        AirPushbackX(18000)
        AirPushbackY(28000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown11042(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_100_00', 5)	# 1-5
    Unknown1084(1)
    sprite('Action_100_01', 3)	# 6-8
    sprite('Action_100_01', 4)	# 9-12
    sprite('Action_100_02', 6)	# 13-18
    Unknown7006('uor200_0', 100, 846360437, 845099056, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_100_03', 2)	# 19-20	 **attackbox here**
    StartMultihit()
    GFX_0('Assault_Zanzo', 100)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    physicsXImpulse(125000)
    Unknown1028(-8000)
    SFX_3('SE038')

    def upon_77():
        Unknown1019(5)
        Unknown1034(5)
        Unknown2038(1)
    GFX_0('Assault_Blade', 100)
    SFX_3('SE045')
    ScreenShake(0, 9000)
    SFX_0('000_airdash_1')
    sprite('Action_100_05', 3)	# 21-23	 **attackbox here**
    sprite('Action_100_06ex01', 3)	# 24-26	 **attackbox here**
    sprite('Action_100_07', 3)	# 27-29
    Unknown23027()
    Recovery()
    Unknown1084(1)
    sprite('Action_100_08', 4)	# 30-33
    sprite('Action_100_09', 4)	# 34-37
    sprite('Action_100_10', 5)	# 38-42
    sprite('Action_100_11', 4)	# 43-46
    ExitState()

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
        Unknown11063(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_141_00', 6)	# 1-6
    sprite('Action_141_01', 6)	# 7-12
    Unknown23029(11, 0, 0)
    GFX_0('Tan_SealingTAG', 100)
    Unknown38(11, 1)
    Unknown7006('uor210_0', 100, 846360437, 828321841, 0, 0, 100, 846360437, 845099057, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_141_02', 6)	# 13-18
    sprite('Action_141_03', 6)	# 19-24
    sprite('Action_141_04', 11)	# 25-35
    sprite('Action_141_05', 13)	# 36-48
    sprite('Action_141_06', 6)	# 49-54
    Recovery()
    sprite('Action_141_07', 6)	# 55-60

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(700)
        AttackP1(70)
        AttackP2(85)
        Unknown11092(1)
        AirUntechableTime(19)
        Hitstop(3)
        AirPushbackX(18000)
        AirPushbackY(7500)
        PushbackX(13000)
        Unknown9016(1)
        Unknown1084(1)
        Unknown11056(2)
        Unknown11042(1)
        Unknown2006()

        def upon_12():
            Unknown2038(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
    sprite('Action_117_00', 8)	# 1-8
    sprite('Action_117_01', 3)	# 9-11
    Unknown7006('uor212_0', 100, 846360437, 828322353, 0, 0, 100, 846360437, 845099569, 0, 0, 100, 0, 0, 0, 0, 0)
    physicsXImpulse(42000)
    Unknown1028(-5000)
    sprite('Action_117_02', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(55000)
    Unknown1028(-2500)
    GFX_0('Eff66CBlade1', 100)
    SFX_3('SE041')
    sprite('Action_117_03', 2)	# 15-16	 **attackbox here**
    sprite('Action_117_04', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    GFX_0('Eff66CBlade2', 100)
    SFX_3('SE041')
    sprite('Action_117_05', 2)	# 19-20	 **attackbox here**
    sprite('Action_117_06', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('Action_117_07', 2)	# 23-24	 **attackbox here**
    loopRest()
    if SLOT_2:
        _gotolabel(10)
    sprite('Action_403_14', 4)	# 25-28	 **attackbox here**
    Unknown23027()
    Recovery()
    Unknown2063()
    sprite('Action_403_15', 4)	# 29-32	 **attackbox here**
    Unknown14074('AN_NmlAtk5A_4th')
    sprite('Action_403_16', 9)	# 33-41
    Unknown8010(0, 1, 1)
    Unknown1084(1)
    Unknown1045(9000)
    sprite('Action_403_16', 6)	# 42-47
    ExitState()
    label(10)
    sprite('Action_117_14', 2)	# 48-49
    Unknown1084(1)
    sprite('Action_117_15', 2)	# 50-51
    sprite('Action_117_16', 1)	# 52-52
    physicsXImpulse(60000)
    Unknown1028(-10000)
    physicsYImpulse(90000)
    setGravity(15000)
    sprite('Action_117_17', 4)	# 53-56	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE045')
    GFX_0('InvincibleAttackBlade', 100)
    AttackLevel_(4)
    Damage(1700)
    AirPushbackX(6500)
    AirPushbackY(38500)
    PushbackX(30400)
    AirUntechableTime(150)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    sprite('Action_117_18', 2)	# 57-58
    physicsXImpulse(10000)
    Unknown1028(-500)
    physicsYImpulse(10240)
    setGravity(2500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(12)
    sprite('Action_117_19', 4)	# 59-62
    sprite('Action_117_20', 3)	# 63-65
    sprite('Action_117_21', 3)	# 66-68
    sprite('Action_117_22', 3)	# 69-71
    sprite('Action_117_23', 3)	# 72-74
    sprite('Action_117_24', 3)	# 75-77
    label(11)
    sprite('Action_117_25', 3)	# 78-80
    sprite('Action_117_26', 3)	# 81-83
    gotoLabel(11)
    label(12)
    sprite('Action_117_28', 4)	# 84-87
    Recovery()
    Unknown1084(1)
    sprite('Action_117_29', 6)	# 88-93
    sprite('Action_117_30', 5)	# 94-98
    sprite('Action_117_31', 5)	# 99-103
    ExitState()

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
    sprite('Action_022_00', 4)	# 3-6
    sprite('Action_022_01', 4)	# 7-10
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
        Unknown23055('')
        Unknown9266(13)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        Unknown11091(100)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        Unknown30063(1)
        Unknown2021(1)
    sprite('Action_120_00', 1)	# 1-1
    Unknown23029(11, 0, 0)
    setInvincible(1)
    sprite('Action_120_00', 17)	# 2-18
    sprite('Action_120_01', 3)	# 19-21	 **attackbox here**
    sprite('Action_120_02', 3)	# 22-24	 **attackbox here**
    sprite('Action_120_03', 2)	# 25-26	 **attackbox here**
    sprite('Action_120_03', 1)	# 27-27	 **attackbox here**
    GFX_0('IW_Tan_DUO', 100)
    Unknown38(11, 1)
    sprite('Action_120_04', 3)	# 28-30	 **attackbox here**
    sprite('Action_120_05', 23)	# 31-53
    sprite('Action_120_06', 4)	# 54-57
    sprite('Action_120_07', 10)	# 58-67
    sprite('Action_120_08', 4)	# 68-71
    sprite('Action_120_09', 4)	# 72-75
    tag_voice(0, 'uor251_0', 'uor251_1', '', '')
    SFX_3('SE010')
    Unknown4004('6566666563745f3331390000000000000000000000000000000000000000000064000000')
    sprite('Action_120_10', 10)	# 76-85
    Unknown2021(0)
    setInvincible(0)
    sprite('Action_120_11', 45)	# 86-130
    sprite('Action_120_12', 6)	# 131-136
    sprite('Action_120_13', 4)	# 137-140
    sprite('Action_120_14', 4)	# 141-144
    sprite('Action_120_15', 8)	# 145-152
    sprite('Action_120_16', 6)	# 153-158
    sprite('Action_120_17', 4)	# 159-162

@State
def UltimateShotDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(625)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11092(1)
        PushbackX(0)
        Hitstop(3)
        GroundedHitstunAnimation(1)
        AirHitstunAnimation(1)
        Unknown9016(1)
        Unknown30063(1)
        Unknown2021(1)

        def upon_43():
            if (SLOT_48 == 5001):
                Unknown2038(1)
                setInvincible(1)
    sprite('Action_120_00', 1)	# 1-1
    Unknown23029(11, 0, 0)
    setInvincible(1)
    sprite('Action_120_00', 17)	# 2-18
    sprite('Action_120_01', 3)	# 19-21	 **attackbox here**
    sprite('Action_120_02', 3)	# 22-24	 **attackbox here**
    sprite('Action_120_03', 2)	# 25-26	 **attackbox here**
    sprite('Action_120_03', 1)	# 27-27	 **attackbox here**
    GFX_0('IW_Tan_ODDUO', 100)
    Unknown38(11, 1)
    sprite('Action_120_04', 3)	# 28-30	 **attackbox here**
    sprite('Action_120_05', 23)	# 31-53
    sprite('Action_120_06', 4)	# 54-57
    sprite('Action_120_07', 10)	# 58-67
    sprite('Action_120_08', 4)	# 68-71
    sprite('Action_120_09', 4)	# 72-75
    SFX_3('SE010')
    Unknown4004('6566666563745f3331390000000000000000000000000000000000000000000064000000')
    tag_voice(0, 'uor251_0', 'uor251_1', '', '')
    sprite('Action_120_10', 10)	# 76-85
    Unknown2021(0)
    if (not SLOT_2):
        setInvincible(0)
    sprite('Action_120_11', 45)	# 86-130
    sprite('Action_120_12', 6)	# 131-136
    sprite('Action_120_13', 4)	# 137-140
    sprite('Action_120_14', 4)	# 141-144
    sprite('Action_120_15', 8)	# 145-152
    if SLOT_2:
        _gotolabel(100)
    sprite('Action_120_16', 6)	# 153-158
    sprite('Action_120_17', 4)	# 159-162
    ExitState()
    label(100)
    sprite('Action_100_00', 5)	# 163-167
    sprite('Action_100_00', 45)	# 168-212
    Unknown2036(35, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown1084(1)
    Damage(500)
    Unknown9266(0)
    Hitstop(0)
    AirUntechableTime(180)
    Unknown9310(1)
    Unknown11001(0, 25, 25)
    Unknown2017(0)
    Unknown2015(200)
    tag_voice(0, 'uor252_0', 'uor252_1', '', '')
    sprite('Action_100_01', 3)	# 213-215
    sprite('Action_100_02', 6)	# 216-221
    tag_voice(0, 'uor253_0', 'uor253_1', '', '')
    sprite('Action_100_03', 3)	# 222-224	 **attackbox here**
    GFX_0('Assault_Zanzo', 100)
    Unknown4004('6566666563745f3339300000000000000000000000000000000000000000000064000000')
    physicsXImpulse(190000)
    Unknown1028(-7500)
    GFX_0('Ultimate_kirakira_matomeX', 100)
    SFX_3('SE038')

    def upon_78():
        clearUponHandler(78)
        SFX_3('SE_BigBomb')
        SFX_0('025_cleanhit_slash')
        SLOT_51 = 1

    def upon_82():
        clearUponHandler(82)
        SFX_0('025_cleanhit_slash')
    sprite('Action_100_03', 9)	# 225-233	 **attackbox here**
    GFX_0('UltimateShot_ODBlade', 100)
    GFX_0('Assault_Blade', 100)
    SFX_3('SE045')
    sprite('Action_100_04', 3)	# 234-236	 **attackbox here**
    sprite('Action_100_05', 4)	# 237-240	 **attackbox here**
    sprite('Action_100_06', 4)	# 241-244
    sprite('Action_100_07', 5)	# 245-249
    Unknown1084(1)
    Unknown2017(1)
    Unknown1045(10000)
    if (not SLOT_51):
        sendToLabel(102)
    label(101)
    sprite('Action_101_04', 5)	# 250-254
    sprite('Action_101_05', 5)	# 255-259
    sprite('Action_101_06', 5)	# 260-264
    sprite('Action_101_07', 5)	# 265-269
    sprite('Action_101_04', 5)	# 270-274
    sprite('Action_101_05', 5)	# 275-279
    sprite('Action_101_06', 5)	# 280-284
    sprite('Action_101_07', 5)	# 285-289
    label(102)
    sprite('Action_100_08', 5)	# 290-294
    sprite('Action_100_09', 7)	# 295-301
    sprite('Action_100_10', 6)	# 302-307
    sprite('Action_100_11', 6)	# 308-313

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
    sprite('null', 1)	# 123-123
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-500000)
    Unknown1007(2400000)
    physicsXImpulse(17857)
    physicsYImpulse(-85714)
    setGravity(0)
    sprite('Action_245_00', 6)	# 124-129
    sprite('Action_245_01', 6)	# 130-135
    sprite('Action_245_02', 6)	# 136-141
    sprite('Action_245_03', 5)	# 142-146
    Unknown2053(1)
    sprite('Action_245_04', 32767)	# 147-32913	 **attackbox here**

    def upon_77():
        clearUponHandler(77)
        sendToLabel(1)
    sendToLabelUpon(2, 9)
    label(1)
    sprite('Action_245_05', 4)	# 32914-32917	 **attackbox here**
    sprite('Action_245_06', 3)	# 32918-32920
    sprite('Action_245_07', 8)	# 32921-32928
    sprite('Action_245_08', 5)	# 32929-32933
    sprite('Action_245_09', 5)	# 32934-32938
    label(5)
    sprite('Action_022_00', 3)	# 32939-32941
    sprite('Action_022_01', 3)	# 32942-32944
    loopRest()
    gotoLabel(5)
    label(9)
    sprite('Action_246_00', 5)	# 32945-32949
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_246_01', 15)	# 32950-32964
    sprite('Action_246_02', 5)	# 32965-32969
    sprite('Action_246_03', 5)	# 32970-32974

@Subroutine
def MouthTableInit():
    Unknown18011('uor500', 12899, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor501', 12899, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor502', 12899, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor503', 12899, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor504', 12643, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor505', 12899, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor520', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor522', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor402_1', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor403_0', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600biz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor601bjb', 12643, 13665, 13667, 13665, 13667, 14177, 14179, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor601bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600brg', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600pmi', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600pna', 12899, 12340, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor601rbl', 12643, 14177, 14179, 14177, 13667, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13364, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600rwi', 12643, 12344, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600uhy', 12643, 14177, 14179, 14177, 14179, 13665, 13667, 13665, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor600uli', 12643, 12345, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor601umi', 12643, 14177, 14179, 14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor701biz', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700bjb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700bjn', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700brg', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700pmi', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor701rbl', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor701rwi', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700uhy', 12643, 12641, 25397, 12855, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14691, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor700uli', 12643, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor701umi', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uor703rwi', 12643, 12641, 25392, 24887, 25399, 24887, 12337, 13923, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bjn')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bjb')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('uhy')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('biz')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(200)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(1)
    sprite('null', 2)	# 2-3
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(1)
    sprite('Action_050_02', 5)	# 4-8
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 3)
    label(2)
    sprite('Action_050_02', 3)	# 9-11
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('Action_050_02', 2)	# 12-13
    Unknown1000(-1230000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 14-15
    sprite('Action_050_04', 7)	# 16-22
    sprite('Action_050_05', 5)	# 23-27
    sprite('Action_050_06', 8)	# 28-35
    sprite('Action_050_07', 4)	# 36-39
    sprite('Action_050_08', 4)	# 40-43
    sprite('Action_050_09', 4)	# 44-47
    Unknown7006('uor500', 100, 896692085, 12592, 0, 0, 100, 896692085, 13360, 0, 0, 100, 896692085, 13616, 0, 0, 100)
    sprite('Action_050_10', 4)	# 48-51
    sprite('Action_050_11', 4)	# 52-55
    sprite('Action_050_12', 4)	# 56-59
    label(4)
    sprite('Action_050_13', 4)	# 60-63
    sprite('Action_050_14', 4)	# 64-67
    sprite('Action_050_15', 4)	# 68-71
    sprite('Action_050_16', 4)	# 72-75
    sprite('Action_050_17', 4)	# 76-79
    if SLOT_97:
        _gotolabel(4)
    sprite('Action_050_18', 4)	# 80-83
    sprite('Action_050_19', 4)	# 84-87
    sprite('Action_050_20', 6)	# 88-93
    sprite('Action_050_21', 7)	# 94-100
    sprite('Action_050_22', 2)	# 101-102
    Unknown23018(1)
    label(5)
    sprite('Action_000_00', 3)	# 103-105	 **attackbox here**
    sprite('Action_000_01', 6)	# 106-111	 **attackbox here**
    sprite('Action_000_02', 6)	# 112-117	 **attackbox here**
    sprite('Action_000_03', 6)	# 118-123	 **attackbox here**
    sprite('Action_000_04', 6)	# 124-129	 **attackbox here**
    sprite('Action_000_05', 6)	# 130-135	 **attackbox here**
    sprite('Action_000_06', 6)	# 136-141	 **attackbox here**
    sprite('Action_000_07', 6)	# 142-147	 **attackbox here**
    sprite('Action_000_08', 6)	# 148-153	 **attackbox here**
    sprite('Action_000_09', 6)	# 154-159	 **attackbox here**
    sprite('Action_000_10', 6)	# 160-165	 **attackbox here**
    sprite('Action_000_11', 6)	# 166-171	 **attackbox here**
    sprite('Action_000_12', 6)	# 172-177	 **attackbox here**
    sprite('Action_000_13', 6)	# 178-183	 **attackbox here**
    sprite('Action_000_14', 6)	# 184-189	 **attackbox here**
    sprite('Action_000_15', 6)	# 190-195	 **attackbox here**
    sprite('Action_000_16', 6)	# 196-201	 **attackbox here**
    sprite('Action_000_17', 6)	# 202-207	 **attackbox here**
    sprite('Action_000_18', 6)	# 208-213
    sprite('Action_000_19', 6)	# 214-219
    sprite('Action_000_20', 6)	# 220-225
    sprite('Action_000_21', 6)	# 226-231
    sprite('Action_000_22', 6)	# 232-237
    sprite('Action_000_23', 6)	# 238-243
    sprite('Action_000_24', 3)	# 244-246
    loopRest()
    gotoLabel(5)
    ExitState()
    label(10)
    sprite('null', 2)	# 247-248
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(10)
    sprite('Action_050_02', 5)	# 249-253
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 12)
    label(11)
    sprite('Action_050_02', 3)	# 254-256
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('Action_050_02', 2)	# 257-258
    Unknown1000(-1230000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 259-260
    sprite('Action_050_04', 7)	# 261-267
    sprite('Action_050_05', 5)	# 268-272
    sprite('Action_050_06', 8)	# 273-280
    sprite('Action_050_07', 4)	# 281-284
    sprite('Action_050_23', 5)	# 285-289
    sprite('Action_050_24', 3)	# 290-292
    Unknown7006('uor502', 100, 896692085, 13104, 0, 0, 100, 896692085, 13360, 0, 0, 100, 896692085, 13616, 0, 0, 100)
    sprite('Action_050_25', 5)	# 293-297
    label(13)
    sprite('Action_050_26', 5)	# 298-302
    sprite('Action_050_27', 5)	# 303-307
    sprite('Action_050_28', 5)	# 308-312
    sprite('Action_050_29', 5)	# 313-317
    sprite('Action_050_30', 5)	# 318-322
    if SLOT_97:
        _gotolabel(13)
    sprite('Action_050_31', 5)	# 323-327
    sprite('Action_050_32', 4)	# 328-331
    sprite('Action_050_33', 6)	# 332-337
    sprite('Action_050_34', 7)	# 338-344
    sprite('Action_050_35', 2)	# 345-346
    Unknown23018(1)
    label(14)
    sprite('Action_000_00', 3)	# 347-349	 **attackbox here**
    sprite('Action_000_01', 6)	# 350-355	 **attackbox here**
    sprite('Action_000_02', 6)	# 356-361	 **attackbox here**
    sprite('Action_000_03', 6)	# 362-367	 **attackbox here**
    sprite('Action_000_04', 6)	# 368-373	 **attackbox here**
    sprite('Action_000_05', 6)	# 374-379	 **attackbox here**
    sprite('Action_000_06', 6)	# 380-385	 **attackbox here**
    sprite('Action_000_07', 6)	# 386-391	 **attackbox here**
    sprite('Action_000_08', 6)	# 392-397	 **attackbox here**
    sprite('Action_000_09', 6)	# 398-403	 **attackbox here**
    sprite('Action_000_10', 6)	# 404-409	 **attackbox here**
    sprite('Action_000_11', 6)	# 410-415	 **attackbox here**
    sprite('Action_000_12', 6)	# 416-421	 **attackbox here**
    sprite('Action_000_13', 6)	# 422-427	 **attackbox here**
    sprite('Action_000_14', 6)	# 428-433	 **attackbox here**
    sprite('Action_000_15', 6)	# 434-439	 **attackbox here**
    sprite('Action_000_16', 6)	# 440-445	 **attackbox here**
    sprite('Action_000_17', 6)	# 446-451	 **attackbox here**
    sprite('Action_000_18', 6)	# 452-457
    sprite('Action_000_19', 6)	# 458-463
    sprite('Action_000_20', 6)	# 464-469
    sprite('Action_000_21', 6)	# 470-475
    sprite('Action_000_22', 6)	# 476-481
    sprite('Action_000_23', 6)	# 482-487
    sprite('Action_000_24', 3)	# 488-490
    loopRest()
    gotoLabel(14)
    ExitState()
    label(20)
    sprite('Ori648_00', 6)	# 491-496
    sprite('Ori648_01', 6)	# 497-502
    sprite('Ori648_02', 6)	# 503-508
    sprite('Ori648_03', 6)	# 509-514	 **attackbox here**
    sprite('Ori648_04', 6)	# 515-520	 **attackbox here**
    sprite('Ori648_05', 6)	# 521-526	 **attackbox here**
    SFX_1('uor701umi')
    sprite('Ori648_06', 32767)	# 527-33293	 **attackbox here**
    ExitState()
    label(100)
    sprite('null', 2)	# 33294-33295
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(100)
    sprite('Action_050_02', 5)	# 33296-33300
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 102)
    label(101)
    sprite('Action_050_02', 3)	# 33301-33303
    loopRest()
    gotoLabel(101)
    label(102)
    sprite('Action_050_02', 2)	# 33304-33305
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 33306-33307
    sprite('Action_050_04', 7)	# 33308-33314
    sprite('Action_050_05', 5)	# 33315-33319
    sprite('Action_050_06', 8)	# 33320-33327
    sprite('Action_050_07', 4)	# 33328-33331
    sprite('Action_050_08', 4)	# 33332-33335
    sprite('Action_050_09', 4)	# 33336-33339
    SFX_1('uor600brg')
    sprite('Action_050_10', 4)	# 33340-33343
    sprite('Action_050_11', 4)	# 33344-33347
    sprite('Action_050_12', 4)	# 33348-33351
    label(103)
    sprite('Action_050_13', 4)	# 33352-33355
    sprite('Action_050_14', 4)	# 33356-33359
    sprite('Action_050_15', 4)	# 33360-33363
    sprite('Action_050_16', 4)	# 33364-33367
    sprite('Action_050_17', 4)	# 33368-33371
    if SLOT_97:
        _gotolabel(103)
    sprite('Action_050_18', 4)	# 33372-33375
    sprite('Action_050_19', 4)	# 33376-33379
    sprite('Action_050_20', 6)	# 33380-33385
    sprite('Action_050_21', 7)	# 33386-33392
    sprite('Action_050_22', 2)	# 33393-33394
    Unknown21007(24, 40)
    Unknown21011(240)
    label(104)
    sprite('Action_000_00', 3)	# 33395-33397	 **attackbox here**
    sprite('Action_000_01', 6)	# 33398-33403	 **attackbox here**
    sprite('Action_000_02', 6)	# 33404-33409	 **attackbox here**
    sprite('Action_000_03', 6)	# 33410-33415	 **attackbox here**
    sprite('Action_000_04', 6)	# 33416-33421	 **attackbox here**
    sprite('Action_000_05', 6)	# 33422-33427	 **attackbox here**
    sprite('Action_000_06', 6)	# 33428-33433	 **attackbox here**
    sprite('Action_000_07', 6)	# 33434-33439	 **attackbox here**
    sprite('Action_000_08', 6)	# 33440-33445	 **attackbox here**
    sprite('Action_000_09', 6)	# 33446-33451	 **attackbox here**
    sprite('Action_000_10', 6)	# 33452-33457	 **attackbox here**
    sprite('Action_000_11', 6)	# 33458-33463	 **attackbox here**
    sprite('Action_000_12', 6)	# 33464-33469	 **attackbox here**
    sprite('Action_000_13', 6)	# 33470-33475	 **attackbox here**
    sprite('Action_000_14', 6)	# 33476-33481	 **attackbox here**
    sprite('Action_000_15', 6)	# 33482-33487	 **attackbox here**
    sprite('Action_000_16', 6)	# 33488-33493	 **attackbox here**
    sprite('Action_000_17', 6)	# 33494-33499	 **attackbox here**
    sprite('Action_000_18', 6)	# 33500-33505
    sprite('Action_000_19', 6)	# 33506-33511
    sprite('Action_000_20', 6)	# 33512-33517
    sprite('Action_000_21', 6)	# 33518-33523
    sprite('Action_000_22', 6)	# 33524-33529
    sprite('Action_000_23', 6)	# 33530-33535
    sprite('Action_000_24', 3)	# 33536-33538
    loopRest()
    gotoLabel(104)
    ExitState()
    label(110)
    sprite('Action_000_00', 1)	# 33539-33539	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 3)	# 33540-33542	 **attackbox here**
    sprite('Action_000_01', 6)	# 33543-33548	 **attackbox here**
    sprite('Action_000_02', 6)	# 33549-33554	 **attackbox here**
    sprite('Action_000_03', 6)	# 33555-33560	 **attackbox here**
    sprite('Action_000_04', 6)	# 33561-33566	 **attackbox here**
    sprite('Action_000_05', 6)	# 33567-33572	 **attackbox here**
    sprite('Action_000_06', 6)	# 33573-33578	 **attackbox here**
    sprite('Action_000_07', 6)	# 33579-33584	 **attackbox here**
    sprite('Action_000_08', 6)	# 33585-33590	 **attackbox here**
    sprite('Action_000_09', 6)	# 33591-33596	 **attackbox here**
    sprite('Action_000_10', 6)	# 33597-33602	 **attackbox here**
    sprite('Action_000_11', 6)	# 33603-33608	 **attackbox here**
    sprite('Action_000_12', 6)	# 33609-33614	 **attackbox here**
    sprite('Action_000_13', 6)	# 33615-33620	 **attackbox here**
    sprite('Action_000_14', 6)	# 33621-33626	 **attackbox here**
    sprite('Action_000_15', 6)	# 33627-33632	 **attackbox here**
    sprite('Action_000_16', 6)	# 33633-33638	 **attackbox here**
    sprite('Action_000_17', 6)	# 33639-33644	 **attackbox here**
    sprite('Action_000_18', 6)	# 33645-33650
    sprite('Action_000_19', 6)	# 33651-33656
    sprite('Action_000_20', 6)	# 33657-33662
    sprite('Action_000_21', 6)	# 33663-33668
    sprite('Action_000_22', 6)	# 33669-33674
    sprite('Action_000_23', 6)	# 33675-33680
    sprite('Action_000_24', 3)	# 33681-33683
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('Action_000_26', 5)	# 33684-33688
    sprite('Action_000_27', 5)	# 33689-33693
    sprite('Action_000_28', 7)	# 33694-33700
    sprite('Action_000_29', 4)	# 33701-33704
    sprite('Action_000_30', 4)	# 33705-33708
    sprite('Action_000_31', 9)	# 33709-33717
    SFX_1('uor601bjn')
    sprite('Action_000_32', 5)	# 33718-33722
    sprite('Action_000_33', 5)	# 33723-33727
    Unknown23018(1)
    label(113)
    sprite('Action_000_00', 3)	# 33728-33730	 **attackbox here**
    sprite('Action_000_01', 6)	# 33731-33736	 **attackbox here**
    sprite('Action_000_02', 6)	# 33737-33742	 **attackbox here**
    sprite('Action_000_03', 6)	# 33743-33748	 **attackbox here**
    sprite('Action_000_04', 6)	# 33749-33754	 **attackbox here**
    sprite('Action_000_05', 6)	# 33755-33760	 **attackbox here**
    sprite('Action_000_06', 6)	# 33761-33766	 **attackbox here**
    sprite('Action_000_07', 6)	# 33767-33772	 **attackbox here**
    sprite('Action_000_08', 6)	# 33773-33778	 **attackbox here**
    sprite('Action_000_09', 6)	# 33779-33784	 **attackbox here**
    sprite('Action_000_10', 6)	# 33785-33790	 **attackbox here**
    sprite('Action_000_11', 6)	# 33791-33796	 **attackbox here**
    sprite('Action_000_12', 6)	# 33797-33802	 **attackbox here**
    sprite('Action_000_13', 6)	# 33803-33808	 **attackbox here**
    sprite('Action_000_14', 6)	# 33809-33814	 **attackbox here**
    sprite('Action_000_15', 6)	# 33815-33820	 **attackbox here**
    sprite('Action_000_16', 6)	# 33821-33826	 **attackbox here**
    sprite('Action_000_17', 6)	# 33827-33832	 **attackbox here**
    sprite('Action_000_18', 6)	# 33833-33838
    sprite('Action_000_19', 6)	# 33839-33844
    sprite('Action_000_20', 6)	# 33845-33850
    sprite('Action_000_21', 6)	# 33851-33856
    sprite('Action_000_22', 6)	# 33857-33862
    sprite('Action_000_23', 6)	# 33863-33868
    sprite('Action_000_24', 3)	# 33869-33871
    loopRest()
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('Action_000_00', 1)	# 33872-33872	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
        SFX_1('uor601bjb')
    label(121)
    sprite('Action_000_00', 3)	# 33873-33875	 **attackbox here**
    sprite('Action_000_01', 6)	# 33876-33881	 **attackbox here**
    sprite('Action_000_02', 6)	# 33882-33887	 **attackbox here**
    sprite('Action_000_03', 6)	# 33888-33893	 **attackbox here**
    sprite('Action_000_04', 6)	# 33894-33899	 **attackbox here**
    sprite('Action_000_05', 6)	# 33900-33905	 **attackbox here**
    sprite('Action_000_06', 6)	# 33906-33911	 **attackbox here**
    sprite('Action_000_07', 6)	# 33912-33917	 **attackbox here**
    sprite('Action_000_08', 6)	# 33918-33923	 **attackbox here**
    sprite('Action_000_09', 6)	# 33924-33929	 **attackbox here**
    sprite('Action_000_10', 6)	# 33930-33935	 **attackbox here**
    sprite('Action_000_11', 6)	# 33936-33941	 **attackbox here**
    sprite('Action_000_12', 6)	# 33942-33947	 **attackbox here**
    sprite('Action_000_13', 6)	# 33948-33953	 **attackbox here**
    sprite('Action_000_14', 6)	# 33954-33959	 **attackbox here**
    sprite('Action_000_15', 6)	# 33960-33965	 **attackbox here**
    sprite('Action_000_16', 6)	# 33966-33971	 **attackbox here**
    sprite('Action_000_17', 6)	# 33972-33977	 **attackbox here**
    sprite('Action_000_18', 6)	# 33978-33983
    sprite('Action_000_19', 6)	# 33984-33989
    sprite('Action_000_20', 6)	# 33990-33995
    sprite('Action_000_21', 6)	# 33996-34001
    sprite('Action_000_22', 6)	# 34002-34007
    sprite('Action_000_23', 6)	# 34008-34013
    sprite('Action_000_24', 3)	# 34014-34016
    loopRest()
    gotoLabel(121)
    label(122)
    sprite('Action_000_26', 5)	# 34017-34021
    sprite('Action_000_27', 5)	# 34022-34026
    sprite('Action_000_28', 7)	# 34027-34033
    sprite('Action_000_29', 4)	# 34034-34037
    sprite('Action_000_30', 4)	# 34038-34041
    sprite('Action_000_31', 9)	# 34042-34050
    sprite('Action_000_32', 5)	# 34051-34055
    sprite('Action_000_33', 5)	# 34056-34060
    Unknown23018(1)
    label(123)
    sprite('Action_000_00', 3)	# 34061-34063	 **attackbox here**
    sprite('Action_000_01', 6)	# 34064-34069	 **attackbox here**
    sprite('Action_000_02', 6)	# 34070-34075	 **attackbox here**
    sprite('Action_000_03', 6)	# 34076-34081	 **attackbox here**
    sprite('Action_000_04', 6)	# 34082-34087	 **attackbox here**
    sprite('Action_000_05', 6)	# 34088-34093	 **attackbox here**
    sprite('Action_000_06', 6)	# 34094-34099	 **attackbox here**
    sprite('Action_000_07', 6)	# 34100-34105	 **attackbox here**
    sprite('Action_000_08', 6)	# 34106-34111	 **attackbox here**
    sprite('Action_000_09', 6)	# 34112-34117	 **attackbox here**
    sprite('Action_000_10', 6)	# 34118-34123	 **attackbox here**
    sprite('Action_000_11', 6)	# 34124-34129	 **attackbox here**
    sprite('Action_000_12', 6)	# 34130-34135	 **attackbox here**
    sprite('Action_000_13', 6)	# 34136-34141	 **attackbox here**
    sprite('Action_000_14', 6)	# 34142-34147	 **attackbox here**
    sprite('Action_000_15', 6)	# 34148-34153	 **attackbox here**
    sprite('Action_000_16', 6)	# 34154-34159	 **attackbox here**
    sprite('Action_000_17', 6)	# 34160-34165	 **attackbox here**
    sprite('Action_000_18', 6)	# 34166-34171
    sprite('Action_000_19', 6)	# 34172-34177
    sprite('Action_000_20', 6)	# 34178-34183
    sprite('Action_000_21', 6)	# 34184-34189
    sprite('Action_000_22', 6)	# 34190-34195
    sprite('Action_000_23', 6)	# 34196-34201
    sprite('Action_000_24', 3)	# 34202-34204
    loopRest()
    gotoLabel(123)
    ExitState()
    label(130)
    sprite('null', 2)	# 34205-34206
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(130)
    sprite('Action_050_02', 5)	# 34207-34211
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 132)
    label(131)
    sprite('Action_050_02', 3)	# 34212-34214
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('Action_050_02', 2)	# 34215-34216
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 34217-34218
    sprite('Action_050_04', 7)	# 34219-34225
    sprite('Action_050_05', 5)	# 34226-34230
    sprite('Action_050_06', 8)	# 34231-34238
    sprite('Action_050_07', 4)	# 34239-34242
    sprite('Action_050_08', 4)	# 34243-34246
    sprite('Action_050_09', 4)	# 34247-34250
    SFX_1('uor600pna')
    sprite('Action_050_10', 4)	# 34251-34254
    sprite('Action_050_11', 4)	# 34255-34258
    sprite('Action_050_12', 4)	# 34259-34262
    label(133)
    sprite('Action_050_13', 6)	# 34263-34268
    sprite('Action_050_14', 6)	# 34269-34274
    sprite('Action_050_15', 6)	# 34275-34280
    sprite('Action_050_16', 6)	# 34281-34286
    sprite('Action_050_17', 6)	# 34287-34292
    if SLOT_97:
        _gotolabel(133)
    sprite('Action_050_18', 4)	# 34293-34296
    sprite('Action_050_19', 4)	# 34297-34300
    sprite('Action_050_20', 6)	# 34301-34306
    sprite('Action_050_21', 7)	# 34307-34313
    sprite('Action_050_22', 2)	# 34314-34315
    Unknown21007(24, 40)
    Unknown21011(240)
    label(134)
    sprite('Action_000_00', 3)	# 34316-34318	 **attackbox here**
    sprite('Action_000_01', 6)	# 34319-34324	 **attackbox here**
    sprite('Action_000_02', 6)	# 34325-34330	 **attackbox here**
    sprite('Action_000_03', 6)	# 34331-34336	 **attackbox here**
    sprite('Action_000_04', 6)	# 34337-34342	 **attackbox here**
    sprite('Action_000_05', 6)	# 34343-34348	 **attackbox here**
    sprite('Action_000_06', 6)	# 34349-34354	 **attackbox here**
    sprite('Action_000_07', 6)	# 34355-34360	 **attackbox here**
    sprite('Action_000_08', 6)	# 34361-34366	 **attackbox here**
    sprite('Action_000_09', 6)	# 34367-34372	 **attackbox here**
    sprite('Action_000_10', 6)	# 34373-34378	 **attackbox here**
    sprite('Action_000_11', 6)	# 34379-34384	 **attackbox here**
    sprite('Action_000_12', 6)	# 34385-34390	 **attackbox here**
    sprite('Action_000_13', 6)	# 34391-34396	 **attackbox here**
    sprite('Action_000_14', 6)	# 34397-34402	 **attackbox here**
    sprite('Action_000_15', 6)	# 34403-34408	 **attackbox here**
    sprite('Action_000_16', 6)	# 34409-34414	 **attackbox here**
    sprite('Action_000_17', 6)	# 34415-34420	 **attackbox here**
    sprite('Action_000_18', 6)	# 34421-34426
    sprite('Action_000_19', 6)	# 34427-34432
    sprite('Action_000_20', 6)	# 34433-34438
    sprite('Action_000_21', 6)	# 34439-34444
    sprite('Action_000_22', 6)	# 34445-34450
    sprite('Action_000_23', 6)	# 34451-34456
    sprite('Action_000_24', 3)	# 34457-34459
    loopRest()
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('Action_000_00', 1)	# 34460-34460	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_000_00', 3)	# 34461-34463	 **attackbox here**
    sprite('Action_000_01', 6)	# 34464-34469	 **attackbox here**
    sprite('Action_000_02', 6)	# 34470-34475	 **attackbox here**
    sprite('Action_000_03', 6)	# 34476-34481	 **attackbox here**
    sprite('Action_000_04', 6)	# 34482-34487	 **attackbox here**
    sprite('Action_000_05', 6)	# 34488-34493	 **attackbox here**
    sprite('Action_000_06', 6)	# 34494-34499	 **attackbox here**
    sprite('Action_000_26', 5)	# 34500-34504
    SFX_1('uor600uhy')
    sprite('Action_000_27', 5)	# 34505-34509
    sprite('Action_000_28', 7)	# 34510-34516
    sprite('Action_000_29', 4)	# 34517-34520
    sprite('Action_000_30', 4)	# 34521-34524
    sprite('Action_000_31', 9)	# 34525-34533
    sprite('Action_000_32', 5)	# 34534-34538
    sprite('Action_000_33', 5)	# 34539-34543
    Unknown21011(200)
    label(141)
    sprite('Action_000_00', 3)	# 34544-34546	 **attackbox here**
    sprite('Action_000_01', 6)	# 34547-34552	 **attackbox here**
    sprite('Action_000_02', 6)	# 34553-34558	 **attackbox here**
    sprite('Action_000_03', 6)	# 34559-34564	 **attackbox here**
    sprite('Action_000_04', 6)	# 34565-34570	 **attackbox here**
    sprite('Action_000_05', 6)	# 34571-34576	 **attackbox here**
    sprite('Action_000_06', 6)	# 34577-34582	 **attackbox here**
    sprite('Action_000_07', 6)	# 34583-34588	 **attackbox here**
    sprite('Action_000_08', 6)	# 34589-34594	 **attackbox here**
    sprite('Action_000_09', 6)	# 34595-34600	 **attackbox here**
    sprite('Action_000_10', 6)	# 34601-34606	 **attackbox here**
    sprite('Action_000_11', 6)	# 34607-34612	 **attackbox here**
    sprite('Action_000_12', 6)	# 34613-34618	 **attackbox here**
    sprite('Action_000_13', 6)	# 34619-34624	 **attackbox here**
    sprite('Action_000_14', 6)	# 34625-34630	 **attackbox here**
    Unknown21007(24, 40)
    sprite('Action_000_15', 6)	# 34631-34636	 **attackbox here**
    sprite('Action_000_16', 6)	# 34637-34642	 **attackbox here**
    sprite('Action_000_17', 6)	# 34643-34648	 **attackbox here**
    sprite('Action_000_18', 6)	# 34649-34654
    sprite('Action_000_19', 6)	# 34655-34660
    sprite('Action_000_20', 6)	# 34661-34666
    sprite('Action_000_21', 6)	# 34667-34672
    sprite('Action_000_22', 6)	# 34673-34678
    sprite('Action_000_23', 6)	# 34679-34684
    sprite('Action_000_24', 3)	# 34685-34687
    loopRest()
    gotoLabel(141)
    ExitState()
    label(150)
    sprite('null', 2)	# 34688-34689
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(150)
    sprite('Action_050_02', 5)	# 34690-34694
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 152)
    label(151)
    sprite('Action_050_02', 3)	# 34695-34697
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('Action_050_02', 2)	# 34698-34699
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 34700-34701
    sprite('Action_050_04', 7)	# 34702-34708
    sprite('Action_050_05', 5)	# 34709-34713
    sprite('Action_050_06', 8)	# 34714-34721
    sprite('Action_050_07', 4)	# 34722-34725
    sprite('Action_050_08', 4)	# 34726-34729
    sprite('Action_050_09', 4)	# 34730-34733
    SFX_1('uor600uli')
    sprite('Action_050_10', 4)	# 34734-34737
    sprite('Action_050_11', 4)	# 34738-34741
    sprite('Action_050_12', 4)	# 34742-34745
    label(153)
    sprite('Action_050_13', 6)	# 34746-34751
    sprite('Action_050_14', 6)	# 34752-34757
    sprite('Action_050_15', 6)	# 34758-34763
    sprite('Action_050_16', 6)	# 34764-34769
    sprite('Action_050_17', 6)	# 34770-34775
    if SLOT_97:
        _gotolabel(153)
    sprite('Action_050_18', 4)	# 34776-34779
    sprite('Action_050_19', 4)	# 34780-34783
    sprite('Action_050_20', 6)	# 34784-34789
    sprite('Action_050_21', 7)	# 34790-34796
    sprite('Action_050_22', 2)	# 34797-34798
    Unknown21007(24, 40)
    Unknown21011(240)
    label(154)
    sprite('Action_000_00', 3)	# 34799-34801	 **attackbox here**
    sprite('Action_000_01', 6)	# 34802-34807	 **attackbox here**
    sprite('Action_000_02', 6)	# 34808-34813	 **attackbox here**
    sprite('Action_000_03', 6)	# 34814-34819	 **attackbox here**
    sprite('Action_000_04', 6)	# 34820-34825	 **attackbox here**
    sprite('Action_000_05', 6)	# 34826-34831	 **attackbox here**
    sprite('Action_000_06', 6)	# 34832-34837	 **attackbox here**
    sprite('Action_000_07', 6)	# 34838-34843	 **attackbox here**
    sprite('Action_000_08', 6)	# 34844-34849	 **attackbox here**
    sprite('Action_000_09', 6)	# 34850-34855	 **attackbox here**
    sprite('Action_000_10', 6)	# 34856-34861	 **attackbox here**
    sprite('Action_000_11', 6)	# 34862-34867	 **attackbox here**
    sprite('Action_000_12', 6)	# 34868-34873	 **attackbox here**
    sprite('Action_000_13', 6)	# 34874-34879	 **attackbox here**
    sprite('Action_000_14', 6)	# 34880-34885	 **attackbox here**
    sprite('Action_000_15', 6)	# 34886-34891	 **attackbox here**
    sprite('Action_000_16', 6)	# 34892-34897	 **attackbox here**
    sprite('Action_000_17', 6)	# 34898-34903	 **attackbox here**
    sprite('Action_000_18', 6)	# 34904-34909
    sprite('Action_000_19', 6)	# 34910-34915
    sprite('Action_000_20', 6)	# 34916-34921
    sprite('Action_000_21', 6)	# 34922-34927
    sprite('Action_000_22', 6)	# 34928-34933
    sprite('Action_000_23', 6)	# 34934-34939
    sprite('Action_000_24', 3)	# 34940-34942
    loopRest()
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('null', 2)	# 34943-34944
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(160)
    sprite('Action_050_02', 5)	# 34945-34949
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 162)
    label(161)
    sprite('Action_050_02', 3)	# 34950-34952
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('Action_050_02', 2)	# 34953-34954
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 34955-34956
    sprite('Action_050_04', 7)	# 34957-34963
    sprite('Action_050_05', 5)	# 34964-34968
    sprite('Action_050_06', 8)	# 34969-34976
    sprite('Action_050_07', 4)	# 34977-34980
    sprite('Action_050_23', 5)	# 34981-34985
    sprite('Action_050_24', 3)	# 34986-34988
    SFX_1('uor600rwi')
    sprite('Action_050_25', 5)	# 34989-34993
    label(163)
    sprite('Action_050_26', 5)	# 34994-34998
    sprite('Action_050_27', 5)	# 34999-35003
    sprite('Action_050_28', 5)	# 35004-35008
    sprite('Action_050_29', 5)	# 35009-35013
    sprite('Action_050_30', 5)	# 35014-35018
    if SLOT_97:
        _gotolabel(163)
    sprite('Action_050_31', 5)	# 35019-35023
    sprite('Action_050_32', 4)	# 35024-35027
    sprite('Action_050_33', 6)	# 35028-35033
    sprite('Action_050_34', 7)	# 35034-35040
    sprite('Action_050_35', 2)	# 35041-35042
    Unknown21007(24, 40)
    Unknown21011(240)
    label(164)
    sprite('Action_000_00', 3)	# 35043-35045	 **attackbox here**
    sprite('Action_000_01', 6)	# 35046-35051	 **attackbox here**
    sprite('Action_000_02', 6)	# 35052-35057	 **attackbox here**
    sprite('Action_000_03', 6)	# 35058-35063	 **attackbox here**
    sprite('Action_000_04', 6)	# 35064-35069	 **attackbox here**
    sprite('Action_000_05', 6)	# 35070-35075	 **attackbox here**
    sprite('Action_000_06', 6)	# 35076-35081	 **attackbox here**
    sprite('Action_000_07', 6)	# 35082-35087	 **attackbox here**
    sprite('Action_000_08', 6)	# 35088-35093	 **attackbox here**
    sprite('Action_000_09', 6)	# 35094-35099	 **attackbox here**
    sprite('Action_000_10', 6)	# 35100-35105	 **attackbox here**
    sprite('Action_000_11', 6)	# 35106-35111	 **attackbox here**
    sprite('Action_000_12', 6)	# 35112-35117	 **attackbox here**
    sprite('Action_000_13', 6)	# 35118-35123	 **attackbox here**
    sprite('Action_000_14', 6)	# 35124-35129	 **attackbox here**
    sprite('Action_000_15', 6)	# 35130-35135	 **attackbox here**
    sprite('Action_000_16', 6)	# 35136-35141	 **attackbox here**
    sprite('Action_000_17', 6)	# 35142-35147	 **attackbox here**
    sprite('Action_000_18', 6)	# 35148-35153
    sprite('Action_000_19', 6)	# 35154-35159
    sprite('Action_000_20', 6)	# 35160-35165
    sprite('Action_000_21', 6)	# 35166-35171
    sprite('Action_000_22', 6)	# 35172-35177
    sprite('Action_000_23', 6)	# 35178-35183
    sprite('Action_000_24', 3)	# 35184-35186
    loopRest()
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('Action_000_00', 1)	# 35187-35187	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
        SFX_1('uor601rbl')
    label(171)
    sprite('Action_000_00', 3)	# 35188-35190	 **attackbox here**
    sprite('Action_000_01', 6)	# 35191-35196	 **attackbox here**
    sprite('Action_000_02', 6)	# 35197-35202	 **attackbox here**
    sprite('Action_000_03', 6)	# 35203-35208	 **attackbox here**
    sprite('Action_000_04', 6)	# 35209-35214	 **attackbox here**
    sprite('Action_000_05', 6)	# 35215-35220	 **attackbox here**
    sprite('Action_000_06', 6)	# 35221-35226	 **attackbox here**
    sprite('Action_000_07', 6)	# 35227-35232	 **attackbox here**
    sprite('Action_000_08', 6)	# 35233-35238	 **attackbox here**
    sprite('Action_000_09', 6)	# 35239-35244	 **attackbox here**
    sprite('Action_000_10', 6)	# 35245-35250	 **attackbox here**
    sprite('Action_000_11', 6)	# 35251-35256	 **attackbox here**
    sprite('Action_000_12', 6)	# 35257-35262	 **attackbox here**
    sprite('Action_000_13', 6)	# 35263-35268	 **attackbox here**
    sprite('Action_000_14', 6)	# 35269-35274	 **attackbox here**
    sprite('Action_000_15', 6)	# 35275-35280	 **attackbox here**
    sprite('Action_000_16', 6)	# 35281-35286	 **attackbox here**
    sprite('Action_000_17', 6)	# 35287-35292	 **attackbox here**
    sprite('Action_000_18', 6)	# 35293-35298
    sprite('Action_000_19', 6)	# 35299-35304
    sprite('Action_000_20', 6)	# 35305-35310
    sprite('Action_000_21', 6)	# 35311-35316
    sprite('Action_000_22', 6)	# 35317-35322
    sprite('Action_000_23', 6)	# 35323-35328
    sprite('Action_000_24', 3)	# 35329-35331
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('Action_000_26', 5)	# 35332-35336
    sprite('Action_000_27', 5)	# 35337-35341
    sprite('Action_000_28', 7)	# 35342-35348
    sprite('Action_000_29', 4)	# 35349-35352
    sprite('Action_000_30', 4)	# 35353-35356
    sprite('Action_000_31', 9)	# 35357-35365
    sprite('Action_000_32', 5)	# 35366-35370
    sprite('Action_000_33', 5)	# 35371-35375
    Unknown23018(1)
    label(173)
    sprite('Action_000_00', 3)	# 35376-35378	 **attackbox here**
    sprite('Action_000_01', 6)	# 35379-35384	 **attackbox here**
    sprite('Action_000_02', 6)	# 35385-35390	 **attackbox here**
    sprite('Action_000_03', 6)	# 35391-35396	 **attackbox here**
    sprite('Action_000_04', 6)	# 35397-35402	 **attackbox here**
    sprite('Action_000_05', 6)	# 35403-35408	 **attackbox here**
    sprite('Action_000_06', 6)	# 35409-35414	 **attackbox here**
    sprite('Action_000_07', 6)	# 35415-35420	 **attackbox here**
    sprite('Action_000_08', 6)	# 35421-35426	 **attackbox here**
    sprite('Action_000_09', 6)	# 35427-35432	 **attackbox here**
    sprite('Action_000_10', 6)	# 35433-35438	 **attackbox here**
    sprite('Action_000_11', 6)	# 35439-35444	 **attackbox here**
    sprite('Action_000_12', 6)	# 35445-35450	 **attackbox here**
    sprite('Action_000_13', 6)	# 35451-35456	 **attackbox here**
    sprite('Action_000_14', 6)	# 35457-35462	 **attackbox here**
    sprite('Action_000_15', 6)	# 35463-35468	 **attackbox here**
    sprite('Action_000_16', 6)	# 35469-35474	 **attackbox here**
    sprite('Action_000_17', 6)	# 35475-35480	 **attackbox here**
    sprite('Action_000_18', 6)	# 35481-35486
    sprite('Action_000_19', 6)	# 35487-35492
    sprite('Action_000_20', 6)	# 35493-35498
    sprite('Action_000_21', 6)	# 35499-35504
    sprite('Action_000_22', 6)	# 35505-35510
    sprite('Action_000_23', 6)	# 35511-35516
    sprite('Action_000_24', 3)	# 35517-35519
    loopRest()
    gotoLabel(173)
    ExitState()
    label(180)
    sprite('null', 2)	# 35520-35521
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(180)
    sprite('Action_050_02', 5)	# 35522-35526
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown3038(0)
    teleportRelativeY(600000)
    physicsYImpulse(-2000)
    setGravity(1500)
    sendToLabelUpon(2, 182)
    label(181)
    sprite('Action_050_02', 3)	# 35527-35529
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('Action_050_02', 2)	# 35530-35531
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    sprite('Action_050_03', 2)	# 35532-35533
    sprite('Action_050_04', 7)	# 35534-35540
    sprite('Action_050_05', 5)	# 35541-35545
    sprite('Action_050_06', 8)	# 35546-35553
    sprite('Action_050_07', 4)	# 35554-35557
    sprite('Action_050_23', 5)	# 35558-35562
    sprite('Action_050_24', 3)	# 35563-35565
    SFX_1('uor600pmi')
    sprite('Action_050_25', 5)	# 35566-35570
    label(183)
    sprite('Action_050_26', 5)	# 35571-35575
    sprite('Action_050_27', 5)	# 35576-35580
    sprite('Action_050_28', 5)	# 35581-35585
    sprite('Action_050_29', 5)	# 35586-35590
    sprite('Action_050_30', 5)	# 35591-35595
    if SLOT_97:
        _gotolabel(183)
    sprite('Action_050_31', 5)	# 35596-35600
    sprite('Action_050_32', 4)	# 35601-35604
    sprite('Action_050_33', 6)	# 35605-35610
    sprite('Action_050_34', 7)	# 35611-35617
    sprite('Action_050_35', 2)	# 35618-35619
    Unknown21007(24, 40)
    Unknown21011(270)
    label(184)
    sprite('Action_000_00', 3)	# 35620-35622	 **attackbox here**
    sprite('Action_000_01', 6)	# 35623-35628	 **attackbox here**
    sprite('Action_000_02', 6)	# 35629-35634	 **attackbox here**
    sprite('Action_000_03', 6)	# 35635-35640	 **attackbox here**
    sprite('Action_000_04', 6)	# 35641-35646	 **attackbox here**
    sprite('Action_000_05', 6)	# 35647-35652	 **attackbox here**
    sprite('Action_000_06', 6)	# 35653-35658	 **attackbox here**
    sprite('Action_000_07', 6)	# 35659-35664	 **attackbox here**
    sprite('Action_000_08', 6)	# 35665-35670	 **attackbox here**
    sprite('Action_000_09', 6)	# 35671-35676	 **attackbox here**
    sprite('Action_000_10', 6)	# 35677-35682	 **attackbox here**
    sprite('Action_000_11', 6)	# 35683-35688	 **attackbox here**
    sprite('Action_000_12', 6)	# 35689-35694	 **attackbox here**
    sprite('Action_000_13', 6)	# 35695-35700	 **attackbox here**
    sprite('Action_000_14', 6)	# 35701-35706	 **attackbox here**
    sprite('Action_000_15', 6)	# 35707-35712	 **attackbox here**
    sprite('Action_000_16', 6)	# 35713-35718	 **attackbox here**
    sprite('Action_000_17', 6)	# 35719-35724	 **attackbox here**
    sprite('Action_000_18', 6)	# 35725-35730
    sprite('Action_000_19', 6)	# 35731-35736
    sprite('Action_000_20', 6)	# 35737-35742
    sprite('Action_000_21', 6)	# 35743-35748
    sprite('Action_000_22', 6)	# 35749-35754
    sprite('Action_000_23', 6)	# 35755-35760
    sprite('Action_000_24', 3)	# 35761-35763
    loopRest()
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('Ori634_00', 1)	# 35764-35764	 **attackbox here**
    Unknown1000(-1230000)
    SFX_1('uor600biz')

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Ori634_00', 1)	# 35765-35765	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Ori634_00', 10)	# 35766-35775	 **attackbox here**
    sprite('Ori634_00', 32767)	# 35776-68542	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(192)
    sprite('Ori634_01', 6)	# 68543-68548
    sprite('Ori634_02', 6)	# 68549-68554
    sprite('Ori634_03', 6)	# 68555-68560	 **attackbox here**
    sprite('Ori634_04', 6)	# 68561-68566	 **attackbox here**
    sprite('Ori634_05', 6)	# 68567-68572	 **attackbox here**
    sprite('Ori634_06', 32767)	# 68573-101339	 **attackbox here**
    ExitState()
    label(200)
    sprite('Action_000_00', 1)	# 101340-101340	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        SFX_1('uor601umi')
        Unknown23018(1)
    label(201)
    sprite('Action_000_00', 3)	# 101341-101343	 **attackbox here**
    sprite('Action_000_01', 6)	# 101344-101349	 **attackbox here**
    sprite('Action_000_02', 6)	# 101350-101355	 **attackbox here**
    sprite('Action_000_03', 6)	# 101356-101361	 **attackbox here**
    sprite('Action_000_04', 6)	# 101362-101367	 **attackbox here**
    sprite('Action_000_05', 6)	# 101368-101373	 **attackbox here**
    sprite('Action_000_06', 6)	# 101374-101379	 **attackbox here**
    sprite('Action_000_07', 6)	# 101380-101385	 **attackbox here**
    sprite('Action_000_08', 6)	# 101386-101391	 **attackbox here**
    sprite('Action_000_09', 6)	# 101392-101397	 **attackbox here**
    sprite('Action_000_10', 6)	# 101398-101403	 **attackbox here**
    sprite('Action_000_11', 6)	# 101404-101409	 **attackbox here**
    sprite('Action_000_12', 6)	# 101410-101415	 **attackbox here**
    sprite('Action_000_13', 6)	# 101416-101421	 **attackbox here**
    sprite('Action_000_14', 6)	# 101422-101427	 **attackbox here**
    sprite('Action_000_15', 6)	# 101428-101433	 **attackbox here**
    sprite('Action_000_16', 6)	# 101434-101439	 **attackbox here**
    sprite('Action_000_17', 6)	# 101440-101445	 **attackbox here**
    sprite('Action_000_18', 6)	# 101446-101451
    sprite('Action_000_19', 6)	# 101452-101457
    sprite('Action_000_20', 6)	# 101458-101463
    sprite('Action_000_21', 6)	# 101464-101469
    sprite('Action_000_22', 6)	# 101470-101475
    sprite('Action_000_23', 6)	# 101476-101481
    sprite('Action_000_24', 3)	# 101482-101484
    loopRest()
    gotoLabel(201)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 101485-101485	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 3)	# 101486-101488	 **attackbox here**
    sprite('Action_000_01', 6)	# 101489-101494	 **attackbox here**
    sprite('Action_000_02', 6)	# 101495-101500	 **attackbox here**
    sprite('Action_000_03', 6)	# 101501-101506	 **attackbox here**
    sprite('Action_000_04', 6)	# 101507-101512	 **attackbox here**
    sprite('Action_000_05', 6)	# 101513-101518	 **attackbox here**
    sprite('Action_000_06', 6)	# 101519-101524	 **attackbox here**
    sprite('Action_000_07', 6)	# 101525-101530	 **attackbox here**
    sprite('Action_000_08', 6)	# 101531-101536	 **attackbox here**
    sprite('Action_000_09', 6)	# 101537-101542	 **attackbox here**
    sprite('Action_000_10', 6)	# 101543-101548	 **attackbox here**
    sprite('Action_000_11', 6)	# 101549-101554	 **attackbox here**
    sprite('Action_000_12', 6)	# 101555-101560	 **attackbox here**
    sprite('Action_000_13', 6)	# 101561-101566	 **attackbox here**
    sprite('Action_000_14', 6)	# 101567-101572	 **attackbox here**
    sprite('Action_000_15', 6)	# 101573-101578	 **attackbox here**
    sprite('Action_000_16', 6)	# 101579-101584	 **attackbox here**
    sprite('Action_000_17', 6)	# 101585-101590	 **attackbox here**
    sprite('Action_000_18', 6)	# 101591-101596
    sprite('Action_000_19', 6)	# 101597-101602
    sprite('Action_000_20', 6)	# 101603-101608
    sprite('Action_000_21', 6)	# 101609-101614
    sprite('Action_000_22', 6)	# 101615-101620
    sprite('Action_000_23', 6)	# 101621-101626
    sprite('Action_000_24', 3)	# 101627-101629
    loopRest()
    gotoLabel(992)
    label(993)
    sprite('Action_046_00', 2)	# 101630-101631

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
    sprite('Action_046_01', 2)	# 101632-101633
    sprite('Action_046_02', 1)	# 101634-101634
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 101635-101637
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
            if PartnerChar('brg'):
                if (SLOT_145 < 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bjn'):
                if (SLOT_145 < 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 < 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 < 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 < 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 < 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 < 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 < 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 < 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('biz'):
                if (SLOT_145 < 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 700000):
                    if (SLOT_145 >= 200000):
                        sendToLabel(200)
                        clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    sprite('keep', 1)	# 4-4
    if (not SLOT_52):
        if (not SLOT_108):
            if random_(2, 0, 50):
                sendToLabel(10)
    sprite('Action_053_00', 5)	# 5-9
    sprite('Action_053_01', 5)	# 10-14
    sprite('Action_053_02', 7)	# 15-21
    sprite('Action_053_03', 4)	# 22-25
    sprite('Action_053_04', 3)	# 26-28
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 29-36
    sprite('Action_053_06', 7)	# 37-43
    sprite('Action_053_07', 7)	# 44-50
    sprite('Action_053_08', 5)	# 51-55	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uor524', 100, 896692085, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uor402_0', 100, 879914869, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uor520', 100, 896692085, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_053_09', 20)	# 56-75	 **attackbox here**
    Unknown23018(1)
    label(1)
    sprite('Action_053_10', 5)	# 76-80	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('Action_052_00', 5)	# 81-85
    sprite('Action_052_01', 5)	# 86-90
    sprite('Action_052_02', 4)	# 91-94
    sprite('Action_052_03', 5)	# 95-99
    sprite('Action_052_04', 5)	# 100-104	 **attackbox here**
    if SLOT_158:
        Unknown7006('uor522', 100, 896692085, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(11)
    sprite('Action_052_05', 5)	# 105-109	 **attackbox here**
    sprite('Action_052_06', 5)	# 110-114	 **attackbox here**
    sprite('Action_052_07', 5)	# 115-119	 **attackbox here**
    sprite('Action_052_08', 5)	# 120-124	 **attackbox here**
    sprite('Action_052_09', 5)	# 125-129	 **attackbox here**
    loopRest()
    gotoLabel(11)
    label(100)
    sprite('Action_053_00', 5)	# 130-134
    sprite('Action_053_01', 5)	# 135-139
    sprite('Action_053_02', 7)	# 140-146
    sprite('Action_053_03', 4)	# 147-150
    sprite('Action_053_04', 3)	# 151-153
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 154-161
    sprite('Action_053_06', 7)	# 162-168
    sprite('Action_053_07', 7)	# 169-175
    sprite('Action_053_08', 5)	# 176-180	 **attackbox here**
    SFX_1('uor700brg')
    sprite('Action_053_09', 20)	# 181-200	 **attackbox here**
    label(101)
    sprite('Action_053_10', 1)	# 201-201	 **attackbox here**
    if SLOT_97:
        _gotolabel(101)
    sprite('Action_053_10', 30)	# 202-231	 **attackbox here**
    sprite('Action_053_10', 32767)	# 232-32998	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(110)
    sprite('Action_053_00', 5)	# 32999-33003
    sprite('Action_053_01', 5)	# 33004-33008
    sprite('Action_053_02', 7)	# 33009-33015
    sprite('Action_053_03', 4)	# 33016-33019
    sprite('Action_053_04', 3)	# 33020-33022
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 33023-33030
    sprite('Action_053_06', 7)	# 33031-33037
    sprite('Action_053_07', 7)	# 33038-33044
    sprite('Action_053_08', 5)	# 33045-33049	 **attackbox here**
    SFX_1('uor700bjn')
    sprite('Action_053_09', 20)	# 33050-33069	 **attackbox here**
    label(111)
    sprite('Action_053_10', 1)	# 33070-33070	 **attackbox here**
    if SLOT_97:
        _gotolabel(111)
    sprite('Action_053_10', 15)	# 33071-33085	 **attackbox here**
    sprite('Action_053_10', 32767)	# 33086-65852	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(320)
    label(120)
    sprite('Action_053_00', 5)	# 65853-65857
    sprite('Action_053_01', 5)	# 65858-65862
    sprite('Action_053_02', 7)	# 65863-65869
    sprite('Action_053_03', 4)	# 65870-65873
    sprite('Action_053_04', 3)	# 65874-65876
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 65877-65884
    sprite('Action_053_06', 7)	# 65885-65891
    sprite('Action_053_07', 7)	# 65892-65898
    sprite('Action_053_08', 5)	# 65899-65903	 **attackbox here**
    SFX_1('uor700bjb')
    sprite('Action_053_09', 20)	# 65904-65923	 **attackbox here**
    label(121)
    sprite('Action_053_10', 1)	# 65924-65924	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_053_10', 30)	# 65925-65954	 **attackbox here**
    sprite('Action_053_10', 32767)	# 65955-98721	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(130)
    sprite('Action_053_00', 5)	# 98722-98726
    sprite('Action_053_01', 5)	# 98727-98731
    sprite('Action_053_02', 7)	# 98732-98738
    sprite('Action_053_03', 4)	# 98739-98742
    sprite('Action_053_04', 3)	# 98743-98745
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 98746-98753
    sprite('Action_053_06', 7)	# 98754-98760
    sprite('Action_053_07', 7)	# 98761-98767
    sprite('Action_053_08', 5)	# 98768-98772	 **attackbox here**
    SFX_1('uor700pna')
    sprite('Action_053_09', 20)	# 98773-98792	 **attackbox here**
    label(131)
    sprite('Action_053_10', 1)	# 98793-98793	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_053_10', 32767)	# 98794-131560	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(200)
    label(140)
    sprite('Action_052_00', 5)	# 131561-131565
    sprite('Action_052_01', 5)	# 131566-131570
    sprite('Action_052_02', 4)	# 131571-131574
    sprite('Action_052_03', 5)	# 131575-131579
    sprite('Action_052_04', 5)	# 131580-131584	 **attackbox here**
    SFX_1('uor700uhy')
    label(141)
    sprite('Action_052_05', 5)	# 131585-131589	 **attackbox here**
    sprite('Action_052_06', 5)	# 131590-131594	 **attackbox here**
    sprite('Action_052_07', 5)	# 131595-131599	 **attackbox here**
    sprite('Action_052_08', 5)	# 131600-131604	 **attackbox here**
    sprite('Action_052_09', 5)	# 131605-131609	 **attackbox here**
    loopRest()
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_052_05', 1)	# 131610-131610	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(142)
    sprite('Action_052_05', 5)	# 131611-131615	 **attackbox here**
    sprite('Action_052_06', 5)	# 131616-131620	 **attackbox here**
    sprite('Action_052_07', 5)	# 131621-131625	 **attackbox here**
    sprite('Action_052_08', 5)	# 131626-131630	 **attackbox here**
    sprite('Action_052_09', 5)	# 131631-131635	 **attackbox here**
    gotoLabel(142)
    label(150)
    sprite('Action_053_00', 5)	# 131636-131640
    sprite('Action_053_01', 5)	# 131641-131645
    sprite('Action_053_02', 7)	# 131646-131652
    sprite('Action_053_03', 4)	# 131653-131656
    sprite('Action_053_04', 3)	# 131657-131659
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 131660-131667
    sprite('Action_053_06', 7)	# 131668-131674
    sprite('Action_053_07', 7)	# 131675-131681
    sprite('Action_053_08', 5)	# 131682-131686	 **attackbox here**
    SFX_1('uor700uli')
    sprite('Action_053_09', 20)	# 131687-131706	 **attackbox here**
    label(151)
    sprite('Action_053_10', 1)	# 131707-131707	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('Action_053_10', 30)	# 131708-131737	 **attackbox here**
    sprite('Action_053_10', 32767)	# 131738-164504	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    label(160)
    sprite('Action_000_00', 1)	# 164505-164505	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)

    def upon_39():
        clearUponHandler(39)
        sendToLabel(164)
    label(161)
    sprite('Action_000_00', 3)	# 164506-164508	 **attackbox here**
    sprite('Action_000_01', 6)	# 164509-164514	 **attackbox here**
    sprite('Action_000_02', 6)	# 164515-164520	 **attackbox here**
    sprite('Action_000_03', 6)	# 164521-164526	 **attackbox here**
    sprite('Action_000_04', 6)	# 164527-164532	 **attackbox here**
    sprite('Action_000_05', 6)	# 164533-164538	 **attackbox here**
    sprite('Action_000_06', 6)	# 164539-164544	 **attackbox here**
    sprite('Action_000_07', 6)	# 164545-164550	 **attackbox here**
    sprite('Action_000_08', 6)	# 164551-164556	 **attackbox here**
    sprite('Action_000_09', 6)	# 164557-164562	 **attackbox here**
    sprite('Action_000_10', 6)	# 164563-164568	 **attackbox here**
    sprite('Action_000_11', 6)	# 164569-164574	 **attackbox here**
    sprite('Action_000_12', 6)	# 164575-164580	 **attackbox here**
    sprite('Action_000_13', 6)	# 164581-164586	 **attackbox here**
    sprite('Action_000_14', 6)	# 164587-164592	 **attackbox here**
    sprite('Action_000_15', 6)	# 164593-164598	 **attackbox here**
    sprite('Action_000_16', 6)	# 164599-164604	 **attackbox here**
    sprite('Action_000_17', 6)	# 164605-164610	 **attackbox here**
    sprite('Action_000_18', 6)	# 164611-164616
    sprite('Action_000_19', 6)	# 164617-164622
    sprite('Action_000_20', 6)	# 164623-164628
    sprite('Action_000_21', 6)	# 164629-164634
    sprite('Action_000_22', 6)	# 164635-164640
    sprite('Action_000_23', 6)	# 164641-164646
    sprite('Action_000_24', 3)	# 164647-164649
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('Action_053_00', 5)	# 164650-164654
    sprite('Action_053_01', 5)	# 164655-164659
    sprite('Action_053_02', 7)	# 164660-164666
    sprite('Action_053_03', 4)	# 164667-164670
    sprite('Action_053_04', 3)	# 164671-164673
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 164674-164681
    sprite('Action_053_06', 7)	# 164682-164688
    sprite('Action_053_07', 7)	# 164689-164695
    sprite('Action_053_08', 5)	# 164696-164700	 **attackbox here**
    SFX_1('uor701rwi')
    label(163)
    sprite('Action_053_09', 1)	# 164701-164701	 **attackbox here**
    if SLOT_97:
        _gotolabel(163)
    sprite('Action_053_09', 40)	# 164702-164741	 **attackbox here**
    sprite('Action_053_10', 32767)	# 164742-197508	 **attackbox here**
    Unknown21007(24, 40)
    label(164)
    sprite('Action_053_10', 32767)	# 197509-230275	 **attackbox here**
    SFX_1('uor703rwi')
    Unknown23018(1)
    label(170)
    sprite('Action_000_00', 1)	# 230276-230276	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_00', 3)	# 230277-230279	 **attackbox here**
    sprite('Action_000_01', 6)	# 230280-230285	 **attackbox here**
    sprite('Action_000_02', 6)	# 230286-230291	 **attackbox here**
    sprite('Action_000_03', 6)	# 230292-230297	 **attackbox here**
    sprite('Action_000_04', 6)	# 230298-230303	 **attackbox here**
    sprite('Action_000_05', 6)	# 230304-230309	 **attackbox here**
    sprite('Action_000_06', 6)	# 230310-230315	 **attackbox here**
    sprite('Action_000_07', 6)	# 230316-230321	 **attackbox here**
    sprite('Action_000_08', 6)	# 230322-230327	 **attackbox here**
    sprite('Action_000_09', 6)	# 230328-230333	 **attackbox here**
    sprite('Action_000_10', 6)	# 230334-230339	 **attackbox here**
    sprite('Action_000_11', 6)	# 230340-230345	 **attackbox here**
    sprite('Action_000_12', 6)	# 230346-230351	 **attackbox here**
    sprite('Action_000_13', 6)	# 230352-230357	 **attackbox here**
    sprite('Action_000_14', 6)	# 230358-230363	 **attackbox here**
    sprite('Action_000_15', 6)	# 230364-230369	 **attackbox here**
    sprite('Action_000_16', 6)	# 230370-230375	 **attackbox here**
    sprite('Action_000_17', 6)	# 230376-230381	 **attackbox here**
    sprite('Action_000_18', 6)	# 230382-230387
    sprite('Action_000_19', 6)	# 230388-230393
    sprite('Action_000_20', 6)	# 230394-230399
    sprite('Action_000_21', 6)	# 230400-230405
    sprite('Action_000_22', 6)	# 230406-230411
    sprite('Action_000_23', 6)	# 230412-230417
    sprite('Action_000_24', 3)	# 230418-230420
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('Action_053_00', 5)	# 230421-230425
    sprite('Action_053_01', 5)	# 230426-230430
    sprite('Action_053_02', 7)	# 230431-230437
    sprite('Action_053_03', 4)	# 230438-230441
    sprite('Action_053_04', 3)	# 230442-230444
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 230445-230452
    sprite('Action_053_06', 7)	# 230453-230459
    sprite('Action_053_07', 7)	# 230460-230466
    sprite('Action_053_08', 5)	# 230467-230471	 **attackbox here**
    SFX_1('uor701rbl')
    label(173)
    sprite('Action_053_09', 1)	# 230472-230472	 **attackbox here**
    if SLOT_97:
        _gotolabel(173)
    sprite('Action_053_10', 32767)	# 230473-263239	 **attackbox here**
    Unknown23018(1)
    label(180)
    sprite('Action_053_00', 5)	# 263240-263244
    sprite('Action_053_01', 5)	# 263245-263249
    sprite('Action_053_02', 7)	# 263250-263256
    sprite('Action_053_03', 4)	# 263257-263260
    sprite('Action_053_04', 3)	# 263261-263263
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 263264-263271
    sprite('Action_053_06', 7)	# 263272-263278
    sprite('Action_053_07', 7)	# 263279-263285
    sprite('Action_053_08', 5)	# 263286-263290	 **attackbox here**
    SFX_1('uor700pmi')
    label(181)
    sprite('Action_053_09', 1)	# 263291-263291	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_053_10', 32767)	# 263292-296058	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(260)
    label(190)
    sprite('Action_000_00', 1)	# 296059-296059	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_000_00', 3)	# 296060-296062	 **attackbox here**
    sprite('Action_000_01', 6)	# 296063-296068	 **attackbox here**
    sprite('Action_000_02', 6)	# 296069-296074	 **attackbox here**
    sprite('Action_000_03', 6)	# 296075-296080	 **attackbox here**
    sprite('Action_000_04', 6)	# 296081-296086	 **attackbox here**
    sprite('Action_000_05', 6)	# 296087-296092	 **attackbox here**
    sprite('Action_000_06', 6)	# 296093-296098	 **attackbox here**
    sprite('Action_000_07', 6)	# 296099-296104	 **attackbox here**
    sprite('Action_000_08', 6)	# 296105-296110	 **attackbox here**
    sprite('Action_000_09', 6)	# 296111-296116	 **attackbox here**
    sprite('Action_000_10', 6)	# 296117-296122	 **attackbox here**
    sprite('Action_000_11', 6)	# 296123-296128	 **attackbox here**
    sprite('Action_000_12', 6)	# 296129-296134	 **attackbox here**
    sprite('Action_000_13', 6)	# 296135-296140	 **attackbox here**
    sprite('Action_000_14', 6)	# 296141-296146	 **attackbox here**
    sprite('Action_000_15', 6)	# 296147-296152	 **attackbox here**
    sprite('Action_000_16', 6)	# 296153-296158	 **attackbox here**
    sprite('Action_000_17', 6)	# 296159-296164	 **attackbox here**
    sprite('Action_000_18', 6)	# 296165-296170
    sprite('Action_000_19', 6)	# 296171-296176
    sprite('Action_000_20', 6)	# 296177-296182
    sprite('Action_000_21', 6)	# 296183-296188
    sprite('Action_000_22', 6)	# 296189-296194
    sprite('Action_000_23', 6)	# 296195-296200
    sprite('Action_000_24', 3)	# 296201-296203
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('Action_053_00', 5)	# 296204-296208
    sprite('Action_053_01', 5)	# 296209-296213
    sprite('Action_053_02', 7)	# 296214-296220
    sprite('Action_053_03', 4)	# 296221-296224
    sprite('Action_053_04', 3)	# 296225-296227
    SFX_3('SE042')
    sprite('Action_053_05', 8)	# 296228-296235
    sprite('Action_053_06', 7)	# 296236-296242
    sprite('Action_053_07', 7)	# 296243-296249
    sprite('Action_053_08', 5)	# 296250-296254	 **attackbox here**
    SFX_1('uor701biz')
    Unknown23018(1)
    sprite('Action_053_10', 32767)	# 296255-329021	 **attackbox here**
    label(200)
    sprite('Action_000_00', 1)	# 329022-329022	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 3)	# 329023-329025	 **attackbox here**
    sprite('Action_000_01', 6)	# 329026-329031	 **attackbox here**
    sprite('Action_000_02', 6)	# 329032-329037	 **attackbox here**
    sprite('Action_000_03', 6)	# 329038-329043	 **attackbox here**
    sprite('Action_000_04', 6)	# 329044-329049	 **attackbox here**
    sprite('Action_000_05', 6)	# 329050-329055	 **attackbox here**
    sprite('Action_000_06', 6)	# 329056-329061	 **attackbox here**
    sprite('Action_000_07', 6)	# 329062-329067	 **attackbox here**
    sprite('Action_000_08', 6)	# 329068-329073	 **attackbox here**
    sprite('Action_000_09', 6)	# 329074-329079	 **attackbox here**
    sprite('Action_000_10', 6)	# 329080-329085	 **attackbox here**
    sprite('Action_000_11', 6)	# 329086-329091	 **attackbox here**
    sprite('Action_000_12', 6)	# 329092-329097	 **attackbox here**
    sprite('Action_000_13', 6)	# 329098-329103	 **attackbox here**
    sprite('Action_000_14', 6)	# 329104-329109	 **attackbox here**
    sprite('Action_000_15', 6)	# 329110-329115	 **attackbox here**
    sprite('Action_000_16', 6)	# 329116-329121	 **attackbox here**
    sprite('Action_000_17', 6)	# 329122-329127	 **attackbox here**
    sprite('Action_000_18', 6)	# 329128-329133
    sprite('Action_000_19', 6)	# 329134-329139
    sprite('Action_000_20', 6)	# 329140-329145
    sprite('Action_000_21', 6)	# 329146-329151
    sprite('Action_000_22', 6)	# 329152-329157
    sprite('Action_000_23', 6)	# 329158-329163
    sprite('Action_000_24', 3)	# 329164-329166
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('keep', 1)	# 329167-329167
    Unknown2037(1)
    Unknown2019(-500)
    sprite('Action_010_00', 1)	# 329168-329168
    if (not SLOT_39):
        Unknown48('190000000200000033000000180000000200000016000000')
        Unknown47('01000000020000003300000002000000160000000200000033000000')
        if (SLOT_51 >= 0):
            pass
        else:
            Unknown2005()
    else:
        Unknown48('190000000200000033000000180000000200000016000000')
        Unknown47('01000000020000003300000002000000160000000200000033000000')
        if (SLOT_51 <= 0):
            pass
        else:
            Unknown2005()
    sprite('Action_010_00', 1)	# 329169-329169
    physicsXImpulse(8000)
    Unknown20000(1)

    def upon_3():
        if SLOT_2:
            if (SLOT_145 < 120000):
                Unknown2037(0)
                sendToLabel(204)
    label(203)
    sprite('Action_010_01', 4)	# 329170-329173
    sprite('Action_010_02', 4)	# 329174-329177
    sprite('Action_010_03', 3)	# 329178-329180
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_04', 3)	# 329181-329183
    sprite('Action_010_05', 4)	# 329184-329187
    sprite('Action_010_06', 4)	# 329188-329191
    sprite('Action_010_07', 4)	# 329192-329195
    sprite('Action_010_08', 4)	# 329196-329199
    sprite('Action_010_09', 3)	# 329200-329202
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_10', 3)	# 329203-329205
    sprite('Action_010_11', 4)	# 329206-329209
    sprite('Action_010_12', 4)	# 329210-329213
    loopRest()
    gotoLabel(203)
    label(204)
    sprite('Ori648_00', 6)	# 329214-329219
    Unknown1084(1)
    clearUponHandler(3)
    sprite('Ori648_01', 6)	# 329220-329225
    sprite('Ori648_02', 6)	# 329226-329231
    sprite('Ori648_03', 6)	# 329232-329237	 **attackbox here**
    sprite('Ori648_04', 6)	# 329238-329243	 **attackbox here**
    sprite('Ori648_05', 6)	# 329244-329249	 **attackbox here**
    SFX_1('uor701umi')
    Unknown23018(1)
    sprite('Ori648_06', 32767)	# 329250-362016	 **attackbox here**

@State
def CmnActLose():
    sprite('Action_248_00', 4)	# 1-4
    sprite('Action_248_01', 5)	# 5-9
    sprite('Action_248_02', 7)	# 10-16
    sprite('Action_248_03', 1)	# 17-17	 **attackbox here**
    if SLOT_158:
        Unknown7006('uor403_0', 100, 879914869, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    label(1)
    sprite('Action_248_04', 1)	# 18-18	 **attackbox here**
    gotoLabel(1)

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