@Subroutine
def PreInit():
    Unknown12019('75686900000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFInitialVelocity(16000)
    Unknown12038(23000)
    Unknown12034(33)
    SuperFreezeDuration(-1500)
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(2)
    Unknown13039(2)
    Unknown2049(1)
    Unknown15019(2000)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15015(28, 30)
    Unknown14015(0, 600000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(350000, 800000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(350000, 800000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A_4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 800000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15021(1)
    Unknown14015(0, 750000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(350000, 1500000, -200000, 150000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk5B_2nd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(0, 1500000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B_3rd', 0x19)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15008()
    Unknown14015(0, 1500000, -200000, 600000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14015(250000, 1000000, 300000, 600000, 1000, 5)
    Move_EndRegister()
    Move_Register('NmlAtk2B_2nd', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown14015(250000, 1000000, 300000, 600000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(250000, 800000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown15009()
    Unknown14015(250000, 900000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C_2nd', 0x28)
    MoveMaxChainRepeat(1)
    Unknown14020(1)
    Unknown14005(1)
    Unknown15009()
    Unknown14015(250000, 900000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 450000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2nd', 0x10)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 650000, -500000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14015(450000, 1000000, -600000, -200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B_2nd', 0x22)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(450000, 1000000, -600000, -200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    MoveMaxChainRepeat(1)
    Unknown14015(250000, 650000, -400000, 100000, 1000, 50)
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
    Move_Register('MidShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown14015(350000, 1000000, -200000, 300000, 500, 25)
    Move_EndRegister()
    Move_Register('BackAttackShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(2000)
    Unknown14015(350000, 1500000, -200000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('LowShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15009()
    Unknown15013(1)
    Unknown14015(800000, 2000000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('DelayShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(4000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown14015(0, 550000, -200000, 300000, 500, 25)
    Move_EndRegister()
    Move_Register('AirDelayShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(450000, 900000, -500000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('SpreadShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown15011(10000)
    Unknown14015(800000, 1500000, -200000, 250000, 500, 25)
    Move_EndRegister()
    Move_Register('AirSpreadShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15011(10000)
    Unknown14015(800000, 1500000, -200000, 250000, 500, 25)
    Move_EndRegister()
    Move_Register('DropShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15008()
    Unknown15013(1)
    Unknown14015(800000, 2000000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('AirDropShot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_AirGround_(0x300d)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15008()
    Unknown15013(1)
    Unknown14015(800000, 2000000, -400000, 100000, 250, 10)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 450000, -200000, 600000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-50000, 450000, -200000, 600000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateAllRangeShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(1)
    Unknown15014(8000)
    Unknown15013(1)
    Unknown15012(0)
    Unknown14015(0, 1500000, -200000, 150000, 100, 1)
    Move_EndRegister()
    Move_Register('UltimateAllRangeShotOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15021(1)
    Unknown15014(8000)
    Unknown15013(1)
    Unknown15012(0)
    Unknown14015(0, 1500000, -200000, 150000, 100, 1)
    Move_EndRegister()
    Move_Register('UltimateStorm', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x300c)
    Unknown15013(4000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(350000, 1000000, -200000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateStormOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x300c)
    Unknown15013(4000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(350000, 1000000, -200000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('AirUltimateStorm', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x300c)
    Unknown15013(4000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(0, 600000, -500000, 100000, 250, 0)
    Move_EndRegister()
    Move_Register('AirUltimateStormOD', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x300c)
    Unknown15013(4000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(0, 600000, -500000, 100000, 250, 0)
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
    Unknown15024('NmlAtk5A', 'NmlAtk5A_2nd', 10000000)
    Unknown15024('NmlAtk5A_2nd', 'NmlAtk5A_3rd', 10000000)
    Unknown15024('NmlAtk5A_3rd', 'NmlAtk5A_4th', 10000000)
    Unknown15024('NmlAtk5A_3rd', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B_2nd', 10000000)
    Unknown15024('NmlAtk5B_2nd', 'NmlAtk5B_3rd', 10000000)
    Unknown15024('NmlAtk5B_3rd', 'NmlAtk5B_3rd', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2B_2nd', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('NmlAtk2B_2nd', 'BackAttackShot', 10000000)
    Unknown15024('NmlAtk2C', 'NmlAtk2C_2nd', 10000000)
    Unknown15024('NmlAtk2C_2nd', 'MidShot', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A_2nd', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5B_2nd', 10000000)
    Unknown15024('NmlAtkAIR5B_2nd', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5B_2nd', 'AirDelayShot', 10000000)
    Unknown15024('NmlAtkAIR5B_2nd', 'BJump', 10000000)
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
    Unknown12018(29, 'Action_291_00')
    Unknown12018(24, 'Action_348_00')
    Unknown7010(0, 'uhi000')
    Unknown7010(1, 'uhi001')
    Unknown7010(2, 'uhi002')
    Unknown7010(3, 'uhi003')
    Unknown7010(4, 'uhi004')
    Unknown7010(5, 'uhi005')
    Unknown7010(6, 'uhi006')
    Unknown7010(7, 'uhi007')
    Unknown7010(8, 'uhi008')
    Unknown7010(9, 'uhi009')
    Unknown7010(10, 'uhi010')
    Unknown7010(15, 'uhi011')
    Unknown7010(16, 'uhi012')
    Unknown7010(17, 'uhi013')
    Unknown7010(18, 'uhi014')
    Unknown7010(19, 'uhi015')
    Unknown7010(20, 'uhi016')
    Unknown7010(21, 'uhi017')
    Unknown7010(22, 'uhi018')
    Unknown7010(23, 'uhi019')
    Unknown7010(24, 'uhi020')
    Unknown7010(25, 'uhi021')
    Unknown7010(28, 'uhi022')
    Unknown7010(29, 'uhi023')
    Unknown7010(30, 'uhi024')
    Unknown7010(31, 'uhi025')
    Unknown7010(32, 'uhi026')
    Unknown7010(33, 'uhi027')
    Unknown7010(34, 'uhi028')
    Unknown7010(35, 'uhi029')
    Unknown7010(36, 'uhi030')
    Unknown7010(37, 'uhi031')
    Unknown7010(39, 'uhi032')
    Unknown7010(42, 'uhi033')
    Unknown7010(43, 'uhi034')
    Unknown7010(44, 'uhi035')
    Unknown7010(45, 'uhi036')
    Unknown7010(46, 'uhi037')
    Unknown7010(47, 'uhi038')
    Unknown7010(48, 'uhi039')
    Unknown7010(49, 'uhi040')
    Unknown7010(50, 'uhi041')
    Unknown7010(52, 'uhi042')
    Unknown7010(53, 'uhi043')
    Unknown7010(54, 'uhi100_0')
    Unknown7010(55, 'uhi100_1')
    Unknown7010(56, 'uhi100_2')
    Unknown7010(63, 'uhi101_0')
    Unknown7010(64, 'uhi101_1')
    Unknown7010(65, 'uhi101_2')
    Unknown7010(57, 'uhi102_0')
    Unknown7010(58, 'uhi102_1')
    Unknown7010(59, 'uhi102_2')
    Unknown7010(66, 'uhi103_0')
    Unknown7010(67, 'uhi103_1')
    Unknown7010(68, 'uhi103_2')
    Unknown7010(60, 'uhi104_0')
    Unknown7010(61, 'uhi104_1')
    Unknown7010(62, 'uhi104_2')
    Unknown7010(69, 'uhi105_0')
    Unknown7010(70, 'uhi105_1')
    Unknown7010(71, 'uhi105_2')
    Unknown7010(72, 'uhi150')
    Unknown7010(73, 'uhi151')
    Unknown7010(74, 'uhi152')
    Unknown7010(85, 'uhi153')
    Unknown7010(87, 'uhi154')
    Unknown7010(88, 'uhi155')
    Unknown7010(96, 'uhi161_0')
    Unknown7010(97, 'uhi161_1')
    Unknown7010(92, 'uhi162_0')
    Unknown7010(93, 'uhi162_1')
    Unknown7010(98, 'uhi163_0')
    Unknown7010(99, 'uhi163_1')
    Unknown7010(100, 'uhi164_0')
    Unknown7010(101, 'uhi164_1')
    Unknown7010(105, 'uhi165_0')
    Unknown7010(106, 'uhi165_1')
    Unknown7010(102, 'uhi166_0')
    Unknown7010(103, 'uhi166_1')
    Unknown7010(90, 'uhi167_0')
    Unknown7010(91, 'uhi167_1')
    Unknown7010(107, 'uhi168_0')
    Unknown7010(108, 'uhi168_1')
    Unknown7010(110, 'uhi169_0')
    Unknown7010(111, 'uhi169_1')
    Unknown7010(112, 'uhi159_0')
    Unknown7010(113, 'uhi159_1')
    Unknown7010(94, 'uhi400_0')
    Unknown7010(95, 'uhi400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d617465416c6c52616e676553686f74000000000000000000000000')
    Unknown12059('03000000556c74696d617465416c6c52616e676553686f744f4400000000000000000000')
    Unknown12059('04000000556c74696d61746553746f726d00000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746553746f726d4f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnPreDraw():
    Unknown23030('5548495f526576436f6c6f7200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def OnFrameStep():
    if Unknown46(10):
        SLOT_4 = 1
    else:
        SLOT_4 = 0
    if Unknown68('0100000000000000000000000000000000000000'):
        if (not Unknown46(11)):
            SLOT_5 = 0
            GFX_0('CrouchChair', 100)
            Unknown38(11, 1)
        else:
            Unknown23029(11, 22, 1)
    elif Unknown46(11):
        Unknown23029(11, 21, 1)
        if (not Unknown23148('CmnActCrouch2Stand')):
            SLOT_5 = 1
    if SLOT_37:
        SLOT_8 = 0
        SLOT_9 = 0

@Subroutine
def OnMainEnemyComboBreak():
    SLOT_10 = 0

@Subroutine
def OnDamage():
    if Unknown46(11):
        Unknown23029(11, 25, 1)

@Subroutine
def GuardAuraCreate():
    if (not SLOT_4):
        GFX_0('GuardAura', 100)
        Unknown38(10, 1)
    else:
        Unknown23029(10, 11, 0)

@State
def CmnActStand():
    label(0)
    sprite('Action_000_00', 6)	# 1-6	 **attackbox here**
    sprite('Action_000_01', 6)	# 7-12	 **attackbox here**
    sprite('Action_000_02', 6)	# 13-18	 **attackbox here**
    sprite('Action_000_03', 6)	# 19-24	 **attackbox here**
    sprite('Action_000_04', 6)	# 25-30	 **attackbox here**
    sprite('Action_000_05', 6)	# 31-36	 **attackbox here**
    sprite('Action_000_06', 6)	# 37-42	 **attackbox here**
    sprite('Action_000_07', 6)	# 43-48	 **attackbox here**
    sprite('Action_000_08', 6)	# 49-54	 **attackbox here**
    sprite('Action_000_09', 6)	# 55-60	 **attackbox here**
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    label(1)
    sprite('Action_000_11', 4)	# 61-64	 **attackbox here**
    SLOT_88 = 960
    SFX_1('uhi000')
    Unknown2037(3)
    sprite('Action_000_12', 5)	# 65-69	 **attackbox here**
    sprite('Action_000_13', 6)	# 70-75	 **attackbox here**
    sprite('Action_000_14', 4)	# 76-79	 **attackbox here**
    sprite('Action_000_15', 5)	# 80-84	 **attackbox here**
    label(2)
    sprite('Action_000_16', 6)	# 85-90	 **attackbox here**
    sprite('Action_000_17', 6)	# 91-96	 **attackbox here**
    sprite('Action_000_18', 6)	# 97-102	 **attackbox here**
    sprite('Action_000_19', 6)	# 103-108	 **attackbox here**
    sprite('Action_000_20', 6)	# 109-114	 **attackbox here**
    sprite('Action_000_21', 6)	# 115-120	 **attackbox here**
    sprite('Action_000_22', 6)	# 121-126	 **attackbox here**
    sprite('Action_000_23', 6)	# 127-132	 **attackbox here**
    sprite('Action_000_24', 6)	# 133-138	 **attackbox here**
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(2)
    sprite('Action_000_25', 5)	# 139-143	 **attackbox here**
    sprite('Action_000_26', 5)	# 144-148
    sprite('Action_000_27', 5)	# 149-153
    sprite('Action_000_28', 5)	# 154-158
    sprite('Action_000_29', 5)	# 159-163
    sprite('Action_000_30', 5)	# 164-168
    sprite('Action_000_31', 5)	# 169-173
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('Action_015_00', 3)	# 1-3
    sprite('Action_015_01', 3)	# 4-6

@State
def CmnActStand2Crouch():
    sprite('Action_012_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_012_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_012_02', 4)	# 11-14	 **attackbox here**
    sprite('Action_012_03', 2)	# 15-16	 **attackbox here**
    sprite('Action_012_04', 5)	# 17-21	 **attackbox here**
    sprite('Action_012_05', 5)	# 22-26	 **attackbox here**

@State
def CmnActCrouch():
    sprite('Action_013_00', 4)	# 1-4	 **attackbox here**
    label(0)
    sprite('Action_013_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_013_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_013_03', 4)	# 13-16	 **attackbox here**
    sprite('Action_013_04', 4)	# 17-20	 **attackbox here**
    sprite('Action_013_05', 4)	# 21-24	 **attackbox here**
    sprite('Action_013_06', 4)	# 25-28	 **attackbox here**
    sprite('Action_013_07', 4)	# 29-32	 **attackbox here**
    sprite('Action_013_08', 4)	# 33-36	 **attackbox here**
    sprite('Action_013_09', 4)	# 37-40	 **attackbox here**
    sprite('Action_013_10', 4)	# 41-44	 **attackbox here**
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('Action_013_11', 6)	# 45-50	 **attackbox here**
    SLOT_88 = 960
    SFX_1('uhi004')
    sprite('Action_013_12', 8)	# 51-58	 **attackbox here**
    sprite('Action_013_13', 7)	# 59-65	 **attackbox here**
    sprite('Action_013_14', 10)	# 66-75	 **attackbox here**
    sprite('Action_013_15', 7)	# 76-82	 **attackbox here**
    sprite('Action_013_13', 7)	# 83-89	 **attackbox here**
    sprite('Action_013_14', 10)	# 90-99	 **attackbox here**
    sprite('Action_013_21', 6)	# 100-105	 **attackbox here**
    sprite('Action_013_19', 5)	# 106-110	 **attackbox here**
    sprite('Action_013_20', 8)	# 111-118	 **attackbox here**
    sprite('Action_013_21', 6)	# 119-124	 **attackbox here**
    sprite('Action_013_22', 1)	# 125-125	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():

    def upon_IMMEDIATE():
        GFX_0('CrouchTurnChair', 100)
        Unknown23029(11, 23, 1)

        def upon_STATE_END():
            Unknown23029(11, 24, 1)
    sprite('Action_016_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_016_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouch2Stand():
    sprite('Action_014_00', 4)	# 1-4	 **attackbox here**
    sprite('Action_014_01', 5)	# 5-9	 **attackbox here**
    sprite('Action_014_02', 5)	# 10-14	 **attackbox here**
    sprite('Action_014_03', 5)	# 15-19	 **attackbox here**
    sprite('Action_014_04', 4)	# 20-23	 **attackbox here**
    sprite('Action_014_05', 2)	# 24-25	 **attackbox here**
    sprite('Action_014_06', 4)	# 26-29	 **attackbox here**

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
    sprite('Action_036_02', 3)	# 4-6
    sprite('Action_036_03', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_01', 3)	# 10-12
    sprite('Action_035_02', 32767)	# 13-32779
    label(2)
    sprite('Action_037_01', 4)	# 32780-32783
    sprite('Action_037_02', 4)	# 32784-32787
    sprite('Action_037_03', 4)	# 32788-32791
    sprite('Action_037_04', 32767)	# 32792-65558

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_036_04', 4)	# 1-4
    sprite('Action_036_05', 3)	# 5-7
    sprite('Action_036_06', 5)	# 8-12
    sprite('Action_036_07', 5)	# 13-17
    sprite('Action_036_08', 5)	# 18-22
    ExitState()
    label(1)
    sprite('Action_035_03', 5)	# 23-27
    sprite('Action_035_04', 6)	# 28-33
    sprite('Action_035_05', 5)	# 34-38
    sprite('Action_035_06', 4)	# 39-42
    ExitState()
    label(2)
    sprite('Action_037_05', 4)	# 43-46
    sprite('Action_037_06', 4)	# 47-50
    ExitState()

@State
def CmnActJumpDown():
    Unknown23145('NmlAtkAIR5A')
    if SLOT_ReturnVal:
        _gotolabel(3)
    Unknown23145('NmlAtkAIR5A_2nd')
    if SLOT_ReturnVal:
        _gotolabel(3)
    Unknown23145('UltimateStorm')
    if SLOT_ReturnVal:
        _gotolabel(3)
    Unknown23145('UltimateStormOD')
    if SLOT_ReturnVal:
        _gotolabel(3)
    Unknown23145('AirUltimateStorm')
    if SLOT_ReturnVal:
        _gotolabel(3)
    Unknown23145('AirUltimateStormOD')
    if SLOT_ReturnVal:
        _gotolabel(3)
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    label(0)
    sprite('Action_020_00', 3)	# 1-3
    sprite('Action_020_01', 3)	# 4-6
    sprite('Action_020_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_035_07', 3)	# 10-12
    sprite('Action_035_08', 3)	# 13-15
    sprite('Action_035_09', 3)	# 16-18
    gotoLabel(1)
    label(2)
    sprite('Action_037_07', 3)	# 19-21
    sprite('Action_037_08', 3)	# 22-24
    sprite('Action_037_09', 3)	# 25-27
    gotoLabel(2)
    label(3)
    sprite('Action_009_11', 3)	# 28-30
    sprite('Action_009_12', 3)	# 31-33
    gotoLabel(3)
    label(3)
    sprite('Action_008_10', 3)	# 34-36
    sprite('Action_008_11', 3)	# 37-39
    sprite('Action_008_12', 3)	# 40-42
    gotoLabel(3)

@State
def CmnActJumpLanding():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('Action_021_00', 6)	# 1-6
    sprite('Action_021_01', 6)	# 7-12
    ExitState()
    label(1)
    sprite('Action_035_10', 6)	# 13-18
    sprite('Action_035_11', 6)	# 19-24
    ExitState()
    label(2)
    sprite('Action_037_10', 6)	# 25-30
    sprite('Action_037_11', 6)	# 31-36
    ExitState()

@State
def CmnActLandingStiffLoop():
    sprite('Action_041_07', 3)	# 1-3
    sprite('Action_041_08', 32767)	# 4-32770

@State
def CmnActLandingStiffEnd():
    sprite('Action_041_09', 3)	# 1-3
    sprite('Action_041_10', 3)	# 4-6

@State
def CmnActFWalk():
    label(0)
    sprite('Action_010_00', 4)	# 1-4
    sprite('Action_010_01', 4)	# 5-8
    sprite('Action_010_02', 4)	# 9-12
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_03', 4)	# 13-16
    sprite('Action_010_04', 4)	# 17-20
    sprite('Action_010_05', 4)	# 21-24
    sprite('Action_010_06', 4)	# 25-28
    sprite('Action_010_07', 4)	# 29-32
    sprite('Action_010_08', 4)	# 33-36
    sprite('Action_010_09', 4)	# 37-40
    sprite('Action_010_10', 4)	# 41-44
    sprite('Action_010_11', 4)	# 45-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_010_12', 4)	# 49-52
    sprite('Action_010_13', 4)	# 53-56
    sprite('Action_010_14', 4)	# 57-60
    sprite('Action_010_15', 4)	# 61-64
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    label(0)
    sprite('Action_011_00', 4)	# 1-4
    sprite('Action_011_01', 4)	# 5-8
    sprite('Action_011_02', 4)	# 9-12
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_03', 4)	# 13-16
    sprite('Action_011_04', 4)	# 17-20
    sprite('Action_011_05', 4)	# 21-24
    sprite('Action_011_06', 4)	# 25-28
    sprite('Action_011_07', 4)	# 29-32
    sprite('Action_011_08', 4)	# 33-36
    sprite('Action_011_09', 4)	# 37-40
    sprite('Action_011_10', 4)	# 41-44
    sprite('Action_011_11', 4)	# 45-48
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('Action_011_12', 4)	# 49-52
    sprite('Action_011_13', 4)	# 53-56
    sprite('Action_011_14', 4)	# 57-60
    sprite('Action_011_15', 4)	# 61-64
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('Action_010_00', 2)	# 1-2
    sprite('Action_045_00', 4)	# 3-6
    sprite('Action_045_01', 3)	# 7-9
    SFX_3('SE050_SlideDash')

    def upon_CLEAR_OR_EXIT():
        Unknown2038(1)
        if (SLOT_2 >= 3):
            Unknown2037(0)
            GFX_0('DashEff', 100)
    label(0)
    sprite('Action_045_02', 3)	# 10-12
    Unknown8006(100, 1, 0)
    sprite('Action_045_03', 4)	# 13-16
    sprite('Action_045_04', 4)	# 17-20
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('Action_045_05', 4)	# 1-4
    sprite('Action_045_06', 3)	# 5-7

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
            Unknown1019(95)
            Unknown2038(1)
            if (SLOT_2 >= 3):
                Unknown2037(0)
                GFX_0('BackDashEff', 100)
    sprite('Action_046_00', 2)	# 1-2
    sprite('Action_046_01', 2)	# 3-4
    physicsXImpulse(-25800)
    Unknown8002()
    SFX_1('uhi006')
    sprite('Action_046_02', 3)	# 5-7
    sprite('Action_046_03', 3)	# 8-10
    sprite('Action_046_04', 4)	# 11-14
    sprite('Action_046_05', 4)	# 15-18
    sprite('Action_046_06', 4)	# 19-22
    sprite('Action_046_07', 4)	# 23-26
    Unknown8000(100, 1, 1)
    clearUponHandler(3)
    Unknown1019(10)
    sprite('Action_046_08', 2)	# 27-28

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
    sprite('Action_046_00', 2)	# 1-2
    physicsYImpulse(12000)
    sprite('Action_046_01', 2)	# 3-4
    sprite('Action_046_02', 2)	# 5-6
    sprite('Action_046_04', 3)	# 7-9
    sprite('Action_046_07', 3)	# 10-12
    sprite('Action_046_00', 32767)	# 13-32779

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
    sprite('Action_305_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_02', 1)	# 2-2	 **attackbox here**
    sprite('Action_305_03', 2)	# 3-4	 **attackbox here**

@State
def CmnActHitCrouchLv2():
    sprite('Action_305_02', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_02', 2)	# 2-3	 **attackbox here**
    sprite('Action_305_03', 3)	# 4-6	 **attackbox here**

@State
def CmnActHitCrouchLv3():
    sprite('Action_305_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_00', 2)	# 2-3	 **attackbox here**
    sprite('Action_305_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_305_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_305_03', 2)	# 8-9	 **attackbox here**

@State
def CmnActHitCrouchLv4():
    sprite('Action_305_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_00', 1)	# 2-2	 **attackbox here**
    sprite('Action_305_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_305_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_305_03', 2)	# 9-10	 **attackbox here**

@State
def CmnActHitCrouchLv5():
    sprite('Action_305_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_305_00', 3)	# 2-4	 **attackbox here**
    sprite('Action_305_01', 4)	# 5-8	 **attackbox here**
    sprite('Action_305_02', 4)	# 9-12	 **attackbox here**
    sprite('Action_305_03', 4)	# 13-16	 **attackbox here**

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
    sprite('Action_326_01', 3)	# 1-3
    sprite('Action_326_02', 3)	# 4-6

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
    sprite('Action_041_04', 3)	# 15-17
    label(0)
    sprite('Action_041_05', 3)	# 18-20
    sprite('Action_041_06', 3)	# 21-23
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('Action_041_07', 4)	# 1-4
    sprite('Action_041_08', 4)	# 5-8
    sprite('Action_041_09', 4)	# 9-12
    sprite('Action_041_10', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('Action_017_00', 3)	# 1-3
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    sprite('Action_017_00', 3)	# 1-3
    callSubroutine('GuardAuraCreate')
    sprite('Action_017_01', 3)	# 4-6
    label(0)
    sprite('Action_017_00', 3)	# 7-9
    sprite('Action_017_01', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('Action_017_00', 3)	# 1-3
    callSubroutine('GuardAuraCreate')
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
    callSubroutine('GuardAuraCreate')

@State
def CmnActHighGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('Action_017_00', 3)	# 1-3
    callSubroutine('GuardAuraCreate')
    sprite('Action_017_01', 3)	# 4-6

@State
def CmnActHighHeavyGuardEnd():
    sprite('Action_017_06', 3)	# 1-3
    sprite('Action_017_07', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('Action_018_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchGuardLoop():
    sprite('Action_018_02', 3)	# 1-3	 **attackbox here**
    callSubroutine('GuardAuraCreate')
    sprite('Action_018_03', 3)	# 4-6	 **attackbox here**
    label(0)
    sprite('Action_018_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_018_03', 3)	# 10-12	 **attackbox here**
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('Action_018_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('Action_018_01', 3)	# 1-3	 **attackbox here**
    callSubroutine('GuardAuraCreate')
    sprite('Action_018_02', 3)	# 4-6	 **attackbox here**

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('Action_018_06', 3)	# 1-3	 **attackbox here**
    sprite('Action_018_07', 3)	# 4-6	 **attackbox here**

@State
def CmnActAirGuardPre():
    sprite('Action_019_00', 3)	# 1-3
    sprite('Action_019_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    sprite('Action_019_02', 3)	# 1-3
    callSubroutine('GuardAuraCreate')
    sprite('Action_019_03', 3)	# 4-6
    label(0)
    sprite('Action_019_02', 3)	# 7-9
    sprite('Action_019_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('Action_019_02', 3)	# 1-3
    callSubroutine('GuardAuraCreate')
    sprite('Action_019_03', 3)	# 4-6

@State
def CmnActAirHeavyGuardEnd():
    sprite('Action_019_06', 3)	# 1-3
    sprite('Action_019_07', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('Action_017_00', 2)	# 1-2
    callSubroutine('GuardAuraCreate')
    sprite('Action_017_01', 2)	# 3-4
    sprite('Action_017_00', 1)	# 5-5
    Unknown2042(1)
    sprite('Action_017_06', 6)	# 6-11
    sprite('Action_017_07', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('Action_018_00', 2)	# 1-2	 **attackbox here**
    callSubroutine('GuardAuraCreate')
    sprite('Action_018_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_018_00', 1)	# 5-5	 **attackbox here**
    Unknown2042(1)
    sprite('Action_018_01', 6)	# 6-11	 **attackbox here**
    sprite('Action_018_00', 6)	# 12-17	 **attackbox here**

@State
def CmnActGuardBreakAir():
    sprite('Action_019_00', 2)	# 1-2
    callSubroutine('GuardAuraCreate')
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
    sprite('Action_002_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_002_03', 6)	# 8-13	 **attackbox here**
    sprite('Action_002_04', 6)	# 14-19	 **attackbox here**
    sprite('Action_002_08', 4)	# 20-23
    GFX_0('EffAtkCrush1stMain', 100)
    sprite('Action_002_10', 4)	# 24-27
    sprite('Action_002_11', 4)	# 28-31

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
    sprite('Action_262_09', 4)	# 7-10
    sprite('Action_262_10', 4)	# 11-14
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
    sprite('Action_262_09', 4)	# 7-10
    sprite('Action_262_10', 4)	# 11-14
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
    sprite('Action_026_04', 32767)	# 32-32798	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    label(1)
    sprite('keep', 1)	# 32799-32799
    sprite('Action_152_05', 5)	# 32800-32804
    GFX_0('EffAtkAIR5A', 100)
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_152_06', 17)	# 32805-32821
    sprite('Action_152_07', 8)	# 32822-32829

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('Action_152_05', 1)	# 2-2
    Unknown18009(1)
    sprite('Action_012_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_012_02', 3)	# 6-8	 **attackbox here**
    sprite('Action_012_03', 1)	# 9-9	 **attackbox here**
    sprite('Action_012_04', 3)	# 10-12	 **attackbox here**
    sprite('Action_012_05', 3)	# 13-15	 **attackbox here**
    sprite('Action_422_00', 1)	# 16-16	 **attackbox here**
    sprite('Action_422_01', 2)	# 17-18	 **attackbox here**
    sprite('Action_422_02', 8)	# 19-26	 **attackbox here**
    sprite('Action_422_02', 8)	# 27-34	 **attackbox here**
    GFX_0('EffCrushFinish', 100)
    Unknown7009(2)
    sprite('Action_422_02ex01', 3)	# 35-37	 **attackbox here**
    sprite('Action_422_03', 4)	# 38-41	 **attackbox here**
    sprite('Action_422_04', 3)	# 42-44	 **attackbox here**
    sprite('Action_422_05', 3)	# 45-47	 **attackbox here**
    sprite('Action_424_00', 4)	# 48-51	 **attackbox here**
    sprite('Action_424_01', 5)	# 52-56	 **attackbox here**
    sprite('Action_424_02', 12)	# 57-68	 **attackbox here**
    sprite('Action_424_03', 4)	# 69-72	 **attackbox here**
    sprite('Action_424_04', 3)	# 73-75	 **attackbox here**

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
        Damage(550)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(2)
        PushbackX(25000)
        AirPushbackX(12000)
        AirPushbackY(18000)
        Unknown1112('')
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown30055('20a10700c8000000c8000000')
        Unknown30056('a08601006400000064000000')
    sprite('Action_402_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_402_01', 3)	# 3-5	 **attackbox here**
    sprite('Action_402_02', 3)	# 6-8	 **attackbox here**
    SFX_4('uhi108_0')
    SFX_3('SE_Hari_Appear')
    sprite('Action_402_03', 3)	# 9-11	 **attackbox here**
    sprite('Action_402_04ex02', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    sprite('Action_402_05', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('Action_402_06', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    sprite('Action_402_07', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    Unknown30055('ffffffffffffffffffffffff')
    Unknown30056('ffffffffffffffffffffffff')

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5A_2nd')
    sprite('Action_402_07', 1)	# 19-19	 **attackbox here**
    HitOrBlockCancel('NmlAtk5A_2nd')
    sprite('Action_402_08', 4)	# 20-23
    GFX_0('EffAtk5A', 100)
    Recovery()
    Unknown2063()
    sprite('Action_402_09', 4)	# 24-27
    sprite('Action_402_10', 4)	# 28-31
    sprite('Action_402_11', 4)	# 32-35
    sprite('Action_402_14', 4)	# 36-39
    sprite('Action_402_15', 4)	# 40-43

@State
def NmlAtk5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        PushbackX(9900)
        AirPushbackY(15000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A_3rd')
        callSubroutine('ChainRoot')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('Action_003_19', 3)	# 1-3
    sprite('Action_003_20', 1)	# 4-4	 **attackbox here**
    sprite('Action_003_21', 2)	# 5-6	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    SFX_4('uhi110_2')
    sprite('Action_003_22', 2)	# 7-8	 **attackbox here**
    sprite('Action_003_23', 2)	# 9-10	 **attackbox here**
    sprite('Action_003_24ex01', 3)	# 11-13	 **attackbox here**
    sprite('Action_003_25', 3)	# 14-16	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_003_26', 3)	# 17-19	 **attackbox here**
    sprite('Action_003_27', 4)	# 20-23
    GFX_0('EffAtk5A2nd', 100)
    sprite('Action_003_28', 4)	# 24-27
    sprite('Action_003_31', 4)	# 28-31
    sprite('Action_003_32', 3)	# 32-34
    sprite('Action_003_33', 3)	# 35-37

@State
def NmlAtk5A_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP2(70)
        Unknown9016(1)
        PushbackX(-30400)
        AirPushbackX(-11700)
        AirPushbackY(25000)
        YImpluseBeforeWallbounce(2500)
        hitstun(22)
        AirUntechableTime(22)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        HitOrBlockCancel('NmlAtk5A_4th')
        callSubroutine('ChainRoot')
    sprite('Action_147_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_147_01', 4)	# 4-7	 **attackbox here**
    sprite('Action_147_02', 2)	# 8-9	 **attackbox here**
    sprite('Action_147_03', 2)	# 10-11	 **attackbox here**
    sprite('Action_147_04', 2)	# 12-13	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_147_05', 2)	# 14-15	 **attackbox here**
    sprite('Action_147_06ex01', 1)	# 16-16	 **attackbox here**
    sprite('Action_147_07', 3)	# 17-19	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_147_08', 5)	# 20-24	 **attackbox here**
    sprite('Action_147_09', 4)	# 25-28
    GFX_0('EffAtk5A3rd', 100)
    sprite('Action_147_10', 4)	# 29-32
    sprite('Action_147_11', 4)	# 33-36

@State
def NmlAtk5A_4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 101):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('Action_055_00', 6)	# 1-6
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 6)	# 7-12	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_01', 2)	# 13-14	 **attackbox here**
    GFX_0('EffAtk5AAAA_1st', 100)
    sprite('Action_055_03', 23)	# 15-37
    SFX_3('SE042')
    GFX_0('EffAtkThrowMiss', 100)
    sprite('Action_055_04', 7)	# 38-44
    sprite('Action_055_05', 8)	# 45-52
    sprite('Action_055_06', 5)	# 53-57
    ExitState()
    label(1)
    sprite('Action_056_01', 15)	# 58-72
    setInvincible(1)

    def upon_78():
        clearUponHandler(78)
        GFX_0('ThrowHitmarkMatome', 100)
    Unknown7006('uhi156_0', 100, 828991605, 828323381, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_056_01', 3)	# 73-75
    GFX_0('EffAtk5AAAA_Exe', 100)
    sprite('Action_056_02', 4)	# 76-79
    sprite('Action_056_02', 1)	# 80-80
    sprite('Action_057_00', 3)	# 81-83
    sprite('Action_057_01', 3)	# 84-86
    sprite('Action_057_02', 2)	# 87-88
    sprite('Action_057_03', 2)	# 89-90
    sprite('Action_057_04ex01', 14)	# 91-104	 **attackbox here**
    GFX_0('EffAtk5AAAA_Exe_Dmykcol', 100)
    sprite('Action_057_05', 8)	# 105-112
    sprite('Action_057_05', 5)	# 113-117
    Recovery()
    Unknown2063()
    sprite('Action_057_06', 8)	# 118-125
    sprite('Action_057_07', 7)	# 126-132
    sprite('Action_057_08', 6)	# 133-138

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk5B_2nd')
        HitJumpCancel(1)
    sprite('Action_170_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_170_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_170_02', 1)	# 5-5	 **attackbox here**
    Unknown7006('uhi200_0', 100, 845768821, 828321840, 0, 0, 100, 845768821, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_170_03', 1)	# 6-6	 **attackbox here**
    sprite('Action_170_04', 2)	# 7-8	 **attackbox here**
    sprite('Action_170_05', 2)	# 9-10	 **attackbox here**
    sprite('Action_170_06', 2)	# 11-12	 **attackbox here**
    SFX_3('SE_BallExplosion')
    GFX_0('EffAtk5B_Atk', 0)
    sprite('Action_170_07', 5)	# 13-17	 **attackbox here**
    sprite('Action_170_08', 16)	# 18-33	 **attackbox here**
    sprite('Action_170_09', 7)	# 34-40	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_170_10', 6)	# 41-46
    sprite('Action_170_11', 6)	# 47-52

@State
def NmlAtk5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk5B_3rd')
        HitOrBlockCancel('CmnActCrushAttack')
        if SLOT_10:
            SLOT_51 = 1
        SLOT_10 = 0
    sprite('Action_420_00', 1)	# 1-1	 **attackbox here**
    sprite('Action_420_00', 7)	# 2-8	 **attackbox here**
    Unknown23029(11, 26, 1)
    sprite('Action_420_01', 8)	# 9-16	 **attackbox here**
    SFX_1('uhi214_1')
    sprite('Action_420_02', 4)	# 17-20	 **attackbox here**
    GFX_0('EffAtk5BB_Atk', 100)
    if SLOT_51:
        Unknown23029(1, 103, 0)
    sprite('Action_420_02', 11)	# 21-31	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_420_03', 5)	# 32-36	 **attackbox here**
    sprite('Action_420_04', 5)	# 37-41	 **attackbox here**
    sprite('Action_420_05', 5)	# 42-46	 **attackbox here**

@State
def NmlAtk5B_3rd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('Action_431_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_431_00', 2)	# 4-5	 **attackbox here**
    sprite('Action_431_01', 7)	# 6-12	 **attackbox here**
    sprite('Action_431_02', 10)	# 13-22	 **attackbox here**
    Unknown7006('uhi212_1', 100, 845768821, 845099569, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    GFX_0('EffDropShot_Pacchin', 0)
    GFX_0('Eff5BBB_Atk', 0)
    sprite('Action_431_03', 3)	# 23-25	 **attackbox here**
    sprite('Action_431_04', 8)	# 26-33	 **attackbox here**
    sprite('Action_431_05', 8)	# 34-41	 **attackbox here**
    sprite('Action_431_06', 10)	# 42-51	 **attackbox here**
    sprite('Action_431_07', 7)	# 52-58	 **attackbox here**

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Unknown9016(1)
        callSubroutine('ChainRoot')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('Action_005_01', 2)	# 1-2	 **attackbox here**
    sprite('Action_005_02', 2)	# 3-4	 **attackbox here**
    sprite('Action_005_03', 3)	# 5-7	 **attackbox here**
    sprite('Action_005_04', 3)	# 8-10	 **attackbox here**
    Unknown7007('7568693130385f310000000000000000640000007568693130345f300000000000000000210000007568693130345f303200000000000000210000000000000000000000000000000000000000000000')
    SFX_3('SE_Hari_Appear')
    sprite('Action_005_05ex01', 4)	# 11-14	 **attackbox here**
    sprite('Action_005_06', 4)	# 15-18	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_005_07', 4)	# 19-22	 **attackbox here**
    sprite('Action_005_08', 5)	# 23-27	 **attackbox here**
    GFX_0('EffAtkCrush1stSub', 100)
    sprite('Action_005_09', 5)	# 28-32	 **attackbox here**
    sprite('Action_005_10', 4)	# 33-36	 **attackbox here**

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackY(20000)
        AirUntechableTime(22)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        callSubroutine('ChainRoot')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('NmlAtk2B_2nd')
    sprite('Action_006_12', 2)	# 1-2	 **attackbox here**
    sprite('Action_006_13', 2)	# 3-4	 **attackbox here**
    sprite('Action_006_14', 2)	# 5-6	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    Unknown7007('7568693130385f320000000000000000640000007568693130365f300000000000000000210000007568693130355f300000000000000000210000007568693130355f31000000000000000021000000')
    sprite('Action_006_15', 2)	# 7-8	 **attackbox here**
    sprite('Action_006_16', 2)	# 9-10	 **attackbox here**
    Unknown14070('NmlAtk2B_2nd')
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('Action_006_17ex01', 3)	# 11-13	 **attackbox here**
    sprite('Action_006_18', 7)	# 14-20	 **attackbox here**
    setInvincible(0)
    Recovery()
    Unknown2063()
    Unknown14072('NmlAtk2B_2nd')
    sprite('Action_006_19', 3)	# 21-23	 **attackbox here**
    GFX_0('EffAtk2B', 100)
    Unknown14074('NmlAtk2B_2nd')
    sprite('Action_006_20', 3)	# 24-26	 **attackbox here**
    sprite('Action_006_21', 4)	# 27-30	 **attackbox here**
    sprite('Action_006_22', 4)	# 31-34	 **attackbox here**

@State
def NmlAtk2B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        PushbackX(-30400)
        AirPushbackX(-6500)
        AirPushbackY(22000)
        AirUntechableTime(32)
        Unknown11001(0, 3, 5)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9016(1)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5B')
    sprite('Action_148_14', 2)	# 1-2	 **attackbox here**
    sprite('Action_148_15', 2)	# 3-4	 **attackbox here**
    sprite('Action_148_16', 3)	# 5-7	 **attackbox here**
    sprite('Action_148_17', 3)	# 8-10	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_148_18', 2)	# 11-12	 **attackbox here**
    sprite('Action_148_19', 3)	# 13-15	 **attackbox here**
    sprite('Action_148_20', 4)	# 16-19	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_148_21', 4)	# 20-23	 **attackbox here**
    GFX_0('EffAtk2BB', 100)
    sprite('Action_148_22', 4)	# 24-27	 **attackbox here**
    sprite('Action_148_23', 4)	# 28-31	 **attackbox here**
    sprite('Action_148_24', 4)	# 32-35	 **attackbox here**
    sprite('Action_148_25', 4)	# 36-39	 **attackbox here**
    sprite('Action_148_26', 4)	# 40-43	 **attackbox here**
    sprite('Action_148_27', 4)	# 44-47	 **attackbox here**

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirPushbackY(20000)
        AirUntechableTime(22)
        Unknown9016(1)
        HitLow(2)
        callSubroutine('ChainRoot')

        def upon_ON_HIT_OR_BLOCK():
            Unknown14072('NmlAtk2C_2nd')
    sprite('Action_006_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_006_01', 3)	# 4-6	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    Unknown7007('7568693130395f300000000000000000640000007568693130375f300000000000000000210000007568693330355f300000000000000000210000000000000000000000000000000000000000000000')
    sprite('Action_006_02', 3)	# 7-9	 **attackbox here**
    sprite('Action_006_03', 2)	# 10-11	 **attackbox here**
    sprite('Action_006_04', 2)	# 12-13	 **attackbox here**
    Unknown14070('NmlAtk2C_2nd')
    sprite('Action_006_05ex01', 3)	# 14-16	 **attackbox here**
    sprite('Action_006_06', 7)	# 17-23	 **attackbox here**
    Unknown14072('NmlAtk2C_2nd')
    Recovery()
    Unknown2063()
    sprite('Action_006_07', 5)	# 24-28	 **attackbox here**
    GFX_0('EffAtk2C', 100)
    Unknown14074('NmlAtk2C_2nd')
    sprite('Action_006_08', 5)	# 29-33	 **attackbox here**
    sprite('Action_006_09', 5)	# 34-38	 **attackbox here**
    sprite('Action_006_10', 7)	# 39-45	 **attackbox here**

@State
def NmlAtk2C_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        PushbackX(-30400)
        AirPushbackX(-6500)
        AirPushbackY(20000)
        AirUntechableTime(32)
        Unknown11001(0, 3, 5)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        Unknown9016(1)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
    sprite('Action_148_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_148_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_148_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_148_03', 3)	# 8-10	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_148_04', 2)	# 11-12	 **attackbox here**
    sprite('Action_148_05', 3)	# 13-15	 **attackbox here**
    sprite('Action_148_06', 4)	# 16-19	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_148_07', 4)	# 20-23	 **attackbox here**
    GFX_0('EffAtk2CC', 100)
    sprite('Action_148_08', 4)	# 24-27	 **attackbox here**
    sprite('Action_148_09', 4)	# 28-31	 **attackbox here**
    sprite('Action_148_10', 4)	# 32-35	 **attackbox here**
    sprite('Action_148_11', 4)	# 36-39	 **attackbox here**
    sprite('Action_148_12', 4)	# 40-43	 **attackbox here**
    sprite('Action_148_13', 4)	# 44-47	 **attackbox here**

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(22000)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtkAIR5A_2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_026_00ex01', 3)	# 1-3
    sprite('Action_026_00', 3)	# 4-6	 **attackbox here**
    sprite('Action_026_01', 3)	# 7-9	 **attackbox here**
    Unknown7007('7568693130325f310000000000000000640000007568693130365f310000000000000000640000007568693130365f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('SE_Hari_Appear')
    sprite('Action_026_02', 3)	# 10-12	 **attackbox here**
    sprite('Action_026_03', 3)	# 13-15	 **attackbox here**
    sprite('Action_026_04', 3)	# 16-18	 **attackbox here**
    sprite('Action_026_05', 4)	# 19-22	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_026_06', 4)	# 23-26	 **attackbox here**
    sprite('Action_026_07', 6)	# 27-32
    GFX_0('EffAtkAIR5A', 100)
    sprite('Action_026_08', 6)	# 33-38

@State
def NmlAtkAIR5A_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackY(18000)
        AirUntechableTime(22)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('Action_008_00', 3)	# 1-3
    sprite('Action_008_01', 3)	# 4-6	 **attackbox here**
    sprite('Action_008_02', 3)	# 7-9	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    Unknown7009(4)
    sprite('Action_008_03', 3)	# 10-12	 **attackbox here**
    sprite('Action_008_04', 3)	# 13-15
    GFX_0('EffAtkAIR5AA', 100)
    Recovery()
    Unknown2063()
    sprite('Action_008_05', 3)	# 16-18
    sprite('Action_008_06', 3)	# 19-21
    sprite('Action_008_07', 5)	# 22-26
    sprite('Action_008_08', 5)	# 27-31
    sprite('Action_008_09', 5)	# 32-36

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtkAIR5B_2nd')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_STATE_END():
            Unknown23029(7, 51, 0)
            Unknown23029(8, 52, 0)
    sprite('Action_179_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_179_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_179_02', 1)	# 5-5	 **attackbox here**
    Unknown1084(1)
    setGravity(0)
    GFX_0('AirStandFront', 100)
    Unknown38(7, 1)
    GFX_0('AirStandBack', 100)
    Unknown38(8, 1)
    Unknown7006('uhi200_0', 100, 845768821, 828321840, 0, 0, 100, 845768821, 845099056, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_179_03', 1)	# 6-6	 **attackbox here**
    sprite('Action_179_04', 2)	# 7-8	 **attackbox here**
    sprite('Action_179_05', 2)	# 9-10	 **attackbox here**
    sprite('Action_179_06', 2)	# 11-12	 **attackbox here**
    SFX_3('SE_BallExplosion')
    GFX_0('EffAtkAIR5B_Atk', 0)
    sprite('Action_179_07', 5)	# 13-17	 **attackbox here**
    sprite('Action_179_08', 16)	# 18-33	 **attackbox here**
    sprite('Action_179_09', 7)	# 34-40	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('Action_179_10', 6)	# 41-46
    sprite('Action_179_11', 6)	# 47-52
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23029(7, 51, 0)
    Unknown23029(8, 52, 0)
    label(0)
    sprite('Action_020_00', 3)	# 53-55
    sprite('Action_020_01', 3)	# 56-58
    sprite('Action_020_02', 3)	# 59-61
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 3)	# 62-64
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    clearUponHandler(1)
    sprite('Action_021_01', 3)	# 65-67

@State
def NmlAtkAIR5B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown2003(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_STATE_END():
            Unknown1051(0)
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_125_00', 1)	# 1-1
    sprite('Action_125_01', 1)	# 2-2
    sprite('Action_125_02', 2)	# 3-4
    sprite('Action_125_03', 2)	# 5-6
    sprite('Action_125_04', 2)	# 7-8
    GFX_0('EffWarpOut', 100)
    sprite('Action_125_05', 2)	# 9-10
    setInvincible(1)
    sprite('Action_125_06', 3)	# 11-13
    Unknown3004(-85)
    sprite('null', 1)	# 14-14
    Unknown3001(0)
    sprite('null', 1)	# 15-15
    Unknown1086(22)
    teleportRelativeX(-280000)
    Unknown1007(12000)
    sprite('Action_145_00', 2)	# 16-17
    Unknown2006()
    GFX_0('EffWarpIn', 100)
    Unknown3004(51)
    Unknown1045(-12000)
    sendToLabelUpon(2, 1)
    Unknown7006('uhi209_0', 0, 845768821, 828324144, 0, 0, 100, 845768821, 845101360, 0, 0, 100, 0, 0, 0, 0, 0)
    setInvincible(0)
    sprite('Action_145_01', 7)	# 18-24
    GFX_0('EffAtkAIR5BBAtkMatome', 0)
    physicsYImpulse(10000)
    Unknown3001(255)
    setGravity(500)
    sprite('Action_145_02', 6)	# 25-30
    sprite('Action_145_03', 5)	# 31-35
    sprite('Action_145_04', 7)	# 36-42
    sprite('Action_145_05', 6)	# 43-48
    Recovery()
    sprite('Action_145_06', 5)	# 49-53
    Unknown1043()
    sprite('Action_145_07', 5)	# 54-58
    sprite('Action_145_08', 5)	# 59-63
    label(0)
    sprite('Action_145_06', 5)	# 64-68
    sprite('Action_145_07', 5)	# 69-73
    sprite('Action_145_08', 5)	# 74-78
    gotoLabel(0)
    label(1)
    sprite('Action_145_09', 5)	# 79-83
    Unknown1084(1)
    sprite('Action_145_10', 5)	# 84-88
    sprite('Action_145_11', 5)	# 89-93
    sprite('Action_145_12', 5)	# 94-98

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Unknown9016(1)
        AirUntechableTime(60)
        Unknown9310(1)
        blockstun(24)
        AirPushbackX(30000)
        AirPushbackY(-30000)
        GroundedHitstunAnimation(1)
        JumpCancel_(0)
        HitOverhead(0)
    sprite('Action_152_00', 3)	# 1-3	 **attackbox here**
    clearUponHandler(2)
    sprite('Action_152_00', 3)	# 4-6	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(12000)
    physicsYImpulse(18000)
    setGravity(1200)
    Unknown23087(45000)
    sprite('Action_152_01', 6)	# 7-12	 **attackbox here**
    sprite('Action_152_02', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(29000)
    Unknown1028(1250)
    physicsYImpulse(-20000)
    setGravity(1000)
    SFX_3('SE038')
    SFX_4('uhi106_0')
    sprite('Action_152_03', 3)	# 15-17	 **attackbox here**
    sendToLabelUpon(2, 1)
    sprite('Action_152_04', 3)	# 18-20	 **attackbox here**
    label(0)
    sprite('Action_152_03', 3)	# 21-23	 **attackbox here**
    sprite('Action_152_04', 3)	# 24-26	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('Action_152_05', 6)	# 27-32
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    GFX_0('EffAtkAIR5C', 100)
    sprite('Action_152_06', 10)	# 33-42
    sprite('Action_152_07', 6)	# 43-48

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('Action_068_00', 4)	# 1-4
    sprite('Action_068_02', 3)	# 5-7
    Unknown1084(1)
    SLOT_12 = SLOT_19
    Unknown1019(4)
    physicsYImpulse(23000)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    setGravity(1800)
    Unknown23087(70000)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    sprite('Action_068_03', 3)	# 8-10
    tag_voice(1, 'uhi305_0', 'uhi110_1', '', '')
    sprite('Action_068_04', 3)	# 11-13
    sprite('Action_068_05', 3)	# 14-16
    sprite('Action_026_00', 2)	# 17-18	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_026_01', 2)	# 19-20	 **attackbox here**
    sprite('Action_026_02', 3)	# 21-23	 **attackbox here**
    sprite('Action_026_03', 2)	# 24-25	 **attackbox here**
    sprite('Action_026_04', 3)	# 26-28	 **attackbox here**
    sprite('Action_026_07', 6)	# 29-34
    GFX_0('EffAtkAIR5A', 100)
    sprite('Action_026_08', 6)	# 35-40
    label(0)
    sprite('Action_026_09', 3)	# 41-43
    sprite('Action_026_10', 3)	# 44-46
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_152_05', 2)	# 47-48
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_152_05', 5)	# 49-53
    sprite('Action_152_06', 3)	# 54-56
    sprite('Action_152_07', 3)	# 57-59

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        loopRelated(17, 19)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        setGravity(3000)
        sendToLabelUpon(2, 1)
    sprite('Action_026_07', 6)	# 1-6
    GFX_0('EffAtkAIR5A', 100)
    sprite('Action_026_08', 6)	# 7-12
    label(0)
    sprite('Action_026_09', 3)	# 13-15
    sprite('Action_026_10', 3)	# 16-18
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_152_05', 2)	# 19-20
    Unknown8000(100, 1, 1)
    clearUponHandler(2)
    Unknown1084(1)
    sprite('Action_152_05', 5)	# 21-25
    sprite('Action_152_06', 3)	# 26-28
    sprite('Action_152_07', 3)	# 29-31
    label(2)
    sprite('Action_002_00', 2)	# 32-33
    loopRelated(17, 180)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(11)
    sprite('Action_002_01', 2)	# 34-35
    SFX_3('SE_Hari_Appear')
    sprite('Action_002_02', 3)	# 36-38	 **attackbox here**
    sprite('Action_002_03', 3)	# 39-41	 **attackbox here**
    sprite('Action_002_04', 3)	# 42-44	 **attackbox here**
    sprite('Action_002_05', 3)	# 45-47	 **attackbox here**
    sprite('Action_002_08', 3)	# 48-50
    GFX_0('EffAtkCrush1stMain', 100)
    tag_voice(0, 'uhi157_0', 'uhi157_1', '', '')
    sprite('Action_002_09', 2)	# 51-52
    sprite('Action_002_10', 2)	# 53-54
    sprite('Action_002_11', 2)	# 55-56
    sprite('Action_012_00', 5)	# 57-61	 **attackbox here**
    sprite('Action_012_01', 5)	# 62-66	 **attackbox here**
    Unknown18009(1)
    sprite('Action_012_02', 4)	# 67-70	 **attackbox here**
    sprite('Action_012_03', 2)	# 71-72	 **attackbox here**
    sprite('Action_012_04', 5)	# 73-77	 **attackbox here**
    sprite('Action_012_05', 5)	# 78-82	 **attackbox here**
    sprite('Action_013_00', 4)	# 83-86	 **attackbox here**
    label(10)
    sprite('Action_013_01', 4)	# 87-90	 **attackbox here**
    sprite('Action_013_02', 4)	# 91-94	 **attackbox here**
    sprite('Action_013_03', 4)	# 95-98	 **attackbox here**
    sprite('Action_013_04', 4)	# 99-102	 **attackbox here**
    sprite('Action_013_05', 4)	# 103-106	 **attackbox here**
    sprite('Action_013_06', 4)	# 107-110	 **attackbox here**
    sprite('Action_013_07', 4)	# 111-114	 **attackbox here**
    sprite('Action_013_08', 4)	# 115-118	 **attackbox here**
    sprite('Action_013_09', 4)	# 119-122	 **attackbox here**
    sprite('Action_013_10', 4)	# 123-126	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 127-127

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_012_00', 2)	# 1-2	 **attackbox here**
    Unknown18009(1)
    sprite('Action_012_01', 2)	# 3-4	 **attackbox here**
    Unknown23029(11, 26, 1)
    sprite('Action_150_00', 2)	# 5-6	 **attackbox here**
    sprite('Action_150_01', 2)	# 7-8	 **attackbox here**
    sprite('Action_150_02', 3)	# 9-11	 **attackbox here**
    sprite('Action_150_03', 3)	# 12-14	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_150_04', 2)	# 15-16	 **attackbox here**
    sprite('Action_150_05', 6)	# 17-22	 **attackbox here**
    sprite('Action_150_06', 6)	# 23-28	 **attackbox here**
    GFX_0('EffAtkCrush2ndMain', 100)
    sprite('Action_150_07', 6)	# 29-34	 **attackbox here**
    sprite('Action_150_08', 5)	# 35-39	 **attackbox here**
    label(10)
    sprite('Action_013_01', 4)	# 40-43	 **attackbox here**
    sprite('Action_013_02', 4)	# 44-47	 **attackbox here**
    sprite('Action_013_03', 4)	# 48-51	 **attackbox here**
    sprite('Action_013_04', 4)	# 52-55	 **attackbox here**
    sprite('Action_013_05', 4)	# 56-59	 **attackbox here**
    sprite('Action_013_06', 4)	# 60-63	 **attackbox here**
    sprite('Action_013_07', 4)	# 64-67	 **attackbox here**
    sprite('Action_013_08', 4)	# 68-71	 **attackbox here**
    sprite('Action_013_09', 4)	# 72-75	 **attackbox here**
    sprite('Action_013_10', 4)	# 76-79	 **attackbox here**
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 80-80

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
    sprite('Action_422_00', 1)	# 1-1	 **attackbox here**
    Unknown18009(1)
    sprite('Action_422_01', 2)	# 2-3	 **attackbox here**
    sprite('Action_422_02', 8)	# 4-11	 **attackbox here**
    sprite('Action_422_02', 4)	# 12-15	 **attackbox here**
    GFX_0('EffCrushFinish', 100)
    sprite('Action_422_02', 4)	# 16-19	 **attackbox here**
    tag_voice(0, 'uhi158_0', 'uhi158_1', '', '')
    sprite('Action_422_02ex01', 3)	# 20-22	 **attackbox here**
    sprite('Action_422_03', 4)	# 23-26	 **attackbox here**
    sprite('Action_422_04', 3)	# 27-29	 **attackbox here**
    sprite('Action_422_05', 3)	# 30-32	 **attackbox here**
    sprite('Action_424_00', 4)	# 33-36	 **attackbox here**
    sprite('Action_424_01', 5)	# 37-41	 **attackbox here**
    sprite('Action_424_02', 12)	# 42-53	 **attackbox here**
    sprite('Action_424_03', 4)	# 54-57	 **attackbox here**
    sprite('Action_424_04', 3)	# 58-60	 **attackbox here**

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_013_01', 1)	# 1-1	 **attackbox here**
    Unknown18009(1)
    label(0)
    sprite('Action_013_01', 4)	# 2-5	 **attackbox here**
    sprite('Action_013_02', 4)	# 6-9	 **attackbox here**
    sprite('Action_013_03', 4)	# 10-13	 **attackbox here**
    sprite('Action_013_04', 4)	# 14-17	 **attackbox here**
    sprite('Action_013_05', 4)	# 18-21	 **attackbox here**
    sprite('Action_013_06', 4)	# 22-25	 **attackbox here**
    sprite('Action_013_07', 4)	# 26-29	 **attackbox here**
    sprite('Action_013_08', 4)	# 30-33	 **attackbox here**
    sprite('Action_013_09', 4)	# 34-37	 **attackbox here**
    sprite('Action_013_10', 4)	# 38-41	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_422_00', 1)	# 42-42	 **attackbox here**
    sprite('Action_422_01', 2)	# 43-44	 **attackbox here**
    sprite('Action_422_02', 8)	# 45-52	 **attackbox here**
    sprite('Action_422_02', 4)	# 53-56	 **attackbox here**
    GFX_0('EffCrushFinish', 100)
    sprite('Action_422_02', 4)	# 57-60	 **attackbox here**
    tag_voice(0, 'uhi158_0', 'uhi158_1', '', '')
    sprite('Action_422_02ex01', 3)	# 61-63	 **attackbox here**
    sprite('Action_422_03', 4)	# 64-67	 **attackbox here**
    sprite('Action_422_04', 3)	# 68-70	 **attackbox here**
    sprite('Action_422_05', 3)	# 71-73	 **attackbox here**
    sprite('Action_424_00', 4)	# 74-77	 **attackbox here**
    sprite('Action_424_01', 5)	# 78-82	 **attackbox here**
    sprite('Action_424_02', 12)	# 83-94	 **attackbox here**
    sprite('Action_424_03', 4)	# 95-98	 **attackbox here**
    sprite('Action_424_04', 3)	# 99-101	 **attackbox here**

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('null', 1)	# 1-1
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-450000)
    teleportRelativeY(1000)
    Unknown3001(0)
    Unknown3004(19)
    GFX_0('EffWarpIn', 100)
    physicsXImpulse(1000)
    physicsYImpulse(1000)
    setGravity(100)
    sprite('Action_160_06', 4)	# 2-5
    sprite('Action_160_07', 4)	# 6-9
    sprite('Action_160_08', 4)	# 10-13
    sprite('Action_160_09', 4)	# 14-17
    sprite('Action_160_10', 3)	# 18-20
    sprite('Action_160_11', 3)	# 21-23
    Unknown1084(1)
    teleportRelativeY(0)
    sprite('Action_012_00', 3)	# 24-26	 **attackbox here**
    Unknown18009(1)
    sprite('Action_012_01', 3)	# 27-29	 **attackbox here**
    sprite('Action_005_00', 2)	# 30-31	 **attackbox here**
    sprite('Action_005_01', 2)	# 32-33	 **attackbox here**
    sprite('Action_005_02', 2)	# 34-35	 **attackbox here**
    sprite('Action_005_03', 3)	# 36-38	 **attackbox here**
    sprite('Action_005_04', 3)	# 39-41	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_005_05', 4)	# 42-45	 **attackbox here**
    sprite('Action_005_06', 4)	# 46-49	 **attackbox here**
    sprite('Action_005_07', 4)	# 50-53	 **attackbox here**
    sprite('Action_005_08', 5)	# 54-58	 **attackbox here**
    GFX_0('EffAtkCrush1stSub', 100)
    sprite('Action_005_09', 5)	# 59-63	 **attackbox here**
    sprite('Action_005_10', 4)	# 64-67	 **attackbox here**
    sprite('Action_013_01', 4)	# 68-71	 **attackbox here**
    sprite('Action_013_02', 4)	# 72-75	 **attackbox here**
    sprite('Action_013_03', 4)	# 76-79	 **attackbox here**
    sprite('Action_013_04', 4)	# 80-83	 **attackbox here**
    sprite('Action_013_05', 4)	# 84-87	 **attackbox here**
    sprite('Action_013_06', 4)	# 88-91	 **attackbox here**
    sprite('Action_013_07', 4)	# 92-95	 **attackbox here**
    sprite('Action_013_08', 4)	# 96-99	 **attackbox here**
    sprite('Action_013_09', 4)	# 100-103	 **attackbox here**
    sprite('Action_013_10', 4)	# 104-107	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('Action_006_00', 2)	# 1-2	 **attackbox here**
    Unknown18009(1)
    sprite('Action_006_01', 2)	# 3-4	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    sprite('Action_006_02', 3)	# 5-7	 **attackbox here**
    sprite('Action_006_03', 2)	# 8-9	 **attackbox here**
    sprite('Action_006_04', 2)	# 10-11	 **attackbox here**
    sprite('Action_006_05', 3)	# 12-14	 **attackbox here**
    sprite('Action_006_06', 7)	# 15-21	 **attackbox here**
    sprite('Action_006_07', 5)	# 22-26	 **attackbox here**
    GFX_0('EffAtk2C', 100)
    sprite('Action_006_08', 5)	# 27-31	 **attackbox here**
    sprite('Action_006_09', 5)	# 32-36	 **attackbox here**
    sprite('Action_006_10', 7)	# 37-43	 **attackbox here**
    sprite('Action_013_01', 4)	# 44-47	 **attackbox here**
    sprite('Action_013_02', 4)	# 48-51	 **attackbox here**
    sprite('Action_013_03', 4)	# 52-55	 **attackbox here**
    sprite('Action_013_04', 4)	# 56-59	 **attackbox here**
    sprite('Action_013_05', 4)	# 60-63	 **attackbox here**
    sprite('Action_013_06', 4)	# 64-67	 **attackbox here**
    sprite('Action_013_07', 4)	# 68-71	 **attackbox here**
    sprite('Action_013_08', 4)	# 72-75	 **attackbox here**
    sprite('Action_013_09', 4)	# 76-79	 **attackbox here**
    sprite('Action_013_10', 4)	# 80-83	 **attackbox here**
    loopRest()

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('Action_422_00', 1)	# 1-1	 **attackbox here**
    Unknown18009(1)
    sprite('Action_422_01', 2)	# 2-3	 **attackbox here**
    sprite('Action_422_02', 8)	# 4-11	 **attackbox here**
    sprite('Action_422_02', 8)	# 12-19	 **attackbox here**
    GFX_0('EffCrushFinish', 100)
    sprite('Action_422_02ex01', 3)	# 20-22	 **attackbox here**
    sprite('Action_422_03', 4)	# 23-26	 **attackbox here**
    sprite('Action_422_04', 3)	# 27-29	 **attackbox here**
    sprite('Action_422_05', 3)	# 30-32	 **attackbox here**
    sprite('Action_424_00', 4)	# 33-36	 **attackbox here**
    sprite('Action_424_01', 5)	# 37-41	 **attackbox here**
    sprite('Action_424_02', 12)	# 42-53	 **attackbox here**
    sprite('Action_424_03', 4)	# 54-57	 **attackbox here**
    sprite('Action_424_04', 3)	# 58-60	 **attackbox here**

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('Action_013_01', 1)	# 1-1	 **attackbox here**
    Unknown18009(1)
    label(0)
    sprite('Action_013_01', 4)	# 2-5	 **attackbox here**
    sprite('Action_013_02', 4)	# 6-9	 **attackbox here**
    sprite('Action_013_03', 4)	# 10-13	 **attackbox here**
    sprite('Action_013_04', 4)	# 14-17	 **attackbox here**
    sprite('Action_013_05', 4)	# 18-21	 **attackbox here**
    sprite('Action_013_06', 4)	# 22-25	 **attackbox here**
    sprite('Action_013_07', 4)	# 26-29	 **attackbox here**
    sprite('Action_013_08', 4)	# 30-33	 **attackbox here**
    sprite('Action_013_09', 4)	# 34-37	 **attackbox here**
    sprite('Action_013_10', 4)	# 38-41	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_422_00', 1)	# 42-42	 **attackbox here**
    sprite('Action_422_01', 2)	# 43-44	 **attackbox here**
    sprite('Action_422_02', 8)	# 45-52	 **attackbox here**
    sprite('Action_422_02', 8)	# 53-60	 **attackbox here**
    GFX_0('EffCrushFinish', 100)
    sprite('Action_422_02ex01', 3)	# 61-63	 **attackbox here**
    sprite('Action_422_03', 4)	# 64-67	 **attackbox here**
    sprite('Action_422_04', 3)	# 68-70	 **attackbox here**
    sprite('Action_422_05', 3)	# 71-73	 **attackbox here**
    sprite('Action_424_00', 4)	# 74-77	 **attackbox here**
    sprite('Action_424_01', 5)	# 78-82	 **attackbox here**
    sprite('Action_424_02', 12)	# 83-94	 **attackbox here**
    sprite('Action_424_03', 4)	# 95-98	 **attackbox here**
    sprite('Action_424_04', 3)	# 99-101	 **attackbox here**

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(3000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(16000)
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
    sprite('Action_045_00', 4)	# 3-6
    sprite('Action_045_01', 3)	# 7-9
    label(0)
    sprite('Action_045_02', 3)	# 10-12
    sprite('Action_045_03', 4)	# 13-16
    sprite('Action_045_04', 4)	# 17-20
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 21-23
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 24-26	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_01', 2)	# 27-28	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('Action_055_03', 6)	# 29-34
    SFX_3('SE042')
    GFX_0('EffAtkThrowMiss', 100)
    sprite('Action_055_04', 7)	# 35-41
    SFX_4('uhi154')
    sprite('Action_055_05', 5)	# 42-46
    sprite('Action_055_06', 3)	# 47-49

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        AttackP2(50)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(55000)
        AirPushbackY(10)
        YImpluseBeforeWallbounce(5)
        Hitstop(10)
        AirUntechableTime(60)
        Unknown9178(1)
        WallbounceReboundTime(35)
        AirHitstunAfterWallbounce(60)
        Unknown9362(1)
        Unknown9364(35)
        Unknown9016(1)
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            GFX_0('ThrowHitmarkMatome', 100)

        def upon_STATE_END():
            Unknown23029(6, 102, 0)
    sprite('Action_056_00', 3)	# 1-3
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    GFX_0('EffAtkThrowCatch', 100)
    SFX_4('uhi153')
    sprite('Action_056_01', 3)	# 4-6
    sprite('Action_056_02', 4)	# 7-10
    Unknown5003(1)
    sprite('Action_056_02', 1)	# 11-11
    Unknown5000(10, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    GFX_0('EffAtkThrowExe', 100)
    Unknown38(6, 1)
    sprite('Action_057_00', 6)	# 12-17
    sprite('Action_057_01', 6)	# 18-23
    sprite('Action_057_02', 4)	# 24-27
    sprite('Action_057_03', 4)	# 28-31
    sprite('Action_057_04', 6)	# 32-37	 **attackbox here**
    RefreshMultihit()
    sprite('Action_057_05', 8)	# 38-45
    Unknown23029(6, 102, 0)
    clearUponHandler(1)
    sprite('Action_057_06', 4)	# 46-49
    sprite('Action_057_07', 4)	# 50-53
    sprite('Action_057_08', 3)	# 54-56

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(3000)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(16000)
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
    sprite('Action_045_00', 4)	# 3-6
    sprite('Action_045_01', 3)	# 7-9
    sprite('Action_045_02', 3)	# 10-12
    label(0)
    sprite('Action_045_03', 4)	# 13-16
    sprite('Action_045_04', 4)	# 17-20
    gotoLabel(0)
    label(1)
    sprite('Action_055_00', 3)	# 21-23
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('Action_055_01', 3)	# 24-26	 **attackbox here**
    SFX_0('010_swing_sword_0')
    Unknown1084(1)
    sprite('Action_055_01', 2)	# 27-28	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('Action_055_03', 6)	# 29-34
    SFX_3('SE042')
    sprite('Action_055_04', 7)	# 35-41
    SFX_4('uhi154')
    GFX_0('EffAtkThrowMiss', 100)
    sprite('Action_055_05', 5)	# 42-46
    sprite('Action_055_06', 3)	# 47-49

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(5)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AttackP2(50)
        AirPushbackX(55000)
        AirPushbackY(10)
        YImpluseBeforeWallbounce(5)
        Hitstop(10)
        AirUntechableTime(60)
        Unknown9178(1)
        WallbounceReboundTime(35)
        AirHitstunAfterWallbounce(60)
        Unknown9362(1)
        Unknown9364(35)
        Unknown9016(1)
        Unknown30048(1)

        def upon_78():
            clearUponHandler(78)
            GFX_0('ThrowHitmarkMatome', 100)

        def upon_STATE_END():
            Unknown23029(6, 102, 0)
    sprite('Action_056_00', 3)	# 1-3
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    GFX_0('EffAtkThrowCatch', 100)
    SFX_4('uhi153')
    sprite('Action_056_01', 3)	# 4-6
    sprite('Action_056_02', 4)	# 7-10
    Unknown5003(1)
    sprite('Action_056_02', 1)	# 11-11
    Unknown2005()
    Unknown5000(10, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    GFX_0('EffAtkThrowExe', 100)
    Unknown38(6, 1)
    sprite('Action_057_00', 6)	# 12-17
    sprite('Action_057_01', 6)	# 18-23
    sprite('Action_057_02', 4)	# 24-27
    sprite('Action_057_03', 4)	# 28-31
    sprite('Action_057_04', 6)	# 32-37	 **attackbox here**
    RefreshMultihit()
    sprite('Action_057_05', 8)	# 38-45
    clearUponHandler(1)
    Unknown23029(6, 102, 0)
    sprite('Action_057_06', 4)	# 46-49
    sprite('Action_057_07', 4)	# 50-53
    sprite('Action_057_08', 3)	# 54-56

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        Hitstop(2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackX(2000)
        AirPushbackY(40000)
        PushbackX(5000)
        Unknown9016(1)
    sprite('Action_278_00', 2)	# 1-2
    Unknown1084(1)
    physicsYImpulse(2000)
    physicsXImpulse(2500)
    sprite('Action_278_01', 2)	# 3-4
    sprite('Action_278_02', 2)	# 5-6
    sprite('Action_278_03', 2)	# 7-8
    physicsXImpulse(5000)
    sprite('Action_278_04', 2)	# 9-10
    sprite('Action_278_05', 2)	# 11-12
    physicsXImpulse(7000)
    Unknown1028(-400)
    physicsYImpulse(5000)
    setGravity(400)
    Unknown7006('uhi216_0', 0, 845768821, 828323377, 0, 0, 100, 845768821, 845100593, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_278_06', 5)	# 13-17
    sprite('Action_278_07', 5)	# 18-22	 **attackbox here**
    Unknown1084(1)
    setGravity(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_278_08', 4)	# 23-26	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_Hari_Appear')
    sprite('Action_278_09', 4)	# 27-30	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_Hari_Appear')
    setInvincible(0)
    sprite('Action_278_10', 4)	# 31-34	 **attackbox here**
    RefreshMultihit()
    sprite('Action_278_11', 6)	# 35-40	 **attackbox here**
    sprite('Action_278_12', 6)	# 41-46
    GFX_0('EffReversal', 100)
    sprite('Action_278_13', 6)	# 47-52
    sprite('Action_278_14', 3)	# 53-55
    sprite('Action_278_15', 5)	# 56-60
    sprite('Action_278_16', 150)	# 61-210
    Unknown1043()
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_278_17', 6)	# 211-216
    clearUponHandler(3)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_278_18', 6)	# 217-222

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(1200)
        Unknown11092(1)
        Hitstop(2)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackX(2000)
        AirPushbackY(40000)
        PushbackX(5000)
        Unknown9016(1)
    sprite('Action_278_00', 2)	# 1-2
    clearUponHandler(2)
    Unknown1084(1)
    physicsYImpulse(2000)
    physicsXImpulse(2500)
    sprite('Action_278_01', 2)	# 3-4
    sprite('Action_278_02', 2)	# 5-6
    sprite('Action_278_03', 2)	# 7-8
    physicsXImpulse(5000)
    sprite('Action_278_04', 2)	# 9-10
    sprite('Action_278_05', 2)	# 11-12
    physicsXImpulse(7000)
    Unknown1028(-400)
    physicsYImpulse(5000)
    setGravity(400)
    Unknown7006('uhi216_0', 0, 845768821, 828323377, 0, 0, 100, 845768821, 845100593, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_278_06', 5)	# 13-17
    sprite('Action_278_07', 5)	# 18-22	 **attackbox here**
    Unknown1084(1)
    setGravity(0)
    SFX_3('SE_Hari_Appear')
    sprite('Action_278_08', 4)	# 23-26	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_Hari_Appear')
    sprite('Action_278_09', 4)	# 27-30	 **attackbox here**
    RefreshMultihit()
    SFX_3('SE_Hari_Appear')
    setInvincible(0)
    sprite('Action_278_10', 4)	# 31-34	 **attackbox here**
    RefreshMultihit()
    sprite('Action_278_11', 6)	# 35-40	 **attackbox here**
    sprite('Action_278_12', 6)	# 41-46
    GFX_0('EffReversal', 100)
    sprite('Action_278_13', 6)	# 47-52
    sprite('Action_278_14', 3)	# 53-55
    sprite('Action_278_15', 5)	# 56-60
    sprite('Action_278_16', 150)	# 61-210
    Unknown1043()
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_278_17', 6)	# 211-216
    clearUponHandler(3)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_278_18', 6)	# 217-222

@State
def MidShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 531):
                Recovery()
    sprite('Action_212_00', 2)	# 1-2
    sprite('Action_212_01', 2)	# 3-4
    sprite('Action_212_02', 3)	# 5-7
    SFX_1('uhi203_1')
    sprite('Action_212_03', 6)	# 8-13
    GFX_0('EffMidShot', 0)
    sprite('Action_212_04', 9)	# 14-22
    sprite('Action_212_05', 11)	# 23-33
    sprite('Action_212_06', 8)	# 34-41
    sprite('Action_212_07', 7)	# 42-48
    sprite('Action_212_08', 7)	# 49-55

@State
def BackAttackShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 531):
                Recovery()
    sprite('Action_213_00', 5)	# 1-5
    sprite('Action_213_01', 5)	# 6-10
    sprite('Action_213_02', 6)	# 11-16
    SFX_1('uhi203_2')
    sprite('Action_213_03', 6)	# 17-22
    sprite('Action_213_04', 4)	# 23-26
    GFX_0('EffBackAttackShot', 0)
    sprite('Action_213_05', 9)	# 27-35
    sprite('Action_213_06', 8)	# 36-43
    sprite('Action_213_07', 6)	# 44-49
    sprite('Action_213_08', 6)	# 50-55

@State
def LowShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_43():
            if (SLOT_48 == 511):
                setInvincible(1)
                Unknown14083(0)
                SLOT_51 = 1
            if (SLOT_48 == 512):
                SLOT_52 = 1
                Unknown14083(1)
            if (SLOT_48 == 513):
                Recovery()
    sprite('Action_422_00', 1)	# 1-1	 **attackbox here**
    Unknown18009(1)
    sprite('Action_422_00', 2)	# 2-3	 **attackbox here**
    Unknown23029(11, 26, 1)
    sprite('Action_422_00', 3)	# 4-6	 **attackbox here**
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    GFX_0('LowShotAtk', 100)
    SFX_1('uhi214_2')
    sprite('Action_422_01', 7)	# 7-13	 **attackbox here**
    sprite('Action_422_02', 20)	# 14-33	 **attackbox here**
    sprite('Action_422_03', 11)	# 34-44	 **attackbox here**
    sprite('Action_422_04', 7)	# 45-51	 **attackbox here**
    if SLOT_51:
        _gotolabel(10)
    sprite('Action_422_05', 7)	# 52-58	 **attackbox here**
    loopRest()
    ExitState()
    label(10)
    sprite('Action_431_00', 4)	# 59-62	 **attackbox here**
    setInvincible(1)
    GFX_0('LowShotAtkExe', 100)
    sprite('Action_431_01', 5)	# 63-67	 **attackbox here**
    sprite('Action_431_02', 8)	# 68-75	 **attackbox here**
    sprite('Action_431_03', 4)	# 76-79	 **attackbox here**
    sprite('Action_431_04', 8)	# 80-87	 **attackbox here**
    sprite('Action_431_05', 4)	# 88-91	 **attackbox here**
    if SLOT_51:
        _gotolabel(20)
    sprite('Action_431_06', 3)	# 92-94	 **attackbox here**
    sprite('Action_431_07', 3)	# 95-97	 **attackbox here**
    loopRest()
    ExitState()
    label(20)
    sprite('Action_013_15', 5)	# 98-102	 **attackbox here**
    sprite('Action_013_16', 5)	# 103-107	 **attackbox here**
    sprite('Action_013_17', 8)	# 108-115	 **attackbox here**
    sprite('Action_013_15', 4)	# 116-119	 **attackbox here**
    sprite('Action_013_16', 5)	# 120-124	 **attackbox here**
    sprite('Action_013_17', 8)	# 125-132	 **attackbox here**
    sprite('Action_013_16', 5)	# 133-137	 **attackbox here**
    sprite('Action_013_00', 3)	# 138-140	 **attackbox here**

@State
def DelayShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('Action_199_00', 2)	# 1-2
    sprite('Action_199_01', 1)	# 3-3
    sprite('Action_199_01', 2)	# 4-5
    GFX_0('EffDelayShotStart', 100)
    GFX_0('EffDelayShotCharge', 0)
    Unknown38(4, 1)
    Unknown1084(1)
    physicsXImpulse(-9000)
    Unknown1028(220)
    physicsYImpulse(10000)
    setGravity(220)
    if random_(2, 0, 50):
        Unknown7006('uhi206_0', 100, 845768821, 828323376, 0, 0, 100, 845768821, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('uhi207_0', 100, 845768821, 828323632, 0, 0, 100, 845768821, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_199_02', 3)	# 6-8
    sprite('Action_199_03', 3)	# 9-11
    sprite('Action_199_04', 4)	# 12-15
    sprite('Action_199_05', 4)	# 16-19
    sprite('Action_199_06', 3)	# 20-22
    Unknown23029(4, 521, 0)
    Unknown23029(4, 522, 0)
    physicsXImpulse(-12000)
    Unknown1028(0)
    physicsYImpulse(12000)
    setGravity(1700)
    sendToLabelUpon(2, 1)
    sprite('Action_199_07', 8)	# 23-30
    sprite('Action_199_08', 5)	# 31-35
    sprite('Action_199_09', 4)	# 36-39
    sprite('Action_199_10', 4)	# 40-43
    sprite('Action_199_11', 50)	# 44-93
    label(1)
    sprite('Action_199_12', 6)	# 94-99
    Unknown1084(1)
    sprite('Action_199_13', 6)	# 100-105

@State
def WarpOutShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_125_00', 6)	# 1-6
    sprite('Action_125_01', 6)	# 7-12
    sprite('Action_125_02', 6)	# 13-18
    sprite('Action_125_03', 7)	# 19-25
    sprite('Action_125_04', 7)	# 26-32
    GFX_0('EffWarpOut', 100)
    sprite('Action_125_05', 7)	# 33-39
    setInvincible(1)
    sprite('Action_125_06', 15)	# 40-54
    Unknown3004(-17)
    sprite('null', 2)	# 55-56
    Unknown3001(0)
    sprite('null', 1)	# 57-57
    Unknown1086(22)
    teleportRelativeX(350000)
    teleportRelativeY(150000)
    sprite('Action_145_00', 7)	# 58-64
    Unknown2006()
    GFX_0('EffWarpIn', 100)
    Unknown3004(36)
    Unknown1045(-35000)
    sendToLabelUpon(2, 1)
    sprite('Action_145_01', 7)	# 65-71
    GFX_0('WarpShotAtkMatome', 0)
    Unknown3001(255)
    Unknown1043()
    sprite('Action_145_02', 6)	# 72-77
    sprite('Action_145_03', 5)	# 78-82
    sprite('Action_145_04', 7)	# 83-89
    sprite('Action_145_05', 6)	# 90-95
    label(0)
    sprite('Action_145_06', 5)	# 96-100
    sprite('Action_145_07', 5)	# 101-105
    sprite('Action_145_08', 5)	# 106-110
    gotoLabel(0)
    label(1)
    sprite('Action_145_09', 5)	# 111-115
    Unknown1084(1)
    sprite('Action_145_10', 5)	# 116-120
    sprite('Action_145_11', 5)	# 121-125
    sprite('Action_145_12', 5)	# 126-130

@State
def SpreadShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('Action_250_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_250_01', 2)	# 4-5	 **attackbox here**
    sprite('Action_250_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_250_03', 3)	# 8-10	 **attackbox here**
    teleportRelativeX(10000)
    Unknown7006('uhi217_0', 100, 845768821, 828323633, 0, 0, 100, 845768821, 845100849, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_250_04', 3)	# 11-13	 **attackbox here**
    sprite('Action_250_05', 3)	# 14-16	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_250_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_250_07', 3)	# 20-22	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_250_08', 5)	# 23-27	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_250_09', 8)	# 28-35	 **attackbox here**
    teleportRelativeX(14000)
    sprite('Action_250_10', 5)	# 36-40	 **attackbox here**
    sprite('Action_250_11', 5)	# 41-45	 **attackbox here**
    SFX_3('SE_BallExplosion')
    GFX_0('EffSpreadShotDel', 100)
    GFX_0('SpreadShotMatome', 0)
    sprite('Action_250_12', 10)	# 46-55	 **attackbox here**
    sprite('Action_250_13', 5)	# 56-60
    sprite('Action_250_14', 4)	# 61-64
    sprite('Action_250_15', 3)	# 65-67

@State
def AirSpreadShot():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)

        def upon_STATE_END():
            Unknown23029(7, 51, 0)
            Unknown23029(8, 52, 0)
    sprite('Action_250_00', 3)	# 1-3	 **attackbox here**
    sprite('Action_250_01', 2)	# 4-5	 **attackbox here**
    Unknown1084(1)
    setGravity(0)
    GFX_0('AirStandFront', 100)
    Unknown38(7, 1)
    GFX_0('AirStandBack', 100)
    Unknown38(8, 1)
    sprite('Action_250_02', 2)	# 6-7	 **attackbox here**
    sprite('Action_250_03', 3)	# 8-10	 **attackbox here**
    teleportRelativeX(10000)
    Unknown7006('uhi217_0', 100, 845768821, 828323633, 0, 0, 100, 845768821, 845100849, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_250_04', 3)	# 11-13	 **attackbox here**
    sprite('Action_250_05', 3)	# 14-16	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_250_06', 3)	# 17-19	 **attackbox here**
    sprite('Action_250_07', 3)	# 20-22	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_250_08', 5)	# 23-27	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_250_09', 8)	# 28-35	 **attackbox here**
    teleportRelativeX(14000)
    sprite('Action_250_10', 5)	# 36-40	 **attackbox here**
    sprite('Action_250_11', 5)	# 41-45	 **attackbox here**
    SFX_3('SE_BallExplosion')
    GFX_0('EffSpreadShotDel', 100)
    GFX_0('SpreadShotMatome', 0)
    sprite('Action_250_12', 10)	# 46-55	 **attackbox here**
    sprite('Action_250_13', 5)	# 56-60
    sprite('Action_250_14', 4)	# 61-64
    sprite('Action_250_15', 3)	# 65-67
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23029(7, 51, 0)
    Unknown23029(8, 52, 0)
    label(0)
    sprite('Action_020_00', 3)	# 68-70
    sprite('Action_020_01', 3)	# 71-73
    sprite('Action_020_02', 3)	# 74-76
    gotoLabel(0)
    label(1)
    sprite('Action_021_00', 3)	# 77-79
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    clearUponHandler(1)
    sprite('Action_021_01', 3)	# 80-82

@State
def StormShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('Action_449_02', 4)	# 1-4
    sprite('Action_449_02', 4)	# 5-8
    Unknown1084(1)
    physicsXImpulse(-5500)
    Unknown1028(64)
    physicsYImpulse(6500)
    setGravity(128)
    sprite('Action_449_03', 4)	# 9-12
    sprite('Action_449_04', 4)	# 13-16
    sprite('Action_449_02', 4)	# 17-20
    sprite('Action_449_03', 4)	# 21-24
    sprite('Action_449_05', 4)	# 25-28
    GFX_0('StormShotCharge', 100)
    Unknown1039(50)
    sprite('Action_449_06', 4)	# 29-32
    sprite('Action_449_07', 4)	# 33-36
    sprite('Action_449_08', 3)	# 37-39
    sprite('Action_449_09', 4)	# 40-43
    sprite('Action_449_10', 4)	# 44-47
    sprite('Action_449_12', 6)	# 48-53
    sprite('Action_449_13', 6)	# 54-59
    sprite('Action_449_14', 7)	# 60-66
    sprite('Action_449_15', 8)	# 67-74
    sprite('Action_449_16', 60)	# 75-134
    setGravity(1500)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_449_17', 4)	# 135-138

@State
def AirStormShot():

    def upon_IMMEDIATE():
        Unknown17003()
        Unknown2003(1)
    sprite('Action_449_02', 4)	# 1-4
    sprite('Action_449_02', 4)	# 5-8
    Unknown1084(1)
    physicsXImpulse(-5500)
    Unknown1028(64)
    physicsYImpulse(6500)
    setGravity(128)
    sprite('Action_449_03', 4)	# 9-12
    sprite('Action_449_04', 4)	# 13-16
    sprite('Action_449_02', 4)	# 17-20
    sprite('Action_449_03', 4)	# 21-24
    sprite('Action_449_05', 4)	# 25-28
    GFX_0('StormShotCharge', 100)
    Unknown1039(50)
    sprite('Action_449_06', 4)	# 29-32
    sprite('Action_449_07', 4)	# 33-36
    sprite('Action_449_08', 3)	# 37-39
    sprite('Action_449_09', 4)	# 40-43
    sprite('Action_449_10', 4)	# 44-47
    sprite('Action_449_12', 6)	# 48-53
    sprite('Action_449_13', 6)	# 54-59
    sprite('Action_449_14', 7)	# 60-66
    sprite('Action_449_15', 8)	# 67-74
    sprite('Action_449_16', 60)	# 75-134
    setGravity(1500)
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    label(1)
    sprite('Action_449_17', 4)	# 135-138

@State
def DropShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
    sprite('Action_431_00', 1)	# 1-1	 **attackbox here**
    Unknown18009(1)
    sprite('Action_431_00', 2)	# 2-3	 **attackbox here**
    Unknown23029(11, 26, 1)
    sprite('Action_431_00', 2)	# 4-5	 **attackbox here**
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown7006('uhi212_0', 100, 845768821, 828322353, 0, 0, 0, 845768821, 845099569, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_431_01', 7)	# 6-12	 **attackbox here**
    sprite('Action_431_02', 12)	# 13-24	 **attackbox here**
    GFX_0('EffDropShot_Pacchin', 0)
    GFX_0('EffDropShot_Atk', 0)
    sprite('Action_431_03', 3)	# 25-27	 **attackbox here**
    sprite('Action_431_04', 8)	# 28-35	 **attackbox here**
    sprite('Action_431_05', 8)	# 36-43	 **attackbox here**
    sprite('Action_431_06', 10)	# 44-53	 **attackbox here**
    sprite('Action_431_07', 7)	# 54-60	 **attackbox here**

@State
def AirDropShot():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)

        def upon_STATE_END():
            Unknown23029(7, 51, 0)
            Unknown23029(8, 52, 0)
    sprite('Action_053_00', 3)	# 1-3
    sprite('Action_053_01', 3)	# 4-6
    Unknown1084(1)
    setGravity(0)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    GFX_0('AirStandFront', 100)
    Unknown38(7, 1)
    GFX_0('AirStandBack', 100)
    Unknown38(8, 1)
    SLOT_9 = 1
    Unknown7006('uhi212_0', 100, 845768821, 828322353, 0, 0, 0, 845768821, 845099569, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_053_02', 4)	# 7-10
    sprite('Action_053_03', 1)	# 11-11	 **attackbox here**
    sprite('Action_053_03', 3)	# 12-14	 **attackbox here**
    GFX_0('EffDropShot_Atk', 0)
    sprite('Action_053_04', 3)	# 15-17
    sprite('Action_053_05', 5)	# 18-22	 **attackbox here**
    sprite('Action_053_06', 5)	# 23-27	 **attackbox here**
    sprite('Action_053_07', 5)	# 28-32	 **attackbox here**
    sprite('Action_053_08', 5)	# 33-37	 **attackbox here**
    sprite('Action_053_09', 17)	# 38-54	 **attackbox here**
    sprite('Action_053_01', 5)	# 55-59
    sprite('Action_053_00', 3)	# 60-62
    Unknown1043()
    clearUponHandler(2)
    sendToLabelUpon(2, 1)
    Unknown23029(7, 51, 0)
    Unknown23029(8, 52, 0)

@State
def AirWarpOutShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_125_00', 6)	# 1-6
    sprite('Action_125_01', 6)	# 7-12
    sprite('Action_125_02', 6)	# 13-18
    sprite('Action_125_03', 7)	# 19-25
    sprite('Action_125_04', 7)	# 26-32
    GFX_0('EffWarpOut', 100)
    sprite('Action_125_05', 7)	# 33-39
    setInvincible(1)
    sprite('Action_125_06', 15)	# 40-54
    Unknown3004(-17)
    sprite('null', 2)	# 55-56
    Unknown3001(0)
    sprite('null', 1)	# 57-57
    Unknown1086(22)
    teleportRelativeX(350000)
    teleportRelativeY(150000)
    sprite('Action_145_00', 7)	# 58-64
    Unknown2006()
    GFX_0('EffWarpIn', 100)
    Unknown3004(36)
    Unknown1045(-35000)
    sendToLabelUpon(2, 1)
    sprite('Action_145_01', 7)	# 65-71
    GFX_0('WarpShotAtkMatome', 0)
    Unknown3001(255)
    Unknown1043()
    sprite('Action_145_02', 6)	# 72-77
    sprite('Action_145_03', 5)	# 78-82
    sprite('Action_145_04', 7)	# 83-89
    sprite('Action_145_05', 6)	# 90-95
    label(0)
    sprite('Action_145_06', 5)	# 96-100
    sprite('Action_145_07', 5)	# 101-105
    sprite('Action_145_08', 5)	# 106-110
    gotoLabel(0)
    label(1)
    sprite('Action_145_09', 5)	# 111-115
    Unknown1084(1)
    sprite('Action_145_10', 5)	# 116-120
    sprite('Action_145_11', 5)	# 121-125
    sprite('Action_145_12', 5)	# 126-130

@State
def AirDelayShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('Action_199_00', 2)	# 1-2
    sprite('Action_199_01', 1)	# 3-3
    sprite('Action_199_01', 2)	# 4-5
    GFX_0('EffDelayShotCharge', 0)
    Unknown38(5, 1)
    Unknown1084(1)
    physicsXImpulse(-9000)
    Unknown1028(220)
    physicsYImpulse(10000)
    setGravity(220)
    if random_(2, 0, 50):
        Unknown7006('uhi206_0', 100, 845768821, 828323376, 0, 0, 100, 845768821, 845100592, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        Unknown7006('uhi207_0', 100, 845768821, 828323632, 0, 0, 100, 845768821, 845100848, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_199_02', 3)	# 6-8
    sprite('Action_199_03', 3)	# 9-11
    sprite('Action_199_04', 4)	# 12-15
    sprite('Action_199_05', 4)	# 16-19
    sprite('Action_199_06', 3)	# 20-22
    Unknown23029(5, 521, 0)
    Unknown23029(5, 523, 0)
    physicsXImpulse(-12000)
    Unknown1028(0)
    physicsYImpulse(12000)
    setGravity(1700)
    sendToLabelUpon(2, 1)
    sprite('Action_199_07', 8)	# 23-30
    sprite('Action_199_08', 5)	# 31-35
    sprite('Action_199_09', 4)	# 36-39
    sprite('Action_199_10', 4)	# 40-43
    sprite('Action_199_11', 50)	# 44-93
    label(1)
    sprite('Action_199_12', 6)	# 94-99
    Unknown1084(1)
    sprite('Action_199_13', 6)	# 100-105

@State
def UltimateAllRangeShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(450)
        Unknown11064(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(150)
        AirPushbackX(0)
        AirPushbackY(3000)
        YImpluseBeforeWallbounce(30)
        Unknown30048(1)
        Unknown11084(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11069('AllRangeShotAtk')
        Unknown11023(1)

        def upon_78():
            Unknown13024(0)
            Hitstop(0)
            sendToLabel(100)
    sprite('Action_052_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_052_01', 5)	# 6-10
    sprite('Action_052_02', 5)	# 11-15
    Unknown2036(63, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown7006('uhi250_0', 100, 845768821, 828321845, 0, 0, 0, 845768821, 845099061, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_052_03', 5)	# 16-20
    sprite('Action_052_04', 5)	# 21-25
    sprite('Action_233_00', 15)	# 26-40
    sprite('Action_233_01', 3)	# 41-43	 **attackbox here**
    sprite('Action_233_02', 3)	# 44-46	 **attackbox here**
    Unknown18009(1)
    sprite('Action_233_03', 3)	# 47-49	 **attackbox here**
    sprite('Action_233_04', 4)	# 50-53	 **attackbox here**
    sprite('Action_233_05', 3)	# 54-56	 **attackbox here**
    sprite('Action_233_06', 5)	# 57-61	 **attackbox here**
    sprite('Action_233_07', 5)	# 62-66	 **attackbox here**
    sprite('Action_233_08', 6)	# 67-72	 **attackbox here**
    sprite('Action_233_09', 10)	# 73-82	 **attackbox here**
    sprite('Action_233_10', 5)	# 83-87	 **attackbox here**
    sprite('Action_233_11', 18)	# 88-105	 **attackbox here**
    setInvincible(0)
    sprite('Action_233_12', 7)	# 106-112	 **attackbox here**
    sprite('Action_233_13', 10)	# 113-122	 **attackbox here**
    sprite('Action_233_14', 10)	# 123-132	 **attackbox here**
    sprite('Action_232_00', 8)	# 133-140	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_234_00', 5)	# 141-145	 **attackbox here**
    setInvincible(1)
    GFX_0('AllRangeShotAtk', 100)
    Unknown38(6, 1)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_158):
            Unknown23029(1, 1151, 0)
    sprite('Action_234_01', 8)	# 146-153	 **attackbox here**
    sprite('Action_234_02', 5)	# 154-158	 **attackbox here**
    sprite('Action_234_03', 7)	# 159-165	 **attackbox here**
    sprite('Action_234_04', 5)	# 166-170	 **attackbox here**
    sprite('Action_234_05', 20)	# 171-190	 **attackbox here**
    sprite('Action_234_06', 4)	# 191-194	 **attackbox here**
    sprite('Action_234_07', 7)	# 195-201	 **attackbox here**
    sprite('Action_234_08', 10)	# 202-211	 **attackbox here**
    sprite('Action_234_09', 4)	# 212-215	 **attackbox here**
    sprite('Action_234_10', 7)	# 216-222	 **attackbox here**
    sprite('Action_234_11', 7)	# 223-229	 **attackbox here**
    sprite('Action_234_12', 4)	# 230-233	 **attackbox here**
    sprite('Action_234_13', 7)	# 234-240	 **attackbox here**
    sprite('Action_234_14', 3)	# 241-243	 **attackbox here**
    sprite('Action_234_15', 8)	# 244-251	 **attackbox here**
    sprite('Action_234_16', 8)	# 252-259	 **attackbox here**
    SFX_1('uhi252')
    sprite('Action_234_17', 8)	# 260-267	 **attackbox here**
    sprite('Action_234_18', 8)	# 268-275	 **attackbox here**
    sprite('Action_234_19', 8)	# 276-283	 **attackbox here**
    sprite('Action_234_20', 7)	# 284-290	 **attackbox here**
    sprite('Action_234_21', 7)	# 291-297	 **attackbox here**
    sprite('Action_234_22', 7)	# 298-304	 **attackbox here**
    sprite('Action_234_23', 7)	# 305-311	 **attackbox here**
    sprite('Action_234_24', 7)	# 312-318	 **attackbox here**
    sprite('Action_234_25', 7)	# 319-325	 **attackbox here**
    sprite('Action_234_26', 7)	# 326-332	 **attackbox here**
    sprite('Action_234_27', 7)	# 333-339	 **attackbox here**
    sprite('Action_234_28', 4)	# 340-343	 **attackbox here**
    sprite('Action_234_29', 7)	# 344-350	 **attackbox here**
    sprite('Action_234_48', 7)	# 351-357	 **attackbox here**
    sprite('Action_234_49', 7)	# 358-364	 **attackbox here**
    sprite('Action_234_50', 6)	# 365-370	 **attackbox here**
    Unknown13024(1)
    sprite('Action_234_51', 8)	# 371-378	 **attackbox here**
    sprite('Action_234_52', 5)	# 379-383	 **attackbox here**
    sprite('Action_234_53', 5)	# 384-388	 **attackbox here**

@State
def UltimateAllRangeShotOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(450)
        Unknown11064(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        AirUntechableTime(150)
        AirPushbackX(0)
        AirPushbackY(3000)
        YImpluseBeforeWallbounce(30)
        Unknown30048(1)
        Unknown11084(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11069('AllRangeShotAtkOD')
        Unknown11023(1)

        def upon_78():
            Unknown13024(0)
            Hitstop(0)
            sendToLabel(100)
    sprite('Action_052_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_052_01', 5)	# 6-10
    sprite('Action_052_02', 5)	# 11-15
    Unknown2036(63, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown7006('uhi250_0', 100, 845768821, 828321845, 0, 0, 0, 845768821, 845099061, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_052_03', 5)	# 16-20
    sprite('Action_052_04', 5)	# 21-25
    sprite('Action_233_00', 15)	# 26-40
    sprite('Action_233_01', 3)	# 41-43	 **attackbox here**
    sprite('Action_233_02', 3)	# 44-46	 **attackbox here**
    Unknown18009(1)
    sprite('Action_233_03', 3)	# 47-49	 **attackbox here**
    sprite('Action_233_04', 4)	# 50-53	 **attackbox here**
    sprite('Action_233_05', 3)	# 54-56	 **attackbox here**
    sprite('Action_233_06', 5)	# 57-61	 **attackbox here**
    sprite('Action_233_07', 5)	# 62-66	 **attackbox here**
    sprite('Action_233_08', 6)	# 67-72	 **attackbox here**
    sprite('Action_233_09', 10)	# 73-82	 **attackbox here**
    sprite('Action_233_10', 5)	# 83-87	 **attackbox here**
    sprite('Action_233_11', 18)	# 88-105	 **attackbox here**
    setInvincible(0)
    sprite('Action_233_12', 7)	# 106-112	 **attackbox here**
    sprite('Action_233_13', 10)	# 113-122	 **attackbox here**
    sprite('Action_233_14', 10)	# 123-132	 **attackbox here**
    sprite('Action_232_00', 8)	# 133-140	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_234_00', 5)	# 141-145	 **attackbox here**
    setInvincible(1)
    GFX_0('AllRangeShotAtkOD', 100)
    Unknown38(6, 1)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_158):
            Unknown23029(1, 1151, 0)
    sprite('Action_234_01', 8)	# 146-153	 **attackbox here**
    sprite('Action_234_02', 5)	# 154-158	 **attackbox here**
    sprite('Action_234_03', 7)	# 159-165	 **attackbox here**
    sprite('Action_234_04', 5)	# 166-170	 **attackbox here**
    sprite('Action_234_05', 20)	# 171-190	 **attackbox here**
    SFX_1('uhi251')
    sprite('Action_234_06', 4)	# 191-194	 **attackbox here**
    sprite('Action_234_07', 7)	# 195-201	 **attackbox here**
    sprite('Action_234_08', 10)	# 202-211	 **attackbox here**
    sprite('Action_234_09', 4)	# 212-215	 **attackbox here**
    sprite('Action_234_10', 7)	# 216-222	 **attackbox here**
    sprite('Action_234_11', 7)	# 223-229	 **attackbox here**
    sprite('Action_234_12', 4)	# 230-233	 **attackbox here**
    sprite('Action_234_13', 7)	# 234-240	 **attackbox here**
    sprite('Action_234_14', 3)	# 241-243	 **attackbox here**
    sprite('Action_234_15', 8)	# 244-251	 **attackbox here**
    sprite('Action_234_16', 8)	# 252-259	 **attackbox here**
    sprite('Action_234_17', 8)	# 260-267	 **attackbox here**
    sprite('Action_234_18', 8)	# 268-275	 **attackbox here**
    sprite('Action_234_19', 8)	# 276-283	 **attackbox here**
    sprite('Action_234_20', 7)	# 284-290	 **attackbox here**
    sprite('Action_234_21', 7)	# 291-297	 **attackbox here**
    sprite('Action_234_22', 7)	# 298-304	 **attackbox here**
    sprite('Action_234_23', 7)	# 305-311	 **attackbox here**
    SFX_1('uhi252')
    sprite('Action_234_24', 7)	# 312-318	 **attackbox here**
    sprite('Action_234_25', 7)	# 319-325	 **attackbox here**
    sprite('Action_234_26', 7)	# 326-332	 **attackbox here**
    sprite('Action_234_27', 7)	# 333-339	 **attackbox here**
    sprite('Action_234_28', 4)	# 340-343	 **attackbox here**
    sprite('Action_234_29', 7)	# 344-350	 **attackbox here**
    sprite('Action_234_30', 7)	# 351-357	 **attackbox here**
    sprite('Action_234_31', 7)	# 358-364	 **attackbox here**
    sprite('Action_234_32', 7)	# 365-371	 **attackbox here**
    sprite('Action_234_33', 7)	# 372-378	 **attackbox here**
    sprite('Action_234_34', 7)	# 379-385	 **attackbox here**
    sprite('Action_234_35', 7)	# 386-392	 **attackbox here**
    sprite('Action_234_36', 7)	# 393-399	 **attackbox here**
    sprite('Action_234_37', 7)	# 400-406	 **attackbox here**
    sprite('Action_234_38', 7)	# 407-413	 **attackbox here**
    sprite('Action_234_39', 7)	# 414-420	 **attackbox here**
    sprite('Action_234_40', 8)	# 421-428	 **attackbox here**
    sprite('Action_234_45', 7)	# 429-435	 **attackbox here**
    sprite('Action_234_46', 7)	# 436-442	 **attackbox here**
    sprite('Action_234_47', 7)	# 443-449	 **attackbox here**
    sprite('Action_234_48', 8)	# 450-457	 **attackbox here**
    sprite('Action_234_49', 8)	# 458-465	 **attackbox here**
    sprite('Action_234_50', 6)	# 466-471	 **attackbox here**
    Unknown13024(1)
    sprite('Action_234_51', 8)	# 472-479	 **attackbox here**
    sprite('Action_234_52', 6)	# 480-485	 **attackbox here**
    sprite('Action_234_53', 6)	# 486-491	 **attackbox here**

@State
def UltimateStorm():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
    sprite('Action_449_02', 4)	# 1-4
    Unknown1084(1)
    physicsXImpulse(-10000)
    Unknown1028(640)
    physicsYImpulse(10000)
    setGravity(640)
    setInvincible(1)
    Unknown7006('uhi253_0', 100, 845768821, 828322613, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_449_03', 4)	# 5-8
    sprite('Action_449_04', 4)	# 9-12
    Unknown2036(28, -1, 0)
    Unknown1084(1)
    setGravity(0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsXImpulse(-1280)
    physicsYImpulse(1280)
    GFX_0('UltimateStormCharge', 100)
    SLOT_8 = 1
    sprite('Action_449_05', 3)	# 13-15
    sprite('Action_449_06', 3)	# 16-18
    sprite('Action_449_07', 3)	# 19-21
    sprite('Action_449_08', 3)	# 22-24
    sprite('Action_449_09', 4)	# 25-28
    sprite('Action_449_10', 4)	# 29-32
    sprite('Action_449_11', 4)	# 33-36
    sprite('Action_449_12', 6)	# 37-42
    setInvincible(0)
    sprite('Action_449_13', 6)	# 43-48
    sprite('Action_449_14', 7)	# 49-55
    sprite('Action_449_15', 8)	# 56-63
    sprite('Action_449_16', 5)	# 64-68
    physicsYImpulse(10500)
    setGravity(2000)
    sprite('Action_449_17', 5)	# 69-73

@State
def UltimateStormOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
    sprite('Action_449_02', 4)	# 1-4
    Unknown1084(1)
    physicsXImpulse(-10000)
    Unknown1028(640)
    physicsYImpulse(10000)
    setGravity(640)
    setInvincible(1)
    Unknown7006('uhi253_0', 100, 845768821, 828322613, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_449_03', 4)	# 5-8
    sprite('Action_449_04', 4)	# 9-12
    Unknown1084(1)
    setGravity(0)
    Unknown2036(28, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsXImpulse(-1280)
    physicsYImpulse(1280)
    GFX_0('UltimateStormChargeOD', 100)
    SLOT_8 = 1
    sprite('Action_449_05', 3)	# 13-15
    sprite('Action_449_06', 3)	# 16-18
    sprite('Action_449_07', 3)	# 19-21
    sprite('Action_449_08', 3)	# 22-24
    sprite('Action_449_09', 4)	# 25-28
    sprite('Action_449_10', 4)	# 29-32
    sprite('Action_449_11', 4)	# 33-36
    sprite('Action_449_12', 6)	# 37-42
    setInvincible(0)
    sprite('Action_449_13', 6)	# 43-48
    sprite('Action_449_14', 7)	# 49-55
    sprite('Action_449_15', 8)	# 56-63
    sprite('Action_449_16', 5)	# 64-68
    physicsYImpulse(10500)
    setGravity(2000)
    sprite('Action_449_17', 5)	# 69-73

@State
def AirUltimateStorm():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
    sprite('Action_449_02', 4)	# 1-4
    Unknown1084(1)
    physicsXImpulse(-10000)
    Unknown1028(640)
    physicsYImpulse(10000)
    setGravity(640)
    setInvincible(1)
    Unknown7006('uhi253_0', 100, 845768821, 828322613, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_449_03', 4)	# 5-8
    sprite('Action_449_04', 4)	# 9-12
    Unknown2036(28, -1, 0)
    Unknown1084(1)
    setGravity(0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsXImpulse(-1280)
    physicsYImpulse(1280)
    GFX_0('UltimateStormCharge', 100)
    SLOT_8 = 1
    sprite('Action_449_05', 3)	# 13-15
    sprite('Action_449_06', 3)	# 16-18
    sprite('Action_449_07', 3)	# 19-21
    sprite('Action_449_08', 3)	# 22-24
    sprite('Action_449_09', 4)	# 25-28
    sprite('Action_449_10', 4)	# 29-32
    sprite('Action_449_11', 4)	# 33-36
    sprite('Action_449_12', 6)	# 37-42
    setInvincible(0)
    sprite('Action_449_13', 6)	# 43-48
    sprite('Action_449_14', 7)	# 49-55
    sprite('Action_449_15', 8)	# 56-63
    sprite('Action_449_16', 5)	# 64-68
    physicsYImpulse(10500)
    setGravity(2000)
    sprite('Action_449_17', 5)	# 69-73

@State
def AirUltimateStormOD():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
    sprite('Action_449_02', 4)	# 1-4
    Unknown1084(1)
    physicsXImpulse(-10000)
    Unknown1028(640)
    physicsYImpulse(10000)
    setGravity(640)
    setInvincible(1)
    Unknown7006('uhi253_0', 100, 845768821, 828322613, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_449_03', 4)	# 5-8
    sprite('Action_449_04', 4)	# 9-12
    Unknown2036(28, -1, 0)
    Unknown1084(1)
    setGravity(0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsXImpulse(-1280)
    physicsYImpulse(1280)
    GFX_0('UltimateStormChargeOD', 100)
    SLOT_8 = 1
    sprite('Action_449_05', 3)	# 13-15
    sprite('Action_449_06', 3)	# 16-18
    sprite('Action_449_07', 3)	# 19-21
    sprite('Action_449_08', 3)	# 22-24
    sprite('Action_449_09', 4)	# 25-28
    sprite('Action_449_10', 4)	# 29-32
    sprite('Action_449_11', 4)	# 33-36
    sprite('Action_449_12', 6)	# 37-42
    setInvincible(0)
    sprite('Action_449_13', 6)	# 43-48
    sprite('Action_449_14', 7)	# 49-55
    sprite('Action_449_15', 8)	# 56-63
    sprite('Action_449_16', 5)	# 64-68
    physicsYImpulse(10500)
    setGravity(2000)
    sprite('Action_449_17', 5)	# 69-73

@State
def UltimateBlackHole():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 1201):
                sendToLabel(10)
            if (SLOT_48 == 1202):
                setInvincible(0)
    sprite('Action_261_00', 4)	# 1-4
    sprite('Action_261_01', 4)	# 5-8
    ConsumeSuperMeter(-10000)
    sprite('Action_261_02', 5)	# 9-13
    sprite('Action_261_03', 4)	# 14-17
    sprite('Action_261_04', 4)	# 18-21
    sprite('Action_261_05', 4)	# 22-25
    sprite('Action_261_03', 4)	# 26-29
    sprite('Action_261_04', 2)	# 30-31
    sprite('Action_262_00', 5)	# 32-36
    Unknown2036(62, -1, 0)
    Unknown30080('')
    setInvincible(1)
    sprite('Action_262_01', 5)	# 37-41
    sprite('Action_262_02', 5)	# 42-46
    sprite('Action_262_03', 5)	# 47-51
    sprite('Action_262_04', 5)	# 52-56
    sprite('Action_262_03', 5)	# 57-61
    sprite('Action_262_04', 5)	# 62-66
    sprite('Action_262_03', 5)	# 67-71
    sprite('Action_262_04', 2)	# 72-73
    sprite('Action_262_04', 3)	# 74-76
    GFX_0('UltimateHole_Atk', 100)
    loopRelated(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('Action_262_03', 5)	# 77-81
    sprite('Action_262_04', 5)	# 82-86
    gotoLabel(0)
    label(1)
    sprite('Action_262_05', 10)	# 87-96
    sprite('Action_262_06', 10)	# 97-106
    ExitState()
    label(10)
    sprite('Action_262_03', 5)	# 107-111
    clearUponHandler(17)
    sprite('Action_262_04', 5)	# 112-116
    sprite('Action_262_03', 5)	# 117-121
    sprite('Action_262_04', 5)	# 122-126
    sprite('Action_052_04', 2)	# 127-128
    sprite('Action_052_04', 3)	# 129-131
    sprite('Action_052_05', 7)	# 132-138
    sprite('Action_052_06', 4)	# 139-142
    GFX_0('UltimateHole_HoldAtkEff', 100)
    Unknown38(6, 1)
    GFX_0('UltimateHoleCharge', 100)
    GFX_0('UltimateHoleCamera', 100)
    Unknown38(9, 1)
    sprite('Action_052_07', 7)	# 143-149
    sprite('Action_052_08', 3)	# 150-152
    sprite('Action_052_09', 5)	# 153-157
    sprite('Action_052_10', 2)	# 158-159
    sprite('Action_052_11', 4)	# 160-163
    sprite('Action_052_12', 2)	# 164-165
    sprite('Action_052_13', 5)	# 166-170
    sprite('Action_052_14', 2)	# 171-172
    sprite('Action_052_15', 3)	# 173-175
    sprite('Action_052_09', 5)	# 176-180
    sprite('Action_052_10', 2)	# 181-182
    sprite('Action_052_11', 4)	# 183-186
    sprite('Action_052_12', 2)	# 187-188
    sprite('Action_052_09', 5)	# 189-193
    sprite('Action_052_10', 2)	# 194-195
    sprite('Action_052_16', 3)	# 196-198
    sprite('Action_052_17', 2)	# 199-200
    sprite('Action_052_18', 5)	# 201-205
    sprite('Action_052_19', 4)	# 206-209
    sprite('Action_052_20', 3)	# 210-212
    sprite('Action_052_21', 4)	# 213-216	 **attackbox here**
    sprite('Action_052_22', 3)	# 217-219	 **attackbox here**
    sprite('Action_052_23', 6)	# 220-225	 **attackbox here**
    sprite('Action_052_24', 2)	# 226-227	 **attackbox here**
    sprite('Action_052_25', 8)	# 228-235	 **attackbox here**
    sprite('Action_052_26', 4)	# 236-239	 **attackbox here**
    sprite('Action_052_27', 7)	# 240-246	 **attackbox here**
    sprite('Action_052_28', 2)	# 247-248	 **attackbox here**
    sprite('Action_052_29', 8)	# 249-256	 **attackbox here**
    sprite('Action_052_30', 2)	# 257-258	 **attackbox here**
    sprite('Action_052_31', 5)	# 259-263	 **attackbox here**
    sprite('Action_052_32', 1)	# 264-264	 **attackbox here**
    sprite('Action_052_21', 4)	# 265-268	 **attackbox here**
    sprite('Action_052_22', 3)	# 269-271	 **attackbox here**
    sprite('Action_052_23', 6)	# 272-277	 **attackbox here**
    sprite('Action_052_24', 2)	# 278-279	 **attackbox here**
    sprite('Action_052_25', 8)	# 280-287	 **attackbox here**
    sprite('Action_052_26', 4)	# 288-291	 **attackbox here**
    sprite('Action_052_27', 7)	# 292-298	 **attackbox here**
    sprite('Action_052_28', 2)	# 299-300	 **attackbox here**
    sprite('Action_052_29', 8)	# 301-308	 **attackbox here**
    sprite('Action_052_30', 2)	# 309-310	 **attackbox here**
    sprite('Action_052_31', 5)	# 311-315	 **attackbox here**
    sprite('Action_052_32', 2)	# 316-317	 **attackbox here**
    sprite('Action_052_21', 4)	# 318-321	 **attackbox here**
    Unknown23029(9, 1203, 0)
    Unknown13(6)
    sprite('Action_052_22', 3)	# 322-324	 **attackbox here**
    sprite('Action_052_23', 6)	# 325-330	 **attackbox here**
    sprite('Action_052_24', 2)	# 331-332	 **attackbox here**
    sprite('Action_052_25', 8)	# 333-340	 **attackbox here**
    sprite('Action_052_26', 4)	# 341-344	 **attackbox here**
    sprite('Action_052_27', 7)	# 345-351	 **attackbox here**
    sprite('Action_052_28', 2)	# 352-353	 **attackbox here**
    sprite('Action_052_29', 8)	# 354-361	 **attackbox here**
    sprite('Action_052_30', 2)	# 362-363	 **attackbox here**
    sprite('Action_052_31', 5)	# 364-368	 **attackbox here**
    sprite('Action_052_04', 2)	# 369-370
    Unknown13024(1)
    sprite('Action_052_03', 4)	# 371-374
    sprite('Action_052_02', 3)	# 375-377
    sprite('Action_052_01', 4)	# 378-381
    sprite('Action_052_00', 2)	# 382-383

@State
def UltimateBlackHoleOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 1201):
                sendToLabel(10)
            if (SLOT_48 == 1202):
                setInvincible(0)
    sprite('Action_261_00', 4)	# 1-4
    sprite('Action_261_01', 4)	# 5-8
    ConsumeSuperMeter(-10000)
    sprite('Action_261_02', 5)	# 9-13
    sprite('Action_261_03', 4)	# 14-17
    sprite('Action_261_04', 4)	# 18-21
    sprite('Action_261_05', 4)	# 22-25
    sprite('Action_261_03', 4)	# 26-29
    sprite('Action_261_04', 2)	# 30-31
    sprite('Action_262_00', 5)	# 32-36
    Unknown2036(62, -1, 0)
    Unknown30080('')
    setInvincible(1)
    sprite('Action_262_01', 5)	# 37-41
    sprite('Action_262_02', 5)	# 42-46
    sprite('Action_262_03', 5)	# 47-51
    sprite('Action_262_04', 5)	# 52-56
    sprite('Action_262_03', 5)	# 57-61
    sprite('Action_262_04', 5)	# 62-66
    sprite('Action_262_03', 5)	# 67-71
    sprite('Action_262_04', 2)	# 72-73
    sprite('Action_262_04', 3)	# 74-76
    GFX_0('UltimateHole_AtkOD', 100)
    Unknown23029(1, 1204, 0)
    loopRelated(17, 120)

    def upon_17():
        clearUponHandler(17)
        sendToLabel(1)
    label(0)
    sprite('Action_262_03', 5)	# 77-81
    sprite('Action_262_04', 5)	# 82-86
    gotoLabel(0)
    label(1)
    sprite('Action_262_05', 10)	# 87-96
    sprite('Action_262_06', 10)	# 97-106
    ExitState()
    label(10)
    sprite('Action_262_05', 10)	# 107-116
    clearUponHandler(17)
    Unknown2003(1)
    sprite('Action_262_06', 10)	# 117-126
    sprite('Action_402_00ex01', 4)	# 127-130
    sprite('Action_402_01ex01', 3)	# 131-133
    sprite('Action_402_02ex01', 3)	# 134-136
    sprite('Action_402_03ex01', 3)	# 137-139
    sprite('Action_402_04ex01', 3)	# 140-142
    sprite('Action_402_07ex01', 4)	# 143-146
    GFX_0('UltimateHoleOD_LowShotAtk', 100)
    sprite('Action_402_08', 4)	# 147-150
    sprite('Action_402_09', 4)	# 151-154
    sprite('Action_402_07ex01', 4)	# 155-158
    sprite('Action_402_08', 4)	# 159-162
    sprite('Action_402_09', 4)	# 163-166
    sprite('Action_402_07ex01', 4)	# 167-170
    sprite('Action_402_08', 4)	# 171-174
    sprite('Action_402_09', 4)	# 175-178
    sprite('Action_402_07ex01', 4)	# 179-182
    sprite('Action_402_08', 4)	# 183-186
    sprite('Action_402_09', 4)	# 187-190
    sprite('Action_402_07ex01', 4)	# 191-194
    sprite('Action_402_08', 4)	# 195-198
    sprite('Action_402_09', 4)	# 199-202
    sprite('Action_402_07ex01', 4)	# 203-206
    sprite('Action_402_08', 4)	# 207-210
    sprite('Action_402_09', 4)	# 211-214
    sprite('Action_402_07ex01', 4)	# 215-218
    GFX_0('UltimateHoleCharge', 100)
    GFX_0('UltimateHoleCamera', 100)
    Unknown38(9, 1)
    sprite('Action_402_07ex01', 4)	# 219-222
    sprite('Action_402_08', 4)	# 223-226
    sprite('Action_402_09', 4)	# 227-230
    sprite('Action_402_07ex01', 4)	# 231-234
    sprite('Action_402_08', 4)	# 235-238
    sprite('Action_402_09', 4)	# 239-242
    sprite('Action_402_08', 4)	# 243-246
    sprite('Action_402_09', 4)	# 247-250
    sprite('Action_402_13', 4)	# 251-254
    sprite('Action_402_14', 4)	# 255-258
    sprite('Action_402_15', 4)	# 259-262
    sprite('Action_052_03', 4)	# 263-266
    sprite('Action_052_04', 2)	# 267-268
    sprite('Action_052_04', 3)	# 269-271
    sprite('Action_052_19', 4)	# 272-275
    sprite('Action_052_20', 3)	# 276-278
    sprite('Action_052_21', 4)	# 279-282	 **attackbox here**
    sprite('Action_052_22', 3)	# 283-285	 **attackbox here**
    sprite('Action_052_23', 6)	# 286-291	 **attackbox here**
    sprite('Action_052_24', 2)	# 292-293	 **attackbox here**
    sprite('Action_052_25', 8)	# 294-301	 **attackbox here**
    sprite('Action_052_26', 4)	# 302-305	 **attackbox here**
    sprite('Action_052_27', 7)	# 306-312	 **attackbox here**
    sprite('Action_052_28', 2)	# 313-314	 **attackbox here**
    sprite('Action_052_29', 8)	# 315-322	 **attackbox here**
    sprite('Action_052_30', 2)	# 323-324	 **attackbox here**
    sprite('Action_052_31', 5)	# 325-329	 **attackbox here**
    sprite('Action_052_32', 2)	# 330-331	 **attackbox here**
    sprite('Action_052_21', 4)	# 332-335	 **attackbox here**
    Unknown23029(9, 1203, 0)
    sprite('Action_052_22', 3)	# 336-338	 **attackbox here**
    sprite('Action_052_23', 6)	# 339-344	 **attackbox here**
    sprite('Action_052_24', 2)	# 345-346	 **attackbox here**
    sprite('Action_052_25', 8)	# 347-354	 **attackbox here**
    sprite('Action_052_26', 4)	# 355-358	 **attackbox here**
    sprite('Action_052_27', 7)	# 359-365	 **attackbox here**
    sprite('Action_052_28', 2)	# 366-367	 **attackbox here**
    sprite('Action_052_29', 8)	# 368-375	 **attackbox here**
    sprite('Action_052_30', 2)	# 376-377	 **attackbox here**
    sprite('Action_052_31', 5)	# 378-382	 **attackbox here**
    sprite('Action_052_32', 2)	# 383-384	 **attackbox here**
    sprite('Action_052_21', 4)	# 385-388	 **attackbox here**
    sprite('Action_052_22', 3)	# 389-391	 **attackbox here**
    sprite('Action_052_23', 6)	# 392-397	 **attackbox here**
    sprite('Action_052_24', 2)	# 398-399	 **attackbox here**
    sprite('Action_052_25', 8)	# 400-407	 **attackbox here**
    sprite('Action_052_26', 4)	# 408-411	 **attackbox here**
    sprite('Action_052_27', 7)	# 412-418	 **attackbox here**
    sprite('Action_052_28', 2)	# 419-420	 **attackbox here**
    sprite('Action_052_29', 8)	# 421-428	 **attackbox here**
    sprite('Action_052_30', 2)	# 429-430	 **attackbox here**
    sprite('Action_052_31', 5)	# 431-435	 **attackbox here**
    sprite('Action_052_32', 2)	# 436-437	 **attackbox here**
    sprite('Action_052_21', 4)	# 438-441	 **attackbox here**
    sprite('Action_052_22', 3)	# 442-444	 **attackbox here**
    sprite('Action_052_04', 2)	# 445-446
    Unknown13024(1)
    sprite('Action_052_03', 4)	# 447-450
    sprite('Action_052_02', 3)	# 451-453
    sprite('Action_052_01', 4)	# 454-457
    sprite('Action_052_00', 2)	# 458-459

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(500)
        PushbackX(19800)
        Hitstop(0)
        MinimumDamagePct(100)

        def upon_STATE_END():
            if (not SLOT_66):
                Unknown3004(0)
                Unknown3001(255)
                Unknown13(9)

        def upon_43():
            if (SLOT_48 == 5001):
                if (not SLOT_66):
                    GFX_0('AstralCamera', 100)
                    Unknown38(4, 1)
                    Unknown11067(1)
                    Unknown23157(1)
                    Unknown23088(1, 1)
                    Unknown23084(1)
                    SLOT_66 = 1
    sprite('Action_380_00', 15)	# 1-15
    Unknown2036(70, -1, 2)
    GFX_0('AstralCutIn', 100)
    Unknown23147()
    Unknown4004('617572610000000000000000000000000000000000000000000000000000000000000000')
    Unknown4004('43616c6c5f556e69495745424700000000000000000000000000000000000000ffff0000')
    Unknown38(9, 1)
    setInvincible(1)
    Unknown7006('uhi290', 100, 845768821, 12601, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_380_01', 4)	# 16-19
    sprite('Action_380_02', 4)	# 20-23
    sprite('Action_380_03', 4)	# 24-27
    sprite('Action_380_04', 6)	# 28-33
    GFX_0('AstralShotAtk', 100)
    sprite('Action_380_05', 60)	# 34-93
    sprite('Action_380_05', 5)	# 94-98
    sprite('Action_380_06', 5)	# 99-103
    GFX_0('AstralWarpOut', 100)
    Unknown3004(-12)
    if (not SLOT_66):
        setInvincible(0)
    sprite('Action_380_06', 7)	# 104-110
    sprite('Action_380_07', 15)	# 111-125
    Unknown3001(0)
    sprite('Action_380_07', 1)	# 126-126
    if SLOT_66:
        enterState('AstralHeatExe')
    sprite('Action_160_04', 2)	# 127-128
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-450000)
    sprite('Action_160_04', 3)	# 129-131
    GFX_0('EffWarpOut', 100)
    Unknown3004(21)
    setInvincible(0)
    sprite('Action_160_05', 3)	# 132-134
    sprite('Action_160_06', 4)	# 135-138
    sprite('Action_160_07', 4)	# 139-142
    Unknown3001(255)
    Unknown3004(0)
    sprite('Action_160_08', 4)	# 143-146
    sprite('Action_160_06', 4)	# 147-150
    sprite('Action_160_07', 4)	# 151-154
    sprite('Action_160_08', 4)	# 155-158
    sprite('Action_160_09', 4)	# 159-162
    sprite('Action_160_10', 5)	# 163-167
    sprite('Action_160_11', 5)	# 168-172

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown1096(500)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 5002):
                Unknown3038(1)
                Unknown3025(-1, 10)
            if (SLOT_48 == 5003):
                Unknown1096(1000)
                teleportRelativeX(-500000)
                teleportRelativeY(0)
                Unknown3038(0)
                Unknown13(9)
                Unknown20006(1)
                Unknown23024(0)
                sendToLabel(100)
    sprite('Action_381_00', 21)	# 1-21
    sprite('Action_381_00', 5)	# 22-26
    Unknown1086(4)
    Unknown1007(900000)
    sprite('Action_381_00', 8)	# 27-34
    Unknown23029(4, 5004, 0)
    Unknown3004(12)
    SFX_1('uhi292')
    sprite('Action_381_00', 7)	# 35-41
    GFX_0('AstralExeAura', 100)
    Unknown3004(0)
    Unknown3001(255)
    sprite('Action_381_01', 14)	# 42-55
    sprite('Action_381_02', 5)	# 56-60
    GFX_0('AstralExeBlackOut', 100)
    Unknown3025(-16777216, 60)
    sprite('Action_381_03', 5)	# 61-65
    sprite('Action_381_04', 5)	# 66-70
    sprite('Action_381_05', 5)	# 71-75
    sprite('Action_381_06', 3)	# 76-78
    sprite('Action_381_07', 3)	# 79-81
    label(0)
    sprite('Action_381_08', 3)	# 82-84
    sprite('Action_381_09', 3)	# 85-87
    sprite('Action_381_10', 3)	# 88-90
    gotoLabel(0)
    label(100)
    sprite('Action_382_01', 5)	# 91-95	 **attackbox here**
    sprite('Action_382_02', 5)	# 96-100	 **attackbox here**
    sprite('Action_382_03', 5)	# 101-105	 **attackbox here**
    sprite('Action_382_04', 5)	# 106-110	 **attackbox here**
    sprite('Action_382_05', 5)	# 111-115	 **attackbox here**
    sprite('Action_382_06', 5)	# 116-120	 **attackbox here**
    sprite('Action_382_07', 5)	# 121-125	 **attackbox here**
    sprite('Action_382_08', 5)	# 126-130	 **attackbox here**
    sprite('Action_382_09', 5)	# 131-135	 **attackbox here**
    sprite('Action_382_10', 5)	# 136-140	 **attackbox here**
    sprite('Action_382_01', 5)	# 141-145	 **attackbox here**
    sprite('Action_382_02', 5)	# 146-150	 **attackbox here**
    sprite('Action_382_03', 5)	# 151-155	 **attackbox here**
    sprite('Action_382_04', 5)	# 156-160	 **attackbox here**
    sprite('Action_382_05', 5)	# 161-165	 **attackbox here**
    sprite('Action_382_06', 5)	# 166-170	 **attackbox here**
    sprite('Action_382_07', 5)	# 171-175	 **attackbox here**
    sprite('Action_382_08', 5)	# 176-180	 **attackbox here**
    sprite('Action_382_09', 5)	# 181-185	 **attackbox here**
    sprite('Action_382_10', 5)	# 186-190	 **attackbox here**
    sprite('Action_382_01', 5)	# 191-195	 **attackbox here**
    sprite('Action_382_02', 5)	# 196-200	 **attackbox here**
    sprite('Action_382_03', 5)	# 201-205	 **attackbox here**
    sprite('Action_382_04', 5)	# 206-210	 **attackbox here**
    sprite('Action_382_05', 5)	# 211-215	 **attackbox here**
    sprite('Action_382_06', 5)	# 216-220	 **attackbox here**
    sprite('Action_382_07', 5)	# 221-225	 **attackbox here**
    sprite('Action_382_08', 5)	# 226-230	 **attackbox here**
    sprite('Action_382_09', 5)	# 231-235	 **attackbox here**
    sprite('Action_382_10', 5)	# 236-240	 **attackbox here**
    sprite('Action_382_01', 5)	# 241-245	 **attackbox here**
    sprite('Action_382_02', 5)	# 246-250	 **attackbox here**
    sprite('Action_382_03', 5)	# 251-255	 **attackbox here**
    sprite('Action_382_04', 5)	# 256-260	 **attackbox here**
    sprite('Action_382_05', 5)	# 261-265	 **attackbox here**
    sprite('Action_382_06', 5)	# 266-270	 **attackbox here**
    sprite('Action_382_07', 5)	# 271-275	 **attackbox here**
    sprite('Action_382_08', 5)	# 276-280	 **attackbox here**
    sprite('Action_382_09', 5)	# 281-285	 **attackbox here**
    sprite('Action_382_10', 5)	# 286-290	 **attackbox here**
    sprite('Action_382_01', 5)	# 291-295	 **attackbox here**
    sprite('Action_382_02', 5)	# 296-300	 **attackbox here**
    sprite('Action_382_03', 5)	# 301-305	 **attackbox here**
    sprite('Action_382_04', 5)	# 306-310	 **attackbox here**
    sprite('Action_382_05', 5)	# 311-315	 **attackbox here**
    sprite('Action_382_06', 5)	# 316-320	 **attackbox here**
    sprite('Action_382_07', 5)	# 321-325	 **attackbox here**
    sprite('Action_382_08', 5)	# 326-330	 **attackbox here**
    sprite('Action_382_09', 5)	# 331-335	 **attackbox here**
    sprite('Action_382_10', 5)	# 336-340	 **attackbox here**
    sprite('Action_382_11', 5)	# 341-345
    sprite('Action_382_12', 5)	# 346-350
    sprite('Action_382_13', 5)	# 351-355

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
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_125_00', 2)	# 1-2
    Unknown1019(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('Action_125_01', 2)	# 3-4
    sprite('Action_125_02', 2)	# 5-6
    sprite('Action_125_03', 3)	# 7-9
    GFX_0('EffWarpOut', 100)
    sprite('Action_125_04', 3)	# 10-12
    sprite('Action_125_05', 3)	# 13-15
    sprite('Action_125_06', 30)	# 16-45

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('Action_248_00', 5)	# 1-5	 **attackbox here**
    sprite('Action_248_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_248_02', 6)	# 11-16	 **attackbox here**
    sprite('Action_248_03', 5)	# 17-21
    sprite('Action_248_04', 50)	# 22-71	 **attackbox here**
    sprite('Action_248_02', 30)	# 72-101	 **attackbox here**

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)
        Unknown11032('ffffffffffffffffa08601003022f9ff')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 27)	# 603-629
    label(0)
    sprite('Action_160_06', 1)	# 630-630
    Unknown1086(22)
    teleportRelativeX(-200000)
    teleportRelativeY(200000)
    Unknown3001(0)
    Unknown3004(42)
    GFX_0('EffWarpIn', 100)
    sprite('Action_160_06', 1)	# 631-631
    sprite('Action_149_00ex01', 1)	# 632-632
    sprite('Action_149_01ex01', 1)	# 633-633
    sprite('Action_149_04', 1)	# 634-634	 **attackbox here**
    EnableCollision(1)
    Unknown2053(1)
    Unknown3001(255)
    Unknown3004(0)
    sprite('Action_149_05', 1)	# 635-635	 **attackbox here**
    sprite('Action_149_06', 3)	# 636-638	 **attackbox here**
    sprite('Action_149_06', 2)	# 639-640	 **attackbox here**
    Unknown1043()
    sprite('Action_149_10', 4)	# 641-644
    GFX_0('EffBurst', 100)
    sprite('Action_149_11', 4)	# 645-648
    sprite('Action_036_06', 5)	# 649-653
    sprite('Action_036_07', 5)	# 654-658
    sprite('Action_036_08', 5)	# 659-663
    label(2)
    sprite('Action_020_00', 4)	# 664-667
    sprite('Action_020_01', 4)	# 668-671
    sprite('Action_020_02', 4)	# 672-675
    gotoLabel(2)
    label(1)
    sprite('Action_021_00', 3)	# 676-678
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_021_01', 3)	# 679-681
    ExitState()

@State
def CmnActChangeReturnAppealBurst():
    sprite('Action_312_02', 2)	# 1-2
    sprite('Action_312_03', 2)	# 3-4
    sprite('Action_312_04', 12)	# 5-16
    sprite('Action_312_04', 12)	# 17-28
    Unknown18009(1)
    sprite('Action_312_05', 4)	# 29-32
    sprite('Action_312_06', 4)	# 33-36	 **attackbox here**
    sprite('Action_312_07', 4)	# 37-40	 **attackbox here**
    sprite('Action_312_08', 4)	# 41-44	 **attackbox here**
    sprite('Action_014_00', 4)	# 45-48	 **attackbox here**
    sprite('Action_014_01', 4)	# 49-52	 **attackbox here**
    sprite('Action_014_02', 4)	# 53-56	 **attackbox here**
    sprite('Action_000_00', 30)	# 57-86	 **attackbox here**

@State
def CmnActChangePartnerQuickIn():
    sprite('Action_160_06', 8)	# 1-8
    GFX_0('EffWarpIn', 100)
    sprite('Action_160_06', 2)	# 9-10
    sprite('Action_160_07', 3)	# 11-13
    sprite('Action_160_08', 3)	# 14-16
    sprite('Action_160_09', 3)	# 17-19
    sprite('Action_160_10', 3)	# 20-22
    sprite('Action_160_11', 3)	# 23-25

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
    sprite('Action_046_04', 3)	# 7-9
    loopRest()
    label(0)
    sprite('Action_046_04', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('Action_046_07', 3)	# 13-15
    sprite('Action_046_08', 3)	# 16-18

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2042(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('Action_160_06', 2)	# 1-2
    Unknown3001(0)
    Unknown3004(19)
    Unknown1086(24)
    teleportRelativeX(-78520)
    teleportRelativeY(0)
    Unknown2006()
    physicsXImpulse(1000)
    physicsYImpulse(1000)
    setGravity(100)
    GFX_0('EffWarpIn', 100)
    sprite('Action_160_07', 3)	# 3-5
    sprite('Action_160_08', 3)	# 6-8
    sprite('Action_160_09', 3)	# 9-11
    sprite('Action_160_10', 3)	# 12-14
    sprite('Action_160_11', 3)	# 15-17
    sprite('keep', 100)	# 18-117
    Unknown1084(1)
    teleportRelativeY(0)

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
    sprite('Action_250_00', 2)	# 1-2	 **attackbox here**
    sprite('Action_250_01', 2)	# 3-4	 **attackbox here**
    sprite('Action_250_02', 2)	# 5-6	 **attackbox here**
    sprite('Action_250_03', 3)	# 7-9	 **attackbox here**
    teleportRelativeX(10000)
    Unknown7006('uhi217_0', 100, 845768821, 828323633, 0, 0, 100, 845768821, 845100849, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_250_04', 3)	# 10-12	 **attackbox here**
    sprite('Action_250_05', 3)	# 13-15	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_250_06', 3)	# 16-18	 **attackbox here**
    sprite('Action_250_07', 3)	# 19-21	 **attackbox here**
    teleportRelativeX(20000)
    sprite('Action_250_08', 5)	# 22-26	 **attackbox here**
    teleportRelativeX(10000)
    sprite('Action_250_09', 8)	# 27-34	 **attackbox here**
    teleportRelativeX(14000)
    sprite('Action_250_10', 5)	# 35-39	 **attackbox here**
    sprite('Action_250_11', 5)	# 40-44	 **attackbox here**
    SFX_3('SE_BallExplosion')
    GFX_0('EffSpreadShotDel', 100)
    GFX_0('SpreadShotMatome', 0)
    Unknown23029(1, 508, 0)
    sprite('Action_250_12', 10)	# 45-54	 **attackbox here**
    sprite('Action_250_13', 5)	# 55-59
    sprite('Action_250_14', 4)	# 60-63
    sprite('Action_250_15', 3)	# 64-66

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(800)
        Hitstop(5)
        AttackP1(70)
        Unknown11092(1)
        PushbackX(9800)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(1900)
        AirUntechableTime(60)
        Unknown11042(1)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        GroundedHitstunAnimation(1)
    sprite('Action_003_00', 6)	# 1-6
    sprite('Action_003_01', 6)	# 7-12
    sprite('Action_003_02', 9)	# 13-21	 **attackbox here**
    sprite('Action_003_03', 3)	# 22-24	 **attackbox here**
    sprite('Action_003_04', 2)	# 25-26	 **attackbox here**
    sprite('Action_003_05', 3)	# 27-29	 **attackbox here**
    SFX_3('SE_Hari_Appear')
    Unknown7006('uhi110_0', 100, 828991605, 828321841, 0, 0, 100, 845768821, 845100081, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_003_06', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    sprite('Action_003_07', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    sprite('Action_003_08ex01', 3)	# 36-38	 **attackbox here**
    RefreshMultihit()
    sprite('Action_003_09ex01', 3)	# 39-41	 **attackbox here**
    RefreshMultihit()
    sprite('Action_003_10', 3)	# 42-44	 **attackbox here**
    Recovery()
    sprite('Action_003_11', 5)	# 45-49
    GFX_0('EffAtkAIR5B2nd', 100)
    sprite('Action_003_12', 5)	# 50-54
    sprite('Action_003_13', 5)	# 55-59
    sprite('Action_003_14', 5)	# 60-64
    sprite('Action_003_15', 5)	# 65-69
    sprite('Action_003_16', 5)	# 70-74
    sprite('Action_003_17', 5)	# 75-79
    loopRest()

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(650)
        AttackP1(70)
        Unknown11092(1)
        Unknown11042(1)
        Hitstop(2)
        GroundedHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        Hitstop(2)
        PushbackX(25000)
        AirPushbackX(12000)
        AirPushbackY(30000)
        AirUntechableTime(60)
        Unknown9016(1)
        Unknown30055('20a10700c8000000c8000000')
        Unknown30056('a08601006400000064000000')
    sprite('Action_010_00', 2)	# 1-2
    sprite('Action_045_00', 2)	# 3-4
    Unknown1045(32000)
    sprite('Action_045_01', 2)	# 5-6
    sprite('Action_402_00', 2)	# 7-8	 **attackbox here**
    sprite('Action_402_01', 3)	# 9-11	 **attackbox here**
    sprite('Action_402_02', 3)	# 12-14	 **attackbox here**
    SFX_4('uhi108_0')
    SFX_3('SE_Hari_Appear')
    sprite('Action_402_03', 3)	# 15-17	 **attackbox here**
    sprite('Action_402_04', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    sprite('Action_402_05', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    sprite('Action_402_06', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('Action_402_07', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    Unknown30055('ffffffffffffffffffffffff')
    Unknown30056('ffffffffffffffffffffffff')
    sprite('Action_402_08', 4)	# 26-29
    GFX_0('EffAtk5A', 100)
    sprite('Action_402_09', 4)	# 30-33
    sprite('Action_402_10', 4)	# 34-37
    sprite('Action_402_11', 4)	# 38-41
    sprite('Action_402_12', 4)	# 42-45
    sprite('Action_402_13', 4)	# 46-49
    sprite('Action_402_14', 4)	# 50-53
    sprite('Action_402_15', 4)	# 54-57

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
    Unknown2036(107, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-500000)
    Unknown1019(4)
    label(0)
    sprite('Action_035_06', 4)	# 3-6
    sprite('Action_035_07', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateAllRangeShotDDDOD')
    else:
        enterState('UltimateAllRangeShotDDD')

@State
def UltimateAllRangeShotDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(4)
        Damage(250)
        AttackP1(100)
        AttackP2(100)
        Unknown11064(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MinimumDamagePct(100)
        AirUntechableTime(150)
        AirPushbackX(0)
        AirPushbackY(3000)
        YImpluseBeforeWallbounce(30)
        Unknown30048(1)
        Unknown11084(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11069('AllRangeShotAtk')
        Unknown11023(1)

        def upon_78():
            Hitstop(0)
            sendToLabel(100)
    sprite('Action_052_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_052_01', 5)	# 6-10
    sprite('Action_052_02', 5)	# 11-15
    sprite('Action_052_03', 5)	# 16-20
    sprite('Action_052_04', 5)	# 21-25
    sprite('Action_233_00', 15)	# 26-40
    sprite('Action_233_01', 3)	# 41-43	 **attackbox here**
    sprite('Action_233_02', 3)	# 44-46	 **attackbox here**
    Unknown18009(1)
    sprite('Action_233_03', 3)	# 47-49	 **attackbox here**
    sprite('Action_233_04', 4)	# 50-53	 **attackbox here**
    sprite('Action_233_05', 3)	# 54-56	 **attackbox here**
    sprite('Action_233_06', 5)	# 57-61	 **attackbox here**
    sprite('Action_233_07', 5)	# 62-66	 **attackbox here**
    sprite('Action_233_08', 6)	# 67-72	 **attackbox here**
    sprite('Action_233_09', 10)	# 73-82	 **attackbox here**
    sprite('Action_233_10', 5)	# 83-87	 **attackbox here**
    sprite('Action_233_11', 8)	# 88-95	 **attackbox here**
    setInvincible(0)
    sprite('Action_233_12', 7)	# 96-102	 **attackbox here**
    sprite('Action_233_13', 10)	# 103-112	 **attackbox here**
    sprite('Action_233_14', 10)	# 113-122	 **attackbox here**
    sprite('Action_232_00', 8)	# 123-130	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_234_00', 5)	# 131-135	 **attackbox here**
    setInvincible(1)
    GFX_0('AllRangeShotAtk', 100)
    Unknown23029(1, 1150, 0)
    sprite('Action_234_01', 8)	# 136-143	 **attackbox here**
    sprite('Action_234_02', 5)	# 144-148	 **attackbox here**
    sprite('Action_234_03', 7)	# 149-155	 **attackbox here**
    sprite('Action_234_04', 5)	# 156-160	 **attackbox here**
    sprite('Action_234_05', 20)	# 161-180	 **attackbox here**
    sprite('Action_234_06', 4)	# 181-184	 **attackbox here**
    sprite('Action_234_07', 7)	# 185-191	 **attackbox here**
    sprite('Action_234_08', 10)	# 192-201	 **attackbox here**
    sprite('Action_234_09', 4)	# 202-205	 **attackbox here**
    sprite('Action_234_10', 7)	# 206-212	 **attackbox here**
    sprite('Action_234_11', 7)	# 213-219	 **attackbox here**
    sprite('Action_234_12', 4)	# 220-223	 **attackbox here**
    sprite('Action_234_13', 7)	# 224-230	 **attackbox here**
    sprite('Action_234_14', 3)	# 231-233	 **attackbox here**
    sprite('Action_234_15', 8)	# 234-241	 **attackbox here**
    sprite('Action_234_16', 8)	# 242-249	 **attackbox here**
    SFX_1('uhi252')
    sprite('Action_234_17', 8)	# 250-257	 **attackbox here**
    sprite('Action_234_18', 8)	# 258-265	 **attackbox here**
    sprite('Action_234_19', 8)	# 266-273	 **attackbox here**
    sprite('Action_234_20', 7)	# 274-280	 **attackbox here**
    sprite('Action_234_21', 7)	# 281-287	 **attackbox here**
    sprite('Action_234_22', 7)	# 288-294	 **attackbox here**
    sprite('Action_234_23', 7)	# 295-301	 **attackbox here**
    sprite('Action_234_24', 7)	# 302-308	 **attackbox here**
    sprite('Action_234_25', 7)	# 309-315	 **attackbox here**
    sprite('Action_234_26', 7)	# 316-322	 **attackbox here**
    sprite('Action_234_27', 7)	# 323-329	 **attackbox here**
    sprite('Action_234_28', 4)	# 330-333	 **attackbox here**
    sprite('Action_234_29', 7)	# 334-340	 **attackbox here**
    sprite('Action_234_48', 7)	# 341-347	 **attackbox here**
    sprite('Action_234_49', 7)	# 348-354	 **attackbox here**
    sprite('Action_234_50', 6)	# 355-360	 **attackbox here**
    sprite('Action_234_51', 8)	# 361-368	 **attackbox here**
    sprite('Action_234_52', 5)	# 369-373	 **attackbox here**
    sprite('Action_234_53', 5)	# 374-378	 **attackbox here**

@State
def UltimateAllRangeShotDDDOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(4)
        Damage(250)
        Unknown11064(1)
        GroundedHitstunAnimation(10)
        AirHitstunAnimation(10)
        MinimumDamagePct(100)
        AirUntechableTime(150)
        AirPushbackX(0)
        AirPushbackY(3000)
        YImpluseBeforeWallbounce(30)
        Unknown30048(1)
        Unknown11084(1)
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11069('AllRangeShotAtkOD')
        Unknown11023(1)

        def upon_78():
            Hitstop(0)
            sendToLabel(100)
    sprite('Action_052_00', 5)	# 1-5
    setInvincible(1)
    sprite('Action_052_01', 5)	# 6-10
    sprite('Action_052_02', 5)	# 11-15
    sprite('Action_052_03', 5)	# 16-20
    sprite('Action_052_04', 5)	# 21-25
    sprite('Action_233_00', 15)	# 26-40
    sprite('Action_233_01', 3)	# 41-43	 **attackbox here**
    sprite('Action_233_02', 3)	# 44-46	 **attackbox here**
    Unknown18009(1)
    sprite('Action_233_03', 3)	# 47-49	 **attackbox here**
    sprite('Action_233_04', 4)	# 50-53	 **attackbox here**
    sprite('Action_233_05', 3)	# 54-56	 **attackbox here**
    sprite('Action_233_06', 5)	# 57-61	 **attackbox here**
    sprite('Action_233_07', 5)	# 62-66	 **attackbox here**
    sprite('Action_233_08', 6)	# 67-72	 **attackbox here**
    sprite('Action_233_09', 10)	# 73-82	 **attackbox here**
    sprite('Action_233_10', 5)	# 83-87	 **attackbox here**
    sprite('Action_233_11', 8)	# 88-95	 **attackbox here**
    setInvincible(0)
    sprite('Action_233_12', 7)	# 96-102	 **attackbox here**
    sprite('Action_233_13', 10)	# 103-112	 **attackbox here**
    sprite('Action_233_14', 10)	# 113-122	 **attackbox here**
    sprite('Action_232_00', 8)	# 123-130	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_234_00', 5)	# 131-135	 **attackbox here**
    setInvincible(1)
    GFX_0('AllRangeShotAtkOD', 100)
    Unknown23029(1, 1150, 0)
    sprite('Action_234_01', 8)	# 136-143	 **attackbox here**
    sprite('Action_234_02', 5)	# 144-148	 **attackbox here**
    sprite('Action_234_03', 7)	# 149-155	 **attackbox here**
    sprite('Action_234_04', 5)	# 156-160	 **attackbox here**
    sprite('Action_234_05', 20)	# 161-180	 **attackbox here**
    SFX_1('uhi251')
    sprite('Action_234_06', 4)	# 181-184	 **attackbox here**
    sprite('Action_234_07', 7)	# 185-191	 **attackbox here**
    sprite('Action_234_08', 10)	# 192-201	 **attackbox here**
    sprite('Action_234_09', 4)	# 202-205	 **attackbox here**
    sprite('Action_234_10', 7)	# 206-212	 **attackbox here**
    sprite('Action_234_11', 7)	# 213-219	 **attackbox here**
    sprite('Action_234_12', 4)	# 220-223	 **attackbox here**
    sprite('Action_234_13', 7)	# 224-230	 **attackbox here**
    sprite('Action_234_14', 3)	# 231-233	 **attackbox here**
    sprite('Action_234_15', 8)	# 234-241	 **attackbox here**
    sprite('Action_234_16', 8)	# 242-249	 **attackbox here**
    sprite('Action_234_17', 8)	# 250-257	 **attackbox here**
    sprite('Action_234_18', 8)	# 258-265	 **attackbox here**
    sprite('Action_234_19', 8)	# 266-273	 **attackbox here**
    sprite('Action_234_20', 7)	# 274-280	 **attackbox here**
    sprite('Action_234_21', 7)	# 281-287	 **attackbox here**
    sprite('Action_234_22', 7)	# 288-294	 **attackbox here**
    sprite('Action_234_23', 7)	# 295-301	 **attackbox here**
    SFX_1('uhi252')
    sprite('Action_234_24', 7)	# 302-308	 **attackbox here**
    sprite('Action_234_25', 7)	# 309-315	 **attackbox here**
    sprite('Action_234_26', 7)	# 316-322	 **attackbox here**
    sprite('Action_234_27', 7)	# 323-329	 **attackbox here**
    sprite('Action_234_28', 4)	# 330-333	 **attackbox here**
    sprite('Action_234_29', 7)	# 334-340	 **attackbox here**
    sprite('Action_234_30', 7)	# 341-347	 **attackbox here**
    sprite('Action_234_31', 7)	# 348-354	 **attackbox here**
    sprite('Action_234_32', 7)	# 355-361	 **attackbox here**
    sprite('Action_234_33', 7)	# 362-368	 **attackbox here**
    sprite('Action_234_34', 7)	# 369-375	 **attackbox here**
    sprite('Action_234_35', 7)	# 376-382	 **attackbox here**
    sprite('Action_234_36', 7)	# 383-389	 **attackbox here**
    sprite('Action_234_37', 7)	# 390-396	 **attackbox here**
    sprite('Action_234_38', 7)	# 397-403	 **attackbox here**
    sprite('Action_234_39', 7)	# 404-410	 **attackbox here**
    sprite('Action_234_40', 8)	# 411-418	 **attackbox here**
    sprite('Action_234_45', 7)	# 419-425	 **attackbox here**
    sprite('Action_234_46', 7)	# 426-432	 **attackbox here**
    sprite('Action_234_47', 7)	# 433-439	 **attackbox here**
    sprite('Action_234_48', 8)	# 440-447	 **attackbox here**
    sprite('Action_234_49', 8)	# 448-455	 **attackbox here**
    sprite('Action_234_50', 6)	# 456-461	 **attackbox here**
    sprite('Action_234_51', 8)	# 462-469	 **attackbox here**
    sprite('Action_234_52', 6)	# 470-475	 **attackbox here**
    sprite('Action_234_53', 6)	# 476-481	 **attackbox here**

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
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 13)	# 121-133
    sprite('Action_160_06', 4)	# 134-137
    Unknown1086(22)
    teleportRelativeX(-200000)
    Unknown1007(200000)
    Unknown3001(0)
    Unknown3004(19)
    GFX_0('EffWarpIn', 100)
    Unknown2053(1)
    sprite('Action_160_06', 4)	# 138-141
    sprite('Action_149_00ex01', 1)	# 142-142
    sprite('Action_149_01ex01', 2)	# 143-144
    Unknown3001(255)
    Unknown3004(0)
    sprite('Action_149_04', 2)	# 145-146	 **attackbox here**
    sprite('Action_149_05', 2)	# 147-148	 **attackbox here**
    sprite('Action_149_06', 3)	# 149-151	 **attackbox here**
    sprite('Action_149_06', 2)	# 152-153	 **attackbox here**
    Unknown1043()
    sprite('Action_149_10', 4)	# 154-157
    GFX_0('EffBurst', 100)
    sprite('Action_149_11', 4)	# 158-161
    sprite('Action_036_06', 5)	# 162-166
    sprite('Action_036_07', 5)	# 167-171
    sprite('Action_036_08', 5)	# 172-176
    label(2)
    sprite('Action_020_00', 4)	# 177-180
    sprite('Action_020_01', 4)	# 181-184
    sprite('Action_020_02', 4)	# 185-188
    gotoLabel(2)
    label(1)
    sprite('Action_021_00', 8)	# 189-196
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('Action_021_01', 6)	# 197-202

@Subroutine
def MouthTableInit():
    Unknown18011('uhi000', 13665, 12643, 24886, 25397, 24886, 25397, 24885, 25397, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhi600def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25400, 13873, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600def', '001')
    Unknown18011('uhi601def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi601def', '002')
    Unknown18011('uhi602def', 12643, 12897, 25396, 24887, 12595, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi602def', '003')
    Unknown18011('uhi603def', 12643, 13153, 25395, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi603def', '004')
    Unknown18011('uhi604def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi604def', '005')
    Unknown18011('uhi605def', 12643, 12897, 25395, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi605def', '006')
    Unknown18011('uhi700def', 14177, 12899, 24883, 25397, 24886, 25397, 12851, 13153, 25399, 12849, 14689, 13923, 14177, 13923, 14433, 13923, 14177, 13667, 14177, 13667, 14177, 13667, 13921, 14179, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700def', '007')
    Unknown18011('uhi701def', 12643, 14433, 14179, 14433, 14179, 14433, 14179, 14433, 13155, 24881, 12337, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25395, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi701def', '008')
    Unknown18011('uhi702def', 12641, 25396, 24887, 13618, 12899, 24884, 13873, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi702def', '009')
    Unknown18011('uhi703def', 13921, 14179, 13921, 12643, 24882, 12849, 12899, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 13363, 12643, 24887, 12337, 12643, 24880, 25399, 24884, 25398, 24884, 25398, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi703def', '010')
    Unknown18011('uhi704def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi704def', '011')
    Unknown18011('uhi705def', 13921, 12643, 24882, 25395, 24883, 25395, 13619, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi705def', '012')
    Unknown18011('uhi402_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 14386, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhi402_1', 13409, 25397, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24889, 25400, 13362, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhi403_0', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhi403_1', 14177, 14179, 12641, 25394, 12339, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('uhi601brc', 12899, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi601brc', '017')
    Unknown18011('uhi601bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi601bny', '018')
    Unknown18011('uhi600bhz', 12643, 12897, 25399, 14641, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600bhz', '019')
    Unknown18011('uhi601bph', 12643, 12897, 25393, 14385, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi601bph', '020')
    Unknown18011('uhi600pce', 12643, 13153, 25394, 24888, 13874, 12643, 24888, 25399, 13361, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600pce', '021')
    Unknown18011('uhi600pka', 14435, 12641, 25398, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600pka', '022')
    Unknown18011('uhi600pmi', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24883, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600pmi', '023')
    Unknown18011('uhi600uhy', 12899, 14177, 14179, 13153, 25401, 13874, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600uhy', '024')
    Unknown18011('uhi600uli', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600uli', '025')
    Unknown18011('uhi601rwi', 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi601rwi', '026')
    Unknown18011('uhi600uak', 12643, 24885, 13618, 12899, 24882, 13361, 13155, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600uak', '027')
    Unknown18011('uhi600pad', 13923, 12897, 25394, 24887, 13618, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600pad', '028')
    Unknown18011('uhi600pel', 12643, 14177, 12643, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13362, 12641, 25392, 14130, 12641, 25392, 14130, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600pel', '029')
    Unknown18011('uhi600rne', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24888, 25399, 24887, 12337, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi600rne', '030')
    Unknown18011('uhi701brc', 12643, 12641, 25394, 13361, 14177, 14179, 14177, 14179, 13409, 25394, 14385, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi701brc', '031')
    Unknown18011('uhi701bny', 12899, 14177, 14179, 13409, 25394, 13619, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 13362, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi701bny', '032')
    Unknown18011('uhi700bhz', 13667, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700bhz', '033')
    Unknown18011('uhi700bph', 12643, 12641, 25392, 24887, 14642, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700bph', '034')
    Unknown18011('uhi700pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700pce', '035')
    Unknown18011('uhi700pka', 14177, 14179, 12641, 25398, 14130, 13923, 13153, 13923, 13153, 13923, 13153, 13923, 13153, 12643, 24888, 25400, 24887, 12593, 13923, 13665, 13923, 13665, 13155, 24886, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700pka', '036')
    Unknown18011('uhi700pmi', 12641, 25398, 12337, 13409, 25400, 12595, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700pmi', '037')
    Unknown18011('uhi700uhy', 12899, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 14386, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 13875, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700uhy', '038')
    Unknown18011('uhi701uli', 12643, 12641, 25401, 24887, 12849, 12643, 24886, 25399, 24887, 13105, 12643, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi701uli', '039')
    Unknown18011('uhi700rwi', 12643, 12641, 25392, 24887, 12337, 14179, 14177, 14179, 13665, 14691, 14177, 14179, 14177, 14179, 13409, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700rwi', '040')
    Unknown18011('uhi700uak', 12643, 14177, 12643, 24883, 12594, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12851, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700uak', '041')
    Unknown18011('uhi701pad', 12643, 12641, 25396, 13617, 14689, 14179, 13665, 25399, 14642, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi701pad', '042')
    Unknown18011('uhi700pel', 12643, 12641, 25393, 24887, 13106, 14179, 12897, 25393, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 13362, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi700pel', '043')
    Unknown18011('uhi701rne', 12643, 14433, 14179, 13153, 25392, 13107, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('uhi701rne', '044')
    if SLOT_172:
        Unknown18011('uhi000', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 13667, 13665, 13923, 12897, 13667, 12641, 13155, 14177, 14179, 13665, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600def', 12643, 14435, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi601def', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi602def', 12643, 12643, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 13667, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi603def', 12643, 12643, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 13923, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi604def', 12643, 12643, 12641, 12643, 14177, 14179, 12897, 13923, 14177, 14179, 14177, 14179, 12897, 13155, 14177, 13923, 12899, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi605def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12643, 13665, 12643, 24880, 25399, 24887, 25398, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 24881, 25399, 24887, 25398, 24881, 25399, 25394, 24883, 25399, 25394, 24881, 25399, 25393, 24887, 25395, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi701def', 12643, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 13155, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi702def', 12643, 12643, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi703def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 24885, 25399, 24887, 25399, 24887, 25393, 24883, 25396, 24887, 25394, 24881, 25394, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi704def', 12643, 12643, 14177, 14179, 14177, 14179, 12641, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13667, 13921, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi705def', 12643, 12643, 14177, 14179, 14177, 14179, 13153, 12899, 13665, 12643, 24885, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi402_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi402_1', 12643, 14177, 14179, 14177, 14179, 12897, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25393, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi403_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi403_1', 12643, 12899, 14177, 14179, 14177, 12899, 24884, 25399, 24887, 25399, 24887, 25399, 25393, 24883, 25399, 24887, 25399, 24887, 25395, 24882, 25399, 24887, 25399, 24887, 25394, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25394, 24882, 25399, 24887, 25399, 24887, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi601brc', 12643, 12643, 14177, 14179, 12897, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 13411, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi601bny', 12643, 12643, 14177, 13667, 12643, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 13667, 12899, 13921, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600bhz', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 14177, 13667, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi601bph', 12643, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 13155, 12899, 14177, 14179, 14177, 12899, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600pce', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600pka', 12643, 14177, 13667, 12643, 13921, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600pmi', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600uhy', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12641, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600uli', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13155, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13923, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi601rwi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600uak', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14691, 14177, 14179, 13153, 12899, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 13153, 12643, 13921, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 13153, 12899, 12897, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600pad', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13411, 14177, 14179, 14177, 14179, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13411, 14177, 13411, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600pel', 12643, 12643, 14177, 14179, 14177, 14179, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi600rne', 12643, 12899, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 13411, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi701brc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 13411, 14177, 12643, 12643, 24880, 25399, 24887, 25399, 25393, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25395, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi701bny', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13667, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 13155, 13155, 12897, 13411, 14177, 14179, 14177, 14179, 13153, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700bhz', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 12897, 12643, 24888, 25399, 25399, 24882, 25399, 24887, 25399, 24887, 25399, 25398, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700bph', 12643, 12899, 14177, 14179, 14177, 13923, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700pce', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700pka', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 12899, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700pmi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 14177, 13923, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700uhy', 12643, 14177, 14179, 13665, 13155, 14177, 14179, 14177, 14179, 13153, 13155, 14177, 14179, 14177, 12643, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 24883, 25399, 24887, 25399, 25396, 24882, 25399, 24887, 25397, 24882, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi701uli', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700rwi', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700uak', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 13409, 12643, 24883, 25399, 24887, 25399, 25396, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 24883, 25399, 24887, 25399, 25398, 24883, 25399, 24887, 25399, 24887, 25399, 25399, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi701pad', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13411, 14177, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi700pel', 12643, 12643, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('uhi701rne', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 14177, 13155, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25397, 24882, 25397, 24881, 25396, 24882, 25399, 24887, 25399, 24887, 25399, 24881, 25393, 24885, 25399, 25399, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    PartnerChar('brc')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bny')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('bhz')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('pce')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('pka')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('pmi')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('uhy')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('uli')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('rwi')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uak')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('pad')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('pel')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('rne')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('bph')
    if SLOT_ReturnVal:
        _gotolabel(230)
    Unknown19(991, 2, 158)
    label(0)
    sprite('null', 1)	# 2-2
    Unknown3038(1)
    teleportRelativeY(675000)
    setGravity(0)
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    label(1)
    sprite('Action_120_00', 5)	# 3-7	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 3)
    loopRest()
    label(2)
    sprite('Action_120_01', 5)	# 8-12	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 13-17	 **attackbox here**
    sprite('Action_120_03', 5)	# 18-22	 **attackbox here**
    sprite('Action_120_04', 5)	# 23-27	 **attackbox here**
    sprite('Action_120_05', 5)	# 28-32	 **attackbox here**
    sprite('Action_120_06', 5)	# 33-37	 **attackbox here**
    sprite('Action_120_07', 5)	# 38-42	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 43-47	 **attackbox here**
    sprite('Action_120_09', 5)	# 48-52	 **attackbox here**
    sprite('Action_120_10', 5)	# 53-57	 **attackbox here**
    sprite('Action_120_11', 5)	# 58-62	 **attackbox here**
    sprite('Action_120_12', 5)	# 63-67	 **attackbox here**
    gotoLabel(2)
    label(3)
    sprite('Action_050_02', 3)	# 68-70
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 71-73
    sprite('Action_050_04', 3)	# 74-76
    sprite('Action_050_05', 5)	# 77-81
    sprite('Action_050_06', 5)	# 82-86
    sprite('Action_050_07', 4)	# 87-90	 **attackbox here**
    if SLOT_158:
        if random_(2, 0, 50):
            Unknown7006('uhi600def', 100, 912877685, 1701065008, 102, 0, 100, 912877685, 1701065264, 102, 0, 100, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uhi603def', 100, 912877685, 1701065776, 102, 0, 100, 912877685, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_050_08', 4)	# 91-94	 **attackbox here**
    sprite('Action_050_09', 2)	# 95-96	 **attackbox here**
    label(4)
    sprite('Action_050_10', 5)	# 97-101	 **attackbox here**
    sprite('Action_050_11', 5)	# 102-106	 **attackbox here**
    sprite('Action_050_12', 5)	# 107-111	 **attackbox here**
    sprite('Action_050_13', 5)	# 112-116	 **attackbox here**
    sprite('Action_050_14', 5)	# 117-121	 **attackbox here**
    sprite('Action_050_15', 5)	# 122-126	 **attackbox here**
    sprite('Action_050_16', 5)	# 127-131	 **attackbox here**
    sprite('Action_050_17', 5)	# 132-136	 **attackbox here**
    sprite('Action_050_18', 5)	# 137-141	 **attackbox here**
    sprite('Action_050_19', 5)	# 142-146	 **attackbox here**
    if SLOT_97:
        _gotolabel(4)
    sprite('Action_050_20', 5)	# 147-151	 **attackbox here**
    sprite('Action_050_21', 5)	# 152-156	 **attackbox here**
    sprite('Action_050_22', 5)	# 157-161	 **attackbox here**
    sprite('Action_050_23', 5)	# 162-166	 **attackbox here**
    sprite('Action_050_24', 5)	# 167-171	 **attackbox here**
    sprite('Action_050_25', 5)	# 172-176	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_000_00', 5)	# 177-181	 **attackbox here**
    Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_000_01', 5)	# 182-186	 **attackbox here**
    sprite('Action_000_02', 5)	# 187-191	 **attackbox here**
    sprite('Action_000_03', 5)	# 192-196	 **attackbox here**
    sprite('Action_000_04', 5)	# 197-201	 **attackbox here**
    sprite('Action_000_05', 5)	# 202-206	 **attackbox here**
    sprite('Action_000_06', 5)	# 207-211	 **attackbox here**
    sprite('Action_000_07', 5)	# 212-216	 **attackbox here**
    sprite('Action_000_08', 5)	# 217-221	 **attackbox here**
    sprite('Action_000_09', 5)	# 222-226	 **attackbox here**
    sprite('Action_000_10', 5)	# 227-231	 **attackbox here**
    sprite('Action_000_00', 5)	# 232-236	 **attackbox here**
    gotoLabel(101)
    label(102)
    sprite('Action_248_00', 5)	# 237-241	 **attackbox here**
    SFX_1('uhi601brc')
    sprite('Action_248_01', 5)	# 242-246	 **attackbox here**
    sprite('Action_248_02', 6)	# 247-252	 **attackbox here**
    sprite('Action_248_03', 3)	# 253-255
    sprite('Action_248_04', 30)	# 256-285	 **attackbox here**
    sprite('Action_248_05', 32767)	# 286-33052	 **attackbox here**
    Unknown23018(1)
    label(110)
    sprite('Action_000_00', 5)	# 33053-33057	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_01', 5)	# 33058-33062	 **attackbox here**
    sprite('Action_000_02', 5)	# 33063-33067	 **attackbox here**
    sprite('Action_000_03', 5)	# 33068-33072	 **attackbox here**
    sprite('Action_000_04', 5)	# 33073-33077	 **attackbox here**
    sprite('Action_000_05', 5)	# 33078-33082	 **attackbox here**
    sprite('Action_000_06', 5)	# 33083-33087	 **attackbox here**
    sprite('Action_000_07', 5)	# 33088-33092	 **attackbox here**
    sprite('Action_000_08', 5)	# 33093-33097	 **attackbox here**
    sprite('Action_000_09', 5)	# 33098-33102	 **attackbox here**
    sprite('Action_000_10', 5)	# 33103-33107	 **attackbox here**
    sprite('Action_000_00', 5)	# 33108-33112	 **attackbox here**
    gotoLabel(111)
    label(112)
    sprite('Action_050_25', 5)	# 33113-33117	 **attackbox here**
    SFX_1('uhi601bny')
    sprite('Action_050_24', 5)	# 33118-33122	 **attackbox here**
    sprite('Action_050_23', 5)	# 33123-33127	 **attackbox here**
    sprite('Action_050_22', 5)	# 33128-33132	 **attackbox here**
    sprite('Action_050_21', 5)	# 33133-33137	 **attackbox here**
    sprite('Action_050_20', 5)	# 33138-33142	 **attackbox here**
    label(113)
    sprite('Action_050_09', 2)	# 33143-33144	 **attackbox here**
    sprite('Action_050_10', 5)	# 33145-33149	 **attackbox here**
    sprite('Action_050_11', 5)	# 33150-33154	 **attackbox here**
    sprite('Action_050_12', 5)	# 33155-33159	 **attackbox here**
    sprite('Action_050_13', 5)	# 33160-33164	 **attackbox here**
    sprite('Action_050_14', 5)	# 33165-33169	 **attackbox here**
    sprite('Action_050_15', 5)	# 33170-33174	 **attackbox here**
    sprite('Action_050_16', 5)	# 33175-33179	 **attackbox here**
    sprite('Action_050_17', 5)	# 33180-33184	 **attackbox here**
    sprite('Action_050_18', 5)	# 33185-33189	 **attackbox here**
    if SLOT_97:
        _gotolabel(113)
    sprite('Action_050_09', 2)	# 33190-33191	 **attackbox here**
    Unknown23018(1)
    label(114)
    sprite('Action_050_10', 5)	# 33192-33196	 **attackbox here**
    sprite('Action_050_11', 5)	# 33197-33201	 **attackbox here**
    sprite('Action_050_12', 5)	# 33202-33206	 **attackbox here**
    sprite('Action_050_13', 5)	# 33207-33211	 **attackbox here**
    sprite('Action_050_14', 5)	# 33212-33216	 **attackbox here**
    sprite('Action_050_15', 5)	# 33217-33221	 **attackbox here**
    sprite('Action_050_16', 5)	# 33222-33226	 **attackbox here**
    sprite('Action_050_17', 5)	# 33227-33231	 **attackbox here**
    sprite('Action_050_18', 5)	# 33232-33236	 **attackbox here**
    sprite('Action_050_09', 2)	# 33237-33238	 **attackbox here**
    gotoLabel(114)
    label(120)
    sprite('null', 1)	# 33239-33239
    Unknown3038(1)
    Unknown1000(-1230000)
    teleportRelativeY(675000)
    setGravity(0)
    sprite('Action_120_00', 5)	# 33240-33244	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 122)
    loopRest()
    label(121)
    sprite('Action_120_01', 5)	# 33245-33249	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 33250-33254	 **attackbox here**
    sprite('Action_120_03', 5)	# 33255-33259	 **attackbox here**
    sprite('Action_120_04', 5)	# 33260-33264	 **attackbox here**
    sprite('Action_120_05', 5)	# 33265-33269	 **attackbox here**
    sprite('Action_120_06', 5)	# 33270-33274	 **attackbox here**
    sprite('Action_120_07', 5)	# 33275-33279	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 33280-33284	 **attackbox here**
    sprite('Action_120_09', 5)	# 33285-33289	 **attackbox here**
    sprite('Action_120_10', 5)	# 33290-33294	 **attackbox here**
    sprite('Action_120_11', 5)	# 33295-33299	 **attackbox here**
    sprite('Action_120_12', 5)	# 33300-33304	 **attackbox here**
    gotoLabel(121)
    label(122)
    sprite('Action_050_02', 3)	# 33305-33307
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 33308-33310
    sprite('Action_050_04', 3)	# 33311-33313
    sprite('Action_050_05', 5)	# 33314-33318
    sprite('Action_050_06', 5)	# 33319-33323
    sprite('Action_050_07', 4)	# 33324-33327	 **attackbox here**
    SFX_1('uhi600bhz')
    sprite('Action_050_08', 4)	# 33328-33331	 **attackbox here**
    label(123)
    sprite('Action_050_09', 2)	# 33332-33333	 **attackbox here**
    sprite('Action_050_10', 5)	# 33334-33338	 **attackbox here**
    sprite('Action_050_11', 5)	# 33339-33343	 **attackbox here**
    sprite('Action_050_12', 5)	# 33344-33348	 **attackbox here**
    sprite('Action_050_13', 5)	# 33349-33353	 **attackbox here**
    sprite('Action_050_14', 5)	# 33354-33358	 **attackbox here**
    sprite('Action_050_15', 5)	# 33359-33363	 **attackbox here**
    sprite('Action_050_16', 5)	# 33364-33368	 **attackbox here**
    sprite('Action_050_17', 5)	# 33369-33373	 **attackbox here**
    sprite('Action_050_18', 5)	# 33374-33378	 **attackbox here**
    if SLOT_97:
        _gotolabel(123)
    sprite('Action_050_19', 5)	# 33379-33383	 **attackbox here**
    sprite('Action_050_20', 5)	# 33384-33388	 **attackbox here**
    sprite('Action_050_21', 5)	# 33389-33393	 **attackbox here**
    sprite('Action_050_22', 5)	# 33394-33398	 **attackbox here**
    sprite('Action_050_23', 5)	# 33399-33403	 **attackbox here**
    sprite('Action_050_24', 5)	# 33404-33408	 **attackbox here**
    sprite('Action_050_25', 5)	# 33409-33413	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(124)
    sprite('Action_000_00', 5)	# 33414-33418	 **attackbox here**
    sprite('Action_000_01', 5)	# 33419-33423	 **attackbox here**
    sprite('Action_000_02', 5)	# 33424-33428	 **attackbox here**
    sprite('Action_000_03', 5)	# 33429-33433	 **attackbox here**
    sprite('Action_000_04', 5)	# 33434-33438	 **attackbox here**
    sprite('Action_000_05', 5)	# 33439-33443	 **attackbox here**
    sprite('Action_000_06', 5)	# 33444-33448	 **attackbox here**
    sprite('Action_000_07', 5)	# 33449-33453	 **attackbox here**
    sprite('Action_000_08', 5)	# 33454-33458	 **attackbox here**
    sprite('Action_000_09', 5)	# 33459-33463	 **attackbox here**
    sprite('Action_000_10', 5)	# 33464-33468	 **attackbox here**
    gotoLabel(124)
    label(130)
    sprite('Action_248_00', 5)	# 33469-33473	 **attackbox here**
    sprite('Action_248_01', 5)	# 33474-33478	 **attackbox here**
    sprite('Action_248_02', 6)	# 33479-33484	 **attackbox here**
    sprite('Action_248_03', 3)	# 33485-33487
    sprite('Action_248_04', 30)	# 33488-33517	 **attackbox here**
    SFX_1('uhi600pce')
    label(131)
    sprite('Action_248_05', 1)	# 33518-33518	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_248_05', 30)	# 33519-33548	 **attackbox here**
    sprite('Action_248_05', 32767)	# 33549-66315	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(140)
    sprite('null', 1)	# 66316-66316
    Unknown3038(1)
    Unknown1000(-1230000)
    teleportRelativeY(675000)
    setGravity(0)
    sprite('Action_120_00', 5)	# 66317-66321	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 142)
    loopRest()
    label(141)
    sprite('Action_120_01', 5)	# 66322-66326	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 66327-66331	 **attackbox here**
    sprite('Action_120_03', 5)	# 66332-66336	 **attackbox here**
    sprite('Action_120_04', 5)	# 66337-66341	 **attackbox here**
    sprite('Action_120_05', 5)	# 66342-66346	 **attackbox here**
    sprite('Action_120_06', 5)	# 66347-66351	 **attackbox here**
    sprite('Action_120_07', 5)	# 66352-66356	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 66357-66361	 **attackbox here**
    sprite('Action_120_09', 5)	# 66362-66366	 **attackbox here**
    sprite('Action_120_10', 5)	# 66367-66371	 **attackbox here**
    sprite('Action_120_11', 5)	# 66372-66376	 **attackbox here**
    sprite('Action_120_12', 5)	# 66377-66381	 **attackbox here**
    gotoLabel(141)
    label(142)
    sprite('Action_050_02', 3)	# 66382-66384
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 66385-66387
    sprite('Action_050_04', 3)	# 66388-66390
    sprite('Action_050_05', 5)	# 66391-66395
    sprite('Action_050_06', 5)	# 66396-66400
    sprite('Action_050_07', 4)	# 66401-66404	 **attackbox here**
    SFX_1('uhi600pka')
    sprite('Action_050_08', 4)	# 66405-66408	 **attackbox here**
    label(143)
    sprite('Action_050_09', 2)	# 66409-66410	 **attackbox here**
    sprite('Action_050_10', 5)	# 66411-66415	 **attackbox here**
    sprite('Action_050_11', 5)	# 66416-66420	 **attackbox here**
    sprite('Action_050_12', 5)	# 66421-66425	 **attackbox here**
    sprite('Action_050_13', 5)	# 66426-66430	 **attackbox here**
    sprite('Action_050_14', 5)	# 66431-66435	 **attackbox here**
    sprite('Action_050_15', 5)	# 66436-66440	 **attackbox here**
    sprite('Action_050_16', 5)	# 66441-66445	 **attackbox here**
    sprite('Action_050_17', 5)	# 66446-66450	 **attackbox here**
    sprite('Action_050_18', 5)	# 66451-66455	 **attackbox here**
    if SLOT_97:
        _gotolabel(143)
    sprite('Action_050_19', 5)	# 66456-66460	 **attackbox here**
    sprite('Action_050_20', 5)	# 66461-66465	 **attackbox here**
    sprite('Action_050_21', 5)	# 66466-66470	 **attackbox here**
    sprite('Action_050_22', 5)	# 66471-66475	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    sprite('Action_050_23', 5)	# 66476-66480	 **attackbox here**
    sprite('Action_050_24', 5)	# 66481-66485	 **attackbox here**
    sprite('Action_050_25', 5)	# 66486-66490	 **attackbox here**
    label(144)
    sprite('Action_000_00', 5)	# 66491-66495	 **attackbox here**
    sprite('Action_000_01', 5)	# 66496-66500	 **attackbox here**
    sprite('Action_000_02', 5)	# 66501-66505	 **attackbox here**
    sprite('Action_000_03', 5)	# 66506-66510	 **attackbox here**
    sprite('Action_000_04', 5)	# 66511-66515	 **attackbox here**
    sprite('Action_000_05', 5)	# 66516-66520	 **attackbox here**
    sprite('Action_000_06', 5)	# 66521-66525	 **attackbox here**
    sprite('Action_000_07', 5)	# 66526-66530	 **attackbox here**
    sprite('Action_000_08', 5)	# 66531-66535	 **attackbox here**
    sprite('Action_000_09', 5)	# 66536-66540	 **attackbox here**
    sprite('Action_000_10', 5)	# 66541-66545	 **attackbox here**
    gotoLabel(144)
    label(150)
    sprite('null', 1)	# 66546-66546
    Unknown3038(1)
    teleportRelativeY(675000)
    setGravity(0)
    sprite('Action_120_00', 5)	# 66547-66551	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 152)
    loopRest()
    label(151)
    sprite('Action_120_01', 5)	# 66552-66556	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 66557-66561	 **attackbox here**
    sprite('Action_120_03', 5)	# 66562-66566	 **attackbox here**
    sprite('Action_120_04', 5)	# 66567-66571	 **attackbox here**
    sprite('Action_120_05', 5)	# 66572-66576	 **attackbox here**
    sprite('Action_120_06', 5)	# 66577-66581	 **attackbox here**
    sprite('Action_120_07', 5)	# 66582-66586	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 66587-66591	 **attackbox here**
    sprite('Action_120_09', 5)	# 66592-66596	 **attackbox here**
    sprite('Action_120_10', 5)	# 66597-66601	 **attackbox here**
    sprite('Action_120_11', 5)	# 66602-66606	 **attackbox here**
    sprite('Action_120_12', 5)	# 66607-66611	 **attackbox here**
    gotoLabel(151)
    label(152)
    sprite('Action_050_02', 3)	# 66612-66614
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 66615-66617
    sprite('Action_050_04', 3)	# 66618-66620
    sprite('Action_050_05', 5)	# 66621-66625
    sprite('Action_050_06', 5)	# 66626-66630
    sprite('Action_050_07', 4)	# 66631-66634	 **attackbox here**
    SFX_1('uhi600pmi')
    sprite('Action_050_08', 4)	# 66635-66638	 **attackbox here**
    label(153)
    sprite('Action_050_09', 2)	# 66639-66640	 **attackbox here**
    sprite('Action_050_10', 5)	# 66641-66645	 **attackbox here**
    sprite('Action_050_11', 5)	# 66646-66650	 **attackbox here**
    sprite('Action_050_12', 5)	# 66651-66655	 **attackbox here**
    sprite('Action_050_13', 5)	# 66656-66660	 **attackbox here**
    sprite('Action_050_14', 5)	# 66661-66665	 **attackbox here**
    sprite('Action_050_15', 5)	# 66666-66670	 **attackbox here**
    sprite('Action_050_16', 5)	# 66671-66675	 **attackbox here**
    sprite('Action_050_17', 5)	# 66676-66680	 **attackbox here**
    sprite('Action_050_18', 5)	# 66681-66685	 **attackbox here**
    if SLOT_97:
        _gotolabel(153)
    sprite('Action_050_19', 5)	# 66686-66690	 **attackbox here**
    sprite('Action_050_20', 5)	# 66691-66695	 **attackbox here**
    sprite('Action_050_21', 5)	# 66696-66700	 **attackbox here**
    sprite('Action_050_22', 5)	# 66701-66705	 **attackbox here**
    sprite('Action_050_23', 5)	# 66706-66710	 **attackbox here**
    sprite('Action_050_24', 5)	# 66711-66715	 **attackbox here**
    sprite('Action_050_25', 5)	# 66716-66720	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(154)
    sprite('Action_000_00', 5)	# 66721-66725	 **attackbox here**
    sprite('Action_000_01', 5)	# 66726-66730	 **attackbox here**
    sprite('Action_000_02', 5)	# 66731-66735	 **attackbox here**
    sprite('Action_000_03', 5)	# 66736-66740	 **attackbox here**
    sprite('Action_000_04', 5)	# 66741-66745	 **attackbox here**
    sprite('Action_000_05', 5)	# 66746-66750	 **attackbox here**
    sprite('Action_000_06', 5)	# 66751-66755	 **attackbox here**
    sprite('Action_000_07', 5)	# 66756-66760	 **attackbox here**
    sprite('Action_000_08', 5)	# 66761-66765	 **attackbox here**
    sprite('Action_000_09', 5)	# 66766-66770	 **attackbox here**
    sprite('Action_000_10', 5)	# 66771-66775	 **attackbox here**
    gotoLabel(154)
    label(160)
    sprite('Action_248_00', 5)	# 66776-66780	 **attackbox here**
    Unknown1000(-1465000)
    sprite('Action_248_01', 5)	# 66781-66785	 **attackbox here**
    sprite('Action_248_02', 6)	# 66786-66791	 **attackbox here**
    sprite('Action_248_03', 3)	# 66792-66794
    sprite('Action_248_04', 30)	# 66795-66824	 **attackbox here**
    SFX_1('uhi600uhy')
    label(161)
    sprite('Action_248_05', 1)	# 66825-66825	 **attackbox here**
    if SLOT_97:
        _gotolabel(161)
    sprite('Action_248_05', 60)	# 66826-66885	 **attackbox here**
    sprite('Action_248_05', 32767)	# 66886-99652	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(170)
    sprite('null', 1)	# 99653-99653
    Unknown3038(1)
    teleportRelativeY(675000)
    setGravity(0)
    sprite('Action_120_00', 5)	# 99654-99658	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 172)
    loopRest()
    label(171)
    sprite('Action_120_01', 5)	# 99659-99663	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 99664-99668	 **attackbox here**
    sprite('Action_120_03', 5)	# 99669-99673	 **attackbox here**
    sprite('Action_120_04', 5)	# 99674-99678	 **attackbox here**
    sprite('Action_120_05', 5)	# 99679-99683	 **attackbox here**
    sprite('Action_120_06', 5)	# 99684-99688	 **attackbox here**
    sprite('Action_120_07', 5)	# 99689-99693	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 99694-99698	 **attackbox here**
    sprite('Action_120_09', 5)	# 99699-99703	 **attackbox here**
    sprite('Action_120_10', 5)	# 99704-99708	 **attackbox here**
    sprite('Action_120_11', 5)	# 99709-99713	 **attackbox here**
    sprite('Action_120_12', 5)	# 99714-99718	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('Action_050_02', 3)	# 99719-99721
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 99722-99724
    sprite('Action_050_04', 3)	# 99725-99727
    sprite('Action_050_05', 5)	# 99728-99732
    sprite('Action_050_06', 5)	# 99733-99737
    sprite('Action_050_07', 4)	# 99738-99741	 **attackbox here**
    SFX_1('uhi600uli')
    sprite('Action_050_08', 4)	# 99742-99745	 **attackbox here**
    label(173)
    sprite('Action_050_09', 2)	# 99746-99747	 **attackbox here**
    sprite('Action_050_10', 5)	# 99748-99752	 **attackbox here**
    sprite('Action_050_11', 5)	# 99753-99757	 **attackbox here**
    sprite('Action_050_12', 5)	# 99758-99762	 **attackbox here**
    sprite('Action_050_13', 5)	# 99763-99767	 **attackbox here**
    sprite('Action_050_14', 5)	# 99768-99772	 **attackbox here**
    sprite('Action_050_15', 5)	# 99773-99777	 **attackbox here**
    sprite('Action_050_16', 5)	# 99778-99782	 **attackbox here**
    sprite('Action_050_17', 5)	# 99783-99787	 **attackbox here**
    sprite('Action_050_18', 5)	# 99788-99792	 **attackbox here**
    if SLOT_97:
        _gotolabel(173)
    sprite('Action_050_19', 5)	# 99793-99797	 **attackbox here**
    sprite('Action_050_20', 5)	# 99798-99802	 **attackbox here**
    sprite('Action_050_21', 5)	# 99803-99807	 **attackbox here**
    sprite('Action_050_22', 5)	# 99808-99812	 **attackbox here**
    sprite('Action_050_23', 5)	# 99813-99817	 **attackbox here**
    sprite('Action_050_24', 5)	# 99818-99822	 **attackbox here**
    sprite('Action_050_25', 5)	# 99823-99827	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(174)
    sprite('Action_000_00', 5)	# 99828-99832	 **attackbox here**
    sprite('Action_000_01', 5)	# 99833-99837	 **attackbox here**
    sprite('Action_000_02', 5)	# 99838-99842	 **attackbox here**
    sprite('Action_000_03', 5)	# 99843-99847	 **attackbox here**
    sprite('Action_000_04', 5)	# 99848-99852	 **attackbox here**
    sprite('Action_000_05', 5)	# 99853-99857	 **attackbox here**
    sprite('Action_000_06', 5)	# 99858-99862	 **attackbox here**
    sprite('Action_000_07', 5)	# 99863-99867	 **attackbox here**
    sprite('Action_000_08', 5)	# 99868-99872	 **attackbox here**
    sprite('Action_000_09', 5)	# 99873-99877	 **attackbox here**
    sprite('Action_000_10', 5)	# 99878-99882	 **attackbox here**
    gotoLabel(174)
    label(180)
    sprite('Action_000_00', 5)	# 99883-99887	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('Action_000_01', 5)	# 99888-99892	 **attackbox here**
    sprite('Action_000_02', 5)	# 99893-99897	 **attackbox here**
    sprite('Action_000_03', 5)	# 99898-99902	 **attackbox here**
    sprite('Action_000_04', 5)	# 99903-99907	 **attackbox here**
    sprite('Action_000_05', 5)	# 99908-99912	 **attackbox here**
    sprite('Action_000_06', 5)	# 99913-99917	 **attackbox here**
    sprite('Action_000_07', 5)	# 99918-99922	 **attackbox here**
    sprite('Action_000_08', 5)	# 99923-99927	 **attackbox here**
    sprite('Action_000_09', 5)	# 99928-99932	 **attackbox here**
    sprite('Action_000_10', 5)	# 99933-99937	 **attackbox here**
    sprite('Action_000_00', 5)	# 99938-99942	 **attackbox here**
    gotoLabel(181)
    label(182)
    sprite('Action_050_25', 5)	# 99943-99947	 **attackbox here**
    sprite('Action_050_24', 5)	# 99948-99952	 **attackbox here**
    sprite('Action_050_23', 5)	# 99953-99957	 **attackbox here**
    sprite('Action_050_22', 5)	# 99958-99962	 **attackbox here**
    sprite('Action_050_21', 5)	# 99963-99967	 **attackbox here**
    sprite('Action_050_20', 5)	# 99968-99972	 **attackbox here**
    SFX_1('uhi601rwi')
    label(183)
    sprite('Action_050_09', 2)	# 99973-99974	 **attackbox here**
    sprite('Action_050_10', 5)	# 99975-99979	 **attackbox here**
    sprite('Action_050_11', 5)	# 99980-99984	 **attackbox here**
    sprite('Action_050_12', 5)	# 99985-99989	 **attackbox here**
    sprite('Action_050_13', 5)	# 99990-99994	 **attackbox here**
    sprite('Action_050_14', 5)	# 99995-99999	 **attackbox here**
    sprite('Action_050_15', 5)	# 100000-100004	 **attackbox here**
    sprite('Action_050_16', 5)	# 100005-100009	 **attackbox here**
    sprite('Action_050_17', 5)	# 100010-100014	 **attackbox here**
    sprite('Action_050_18', 5)	# 100015-100019	 **attackbox here**
    if SLOT_97:
        _gotolabel(183)
    sprite('Action_050_09', 2)	# 100020-100021	 **attackbox here**
    Unknown21011(30)
    label(184)
    sprite('Action_050_10', 5)	# 100022-100026	 **attackbox here**
    sprite('Action_050_11', 5)	# 100027-100031	 **attackbox here**
    sprite('Action_050_12', 5)	# 100032-100036	 **attackbox here**
    sprite('Action_050_13', 5)	# 100037-100041	 **attackbox here**
    sprite('Action_050_14', 5)	# 100042-100046	 **attackbox here**
    sprite('Action_050_15', 5)	# 100047-100051	 **attackbox here**
    sprite('Action_050_16', 5)	# 100052-100056	 **attackbox here**
    sprite('Action_050_17', 5)	# 100057-100061	 **attackbox here**
    sprite('Action_050_18', 5)	# 100062-100066	 **attackbox here**
    sprite('Action_050_09', 2)	# 100067-100068	 **attackbox here**
    gotoLabel(184)
    label(190)
    sprite('null', 1)	# 100069-100069
    Unknown3038(1)
    Unknown1000(-1230000)
    teleportRelativeY(675000)
    setGravity(0)
    sprite('Action_120_00', 5)	# 100070-100074	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 192)
    loopRest()
    label(191)
    sprite('Action_120_01', 5)	# 100075-100079	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 100080-100084	 **attackbox here**
    sprite('Action_120_03', 5)	# 100085-100089	 **attackbox here**
    sprite('Action_120_04', 5)	# 100090-100094	 **attackbox here**
    sprite('Action_120_05', 5)	# 100095-100099	 **attackbox here**
    sprite('Action_120_06', 5)	# 100100-100104	 **attackbox here**
    sprite('Action_120_07', 5)	# 100105-100109	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 100110-100114	 **attackbox here**
    sprite('Action_120_09', 5)	# 100115-100119	 **attackbox here**
    sprite('Action_120_10', 5)	# 100120-100124	 **attackbox here**
    sprite('Action_120_11', 5)	# 100125-100129	 **attackbox here**
    sprite('Action_120_12', 5)	# 100130-100134	 **attackbox here**
    gotoLabel(191)
    label(192)
    sprite('Action_050_02', 3)	# 100135-100137
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 100138-100140
    sprite('Action_050_04', 3)	# 100141-100143
    sprite('Action_050_05', 5)	# 100144-100148
    sprite('Action_050_06', 5)	# 100149-100153
    sprite('Action_050_07', 4)	# 100154-100157	 **attackbox here**
    SFX_1('uhi600uak')
    sprite('Action_050_08', 4)	# 100158-100161	 **attackbox here**
    label(193)
    sprite('Action_050_09', 2)	# 100162-100163	 **attackbox here**
    sprite('Action_050_10', 5)	# 100164-100168	 **attackbox here**
    sprite('Action_050_11', 5)	# 100169-100173	 **attackbox here**
    sprite('Action_050_12', 5)	# 100174-100178	 **attackbox here**
    sprite('Action_050_13', 5)	# 100179-100183	 **attackbox here**
    sprite('Action_050_14', 5)	# 100184-100188	 **attackbox here**
    sprite('Action_050_15', 5)	# 100189-100193	 **attackbox here**
    sprite('Action_050_16', 5)	# 100194-100198	 **attackbox here**
    sprite('Action_050_17', 5)	# 100199-100203	 **attackbox here**
    sprite('Action_050_18', 5)	# 100204-100208	 **attackbox here**
    if SLOT_97:
        _gotolabel(193)
    sprite('Action_050_19', 5)	# 100209-100213	 **attackbox here**
    sprite('Action_050_20', 5)	# 100214-100218	 **attackbox here**
    sprite('Action_050_21', 5)	# 100219-100223	 **attackbox here**
    sprite('Action_050_22', 5)	# 100224-100228	 **attackbox here**
    sprite('Action_050_23', 5)	# 100229-100233	 **attackbox here**
    sprite('Action_050_24', 5)	# 100234-100238	 **attackbox here**
    sprite('Action_050_25', 5)	# 100239-100243	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(194)
    sprite('Action_000_00', 5)	# 100244-100248	 **attackbox here**
    sprite('Action_000_01', 5)	# 100249-100253	 **attackbox here**
    sprite('Action_000_02', 5)	# 100254-100258	 **attackbox here**
    sprite('Action_000_03', 5)	# 100259-100263	 **attackbox here**
    sprite('Action_000_04', 5)	# 100264-100268	 **attackbox here**
    sprite('Action_000_05', 5)	# 100269-100273	 **attackbox here**
    sprite('Action_000_06', 5)	# 100274-100278	 **attackbox here**
    sprite('Action_000_07', 5)	# 100279-100283	 **attackbox here**
    sprite('Action_000_08', 5)	# 100284-100288	 **attackbox here**
    sprite('Action_000_09', 5)	# 100289-100293	 **attackbox here**
    sprite('Action_000_10', 5)	# 100294-100298	 **attackbox here**
    gotoLabel(194)
    label(200)
    sprite('Action_248_00', 5)	# 100299-100303	 **attackbox here**
    sprite('Action_248_01', 5)	# 100304-100308	 **attackbox here**
    sprite('Action_248_02', 6)	# 100309-100314	 **attackbox here**
    sprite('Action_248_03', 3)	# 100315-100317
    sprite('Action_248_04', 30)	# 100318-100347	 **attackbox here**
    SFX_1('uhi600pad')
    label(201)
    sprite('Action_248_05', 1)	# 100348-100348	 **attackbox here**
    if SLOT_97:
        _gotolabel(201)
    sprite('Action_248_05', 30)	# 100349-100378	 **attackbox here**
    sprite('Action_248_05', 32767)	# 100379-133145	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(210)
    sprite('null', 1)	# 133146-133146
    Unknown3038(1)
    teleportRelativeY(600000)
    setGravity(0)

    def upon_CLEAR_OR_EXIT():
        YAccel(98)
    sprite('Action_120_00', 5)	# 133147-133151	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-13000)
    sendToLabelUpon(2, 212)
    loopRest()
    label(211)
    sprite('Action_120_01', 5)	# 133152-133156	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 133157-133161	 **attackbox here**
    sprite('Action_120_03', 5)	# 133162-133166	 **attackbox here**
    sprite('Action_120_04', 5)	# 133167-133171	 **attackbox here**
    sprite('Action_120_05', 5)	# 133172-133176	 **attackbox here**
    sprite('Action_120_06', 5)	# 133177-133181	 **attackbox here**
    sprite('Action_120_07', 5)	# 133182-133186	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 133187-133191	 **attackbox here**
    sprite('Action_120_09', 5)	# 133192-133196	 **attackbox here**
    sprite('Action_120_10', 5)	# 133197-133201	 **attackbox here**
    sprite('Action_120_11', 5)	# 133202-133206	 **attackbox here**
    sprite('Action_120_12', 5)	# 133207-133211	 **attackbox here**
    gotoLabel(211)
    label(212)
    sprite('Action_050_02', 3)	# 133212-133214
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 133215-133217
    sprite('Action_050_04', 3)	# 133218-133220
    sprite('Action_050_05', 5)	# 133221-133225
    sprite('Action_050_06', 5)	# 133226-133230
    sprite('Action_050_07', 4)	# 133231-133234	 **attackbox here**
    SFX_1('uhi600pel')
    sprite('Action_050_08', 4)	# 133235-133238	 **attackbox here**
    label(213)
    sprite('Action_050_09', 2)	# 133239-133240	 **attackbox here**
    sprite('Action_050_10', 5)	# 133241-133245	 **attackbox here**
    sprite('Action_050_11', 5)	# 133246-133250	 **attackbox here**
    sprite('Action_050_12', 5)	# 133251-133255	 **attackbox here**
    sprite('Action_050_13', 5)	# 133256-133260	 **attackbox here**
    sprite('Action_050_14', 5)	# 133261-133265	 **attackbox here**
    sprite('Action_050_15', 5)	# 133266-133270	 **attackbox here**
    sprite('Action_050_16', 5)	# 133271-133275	 **attackbox here**
    sprite('Action_050_17', 5)	# 133276-133280	 **attackbox here**
    sprite('Action_050_18', 5)	# 133281-133285	 **attackbox here**
    if SLOT_97:
        _gotolabel(213)
    sprite('Action_050_19', 5)	# 133286-133290	 **attackbox here**
    sprite('Action_050_20', 5)	# 133291-133295	 **attackbox here**
    sprite('Action_050_21', 5)	# 133296-133300	 **attackbox here**
    sprite('Action_050_22', 5)	# 133301-133305	 **attackbox here**
    sprite('Action_050_23', 5)	# 133306-133310	 **attackbox here**
    sprite('Action_050_24', 5)	# 133311-133315	 **attackbox here**
    sprite('Action_050_25', 5)	# 133316-133320	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(214)
    sprite('Action_000_00', 5)	# 133321-133325	 **attackbox here**
    sprite('Action_000_01', 5)	# 133326-133330	 **attackbox here**
    sprite('Action_000_02', 5)	# 133331-133335	 **attackbox here**
    sprite('Action_000_03', 5)	# 133336-133340	 **attackbox here**
    sprite('Action_000_04', 5)	# 133341-133345	 **attackbox here**
    sprite('Action_000_05', 5)	# 133346-133350	 **attackbox here**
    sprite('Action_000_06', 5)	# 133351-133355	 **attackbox here**
    sprite('Action_000_07', 5)	# 133356-133360	 **attackbox here**
    sprite('Action_000_08', 5)	# 133361-133365	 **attackbox here**
    sprite('Action_000_09', 5)	# 133366-133370	 **attackbox here**
    sprite('Action_000_10', 5)	# 133371-133375	 **attackbox here**
    gotoLabel(214)
    label(220)
    sprite('null', 1)	# 133376-133376
    Unknown3038(1)
    teleportRelativeY(675000)
    setGravity(0)
    sprite('Action_120_00', 5)	# 133377-133381	 **attackbox here**
    Unknown3038(0)
    physicsYImpulse(-5000)
    sendToLabelUpon(2, 222)
    loopRest()
    label(221)
    sprite('Action_120_01', 5)	# 133382-133386	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_02', 5)	# 133387-133391	 **attackbox here**
    sprite('Action_120_03', 5)	# 133392-133396	 **attackbox here**
    sprite('Action_120_04', 5)	# 133397-133401	 **attackbox here**
    sprite('Action_120_05', 5)	# 133402-133406	 **attackbox here**
    sprite('Action_120_06', 5)	# 133407-133411	 **attackbox here**
    sprite('Action_120_07', 5)	# 133412-133416	 **attackbox here**
    SFX_3('SE239_Concentration_Loop')
    sprite('Action_120_08', 5)	# 133417-133421	 **attackbox here**
    sprite('Action_120_09', 5)	# 133422-133426	 **attackbox here**
    sprite('Action_120_10', 5)	# 133427-133431	 **attackbox here**
    sprite('Action_120_11', 5)	# 133432-133436	 **attackbox here**
    sprite('Action_120_12', 5)	# 133437-133441	 **attackbox here**
    gotoLabel(221)
    label(222)
    sprite('Action_050_02', 3)	# 133442-133444
    SFX_3('SE_AppearInsulator')
    GFX_0('Entry_Back_Aura', -1)
    GFX_0('Entry_Front_Aura', -1)
    sprite('Action_050_03', 3)	# 133445-133447
    sprite('Action_050_04', 3)	# 133448-133450
    sprite('Action_050_05', 5)	# 133451-133455
    sprite('Action_050_06', 5)	# 133456-133460
    sprite('Action_050_07', 4)	# 133461-133464	 **attackbox here**
    SFX_1('uhi600rne')
    sprite('Action_050_08', 4)	# 133465-133468	 **attackbox here**
    label(223)
    sprite('Action_050_09', 2)	# 133469-133470	 **attackbox here**
    sprite('Action_050_10', 5)	# 133471-133475	 **attackbox here**
    sprite('Action_050_11', 5)	# 133476-133480	 **attackbox here**
    sprite('Action_050_12', 5)	# 133481-133485	 **attackbox here**
    sprite('Action_050_13', 5)	# 133486-133490	 **attackbox here**
    sprite('Action_050_14', 5)	# 133491-133495	 **attackbox here**
    sprite('Action_050_15', 5)	# 133496-133500	 **attackbox here**
    sprite('Action_050_16', 5)	# 133501-133505	 **attackbox here**
    sprite('Action_050_17', 5)	# 133506-133510	 **attackbox here**
    sprite('Action_050_18', 5)	# 133511-133515	 **attackbox here**
    if SLOT_97:
        _gotolabel(223)
    sprite('Action_050_19', 5)	# 133516-133520	 **attackbox here**
    sprite('Action_050_20', 5)	# 133521-133525	 **attackbox here**
    sprite('Action_050_21', 5)	# 133526-133530	 **attackbox here**
    sprite('Action_050_22', 5)	# 133531-133535	 **attackbox here**
    sprite('Action_050_23', 5)	# 133536-133540	 **attackbox here**
    sprite('Action_050_24', 5)	# 133541-133545	 **attackbox here**
    sprite('Action_050_25', 5)	# 133546-133550	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(224)
    sprite('Action_000_00', 5)	# 133551-133555	 **attackbox here**
    sprite('Action_000_01', 5)	# 133556-133560	 **attackbox here**
    sprite('Action_000_02', 5)	# 133561-133565	 **attackbox here**
    sprite('Action_000_03', 5)	# 133566-133570	 **attackbox here**
    sprite('Action_000_04', 5)	# 133571-133575	 **attackbox here**
    sprite('Action_000_05', 5)	# 133576-133580	 **attackbox here**
    sprite('Action_000_06', 5)	# 133581-133585	 **attackbox here**
    sprite('Action_000_07', 5)	# 133586-133590	 **attackbox here**
    sprite('Action_000_08', 5)	# 133591-133595	 **attackbox here**
    sprite('Action_000_09', 5)	# 133596-133600	 **attackbox here**
    sprite('Action_000_10', 5)	# 133601-133605	 **attackbox here**
    gotoLabel(224)
    label(230)
    sprite('Hil657_00', 7)	# 133606-133612	 **attackbox here**
    Unknown1000(-1350000)
    Unknown2019(-500)

    def upon_40():
        clearUponHandler(40)
        SFX_1('uhi601bph')
        Unknown23018(1)
    label(231)
    sprite('Hil657_01', 7)	# 133613-133619	 **attackbox here**
    sprite('Hil657_02', 7)	# 133620-133626	 **attackbox here**
    sprite('Hil657_03', 7)	# 133627-133633	 **attackbox here**
    sprite('Hil657_00', 7)	# 133634-133640	 **attackbox here**
    gotoLabel(231)
    label(991)
    sprite('Action_000_00', 1)	# 133641-133641	 **attackbox here**
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('Action_000_00', 5)	# 133642-133646	 **attackbox here**
    sprite('Action_000_01', 5)	# 133647-133651	 **attackbox here**
    sprite('Action_000_02', 5)	# 133652-133656	 **attackbox here**
    sprite('Action_000_03', 5)	# 133657-133661	 **attackbox here**
    sprite('Action_000_04', 5)	# 133662-133666	 **attackbox here**
    sprite('Action_000_05', 5)	# 133667-133671	 **attackbox here**
    sprite('Action_000_06', 5)	# 133672-133676	 **attackbox here**
    sprite('Action_000_07', 5)	# 133677-133681	 **attackbox here**
    sprite('Action_000_08', 5)	# 133682-133686	 **attackbox here**
    sprite('Action_000_09', 5)	# 133687-133691	 **attackbox here**
    sprite('Action_000_10', 5)	# 133692-133696	 **attackbox here**
    loopRest()
    gotoLabel(992)

@State
def CmnActMatchWin():
    if SLOT_169:
        _gotolabel(482)
    sprite('keep', 2)	# 1-2

    def upon_CLEAR_OR_EXIT():
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
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('uli'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('pad'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('pel'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('rne'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('bph'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 75)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('Action_052_00', 2)	# 4-5
    Unknown1084(1)
    sprite('Action_052_01', 4)	# 6-9
    GFX_0('Win_Effect', 100)
    sprite('Action_052_02', 3)	# 10-12
    sprite('Action_052_03', 4)	# 13-16
    sprite('Action_052_04', 5)	# 17-21
    sprite('Action_052_05', 7)	# 22-28
    if SLOT_158:
        SFX_1('uhi700def')
    sprite('Action_052_06', 4)	# 29-32
    sprite('Action_052_07', 7)	# 33-39
    sprite('Action_052_08', 3)	# 40-42
    sprite('Action_052_09', 5)	# 43-47
    sprite('Action_052_10', 2)	# 48-49
    sprite('Action_052_11', 4)	# 50-53
    sprite('Action_052_12', 2)	# 54-55
    sprite('Action_052_13', 5)	# 56-60
    sprite('Action_052_14', 2)	# 61-62
    sprite('Action_052_15', 3)	# 63-65
    sprite('Action_052_16', 3)	# 66-68
    sprite('Action_052_17', 2)	# 69-70
    sprite('Action_052_18', 5)	# 71-75
    sprite('Action_052_19', 4)	# 76-79
    sprite('Action_052_20', 3)	# 80-82
    Unknown23018(1)
    label(1)
    sprite('Action_052_21', 4)	# 83-86	 **attackbox here**
    sprite('Action_052_22', 3)	# 87-89	 **attackbox here**
    sprite('Action_052_23', 6)	# 90-95	 **attackbox here**
    sprite('Action_052_24', 2)	# 96-97	 **attackbox here**
    sprite('Action_052_25', 8)	# 98-105	 **attackbox here**
    sprite('Action_052_26', 4)	# 106-109	 **attackbox here**
    sprite('Action_052_27', 7)	# 110-116	 **attackbox here**
    sprite('Action_052_28', 2)	# 117-118	 **attackbox here**
    sprite('Action_052_29', 8)	# 119-126	 **attackbox here**
    sprite('Action_052_30', 2)	# 127-128	 **attackbox here**
    sprite('Action_052_31', 5)	# 129-133	 **attackbox here**
    sprite('Action_052_32', 1)	# 134-134	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('Action_053_00', 4)	# 135-138
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 139-141
    sprite('Action_053_02', 4)	# 142-145
    sprite('Action_053_03', 5)	# 146-150	 **attackbox here**
    if SLOT_158:
        if SLOT_52:
            Unknown7006('uhi704def', 100, 929654901, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('uhi402_0', 100, 879323253, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('uhi701def', 100, 929654901, 1701065264, 102, 0, 100, 929654901, 1701065520, 102, 0, 100, 0, 0, 0, 0, 0)
    sprite('Action_053_04', 4)	# 151-154
    sprite('Action_053_05', 3)	# 155-157	 **attackbox here**
    sprite('Action_053_06', 4)	# 158-161	 **attackbox here**
    sprite('Action_053_07', 4)	# 162-165	 **attackbox here**
    sprite('Action_053_08', 5)	# 166-170	 **attackbox here**
    sprite('Action_053_09', 5)	# 171-175	 **attackbox here**
    sprite('Action_053_10', 60)	# 176-235	 **attackbox here**
    Unknown21011(100)
    sprite('Action_053_11', 32767)	# 236-33002	 **attackbox here**
    ExitState()
    label(100)
    sprite('Action_000_00', 5)	# 33003-33007	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('Action_000_01', 5)	# 33008-33012	 **attackbox here**
    sprite('Action_000_02', 5)	# 33013-33017	 **attackbox here**
    sprite('Action_000_03', 5)	# 33018-33022	 **attackbox here**
    sprite('Action_000_04', 5)	# 33023-33027	 **attackbox here**
    sprite('Action_000_05', 5)	# 33028-33032	 **attackbox here**
    sprite('Action_000_06', 5)	# 33033-33037	 **attackbox here**
    sprite('Action_000_07', 5)	# 33038-33042	 **attackbox here**
    sprite('Action_000_08', 5)	# 33043-33047	 **attackbox here**
    sprite('Action_000_09', 5)	# 33048-33052	 **attackbox here**
    sprite('Action_000_10', 5)	# 33053-33057	 **attackbox here**
    sprite('Action_000_00', 5)	# 33058-33062	 **attackbox here**
    gotoLabel(101)
    label(102)
    sprite('Action_053_00', 4)	# 33063-33066
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 33067-33069
    sprite('Action_053_02', 4)	# 33070-33073
    sprite('Action_053_03', 5)	# 33074-33078	 **attackbox here**
    sprite('Action_053_04', 4)	# 33079-33082
    SFX_1('uhi701brc')
    sprite('Action_053_05', 3)	# 33083-33085	 **attackbox here**
    sprite('Action_053_06', 4)	# 33086-33089	 **attackbox here**
    sprite('Action_053_07', 4)	# 33090-33093	 **attackbox here**
    sprite('Action_053_08', 5)	# 33094-33098	 **attackbox here**
    sprite('Action_053_09', 5)	# 33099-33103	 **attackbox here**
    sprite('Action_053_10', 60)	# 33104-33163	 **attackbox here**
    sprite('Action_053_11', 32767)	# 33164-65930	 **attackbox here**
    Unknown23018(1)
    label(110)
    sprite('Action_000_00', 5)	# 65931-65935	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('Action_000_01', 5)	# 65936-65940	 **attackbox here**
    sprite('Action_000_02', 5)	# 65941-65945	 **attackbox here**
    sprite('Action_000_03', 5)	# 65946-65950	 **attackbox here**
    sprite('Action_000_04', 5)	# 65951-65955	 **attackbox here**
    sprite('Action_000_05', 5)	# 65956-65960	 **attackbox here**
    sprite('Action_000_06', 5)	# 65961-65965	 **attackbox here**
    sprite('Action_000_07', 5)	# 65966-65970	 **attackbox here**
    sprite('Action_000_08', 5)	# 65971-65975	 **attackbox here**
    sprite('Action_000_09', 5)	# 65976-65980	 **attackbox here**
    sprite('Action_000_10', 5)	# 65981-65985	 **attackbox here**
    sprite('Action_000_00', 5)	# 65986-65990	 **attackbox here**
    gotoLabel(111)
    label(112)
    sprite('Action_053_00', 4)	# 65991-65994
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 65995-65997
    sprite('Action_053_02', 4)	# 65998-66001
    sprite('Action_053_03', 5)	# 66002-66006	 **attackbox here**
    sprite('Action_053_04', 4)	# 66007-66010
    SFX_1('uhi701bny')
    sprite('Action_053_05', 3)	# 66011-66013	 **attackbox here**
    sprite('Action_053_06', 4)	# 66014-66017	 **attackbox here**
    sprite('Action_053_07', 4)	# 66018-66021	 **attackbox here**
    sprite('Action_053_08', 5)	# 66022-66026	 **attackbox here**
    sprite('Action_053_09', 5)	# 66027-66031	 **attackbox here**
    sprite('Action_053_10', 60)	# 66032-66091	 **attackbox here**
    sprite('Action_053_11', 32767)	# 66092-98858	 **attackbox here**
    Unknown23018(1)
    label(120)
    sprite('Action_053_00', 4)	# 98859-98862
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 98863-98865
    sprite('Action_053_02', 4)	# 98866-98869
    sprite('Action_053_03', 5)	# 98870-98874	 **attackbox here**
    sprite('Action_053_04', 4)	# 98875-98878
    SFX_1('uhi700bhz')
    sprite('Action_053_05', 3)	# 98879-98881	 **attackbox here**
    sprite('Action_053_06', 4)	# 98882-98885	 **attackbox here**
    sprite('Action_053_07', 4)	# 98886-98889	 **attackbox here**
    sprite('Action_053_08', 5)	# 98890-98894	 **attackbox here**
    sprite('Action_053_09', 5)	# 98895-98899	 **attackbox here**
    sprite('Action_053_10', 60)	# 98900-98959	 **attackbox here**
    label(121)
    sprite('Action_053_11', 1)	# 98960-98960	 **attackbox here**
    if SLOT_97:
        _gotolabel(121)
    sprite('Action_053_11', 30)	# 98961-98990	 **attackbox here**
    sprite('Action_053_11', 32767)	# 98991-131757	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(210)
    label(130)
    sprite('Action_248_00', 5)	# 131758-131762	 **attackbox here**
    sprite('Action_248_01', 5)	# 131763-131767	 **attackbox here**
    sprite('Action_248_02', 6)	# 131768-131773	 **attackbox here**
    sprite('Action_248_03', 3)	# 131774-131776
    sprite('Action_248_04', 30)	# 131777-131806	 **attackbox here**
    SFX_1('uhi700pce')
    label(131)
    sprite('Action_248_05', 1)	# 131807-131807	 **attackbox here**
    if SLOT_97:
        _gotolabel(131)
    sprite('Action_248_05', 30)	# 131808-131837	 **attackbox here**
    sprite('Action_248_05', 32767)	# 131838-164604	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(150)
    label(140)
    sprite('Action_052_00', 2)	# 164605-164606
    Unknown1084(1)
    sprite('Action_052_01', 4)	# 164607-164610
    sprite('Action_052_02', 3)	# 164611-164613
    sprite('Action_052_03', 4)	# 164614-164617
    sprite('Action_052_04', 5)	# 164618-164622
    sprite('Action_052_05', 7)	# 164623-164629
    SFX_1('uhi700pka')
    sprite('Action_052_06', 4)	# 164630-164633
    sprite('Action_052_07', 7)	# 164634-164640
    sprite('Action_052_08', 3)	# 164641-164643
    sprite('Action_052_09', 5)	# 164644-164648
    sprite('Action_052_10', 2)	# 164649-164650
    sprite('Action_052_11', 4)	# 164651-164654
    sprite('Action_052_12', 2)	# 164655-164656
    sprite('Action_052_13', 5)	# 164657-164661
    sprite('Action_052_14', 2)	# 164662-164663
    sprite('Action_052_15', 3)	# 164664-164666
    sprite('Action_052_16', 3)	# 164667-164669
    sprite('Action_052_17', 2)	# 164670-164671
    sprite('Action_052_18', 5)	# 164672-164676
    sprite('Action_052_19', 4)	# 164677-164680
    sprite('Action_052_20', 3)	# 164681-164683
    label(141)
    sprite('Action_052_21', 4)	# 164684-164687	 **attackbox here**
    sprite('Action_052_22', 3)	# 164688-164690	 **attackbox here**
    sprite('Action_052_23', 6)	# 164691-164696	 **attackbox here**
    sprite('Action_052_24', 2)	# 164697-164698	 **attackbox here**
    sprite('Action_052_25', 8)	# 164699-164706	 **attackbox here**
    sprite('Action_052_26', 4)	# 164707-164710	 **attackbox here**
    sprite('Action_052_27', 7)	# 164711-164717	 **attackbox here**
    sprite('Action_052_28', 2)	# 164718-164719	 **attackbox here**
    sprite('Action_052_29', 8)	# 164720-164727	 **attackbox here**
    sprite('Action_052_30', 2)	# 164728-164729	 **attackbox here**
    sprite('Action_052_31', 5)	# 164730-164734	 **attackbox here**
    sprite('Action_052_32', 1)	# 164735-164735	 **attackbox here**
    if SLOT_97:
        _gotolabel(141)
    sprite('Action_052_21', 4)	# 164736-164739	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(180)
    label(142)
    sprite('Action_052_22', 3)	# 164740-164742	 **attackbox here**
    sprite('Action_052_23', 6)	# 164743-164748	 **attackbox here**
    sprite('Action_052_24', 2)	# 164749-164750	 **attackbox here**
    sprite('Action_052_25', 8)	# 164751-164758	 **attackbox here**
    sprite('Action_052_26', 4)	# 164759-164762	 **attackbox here**
    sprite('Action_052_27', 7)	# 164763-164769	 **attackbox here**
    sprite('Action_052_28', 2)	# 164770-164771	 **attackbox here**
    sprite('Action_052_29', 8)	# 164772-164779	 **attackbox here**
    sprite('Action_052_30', 2)	# 164780-164781	 **attackbox here**
    sprite('Action_052_31', 5)	# 164782-164786	 **attackbox here**
    sprite('Action_052_32', 1)	# 164787-164787	 **attackbox here**
    sprite('Action_052_21', 4)	# 164788-164791	 **attackbox here**
    gotoLabel(142)
    label(150)
    sprite('Action_053_00', 4)	# 164792-164795
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 164796-164798
    sprite('Action_053_02', 4)	# 164799-164802
    sprite('Action_053_03', 5)	# 164803-164807	 **attackbox here**
    sprite('Action_053_04', 4)	# 164808-164811
    SFX_1('uhi700pmi')
    sprite('Action_053_05', 3)	# 164812-164814	 **attackbox here**
    sprite('Action_053_06', 4)	# 164815-164818	 **attackbox here**
    sprite('Action_053_07', 4)	# 164819-164822	 **attackbox here**
    sprite('Action_053_08', 5)	# 164823-164827	 **attackbox here**
    sprite('Action_053_09', 5)	# 164828-164832	 **attackbox here**
    sprite('Action_053_10', 60)	# 164833-164892	 **attackbox here**
    label(151)
    sprite('Action_053_11', 1)	# 164893-164893	 **attackbox here**
    if SLOT_97:
        _gotolabel(151)
    sprite('Action_053_11', 30)	# 164894-164923	 **attackbox here**
    sprite('Action_053_11', 32767)	# 164924-197690	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(160)
    label(160)
    sprite('Action_053_00', 4)	# 197691-197694
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 197695-197697
    sprite('Action_053_02', 4)	# 197698-197701
    sprite('Action_053_03', 5)	# 197702-197706	 **attackbox here**
    sprite('Action_053_04', 4)	# 197707-197710
    SFX_1('uhi700uhy')
    sprite('Action_053_05', 3)	# 197711-197713	 **attackbox here**
    sprite('Action_053_06', 4)	# 197714-197717	 **attackbox here**
    sprite('Action_053_07', 4)	# 197718-197721	 **attackbox here**
    sprite('Action_053_08', 5)	# 197722-197726	 **attackbox here**
    sprite('Action_053_09', 5)	# 197727-197731	 **attackbox here**
    sprite('Action_053_10', 60)	# 197732-197791	 **attackbox here**
    label(161)
    sprite('Action_053_11', 1)	# 197792-197792	 **attackbox here**
    if SLOT_97:
        _gotolabel(161)
    sprite('Action_053_11', 32767)	# 197793-230559	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(120)
    label(170)
    sprite('Action_000_00', 5)	# 230560-230564	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('Action_000_01', 5)	# 230565-230569	 **attackbox here**
    sprite('Action_000_02', 5)	# 230570-230574	 **attackbox here**
    sprite('Action_000_03', 5)	# 230575-230579	 **attackbox here**
    sprite('Action_000_04', 5)	# 230580-230584	 **attackbox here**
    sprite('Action_000_05', 5)	# 230585-230589	 **attackbox here**
    sprite('Action_000_06', 5)	# 230590-230594	 **attackbox here**
    sprite('Action_000_07', 5)	# 230595-230599	 **attackbox here**
    sprite('Action_000_08', 5)	# 230600-230604	 **attackbox here**
    sprite('Action_000_09', 5)	# 230605-230609	 **attackbox here**
    sprite('Action_000_10', 5)	# 230610-230614	 **attackbox here**
    sprite('Action_000_00', 5)	# 230615-230619	 **attackbox here**
    gotoLabel(171)
    label(172)
    sprite('keep', 1)	# 230620-230620
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(175)
        elif (SLOT_38 == 1):
            sendToLabel(175)
    label(173)
    sprite('Action_248_00', 5)	# 230621-230625	 **attackbox here**
    SFX_1('uhi701uli')
    sprite('Action_248_01', 5)	# 230626-230630	 **attackbox here**
    sprite('Action_248_02', 6)	# 230631-230636	 **attackbox here**
    sprite('Action_248_03', 3)	# 230637-230639
    sprite('Action_248_04', 30)	# 230640-230669	 **attackbox here**
    label(174)
    sprite('Action_248_05', 1)	# 230670-230670	 **attackbox here**
    if SLOT_97:
        _gotolabel(174)
    sprite('Action_248_05', 32767)	# 230671-263437	 **attackbox here**
    Unknown21011(30)
    label(175)
    sprite('Action_015_00', 5)	# 263438-263442
    Unknown2005()
    sprite('Action_015_01', 5)	# 263443-263447
    gotoLabel(173)
    label(180)
    sprite('Action_053_00', 4)	# 263448-263451
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 263452-263454
    sprite('Action_053_02', 4)	# 263455-263458
    sprite('Action_053_03', 5)	# 263459-263463	 **attackbox here**
    sprite('Action_053_04', 4)	# 263464-263467
    SFX_1('uhi700rwi')
    sprite('Action_053_05', 3)	# 263468-263470	 **attackbox here**
    sprite('Action_053_06', 4)	# 263471-263474	 **attackbox here**
    sprite('Action_053_07', 4)	# 263475-263478	 **attackbox here**
    sprite('Action_053_08', 5)	# 263479-263483	 **attackbox here**
    sprite('Action_053_09', 5)	# 263484-263488	 **attackbox here**
    sprite('Action_053_10', 60)	# 263489-263548	 **attackbox here**
    label(181)
    sprite('Action_053_11', 1)	# 263549-263549	 **attackbox here**
    if SLOT_97:
        _gotolabel(181)
    sprite('Action_053_11', 32767)	# 263550-296316	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(170)
    label(190)
    sprite('Action_053_00', 4)	# 296317-296320
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 296321-296323
    sprite('Action_053_02', 4)	# 296324-296327
    sprite('Action_053_03', 5)	# 296328-296332	 **attackbox here**
    sprite('Action_053_04', 4)	# 296333-296336
    sprite('Action_053_05', 3)	# 296337-296339	 **attackbox here**
    sprite('Action_053_06', 4)	# 296340-296343	 **attackbox here**
    sprite('Action_053_07', 4)	# 296344-296347	 **attackbox here**
    sprite('Action_053_08', 5)	# 296348-296352	 **attackbox here**
    sprite('Action_053_09', 5)	# 296353-296357	 **attackbox here**
    sprite('Action_053_10', 60)	# 296358-296417	 **attackbox here**
    SFX_1('uhi700uak')
    label(191)
    sprite('Action_053_11', 1)	# 296418-296418	 **attackbox here**
    if SLOT_97:
        _gotolabel(191)
    sprite('Action_053_11', 30)	# 296419-296448	 **attackbox here**
    sprite('Action_053_11', 32767)	# 296449-329215	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(210)
    label(200)
    sprite('Action_000_00', 5)	# 329216-329220	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('Action_000_01', 5)	# 329221-329225	 **attackbox here**
    sprite('Action_000_02', 5)	# 329226-329230	 **attackbox here**
    sprite('Action_000_03', 5)	# 329231-329235	 **attackbox here**
    sprite('Action_000_04', 5)	# 329236-329240	 **attackbox here**
    sprite('Action_000_05', 5)	# 329241-329245	 **attackbox here**
    sprite('Action_000_06', 5)	# 329246-329250	 **attackbox here**
    sprite('Action_000_07', 5)	# 329251-329255	 **attackbox here**
    sprite('Action_000_08', 5)	# 329256-329260	 **attackbox here**
    sprite('Action_000_09', 5)	# 329261-329265	 **attackbox here**
    sprite('Action_000_10', 5)	# 329266-329270	 **attackbox here**
    sprite('Action_000_00', 5)	# 329271-329275	 **attackbox here**
    gotoLabel(201)
    label(202)
    sprite('Action_053_00', 4)	# 329276-329279
    sprite('Action_053_01', 3)	# 329280-329282
    sprite('Action_053_02', 4)	# 329283-329286
    sprite('Action_053_03', 5)	# 329287-329291	 **attackbox here**
    sprite('Action_053_04', 4)	# 329292-329295
    SFX_1('uhi701pad')
    sprite('Action_053_05', 3)	# 329296-329298	 **attackbox here**
    sprite('Action_053_06', 4)	# 329299-329302	 **attackbox here**
    sprite('Action_053_07', 4)	# 329303-329306	 **attackbox here**
    sprite('Action_053_08', 5)	# 329307-329311	 **attackbox here**
    sprite('Action_053_09', 5)	# 329312-329316	 **attackbox here**
    sprite('Action_053_10', 60)	# 329317-329376	 **attackbox here**
    sprite('Action_053_11', 32767)	# 329377-362143	 **attackbox here**
    Unknown23018(1)
    label(210)
    sprite('Action_053_00', 4)	# 362144-362147
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 362148-362150
    sprite('Action_053_02', 4)	# 362151-362154
    sprite('Action_053_03', 5)	# 362155-362159	 **attackbox here**
    sprite('Action_053_04', 4)	# 362160-362163
    sprite('Action_053_05', 3)	# 362164-362166	 **attackbox here**
    sprite('Action_053_06', 4)	# 362167-362170	 **attackbox here**
    sprite('Action_053_07', 4)	# 362171-362174	 **attackbox here**
    sprite('Action_053_08', 5)	# 362175-362179	 **attackbox here**
    sprite('Action_053_09', 5)	# 362180-362184	 **attackbox here**
    sprite('Action_053_10', 60)	# 362185-362244	 **attackbox here**
    SFX_1('uhi700pel')
    label(211)
    sprite('Action_053_11', 1)	# 362245-362245	 **attackbox here**
    if SLOT_97:
        _gotolabel(211)
    sprite('Action_053_11', 30)	# 362246-362275	 **attackbox here**
    sprite('Action_053_11', 32767)	# 362276-395042	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(180)
    label(220)
    sprite('Action_000_00', 5)	# 395043-395047	 **attackbox here**

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('Action_000_01', 5)	# 395048-395052	 **attackbox here**
    sprite('Action_000_02', 5)	# 395053-395057	 **attackbox here**
    sprite('Action_000_03', 5)	# 395058-395062	 **attackbox here**
    sprite('Action_000_04', 5)	# 395063-395067	 **attackbox here**
    sprite('Action_000_05', 5)	# 395068-395072	 **attackbox here**
    sprite('Action_000_06', 5)	# 395073-395077	 **attackbox here**
    sprite('Action_000_07', 5)	# 395078-395082	 **attackbox here**
    sprite('Action_000_08', 5)	# 395083-395087	 **attackbox here**
    sprite('Action_000_09', 5)	# 395088-395092	 **attackbox here**
    sprite('Action_000_10', 5)	# 395093-395097	 **attackbox here**
    sprite('Action_000_00', 5)	# 395098-395102	 **attackbox here**
    gotoLabel(221)
    label(222)
    sprite('Action_053_00', 4)	# 395103-395106
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 395107-395109
    sprite('Action_053_02', 4)	# 395110-395113
    sprite('Action_053_03', 5)	# 395114-395118	 **attackbox here**
    sprite('Action_053_04', 4)	# 395119-395122
    SFX_1('uhi701rne')
    sprite('Action_053_05', 3)	# 395123-395125	 **attackbox here**
    sprite('Action_053_06', 4)	# 395126-395129	 **attackbox here**
    sprite('Action_053_07', 4)	# 395130-395133	 **attackbox here**
    sprite('Action_053_08', 5)	# 395134-395138	 **attackbox here**
    sprite('Action_053_09', 5)	# 395139-395143	 **attackbox here**
    sprite('Action_053_10', 60)	# 395144-395203	 **attackbox here**
    sprite('Action_053_11', 32767)	# 395204-427970	 **attackbox here**
    Unknown23018(1)
    label(230)
    sprite('Action_053_00', 4)	# 427971-427974
    Unknown1084(1)
    sprite('Action_053_01', 3)	# 427975-427977
    sprite('Action_053_02', 4)	# 427978-427981
    sprite('Action_053_03', 5)	# 427982-427986	 **attackbox here**
    sprite('Action_053_04', 4)	# 427987-427990
    sprite('Action_053_05', 3)	# 427991-427993	 **attackbox here**
    sprite('Action_053_06', 4)	# 427994-427997	 **attackbox here**
    sprite('Action_053_07', 4)	# 427998-428001	 **attackbox here**
    sprite('Action_053_08', 5)	# 428002-428006	 **attackbox here**
    sprite('Action_053_09', 5)	# 428007-428011	 **attackbox here**
    sprite('Action_053_10', 60)	# 428012-428071	 **attackbox here**
    SFX_1('uhi700bph')
    label(231)
    sprite('Action_053_11', 1)	# 428072-428072	 **attackbox here**
    if SLOT_97:
        _gotolabel(231)
    sprite('Action_053_11', 30)	# 428073-428102	 **attackbox here**
    sprite('Action_053_11', 32767)	# 428103-460869	 **attackbox here**
    Unknown21007(24, 40)
    Unknown21011(200)

@State
def CmnActLose():
    sprite('Action_248_00', 5)	# 1-5	 **attackbox here**
    if SLOT_158:
        Unknown7006('uhi403_0', 100, 879323253, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('Action_248_01', 5)	# 6-10	 **attackbox here**
    sprite('Action_248_02', 6)	# 11-16	 **attackbox here**
    sprite('Action_248_03', 3)	# 17-19
    sprite('Action_248_04', 30)	# 20-49	 **attackbox here**
    sprite('Action_248_05', 32767)	# 50-32816	 **attackbox here**
    Unknown23018(1)