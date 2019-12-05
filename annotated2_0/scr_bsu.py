@Subroutine
def PreInit():
    Unknown12019('62737500000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    Health(18000)
    WalkFSpeed(8250)
    WalkBSpeed(6600)
    DashFInitialVelocity(10000)
    Unknown12024(4)
    Unknown13039(0)
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
    Unknown15013(2000)
    Unknown14015(0, 500000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    Unknown14015(0, 350000, -200000, 200000, 2000, 50)
    MoveMaxChainRepeat(2)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    MoveMaxChainRepeat(2)
    Unknown15009()
    Unknown15013(2000)
    Unknown14015(0, 450000, -200000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 500000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 550000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 550000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(2)
    Unknown14015(-50000, 550000, -200000, 200000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Unknown15013(2000)
    Unknown15012(2000)
    Unknown14015(-50000, 650000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown14027('NmlAtk5B')
    Unknown15021(8000)
    Unknown14015(100000, 400000, 150000, 450000, 250, 10)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15021(1)
    Unknown15015(45, 48)
    Unknown15012(1500)
    Unknown14015(50000, 500000, -100000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown15013(20000)
    Unknown14015(0, 400000, -250000, 300000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Unknown14015(0, 300000, -200000, 300000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown14015(0, 500000, -300000, 300000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5BB', 0x22)
    Unknown14005(1)
    Unknown14015(-300000, 300000, -300000, 300000, 1000, 25)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15014(1)
    Unknown14015(0, 350000, -500000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15021(1)
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1000, 0)
    Move_EndRegister()
    Move_Register('Assault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15012(2000)
    Unknown14015(200000, 750000, -200000, 100000, 250, 10)
    Move_EndRegister()
    Move_Register('LowAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15009()
    Unknown15014(1)
    Unknown15013(2000)
    Unknown14015(200000, 750000, -200000, 100000, 250, 5)
    Move_EndRegister()
    Move_Register('Shot', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown15013(1)
    Unknown15012(2000)
    Unknown14015(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('RushAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15013(1)
    Unknown15012(4000)
    Unknown14015(0, 300000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(-350000, 350000, -200000, 300000, 250, 5)
    Move_EndRegister()
    Move_Register('LongAssault', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(1)
    Unknown15027(2000)
    Unknown14015(200000, 1000000, -200000, 200000, 150, 10)
    Move_EndRegister()
    Move_Register('AssaultThrow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15010()
    Unknown15021(0)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(3000)
    Unknown14015(0, 500000, -200000, 200000, 500, 10)
    Move_EndRegister()
    Move_Register('UltimateLongAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(4000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(550000, 1500000, -200000, 300000, 250, 5)
    if SLOT_100:
        Unknown14013('UltimateLongAssaultOD')
    Move_EndRegister()
    Move_Register('UltimateLongAssaultOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15013(1)
    Unknown15014(4000)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(550000, 1500000, -200000, 300000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateAntiAir', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15021(2000)
    Unknown15014(4000)
    Unknown15012(1)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 350000, -200000, 500000, 500, 1)
    if SLOT_100:
        Unknown14013('UltimateAntiAirOD')
    Move_EndRegister()
    Move_Register('UltimateAntiAirOD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15021(2000)
    Unknown15014(4000)
    Unknown15012(1)
    Unknown15020(500, 1000, 1, 1000)
    Unknown14015(0, 350000, -200000, 500000, 500, 1)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'Assault', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk2B', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk2B', 'VHighJump', 10000000)
    Unknown15024('NmlAtk2C', 'Assault', 10000000)
    Unknown15024('NmlAtk2C', 'LowAssault', 10000000)
    Unknown15024('NmlAtk2C', 'LongAssault', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5B', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5B', 'NmlAtkAIR5C', 10000000)
    Unknown15024('NmlAtkAIR5BB', 'FJump', 10000000)
    Unknown15024('LowAssault', 'FHighJump', 10000000)
    Unknown12018(0, 'su062_01')
    Unknown12018(1, 'su062_03')
    Unknown12018(2, 'su062_04')
    Unknown12018(3, 'su062_05')
    Unknown12018(4, 'su062_05')
    Unknown12018(5, 'su062_06')
    Unknown12018(6, 'su062_07')
    Unknown12018(7, 'su041_02')
    Unknown12018(8, 'su040_02')
    Unknown12018(9, 'su045_02')
    Unknown12018(10, 'su060_00')
    Unknown12018(11, 'su060_01')
    Unknown12018(12, 'su060_03')
    Unknown12018(13, 'su060_05')
    Unknown12018(14, 'su060_07')
    Unknown12018(15, 'su060_14')
    Unknown12018(16, 'su050_00')
    Unknown12018(17, 'su052_00')
    Unknown12018(18, 'su054_00')
    Unknown12018(19, 'su000_00')
    Unknown12018(20, 'su000_00')
    Unknown12018(25, 'su063_00')
    Unknown12018(26, 'su063_01')
    Unknown12018(27, 'su063_02')
    Unknown12018(28, 'su063_04')
    Unknown12018(29, 'su063_10')
    Unknown12018(24, 'su073_01')
    Unknown7010(0, 'bsu000')
    Unknown7010(1, 'bsu001')
    Unknown7010(2, 'bsu002')
    Unknown7010(3, 'bsu003')
    Unknown7010(4, 'bsu004')
    Unknown7010(5, 'bsu005')
    Unknown7010(6, 'bsu006')
    Unknown7010(7, 'bsu007')
    Unknown7010(8, 'bsu008')
    Unknown7010(9, 'bsu009')
    Unknown7010(10, 'bsu010')
    Unknown7010(15, 'bsu011')
    Unknown7010(16, 'bsu012')
    Unknown7010(17, 'bsu013')
    Unknown7010(18, 'bsu014')
    Unknown7010(19, 'bsu015')
    Unknown7010(20, 'bsu016')
    Unknown7010(21, 'bsu017')
    Unknown7010(22, 'bsu018')
    Unknown7010(23, 'bsu019')
    Unknown7010(24, 'bsu020')
    Unknown7010(25, 'bsu021')
    Unknown7010(28, 'bsu022')
    Unknown7010(29, 'bsu023')
    Unknown7010(30, 'bsu024')
    Unknown7010(31, 'bsu025')
    Unknown7010(32, 'bsu026')
    Unknown7010(33, 'bsu027')
    Unknown7010(34, 'bsu028')
    Unknown7010(35, 'bsu029')
    Unknown7010(36, 'bsu030')
    Unknown7010(37, 'bsu031')
    Unknown7010(39, 'bsu032')
    Unknown7010(42, 'bsu033')
    Unknown7010(43, 'bsu034')
    Unknown7010(44, 'bsu035')
    Unknown7010(45, 'bsu036')
    Unknown7010(46, 'bsu037')
    Unknown7010(47, 'bsu038')
    Unknown7010(48, 'bsu039')
    Unknown7010(49, 'bsu040')
    Unknown7010(50, 'bsu041')
    Unknown7010(52, 'bsu042')
    Unknown7010(53, 'bsu043')
    Unknown7010(54, 'bsu100_0')
    Unknown7010(55, 'bsu100_1')
    Unknown7010(56, 'bsu100_2')
    Unknown7010(63, 'bsu101_0')
    Unknown7010(64, 'bsu101_1')
    Unknown7010(65, 'bsu101_2')
    Unknown7010(57, 'bsu102_0')
    Unknown7010(58, 'bsu102_1')
    Unknown7010(59, 'bsu102_2')
    Unknown7010(66, 'bsu103_0')
    Unknown7010(67, 'bsu103_1')
    Unknown7010(68, 'bsu103_2')
    Unknown7010(60, 'bsu104_0')
    Unknown7010(61, 'bsu104_1')
    Unknown7010(62, 'bsu104_2')
    Unknown7010(69, 'bsu105_0')
    Unknown7010(70, 'bsu105_1')
    Unknown7010(71, 'bsu105_2')
    Unknown7010(72, 'bsu150')
    Unknown7010(73, 'bsu151')
    Unknown7010(74, 'bsu152')
    Unknown7010(85, 'bsu153')
    Unknown7010(87, 'bsu154')
    Unknown7010(88, 'bsu155')
    Unknown7010(96, 'bsu161_0')
    Unknown7010(97, 'bsu161_1')
    Unknown7010(92, 'bsu162_0')
    Unknown7010(93, 'bsu162_1')
    Unknown7010(98, 'bsu163_0')
    Unknown7010(99, 'bsu163_1')
    Unknown7010(100, 'bsu164_0')
    Unknown7010(101, 'bsu164_1')
    Unknown7010(105, 'bsu165_0')
    Unknown7010(106, 'bsu165_1')
    Unknown7010(102, 'bsu166_0')
    Unknown7010(103, 'bsu166_1')
    Unknown7010(90, 'bsu167_0')
    Unknown7010(91, 'bsu167_1')
    Unknown7010(107, 'bsu168_0')
    Unknown7010(108, 'bsu168_1')
    Unknown7010(110, 'bsu169_0')
    Unknown7010(111, 'bsu169_1')
    Unknown7010(112, 'bsu159_0')
    Unknown7010(113, 'bsu159_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d6174654c6f6e6741737361756c7400000000000000000000000000')
    Unknown12059('03000000556c74696d6174654c6f6e6741737361756c744f440000000000000000000000')
    Unknown12059('04000000556c74696d617465416e74694169720000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465416e74694169724f44000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def MatchInit2():
    if SLOT_100:
        Health(54000)

@Subroutine
def EmissionStart():
    Unknown30007('01000000')
    Unknown30011('')
    Unknown30009('05000000')
    Unknown30016('00000000')
    Unknown30017('00000000')
    if (not SLOT_57):
        Unknown30009('0b000000')

@Subroutine
def OnFrameStep():
    if (not Unknown23148('CmnActTagBattleWait')):
        if SLOT_75:
            if (not SLOT_30):
                if (not SLOT_6):
                    GFX_0('suef_aura', 103)

@Subroutine
def OnFinalize():
    Unknown30007('00000000')
    Unknown30011('')
    Unknown30016('ff000000')
    Unknown30017('00000000')

@State
def CmnActStand():
    label(0)
    sprite('su000_00', 7)	# 1-7
    sprite('su000_01', 7)	# 8-14
    sprite('su000_02', 7)	# 15-21
    sprite('su000_03', 7)	# 22-28
    sprite('su000_04', 7)	# 29-35
    sprite('su000_05', 7)	# 36-42
    sprite('su000_06', 7)	# 43-49
    sprite('su000_07', 7)	# 50-56
    sprite('su000_08', 7)	# 57-63
    sprite('su000_09', 7)	# 64-70
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('su001_00', 6)	# 71-76
    SLOT_88 = 960

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    callSubroutine('EmissionStart')
    Unknown30017('11000000')
    GFX_0('suef_001', -1)
    GFX_0('suef_001_blm_2d', -1)
    SFX_0('022_magiccircle_b')
    SFX_4('bsu000')
    sprite('su001_01', 6)	# 77-82
    sprite('su001_02', 7)	# 83-89
    sprite('su001_03', 8)	# 90-97
    sprite('su001_04', 9)	# 98-106
    sprite('su001_05', 9)	# 107-115
    sprite('su001_06', 9)	# 116-124
    sprite('su001_07', 8)	# 125-132
    sprite('su001_08', 7)	# 133-139
    Unknown30017('f4ffffff')
    sprite('su001_09', 6)	# 140-145
    sprite('su001_10', 6)	# 146-151
    SLOT_57 = 0
    clearUponHandler(3)
    clearUponHandler(1)
    SLOT_6 = 0
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('su003_00', 3)	# 1-3
    sprite('su003_01', 3)	# 4-6
    sprite('su003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('su010_00', 4)	# 1-4
    sprite('su010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('su010_02', 6)	# 1-6
    sprite('su010_03', 6)	# 7-12
    sprite('su010_04', 6)	# 13-18
    sprite('su010_05', 6)	# 19-24
    sprite('su010_06', 6)	# 25-30
    sprite('su010_07', 6)	# 31-36
    sprite('su010_08', 6)	# 37-42
    sprite('su010_09', 6)	# 43-48
    sprite('su010_10', 6)	# 49-54
    sprite('su010_11', 6)	# 55-60
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('su013_00', 3)	# 1-3
    sprite('su013_01', 3)	# 4-6
    sprite('su013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('su010_01', 4)	# 1-4
    sprite('su010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('su023_00', 2)	# 1-2
    sprite('su023_01', 2)	# 3-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('su020_00', 4)	# 1-4
    sprite('su020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('su020_02', 3)	# 1-3
    sprite('su020_03', 3)	# 4-6
    sprite('su020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('su020_05', 3)	# 1-3
    sprite('su020_06', 3)	# 4-6
    label(0)
    sprite('su020_07', 4)	# 7-10
    sprite('su020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    Unknown8000(100, 1, 0)
    sprite('su024_00', 3)	# 1-3
    sprite('su024_01', 3)	# 4-6
    sprite('su024_02', 3)	# 7-9
    sprite('su024_03', 3)	# 10-12
    sprite('su024_04', 3)	# 13-15

@State
def CmnActLandingStiffLoop():
    sprite('su024_00', 2)	# 1-2
    sprite('su024_01', 2)	# 3-4
    sprite('su024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('su024_03', 3)	# 1-3
    sprite('su024_04', 3)	# 4-6

@State
def CmnActFWalk():
    sprite('null', 60)	# 1-60

@State
def CmnActBWalk():
    sprite('su031_00', 7)	# 1-7
    label(0)
    sprite('su031_01', 7)	# 8-14
    sprite('su031_02', 7)	# 15-21
    sprite('su031_03', 7)	# 22-28
    sprite('su031_04', 7)	# 29-35
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('su031_05', 7)	# 36-42
    sprite('su031_06', 7)	# 43-49
    sprite('su031_07', 7)	# 50-56
    sprite('su031_08', 7)	# 57-63
    sprite('su031_09', 7)	# 64-70
    sprite('su031_10', 7)	# 71-77
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('su031_11', 7)	# 78-84
    sprite('su031_12', 7)	# 85-91
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('su032_15', 3)	# 1-3
    sprite('su032_14', 3)	# 4-6
    sprite('su032_13', 3)	# 7-9
    sprite('su032_12', 3)	# 10-12
    sprite('su032_11', 3)	# 13-15
    sprite('su032_00', 3)	# 16-18
    Unknown1015(12000)
    label(0)
    sprite('su032_01', 4)	# 19-22
    sprite('su032_02', 4)	# 23-26
    sprite('su032_03', 4)	# 27-30
    sprite('su032_04', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('su032_05', 4)	# 35-38
    sprite('su032_06', 4)	# 39-42
    sprite('su032_07', 4)	# 43-46
    sprite('su032_08', 4)	# 47-50
    Unknown8006(100, 1, 1)
    sprite('su032_09', 4)	# 51-54
    sprite('su032_10', 4)	# 55-58
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('su032_11', 2)	# 1-2
    sprite('su032_12', 2)	# 3-4
    sprite('su032_13', 2)	# 5-6
    sprite('su032_14', 3)	# 7-9
    sprite('su032_15', 3)	# 10-12

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

        def upon_STATE_END():
            physicsYImpulse(0)
            setGravity(0)
    sprite('su033_00', 1)	# 1-1
    sprite('su033_01', 3)	# 2-4
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('su033_02', 1)	# 5-5
    sprite('su033_02', 2)	# 6-7
    loopRest()
    label(0)
    sprite('su033_01', 3)	# 8-10
    sprite('su033_02', 3)	# 11-13
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su033_03', 3)	# 14-16
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('su033_04', 3)	# 17-19
    sprite('su033_05', 3)	# 20-22
    Unknown13002(1)
    Unknown13003(1)
    Unknown13005(1)
    Unknown13006(1)
    Unknown13008(1)
    Unknown13019(1)
    Unknown13014(1)
    Unknown13015(1)
    sprite('su033_06', 3)	# 23-25
    sprite('su033_07', 3)	# 26-28

@State
def CmnActBDashLanding():
    sprite('null', 60)	# 1-60

@State
def CmnActAirFDash():
    sprite('su035_00', 3)	# 1-3
    label(0)
    sprite('su035_01', 3)	# 4-6
    sprite('su035_02', 3)	# 7-9
    sprite('su035_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('su036_00', 3)	# 1-3
    label(0)
    sprite('su036_01', 3)	# 4-6
    sprite('su036_02', 3)	# 7-9
    sprite('su036_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('su050_00', 1)	# 1-1
    sprite('su050_01', 1)	# 2-2
    sprite('su050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('su050_01', 1)	# 1-1
    sprite('su050_02', 1)	# 2-2
    sprite('su050_01', 2)	# 3-4
    sprite('su050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('su050_02', 1)	# 1-1
    sprite('su050_03', 1)	# 2-2
    sprite('su050_02', 2)	# 3-4
    sprite('su050_01', 2)	# 5-6
    sprite('su050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('su050_03', 1)	# 1-1
    sprite('su050_04', 1)	# 2-2
    sprite('su050_03', 2)	# 3-4
    sprite('su050_02', 2)	# 5-6
    sprite('su050_01', 2)	# 7-8
    sprite('su050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('su050_04', 1)	# 1-1
    sprite('su050_04', 1)	# 2-2
    sprite('su050_04', 2)	# 3-4
    sprite('su050_03', 2)	# 5-6
    sprite('su050_02', 2)	# 7-8
    sprite('su050_01', 2)	# 9-10
    sprite('su050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('su052_00', 1)	# 1-1
    sprite('su052_01', 1)	# 2-2
    sprite('su052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('su052_01', 1)	# 1-1
    sprite('su052_02', 1)	# 2-2
    sprite('su052_01', 2)	# 3-4
    sprite('su052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('su052_02', 1)	# 1-1
    sprite('su052_03', 1)	# 2-2
    sprite('su052_02', 2)	# 3-4
    sprite('su052_01', 2)	# 5-6
    sprite('su052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('su052_03', 1)	# 1-1
    sprite('su052_04', 1)	# 2-2
    sprite('su052_03', 2)	# 3-4
    sprite('su052_02', 2)	# 5-6
    sprite('su052_01', 2)	# 7-8
    sprite('su052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('su052_04', 1)	# 1-1
    sprite('su052_04', 1)	# 2-2
    sprite('su052_04', 2)	# 3-4
    sprite('su052_03', 2)	# 5-6
    sprite('su052_02', 2)	# 7-8
    sprite('su052_01', 2)	# 9-10
    sprite('su052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('su054_00', 1)	# 1-1
    sprite('su054_01', 1)	# 2-2
    sprite('su054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('su054_01', 1)	# 1-1
    sprite('su054_02', 1)	# 2-2
    sprite('su054_01', 2)	# 3-4
    sprite('su054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('su054_02', 1)	# 1-1
    sprite('su054_03', 1)	# 2-2
    sprite('su054_02', 2)	# 3-4
    sprite('su054_01', 2)	# 5-6
    sprite('su054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('su054_03', 1)	# 1-1
    sprite('su054_04', 1)	# 2-2
    sprite('su054_03', 2)	# 3-4
    sprite('su054_02', 2)	# 5-6
    sprite('su054_01', 2)	# 7-8
    sprite('su054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('su054_04', 1)	# 1-1
    sprite('su054_04', 1)	# 2-2
    sprite('su054_04', 2)	# 3-4
    sprite('su054_03', 2)	# 5-6
    sprite('su054_02', 2)	# 7-8
    sprite('su054_01', 2)	# 9-10
    sprite('su054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('su060_00', 4)	# 1-4
    label(0)
    sprite('su060_01', 4)	# 5-8
    sprite('su060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('su060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('su060_04', 4)	# 1-4
    label(0)
    sprite('su060_05', 4)	# 5-8
    sprite('su060_06', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('su060_07', 2)	# 1-2
    sprite('su060_08', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('su060_09', 3)	# 1-3
    sprite('su060_10', 3)	# 4-6
    sprite('su060_11', 3)	# 7-9
    sprite('su060_12', 3)	# 10-12
    sprite('su060_13', 3)	# 13-15

@State
def CmnActBDownLoop():
    sprite('su060_14', 1)	# 1-1

@State
def CmnActBDown2Stand():
    sprite('su061_00', 3)	# 1-3
    sprite('su061_01', 3)	# 4-6
    sprite('su061_02', 3)	# 7-9
    sprite('su061_03', 3)	# 10-12
    sprite('su061_04', 3)	# 13-15
    sprite('su061_05', 3)	# 16-18
    sprite('su061_06', 2)	# 19-20
    sprite('su061_07', 2)	# 21-22
    sprite('su061_08', 3)	# 23-25
    sprite('su061_09', 3)	# 26-28

@State
def CmnActFDownUpper():
    sprite('su063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('su063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('su063_02', 3)	# 1-3
    sprite('su063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('su063_04', 2)	# 1-2
    sprite('su063_05', 2)	# 3-4

@State
def CmnActFDownBound():
    sprite('su063_06', 2)	# 1-2
    sprite('su063_07', 2)	# 3-4
    sprite('su063_08', 3)	# 5-7
    sprite('su063_09', 3)	# 8-10
    sprite('su063_10', 3)	# 11-13

@State
def CmnActFDownLoop():
    sprite('su063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('su064_00', 2)	# 1-2
    sprite('su064_01', 2)	# 3-4
    sprite('su064_02', 2)	# 5-6
    sprite('su064_03', 2)	# 7-8
    sprite('su064_04', 2)	# 9-10
    sprite('su064_05', 2)	# 11-12
    sprite('su064_06', 2)	# 13-14
    sprite('su064_07', 2)	# 15-16
    sprite('su064_08', 3)	# 17-19
    sprite('su064_09', 3)	# 20-22

@State
def CmnActVDownUpper():
    sprite('su062_00', 3)	# 1-3
    label(0)
    sprite('su062_01', 3)	# 4-6
    sprite('su062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('su062_03', 3)	# 1-3
    sprite('su062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('su062_05', 3)	# 1-3
    sprite('su062_06', 3)	# 4-6
    label(0)
    sprite('su062_07', 3)	# 7-9
    sprite('su062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('su062_09', 2)	# 1-2
    sprite('su062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('su072_00', 3)	# 1-3
    sprite('su072_01', 3)	# 4-6
    sprite('su072_02', 3)	# 7-9
    label(0)
    sprite('su072_01', 3)	# 10-12
    sprite('su072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('su074_00', 3)	# 1-3
    sprite('su074_01', 3)	# 4-6
    sprite('su074_02', 3)	# 7-9
    sprite('su074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('su082_00', 2)	# 1-2
    sprite('su082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('su071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('su073_00', 3)	# 1-3
    sprite('su073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('su073_02', 3)	# 1-3
    label(0)
    sprite('su073_03', 3)	# 4-6
    sprite('su073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('su070_00', 2)	# 1-2
    sprite('su070_01', 2)	# 3-4
    label(0)
    sprite('su070_02', 5)	# 5-9
    sprite('su070_03', 5)	# 10-14
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('su070_04', 4)	# 1-4
    sprite('su070_05', 4)	# 5-8
    sprite('su070_06', 4)	# 9-12
    sprite('su070_07', 4)	# 13-16
    sprite('su070_08', 4)	# 17-20
    sprite('su070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('su070_11', 2)	# 1-2
    sprite('su070_12', 3)	# 3-5
    sprite('su070_13', 3)	# 6-8

@State
def CmnActUkemiAirF():
    sprite('su113_00', 3)	# 1-3
    sprite('su113_01', 3)	# 4-6
    sprite('su113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('su113_00', 3)	# 1-3
    sprite('su113_01', 3)	# 4-6
    sprite('su113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('su113_00', 3)	# 1-3
    sprite('su113_01', 3)	# 4-6
    sprite('su113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('su110_00', 2)	# 1-2
    sprite('su110_01', 2)	# 3-4
    sprite('su110_02', 2)	# 5-6
    sprite('su110_03', 2)	# 7-8
    sprite('su110_04', 3)	# 9-11
    sprite('su110_05', 3)	# 12-14
    sprite('su110_06', 200)	# 15-214
    sprite('su110_07', 3)	# 215-217
    sprite('su110_08', 3)	# 218-220

@State
def CmnActUkemiLandB():
    sprite('su111_00', 3)	# 1-3
    sprite('su111_01', 3)	# 4-6
    sprite('su111_02', 3)	# 7-9
    sprite('su111_03', 3)	# 10-12
    sprite('su111_04', 3)	# 13-15
    sprite('su111_05', 3)	# 16-18
    sprite('su111_06', 200)	# 19-218
    sprite('su111_07', 3)	# 219-221
    sprite('su111_08', 3)	# 222-224

@State
def CmnActUkemiLandN():
    sprite('su112_00', 2)	# 1-2
    sprite('su112_01', 2)	# 3-4
    sprite('su112_02', 2)	# 5-6
    sprite('su112_03', 2)	# 7-8
    sprite('su112_04', 2)	# 9-10
    sprite('su112_05', 2)	# 11-12
    sprite('su112_06', 2)	# 13-14
    sprite('su112_07', 3)	# 15-17

@State
def CmnActUkemiLandNLanding():
    sprite('su024_00', 3)	# 1-3
    sprite('su024_01', 3)	# 4-6
    sprite('su024_02', 3)	# 7-9
    sprite('su024_03', 3)	# 10-12
    sprite('su024_04', 3)	# 13-15

@State
def CmnActMidGuardPre():
    sprite('su040_00', 3)	# 1-3
    sprite('su040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('su040_02', 4)	# 1-4
    sprite('su040_03', 4)	# 5-8
    sprite('su040_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('su040_01', 3)	# 1-3
    sprite('su040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('su040_05', 3)	# 1-3
    label(0)
    sprite('su040_02', 3)	# 4-6
    sprite('su040_03', 3)	# 7-9
    sprite('su040_04', 3)	# 10-12
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('su040_01', 3)	# 1-3
    sprite('su040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('su041_00', 3)	# 1-3
    sprite('su041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    label(0)
    sprite('su041_02', 4)	# 1-4
    sprite('su041_03', 4)	# 5-8
    sprite('su041_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('su041_01', 3)	# 1-3
    sprite('su041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('su041_05', 3)	# 1-3
    label(0)
    sprite('su041_02', 4)	# 4-7
    sprite('su041_03', 4)	# 8-11
    sprite('su041_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('su041_01', 3)	# 1-3
    sprite('su041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('su043_00', 3)	# 1-3
    sprite('su043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('su043_02', 4)	# 1-4
    sprite('su043_03', 4)	# 5-8
    sprite('su043_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('su043_01', 3)	# 1-3
    sprite('su043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('su043_05', 3)	# 1-3
    label(0)
    sprite('su043_02', 4)	# 4-7
    sprite('su043_03', 4)	# 8-11
    sprite('su043_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('su043_01', 3)	# 1-3
    sprite('su043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('su045_00', 3)	# 1-3
    sprite('su045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('su045_02', 4)	# 1-4
    sprite('su045_03', 4)	# 5-8
    sprite('su045_04', 4)	# 9-12
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('su045_01', 3)	# 1-3
    sprite('su045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('su045_05', 3)	# 1-3
    label(0)
    sprite('su045_02', 4)	# 4-7
    sprite('su045_03', 4)	# 8-11
    sprite('su045_04', 4)	# 12-15
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('su045_01', 3)	# 1-3
    sprite('su045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('su090_00', 2)	# 1-2
    sprite('su090_01', 2)	# 3-4
    sprite('su090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('su090_03', 6)	# 6-11
    sprite('su090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('su091_00', 2)	# 1-2
    sprite('su091_01', 2)	# 3-4
    sprite('su091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('su091_03', 6)	# 6-11
    sprite('su091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('su092_00', 2)	# 1-2
    sprite('su092_01', 2)	# 3-4
    sprite('su092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('su092_03', 6)	# 6-11
    sprite('su092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('su025_00', 4)	# 1-4
    sprite('su025_01', 4)	# 5-8
    sprite('su025_02', 4)	# 9-12

@State
def CmnActLockWait():
    sprite('su040_02', 1)	# 1-1
    sprite('su040_01', 3)	# 2-4
    sprite('su040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('su312_00', 2)	# 1-2
    sprite('su312_01', 2)	# 3-4
    sprite('su312_02', 2)	# 5-6
    sprite('su312_03', 5)	# 7-11	 **attackbox here**
    GFX_0('suef_312', -1)
    sprite('su312_04', 3)	# 12-14
    sprite('su312_05', 3)	# 15-17
    sprite('su312_06', 3)	# 18-20
    sprite('su312_07', 3)	# 21-23
    sprite('su312_08', 3)	# 24-26
    sprite('su312_09', 3)	# 27-29

@State
def CmnActAirLockWait():
    sprite('su045_02', 1)	# 1-1
    sprite('su045_01', 3)	# 2-4
    sprite('su045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('su322_00', 3)	# 1-3
    sprite('su322_01', 3)	# 4-6
    sprite('su322_02', 6)	# 7-12
    sprite('su322_03', 8)	# 13-20	 **attackbox here**
    GFX_0('suef_312', -1)
    Unknown36(1)
    teleportRelativeX(-48000)
    Unknown35()
    sprite('su322_04', 3)	# 21-23
    sprite('su322_05', 3)	# 24-26
    sprite('su322_06', 3)	# 27-29

@State
def CmnActLandSpin():
    sprite('su071_00', 4)	# 1-4
    sprite('su071_01', 4)	# 5-8
    label(0)
    sprite('su071_02', 2)	# 9-10
    sprite('su071_03', 2)	# 11-12
    sprite('su071_04', 2)	# 13-14
    sprite('su071_05', 2)	# 15-16
    sprite('su071_06', 2)	# 17-18
    sprite('su071_07', 2)	# 19-20
    sprite('su071_08', 2)	# 21-22
    sprite('su071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('su071_10', 6)	# 1-6
    sprite('su071_11', 5)	# 7-11
    sprite('su071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('su071_02', 2)	# 1-2
    sprite('su071_03', 2)	# 3-4
    sprite('su071_04', 2)	# 5-6
    sprite('su071_05', 2)	# 7-8
    sprite('su071_06', 2)	# 9-10
    sprite('su071_07', 2)	# 11-12
    sprite('su071_08', 2)	# 13-14
    sprite('su071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('su077_00', 2)	# 1-2
    sprite('su077_01', 2)	# 3-4
    sprite('su077_00ex00', 2)	# 5-6
    sprite('su077_01ex00', 2)	# 7-8
    sprite('su077_00ex01', 2)	# 9-10
    sprite('su077_01ex01', 2)	# 11-12
    sprite('su077_00ex02', 2)	# 13-14
    sprite('su077_01ex02', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('su077_02', 4)	# 1-4
    label(0)
    sprite('su077_03', 3)	# 5-7
    sprite('su077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('su077_05', 5)	# 1-5
    sprite('su077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('su060_07', 3)	# 1-3
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('su060_11', 4)	# 1-4
    sprite('su060_13', 5)	# 5-9

@State
def CmnActBurstBegin():
    sprite('su331_00', 2)	# 1-2
    GFX_0('suef_331', 103)
    sprite('su331_01', 2)	# 3-4
    label(0)
    sprite('su331_02', 3)	# 5-7
    sprite('su331_03', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('su331_04', 2)	# 1-2
    sprite('su331_05', 2)	# 3-4
    callSubroutine('EmissionStart')
    SLOT_57 = 1
    Unknown30016('ff000000')
    label(0)
    sprite('su331_06', 3)	# 5-7
    sprite('su331_07', 3)	# 8-10
    sprite('su331_08', 3)	# 11-13
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('su331_09', 3)	# 1-3
    callSubroutine('EmissionStart')
    SLOT_57 = 1
    Unknown30016('ff000000')
    Unknown30017('d6ffffff')
    sprite('su331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('su331_11', 2)	# 1-2
    GFX_0('suef_331', 103)
    sprite('su331_12', 2)	# 3-4
    label(0)
    sprite('su331_02', 3)	# 5-7
    sprite('su331_03', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('su331_04', 2)	# 1-2
    sprite('su331_05', 2)	# 3-4
    callSubroutine('EmissionStart')
    SLOT_57 = 1
    Unknown30016('ff000000')
    label(0)
    sprite('su331_06', 2)	# 5-6
    sprite('su331_07', 2)	# 7-8
    sprite('su331_08', 2)	# 9-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('su331_13', 2)	# 1-2
    callSubroutine('EmissionStart')
    SLOT_57 = 1
    Unknown30016('ff000000')
    Unknown30017('d6ffffff')
    sprite('su331_14', 2)	# 3-4
    sprite('su020_05', 3)	# 5-7
    sprite('su020_06', 3)	# 8-10
    label(0)
    sprite('su020_07', 4)	# 11-14
    sprite('su020_08', 4)	# 15-18
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('su333_00', 3)	# 1-3
    sprite('su333_01', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    sprite('su333_02', 3)	# 7-9
    sprite('su333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('su333_04', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    label(0)
    sprite('su333_05', 3)	# 4-6
    sprite('su333_06', 3)	# 7-9
    sprite('su333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('su333_08', 6)	# 1-6
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    Unknown30017('ebffffff')
    sprite('su333_09', 6)	# 7-12

@State
def CmnActAirOverDriveBegin():
    sprite('su333_10', 3)	# 1-3
    sprite('su333_11', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    sprite('su333_12', 3)	# 7-9
    sprite('su333_13', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('su333_14', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    label(0)
    sprite('su333_05', 3)	# 4-6
    sprite('su333_06', 3)	# 7-9
    sprite('su333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('su333_15', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    Unknown30017('ebffffff')
    sprite('su333_16', 3)	# 4-6
    sprite('su020_05', 3)	# 7-9
    sprite('su020_06', 3)	# 10-12
    label(0)
    sprite('su020_07', 4)	# 13-16
    sprite('su020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('su333_00', 3)	# 1-3
    sprite('su333_01', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    sprite('su333_02', 3)	# 7-9
    sprite('su333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('su333_04', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    label(0)
    sprite('su333_05', 3)	# 4-6
    sprite('su333_06', 3)	# 7-9
    sprite('su333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('su333_08', 6)	# 1-6
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    Unknown30017('ebffffff')
    sprite('su333_09', 6)	# 7-12

@State
def CmnActAirCrossRushBegin():
    sprite('su333_10', 3)	# 1-3
    sprite('su333_11', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    sprite('su333_12', 3)	# 7-9
    sprite('su333_13', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('su333_14', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    label(0)
    sprite('su333_05', 3)	# 4-6
    sprite('su333_06', 3)	# 7-9
    sprite('su333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('su333_15', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    Unknown30017('ebffffff')
    sprite('su333_16', 3)	# 4-6
    sprite('su020_05', 3)	# 7-9
    sprite('su020_06', 3)	# 10-12
    label(0)
    sprite('su020_07', 4)	# 13-16
    sprite('su020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('su214_00', 2)	# 1-2
    sprite('su214_01', 2)	# 3-4
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su214_02', 2)	# 5-6
    sprite('su214_03', 2)	# 7-8
    label(0)
    sprite('su214_04', 3)	# 9-11
    sprite('su214_05', 3)	# 12-14
    sprite('su214_06', 3)	# 15-17
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('su214_07', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    label(0)
    sprite('su214_08', 3)	# 4-6
    sprite('su214_09', 3)	# 7-9
    sprite('su214_10', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('su214_11', 2)	# 1-2
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    Unknown30017('ebffffff')
    sprite('su214_12', 2)	# 3-4
    sprite('su214_13', 2)	# 5-6

@State
def CmnActAirCrossChangeBegin():
    sprite('su214_00', 2)	# 1-2
    sprite('su214_01', 2)	# 3-4
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su214_02', 2)	# 5-6
    sprite('su214_03', 2)	# 7-8
    label(0)
    sprite('su214_04', 3)	# 9-11
    sprite('su214_05', 3)	# 12-14
    sprite('su214_06', 3)	# 15-17
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('su214_07', 3)	# 1-3
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    label(0)
    sprite('su214_08', 3)	# 4-6
    sprite('su214_09', 3)	# 7-9
    sprite('su214_10', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('su214_11', 2)	# 1-2
    callSubroutine('EmissionStart')
    Unknown30016('ff000000')
    Unknown30017('ebffffff')
    sprite('su214_12', 2)	# 3-4
    sprite('su214_13', 2)	# 5-6
    sprite('su020_05', 3)	# 7-9
    sprite('su020_06', 3)	# 10-12
    label(0)
    sprite('su020_07', 4)	# 13-16
    sprite('su020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActTagBattleWait():

    def upon_IMMEDIATE():
        setInvincible(1)
        EnableCollision(0)
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

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 27)	# 603-629
    sprite('su251_00', 1)	# 630-630
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    teleportRelativeY(1000000)
    Unknown1007(30000)
    physicsXImpulse(375000)
    physicsYImpulse(-250000)
    sprite('su251_01', 1)	# 631-631
    sprite('su251_02', 2)	# 632-633
    sprite('su251_03', 2)	# 634-635
    physicsXImpulse(0)
    physicsYImpulse(0)
    Unknown2053(1)
    EnableCollision(1)
    sendToLabelUpon(2, 9)
    sprite('su251_04ex01', 4)	# 636-639	 **attackbox here**
    GFX_0('suef_251_3d', -1)
    physicsXImpulse(0)
    physicsYImpulse(1000)
    sendToLabelUpon(2, 9)
    sprite('su251_05', 4)	# 640-643
    sprite('su251_06', 4)	# 644-647
    Unknown1043()
    sprite('su251_07', 4)	# 648-651
    sprite('su251_08', 4)	# 652-655
    sprite('su251_09', 3)	# 656-658
    sprite('su251_10', 3)	# 659-661
    sprite('su020_03', 3)	# 662-664
    sprite('su020_04', 3)	# 665-667
    sprite('su020_05', 3)	# 668-670
    label(1)
    sprite('su020_06', 3)	# 671-673
    sprite('su020_07', 3)	# 674-676
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('su024_00', 2)	# 677-678
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('su024_01', 2)	# 679-680
    sprite('su024_02', 2)	# 681-682
    sprite('su024_03', 2)	# 683-684
    sprite('su024_04', 1)	# 685-685

@State
def CmnActChangePartnerQuickIn():
    sprite('su032_11', 4)	# 1-4
    sprite('su032_12', 4)	# 5-8
    sprite('su032_13', 7)	# 9-15
    sprite('su032_14', 7)	# 16-22
    sprite('su032_15', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('su033_00', 1)	# 1-1
    sprite('su033_01', 3)	# 2-4
    sprite('su033_01', 3)	# 5-7
    sprite('su033_02', 3)	# 8-10
    sprite('su033_01', 3)	# 11-13
    sprite('su033_02', 3)	# 14-16
    sprite('su033_01', 3)	# 17-19
    sprite('su033_02', 3)	# 20-22
    sprite('su033_01', 3)	# 23-25
    sprite('su033_02', 3)	# 26-28
    sprite('su033_02', 30)	# 29-58

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()
        sendToLabelUpon(2, 1)
    sprite('su033_00', 1)	# 1-1
    sprite('su033_01', 3)	# 2-4
    loopRest()
    label(0)
    sprite('su033_01', 3)	# 5-7
    sprite('su033_02', 3)	# 8-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su033_03', 3)	# 11-13
    physicsXImpulse(0)
    sprite('su033_04', 3)	# 14-16

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('su300_00', 7)	# 1-7
    sprite('su300_01', 7)	# 8-14
    sprite('su300_02', 7)	# 15-21
    sprite('su300_03', 34)	# 22-55
    sprite('su300_04', 7)	# 56-62
    sprite('su300_05', 7)	# 63-69
    sprite('su300_06', 7)	# 70-76

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
    sprite('su252_04', 2)	# 32-33	 **attackbox here**
    SFX_0('005_swing_grap_2_2')
    GFX_0('suef_252_ForAComboFinal', -1)
    StartMultihit()
    sprite('su252_05', 30)	# 34-63	 **attackbox here**
    label(1)
    sprite('su252_05', 1)	# 64-64	 **attackbox here**
    sprite('su024_00', 5)	# 65-69
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('su024_01', 12)	# 70-81
    sprite('su024_02', 5)	# 82-86
    sprite('su024_03', 4)	# 87-90
    sprite('su024_04', 4)	# 91-94

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2004(1, 0)
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('su024_00', 2)	# 2-3
    sprite('su024_01', 3)	# 4-6
    sprite('su024_02', 3)	# 7-9
    sprite('su024_03', 3)	# 10-12
    sprite('su024_04', 3)	# 13-15
    sprite('su203_00', 2)	# 16-17
    sprite('su203_01', 3)	# 18-20
    sprite('su203_02', 3)	# 21-23
    GFX_0('suef_203', -1)
    SFX_3('suse_00')
    sprite('su203_03', 5)	# 24-28
    sprite('su203_04', 3)	# 29-31
    sprite('su203_05', 3)	# 32-34
    SFX_0('005_swing_grap_2_2')
    sprite('su203_06', 3)	# 35-37	 **attackbox here**
    GFX_0('suef_203_atk', -1)
    sprite('su203_07', 4)	# 38-41
    sprite('su203_08', 4)	# 42-45
    sprite('su203_09', 5)	# 46-50
    sprite('su203_10', 5)	# 51-55
    sprite('su203_11', 5)	# 56-60
    sprite('su203_12', 5)	# 61-65
    sprite('su203_13', 5)	# 66-70
    sprite('su203_14', 5)	# 71-75

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        PushbackX(12000)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtk4A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('su200_00', 2)	# 1-2
    Unknown1051(60)
    sprite('su200_01', 3)	# 3-5
    SFX_0('005_swing_grap_2_0')
    sprite('su200_02', 2)	# 6-7
    Unknown7009(0)
    sprite('su200_03', 5)	# 8-12	 **attackbox here**
    GFX_0('suef_200', -1)
    sprite('su200_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('su200_05', 1)	# 17-17
    sprite('su200_06', 1)	# 18-18

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirUntechableTime(19)
        AirPushbackY(20000)
        AirPushbackX(10000)
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
        Unknown2004(1, 0)
    sprite('su201_00', 2)	# 1-2
    sprite('su201_01', 3)	# 3-5
    SFX_0('005_swing_grap_2_1')
    sprite('su201_02', 3)	# 6-8
    Unknown7009(1)
    sprite('su201_03', 2)	# 9-10	 **attackbox here**
    sprite('su201_04', 4)	# 11-14	 **attackbox here**
    sprite('su201_05', 2)	# 15-16
    Recovery()
    Unknown2063()
    sprite('su201_06', 2)	# 17-18
    sprite('su201_07', 3)	# 19-21
    sprite('su201_08', 3)	# 22-24
    sprite('su201_09', 4)	# 25-28
    sprite('su201_10', 4)	# 29-32

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Hitstop(15)
        PushbackX(39900)
        AirPushbackX(18000)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown2004(1, 0)
    sprite('su202_00', 3)	# 1-3
    sprite('su202_01', 3)	# 4-6
    Unknown2015(150)
    sprite('su202_02', 4)	# 7-10
    sprite('su202_03', 2)	# 11-12
    SFX_0('005_swing_grap_2_2')
    sprite('su202_04', 2)	# 13-14	 **attackbox here**
    sprite('su202_05', 4)	# 15-18	 **attackbox here**
    sprite('su202_06', 4)	# 19-22
    Recovery()
    Unknown2063()
    sprite('su202_07', 4)	# 23-26
    sprite('su202_08', 3)	# 27-29
    Unknown2015(-1)
    sprite('su202_09', 2)	# 30-31
    sprite('su202_10', 2)	# 32-33
    sprite('su202_11', 2)	# 34-35
    sprite('su202_12', 2)	# 36-37

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirHitstunAnimation(9)
        AirPushbackX(30000)
        AirPushbackY(-40000)
        Unknown9190(1)
        Unknown9118(30)
        Unknown9310(10)
        AirUntechableTime(25)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown11056(0)
        Unknown2004(1, 0)
    sprite('su213_00', 3)	# 1-3
    sprite('su213_01', 3)	# 4-6
    sprite('su213_02', 2)	# 7-8
    GFX_0('suef_213', -1)
    Unknown2015(200)
    sprite('su213_03', 2)	# 9-10
    sprite('su213_04', 2)	# 11-12
    SFX_3('suse_00')
    sprite('su213_05', 2)	# 13-14
    GFX_0('suef_213_2', -1)
    physicsXImpulse(10000)
    SFX_0('005_swing_grap_2_2')
    Unknown7009(4)
    sprite('su213_06ex00', 2)	# 15-16	 **attackbox here**
    Unknown1019(200)
    sprite('su213_07', 2)	# 17-18
    sprite('su213_08', 1)	# 19-19	 **attackbox here**
    GFX_0('suef_213_3d', 0)
    StartMultihit()
    sprite('su213_08', 1)	# 20-20	 **attackbox here**
    physicsXImpulse(0)
    sprite('su213_08', 3)	# 21-23	 **attackbox here**
    DisableAttackRestOfMove()
    Recovery()
    Unknown2063()
    sprite('su213_09', 4)	# 24-27
    sprite('su213_10', 5)	# 28-32
    sprite('su213_11', 5)	# 33-37
    sprite('su213_12', 4)	# 38-41
    Unknown2015(-1)
    sprite('su213_13', 4)	# 42-45
    sprite('su213_14', 4)	# 46-49

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirUntechableTime(60)
        AirPushbackX(12000)
        AirPushbackY(32000)
        JumpCancel_(0)
        Unknown2004(1, 0)
        Unknown11044(1)
        Unknown30088(1)
    sprite('su203_00', 2)	# 1-2
    sprite('su203_01', 2)	# 3-4
    sprite('su203_02', 2)	# 5-6
    GFX_0('suef_203', -1)
    SFX_3('suse_00')
    sprite('su203_03', 4)	# 7-10
    sprite('su203_04', 3)	# 11-13
    Unknown2015(200)
    sprite('su203_05', 3)	# 14-16
    Unknown7009(2)
    SFX_0('005_swing_grap_2_2')
    sprite('su203_06', 3)	# 17-19	 **attackbox here**
    GFX_0('suef_203_atk', -1)
    Unknown2015(250)
    ScreenShake(15000, 15000)
    sprite('su203_07', 4)	# 20-23
    Recovery()
    Unknown2063()
    sprite('su203_08', 4)	# 24-27
    sprite('su203_09', 5)	# 28-32
    sprite('su203_10', 5)	# 33-37
    sprite('su203_11', 4)	# 38-41
    Unknown2015(-1)
    sprite('su203_12', 4)	# 42-45
    sprite('su203_13', 4)	# 46-49
    sprite('su203_14', 4)	# 50-53

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AirUntechableTime(27)
        AirPushbackX(9000)
        AirPushbackY(18000)
        PushbackX(12000)
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown1112('')
        Unknown2004(1, 0)
    sprite('su211_00', 3)	# 1-3
    sprite('su211_01', 2)	# 4-5
    Unknown2015(200)
    sprite('su211_02', 2)	# 6-7
    physicsXImpulse(40000)
    SFX_0('005_swing_grap_2_1')
    sprite('su211_03', 3)	# 8-10
    Unknown1019(20)
    GFX_0('suef_211', -1)
    Unknown7009(4)
    sprite('su211_04', 4)	# 11-14	 **attackbox here**
    ScreenShake(0, 3000)
    GFX_0('suef_211_foot', 0)
    GFX_0('suef_211_foot', 1)
    physicsXImpulse(0)
    SFX_0('213_bound_0')
    sprite('su211_04', 4)	# 15-18	 **attackbox here**
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('su211_05', 4)	# 19-22
    sprite('su211_06', 4)	# 23-26
    sprite('su211_12', 4)	# 27-30
    sprite('su211_13', 4)	# 31-34

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AirUntechableTime(27)
        AirPushbackX(9000)
        AirPushbackY(18000)
        PushbackX(12000)
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown2004(1, 0)
        Unknown2015(200)
    sprite('su211_05ex01', 5)	# 1-5
    sprite('su211_06ex01', 4)	# 6-9
    sprite('su211_07ex01', 2)	# 10-11
    physicsXImpulse(80000)
    Unknown2015(-1)
    SFX_0('005_swing_grap_2_1')
    sprite('su211_08ex01', 5)	# 12-16	 **attackbox here**
    AirPushbackY(20000)
    RefreshMultihit()
    ScreenShake(0, 9000)
    GFX_0('suef_211_2', -1)
    GFX_0('suef_211_foot2', 0)
    GFX_0('suef_211_foot2', 1)
    physicsXImpulse(0)
    Unknown1028(0)
    SFX_0('213_bound_0')
    sprite('su211_09ex01', 4)	# 17-20
    Recovery()
    Unknown2063()
    sprite('su211_10ex01', 4)	# 21-24
    sprite('su211_11ex01', 4)	# 25-28
    sprite('su211_12ex01', 4)	# 29-32
    sprite('su211_13ex01', 4)	# 33-36

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        HitLow(2)
    sprite('su231_00', 2)	# 1-2
    sprite('su231_01', 2)	# 3-4
    sprite('su231_01', 2)	# 5-6
    sprite('su231_02', 3)	# 7-9
    Unknown7009(3)
    SFX_0('006_swing_blade_1')
    sprite('su231_03', 3)	# 10-12	 **attackbox here**
    GFX_0('suef_231', -1)
    sprite('su231_04', 4)	# 13-16
    Recovery()
    Unknown2063()
    sprite('su231_05', 4)	# 17-20
    sprite('su231_06', 4)	# 21-24
    sprite('su231_07', 4)	# 25-28
    sprite('su231_08', 3)	# 29-31

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        AirUntechableTime(22)
        PushbackX(9900)
        Unknown11058('0000000001000000000000000000000000000000')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        Unknown2004(1, 0)
    sprite('su232_00', 3)	# 1-3
    sprite('su232_01', 3)	# 4-6
    Unknown1028(8000)
    sprite('su232_02', 3)	# 7-9
    Unknown7009(2)
    SFX_0('005_swing_grap_2_2')
    sprite('su232_03', 3)	# 10-12	 **attackbox here**
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    GFX_0('suef_232', -1)
    Unknown1084(1)
    sprite('su232_03', 2)	# 13-14	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('su232_04', 1)	# 15-15	 **attackbox here**
    PushbackX(30400)
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockJumpCancel(1)
    sprite('su232_04', 4)	# 16-19	 **attackbox here**
    HitOrBlockJumpCancel(1)
    setInvincible(0)
    sprite('su232_06', 4)	# 20-23
    Recovery()
    Unknown2063()
    sprite('su232_07', 5)	# 24-28
    sprite('su232_08', 5)	# 29-33
    sprite('su232_09', 5)	# 34-38
    sprite('su232_10', 3)	# 39-41

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(3)
        AttackP1(90)
        Unknown11092(1)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirUntechableTime(40)
        AirPushbackX(3000)
        AirPushbackY(16000)
        HitLow(2)
        Unknown2004(1, 0)
    sprite('su235_00', 2)	# 1-2
    sprite('su235_01', 3)	# 3-5
    Unknown2015(200)
    sprite('su235_02', 3)	# 6-8
    SFX_0('005_swing_grap_2_2')
    sprite('su235_03', 3)	# 9-11
    GFX_0('suef_235', -1)
    Unknown7009(5)
    sprite('su235_04', 2)	# 12-13	 **attackbox here**
    sprite('su235_05', 2)	# 14-15	 **attackbox here**
    sprite('su235_06', 2)	# 16-17
    sprite('su235_07', 2)	# 18-19
    sprite('su235_08', 2)	# 20-21
    SFX_0('005_swing_grap_2_2')
    sprite('su235_09', 2)	# 22-23
    GFX_0('suef_235_2', -1)
    sprite('su235_10', 4)	# 24-27	 **attackbox here**
    AttackLevel_(4)
    RefreshMultihit()
    AirPushbackX(8000)
    AirPushbackY(18000)
    sprite('su235_11', 4)	# 28-31
    Recovery()
    Unknown2063()
    sprite('su235_12', 4)	# 32-35
    sprite('su235_13', 4)	# 36-39
    sprite('su235_14', 5)	# 40-44
    Unknown2015(-1)
    sprite('su235_15', 5)	# 45-49
    sprite('su235_16', 4)	# 50-53

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        AirPushbackY(20000)
        Unknown9016(1)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('su251_00', 3)	# 1-3
    sprite('su251_01', 3)	# 4-6
    Unknown7009(1)
    sprite('su251_02', 2)	# 7-8
    GFX_0('suef_251', -1)
    sprite('su251_03', 2)	# 9-10
    SFX_0('006_swing_blade_1')
    sprite('su251_04', 4)	# 11-14	 **attackbox here**
    GFX_0('suef_251_3d', -1)
    sprite('su251_05', 4)	# 15-18
    Recovery()
    Unknown2063()
    sprite('su251_06', 4)	# 19-22
    sprite('su251_07', 4)	# 23-26
    sprite('su251_08', 4)	# 27-30
    sprite('su251_09', 3)	# 31-33
    sprite('su251_10', 3)	# 34-36

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AttackP1(80)
        AirPushbackY(20000)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('su250_00', 3)	# 1-3
    sprite('su250_01', 3)	# 4-6
    sprite('su250_02', 4)	# 7-10
    Unknown7009(0)
    SFX_0('005_swing_grap_2_0')
    sprite('su250_03', 4)	# 11-14	 **attackbox here**
    GFX_0('suef_250', -1)
    sprite('su250_04', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('su250_05', 3)	# 18-20
    sprite('su250_06', 3)	# 21-23
    sprite('su250_07', 3)	# 24-26
    sprite('su250_08', 3)	# 27-29

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        Damage(1700)
        AttackP1(80)
        AirHitstunAnimation(10)
        HitOrBlockCancel('NmlAtkAIR5BB')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_52:
                clearUponHandler(3)
                HitOverhead(0)
    sprite('su252_00', 3)	# 1-3
    sprite('su252_01', 1)	# 4-4
    GFX_0('suef_252', -1)
    sprite('su252_02', 2)	# 5-6
    SFX_0('005_swing_grap_2_2')
    sprite('su252_03', 2)	# 7-8
    Unknown7009(2)
    sprite('su252_04', 2)	# 9-10	 **attackbox here**
    sprite('su252_04', 2)	# 11-12	 **attackbox here**
    DisableAttackRestOfMove()
    sprite('su252_05', 3)	# 13-15	 **attackbox here**
    RefreshMultihit()
    AirUntechableTime(30)
    AirPushbackX(10000)
    AirPushbackY(-40000)
    sprite('su252_06', 4)	# 16-19
    Recovery()
    Unknown2063()
    sprite('su252_07', 4)	# 20-23
    sprite('su252_08', 4)	# 24-27
    sprite('su252_09', 4)	# 28-31
    sprite('su252_10', 4)	# 32-35
    sprite('su252_11', 3)	# 36-38

@State
def NmlAtkAIR5BB():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(80)
        AttackP2(80)
        AirHitstunAnimation(13)
        AirPushbackY(26000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('su253_00', 3)	# 1-3
    sprite('su253_01', 2)	# 4-5
    Unknown22004(9, 1)
    sprite('su253_02', 3)	# 6-8
    GFX_0('suef_253_3d', 103)
    SFX_3('suse_00')
    sprite('su253_03', 3)	# 9-11
    sprite('su253_04', 3)	# 12-14
    sprite('su253_05', 3)	# 15-17	 **attackbox here**
    sprite('su253_06', 3)	# 18-20	 **attackbox here**
    sprite('su253_07', 3)	# 21-23
    Recovery()
    Unknown2063()
    sprite('su253_08', 6)	# 24-29
    sprite('su253_09', 6)	# 30-35
    sprite('su253_10', 6)	# 36-41

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        Damage(1000)
        AttackP1(80)
        Unknown11092(1)
        AirHitstunAnimation(11)
        AirUntechableTime(45)
        Unknown9310(1)
        AirPushbackY(-44000)
        Hitstop(2)
        Unknown11001(0, -1, 2)
        Unknown11058('0100000000000000000000000000000000000000')
        DisableAttackRestOfMove()
        JumpCancel_(0)
        clearUponHandler(2)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                SLOT_52 = (SLOT_52 + (-1))
                if (not SLOT_52):
                    RefreshMultihit()

        def upon_ON_HIT_OR_BLOCK():
            SLOT_52 = 5
        Unknown2004(1, 0)
    sprite('su406_02', 3)	# 1-3
    sprite('su406_02', 1)	# 4-4
    Unknown1051(0)
    Unknown1015(15000)
    YAccel(20)
    Unknown1021(25000)
    setGravity(3000)
    callSubroutine('EmissionStart')
    Unknown30017('19000000')

    def upon_LANDING():
        clearUponHandler(3)
        sendToLabel(2)
        Unknown1084(1)
        Unknown8003(100, 1, 1)
        Unknown26('suef_406_roll_3d')
        RefreshMultihit()
        GroundedHitstunAnimation(11)
        Hitstop(11)
    sprite('su406_03', 1)	# 5-5
    tag_voice(1, 'bsu108_0', 'bsu108_1', 'bsu108_2', '')
    Unknown1019(80)
    sprite('su406_04', 2)	# 6-7
    Unknown1019(80)
    sprite('su406_05', 2)	# 8-9
    Unknown1019(80)
    sprite('su406_06ex01', 2)	# 10-11	 **attackbox here**
    Unknown1019(80)
    GFX_0('suef_406_roll_3d', 103)
    SFX_3('suse_02')
    SFX_0('006_swing_blade_2')
    sprite('su406_07ex01', 2)	# 12-13	 **attackbox here**
    sprite('su406_08ex01', 2)	# 14-15	 **attackbox here**
    Unknown2037(1)
    RefreshMultihit()
    SFX_0('006_swing_blade_2')
    sprite('su406_09ex01', 2)	# 16-17	 **attackbox here**
    label(1)
    sprite('su406_06ex01', 2)	# 18-19	 **attackbox here**
    Unknown1019(80)
    SFX_0('006_swing_blade_2')
    sprite('su406_07ex01', 2)	# 20-21	 **attackbox here**
    sprite('su406_08ex01', 2)	# 22-23	 **attackbox here**
    sprite('su406_09ex01', 2)	# 24-25	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('su406_10', 3)	# 26-28	 **attackbox here**
    HitOverhead(0)

    def upon_78():
        clearUponHandler(78)
        GFX_0('suef_406_OD', 0)
        SFX_0('016_explode_2')
    GFX_0('suef_406', 0)
    sprite('su406_11', 4)	# 29-32
    Recovery()
    Unknown2063()
    sprite('su406_12', 4)	# 33-36
    sprite('su406_13', 4)	# 37-40
    sprite('su406_14', 3)	# 41-43
    Unknown30017('e7ffffff')
    sprite('su406_15', 3)	# 44-46
    sprite('su406_16', 3)	# 47-49
    sprite('su406_17', 3)	# 50-52

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('su340_00', 3)	# 1-3
    sprite('su340_01', 1)	# 4-4
    tag_voice(1, 'bsu156_0', 'bsu156_1', '', '')
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su340_01', 2)	# 5-6
    sprite('su340_02', 3)	# 7-9
    sprite('su340_03', 3)	# 10-12
    sprite('su340_04', 2)	# 13-14
    GFX_0('suef_340', -1)
    sprite('su340_05', 2)	# 15-16
    sprite('su340_06', 2)	# 17-18
    SFX_0('005_swing_grap_2_2')
    sprite('su340_07', 3)	# 19-21
    physicsXImpulse(20000)
    sprite('su340_08', 1)	# 22-22	 **attackbox here**
    physicsXImpulse(0)
    GFX_1('suef_340foot', 0)
    GFX_0('suef_340_rock', 0)
    GFX_0('suef_406_crack', 0)
    ScreenShake(15000, 25000)
    SFX_0('209_down_normal_1')
    sprite('su340_08', 2)	# 23-24	 **attackbox here**
    Unknown2004(1, 0)
    DisableAttackRestOfMove()
    Unknown3029(0)
    sprite('su340_09', 3)	# 25-27
    sprite('su340_10', 3)	# 28-30
    sprite('su340_11', 3)	# 31-33
    sprite('su340_12', 3)	# 34-36
    Unknown30017('e7ffffff')
    sprite('su340_13', 3)	# 37-39
    sprite('su340_14ex01', 3)	# 40-42
    sprite('su340_15ex01', 3)	# 43-45
    sprite('su340_16ex01', 3)	# 46-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)
        Unknown2004(1, 0)
    sprite('su340_09', 3)	# 1-3
    Unknown1084(1)
    Unknown3029(0)
    sprite('su340_10', 2)	# 4-5
    sprite('su340_11', 2)	# 6-7
    sprite('su340_12', 2)	# 8-9
    Unknown30017('e7ffffff')
    sprite('su340_13', 2)	# 10-11
    sprite('su340_14', 2)	# 12-13
    sprite('su340_15', 2)	# 14-15
    sprite('su340_16', 2)	# 16-17
    sprite('su203_00ex00', 2)	# 18-19
    sprite('su203_01ex00', 2)	# 20-21
    sprite('su203_02ex00', 2)	# 22-23
    sprite('su203_03ex00', 3)	# 24-26
    sprite('su203_04ex00', 3)	# 27-29
    tag_voice(0, 'bsu157_0', 'bsu157_1', '', '')
    sprite('su313_06ex00', 3)	# 30-32	 **attackbox here**
    GFX_0('suef_440', 0)
    GFX_0('suef_440_smoke', -1)
    SFX_3('suse_02')
    sprite('su313_07ex00', 2)	# 33-34
    sprite('su313_08ex00', 2)	# 35-36
    sprite('su313_09ex00', 2)	# 37-38
    sprite('su313_10ex00', 2)	# 39-40
    sprite('su313_11ex00', 2)	# 41-42
    sprite('su313_12ex00', 2)	# 43-44
    sprite('su313_13ex00', 2)	# 45-46
    sprite('su000_00', 7)	# 47-53
    sprite('su000_01', 7)	# 54-60
    sprite('su000_02', 7)	# 61-67
    sprite('su000_03', 7)	# 68-74
    sprite('su000_04', 7)	# 75-81
    sprite('su000_05', 7)	# 82-88
    sprite('su000_06', 7)	# 89-95
    sprite('su000_07', 7)	# 96-102
    sprite('su000_08', 7)	# 103-109
    sprite('su000_09', 7)	# 110-116
    label(10)
    sprite('su000_00', 7)	# 117-123
    sprite('su000_01', 7)	# 124-130
    sprite('su000_02', 7)	# 131-137
    sprite('su000_03', 7)	# 138-144
    sprite('su000_04', 7)	# 145-151
    sprite('su000_05', 7)	# 152-158
    sprite('su000_06', 7)	# 159-165
    sprite('su000_07', 7)	# 166-172
    sprite('su000_08', 7)	# 173-179
    sprite('su000_09', 7)	# 180-186
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 187-187

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        Unknown2004(1, 0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('su405_03', 4)	# 1-4
    GFX_0('suef_405', 0)
    GFX_0('suef_405_crack', 0)
    sprite('su405_06', 4)	# 5-8
    sprite('su405_07', 3)	# 9-11
    Unknown26('suef_405')
    GFX_0('suef_405kick_SP', -1)
    SFX_3('suse_04')
    SFX_0('209_down_normal_0')
    sprite('su405_08', 3)	# 12-14
    sprite('su405_09', 3)	# 15-17	 **attackbox here**
    sprite('su405_10', 3)	# 18-20
    sprite('su405_11', 3)	# 21-23
    sprite('su405_12', 3)	# 24-26
    sprite('su405_13', 3)	# 27-29
    sprite('su405_14', 3)	# 30-32
    sprite('su405_15', 3)	# 33-35
    sprite('su000_00', 7)	# 36-42
    sprite('su000_01', 7)	# 43-49
    sprite('su000_02', 7)	# 50-56
    sprite('su000_03', 7)	# 57-63
    sprite('su000_04', 7)	# 64-70
    sprite('su000_05', 7)	# 71-77
    sprite('su000_06', 7)	# 78-84
    sprite('su000_07', 7)	# 85-91
    sprite('su000_08', 7)	# 92-98
    sprite('su000_09', 7)	# 99-105
    label(0)
    sprite('su000_00', 7)	# 106-112
    sprite('su000_01', 7)	# 113-119
    sprite('su000_02', 7)	# 120-126
    sprite('su000_03', 7)	# 127-133
    sprite('su000_04', 7)	# 134-140
    sprite('su000_05', 7)	# 141-147
    sprite('su000_06', 7)	# 148-154
    sprite('su000_07', 7)	# 155-161
    sprite('su000_08', 7)	# 162-168
    sprite('su000_09', 7)	# 169-175
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 176-176

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        Unknown2004(1, 0)
        Unknown1084(1)
    sprite('su203_00', 2)	# 1-2
    sprite('su203_01', 3)	# 3-5
    physicsXImpulse(-18000)
    sprite('su203_02', 3)	# 6-8
    GFX_0('suef_203', -1)
    SFX_3('suse_00')
    Unknown1019(50)
    sprite('su203_03', 5)	# 9-13
    Unknown1019(30)
    sprite('su203_04', 3)	# 14-16
    physicsXImpulse(0)
    sprite('su203_05', 3)	# 17-19
    SFX_0('005_swing_grap_2_2')
    sprite('su203_06', 3)	# 20-22	 **attackbox here**
    GFX_0('suef_203_atk', -1)
    tag_voice(0, 'bsu158_0', 'bsu158_1', '', '')
    sprite('su203_07', 4)	# 23-26
    sprite('su203_08', 4)	# 27-30
    sprite('su203_09', 5)	# 31-35
    sprite('su203_10', 5)	# 36-40
    sprite('su203_11', 5)	# 41-45
    sprite('su203_12', 5)	# 46-50
    sprite('su203_13', 5)	# 51-55
    sprite('su203_14', 5)	# 56-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        Unknown2004(1, 0)
        Unknown1084(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('su000_00', 7)	# 1-7
    sprite('su000_01', 7)	# 8-14
    sprite('su000_02', 7)	# 15-21
    sprite('su000_03', 7)	# 22-28
    sprite('su000_04', 7)	# 29-35
    sprite('su000_05', 7)	# 36-42
    sprite('su000_06', 7)	# 43-49
    sprite('su000_07', 7)	# 50-56
    sprite('su000_08', 7)	# 57-63
    sprite('su000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su203_00', 2)	# 71-72
    sprite('su203_01', 3)	# 73-75
    physicsXImpulse(-18000)
    sprite('su203_02', 3)	# 76-78
    GFX_0('suef_203', -1)
    SFX_3('suse_00')
    Unknown1019(50)
    sprite('su203_03', 5)	# 79-83
    Unknown1019(30)
    sprite('su203_04', 3)	# 84-86
    physicsXImpulse(0)
    sprite('su203_05', 3)	# 87-89
    SFX_0('005_swing_grap_2_2')
    sprite('su203_06', 3)	# 90-92	 **attackbox here**
    GFX_0('suef_203_atk', -1)
    tag_voice(0, 'bsu158_0', 'bsu158_1', '', '')
    sprite('su203_07', 4)	# 93-96
    sprite('su203_08', 4)	# 97-100
    sprite('su203_09', 5)	# 101-105
    sprite('su203_10', 5)	# 106-110
    sprite('su203_11', 5)	# 111-115
    sprite('su203_12', 5)	# 116-120
    sprite('su203_13', 5)	# 121-125
    sprite('su203_14', 5)	# 126-130

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
    sprite('null', 11)	# 1-11
    sprite('null', 10)	# 12-21
    Unknown30081('')
    sprite('su403_09', 2)	# 22-23
    Unknown1086(22)
    teleportRelativeX(-1000000)
    SLOT_12 = SLOT_19
    Unknown1019(7)
    sprite('su403_10', 2)	# 24-25
    Unknown8006(100, 1, 0)
    sprite('su403_09', 2)	# 26-27
    Unknown8006(100, 1, 0)
    sprite('su403_10', 2)	# 28-29
    Unknown8006(100, 1, 0)
    sprite('su403_09', 2)	# 30-31
    Unknown8006(100, 1, 0)
    sprite('su403_12', 3)	# 32-34	 **attackbox here**
    StartMultihit()
    Unknown1019(10)
    sprite('su403_13', 3)	# 35-37
    GFX_0('suef_403_hand02', -1)
    Unknown1019(30)
    Unknown8010(100, 1, 0)
    sprite('su403_14', 2)	# 38-39
    sprite('su403_15', 2)	# 40-41
    GFX_0('suef_403_smash02', -1)
    Unknown26('suef_403_hand02')
    sprite('su403_16', 3)	# 42-44	 **attackbox here**
    Unknown1084(1)
    sprite('su403_17', 4)	# 45-48
    sprite('su403_18', 4)	# 49-52
    sprite('su403_19', 4)	# 53-56
    sprite('su403_20', 4)	# 57-60
    Unknown3029(0)
    sprite('su403_21', 4)	# 61-64
    sprite('su403_22', 4)	# 65-68
    sprite('su403_23', 4)	# 69-72
    sprite('su403_24', 4)	# 73-76
    sprite('su403_25', 6)	# 77-82
    Unknown30017('f4ffffff')
    sprite('su403_26', 6)	# 83-88
    sprite('su403_27', 6)	# 89-94
    sprite('su403_28', 6)	# 95-100

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('su212_00', 1)	# 1-1
    sprite('su212_01', 1)	# 2-2
    sprite('su212_02', 1)	# 3-3
    sprite('su212_03', 2)	# 4-5
    sprite('su212_04', 2)	# 6-7
    GFX_0('suef_212_02', -1)
    sprite('su212_05', 2)	# 8-9
    SFX_0('005_swing_grap_2_2')
    sprite('su212_06', 2)	# 10-11
    sprite('su212_07', 4)	# 12-15	 **attackbox here**
    sprite('su212_08', 5)	# 16-20
    sprite('su212_09', 4)	# 21-24
    sprite('su212_10', 4)	# 25-28
    sprite('su212_11', 4)	# 29-32
    sprite('su212_12', 3)	# 33-35
    sprite('su000_00', 7)	# 36-42
    sprite('su000_01', 7)	# 43-49
    sprite('su000_02', 7)	# 50-56
    sprite('su000_03', 7)	# 57-63
    sprite('su000_04', 7)	# 64-70
    sprite('su000_05', 7)	# 71-77
    sprite('su000_06', 7)	# 78-84
    sprite('su000_07', 7)	# 85-91
    sprite('su000_08', 7)	# 92-98
    sprite('su000_09', 7)	# 99-105

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('su203_00', 2)	# 1-2
    sprite('su203_01', 3)	# 3-5
    physicsXImpulse(-18000)
    sprite('su203_02', 3)	# 6-8
    GFX_0('suef_203', -1)
    SFX_3('suse_00')
    Unknown1019(50)
    sprite('su203_03', 5)	# 9-13
    Unknown1019(30)
    sprite('su203_04', 3)	# 14-16
    physicsXImpulse(0)
    sprite('su203_05', 3)	# 17-19
    SFX_0('005_swing_grap_2_2')
    sprite('su203_06', 3)	# 20-22	 **attackbox here**
    GFX_0('suef_203_atk', -1)
    sprite('su203_07', 4)	# 23-26
    sprite('su203_08', 4)	# 27-30
    sprite('su203_09', 5)	# 31-35
    sprite('su203_10', 5)	# 36-40
    sprite('su203_11', 5)	# 41-45
    sprite('su203_12', 5)	# 46-50
    sprite('su203_13', 5)	# 51-55
    sprite('su203_14', 5)	# 56-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        Unknown2004(1, 0)
        Unknown1084(1)
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('su000_00', 7)	# 1-7
    sprite('su000_01', 7)	# 8-14
    sprite('su000_02', 7)	# 15-21
    sprite('su000_03', 7)	# 22-28
    sprite('su000_04', 7)	# 29-35
    sprite('su000_05', 7)	# 36-42
    sprite('su000_06', 7)	# 43-49
    sprite('su000_07', 7)	# 50-56
    sprite('su000_08', 7)	# 57-63
    sprite('su000_09', 7)	# 64-70
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su203_00', 2)	# 71-72
    sprite('su203_01', 3)	# 73-75
    physicsXImpulse(-18000)
    sprite('su203_02', 3)	# 76-78
    GFX_0('suef_203', -1)
    SFX_3('suse_00')
    Unknown1019(50)
    sprite('su203_03', 5)	# 79-83
    Unknown1019(30)
    sprite('su203_04', 3)	# 84-86
    physicsXImpulse(0)
    sprite('su203_05', 3)	# 87-89
    SFX_0('005_swing_grap_2_2')
    sprite('su203_06', 3)	# 90-92	 **attackbox here**
    GFX_0('suef_203_atk', -1)
    sprite('su203_07', 4)	# 93-96
    sprite('su203_08', 4)	# 97-100
    sprite('su203_09', 5)	# 101-105
    sprite('su203_10', 5)	# 106-110
    sprite('su203_11', 5)	# 111-115
    sprite('su203_12', 5)	# 116-120
    sprite('su203_13', 5)	# 121-125
    sprite('su203_14', 5)	# 126-130

@Subroutine
def ThrowApproachInit():
    physicsXImpulse(8250)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_18 == 7):
            Unknown8007(100, 1, 1)
            physicsXImpulse(10000)
        if (SLOT_18 >= 7):
            Unknown1015(440)
            if (SLOT_12 >= 28000):
                SLOT_12 = 28000
        if (SLOT_18 >= 16):
            Unknown1015(12000)
            if (SLOT_12 >= 28000):
                SLOT_12 = 28000
        if (SLOT_18 >= 17):
            Unknown1015(440)
            if (SLOT_12 >= 28000):
                SLOT_12 = 28000
        if (SLOT_18 >= 25):
            sendToLabel(1)
        if (SLOT_18 >= 3):
            if (SLOT_19 < 180000):
                sendToLabel(1)

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('su032_15', 3)	# 1-3
    sprite('su032_14', 3)	# 4-6
    sprite('su032_13', 3)	# 7-9
    sprite('su032_12', 3)	# 10-12
    sprite('su032_11', 3)	# 13-15
    sprite('su032_00', 2)	# 16-17
    label(0)
    sprite('su032_01', 4)	# 18-21
    sprite('su032_02', 4)	# 22-25
    sprite('su032_03', 4)	# 26-29
    sprite('su032_04', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('su032_05', 4)	# 34-37
    sprite('su032_06', 4)	# 38-41
    sprite('su032_07', 4)	# 42-45
    sprite('su032_08', 4)	# 46-49
    Unknown8006(100, 1, 1)
    sprite('su032_09', 4)	# 50-53
    sprite('su032_10', 4)	# 54-57
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su310_00', 1)	# 58-58
    clearUponHandler(3)
    Unknown1019(10)
    sprite('su310_01', 2)	# 59-60
    sprite('su310_02', 3)	# 61-63	 **attackbox here**
    Unknown1084(1)
    sprite('su310_03', 3)	# 64-66
    SFX_0('010_swing_sword_1')
    sprite('su310_04', 3)	# 67-69
    sprite('su310_05', 3)	# 70-72
    SFX_1('bsu154')
    sprite('su310_06', 8)	# 73-80
    sprite('su310_07', 3)	# 81-83
    sprite('su310_08', 3)	# 84-86

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(15)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(6500)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(1500)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11001(-1, -1, -1)
        Unknown9310(10)
        StarterRating(2)
        Unknown11072(1, 150000, 150000)
        JumpCancel_(0)
        Unknown13024(0)
        Unknown11080(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('ThrowExe')
        Unknown2004(1, 0)
    sprite('su310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    DisableAttackRestOfMove()
    Unknown5003(1)
    sprite('su311_00', 4)	# 4-7
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_01', 20)	# 8-27	 **attackbox here**
    Unknown5000(28, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23011(1)
    ScreenShake(5000, 10000)
    GFX_1('ef_hitmd', 0)
    Unknown36(22)
    Unknown8004(104, 1, 1)
    Unknown8003(104, 1, 1)
    Unknown35()
    sprite('su311_02', 6)	# 28-33
    Unknown5000(29, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_03', 6)	# 34-39
    Unknown5000(27, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_04', 6)	# 40-45
    Unknown5000(25, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_05', 6)	# 46-51
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_06', 6)	# 52-57
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_07', 10)	# 58-67	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su311_07', 1)	# 68-68	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    RefreshMultihit()
    sprite('su311_08', 6)	# 69-74
    sprite('su311_09', 10)	# 75-84
    sprite('su311_10', 4)	# 85-88
    SFX_1('bsu153')
    SFX_0('005_swing_grap_2_2')
    sprite('su311_11', 4)	# 89-92	 **attackbox here**
    GFX_0('suef_311', -1)
    RefreshMultihit()
    AttackLevel_(5)
    Damage(2000)
    AttackP2(50)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(2000)
    AirPushbackY(39000)
    Unknown9095()
    Hitstop(15)
    Unknown11001(0, 0, 5)
    Unknown9311()
    Unknown11072(0, 0, 0)
    Unknown11080(0)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')

    def upon_11():
        JumpCancel_(1)
    ScreenShake(15000, 30000)
    sprite('su311_12', 5)	# 93-97
    sprite('su311_13', 5)	# 98-102
    sprite('su311_14', 5)	# 103-107
    sprite('su311_15', 5)	# 108-112
    sprite('su311_16', 5)	# 113-117
    sprite('su311_17', 5)	# 118-122

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('su032_15', 3)	# 1-3
    sprite('su032_14', 3)	# 4-6
    sprite('su032_13', 3)	# 7-9
    sprite('su032_12', 3)	# 10-12
    sprite('su032_11', 3)	# 13-15
    sprite('su032_00', 2)	# 16-17
    label(0)
    sprite('su032_01', 4)	# 18-21
    sprite('su032_02', 4)	# 22-25
    sprite('su032_03', 4)	# 26-29
    sprite('su032_04', 4)	# 30-33
    Unknown8006(100, 1, 1)
    sprite('su032_05', 4)	# 34-37
    sprite('su032_06', 4)	# 38-41
    sprite('su032_07', 4)	# 42-45
    sprite('su032_08', 4)	# 46-49
    Unknown8006(100, 1, 1)
    sprite('su032_09', 4)	# 50-53
    sprite('su032_10', 4)	# 54-57
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su310_00', 1)	# 58-58
    clearUponHandler(3)
    Unknown1019(10)
    sprite('su310_01', 2)	# 59-60
    sprite('su310_02', 3)	# 61-63	 **attackbox here**
    Unknown1084(1)
    sprite('su310_03', 3)	# 64-66
    SFX_0('010_swing_sword_1')
    sprite('su310_04', 3)	# 67-69
    sprite('su310_05', 3)	# 70-72
    SFX_1('bsu154')
    sprite('su310_06', 8)	# 73-80
    sprite('su310_07', 3)	# 81-83
    sprite('su310_08', 3)	# 84-86

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackX(-6500)
        AirPushbackY(12000)
        YImpluseBeforeWallbounce(1500)
        AirUntechableTime(60)
        Hitstop(0)
        Unknown11072(1, -110000, 120000)
        JumpCancel_(0)
        Unknown11080(1)
        Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
        Unknown11069('BackThrowExe')
        Unknown13021(1)
        Unknown21005(1)
    sprite('su310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    DisableAttackRestOfMove()
    Unknown5003(1)
    sprite('su313_00', 6)	# 4-9
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su313_01', 6)	# 10-15
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su313_02', 6)	# 16-21
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su313_03', 15)	# 22-36
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su313_04', 17)	# 37-53	 **attackbox here**
    RefreshMultihit()
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su313_05', 6)	# 54-59
    SFX_1('bsu153')
    sprite('su313_06', 3)	# 60-62	 **attackbox here**
    ScreenShake(15000, 0)
    RefreshMultihit()
    GFX_0('suef_313', 0)
    GFX_0('suef_313_smoke', -1)
    SFX_3('suse_02')
    AttackLevel_(5)
    Damage(2000)
    AttackP2(50)
    GroundedHitstunAnimation(12)
    AirHitstunAnimation(12)
    AirPushbackX(120000)
    AirPushbackY(8000)
    Unknown11099(1)
    Unknown9178(1)
    WallbounceReboundTime(20)
    AirHitstunAfterWallbounce(60)
    Unknown9362(1)
    Unknown9364(40)
    Hitstop(13)
    Unknown11072(0, 0, 0)
    Unknown11080(0)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11069('')

    def upon_11():
        JumpCancel_(1)
    sprite('su313_07', 3)	# 63-65
    sprite('su313_08', 3)	# 66-68
    sprite('su313_09', 3)	# 69-71
    sprite('su313_07', 3)	# 72-74
    sprite('su313_08', 3)	# 75-77
    sprite('su313_10', 2)	# 78-79
    sprite('su313_11', 2)	# 80-81
    sprite('su313_12', 2)	# 82-83
    sprite('su313_13', 2)	# 84-85

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2500)
        AirPushbackX(10000)
        AirPushbackY(40000)
        YImpluseBeforeWallbounce(2300)
        AirUntechableTime(70)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
    sprite('su401_00', 3)	# 1-3
    sprite('su401_01', 1)	# 4-4
    GFX_0('suef_401handaura', -1)
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su401_02', 2)	# 5-6
    tag_voice(1, 'bsu202_0', 'bsu202_1', 'bsu202_2', '')
    sprite('su401_03', 4)	# 7-10
    sprite('su401_04', 1)	# 11-11
    sprite('su401_05', 3)	# 12-14	 **attackbox here**
    ScreenShake(10000, 25000)
    GFX_0('suef_401', -1)
    SFX_0('016_explode_1')
    SFX_0('209_down_normal_1')
    sprite('su401_06', 3)	# 15-17
    sprite('su401_07', 3)	# 18-20
    sprite('su401_08', 3)	# 21-23
    setInvincible(0)
    sprite('su401_06', 3)	# 24-26
    sprite('su401_07', 3)	# 27-29
    sprite('su401_08', 3)	# 30-32
    sprite('su401_09', 3)	# 33-35
    sprite('su401_10', 3)	# 36-38
    sprite('su401_11', 3)	# 39-41
    Unknown2015(-1)
    sprite('su401_12', 3)	# 42-44
    sprite('su401_13', 4)	# 45-48
    Unknown30017('e7ffffff')
    sprite('su401_14', 4)	# 49-52
    sprite('su401_15', 4)	# 53-56
    sprite('su401_16', 4)	# 57-60

@State
def Assault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(1800)
        AttackP1(80)
        hitstun(23)
        AirUntechableTime(30)
        AirPushbackX(24000)
        AirPushbackY(15000)
        Unknown11056(0)

        def upon_ON_HIT_OR_BLOCK():
            sendToLabel(1)
    sprite('su400_00', 3)	# 1-3
    sprite('su400_01', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    Unknown26('suef_aura')
    tag_voice(1, 'bsu200_0', 'bsu200_1', 'bsu200_2', '')
    sprite('su400_02', 3)	# 7-9
    sprite('su400_03', 3)	# 10-12
    Unknown8004(100, 1, 1)
    GFX_0('suef_400_particle2', -1)
    sprite('su400_04', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(50000)
    Unknown2015(250)
    SFX_0('000_airdash_1')
    GFX_0('suef_400_aura3', 0)
    sprite('su400_05', 3)	# 15-17	 **attackbox here**
    Unknown8006(100, 1, 0)
    GFX_0('suef_400', -1)
    sprite('su400_06', 2)	# 18-19	 **attackbox here**
    sprite('su400_06', 1)	# 20-20	 **attackbox here**
    sprite('su400_05', 3)	# 21-23	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('su400_06', 3)	# 24-26	 **attackbox here**
    label(1)
    sprite('su400_07', 3)	# 27-29
    Unknown26('suef_400')
    GFX_0('suef_400_aura2', 0)
    clearUponHandler(10)
    clearUponHandler(12)
    Unknown8006(100, 1, 0)
    Recovery()
    sprite('su400_21', 3)	# 30-32
    Unknown26('suef_400_particle2')
    Unknown1019(60)
    Unknown2015(-1)
    Unknown8006(100, 1, 0)
    sprite('su032_11', 3)	# 33-35
    Unknown1019(60)
    Unknown8010(100, 1, 1)
    Unknown30017('e7ffffff')
    sprite('su032_12', 3)	# 36-38
    Unknown1084(1)
    Unknown8010(100, 1, 1)
    sprite('su032_13', 2)	# 39-40
    sprite('su032_14', 2)	# 41-42
    sprite('su032_15', 2)	# 43-44

@State
def LongAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(5)
        Damage(2700)
        AttackP1(80)
        Hitstop(15)
        GroundedHitstunAnimation(13)
        AirHitstunAnimation(13)
        AirPushbackX(30000)
        AirPushbackY(38000)
        AirUntechableTime(45)
        Unknown9016(1)
        Unknown11056(0)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown2004(1, 0)
    sprite('su402_00', 3)	# 1-3
    GFX_0('suef_402', -1)
    sprite('su402_01', 1)	# 4-4
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    sprite('su402_01', 2)	# 5-6
    sprite('su402_02', 3)	# 7-9
    tag_voice(1, 'bsu208_0', 'bsu208_1', 'bsu208_2', '')
    sprite('su402_03', 2)	# 10-11
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su402_04', 2)	# 12-13
    Unknown2015(200)
    SFX_3('suse_05')
    SFX_3('suse_02')
    SFX_0('006_swing_blade_2')
    sprite('su402_05', 2)	# 14-15
    sprite('su402_06', 3)	# 16-18	 **attackbox here**
    Unknown8003(100, 1, 0)
    DisableAttackRestOfMove()
    sprite('su402_07', 3)	# 19-21	 **attackbox here**
    RefreshMultihit()
    sprite('su402_08', 3)	# 22-24
    Recovery()
    sprite('su402_09', 3)	# 25-27
    sprite('su402_10', 3)	# 28-30
    sprite('su402_11', 4)	# 31-34
    Unknown30017('e7ffffff')
    sprite('su402_12', 4)	# 35-38
    Unknown2015(-1)
    sprite('su402_13', 4)	# 39-42
    sprite('su402_14', 3)	# 43-45

@State
def AssaultThrow():

    def upon_IMMEDIATE():
        Unknown17011('AssaultThrowExe', 2, 0, 0)
        Unknown11032('ffffffffffffffffd0fb010000000000')
        Unknown11054(70000)
        Unknown11002(-1)
        SLOT_59 = 0

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 200000)
            if op(5, 2, 0, 2, 52):
                clearUponHandler(3)
                sendToLabel(1)
            if (not SLOT_158):
                SLOT_59 = 1
        setInvincible(1)
        Unknown22019('0000000000000000000000000000000001000000')
        Unknown2004(1, 0)
    sprite('su403_00', 3)	# 1-3
    sprite('su403_01', 2)	# 4-5
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    Unknown3029(1)
    Unknown3070(1)
    Unknown3071(7)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    tag_voice(1, 'bsu206_0', 'bsu206_1', 'bsu206_2', '')
    sprite('su403_02', 3)	# 6-8
    sprite('su403_03', 3)	# 9-11
    sprite('su403_01', 3)	# 12-14
    sprite('su403_02', 3)	# 15-17
    sprite('su403_03', 3)	# 18-20
    sprite('su403_01', 3)	# 21-23
    sprite('su403_02', 3)	# 24-26
    sprite('su403_04', 3)	# 27-29
    physicsXImpulse(50000)
    Unknown2015(200)
    SFX_0('000_airdash_2')
    sprite('su403_05', 4)	# 30-33	 **attackbox here**
    GFX_1('suef_403dash', -1)
    sprite('su403_06', 4)	# 34-37	 **attackbox here**
    SLOT_52 = 1
    sprite('su403_05', 4)	# 38-41	 **attackbox here**
    sprite('su403_06', 4)	# 42-45	 **attackbox here**
    SFX_0('010_swing_sword_1')
    label(1)
    sprite('su403_29', 4)	# 46-49
    setInvincible(0)
    clearUponHandler(3)
    Unknown1019(60)
    sprite('su403_30', 4)	# 50-53
    Unknown1019(60)
    sprite('su233_05', 4)	# 54-57
    Unknown1019(60)
    Unknown18009(1)
    Unknown30017('f4ffffff')
    Unknown8003(100, 1, 1)
    sprite('su233_06', 4)	# 58-61
    Unknown1019(60)
    Unknown3029(0)
    sprite('su233_07', 4)	# 62-65
    Unknown1019(60)
    sprite('su233_08', 4)	# 66-69
    Unknown1019(60)
    sprite('su233_09', 4)	# 70-73
    Unknown1019(0)
    sprite('su233_10', 3)	# 74-76
    sprite('su233_11', 3)	# 77-79
    sprite('su233_12', 3)	# 80-82

@State
def AssaultThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        Unknown11069('AssaultThrowExe')
        AttackLevel_(4)
        Damage(1900)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirUntechableTime(60)
        AirPushbackX(90000)
        AirPushbackY(20000)
        Unknown9178(0)
        WallbounceReboundTime(25)
        AirHitstunAfterWallbounce(40)
        Unknown9362(1)
        Unknown9364(40)
        Unknown9310(15)
        YImpluseBeforeWallbounce(1000)
        Unknown11064(1)
        MinimumDamagePct(10)
        Unknown30065(0)
        Unknown13024(0)
        Unknown14083(0)
        callSubroutine('EmissionStart')
        Unknown30016('ff000000')
        Unknown20000(1)
        Unknown2004(1, 0)
        Unknown2037(20)

        def upon_CLEAR_OR_EXIT():
            if (SLOT_25 < 250000):
                clearUponHandler(3)
                clearUponHandler(17)
                Unknown2037(0)
                sendToLabel(2)
            if (SLOT_59 == 1):
                YImpluseBeforeWallbounce(2000)
                clearUponHandler(3)
                clearUponHandler(17)
                Unknown2037(2)
                Unknown20000(0)
        loopRelated(17, 80)

        def upon_17():
            clearUponHandler(3)
            clearUponHandler(17)
            Unknown2037(0)
            sendToLabel(2)
    sprite('su403_06', 1)	# 1-1	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0100000004000000040000000000000000000000')
    DisableAttackRestOfMove()
    Unknown2015(140)
    physicsXImpulse(20000)
    GFX_0('suef_403_aura', 103)
    Unknown3029(1)
    Unknown3070(0)
    Unknown3071(10)
    Unknown3072('80000000000000000000000000000000')
    Unknown3073('00000000000000000000000000000000')
    GFX_0('suef_403_camera', 100)
    sprite('su403_07', 2)	# 2-3
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown21015('737565665f3430335f63616d6572610000000000000000000000000000000000bf0f000000000000')
    sprite('su403_08', 3)	# 4-6
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    physicsXImpulse(50000)
    label(1)
    sprite('su403_09', 2)	# 7-8
    Unknown5000(11, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    SFX_0('015_blaze_0')
    sprite('su403_10', 2)	# 9-10
    Unknown5000(11, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    loopRest()
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(1)
    label(2)
    sprite('su403_10', 2)	# 11-12
    Unknown20000(0)
    Unknown5000(11, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su403_11', 2)	# 13-14
    Unknown5000(11, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    physicsXImpulse(0)
    Unknown1028(0)
    Unknown26('suef_403_aura')
    sprite('su403_12', 12)	# 15-26	 **attackbox here**
    Unknown5000(11, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    Unknown8008(0, 0, 0)
    Unknown2015(140)
    RefreshMultihit()
    ScreenShake(10000, 5000)
    sprite('su403_13', 4)	# 27-30
    GFX_0('suef_403_hand', -1)
    sprite('su403_14', 4)	# 31-34
    sprite('su403_15', 5)	# 35-39
    Unknown2015(150)
    Unknown26('suef_403_hand')
    GFX_0('suef_403_smash', -1)
    sprite('su403_16', 4)	# 40-43	 **attackbox here**
    GFX_0('suef_403_smoke', -1)
    Unknown8008(0, 0, 0)
    RefreshMultihit()
    AirHitstunAnimation(12)
    GroundedHitstunAnimation(12)
    AirPushbackX(50000)
    AirPushbackY(40000)
    AttackP2(50)
    Unknown9178(0)
    Unknown11102(1)
    Unknown11069('')
    Unknown11064(0)
    if (SLOT_59 == 1):
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        AirPushbackY(15000)
        Unknown9202(40)
    ScreenShake(20000, 10000)
    tag_voice(0, 'bsu207_0', 'bsu207_1', 'bsu207_2', '')
    SFX_0('016_explode_2')
    SFX_0('016_explode_2')
    sprite('su403_17', 4)	# 44-47
    Unknown14083(1)
    sprite('su403_18', 4)	# 48-51
    sprite('su403_19', 4)	# 52-55
    sprite('su403_20', 4)	# 56-59
    Unknown3029(0)
    sprite('su403_21', 4)	# 60-63
    sprite('su403_22', 4)	# 64-67
    sprite('su403_23', 4)	# 68-71
    sprite('su403_24', 4)	# 72-75
    sprite('su403_25', 6)	# 76-81
    Unknown30017('f4ffffff')
    sprite('su403_26', 6)	# 82-87
    sprite('su403_27', 6)	# 88-93
    sprite('su403_28', 6)	# 94-99

@State
def RushAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(800)
        AttackP1(80)
        AttackP2(75)
        ChipDamagePct(15)
        Hitstop(3)
        Unknown11001(-1, -1, 2)
        AirUntechableTime(35)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(9)
        AirPushbackX(10000)
        AirPushbackY(10000)
        PushbackX(12000)
        Unknown9142(22)
        Unknown9132(22)
        Unknown9144(22)
        Unknown11034(0)
        ProjectileDurabilityLvl(2)
        Unknown11057(600)
        Unknown11110(30)

        def upon_CLEAR_OR_EXIT():
            if CheckInput(0xa):
                Unknown2037(1)
            else:
                Unknown2037(0)
            SLOT_52 = (SLOT_52 + 1)
            if (SLOT_52 >= 3):
                Unknown23086(0)
                RefreshMultihit()
            else:
                Unknown23086(1)
            if (SLOT_53 >= 12):
                sendToLabel(3)

        def upon_77():
            SLOT_52 = 0
            SLOT_53 = (SLOT_53 + 1)

        def upon_46():
            SLOT_52 = 0
            SLOT_53 = (SLOT_53 + 1)
        Unknown2004(1, 0)
    sprite('su404_00', 3)	# 1-3
    sprite('su404_01', 1)	# 4-4
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    Unknown2015(200)
    sprite('su404_02', 1)	# 5-5
    tag_voice(1, 'bsu205_0', 'bsu205_1', 'bsu205_2', '')
    sprite('su404_03', 1)	# 6-6
    sprite('su404_04', 3)	# 7-9	 **attackbox here**
    GFX_0('suef_404', 0)
    ScreenShake(1500, 1500)
    sprite('su404_05', 3)	# 10-12	 **attackbox here**
    sprite('su404_06', 3)	# 13-15	 **attackbox here**
    loopRest()
    Unknown19(2, 2, 2)
    label(1)
    sprite('su404_04', 3)	# 16-18	 **attackbox here**
    Unknown2037(0)
    ScreenShake(1500, 1500)
    sprite('su404_05', 3)	# 19-21	 **attackbox here**
    sprite('su404_06', 3)	# 22-24	 **attackbox here**
    loopRest()
    Unknown19(2, 2, 2)
    SLOT_55 = (SLOT_55 + 1)
    (SLOT_55 >= 10)
    Unknown19(1, 2, 0)
    label(3)
    sprite('keep', 1)	# 25-25
    StartMultihit()
    clearUponHandler(3)
    label(2)
    sprite('su404_07', 3)	# 26-28
    clearUponHandler(3)
    Unknown26('suef_404')
    Unknown23086(0)
    Unknown30017('f4ffffff')
    Recovery()
    sprite('su404_08', 3)	# 29-31
    sprite('su404_09', 3)	# 32-34
    sprite('su404_10', 2)	# 35-36
    sprite('su404_11', 2)	# 37-38
    Unknown2015(-1)
    sprite('su404_12', 2)	# 39-40
    sprite('su404_13', 2)	# 41-42
    sprite('su404_14', 3)	# 43-45

@State
def Shot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown2003(1)
        callSubroutine('EmissionStart')
        Unknown30017('19000000')
    sprite('su405_00', 2)	# 1-2
    sprite('su405_01', 3)	# 3-5
    sprite('su405_02', 2)	# 6-7
    ScreenShake(2000, 2000)
    SFX_0('019_quake_1')
    sprite('su405_03', 2)	# 8-9
    tag_voice(1, 'bsu203_0', 'bsu203_1', 'bsu203_2', '')
    GFX_0('suef_405', 0)
    GFX_0('suef_405_crack', 0)
    sprite('su405_04', 2)	# 10-11
    sprite('su405_05', 2)	# 12-13
    ScreenShake(2000, 2000)
    sprite('su405_03', 2)	# 14-15
    sprite('su405_06', 3)	# 16-18
    sprite('su405_07', 3)	# 19-21
    ScreenShake(5000, 5000)
    Unknown26('suef_405')
    GFX_0('suef_405kick', -1)
    SFX_3('suse_04')
    SFX_0('209_down_normal_1')
    sprite('su405_08', 3)	# 22-24
    sprite('su405_09', 3)	# 25-27	 **attackbox here**
    sprite('su405_10', 3)	# 28-30
    Recovery()
    sprite('su405_11', 3)	# 31-33
    sprite('su405_12', 3)	# 34-36
    sprite('su405_13', 4)	# 37-40
    Unknown30017('e7ffffff')
    sprite('su405_14', 4)	# 41-44
    sprite('su405_15', 2)	# 45-46
    loopRest()
    sprite('su405_15', 1)	# 47-47

@State
def LowAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(600)
        AttackP1(70)
        AttackP2(75)
        Unknown11092(1)
        AirPushbackY(-4000)
        AirUntechableTime(60)
        hitstun(40)
        Hitstop(4)
        Unknown9310(30)
        HitLow(2)
        StarterRating(2)
        Unknown11058('0000000000000000010000000000000000000000')

        def upon_CLEAR_OR_EXIT():
            (SLOT_19 < 200000)
            if op(5, 2, 0, 2, 2):
                sendToLabel(1)

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(3)
    sprite('su407_00', 3)	# 1-3
    sprite('su407_01', 4)	# 4-7
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su407_02', 4)	# 8-11
    sprite('su407_03', 3)	# 12-14
    physicsXImpulse(3000)
    Unknown2015(250)
    sprite('su407_03', 3)	# 15-17
    Unknown1019(200)
    SFX_0('000_airdash_2')
    sprite('su407_04', 2)	# 18-19	 **attackbox here**
    Unknown1019(1000)
    GFX_0('suef_407_jiware', -1)
    ScreenShake(13000, 13000)
    RefreshMultihit()
    SFX_0('209_down_normal_1')
    sprite('su407_05', 2)	# 20-21	 **attackbox here**
    Unknown2037(1)
    sprite('su407_04', 2)	# 22-23	 **attackbox here**
    RefreshMultihit()
    sprite('su407_05', 2)	# 24-25	 **attackbox here**
    sprite('su407_04', 2)	# 26-27	 **attackbox here**
    RefreshMultihit()
    sprite('su407_05', 2)	# 28-29	 **attackbox here**
    sprite('su407_04', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    sprite('su407_05', 2)	# 32-33	 **attackbox here**
    sprite('su407_04', 2)	# 34-35	 **attackbox here**
    RefreshMultihit()
    sprite('su407_05', 2)	# 36-37	 **attackbox here**
    loopRest()
    gotoLabel(1)
    sprite('su407_03', 3)	# 38-40
    clearUponHandler(3)
    clearUponHandler(10)
    Unknown30017('e7ffffff')
    Unknown26('suef_407_jiware')
    Recovery()
    Unknown1019(50)
    sprite('su407_02', 3)	# 41-43
    Unknown1019(50)
    sprite('su407_01', 3)	# 44-46
    Unknown1019(50)
    sprite('su407_00', 3)	# 47-49
    Unknown1019(0)
    ExitState()
    label(1)
    sprite('keep', 6)	# 50-55
    StartMultihit()
    clearUponHandler(3)
    clearUponHandler(10)
    Unknown1028(-4000)
    sprite('su407_06', 2)	# 56-57
    sprite('su407_07', 2)	# 58-59
    sprite('su407_08', 2)	# 60-61
    sprite('su407_09', 3)	# 62-64
    Unknown2015(-1)
    sprite('su407_10', 3)	# 65-67
    Unknown26('suef_407_jiware')
    Unknown1028(0)
    sprite('su407_11', 3)	# 68-70
    tag_voice(1, 'bsu204_0', 'bsu204_1', 'bsu204_2', '')
    sprite('su407_12', 3)	# 71-73
    sprite('su407_13', 4)	# 74-77	 **attackbox here**
    Unknown8003(100, 1, 1)
    GFX_0('suef_407_kick', -1)
    Unknown1019(0)
    RefreshMultihit()
    Damage(1000)
    Hitstop(15)
    GroundedHitstunAnimation(10)
    AirHitstunAnimation(10)
    AirPushbackX(8000)
    AirPushbackY(40000)
    AttackP2(75)
    HitLow(0)
    Unknown9310(0)
    Unknown11058('0000000001000000000000000000000000000000')

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockJumpCancel(1)
    sendToLabelUpon(2, 2)
    sprite('su407_14', 4)	# 78-81
    Recovery()
    physicsYImpulse(12000)
    setGravity(1500)
    HitOrBlockJumpCancel(0)
    sprite('su407_15', 4)	# 82-85
    sprite('su407_16', 4)	# 86-89
    sprite('su407_17', 4)	# 90-93
    sprite('su407_18', 32767)	# 94-32860
    label(2)
    sprite('su407_19', 4)	# 32861-32864
    Unknown1084(1)
    HitOrBlockJumpCancel(0)
    Unknown30017('e7ffffff')
    Unknown8000(100, 1, 1)
    sprite('su407_20', 4)	# 32865-32868
    sprite('su407_21', 4)	# 32869-32872
    sprite('su407_22', 4)	# 32873-32876
    sprite('su407_23', 4)	# 32877-32880

@State
def UltimateLongAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5500)
        AttackP1(80)
        MinimumDamagePct(31)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(15000)
        WallbounceReboundTime(0)
        Unknown9202(20)
        Unknown9016(1)
        Unknown11056(0)
        Unknown2004(1, 0)
    sprite('su430_00', 3)	# 1-3
    setInvincible(1)
    GFX_0('suef_430_sword', -1)
    sprite('su430_01', 3)	# 4-6
    Unknown20000(1)
    Unknown20009(900)
    callSubroutine('EmissionStart')
    Unknown30017('0c000000')
    sprite('su430_02', 3)	# 7-9
    Unknown2036(75, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('su430_03', 3)	# 10-12
    tag_voice(1, 'bsu250_0', 'bsu250_1', '', '')
    sprite('su430_04', 3)	# 13-15
    Unknown4047(128, 128, 128)
    Unknown4045('737565665f34333073776f72640000000000000000000000000000000000000067000000')
    sprite('su430_05', 3)	# 16-18
    sprite('su430_06', 3)	# 19-21
    sprite('su430_07', 3)	# 22-24
    sprite('su430_05', 3)	# 25-27
    sprite('su430_06', 3)	# 28-30
    sprite('su430_07', 3)	# 31-33
    sprite('su430_05', 3)	# 34-36
    sprite('su430_06', 3)	# 37-39
    sprite('su430_07', 3)	# 40-42
    sprite('su430_05', 3)	# 43-45
    Unknown20000(0)
    sprite('su430_06', 3)	# 46-48
    sprite('su430_07', 3)	# 49-51
    sprite('su430_08', 6)	# 52-57
    Unknown21015('737565665f3433305f73776f7264000000000000000000000000000000000000cd10000000000000')
    sprite('su430_09', 6)	# 58-63
    sprite('su430_10', 6)	# 64-69
    sprite('su430_11', 6)	# 70-75
    sprite('su430_12', 6)	# 76-81
    sprite('su430_13', 6)	# 82-87
    sprite('su430_14', 1)	# 88-88
    tag_voice(0, 'bsu251_0', 'bsu251_1', '', '')
    sprite('su430_15', 1)	# 89-89
    sprite('su430_16', 6)	# 90-95	 **attackbox here**
    GFX_0('suef_430_slash', -1)
    SFX_3('suse_02')
    SFX_3('suse_06')
    SFX_3('suse_06')

    def upon_12():
        SFX_0('025_cleanhit_slash')
    sprite('su430_17', 3)	# 96-98
    setInvincible(0)
    sprite('su430_18', 3)	# 99-101
    sprite('su430_19', 3)	# 102-104
    sprite('su430_20', 3)	# 105-107
    sprite('su430_17', 3)	# 108-110
    sprite('su430_18', 3)	# 111-113
    sprite('su430_19', 3)	# 114-116
    sprite('su430_20', 3)	# 117-119
    sprite('su430_17', 3)	# 120-122
    sprite('su430_21', 5)	# 123-127
    sprite('su430_22', 5)	# 128-132
    sprite('su402_11ex01', 5)	# 133-137
    Unknown2015(-1)
    Unknown30017('e7ffffff')
    sprite('su402_12ex01', 5)	# 138-142
    sprite('su402_13ex01', 4)	# 143-146
    sprite('su402_14ex01', 4)	# 147-150

@State
def UltimateLongAssaultOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(5)
        Damage(5200)
        AttackP1(80)
        MinimumDamagePct(25)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(6000)
        AirPushbackY(20000)
        YImpluseBeforeWallbounce(1000)
        Unknown9016(1)
        Unknown11056(0)

        def upon_78():
            sendToLabel(10)
            Unknown13024(0)
            Unknown11064(1)
            Unknown11069('UltimateLongAssaultOD_Finish')
        Unknown2004(1, 0)
    sprite('su430_00', 3)	# 1-3
    setInvincible(1)
    GFX_0('suef_430_sword', -1)
    sprite('su430_01', 3)	# 4-6
    Unknown20000(1)
    Unknown20009(900)
    callSubroutine('EmissionStart')
    Unknown30017('0c000000')
    sprite('su430_02', 3)	# 7-9
    Unknown2036(75, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    sprite('su430_03', 3)	# 10-12
    tag_voice(1, 'bsu250_0', 'bsu250_1', '', '')
    sprite('su430_04', 3)	# 13-15
    Unknown4047(128, 128, 128)
    Unknown4045('737565665f34333073776f72640000000000000000000000000000000000000067000000')
    sprite('su430_05', 3)	# 16-18
    sprite('su430_06', 3)	# 19-21
    sprite('su430_07', 3)	# 22-24
    sprite('su430_05', 3)	# 25-27
    sprite('su430_06', 3)	# 28-30
    sprite('su430_07', 3)	# 31-33
    sprite('su430_05', 3)	# 34-36
    sprite('su430_06', 3)	# 37-39
    sprite('su430_07', 3)	# 40-42
    sprite('su430_05', 3)	# 43-45
    Unknown20000(0)
    sprite('su430_06', 3)	# 46-48
    sprite('su430_07', 3)	# 49-51
    sprite('su430_08', 6)	# 52-57
    Unknown21015('737565665f3433305f73776f7264000000000000000000000000000000000000cd10000000000000')
    sprite('su430_09', 6)	# 58-63
    sprite('su430_10', 6)	# 64-69
    sprite('su430_11', 6)	# 70-75
    sprite('su430_12', 6)	# 76-81
    sprite('su430_13', 6)	# 82-87
    sprite('su430_14', 1)	# 88-88
    tag_voice(0, 'bsu251_0', 'bsu251_1', '', '')
    sprite('su430_15', 1)	# 89-89
    sprite('su430_16', 6)	# 90-95	 **attackbox here**
    GFX_0('suef_430_slash', -1)
    SFX_3('suse_02')
    SFX_3('suse_06')
    SFX_3('suse_06')

    def upon_12():
        SFX_0('025_cleanhit_slash')
    sprite('su430_17', 3)	# 96-98
    setInvincible(0)
    sprite('su430_18', 3)	# 99-101
    sprite('su430_19', 3)	# 102-104
    sprite('su430_20', 3)	# 105-107
    sprite('su430_17', 3)	# 108-110
    sprite('su430_18', 3)	# 111-113
    sprite('su430_19', 3)	# 114-116
    sprite('su430_20', 3)	# 117-119
    sprite('su430_17', 3)	# 120-122
    sprite('su430_21', 5)	# 123-127
    sprite('su430_22', 5)	# 128-132
    sprite('su402_11ex01', 5)	# 133-137
    Unknown2015(-1)
    Unknown30017('e7ffffff')
    sprite('su402_12ex01', 5)	# 138-142
    sprite('su402_13ex01', 4)	# 143-146
    sprite('su402_14ex01', 4)	# 147-150
    ExitState()
    label(10)
    sprite('su430_16', 5)	# 151-155	 **attackbox here**
    StartMultihit()
    sprite('su430_17', 3)	# 156-158
    sprite('su430_18', 3)	# 159-161
    sprite('su430_19', 3)	# 162-164
    sprite('su430_20', 3)	# 165-167
    sprite('su430_21', 5)	# 168-172
    sprite('su430_22', 5)	# 173-177
    Unknown30017('e7ffffff')
    sprite('su402_11ex01', 5)	# 178-182
    sprite('su402_12ex01', 5)	# 183-187
    sprite('su402_13ex01', 4)	# 188-191
    sprite('su402_14ex01', 3)	# 192-194
    sprite('su402_14ex01', 1)	# 195-195
    enterState('UltimateLongAssaultOD_Finish')

@State
def UltimateLongAssaultOD_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(5)
        Damage(120)
        MinimumDamagePct(20)
        AttackP1(100)
        AttackP2(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(500)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(0)
        WallbounceReboundTime(0)
        Unknown11055(1)
        Unknown11066(1)
        Unknown11084(1)
        Unknown11108('03000000')
        Unknown11064(1)
        Unknown13024(0)
        SLOT_51 = 3
        SLOT_52 = 10

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(5000, 5000)
            Unknown1019(95)
            Unknown8006(100, 1, 1)
        setInvincible(1)
    sprite('su000_00', 1)	# 1-1
    sprite('su431_12', 5)	# 2-6
    sprite('su431_13', 5)	# 7-11
    Unknown2036(60, -1, 0)
    sprite('su431_14', 5)	# 12-16
    sprite('su431_15', 5)	# 17-21
    sprite('su431_16', 5)	# 22-26
    sprite('su431_17', 5)	# 27-31
    callSubroutine('EmissionStart')
    Unknown30017('08000000')
    sprite('su431_18', 5)	# 32-36
    tag_voice(0, 'bsu252_0', 'bsu252_1', '', '')
    sprite('su431_19', 3)	# 37-39
    GFX_0('suef_431_charge', -1)
    ScreenShake(2500, 2500)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_51):
            clearUponHandler(3)
            sendToLabel(1)
    label(0)
    sprite('su431_20', 3)	# 40-42
    ScreenShake(2500, 2500)
    SLOT_51 = (SLOT_51 + (-1))
    sprite('su431_21', 3)	# 43-45
    ScreenShake(2500, 2500)
    sprite('su431_22', 3)	# 46-48
    ScreenShake(2500, 2500)
    sprite('su431_19', 3)	# 49-51
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su431_23', 6)	# 52-57
    ScreenShake(5000, 5000)
    GFX_0('suef_431_ring', -1)
    sprite('su431_24', 6)	# 58-63
    ScreenShake(5000, 5000)
    sprite('su431_25', 2)	# 64-65	 **attackbox here**
    ScreenShake(5000, 5000)
    Unknown26('suef_431_charge')
    GFX_0('suef_431_beam', -1)
    physicsXImpulse(-40000)
    SFX_3('suse_07')
    sprite('su431_26', 2)	# 66-67

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_52):
            clearUponHandler(3)
            clearUponHandler(10)
            Unknown13024(1)
            sendToLabel(9)
    label(2)
    sprite('su431_27', 2)	# 68-69	 **attackbox here**
    SLOT_52 = (SLOT_52 + (-1))
    RefreshMultihit()
    Unknown1019(75)
    sprite('su431_28', 2)	# 70-71	 **attackbox here**
    RefreshMultihit()
    sprite('su431_29', 2)	# 72-73	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('su431_27', 3)	# 74-76	 **attackbox here**
    clearUponHandler(3)
    AttackP2(60)
    RefreshMultihit()
    Unknown11064(0)
    Unknown1019(70)
    Unknown11069('')
    sprite('su431_28', 3)	# 77-79	 **attackbox here**
    sprite('su431_29', 3)	# 80-82	 **attackbox here**
    sprite('su431_27', 4)	# 83-86	 **attackbox here**
    Unknown1019(70)
    Unknown26('suef_431_beam')
    sprite('su431_28', 4)	# 87-90	 **attackbox here**
    sprite('su431_29', 4)	# 91-94	 **attackbox here**
    sprite('su431_30', 4)	# 95-98
    Unknown1084(1)
    Unknown2015(-1)
    Unknown13024(1)
    setInvincible(0)
    Unknown30017('e7ffffff')
    sprite('su431_31', 4)	# 99-102
    sprite('su431_32', 4)	# 103-106
    sprite('su431_33', 6)	# 107-112
    sprite('su431_34', 6)	# 113-118
    sprite('su431_35', 6)	# 119-124
    sprite('su431_36', 6)	# 125-130

@State
def UltimateAntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1500)
        AttackP1(80)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9310(10)
        Unknown11069('UltimateAntiAir')
        Unknown11064(1)
        Unknown11056(0)
        MinimumDamagePct(10)
        Unknown11001(0, 2, 2)
        AirPushbackX(10000)
        AirPushbackY(80000)
        Unknown2004(1, 0)

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 2)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown20000(0)
            Unknown20003(0)
            Unknown20002(0)
    sprite('su214_00', 3)	# 1-3
    setInvincible(1)
    sprite('su214_01', 3)	# 4-6
    Unknown2036(61, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown1084(1)
    tag_voice(1, 'bsu280_0', 'bsu280_1', '', '')
    sprite('su214_02', 3)	# 7-9
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su214_03', 3)	# 10-12
    sprite('su214_07', 3)	# 13-15
    sprite('su214_08', 3)	# 16-18
    sprite('su214_09', 3)	# 19-21
    sprite('su214_10', 3)	# 22-24
    sprite('su214_08', 3)	# 25-27
    sprite('su214_09', 3)	# 28-30
    sprite('su214_10', 3)	# 31-33
    sprite('su214_08', 3)	# 34-36
    sprite('su214_09', 3)	# 37-39
    sprite('su214_08', 3)	# 40-42
    sprite('su214_09', 3)	# 43-45
    sprite('su214_08', 3)	# 46-48
    sprite('su214_09', 3)	# 49-51
    sprite('su214_11', 3)	# 52-54
    Unknown30017('e7ffffff')
    sprite('su214_12', 3)	# 55-57
    sprite('su214_13', 3)	# 58-60
    sprite('su000_00', 2)	# 61-62
    GFX_0('suef_440_fireaura', 103)
    sprite('su023_00ex00', 4)	# 63-66
    sprite('su023_01ex00', 4)	# 67-70
    physicsXImpulse(15000)
    tag_voice(0, 'bsu281_0', 'bsu281_1', '', '')
    sprite('su406_00ex00', 3)	# 71-73	 **attackbox here**
    GFX_0('suef_440_kick', -1)
    SFX_0('016_explode_2')
    SFX_3('suse_00')
    Unknown8001(1, 1)
    physicsYImpulse(60000)
    setGravity(2000)
    sprite('su406_01ex00', 3)	# 74-76	 **attackbox here**
    sprite('keep', 1)	# 77-77
    loopRest()
    sprite('su406_06ex00', 2)	# 78-79	 **attackbox here**
    Damage(400)
    AttackP2(100)
    Hitstop(5)
    AirPushbackX(16000)
    AirPushbackY(34000)
    GFX_0('suef_440_rolling', 103)
    setInvincible(0)
    sprite('su406_07ex00', 2)	# 80-81	 **attackbox here**
    sprite('su406_08ex00', 2)	# 82-83	 **attackbox here**
    RefreshMultihit()
    sprite('su406_09ex00', 2)	# 84-85	 **attackbox here**
    sprite('su406_06ex00', 2)	# 86-87	 **attackbox here**
    RefreshMultihit()
    sprite('su406_07ex00', 2)	# 88-89	 **attackbox here**
    sprite('su406_08ex00', 2)	# 90-91	 **attackbox here**
    RefreshMultihit()
    sprite('su406_09ex00', 2)	# 92-93	 **attackbox here**
    sprite('su406_06ex00', 2)	# 94-95	 **attackbox here**
    RefreshMultihit()
    sprite('su406_07ex00', 2)	# 96-97	 **attackbox here**
    sprite('su406_08ex00', 2)	# 98-99	 **attackbox here**
    sprite('su406_09ex00', 2)	# 100-101	 **attackbox here**
    sprite('su440_00', 3)	# 102-104	 **attackbox here**
    Unknown21012('737565665f3434305f726f6c6c696e670000000000000000000000000000000020000000')
    sprite('su440_00', 1)	# 105-105	 **attackbox here**
    RefreshMultihit()
    sprite('su440_00', 3)	# 106-108	 **attackbox here**

    def upon_78():
        Hitstop(0)
        Unknown13024(0)
        enterState('UltimateAntiAir_catch')
        Unknown11069('UltimateAntiAir_catch')
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Unknown11054(1000000)
    Unknown11002(-1)
    Unknown11045(0)
    RefreshMultihit()
    Unknown1019(0)
    sprite('su020_05', 3)	# 109-111
    Unknown26('suef_440_fireaura')
    Unknown21015('737565665f3434305f6b69636b310000000000000000000000000000000000003111000000000000')
    Unknown1044()
    sprite('su020_06', 3)	# 112-114
    label(0)
    sprite('su020_07', 4)	# 115-118
    sprite('su020_08', 4)	# 119-122
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('su024_00', 4)	# 123-126
    clearUponHandler(2)
    DisableAttackRestOfMove()
    Unknown8000(100, 1, 0)
    sprite('su024_01', 8)	# 127-134
    sprite('su024_02', 4)	# 135-138
    sprite('su024_03', 4)	# 139-142
    sprite('su024_04', 4)	# 143-146

@State
def UltimateAntiAir_catch():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAntiAirFinish', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(400)
        AttackP2(100)
        MinimumDamagePct(20)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown20003(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11108('03000000')
        Unknown11069('UltimateAntiAirFinish')
        Unknown11064(1)
        Unknown11023(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20002(1)
    sprite('su440_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    physicsXImpulse(0)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('keep', 1)	# 4-4
    StartMultihit()
    Unknown2053(1)

@State
def UltimateAntiAirFinish():

    def upon_IMMEDIATE():
        Unknown17012(3, 1, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(4000)
        AttackP1(80)
        AttackP2(100)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(200)
        AirPushbackX(9000)
        AirPushbackY(75000)
        YImpluseBeforeWallbounce(3000)
        Unknown9310(10)
        Unknown11002(-1)
        Unknown11064(0)
        Unknown11069('UltimateAntiAirFinish')
        Unknown11108('03000000')
        MinimumDamagePct(41)
        DisableAttackRestOfMove()
        setInvincible(1)
        Unknown13024(0)
        EnableCollision(0)
        Unknown1084(1)
        Unknown1043()
        Unknown20000(1)
        Unknown20003(1)
        Unknown20002(1)
        clearUponHandler(2)

        def upon_LANDING():
            ScreenShake(4000, 20000)
            sendToLabel(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown20000(0)
            Unknown20001(0)
            Unknown20003(0)
            Unknown20002(0)
        Unknown2004(1, 0)
    sprite('su440_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('su440_01', 3)	# 4-6
    Unknown5000(2, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown3029(1)
    sprite('su440_02', 3)	# 7-9
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_03', 3)	# 10-12
    Unknown5000(4, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_04', 3)	# 13-15
    Unknown5000(5, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_05', 6)	# 16-21
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_05', 6)	# 22-27
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1039(200)
    sprite('su440_05', 300)	# 28-327
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    label(1)
    sprite('su401_05ex00', 3)	# 328-330	 **attackbox here**
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    clearUponHandler(2)
    AttackP2(60)
    teleportRelativeY(0)
    Unknown1084(1)
    RefreshMultihit()
    ScreenShake(4000, 20000)
    GFX_0('suef_440_finish', -1)
    SFX_3('suse_04')
    SFX_0('016_explode_2')
    SFX_0('209_down_normal_1')
    Unknown11069('')
    tag_voice(0, 'bsu282_0', 'bsu282_1', '', '')
    sprite('su401_05ex00', 3)	# 331-333	 **attackbox here**
    sprite('su401_06ex00', 3)	# 334-336
    EnableCollision(1)
    Unknown3029(0)
    sprite('su401_07ex00', 3)	# 337-339
    sprite('su401_08ex00', 3)	# 340-342
    sprite('su401_06ex00', 3)	# 343-345
    sprite('su401_07ex00', 3)	# 346-348
    sprite('su401_08ex00', 3)	# 349-351
    sprite('su401_06ex00', 3)	# 352-354
    sprite('su401_07ex00', 3)	# 355-357
    sprite('su401_08ex00', 3)	# 358-360
    sprite('su401_06ex00', 3)	# 361-363
    sprite('su401_07ex00', 3)	# 364-366
    sprite('su401_08ex00', 3)	# 367-369
    sprite('su401_06ex00', 3)	# 370-372
    sprite('su401_07ex00', 3)	# 373-375
    sprite('su401_08ex00', 3)	# 376-378
    sprite('su401_06ex00', 3)	# 379-381
    Unknown20000(0)
    Unknown13024(1)
    sprite('su401_07ex00', 3)	# 382-384
    sprite('su401_08ex00', 3)	# 385-387
    sprite('su401_06ex00', 3)	# 388-390
    sprite('su401_07ex00', 3)	# 391-393
    sprite('su401_08ex00', 3)	# 394-396
    sprite('su401_09ex00', 3)	# 397-399
    sprite('su401_10ex00', 3)	# 400-402
    sprite('su403_26ex00', 4)	# 403-406
    sprite('su403_27ex00', 4)	# 407-410
    sprite('su403_28ex00', 4)	# 411-414

@State
def UltimateAntiAirOD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(4)
        Damage(1500)
        AttackP1(80)
        AttackP2(100)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        Unknown9310(10)
        Unknown11069('UltimateAntiAirOD')
        Unknown11064(1)
        Unknown11056(0)
        MinimumDamagePct(10)
        Unknown11001(0, 2, 2)
        AirPushbackX(11000)
        AirPushbackY(105000)
        Unknown2004(1, 0)

        def upon_78():
            clearUponHandler(78)
            Unknown13024(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 2)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown20000(0)
            Unknown20003(0)
            Unknown20002(0)
    sprite('su214_00', 3)	# 1-3
    setInvincible(1)
    sprite('su214_01', 3)	# 4-6
    Unknown2036(61, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown30080('')
    Unknown1084(1)
    tag_voice(1, 'bsu280_0', 'bsu280_1', '', '')
    sprite('su214_02', 3)	# 7-9
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su214_03', 3)	# 10-12
    sprite('su214_07', 3)	# 13-15
    sprite('su214_08', 3)	# 16-18
    sprite('su214_09', 3)	# 19-21
    sprite('su214_10', 3)	# 22-24
    sprite('su214_08', 3)	# 25-27
    sprite('su214_09', 3)	# 28-30
    sprite('su214_10', 3)	# 31-33
    sprite('su214_08', 3)	# 34-36
    sprite('su214_09', 3)	# 37-39
    sprite('su214_08', 3)	# 40-42
    sprite('su214_09', 3)	# 43-45
    sprite('su214_08', 3)	# 46-48
    sprite('su214_09', 3)	# 49-51
    sprite('su214_11', 3)	# 52-54
    Unknown30017('e7ffffff')
    sprite('su214_12', 3)	# 55-57
    sprite('su214_13', 3)	# 58-60
    sprite('su000_00', 2)	# 61-62
    GFX_0('suef_440_fireaura', 103)
    sprite('su023_00ex00', 4)	# 63-66
    sprite('su023_01ex00', 4)	# 67-70
    physicsXImpulse(15000)
    tag_voice(0, 'bsu281_0', 'bsu281_1', '', '')
    sprite('su406_00ex00', 3)	# 71-73	 **attackbox here**
    GFX_0('suef_440_kick', -1)
    SFX_0('016_explode_2')
    SFX_3('suse_00')
    Unknown8001(1, 1)
    physicsYImpulse(80000)
    setGravity(2000)
    sprite('su406_01ex00', 3)	# 74-76	 **attackbox here**
    sprite('keep', 1)	# 77-77
    loopRest()
    sprite('su406_06ex00', 2)	# 78-79	 **attackbox here**
    Damage(310)
    Hitstop(5)
    Unknown11001(0, 0, 0)
    AirPushbackX(20000)
    AirPushbackY(70000)
    GFX_0('suef_440_rolling', 103)
    setInvincible(0)
    sprite('su406_07ex00', 2)	# 80-81	 **attackbox here**
    sprite('su406_08ex00', 2)	# 82-83	 **attackbox here**
    RefreshMultihit()
    sprite('su406_09ex00', 2)	# 84-85	 **attackbox here**
    sprite('su406_06ex00', 2)	# 86-87	 **attackbox here**
    RefreshMultihit()
    sprite('su406_07ex00', 2)	# 88-89	 **attackbox here**
    sprite('su406_08ex00', 2)	# 90-91	 **attackbox here**
    RefreshMultihit()
    sprite('su406_09ex00', 2)	# 92-93	 **attackbox here**
    RefreshMultihit()
    sprite('su406_06ex00', 2)	# 94-95	 **attackbox here**
    RefreshMultihit()
    Hitstop(4)
    Unknown11001(0, 0, 0)
    sprite('su406_07ex00', 2)	# 96-97	 **attackbox here**
    RefreshMultihit()
    sprite('su406_08ex00', 2)	# 98-99	 **attackbox here**
    RefreshMultihit()
    sprite('su406_09ex00', 2)	# 100-101	 **attackbox here**
    RefreshMultihit()
    sprite('su406_06ex00', 2)	# 102-103	 **attackbox here**
    Hitstop(3)
    RefreshMultihit()
    AirPushbackX(5000)
    AirPushbackY(1000)
    sprite('su406_07ex00', 2)	# 104-105	 **attackbox here**
    RefreshMultihit()
    sprite('su406_08ex00', 2)	# 106-107	 **attackbox here**
    RefreshMultihit()
    sprite('su406_09ex00', 2)	# 108-109	 **attackbox here**
    RefreshMultihit()
    sprite('su406_06ex00', 2)	# 110-111	 **attackbox here**
    AirPushbackX(10000)
    AirPushbackY(5000)
    RefreshMultihit()
    sprite('su406_07ex00', 2)	# 112-113	 **attackbox here**
    sprite('su406_08ex00', 2)	# 114-115	 **attackbox here**
    sprite('su406_09ex00', 1)	# 116-116	 **attackbox here**
    loopRest()
    label(1)
    sprite('su440_00', 2)	# 117-118	 **attackbox here**
    Unknown21012('737565665f3434305f726f6c6c696e670000000000000000000000000000000020000000')
    sprite('su440_00', 1)	# 119-119	 **attackbox here**
    RefreshMultihit()
    sprite('su440_00', 3)	# 120-122	 **attackbox here**

    def upon_78():
        Hitstop(0)
        Unknown13024(0)
        enterState('UltimateAntiAirOD_catch')
        Unknown11069('UltimateAntiAirOD_catch')
    Unknown11032('ffffffffffffffffffffffffffffffff')
    Unknown11054(1000000)
    Unknown11002(-1)
    Unknown11045(0)
    RefreshMultihit()
    Unknown1019(0)
    sprite('su020_05', 3)	# 123-125
    Unknown26('suef_440_fireaura')
    Unknown21015('737565665f3434305f6b69636b310000000000000000000000000000000000003111000000000000')
    Unknown1044()
    sprite('su020_06', 3)	# 126-128
    label(0)
    sprite('su020_07', 4)	# 129-132
    sprite('su020_08', 4)	# 133-136
    loopRest()
    gotoLabel(0)
    label(2)
    sprite('su024_00', 4)	# 137-140
    clearUponHandler(2)
    DisableAttackRestOfMove()
    Unknown8000(100, 1, 0)
    sprite('su024_01', 8)	# 141-148
    sprite('su024_02', 4)	# 149-152
    sprite('su024_03', 4)	# 153-156
    sprite('su024_04', 4)	# 157-160

@State
def UltimateAntiAirOD_catch():

    def upon_IMMEDIATE():
        Unknown17011('UltimateAntiAirODFinish', 3, 1, 0)
        Unknown23056('')
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackLevel_(4)
        Damage(300)
        AttackP2(100)
        MinimumDamagePct(20)
        Unknown30061(1)
        Unknown11050('0400000065665f6e6f6e0000000000000000000000000000000000000000000000000000')
        setInvincible(1)
        Unknown20003(1)
        Unknown11068(1)
        Unknown13024(0)
        Unknown2015(500)
        Unknown11108('03000000')
        Unknown11069('UltimateAntiAirODFinish')
        Unknown11064(1)
        Unknown11023(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20002(1)
    sprite('su440_00', 3)	# 1-3	 **attackbox here**
    Unknown5000(0, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    physicsXImpulse(0)
    physicsYImpulse(5000)
    setGravity(100)
    sprite('keep', 1)	# 4-4
    StartMultihit()
    Unknown2053(1)

@State
def UltimateAntiAirODFinish():

    def upon_IMMEDIATE():
        Unknown17012(3, 1, 0)
        Unknown23056('')
        AttackLevel_(4)
        Damage(3400)
        AttackP1(80)
        AttackP2(100)
        Hitstop(0)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirUntechableTime(200)
        AirPushbackY(75000)
        YImpluseBeforeWallbounce(3000)
        Unknown9190(1)
        Unknown9118(40)
        Unknown9310(10)
        Unknown11002(-1)
        Unknown11043(0)
        Unknown11064(0)
        Unknown11069('UltimateAntiAirODFinish')
        Unknown11108('03000000')
        MinimumDamagePct(48)
        DisableAttackRestOfMove()
        setInvincible(1)
        Unknown13024(0)
        EnableCollision(0)
        Unknown1084(1)
        Unknown20000(1)
        Unknown20003(1)
        Unknown20002(1)
        clearUponHandler(2)

        def upon_LANDING():
            ScreenShake(8000, 40000)
            sendToLabel(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown20000(0)
            Unknown20001(0)
            Unknown20003(0)
            Unknown20002(0)
        Unknown2004(1, 0)
    sprite('su440_00', 6)	# 1-6	 **attackbox here**
    Unknown5000(1, 0)
    Unknown5001('0000000005000000050000000000000000000000')
    sprite('su440_01', 6)	# 7-12
    Unknown5000(2, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown3029(1)
    sprite('su440_02', 3)	# 13-15
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_02', 3)	# 16-18
    Unknown5000(3, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1043()
    sprite('su440_03', 6)	# 19-24
    Unknown5000(4, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_04', 6)	# 25-30
    Unknown5000(5, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_05', 6)	# 31-36
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('su440_05', 6)	# 37-42
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1039(150)
    sprite('su440_05', 6)	# 43-48
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1039(200)
    sprite('su440_05', 300)	# 49-348
    Unknown5000(6, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown1039(300)
    label(1)
    sprite('su401_05ex00', 3)	# 349-351	 **attackbox here**
    Unknown5000(29, 0)
    Unknown5001('0000000001000000010000000000000000000000')
    clearUponHandler(2)
    AttackP2(60)
    teleportRelativeY(0)
    Unknown1084(1)
    RefreshMultihit()
    ScreenShake(8000, 40000)
    GFX_0('suef_440_finish_sp', -1)
    SFX_3('suse_04')
    SFX_0('016_explode_2')
    SFX_0('209_down_normal_1')
    SFX_0('025_cleanhit_grap')
    Unknown11069('')
    tag_voice(0, 'bsu282_0', 'bsu282_1', '', '')
    sprite('su401_05ex00', 3)	# 352-354	 **attackbox here**
    sprite('su401_06ex00', 3)	# 355-357
    EnableCollision(1)
    Unknown3029(0)
    sprite('su401_07ex00', 3)	# 358-360
    sprite('su401_08ex00', 3)	# 361-363
    sprite('su401_06ex00', 3)	# 364-366
    sprite('su401_07ex00', 3)	# 367-369
    sprite('su401_08ex00', 3)	# 370-372
    sprite('su401_06ex00', 3)	# 373-375
    sprite('su401_07ex00', 3)	# 376-378
    sprite('su401_08ex00', 3)	# 379-381
    sprite('su401_06ex00', 3)	# 382-384
    sprite('su401_07ex00', 3)	# 385-387
    sprite('su401_08ex00', 3)	# 388-390
    sprite('su401_06ex00', 3)	# 391-393
    sprite('su401_07ex00', 3)	# 394-396
    sprite('su401_08ex00', 3)	# 397-399
    sprite('su401_06ex00', 3)	# 400-402
    sprite('su401_07ex00', 3)	# 403-405
    sprite('su401_08ex00', 3)	# 406-408
    sprite('su401_06ex00', 3)	# 409-411
    sprite('su401_07ex00', 3)	# 412-414
    sprite('su401_08ex00', 3)	# 415-417
    sprite('su401_06ex00', 3)	# 418-420
    sprite('su401_07ex00', 3)	# 421-423
    sprite('su401_08ex00', 3)	# 424-426
    sprite('su401_06ex00', 3)	# 427-429
    Unknown20000(0)
    Unknown13024(1)
    sprite('su401_07ex00', 3)	# 430-432
    sprite('su401_08ex00', 3)	# 433-435
    sprite('su401_06ex00', 3)	# 436-438
    sprite('su401_07ex00', 3)	# 439-441
    sprite('su401_08ex00', 3)	# 442-444
    sprite('su401_06ex00', 3)	# 445-447
    sprite('su401_07ex00', 3)	# 448-450
    sprite('su401_08ex00', 3)	# 451-453
    sprite('su401_06ex00', 3)	# 454-456
    sprite('su401_07ex00', 3)	# 457-459
    sprite('su401_08ex00', 3)	# 460-462
    sprite('su401_09ex00', 3)	# 463-465
    sprite('su401_10ex00', 3)	# 466-468
    sprite('su403_26ex00', 4)	# 469-472
    sprite('su403_27ex00', 4)	# 473-476
    sprite('su403_28ex00', 4)	# 477-480

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown11069('AstralHeat')
        AttackLevel_(5)
        Damage(0)
        MinimumDamagePct(100)
        AirUntechableTime(300)
        AirPushbackX(0)
        AirPushbackY(-100000)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9310(999)
        Unknown11072(1, 0, 0)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11064(1)

        def upon_78():
            clearUponHandler(78)
            Hitstop(0)
            Unknown11001(0, -1, -1)
            PushbackX(0)
            Unknown2019(500)
            Unknown23088(1, 1)
            Unknown23157(1)
            Unknown11067(1)
            EnableCollision(0)
            Unknown2053(0)
            Unknown2034(0)
            sendToLabel(1)

            def upon_45():
                SLOT_6 = 1

            def upon_STATE_END():
                clearUponHandler(45)
                SLOT_6 = 0
        Unknown2004(1, 0)
    sprite('su450_00', 3)	# 1-3
    setInvincible(1)
    Unknown1084(1)
    GFX_0('suef_450_hand', -1)
    Unknown26('suef_aura')
    sprite('su450_01', 3)	# 4-6
    Unknown2036(50, -1, 2)
    Unknown23147()
    GFX_0('EMB_SU_AH', -1)
    sprite('su450_02', 3)	# 7-9
    tag_voice(1, 'bsu290_0', 'bsu290_1', '', '')
    sprite('su450_03', 3)	# 10-12
    sprite('su450_04', 3)	# 13-15
    sprite('su450_02', 3)	# 16-18
    sprite('su450_03', 3)	# 19-21
    sprite('su450_04', 3)	# 22-24
    sprite('su450_02', 3)	# 25-27
    sprite('su450_03', 3)	# 28-30
    sprite('su450_04', 3)	# 31-33
    sprite('su450_02', 3)	# 34-36
    sprite('su450_03', 3)	# 37-39
    sprite('su450_04', 3)	# 40-42
    sprite('su450_02', 3)	# 43-45
    sprite('su450_03', 3)	# 46-48
    sprite('su450_04', 3)	# 49-51
    sprite('su450_02', 3)	# 52-54
    sprite('su450_03', 3)	# 55-57
    sprite('su450_04', 3)	# 58-60
    sprite('su450_05', 3)	# 61-63
    Unknown26('suef_450_hand')
    GFX_0('suef_450_atk1', -1)
    SFX_3('suse_04')
    SFX_0('005_swing_grap_2_2')
    sprite('su450_06', 3)	# 64-66	 **attackbox here**
    sprite('su450_07', 4)	# 67-70
    setInvincible(0)
    sprite('su450_08', 4)	# 71-74
    sprite('su450_09', 4)	# 75-78
    sprite('su450_07', 4)	# 79-82
    sprite('su450_08', 4)	# 83-86
    sprite('su450_09', 4)	# 87-90
    sprite('su450_33', 4)	# 91-94
    sprite('su450_34', 4)	# 95-98
    sprite('su450_35', 4)	# 99-102
    ExitState()
    label(1)
    sprite('su450_07', 3)	# 103-105
    sprite('su450_08', 3)	# 106-108
    sprite('su450_09', 3)	# 109-111
    sprite('su450_07', 3)	# 112-114
    sprite('su450_08', 3)	# 115-117
    sprite('su450_09', 3)	# 118-120
    sprite('su450_07', 3)	# 121-123
    sprite('su450_08', 3)	# 124-126
    sprite('su450_09', 3)	# 127-129
    sprite('su450_07', 3)	# 130-132
    sprite('su450_08', 3)	# 133-135
    sprite('su450_09', 3)	# 136-138
    sprite('su450_07', 3)	# 139-141
    sprite('su450_08', 3)	# 142-144
    sprite('su450_09', 3)	# 145-147
    Unknown23084(1)
    sprite('su450_10', 6)	# 148-153	 **attackbox here**
    GFX_0('suef_450_atk2', 0)
    RefreshMultihit()
    Damage(3000)
    Unknown11023(1)
    Hitstop(6)
    Unknown11001(0, 0, 0)
    Unknown11072(0, 0, 0)
    AirUntechableTime(999)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(80000)
    AirPushbackY(40000)
    YImpluseBeforeWallbounce(0)
    GFX_0('AstralHeat_Camera', -1)
    SFX_3('suse_00')
    sprite('su450_11', 3)	# 154-156
    GFX_0('suef_450_bg', -1)
    tag_voice(0, 'bsu291_0', 'bsu291_1', '', '')
    sprite('su450_12', 3)	# 157-159
    sprite('su450_13', 3)	# 160-162
    sprite('su450_11', 3)	# 163-165
    sprite('su450_12', 3)	# 166-168
    sprite('su450_13', 3)	# 169-171
    sprite('su450_11', 3)	# 172-174
    sprite('su450_12', 3)	# 175-177
    sprite('su450_13', 3)	# 178-180
    sprite('su450_11', 3)	# 181-183
    sprite('su450_12', 3)	# 184-186
    sprite('su450_13', 3)	# 187-189
    sprite('su450_11', 3)	# 190-192
    sprite('su450_12', 3)	# 193-195
    sprite('su450_13', 3)	# 196-198
    sprite('su450_11', 3)	# 199-201
    sprite('su450_12', 3)	# 202-204
    sprite('su450_13', 3)	# 205-207
    sprite('su450_11', 3)	# 208-210
    sprite('su450_12', 3)	# 211-213
    sprite('su450_13', 3)	# 214-216
    sprite('su450_14', 6)	# 217-222
    GFX_0('suef_450_shake', -1)
    sprite('su450_15', 6)	# 223-228	 **attackbox here**
    GFX_0('suef_450_sword', -1)
    SFX_3('suse_05')
    SFX_3('suse_05')
    sprite('su450_16', 8)	# 229-236	 **attackbox here**
    sprite('su450_17', 8)	# 237-244	 **attackbox here**
    tag_voice(0, 'bsu292_0', 'bsu292_1', '', '')
    sprite('su450_18', 8)	# 245-252	 **attackbox here**
    sprite('su450_19', 8)	# 253-260	 **attackbox here**
    sprite('su450_20', 6)	# 261-266	 **attackbox here**
    sprite('su450_21', 6)	# 267-272	 **attackbox here**
    sprite('su450_22', 6)	# 273-278	 **attackbox here**
    Unknown21012('737565665f3435305f7368616b6500000000000000000000000000000000000020000000')
    SFX_3('suse_05')
    SFX_3('suse_05')
    sprite('su450_23', 6)	# 279-284	 **attackbox here**
    sprite('su450_24', 3)	# 285-287	 **attackbox here**
    GFX_0('suef_450_swordaura', -1)
    GFX_0('suef_450_storm_group', -1)
    SFX_3('suse_07')
    Unknown2037(12)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_2 >= 12):
            RefreshMultihit()
            Damage(1498)
            Unknown9016(1)
            Unknown11057(0)
            Hitstop(0)
            Unknown2037(0)
            Unknown23011(1)
            GFX_0('suef_450_HitEff', 100)
        else:
            Unknown2038(1)
    sprite('su450_25', 3)	# 288-290	 **attackbox here**
    sprite('su450_26', 3)	# 291-293	 **attackbox here**
    sprite('su450_24', 3)	# 294-296	 **attackbox here**
    sprite('su450_25', 3)	# 297-299	 **attackbox here**
    sprite('su450_26', 3)	# 300-302	 **attackbox here**
    sprite('su450_24', 3)	# 303-305	 **attackbox here**
    sprite('su450_25', 3)	# 306-308	 **attackbox here**
    sprite('su450_26', 3)	# 309-311	 **attackbox here**
    sprite('su450_24', 3)	# 312-314	 **attackbox here**
    sprite('su450_25', 3)	# 315-317	 **attackbox here**
    sprite('su450_26', 3)	# 318-320	 **attackbox here**
    sprite('su450_24', 3)	# 321-323	 **attackbox here**
    tag_voice(0, 'bsu293_0', 'bsu293_1', '', '')
    sprite('su450_25', 3)	# 324-326	 **attackbox here**
    sprite('su450_26', 3)	# 327-329	 **attackbox here**
    sprite('su450_24', 3)	# 330-332	 **attackbox here**
    sprite('su450_25', 3)	# 333-335	 **attackbox here**
    sprite('su450_26', 3)	# 336-338	 **attackbox here**
    sprite('su450_24', 3)	# 339-341	 **attackbox here**
    sprite('su450_25', 3)	# 342-344	 **attackbox here**
    sprite('su450_26', 3)	# 345-347	 **attackbox here**
    sprite('su450_24', 3)	# 348-350	 **attackbox here**
    sprite('su450_25', 3)	# 351-353	 **attackbox here**
    sprite('su450_26', 3)	# 354-356	 **attackbox here**
    sprite('su450_24', 3)	# 357-359	 **attackbox here**
    sprite('su450_25', 3)	# 360-362	 **attackbox here**
    sprite('su450_26', 3)	# 363-365	 **attackbox here**
    sprite('su450_27', 3)	# 366-368	 **attackbox here**
    Unknown21012('737565665f3435305f73776f726400000000000000000000000000000000000020000000')
    SFX_3('suse_06')
    SFX_3('suse_06')
    Unknown2037(8)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_2 >= 8):
            Damage(1498)
            RefreshMultihit()
            Unknown2037(0)
            Unknown23011(1)
            GFX_0('suef_450_HitEff', 100)
        else:
            Unknown2038(1)
    sprite('su450_28', 3)	# 369-371	 **attackbox here**
    Unknown21012('737565665f3435305f73776f726461757261000000000000000000000000000020000000')
    sprite('su450_29', 3)	# 372-374	 **attackbox here**
    Unknown21012('41737472616c486561745f43616d65726100000000000000000000000000000021000000')
    Unknown26('suef_450_storm_group')
    Unknown21015('737565665f3435305f73746f726d0000000000000000000000000000000000009511000000000000')
    Unknown21015('737565665f3435305f73746f726d5f62000000000000000000000000000000009511000000000000')
    sprite('su450_30', 3)	# 375-377	 **attackbox here**
    GFX_0('suef_450_swordaura2', -1)
    GFX_0('suef_450_storm2_group', -1)
    sprite('su450_31', 3)	# 378-380	 **attackbox here**
    sprite('su450_32', 3)	# 381-383	 **attackbox here**
    sprite('su450_30', 3)	# 384-386	 **attackbox here**
    SFX_3('suse_10')
    sprite('su450_31', 3)	# 387-389	 **attackbox here**
    sprite('su450_32', 3)	# 390-392	 **attackbox here**
    sprite('su450_30', 3)	# 393-395	 **attackbox here**
    sprite('su450_31', 3)	# 396-398	 **attackbox here**
    sprite('su450_32', 3)	# 399-401	 **attackbox here**
    sprite('su450_30', 3)	# 402-404	 **attackbox here**
    sprite('su450_31', 3)	# 405-407	 **attackbox here**
    sprite('su450_32', 3)	# 408-410	 **attackbox here**
    sprite('su450_30', 3)	# 411-413	 **attackbox here**
    sprite('su450_31', 3)	# 414-416	 **attackbox here**
    sprite('su450_32', 3)	# 417-419	 **attackbox here**
    sprite('su450_30', 3)	# 420-422	 **attackbox here**
    sprite('su450_31', 3)	# 423-425	 **attackbox here**
    sprite('su450_32', 3)	# 426-428	 **attackbox here**
    sprite('su450_30', 3)	# 429-431	 **attackbox here**
    Unknown21012('737565665f3435305f7368616b6500000000000000000000000000000000000021000000')
    Unknown21012('737565665f3435305f73746f726d325f67726f7570000000000000000000000020000000')
    sprite('su450_31', 3)	# 432-434	 **attackbox here**
    sprite('su450_32', 3)	# 435-437	 **attackbox here**
    sprite('su450_30', 3)	# 438-440	 **attackbox here**
    sprite('su450_31', 3)	# 441-443	 **attackbox here**
    sprite('su450_32', 3)	# 444-446	 **attackbox here**
    sprite('su450_30', 3)	# 447-449	 **attackbox here**
    sprite('su450_31', 3)	# 450-452	 **attackbox here**
    sprite('su450_32', 3)	# 453-455	 **attackbox here**
    sprite('su450_30', 3)	# 456-458	 **attackbox here**
    sprite('su450_31', 3)	# 459-461	 **attackbox here**
    sprite('su450_32', 3)	# 462-464	 **attackbox here**
    sprite('su450_30', 3)	# 465-467	 **attackbox here**
    Unknown21012('737565665f3435305f7368616b6500000000000000000000000000000000000022000000')
    Unknown21012('737565665f3435305f73746f726d325f67726f7570000000000000000000000021000000')
    SFX_3('suse_10')
    Unknown2037(4)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_2 >= 4):
            RefreshMultihit()
            Damage(1997)
            Unknown2037(0)
            Unknown23011(1)
            GFX_0('suef_450_HitEff', 100)
            GFX_0('suef_450_HitEff', 100)
        else:
            Unknown2038(1)
    sprite('su450_31', 3)	# 468-470	 **attackbox here**
    sprite('su450_32', 3)	# 471-473	 **attackbox here**
    sprite('su450_30', 3)	# 474-476	 **attackbox here**
    sprite('su450_31', 3)	# 477-479	 **attackbox here**
    sprite('su450_32', 3)	# 480-482	 **attackbox here**
    sprite('su450_30', 3)	# 483-485	 **attackbox here**
    sprite('su450_31', 3)	# 486-488	 **attackbox here**
    sprite('su450_32', 3)	# 489-491	 **attackbox here**
    sprite('su450_30', 3)	# 492-494	 **attackbox here**
    tag_voice(0, 'bsu294_0', 'bsu294_1', '', '')
    sprite('su450_31', 3)	# 495-497	 **attackbox here**
    sprite('su450_32', 3)	# 498-500	 **attackbox here**
    sprite('su450_30', 3)	# 501-503	 **attackbox here**
    sprite('su450_31', 3)	# 504-506	 **attackbox here**
    sprite('su450_32', 3)	# 507-509	 **attackbox here**
    sprite('su450_30', 3)	# 510-512	 **attackbox here**
    sprite('su450_31', 3)	# 513-515	 **attackbox here**
    sprite('su450_32', 3)	# 516-518	 **attackbox here**
    sprite('su450_30', 3)	# 519-521	 **attackbox here**
    sprite('su450_31', 3)	# 522-524	 **attackbox here**
    sprite('su450_32', 3)	# 525-527	 **attackbox here**
    sprite('su450_30', 3)	# 528-530	 **attackbox here**
    sprite('su450_31', 3)	# 531-533	 **attackbox here**
    sprite('su450_32', 3)	# 534-536	 **attackbox here**
    sprite('su450_30', 3)	# 537-539	 **attackbox here**
    sprite('su450_31', 3)	# 540-542	 **attackbox here**
    sprite('su450_32', 3)	# 543-545	 **attackbox here**
    sprite('su450_30', 3)	# 546-548	 **attackbox here**
    sprite('su450_31', 3)	# 549-551	 **attackbox here**
    sprite('su450_32', 3)	# 552-554	 **attackbox here**
    GFX_0('suef_450_storm3_group', -1)
    sprite('su450_30', 3)	# 555-557	 **attackbox here**
    Unknown2037(2)

    def upon_CLEAR_OR_EXIT():
        if (SLOT_2 >= 2):
            RefreshMultihit()
            Unknown2037(0)
            Unknown23011(1)
            GFX_0('suef_450_HitEff', 100)
            GFX_0('suef_450_HitEff', 100)
        else:
            Unknown2038(1)
    sprite('su450_31', 3)	# 558-560	 **attackbox here**
    sprite('su450_32', 3)	# 561-563	 **attackbox here**
    sprite('su450_30', 3)	# 564-566	 **attackbox here**
    sprite('su450_31', 3)	# 567-569	 **attackbox here**
    sprite('su450_32', 3)	# 570-572	 **attackbox here**
    sprite('su450_30', 3)	# 573-575	 **attackbox here**
    sprite('su450_31', 3)	# 576-578	 **attackbox here**
    sprite('su450_32', 3)	# 579-581	 **attackbox here**
    sprite('su450_30', 3)	# 582-584	 **attackbox here**
    sprite('null', 10)	# 585-594
    clearUponHandler(3)
    Unknown26('suef_450_sword')
    Unknown26('suef_450_swordaura2')
    Unknown26('suef_450_storm2_group')
    Unknown26('suef_450_storm3_group')
    Unknown26('suef_450_shake')
    Unknown26('suef_450_bg')
    GFX_0('suef_450_HitEff', 100)
    GFX_0('suef_450_HitEff', 100)
    GFX_0('suef_450_HitEff', 100)
    GFX_0('suef_450_HitEff', 100)
    GFX_0('suef_450_HitEff', 100)
    sprite('su450_29', 80)	# 595-674	 **attackbox here**
    Unknown21012('41737472616c486561745f43616d65726100000000000000000000000000000029000000')
    Unknown3038(1)
    Unknown23024(2)
    Unknown20000(1)
    Unknown20001(1)
    RefreshMultihit()
    Damage(14119)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackY(30000)
    AirPushbackX(100000)
    Unknown9095()
    Unknown11072(2, 0, 0)
    Unknown11064(3)
    Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11057(1000)
    Unknown23011(4)

    def upon_11():
        Unknown36(22)
        Unknown3001(0)
        Unknown35()
    sprite('su450_29', 20)	# 675-694	 **attackbox here**
    Unknown23024(3)
    sprite('su611_09', 6)	# 695-700
    Unknown1000(260000)
    Unknown3038(0)
    GFX_0('suef_450_end', -1)
    GFX_0('suef_611_ah', -1)
    sprite('su611_10', 6)	# 701-706
    sprite('su611_11', 6)	# 707-712
    sprite('su611_12', 6)	# 713-718
    sprite('su611_09', 6)	# 719-724
    sprite('su611_10', 6)	# 725-730
    sprite('su611_11', 6)	# 731-736
    sprite('su611_12', 6)	# 737-742
    sprite('su611_09', 6)	# 743-748
    sprite('su611_10', 6)	# 749-754
    sprite('su611_11', 6)	# 755-760
    sprite('su611_12', 6)	# 761-766
    sprite('su611_09', 6)	# 767-772
    sprite('su611_10', 6)	# 773-778
    sprite('su611_11', 6)	# 779-784
    sprite('su611_12', 6)	# 785-790
    Unknown18010()
    tag_voice(0, 'bsu295_0', 'bsu295_1', '', '')
    Unknown23018(1)
    label(3)
    sprite('su611_09', 6)	# 791-796
    sprite('su611_10', 6)	# 797-802
    sprite('su611_11', 6)	# 803-808
    sprite('su611_12', 6)	# 809-814
    loopRest()
    gotoLabel(3)

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
    sprite('su020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('su020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('su024_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackP1(70)
        Unknown11042(1)
        Unknown2004(1, 0)
        Unknown30040(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('su210_00', 4)	# 1-4
    Unknown1051(60)
    sprite('su210_01', 5)	# 5-9
    sprite('su210_02', 3)	# 10-12
    Unknown2015(200)
    sprite('su210_03', 2)	# 13-14
    tag_voice(1, 'bsu107_0', 'bsu107_1', 'bsu107_2', '')
    sprite('su210_04', 2)	# 15-16
    GFX_0('suef_210_Atk', 0)
    SFX_3('suse_02')
    sprite('su210_04', 6)	# 17-22
    GFX_0('suef_210_shot', 0)
    ScreenShake(10000, 10000)
    sprite('su210_05', 6)	# 23-28
    sprite('su210_06', 6)	# 29-34
    sprite('su210_07', 12)	# 35-46
    sprite('su210_08', 7)	# 47-53
    sprite('su210_09', 7)	# 54-60
    Unknown2015(-1)
    sprite('su210_10', 7)	# 61-67

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown11042(1)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)
        Unknown2004(1, 0)
    sprite('su340_00', 3)	# 1-3
    sprite('su340_01', 1)	# 4-4
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    sprite('su340_04', 1)	# 5-5
    GFX_0('suef_340_Pskill', -1)
    sprite('su340_05', 1)	# 6-6
    sprite('su340_06', 1)	# 7-7
    SFX_0('005_swing_grap_2_2')
    sprite('su340_07', 2)	# 8-9
    tag_voice(1, 'bsu106_0', 'bsu106_1', 'bsu106_2', '')
    sprite('su340_08', 1)	# 10-10	 **attackbox here**
    StartMultihit()
    physicsXImpulse(0)
    GFX_1('suef_340foot', 0)
    GFX_0('suef_340_rock', 0)
    GFX_0('suef_406_crack', 0)
    GFX_0('suef_406_OD', 0)
    Unknown23029(1, 4061, 0)
    ScreenShake(15000, 25000)
    SFX_0('209_down_normal_1')
    sprite('su340_08', 6)	# 11-16	 **attackbox here**
    Unknown2004(1, 0)
    DisableAttackRestOfMove()
    Unknown3029(0)
    sprite('su340_09', 6)	# 17-22
    sprite('su340_10', 6)	# 23-28
    sprite('su340_11', 6)	# 29-34
    sprite('su340_12', 6)	# 35-40
    Unknown30017('e7ffffff')
    sprite('su340_13', 6)	# 41-46
    sprite('su340_14ex01', 6)	# 47-52
    sprite('su340_15ex01', 6)	# 53-58
    sprite('su340_16ex01', 6)	# 59-64

@State
def CmnActChangePartnerAssistAtk_C():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('keep', 180)	# 1-180

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1700)
        AirUntechableTime(50)
        AttackP1(70)
        Hitstop(12)
        AirPushbackX(24000)
        AirPushbackY(22000)
        AirPushbackY(16000)
        AirHitstunAnimation(9)
        Unknown11056(0)
        Unknown11042(1)
        Unknown2006()

        def upon_STATE_END():
            EnableCollision(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_61():
            sendToLabel(1)

        def upon_12():
            clearUponHandler(12)
            sendToLabel(10)
    sprite('su400_00', 3)	# 1-3
    sprite('su400_01', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30017('19000000')
    Unknown26('suef_aura')
    tag_voice(1, 'bsu200_0', 'bsu200_1', 'bsu200_2', '')
    sprite('su400_02', 3)	# 7-9
    sprite('su400_03', 3)	# 10-12
    Unknown8004(100, 1, 1)
    GFX_0('suef_400_particle2', -1)
    sprite('su400_04', 2)	# 13-14	 **attackbox here**
    physicsXImpulse(50000)
    Unknown2015(250)
    SFX_0('000_airdash_1')
    GFX_0('suef_400_aura3', 0)
    sprite('su400_05', 3)	# 15-17	 **attackbox here**
    Unknown8006(100, 1, 0)
    GFX_0('suef_400', -1)
    sprite('su400_06', 2)	# 18-19	 **attackbox here**
    sprite('su400_06', 1)	# 20-20	 **attackbox here**
    sprite('su400_05', 3)	# 21-23	 **attackbox here**
    Unknown8006(100, 1, 0)
    sprite('su400_06', 3)	# 24-26	 **attackbox here**
    label(1)
    sprite('su400_07', 4)	# 27-30
    Unknown1019(50)
    clearUponHandler(61)
    Unknown26('suef_400')
    GFX_0('suef_400_aura2', 0)
    clearUponHandler(10)
    clearUponHandler(12)
    Unknown8006(100, 1, 0)
    Recovery()
    sprite('su400_21', 6)	# 31-36
    Unknown26('suef_400_particle2')
    Unknown1019(40)
    Unknown2015(-1)
    Unknown8006(100, 1, 0)
    sprite('su032_11', 6)	# 37-42
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    Unknown30017('e7ffffff')
    sprite('su032_12', 6)	# 43-48
    Unknown1084(1)
    Unknown8010(100, 1, 1)
    sprite('su032_13', 14)	# 49-62
    sprite('su032_14', 4)	# 63-66
    sprite('su032_15', 4)	# 67-70
    ExitState()
    label(10)
    sprite('su400_07', 2)	# 71-72
    Unknown26('suef_400')
    GFX_0('suef_400_aura2', 0)
    Unknown26('suef_400_particle2')
    Unknown1019(80)
    Unknown8006(100, 1, 0)
    sendToLabelUpon(2, 11)
    sprite('su400_08', 2)	# 73-74
    Unknown26('suef_400_aura2')
    Unknown2015(-1)
    Unknown8006(100, 1, 0)
    sprite('su400_09', 2)	# 75-76
    Unknown1019(80)
    sprite('su400_10', 2)	# 77-78
    sprite('su400_11', 2)	# 79-80
    Unknown1019(60)
    SFX_0('005_swing_grap_2_2')
    sprite('su400_12', 4)	# 81-84	 **attackbox here**
    physicsYImpulse(8000)
    Unknown1043()
    RefreshMultihit()
    AttackLevel_(4)
    GroundedHitstunAnimation(13)
    AirHitstunAnimation(13)
    AirPushbackX(12000)
    AirPushbackY(25000)
    YImpluseBeforeWallbounce(1600)
    PushbackX(19800)
    AirUntechableTime(55)
    Unknown9016(1)
    GFX_0('suef_400_claw', -1)
    GFX_0('suef_400_claw2', -1)
    sprite('su400_13', 4)	# 85-88
    Unknown1019(60)
    Recovery()
    sprite('su400_14', 120)	# 89-208
    Unknown1019(60)
    label(11)
    sprite('su400_15', 3)	# 209-211
    Unknown1084(1)
    Unknown8004(100, 1, 1)
    Unknown30017('efffffff')
    sprite('su400_16', 3)	# 212-214
    sprite('su400_17', 3)	# 215-217
    sprite('su400_18', 3)	# 218-220
    sprite('su400_19', 2)	# 221-222
    sprite('su400_20', 2)	# 223-224

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
    Unknown2036(114, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-600000)
    Unknown1019(4)
    label(0)
    sprite('su020_07', 4)	# 3-6
    sprite('su020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('AN_CmnActChangePartnerDDODExe')
    else:
        enterState('AN_CmnActChangePartnerDDExe')

@State
def AN_CmnActChangePartnerDDExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(2000)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(60000)
        AirPushbackY(15000)
        WallbounceReboundTime(0)
        Unknown9202(20)
        Unknown9016(1)
        Unknown11056(0)
        Unknown13024(0)
        Unknown11062(1)
        Unknown1084(1)
        setInvincible(1)
        Unknown2004(1, 0)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown23087(0)
            Unknown12046(0)
    sprite('su430_00', 3)	# 1-3
    GFX_0('suef_430_sword', -1)
    sprite('su430_01', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30017('0c000000')
    sprite('su430_02', 3)	# 7-9
    sprite('su430_03', 3)	# 10-12
    sprite('su430_04', 3)	# 13-15
    Unknown4047(128, 128, 128)
    Unknown4045('737565665f34333073776f72640000000000000000000000000000000000000067000000')
    sprite('su430_05', 3)	# 16-18
    sprite('su430_06', 3)	# 19-21
    sprite('su430_07', 3)	# 22-24
    sprite('su430_05', 3)	# 25-27
    sprite('su430_06', 3)	# 28-30
    sprite('su430_07', 3)	# 31-33
    sprite('su430_05', 3)	# 34-36
    sprite('su430_06', 3)	# 37-39
    sprite('su430_07', 3)	# 40-42
    sprite('su430_05', 3)	# 43-45
    sprite('su430_06', 3)	# 46-48
    sprite('su430_07', 3)	# 49-51
    sprite('su430_08', 6)	# 52-57
    Unknown21015('737565665f3433305f73776f7264000000000000000000000000000000000000cd10000000000000')
    sprite('su430_09', 6)	# 58-63
    sprite('su430_10', 6)	# 64-69
    sprite('su430_11', 6)	# 70-75
    sprite('su430_12', 6)	# 76-81
    sprite('su430_13', 6)	# 82-87
    sprite('su430_14', 1)	# 88-88
    sprite('su430_15', 1)	# 89-89
    sprite('su430_16', 6)	# 90-95	 **attackbox here**
    GFX_0('suef_430_slash', -1)
    SFX_3('suse_02')
    SFX_3('suse_06')
    SFX_3('suse_06')

    def upon_12():
        SFX_0('025_cleanhit_slash')
    sprite('su430_17', 3)	# 96-98
    setInvincible(0)
    sprite('su430_18', 3)	# 99-101
    sprite('su430_19', 3)	# 102-104
    sprite('su430_20', 3)	# 105-107
    sprite('su430_17', 3)	# 108-110
    sprite('su430_18', 3)	# 111-113
    sprite('su430_19', 3)	# 114-116
    sprite('su430_20', 3)	# 117-119
    sprite('su430_17', 3)	# 120-122
    sprite('su430_21', 5)	# 123-127
    sprite('su430_22', 5)	# 128-132
    sprite('su402_11ex01', 5)	# 133-137
    Unknown2015(-1)
    Unknown30017('e7ffffff')
    sprite('su402_12ex01', 5)	# 138-142
    sprite('su402_13ex01', 4)	# 143-146
    sprite('su402_14ex01', 4)	# 147-150

@State
def AN_CmnActChangePartnerDDODExe():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(1750)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        AirUntechableTime(80)
        Hitstop(0)
        Unknown11001(20, 20, 28)
        Hitstop(20)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        AirPushbackX(6000)
        AirPushbackY(20000)
        YImpluseBeforeWallbounce(1000)
        Unknown9016(1)
        Unknown11056(0)
        Unknown11064(1)
        Unknown11062(1)
        Unknown1084(1)
        setInvincible(1)
        Unknown2004(1, 0)

        def upon_STATE_END():
            EnableCollision(1)
            Unknown23087(0)
            Unknown12046(0)

        def upon_78():
            sendToLabel(10)
    sprite('su430_00', 3)	# 1-3
    GFX_0('suef_430_sword', -1)
    sprite('su430_01', 3)	# 4-6
    callSubroutine('EmissionStart')
    Unknown30017('0c000000')
    sprite('su430_02', 3)	# 7-9
    sprite('su430_03', 3)	# 10-12
    sprite('su430_04', 3)	# 13-15
    Unknown4047(128, 128, 128)
    Unknown4045('737565665f34333073776f72640000000000000000000000000000000000000067000000')
    sprite('su430_05', 3)	# 16-18
    sprite('su430_06', 3)	# 19-21
    sprite('su430_07', 3)	# 22-24
    sprite('su430_05', 3)	# 25-27
    sprite('su430_06', 3)	# 28-30
    sprite('su430_07', 3)	# 31-33
    sprite('su430_05', 3)	# 34-36
    sprite('su430_06', 3)	# 37-39
    sprite('su430_07', 3)	# 40-42
    sprite('su430_05', 3)	# 43-45
    sprite('su430_06', 3)	# 46-48
    sprite('su430_07', 3)	# 49-51
    sprite('su430_08', 6)	# 52-57
    Unknown21015('737565665f3433305f73776f7264000000000000000000000000000000000000cd10000000000000')
    sprite('su430_09', 6)	# 58-63
    sprite('su430_10', 6)	# 64-69
    sprite('su430_11', 6)	# 70-75
    sprite('su430_12', 6)	# 76-81
    sprite('su430_13', 6)	# 82-87
    sprite('su430_14', 1)	# 88-88
    sprite('su430_15', 1)	# 89-89
    sprite('su430_16', 6)	# 90-95	 **attackbox here**
    GFX_0('suef_430_slash', -1)
    SFX_3('suse_02')
    SFX_3('suse_06')
    SFX_3('suse_06')

    def upon_12():
        SFX_0('025_cleanhit_slash')
    sprite('su430_17', 3)	# 96-98
    setInvincible(0)
    sprite('su430_18', 3)	# 99-101
    sprite('su430_19', 3)	# 102-104
    sprite('su430_20', 3)	# 105-107
    sprite('su430_17', 3)	# 108-110
    sprite('su430_18', 3)	# 111-113
    sprite('su430_19', 3)	# 114-116
    sprite('su430_20', 3)	# 117-119
    sprite('su430_17', 3)	# 120-122
    sprite('su430_21', 5)	# 123-127
    sprite('su430_22', 5)	# 128-132
    sprite('su402_11ex01', 5)	# 133-137
    Unknown2015(-1)
    Unknown30017('e7ffffff')
    sprite('su402_12ex01', 5)	# 138-142
    sprite('su402_13ex01', 4)	# 143-146
    sprite('su402_14ex01', 4)	# 147-150
    ExitState()
    label(10)
    sprite('su430_16', 5)	# 151-155	 **attackbox here**
    StartMultihit()
    sprite('su430_17', 3)	# 156-158
    sprite('su430_18', 3)	# 159-161
    sprite('su430_19', 3)	# 162-164
    sprite('su430_20', 3)	# 165-167
    sprite('su430_21', 5)	# 168-172
    sprite('su430_22', 5)	# 173-177
    Unknown30017('e7ffffff')
    sprite('su402_11ex01', 5)	# 178-182
    sprite('su402_12ex01', 5)	# 183-187
    sprite('su402_13ex01', 4)	# 188-191
    sprite('su402_14ex01', 3)	# 192-194
    sprite('su402_14ex01', 1)	# 195-195
    enterState('UltimateLongAssaultDDOD_Finish')

@State
def UltimateLongAssaultDDOD_Finish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        AttackLevel_(5)
        Damage(25)
        AttackP1(100)
        AttackP2(100)
        MinimumDamagePct(100)
        GroundedHitstunAnimation(12)
        AirHitstunAnimation(12)
        AirPushbackX(30000)
        AirPushbackY(500)
        AirUntechableTime(60)
        Unknown9310(1)
        Hitstop(0)
        WallbounceReboundTime(0)
        Unknown11055(1)
        Unknown11066(1)
        Unknown11084(1)
        Unknown11108('03000000')
        Unknown11064(1)
        Unknown13024(0)
        SLOT_51 = 3
        SLOT_52 = 10

        def upon_ON_HIT_OR_BLOCK():
            ScreenShake(5000, 5000)
            Unknown1019(95)
            Unknown8006(100, 1, 1)
        setInvincible(1)
    sprite('su000_00', 1)	# 1-1
    sprite('su431_12', 5)	# 2-6
    sprite('su431_13', 5)	# 7-11
    Unknown2036(60, -1, 0)
    sprite('su431_14', 5)	# 12-16
    sprite('su431_15', 5)	# 17-21
    sprite('su431_16', 5)	# 22-26
    sprite('su431_17', 5)	# 27-31
    callSubroutine('EmissionStart')
    Unknown30017('08000000')
    sprite('su431_18', 5)	# 32-36
    tag_voice(1, 'bsu252_0', 'bsu252_1', '', '')
    sprite('su431_19', 3)	# 37-39
    GFX_0('suef_431_charge', -1)
    ScreenShake(2500, 2500)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_51):
            clearUponHandler(3)
            sendToLabel(1)
    label(0)
    sprite('su431_20', 3)	# 40-42
    ScreenShake(2500, 2500)
    SLOT_51 = (SLOT_51 + (-1))
    sprite('su431_21', 3)	# 43-45
    ScreenShake(2500, 2500)
    sprite('su431_22', 3)	# 46-48
    ScreenShake(2500, 2500)
    sprite('su431_19', 3)	# 49-51
    ScreenShake(2500, 2500)
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('su431_23', 6)	# 52-57
    Unknown23024(1)
    ScreenShake(5000, 5000)
    GFX_0('suef_431_ring', -1)
    sprite('su431_24', 6)	# 58-63
    ScreenShake(5000, 5000)
    sprite('su431_25', 2)	# 64-65	 **attackbox here**
    ScreenShake(5000, 5000)
    Unknown26('suef_431_charge')
    GFX_0('suef_431_beam', -1)
    physicsXImpulse(-40000)
    SFX_3('suse_07')
    sprite('su431_26', 2)	# 66-67

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_52):
            clearUponHandler(3)
            clearUponHandler(10)
            sendToLabel(9)
    label(2)
    sprite('su431_27', 2)	# 68-69	 **attackbox here**
    SLOT_52 = (SLOT_52 + (-1))
    RefreshMultihit()
    Unknown1019(75)
    sprite('su431_28', 2)	# 70-71	 **attackbox here**
    RefreshMultihit()
    sprite('su431_29', 2)	# 72-73	 **attackbox here**
    RefreshMultihit()
    loopRest()
    gotoLabel(2)
    label(9)
    sprite('su431_27', 3)	# 74-76	 **attackbox here**
    clearUponHandler(3)
    RefreshMultihit()
    Unknown11064(0)
    Unknown1019(70)
    sprite('su431_28', 3)	# 77-79	 **attackbox here**
    sprite('su431_29', 3)	# 80-82	 **attackbox here**
    sprite('su431_27', 4)	# 83-86	 **attackbox here**
    Unknown1019(70)
    Unknown26('suef_431_beam')
    sprite('su431_28', 4)	# 87-90	 **attackbox here**
    sprite('su431_29', 4)	# 91-94	 **attackbox here**
    sprite('su431_30', 4)	# 95-98
    Unknown1084(1)
    Unknown2015(-1)
    setInvincible(0)
    Unknown30017('e7ffffff')
    sprite('su431_31', 4)	# 99-102
    sprite('su431_32', 4)	# 103-106
    sprite('su431_33', 6)	# 107-112
    sprite('su431_34', 6)	# 113-118
    sprite('su431_35', 6)	# 119-124
    sprite('su431_36', 6)	# 125-130

@State
def CmnActChangePartnerBurst():

    def upon_IMMEDIATE():
        Unknown17021('')
        Unknown9016(1)

        def upon_41():
            clearUponHandler(41)
            sendToLabel(0)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('su251_00', 3)	# 121-123
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-1500000)
    Unknown1007(1000000)
    physicsXImpulse(55555)
    physicsYImpulse(-37037)
    sprite('su251_01', 8)	# 124-131
    sprite('su251_02', 8)	# 132-139
    GFX_0('suef_251', -1)
    sprite('su251_03', 5)	# 140-144
    sprite('su251_03', 3)	# 145-147
    Unknown2053(1)
    EnableCollision(1)
    sprite('su251_04ex01', 4)	# 148-151	 **attackbox here**
    GFX_0('suef_251_3d', -1)
    physicsXImpulse(0)
    physicsYImpulse(1000)
    sendToLabelUpon(2, 9)
    sprite('su251_05', 4)	# 152-155
    sprite('su251_06', 4)	# 156-159
    Unknown1043()
    sprite('su251_07', 4)	# 160-163
    sprite('su251_08', 4)	# 164-167
    sprite('su251_09', 3)	# 168-170
    sprite('su251_10', 3)	# 171-173
    sprite('su020_03', 3)	# 174-176
    sprite('su020_04', 3)	# 177-179
    sprite('su020_05', 3)	# 180-182
    label(1)
    sprite('su020_06', 3)	# 183-185
    sprite('su020_07', 3)	# 186-188
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('su024_00', 3)	# 189-191
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('su024_01', 9)	# 192-200
    sprite('su024_02', 3)	# 201-203
    sprite('su024_03', 3)	# 204-206
    sprite('su024_04', 3)	# 207-209

@State
def CmnActChangeReturnAppealBurst():
    sprite('su111_05', 5)	# 1-5
    sprite('su111_06', 55)	# 6-60

@Subroutine
def MouthTableInit():
    Unknown18011('bsu600def', 12643, 13153, 25392, 14129, 14177, 12899, 24884, 25399, 13361, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu600def', '001')
    Unknown18011('bsu601def', 12643, 12641, 12341, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601def', '002')
    Unknown18011('bsu602def', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu602def', '003')
    Unknown18011('bsu603def', 12643, 12897, 14389, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu603def', '004')
    Unknown18011('bsu604def', 12643, 12641, 14128, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu604def', '005')
    Unknown18011('bsu605def', 12643, 12641, 13109, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu605def', '006')
    Unknown18011('bsu606def', 12643, 14689, 25401, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu606def', '007')
    Unknown18011('bsu607def', 12643, 12641, 12850, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu607def', '008')
    Unknown18011('bsu608def', 12643, 12641, 13873, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu608def', '009')
    Unknown18011('bsu609def', 12643, 12641, 13617, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu609def', '010')
    Unknown18011('bsu610def', 12643, 12641, 12338, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu610def', '011')
    Unknown18011('bsu611def', 12643, 12641, 14643, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu611def', '012')
    Unknown18011('bsu700def', 12643, 12641, 12857, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700def', '013')
    Unknown18011('bsu701def', 12643, 12641, 13367, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701def', '014')
    Unknown18011('bsu702def', 12643, 12641, 14648, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu702def', '015')
    Unknown18011('bsu703def', 12643, 12641, 13111, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu703def', '016')
    Unknown18011('bsu704def', 12643, 12897, 13875, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu704def', '017')
    Unknown18011('bsu705def', 12643, 12897, 13106, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu705def', '018')
    Unknown18011('bsu402_0', 12643, 12897, 14129, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bsu402_1', 12643, 12897, 13105, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bsu403_0', 12643, 12641, 13622, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bsu403_1', 12643, 12641, 12854, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bsu600brg', 12643, 12641, 25398, 12337, 14177, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12341, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu600brg', '023')
    Unknown18011('bsu601brg', 12643, 12897, 13362, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601brg', '024')
    Unknown18011('bsu601bha', 12643, 13153, 14386, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601bha', '025')
    Unknown18011('bsu603bha', 12643, 12897, 12856, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu603bha', '026')
    Unknown18011('bsu605bha', 12643, 12641, 12337, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu605bha', '027')
    Unknown18011('bsu601baz', 12643, 13618, 25396, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601baz', '028')
    Unknown18011('bsu600bhz', 13923, 12641, 25401, 24887, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 24882, 13365, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu600bhz', '029')
    Unknown18011('bsu601bhz', 12643, 12897, 13367, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601bhz', '030')
    Unknown18011('bsu600pce', 12643, 12897, 13877, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu600pce', '031')
    Unknown18011('bsu601pak', 12643, 12897, 12338, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601pak', '032')
    Unknown18011('bsu601uwa', 12643, 12897, 13621, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601uwa', '033')
    Unknown18011('bsu601ume', 12643, 12897, 14386, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601ume', '034')
    Unknown18011('bsu601uva', 12643, 12897, 13622, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601uva', '035')
    Unknown18011('bsu601umi', 12643, 12897, 13880, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601umi', '036')
    Unknown18011('bsu601rrb', 12643, 12641, 25395, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25401, 24887, 25399, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 12849, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601rrb', '037')
    Unknown18011('bsu602rrb', 12643, 12897, 14132, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu602rrb', '038')
    Unknown18011('bsu600rbl', 12643, 13153, 13620, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu600rbl', '039')
    Unknown18011('bsu601pad', 12643, 13153, 14640, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601pad', '040')
    Unknown18011('bsu601rne', 12643, 13153, 12595, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu601rne', '041')
    Unknown18011('bsu701brg', 12643, 12897, 12593, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701brg', '042')
    Unknown18011('bsu701bha', 12643, 12897, 13368, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701bha', '043')
    Unknown18011('bsu700baz', 12643, 12641, 14136, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700baz', '044')
    Unknown18011('bsu700bhz', 12643, 12897, 14134, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700bhz', '045')
    Unknown18011('bsu700pce', 12643, 12897, 14129, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700pce', '046')
    Unknown18011('bsu700pak', 12643, 12641, 12338, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700pak', '047')
    Unknown18011('bsu700uwa', 12643, 12897, 13363, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700uwa', '048')
    Unknown18011('bsu701ume', 12643, 12897, 13878, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701ume', '049')
    Unknown18011('bsu701uva', 12643, 12897, 14391, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701uva', '050')
    Unknown18011('bsu700umi', 12643, 12641, 12345, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700umi', '051')
    Unknown18011('bsu700rrb', 12643, 12897, 12601, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700rrb', '052')
    Unknown18011('bsu700rbl', 12643, 12897, 12596, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu700rbl', '053')
    Unknown18011('bsu701pad', 12643, 12897, 13617, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701pad', '054')
    Unknown18011('bsu701rne', 12643, 13153, 14128, 12643, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu701rne', '055')
    Unknown18011('bsu295_0', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12643, 12641, 13411, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bsu295_1', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('bsu295_0', '056')
    Unknown30092('bsu295_1', '057')
    if SLOT_172:
        Unknown18011('bsu600def', 12643, 12899, 14177, 14179, 14177, 13667, 13155, 14177, 13411, 13411, 14177, 14179, 14177, 14179, 12641, 12899, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 14177, 12643, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu602def', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12643, 12641, 12899, 14177, 13923, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu603def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 12641, 12899, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu604def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu605def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12641, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu606def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu607def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 12641, 12899, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu608def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13155, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu609def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu610def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu611def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu702def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu703def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 12899, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu704def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12899, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu705def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu402_0', 12643, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12643, 12641, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13155, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu403_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu403_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13155, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu600brg', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13411, 14177, 14179, 14177, 14179, 13153, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601brg', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601bha', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 13155, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu603bha', 12643, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu605bha', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 12339, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu600bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601bhz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu600pce', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601pak', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24881, 25393, 13363, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601uwa', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 12641, 12899, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601ume', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601uva', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601umi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 14642, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu602rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12899, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu600rbl', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601pad', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 14177, 14179, 14177, 13923, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu601rne', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25397, 13362, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701brg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701bha', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 12899, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700bhz', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 12641, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 12641, 13155, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700pce', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12899, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700pak', 12643, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13155, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700uwa', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 12641, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701ume', 12643, 14177, 14179, 14177, 14179, 14177, 12899, 13411, 12897, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701uva', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700umi', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700rrb', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 13155, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu700rbl', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12899, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701pad', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu701rne', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13155, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu295_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('bsu295_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 12897, 13411, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    PartnerChar('brg')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bha')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('baz')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('pce')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('pak')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('uwa')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('ume')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('uva')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('umi')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('rrb')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('rbl')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('pad')
    if SLOT_ReturnVal:
        _gotolabel(220)
    PartnerChar('rne')
    if SLOT_ReturnVal:
        _gotolabel(230)
    PartnerChar('bhz')
    if SLOT_ReturnVal:
        _gotolabel(240)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(1)
    sprite('su600_tm610', 1)	# 2-2
    GFX_0('su600_ha', -1)
    GFX_0('su600_tm', -1)
    Unknown4061(5)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    if random_(2, 0, 50):
        SLOT_53 = 1
    label(2)
    sprite('su600_tm610', 1)	# 3-3
    loopRest()
    if SLOT_17:
        _gotolabel(2)
    sprite('su600_tm610', 20)	# 4-23
    sprite('su600_tm610', 1)	# 24-24
    if SLOT_53:
        SFX_1('bsu600def')
    else:
        SFX_1('bsu602def')
    label(3)
    sprite('su600_tm610', 1)	# 25-25
    if SLOT_97:
        _gotolabel(3)
    sprite('su600_tm610', 20)	# 26-45
    sprite('null', 30)	# 46-75
    Unknown21015('73753630305f68610000000000000000000000000000000000000000000000002923000000000000')
    SFX_0('015_blaze_2')
    sprite('null', 8)	# 76-83
    Unknown4061(0)
    Unknown21015('73753630305f746d0000000000000000000000000000000000000000000000002923000000000000')
    SFX_3('suse_08')
    sprite('null', 8)	# 84-91
    sprite('null', 8)	# 92-99
    sprite('null', 4)	# 100-103
    sprite('null', 4)	# 104-107
    sprite('null', 4)	# 108-111
    sprite('null', 4)	# 112-115
    sprite('null', 4)	# 116-119
    sprite('null', 4)	# 120-123
    sprite('null', 4)	# 124-127
    sprite('null', 4)	# 128-131
    sprite('null', 4)	# 132-135
    sprite('null', 4)	# 136-139
    sprite('null', 4)	# 140-143
    sprite('null', 4)	# 144-147
    sprite('null', 4)	# 148-151
    sprite('null', 4)	# 152-155
    sprite('null', 4)	# 156-159
    sprite('null', 4)	# 160-163
    sprite('null', 4)	# 164-167
    sprite('null', 4)	# 168-171
    sprite('null', 4)	# 172-175
    sprite('null', 4)	# 176-179
    sprite('su600_00', 6)	# 180-185
    Unknown1096(1000)
    GFX_0('suef_600_bloom', -1)
    Unknown3032()
    Unknown13044(1)
    Unknown3026(-16777216)
    Unknown3001(0)
    Unknown3004(4)
    sprite('su600_01', 6)	# 186-191
    sprite('su600_02', 6)	# 192-197
    Unknown2037(5)
    label(4)
    sprite('su600_00', 6)	# 198-203
    Unknown2038(-1)
    sprite('su600_01', 6)	# 204-209
    sprite('su600_02', 6)	# 210-215
    loopRest()
    if SLOT_2:
        _gotolabel(4)
    sprite('su600_03', 10)	# 216-225
    Unknown21015('737565665f3630305f626c6f6f6d0000000000000000000000000000000000002923000000000000')
    SFX_3('suse_02')
    SFX_3('suse_04')
    sprite('su600_04', 8)	# 226-233
    ScreenShake(1000, 10000)
    GFX_0('suef_600_splash', 103)
    GFX_1('suef_600ground2', -1)
    Unknown13044(1)
    Unknown23069(1)
    Unknown3025(-1, 30)
    sprite('su600_05', 6)	# 234-239
    if SLOT_53:
        SFX_1('bsu601def')
    else:
        SFX_1('bsu603def')
    label(5)
    sprite('su600_06', 6)	# 240-245
    sprite('su600_07', 6)	# 246-251
    sprite('su600_05', 6)	# 252-257
    if SLOT_97:
        _gotolabel(5)
    sprite('su600_08', 9)	# 258-266
    sprite('su600_09', 9)	# 267-275
    Unknown23018(1)
    label(6)
    sprite('su000_00', 7)	# 276-282
    sprite('su000_01', 7)	# 283-289
    sprite('su000_02', 7)	# 290-296
    sprite('su000_03', 7)	# 297-303
    sprite('su000_04', 7)	# 304-310
    sprite('su000_05', 7)	# 311-317
    sprite('su000_06', 7)	# 318-324
    sprite('su000_07', 7)	# 325-331
    sprite('su000_08', 7)	# 332-338
    sprite('su000_09', 7)	# 339-345
    loopRest()
    gotoLabel(6)
    label(10)
    sprite('null', 1)	# 346-346

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    if random_(2, 0, 25):
        SLOT_53 = 1
    elif random_(2, 0, 33):
        SLOT_53 = 2
    elif random_(2, 0, 50):
        SLOT_53 = 3
    label(11)
    sprite('null', 1)	# 347-347
    loopRest()
    if SLOT_17:
        _gotolabel(11)
    sprite('null', 20)	# 348-367
    sprite('su020_00', 4)	# 368-371
    Unknown3026(-11513776)
    GFX_0('suef_601', -1)
    SFX_0('016_explode_2')
    SFX_0('209_down_normal_1')
    GFX_0('suef_601_bloom', -1)
    GFX_0('suef_601_bloom_add', -1)
    physicsYImpulse(70000)
    ScreenShake(0, 30000)
    Unknown1043()
    sendToLabelUpon(4, 13)
    clearUponHandler(2)
    sendToLabelUpon(2, 15)
    sprite('su020_01', 4)	# 372-375
    label(12)
    sprite('su020_00', 4)	# 376-379
    sprite('su020_01', 4)	# 380-383
    loopRest()
    gotoLabel(12)
    label(13)
    sprite('su020_07', 5)	# 384-388
    Unknown26('suef_601_bloom')
    GFX_0('suef_601_bloom2', -1)
    clearUponHandler(4)
    if (SLOT_53 == 1):
        SFX_1('bsu604def')
    elif (SLOT_53 == 2):
        SFX_1('bsu606def')
    elif (SLOT_53 == 3):
        SFX_1('bsu608def')
    else:
        SFX_1('bsu610def')
    sprite('su020_08', 5)	# 389-393
    label(14)
    sprite('su020_07', 5)	# 394-398
    clearUponHandler(4)
    sprite('su020_08', 5)	# 399-403
    loopRest()
    gotoLabel(14)
    label(15)
    sprite('su024_00', 7)	# 404-410
    Unknown26('suef_601_bloom2')
    Unknown3025(-1, 30)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    sprite('su601_00', 7)	# 411-417
    sprite('su601_01', 7)	# 418-424
    GFX_0('suef_aura', 103)
    sprite('su601_02', 7)	# 425-431
    sprite('su601_03', 7)	# 432-438
    sprite('su601_04', 7)	# 439-445
    sprite('su601_05', 7)	# 446-452
    sprite('su601_06', 7)	# 453-459
    sprite('su000_00', 7)	# 460-466
    sprite('su000_01', 7)	# 467-473
    if (SLOT_53 == 1):
        SFX_1('bsu605def')
    elif (SLOT_53 == 2):
        SFX_1('bsu607def')
    elif (SLOT_53 == 3):
        SFX_1('bsu609def')
    else:
        SFX_1('bsu611def')
    sprite('su000_02', 7)	# 474-480
    sprite('su000_03', 7)	# 481-487
    sprite('su000_04', 7)	# 488-494
    sprite('su000_05', 7)	# 495-501
    sprite('su000_06', 7)	# 502-508
    sprite('su000_07', 7)	# 509-515
    sprite('su000_08', 7)	# 516-522
    sprite('su000_09', 7)	# 523-529
    Unknown23018(1)
    label(16)
    sprite('su000_00', 7)	# 530-536
    sprite('su000_01', 7)	# 537-543
    sprite('su000_02', 7)	# 544-550
    sprite('su000_03', 7)	# 551-557
    sprite('su000_04', 7)	# 558-564
    sprite('su000_05', 7)	# 565-571
    sprite('su000_06', 7)	# 572-578
    sprite('su000_07', 7)	# 579-585
    sprite('su000_08', 7)	# 586-592
    sprite('su000_09', 7)	# 593-599
    loopRest()
    gotoLabel(16)
    label(100)
    sprite('su600_tm610', 1)	# 600-600
    GFX_0('su600_ha', -1)
    GFX_0('su600_tm', -1)
    Unknown4061(5)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su600_tm610', 20)	# 601-620
    sprite('su600_tm610', 1)	# 621-621
    SFX_1('bsu600brg')
    label(101)
    sprite('su600_tm610', 1)	# 622-622
    if SLOT_97:
        _gotolabel(101)
    sprite('su600_tm610', 20)	# 623-642
    sprite('null', 30)	# 643-672
    Unknown21015('73753630305f68610000000000000000000000000000000000000000000000002923000000000000')
    SFX_0('015_blaze_2')
    sprite('null', 8)	# 673-680
    Unknown4061(0)
    Unknown21015('73753630305f746d0000000000000000000000000000000000000000000000002923000000000000')
    SFX_3('suse_08')
    sprite('null', 96)	# 681-776
    sprite('su600_00', 6)	# 777-782
    Unknown1096(1000)
    GFX_0('suef_600_bloom', -1)
    Unknown3032()
    Unknown13044(1)
    Unknown3026(-16777216)
    Unknown3001(0)
    Unknown3004(4)
    sprite('su600_01', 6)	# 783-788
    sprite('su600_02', 6)	# 789-794
    Unknown2037(5)
    label(102)
    sprite('su600_00', 6)	# 795-800
    Unknown2038(-1)
    sprite('su600_01', 6)	# 801-806
    sprite('su600_02', 6)	# 807-812
    loopRest()
    if SLOT_2:
        _gotolabel(102)
    sprite('su600_03', 10)	# 813-822
    Unknown21015('737565665f3630305f626c6f6f6d0000000000000000000000000000000000002923000000000000')
    SFX_3('suse_02')
    SFX_3('suse_04')
    sprite('su600_04', 8)	# 823-830
    ScreenShake(1000, 10000)
    GFX_0('suef_600_splash', 103)
    GFX_1('suef_600ground2', -1)
    Unknown13044(1)
    Unknown23069(1)
    Unknown3025(-1, 30)
    sprite('su600_05', 6)	# 831-836
    SFX_1('bsu601brg')
    sprite('su600_06', 6)	# 837-842
    sprite('su600_07', 6)	# 843-848
    label(103)
    sprite('su600_05', 6)	# 849-854
    sprite('su600_06', 6)	# 855-860
    sprite('su600_07', 6)	# 861-866
    if SLOT_97:
        _gotolabel(103)
    sprite('su600_05', 6)	# 867-872
    sprite('su600_06', 6)	# 873-878
    sprite('su600_07', 6)	# 879-884
    sprite('su600_08', 9)	# 885-893
    sprite('su600_09', 9)	# 894-902
    Unknown21007(24, 40)
    Unknown21011(120)
    label(104)
    sprite('su000_00', 7)	# 903-909
    sprite('su000_01', 7)	# 910-916
    sprite('su000_02', 7)	# 917-923
    sprite('su000_03', 7)	# 924-930
    sprite('su000_04', 7)	# 931-937
    sprite('su000_05', 7)	# 938-944
    sprite('su000_06', 7)	# 945-951
    sprite('su000_07', 7)	# 952-958
    sprite('su000_08', 7)	# 959-965
    sprite('su000_09', 7)	# 966-972
    loopRest()
    gotoLabel(104)
    label(110)
    sprite('su658_00', 6)	# 973-978
    Unknown1000(-1365000)
    Unknown2019(100)
    Unknown2037(1)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    sprite('su658_01', 6)	# 979-984
    sprite('su658_02', 6)	# 985-990
    sprite('su658_03', 6)	# 991-996
    label(111)
    sprite('su658_00', 6)	# 997-1002
    sprite('su658_01', 6)	# 1003-1008
    sprite('su658_02', 6)	# 1009-1014
    sprite('su658_03', 6)	# 1015-1020
    gotoLabel(111)
    label(112)
    sprite('su658_04', 9)	# 1021-1029
    SFX_1('bsu601bha')
    sprite('su658_05', 3)	# 1030-1032
    label(113)
    sprite('su658_06', 6)	# 1033-1038
    sprite('su658_07', 6)	# 1039-1044
    sprite('su658_08', 6)	# 1045-1050
    if SLOT_97:
        _gotolabel(113)
    sprite('su658_06', 6)	# 1051-1056
    sprite('su658_07', 6)	# 1057-1062
    sprite('su658_08', 6)	# 1063-1068
    Unknown21007(24, 40)

    def upon_40():
        clearUponHandler(40)
        Unknown2037(0)
    sprite('su658_06', 6)	# 1069-1074
    sprite('su658_07', 6)	# 1075-1080
    sprite('su658_08', 6)	# 1081-1086
    label(114)
    sprite('su658_06', 6)	# 1087-1092
    sprite('su658_07', 6)	# 1093-1098
    sprite('su658_08', 6)	# 1099-1104
    Unknown19(115, 2, 2)
    gotoLabel(114)
    label(115)
    sprite('su658_06', 6)	# 1105-1110
    callSubroutine('EmissionStart')
    Unknown30017('0a000000')
    SFX_0('022_magiccircle_b')
    SFX_3('suse_02')
    SFX_3('suse_04')
    sprite('su658_07', 6)	# 1111-1116
    sprite('su658_08', 6)	# 1117-1122
    SFX_1('bsu603bha')
    label(116)
    sprite('su658_06', 6)	# 1123-1128
    sprite('su658_07', 6)	# 1129-1134
    sprite('su658_08', 6)	# 1135-1140
    if SLOT_97:
        _gotolabel(116)
    sprite('su658_09', 6)	# 1141-1146
    Unknown21007(24, 40)
    sprite('su658_10', 6)	# 1147-1152
    sprite('su658_11', 6)	# 1153-1158
    sprite('su658_12', 2)	# 1159-1160
    sprite('su658_12', 4)	# 1161-1164
    sprite('su658_13', 6)	# 1165-1170
    sprite('su658_14', 6)	# 1171-1176
    GFX_0('suef_600_splash', 0)
    GFX_1('suef_600ground2', -1)
    ScreenShake(1000, 10000)
    Unknown30017('01ffffff')
    sprite('su658_15', 6)	# 1177-1182
    sprite('su658_16', 6)	# 1183-1188
    sprite('su658_17', 6)	# 1189-1194
    Unknown21011(30)
    label(117)
    sprite('su658_14', 6)	# 1195-1200
    sprite('su658_15', 6)	# 1201-1206
    sprite('su658_16', 6)	# 1207-1212
    sprite('su658_17', 6)	# 1213-1218
    gotoLabel(117)
    label(120)
    sprite('null', 1)	# 1219-1219
    if (not SLOT_158):
        Unknown1000(-1565000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('null', 10)	# 1220-1229
    sprite('su020_00', 4)	# 1230-1233
    Unknown3026(-11513776)
    GFX_0('suef_601', -1)
    SFX_0('016_explode_2')
    SFX_0('209_down_normal_1')
    GFX_0('suef_601_bloom', -1)
    GFX_0('suef_601_bloom_add', -1)
    physicsYImpulse(70000)
    ScreenShake(0, 30000)
    Unknown1043()
    sendToLabelUpon(4, 122)
    clearUponHandler(2)
    sendToLabelUpon(2, 124)
    sprite('su020_01', 4)	# 1234-1237
    label(121)
    sprite('su020_00', 4)	# 1238-1241
    sprite('su020_01', 4)	# 1242-1245
    loopRest()
    gotoLabel(121)
    label(122)
    sprite('su020_07', 5)	# 1246-1250
    Unknown26('suef_601_bloom')
    GFX_0('suef_601_bloom2', -1)
    clearUponHandler(4)
    sprite('su020_08', 5)	# 1251-1255
    label(123)
    sprite('su020_07', 5)	# 1256-1260
    clearUponHandler(4)
    sprite('su020_08', 5)	# 1261-1265
    loopRest()
    gotoLabel(123)
    label(124)
    sprite('su024_00', 7)	# 1266-1272
    Unknown26('suef_601_bloom2')
    Unknown3025(-1, 30)
    clearUponHandler(2)
    Unknown8000(100, 1, 1)
    Unknown1084(1)

    def upon_40():
        clearUponHandler(40)
        SFX_1('bsu601baz')
        Unknown23018(1)
        sendToLabel(126)
    sprite('su601_00', 7)	# 1273-1279
    sprite('su601_01', 7)	# 1280-1286
    GFX_0('suef_aura', 103)
    sprite('su601_02', 7)	# 1287-1293
    sprite('su601_03', 7)	# 1294-1300
    sprite('su601_04', 7)	# 1301-1307
    sprite('su601_05', 7)	# 1308-1314
    sprite('su601_06', 7)	# 1315-1321
    label(125)
    sprite('su000_00', 7)	# 1322-1328
    sprite('su000_01', 7)	# 1329-1335
    sprite('su000_02', 7)	# 1336-1342
    sprite('su000_03', 7)	# 1343-1349
    sprite('su000_04', 7)	# 1350-1356
    sprite('su000_05', 7)	# 1357-1363
    sprite('su000_06', 7)	# 1364-1370
    sprite('su000_07', 7)	# 1371-1377
    sprite('su000_08', 7)	# 1378-1384
    sprite('su000_09', 7)	# 1385-1391
    loopRest()
    gotoLabel(125)
    label(126)
    sprite('su001_00', 6)	# 1392-1397
    SLOT_88 = 960
    callSubroutine('EmissionStart')
    Unknown30017('11000000')
    GFX_0('suef_001', -1)
    GFX_0('suef_001_blm_2d', -1)
    SFX_0('022_magiccircle_b')
    sprite('su001_01', 6)	# 1398-1403
    sprite('su001_02', 7)	# 1404-1410
    sprite('su001_03', 8)	# 1411-1418
    sprite('su001_04', 9)	# 1419-1427
    sprite('su001_05', 9)	# 1428-1436
    sprite('su001_06', 9)	# 1437-1445
    sprite('su001_07', 8)	# 1446-1453
    sprite('su001_08', 7)	# 1454-1460
    Unknown30017('f4ffffff')
    sprite('su001_09', 6)	# 1461-1466
    sprite('su001_10', 6)	# 1467-1472
    gotoLabel(125)
    label(140)
    sprite('su611_00', 6)	# 1473-1478
    Unknown1000(-1465000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 1479-1484
    SFX_1('bsu600pce')
    sprite('su611_02', 6)	# 1485-1490
    sprite('su611_03', 6)	# 1491-1496
    sprite('su611_04', 6)	# 1497-1502
    sprite('su611_05', 7)	# 1503-1509
    sprite('su611_06', 7)	# 1510-1516
    sprite('su611_07', 5)	# 1517-1521
    sprite('su611_08', 6)	# 1522-1527
    ScreenShake(0, 10000)
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(120)
    label(141)
    sprite('su611_09', 6)	# 1528-1533
    sprite('su611_10', 6)	# 1534-1539
    sprite('su611_11', 6)	# 1540-1545
    sprite('su611_12', 6)	# 1546-1551
    loopRest()
    gotoLabel(141)
    label(150)
    sprite('su615_04', 6)	# 1552-1557
    Unknown2037(1)
    if (not SLOT_158):
        Unknown1000(-1565000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        Unknown2037(0)
        SFX_1('bsu601pak')
    label(151)
    sprite('su615_05', 6)	# 1558-1563
    sprite('su615_06', 6)	# 1564-1569
    sprite('su615_07', 6)	# 1570-1575
    sprite('su615_08', 6)	# 1576-1581
    sprite('su615_09', 6)	# 1582-1587
    sprite('su615_04', 6)	# 1588-1593
    if SLOT_97:
        _gotolabel(151)
    if SLOT_2:
        _gotolabel(151)
    sprite('su615_03', 6)	# 1594-1599
    sprite('su615_02', 6)	# 1600-1605
    sprite('su615_01', 6)	# 1606-1611
    sprite('su615_00', 6)	# 1612-1617
    Unknown23018(1)
    label(152)
    sprite('su000_00', 7)	# 1618-1624
    sprite('su000_01', 7)	# 1625-1631
    sprite('su000_02', 7)	# 1632-1638
    sprite('su000_03', 7)	# 1639-1645
    sprite('su000_04', 7)	# 1646-1652
    sprite('su000_05', 7)	# 1653-1659
    sprite('su000_06', 7)	# 1660-1666
    sprite('su000_07', 7)	# 1667-1673
    sprite('su000_08', 7)	# 1674-1680
    sprite('su000_09', 7)	# 1681-1687
    gotoLabel(152)
    label(160)
    sprite('su615_04', 6)	# 1688-1693
    if (not SLOT_158):
        Unknown1000(-1565000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        SFX_1('bsu601uwa')
        Unknown2037(78)

        def upon_CLEAR_OR_EXIT():
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                sendToLabel(162)
    label(161)
    sprite('su615_05', 6)	# 1694-1699
    sprite('su615_06', 6)	# 1700-1705
    sprite('su615_07', 6)	# 1706-1711
    sprite('su615_08', 6)	# 1712-1717
    sprite('su615_09', 6)	# 1718-1723
    sprite('su615_04', 6)	# 1724-1729
    gotoLabel(161)
    label(162)
    sprite('su615_03', 6)	# 1730-1735
    sprite('su615_02', 6)	# 1736-1741
    sprite('su615_01', 6)	# 1742-1747
    sprite('su615_00', 6)	# 1748-1753
    Unknown23018(1)
    label(163)
    sprite('su000_00', 7)	# 1754-1760
    sprite('su000_01', 7)	# 1761-1767
    sprite('su000_02', 7)	# 1768-1774
    sprite('su000_03', 7)	# 1775-1781
    sprite('su000_04', 7)	# 1782-1788
    sprite('su000_05', 7)	# 1789-1795
    sprite('su000_06', 7)	# 1796-1802
    sprite('su000_07', 7)	# 1803-1809
    sprite('su000_08', 7)	# 1810-1816
    sprite('su000_09', 7)	# 1817-1823
    gotoLabel(163)
    label(170)
    sprite('su000_00', 7)	# 1824-1830

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('su000_01', 7)	# 1831-1837
    sprite('su000_02', 7)	# 1838-1844
    sprite('su000_03', 7)	# 1845-1851
    sprite('su000_04', 7)	# 1852-1858
    sprite('su000_05', 7)	# 1859-1865
    sprite('su000_06', 7)	# 1866-1872
    sprite('su000_07', 7)	# 1873-1879
    sprite('su000_08', 7)	# 1880-1886
    sprite('su000_09', 7)	# 1887-1893
    sprite('su000_00', 7)	# 1894-1900
    gotoLabel(171)
    label(172)
    sprite('su610_01', 8)	# 1901-1908
    SFX_1('bsu601ume')
    Unknown23018(1)
    sprite('su610_02', 8)	# 1909-1916
    label(173)
    sprite('su610_03', 8)	# 1917-1924
    sprite('su610_04', 8)	# 1925-1932
    sprite('su610_05', 8)	# 1933-1940
    gotoLabel(173)
    label(180)
    sprite('su615_04', 6)	# 1941-1946
    Unknown1000(-1230000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        Unknown2037(100)
        SFX_1('bsu601uva')

        def upon_CLEAR_OR_EXIT():
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                sendToLabel(182)
    label(181)
    sprite('su615_05', 6)	# 1947-1952
    sprite('su615_06', 6)	# 1953-1958
    sprite('su615_07', 6)	# 1959-1964
    sprite('su615_08', 6)	# 1965-1970
    sprite('su615_09', 6)	# 1971-1976
    sprite('su615_04', 6)	# 1977-1982
    gotoLabel(181)
    label(182)
    sprite('su615_03', 6)	# 1983-1988
    sprite('su615_02', 6)	# 1989-1994
    sprite('su615_01', 6)	# 1995-2000
    sprite('su615_00', 6)	# 2001-2006
    Unknown23018(1)
    label(183)
    sprite('su000_00', 7)	# 2007-2013
    sprite('su000_01', 7)	# 2014-2020
    sprite('su000_02', 7)	# 2021-2027
    sprite('su000_03', 7)	# 2028-2034
    sprite('su000_04', 7)	# 2035-2041
    sprite('su000_05', 7)	# 2042-2048
    sprite('su000_06', 7)	# 2049-2055
    sprite('su000_07', 7)	# 2056-2062
    sprite('su000_08', 7)	# 2063-2069
    sprite('su000_09', 7)	# 2070-2076
    gotoLabel(183)
    label(190)
    sprite('su000_00', 7)	# 2077-2083

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('su000_01', 7)	# 2084-2090
    sprite('su000_02', 7)	# 2091-2097
    sprite('su000_03', 7)	# 2098-2104
    sprite('su000_04', 7)	# 2105-2111
    sprite('su000_05', 7)	# 2112-2118
    sprite('su000_06', 7)	# 2119-2125
    sprite('su000_07', 7)	# 2126-2132
    sprite('su000_08', 7)	# 2133-2139
    sprite('su000_09', 7)	# 2140-2146
    sprite('su000_00', 7)	# 2147-2153
    gotoLabel(191)
    label(192)
    sprite('su610_01', 8)	# 2154-2161
    SFX_1('bsu601umi')
    Unknown23018(1)
    sprite('su610_02', 8)	# 2162-2169
    label(193)
    sprite('su610_03', 8)	# 2170-2177
    sprite('su610_04', 8)	# 2178-2185
    sprite('su610_05', 8)	# 2186-2193
    gotoLabel(193)
    label(200)
    sprite('su600_tm610', 32767)	# 2194-34960
    Unknown1000(-1465000)
    GFX_0('su600_ha', -1)
    GFX_0('su600_tm', -1)
    Unknown4061(5)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        sendToLabel(201)
    label(201)
    sprite('su600_tm610', 20)	# 34961-34980
    sprite('su600_tm610', 1)	# 34981-34981
    SFX_1('bsu601rrb')
    label(202)
    sprite('su600_tm610', 1)	# 34982-34982
    if SLOT_97:
        _gotolabel(202)
    sprite('su600_tm610', 20)	# 34983-35002
    sprite('null', 30)	# 35003-35032
    Unknown21015('73753630305f68610000000000000000000000000000000000000000000000002923000000000000')
    SFX_0('015_blaze_2')
    sprite('null', 8)	# 35033-35040
    Unknown4061(0)
    Unknown21015('73753630305f746d0000000000000000000000000000000000000000000000002923000000000000')
    SFX_3('suse_08')
    sprite('null', 96)	# 35041-35136
    sprite('su600_00', 6)	# 35137-35142
    Unknown1096(1000)
    GFX_0('suef_600_bloom', -1)
    Unknown3032()
    Unknown13044(1)
    Unknown3026(-16777216)
    Unknown3001(0)
    Unknown3004(4)
    sprite('su600_01', 6)	# 35143-35148
    sprite('su600_02', 6)	# 35149-35154
    Unknown2037(5)
    label(203)
    sprite('su600_00', 6)	# 35155-35160
    Unknown2038(-1)
    sprite('su600_01', 6)	# 35161-35166
    sprite('su600_02', 6)	# 35167-35172
    loopRest()
    if SLOT_2:
        _gotolabel(203)
    sprite('su600_03', 10)	# 35173-35182
    Unknown21015('737565665f3630305f626c6f6f6d0000000000000000000000000000000000002923000000000000')
    SFX_3('suse_02')
    SFX_3('suse_04')
    sprite('su600_04', 8)	# 35183-35190
    ScreenShake(1000, 10000)
    GFX_0('suef_600_splash', 103)
    GFX_1('suef_600ground2', -1)
    Unknown13044(1)
    Unknown23069(1)
    Unknown3025(-1, 30)
    Unknown21007(24, 40)
    sprite('su600_05', 6)	# 35191-35196
    SFX_1('bsu602rrb')
    sprite('su600_06', 6)	# 35197-35202
    sprite('su600_07', 6)	# 35203-35208
    Unknown23018(1)
    label(204)
    sprite('su600_05', 6)	# 35209-35214
    sprite('su600_06', 6)	# 35215-35220
    sprite('su600_07', 6)	# 35221-35226
    gotoLabel(204)
    label(210)
    sprite('su610_01', 7)	# 35227-35233

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su610_01', 1)	# 35234-35234
    SFX_1('bsu600rbl')
    sprite('su610_02', 8)	# 35235-35242
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(120)
    label(211)
    sprite('su610_03', 8)	# 35243-35250
    sprite('su610_04', 8)	# 35251-35258
    sprite('su610_05', 8)	# 35259-35266
    gotoLabel(211)
    label(220)
    sprite('su615_04', 6)	# 35267-35272
    Unknown1000(-1230000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        Unknown2037(80)
        SFX_1('bsu601pad')

        def upon_CLEAR_OR_EXIT():
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                sendToLabel(222)
    label(221)
    sprite('su615_05', 6)	# 35273-35278
    sprite('su615_06', 6)	# 35279-35284
    sprite('su615_07', 6)	# 35285-35290
    sprite('su615_08', 6)	# 35291-35296
    sprite('su615_09', 6)	# 35297-35302
    sprite('su615_04', 6)	# 35303-35308
    gotoLabel(221)
    label(222)
    sprite('su615_03', 6)	# 35309-35314
    sprite('su615_02', 6)	# 35315-35320
    sprite('su615_01', 6)	# 35321-35326
    sprite('su615_00', 6)	# 35327-35332
    Unknown23018(1)
    label(223)
    sprite('su000_00', 7)	# 35333-35339
    sprite('su000_01', 7)	# 35340-35346
    sprite('su000_02', 7)	# 35347-35353
    sprite('su000_03', 7)	# 35354-35360
    sprite('su000_04', 7)	# 35361-35367
    sprite('su000_05', 7)	# 35368-35374
    sprite('su000_06', 7)	# 35375-35381
    sprite('su000_07', 7)	# 35382-35388
    sprite('su000_08', 7)	# 35389-35395
    sprite('su000_09', 7)	# 35396-35402
    gotoLabel(223)
    label(230)
    sprite('su615_04', 6)	# 35403-35408
    Unknown2019(1000)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0

    def upon_40():
        clearUponHandler(40)
        Unknown2037(180)
        SFX_1('bsu601rne')

        def upon_CLEAR_OR_EXIT():
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                sendToLabel(232)
    label(231)
    sprite('su615_05', 6)	# 35409-35414
    sprite('su615_06', 6)	# 35415-35420
    sprite('su615_07', 6)	# 35421-35426
    sprite('su615_08', 6)	# 35427-35432
    sprite('su615_09', 6)	# 35433-35438
    sprite('su615_04', 6)	# 35439-35444
    gotoLabel(231)
    label(232)
    sprite('su615_03', 6)	# 35445-35450
    sprite('su615_02', 6)	# 35451-35456
    sprite('su615_01', 6)	# 35457-35462
    sprite('su615_00', 6)	# 35463-35468
    Unknown23018(1)
    label(233)
    sprite('su000_00', 7)	# 35469-35475
    sprite('su000_01', 7)	# 35476-35482
    sprite('su000_02', 7)	# 35483-35489
    sprite('su000_03', 7)	# 35490-35496
    sprite('su000_04', 7)	# 35497-35503
    sprite('su000_05', 7)	# 35504-35510
    sprite('su000_06', 7)	# 35511-35517
    sprite('su000_07', 7)	# 35518-35524
    sprite('su000_08', 7)	# 35525-35531
    sprite('su000_09', 7)	# 35532-35538
    gotoLabel(233)
    label(240)
    sprite('su600_tm610', 1)	# 35539-35539
    Unknown1000(-1230000)
    GFX_0('su600_ha', -1)
    GFX_0('su600_tm', -1)
    Unknown4061(5)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su600_tm610', 20)	# 35540-35559
    sprite('su600_tm610', 1)	# 35560-35560
    SFX_1('bsu600bhz')
    Unknown2037(95)
    label(241)
    sprite('su600_tm610', 1)	# 35561-35561
    Unknown2038(-1)
    if SLOT_2:
        _gotolabel(241)
    sprite('null', 30)	# 35562-35591
    Unknown21015('73753630305f68610000000000000000000000000000000000000000000000002923000000000000')
    SFX_0('015_blaze_2')
    sprite('null', 8)	# 35592-35599
    Unknown4061(0)
    Unknown21015('73753630305f746d0000000000000000000000000000000000000000000000002923000000000000')
    SFX_3('suse_08')
    sprite('null', 96)	# 35600-35695
    sprite('su600_00', 6)	# 35696-35701
    Unknown1096(1000)
    GFX_0('suef_600_bloom', -1)
    Unknown3032()
    Unknown13044(1)
    Unknown3026(-16777216)
    Unknown3001(0)
    Unknown3004(4)
    sprite('su600_01', 6)	# 35702-35707
    sprite('su600_02', 6)	# 35708-35713
    Unknown2037(5)
    label(242)
    sprite('su600_00', 6)	# 35714-35719
    Unknown2038(-1)
    sprite('su600_01', 6)	# 35720-35725
    sprite('su600_02', 6)	# 35726-35731
    loopRest()
    if SLOT_2:
        _gotolabel(242)
    sprite('su600_03', 10)	# 35732-35741
    Unknown21015('737565665f3630305f626c6f6f6d0000000000000000000000000000000000002923000000000000')
    SFX_3('suse_02')
    SFX_3('suse_04')
    sprite('su600_04', 8)	# 35742-35749
    ScreenShake(1000, 10000)
    GFX_0('suef_600_splash', 103)
    GFX_1('suef_600ground2', -1)
    Unknown13044(1)
    Unknown23069(1)
    Unknown3025(-1, 30)
    sprite('su600_05', 6)	# 35750-35755
    SFX_1('bsu601bhz')
    sprite('su600_06', 6)	# 35756-35761
    sprite('su600_07', 6)	# 35762-35767
    label(243)
    sprite('su600_05', 6)	# 35768-35773
    sprite('su600_06', 6)	# 35774-35779
    sprite('su600_07', 6)	# 35780-35785
    if SLOT_97:
        _gotolabel(243)
    sprite('su600_05', 6)	# 35786-35791
    sprite('su600_06', 6)	# 35792-35797
    sprite('su600_07', 6)	# 35798-35803
    sprite('su600_08', 9)	# 35804-35812
    sprite('su600_09', 9)	# 35813-35821
    Unknown21007(24, 40)
    Unknown21011(120)
    label(244)
    sprite('su000_00', 7)	# 35822-35828
    sprite('su000_01', 7)	# 35829-35835
    sprite('su000_02', 7)	# 35836-35842
    sprite('su000_03', 7)	# 35843-35849
    sprite('su000_04', 7)	# 35850-35856
    sprite('su000_05', 7)	# 35857-35863
    sprite('su000_06', 7)	# 35864-35870
    sprite('su000_07', 7)	# 35871-35877
    sprite('su000_08', 7)	# 35878-35884
    sprite('su000_09', 7)	# 35885-35891
    loopRest()
    gotoLabel(244)
    label(991)
    sprite('su000_00', 1)	# 35892-35892
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('su000_00', 7)	# 35893-35899
    sprite('su000_01', 7)	# 35900-35906
    sprite('su000_02', 7)	# 35907-35913
    sprite('su000_03', 7)	# 35914-35920
    sprite('su000_04', 7)	# 35921-35927
    sprite('su000_05', 7)	# 35928-35934
    sprite('su000_06', 7)	# 35935-35941
    sprite('su000_07', 7)	# 35942-35948
    sprite('su000_08', 7)	# 35949-35955
    sprite('su000_09', 7)	# 35956-35962
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
            if PartnerChar('brg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('pce'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('pak'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('uwa'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('ume'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('uva'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('pad'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
            if PartnerChar('rne'):
                if (SLOT_145 <= 500000):
                    sendToLabel(230)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(240)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    if SLOT_108:
        gotoLabel(50)
    if SLOT_122:
        random_(2, 0, 50)
        if (not 
        if SLOT_ReturnVal:
            _gotolabel(50)):
            random_(2, 0, 50)
            if SLOT_ReturnVal:
                _gotolabel(20)
            Unknown19(30, 2, 0)
    random_(2, 0, 33)
    if (not 
    if SLOT_ReturnVal:
        _gotolabel(10)):
        random_(2, 0, 50)
        if (not 
        if SLOT_ReturnVal:
            _gotolabel(50)):
            random_(2, 0, 50)
            if SLOT_ReturnVal:
                _gotolabel(20)
            Unknown19(30, 2, 0)
    label(10)
    sprite('su610_00', 8)	# 4-11

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su610_01', 8)	# 12-19
    sprite('su610_02', 8)	# 20-27
    Unknown21011(60)
    label(11)
    sprite('su610_03', 8)	# 28-35
    sprite('su610_04', 8)	# 36-43
    sprite('su610_05', 7)	# 44-50
    sprite('su610_05', 1)	# 51-51
    Unknown23166('CmnActFDownLoop')
    if Unknown19(11, 2, 0):
        if SLOT_158:
            Unknown21011(99999)
            if (SLOT_19 >= 640000):
                Unknown20007(1)
    sprite('su610_03', 8)	# 52-59
    GFX_0('suef_610_soul', -1)
    sprite('su610_04', 8)	# 60-67
    sprite('su610_05', 8)	# 68-75
    sprite('su610_03', 8)	# 76-83
    sprite('su610_04', 8)	# 84-91
    sprite('su610_05', 8)	# 92-99
    sprite('su610_06', 8)	# 100-107
    Unknown21015('737565665f3631305f736f756c000000000000000000000000000000000000002a23000000000000')
    if SLOT_158:
        Unknown20007(0)
        Unknown20000(1)
    sprite('su610_07', 6)	# 108-113
    GFX_0('suef_610_soul2', -1)
    SFX_0('015_blaze_0')
    SFX_0('015_blaze_1')
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bsu704def', 100, 930444130, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bsu700def', 100, 930444130, 1701065008, 102, 0, 100, 930444130, 1701065264, 102, 0, 100, 930444130, 1701065520, 102, 0, 100)
    Unknown23018(1)
    sprite('su610_08', 7)	# 114-120
    sprite('su610_09', 7)	# 121-127
    sprite('su610_10', 20)	# 128-147
    sprite('su610_11', 6)	# 148-153
    sprite('su610_12', 6)	# 154-159
    sprite('su610_13', 6)	# 160-165
    label(12)
    sprite('su610_14', 6)	# 166-171
    sprite('su610_15', 6)	# 172-177
    sprite('su610_16', 6)	# 178-183
    if SLOT_97:
        _gotolabel(12)
    sprite('su610_17', 6)	# 184-189
    Unknown21015('737565665f3631305f736f756c320000000000000000000000000000000000002b23000000000000')
    SFX_3('suse_02')
    sprite('su610_18', 6)	# 190-195
    sprite('su610_19', 6)	# 196-201
    ScreenShake(0, 10000)
    Unknown23018(1)
    label(13)
    sprite('su610_20', 7)	# 202-208
    sprite('su610_21', 7)	# 209-215
    sprite('su610_22', 7)	# 216-222
    sprite('su610_23', 7)	# 223-229
    loopRest()
    gotoLabel(13)
    label(20)
    sprite('su611_00', 6)	# 230-235

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 236-241
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bsu704def', 100, 930444130, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bsu700def', 100, 930444130, 1701065008, 102, 0, 100, 930444130, 1701065264, 102, 0, 100, 930444130, 1701065520, 102, 0, 100)
    Unknown23018(1)
    sprite('su611_02', 6)	# 242-247
    sprite('su611_03', 6)	# 248-253
    sprite('su611_04', 6)	# 254-259
    sprite('su611_05', 7)	# 260-266
    sprite('su611_06', 7)	# 267-273
    sprite('su611_07', 5)	# 274-278
    sprite('su611_08', 6)	# 279-284
    ScreenShake(0, 10000)
    SFX_3('suse_02')
    label(21)
    sprite('su611_09', 6)	# 285-290
    sprite('su611_10', 6)	# 291-296
    sprite('su611_11', 6)	# 297-302
    sprite('su611_12', 6)	# 303-308
    loopRest()
    gotoLabel(21)
    label(30)
    sprite('su611_00', 6)	# 309-314

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 315-320
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bsu704def', 100, 930444130, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bsu700def', 100, 930444130, 1701065008, 102, 0, 100, 930444130, 1701065264, 102, 0, 100, 930444130, 1701065520, 102, 0, 100)
    Unknown23018(1)
    sprite('su611_02', 6)	# 321-326
    sprite('su611_03', 6)	# 327-332
    sprite('su611_04', 7)	# 333-339
    sprite('su611_05', 7)	# 340-346
    sprite('su611_06', 7)	# 347-353
    sprite('su611_07', 5)	# 354-358
    sprite('su611_08', 6)	# 359-364
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    label(31)
    sprite('su611_09', 6)	# 365-370
    sprite('su611_10', 6)	# 371-376
    sprite('su611_11', 6)	# 377-382
    sprite('su611_12', 6)	# 383-388
    loopRest()
    gotoLabel(31)
    label(50)
    sprite('su615_00', 6)	# 389-394
    Unknown2004(1, 0)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su615_01', 6)	# 395-400
    sprite('su615_02', 6)	# 401-406
    sprite('su615_03', 6)	# 407-412
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bsu704def', 100, 930444130, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bsu402_0', 100, 880112482, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bsu700def', 100, 930444130, 1701065008, 102, 0, 100, 930444130, 1701065264, 102, 0, 100, 930444130, 1701065520, 102, 0, 100)
    Unknown23018(1)
    label(51)
    sprite('su615_04', 6)	# 413-418
    sprite('su615_05', 6)	# 419-424
    sprite('su615_06', 6)	# 425-430
    sprite('su615_07', 6)	# 431-436
    sprite('su615_08', 6)	# 437-442
    sprite('su615_09', 6)	# 443-448
    loopRest()
    gotoLabel(51)
    label(100)
    sprite('su000_00', 7)	# 449-455

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('su000_01', 7)	# 456-462
    sprite('su000_02', 7)	# 463-469
    sprite('su000_03', 7)	# 470-476
    sprite('su000_04', 7)	# 477-483
    sprite('su000_05', 7)	# 484-490
    sprite('su000_06', 7)	# 491-497
    sprite('su000_07', 7)	# 498-504
    sprite('su000_08', 7)	# 505-511
    sprite('su000_09', 7)	# 512-518
    sprite('su000_00', 7)	# 519-525
    gotoLabel(101)
    label(102)
    sprite('su611_00', 6)	# 526-531

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 532-537
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    SFX_1('bsu701brg')
    sprite('su611_02', 6)	# 538-543
    sprite('su611_03', 6)	# 544-549
    sprite('su611_04', 7)	# 550-556
    sprite('su611_05', 7)	# 557-563
    sprite('su611_06', 7)	# 564-570
    sprite('su611_07', 5)	# 571-575
    sprite('su611_08', 6)	# 576-581
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown23018(1)
    label(103)
    sprite('su611_09', 6)	# 582-587
    sprite('su611_10', 6)	# 588-593
    sprite('su611_11', 6)	# 594-599
    sprite('su611_12', 6)	# 600-605
    loopRest()
    gotoLabel(103)
    label(110)
    sprite('su000_00', 7)	# 606-612

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('su000_01', 7)	# 613-619
    sprite('su000_02', 7)	# 620-626
    sprite('su000_03', 7)	# 627-633
    sprite('su000_04', 7)	# 634-640
    sprite('su000_05', 7)	# 641-647
    sprite('su000_06', 7)	# 648-654
    sprite('su000_07', 7)	# 655-661
    sprite('su000_08', 7)	# 662-668
    sprite('su000_09', 7)	# 669-675
    sprite('su000_00', 7)	# 676-682
    gotoLabel(111)
    label(112)
    sprite('su611_00', 6)	# 683-688

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 689-694
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    SFX_1('bsu701bha')
    sprite('su611_02', 6)	# 695-700
    sprite('su611_03', 6)	# 701-706
    sprite('su611_04', 7)	# 707-713
    sprite('su611_05', 7)	# 714-720
    sprite('su611_06', 7)	# 721-727
    sprite('su611_07', 5)	# 728-732
    sprite('su611_08', 6)	# 733-738
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown23018(1)
    label(113)
    sprite('su611_09', 6)	# 739-744
    sprite('su611_10', 6)	# 745-750
    sprite('su611_11', 6)	# 751-756
    sprite('su611_12', 6)	# 757-762
    loopRest()
    gotoLabel(113)
    label(120)
    sprite('su611_00', 6)	# 763-768

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 769-774
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    SFX_1('bsu700baz')
    sprite('su611_02', 6)	# 775-780
    sprite('su611_03', 6)	# 781-786
    sprite('su611_04', 7)	# 787-793
    sprite('su611_05', 7)	# 794-800
    sprite('su611_06', 7)	# 801-807
    sprite('su611_07', 5)	# 808-812
    sprite('su611_08', 6)	# 813-818
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(330)
    label(121)
    sprite('su611_09', 6)	# 819-824
    sprite('su611_10', 6)	# 825-830
    sprite('su611_11', 6)	# 831-836
    sprite('su611_12', 6)	# 837-842
    loopRest()
    gotoLabel(121)
    label(140)
    sprite('su611_00', 6)	# 843-848

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 849-854
    SFX_1('bsu700pce')
    sprite('su611_02', 6)	# 855-860
    sprite('su611_03', 6)	# 861-866
    sprite('su611_04', 7)	# 867-873
    sprite('su611_05', 7)	# 874-880
    sprite('su611_06', 7)	# 881-887
    sprite('su611_07', 5)	# 888-892
    sprite('su611_08', 6)	# 893-898
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(150)
    label(141)
    sprite('su611_09', 6)	# 899-904
    sprite('su611_10', 6)	# 905-910
    sprite('su611_11', 6)	# 911-916
    sprite('su611_12', 6)	# 917-922
    loopRest()
    gotoLabel(141)
    label(150)
    sprite('su611_00', 6)	# 923-928

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 929-934
    SFX_1('bsu700pak')
    sprite('su611_02', 6)	# 935-940
    sprite('su611_03', 6)	# 941-946
    sprite('su611_04', 7)	# 947-953
    sprite('su611_05', 7)	# 954-960
    sprite('su611_06', 7)	# 961-967
    sprite('su611_07', 5)	# 968-972
    sprite('su611_08', 6)	# 973-978
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(140)
    label(151)
    sprite('su611_09', 6)	# 979-984
    sprite('su611_10', 6)	# 985-990
    sprite('su611_11', 6)	# 991-996
    sprite('su611_12', 6)	# 997-1002
    loopRest()
    gotoLabel(151)
    label(160)
    sprite('su615_00', 6)	# 1003-1008
    Unknown2004(1, 0)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su615_01', 6)	# 1009-1014
    sprite('su615_02', 6)	# 1015-1020
    sprite('su615_03', 6)	# 1021-1026
    SFX_1('bsu700uwa')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(180)
    label(161)
    sprite('su615_04', 6)	# 1027-1032
    sprite('su615_05', 6)	# 1033-1038
    sprite('su615_06', 6)	# 1039-1044
    sprite('su615_07', 6)	# 1045-1050
    sprite('su615_08', 6)	# 1051-1056
    sprite('su615_09', 6)	# 1057-1062
    loopRest()
    gotoLabel(161)
    label(170)
    sprite('su000_00', 7)	# 1063-1069

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('su000_01', 7)	# 1070-1076
    sprite('su000_02', 7)	# 1077-1083
    sprite('su000_03', 7)	# 1084-1090
    sprite('su000_04', 7)	# 1091-1097
    sprite('su000_05', 7)	# 1098-1104
    sprite('su000_06', 7)	# 1105-1111
    sprite('su000_07', 7)	# 1112-1118
    sprite('su000_08', 7)	# 1119-1125
    sprite('su000_09', 7)	# 1126-1132
    sprite('su000_00', 7)	# 1133-1139
    gotoLabel(171)
    label(172)
    sprite('su615_00', 6)	# 1140-1145
    Unknown2004(1, 0)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su615_01', 6)	# 1146-1151
    sprite('su615_02', 6)	# 1152-1157
    sprite('su615_03', 6)	# 1158-1163
    SFX_1('bsu701ume')
    Unknown23018(1)
    label(173)
    sprite('su615_04', 6)	# 1164-1169
    sprite('su615_05', 6)	# 1170-1175
    sprite('su615_06', 6)	# 1176-1181
    sprite('su615_07', 6)	# 1182-1187
    sprite('su615_08', 6)	# 1188-1193
    sprite('su615_09', 6)	# 1194-1199
    loopRest()
    gotoLabel(173)
    label(180)
    sprite('su000_00', 7)	# 1200-1206
    Unknown2019(100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('su000_01', 7)	# 1207-1213
    sprite('su000_02', 7)	# 1214-1220
    sprite('su000_03', 7)	# 1221-1227
    sprite('su000_04', 7)	# 1228-1234
    sprite('su000_05', 7)	# 1235-1241
    sprite('su000_06', 7)	# 1242-1248
    sprite('su000_07', 7)	# 1249-1255
    sprite('su000_08', 7)	# 1256-1262
    sprite('su000_09', 7)	# 1263-1269
    sprite('su000_00', 7)	# 1270-1276
    gotoLabel(181)
    label(182)
    sprite('su611_00', 6)	# 1277-1282

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 1283-1288
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    SFX_1('bsu701uva')
    Unknown23018(1)
    sprite('su611_02', 6)	# 1289-1294
    sprite('su611_03', 6)	# 1295-1300
    sprite('su611_04', 7)	# 1301-1307
    sprite('su611_05', 7)	# 1308-1314
    sprite('su611_06', 7)	# 1315-1321
    sprite('su611_07', 5)	# 1322-1326
    sprite('su611_08', 6)	# 1327-1332
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    label(183)
    sprite('su611_09', 6)	# 1333-1338
    sprite('su611_10', 6)	# 1339-1344
    sprite('su611_11', 6)	# 1345-1350
    sprite('su611_12', 6)	# 1351-1356
    loopRest()
    gotoLabel(183)
    label(190)
    sprite('su611_00', 6)	# 1357-1362

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 1363-1368
    SFX_1('bsu700umi')
    sprite('su611_02', 6)	# 1369-1374
    sprite('su611_03', 6)	# 1375-1380
    sprite('su611_04', 7)	# 1381-1387
    sprite('su611_05', 7)	# 1388-1394
    sprite('su611_06', 7)	# 1395-1401
    sprite('su611_07', 5)	# 1402-1406
    sprite('su611_08', 6)	# 1407-1412
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(120)
    label(191)
    sprite('su611_09', 6)	# 1413-1418
    sprite('su611_10', 6)	# 1419-1424
    sprite('su611_11', 6)	# 1425-1430
    sprite('su611_12', 6)	# 1431-1436
    loopRest()
    gotoLabel(191)
    label(200)
    sprite('su611_00', 6)	# 1437-1442

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 1443-1448
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    SFX_1('bsu700rrb')
    sprite('su611_02', 6)	# 1449-1454
    sprite('su611_03', 6)	# 1455-1460
    sprite('su611_04', 7)	# 1461-1467
    sprite('su611_05', 7)	# 1468-1474
    sprite('su611_06', 7)	# 1475-1481
    sprite('su611_07', 5)	# 1482-1486
    sprite('su611_08', 6)	# 1487-1492
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(200)
    label(201)
    sprite('su611_09', 6)	# 1493-1498
    sprite('su611_10', 6)	# 1499-1504
    sprite('su611_11', 6)	# 1505-1510
    sprite('su611_12', 6)	# 1511-1516
    loopRest()
    gotoLabel(201)
    label(210)
    sprite('su300_00', 7)	# 1517-1523

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su300_01', 7)	# 1524-1530
    GFX_0('suef_300', -1)
    SFX_0('022_magiccircle_b')
    sprite('su300_02', 7)	# 1531-1537
    sprite('su300_03', 1)	# 1538-1538
    SFX_1('bsu700rbl')
    label(211)
    sprite('su300_03', 1)	# 1539-1539
    if SLOT_97:
        _gotolabel(211)
    sprite('su300_03', 30)	# 1540-1569
    sprite('su300_03', 32767)	# 1570-34336
    Unknown21007(24, 40)
    Unknown21011(210)
    label(220)
    sprite('su000_00', 7)	# 34337-34343
    Unknown2019(100)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('su000_01', 7)	# 34344-34350
    sprite('su000_02', 7)	# 34351-34357
    sprite('su000_03', 7)	# 34358-34364
    sprite('su000_04', 7)	# 34365-34371
    sprite('su000_05', 7)	# 34372-34378
    sprite('su000_06', 7)	# 34379-34385
    sprite('su000_07', 7)	# 34386-34392
    sprite('su000_08', 7)	# 34393-34399
    sprite('su000_09', 7)	# 34400-34406
    sprite('su000_00', 7)	# 34407-34413
    gotoLabel(221)
    label(222)
    sprite('su611_00', 6)	# 34414-34419

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 34420-34425
    GFX_0('suef_611', -1)
    SFX_3('suse_00')
    SFX_1('bsu701pad')
    sprite('su611_02', 6)	# 34426-34431
    sprite('su611_03', 6)	# 34432-34437
    sprite('su611_04', 7)	# 34438-34444
    sprite('su611_05', 7)	# 34445-34451
    sprite('su611_06', 7)	# 34452-34458
    sprite('su611_07', 5)	# 34459-34463
    sprite('su611_08', 6)	# 34464-34469
    GFX_0('suef_611_b', -1)
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown23018(1)
    label(223)
    sprite('su611_09', 6)	# 34470-34475
    sprite('su611_10', 6)	# 34476-34481
    sprite('su611_11', 6)	# 34482-34487
    sprite('su611_12', 6)	# 34488-34493
    loopRest()
    gotoLabel(223)
    label(230)
    sprite('su000_00', 7)	# 34494-34500

    def upon_40():
        clearUponHandler(40)
        sendToLabel(232)
    label(231)
    sprite('su000_01', 7)	# 34501-34507
    sprite('su000_02', 7)	# 34508-34514
    sprite('su000_03', 7)	# 34515-34521
    sprite('su000_04', 7)	# 34522-34528
    sprite('su000_05', 7)	# 34529-34535
    sprite('su000_06', 7)	# 34536-34542
    sprite('su000_07', 7)	# 34543-34549
    sprite('su000_08', 7)	# 34550-34556
    sprite('su000_09', 7)	# 34557-34563
    sprite('su000_00', 7)	# 34564-34570
    gotoLabel(231)
    label(232)
    sprite('su615_00', 6)	# 34571-34576
    Unknown2004(1, 0)

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su615_01', 6)	# 34577-34582
    sprite('su615_02', 6)	# 34583-34588
    sprite('su615_03', 6)	# 34589-34594
    SFX_1('bsu701rne')
    Unknown23018(1)
    label(233)
    sprite('su615_04', 6)	# 34595-34600
    sprite('su615_05', 6)	# 34601-34606
    sprite('su615_06', 6)	# 34607-34612
    sprite('su615_07', 6)	# 34613-34618
    sprite('su615_08', 6)	# 34619-34624
    sprite('su615_09', 6)	# 34625-34630
    loopRest()
    gotoLabel(233)
    label(240)
    sprite('su611_00', 6)	# 34631-34636

    def upon_CLEAR_OR_EXIT():
        SLOT_6 = 1

    def upon_STATE_END():
        clearUponHandler(3)
        SLOT_6 = 0
    sprite('su611_01', 6)	# 34637-34642
    SFX_3('suse_00')
    SFX_1('bsu700bhz')
    sprite('su611_02', 6)	# 34643-34648
    sprite('su611_03', 6)	# 34649-34654
    sprite('su611_04', 7)	# 34655-34661
    sprite('su611_05', 7)	# 34662-34668
    sprite('su611_06', 7)	# 34669-34675
    sprite('su611_07', 5)	# 34676-34680
    sprite('su611_08', 6)	# 34681-34686
    ScreenShake(0, 10000)
    SFX_3('suse_05')
    SFX_3('suse_02')
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(220)
    label(241)
    sprite('su611_09', 6)	# 34687-34692
    sprite('su611_10', 6)	# 34693-34698
    sprite('su611_11', 6)	# 34699-34704
    sprite('su611_12', 6)	# 34705-34710
    loopRest()
    gotoLabel(241)

@State
def CmnActLose():
    sprite('su620_00', 6)	# 1-6
    Unknown2004(1, 0)
    sprite('su620_01', 6)	# 7-12
    Unknown7006('bsu403_0', 100, 880112482, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('su620_02', 6)	# 13-18
    sprite('su620_03', 6)	# 19-24
    sprite('su620_04', 6)	# 25-30
    sprite('su620_05', 6)	# 31-36
    sprite('su620_06', 32767)	# 37-32803
    Unknown23018(1)