@Subroutine
def ItemIconUpDate():
    if (SLOT_5 == 1):
        Unknown23006(0, 18)
    if (SLOT_5 == 2):
        Unknown23006(0, 19)
    if (SLOT_5 == 3):
        Unknown23006(0, 20)
    if (SLOT_5 == 4):
        Unknown23006(0, 27)
    if (SLOT_5 == 5):
        Unknown23006(0, 22)
    if (SLOT_5 == 6):
        Unknown23006(0, 23)
    if (SLOT_5 == 7):
        Unknown23006(0, 24)
    if (SLOT_5 == 8):
        Unknown23006(0, 25)
    if (SLOT_5 == 9):
        Unknown23006(0, 26)
    if (SLOT_5 == 10):
        Unknown23006(0, 21)
    if (SLOT_5 == 11):
        Unknown23006(0, 28)
    if (SLOT_5 == 12):
        Unknown23006(0, 29)
    if (SLOT_5 >= 13):
        Unknown23006(0, 30)

@Subroutine
def PreInit():
    Unknown12019('706b7500000000000000000000000000')

@Subroutine
def MatchInit():
    DashFInitialVelocity(15000)
    DashFAccel(352)
    DashFMaxVelocity(22400)
    Unknown12011(1500)
    Unknown12038(27000)
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
    MoveMaxChainRepeat(3)
    Unknown14015(0, 350000, -200000, 250000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A2nd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15015(24, 26)
    Unknown14015(0, 400000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A3rd', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown15015(33, 35)
    Unknown14015(0, 500000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5A4th', 0x7)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 330000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown14015(0, 200000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown15013(250)
    Unknown14015(0, 700000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B2nd', 0x19)
    Move_AirGround_(0x3083)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 700000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B3rd', 0x19)
    Move_AirGround_(0x3083)
    MoveMaxChainRepeat(1)
    Unknown14005(1)
    Unknown14015(0, 700000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15021(4000)
    Unknown14015(0, 350000, 150000, 400000, 500, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(20000, 350000, -219000, -66000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(500)
    Unknown14015(0, 450000, -100000, 250000, 750, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(2000)
    Unknown14015(0, 450000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A2nd', 0x10)
    Unknown14005(1)
    Unknown15013(2000)
    Unknown14015(0, 450000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Unknown15013(250)
    Unknown14015(0, 550000, -300000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15008()
    Unknown15021(150)
    Unknown14015(0, 300000, -800000, 150000, 1500, 50)
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
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(4000)
    Unknown14015(-50000, 400000, -200000, 250000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(4000)
    Unknown14015(-50000, 400000, -200000, 250000, 250, 0)
    Move_EndRegister()
    Move_Register('ScrewDriverA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 150, 10)
    Move_EndRegister()
    Move_Register('ScrewDriverB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 150, 10)
    Move_EndRegister()
    Move_Register('ScrewDriverEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 100, 5)
    Move_EndRegister()
    Move_Register('AirScrewDriverA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 150, 10)
    Move_EndRegister()
    Move_Register('AirScrewDriverB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 150, 10)
    Move_EndRegister()
    Move_Register('AirScrewDriverEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown15013(500)
    Unknown14015(0, 700000, -200000, 250000, 100, 5)
    Move_EndRegister()
    Move_Register('TripleTVA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(0xe2)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(0, 700000, -200000, 250000, 1, 30)
    Move_EndRegister()
    Move_Register('TripleTVB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(0xe2)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown14015(0, 700000, -200000, 250000, 1, 30)
    Move_EndRegister()
    Move_Register('TripleTVEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(0xe2)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown14015(0, 700000, -200000, 250000, 1, 30)
    Move_EndRegister()
    Move_Register('ItemShootA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(350000, 700000, -200000, 250000, 100, 30)
    Move_EndRegister()
    Move_Register('ItemShootB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown14015(350000, 700000, -200000, 250000, 100, 30)
    Move_EndRegister()
    Move_Register('ItemShootEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown14015(350000, 700000, -200000, 250000, 100, 30)
    Move_EndRegister()
    Move_Register('AirItemShootA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300d)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown14015(350000, 700000, -200000, 250000, 100, 30)
    Move_EndRegister()
    Move_Register('AirItemShootB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300d)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown14015(350000, 700000, -200000, 250000, 100, 30)
    Move_EndRegister()
    Move_Register('AirItemShootEx', INPUT_SPECIALMOVE)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300d)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15014(1)
    Unknown14015(350000, 700000, -200000, 250000, 100, 30)
    Move_EndRegister()
    Move_Register('UltimateMissile', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3089)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(4000)
    Unknown15020(600, 1000, 10, 1000)
    Unknown14015(600000, 900000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateMissileOD', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x3089)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(4000)
    Unknown15020(600, 1000, 10, 1000)
    Unknown14015(600000, 900000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('AirUltimateMissile', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3089)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(500000, 1500000, 50000, -400000, 50, 0)
    Move_EndRegister()
    Move_Register('AirUltimateMissileOD', 0x68)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(500000, 1500000, 50000, -400000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateNihil', 0x68)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3089)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(0, 400000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateNihilOD', 0x68)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Move_AirGround_(0x3081)
    Move_AirGround_(0x3089)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown15020(600, 1000, 1, 1000)
    Unknown14015(0, 400000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x304a)
    Move_AirGround_(0x2000)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15005(10)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(200000, 300000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5A2nd', 10000000)
    Unknown15024('NmlAtk5A2nd', 'NmlAtk5A3rd', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk5A4th', 10000000)
    Unknown15024('NmlAtk5A3rd', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2B', 'FHighJump', 10000000)
    Unknown15024('NmlAtk2C', 'ScrewDriverA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5B2nd', 10000000)
    Unknown15024('NmlAtk5B2nd', 'NmlAtk5B3rd', 10000000)
    Unknown15024('NmlAtk5B3rd', 'ItemShootB', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5A2nd', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'AirScrewDriverA', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'AirUltimateMissile', 10000000)
    Unknown15024('NmlAtkAIR5A2nd', 'AirUltimateMissileOD', 10000000)
    Unknown7010(0, 'pku000')
    Unknown7010(1, 'pku001')
    Unknown7010(2, 'pku002')
    Unknown7010(3, 'pku003')
    Unknown7010(4, 'pku004')
    Unknown7010(5, 'pku005')
    Unknown7010(6, 'pku006')
    Unknown7010(7, 'pku007')
    Unknown7010(8, 'pku008')
    Unknown7010(9, 'pku009')
    Unknown7010(10, 'pku010')
    Unknown7010(15, 'pku015')
    Unknown7010(16, 'pku016')
    Unknown7010(17, 'pku017')
    Unknown7010(18, 'pku018')
    Unknown7010(19, 'pku019')
    Unknown7010(20, 'pku020')
    Unknown7010(21, 'pku021')
    Unknown7010(22, 'pku022')
    Unknown7010(23, 'pku023')
    Unknown7010(24, 'pku024')
    Unknown7010(25, 'pku025')
    Unknown7010(28, 'pku028')
    Unknown7010(29, 'pku029')
    Unknown7010(30, 'pku030')
    Unknown7010(31, 'pku031')
    Unknown7010(32, 'pku032')
    Unknown7010(33, 'pku033')
    Unknown7010(34, 'pku034')
    Unknown7010(35, 'pku035')
    Unknown7010(36, 'pku036')
    Unknown7010(37, 'pku037')
    Unknown7010(39, 'pku039')
    Unknown7010(42, 'pku042')
    Unknown7010(43, 'pku043')
    Unknown7010(44, 'pku044')
    Unknown7010(45, 'pku045')
    Unknown7010(46, 'pku046')
    Unknown7010(47, 'pku047')
    Unknown7010(48, 'pku048')
    Unknown7010(49, 'pku049')
    Unknown7010(50, 'pku050')
    Unknown7010(52, 'pku052')
    Unknown7010(53, 'pku053')
    Unknown7010(54, 'pku100_0')
    Unknown7010(55, 'pku100_1')
    Unknown7010(56, 'pku100_2')
    Unknown7010(63, 'pku101_0')
    Unknown7010(64, 'pku101_1')
    Unknown7010(65, 'pku101_2')
    Unknown7010(57, 'pku102_0')
    Unknown7010(58, 'pku102_1')
    Unknown7010(66, 'pku103_0')
    Unknown7010(67, 'pku103_1')
    Unknown7010(60, 'pku104_0')
    Unknown7010(61, 'pku104_1')
    Unknown7010(69, 'pku105_0')
    Unknown7010(70, 'pku105_1')
    Unknown7010(72, 'pku150')
    Unknown7010(73, 'pku151')
    Unknown7010(74, 'pku152')
    Unknown7010(85, 'pku153')
    Unknown7010(87, 'pku164')
    Unknown7010(88, 'pku155')
    Unknown7010(96, 'pku161_0')
    Unknown7010(97, 'pku161_1')
    Unknown7010(92, 'pku162_0')
    Unknown7010(93, 'pku162_1')
    Unknown7010(98, 'pku163_0')
    Unknown7010(99, 'pku163_1')
    Unknown7010(100, 'pku164_0')
    Unknown7010(101, 'pku164_1')
    Unknown7010(105, 'pku165_0')
    Unknown7010(106, 'pku165_1')
    Unknown7010(102, 'pku166_0')
    Unknown7010(103, 'pku166_1')
    Unknown7010(90, 'pku167_0')
    Unknown7010(91, 'pku167_1')
    Unknown7010(107, 'pku168_0')
    Unknown7010(108, 'pku168_1')
    Unknown7010(110, 'pku169_0')
    Unknown7010(111, 'pku169_1')
    Unknown7010(94, 'pku401_0')
    Unknown7010(95, 'pku401_1')
    Unknown12018(0, 'ku060_00')
    Unknown12018(1, 'ku060_01')
    Unknown12018(2, 'ku060_02')
    Unknown12018(3, 'ku060_03')
    Unknown12018(4, 'ku060_04')
    Unknown12018(5, 'ku060_05')
    Unknown12018(6, 'ku060_06')
    Unknown12018(7, 'ku040_02')
    Unknown12018(8, 'ku040_02')
    Unknown12018(9, 'ku045_02')
    Unknown12018(10, 'ku060_00')
    Unknown12018(11, 'ku060_01')
    Unknown12018(12, 'ku060_03')
    Unknown12018(13, 'ku060_05')
    Unknown12018(14, 'ku060_07')
    Unknown12018(15, 'ku125_00')
    Unknown12018(16, 'ku050_00')
    Unknown12018(17, 'ku052_00')
    Unknown12018(18, 'ku054_00')
    Unknown12018(19, 'ku000_00')
    Unknown12018(20, 'ku000_00')
    Unknown12018(25, 'ku063_00')
    Unknown12018(26, 'ku063_02')
    Unknown12018(27, 'ku063_03')
    Unknown12018(28, 'ku060_07')
    Unknown12018(29, 'ku060_12')
    Unknown12018(24, 'ku072_03')
    Unknown30036('504b555f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654d697373696c650000000000000000000000000000000000')
    Unknown12059('03000000556c74696d6174654d697373696c654f44000000000000000000000000000000')
    Unknown12059('04000000556c74696d6174654e6968696c00000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d6174654e6968696c4f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MatchInit2():
    SLOT_5 = 1
    if SLOT_91:
        Unknown58('TRI_PKUItemStart', 2, 67)
        if (SLOT_67 > 0):
            SLOT_5 = SLOT_67
    Unknown23003(0, 1, 18, 1, 1, 0, -1, -1)
    Unknown23044(0, 1)
    callSubroutine('ItemIconUpDate')

@Subroutine
def OnFrameStep():
    if SLOT_170:
        Unknown23008(0, 0)
    else:
        Unknown23008(0, 1)

    @Subroutine
    def OnFrameStep():
        if SLOT_37:
            SLOT_9 = 0

@State
def CmnActStand():
    label(0)
    sprite('ku000_00', 6)	# 1-6
    sprite('ku000_01', 6)	# 7-12
    sprite('ku000_02', 6)	# 13-18
    sprite('ku000_03', 6)	# 19-24
    sprite('ku000_04', 6)	# 25-30
    sprite('ku000_05', 6)	# 31-36
    sprite('ku000_00', 6)	# 37-42
    sprite('ku000_07', 6)	# 43-48
    sprite('ku000_08', 6)	# 49-54
    sprite('ku000_09', 6)	# 55-60
    sprite('ku000_10', 6)	# 61-66
    sprite('ku000_11', 6)	# 67-72
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('ku001_00', 6)	# 73-78
    SLOT_88 = 960
    SFX_1('pku000')
    sprite('ku001_01', 6)	# 79-84
    sprite('ku001_02', 6)	# 85-90
    sprite('ku001_03', 8)	# 91-98
    sprite('ku001_04', 6)	# 99-104
    sprite('ku001_05', 6)	# 105-110
    sprite('ku001_01', 6)	# 111-116
    sprite('ku001_02', 6)	# 117-122
    sprite('ku001_03', 8)	# 123-130
    sprite('ku001_04', 6)	# 131-136
    sprite('ku001_05', 6)	# 137-142
    sprite('ku001_01', 6)	# 143-148
    sprite('ku001_02', 6)	# 149-154
    sprite('ku001_03', 8)	# 155-162
    sprite('ku001_04', 6)	# 163-168
    sprite('ku001_05', 6)	# 169-174
    sprite('ku001_01', 6)	# 175-180
    sprite('ku001_02', 6)	# 181-186
    sprite('ku001_03', 8)	# 187-194
    sprite('ku001_04', 6)	# 195-200
    sprite('ku001_05', 6)	# 201-206
    sprite('ku001_01', 6)	# 207-212
    sprite('ku001_02', 6)	# 213-218
    sprite('ku001_03', 8)	# 219-226
    sprite('ku001_04', 6)	# 227-232
    sprite('ku001_05', 6)	# 233-238
    sprite('ku001_00', 6)	# 239-244
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ku003_00', 4)	# 1-4
    sprite('ku003_01', 4)	# 5-8
    sprite('ku003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('ku010_00', 4)	# 1-4
    sprite('ku010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ku010_02', 6)	# 1-6
    sprite('ku010_03', 6)	# 7-12
    sprite('ku010_04', 6)	# 13-18
    sprite('ku010_05', 6)	# 19-24
    sprite('ku010_06', 6)	# 25-30
    sprite('ku010_07', 6)	# 31-36
    sprite('ku010_08', 6)	# 37-42	 **attackbox here**
    sprite('ku010_09', 6)	# 43-48
    sprite('ku010_10', 6)	# 49-54
    sprite('ku010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ku013_00', 4)	# 1-4
    sprite('ku013_01', 4)	# 5-8
    sprite('ku013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('ku010_01', 4)	# 1-4
    sprite('ku010_00', 4)	# 5-8

@State
def CmnActJumpPre():

    def upon_IMMEDIATE():
        SLOT_4 = 0
    sprite('ku010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ku020_00', 4)	# 1-4
    sprite('ku020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ku020_02', 3)	# 1-3
    sprite('ku020_03', 3)	# 4-6
    sprite('ku020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ku020_05', 3)	# 1-3
    sprite('ku020_06', 3)	# 4-6
    label(0)
    sprite('ku020_07', 4)	# 7-10
    sprite('ku020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ku010_00', 3)	# 1-3

@State
def CmnActLandingStiffLoop():
    sprite('ku402_10', 2)	# 1-2
    sprite('ku402_11', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('ku402_11', 3)	# 1-3
    sprite('ku402_10', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ku030_00', 3)	# 1-3
    sprite('ku030_01', 3)	# 4-6
    label(0)
    sprite('ku030_02', 3)	# 7-9
    sprite('ku030_03', 3)	# 10-12
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ku000')
    sprite('ku030_04', 3)	# 13-15
    sprite('ku030_05', 3)	# 16-18
    sprite('ku030_06', 3)	# 19-21
    sprite('ku030_07', 3)	# 22-24
    sprite('ku030_08', 3)	# 25-27
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ku000')
    sprite('ku030_09', 3)	# 28-30
    sprite('ku030_10', 3)	# 31-33
    sprite('ku030_11', 3)	# 34-36
    loopRest()
    gotoLabel(0)
    sprite('ku030_00', 3)	# 37-39

@State
def CmnActBWalk():
    sprite('ku031_00', 4)	# 1-4
    sprite('ku031_01', 4)	# 5-8
    label(0)
    sprite('ku031_02', 4)	# 9-12
    sprite('ku031_03', 4)	# 13-16
    sprite('ku031_04', 4)	# 17-20
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ku001')
    sprite('ku031_05', 4)	# 21-24
    sprite('ku031_06', 4)	# 25-28
    sprite('ku031_07', 4)	# 29-32
    sprite('ku031_08', 4)	# 33-36
    sprite('ku031_09', 4)	# 37-40
    SFX_FOOTSTEP_(100, 1, 1)
    SFX_3('ku001')
    sprite('ku031_10', 4)	# 41-44
    sprite('ku031_11', 4)	# 45-48
    loopRest()
    gotoLabel(0)
    sprite('ku031_00', 3)	# 49-51

@State
def CmnActFDash():
    sprite('ku031_00', 3)	# 1-3
    sprite('ku031_01', 2)	# 4-5
    sprite('ku032_00', 2)	# 6-7
    label(0)
    sprite('ku032_01', 3)	# 8-10
    sprite('ku032_02', 3)	# 11-13
    sprite('ku032_03', 3)	# 14-16
    sprite('ku032_04', 3)	# 17-19
    Unknown8006(100, 1, 1)
    SFX_3('ku000')
    sprite('ku032_05', 3)	# 20-22
    sprite('ku032_06', 3)	# 23-25
    sprite('ku032_07', 3)	# 26-28
    sprite('ku032_08', 3)	# 29-31
    Unknown8006(100, 1, 1)
    SFX_3('ku000')
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ku032_09', 6)	# 1-6
    sprite('ku032_10', 6)	# 7-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        setInvincibleFor(7)
        sendToLabelUpon(2, 1)
        Unknown23001(100, 0)
        Unknown23076()
    sprite('ku033_00', 2)	# 1-2
    sprite('ku033_01', 3)	# 3-5
    physicsXImpulse(-23000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    SFX_4('pku006')
    sprite('ku033_02', 3)	# 6-8
    label(0)
    sprite('ku033_01', 3)	# 9-11
    sprite('ku033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku033_03', 3)	# 15-17
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirTurn():
    sprite('ku025_00', 1)	# 1-1
    sprite('ku025_01', 2)	# 2-3
    sprite('ku025_02', 1)	# 4-4

@State
def CmnActAirFDash():
    sprite('ku035_00', 3)	# 1-3
    label(0)
    sprite('ku035_01', 3)	# 4-6
    sprite('ku035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)
    sprite('ku035_00', 4)	# 10-13

@State
def CmnActAirBDash():
    sprite('ku033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('ku033_02', 3)	# 4-6
    sprite('ku033_01', 3)	# 7-9
    sprite('ku033_02', 3)	# 10-12
    sprite('ku033_01', 3)	# 13-15
    sprite('ku033_02', 3)	# 16-18
    sprite('ku033_01', 3)	# 19-21
    sprite('ku033_02', 3)	# 22-24
    sprite('ku020_05', 3)	# 25-27
    sprite('ku020_06', 3)	# 28-30
    label(0)
    sprite('ku020_07', 4)	# 31-34
    sprite('ku020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ku050_00', 1)	# 1-1
    sprite('ku050_01', 1)	# 2-2
    sprite('ku050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ku050_01', 1)	# 1-1
    sprite('ku050_02', 1)	# 2-2
    sprite('ku050_01', 2)	# 3-4
    sprite('ku050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ku050_02', 1)	# 1-1
    sprite('ku050_03', 1)	# 2-2
    sprite('ku050_02', 2)	# 3-4
    sprite('ku050_01', 2)	# 5-6
    sprite('ku050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ku050_03', 1)	# 1-1
    sprite('ku050_04', 1)	# 2-2
    sprite('ku050_03', 2)	# 3-4
    sprite('ku050_02', 2)	# 5-6
    sprite('ku050_01', 2)	# 7-8
    sprite('ku050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ku050_04', 1)	# 1-1
    sprite('ku050_04', 1)	# 2-2
    sprite('ku050_04', 2)	# 3-4
    sprite('ku050_03', 2)	# 5-6
    sprite('ku050_02', 2)	# 7-8
    sprite('ku050_01', 2)	# 9-10
    sprite('ku050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ku052_00', 1)	# 1-1
    sprite('ku052_01', 1)	# 2-2
    sprite('ku052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ku052_01', 1)	# 1-1
    sprite('ku052_02', 1)	# 2-2
    sprite('ku052_01', 2)	# 3-4
    sprite('ku052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ku052_02', 1)	# 1-1
    sprite('ku052_03', 1)	# 2-2
    sprite('ku052_02', 2)	# 3-4
    sprite('ku052_01', 2)	# 5-6
    sprite('ku052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ku052_03', 1)	# 1-1
    sprite('ku052_04', 1)	# 2-2
    sprite('ku052_03', 2)	# 3-4
    sprite('ku052_02', 2)	# 5-6
    sprite('ku052_01', 2)	# 7-8
    sprite('ku052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ku052_04', 1)	# 1-1
    sprite('ku052_04', 1)	# 2-2
    sprite('ku052_04', 2)	# 3-4
    sprite('ku052_03', 2)	# 5-6
    sprite('ku052_02', 2)	# 7-8
    sprite('ku052_01', 2)	# 9-10
    sprite('ku052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ku054_00', 1)	# 1-1
    sprite('ku054_01', 1)	# 2-2
    sprite('ku054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ku054_01', 1)	# 1-1
    sprite('ku054_02', 1)	# 2-2
    sprite('ku054_01', 2)	# 3-4
    sprite('ku054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ku054_02', 1)	# 1-1
    sprite('ku054_03', 1)	# 2-2
    sprite('ku054_02', 2)	# 3-4
    sprite('ku054_01', 2)	# 5-6
    sprite('ku054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ku054_03', 1)	# 1-1
    sprite('ku054_04', 1)	# 2-2
    sprite('ku054_03', 2)	# 3-4
    sprite('ku054_02', 2)	# 5-6
    sprite('ku054_01', 2)	# 7-8
    sprite('ku054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ku054_04', 1)	# 1-1
    sprite('ku054_04', 1)	# 2-2
    sprite('ku054_04', 2)	# 3-4
    sprite('ku054_03', 2)	# 5-6
    sprite('ku054_02', 2)	# 7-8
    sprite('ku054_01', 2)	# 9-10
    sprite('ku054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ku060_00', 4)	# 1-4
    label(0)
    sprite('ku060_01', 4)	# 5-8
    sprite('ku060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ku060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ku060_04', 8)	# 1-8
    label(1)
    sprite('ku060_05', 4)	# 9-12
    sprite('ku060_06', 4)	# 13-16
    loopRest()
    gotoLabel(1)

@State
def CmnActBDownCrash():
    sprite('ku063_05', 6)	# 1-6

@State
def CmnActBDownBound():
    sprite('ku060_08', 2)	# 1-2
    sprite('ku060_09', 2)	# 3-4
    sprite('ku060_10', 2)	# 5-6
    sprite('ku060_11', 2)	# 7-8

@State
def CmnActBDownLoop():
    sprite('ku060_12', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('ku064_00', 6)	# 1-6
    sprite('ku064_01', 6)	# 7-12
    sprite('ku064_02', 6)	# 13-18
    sprite('ku064_03', 6)	# 19-24

@State
def CmnActFDownUpper():
    sprite('ku063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ku063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ku063_03', 3)	# 1-3
    sprite('ku063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ku063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('ku060_08', 2)	# 1-2
    sprite('ku060_09', 2)	# 3-4
    sprite('ku060_10', 2)	# 5-6
    sprite('ku060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('ku060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ku064_00', 6)	# 1-6
    sprite('ku064_01', 6)	# 7-12
    sprite('ku064_02', 6)	# 13-18
    sprite('ku064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('ku060_00', 4)	# 1-4
    label(0)
    sprite('ku060_01', 4)	# 5-8
    sprite('ku060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ku060_03', 4)	# 1-4
    sprite('ku060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('ku060_04', 8)	# 1-8
    label(0)
    sprite('ku060_05', 4)	# 9-12
    sprite('ku060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ku060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('ku072_00', 3)	# 1-3
    sprite('ku072_01', 3)	# 4-6
    sprite('ku072_02', 3)	# 7-9
    label(0)
    sprite('ku072_01', 3)	# 10-12
    sprite('ku072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ku074_00', 2)	# 1-2
    sprite('ku074_01', 2)	# 3-4
    sprite('ku074_02', 2)	# 5-6
    sprite('ku074_03', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActWallBound():
    sprite('ku072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('ku063_00', 3)	# 1-3
    label(0)
    sprite('ku063_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('ku082_00', 32767)	# 1-32767

@State
def CmnActFreeze():
    sprite('ku052_01', 1)	# 1-1

@State
def CmnActStaggerLoop():
    sprite('ku070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('ku070_01', 4)	# 1-4
    sprite('ku070_02', 4)	# 5-8
    sprite('ku070_03', 4)	# 9-12
    sprite('ku070_04', 4)	# 13-16
    sprite('ku070_05', 4)	# 17-20
    sprite('ku070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ku040_03', 2)	# 1-2
    sprite('ku040_02', 2)	# 3-4
    sprite('ku040_01', 2)	# 5-6
    sprite('ku040_00', 2)	# 7-8

@State
def CmnActUkemiAirN():
    sprite('ku020_02', 3)	# 1-3
    sprite('ku020_03', 3)	# 4-6
    sprite('ku020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirF():
    sprite('ku020_02', 3)	# 1-3
    sprite('ku020_03', 3)	# 4-6
    sprite('ku020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('ku020_02', 3)	# 1-3
    sprite('ku020_03', 3)	# 4-6
    sprite('ku020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandN():
    sprite('ku112_00', 3)	# 1-3
    sprite('ku112_01', 3)	# 4-6
    sprite('ku112_02', 3)	# 7-9
    sprite('ku112_03', 3)	# 10-12
    sprite('ku112_04', 3)	# 13-15
    sprite('ku112_05', 3)	# 16-18
    sprite('ku020_07', 4)	# 19-22
    sprite('ku020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandF():
    sprite('ku112_00', 3)	# 1-3
    sprite('ku112_01', 3)	# 4-6
    sprite('ku112_02', 3)	# 7-9
    sprite('ku112_03', 3)	# 10-12
    sprite('ku112_04', 3)	# 13-15
    sprite('ku112_05', 3)	# 16-18
    sprite('ku020_07', 4)	# 19-22
    sprite('ku020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandB():
    sprite('ku112_00', 3)	# 1-3
    sprite('ku112_01', 3)	# 4-6
    sprite('ku112_02', 3)	# 7-9
    sprite('ku112_03', 3)	# 10-12
    sprite('ku112_04', 3)	# 13-15
    sprite('ku112_05', 3)	# 16-18
    sprite('ku020_07', 4)	# 19-22
    sprite('ku020_08', 4)	# 23-26
    loopRest()

@State
def CmnActUkemiLandNLanding():
    sprite('ku010_00', 3)	# 1-3

@State
def CmnActMidGuardPre():
    sprite('ku040_00', 3)	# 1-3
    sprite('ku040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ku040_02', 5)	# 1-5
    sprite('ku040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ku040_01', 3)	# 1-3
    sprite('ku040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ku040_04', 1)	# 1-1
    label(0)
    sprite('ku040_02', 5)	# 2-6
    sprite('ku040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ku040_01', 3)	# 1-3
    sprite('ku040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ku040_00', 3)	# 1-3
    sprite('ku040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('ku040_04', 1)	# 1-1
    label(0)
    sprite('ku040_02', 5)	# 2-6
    sprite('ku040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ku040_01', 3)	# 1-3
    sprite('ku040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ku040_04', 1)	# 1-1
    label(0)
    sprite('ku040_02', 5)	# 2-6
    sprite('ku040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ku040_01', 3)	# 1-3
    sprite('ku040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ku043_00', 3)	# 1-3
    sprite('ku043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ku043_02', 5)	# 1-5
    sprite('ku043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ku043_01', 3)	# 1-3
    sprite('ku043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ku043_04', 1)	# 1-1
    label(0)
    sprite('ku043_02', 5)	# 2-6
    sprite('ku043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ku043_01', 3)	# 1-3
    sprite('ku043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ku045_00', 3)	# 1-3
    sprite('ku045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ku045_02', 5)	# 1-5
    sprite('ku045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ku045_01', 3)	# 1-3
    sprite('ku045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ku045_04', 1)	# 1-1
    label(0)
    sprite('ku045_02', 5)	# 2-6
    sprite('ku045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ku045_01', 3)	# 1-3
    sprite('ku045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ku040_04', 2)	# 1-2
    sprite('ku040_04', 2)	# 3-4
    sprite('ku040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ku040_02', 4)	# 6-9
    sprite('ku040_01', 4)	# 10-13
    sprite('ku040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ku043_04', 2)	# 1-2
    sprite('ku043_04', 2)	# 3-4
    sprite('ku043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ku043_02', 4)	# 6-9
    sprite('ku043_01', 4)	# 10-13
    sprite('ku043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ku045_04', 2)	# 1-2
    sprite('ku045_04', 2)	# 3-4
    sprite('ku045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ku045_02', 4)	# 6-9
    sprite('ku045_01', 4)	# 10-13
    sprite('ku045_00', 4)	# 14-17

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('ku201_00', 3)	# 1-3
    sprite('ku201_01', 4)	# 4-7
    sprite('ku201_02', 4)	# 8-11	 **attackbox here**
    RefreshMultihit()
    sprite('ku201_03', 4)	# 12-15
    sprite('ku201_04', 6)	# 16-21
    sprite('ku201_05', 4)	# 22-25
    sprite('ku201_06', 4)	# 26-29

@State
def CmnActAirLockWait():
    sprite('ku045_02', 1)	# 1-1
    sprite('ku045_01', 3)	# 2-4
    sprite('ku045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ku250_00', 3)	# 1-3
    sprite('ku250_01', 3)	# 4-6	 **attackbox here**
    sprite('ku250_03', 3)	# 7-9
    sprite('ku250_03', 7)	# 10-16
    DisableAttackRestOfMove()
    sprite('ku250_04', 3)	# 17-19
    sprite('ku250_05', 3)	# 20-22
    sprite('ku250_06', 3)	# 23-25
    Unknown2001()

@State
def CmnActLandSpin():
    sprite('ku071_00', 2)	# 1-2
    label(0)
    sprite('ku071_01', 2)	# 3-4
    sprite('ku071_02', 2)	# 5-6
    sprite('ku071_03', 2)	# 7-8
    sprite('ku071_04', 2)	# 9-10
    sprite('ku071_05', 2)	# 11-12
    sprite('ku071_06', 2)	# 13-14
    sprite('ku071_07', 2)	# 15-16
    sprite('ku071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ku040_02', 3)	# 1-3
    sprite('ku040_01', 3)	# 4-6
    sprite('ku040_00', 3)	# 7-9

@State
def CmnActVertSpin():
    sprite('ku071_00', 2)	# 1-2
    label(0)
    sprite('ku071_01', 2)	# 3-4
    sprite('ku071_02', 2)	# 5-6
    sprite('ku071_03', 2)	# 7-8
    sprite('ku071_04', 2)	# 9-10
    sprite('ku071_05', 2)	# 11-12
    sprite('ku071_06', 2)	# 13-14
    sprite('ku071_07', 2)	# 15-16
    sprite('ku071_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    sprite('ku124_00', 2)	# 1-2
    label(0)
    sprite('ku124_01', 2)	# 3-4
    sprite('ku124_02', 2)	# 5-6
    sprite('ku124_03', 2)	# 7-8
    sprite('ku124_04', 2)	# 9-10
    sprite('ku124_05', 2)	# 11-12
    sprite('ku124_06', 2)	# 13-14
    sprite('ku124_07', 2)	# 15-16
    sprite('ku124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ku077_02', 4)	# 1-4
    label(0)
    sprite('ku077_03', 3)	# 5-7
    sprite('ku077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ku077_05', 5)	# 1-5
    sprite('ku077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ku077_02', 4)	# 1-4
    label(0)
    sprite('ku077_03', 3)	# 5-7
    sprite('ku077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ku077_05', 5)	# 1-5
    sprite('ku077_06', 4)	# 6-9

@State
def CmnActBurstBegin():
    label(0)
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    sprite('ku121_02', 2)	# 5-6
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ku121_03', 3)	# 1-3
    label(1)
    sprite('ku121_04', 2)	# 4-5
    sprite('ku121_05', 2)	# 6-7
    sprite('ku121_06', 2)	# 8-9
    loopRest()
    gotoLabel(1)

@State
def CmnActBurstEnd():
    sprite('ku121_07', 3)	# 1-3
    sprite('ku121_08', 3)	# 4-6
    sprite('ku020_04', 3)	# 7-9
    sprite('ku020_05', 3)	# 10-12
    sprite('ku020_06', 3)	# 13-15
    sprite('ku020_07', 4)	# 16-19
    sprite('ku020_08', 4)	# 20-23
    loopRest()

@State
def CmnActAirBurstBegin():
    sprite('ku331_11', 2)	# 1-2
    sprite('ku331_12', 2)	# 3-4
    label(0)
    sprite('ku331_02', 3)	# 5-7
    sprite('ku331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ku331_04', 2)	# 1-2
    sprite('ku331_05', 2)	# 3-4
    label(0)
    sprite('ku331_06', 3)	# 5-7
    sprite('ku331_07', 3)	# 8-10
    sprite('ku331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ku121_07', 2)	# 1-2
    sprite('ku121_08', 2)	# 3-4
    sprite('ku020_05', 3)	# 5-7
    sprite('ku020_06', 3)	# 8-10
    label(0)
    sprite('ku020_07', 4)	# 11-14
    sprite('ku020_08', 4)	# 15-18
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    label(0)
    sprite('ku121_00', 2)	# 5-6
    sprite('ku121_01', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveLoop():
    sprite('ku121_02', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('ku121_03', 3)	# 4-6
    sprite('ku121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActOverDriveEnd():
    sprite('ku121_06', 2)	# 1-2
    sprite('ku010_00', 6)	# 3-8

@State
def CmnActAirOverDriveBegin():
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    loopRest()
    Unknown23119(16639, 20, 1)
    Unknown4054(11)
    label(0)
    sprite('ku121_00', 2)	# 5-6
    sprite('ku121_01', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveLoop():
    sprite('ku121_02', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(1)
    sprite('ku121_03', 3)	# 4-6
    sprite('ku121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirOverDriveEnd():
    sprite('ku121_05', 2)	# 1-2
    sprite('ku121_06', 2)	# 3-4
    sprite('ku020_04', 2)	# 5-6
    sprite('ku020_05', 2)	# 7-8
    sprite('ku020_06', 2)	# 9-10
    label(0)
    sprite('ku020_07', 4)	# 11-14
    sprite('ku020_08', 4)	# 15-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PKU_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushLoop():
    sprite('ku121_02', 3)	# 1-3
    label(1)
    sprite('ku121_03', 3)	# 4-6
    sprite('ku121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossRushEnd():
    sprite('ku121_05', 2)	# 1-2
    sprite('ku121_06', 2)	# 3-4
    sprite('ku020_04', 2)	# 5-6
    sprite('ku020_05', 2)	# 7-8
    sprite('ku020_06', 2)	# 9-10
    sprite('ku020_07', 2)	# 11-12

@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PKU_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushLoop():

    def upon_STATE_END():
        pass
    sprite('ku121_02', 3)	# 1-3
    label(1)
    sprite('ku121_03', 3)	# 4-6
    sprite('ku121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossRushEnd():
    sprite('ku121_05', 2)	# 1-2
    sprite('ku121_06', 2)	# 3-4
    sprite('ku020_04', 3)	# 5-7
    sprite('ku020_05', 3)	# 8-10
    sprite('ku020_06', 2)	# 11-12
    label(0)
    sprite('ku020_07', 4)	# 13-16
    sprite('ku020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PKU_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('ku121_02', 3)	# 1-3
    label(1)
    sprite('ku121_04', 2)	# 4-5
    sprite('ku121_03', 2)	# 6-7
    loopRest()
    gotoLabel(1)

@State
def CmnActCrossChangeEnd():
    sprite('ku121_05', 2)	# 1-2
    sprite('ku121_06', 2)	# 3-4
    sprite('ku020_04', 3)	# 5-7
    sprite('ku020_05', 3)	# 8-10
    sprite('ku020_06', 3)	# 11-13
    sprite('ku020_07', 4)	# 14-17
    sprite('ku020_08', 4)	# 18-21
    loopRest()

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        Unknown36(28)
        Unknown23148('PKU_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        if (not SLOT_51):
            Unknown23029(11, 9999, 0)
    label(0)
    sprite('ku121_00', 2)	# 1-2
    sprite('ku121_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('ku121_02', 3)	# 1-3
    label(1)
    sprite('ku121_03', 3)	# 4-6
    sprite('ku121_04', 3)	# 7-9
    loopRest()
    gotoLabel(1)

@State
def CmnActAirCrossChangeEnd():
    sprite('ku121_05', 2)	# 1-2
    sprite('ku121_06', 2)	# 3-4
    sprite('ku020_04', 3)	# 5-7
    sprite('ku020_05', 3)	# 8-10
    sprite('ku020_06', 3)	# 11-13
    label(0)
    sprite('ku020_07', 4)	# 14-17
    sprite('ku020_08', 4)	# 18-21
    loopRest()
    gotoLabel(0)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        AirPushbackY(10000)
        Unknown9016(1)
        Unknown1112('')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A2nd')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ku200_00', 3)	# 1-3
    sprite('ku200_01', 4)	# 4-7
    Unknown1051(80)
    SFX_3('slash_knife_slow')
    Unknown7009(0)
    sprite('ku200_50', 3)	# 8-10	 **attackbox here**
    Unknown23054('6b753230305f303200000000000000000000000000000000000000000000000002000000')
    sprite('ku200_50', 12)	# 11-22	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku200_03', 7)	# 23-29

@State
def NmlAtk5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(250)
        Unknown11092(1)
        PushbackX(10000)
        Hitstop(2)
        AirPushbackX(6000)
        AirPushbackY(5000)
        Unknown11057(500)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            SFX_3('ku004')
    sprite('ku208_00', 2)	# 1-2
    sprite('ku208_01', 2)	# 3-4
    physicsXImpulse(15000)
    sprite('ku208_02', 1)	# 5-5
    sprite('ku208_03', 2)	# 6-7
    sprite('ku208_04', 2)	# 8-9
    Unknown8007(100, 1, 1)
    Unknown1019(80)
    sprite('ku208_05', 2)	# 10-11
    Unknown7009(2)
    sprite('ku208_06', 2)	# 12-13	 **attackbox here**
    Unknown1084(1)
    RefreshMultihit()
    sprite('ku208_07ex01', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('ku208_07ex02', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    sprite('ku208_07ex03', 2)	# 18-19	 **attackbox here**
    RefreshMultihit()
    sprite('ku208_06', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    sprite('ku208_07', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    Unknown14070('NmlAtk5A3rd')
    sprite('ku208_07ex01', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    sprite('ku208_07ex02', 2)	# 26-27	 **attackbox here**
    RefreshMultihit()
    sprite('ku208_09', 3)	# 28-30
    if SLOT_2:
        Unknown14072('NmlAtk5A3rd')
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku208_10', 2)	# 31-32
    sprite('ku208_10', 1)	# 33-33
    Unknown14074('NmlAtk5A3rd')
    sprite('ku208_11', 5)	# 34-38
    sprite('ku208_12', 3)	# 39-41
    sprite('ku208_13', 3)	# 42-44
    sprite('ku208_14', 3)	# 45-47

@State
def NmlAtk5A3rd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(550)
        Unknown11092(1)
        Hitstop(10)
        Unknown11001(-3, -3, -3)
        AirPushbackX(13000)
        AirPushbackY(9500)
        PushbackX(10000)

        def upon_ON_HIT_OR_BLOCK():
            Unknown2038(1)
            SFX_3('bound_wood_m')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('ku207_00', 3)	# 1-3
    sprite('ku207_01', 3)	# 4-6
    physicsXImpulse(40000)
    SFX_3('slash_blade_middle')
    Unknown8007(100, 1, 1)
    sprite('ku207_02', 5)	# 7-11	 **attackbox here**
    physicsXImpulse(28000)
    RefreshMultihit()
    sprite('ku207_03', 1)	# 12-12	 **attackbox here**
    DisableAttackRestOfMove()
    Unknown7009(3)
    sprite('ku207_04', 2)	# 13-14
    Unknown1019(80)
    SFX_3('slash_blade_middle')
    Unknown8007(100, 1, 1)
    sprite('ku207_05', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    sprite('ku207_05', 2)	# 18-19	 **attackbox here**
    sprite('ku207_06', 2)	# 20-21	 **attackbox here**
    sprite('ku207_07', 2)	# 22-23
    SFX_3('slash_blade_middle')
    Unknown8007(100, 1, 1)
    sprite('ku207_02', 5)	# 24-28	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(4)
    sprite('ku207_03', 2)	# 29-30	 **attackbox here**
    Unknown14070('NmlAtk5A4th')
    DisableAttackRestOfMove()
    sprite('ku207_04', 2)	# 31-32
    SFX_3('slash_blade_middle')
    Unknown8007(100, 1, 1)
    sprite('ku207_05', 3)	# 33-35	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(18000)
    Unknown1019(0)
    HitJumpCancel(0)
    PushbackX(30000)
    sprite('ku207_05', 4)	# 36-39	 **attackbox here**
    if SLOT_2:
        Unknown14072('NmlAtk5A4th')
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku207_06', 6)	# 40-45	 **attackbox here**
    Unknown14074('NmlAtk5A4th')
    Unknown8010(100, 1, 1)
    Unknown1084(1)
    sprite('ku207_07', 7)	# 46-52
    sprite('ku207_01', 5)	# 53-57
    sprite('ku207_00', 5)	# 58-62

@State
def NmlAtk5A4th():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        Unknown9310(1)
        AirUntechableTime(60)
        AirPushbackX(16000)
        AirPushbackY(-25000)
        YImpluseBeforeWallbounce(2000)
        Unknown9016(1)
        JumpCancel_(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 0)
    sprite('ku202_00', 2)	# 1-2
    sprite('ku202_01', 2)	# 3-4
    sprite('ku202_02', 2)	# 5-6
    sprite('ku202_03', 2)	# 7-8
    physicsXImpulse(-5000)
    physicsYImpulse(23000)
    setGravity(2000)
    SFX_3('hit_m_slow')
    sprite('ku202_04', 4)	# 9-12	 **attackbox here**
    RefreshMultihit()
    GFX_0('kuef_202', 100)
    SFX_1('pku307_0')
    sprite('ku202_05', 4)	# 13-16
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku202_06', 4)	# 17-20
    sprite('ku202_07', 30)	# 21-50
    label(0)
    sprite('ku202_08', 4)	# 51-54
    Unknown1084(1)
    sprite('ku202_09', 4)	# 55-58

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AttackP2(70)
        AirPushbackX(9000)
        AirPushbackY(23000)
        AirUntechableTime(21)
        GroundedHitstunAnimation(1)
        Unknown1112('')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5B2nd')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')

        def upon_45():
            if Unknown2065(25):
                clearUponHandler(45)
                SFX_3('ku003')
    sprite('ku203_00', 2)	# 1-2
    Unknown2018(0, 30)
    sprite('ku203_01', 4)	# 3-6
    sprite('ku203_02', 2)	# 7-8
    SFX_3('slash_blade_middle')
    sprite('ku203_03', 2)	# 9-10
    sprite('ku203_04', 2)	# 11-12
    sprite('ku203_05', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    Unknown7007('706b753130345f32000000000000000064000000706b755f3130355f320000000000000064000000706b753130325f30000000000000000064000000706b753130325f30000000000000000064000000')
    sprite('ku203_06', 2)	# 16-17
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku203_07', 2)	# 18-19	 **attackbox here**
    sprite('ku203_08', 7)	# 20-26
    sprite('ku203_09', 5)	# 27-31
    sprite('ku203_10', 5)	# 32-36
    sprite('ku203_11', 5)	# 37-41
    sprite('ku203_12', 4)	# 42-45

@State
def NmlAtk5B2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')

        def upon_43():
            if (SLOT_48 == 1100):
                Unknown14070('NmlAtk5B3rd')
                Unknown2038(1)
    sprite('ku204_00', 3)	# 1-3
    sprite('ku204_01', 3)	# 4-6
    Unknown7007('706b753132305f30000000000000000064000000706b753132305f31000000000000000064000000706b753132305f320000000000000000000000000000000000000000000000000000000000000000')
    Unknown23029(11, 110, 0)
    sprite('ku204_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    sprite('ku204_03', 4)	# 10-13
    sprite('ku204_02', 4)	# 14-17
    sprite('ku204_03', 4)	# 18-21
    sprite('ku204_02', 4)	# 22-25
    sprite('ku204_03', 4)	# 26-29
    Recovery()
    if SLOT_2:
        Unknown14072('NmlAtk5B3rd')
    sprite('ku204_02', 4)	# 30-33
    sprite('ku204_03', 4)	# 34-37
    Unknown14074('NmlAtk5B3rd')
    sprite('ku204_04', 4)	# 38-41

@State
def NmlAtk5B3rd():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('ku232_00', 3)	# 1-3
    sprite('ku232_01', 3)	# 4-6
    Unknown7007('706b753132315f30000000000000000064000000706b753132315f31000000000000000064000000706b753132315f320000000000000000000000000000000000000000000000000000000000000000')
    Unknown23029(11, 120, 0)
    sprite('ku232_02', 4)	# 7-10
    GFX_1('persona_enter_ply', 0)
    sprite('ku232_03', 4)	# 11-14
    sprite('ku232_02', 4)	# 15-18
    sprite('ku232_03', 4)	# 19-22
    sprite('ku232_02', 4)	# 23-26
    sprite('ku232_03', 1)	# 27-27
    sprite('ku232_03', 3)	# 28-30
    Recovery()
    Unknown2063()
    sprite('ku232_02', 4)	# 31-34
    sprite('ku232_03', 4)	# 35-38
    sprite('ku232_02', 4)	# 39-42
    sprite('ku232_03', 4)	# 43-46
    sprite('ku232_02', 4)	# 47-50
    sprite('ku232_01', 4)	# 51-54

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        Damage(600)
        AttackP1(90)
        Unknown11092(1)
        HitLow(2)
        Hitstop(7)
        WhiffCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('ku004')
    sprite('ku230_00', 3)	# 1-3
    sprite('ku230_00', 2)	# 4-5
    Unknown1051(80)
    SFX_3('hit_l_fast')
    sprite('ku230_01', 2)	# 6-7	 **attackbox here**
    RefreshMultihit()
    Unknown7009(3)
    sprite('ku230_02', 1)	# 8-8
    sprite('ku230_02', 2)	# 9-10
    SFX_3('hit_l_fast')
    sprite('ku230_03', 1)	# 11-11	 **attackbox here**
    RefreshMultihit()
    sprite('ku230_03', 1)	# 12-12	 **attackbox here**
    WhiffCancelEnable(1)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku230_04', 6)	# 13-18
    sprite('ku230_05', 6)	# 19-24

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirUntechableTime(20)
        AirPushbackY(27000)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('ku231_00', 2)	# 1-2
    sprite('ku231_01', 1)	# 3-3
    sprite('ku231_01', 1)	# 4-4
    SFX_3('slash_sword_slow')
    sprite('ku231_02', 2)	# 5-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ku231_03', 3)	# 7-9
    sprite('ku231_04', 4)	# 10-13	 **attackbox here**
    Unknown7007('706b753130365f30000000000000000064000000706b753130365f31000000000000000064000000706b753130365f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ku006')
    sprite('ku231_05', 2)	# 14-15
    setInvincible(0)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku231_06', 4)	# 16-19
    sprite('ku231_05', 4)	# 20-23
    SFX_3('ku006')
    sprite('ku231_06', 4)	# 24-27
    sprite('ku231_05', 6)	# 28-33
    sprite('ku231_06', 6)	# 34-39
    sprite('ku231_02', 5)	# 40-44

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Unknown11001(0, -3, -3)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        Unknown9016(1)
        AirPushbackX(12000)
        AirPushbackY(20000)
        PushbackX(13000)
        AirUntechableTime(40)
    sprite('ku211_00', 3)	# 1-3
    sprite('ku211_01', 1)	# 4-4
    GFX_0('AsiWater', 0)
    sprite('ku211_01', 4)	# 5-8
    sprite('ku211_02', 2)	# 9-10
    SFX_3('slash_blade_middle')
    sprite('ku211_03', 2)	# 11-12
    physicsXImpulse(42000)
    sprite('ku211_04', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    Unknown1019(60)
    Unknown7007('706b753130375f30000000000000000064000000706b753130375f31000000000000000064000000706b753130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ku211_05', 3)	# 15-17	 **attackbox here**
    Unknown1019(60)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku211_06', 5)	# 18-22
    Unknown1019(60)
    sprite('ku211_06', 5)	# 23-27
    Unknown1019(60)
    sprite('ku211_06', 4)	# 28-31
    Unknown1019(60)
    sprite('ku211_07', 4)	# 32-35
    Unknown1019(0)
    sprite('ku211_08', 4)	# 36-39

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
    sprite('ku210_00', 3)	# 1-3
    Unknown1084(1)
    sprite('ku210_01', 2)	# 4-5
    tag_voice(1, 'pku156_0', 'pku156_1', '', '')
    sprite('ku210_02', 1)	# 6-6
    GFX_1('kuef_flysmoke_09', 100)
    physicsXImpulse(15500)
    physicsYImpulse(50000)
    setGravity(5000)
    if (SLOT_19 >= 350000):
        physicsXImpulse(27600)
    sprite('ku210_02', 2)	# 7-8
    sprite('ku210_03', 3)	# 9-11
    sprite('ku210_04', 3)	# 12-14
    sprite('ku210_05', 3)	# 15-17
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('ku210_06', 3)	# 18-20
    sprite('ku210_07', 2)	# 21-22
    SFX_3('hit_m_slow')
    sprite('ku210_08', 1)	# 23-23	 **attackbox here**
    DisableAttackRestOfMove()
    physicsXImpulse(0)
    physicsYImpulse(-52000)
    setGravity(0)
    sprite('ku210_08', 2)	# 24-25	 **attackbox here**
    sprite('ku210_08', 3)	# 26-28	 **attackbox here**
    RefreshMultihit()
    sprite('ku210_09', 9)	# 29-37
    DisableAttackRestOfMove()
    SFX_3('down_steal_m')
    GFX_1('kuef_groundshock_06', 0)
    ScreenShake(0, 10000)
    sprite('ku210_10', 5)	# 38-42
    sprite('ku210_11', 4)	# 43-46

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        Unknown9016(1)
        setGravity(3000)
    sprite('ku210_08', 3)	# 1-3	 **attackbox here**
    StartMultihit()
    label(1)
    sprite('ku210_09', 7)	# 4-10
    StartMultihit()
    SFX_3('down_steal_m')
    GFX_1('kuef_groundshock_06', 0)
    ScreenShake(0, 10000)
    sprite('ku210_10', 4)	# 11-14
    sprite('ku210_11', 3)	# 15-17
    sprite('ku201_00', 2)	# 18-19
    sprite('ku201_01', 4)	# 20-23
    SFX_3('hit_m_slow')
    sprite('ku201_50', 1)	# 24-24	 **attackbox here**
    Unknown23054('6b753230315f303200000000000000000000000000000000000000000000000003000000')
    sprite('ku201_50', 2)	# 25-26	 **attackbox here**
    physicsXImpulse(15000)
    physicsYImpulse(7000)
    setGravity(2300)
    sprite('ku201_03', 3)	# 27-29
    DisableAttackRestOfMove()
    sprite('ku201_04', 6)	# 30-35
    label(0)
    sprite('ku000_00', 6)	# 36-41
    sprite('ku000_01', 6)	# 42-47
    sprite('ku000_02', 6)	# 48-53
    sprite('ku000_03', 6)	# 54-59
    sprite('ku000_04', 6)	# 60-65
    sprite('ku000_05', 6)	# 66-71
    sprite('ku000_00', 6)	# 72-77
    sprite('ku000_07', 6)	# 78-83
    sprite('ku000_08', 6)	# 84-89
    sprite('ku000_09', 6)	# 90-95
    sprite('ku000_10', 6)	# 96-101
    sprite('ku000_11', 6)	# 102-107
    loopRest()
    label(10)
    sprite('ku000_00', 6)	# 108-113
    sprite('ku000_01', 6)	# 114-119
    sprite('ku000_02', 6)	# 120-125
    sprite('ku000_03', 6)	# 126-131
    sprite('ku000_04', 6)	# 132-137
    sprite('ku000_05', 6)	# 138-143
    sprite('ku000_00', 6)	# 144-149
    sprite('ku000_07', 6)	# 150-155
    sprite('ku000_08', 6)	# 156-161
    sprite('ku000_09', 6)	# 162-167
    sprite('ku000_10', 6)	# 168-173
    sprite('ku000_11', 6)	# 174-179
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 180-180

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown9016(1)
    sprite('ku202_00', 4)	# 1-4
    sprite('ku202_01', 5)	# 5-9
    sprite('ku202_02', 3)	# 10-12
    tag_voice(0, 'pku157_0', 'pku157_1', '', '')
    sprite('ku202_03', 2)	# 13-14
    physicsXImpulse(-5000)
    physicsYImpulse(23000)
    setGravity(2000)
    SFX_3('hit_m_slow')
    sprite('ku202_04', 4)	# 15-18	 **attackbox here**
    RefreshMultihit()
    GFX_0('kuef_202', 100)
    sprite('ku202_05', 4)	# 19-22
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku202_06', 4)	# 23-26
    sprite('ku202_07', 15)	# 27-41
    label(10)
    sprite('ku202_08', 4)	# 42-45
    Unknown1084(1)
    sprite('ku202_09', 4)	# 46-49
    loopRest()
    sprite('ku433_00', 3)	# 50-52
    sprite('ku433_01', 3)	# 53-55
    GFX_1('kuef_433aura', 100)
    sprite('ku433_02', 3)	# 56-58
    label(0)
    sprite('ku433_01', 3)	# 59-61
    sprite('ku433_02', 3)	# 62-64
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 65-65

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
    sprite('ku433_01', 3)	# 1-3
    GFX_1('kuef_433aura', 100)
    sprite('ku433_02', 3)	# 4-6
    sprite('ku433_01', 3)	# 7-9
    sprite('ku433_02', 2)	# 10-11
    sprite('ku433_03', 2)	# 12-13
    physicsXImpulse(21000)
    Unknown8007(100, 1, 1)
    sprite('ku433_03', 2)	# 14-15
    Unknown1019(70)
    sprite('ku433_03', 2)	# 16-17
    Unknown1019(70)
    sprite('ku433_03', 2)	# 18-19
    Unknown1019(70)
    GFX_0('kuef_433_upper', 100)
    GFX_1('kuef_433tornafe', 100)
    tag_voice(0, 'pku158_0', 'pku158_1', '', '')
    sprite('ku433_05', 4)	# 20-23	 **attackbox here**
    Unknown23054('6b753433335f303400000000000000000000000000000000000000000000000004000000')
    Unknown1019(0)
    sprite('ku433_05', 7)	# 24-30	 **attackbox here**
    StartMultihit()
    sprite('ku433_06', 7)	# 31-37
    sprite('ku433_07', 10)	# 38-47
    sprite('ku433_08', 4)	# 48-51
    sprite('ku433_09', 4)	# 52-55
    sprite('ku433_10', 6)	# 56-61

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 16)	# 1-16
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 17-17
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    Unknown1007(100000)
    setGravity(2000)
    sprite('ku020_02', 3)	# 18-20
    physicsXImpulse(32000)
    physicsYImpulse(43000)
    setGravity(3100)
    sprite('ku020_03', 3)	# 21-23
    sprite('ku020_04', 3)	# 24-26
    sprite('ku251_00', 5)	# 27-31
    sprite('ku251_01', 2)	# 32-33
    sprite('ku251_01', 4)	# 34-37
    SFX_3('hit_m_slow')
    sprite('ku251_02', 4)	# 38-41
    sprite('ku251_50', 1)	# 42-42	 **attackbox here**
    Unknown23054('6b753235315f303300000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    sprite('ku251_04', 3)	# 43-45	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(-12000)
    physicsYImpulse(-4000)
    setGravity(3200)
    DisableAttackRestOfMove()
    Recovery()
    sendToLabelUpon(2, 1)
    sprite('ku251_05', 3)	# 46-48
    sprite('ku251_06', 3)	# 49-51
    sprite('ku251_07', 4)	# 52-55
    sprite('ku251_08', 5)	# 56-60
    sprite('ku020_05', 3)	# 61-63
    sprite('ku020_06', 3)	# 64-66
    label(0)
    sprite('ku020_07', 4)	# 67-70
    sprite('ku020_08', 4)	# 71-74
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku010_00', 3)	# 75-77
    Unknown8000(100, 1, 1)
    setGravity(0)
    physicsYImpulse(0)
    Unknown1019(0)
    sprite('ku000_00', 6)	# 78-83
    sprite('ku000_01', 6)	# 84-89
    sprite('ku000_02', 6)	# 90-95
    sprite('ku000_03', 6)	# 96-101
    sprite('ku000_04', 6)	# 102-107
    sprite('ku000_05', 6)	# 108-113
    sprite('ku000_00', 6)	# 114-119
    sprite('ku000_07', 6)	# 120-125
    sprite('ku000_08', 6)	# 126-131
    sprite('ku000_09', 6)	# 132-137
    sprite('ku000_10', 6)	# 138-143
    sprite('ku000_11', 6)	# 144-149

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('ku211_00', 3)	# 1-3
    sprite('ku211_01', 1)	# 4-4
    GFX_0('AsiWater_Crush', 0)
    sprite('ku211_01', 3)	# 5-7
    sprite('ku211_02', 2)	# 8-9
    SFX_3('slash_blade_middle')
    sprite('ku211_03', 2)	# 10-11
    physicsXImpulse(15000)
    sprite('ku211_04', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    Unknown1019(60)
    Unknown7007('6b753132300000000000000000000000640000006b7532303100000000000000000000003200000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ku211_05', 3)	# 14-16	 **attackbox here**
    Unknown1019(60)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku211_06', 5)	# 17-21
    Unknown1019(30)
    sprite('ku211_06', 5)	# 22-26
    Unknown1019(30)
    sprite('ku211_07', 6)	# 27-32
    Unknown1019(0)
    sprite('ku211_08', 5)	# 33-37
    loopRest()
    sprite('ku433_00', 3)	# 38-40
    sprite('ku433_01', 3)	# 41-43
    GFX_1('kuef_433aura', 100)
    sprite('ku433_02', 3)	# 44-46
    sprite('ku433_01', 3)	# 47-49
    sprite('ku433_02', 3)	# 50-52
    sprite('ku433_01', 3)	# 53-55
    sprite('ku433_02', 3)	# 56-58
    sprite('ku433_01', 3)	# 59-61
    sprite('ku433_02', 3)	# 62-64
    sprite('ku433_01', 3)	# 65-67
    sprite('ku433_02', 3)	# 68-70
    sprite('ku433_01', 3)	# 71-73
    sprite('ku433_02', 3)	# 74-76
    sprite('ku433_01', 3)	# 77-79
    sprite('ku433_02', 3)	# 80-82
    sprite('ku433_01', 3)	# 83-85
    sprite('ku433_02', 3)	# 86-88
    sprite('ku433_01', 3)	# 89-91
    sprite('ku433_02', 3)	# 92-94
    sprite('ku433_01', 3)	# 95-97
    sprite('ku433_02', 3)	# 98-100

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ku433_01', 3)	# 1-3
    GFX_1('kuef_433aura', 100)
    sprite('ku433_02', 3)	# 4-6
    sprite('ku433_01', 3)	# 7-9
    sprite('ku433_02', 2)	# 10-11
    sprite('ku433_03', 2)	# 12-13
    physicsXImpulse(21000)
    Unknown8007(100, 1, 1)
    sprite('ku433_03', 2)	# 14-15
    Unknown1019(70)
    sprite('ku433_03', 2)	# 16-17
    Unknown1019(70)
    sprite('ku433_03', 2)	# 18-19
    Unknown1019(70)
    GFX_0('kuef_433_upper', 100)
    GFX_1('kuef_433tornafe', 100)
    sprite('ku433_05', 4)	# 20-23	 **attackbox here**
    Unknown23054('6b753433335f303400000000000000000000000000000000000000000000000004000000')
    Unknown1019(0)
    sprite('ku433_05', 7)	# 24-30	 **attackbox here**
    StartMultihit()
    sprite('ku433_06', 7)	# 31-37
    sprite('ku433_07', 10)	# 38-47
    sprite('ku433_08', 4)	# 48-51
    sprite('ku433_09', 4)	# 52-55
    sprite('ku433_10', 6)	# 56-61

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(500)
        Unknown11092(1)
        AirPushbackY(13000)
        Hitstop(4)
        AirUntechableTime(20)
        HitOrBlockJumpCancel(1)
        HitOverhead(0)
        HitOrBlockCancel('NmlAtkAIR5A2nd')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            SFX_3('ku004')
    sprite('ku250_00', 4)	# 1-4
    sprite('ku250_00', 3)	# 5-7
    SFX_3('hit_l_fast')
    sprite('ku250_01', 3)	# 8-10	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    Unknown7009(0)
    sprite('ku250_02', 3)	# 11-13	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ku250_01', 3)	# 14-16	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_fast')
    sprite('ku250_02', 4)	# 17-20	 **attackbox here**
    RefreshMultihit()
    sprite('ku250_03', 9)	# 21-29
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()

@State
def NmlAtkAIR5A2nd():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirPushbackX(10000)
        AirPushbackY(25000)
        Hitstop(7)
        AirUntechableTime(22)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        HitOverhead(0)
        HitJumpCancel(1)
        sendToLabelUpon(10, 0)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('ku251_00', 2)	# 1-2
    sprite('ku251_01', 1)	# 3-3
    sprite('ku251_01', 3)	# 4-6
    SFX_3('hit_m_slow')
    sprite('ku251_02', 2)	# 7-8
    sprite('ku251_50', 3)	# 9-11	 **attackbox here**
    Unknown23054('6b753235315f303300000000000000000000000000000000000000000000000002000000')
    RefreshMultihit()
    Unknown7007('706b753130325f32000000000000000064000000706b753130335f32000000000000000064000000706b753331325f300000000000000000640000000000000000000000000000000000000000000000')
    sprite('ku251_04', 3)	# 12-14	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku251_05', 3)	# 15-17
    sprite('ku251_06', 3)	# 18-20
    sprite('ku251_07', 4)	# 21-24
    sprite('ku251_08', 5)	# 25-29
    ExitState()
    label(0)
    sprite('ku251_04', 3)	# 30-32	 **attackbox here**
    Unknown1084(1)
    physicsXImpulse(9000)
    physicsYImpulse(21000)
    setGravity(2000)
    Unknown22004(4, 4)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    if CheckInput(0x5f):
        physicsXImpulse(-9000)
    sprite('ku251_05', 3)	# 33-35
    sprite('ku251_06', 4)	# 36-39
    sprite('ku251_07', 5)	# 40-44
    sprite('ku251_08', 5)	# 45-49

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        HitOrBlockJumpCancel(1)
    sprite('ku254_00', 3)	# 1-3
    sprite('ku254_01', 3)	# 4-6
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown22004(6, 6)
    Unknown1084(1)
    Unknown7007('706b753132335f30000000000000000064000000706b753132325f30000000000000000064000000706b753132335f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ku254_02', 4)	# 7-10
    sprite('ku254_03', 4)	# 11-14
    GFX_1('persona_enter_ply', 0)
    Unknown23029(11, 130, 0)

    def upon_43():
        if (SLOT_48 == 998):
            Recovery()
    sprite('ku254_02', 4)	# 15-18
    sprite('ku254_03', 4)	# 19-22
    sprite('ku254_02', 4)	# 23-26
    sprite('ku254_03', 4)	# 27-30
    sprite('ku254_02', 4)	# 31-34
    sprite('ku254_03', 2)	# 35-36
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(40)
    YAccel(40)
    DisableAttackRestOfMove()
    Unknown2063()
    sprite('ku254_03', 6)	# 37-42
    sprite('ku254_04', 6)	# 43-48

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        AirPushbackX(3500)
        AirPushbackY(-60000)
        blockstun(22)
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirUntechableTime(60)
        Unknown9310(1)

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(0, 10000)
        JumpCancel_(0)
        clearUponHandler(2)
        Unknown2015(50)
    sprite('ku210_02', 3)	# 1-3
    sprite('ku210_02', 2)	# 4-5
    Unknown1084(1)
    SFX_1('pku308_1')
    physicsXImpulse(20000)
    physicsYImpulse(35000)
    setGravity(5000)
    if CheckInput(0x79):
        physicsXImpulse(50000)
    sprite('ku210_03', 2)	# 6-7
    sprite('ku210_04', 1)	# 8-8
    sprite('ku210_05', 3)	# 9-11
    physicsXImpulse(0)
    physicsYImpulse(0)
    setGravity(0)
    sprite('ku210_06', 4)	# 12-15
    sprite('ku210_07', 3)	# 16-18
    SFX_3('hit_m_slow')
    sprite('ku210_08', 1)	# 19-19	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(0)
    physicsYImpulse(-10000)
    setGravity(10000)
    Unknown2015(-1)
    sprite('ku210_08', 1)	# 20-20	 **attackbox here**
    loopRest()
    sendToLabelUpon(2, 1)
    label(0)
    sprite('ku210_08', 1)	# 21-21	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku210_09', 13)	# 22-34
    SFX_3('down_steal_m')
    GFX_1('kuef_groundshock_06', 0)
    ScreenShake(0, 10000)
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('ku210_10', 3)	# 35-37
    sprite('ku210_11', 4)	# 38-41

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(15000)
            if (SLOT_18 >= 7):
                Unknown1015(352)
                if (SLOT_12 >= 22400):
                    SLOT_12 = 22400
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ku031_00', 3)	# 1-3
    sprite('ku031_01', 2)	# 4-5
    sprite('ku032_00', 2)	# 6-7
    label(0)
    sprite('ku032_01', 3)	# 8-10
    sprite('ku032_02', 3)	# 11-13
    sprite('ku032_03', 3)	# 14-16
    sprite('ku032_04', 3)	# 17-19
    Unknown8006(100, 1, 1)
    sprite('ku032_05', 3)	# 20-22
    sprite('ku032_06', 3)	# 23-25
    sprite('ku032_07', 3)	# 26-28
    sprite('ku032_08', 3)	# 29-31
    Unknown8006(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku310_00', 1)	# 32-32
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ku310_01', 2)	# 33-34
    sprite('ku310_02', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    sprite('ku310_03', 3)	# 38-40
    sprite('ku310_04', 10)	# 41-50
    SFX_4('pku154')
    sprite('ku310_03', 4)	# 51-54
    sprite('ku310_01', 4)	# 55-58
    sprite('ku310_00', 2)	# 59-60

@State
def NmlAtkThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AttackP2(50)
        AirPushbackX(11000)
        AirPushbackY(30000)
        Hitstop(5)
        DisableAttackRestOfMove()
        Unknown2004(1, 0)
    sprite('ku310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('ku311_00', 5)	# 5-9
    Unknown2018(1, 80)
    sprite('ku311_01', 12)	# 10-21
    SFX_1('pku153')
    sprite('ku311_02', 4)	# 22-25	 **attackbox here**
    GFX_1('kuef_tukkomi_05', 1)
    SFX_3('grip_fast')
    sprite('ku311_01', 13)	# 26-38
    sprite('ku311_02', 4)	# 39-42	 **attackbox here**
    GFX_1('kuef_tukkomi_05', 1)
    SFX_3('grip_fast')
    sprite('ku311_01', 15)	# 43-57
    sprite('ku311_03', 5)	# 58-62
    sprite('ku311_04', 15)	# 63-77
    sprite('ku311_05', 2)	# 78-79
    sprite('ku311_06', 2)	# 80-81
    Unknown2018(0, 80)
    sprite('ku311_07', 3)	# 82-84	 **attackbox here**
    RefreshMultihit()
    Unknown2018(1, 80)
    SFX_3('slap_large')
    sprite('ku311_08', 3)	# 85-87
    sprite('ku311_09', 3)	# 88-90
    sprite('ku311_10', 3)	# 91-93
    sprite('ku311_11', 3)	# 94-96
    sprite('ku311_12', 3)	# 97-99

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtkBackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(15000)
            if (SLOT_18 >= 7):
                Unknown1015(352)
                if (SLOT_12 >= 22400):
                    SLOT_12 = 22400
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ku031_00', 3)	# 1-3
    sprite('ku031_01', 2)	# 4-5
    sprite('ku032_00', 2)	# 6-7
    label(0)
    sprite('ku032_01', 3)	# 8-10
    sprite('ku032_02', 3)	# 11-13
    sprite('ku032_03', 3)	# 14-16
    sprite('ku032_04', 3)	# 17-19
    Unknown8006(100, 1, 1)
    sprite('ku032_05', 3)	# 20-22
    sprite('ku032_06', 3)	# 23-25
    sprite('ku032_07', 3)	# 26-28
    sprite('ku032_08', 3)	# 29-31
    Unknown8006(100, 1, 1)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku310_00', 1)	# 32-32
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ku310_01', 2)	# 33-34
    sprite('ku310_02', 3)	# 35-37	 **attackbox here**
    Unknown1084(1)
    sprite('ku310_03', 3)	# 38-40
    sprite('ku310_04', 10)	# 41-50
    SFX_4('pku154')
    sprite('ku310_03', 4)	# 51-54
    sprite('ku310_01', 4)	# 55-58
    sprite('ku310_00', 2)	# 59-60

@State
def NmlAtkBackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AirUntechableTime(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AttackP2(50)
        AirPushbackX(11000)
        AirPushbackY(30000)
        Hitstop(5)
        DisableAttackRestOfMove()
        Unknown2004(1, 0)
    sprite('ku310_02', 4)	# 1-4	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('ku311_00ex01', 2)	# 5-6
    Unknown5001('0000000004000000040000000000000001000000')
    Unknown2018(1, 80)
    sprite('ku311_00', 2)	# 7-8
    Unknown2005()
    sprite('ku311_01', 12)	# 9-20
    SFX_1('pku153')
    sprite('ku311_02', 4)	# 21-24	 **attackbox here**
    GFX_1('kuef_tukkomi_05', 1)
    SFX_3('grip_fast')
    sprite('ku311_01', 13)	# 25-37
    sprite('ku311_02', 4)	# 38-41	 **attackbox here**
    GFX_1('kuef_tukkomi_05', 1)
    SFX_3('grip_fast')
    sprite('ku311_01', 15)	# 42-56
    sprite('ku311_03', 5)	# 57-61
    sprite('ku311_04', 15)	# 62-76
    sprite('ku311_05', 2)	# 77-78
    sprite('ku311_06', 2)	# 79-80
    Unknown2018(0, 80)
    sprite('ku311_07', 3)	# 81-83	 **attackbox here**
    RefreshMultihit()
    Unknown2018(1, 80)
    SFX_3('slap_large')
    sprite('ku311_08', 3)	# 84-86
    sprite('ku311_09', 3)	# 87-89
    sprite('ku311_10', 3)	# 90-92
    sprite('ku311_11', 3)	# 93-95
    sprite('ku311_12', 3)	# 96-98

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2400)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(30000)
        PushbackX(19800)
        AirUntechableTime(60)
        Unknown1084(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    sprite('ku403_00', 1)	# 1-1
    sprite('ku403_01', 2)	# 2-3
    sprite('ku403_02', 3)	# 4-6
    physicsXImpulse(-10000)
    physicsYImpulse(20000)
    setGravity(1600)
    Unknown7006('pku206_2', 100, 846556016, 845100848, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku403_02', 2)	# 7-8
    sprite('ku403_03', 2)	# 9-10
    clearUponHandler(3)
    Unknown1084(1)
    setGravity(0)
    SFX_3('ku013')
    sprite('ku403_53', 5)	# 11-15
    sprite('ku403_54ex01', 5)	# 16-20	 **attackbox here**
    GFX_1('kuef_rageblow_02', 0)
    RefreshMultihit()
    sprite('ku403_54ex01', 5)	# 21-25	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('ku403_55', 3)	# 26-28
    setInvincible(0)
    physicsXImpulse(-5000)
    setGravity(700)
    sprite('ku020_04', 3)	# 29-31
    sprite('ku020_05', 3)	# 32-34
    sprite('ku020_06', 3)	# 35-37
    label(0)
    sprite('ku020_07', 3)	# 38-40
    sprite('ku020_08', 3)	# 41-43
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku402_10', 5)	# 44-48
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 15)	# 49-63
    sprite('ku402_10', 5)	# 64-68

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(2400)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(40000)
        AirPushbackY(30000)
        PushbackX(19800)
        AirUntechableTime(60)
        Unknown1084(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 1)
    label(2)
    sprite('ku403_02', 3)	# 1-3
    Unknown1084(1)
    sprite('ku403_02', 3)	# 4-6
    physicsXImpulse(-15000)
    physicsYImpulse(20000)
    setGravity(1600)
    Unknown7006('pku206_2', 100, 846556016, 845100848, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku403_02', 2)	# 7-8
    sprite('ku403_03', 2)	# 9-10
    clearUponHandler(3)
    Unknown1084(1)
    setGravity(0)
    SFX_3('ku013')
    sprite('ku403_53', 5)	# 11-15
    sprite('ku403_54ex01', 5)	# 16-20	 **attackbox here**
    GFX_1('kuef_rageblow_02', 0)
    RefreshMultihit()
    sprite('ku403_54ex01', 5)	# 21-25	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('ku403_55', 3)	# 26-28
    setInvincible(0)
    physicsXImpulse(-5000)
    setGravity(1000)
    sprite('ku020_04', 3)	# 29-31
    sprite('ku020_05', 3)	# 32-34
    sprite('ku020_06', 3)	# 35-37
    label(0)
    sprite('ku020_07', 3)	# 38-40
    sprite('ku020_08', 3)	# 41-43
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku402_10', 5)	# 44-48
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 10)	# 49-58
    sprite('ku402_10', 5)	# 59-63

@State
def ScrewDriverA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(420)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(55)
        blockstun(25)
        Unknown11001(3, 3, 3)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
        AirPushbackX(0)
        AirPushbackY(22000)
        Unknown9016(1)
        PushbackX(20000)
        setGravity(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(5, 1)

        def upon_11():
            sendToLabel(0)

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('ku402_00', 2)	# 1-2
    sprite('ku402_01', 1)	# 3-3
    sprite('ku402_01', 3)	# 4-6
    Unknown7006('pku203_0', 100, 846556016, 811545648, 0, 0, 100, 846556016, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ku402_02', 1)	# 7-7
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03', 2)	# 8-9	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(35000)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 10-11	 **attackbox here**
    sprite('ku402_05', 2)	# 12-13	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 14-15	 **attackbox here**
    sprite('ku402_03', 2)	# 16-17	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 18-19	 **attackbox here**
    sprite('ku402_05', 2)	# 20-21	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 22-23	 **attackbox here**
    sprite('ku402_07', 2)	# 24-25
    Recovery()
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 26-28
    sprite('ku402_09', 3)	# 29-31
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 32-33	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(11000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 34-35	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 38-39	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 40-41	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 44-45	 **attackbox here**
    Unknown23029(5, 2000, 0)
    RefreshMultihit()
    sprite('ku402_03', 2)	# 46-47	 **attackbox here**
    physicsXImpulse(33000)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_04', 2)	# 48-49	 **attackbox here**
    sprite('ku402_05', 2)	# 50-51	 **attackbox here**
    sprite('ku402_06', 2)	# 52-53	 **attackbox here**
    sprite('ku402_07', 2)	# 54-55
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 56-58
    sprite('ku402_09', 3)	# 59-61
    label(1)
    sprite('ku402_10', 2)	# 62-63
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 7)	# 64-70
    sprite('ku402_12', 3)	# 71-73
    sprite('ku402_13', 3)	# 74-76

@State
def ScrewDriverB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(500)
        AttackP1(80)
        AttackP2(85)
        Unknown11092(1)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(55)
        blockstun(25)
        Unknown11001(3, 3, 3)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
        AirPushbackX(12000)
        AirPushbackY(30000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        PushbackX(20000)
        setGravity(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(5, 1)

        def upon_11():
            sendToLabel(0)

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('ku402_00', 3)	# 1-3
    sprite('ku402_01', 11)	# 4-14
    Unknown7006('pku205_0', 100, 846556016, 828322864, 0, 0, 100, 846556016, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ku402_02', 3)	# 15-17
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03', 1)	# 18-18	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(50000)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_03', 2)	# 19-20	 **attackbox here**
    setInvincible(0)
    sprite('ku402_04', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05', 2)	# 23-24	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 25-26	 **attackbox here**
    sprite('ku402_03', 2)	# 27-28	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 29-30	 **attackbox here**
    sprite('ku402_05', 2)	# 31-32	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 33-34	 **attackbox here**
    sprite('ku402_03', 3)	# 35-37	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_07', 2)	# 38-39
    Recovery()
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2300)
    sprite('ku402_08', 3)	# 40-42
    sprite('ku402_09', 3)	# 43-45
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 46-47	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(10000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 48-49	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 52-53	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 54-55	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 56-57	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 58-59	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 60-61	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_04', 2)	# 62-63	 **attackbox here**
    physicsXImpulse(60000)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_05', 2)	# 64-65	 **attackbox here**
    sprite('ku402_06', 2)	# 66-67	 **attackbox here**
    sprite('ku402_03', 2)	# 68-69	 **attackbox here**
    sprite('ku402_04', 2)	# 70-71	 **attackbox here**
    sprite('ku402_07', 2)	# 72-73
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2300)
    sprite('ku402_08', 3)	# 74-76
    sprite('ku402_09', 3)	# 77-79
    label(1)
    sprite('ku402_10', 3)	# 80-82
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 7)	# 83-89
    sprite('ku402_12', 3)	# 90-92
    sprite('ku402_13', 3)	# 93-95

@State
def ScrewDriverEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(550)
        AttackP1(80)
        AttackP2(75)
        Unknown11092(1)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(55)
        blockstun(25)
        Unknown11001(3, 2, 2)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown11056(0)
        AirPushbackX(15000)
        AirPushbackY(27000)
        YImpluseBeforeWallbounce(2200)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        PushbackX(20000)
        setGravity(0)
        Unknown1084(1)
        Unknown30065(0)
        MinimumDamagePct(10)
        clearUponHandler(2)
        sendToLabelUpon(5, 1)

        def upon_11():
            sendToLabel(0)

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('ku402_00', 3)	# 1-3
    sprite('ku402_01', 4)	# 4-7
    Unknown7006('pku205_1', 100, 846556016, 845100336, 0, 0, 100, 846556016, 828322608, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ku402_02', 3)	# 8-10
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03ex', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(52000)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 13-14	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 15-16	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 17-18	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 19-20	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 21-22	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 23-24	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 25-26	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 27-28	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 29-30	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05', 2)	# 31-32	 **attackbox here**
    DisableAttackRestOfMove()
    setInvincible(0)
    sprite('ku402_06', 2)	# 33-34	 **attackbox here**
    sprite('ku402_03', 2)	# 35-36	 **attackbox here**
    sprite('ku402_07', 2)	# 37-38
    Recovery()
    Unknown23029(5, 2000, 0)
    physicsXImpulse(40000)
    EnableCollision(1)
    setGravity(2300)
    sprite('ku402_08', 3)	# 39-41
    sprite('ku402_09', 3)	# 42-44
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 45-46	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(11000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 47-48	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 49-50	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 51-52	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 53-54	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_04ex', 2)	# 59-60	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    Unknown23029(5, 2000, 0)
    sprite('ku402_03', 2)	# 63-64	 **attackbox here**
    physicsXImpulse(42900)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_04', 2)	# 65-66	 **attackbox here**
    sprite('ku402_05', 2)	# 67-68	 **attackbox here**
    sprite('ku402_07', 2)	# 69-70
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 71-73
    sprite('ku402_09', 3)	# 74-76
    sprite('ku020_06', 3)	# 77-79
    label(1)
    sprite('ku402_10', 2)	# 80-81
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 5)	# 82-86
    sprite('ku402_12', 2)	# 87-88
    sprite('ku402_13', 2)	# 89-90

@State
def AirScrewDriverA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(420)
        AttackP1(80)
        Unknown11092(1)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(45)
        blockstun(25)
        Unknown11001(3, 3, 3)
        Unknown11058('0100000000000000000000000000000000000000')
        AirPushbackX(0)
        AirPushbackY(28000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        PushbackX(20000)
        Unknown11056(3)
        setGravity(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(5, 2)

        def upon_11():
            sendToLabel(0)

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('ku402_00', 2)	# 1-2
    sprite('ku402_01', 1)	# 3-3
    sprite('ku402_01', 3)	# 4-6
    Unknown7006('pku203_0', 100, 846556016, 811545648, 0, 0, 100, 846556016, 845099824, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ku402_02', 3)	# 7-9
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(29000)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 13-14	 **attackbox here**
    sprite('ku402_05', 2)	# 15-16	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 17-18	 **attackbox here**
    sprite('ku402_03', 2)	# 19-20	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 21-22	 **attackbox here**
    sprite('ku402_05', 2)	# 23-24	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 25-26	 **attackbox here**
    sprite('ku402_07', 2)	# 27-28
    Recovery()
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 29-31
    sprite('ku402_09', 3)	# 32-34
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 35-36	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(10000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 37-38	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 39-40	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 41-42	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 43-44	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 45-46	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 47-48	 **attackbox here**
    Unknown23029(5, 2000, 0)
    RefreshMultihit()
    sprite('ku402_03', 2)	# 49-50	 **attackbox here**
    physicsXImpulse(33000)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_04', 2)	# 51-52	 **attackbox here**
    sprite('ku402_05', 2)	# 53-54	 **attackbox here**
    sprite('ku402_06', 2)	# 55-56	 **attackbox here**
    sprite('ku402_07', 2)	# 57-58
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2300)
    sprite('ku402_08', 3)	# 59-61
    sprite('ku402_09', 3)	# 62-64
    label(1)
    sprite('ku020_07', 3)	# 65-67
    sprite('ku020_08', 3)	# 68-70
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ku402_10', 2)	# 71-72
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 7)	# 73-79
    sprite('ku402_12', 3)	# 80-82
    sprite('ku402_13', 3)	# 83-85

@State
def AirScrewDriverB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(500)
        AttackP1(80)
        AttackP2(85)
        Unknown11092(1)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(48)
        blockstun(25)
        Unknown11001(3, 3, 3)
        Unknown11058('0100000000000000000000000000000000000000')
        AirPushbackX(0)
        AirPushbackY(37000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        PushbackX(20000)
        Unknown11056(3)
        setGravity(0)
        Unknown1084(1)
        clearUponHandler(2)
        sendToLabelUpon(5, 2)

        def upon_11():
            sendToLabel(0)

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('ku402_00', 3)	# 1-3
    sprite('ku402_01', 11)	# 4-14
    Unknown7006('pku205_0', 100, 846556016, 828322864, 0, 0, 100, 846556016, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ku402_02', 3)	# 15-17
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(50000)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 21-22	 **attackbox here**
    sprite('ku402_05', 2)	# 23-24	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 25-26	 **attackbox here**
    sprite('ku402_03', 2)	# 27-28	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 29-30	 **attackbox here**
    sprite('ku402_05', 2)	# 31-32	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 33-34	 **attackbox here**
    sprite('ku402_07', 2)	# 35-36
    Recovery()
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 37-39
    sprite('ku402_09', 3)	# 40-42
    sprite('ku020_05', 3)	# 43-45
    sprite('ku020_06', 3)	# 46-48
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 49-50	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(10000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 51-52	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 53-54	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 57-58	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 59-60	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 61-62	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_04ex', 2)	# 63-64	 **attackbox here**
    Unknown23029(5, 2000, 0)
    RefreshMultihit()
    sprite('ku402_03', 2)	# 65-66	 **attackbox here**
    physicsXImpulse(33000)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_04', 2)	# 67-68	 **attackbox here**
    sprite('ku402_05', 2)	# 69-70	 **attackbox here**
    sprite('ku402_06', 2)	# 71-72	 **attackbox here**
    sprite('ku402_07', 2)	# 73-74
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2300)
    sprite('ku402_08', 3)	# 75-77
    sprite('ku402_09', 3)	# 78-80
    sprite('ku020_06', 3)	# 81-83
    label(1)
    sprite('ku020_07', 3)	# 84-86
    sprite('ku020_08', 3)	# 87-89
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ku402_10', 3)	# 90-92
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 14)	# 93-106
    sprite('ku402_12', 2)	# 107-108
    sprite('ku402_13', 2)	# 109-110

@State
def AirScrewDriverEx():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(550)
        AttackP1(80)
        AttackP2(75)
        Unknown11092(1)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(50)
        blockstun(25)
        Unknown11001(3, 3, 3)
        Unknown11058('0100000000000000000000000000000000000000')
        AirPushbackX(0)
        AirPushbackY(37000)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Unknown9016(1)
        PushbackX(20000)
        Unknown11056(3)
        setGravity(0)
        Unknown1084(1)
        Unknown30065(0)
        MinimumDamagePct(10)
        clearUponHandler(2)
        sendToLabelUpon(5, 2)

        def upon_11():
            sendToLabel(0)

        def upon_3():
            if (SLOT_163 < 0):
                Unknown23073()
    sprite('ku402_00', 3)	# 1-3
    sprite('ku402_01', 4)	# 4-7
    Unknown7006('pku205_1', 100, 846556016, 845100336, 0, 0, 100, 846556016, 828322608, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('ku402_02', 3)	# 8-10
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03ex', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(52000)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 13-14	 **attackbox here**
    sprite('ku402_05ex', 2)	# 15-16	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 17-18	 **attackbox here**
    sprite('ku402_03ex', 2)	# 19-20	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 21-22	 **attackbox here**
    sprite('ku402_05ex', 2)	# 23-24	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 25-26	 **attackbox here**
    sprite('ku402_07', 2)	# 27-28
    Recovery()
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 29-31
    sprite('ku402_09', 3)	# 32-34
    sprite('ku020_05', 3)	# 35-37
    sprite('ku020_06', 3)	# 38-40
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 41-42	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(10000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 43-44	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 45-46	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 47-48	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 49-50	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 51-52	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 53-54	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 55-56	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_04ex', 2)	# 57-58	 **attackbox here**
    Unknown23029(5, 2000, 0)
    RefreshMultihit()
    sprite('ku402_03', 2)	# 59-60	 **attackbox here**
    physicsXImpulse(33000)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_04', 2)	# 61-62	 **attackbox here**
    sprite('ku402_05', 2)	# 63-64	 **attackbox here**
    sprite('ku402_06', 2)	# 65-66	 **attackbox here**
    sprite('ku402_07', 2)	# 67-68
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2300)
    sprite('ku402_08', 3)	# 69-71
    sprite('ku402_09', 3)	# 72-74
    sprite('ku020_06', 3)	# 75-77
    label(1)
    sprite('ku020_07', 3)	# 78-80
    sprite('ku020_08', 3)	# 81-83
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('ku402_10', 2)	# 84-85
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 7)	# 86-92
    sprite('ku402_12', 3)	# 93-95
    sprite('ku402_13', 3)	# 96-98

@State
def TripleTVA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_64 = 0

        def upon_43():
            if (SLOT_48 == 5106):
                SLOT_58 = 1
    sprite('ku404_00', 3)	# 1-3
    sprite('ku404_00', 4)	# 4-7
    Unknown23029(11, 510, 0)
    Unknown7006('pku210_0', 100, 846556016, 828321841, 0, 0, 100, 846556016, 845099057, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ku404_01', 2)	# 8-9
    SFX_3('bound_wood_m')
    sprite('ku404_01', 1)	# 10-10
    sprite('ku404_01', 2)	# 11-12
    GFX_0('Tvwarp', 0)
    Unknown38(6, 1)
    Unknown23029(1, 5100, 0)
    sprite('ku404_02', 6)	# 13-18
    sprite('ku404_03', 5)	# 19-23
    sprite('ku404_03', 12)	# 24-35
    if (not SLOT_58):
        enterState('TVWarpA')
    sprite('ku404_04', 9)	# 36-44

@State
def TripleTVB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_64 = 0

        def upon_43():
            if (SLOT_48 == 5106):
                SLOT_58 = 1
    sprite('ku404_00', 3)	# 1-3
    sprite('ku404_00', 4)	# 4-7
    Unknown23029(11, 510, 0)
    if random_(2, 0, 75):
        Unknown7006('pku210_0', 100, 846556016, 828321841, 0, 0, 100, 846556016, 845099057, 0, 0, 100, 0, 0, 0, 0, 0)
    else:
        SLOT_64 = 1
    sprite('ku404_01', 2)	# 8-9
    SFX_3('bound_wood_m')
    sprite('ku404_01', 1)	# 10-10
    sprite('ku404_01', 2)	# 11-12
    GFX_0('Tvwarp', 0)
    Unknown38(6, 1)
    Unknown23029(1, 5101, 0)
    sprite('ku404_02', 3)	# 13-15
    sprite('ku404_02', 3)	# 16-18
    sprite('ku404_03', 5)	# 19-23
    sprite('ku404_03', 12)	# 24-35
    if (not SLOT_58):
        enterState('TVWarpB')
    sprite('ku404_04', 9)	# 36-44
    loopRest()

@State
def TripleTVEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        SLOT_64 = 0

        def upon_3():
            if CheckInput(0x17):
                clearUponHandler(3)
                Unknown2038(1)

        def upon_43():
            if (SLOT_48 == 5106):
                SLOT_58 = 1
    sprite('ku404_00', 3)	# 1-3
    sprite('ku404_00', 4)	# 4-7
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 510, 0)
    if random_(2, 0, 66):
        Unknown7006('pku211_0', 100, 846556016, 828322097, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    else:
        SLOT_64 = 1
    sprite('ku404_01', 2)	# 8-9
    SFX_3('bound_wood_m')
    sprite('ku404_01', 1)	# 10-10
    sprite('ku404_01', 2)	# 11-12
    GFX_0('Tvwarp', 0)
    Unknown38(6, 1)
    Unknown23029(6, 5102, 0)
    GFX_0('Tvwarp_Back', 1)
    Unknown38(7, 1)
    sprite('ku404_02', 3)	# 13-15
    sprite('ku404_02', 3)	# 16-18
    sprite('ku404_03', 2)	# 19-20
    sprite('ku404_03', 5)	# 21-25
    if (not SLOT_58):
        if SLOT_2:
            enterState('TVWarpEx_Front')
        else:
            enterState('TVWarpEx_Back')
    sprite('ku404_04', 5)	# 26-30
    sprite('ku404_04', 4)	# 31-34
    loopRest()

@State
def TVWarpA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        clearUponHandler(2)
        Unknown2018(0, 2)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown11063(1)
        Unknown30068(1)
        Unknown23029(6, 5104, 0)

        def upon_STATE_END():
            Unknown23029(6, 5105, 0)
    sprite('ku405_00', 3)	# 1-3
    Unknown1084(1)
    sprite('ku405_01ex00', 3)	# 4-6
    Unknown23029(11, 511, 0)
    setGravity(0)
    Unknown1007(20000)
    sprite('ku405_00', 1)	# 7-7
    sprite('ku405_01ex01', 1)	# 8-8
    sprite('ku405_01ex02', 1)	# 9-9
    sprite('ku405_01ex03', 1)	# 10-10
    sprite('ku405_00ex04', 1)	# 11-11
    sprite('ku405_00ex06', 1)	# 12-12
    sprite('null', 1)	# 13-13
    sprite('null', 1)	# 14-14
    EnableCollision(0)
    Unknown23151(6, 2)
    Unknown1084(1)
    setGravity(0)
    Unknown1007(-150000)
    sprite('ku405_02', 4)	# 15-18
    Unknown2006()
    sprite('ku405_03', 4)	# 19-22
    sprite('ku405_04', 1)	# 23-23
    EnableCollision(1)
    setGravity(2000)
    Unknown13014(1)
    Unknown13008(1)
    Unknown13019(1)
    Unknown13015(1)
    physicsXImpulse(27000)
    physicsYImpulse(19000)
    SFX_3('ku011')
    sprite('ku405_04', 32767)	# 24-32790

    def upon_3():

        def upon_4():
            clearUponHandler(3)
            clearUponHandler(4)
            sendToLabel(0)
    label(0)
    sprite('ku405_05', 5)	# 32791-32795
    Unknown23026(0)
    ExitState()
    label(1)
    sprite('null', 1)	# 32796-32796
    Unknown23033(0)
    setGravity(2000)
    Unknown23026(0)
    sprite('ku020_07', 3)	# 32797-32799
    SFX_1('ku329')
    sprite('ku020_08', 4)	# 32800-32803
    sprite('ku020_07', 4)	# 32804-32807
    sprite('ku020_08', 4)	# 32808-32811
    Unknown13014(1)
    Unknown13008(1)
    Unknown13019(1)
    Unknown13015(1)
    Unknown13011(1)
    Unknown13012(1)
    label(2)
    sprite('ku020_07', 4)	# 32812-32815
    sprite('ku020_08', 4)	# 32816-32819
    loopRest()
    gotoLabel(2)

@State
def TVWarpB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2018(0, 2)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown11063(1)
        Unknown30068(1)
        Unknown23029(6, 5104, 0)

        def upon_STATE_END():
            Unknown23029(6, 5105, 0)
    sprite('ku405_00', 3)	# 1-3
    Unknown1084(1)
    sprite('ku405_01ex00', 3)	# 4-6
    Unknown23029(11, 511, 0)
    setGravity(0)
    Unknown1007(20000)
    sprite('ku405_00', 1)	# 7-7
    sprite('ku405_01ex01', 1)	# 8-8
    sprite('ku405_01ex02', 1)	# 9-9
    sprite('ku405_01ex03', 1)	# 10-10
    sprite('ku405_00ex04', 1)	# 11-11
    sprite('ku405_00ex06', 1)	# 12-12
    sprite('null', 1)	# 13-13
    sprite('null', 1)	# 14-14
    Unknown23151(6, 0)
    Unknown1084(1)
    setGravity(0)
    EnableCollision(0)
    Unknown1007(-31000)
    teleportRelativeX(-6500)
    sprite('ku405_02', 4)	# 15-18
    setInvincible(0)
    Unknown2006()
    if SLOT_64:
        SFX_1('pku211_2')
    sprite('ku405_03', 4)	# 19-22
    sprite('ku405_04', 32767)	# 23-32789
    EnableCollision(1)
    Unknown1047(80000)
    physicsYImpulse(2500)
    setGravity(4000)
    sendToLabelUpon(2, 0)
    label(0)
    sprite('ku123_02ex', 18)	# 32790-32807	 **attackbox here**
    Unknown13014(1)
    Unknown13008(1)
    Unknown13015(1)
    SFX_3('ku011')
    Unknown2018(1, 1)
    AttackLevel_(2)
    RefreshMultihit()
    teleportRelativeX(-60000)
    Unknown23026(0)
    sprite('ku123_02ex', 2)	# 32808-32809	 **attackbox here**
    Recovery()
    ExitState()

@State
def TVWarpEx_Front():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2018(0, 2)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown11063(1)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown30068(1)
        Unknown23029(7, 5104, 0)

        def upon_STATE_END():
            Unknown23029(7, 5105, 0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('ku405_00', 3)	# 1-3
    Unknown1084(1)
    sprite('ku405_01ex00', 3)	# 4-6
    Unknown23029(11, 511, 0)
    setGravity(0)
    Unknown1007(20000)
    sprite('ku405_00', 1)	# 7-7
    sprite('ku405_01ex01', 1)	# 8-8
    sprite('ku405_01ex02', 1)	# 9-9
    sprite('ku405_01ex03', 1)	# 10-10
    sprite('ku405_00ex04', 1)	# 11-11
    sprite('ku405_00ex06', 1)	# 12-12
    sprite('null', 1)	# 13-13
    sprite('null', 1)	# 14-14
    Unknown23151(6, 0)
    Unknown1084(1)
    setGravity(0)
    EnableCollision(0)
    Unknown1007(-28000)
    teleportRelativeX(-6500)
    sprite('ku405_02', 1)	# 15-15
    setInvincible(0)
    Unknown2006()
    if SLOT_64:
        SFX_1('pku211_2')
    sprite('ku405_03', 1)	# 16-16
    sprite('ku405_04', 32767)	# 17-32783
    EnableCollision(1)
    Unknown1047(80000)
    physicsYImpulse(2500)
    setGravity(4000)
    SFX_3('ku011')
    sendToLabelUpon(2, 0)
    label(0)
    sprite('ku123_02ex', 18)	# 32784-32801	 **attackbox here**
    Unknown13014(1)
    Unknown13008(1)
    Unknown13015(1)
    Unknown2018(1, 1)
    AttackLevel_(2)
    RefreshMultihit()
    teleportRelativeX(-60000)
    Unknown23026(0)
    sprite('ku123_02ex', 2)	# 32802-32803	 **attackbox here**
    Recovery()

@State
def TVWarpEx_Back():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2018(0, 2)
        Unknown23001(0, 0)
        Unknown23014()
        Unknown11063(1)
        Unknown30065(0)
        MinimumDamagePct(10)
        Unknown30068(1)
        Unknown23029(6, 5104, 0)

        def upon_STATE_END():
            Unknown23029(6, 5105, 0)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('ku405_00', 3)	# 1-3
    Unknown1084(1)
    sprite('ku405_01ex00', 3)	# 4-6
    Unknown23029(11, 511, 0)
    setGravity(0)
    Unknown1007(20000)
    sprite('ku405_00', 1)	# 7-7
    sprite('ku405_01ex01', 1)	# 8-8
    sprite('ku405_01ex02', 1)	# 9-9
    sprite('ku405_01ex03', 1)	# 10-10
    sprite('ku405_00ex04', 1)	# 11-11
    sprite('ku405_00ex06', 1)	# 12-12
    sprite('null', 1)	# 13-13
    EnableCollision(0)
    Unknown2015(40)
    teleportRelativeX(-15000)
    sprite('null', 1)	# 14-14
    Unknown23151(7, 0)
    Unknown1084(1)
    setGravity(0)
    Unknown1007(-28000)
    teleportRelativeX(7000)
    sprite('ku405_02', 1)	# 15-15
    setInvincible(0)
    Unknown2006()
    sprite('ku405_03', 1)	# 16-16
    EnableCollision(1)
    if SLOT_64:
        SFX_1('pku211_2')
    sprite('ku405_04', 32767)	# 17-32783
    Unknown1047(80000)
    physicsYImpulse(2500)
    setGravity(4000)
    SFX_3('ku011')
    sendToLabelUpon(2, 0)
    label(0)
    sprite('ku123_02ex', 18)	# 32784-32801	 **attackbox here**
    Unknown13014(1)
    Unknown13008(1)
    Unknown13015(1)
    Unknown2015(100)
    Unknown2018(1, 1)
    AttackLevel_(2)
    RefreshMultihit()
    teleportRelativeX(-60000)
    Unknown23026(0)
    sprite('ku123_02ex', 2)	# 32802-32803	 **attackbox here**
    Recovery()

@State
def ItemShootA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ku205_00', 3)	# 1-3
    sprite('ku205_01', 9)	# 4-12
    Unknown23029(11, 550, 0)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku205_02', 3)	# 13-15
    sprite('ku205_03', 3)	# 16-18
    GFX_1('persona_enter_ply', 0)
    sprite('ku205_04', 3)	# 19-21
    sprite('ku205_03', 3)	# 22-24
    sprite('ku205_04', 3)	# 25-27
    sprite('ku205_03', 3)	# 28-30
    sprite('ku205_03', 2)	# 31-32
    sprite('ku205_05', 2)	# 33-34

@State
def ItemShootB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ku205_00', 3)	# 1-3
    sprite('ku205_01', 20)	# 4-23
    Unknown23029(11, 551, 0)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku205_02', 4)	# 24-27
    sprite('ku205_03', 3)	# 28-30
    GFX_1('persona_enter_ply', 0)
    sprite('ku205_04', 3)	# 31-33
    sprite('ku205_03', 3)	# 34-36
    sprite('ku205_04', 2)	# 37-38
    sprite('ku205_03', 3)	# 39-41
    sprite('ku205_04', 3)	# 42-44
    sprite('ku205_03', 3)	# 45-47
    sprite('ku205_04', 3)	# 48-50
    sprite('ku205_03', 3)	# 51-53
    sprite('ku205_04', 3)	# 54-56
    sprite('ku205_03', 3)	# 57-59
    sprite('ku205_04', 3)	# 60-62
    sprite('ku205_03', 2)	# 63-64
    sprite('ku205_05', 2)	# 65-66

@State
def ItemShootEx():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ku205_00', 3)	# 1-3
    sprite('ku205_01', 22)	# 4-25
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 552, 0)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku205_02', 3)	# 26-28
    sprite('ku205_03', 3)	# 29-31
    GFX_1('persona_enter_ply', 0)
    sprite('ku205_04', 3)	# 32-34
    sprite('ku205_03', 3)	# 35-37
    sprite('ku205_04', 3)	# 38-40
    sprite('ku205_03', 3)	# 41-43
    sprite('ku205_05', 2)	# 44-45

@State
def AirItemShootA():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ku255_00', 3)	# 1-3
    sprite('ku255_01', 9)	# 4-12
    SLOT_9 = 1
    Unknown23029(11, 550, 0)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown22004(5, 0)
    sprite('ku255_02', 4)	# 13-16
    GFX_1('persona_enter_ply', 0)
    GFX_1('kuef_nagekiss_02', 0)
    sprite('ku255_03', 4)	# 17-20
    sprite('ku255_04', 4)	# 21-24
    sprite('ku255_03', 4)	# 25-28
    sprite('ku255_04', 4)	# 29-32
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    Recovery()
    sprite('ku255_05', 4)	# 33-36

@State
def AirItemShootB():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ku255_00', 3)	# 1-3
    sprite('ku255_01', 23)	# 4-26
    SLOT_9 = 1
    Unknown23029(11, 551, 0)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown22004(5, 0)
    sprite('ku255_02', 4)	# 27-30
    GFX_1('persona_enter_ply', 0)
    GFX_1('kuef_nagekiss_02', 0)
    sprite('ku255_03', 4)	# 31-34
    sprite('ku255_04', 4)	# 35-38
    sprite('ku255_03', 4)	# 39-42
    sprite('ku255_04', 4)	# 43-46
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    Recovery()
    sprite('ku255_05', 4)	# 47-50

@State
def AirItemShootEx():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ku255_00', 3)	# 1-3
    sprite('ku255_01', 25)	# 4-28
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    SLOT_9 = 1
    Unknown23029(11, 552, 0)
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown22004(5, 0)
    sprite('ku255_02', 4)	# 29-32
    GFX_1('persona_enter_ply', 0)
    GFX_1('kuef_nagekiss_02', 0)
    sprite('ku255_03', 4)	# 33-36
    sprite('ku255_04', 2)	# 37-38
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    Recovery()
    sprite('ku255_03', 4)	# 39-42
    sprite('ku255_04', 4)	# 43-46
    sprite('ku255_03', 4)	# 47-50
    sprite('ku255_05', 4)	# 51-54

@State
def UltimateMissile():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        sendToLabelUpon(2, 0)
        AttackP1(80)
        AttackP2(60)
        Unknown11092(1)
    sprite('ku430_00', 3)	# 1-3
    Unknown1084(1)
    Unknown2006()
    sprite('ku430_00', 1)	# 4-4
    tag_voice(1, 'pku251_0', 'pku251_1', '', '')
    sprite('ku430_01', 2)	# 5-6
    sprite('ku430_02', 3)	# 7-9
    Unknown2036(57, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsYImpulse(20000)
    Unknown23029(11, 600, 0)
    sprite('ku430_02', 30)	# 10-39
    physicsYImpulse(0)
    setGravity(0)
    sprite('ku430_03', 3)	# 40-42
    SFX_3('hit_m_slow')
    sprite('ku430_04', 3)	# 43-45
    sprite('ku430_05', 3)	# 46-48
    tag_voice(0, 'pku252_0', 'pku252_1', '', '')
    sprite('ku430_06', 3)	# 49-51
    sprite('ku430_05', 3)	# 52-54
    sprite('ku430_06', 3)	# 55-57
    sprite('ku430_05', 3)	# 58-60
    setInvincible(0)
    sprite('ku430_06', 3)	# 61-63
    sprite('ku430_05', 3)	# 64-66
    sprite('ku430_06', 3)	# 67-69
    sprite('ku430_05', 3)	# 70-72
    sprite('ku430_06', 3)	# 73-75
    sprite('ku430_05', 3)	# 76-78
    sprite('ku430_06', 3)	# 79-81
    sprite('ku430_05', 3)	# 82-84
    sprite('ku430_06', 3)	# 85-87
    sprite('ku430_05', 3)	# 88-90
    sprite('ku430_06', 3)	# 91-93
    sprite('ku430_05', 3)	# 94-96
    sprite('ku430_06', 3)	# 97-99
    sprite('ku430_05', 3)	# 100-102
    sprite('ku430_06', 3)	# 103-105
    sprite('ku430_05', 3)	# 106-108
    sprite('ku430_06', 3)	# 109-111
    sprite('ku430_05', 3)	# 112-114
    sprite('ku430_06', 3)	# 115-117
    sprite('ku430_07', 3)	# 118-120
    setGravity(2000)
    sprite('ku430_08', 32767)	# 121-32887
    label(0)
    sprite('ku430_09', 9)	# 32888-32896

@State
def UltimateMissileOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        sendToLabelUpon(2, 0)
    sprite('ku430_00', 3)	# 1-3
    Unknown1084(1)
    Unknown2006()
    sprite('ku430_00', 1)	# 4-4
    tag_voice(1, 'pku250_0', 'pku250_1', '', '')
    sprite('ku430_01', 2)	# 5-6
    sprite('ku430_02', 3)	# 7-9
    Unknown2036(57, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsYImpulse(20000)
    Unknown23029(11, 610, 0)
    sprite('ku430_02', 30)	# 10-39
    physicsYImpulse(0)
    setGravity(0)
    sprite('ku430_03', 3)	# 40-42
    SFX_3('hit_m_slow')
    sprite('ku430_04', 3)	# 43-45
    sprite('ku430_05', 3)	# 46-48
    SFX_1('ku325')
    sprite('ku430_06', 3)	# 49-51
    sprite('ku430_05', 3)	# 52-54
    sprite('ku430_06', 3)	# 55-57
    sprite('ku430_05', 3)	# 58-60
    setInvincible(0)
    sprite('ku430_06', 3)	# 61-63
    sprite('ku430_04', 3)	# 64-66
    sprite('ku430_03', 3)	# 67-69
    sprite('ku430_02', 10)	# 70-79
    sprite('ku430_03', 3)	# 80-82
    sprite('ku430_04', 3)	# 83-85
    tag_voice(0, 'pku252_0', '', '', '')
    sprite('ku430_05', 3)	# 86-88
    sprite('ku430_06', 3)	# 89-91
    sprite('ku430_05', 3)	# 92-94
    sprite('ku430_06', 3)	# 95-97
    sprite('ku430_05', 3)	# 98-100
    sprite('ku430_06', 3)	# 101-103
    sprite('ku430_05', 3)	# 104-106
    sprite('ku430_06', 3)	# 107-109
    sprite('ku430_05', 3)	# 110-112
    sprite('ku430_06', 3)	# 113-115
    sprite('ku430_05', 3)	# 116-118
    sprite('ku430_06', 3)	# 119-121
    sprite('ku430_05', 3)	# 122-124
    sprite('ku430_06', 3)	# 125-127
    sprite('ku430_05', 3)	# 128-130
    sprite('ku430_06', 3)	# 131-133
    sprite('ku430_05', 3)	# 134-136
    sprite('ku430_06', 3)	# 137-139
    sprite('ku430_05', 3)	# 140-142
    sprite('ku430_07', 3)	# 143-145
    setGravity(2000)
    sprite('ku430_08', 32767)	# 146-32912
    label(0)
    sprite('ku430_09', 9)	# 32913-32921

@State
def AirUltimateMissile():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
    sprite('ku430_00', 3)	# 1-3
    Unknown1084(1)
    setGravity(0)
    Unknown2006()
    sprite('ku430_01', 3)	# 4-6
    tag_voice(1, 'pku254_0', 'pku254_1', '', '')
    sprite('ku430_02', 3)	# 7-9
    Unknown2036(57, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown23029(11, 600, 0)
    sprite('ku430_02', 30)	# 10-39
    sprite('ku430_03', 3)	# 40-42
    SFX_3('hit_m_slow')
    sprite('ku430_04', 3)	# 43-45
    sprite('ku430_05', 3)	# 46-48
    sprite('ku430_06', 3)	# 49-51
    sprite('ku430_05', 3)	# 52-54
    sprite('ku430_06', 3)	# 55-57
    tag_voice(0, 'pku255_0', 'pku255_1', '', '')
    sprite('ku430_05', 3)	# 58-60
    setInvincible(0)
    sprite('ku430_06', 3)	# 61-63
    sprite('ku430_05', 3)	# 64-66
    sprite('ku430_06', 3)	# 67-69
    sprite('ku430_05', 3)	# 70-72
    sprite('ku430_06', 3)	# 73-75
    sprite('ku430_05', 3)	# 76-78
    sprite('ku430_06', 3)	# 79-81
    sprite('ku430_05', 3)	# 82-84
    sprite('ku430_06', 3)	# 85-87
    sprite('ku430_05', 3)	# 88-90
    sprite('ku430_06', 3)	# 91-93
    sprite('ku430_05', 3)	# 94-96
    sprite('ku430_06', 3)	# 97-99
    sprite('ku430_05', 3)	# 100-102
    sprite('ku430_06', 3)	# 103-105
    sprite('ku430_05', 3)	# 106-108
    sprite('ku430_06', 3)	# 109-111
    sprite('ku430_05', 3)	# 112-114
    sprite('ku430_06', 3)	# 115-117
    sprite('ku430_07', 3)	# 118-120
    setGravity(2000)
    sprite('ku430_08', 3)	# 121-123
    sprite('ku430_10', 3)	# 124-126

@State
def AirUltimateMissileOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
    sprite('ku430_00', 3)	# 1-3
    Unknown1084(1)
    Unknown2006()
    sprite('ku430_00', 1)	# 4-4
    tag_voice(1, 'pku253_0', 'pku253_1', '', '')
    sprite('ku430_01', 2)	# 5-6
    sprite('ku430_02', 3)	# 7-9
    Unknown2036(57, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    physicsYImpulse(20000)
    Unknown23029(11, 610, 0)
    sprite('ku430_02', 30)	# 10-39
    physicsYImpulse(0)
    setGravity(0)
    sprite('ku430_03', 3)	# 40-42
    SFX_3('hit_m_slow')
    sprite('ku430_04', 3)	# 43-45
    sprite('ku430_05', 3)	# 46-48
    sprite('ku430_06', 3)	# 49-51
    sprite('ku430_05', 3)	# 52-54
    sprite('ku430_06', 3)	# 55-57
    sprite('ku430_05', 3)	# 58-60
    setInvincible(0)
    sprite('ku430_06', 3)	# 61-63
    sprite('ku430_04', 3)	# 64-66
    sprite('ku430_03', 3)	# 67-69
    sprite('ku430_02', 10)	# 70-79
    sprite('ku430_03', 3)	# 80-82
    sprite('ku430_04', 3)	# 83-85
    tag_voice(0, 'pku255_0', 'pku255_1', '', '')
    sprite('ku430_05', 3)	# 86-88
    sprite('ku430_06', 3)	# 89-91
    sprite('ku430_05', 3)	# 92-94
    sprite('ku430_06', 3)	# 95-97
    sprite('ku430_05', 3)	# 98-100
    sprite('ku430_06', 3)	# 101-103
    sprite('ku430_05', 3)	# 104-106
    sprite('ku430_06', 3)	# 107-109
    sprite('ku430_05', 3)	# 110-112
    sprite('ku430_06', 3)	# 113-115
    sprite('ku430_05', 3)	# 116-118
    sprite('ku430_06', 3)	# 119-121
    sprite('ku430_05', 3)	# 122-124
    sprite('ku430_06', 3)	# 125-127
    sprite('ku430_05', 3)	# 128-130
    sprite('ku430_06', 3)	# 131-133
    sprite('ku430_05', 3)	# 134-136
    sprite('ku430_06', 3)	# 137-139
    sprite('ku430_05', 3)	# 140-142
    sprite('ku430_07', 3)	# 143-145
    setGravity(2000)
    sprite('ku430_08', 3)	# 146-148
    sprite('ku430_10', 3)	# 149-151

@State
def UltimateNihil():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        setInvincible(1)
        Damage(2800)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(42000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(600)
        blockstun(35)
        Unknown11001(10, 0, 0)
        Unknown9310(1)
        Hitstop(20)
        Unknown13024(0)
        MinimumDamagePct(10)
        Unknown11084(1)
        Unknown11068(1)
        Unknown11064(1)
        Unknown2073(1)
        Unknown11069('ShadowKuma')

        def upon_78():
            AirPushbackY(90000)
            enterState('UltimateUltimaChage')
            clearUponHandler(12)
    sprite('ku433_00', 3)	# 1-3
    Unknown2006()
    sprite('ku433_01', 3)	# 4-6
    GFX_1('kuef_433aura', 100)
    SFX_3('ku023')
    Unknown2036(62, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown1084(1)
    sprite('ku433_02', 3)	# 7-9
    sprite('ku433_01', 3)	# 10-12
    sprite('ku433_02', 3)	# 13-15
    Unknown7006('pku260_0', 100, 846556016, 828321846, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku433_01', 3)	# 16-18
    sprite('ku433_02', 3)	# 19-21
    sprite('ku433_01', 3)	# 22-24
    sprite('ku433_02', 3)	# 25-27
    sprite('ku433_01', 3)	# 28-30
    sprite('ku433_02', 3)	# 31-33
    sprite('ku433_01', 3)	# 34-36
    sprite('ku433_02', 3)	# 37-39
    sprite('ku433_01', 3)	# 40-42
    sprite('ku433_02', 3)	# 43-45
    sprite('ku433_01', 3)	# 46-48
    sprite('ku433_02', 3)	# 49-51
    sprite('ku433_01', 3)	# 52-54
    sprite('ku433_02', 3)	# 55-57
    sprite('ku433_01', 3)	# 58-60
    sprite('ku433_02', 3)	# 61-63
    sprite('ku433_03', 2)	# 64-65
    physicsXImpulse(38000)
    Unknown8007(100, 1, 1)
    sprite('ku433_03', 2)	# 66-67
    Unknown1019(80)
    sprite('ku433_03', 2)	# 68-69
    Unknown1019(80)
    sprite('ku433_03', 2)	# 70-71
    Unknown1019(80)
    SFX_3('hit_l_slow')
    GFX_0('kuef_433_upper', 100)
    GFX_1('kuef_433tornafe', 100)
    sprite('ku433_05', 4)	# 72-75	 **attackbox here**
    Unknown23054('6b753433335f303400000000000000000000000000000000000000000000000004000000')
    Unknown1019(0)
    RefreshMultihit()
    sprite('ku433_06', 20)	# 76-95
    Unknown7007('706b753236315f30000000000000000064000000706b753236315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    setInvincible(0)
    sprite('ku433_07', 40)	# 96-135
    sprite('ku433_08', 5)	# 136-140
    sprite('ku433_09', 5)	# 141-145
    sprite('ku433_10', 5)	# 146-150

@State
def UltimateUltimaChage():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown23083(1)
        setInvincible(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown23084(1)
        Unknown2054(1)
        Unknown13024(0)
        Unknown2004(1, 1)

        def upon_43():
            if (SLOT_48 == 6510):
                Unknown23084(0)
            if (SLOT_48 == 6511):
                sendToLabel(1)
            if (SLOT_48 == 6512):
                Unknown2038(1)
            if (SLOT_48 == 6513):
                SLOT_56 = 0
            if (SLOT_48 == 6521):
                Unknown13024(1)

            def upon_3():
                if (not SLOT_158):
                    Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006719000000000000')
                    Unknown2034(1)
                    Unknown2053(1)
    sprite('ku433_05', 10)	# 1-10	 **attackbox here**
    GFX_0('Nihil_Camera', 0)
    sprite('ku434_00', 30)	# 11-40	 **attackbox here**
    sprite('ku434_00', 11)	# 41-51	 **attackbox here**
    Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006419000000000000')
    sprite('ku434_01', 11)	# 52-62	 **attackbox here**
    GFX_0('ShadowKuma', 0)
    label(0)
    sprite('ku434_01', 12)	# 63-74	 **attackbox here**

    def upon_3():
        if SLOT_2:
            clearUponHandler(3)
            sendToLabel(1)
    sprite('ku434_02', 12)	# 75-86	 **attackbox here**
    sprite('ku434_03', 12)	# 87-98	 **attackbox here**
    sprite('ku434_04', 12)	# 99-110	 **attackbox here**
    sprite('ku434_03', 12)	# 111-122	 **attackbox here**
    sprite('ku434_02', 12)	# 123-134	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 135-144
    EnableCollision(1)
    setInvincible(0)
    sprite('ku434_05', 4)	# 145-148
    sprite('ku434_06', 23)	# 149-171

@State
def UltimateNihilOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        setInvincible(1)
        Damage(2800)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(8000)
        AirPushbackY(42000)
        YImpluseBeforeWallbounce(2000)
        AirUntechableTime(600)
        blockstun(35)
        Unknown11001(10, 0, 0)
        Unknown9310(1)
        Hitstop(20)
        Unknown13024(0)
        MinimumDamagePct(10)
        Unknown11084(1)
        Unknown11068(1)
        Unknown11064(1)
        Unknown2073(1)
        Unknown11069('ShadowKuma')

        def upon_78():
            AirPushbackY(90000)
            enterState('UltimateUltimaChageOD')
            clearUponHandler(12)
    sprite('ku433_00', 3)	# 1-3
    Unknown2006()
    sprite('ku433_01', 3)	# 4-6
    GFX_1('kuef_433aura', 100)
    SFX_3('ku023')
    Unknown2036(62, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown1084(1)
    sprite('ku433_02', 3)	# 7-9
    sprite('ku433_01', 3)	# 10-12
    sprite('ku433_02', 3)	# 13-15
    Unknown7006('pku260_0', 100, 846556016, 828321846, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku433_01', 3)	# 16-18
    sprite('ku433_02', 3)	# 19-21
    sprite('ku433_01', 3)	# 22-24
    sprite('ku433_02', 3)	# 25-27
    sprite('ku433_01', 3)	# 28-30
    sprite('ku433_02', 3)	# 31-33
    sprite('ku433_01', 3)	# 34-36
    sprite('ku433_02', 3)	# 37-39
    sprite('ku433_01', 3)	# 40-42
    sprite('ku433_02', 3)	# 43-45
    sprite('ku433_01', 3)	# 46-48
    sprite('ku433_02', 3)	# 49-51
    sprite('ku433_01', 3)	# 52-54
    sprite('ku433_02', 3)	# 55-57
    sprite('ku433_01', 3)	# 58-60
    sprite('ku433_02', 3)	# 61-63
    sprite('ku433_03', 2)	# 64-65
    physicsXImpulse(38000)
    Unknown8007(100, 1, 1)
    sprite('ku433_03', 2)	# 66-67
    Unknown1019(80)
    sprite('ku433_03', 2)	# 68-69
    Unknown1019(80)
    sprite('ku433_03', 2)	# 70-71
    Unknown1019(80)
    SFX_3('hit_l_slow')
    GFX_0('kuef_433_upper', 100)
    GFX_1('kuef_433tornafe', 100)
    sprite('ku433_05', 4)	# 72-75	 **attackbox here**
    Unknown23054('6b753433335f303400000000000000000000000000000000000000000000000004000000')
    Unknown1019(0)
    RefreshMultihit()
    sprite('ku433_06', 20)	# 76-95
    Unknown7007('706b753236315f30000000000000000064000000706b753236315f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    setInvincible(0)
    sprite('ku433_07', 40)	# 96-135
    sprite('ku433_08', 5)	# 136-140
    sprite('ku433_09', 5)	# 141-145
    sprite('ku433_10', 5)	# 146-150

@State
def UltimateUltimaChageOD():

    def upon_IMMEDIATE():
        Unknown17012(3, 0, 0)
        Unknown23056('')
        Unknown23083(1)
        setInvincible(1)
        EnableCollision(0)
        Unknown2034(0)
        Unknown23084(1)
        Unknown2054(1)
        Unknown13024(0)
        Unknown2004(1, 1)

        def upon_43():
            if (SLOT_48 == 6510):
                Unknown23084(0)
            if (SLOT_48 == 6511):
                sendToLabel(1)
            if (SLOT_48 == 6512):
                Unknown2038(1)
            if (SLOT_48 == 6513):
                SLOT_56 = 0
            if (SLOT_48 == 6521):
                Unknown13024(1)

        def upon_3():
            if (not SLOT_158):
                Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006719000000000000')
                Unknown2034(1)
                Unknown2053(1)
    sprite('ku433_05', 10)	# 1-10	 **attackbox here**
    GFX_0('Nihil_Camera', 0)
    sprite('ku434_00', 30)	# 11-40	 **attackbox here**
    sprite('ku434_00', 11)	# 41-51	 **attackbox here**
    Unknown21015('4e6968696c5f43616d65726100000000000000000000000000000000000000006419000000000000')
    sprite('ku434_01', 11)	# 52-62	 **attackbox here**
    GFX_0('ShadowKuma', 0)
    Unknown23029(1, 6520, 0)
    label(0)
    sprite('ku434_01', 12)	# 63-74	 **attackbox here**

    def upon_3():
        if SLOT_2:
            clearUponHandler(3)
            sendToLabel(1)
    sprite('ku434_02', 12)	# 75-86	 **attackbox here**
    sprite('ku434_03', 12)	# 87-98	 **attackbox here**
    sprite('ku434_04', 12)	# 99-110	 **attackbox here**
    sprite('ku434_03', 12)	# 111-122	 **attackbox here**
    sprite('ku434_02', 12)	# 123-134	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 135-144
    Unknown13024(1)
    EnableCollision(1)
    setInvincible(0)
    sprite('ku434_05', 4)	# 145-148
    sprite('ku434_06', 23)	# 149-171

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(5)
        Damage(27910)
        AirPushbackX(40000)
        AirPushbackY(50000)
        YImpluseBeforeWallbounce(0)
        Hitstop(0)
        MinimumDamagePct(100)
        Unknown11064(3)
        Unknown11056(3)
        Unknown21010(1)
        Unknown11023(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown9001(6)

        def upon_43():
            if (SLOT_48 == 7000):
                setInvincible(1)
                Unknown23083(1)
                Unknown23084(1)
                Unknown23088(1, 1)
                GFX_0('IchigekiCamera', 100)
                Unknown23157(1)
                sendToLabel(0)
        clearUponHandler(2)
        setInvincible(1)
        Unknown2021(1)
        Unknown1084(1)
    sprite('ku450_00', 4)	# 1-4
    Unknown2006()
    Unknown2005()
    sprite('ku450_01', 12)	# 5-16
    Unknown2036(50, -1, 2)
    Unknown23147()
    GFX_0('P4U_Cutin_Parent', 100)
    sprite('ku450_02', 6)	# 17-22
    physicsYImpulse(3000)
    setGravity(2000)
    sprite('ku450_00', 4)	# 23-26
    Unknown2005()
    sprite('ku450_01', 12)	# 27-38
    Unknown23029(11, 700, 0)
    sprite('ku450_03', 6)	# 39-44
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    physicsYImpulse(-4000)
    Unknown35()
    sprite('ku450_04', 10)	# 45-54
    physicsYImpulse(4000)
    setGravity(400)
    sprite('ku450_05', 4)	# 55-58
    setGravity(0)
    physicsYImpulse(0)
    sprite('ku450_06', 4)	# 59-62
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    tag_voice(1, 'pku290_0', 'pku290_1', '', '')
    SFX_3('persona_destroy')
    sprite('ku450_07', 10)	# 63-72
    sprite('ku450_07', 5)	# 73-77
    setInvincible(0)
    sprite('ku450_08', 6)	# 78-83
    setGravity(500)
    sprite('ku450_09', 30)	# 84-113
    sprite('ku450_09', 10)	# 114-123
    sprite('ku450_09', 1)	# 124-124
    sprite('ku450_09', 25)	# 125-149
    ExitState()
    label(0)
    sprite('ku450_08', 6)	# 150-155
    setGravity(500)
    sprite('ku450_09', 23)	# 156-178
    sprite('ku450_10', 6)	# 179-184
    setInvincible(1)
    sprite('ku450_11', 6)	# 185-190
    sprite('ku450_12', 20)	# 191-210
    physicsYImpulse(4000)
    setGravity(200)
    sprite('ku450_13', 3)	# 211-213
    GFX_0('Hanabidama', 0)
    Unknown1087(22, 11)
    Unknown36(22)
    Unknown1084(1)
    teleportRelativeX(20000)
    teleportRelativeY(5800000)
    setGravity(4200)
    Unknown35()
    SFX_3('hit_m_slow')
    sprite('ku450_14', 3)	# 214-216
    sprite('ku450_15', 12)	# 217-228
    setGravity(1000)
    sprite('ku450_16', 3)	# 229-231
    sprite('ku450_17', 25)	# 232-256
    sprite('ku450_18', 4)	# 257-260
    sprite('ku450_19', 30)	# 261-290
    tag_voice(0, 'pku291_0', 'pku291_1', '', '')
    sprite('ku450_20', 3)	# 291-293
    SFX_3('camera_flash')
    SFX_3('slap_fast')
    sprite('ku450_21', 3)	# 294-296
    sprite('ku450_22', 3)	# 297-299
    sprite('ku450_21', 3)	# 300-302
    sprite('ku450_22', 3)	# 303-305
    sprite('ku450_21', 3)	# 306-308
    sprite('ku450_22', 3)	# 309-311
    sprite('ku450_21', 3)	# 312-314
    sprite('ku450_22', 3)	# 315-317
    sprite('ku450_21', 3)	# 318-320
    sprite('ku450_22', 3)	# 321-323
    sprite('ku450_21', 3)	# 324-326
    sprite('ku450_22', 3)	# 327-329
    sprite('ku450_21', 3)	# 330-332
    sprite('ku450_22', 3)	# 333-335
    sprite('ku450_21', 3)	# 336-338
    sprite('ku450_22', 3)	# 339-341
    sprite('ku450_21', 3)	# 342-344
    sprite('ku450_22', 3)	# 345-347
    sprite('ku450_21', 3)	# 348-350
    sprite('ku450_22', 3)	# 351-353
    sprite('ku450_21', 3)	# 354-356
    sprite('ku450_22', 3)	# 357-359
    sprite('ku450_21', 3)	# 360-362
    sprite('ku450_22', 3)	# 363-365
    sprite('ku450_21', 3)	# 366-368
    sprite('ku450_22', 3)	# 369-371
    sprite('ku450_21', 3)	# 372-374
    sprite('ku450_22', 3)	# 375-377
    sprite('ku450_21', 3)	# 378-380
    sprite('ku450_22', 3)	# 381-383
    sprite('ku450_21', 3)	# 384-386
    sprite('ku450_22', 3)	# 387-389
    sprite('ku450_21', 3)	# 390-392
    sprite('ku450_22', 3)	# 393-395
    sprite('ku450_21', 3)	# 396-398
    sprite('ku450_22', 3)	# 399-401
    sprite('ku450_21', 3)	# 402-404
    sprite('ku450_22', 3)	# 405-407
    sprite('ku450_21', 3)	# 408-410
    sprite('ku450_22', 3)	# 411-413
    sprite('ku450_21', 3)	# 414-416
    sprite('ku450_22', 3)	# 417-419
    sprite('ku450_21', 3)	# 420-422
    sprite('ku450_22', 3)	# 423-425
    sprite('ku450_21', 3)	# 426-428
    GFX_0('450cutinsmoke', 0)
    sprite('ku450_22', 3)	# 429-431
    sprite('ku450_21', 3)	# 432-434
    sprite('ku450_22', 3)	# 435-437
    sprite('ku450_21', 3)	# 438-440
    sprite('ku450_22', 3)	# 441-443
    sprite('ku450_21', 3)	# 444-446
    sprite('ku450_22', 3)	# 447-449
    sprite('ku450_21', 3)	# 450-452
    sprite('ku450_22', 3)	# 453-455
    Unknown23024(3)
    sprite('ku450_21', 3)	# 456-458
    sprite('ku450_22', 3)	# 459-461
    sprite('ku450_21', 3)	# 462-464
    sprite('ku450_22', 3)	# 465-467
    GFX_0('Cutinbg', 100)
    sprite('ku450_21', 3)	# 468-470
    sprite('ku450_22', 3)	# 471-473
    GFX_0('IchigekiPictureA', 100)
    GFX_0('IchigekiPictureB', 100)
    sprite('ku450_dmy', 30)	# 474-503
    GFX_0('450kintokirocket', 0)
    sprite('ku450_dmy', 30)	# 504-533
    GFX_0('450rocketsmoke', 2)
    sprite('ku450_dmy', 90)	# 534-623
    tag_voice(0, 'pku292_0', 'pku292_1', '', '')
    sprite('ku450_dmy', 30)	# 624-653
    GFX_0('450kirari', 1)
    sprite('ku450_dmy', 40)	# 654-693
    GFX_0('450hanabiBG', 100)
    GFX_0('450kumahanabi', 0)
    SFX_3('ku009')
    sprite('null', 60)	# 694-753
    sprite('null', 40)	# 754-793
    sprite('null', 2)	# 794-795
    SFX_3('ku010')
    sprite('null', 2)	# 796-797
    SFX_3('bomb_m')
    sprite('null', 2)	# 798-799
    SFX_3('bomb_m')
    sprite('null', 54)	# 800-853
    tag_voice(0, 'pku293_0', 'pku293_1', '', '')
    SFX_3('bomb_m')
    sprite('dmy_atk', 60)	# 854-913
    RefreshMultihit()
    sprite('null', 65)	# 914-978
    sprite('null', 5)	# 979-983
    Unknown20006(1)
    Unknown23024(0)
    Unknown2034(0)
    Unknown1000(-450000)
    Unknown36(22)
    Unknown1000(0)
    physicsXImpulse(0)
    Unknown2034(0)
    Unknown35()
    Unknown21015('4963686967656b6943616d657261000000000000000000000000000000000000631b000000000000')
    sprite('ku450_23', 4)	# 984-987
    sprite('ku450_25', 4)	# 988-991
    sprite('ku450_26', 4)	# 992-995
    sprite('ku450_27', 4)	# 996-999
    sprite('ku450_26', 4)	# 1000-1003
    sprite('ku450_25', 4)	# 1004-1007
    sprite('ku450_23', 4)	# 1008-1011
    sprite('ku450_24', 4)	# 1012-1015
    sprite('ku450_23', 4)	# 1016-1019
    Unknown18010()
    Unknown20006(1)
    Unknown21011(180)
    Unknown2034(1)
    sprite('ku450_25', 4)	# 1020-1023
    sprite('ku450_26', 4)	# 1024-1027
    sprite('ku450_27', 4)	# 1028-1031
    sprite('ku450_26', 4)	# 1032-1035
    sprite('ku450_25', 4)	# 1036-1039
    Unknown23029(11, 7002, 0)
    sprite('ku450_23', 4)	# 1040-1043
    sprite('ku450_24', 4)	# 1044-1047
    sprite('ku450_23', 4)	# 1048-1051
    sprite('ku450_25', 4)	# 1052-1055
    sprite('ku450_26', 4)	# 1056-1059
    sprite('ku450_27', 4)	# 1060-1063
    sprite('ku450_26', 4)	# 1064-1067
    label(1)
    sprite('ku450_25', 4)	# 1068-1071
    sprite('ku450_23', 4)	# 1072-1075
    sprite('ku450_24', 4)	# 1076-1079
    sprite('ku450_23', 4)	# 1080-1083
    sprite('ku450_25', 4)	# 1084-1087
    sprite('ku450_26', 4)	# 1088-1091
    sprite('ku450_27', 4)	# 1092-1095
    sprite('ku450_26', 4)	# 1096-1099
    loopRest()
    gotoLabel(1)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        EnableCollision(0)
        Unknown2034(0)
        teleportRelativeY(0)
    label(0)
    sprite('null', 1)	# 1-1
    gotoLabel(0)

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 25)	# 1-25
    sprite('ku210_08', 32767)	# 26-32792	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-130000)
    Unknown1007(2400000)
    physicsYImpulse(-240000)
    setGravity(0)
    Unknown2053(1)
    EnableCollision(1)
    label(1)
    sprite('ku210_09ex01', 12)	# 32793-32804	 **attackbox here**
    Unknown1084(1)
    SFX_3('down_steal_m')
    GFX_1('kuef_groundshock_06', 0)
    ScreenShake(0, 10000)
    sprite('ku210_10', 6)	# 32805-32810
    sprite('ku210_11', 7)	# 32811-32817

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ku033_01', 3)	# 1-3
    sprite('ku033_02', 3)	# 4-6
    sprite('ku033_01', 3)	# 7-9
    sprite('ku033_02', 3)	# 10-12
    sprite('ku033_01', 3)	# 13-15
    sprite('ku033_02', 3)	# 16-18
    sprite('ku033_01', 3)	# 19-21
    sprite('ku033_02', 3)	# 22-24
    sprite('ku033_01', 3)	# 25-27
    sprite('ku033_02', 3)	# 28-30
    sprite('ku033_01', 30)	# 31-60

@State
def CmnActChangePartnerAppeal():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('ku205_00', 5)	# 1-5
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    sprite('ku205_01', 4)	# 6-9
    sprite('ku205_02', 4)	# 10-13
    sprite('ku205_03', 4)	# 14-17
    sprite('ku205_04', 4)	# 18-21
    sprite('ku205_05', 4)	# 22-25
    sprite('ku205_06', 4)	# 26-29
    sprite('ku205_04', 4)	# 30-33
    sprite('ku205_05', 4)	# 34-37
    sprite('ku205_06', 4)	# 38-41
    sprite('ku205_04', 4)	# 42-45
    sprite('ku205_05', 4)	# 46-49
    sprite('ku205_05', 4)	# 50-53
    sprite('ku205_06', 4)	# 54-57
    sprite('ku205_00', 5)	# 58-62

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        Unknown17015()

        def upon_3():
            if Unknown30042(25):
                Unknown2034(1)
            else:
                Unknown2034(0)
    sprite('ku045_00', 1)	# 1-1
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ku045_00', 3)	# 2-4
    sprite('ku045_01', 4)	# 5-8
    Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
    label(0)
    sprite('ku045_02', 5)	# 9-13
    sprite('ku045_03', 5)	# 14-18
    loopRest()
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
    gotoLabel(0)
    label(1)
    sprite('ku045_01', 6)	# 19-24
    sprite('ku045_00', 6)	# 25-30

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ku001_01', 6)	# 1-6
    sprite('ku001_02', 6)	# 7-12
    sprite('ku001_03', 8)	# 13-20
    sprite('ku001_04', 6)	# 21-26
    sprite('ku001_05', 6)	# 27-32
    sprite('ku001_01', 6)	# 33-38
    sprite('ku001_02', 6)	# 39-44
    sprite('ku001_03', 8)	# 45-52
    sprite('ku001_04', 6)	# 53-58
    sprite('ku001_05', 6)	# 59-64
    sprite('ku001_01', 6)	# 65-70
    sprite('ku001_02', 6)	# 71-76
    sprite('ku001_03', 8)	# 77-84
    sprite('ku001_04', 6)	# 85-90
    sprite('ku001_05', 6)	# 91-96
    sprite('ku001_00', 30)	# 97-126

@State
def CmnActChangePartnerQuickIn():
    sprite('ku032_05', 3)	# 1-3
    sprite('ku032_06', 5)	# 4-8
    sprite('ku032_09', 7)	# 9-15
    sprite('ku032_09', 7)	# 16-22
    sprite('ku032_10', 7)	# 23-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ku033_00', 1)	# 1-1
    sprite('ku033_01', 2)	# 2-3
    sprite('ku033_01', 2)	# 4-5
    sprite('ku033_02', 1)	# 6-6
    sprite('ku033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('ku033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ku033_03', 3)	# 13-15
    sprite('ku033_04', 3)	# 16-18

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
    sprite('ku020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ku020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ku010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()
        AttackP1(70)
        AttackP2(85)
        Unknown11092(1)
        sendToLabelUpon(2, 0)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ku430_00', 3)	# 1-3
    Unknown1084(1)
    Unknown2006()
    sprite('ku430_00', 1)	# 4-4
    sprite('ku430_01', 2)	# 5-6
    sprite('ku430_02', 3)	# 7-9
    physicsYImpulse(20000)
    Unknown23029(11, 611, 0)
    sprite('ku430_02', 10)	# 10-19
    physicsYImpulse(0)
    setGravity(0)
    sprite('ku430_03', 3)	# 20-22
    SFX_3('hit_m_slow')
    sprite('ku430_04', 3)	# 23-25
    sprite('ku430_05', 3)	# 26-28
    Unknown7007('706b753331325f30000000000000000064000000706b753331325f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    sprite('ku430_06', 3)	# 29-31
    sprite('ku430_05', 3)	# 32-34
    sprite('ku430_06', 3)	# 35-37
    sprite('ku430_05', 3)	# 38-40
    setInvincible(0)
    sprite('ku430_06', 3)	# 41-43
    sprite('ku430_05', 3)	# 44-46
    sprite('ku430_06', 3)	# 47-49
    sprite('ku430_05', 3)	# 50-52
    sprite('ku430_06', 3)	# 53-55
    sprite('ku430_05', 3)	# 56-58
    sprite('ku430_06', 3)	# 59-61
    sprite('ku430_05', 3)	# 62-64
    sprite('ku430_06', 3)	# 65-67
    sprite('ku430_05', 3)	# 68-70
    sprite('ku430_06', 3)	# 71-73
    sprite('ku430_05', 3)	# 74-76
    sprite('ku430_06', 3)	# 77-79
    sprite('ku430_07', 3)	# 80-82
    setGravity(2000)
    sprite('ku430_08', 32767)	# 83-32849
    label(0)
    sprite('ku430_09', 9)	# 32850-32858

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30039(24)
        Unknown30040(1)
        Unknown2006()
        Unknown11042(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('ku205_00', 3)	# 1-3
    sprite('ku205_01', 6)	# 4-9
    Unknown23029(11, 553, 0)
    Unknown7006('pku306_0', 100, 863333232, 828323376, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku205_02', 3)	# 10-12
    sprite('ku205_03', 3)	# 13-15
    GFX_1('persona_enter_ply', 0)
    sprite('ku205_04', 3)	# 16-18
    sprite('ku205_03', 3)	# 19-21
    sprite('ku205_04', 2)	# 22-23
    sprite('ku205_03', 3)	# 24-26
    sprite('ku205_04', 3)	# 27-29
    sprite('ku205_03', 3)	# 30-32
    sprite('ku205_04', 3)	# 33-35
    sprite('ku205_03', 3)	# 36-38
    sprite('ku205_04', 3)	# 39-41
    sprite('ku205_03', 3)	# 42-44
    sprite('ku205_04', 3)	# 45-47
    sprite('ku205_03', 3)	# 48-50
    sprite('ku205_04', 3)	# 51-53
    sprite('ku205_05', 2)	# 54-55

@State
def CmnActChangePartnerAssistAtk_C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(420)
        AttackP1(70)
        Unknown11092(1)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        Hitstop(1)
        hitstun(33)
        AirUntechableTime(70)
        blockstun(8)
        Unknown11001(3, 3, 3)
        Unknown11058('0100000000000000000000000000000000000000')
        AirPushbackX(6000)
        AirPushbackY(34000)
        Unknown9016(1)
        PushbackX(20000)
        setGravity(0)
        Unknown1084(1)
        Unknown11042(1)
        Unknown2006()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
        clearUponHandler(2)
        sendToLabelUpon(5, 1)

        def upon_11():
            sendToLabel(0)
    sprite('ku402_00', 2)	# 1-2
    sprite('ku402_01', 1)	# 3-3
    sprite('ku402_01', 3)	# 4-6
    Unknown7006('pku205_0', 100, 846556016, 828322864, 0, 0, 100, 846556016, 845100080, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ku402_02', 1)	# 7-7
    GFX_0('ScrewWind', 0)
    Unknown38(5, 1)
    sprite('ku402_03', 2)	# 8-9	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(37700)
    Unknown1007(50000)
    EnableCollision(0)
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 10-11	 **attackbox here**
    sprite('ku402_05', 2)	# 12-13	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 14-15	 **attackbox here**
    sprite('ku402_03', 2)	# 16-17	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_04', 2)	# 18-19	 **attackbox here**
    sprite('ku402_05', 2)	# 20-21	 **attackbox here**
    SFX_3('hit_l_middle')
    sprite('ku402_06', 2)	# 22-23	 **attackbox here**
    sprite('ku402_07', 2)	# 24-25
    Recovery()
    Unknown23029(5, 2000, 0)
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 26-28
    sprite('ku402_09', 3)	# 29-31
    loopRest()
    gotoLabel(1)
    label(0)
    sprite('ku402_04ex', 2)	# 32-33	 **attackbox here**
    clearUponHandler(11)
    physicsXImpulse(11000)
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 34-35	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 36-37	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_03ex', 2)	# 38-39	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_04ex', 2)	# 40-41	 **attackbox here**
    RefreshMultihit()
    sprite('ku402_05ex', 2)	# 42-43	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_l_middle')
    sprite('ku402_06ex', 2)	# 44-45	 **attackbox here**
    Unknown23029(5, 2000, 0)
    RefreshMultihit()
    sprite('ku402_03', 2)	# 46-47	 **attackbox here**
    physicsXImpulse(33000)
    DisableAttackRestOfMove()
    Recovery()
    sprite('ku402_04', 2)	# 48-49	 **attackbox here**
    sprite('ku402_05', 2)	# 50-51	 **attackbox here**
    sprite('ku402_06', 2)	# 52-53	 **attackbox here**
    sprite('ku402_07', 2)	# 54-55
    Unknown1019(60)
    EnableCollision(1)
    setGravity(2000)
    sprite('ku402_08', 3)	# 56-58
    sprite('ku402_09', 3)	# 59-61
    label(1)
    sprite('ku402_10', 2)	# 62-63
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ku402_11', 7)	# 64-70
    sprite('ku402_12', 3)	# 71-73
    sprite('ku402_13', 3)	# 74-76

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
    Unknown2036(115, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-180000)
    Unknown1019(4)
    label(0)
    sprite('ku020_07', 4)	# 3-6
    sprite('ku020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateGorogoroODDDD')
    else:
        enterState('UltimateGorogoroDDD')

@State
def UltimateGorogoroDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
        SLOT_51 = SLOT_83

        def upon_STATE_END():
            Unknown2053(1)
            Unknown2034(1)
            EnableCollision(1)
    sprite('ku432_00', 3)	# 1-3
    sprite('ku432_00', 2)	# 4-5
    sprite('ku432_01', 10)	# 6-15
    GFX_1('kuef_kira_03', 1)
    sprite('ku432_02', 4)	# 16-19
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    physicsYImpulse(-500)
    Unknown35()
    sprite('ku432_03', 4)	# 20-23
    physicsYImpulse(20000)
    setGravity(2500)
    GFX_0('kuef_432_Trampoline', 100)
    sprite('ku432_04', 4)	# 24-27
    sprite('ku432_05', 6)	# 28-33
    sprite('ku432_06', 32767)	# 34-32800
    sendToLabelUpon(2, 0)
    label(0)
    sprite('ku432_07', 2)	# 32801-32802
    GFX_0('UltimateGorogoroCamera', 100)
    clearUponHandler(2)
    sprite('ku432_07', 1)	# 32803-32803
    SFX_3('ku006')
    sprite('ku432_08', 8)	# 32804-32811
    loopRest()
    sprite('ku432_09', 2)	# 32812-32813
    physicsYImpulse(60000)
    SFX_3('persona_destroy')
    sprite('ku432_09', 5)	# 32814-32818
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    sprite('ku432_09', 5)	# 32819-32823
    SFX_3('ku007')
    sprite('null', 10)	# 32824-32833
    Unknown2053(0)
    Unknown2034(0)
    EnableCollision(0)
    sprite('ku432_10', 2)	# 32834-32835
    Unknown1084(1)
    teleportRelativeY(230000)
    teleportRelativeX(-1350000)
    physicsXImpulse(67500)
    setGravity(0)
    GFX_0('UltimateGorogoroTama', 100)
    Unknown38(10, 1)
    sprite('ku432_11', 2)	# 32836-32837
    sprite('ku432_12', 2)	# 32838-32839
    sprite('ku432_11', 2)	# 32840-32841
    SFX_3('ku007')
    Unknown7006('pku257_0', 100, 846556016, 828323637, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku432_11', 2)	# 32842-32843
    sprite('ku432_12', 2)	# 32844-32845
    sprite('ku432_11', 2)	# 32846-32847
    sprite('ku432_12', 2)	# 32848-32849
    sprite('ku432_11', 1)	# 32850-32850
    sprite('ku432_11', 1)	# 32851-32851
    Unknown23029(10, 6530, 0)
    sprite('ku432_12', 2)	# 32852-32853
    sprite('ku432_11', 2)	# 32854-32855
    sprite('ku432_12', 2)	# 32856-32857
    sprite('ku432_11', 2)	# 32858-32859
    sprite('ku432_12', 2)	# 32860-32861
    sprite('ku432_11', 2)	# 32862-32863
    sprite('ku432_12', 2)	# 32864-32865
    sprite('ku432_11', 2)	# 32866-32867
    sprite('ku432_12', 2)	# 32868-32869
    sprite('ku432_11', 2)	# 32870-32871
    sprite('ku432_12', 2)	# 32872-32873
    sprite('ku432_11', 2)	# 32874-32875
    sprite('null', 2)	# 32876-32877
    Unknown23029(10, 6531, 0)
    sprite('null', 1)	# 32878-32878
    Unknown1084(1)
    Unknown2053(1)
    Unknown2034(1)
    SLOT_83 = SLOT_51
    Unknown23033(0)
    setGravity(2000)
    loopRest()
    label(2)
    sprite('ku020_07', 3)	# 32879-32881
    sendToLabelUpon(2, 4)
    Unknown2006()
    setInvincible(0)
    sprite('ku020_08', 4)	# 32882-32885
    sprite('ku020_07', 4)	# 32886-32889
    sprite('ku020_08', 4)	# 32890-32893
    label(3)
    sprite('ku020_07', 4)	# 32894-32897
    sprite('ku020_08', 4)	# 32898-32901
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ku402_10', 5)	# 32902-32906
    sprite('ku402_11', 13)	# 32907-32919
    sprite('ku402_10', 7)	# 32920-32926

@State
def UltimateGorogoroODDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        setInvincible(1)
        SLOT_51 = SLOT_83

        def upon_43():
            if (SLOT_48 == 6533):
                SLOT_56 = 1

        def upon_STATE_END():
            Unknown2053(1)
            Unknown2034(1)
            EnableCollision(1)
    sprite('ku432_00', 3)	# 1-3
    sprite('ku432_00', 2)	# 4-5
    sprite('ku432_01', 10)	# 6-15
    GFX_1('kuef_kira_03', 1)
    sprite('ku432_02', 4)	# 16-19
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    physicsYImpulse(-500)
    Unknown35()
    sprite('ku432_03', 4)	# 20-23
    physicsYImpulse(20000)
    setGravity(2500)
    GFX_0('kuef_432_Trampoline', 100)
    sprite('ku432_04', 4)	# 24-27
    sprite('ku432_05', 6)	# 28-33
    sprite('ku432_06', 32767)	# 34-32800
    sendToLabelUpon(2, 0)
    label(0)
    sprite('ku432_07', 2)	# 32801-32802
    GFX_0('UltimateGorogoroCamera', 100)
    clearUponHandler(2)
    sprite('ku432_07', 1)	# 32803-32803
    SFX_3('ku006')
    sprite('ku432_08', 8)	# 32804-32811
    loopRest()
    sprite('ku432_09', 2)	# 32812-32813
    physicsYImpulse(60000)
    SFX_3('persona_destroy')
    sprite('ku432_09', 5)	# 32814-32818
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    sprite('ku432_09', 5)	# 32819-32823
    SFX_3('ku007')
    sprite('null', 10)	# 32824-32833
    Unknown2053(0)
    Unknown2034(0)
    EnableCollision(0)
    sprite('ku432_10', 2)	# 32834-32835
    Unknown1084(1)
    teleportRelativeY(230000)
    teleportRelativeX(-1350000)
    physicsXImpulse(67500)
    setGravity(0)
    GFX_0('UltimateGorogoroTama', 100)
    Unknown38(10, 1)
    Unknown23029(10, 6532, 0)
    sprite('ku432_11', 2)	# 32836-32837
    sprite('ku432_12', 2)	# 32838-32839
    sprite('ku432_11', 2)	# 32840-32841
    SFX_3('ku007')
    Unknown7006('pku257_0', 100, 846556016, 828323637, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku432_11', 2)	# 32842-32843
    sprite('ku432_12', 2)	# 32844-32845
    sprite('ku432_11', 2)	# 32846-32847
    sprite('ku432_12', 2)	# 32848-32849
    sprite('ku432_11', 1)	# 32850-32850
    sprite('ku432_11', 1)	# 32851-32851
    Unknown23029(10, 6530, 0)
    sprite('ku432_12', 2)	# 32852-32853
    sprite('ku432_11', 2)	# 32854-32855
    sprite('ku432_12', 2)	# 32856-32857
    sprite('ku432_11', 2)	# 32858-32859
    sprite('ku432_12', 2)	# 32860-32861
    sprite('ku432_11', 2)	# 32862-32863
    sprite('ku432_12', 2)	# 32864-32865
    sprite('ku432_11', 2)	# 32866-32867
    sprite('ku432_12', 2)	# 32868-32869
    loopRest()
    Unknown19(1, 2, 56)
    sprite('null', 25)	# 32870-32894
    Unknown1084(1)
    Unknown23029(10, 6534, 0)
    sprite('ku432_10', 2)	# 32895-32896
    SLOT_83 = SLOT_51
    Unknown2005()
    Unknown1084(1)
    teleportRelativeY(230000)
    teleportRelativeX(-1350000)
    physicsXImpulse(67500)
    setGravity(0)
    Unknown23029(10, 6535, 0)
    sprite('ku432_11', 2)	# 32897-32898
    sprite('ku432_12', 2)	# 32899-32900
    sprite('ku432_11', 2)	# 32901-32902
    SFX_3('ku007')
    sprite('ku432_11', 2)	# 32903-32904
    sprite('ku432_12', 2)	# 32905-32906
    sprite('ku432_11', 2)	# 32907-32908
    sprite('ku432_12', 2)	# 32909-32910
    sprite('ku432_11', 1)	# 32911-32911
    sprite('ku432_11', 1)	# 32912-32912
    sprite('ku432_12', 2)	# 32913-32914
    sprite('ku432_11', 2)	# 32915-32916
    sprite('ku432_12', 2)	# 32917-32918
    sprite('ku432_11', 2)	# 32919-32920
    sprite('ku432_12', 2)	# 32921-32922
    sprite('ku432_11', 2)	# 32923-32924
    sprite('ku432_12', 2)	# 32925-32926
    label(1)
    sprite('null', 3)	# 32927-32929
    clearUponHandler(78)
    Unknown23029(10, 6531, 0)
    sprite('null', 1)	# 32930-32930
    Unknown1084(1)
    Unknown2053(1)
    Unknown2034(1)
    SLOT_83 = SLOT_51
    Unknown23033(0)
    setGravity(2000)
    loopRest()
    label(2)
    sprite('ku020_07', 3)	# 32931-32933
    sendToLabelUpon(2, 4)
    Unknown2006()
    setInvincible(0)
    sprite('ku020_08', 4)	# 32934-32937
    sprite('ku020_07', 4)	# 32938-32941
    sprite('ku020_08', 4)	# 32942-32945
    label(3)
    sprite('ku020_07', 4)	# 32946-32949
    sprite('ku020_08', 4)	# 32950-32953
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ku402_10', 5)	# 32954-32958
    sprite('ku402_11', 18)	# 32959-32976
    sprite('ku402_10', 7)	# 32977-32983

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9015(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('ku210_08', 32767)	# 121-32887	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-100000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('ku210_09', 18)	# 32888-32905
    Unknown1084(1)
    SFX_3('down_steal_m')
    GFX_1('kuef_groundshock_06', 0)
    ScreenShake(0, 10000)
    sprite('ku210_10', 6)	# 32906-32911
    sprite('ku210_11', 7)	# 32912-32918

@State
def CmnActChangeReturnAppealBurst():
    sprite('ku600_13', 7)	# 1-7
    sprite('ku600_14', 7)	# 8-14
    sprite('ku600_13', 7)	# 15-21
    sprite('ku600_14', 20)	# 22-41
    sprite('ku010_02', 5)	# 42-46
    sprite('ku010_01', 5)	# 47-51
    sprite('ku010_00', 5)	# 52-56
    sprite('ku000_00', 30)	# 57-86

@Subroutine
def MouthTableInit():
    Unknown18011('pku000', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25396, 24887, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku520', 12897, 25392, 14385, 12897, 25392, 12849, 13409, 25400, 14388, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku521', 12641, 25397, 24886, 12849, 14435, 12641, 25397, 12339, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku522', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 14433, 14435, 13921, 13923, 12897, 25392, 12342, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku523', 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 14433, 13667, 24880, 25396, 24884, 25396, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku540', 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25395, 13362, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14689, 14691, 12641, 25397, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku541', 13665, 12899, 24880, 14388, 13411, 24885, 25400, 24888, 25400, 24888, 25400, 24888, 12339, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku542', 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25394, 14388, 13409, 13411, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku543', 13921, 13923, 13921, 13923, 13921, 13923, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25394, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku544', 12641, 25394, 12849, 14433, 13411, 24885, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku545', 12641, 25394, 12849, 14433, 13411, 24885, 13361, 12643, 24884, 13361, 12643, 24884, 13361, 12643, 24884, 13361, 12643, 24884, 13361, 12643, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku402_0', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku402_1', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku403_0', 12643, 12341, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pku403_1', 12643, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
        _gotolabel(2)
    sprite('ku600_00', 1)	# 2-2
    GFX_0('ToujouTVTaiki', 0)
    Unknown1007(1)
    Unknown23013(0)
    label(0)
    sprite('ku600_00', 6)	# 3-8
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    label(1)
    loopRest()
    sprite('ku600_00', 34)	# 9-42
    Unknown7006('pku522', 100, 896887664, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    if random_(2, 0, 50):
        SFX_1('pku522')
        SLOT_51 = 1
    else:
        SFX_1('pku523')
        SLOT_51 = 1
    Unknown23018(1)
    sprite('ku600_00', 1)	# 43-43
    Unknown23183('6b753630305f30300000000000000000000000000000000000000000000000000f0000000200000033000000')
    sprite('ku600_00', 6)	# 44-49
    Unknown26('ToujouTVTaiki')
    GFX_0('ToujouTV', 0)
    sprite('ku600_01', 6)	# 50-55
    Unknown1007(-10001)
    Unknown3001(255)
    sprite('ku600_02', 6)	# 56-61
    sprite('ku600_03', 6)	# 62-67
    SFX_0('wring_skin')
    sprite('ku600_04', 6)	# 68-73
    sprite('ku600_05', 15)	# 74-88
    sprite('ku600_06', 5)	# 89-93
    SFX_3('ku011')
    Unknown1007(30000)
    Unknown23013(1)
    sprite('ku600_07', 5)	# 94-98
    sprite('ku600_08', 3)	# 99-101
    Unknown1007(-20000)
    sprite('ku600_09', 3)	# 102-104
    sprite('ku600_10', 3)	# 105-107
    sprite('ku600_11', 16)	# 108-123
    sprite('ku600_12', 12)	# 124-135
    sprite('ku600_13', 7)	# 136-142
    sprite('ku600_14', 7)	# 143-149
    sprite('ku600_13', 7)	# 150-156
    sprite('ku600_14', 16)	# 157-172
    sprite('ku010_02', 6)	# 173-178
    sprite('ku010_01', 6)	# 179-184
    sprite('ku010_00', 6)	# 185-190
    teleportRelativeY(0)
    ExitState()
    label(2)
    sprite('null', 6)	# 191-196
    Unknown1000(-715000)
    Unknown2034(0)
    Unknown2053(0)

    def upon_STATE_END():
        Unknown2053(1)
        Unknown2034(1)
    label(3)
    sprite('null', 6)	# 197-202
    loopRest()
    if SLOT_17:
        _gotolabel(3)
    label(4)
    loopRest()
    sprite('ku601_00', 1)	# 203-203
    Unknown1000(-1965000)
    sprite('ku601_00', 1)	# 204-204
    Unknown1000(-1964000)
    sprite('ku601_00', 1)	# 205-205
    Unknown1000(-1963000)
    sprite('ku601_00', 1)	# 206-206
    Unknown1000(-1962000)
    sprite('ku601_00', 1)	# 207-207
    Unknown1000(-1961000)
    sprite('ku601_00', 1)	# 208-208
    Unknown1000(-1960000)
    sprite('ku601_00', 1)	# 209-209
    Unknown1000(-1959000)
    sprite('ku601_00', 1)	# 210-210
    Unknown1000(-1958000)
    sprite('ku601_00', 1)	# 211-211
    Unknown1000(-1957000)
    sprite('ku601_00', 1)	# 212-212
    Unknown1000(-1956000)
    sprite('ku601_00', 20)	# 213-232
    Unknown1000(-1955000)
    sprite('ku601_00', 50)	# 233-282
    Unknown7006('pku520', 100, 896887664, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ku601_00', 80)	# 283-362
    sprite('ku601_01', 8)	# 363-370
    sprite('ku601_02', 45)	# 371-415
    sprite('ku601_01', 8)	# 416-423
    sprite('ku601_00', 50)	# 424-473
    sprite('ku030_00', 3)	# 474-476
    physicsXImpulse(7500)
    sprite('ku030_01', 3)	# 477-479
    sprite('ku030_02', 3)	# 480-482
    sprite('ku030_03', 3)	# 483-485
    SFX_0('200_walk_normal_0')
    SFX_3('ku000')
    sprite('ku030_04', 3)	# 486-488
    sprite('ku030_05', 3)	# 489-491
    sprite('ku030_06', 3)	# 492-494
    sprite('ku030_07', 3)	# 495-497
    sprite('ku030_08', 3)	# 498-500
    SFX_0('200_walk_normal_0')
    SFX_3('ku000')
    sprite('ku030_09', 3)	# 501-503
    sprite('ku030_10', 3)	# 504-506
    sprite('ku030_11', 3)	# 507-509
    sprite('ku030_03', 3)	# 510-512
    SFX_0('200_walk_normal_0')
    SFX_3('ku000')
    sprite('ku030_04', 3)	# 513-515
    sprite('ku030_05', 3)	# 516-518
    sprite('ku030_06', 3)	# 519-521
    sprite('ku030_07', 3)	# 522-524
    sprite('ku030_08', 3)	# 525-527
    SFX_0('200_walk_normal_0')
    SFX_3('ku000')
    sprite('ku030_09', 3)	# 528-530
    sprite('ku030_10', 3)	# 531-533
    sprite('ku030_11', 3)	# 534-536
    sprite('ku030_03', 3)	# 537-539
    SFX_0('200_walk_normal_0')
    SFX_3('ku000')
    sprite('ku030_04', 3)	# 540-542
    sprite('ku030_05', 3)	# 543-545
    sprite('ku030_06', 3)	# 546-548
    sprite('ku030_07', 3)	# 549-551
    sprite('ku030_08', 3)	# 552-554
    SFX_0('200_walk_normal_0')
    SFX_3('ku000')
    sprite('ku030_09', 3)	# 555-557
    sprite('ku030_10', 3)	# 558-560
    sprite('ku030_03', 3)	# 561-563
    sprite('ku030_04', 3)	# 564-566
    sprite('ku030_05', 3)	# 567-569
    sprite('ku030_06', 3)	# 570-572
    physicsXImpulse(0)
    Unknown1000(-1230000)
    sprite('ku000_00', 20)	# 573-592
    sprite('ku601_03', 6)	# 593-598
    SFX_3('ku016')
    sprite('ku601_04', 6)	# 599-604
    GFX_1('kuef_flower_01', 0)
    sprite('ku601_05', 6)	# 605-610
    sprite('ku601_04', 6)	# 611-616
    GFX_1('kuef_flower_01', 0)
    sprite('ku601_03', 6)	# 617-622
    GFX_1('kuef_flower_01', 0)
    Unknown21011(60)
    ExitState()
    label(991)
    sprite('ku000_00', 1)	# 623-623
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ku000_00', 6)	# 624-629
    sprite('ku000_01', 6)	# 630-635
    sprite('ku000_02', 6)	# 636-641
    sprite('ku000_03', 6)	# 642-647
    sprite('ku000_04', 6)	# 648-653
    sprite('ku000_05', 6)	# 654-659
    sprite('ku000_00', 6)	# 660-665
    sprite('ku000_07', 6)	# 666-671
    sprite('ku000_08', 6)	# 672-677
    sprite('ku000_09', 6)	# 678-683
    sprite('ku000_10', 6)	# 684-689
    sprite('ku000_11', 6)	# 690-695
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
    if SLOT_108:
        _gotolabel(10)
    random_(2, 0, 2)
    if SLOT_0:
        _gotolabel(6)
    random_(2, 0, 33)
    if SLOT_0:
        _gotolabel(2)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(4)
    Unknown19(482, 2, 158)
    label(0)
    sprite('null', 1)	# 4-4
    sprite('null', 75)	# 5-79
    GFX_0('Win1', 100)
    sprite('null', 80)	# 80-159
    sprite('null', 180)	# 160-339
    Unknown7006('pku540', 100, 896887664, 12596, 0, 0, 100, 896887664, 12852, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('null', 32767)	# 340-33106
    label(2)
    sprite('ku611_00', 6)	# 33107-33112
    sprite('ku611_01', 6)	# 33113-33118
    SFX_0('cloth_m')
    sprite('ku611_02', 6)	# 33119-33124
    sprite('ku611_03', 6)	# 33125-33130
    sprite('ku611_04', 6)	# 33131-33136
    GFX_0('KiraKiraWin', 100)
    if SLOT_158:
        SFX_1('pku543')
    Unknown23018(1)
    sprite('ku611_05', 6)	# 33137-33142
    sprite('ku611_06', 6)	# 33143-33148
    sprite('ku611_07', 6)	# 33149-33154
    label(3)
    sprite('ku611_08', 6)	# 33155-33160
    sprite('ku611_09', 6)	# 33161-33166
    sprite('ku611_10', 6)	# 33167-33172
    loopRest()
    gotoLabel(3)
    label(4)
    sprite('ku611_11', 6)	# 33173-33178
    sprite('ku611_12', 6)	# 33179-33184
    sprite('ku611_13', 6)	# 33185-33190
    sprite('ku611_14', 6)	# 33191-33196
    sprite('ku611_15', 6)	# 33197-33202
    GFX_0('KiraKiraWin', 100)
    sprite('ku611_16', 6)	# 33203-33208
    sprite('ku611_17', 6)	# 33209-33214
    if SLOT_158:
        SFX_1('pku544')
    Unknown23018(1)
    sprite('ku611_18', 6)	# 33215-33220
    sprite('ku611_19', 6)	# 33221-33226
    sprite('ku611_20', 6)	# 33227-33232
    sprite('ku611_21', 6)	# 33233-33238
    sprite('ku611_19', 6)	# 33239-33244
    sprite('ku611_20', 6)	# 33245-33250
    sprite('ku611_21', 6)	# 33251-33256
    sprite('ku611_19', 6)	# 33257-33262
    sprite('ku611_19', 6)	# 33263-33268
    sprite('ku611_20', 6)	# 33269-33274
    sprite('ku611_21', 6)	# 33275-33280
    sprite('ku611_22', 4)	# 33281-33284
    sprite('ku611_23', 4)	# 33285-33288
    label(5)
    sprite('ku611_24', 6)	# 33289-33294
    sprite('ku611_25', 6)	# 33295-33300
    sprite('ku611_26', 6)	# 33301-33306
    loopRest()
    gotoLabel(5)
    label(6)
    sprite('ku611_27', 6)	# 33307-33312
    sprite('ku611_28', 6)	# 33313-33318
    sprite('ku611_29', 6)	# 33319-33324
    sprite('ku611_30', 6)	# 33325-33330
    sprite('ku611_31', 6)	# 33331-33336
    sprite('ku611_32', 6)	# 33337-33342
    sprite('ku611_33', 6)	# 33343-33348
    if SLOT_158:
        SFX_1('pku545')
    Unknown23018(1)
    GFX_0('KiraKiraWin', 100)
    label(7)
    sprite('ku611_34', 6)	# 33349-33354
    sprite('ku611_35', 6)	# 33355-33360
    sprite('ku611_36', 6)	# 33361-33366
    loopRest()
    gotoLabel(7)
    label(10)
    sprite('keep', 1)	# 33367-33367
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(11)
    sprite('ku010_00', 4)	# 33368-33371
    if SLOT_158:
        SFX_1('pku402_1')
    sprite('ku010_01', 4)	# 33372-33375
    sprite('ku010_02', 4)	# 33376-33379
    sprite('ku230_05', 5)	# 33380-33384
    Unknown23018(1)
    sprite('ku230_04', 32767)	# 33385-66151
    Unknown21011(280)
    label(11)
    sprite('ku208_14', 5)	# 66152-66156
    if SLOT_158:
        SFX_1('pku402_0')
    sprite('ku208_13', 5)	# 66157-66161
    sprite('ku208_12', 32767)	# 66162-98928
    Unknown21011(200)

@State
def CmnActLose():
    sprite('ku070_00', 6)	# 1-6
    Unknown7006('pku403_0', 100, 880110448, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ku070_01', 6)	# 7-12
    sprite('ku070_02', 2)	# 13-14
    sprite('ku070_03', 32767)	# 15-32781
