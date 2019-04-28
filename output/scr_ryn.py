@Subroutine
def PreInit():
    Unknown12019('72796e00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(18000)
    DashFInitialVelocity(20000)
    DashFAccel(360)
    Unknown13039(1)
    Unknown2049(1)
    Unknown15018(500)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown15013(5000)
    Unknown14015(-50000, 250000, -200000, 250000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-50000, 350000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-50000, 350000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(-50000, 350000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 300000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Unknown15013(2000)
    Unknown14015(0, 450000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15021(2000)
    Unknown14015(0, 300000, -200000, 300000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown15013(0)
    Unknown14015(50000, 300000, 200000, 400000, 2000, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 400000, -100000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(500)
    Unknown14015(0, 400000, -100000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(3000)
    Unknown14015(0, 400000, -150000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(0, 400000, -250000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15013(3000)
    Unknown14015(0, 400000, -250000, 50000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5BB', 0x22)
    Unknown14005(1)
    Unknown14013('NmlAtkAIR5AA')
    Unknown14027('NmlAtkAIR5AA')
    Unknown14015(0, 400000, -250000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown14015(-150000, 250000, -450000, 150000, 1000, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('LandShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(250000, 550000, -200000, 200000, 250, 0)
    Move_EndRegister()
    Move_Register('LandShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(550000, 850000, -200000, 200000, 150, 0)
    Move_EndRegister()
    Move_Register('LandShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(400000, 700000, -200000, 200000, 150, 0)
    Move_EndRegister()
    Move_Register('AssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(50000, 450000, -200000, 150000, 500, 0)
    Move_EndRegister()
    Move_Register('AddAssaultA', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(2000)
    Unknown14015(-50000, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('AddAssaultB', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_B)
    Unknown15012(2000)
    Unknown14015(-50000, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('AddAssaultC', INPUT_SPECIALMOVE)
    Unknown14005(1)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15012(0)
    Unknown14015(-50000, 350000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('AssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(500)
    Unknown15012(2000)
    Unknown14015(50000, 300000, -200000, 350000, 500, 0)
    Move_EndRegister()
    Move_Register('AssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15010()
    Unknown14015(-50000, 250000, 50000, 350000, 1500, 0)
    Move_EndRegister()
    Move_Register('AirShotA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(2000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(250000, 550000, -500000, -100000, 500, 0)
    Move_EndRegister()
    Move_Register('AirShotB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(2000)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(550000, 850000, -500000, -200000, 250, 0)
    Move_EndRegister()
    Move_Register('AirShotC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15012(1)
    Unknown15006(1)
    Unknown15014(1)
    Unknown15021(1)
    Unknown15011(10000)
    Unknown14015(400000, 700000, -500000, -200000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(6000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(50000, 300000, -150000, 300000, 250, 0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttackAir', 0x65)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(-50000, 250000, -100000, 300000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(10000)
    Unknown15014(1)
    Unknown15006(1)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(650000, 850000, -200000, 250000, 50, 0)
    Move_EndRegister()
    Move_Register('UltimateAssaultSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(10000)
    Unknown15014(1)
    Unknown15006(1)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(650000, 850000, -200000, 250000, 50, 0)
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
    Unknown14015(0, 400000, -200000, 150000, 150, 0)
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
    Unknown14015(0, 400000, -200000, 150000, 150, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
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
    Move_Register('DangerMode', 0x68)
    Move_AirGround_(0x2000)
    Unknown14030(0)
    Unknown14006(0)
    Move_AirGround_(0x300a)
    Unknown14024('Func_DangerMode')
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5BB', 'FJump', 10000000)
    Unknown15024('NmlAtk5BB', 'AssaultC', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('NmlAtk2C', 'AssaultA', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'CmnActInvincibleAttackAir', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5BB', 10000000)
    Unknown15024('NmlAtkAIR5BB', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5BB', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5BB', 'CmnActInvincibleAttackAir', 10000000)
    Unknown15024('AssaultA', 'AddAssaultA', 10000000)
    Unknown15024('AssaultA', 'AddAssaultB', 10000000)
    Unknown15024('AssaultA', 'AddAssaultC', 10000000)
    Unknown12018(0, 'ryn062_01')
    Unknown12018(1, 'ryn062_03')
    Unknown12018(2, 'ryn062_04')
    Unknown12018(3, 'ryn062_05')
    Unknown12018(4, 'ryn062_06')
    Unknown12018(5, 'ryn062_07')
    Unknown12018(6, 'ryn062_09')
    Unknown12018(7, 'ryn040_02')
    Unknown12018(8, 'ryn040_02')
    Unknown12018(9, 'ryn045_02')
    Unknown12018(10, 'ryn062_00')
    Unknown12018(11, 'ryn062_01')
    Unknown12018(12, 'ryn062_03')
    Unknown12018(13, 'ryn062_05')
    Unknown12018(14, 'ryn062_09')
    Unknown12018(15, 'ryn073_01ex01')
    Unknown12018(16, 'ryn050_00')
    Unknown12018(17, 'ryn052_00')
    Unknown12018(18, 'ryn054_00')
    Unknown12018(19, 'ryn000_00')
    Unknown12018(20, 'ryn000_00')
    Unknown12018(25, 'ryn063_00')
    Unknown12018(26, 'ryn063_01')
    Unknown12018(27, 'ryn063_02')
    Unknown12018(28, 'ryn063_04')
    Unknown12018(29, 'ryn063_09')
    Unknown12018(24, 'ryn073_01')
    Unknown7010(0, 'ryn000')
    Unknown7010(1, 'ryn001')
    Unknown7010(2, 'ryn002')
    Unknown7010(3, 'ryn003')
    Unknown7010(4, 'ryn004')
    Unknown7010(5, 'ryn005')
    Unknown7010(6, 'ryn006')
    Unknown7010(7, 'ryn007')
    Unknown7010(8, 'ryn008')
    Unknown7010(9, 'ryn009')
    Unknown7010(10, 'ryn010')
    Unknown7010(15, 'ryn015')
    Unknown7010(16, 'ryn016')
    Unknown7010(17, 'ryn017')
    Unknown7010(18, 'ryn018')
    Unknown7010(19, 'ryn019')
    Unknown7010(20, 'ryn020')
    Unknown7010(21, 'ryn021')
    Unknown7010(22, 'ryn022')
    Unknown7010(23, 'ryn023')
    Unknown7010(24, 'ryn024')
    Unknown7010(25, 'ryn025')
    Unknown7010(28, 'ryn028')
    Unknown7010(29, 'ryn029')
    Unknown7010(30, 'ryn030')
    Unknown7010(31, 'ryn031')
    Unknown7010(32, 'ryn032')
    Unknown7010(33, 'ryn033')
    Unknown7010(34, 'ryn034')
    Unknown7010(35, 'ryn035')
    Unknown7010(36, 'ryn036')
    Unknown7010(37, 'ryn037')
    Unknown7010(39, 'ryn039')
    Unknown7010(42, 'ryn042')
    Unknown7010(43, 'ryn043')
    Unknown7010(44, 'ryn044')
    Unknown7010(45, 'ryn045')
    Unknown7010(46, 'ryn046')
    Unknown7010(47, 'ryn047')
    Unknown7010(48, 'ryn048')
    Unknown7010(49, 'ryn049')
    Unknown7010(50, 'ryn050')
    Unknown7010(52, 'ryn052')
    Unknown7010(53, 'ryn053')
    Unknown7010(54, 'ryn100_0')
    Unknown7010(55, 'ryn100_1')
    Unknown7010(56, 'ryn100_2')
    Unknown7010(63, 'ryn101_0')
    Unknown7010(64, 'ryn101_1')
    Unknown7010(65, 'ryn101_2')
    Unknown7010(57, 'ryn102_0')
    Unknown7010(58, 'ryn102_1')
    Unknown7010(59, 'ryn102_2')
    Unknown7010(66, 'ryn103_0')
    Unknown7010(67, 'ryn103_1')
    Unknown7010(68, 'ryn103_2')
    Unknown7010(60, 'ryn104_0')
    Unknown7010(61, 'ryn104_1')
    Unknown7010(62, 'ryn104_2')
    Unknown7010(69, 'ryn105_0')
    Unknown7010(70, 'ryn105_1')
    Unknown7010(71, 'ryn105_2')
    Unknown7010(72, 'ryn150')
    Unknown7010(73, 'ryn151')
    Unknown7010(74, 'ryn152')
    Unknown7010(85, 'ryn153')
    Unknown7010(88, 'ryn156')
    Unknown7010(94, 'ryn401_0')
    Unknown7010(95, 'ryn401_1')
    Unknown7010(96, 'ryn162_0')
    Unknown7010(97, 'ryn162_1')
    Unknown7010(98, 'ryn164_0')
    Unknown7010(99, 'ryn164_1')
    Unknown7010(100, 'ryn165_0')
    Unknown7010(101, 'ryn165_1')
    Unknown7010(102, 'ryn167_0')
    Unknown7010(103, 'ryn167_1')
    Unknown7010(92, 'ryn163_0')
    Unknown7010(93, 'ryn163_1')
    Unknown7010(90, 'ryn168_0')
    Unknown7010(91, 'ryn168_1')
    Unknown7010(105, 'ryn166_0')
    Unknown7010(106, 'ryn166_1')
    Unknown7010(107, 'ryn169_0')
    Unknown7010(108, 'ryn169_1')
    Unknown7010(110, 'ryn170_0')
    Unknown7010(111, 'ryn170_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3541000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745350000000000000000000000000000000')
    Unknown12059('04000000556c74696d617465527573680000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465527573685350000000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def Func_DangerMode():
    SLOT_47 = 0
    if (not SLOT_5):
        if (SLOT_124 < 3000):
            SLOT_47 = 1
    if SLOT_47:
        Unknown58('TRI_RYNPowerUp', 2, 67)
        if op(15, 2, 67, 0, 0):
            SLOT_47 = 0

@Subroutine
def OnPreDraw():
    Unknown23030('52594e5f457965537769746368000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

@Subroutine
def OnDamage():
    SLOT_4 = 0

@Subroutine
def CheckSembalnceActivate():
    Unknown58('TRI_RYNPowerUp', 2, 67)
    if (SLOT_67 == 1):
        SLOT_5 = 1
        SLOT_6 = 1
    Unknown58('TRI_RYNPowerUp', 2, 67)
    if (SLOT_67 == 2):
        SLOT_5 = 0
        SLOT_6 = 0
    if Unknown46(4):
        Unknown13(4)
    SLOT_7 = 0
    SLOT_66 = 0
    if SLOT_5:
        SLOT_7 = 1
        SLOT_66 = 1
        if Unknown23148('CmnActTagBattleWait'):
            SLOT_7 = 0
        if SLOT_30:
            SLOT_7 = 0
        if (not SLOT_21):
            SLOT_7 = 0
            SLOT_66 = 0
        if SLOT_7:
            GFX_0('AuraFireMaster', -1)
            Unknown38(4, 1)

@Subroutine
def OnActionBegin():
    callSubroutine('CheckSembalnceActivate')

@State
def CmnActStand():
    if SLOT_4:
        _gotolabel(1)
    label(0)
    sprite('ryn000_00', 6)	# 1-6
    sprite('ryn000_01', 6)	# 7-12
    sprite('ryn000_02', 6)	# 13-18
    sprite('ryn000_03', 6)	# 19-24
    sprite('ryn000_04', 6)	# 25-30
    sprite('ryn000_05', 6)	# 31-36
    sprite('ryn000_06', 6)	# 37-42
    sprite('ryn000_07', 6)	# 43-48
    sprite('ryn000_08', 6)	# 49-54
    sprite('ryn000_09', 6)	# 55-60
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 100)
    if SLOT_0:
        _gotolabel(0)
    label(1)
    sprite('ryn001_00', 4)	# 61-64
    SLOT_4 = 0
    sprite('ryn001_01', 4)	# 65-68
    sprite('ryn001_02', 4)	# 69-72
    sprite('ryn001_03', 4)	# 73-76
    SFX_3('rynse_00')
    sprite('ryn001_04', 4)	# 77-80
    sprite('ryn001_05', 8)	# 81-88
    sprite('ryn001_06', 6)	# 89-94
    sprite('ryn001_07', 6)	# 95-100
    GFX_1('rynef_case', 0)
    SFX_3('rynse_01')
    sprite('ryn001_08', 6)	# 101-106
    sprite('ryn001_09', 6)	# 107-112
    sprite('ryn001_10', 8)	# 113-120
    sprite('ryn001_11', 4)	# 121-124
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ryn003_00', 3)	# 1-3
    sprite('ryn003_01', 3)	# 4-6
    sprite('ryn003_00ex01', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('ryn010_00', 4)	# 1-4
    sprite('ryn010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ryn010_02', 5)	# 1-5
    sprite('ryn010_03', 5)	# 6-10
    sprite('ryn010_04', 5)	# 11-15
    sprite('ryn010_05', 5)	# 16-20
    sprite('ryn010_06', 5)	# 21-25
    sprite('ryn010_07', 5)	# 26-30
    sprite('ryn010_06', 5)	# 31-35
    sprite('ryn010_05', 5)	# 36-40
    sprite('ryn010_04', 5)	# 41-45
    sprite('ryn010_03', 5)	# 46-50
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ryn013_00', 3)	# 1-3
    sprite('ryn013_01', 3)	# 4-6
    sprite('ryn013_00ex01', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('ryn010_01', 4)	# 1-4
    sprite('ryn010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ryn010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    Unknown7006('ryn002', 25, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(0)
    sprite('ryn020_00', 3)	# 1-3
    sprite('ryn020_01', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ryn020_02', 3)	# 1-3
    sprite('ryn020_03', 3)	# 4-6
    sprite('ryn020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ryn020_05', 3)	# 1-3
    sprite('ryn020_06', 3)	# 4-6
    label(0)
    sprite('ryn020_07', 3)	# 7-9
    sprite('ryn020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ryn010_01', 2)	# 1-2
    sprite('ryn010_00', 2)	# 3-4

@State
def CmnActLandingStiffLoop():
    sprite('ryn010_00', 2)	# 1-2
    sprite('ryn010_01', 32767)	# 3-32769

@State
def CmnActLandingStiffEnd():
    sprite('ryn010_00', 3)	# 1-3
    sprite('ryn010_00', 3)	# 4-6

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
    sprite('ryn031_00', 5)	# 1-5
    sprite('ryn031_01', 5)	# 6-10
    label(0)
    sprite('ryn031_02', 5)	# 11-15
    sprite('ryn031_03', 5)	# 16-20
    sprite('ryn031_04', 5)	# 21-25
    sprite('ryn031_05', 5)	# 26-30
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ryn031_06', 5)	# 31-35
    sprite('ryn031_07', 5)	# 36-40
    sprite('ryn031_08', 5)	# 41-45
    sprite('ryn031_09', 5)	# 46-50
    SFX_FOOTSTEP_(100, 1, 1)
    loopRest()
    sendToLabel(0)

@State
def CmnActFDash():
    sprite('ryn032_00', 3)	# 1-3
    sprite('ryn032_01', 3)	# 4-6
    label(0)
    sprite('ryn032_02', 4)	# 7-10
    sprite('ryn032_03', 4)	# 11-14
    sprite('ryn032_04', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('ryn032_05', 4)	# 19-22
    sprite('ryn032_06', 4)	# 23-26
    sprite('ryn032_07', 4)	# 27-30
    sprite('ryn032_08', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('ryn032_09', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ryn032_10', 3)	# 1-3
    sprite('ryn032_11', 3)	# 4-6
    sprite('ryn032_12', 3)	# 7-9
    sprite('ryn032_13', 3)	# 10-12
    sprite('ryn032_14', 3)	# 13-15

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
    sprite('ryn033_00', 3)	# 1-3
    sprite('ryn033_01', 2)	# 4-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    SFX_4('ryn005')
    sprite('ryn033_02', 2)	# 6-7
    loopRest()
    label(0)
    sprite('ryn033_01', 2)	# 8-9
    sprite('ryn033_02', 2)	# 10-11
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ryn033_03', 3)	# 12-14
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ryn033_04', 3)	# 15-17

@State
def CmnActBDashLanding():
    sprite('ny033_05', 4)	# 1-4
    sprite('ny033_06', 4)	# 5-8

@State
def CmnActAirFDash():
    sprite('ryn035_00', 2)	# 1-2
    label(0)
    sprite('ryn035_01', 3)	# 3-5
    sprite('ryn035_02', 3)	# 6-8
    sprite('ryn035_03', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ryn033_00', 3)	# 1-3
    label(0)
    sprite('ryn033_01', 3)	# 4-6
    sprite('ryn033_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ryn050_00', 1)	# 1-1
    sprite('ryn050_01', 1)	# 2-2
    sprite('ryn050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ryn050_01', 1)	# 1-1
    sprite('ryn050_02', 1)	# 2-2
    sprite('ryn050_01', 2)	# 3-4
    sprite('ryn050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ryn050_02', 1)	# 1-1
    sprite('ryn050_02', 1)	# 2-2
    sprite('ryn050_02', 2)	# 3-4
    sprite('ryn050_01', 2)	# 5-6
    sprite('ryn050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ryn050_02', 1)	# 1-1
    sprite('ryn050_03', 1)	# 2-2
    sprite('ryn050_02', 2)	# 3-4
    sprite('ryn050_02', 2)	# 5-6
    sprite('ryn050_01', 2)	# 7-8
    sprite('ryn050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ryn050_03', 1)	# 1-1
    sprite('ryn050_03', 1)	# 2-2
    sprite('ryn050_03', 2)	# 3-4
    sprite('ryn050_02', 2)	# 5-6
    sprite('ryn050_02', 2)	# 7-8
    sprite('ryn050_01', 2)	# 9-10
    sprite('ryn050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ryn052_00', 1)	# 1-1
    sprite('ryn052_01', 1)	# 2-2
    sprite('ryn052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ryn052_01', 1)	# 1-1
    sprite('ryn052_02', 1)	# 2-2
    sprite('ryn052_01', 2)	# 3-4
    sprite('ryn052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ryn052_02', 1)	# 1-1
    sprite('ryn052_02', 1)	# 2-2
    sprite('ryn052_02', 2)	# 3-4
    sprite('ryn052_01', 2)	# 5-6
    sprite('ryn052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ryn052_02', 1)	# 1-1
    sprite('ryn052_03', 1)	# 2-2
    sprite('ryn052_02', 2)	# 3-4
    sprite('ryn052_02', 2)	# 5-6
    sprite('ryn052_01', 2)	# 7-8
    sprite('ryn052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ryn052_03', 1)	# 1-1
    sprite('ryn052_03', 1)	# 2-2
    sprite('ryn052_03', 2)	# 3-4
    sprite('ryn052_02', 2)	# 5-6
    sprite('ryn052_02', 2)	# 7-8
    sprite('ryn052_01', 2)	# 9-10
    sprite('ryn052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ryn054_00', 1)	# 1-1
    sprite('ryn054_01', 1)	# 2-2
    sprite('ryn054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ryn054_01', 1)	# 1-1
    sprite('ryn054_02', 1)	# 2-2
    sprite('ryn054_01', 2)	# 3-4
    sprite('ryn054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ryn054_02', 1)	# 1-1
    sprite('ryn054_02', 1)	# 2-2
    sprite('ryn054_02', 2)	# 3-4
    sprite('ryn054_01', 2)	# 5-6
    sprite('ryn054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ryn054_02', 1)	# 1-1
    sprite('ryn054_03', 1)	# 2-2
    sprite('ryn054_02', 2)	# 3-4
    sprite('ryn054_02', 2)	# 5-6
    sprite('ryn054_01', 2)	# 7-8
    sprite('ryn054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ryn054_03', 1)	# 1-1
    sprite('ryn054_03', 1)	# 2-2
    sprite('ryn054_03', 2)	# 3-4
    sprite('ryn054_02', 2)	# 5-6
    sprite('ryn054_02', 2)	# 7-8
    sprite('ryn054_01', 2)	# 9-10
    sprite('ryn054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ryn062_00', 3)	# 1-3
    label(0)
    sprite('ryn062_01', 3)	# 4-6
    sprite('ryn062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ryn062_03', 2)	# 1-2
    sprite('ryn062_04', 2)	# 3-4

@State
def CmnActBDownDown():
    sprite('ryn062_05', 3)	# 1-3
    sprite('ryn062_06', 3)	# 4-6
    label(0)
    sprite('ryn062_07', 3)	# 7-9
    sprite('ryn062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ryn062_09', 2)	# 1-2
    sprite('ryn062_10', 2)	# 3-4

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
    sprite('ryn063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ryn063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ryn063_02', 3)	# 1-3
    sprite('ryn063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ryn063_04', 3)	# 1-3
    sprite('ryn063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('ryn063_06', 4)	# 1-4
    sprite('ryn063_07', 3)	# 5-7
    sprite('ryn063_08', 3)	# 8-10
    sprite('ryn063_09', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('ryn063_09', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ryn064_00', 2)	# 1-2
    sprite('ryn064_01', 3)	# 3-5
    sprite('ryn064_02', 3)	# 6-8
    sprite('ryn064_03', 3)	# 9-11
    sprite('ryn010_02', 3)	# 12-14
    sprite('ryn010_01', 3)	# 15-17
    sprite('ryn010_00', 3)	# 18-20

@State
def CmnActVDownUpper():
    sprite('ryn062_00', 3)	# 1-3
    label(0)
    sprite('ryn062_01', 3)	# 4-6
    sprite('ryn062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ryn062_03', 2)	# 1-2
    sprite('ryn062_04', 2)	# 3-4

@State
def CmnActVDownDown():
    sprite('ryn062_05', 3)	# 1-3
    sprite('ryn062_06', 3)	# 4-6
    label(0)
    sprite('ryn062_07', 3)	# 7-9
    sprite('ryn062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ryn063_04', 3)	# 1-3
    sprite('ryn063_05', 3)	# 4-6

@State
def CmnActBlowoff():
    sprite('ryn072_00', 3)	# 1-3
    label(0)
    sprite('ryn072_01', 3)	# 4-6
    sprite('ryn072_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ryn074_00', 3)	# 1-3
    sprite('ryn074_01', 3)	# 4-6
    sprite('ryn074_02', 3)	# 7-9
    sprite('ryn074_03', 3)	# 10-12
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
    sprite('ryn062_00', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ryn073_00', 3)	# 1-3
    sprite('ryn073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('ryn073_02', 3)	# 1-3
    sprite('ryn073_03', 3)	# 4-6
    label(0)
    sprite('ryn063_02', 3)	# 7-9
    sprite('ryn063_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ryn070_00', 3)	# 1-3
    label(0)
    sprite('ryn070_01', 4)	# 4-7
    sprite('ryn070_02', 4)	# 8-11
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('ryn070_03', 4)	# 1-4
    sprite('ryn070_04', 4)	# 5-8
    sprite('ryn070_05', 4)	# 9-12
    sprite('ryn070_06', 4)	# 13-16
    sprite('ryn070_07', 4)	# 17-20
    sprite('ryn070_08', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ryn070_09', 4)	# 1-4
    sprite('ryn070_10', 2)	# 5-6
    sprite('ryn070_11', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ryn113_00', 3)	# 1-3
    sprite('ryn113_01', 3)	# 4-6
    sprite('ryn113_02', 9)	# 7-15

@State
def CmnActUkemiAirB():
    sprite('ryn113_00', 3)	# 1-3
    sprite('ryn113_01', 3)	# 4-6
    sprite('ryn113_02', 9)	# 7-15

@State
def CmnActUkemiAirN():
    sprite('ryn113_00', 3)	# 1-3
    sprite('ryn113_01', 3)	# 4-6
    sprite('ryn113_02', 9)	# 7-15

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
    sprite('ryn112_00', 2)	# 1-2
    sprite('ryn112_01', 2)	# 3-4
    sprite('ryn112_02', 2)	# 5-6
    sprite('ryn112_03', 2)	# 7-8
    sprite('ryn112_04', 2)	# 9-10
    sprite('ryn112_05', 2)	# 11-12
    sprite('ryn112_06', 2)	# 13-14
    sprite('ryn112_07', 2)	# 15-16
    label(0)
    sprite('ryn020_07', 3)	# 17-19
    sprite('ryn020_08', 3)	# 20-22
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('ryn010_00', 5)	# 1-5
    sprite('ryn010_01', 5)	# 6-10
    sprite('ryn010_00', 5)	# 11-15

@State
def CmnActMidGuardPre():
    sprite('ryn040_00', 3)	# 1-3
    sprite('ryn040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ryn040_02', 3)	# 1-3
    sprite('ryn040_03', 3)	# 4-6
    sprite('ryn040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ryn040_01', 3)	# 1-3
    sprite('ryn040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    label(0)
    sprite('ryn040_02', 3)	# 1-3
    sprite('ryn040_03', 3)	# 4-6
    sprite('ryn040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ryn040_01', 3)	# 1-3
    sprite('ryn040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ryn040_00', 3)	# 1-3
    sprite('ryn040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('ryn040_02', 3)	# 1-3
    sprite('ryn040_03', 3)	# 4-6
    sprite('ryn040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ryn040_01', 3)	# 1-3
    sprite('ryn040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    label(0)
    sprite('ryn040_02', 3)	# 1-3
    sprite('ryn040_03', 3)	# 4-6
    sprite('ryn040_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ryn040_01', 3)	# 1-3
    sprite('ryn040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ryn043_00', 3)	# 1-3
    sprite('ryn043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ryn043_02', 3)	# 1-3
    sprite('ryn043_03', 3)	# 4-6
    sprite('ryn043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ryn043_01', 3)	# 1-3
    sprite('ryn043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    label(0)
    sprite('ryn043_02', 3)	# 1-3
    sprite('ryn043_03', 3)	# 4-6
    sprite('ryn043_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ryn043_01', 3)	# 1-3
    sprite('ryn043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ryn045_00', 3)	# 1-3
    sprite('ryn045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ryn045_02', 3)	# 1-3
    sprite('ryn045_03', 3)	# 4-6
    sprite('ryn045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ryn045_01', 3)	# 1-3
    sprite('ryn045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    label(0)
    sprite('ryn045_02', 3)	# 1-3
    sprite('ryn045_03', 3)	# 4-6
    sprite('ryn045_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ryn045_01', 3)	# 1-3
    sprite('ryn045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ryn040_04', 2)	# 1-2
    sprite('ryn040_04', 2)	# 3-4
    sprite('ryn040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ryn040_02', 4)	# 6-9
    sprite('ryn040_01', 4)	# 10-13
    sprite('ryn040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ryn043_04', 2)	# 1-2
    sprite('ryn043_04', 2)	# 3-4
    sprite('ryn043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ryn043_02', 4)	# 6-9
    sprite('ryn043_01', 4)	# 10-13
    sprite('ryn043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ryn045_04', 2)	# 1-2
    sprite('ryn045_04', 2)	# 3-4
    sprite('ryn045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ryn045_02', 4)	# 6-9
    sprite('ryn045_01', 4)	# 10-13
    sprite('ryn045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('ryn025_00', 4)	# 1-4
    sprite('ryn025_01', 4)	# 5-8
    sprite('ryn025_00ex01', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('keep', 6)	# 1-6

@State
def CmnActLockReject():
    sprite('ryn312_00', 3)	# 1-3
    sprite('ryn312_01', 2)	# 4-5
    sprite('ryn312_02', 3)	# 6-8	 **attackbox here**
    sprite('ryn312_03', 3)	# 9-11
    sprite('ryn312_04', 3)	# 12-14
    sprite('ryn312_05', 3)	# 15-17
    sprite('ryn312_06', 4)	# 18-21
    sprite('ryn312_07', 4)	# 22-25
    sprite('ryn312_08', 4)	# 26-29

@State
def CmnActAirLockWait():
    sprite('ny045_02', 1)	# 1-1
    sprite('ny045_01', 3)	# 2-4
    sprite('ny045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('ny322_00', 2)	# 1-2
    sprite('ny322_01', 2)	# 3-4
    sprite('ny322_02', 2)	# 5-6
    sprite('ny322_03', 8)	# 7-14
    sprite('ny322_04', 4)	# 15-18
    sprite('ny322_05', 3)	# 19-21
    sprite('ny322_06', 3)	# 22-24
    sprite('ny322_07', 3)	# 25-27
    sprite('ny322_08', 2)	# 28-29

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
    sprite('ryn077_00', 2)	# 1-2
    sprite('ryn077_01', 2)	# 3-4
    sprite('ryn077_00ex00', 2)	# 5-6
    sprite('ryn077_01ex00', 2)	# 7-8
    sprite('ryn077_00ex01', 2)	# 9-10
    sprite('ryn077_01ex01', 2)	# 11-12
    sprite('ryn077_00ex02', 2)	# 13-14
    sprite('ryn077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ryn077_02', 4)	# 1-4
    label(0)
    sprite('ryn077_03', 3)	# 5-7
    sprite('ryn077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ryn077_05', 5)	# 1-5
    sprite('ryn077_06', 4)	# 6-9

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
    sprite('ryn333_00', 6)	# 1-6
    sprite('ryn333_01', 32767)	# 7-32773
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('ryn333_02', 2)	# 1-2
    SFX_3('rynse_10')
    sprite('ryn333_03', 2)	# 3-4
    GFX_0('rynef_OD_Begin', -1)
    sprite('ryn333_04', 2)	# 5-6
    sprite('ryn333_05', 2)	# 7-8
    label(0)
    sprite('ryn333_03', 2)	# 9-10
    sprite('ryn333_04', 2)	# 11-12
    sprite('ryn333_05', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('ryn333_06', 4)	# 5-8
    sprite('ryn333_07', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('ryn333_08', 6)	# 1-6
    sprite('ryn333_01', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('ryn333_02', 2)	# 1-2
    SFX_3('rynse_10')
    sprite('ryn333_03', 2)	# 3-4
    GFX_0('rynef_OD_Begin', -1)
    sprite('ryn333_04', 2)	# 5-6
    sprite('ryn333_05', 2)	# 7-8
    label(0)
    sprite('ryn333_03', 2)	# 9-10
    sprite('ryn333_04', 2)	# 11-12
    sprite('ryn333_05', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('keep', 4)	# 1-4
    sprite('ryn333_09', 4)	# 5-8
    sprite('ryn333_10', 4)	# 9-12
    sprite('ryn020_04', 3)	# 13-15
    sprite('ryn020_05', 3)	# 16-18
    sprite('ryn020_06', 3)	# 19-21
    label(0)
    sprite('ryn020_07', 3)	# 22-24
    sprite('ryn020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('ryn333_00', 6)	# 1-6
    sprite('ryn333_01', 32767)	# 7-32773
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('ryn333_02', 2)	# 1-2
    SFX_3('rynse_10')
    sprite('ryn333_03', 2)	# 3-4
    GFX_0('rynef_OD_Begin', -1)
    sprite('ryn333_04', 2)	# 5-6
    sprite('ryn333_05', 2)	# 7-8
    label(0)
    sprite('ryn333_03', 2)	# 9-10
    sprite('ryn333_04', 2)	# 11-12
    sprite('ryn333_05', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('ryn333_06', 4)	# 5-8
    sprite('ryn333_07', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('ryn333_08', 6)	# 1-6
    sprite('ryn333_01', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('ryn333_02', 2)	# 1-2
    SFX_3('rynse_10')
    sprite('ryn333_03', 2)	# 3-4
    GFX_0('rynef_OD_Begin', -1)
    sprite('ryn333_04', 2)	# 5-6
    sprite('ryn333_05', 2)	# 7-8
    label(0)
    sprite('ryn333_03', 2)	# 9-10
    sprite('ryn333_04', 2)	# 11-12
    sprite('ryn333_05', 2)	# 13-14
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('keep', 4)	# 1-4
    sprite('ryn333_09', 4)	# 5-8
    sprite('ryn333_10', 4)	# 9-12
    sprite('ryn020_04', 3)	# 13-15
    sprite('ryn020_05', 3)	# 16-18
    sprite('ryn020_06', 3)	# 19-21
    label(0)
    sprite('ryn020_07', 3)	# 22-24
    sprite('ryn020_08', 3)	# 25-27
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('ryn333_00', 6)	# 1-6
    sprite('ryn333_01', 32767)	# 7-32773
    loopRest()

@State
def CmnActCrossChangeLoop():
    sprite('ryn333_02', 2)	# 1-2
    label(0)
    sprite('ryn333_03', 2)	# 3-4
    sprite('ryn333_04', 2)	# 5-6
    sprite('ryn333_05', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('keep', 4)	# 1-4
    sprite('ryn333_06', 4)	# 5-8
    sprite('ryn333_07', 4)	# 9-12

@State
def CmnActAirCrossChangeBegin():
    sprite('ryn333_08', 6)	# 1-6
    sprite('ryn333_01', 32767)	# 7-32773
    loopRest()

@State
def CmnActAirCrossChangeLoop():
    sprite('ryn333_02', 2)	# 1-2
    label(0)
    sprite('ryn333_03', 2)	# 3-4
    sprite('ryn333_04', 2)	# 5-6
    sprite('ryn333_05', 2)	# 7-8
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('keep', 4)	# 1-4
    sprite('ryn333_09', 4)	# 5-8
    sprite('ryn333_10', 4)	# 9-12
    sprite('ryn020_04', 3)	# 13-15
    sprite('ryn020_05', 3)	# 16-18
    label(0)
    sprite('ryn020_06', 3)	# 19-21
    sprite('ryn020_07', 3)	# 22-24
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
        Unknown9015(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown8000(100, 1, 1)
            Unknown1084(1)
            sendToLabel(2)
    sprite('null', 25)	# 1-25
    label(0)
    sprite('ryn203_06', 2)	# 26-27	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-130000)
    Unknown1007(2400000)
    physicsYImpulse(-240000)
    setGravity(0)
    Unknown2053(1)
    Unknown2017(1)
    GFX_0('rynef203_Fall', 0)
    sprite('ryn203_07', 2)	# 28-29	 **attackbox here**
    sprite('ryn203_06', 2)	# 30-31	 **attackbox here**
    label(1)
    sprite('ryn203_07', 2)	# 32-33	 **attackbox here**
    sprite('ryn203_06', 2)	# 34-35	 **attackbox here**
    gotoLabel(1)
    label(2)
    sprite('ryn203_08', 4)	# 36-39	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 30000)
    Unknown26('rynef203_Fall')
    GFX_0('rynef203_ShockWave', -1)
    sprite('ryn203_09', 3)	# 40-42
    sprite('ryn203_10', 3)	# 43-45
    sprite('ryn203_12', 3)	# 46-48
    sprite('ryn203_13', 3)	# 49-51
    sprite('ryn203_14', 3)	# 52-54
    sprite('ryn203_15', 3)	# 55-57
    sprite('ryn203_16', 3)	# 58-60

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ryn033_01', 3)	# 1-3
    sprite('ryn033_02', 3)	# 4-6
    sprite('ryn033_01', 3)	# 7-9
    Unknown13(4)
    SLOT_7 = 0
    sprite('ryn033_02', 3)	# 10-12
    sprite('ryn033_01', 3)	# 13-15
    sprite('ryn033_02', 3)	# 16-18
    sprite('ryn033_01', 3)	# 19-21
    sprite('ryn033_02', 3)	# 22-24
    sprite('ryn033_01', 3)	# 25-27
    sprite('ryn033_02', 3)	# 28-30
    sprite('ryn033_01', 30)	# 31-60

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
        Unknown2004(1, 0)
    sprite('ryn300_00', 6)	# 1-6
    sprite('ryn300_01', 6)	# 7-12
    sprite('ryn300_02', 6)	# 13-18
    sprite('ryn300_03', 6)	# 19-24
    sprite('ryn300_04', 6)	# 25-30
    sprite('ryn300_05', 6)	# 31-36
    sprite('ryn300_04', 6)	# 37-42
    sprite('ryn300_03', 6)	# 43-48
    sprite('ryn300_04', 6)	# 49-54
    sprite('ryn300_05', 6)	# 55-60
    sprite('ryn300_02', 6)	# 61-66
    sprite('ryn300_01', 6)	# 67-72
    sprite('ryn300_00', 6)	# 73-78
    sprite('ryn000_00', 30)	# 79-108

@State
def CmnActChangeRequest():
    pass

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('ryn203_06', 2)	# 121-122	 **attackbox here**
    Unknown1086(22)
    teleportRelativeX(-130000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    GFX_0('rynef203_Fall', 0)
    sprite('ryn203_07', 2)	# 123-124	 **attackbox here**
    sprite('ryn203_06', 2)	# 125-126	 **attackbox here**
    label(2)
    sprite('ryn203_07', 2)	# 127-128	 **attackbox here**
    sprite('ryn203_06', 2)	# 129-130	 **attackbox here**
    gotoLabel(2)
    label(1)
    sprite('ryn203_08', 3)	# 131-133	 **attackbox here**
    StartMultihit()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 30000)
    Unknown26('rynef203_Fall')
    GFX_0('rynef203_ShockWave', -1)
    sprite('ryn203_09', 4)	# 134-137
    sprite('ryn203_10', 4)	# 138-141
    sprite('ryn203_12', 4)	# 142-145
    sprite('ryn203_13', 4)	# 146-149
    sprite('ryn203_14', 4)	# 150-153
    sprite('ryn203_15', 4)	# 154-157
    sprite('ryn203_16', 4)	# 158-161

@State
def CmnActChangeReturnAppealBurst():
    sprite('ryn611_08', 5)	# 1-5
    sprite('ryn611_09', 5)	# 6-10
    sprite('ryn611_10', 5)	# 11-15
    sprite('ryn611_11', 5)	# 16-20
    sprite('ryn611_12', 5)	# 21-25
    sprite('ryn611_13', 15)	# 26-40
    sprite('ryn611_12', 5)	# 41-45
    sprite('ryn611_11', 5)	# 46-50
    sprite('ryn611_10', 5)	# 51-55
    sprite('ryn611_09', 30)	# 56-85

@State
def CmnActChangePartnerQuickIn():
    sprite('ryn032_07', 3)	# 1-3
    sprite('ryn032_08', 3)	# 4-6
    sprite('ryn032_09', 3)	# 7-9
    sprite('ryn032_10', 4)	# 10-13
    sprite('ryn032_11', 4)	# 14-17
    sprite('ryn032_12', 4)	# 18-21
    sprite('ryn032_13', 4)	# 22-25
    sprite('ryn032_14', 4)	# 26-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('ryn033_00', 3)	# 1-3
    sprite('ryn033_01', 2)	# 4-5
    Unknown3001(255)
    Unknown3004(-42)
    Unknown23001(0, 0)
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ryn033_01', 1)	# 6-6
    sprite('ryn033_02', 3)	# 7-9
    Unknown13(4)
    SLOT_7 = 0
    loopRest()
    label(0)
    sprite('ryn033_01', 3)	# 10-12
    sprite('ryn033_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ryn033_03', 3)	# 16-18
    Unknown1084(1)
    sprite('ryn033_04', 3)	# 19-21

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
    sprite('ryn020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ryn020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ryn010_01', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1200)
        GroundedHitstunAnimation(9)
        AttackP1(70)
        AttackP2(85)
        Unknown11092(1)
        Unknown11042(1)
        AirPushbackY(10000)
        PushbackX(15300)
        AirUntechableTime(25)
        Hitstop(3)
        Unknown11042(1)
        Unknown23027()
    sprite('ryn430_00', 4)	# 1-4
    sprite('ryn430_01', 4)	# 5-8
    tag_voice(1, 'ryn305_0', 'ryn305_1', '', '')
    sprite('ryn430_02', 4)	# 9-12
    sprite('ryn430_03', 4)	# 13-16
    sprite('ryn430_04', 4)	# 17-20
    physicsXImpulse(10000)
    GFX_0('rynef_6Assist_Speed', -1)
    SFX_3('rynse_04')
    sprite('ryn430_05', 4)	# 21-24
    Unknown1019(200)
    sprite('ryn430_06', 4)	# 25-28
    Unknown1019(500)
    sprite('ryn430_07', 4)	# 29-32
    sprite('ryn403_12', 3)	# 33-35
    Unknown1019(25)
    sprite('ryn403_13', 3)	# 36-38
    Unknown1019(50)
    Unknown26('rynef_6Assist_Speed')
    sprite('ryn403_14', 3)	# 39-41	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9902, 0)
    sprite('ryn201_01', 3)	# 42-44
    Unknown1019(50)
    sprite('ryn201_02', 3)	# 45-47
    Unknown1019(50)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn201_03', 3)	# 48-50	 **attackbox here**
    Unknown1019(50)
    RefreshMultihit()
    GFX_0('rynef201', -1)
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9903, 0)
    sprite('ryn202_01', 3)	# 51-53
    teleportRelativeX(60000)
    Unknown1019(50)
    Unknown2004(1, 0)
    sprite('ryn202_02', 3)	# 54-56
    Unknown1019(50)
    sprite('ryn202_03', 3)	# 57-59
    Unknown1019(50)
    Unknown7009(2)
    SFX_0('004_swing_grap_1_2')
    sprite('ryn202_04ex', 3)	# 60-62	 **attackbox here**
    RefreshMultihit()
    AirPushbackY(35000)
    Unknown9215()
    AirUntechableTime(60)
    Hitstop(6)
    Unknown1084(1)
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9904, 0)
    sprite('ryn202_05', 3)	# 63-65
    Recovery()
    sprite('ryn202_06', 3)	# 66-68
    sprite('ryn202_07', 3)	# 69-71
    sprite('ryn202_08', 3)	# 72-74
    sprite('ryn202_09', 3)	# 75-77
    sprite('ryn202_10', 3)	# 78-80
    sprite('ryn202_11', 3)	# 81-83
    sprite('ryn202_12', 3)	# 84-86
    sprite('ryn202_13', 3)	# 87-89

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(70)
        AirHitstunAnimation(1)
        GroundedHitstunAnimation(1)
        AirPushbackX(1500)
        AirPushbackY(45000)
        AirUntechableTime(60)
        Unknown11042(1)
        if SLOT_5:
            Unknown11092(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
    sprite('ryn402_07', 4)	# 1-4
    physicsXImpulse(20000)
    sprite('ryn402_08', 4)	# 5-8
    Unknown1019(25)
    SFX_3('rynse_06')
    sprite('ryn402_09', 1)	# 9-9
    Unknown1019(50)
    tag_voice(1, 'ryn306_0', 'ryn306_1', '', '')
    sprite('ryn402_09', 3)	# 10-12
    GFX_0('rynef402_2nd', -1)
    sprite('ryn402_10', 10)	# 13-22	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9906, 0)
    physicsXImpulse(10000)
    physicsYImpulse(25000)
    Unknown1043()
    sprite('ryn431_29', 3)	# 23-25
    Recovery()
    sprite('ryn431_30', 3)	# 26-28
    label(0)
    sprite('ryn320_10', 3)	# 29-31
    sprite('ryn320_11', 3)	# 32-34
    gotoLabel(0)
    label(1)
    sprite('ryn010_00', 3)	# 35-37
    sprite('ryn010_01', 3)	# 38-40
    sprite('ryn010_00', 3)	# 41-43

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(70)
        AttackP2(80)
        Unknown11092(1)
        AirPushbackY(13000)
        AirUntechableTime(30)
        Unknown11042(1)

        def upon_12():
            clearUponHandler(12)
            Hitstop(3)
            sendToLabel(1)
            GFX_0('rynef402_Singal02', -1)
    sprite('ryn402_00', 3)	# 1-3
    sprite('ryn402_01', 3)	# 4-6
    sprite('ryn402_02', 3)	# 7-9
    sprite('ryn402_03', 3)	# 10-12
    sprite('ryn402_04', 3)	# 13-15
    physicsXImpulse(80000)
    GFX_0('rynef402', -1)
    sprite('ryn402_05', 3)	# 16-18	 **attackbox here**
    Unknown1019(70)
    sprite('ryn402_06', 3)	# 19-21	 **attackbox here**
    GFX_0('rynef402_Singal01', -1)
    sprite('ryn402_05', 3)	# 22-24	 **attackbox here**
    sprite('ryn402_20', 4)	# 25-28
    Unknown1019(25)
    GFX_0('rynef402_Singal02', -1)
    Recovery()
    sprite('ryn402_21', 4)	# 29-32
    Unknown1019(50)
    sprite('ryn402_22', 4)	# 33-36
    Unknown1019(50)
    sprite('ryn402_23', 4)	# 37-40
    Unknown1019(0)
    sprite('ryn402_24', 4)	# 41-44
    ExitState()
    label(1)
    sprite('ryn402_20', 3)	# 45-47
    Unknown1019(50)
    sprite('ryn402_21', 3)	# 48-50
    Unknown1019(50)
    sprite('ryn271_00', 2)	# 51-52
    Unknown1019(0)
    Unknown2004(1, 0)
    sprite('ryn271_01', 2)	# 53-54
    SFX_0('005_swing_grap_2_0')
    sprite('ryn271_02', 3)	# 55-57
    RefreshMultihit()
    AttackLevel_(4)
    GFX_0('rynef271', -1)
    sprite('ryn271_03', 2)	# 58-59	 **attackbox here**
    sprite('ryn272_00', 2)	# 60-61
    GFX_0('rynef272_Muzzle', -1)
    sprite('ryn272_01', 2)	# 62-63
    SFX_0('011_spin_1')
    sprite('ryn272_01ex', 2)	# 64-65
    sprite('ryn272_00', 2)	# 66-67
    sprite('ryn272_01', 2)	# 68-69
    tag_voice(1, 'ryn106_0', 'ryn106_1', 'ryn106_2', '')
    GFX_0('rynef272', -1)
    SFX_0('005_swing_grap_2_1')
    sprite('ryn272_02', 3)	# 70-72	 **attackbox here**
    RefreshMultihit()
    Damage(1500)
    GroundedHitstunAnimation(9)
    AirPushbackX(50000)
    AirPushbackY(20000)
    Unknown9178(1)
    Hitstop(6)
    WallbounceReboundTime(0)
    AirHitstunAfterWallbounce(40)
    sprite('ryn272_03', 4)	# 73-76
    Recovery()
    Unknown2063()
    sprite('ryn272_04', 4)	# 77-80
    sprite('ryn272_05', 4)	# 81-84
    sprite('ryn272_06', 4)	# 85-88
    sprite('ryn272_07', 4)	# 89-92
    sprite('ryn272_08', 4)	# 93-96
    sprite('ryn272_09', 3)	# 97-99
    sprite('ryn272_10', 3)	# 100-102

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
    Unknown2036(77, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-700000)
    Unknown1019(4)
    label(0)
    sprite('ryn020_07', 3)	# 3-5
    sprite('ryn020_08', 3)	# 6-8
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
        Hitstop(20)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        setInvincible(1)
        GroundedHitstunAnimation(9)
        Unknown11056(0)
        AirUntechableTime(60)
        AirPushbackX(60000)
        AirPushbackY(35000)

        def upon_3():
            if SLOT_51:
                if (SLOT_163 < 300000):
                    Unknown1019(50)
        Unknown11050('0200000072796e65663433305f4869744100000000000000000000000000000000000000')

        def upon_11():
            ScreenShake(100000, 100000)
            Unknown2037(1)
    sprite('ryn430_00', 6)	# 1-6
    sprite('ryn430_01', 6)	# 7-12
    sprite('ryn430_02', 6)	# 13-18
    sprite('ryn430_03', 12)	# 19-30
    sprite('ryn430_04', 6)	# 31-36
    sprite('ryn430_05', 3)	# 37-39
    SFX_3('rynse_12')
    sprite('ryn430_06', 3)	# 40-42
    GFX_0('rynef430', -1)
    physicsXImpulse(30000)
    sprite('ryn430_07', 3)	# 43-45
    Unknown1019(500)
    sprite('ryn430_08', 3)	# 46-48
    Unknown1019(50)
    SLOT_51 = 1
    sprite('ryn430_09', 2)	# 49-50
    GFX_0('rynef403', -1)
    Unknown1019(50)
    sprite('ryn430_10', 2)	# 51-52	 **attackbox here**
    SLOT_51 = 0
    StartMultihit()
    GFX_0('rynef430_DashSingal', -1)
    sprite('ryn430_15', 3)	# 53-55	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    sprite('ryn430_16', 3)	# 56-58
    setInvincible(0)
    physicsXImpulse(10000)
    GFX_0('rynef430_DashEnd', -1)
    GFX_0('rynef_DDD_Particle', -1)
    label(0)
    sprite('ryn430_17', 3)	# 59-61
    sprite('ryn430_18', 3)	# 62-64
    sprite('ryn430_19', 2)	# 65-66
    sprite('keep', 1)	# 67-67
    if (SLOT_2 > 0):
        Unknown2038(-1)
        sendToLabel(0)
    sprite('ryn430_20', 5)	# 68-72
    Unknown8000(100, 1, 1)
    Unknown1019(25)
    sprite('ryn430_21', 5)	# 73-77
    sprite('ryn430_22', 5)	# 78-82
    Unknown1084(1)
    sprite('ryn430_23', 5)	# 83-87
    sprite('ryn430_24', 5)	# 88-92

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        setInvincible(1)
        AttackLevel_(5)
        Damage(2000)
        Unknown11091(100)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(9)
        Unknown11001(30, 30, 30)

        def upon_3():
            if SLOT_51:
                if (SLOT_163 < 300000):
                    Unknown1019(50)
        Unknown11056(0)
        AirUntechableTime(60)
        AirPushbackX(60000)
        AirPushbackY(35000)
    sprite('ryn430_00', 6)	# 1-6
    sprite('ryn430_01', 6)	# 7-12
    sprite('ryn430_02', 6)	# 13-18
    sprite('ryn430_03', 14)	# 19-32
    sprite('ryn430_04', 6)	# 33-38
    sprite('ryn430_05', 3)	# 39-41
    SFX_3('rynse_12')
    sprite('ryn430_06', 3)	# 42-44
    GFX_0('rynef430', -1)
    physicsXImpulse(30000)
    sprite('ryn430_07', 3)	# 45-47
    Unknown1019(500)
    sprite('ryn430_08', 3)	# 48-50
    Unknown1019(50)
    SLOT_51 = 1
    sprite('ryn430_09', 2)	# 51-52
    GFX_0('rynef403', -1)
    Unknown1019(50)
    sprite('ryn430_10', 2)	# 53-54	 **attackbox here**
    GFX_0('rynef430_DashSingal', -1)
    SLOT_51 = 0
    Unknown11050('0200000072796e65665f45584849545f4200000000000000000000000000000000000000')

    def upon_78():
        clearUponHandler(78)
        clearUponHandler(80)
        sendToLabel(1)
        GFX_0('rynef430_Flare', -1)

    def upon_80():
        clearUponHandler(78)
        clearUponHandler(80)
        sendToLabel(1)
        GFX_0('rynef430_Flare', -1)
    sprite('ryn430_15', 3)	# 55-57	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    clearUponHandler(78)
    clearUponHandler(80)
    Unknown11050('0200000072796e65663433305f4869744100000000000000000000000000000000000000')

    def upon_11():
        ScreenShake(100000, 100000)
        Unknown2037(1)
    label(100)
    sprite('ryn430_16', 3)	# 58-60
    GFX_0('rynef430_DashEnd', -1)
    GFX_0('rynef_DDD_Particle', -1)
    setInvincible(0)
    physicsXImpulse(10000)
    label(0)
    sprite('ryn430_17', 3)	# 61-63
    sprite('ryn430_18', 3)	# 64-66
    sprite('ryn430_19', 2)	# 67-68
    sprite('keep', 1)	# 69-69
    if (SLOT_2 > 0):
        Unknown2038(-1)
        sendToLabel(0)
    sprite('ryn430_20', 5)	# 70-74
    Unknown8000(100, 1, 1)
    Unknown1019(25)
    sprite('ryn430_21', 5)	# 75-79
    sprite('ryn430_22', 5)	# 80-84
    Unknown1084(1)
    sprite('ryn430_23', 5)	# 85-89
    sprite('ryn430_24', 5)	# 90-94
    ExitState()
    label(1)
    sprite('ryn430_11', 6)	# 95-100
    Unknown1019(10)
    sprite('ryn430_12', 6)	# 101-106
    sprite('ryn430_13', 6)	# 107-112
    GFX_0('rynef430_DashEnd', -1)
    sprite('ryn430_14', 3)	# 113-115
    sprite('ryn430_14', 3)	# 116-118
    sprite('ryn430_15', 2)	# 119-120	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    RefreshMultihit()
    AttackLevel_(5)
    Unknown11056(0)
    Damage(500)
    Hitstop(20)
    Unknown11001(0, 0, 8)
    Unknown11050('0200000072796e65663433305f4869744100000000000000000000000000000000000000')

    def upon_11():
        ScreenShake(150000, 150000)
        Unknown2037(1)
    sprite('keep', 10)	# 121-130
    Unknown1019(1000)
    sendToLabel(100)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        Damage(1200)
        AirPushbackY(15000)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2064(0)
        Unknown1112('')
    sprite('ryn200_00', 3)	# 1-3
    sprite('ryn200_01', 2)	# 4-5
    Unknown7009(0)
    SFX_0('004_swing_grap_1_0')
    sprite('ryn200_02', 3)	# 6-8	 **attackbox here**
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9901, 0)
    sprite('ryn200_03', 3)	# 9-11
    Recovery()
    Unknown2063()
    sprite('ryn200_04', 4)	# 12-15
    sprite('ryn200_01', 4)	# 16-19
    sprite('ryn200_00', 4)	# 20-23

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(15000)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2064(0)
        Unknown2004(1, 0)
    sprite('ryn270_00', 3)	# 1-3
    sprite('ryn270_01', 2)	# 4-5
    sprite('ryn270_02', 2)	# 6-7
    SFX_0('004_swing_grap_1_1')
    sprite('ryn270_03', 3)	# 8-10	 **attackbox here**
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9902, 0)
    sprite('ryn270_04', 4)	# 11-14
    Recovery()
    Unknown2063()
    sprite('ryn270_05', 4)	# 15-18
    sprite('ryn270_06', 5)	# 19-23
    sprite('ryn270_07', 5)	# 24-28

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirPushbackX(10000)
        AirPushbackY(20000)
        AirUntechableTime(22)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        Unknown2004(1, 0)
    sprite('ryn271_00', 3)	# 1-3
    sprite('ryn271_01', 3)	# 4-6
    Unknown7009(1)
    sprite('ryn271_02', 3)	# 7-9
    GFX_0('rynef271', -1)
    SFX_0('005_swing_grap_2_0')
    sprite('ryn271_03', 3)	# 10-12	 **attackbox here**
    sprite('ryn271_04', 3)	# 13-15
    Recovery()
    Unknown2063()
    sprite('ryn271_05', 3)	# 16-18
    sprite('ryn271_06', 3)	# 19-21
    sprite('ryn271_07', 3)	# 22-24
    sprite('ryn271_08', 3)	# 25-27
    sprite('ryn271_09', 3)	# 28-30
    sprite('ryn271_10', 3)	# 31-33

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        Damage(2500)
        AirUntechableTime(35)
        GroundedHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(20000)
        Unknown2004(1, 0)
        JumpCancel_(0)
        SLOT_4 = 1
    sprite('ryn272_00', 2)	# 1-2
    GFX_0('rynef272_Muzzle', -1)
    sprite('ryn272_01', 2)	# 3-4
    SFX_0('011_spin_2')
    sprite('ryn272_01ex', 2)	# 5-6
    tag_voice(1, 'ryn106_0', 'ryn106_1', 'ryn106_2', '')
    sprite('ryn272_00', 2)	# 7-8
    sprite('ryn272_01', 2)	# 9-10
    SFX_0('005_swing_grap_2_1')
    GFX_0('rynef272', -1)
    sprite('ryn272_02', 3)	# 11-13	 **attackbox here**
    sprite('ryn272_03', 4)	# 14-17
    Recovery()
    Unknown2063()
    sprite('ryn272_04', 4)	# 18-21
    sprite('ryn272_05', 4)	# 22-25
    sprite('ryn272_06', 4)	# 26-29
    sprite('ryn272_07', 4)	# 30-33
    sprite('ryn272_08', 4)	# 34-37
    sprite('ryn272_09', 3)	# 38-40
    sprite('ryn272_10', 3)	# 41-43

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AttackP1(90)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        Unknown2064(0)
        Unknown1112('')
        Unknown2004(1, 0)

        def upon_STATE_END():
            Unknown2004(0, 0)
    sprite('ryn201_00', 3)	# 1-3
    sprite('ryn201_01', 3)	# 4-6
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    Unknown22030(0)
    GuardPoint_(1)
    Unknown22035(100)
    if SLOT_5:
        Unknown22035(0)
    Unknown22031(15, -1)
    physicsXImpulse(15000)
    sprite('ryn201_02', 3)	# 7-9
    Unknown1019(50)
    Unknown7009(1)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn201_03', 3)	# 10-12	 **attackbox here**
    Unknown1019(50)
    GFX_0('rynef201', -1)
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9903, 0)
    sprite('ryn201_04', 5)	# 13-17
    setInvincible(0)
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ryn201_05', 5)	# 18-22
    sprite('ryn201_06', 5)	# 23-27
    sprite('ryn201_07', 5)	# 28-32
    sprite('ryn201_08', 5)	# 33-37

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        GroundedHitstunAnimation(10)
        AirUntechableTime(24)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitJumpCancel(1)
        Unknown2064(0)
    sprite('ryn201_04ex01', 3)	# 1-3
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    Unknown22030(0)
    GuardPoint_(1)
    Unknown22035(100)
    if SLOT_5:
        Unknown22035(0)
    Unknown22031(15, -1)
    sprite('ryn201_05ex01', 3)	# 4-6
    sprite('ryn202_00', 3)	# 7-9
    sprite('ryn202_01', 2)	# 10-11
    Unknown2004(1, 0)
    physicsXImpulse(60000)
    sprite('ryn202_02', 2)	# 12-13
    Unknown1019(50)
    sprite('ryn202_03', 2)	# 14-15
    Unknown1019(50)
    Unknown7009(2)
    SFX_0('004_swing_grap_1_2')
    sprite('ryn202_04', 3)	# 16-18	 **attackbox here**
    Unknown1019(50)
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9904, 0)
    sprite('ryn202_05', 3)	# 19-21
    setInvincible(0)
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ryn202_06', 3)	# 22-24
    sprite('ryn202_07', 3)	# 25-27
    sprite('ryn202_08', 3)	# 28-30
    sprite('ryn202_10', 2)	# 31-32
    sprite('ryn202_11', 3)	# 33-35
    sprite('ryn202_12', 3)	# 36-38
    sprite('ryn202_13', 3)	# 39-41

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        Damage(1200)
        AttackP1(90)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ryn231_00', 2)	# 1-2
    sprite('ryn231_01', 2)	# 3-4
    physicsXImpulse(0)
    sprite('ryn231_02', 2)	# 5-6
    Unknown1019(50)
    Unknown7009(1)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn231_03', 3)	# 7-9	 **attackbox here**
    Unknown1019(50)
    sprite('ryn231_04', 3)	# 10-12
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ryn231_05', 3)	# 13-15
    sprite('ryn231_06', 3)	# 16-18
    sprite('ryn231_07', 3)	# 19-21
    sprite('ryn231_08', 3)	# 22-24

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirUntechableTime(27)
        AirPushbackY(32500)
        AttackP1(90)
        AttackP2(75)
        PushbackX(19800)
        Unknown11058('0000000001000000000000000000000000000000')
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Unknown2064(0)

        def upon_LANDING():
            sendToLabel(9)
    sprite('ryn402_07', 3)	# 1-3
    sprite('ryn402_08', 3)	# 4-6
    physicsXImpulse(10000)
    GFX_0('rynef2B', -1)
    SFX_0('005_swing_grap_2_1')
    sprite('ryn402_09', 2)	# 7-8
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    Unknown7009(2)
    GFX_1('rynef320_smoke', -1)
    sprite('ryn402_10', 8)	# 9-16	 **attackbox here**
    physicsXImpulse(5000)
    physicsYImpulse(25000)
    Unknown1043()
    Unknown18009(0)
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9906, 0)
    sprite('ryn431_29', 4)	# 17-20
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ryn431_30', 4)	# 21-24
    label(0)
    sprite('ryn320_10', 3)	# 25-27
    sprite('ryn320_11', 3)	# 28-30
    gotoLabel(0)
    label(9)
    sprite('ryn010_00', 2)	# 31-32
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ryn010_01', 4)	# 33-36

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        Damage(2000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(2500)
        AirPushbackY(16000)
        AirUntechableTime(30)
        AttackP1(90)
        HitLow(2)
        Unknown2004(1, 0)
    sprite('ryn232_00', 3)	# 1-3
    sprite('ryn232_01', 3)	# 4-6
    sprite('ryn232_02', 3)	# 7-9
    physicsXImpulse(20000)
    sprite('ryn232_03', 3)	# 10-12
    Unknown7009(2)
    SFX_0('004_swing_grap_1_2')
    sprite('ryn232_04', 3)	# 13-15	 **attackbox here**
    Unknown1019(75)
    sprite('ryn232_05', 3)	# 16-18
    Unknown1019(50)
    Recovery()
    Unknown2063()
    sprite('ryn232_06', 3)	# 19-21
    Unknown1019(50)
    sprite('ryn232_07', 3)	# 22-24
    Unknown1019(50)
    sprite('ryn232_08', 3)	# 25-27
    Unknown1019(50)
    sprite('ryn232_09', 3)	# 28-30
    Unknown1019(50)
    sprite('ryn232_10', 4)	# 31-34
    Unknown1019(0)
    sprite('ryn232_11', 4)	# 35-38

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1700)
        AttackP1(80)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ryn251_00', 3)	# 1-3
    sprite('ryn251_01', 3)	# 4-6
    sprite('ryn251_02', 4)	# 7-10
    Unknown7009(4)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn251_03', 5)	# 11-15	 **attackbox here**
    sprite('ryn251_04', 6)	# 16-21
    Recovery()
    Unknown2063()
    sprite('ryn251_05', 4)	# 22-25
    sprite('ryn251_06', 4)	# 26-29
    sprite('ryn251_07', 4)	# 30-33
    sprite('ryn251_08', 4)	# 34-37

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Unknown2064(0)
    sprite('ryn250_00', 3)	# 1-3
    sprite('ryn250_01', 3)	# 4-6
    Unknown7009(3)
    sprite('ryn250_02', 3)	# 7-9	 **attackbox here**
    SFX_0('004_swing_grap_1_0')
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9907, 0)
    sprite('ryn250_03', 4)	# 10-13
    Recovery()
    Unknown2063()
    sprite('ryn250_04', 4)	# 14-17
    sprite('ryn250_05', 4)	# 18-21

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1700)
        AttackP1(80)
        if SLOT_5:
            Unknown11092(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5BB')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
        Unknown2064(0)
    sprite('ryn252_00', 3)	# 1-3
    sprite('ryn252_01', 3)	# 4-6
    sprite('ryn252_02', 3)	# 7-9
    sprite('ryn252_03', 3)	# 10-12
    Unknown7009(4)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn252_04', 3)	# 13-15	 **attackbox here**
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9908, 0)
    sprite('ryn252_05', 5)	# 16-20
    Recovery()
    Unknown2063()
    sprite('ryn252_06', 5)	# 21-25
    sprite('ryn252_07', 5)	# 26-30
    sprite('ryn252_08', 4)	# 31-34
    sprite('ryn252_09', 4)	# 35-38
    sprite('ryn252_10', 4)	# 39-42

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(5)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        AirPushbackY(-90000)
        AirUntechableTime(24)
        Unknown9310(1)
        clearUponHandler(2)
        JumpCancel_(0)
        if SLOT_5:
            Unknown11092(1)
    sprite('ryn253_00', 3)	# 1-3
    sprite('ryn253_01', 2)	# 4-5
    Unknown1084(1)
    setGravity(2000)
    physicsXImpulse(10000)
    physicsYImpulse(30000)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
sprite('ryn203_03', 3)	# 6-8
Unknown1019(75)
sprite('ryn203_04', 3)	# 9-11
Unknown1019(75)
GFX_0('rynef203_FistAura', 0)
SFX_3('rynse_07')
sprite('ryn203_05', 2)	# 12-13
Unknown1019(75)
Unknown7009(5)
sprite('ryn203_06', 2)	# 14-15	 **attackbox here**
physicsYImpulse(-50000)
Unknown26('rynef203_FistAura')
GFX_0('rynef203_Fall', 0)
sprite('ryn203_07', 2)	# 16-17	 **attackbox here**
label(0)
sprite('ryn203_06', 2)	# 18-19	 **attackbox here**
sprite('ryn203_07', 2)	# 20-21	 **attackbox here**
gotoLabel(0)
label(1)
sprite('ryn203_08', 3)	# 22-24	 **attackbox here**
Unknown1084(1)
Unknown8000(100, 1, 1)
ScreenShake(0, 30000)
Unknown26('rynef203_Fall')
GFX_0('rynef203_LandParticle', -1)

def upon_12():
    Unknown23073()
if SLOT_5:
    GFX_0('rynef203_ShockWave', -1)
    RefreshMultihit()
    Unknown10000(50)
    HitOverhead(0)
    Unknown9266(1)
else:
    Unknown23027()
    Recovery()
sprite('ryn203_09', 3)	# 25-27
Recovery()
sprite('ryn203_10', 3)	# 28-30
sprite('ryn203_12', 3)	# 31-33
sprite('ryn203_13', 3)	# 34-36
sprite('ryn203_14', 3)	# 37-39
sprite('ryn203_15', 3)	# 40-42
sprite('ryn203_16', 3)	# 43-45
endState()

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown23027()
        Unknown11058('0100000000000000000000000000000000000000')
        clearUponHandler(2)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        if SLOT_5:
            Unknown9266(1)
    sprite('ryn010_00', 3)	# 1-3
    sprite('ryn203_00', 2)	# 4-5
    tag_voice(1, 'ryn157_0', 'ryn157_1', '', '')
    SLOT_12 = SLOT_19
    Unknown1019(6)
    if (SLOT_12 >= 40000):
        SLOT_12 = 40000
    physicsYImpulse(30000)
    setGravity(2000)
    Unknown23087(100000)
    sprite('ryn203_01', 2)	# 6-7
    sprite('ryn203_00', 2)	# 8-9
    sprite('ryn203_02', 3)	# 10-12
    Unknown1019(75)
    YAccel(25)
    Unknown1039(25)
    sprite('ryn203_03', 5)	# 13-17
    Unknown1019(75)
    sprite('ryn203_04', 3)	# 18-20
    Unknown1019(75)
    GFX_0('rynef203_FistAura', 0)
    sprite('ryn203_05', 3)	# 21-23
    Unknown1019(75)
    sprite('ryn203_06', 2)	# 24-25	 **attackbox here**
    physicsYImpulse(-100000)
    Unknown26('rynef203_FistAura')
    GFX_0('rynef203_Fall', 0)
    sprite('ryn203_07', 2)	# 26-27	 **attackbox here**
    label(0)
    sprite('ryn203_06', 2)	# 28-29	 **attackbox here**
    sprite('ryn203_07', 2)	# 30-31	 **attackbox here**
    gotoLabel(0)
    label(1)
    sprite('ryn203_08', 3)	# 32-34	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    ScreenShake(0, 30000)
    Unknown26('rynef203_Fall')
    GFX_0('rynef203_ShockWave', -1)
    GFX_0('rynef203_LandParticle', -1)
    sprite('ryn203_09', 3)	# 35-37
    sprite('ryn203_10', 3)	# 38-40
    sprite('ryn203_12', 2)	# 41-42
    sprite('ryn203_13', 2)	# 43-44
    sprite('ryn203_14', 2)	# 45-46
    sprite('ryn203_15', 3)	# 47-49
    sprite('ryn203_16', 3)	# 50-52

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        if SLOT_5:
            Unknown9266(1)
    sprite('ryn203_09', 3)	# 1-3
    sprite('ryn203_10', 3)	# 4-6
    sprite('ryn203_12', 3)	# 7-9
    sprite('ryn203_13', 3)	# 10-12
    sprite('ryn203_14', 3)	# 13-15
    sprite('ryn203_15', 3)	# 16-18
    sprite('ryn203_16', 3)	# 19-21
    sprite('ryn201_00', 3)	# 22-24
    tag_voice(0, 'ryn158_0', 'ryn158_1', '', '')
    sprite('ryn201_01', 3)	# 25-27
    sprite('ryn201_02', 2)	# 28-29
    SFX_0('004_swing_grap_1_1')
    sprite('ryn201_03', 3)	# 30-32	 **attackbox here**
    GFX_0('rynef201', -1)
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9903, 0)
    sprite('ryn201_04', 3)	# 33-35
    sprite('ryn201_05', 3)	# 36-38
    sprite('ryn201_06', 3)	# 39-41
    sprite('ryn201_07', 3)	# 42-44
    sprite('ryn201_08', 3)	# 45-47
    sprite('ryn000_00', 6)	# 48-53
    sprite('ryn000_01', 6)	# 54-59
    sprite('ryn000_02', 6)	# 60-65
    sprite('ryn000_03', 6)	# 66-71
    sprite('ryn000_04', 6)	# 72-77
    sprite('ryn000_05', 6)	# 78-83
    sprite('ryn000_06', 6)	# 84-89
    sprite('ryn000_07', 6)	# 90-95
    sprite('ryn000_08', 6)	# 96-101
    sprite('ryn000_09', 6)	# 102-107
    label(1)
    sprite('keep', 1)	# 108-108

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        if SLOT_5:
            Unknown9266(1)
    sprite('keep', 2)	# 1-2
    StartMultihit()
    sprite('ryn202_00', 3)	# 3-5
    teleportRelativeX(100000)
    sprite('ryn202_01', 3)	# 6-8
    sprite('ryn202_02', 3)	# 9-11
    sprite('ryn202_03', 3)	# 12-14
    SFX_0('004_swing_grap_1_2')
    sprite('ryn202_04', 3)	# 15-17	 **attackbox here**
    GFX_0('AddAtkFire', 0)
    Unknown23029(1, 9904, 0)
    sprite('ryn202_05', 4)	# 18-21
    sprite('ryn202_06', 4)	# 22-25
    sprite('ryn202_07', 4)	# 26-29
    sprite('ryn202_08', 4)	# 30-33
    sprite('ryn202_09', 4)	# 34-37
    sprite('ryn202_10', 4)	# 38-41
    sprite('ryn202_11', 4)	# 42-45
    sprite('ryn202_12', 4)	# 46-49
    sprite('ryn202_13', 4)	# 50-53
    sprite('ryn000_00', 6)	# 54-59
    teleportRelativeX(-20000)
    sprite('ryn000_01', 6)	# 60-65
    sprite('ryn000_02', 6)	# 66-71
    sprite('ryn000_03', 6)	# 72-77
    sprite('ryn000_04', 6)	# 78-83
    sprite('ryn000_05', 6)	# 84-89
    sprite('ryn000_06', 6)	# 90-95
    sprite('ryn000_07', 6)	# 96-101
    sprite('ryn000_08', 6)	# 102-107
    sprite('ryn000_09', 6)	# 108-113
    label(1)
    sprite('keep', 1)	# 114-114

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        SLOT_4 = 1
        if SLOT_5:
            Unknown9266(1)
    sprite('ryn406_13', 4)	# 1-4
    sprite('ryn406_14', 4)	# 5-8
    sprite('ryn406_15', 4)	# 9-12
    sprite('ryn406_16', 4)	# 13-16
    SFX_3('rynse_05')
    sprite('ryn406_17', 3)	# 17-19
    tag_voice(0, 'ryn159_0', 'ryn159_1', '', '')
    sprite('ryn406_18', 3)	# 20-22	 **attackbox here**
    GFX_0('rynef406', -1)

    def upon_11():
        GFX_0('vref_ryn406_Hit', -1)
    sprite('ryn406_19', 6)	# 23-28
    sprite('ryn406_20', 6)	# 29-34
    sprite('ryn406_21', 6)	# 35-40
    sprite('ryn406_22', 6)	# 41-46
    sprite('ryn406_23', 6)	# 47-52
    sprite('ryn406_24', 6)	# 53-58
    sprite('ryn406_25', 6)	# 59-64

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        Unknown23027()

        def upon_3():
            if (SLOT_18 == 42):
                RefreshMultihit()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(0)
    sprite('null', 23)	# 1-23
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 24-24
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1000000)
    sprite('ryn404_06', 7)	# 25-31
    physicsXImpulse(40000)
    physicsYImpulse(15000)
    Unknown1043()
    sprite('ryn404_07', 5)	# 32-36
    SFX_0('005_swing_grap_2_2')
    sprite('ryn404_08', 5)	# 37-41
    GFX_0('rynef404', -1)
    sprite('ryn404_09', 3)	# 42-44	 **attackbox here**
    Unknown1019(50)
    sprite('ryn404_10', 3)	# 45-47
    sprite('ryn404_11', 32767)	# 48-32814
    label(0)
    sprite('ryn404_12', 5)	# 32815-32819
    sprite('ryn404_13', 5)	# 32820-32824
    sprite('ryn404_14', 5)	# 32825-32829
    sprite('ryn404_15', 5)	# 32830-32834
    sprite('ryn000_00', 6)	# 32835-32840
    sprite('ryn000_01', 6)	# 32841-32846
    sprite('ryn000_02', 6)	# 32847-32852
    sprite('ryn000_03', 6)	# 32853-32858
    sprite('ryn000_04', 6)	# 32859-32864
    sprite('ryn000_05', 6)	# 32865-32870
    sprite('ryn000_06', 6)	# 32871-32876
    sprite('ryn000_07', 6)	# 32877-32882
    sprite('ryn000_08', 6)	# 32883-32888
    sprite('ryn000_09', 6)	# 32889-32894
    sprite('keep', 1)	# 32895-32895

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        if SLOT_5:
            Unknown9266(1)
    sprite('ryn431_17', 3)	# 1-3
    sprite('ryn431_18', 3)	# 4-6
    physicsXImpulse(5000)
    sprite('ryn431_19', 3)	# 7-9
    Unknown1019(25)
    sprite('ryn431_20', 2)	# 10-11
    Unknown1019(25)
    SFX_0('004_swing_grap_1_2')
    sprite('ryn431_21', 3)	# 12-14	 **attackbox here**
    Unknown1019(0)
    sprite('ryn431_22', 6)	# 15-20
    sprite('ryn431_23', 6)	# 21-26
    sprite('ryn431_24', 6)	# 27-32
    sprite('ryn431_25', 6)	# 33-38
    sprite('ryn431_26', 6)	# 39-44
    sprite('ryn431_27', 6)	# 45-50
    sprite('ryn431_28', 6)	# 51-56
    sprite('ryn000_00', 6)	# 57-62
    sprite('ryn000_01', 6)	# 63-68
    sprite('ryn000_02', 6)	# 69-74
    sprite('ryn000_03', 6)	# 75-80
    sprite('ryn000_04', 6)	# 81-86
    sprite('ryn000_05', 6)	# 87-92
    sprite('ryn000_06', 6)	# 93-98
    sprite('ryn000_07', 6)	# 99-104
    sprite('ryn000_08', 6)	# 105-110
    sprite('ryn000_09', 6)	# 111-116
    sprite('keep', 1)	# 117-117

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
        if SLOT_5:
            Unknown9266(1)
    sprite('ryn406_13', 4)	# 1-4
    sprite('ryn406_14', 4)	# 5-8
    sprite('ryn406_15', 4)	# 9-12
    sprite('ryn406_16', 4)	# 13-16
    SFX_3('rynse_05')
    sprite('ryn406_17', 3)	# 17-19
    sprite('ryn406_18', 3)	# 20-22	 **attackbox here**
    GFX_0('rynef406', -1)

    def upon_11():
        GFX_0('vref_ryn406_Hit', -1)
    sprite('ryn406_19', 6)	# 23-28
    sprite('ryn406_20', 6)	# 29-34
    sprite('ryn406_21', 6)	# 35-40
    sprite('ryn406_22', 6)	# 41-46
    sprite('ryn406_23', 6)	# 47-52
    sprite('ryn406_24', 6)	# 53-58
    sprite('ryn406_25', 6)	# 59-64

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
                Unknown1015(360)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ryn000_00', 3)	# 1-3
    sprite('ryn032_00', 3)	# 4-6
    sprite('ryn032_01', 3)	# 7-9
    sprite('ryn032_02', 3)	# 10-12
    physicsXImpulse(20000)
    sprite('ryn032_03', 3)	# 13-15
    Unknown1019(180)
    sprite('ryn032_04', 3)	# 16-18
    Unknown8006(100, 1, 1)
    sprite('ryn032_05', 3)	# 19-21
    sprite('ryn032_10', 4)	# 22-25
    Unknown1019(50)
    sprite('ryn032_11', 4)	# 26-29
    Unknown1019(50)
    label(1)
    sprite('ryn310_00', 2)	# 30-31
    clearUponHandler(3)
    Unknown1084(1)
    Unknown8010(100, 1, 1)
    sprite('ryn310_01', 1)	# 32-32
    sprite('ryn310_02', 3)	# 33-35	 **attackbox here**
    SFX_0('010_swing_sword_0')
    sprite('ryn310_03', 4)	# 36-39
    SFX_1('ryn155')
    sprite('ryn310_04', 4)	# 40-43
    sprite('ryn310_05', 4)	# 44-47
    sprite('ryn310_06', 4)	# 48-51
    sprite('ryn310_07', 4)	# 52-55
    sprite('ryn310_08', 3)	# 56-58

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(500)
        Unknown11064(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(36)
        Unknown9142(31)
        Hitstop(6)
        PushbackX(0)
        AttackP2(50)
        Unknown11092(1)
        Unknown11080(1)
        Unknown12051(2)
        Unknown2004(1, 0)
    sprite('ryn310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ryn311_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ryn311_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown7009(0)
    SFX_0('003_swing_grap_0_1')
    sprite('ryn311_02', 3)	# 10-12	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ryn311_03', 3)	# 13-15
    sprite('ryn311_04', 3)	# 16-18
    sprite('ryn311_05', 3)	# 19-21
    sprite('ryn311_06', 3)	# 22-24
    Unknown7009(0)
    SFX_0('003_swing_grap_0_1')
    sprite('ryn311_02', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    sprite('ryn311_03', 3)	# 28-30
    sprite('ryn311_07', 3)	# 31-33
    sprite('ryn311_08', 3)	# 34-36
    sprite('ryn201_00', 2)	# 37-38
    sprite('ryn201_01', 2)	# 39-40
    Unknown2017(1)
    physicsXImpulse(20000)
    sprite('ryn201_02', 2)	# 41-42
    Unknown1019(50)
    SFX_1('ryn153')
    SFX_0('004_swing_grap_1_1')
    sprite('ryn201_03', 3)	# 43-45	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1000)
    Unknown11064(0)
    GroundedHitstunAnimation(9)
    Hitstop(12)
    AirUntechableTime(60)
    AirPushbackX(5000)
    AirPushbackY(-50000)
    Unknown9190(1)
    Unknown9118(40)
    Unknown1019(50)
    sprite('ryn201_04', 3)	# 46-48
    Unknown1019(0)
    sprite('ryn201_05', 3)	# 49-51
    sprite('ryn201_06', 3)	# 52-54
    sprite('ryn201_07', 3)	# 55-57
    sprite('ryn201_08', 3)	# 58-60

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
                Unknown1015(360)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ryn000_00', 3)	# 1-3
    sprite('ryn032_00', 3)	# 4-6
    sprite('ryn032_01', 3)	# 7-9
    sprite('ryn032_02', 3)	# 10-12
    physicsXImpulse(20000)
    sprite('ryn032_03', 3)	# 13-15
    Unknown1019(180)
    sprite('ryn032_04', 3)	# 16-18
    Unknown8006(100, 1, 1)
    sprite('ryn032_05', 3)	# 19-21
    sprite('ryn032_10', 4)	# 22-25
    Unknown1019(50)
    sprite('ryn032_11', 4)	# 26-29
    Unknown1019(50)
    label(1)
    sprite('ryn310_00', 2)	# 30-31
    clearUponHandler(3)
    Unknown1084(1)
    Unknown8010(100, 1, 1)
    sprite('ryn310_01', 1)	# 32-32
    sprite('ryn310_02', 3)	# 33-35	 **attackbox here**
    SFX_0('010_swing_sword_0')
    sprite('ryn310_03', 4)	# 36-39
    SFX_1('ryn155')
    sprite('ryn310_04', 4)	# 40-43
    sprite('ryn310_05', 4)	# 44-47
    sprite('ryn310_06', 4)	# 48-51
    sprite('ryn310_07', 4)	# 52-55
    sprite('ryn310_08', 3)	# 56-58

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(3)
        Damage(500)
        Unknown11064(1)
        AirHitstunAnimation(2)
        GroundedHitstunAnimation(2)
        Unknown9130(36)
        Unknown9142(31)
        Hitstop(6)
        PushbackX(0)
        AttackP2(50)
        Unknown11092(1)
        Unknown11080(1)
        Unknown12051(2)
        Unknown2004(1, 0)
    sprite('ryn310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ryn313_00', 3)	# 4-6
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ryn313_01', 3)	# 7-9
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('ryn311_05', 3)	# 10-12
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ryn311_06', 3)	# 13-15
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    Unknown7009(0)
    SFX_0('003_swing_grap_0_1')
    sprite('ryn311_02', 3)	# 16-18	 **attackbox here**
    sprite('ryn311_03', 3)	# 19-21
    sprite('ryn311_04', 3)	# 22-24
    sprite('ryn311_05', 3)	# 25-27
    sprite('ryn311_06', 3)	# 28-30
    Unknown7009(0)
    SFX_0('003_swing_grap_0_1')
    sprite('ryn311_02', 3)	# 31-33	 **attackbox here**
    RefreshMultihit()
    sprite('ryn311_03', 3)	# 34-36
    sprite('ryn311_07', 3)	# 37-39
    sprite('ryn311_08', 3)	# 40-42
    sprite('ryn201_00', 2)	# 43-44
    sprite('ryn201_01', 2)	# 45-46
    Unknown2017(1)
    physicsXImpulse(20000)
    sprite('ryn201_02', 2)	# 47-48
    Unknown1019(50)
    SFX_1('ryn153')
    SFX_0('004_swing_grap_1_1')
    sprite('ryn201_03', 3)	# 49-51	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1000)
    Unknown11064(0)
    GroundedHitstunAnimation(9)
    Hitstop(12)
    AirUntechableTime(60)
    AirPushbackX(5000)
    AirPushbackY(-50000)
    Unknown9190(1)
    Unknown9118(40)
    Unknown1019(50)
    sprite('ryn201_04', 3)	# 52-54
    Unknown1019(0)
    sprite('ryn201_05', 3)	# 55-57
    sprite('ryn201_06', 3)	# 58-60
    sprite('ryn201_07', 3)	# 61-63
    sprite('ryn201_08', 3)	# 64-66

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2200)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(35000)
        Unknown11001(0, 0, 0)
        if SLOT_5:
            Unknown11092(1)
            Unknown9266(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(1)
        SLOT_4 = 1
    sprite('ryn320_00', 4)	# 1-4
    sprite('ryn320_01', 4)	# 5-8
    sprite('ryn320_02', 4)	# 9-12
    tag_voice(1, 'ryn200_0', 'ryn200_1', 'ryn200_2', '')
    physicsXImpulse(5000)
    GFX_1('rynef320_smoke', -1)
    SFX_3('rynse_05')
    sprite('ryn320_03', 3)	# 13-15	 **attackbox here**
    GFX_0('rynef320', -1)
    Unknown1019(200)
    physicsYImpulse(30000)
    Unknown1043()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9909, 0)
    sprite('ryn320_03', 7)	# 16-22	 **attackbox here**
    if SLOT_5:
        RefreshMultihit()
        Unknown10000(50)
    sprite('ryn320_04', 3)	# 23-25
    Unknown1019(75)
    setInvincible(0)
    sprite('ryn320_05', 4)	# 26-29
    sprite('ryn320_06', 4)	# 30-33
    sprite('ryn320_07', 4)	# 34-37
    sprite('ryn320_08', 4)	# 38-41
    sprite('ryn320_09', 3)	# 42-44
    label(0)
    sprite('ryn320_10', 3)	# 45-47
    sprite('ryn320_11', 3)	# 48-50
    gotoLabel(0)
    label(1)
    sprite('ryn320_12', 3)	# 51-53
    sprite('ryn320_13', 3)	# 54-56
    sprite('ryn320_14', 3)	# 57-59
    sprite('ryn320_15', 3)	# 60-62

@State
def CmnActInvincibleAttackAir():

    def upon_IMMEDIATE():
        Unknown17025('')
        AttackLevel_(4)
        Damage(2200)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackX(5000)
        AirPushbackY(35000)
        Unknown11001(0, 0, 0)
        if SLOT_5:
            Unknown11092(1)
            Unknown9266(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            setInvincible(0)
            sendToLabel(1)
        SLOT_4 = 1
    sprite('ryn320_00', 2)	# 1-2
    Unknown1007(50000)
    sprite('ryn320_01', 2)	# 3-4
    Unknown1084(1)
    sprite('ryn320_02', 2)	# 5-6
    tag_voice(1, 'ryn200_0', 'ryn200_1', 'ryn200_2', '')
    SFX_3('rynse_05')
    sprite('ryn320_03', 3)	# 7-9	 **attackbox here**
    GFX_0('rynef320', -1)
    physicsXImpulse(5000)
    physicsYImpulse(30000)
    Unknown1043()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9909, 0)
    sprite('ryn320_03', 3)	# 10-12	 **attackbox here**
    if SLOT_5:
        RefreshMultihit()
        Unknown10000(50)
    sprite('ryn320_04', 3)	# 13-15
    setInvincible(0)
    sprite('ryn320_05', 4)	# 16-19
    sprite('ryn320_06', 4)	# 20-23
    sprite('ryn320_07', 4)	# 24-27
    sprite('ryn320_08', 4)	# 28-31
    sprite('ryn320_09', 3)	# 32-34
    label(0)
    sprite('ryn320_10', 3)	# 35-37
    sprite('ryn320_11', 3)	# 38-40
    gotoLabel(0)
    label(1)
    sprite('ryn320_12', 3)	# 41-43
    sprite('ryn320_13', 3)	# 44-46
    sprite('ryn320_14', 3)	# 47-49
    sprite('ryn320_15', 3)	# 50-52

@State
def LandShotA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ryn400_00', 3)	# 1-3
    sprite('ryn400_01', 3)	# 4-6
    sprite('ryn400_02', 3)	# 7-9
    GFX_0('rynef400_Flare', -1)
    tag_voice(1, 'ryn201_0', 'ryn201_1', 'ryn201_2', '')
    sprite('ryn400_05', 3)	# 10-12
    Unknown21012('72796e65663430305f466c61726500000000000000000000000000000000000020000000')
    SFX_3('rynse_02')
    sprite('ryn400_06', 3)	# 13-15
    GFX_0('LandShotObj', -1)
    Unknown23029(1, 4001, 0)
    SLOT_4 = 1
    GFX_0('rynef400_Muzzle', -1)
    Unknown36(1)
    Unknown1073(27000)
    Unknown35()
    sprite('ryn400_07', 5)	# 16-20
    sprite('ryn400_08', 5)	# 21-25
    sprite('ryn400_09', 4)	# 26-29
    sprite('ryn400_10', 4)	# 30-33
    sprite('ryn400_11', 4)	# 34-37
    sprite('ryn400_12', 4)	# 38-41
    sprite('ryn400_13', 4)	# 42-45

@State
def LandShotB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ryn400_00', 3)	# 1-3
    sprite('ryn400_01', 3)	# 4-6
    sprite('ryn400_02', 3)	# 7-9
    GFX_0('rynef400_Flare', -1)
    sprite('ryn400_03', 3)	# 10-12
    tag_voice(1, 'ryn201_0', 'ryn201_1', 'ryn201_2', '')
    sprite('ryn400_05', 3)	# 13-15
    Unknown21012('72796e65663430305f466c61726500000000000000000000000000000000000020000000')
    SFX_3('rynse_02')
    sprite('ryn400_06', 3)	# 16-18
    GFX_0('LandShotObj', -1)
    Unknown23029(1, 4002, 0)
    SLOT_4 = 1
    GFX_0('rynef400_Muzzle', -1)
    Unknown36(1)
    Unknown1073(17000)
    Unknown35()
    sprite('ryn400_07', 5)	# 19-23
    sprite('ryn400_08', 5)	# 24-28
    sprite('ryn400_09', 4)	# 29-32
    sprite('ryn400_10', 4)	# 33-36
    sprite('ryn400_11', 4)	# 37-40
    sprite('ryn400_12', 4)	# 41-44
    sprite('ryn400_13', 4)	# 45-48

@State
def LandShotC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ryn400_00', 3)	# 1-3
    sprite('ryn400_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ryn400_02', 3)	# 7-9
    GFX_0('rynef400_Flare', -1)
    sprite('ryn400_03', 3)	# 10-12
    sprite('ryn400_04', 3)	# 13-15
    tag_voice(1, 'ryn202_0', 'ryn202_1', 'ryn202_2', '')
    sprite('ryn400_05', 3)	# 16-18
    Unknown21012('72796e65663430305f466c61726500000000000000000000000000000000000020000000')
    SFX_3('rynse_02')
    sprite('ryn400_06', 3)	# 19-21
    GFX_0('LandShotObj', -1)
    Unknown23029(1, 4003, 0)
    SLOT_4 = 1
    GFX_0('rynef400_Muzzle', -1)
    Unknown36(1)
    Unknown1073(17000)
    Unknown35()
    sprite('ryn400_07', 4)	# 22-25
    sprite('ryn400_08', 4)	# 26-29
    sprite('ryn400_09', 4)	# 30-33
    sprite('ryn400_10', 4)	# 34-37
    sprite('ryn400_11', 3)	# 38-40
    sprite('ryn400_12', 3)	# 41-43
    sprite('ryn400_13', 3)	# 44-46

@State
def AssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(80)
        AirPushbackX(15000)
        AirPushbackY(20000)
        AirUntechableTime(24)
        Unknown9154(19)
        Unknown11032('400d0300ffffffffffffffffffffffff')
        HitOrBlockCancel('AddAssaultA')
        HitOrBlockCancel('AddAssaultB')
        HitOrBlockCancel('AddAssaultC')

        def upon_11():
            clearUponHandler(11)
            sendToLabel(1)
            GFX_0('rynef402_Singal02', -1)
        SLOT_4 = 1
    sprite('ryn402_00', 3)	# 1-3
    sprite('ryn402_01', 3)	# 4-6
    tag_voice(1, 'ryn205_0', 'ryn205_1', 'ryn205_2', '')
    sprite('ryn402_02', 4)	# 7-10
    setInvincible(1)
    Unknown22019('0000000001000000000000000100000000000000')
    Unknown22030(0)
    GuardPoint_(1)
    Unknown22035(50)
    if SLOT_5:
        Unknown22035(0)
    Unknown22031(15, -1)
    sprite('ryn402_03', 4)	# 11-14
    sprite('ryn402_04', 3)	# 15-17
    physicsXImpulse(100000)
    GFX_0('rynef402', -1)
    sprite('ryn402_05', 3)	# 18-20	 **attackbox here**
    Unknown1019(75)
    Unknown1017()
    Unknown1022()
    sprite('ryn402_06', 3)	# 21-23	 **attackbox here**
    GFX_0('rynef402_Singal01', -1)
    sprite('ryn402_20', 5)	# 24-28
    clearUponHandler(11)
    setInvincible(0)
    Recovery()
    Unknown1019(20)
    GFX_0('rynef402_Singal02', -1)
    sprite('ryn402_21', 5)	# 29-33
    Unknown1019(40)
    sprite('ryn402_22', 5)	# 34-38
    Unknown1019(40)
    Unknown14077(0)
    sprite('ryn402_23', 5)	# 39-43
    Unknown1019(0)
    sprite('ryn402_24', 5)	# 44-48
    ExitState()
    label(1)
    sprite('ryn402_20', 4)	# 49-52
    setInvincible(0)
    Recovery()
    Unknown1019(50)
    GFX_0('rynef402_Singal02', -1)
    sprite('ryn402_21', 4)	# 53-56
    Unknown1019(50)
    sprite('ryn402_22', 4)	# 57-60
    Unknown1019(50)
    Unknown14077(0)
    sprite('ryn402_23', 4)	# 61-64
    Unknown1019(0)
    sprite('ryn402_24', 4)	# 65-68

@State
def AddAssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(25000)
        AirUntechableTime(30)
        Unknown11108('03000000')
        if SLOT_5:
            Unknown11092(1)
            Unknown9266(1)

            def upon_78():
                clearUponHandler(78)
                Unknown2037(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(3)
        Unknown1018()
        Unknown1023()
        Unknown1019(50)
        Unknown30068(1)
    sprite('ryn402_07', 3)	# 1-3
    sprite('ryn402_08', 3)	# 4-6
    tag_voice(1, 'ryn206_0', 'ryn206_1', 'ryn206_2', '')
    Unknown1019(50)
    sprite('ryn402_09', 3)	# 7-9
    Unknown1019(0)
    GFX_0('rynef402_2nd', -1)
    GFX_1('rynef320_smoke', -1)
    sprite('ryn402_10', 1)	# 10-10	 **attackbox here**
    RefreshMultihit()
    physicsXImpulse(15000)
    physicsYImpulse(22500)
    Unknown1043()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9910, 0)
    sprite('ryn402_10', 1)	# 11-11	 **attackbox here**
    clearUponHandler(78)
    if SLOT_5:
        if SLOT_2:
            RefreshMultihit()
            Unknown10000(50)
            Hitstop(6)
    sprite('ryn402_10', 1)	# 12-12	 **attackbox here**
    if SLOT_5:
        if SLOT_2:
            RefreshMultihit()
    sprite('ryn402_11', 3)	# 13-15
    sprite('ryn402_12', 4)	# 16-19
    sprite('ryn402_13', 4)	# 20-23
    setGravity(1000)
    sprite('ryn402_14', 4)	# 24-27
    Unknown1019(50)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn402_15', 3)	# 28-30	 **attackbox here**
    tag_voice(0, 'ryn207_0', 'ryn207_1', 'ryn207_2', '')
    RefreshMultihit()
    Damage(1700)
    Hitstop(12)
    AirPushbackX(35000)
    AirPushbackY(-5000)
    PushbackX(19800)
    Unknown11058('0100000000000000000000000000000000000000')
    Unknown11092(0)
    Unknown9266(0)
    Unknown1043()

    def upon_11():
        clearUponHandler(11)
        GFX_0('vref_ryn402_Hit', -1)
    sprite('ryn402_16', 3)	# 31-33
    Recovery()
    sprite('ryn402_17', 3)	# 34-36
    sprite('ryn402_18', 3)	# 37-39
    sprite('ryn402_19', 3)	# 40-42
    sprite('ryn020_05', 3)	# 43-45
    sprite('ryn020_06', 3)	# 46-48
    label(2)
    sprite('ryn020_07', 3)	# 49-51
    sprite('ryn020_08', 3)	# 52-54
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ryn010_01', 2)	# 55-56
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ryn010_00', 2)	# 57-58

@State
def AddAssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(2000)
        AttackP1(80)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(15000)
        AirPushbackY(-70000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(35)
        AirUntechableTime(60)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(2)
        Unknown23027()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            Unknown8000(100, 1, 1)
            sendToLabel(0)
        Unknown1018()
        Unknown1023()
        Unknown1019(25)
        Unknown30068(1)
    sprite('ryn404_04', 5)	# 1-5	 **attackbox here**
    tag_voice(1, 'ryn210_0', 'ryn210_1', 'ryn210_2', '')
    sprite('ryn404_05', 3)	# 6-8	 **attackbox here**
    physicsXImpulse(5000)
    physicsYImpulse(16000)
    Unknown1043()
    setInvincible(1)
    Unknown22019('0000000000000000010000000000000000000000')
    sprite('ryn404_06', 8)	# 9-16
    sprite('ryn404_07', 4)	# 17-20
    SFX_0('005_swing_grap_2_2')
    sprite('ryn404_08', 3)	# 21-23
    GFX_0('rynef404', -1)
    sprite('ryn404_09ex01', 3)	# 24-26	 **attackbox here**
    RefreshMultihit()
    sprite('ryn404_10', 3)	# 27-29
    setInvincible(0)
    Recovery()
    sprite('ryn404_11', 32767)	# 30-32796
    label(0)
    sprite('ryn404_12', 6)	# 32797-32802
    setInvincible(0)
    Recovery()
    sprite('ryn404_13', 6)	# 32803-32808
    sprite('ryn404_14', 6)	# 32809-32814
    sprite('ryn404_15', 6)	# 32815-32820

@State
def AddAssaultC():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(500)
        AttackP1(80)
        AttackP2(75)
        Unknown11092(1)
        AirUntechableTime(40)
        Hitstop(1)
        AirPushbackX(-2500)
        Unknown30055('d0fb01001400000014000000')
        AirPushbackY(2000)
        PushbackX(2500)
        Unknown11108('03000000')
        Unknown11091(10)
        Unknown30065(0)
        if SLOT_5:
            Unknown10000(150)
            Unknown9266(1)
        Unknown2004(1, 0)
        Unknown1018()
        Unknown1023()
        Unknown1019(50)
        Unknown30068(1)
    sprite('ryn403_00', 3)	# 1-3
    sprite('ryn403_01', 3)	# 4-6
    tag_voice(1, 'ryn208_0', 'ryn208_1', 'ryn208_2', '')
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ryn403_02', 3)	# 7-9
    Unknown1019(0)
    sprite('ryn403_03', 2)	# 10-11
    SFX_0('004_swing_grap_1_0')
    sprite('ryn403_04', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9911, 0)
    sprite('ryn403_05', 2)	# 14-15
    SFX_0('004_swing_grap_1_0')
    sprite('ryn403_06', 2)	# 16-17	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9911, 0)
    sprite('ryn403_03', 2)	# 18-19
    SFX_0('004_swing_grap_1_0')
    sprite('ryn403_04', 2)	# 20-21	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9911, 0)
    sprite('ryn403_05', 2)	# 22-23
    SFX_0('004_swing_grap_1_0')
    sprite('ryn403_06', 2)	# 24-25	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9911, 0)
    sprite('ryn403_03', 2)	# 26-27
    SFX_0('004_swing_grap_1_0')
    sprite('ryn403_04', 2)	# 28-29	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9911, 0)
    sprite('ryn403_05', 2)	# 30-31
    SFX_0('004_swing_grap_1_0')
    sprite('ryn403_06', 2)	# 32-33	 **attackbox here**
    RefreshMultihit()
    Unknown11028(22)
    GroundedHitstunAnimation(2)
    AirPushbackX(15000)
    AirPushbackY(15000)
    Unknown9130(28)
    Unknown9142(23)
    Unknown30055('000000000000000000000000')
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9912, 0)
    sprite('ryn403_07', 3)	# 34-36
    sprite('ryn403_08', 3)	# 37-39
    sprite('ryn403_09', 3)	# 40-42
    sprite('ryn403_10', 3)	# 43-45
    physicsXImpulse(5000)
    sprite('ryn403_11', 3)	# 46-48
    Unknown1019(1000)
    sprite('ryn403_12', 3)	# 49-51
    Unknown1019(50)
    GFX_0('rynef403', -1)
    Unknown2015(120)
    sprite('ryn403_13', 2)	# 52-53
    Unknown21012('72796e656634303300000000000000000000000000000000000000000000000020000000')
    Unknown1019(50)
    Unknown2015(140)
    sprite('ryn403_14', 3)	# 54-56	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    tag_voice(0, 'ryn209_0', 'ryn209_1', 'ryn209_2', '')
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1500)
    GroundedHitstunAnimation(9)
    Hitstop(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Unknown9215()
    Unknown9202(5)
    Unknown11028(18)
    if SLOT_5:
        Unknown10000(150)
    Unknown1019(50)
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9913, 0)
    Unknown2015(150)

    def upon_11():
        clearUponHandler(11)
        GFX_0('vref_ryn403_Hit', -1)
    sprite('ryn403_15', 3)	# 57-59
    Recovery()
    Unknown1019(50)
    Unknown2015(-1)
    sprite('ryn403_16', 4)	# 60-63
    Unknown1019(0)
    sprite('ryn403_17', 4)	# 64-67
    sprite('ryn403_18', 4)	# 68-71
    sprite('ryn403_19', 3)	# 72-74
    sprite('ryn403_20', 3)	# 75-77
    sprite('ryn403_21', 3)	# 78-80
    sprite('ryn403_22', 3)	# 81-83

@State
def AssaultB():

    def upon_IMMEDIATE():
        Unknown17011('AssaultBExe', 2, 0, 0)
        Unknown11054(120000)
        Unknown11045(1)
        Unknown11002(-1)
        Unknown30061(0)
    sprite('ryn405_00', 4)	# 1-4
    sprite('ryn405_01', 4)	# 5-8
    sprite('ryn405_02', 5)	# 9-13
    sprite('ryn405_03', 5)	# 14-18
    sprite('ryn405_04', 5)	# 19-23
    sprite('ryn405_05', 3)	# 24-26
    Unknown8006(100, 1, 1)
    physicsXImpulse(55000)
    sprite('ryn405_06', 3)	# 27-29
    sprite('ryn405_07', 3)	# 30-32	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1019(50)
    sprite('ryn405_23', 3)	# 33-35
    Unknown1019(50)
    sprite('ryn310_03', 6)	# 36-41
    Unknown1019(25)
    SFX_1('ryn155')
    sprite('ryn310_04', 6)	# 42-47
    Unknown1019(25)
    sprite('ryn310_05', 6)	# 48-53
    Unknown1019(0)
    sprite('ryn310_06', 6)	# 54-59
    sprite('ryn310_07', 6)	# 60-65
    sprite('ryn310_08', 6)	# 66-71

@State
def AssaultBExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(4)
        Damage(3000)
        Unknown11091(5)
        AttackP2(50)
        AirUntechableTime(60)
        AirPushbackY(25000)
        Unknown11108('03000000')
        Unknown11099(1)
        Unknown11072(1, -50000, 350000)
        if SLOT_5:
            Unknown10000(120)
            AirPushbackY(40000)
            Unknown9266(1)

            def upon_12():
                GFX_0('rynef405_Danger', -1)

        def upon_12():
            Unknown23073()
            if SLOT_5:
                GFX_0('rynef405_Danger', -1)
        SLOT_4 = 1
    sprite('ryn405_07', 6)	# 1-6	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    tag_voice(1, 'ryn211_0', 'ryn211_1', 'ryn211_2', '')
    sprite('ryn405_08', 6)	# 7-12
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('ryn405_09', 6)	# 13-18
    Unknown5000(2, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('ryn405_10', 6)	# 19-24
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('ryn405_11', 6)	# 25-30
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('ryn405_12', 12)	# 31-42
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('ryn405_13', 12)	# 43-54
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('ryn405_14', 18)	# 55-72
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    sprite('ryn405_15', 3)	# 73-75	 **attackbox here**
    GFX_0('rynef405', -1)
    Unknown5000(15, 0)
    Unknown5001('0000000001000000010000000000000001000000')
    tag_voice(0, 'ryn212_0', 'ryn212_1', 'ryn212_2', '')
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9914, 0)
    sprite('ryn405_16', 5)	# 76-80
    sprite('ryn405_17', 5)	# 81-85
    sprite('ryn405_18', 5)	# 86-90
    sprite('ryn405_19', 5)	# 91-95
    sprite('ryn405_20', 5)	# 96-100
    sprite('ryn405_21', 5)	# 101-105
    sprite('ryn405_22', 5)	# 106-110

@State
def AssaultC():

    def upon_IMMEDIATE():
        Unknown17011('AssaultCExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(180000)
        Unknown11002(-1)
        Unknown11045(0)
        Unknown11061(1)
        Unknown30061(1)
        AttackP1(80)
        Unknown11091(10)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 == 7):
                Unknown8007(100, 1, 1)
                physicsXImpulse(20000)
            if (SLOT_18 >= 7):
                Unknown1015(360)
                if (SLOT_12 >= 28000):
                    SLOT_12 = 28000
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('ryn000_00', 3)	# 1-3
    sprite('ryn032_00', 3)	# 4-6
    Unknown2037(1)
    Unknown23125('')
    Unknown2058(-5000)
    sprite('ryn032_01', 3)	# 7-9
    sprite('ryn032_02', 3)	# 10-12
    physicsXImpulse(20000)
    sprite('ryn032_03', 3)	# 13-15
    Unknown1019(180)
    sprite('ryn032_04', 3)	# 16-18
    Unknown8006(100, 1, 1)
    sprite('ryn032_05', 3)	# 19-21
    sprite('ryn032_10', 4)	# 22-25
    Unknown1019(50)
    sprite('ryn032_11', 4)	# 26-29
    Unknown1019(50)
    label(1)
    sprite('ryn406_00', 3)	# 30-32
    clearUponHandler(3)
    Unknown1084(1)
    Unknown8010(100, 1, 1)
    if (not SLOT_2):
        Unknown23125('')
        Unknown2058(-5000)
    sprite('ryn406_01', 3)	# 33-35
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ryn406_02', 3)	# 36-38
    sprite('ryn406_03', 3)	# 39-41
    sprite('ryn406_04', 2)	# 42-43
    physicsXImpulse(10000)
    sprite('ryn406_05', 3)	# 44-46	 **attackbox here**
    Unknown1019(50)
    sprite('ryn406_26', 4)	# 47-50
    setInvincible(0)
    Unknown1019(0)
    SFX_1('ryn155')
    sprite('ryn406_27', 4)	# 51-54
    sprite('ryn406_28', 4)	# 55-58
    sprite('ryn406_29', 4)	# 59-62

@State
def AssaultCExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(2)
        Damage(1000)
        Unknown11091(10)
        AttackP2(70)
        Unknown11092(1)
        GroundedHitstunAnimation(9)
        Hitstop(6)
        AirUntechableTime(60)
        AirPushbackY(25000)
        Unknown11064(1)
        Unknown11108('03000000')
        Unknown30065(0)
        Unknown12051(2)
        Unknown14077(0)
        if SLOT_5:
            Unknown10000(120)
            Unknown9266(1)
        Unknown11069('AssaultCExe')
        SLOT_4 = 1
    sprite('ryn406_05', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    tag_voice(1, 'ryn213_0', 'ryn213_1', 'ryn213_2', '')
    sprite('ryn406_06', 3)	# 4-6
    SFX_0('004_swing_grap_1_0')
    sprite('ryn406_07', 2)	# 7-8	 **attackbox here**
    RefreshMultihit()
    Hitstop(1)
    AirPushbackX(3500)
    AirPushbackY(500)
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9915, 0)
    sprite('ryn406_08', 2)	# 9-10
    SFX_0('004_swing_grap_1_0')
    sprite('ryn406_09', 2)	# 11-12	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9915, 0)
    sprite('ryn406_10', 2)	# 13-14
    SFX_0('004_swing_grap_1_0')
    sprite('ryn406_11', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Hitstop(12)
    AirPushbackY(30000)
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9916, 0)
    sprite('ryn406_12', 6)	# 18-23
    sprite('ryn406_13', 6)	# 24-29
    sprite('ryn406_14', 6)	# 30-35
    sprite('ryn406_15', 6)	# 36-41
    sprite('ryn406_16', 6)	# 42-47
    sprite('ryn406_17', 2)	# 48-49
    tag_voice(0, 'ryn214_0', 'ryn214_1', 'ryn214_2', '')
    SFX_3('rynse_05')
    sprite('ryn406_18', 3)	# 50-52	 **attackbox here**
    GFX_0('rynef406', -1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2000)
    Unknown11064(0)
    GroundedHitstunAnimation(9)
    AirPushbackX(24000)
    AirPushbackY(30000)
    Hitstop(15)
    Unknown11069('')
    GFX_0('AddAtkFireSpecial', 0)
    Unknown23029(1, 9917, 0)
    Unknown14077(1)
    if SLOT_5:
        Unknown10000(120)
        GroundedHitstunAnimation(9)
        AirPushbackX(60000)
        AirPushbackY(15000)
        Unknown9178(1)
        WallbounceReboundTime(0)
        AirHitstunAfterWallbounce(40)

    def upon_11():
        GFX_0('vref_ryn406_Hit', -1)
    sprite('ryn406_19', 3)	# 53-55
    sprite('ryn406_20', 3)	# 56-58
    sprite('ryn406_21', 3)	# 59-61
    sprite('ryn406_22', 3)	# 62-64
    sprite('ryn406_23', 2)	# 65-66
    sprite('ryn406_24', 2)	# 67-68
    sprite('ryn406_25', 2)	# 69-70

@State
def AirShotA():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('ryn401_00', 3)	# 1-3
    sprite('ryn401_01', 3)	# 4-6
    physicsYImpulse(12000)
    setGravity(1600)
    tag_voice(1, 'ryn203_0', 'ryn203_1', 'ryn203_2', '')
    Unknown28(2, 'CmnActJumpLanding')
    Unknown22004(12, 1)
    sprite('ryn401_02', 2)	# 7-8
    GFX_0('rynef401_Flare', -1)
    sprite('ryn401_05', 2)	# 9-10
    Unknown21012('72796e65663430315f466c61726500000000000000000000000000000000000020000000')
    SFX_3('rynse_02')
    sprite('ryn401_06', 5)	# 11-15
    GFX_0('rynef401_Muzzle', -1)
    Unknown36(1)
    Unknown1072(47000)
    Unknown35()
    GFX_0('AirShotObj', -1)
    Unknown23029(1, 4011, 0)
    SLOT_4 = 1
    Unknown1019(50)
    sprite('ryn401_07', 5)	# 16-20
    sprite('ryn401_08', 5)	# 21-25
    sprite('ryn401_09', 5)	# 26-30
    sprite('ryn401_10', 5)	# 31-35
    sprite('ryn401_11', 5)	# 36-40
    sprite('ryn401_12', 5)	# 41-45
    sprite('ryn401_13', 5)	# 46-50

@State
def AirShotB():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('ryn401_00', 3)	# 1-3
    sprite('ryn401_01', 3)	# 4-6
    physicsYImpulse(12000)
    setGravity(1600)
    tag_voice(1, 'ryn203_0', 'ryn203_1', 'ryn203_2', '')
    Unknown28(2, 'CmnActJumpLanding')
    Unknown22004(12, 1)
    sprite('ryn401_02', 2)	# 7-8
    GFX_0('rynef401_Flare', -1)
    sprite('ryn401_05', 2)	# 9-10
    Unknown21012('72796e65663430315f466c61726500000000000000000000000000000000000020000000')
    SFX_3('rynse_02')
    sprite('ryn401_06', 5)	# 11-15
    GFX_0('rynef401_Muzzle', -1)
    Unknown36(1)
    Unknown1072(38000)
    Unknown35()
    GFX_0('AirShotObj', -1)
    Unknown23029(1, 4012, 0)
    SLOT_4 = 1
    Unknown1019(50)
    sprite('ryn401_07', 5)	# 16-20
    sprite('ryn401_08', 5)	# 21-25
    sprite('ryn401_09', 5)	# 26-30
    sprite('ryn401_10', 5)	# 31-35
    sprite('ryn401_11', 5)	# 36-40
    sprite('ryn401_12', 5)	# 41-45
    sprite('ryn401_13', 5)	# 46-50

@State
def AirShotC():

    def upon_IMMEDIATE():
        Unknown17003()
        clearUponHandler(2)
    sprite('ryn401_00', 3)	# 1-3
    sprite('ryn401_01', 3)	# 4-6
    physicsYImpulse(12000)
    setGravity(1600)
    Unknown23125('')
    Unknown2058(-5000)
    tag_voice(1, 'ryn204_0', 'ryn204_1', 'ryn204_2', '')
    Unknown28(2, 'CmnActJumpLanding')
    Unknown22004(12, 1)
    sprite('ryn401_02', 3)	# 7-9
    GFX_0('rynef401_Flare', -1)
    sprite('ryn401_05', 3)	# 10-12
    Unknown21012('72796e65663430315f466c61726500000000000000000000000000000000000020000000')
    SFX_3('rynse_02')
    sprite('ryn401_06', 5)	# 13-17
    GFX_0('rynef401_Muzzle', -1)
    Unknown36(1)
    Unknown1072(34000)
    Unknown35()
    GFX_0('AirShotObj', -1)
    Unknown23029(1, 4013, 0)
    SLOT_4 = 1
    sprite('ryn401_07', 5)	# 18-22
    sprite('ryn401_08', 5)	# 23-27
    sprite('ryn401_09', 5)	# 28-32
    sprite('ryn401_10', 5)	# 33-37
    sprite('ryn401_11', 5)	# 38-42
    sprite('ryn401_12', 5)	# 43-47
    sprite('ryn401_13', 5)	# 48-52

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5400)
        Hitstop(20)
        Unknown11091(25)
        setInvincible(1)
        GroundedHitstunAnimation(9)
        Unknown11056(0)
        AirUntechableTime(60)
        AirPushbackX(60000)
        AirPushbackY(35000)
        if SLOT_5:
            Unknown10000(110)
            Unknown9266(1)

        def upon_11():
            ScreenShake(100000, 100000)
            Unknown2037(1)

        def upon_3():
            if SLOT_51:
                if (SLOT_163 < 300000):
                    Unknown1019(50)
        Unknown11050('0200000072796e65663433305f4869744100000000000000000000000000000000000000')
        SLOT_4 = 1
    sprite('ryn430_00', 8)	# 1-8
    tag_voice(1, 'ryn250_0', 'ryn250_1', '', '')
    Unknown2036(53, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('ryn430_01', 8)	# 9-16
    sprite('ryn430_02', 8)	# 17-24
    sprite('ryn430_03', 18)	# 25-42
    sprite('ryn430_04', 6)	# 43-48
    sprite('ryn430_05', 3)	# 49-51
    SFX_3('rynse_12')
    sprite('ryn430_06', 3)	# 52-54
    GFX_0('rynef430', -1)
    physicsXImpulse(40000)
    sprite('ryn430_07', 3)	# 55-57
    Unknown1019(500)
    sprite('ryn430_08', 3)	# 58-60
    Unknown1019(50)
    SLOT_51 = 1
    sprite('ryn430_09', 2)	# 61-62
    Unknown1019(50)
    GFX_0('rynef403', -1)
    sprite('ryn430_10', 2)	# 63-64	 **attackbox here**
    SLOT_51 = 0
    StartMultihit()
    tag_voice(0, 'ryn251_0', 'ryn251_1', '', '')
    GFX_0('rynef430_DashSingal', -1)
    sprite('ryn430_15', 3)	# 65-67	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9918, 0)
    sprite('ryn430_16', 3)	# 68-70
    setInvincible(0)
    physicsXImpulse(10000)
    GFX_0('rynef430_DashEnd', -1)
    label(0)
    sprite('ryn430_17', 3)	# 71-73
    sprite('ryn430_18', 3)	# 74-76
    sprite('ryn430_19', 2)	# 77-78
    sprite('keep', 1)	# 79-79
    if (SLOT_2 > 0):
        Unknown2038(-1)
        sendToLabel(0)
    sprite('ryn430_20', 5)	# 80-84
    Unknown8000(100, 1, 1)
    Unknown1019(25)
    sprite('ryn430_21', 5)	# 85-89
    sprite('ryn430_22', 5)	# 90-94
    Unknown1084(1)
    sprite('ryn430_23', 5)	# 95-99
    sprite('ryn430_24', 5)	# 100-104

@State
def UltimateAssaultSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        setInvincible(1)
        AttackLevel_(5)
        Damage(5400)
        Unknown11091(25)
        Unknown11064(1)
        GroundedHitstunAnimation(9)
        Unknown11001(30, 30, 30)
        Unknown11056(0)
        AirUntechableTime(60)
        AirPushbackX(60000)
        AirPushbackY(35000)
        Unknown11092(1)
        Unknown11069('UltimateAssaultSP')

        def upon_3():
            if SLOT_51:
                if (SLOT_163 < 300000):
                    Unknown1019(50)
        if SLOT_5:
            Unknown10000(110)
            Unknown9266(1)
        if Unknown23145('AssaultBExe'):
            Unknown2006()
        SLOT_4 = 1
    sprite('ryn430_00', 8)	# 1-8
    tag_voice(1, 'ryn250_0', 'ryn250_1', '', '')
    Unknown2036(53, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('ryn430_01', 8)	# 9-16
    sprite('ryn430_02', 8)	# 17-24
    sprite('ryn430_03', 20)	# 25-44
    sprite('ryn430_04', 6)	# 45-50
    sprite('ryn430_05', 3)	# 51-53
    SFX_3('rynse_12')
    sprite('ryn430_06', 3)	# 54-56
    physicsXImpulse(40000)
    GFX_0('rynef430', -1)
    sprite('ryn430_07', 3)	# 57-59
    Unknown1019(500)
    sprite('ryn430_08', 3)	# 60-62
    Unknown1019(50)
    SLOT_51 = 1
    sprite('ryn430_09', 2)	# 63-64
    Unknown1019(50)
    GFX_0('rynef403', -1)
    sprite('ryn430_10', 2)	# 65-66	 **attackbox here**
    GFX_0('rynef430_DashSingal', -1)
    SLOT_51 = 0
    Unknown11050('0200000072796e65665f45584849545f4200000000000000000000000000000000000000')

    def upon_78():
        SFX_3('rynse_13')
        clearUponHandler(78)
        clearUponHandler(80)
        sendToLabel(1)
        GFX_0('rynef430_Flare', -1)

    def upon_80():
        SFX_3('rynse_13')
        clearUponHandler(78)
        clearUponHandler(80)
        sendToLabel(1)
        GFX_0('rynef430_Flare', -1)
    sprite('ryn430_15', 3)	# 67-69	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    Unknown11064(0)
    Hitstop(20)
    Unknown11001(0, 0, 8)
    Unknown11069('')
    clearUponHandler(78)
    clearUponHandler(80)
    tag_voice(0, 'ryn251_0', 'ryn251_1', '', '')
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9918, 0)

    def upon_11():
        ScreenShake(100000, 100000)
        Unknown2037(1)
    label(100)
    sprite('ryn430_16', 3)	# 70-72
    GFX_0('rynef430_DashEnd', -1)
    setInvincible(0)
    physicsXImpulse(10000)
    label(0)
    sprite('ryn430_17', 3)	# 73-75
    sprite('ryn430_18', 3)	# 76-78
    sprite('ryn430_19', 2)	# 79-80
    sprite('keep', 1)	# 81-81
    if (SLOT_2 > 0):
        Unknown2038(-1)
        sendToLabel(0)
    sprite('ryn430_20', 5)	# 82-86
    Unknown8000(100, 1, 1)
    Unknown1019(25)
    sprite('ryn430_21', 5)	# 87-91
    sprite('ryn430_22', 5)	# 92-96
    Unknown1084(1)
    sprite('ryn430_23', 5)	# 97-101
    sprite('ryn430_24', 5)	# 102-106
    ExitState()
    label(1)
    sprite('ryn430_11', 6)	# 107-112
    Unknown1019(10)
    sprite('ryn430_12', 6)	# 113-118
    sprite('ryn430_13', 6)	# 119-124
    GFX_0('rynef430_DashEnd', -1)
    sprite('ryn430_14', 3)	# 125-127
    sprite('ryn430_14', 3)	# 128-130
    tag_voice(0, 'ryn251_0', 'ryn251_1', '', '')
    SFX_3('rynse_05')
    sprite('ryn430_15', 2)	# 131-132	 **attackbox here**
    GFX_0('rynef430_DashSingalB', -1)
    RefreshMultihit()
    AttackLevel_(5)
    Unknown11056(0)
    Damage(2700)
    Unknown11064(0)
    Hitstop(20)
    Unknown11091(10)
    Unknown11001(0, 0, 8)
    Unknown11069('')
    Unknown11050('0200000072796e65663433305f4869744100000000000000000000000000000000000000')
    if SLOT_5:
        Unknown10000(110)

    def upon_11():
        ScreenShake(150000, 150000)
        Unknown2037(1)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9918, 0)
    sprite('keep', 10)	# 133-142
    Unknown1019(1000)
    sendToLabel(100)

@State
def UltimateRush():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(3)
        Damage(1350)
        Unknown11064(1)
        Unknown11091(10)
        AirHitstunAnimation(4)
        Unknown11092(1)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11072(1, 250000, 0)
        PushbackX(1800)
        setInvincible(1)
        Unknown22019('0100000001000000010000000100000000000000')
        Unknown22030(0)
        GuardPoint_(1)
        Unknown22035(50)
        if SLOT_5:
            Unknown22035(0)
        Unknown22031(9, 8)
        Unknown11050('0200000072796e65663433315f4869743031000000000000000000000000000000000000')
        if SLOT_5:
            Unknown10000(110)
            Unknown9266(1)
        Unknown2037(0)

        def upon_12():
            clearUponHandler(12)
            Unknown2037(1)
            Unknown13024(0)
        SLOT_4 = 1
    sprite('ryn431_00', 8)	# 1-8
    tag_voice(1, 'ryn252_0', 'ryn252_1', '', '')
    Unknown2036(82, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('ryn431_01', 8)	# 9-16
    sprite('ryn431_02', 8)	# 17-24
    sprite('ryn431_03', 8)	# 25-32
    sprite('ryn431_04', 8)	# 33-40
    sprite('ryn431_05', 28)	# 41-68
    sprite('ryn431_06', 6)	# 69-74
    sprite('ryn431_07', 6)	# 75-80
    sprite('ryn431_08', 6)	# 81-86
    physicsXImpulse(60000)
    GFX_0('rynef431', -1)
    sprite('ryn431_09', 5)	# 87-91
    Unknown1019(25)
    sprite('ryn431_10', 5)	# 92-96
    Unknown1019(25)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 5)	# 97-101	 **attackbox here**
    Unknown21012('72796e656634333100000000000000000000000000000000000000000000000020000000')
    RefreshMultihit()
    Unknown1019(0)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9919, 0)
    sprite('ryn431_12', 5)	# 102-106
    setInvincible(0)
    tag_voice(0, 'ryn253_0', 'ryn253_1', '', '')
    sprite('ryn431_13', 5)	# 107-111
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 5)	# 112-116	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9919, 0)
    sprite('ryn431_15', 5)	# 117-121
    sprite('ryn431_10', 4)	# 122-125
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 4)	# 126-129	 **attackbox here**
    RefreshMultihit()
    Hitstop(9)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9920, 0)
    sprite('ryn431_12', 4)	# 130-133
    sprite('ryn431_13', 4)	# 134-137
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 4)	# 138-141	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9920, 0)
    sprite('ryn431_15', 4)	# 142-145
    sprite('ryn431_10', 3)	# 146-148
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 3)	# 149-151	 **attackbox here**
    RefreshMultihit()
    Hitstop(6)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9921, 0)
    sprite('ryn431_12', 3)	# 152-154
    sprite('ryn431_13', 3)	# 155-157
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 3)	# 158-160	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9921, 0)
    sprite('ryn431_15', 3)	# 161-163
    sprite('ryn431_10', 3)	# 164-166
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 2)	# 167-168	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Hitstop(11)
    Unknown9215()
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9130(40)
    Unknown9142(30)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9925, 0)
    sprite('keep', 2)	# 169-170
    StartMultihit()
    if SLOT_2:
        sendToLabel(100)
    sprite('keep', 6)	# 171-176
    sprite('ryn431_12', 8)	# 177-184
    sprite('ryn430_23', 8)	# 185-192
    sprite('ryn430_24', 8)	# 193-200
    ExitState()
    label(100)
    sprite('ryn431_16', 5)	# 201-205
    Unknown23024(2)
    sprite('ryn431_17', 5)	# 206-210
    sprite('ryn431_18', 5)	# 211-215
    physicsXImpulse(70000)
    sprite('ryn431_19', 5)	# 216-220
    Unknown1019(25)
    sprite('ryn431_20', 2)	# 221-222
    Unknown1019(25)
    tag_voice(0, 'ryn254_0', 'ryn254_1', '', '')
    SFX_3('rynse_05')
    sprite('ryn431_21', 3)	# 223-225	 **attackbox here**
    Unknown11050('0200000072796e65665f45584849545f4100000000000000000000000000000000000000')
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2500)
    Unknown11064(0)
    Unknown11091(20)
    GroundedHitstunAnimation(9)
    Hitstop(13)
    AirUntechableTime(60)
    AirPushbackX(30000)
    AirPushbackY(-60000)
    Unknown9190(1)
    Unknown9118(55)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Unknown11072(0, 0, 0)
    if SLOT_5:
        Unknown10000(110)
    Unknown1019(0)
    Unknown13024(1)

    def upon_11():
        ScreenShake(100000, 100000)
        GFX_0('rynef431_BG', -1)
        GFX_0('rynef431_Hit_Circle', -1)
        SFX_0('025_cleanhit_grap')
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9928, 0)
    sprite('ryn431_22', 6)	# 226-231
    sprite('ryn431_23', 6)	# 232-237
    sprite('ryn431_24', 6)	# 238-243
    sprite('ryn431_25', 6)	# 244-249
    sprite('ryn431_26', 6)	# 250-255
    sprite('ryn431_27', 6)	# 256-261
    sprite('ryn431_28', 6)	# 262-267

@State
def UltimateRushSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(3)
        Damage(600)
        Unknown11064(1)
        Unknown11091(10)
        AirHitstunAnimation(4)
        Unknown11092(1)
        Unknown11032('40420f0000000000ffffffffffffffff')
        Unknown11072(1, 250000, 0)
        PushbackX(1800)
        setInvincible(1)
        Unknown22019('0100000001000000010000000100000000000000')
        Unknown22030(0)
        GuardPoint_(1)
        Unknown22035(50)
        if SLOT_5:
            Unknown22035(0)
        Unknown22031(9, 8)
        Unknown11050('0200000072796e65663433315f4869743031000000000000000000000000000000000000')
        if SLOT_5:
            Unknown10000(110)
            Unknown9266(1)
        Unknown2037(0)

        def upon_12():
            clearUponHandler(12)
            Unknown2037(1)
            Unknown13024(0)
        if Unknown23145('AssaultBExe'):
            Unknown2006()
        SLOT_4 = 1
    sprite('ryn431_00', 8)	# 1-8
    tag_voice(1, 'ryn252_0', 'ryn252_1', '', '')
    Unknown2036(82, -1, 0)
    Unknown30080('')
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2058(-10000)
    sprite('ryn431_01', 8)	# 9-16
    sprite('ryn431_02', 8)	# 17-24
    sprite('ryn431_03', 8)	# 25-32
    sprite('ryn431_04', 8)	# 33-40
    sprite('ryn431_05', 28)	# 41-68
    sprite('ryn431_06', 6)	# 69-74
    sprite('ryn431_07', 6)	# 75-80
    sprite('ryn431_08', 6)	# 81-86
    physicsXImpulse(60000)
    GFX_0('rynef431OD', -1)
    sprite('ryn431_09', 4)	# 87-90
    Unknown1019(25)
    sprite('ryn431_10', 4)	# 91-94
    Unknown1019(25)
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 4)	# 95-98	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9919, 0)
    Unknown21012('72796e65663433314f440000000000000000000000000000000000000000000020000000')
    sprite('ryn431_12', 4)	# 99-102
    setInvincible(0)
    tag_voice(0, 'ryn253_0', 'ryn253_1', '', '')
    sprite('ryn431_13', 4)	# 103-106
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 4)	# 107-110	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9919, 0)
    sprite('ryn431_15', 4)	# 111-114
    sprite('ryn431_10', 3)	# 115-117
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 3)	# 118-120	 **attackbox here**
    RefreshMultihit()
    Hitstop(9)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9920, 0)
    sprite('ryn431_12', 3)	# 121-123
    sprite('ryn431_13', 3)	# 124-126
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 3)	# 127-129	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9920, 0)
    sprite('ryn431_15', 3)	# 130-132
    sprite('ryn431_10', 2)	# 133-134
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 2)	# 135-136	 **attackbox here**
    RefreshMultihit()
    Hitstop(6)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9921, 0)
    sprite('ryn431_12', 2)	# 137-138
    sprite('ryn431_13', 2)	# 139-140
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 2)	# 141-142	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9921, 0)
    sprite('ryn431_15', 2)	# 143-144
    sprite('ryn431_10', 2)	# 145-146
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 2)	# 147-148	 **attackbox here**
    RefreshMultihit()
    Hitstop(3)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9922, 0)
    sprite('ryn431_12', 2)	# 149-150
    sprite('ryn431_13', 2)	# 151-152
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 2)	# 153-154	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9922, 0)
    sprite('ryn431_15', 2)	# 155-156
    sprite('ryn431_10', 1)	# 157-157
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 1)	# 158-158	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9923, 0)
    sprite('ryn431_12', 1)	# 159-159
    sprite('ryn431_13', 1)	# 160-160
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 1)	# 161-161	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9923, 0)
    sprite('ryn431_15', 1)	# 162-162
    sprite('ryn431_10', 1)	# 163-163
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 1)	# 164-164	 **attackbox here**
    RefreshMultihit()
    Hitstop(1)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9924, 0)
    sprite('ryn431_12', 1)	# 165-165
    sprite('ryn431_13', 1)	# 166-166
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_14', 1)	# 167-167	 **attackbox here**
    RefreshMultihit()
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9924, 0)
    sprite('ryn431_15', 1)	# 168-168
    sprite('ryn431_10', 1)	# 169-169
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 1)	# 170-170	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Hitstop(11)
    AirHitstunAnimation(2)
    GroundedHitstunAnimation(2)
    Unknown9130(40)
    Unknown9142(30)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9924, 0)

    def upon_12():
        clearUponHandler(12)
        Hitstop(1)
    sprite('keep', 2)	# 171-172
    StartMultihit()
    if SLOT_2:
        sendToLabel(100)
    sprite('keep', 7)	# 173-179
    sprite('ryn431_12', 8)	# 180-187
    sprite('ryn430_23', 8)	# 188-195
    sprite('ryn430_24', 8)	# 196-203
    ExitState()
    label(100)
    sprite('ryn402_07', 5)	# 204-208
    physicsXImpulse(20000)
    sprite('ryn402_08', 5)	# 209-213
    Unknown1019(50)
    sprite('ryn402_09', 5)	# 214-218
    Unknown1019(0)
    sprite('ryn402_10', 3)	# 219-221	 **attackbox here**
    Unknown21012('72796e65663433314f440000000000000000000000000000000000000000000021000000')
    GFX_1('rynef320_smoke', -1)
    RefreshMultihit()
    AttackLevel_(4)
    Damage(900)
    Hitstop(12)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirUntechableTime(60)
    AirPushbackY(32500)
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Unknown11072(0, 0, 0)
    if SLOT_5:
        Unknown10000(110)
    physicsXImpulse(5000)
    physicsYImpulse(25000)
    Unknown1043()

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        Unknown8000(100, 1, 1)
        sendToLabel(1)
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9926, 0)
    sprite('ryn402_10', 3)	# 222-224	 **attackbox here**
    RefreshMultihit()
    Hitstop(2)
    if SLOT_5:
        Unknown9266(1)
    sprite('ryn402_10', 3)	# 225-227	 **attackbox here**
    RefreshMultihit()
    sprite('ryn402_10', 3)	# 228-230	 **attackbox here**
    RefreshMultihit()
    sprite('ryn402_10', 3)	# 231-233	 **attackbox here**
    RefreshMultihit()
    sprite('ryn402_10', 3)	# 234-236	 **attackbox here**
    RefreshMultihit()
    sprite('ryn431_29', 3)	# 237-239
    sprite('ryn431_30', 3)	# 240-242
    label(0)
    sprite('ryn320_10', 3)	# 243-245
    sprite('ryn320_11', 3)	# 246-248
    gotoLabel(0)
    label(1)
    sprite('ryn320_12', 3)	# 249-251
    sprite('ryn320_13', 3)	# 252-254
    Unknown23024(2)
    sprite('ryn320_14', 3)	# 255-257
    sprite('ryn431_31', 3)	# 258-260
    sprite('ryn431_32', 3)	# 261-263
    sprite('ryn431_18', 5)	# 264-268
    physicsXImpulse(25000)
    sprite('ryn431_19', 5)	# 269-273
    Unknown1019(25)
    sprite('ryn431_20', 2)	# 274-275
    Unknown1019(25)
    tag_voice(0, 'ryn254_0', 'ryn254_1', '', '')
    SFX_3('rynse_05')
    sprite('ryn431_21', 3)	# 276-278	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(5)
    Damage(3000)
    Unknown11064(0)
    Unknown11091(10)
    GroundedHitstunAnimation(9)
    Hitstop(13)
    AirUntechableTime(60)
    AirPushbackX(30000)
    AirPushbackY(-60000)
    Unknown9190(1)
    Unknown9118(55)
    if SLOT_5:
        Unknown10000(110)
    Unknown1019(0)
    Unknown13024(1)
    Unknown11050('0200000072796e65665f45584849545f4100000000000000000000000000000000000000')

    def upon_11():
        ScreenShake(100000, 100000)
        GFX_0('rynef431_BG', -1)
        GFX_0('rynef431_Hit_Circle', -1)
        SFX_0('025_cleanhit_grap')
    GFX_0('AddAtkFireUltimate', 0)
    Unknown23029(1, 9928, 0)
    sprite('ryn431_22', 6)	# 279-284
    sprite('ryn431_23', 6)	# 285-290
    sprite('ryn431_24', 6)	# 291-296
    sprite('ryn431_25', 6)	# 297-302
    sprite('ryn431_26', 6)	# 303-308
    sprite('ryn431_27', 6)	# 309-314
    sprite('ryn431_28', 6)	# 315-320

@State
def DangerMode():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown2036(98, -1, 0)
        Unknown30080('')
        Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
        setInvincible(1)
        Unknown20000(1)
        Unknown20009(800)
        Unknown20003(1)
        SLOT_6 = 1
    sprite('ryn333_00', 6)	# 1-6
    sprite('ryn333_01', 15)	# 7-21
    Unknown23024(2)
    sprite('ryn333_02', 2)	# 22-23
    SFX_3('rynse_10')
    sprite('ryn333_03', 3)	# 24-26
    GFX_0('rynef_OD_Begin', -1)
    SLOT_5 = 1
    callSubroutine('CheckSembalnceActivate')
    sprite('ryn333_04', 3)	# 27-29
    sprite('ryn333_05', 3)	# 30-32
    sprite('ryn450_00', 6)	# 33-38
    sprite('ryn450_01', 6)	# 39-44
    sprite('ryn450_02', 6)	# 45-50
    sprite('ryn450_03', 12)	# 51-62
    sprite('ryn450_04', 3)	# 63-65
    GFX_0('rynef450_Aura', -1)
    Unknown20000(0)
    Unknown20003(0)
    SFX_3('rynse_11')
    sprite('ryn450_05', 3)	# 66-68
    sprite('ryn450_06', 3)	# 69-71
    sprite('ryn450_07', 3)	# 72-74
    sprite('ryn450_05', 3)	# 75-77
    sprite('ryn450_06', 3)	# 78-80
    sprite('ryn450_07', 3)	# 81-83
    sprite('ryn450_05', 3)	# 84-86
    sprite('ryn333_06', 6)	# 87-92
    sprite('ryn333_07', 6)	# 93-98

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        AttackLevel_(4)
        Damage(0)
        Unknown11056(0)
        AirUntechableTime(60)
        Unknown9154(60)
        AirHitstunAnimation(4)
        GroundedHitstunAnimation(4)
        Unknown11072(1, 200000, 0)
        Unknown11067(1)
        loopRelated(17, 70)

        def upon_17():
            sendToLabel(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            ScreenShake(0, 50000)
            sendToLabel(2)
            Unknown21012('72796e65663435305f317374000000000000000000000000000000000000000020000000')

        def upon_78():
            clearUponHandler(78)
            Unknown23088(1, 1)
            enterState('AstralHeatExe')
            Unknown11069('AstralHeatExe')
            Unknown20000(1)
            Unknown20003(1)
            Unknown21012('72796e65663435305f317374000000000000000000000000000000000000000021000000')
    sprite('ryn450_00', 6)	# 1-6
    tag_voice(1, 'ryn290_0', 'ryn290_1', '', '')
    setInvincible(1)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown2036(83, -1, 2)
    Unknown23147()
    sprite('ryn450_01', 6)	# 7-12
    sprite('ryn450_02', 6)	# 13-18
    sprite('ryn450_03', 12)	# 19-30
    sprite('ryn450_04', 3)	# 31-33
    GFX_0('rynef450_Aura', -1)
    SFX_3('rynse_11')
    label(0)
    sprite('ryn450_05', 3)	# 34-36
    sprite('ryn450_06', 3)	# 37-39
    sprite('ryn450_07', 3)	# 40-42
    gotoLabel(0)
    label(1)
    sprite('ryn450_08', 3)	# 43-45
    physicsXImpulse(5000)
    physicsYImpulse(40000)
    setGravity(2500)
    sprite('ryn450_09', 5)	# 46-50
    YAccel(50)
    sprite('ryn450_10', 5)	# 51-55
    YAccel(50)
    GFX_0('rynef450_1st', -1)
    sprite('ryn450_11', 5)	# 56-60
    sprite('ryn450_12', 30)	# 61-90
    label(2)
    sprite('ryn450_13', 3)	# 91-93	 **attackbox here**
    SFX_0('213_bound_1')
    sprite('ryn450_13', 3)	# 94-96	 **attackbox here**
    StartMultihit()
    sprite('ryn450_14', 6)	# 97-102
    setInvincible(0)
    sprite('ryn450_15', 15)	# 103-117
    sprite('ryn450_33', 6)	# 118-123
    sprite('ryn450_34', 6)	# 124-129
    sprite('ryn450_35', 6)	# 130-135

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23157(0)
        Unknown23084(1)
        Unknown20002(1)
        Unknown20003(1)
        Unknown20004(1)
        AttackLevel_(3)
        Unknown11056(0)
        Unknown11064(1)
        Unknown11091(100)
        AirUntechableTime(120)
        Unknown9154(120)
        Unknown9310(1)
        AirPushbackX(15000)
        Unknown11072(1, 200000, 0)
        Unknown11067(1)
        Unknown11023(1)
        setInvincible(1)
        Unknown2034(0)
        Unknown2053(0)
        loopRelated(17, 480)

        def upon_17():
            sendToLabel(2)
    sprite('ryn450_14', 5)	# 1-5
    GFX_0('AstralFirstCamera', -1)
    Unknown38(11, 1)
    GFX_0('rynef450_AuraLoop', -1)
    sprite('ryn450_15', 5)	# 6-10
    sprite('ryn450_16', 5)	# 11-15
    physicsXImpulse(5000)
    sprite('ryn402_05', 3)	# 16-18	 **attackbox here**
    StartMultihit()
    Unknown1019(1000)
    sprite('ryn402_06', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    sprite('ryn402_07', 2)	# 22-23
    Unknown1019(50)
    sprite('ryn402_08', 2)	# 24-25
    Unknown1019(50)
    GFX_0('rynef402_2nd', -1)
    sprite('ryn402_09', 2)	# 26-27
    sprite('ryn402_10', 3)	# 28-30	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    GroundedHitstunAnimation(9)
    physicsYImpulse(15000)
    Unknown1043()
    sprite('ryn252_00', 2)	# 31-32
    teleportRelativeX(50000)
    Unknown1007(100000)
    sprite('ryn252_01', 2)	# 33-34
    setGravity(800)
    sprite('ryn252_02', 2)	# 35-36
    sprite('ryn252_03', 2)	# 37-38
    SFX_0('004_swing_grap_1_1')
    sprite('ryn252_04', 3)	# 39-41	 **attackbox here**
    GFX_0('rynef450_RushHit01', -1)
    RefreshMultihit()
    AirPushbackY(-60000)
    Unknown9190(1)
    Unknown9118(25)
    Unknown1043()
    sprite('ryn252_05', 3)	# 42-44
    sprite('ryn252_06', 3)	# 45-47
    sprite('ryn252_07', 3)	# 48-50
    sprite('ryn252_08', 3)	# 51-53
    sprite('ryn431_08', 3)	# 54-56
    Unknown1019(50)
    sprite('ryn431_09', 3)	# 57-59
    sprite('ryn431_10', 3)	# 60-62
    tag_voice(0, 'ryn291_0', 'ryn291_1', '', '')
    SFX_0('004_swing_grap_1_1')
    sprite('ryn431_11', 3)	# 63-65	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(5000)
    Hitstop(3)
    GFX_0('rynef450_431bake', -1)
    sprite('ryn431_12', 3)	# 66-68
    sprite('ryn431_13', 3)	# 69-71
    sprite('ryn431_14', 3)	# 72-74	 **attackbox here**
    RefreshMultihit()
    sprite('ryn431_15', 3)	# 75-77
    sprite('ryn403_11', 3)	# 78-80
    sprite('ryn403_12', 3)	# 81-83
    SFX_0('004_swing_grap_1_1')
    sprite('ryn403_13', 3)	# 84-86
    sprite('ryn403_14', 3)	# 87-89	 **attackbox here**
    GFX_0('rynef450_RushHit02', -1)
    RefreshMultihit()
    Hitstop(12)
    AirPushbackX(50000)
    AirPushbackY(15000)
    sprite('ryn403_15', 3)	# 90-92
    sprite('ryn403_16', 3)	# 93-95
    sprite('ryn430_05', 3)	# 96-98
    SFX_3('rynse_12')
    sprite('ryn430_06', 3)	# 99-101
    GFX_0('rynef450_Dash', -1)
    Unknown1019(500)
    sprite('ryn430_07', 3)	# 102-104
    Unknown1019(500)
    sprite('ryn430_08', 3)	# 105-107
    Unknown1019(50)
    sprite('ryn430_09', 2)	# 108-109
    Unknown1019(50)
    SFX_0('005_swing_grap_2_1')
    sprite('ryn430_10', 2)	# 110-111	 **attackbox here**
    Unknown1019(50)
    StartMultihit()
    sprite('ryn430_15', 3)	# 112-114	 **attackbox here**
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(25000)
    Unknown1019(50)
    Unknown21012('72796e65663435305f547261696c00000000000000000000000000000000000021000000')
    Unknown21012('72796e65663435305f4461736857696e6400000000000000000000000000000021000000')
    SFX_0('025_cleanhit_grap')
    sprite('ryn430_16', 3)	# 115-117
    Unknown1019(50)
    sprite('ryn430_17', 3)	# 118-120
    sprite('ryn320_00', 2)	# 121-122
    teleportRelativeX(50000)
    sprite('ryn320_01', 2)	# 123-124
    sprite('ryn320_02', 2)	# 125-126
    Unknown23029(11, 4501, 0)
    Unknown20000(1)
    GFX_1('rynef320_smoke', -1)
    SFX_3('rynse_05')
    sprite('ryn320_03', 6)	# 127-132	 **attackbox here**
    GFX_0('rynef320', -1)
    RefreshMultihit()
    AirPushbackX(10000)
    AirPushbackY(60000)
    AirUntechableTime(600)
    Unknown11072(0, 0, 0)
    Unknown1019(25)
    physicsYImpulse(20000)
    Unknown1043()
    sprite('ryn320_04', 3)	# 133-135
    sprite('ryn320_05', 3)	# 136-138
    sprite('ryn320_06', 3)	# 139-141
    sprite('ryn320_07', 3)	# 142-144
    sprite('ryn320_08', 3)	# 145-147
    sprite('ryn320_09', 3)	# 148-150
    sprite('ryn320_10', 3)	# 151-153
    sprite('ryn320_12', 2)	# 154-155
    SFX_3('rynse_06')
    sprite('ryn320_13', 2)	# 156-157
    sprite('ryn320_14', 2)	# 158-159
    SFX_3('rynse_04')
    sprite('ryn010_00', 3)	# 160-162
    Unknown36(22)
    Unknown1019(10)
    YAccel(10)
    setGravity(10)
    Unknown35()
    sprite('ryn020_00', 5)	# 163-167
    tag_voice(0, 'ryn292_0', 'ryn292_1', '', '')
    physicsXImpulse(12500)
    physicsYImpulse(180000)
    GFX_0('rynef450_3rd', -1)
    Unknown1043()
    Unknown20001(1)
    Unknown23024(3)
    sprite('ryn020_01', 5)	# 168-172
    sprite('ryn450_17', 5)	# 173-177
    YAccel(50)
    SFX_3('rynse_05')
    sprite('ryn450_18', 5)	# 178-182
    YAccel(50)
    Unknown20001(0)
    sprite('ryn450_19', 5)	# 183-187
    sprite('ryn450_20', 5)	# 188-192
    sprite('ryn450_21', 6)	# 193-198
    Unknown1019(50)
    YAccel(50)
    setGravity(100)
    Unknown21012('72796e65663435305f337264000000000000000000000000000000000000000020000000')
    sprite('ryn450_22', 8)	# 199-206
    Unknown1019(50)
    YAccel(50)
    sprite('ryn450_23', 8)	# 207-214
    sprite('ryn450_24', 8)	# 215-222
    sprite('ryn450_25', 6)	# 223-228
    SFX_3('rynse_14')
    sprite('ryn450_26', 3)	# 229-231
    SFX_3('rynse_15')
    sprite('ryn450_27', 3)	# 232-234
    Unknown20001(1)
    physicsYImpulse(-10000)
    Unknown1043()
    sprite('ryn450_28', 6)	# 235-240	 **attackbox here**
    Unknown21012('72796e65663435305f337264000000000000000000000000000000000000000021000000')
    StartMultihit()
    tag_voice(0, 'ryn293_0', 'ryn293_1', '', '')
    YAccel(500)
    Hitstop(0)
    AirPushbackY(-110000)

    def upon_LANDING():
        clearUponHandler(2)
        Unknown1084(1)
        sendToLabel(0)
        Unknown21012('72796e65663435305f337264000000000000000000000000000000000000000022000000')
        ScreenShake(0, 50000)
    sprite('ryn450_28ex1', 6)	# 241-246	 **attackbox here**
    StartMultihit()
    sprite('ryn450_28ex2', 3)	# 247-249	 **attackbox here**
    StartMultihit()
    sprite('ryn450_28ex2', 30)	# 250-279	 **attackbox here**
    RefreshMultihit()
    label(0)
    sprite('ryn450_29', 1)	# 280-280
    Unknown20001(0)
    GFX_0('AstralAtkFinal', -1)
    ScreenShake(5000, 5000)
    SFX_3('rynse_16')
    sprite('ryn450_29', 2)	# 281-282
    Unknown3029(1)
    Unknown3072('80000000ff000000ff000000ff000000')
    Unknown3073('00000000ff000000ff000000ff000000')
    Unknown3070(3)
    sprite('ryn450_30', 12)	# 283-294
    ScreenShake(0, 3000)
    sprite('ryn450_31', 12)	# 295-306
    ScreenShake(0, 2000)
    SFX_3('rynse_17')
    sprite('ryn450_32', 12)	# 307-318
    ScreenShake(0, 3000)
    label(1)
    sprite('ryn450_30', 12)	# 319-330
    ScreenShake(0, 3000)
    sprite('ryn450_31', 12)	# 331-342
    ScreenShake(0, 2000)
    sprite('ryn450_32', 12)	# 343-354
    ScreenShake(0, 3000)
    gotoLabel(1)
    label(2)
    sprite('ryn450_30', 12)	# 355-366
    sprite('ryn450_31', 12)	# 367-378
    sprite('ryn450_32', 12)	# 379-390
    sprite('ryn450_30', 12)	# 391-402
    sprite('ryn450_31', 12)	# 403-414
    sprite('keep', 3)	# 415-417
    GFX_0('rynef450_End', -1)
    Unknown1000(260000)
    Unknown20000(1)
    Unknown20001(1)
    Unknown20006(1)
    Unknown20003(1)
    Unknown20004(1)

@Subroutine
def MouthTableInit():
    Unknown18011('ryn000', 12643, 12338, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn500', 12643, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn501', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24885, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn502', 12643, 14177, 12643, 24880, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn503', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn504', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 12337, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24885, 25399, 12337, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn520', 13667, 24885, 25399, 12849, 13921, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn521', 12643, 14177, 14179, 12641, 25397, 14130, 14177, 14179, 12641, 25392, 24886, 25398, 24886, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn522', 12643, 14177, 14179, 12897, 25397, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn523', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 12338, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn524', 12643, 14177, 12899, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn525', 12643, 14177, 12643, 24880, 25399, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn402_0', 12643, 14177, 12643, 24882, 25399, 24887, 25399, 12849, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn402_1', 12643, 12641, 25397, 13618, 13665, 13667, 13665, 12643, 24882, 25397, 24885, 25397, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn403_0', 12643, 13153, 25392, 12340, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn403_1', 12643, 12897, 25392, 12340, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn600baz', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn600btg', 12643, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 12849, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn600pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 14133, 12641, 25392, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn600pla', 12643, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn600rrb', 12643, 12897, 25392, 24887, 25399, 24887, 13617, 12643, 24882, 25399, 24887, 25399, 24887, 13361, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601bno', 12643, 12641, 25397, 24887, 25399, 14129, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601pce', 12643, 12897, 25392, 12343, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601pka', 12643, 12641, 25397, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24880, 25399, 24887, 12337, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601pyo', 12643, 12897, 25392, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601rbl', 12643, 14177, 14179, 12641, 25392, 24887, 25399, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601rwi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24880, 12337, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601uca', 12643, 12897, 25392, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 14130, 14177, 14179, 14177, 12643, 24885, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24880, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn601uwa', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24882, 25399, 24887, 25399, 13618, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn603', 12643, 14177, 12643, 24880, 25399, 12850, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn607', 12643, 12641, 25397, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700bno', 12643, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 12337, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700btg', 12643, 13665, 13667, 12641, 25397, 12339, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700pce', 12643, 13153, 25397, 12339, 14177, 14179, 14177, 12643, 24885, 25399, 24887, 12337, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700pla', 12643, 13665, 25392, 24887, 25399, 24887, 12338, 13411, 24887, 25399, 24887, 12337, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700rrb', 12643, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 12338, 14179, 12897, 25392, 12339, 13153, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700rwi', 12643, 14177, 14179, 12641, 25397, 12337, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25397, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn700uca', 12643, 12897, 25392, 24887, 12338, 12899, 24887, 25399, 24887, 25399, 24888, 25399, 24887, 12338, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn701baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 24887, 12849, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn701pak', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn701pka', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn701rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 12897, 25392, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn701umi', 12643, 12641, 25397, 12340, 14177, 14179, 14177, 12643, 24880, 25399, 24887, 25399, 24887, 13617, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('ryn701uwa', 12643, 12897, 25392, 24887, 25399, 24887, 25399, 24889, 12338, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12338, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('btg')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('rrb')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('bno')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('pce')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('pka')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('rwi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('uwa')
    if SLOT_0:
        _gotolabel(190)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(200)
    PartnerChar('pla')
    if SLOT_0:
        _gotolabel(210)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(220)
    PartnerChar('pak')
    if SLOT_0:
        _gotolabel(230)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('ryn600_00', 6)	# 2-7
    sprite('ryn600_01', 6)	# 8-13
    sprite('ryn600_02', 6)	# 14-19
    Unknown7006('ryn500', 100, 896432498, 12592, 0, 0, 100, 896432498, 13360, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ryn600_03', 6)	# 20-25
    sprite('ryn600_04', 6)	# 26-31
    sprite('ryn600_05', 6)	# 32-37
    sprite('ryn600_06', 6)	# 38-43
    sprite('ryn600_07', 10)	# 44-53
    sprite('ryn600_08', 4)	# 54-57
    SFX_3('rynse_01')
    sprite('ryn600_09', 6)	# 58-63
    sprite('ryn600_10', 6)	# 64-69
    sprite('ryn600_11', 6)	# 70-75
    sprite('ryn600_12', 6)	# 76-81
    Unknown23018(1)
    label(1)
    sprite('ryn000_00', 6)	# 82-87
    sprite('ryn000_01', 6)	# 88-93
    sprite('ryn000_02', 6)	# 94-99
    sprite('ryn000_03', 6)	# 100-105
    sprite('ryn000_04', 6)	# 106-111
    sprite('ryn000_05', 6)	# 112-117
    sprite('ryn000_06', 6)	# 118-123
    sprite('ryn000_07', 6)	# 124-129
    sprite('ryn000_08', 6)	# 130-135
    sprite('ryn000_09', 6)	# 136-141
    loopRest()
    gotoLabel(1)
    ExitState()
    label(10)
    sprite('ryn601_00', 6)	# 142-147
    sprite('ryn601_01', 6)	# 148-153
    Unknown7006('ryn502', 100, 896432498, 13104, 0, 0, 100, 896432498, 13616, 0, 0, 100, 0, 0, 0, 0, 0)
    sprite('ryn601_02', 15)	# 154-168
    sprite('ryn601_03', 6)	# 169-174
    sprite('ryn601_04', 6)	# 175-180
    sprite('ryn601_05', 6)	# 181-186
    sprite('ryn601_06', 6)	# 187-192
    sprite('ryn601_07', 6)	# 193-198
    sprite('ryn601_08', 6)	# 199-204
    sprite('ryn601_09', 15)	# 205-219
    sprite('ryn601_10', 6)	# 220-225
    sprite('ryn601_11', 6)	# 226-231
    Unknown23018(1)
    label(11)
    sprite('ryn000_00', 6)	# 232-237
    sprite('ryn000_01', 6)	# 238-243
    sprite('ryn000_02', 6)	# 244-249
    sprite('ryn000_03', 6)	# 250-255
    sprite('ryn000_04', 6)	# 256-261
    sprite('ryn000_05', 6)	# 262-267
    sprite('ryn000_06', 6)	# 268-273
    sprite('ryn000_07', 6)	# 274-279
    sprite('ryn000_08', 6)	# 280-285
    sprite('ryn000_09', 6)	# 286-291
    loopRest()
    gotoLabel(11)
    ExitState()
    label(20)
    sprite('ryn300_00', 7)	# 292-298
    sprite('ryn300_01', 7)	# 299-305
    sprite('ryn300_02', 7)	# 306-312
    sprite('ryn300_03', 7)	# 313-319
    label(21)
    sprite('ryn300_04', 7)	# 320-326
    sprite('ryn300_05', 7)	# 327-333
    sprite('ryn300_04', 7)	# 334-340
    sprite('ryn300_03', 7)	# 341-347
    gotoLabel(21)
    ExitState()
    label(991)
    sprite('ryn000_00', 1)	# 348-348
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ryn000_00', 6)	# 349-354
    sprite('ryn000_01', 6)	# 355-360
    sprite('ryn000_02', 6)	# 361-366
    sprite('ryn000_03', 6)	# 367-372
    sprite('ryn000_04', 6)	# 373-378
    sprite('ryn000_05', 6)	# 379-384
    sprite('ryn000_06', 6)	# 385-390
    sprite('ryn000_07', 6)	# 391-396
    sprite('ryn000_08', 6)	# 397-402
    sprite('ryn000_09', 6)	# 403-408
    loopRest()
    gotoLabel(992)
    label(993)
    sprite('ryn033_00', 2)	# 409-410

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
    sprite('ryn033_01', 2)	# 411-412
    label(994)
    sprite('ryn033_02', 3)	# 413-415
    sprite('ryn033_01', 3)	# 416-418
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 419-421
    ExitState()
    label(100)
    sprite('ryn601_00', 6)	# 422-427
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ryn601_01', 6)	# 428-433
    SFX_1('ryn600baz')
    sprite('ryn601_02', 15)	# 434-448
    sprite('ryn601_03', 6)	# 449-454
    sprite('ryn601_04', 6)	# 455-460
    sprite('ryn601_05', 6)	# 461-466
    sprite('ryn601_06', 6)	# 467-472
    sprite('ryn601_07', 6)	# 473-478
    sprite('ryn601_08', 6)	# 479-484
    sprite('ryn601_09', 15)	# 485-499
    sprite('ryn601_10', 6)	# 500-505
    sprite('ryn601_11', 6)	# 506-511
    Unknown2037(1)
    label(101)
    sprite('ryn000_00', 6)	# 512-517
    sprite('ryn000_01', 6)	# 518-523
    sprite('ryn000_02', 6)	# 524-529
    sprite('ryn000_03', 6)	# 530-535
    sprite('ryn000_04', 6)	# 536-541
    if (not SLOT_2):
        Unknown21007(24, 40)
        Unknown21011(180)
    sprite('ryn000_05', 6)	# 542-547
    sprite('ryn000_06', 6)	# 548-553
    sprite('ryn000_07', 6)	# 554-559
    sprite('ryn000_08', 6)	# 560-565
    sprite('ryn000_09', 6)	# 566-571
    Unknown2038(-1)
    gotoLabel(101)
    ExitState()
    label(110)
    sprite('ryn600_00', 6)	# 572-577
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ryn600_01', 6)	# 578-583
    sprite('ryn600_02', 6)	# 584-589
    SFX_1('ryn600btg')
    sprite('ryn600_03', 6)	# 590-595
    sprite('ryn600_04', 6)	# 596-601
    sprite('ryn600_05', 6)	# 602-607
    sprite('ryn600_06', 6)	# 608-613
    sprite('ryn600_07', 10)	# 614-623
    sprite('ryn600_08', 4)	# 624-627
    SFX_3('rynse_01')
    sprite('ryn600_09', 6)	# 628-633
    sprite('ryn600_10', 6)	# 634-639
    sprite('ryn600_11', 6)	# 640-645
    sprite('ryn600_12', 6)	# 646-651
    Unknown23018(1)
    Unknown2037(2)
    label(111)
    sprite('ryn000_00', 6)	# 652-657
    sprite('ryn000_01', 6)	# 658-663
    sprite('ryn000_02', 6)	# 664-669
    sprite('ryn000_03', 6)	# 670-675
    sprite('ryn000_04', 6)	# 676-681
    sprite('ryn000_05', 6)	# 682-687
    sprite('ryn000_06', 6)	# 688-693
    sprite('ryn000_07', 6)	# 694-699
    sprite('ryn000_08', 6)	# 700-705
    sprite('ryn000_09', 6)	# 706-711
    Unknown2038(-1)
    loopRest()
    if SLOT_2:
        _gotolabel(111)
    sprite('ryn000_00', 1)	# 712-712
    Unknown21007(24, 40)
    Unknown21011(270)
    label(112)
    sprite('ryn000_00', 6)	# 713-718
    sprite('ryn000_01', 6)	# 719-724
    sprite('ryn000_02', 6)	# 725-730
    sprite('ryn000_03', 6)	# 731-736
    sprite('ryn000_04', 6)	# 737-742
    sprite('ryn000_05', 6)	# 743-748
    sprite('ryn000_06', 6)	# 749-754
    sprite('ryn000_07', 6)	# 755-760
    sprite('ryn000_08', 6)	# 761-766
    sprite('ryn000_09', 6)	# 767-772
    loopRest()
    gotoLabel(112)
    ExitState()
    label(120)
    sprite('ryn601_00', 6)	# 773-778
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('ryn601_01', 6)	# 779-784
    SFX_1('ryn600rrb')
    sprite('ryn601_02', 15)	# 785-799
    sprite('ryn601_03', 6)	# 800-805
    sprite('ryn601_04', 6)	# 806-811
    sprite('ryn601_05', 6)	# 812-817
    sprite('ryn601_06', 6)	# 818-823
    sprite('ryn601_07', 6)	# 824-829
    sprite('ryn601_08', 6)	# 830-835
    sprite('ryn601_09', 15)	# 836-850
    sprite('ryn601_10', 6)	# 851-856
    sprite('ryn601_11', 6)	# 857-862
    Unknown2037(1)
    Unknown21011(280)
    label(121)
    sprite('ryn000_00', 6)	# 863-868
    sprite('ryn000_01', 6)	# 869-874
    sprite('ryn000_02', 6)	# 875-880
    sprite('ryn000_03', 6)	# 881-886
    sprite('ryn000_04', 6)	# 887-892
    sprite('ryn000_05', 6)	# 893-898
    sprite('ryn000_06', 6)	# 899-904
    sprite('ryn000_07', 6)	# 905-910
    Unknown21007(24, 40)
    sprite('ryn000_08', 6)	# 911-916
    sprite('ryn000_09', 6)	# 917-922
    gotoLabel(121)
    ExitState()
    label(130)
    sprite('ryn000_00', 1)	# 923-923
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ryn000_00', 6)	# 924-929
    sprite('ryn000_01', 6)	# 930-935
    sprite('ryn000_02', 6)	# 936-941
    sprite('ryn000_03', 6)	# 942-947
    sprite('ryn000_04', 6)	# 948-953
    sprite('ryn000_05', 6)	# 954-959
    sprite('ryn000_06', 6)	# 960-965
    sprite('ryn000_07', 6)	# 966-971
    sprite('ryn000_08', 6)	# 972-977
    sprite('ryn000_09', 6)	# 978-983
    loopRest()
    gotoLabel(131)
    label(132)
    sprite('ryn001_00', 4)	# 984-987
    SFX_1('ryn601bno')
    sprite('ryn001_01', 4)	# 988-991
    sprite('ryn001_02', 4)	# 992-995
    sprite('ryn001_03', 4)	# 996-999
    SFX_3('rynse_00')
    sprite('ryn001_04', 4)	# 1000-1003
    sprite('ryn001_05', 8)	# 1004-1011
    sprite('ryn001_06', 6)	# 1012-1017
    sprite('ryn001_07', 6)	# 1018-1023
    GFX_1('rynef_case', 0)
    SFX_3('rynse_01')
    sprite('ryn001_08', 6)	# 1024-1029
    sprite('ryn001_09', 6)	# 1030-1035
    sprite('ryn001_10', 8)	# 1036-1043
    sprite('ryn001_11', 5)	# 1044-1048
    Unknown23018(1)
    label(133)
    sprite('ryn000_00', 6)	# 1049-1054
    sprite('ryn000_01', 6)	# 1055-1060
    sprite('ryn000_02', 6)	# 1061-1066
    sprite('ryn000_03', 6)	# 1067-1072
    sprite('ryn000_04', 6)	# 1073-1078
    sprite('ryn000_05', 6)	# 1079-1084
    sprite('ryn000_06', 6)	# 1085-1090
    sprite('ryn000_07', 6)	# 1091-1096
    sprite('ryn000_08', 6)	# 1097-1102
    sprite('ryn000_09', 6)	# 1103-1108
    loopRest()
    gotoLabel(133)
    ExitState()
    label(140)
    sprite('ryn000_00', 1)	# 1109-1109
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('ryn000_00', 6)	# 1110-1115
    sprite('ryn000_01', 6)	# 1116-1121
    sprite('ryn000_02', 6)	# 1122-1127
    sprite('ryn000_03', 6)	# 1128-1133
    sprite('ryn000_04', 6)	# 1134-1139
    sprite('ryn000_05', 6)	# 1140-1145
    sprite('ryn000_06', 6)	# 1146-1151
    sprite('ryn000_07', 6)	# 1152-1157
    sprite('ryn000_08', 6)	# 1158-1163
    sprite('ryn000_09', 6)	# 1164-1169
    loopRest()
    gotoLabel(141)
    label(142)
    sprite('ryn601_11', 6)	# 1170-1175
    SFX_1('ryn601pce')
    sprite('ryn601_05', 6)	# 1176-1181
    sprite('ryn601_04', 6)	# 1182-1187
    sprite('ryn601_03', 6)	# 1188-1193
    sprite('ryn601_01', 6)	# 1194-1199
    sprite('ryn601_02', 15)	# 1200-1214
    sprite('ryn601_03', 6)	# 1215-1220
    sprite('ryn601_04', 6)	# 1221-1226
    sprite('ryn601_05', 6)	# 1227-1232
    sprite('ryn601_06', 6)	# 1233-1238
    sprite('ryn601_07', 6)	# 1239-1244
    sprite('ryn601_08', 6)	# 1245-1250
    sprite('ryn601_09', 15)	# 1251-1265
    sprite('ryn601_10', 6)	# 1266-1271
    sprite('ryn601_11', 6)	# 1272-1277
    Unknown23018(1)
    label(143)
    sprite('ryn000_00', 6)	# 1278-1283
    sprite('ryn000_01', 6)	# 1284-1289
    sprite('ryn000_02', 6)	# 1290-1295
    sprite('ryn000_03', 6)	# 1296-1301
    sprite('ryn000_04', 6)	# 1302-1307
    sprite('ryn000_05', 6)	# 1308-1313
    sprite('ryn000_06', 6)	# 1314-1319
    sprite('ryn000_07', 6)	# 1320-1325
    sprite('ryn000_08', 6)	# 1326-1331
    sprite('ryn000_09', 6)	# 1332-1337
    loopRest()
    gotoLabel(143)
    ExitState()
    label(150)
    sprite('ryn000_00', 1)	# 1338-1338
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1485000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ryn000_00', 6)	# 1339-1344
    sprite('ryn000_01', 6)	# 1345-1350
    sprite('ryn000_02', 6)	# 1351-1356
    sprite('ryn000_03', 6)	# 1357-1362
    sprite('ryn000_04', 6)	# 1363-1368
    sprite('ryn000_05', 6)	# 1369-1374
    sprite('ryn000_06', 6)	# 1375-1380
    sprite('ryn000_07', 6)	# 1381-1386
    sprite('ryn000_08', 6)	# 1387-1392
    sprite('ryn000_09', 6)	# 1393-1398
    loopRest()
    gotoLabel(151)
    label(152)
    sprite('ryn300_00', 6)	# 1399-1404
    SFX_1('ryn601pka')
    sprite('ryn300_01', 6)	# 1405-1410
    sprite('ryn300_02', 6)	# 1411-1416
    sprite('ryn300_06', 6)	# 1417-1422
    sprite('ryn300_07', 6)	# 1423-1428
    label(153)
    sprite('ryn300_08', 1)	# 1429-1429
    if SLOT_97:
        _gotolabel(153)
    sprite('ryn300_08', 30)	# 1430-1459
    sprite('ryn300_09', 6)	# 1460-1465
    sprite('ryn300_10', 6)	# 1466-1471
    Unknown23018(1)
    label(154)
    sprite('ryn000_00', 6)	# 1472-1477
    sprite('ryn000_01', 6)	# 1478-1483
    sprite('ryn000_02', 6)	# 1484-1489
    sprite('ryn000_03', 6)	# 1490-1495
    sprite('ryn000_04', 6)	# 1496-1501
    sprite('ryn000_05', 6)	# 1502-1507
    sprite('ryn000_06', 6)	# 1508-1513
    sprite('ryn000_07', 6)	# 1514-1519
    sprite('ryn000_08', 6)	# 1520-1525
    sprite('ryn000_09', 6)	# 1526-1531
    loopRest()
    gotoLabel(154)
    ExitState()
    label(160)
    sprite('ryn000_00', 1)	# 1532-1532
    if SLOT_158:
        Unknown1000(-1465000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ryn000_00', 6)	# 1533-1538
    sprite('ryn000_01', 6)	# 1539-1544
    sprite('ryn000_02', 6)	# 1545-1550
    sprite('ryn000_03', 6)	# 1551-1556
    sprite('ryn000_04', 6)	# 1557-1562
    sprite('ryn000_05', 6)	# 1563-1568
    sprite('ryn000_06', 6)	# 1569-1574
    sprite('ryn000_07', 6)	# 1575-1580
    sprite('ryn000_08', 6)	# 1581-1586
    sprite('ryn000_09', 6)	# 1587-1592
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('ryn300_00', 6)	# 1593-1598
    SFX_1('ryn601pyo')
    sprite('ryn300_01', 6)	# 1599-1604
    sprite('ryn300_02', 6)	# 1605-1610
    label(163)
    sprite('ryn300_03', 1)	# 1611-1611
    if SLOT_97:
        _gotolabel(163)
    sprite('ryn300_03', 20)	# 1612-1631
    sprite('ryn300_02', 6)	# 1632-1637
    sprite('ryn300_01', 6)	# 1638-1643
    sprite('ryn300_00', 6)	# 1644-1649
    Unknown23018(1)
    label(164)
    sprite('ryn000_00', 6)	# 1650-1655
    sprite('ryn000_01', 6)	# 1656-1661
    sprite('ryn000_02', 6)	# 1662-1667
    sprite('ryn000_03', 6)	# 1668-1673
    sprite('ryn000_04', 6)	# 1674-1679
    sprite('ryn000_05', 6)	# 1680-1685
    sprite('ryn000_06', 6)	# 1686-1691
    sprite('ryn000_07', 6)	# 1692-1697
    sprite('ryn000_08', 6)	# 1698-1703
    sprite('ryn000_09', 6)	# 1704-1709
    loopRest()
    gotoLabel(164)
    ExitState()
    label(170)
    sprite('ryn000_00', 1)	# 1710-1710
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ryn000_00', 6)	# 1711-1716
    sprite('ryn000_01', 6)	# 1717-1722
    sprite('ryn000_02', 6)	# 1723-1728
    sprite('ryn000_03', 6)	# 1729-1734
    sprite('ryn000_04', 6)	# 1735-1740
    sprite('ryn000_05', 6)	# 1741-1746
    sprite('ryn000_06', 6)	# 1747-1752
    sprite('ryn000_07', 6)	# 1753-1758
    sprite('ryn000_08', 6)	# 1759-1764
    sprite('ryn000_09', 6)	# 1765-1770
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('ryn001_00', 4)	# 1771-1774
    sprite('ryn001_01', 4)	# 1775-1778
    SFX_1('ryn601rbl')
    sprite('ryn001_02', 4)	# 1779-1782
    sprite('ryn001_03', 4)	# 1783-1786
    SFX_3('rynse_00')
    sprite('ryn001_04', 4)	# 1787-1790
    sprite('ryn001_05', 8)	# 1791-1798
    sprite('ryn001_06', 6)	# 1799-1804
    sprite('ryn001_07', 6)	# 1805-1810
    GFX_1('rynef_case', 0)
    SFX_3('rynse_01')
    sprite('ryn001_08', 6)	# 1811-1816
    label(173)
    sprite('ryn001_09', 1)	# 1817-1817
    if SLOT_97:
        _gotolabel(173)
    sprite('ryn001_09', 20)	# 1818-1837
    sprite('ryn001_10', 8)	# 1838-1845
    sprite('ryn001_11', 5)	# 1846-1850
    Unknown23018(1)
    label(174)
    sprite('ryn000_00', 6)	# 1851-1856
    sprite('ryn000_01', 6)	# 1857-1862
    sprite('ryn000_02', 6)	# 1863-1868
    sprite('ryn000_03', 6)	# 1869-1874
    sprite('ryn000_04', 6)	# 1875-1880
    sprite('ryn000_05', 6)	# 1881-1886
    sprite('ryn000_06', 6)	# 1887-1892
    sprite('ryn000_07', 6)	# 1893-1898
    sprite('ryn000_08', 6)	# 1899-1904
    sprite('ryn000_09', 6)	# 1905-1910
    loopRest()
    gotoLabel(174)
    ExitState()
    label(180)
    sprite('ryn000_00', 1)	# 1911-1911
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ryn000_00', 6)	# 1912-1917
    sprite('ryn000_01', 6)	# 1918-1923
    sprite('ryn000_02', 6)	# 1924-1929
    sprite('ryn000_03', 6)	# 1930-1935
    sprite('ryn000_04', 6)	# 1936-1941
    sprite('ryn000_05', 6)	# 1942-1947
    sprite('ryn000_06', 6)	# 1948-1953
    sprite('ryn000_07', 6)	# 1954-1959
    sprite('ryn000_08', 6)	# 1960-1965
    sprite('ryn000_09', 6)	# 1966-1971
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('ryn001_00', 4)	# 1972-1975
    sprite('ryn001_01', 4)	# 1976-1979
    SFX_1('ryn601rwi')
    sprite('ryn001_02', 4)	# 1980-1983
    sprite('ryn001_03', 4)	# 1984-1987
    SFX_3('rynse_00')
    sprite('ryn001_04', 4)	# 1988-1991
    sprite('ryn001_05', 8)	# 1992-1999
    sprite('ryn001_06', 6)	# 2000-2005
    sprite('ryn001_07', 6)	# 2006-2011
    GFX_1('rynef_case', 0)
    SFX_3('rynse_01')
    sprite('ryn001_08', 6)	# 2012-2017
    label(183)
    sprite('ryn001_09', 1)	# 2018-2018
    if SLOT_97:
        _gotolabel(183)
    sprite('ryn001_09', 20)	# 2019-2038
    sprite('ryn001_10', 8)	# 2039-2046
    sprite('ryn001_11', 5)	# 2047-2051
    Unknown23018(1)
    label(184)
    sprite('ryn000_00', 6)	# 2052-2057
    sprite('ryn000_01', 6)	# 2058-2063
    sprite('ryn000_02', 6)	# 2064-2069
    sprite('ryn000_03', 6)	# 2070-2075
    sprite('ryn000_04', 6)	# 2076-2081
    sprite('ryn000_05', 6)	# 2082-2087
    sprite('ryn000_06', 6)	# 2088-2093
    sprite('ryn000_07', 6)	# 2094-2099
    sprite('ryn000_08', 6)	# 2100-2105
    sprite('ryn000_09', 6)	# 2106-2111
    loopRest()
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('ryn000_00', 1)	# 2112-2112
    if SLOT_158:
        Unknown1000(-1200000)
    else:
        Unknown1000(-1495000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ryn000_00', 6)	# 2113-2118
    sprite('ryn000_01', 6)	# 2119-2124
    sprite('ryn000_02', 6)	# 2125-2130
    sprite('ryn000_03', 6)	# 2131-2136
    sprite('ryn000_04', 6)	# 2137-2142
    sprite('ryn000_05', 6)	# 2143-2148
    sprite('ryn000_06', 6)	# 2149-2154
    sprite('ryn000_07', 6)	# 2155-2160
    sprite('ryn000_08', 6)	# 2161-2166
    sprite('ryn000_09', 6)	# 2167-2172
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('ryn601_11', 6)	# 2173-2178
    SFX_1('ryn601uwa')
    sprite('ryn601_05', 6)	# 2179-2184
    sprite('ryn601_04', 6)	# 2185-2190
    sprite('ryn601_03', 6)	# 2191-2196
    sprite('ryn601_01', 6)	# 2197-2202
    sprite('ryn601_02', 15)	# 2203-2217
    sprite('ryn601_03', 6)	# 2218-2223
    sprite('ryn601_04', 6)	# 2224-2229
    sprite('ryn601_05', 6)	# 2230-2235
    sprite('ryn601_06', 6)	# 2236-2241
    sprite('ryn601_07', 6)	# 2242-2247
    sprite('ryn601_08', 6)	# 2248-2253
    sprite('ryn601_09', 15)	# 2254-2268
    sprite('ryn601_10', 6)	# 2269-2274
    sprite('ryn601_11', 6)	# 2275-2280
    Unknown23018(1)
    label(193)
    sprite('ryn000_00', 6)	# 2281-2286
    sprite('ryn000_01', 6)	# 2287-2292
    sprite('ryn000_02', 6)	# 2293-2298
    sprite('ryn000_03', 6)	# 2299-2304
    sprite('ryn000_04', 6)	# 2305-2310
    sprite('ryn000_05', 6)	# 2311-2316
    sprite('ryn000_06', 6)	# 2317-2322
    sprite('ryn000_07', 6)	# 2323-2328
    sprite('ryn000_08', 6)	# 2329-2334
    sprite('ryn000_09', 6)	# 2335-2340
    loopRest()
    gotoLabel(193)
    ExitState()
    label(200)
    sprite('ryn000_00', 1)	# 2341-2341
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ryn000_00', 6)	# 2342-2347
    sprite('ryn000_01', 6)	# 2348-2353
    sprite('ryn000_02', 6)	# 2354-2359
    sprite('ryn000_03', 6)	# 2360-2365
    sprite('ryn000_04', 6)	# 2366-2371
    sprite('ryn000_05', 6)	# 2372-2377
    sprite('ryn000_06', 6)	# 2378-2383
    sprite('ryn000_07', 6)	# 2384-2389
    sprite('ryn000_08', 6)	# 2390-2395
    sprite('ryn000_09', 6)	# 2396-2401
    loopRest()
    gotoLabel(201)
    label(202)
    sprite('ryn300_00', 6)	# 2402-2407
    SFX_1('ryn601uca')
    sprite('ryn300_01', 6)	# 2408-2413
    sprite('ryn300_02', 6)	# 2414-2419
    label(203)
    sprite('ryn300_03', 1)	# 2420-2420
    if SLOT_97:
        _gotolabel(203)
    sprite('ryn300_03', 20)	# 2421-2440
    sprite('ryn300_02', 6)	# 2441-2446
    sprite('ryn300_01', 6)	# 2447-2452
    sprite('ryn300_00', 6)	# 2453-2458
    Unknown23018(1)
    label(204)
    sprite('ryn000_00', 6)	# 2459-2464
    sprite('ryn000_01', 6)	# 2465-2470
    sprite('ryn000_02', 6)	# 2471-2476
    sprite('ryn000_03', 6)	# 2477-2482
    sprite('ryn000_04', 6)	# 2483-2488
    sprite('ryn000_05', 6)	# 2489-2494
    sprite('ryn000_06', 6)	# 2495-2500
    sprite('ryn000_07', 6)	# 2501-2506
    sprite('ryn000_08', 6)	# 2507-2512
    sprite('ryn000_09', 6)	# 2513-2518
    loopRest()
    gotoLabel(204)
    ExitState()
    label(210)
    sprite('ryn600_00', 6)	# 2519-2524
    sprite('ryn600_01', 6)	# 2525-2530
    sprite('ryn600_02', 6)	# 2531-2536
    SFX_1('ryn600pla')
    sprite('ryn600_03', 6)	# 2537-2542
    sprite('ryn600_04', 6)	# 2543-2548
    sprite('ryn600_05', 6)	# 2549-2554
    sprite('ryn600_06', 6)	# 2555-2560
    sprite('ryn600_07', 10)	# 2561-2570
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('ryn600_08', 4)	# 2571-2574
    SFX_3('rynse_01')
    sprite('ryn600_09', 6)	# 2575-2580
    sprite('ryn600_10', 6)	# 2581-2586
    sprite('ryn600_11', 6)	# 2587-2592
    sprite('ryn600_12', 6)	# 2593-2598
    label(211)
    sprite('ryn000_00', 6)	# 2599-2604
    sprite('ryn000_01', 6)	# 2605-2610
    sprite('ryn000_02', 6)	# 2611-2616
    sprite('ryn000_03', 6)	# 2617-2622
    sprite('ryn000_04', 6)	# 2623-2628
    sprite('ryn000_05', 6)	# 2629-2634
    sprite('ryn000_06', 6)	# 2635-2640
    sprite('ryn000_07', 6)	# 2641-2646
    sprite('ryn000_08', 6)	# 2647-2652
    sprite('ryn000_09', 6)	# 2653-2658
    loopRest()
    gotoLabel(211)
    ExitState()
    label(220)
    sprite('ryn000_00', 1)	# 2659-2659
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('ryn000_00', 6)	# 2660-2665
    sprite('ryn000_01', 6)	# 2666-2671
    sprite('ryn000_02', 6)	# 2672-2677
    sprite('ryn000_03', 6)	# 2678-2683
    sprite('ryn000_04', 6)	# 2684-2689
    sprite('ryn000_05', 6)	# 2690-2695
    sprite('ryn000_06', 6)	# 2696-2701
    sprite('ryn000_07', 6)	# 2702-2707
    sprite('ryn000_08', 6)	# 2708-2713
    sprite('ryn000_09', 6)	# 2714-2719
    loopRest()
    gotoLabel(221)
    label(222)
    sprite('ryn601_11', 6)	# 2720-2725
    SFX_1('ryn601umi')
    sprite('ryn601_05', 6)	# 2726-2731
    sprite('ryn601_04', 6)	# 2732-2737
    sprite('ryn601_03', 6)	# 2738-2743
    sprite('ryn601_01', 6)	# 2744-2749
    sprite('ryn601_02', 15)	# 2750-2764
    sprite('ryn601_03', 6)	# 2765-2770
    sprite('ryn601_04', 6)	# 2771-2776
    sprite('ryn601_05', 6)	# 2777-2782
    sprite('ryn601_06', 6)	# 2783-2788
    sprite('ryn601_07', 6)	# 2789-2794
    sprite('ryn601_08', 6)	# 2795-2800
    sprite('ryn601_09', 15)	# 2801-2815
    sprite('ryn601_10', 6)	# 2816-2821
    sprite('ryn601_11', 6)	# 2822-2827
    Unknown23018(1)
    label(223)
    sprite('ryn000_00', 6)	# 2828-2833
    sprite('ryn000_01', 6)	# 2834-2839
    sprite('ryn000_02', 6)	# 2840-2845
    sprite('ryn000_03', 6)	# 2846-2851
    sprite('ryn000_04', 6)	# 2852-2857
    sprite('ryn000_05', 6)	# 2858-2863
    sprite('ryn000_06', 6)	# 2864-2869
    sprite('ryn000_07', 6)	# 2870-2875
    sprite('ryn000_08', 6)	# 2876-2881
    sprite('ryn000_09', 6)	# 2882-2887
    loopRest()
    gotoLabel(223)
    ExitState()
    label(230)
    sprite('ryn000_00', 1)	# 2888-2888
    if SLOT_158:
        Unknown1000(-1230000)
        Unknown2005()
    else:
        Unknown1000(-1465000)
    sprite('ryn000_00', 6)	# 2889-2894
    SFX_1('ryn600pak')
    sprite('ryn000_01', 6)	# 2895-2900
    sprite('ryn000_02', 6)	# 2901-2906
    sprite('ryn000_03', 6)	# 2907-2912
    sprite('ryn000_04', 6)	# 2913-2918
    sprite('ryn000_05', 6)	# 2919-2924
    sprite('ryn000_06', 6)	# 2925-2930
    sprite('ryn000_07', 6)	# 2931-2936
    sprite('ryn000_08', 6)	# 2937-2942
    sprite('ryn000_09', 6)	# 2943-2948
    sprite('ryn000_00', 6)	# 2949-2954
    sprite('ryn000_01', 6)	# 2955-2960
    sprite('ryn000_02', 6)	# 2961-2966
    sprite('ryn300_00', 6)	# 2967-2972
    sprite('ryn300_01', 6)	# 2973-2978
    sprite('ryn300_02', 6)	# 2979-2984
    sprite('ryn300_06', 6)	# 2985-2990
    sprite('ryn300_07', 6)	# 2991-2996
    label(231)
    sprite('ryn300_08', 1)	# 2997-2997
    if SLOT_97:
        _gotolabel(231)
    sprite('ryn300_08', 30)	# 2998-3027
    sprite('ryn300_08', 32767)	# 3028-35794
    Unknown21007(24, 40)
    Unknown21011(320)
    ExitState()
    label(1000)
    sprite('ryn649_01', 32767)	# 35795-68561
    Unknown2019(1000)
    Unknown1000(-200000)
    if (not SLOT_158):
        Unknown1000(-350000)

    def upon_43():
        if (SLOT_48 == 8002):
            clearUponHandler(43)
            sendToLabel(1001)
    label(1001)
    sprite('ryn649_00', 6)	# 68562-68567
    sprite('ryn300_03', 1)	# 68568-68568
    SFX_1('ryn603')
    Unknown2037(2)
    label(1002)
    sprite('ryn300_03', 6)	# 68569-68574
    sprite('ryn300_04', 6)	# 68575-68580
    sprite('ryn300_05', 10)	# 68581-68590
    sprite('ryn300_04', 6)	# 68591-68596
    sprite('ryn300_03', 10)	# 68597-68606
    sprite('ryn300_04', 6)	# 68607-68612
    if (not SLOT_2):
        Unknown23029(24, 8003, 0)
        Unknown23029(22, 8003, 0)
        Unknown23029(23, 8003, 0)
    sprite('ryn300_05', 10)	# 68613-68622
    sprite('ryn300_04', 6)	# 68623-68628
    sprite('ryn300_03', 10)	# 68629-68638
    Unknown2038(-1)
    if SLOT_97:
        _gotolabel(1002)
    sprite('ryn649_00', 6)	# 68639-68644
    sprite('ryn649_01', 6)	# 68645-68650

    def upon_43():
        if (SLOT_48 == 8004):
            clearUponHandler(43)
            SFX_1('ryn607')
            Unknown23018(1)
        if (SLOT_48 == 8007):
            sendToLabel(1005)
    label(1004)
    sprite('ryn649_01', 1)	# 68651-68651
    gotoLabel(1004)
    label(1005)
    sprite('ryn300_02', 6)	# 68652-68657
    sprite('ryn300_01', 6)	# 68658-68663
    sprite('ryn300_00', 6)	# 68664-68669
    sprite('ryn000_00', 6)	# 68670-68675
    sprite('ryn001_00', 4)	# 68676-68679
    sprite('ryn001_01', 4)	# 68680-68683
    sprite('ryn001_02', 4)	# 68684-68687
    sprite('ryn001_03', 4)	# 68688-68691
    SFX_3('rynse_00')
    sprite('ryn001_04', 4)	# 68692-68695
    sprite('ryn001_05', 8)	# 68696-68703
    sprite('ryn001_06', 6)	# 68704-68709
    sprite('ryn001_07', 6)	# 68710-68715
    GFX_1('rynef_case', 0)
    SFX_3('rynse_01')
    sprite('ryn001_08', 6)	# 68716-68721
    sprite('ryn001_09', 6)	# 68722-68727
    sprite('ryn001_10', 8)	# 68728-68735
    sprite('ryn001_11', 5)	# 68736-68740
    label(1006)
    sprite('ryn000_00', 6)	# 68741-68746
    sprite('ryn000_01', 6)	# 68747-68752
    sprite('ryn000_02', 6)	# 68753-68758
    sprite('ryn000_03', 6)	# 68759-68764
    sprite('ryn000_04', 6)	# 68765-68770
    sprite('ryn000_05', 6)	# 68771-68776
    sprite('ryn000_06', 6)	# 68777-68782
    sprite('ryn000_07', 6)	# 68783-68788
    sprite('ryn000_08', 6)	# 68789-68794
    sprite('ryn000_09', 6)	# 68795-68800
    loopRest()
    gotoLabel(1006)
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
            if PartnerChar('bno'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('rwi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pka'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    label(0)
    sprite('ryn610_00', 6)	# 4-9
    sprite('ryn610_01', 6)	# 10-15
    sprite('ryn610_02', 8)	# 16-23
    sprite('ryn610_03', 8)	# 24-31
    sprite('ryn610_04', 4)	# 32-35
    sprite('ryn610_05', 6)	# 36-41
    if SLOT_158:
        if SLOT_52:
            Unknown7006('ryn525', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('ryn402_0', 100, 879655282, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('ryn520', 100, 896432498, 12594, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ryn610_07', 32767)	# 42-32808
    label(10)
    sprite('ryn611_00', 4)	# 32809-32812
    sprite('ryn611_01', 4)	# 32813-32816
    sprite('ryn611_02', 2)	# 32817-32818
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_03', 4)	# 32819-32822
    sprite('ryn611_04', 4)	# 32823-32826
    sprite('ryn611_05', 4)	# 32827-32830
    sprite('ryn611_06', 2)	# 32831-32832
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_07', 6)	# 32833-32838
    sprite('ryn611_08', 6)	# 32839-32844
    sprite('ryn611_09', 6)	# 32845-32850
    sprite('ryn611_10', 12)	# 32851-32862
    sprite('ryn611_11', 6)	# 32863-32868
    SFX_0('100_hit_grap_1')
    sprite('ryn611_12', 6)	# 32869-32874
    if SLOT_158:
        if SLOT_52:
            Unknown7006('ryn524', 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('ryn402_0', 100, 879655282, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('ryn522', 100, 896432498, 13106, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('ryn611_13', 32767)	# 32875-65641
    label(100)
    sprite('ryn300_00', 6)	# 65642-65647
    SFX_1('ryn700bno')
    sprite('ryn300_01', 6)	# 65648-65653
    sprite('ryn300_02', 6)	# 65654-65659
    label(101)
    sprite('ryn300_03', 1)	# 65660-65660
    if SLOT_97:
        _gotolabel(101)
    sprite('ryn300_03', 20)	# 65661-65680
    sprite('ryn300_03', 32767)	# 65681-98447
    Unknown21007(24, 40)
    Unknown21011(180)
    label(110)
    sprite('ryn610_00', 6)	# 98448-98453
    sprite('ryn610_01', 6)	# 98454-98459
    sprite('ryn610_02', 8)	# 98460-98467
    sprite('ryn610_03', 8)	# 98468-98475
    sprite('ryn610_04', 4)	# 98476-98479
    sprite('ryn610_05', 6)	# 98480-98485
    SFX_1('ryn700btg')
    label(111)
    sprite('ryn610_07', 1)	# 98486-98486
    if SLOT_97:
        _gotolabel(111)
    sprite('ryn610_07', 30)	# 98487-98516
    sprite('ryn610_07', 32767)	# 98517-131283
    Unknown21007(24, 40)
    Unknown21011(270)
    label(120)
    sprite('ryn610_00', 6)	# 131284-131289
    sprite('ryn610_01', 6)	# 131290-131295
    sprite('ryn610_02', 8)	# 131296-131303
    sprite('ryn610_03', 8)	# 131304-131311
    sprite('ryn610_04', 4)	# 131312-131315
    sprite('ryn610_05', 6)	# 131316-131321
    SFX_1('ryn700pce')
    sprite('ryn610_07', 90)	# 131322-131411
    sprite('ryn610_07', 32767)	# 131412-164178
    Unknown2034(0)
    Unknown2053(0)
    Unknown21007(24, 40)
    Unknown21011(150)
    label(130)
    sprite('ryn300_00', 6)	# 164179-164184
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
    SFX_1('ryn700pyo')
    sprite('ryn300_01', 6)	# 164185-164190
    sprite('ryn300_02', 6)	# 164191-164196
    label(131)
    sprite('ryn300_03', 1)	# 164197-164197
    if SLOT_97:
        _gotolabel(131)
    sprite('ryn300_03', 32767)	# 164198-196964
    Unknown21007(24, 40)
    Unknown21011(200)
    label(140)
    sprite('ryn610_00', 6)	# 196965-196970
    sprite('ryn610_01', 6)	# 196971-196976
    sprite('ryn610_02', 8)	# 196977-196984
    sprite('ryn610_03', 8)	# 196985-196992
    sprite('ryn610_04', 4)	# 196993-196996
    sprite('ryn610_05', 6)	# 196997-197002
    SFX_1('ryn700rrb')
    label(141)
    sprite('ryn610_07', 1)	# 197003-197003
    if SLOT_97:
        _gotolabel(141)
    sprite('ryn610_07', 30)	# 197004-197033
    sprite('ryn610_07', 32767)	# 197034-229800
    Unknown21007(24, 40)
    Unknown21011(270)
    label(150)
    sprite('ryn300_00', 6)	# 229801-229806
    SFX_1('ryn700rwi')
    sprite('ryn300_01', 6)	# 229807-229812
    sprite('ryn300_02', 6)	# 229813-229818
    sprite('ryn300_06', 6)	# 229819-229824
    sprite('ryn300_07', 6)	# 229825-229830
    label(151)
    sprite('ryn300_08', 1)	# 229831-229831
    if SLOT_97:
        _gotolabel(151)
    sprite('ryn300_08', 32767)	# 229832-262598
    Unknown21007(24, 40)
    Unknown21011(200)
    label(160)
    sprite('ryn000_00', 1)	# 262599-262599

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ryn000_00', 6)	# 262600-262605
    sprite('ryn000_01', 6)	# 262606-262611
    sprite('ryn000_02', 6)	# 262612-262617
    sprite('ryn000_03', 6)	# 262618-262623
    sprite('ryn000_04', 6)	# 262624-262629
    sprite('ryn000_05', 6)	# 262630-262635
    sprite('ryn000_06', 6)	# 262636-262641
    sprite('ryn000_07', 6)	# 262642-262647
    sprite('ryn000_08', 6)	# 262648-262653
    sprite('ryn000_09', 6)	# 262654-262659
    loopRest()
    gotoLabel(161)
    label(162)
    sprite('ryn300_00', 6)	# 262660-262665
    SFX_1('ryn701baz')
    sprite('ryn300_01', 6)	# 262666-262671
    sprite('ryn300_02', 6)	# 262672-262677
    Unknown23018(1)
    sprite('ryn300_03', 32767)	# 262678-295444
    label(170)
    sprite('ryn000_00', 1)	# 295445-295445

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('ryn000_00', 6)	# 295446-295451
    sprite('ryn000_01', 6)	# 295452-295457
    sprite('ryn000_02', 6)	# 295458-295463
    sprite('ryn000_03', 6)	# 295464-295469
    sprite('ryn000_04', 6)	# 295470-295475
    sprite('ryn000_05', 6)	# 295476-295481
    sprite('ryn000_06', 6)	# 295482-295487
    sprite('ryn000_07', 6)	# 295488-295493
    sprite('ryn000_08', 6)	# 295494-295499
    sprite('ryn000_09', 6)	# 295500-295505
    loopRest()
    gotoLabel(171)
    label(172)
    sprite('ryn611_00', 4)	# 295506-295509
    sprite('ryn611_01', 4)	# 295510-295513
    sprite('ryn611_02', 2)	# 295514-295515
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_03', 4)	# 295516-295519
    sprite('ryn611_04', 4)	# 295520-295523
    sprite('ryn611_05', 4)	# 295524-295527
    sprite('ryn611_06', 2)	# 295528-295529
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_07', 6)	# 295530-295535
    sprite('ryn611_08', 6)	# 295536-295541
    sprite('ryn611_09', 6)	# 295542-295547
    sprite('ryn611_10', 12)	# 295548-295559
    sprite('ryn611_11', 6)	# 295560-295565
    SFX_0('100_hit_grap_1')
    sprite('ryn611_12', 6)	# 295566-295571
    SFX_1('ryn701pka')
    Unknown23018(1)
    sprite('ryn611_13', 32767)	# 295572-328338
    label(180)
    sprite('ryn000_00', 1)	# 328339-328339

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ryn000_00', 6)	# 328340-328345
    sprite('ryn000_01', 6)	# 328346-328351
    sprite('ryn000_02', 6)	# 328352-328357
    sprite('ryn000_03', 6)	# 328358-328363
    sprite('ryn000_04', 6)	# 328364-328369
    sprite('ryn000_05', 6)	# 328370-328375
    sprite('ryn000_06', 6)	# 328376-328381
    sprite('ryn000_07', 6)	# 328382-328387
    sprite('ryn000_08', 6)	# 328388-328393
    sprite('ryn000_09', 6)	# 328394-328399
    loopRest()
    gotoLabel(181)
    label(182)
    sprite('ryn300_00', 6)	# 328400-328405
    SFX_1('ryn701rbl')
    sprite('ryn300_01', 6)	# 328406-328411
    sprite('ryn300_02', 6)	# 328412-328417
    Unknown23018(1)
    sprite('ryn300_03', 32767)	# 328418-361184
    label(190)
    sprite('ryn000_00', 1)	# 361185-361185

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('ryn000_00', 6)	# 361186-361191
    sprite('ryn000_01', 6)	# 361192-361197
    sprite('ryn000_02', 6)	# 361198-361203
    sprite('ryn000_03', 6)	# 361204-361209
    sprite('ryn000_04', 6)	# 361210-361215
    sprite('ryn000_05', 6)	# 361216-361221
    sprite('ryn000_06', 6)	# 361222-361227
    sprite('ryn000_07', 6)	# 361228-361233
    sprite('ryn000_08', 6)	# 361234-361239
    sprite('ryn000_09', 6)	# 361240-361245
    loopRest()
    gotoLabel(191)
    label(192)
    sprite('ryn611_00', 4)	# 361246-361249
    sprite('ryn611_01', 4)	# 361250-361253
    sprite('ryn611_02', 2)	# 361254-361255
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_03', 4)	# 361256-361259
    sprite('ryn611_04', 4)	# 361260-361263
    sprite('ryn611_05', 4)	# 361264-361267
    sprite('ryn611_06', 2)	# 361268-361269
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_07', 6)	# 361270-361275
    sprite('ryn611_08', 6)	# 361276-361281
    sprite('ryn611_09', 6)	# 361282-361287
    sprite('ryn611_10', 12)	# 361288-361299
    sprite('ryn611_11', 6)	# 361300-361305
    SFX_0('100_hit_grap_1')
    sprite('ryn611_12', 6)	# 361306-361311
    SFX_1('ryn701uwa')
    Unknown23018(1)
    sprite('ryn611_13', 32767)	# 361312-394078
    label(200)
    sprite('ryn611_00', 4)	# 394079-394082
    sprite('ryn611_01', 4)	# 394083-394086
    sprite('ryn611_02', 2)	# 394087-394088
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_03', 4)	# 394089-394092
    sprite('ryn611_04', 4)	# 394093-394096
    sprite('ryn611_05', 4)	# 394097-394100
    sprite('ryn611_06', 2)	# 394101-394102
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_07', 6)	# 394103-394108
    sprite('ryn611_08', 6)	# 394109-394114
    sprite('ryn611_09', 6)	# 394115-394120
    sprite('ryn611_10', 12)	# 394121-394132
    sprite('ryn611_11', 6)	# 394133-394138
    SFX_0('100_hit_grap_1')
    sprite('ryn611_12', 6)	# 394139-394144
    SFX_1('ryn700uca')
    label(201)
    sprite('ryn611_13', 1)	# 394145-394145
    if SLOT_97:
        _gotolabel(201)
    sprite('ryn611_13', 20)	# 394146-394165
    sprite('ryn611_13', 32767)	# 394166-426932
    Unknown21007(24, 40)
    Unknown21011(180)
    label(210)
    sprite('ryn300_00', 6)	# 426933-426938
    SFX_1('ryn700pla')
    sprite('ryn300_01', 6)	# 426939-426944
    sprite('ryn300_02', 6)	# 426945-426950
    label(211)
    sprite('ryn300_03', 1)	# 426951-426951
    if SLOT_97:
        _gotolabel(211)
    sprite('ryn300_03', 32767)	# 426952-459718
    Unknown21007(24, 40)
    Unknown21011(360)
    label(220)
    sprite('ryn000_00', 1)	# 459719-459719

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('ryn000_00', 6)	# 459720-459725
    sprite('ryn000_01', 6)	# 459726-459731
    sprite('ryn000_02', 6)	# 459732-459737
    sprite('ryn000_03', 6)	# 459738-459743
    sprite('ryn000_04', 6)	# 459744-459749
    sprite('ryn000_05', 6)	# 459750-459755
    sprite('ryn000_06', 6)	# 459756-459761
    sprite('ryn000_07', 6)	# 459762-459767
    sprite('ryn000_08', 6)	# 459768-459773
    sprite('ryn000_09', 6)	# 459774-459779
    loopRest()
    gotoLabel(221)
    label(222)
    sprite('keep', 1)	# 459780-459780
    if (SLOT_38 == 1):
        if (SLOT_152 == 1):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 >= 0):
                Unknown2037(1)
    if (SLOT_38 == 0):
        if (SLOT_152 == 0):
            Unknown48('190000000200000033000000180000000200000016000000')
            Unknown47('01000000020000003300000002000000160000000200000033000000')
            if (SLOT_51 <= 0):
                Unknown2037(1)
    sprite('keep', 1)	# 459781-459781
    if (not SLOT_2):
        sendToLabel(223)
    sprite('ryn003_00', 3)	# 459782-459784
    Unknown2005()
    sprite('ryn003_01', 3)	# 459785-459787
    sprite('ryn003_00ex01', 3)	# 459788-459790
    label(223)
    sprite('ryn000_00', 1)	# 459791-459791
    SFX_1('ryn701umi')
    Unknown23018(1)
    label(224)
    sprite('ryn000_00', 6)	# 459792-459797
    sprite('ryn000_01', 6)	# 459798-459803
    sprite('ryn000_02', 6)	# 459804-459809
    sprite('ryn000_03', 6)	# 459810-459815
    sprite('ryn000_04', 6)	# 459816-459821
    sprite('ryn000_05', 6)	# 459822-459827
    sprite('ryn000_06', 6)	# 459828-459833
    sprite('ryn000_07', 6)	# 459834-459839
    sprite('ryn000_08', 6)	# 459840-459845
    sprite('ryn000_09', 6)	# 459846-459851
    loopRest()
    gotoLabel(224)
    label(230)
    sprite('ryn000_00', 1)	# 459852-459852

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('ryn000_00', 6)	# 459853-459858
    sprite('ryn000_01', 6)	# 459859-459864
    sprite('ryn000_02', 6)	# 459865-459870
    sprite('ryn000_03', 6)	# 459871-459876
    sprite('ryn000_04', 6)	# 459877-459882
    sprite('ryn000_05', 6)	# 459883-459888
    sprite('ryn000_06', 6)	# 459889-459894
    sprite('ryn000_07', 6)	# 459895-459900
    sprite('ryn000_08', 6)	# 459901-459906
    sprite('ryn000_09', 6)	# 459907-459912
    loopRest()
    gotoLabel(231)
    label(232)
    sprite('ryn611_00', 4)	# 459913-459916
    sprite('ryn611_01', 4)	# 459917-459920
    sprite('ryn611_02', 2)	# 459921-459922
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_03', 4)	# 459923-459926
    sprite('ryn611_04', 4)	# 459927-459930
    sprite('ryn611_05', 4)	# 459931-459934
    sprite('ryn611_06', 2)	# 459935-459936
    SFX_0('004_swing_grap_1_1')
    sprite('ryn611_07', 6)	# 459937-459942
    sprite('ryn611_08', 6)	# 459943-459948
    sprite('ryn611_09', 6)	# 459949-459954
    sprite('ryn611_10', 12)	# 459955-459966
    sprite('ryn611_11', 6)	# 459967-459972
    SFX_0('100_hit_grap_1')
    sprite('ryn611_12', 6)	# 459973-459978
    SFX_1('ryn701pak')
    label(233)
    sprite('ryn611_13', 1)	# 459979-459979
    if SLOT_97:
        _gotolabel(233)
    sprite('ryn611_13', 30)	# 459980-460009
    sprite('ryn611_13', 32767)	# 460010-492776
    Unknown21007(24, 40)
    Unknown21011(300)

@State
def CmnActLose():
    sprite('ryn620_00', 6)	# 1-6
    sprite('ryn620_01', 6)	# 7-12
    sprite('ryn620_02', 6)	# 13-18
    if SLOT_158:
        Unknown7006('ryn403_0', 100, 879655282, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('ryn620_03', 6)	# 19-24
    sprite('ryn620_04', 6)	# 25-30
    sprite('ryn620_05', 6)	# 31-36
    sprite('ryn620_06', 6)	# 37-42
    sprite('ryn620_07', 6)	# 43-48
    Unknown23018(1)
    sprite('ryn620_08', 32767	# 49-32815
