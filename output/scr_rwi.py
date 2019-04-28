@Subroutine
def PreInit():
    Unknown12019('72776900000000000000000000000000')
    Unknown12050(1)

@Subroutine
def CheckMagicCircleDistance():
    SLOT_47 = 0
    if SLOT_60:
        if Unknown46(4):
            Unknown59('04000000640000000300000064000000')
            if (SLOT_0 <= 200000):
                SLOT_59 = 1
                SLOT_47 = 1
        if Unknown46(5):
            Unknown59('05000000640000000300000064000000')
            if (SLOT_0 <= 200000):
                SLOT_59 = 2
                SLOT_47 = 1
        if Unknown46(6):
            Unknown59('06000000640000000300000064000000')
            if (SLOT_0 <= 200000):
                SLOT_59 = 3
                SLOT_47 = 1
        if Unknown46(7):
            Unknown59('07000000640000000300000064000000')
            if (SLOT_0 <= 200000):
                SLOT_59 = 4
                SLOT_47 = 1

@Subroutine
def MatchInit():
    DashFInitialVelocity(20000)
    DashFAccel(300)
    Unknown12024(2)
    Unknown13039(2)
    Unknown2049(1)
    Unknown15019(500)
    Unknown15018(500)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(1)
    Unknown15013(1500)
    Unknown15021(1500)
    Unknown14015(0, 500000, -200000, 250000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(1)
    Unknown15021(500)
    Unknown14015(0, 400000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4AA', 0x6)
    Unknown14005(1)
    Unknown14013('NmlAtk5AA')
    Unknown14015(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(3)
    Unknown15013(2000)
    Unknown14015(0, 300000, -100000, 150000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown15021(2000)
    Unknown15013(250)
    Unknown14015(0, 300000, -200000, 250000, 750, 10)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15021(2000)
    Unknown15012(1)
    Unknown14015(0, 350000, -200000, 250000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown15021(500)
    Unknown14015(0, 450000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    MoveMaxChainRepeat(1)
    Unknown15009()
    Unknown14015(0, 450000, -100000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(-100000, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5B')
    Unknown14015(-100000, 350000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR4A', 0xf)
    Unknown15003(0)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15013(2000)
    Unknown14015(-100000, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5BB', 0x22)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5A')
    Unknown14015(-100000, 400000, -100000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15014(1)
    Unknown14015(-150000, 300000, -250000, 200000, 500, 50)
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
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15016(0, 5, 15)
    Unknown14015(-50000, 400000, -150000, 200000, 250, 1)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15016(1, 1, 5)
    Unknown14015(-50000, 450000, -150000, 200000, 200, 1)
    Move_EndRegister()
    Move_Register('AssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(-50000, 450000, -150000, 200000, 150, 1)
    Move_EndRegister()
    Move_Register('AirAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-150000, 300000, -250000, 200000, 250, 1)
    Move_EndRegister()
    Move_Register('AirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown14015(-150000, 300000, -250000, 200000, 200, 1)
    Move_EndRegister()
    Move_Register('AirAssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown14015(-150000, 300000, -250000, 200000, 150, 1)
    Move_EndRegister()
    Move_Register('IceShieldA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_A)
    Unknown15006(0)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(800000, 2000000, -100000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('IceShieldB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_B)
    Unknown15006(0)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(1200000, 2000000, -100000, 200000, 150, 0)
    Move_EndRegister()
    Move_Register('IceShieldC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_22)
    Move_Input_(INPUT_PRESS_C)
    Unknown15006(0)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-200000, 200000, -100000, 200000, 200, 0)
    Move_EndRegister()
    Move_Register('SetMagicA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15016(0, 25, 35)
    Unknown14015(300000, 800000, -200000, 800000, 0, 250)
    Move_EndRegister()
    Move_Register('SetMagicB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15021(1)
    Unknown14015(300000, 800000, -200000, 800000, 0, 250)
    Move_EndRegister()
    Move_Register('SetMagicC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15000(0)
    Move_EndRegister()
    Move_Register('ExLandAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x93)
    Move_Input_(0x1)
    Unknown14024('CheckMagicCircleDistance')
    Unknown15008()
    Unknown15005(100000)
    Unknown15012(2000)
    Unknown15006(5000)
    Move_EndRegister()
    Move_Register('ExAirAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(0x93)
    Move_Input_(0x1)
    Unknown14024('CheckMagicCircleDistance')
    Unknown15008()
    Unknown15005(100000)
    Unknown15012(2000)
    Unknown15006(5000)
    Move_EndRegister()
    Move_Register('ExLandAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x93)
    Move_Input_(0xa)
    Unknown14024('CheckMagicCircleDistance')
    Unknown15005(100000)
    Unknown15014(4000)
    Unknown15006(5000)
    Move_EndRegister()
    Move_Register('ExAirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(0x93)
    Move_Input_(0xa)
    Unknown14024('CheckMagicCircleDistance')
    Unknown15005(100000)
    Unknown15014(4000)
    Unknown15006(5000)
    Move_EndRegister()
    Move_Register('ExLandAssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(0x93)
    Move_Input_(0x13)
    Unknown14024('CheckMagicCircleDistance')
    Unknown15005(100000)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown15006(5000)
    Move_EndRegister()
    Move_Register('ExAirAssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(0x93)
    Move_Input_(0x13)
    Unknown14024('CheckMagicCircleDistance')
    Unknown15005(100000)
    Unknown15012(2000)
    Unknown15013(2000)
    Unknown15006(5000)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-150000, 150000, -100000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateShotSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(700000, 1500000, -200000, 200000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateRush', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 450000, -200000, 150000, 150, 0)
    Move_EndRegister()
    Move_Register('UltimateRushSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(10000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 450000, -200000, 150000, 150, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(20000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 450000, -200000, 150000, 100, 0)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'AssaultA', 10000000)
    Unknown15024('NmlAtk5AAA', 'AssaultB', 10000000)
    Unknown15024('NmlAtk5AAA', 'SetMagicA', 10000000)
    Unknown15024('NmlAtk5AAA', 'SetMagicB', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4AA', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'FJump', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2C', 'AssaultA', 10000000)
    Unknown15024('NmlAtk2C', 'SetMagicA', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5C', 'AirAssaultA', 10000000)
    Unknown15024('AssaultA', 'ExLandAssaultC', 10000000)
    Unknown15024('AirAssaultA', 'ExLandAssaultC', 10000000)
    Unknown12018(0, 'rwi062_01')
    Unknown12018(1, 'rwi062_03')
    Unknown12018(2, 'rwi062_04')
    Unknown12018(3, 'rwi062_05')
    Unknown12018(4, 'rwi062_06')
    Unknown12018(5, 'rwi062_07')
    Unknown12018(6, 'rwi062_09')
    Unknown12018(7, 'rwi040_02')
    Unknown12018(8, 'rwi040_02')
    Unknown12018(9, 'rwi045_02')
    Unknown12018(10, 'rwi062_00')
    Unknown12018(11, 'rwi062_01')
    Unknown12018(12, 'rwi062_03')
    Unknown12018(13, 'rwi062_05')
    Unknown12018(14, 'rwi062_09')
    Unknown12018(15, 'rwi073_01ex01')
    Unknown12018(16, 'rwi050_00')
    Unknown12018(17, 'rwi052_00')
    Unknown12018(18, 'rwi054_00')
    Unknown12018(19, 'rwi000_00')
    Unknown12018(20, 'rwi000_00')
    Unknown12018(25, 'rwi063_00')
    Unknown12018(26, 'rwi063_01')
    Unknown12018(27, 'rwi063_02')
    Unknown12018(28, 'rwi063_04')
    Unknown12018(29, 'rwi063_09')
    Unknown12018(24, 'rwi073_01')
    Unknown7010(0, 'rwi000')
    Unknown7010(1, 'rwi001')
    Unknown7010(2, 'rwi002')
    Unknown7010(3, 'rwi003')
    Unknown7010(4, 'rwi004')
    Unknown7010(5, 'rwi005')
    Unknown7010(6, 'rwi006')
    Unknown7010(7, 'rwi007')
    Unknown7010(8, 'rwi008')
    Unknown7010(9, 'rwi009')
    Unknown7010(10, 'rwi010')
    Unknown7010(15, 'rwi015')
    Unknown7010(16, 'rwi016')
    Unknown7010(17, 'rwi017')
    Unknown7010(18, 'rwi018')
    Unknown7010(19, 'rwi019')
    Unknown7010(20, 'rwi020')
    Unknown7010(21, 'rwi021')
    Unknown7010(22, 'rwi022')
    Unknown7010(23, 'rwi023')
    Unknown7010(24, 'rwi024')
    Unknown7010(25, 'rwi025')
    Unknown7010(28, 'rwi028')
    Unknown7010(29, 'rwi029')
    Unknown7010(30, 'rwi030')
    Unknown7010(31, 'rwi031')
    Unknown7010(32, 'rwi032')
    Unknown7010(33, 'rwi033')
    Unknown7010(34, 'rwi034')
    Unknown7010(35, 'rwi035')
    Unknown7010(36, 'rwi036')
    Unknown7010(37, 'rwi037')
    Unknown7010(39, 'rwi039')
    Unknown7010(42, 'rwi042')
    Unknown7010(43, 'rwi043')
    Unknown7010(44, 'rwi044')
    Unknown7010(45, 'rwi045')
    Unknown7010(46, 'rwi046')
    Unknown7010(47, 'rwi047')
    Unknown7010(48, 'rwi048')
    Unknown7010(49, 'rwi049')
    Unknown7010(50, 'rwi050')
    Unknown7010(52, 'rwi052')
    Unknown7010(53, 'rwi053')
    Unknown7010(54, 'rwi100_0')
    Unknown7010(55, 'rwi100_1')
    Unknown7010(56, 'rwi100_2')
    Unknown7010(63, 'rwi101_0')
    Unknown7010(64, 'rwi101_1')
    Unknown7010(65, 'rwi101_2')
    Unknown7010(57, 'rwi102_0')
    Unknown7010(58, 'rwi102_1')
    Unknown7010(59, 'rwi102_2')
    Unknown7010(66, 'rwi103_0')
    Unknown7010(67, 'rwi103_1')
    Unknown7010(68, 'rwi103_2')
    Unknown7010(60, 'rwi104_0')
    Unknown7010(61, 'rwi104_1')
    Unknown7010(62, 'rwi104_2')
    Unknown7010(69, 'rwi105_0')
    Unknown7010(70, 'rwi105_1')
    Unknown7010(71, 'rwi105_2')
    Unknown7010(72, 'rwi150')
    Unknown7010(73, 'rwi151')
    Unknown7010(74, 'rwi152')
    Unknown7010(85, 'rwi153')
    Unknown7010(88, 'rwi156')
    Unknown7010(94, 'rwi401_0')
    Unknown7010(95, 'rwi401_1')
    Unknown7010(96, 'rwi162_0')
    Unknown7010(97, 'rwi162_1')
    Unknown7010(98, 'rwi164_0')
    Unknown7010(99, 'rwi164_1')
    Unknown7010(100, 'rwi165_0')
    Unknown7010(101, 'rwi165_1')
    Unknown7010(102, 'rwi167_0')
    Unknown7010(103, 'rwi167_1')
    Unknown7010(92, 'rwi163_0')
    Unknown7010(93, 'rwi163_1')
    Unknown7010(90, 'rwi168_0')
    Unknown7010(91, 'rwi168_1')
    Unknown7010(105, 'rwi166_0')
    Unknown7010(106, 'rwi166_1')
    Unknown7010(107, 'rwi169_0')
    Unknown7010(108, 'rwi169_1')
    Unknown7010(110, 'rwi170_0')
    Unknown7010(111, 'rwi170_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3241000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746553686f745350000000000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465527573685350000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnFrameStep():
    if (not SLOT_21):
        callSubroutine('AllDeleteMagicCircle')

@State
def CmnActStand():
    label(0)
    sprite('rwi000_00', 6)	# 1-6
    sprite('rwi000_01', 6)	# 7-12
    sprite('rwi000_02', 6)	# 13-18
    sprite('rwi000_03', 6)	# 19-24
    sprite('rwi000_04', 6)	# 25-30
    sprite('rwi000_05', 6)	# 31-36
    sprite('rwi000_06', 6)	# 37-42
    sprite('rwi000_07', 6)	# 43-48
    sprite('rwi000_08', 6)	# 49-54
    sprite('rwi000_09', 6)	# 55-60
    sprite('rwi000_10', 6)	# 61-66
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('rwi001_00', 6)	# 67-72
    SLOT_88 = 960
    SFX_1('rwi000')
    sprite('rwi001_01', 6)	# 73-78
    sprite('rwi001_02', 6)	# 79-84
    sprite('rwi001_03', 6)	# 85-90
    sprite('rwi001_04', 30)	# 91-120
    sprite('rwi001_03', 6)	# 121-126
    sprite('rwi001_02', 6)	# 127-132
    sprite('rwi001_01', 6)	# 133-138
    sprite('rwi001_00', 6)	# 139-144
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('rwi003_00', 3)	# 1-3
    sprite('rwi003_01', 3)	# 4-6
    sprite('rwi003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('rwi010_00', 4)	# 1-4
    sprite('rwi010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('rwi010_02', 6)	# 1-6
    sprite('rwi010_03', 6)	# 7-12
    sprite('rwi010_04', 6)	# 13-18
    sprite('rwi010_05', 6)	# 19-24
    sprite('rwi010_06', 6)	# 25-30
    sprite('rwi010_07', 6)	# 31-36
    sprite('rwi010_06', 6)	# 37-42
    sprite('rwi010_05', 6)	# 43-48
    sprite('rwi010_04', 6)	# 49-54
    sprite('rwi010_03', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('rwi013_00', 3)	# 1-3
    sprite('rwi013_01', 3)	# 4-6
    sprite('rwi013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('rwi010_01', 4)	# 1-4
    sprite('rwi010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('rwi010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    sprite('rwi020_00', 3)	# 1-3
    Unknown7006('rwi002', 25, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('rwi020_01', 3)	# 4-6
    label(0)
    sprite('rwi020_00', 3)	# 7-9
    sprite('rwi020_01', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('rwi020_02', 3)	# 1-3
    sprite('rwi020_03', 3)	# 4-6
    sprite('rwi020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('rwi020_05', 3)	# 1-3
    sprite('rwi020_06', 3)	# 4-6
    label(0)
    sprite('rwi020_07', 3)	# 7-9
    sprite('rwi020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('rwi010_01', 2)	# 1-2
    sprite('rwi010_00', 2)	# 3-4

@State
def CmnActLandingStiffLoop():
    sprite('rwi010_01', 4)	# 1-4
    sprite('rwi010_00', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('rwi010_00', 3)	# 1-3
    sprite('rwi010_00', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('ny030_00', 7)	# 1-7
    label(0)
    sprite('ny030_01', 7)	# 8-14
    SFX_3('GG2_218SE')
    GFX_1('nyef_ny030', -1)
    sprite('ny030_02', 7)	# 15-21
    GFX_1('nyef_ny030', -1)
    sprite('ny030_03', 7)	# 22-28
    GFX_1('nyef_ny030', -1)
    sprite('ny030_04', 7)	# 29-35
    GFX_1('nyef_ny030', -1)
    sprite('ny030_05', 7)	# 36-42
    GFX_1('nyef_ny030', -1)
    sprite('ny030_06', 7)	# 43-49
    GFX_1('nyef_ny030', -1)
    sprite('ny030_07', 7)	# 50-56
    GFX_1('nyef_ny030', -1)
    sprite('ny030_08', 7)	# 57-63
    GFX_1('nyef_ny030', -1)
    sprite('ny030_09', 7)	# 64-70
    GFX_1('nyef_ny030', -1)
    sprite('ny030_10', 7)	# 71-77
    GFX_1('nyef_ny030', -1)
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('rwi031_00', 7)	# 1-7
    sprite('rwi031_01', 7)	# 8-14
    label(0)
    sprite('rwi031_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rwi031_03', 7)	# 22-28
    sprite('rwi031_04', 7)	# 29-35
    sprite('rwi031_05', 7)	# 36-42
    sprite('rwi031_06', 7)	# 43-49
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('rwi031_07', 7)	# 50-56
    sprite('rwi031_08', 7)	# 57-63
    sprite('rwi031_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('rwi032_00', 3)	# 1-3
    sprite('rwi032_01', 3)	# 4-6
    label(0)
    sprite('rwi032_02', 4)	# 7-10
    sprite('rwi032_03', 4)	# 11-14
    sprite('rwi032_04', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('rwi032_05', 4)	# 19-22
    sprite('rwi032_06', 4)	# 23-26
    sprite('rwi032_07', 4)	# 27-30
    sprite('rwi032_08', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('rwi032_09', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('rwi032_10', 3)	# 1-3
    sprite('rwi032_11', 3)	# 4-6
    sprite('rwi032_12', 3)	# 7-9
    sprite('rwi032_13', 3)	# 10-12
    sprite('rwi032_14', 3)	# 13-15

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
    sprite('rwi033_00', 2)	# 1-2
    sprite('rwi033_01', 2)	# 3-4
    SFX_3('rgse_00')
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('rwi033_02', 2)	# 5-6
    loopRest()
    label(0)
    sprite('rwi033_01', 2)	# 7-8
    sprite('rwi033_02', 2)	# 9-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rwi033_03', 3)	# 11-13
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rwi033_04', 3)	# 14-16

@State
def CmnActBDashLanding():
    sprite('ny033_05', 4)	# 1-4
    sprite('ny033_06', 4)	# 5-8

@State
def CmnActAirFDash():
    sprite('rwi035_00', 2)	# 1-2
    Unknown7006('rwi004', 25, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('rwi035_01', 3)	# 3-5
    sprite('rwi035_02', 3)	# 6-8
    sprite('rwi035_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('rwi033_00', 3)	# 1-3
    Unknown7006('rwi006', 25, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('rwi033_01', 3)	# 4-6
    sprite('rwi033_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('rwi050_00', 1)	# 1-1
    sprite('rwi050_01', 1)	# 2-2
    sprite('rwi050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('rwi050_01', 1)	# 1-1
    sprite('rwi050_02', 1)	# 2-2
    sprite('rwi050_01', 2)	# 3-4
    sprite('rwi050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('rwi050_02', 1)	# 1-1
    sprite('rwi050_02', 1)	# 2-2
    sprite('rwi050_02', 2)	# 3-4
    sprite('rwi050_01', 2)	# 5-6
    sprite('rwi050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('rwi050_02', 1)	# 1-1
    sprite('rwi050_03', 1)	# 2-2
    sprite('rwi050_02', 2)	# 3-4
    sprite('rwi050_02', 2)	# 5-6
    sprite('rwi050_01', 2)	# 7-8
    sprite('rwi050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('rwi050_03', 1)	# 1-1
    sprite('rwi050_03', 1)	# 2-2
    sprite('rwi050_03', 2)	# 3-4
    sprite('rwi050_02', 2)	# 5-6
    sprite('rwi050_02', 2)	# 7-8
    sprite('rwi050_01', 2)	# 9-10
    sprite('rwi050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('rwi052_00', 1)	# 1-1
    sprite('rwi052_01', 1)	# 2-2
    sprite('rwi052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('rwi052_01', 1)	# 1-1
    sprite('rwi052_02', 1)	# 2-2
    sprite('rwi052_01', 2)	# 3-4
    sprite('rwi052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('rwi052_02', 1)	# 1-1
    sprite('rwi052_02', 1)	# 2-2
    sprite('rwi052_02', 2)	# 3-4
    sprite('rwi052_01', 2)	# 5-6
    sprite('rwi052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('rwi052_02', 1)	# 1-1
    sprite('rwi052_03', 1)	# 2-2
    sprite('rwi052_02', 2)	# 3-4
    sprite('rwi052_02', 2)	# 5-6
    sprite('rwi052_01', 2)	# 7-8
    sprite('rwi052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('rwi052_03', 1)	# 1-1
    sprite('rwi052_03', 1)	# 2-2
    sprite('rwi052_03', 2)	# 3-4
    sprite('rwi052_02', 2)	# 5-6
    sprite('rwi052_02', 2)	# 7-8
    sprite('rwi052_01', 2)	# 9-10
    sprite('rwi052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('rwi054_00', 1)	# 1-1
    sprite('rwi054_01', 1)	# 2-2
    sprite('rwi054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('rwi054_01', 1)	# 1-1
    sprite('rwi054_02', 1)	# 2-2
    sprite('rwi054_01', 2)	# 3-4
    sprite('rwi054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('rwi054_02', 1)	# 1-1
    sprite('rwi054_02', 1)	# 2-2
    sprite('rwi054_02', 2)	# 3-4
    sprite('rwi054_01', 2)	# 5-6
    sprite('rwi054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('rwi054_02', 1)	# 1-1
    sprite('rwi054_03', 1)	# 2-2
    sprite('rwi054_02', 2)	# 3-4
    sprite('rwi054_02', 2)	# 5-6
    sprite('rwi054_01', 2)	# 7-8
    sprite('rwi054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('rwi054_03', 1)	# 1-1
    sprite('rwi054_03', 1)	# 2-2
    sprite('rwi054_03', 2)	# 3-4
    sprite('rwi054_02', 2)	# 5-6
    sprite('rwi054_02', 2)	# 7-8
    sprite('rwi054_01', 2)	# 9-10
    sprite('rwi054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('rwi062_00', 3)	# 1-3
    label(0)
    sprite('rwi062_01', 3)	# 4-6
    sprite('rwi062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('rwi062_03', 2)	# 1-2
    sprite('rwi062_04', 2)	# 3-4

@State
def CmnActBDownDown():
    sprite('rwi062_05', 3)	# 1-3
    sprite('rwi062_06', 3)	# 4-6
    label(0)
    sprite('rwi062_07', 3)	# 7-9
    sprite('rwi062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('rwi062_09', 2)	# 1-2
    sprite('rwi062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('ny060_09', 2)	# 1-2
    sprite('ny060_10', 2)	# 3-4
    sprite('ny060_11', 2)	# 5-6
    sprite('ny060_12', 3)	# 7-9
    sprite('ny060_13', 3)	# 10-12

@State
def CmnActBDownLoop():
    sprite('ny060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('ny061_00', 3)	# 1-3
    SFX_0('205_runjump_garden_0')
    SFX_3('nyse_03')
    sprite('ny061_01', 3)	# 4-6
    sprite('ny061_02', 3)	# 7-9
    sprite('ny061_03', 3)	# 10-12
    sprite('ny061_04', 3)	# 13-15
    sprite('ny061_05', 3)	# 16-18
    sprite('ny061_06', 3)	# 19-21
    sprite('ny061_07', 3)	# 22-24
    sprite('ny061_08', 2)	# 25-26
    sprite('ny061_09', 2)	# 27-28

@State
def CmnActFDownUpper():
    sprite('rwi063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('rwi063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('rwi063_02', 3)	# 1-3
    sprite('rwi063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('rwi063_04', 3)	# 1-3
    sprite('rwi063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('rwi063_06', 4)	# 1-4
    sprite('rwi063_07', 3)	# 5-7
    sprite('rwi063_08', 3)	# 8-10
    sprite('rwi063_09', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('rwi063_09', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('rwi064_00', 2)	# 1-2
    sprite('rwi064_01', 3)	# 3-5
    sprite('rwi064_02', 3)	# 6-8
    sprite('rwi064_03', 3)	# 9-11
    sprite('rwi064_04', 3)	# 12-14
    sprite('rwi064_05', 3)	# 15-17
    sprite('rwi064_06', 3)	# 18-20

@State
def CmnActVDownUpper():
    sprite('rwi062_00', 3)	# 1-3
    label(0)
    sprite('rwi062_01', 3)	# 4-6
    sprite('rwi062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('rwi062_03', 2)	# 1-2
    sprite('rwi062_04', 2)	# 3-4

@State
def CmnActVDownDown():
    sprite('rwi062_05', 3)	# 1-3
    sprite('rwi062_06', 3)	# 4-6
    label(0)
    sprite('rwi062_07', 3)	# 7-9
    sprite('rwi062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('rwi063_04', 3)	# 1-3
    sprite('rwi063_05', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('rwi072_00', 3)	# 1-3
    label(0)
    sprite('rwi072_01', 3)	# 4-6
    sprite('rwi072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('rwi074_00', 3)	# 1-3
    sprite('rwi074_01', 3)	# 4-6
    sprite('rwi074_02', 3)	# 7-9
    sprite('rwi074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('ny082_00', 2)	# 1-2
    sprite('ny082_00', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('rwi062_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('rwi073_00', 3)	# 1-3
    sprite('rwi073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('rwi073_02', 3)	# 1-3
    sprite('rwi073_03', 3)	# 4-6
    label(0)
    sprite('rwi063_02', 3)	# 7-9
    sprite('rwi063_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('rwi070_00', 3)	# 1-3
    label(0)
    sprite('rwi070_01', 4)	# 4-7
    sprite('rwi070_02', 4)	# 8-11
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('rwi070_03', 4)	# 1-4
    sprite('rwi070_04', 4)	# 5-8
    sprite('rwi070_05', 4)	# 9-12
    sprite('rwi070_06', 4)	# 13-16
    sprite('rwi070_07', 4)	# 17-20
    sprite('rwi070_08', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('rwi070_09', 4)	# 1-4
    sprite('rwi070_10', 2)	# 5-6
    sprite('rwi070_11', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('rwi113_00', 3)	# 1-3
    sprite('rwi113_01', 3)	# 4-6
    sprite('rwi113_02', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('rwi113_00', 3)	# 1-3
    sprite('rwi113_01', 3)	# 4-6
    sprite('rwi113_02', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('rwi113_00', 3)	# 1-3
    sprite('rwi113_01', 3)	# 4-6
    sprite('rwi113_02', 9)	# 7-15

@State
def CmnActUkemiLandF():
    sprite('ny110_00', 2)	# 1-2
    sprite('ny110_01', 2)	# 3-4
    sprite('ny110_02', 2)	# 5-6
    sprite('ny110_03', 2)	# 7-8
    sprite('ny110_04', 2)	# 9-10
    sprite('ny110_05', 2)	# 11-12
    sprite('ny110_06', 2)	# 13-14
    sprite('ny110_07', 2)	# 15-16
    sprite('ny110_08', 200)	# 17-216
    sprite('ny110_09', 3)	# 217-219
    sprite('ny110_10', 3)	# 220-222

@State
def CmnActUkemiLandB():
    sprite('ny111_00', 3)	# 1-3
    sprite('ny111_01', 3)	# 4-6
    sprite('ny111_02', 3)	# 7-9
    sprite('ny111_03', 3)	# 10-12
    sprite('ny111_04', 3)	# 13-15
    sprite('ny111_06', 3)	# 16-18
    sprite('ny111_07', 200)	# 19-218
    sprite('ny111_08', 2)	# 219-220
    sprite('ny111_09', 2)	# 221-222
    sprite('ny111_10', 2)	# 223-224

@State
def CmnActUkemiLandN():
    sprite('rwi112_00', 2)	# 1-2
    sprite('rwi112_01', 2)	# 3-4
    sprite('rwi112_02', 2)	# 5-6
    sprite('rwi112_03', 2)	# 7-8
    sprite('rwi112_04', 2)	# 9-10
    sprite('rwi112_05', 2)	# 11-12
    sprite('rwi112_06', 2)	# 13-14
    sprite('rwi112_07', 2)	# 15-16
    sprite('rwi112_08', 2)	# 17-18
    sprite('rwi112_09', 2)	# 19-20
    label(0)
    sprite('rwi020_07', 3)	# 21-23
    sprite('rwi020_08', 3)	# 24-26
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('rwi010_00', 5)	# 1-5
    sprite('rwi010_01', 5)	# 6-10
    sprite('rwi010_00', 5)	# 11-15

@State
def CmnActMidGuardPre():
    sprite('rwi040_00', 3)	# 1-3
    sprite('rwi040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('rwi040_02', 3)	# 1-3
    sprite('rwi040_03', 3)	# 4-6
    sprite('rwi040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('rwi040_01', 3)	# 1-3
    sprite('rwi040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('rwi040_02', 3)	# 1-3
    sprite('rwi040_03', 3)	# 4-6
    sprite('rwi040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('rwi040_01', 3)	# 1-3
    sprite('rwi040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('rwi040_00', 3)	# 1-3
    sprite('rwi040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('rwi040_02', 3)	# 1-3
    sprite('rwi040_03', 3)	# 4-6
    sprite('rwi040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('rwi040_01', 3)	# 1-3
    sprite('rwi040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('rwi040_02', 3)	# 1-3
    sprite('rwi040_03', 3)	# 4-6
    sprite('rwi040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('rwi040_01', 3)	# 1-3
    sprite('rwi040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('rwi043_00', 3)	# 1-3
    sprite('rwi043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('rwi043_02', 3)	# 1-3
    sprite('rwi043_03', 3)	# 4-6
    sprite('rwi043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('rwi043_01', 3)	# 1-3
    sprite('rwi043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('rwi043_02', 3)	# 1-3
    sprite('rwi043_03', 3)	# 4-6
    sprite('rwi043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('rwi043_01', 3)	# 1-3
    sprite('rwi043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('rwi045_00', 3)	# 1-3
    sprite('rwi045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('rwi045_02', 3)	# 1-3
    sprite('rwi045_03', 3)	# 4-6
    sprite('rwi045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('rwi045_01', 3)	# 1-3
    sprite('rwi045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('rwi045_02', 3)	# 1-3
    sprite('rwi045_03', 3)	# 4-6
    sprite('rwi045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('rwi045_01', 3)	# 1-3
    sprite('rwi045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('rwi040_04', 2)	# 1-2
    sprite('rwi040_04', 2)	# 3-4
    sprite('rwi040_04', 1)	# 5-5
    Unknown2042(1)
    Unknown21012('72776965663331305f676c79706800000000000000000000000000000000000029000000')
    sprite('rwi040_02', 4)	# 6-9
    sprite('rwi040_01', 4)	# 10-13
    sprite('rwi040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('rwi043_04', 2)	# 1-2
    sprite('rwi043_04', 2)	# 3-4
    sprite('rwi043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('rwi043_02', 4)	# 6-9
    sprite('rwi043_01', 4)	# 10-13
    sprite('rwi043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('rwi045_04', 2)	# 1-2
    sprite('rwi045_04', 2)	# 3-4
    sprite('rwi045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('rwi045_02', 4)	# 6-9
    sprite('rwi045_01', 4)	# 10-13
    sprite('rwi045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('rwi025_00', 4)	# 1-4
    sprite('rwi025_01', 4)	# 5-8
    sprite('rwi025_00ex01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('rwi312_00', 5)	# 1-5
    GFX_0('rwief312_Glyph', -1)
    sprite('rwi312_01', 2)	# 6-7
    sprite('rwi312_02', 4)	# 8-11	 **attackbox here**
    sprite('rwi312_03', 4)	# 12-15
    sprite('rwi312_04', 4)	# 16-19
    sprite('rwi312_05', 3)	# 20-22
    sprite('rwi312_06', 3)	# 23-25

@State
def CmnActAirLockWait():
    sprite('ny045_02', 1)	# 1-1
    sprite('ny045_01', 3)	# 2-4
    sprite('ny045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('null', 3)	# 1-3

@State
def CmnActLandSpin():
    sprite('ny071_00', 3)	# 1-3
    sprite('ny071_01', 3)	# 4-6
    sprite('ny071_02', 3)	# 7-9
    label(0)
    sprite('ny071_03', 2)	# 10-11
    sprite('ny071_04', 2)	# 12-13
    sprite('ny071_05', 2)	# 14-15
    sprite('ny071_06', 2)	# 16-17
    sprite('ny071_07', 2)	# 18-19
    sprite('ny071_08', 2)	# 20-21
    sprite('ny071_09', 2)	# 22-23
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('ny071_10', 6)	# 1-6
    sprite('ny071_11', 5)	# 7-11
    sprite('ny071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('ny071_03', 2)	# 1-2
    sprite('ny071_04', 2)	# 3-4
    sprite('ny071_05', 2)	# 5-6
    sprite('ny071_06', 2)	# 7-8
    sprite('ny071_07', 2)	# 9-10
    sprite('ny071_08', 2)	# 11-12
    sprite('ny071_09', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('rwi077_00', 2)	# 1-2
    sprite('rwi077_01', 2)	# 3-4
    sprite('rwi077_00ex00', 2)	# 5-6
    sprite('rwi077_01ex00', 2)	# 7-8
    sprite('rwi077_00ex01', 2)	# 9-10
    sprite('rwi077_01ex01', 2)	# 11-12
    sprite('rwi077_00ex02', 2)	# 13-14
    sprite('rwi077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('rwi077_02', 4)	# 1-4
    label(0)
    sprite('rwi077_03', 3)	# 5-7
    sprite('rwi077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('rwi077_05', 5)	# 1-5
    sprite('rwi077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('ny060_07', 3)	# 1-3
    label(0)
    sprite('ny060_08', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('ny060_11', 4)	# 1-4
    sprite('ny060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('ny331_00', 2)	# 1-2
    label(0)
    sprite('ny331_01', 3)	# 3-5
    sprite('ny331_02', 3)	# 6-8
    sprite('ny331_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('ny331_04', 2)	# 1-2
    label(0)
    sprite('ny331_05', 3)	# 3-5
    sprite('ny331_06', 3)	# 6-8
    sprite('ny331_07', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('ny331_08', 2)	# 1-2
    sprite('ny331_09', 2)	# 3-4
    sprite('ny331_10', 2)	# 5-6

@State
def CmnActAirBurstBegin():
    sprite('ny332_00', 2)	# 1-2
    label(0)
    sprite('ny332_01', 3)	# 3-5
    sprite('ny332_02', 3)	# 6-8
    sprite('ny332_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('ny332_04', 2)	# 1-2
    label(0)
    sprite('ny332_05', 3)	# 3-5
    sprite('ny332_06', 3)	# 6-8
    sprite('ny332_07', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('ny332_08', 3)	# 1-3
    sprite('ny332_09', 3)	# 4-6
    sprite('ny332_10', 3)	# 7-9
    sprite('ny020_04', 3)	# 10-12
    sprite('ny020_05', 3)	# 13-15
    label(0)
    sprite('ny020_06', 4)	# 16-19
    sprite('ny020_07', 4)	# 20-23
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('rwi333_00', 3)	# 1-3
    sprite('rwi333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('rwi333_02', 3)	# 1-3
    label(0)
    sprite('rwi333_03', 3)	# 4-6
    sprite('rwi333_04', 3)	# 7-9
    sprite('rwi333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('rwi333_06', 4)	# 5-8
    sprite('rwi333_07', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('rwi333_08', 3)	# 1-3
    sprite('rwi333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('rwi333_02', 3)	# 1-3
    label(0)
    sprite('rwi333_03', 3)	# 4-6
    sprite('rwi333_04', 3)	# 7-9
    sprite('rwi333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('rwi333_09', 4)	# 5-8
    sprite('rwi333_10', 4)	# 9-12
    sprite('rwi020_04', 3)	# 13-15
    sprite('rwi020_05', 3)	# 16-18
    sprite('rwi020_06', 3)	# 19-21
    label(0)
    sprite('rwi020_07', 3)	# 22-24
    sprite('rwi020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('rwi333_00', 3)	# 1-3
    sprite('rwi333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('rwi333_02', 3)	# 1-3
    label(0)
    sprite('rwi333_03', 3)	# 4-6
    sprite('rwi333_04', 3)	# 7-9
    sprite('rwi333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('rwi333_06', 4)	# 5-8
    sprite('rwi333_07', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('rwi333_08', 3)	# 1-3
    sprite('rwi333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('rwi333_02', 3)	# 1-3
    label(0)
    sprite('rwi333_03', 3)	# 4-6
    sprite('rwi333_04', 3)	# 7-9
    sprite('rwi333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('rwi333_09', 4)	# 5-8
    sprite('rwi333_10', 4)	# 9-12
    sprite('rwi020_04', 3)	# 13-15
    sprite('rwi020_05', 3)	# 16-18
    sprite('rwi020_06', 3)	# 19-21
    label(0)
    sprite('rwi020_07', 3)	# 22-24
    sprite('rwi020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('rwi333_00', 3)	# 1-3
    sprite('rwi333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('rwi333_02', 3)	# 1-3
    label(0)
    sprite('rwi333_03', 3)	# 4-6
    sprite('rwi333_04', 3)	# 7-9
    sprite('rwi333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('rwi333_06', 3)	# 1-3
    sprite('rwi333_07', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('rwi333_08', 3)	# 1-3
    sprite('rwi333_01', 32767)	# 4-32770
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('rwi333_02', 3)	# 1-3
    label(0)
    sprite('rwi333_03', 3)	# 4-6
    sprite('rwi333_04', 3)	# 7-9
    sprite('rwi333_05', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('rwi333_09', 3)	# 1-3
    sprite('rwi333_10', 3)	# 4-6
    sprite('rwi020_04', 3)	# 7-9
    sprite('rwi020_05', 3)	# 10-12
    sprite('rwi020_06', 3)	# 13-15
    label(0)
    sprite('rwi020_07', 3)	# 16-18
    sprite('rwi020_08', 3)	# 19-21
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        Unknown2017(0)
        Unknown2034(0)
        teleportRelativeY(0)
        if SLOT_170:
            callSubroutine('AllDeleteMagicCircle')
        if Unknown46(8):
            Unknown23029(8, 4051, 0)
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
        Unknown23027()

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 25)	# 1-25
    sprite('null', 1)	# 26-26
    Unknown1086(22)
    teleportRelativeX(-1650000)
    teleportRelativeY(1000000)
    physicsXImpulse(150000)
    physicsYImpulse(-100000)
    setGravity(0)
    label(0)
    sprite('rwi408_03', 3)	# 27-29	 **attackbox here**
    sprite('rwi408_04', 3)	# 30-32	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('keep', 3)	# 33-35
    Unknown1019(30)
    sprite('rwi408_05', 3)	# 36-38
    Unknown1019(50)
    Unknown8000(100, 1, 1)
    sprite('rwi408_06', 3)	# 39-41
    Unknown1019(50)
    sprite('rwi408_07', 3)	# 42-44
    Unknown1019(50)
    sprite('rwi408_08', 3)	# 45-47
    Unknown1019(50)
    sprite('rwi408_09', 4)	# 48-51
    Unknown1084(1)
    sprite('rwi408_10', 3)	# 52-54
    sprite('rwi408_11', 3)	# 55-57

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rwi033_01', 3)	# 1-3
    sprite('rwi033_02', 3)	# 4-6
    sprite('rwi033_01', 3)	# 7-9
    sprite('rwi033_02', 3)	# 10-12
    sprite('rwi033_01', 3)	# 13-15
    sprite('rwi033_02', 3)	# 16-18
    sprite('rwi033_01', 3)	# 19-21
    sprite('rwi033_02', 3)	# 22-24
    sprite('rwi033_01', 3)	# 25-27
    sprite('rwi033_02', 3)	# 28-30
    sprite('rwi033_01', 30)	# 31-60

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('rwi611_00', 6)	# 1-6
    sprite('rwi611_01', 6)	# 7-12
    sprite('rwi611_02', 6)	# 13-18
    sprite('rwi611_03', 4)	# 19-22
    sprite('rwi611_04', 6)	# 23-28
    sprite('rwi611_05', 25)	# 29-53
    sprite('rwi611_03', 6)	# 54-59
    sprite('rwi611_02', 6)	# 60-65
    sprite('rwi611_01', 6)	# 66-71
    sprite('rwi611_00', 6)	# 72-77

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
            Unknown2015(-1)
            Unknown23087(-1)
            sendToLabel(2)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 10)	# 121-130
    sprite('null', 1)	# 131-131
    Unknown1086(22)
    teleportRelativeX(-2200000)
    Unknown1007(400000)
    setGravity(1000)
    physicsXImpulse(100000)
    physicsYImpulse(-7000)
    sprite('rwi408_03', 3)	# 132-134	 **attackbox here**
    Unknown2015(300)
    Unknown23087(100000)
    sprite('rwi408_04', 3)	# 135-137	 **attackbox here**
    sprite('rwi408_03', 3)	# 138-140	 **attackbox here**
    sprite('rwi408_04', 3)	# 141-143	 **attackbox here**
    label(1)
    sprite('rwi408_03', 3)	# 144-146	 **attackbox here**
    sprite('rwi408_04', 3)	# 147-149	 **attackbox here**
    gotoLabel(1)
    label(2)
    sprite('rwi408_05', 4)	# 150-153
    Unknown1019(30)
    Unknown8000(100, 1, 1)
    sprite('rwi408_06', 4)	# 154-157
    Unknown1019(50)
    sprite('rwi408_07', 4)	# 158-161
    Unknown1019(50)
    sprite('rwi408_08', 4)	# 162-165
    Unknown1019(50)
    sprite('rwi408_09', 4)	# 166-169
    Unknown1084(1)
    sprite('rwi408_10', 4)	# 170-173
    sprite('rwi408_11', 4)	# 174-177

@State
def CmnActChangeReturnAppealBurst():
    sprite('rwi010_01', 2)	# 1-2
    sprite('rwi010_00', 2)	# 3-4
    sprite('rwi000_00', 3)	# 5-7
    sprite('rwi300_00', 6)	# 8-13
    sprite('rwi300_01', 6)	# 14-19
    sprite('rwi300_02', 6)	# 20-25
    sprite('rwi300_03', 6)	# 26-31
    sprite('rwi300_04', 6)	# 32-37
    sprite('rwi300_05', 6)	# 38-43
    sprite('rwi300_06', 6)	# 44-49
    sprite('rwi300_07', 6)	# 50-55
    sprite('rwi300_08', 6)	# 56-61
    sprite('rwi300_06', 6)	# 62-67
    sprite('rwi300_07', 6)	# 68-73
    sprite('rwi300_08', 6)	# 74-79
    sprite('rwi300_06', 6)	# 80-85
    sprite('rwi300_07', 6)	# 86-91
    sprite('rwi300_08', 6)	# 92-97
    sprite('rwi300_09', 6)	# 98-103
    sprite('rwi300_10', 6)	# 104-109
    loopRest()

@State
def CmnActChangePartnerQuickIn():
    sprite('rwi032_07', 3)	# 1-3
    sprite('rwi032_08', 3)	# 4-6
    sprite('rwi032_09', 3)	# 7-9
    sprite('rwi032_10', 4)	# 10-13
    sprite('rwi032_11', 4)	# 14-17
    sprite('rwi032_12', 4)	# 18-21
    sprite('rwi032_13', 4)	# 22-25
    sprite('rwi032_14', 4)	# 26-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('rwi033_00', 3)	# 1-3
    sprite('rwi033_01', 2)	# 4-5
    sprite('rwi033_01', 1)	# 6-6
    sprite('rwi033_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('rwi033_01', 3)	# 10-12
    sprite('rwi033_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rwi033_03', 3)	# 16-18
    sprite('rwi033_04', 3)	# 19-21

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
    sprite('rwi020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('rwi020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('rwi010_01', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('rwi406_00', 3)	# 1-3
    sprite('rwi406_01', 3)	# 4-6
    sprite('rwi406_02', 3)	# 7-9
    tag_voice(1, 'rwi208_0', 'rwi208_1', 'rwi208_2', '')
    sprite('rwi406_03', 3)	# 10-12
    sprite('rwi406_04', 3)	# 13-15
    sprite('rwi406_05', 3)	# 16-18
    sprite('rwi406_06', 3)	# 19-21
    sprite('rwi406_07', 3)	# 22-24
    sprite('rwi406_08', 3)	# 25-27
    GFX_0('InstallationMagic', -1)
    Unknown23029(1, 4065, 0)
    sprite('rwi406_09', 3)	# 28-30
    Recovery()
    sprite('rwi406_10', 4)	# 31-34
    sprite('rwi406_11', 4)	# 35-38
    sprite('rwi406_12', 4)	# 39-42
    sprite('rwi406_10', 4)	# 43-46
    sprite('rwi406_11', 4)	# 47-50
    sprite('rwi406_12', 4)	# 51-54
    sprite('rwi406_13', 5)	# 55-59
    ExitState()

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1750)
        AttackP1(70)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(1000)
        AirPushbackY(50000)
        AirUntechableTime(70)
        Unknown11058('0100000000000000000000000000000000000000')
        Hitstop(6)
        Unknown11001(8, 8, 10)
        Unknown11042(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        loopRelated(17, 13)

        def upon_17():
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 300000):
                    sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(3)

        def upon_STATE_END():
            Unknown23029(10, 4004, 0)
            GFX_0('rwief401_Slash_End', -1)

        def upon_12():
            GFX_0('rwief401_Hit', 103)
    sprite('rwi400_00', 2)	# 1-2
    GFX_0('rwief401_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi400_01', 2)	# 3-4
    sprite('rwi400_02', 2)	# 5-6
    GFX_0('rwief401_slash', -1)
    SFX_3('rwise_10')
    sprite('rwi400_03', 3)	# 7-9
    sprite('rwi400_04', 3)	# 10-12
    sprite('rwi400_05', 3)	# 13-15
    SFX_3('rwise_00')
    Unknown2037(1)
    physicsXImpulse(120000)
    Unknown23029(10, 4001, 0)
    sprite('rwi400_06', 3)	# 16-18
    label(0)
    sprite('rwi400_05', 3)	# 19-21
    Unknown23029(10, 4002, 0)
    sprite('rwi400_06', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rwi401_00', 3)	# 25-27
    GFX_0('rwief401_Slash_Hit', -1)
    Unknown1019(25)
    clearUponHandler(17)
    clearUponHandler(3)
    Unknown23029(10, 4003, 0)
    sprite('rwi401_01', 3)	# 28-30
    Unknown1019(50)
    sprite('rwi401_02', 3)	# 31-33
    Unknown1019(50)
    sprite('rwi401_03', 3)	# 34-36
    Unknown1084(1)
    tag_voice(1, 'rwi202_0', 'rwi202_1', 'rwi202_2', '')
    SFX_3('rwise_03')
    sprite('rwi401_04', 3)	# 37-39	 **attackbox here**
    physicsXImpulse(10000)
    physicsYImpulse(40000)
    Unknown1043()
    Unknown28(2, '_NEUTRAL')
    sprite('rwi401_05', 3)	# 40-42	 **attackbox here**
    sprite('rwi401_04', 3)	# 43-45	 **attackbox here**
    YAccel(50)
    sprite('rwi401_05', 3)	# 46-48	 **attackbox here**
    sprite('rwi401_06', 3)	# 49-51
    Recovery()
    Unknown1043()
    sprite('rwi401_07', 3)	# 52-54
    sprite('rwi401_08', 3)	# 55-57
    sprite('rwi401_09', 3)	# 58-60
    Unknown23029(10, 4004, 0)
    label(2)
    sprite('rwi020_07', 3)	# 61-63
    sprite('rwi020_08', 3)	# 64-66
    gotoLabel(2)
    label(3)
    sprite('rwi010_01', 2)	# 67-68
    sprite('rwi010_00', 2)	# 69-70

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(70)
        Unknown11092(1)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(20000)
        AirPushbackY(12500)
        AirUntechableTime(30)
        Unknown11042(1)
        Unknown9016(1)
        Unknown11057(750)
        Unknown2004(1, 0)
        loopRelated(17, 21)

        def upon_17():
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 300000):
                    sendToLabel(1)

        def upon_12():
            clearUponHandler(12)
            Hitstop(2)
            sendToLabel(2)

        def upon_STATE_END():
            Unknown23029(10, 4004, 0)
            GFX_0('rwief402_Slash_End', -1)
    sprite('rwi400_00', 3)	# 1-3
    GFX_0('rwief400_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi400_01', 3)	# 4-6
    sprite('rwi400_02', 2)	# 7-8
    GFX_0('rwief400_slash', -1)
    SFX_3('rwise_10')
    tag_voice(1, 'rwi201_0', 'rwi201_1', 'rwi201_2', '')
    sprite('rwi400_03', 3)	# 9-11
    sprite('rwi400_04', 3)	# 12-14
    Unknown2037(1)
    SFX_3('rwise_44')
    sprite('rwi400_05', 3)	# 15-17
    physicsXImpulse(90000)
    Unknown23029(10, 4001, 0)
    sprite('rwi400_06', 3)	# 18-20
    Unknown1019(50)
    label(0)
    sprite('rwi400_05', 3)	# 21-23
    Unknown23029(10, 4002, 0)
    sprite('rwi400_06', 3)	# 24-26
    gotoLabel(0)
    label(1)
    sprite('rwi400_07', 3)	# 27-29	 **attackbox here**
    GFX_0('rwief400_Slash_Hit', -1)
    SFX_3('rwise_02')
    clearUponHandler(17)
    clearUponHandler(3)
    physicsXImpulse(30000)
    SLOT_60 = 1
    Unknown23029(10, 4003, 0)
    sprite('rwi400_08', 6)	# 30-35
    Recovery()
    Unknown1019(25)
    sprite('rwi400_09', 6)	# 36-41
    Unknown1019(50)
    Unknown23029(10, 4004, 0)
    sprite('rwi400_10', 6)	# 42-47
    Unknown1019(50)
    sprite('rwi400_11', 6)	# 48-53
    Unknown1084(1)
    ExitState()
    label(2)
    sprite('rwi400_08', 3)	# 54-56
    sprite('rwi402_02', 3)	# 57-59
    Unknown1019(50)
    sprite('rwi402_03', 3)	# 60-62
    Unknown1019(50)
    sprite('rwi402_04', 3)	# 63-65
    Unknown1019(200)
    physicsYImpulse(18000)
    setGravity(1000)
    Unknown7009(1)
    SFX_3('rwise_03')
    sprite('rwi402_05', 3)	# 66-68	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(15000)
    Unknown11058('0100000000000000000000000000000000000000')
    sprite('rwi402_06', 2)	# 69-70
    YAccel(50)
    sprite('rwi402_07', 2)	# 71-72
    sprite('rwi402_08', 2)	# 73-74
    Unknown7009(2)
    SFX_3('rwise_03')
    sprite('rwi402_09', 3)	# 75-77	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    Hitstop(9)
    AirPushbackX(60000)
    AirPushbackY(12000)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(40)

    def upon_12():
        GFX_0('rwief402_Hit', 102)
    sprite('rwi402_10', 3)	# 78-80
    Recovery()
    Unknown1019(50)
    sprite('rwi402_11', 3)	# 81-83
    Unknown1019(50)
    sprite('rwi402_12', 3)	# 84-86
    Unknown1019(50)
    Unknown23029(10, 4004, 0)
    sprite('rwi402_13', 3)	# 87-89
    Unknown1019(50)
    sprite('rwi402_14', 3)	# 90-92

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(10)
    label(3)
    sprite('rwi020_07', 3)	# 93-95
    sprite('rwi020_08', 3)	# 96-98
    loopRest()
    gotoLabel(3)
    label(10)
    sprite('rwi010_01', 3)	# 99-101
    sprite('rwi010_00', 3)	# 102-104

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
    sprite('rwi020_07', 3)	# 3-5
    sprite('rwi020_08', 3)	# 6-8
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
        Unknown9016(1)
        GroundedHitstunAnimation(9)
        Unknown30063(1)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        AirPushbackX(40000)
        AirPushbackY(35000)
        loopRelated(17, 40)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
        Unknown2004(1, 0)

        def upon_78():
            SFX_0('025_cleanhit_slash')

        def upon_82():
            SFX_0('025_cleanhit_slash')
    sprite('rwi355_00', 3)	# 1-3
    GFX_0('rwief355_Glyph', -1)
    SFX_3('rwise_43')
    sprite('rwi355_01', 3)	# 4-6
    SFX_3('rwise_22')
    label(0)
    sprite('rwi355_02', 3)	# 7-9
    sprite('rwi355_03', 3)	# 10-12
    sprite('rwi355_04', 3)	# 13-15
    gotoLabel(0)
    label(1)
    sprite('rwi355_05', 5)	# 16-20
    sprite('rwi355_06', 5)	# 21-25
    GFX_0('rwief355_Sword_Signal', -1)
    sprite('rwi355_07', 5)	# 26-30
    sprite('rwi355_08', 5)	# 31-35
    SFX_3('rwise_48')
    sprite('rwi355_09', 5)	# 36-40
    sprite('rwi355_10', 3)	# 41-43
    sprite('rwi355_11', 3)	# 44-46	 **attackbox here**
    sprite('rwi355_12', 3)	# 47-49
    setInvincible(0)
    sprite('rwi355_13', 3)	# 50-52
    sprite('rwi355_14', 3)	# 53-55
    sprite('rwi355_12', 4)	# 56-59
    sprite('rwi355_13', 4)	# 60-63
    sprite('rwi355_14', 4)	# 64-67
    sprite('rwi355_12', 5)	# 68-72
    sprite('rwi355_13', 5)	# 73-77
    sprite('rwi355_14', 5)	# 78-82
    sprite('rwi355_15', 5)	# 83-87
    sprite('rwi202_09ex01', 5)	# 88-92
    sprite('rwi202_10ex01', 5)	# 93-97
    GFX_0('rwief355_SnowFall', -1)
    sprite('rwi202_11ex01', 5)	# 98-102
    sprite('rwi202_12ex01', 5)	# 103-107

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
        Unknown9016(1)
        GroundedHitstunAnimation(9)
        Unknown30063(1)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        AirPushbackX(40000)
        AirPushbackY(35000)
        loopRelated(17, 40)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
        Unknown2004(1, 0)

        def upon_78():
            SFX_0('025_cleanhit_slash')

        def upon_82():
            SFX_0('025_cleanhit_slash')
    sprite('rwi355_00', 3)	# 1-3
    GFX_0('rwief355_Glyph', -1)
    SFX_3('rwise_43')
    sprite('rwi355_01', 3)	# 4-6
    SFX_3('rwise_22')
    label(0)
    sprite('rwi355_02', 3)	# 7-9
    sprite('rwi355_03', 3)	# 10-12
    sprite('rwi355_04', 3)	# 13-15
    gotoLabel(0)
    label(1)
    sprite('rwi355_05', 5)	# 16-20
    sprite('rwi355_06', 5)	# 21-25
    GFX_0('rwief355_Sword_Signal', -1)
    sprite('rwi355_07', 5)	# 26-30
    sprite('rwi355_08', 5)	# 31-35
    SFX_3('rwise_48')
    sprite('rwi355_09', 5)	# 36-40
    sprite('rwi355_10', 3)	# 41-43
    sprite('rwi355_11', 3)	# 44-46	 **attackbox here**
    sprite('rwi355_12', 3)	# 47-49
    setInvincible(0)
    sprite('rwi355_13', 3)	# 50-52
    sprite('rwi355_14', 3)	# 53-55
    sprite('rwi355_12', 4)	# 56-59
    sprite('rwi355_13', 4)	# 60-63
    sprite('rwi355_14', 4)	# 64-67
    sprite('rwi355_12', 5)	# 68-72
    sprite('rwi355_13', 5)	# 73-77
    sprite('rwi355_14', 5)	# 78-82
    sprite('rwi355_15', 5)	# 83-87
    sprite('rwi202_09ex01', 5)	# 88-92
    sprite('rwi202_10ex01', 5)	# 93-97
    GFX_0('rwief355_SnowFall', -1)
    sprite('rwi202_11ex01', 5)	# 98-102
    sprite('rwi202_12ex01', 5)	# 103-107

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk4AA')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('rwi200_00', 3)	# 1-3
    sprite('rwi200_01', 4)	# 4-7
    Unknown7009(0)
    sprite('rwi200_02', 3)	# 8-10	 **attackbox here**
    GFX_0('rwief200_slash', -1)
    SFX_3('rwise_00')
    sprite('rwi200_03', 4)	# 11-14
    Recovery()
    Unknown2063()
    sprite('rwi200_04', 4)	# 15-18
    sprite('rwi200_05', 4)	# 19-22

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown9016(1)
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
    sprite('rwi201_00', 3)	# 1-3
    sprite('rwi201_01', 3)	# 4-6
    sprite('rwi201_02', 3)	# 7-9
    Unknown7009(1)
    GFX_0('rwief201_slash', -1)
    SFX_3('rwise_03')
    sprite('rwi201_03', 3)	# 10-12	 **attackbox here**
    sprite('rwi201_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('rwi201_05', 4)	# 17-20
    sprite('rwi201_06', 4)	# 21-24
    sprite('rwi201_07', 4)	# 25-28
    sprite('rwi201_08', 3)	# 29-31

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(800)
        AttackP2(80)
        Unknown11092(1)
        AirUntechableTime(22)
        AirPushbackY(-40000)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9190(1)
        Unknown9118(25)
        Hitstop(3)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        Unknown14077(0)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1019(25)
            sendToLabel(1)
    sprite('rwi270_00', 3)	# 1-3
    sprite('rwi270_01', 2)	# 4-5
    physicsXImpulse(17500)
    physicsYImpulse(10000)
    Unknown1043()
    sprite('rwi270_02', 3)	# 6-8
    sprite('rwi270_03', 3)	# 9-11
    GFX_0('rwief270_wind', -1)
    Unknown7009(1)
    SFX_0('004_swing_grap_1_0')
    sprite('rwi270_04', 3)	# 12-14	 **attackbox here**
    sprite('rwi270_05', 3)	# 15-17
    sprite('rwi270_06', 32767)	# 18-32784
    label(1)
    sprite('rwi270_06', 2)	# 32785-32786
    GFX_0('rwief270_wind2', -1)
    SFX_0('003_swing_grap_0_1')
    sprite('rwi270_07', 3)	# 32787-32789	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(3)
    PushbackX(30400)
    AirUntechableTime(17)
    Hitstop(11)
    Unknown11058('0000000001000000000000000000000000000000')
    Unknown14077(1)
    sprite('rwi270_08', 4)	# 32790-32793
    Recovery()
    Unknown2063()
    sprite('rwi270_09', 4)	# 32794-32797
    Unknown1084(1)
    sprite('rwi270_10', 4)	# 32798-32801
    sprite('rwi270_11', 4)	# 32802-32805

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(28000)
        AirPushbackY(12000)
        AirUntechableTime(30)
        Unknown9202(30)
        HitOrBlockCancel('NmlAtk5AAAA')
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('rwi271_00', 3)	# 2-4
    sprite('rwi271_01', 3)	# 5-7
    sprite('rwi271_02', 3)	# 8-10
    tag_voice(1, 'rwi106_0', 'rwi106_1', 'rwi106_2', '')
    sprite('rwi271_03', 3)	# 11-13
    GFX_0('rwief271_slash', -1)
    SFX_3('rwise_02')
    sprite('rwi271_04', 3)	# 14-16	 **attackbox here**
    sprite('rwi271_05', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('rwi271_06', 3)	# 20-22
    sprite('rwi271_07', 3)	# 23-25
    sprite('rwi271_08', 3)	# 26-28
    sprite('rwi271_09', 3)	# 29-31
    sprite('rwi271_10', 4)	# 32-35
    sprite('rwi271_11', 4)	# 36-39

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown2003(1)
        JumpCancel_(0)
        loopRelated(17, 50)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('rwi405_00', 3)	# 1-3
    sprite('rwi405_01', 3)	# 4-6
    sprite('rwi405_02', 3)	# 7-9
    sprite('rwi405_03', 3)	# 10-12
    sprite('rwi405_06', 3)	# 13-15
    sprite('rwi405_07', 3)	# 16-18
    GFX_0('5AAAAObj', -1)
    label(0)
    sprite('rwi405_08', 3)	# 19-21
    sprite('rwi405_09', 3)	# 22-24
    sprite('rwi405_07', 3)	# 25-27
    gotoLabel(0)
    label(1)
    sprite('rwi405_10', 5)	# 28-32
    Recovery()
    sprite('rwi405_11', 5)	# 33-37
    sprite('rwi405_12', 5)	# 38-42

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirUntechableTime(24)
        AttackP1(90)
        AirPushbackY(23000)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown2004(1, 0)
        Unknown1112('')
    sprite('rwi202_00', 3)	# 1-3
    sprite('rwi202_01', 3)	# 4-6
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('rwi202_02', 3)	# 7-9
    sprite('rwi202_03', 2)	# 10-11
    sprite('rwi202_04', 2)	# 12-13
    Unknown7009(2)
    SFX_3('rwise_01')
    sprite('rwi202_05', 3)	# 14-16	 **attackbox here**
    GFX_0('rwief202_slash', -1)
    sprite('rwi202_06', 3)	# 17-19
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('rwi202_07', 3)	# 20-22
    sprite('rwi202_08', 3)	# 23-25
    sprite('rwi202_09', 3)	# 26-28
    sprite('rwi202_10', 3)	# 29-31
    sprite('rwi202_11', 3)	# 32-34
    sprite('rwi202_12', 3)	# 35-37

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(2500)
        AirPushbackY(24000)
        AirUntechableTime(24)
        AttackP2(75)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
    sprite('rwi272_00', 5)	# 1-5
    sprite('rwi272_01', 5)	# 6-10
    sprite('rwi272_02', 2)	# 11-12
    GFX_0('rwief272_slash', -1)
    SFX_3('rwise_00')
    physicsXImpulse(4000)
    tag_voice(1, 'rwi107_0', 'rwi107_1', 'rwi107_2', '')
    sprite('rwi272_03', 3)	# 13-15	 **attackbox here**
    Unknown1019(50)
    sprite('rwi272_04', 3)	# 16-18
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('rwi272_05', 3)	# 19-21
    Unknown1019(50)
    sprite('rwi272_06', 3)	# 22-24
    Unknown1019(50)
    sprite('rwi272_07', 3)	# 25-27
    Unknown1019(50)
    sprite('rwi272_08', 3)	# 28-30
    Unknown1084(1)
    sprite('rwi272_09', 3)	# 31-33
    sprite('rwi272_10', 3)	# 34-36
    sprite('rwi272_11', 3)	# 37-39
    sprite('rwi272_12', 3)	# 40-42

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(1)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('rwi230_00', 2)	# 1-2
    sprite('rwi230_01', 2)	# 3-4
    sprite('rwi230_02', 2)	# 5-6
    SFX_0('003_swing_grap_0_0')
    Unknown7009(1)
    sprite('rwi230_03', 3)	# 7-9	 **attackbox here**
    sprite('rwi230_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('rwi230_01', 5)	# 13-17
    sprite('rwi230_00', 5)	# 18-22

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        Unknown9016(1)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('rwi231_00', 3)	# 1-3
    sprite('rwi231_01', 3)	# 4-6
    sprite('rwi231_02', 3)	# 7-9
    sprite('rwi231_03', 2)	# 10-11
    GFX_0('rwief231_slash', -1)
    SFX_3('rwise_03')
    Unknown7009(1)
    sprite('rwi231_04', 3)	# 12-14	 **attackbox here**
    sprite('rwi231_05', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('rwi231_06', 3)	# 18-20
    sprite('rwi231_07', 3)	# 21-23
    sprite('rwi231_08', 3)	# 24-26
    sprite('rwi231_09', 3)	# 27-29
    sprite('rwi231_10', 3)	# 30-32

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(15000)
        AirUntechableTime(30)
        Unknown9016(1)
        AttackP1(90)
        HitLow(2)
        Unknown2004(1, 0)
    sprite('rwi232_00', 2)	# 1-2
    sprite('rwi232_01', 3)	# 3-5
    sprite('rwi232_02', 3)	# 6-8
    sprite('rwi232_03', 2)	# 9-10
    sprite('rwi232_04', 2)	# 11-12
    sprite('rwi232_05', 3)	# 13-15
    Unknown7009(2)
    SFX_3('rwise_04')
    GFX_0('rwief232_slash', -1)
    sprite('rwi232_06', 3)	# 16-18	 **attackbox here**
    sprite('rwi232_07', 3)	# 19-21
    Recovery()
    Unknown2063()
    sprite('rwi232_08', 3)	# 22-24
    sprite('rwi232_09', 3)	# 25-27
    sprite('rwi232_10', 3)	# 28-30
    sprite('rwi232_11', 3)	# 31-33
    sprite('rwi232_12', 3)	# 34-36
    sprite('rwi232_13', 3)	# 37-39
    sprite('rwi232_14', 3)	# 40-42
    sprite('rwi232_15', 3)	# 43-45

@State
def NmlAtkAIR4A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(1)
        WhiffCancel('NmlAtkAIR4A')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rwi250_00', 2)	# 1-2
    sprite('rwi250_01', 2)	# 3-4
    sprite('rwi250_02', 2)	# 5-6
    SFX_0('003_swing_grap_0_0')
    Unknown7009(3)
    sprite('rwi250_03', 3)	# 7-9	 **attackbox here**
    sprite('rwi250_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    sprite('rwi250_05', 3)	# 13-15
    WhiffCancelEnable(1)
    sprite('rwi250_02', 3)	# 16-18
    sprite('rwi250_01', 3)	# 19-21
    sprite('rwi250_00', 3)	# 22-24

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rwi251_00', 2)	# 1-2
    sprite('rwi251_01', 3)	# 3-5
    sprite('rwi251_02', 3)	# 6-8
    GFX_0('rwief251_slash', -1)
    Unknown7009(4)
    SFX_3('rwise_00')
    sprite('rwi251_03', 5)	# 9-13	 **attackbox here**
    Unknown21012('72776965663235315f736c61736800000000000000000000000000000000000020000000')
    sprite('rwi251_04', 5)	# 14-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('rwi251_05', 5)	# 19-23
    sprite('rwi251_06', 5)	# 24-28
    sprite('rwi251_07', 5)	# 29-33

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5BB')
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('rwi252_00', 2)	# 1-2
    sprite('rwi252_01', 2)	# 3-4
    sprite('rwi252_02', 3)	# 5-7
    sprite('rwi252_03', 3)	# 8-10
    Unknown7009(4)
    SFX_3('rwise_03')
    sprite('rwi252_04', 3)	# 11-13	 **attackbox here**
    GFX_0('rwief252_slash', -1)
    sprite('rwi252_05', 4)	# 14-17
    Recovery()
    Unknown2063()
    sprite('rwi252_06', 4)	# 18-21
    sprite('rwi252_07', 4)	# 22-25
    sprite('rwi252_08', 4)	# 26-29
    sprite('rwi252_09', 4)	# 30-33
    sprite('rwi252_10', 4)	# 34-37
    sprite('rwi252_11', 4)	# 38-41

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        AirUntechableTime(60)
        Unknown9310(1)
        Unknown9016(1)

        def upon_3():
            if SLOT_2:
                Unknown2037(0)
                clearUponHandler(2)

                def upon_LANDING():
                    clearUponHandler(2)
                    sendToLabel(101)
    sprite('rwi203_02', 4)	# 1-4
    sprite('rwi203_03', 4)	# 5-8
    Unknown7009(5)
    physicsYImpulse(16000)
    Unknown1043()
    Unknown2037(1)
    sprite('rwi203_04', 4)	# 9-12
    SFX_3('rwise_05')
    sprite('rwi203_05', 3)	# 13-15	 **attackbox here**
    GFX_0('rwief203_slash', -1)
    sprite('rwi203_06', 4)	# 16-19
    Recovery()
    Unknown2063()
    label(100)
    sprite('rwi203_07', 4)	# 20-23
    sprite('rwi203_08', 4)	# 24-27
    gotoLabel(100)
    label(101)
    sprite('rwi203_09', 3)	# 28-30
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rwi203_10', 3)	# 31-33
    sprite('rwi203_11', 3)	# 34-36
    sprite('rwi203_12', 3)	# 37-39
    sprite('rwi203_13', 3)	# 40-42
    sprite('rwi203_14', 3)	# 43-45
    sprite('rwi203_15', 3)	# 46-48

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown9016(1)

        def upon_4():
            clearUponHandler(4)
            sendToLabel(1)
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(101)
    sprite('rwi010_00', 3)	# 1-3
    sprite('rwi203_00', 3)	# 4-6
    tag_voice(1, 'rwi157_0', 'rwi157_1', '', '')
    SLOT_12 = SLOT_19
    Unknown1019(5)
    if (SLOT_12 >= 20000):
        SLOT_12 = 20000
    physicsYImpulse(18000)
    setGravity(1800)
    Unknown23087(100000)
    label(0)
    sprite('rwi203_01', 3)	# 7-9
    sprite('rwi203_00', 3)	# 10-12
    gotoLabel(0)
    label(1)
    sprite('rwi203_02', 3)	# 13-15
    setGravity(900)
    sprite('rwi203_03', 3)	# 16-18
    SFX_3('rwise_05')
    sprite('rwi203_04', 3)	# 19-21
    sprite('rwi203_05', 3)	# 22-24	 **attackbox here**
    GFX_0('rwief203_slash', -1)
    sprite('rwi203_06', 3)	# 25-27
    label(100)
    sprite('rwi203_07', 3)	# 28-30
    sprite('rwi203_08', 3)	# 31-33
    gotoLabel(100)
    label(101)
    sprite('rwi203_09', 3)	# 34-36
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rwi203_10', 2)	# 37-38
    sprite('rwi203_11', 2)	# 39-40
    sprite('rwi203_12', 2)	# 41-42
    sprite('rwi203_13', 2)	# 43-44
    sprite('rwi203_14', 3)	# 45-47
    sprite('rwi203_15', 3)	# 48-50

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        Unknown9016(1)
        physicsYImpulse(-20000)
        Unknown1043()
        loopRelated(17, 16)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(2)
        sendToLabelUpon(2, 1)
        Unknown2004(1, 0)
    sprite('rwi203_06', 3)	# 1-3
    sprite('rwi203_07', 3)	# 4-6
    sprite('rwi203_08', 3)	# 7-9
    sprite('rwi203_07', 3)	# 10-12
    sprite('rwi203_08', 3)	# 13-15
    label(1)
    sprite('rwi203_09', 2)	# 16-17
    teleportRelativeY(0)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('rwi203_10', 2)	# 18-19
    sprite('rwi203_11', 2)	# 20-21
    sprite('rwi203_12', 2)	# 22-23
    sprite('rwi203_13', 2)	# 24-25
    sprite('rwi203_14', 2)	# 26-27
    sprite('rwi000_00', 20)	# 28-47
    label(2)
    sprite('rwi202_00', 3)	# 48-50
    sprite('rwi202_01', 3)	# 51-53
    sprite('rwi202_02', 3)	# 54-56
    sprite('rwi202_03', 2)	# 57-58
    sprite('rwi202_04', 2)	# 59-60
    tag_voice(1, 'rwi158_0', 'rwi158_1', '', '')
    SFX_3('rwise_01')
    sprite('rwi202_05', 3)	# 61-63	 **attackbox here**
    GFX_0('rwief202_slash', -1)
    sprite('rwi202_06', 3)	# 64-66
    sprite('rwi202_07', 3)	# 67-69
    sprite('rwi202_08', 3)	# 70-72
    sprite('rwi202_09', 3)	# 73-75
    sprite('rwi202_10', 3)	# 76-78
    sprite('rwi202_11', 3)	# 79-81
    sprite('rwi202_12', 3)	# 82-84
    sprite('rwi001_00', 6)	# 85-90
    sprite('rwi001_01', 6)	# 91-96
    sprite('rwi001_02', 6)	# 97-102
    sprite('rwi001_03', 6)	# 103-108
    sprite('rwi001_04', 30)	# 109-138
    sprite('rwi001_03', 6)	# 139-144
    sprite('rwi001_02', 6)	# 145-150
    sprite('rwi001_01', 6)	# 151-156
    sprite('rwi001_00', 6)	# 157-162
    sprite('rwi000_00', 6)	# 163-168
    sprite('rwi000_01', 6)	# 169-174
    sprite('rwi000_02', 6)	# 175-180
    sprite('rwi000_03', 6)	# 181-186
    sprite('rwi000_04', 6)	# 187-192
    sprite('rwi000_05', 6)	# 193-198
    sprite('rwi000_06', 6)	# 199-204
    sprite('rwi000_07', 6)	# 205-210
    sprite('rwi000_08', 6)	# 211-216
    sprite('rwi000_09', 6)	# 217-222
    sprite('rwi000_10', 6)	# 223-228
    label(1)
    sprite('keep', 1)	# 229-229

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown9016(1)
        Unknown2004(1, 0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('rwi272_00', 6)	# 1-6
    sprite('rwi272_01', 6)	# 7-12
    sprite('rwi272_02', 2)	# 13-14
    GFX_0('rwief272_slash', -1)
    SFX_3('rwise_00')
    sprite('rwi272_03', 3)	# 15-17	 **attackbox here**
    Unknown1019(50)
    sprite('rwi272_04', 3)	# 18-20
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('rwi272_05', 3)	# 21-23
    Unknown1019(50)
    sprite('rwi272_06', 3)	# 24-26
    Unknown1019(50)
    sprite('rwi272_07', 3)	# 27-29
    Unknown1019(50)
    sprite('rwi272_08', 3)	# 30-32
    Unknown1084(1)
    sprite('rwi272_09', 3)	# 33-35
    sprite('rwi272_10', 3)	# 36-38
    sprite('rwi272_11', 3)	# 39-41
    sprite('rwi272_12', 3)	# 42-44
    sprite('rwi000_00', 6)	# 45-50
    sprite('rwi000_01', 6)	# 51-56
    sprite('rwi000_02', 6)	# 57-62
    sprite('rwi000_03', 6)	# 63-68
    sprite('rwi000_04', 6)	# 69-74
    sprite('rwi000_05', 6)	# 75-80
    sprite('rwi000_06', 6)	# 81-86
    sprite('rwi000_07', 6)	# 87-92
    sprite('rwi000_08', 6)	# 93-98
    sprite('rwi000_09', 6)	# 99-104
    sprite('rwi000_10', 6)	# 105-110
    label(1)
    sprite('keep', 1)	# 111-111

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('rwi355_05', 3)	# 1-3
    sprite('rwi355_06', 3)	# 4-6
    sprite('rwi355_07', 3)	# 7-9
    sprite('rwi355_08', 3)	# 10-12
    sprite('rwi355_09', 3)	# 13-15
    sprite('rwi355_10', 4)	# 16-19
    tag_voice(0, 'rwi159_0', 'rwi159_1', '', '')
    SFX_3('rwise_03')
    sprite('rwi355_11', 3)	# 20-22	 **attackbox here**
    sprite('rwi355_12', 3)	# 23-25
    sprite('rwi355_13', 3)	# 26-28
    sprite('rwi355_14', 3)	# 29-31
    sprite('rwi355_12', 3)	# 32-34
    sprite('rwi355_13', 3)	# 35-37
    sprite('rwi355_14', 3)	# 38-40
    sprite('rwi355_15', 4)	# 41-44
    sprite('rwi202_09ex01', 4)	# 45-48
    sprite('rwi202_10ex01', 4)	# 49-52
    sprite('rwi202_11ex01', 4)	# 53-56
    sprite('rwi202_12ex01', 4)	# 57-60

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 15)	# 1-15
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 16-16
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    sprite('rwi403_00', 3)	# 17-19
    Unknown1007(250000)
    sprite('rwi403_01', 3)	# 20-22
    sprite('rwi403_02', 3)	# 23-25
    sprite('rwi403_03', 3)	# 26-28
    sprite('rwi403_04', 3)	# 29-31
    Unknown1109(75000, -20000)
    sprite('rwi403_05', 3)	# 32-34
    label(0)
    sprite('rwi403_04', 3)	# 35-37
    sprite('rwi403_05', 3)	# 38-40
    gotoLabel(0)
    label(1)
    sprite('rwi403_06', 3)	# 41-43
    SFX_3('rwise_11')
    sprite('rwi403_07', 3)	# 44-46	 **attackbox here**
    sprite('rwi403_08', 3)	# 47-49
    sprite('rwi403_09', 3)	# 50-52
    sprite('rwi403_10', 3)	# 53-55
    sprite('rwi403_11', 3)	# 56-58
    sprite('rwi403_12', 3)	# 59-61
    sprite('rwi403_13', 3)	# 62-64
    sprite('rwi403_14', 3)	# 65-67
    sprite('rwi000_00', 6)	# 68-73
    sprite('rwi000_01', 6)	# 74-79
    sprite('rwi000_02', 6)	# 80-85
    sprite('rwi000_03', 6)	# 86-91
    sprite('rwi000_04', 6)	# 92-97
    sprite('rwi000_05', 6)	# 98-103
    sprite('rwi000_06', 6)	# 104-109
    sprite('rwi000_07', 6)	# 110-115
    sprite('rwi000_08', 6)	# 116-121
    sprite('rwi000_09', 6)	# 122-127
    sprite('rwi000_10', 6)	# 128-133
    label(1)
    sprite('keep', 1)	# 134-134

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        Unknown9016(1)
    sprite('rwi232_00', 2)	# 1-2
    sprite('rwi232_01', 2)	# 3-4
    sprite('rwi232_02', 2)	# 5-6
    sprite('rwi232_03', 2)	# 7-8
    sprite('rwi232_04', 2)	# 9-10
    sprite('rwi232_05', 1)	# 11-11
    GFX_0('rwief232_slash', -1)
    SFX_3('rwise_04')
    sprite('rwi232_06', 3)	# 12-14	 **attackbox here**
    sprite('rwi232_07', 3)	# 15-17
    sprite('rwi232_08', 3)	# 18-20
    sprite('rwi232_09', 3)	# 21-23
    sprite('rwi232_10', 3)	# 24-26
    sprite('rwi232_11', 3)	# 27-29
    sprite('rwi232_12', 3)	# 30-32
    sprite('rwi232_13', 3)	# 33-35
    sprite('rwi232_14', 3)	# 36-38
    sprite('rwi232_15', 3)	# 39-41
    sprite('rwi000_00', 6)	# 42-47
    sprite('rwi000_01', 6)	# 48-53
    sprite('rwi000_02', 6)	# 54-59
    sprite('rwi000_03', 6)	# 60-65
    sprite('rwi000_04', 6)	# 66-71
    sprite('rwi000_05', 6)	# 72-77
    sprite('rwi000_06', 6)	# 78-83
    sprite('rwi000_07', 6)	# 84-89
    sprite('rwi000_08', 6)	# 90-95
    sprite('rwi000_09', 6)	# 96-101
    sprite('rwi000_10', 6)	# 102-107
    label(1)
    sprite('keep', 1)	# 108-108

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        Unknown9016(1)
        Unknown2004(1, 0)
    sprite('rwi355_05', 3)	# 1-3
    sprite('rwi355_06', 3)	# 4-6
    sprite('rwi355_07', 3)	# 7-9
    sprite('rwi355_08', 3)	# 10-12
    sprite('rwi355_09', 3)	# 13-15
    sprite('rwi355_10', 4)	# 16-19
    SFX_3('rwise_03')
    sprite('rwi355_11', 3)	# 20-22	 **attackbox here**
    sprite('rwi355_12', 3)	# 23-25
    sprite('rwi355_13', 3)	# 26-28
    sprite('rwi355_14', 3)	# 29-31
    sprite('rwi355_12', 3)	# 32-34
    sprite('rwi355_13', 3)	# 35-37
    sprite('rwi355_14', 3)	# 38-40
    sprite('rwi355_15', 4)	# 41-44
    sprite('rwi202_09ex01', 4)	# 45-48
    sprite('rwi202_10ex01', 4)	# 49-52
    sprite('rwi202_11ex01', 4)	# 53-56
    sprite('rwi202_12ex01', 4)	# 57-60

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(300)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rwi032_00', 3)	# 1-3
    sprite('rwi032_01', 3)	# 4-6
    label(0)
    sprite('rwi032_02', 4)	# 7-10
    sprite('rwi032_03', 4)	# 11-14
    sprite('rwi032_04', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('rwi032_05', 4)	# 19-22
    sprite('rwi032_06', 4)	# 23-26
    sprite('rwi032_07', 4)	# 27-30
    sprite('rwi032_08', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('rwi032_09', 4)	# 35-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rwi310_00', 2)	# 39-40
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rwi310_01', 1)	# 41-41
    SFX_3('rwise_43')
    sprite('rwi310_02', 3)	# 42-44	 **attackbox here**
    GFX_0('rwief310_glyph', -1)
    Unknown1084(1)
    sprite('rwi310_03', 4)	# 45-48
    SFX_1('rwi155')
    sprite('rwi310_04', 4)	# 49-52
    sprite('rwi310_05', 4)	# 53-56
    sprite('rwi310_06', 4)	# 57-60
    sprite('rwi310_07', 4)	# 61-64
    sprite('rwi310_08', 3)	# 65-67
    Unknown21012('72776965663331305f676c79706800000000000000000000000000000000000029000000')

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Unknown9016(1)
        Damage(1000)
        AttackP2(50)
        GroundedHitstunAnimation(9)
        AirPushbackX(20000)
        AirPushbackY(15000)
        AirUntechableTime(30)
        Unknown11064(1)
        Unknown12051(2)
        Unknown21012('72776965663331305f676c79706800000000000000000000000000000000000020000000')
        Unknown11069('ThrowMagic')
    sprite('rwi310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('rwi311_00', 6)	# 4-9
    SFX_1('rwi153')
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rwi311_01', 6)	# 10-15
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    GFX_0('rwief311_slash', -1)
    sprite('rwi311_02', 3)	# 16-18
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rwi311_03', 3)	# 19-21
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('rwi311_04', 3)	# 22-24	 **attackbox here**
    GFX_0('ThrowMagic', -1)
    sprite('rwi311_05', 3)	# 25-27
    sprite('rwi311_06', 3)	# 28-30
    sprite('rwi311_07', 6)	# 31-36
    sprite('rwi311_08', 6)	# 37-42
    sprite('rwi311_09', 6)	# 43-48
    sprite('rwi311_10', 6)	# 49-54

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(300)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('rwi032_00', 3)	# 1-3
    sprite('rwi032_01', 3)	# 4-6
    label(0)
    sprite('rwi032_02', 4)	# 7-10
    sprite('rwi032_03', 4)	# 11-14
    sprite('rwi032_04', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('rwi032_05', 4)	# 19-22
    sprite('rwi032_06', 4)	# 23-26
    sprite('rwi032_07', 4)	# 27-30
    sprite('rwi032_08', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('rwi032_09', 4)	# 35-38
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('rwi310_00', 2)	# 39-40
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('rwi310_01', 1)	# 41-41
    SFX_3('rwise_43')
    sprite('rwi310_02', 3)	# 42-44	 **attackbox here**
    GFX_0('rwief310_glyph', -1)
    Unknown1084(1)
    sprite('rwi310_03', 4)	# 45-48
    SFX_1('rwi155')
    sprite('rwi310_04', 4)	# 49-52
    sprite('rwi310_05', 4)	# 53-56
    sprite('rwi310_06', 4)	# 57-60
    sprite('rwi310_07', 4)	# 61-64
    sprite('rwi310_08', 3)	# 65-67
    Unknown21012('72776965663331305f676c79706800000000000000000000000000000000000029000000')

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(1)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(18000)
        AirPushbackY(27000)
        AirUntechableTime(100)
        Unknown11064(1)
        Unknown9346(1)
        Unknown9178(1)
        WallbounceReboundTime(1)
        Unknown11080(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown12051(2)
        Unknown13021(1)
        Unknown21005(1)
        Unknown23027()
        Unknown14077(0)
        Unknown13024(0)
        Unknown11069('BackThrowExe')
        Unknown21012('72776965663331305f676c79706800000000000000000000000000000000000021000000')
    sprite('rwi310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown5003(1)
    sprite('rwi310_02', 1)	# 4-4	 **attackbox here**
    RefreshMultihit()
    Hitstop(0)
    Unknown11083(1)
    Unknown11001(100, 100, 100)
    sprite('rwi313_00', 3)	# 5-7
    SFX_1('rwi153')
    Unknown2015(50)
    Unknown2017(0)
    physicsXImpulse(80000)
    sprite('rwi313_01', 3)	# 8-10
    Unknown1019(50)
    sprite('rwi313_01', 3)	# 11-13
    Unknown2017(1)
    Unknown1019(50)
    sprite('rwi313_02', 3)	# 14-16
    Unknown2015(100)
    Unknown2017(1)
    Unknown1019(50)
    sprite('rwi313_02', 3)	# 17-19
    Unknown2015(150)
    Unknown1019(50)
    sprite('rwi313_03', 5)	# 20-24
    Unknown2015(200)
    Unknown1084(1)
    sprite('rwi311_02', 3)	# 25-27
    GFX_0('rwief313_slash', -1)
    Unknown2006()
    sprite('rwi311_03', 3)	# 28-30
    sprite('rwi311_04', 3)	# 31-33	 **attackbox here**
    AttackLevel_(3)
    Unknown9016(1)
    Damage(1000)
    AttackP2(50)
    GroundedHitstunAnimation(9)
    AirPushbackX(20000)
    AirPushbackY(15000)
    AirUntechableTime(30)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11080(0)
    Unknown11083(0)
    Hitstop(11)
    Unknown11001(0, 0, 2)
    Unknown11069('ThrowMagic')
    RefreshMultihit()
    Unknown14077(1)
    GFX_0('ThrowMagic', -1)
    sprite('rwi311_05', 3)	# 34-36
    sprite('rwi311_06', 3)	# 37-39
    sprite('rwi311_07', 6)	# 40-45
    sprite('rwi311_08', 6)	# 46-51
    sprite('rwi311_09', 6)	# 52-57
    sprite('rwi311_10', 6)	# 58-63

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9021(1)
        Unknown9266(9)
        AirPushbackX(5000)
        AirPushbackY(25000)
        Unknown11001(0, 10, 10)

        def upon_11():
            Unknown21012('727769656633323000000000000000000000000000000000000000000000000020000000')

        def upon_STATE_END():
            Unknown21012('72776965663332305f476c79706800000000000000000000000000000000000020000000')
            Unknown21012('72776965663332305f426c6f6f6d00000000000000000000000000000000000020000000')
    sprite('rwi320_00', 4)	# 1-4
    sprite('rwi320_01', 4)	# 5-8
    GFX_0('rwief320', -1)
    tag_voice(1, 'rwi200_0', 'rwi200_1', 'rwi200_2', '')
    sprite('rwi320_02', 5)	# 9-13
    sprite('rwi320_03', 3)	# 14-16	 **attackbox here**
    sprite('rwi320_04', 2)	# 17-18
    setInvincible(0)
    sprite('rwi320_05', 2)	# 19-20
    sprite('rwi320_06', 2)	# 21-22
    sprite('rwi320_04', 3)	# 23-25
    sprite('rwi320_05', 3)	# 26-28
    sprite('rwi320_06', 3)	# 29-31
    sprite('rwi320_04', 3)	# 32-34
    sprite('rwi320_05', 3)	# 35-37
    sprite('rwi320_06', 3)	# 38-40
    label(1)
    sprite('rwi320_07', 4)	# 41-44
    sprite('rwi320_08', 4)	# 45-48
    sprite('rwi320_09', 4)	# 49-52
    sprite('rwi320_10', 4)	# 53-56
    sprite('rwi320_11', 4)	# 57-60
    sprite('rwi320_12', 4)	# 61-64

@Subroutine
def DeleteMagicCircle():
    if (SLOT_59 == 1):
        SLOT_59 = 0
        Unknown23029(4, 4069, 0)
    if (SLOT_59 == 2):
        SLOT_59 = 0
        Unknown23029(5, 4069, 0)
    if (SLOT_59 == 3):
        SLOT_59 = 0
        Unknown23029(6, 4069, 0)
    if (SLOT_59 == 4):
        SLOT_59 = 0
        Unknown23029(7, 4069, 0)

@Subroutine
def AllDeleteMagicCircle():
    if Unknown46(4):
        Unknown23029(4, 4069, 0)
    if Unknown46(5):
        Unknown23029(5, 4069, 0)
    if Unknown46(6):
        Unknown23029(6, 4069, 0)
    if Unknown46(7):
        Unknown23029(7, 4069, 0)

@Subroutine
def FirstExAssaultCancelSetting():
    WhiffCancelEnable(1)
    WhiffCancel('ExLandAssaultA')
    WhiffCancel('ExLandAssaultB')
    WhiffCancel('ExLandAssaultC')
    WhiffCancel('ExAirAssaultA')
    WhiffCancel('ExAirAssaultB')
    WhiffCancel('ExAirAssaultC')

    def upon_STATE_END():
        SLOT_60 = 0

@Subroutine
def ExAssaultCancelSetting():
    WhiffCancelEnable(1)
    WhiffCancel('ExLandAssaultA')
    WhiffCancel('ExLandAssaultB')
    WhiffCancel('ExLandAssaultC')
    WhiffCancel('ExAirAssaultA')
    WhiffCancel('ExAirAssaultB')
    WhiffCancel('ExAirAssaultC')

    def upon_STATE_END():
        SLOT_60 = 0

@State
def AssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AttackP1(80)
        AirPushbackX(20000)
        AirPushbackY(14000)
        AirUntechableTime(30)
        Unknown9016(1)
        Unknown2004(1, 0)
        loopRelated(17, 27)

        def upon_17():
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 300000):
                    sendToLabel(1)
            elif CheckInput(0x1):
                SLOT_51 = (SLOT_51 + 1)
                if (SLOT_51 > 11):
                    SLOT_51 = 100
                    clearUponHandler(17)
                    clearUponHandler(3)
                    sendToLabel(100)
        callSubroutine('FirstExAssaultCancelSetting')

        def upon_STATE_END():
            SLOT_60 = 0
            Unknown23029(10, 4004, 0)
            GFX_0('rwief400_Slash_End', -1)

        def upon_12():
            GFX_0('rwief400_Hit', 103)
    sprite('rwi400_00', 2)	# 1-2
    GFX_0('rwief400_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi400_01', 2)	# 3-4
    sprite('rwi400_02', 2)	# 5-6
    GFX_0('rwief400_slash', -1)
    SFX_3('rwise_10')
    sprite('rwi400_03', 3)	# 7-9
    sprite('rwi400_04', 3)	# 10-12
    sprite('rwi400_05', 3)	# 13-15
    tag_voice(1, 'rwi201_0', 'rwi201_1', 'rwi201_2', '')
    physicsXImpulse(90000)
    Unknown23029(10, 4001, 0)
    Unknown2037(1)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi400_06', 3)	# 16-18
    Unknown1019(70)
    label(0)
    sprite('rwi400_05', 3)	# 19-21
    Unknown23029(10, 4002, 0)
    sprite('rwi400_06', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rwi400_07', 3)	# 25-27	 **attackbox here**
    GFX_0('rwief400_Slash_Hit', -1)
    SFX_3('rwise_02')
    clearUponHandler(17)
    clearUponHandler(3)
    physicsXImpulse(30000)
    Unknown23029(10, 4003, 0)
    sprite('rwi400_07', 2)	# 28-29	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown1019(25)
    sprite('rwi400_08', 4)	# 30-33
    sprite('rwi400_09', 4)	# 34-37
    Unknown1019(50)
    Unknown23029(10, 4004, 0)
    sprite('rwi400_10', 4)	# 38-41
    Unknown1019(50)
    sprite('rwi400_11', 4)	# 42-45
    Unknown1084(1)
    ExitState()
    label(100)
    sprite('rwi400_04', 5)	# 46-50
    Unknown1084(1)
    Unknown23029(10, 4003, 0)
    GFX_0('rwief400_Slash_Cancel', -1)
    sprite('rwi400_03', 5)	# 51-55
    Unknown23029(10, 4004, 0)
    sprite('rwi400_01', 5)	# 56-60
    sprite('rwi400_00', 5)	# 61-65

@State
def AssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(7500)
        AirPushbackY(30000)
        PushbackX(49800)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(30)
        Unknown9168(40)
        Unknown9016(1)
        Unknown2004(1, 0)
        loopRelated(17, 35)

        def upon_17():
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 300000):
                    sendToLabel(1)
            elif CheckInput(0xa):
                SLOT_51 = (SLOT_51 + 1)
                if (SLOT_51 > 19):
                    SLOT_51 = 100
                    clearUponHandler(17)
                    clearUponHandler(3)
                    sendToLabel(100)

        def upon_12():
            clearUponHandler(12)
            GFX_0('rwief400_Hit', 103)
            sendToLabel(10)
        callSubroutine('FirstExAssaultCancelSetting')

        def upon_STATE_END():
            SLOT_60 = 0
            Unknown23029(10, 4004, 0)
            GFX_0('rwief401_Slash_End', -1)
    sprite('rwi400_00', 2)	# 1-2
    GFX_0('rwief401_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi400_01', 2)	# 3-4
    sprite('rwi400_02', 2)	# 5-6
    GFX_0('rwief401_slash', -1)
    SFX_3('rwise_10')
    sprite('rwi400_03', 7)	# 7-13
    sprite('rwi400_04', 7)	# 14-20
    sprite('rwi400_05', 3)	# 21-23
    tag_voice(1, 'rwi201_0', 'rwi201_1', 'rwi201_2', '')
    physicsXImpulse(150000)
    Unknown23029(10, 4001, 0)
    Unknown2037(1)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi400_06', 3)	# 24-26
    Unknown1019(50)
    label(0)
    sprite('rwi400_05', 3)	# 27-29
    Unknown23029(10, 4002, 0)
    sprite('rwi400_06', 3)	# 30-32
    gotoLabel(0)
    label(1)
    sprite('rwi400_07', 3)	# 33-35	 **attackbox here**
    SFX_3('rwise_02')
    GFX_0('rwief401_Slash_PreHit', -1)
    clearUponHandler(17)
    clearUponHandler(3)
    physicsXImpulse(30000)
    Unknown23029(10, 4003, 0)
    sprite('rwi400_08', 4)	# 36-39
    Recovery()
    Unknown1019(25)
    sprite('rwi400_09', 4)	# 40-43
    Unknown1019(50)
    Unknown23029(10, 4004, 0)
    sprite('rwi400_10', 4)	# 44-47
    Unknown1019(50)
    sprite('rwi400_11', 4)	# 48-51
    Unknown1084(1)
    ExitState()
    label(10)
    sprite('rwi401_00', 3)	# 52-54
    GFX_0('rwief401_Slash_Hit', -1)
    Unknown1019(50)
    sprite('rwi401_01', 3)	# 55-57
    Unknown1019(50)
    sprite('rwi401_02', 3)	# 58-60
    Unknown1019(50)
    sprite('rwi401_03', 3)	# 61-63
    Unknown1084(1)
    tag_voice(0, 'rwi202_0', 'rwi202_1', 'rwi202_2', '')
    sprite('rwi401_04', 3)	# 64-66	 **attackbox here**
    RefreshMultihit()
    Damage(1200)
    AirUntechableTime(45)
    Unknown9168(55)
    Unknown11058('0100000000000000000000000000000000000000')
    CounterHitAirPushbackY(33000)
    physicsXImpulse(10000)
    physicsYImpulse(43000)
    Unknown1043()
    SFX_3('rwise_03')

    def upon_12():
        GFX_0('rwief401_Hit', 103)
    Unknown28(2, '_NEUTRAL')
    sprite('rwi401_05', 3)	# 67-69	 **attackbox here**
    sprite('rwi401_04', 3)	# 70-72	 **attackbox here**
    YAccel(50)
    sprite('rwi401_05', 3)	# 73-75	 **attackbox here**
    sprite('rwi401_06', 4)	# 76-79
    Recovery()
    Unknown1043()
    sprite('rwi401_07', 4)	# 80-83
    sprite('rwi401_08', 4)	# 84-87
    sprite('rwi401_09', 4)	# 88-91
    Unknown23029(10, 4004, 0)
    label(2)
    sprite('rwi020_07', 3)	# 92-94
    sprite('rwi020_08', 3)	# 95-97
    gotoLabel(2)
    label(100)
    sprite('rwi400_04', 5)	# 98-102
    Unknown1084(1)
    Unknown23029(10, 4003, 0)
    GFX_0('rwief401_Slash_Cancel', -1)
    sprite('rwi400_03', 5)	# 103-107
    Unknown23029(10, 4004, 0)
    sprite('rwi400_01', 5)	# 108-112
    sprite('rwi400_00', 5)	# 113-117

@State
def AssaultC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1450)
        Hitstop(3)
        Unknown11091(10)
        Unknown30065(0)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(20000)
        AirPushbackY(20000)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(35)
        Unknown9016(1)
        Unknown11057(750)
        Unknown2004(1, 0)
        loopRelated(17, 21)

        def upon_17():
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if SLOT_2:
                if (SLOT_19 < 300000):
                    sendToLabel(1)
        callSubroutine('FirstExAssaultCancelSetting')

        def upon_STATE_END():
            SLOT_60 = 0
            Unknown23029(10, 4004, 0)
            GFX_0('rwief402_Slash_End', -1)
    sprite('rwi400_00', 2)	# 1-2
    GFX_0('rwief400_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi400_01', 1)	# 3-3
    sprite('rwi400_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('rwi400_02', 2)	# 5-6
    GFX_0('rwief402_slash', -1)
    SFX_3('rwise_10')
    tag_voice(1, 'rwi203_0', 'rwi203_1', 'rwi203_2', '')
    sprite('rwi400_03', 3)	# 7-9
    sprite('rwi400_04', 3)	# 10-12
    sprite('rwi400_05', 3)	# 13-15
    physicsXImpulse(90000)
    Unknown23029(10, 4001, 0)
    Unknown2037(1)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi400_06', 3)	# 16-18
    Unknown1019(50)
    label(0)
    sprite('rwi400_05', 3)	# 19-21
    Unknown23029(10, 4002, 0)
    sprite('rwi400_06', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rwi402_00', 3)	# 25-27	 **attackbox here**
    clearUponHandler(17)
    clearUponHandler(3)
    physicsXImpulse(30000)
    GFX_0('rwief402_Slash_Hit', -1)
    Unknown23029(10, 4003, 0)
    SFX_3('rwise_02')
    sprite('rwi402_01', 3)	# 28-30
    Unknown1019(50)
    sprite('rwi402_02', 3)	# 31-33
    Unknown1019(50)
    sprite('rwi402_03', 3)	# 34-36
    Unknown1019(50)
    sprite('rwi402_04', 3)	# 37-39
    Unknown1019(400)
    physicsYImpulse(25000)
    setGravity(1000)
    sprite('rwi402_05', 3)	# 40-42	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(22000)
    Unknown11058('0100000000000000000000000000000000000000')
    SFX_3('rwise_03')
    sprite('rwi402_06', 3)	# 43-45
    YAccel(50)
    sprite('rwi402_07', 3)	# 46-48
    sprite('rwi402_08', 3)	# 49-51
    Unknown7009(2)
    sprite('rwi402_09', 3)	# 52-54	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    AirPushbackX(35000)
    AirPushbackY(17500)
    SFX_3('rwise_03')

    def upon_12():
        GFX_0('rwief402_Hit', 102)
    sprite('rwi402_10', 3)	# 55-57
    Recovery()
    Unknown1019(50)
    sprite('rwi402_11', 3)	# 58-60
    Unknown1019(50)
    sprite('rwi402_12', 3)	# 61-63
    Unknown1019(50)
    Unknown23029(10, 4004, 0)
    sprite('rwi402_13', 3)	# 64-66
    Unknown1019(50)
    sprite('rwi402_14', 3)	# 67-69

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(3)
    label(2)
    sprite('rwi020_07', 3)	# 70-72
    sprite('rwi020_08', 3)	# 73-75
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('rwi010_00', 3)	# 76-78
    sprite('rwi010_01', 3)	# 79-81
    sprite('rwi010_00', 3)	# 82-84

@State
def AirAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(1500)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        AttackP1(80)
        AirUntechableTime(20)
        Unknown9154(20)
        Unknown9202(25)
        Unknown9016(1)
        Unknown11058('0000000000000000010000000000000000000000')

        def upon_LANDING():
            if SLOT_2:
                clearUponHandler(2)
                Unknown1019(25)
                physicsYImpulse(0)
                sendToLabel(1)
        callSubroutine('FirstExAssaultCancelSetting')

        def upon_STATE_END():
            SLOT_60 = 0
            Unknown23029(10, 4004, 0)
            GFX_0('rwief403A_Slash_End', -1)
    sprite('rwi403_00', 3)	# 1-3
    GFX_0('rwief403A_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi403_01', 3)	# 4-6
    Unknown1084(1)
    tag_voice(1, 'rwi204_0', 'rwi204_1', 'rwi204_2', '')
    sprite('rwi403_02', 3)	# 7-9
    sprite('rwi403_03', 3)	# 10-12
    GFX_0('rwief403A_slash', -1)
    sprite('rwi403_15', 3)	# 13-15
    Unknown1109(80000, -45000)
    Unknown23029(10, 4001, 0)
    Unknown2037(1)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi403_16', 3)	# 16-18
    label(0)
    sprite('rwi403_15', 3)	# 19-21
    Unknown23029(10, 4002, 0)
    sprite('rwi403_16', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rwi403_17', 3)	# 25-27
    GFX_0('rwief403A_Slash_Signal', -1)
    Unknown23029(10, 4003, 0)
    SFX_3('rwise_11')
    sprite('rwi403_07', 3)	# 28-30	 **attackbox here**
    sprite('rwi403_08', 3)	# 31-33
    Recovery()
    Unknown1019(50)
    sprite('rwi403_09', 3)	# 34-36
    Unknown1019(50)
    sprite('rwi403_10', 3)	# 37-39
    Unknown1019(50)
    sprite('rwi403_11', 3)	# 40-42
    Unknown1019(50)
    sprite('rwi403_12', 2)	# 43-44
    Unknown23029(10, 4004, 0)
    Unknown1084(1)
    sprite('rwi403_13', 2)	# 45-46
    sprite('rwi403_14', 2)	# 47-48

@State
def AirAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        Damage(1700)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        AttackP1(80)
        AirUntechableTime(27)
        Unknown9154(27)
        Unknown9202(32)
        Unknown9016(1)
        Unknown11058('0000000000000000010000000000000000000000')

        def upon_LANDING():
            if SLOT_2:
                clearUponHandler(2)
                Unknown1019(25)
                physicsYImpulse(0)
                sendToLabel(1)
        callSubroutine('FirstExAssaultCancelSetting')

        def upon_STATE_END():
            SLOT_60 = 0
            Unknown23029(10, 4004, 0)
            GFX_0('rwief403B_Slash_End', -1)
    sprite('rwi403_00', 4)	# 1-4
    GFX_0('rwief403B_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi403_01', 4)	# 5-8
    Unknown1084(1)
    tag_voice(1, 'rwi204_0', 'rwi204_1', 'rwi204_2', '')
    sprite('rwi403_02', 4)	# 9-12
    sprite('rwi403_03', 6)	# 13-18
    GFX_0('rwief403B_slash', -1)
    sprite('rwi403_04', 3)	# 19-21
    Unknown1109(80000, -30000)
    Unknown23029(10, 4001, 0)
    Unknown2037(1)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi403_05', 3)	# 22-24
    label(0)
    sprite('rwi403_04', 3)	# 25-27
    Unknown23029(10, 4002, 0)
    sprite('rwi403_05', 3)	# 28-30
    gotoLabel(0)
    label(1)
    sprite('rwi403_06', 3)	# 31-33
    Unknown23029(10, 4003, 0)
    GFX_0('rwief403B_Slash_Signal', -1)
    SFX_3('rwise_11')
    sprite('rwi403_07', 3)	# 34-36	 **attackbox here**
    sprite('rwi403_08', 3)	# 37-39
    Recovery()
    Unknown1019(50)
    sprite('rwi403_09', 3)	# 40-42
    Unknown1019(50)
    sprite('rwi403_10', 3)	# 43-45
    Unknown1019(50)
    sprite('rwi403_11', 3)	# 46-48
    Unknown1019(50)
    sprite('rwi403_12', 4)	# 49-52
    Unknown1084(1)
    sprite('rwi403_13', 4)	# 53-56
    sprite('rwi403_14', 4)	# 57-60

@State
def AirAssaultC():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1500)
        Unknown11091(10)
        Unknown30065(0)
        AttackP1(80)
        Unknown11092(1)
        AirUntechableTime(30)
        Unknown9016(1)
        GroundedHitstunAnimation(9)
        AirPushbackY(25000)
        Unknown11058('0000000000000000010000000000000000000000')

        def upon_LANDING():
            if SLOT_2:
                clearUponHandler(2)
                Unknown1019(25)
                physicsYImpulse(0)
                sendToLabel(1)
        callSubroutine('FirstExAssaultCancelSetting')

        def upon_STATE_END():
            SLOT_60 = 0
            Unknown23029(10, 4004, 0)
            GFX_0('rwief404_Slash_End', -1)
    sprite('rwi403_00', 3)	# 1-3
    GFX_0('rwief404_GlyphMaster', -1)
    Unknown38(10, 1)
    sprite('rwi403_01', 3)	# 4-6
    Unknown1084(1)
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'rwi204_0', 'rwi204_1', 'rwi204_2', '')
    sprite('rwi403_02', 3)	# 7-9
    sprite('rwi403_03', 3)	# 10-12
    GFX_0('rwief404_slash', -1)
    sprite('rwi403_04', 3)	# 13-15
    Unknown1109(80000, -30000)
    Unknown23029(10, 4001, 0)
    Unknown2037(1)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi403_05', 3)	# 16-18
    label(0)
    sprite('rwi403_04', 3)	# 19-21
    Unknown23029(10, 4002, 0)
    sprite('rwi403_05', 3)	# 22-24
    gotoLabel(0)
    label(1)
    sprite('rwi403_06', 3)	# 25-27
    Unknown23029(10, 4003, 0)
    GFX_0('rwief404_Slash_Signal', -1)
    SFX_3('rwise_11')
    sprite('rwi403_07', 3)	# 28-30	 **attackbox here**
    sprite('rwi403_08', 3)	# 31-33
    Unknown1019(50)
    sprite('rwi403_09', 3)	# 34-36
    sprite('rwi401_01', 3)	# 37-39
    Unknown1019(50)
    sprite('rwi401_02', 3)	# 40-42
    sprite('rwi401_03', 3)	# 43-45
    Unknown1019(50)
    SFX_3('rwise_10')
    sprite('rwi401_04', 2)	# 46-47	 **attackbox here**
    tag_voice(0, 'rwi205_0', 'rwi205_1', 'rwi205_2', '')
    physicsXImpulse(5000)
    physicsYImpulse(30000)
    Unknown1043()
    RefreshMultihit()
    Damage(500)
    Hitstop(3)
    AirUntechableTime(60)
    AirPushbackY(30000)
    Unknown11058('0100000000000000000000000000000000000000')

    def upon_12():
        GFX_0('rwief401_Hit', 103)
        clearUponHandler(12)
    sprite('rwi401_05', 2)	# 48-49	 **attackbox here**
    RefreshMultihit()
    sprite('rwi401_04', 2)	# 50-51	 **attackbox here**
    RefreshMultihit()
    sprite('rwi401_05', 2)	# 52-53	 **attackbox here**
    RefreshMultihit()
    sprite('rwi401_06', 3)	# 54-56
    Recovery()
    sprite('rwi401_07', 3)	# 57-59
    sprite('rwi401_08', 3)	# 60-62
    sprite('rwi401_09', 3)	# 63-65
    Unknown23029(10, 4004, 0)
    sprite('rwi020_05', 3)	# 66-68
    sprite('rwi020_06', 3)	# 69-71

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(11)
    label(10)
    sprite('rwi020_07', 3)	# 72-74
    sprite('rwi020_08', 3)	# 75-77
    gotoLabel(10)
    label(11)
    sprite('rwi010_00', 3)	# 78-80
    sprite('rwi010_01', 3)	# 81-83
    sprite('rwi010_00', 3)	# 84-86

@State
def IceShieldA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        loopRelated(17, 24)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('rwi405_00', 3)	# 1-3
    sprite('rwi405_01', 3)	# 4-6
    sprite('rwi405_02', 3)	# 7-9
    sprite('rwi405_03', 3)	# 10-12
    tag_voice(1, 'rwi206_0', 'rwi206_1', 'rwi206_2', '')
    sprite('rwi405_06', 3)	# 13-15
    Unknown23029(8, 4051, 0)
    GFX_0('IceShieldA', -1)
    Unknown38(8, 1)
    sprite('rwi405_07', 3)	# 16-18
    Recovery()
    label(0)
    sprite('rwi405_08', 3)	# 19-21
    sprite('rwi405_09', 3)	# 22-24
    sprite('rwi405_07', 3)	# 25-27
    gotoLabel(0)
    label(1)
    sprite('rwi405_10', 5)	# 28-32
    Recovery()
    sprite('rwi405_11', 5)	# 33-37
    sprite('rwi405_12', 5)	# 38-42

@State
def IceShieldB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        loopRelated(17, 30)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('rwi405_00', 3)	# 1-3
    sprite('rwi405_01', 3)	# 4-6
    sprite('rwi405_02', 3)	# 7-9
    sprite('rwi405_03', 3)	# 10-12
    sprite('rwi405_04', 3)	# 13-15
    sprite('rwi405_05', 3)	# 16-18
    tag_voice(1, 'rwi206_0', 'rwi206_1', 'rwi206_2', '')
    sprite('rwi405_06', 3)	# 19-21
    Unknown23029(8, 4051, 0)
    GFX_0('IceShieldB', -1)
    Unknown38(8, 1)
    sprite('rwi405_07', 3)	# 22-24
    Recovery()
    label(0)
    sprite('rwi405_08', 3)	# 25-27
    sprite('rwi405_09', 3)	# 28-30
    sprite('rwi405_07', 3)	# 31-33
    gotoLabel(0)
    label(1)
    sprite('rwi405_07', 3)	# 34-36
    sprite('rwi405_08', 3)	# 37-39
    sprite('rwi405_09', 3)	# 40-42
    sprite('rwi405_10', 5)	# 43-47
    Recovery()
    sprite('rwi405_11', 5)	# 48-52
    sprite('rwi405_12', 5)	# 53-57

@State
def IceShieldC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        Unknown11063(1)
        loopRelated(17, 40)

        def upon_17():
            clearUponHandler(17)
            setInvincible(0)
            sendToLabel(1)
        GuardPoint_(1)
        Unknown22019('0100000001000000010000000100000000000000')
        Unknown22030(0)
        Unknown22031(15, 30)

        def upon_42():
            Unknown23022(1)
            ScreenShake(8000, 2000)
            Unknown21012('727769656634303543000000000000000000000000000000000000000000000020000000')
            if Unknown23036():
                enterState('IceShieldCounter')
    sprite('rwi405_00', 3)	# 1-3
    sprite('rwi405_01', 3)	# 4-6
    GFX_0('rwief405C', -1)
    Unknown23125('')
    Unknown2058(-5000)
    Unknown22008(37)
    sprite('rwi405_02', 3)	# 7-9
    SFX_3('rwise_43')
    sprite('rwi405_03', 3)	# 10-12
    sprite('rwi405_04', 3)	# 13-15
    sprite('rwi405_05', 3)	# 16-18
    label(0)
    sprite('rwi405_03', 4)	# 19-22
    sprite('rwi405_04', 4)	# 23-26
    sprite('rwi405_05', 4)	# 27-30
    gotoLabel(0)
    label(1)
    sprite('rwi405_02', 5)	# 31-35
    sprite('rwi405_01', 5)	# 36-40
    sprite('rwi405_00', 5)	# 41-45

@State
def IceShieldCounter():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        AttackLevel_(4)
        Damage(1850)
        Unknown11091(10)
        Unknown30065(0)
        GroundedHitstunAnimation(9)
        AttackP1(80)
        AttackP2(75)
        AirUntechableTime(25)
        AirPushbackY(-40000)
        Unknown9190(1)
        Unknown9118(50)
        Unknown9016(1)
        Unknown12051(0)
        Unknown2004(1, 0)
        setInvincible(1)
    sprite('rwi202_00', 3)	# 1-3
    sprite('rwi202_01', 3)	# 4-6
    sprite('rwi202_02', 3)	# 7-9
    sprite('rwi202_03', 2)	# 10-11
    sprite('rwi202_04', 2)	# 12-13
    tag_voice(1, 'rwi207_0', 'rwi207_1', 'rwi207_2', '')
    sprite('rwi202_05', 3)	# 14-16	 **attackbox here**
    GFX_0('rwief202_slash', -1)
    sprite('rwi202_06', 3)	# 17-19
    setInvincible(0)
    Recovery()
    sprite('rwi202_07', 3)	# 20-22
    sprite('rwi202_08', 3)	# 23-25
    sprite('rwi202_09', 3)	# 26-28
    sprite('rwi202_10', 3)	# 29-31
    sprite('rwi202_11', 3)	# 32-34
    sprite('rwi202_12', 3)	# 35-37

@State
def SetMagicA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        loopRelated(17, 15)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if CheckInput(0x5):
                Unknown2037(1)
    sprite('rwi406_00', 3)	# 1-3
    sprite('rwi406_01', 3)	# 4-6
    sprite('rwi406_02', 3)	# 7-9
    tag_voice(1, 'rwi208_0', 'rwi208_1', 'rwi208_2', '')
    label(0)
    sprite('rwi406_03', 3)	# 10-12
    sprite('rwi406_04', 3)	# 13-15
    sprite('rwi406_05', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('rwi406_06', 3)	# 19-21
    sprite('rwi406_07', 3)	# 22-24
    sprite('rwi406_08', 3)	# 25-27
    Unknown23029(4, 4069, 0)
    GFX_0('InstallationMagic', -1)
    Unknown38(4, 1)
    Unknown23029(4, 4061, 0)
    sprite('rwi406_09', 3)	# 28-30
    Recovery()
    if SLOT_2:
        sendToLabel(3)
    sprite('rwi406_10', 3)	# 31-33
    sprite('rwi406_11', 3)	# 34-36
    Unknown23029(4, 4066, 0)
    sprite('rwi406_12', 3)	# 37-39
    sprite('rwi406_13', 3)	# 40-42
    ExitState()
    label(3)
    sprite('rwi406_10', 4)	# 43-46
    sprite('rwi406_11', 4)	# 47-50
    sprite('rwi406_12', 4)	# 51-54
    sprite('rwi406_10', 4)	# 55-58
    sprite('rwi406_11', 4)	# 59-62
    sprite('rwi406_12', 4)	# 63-66
    sprite('rwi406_13', 5)	# 67-71
    ExitState()

@State
def SetMagicB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        loopRelated(17, 15)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if CheckInput(0xe):
                Unknown2037(1)
    sprite('rwi406_00', 3)	# 1-3
    sprite('rwi406_01', 3)	# 4-6
    sprite('rwi406_02', 3)	# 7-9
    tag_voice(1, 'rwi208_0', 'rwi208_1', 'rwi208_2', '')
    label(0)
    sprite('rwi406_03', 3)	# 10-12
    sprite('rwi406_04', 3)	# 13-15
    sprite('rwi406_05', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('rwi406_06', 3)	# 19-21
    sprite('rwi406_07', 3)	# 22-24
    sprite('rwi406_08', 3)	# 25-27
    Unknown23029(5, 4069, 0)
    GFX_0('InstallationMagic', -1)
    Unknown38(5, 1)
    Unknown23029(5, 4062, 0)
    sprite('rwi406_09', 3)	# 28-30
    Recovery()
    if SLOT_2:
        sendToLabel(3)
    sprite('rwi406_10', 3)	# 31-33
    sprite('rwi406_11', 3)	# 34-36
    Unknown23029(5, 4066, 0)
    sprite('rwi406_12', 3)	# 37-39
    sprite('rwi406_13', 3)	# 40-42
    ExitState()
    label(3)
    sprite('rwi406_10', 4)	# 43-46
    sprite('rwi406_11', 4)	# 47-50
    sprite('rwi406_12', 4)	# 51-54
    sprite('rwi406_10', 4)	# 55-58
    sprite('rwi406_11', 4)	# 59-62
    sprite('rwi406_12', 4)	# 63-66
    sprite('rwi406_13', 5)	# 67-71
    ExitState()

@State
def SetMagicC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        loopRelated(17, 15)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown2037(0)

        def upon_3():
            if CheckInput(0x17):
                Unknown2037(1)
    sprite('rwi406_00', 3)	# 1-3
    sprite('rwi406_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('rwi406_02', 3)	# 7-9
    tag_voice(1, 'rwi208_0', 'rwi208_1', 'rwi208_2', '')
    label(0)
    sprite('rwi406_03', 3)	# 10-12
    sprite('rwi406_04', 3)	# 13-15
    sprite('rwi406_05', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('rwi406_06', 3)	# 19-21
    sprite('rwi406_07', 3)	# 22-24
    sprite('rwi406_08', 3)	# 25-27
    Unknown23029(6, 4069, 0)
    Unknown23029(7, 4069, 0)
    GFX_0('InstallationMagic', -1)
    Unknown38(6, 1)
    Unknown23029(6, 4063, 0)
    sprite('rwi406_09', 3)	# 28-30
    GFX_0('InstallationMagic', -1)
    Unknown38(7, 1)
    Unknown23029(7, 4064, 0)
    Recovery()
    if SLOT_2:
        sendToLabel(3)
    sprite('rwi406_10', 3)	# 31-33
    sprite('rwi406_11', 3)	# 34-36
    Unknown23029(6, 4066, 0)
    Unknown23029(7, 4066, 0)
    sprite('rwi406_12', 3)	# 37-39
    sprite('rwi406_13', 3)	# 40-42
    ExitState()
    label(3)
    sprite('rwi406_10', 4)	# 43-46
    sprite('rwi406_11', 4)	# 47-50
    sprite('rwi406_12', 4)	# 51-54
    sprite('rwi406_10', 4)	# 55-58
    sprite('rwi406_11', 4)	# 59-62
    sprite('rwi406_12', 4)	# 63-66
    sprite('rwi406_13', 5)	# 67-71
    ExitState()

@State
def ExLandAssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        AttackLevel_(4)
        Damage(1750)
        AttackP1(80)
        GroundedHitstunAnimation(10)
        AirPushbackX(-1000)
        AirPushbackY(-40000)
        AirUntechableTime(30)
        HitOverhead(2)
        Unknown11056(3)
        Unknown9016(1)
        Unknown9310(1)
        Unknown11065(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown12051(2)

        def upon_STATE_END():
            Unknown2015(-1)

        def upon_8():
            Unknown2005()
            if (SLOT_40 < 0):
                Unknown21005(1)
        Unknown2006()
        callSubroutine('ExAssaultCancelSetting')
    sprite('rwi407_00', 2)	# 1-2
    sprite('rwi407_01', 2)	# 3-4
    Unknown1084(1)
    callSubroutine('DeleteMagicCircle')
    sprite('rwi407_02', 2)	# 5-6
    sprite('rwi407_03', 2)	# 7-8
    sprite('rwi407_04', 2)	# 9-10
    SFX_3('rwise_44')
    sprite('rwi407_05', 2)	# 11-12
    physicsXImpulse(25000)
    physicsYImpulse(18000)
    Unknown1043()
    Unknown2015(50)
    Unknown23087(-100000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rwi407_06', 2)	# 13-14
    sprite('rwi407_07', 2)	# 15-16
    tag_voice(1, 'rwi209_0', 'rwi209_1', 'rwi209_2', '')
    sprite('rwi407_08', 2)	# 17-18
    sprite('rwi407_09', 3)	# 19-21
    GFX_0('rwief407_slash', -1)
    sprite('rwi407_10', 3)	# 22-24
    SFX_3('rwise_03')
    sprite('rwi407_11', 5)	# 25-29	 **attackbox here**
    SLOT_60 = 1
    sprite('rwi407_12', 3)	# 30-32
    Recovery()
    label(0)
    sprite('rwi407_13', 3)	# 33-35
    sprite('rwi407_14', 3)	# 36-38
    gotoLabel(0)
    label(1)
    sprite('rwi407_15', 3)	# 39-41
    Unknown1019(50)
    Unknown8000(100, 1, 1)
    Unknown23073()
    sprite('rwi407_16', 3)	# 42-44
    Unknown1084(1)
    sprite('rwi407_17', 2)	# 45-46

@State
def ExAirAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        Unknown30068(1)
        AttackLevel_(4)
        Damage(1900)
        AttackP1(80)
        GroundedHitstunAnimation(10)
        AirPushbackX(-1000)
        AirPushbackY(-80000)
        AirUntechableTime(30)
        HitOverhead(2)
        Unknown11056(3)
        Unknown9310(10)
        Unknown9016(1)
        Unknown12051(2)

        def upon_STATE_END():
            Unknown2015(-1)

        def upon_8():
            Unknown2005()
            if (SLOT_40 < 0):
                Unknown21005(1)
        Unknown2006()
        callSubroutine('ExAssaultCancelSetting')
    sprite('rwi408_01', 2)	# 1-2
    physicsXImpulse(-15000)
    physicsYImpulse(10000)
    GFX_0('rwief408_Glyph', -1)
    Unknown38(9, 1)
    Unknown23029(9, 4071, 0)
    physicsXImpulse(-5000)
    sprite('rwi408_02', 2)	# 3-4
    Unknown1019(50)
    callSubroutine('DeleteMagicCircle')
    sprite('rwi403_01', 2)	# 5-6
    Unknown1019(50)
    sprite('rwi403_02', 2)	# 7-8
    Unknown1019(50)
    sprite('rwi403_03', 2)	# 9-10
    Unknown1084(1)
    SFX_3('rwise_44')
    sprite('rwi407_05', 2)	# 11-12
    Unknown23029(9, 4072, 0)
    Unknown1007(30000)
    physicsXImpulse(18000)
    physicsYImpulse(10000)
    Unknown1043()
    Unknown2015(50)
    Unknown23087(-100000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rwi407_06', 2)	# 13-14
    sprite('rwi407_07', 2)	# 15-16
    tag_voice(1, 'rwi209_0', 'rwi209_1', 'rwi209_2', '')
    sprite('rwi407_08', 2)	# 17-18
    sprite('rwi407_09', 3)	# 19-21
    GFX_0('rwief407_slash', -1)
    sprite('rwi407_10', 3)	# 22-24
    SFX_3('rwise_03')
    sprite('rwi407_11', 5)	# 25-29	 **attackbox here**
    SLOT_60 = 1
    sprite('rwi407_12', 3)	# 30-32
    Recovery()
    label(0)
    sprite('rwi407_13', 3)	# 33-35
    sprite('rwi407_14', 3)	# 36-38
    gotoLabel(0)
    label(1)
    sprite('rwi407_15', 5)	# 39-43
    Unknown1019(50)
    Unknown8000(100, 1, 1)
    Unknown23073()
    sprite('rwi407_16', 5)	# 44-48
    Unknown1084(1)
    sprite('rwi407_17', 5)	# 49-53

@State
def ExLandAssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        AttackLevel_(4)
        Damage(2200)
        AttackP1(80)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirPushbackY(-40000)
        AirUntechableTime(30)
        Unknown9310(15)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown12051(2)
        Unknown2006()
        callSubroutine('ExAssaultCancelSetting')
    sprite('rwi407_00', 2)	# 1-2
    GFX_0('rwief408_Glyph', -1)
    Unknown38(9, 1)
    sprite('rwi407_01', 2)	# 3-4
    Unknown1084(1)
    callSubroutine('DeleteMagicCircle')
    sprite('rwi407_02', 2)	# 5-6
    sprite('rwi407_03', 2)	# 7-8
    sprite('rwi407_04', 2)	# 9-10
    SFX_3('rwise_44')
    sprite('rwi408_00', 3)	# 11-13
    Unknown23029(9, 4072, 0)
    physicsXImpulse(-60000)
    physicsYImpulse(36000)
    setGravity(3500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    setInvincible(1)
    Unknown22019('0000000001000000000000000000000000000000')
    sprite('rwi408_01', 3)	# 14-16
    Unknown1019(50)
    sprite('rwi408_02', 3)	# 17-19
    Unknown1019(75)
    sprite('rwi403_01', 2)	# 20-21
    Unknown1019(75)
    sprite('rwi403_02', 6)	# 22-27
    Unknown1019(25)
    physicsYImpulse(0)
    setGravity(0)
    sprite('rwi403_03', 6)	# 28-33
    GFX_0('rwief408_slash', -1)
    tag_voice(1, 'rwi210_0', 'rwi210_1', 'rwi210_2', '')
    Unknown1084(1)
    sprite('rwi408_03', 3)	# 34-36	 **attackbox here**
    Unknown21012('72776965663430385f476c79706800000000000000000000000000000000000029000000')
    physicsXImpulse(100000)
    physicsYImpulse(-40000)
    Unknown23087(100000)
    SLOT_60 = 1
    SFX_3('rwise_44')
    sprite('rwi408_04', 3)	# 37-39	 **attackbox here**
    setInvincible(0)
    label(0)
    sprite('rwi408_03', 3)	# 40-42	 **attackbox here**
    sprite('rwi408_04', 3)	# 43-45	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('rwi408_05', 2)	# 46-47
    Unknown1019(50)
    Unknown8000(100, 1, 1)
    Recovery()
    Unknown21012('72776965663430385f736c61736800000000000000000000000000000000000020000000')
    SFX_3('rwise_11')
    sprite('rwi408_06', 2)	# 48-49
    Unknown1019(50)
    sprite('rwi408_09', 3)	# 50-52
    Unknown1019(50)
    sprite('rwi408_10', 3)	# 53-55
    Unknown1084(1)
    sprite('rwi408_11', 2)	# 56-57

@State
def ExAirAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        Unknown30068(1)
        AttackLevel_(4)
        Damage(2350)
        AttackP1(80)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirPushbackY(-80000)
        Unknown9190(1)
        Unknown9118(25)
        AirUntechableTime(45)
        Unknown9016(1)
        Unknown12051(2)
        Unknown2006()
        callSubroutine('ExAssaultCancelSetting')
    sprite('rwi408_01', 3)	# 1-3
    physicsXImpulse(-15000)
    physicsYImpulse(10000)
    GFX_0('rwief408_Glyph', -1)
    Unknown38(9, 1)
    Unknown23029(9, 4071, 0)
    SFX_3('rwise_44')
    setInvincible(1)
    Unknown22019('0000000001000000000000000000000000000000')
    sprite('rwi408_02', 3)	# 4-6
    Unknown1019(75)
    callSubroutine('DeleteMagicCircle')
    sprite('rwi403_01', 3)	# 7-9
    sprite('rwi403_02', 6)	# 10-15
    Unknown1019(25)
    physicsYImpulse(0)
    setGravity(0)
    sprite('rwi403_03', 6)	# 16-21
    GFX_0('rwief408_slash', -1)
    tag_voice(1, 'rwi210_0', 'rwi210_1', 'rwi210_2', '')
    Unknown1084(1)
    sprite('rwi408_03', 3)	# 22-24	 **attackbox here**
    Unknown23029(9, 4072, 0)
    Unknown21012('72776965663430385f476c79706800000000000000000000000000000000000029000000')
    physicsXImpulse(100000)
    physicsYImpulse(-60000)
    Unknown23087(100000)
    SLOT_60 = 1
    SFX_3('rwise_44')

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rwi408_04', 3)	# 25-27	 **attackbox here**
    setInvincible(0)
    label(0)
    sprite('rwi408_03', 3)	# 28-30	 **attackbox here**
    sprite('rwi408_04', 3)	# 31-33	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('rwi408_05', 2)	# 34-35
    Unknown21012('72776965663430385f736c61736800000000000000000000000000000000000020000000')
    Unknown1019(50)
    Unknown8000(100, 1, 1)
    Recovery()
    SFX_3('rwise_11')
    sprite('rwi408_06', 2)	# 36-37
    Unknown1019(50)
    sprite('rwi408_07', 2)	# 38-39
    Unknown1019(50)
    sprite('rwi408_08', 2)	# 40-41
    Unknown1019(50)
    sprite('rwi408_09', 3)	# 42-44
    Unknown1019(50)
    sprite('rwi408_10', 3)	# 45-47
    Unknown1084(1)
    sprite('rwi408_11', 3)	# 48-50

@State
def ExLandAssaultC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30068(1)
        AttackLevel_(4)
        Damage(1300)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(6)
        Unknown11001(0, 0, 0)
        AirUntechableTime(30)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(17000)
        Unknown11056(3)
        Unknown9016(1)
        Unknown11058('0100000000000000000000000000000000000000')
        Unknown2006()
        callSubroutine('ExAssaultCancelSetting')
    sprite('rwi407_00', 2)	# 1-2
    sprite('rwi407_01', 2)	# 3-4
    Unknown1084(1)
    callSubroutine('DeleteMagicCircle')
    sprite('rwi407_02', 2)	# 5-6
    sprite('rwi407_03', 2)	# 7-8
    sprite('rwi407_04', 2)	# 9-10
    SFX_3('rwise_44')
    sprite('rwi409_00', 2)	# 11-12
    tag_voice(1, 'rwi211_0', 'rwi211_1', 'rwi211_2', '')
    physicsXImpulse(25000)
    physicsYImpulse(12000)
    setGravity(1000)
    Unknown23087(60000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rwi409_01', 2)	# 13-14
    sprite('rwi409_02', 3)	# 15-17
    GFX_0('rwief409_slash', -1)
    SFX_3('rwise_04')
    sprite('rwi409_03', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    SLOT_60 = 1
    sprite('rwi409_04', 2)	# 21-22
    sprite('rwi409_05', 2)	# 23-24
    sprite('rwi409_06', 2)	# 25-26
    SFX_3('rwise_02')
    sprite('rwi409_07', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    sprite('rwi409_08', 3)	# 30-32
    Recovery()
    sprite('rwi409_09', 3)	# 33-35
    Unknown1043()
    label(0)
    sprite('rwi409_10', 3)	# 36-38
    sprite('rwi409_11', 3)	# 39-41
    gotoLabel(0)
    label(1)
    sprite('rwi407_15ex01', 2)	# 42-43
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rwi407_16ex01', 2)	# 44-45
    sprite('rwi407_17ex01', 2)	# 46-47

@State
def ExAirAssaultC():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
        Unknown30068(1)
        AttackLevel_(4)
        Damage(1400)
        AttackP1(90)
        Unknown11092(1)
        Hitstop(6)
        AirUntechableTime(35)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(15000)
        Unknown11056(3)
        Unknown9016(1)
        Unknown2006()
        callSubroutine('ExAssaultCancelSetting')
    sprite('rwi408_01', 2)	# 1-2
    physicsXImpulse(-15000)
    physicsYImpulse(18000)
    GFX_0('rwief408_Glyph', -1)
    Unknown38(9, 1)
    Unknown23029(9, 4071, 0)
    physicsXImpulse(-5000)
    sprite('rwi408_02', 2)	# 3-4
    Unknown1019(50)
    callSubroutine('DeleteMagicCircle')
    sprite('rwi403_01', 2)	# 5-6
    Unknown1019(50)
    sprite('rwi403_02', 2)	# 7-8
    Unknown1019(50)
    sprite('rwi403_03', 2)	# 9-10
    Unknown1084(1)
    SFX_3('rwise_44')
    sprite('rwi409_00', 2)	# 11-12
    Unknown23029(9, 4072, 0)
    tag_voice(1, 'rwi211_0', 'rwi211_1', 'rwi211_2', '')
    Unknown1007(30000)
    physicsXImpulse(35000)
    physicsYImpulse(13000)
    setGravity(1000)
    Unknown23087(60000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sprite('rwi409_01', 2)	# 13-14
    sprite('rwi409_02', 3)	# 15-17
    GFX_0('rwief409_slash', -1)
    SFX_3('rwise_04')
    sprite('rwi409_03', 3)	# 18-20	 **attackbox here**
    RefreshMultihit()
    SLOT_60 = 1
    sprite('rwi409_04', 2)	# 21-22
    sprite('rwi409_05', 2)	# 23-24
    sprite('rwi409_06', 2)	# 25-26
    SFX_3('rwise_02')
    sprite('rwi409_07', 3)	# 27-29	 **attackbox here**
    RefreshMultihit()
    Hitstop(12)
    sprite('rwi409_08', 3)	# 30-32
    Recovery()
    sprite('rwi409_09', 3)	# 33-35
    Unknown1043()
    label(0)
    sprite('rwi409_10', 3)	# 36-38
    sprite('rwi409_11', 3)	# 39-41
    gotoLabel(0)
    label(1)
    sprite('rwi407_15ex01', 2)	# 42-43
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rwi407_16ex01', 2)	# 44-45
    sprite('rwi407_17ex01', 2)	# 46-47

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        loopRelated(17, 70)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 4314):
                clearUponHandler(43)
                sendToLabel(1)
            if (SLOT_48 == 4315):
                clearUponHandler(43)
                sendToLabel(1)
    sprite('rwi000_00', 6)	# 1-6
    tag_voice(1, 'rwi253_0', 'rwi253_1', 'rwi253_2', '')
    Unknown2036(43, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('rwi431_00', 6)	# 7-12
    GFX_0('rwief431_Charge', -1)
    sprite('rwi431_01', 6)	# 13-18
    sprite('rwi431_02', 6)	# 19-24
    sprite('rwi431_03', 6)	# 25-30
    SFX_3('rwise_46')
    sprite('rwi431_04', 6)	# 31-36
    sprite('rwi431_05', 10)	# 37-46
    sprite('rwi431_06', 3)	# 47-49
    sprite('rwi431_07', 3)	# 50-52
    GFX_0('UltimateShotMaster', -1)
    tag_voice(0, 'rwi254_0', 'rwi254_1', 'rwi254_2', '')
    sprite('rwi431_08', 3)	# 53-55
    setInvincible(0)
    label(0)
    sprite('rwi431_09', 3)	# 56-58
    sprite('rwi431_10', 3)	# 59-61
    sprite('rwi431_08', 3)	# 62-64
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 65-65
    setInvincible(0)
    clearUponHandler(17)
    sprite('rwi431_08', 4)	# 66-69
    sprite('rwi431_09', 4)	# 70-73
    sprite('rwi431_10', 4)	# 74-77
    sprite('rwi431_08', 5)	# 78-82
    sprite('rwi431_09', 5)	# 83-87
    sprite('rwi431_10', 5)	# 88-92
    sprite('rwi431_11', 5)	# 93-97
    sprite('rwi431_12', 5)	# 98-102
    sprite('rwi431_13', 5)	# 103-107
    sprite('rwi431_14', 4)	# 108-111
    sprite('rwi431_15', 4)	# 112-115
    sprite('rwi431_16', 4)	# 116-119

@State
def UltimateShotSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        loopRelated(17, 70)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        Unknown2037(0)
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 4314):
                Unknown2037(1)
                Unknown13024(0)
                sendToLabel(1)
            if (SLOT_48 == 4315):
                sendToLabel(1)
            if (SLOT_48 == 4317):
                Unknown2064(1)
    sprite('rwi000_00', 6)	# 1-6
    tag_voice(1, 'rwi253_0', 'rwi253_1', 'rwi253_2', '')
    Unknown2036(43, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('rwi431_00', 6)	# 7-12
    sprite('rwi431_01', 6)	# 13-18
    sprite('rwi431_02', 6)	# 19-24
    sprite('rwi431_03', 6)	# 25-30
    SFX_3('rwise_46')
    sprite('rwi431_04', 6)	# 31-36
    sprite('rwi431_05', 10)	# 37-46
    sprite('rwi431_06', 3)	# 47-49
    sprite('rwi431_07', 3)	# 50-52
    GFX_0('UltimateShotMaster', -1)
    Unknown23029(1, 4316, 0)
    tag_voice(0, 'rwi254_0', 'rwi254_1', 'rwi254_2', '')
    sprite('rwi431_08', 3)	# 53-55
    setInvincible(0)
    label(0)
    sprite('rwi431_09', 3)	# 56-58
    sprite('rwi431_10', 3)	# 59-61
    sprite('rwi431_08', 3)	# 62-64
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 65-65
    setInvincible(0)
    clearUponHandler(17)
    sprite('rwi431_08', 4)	# 66-69
    sprite('rwi431_09', 4)	# 70-73
    sprite('rwi431_10', 4)	# 74-77
    sprite('rwi431_08', 5)	# 78-82
    sprite('rwi431_09', 5)	# 83-87
    sprite('rwi431_10', 5)	# 88-92
    sprite('rwi431_11', 5)	# 93-97
    sprite('rwi431_12', 5)	# 98-102
    sprite('rwi431_13', 5)	# 103-107
    sprite('rwi431_14', 4)	# 108-111
    sprite('rwi431_15', 4)	# 112-115
    sprite('rwi431_16', 3)	# 116-118
    sprite('keep', 1)	# 119-119
    if SLOT_2:
        enterState('UltimateShotSP_Add')

@State
def UltimateShotSP_Add():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown11108('03000000')
        AttackLevel_(5)
        Damage(2500)
        AttackP2(100)
        Unknown11091(10)
        Unknown9016(1)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        AirPushbackX(40000)
        AirPushbackY(35000)
        loopRelated(17, 40)

        def upon_17():
            sendToLabel(1)
        setInvincible(1)
        Unknown2004(1, 0)

        def upon_78():
            SFX_0('025_cleanhit_slash')

        def upon_82():
            SFX_0('025_cleanhit_slash')
    sprite('rwi430_04', 3)	# 1-3
    tag_voice(1, 'rwi255_0', 'rwi255_1', 'rwi255_2', '')
    Unknown2036(67, -1, 0)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    sprite('rwi430_05', 3)	# 4-6
    sprite('rwi430_06', 3)	# 7-9
    GFX_0('rwief355_Glyph', -1)
    SFX_3('rwise_22')
    label(0)
    sprite('rwi430_04', 3)	# 10-12
    sprite('rwi430_05', 3)	# 13-15
    sprite('rwi430_06', 3)	# 16-18
    gotoLabel(0)
    label(1)
    sprite('rwi355_05', 5)	# 19-23
    sprite('rwi355_06', 5)	# 24-28
    GFX_0('rwief355_Sword_Signal', -1)
    sprite('rwi355_07', 5)	# 29-33
    sprite('rwi355_08', 5)	# 34-38
    SFX_3('rwise_48')
    sprite('rwi355_09', 5)	# 39-43
    sprite('rwi355_10', 3)	# 44-46
    tag_voice(0, 'rwi256_0', 'rwi256_1', 'rwi256_2', '')
    sprite('rwi355_11', 3)	# 47-49	 **attackbox here**
    sprite('rwi355_12', 3)	# 50-52
    setInvincible(0)
    sprite('rwi355_13', 3)	# 53-55
    sprite('rwi355_14', 3)	# 56-58
    sprite('rwi355_12', 4)	# 59-62
    sprite('rwi355_13', 4)	# 63-66
    sprite('rwi355_14', 4)	# 67-70
    sprite('rwi355_12', 5)	# 71-75
    sprite('rwi355_13', 5)	# 76-80
    sprite('rwi355_14', 5)	# 81-85
    sprite('rwi355_15', 5)	# 86-90
    sprite('rwi202_09ex01', 5)	# 91-95
    sprite('rwi202_10ex01', 5)	# 96-100
    sprite('rwi202_11ex01', 5)	# 101-105
    sprite('rwi202_12ex01', 5)	# 106-110

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(35)
        AttackP2(100)
        Unknown11064(1)
        Unknown11056(0)
        Unknown11001(0, 20, 20)
        Unknown9016(1)
        Unknown12051(2)
        setInvincible(1)

        def upon_78():
            Unknown11069('UltimateRushChase')
            Unknown23027()
            Unknown13024(0)
            enterState('UltimateRushChase')
            Unknown21012('727769656634333000000000000000000000000000000000000000000000000028000000')

        def upon_61():
            clearUponHandler(11)
            sendToLabel(1)
    sprite('rwi430_00', 6)	# 1-6
    tag_voice(1, 'rwi250_0', 'rwi250_1', 'rwi250_2', '')
    Unknown2036(70, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('rwi430_01', 6)	# 7-12
    sprite('rwi430_02', 6)	# 13-18
    sprite('rwi430_03', 6)	# 19-24
    sprite('rwi430_04', 4)	# 25-28
    sprite('rwi430_05', 4)	# 29-32
    SFX_3('rwise_43')
    sprite('rwi430_06', 4)	# 33-36
    GFX_0('rwief430', -1)
    sprite('rwi430_04', 4)	# 37-40
    sprite('rwi430_05', 4)	# 41-44
    sprite('rwi430_06', 4)	# 45-48
    sprite('rwi430_04', 4)	# 49-52
    sprite('rwi430_05', 4)	# 53-56
    sprite('rwi430_06', 4)	# 57-60
    sprite('rwi430_07', 8)	# 61-68
    sprite('rwi430_08', 8)	# 69-76
    sprite('rwi430_09', 8)	# 77-84
    SFX_3('rwise_45')
    sprite('vrrwi_UltimateRushAtk', 6)	# 85-90	 **attackbox here**
    Unknown2017(0)
    physicsXImpulse(125000)
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000020000000')
    label(1)
    sprite('vrrwi_UltimateRushAtk', 3)	# 91-93	 **attackbox here**
    StartMultihit()
    sprite('rwi408_05', 3)	# 94-96
    Unknown2017(1)
    setInvincible(0)
    Unknown1019(40)
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000029000000')
    sprite('rwi408_06', 5)	# 97-101
    Unknown1019(50)
    sprite('rwi408_07', 5)	# 102-106
    Unknown1019(50)
    sprite('rwi408_08', 5)	# 107-111
    Unknown1019(50)
    sprite('rwi408_09', 5)	# 112-116
    Unknown1019(50)
    sprite('rwi408_10', 5)	# 117-121
    Unknown1019(50)
    sprite('rwi408_11', 5)	# 122-126
    Unknown1084(1)

@State
def UltimateRushChase():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown11108('03000000')
        AttackLevel_(3)
        Damage(1000)
        Unknown11064(1)
        AttackP2(100)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        AirPushbackX(0)
        AirPushbackY(35000)
        setInvincible(1)
        Hitstop(1)
        Unknown11069('UltimateRushChase')
        Unknown30048(1)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20007(1)
        Unknown28(2, 'CmnActJumpLanding')
        Unknown11023(1)
        Unknown13024(0)
        Unknown23027()

        def upon_STATE_END():
            Unknown2053(1)
            Unknown2034(1)
            Unknown2017(1)
    sprite('vrrwi_UltimateRushAtk', 1)	# 1-1	 **attackbox here**
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-100000)
    Unknown1084(1)
    physicsXImpulse(100000)
    sprite('vrrwi_UltimateRushAtk', 4)	# 2-5	 **attackbox here**
    Unknown2017(0)
    sprite('rwi430_10', 3)	# 6-8
    Unknown1019(50)
    sprite('rwi430_11', 3)	# 9-11
    Unknown1019(50)
    sprite('rwi430_12', 3)	# 12-14
    Unknown1019(50)
    tag_voice(0, 'rwi251_0', 'rwi251_1', 'rwi251_2', '')
    sprite('vrrwi_UltimateRushAtk', 2)	# 15-16	 **attackbox here**
    physicsXImpulse(-250000)
    physicsYImpulse(50000)
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000021000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 17-17	 **attackbox here**
    Unknown1019(80)
    Unknown2017(0)
    RefreshMultihit()
    sprite('vrrwi_UltimateRushAtk', 2)	# 18-19	 **attackbox here**
    Unknown23027()
    sprite('rwi430_13', 3)	# 20-22
    Unknown1019(10)
    YAccel(1)
    sprite('rwi430_14', 3)	# 23-25
    Unknown1019(50)
    sprite('rwi430_15', 3)	# 26-28
    Unknown1019(50)
    sprite('vrrwi_UltimateRushAtk', 2)	# 29-30	 **attackbox here**
    physicsXImpulse(250000)
    physicsYImpulse(50000)
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000022000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 31-31	 **attackbox here**
    Unknown1019(80)
    Unknown2017(0)
    RefreshMultihit()
    sprite('vrrwi_UltimateRushAtk', 2)	# 32-33	 **attackbox here**
    Unknown23027()
    sprite('rwi430_16', 3)	# 34-36
    Unknown1019(10)
    YAccel(1)
    sprite('rwi430_17', 2)	# 37-38
    Unknown1019(90)
    sprite('rwi430_18', 2)	# 39-40
    Unknown1019(90)
    sprite('rwi430_19', 2)	# 41-42
    Unknown1019(90)
    sprite('vrrwi_UltimateRushAtk', 2)	# 43-44	 **attackbox here**
    physicsXImpulse(-250000)
    physicsYImpulse(50000)
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000023000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 45-45	 **attackbox here**
    Unknown1019(80)
    Unknown2017(0)
    RefreshMultihit()
    sprite('vrrwi_UltimateRushAtk', 2)	# 46-47	 **attackbox here**
    Unknown23027()
    sprite('rwi430_20', 3)	# 48-50
    Unknown1019(5)
    YAccel(1)
    sprite('rwi430_21', 3)	# 51-53
    Unknown1019(50)
    sprite('rwi430_22', 3)	# 54-56
    Unknown1019(50)
    sprite('vrrwi_UltimateRushAtk', 2)	# 57-58	 **attackbox here**
    physicsXImpulse(175000)
    physicsYImpulse(100000)
    Unknown1043()
    Unknown23027()
    Unknown2017(1)
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000024000000')
    SFX_3('rwise_45')
    sprite('vrrwi_UltimateRushAtk', 1)	# 59-59	 **attackbox here**
    Unknown2017(0)
    RefreshMultihit()
    AttackLevel_(4)
    AttackP2(60)
    Unknown11064(0)
    Unknown11056(0)
    AirPushbackX(10000)
    AirPushbackY(-60000)
    Unknown9190(1)
    Unknown9118(25)
    Hitstop(15)
    Unknown11069('')
    Unknown20007(0)
    sprite('rwi408_01', 3)	# 60-62
    Unknown2053(1)
    Unknown2034(1)
    Unknown2017(1)
    Unknown13024(1)
    Unknown1019(5)
    YAccel(20)
    sprite('rwi408_02', 3)	# 63-65
    Unknown1019(50)
    sprite('rwi430_23', 3)	# 66-68
    Unknown1019(50)
    sprite('rwi020_07', 3)	# 69-71
    sprite('rwi020_08', 3)	# 72-74
    label(0)
    sprite('rwi020_07', 3)	# 75-77
    sprite('rwi020_08', 3)	# 78-80
    gotoLabel(0)

@State
def UltimateRushSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(2000)
        Unknown11091(35)
        AttackP2(100)
        Unknown11064(1)
        Unknown11056(0)
        Unknown11001(0, 20, 20)
        Unknown9016(1)
        Unknown30082(1)
        Unknown12051(2)
        setInvincible(1)

        def upon_78():
            Unknown11069('UltimateRushSPChase')
            Unknown23027()
            Unknown13024(0)
            enterState('UltimateRushSPChase')
            Unknown21012('727769656634333000000000000000000000000000000000000000000000000028000000')

        def upon_61():
            clearUponHandler(11)
            sendToLabel(1)
    sprite('rwi430_00', 6)	# 1-6
    tag_voice(1, 'rwi250_0', 'rwi250_1', 'rwi250_2', '')
    Unknown2036(70, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('rwi430_01', 6)	# 7-12
    sprite('rwi430_02', 6)	# 13-18
    sprite('rwi430_03', 6)	# 19-24
    sprite('rwi430_04', 4)	# 25-28
    sprite('rwi430_05', 4)	# 29-32
    SFX_3('rwise_43')
    sprite('rwi430_06', 4)	# 33-36
    GFX_0('rwief430', -1)
    sprite('rwi430_04', 4)	# 37-40
    sprite('rwi430_05', 4)	# 41-44
    sprite('rwi430_06', 4)	# 45-48
    sprite('rwi430_04', 4)	# 49-52
    sprite('rwi430_05', 4)	# 53-56
    sprite('rwi430_06', 4)	# 57-60
    sprite('rwi430_07', 8)	# 61-68
    sprite('rwi430_08', 8)	# 69-76
    sprite('rwi430_09', 8)	# 77-84
    SFX_3('rwise_45')
    sprite('vrrwi_UltimateRushAtk', 6)	# 85-90	 **attackbox here**
    Unknown2017(0)
    physicsXImpulse(125000)
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000020000000')
    label(1)
    sprite('vrrwi_UltimateRushAtk', 3)	# 91-93	 **attackbox here**
    StartMultihit()
    sprite('rwi408_05', 3)	# 94-96
    Unknown2017(1)
    setInvincible(0)
    Unknown1019(40)
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000029000000')
    sprite('rwi408_06', 5)	# 97-101
    Unknown1019(50)
    sprite('rwi408_07', 5)	# 102-106
    Unknown1019(50)
    sprite('rwi408_08', 5)	# 107-111
    Unknown1019(50)
    sprite('rwi408_09', 5)	# 112-116
    Unknown1019(50)
    sprite('rwi408_10', 5)	# 117-121
    Unknown1019(50)
    sprite('rwi408_11', 5)	# 122-126
    Unknown1084(1)

@State
def UltimateRushSPChase():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown11108('03000000')
        AttackLevel_(3)
        Damage(1000)
        Unknown11064(1)
        AttackP2(100)
        Unknown9016(1)
        GroundedHitstunAnimation(1)
        AirUntechableTime(60)
        Hitstop(1)
        AirPushbackX(0)
        AirPushbackY(35000)
        Unknown30082(1)
        Unknown11069('UltimateRushSPChase')
        Unknown30048(1)
        Unknown13024(0)
        Unknown2053(0)
        Unknown2034(0)
        Unknown20003(1)
        Unknown20007(1)
        Unknown28(2, 'CmnActJumpLanding')
        Unknown11023(1)
        Unknown23027()

        def upon_STATE_END():
            Unknown2053(1)
            Unknown2034(1)
            Unknown2017(1)
        setInvincible(1)
    sprite('vrrwi_UltimateRushAtk', 1)	# 1-1	 **attackbox here**
    Unknown1086(22)
    teleportRelativeY(0)
    teleportRelativeX(-100000)
    Unknown1084(1)
    physicsXImpulse(100000)
    sprite('vrrwi_UltimateRushAtk', 4)	# 2-5	 **attackbox here**
    Unknown2017(0)
    sprite('rwi430_10', 3)	# 6-8
    Unknown1019(50)
    sprite('rwi430_11', 3)	# 9-11
    Unknown1019(50)
    sprite('rwi430_12', 3)	# 12-14
    Unknown1019(50)
    tag_voice(0, 'rwi251_0', 'rwi251_1', 'rwi251_2', '')
    sprite('vrrwi_UltimateRushAtk', 2)	# 15-16	 **attackbox here**
    physicsXImpulse(-250000)
    physicsYImpulse(50000)
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000021000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 17-17	 **attackbox here**
    Unknown1019(80)
    Unknown2017(0)
    RefreshMultihit()
    sprite('vrrwi_UltimateRushAtk', 2)	# 18-19	 **attackbox here**
    Unknown23027()
    sprite('rwi430_13', 3)	# 20-22
    Unknown1019(10)
    YAccel(1)
    sprite('rwi430_14', 3)	# 23-25
    Unknown1019(50)
    sprite('rwi430_15', 3)	# 26-28
    Unknown1019(50)
    sprite('vrrwi_UltimateRushAtk', 2)	# 29-30	 **attackbox here**
    physicsXImpulse(250000)
    physicsYImpulse(50000)
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000022000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 31-31	 **attackbox here**
    Unknown1019(80)
    Unknown2017(0)
    RefreshMultihit()
    sprite('vrrwi_UltimateRushAtk', 2)	# 32-33	 **attackbox here**
    Unknown23027()
    sprite('rwi430_16', 3)	# 34-36
    Unknown1019(10)
    YAccel(1)
    sprite('rwi430_17', 2)	# 37-38
    Unknown1019(90)
    sprite('rwi430_18', 2)	# 39-40
    Unknown1019(90)
    sprite('rwi430_19', 2)	# 41-42
    Unknown1019(90)
    sprite('vrrwi_UltimateRushAtk', 2)	# 43-44	 **attackbox here**
    physicsXImpulse(-250000)
    physicsYImpulse(50000)
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000023000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 45-45	 **attackbox here**
    Unknown1019(80)
    Unknown2017(0)
    RefreshMultihit()
    sprite('vrrwi_UltimateRushAtk', 2)	# 46-47	 **attackbox here**
    Unknown23027()
    sprite('rwi430_20', 3)	# 48-50
    Unknown1019(5)
    YAccel(1)
    sprite('rwi430_21', 3)	# 51-53
    Unknown1019(50)
    sprite('rwi430_22', 3)	# 54-56
    Unknown1019(50)
    sprite('vrrwi_UltimateRushAtk', 2)	# 57-58	 **attackbox here**
    physicsXImpulse(175000)
    physicsYImpulse(100000)
    Unknown1043()
    Unknown23027()
    Unknown2017(1)
    SFX_3('rwise_45')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000025000000')
    sprite('vrrwi_UltimateRushAtk', 1)	# 59-59	 **attackbox here**
    Unknown2017(0)
    RefreshMultihit()
    AttackLevel_(4)
    Unknown11056(0)
    AirPushbackX(2500)
    AirPushbackY(-60000)
    Unknown9190(1)
    Unknown9118(35)
    Hitstop(15)
    Unknown20007(0)
    Unknown20000(1)
    sprite('rwi430_24', 5)	# 60-64
    Unknown1019(1)
    YAccel(1)
    setGravity(0)
    sprite('rwi430_25', 5)	# 65-69
    Unknown1019(50)
    sprite('rwi430_26', 5)	# 70-74
    Unknown1019(50)
    sprite('rwi430_27', 5)	# 75-79
    Unknown1019(50)
    SFX_3('rwise_45')
    sprite('rwi430_28', 2)	# 80-81	 **attackbox here**
    Unknown20000(0)
    tag_voice(0, 'rwi252_0', 'rwi252_1', 'rwi252_2', '')
    RefreshMultihit()
    AttackP2(60)
    Unknown11092(1)
    Unknown11023(0)
    Damage(500)
    Unknown11091(10)
    Unknown11064(0)
    Hitstop(3)
    AirPushbackX(5000)
    Unknown11069('')
    Unknown21012('727769656634333000000000000000000000000000000000000000000000000026000000')
    physicsYImpulse(-90000)
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    label(0)
    sprite('rwi430_29', 2)	# 82-83	 **attackbox here**
    RefreshMultihit()
    sprite('rwi430_30', 2)	# 84-85	 **attackbox here**
    RefreshMultihit()
    sprite('rwi430_31', 2)	# 86-87	 **attackbox here**
    RefreshMultihit()
    sprite('rwi430_28', 2)	# 88-89	 **attackbox here**
    RefreshMultihit()
    gotoLabel(0)
    label(1)
    sprite('rwi430_32', 5)	# 90-94
    Unknown2053(1)
    Unknown2034(1)
    Unknown2017(1)
    Unknown13024(1)
    sprite('rwi430_33', 5)	# 95-99
    sprite('rwi430_34', 32767)	# 100-32866
    physicsXImpulse(-5000)
    physicsYImpulse(7500)
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(2)
    label(2)
    sprite('rwi430_35', 3)	# 32867-32869
    Unknown18009(1)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('rwi430_36', 3)	# 32870-32872
    sprite('rwi430_37', 3)	# 32873-32875
    sprite('rwi430_38', 3)	# 32876-32878
    sprite('rwi430_39', 3)	# 32879-32881

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        loopRelated(17, 70)

        def upon_17():
            sendToLabel(1)
        AttackLevel_(4)
        Damage(0)
        Unknown11064(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(220)
        Unknown9142(200)
        PushbackX(9800)
        Unknown11091(100)
        Unknown9021(1)
        Unknown11072(1, 500000, 0)
        Unknown11069('AstralAtkSecond')
        Unknown11067(1)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown11034(0)
        Unknown11033(2)
        Unknown23027()

        def upon_78():
            Unknown23088(1, 1)
            Unknown11069('AstralAtkSecond')
            enterState('AstralHeatExe')
            GFX_0('rwief450_Glyph_Hit', -1)
            Unknown21012('72776965663435305f317374000000000000000000000000000000000000000020000000')
    sprite('rwi450_00', 3)	# 1-3
    setInvincible(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2036(60, -1, 2)
    Unknown23147()
    sprite('rwi450_01', 3)	# 4-6	 **attackbox here**
    tag_voice(1, 'rwi290_0', 'rwi290_1', '', '')
    sprite('rwi450_02', 3)	# 7-9	 **attackbox here**
    sprite('rwi450_03', 3)	# 10-12	 **attackbox here**
    GFX_0('rwief450_1st', -1)
    label(0)
    sprite('rwi450_01', 3)	# 13-15	 **attackbox here**
    sprite('rwi450_02', 3)	# 16-18	 **attackbox here**
    sprite('rwi450_03', 3)	# 19-21	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('rwi450_01', 4)	# 22-25	 **attackbox here**
    RefreshMultihit()
    sprite('rwi450_02', 4)	# 26-29	 **attackbox here**
    sprite('rwi450_03', 4)	# 30-33	 **attackbox here**
    sprite('rwi450_01', 5)	# 34-38	 **attackbox here**
    sprite('rwi450_02', 5)	# 39-43	 **attackbox here**
    Unknown23027()
    setInvincible(0)
    Unknown21012('72776965663435305f317374000000000000000000000000000000000000000029000000')
    sprite('rwi450_03', 5)	# 44-48	 **attackbox here**
    sprite('rwi450_01', 6)	# 49-54	 **attackbox here**
    sprite('rwi450_02', 6)	# 55-60	 **attackbox here**
    sprite('rwi450_03', 6)	# 61-66	 **attackbox here**
    sprite('rwi450_00', 6)	# 67-72

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23157(0)
        Unknown23084(1)
        Unknown2017(0)
        Unknown2034(0)
        Unknown2053(0)
        setInvincible(1)
        AttackLevel_(5)
        Damage(4500)
        Unknown11064(1)
        Hitstop(0)
        Unknown11091(100)
        Unknown9016(1)
        Unknown11067(1)
        Unknown11001(300, 300, 300)
        Unknown11032('400d0300c0f2fcffc0f2fcff400d0300')
        Unknown11072(1, 300000, -250000)
        loopRelated(17, 310)

        def upon_17():
            sendToLabel(3)

        def upon_78():
            Unknown20000(0)
            Unknown20001(0)
            GFX_0('AstralLastCamera', -1)

        def upon_43():
            if (SLOT_48 == 4502):
                SLOT_51 = (SLOT_51 + 1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown20000(0)
            Unknown8000(100, 1, 1)
            sendToLabel(5)
    sprite('rwi450_01', 4)	# 1-4	 **attackbox here**
    GFX_0('AstralFirstCamera', -1)
    Unknown38(11, 1)
    sprite('rwi450_02', 4)	# 5-8	 **attackbox here**
    sprite('rwi450_03', 4)	# 9-12	 **attackbox here**
    sprite('rwi450_01', 4)	# 13-16	 **attackbox here**
    sprite('rwi450_02', 4)	# 17-20	 **attackbox here**
    sprite('rwi450_03', 4)	# 21-24	 **attackbox here**
    sprite('rwi450_01', 4)	# 25-28	 **attackbox here**
    sprite('rwi450_02', 4)	# 29-32	 **attackbox here**
    sprite('rwi450_03', 4)	# 33-36	 **attackbox here**
    sprite('rwi450_04', 4)	# 37-40
    GFX_0('rwief450_2nd', -1)
    SFX_3('rwise_42')
    sprite('rwi450_05', 4)	# 41-44
    GFX_0('AstralAtkSecond', -1)
    GFX_0('rwief450_Glyph_Hit', -1)
    sprite('rwi450_06', 6)	# 45-50
    tag_voice(0, 'rwi291_0', 'rwi291_1', '', '')
    sprite('rwi450_07', 6)	# 51-56
    Unknown23024(3)
    sprite('rwi450_08', 6)	# 57-62
    sprite('rwi450_09', 8)	# 63-70
    sprite('rwi450_10', 8)	# 71-78
    sprite('rwi450_11', 8)	# 79-86
    sprite('rwi450_12', 4)	# 87-90
    label(0)
    sprite('rwi450_13', 3)	# 91-93
    GFX_0('AstralAtkShotRush', -1)
    if (SLOT_51 == 11):
        Unknown23029(1, 4503, 0)
        sendToLabel(1)
    sprite('rwi450_14', 3)	# 94-96
    sprite('rwi450_15', 3)	# 97-99
    gotoLabel(0)
    label(1)
    sprite('rwi450_14', 3)	# 100-102
    GFX_0('rwief450_3rd', -1)
    sprite('rwi450_15', 3)	# 103-105
    sprite('rwi407_00', 3)	# 106-108
    Unknown23029(11, 4504, 0)
    Unknown20000(1)
    Unknown20003(1)
    Unknown20004(1)
    sprite('rwi407_01', 3)	# 109-111
    sprite('rwi407_02', 3)	# 112-114
    sprite('rwi407_03', 3)	# 115-117
    sprite('rwi407_04', 3)	# 118-120
    SFX_3('rwise_44')
    sprite('rwi020_00', 3)	# 121-123
    physicsXImpulse(-15000)
    physicsYImpulse(55000)
    setGravity(1000)
    sprite('rwi020_01', 3)	# 124-126
    sprite('rwi020_00', 3)	# 127-129
    sprite('rwi020_01', 3)	# 130-132
    sprite('rwi020_00', 3)	# 133-135
    sprite('rwi020_01', 3)	# 136-138
    sprite('rwi020_00', 3)	# 139-141
    sprite('rwi020_01', 3)	# 142-144
    SFX_3('rwise_42')
    sprite('rwi408_00', 6)	# 145-150
    Unknown1019(50)
    sprite('rwi408_01', 6)	# 151-156
    Unknown1019(50)
    tag_voice(0, 'rwi292_0', 'rwi292_1', '', '')
    sprite('rwi450_16', 6)	# 157-162
    Unknown1084(1)
    label(2)
    sprite('rwi450_17', 4)	# 163-166
    sprite('rwi450_18', 4)	# 167-170
    sprite('rwi450_19', 4)	# 171-174
    gotoLabel(2)
    label(3)
    sprite('rwi450_20', 6)	# 175-180
    physicsXImpulse(5000)
    setGravity(0)
    Unknown20001(1)
    SFX_3('rwise_45')
    SFX_3('rwise_53')
    sprite('rwi450_21', 6)	# 181-186
    sprite('rwi450_22', 3)	# 187-189	 **attackbox here**
    Unknown47('0300000002000000130000000000000008000000020000000c000000')
    physicsYImpulse(-120000)

    def upon_43():
        if (SLOT_48 == 4505):
            clearUponHandler(43)
            sendToLabel(100)

    def upon_12():
        GFX_0('AstralAtkFinal', -1)
    sprite('rwi450_23', 3)	# 190-192	 **attackbox here**
    tag_voice(0, 'rwi293_0', 'rwi293_1', '', '')
    label(4)
    sprite('rwi450_22', 3)	# 193-195	 **attackbox here**
    sprite('rwi450_23', 3)	# 196-198	 **attackbox here**
    gotoLabel(4)
    label(5)
    sprite('rwi408_05', 3)	# 199-201
    Unknown1019(15)
    sprite('rwi408_06', 3)	# 202-204
    Unknown1019(15)
    Unknown21012('72776965663435305f337264000000000000000000000000000000000000000020000000')
    sprite('rwi408_07', 2)	# 205-206
    Unknown1019(50)
    sprite('rwi408_08', 2)	# 207-208
    Unknown1019(50)
    sprite('rwi408_06', 2)	# 209-210
    Unknown1084(1)
    sprite('rwi408_07', 3)	# 211-213
    sprite('rwi408_08', 3)	# 214-216
    sprite('rwi408_06', 3)	# 217-219
    label(6)
    sprite('rwi408_07', 4)	# 220-223
    sprite('rwi408_08', 4)	# 224-227
    sprite('rwi408_06', 4)	# 228-231
    gotoLabel(6)
    label(100)
    sprite('keep', 3)	# 232-234
    GFX_0('rwief450_SnowFall', -1)
    Unknown1000(260000)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20006(1)
    Unknown23024(0)
    sprite('rwi408_09', 5)	# 235-239
    sprite('rwi408_10', 5)	# 240-244
    sprite('rwi408_11', 5)	# 245-249

@Subroutine
def MouthTableInit():
    Unknown18011('rwi000', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi500', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi502', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi503', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi504', 13155, 12336, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi520', 12643, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi521', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi522', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi523', 12643, 14177, 14179, 14177, 14179, 14177, 13667, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi403_0', 12899, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi403_1', 13667, 24884, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi601bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi601bph', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600bpt', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600pmi', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12593, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi601pna', 12643, 12897, 25397, 24887, 25399, 12851, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi601pyu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12340, 14177, 14179, 12641, 25392, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600rrb', 12643, 14177, 14179, 12641, 25396, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi603', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600ryn', 12643, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi601uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi600uva', 12643, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi605', 12643, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701bha', 12643, 14177, 14179, 14177, 13411, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701bmk', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701bny', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701bph', 12643, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701bpt', 12643, 14177, 13411, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi700pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701pmi', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi700pna', 12643, 14177, 14179, 14177, 14179, 12641, 25396, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701pyu', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi700rbl', 12643, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi700rwi', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701ryn', 13667, 12641, 25394, 12340, 14177, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi700uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi701uva', 12643, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 12341, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi702pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24884, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('rwi702uor', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    if Unknown70('727262000000000000000000000000007277690000000000000000000000000072626c0000000000000000000000000072796e00000000000000000000000000'):
        SLOT_171 = 1
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
    if SLOT_171:
        _gotolabel(1000)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('bha')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('pbc')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pyu')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('bmk')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('uor')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('uva')
    if SLOT_0:
        _gotolabel(200)
    PartnerChar('ryn')
    if SLOT_0:
        _gotolabel(210)
    PartnerChar('pmi')
    if SLOT_0:
        _gotolabel(220)
    PartnerChar('bph')
    if SLOT_0:
        _gotolabel(230)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('rwi600_00', 6)	# 2-7
    sprite('rwi600_01', 6)	# 8-13
    sprite('rwi600_02', 6)	# 14-19
    sprite('rwi600_03', 6)	# 20-25
    sprite('rwi600_04', 6)	# 26-31
    if SLOT_158:
        Unknown7006('rwi501', 100, 896104306, 12848, 0, 0, 100, 896104306, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('rwi600_05', 6)	# 32-37
    sprite('rwi600_06', 6)	# 38-43
    sprite('rwi600_07', 6)	# 44-49
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 50-55
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 56-61
    sprite('rwi600_10', 6)	# 62-67
    sprite('rwi600_11', 6)	# 68-73
    label(1)
    sprite('rwi000_00', 6)	# 74-79
    sprite('rwi000_01', 6)	# 80-85
    sprite('rwi000_02', 6)	# 86-91
    sprite('rwi000_03', 6)	# 92-97
    sprite('rwi000_04', 6)	# 98-103
    sprite('rwi000_05', 6)	# 104-109
    sprite('rwi000_06', 6)	# 110-115
    sprite('rwi000_07', 6)	# 116-121
    sprite('rwi000_08', 6)	# 122-127
    sprite('rwi000_09', 6)	# 128-133
    sprite('rwi000_10', 6)	# 134-139
    if SLOT_97:
        _gotolabel(1)
    sprite('rwi000_00', 6)	# 140-145
    Unknown21007(24, 41)
    sprite('rwi000_01', 6)	# 146-151
    sprite('rwi000_02', 6)	# 152-157
    sprite('rwi000_03', 6)	# 158-163
    sprite('rwi000_04', 6)	# 164-169
    sprite('rwi000_05', 6)	# 170-175
    sprite('rwi000_06', 6)	# 176-181
    sprite('rwi000_07', 6)	# 182-187
    sprite('rwi000_08', 6)	# 188-193
    sprite('rwi000_09', 6)	# 194-199
    sprite('rwi000_10', 6)	# 200-205
    loopRest()
    ExitState()
    label(10)
    sprite('rwi601_00', 1)	# 206-206
    if SLOT_158:
        Unknown7006('rwi500', 100, 896104306, 13104, 0, 0, 100, 896104306, 13360, 0, 0, 100, 0, 0, 0, 0, 0)
    GFX_0('rwief601', -1)
    label(11)
    sprite('rwi601_00', 1)	# 207-207
    if SLOT_97:
        _gotolabel(11)
    sprite('rwi601_01', 6)	# 208-213
    Unknown21007(24, 41)
    sprite('rwi601_02', 6)	# 214-219
    Unknown21012('727769656636303100000000000000000000000000000000000000000000000020000000')
    sprite('rwi601_03', 6)	# 220-225
    sprite('rwi601_04', 6)	# 226-231
    sprite('rwi601_05', 6)	# 232-237
    sprite('rwi601_06', 6)	# 238-243
    sprite('rwi601_07', 6)	# 244-249
    loopRest()
    ExitState()
    label(20)
    sprite('rwi000_00', 1)	# 250-250
    SFX_1('rwi603')
    label(21)
    sprite('rwi000_00', 5)	# 251-255
    sprite('rwi000_01', 6)	# 256-261
    sprite('rwi000_02', 6)	# 262-267
    sprite('rwi000_03', 6)	# 268-273
    sprite('rwi000_04', 6)	# 274-279
    sprite('rwi000_05', 6)	# 280-285
    sprite('rwi000_06', 6)	# 286-291
    sprite('rwi000_07', 6)	# 292-297
    sprite('rwi000_08', 6)	# 298-303
    sprite('rwi000_09', 6)	# 304-309
    sprite('rwi000_10', 6)	# 310-315
    gotoLabel(21)
    label(100)
    sprite('rwi600_00', 6)	# 316-321
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rwi600_01', 6)	# 322-327
    SFX_1('rwi600bpt')
    sprite('rwi600_02', 6)	# 328-333
    sprite('rwi600_03', 6)	# 334-339
    sprite('rwi600_04', 6)	# 340-345
    sprite('rwi600_05', 6)	# 346-351
    sprite('rwi600_06', 6)	# 352-357
    sprite('rwi600_07', 6)	# 358-363
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 364-369
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 370-375
    sprite('rwi600_10', 6)	# 376-381
    sprite('rwi600_11', 6)	# 382-387
    label(101)
    sprite('rwi000_00', 6)	# 388-393
    sprite('rwi000_01', 6)	# 394-399
    sprite('rwi000_02', 6)	# 400-405
    sprite('rwi000_03', 6)	# 406-411
    sprite('rwi000_04', 6)	# 412-417
    sprite('rwi000_05', 6)	# 418-423
    sprite('rwi000_06', 6)	# 424-429
    sprite('rwi000_07', 6)	# 430-435
    sprite('rwi000_08', 6)	# 436-441
    sprite('rwi000_09', 6)	# 442-447
    sprite('rwi000_10', 6)	# 448-453
    if SLOT_97:
        _gotolabel(101)
    sprite('rwi000_00', 1)	# 454-454
    Unknown21007(24, 40)
    Unknown21011(240)
    label(102)
    sprite('rwi000_00', 6)	# 455-460
    sprite('rwi000_01', 6)	# 461-466
    sprite('rwi000_02', 6)	# 467-472
    sprite('rwi000_03', 6)	# 473-478
    sprite('rwi000_04', 6)	# 479-484
    sprite('rwi000_05', 6)	# 485-490
    sprite('rwi000_06', 6)	# 491-496
    sprite('rwi000_07', 6)	# 497-502
    sprite('rwi000_08', 6)	# 503-508
    sprite('rwi000_09', 6)	# 509-514
    sprite('rwi000_10', 6)	# 515-520
    gotoLabel(102)
    ExitState()
    label(110)
    sprite('rwi000_00', 1)	# 521-521
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1505000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('rwi000_00', 6)	# 522-527
    sprite('rwi000_01', 6)	# 528-533
    sprite('rwi000_02', 6)	# 534-539
    sprite('rwi000_03', 6)	# 540-545
    sprite('rwi000_04', 6)	# 546-551
    sprite('rwi000_05', 6)	# 552-557
    sprite('rwi000_06', 6)	# 558-563
    sprite('rwi000_07', 6)	# 564-569
    sprite('rwi000_08', 6)	# 570-575
    sprite('rwi000_09', 6)	# 576-581
    sprite('rwi000_10', 6)	# 582-587
    gotoLabel(111)
    label(112)
    sprite('rwi600_00', 6)	# 588-593
    sprite('rwi600_01', 6)	# 594-599
    sprite('rwi600_02', 6)	# 600-605
    sprite('rwi600_03', 6)	# 606-611
    sprite('rwi600_04', 6)	# 612-617
    SFX_1('rwi601bha')
    sprite('rwi600_05', 6)	# 618-623
    sprite('rwi600_06', 6)	# 624-629
    sprite('rwi600_07', 6)	# 630-635
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 636-641
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 642-647
    sprite('rwi600_10', 6)	# 648-653
    sprite('rwi600_11', 6)	# 654-659
    Unknown23018(1)
    label(113)
    sprite('rwi000_00', 6)	# 660-665
    sprite('rwi000_01', 6)	# 666-671
    sprite('rwi000_02', 6)	# 672-677
    sprite('rwi000_03', 6)	# 678-683
    sprite('rwi000_04', 6)	# 684-689
    sprite('rwi000_05', 6)	# 690-695
    sprite('rwi000_06', 6)	# 696-701
    sprite('rwi000_07', 6)	# 702-707
    sprite('rwi000_08', 6)	# 708-713
    sprite('rwi000_09', 6)	# 714-719
    sprite('rwi000_10', 6)	# 720-725
    gotoLabel(113)
    ExitState()
    label(120)
    sprite('rwi601_00', 1)	# 726-726
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rwi600bny')
    label(121)
    sprite('rwi601_00', 1)	# 727-727
    if SLOT_97:
        _gotolabel(121)
    sprite('rwi601_01', 6)	# 728-733
    sprite('rwi601_02', 6)	# 734-739
    sprite('rwi601_03', 6)	# 740-745
    sprite('rwi601_04', 6)	# 746-751
    sprite('rwi601_05', 6)	# 752-757
    sprite('rwi601_06', 6)	# 758-763
    sprite('rwi601_07', 6)	# 764-769
    Unknown21007(24, 40)
    Unknown21011(60)
    label(122)
    sprite('rwi000_00', 6)	# 770-775
    sprite('rwi000_01', 6)	# 776-781
    sprite('rwi000_02', 6)	# 782-787
    sprite('rwi000_03', 6)	# 788-793
    sprite('rwi000_04', 6)	# 794-799
    sprite('rwi000_05', 6)	# 800-805
    sprite('rwi000_06', 6)	# 806-811
    sprite('rwi000_07', 6)	# 812-817
    sprite('rwi000_08', 6)	# 818-823
    sprite('rwi000_09', 6)	# 824-829
    sprite('rwi000_10', 6)	# 830-835
    gotoLabel(122)
    ExitState()
    label(130)
    sprite('rwi600_00', 6)	# 836-841
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rwi600_01', 6)	# 842-847
    SFX_1('rwi600pbc')
    sprite('rwi600_02', 6)	# 848-853
    sprite('rwi600_03', 6)	# 854-859
    sprite('rwi600_04', 6)	# 860-865
    sprite('rwi600_05', 6)	# 866-871
    sprite('rwi600_06', 6)	# 872-877
    sprite('rwi600_07', 6)	# 878-883
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 884-889
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 890-895
    sprite('rwi600_10', 6)	# 896-901
    sprite('rwi600_11', 6)	# 902-907
    label(131)
    sprite('rwi000_00', 6)	# 908-913
    sprite('rwi000_01', 6)	# 914-919
    sprite('rwi000_02', 6)	# 920-925
    sprite('rwi000_03', 6)	# 926-931
    sprite('rwi000_04', 6)	# 932-937
    sprite('rwi000_05', 6)	# 938-943
    sprite('rwi000_06', 6)	# 944-949
    sprite('rwi000_07', 6)	# 950-955
    sprite('rwi000_08', 6)	# 956-961
    sprite('rwi000_09', 6)	# 962-967
    sprite('rwi000_10', 6)	# 968-973
    if SLOT_97:
        _gotolabel(131)
    sprite('rwi000_00', 1)	# 974-974
    Unknown21007(24, 40)
    Unknown21011(60)
    label(132)
    sprite('rwi000_00', 6)	# 975-980
    sprite('rwi000_01', 6)	# 981-986
    sprite('rwi000_02', 6)	# 987-992
    sprite('rwi000_03', 6)	# 993-998
    sprite('rwi000_04', 6)	# 999-1004
    sprite('rwi000_05', 6)	# 1005-1010
    sprite('rwi000_06', 6)	# 1011-1016
    sprite('rwi000_07', 6)	# 1017-1022
    sprite('rwi000_08', 6)	# 1023-1028
    sprite('rwi000_09', 6)	# 1029-1034
    sprite('rwi000_10', 6)	# 1035-1040
    gotoLabel(132)
    ExitState()
    label(140)
    sprite('rwi000_00', 1)	# 1041-1041
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1665000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    Unknown2019(-1000)
    label(141)
    sprite('rwi000_00', 6)	# 1042-1047
    sprite('rwi000_01', 6)	# 1048-1053
    sprite('rwi000_02', 6)	# 1054-1059
    sprite('rwi000_03', 6)	# 1060-1065
    sprite('rwi000_04', 6)	# 1066-1071
    sprite('rwi000_05', 6)	# 1072-1077
    sprite('rwi000_06', 6)	# 1078-1083
    sprite('rwi000_07', 6)	# 1084-1089
    sprite('rwi000_08', 6)	# 1090-1095
    sprite('rwi000_09', 6)	# 1096-1101
    sprite('rwi000_10', 6)	# 1102-1107
    gotoLabel(141)
    label(142)
    sprite('rwi600_00', 6)	# 1108-1113
    SFX_1('rwi601pyu')
    sprite('rwi600_01', 6)	# 1114-1119
    sprite('rwi600_02', 6)	# 1120-1125
    sprite('rwi600_03', 6)	# 1126-1131
    sprite('rwi600_04', 6)	# 1132-1137
    sprite('rwi600_05', 6)	# 1138-1143
    sprite('rwi600_06', 6)	# 1144-1149
    sprite('rwi600_07', 6)	# 1150-1155
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 1156-1161
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 1162-1167
    sprite('rwi600_10', 6)	# 1168-1173
    sprite('rwi600_11', 6)	# 1174-1179
    Unknown21011(320)
    label(143)
    sprite('rwi000_00', 6)	# 1180-1185
    sprite('rwi000_01', 6)	# 1186-1191
    sprite('rwi000_02', 6)	# 1192-1197
    sprite('rwi000_03', 6)	# 1198-1203
    sprite('rwi000_04', 6)	# 1204-1209
    sprite('rwi000_05', 6)	# 1210-1215
    sprite('rwi000_06', 6)	# 1216-1221
    sprite('rwi000_07', 6)	# 1222-1227
    sprite('rwi000_08', 6)	# 1228-1233
    sprite('rwi000_09', 6)	# 1234-1239
    sprite('rwi000_10', 6)	# 1240-1245
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('rwi600_00', 6)	# 1246-1251
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rwi600_01', 6)	# 1252-1257
    SFX_1('rwi600rrb')
    sprite('rwi600_02', 6)	# 1258-1263
    sprite('rwi600_03', 6)	# 1264-1269
    sprite('rwi600_04', 6)	# 1270-1275
    sprite('rwi600_05', 6)	# 1276-1281
    sprite('rwi600_06', 6)	# 1282-1287
    sprite('rwi600_07', 6)	# 1288-1293
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 1294-1299
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 1300-1305
    sprite('rwi600_10', 6)	# 1306-1311
    sprite('rwi600_11', 6)	# 1312-1317
    label(151)
    sprite('rwi000_00', 6)	# 1318-1323
    sprite('rwi000_01', 6)	# 1324-1329
    sprite('rwi000_02', 6)	# 1330-1335
    sprite('rwi000_03', 6)	# 1336-1341
    sprite('rwi000_04', 6)	# 1342-1347
    sprite('rwi000_05', 6)	# 1348-1353
    sprite('rwi000_06', 6)	# 1354-1359
    sprite('rwi000_07', 6)	# 1360-1365
    sprite('rwi000_08', 6)	# 1366-1371
    sprite('rwi000_09', 6)	# 1372-1377
    sprite('rwi000_10', 6)	# 1378-1383
    if SLOT_97:
        _gotolabel(151)
    sprite('rwi000_00', 1)	# 1384-1384
    Unknown21007(24, 40)
    Unknown21011(120)
    label(152)
    sprite('rwi000_00', 6)	# 1385-1390
    sprite('rwi000_01', 6)	# 1391-1396
    sprite('rwi000_02', 6)	# 1397-1402
    sprite('rwi000_03', 6)	# 1403-1408
    sprite('rwi000_04', 6)	# 1409-1414
    sprite('rwi000_05', 6)	# 1415-1420
    sprite('rwi000_06', 6)	# 1421-1426
    sprite('rwi000_07', 6)	# 1427-1432
    sprite('rwi000_08', 6)	# 1433-1438
    sprite('rwi000_09', 6)	# 1439-1444
    sprite('rwi000_10', 6)	# 1445-1450
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('rwi600_00', 6)	# 1451-1456
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rwi600_01', 6)	# 1457-1462
    SFX_1('rwi600rbl')
    sprite('rwi600_02', 6)	# 1463-1468
    sprite('rwi600_03', 6)	# 1469-1474
    sprite('rwi600_04', 6)	# 1475-1480
    sprite('rwi600_05', 6)	# 1481-1486
    sprite('rwi600_06', 6)	# 1487-1492
    sprite('rwi600_07', 6)	# 1493-1498
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 1499-1504
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 1505-1510
    sprite('rwi600_10', 6)	# 1511-1516
    sprite('rwi600_11', 6)	# 1517-1522
    Unknown21011(120)
    label(161)
    sprite('rwi000_00', 6)	# 1523-1528
    sprite('rwi000_01', 6)	# 1529-1534
    sprite('rwi000_02', 6)	# 1535-1540
    sprite('rwi000_03', 6)	# 1541-1546
    sprite('rwi000_04', 6)	# 1547-1552
    sprite('rwi000_05', 6)	# 1553-1558
    Unknown21007(24, 40)
    sprite('rwi000_06', 6)	# 1559-1564
    sprite('rwi000_07', 6)	# 1565-1570
    sprite('rwi000_08', 6)	# 1571-1576
    sprite('rwi000_09', 6)	# 1577-1582
    sprite('rwi000_10', 6)	# 1583-1588
    gotoLabel(161)
    ExitState()
    label(170)
    sprite('rwi000_00', 1)	# 1589-1589
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('rwi000_00', 6)	# 1590-1595
    sprite('rwi000_01', 6)	# 1596-1601
    sprite('rwi000_02', 6)	# 1602-1607
    sprite('rwi000_03', 6)	# 1608-1613
    sprite('rwi000_04', 6)	# 1614-1619
    sprite('rwi000_05', 6)	# 1620-1625
    sprite('rwi000_06', 6)	# 1626-1631
    sprite('rwi000_07', 6)	# 1632-1637
    sprite('rwi000_08', 6)	# 1638-1643
    sprite('rwi000_09', 6)	# 1644-1649
    sprite('rwi000_10', 6)	# 1650-1655
    gotoLabel(171)
    label(172)
    sprite('rwi003_00', 3)	# 1656-1658
    Unknown2005()
    sprite('rwi003_01', 3)	# 1659-1661
    sprite('rwi003_00ex01', 3)	# 1662-1664
    sprite('rwi300_00', 6)	# 1665-1670
    sprite('rwi300_01', 6)	# 1671-1676
    sprite('rwi300_02', 6)	# 1677-1682
    sprite('rwi300_03', 6)	# 1683-1688
    sprite('rwi300_04', 6)	# 1689-1694
    SFX_1('rwi601pna')
    sprite('rwi300_05', 6)	# 1695-1700
    sprite('rwi300_06', 6)	# 1701-1706
    sprite('rwi300_07', 6)	# 1707-1712
    sprite('rwi300_08', 6)	# 1713-1718
    sprite('rwi300_06', 6)	# 1719-1724
    sprite('rwi300_07', 6)	# 1725-1730
    sprite('rwi300_08', 6)	# 1731-1736
    label(173)
    sprite('rwi300_06', 6)	# 1737-1742
    sprite('rwi300_07', 6)	# 1743-1748
    sprite('rwi300_08', 6)	# 1749-1754
    if SLOT_97:
        _gotolabel(173)
    sprite('rwi300_09', 6)	# 1755-1760
    sprite('rwi300_10', 6)	# 1761-1766
    Unknown23018(1)
    label(174)
    sprite('rwi000_00', 6)	# 1767-1772
    sprite('rwi000_01', 6)	# 1773-1778
    sprite('rwi000_02', 6)	# 1779-1784
    sprite('rwi000_03', 6)	# 1785-1790
    sprite('rwi000_04', 6)	# 1791-1796
    sprite('rwi000_05', 6)	# 1797-1802
    sprite('rwi000_06', 6)	# 1803-1808
    sprite('rwi000_07', 6)	# 1809-1814
    sprite('rwi000_08', 6)	# 1815-1820
    sprite('rwi000_09', 6)	# 1821-1826
    sprite('rwi000_10', 6)	# 1827-1832
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('rwi601_00', 80)	# 1833-1912
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rwi600bmk')
    sprite('rwi601_01', 6)	# 1913-1918
    sprite('rwi601_02', 6)	# 1919-1924
    sprite('rwi601_03', 6)	# 1925-1930
    sprite('rwi601_04', 6)	# 1931-1936
    sprite('rwi601_05', 6)	# 1937-1942
    sprite('rwi601_06', 6)	# 1943-1948
    sprite('rwi601_07', 6)	# 1949-1954
    label(181)
    sprite('rwi000_00', 6)	# 1955-1960
    sprite('rwi000_01', 6)	# 1961-1966
    sprite('rwi000_02', 6)	# 1967-1972
    sprite('rwi000_03', 6)	# 1973-1978
    sprite('rwi000_04', 6)	# 1979-1984
    sprite('rwi000_05', 6)	# 1985-1990
    sprite('rwi000_06', 6)	# 1991-1996
    sprite('rwi000_07', 6)	# 1997-2002
    sprite('rwi000_08', 6)	# 2003-2008
    sprite('rwi000_09', 6)	# 2009-2014
    sprite('rwi000_10', 6)	# 2015-2020
    if SLOT_97:
        _gotolabel(181)
    sprite('rwi000_00', 1)	# 2021-2021
    Unknown21007(24, 40)
    Unknown21011(120)
    label(182)
    sprite('rwi000_00', 6)	# 2022-2027
    sprite('rwi000_01', 6)	# 2028-2033
    sprite('rwi000_02', 6)	# 2034-2039
    sprite('rwi000_03', 6)	# 2040-2045
    sprite('rwi000_04', 6)	# 2046-2051
    sprite('rwi000_05', 6)	# 2052-2057
    sprite('rwi000_06', 6)	# 2058-2063
    sprite('rwi000_07', 6)	# 2064-2069
    sprite('rwi000_08', 6)	# 2070-2075
    sprite('rwi000_09', 6)	# 2076-2081
    sprite('rwi000_10', 6)	# 2082-2087
    gotoLabel(182)
    ExitState()
    label(190)
    sprite('rwi601_00', 32767)	# 2088-34854
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(191)
        SFX_1('rwi601uor')
    label(191)
    sprite('rwi601_00', 100)	# 34855-34954
    sprite('rwi601_01', 6)	# 34955-34960
    sprite('rwi601_02', 6)	# 34961-34966
    Unknown21012('727769656636303100000000000000000000000000000000000000000000000020000000')
    sprite('rwi601_03', 6)	# 34967-34972
    sprite('rwi601_04', 6)	# 34973-34978
    sprite('rwi601_05', 6)	# 34979-34984
    sprite('rwi601_06', 6)	# 34985-34990
    sprite('rwi601_07', 6)	# 34991-34996
    Unknown21011(240)
    label(192)
    sprite('rwi000_00', 6)	# 34997-35002
    sprite('rwi000_01', 6)	# 35003-35008
    sprite('rwi000_02', 6)	# 35009-35014
    sprite('rwi000_03', 6)	# 35015-35020
    sprite('rwi000_04', 6)	# 35021-35026
    sprite('rwi000_05', 6)	# 35027-35032
    sprite('rwi000_06', 6)	# 35033-35038
    sprite('rwi000_07', 6)	# 35039-35044
    sprite('rwi000_08', 6)	# 35045-35050
    sprite('rwi000_09', 6)	# 35051-35056
    sprite('rwi000_10', 6)	# 35057-35062
    gotoLabel(192)
    ExitState()
    label(200)
    sprite('rwi601_00', 80)	# 35063-35142
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('rwi600uva')
    sprite('rwi601_01', 6)	# 35143-35148
    sprite('rwi601_02', 6)	# 35149-35154
    sprite('rwi601_03', 6)	# 35155-35160
    sprite('rwi601_04', 6)	# 35161-35166
    sprite('rwi601_05', 6)	# 35167-35172
    sprite('rwi601_06', 6)	# 35173-35178
    sprite('rwi601_07', 6)	# 35179-35184
    Unknown21007(24, 40)
    Unknown21011(360)
    label(201)
    sprite('rwi000_00', 6)	# 35185-35190
    sprite('rwi000_01', 6)	# 35191-35196
    sprite('rwi000_02', 6)	# 35197-35202
    sprite('rwi000_03', 6)	# 35203-35208
    sprite('rwi000_04', 6)	# 35209-35214
    sprite('rwi000_05', 6)	# 35215-35220
    sprite('rwi000_06', 6)	# 35221-35226
    sprite('rwi000_07', 6)	# 35227-35232
    sprite('rwi000_08', 6)	# 35233-35238
    sprite('rwi000_09', 6)	# 35239-35244
    sprite('rwi000_10', 6)	# 35245-35250
    gotoLabel(201)
    ExitState()
    label(210)
    sprite('rwi601_00', 40)	# 35251-35290
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rwi601_01', 6)	# 35291-35296
    sprite('rwi601_02', 6)	# 35297-35302
    sprite('rwi601_03', 6)	# 35303-35308
    SFX_1('rwi600ryn')
    sprite('rwi601_04', 6)	# 35309-35314
    sprite('rwi601_05', 6)	# 35315-35320
    sprite('rwi601_06', 6)	# 35321-35326
    sprite('rwi601_07', 6)	# 35327-35332
    Unknown21011(300)
    Unknown2037(1)
    label(211)
    sprite('rwi000_00', 6)	# 35333-35338
    sprite('rwi000_01', 6)	# 35339-35344
    sprite('rwi000_02', 6)	# 35345-35350
    sprite('rwi000_03', 6)	# 35351-35356
    sprite('rwi000_04', 6)	# 35357-35362
    sprite('rwi000_05', 6)	# 35363-35368
    sprite('rwi000_06', 6)	# 35369-35374
    if (not SLOT_2):
        Unknown21007(24, 40)
    sprite('rwi000_07', 6)	# 35375-35380
    sprite('rwi000_08', 6)	# 35381-35386
    sprite('rwi000_09', 6)	# 35387-35392
    sprite('rwi000_10', 6)	# 35393-35398
    Unknown2038(-1)
    gotoLabel(211)
    ExitState()
    label(220)
    sprite('rwi601_00', 1)	# 35399-35399
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('rwi601_00', 60)	# 35400-35459
    SFX_1('rwi600pmi')
    sprite('rwi601_01', 6)	# 35460-35465
    sprite('rwi601_02', 6)	# 35466-35471
    sprite('rwi601_03', 6)	# 35472-35477
    sprite('rwi601_04', 6)	# 35478-35483
    sprite('rwi601_05', 6)	# 35484-35489
    sprite('rwi601_06', 6)	# 35490-35495
    sprite('rwi601_07', 6)	# 35496-35501
    label(221)
    sprite('rwi000_00', 6)	# 35502-35507
    sprite('rwi000_01', 6)	# 35508-35513
    sprite('rwi000_02', 6)	# 35514-35519
    sprite('rwi000_03', 6)	# 35520-35525
    sprite('rwi000_04', 6)	# 35526-35531
    sprite('rwi000_05', 6)	# 35532-35537
    sprite('rwi000_06', 6)	# 35538-35543
    sprite('rwi000_07', 6)	# 35544-35549
    sprite('rwi000_08', 6)	# 35550-35555
    sprite('rwi000_09', 6)	# 35556-35561
    sprite('rwi000_10', 6)	# 35562-35567
    if SLOT_97:
        _gotolabel(221)
    sprite('rwi000_00', 1)	# 35568-35568
    Unknown21007(24, 40)
    Unknown21011(200)
    label(222)
    sprite('rwi000_00', 6)	# 35569-35574
    sprite('rwi000_01', 6)	# 35575-35580
    sprite('rwi000_02', 6)	# 35581-35586
    sprite('rwi000_03', 6)	# 35587-35592
    sprite('rwi000_04', 6)	# 35593-35598
    sprite('rwi000_05', 6)	# 35599-35604
    sprite('rwi000_06', 6)	# 35605-35610
    sprite('rwi000_07', 6)	# 35611-35616
    sprite('rwi000_08', 6)	# 35617-35622
    sprite('rwi000_09', 6)	# 35623-35628
    sprite('rwi000_10', 6)	# 35629-35634
    gotoLabel(222)
    ExitState()
    label(230)
    sprite('rwi000_00', 1)	# 35635-35635
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('rwi000_00', 6)	# 35636-35641
    sprite('rwi000_01', 6)	# 35642-35647
    sprite('rwi000_02', 6)	# 35648-35653
    sprite('rwi000_03', 6)	# 35654-35659
    sprite('rwi000_04', 6)	# 35660-35665
    sprite('rwi000_05', 6)	# 35666-35671
    sprite('rwi000_06', 6)	# 35672-35677
    sprite('rwi000_07', 6)	# 35678-35683
    sprite('rwi000_08', 6)	# 35684-35689
    sprite('rwi000_09', 6)	# 35690-35695
    sprite('rwi000_10', 6)	# 35696-35701
    gotoLabel(231)
    label(232)
    sprite('rwi600_00', 6)	# 35702-35707
    sprite('rwi600_01', 6)	# 35708-35713
    sprite('rwi600_02', 6)	# 35714-35719
    sprite('rwi600_03', 6)	# 35720-35725
    sprite('rwi600_04', 6)	# 35726-35731
    SFX_1('rwi601bph')
    sprite('rwi600_05', 6)	# 35732-35737
    sprite('rwi600_06', 6)	# 35738-35743
    sprite('rwi600_07', 6)	# 35744-35749
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 35750-35755
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 35756-35761
    sprite('rwi600_10', 6)	# 35762-35767
    sprite('rwi600_11', 6)	# 35768-35773
    Unknown23018(1)
    label(233)
    sprite('rwi000_00', 6)	# 35774-35779
    sprite('rwi000_01', 6)	# 35780-35785
    sprite('rwi000_02', 6)	# 35786-35791
    sprite('rwi000_03', 6)	# 35792-35797
    sprite('rwi000_04', 6)	# 35798-35803
    sprite('rwi000_05', 6)	# 35804-35809
    sprite('rwi000_06', 6)	# 35810-35815
    sprite('rwi000_07', 6)	# 35816-35821
    sprite('rwi000_08', 6)	# 35822-35827
    sprite('rwi000_09', 6)	# 35828-35833
    sprite('rwi000_10', 6)	# 35834-35839
    gotoLabel(233)
    ExitState()
    label(991)
    sprite('rwi000_00', 1)	# 35840-35840
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('rwi000_00', 6)	# 35841-35846
    sprite('rwi000_01', 6)	# 35847-35852
    sprite('rwi000_02', 6)	# 35853-35858
    sprite('rwi000_03', 6)	# 35859-35864
    sprite('rwi000_04', 6)	# 35865-35870
    sprite('rwi000_05', 6)	# 35871-35876
    sprite('rwi000_06', 6)	# 35877-35882
    sprite('rwi000_07', 6)	# 35883-35888
    sprite('rwi000_08', 6)	# 35889-35894
    sprite('rwi000_09', 6)	# 35895-35900
    sprite('rwi000_10', 6)	# 35901-35906
    gotoLabel(992)
    label(993)
    sprite('rwi033_00', 3)	# 35907-35909

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
    sprite('rwi033_01', 3)	# 35910-35912
    sprite('rwi033_02', 3)	# 35913-35915
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 35916-35918
    ExitState()
    label(1000)
    sprite('rwi649_00', 6)	# 35919-35924
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 8003):
            clearUponHandler(43)
            sendToLabel(1001)
    sprite('rwi649_00', 6)	# 35925-35930
    sprite('rwi649_00', 6)	# 35931-35936
    sprite('rwi649_00', 6)	# 35937-35942
    sprite('rwi649_00', 32767)	# 35943-68709
    label(1001)
    sprite('rwi001_02', 6)	# 68710-68715
    SFX_1('rwi603')
    sprite('rwi001_01', 6)	# 68716-68721
    sprite('rwi001_01', 6)	# 68722-68727
    sprite('rwi001_00', 6)	# 68728-68733
    Unknown2037(2)
    label(1002)
    sprite('rwi000_00', 6)	# 68734-68739
    sprite('rwi000_01', 6)	# 68740-68745
    sprite('rwi000_02', 6)	# 68746-68751
    sprite('rwi000_03', 6)	# 68752-68757
    sprite('rwi000_04', 6)	# 68758-68763
    sprite('rwi000_05', 6)	# 68764-68769
    sprite('rwi000_06', 6)	# 68770-68775
    sprite('rwi000_07', 6)	# 68776-68781
    sprite('rwi000_08', 6)	# 68782-68787
    sprite('rwi000_09', 6)	# 68788-68793
    sprite('rwi000_10', 6)	# 68794-68799
    sprite('rwi000_00', 6)	# 68800-68805
    sprite('rwi000_01', 6)	# 68806-68811
    sprite('rwi000_02', 6)	# 68812-68817
    sprite('rwi000_03', 6)	# 68818-68823
    sprite('rwi000_04', 6)	# 68824-68829
    sprite('rwi000_05', 6)	# 68830-68835
    sprite('rwi000_06', 6)	# 68836-68841
    sprite('rwi000_07', 6)	# 68842-68847
    sprite('rwi000_08', 6)	# 68848-68853
    sprite('rwi000_09', 6)	# 68854-68859
    sprite('rwi000_10', 6)	# 68860-68865
    sprite('rwi000_00', 6)	# 68866-68871
    sprite('rwi000_01', 6)	# 68872-68877
    sprite('rwi000_02', 6)	# 68878-68883
    sprite('rwi000_03', 6)	# 68884-68889
    sprite('rwi000_04', 6)	# 68890-68895
    Unknown23029(24, 8006, 0)
    Unknown23029(22, 8006, 0)
    Unknown23029(23, 8006, 0)
    Unknown23029(24, 8008, 0)
    Unknown23029(22, 8008, 0)
    Unknown23029(23, 8008, 0)
    Unknown23029(24, 8007, 0)
    Unknown23029(22, 8007, 0)
    Unknown23029(23, 8007, 0)
    sprite('rwi600_00', 6)	# 68896-68901
    sprite('rwi600_01', 6)	# 68902-68907
    sprite('rwi600_02', 6)	# 68908-68913
    sprite('rwi600_03', 6)	# 68914-68919
    sprite('rwi600_04', 6)	# 68920-68925
    sprite('rwi600_05', 6)	# 68926-68931
    sprite('rwi600_06', 6)	# 68932-68937
    sprite('rwi600_07', 6)	# 68938-68943
    GFX_0('rwief600', -1)
    sprite('rwi600_08', 6)	# 68944-68949
    SFX_0('007_swing_knife_0')
    sprite('rwi600_09', 6)	# 68950-68955
    sprite('rwi600_10', 6)	# 68956-68961
    sprite('rwi600_11', 6)	# 68962-68967
    if SLOT_97:
        _gotolabel(1002)
    sprite('rwi000_00', 6)	# 68968-68973
    sprite('rwi000_01', 6)	# 68974-68979
    sprite('rwi000_02', 6)	# 68980-68985
    Unknown23029(24, 8004, 0)
    Unknown23029(22, 8004, 0)
    Unknown23029(23, 8004, 0)
    label(1003)
    sprite('rwi000_03', 6)	# 68986-68991
    SFX_1('rwi605')
    sprite('rwi000_04', 6)	# 68992-68997
    sprite('rwi000_05', 6)	# 68998-69003
    sprite('rwi000_06', 6)	# 69004-69009
    sprite('rwi000_07', 6)	# 69010-69015
    sprite('rwi000_08', 6)	# 69016-69021
    sprite('rwi000_09', 6)	# 69022-69027
    sprite('rwi000_10', 6)	# 69028-69033
    Unknown23018(1)
    label(1004)
    sprite('rwi000_00', 6)	# 69034-69039
    sprite('rwi000_01', 6)	# 69040-69045
    sprite('rwi000_02', 6)	# 69046-69051
    sprite('rwi000_03', 6)	# 69052-69057
    sprite('rwi000_04', 6)	# 69058-69063
    sprite('rwi000_05', 6)	# 69064-69069
    sprite('rwi000_06', 6)	# 69070-69075
    sprite('rwi000_07', 6)	# 69076-69081
    sprite('rwi000_08', 6)	# 69082-69087
    sprite('rwi000_09', 6)	# 69088-69093
    sprite('rwi000_10', 6)	# 69094-69099
    gotoLabel(1004)
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
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('bmk'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pna'):
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
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('ryn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('pmi'):
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
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(1)
    label(0)
    sprite('rwi610_00', 6)	# 4-9
    sprite('rwi610_01', 6)	# 10-15
    sprite('rwi610_02', 6)	# 16-21
    sprite('rwi610_03', 6)	# 22-27
    sprite('rwi610_04', 6)	# 28-33
    sprite('rwi610_05', 15)	# 34-48
    sprite('rwi610_06', 6)	# 49-54
    sprite('rwi610_07', 6)	# 55-60
    if SLOT_158:
        if SLOT_52:
            SFX_1('rwi524')
        elif SLOT_108:
            Unknown7006('rwi402_0', 100, 879327090, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rwi520', 100, 896104306, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('rwi610_08', 6)	# 61-66
    sprite('rwi610_09', 6)	# 67-72
    sprite('rwi610_10', 6)	# 73-78
    sprite('rwi610_11', 6)	# 79-84
    sprite('rwi610_12', 6)	# 85-90
    sprite('rwi610_13', 32767)	# 91-32857
    label(1)
    sprite('rwi611_00', 6)	# 32858-32863
    sprite('rwi611_01', 6)	# 32864-32869
    sprite('rwi611_02', 6)	# 32870-32875
    sprite('rwi611_03', 4)	# 32876-32879
    if SLOT_158:
        if SLOT_52:
            SFX_1('rwi525')
        elif SLOT_108:
            Unknown7006('rwi402_0', 100, 879327090, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('rwi522', 100, 896104306, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('rwi611_04', 6)	# 32880-32885
    SFX_0('007_swing_knife_1')
    sprite('rwi611_05', 32767)	# 32886-65652
    label(100)
    sprite('rwi000_00', 1)	# 65653-65653

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('rwi000_00', 6)	# 65654-65659
    sprite('rwi000_01', 6)	# 65660-65665
    sprite('rwi000_02', 6)	# 65666-65671
    sprite('rwi000_03', 6)	# 65672-65677
    sprite('rwi000_04', 6)	# 65678-65683
    sprite('rwi000_05', 6)	# 65684-65689
    sprite('rwi000_06', 6)	# 65690-65695
    sprite('rwi000_07', 6)	# 65696-65701
    sprite('rwi000_08', 6)	# 65702-65707
    sprite('rwi000_09', 6)	# 65708-65713
    sprite('rwi000_10', 6)	# 65714-65719
    gotoLabel(101)
    label(102)
    sprite('rwi610_00', 6)	# 65720-65725
    sprite('rwi610_01', 6)	# 65726-65731
    sprite('rwi610_02', 6)	# 65732-65737
    sprite('rwi610_03', 6)	# 65738-65743
    sprite('rwi610_04', 6)	# 65744-65749
    sprite('rwi610_05', 15)	# 65750-65764
    sprite('rwi610_06', 6)	# 65765-65770
    sprite('rwi610_07', 6)	# 65771-65776
    SFX_1('rwi701bha')
    sprite('rwi610_08', 6)	# 65777-65782
    sprite('rwi610_09', 6)	# 65783-65788
    sprite('rwi610_10', 6)	# 65789-65794
    sprite('rwi610_11', 6)	# 65795-65800
    sprite('rwi610_12', 6)	# 65801-65806
    Unknown23018(1)
    sprite('rwi610_13', 32767)	# 65807-98573
    label(110)
    sprite('rwi000_00', 1)	# 98574-98574

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('rwi000_00', 6)	# 98575-98580
    sprite('rwi000_01', 6)	# 98581-98586
    sprite('rwi000_02', 6)	# 98587-98592
    sprite('rwi000_03', 6)	# 98593-98598
    sprite('rwi000_04', 6)	# 98599-98604
    sprite('rwi000_05', 6)	# 98605-98610
    sprite('rwi000_06', 6)	# 98611-98616
    sprite('rwi000_07', 6)	# 98617-98622
    sprite('rwi000_08', 6)	# 98623-98628
    sprite('rwi000_09', 6)	# 98629-98634
    sprite('rwi000_10', 6)	# 98635-98640
    gotoLabel(111)
    label(112)
    sprite('rwi610_00', 6)	# 98641-98646
    sprite('rwi610_01', 6)	# 98647-98652
    sprite('rwi610_02', 6)	# 98653-98658
    sprite('rwi610_03', 6)	# 98659-98664
    sprite('rwi610_04', 6)	# 98665-98670
    sprite('rwi610_05', 15)	# 98671-98685
    sprite('rwi610_06', 6)	# 98686-98691
    sprite('rwi610_07', 6)	# 98692-98697
    SFX_1('rwi701bny')
    sprite('rwi610_08', 6)	# 98698-98703
    sprite('rwi610_09', 6)	# 98704-98709
    sprite('rwi610_10', 6)	# 98710-98715
    sprite('rwi610_11', 6)	# 98716-98721
    sprite('rwi610_12', 6)	# 98722-98727
    Unknown21011(130)
    sprite('rwi610_13', 32767)	# 98728-131494
    label(120)
    sprite('rwi000_00', 1)	# 131495-131495
    if (not SLOT_158):
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('rwi000_00', 6)	# 131496-131501
    sprite('rwi000_01', 6)	# 131502-131507
    sprite('rwi000_02', 6)	# 131508-131513
    sprite('rwi000_03', 6)	# 131514-131519
    sprite('rwi000_04', 6)	# 131520-131525
    sprite('rwi000_05', 6)	# 131526-131531
    sprite('rwi000_06', 6)	# 131532-131537
    sprite('rwi000_07', 6)	# 131538-131543
    sprite('rwi000_08', 6)	# 131544-131549
    sprite('rwi000_09', 6)	# 131550-131555
    sprite('rwi000_10', 6)	# 131556-131561
    gotoLabel(121)
    label(122)
    sprite('rwi610_00', 6)	# 131562-131567
    sprite('rwi610_01', 6)	# 131568-131573
    sprite('rwi610_02', 6)	# 131574-131579
    sprite('rwi610_03', 6)	# 131580-131585
    sprite('rwi610_04', 6)	# 131586-131591
    sprite('rwi610_05', 15)	# 131592-131606
    sprite('rwi610_06', 6)	# 131607-131612
    sprite('rwi610_07', 6)	# 131613-131618
    SFX_1('rwi701bmk')
    sprite('rwi610_08', 6)	# 131619-131624
    sprite('rwi610_09', 6)	# 131625-131630
    sprite('rwi610_10', 6)	# 131631-131636
    sprite('rwi610_11', 6)	# 131637-131642
    sprite('rwi610_12', 6)	# 131643-131648
    label(123)
    sprite('rwi610_13', 1)	# 131649-131649
    if SLOT_97:
        _gotolabel(123)
    sprite('rwi610_13', 30)	# 131650-131679
    sprite('rwi610_13', 32767)	# 131680-164446
    Unknown21007(24, 40)
    Unknown21011(150)
    label(130)
    sprite('rwi000_00', 1)	# 164447-164447

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('rwi000_00', 6)	# 164448-164453
    sprite('rwi000_01', 6)	# 164454-164459
    sprite('rwi000_02', 6)	# 164460-164465
    sprite('rwi000_03', 6)	# 164466-164471
    sprite('rwi000_04', 6)	# 164472-164477
    sprite('rwi000_05', 6)	# 164478-164483
    sprite('rwi000_06', 6)	# 164484-164489
    sprite('rwi000_07', 6)	# 164490-164495
    sprite('rwi000_08', 6)	# 164496-164501
    sprite('rwi000_09', 6)	# 164502-164507
    sprite('rwi000_10', 6)	# 164508-164513
    gotoLabel(131)
    label(132)
    sprite('rwi300_00', 6)	# 164514-164519
    if (SLOT_38 == 1):
        if (SLOT_152 == 1):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                Unknown2005()
    if (SLOT_38 == 0):
        if (SLOT_152 == 0):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                Unknown2005()
    sprite('rwi300_01', 6)	# 164520-164525
    sprite('rwi300_02', 6)	# 164526-164531
    sprite('rwi300_03', 6)	# 164532-164537
    sprite('rwi300_04', 6)	# 164538-164543
    SFX_1('rwi701bpt')
    sprite('rwi300_05', 6)	# 164544-164549
    label(133)
    sprite('rwi300_06', 6)	# 164550-164555
    sprite('rwi300_07', 6)	# 164556-164561
    sprite('rwi300_08', 6)	# 164562-164567
    if SLOT_97:
        _gotolabel(133)
    sprite('rwi300_09', 6)	# 164568-164573
    sprite('rwi300_10', 6)	# 164574-164579
    sprite('rwi000_00', 6)	# 164580-164585
    sprite('rwi610_00', 6)	# 164586-164591
    sprite('rwi610_01', 6)	# 164592-164597
    sprite('rwi610_02', 6)	# 164598-164603
    sprite('rwi610_03', 6)	# 164604-164609
    sprite('rwi610_04', 6)	# 164610-164615
    sprite('rwi610_05', 15)	# 164616-164630
    Unknown23018(1)
    sprite('rwi610_06', 6)	# 164631-164636
    sprite('rwi610_07', 6)	# 164637-164642
    sprite('rwi610_08', 6)	# 164643-164648
    sprite('rwi610_09', 6)	# 164649-164654
    sprite('rwi610_10', 6)	# 164655-164660
    sprite('rwi610_11', 6)	# 164661-164666
    sprite('rwi610_12', 6)	# 164667-164672
    sprite('rwi610_13', 32767)	# 164673-197439
    label(140)
    sprite('rwi610_00', 6)	# 197440-197445

    def upon_40():
        clearUponHandler(40)
        SFX_1('rwi702pbc')
        Unknown23018(1)
    sprite('rwi610_01', 6)	# 197446-197451
    sprite('rwi610_02', 6)	# 197452-197457
    sprite('rwi610_03', 6)	# 197458-197463
    sprite('rwi610_04', 6)	# 197464-197469
    sprite('rwi610_05', 15)	# 197470-197484
    sprite('rwi610_06', 6)	# 197485-197490
    sprite('rwi610_07', 6)	# 197491-197496
    SFX_1('rwi700pbc')
    sprite('rwi610_08', 6)	# 197497-197502
    sprite('rwi610_09', 6)	# 197503-197508
    sprite('rwi610_10', 6)	# 197509-197514
    sprite('rwi610_11', 6)	# 197515-197520
    sprite('rwi610_12', 6)	# 197521-197526
    label(141)
    sprite('rwi610_13', 1)	# 197527-197527
    if SLOT_97:
        _gotolabel(141)
    sprite('rwi610_13', 30)	# 197528-197557
    sprite('rwi610_13', 32767)	# 197558-230324
    Unknown21007(24, 40)
    label(150)
    sprite('rwi000_00', 1)	# 230325-230325

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('rwi000_00', 6)	# 230326-230331
    sprite('rwi000_01', 6)	# 230332-230337
    sprite('rwi000_02', 6)	# 230338-230343
    sprite('rwi000_03', 6)	# 230344-230349
    sprite('rwi000_04', 6)	# 230350-230355
    sprite('rwi000_05', 6)	# 230356-230361
    sprite('rwi000_06', 6)	# 230362-230367
    sprite('rwi000_07', 6)	# 230368-230373
    sprite('rwi000_08', 6)	# 230374-230379
    sprite('rwi000_09', 6)	# 230380-230385
    sprite('rwi000_10', 6)	# 230386-230391
    gotoLabel(151)
    label(152)
    sprite('rwi610_00', 6)	# 230392-230397
    sprite('rwi610_01', 6)	# 230398-230403
    sprite('rwi610_02', 6)	# 230404-230409
    sprite('rwi610_03', 6)	# 230410-230415
    sprite('rwi610_04', 6)	# 230416-230421
    sprite('rwi610_05', 15)	# 230422-230436
    sprite('rwi610_06', 6)	# 230437-230442
    sprite('rwi610_07', 6)	# 230443-230448
    SFX_1('rwi701pyu')
    sprite('rwi610_08', 6)	# 230449-230454
    sprite('rwi610_09', 6)	# 230455-230460
    sprite('rwi610_10', 6)	# 230461-230466
    sprite('rwi610_11', 6)	# 230467-230472
    sprite('rwi610_12', 6)	# 230473-230478
    Unknown21011(120)
    sprite('rwi610_13', 32767)	# 230479-263245
    label(160)
    sprite('rwi610_00', 6)	# 263246-263251
    sprite('rwi610_01', 6)	# 263252-263257
    sprite('rwi610_02', 6)	# 263258-263263
    sprite('rwi610_03', 6)	# 263264-263269
    sprite('rwi610_04', 6)	# 263270-263275
    sprite('rwi610_05', 15)	# 263276-263290
    sprite('rwi610_06', 6)	# 263291-263296
    sprite('rwi610_07', 6)	# 263297-263302
    SFX_1('rwi700pna')
    sprite('rwi610_08', 6)	# 263303-263308
    sprite('rwi610_09', 6)	# 263309-263314
    sprite('rwi610_10', 6)	# 263315-263320
    sprite('rwi610_11', 6)	# 263321-263326
    sprite('rwi610_12', 6)	# 263327-263332
    label(161)
    sprite('rwi610_13', 1)	# 263333-263333
    if SLOT_97:
        _gotolabel(161)
    sprite('rwi610_13', 32767)	# 263334-296100
    Unknown21007(24, 40)
    Unknown21011(240)
    label(170)
    sprite('rwi000_00', 1)	# 296101-296101

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('rwi000_00', 6)	# 296102-296107
    sprite('rwi000_01', 6)	# 296108-296113
    sprite('rwi000_02', 6)	# 296114-296119
    sprite('rwi000_03', 6)	# 296120-296125
    sprite('rwi000_04', 6)	# 296126-296131
    sprite('rwi000_05', 6)	# 296132-296137
    sprite('rwi000_06', 6)	# 296138-296143
    sprite('rwi000_07', 6)	# 296144-296149
    sprite('rwi000_08', 6)	# 296150-296155
    sprite('rwi000_09', 6)	# 296156-296161
    sprite('rwi000_10', 6)	# 296162-296167
    gotoLabel(171)
    label(172)
    sprite('rwi611_00', 6)	# 296168-296173
    sprite('rwi611_01', 6)	# 296174-296179
    sprite('rwi611_02', 6)	# 296180-296185
    sprite('rwi611_03', 4)	# 296186-296189
    SFX_1('rwi701rrb')
    sprite('rwi611_04', 6)	# 296190-296195
    SFX_0('007_swing_knife_1')
    sprite('rwi611_05', 32767)	# 296196-328962
    Unknown23018(1)
    label(180)
    sprite('rwi610_00', 6)	# 328963-328968
    sprite('rwi610_01', 6)	# 328969-328974
    sprite('rwi610_02', 6)	# 328975-328980
    sprite('rwi610_03', 6)	# 328981-328986
    sprite('rwi610_04', 6)	# 328987-328992
    sprite('rwi610_05', 15)	# 328993-329007
    sprite('rwi610_06', 6)	# 329008-329013
    sprite('rwi610_07', 6)	# 329014-329019
    SFX_1('rwi700rbl')
    sprite('rwi610_08', 6)	# 329020-329025
    sprite('rwi610_09', 6)	# 329026-329031
    sprite('rwi610_10', 6)	# 329032-329037
    sprite('rwi610_11', 6)	# 329038-329043
    sprite('rwi610_12', 6)	# 329044-329049
    label(181)
    sprite('rwi610_13', 1)	# 329050-329050
    if SLOT_97:
        _gotolabel(181)
    sprite('rwi610_13', 30)	# 329051-329080
    sprite('rwi610_13', 32767)	# 329081-361847
    Unknown21007(24, 40)
    Unknown21011(120)
    label(190)
    sprite('rwi610_00', 6)	# 361848-361853

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
        SFX_1('rwi702uor')
    sprite('rwi610_01', 6)	# 361854-361859
    sprite('rwi610_02', 6)	# 361860-361865
    sprite('rwi610_03', 6)	# 361866-361871
    sprite('rwi610_04', 6)	# 361872-361877
    sprite('rwi610_05', 15)	# 361878-361892
    sprite('rwi610_06', 6)	# 361893-361898
    sprite('rwi610_07', 6)	# 361899-361904
    sprite('rwi610_08', 6)	# 361905-361910
    sprite('rwi610_09', 6)	# 361911-361916
    SFX_1('rwi700uor')
    sprite('rwi610_10', 6)	# 361917-361922
    sprite('rwi610_11', 6)	# 361923-361928
    sprite('rwi610_12', 6)	# 361929-361934
    label(191)
    sprite('rwi610_13', 1)	# 361935-361935
    if SLOT_97:
        _gotolabel(191)
    sprite('rwi610_13', 32767)	# 361936-394702
    Unknown21007(24, 40)
    label(192)
    sprite('rwi610_13', 1)	# 394703-394703
    if SLOT_97:
        _gotolabel(192)
    sprite('rwi610_13', 20)	# 394704-394723
    sprite('rwi610_13', 32767)	# 394724-427490
    Unknown21007(24, 39)
    Unknown21011(180)
    label(200)
    sprite('rwi000_00', 1)	# 427491-427491

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('rwi000_00', 6)	# 427492-427497
    sprite('rwi000_01', 6)	# 427498-427503
    sprite('rwi000_02', 6)	# 427504-427509
    sprite('rwi000_03', 6)	# 427510-427515
    sprite('rwi000_04', 6)	# 427516-427521
    sprite('rwi000_05', 6)	# 427522-427527
    sprite('rwi000_06', 6)	# 427528-427533
    sprite('rwi000_07', 6)	# 427534-427539
    sprite('rwi000_08', 6)	# 427540-427545
    sprite('rwi000_09', 6)	# 427546-427551
    sprite('rwi000_10', 6)	# 427552-427557
    gotoLabel(201)
    label(202)
    sprite('rwi610_00', 6)	# 427558-427563
    sprite('rwi610_01', 6)	# 427564-427569
    sprite('rwi610_02', 6)	# 427570-427575
    sprite('rwi610_03', 6)	# 427576-427581
    sprite('rwi610_04', 6)	# 427582-427587
    sprite('rwi610_05', 15)	# 427588-427602
    sprite('rwi610_06', 6)	# 427603-427608
    sprite('rwi610_07', 6)	# 427609-427614
    SFX_1('rwi701uva')
    sprite('rwi610_08', 6)	# 427615-427620
    sprite('rwi610_09', 6)	# 427621-427626
    sprite('rwi610_10', 6)	# 427627-427632
    sprite('rwi610_11', 6)	# 427633-427638
    sprite('rwi610_12', 6)	# 427639-427644
    Unknown23018(1)
    sprite('rwi610_13', 32767)	# 427645-460411
    label(210)
    sprite('rwi000_00', 1)	# 460412-460412

    def upon_40():
        clearUponHandler(40)
        sendToLabel(212)
    label(211)
    sprite('rwi000_00', 6)	# 460413-460418
    sprite('rwi000_01', 6)	# 460419-460424
    sprite('rwi000_02', 6)	# 460425-460430
    sprite('rwi000_03', 6)	# 460431-460436
    sprite('rwi000_04', 6)	# 460437-460442
    sprite('rwi000_05', 6)	# 460443-460448
    sprite('rwi000_06', 6)	# 460449-460454
    sprite('rwi000_07', 6)	# 460455-460460
    sprite('rwi000_08', 6)	# 460461-460466
    sprite('rwi000_09', 6)	# 460467-460472
    sprite('rwi000_10', 6)	# 460473-460478
    gotoLabel(211)
    label(212)
    sprite('rwi610_00', 6)	# 460479-460484
    sprite('rwi610_01', 6)	# 460485-460490
    sprite('rwi610_02', 6)	# 460491-460496
    sprite('rwi610_03', 6)	# 460497-460502
    sprite('rwi610_04', 6)	# 460503-460508
    sprite('rwi610_05', 15)	# 460509-460523
    sprite('rwi610_06', 6)	# 460524-460529
    sprite('rwi610_07', 6)	# 460530-460535
    SFX_1('rwi701ryn')
    sprite('rwi610_08', 6)	# 460536-460541
    sprite('rwi610_09', 6)	# 460542-460547
    sprite('rwi610_10', 6)	# 460548-460553
    sprite('rwi610_11', 6)	# 460554-460559
    sprite('rwi610_12', 6)	# 460560-460565
    Unknown23018(1)
    sprite('rwi610_13', 32767)	# 460566-493332
    label(220)
    sprite('rwi000_00', 1)	# 493333-493333

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('rwi000_00', 6)	# 493334-493339
    sprite('rwi000_01', 6)	# 493340-493345
    sprite('rwi000_02', 6)	# 493346-493351
    sprite('rwi000_03', 6)	# 493352-493357
    sprite('rwi000_04', 6)	# 493358-493363
    sprite('rwi000_05', 6)	# 493364-493369
    sprite('rwi000_06', 6)	# 493370-493375
    sprite('rwi000_07', 6)	# 493376-493381
    sprite('rwi000_08', 6)	# 493382-493387
    sprite('rwi000_09', 6)	# 493388-493393
    sprite('rwi000_10', 6)	# 493394-493399
    gotoLabel(221)
    label(222)
    sprite('rwi610_00', 6)	# 493400-493405
    sprite('rwi610_01', 6)	# 493406-493411
    sprite('rwi610_02', 6)	# 493412-493417
    sprite('rwi610_03', 6)	# 493418-493423
    sprite('rwi610_04', 6)	# 493424-493429
    sprite('rwi610_05', 15)	# 493430-493444
    sprite('rwi610_06', 6)	# 493445-493450
    sprite('rwi610_07', 6)	# 493451-493456
    SFX_1('rwi701pmi')
    sprite('rwi610_08', 6)	# 493457-493462
    sprite('rwi610_09', 6)	# 493463-493468
    sprite('rwi610_10', 6)	# 493469-493474
    sprite('rwi610_11', 6)	# 493475-493480
    sprite('rwi610_12', 6)	# 493481-493486
    Unknown23018(1)
    sprite('rwi610_13', 32767)	# 493487-526253
    label(230)
    sprite('rwi000_00', 1)	# 526254-526254

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('rwi000_00', 6)	# 526255-526260
    sprite('rwi000_01', 6)	# 526261-526266
    sprite('rwi000_02', 6)	# 526267-526272
    sprite('rwi000_03', 6)	# 526273-526278
    sprite('rwi000_04', 6)	# 526279-526284
    sprite('rwi000_05', 6)	# 526285-526290
    sprite('rwi000_06', 6)	# 526291-526296
    sprite('rwi000_07', 6)	# 526297-526302
    sprite('rwi000_08', 6)	# 526303-526308
    sprite('rwi000_09', 6)	# 526309-526314
    sprite('rwi000_10', 6)	# 526315-526320
    gotoLabel(231)
    label(232)
    sprite('rwi610_00', 6)	# 526321-526326
    sprite('rwi610_01', 6)	# 526327-526332
    sprite('rwi610_02', 6)	# 526333-526338
    sprite('rwi610_03', 6)	# 526339-526344
    sprite('rwi610_04', 6)	# 526345-526350
    sprite('rwi610_05', 15)	# 526351-526365
    sprite('rwi610_06', 6)	# 526366-526371
    sprite('rwi610_07', 6)	# 526372-526377
    SFX_1('rwi701bph')
    sprite('rwi610_08', 6)	# 526378-526383
    sprite('rwi610_09', 6)	# 526384-526389
    sprite('rwi610_10', 6)	# 526390-526395
    sprite('rwi610_11', 6)	# 526396-526401
    sprite('rwi610_12', 6)	# 526402-526407
    Unknown23018(1)
    sprite('rwi610_13', 32767)	# 526408-559174

@State
def CmnActLose():
    sprite('rwi620_00', 6)	# 1-6
    if SLOT_158:
        Unknown7006('rwi403_0', 100, 879327090, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('rwi620_01', 6)	# 7-12
    sprite('rwi620_02', 6)	# 13-18
    sprite('rwi620_03', 6)	# 19-24
    sprite('rwi620_04', 6)	# 25-30
    sprite('rwi620_05', 32767	# 31-32797
