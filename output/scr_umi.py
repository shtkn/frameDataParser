@Subroutine
def PreInit():
    Unknown12019('756d6900000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(18000)
    DashFAccel(1000)
    DashFMaxVelocity(32000)
    Unknown12038(23000)
    Unknown12034(33)
    Unknown12036(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
    Unknown13039(1)
    Unknown2049(1)
    Unknown23003(0, 0, 0, 1, 1, 1, -49152, -49152)
    Unknown23003(1, 0, 0, 1, 3, 0, -49152, -49152)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(-2000, 230000, -248000, 114000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(-2000, 230000, -248000, 114000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15015(30, 40)
    Unknown14015(-2000, 230000, -248000, 114000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(0, 460000, -200000, 160000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 460000, -200000, 160000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_2ndShot', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 460000, -200000, 160000, 1500, 50)
    Move_EndRegister()
    Move_Register('AN_NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 460000, -200000, 160000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 280000, -200000, -61000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(2500)
    Unknown14015(-36000, 387000, 50000, 412000, 200, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(0, 560000, -200000, -40000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(-2000, 298000, -353000, 128000, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(-150000, 320000, -360000, 122000, 1200, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(-161000, 450000, -650000, 34000, 600, 50)
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
    Move_AirGround_(0x304d)
    Unknown14015(14000, 1800000, -27000, 95000, 200, 50)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x304d)
    Unknown15021(2000)
    Unknown14015(14000, 300000, -27000, 550000, 125, 50)
    Move_EndRegister()
    Move_Register('CommandThrow_A', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15010()
    Unknown15021(50)
    Unknown15012(2500)
    Unknown14015(14000, 400000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('CommandThrow_B', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15010()
    Unknown15021(50)
    Unknown15012(2500)
    Unknown14015(14000, 400000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('AssaultA_Air', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Move_AirGround_(0x304d)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('AssaultB_Air', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Move_AirGround_(0x304d)
    Unknown15021(500)
    Unknown14015(14000, 300000, -300000, 0, 500, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_5', INPUT_SPECIALMOVE)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14013('Assault_Add_6')
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_6', INPUT_SPECIALMOVE)
    Move_Input_(0x78)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_4', INPUT_SPECIALMOVE)
    Move_Input_(0x5e)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_8', INPUT_SPECIALMOVE)
    Move_Input_(0x92)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_2', INPUT_SPECIALMOVE)
    Move_Input_(0x44)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_9', INPUT_SPECIALMOVE)
    Move_Input_(0x9f)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_7', INPUT_SPECIALMOVE)
    Move_Input_(0x85)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_1', INPUT_SPECIALMOVE)
    Move_Input_(0x37)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('Assault_Add_3', INPUT_SPECIALMOVE)
    Move_Input_(0x51)
    Move_Input_(0xed)
    Unknown14005(1)
    Move_AirGround_(0x304e)
    Unknown15012(2500)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('AssaultEX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x304d)
    Unknown15005(10)
    Unknown15012(2500)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('CommandThrow_EX', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15005(10)
    Unknown15010()
    Unknown15021(50)
    Unknown15012(2500)
    Unknown14015(14000, 550000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('AssaultEX_Air', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x304d)
    Unknown15005(10)
    Unknown15012(2500)
    Unknown14015(14000, 1800000, -27000, 95000, 250, 50)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 266000, -123000, 755000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(7000, 266000, -123000, 755000, 250, 0)
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
    Unknown14015(-100000, 246000, -123000, 755000, 500, 0)
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
    Unknown14015(-100000, 246000, -123000, 755000, 500, 0)
    Move_EndRegister()
    Move_Register('AirUltimateAssault', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-100000, 246000, -123000, 755000, 500, 0)
    Move_EndRegister()
    Move_Register('AirUltimateAssaultOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x3009)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-100000, 246000, -123000, 755000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateThrow', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15012(0)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15021(50)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 100000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateThrowOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15012(0)
    Unknown15013(1)
    Unknown15021(50)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 100000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15010()
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(50000, 250000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'AN_NmlAtk5A_2nd', 10000000)
    Unknown15024('AN_NmlAtk5A_2nd', 'AN_NmlAtk5A_3rd', 10000000)
    Unknown15024('AN_NmlAtk5A_3rd', 'AN_NmlAtk5A_4th', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'CommandThrow_A', 10000000)
    Unknown15024('NmlAtk5B', 'AN_NmlAtk5B_2nd', 10000000)
    Unknown15024('AN_NmlAtk5B_2nd', 'AN_NmlAtk5B_3rd', 10000000)
    Unknown15024('AN_NmlAtk5B_3rd', 'AssultB', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('AssultA', 'Assault_Add_5', 10000000)
    Unknown15024('AssultB', 'Assault_Add_5', 10000000)
    Unknown15024('AssultEX', 'Assault_Add_5', 10000000)
    Unknown15024('AssaultA_Air', 'Assault_Add_5', 10000000)
    Unknown15024('AssaultB_Air', 'Assault_Add_5', 10000000)
    Unknown15024('AssaultEX_Air', 'Assault_Add_5', 10000000)
    Unknown15024('Assault_Add_5', 'Assault_Add_5', 10000000)
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
    Unknown12018(29, 'Action_354_04')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'umi000')
    Unknown7010(1, 'umi001')
    Unknown7010(2, 'umi002')
    Unknown7010(3, 'umi003')
    Unknown7010(4, 'umi004')
    Unknown7010(5, 'umi005')
    Unknown7010(6, 'umi006')
    Unknown7010(7, 'umi007')
    Unknown7010(8, 'umi008')
    Unknown7010(9, 'umi009')
    Unknown7010(10, 'umi010')
    Unknown7010(15, 'umi011')
    Unknown7010(16, 'umi012')
    Unknown7010(17, 'umi013')
    Unknown7010(18, 'umi014')
    Unknown7010(19, 'umi015')
    Unknown7010(20, 'umi016')
    Unknown7010(21, 'umi017')
    Unknown7010(22, 'umi018')
    Unknown7010(23, 'umi019')
    Unknown7010(24, 'umi020')
    Unknown7010(25, 'umi021')
    Unknown7010(28, 'umi022')
    Unknown7010(29, 'umi023')
    Unknown7010(30, 'umi024')
    Unknown7010(31, 'umi025')
    Unknown7010(32, 'umi026')
    Unknown7010(33, 'umi027')
    Unknown7010(34, 'umi028')
    Unknown7010(35, 'umi029')
    Unknown7010(36, 'umi030')
    Unknown7010(37, 'umi031')
    Unknown7010(39, 'umi032')
    Unknown7010(42, 'umi033')
    Unknown7010(43, 'umi034')
    Unknown7010(44, 'umi035')
    Unknown7010(45, 'umi036')
    Unknown7010(46, 'umi037')
    Unknown7010(47, 'umi038')
    Unknown7010(48, 'umi039')
    Unknown7010(49, 'umi040')
    Unknown7010(50, 'umi041')
    Unknown7010(52, 'umi042')
    Unknown7010(53, 'umi043')
    Unknown7010(54, 'umi100_0')
    Unknown7010(55, 'umi100_1')
    Unknown7010(56, 'umi100_2')
    Unknown7010(63, 'umi101_0')
    Unknown7010(64, 'umi101_1')
    Unknown7010(65, 'umi101_2')
    Unknown7010(57, 'umi102_0')
    Unknown7010(58, 'umi102_1')
    Unknown7010(59, 'umi102_2')
    Unknown7010(66, 'umi103_0')
    Unknown7010(67, 'umi103_1')
    Unknown7010(68, 'umi103_2')
    Unknown7010(60, 'umi104_0')
    Unknown7010(61, 'umi104_1')
    Unknown7010(62, 'umi104_2')
    Unknown7010(69, 'umi105_0')
    Unknown7010(70, 'umi105_1')
    Unknown7010(71, 'umi105_2')
    Unknown7010(72, 'umi150')
    Unknown7010(73, 'umi151')
    Unknown7010(74, 'umi152')
    Unknown7010(85, 'umi153')
    Unknown7010(87, 'umi154')
    Unknown7010(88, 'umi155')
    Unknown7010(96, 'umi161_0')
    Unknown7010(97, 'umi161_1')
    Unknown7010(92, 'umi162_0')
    Unknown7010(93, 'umi162_1')
    Unknown7010(98, 'umi163_0')
    Unknown7010(99, 'umi163_1')
    Unknown7010(100, 'umi164_0')
    Unknown7010(101, 'umi164_1')
    Unknown7010(105, 'umi165_0')
    Unknown7010(106, 'umi165_1')
    Unknown7010(102, 'umi166_0')
    Unknown7010(103, 'umi166_1')
    Unknown7010(90, 'umi167_0')
    Unknown7010(91, 'umi167_1')
    Unknown7010(107, 'umi168_0')
    Unknown7010(108, 'umi168_1')
    Unknown7010(110, 'umi169_0')
    Unknown7010(111, 'umi169_1')
    Unknown7010(94, 'umi400_0')
    Unknown7010(95, 'umi400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c744f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174655468726f7700000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174655468726f774f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def ChainRoot():
    HitJumpCancel(1)
    HitOrBlockCancel('NmlAtk5A')
    HitOrBlockCancel('NmlAtk2A')
    HitOrBlockCancel('NmlAtk5B')
    HitOrBlockCancel('NmlAtk2B')
    HitOrBlockCancel('NmlAtk2C')
    HitOrBlockCancel('CmnActCrushAttack')

@Subroutine
def OnLanding():
    SLOT_31 = 999
    SLOT_5 = 0

@Subroutine
def OnDamage():
    SLOT_31 = 999
    SLOT_5 = 0

@State
def CmnActStand():
    if SLOT_4:
        gotoLabel(1)
    sprite('Action_000_00', 1)	# 1-1	 **attackbox here**
    label(0)
    sprite('Action_000_00', 5)	# 2-6	 **attackbox here**
    sprite('Action_000_01', 5)	# 7-11	 **attackbox here**
    sprite('Action_000_02', 5)	# 12-16	 **attackbox here**
    sprite('Action_000_03', 5)	# 17-21	 **attackbox here**
    sprite('Action_000_04', 5)	# 22-26	 **attackbox here**
    sprite('Action_000_05', 5)	# 27-31	 **attackbox here**
    sprite('Action_000_06', 5)	# 32-36	 **attackbox here**
    sprite('Action_000_07', 5)	# 37-41	 **attackbox here**
    sprite('Action_000_08', 5)	# 42-46	 **attackbox here**
    sprite('Action_000_09', 5)	# 47-51	 **attackbox here**
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('Action_000_00', 1)	# 52-52	 **attackbox here**
    SLOT_88 = 960
    SFX_1('umi000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_000_11', 5)	# 53-57
    SLOT_4 = 0
    sprite('Action_000_12', 5)	# 58-62
    sprite('Action_000_13', 6)	# 63-68
    sprite('Action_000_14', 5)	# 69-73
    sprite('Action_000_15', 4)	# 74-77
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 3)	# 1-3
    sprite('Action_015_01', 3)	# 4-6

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 2)	# 1-2
    sprite('Action_012_01', 2)	# 3-4
    sprite('Action_012_02', 2)	# 5-6
    sprite('Action_012_03', 2)	# 7-8

@State
def CmnActCrouch():
    label(0)
    sprite('Action_013_00', 5)	# 1-5
    SLOT_4 = 1
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
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('Action_016_00', 3)	# 1-3
    sprite('Action_016_01', 3)	# 4-6

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 6)	# 1-6
    sprite('Action_014_01', 6)	# 7-12

@State
def CmnActJumpPre():
    sprite('Action_036_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_01', 4)	# 1-4
    sprite('Action_036_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_01', 4)	# 9-12
    sprite('Action_035_01', 4)	# 13-16
    gotoLabel(1)
    label(2)
    sprite('Action_037_01', 4)	# 17-20
    sprite('Action_037_01', 4)	# 21-24
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
    sprite('Action_036_04', 2)	# 7-8
    sprite('Action_036_05', 2)	# 9-10
    ExitState()
    label(1)
    sprite('Action_035_02', 3)	# 11-13
    sprite('Action_035_03', 3)	# 14-16
    sprite('Action_035_04', 2)	# 17-18
    sprite('Action_035_05', 2)	# 19-20
    ExitState()
    label(2)
    sprite('Action_037_02', 3)	# 21-23
    sprite('Action_037_03', 3)	# 24-26
    sprite('Action_037_04', 2)	# 27-28
    sprite('Action_037_05', 2)	# 29-30
    ExitState()

@State
def CmnActJumpDown():
    label(0)
    sprite('Action_020_00', 3)	# 1-3
    sprite('Action_020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('Action_021_00', 3)	# 1-3
    sprite('Action_021_01', 4)	# 4-7
    sprite('Action_021_02', 4)	# 8-11

@State
def CmnActLandingStiffLoop():
    sprite('Action_021_00', 2)	# 1-2
    sprite('Action_021_00', 2)	# 3-4
    sprite('Action_021_01', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('Action_021_02', 6)	# 1-6

@State
def CmnActFWalk():
    sprite('Action_010_00', 2)	# 1-2
    label(0)
    sprite('Action_010_01', 3)	# 3-5
    sprite('Action_010_02', 5)	# 6-10
    sprite('Action_010_03', 5)	# 11-15
    sprite('Action_010_04', 5)	# 16-20
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_05', 5)	# 21-25
    sprite('Action_010_06', 5)	# 26-30
    sprite('Action_010_07', 5)	# 31-35
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_08', 5)	# 36-40
    sprite('Action_010_09', 5)	# 41-45
    sprite('Action_010_10', 5)	# 46-50
    sprite('Action_010_11', 5)	# 51-55
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('Action_011_00', 2)	# 1-2
    label(0)
    sprite('Action_011_01', 3)	# 3-5
    sprite('Action_011_02', 6)	# 6-11
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_03', 6)	# 12-17
    sprite('Action_011_04', 6)	# 18-23
    sprite('Action_011_05', 6)	# 24-29
    sprite('Action_011_06', 6)	# 30-35
    sprite('Action_011_07', 6)	# 36-41
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_08', 6)	# 42-47
    sprite('Action_011_09', 6)	# 48-53
    sprite('Action_011_10', 6)	# 54-59
    sprite('Action_011_11', 6)	# 60-65
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_045_00', 3)	# 1-3
    sprite('Action_045_01', 3)	# 4-6
    label(0)
    sprite('Action_045_02', 3)	# 7-9
    Unknown8006(100, 1, 1)
    sprite('Action_045_03', 3)	# 10-12
    sprite('Action_045_04', 3)	# 13-15
    sprite('Action_045_05', 3)	# 16-18
    sprite('Action_045_06', 3)	# 19-21
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 22-24
    sprite('Action_045_08', 3)	# 25-27
    sprite('Action_045_09', 3)	# 28-30
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_10', 4)	# 1-4
    sprite('Action_045_11', 4)	# 5-8
    sprite('Action_045_12', 4)	# 9-12

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
    sprite('Action_046_00', 1)	# 1-1
    sprite('Action_046_01', 2)	# 2-3
    physicsXImpulse(-40000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('Action_046_02', 2)	# 4-5
    sprite('Action_046_02', 1)	# 6-6
    sprite('Action_046_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('Action_046_03', 3)	# 10-12
    sprite('Action_046_04', 3)	# 13-15
    sprite('Action_046_05', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_06', 1)	# 19-19
    physicsXImpulse(0)
    clearUponHandler(3)
    sprite('Action_046_07', 2)	# 20-21
    Unknown8000(100, 1, 1)
    sprite('Action_046_08', 3)	# 22-24

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
    sprite('Action_046_03', 4)	# 9-12
    sprite('Action_046_04', 4)	# 13-16
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
    sprite('Action_351_01', 3)	# 1-3
    sprite('Action_351_02', 3)	# 4-6
    sprite('Action_351_03', 3)	# 7-9
    sprite('Action_351_04', 3)	# 10-12
    sprite('Action_351_05', 3)	# 13-15

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
    sprite('Action_326_00', 3)	# 1-3	 **attackbox here**

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
    sprite('Action_354_04', 3)	# 1-3

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
    sprite('Action_330_07', 3)	# 4-6
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
    sprite('Action_340_03', 3)	# 1-3	 **attackbox here**
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
    sprite('Action_041_00', 3)	# 1-3
    sprite('Action_041_01', 3)	# 4-6
    sprite('Action_041_02', 4)	# 7-10
    sprite('Action_041_03', 4)	# 11-14
    sprite('Action_041_04', 4)	# 15-18

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_05', 3)	# 1-3
    sprite('Action_041_06', 3)	# 4-6
    sprite('Action_041_07', 3)	# 7-9
    sprite('Action_041_08', 3)	# 10-12
    sprite('Action_041_09', 3)	# 13-15

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
    sprite('Action_018_06', 6)	# 6-11
    sprite('Action_018_07', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('Action_019_00', 2)	# 1-2
    sprite('Action_019_01', 2)	# 3-4
    sprite('Action_019_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_019_06', 6)	# 6-11
    sprite('Action_019_07', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('Action_036_01', 9)	# 1-9

@State
def CmnActLockWait():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActLockReject():
    sprite('Action_001_00', 3)	# 1-3
    sprite('Action_001_01', 3)	# 4-6
    sprite('Action_001_02', 2)	# 7-8	 **attackbox here**
    sprite('Action_001_03', 6)	# 9-14
    sprite('Action_001_04', 5)	# 15-19
    sprite('Action_001_05', 4)	# 20-23
    sprite('Action_001_06', 4)	# 24-27

@State
def CmnActAirLockWait():
    sprite('Action_019_02', 1)	# 1-1
    sprite('Action_019_03', 3)	# 2-4
    sprite('Action_019_00', 3)	# 5-7

@State
def CmnActLandSpin():
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6
    sprite('Action_333_03', 2)	# 7-8
    sprite('Action_333_04', 2)	# 9-10
    sprite('Action_333_05', 2)	# 11-12
    sprite('Action_333_06', 2)	# 13-14
    loopRest()

@State
def CmnActLandSpinDown():
    sprite('Action_333_00', 2)	# 1-2
    sprite('Action_333_01', 2)	# 3-4
    sprite('Action_333_02', 2)	# 5-6

@State
def CmnActVertSpin():
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
def CmnActSlideAir():
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
    sprite('Action_351_00', 1)	# 1-1
    label(0)
    sprite('Action_351_00', 3)	# 2-4
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
    sprite('Action_020_00', 3)	# 13-15
    sprite('Action_020_01', 3)	# 16-18
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
    sprite('Action_020_00', 3)	# 13-15
    sprite('Action_020_01', 3)	# 16-18
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

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(20000)
        PushbackX(12000)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_2nd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown28(8, 'CmnActCrouch')
    sprite('Action_004_00', 2)	# 1-2
    sprite('Action_004_01', 2)	# 3-4
    sprite('Action_004_02', 1)	# 5-5
    SFX_0('003_swing_grap_0_0')
    GFX_0('EffNmlAtk5A', -1)
    sprite('Action_004_03', 4)	# 6-9	 **attackbox here**
    Unknown7009(0)
    sprite('Action_004_04', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('Action_004_05', 5)	# 14-18
    sprite('Action_004_06', 4)	# 19-22
    SLOT_4 = 1

@State
def AN_NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(20000)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_3rd')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_006_00', 3)	# 1-3
    sprite('Action_006_01', 4)	# 4-7
    physicsXImpulse(20000)
    Unknown8007(100, 1, 1)
    sprite('Action_006_02', 2)	# 8-9
    SFX_0('005_swing_grap_2_0')
    GFX_0('EffNmlAtk5AA', -1)
    sprite('Action_006_03', 3)	# 10-12	 **attackbox here**
    Unknown7009(0)
    Unknown1019(0)
    Unknown8010(100, 1, 1)
    sprite('Action_006_04', 2)	# 13-14
    Recovery()
    Unknown2063()
    sprite('Action_006_05', 6)	# 15-20
    sprite('Action_006_06', 4)	# 21-24
    sprite('Action_006_07', 3)	# 25-27
    sprite('Action_006_08', 3)	# 28-30
    SLOT_4 = 1

@State
def AN_NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(7500)
        AirPushbackY(-30000)
        PushbackX(19800)
        Unknown9154(21)
        Unknown9310(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5A_4th')
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 3)	# 3-5
    sprite('Action_003_02', 3)	# 6-8
    sprite('Action_003_03', 2)	# 9-10
    sprite('Action_003_04', 2)	# 11-12
    sprite('Action_003_05', 4)	# 13-16	 **attackbox here**
    GFX_0('EffNmlAtk5AAA', -1)
    Unknown7009(1)
    SFX_0('024_getset_a')
    sprite('Action_003_06', 13)	# 17-29
    Recovery()
    Unknown2063()
    sprite('Action_003_07', 7)	# 30-36
    sprite('Action_003_08', 6)	# 37-42
    SLOT_4 = 1

@State
def AN_NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2500)
        AirHitstunAnimation(18)
        GroundedHitstunAnimation(18)
        AirPushbackX(40000)
        AirPushbackY(5000)
        AirUntechableTime(35)
        Unknown9202(10)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
        sendToLabelUpon(10, 10)
        sendToLabelUpon(2, 0)
        JumpCancel_(0)
    sprite('Action_403_00', 3)	# 1-3
    sprite('Action_403_01', 3)	# 4-6
    SFX_4('umi109_0')
    physicsYImpulse(17000)
    physicsXImpulse(22000)
    setGravity(1600)
    sprite('Action_403_02', 3)	# 7-9
    sprite('Action_403_03', 2)	# 10-11
    sprite('Action_403_04', 4)	# 12-15
    sprite('Action_403_05', 3)	# 16-18
    GFX_0('EffNmlAtk5BBB', -1)
    SFX_0('016_explode_0')
    physicsXImpulse(50000)
    sprite('Action_403_06', 32767)	# 19-32785	 **attackbox here**
    label(0)
    sprite('Action_403_07', 2)	# 32786-32787
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('Action_403_08', 4)	# 32788-32791
    sprite('Action_403_09', 10)	# 32792-32801
    clearUponHandler(2)
    SFX_0('209_down_normal_0')
    sprite('Action_403_10', 6)	# 32802-32807
    sprite('Action_403_11', 4)	# 32808-32811
    sprite('Action_403_12', 4)	# 32812-32815
    sprite('Action_403_13', 4)	# 32816-32819
    sprite('Action_403_14', 4)	# 32820-32823
    ExitState()
    label(10)
    sprite('Action_403_16', 2)	# 32824-32825
    clearUponHandler(11)
    clearUponHandler(2)
    sendToLabelUpon(2, 12)
    physicsYImpulse(20000)
    physicsXImpulse(-7000)
    Recovery()
    sprite('Action_403_17', 4)	# 32826-32829
    sprite('Action_403_18', 4)	# 32830-32833
    sprite('Action_403_19', 4)	# 32834-32837
    sprite('Action_403_20', 5)	# 32838-32842
    sprite('Action_403_21', 4)	# 32843-32846
    label(11)
    sprite('Action_403_22', 3)	# 32847-32849
    sprite('Action_403_23', 3)	# 32850-32852
    loopRest()
    gotoLabel(11)
    label(12)
    sprite('Action_403_24', 3)	# 32853-32855
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_403_25', 3)	# 32856-32858
    sprite('Action_403_26', 2)	# 32859-32860

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackX(10000)
        AirPushbackY(17000)
        Unknown1112('')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5B_2nd')

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
    sprite('Action_002_00', 3)	# 1-3
    sprite('Action_002_01', 3)	# 4-6
    sprite('Action_002_02', 2)	# 7-8	 **attackbox here**
    StartMultihit()
    GFX_0('EffNmlAtk5B', -1)
    physicsXImpulse(30000)
    Unknown1028(-3000)
    Unknown7009(1)
    SFX_0('005_swing_grap_2_0')
    Unknown8007(100, 1, 1)
    sprite('Action_002_02', 3)	# 9-11	 **attackbox here**
    Unknown14070('AN_NmlAtk5B_2ndShot')
    sprite('Action_002_03', 3)	# 12-14	 **attackbox here**
    Unknown1019(50)
    Unknown8010(100, 1, 1)
    sprite('Action_002_04', 4)	# 15-18
    Unknown1084(1)
    Recovery()
    Unknown2063()
    if (not SLOT_2):
        Unknown14072('AN_NmlAtk5B_2ndShot')
    sprite('Action_002_05', 4)	# 19-22
    Unknown14074('AN_NmlAtk5B_2ndShot')
    sprite('Action_002_06', 4)	# 23-26
    sprite('Action_002_07', 4)	# 27-30

@State
def AN_NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(13)
        AirPushbackX(20000)
        AirPushbackY(20000)
        PushbackX(12000)
        AirUntechableTime(30)
        Unknown11033(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('AN_NmlAtk5B_3rd')

        def upon_STATE_END():
            Unknown1051(0)
    sprite('Action_130_00', 2)	# 1-2
    Unknown8010(100, 1, 1)
    sprite('Action_130_01', 1)	# 3-3
    sprite('Action_130_01', 5)	# 4-8
    GFX_0('EffNmlAtk5BB_01', 0)
    sprite('Action_130_02', 2)	# 9-10
    SFX_0('016_explode_0')
    sprite('Action_130_03', 3)	# 11-13	 **attackbox here**
    GFX_0('EffNmlAtk5BB_02', -1)
    Unknown7009(1)
    Unknown1045(-20000)
    sprite('Action_130_04', 3)	# 14-16	 **attackbox here**
    sprite('Action_130_05', 4)	# 17-20
    Unknown1084(1)
    Recovery()
    Unknown2063()
    sprite('Action_130_06', 4)	# 21-24
    sprite('Action_130_07', 4)	# 25-28
    sprite('Action_130_08', 4)	# 29-32
    sprite('Action_130_09', 4)	# 33-36
    sprite('Action_130_10', 4)	# 37-40

@State
def AN_NmlAtk5B_2ndShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(65000)
        AirPushbackY(30000)
        WallbounceReboundTime(35)
        PushbackX(39800)
        Hitstop(8)
        AirUntechableTime(80)
        Unknown11033(1)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(3000, 3000)
    sprite('Action_130_00', 2)	# 1-2
    Unknown8010(100, 1, 1)
    sprite('Action_130_01', 1)	# 3-3
    sprite('Action_130_01', 12)	# 4-15
    GFX_0('EffNmlAtk5BB_03', 0)
    sprite('Action_130_02', 6)	# 16-21
    SFX_0('016_explode_0')
    sprite('Action_130_03', 2)	# 22-23	 **attackbox here**
    GFX_0('EffNmlAtk5BB_02', -1)
    Unknown7009(1)
    physicsXImpulse(-25000)
    Unknown1028(2500)
    sprite('Action_130_04', 2)	# 24-25	 **attackbox here**
    sprite('Action_130_05', 5)	# 26-30
    sprite('Action_130_06', 5)	# 31-35
    Unknown1084(1)
    sprite('Action_130_07', 5)	# 36-40
    sprite('Action_130_08', 5)	# 41-45
    sprite('Action_130_09', 4)	# 46-49
    sprite('Action_130_10', 4)	# 50-53

@State
def AN_NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP2(75)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(22000)
        AirUntechableTime(32)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown1084(1)
        sendToLabelUpon(2, 0)
        callSubroutine('ChainRoot')
    sprite('Action_140_00', 2)	# 1-2
    sprite('Action_140_01', 3)	# 3-5
    sprite('Action_140_02', 4)	# 6-9
    GFX_0('EffNmlAtk5AAAA', -1)
    Unknown8001(0, 100)
    physicsXImpulse(32000)
    physicsYImpulse(15000)
    setGravity(2000)
    SFX_0('005_swing_grap_2_0')
    sprite('Action_140_03', 3)	# 10-12
    sprite('Action_140_04', 32767)	# 13-32779	 **attackbox here**
    tag_voice(1, 'umi109_1', 'umi109_2', '', '')
    label(0)
    sprite('Action_140_05', 2)	# 32780-32781	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    SFX_0('209_down_normal_0')
    sprite('Action_140_06', 2)	# 32782-32783
    Recovery()
    Unknown2063()
    sprite('Action_140_07', 10)	# 32784-32793
    sprite('Action_140_08', 4)	# 32794-32797
    sprite('Action_140_09', 4)	# 32798-32801
    SLOT_4 = 1

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        callSubroutine('ChainRoot')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_005_00', 3)	# 1-3
    sprite('Action_005_01', 3)	# 4-6
    Unknown7009(0)
    physicsXImpulse(10000)
    Unknown8007(100, 1, 1)
    SFX_0('005_swing_grap_2_0')
    sprite('Action_005_02', 5)	# 7-11	 **attackbox here**
    sprite('Action_005_03', 3)	# 12-14
    Unknown1019(60)
    Recovery()
    Unknown2063()
    sprite('Action_005_04', 5)	# 15-19
    Unknown1019(60)
    sprite('Action_005_05', 4)	# 20-23
    Unknown1019(0)
    sprite('Action_005_06', 3)	# 24-26
    SLOT_4 = 1

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirUntechableTime(24)
        AirHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('ChainRoot')
    sprite('Action_137_00', 3)	# 1-3
    sprite('Action_137_01', 4)	# 4-7
    sprite('Action_137_02', 3)	# 8-10
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    SFX_0('004_swing_grap_1_2')
    sprite('Action_137_03', 4)	# 11-14	 **attackbox here**
    GFX_0('EffNmlAtk2B', -1)
    tag_voice(1, 'umi106_0', 'umi106_1', 'umi106_2', '')
    sprite('Action_137_04', 8)	# 15-22
    Recovery()
    Unknown2063()
    setInvincible(0)
    sprite('Action_137_05', 6)	# 23-28
    sprite('Action_137_06', 4)	# 29-32
    sprite('Action_137_07', 4)	# 33-36
    SLOT_4 = 1

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
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
    sprite('Action_402_00', 4)	# 1-4
    sprite('Action_402_01', 5)	# 5-9
    physicsXImpulse(20000)
    sprite('Action_402_02', 5)	# 10-14
    Unknown1019(200)
    sprite('Action_402_04', 2)	# 15-16	 **attackbox here**
    GFX_0('EffNmlAtk2C', -1)
    tag_voice(1, 'umi107_1', '', '', '')
    Unknown8006(100, 1, 1)
    SFX_0('209_down_normal_0')
    Unknown1019(50)
    sprite('Action_402_05', 2)	# 17-18	 **attackbox here**
    Unknown1019(80)
    sprite('Action_402_06', 3)	# 19-21	 **attackbox here**
    Unknown1019(80)
    sprite('Action_402_07', 3)	# 22-24	 **attackbox here**
    Unknown1019(80)
    sprite('Action_402_08', 3)	# 25-27
    Recovery()
    Unknown2063()
    Unknown1019(80)
    sprite('Action_402_09', 4)	# 28-31
    Unknown1084(1)
    sprite('Action_402_10', 3)	# 32-34
    sprite('Action_402_11', 5)	# 35-39
    sprite('Action_402_12', 3)	# 40-42
    SLOT_4 = 1

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
    sprite('Action_007_00', 4)	# 1-4
    sprite('Action_007_01', 2)	# 5-6
    GFX_0('EffNmlAtkJA', -1)
    sprite('Action_007_02', 3)	# 7-9	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    Unknown7009(3)
    sprite('Action_007_03', 6)	# 10-15
    Recovery()
    Unknown2063()
    sprite('Action_007_04', 4)	# 16-19
    sprite('Action_007_05', 4)	# 20-23
    sprite('Action_007_06', 3)	# 24-26
    sprite('Action_007_07', 3)	# 27-29
    sprite('Action_007_08', 3)	# 30-32

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(500)
        Unknown11092(1)
        AirPushbackY(10000)
        Hitstop(3)
        HitOverhead(0)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_135_00', 2)	# 1-2
    sprite('Action_135_01', 2)	# 3-4
    GFX_0('EffNmlAtkJAA_01', -1)
    sprite('Action_135_02', 2)	# 5-6	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    tag_voice(1, 'umi107_2', '', '', '')
    sprite('Action_135_03', 2)	# 7-8
    sprite('Action_135_04', 2)	# 9-10
    GFX_0('EffNmlAtkJA', -1)
    sprite('Action_135_05', 2)	# 11-12	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    RefreshMultihit()
    sprite('Action_135_06', 2)	# 13-14
    GFX_0('EffNmlAtkJAA_01', -1)
    sprite('Action_135_07', 2)	# 15-16	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    RefreshMultihit()
    sprite('Action_135_08', 2)	# 17-18
    sprite('Action_135_09', 2)	# 19-20
    GFX_0('EffNmlAtkJA', -1)
    sprite('Action_135_10', 3)	# 21-23	 **attackbox here**
    Hitstop(11)
    AirPushbackY(20000)
    GFX_0('EffNmlAtkJAA_02', -1)
    SFX_0('004_swing_grap_1_0')
    RefreshMultihit()
    sprite('Action_135_11', 6)	# 24-29
    Recovery()
    Unknown2063()
    sprite('Action_135_12', 5)	# 30-34
    sprite('Action_135_13', 4)	# 35-38
    sprite('Action_135_14', 3)	# 39-41
    sprite('Action_135_15', 3)	# 42-44
    sprite('Action_135_16', 3)	# 45-47

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_009_00', 2)	# 1-2
    sprite('Action_009_01', 3)	# 3-5
    sprite('Action_009_02', 2)	# 6-7
    sprite('Action_009_03', 6)	# 8-13
    Unknown7009(4)
    sprite('Action_009_05', 6)	# 14-19	 **attackbox here**
    GFX_0('EffNmlAtkJB', -1)
    SFX_0('004_swing_grap_1_2')
    sprite('Action_009_07', 8)	# 20-27
    Recovery()
    Unknown2063()
    sprite('Action_009_08', 4)	# 28-31
    sprite('Action_009_09', 4)	# 32-35
    sprite('Action_009_10', 4)	# 36-39
    sprite('Action_009_11', 3)	# 40-42
    sprite('Action_009_12', 3)	# 43-45
    sprite('Action_009_13', 3)	# 46-48

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(36000)
        AirPushbackY(-48000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        JumpCancel_(0)
    sprite('Action_148_00', 3)	# 1-3
    physicsYImpulse(15000)
    sprite('Action_148_01', 3)	# 4-6
    sprite('Action_148_02', 3)	# 7-9
    sprite('Action_148_03', 3)	# 10-12
    sprite('Action_148_06', 2)	# 13-14
    sprite('Action_148_07', 1)	# 15-15	 **attackbox here**
    GFX_0('EffNmlAtkJC_01', -1)
    GFX_0('EffNmlAtkJC_02', -1)
    GFX_0('EffNmlAtkJC_03', -1)
    SFX_0('004_swing_grap_1_2')
    tag_voice(1, 'umi110_0', 'umi110_1', 'umi110_2', '')
    sprite('Action_148_07', 2)	# 16-17	 **attackbox here**
    physicsXImpulse(30000)
    physicsYImpulse(-40000)
    Unknown1028(1200)
    setGravity(1600)
    label(0)
    sprite('Action_148_08', 3)	# 18-20	 **attackbox here**
    sprite('Action_148_09', 3)	# 21-23	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_148_11', 4)	# 24-27
    GFX_0('EffGroundBreak01', 0)
    Unknown1084(1)
    ScreenShake(0, 15000)
    SFX_0('209_down_normal_0')
    sprite('Action_148_12', 10)	# 28-37
    Recovery()
    Unknown2063()
    sprite('Action_149_00', 4)	# 38-41
    physicsXImpulse(-10000)
    physicsYImpulse(15000)
    Unknown1043()
    sendToLabelUpon(2, 11)
    sprite('Action_149_01', 4)	# 42-45
    sprite('Action_149_02', 4)	# 46-49
    sprite('Action_149_03', 4)	# 50-53
    sprite('Action_149_04', 4)	# 54-57
    label(10)
    sprite('Action_149_05', 3)	# 58-60
    sprite('Action_149_06', 3)	# 61-63
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('Action_149_07', 3)	# 64-66
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_149_08', 4)	# 67-70
    sprite('Action_149_09', 4)	# 71-74

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
    tag_voice(1, 'umi156_0', 'umi156_1', '', '')
    sprite('Action_068_03', 3)	# 8-10
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 2)	# 14-15
    sprite('Action_009_00', 2)	# 16-17
    sprite('Action_009_01', 3)	# 18-20
    sprite('Action_009_02', 2)	# 21-22
    sprite('Action_009_03', 3)	# 23-25
    sprite('Action_009_05', 3)	# 26-28	 **attackbox here**
    GFX_0('EffNmlAtkJB', -1)
    SFX_0('004_swing_grap_1_2')
    sprite('Action_009_07', 8)	# 29-36
    sprite('Action_009_08', 4)	# 37-40
    sprite('Action_009_09', 4)	# 41-44
    sprite('Action_009_10', 4)	# 45-48
    sprite('Action_009_11', 3)	# 49-51
    sprite('Action_009_12', 3)	# 52-54
    sprite('Action_009_13', 3)	# 55-57
    label(0)
    sprite('Action_068_10', 3)	# 58-60
    sprite('Action_068_11', 3)	# 61-63
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 2)	# 64-65
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_021_01', 6)	# 66-71
    sprite('Action_021_01', 2)	# 72-73
    Unknown18009(0)
    sprite('Action_021_02', 3)	# 74-76

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 16)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_009_07', 8)	# 1-8
    sprite('Action_009_08', 4)	# 9-12
    sprite('Action_009_09', 4)	# 13-16
    sprite('Action_009_10', 4)	# 17-20
    sprite('Action_009_11', 3)	# 21-23
    sprite('Action_009_12', 3)	# 24-26
    sprite('Action_009_13', 3)	# 27-29
    label(1)
    sprite('Action_021_00', 1)	# 30-30
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_021_01', 2)	# 31-32
    sprite('Action_021_01', 2)	# 33-34
    sprite('Action_021_02', 1)	# 35-35
    label(2)
    sprite('Action_003_00', 2)	# 36-37
    clearUponHandler(17)
    teleportRelativeY(0)
    sprite('Action_003_01', 2)	# 38-39
    sprite('Action_003_02', 2)	# 40-41
    SFX_0('005_swing_grap_2_0')
    sprite('Action_003_03', 5)	# 42-46
    RefreshMultihit()
    sprite('Action_003_04', 2)	# 47-48
    sprite('Action_003_05', 4)	# 49-52	 **attackbox here**
    GFX_0('EffNmlAtk5AAA', -1)
    tag_voice(0, 'umi157_0', 'umi157_1', '', '')
    sprite('Action_003_06', 13)	# 53-65
    sprite('Action_003_07', 5)	# 66-70
    sprite('Action_003_08', 5)	# 71-75
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    label(10)
    sprite('Action_000_00', 5)	# 76-80	 **attackbox here**
    sprite('Action_000_01', 5)	# 81-85	 **attackbox here**
    sprite('Action_000_02', 5)	# 86-90	 **attackbox here**
    sprite('Action_000_03', 5)	# 91-95	 **attackbox here**
    sprite('Action_000_04', 5)	# 96-100	 **attackbox here**
    sprite('Action_000_05', 5)	# 101-105	 **attackbox here**
    sprite('Action_000_06', 5)	# 106-110	 **attackbox here**
    sprite('Action_000_07', 5)	# 111-115	 **attackbox here**
    sprite('Action_000_08', 5)	# 116-120	 **attackbox here**
    sprite('Action_000_09', 5)	# 121-125	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 126-126

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_137_00', 5)	# 1-5
    sprite('Action_137_01', 5)	# 6-10
    sprite('Action_137_02', 4)	# 11-14
    SFX_0('004_swing_grap_1_2')
    sprite('Action_137_03', 2)	# 15-16	 **attackbox here**
    GFX_0('EffNmlAtk2B', -1)
    sprite('Action_137_04', 8)	# 17-24
    sprite('Action_137_05', 6)	# 25-30
    sprite('Action_137_06', 4)	# 31-34
    sprite('Action_137_07', 4)	# 35-38
    label(0)
    sprite('Action_000_00', 5)	# 39-43	 **attackbox here**
    sprite('Action_000_01', 5)	# 44-48	 **attackbox here**
    sprite('Action_000_02', 5)	# 49-53	 **attackbox here**
    sprite('Action_000_03', 5)	# 54-58	 **attackbox here**
    sprite('Action_000_04', 5)	# 59-63	 **attackbox here**
    sprite('Action_000_05', 5)	# 64-68	 **attackbox here**
    sprite('Action_000_06', 5)	# 69-73	 **attackbox here**
    sprite('Action_000_07', 5)	# 74-78	 **attackbox here**
    sprite('Action_000_08', 5)	# 79-83	 **attackbox here**
    sprite('Action_000_09', 5)	# 84-88	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 89-89

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('Action_130_00', 2)	# 1-2
    sprite('Action_130_01', 11)	# 3-13
    GFX_0('EffNmlAtk5BB_03', 0)
    sprite('Action_130_02', 6)	# 14-19
    sprite('Action_130_03', 2)	# 20-21	 **attackbox here**
    GFX_0('EffNmlAtk5BB_02', -1)
    tag_voice(0, 'umi158_0', 'umi158_1', '', '')
    SFX_0('016_explode_0')
    sprite('Action_130_04', 2)	# 22-23	 **attackbox here**
    sprite('Action_130_05', 5)	# 24-28
    sprite('Action_130_06', 5)	# 29-33
    sprite('Action_130_07', 5)	# 34-38
    sprite('Action_130_08', 5)	# 39-43
    sprite('Action_130_07', 5)	# 44-48
    sprite('Action_130_08', 5)	# 49-53
    sprite('Action_130_09', 4)	# 54-57
    sprite('Action_130_10', 4)	# 58-61

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 23)	# 1-23
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 24-24
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    physicsYImpulse(-4000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('Action_140_00', 2)	# 25-26
    sprite('Action_140_01', 3)	# 27-29
    Unknown8001(0, 100)
    physicsXImpulse(32000)
    physicsYImpulse(20000)
    setGravity(3500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('Action_140_02', 4)	# 30-33
    GFX_0('EffNmlAtk5AAAA', -1)
    SFX_0('005_swing_grap_2_0')
    sprite('Action_140_03', 3)	# 34-36
    sprite('Action_140_04', 5)	# 37-41	 **attackbox here**
    StartMultihit()
    label(1)
    sprite('Action_140_05', 2)	# 42-43	 **attackbox here**
    SFX_0('209_down_normal_0')
    Unknown1019(0)
    sprite('Action_140_06', 2)	# 44-45
    Unknown8000(100, 1, 1)
    sprite('Action_140_07', 7)	# 46-52
    sprite('Action_140_08', 3)	# 53-55
    sprite('Action_140_09', 3)	# 56-58
    sprite('Action_000_00', 5)	# 59-63	 **attackbox here**
    sprite('Action_000_01', 5)	# 64-68	 **attackbox here**
    sprite('Action_000_02', 5)	# 69-73	 **attackbox here**
    sprite('Action_000_03', 5)	# 74-78	 **attackbox here**
    sprite('Action_000_04', 5)	# 79-83	 **attackbox here**
    sprite('Action_000_05', 5)	# 84-88	 **attackbox here**
    sprite('Action_000_06', 5)	# 89-93	 **attackbox here**
    sprite('Action_000_07', 5)	# 94-98	 **attackbox here**
    sprite('Action_000_08', 5)	# 99-103	 **attackbox here**
    sprite('Action_000_09', 5)	# 104-108	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('Action_006_00', 5)	# 1-5
    sprite('Action_006_01', 4)	# 6-9
    sprite('Action_006_02', 2)	# 10-11
    GFX_0('EffNmlAtk5AA', -1)
    SFX_0('005_swing_grap_2_0')
    sprite('Action_006_03', 3)	# 12-14	 **attackbox here**
    sprite('Action_006_04', 2)	# 15-16
    sprite('Action_006_05', 6)	# 17-22
    sprite('Action_006_06', 4)	# 23-26
    sprite('Action_006_07', 4)	# 27-30
    sprite('Action_006_08', 4)	# 31-34
    sprite('Action_000_00', 5)	# 35-39	 **attackbox here**
    sprite('Action_000_01', 5)	# 40-44	 **attackbox here**
    sprite('Action_000_02', 5)	# 45-49	 **attackbox here**
    sprite('Action_000_03', 5)	# 50-54	 **attackbox here**
    sprite('Action_000_04', 5)	# 55-59	 **attackbox here**
    sprite('Action_000_05', 5)	# 60-64	 **attackbox here**
    sprite('Action_000_06', 5)	# 65-69	 **attackbox here**
    sprite('Action_000_07', 5)	# 70-74	 **attackbox here**
    sprite('Action_000_08', 5)	# 75-79	 **attackbox here**
    sprite('Action_000_09', 5)	# 80-84	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('Action_130_00', 2)	# 1-2
    sprite('Action_130_01', 11)	# 3-13
    GFX_0('EffNmlAtk5BB_03', 0)
    sprite('Action_130_02', 6)	# 14-19
    sprite('Action_130_03', 2)	# 20-21	 **attackbox here**
    GFX_0('EffNmlAtk5BB_02', -1)
    SFX_0('016_explode_0')
    sprite('Action_130_04', 2)	# 22-23	 **attackbox here**
    sprite('Action_130_05', 5)	# 24-28
    sprite('Action_130_06', 5)	# 29-33
    sprite('Action_130_07', 5)	# 34-38
    sprite('Action_130_08', 5)	# 39-43
    sprite('Action_130_07', 5)	# 44-48
    sprite('Action_130_08', 5)	# 49-53
    sprite('Action_130_09', 4)	# 54-57
    sprite('Action_130_10', 4)	# 58-61

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
                Unknown1015(1000)
                if (SLOT_12 >= 32000):
                    SLOT_12 = 32000
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
    sprite('Action_045_04', 3)	# 16-18
    sprite('Action_045_05', 3)	# 19-21
    sprite('Action_045_06', 3)	# 22-24
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 25-27
    sprite('Action_045_08', 3)	# 28-30
    sprite('Action_045_09', 3)	# 31-33
    sprite('Action_045_02', 3)	# 34-36
    Unknown8006(100, 1, 1)
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
    Unknown23027()
    sprite('Action_055_02', 2)	# 45-46
    sprite('Action_055_03', 3)	# 47-49
    SFX_4('umi154')
    sprite('Action_055_04', 4)	# 50-53
    sprite('Action_055_05', 4)	# 54-57
    sprite('Action_055_06', 4)	# 58-61
    sprite('Action_055_07', 2)	# 62-63
    sprite('Action_055_08', 2)	# 64-65

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(7000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown11001(0, 10, 0)
        JumpCancel_(0)
    sprite('Action_056_01', 8)	# 1-8	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 3)	# 9-11	 **attackbox here**
    Unknown20000(1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    physicsXImpulse(6000)
    physicsYImpulse(35000)
    setGravity(2000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_057_01', 5)	# 12-16	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    SFX_4('umi153')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_02', 5)	# 17-21	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_03', 4)	# 22-25	 **attackbox here**
    Unknown5000(5, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_04', 4)	# 26-29	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_05', 3)	# 30-32	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_06', 3)	# 33-35	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_07', 2)	# 36-37	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_08', 2)	# 38-39	 **attackbox here**
    Unknown5000(5, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_09', 2)	# 40-41	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_10', 14)	# 42-55	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(1)
    sprite('Action_057_11', 10)	# 56-65	 **attackbox here**
    GFX_0('EffGroundBreak02', 1)
    SFX_4('umi102_0')
    Unknown20000(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    SFX_0('209_down_normal_0')
    sprite('Action_057_12', 2)	# 66-67
    sprite('Action_057_13', 3)	# 68-70
    physicsXImpulse(-7000)
    physicsYImpulse(12000)
    setGravity(3000)
    clearUponHandler(2)
    sendToLabelUpon(2, 11)
    sprite('Action_057_14', 5)	# 71-75
    sprite('Action_057_15', 5)	# 76-80
    label(10)
    sprite('Action_057_16', 5)	# 81-85
    sprite('Action_057_17', 3)	# 86-88
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('Action_057_18', 3)	# 89-91
    JumpCancel_(1)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_057_19', 2)	# 92-93
    sprite('Action_057_20', 3)	# 94-96
    sprite('Action_057_21', 3)	# 97-99
    sprite('Action_057_22', 3)	# 100-102

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
                Unknown1015(1000)
                if (SLOT_12 >= 32000):
                    SLOT_12 = 32000
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
    sprite('Action_045_04', 3)	# 16-18
    sprite('Action_045_05', 3)	# 19-21
    sprite('Action_045_06', 3)	# 22-24
    Unknown8006(100, 1, 1)
    sprite('Action_045_07', 3)	# 25-27
    sprite('Action_045_08', 3)	# 28-30
    sprite('Action_045_09', 3)	# 31-33
    sprite('Action_045_02', 3)	# 34-36
    Unknown8006(100, 1, 1)
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
    Unknown23027()
    sprite('Action_055_02', 2)	# 45-46
    sprite('Action_055_03', 3)	# 47-49
    SFX_4('umi154')
    sprite('Action_055_04', 4)	# 50-53
    sprite('Action_055_05', 4)	# 54-57
    sprite('Action_055_06', 4)	# 58-61
    sprite('Action_055_07', 2)	# 62-63
    sprite('Action_055_08', 2)	# 64-65

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(7000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown11001(0, 10, 0)
        Unknown13021(1)
        Unknown21005(1)
        JumpCancel_(0)
    sprite('Action_056_01', 8)	# 1-8	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('Action_057_00', 3)	# 9-11	 **attackbox here**
    Unknown2005()
    Unknown20000(1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    physicsXImpulse(6000)
    physicsYImpulse(35000)
    setGravity(2000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_057_01', 5)	# 12-16	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    SFX_4('umi153')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_02', 5)	# 17-21	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_03', 4)	# 22-25	 **attackbox here**
    Unknown5000(5, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_04', 4)	# 26-29	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_05', 3)	# 30-32	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_06', 3)	# 33-35	 **attackbox here**
    SFX_0('005_swing_grap_2_0')
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_07', 2)	# 36-37	 **attackbox here**
    Unknown5000(27, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_08', 2)	# 38-39	 **attackbox here**
    Unknown5000(5, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_09', 2)	# 40-41	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_057_10', 14)	# 42-55	 **attackbox here**
    Unknown5000(6, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    label(1)
    sprite('Action_057_11', 10)	# 56-65	 **attackbox here**
    GFX_0('EffGroundBreak02', 1)
    SFX_4('umi102_0')
    Unknown20000(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    SFX_0('209_down_normal_0')
    sprite('Action_057_12', 2)	# 66-67
    sprite('Action_057_13', 3)	# 68-70
    physicsXImpulse(-7000)
    physicsYImpulse(12000)
    setGravity(3000)
    clearUponHandler(2)
    sendToLabelUpon(2, 11)
    sprite('Action_057_14', 5)	# 71-75
    sprite('Action_057_15', 5)	# 76-80
    label(10)
    sprite('Action_057_16', 5)	# 81-85
    sprite('Action_057_17', 3)	# 86-88
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('Action_057_18', 3)	# 89-91
    JumpCancel_(1)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_057_19', 2)	# 92-93
    sprite('Action_057_20', 3)	# 94-96
    sprite('Action_057_21', 3)	# 97-99
    sprite('Action_057_22', 3)	# 100-102

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(28000)
        AirPushbackX(7000)
        AirUntechableTime(52)
        Unknown1084(0)
        sendToLabelUpon(2, 1)
        Hitstop(2)
    sprite('Action_422_00', 6)	# 1-6
    sprite('Action_422_01', 6)	# 7-12
    sprite('Action_422_02', 2)	# 13-14	 **attackbox here**
    StartMultihit()
    physicsYImpulse(36000)
    physicsXImpulse(10000)
    setGravity(1300)
    tag_voice(1, 'umi206_0', 'umi206_1', 'umi206_2', '')
    SFX_0('008_swing_pole_1')
    sprite('Action_422_03', 2)	# 15-16	 **attackbox here**
    sprite('Action_422_04', 2)	# 17-18	 **attackbox here**
    sprite('Action_422_05', 2)	# 19-20	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    sprite('Action_422_06', 2)	# 21-22	 **attackbox here**
    sprite('Action_422_07', 2)	# 23-24	 **attackbox here**
    sprite('Action_422_08', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(26000)
    YAccel(50)
    setGravity(800)
    SFX_0('008_swing_pole_1')
    sprite('Action_422_09', 2)	# 27-28	 **attackbox here**
    sprite('Action_422_20', 4)	# 29-32	 **attackbox here**
    setGravity(1800)
    setInvincible(0)
    sprite('Action_422_21', 3)	# 33-35	 **attackbox here**
    sprite('Action_422_22', 3)	# 36-38	 **attackbox here**
    sprite('Action_422_23', 3)	# 39-41
    label(0)
    sprite('Action_422_24', 3)	# 42-44
    sprite('Action_422_25', 3)	# 45-47
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 6)	# 48-53
    clearUponHandler(2)
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_021_01', 6)	# 54-59
    sprite('Action_021_01', 5)	# 60-64
    Unknown18009(0)
    sprite('Action_021_02', 5)	# 65-69

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(28000)
        AirPushbackX(7000)
        AirUntechableTime(52)
        Unknown1084(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
        Hitstop(2)
    sprite('Action_420_00', 7)	# 1-7
    sprite('Action_422_02', 2)	# 8-9	 **attackbox here**
    StartMultihit()
    physicsYImpulse(36000)
    physicsXImpulse(5120)
    setGravity(1300)
    tag_voice(1, 'umi206_0', 'umi206_1', 'umi206_2', '')
    SFX_0('008_swing_pole_1')
    sprite('Action_422_03', 2)	# 10-11	 **attackbox here**
    sprite('Action_422_04', 2)	# 12-13	 **attackbox here**
    sprite('Action_422_05', 2)	# 14-15	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    sprite('Action_422_06', 2)	# 16-17	 **attackbox here**
    sprite('Action_422_07', 2)	# 18-19	 **attackbox here**
    sprite('Action_422_08', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(26000)
    YAccel(50)
    setGravity(800)
    SFX_0('008_swing_pole_1')
    sprite('Action_422_09', 2)	# 22-23	 **attackbox here**
    sprite('Action_422_20', 4)	# 24-27	 **attackbox here**
    setGravity(1800)
    setInvincible(0)
    sprite('Action_422_21', 3)	# 28-30	 **attackbox here**
    sprite('Action_422_22', 3)	# 31-33	 **attackbox here**
    sprite('Action_422_23', 3)	# 34-36
    label(0)
    sprite('Action_422_24', 3)	# 37-39
    sprite('Action_422_25', 3)	# 40-42
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 6)	# 43-48
    Unknown18009(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_021_01', 6)	# 49-54
    sprite('Action_021_01', 5)	# 55-59
    Unknown18009(0)
    sprite('Action_021_02', 5)	# 60-64

@Subroutine
def MissileInit():
    AttackLevel_(3)
    Damage(1800)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AttackP1(80)
    AirUntechableTime(36)
    AirPushbackX(8000)
    AirPushbackY(20000)
    Unknown11001(-3, -3, 2)
    Unknown11058('0100000000000000000000000000000000000000')
    if (SLOT_2 == 3):
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-40000)
        Unknown9202(1)
    if (SLOT_2 == 9):
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackY(33000)
    if (SLOT_2 == 2):
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(-40000)
        Unknown9202(1)
    if (SLOT_2 == 8):
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(1000)
        AirPushbackY(33000)
    SLOT_31 = (SLOT_31 + (-1))
    Unknown1084(1)
    Unknown22004(10, 1)

    def upon_8():
        if SLOT_36:
            Unknown2006()

@Subroutine
def MissileAddInit():
    SLOT_32 = (SLOT_32 + (-1))
    clearUponHandler(2)
    Unknown30068(1)
    if SLOT_59:
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
    Unknown23159('Assault_Add_Any')

@Subroutine
def MissileAdd_Begin():
    Unknown14070('Assault_Add_1')
    Unknown14070('Assault_Add_2')
    Unknown14070('Assault_Add_3')
    Unknown14070('Assault_Add_4')
    Unknown14070('Assault_Add_6')
    Unknown14070('Assault_Add_7')
    Unknown14070('Assault_Add_8')
    Unknown14070('Assault_Add_9')

    def upon_ON_HIT_OR_BLOCK():
        Unknown14070('Assault_Add_5')

@Subroutine
def MissileAdd_Timing():
    Unknown14072('Assault_Add_1')
    Unknown14072('Assault_Add_2')
    Unknown14072('Assault_Add_3')
    Unknown14072('Assault_Add_4')
    Unknown14072('Assault_Add_5')
    Unknown14072('Assault_Add_6')
    Unknown14072('Assault_Add_7')
    Unknown14072('Assault_Add_8')
    Unknown14072('Assault_Add_9')

@Subroutine
def MissileAdd_Clear():
    Unknown14074('Assault_Add_1')
    Unknown14074('Assault_Add_2')
    Unknown14074('Assault_Add_3')
    Unknown14074('Assault_Add_4')
    Unknown14074('Assault_Add_5')
    Unknown14074('Assault_Add_6')
    Unknown14074('Assault_Add_7')
    Unknown14074('Assault_Add_8')
    Unknown14074('Assault_Add_9')

@State
def AssaultA():

    def upon_IMMEDIATE():
        SLOT_59 = 0
        SLOT_32 = 1
        AttackDefaults_StandingSpecial()
        callSubroutine('MissileInit')
    sprite('Action_160_00', 4)	# 1-4
    sprite('Action_160_01', 3)	# 5-7
    clearUponHandler(2)
    Unknown1007(5000)
    sprite('Action_160_02', 3)	# 8-10
    sprite('Action_160_03', 3)	# 11-13
    sprite('Action_160_04', 2)	# 14-15
    sprite('Action_160_05', 5)	# 16-20	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(50000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_160_06', 5)	# 21-25	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_160_07', 5)	# 26-30	 **attackbox here**
    sprite('Action_160_08', 5)	# 31-35	 **attackbox here**
    sprite('Action_160_09', 3)	# 36-38
    Unknown2017(1)
    Unknown26('EffMissile_Move')
    Unknown1019(10)
    Unknown1043()
    Recovery()
    sprite('Action_160_10', 3)	# 39-41
    callSubroutine('MissileAdd_Clear')
    sprite('Action_160_11', 3)	# 42-44
    sprite('Action_160_12', 3)	# 45-47
    ExitState()
    label(1)
    sprite('Action_168_00', 3)	# 48-50
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 3)	# 51-53
    sprite('Action_168_02', 3)	# 54-56

@State
def AssaultB():

    def upon_IMMEDIATE():
        SLOT_59 = 0
        SLOT_32 = 1
        Unknown2037(9)
        AttackDefaults_StandingSpecial()
        callSubroutine('MissileInit')
    sprite('Action_161_00', 4)	# 1-4
    sprite('Action_161_01', 3)	# 5-7
    clearUponHandler(2)
    Unknown1007(5000)
    sprite('Action_161_02', 3)	# 8-10
    sprite('Action_161_03', 3)	# 11-13
    sprite('Action_161_04', 2)	# 14-15
    sprite('Action_161_05', 5)	# 16-20	 **attackbox here**
    GFX_0('EffMissile_9', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2009, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_161_06', 5)	# 21-25	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_161_07', 5)	# 26-30	 **attackbox here**
    sprite('Action_161_08', 5)	# 31-35	 **attackbox here**
    sprite('Action_161_09', 3)	# 36-38
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_161_10', 3)	# 39-41
    callSubroutine('MissileAdd_Clear')
    sprite('Action_161_11', 3)	# 42-44
    sprite('Action_161_12', 3)	# 45-47
    ExitState()
    label(1)
    sprite('Action_168_00', 3)	# 48-50
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 3)	# 51-53
    sprite('Action_168_02', 3)	# 54-56

@State
def AssaultA_Air():

    def upon_IMMEDIATE():
        SLOT_59 = 0
        SLOT_32 = 1
        Unknown17003()
        callSubroutine('MissileInit')
    sprite('Action_160_00', 2)	# 1-2
    sprite('Action_160_01', 2)	# 3-4
    clearUponHandler(2)
    Unknown1007(5000)
    sprite('Action_160_02', 3)	# 5-7
    sprite('Action_160_03', 3)	# 8-10
    sprite('Action_160_04', 2)	# 11-12
    sprite('Action_160_05', 5)	# 13-17	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(50000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_160_06', 5)	# 18-22	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_160_07', 5)	# 23-27	 **attackbox here**
    sprite('Action_160_08', 5)	# 28-32	 **attackbox here**
    sprite('Action_160_09', 3)	# 33-35
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    Unknown1043()
    Recovery()
    sprite('Action_160_10', 3)	# 36-38
    callSubroutine('MissileAdd_Clear')
    sprite('Action_160_11', 3)	# 39-41
    sprite('Action_160_12', 3)	# 42-44
    ExitState()
    label(1)
    sprite('Action_168_00', 3)	# 45-47
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 3)	# 48-50
    sprite('Action_168_02', 3)	# 51-53

@State
def AssaultB_Air():

    def upon_IMMEDIATE():
        SLOT_59 = 0
        SLOT_32 = 1
        Unknown2037(3)
        Unknown17003()
        callSubroutine('MissileInit')
    sprite('Action_164_00', 2)	# 1-2
    sprite('Action_164_01', 2)	# 3-4
    clearUponHandler(2)
    Unknown1007(5000)
    sprite('Action_164_02', 3)	# 5-7
    sprite('Action_164_03', 3)	# 8-10
    sprite('Action_164_04', 2)	# 11-12
    sprite('Action_164_05', 5)	# 13-17	 **attackbox here**
    GFX_0('EffMissile_3', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2003, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(-30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_164_06', 5)	# 18-22	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_164_07', 5)	# 23-27	 **attackbox here**
    sprite('Action_164_08', 5)	# 28-32	 **attackbox here**
    sprite('Action_164_09', 3)	# 33-35
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_164_10', 3)	# 36-38
    callSubroutine('MissileAdd_Clear')
    sprite('Action_164_11', 3)	# 39-41
    sprite('Action_164_12', 3)	# 42-44
    label(0)
    sprite('Action_164_13', 3)	# 45-47
    sprite('Action_164_14', 3)	# 48-50
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_168_00', 3)	# 51-53
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 5)	# 54-58
    sprite('Action_168_02', 6)	# 59-64

@State
def AssaultEX():

    def upon_IMMEDIATE():
        SLOT_59 = 1
        SLOT_32 = 3
        AttackDefaults_StandingSpecial()
        callSubroutine('MissileInit')
        Unknown11091(10)
        Unknown30065(0)
    sprite('Action_160_00', 3)	# 1-3
    sprite('Action_160_00', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_160_01', 3)	# 5-7
    clearUponHandler(2)
    Unknown1007(5000)
    sprite('Action_160_02', 3)	# 8-10
    sprite('Action_160_03', 3)	# 11-13
    sprite('Action_160_04', 2)	# 14-15
    sprite('Action_160_05', 5)	# 16-20	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(60000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_160_06', 5)	# 21-25	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_160_07', 5)	# 26-30	 **attackbox here**
    sprite('Action_160_08', 5)	# 31-35	 **attackbox here**
    sprite('Action_160_09', 3)	# 36-38
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    Unknown1043()
    Recovery()
    sprite('Action_160_10', 3)	# 39-41
    callSubroutine('MissileAdd_Clear')
    sprite('Action_160_11', 3)	# 42-44
    sprite('Action_160_12', 3)	# 45-47
    label(0)
    sprite('Action_160_13', 3)	# 48-50
    sprite('Action_160_14', 3)	# 51-53
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_168_00', 3)	# 54-56
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 3)	# 57-59
    sprite('Action_168_02', 3)	# 60-62

@State
def AssaultEX_Air():

    def upon_IMMEDIATE():
        SLOT_59 = 1
        SLOT_32 = 3
        Unknown17003()
        callSubroutine('MissileInit')
        Unknown11091(10)
        Unknown30065(0)
    sprite('Action_160_00', 2)	# 1-2
    sprite('Action_160_01', 1)	# 3-3
    clearUponHandler(2)
    Unknown1007(5000)
    sprite('Action_160_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('Action_160_02', 3)	# 5-7
    sprite('Action_160_03', 3)	# 8-10
    sprite('Action_160_04', 2)	# 11-12
    sprite('Action_160_05', 5)	# 13-17	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(60000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_160_06', 5)	# 18-22	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_160_07', 5)	# 23-27	 **attackbox here**
    sprite('Action_160_08', 5)	# 28-32	 **attackbox here**
    sprite('Action_160_09', 3)	# 33-35
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    Unknown1043()
    Recovery()
    sprite('Action_160_10', 3)	# 36-38
    callSubroutine('MissileAdd_Clear')
    sprite('Action_160_11', 3)	# 39-41
    sprite('Action_160_12', 3)	# 42-44
    label(0)
    sprite('Action_160_13', 3)	# 45-47
    sprite('Action_160_14', 3)	# 48-50
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_168_00', 3)	# 51-53
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 3)	# 54-56
    sprite('Action_168_02', 3)	# 57-59

@State
def Assault_Add_6():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
    sprite('Action_173_00', 6)	# 1-6
    sprite('Action_173_01', 3)	# 7-9
    sprite('Action_173_02', 2)	# 10-11
    sprite('Action_173_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(50000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_173_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_173_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_173_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_173_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    Unknown1043()
    Recovery()
    sprite('Action_173_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_173_09', 3)	# 34-36
    sprite('Action_173_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 4)	# 54-57

@State
def Assault_Add_4():

    def upon_IMMEDIATE():
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
        Unknown2005()
    sprite('Action_173_00', 6)	# 1-6
    sprite('Action_173_01', 3)	# 7-9
    sprite('Action_173_02', 2)	# 10-11
    sprite('Action_173_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(50000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_173_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_173_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_173_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_173_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    Unknown1043()
    Recovery()
    sprite('Action_173_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_173_09', 3)	# 34-36
    sprite('Action_173_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 4)	# 54-57

@State
def Assault_Add_9():

    def upon_IMMEDIATE():
        Unknown2037(9)
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
    sprite('Action_177_00', 6)	# 1-6
    sprite('Action_177_01', 3)	# 7-9
    sprite('Action_177_02', 2)	# 10-11
    sprite('Action_177_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_9', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2009, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_177_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_177_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_177_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_177_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_177_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_177_09', 3)	# 34-36
    sprite('Action_177_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 4)	# 54-57

@State
def Assault_Add_7():

    def upon_IMMEDIATE():
        Unknown2037(9)
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
        Unknown2005()
    sprite('Action_177_00', 6)	# 1-6
    sprite('Action_177_01', 3)	# 7-9
    sprite('Action_177_02', 2)	# 10-11
    sprite('Action_177_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_9', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2009, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_177_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_177_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_177_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_177_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_177_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_177_09', 3)	# 34-36
    sprite('Action_177_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 4)	# 54-57

@State
def Assault_Add_8():

    def upon_IMMEDIATE():
        Unknown2037(8)
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
        Unknown2006()
    sprite('Action_179_00', 6)	# 1-6
    sprite('Action_179_01', 3)	# 7-9
    sprite('Action_179_02', 2)	# 10-11
    sprite('Action_179_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_8', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2008, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsYImpulse(30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_179_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_179_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_179_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_179_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_179_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_179_09', 3)	# 34-36
    sprite('Action_179_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 4)	# 54-57

@State
def Assault_Add_2():

    def upon_IMMEDIATE():
        Unknown2037(2)
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
        Unknown2006()
    sprite('Action_181_00', 6)	# 1-6
    sprite('Action_181_01', 3)	# 7-9
    sprite('Action_181_02', 2)	# 10-11
    sprite('Action_181_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_2', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2002, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsYImpulse(-40000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_181_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_181_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_181_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_181_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_181_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_181_09', 3)	# 34-36
    sprite('Action_181_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 7)	# 54-60

@State
def Assault_Add_3():

    def upon_IMMEDIATE():
        Unknown2037(3)
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
    sprite('Action_175_00', 6)	# 1-6
    sprite('Action_175_01', 3)	# 7-9
    sprite('Action_175_02', 2)	# 10-11
    sprite('Action_175_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_3', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2003, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(-30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_175_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_175_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_175_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_175_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_175_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_175_09', 3)	# 34-36
    sprite('Action_175_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 7)	# 54-60

@State
def Assault_Add_1():

    def upon_IMMEDIATE():
        Unknown2037(3)
        Unknown17003()
        callSubroutine('MissileInit')
        callSubroutine('MissileAddInit')
        Unknown2005()
    sprite('Action_175_00', 6)	# 1-6
    sprite('Action_175_01', 3)	# 7-9
    sprite('Action_175_02', 2)	# 10-11
    sprite('Action_175_03', 4)	# 12-15	 **attackbox here**
    GFX_0('EffMissile_3', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2003, 0)
    tag_voice(1, 'umi202_0', 'umi202_1', 'umi202_2', '')
    callSubroutine('MissileAdd_Begin')
    Unknown2017(0)
    physicsXImpulse(30000)
    physicsYImpulse(-30000)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_175_04', 4)	# 16-19	 **attackbox here**
    callSubroutine('MissileAdd_Timing')
    sprite('Action_175_05', 4)	# 20-23	 **attackbox here**
    sprite('Action_175_06', 4)	# 24-27	 **attackbox here**
    sprite('Action_175_07', 3)	# 28-30
    Unknown26('EffMissile_Move')
    Unknown2017(1)
    Unknown1019(10)
    YAccel(10)
    Unknown1043()
    Recovery()
    sprite('Action_175_08', 3)	# 31-33
    callSubroutine('MissileAdd_Clear')
    sprite('Action_175_09', 3)	# 34-36
    sprite('Action_175_10', 3)	# 37-39
    ExitState()
    label(1)
    sprite('Action_168_00', 4)	# 40-43
    callSubroutine('MissileAdd_Clear')
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    Unknown2017(1)
    sprite('Action_168_01', 10)	# 44-53
    sprite('Action_168_02', 7)	# 54-60

@Subroutine
def CommandThrowInit():
    Unknown17011('CommandThrow_Exe', 2, 0, 0)
    Unknown11054(150000)
    Unknown11032('40420f0000000000ffffffffffffffff')
    Unknown11002(-1)
    Unknown30061(1)
    Unknown11107(1)
    Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
    Unknown23027()
    sendToLabelUpon(2, 1)

    def upon_LANDING():
        Unknown11107(0)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
    Unknown28(8, 'CommandThrow_Suka')

@State
def CommandThrow_A():

    def upon_IMMEDIATE():
        callSubroutine('CommandThrowInit')
    sprite('Action_198_00', 3)	# 1-3
    sprite('Action_198_01', 6)	# 4-9
    tag_voice(1, 'umi203_0', 'umi203_1', 'umi203_2', '')
    sprite('Action_198_02', 4)	# 10-13
    Unknown8000(100, 1, 1)
    physicsXImpulse(21000)
    physicsYImpulse(11000)
    setGravity(2000)
    SFX_0('001_airbackdash_0')
    sprite('Action_198_03', 4)	# 14-17	 **attackbox here**
    sprite('Action_198_03', 32767)	# 18-32784	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('Action_198_04', 3)	# 32785-32787	 **attackbox here**

@State
def CommandThrow_B():

    def upon_IMMEDIATE():
        callSubroutine('CommandThrowInit')
    sprite('Action_198_00', 3)	# 1-3
    sprite('Action_198_00', 3)	# 4-6
    tag_voice(1, 'umi203_0', 'umi203_1', 'umi203_2', '')
    sprite('Action_198_01', 6)	# 7-12
    sprite('Action_198_02', 4)	# 13-16
    Unknown8000(100, 1, 1)
    physicsXImpulse(40000)
    physicsYImpulse(12000)
    setGravity(2000)
    SFX_0('001_airbackdash_0')
    sprite('Action_198_03', 4)	# 17-20	 **attackbox here**
    sprite('Action_198_03', 32767)	# 21-32787	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('Action_198_04', 3)	# 32788-32790	 **attackbox here**

@State
def CommandThrow_EX():

    def upon_IMMEDIATE():
        callSubroutine('CommandThrowInit')
        Unknown11091(10)
        Unknown30065(0)
    sprite('Action_198_00', 3)	# 1-3
    sprite('Action_198_00', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'umi203_0', 'umi203_1', 'umi203_2', '')
    sprite('Action_198_01', 6)	# 7-12
    sprite('Action_198_02', 4)	# 13-16
    Unknown8000(100, 1, 1)
    physicsYImpulse(12000)
    SLOT_12 = SLOT_19
    Unknown1019(5)
    if (SLOT_12 >= 50000):
        SLOT_12 = 50000
        physicsYImpulse(14000)
    if (SLOT_12 <= 20000):
        SLOT_12 = 20000
        physicsYImpulse(8000)
    setGravity(1600)
    SFX_0('001_airbackdash_0')
    sprite('Action_198_03', 4)	# 17-20	 **attackbox here**
    sprite('Action_198_03', 32767)	# 21-32787	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('Action_198_04', 3)	# 32788-32790	 **attackbox here**

@State
def CommandThrow_Suka():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown23027()
        Unknown30068(1)
        if Unknown23145('CommandThrow_EX'):
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)
    sprite('Action_198_05', 3)	# 1-3
    SFX_4('umi154')
    sprite('Action_198_06', 3)	# 4-6
    sprite('Action_198_05', 4)	# 7-10
    sprite('Action_198_06', 4)	# 11-14
    sprite('Action_198_05', 5)	# 15-19
    sprite('Action_198_06', 5)	# 20-24
    sprite('Action_198_08', 8)	# 25-32
    sprite('Action_198_09', 3)	# 33-35

@State
def CommandThrow_Exe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Unknown11091(5)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(10000)
        AirUntechableTime(60)
        Unknown11023(1)
        Unknown11072(1, 112500, 251000)
        Unknown23027()
        if Unknown23145('CommandThrow_A'):
            Damage(3200)
            AirPushbackY(22000)

            def upon_78():
                Unknown8003(100, 1, 1)
                ScreenShake(4000, 4000)
        if Unknown23145('CommandThrow_B'):
            Damage(3700)
            AirPushbackY(30000)

            def upon_78():
                Unknown8003(100, 1, 1)
                ScreenShake(6000, 6000)
        if Unknown23145('CommandThrow_EX'):
            Damage(4000)
            AirHitstunAnimation(13)
            GroundedHitstunAnimation(13)
            AirPushbackX(5000)
            AirPushbackY(38000)
            Hitstop(20)
            Unknown11091(10)
            Unknown30065(0)
            Unknown2037(1)
            Unknown3029(1)
            Unknown3069(2)
            Unknown3072('80000000000000000000000000000000')
            Unknown3073('00000000000000000000000000000000')
            Unknown3074('000000000400000032000000a0000000')
            Unknown3075('00000000000000000000000010000000')
            Unknown3076(1010)
            Unknown3077(900)

            def upon_78():
                Unknown8004(100, 1, 1)
                ScreenShake(10000, 10000)
        Unknown13024(0)
        Unknown30068(1)
        setInvincible(1)
        sendToLabelUpon(2, 1)
    sprite('Action_198_04', 32767)	# 1-32767	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000000000000040000000000000000000000')
    physicsXImpulse(22000)
    physicsYImpulse(-100)
    setGravity(2000)
    label(1)
    sprite('Action_201_01', 3)	# 32768-32770	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_201_02', 6)	# 32771-32776	 **attackbox here**
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_201_03', 4)	# 32777-32780
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_201_04', 3)	# 32781-32783
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_05', 3)	# 32784-32786
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_06', 2)	# 32787-32788
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_07', 20)	# 32789-32808
    Unknown20(30, 2, 2)
    GFX_0('EffCanonCharge', 0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_08', 2)	# 32809-32810
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_09', 3)	# 32811-32813	 **attackbox here**
    GFX_0('EffCanonExe', -1)
    tag_voice(0, 'umi204_0', 'umi204_1', 'umi204_2', '')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    SFX_0('016_explode_1')
    sprite('Action_201_10', 5)	# 32814-32818	 **attackbox here**
    Unknown1045(-30000)
    sprite('Action_201_11', 9)	# 32819-32827
    Unknown23183('416374696f6e5f3230315f313100000000000000000000000000000000000000070000000200000002000000')
    sprite('Action_201_12', 5)	# 32828-32832
    Unknown23183('416374696f6e5f3230315f313200000000000000000000000000000000000000030000000200000002000000')
    sprite('Action_201_13', 6)	# 32833-32838
    Unknown23183('416374696f6e5f3230315f313300000000000000000000000000000000000000040000000200000002000000')
    Unknown1084(1)
    sprite('Action_201_14', 6)	# 32839-32844
    Unknown23183('416374696f6e5f3230315f313400000000000000000000000000000000000000050000000200000002000000')
    SLOT_4 = 1

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AttackP2(100)
        Unknown11091(20)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2073(1)
        setInvincible(1)

        def upon_78():
            Hitstop(0)
            Unknown13024(0)
            enterState('UltimateAssault_catch')
            Unknown11069('UltimateAssault_catch')
    sprite('Action_222_00', 5)	# 1-5
    sprite('Action_222_01', 5)	# 6-10
    Unknown23024(1)
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'umi250_0', 'umi250_1', '', '')
    sprite('Action_222_02', 5)	# 11-15
    sprite('Action_222_03', 5)	# 16-20
    sprite('Action_222_04', 5)	# 21-25
    sprite('Action_222_05', 5)	# 26-30
    sprite('Action_222_06', 5)	# 31-35
    sprite('Action_222_07', 5)	# 36-40
    sprite('Action_222_08', 5)	# 41-45
    sprite('Action_222_09', 24)	# 46-69
    sprite('Action_222_10ex', 4)	# 70-73	 **attackbox here**
    GFX_0('EffUltimateAssault_01', -1)
    tag_voice(0, 'umi251_0', 'umi251_1', '', '')
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_222_11ex', 4)	# 74-77	 **attackbox here**
    setInvincible(0)
    Unknown1019(70)
    YAccel(70)
    sprite('Action_222_12ex', 4)	# 78-81	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    sprite('Action_223_00', 4)	# 82-85
    Unknown13024(1)
    Unknown1019(10)
    YAccel(10)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    sprite('Action_223_01', 4)	# 86-89
    setInvincible(0)
    sprite('Action_223_02', 4)	# 90-93
    sprite('Action_223_03', 3)	# 94-96
    sprite('Action_223_04', 3)	# 97-99
    sprite('Action_223_05', 2)	# 100-101
    sprite('Action_223_06', 3)	# 102-104
    sprite('Action_223_07', 2)	# 105-106
    sprite('Action_223_08', 3)	# 107-109	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    RefreshMultihit()
    AttackP2(60)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7000)
    AirPushbackY(-40000)
    Unknown9190(1)
    Unknown9118(80)
    Unknown9310(-1)
    Hitstop(8)
    Unknown11064(0)
    Unknown2073(0)
    physicsXImpulse(50000)
    physicsYImpulse(-60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_223_09', 3)	# 110-112	 **attackbox here**
    sprite('Action_223_10', 3)	# 113-115	 **attackbox here**
    sprite('Action_223_11', 5)	# 116-120	 **attackbox here**
    label(109)
    sprite('Action_223_12', 5)	# 121-125
    GFX_0('EffGroundBreak03', 0)
    Unknown1084(1)
    SFX_0('016_explode_2')
    ScreenShake(0, 20000)
    sprite('Action_224_00', 5)	# 126-130
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 111)
    sprite('Action_224_01', 5)	# 131-135
    sprite('Action_224_02', 5)	# 136-140
    sprite('Action_224_03', 5)	# 141-145
    sprite('Action_224_04', 4)	# 146-149
    label(110)
    sprite('Action_224_05', 3)	# 150-152
    sprite('Action_224_06', 3)	# 153-155
    loopRest()
    gotoLabel(110)
    label(111)
    sprite('Action_224_07', 5)	# 156-160
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_224_08', 6)	# 161-166
    sprite('Action_224_09', 5)	# 167-171

@State
def AirUltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AttackP2(100)
        Unknown11091(20)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2073(1)
        Unknown11072(1, 100000, 150000)
        SLOT_5 = 1
        setInvincible(1)

        def upon_78():
            Hitstop(0)
            Unknown13024(0)
            enterState('UltimateAssault_catch')
            Unknown11069('UltimateAssault_catch')
    sprite('Action_262_00', 5)	# 1-5
    Unknown1084(1)
    sprite('Action_262_01', 3)	# 6-8
    Unknown23024(1)
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'umi250_0', 'umi250_1', '', '')
    Unknown1007(5000)
    sprite('Action_262_02', 3)	# 9-11
    sprite('Action_262_03', 3)	# 12-14
    sprite('Action_262_04', 3)	# 15-17
    sprite('Action_262_03', 3)	# 18-20
    sprite('Action_262_04', 3)	# 21-23
    sprite('Action_262_03', 3)	# 24-26
    sprite('Action_262_04', 3)	# 27-29
    sprite('Action_262_03', 3)	# 30-32
    sprite('Action_262_04', 3)	# 33-35
    sprite('Action_262_03', 3)	# 36-38
    sprite('Action_262_07', 3)	# 39-41
    sprite('Action_164_00', 5)	# 42-46
    sprite('Action_164_01', 5)	# 47-51
    sprite('Action_164_02', 5)	# 52-56
    sprite('Action_177_00', 5)	# 57-61
    sprite('Action_177_01', 8)	# 62-69
    sprite('Action_222_10ex', 4)	# 70-73	 **attackbox here**
    GFX_0('EffUltimateAssault_01', -1)
    tag_voice(0, 'umi251_0', 'umi251_1', '', '')
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_222_11ex', 4)	# 74-77	 **attackbox here**
    setInvincible(0)
    Unknown1019(70)
    YAccel(70)
    sprite('Action_222_12ex', 4)	# 78-81	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    sprite('Action_223_00', 4)	# 82-85
    Unknown13024(1)
    Unknown1019(10)
    YAccel(10)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    sprite('Action_223_01', 4)	# 86-89
    setInvincible(0)
    sprite('Action_223_02', 4)	# 90-93
    sprite('Action_223_03', 3)	# 94-96
    sprite('Action_223_04', 3)	# 97-99
    sprite('Action_223_05', 2)	# 100-101
    sprite('Action_223_06', 3)	# 102-104
    sprite('Action_223_07', 2)	# 105-106
    sprite('Action_223_08', 3)	# 107-109	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    RefreshMultihit()
    AttackP2(60)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7000)
    AirPushbackY(-40000)
    Unknown9190(1)
    Unknown9118(80)
    Unknown9310(-1)
    Hitstop(8)
    Unknown11064(0)
    Unknown2073(0)
    physicsXImpulse(50000)
    physicsYImpulse(-60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_223_09', 3)	# 110-112	 **attackbox here**
    sprite('Action_223_10', 3)	# 113-115	 **attackbox here**
    sprite('Action_223_11', 5)	# 116-120	 **attackbox here**
    label(108)
    sprite('Action_223_08', 3)	# 121-123	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    sprite('Action_223_09', 3)	# 124-126	 **attackbox here**
    sprite('Action_223_10', 3)	# 127-129	 **attackbox here**
    sprite('Action_223_11', 5)	# 130-134	 **attackbox here**
    gotoLabel(108)
    label(109)
    sprite('Action_223_12', 5)	# 135-139
    GFX_0('EffGroundBreak03', 0)
    Unknown1084(1)
    SFX_0('016_explode_2')
    ScreenShake(0, 20000)
    sprite('Action_224_00', 5)	# 140-144
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 111)
    sprite('Action_224_01', 5)	# 145-149
    sprite('Action_224_02', 5)	# 150-154
    sprite('Action_224_03', 5)	# 155-159
    sprite('Action_224_04', 4)	# 160-163
    label(110)
    sprite('Action_224_05', 3)	# 164-166
    sprite('Action_224_06', 3)	# 167-169
    loopRest()
    gotoLabel(110)
    label(111)
    sprite('Action_224_07', 5)	# 170-174
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_224_08', 6)	# 175-180
    sprite('Action_224_09', 5)	# 181-185

@State
def UltimateAssault_catch():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssault_exe_1', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(150)
        AttackP2(100)
        Unknown11091(20)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown20003(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11108('03000000')
        Unknown11069('UltimateAssault_exe_1')
        Unknown11064(1)
        Unknown11023(1)
    sprite('Action_225_00', 4)	# 1-4	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('UltimateAssaultLookAtMeCamera', -1)
    physicsXImpulse(0)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('keep', 1)	# 5-5
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssault_exe_1():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP2(100)
        Unknown11091(20)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown2037(4)

        def upon_3():
            if (not SLOT_2):
                sendToLabel(1)
    label(0)
    sprite('Action_225_00', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    ScreenShake(0, 8000)
    physicsXImpulse(1000)
    physicsYImpulse(60000)
    setGravity(100)
    RefreshMultihit()
    Damage(150)
    PushbackX(60000)
    Hitstop(0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown2038(-1)
    Unknown30048(1)
    Unknown11023(1)
    sprite('Action_225_01', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_225_03', 60)	# 11-70	 **attackbox here**
    clearUponHandler(3)
    Unknown2034(0)
    Unknown2053(0)
    RefreshMultihit()
    Unknown30079(0)
    physicsXImpulse(50000)
    physicsYImpulse(50000)
    setGravity(100)
    AirPushbackX(100)
    AirPushbackY(5000)
    YImpluseBeforeWallbounce(50)
    PushbackX(60000)
    Hitstop(0)
    AirUntechableTime(120)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    Unknown30048(1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008913000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('Action_225_03', 5)	# 71-75	 **attackbox here**
    StartMultihit()
    Unknown11069('UltimateAssault_catch_2')
    enterState('UltimateAssault_catch_2')

@State
def UltimateAssault_catch_2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssault_exe_2', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(150)
        AttackP2(100)
        Unknown11091(15)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11108('03000000')
        Unknown11069('UltimateAssault_exe_2')
        Unknown11064(1)
    sprite('null', 1)	# 1-1
    Unknown1086(22)
    teleportRelativeX(-5000)
    Unknown1007(5000)
    sprite('Action_226_01', 1)	# 2-2	 **attackbox here**
    GFX_0('EffUltimateAssault_05', -1)
    physicsXImpulse(0)
    physicsYImpulse(-5000)
    setGravity(100)
    SFX_0('005_swing_grap_2_2')
    sprite('keep', 1)	# 3-3
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssault_exe_2():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(150)
        AttackP2(100)
        Unknown11091(20)
        setInvincible(1)
        Unknown30079(1)
        Unknown11064(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11108('03000000')
        Unknown2037(9)
        Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008a13000000000000')

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown20000(0)
                Unknown26('UltimateAssaultLookAtMeCamera')
    label(1)
    sprite('Action_226_01', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_06', -1)
    ScreenShake(0, 8000)
    clearUponHandler(78)
    physicsXImpulse(1000)
    physicsYImpulse(-70000)
    setGravity(100)
    RefreshMultihit()
    PushbackX(60000)
    Hitstop(0)
    Unknown30048(1)
    Unknown11023(1)
    sendToLabelUpon(2, 9)
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_226_02', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_227_00', 12)	# 11-22	 **attackbox here**
    GFX_0('EffGroundBreak03', -1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008b13000000000000')
    Unknown20000(1)
    Unknown4004('6566666563745f3338305f430000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f3338325f430000000000000000000000000000000000000000ffff0000')
    Unknown30079(0)
    RefreshMultihit()
    Unknown1084(1)
    clearUponHandler(2)
    Damage(3000)
    AirPushbackX(3000)
    AirPushbackY(100000)
    AttackP1(80)
    AttackP2(60)
    Unknown11091(37)
    AirUntechableTime(120)
    Unknown9310(30)
    Unknown11064(0)
    SFX_0('016_explode_2')
    sprite('Action_227_01', 40)	# 23-62	 **attackbox here**
    Unknown48('19000000020000003300000016000000020000004b000000')
    Unknown48('19000000020000003400000017000000020000004b000000')
    Unknown20003(0)
    sprite('Action_227_02', 1)	# 63-63	 **attackbox here**
    if (not SLOT_51):
        if (not SLOT_52):
            sendToLabel(10)
    sprite('Action_228_00', 4)	# 64-67	 **attackbox here**
    sprite('Action_228_01', 4)	# 68-71	 **attackbox here**
    sprite('Action_228_02', 4)	# 72-75	 **attackbox here**
    sprite('Action_228_03', 4)	# 76-79	 **attackbox here**
    sprite('Action_228_04', 10)	# 80-89	 **attackbox here**
    sprite('Action_228_05', 4)	# 90-93	 **attackbox here**
    sprite('Action_228_06', 14)	# 94-107	 **attackbox here**
    tag_voice(0, 'umi252_0', 'umi252_1', '', '')
    sprite('Action_228_07', 4)	# 108-111	 **attackbox here**
    sprite('Action_228_09', 14)	# 112-125	 **attackbox here**
    Unknown13024(1)
    sprite('Action_228_10', 3)	# 126-128	 **attackbox here**
    sprite('Action_228_11', 3)	# 129-131	 **attackbox here**
    sprite('Action_228_12', 5)	# 132-136	 **attackbox here**
    sprite('Action_228_13', 13)	# 137-149	 **attackbox here**
    Unknown20000(0)
    setInvincible(0)
    Unknown2053(1)
    sprite('Action_228_14', 4)	# 150-153
    sprite('Action_228_15', 5)	# 154-158
    sprite('Action_228_16', 3)	# 159-161
    ExitState()
    label(10)
    sprite('Action_228_00', 60)	# 162-221	 **attackbox here**
    Unknown23024(0)
    Unknown18010()
    sprite('Action_228_05', 5)	# 222-226	 **attackbox here**
    SFX_1('umi252_1')

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 120):
            clearUponHandler(3)
            Unknown21011(100)
            if random_(2, 0, 5):
                sendToLabel(14)
            else:
                SFX_1('umi252_0')
    label(11)
    sprite('Action_228_00', 20)	# 227-246	 **attackbox here**
    sprite('Action_228_00', 25)	# 247-271	 **attackbox here**
    random_(2, 0, 16)
    if SLOT_0:
        _gotolabel(12)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(13)
    sprite('Action_228_00', 50)	# 272-321	 **attackbox here**
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(12)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(13)
    gotoLabel(11)
    label(12)
    sprite('Action_228_01', 4)	# 322-325	 **attackbox here**
    sprite('Action_228_02', 4)	# 326-329	 **attackbox here**
    sprite('Action_228_03', 4)	# 330-333	 **attackbox here**
    sprite('Action_228_04', 10)	# 334-343	 **attackbox here**
    gotoLabel(11)
    label(13)
    sprite('Action_228_05', 5)	# 344-348	 **attackbox here**
    sprite('Action_228_06', 14)	# 349-362	 **attackbox here**
    sprite('Action_228_07', 4)	# 363-366	 **attackbox here**
    sprite('Action_228_09', 14)	# 367-380	 **attackbox here**
    gotoLabel(11)
    label(14)
    sprite('Action_228_10', 3)	# 381-383	 **attackbox here**
    sprite('Action_228_11', 3)	# 384-386	 **attackbox here**
    sprite('Action_228_12', 5)	# 387-391	 **attackbox here**
    sprite('Action_228_13', 13)	# 392-404	 **attackbox here**
    SFX_0('210_down_garden_1')
    sprite('Action_228_14', 4)	# 405-408
    sprite('Action_228_15', 5)	# 409-413
    sprite('Action_228_16', 3)	# 414-416
    sprite('Action_445_08', 3)	# 417-419
    sprite('Action_445_07', 3)	# 420-422
    SFX_1('umi160_1')
    sprite('Action_445_05', 3)	# 423-425
    sprite('Action_445_06', 32767)	# 426-33192

@State
def UltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(100)
        Unknown11091(20)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2073(1)
        setInvincible(1)

        def upon_78():
            Hitstop(0)
            Unknown13024(0)
            enterState('UltimateAssaultOD_catch')
            Unknown11069('UltimateAssaultOD_catch')
    sprite('Action_222_00', 5)	# 1-5
    sprite('Action_222_01', 5)	# 6-10
    Unknown23024(1)
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'umi250_0', 'umi250_1', '', '')
    sprite('Action_222_02', 5)	# 11-15
    sprite('Action_222_03', 5)	# 16-20
    sprite('Action_222_04', 5)	# 21-25
    sprite('Action_222_05', 5)	# 26-30
    sprite('Action_222_06', 5)	# 31-35
    sprite('Action_222_07', 5)	# 36-40
    sprite('Action_222_08', 5)	# 41-45
    sprite('Action_222_09', 24)	# 46-69
    sprite('Action_222_10ex', 4)	# 70-73	 **attackbox here**
    GFX_0('EffUltimateAssault_01', -1)
    tag_voice(0, 'umi251_0', 'umi251_1', '', '')
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_222_11ex', 4)	# 74-77	 **attackbox here**
    setInvincible(0)
    Unknown1019(70)
    YAccel(70)
    sprite('Action_222_12ex', 4)	# 78-81	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    sprite('Action_223_00', 4)	# 82-85
    Unknown13024(1)
    Unknown1019(10)
    YAccel(10)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    sprite('Action_223_01', 4)	# 86-89
    setInvincible(0)
    sprite('Action_223_02', 4)	# 90-93
    sprite('Action_223_03', 3)	# 94-96
    sprite('Action_223_04', 3)	# 97-99
    sprite('Action_223_05', 2)	# 100-101
    sprite('Action_223_06', 3)	# 102-104
    sprite('Action_223_07', 2)	# 105-106
    sprite('Action_223_08', 3)	# 107-109	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    RefreshMultihit()
    AttackP2(60)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7000)
    AirPushbackY(-40000)
    Unknown9190(1)
    Unknown9118(80)
    Unknown9310(-1)
    Hitstop(8)
    Unknown11064(0)
    Unknown2073(0)
    physicsXImpulse(50000)
    physicsYImpulse(-60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_223_09', 3)	# 110-112	 **attackbox here**
    sprite('Action_223_10', 3)	# 113-115	 **attackbox here**
    sprite('Action_223_11', 5)	# 116-120	 **attackbox here**
    label(109)
    sprite('Action_223_12', 5)	# 121-125
    GFX_0('EffGroundBreak03', 0)
    Unknown1084(1)
    SFX_0('016_explode_2')
    ScreenShake(0, 20000)
    sprite('Action_224_00', 5)	# 126-130
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 111)
    sprite('Action_224_01', 5)	# 131-135
    sprite('Action_224_02', 5)	# 136-140
    sprite('Action_224_03', 5)	# 141-145
    sprite('Action_224_04', 4)	# 146-149
    label(110)
    sprite('Action_224_05', 3)	# 150-152
    sprite('Action_224_06', 3)	# 153-155
    loopRest()
    gotoLabel(110)
    label(111)
    sprite('Action_224_07', 5)	# 156-160
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_224_08', 6)	# 161-166
    sprite('Action_224_09', 5)	# 167-171

@State
def AirUltimateAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(100)
        Unknown11091(20)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2073(1)
        Unknown11072(1, 100000, 150000)
        SLOT_5 = 1
        setInvincible(1)

        def upon_78():
            Hitstop(0)
            Unknown13024(0)
            enterState('UltimateAssaultOD_catch')
            Unknown11069('UltimateAssaultOD_catch')
    sprite('Action_262_00', 5)	# 1-5
    Unknown1084(1)
    sprite('Action_262_01', 3)	# 6-8
    Unknown23024(1)
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown30080('')
    tag_voice(1, 'umi250_0', 'umi250_1', '', '')
    Unknown1007(5000)
    sprite('Action_262_02', 3)	# 9-11
    sprite('Action_262_03', 3)	# 12-14
    sprite('Action_262_04', 3)	# 15-17
    sprite('Action_262_03', 3)	# 18-20
    sprite('Action_262_04', 3)	# 21-23
    sprite('Action_262_03', 3)	# 24-26
    sprite('Action_262_04', 3)	# 27-29
    sprite('Action_262_03', 3)	# 30-32
    sprite('Action_262_04', 3)	# 33-35
    sprite('Action_262_03', 3)	# 36-38
    sprite('Action_262_07', 3)	# 39-41
    sprite('Action_164_00', 5)	# 42-46
    sprite('Action_164_01', 5)	# 47-51
    sprite('Action_164_02', 5)	# 52-56
    sprite('Action_177_00', 5)	# 57-61
    sprite('Action_177_01', 8)	# 62-69
    sprite('Action_222_10ex', 4)	# 70-73	 **attackbox here**
    GFX_0('EffUltimateAssault_01', -1)
    tag_voice(0, 'umi251_0', 'umi251_1', '', '')
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_222_11ex', 4)	# 74-77	 **attackbox here**
    setInvincible(0)
    Unknown1019(70)
    YAccel(70)
    sprite('Action_222_12ex', 4)	# 78-81	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    sprite('Action_223_00', 4)	# 82-85
    Unknown13024(1)
    Unknown1019(10)
    YAccel(10)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    sprite('Action_223_01', 4)	# 86-89
    setInvincible(0)
    sprite('Action_223_02', 4)	# 90-93
    sprite('Action_223_03', 3)	# 94-96
    sprite('Action_223_04', 3)	# 97-99
    sprite('Action_223_05', 2)	# 100-101
    sprite('Action_223_06', 3)	# 102-104
    sprite('Action_223_07', 2)	# 105-106
    sprite('Action_223_08', 3)	# 107-109	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    RefreshMultihit()
    AttackP2(60)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7000)
    AirPushbackY(-40000)
    Unknown9190(1)
    Unknown9118(80)
    Unknown9310(-1)
    Hitstop(8)
    Unknown11064(0)
    Unknown2073(0)
    physicsXImpulse(50000)
    physicsYImpulse(-60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_223_09', 3)	# 110-112	 **attackbox here**
    sprite('Action_223_10', 3)	# 113-115	 **attackbox here**
    sprite('Action_223_11', 5)	# 116-120	 **attackbox here**
    label(108)
    sprite('Action_223_08', 3)	# 121-123	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    sprite('Action_223_09', 3)	# 124-126	 **attackbox here**
    sprite('Action_223_10', 3)	# 127-129	 **attackbox here**
    sprite('Action_223_11', 5)	# 130-134	 **attackbox here**
    gotoLabel(108)
    label(109)
    sprite('Action_223_12', 5)	# 135-139
    GFX_0('EffGroundBreak03', 0)
    Unknown1084(1)
    SFX_0('016_explode_2')
    ScreenShake(0, 20000)
    sprite('Action_224_00', 5)	# 140-144
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 111)
    sprite('Action_224_01', 5)	# 145-149
    sprite('Action_224_02', 5)	# 150-154
    sprite('Action_224_03', 5)	# 155-159
    sprite('Action_224_04', 4)	# 160-163
    label(110)
    sprite('Action_224_05', 3)	# 164-166
    sprite('Action_224_06', 3)	# 167-169
    loopRest()
    gotoLabel(110)
    label(111)
    sprite('Action_224_07', 5)	# 170-174
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_224_08', 6)	# 175-180
    sprite('Action_224_09', 5)	# 181-185

@State
def UltimateAssaultOD_catch():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssaultOD_exe_1', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(180)
        AttackP2(100)
        Unknown11091(20)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown20003(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultOD_exe_1')
        Unknown11064(1)
        Unknown11023(1)
    sprite('Action_225_00', 4)	# 1-4	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('UltimateAssaultLookAtMeCamera', -1)
    physicsXImpulse(0)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('keep', 1)	# 5-5
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssaultOD_exe_1():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP2(100)
        Unknown11091(20)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown2037(4)

        def upon_3():
            if (not SLOT_2):
                sendToLabel(1)
    label(0)
    sprite('Action_225_00', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    ScreenShake(0, 8000)
    physicsXImpulse(1000)
    physicsYImpulse(60000)
    setGravity(100)
    RefreshMultihit()
    Damage(180)
    PushbackX(60000)
    Hitstop(0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown2038(-1)
    Unknown30048(1)
    Unknown11023(1)
    sprite('Action_225_01', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_225_03', 45)	# 11-55	 **attackbox here**
    clearUponHandler(3)
    Unknown2034(0)
    Unknown2053(0)
    RefreshMultihit()
    Unknown30079(0)
    physicsXImpulse(50000)
    physicsYImpulse(50000)
    setGravity(100)
    AirPushbackX(100)
    AirPushbackY(5000)
    YImpluseBeforeWallbounce(50)
    PushbackX(60000)
    Hitstop(0)
    AirUntechableTime(120)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    Unknown30048(1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008913000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('Action_225_03', 5)	# 56-60	 **attackbox here**
    StartMultihit()
    Unknown11069('UltimateAssaultOD_exe_1_ranbu')
    enterState('UltimateAssaultOD_exe_1_ranbu')

@State
def UltimateAssaultOD_exe_1_ranbu():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown1084(1)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11064(1)
        Unknown11108('03000000')

        def upon_43():
            if (SLOT_48 == 5101):
                sendToLabel(1)
    sprite('null', 6)	# 1-6
    SFX_4('umi253')
    GFX_0('UltimateAssaultOD_ranbu', -1)
    sprite('null', 32767)	# 7-32773
    label(1)
    sprite('keep', 1)	# 32774-32774
    enterState('UltimateAssaultOD_catch_2')

@State
def UltimateAssaultOD_catch_2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssaultOD_exe_2', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(180)
        AttackP2(100)
        Unknown11091(20)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultOD_exe_2')
        Unknown11064(1)
    sprite('null', 1)	# 1-1
    Unknown1086(22)
    teleportRelativeX(-5000)
    Unknown1007(5000)
    sprite('Action_226_01', 1)	# 2-2	 **attackbox here**
    GFX_0('EffUltimateAssault_05', -1)
    physicsXImpulse(0)
    physicsYImpulse(-5000)
    setGravity(100)
    SFX_0('005_swing_grap_2_2')
    sprite('keep', 1)	# 3-3
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssaultOD_exe_2():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP2(100)
        Unknown11091(20)
        setInvincible(1)
        Unknown30079(1)
        Unknown11064(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11108('03000000')
        Unknown2037(9)
        Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008a13000000000000')

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown20000(0)
                Unknown26('UltimateAssaultLookAtMeCamera')
    label(1)
    sprite('Action_226_01', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_06', -1)
    ScreenShake(0, 8000)
    clearUponHandler(78)
    physicsXImpulse(1000)
    physicsYImpulse(-70000)
    setGravity(100)
    RefreshMultihit()
    Damage(180)
    PushbackX(60000)
    Hitstop(0)
    Unknown30048(1)
    Unknown11023(1)
    sendToLabelUpon(2, 9)
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_226_02', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_227_00', 12)	# 11-22	 **attackbox here**
    GFX_0('EffGroundBreak03', -1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008b13000000000000')
    Unknown20000(1)
    Unknown4004('6566666563745f3338305f430000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f3338325f430000000000000000000000000000000000000000ffff0000')
    Unknown30079(0)
    RefreshMultihit()
    Unknown1084(1)
    clearUponHandler(2)
    Damage(3000)
    AirPushbackX(3000)
    AirPushbackY(100000)
    AttackP1(80)
    AttackP2(60)
    Unknown11091(35)
    AirUntechableTime(120)
    Unknown9310(30)
    Unknown11064(0)
    SFX_0('016_explode_2')
    sprite('Action_227_01', 40)	# 23-62	 **attackbox here**
    Unknown48('19000000020000003300000016000000020000004b000000')
    Unknown48('19000000020000003400000017000000020000004b000000')
    Unknown20003(0)
    sprite('Action_227_02', 1)	# 63-63	 **attackbox here**
    if (not SLOT_51):
        if (not SLOT_52):
            sendToLabel(10)
    sprite('Action_228_00', 4)	# 64-67	 **attackbox here**
    sprite('Action_228_01', 4)	# 68-71	 **attackbox here**
    sprite('Action_228_02', 4)	# 72-75	 **attackbox here**
    sprite('Action_228_03', 4)	# 76-79	 **attackbox here**
    sprite('Action_228_04', 10)	# 80-89	 **attackbox here**
    sprite('Action_228_05', 4)	# 90-93	 **attackbox here**
    sprite('Action_228_06', 14)	# 94-107	 **attackbox here**
    tag_voice(0, 'umi252_0', 'umi252_1', '', '')
    sprite('Action_228_07', 4)	# 108-111	 **attackbox here**
    sprite('Action_228_09', 14)	# 112-125	 **attackbox here**
    Unknown13024(1)
    sprite('Action_228_10', 3)	# 126-128	 **attackbox here**
    sprite('Action_228_11', 3)	# 129-131	 **attackbox here**
    sprite('Action_228_12', 5)	# 132-136	 **attackbox here**
    sprite('Action_228_13', 13)	# 137-149	 **attackbox here**
    Unknown20000(0)
    setInvincible(0)
    Unknown2053(1)
    sprite('Action_228_14', 4)	# 150-153
    sprite('Action_228_15', 5)	# 154-158
    sprite('Action_228_16', 3)	# 159-161
    ExitState()
    label(10)
    sprite('Action_228_00', 60)	# 162-221	 **attackbox here**
    Unknown23024(0)
    Unknown18010()
    sprite('Action_228_05', 5)	# 222-226	 **attackbox here**
    SFX_1('umi252_1')

    def upon_3():
        Unknown2038(1)
        if (SLOT_2 >= 120):
            clearUponHandler(3)
            Unknown21011(100)
            if random_(2, 0, 5):
                sendToLabel(14)
            else:
                SFX_1('umi252_0')
    label(11)
    sprite('Action_228_00', 20)	# 227-246	 **attackbox here**
    sprite('Action_228_00', 25)	# 247-271	 **attackbox here**
    random_(2, 0, 16)
    if SLOT_0:
        _gotolabel(12)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(13)
    sprite('Action_228_00', 50)	# 272-321	 **attackbox here**
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(12)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(13)
    gotoLabel(11)
    label(12)
    sprite('Action_228_01', 4)	# 322-325	 **attackbox here**
    sprite('Action_228_02', 4)	# 326-329	 **attackbox here**
    sprite('Action_228_03', 4)	# 330-333	 **attackbox here**
    sprite('Action_228_04', 10)	# 334-343	 **attackbox here**
    gotoLabel(11)
    label(13)
    sprite('Action_228_05', 5)	# 344-348	 **attackbox here**
    sprite('Action_228_06', 14)	# 349-362	 **attackbox here**
    sprite('Action_228_07', 4)	# 363-366	 **attackbox here**
    sprite('Action_228_09', 14)	# 367-380	 **attackbox here**
    gotoLabel(11)
    label(14)
    sprite('Action_228_10', 3)	# 381-383	 **attackbox here**
    sprite('Action_228_11', 3)	# 384-386	 **attackbox here**
    sprite('Action_228_12', 5)	# 387-391	 **attackbox here**
    sprite('Action_228_13', 13)	# 392-404	 **attackbox here**
    SFX_0('210_down_garden_1')
    sprite('Action_228_14', 4)	# 405-408
    sprite('Action_228_15', 5)	# 409-413
    sprite('Action_228_16', 3)	# 414-416
    sprite('Action_445_08', 3)	# 417-419
    sprite('Action_445_07', 3)	# 420-422
    SFX_1('umi160_1')
    sprite('Action_445_05', 3)	# 423-425
    sprite('Action_445_06', 32767)	# 426-33192

@State
def UltimateThrow():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowExe_1', 3, 0, 0)
        Unknown23055('')
        Unknown11054(170000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('UltimateThrowExe_1')
        Unknown1084(1)
    sprite('Action_261_00', 2)	# 1-2
    sprite('Action_261_01', 2)	# 3-4
    sprite('Action_261_02', 2)	# 5-6
    sprite('Action_261_03', 3)	# 7-9
    sprite('Action_261_04', 3)	# 10-12
    sprite('Action_261_05', 60)	# 13-72
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    sprite('Action_440_01', 1)	# 73-73	 **attackbox here**
    sprite('Action_440_02', 4)	# 74-77
    setInvincible(0)
    sprite('Action_440_03', 3)	# 78-80
    SFX_4('umi154')
    sprite('Action_440_04', 3)	# 81-83
    sprite('Action_440_05', 3)	# 84-86
    sprite('Action_440_06', 3)	# 87-89
    sprite('Action_440_07', 1)	# 90-90
    physicsXImpulse(30000)
    sprite('Action_440_08', 1)	# 91-91
    sprite('Action_440_09', 1)	# 92-92
    sprite('Action_440_10', 1)	# 93-93
    sprite('Action_440_11', 3)	# 94-96
    SFX_0('209_down_normal_0')
    Unknown1019(30)
    sprite('Action_440_12', 4)	# 97-100
    physicsXImpulse(0)
    sprite('Action_440_13', 5)	# 101-105
    sprite('Action_440_14', 5)	# 106-110
    sprite('Action_440_15', 5)	# 111-115
    sprite('Action_440_16', 11)	# 116-126
    sprite('Action_440_17', 4)	# 127-130
    SLOT_4 = 1

@State
def UltimateThrowExe_1():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(240)
        Unknown9142(210)
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowExe_2')
        Unknown30048(1)
        setInvincible(1)
        Unknown13024(0)
        Unknown30068(1)
        sendToLabelUpon(2, 0)
        Unknown28(8, 'UltimateThrowExe_2')
        Unknown20000(1)
    sprite('Action_441_00', 5)	# 1-5	 **attackbox here**
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_441_01', 2)	# 6-7
    sprite('Action_441_02', 5)	# 8-12
    sprite('Action_441_03', 4)	# 13-16	 **attackbox here**
    tag_voice(1, 'umi254_0', 'umi254_1', 'umi254_2', '')
    physicsXImpulse(22000)
    physicsYImpulse(8000)
    setGravity(2000)
    SFX_0('005_swing_grap_2_0')
    sprite('Action_441_04', 28)	# 17-44
    label(0)
    sprite('Action_441_05', 5)	# 45-49
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    loopRest()

@State
def UltimateThrowExe_2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(180)
        AirPushbackX(3000)
        AirPushbackY(31000)
        YImpluseBeforeWallbounce(1200)
        Unknown9310(30)
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowExe_3')
        Unknown30048(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_LANDING():
            enterState('UltimateThrowExe_3')
        Unknown20000(1)
        SLOT_60 = 0
    sprite('Action_442_00', 6)	# 1-6
    GFX_0('EffUltimateThrowExe_2', 100)
    sprite('Action_442_01', 7)	# 7-13
    sprite('Action_442_02', 7)	# 14-20

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(1)
    sprite('Action_442_02', 5)	# 21-25

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(2)
    sprite('Action_442_02', 3)	# 26-28

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(3)
    sprite('Action_442_03', 2)	# 29-30
    label(1)
    sprite('Action_442_04', 3)	# 31-33
    GFX_0('EffUltimateThrow_01', -1)
    tag_voice(0, 'umi255_0', 'umi255_1', 'umi255_2', '')
    Unknown21015('456666556c74696d6174655468726f774578655f3200000000000000000000007117000000000000')
    clearUponHandler(3)
    Damage(2000)
    physicsXImpulse(8000)
    physicsYImpulse(10000)
    setGravity(1600)
    SFX_0('005_swing_grap_2_1')
    sprite('Action_442_05', 4)	# 34-37	 **attackbox here**
    sprite('Action_442_08', 8)	# 38-45
    sprite('Action_442_09', 4)	# 46-49
    ExitState()
    label(2)
    sprite('Action_442_04', 3)	# 50-52
    GFX_0('EffUltimateThrow_01', -1)
    tag_voice(0, 'umi255_0', 'umi255_1', 'umi255_2', '')
    Unknown21015('456666556c74696d6174655468726f774578655f3200000000000000000000007117000000000000')
    clearUponHandler(3)
    Damage(2500)
    physicsXImpulse(8000)
    physicsYImpulse(10000)
    setGravity(1600)
    SFX_0('005_swing_grap_2_1')
    Unknown20009(850)
    sprite('Action_442_06', 4)	# 53-56	 **attackbox here**
    sprite('Action_442_08', 8)	# 57-64
    sprite('Action_442_09', 4)	# 65-68
    ExitState()
    label(3)
    sprite('Action_442_04', 3)	# 69-71
    GFX_0('EffUltimateThrow_01', -1)
    tag_voice(0, 'umi255_0', 'umi255_1', 'umi255_2', '')
    Unknown21015('456666556c74696d6174655468726f774578655f3200000000000000000000007117000000000000')
    SLOT_60 = 1
    clearUponHandler(3)
    Damage(3000)
    physicsXImpulse(8000)
    physicsYImpulse(10000)
    setGravity(1600)
    SFX_0('005_swing_grap_2_1')
    Unknown20009(700)
    sprite('Action_442_07', 4)	# 72-75	 **attackbox here**
    sprite('Action_442_08', 8)	# 76-83
    sprite('Action_442_09', 4)	# 84-87
    ExitState()

@State
def UltimateThrowExe_3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(50)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(60)
        AirUntechableTime(180)
        AirPushbackX(90000)
        AirPushbackY(35000)
        Unknown11072(1, 100000, 200000)
        Unknown11023(1)
        Unknown11064(0)
        Unknown30048(1)
        setInvincible(1)
        Unknown13024(0)
        Unknown20000(1)
    sprite('Action_443_00', 5)	# 1-5
    Unknown8000(100, 1, 1)
    sprite('Action_443_01', 5)	# 6-10
    sprite('Action_443_02', 4)	# 11-14
    GFX_0('EffUltimateThrowExe_3', 100)
    sprite('Action_443_03', 3)	# 15-17
    GFX_0('EffUltimateThrow_02', 0)
    sprite('Action_443_04', 3)	# 18-20
    if CheckInput(0xed):
        SLOT_51 = (SLOT_51 + 1)
    sprite('Action_443_05', 3)	# 21-23
    sprite('Action_443_06', 3)	# 24-26

    def upon_3():
        if SLOT_51:
            sendToLabel(1)
    sprite('Action_443_07', 1)	# 27-27
    sprite('Action_443_07', 2)	# 28-29

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(2)
    sprite('Action_443_08', 3)	# 30-32
    sprite('Action_443_09', 1)	# 33-33
    sprite('Action_443_09', 2)	# 34-35

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(3)
    sprite('Action_443_10', 1)	# 36-36
    label(1)
    sprite('Action_443_10', 2)	# 37-38
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    Damage(2000)
    clearUponHandler(3)
    sprite('Action_443_11', 4)	# 39-42
    sprite('Action_443_12', 4)	# 43-46	 **attackbox here**
    GFX_0('EffUltimateThrow_03_1', 0)
    SFX_0('016_explode_1')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 47-56
    physicsXImpulse(-18000)
    sprite('Action_444_00', 5)	# 57-61
    Unknown8000(100, 1, 1)
    physicsXImpulse(-1000)
    sprite('Action_444_01', 4)	# 62-65
    sprite('Action_444_02', 6)	# 66-71
    physicsXImpulse(-10000)
    sprite('Action_444_03', 5)	# 72-76
    sprite('Action_444_04', 4)	# 77-80
    Unknown8000(100, 1, 1)
    physicsXImpulse(-1000)
    sprite('Action_444_05', 6)	# 81-86
    sprite('Action_444_06', 5)	# 87-91
    Unknown13024(1)
    tag_voice(0, 'umi257_0', 'umi257_1', 'umi257_2', '')
    physicsXImpulse(-10000)
    sprite('Action_444_07', 4)	# 92-95
    sprite('Action_444_08', 4)	# 96-99
    sprite('Action_444_09', 4)	# 100-103
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_444_10', 4)	# 104-107
    sprite('Action_444_11', 8)	# 108-115
    sprite('Action_444_12', 3)	# 116-118
    sprite('Action_444_13', 3)	# 119-121
    sprite('Action_444_14', 2)	# 122-123
    ExitState()
    label(2)
    sprite('Action_443_10', 2)	# 124-125
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    Damage(2500)
    Unknown20009(850)
    clearUponHandler(3)
    sprite('Action_443_11', 4)	# 126-129
    sprite('Action_443_13', 4)	# 130-133	 **attackbox here**
    GFX_0('EffUltimateThrow_03_2', 0)
    SFX_0('016_explode_1')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 134-143
    physicsXImpulse(-20000)
    sprite('Action_445_00', 5)	# 144-148
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_445_01', 5)	# 149-153
    sprite('Action_445_02', 3)	# 154-156
    sprite('Action_445_03', 3)	# 157-159
    sprite('Action_445_04', 4)	# 160-163
    sprite('Action_445_06', 20)	# 164-183
    Unknown13024(1)
    sprite('Action_445_07', 4)	# 184-187
    sprite('Action_445_08', 3)	# 188-190
    ExitState()
    label(3)
    if SLOT_60:
        sendToLabel(4)
    clearUponHandler(3)
    sprite('Action_443_10', 2)	# 191-192
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    Damage(3000)
    Hitstop(30)
    Unknown20009(700)
    clearUponHandler(3)
    sprite('Action_443_11', 4)	# 193-196
    sprite('Action_443_14', 4)	# 197-200	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    SFX_0('016_explode_1')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 201-210
    physicsXImpulse(-20000)
    sprite('Action_445_00', 5)	# 211-215
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_445_01', 5)	# 216-220
    sprite('Action_445_02', 3)	# 221-223
    sprite('Action_445_03', 3)	# 224-226
    sprite('Action_445_04', 4)	# 227-230
    sprite('Action_445_06', 20)	# 231-250
    Unknown13024(1)
    sprite('Action_445_07', 4)	# 251-254
    sprite('Action_445_08', 3)	# 255-257
    ExitState()
    label(4)
    sprite('Action_443_10', 60)	# 258-317
    Unknown2036(60, -1, 0)
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    Damage(3500)
    Hitstop(30)
    Unknown20009(700)
    clearUponHandler(3)
    sprite('Action_443_11', 4)	# 318-321
    sprite('Action_443_14', 4)	# 322-325	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    SFX_0('016_explode_1')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 326-335
    physicsXImpulse(-20000)
    sprite('Action_445_00', 5)	# 336-340
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_445_01', 5)	# 341-345
    sprite('Action_445_02', 3)	# 346-348
    sprite('Action_445_03', 3)	# 349-351
    sprite('Action_445_04', 4)	# 352-355
    sprite('Action_445_06', 20)	# 356-375
    Unknown13024(1)
    sprite('Action_445_07', 4)	# 376-379
    sprite('Action_445_08', 3)	# 380-382

@State
def UltimateThrowOD():

    def upon_IMMEDIATE():
        Unknown17011('UltimateThrowODExe_1', 3, 0, 0)
        Unknown23055('')
        Unknown11054(170000)
        Unknown11032('80ee360001000000ffffffffffffffff')
        Unknown2018(0, 80)
        setInvincible(1)
        Unknown30048(1)
        AttackP1(100)
        AttackP2(100)
        Unknown11069('UltimateThrowODExe_1')
        Unknown1084(1)
    sprite('Action_261_00', 2)	# 1-2
    sprite('Action_261_01', 2)	# 3-4
    sprite('Action_261_02', 2)	# 5-6
    sprite('Action_261_03', 3)	# 7-9
    sprite('Action_261_04', 3)	# 10-12
    sprite('Action_261_05', 60)	# 13-72
    Unknown2036(60, -1, 0)
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown30080('')
    sprite('Action_440_01', 1)	# 73-73	 **attackbox here**
    sprite('Action_440_02', 4)	# 74-77
    setInvincible(0)
    sprite('Action_440_03', 3)	# 78-80
    SFX_4('umi154')
    sprite('Action_440_04', 3)	# 81-83
    sprite('Action_440_05', 3)	# 84-86
    sprite('Action_440_06', 3)	# 87-89
    sprite('Action_440_07', 1)	# 90-90
    physicsXImpulse(30000)
    sprite('Action_440_08', 1)	# 91-91
    sprite('Action_440_09', 1)	# 92-92
    sprite('Action_440_10', 1)	# 93-93
    sprite('Action_440_11', 3)	# 94-96
    SFX_0('209_down_normal_0')
    Unknown1019(30)
    sprite('Action_440_12', 4)	# 97-100
    physicsXImpulse(0)
    sprite('Action_440_13', 5)	# 101-105
    sprite('Action_440_14', 5)	# 106-110
    sprite('Action_440_15', 5)	# 111-115
    sprite('Action_440_16', 11)	# 116-126
    sprite('Action_440_17', 4)	# 127-130
    SLOT_4 = 1

@State
def UltimateThrowODExe_1():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(240)
        Unknown9142(210)
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowODExe_2')
        Unknown30048(1)
        setInvincible(1)
        Unknown13024(0)
        Unknown30068(1)
        sendToLabelUpon(2, 0)
        Unknown28(8, 'UltimateThrowODExe_2')
        Unknown20000(1)
    sprite('Action_441_00', 5)	# 1-5	 **attackbox here**
    StartMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('Action_441_01', 2)	# 6-7
    sprite('Action_441_02', 5)	# 8-12
    sprite('Action_441_03', 4)	# 13-16	 **attackbox here**
    tag_voice(1, 'umi254_0', 'umi254_1', 'umi254_2', '')
    physicsXImpulse(22000)
    physicsYImpulse(8000)
    setGravity(2000)
    SFX_0('005_swing_grap_2_0')
    sprite('Action_441_04', 28)	# 17-44
    label(0)
    sprite('Action_441_05', 5)	# 45-49
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    loopRest()

@State
def UltimateThrowODExe_2():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(180)
        AirPushbackX(3000)
        AirPushbackY(31000)
        YImpluseBeforeWallbounce(1200)
        Unknown9310(30)
        Unknown11023(1)
        Unknown11064(1)
        Unknown11069('UltimateThrowODExe_3')
        Unknown30048(1)
        setInvincible(1)
        Unknown13024(0)

        def upon_LANDING():
            enterState('UltimateThrowODExe_3')
        Unknown20000(1)
        SLOT_60 = 0
    sprite('Action_442_00', 6)	# 1-6
    GFX_0('EffUltimateThrowExe_2', 100)
    sprite('Action_442_01', 7)	# 7-13
    sprite('Action_442_02', 7)	# 14-20

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(1)
    sprite('Action_442_02', 5)	# 21-25

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(2)
    sprite('Action_442_02', 3)	# 26-28

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(3)
    sprite('Action_442_03', 2)	# 29-30
    label(1)
    sprite('Action_442_04', 3)	# 31-33
    GFX_0('EffUltimateThrow_01', -1)
    tag_voice(0, 'umi255_0', 'umi255_1', 'umi255_2', '')
    Unknown21015('456666556c74696d6174655468726f774578655f3200000000000000000000007117000000000000')
    clearUponHandler(3)
    Damage(2000)
    physicsXImpulse(8000)
    physicsYImpulse(10000)
    setGravity(1600)
    SFX_0('005_swing_grap_2_1')
    sprite('Action_442_05', 4)	# 34-37	 **attackbox here**
    sprite('Action_442_08', 8)	# 38-45
    sprite('Action_442_09', 4)	# 46-49
    ExitState()
    label(2)
    sprite('Action_442_04', 3)	# 50-52
    GFX_0('EffUltimateThrow_01', -1)
    tag_voice(0, 'umi255_0', 'umi255_1', 'umi255_2', '')
    Unknown21015('456666556c74696d6174655468726f774578655f3200000000000000000000007117000000000000')
    clearUponHandler(3)
    Damage(2500)
    physicsXImpulse(8000)
    physicsYImpulse(10000)
    setGravity(1600)
    Unknown20009(850)
    SFX_0('005_swing_grap_2_1')
    sprite('Action_442_06', 4)	# 53-56	 **attackbox here**
    sprite('Action_442_08', 8)	# 57-64
    sprite('Action_442_09', 4)	# 65-68
    ExitState()
    label(3)
    sprite('Action_442_04', 3)	# 69-71
    GFX_0('EffUltimateThrow_01', -1)
    tag_voice(0, 'umi255_0', 'umi255_1', 'umi255_2', '')
    Unknown21015('456666556c74696d6174655468726f774578655f3200000000000000000000007117000000000000')
    SLOT_60 = 1
    clearUponHandler(3)
    Damage(3000)
    physicsXImpulse(8000)
    physicsYImpulse(10000)
    setGravity(1600)
    Unknown20009(700)
    SFX_0('005_swing_grap_2_1')
    sprite('Action_442_07', 4)	# 72-75	 **attackbox here**
    sprite('Action_442_08', 8)	# 76-83
    sprite('Action_442_09', 4)	# 84-87
    ExitState()

@State
def UltimateThrowODExe_3():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Unknown11091(20)
        AttackP2(50)
        Unknown11092(1)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(180)
        AirPushbackY(2500)
        AirPushbackX(0)
        YImpluseBeforeWallbounce(100)
        Hitstop(3)
        Unknown11072(1, 100000, 200000)
        Unknown11023(1)
        Unknown11064(1)
        Unknown30048(1)
        setInvincible(1)
        Unknown13024(0)
        Unknown20000(1)
    sprite('Action_443_00', 5)	# 1-5
    Unknown8000(100, 1, 1)
    sprite('Action_443_01', 5)	# 6-10
    sprite('Action_443_02', 4)	# 11-14
    GFX_0('EffUltimateThrowExe_3', 100)
    sprite('Action_443_03', 3)	# 15-17
    GFX_0('EffUltimateThrow_02', 0)
    sprite('Action_443_04', 3)	# 18-20
    if CheckInput(0xed):
        SLOT_51 = (SLOT_51 + 1)
    sprite('Action_443_05', 3)	# 21-23
    sprite('Action_443_06', 3)	# 24-26

    def upon_3():
        if SLOT_51:
            sendToLabel(1)
    sprite('Action_443_07', 1)	# 27-27
    sprite('Action_443_07', 2)	# 28-29

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(2)
    sprite('Action_443_08', 3)	# 30-32
    sprite('Action_443_09', 1)	# 33-33
    sprite('Action_443_09', 2)	# 34-35

    def upon_3():
        if CheckInput(0xed):
            sendToLabel(3)
    sprite('Action_443_10', 1)	# 36-36
    label(1)
    sprite('Action_443_10', 2)	# 37-38
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    Damage(1300)
    clearUponHandler(3)
    sprite('Action_443_11', 4)	# 39-42
    sprite('Action_443_12', 4)	# 43-46	 **attackbox here**
    GFX_0('EffUltimateThrow_03_1', 0)
    Unknown11064(0)
    SFX_0('016_explode_2')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    sprite('Action_443_12', 4)	# 47-50	 **attackbox here**
    GFX_0('EffUltimateThrow_03_1', 0)
    RefreshMultihit()
    sprite('Action_443_12', 4)	# 51-54	 **attackbox here**
    GFX_0('EffUltimateThrow_03_1', 0)
    RefreshMultihit()
    sprite('Action_443_12', 4)	# 55-58	 **attackbox here**
    AirPushbackX(90000)
    AirPushbackY(35000)
    Hitstop(12)
    YImpluseBeforeWallbounce(1600)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(60)
    RefreshMultihit()
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 59-68
    physicsXImpulse(-18000)
    sprite('Action_444_00', 5)	# 69-73
    Unknown8000(100, 1, 1)
    physicsXImpulse(-1000)
    sprite('Action_444_01', 4)	# 74-77
    sprite('Action_444_02', 6)	# 78-83
    physicsXImpulse(-10000)
    sprite('Action_444_03', 5)	# 84-88
    sprite('Action_444_04', 4)	# 89-92
    Unknown8000(100, 1, 1)
    physicsXImpulse(-1000)
    sprite('Action_444_05', 6)	# 93-98
    sprite('Action_444_06', 5)	# 99-103
    Unknown13024(1)
    tag_voice(0, 'umi257_0', 'umi257_1', 'umi257_2', '')
    physicsXImpulse(-10000)
    sprite('Action_444_07', 4)	# 104-107
    sprite('Action_444_08', 4)	# 108-111
    sprite('Action_444_09', 4)	# 112-115
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_444_10', 4)	# 116-119
    sprite('Action_444_11', 8)	# 120-127
    sprite('Action_444_12', 3)	# 128-130
    sprite('Action_444_13', 3)	# 131-133
    sprite('Action_444_14', 2)	# 134-135
    ExitState()
    label(2)
    sprite('Action_443_10', 2)	# 136-137
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    Damage(1500)
    Unknown20009(850)
    clearUponHandler(3)
    sprite('Action_443_11', 4)	# 138-141
    sprite('Action_443_13', 4)	# 142-145	 **attackbox here**
    GFX_0('EffUltimateThrow_03_2', 0)
    Unknown11064(0)
    SFX_0('016_explode_2')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    sprite('Action_443_13', 4)	# 146-149	 **attackbox here**
    GFX_0('EffUltimateThrow_03_2', 0)
    RefreshMultihit()
    sprite('Action_443_13', 4)	# 150-153	 **attackbox here**
    GFX_0('EffUltimateThrow_03_2', 0)
    RefreshMultihit()
    sprite('Action_443_13', 4)	# 154-157	 **attackbox here**
    AirPushbackX(90000)
    AirPushbackY(35000)
    Hitstop(12)
    YImpluseBeforeWallbounce(1600)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(60)
    RefreshMultihit()
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 158-167
    physicsXImpulse(-20000)
    sprite('Action_445_00', 5)	# 168-172
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_445_01', 5)	# 173-177
    sprite('Action_445_02', 3)	# 178-180
    sprite('Action_445_03', 3)	# 181-183
    sprite('Action_445_04', 4)	# 184-187
    sprite('Action_445_06', 20)	# 188-207
    Unknown13024(1)
    sprite('Action_445_07', 4)	# 208-211
    sprite('Action_445_08', 3)	# 212-214
    ExitState()
    label(3)
    if SLOT_60:
        sendToLabel(4)
    clearUponHandler(3)
    sprite('Action_443_10', 2)	# 215-216
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    clearUponHandler(3)
    Unknown20009(700)
    sprite('Action_443_11', 4)	# 217-220
    sprite('Action_443_14', 4)	# 221-224	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    Unknown11064(0)
    SFX_0('016_explode_2')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    Damage(1700)
    AirPushbackX(90000)
    AirPushbackY(35000)
    YImpluseBeforeWallbounce(1600)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(60)
    sprite('Action_443_14', 4)	# 225-228	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    RefreshMultihit()
    sprite('Action_443_14', 4)	# 229-232	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    RefreshMultihit()
    sprite('Action_443_14', 4)	# 233-236	 **attackbox here**
    Hitstop(30)
    RefreshMultihit()
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 237-246
    physicsXImpulse(-20000)
    sprite('Action_445_00', 5)	# 247-251
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_445_01', 5)	# 252-256
    sprite('Action_445_02', 3)	# 257-259
    sprite('Action_445_03', 3)	# 260-262
    sprite('Action_445_04', 4)	# 263-266
    sprite('Action_445_06', 20)	# 267-286
    Unknown13024(1)
    sprite('Action_445_07', 4)	# 287-290
    sprite('Action_445_08', 3)	# 291-293
    ExitState()
    label(4)
    sprite('Action_443_10', 60)	# 294-353
    Unknown2036(60, -1, 0)
    Unknown21015('456666556c74696d6174655468726f774578655f3300000000000000000000007217000000000000')
    clearUponHandler(3)
    Unknown20009(700)
    sprite('Action_443_11', 4)	# 354-357
    sprite('Action_443_14', 4)	# 358-361	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    Unknown11064(0)
    SFX_0('016_explode_2')
    tag_voice(0, 'umi256_0', 'umi256_1', 'umi256_2', '')
    Damage(1900)
    AirPushbackX(90000)
    AirPushbackY(35000)
    YImpluseBeforeWallbounce(1600)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(60)
    Unknown20009(1000)
    sprite('Action_443_14', 4)	# 362-365	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    RefreshMultihit()
    sprite('Action_443_14', 4)	# 366-369	 **attackbox here**
    GFX_0('EffUltimateThrow_03_3', 0)
    RefreshMultihit()
    sprite('Action_443_14', 4)	# 370-373	 **attackbox here**
    Hitstop(30)
    RefreshMultihit()
    Unknown20000(0)
    sprite('Action_443_16', 10)	# 374-383
    physicsXImpulse(-20000)
    sprite('Action_445_00', 5)	# 384-388
    Unknown8000(100, 1, 1)
    physicsXImpulse(0)
    sprite('Action_445_01', 5)	# 389-393
    sprite('Action_445_02', 3)	# 394-396
    sprite('Action_445_03', 3)	# 397-399
    sprite('Action_445_04', 4)	# 400-403
    sprite('Action_445_06', 20)	# 404-423
    Unknown13024(1)
    sprite('Action_445_07', 4)	# 424-427
    sprite('Action_445_08', 3)	# 428-430

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Unknown17011('AstralHeat_Exe', 6, 0, 0)
        Unknown11054(150000)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11002(-1)
        Unknown30061(1)
        Unknown11107(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        Unknown23027()
        Unknown11064(1)

        def upon_78():
            clearUponHandler(1)
            clearUponHandler(78)
            setInvincible(1)
            Unknown23157(1)
            Unknown23088(1, 1)
            Unknown23084(1)
        sendToLabelUpon(2, 1)
        setInvincible(1)

        def upon_STATE_END():
            Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_261_00', 4)	# 1-4
    Unknown2006()
    Unknown1084(1)
    Unknown2036(95, -1, 2)
    Unknown23147()
    SFX_1('umi290')
    GFX_0('IWEXIST_CutIn', 100)
    Unknown4004('43616c6c5f556e6949574542470000000000000000000000000000000000000064000000')
    sprite('Action_261_01', 4)	# 5-8
    sprite('Action_261_02', 4)	# 9-12
    sprite('Action_261_03', 4)	# 13-16
    sprite('Action_261_04', 4)	# 17-20
    sprite('Action_261_05', 4)	# 21-24
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
    sprite('Action_261_11', 4)	# 73-76
    sprite('Action_261_12', 4)	# 77-80
    sprite('Action_198_00', 6)	# 81-86
    sprite('Action_198_01', 6)	# 87-92
    sprite('Action_198_02', 4)	# 93-96
    Unknown8000(100, 1, 1)
    physicsYImpulse(12000)
    SLOT_12 = SLOT_19
    Unknown1019(6)
    if (SLOT_12 >= 50000):
        SLOT_12 = 50000
        physicsYImpulse(14000)
    if (SLOT_12 <= 20000):
        SLOT_12 = 20000
        physicsYImpulse(8000)
    setGravity(2200)
    SFX_0('001_airbackdash_0')
    sprite('Action_198_03', 4)	# 97-100	 **attackbox here**
    sprite('Action_198_03', 32767)	# 101-32867	 **attackbox here**
    RefreshMultihit()
    label(1)
    sprite('Action_198_04', 3)	# 32868-32870	 **attackbox here**
    Unknown11107(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_198_05', 3)	# 32871-32873
    setInvincible(0)
    SFX_4('umi154')
    sprite('Action_198_06', 3)	# 32874-32876
    sprite('Action_198_05', 4)	# 32877-32880
    sprite('Action_198_06', 4)	# 32881-32884
    sprite('Action_198_05', 5)	# 32885-32889
    sprite('Action_198_06', 5)	# 32890-32894
    sprite('Action_198_08', 8)	# 32895-32902
    sprite('Action_198_09', 3)	# 32903-32905

@State
def AstralHeat_Exe():

    def upon_IMMEDIATE():
        Unknown17012(6, 0, 0)
        AttackLevel_(4)
        Damage(5000)
        Unknown11091(100)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(4000)
        AirPushbackY(22000)
        Hitstop(8)
        Unknown11001(-5, -5, -5)
        YImpluseBeforeWallbounce(10)
        AirUntechableTime(9999)
        Unknown11023(1)
        Unknown23027()
        Unknown11069('IWEXIST_FlyingVernier')
        Unknown11086(1)
        setInvincible(1)
        sendToLabelUpon(2, 1)

        def upon_43():
            if (SLOT_48 == 7001):
                sendToLabel(99)
        Unknown2019(-500)

        def upon_STATE_END():
            Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    sprite('Action_198_04', 32767)	# 1-32767	 **attackbox here**
    Unknown5000(10, 0)
    Unknown5001('0000000000000000040000000000000000000000')
    physicsXImpulse(22000)
    physicsYImpulse(-100)
    setGravity(2000)
    GFX_0('IWEXIST_Camera', 100)
    label(1)
    sprite('Action_201_01', 3)	# 32768-32770	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_201_02', 6)	# 32771-32776	 **attackbox here**
    Unknown5000(16, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('Action_201_03', 4)	# 32777-32780
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    Unknown2018(0, 80)
    sprite('Action_201_04', 3)	# 32781-32783
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_05', 6)	# 32784-32789
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_06', 6)	# 32790-32795
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_07', 6)	# 32796-32801
    SFX_1('umi291')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_201_09', 4)	# 32802-32805	 **attackbox here**
    GFX_0('IWEXIST_Canon', -1)
    SFX_3('SE051')
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    sprite('Action_201_10', 14)	# 32806-32819	 **attackbox here**
    Unknown1045(-30000)
    sprite('Action_201_11', 4)	# 32820-32823
    sprite('Action_201_12', 5)	# 32824-32828
    Unknown1084(1)
    sprite('Action_201_13', 5)	# 32829-32833
    sprite('Action_271_00', 10)	# 32834-32843
    sprite('Action_271_01', 4)	# 32844-32847
    sprite('Action_271_02', 3)	# 32848-32850
    physicsYImpulse(20000)
    setGravity(500)
    GFX_0('IWEXIST_JET', 100)
    GFX_0('IWEXIST_TakeOff', 100)
    SFX_3('SE052')
    sprite('Action_271_03', 4)	# 32851-32854
    sprite('Action_271_04', 4)	# 32855-32858
    sprite('Action_271_05', 4)	# 32859-32862
    sprite('Action_271_06', 4)	# 32863-32866
    physicsYImpulse(50000)
    setGravity(5000)
    sprite('Action_271_07', 4)	# 32867-32870
    sprite('Action_271_08', 4)	# 32871-32874
    physicsYImpulse(80000)
    setGravity(5000)
    sprite('Action_271_07', 4)	# 32875-32878
    sprite('Action_271_08', 4)	# 32879-32882
    Unknown1019(0)
    setGravity(0)
    Unknown3038(1)
    sprite('Action_271_09', 20)	# 32883-32902
    GFX_0('IWEXIST_BlackOut', 100)
    sprite('Action_271_09', 20)	# 32903-32922
    Unknown21013('43616c6c5f556e6949574542470000000000000000000000000000000000000020000000')
    Unknown2034(0)
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown36(22)
    Unknown1019(0)
    Unknown2034(0)
    Unknown1000(0)
    Unknown35()
    Unknown36(23)
    Unknown3038(1)
    Unknown35()
    sprite('Action_271_09', 30)	# 32923-32952
    GFX_0('IWEXIST_Anime', 100)
    sprite('Action_271_09', 32767)	# 32953-65719
    label(99)
    sprite('Action_274_00', 48)	# 65720-65767
    Unknown26('IWEXIST_BG')
    Unknown26('IWEXIST_FlyingMika')
    Unknown23024(0)
    clearUponHandler(2)
    Unknown1084(1)
    Unknown1000(-150000)
    teleportRelativeY(650000)
    setGravity(0)
    Unknown36(22)
    Unknown1000(150000)
    teleportRelativeY(68000)
    physicsYImpulse(-5800)
    Unknown1043()
    Unknown35()
    sprite('Action_274_01', 3)	# 65768-65770
    Unknown3038(0)
    physicsYImpulse(-25000)
    Unknown1043()
    sendToLabelUpon(2, 101)
    label(100)
    sprite('Action_274_02', 3)	# 65771-65773
    sprite('Action_274_03', 3)	# 65774-65776
    gotoLabel(100)
    label(101)
    sprite('Action_274_04', 4)	# 65777-65780
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_274_05', 4)	# 65781-65784
    sprite('Action_274_06', 4)	# 65785-65788

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
    sprite('Action_050_07', 5)	# 1-5
    sprite('Action_050_08', 8)	# 6-13
    sprite('Action_050_09', 3)	# 14-16
    sprite('Action_050_10', 60)	# 17-76	 **attackbox here**

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)
    sprite('null', 25)	# 1-25
    sprite('Action_008_00', 2)	# 26-27
    Unknown1086(22)
    teleportRelativeX(-300000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    physicsXImpulse(160000)
    physicsYImpulse(-100000)
    setGravity(0)
    sprite('Action_008_00', 3)	# 28-30
    sprite('Action_008_01', 3)	# 31-33
    sprite('Action_008_01', 32767)	# 34-32800
    label(9)
    sprite('Action_008_02', 3)	# 32801-32803	 **attackbox here**
    Unknown2017(1)
    Unknown2053(1)
    Unknown1019(30)
    sprite('Action_021_00', 3)	# 32804-32806
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_021_01', 12)	# 32807-32818
    sprite('Action_021_02', 7)	# 32819-32825

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_03', 2)	# 1-2
    sprite('Action_312_04', 26)	# 3-28
    sprite('Action_312_05', 4)	# 29-32
    sprite('Action_312_06', 4)	# 33-36
    sprite('Action_312_07', 4)	# 37-40
    sprite('Action_312_08', 4)	# 41-44
    sprite('Action_013_00', 4)	# 45-48
    sprite('Action_013_01', 4)	# 49-52
    sprite('Action_014_00', 4)	# 53-56
    sprite('Action_014_01', 4)	# 57-60
    sprite('Action_000_00', 30)	# 61-90	 **attackbox here**

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_045_03', 3)	# 1-3
    sprite('Action_045_04', 5)	# 4-8
    sprite('Action_045_05', 7)	# 9-15
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
    sprite('Action_020_00', 4)	# 3-6
    Unknown1019(95)
    sprite('Action_020_01', 4)	# 7-10
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
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AttackP1(70)
        Hitstop(6)
        AirPushbackX(14000)
        AirPushbackY(-25000)
        PushbackX(12000)
        Unknown9310(1)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(0)
        Unknown11042(1)
        Unknown11056(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('Action_148_00', 3)	# 1-3
    physicsYImpulse(26000)
    setGravity(1000)
    SLOT_12 = SLOT_19
    Unknown1019(2)
    if (SLOT_12 >= 23000):
        SLOT_12 = 23000
    sprite('Action_148_01', 3)	# 4-6
    sprite('Action_148_02', 3)	# 7-9
    sprite('Action_148_03', 3)	# 10-12
    sprite('Action_148_04', 3)	# 13-15
    sprite('Action_148_05', 3)	# 16-18
    sprite('Action_148_04', 3)	# 19-21
    sprite('Action_148_05', 3)	# 22-24
    sprite('Action_148_04', 3)	# 25-27
    sprite('Action_148_05', 3)	# 28-30
    sprite('Action_148_04', 3)	# 31-33
    sprite('Action_148_05', 3)	# 34-36
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(100)
    sprite('Action_148_06', 3)	# 37-39
    sprite('Action_148_07', 3)	# 40-42	 **attackbox here**
    GFX_0('EffNmlAtkJC_01', -1)
    GFX_0('EffNmlAtkJC_02', -1)
    GFX_0('EffNmlAtkJC_03', -1)
    tag_voice(1, 'umi110_0', 'umi110_1', 'umi110_2', '')
    physicsXImpulse(25000)
    physicsYImpulse(-40000)
    setGravity(1600)
    SFX_0('209_down_normal_0')
    label(0)
    sprite('Action_148_08', 3)	# 43-45	 **attackbox here**
    sprite('Action_148_09', 3)	# 46-48	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_148_10', 5)	# 49-53	 **attackbox here**
    GFX_0('EffGroundBreak01_Assist', 0)
    Unknown1084(1)
    ScreenShake(0, 15000)
    SFX_0('209_down_normal_0')
    sprite('Action_148_12', 10)	# 54-63
    Recovery()
    sprite('Action_149_00', 5)	# 64-68
    physicsXImpulse(-5000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 11)
    sprite('Action_149_01', 5)	# 69-73
    sprite('Action_149_02', 5)	# 74-78
    sprite('Action_149_03', 5)	# 79-83
    sprite('Action_149_04', 4)	# 84-87
    label(10)
    sprite('Action_149_05', 3)	# 88-90
    sprite('Action_149_06', 3)	# 91-93
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('Action_149_07', 4)	# 94-97
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_149_08', 4)	# 98-101
    sprite('Action_149_09', 4)	# 102-105

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirPushbackX(2000)
        AirPushbackY(38000)
        AirUntechableTime(50)
        Unknown11042(1)
    sprite('Action_003_00', 2)	# 1-2
    sprite('Action_003_01', 3)	# 3-5
    sprite('Action_003_02', 3)	# 6-8
    sprite('Action_003_03', 2)	# 9-10
    sprite('Action_003_04', 2)	# 11-12
    sprite('Action_003_05ex', 4)	# 13-16	 **attackbox here**
    GFX_0('EffNmlAtk5AAA', -1)
    GFX_0('EffNmlAtk5AAA_02', -1)
    tag_voice(1, 'umi106_0', 'umi106_1', 'umi106_2', '')
    SFX_0('024_getset_a')
    ScreenShake(0, 15000)
    sprite('Action_003_06', 13)	# 17-29
    Recovery()
    sprite('Action_003_07', 7)	# 30-36
    sprite('Action_003_08', 6)	# 37-42

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        Unknown11028(22)
        AirUntechableTime(50)
        AttackP1(70)
        Hitstop(12)
        AirPushbackX(2500)
        AirPushbackY(30000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown1084(1)
        Unknown11056(0)
        Unknown11042(1)
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('Action_160_00', 3)	# 1-3
    sprite('Action_160_01', 3)	# 4-6
    physicsYImpulse(1000)
    setGravity(10)
    sprite('Action_160_02', 2)	# 7-8
    sprite('Action_160_03', 2)	# 9-10
    sprite('Action_160_04', 2)	# 11-12
    sprite('Action_160_05ex', 1)	# 13-13	 **attackbox here**
    GFX_0('EffMissile_6', -1)
    GFX_0('EffMissile_Move', -1)
    Unknown23029(1, 2006, 0)
    tag_voice(1, 'umi200_0', 'umi200_1', 'umi200_2', '')
    Unknown2017(0)
    physicsXImpulse(74000)
    physicsYImpulse(0)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    SFX_0('000_airdash_0')
    sprite('Action_160_05ex', 3)	# 14-16	 **attackbox here**
    sprite('Action_160_06ex', 4)	# 17-20	 **attackbox here**
    sprite('Action_160_07ex', 4)	# 21-24	 **attackbox here**
    Unknown1019(30)
    sprite('Action_160_08ex', 4)	# 25-28	 **attackbox here**
    sprite('Action_160_09', 3)	# 29-31
    Unknown2017(1)
    Unknown26('EffMissile_Move')
    Unknown1019(20)
    setGravity(1600)
    Recovery()
    sprite('Action_160_10', 3)	# 32-34
    sprite('Action_160_11', 3)	# 35-37
    sprite('Action_160_12', 3)	# 38-40
    label(0)
    sprite('Action_160_13', 3)	# 41-43
    sprite('Action_160_14', 3)	# 44-46
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_168_00', 3)	# 47-49
    Unknown26('EffMissile_Move')
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_168_01', 3)	# 50-52
    sprite('Action_168_02', 3)	# 53-55

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
    Unknown2036(94, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('Action_020_00', 4)	# 3-6
    sprite('Action_020_01', 4)	# 7-10
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
        Unknown23056('')
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2073(1)
        setInvincible(1)

        def upon_78():
            Hitstop(0)
            Unknown13024(0)
            enterState('UltimateAssaultDDD_catch')
            Unknown11069('UltimateAssaultDDD_catch')
    sprite('Action_222_00', 8)	# 1-8
    sprite('Action_222_01', 5)	# 9-13
    sprite('Action_222_02', 5)	# 14-18
    sprite('Action_222_03', 5)	# 19-23
    sprite('Action_222_04', 5)	# 24-28
    sprite('Action_222_05', 5)	# 29-33
    sprite('Action_222_06', 5)	# 34-38
    sprite('Action_222_07', 5)	# 39-43
    sprite('Action_222_08', 5)	# 44-48
    sprite('Action_222_09', 21)	# 49-69
    sprite('Action_222_10ex', 4)	# 70-73	 **attackbox here**
    GFX_0('EffUltimateAssault_01', -1)
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_222_11ex', 4)	# 74-77	 **attackbox here**
    setInvincible(0)
    Unknown1019(70)
    YAccel(70)
    sprite('Action_222_12ex', 4)	# 78-81	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    sprite('Action_223_00', 4)	# 82-85
    Unknown1019(10)
    YAccel(10)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    sprite('Action_223_01', 4)	# 86-89
    setInvincible(0)
    sprite('Action_223_02', 4)	# 90-93
    sprite('Action_223_03', 3)	# 94-96
    sprite('Action_223_04', 3)	# 97-99
    sprite('Action_223_05', 2)	# 100-101
    sprite('Action_223_06', 3)	# 102-104
    sprite('Action_223_07', 2)	# 105-106
    sprite('Action_223_08', 3)	# 107-109	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    RefreshMultihit()
    Damage(1900)
    AttackP2(60)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7000)
    AirPushbackY(-40000)
    Unknown9190(1)
    Unknown9118(80)
    Unknown9310(-1)
    Hitstop(8)
    Unknown11064(0)
    Unknown2073(0)
    physicsXImpulse(50000)
    physicsYImpulse(-60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_223_09', 3)	# 110-112	 **attackbox here**
    sprite('Action_223_10', 3)	# 113-115	 **attackbox here**
    sprite('Action_223_11', 5)	# 116-120	 **attackbox here**
    label(109)
    sprite('Action_223_12', 5)	# 121-125
    GFX_0('EffGroundBreak03', 0)
    Unknown1084(1)
    SFX_0('016_explode_2')
    ScreenShake(0, 20000)
    sprite('Action_224_00', 5)	# 126-130
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 111)
    sprite('Action_224_01', 5)	# 131-135
    sprite('Action_224_02', 5)	# 136-140
    sprite('Action_224_03', 5)	# 141-145
    sprite('Action_224_04', 4)	# 146-149
    label(110)
    sprite('Action_224_05', 3)	# 150-152
    sprite('Action_224_06', 3)	# 153-155
    loopRest()
    gotoLabel(110)
    label(111)
    sprite('Action_224_07', 5)	# 156-160
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_224_08', 6)	# 161-166
    sprite('Action_224_09', 5)	# 167-171

@State
def UltimateAssaultDDD_catch():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssaultDDD_exe_1', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown20003(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultDDD_exe_1')
        Unknown11064(1)
        Unknown11023(1)
    sprite('Action_225_00', 4)	# 1-4	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('UltimateAssaultLookAtMeCamera', -1)
    physicsXImpulse(0)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('keep', 1)	# 5-5
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssaultDDD_exe_1():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown17012(3, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown2037(4)

        def upon_3():
            if (not SLOT_2):
                sendToLabel(1)
    label(0)
    sprite('Action_225_00', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    ScreenShake(0, 8000)
    physicsXImpulse(1000)
    physicsYImpulse(60000)
    setGravity(100)
    RefreshMultihit()
    Damage(100)
    PushbackX(60000)
    Hitstop(0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown2038(-1)
    Unknown30048(1)
    Unknown11023(1)
    sprite('Action_225_01', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_225_03', 60)	# 11-70	 **attackbox here**
    clearUponHandler(3)
    Unknown2034(0)
    Unknown2053(0)
    RefreshMultihit()
    Unknown30079(0)
    physicsXImpulse(50000)
    physicsYImpulse(50000)
    setGravity(100)
    AirPushbackX(100)
    AirPushbackY(5000)
    YImpluseBeforeWallbounce(50)
    PushbackX(60000)
    Hitstop(0)
    AirUntechableTime(120)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    Unknown30048(1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008913000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('Action_225_03', 5)	# 71-75	 **attackbox here**
    StartMultihit()
    Unknown11069('UltimateAssaultDDD_catch_2')
    enterState('UltimateAssaultDDD_catch_2')

@State
def UltimateAssaultDDD_catch_2():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssaultDDD_exe_2', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultDDD_exe_2')
        Unknown11064(1)
    sprite('null', 1)	# 1-1
    Unknown1086(22)
    teleportRelativeX(-5000)
    Unknown1007(5000)
    sprite('Action_226_01', 1)	# 2-2	 **attackbox here**
    GFX_0('EffUltimateAssault_05', -1)
    physicsXImpulse(0)
    physicsYImpulse(-5000)
    setGravity(100)
    SFX_0('005_swing_grap_2_2')
    sprite('keep', 1)	# 3-3
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssaultDDD_exe_2():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        setInvincible(1)
        Unknown30079(1)
        Unknown11064(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11108('03000000')
        Unknown2037(9)
        Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008a13000000000000')

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown20000(0)
                Unknown26('UltimateAssaultLookAtMeCamera')
    label(1)
    sprite('Action_226_01', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_06', -1)
    ScreenShake(0, 8000)
    clearUponHandler(78)
    physicsXImpulse(1000)
    physicsYImpulse(-70000)
    setGravity(100)
    RefreshMultihit()
    Damage(100)
    PushbackX(60000)
    Hitstop(0)
    Unknown30048(1)
    Unknown11023(1)
    sendToLabelUpon(2, 9)
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_226_02', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_227_00', 12)	# 11-22	 **attackbox here**
    GFX_0('EffGroundBreak03', -1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008b13000000000000')
    Unknown20000(1)
    Unknown4004('6566666563745f3338305f430000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f3338325f430000000000000000000000000000000000000000ffff0000')
    Unknown30079(0)
    RefreshMultihit()
    Unknown1084(1)
    clearUponHandler(2)
    Damage(700)
    AirPushbackX(3000)
    AirPushbackY(100000)
    AirUntechableTime(120)
    Unknown9310(30)
    Unknown11064(0)
    SFX_0('016_explode_2')
    sprite('Action_227_01', 40)	# 23-62	 **attackbox here**
    Unknown20003(0)
    sprite('Action_227_02', 1)	# 63-63	 **attackbox here**
    sprite('Action_228_00', 4)	# 64-67	 **attackbox here**
    sprite('Action_228_01', 4)	# 68-71	 **attackbox here**
    sprite('Action_228_02', 4)	# 72-75	 **attackbox here**
    sprite('Action_228_03', 4)	# 76-79	 **attackbox here**
    sprite('Action_228_04', 10)	# 80-89	 **attackbox here**
    sprite('Action_228_05', 4)	# 90-93	 **attackbox here**
    sprite('Action_228_06', 14)	# 94-107	 **attackbox here**
    tag_voice(1, 'umi252_0', 'umi252_1', '', '')
    sprite('Action_228_07', 4)	# 108-111	 **attackbox here**
    sprite('Action_228_09', 14)	# 112-125	 **attackbox here**
    sprite('Action_228_10', 3)	# 126-128	 **attackbox here**
    sprite('Action_228_11', 3)	# 129-131	 **attackbox here**
    sprite('Action_228_12', 5)	# 132-136	 **attackbox here**
    sprite('Action_228_13', 13)	# 137-149	 **attackbox here**
    Unknown20000(0)
    setInvincible(0)
    Unknown2053(1)
    sprite('Action_228_14', 4)	# 150-153
    sprite('Action_228_15', 5)	# 154-158
    sprite('Action_228_16', 3)	# 159-161

@State
def UltimateAssaultDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(12000)
        PushbackX(12000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown11056(0)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2073(1)
        setInvincible(1)

        def upon_78():
            Hitstop(0)
            Unknown13024(0)
            enterState('UltimateAssaultDDDOD_catch')
            Unknown11069('UltimateAssaultDDDOD_catch')
    sprite('Action_222_00', 8)	# 1-8
    sprite('Action_222_01', 5)	# 9-13
    sprite('Action_222_02', 5)	# 14-18
    sprite('Action_222_03', 5)	# 19-23
    sprite('Action_222_04', 5)	# 24-28
    sprite('Action_222_05', 5)	# 29-33
    sprite('Action_222_06', 5)	# 34-38
    sprite('Action_222_07', 5)	# 39-43
    sprite('Action_222_08', 5)	# 44-48
    sprite('Action_222_09', 21)	# 49-69
    sprite('Action_222_10ex', 4)	# 70-73	 **attackbox here**
    GFX_0('EffUltimateAssault_01', -1)
    physicsXImpulse(60000)
    physicsYImpulse(60000)
    setGravity(800)
    SFX_0('005_swing_grap_2_2')
    sprite('Action_222_11ex', 4)	# 74-77	 **attackbox here**
    setInvincible(0)
    Unknown1019(70)
    YAccel(70)
    sprite('Action_222_12ex', 4)	# 78-81	 **attackbox here**
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    sprite('Action_223_00', 4)	# 82-85
    Unknown1019(10)
    YAccel(10)
    clearUponHandler(2)
    sendToLabelUpon(2, 109)
    clearUponHandler(78)
    sprite('Action_223_01', 4)	# 86-89
    setInvincible(0)
    sprite('Action_223_02', 4)	# 90-93
    sprite('Action_223_03', 3)	# 94-96
    sprite('Action_223_04', 3)	# 97-99
    sprite('Action_223_05', 2)	# 100-101
    sprite('Action_223_06', 3)	# 102-104
    sprite('Action_223_07', 2)	# 105-106
    sprite('Action_223_08', 3)	# 107-109	 **attackbox here**
    GFX_0('EffUltimateAssault_02', -1)
    GFX_0('EffUltimateAssault_03', -1)
    RefreshMultihit()
    Damage(2400)
    AttackP2(60)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackX(7000)
    AirPushbackY(-40000)
    Unknown9190(1)
    Unknown9118(80)
    Unknown9310(-1)
    Hitstop(8)
    Unknown11064(0)
    Unknown2073(0)
    physicsXImpulse(50000)
    physicsYImpulse(-60000)
    setGravity(800)
    sprite('Action_223_09', 3)	# 110-112	 **attackbox here**
    sprite('Action_223_10', 3)	# 113-115	 **attackbox here**
    sprite('Action_223_11', 5)	# 116-120	 **attackbox here**
    label(109)
    sprite('Action_223_12', 5)	# 121-125
    GFX_0('EffGroundBreak03', 0)
    Unknown1084(1)
    SFX_0('016_explode_2')
    ScreenShake(0, 20000)
    sprite('Action_224_00', 5)	# 126-130
    physicsXImpulse(-6000)
    physicsYImpulse(20000)
    setGravity(1600)
    sendToLabelUpon(2, 111)
    sprite('Action_224_01', 5)	# 131-135
    sprite('Action_224_02', 5)	# 136-140
    sprite('Action_224_03', 5)	# 141-145
    sprite('Action_224_04', 4)	# 146-149
    label(110)
    sprite('Action_224_05', 3)	# 150-152
    sprite('Action_224_06', 3)	# 153-155
    loopRest()
    gotoLabel(110)
    label(111)
    sprite('Action_224_07', 5)	# 156-160
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    sprite('Action_224_08', 6)	# 161-166
    sprite('Action_224_09', 5)	# 167-171

@State
def UltimateAssaultDDDOD_catch():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAssaultDDDOD_exe_1', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown20003(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultDDDOD_exe_1')
        Unknown11064(1)
        Unknown11023(1)
    sprite('Action_225_00', 4)	# 1-4	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    GFX_0('UltimateAssaultLookAtMeCamera', -1)
    physicsXImpulse(0)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('keep', 1)	# 5-5
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssaultDDDOD_exe_1():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown2037(4)

        def upon_3():
            if (not SLOT_2):
                sendToLabel(1)
    label(0)
    sprite('Action_225_00', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_04', -1)
    ScreenShake(0, 8000)
    physicsXImpulse(1000)
    physicsYImpulse(60000)
    setGravity(100)
    RefreshMultihit()
    Damage(100)
    PushbackX(60000)
    Hitstop(0)
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    RefreshMultihit()
    Unknown2038(-1)
    Unknown30048(1)
    Unknown11023(1)
    sprite('Action_225_01', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(10, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_225_03', 45)	# 11-55	 **attackbox here**
    clearUponHandler(3)
    Unknown2034(0)
    Unknown2053(0)
    RefreshMultihit()
    Unknown30079(0)
    physicsXImpulse(50000)
    physicsYImpulse(50000)
    setGravity(100)
    AirPushbackX(100)
    AirPushbackY(5000)
    YImpluseBeforeWallbounce(50)
    PushbackX(60000)
    Hitstop(0)
    AirUntechableTime(120)
    AirHitstunAnimation(13)
    GroundedHitstunAnimation(13)
    Unknown30048(1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008913000000000000')
    SFX_0('005_swing_grap_2_2')
    sprite('Action_225_03', 5)	# 56-60	 **attackbox here**
    StartMultihit()
    Unknown11069('UltimateAssaultDDDOD_exe_1_ranb')
    enterState('UltimateAssaultDDDOD_exe_1_ranb')

@State
def UltimateAssaultDDDOD_exe_1_ranb():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown1084(1)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11064(1)
        Unknown11108('03000000')

        def upon_43():
            if (SLOT_48 == 5101):
                sendToLabel(1)
    sprite('null', 6)	# 1-6
    SFX_4('umi253')
    GFX_0('UltimateAssaultODDD_ranbu', -1)
    sprite('null', 32767)	# 7-32773
    label(1)
    sprite('keep', 1)	# 32774-32774
    enterState('UltimateAssaultDDDOD_catch_2')

@State
def UltimateAssaultDDDOD_catch_2():

    def upon_IMMEDIATE():
        Unknown23056('')
        Unknown17011('UltimateAssaultDDDOD_exe_2', 3, 1, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown11108('03000000')
        Unknown11069('UltimateAssaultDDDOD_exe_2')
        Unknown11064(1)
    sprite('null', 1)	# 1-1
    Unknown1086(22)
    teleportRelativeX(-5000)
    Unknown1007(5000)
    sprite('Action_226_01', 1)	# 2-2	 **attackbox here**
    GFX_0('EffUltimateAssault_05', -1)
    physicsXImpulse(0)
    physicsYImpulse(-5000)
    setGravity(100)
    SFX_0('005_swing_grap_2_2')
    sprite('keep', 1)	# 3-3
    StartMultihit()
    Unknown2053(1)
    Unknown26('UltimateAssaultLookAtMeCamera')

@State
def UltimateAssaultDDDOD_exe_2():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        setInvincible(1)
        Unknown30079(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown30061(0)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown2037(9)
        Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008a13000000000000')

        def upon_3():
            if (not SLOT_158):
                clearUponHandler(3)
                Unknown20000(0)
                Unknown26('UltimateAssaultLookAtMeCamera')
    label(1)
    sprite('Action_226_01', 5)	# 1-5	 **attackbox here**
    GFX_0('EffUltimateAssault_06', -1)
    ScreenShake(0, 8000)
    clearUponHandler(78)
    physicsXImpulse(1000)
    physicsYImpulse(-70000)
    setGravity(100)
    RefreshMultihit()
    Damage(100)
    PushbackX(60000)
    Hitstop(0)
    Unknown30048(1)
    Unknown11023(1)
    sendToLabelUpon(2, 9)
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    sprite('Action_226_02', 5)	# 6-10	 **attackbox here**
    ScreenShake(0, 8000)
    RefreshMultihit()
    Unknown5000(12, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('Action_227_00', 12)	# 11-22	 **attackbox here**
    GFX_0('EffGroundBreak03', -1)
    Unknown21015('556c74696d61746541737361756c744c6f6f6b41744d6543616d6572610000008b13000000000000')
    Unknown20000(1)
    Unknown4004('6566666563745f3338305f430000000000000000000000000000000000000000ffff0000')
    Unknown4004('6566666563745f3338325f430000000000000000000000000000000000000000ffff0000')
    Unknown30079(0)
    RefreshMultihit()
    Unknown1084(1)
    clearUponHandler(2)
    Damage(800)
    AirPushbackX(3000)
    AirPushbackY(100000)
    AirUntechableTime(120)
    Unknown9310(30)
    Unknown11064(0)
    SFX_0('016_explode_2')
    sprite('Action_227_01', 40)	# 23-62	 **attackbox here**
    Unknown20003(0)
    sprite('Action_227_02', 1)	# 63-63	 **attackbox here**
    sprite('Action_228_00', 4)	# 64-67	 **attackbox here**
    sprite('Action_228_01', 4)	# 68-71	 **attackbox here**
    sprite('Action_228_02', 4)	# 72-75	 **attackbox here**
    sprite('Action_228_03', 4)	# 76-79	 **attackbox here**
    sprite('Action_228_04', 10)	# 80-89	 **attackbox here**
    sprite('Action_228_05', 4)	# 90-93	 **attackbox here**
    sprite('Action_228_06', 14)	# 94-107	 **attackbox here**
    tag_voice(1, 'umi252_0', 'umi252_1', '', '')
    sprite('Action_228_07', 4)	# 108-111	 **attackbox here**
    sprite('Action_228_09', 14)	# 112-125	 **attackbox here**
    sprite('Action_228_10', 3)	# 126-128	 **attackbox here**
    sprite('Action_228_11', 3)	# 129-131	 **attackbox here**
    sprite('Action_228_12', 5)	# 132-136	 **attackbox here**
    sprite('Action_228_13', 13)	# 137-149	 **attackbox here**
    Unknown20000(0)
    setInvincible(0)
    Unknown2053(1)
    sprite('Action_228_14', 4)	# 150-153
    sprite('Action_228_15', 5)	# 154-158
    sprite('Action_228_16', 3)	# 159-161

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
    sprite('Action_148_08', 6)	# 127-132	 **attackbox here**
    StartMultihit()
    sprite('Action_148_09', 6)	# 133-138	 **attackbox here**
    StartMultihit()
    sprite('Action_148_08', 6)	# 139-144	 **attackbox here**
    StartMultihit()
    sprite('Action_148_09', 3)	# 145-147	 **attackbox here**
    StartMultihit()
    Unknown2053(1)
    sprite('Action_148_07', 3)	# 148-150	 **attackbox here**
    GFX_0('EffNmlAtkJC_01', -1)
    GFX_0('EffNmlAtkJC_02', -1)
    GFX_0('EffNmlAtkJC_03', -1)
    sprite('Action_148_08', 5)	# 151-155	 **attackbox here**
    sendToLabelUpon(2, 9)
    sprite('Action_148_09', 4)	# 156-159	 **attackbox here**
    label(0)
    sprite('Action_148_08', 3)	# 160-162	 **attackbox here**
    sprite('Action_148_09', 3)	# 163-165	 **attackbox here**
    gotoLabel(0)
    label(9)
    sprite('Action_021_00', 5)	# 166-170
    Unknown8000(0, 1, 1)
    Unknown1084(1)
    sprite('Action_021_01', 15)	# 171-185
    sprite('Action_021_02', 10)	# 186-195

@Subroutine
def MouthTableInit():
    Unknown18011('umi000', 12643, 14433, 13667, 13665, 13667, 12897, 25396, 24887, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi500', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi501', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi502', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi503', 12641, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi504', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi505', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25397, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi520', 12641, 14179, 14177, 14179, 12897, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi521', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi522', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi523', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi524', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi525', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25397, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi402_0', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi402_1', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi403_0', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi403_1', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi600brc', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi600bhz', 12641, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi600pak', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi600ryn', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24885, 12339, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi600uor', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi601baz', 12641, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi601bny', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi601pce', 12643, 14177, 12643, 24880, 25399, 12337, 12897, 25392, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12340, 14179, 12641, 25392, 24887, 25399, 24887, 12339, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi601uli', 12641, 14179, 14177, 14179, 14177, 12899, 24880, 13618, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi601uwa', 12641, 14179, 13153, 25392, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 24887, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi602pak', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi700baz', 12641, 25392, 24887, 13619, 14179, 14177, 14179, 14177, 14179, 12897, 25397, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi700bhz', 12641, 12643, 24885, 25399, 24887, 12339, 14179, 14177, 14179, 14177, 12643, 24882, 25399, 24887, 25399, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi700brc', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi700ryn', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi700uor', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 24887, 25399, 24887, 12339, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi701bny', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 13619, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi701brc', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi701pak', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 13617, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi701pce', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 12897, 25399, 12850, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi701uli', 12641, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi701uwa', 12641, 14179, 14177, 13155, 24880, 12339, 14179, 13153, 25392, 24887, 12338, 12899, 24880, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('umi702brc', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('brc')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bhz')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('uli')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('Action_051_01', 3)	# 2-4
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-2000000)
    physicsXImpulse(20000)
    sprite('Action_051_02', 3)	# 5-7
    sprite('Action_051_03', 3)	# 8-10
    sprite('Action_051_04', 3)	# 11-13
    sprite('Action_051_05', 3)	# 14-16
    sprite('Action_051_06', 3)	# 17-19
    sprite('Action_051_07', 3)	# 20-22
    sprite('Action_051_08', 3)	# 23-25
    sprite('Action_051_09', 3)	# 26-28	 **attackbox here**
    Unknown1021(8000)
    setGravity(2000)
    sprite('Action_051_10', 3)	# 29-31
    sprite('Action_051_11', 3)	# 32-34
    sendToLabelUpon(2, 2)
    label(1)
    sprite('Action_051_12', 3)	# 35-37
    sprite('Action_051_13', 3)	# 38-40
    gotoLabel(1)
    label(2)
    sprite('Action_050_01', 4)	# 41-44
    SFX_0('100_hit_grap_0')
    Unknown1000(-1230000)
    Unknown8000(100, 1, 0)
    Unknown1084(1)
    sprite('Action_050_02', 5)	# 45-49
    sprite('Action_050_03', 5)	# 50-54
    sprite('Action_050_04', 6)	# 55-60
    sprite('Action_050_05', 20)	# 61-80
    sprite('Action_050_06', 4)	# 81-84
    sprite('Action_050_07', 5)	# 85-89
    sprite('Action_050_08', 8)	# 90-97
    sprite('Action_050_09', 3)	# 98-100
    Unknown7006('umi500', 100, 896101749, 12592, 0, 0, 100, 896101749, 13360, 0, 0, 100, 0, 0, 0, 0, 0)
    label(3)
    sprite('Action_050_10', 1)	# 101-101	 **attackbox here**
    if SLOT_97:
        _gotolabel(3)
    sprite('Action_050_11', 4)	# 102-105
    Unknown23018(1)
    label(4)
    sprite('Action_000_00', 5)	# 106-110	 **attackbox here**
    sprite('Action_000_01', 5)	# 111-115	 **attackbox here**
    sprite('Action_000_02', 5)	# 116-120	 **attackbox here**
    sprite('Action_000_03', 5)	# 121-125	 **attackbox here**
    sprite('Action_000_04', 5)	# 126-130	 **attackbox here**
    sprite('Action_000_05', 5)	# 131-135	 **attackbox here**
    sprite('Action_000_06', 5)	# 136-140	 **attackbox here**
    sprite('Action_000_07', 5)	# 141-145	 **attackbox here**
    sprite('Action_000_08', 5)	# 146-150	 **attackbox here**
    sprite('Action_000_09', 5)	# 151-155	 **attackbox here**
    loopRest()
    gotoLabel(4)
    ExitState()
    label(10)
    sprite('Action_051_01', 3)	# 156-158
    Unknown2034(0)
    Unknown2053(0)
    Unknown1000(-2000000)
    physicsXImpulse(20000)
    sprite('Action_051_02', 3)	# 159-161
    sprite('Action_051_03', 3)	# 162-164
    sprite('Action_051_04', 3)	# 165-167
    sprite('Action_051_05', 3)	# 168-170
    sprite('Action_051_06', 3)	# 171-173
    sprite('Action_051_07', 3)	# 174-176
    sprite('Action_051_08', 3)	# 177-179
    sprite('Action_051_01', 3)	# 180-182
    sprite('Action_051_02', 3)	# 183-185
    sprite('Action_051_03', 3)	# 186-188
    sprite('Action_051_04', 3)	# 189-191
    sprite('Action_051_05', 3)	# 192-194
    sprite('Action_050_13', 4)	# 195-198
    Unknown1019(15)
    sprite('Action_050_14', 4)	# 199-202	 **attackbox here**
    Unknown7006('umi502', 100, 896101749, 13104, 0, 0, 100, 896101749, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown1000(-1230000)
    Unknown1084(1)
    label(11)
    sprite('Action_050_15', 1)	# 203-203	 **attackbox here**
    if SLOT_97:
        _gotolabel(11)
    sprite('Action_050_16', 4)	# 204-207
    sprite('Action_050_17', 4)	# 208-211
    Unknown23018(1)
    label(12)
    sprite('Action_000_00', 5)	# 212-216	 **attackbox here**
    sprite('Action_000_01', 5)	# 217-221	 **attackbox here**
    sprite('Action_000_02', 5)	# 222-226	 **attackbox here**
    sprite('Action_000_03', 5)	# 227-231	 **attackbox here**
    sprite('Action_000_04', 5)	# 232-236	 **attackbox here**
    sprite('Action_000_05', 5)	# 237-241	 **attackbox here**
    sprite('Action_000_06', 5)	# 242-246	 **attackbox here**
    sprite('Action_000_07', 5)	# 247-251	 **attackbox here**
    sprite('Action_000_08', 5)	# 252-256	 **attackbox here**
    sprite('Action_000_09', 5)	# 257-261	 **attackbox here**
    loopRest()
    gotoLabel(12)
    ExitState()
    label(20)
    sprite('Action_000_00', 32767)	# 262-33028	 **attackbox here**
    SFX_1('umi701uwa')
    ExitState()
    label(100)
    sprite('Action_000_00', 5)	# 33029-33033	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2019(1000)
    else:
        Unknown1000(-1230000)
        Unknown2019(1000)
    sprite('Action_000_01', 5)	# 33034-33038	 **attackbox here**
    sprite('Action_000_02', 5)	# 33039-33043	 **attackbox here**
    sprite('Action_000_03', 5)	# 33044-33048	 **attackbox here**
    sprite('Action_050_07', 5)	# 33049-33053
    SFX_1('umi600brc')
    sprite('Action_050_08', 8)	# 33054-33061
    sprite('Action_050_09', 3)	# 33062-33064
    sprite('Action_050_10', 120)	# 33065-33184	 **attackbox here**
    sprite('Action_050_11', 5)	# 33185-33189
    Unknown21007(24, 40)
    Unknown21011(120)
    label(101)
    sprite('Action_000_00', 5)	# 33190-33194	 **attackbox here**
    sprite('Action_000_01', 5)	# 33195-33199	 **attackbox here**
    sprite('Action_000_02', 5)	# 33200-33204	 **attackbox here**
    sprite('Action_000_03', 5)	# 33205-33209	 **attackbox here**
    sprite('Action_000_04', 5)	# 33210-33214	 **attackbox here**
    sprite('Action_000_05', 5)	# 33215-33219	 **attackbox here**
    sprite('Action_000_06', 5)	# 33220-33224	 **attackbox here**
    sprite('Action_000_07', 5)	# 33225-33229	 **attackbox here**
    sprite('Action_000_08', 5)	# 33230-33234	 **attackbox here**
    sprite('Action_000_09', 5)	# 33235-33239	 **attackbox here**
    loopRest()
    gotoLabel(101)
    ExitState()
    label(110)
    sprite('Action_000_00', 1)	# 33240-33240	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 5)	# 33241-33245	 **attackbox here**
    sprite('Action_000_01', 5)	# 33246-33250	 **attackbox here**
    sprite('Action_000_02', 5)	# 33251-33255	 **attackbox here**
    sprite('Action_000_03', 5)	# 33256-33260	 **attackbox here**
    sprite('Action_000_04', 5)	# 33261-33265	 **attackbox here**
    sprite('Action_000_05', 5)	# 33266-33270	 **attackbox here**
    sprite('Action_000_06', 5)	# 33271-33275	 **attackbox here**
    sprite('Action_000_07', 5)	# 33276-33280	 **attackbox here**
    sprite('Action_000_08', 5)	# 33281-33285	 **attackbox here**
    sprite('Action_000_09', 5)	# 33286-33290	 **attackbox here**
    loopRest()
    gotoLabel(111)
    label(112)
    sprite('Action_050_07', 5)	# 33291-33295
    SFX_1('umi601bny')
    Unknown23018(1)
    sprite('Action_050_08', 8)	# 33296-33303
    sprite('Action_050_09', 3)	# 33304-33306
    sprite('Action_050_10', 120)	# 33307-33426	 **attackbox here**
    sprite('Action_050_11', 5)	# 33427-33431
    label(113)
    sprite('Action_000_00', 5)	# 33432-33436	 **attackbox here**
    sprite('Action_000_01', 5)	# 33437-33441	 **attackbox here**
    sprite('Action_000_02', 5)	# 33442-33446	 **attackbox here**
    sprite('Action_000_03', 5)	# 33447-33451	 **attackbox here**
    sprite('Action_000_04', 5)	# 33452-33456	 **attackbox here**
    sprite('Action_000_05', 5)	# 33457-33461	 **attackbox here**
    sprite('Action_000_06', 5)	# 33462-33466	 **attackbox here**
    sprite('Action_000_07', 5)	# 33467-33471	 **attackbox here**
    sprite('Action_000_08', 5)	# 33472-33476	 **attackbox here**
    sprite('Action_000_09', 5)	# 33477-33481	 **attackbox here**
    loopRest()
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('Action_000_00', 5)	# 33482-33486	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('Action_000_01', 5)	# 33487-33491	 **attackbox here**
    sprite('Action_000_02', 5)	# 33492-33496	 **attackbox here**
    sprite('Action_000_03', 5)	# 33497-33501	 **attackbox here**
    sprite('Action_050_13', 4)	# 33502-33505
    sprite('Action_050_14', 4)	# 33506-33509	 **attackbox here**
    SFX_1('umi600bhz')
    sprite('Action_050_15', 140)	# 33510-33649	 **attackbox here**
    sprite('Action_050_16', 4)	# 33650-33653
    sprite('Action_050_17', 4)	# 33654-33657
    Unknown21007(24, 40)
    Unknown21011(120)
    label(122)
    sprite('Action_000_00', 5)	# 33658-33662	 **attackbox here**
    sprite('Action_000_01', 5)	# 33663-33667	 **attackbox here**
    sprite('Action_000_02', 5)	# 33668-33672	 **attackbox here**
    sprite('Action_000_03', 5)	# 33673-33677	 **attackbox here**
    sprite('Action_000_04', 5)	# 33678-33682	 **attackbox here**
    sprite('Action_000_05', 5)	# 33683-33687	 **attackbox here**
    sprite('Action_000_06', 5)	# 33688-33692	 **attackbox here**
    sprite('Action_000_07', 5)	# 33693-33697	 **attackbox here**
    sprite('Action_000_08', 5)	# 33698-33702	 **attackbox here**
    sprite('Action_000_09', 5)	# 33703-33707	 **attackbox here**
    loopRest()
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('Action_000_00', 1)	# 33708-33708	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('Action_000_00', 5)	# 33709-33713	 **attackbox here**
    sprite('Action_000_01', 5)	# 33714-33718	 **attackbox here**
    sprite('Action_000_02', 5)	# 33719-33723	 **attackbox here**
    sprite('Action_000_03', 5)	# 33724-33728	 **attackbox here**
    sprite('Action_000_04', 5)	# 33729-33733	 **attackbox here**
    sprite('Action_000_05', 5)	# 33734-33738	 **attackbox here**
    sprite('Action_000_06', 5)	# 33739-33743	 **attackbox here**
    sprite('Action_000_07', 5)	# 33744-33748	 **attackbox here**
    sprite('Action_000_08', 5)	# 33749-33753	 **attackbox here**
    sprite('Action_000_09', 5)	# 33754-33758	 **attackbox here**
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('Action_050_13', 4)	# 33759-33762
    sprite('Action_050_14', 4)	# 33763-33766	 **attackbox here**
    SFX_1('umi601baz')
    sprite('Action_050_15', 140)	# 33767-33906	 **attackbox here**
    sprite('Action_050_16', 4)	# 33907-33910
    sprite('Action_050_17', 4)	# 33911-33914
    Unknown21011(90)
    label(133)
    sprite('Action_000_00', 5)	# 33915-33919	 **attackbox here**
    sprite('Action_000_01', 5)	# 33920-33924	 **attackbox here**
    sprite('Action_000_02', 5)	# 33925-33929	 **attackbox here**
    sprite('Action_000_03', 5)	# 33930-33934	 **attackbox here**
    sprite('Action_000_04', 5)	# 33935-33939	 **attackbox here**
    sprite('Action_000_05', 5)	# 33940-33944	 **attackbox here**
    sprite('Action_000_06', 5)	# 33945-33949	 **attackbox here**
    sprite('Action_000_07', 5)	# 33950-33954	 **attackbox here**
    sprite('Action_000_08', 5)	# 33955-33959	 **attackbox here**
    sprite('Action_000_09', 5)	# 33960-33964	 **attackbox here**
    loopRest()
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('Action_000_00', 1)	# 33965-33965	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        Unknown2037(1)
    label(141)
    sprite('Action_000_00', 5)	# 33966-33970	 **attackbox here**
    sprite('Action_000_01', 5)	# 33971-33975	 **attackbox here**
    sprite('Action_000_02', 5)	# 33976-33980	 **attackbox here**
    sprite('Action_000_03', 5)	# 33981-33985	 **attackbox here**
    sprite('Action_000_04', 5)	# 33986-33990	 **attackbox here**
    sprite('Action_000_05', 5)	# 33991-33995	 **attackbox here**
    sprite('Action_000_06', 5)	# 33996-34000	 **attackbox here**
    sprite('Action_000_07', 5)	# 34001-34005	 **attackbox here**
    sprite('Action_000_08', 5)	# 34006-34010	 **attackbox here**
    sprite('Action_000_09', 5)	# 34011-34015	 **attackbox here**
    loopRest()
    Unknown19(141, 2, 2)
    label(142)
    sprite('keep', 1)	# 34016-34016
    SFX_1('umi601pce')
    Unknown23018(1)
    Unknown2037(6)
    label(143)
    sprite('Action_000_00', 5)	# 34017-34021	 **attackbox here**
    Unknown2038(-1)
    sprite('Action_000_01', 5)	# 34022-34026	 **attackbox here**
    sprite('Action_000_02', 5)	# 34027-34031	 **attackbox here**
    sprite('Action_000_03', 5)	# 34032-34036	 **attackbox here**
    sprite('Action_000_04', 5)	# 34037-34041	 **attackbox here**
    sprite('Action_000_05', 5)	# 34042-34046	 **attackbox here**
    sprite('Action_000_06', 5)	# 34047-34051	 **attackbox here**
    sprite('Action_000_07', 5)	# 34052-34056	 **attackbox here**
    sprite('Action_000_08', 5)	# 34057-34061	 **attackbox here**
    sprite('Action_000_09', 5)	# 34062-34066	 **attackbox here**
    loopRest()
    if SLOT_2:
        _gotolabel(143)
    sprite('Action_053_07', 5)	# 34067-34071
    sprite('Action_053_08', 5)	# 34072-34076
    sprite('Action_053_09', 5)	# 34077-34081
    sprite('Action_053_10', 5)	# 34082-34086
    sprite('Action_053_11', 5)	# 34087-34091
    sprite('Action_053_12', 5)	# 34092-34096
    sprite('Action_053_13', 6)	# 34097-34102
    sprite('Action_053_14', 12)	# 34103-34114
    sprite('Action_053_15', 4)	# 34115-34118	 **attackbox here**
    sprite('Action_053_16', 3)	# 34119-34121	 **attackbox here**
    sprite('Action_053_17', 30)	# 34122-34151	 **attackbox here**
    sprite('Action_053_18', 32767)	# 34152-66918	 **attackbox here**
    loopRest()
    ExitState()
    label(150)
    sprite('Mik644_00', 6)	# 66919-66924	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1200000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    Unknown2019(500)
    SFX_1('umi600pak')
    label(151)
    sprite('Mik644_00', 1)	# 66925-66925	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('Mik644_00', 32767)	# 66926-99692	 **attackbox here**
    Unknown21007(24, 40)
    label(152)
    sprite('Mik644_00', 20)	# 99693-99712	 **attackbox here**
    SFX_1('umi602pak')
    sprite('Mik644_01', 6)	# 99713-99718	 **attackbox here**
    sprite('Mik644_02', 6)	# 99719-99724	 **attackbox here**
    sprite('Mik644_03', 6)	# 99725-99730	 **attackbox here**
    sprite('Mik644_04', 6)	# 99731-99736	 **attackbox here**
    sprite('Mik644_05', 6)	# 99737-99742	 **attackbox here**
    Unknown21011(240)
    label(153)
    sprite('Mik644_06', 6)	# 99743-99748	 **attackbox here**
    sprite('Mik644_07', 6)	# 99749-99754	 **attackbox here**
    sprite('Mik644_08', 6)	# 99755-99760	 **attackbox here**
    sprite('Mik644_09', 6)	# 99761-99766	 **attackbox here**
    gotoLabel(153)
    ExitState()
    label(160)
    sprite('Action_000_00', 1)	# 99767-99767	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 5)	# 99768-99772	 **attackbox here**
    sprite('Action_000_01', 5)	# 99773-99777	 **attackbox here**
    sprite('Action_000_02', 5)	# 99778-99782	 **attackbox here**
    sprite('Action_000_03', 5)	# 99783-99787	 **attackbox here**
    sprite('Action_000_04', 5)	# 99788-99792	 **attackbox here**
    sprite('Action_000_05', 5)	# 99793-99797	 **attackbox here**
    sprite('Action_000_06', 5)	# 99798-99802	 **attackbox here**
    sprite('Action_000_07', 5)	# 99803-99807	 **attackbox here**
    sprite('Action_000_08', 5)	# 99808-99812	 **attackbox here**
    sprite('Action_000_09', 5)	# 99813-99817	 **attackbox here**
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('Action_050_07', 5)	# 99818-99822
    SFX_1('umi601uli')
    sprite('Action_050_08', 8)	# 99823-99830
    sprite('Action_050_09', 3)	# 99831-99833
    label(163)
    sprite('Action_050_10', 1)	# 99834-99834	 **attackbox here**
    if SLOT_97:
        _gotolabel(163)
    sprite('Action_050_10', 20)	# 99835-99854	 **attackbox here**
    sprite('Action_050_11', 5)	# 99855-99859
    Unknown23018(1)
    label(164)
    sprite('Action_000_00', 5)	# 99860-99864	 **attackbox here**
    sprite('Action_000_01', 5)	# 99865-99869	 **attackbox here**
    sprite('Action_000_02', 5)	# 99870-99874	 **attackbox here**
    sprite('Action_000_03', 5)	# 99875-99879	 **attackbox here**
    sprite('Action_000_04', 5)	# 99880-99884	 **attackbox here**
    sprite('Action_000_05', 5)	# 99885-99889	 **attackbox here**
    sprite('Action_000_06', 5)	# 99890-99894	 **attackbox here**
    sprite('Action_000_07', 5)	# 99895-99899	 **attackbox here**
    sprite('Action_000_08', 5)	# 99900-99904	 **attackbox here**
    sprite('Action_000_09', 5)	# 99905-99909	 **attackbox here**
    loopRest()
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('Action_051_01', 3)	# 99910-99912
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-2000000)
    else:
        Unknown1000(-2235000)
    physicsXImpulse(20000)
    sprite('Action_051_02', 3)	# 99913-99915
    sprite('Action_051_03', 3)	# 99916-99918
    sprite('Action_051_04', 3)	# 99919-99921
    sprite('Action_051_05', 3)	# 99922-99924
    sprite('Action_051_06', 3)	# 99925-99927
    sprite('Action_051_07', 3)	# 99928-99930
    sprite('Action_051_08', 3)	# 99931-99933
    sprite('Action_051_01', 3)	# 99934-99936
    sprite('Action_051_02', 3)	# 99937-99939
    sprite('Action_051_03', 3)	# 99940-99942
    sprite('Action_051_04', 3)	# 99943-99945
    sprite('Action_051_05', 3)	# 99946-99948
    sprite('Action_050_13', 4)	# 99949-99952
    Unknown1019(15)
    sprite('Action_050_14', 4)	# 99953-99956	 **attackbox here**
    SFX_1('umi600uor')
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown1084(1)
    label(171)
    sprite('Action_050_15', 1)	# 99957-99957	 **attackbox here**
    if SLOT_97:
        _gotolabel(171)
    sprite('Action_050_16', 4)	# 99958-99961
    sprite('Action_050_17', 4)	# 99962-99965
    Unknown21007(24, 40)
    Unknown21011(300)
    label(172)
    sprite('Action_000_00', 5)	# 99966-99970	 **attackbox here**
    sprite('Action_000_01', 5)	# 99971-99975	 **attackbox here**
    sprite('Action_000_02', 5)	# 99976-99980	 **attackbox here**
    sprite('Action_000_03', 5)	# 99981-99985	 **attackbox here**
    sprite('Action_000_04', 5)	# 99986-99990	 **attackbox here**
    sprite('Action_000_05', 5)	# 99991-99995	 **attackbox here**
    sprite('Action_000_06', 5)	# 99996-100000	 **attackbox here**
    sprite('Action_000_07', 5)	# 100001-100005	 **attackbox here**
    sprite('Action_000_08', 5)	# 100006-100010	 **attackbox here**
    sprite('Action_000_09', 5)	# 100011-100015	 **attackbox here**
    loopRest()
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('Action_051_01', 3)	# 100016-100018
    Unknown2034(0)
    Unknown2053(0)
    if SLOT_158:
        Unknown1000(-2000000)
    else:
        Unknown1000(-2235000)
    physicsXImpulse(20000)
    sprite('Action_051_02', 3)	# 100019-100021
    sprite('Action_051_03', 3)	# 100022-100024
    sprite('Action_051_04', 3)	# 100025-100027
    sprite('Action_051_05', 3)	# 100028-100030
    sprite('Action_051_06', 3)	# 100031-100033
    sprite('Action_051_07', 3)	# 100034-100036
    sprite('Action_051_08', 3)	# 100037-100039
    sprite('Action_051_01', 3)	# 100040-100042
    sprite('Action_051_02', 3)	# 100043-100045
    sprite('Action_051_03', 3)	# 100046-100048
    sprite('Action_051_04', 3)	# 100049-100051
    sprite('Action_051_05', 3)	# 100052-100054
    sprite('Action_051_15', 4)	# 100055-100058
    Unknown1019(15)
    sprite('Action_050_07', 5)	# 100059-100063
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    Unknown1084(1)
    SFX_1('umi600ryn')
    sprite('Action_050_08', 8)	# 100064-100071
    sprite('Action_050_09', 3)	# 100072-100074
    label(181)
    sprite('Action_050_10', 1)	# 100075-100075	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_050_10', 20)	# 100076-100095	 **attackbox here**
    sprite('Action_050_11', 5)	# 100096-100100
    Unknown21007(24, 40)
    Unknown21011(300)
    label(182)
    sprite('Action_000_00', 5)	# 100101-100105	 **attackbox here**
    sprite('Action_000_01', 5)	# 100106-100110	 **attackbox here**
    sprite('Action_000_02', 5)	# 100111-100115	 **attackbox here**
    sprite('Action_000_03', 5)	# 100116-100120	 **attackbox here**
    sprite('Action_000_04', 5)	# 100121-100125	 **attackbox here**
    sprite('Action_000_05', 5)	# 100126-100130	 **attackbox here**
    sprite('Action_000_06', 5)	# 100131-100135	 **attackbox here**
    sprite('Action_000_07', 5)	# 100136-100140	 **attackbox here**
    sprite('Action_000_08', 5)	# 100141-100145	 **attackbox here**
    sprite('Action_000_09', 5)	# 100146-100150	 **attackbox here**
    loopRest()
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('Action_000_00', 1)	# 100151-100151	 **attackbox here**
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_000_00', 5)	# 100152-100156	 **attackbox here**
    sprite('Action_000_01', 5)	# 100157-100161	 **attackbox here**
    sprite('Action_000_02', 5)	# 100162-100166	 **attackbox here**
    sprite('Action_000_03', 5)	# 100167-100171	 **attackbox here**
    sprite('Action_000_04', 5)	# 100172-100176	 **attackbox here**
    sprite('Action_000_05', 5)	# 100177-100181	 **attackbox here**
    sprite('Action_000_06', 5)	# 100182-100186	 **attackbox here**
    sprite('Action_000_07', 5)	# 100187-100191	 **attackbox here**
    sprite('Action_000_08', 5)	# 100192-100196	 **attackbox here**
    sprite('Action_000_09', 5)	# 100197-100201	 **attackbox here**
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('Action_050_13', 4)	# 100202-100205
    sprite('Action_050_14', 4)	# 100206-100209	 **attackbox here**
    SFX_1('umi601uwa')
    label(193)
    sprite('Action_050_15', 1)	# 100210-100210	 **attackbox here**
    if SLOT_97:
        _gotolabel(193)
    sprite('Action_050_15', 10)	# 100211-100220	 **attackbox here**
    sprite('Action_050_16', 4)	# 100221-100224
    sprite('Action_050_17', 4)	# 100225-100228
    Unknown23018(1)
    label(194)
    sprite('Action_000_00', 5)	# 100229-100233	 **attackbox here**
    sprite('Action_000_01', 5)	# 100234-100238	 **attackbox here**
    sprite('Action_000_02', 5)	# 100239-100243	 **attackbox here**
    sprite('Action_000_03', 5)	# 100244-100248	 **attackbox here**
    sprite('Action_000_04', 5)	# 100249-100253	 **attackbox here**
    sprite('Action_000_05', 5)	# 100254-100258	 **attackbox here**
    sprite('Action_000_06', 5)	# 100259-100263	 **attackbox here**
    sprite('Action_000_07', 5)	# 100264-100268	 **attackbox here**
    sprite('Action_000_08', 5)	# 100269-100273	 **attackbox here**
    sprite('Action_000_09', 5)	# 100274-100278	 **attackbox here**
    loopRest()
    gotoLabel(194)
    ExitState()
    label(991)
    sprite('Action_000_00', 1)	# 100279-100279	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 5)	# 100280-100284	 **attackbox here**
    sprite('Action_000_01', 5)	# 100285-100289	 **attackbox here**
    sprite('Action_000_02', 5)	# 100290-100294	 **attackbox here**
    sprite('Action_000_03', 5)	# 100295-100299	 **attackbox here**
    sprite('Action_000_04', 5)	# 100300-100304	 **attackbox here**
    sprite('Action_000_05', 5)	# 100305-100309	 **attackbox here**
    sprite('Action_000_06', 5)	# 100310-100314	 **attackbox here**
    sprite('Action_000_07', 5)	# 100315-100319	 **attackbox here**
    sprite('Action_000_08', 5)	# 100320-100324	 **attackbox here**
    sprite('Action_000_09', 5)	# 100325-100329	 **attackbox here**
    loopRest()
    gotoLabel(992)
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
            if PartnerChar('brc'):
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
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(482)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uor'):
                if (SLOT_145 <= 700000):
                    if (SLOT_145 >= 200000):
                        sendToLabel(170)
                        clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('pak'):
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
    label(0)
    sprite('Action_053_00', 3)	# 4-6
    sprite('Action_053_01', 5)	# 7-11
    Unknown1021(15000)
    setGravity(1200)
    sendToLabelUpon(2, 1)
    if SLOT_158:
        if SLOT_52:
            Unknown7006('umi524', 100, 896101749, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('umi402_0', 100, 879324533, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('umi520', 100, 896101749, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_053_02', 3)	# 12-14
    sprite('Action_053_03', 4)	# 15-18
    sprite('Action_053_04', 8)	# 19-26
    sprite('Action_053_05', 4)	# 27-30
    sprite('Action_053_06', 32767)	# 31-32797
    label(1)
    sprite('Action_053_07', 5)	# 32798-32802
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_053_08', 5)	# 32803-32807
    sprite('Action_053_09', 5)	# 32808-32812
    sprite('Action_053_10', 5)	# 32813-32817
    sprite('Action_053_11', 5)	# 32818-32822
    sprite('Action_053_12', 5)	# 32823-32827
    sprite('Action_053_13', 6)	# 32828-32833
    sprite('Action_053_14', 12)	# 32834-32845
    sprite('Action_053_15', 4)	# 32846-32849	 **attackbox here**
    sprite('Action_053_16', 3)	# 32850-32852	 **attackbox here**
    sprite('Action_053_17', 30)	# 32853-32882	 **attackbox here**
    Unknown23018(1)
    sprite('Action_053_18', 32767)	# 32883-65649	 **attackbox here**
    label(10)
    sprite('Action_052_00', 4)	# 65650-65653

    def upon_32():
        clearUponHandler(32)
        sendToLabel(11)
    sprite('Action_052_01', 10)	# 65654-65663
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('Action_052_02', 7)	# 65664-65670
    sprite('Action_052_03', 6)	# 65671-65676
    sprite('Action_052_04', 5)	# 65677-65681
    sprite('Action_052_05', 4)	# 65682-65685
    sprite('Action_052_06', 4)	# 65686-65689
    sprite('Action_052_07', 10)	# 65690-65699
    physicsYImpulse(13000)
    setGravity(1000)
    if SLOT_158:
        tag_voice(1, 'umi523', 'umi999', '', '')
    sprite('Action_052_08', 7)	# 65700-65706
    sprite('Action_052_09', 6)	# 65707-65712
    if SLOT_158:
        tag_voice(0, '', 'umi522', '', '')
    sprite('Action_052_10', 5)	# 65713-65717
    sprite('Action_052_11', 4)	# 65718-65721
    sprite('Action_052_12', 4)	# 65722-65725
    sprite('Action_052_13', 10)	# 65726-65735
    physicsYImpulse(15000)
    setGravity(1000)
    GFX_0('WIN_Kobushi_UP', 0)
    sprite('Action_052_14', 7)	# 65736-65742
    sprite('Action_052_15', 6)	# 65743-65748
    sprite('Action_052_16', 5)	# 65749-65753
    sprite('Action_052_17', 5)	# 65754-65758
    sprite('Action_052_18', 5)	# 65759-65763
    sprite('Action_052_19', 50)	# 65764-65813
    sprite('Action_052_20', 32767)	# 65814-98580
    label(11)
    sprite('Action_052_24', 3)	# 98581-98583
    SFX_0('100_hit_grap_2')
    sprite('Action_052_25', 50)	# 98584-98633
    sprite('Action_052_26', 5)	# 98634-98638	 **attackbox here**
    Unknown23018(1)
    sprite('Action_052_27', 32767)	# 98639-131405	 **attackbox here**
    label(100)
    sprite('Action_052_00', 4)	# 131406-131409

    def upon_32():
        clearUponHandler(32)
        sendToLabel(101)
    if (not SLOT_158):
        Unknown2019(1000)
    sprite('Action_052_01', 10)	# 131410-131419
    physicsYImpulse(13000)
    setGravity(1000)
    SFX_1('umi700brc')
    sprite('Action_052_02', 7)	# 131420-131426
    sprite('Action_052_03', 6)	# 131427-131432
    sprite('Action_052_04', 5)	# 131433-131437
    sprite('Action_052_05', 4)	# 131438-131441
    sprite('Action_052_06', 4)	# 131442-131445
    sprite('Action_052_07', 10)	# 131446-131455
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('Action_052_08', 7)	# 131456-131462
    sprite('Action_052_09', 6)	# 131463-131468
    sprite('Action_052_10', 5)	# 131469-131473
    sprite('Action_052_11', 4)	# 131474-131477
    sprite('Action_052_12', 4)	# 131478-131481
    sprite('Action_052_13', 10)	# 131482-131491
    physicsYImpulse(15000)
    setGravity(1000)
    GFX_0('WIN_Kobushi_UP', 0)
    sprite('Action_052_14', 7)	# 131492-131498
    sprite('Action_052_15', 6)	# 131499-131504
    sprite('Action_052_16', 5)	# 131505-131509
    sprite('Action_052_17', 5)	# 131510-131514
    sprite('Action_052_18', 5)	# 131515-131519
    sprite('Action_052_19', 50)	# 131520-131569
    SFX_1('umi701brc')
    sprite('Action_052_20', 32767)	# 131570-164336
    label(101)
    sprite('Action_052_24', 3)	# 164337-164339
    SFX_0('100_hit_grap_2')
    SFX_1('umi702brc')
    sprite('Action_052_25', 50)	# 164340-164389
    Unknown21007(24, 40)
    sprite('Action_052_26', 5)	# 164390-164394	 **attackbox here**
    Unknown21011(200)
    sprite('Action_052_27', 32767)	# 164395-197161	 **attackbox here**
    loopRest()
    label(110)
    sprite('Action_000_00', 1)	# 197162-197162	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_00', 5)	# 197163-197167	 **attackbox here**
    sprite('Action_000_01', 5)	# 197168-197172	 **attackbox here**
    sprite('Action_000_02', 5)	# 197173-197177	 **attackbox here**
    sprite('Action_000_03', 5)	# 197178-197182	 **attackbox here**
    sprite('Action_000_04', 5)	# 197183-197187	 **attackbox here**
    sprite('Action_000_05', 5)	# 197188-197192	 **attackbox here**
    sprite('Action_000_06', 5)	# 197193-197197	 **attackbox here**
    sprite('Action_000_07', 5)	# 197198-197202	 **attackbox here**
    sprite('Action_000_08', 5)	# 197203-197207	 **attackbox here**
    sprite('Action_000_09', 5)	# 197208-197212	 **attackbox here**
    loopRest()
    gotoLabel(111)
    label(112)
    label(113)
    sprite('Action_053_07', 5)	# 197213-197217
    SFX_1('umi701bny')
    Unknown23018(1)
    sprite('Action_053_08', 5)	# 197218-197222
    sprite('Action_053_09', 5)	# 197223-197227
    sprite('Action_053_10', 5)	# 197228-197232
    sprite('Action_053_11', 5)	# 197233-197237
    sprite('Action_053_12', 5)	# 197238-197242
    sprite('Action_053_13', 6)	# 197243-197248
    sprite('Action_053_14', 12)	# 197249-197260
    sprite('Action_053_15', 4)	# 197261-197264	 **attackbox here**
    sprite('Action_053_16', 3)	# 197265-197267	 **attackbox here**
    sprite('Action_053_17', 30)	# 197268-197297	 **attackbox here**
    sprite('Action_053_18', 32767)	# 197298-230064	 **attackbox here**
    label(120)
    sprite('Action_053_00', 3)	# 230065-230067
    sprite('Action_053_01', 5)	# 230068-230072
    physicsYImpulse(15000)
    setGravity(1200)
    sendToLabelUpon(2, 121)
    SFX_1('umi700bhz')
    sprite('Action_053_02', 3)	# 230073-230075
    sprite('Action_053_03', 4)	# 230076-230079
    sprite('Action_053_04', 8)	# 230080-230087
    sprite('Action_053_05', 4)	# 230088-230091
    sprite('Action_053_06', 32767)	# 230092-262858
    label(121)
    sprite('Action_053_00', 3)	# 262859-262861
    Unknown1084(1)
    sprite('Action_053_01', 5)	# 262862-262866
    physicsYImpulse(15000)
    setGravity(1200)
    sendToLabelUpon(2, 122)
    sprite('Action_053_02', 3)	# 262867-262869
    sprite('Action_053_03', 4)	# 262870-262873
    sprite('Action_053_04', 8)	# 262874-262881
    sprite('Action_053_05', 4)	# 262882-262885
    sprite('Action_053_06', 32767)	# 262886-295652
    label(122)
    sprite('Action_053_07', 5)	# 295653-295657
    Unknown1084(1)
    sprite('Action_053_08', 5)	# 295658-295662
    sprite('Action_053_09', 5)	# 295663-295667
    sprite('Action_053_10', 5)	# 295668-295672
    sprite('Action_053_11', 5)	# 295673-295677
    sprite('Action_053_12', 5)	# 295678-295682
    sprite('Action_053_13', 6)	# 295683-295688
    sprite('Action_053_14', 12)	# 295689-295700
    sprite('Action_053_15', 4)	# 295701-295704	 **attackbox here**
    sprite('Action_053_16', 3)	# 295705-295707	 **attackbox here**
    sprite('Action_053_17', 30)	# 295708-295737	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('Action_053_18', 32767)	# 295738-328504	 **attackbox here**
    label(130)
    sprite('Action_050_21', 3)	# 328505-328507
    SFX_1('umi700baz')
    label(131)
    sprite('Action_050_22', 1)	# 328508-328508	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_050_22', 30)	# 328509-328538	 **attackbox here**
    sprite('Action_050_22', 32767)	# 328539-361305	 **attackbox here**
    Unknown2034(0)
    Unknown2053(0)
    Unknown21007(24, 40)
    Unknown21011(240)
    label(140)
    sprite('Action_000_00', 1)	# 361306-361306	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('Action_000_00', 5)	# 361307-361311	 **attackbox here**
    sprite('Action_000_01', 5)	# 361312-361316	 **attackbox here**
    sprite('Action_000_02', 5)	# 361317-361321	 **attackbox here**
    sprite('Action_000_03', 5)	# 361322-361326	 **attackbox here**
    sprite('Action_000_04', 5)	# 361327-361331	 **attackbox here**
    sprite('Action_000_05', 5)	# 361332-361336	 **attackbox here**
    sprite('Action_000_06', 5)	# 361337-361341	 **attackbox here**
    sprite('Action_000_07', 5)	# 361342-361346	 **attackbox here**
    sprite('Action_000_08', 5)	# 361347-361351	 **attackbox here**
    sprite('Action_000_09', 5)	# 361352-361356	 **attackbox here**
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('Action_050_07', 5)	# 361357-361361
    SFX_1('umi701pce')
    Unknown23018(1)
    sprite('Action_050_08', 8)	# 361362-361369
    sprite('Action_050_09', 3)	# 361370-361372
    sprite('Action_050_10', 120)	# 361373-361492	 **attackbox here**
    sprite('Action_050_11', 5)	# 361493-361497
    sprite('Action_053_07', 5)	# 361498-361502
    sprite('Action_053_08', 5)	# 361503-361507
    sprite('Action_053_09', 5)	# 361508-361512
    sprite('Action_053_10', 5)	# 361513-361517
    sprite('Action_053_11', 5)	# 361518-361522
    sprite('Action_053_12', 5)	# 361523-361527
    sprite('Action_053_13', 6)	# 361528-361533
    sprite('Action_053_14', 12)	# 361534-361545
    sprite('Action_053_15', 4)	# 361546-361549	 **attackbox here**
    sprite('Action_053_16', 3)	# 361550-361552	 **attackbox here**
    sprite('Action_053_17', 30)	# 361553-361582	 **attackbox here**
    sprite('Action_053_18', 32767)	# 361583-394349	 **attackbox here**
    label(160)
    sprite('Action_000_00', 1)	# 394350-394350	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('Action_000_00', 5)	# 394351-394355	 **attackbox here**
    sprite('Action_000_01', 5)	# 394356-394360	 **attackbox here**
    sprite('Action_000_02', 5)	# 394361-394365	 **attackbox here**
    sprite('Action_000_03', 5)	# 394366-394370	 **attackbox here**
    sprite('Action_000_04', 5)	# 394371-394375	 **attackbox here**
    sprite('Action_000_05', 5)	# 394376-394380	 **attackbox here**
    sprite('Action_000_06', 5)	# 394381-394385	 **attackbox here**
    sprite('Action_000_07', 5)	# 394386-394390	 **attackbox here**
    sprite('Action_000_08', 5)	# 394391-394395	 **attackbox here**
    sprite('Action_000_09', 5)	# 394396-394400	 **attackbox here**
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('Action_053_00', 3)	# 394401-394403
    sprite('Action_053_01', 5)	# 394404-394408
    Unknown1021(15000)
    setGravity(1200)
    sendToLabelUpon(2, 163)
    SFX_1('umi701uli')
    sprite('Action_053_02', 3)	# 394409-394411
    sprite('Action_053_03', 4)	# 394412-394415
    sprite('Action_053_04', 8)	# 394416-394423
    sprite('Action_053_05', 4)	# 394424-394427
    sprite('Action_053_06', 32767)	# 394428-427194
    label(163)
    sprite('Action_053_07', 5)	# 427195-427199
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_053_08', 5)	# 427200-427204
    sprite('Action_053_09', 5)	# 427205-427209
    sprite('Action_053_10', 5)	# 427210-427214
    sprite('Action_053_11', 5)	# 427215-427219
    sprite('Action_053_12', 5)	# 427220-427224
    sprite('Action_053_13', 6)	# 427225-427230
    sprite('Action_053_14', 12)	# 427231-427242
    sprite('Action_053_15', 4)	# 427243-427246	 **attackbox here**
    sprite('Action_053_16', 3)	# 427247-427249	 **attackbox here**
    sprite('Action_053_17', 30)	# 427250-427279	 **attackbox here**
    Unknown23018(1)
    sprite('Action_053_18', 32767)	# 427280-460046	 **attackbox here**
    label(170)
    sprite('Action_053_00', 3)	# 460047-460049
    Unknown2019(0)
    sprite('Action_053_01', 5)	# 460050-460054
    Unknown1021(15000)
    setGravity(1200)
    sendToLabelUpon(2, 171)
    SFX_1('umi700uor')
    sprite('Action_053_02', 3)	# 460055-460057
    sprite('Action_053_03', 4)	# 460058-460061
    sprite('Action_053_04', 8)	# 460062-460069
    sprite('Action_053_05', 4)	# 460070-460073
    sprite('Action_053_06', 32767)	# 460074-492840
    label(171)
    sprite('Action_053_07', 5)	# 492841-492845
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_053_08', 5)	# 492846-492850
    sprite('Action_053_09', 5)	# 492851-492855
    sprite('Action_053_10', 5)	# 492856-492860
    sprite('Action_053_11', 5)	# 492861-492865
    sprite('Action_053_12', 5)	# 492866-492870
    sprite('Action_053_13', 6)	# 492871-492876
    sprite('Action_053_14', 12)	# 492877-492888
    sprite('Action_053_15', 4)	# 492889-492892	 **attackbox here**
    sprite('Action_053_16', 3)	# 492893-492895	 **attackbox here**
    sprite('Action_053_17', 30)	# 492896-492925	 **attackbox here**
    label(172)
    sprite('Action_053_18', 1)	# 492926-492926	 **attackbox here**
    if SLOT_97:
        _gotolabel(172)
    sprite('Action_053_18', 32767)	# 492927-525693	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(280)
    label(180)
    sprite('Action_052_00', 4)	# 525694-525697

    def upon_32():
        clearUponHandler(32)
        sendToLabel(181)
    sprite('Action_052_01', 10)	# 525698-525707
    physicsYImpulse(13000)
    setGravity(1000)
    SFX_1('umi700ryn')
    sprite('Action_052_02', 7)	# 525708-525714
    sprite('Action_052_03', 6)	# 525715-525720
    sprite('Action_052_04', 5)	# 525721-525725
    sprite('Action_052_05', 4)	# 525726-525729
    sprite('Action_052_06', 4)	# 525730-525733
    sprite('Action_052_01', 10)	# 525734-525743
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('Action_052_02', 7)	# 525744-525750
    sprite('Action_052_03', 6)	# 525751-525756
    sprite('Action_052_04', 5)	# 525757-525761
    sprite('Action_052_05', 4)	# 525762-525765
    sprite('Action_052_06', 4)	# 525766-525769
    sprite('Action_052_01', 10)	# 525770-525779
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('Action_052_02', 7)	# 525780-525786
    sprite('Action_052_03', 6)	# 525787-525792
    sprite('Action_052_04', 5)	# 525793-525797
    sprite('Action_052_05', 4)	# 525798-525801
    sprite('Action_052_06', 4)	# 525802-525805
    sprite('Action_052_07', 10)	# 525806-525815
    physicsYImpulse(13000)
    setGravity(1000)
    sprite('Action_052_08', 7)	# 525816-525822
    sprite('Action_052_09', 6)	# 525823-525828
    sprite('Action_052_10', 5)	# 525829-525833
    sprite('Action_052_11', 4)	# 525834-525837
    sprite('Action_052_12', 4)	# 525838-525841
    sprite('Action_052_13', 10)	# 525842-525851
    physicsYImpulse(15000)
    setGravity(1000)
    GFX_0('WIN_Kobushi_UP_1', 0)
    sprite('Action_052_14', 7)	# 525852-525858
    sprite('Action_052_15', 6)	# 525859-525864
    sprite('Action_052_16', 5)	# 525865-525869
    sprite('Action_052_17', 5)	# 525870-525874
    sprite('Action_052_18', 5)	# 525875-525879
    sprite('Action_052_19', 50)	# 525880-525929
    sprite('Action_052_20', 32767)	# 525930-558696
    label(181)
    sprite('Action_052_24', 3)	# 558697-558699
    SFX_0('100_hit_grap_2')
    sprite('Action_052_25', 70)	# 558700-558769
    sprite('Action_052_26', 5)	# 558770-558774	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(200)
    sprite('Action_052_27', 32767)	# 558775-591541	 **attackbox here**
    label(190)
    sprite('Action_000_00', 1)	# 591542-591542	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('Action_000_00', 5)	# 591543-591547	 **attackbox here**
    sprite('Action_000_01', 5)	# 591548-591552	 **attackbox here**
    sprite('Action_000_02', 5)	# 591553-591557	 **attackbox here**
    sprite('Action_000_03', 5)	# 591558-591562	 **attackbox here**
    sprite('Action_000_04', 5)	# 591563-591567	 **attackbox here**
    sprite('Action_000_05', 5)	# 591568-591572	 **attackbox here**
    sprite('Action_000_06', 5)	# 591573-591577	 **attackbox here**
    sprite('Action_000_07', 5)	# 591578-591582	 **attackbox here**
    sprite('Action_000_08', 5)	# 591583-591587	 **attackbox here**
    sprite('Action_000_09', 5)	# 591588-591592	 **attackbox here**
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('Action_053_00', 3)	# 591593-591595
    sprite('Action_053_01', 5)	# 591596-591600
    Unknown1021(15000)
    setGravity(1200)
    sendToLabelUpon(2, 193)
    SFX_1('umi701uwa')
    sprite('Action_053_02', 3)	# 591601-591603
    sprite('Action_053_03', 4)	# 591604-591607
    sprite('Action_053_04', 8)	# 591608-591615
    sprite('Action_053_05', 4)	# 591616-591619
    sprite('Action_053_06', 32767)	# 591620-624386
    label(193)
    sprite('Action_053_07', 5)	# 624387-624391
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_053_08', 5)	# 624392-624396
    sprite('Action_053_09', 5)	# 624397-624401
    sprite('Action_053_10', 5)	# 624402-624406
    sprite('Action_053_11', 5)	# 624407-624411
    sprite('Action_053_12', 5)	# 624412-624416
    sprite('Action_053_13', 6)	# 624417-624422
    sprite('Action_053_14', 12)	# 624423-624434
    sprite('Action_053_15', 4)	# 624435-624438	 **attackbox here**
    sprite('Action_053_16', 3)	# 624439-624441	 **attackbox here**
    sprite('Action_053_17', 30)	# 624442-624471	 **attackbox here**
    Unknown23018(1)
    sprite('Action_053_18', 32767)	# 624472-657238	 **attackbox here**
    label(200)
    sprite('Action_000_00', 1)	# 657239-657239	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_00', 5)	# 657240-657244	 **attackbox here**
    sprite('Action_000_01', 5)	# 657245-657249	 **attackbox here**
    sprite('Action_000_02', 5)	# 657250-657254	 **attackbox here**
    sprite('Action_000_03', 5)	# 657255-657259	 **attackbox here**
    sprite('Action_000_04', 5)	# 657260-657264	 **attackbox here**
    sprite('Action_000_05', 5)	# 657265-657269	 **attackbox here**
    sprite('Action_000_06', 5)	# 657270-657274	 **attackbox here**
    sprite('Action_000_07', 5)	# 657275-657279	 **attackbox here**
    sprite('Action_000_08', 5)	# 657280-657284	 **attackbox here**
    sprite('Action_000_09', 5)	# 657285-657289	 **attackbox here**
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('Action_053_00', 3)	# 657290-657292
    sprite('Action_053_01', 5)	# 657293-657297
    Unknown1021(15000)
    setGravity(1200)
    sendToLabelUpon(2, 203)
    SFX_1('umi701pak')
    sprite('Action_053_02', 3)	# 657298-657300
    sprite('Action_053_03', 4)	# 657301-657304
    sprite('Action_053_04', 8)	# 657305-657312
    sprite('Action_053_05', 4)	# 657313-657316
    sprite('Action_053_06', 32767)	# 657317-690083
    label(203)
    sprite('Action_053_07', 5)	# 690084-690088
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('Action_053_08', 5)	# 690089-690093
    sprite('Action_053_09', 5)	# 690094-690098
    sprite('Action_053_10', 5)	# 690099-690103
    sprite('Action_053_11', 5)	# 690104-690108
    sprite('Action_053_12', 5)	# 690109-690113
    sprite('Action_053_13', 6)	# 690114-690119
    sprite('Action_053_14', 12)	# 690120-690131
    sprite('Action_053_15', 4)	# 690132-690135	 **attackbox here**
    sprite('Action_053_16', 3)	# 690136-690138	 **attackbox here**
    sprite('Action_053_17', 30)	# 690139-690168	 **attackbox here**
    Unknown23018(1)
    sprite('Action_053_18', 32767)	# 690169-722935	 **attackbox here**

@State
def CmnActLose():
    sprite('Action_248_00', 15)	# 1-15
    if SLOT_158:
        Unknown7006('umi403_0', 100, 879324533, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_248_01', 5)	# 16-20
    sprite('Action_248_02', 5)	# 21-25
    Unknown23018(1)
    label(1)
    sprite('Action_248_03', 5)	# 26-30
    sprite('Action_248_04', 5)	# 31-35
    gotoLabel(1)