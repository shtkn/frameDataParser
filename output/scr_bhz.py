@Subroutine
def PreInit():
    Unknown12019('62687a00000000000000000000000000')
    Unknown12050(1)

@Subroutine
def MatchInit():
    DashFInitialVelocity(9000)
    DashFAccel(0)
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
    MoveMaxChainRepeat(2)
    Unknown15021(1000)
    Unknown14015(0, 300000, -200000, 350000, 2000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 400000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 600000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 350000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 320000, -200000, 150000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk5A')
    Unknown15009()
    Unknown14015(0, 280000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    Unknown15015(30, 40)
    Unknown15011(10000)
    Unknown14015(500000, 1200000, 0, 100000, 1500, 20)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    Unknown15021(4000)
    Unknown14015(-50000, 320000, 200000, 500000, 800, 10)
    Move_EndRegister()
    Move_Register('AN_NmlAtk2B_2nd', 0x1)
    Unknown14005(1)
    Move_Input_(INPUT_PRESS_B)
    Unknown15015(16, 30)
    Unknown15012(1)
    Unknown14015(100000, 400000, 250000, 1000000, 1000, 0)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 250000, -200000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown15021(0)
    Unknown14015(50000, 550000, -100000, 200000, 800, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 300000, -250000, 110000, 1500, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_2', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown14015(0, 300000, -250000, 110000, 1000, 50)
    Unknown15006(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_3', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown14015(0, 300000, -250000, 110000, 1000, 50)
    Unknown15006(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_4', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown14015(0, 300000, -250000, 110000, 1000, 50)
    Unknown15006(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A_5', 0x1)
    Move_AirGround_(0x2001)
    Move_Input_(0x1)
    Unknown14005(1)
    Unknown14015(0, 300000, -250000, 110000, 1000, 50)
    Unknown15006(50000)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Unknown15021(1)
    Unknown15006(0)
    Unknown15013(1)
    Unknown14015(600000, 1100000, -500000, -100000, 500, 1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR2B', 0x1f)
    Unknown15021(1)
    Unknown15006(0)
    Unknown15013(1)
    Unknown14015(300000, 600000, -800000, -450000, 500, 1)
    Move_EndRegister()
    Move_Register('DriveJump6', 0x1)
    Move_Input_(INPUT_PRESS_B)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('DriveJumpAttack', 0x22)
    Unknown14005(1)
    Unknown14015(0, 350000, -100000, 100000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Unknown15005(1)
    Unknown14015(0, 200000, -600000, 200000, 800, 0)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkThrow', 0x5d)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('NmlAtkBackThrow', 0x61)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 1200, 0)
    Move_EndRegister()
    Move_Register('MidAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(2000)
    Unknown14015(-50000, 400000, -200000, 250000, 250, 10)
    Move_EndRegister()
    Move_Register('MidAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15008()
    Unknown15012(2000)
    Unknown14015(50000, 550000, 0, 350000, 500, 10)
    Move_EndRegister()
    Move_Register('LowAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15013(2000)
    Unknown14015(-50000, 400000, -200000, 250000, 250, 10)
    Move_EndRegister()
    Move_Register('LowAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15009()
    Unknown15012(2000)
    Unknown14015(-50000, 450000, -250000, 150000, 250, 10)
    Move_EndRegister()
    Move_Register('HaseiAssault', INPUT_SPECIALMOVE)
    Unknown14013('CmnActInvincibleAttack')
    Move_Input_(INPUT_PRESS_D)
    Unknown14005(1)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(4000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 250000, -200000, 450000, 250, 0)
    Move_EndRegister()
    Move_Register('AntiAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15013(8000)
    Unknown15021(6000)
    Unknown14015(300000, 800000, 350000, 700000, 200, 0)
    Move_EndRegister()
    Move_Register('SPThrow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15010()
    Unknown15013(1)
    Unknown14015(0, 300000, -200000, 200000, 150, 0)
    Move_EndRegister()
    Move_Register('AirAssaultA', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('AirAssaultB', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('AirAssaultC', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Move_AirGround_(0x3086)
    Unknown15000(0)
    Unknown15003(0)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15012(1)
    Unknown15013(0)
    Unknown15006(1)
    Unknown15014(4000)
    Unknown15020(500, 1000, 10, 1000)
    Unknown14015(0, 250000, -200000, 450000, 250, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(6000)
    Unknown15013(1)
    Unknown14015(0, 350000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateAssault_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15014(6000)
    Unknown15013(1)
    Unknown14015(0, 350000, -100000, 200000, 500, 0)
    Move_EndRegister()
    Move_Register('UltimateShot', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(5000)
    Unknown15011(10000)
    Unknown14015(400000, 1500000, -200000, 0, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateShot_OD', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15013(5000)
    Unknown15011(10000)
    Unknown14015(400000, 1500000, -200000, 0, 100, 0)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15013(20000)
    Unknown14015(-300000, 300000, -200000, 1000000, 500, 1)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5B', 'DriveJump6', 10000000)
    Unknown15024('DriveJump6', 'DriveJumpAttack', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown12018(0, 'hz062_01')
    Unknown12018(1, 'hz062_03')
    Unknown12018(2, 'hz062_04')
    Unknown12018(3, 'hz062_05')
    Unknown12018(4, 'hz062_05')
    Unknown12018(5, 'hz062_06')
    Unknown12018(6, 'hz062_07')
    Unknown12018(7, 'hz041_02')
    Unknown12018(8, 'hz040_02')
    Unknown12018(9, 'hz045_02')
    Unknown12018(10, 'hz060_00')
    Unknown12018(11, 'hz060_01')
    Unknown12018(12, 'hz060_03')
    Unknown12018(13, 'hz060_05')
    Unknown12018(14, 'hz060_07')
    Unknown12018(15, 'hz060_14')
    Unknown12018(16, 'hz050_00')
    Unknown12018(17, 'hz052_00')
    Unknown12018(18, 'hz054_00')
    Unknown12018(19, 'hz000_00')
    Unknown12018(20, 'hz000_00')
    Unknown12018(25, 'hz063_00')
    Unknown12018(26, 'hz063_01')
    Unknown12018(27, 'hz063_02')
    Unknown12018(28, 'hz063_04')
    Unknown12018(29, 'hz063_11')
    Unknown12018(24, 'hz073_01')
    Unknown7010(0, 'bhz000')
    Unknown7010(1, 'bhz001')
    Unknown7010(2, 'bhz002')
    Unknown7010(3, 'bhz003')
    Unknown7010(4, 'bhz004')
    Unknown7010(5, 'bhz005')
    Unknown7010(6, 'bhz006')
    Unknown7010(7, 'bhz007')
    Unknown7010(8, 'bhz008')
    Unknown7010(9, 'bhz009')
    Unknown7010(10, 'bhz010')
    Unknown7010(15, 'bhz011')
    Unknown7010(16, 'bhz012')
    Unknown7010(17, 'bhz013')
    Unknown7010(18, 'bhz014')
    Unknown7010(19, 'bhz015')
    Unknown7010(20, 'bhz016')
    Unknown7010(21, 'bhz017')
    Unknown7010(22, 'bhz018')
    Unknown7010(23, 'bhz019')
    Unknown7010(24, 'bhz020')
    Unknown7010(25, 'bhz021')
    Unknown7010(28, 'bhz022')
    Unknown7010(29, 'bhz023')
    Unknown7010(30, 'bhz024')
    Unknown7010(31, 'bhz025')
    Unknown7010(32, 'bhz026')
    Unknown7010(33, 'bhz027')
    Unknown7010(34, 'bhz028')
    Unknown7010(35, 'bhz029')
    Unknown7010(36, 'bhz030')
    Unknown7010(37, 'bhz031')
    Unknown7010(39, 'bhz032')
    Unknown7010(42, 'bhz033')
    Unknown7010(43, 'bhz034')
    Unknown7010(44, 'bhz035')
    Unknown7010(45, 'bhz036')
    Unknown7010(46, 'bhz037')
    Unknown7010(47, 'bhz038')
    Unknown7010(48, 'bhz039')
    Unknown7010(49, 'bhz040')
    Unknown7010(50, 'bhz041')
    Unknown7010(52, 'bhz042')
    Unknown7010(53, 'bhz043')
    Unknown7010(54, 'bhz100_0')
    Unknown7010(55, 'bhz100_1')
    Unknown7010(56, 'bhz100_2')
    Unknown7010(63, 'bhz101_0')
    Unknown7010(64, 'bhz101_1')
    Unknown7010(65, 'bhz101_2')
    Unknown7010(57, 'bhz102_0')
    Unknown7010(58, 'bhz102_1')
    Unknown7010(59, 'bhz102_2')
    Unknown7010(66, 'bhz103_0')
    Unknown7010(67, 'bhz103_1')
    Unknown7010(68, 'bhz103_2')
    Unknown7010(60, 'bhz104_0')
    Unknown7010(61, 'bhz104_1')
    Unknown7010(62, 'bhz104_2')
    Unknown7010(69, 'bhz105_0')
    Unknown7010(70, 'bhz105_1')
    Unknown7010(71, 'bhz105_2')
    Unknown7010(72, 'bhz150')
    Unknown7010(73, 'bhz151')
    Unknown7010(74, 'bhz152')
    Unknown7010(85, 'bhz153')
    Unknown7010(87, 'bhz154')
    Unknown7010(88, 'bhz155')
    Unknown7010(96, 'bhz161_0')
    Unknown7010(97, 'bhz161_1')
    Unknown7010(92, 'bhz162_0')
    Unknown7010(93, 'bhz162_1')
    Unknown7010(98, 'bhz163_0')
    Unknown7010(99, 'bhz163_1')
    Unknown7010(100, 'bhz164_0')
    Unknown7010(101, 'bhz164_1')
    Unknown7010(105, 'bhz165_0')
    Unknown7010(106, 'bhz165_1')
    Unknown7010(102, 'bhz166_0')
    Unknown7010(103, 'bhz166_1')
    Unknown7010(90, 'bhz167_0')
    Unknown7010(91, 'bhz167_1')
    Unknown7010(107, 'bhz168_0')
    Unknown7010(108, 'bhz168_1')
    Unknown7010(110, 'bhz169_0')
    Unknown7010(111, 'bhz169_1')
    Unknown7010(94, 'bhz400_0')
    Unknown7010(95, 'bhz400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541737361756c740000000000000000000000000000000000')
    Unknown12059('03000000556c74696d61746541737361756c745f4f440000000000000000000000000000')
    Unknown12059('04000000556c74696d61746553686f740000000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d61746553686f745f4f440000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')

@Subroutine
def OnActionBegin():
    Unknown21015('4566664b616d61654c616e6400000000000000000000000000000000000000006500000000000000')
    if SLOT_37:
        SLOT_31 = 1500

@State
def CmnActStand():

    def upon_IMMEDIATE():
        SLOT_62 = 0
    label(0)
    sprite('hz000_00', 8)	# 1-8
    sprite('hz000_01', 8)	# 9-16
    sprite('hz000_02', 8)	# 17-24
    sprite('hz000_03', 8)	# 25-32
    sprite('hz000_04', 8)	# 33-40
    sprite('hz000_05', 8)	# 41-48
    sprite('hz000_06', 8)	# 49-56
    sprite('hz000_07', 8)	# 57-64
    sprite('hz000_08', 8)	# 65-72
    loopRest()
    random_(1, 2, 87)
    if SLOT_0:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_0:
        _gotolabel(0)
    sprite('hz001_00', 7)	# 73-79
    SLOT_88 = 960
    SFX_4('bhz000')
    sprite('hz001_01', 5)	# 80-84
    sprite('hz001_02', 8)	# 85-92
    sprite('hz001_03', 8)	# 93-100
    sprite('hz001_04', 8)	# 101-108
    sprite('hz001_05', 8)	# 109-116
    sprite('hz001_04', 8)	# 117-124
    sprite('hz001_03', 8)	# 125-132
    sprite('hz001_02', 8)	# 133-140
    sprite('hz001_03', 8)	# 141-148
    sprite('hz001_04', 8)	# 149-156
    sprite('hz001_05', 8)	# 157-164
    sprite('hz001_06', 5)	# 165-169
    sprite('hz001_07', 5)	# 170-174
    sprite('hz001_08', 5)	# 175-179
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('hz003_00', 3)	# 1-3
    sprite('hz003_01', 3)	# 4-6
    sprite('hz003_02', 3)	# 7-9

@State
def CmnActStand2Crouch():
    sprite('hz010_00', 4)	# 1-4
    sprite('hz010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('hz010_02', 8)	# 1-8
    sprite('hz010_03', 8)	# 9-16
    sprite('hz010_04', 8)	# 17-24
    sprite('hz010_05', 8)	# 25-32
    sprite('hz010_06', 8)	# 33-40
    sprite('hz010_07', 8)	# 41-48
    sprite('hz010_08', 8)	# 49-56
    sprite('hz010_09', 8)	# 57-64
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('hz013_00', 3)	# 1-3
    sprite('hz013_01', 3)	# 4-6
    sprite('hz013_02', 3)	# 7-9

@State
def CmnActCrouch2Stand():
    sprite('hz010_01', 4)	# 1-4
    sprite('hz010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('hz023_00', 2)	# 1-2
    sprite('hz023_01', 1)	# 3-3
    sprite('hz023_02', 1)	# 4-4

@State
def CmnActJumpUpper():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('hz020_00', 3)	# 1-3
    sprite('hz020_01', 3)	# 4-6
    label(10)
    sprite('hz020_00', 3)	# 7-9
    sprite('hz020_01', 3)	# 10-12
    loopRest()
    gotoLabel(10)
    label(1)
    sprite('hz021_00', 3)	# 13-15
    sprite('hz021_01', 3)	# 16-18
    label(11)
    sprite('hz021_00', 3)	# 19-21
    sprite('hz021_01', 3)	# 22-24
    loopRest()
    gotoLabel(11)
    label(2)
    sprite('hz022_00', 3)	# 25-27
    sprite('hz022_01', 3)	# 28-30
    label(22)
    sprite('hz022_00', 3)	# 31-33
    sprite('hz022_01', 3)	# 34-36
    loopRest()
    gotoLabel(22)

@State
def CmnActJumpUpperEnd():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('hz020_02', 3)	# 1-3
    sprite('hz020_03', 3)	# 4-6
    sprite('hz020_04', 3)	# 7-9
    loopRest()
    ExitState()
    label(1)
    sprite('hz021_02', 3)	# 10-12
    sprite('hz021_03', 2)	# 13-14
    sprite('hz021_04', 2)	# 15-16
    loopRest()
    ExitState()
    label(2)
    sprite('hz022_02', 3)	# 17-19
    sprite('hz022_03', 3)	# 20-22
    sprite('hz022_04', 3)	# 23-25
    loopRest()
    ExitState()

@State
def CmnActJumpDown():
    if SLOT_16:
        _gotolabel(1)
    if SLOT_15:
        _gotolabel(2)
    sprite('hz020_05', 3)	# 1-3
    sprite('hz020_06', 3)	# 4-6
    label(0)
    sprite('hz020_07', 3)	# 7-9
    sprite('hz020_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz021_05', 2)	# 13-14
    sprite('hz021_06', 3)	# 15-17
    label(11)
    sprite('hz021_07', 3)	# 18-20
    sprite('hz021_08', 3)	# 21-23
    loopRest()
    gotoLabel(11)
    label(2)
    sprite('hz022_05', 3)	# 24-26
    label(22)
    sprite('hz022_06', 3)	# 27-29
    sprite('hz022_07', 3)	# 30-32
    loopRest()
    gotoLabel(22)

@State
def CmnActJumpLanding():
    sprite('hz024_00', 3)	# 1-3
    sprite('hz024_01', 3)	# 4-6
    sprite('hz024_02', 3)	# 7-9
    sprite('hz024_03', 3)	# 10-12
    sprite('hz024_04', 3)	# 13-15
    sprite('hz024_05', 3)	# 16-18

@State
def CmnActLandingStiffLoop():
    sprite('hz024_00', 2)	# 1-2
    sprite('hz024_01', 2)	# 3-4
    sprite('hz024_02', 32767)	# 5-32771

@State
def CmnActLandingStiffEnd():
    sprite('hz024_03', 3)	# 1-3
    sprite('hz024_04', 3)	# 4-6
    sprite('hz024_05', 3)	# 7-9

@State
def CmnActFWalk():
    sprite('hz030_00', 7)	# 1-7
    sprite('hz030_01', 7)	# 8-14
    label(0)
    sprite('hz030_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)	# 22-28
    sprite('hz030_04', 7)	# 29-35
    sprite('hz030_05', 7)	# 36-42
    sprite('hz030_06', 7)	# 43-49
    sprite('hz030_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)	# 57-63
    sprite('hz030_09', 7)	# 64-70
    sprite('hz030_10', 7)	# 71-77
    sprite('hz030_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def CmnActBWalk():
    sprite('hz031_00', 7)	# 1-7
    sprite('hz031_01', 7)	# 8-14
    label(0)
    sprite('hz031_02', 7)	# 15-21
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz031_03', 7)	# 22-28
    sprite('hz031_04', 7)	# 29-35
    sprite('hz031_05', 7)	# 36-42
    sprite('hz031_06', 7)	# 43-49
    sprite('hz031_07', 7)	# 50-56
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz031_08', 7)	# 57-63
    sprite('hz031_09', 7)	# 64-70
    sprite('hz031_10', 7)	# 71-77
    sprite('hz031_11', 7)	# 78-84
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        Unknown28(8, '_NEUTRAL')
        Unknown1084(1)
        Unknown13008(1)
        Unknown13019(1)
        Unknown13014(1)
        Unknown13015(1)
        Unknown13026(1)
        Unknown13031(1)
    sprite('hz032_00', 3)	# 1-3
    physicsXImpulse(8000)
    sprite('hz032_01', 3)	# 4-6
    Unknown1019(200)
    sprite('hz032_02', 3)	# 7-9
    Unknown8007(100, 1, 1)
    Unknown1019(200)

    def upon_3():
        if (not CheckInput(0x79)):
            sendToLabel(0)
    sprite('hz032_03', 3)	# 10-12
    sprite('hz032_02', 3)	# 13-15
    sprite('hz032_04', 3)	# 16-18
    Unknown1019(80)
    label(0)
    sprite('hz032_04ex01', 3)	# 19-21
    Unknown1019(60)
    clearUponHandler(3)
    Unknown8010(100, 1, 1)
    sprite('hz032_04ex02', 3)	# 22-24
    sprite('hz032_05', 3)	# 25-27
    Unknown1019(40)
    sprite('hz032_06', 3)	# 28-30
    Unknown1019(20)
    sprite('hz032_07', 3)	# 31-33

@State
def CmnActFDashStop():
    sprite('hz032_06', 2)	# 1-2
    sprite('hz032_07', 2)	# 3-4

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
    sprite('hz033_00', 1)	# 1-1
    sprite('hz033_01', 2)	# 2-3
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1200)
    Unknown8002()
    sprite('hz033_02', 3)	# 4-6
    sprite('hz033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('hz033_03', 3)	# 10-12
    sprite('hz033_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    physicsXImpulse(0)
    Unknown8000(100, 1, 1)
    sprite('hz033_05', 2)	# 16-17
    sprite('hz033_06', 2)	# 18-19
    sprite('hz033_07', 2)	# 20-21

@State
def CmnActBDashLanding():
    pass

@State
def CmnActAirFDash():
    sprite('hz035_00', 2)	# 1-2
    sprite('hz035_01', 3)	# 3-5
    sprite('hz035_02', 3)	# 6-8
    sprite('hz035_03', 3)	# 9-11
    sprite('hz035_00', 3)	# 12-14
    sprite('hz020_04', 3)	# 15-17

@State
def CmnActAirBDash():
    sprite('hz036_00', 2)	# 1-2
    sprite('hz036_01', 2)	# 3-4
    sprite('hz036_02', 2)	# 5-6
    sprite('hz036_03', 2)	# 7-8
    sprite('hz036_01', 2)	# 9-10
    sprite('hz036_00', 2)	# 11-12
    sprite('hz020_04', 2)	# 13-14

@State
def CmnActHitStandLv1():
    sprite('hz050_00', 1)	# 1-1
    sprite('hz050_01', 1)	# 2-2
    sprite('hz050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('hz050_01', 1)	# 1-1
    sprite('hz050_02', 1)	# 2-2
    sprite('hz050_01', 2)	# 3-4
    sprite('hz050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('hz050_02', 1)	# 1-1
    sprite('hz050_03', 1)	# 2-2
    sprite('hz050_02', 2)	# 3-4
    sprite('hz050_01', 2)	# 5-6
    sprite('hz050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('hz050_03', 1)	# 1-1
    sprite('hz050_04', 1)	# 2-2
    sprite('hz050_03', 2)	# 3-4
    sprite('hz050_02', 2)	# 5-6
    sprite('hz050_01', 2)	# 7-8
    sprite('hz050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('hz050_04', 1)	# 1-1
    sprite('hz050_04', 1)	# 2-2
    sprite('hz050_04', 2)	# 3-4
    sprite('hz050_03', 2)	# 5-6
    sprite('hz050_02', 2)	# 7-8
    sprite('hz050_01', 2)	# 9-10
    sprite('hz050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('hz052_00', 1)	# 1-1
    sprite('hz052_01', 1)	# 2-2
    sprite('hz052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('hz052_01', 1)	# 1-1
    sprite('hz052_02', 1)	# 2-2
    sprite('hz052_01', 2)	# 3-4
    sprite('hz052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('hz052_02', 1)	# 1-1
    sprite('hz052_03', 1)	# 2-2
    sprite('hz052_02', 2)	# 3-4
    sprite('hz052_01', 2)	# 5-6
    sprite('hz052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('hz052_03', 1)	# 1-1
    sprite('hz052_04', 1)	# 2-2
    sprite('hz052_03', 2)	# 3-4
    sprite('hz052_02', 2)	# 5-6
    sprite('hz052_01', 2)	# 7-8
    sprite('hz052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('hz052_04', 1)	# 1-1
    sprite('hz052_04', 1)	# 2-2
    sprite('hz052_04', 2)	# 3-4
    sprite('hz052_03', 2)	# 5-6
    sprite('hz052_02', 2)	# 7-8
    sprite('hz052_01', 2)	# 9-10
    sprite('hz052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('hz054_00', 1)	# 1-1
    sprite('hz054_01', 1)	# 2-2
    sprite('hz054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('hz054_01', 1)	# 1-1
    sprite('hz054_02', 1)	# 2-2
    sprite('hz054_01', 2)	# 3-4
    sprite('hz054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('hz054_02', 1)	# 1-1
    sprite('hz054_03', 1)	# 2-2
    sprite('hz054_02', 2)	# 3-4
    sprite('hz054_01', 2)	# 5-6
    sprite('hz054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('hz054_03', 1)	# 1-1
    sprite('hz054_04', 1)	# 2-2
    sprite('hz054_03', 2)	# 3-4
    sprite('hz054_02', 2)	# 5-6
    sprite('hz054_01', 2)	# 7-8
    sprite('hz054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('hz054_04', 1)	# 1-1
    sprite('hz054_04', 1)	# 2-2
    sprite('hz054_04', 2)	# 3-4
    sprite('hz054_03', 2)	# 5-6
    sprite('hz054_02', 2)	# 7-8
    sprite('hz054_01', 2)	# 9-10
    sprite('hz054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('hz060_00', 4)	# 1-4
    label(0)
    sprite('hz060_01', 4)	# 5-8
    sprite('hz060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('hz060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('hz062_05', 3)	# 1-3
    sprite('hz062_06', 3)	# 4-6
    label(0)
    sprite('hz062_07', 3)	# 7-9
    sprite('hz062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('hz062_09', 2)	# 1-2
    sprite('hz062_10', 2)	# 3-4

@State
def CmnActBDownBound():
    sprite('hz063_06', 3)	# 1-3
    sprite('hz063_07', 3)	# 4-6
    sprite('hz063_08', 3)	# 7-9
    sprite('hz063_09', 3)	# 10-12
    sprite('hz063_10', 3)	# 13-15
    sprite('hz063_11', 3)	# 16-18

@State
def CmnActBDownLoop():
    sprite('hz063_11', 3)	# 1-3

@State
def CmnActBDown2Stand():
    sprite('hz064_00', 3)	# 1-3
    sprite('hz064_01', 3)	# 4-6
    sprite('hz064_02', 3)	# 7-9
    sprite('hz064_03', 3)	# 10-12
    sprite('hz064_04', 3)	# 13-15
    sprite('hz064_05', 3)	# 16-18
    sprite('hz064_06', 3)	# 19-21
    sprite('hz064_07', 3)	# 22-24
    sprite('hz064_08', 3)	# 25-27
    sprite('hz064_09', 3)	# 28-30
    sprite('hz064_10', 3)	# 31-33
    sprite('hz064_11', 3)	# 34-36

@State
def CmnActFDownUpper():
    sprite('hz063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('hz063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('hz063_02', 3)	# 1-3
    sprite('hz063_03', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('hz063_04', 3)	# 1-3
    sprite('hz063_05', 3)	# 4-6

@State
def CmnActFDownBound():
    sprite('hz063_06', 3)	# 1-3
    sprite('hz063_07', 3)	# 4-6
    sprite('hz063_08', 3)	# 7-9
    sprite('hz063_09', 3)	# 10-12
    sprite('hz063_10', 3)	# 13-15
    sprite('hz063_11', 3)	# 16-18

@State
def CmnActFDownLoop():
    sprite('hz063_11', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('hz064_00', 3)	# 1-3
    sprite('hz064_01', 3)	# 4-6
    sprite('hz064_02', 3)	# 7-9
    sprite('hz064_03', 3)	# 10-12
    sprite('hz064_04', 3)	# 13-15
    sprite('hz064_05', 3)	# 16-18
    sprite('hz064_06', 3)	# 19-21
    sprite('hz064_07', 3)	# 22-24
    sprite('hz064_08', 3)	# 25-27
    sprite('hz064_09', 3)	# 28-30
    sprite('hz064_10', 3)	# 31-33
    sprite('hz064_11', 3)	# 34-36

@State
def CmnActVDownUpper():
    sprite('hz062_00', 3)	# 1-3
    label(0)
    sprite('hz062_01', 3)	# 4-6
    sprite('hz062_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('hz062_03', 3)	# 1-3
    sprite('hz062_04', 3)	# 4-6

@State
def CmnActVDownDown():
    sprite('hz062_05', 3)	# 1-3
    sprite('hz062_06', 3)	# 4-6
    label(0)
    sprite('hz062_07', 3)	# 7-9
    sprite('hz062_08', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('hz062_09', 2)	# 1-2
    sprite('hz062_10', 2)	# 3-4

@State
def CmnActBlowoff():
    sprite('hz072_00', 3)	# 1-3
    sprite('hz072_01', 3)	# 4-6
    sprite('hz072_02', 3)	# 7-9
    label(0)
    sprite('hz072_01', 3)	# 10-12
    sprite('hz072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('hz074_00', 3)	# 1-3
    sprite('hz074_01', 3)	# 4-6
    sprite('hz074_02', 3)	# 7-9
    sprite('hz074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    label(0)
    sprite('hz082_00', 2)	# 1-2
    sprite('hz082_01', 2)	# 3-4
    loopRest()
    gotoLabel(0)

@State
def CmnActFreeze():
    sprite('hz071_04', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('hz073_00', 3)	# 1-3
    sprite('hz073_01', 3)	# 4-6

@State
def CmnActWallBoundDown():
    sprite('hz073_02', 3)	# 1-3
    label(0)
    sprite('hz073_03', 3)	# 4-6
    sprite('hz073_04', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('hz070_00', 4)	# 1-4
    sprite('hz070_01', 3)	# 5-7
    sprite('hz070_02', 3)	# 8-10
    sprite('hz070_03', 3)	# 11-13
    sprite('hz070_02', 4)	# 14-17
    sprite('hz070_03', 4)	# 18-21
    sprite('hz070_02', 5)	# 22-26
    sprite('hz070_03', 5)	# 27-31
    label(0)
    sprite('hz070_02', 6)	# 32-37
    sprite('hz070_03', 6)	# 38-43
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerDown():
    sprite('hz070_04', 4)	# 1-4
    sprite('hz070_05', 4)	# 5-8
    sprite('hz070_06', 4)	# 9-12
    sprite('hz070_07', 4)	# 13-16
    sprite('hz070_08', 4)	# 17-20
    sprite('hz070_09', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('hz070_10', 2)	# 1-2
    sprite('hz070_11', 2)	# 3-4
    sprite('hz070_12', 2)	# 5-6
    sprite('hz070_13', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('hz113_00', 3)	# 1-3
    sprite('hz113_01', 3)	# 4-6
    sprite('hz113_02', 3)	# 7-9

@State
def CmnActUkemiAirB():
    sprite('hz113_00', 3)	# 1-3
    sprite('hz113_01', 3)	# 4-6
    sprite('hz113_02', 3)	# 7-9

@State
def CmnActUkemiAirN():
    sprite('hz113_00', 3)	# 1-3
    sprite('hz113_01', 3)	# 4-6
    sprite('hz113_02', 3)	# 7-9

@State
def CmnActUkemiLandF():
    sprite('hz110_00', 2)	# 1-2
    sprite('hz110_01', 2)	# 3-4
    sprite('hz110_02', 2)	# 5-6
    sprite('hz110_03', 3)	# 7-9
    sprite('hz110_04', 3)	# 10-12
    sprite('hz110_06', 3)	# 13-15
    sprite('hz110_07', 3)	# 16-18
    sprite('hz110_08', 200)	# 19-218
    sprite('hz110_09', 3)	# 219-221
    sprite('hz110_10', 3)	# 222-224

@State
def CmnActUkemiLandB():
    sprite('hz111_00', 2)	# 1-2
    sprite('hz111_01', 2)	# 3-4
    sprite('hz111_02', 2)	# 5-6
    sprite('hz111_03', 3)	# 7-9
    sprite('hz111_04', 3)	# 10-12
    sprite('hz111_06', 3)	# 13-15
    sprite('hz111_07', 3)	# 16-18
    sprite('hz111_08', 200)	# 19-218
    sprite('hz111_09', 3)	# 219-221
    sprite('hz111_10', 3)	# 222-224

@State
def CmnActUkemiLandN():
    sprite('hz112_00', 2)	# 1-2
    sprite('hz112_01', 2)	# 3-4
    sprite('hz112_02', 2)	# 5-6
    sprite('hz112_03', 2)	# 7-8
    sprite('hz112_04', 2)	# 9-10
    sprite('hz112_05', 2)	# 11-12
    sprite('hz112_06', 2)	# 13-14
    sprite('hz112_07', 2)	# 15-16
    sprite('hz112_08', 2)	# 17-18

@State
def CmnActUkemiLandNLanding():
    sprite('hz024_00', 3)	# 1-3
    sprite('hz024_01', 3)	# 4-6
    sprite('hz024_02', 3)	# 7-9
    sprite('hz024_03', 3)	# 10-12
    sprite('hz024_04', 3)	# 13-15
    sprite('hz024_05', 3)	# 16-18

@State
def CmnActMidGuardPre():
    sprite('hz040_00', 3)	# 1-3	 **attackbox here**
    sprite('hz040_01', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidGuardLoop():
    sprite('hz040_04', 3)	# 1-3	 **attackbox here**
    sprite('hz040_03', 3)	# 4-6	 **attackbox here**
    GFX_0('HZEF_GuardLoop', 0)
    sprite('hz040_02', 3)	# 7-9	 **attackbox here**
    loopRest()
    label(0)
    sprite('hz040_04', 3)	# 10-12	 **attackbox here**
    sprite('hz040_03', 3)	# 13-15	 **attackbox here**
    sprite('hz040_02', 3)	# 16-18	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('hz040_01', 3)	# 1-3	 **attackbox here**
    sprite('hz040_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActMidHeavyGuardLoop():
    sprite('hz040_05', 3)	# 1-3	 **attackbox here**
    GFX_0('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz040_04', 3)	# 4-6	 **attackbox here**
    sprite('hz040_03', 3)	# 7-9	 **attackbox here**
    sprite('hz040_02', 3)	# 10-12	 **attackbox here**
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('hz040_01', 3)	# 1-3	 **attackbox here**
    sprite('hz040_00', 3)	# 4-6	 **attackbox here**

@State
def CmnActHighGuardPre():
    sprite('hz041_00', 3)	# 1-3
    sprite('hz041_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('hz041_04', 3)	# 1-3
    sprite('hz041_03', 3)	# 4-6
    GFX_0('HZEF_GuardLoop', 0)
    sprite('hz041_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('hz041_04', 3)	# 10-12
    sprite('hz041_03', 3)	# 13-15
    sprite('hz041_02', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('hz041_01', 3)	# 1-3
    sprite('hz041_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('hz041_05', 3)	# 1-3
    GFX_0('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz041_04', 3)	# 4-6
    sprite('hz041_03', 3)	# 7-9
    sprite('hz041_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('hz041_01', 3)	# 1-3
    sprite('hz041_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('hz043_00', 3)	# 1-3
    sprite('hz043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    sprite('hz043_04', 3)	# 1-3
    sprite('hz043_03', 3)	# 4-6
    GFX_0('HZEF_GuardLoop', 0)
    sprite('hz043_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('hz043_04', 3)	# 10-12
    sprite('hz043_03', 3)	# 13-15
    sprite('hz043_02', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('hz043_01', 3)	# 1-3
    sprite('hz043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('hz043_05', 3)	# 1-3
    GFX_0('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz043_04', 3)	# 4-6
    sprite('hz043_03', 3)	# 7-9
    sprite('hz043_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('hz043_01', 3)	# 1-3
    sprite('hz043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('hz045_00', 3)	# 1-3
    sprite('hz045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    sprite('hz045_04', 3)	# 1-3
    sprite('hz045_03', 3)	# 4-6
    GFX_0('HZEF_GuardLoop', 0)
    sprite('hz045_02', 3)	# 7-9
    loopRest()
    label(0)
    sprite('hz045_04', 3)	# 10-12
    sprite('hz045_03', 3)	# 13-15
    sprite('hz045_02', 3)	# 16-18
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('hz045_01', 3)	# 1-3
    sprite('hz045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('hz045_05', 3)	# 1-3
    GFX_0('HZEF_HeavyGuardLoop', 0)
    loopRest()
    label(0)
    sprite('hz045_04', 3)	# 4-6
    sprite('hz045_03', 3)	# 7-9
    sprite('hz045_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('hz045_01', 3)	# 1-3
    sprite('hz045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('hz090_00', 2)	# 1-2
    GFX_0('HZEF_HeavyGuardLoop', 0)
    sprite('hz090_01', 2)	# 3-4
    sprite('hz090_02', 1)	# 5-5
    Unknown2042(1)
    sprite('hz090_03', 6)	# 6-11
    sprite('hz090_04', 6)	# 12-17

@State
def CmnActGuardBreakCrouch():
    sprite('hz091_00', 2)	# 1-2
    GFX_0('HZEF_HeavyGuardLoop', 0)
    sprite('hz091_01', 2)	# 3-4
    sprite('hz091_02', 1)	# 5-5
    Unknown2042(1)
    sprite('hz091_03', 6)	# 6-11
    sprite('hz091_04', 6)	# 12-17

@State
def CmnActGuardBreakAir():
    sprite('hz092_00', 2)	# 1-2
    GFX_0('HZEF_HeavyGuardLoop', 0)
    sprite('hz092_01', 2)	# 3-4
    sprite('hz092_02', 1)	# 5-5
    Unknown2042(1)
    sprite('hz092_03', 6)	# 6-11
    sprite('hz092_04', 6)	# 12-17

@State
def CmnActAirTurn():
    sprite('hz025_00', 3)	# 1-3
    sprite('hz025_01', 3)	# 4-6
    sprite('hz025_02', 3)	# 7-9

@State
def CmnActLockWait():
    sprite('hz040_02', 1)	# 1-1	 **attackbox here**
    sprite('hz040_01', 3)	# 2-4	 **attackbox here**
    sprite('hz040_00', 3)	# 5-7	 **attackbox here**

@State
def CmnActLockReject():
    sprite('hz312_00', 2)	# 1-2
    sprite('hz312_01', 3)	# 3-5
    sprite('hz312_02', 3)	# 6-8	 **attackbox here**
    sprite('hz312_03', 5)	# 9-13
    sprite('hz312_04', 5)	# 14-18
    sprite('hz312_05', 3)	# 19-21
    sprite('hz312_06', 4)	# 22-25
    sprite('hz312_07', 4)	# 26-29
    sprite('hz312_08', 3)	# 30-32
    sprite('hz312_09', 3)	# 33-35

@State
def CmnActAirLockWait():
    sprite('hz045_02', 1)	# 1-1
    sprite('hz045_01', 3)	# 2-4
    sprite('hz045_00', 3)	# 5-7

@State
def CmnActAirLockReject():
    sprite('hz322_01', 3)	# 1-3
    sprite('hz322_02', 3)	# 4-6
    sprite('hz322_03', 3)	# 7-9	 **attackbox here**
    sprite('hz322_04', 5)	# 10-14
    sprite('hz322_05', 5)	# 15-19
    sprite('hz322_05', 4)	# 20-23
    sprite('hz322_06', 4)	# 24-27
    sprite('hz322_07', 3)	# 28-30
    sprite('hz322_08', 3)	# 31-33

@State
def CmnActLandSpin():
    sprite('hz071_00', 4)	# 1-4
    sprite('hz071_01', 4)	# 5-8
    label(0)
    sprite('hz071_02', 2)	# 9-10
    sprite('hz071_03', 2)	# 11-12
    sprite('hz071_04', 2)	# 13-14
    sprite('hz071_05', 2)	# 15-16
    sprite('hz071_06', 2)	# 17-18
    sprite('hz071_07', 2)	# 19-20
    sprite('hz071_08', 2)	# 21-22
    sprite('hz071_09', 2)	# 23-24
    loopRest()
    gotoLabel(0)

@State
def CmnActLandSpinDown():
    sprite('hz071_10', 6)	# 1-6
    sprite('hz071_11', 5)	# 7-11
    sprite('hz071_12', 5)	# 12-16

@State
def CmnActVertSpin():
    label(0)
    sprite('hz071_02', 2)	# 1-2
    sprite('hz071_03', 2)	# 3-4
    sprite('hz071_04', 2)	# 5-6
    sprite('hz071_05', 2)	# 7-8
    sprite('hz071_06', 2)	# 9-10
    sprite('hz071_07', 2)	# 11-12
    sprite('hz071_08', 2)	# 13-14
    sprite('hz071_09', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideAir():
    label(0)
    sprite('hz077_00', 2)	# 1-2
    sprite('hz077_01', 2)	# 3-4
    sprite('hz077_00ex01', 2)	# 5-6
    sprite('hz077_01ex01', 2)	# 7-8
    sprite('hz077_00ex02', 2)	# 9-10
    sprite('hz077_01ex02', 2)	# 11-12
    sprite('hz077_00ex03', 2)	# 13-14
    sprite('hz077_01ex03', 2)	# 15-16
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('hz077_02', 4)	# 1-4
    label(0)
    sprite('hz077_03', 3)	# 5-7
    sprite('hz077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('hz077_05', 5)	# 1-5
    sprite('hz077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    label(0)
    sprite('hz060_07', 4)	# 1-4
    sprite('hz060_08', 3)	# 5-7
    loopRest()
    gotoLabel(0)

@State
def CmnActAomukeSlideEnd():
    sprite('hz060_11', 5)	# 1-5
    sprite('hz060_12', 4)	# 6-9

@State
def CmnActBurstBegin():
    sprite('hz331_00', 2)	# 1-2
    sprite('hz331_01', 2)	# 3-4
    label(0)
    sprite('hz331_02', 3)	# 5-7
    sprite('hz331_03', 3)	# 8-10
    sprite('hz331_04', 2)	# 11-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstLoop():
    sprite('hz331_05', 2)	# 1-2
    label(0)
    sprite('hz331_06', 3)	# 3-5
    sprite('hz331_07', 3)	# 6-8
    sprite('hz331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActBurstEnd():
    sprite('hz331_09', 3)	# 1-3
    sprite('hz331_10', 3)	# 4-6

@State
def CmnActAirBurstBegin():
    sprite('hz331_11', 2)	# 1-2
    sprite('hz331_12', 2)	# 3-4
    label(0)
    sprite('hz331_02', 3)	# 5-7
    sprite('hz331_03', 2)	# 8-9
    sprite('hz331_04', 2)	# 10-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstLoop():
    sprite('hz331_05', 2)	# 1-2
    label(0)
    sprite('hz331_06', 2)	# 3-4
    sprite('hz331_07', 2)	# 5-6
    sprite('hz331_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBurstEnd():
    sprite('hz331_13', 3)	# 1-3
    sprite('hz331_14', 3)	# 4-6
    label(0)
    sprite('hz020_07', 4)	# 7-10
    sprite('hz020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveBegin():
    sprite('hz333_00', 3)	# 1-3
    sprite('hz333_01', 3)	# 4-6
    sprite('hz333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('hz333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActOverDriveLoop():
    sprite('hz333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('hz333_05', 3)	# 4-6
    sprite('hz333_06', 3)	# 7-9
    sprite('hz333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('hz333_08', 4)	# 1-4
    sprite('hz333_09', 4)	# 5-8
    sprite('hz333_10', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    sprite('hz333_11', 3)	# 1-3
    sprite('hz333_12', 3)	# 4-6
    sprite('hz333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('hz333_14', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirOverDriveLoop():
    sprite('hz333_15', 3)	# 1-3
    label(0)
    sprite('hz333_05', 3)	# 4-6
    sprite('hz333_06', 3)	# 7-9
    sprite('hz333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('hz333_16', 4)	# 1-4
    sprite('hz333_17', 4)	# 5-8
    sprite('hz333_18', 4)	# 9-12
    sprite('hz020_05', 3)	# 13-15
    sprite('hz020_06', 3)	# 16-18
    label(0)
    sprite('hz020_07', 3)	# 19-21
    sprite('hz020_08', 3)	# 22-24
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():
    sprite('hz333_00', 3)	# 1-3
    sprite('hz333_01', 3)	# 4-6
    sprite('hz333_02', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('hz333_03', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActCrossRushLoop():
    sprite('hz333_04', 3)	# 1-3
    Unknown23118(16639)
    Unknown23119(0, 20, 1)
    label(0)
    sprite('hz333_05', 3)	# 4-6
    sprite('hz333_06', 3)	# 7-9
    sprite('hz333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('hz333_08', 4)	# 1-4
    sprite('hz333_09', 4)	# 5-8
    sprite('hz333_10', 4)	# 9-12

@State
def CmnActAirCrossRushBegin():
    sprite('hz333_11', 3)	# 1-3
    sprite('hz333_12', 3)	# 4-6
    sprite('hz333_13', 3)	# 7-9
    Unknown23119(16639, 20, 1)
    sprite('hz333_14', 32767)	# 10-32776
    GFX_0('EMB_OD', -1)
    loopRest()

@State
def CmnActAirCrossRushLoop():
    sprite('hz333_15', 3)	# 1-3
    label(0)
    sprite('hz333_05', 3)	# 4-6
    sprite('hz333_06', 3)	# 7-9
    sprite('hz333_07', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('hz333_16', 4)	# 1-4
    sprite('hz333_17', 4)	# 5-8
    sprite('hz333_18', 4)	# 9-12
    sprite('hz020_05', 3)	# 13-15
    sprite('hz020_06', 3)	# 16-18
    label(0)
    sprite('hz020_07', 3)	# 19-21
    sprite('hz020_08', 3)	# 22-24
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():
    sprite('hz331_00', 2)	# 1-2
    sprite('hz331_01', 2)	# 3-4
    label(0)
    sprite('hz331_02', 3)	# 5-7
    sprite('hz331_03', 3)	# 8-10
    sprite('hz331_04', 2)	# 11-12
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('hz331_05', 2)	# 1-2
    label(0)
    sprite('hz331_06', 3)	# 3-5
    sprite('hz331_07', 3)	# 6-8
    sprite('hz331_08', 3)	# 9-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('hz331_09', 3)	# 1-3
    sprite('hz331_10', 3)	# 4-6

@State
def CmnActAirCrossChangeBegin():
    sprite('hz331_11', 2)	# 1-2
    sprite('hz331_12', 2)	# 3-4
    label(0)
    sprite('hz331_02', 3)	# 5-7
    sprite('hz331_03', 2)	# 8-9
    sprite('hz331_04', 2)	# 10-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('hz331_05', 2)	# 1-2
    label(0)
    sprite('hz331_06', 2)	# 3-4
    sprite('hz331_07', 2)	# 5-6
    sprite('hz331_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('hz331_13', 3)	# 1-3
    sprite('hz331_14', 3)	# 4-6
    label(0)
    sprite('hz020_07', 4)	# 7-10
    sprite('hz020_08', 4)	# 11-14
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

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()

        def upon_3():
            Unknown2034(0)
            if Unknown30042(25):
                Unknown2034(1)
            if (SLOT_18 == 5):
                Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
                SFX_0('301_overdrive_end')
            if (SLOT_18 == 53):
                sendToLabel(1)
    sprite('hz001_00', 3)	# 1-3
    sprite('hz001_01', 5)	# 4-8
    label(0)
    sprite('hz001_02', 5)	# 9-13
    sprite('hz001_03', 5)	# 14-18
    sprite('hz001_04', 5)	# 19-23
    sprite('hz001_05', 5)	# 24-28
    sprite('hz001_04', 5)	# 29-33
    sprite('hz001_03', 5)	# 34-38
    gotoLabel(0)
    label(1)
    sprite('hz001_06', 3)	# 39-41
    sprite('hz001_07', 3)	# 42-44
    sprite('hz001_08', 3)	# 45-47

@State
def CmnActChangePartnerAppealAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown1017()
        Unknown1022()
        Unknown1037()
        Unknown1084(1)

        def upon_3():
            Unknown2034(0)
            if Unknown30042(25):
                Unknown2034(1)
            if (SLOT_18 == 5):
                Unknown4045('65665f74656b69746f755f67000000000000000000000000000000000000000067000000')
                SFX_0('301_overdrive_end')
            if (SLOT_18 == 59):
                Unknown1018()
                Unknown1023()
                Unknown1038()
                Unknown1019(40)
                YAccel(40)
            if (SLOT_18 == 72):
                clearUponHandler(3)
                sendToLabel(1)
    sprite('hz045_00', 3)	# 1-3
    sprite('hz045_01', 3)	# 4-6
    label(0)
    sprite('hz045_04', 3)	# 7-9
    sprite('hz045_03', 3)	# 10-12
    sprite('hz045_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz045_01', 4)	# 16-19
    sprite('hz045_00', 4)	# 20-23

@State
def CmnActChangePartnerIn():

    def upon_IMMEDIATE():
        Unknown17021('')
        AttackLevel_(4)
        Unknown11028(24)
        Hitstop(20)
        Unknown9016(1)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(9)

        def upon_77():
            clearUponHandler(77)
            ScreenShake(10000, 10000)
    sprite('null', 25)	# 1-25
    sprite('hz412_04', 3)	# 26-28	 **attackbox here**
    GFX_0('Eff412Zanzo', -1)
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-240000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('hz412_05ex', 3)	# 29-31	 **attackbox here**
    sprite('hz412_04ex', 3)	# 32-34	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 35-37
    Unknown1084(1)
    sprite('hz412_06', 6)	# 38-43
    Unknown8000(100, 1, 1)
    sprite('hz412_07', 6)	# 44-49
    sprite('hz412_08', 5)	# 50-54
    sprite('hz412_09', 5)	# 55-59

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('hz033_01', 3)	# 1-3
    sprite('hz033_02', 3)	# 4-6
    sprite('hz033_03', 3)	# 7-9
    sprite('hz033_04', 3)	# 10-12
    sprite('hz033_03', 3)	# 13-15
    sprite('hz033_04', 3)	# 16-18
    sprite('hz033_03', 3)	# 19-21
    sprite('hz033_04', 3)	# 22-24
    sprite('hz033_03', 3)	# 25-27
    sprite('hz033_04', 3)	# 28-30
    sprite('hz033_03', 30)	# 31-60

@State
def CmnActChangeReturnAppeal():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('hz300_00', 6)	# 1-6
    sprite('hz300_01', 6)	# 7-12
    sprite('hz300_02', 6)	# 13-18
    sprite('hz300_03', 6)	# 19-24
    sprite('hz300_04', 6)	# 25-30
    sprite('hz300_05', 6)	# 31-36
    sprite('hz300_06', 22)	# 37-58
    sprite('hz300_07', 6)	# 59-64
    sprite('hz300_08', 6)	# 65-70
    sprite('hz300_09', 30)	# 71-100

@State
def CmnActChangeRequest():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1084(1)
        Unknown2034(0)
        Unknown2017(0)
        Unknown2053(0)
        Unknown2067(2500, 240)

        def upon_STATE_END():
            Unknown2034(1)
            Unknown2017(1)
            Unknown2053(1)
    sprite('hz300_00', 4)	# 1-4
    sprite('hz300_01', 4)	# 5-8
    sprite('hz300_02', 4)	# 9-12
    sprite('hz300_03', 4)	# 13-16
    sprite('hz300_04', 4)	# 17-20
    sprite('hz300_05', 4)	# 21-24
    sprite('hz300_06', 46)	# 25-70
    label(2)
    sprite('hz610_02', 4)	# 71-74
    sprite('hz610_01', 4)	# 75-78
    sprite('hz610_00', 4)	# 79-82

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
    sprite('hz412_04', 3)	# 121-123	 **attackbox here**
    GFX_0('Eff412Zanzo', -1)
    Unknown1086(22)
    teleportRelativeX(-150000)
    Unknown1007(2400000)
    physicsYImpulse(-80000)
    setGravity(0)
    Unknown2053(1)
    label(1)
    sprite('hz412_05ex', 3)	# 124-126	 **attackbox here**
    sprite('hz412_04ex', 3)	# 127-129	 **attackbox here**
    loopRest()
    gotoLabel(1)
    label(9)
    sprite('keep', 3)	# 130-132
    Unknown1084(1)
    sprite('hz412_06', 8)	# 133-140
    Unknown8000(100, 1, 1)
    sprite('hz412_07', 8)	# 141-148
    sprite('hz412_08', 6)	# 149-154
    sprite('hz412_09', 6)	# 155-160

@State
def CmnActChangeReturnAppealBurst():
    sprite('hz061_05', 6)	# 1-6
    sprite('hz061_06', 6)	# 7-12
    sprite('hz061_07', 12)	# 13-24
    sprite('hz061_08', 6)	# 25-30
    sprite('hz061_09', 6)	# 31-36
    sprite('hz061_10', 6)	# 37-42
    sprite('hz061_11', 6)	# 43-48
    sprite('hz061_12', 6)	# 49-54
    sprite('hz061_13', 30)	# 55-84

@State
def CmnActChangePartnerAssistAdmiss():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(99)
    sprite('null', 2)	# 1-2
    label(98)
    sprite('hz020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('hz020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(98)
    label(99)
    sprite('hz024_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerQuickIn():

    def upon_IMMEDIATE():
        Unknown28(8, '_NEUTRAL')
        Unknown3001(0)
        Unknown3004(42)

        def upon_STATE_END():
            Unknown3001(255)
            Unknown3004(0)
    sprite('hz032_03', 4)	# 1-4
    sprite('hz032_02', 4)	# 5-8
    sprite('hz032_04', 4)	# 9-12
    sprite('hz032_04ex01', 4)	# 13-16
    sprite('hz032_04ex02', 4)	# 17-20
    setInvincible(0)
    sprite('hz032_05', 3)	# 21-23
    sprite('hz032_06', 3)	# 24-26
    Unknown1084(1)
    sprite('hz032_07', 3)	# 27-29

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('hz033_00', 1)	# 1-1
    sprite('hz033_01', 2)	# 2-3
    sprite('hz033_02', 2)	# 4-5
    sprite('hz033_02', 1)	# 6-6
    sprite('hz033_03', 3)	# 7-9
    loopRest()
    label(0)
    sprite('hz033_03', 3)	# 10-12
    sprite('hz033_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz033_05', 2)	# 16-17
    sprite('hz033_06', 2)	# 18-19
    sprite('hz033_07', 2)	# 20-21

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown30040(1)
        AttackLevel_(4)
        Damage(0)
        AttackP1(70)
        Unknown11092(1)
        Unknown11046(1)
        Unknown11001(7, 30, 30)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11034(0)
        Unknown11033(2)
        AirPushbackX(0)
        Unknown11068(1)
        Unknown12052(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown30048(1)
        Unknown11042(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)

        def upon_78():
            setInvincible(1)
            sendToLabel(0)

        def upon_3():
            if SLOT_2:
                if Unknown23146('16000000436d6e4163744368616e6765506172746e657241737369737441746b5f420000'):
                    Unknown48('160000000200000053000000040000000200000053000000')
                    Unknown48('190000000200000033000000040000000200000017000000')
                    SLOT_51 = (SLOT_51 + (-300000))
                    Unknown48('160000000200000017000000190000000200000033000000')
                    Unknown36(22)
                    Unknown2017(0)
                    Unknown35()
    sprite('hz405_00', 2)	# 1-2
    sprite('hz405_01', 1)	# 3-3
    sprite('hz405_01', 1)	# 4-4
    tag_voice(1, 'bhz205_0', 'bhz205_1', 'bhz205_2', '')
    GFX_0('AntiAirWindSmoke', -1)
    GFX_0('ExBodyAuraAntiAir', -1)
    Unknown36(1)
    Unknown1007(-80000)
    Unknown35()
    sprite('hz405_02', 2)	# 5-6
    sprite('hz405_03', 2)	# 7-8
    sprite('hz405_04', 2)	# 9-10
    sprite('hz405_05', 3)	# 11-13
    SFX_3('hzse_02')
    SFX_3('hzse_04')
    GFX_0('KusariAntiAir', 109)
    Unknown38(4, 1)
    Unknown4020(4)
    Unknown21015('416e746941697257696e64536d6f6b6500000000000000000000000000000000f501000000000000')
    sprite('hz405_06', 3)	# 14-16
    sprite('hz405_06', 7)	# 17-23
    SLOT_51 = 1
    sprite('hz405_20', 2)	# 24-25
    Unknown23027()
    Unknown21015('416e746941697257696e64536d6f6b6500000000000000000000000000000000f601000000000000')
    Recovery()
    sprite('hz405_21', 2)	# 26-27
    sprite('hz405_22', 2)	# 28-29
    sprite('hz405_23', 2)	# 30-31
    sprite('hz405_24', 2)	# 32-33
    sprite('hz405_25', 2)	# 34-35
    sprite('hz405_26', 2)	# 36-37
    SFX_0('006_swing_blade_0')
    sprite('hz405_27', 3)	# 38-40
    sprite('hz405_28', 3)	# 41-43
    sprite('hz405_29', 3)	# 44-46
    sprite('hz405_30', 3)	# 47-49
    sprite('hz405_31', 3)	# 50-52
    sprite('hz405_32', 3)	# 53-55
    ExitState()
    label(0)
    clearUponHandler(78)
    Unknown2037(1)
    Unknown23029(4, 501, 0)
    Unknown2015(150)
    sprite('hz405_07', 6)	# 56-61
    sprite('hz405_08', 6)	# 62-67
    sprite('hz405_09', 2)	# 68-69
    sprite('hz405_10', 2)	# 70-71
    tag_voice(0, 'bhz206_0', 'bhz206_1', 'bhz206_2', '')
    Unknown21015('416e746941697257696e64536d6f6b6500000000000000000000000000000000f601000000000000')
    sprite('hz405_11', 2)	# 72-73
    SFX_0('011_spin_0')
    sprite('hz405_12', 2)	# 74-75
    Unknown2037(0)
    RefreshMultihit()
    Damage(3300)
    AirPushbackX(-50000)
    AirUntechableTime(120)
    Unknown11001(0, 0, 0)
    Hitstop(0)
    Unknown9178(1)
    WallbounceReboundTime(0)
    Unknown11023(1)
    sprite('hz405_13', 5)	# 76-80
    Unknown23027()
    sprite('hz405_14', 5)	# 81-85
    sprite('hz405_15', 20)	# 86-105
    sprite('hz405_15', 7)	# 106-112
    Unknown23073()
    sprite('hz405_16', 5)	# 113-117
    sprite('hz405_17', 5)	# 118-122
    sprite('hz405_18', 5)	# 123-127
    sprite('hz405_19', 5)	# 128-132

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        AttackP1(70)
        Unknown11092(1)
        Unknown11001(9, 9, 12)
        AirUntechableTime(60)
        Hitstop(6)
        GroundedHitstunAnimation(9)
        AirHitstunAnimation(9)
        PushbackX(-2000)
        AirPushbackY(-40000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(80)
        Unknown11042(1)
        SLOT_65 = 0
        sendToLabelUpon(2, 9)
        Unknown30040(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2034(1)
            Unknown2053(1)
    sprite('hz411_00', 2)	# 1-2
    Unknown1084(1)
    physicsXImpulse(10000)
    sprite('hz411_01', 2)	# 3-4
    tag_voice(1, 'bhz214_0', 'bhz214_1', 'bhz214_2', '')
    Unknown1019(50)
    sprite('hz411_02', 2)	# 5-6
    Unknown1019(50)
    sprite('hz411_03', 2)	# 7-8
    GFX_0('Eff411', -1)
    SFX_0('006_swing_blade_1')
    SFX_3('hzse_06')
    Unknown1084(1)
    sprite('hz411_04', 1)	# 9-9
    sprite('hz411_05', 2)	# 10-11	 **attackbox here**
    sprite('hz411_06', 2)	# 12-13
    sprite('hz411_07', 2)	# 14-15
    sprite('hz411_08', 2)	# 16-17
    sprite('hz411_09', 2)	# 18-19
    sprite('hz411_10', 2)	# 20-21
    Unknown1084(1)
    GFX_0('EffKamae', 0)
    GFX_0('EffKamaeLand', -1)
    sprite('hz401_00', 2)	# 22-23
    SFX_3('hzse_07')
    SFX_0('006_swing_blade_2')
    tag_voice(1, 'bhz201_0', 'bhz201_1', 'bhz201_2', '')
    GFX_0('EffSamaso', -1)
    Unknown36(1)
    teleportRelativeX(70000)
    Unknown35()
    Unknown26('EffKamae')
    Unknown26('EffKamaeLand')
    Unknown1045(20000)
    sprite('hz401_01', 3)	# 24-26
    physicsYImpulse(28000)
    physicsXImpulse(-4000)
    setGravity(2400)
    SFX_0('004_swing_grap_1_1')
    if SLOT_52:
        Unknown23119(32768, 10, 2)
    sprite('hz401_02', 3)	# 27-29
    sprite('hz401_03', 2)	# 30-31	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirUntechableTime(58)
    Unknown9071()
    AirPushbackY(42000)
    Unknown9095()
    Unknown9215()
    Hitstop(12)
    Unknown11001(0, 0, 5)
    Unknown9190(-1)
    sprite('hz401_03', 2)	# 32-33	 **attackbox here**
    sprite('hz401_04', 4)	# 34-37	 **attackbox here**
    setInvincible(0)
    sprite('hz401_05', 4)	# 38-41
    label(0)
    sprite('hz401_06', 3)	# 42-44
    sprite('hz401_07', 3)	# 45-47
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('hz401_08', 3)	# 48-50
    Unknown1084(1)
    Unknown3029(0)
    sprite('hz401_09', 3)	# 51-53
    sprite('hz401_10', 3)	# 54-56
    sprite('hz401_11', 3)	# 57-59
    sprite('hz401_12', 3)	# 60-62
    sprite('hz401_13', 2)	# 63-64
    sprite('hz401_14', 2)	# 65-66

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        AttackP1(70)
        GroundedHitstunAnimation(18)
        AirHitstunAnimation(18)
        AirPushbackX(24000)
        AirPushbackY(8000)
        AirUntechableTime(35)
        Unknown9202(10)
        Hitstop(9)
        Unknown11001(5, 5, 7)
        Unknown11034(1)
        Unknown11033(1)
        Unknown11042(1)
    sprite('hz407_00', 3)	# 1-3
    tag_voice(1, 'bhz208_0', 'bhz208_1', 'bhz208_2', '')
    GFX_0('EffLandAura', -1)
    sprite('hz407_01', 3)	# 4-6
    SFX_3('hzse_08')
    GFX_0('EffSpKensei_PS', -1)
    sprite('hz407_02', 4)	# 7-10
    sprite('hz407_03', 4)	# 11-14
    SFX_0('004_swing_grap_1_0')
    sprite('hz407_04ex', 2)	# 15-16	 **attackbox here**
    sprite('hz407_05', 3)	# 17-19
    Recovery()
    sprite('hz407_06', 3)	# 20-22
    sprite('hz407_07', 3)	# 23-25
    sprite('hz407_08', 2)	# 26-27
    sprite('hz407_09', 2)	# 28-29
    sprite('hz407_10', 2)	# 30-31
    sprite('hz407_11', 2)	# 32-33
    sprite('hz407_12', 2)	# 34-35
    sprite('hz407_13', 2)	# 36-37

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
    Unknown2036(70, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-145000)
    Unknown1019(4)
    label(0)
    sprite('hz020_07', 4)	# 3-6
    sprite('hz020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateShot_ODDDD')
    else:
        enterState('UltimateShot_DDD')

@State
def UltimateShot_DDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(1)
        Damage(100)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(1)
        Unknown11066(1)
        Unknown11064(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        Unknown23027()
        Unknown30063(1)
        Unknown1084(1)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
        Unknown13024(0)
        Unknown11069('UltimateShot_DDD')
    sprite('hz431_06', 3)	# 1-3
    setInvincible(1)
    sprite('hz431_07', 3)	# 4-6
    sprite('hz431_08', 3)	# 7-9
    sprite('hz431_06', 3)	# 10-12
    sprite('hz431_07', 2)	# 13-14
    sprite('hz431_17', 4)	# 15-18
    SFX_0('011_spin_0')
    sprite('hz431_18', 4)	# 19-22
    sprite('hz431_19', 8)	# 23-30
    sprite('hz431_20', 10)	# 31-40
    sprite('hz431_21', 5)	# 41-45
    GFX_0('UltimateWindSmoke', -1)
    GFX_1('hzef_ultimateauraopt', -1)
    GFX_0('DDBodyAura', -1)
    sprite('hz431_22ex', 1)	# 46-46	 **attackbox here**
    Unknown11072(1, 200000, 40000)
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23ex', 1)	# 47-47	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 48-48
    sprite('hz431_24ex', 1)	# 49-49	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25ex', 1)	# 50-50	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 51-51
    sprite('hz431_26ex', 1)	# 52-52	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27ex', 1)	# 53-53	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 54-54
    sprite('hz431_28ex', 1)	# 55-55	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29ex', 1)	# 56-56	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 57-57
    sprite('hz431_22ex', 1)	# 58-58	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23ex', 1)	# 59-59	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 60-60
    sprite('hz431_24ex', 1)	# 61-61	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25ex', 1)	# 62-62	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 63-63
    sprite('hz431_26ex', 1)	# 64-64	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27ex', 1)	# 65-65	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 66-66
    sprite('hz431_28ex', 1)	# 67-67	 **attackbox here**
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(20000)
    AirPushbackX(2000)
    YImpluseBeforeWallbounce(700)
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29ex', 1)	# 68-68	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('hz431_30', 3)	# 69-71
    tag_voice(1, 'bhz253_0', 'bhz253_1', '', '')
    GFX_0('HZEF_DDBackAura', -1)
    Unknown21015('556c74696d61746557696e64536d6f6b65000000000000000000000000000000ec03000000000000')
    Unknown21015('4444426f64794175726100000000000000000000000000000000000000000000ee03000000000000')
    sprite('hz431_31', 3)	# 72-74
    sprite('hz431_32', 3)	# 75-77
    sprite('hz431_33', 3)	# 78-80
    sprite('hz431_34', 3)	# 81-83
    sprite('hz431_35', 3)	# 84-86
    SFX_3('hzse_08')
    SFX_3('hzse_05')
    sprite('hz431_36', 3)	# 87-89
    sprite('hz431_37', 2)	# 90-91
    sprite('hz431_38', 3)	# 92-94
    GFX_0('EffDDSnakeFang', -1)
    ScreenShake(0, 10000)
    sprite('hz431_39', 3)	# 95-97
    ScreenShake(0, 8000)
    sprite('hz431_38', 3)	# 98-100
    ScreenShake(0, 6000)
    sprite('hz431_39', 3)	# 101-103
    ScreenShake(0, 4000)
    sprite('hz431_38', 3)	# 104-106
    ScreenShake(0, 2000)
    sprite('hz431_39', 3)	# 107-109
    sprite('hz431_38', 3)	# 110-112
    sprite('hz431_39', 3)	# 113-115
    sprite('hz431_38', 3)	# 116-118
    sprite('hz431_39', 3)	# 119-121
    sprite('hz431_40', 2)	# 122-123
    Unknown20000(1)
    Unknown21015('556c74696d61746557696e64536d6f6b65000000000000000000000000000000ed03000000000000')
    sprite('hz431_41', 1)	# 124-124
    SFX_0('009_swing_rapier_1')
    sprite('hz431_42', 3)	# 125-127	 **attackbox here**
    SFX_3('hzse_14')
    SFX_3('hzse_03')
    ScreenShake(15000, 15000)
    Unknown11064(0)
    AttackLevel_(4)
    Damage(1200)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    Unknown9202(15)
    AirUntechableTime(50)
    AirPushbackY(10000)
    AirPushbackX(50000)
    YImpluseBeforeWallbounce(1300)
    Unknown9202(20)
    Unknown9310(22)
    Hitstop(12)
    RefreshMultihit()
    Unknown20000(0)
    setInvincible(0)
    Unknown11068(1)
    Unknown11078(1)
    Unknown13024(1)
    Unknown11069('')
    Unknown23159('UltimateShotFinish')
    sprite('hz431_43', 5)	# 128-132
    Unknown2017(1)
    Unknown21015('485a45465f44444261636b417572610000000000000000000000000000000000eb03000000000000')
    Unknown21015('4444426f64794175726100000000000000000000000000000000000000000000ef03000000000000')
    sprite('hz431_44', 5)	# 133-137
    sprite('hz431_45', 5)	# 138-142
    sprite('hz431_43', 5)	# 143-147
    sprite('hz431_44', 5)	# 148-152
    sprite('hz431_45', 5)	# 153-157
    sprite('hz431_43', 5)	# 158-162
    sprite('hz431_44', 5)	# 163-167
    sprite('hz431_45', 5)	# 168-172
    sprite('hz431_46', 5)	# 173-177
    sprite('hz431_47', 5)	# 178-182
    sprite('hz431_48', 5)	# 183-187
    sprite('hz431_49', 5)	# 188-192
    SFX_3('hzse_09')
    sprite('hz431_50', 4)	# 193-196
    SFX_3('hzse_09')
    sprite('hz431_51', 4)	# 197-200
    SFX_3('hzse_09')
    sprite('hz431_52', 3)	# 201-203
    SFX_0('007_swing_knife_2')
    sprite('hz431_53', 12)	# 204-215
    sprite('hz431_55', 4)	# 216-219

@State
def UltimateShot_ODDDD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        AttackLevel_(1)
        Damage(50)
        AttackP1(100)
        AttackP2(100)
        Unknown11091(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(2)
        Unknown11066(1)
        Unknown11064(1)
        Unknown9016(1)
        Unknown11108('03000000')
        Unknown30063(1)
        Unknown2004(1, 0)
        SLOT_64 = 1

        def upon_STATE_END():
            SLOT_64 = 0

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(100)

        def upon_STATE_END():
            Unknown2017(1)
            Unknown2053(1)
            Unknown2034(1)
        Unknown13024(0)
        Unknown11069('UltimateShot_ODDDD')
    sprite('hz431_06', 3)	# 1-3
    setInvincible(1)
    sprite('hz431_07', 3)	# 4-6
    sprite('hz431_08', 3)	# 7-9
    sprite('hz431_06', 3)	# 10-12
    sprite('hz431_07', 2)	# 13-14
    sprite('hz431_17', 4)	# 15-18
    SFX_0('011_spin_0')
    sprite('hz431_18', 4)	# 19-22
    sprite('hz431_19', 8)	# 23-30
    sprite('hz431_20', 10)	# 31-40
    sprite('hz431_21', 5)	# 41-45
    GFX_0('UltimateWindSmoke', -1)
    GFX_1('hzef_ultimateauraopt', -1)
    GFX_0('DDBodyAura', -1)
    sprite('hz431_22ex', 1)	# 46-46	 **attackbox here**
    Unknown11072(1, 200000, 40000)
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23ex', 1)	# 47-47	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 48-48
    sprite('hz431_24ex', 1)	# 49-49	 **attackbox here**
    setInvincible(0)
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25ex', 1)	# 50-50	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 51-51
    sprite('hz431_26ex', 1)	# 52-52	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27ex', 1)	# 53-53	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 54-54
    sprite('hz431_28ex', 1)	# 55-55	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29ex', 1)	# 56-56	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 57-57
    sprite('hz431_22ex', 1)	# 58-58	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23ex', 1)	# 59-59	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 60-60
    sprite('hz431_24ex', 1)	# 61-61	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25ex', 1)	# 62-62	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 63-63
    sprite('hz431_26ex', 1)	# 64-64	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27ex', 1)	# 65-65	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 66-66
    sprite('hz431_28ex', 1)	# 67-67	 **attackbox here**
    RefreshMultihit()
    sprite('hz431_29ex', 1)	# 68-68	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    Hitstop(1)
    sprite('hz431_22ex', 1)	# 69-69	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 70-70
    sprite('hz431_24ex', 1)	# 71-71	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 72-72
    sprite('hz431_26ex', 1)	# 73-73	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 74-74
    sprite('hz431_28ex', 1)	# 75-75	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 76-76
    sprite('hz431_22ex', 1)	# 77-77	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 78-78
    sprite('hz431_24ex', 1)	# 79-79	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 80-80
    sprite('hz431_26ex', 1)	# 81-81	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 82-82
    sprite('hz431_28ex', 1)	# 83-83	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29ex', 1)	# 84-84	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('hz431_22ex', 1)	# 85-85	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 86-86
    sprite('hz431_24ex', 1)	# 87-87	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 88-88
    sprite('hz431_26ex', 1)	# 89-89	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 90-90
    sprite('hz431_28ex', 1)	# 91-91	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 92-92
    sprite('hz431_22ex', 1)	# 93-93	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 94-94
    sprite('hz431_24ex', 1)	# 95-95	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 96-96
    sprite('hz431_26ex', 1)	# 97-97	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 98-98
    sprite('hz431_28ex', 1)	# 99-99	 **attackbox here**
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(20000)
    AirPushbackX(2000)
    YImpluseBeforeWallbounce(700)
    Unknown11072(1, 200000, 40000)
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29ex', 1)	# 100-100	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('hz431_30', 3)	# 101-103
    sprite('hz431_31', 3)	# 104-106
    sprite('hz431_32', 3)	# 107-109
    sprite('hz431_33', 3)	# 110-112
    Unknown21015('556c74696d61746557696e64536d6f6b65000000000000000000000000000000ed03000000000000')
    SFX_0('022_magiccircle_c')
    sprite('hz432_10', 3)	# 113-115
    GFX_0('HZEF_DDBackAura', -1)
    sprite('hz432_11', 3)	# 116-118
    sprite('hz432_12', 3)	# 119-121
    Unknown21015('4444426f64794175726100000000000000000000000000000000000000000000ef03000000000000')
    sprite('hz432_13', 3)	# 122-124
    sprite('hz432_14', 3)	# 125-127
    sprite('hz432_15', 3)	# 128-130
    sprite('hz432_13', 3)	# 131-133
    sprite('hz432_14', 3)	# 134-136
    tag_voice(1, 'bhz254_0', 'bhz254_1', '', '')
    GFX_0('EffDDSnakeFangOD', -1)
    sprite('hz432_15', 3)	# 137-139
    sprite('hz432_16', 3)	# 140-142
    sprite('hz432_17', 3)	# 143-145
    sprite('hz432_18', 4)	# 146-149
    Unknown21015('485a45465f44444261636b417572610000000000000000000000000000000000eb03000000000000')
    sprite('hz432_19', 2)	# 150-151
    Unknown2016(360)
    physicsXImpulse(2000)
    physicsYImpulse(10000)
    setGravity(1500)
    sprite('hz432_20', 2)	# 152-153	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(650)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(5000)
    AirPushbackY(17000)
    Unknown9095()
    Unknown9016(0)
    Unknown9015(1)
    Hitstop(13)
    Unknown9310(1)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11072(0, 0, 0)
    Unknown21015('687a65663433325f62696e640000000000000000000000000000000000000000eb03000000000000')
    sprite('hz432_21', 3)	# 154-156
    sprite('hz432_22', 3)	# 157-159
    sprite('hz432_47', 3)	# 160-162
    SFX_3('hzse_11')
    sprite('hz432_48', 32767)	# 163-32929
    SFX_3('hzse_12')
    label(100)
    sprite('hz432_49', 3)	# 32930-32932	 **attackbox here**
    RefreshMultihit()
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Hitstop(20)
    Unknown9310(60)
    Unknown11064(0)
    Unknown1084(1)
    ScreenShake(50000, 50000)
    SFX_0('005_swing_grap_2_0')
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    SFX_0('213_bound_1')
    SFX_3('hzse_12')
    Unknown23159('UltimateShot_ODFinish')
    Unknown13024(1)
    Unknown11069('')
    sprite('hz432_50', 5)	# 32933-32937
    sprite('hz432_51', 5)	# 32938-32942
    sprite('hz432_52', 5)	# 32943-32947
    sprite('hz432_53', 5)	# 32948-32952
    sprite('hz432_53ex', 5)	# 32953-32957
    clearUponHandler(3)
    sprite('hz432_57', 5)	# 32958-32962
    sprite('hz432_58', 5)	# 32963-32967
    sprite('hz432_59', 5)	# 32968-32972
    sprite('hz601_17', 5)	# 32973-32977
    SFX_0('019_cloth_a')
    sprite('hz601_18', 5)	# 32978-32982
    sprite('hz601_19', 5)	# 32983-32987
    sprite('hz301_00', 5)	# 32988-32992
    sprite('hz301_01', 5)	# 32993-32997
    sprite('hz301_02', 5)	# 32998-33002
    sprite('hz301_03', 5)	# 33003-33007
    sprite('hz301_02', 5)	# 33008-33012
    sprite('hz301_03', 5)	# 33013-33017
    sprite('hz301_02', 5)	# 33018-33022
    sprite('hz301_03', 5)	# 33023-33027
    sprite('hz301_04', 5)	# 33028-33032
    sprite('hz301_05', 5)	# 33033-33037
    sprite('hz301_06', 5)	# 33038-33042
    sprite('hz301_07', 5)	# 33043-33047

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(1300)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('hz201_00', 3)	# 1-3
    sprite('hz201_01', 2)	# 4-5
    sprite('hz201_02', 2)	# 6-7
    sprite('hz201_03', 3)	# 8-10	 **attackbox here**
    SFX_0('003_swing_grap_0_2')
    Unknown7009(1)
    sprite('hz201_04', 3)	# 11-13
    Recovery()
    Unknown2063()
    sprite('hz201_05', 3)	# 14-16
    sprite('hz201_06', 3)	# 17-19
    sprite('hz201_07', 3)	# 20-22
    SFX_FOOTSTEP_(100, 1, 1)

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(950)
        Unknown11092(1)
        AirPushbackX(4000)
        AirPushbackY(16000)
        PushbackX(12000)
        Hitstop(5)
        AirUntechableTime(21)
        Unknown9016(1)
        Unknown1112('')
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('hz202_00', 2)	# 1-2
    sprite('hz202_01', 2)	# 3-4
    sprite('hz202_02', 1)	# 5-5
    GFX_0('EffKnifeSignal', 0)
    GFX_0('EffKnifeSignal', 1)
    sprite('hz202_03', 2)	# 6-7
    sprite('hz202_04', 2)	# 8-9
    sprite('hz202_05', 1)	# 10-10	 **attackbox here**
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    Unknown7009(2)
    GFX_0('Eff5CZanzo', -1)
    sprite('hz202_05', 1)	# 11-11	 **attackbox here**
    StartMultihit()
    sprite('hz202_06', 6)	# 12-17	 **attackbox here**
    RefreshMultihit()

    def upon_ON_HIT_OR_BLOCK():
        HitOrBlockCancel('NmlAtk5AA')
    sprite('hz202_07', 3)	# 18-20
    HitOrBlockCancel('NmlAtk5AA')
    Recovery()
    Unknown2063()
    sprite('hz202_08', 3)	# 21-23
    sprite('hz202_09', 3)	# 24-26
    sprite('hz202_10', 3)	# 27-29
    sprite('hz202_11', 3)	# 30-32
    sprite('hz202_12', 3)	# 33-35
    sprite('hz202_13', 3)	# 36-38

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Unknown9016(1)
        AirPushbackX(20000)
        AirPushbackY(16000)
        PushbackX(19800)
        Unknown2004(1, 0)
        HitJumpCancel(1)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('hz312_00ex01', 4)	# 1-4
    sprite('hz312_01ex01', 4)	# 5-8
    sprite('hz440_00', 4)	# 9-12
    GFX_0('EffKnifeSignal', 0)
    SFX_0('007_swing_knife_2')
    sprite('hz440_01', 3)	# 13-15	 **attackbox here**
    GFX_0('Eff440Zanzo', -1)
    sprite('hz440_02', 3)	# 16-18
    Recovery()
    Unknown2063()
    sprite('hz440_03', 3)	# 19-21
    sprite('hz440_04', 3)	# 22-24
    sprite('hz312_07ex01', 3)	# 25-27
    sprite('hz440_05', 3)	# 28-30
    sprite('hz440_06', 3)	# 31-33
    sprite('hz000_00', 3)	# 34-36

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirHitstunAnimation(18)
        AirPushbackX(24000)
        AirPushbackY(8000)
        AirUntechableTime(35)
        Unknown9202(25)
        Hitstop(9)
        Unknown11001(3, 3, 5)
        Unknown11034(1)
        Unknown11033(1)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
    sprite('hz407_00', 3)	# 1-3
    tag_voice(1, 'bhz208_0', 'bhz208_1', 'bhz208_2', '')
    GFX_0('EffLandAura', -1)
    sprite('hz407_01', 3)	# 4-6
    SFX_3('hzse_08')
    GFX_0('EffSpKensei', -1)
    sprite('hz407_02', 4)	# 7-10
    sprite('hz407_03', 4)	# 11-14
    SFX_0('004_swing_grap_1_0')
    sprite('hz407_04', 2)	# 15-16	 **attackbox here**
    sprite('hz407_05', 3)	# 17-19
    Recovery()
    Unknown2063()
    sprite('hz407_06', 3)	# 20-22
    sprite('hz407_07', 3)	# 23-25
    sprite('hz407_08', 2)	# 26-27
    sprite('hz407_09', 2)	# 28-29
    sprite('hz407_10', 2)	# 30-31
    sprite('hz407_11', 2)	# 32-33
    sprite('hz407_12', 2)	# 34-35
    sprite('hz407_13', 2)	# 36-37

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(5)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(60)
        AirPushbackY(32000)
        JumpCancel_(0)
        sendToLabelUpon(2, 1)
        Unknown2004(1, 0)
    sprite('hz430_01', 3)	# 1-3
    SFX_3('hzse_01')
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(50000)
    sprite('hz430_02', 3)	# 4-6
    Unknown1019(60)
    sprite('hz430_03', 3)	# 7-9
    Unknown1019(40)
    sprite('hz430_04', 2)	# 10-11
    Unknown1019(20)
    SFX_0('hit_m_slow')
    Unknown8004(100, 1, 1)
    sprite('hz430_05', 3)	# 12-14	 **attackbox here**
    setInvincible(0)
    SFX_0('damage_hit_mhh')
    SFX_4('bhz303')
    ScreenShake(10000, 10000)
    sprite('hz430_06', 2)	# 15-16
    physicsYImpulse(8000)
    Recovery()
    Unknown2063()
    sprite('hz430_06', 3)	# 17-19
    sprite('hz430_07', 5)	# 20-24
    Unknown1044()
    sprite('hz430_08', 5)	# 25-29
    label(0)
    sprite('hz430_09', 5)	# 30-34
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz430_10', 2)	# 35-36
    Unknown1019(0)
    sprite('hz430_11', 2)	# 37-38
    sprite('hz430_12', 2)	# 39-40
    sprite('hz430_13', 2)	# 41-42
    sprite('hz430_14', 2)	# 43-44
    sprite('hz430_15', 3)	# 45-47
    sprite('hz430_16', 3)	# 48-50
    sprite('hz430_17', 3)	# 51-53
    sprite('hz430_18', 3)	# 54-56

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        AirUntechableTime(25)
        HitLow(2)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('hz231_00', 3)	# 1-3
    sprite('hz231_01', 3)	# 4-6
    sprite('hz231_02', 3)	# 7-9
    sprite('hz231_03', 2)	# 10-11	 **attackbox here**
    Unknown7009(0)
    SFX_0('003_swing_grap_0_2')
    sprite('hz231_04', 2)	# 12-13
    Recovery()
    Unknown2063()
    sprite('hz231_05', 2)	# 14-15
    sprite('hz231_06', 3)	# 16-18
    sprite('hz231_07', 3)	# 19-21
    sprite('hz231_08', 3)	# 22-24
    sprite('hz231_09', 4)	# 25-28
    Unknown13002(1)
    Unknown13003(1)
    Unknown13005(1)
    Unknown13006(1)
    Unknown13008(1)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13017(1)
    Unknown13021(1)
    Unknown13019(1)
    Unknown13026(1)
    Unknown13029(1)
    Unknown13031(1)
    sprite('hz231_10', 3)	# 29-31
    sprite('hz231_11', 3)	# 32-34

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AttackP2(75)
        AirUntechableTime(25)
        AirPushbackX(8000)
        AirPushbackY(40000)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        Unknown11058('0000000001000000000000000000000000000000')
        Unknown9016(1)
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('AN_NmlAtk2B_2nd')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockJumpCancel(1)
    sprite('hz232_00', 5)	# 1-5
    GFX_0('EffKnifeSignal', 0)
    sprite('hz232_01', 2)	# 6-7
    sprite('hz232_02', 2)	# 8-9
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('hz232_03', 2)	# 10-11
    tag_voice(1, 'bhz106_0', 'bhz106_1', 'bhz106_2', '')
    sprite('hz232_04', 1)	# 12-12	 **attackbox here**
    StartMultihit()
    sprite('hz232_04', 3)	# 13-15	 **attackbox here**
    GFX_0('Eff2CZanzo', -1)
    SFX_0('009_swing_rapier_1')
    SFX_0('004_swing_grap_1_0')
    sprite('hz232_04', 1)	# 16-16	 **attackbox here**
    setInvincible(0)
    StartMultihit()
    Recovery()
    Unknown2063()
    sprite('hz232_05', 4)	# 17-20
    sprite('hz232_06', 4)	# 21-24
    sprite('hz232_07', 4)	# 25-28
    sprite('hz232_08', 4)	# 29-32
    sprite('hz232_09', 4)	# 33-36
    sprite('hz232_10', 4)	# 37-40
    sprite('hz232_11', 4)	# 41-44
    Unknown13002(1)
    Unknown13003(1)
    Unknown13005(1)
    Unknown13006(1)
    Unknown13008(1)
    Unknown13014(1)
    Unknown13015(1)
    Unknown13017(1)
    Unknown13021(1)
    Unknown13019(1)
    Unknown13026(1)
    Unknown13029(1)
    Unknown13031(1)
    sprite('hz232_12', 4)	# 45-48
    sprite('hz232_13', 4)	# 49-52

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(5)
        AttackP1(90)
        HitLow(2)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        Unknown9016(1)
        AirPushbackY(18000)
        AirUntechableTime(40)
    sprite('hz240_00', 3)	# 1-3
    GFX_0('EffKnifeSignal', 0)
    sprite('hz240_01', 3)	# 4-6
    sprite('hz240_02', 3)	# 7-9
    sprite('hz240_03', 3)	# 10-12
    sprite('hz240_04', 1)	# 13-13	 **attackbox here**
    StartMultihit()
    tag_voice(1, 'bhz107_0', 'bhz107_1', 'bhz107_2', '')
    SFX_0('009_swing_rapier_1')
    SFX_0('004_swing_grap_1_0')
    sprite('hz240_04', 4)	# 14-17	 **attackbox here**
    GFX_0('Eff3CZanzo', -1)
    sprite('hz240_05', 2)	# 18-19
    Recovery()
    Unknown2063()
    sprite('hz240_06', 2)	# 20-21
    sprite('hz240_07', 2)	# 22-23
    sprite('hz240_08', 3)	# 24-26
    sprite('hz240_09', 3)	# 27-29
    sprite('hz240_10', 3)	# 30-32
    sprite('hz240_11', 3)	# 33-35
    sprite('hz240_12', 3)	# 36-38

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AttackP2(85)
        Unknown9016(1)
        Hitstop(5)
        Unknown1037()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A_2')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('hz252_00', 1)	# 1-1
    sprite('hz252_01', 1)	# 2-2
    sprite('hz252_02', 2)	# 3-4
    sprite('hz252_03', 2)	# 5-6
    Unknown14070('NmlAtkAIR5A_2')
    GFX_0('EffKnifeSignal', 0)
    GFX_0('EffKnifeSignal', 1)
    sprite('hz252_04', 2)	# 7-8
    Unknown7009(5)
    sprite('hz252_05', 1)	# 9-9	 **attackbox here**
    StartMultihit()
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz252_05', 2)	# 10-11	 **attackbox here**
    GFX_0('Eff8CZanzo', 0)
    sprite('hz252_06', 2)	# 12-13
    Unknown14072('NmlAtkAIR5A_2')
    Recovery()
    Unknown2063()
    sprite('hz252_36', 2)	# 14-15
    Unknown14074('NmlAtkAIR5A_2')
    sprite('hz252_29', 3)	# 16-18
    sprite('hz252_30', 2)	# 19-20
    sprite('hz252_31', 2)	# 21-22
    sprite('hz252_32', 3)	# 23-25
    sprite('hz252_33', 3)	# 26-28
    sprite('hz252_34', 3)	# 29-31
    sprite('hz252_35', 3)	# 32-34

@State
def NmlAtkAIR5A_2():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(1000)
        AttackP2(85)
        AirHitstunAnimation(10)
        Hitstop(5)
        Unknown11001(0, 5, 5)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A_3')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            YAccel(50)
            Unknown1039(50)
    sprite('hz252_07', 2)	# 1-2
    sprite('hz252_08', 1)	# 3-3
    Unknown7009(5)
    sprite('hz252_09', 1)	# 4-4	 **attackbox here**
    Unknown14070('NmlAtkAIR5A_3')
    StartMultihit()
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz252_09', 2)	# 5-6	 **attackbox here**
    GFX_0('Eff8CZanzo_2', 0)
    sprite('hz252_10', 2)	# 7-8
    Recovery()
    Unknown2063()
    sprite('hz252_37', 2)	# 9-10
    Unknown14072('NmlAtkAIR5A_3')
    sprite('hz252_29', 3)	# 11-13
    Unknown14074('NmlAtkAIR5A_3')
    sprite('hz252_30', 2)	# 14-15
    Unknown1038()
    sprite('hz252_31', 2)	# 16-17
    sprite('hz252_32', 3)	# 18-20
    sprite('hz252_33', 3)	# 21-23
    sprite('hz252_34', 3)	# 24-26
    sprite('hz252_35', 3)	# 27-29

@State
def NmlAtkAIR5A_3():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(1000)
        AttackP2(85)
        AirPushbackX(12000)
        AirPushbackY(16000)
        Hitstop(5)
        Unknown11001(0, 5, 5)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A_4')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1019(80)
            YAccel(50)
            Unknown1039(50)
    sprite('hz252_11', 1)	# 1-1
    sprite('hz252_12', 1)	# 2-2
    sprite('hz252_13', 1)	# 3-3
    Unknown7009(5)
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz252_14', 2)	# 4-5	 **attackbox here**
    Unknown14070('NmlAtkAIR5A_4')
    GFX_0('Eff8CZanzo_3', 0)
    sprite('hz252_15', 2)	# 6-7
    Unknown14072('NmlAtkAIR5A_4')
    Recovery()
    Unknown2063()
    sprite('hz252_38', 2)	# 8-9
    Unknown14074('NmlAtkAIR5A_4')
    sprite('hz252_29', 3)	# 10-12
    Unknown1038()
    sprite('hz252_30', 2)	# 13-14
    sprite('hz252_31', 2)	# 15-16
    sprite('hz252_32', 3)	# 17-19
    sprite('hz252_33', 3)	# 20-22
    sprite('hz252_34', 3)	# 23-25
    sprite('hz252_35', 3)	# 26-28

@State
def NmlAtkAIR5A_4():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        Damage(1000)
        AttackP2(85)
        AirPushbackX(12000)
        AirPushbackY(16000)
        Hitstop(5)
        Unknown11001(0, 5, 5)
        Unknown9016(1)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A_5')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')

        def upon_ON_HIT_OR_BLOCK():
            clearUponHandler(10)
            Unknown1019(80)
            YAccel(50)
            Unknown1039(50)
    sprite('hz252_16', 1)	# 1-1
    sprite('hz252_17', 1)	# 2-2
    sprite('hz252_18', 1)	# 3-3
    sprite('hz252_19', 1)	# 4-4
    Unknown7009(5)
    Unknown14070('NmlAtkAIR5A_5')
    sprite('hz252_20', 1)	# 5-5
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz252_21', 3)	# 6-8	 **attackbox here**
    GFX_0('Eff8CZanzo_4', 0)
    sprite('hz252_39', 2)	# 9-10
    Unknown14072('NmlAtkAIR5A_5')
    Recovery()
    Unknown2063()
    sprite('hz252_29', 3)	# 11-13
    Unknown14074('NmlAtkAIR5A_5')
    sprite('hz252_30', 2)	# 14-15
    Unknown1038()
    sprite('hz252_31', 2)	# 16-17
    sprite('hz252_32', 3)	# 18-20
    sprite('hz252_33', 3)	# 21-23
    sprite('hz252_34', 3)	# 24-26
    sprite('hz252_35', 3)	# 27-29

@State
def NmlAtkAIR5A_5():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(2)
        AttackP2(85)
        AirUntechableTime(20)
        AirHitstunAnimation(10)
        AirPushbackX(12000)
        AirPushbackY(16000)
        Unknown9016(1)
        Unknown1038()
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('hz252_22', 1)	# 1-1
    sprite('hz252_23', 1)	# 2-2
    sprite('hz252_24', 1)	# 3-3
    sprite('hz252_25', 1)	# 4-4	 **attackbox here**
    StartMultihit()
    Unknown7009(5)
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz252_25', 2)	# 5-6	 **attackbox here**
    GFX_0('Eff8CZanzo_5', 0)
    sprite('hz252_26', 2)	# 7-8
    Recovery()
    Unknown2063()
    sprite('hz252_27', 3)	# 9-11
    sprite('hz252_28', 2)	# 12-13
    sprite('hz252_29', 3)	# 14-16
    sprite('hz252_30', 2)	# 17-18
    sprite('hz252_31', 2)	# 19-20
    sprite('hz252_32', 3)	# 21-23
    sprite('hz252_33', 3)	# 24-26
    sprite('hz252_34', 3)	# 27-29
    sprite('hz252_35', 3)	# 30-32

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(4)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackX(8000)
        AirPushbackY(-64000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(50)
        Unknown9190(1)
        Unknown9118(20)
        Unknown9016(1)
        HitOverhead(0)
        JumpCancel_(0)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)

        def upon_11():
            Unknown2037(1)
    sprite('hz412_00', 3)	# 1-3
    Unknown1084(1)
    physicsYImpulse(12000)
    setGravity(2400)
    physicsXImpulse(4000)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('00000000ab00000039000000ab000000')
    Unknown3075('00000000000000000000000000000000')
    sprite('hz412_01', 3)	# 4-6
    sprite('hz412_02', 3)	# 7-9
    tag_voice(1, 'bhz215_0', 'bhz215_1', 'bhz215_2', '')
    sprite('hz412_03', 2)	# 10-11	 **attackbox here**
    Unknown1019(50)
    YAccel(120)
    Unknown1039(150)
    Unknown4049(1440)
    Unknown4052()
    Unknown4045('687a65665f343132666c6173680000000000000000000000000000000000000000000000')
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz412_04', 3)	# 12-14	 **attackbox here**
    GFX_0('Eff412Zanzo', -1)
    label(0)
    sprite('hz412_05', 3)	# 15-17	 **attackbox here**
    sprite('hz412_04', 3)	# 18-20	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('hz412_06', 4)	# 21-24
    Recovery()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('hz412_07', 4)	# 25-28
    Unknown3029(0)
    if (not SLOT_2):
        Unknown13021(1)
        Unknown13016(1)
        Unknown13017(1)
        Unknown13014(1)
        Unknown13015(1)
        Unknown13003(1)
        Unknown13002(1)
    sprite('hz412_08', 4)	# 29-32
    sprite('hz412_09', 4)	# 33-36

@Subroutine
def UroborosInit():
    AttackLevel_(3)
    AttackP1(80)
    Unknown11028(9)
    Hitstop(8)
    Unknown11001(0, 20, 20)
    AirUntechableTime(28)
    Unknown9154(14)
    PushbackX(8000)
    AirPushbackX(6000)
    Unknown11034(0)
    Unknown11033(1)
    Unknown9016(1)
    HitOverhead(0)
    HitLow(0)
    HitAirUnblockable(0)
    Unknown12051(2)
    Unknown12052(1)
    Unknown23027()
    Unknown11058('0000000000000000000000000100000000000000')

    def upon_ON_HIT_OR_BLOCK():
        clearUponHandler(10)
        Unknown23029(4, 203, 0)
        Unknown23027()
        Unknown2037(1)

    def upon_43():
        if (SLOT_48 == 206):
            clearUponHandler(10)
            Unknown23029(4, 203, 0)
            Unknown23027()
            Unknown2037(1)
    Unknown2037(0)

    def upon_3():
        if SLOT_2:
            Unknown2037(0)
            clearUponHandler(3)
            sendToLabel(0)
        if (SLOT_23 >= 3000000):
            SLOT_23 = 3000000
    Unknown1051(60)
    WhiffCancel('DriveJump6')

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        Unknown1112('')
        callSubroutine('UroborosInit')
    sprite('hz203_00', 4)	# 1-4
    sprite('hz203_01', 4)	# 5-8
    sprite('hz203_02', 4)	# 9-12
    tag_voice(1, 'bhz108_0', 'bhz108_1', 'bhz108_2', '')
    sprite('hz203_03', 4)	# 13-16
    sprite('hz203_04', 3)	# 17-19
    Unknown1084(1)
    SLOT_54 = 1
    Unknown13(4)
    GFX_0('Kusari', 109)
    Unknown38(4, 1)
    Unknown23029(4, 0, 0)
    Unknown4020(4)
    GFX_0('ExBodyAura', -1)
    SFX_0('004_swing_grap_1_0')
    sprite('hz203_05', 3)	# 20-22
    RefreshMultihit()
    WhiffCancelEnable(1)
    sprite('hz203_06', 2)	# 23-24
    sprite('hz203_07', 2)	# 25-26
    sprite('hz203_08', 2)	# 27-28
    sprite('hz203_06', 2)	# 29-30
    sprite('hz203_07', 2)	# 31-32
    sprite('hz203_08', 2)	# 33-34
    label(0)
    sprite('hz203_06', 3)	# 35-37
    Unknown23029(4, 205, 0)
    Unknown1084(1)
    sprite('hz203_07', 3)	# 38-40
    sprite('hz203_08', 3)	# 41-43
    Unknown23027()
    Recovery()
    sprite('hz203_06', 3)	# 44-46
    loopRest()
    label(1)
    sprite('keep', 1)	# 47-47
    WhiffCancelEnable(0)
    Unknown23027()
    Recovery()
    sprite('hz203_09', 3)	# 48-50
    Unknown23029(4, 201, 0)
    Unknown21015('4578426f647941757261000000000000000000000000000000000000000000002d01000000000000')
    Unknown21015('4578506f7274616c000000000000000000000000000000000000000000000000cf00000000000000')
    sprite('hz203_10', 5)	# 51-55
    sprite('hz203_11', 3)	# 56-58
    sprite('hz203_12', 3)	# 59-61
    sprite('hz203_13', 3)	# 62-64

@State
def AN_NmlAtk2B_2nd():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        callSubroutine('UroborosInit')
    sprite('hz213_00', 3)	# 1-3
    sprite('hz213_01', 3)	# 4-6
    sprite('hz213_02', 3)	# 7-9
    tag_voice(1, 'bhz108_0', 'bhz108_1', 'bhz108_2', '')
    sprite('hz213_03', 3)	# 10-12
    sprite('hz213_04', 3)	# 13-15
    Unknown1084(1)
    SLOT_54 = 1
    Unknown13(4)
    GFX_0('Kusari', 109)
    Unknown38(4, 1)
    Unknown23029(4, 2, 0)
    Unknown4020(4)
    GFX_0('ExBodyAura', -1)
    sprite('hz213_05', 3)	# 16-18
    SFX_0('004_swing_grap_1_0')
    RefreshMultihit()
    WhiffCancelEnable(1)
    sprite('hz213_06', 2)	# 19-20
    sprite('hz213_07', 2)	# 21-22
    sprite('hz213_08', 2)	# 23-24
    sprite('hz213_06', 2)	# 25-26
    sprite('hz213_07', 2)	# 27-28
    sprite('hz213_08', 2)	# 29-30
    label(0)
    sprite('hz213_06', 3)	# 31-33
    Unknown23029(4, 205, 0)
    Unknown1084(1)
    sprite('hz213_07', 3)	# 34-36
    sprite('hz213_08', 3)	# 37-39
    Unknown23027()
    Recovery()
    sprite('hz213_06', 3)	# 40-42
    loopRest()
    label(1)
    sprite('keep', 1)	# 43-43
    WhiffCancelEnable(0)
    Unknown23027()
    Recovery()
    sprite('hz213_09', 3)	# 44-46
    Unknown23029(4, 201, 0)
    Unknown21015('4578426f647941757261000000000000000000000000000000000000000000002d01000000000000')
    Unknown21015('4578506f7274616c000000000000000000000000000000000000000000000000cf00000000000000')
    sprite('hz213_10', 3)	# 47-49
    sprite('hz213_11', 3)	# 50-52
    sprite('hz213_12', 3)	# 53-55
    sprite('hz213_13', 3)	# 56-58

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('UroborosInit')
    sprite('hz254_00', 4)	# 1-4
    sprite('hz254_01', 4)	# 5-8
    tag_voice(1, 'bhz108_0', 'bhz108_1', 'bhz108_2', '')
    sprite('hz254_02', 4)	# 9-12
    sprite('hz254_03', 3)	# 13-15
    SLOT_54 = 1
    Unknown13(4)
    GFX_0('Kusari', 2)
    Unknown38(4, 1)
    Unknown23029(4, 6, 0)
    Unknown4020(4)
    GFX_0('ExBodyAura', -1)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    setGravity(100)
    sprite('hz254_04', 3)	# 16-18
    SFX_0('004_swing_grap_1_0')
    Unknown1039(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)	# 19-20
    Unknown1039(90)
    sprite('hz254_06', 2)	# 21-22
    Unknown1039(90)
    sprite('hz254_07', 2)	# 23-24
    Unknown1084(1)
    sprite('hz254_08', 2)	# 25-26
    sprite('hz254_06', 2)	# 27-28
    sprite('hz254_07', 2)	# 29-30
    sprite('hz254_08', 2)	# 31-32
    loopRest()
    label(0)
    sprite('hz254_06', 3)	# 33-35
    Unknown23029(4, 205, 0)
    Unknown1084(1)
    sprite('hz254_07', 3)	# 36-38
    sprite('hz254_08', 3)	# 39-41
    Unknown23027()
    Recovery()
    sprite('hz254_06', 3)	# 42-44
    loopRest()
    label(1)
    sprite('keep', 1)	# 45-45
    Unknown1018()
    Unknown1023()
    Unknown1043()
    WhiffCancelEnable(0)
    Unknown23027()
    Recovery()
    sprite('hz254_09', 6)	# 46-51
    Unknown1043()
    Unknown23029(4, 201, 0)
    Unknown21015('4578426f647941757261000000000000000000000000000000000000000000002d01000000000000')
    Unknown21015('4578506f7274616c000000000000000000000000000000000000000000000000cf00000000000000')
    sprite('hz254_10', 6)	# 52-57
    sprite('hz254_11', 6)	# 58-63
    sprite('hz254_12', 5)	# 64-68
    sprite('hz254_13', 5)	# 69-73

@State
def NmlAtkAIR2B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        callSubroutine('UroborosInit')
    sprite('hz254_00', 4)	# 1-4
    sprite('hz254_01', 4)	# 5-8
    tag_voice(1, 'bhz108_0', 'bhz108_1', 'bhz108_2', '')
    sprite('hz254_02', 4)	# 9-12
    sprite('hz254_03', 3)	# 13-15
    SLOT_54 = 1
    Unknown13(4)
    GFX_0('Kusari', 3)
    Unknown38(4, 1)
    Unknown23029(4, 7, 0)
    Unknown4020(4)
    GFX_0('ExBodyAura', -1)
    Unknown1017()
    Unknown1022()
    Unknown1084(1)
    setGravity(100)
    sprite('hz254_04', 3)	# 16-18
    SFX_0('004_swing_grap_1_0')
    Unknown1039(90)
    WhiffCancelEnable(1)
    RefreshMultihit()
    sprite('hz254_05', 2)	# 19-20
    Unknown1039(90)
    sprite('hz254_06', 2)	# 21-22
    Unknown1039(90)
    sprite('hz254_07', 2)	# 23-24
    Unknown1084(1)
    sprite('hz254_08', 2)	# 25-26
    sprite('hz254_06', 2)	# 27-28
    sprite('hz254_07', 2)	# 29-30
    sprite('hz254_08', 2)	# 31-32
    loopRest()
    label(0)
    sprite('hz254_06', 3)	# 33-35
    Unknown23029(4, 205, 0)
    Unknown1084(1)
    sprite('hz254_07', 3)	# 36-38
    sprite('hz254_08', 3)	# 39-41
    Unknown23027()
    Recovery()
    sprite('hz254_06', 3)	# 42-44
    loopRest()
    label(1)
    sprite('keep', 1)	# 45-45
    Unknown1018()
    Unknown1023()
    Unknown1043()
    WhiffCancelEnable(0)
    Unknown23027()
    Recovery()
    sprite('hz254_09', 6)	# 46-51
    Unknown1043()
    Unknown23029(4, 201, 0)
    Unknown21015('4578426f647941757261000000000000000000000000000000000000000000002d01000000000000')
    Unknown21015('4578506f7274616c000000000000000000000000000000000000000000000000cf00000000000000')
    sprite('hz254_10', 6)	# 52-57
    sprite('hz254_11', 6)	# 58-63
    sprite('hz254_12', 5)	# 64-68
    sprite('hz254_13', 5)	# 69-73

@State
def DriveJump6():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()

        def upon_STATE_END():
            if (not SLOT_30):
                Unknown1019(40)
                YAccel(30)
                setGravity(2000)

        def upon_3():
            Unknown23030('4b75736172694a756d7049646c696e67000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
            if (SLOT_18 >= 6):
                Unknown14070('DriveJumpAttack')
            if (SLOT_18 >= 12):
                Unknown14072('DriveJumpAttack')
            if Unknown23145('NmlAtkAIR5B'):
                if (SLOT_13 >= 12000):
                    physicsYImpulse(2000)
        SLOT_52 = 12
        SLOT_53 = 16
        Unknown23029(4, 202, 0)
        Unknown23029(4, 204, 0)
        SLOT_54 = 1
        Unknown21015('4578506f7274616c000000000000000000000000000000000000000000000000cf00000000000000')
    Unknown1084(1)
    Unknown23145('NmlAtk5B')
    if SLOT_0:
        _gotolabel(1)
    Unknown23145('NmlAtk2B')
    if SLOT_0:
        _gotolabel(2)
    gotoLabel(3)
    label(0)
    Unknown23130(25650, 8, 2)
    sprite('hz408_30', 2)	# 1-2
    tag_voice(1, 'bhz209_1', 'bhz210_1', 'bhz211_1', '')
    sprite('hz408_31', 2)	# 3-4
    sprite('hz408_02', 2)	# 5-6
    loopRest()
    gotoLabel(10)
    label(1)
    Unknown23130(25650, 8, 2)
    sprite('hz408_32', 2)	# 7-8
    tag_voice(1, 'bhz209_1', 'bhz210_1', 'bhz211_1', '')
    sprite('hz408_33', 2)	# 9-10
    SFX_0('011_spin_0')
    sprite('hz408_02', 2)	# 11-12
    loopRest()
    gotoLabel(10)
    label(2)
    Unknown23130(25650, 8, 2)
    sprite('hz408_34', 2)	# 13-14
    tag_voice(1, 'bhz209_1', 'bhz210_1', 'bhz211_1', '')
    sprite('hz408_35', 2)	# 15-16
    sprite('hz408_02', 2)	# 17-18
    loopRest()
    gotoLabel(10)
    label(3)
    Unknown23130(25650, 8, 2)
    sprite('hz408_00', 2)	# 19-20
    tag_voice(1, 'bhz209_1', 'bhz210_1', 'bhz211_1', '')
    sprite('hz408_01', 2)	# 21-22
    sprite('hz408_02', 2)	# 23-24
    loopRest()
    gotoLabel(10)
    label(4)
    Unknown23130(25650, 8, 2)
    sprite('hz408_00', 2)	# 25-26
    tag_voice(1, 'bhz209_1', 'bhz210_1', 'bhz211_1', '')
    sprite('hz408_01', 2)	# 27-28
    sprite('hz408_02', 2)	# 29-30
    loopRest()
    gotoLabel(10)
    label(10)
    sprite('keep', 1)	# 31-31
    Unknown23030('4b75736172694a756d70537065656436000000000000000000000000000000000000000058020000000000006400000000000000000000000000000000000000')
    Unknown3029(1)
    Unknown2037(1)
    Unknown21015('4578426f647941757261000000000000000000000000000000000000000000002d01000000000000')
    Unknown3004(20)
    label(108)
    sprite('hz408_05', 3)	# 32-34
    sprite('hz408_06', 3)	# 35-37
    sprite('hz408_07', 3)	# 38-40
    loopRest()
    gotoLabel(108)
    label(109)
    sprite('hz408_10', 3)	# 41-43
    sprite('hz408_11', 3)	# 44-46
    sprite('hz408_12', 3)	# 47-49
    loopRest()
    gotoLabel(109)
    label(106)
    sprite('hz408_15', 3)	# 50-52
    sprite('hz408_16', 3)	# 53-55
    sprite('hz408_17', 3)	# 56-58
    loopRest()
    gotoLabel(106)
    label(103)
    sprite('hz408_20', 3)	# 59-61
    sprite('hz408_21', 3)	# 62-64
    sprite('hz408_22', 3)	# 65-67
    loopRest()
    gotoLabel(103)
    label(102)
    sprite('hz408_25', 3)	# 68-70
    sprite('hz408_26', 3)	# 71-73
    sprite('hz408_27', 3)	# 74-76
    loopRest()
    gotoLabel(102)
    label(208)
    sprite('hz408_08', 3)	# 77-79
    sprite('hz408_09', 3)	# 80-82
    loopRest()
    ExitState()
    label(209)
    sprite('hz408_13', 3)	# 83-85
    sprite('hz408_14', 3)	# 86-88
    loopRest()
    ExitState()
    label(206)
    sprite('hz408_18', 3)	# 89-91
    sprite('hz408_19', 3)	# 92-94
    loopRest()
    ExitState()
    label(203)
    sprite('hz408_23', 3)	# 95-97
    sprite('hz408_24', 3)	# 98-100
    loopRest()
    ExitState()
    label(202)
    sprite('hz408_28', 3)	# 101-103
    sprite('hz408_29', 3)	# 104-106
    loopRest()
    ExitState()

@State
def DriveJumpAttack():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        AirUntechableTime(22)
        AirPushbackY(15000)
        HitOrBlockJumpCancel(1)
        HitOrBlockCancel('NmlAtkAIR5A')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR2B')
        HitOrBlockCancel('NmlAtkAIR5C')
    sprite('hz251_00', 2)	# 1-2
    sprite('hz251_01', 2)	# 3-4
    sprite('hz251_02', 3)	# 5-7
    Unknown7009(3)
    SFX_0('004_swing_grap_1_1')
    sprite('hz251_03', 4)	# 8-11	 **attackbox here**
    sprite('hz251_04', 3)	# 12-14	 **attackbox here**
    sprite('hz251_05', 4)	# 15-18
    Recovery()
    Unknown2063()
    sprite('hz251_06', 4)	# 19-22
    sprite('hz251_07', 3)	# 23-25
    sprite('hz251_08', 3)	# 26-28

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
        Unknown9016(1)
    sprite('hz410_00', 3)	# 1-3
    sprite('hz410_01', 3)	# 4-6
    Unknown4004('4775617264437275736857696e6400000000000000000000000000000000000001000000')
    tag_voice(1, 'bhz156_0', 'bhz156_1', '', '')
    GFX_0('EffKnifeSignal', 0)
    sprite('hz410_02', 3)	# 7-9
    sprite('hz410_03', 3)	# 10-12
    sprite('hz410_05', 3)	# 13-15
    sprite('hz410_06', 2)	# 16-17
    sprite('hz410_06', 4)	# 18-21
    GFX_0('Eff410', -1)
    SFX_3('hzse_08')
    sprite('hz410_07', 3)	# 22-24	 **attackbox here**
    SFX_0('007_swing_knife_0')
    SFX_0('004_swing_grap_1_0')
    sprite('hz410_08', 3)	# 25-27
    sprite('hz410_09', 3)	# 28-30
    sprite('hz410_10', 3)	# 31-33
    sprite('hz410_11', 3)	# 34-36
    sprite('hz410_12', 3)	# 37-39
    sprite('hz410_13', 3)	# 40-42
    sprite('hz410_14', 3)	# 43-45
    sprite('hz410_15', 3)	# 46-48

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)
        setGravity(3000)
    sprite('hz410_07', 2)	# 1-2	 **attackbox here**
    StartMultihit()
    sprite('hz410_08', 2)	# 3-4
    sprite('hz410_09', 2)	# 5-6
    sprite('hz410_10', 3)	# 7-9
    sprite('hz410_11', 3)	# 10-12
    sprite('hz410_12', 3)	# 13-15
    sprite('hz407_00', 3)	# 16-18
    tag_voice(1, 'bhz157_0', 'bhz157_1', '', '')
    GFX_0('EffLandAura', -1)
    sprite('hz407_01', 3)	# 19-21
    SFX_3('hzse_08')
    GFX_0('EffSpKensei', -1)
    sprite('hz407_02', 4)	# 22-25
    sprite('hz407_03', 4)	# 26-29
    SFX_0('004_swing_grap_1_0')
    sprite('hz407_04', 2)	# 30-31	 **attackbox here**
    sprite('hz407_05', 3)	# 32-34
    Recovery()
    sprite('hz407_06', 3)	# 35-37
    sprite('hz407_07', 3)	# 38-40
    sprite('hz407_08', 2)	# 41-42
    sprite('hz407_09', 2)	# 43-44
    sprite('hz407_10', 2)	# 45-46
    sprite('hz407_11', 2)	# 47-48
    sprite('hz407_12', 2)	# 49-50
    sprite('hz407_13', 2)	# 51-52
    sprite('hz000_00', 8)	# 53-60
    sprite('hz000_01', 8)	# 61-68
    sprite('hz000_02', 8)	# 69-76
    sprite('hz000_03', 8)	# 77-84
    sprite('hz000_04', 8)	# 85-92
    sprite('hz000_05', 8)	# 93-100
    sprite('hz000_06', 8)	# 101-108
    sprite('hz000_07', 8)	# 109-116
    sprite('hz000_08', 8)	# 117-124
    label(10)
    sprite('hz000_00', 8)	# 125-132
    sprite('hz000_01', 8)	# 133-140
    sprite('hz000_02', 8)	# 141-148
    sprite('hz000_03', 8)	# 149-156
    sprite('hz000_04', 8)	# 157-164
    sprite('hz000_05', 8)	# 165-172
    sprite('hz000_06', 8)	# 173-180
    sprite('hz000_07', 8)	# 181-188
    sprite('hz000_08', 8)	# 189-196
    loopRest()
    gotoLabel(10)
    label(11)
    sprite('keep', 1)	# 197-197

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('hz211_00', 1)	# 1-1
    sprite('hz211_01', 1)	# 2-2
    sprite('hz211_02', 2)	# 3-4
    sprite('hz211_03', 2)	# 5-6
    sprite('hz211_04', 2)	# 7-8
    sprite('hz211_05', 2)	# 9-10
    sprite('hz211_06', 2)	# 11-12
    physicsXImpulse(15000)
    sprite('hz211_07', 2)	# 13-14
    SFX_0('004_swing_grap_1_1')
    physicsXImpulse(10000)
    sprite('hz211_08', 4)	# 15-18	 **attackbox here**
    physicsXImpulse(0)
    sprite('hz211_09', 4)	# 19-22
    sprite('hz211_10', 4)	# 23-26
    physicsXImpulse(-5000)
    sprite('hz211_11', 4)	# 27-30
    sprite('hz211_12', 2)	# 31-32
    sprite('hz211_12', 3)	# 33-35
    physicsXImpulse(0)
    sprite('hz211_13', 5)	# 36-40
    label(0)
    sprite('hz000_00', 8)	# 41-48
    sprite('hz000_01', 8)	# 49-56
    sprite('hz000_02', 8)	# 57-64
    sprite('hz000_03', 8)	# 65-72
    sprite('hz000_04', 8)	# 73-80
    sprite('hz000_05', 8)	# 81-88
    sprite('hz000_06', 8)	# 89-96
    sprite('hz000_07', 8)	# 97-104
    sprite('hz000_08', 8)	# 105-112
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 113-113

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)

    def upon_STATE_END():
        Unknown2005()
    sprite('hz405_00', 2)	# 1-2
    sprite('hz405_02', 2)	# 3-4
    sprite('hz405_03', 3)	# 5-7
    sprite('hz405_17', 3)	# 8-10
    Unknown2005()
    sprite('hz405_16', 3)	# 11-13
    GFX_0('Eff440snake', -1)
    sprite('hz405_16ex01', 3)	# 14-16
    sprite('hz440_23', 3)	# 17-19
    tag_voice(0, 'bhz158_0', 'bhz158_1', '', '')
    sprite('hz440_24', 4)	# 20-23	 **attackbox here**
    Unknown11056(1)
    SFX_3('hzse_08')
    SFX_0('006_swing_blade_2')
    SFX_0('103_hit_counter_slash_0')
    sprite('hz440_25', 4)	# 24-27	 **attackbox here**
    sprite('hz440_26', 4)	# 28-31
    sprite('hz440_27', 4)	# 32-35
    sprite('hz440_28', 4)	# 36-39
    sprite('hz440_29', 4)	# 40-43
    sprite('hz440_30', 4)	# 44-47
    sprite('hz440_31', 4)	# 48-51
    sprite('hz440_32', 4)	# 52-55
    sprite('hz440_33', 5)	# 56-60

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
    sprite('hz402_00', 1)	# 25-25
    sprite('hz402_01', 2)	# 26-27
    teleportRelativeX(50000)
    sprite('hz402_02', 2)	# 28-29
    SFX_0('019_cloth_c')
    physicsXImpulse(15000)
    physicsYImpulse(18000)
    setGravity(2250)
    GFX_0('EffLandAura', -1)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(1)
    sendToLabelUpon(2, 1)
    sprite('hz402_03', 2)	# 30-31
    sprite('hz402_04', 2)	# 32-33
    SFX_0('004_swing_grap_1_1')
    sprite('hz402_05', 2)	# 34-35
    GFX_0('EffChudan', -1)
    sprite('hz402_06', 3)	# 36-38
    SFX_3('hzse_06')
    sprite('hz402_07', 3)	# 39-41
    sprite('hz402_08', 2)	# 42-43	 **attackbox here**
    sprite('hz402_09', 2)	# 44-45	 **attackbox here**
    sprite('hz402_10', 10)	# 46-55
    label(1)
    sprite('hz402_11', 3)	# 56-58
    Unknown1084(1)
    Unknown3029(0)
    sprite('hz402_12', 2)	# 59-60
    sprite('hz402_13', 2)	# 61-62
    sprite('hz402_14', 2)	# 63-64
    sprite('hz402_15', 2)	# 65-66
    sprite('hz000_00', 8)	# 67-74
    sprite('hz000_01', 8)	# 75-82
    sprite('hz000_02', 8)	# 83-90
    sprite('hz000_03', 8)	# 91-98
    sprite('hz000_04', 8)	# 99-106
    sprite('hz000_05', 8)	# 107-114
    sprite('hz000_06', 8)	# 115-122
    sprite('hz000_07', 8)	# 123-130
    sprite('hz000_08', 8)	# 131-138

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
    sprite('hz210_00', 1)	# 1-1
    sprite('hz210_01', 2)	# 2-3
    sprite('hz210_02', 2)	# 4-5
    sprite('hz210_03', 2)	# 6-7
    sprite('hz210_04', 2)	# 8-9
    sprite('hz210_05', 1)	# 10-10
    sprite('hz210_06', 1)	# 11-11
    SFX_0('004_swing_grap_1_1')
    sprite('hz210_07', 3)	# 12-14	 **attackbox here**
    sprite('hz210_08', 3)	# 15-17
    Recovery()
    Unknown2063()
    sprite('hz210_09', 3)	# 18-20
    sprite('hz210_10', 3)	# 21-23
    sprite('hz210_11', 3)	# 24-26
    sprite('hz210_12', 3)	# 27-29
    sprite('hz210_13', 3)	# 30-32
    sprite('hz210_14', 3)	# 33-35
    sprite('hz000_00', 8)	# 36-43
    sprite('hz000_01', 8)	# 44-51
    sprite('hz000_02', 8)	# 52-59
    sprite('hz000_03', 8)	# 60-67
    sprite('hz000_04', 8)	# 68-75
    sprite('hz000_05', 8)	# 76-83
    sprite('hz000_06', 8)	# 84-91
    sprite('hz000_07', 8)	# 92-99
    sprite('hz000_08', 8)	# 100-107

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('hz405_00', 2)	# 1-2
    sprite('hz405_02', 2)	# 3-4
    sprite('hz405_03', 3)	# 5-7
    sprite('hz405_17', 3)	# 8-10
    Unknown2005()
    sprite('hz405_16', 3)	# 11-13
    GFX_0('Eff440snake', -1)
    sprite('hz405_16ex01', 3)	# 14-16
    sprite('hz440_23', 3)	# 17-19
    sprite('hz440_24', 4)	# 20-23	 **attackbox here**
    Unknown11056(1)
    SFX_3('hzse_08')
    SFX_0('006_swing_blade_2')
    SFX_0('103_hit_counter_slash_0')
    sprite('hz440_25', 4)	# 24-27	 **attackbox here**
    sprite('hz440_26', 4)	# 28-31
    sprite('hz440_27', 4)	# 32-35
    sprite('hz440_28', 4)	# 36-39
    sprite('hz440_29', 4)	# 40-43
    sprite('hz440_30', 4)	# 44-47
    sprite('hz440_31', 4)	# 48-51
    sprite('hz440_32', 4)	# 52-55
    sprite('hz440_33', 5)	# 56-60

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('hz032_00', 3)	# 1-3
    sprite('hz032_01', 3)	# 4-6
    Unknown1019(200)
    sprite('hz032_02', 3)	# 7-9
    Unknown8007(100, 1, 1)
    Unknown1019(200)
    sprite('hz032_03', 3)	# 10-12
    sprite('hz032_02', 3)	# 13-15
    sprite('hz032_04', 3)	# 16-18
    Unknown1019(80)
    sprite('hz032_04ex01', 3)	# 19-21
    Unknown1019(60)
    Unknown8010(100, 1, 1)
    sprite('hz032_04ex02', 3)	# 22-24
    sprite('hz032_05', 3)	# 25-27
    Unknown1019(40)
    sprite('hz032_06', 3)	# 28-30
    Unknown1019(20)
    sprite('hz032_07', 3)	# 31-33
    label(1)
    sprite('hz310_00', 1)	# 34-34
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    SFX_0('010_swing_sword_0')
    sprite('hz310_01', 2)	# 35-36
    sprite('hz310_02', 3)	# 37-39	 **attackbox here**
    Unknown1084(1)
    sprite('hz310_03', 4)	# 40-43
    sprite('hz310_04', 4)	# 44-47
    SFX_4('bhz154')
    sprite('hz310_05', 7)	# 48-54
    sprite('hz310_06', 4)	# 55-58
    sprite('hz310_07', 4)	# 59-62

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(4)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(13)
        GroundedHitstunAnimation(13)
        AirPushbackX(2000)
        AirPushbackY(42000)
        AirUntechableTime(70)
        Unknown11001(0, -9, -4)
        Unknown2004(1, 0)
    sprite('hz310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('hz311_00', 5)	# 4-8
    SFX_4('bhz153')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('hz311_01', 8)	# 9-16
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('hz311_02', 6)	# 17-22
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('hz311_03', 4)	# 23-26
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('hz311_04', 3)	# 27-29
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('hz311_05', 2)	# 30-31
    SFX_0('006_swing_blade_1')
    Unknown5000(0, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('hz311_06', 3)	# 32-34	 **attackbox here**
    sprite('hz311_07', 3)	# 35-37
    sprite('hz311_08', 3)	# 38-40
    sprite('hz311_09', 3)	# 41-43
    sprite('hz311_11', 3)	# 44-46
    sprite('hz311_12', 3)	# 47-49
    sprite('hz311_13', 2)	# 50-51
    sprite('hz311_14', 2)	# 52-53

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        physicsXImpulse(8000)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('hz032_00', 3)	# 1-3
    sprite('hz032_01', 3)	# 4-6
    Unknown1019(200)
    sprite('hz032_02', 3)	# 7-9
    Unknown8007(100, 1, 1)
    Unknown1019(200)
    sprite('hz032_03', 3)	# 10-12
    sprite('hz032_02', 3)	# 13-15
    sprite('hz032_04', 3)	# 16-18
    Unknown1019(80)
    sprite('hz032_04ex01', 3)	# 19-21
    Unknown1019(60)
    Unknown8010(100, 1, 1)
    sprite('hz032_04ex02', 3)	# 22-24
    sprite('hz032_05', 3)	# 25-27
    Unknown1019(40)
    sprite('hz032_06', 3)	# 28-30
    Unknown1019(20)
    sprite('hz032_07', 3)	# 31-33
    label(1)
    sprite('hz310_00', 1)	# 34-34
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    SFX_0('010_swing_sword_0')
    sprite('hz310_01', 2)	# 35-36
    sprite('hz310_02', 3)	# 37-39	 **attackbox here**
    Unknown1084(1)
    sprite('hz310_03', 4)	# 40-43
    sprite('hz310_04', 4)	# 44-47
    SFX_4('bhz154')
    sprite('hz310_05', 7)	# 48-54
    sprite('hz310_06', 4)	# 55-58
    sprite('hz310_07', 4)	# 59-62

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(0)
        Damage(2000)
        AttackP2(50)
        AirHitstunAnimation(12)
        GroundedHitstunAnimation(12)
        AirPushbackX(65000)
        AirPushbackY(20000)
        Hitstop(15)
        AirUntechableTime(60)
        Unknown11099(1)
        Unknown13021(1)
        Unknown21005(1)
    sprite('hz310_02', 3)	# 1-3	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('hz313_00', 4)	# 4-7
    SFX_4('bhz153')
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('hz313_01', 4)	# 8-11
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('hz313_02', 4)	# 12-15
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000001000000')
    sprite('hz313_03', 4)	# 16-19
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('hz313_04', 4)	# 20-23
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('hz313_05', 4)	# 24-27
    Unknown5000(0, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    sprite('hz313_06', 6)	# 28-33
    sprite('hz313_07', 6)	# 34-39
    sprite('hz313_08', 1)	# 40-40
    SFX_0('004_swing_grap_1_1')
    sprite('hz313_09', 3)	# 41-43	 **attackbox here**
    SFX_0('100_hit_grap_3')
    sprite('hz313_10', 6)	# 44-49
    sprite('hz313_11', 6)	# 50-55
    sprite('hz313_12', 4)	# 56-59
    sprite('hz313_13', 4)	# 60-63
    sprite('hz313_14', 3)	# 64-66
    sprite('hz313_15', 3)	# 67-69

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        HitAirUnblockable(3)
        PushbackX(19800)
        Unknown9016(1)
        Unknown12051(2)
        AttackLevel_(4)
        Damage(2300)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirUntechableTime(48)
        AirPushbackY(36000)
        Unknown13024(0)
        Unknown13045(0)
        sendToLabelUpon(2, 1)
        setInvincible(1)
        Unknown3029(1)
        teleportRelativeX(10000)
    sprite('hz401_00', 3)	# 1-3
    SFX_3('hzse_07')
    SFX_0('006_swing_blade_2')
    tag_voice(1, 'bhz201_0', 'bhz201_1', 'bhz201_2', '')
    GFX_0('EffSamaso', -1)
    sprite('hz401_01', 3)	# 4-6
    Unknown26('EffKamae')
    Unknown26('EffKamaeLand')
    physicsYImpulse(28000)
    physicsXImpulse(-4000)
    setGravity(2400)
    SFX_0('004_swing_grap_1_1')
    if SLOT_52:
        Unknown23119(32768, 10, 2)
    sprite('hz401_02', 3)	# 7-9
    sprite('hz401_03ex01', 2)	# 10-11	 **attackbox here**
    sprite('hz401_03', 2)	# 12-13	 **attackbox here**
    sprite('hz401_04', 4)	# 14-17	 **attackbox here**
    setInvincible(0)
    sprite('hz401_05', 4)	# 18-21
    label(0)
    sprite('hz401_06', 3)	# 22-24
    sprite('hz401_07', 3)	# 25-27
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz401_08', 4)	# 28-31
    Unknown1084(1)
    Unknown3029(0)
    sprite('hz401_09', 4)	# 32-35
    sprite('hz401_10', 4)	# 36-39
    sprite('hz401_11', 4)	# 40-43
    sprite('hz401_12', 4)	# 44-47
    sprite('hz401_13', 4)	# 48-51
    sprite('hz401_14', 4)	# 52-55

@Subroutine
def Kamae_Zanzou():
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(6)
    Unknown3070(2)
    Unknown3072('f0000000000000008000000000000000')
    Unknown3073('3c000000000000008000000000000000')
    Unknown3074('00000000000000004000000000000000')
    Unknown3075('00000000000000000000000000000000')
    Unknown3076(1010)
    Unknown3077(1010)

@State
def MidAssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Unknown11001(9, 5, 10)
        AirUntechableTime(40)
        Hitstop(6)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(9)
        PushbackX(2000)
        AirPushbackY(-34000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(50)
        WhiffCancel('HaseiAssault')
        WhiffCancel('CmnActInvincibleAttack')
        SLOT_65 = 0
        sendToLabelUpon(2, 9)
    sprite('hz411_00', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(10000)
    sprite('hz411_01', 3)	# 4-6
    tag_voice(1, 'bhz214_0', 'bhz214_1', 'bhz214_2', '')
    Unknown1019(50)
    sprite('hz411_02', 3)	# 7-9
    Unknown1019(50)
    sprite('hz411_03', 3)	# 10-12
    GFX_0('Eff411', -1)
    SFX_0('006_swing_blade_1')
    SFX_3('hzse_06')
    Unknown1084(1)
    sprite('hz411_04', 2)	# 13-14
    sprite('hz411_05', 2)	# 15-16	 **attackbox here**
    sprite('hz411_06', 2)	# 17-18
    sprite('hz411_07', 2)	# 19-20
    sprite('hz411_08', 2)	# 21-22
    sprite('hz411_09', 2)	# 23-24
    sprite('hz411_10', 2)	# 25-26
    Unknown1084(1)
    GFX_0('EffKamae', 0)
    GFX_0('EffKamaeLand', -1)

    def upon_23():
        sendToLabel(0)
    WhiffCancelEnable(1)
    sprite('hz411_10', 2)	# 27-28
    SFX_3('hzse_05')
    sprite('hz400_02', 5)	# 29-33
    sprite('hz400_03', 5)	# 34-38
    sprite('hz400_04', 5)	# 39-43
    sprite('hz400_05', 5)	# 44-48
    sprite('hz400_06', 5)	# 49-53
    sprite('hz400_07', 5)	# 54-58
    sprite('hz400_08', 5)	# 59-63
    sprite('hz400_09', 5)	# 64-68
    callSubroutine('Kamae_Zanzou')
    Unknown2037(1)
    label(0)
    sprite('hz402_00', 1)	# 69-69
    WhiffCancelEnable(0)
    AttackP1(80)
    Hitstop(11)
    Unknown11001(0, 5, 10)
    GroundedHitstunAnimation(0)
    AirHitstunAnimation(11)
    AirPushbackY(-60000)
    PushbackX(15300)
    Unknown9190(0)
    Unknown11058('0100000000000000000000000000000000000000')
    HitOverhead(2)
    if SLOT_2:
        Damage(2200)
    clearUponHandler(3)
    clearUponHandler(23)
    GFX_0('EffLandAura', -1)
    sprite('hz402_01', 2)	# 70-71
    Unknown26('EffKamae')
    Unknown26('EffKamaeLand')
    teleportRelativeX(50000)
    sprite('hz402_02', 2)	# 72-73
    tag_voice(0, 'bhz202_0', 'bhz202_1', 'bhz202_2', '')
    SFX_0('019_cloth_c')
    physicsXImpulse(16000)
    physicsYImpulse(18000)
    setGravity(2250)
    sprite('hz402_03', 2)	# 74-75
    sprite('hz402_04', 2)	# 76-77
    SFX_0('004_swing_grap_1_1')
    sprite('hz402_05', 2)	# 78-79
    GFX_0('EffChudan', -1)
    sprite('hz402_06', 3)	# 80-82
    SFX_3('hzse_06')
    sprite('hz402_07', 3)	# 83-85
    sprite('hz402_08', 2)	# 86-87	 **attackbox here**
    RefreshMultihit()
    sprite('hz402_09', 2)	# 88-89	 **attackbox here**
    sprite('hz402_10', 32767)	# 90-32856
    Recovery()
    label(9)
    sprite('hz402_11', 2)	# 32857-32858
    setInvincible(0)
    Unknown1084(1)
    Unknown3029(0)
    sprite('hz402_12', 3)	# 32859-32861
    sprite('hz402_13', 3)	# 32862-32864
    sprite('hz402_14', 3)	# 32865-32867
    sprite('hz402_15', 2)	# 32868-32869

@State
def MidAssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(2200)
        AttackP1(80)
        Unknown11001(0, 5, 10)
        AirUntechableTime(40)
        YImpluseBeforeWallbounce(0)
        Hitstop(11)
        GroundedHitstunAnimation(0)
        AirHitstunAnimation(11)
        AirPushbackY(-60000)
        PushbackX(15300)
        Unknown9190(0)
        Unknown11058('0100000000000000000000000000000000000000')
        HitOverhead(2)
        WhiffCancel('CmnActInvincibleAttack')

        def upon_3():
            SLOT_65 = (SLOT_65 + 2)
            if (SLOT_65 > 22):
                callSubroutine('Kamae_Zanzou')

                def upon_24():
                    sendToLabel(0)
        SLOT_65 = 0
        sendToLabelUpon(2, 9)
    sprite('hz400_00', 3)	# 1-3
    sprite('hz400_01', 2)	# 4-5
    Unknown1084(1)
    sprite('hz400_01', 1)	# 6-6
    GFX_0('EffKamae', 0)
    GFX_0('EffKamaeLand', -1)
    tag_voice(1, 'bhz200_0', 'bhz200_1', 'bhz200_2', '')
    WhiffCancelEnable(1)
    sprite('hz400_02', 5)	# 7-11
    SFX_3('hzse_05')
    sprite('hz400_03', 5)	# 12-16
    sprite('hz400_04', 5)	# 17-21
    sprite('hz400_05', 5)	# 22-26
    sprite('hz400_06', 5)	# 27-31
    sprite('hz400_07', 5)	# 32-36
    sprite('hz400_08', 5)	# 37-41
    sprite('hz400_09', 5)	# 42-46
    label(0)
    sprite('hz402_00', 1)	# 47-47
    WhiffCancelEnable(0)
    clearUponHandler(3)
    clearUponHandler(24)
    GFX_0('EffLandAura', -1)
    sprite('hz402_01', 2)	# 48-49
    Unknown26('EffKamae')
    Unknown26('EffKamaeLand')
    teleportRelativeX(50000)
    sprite('hz402_02', 2)	# 50-51
    tag_voice(0, 'bhz202_0', 'bhz202_1', 'bhz202_2', '')
    SFX_0('019_cloth_c')
    physicsXImpulse(16000)
    physicsYImpulse(18000)
    setGravity(2250)
    sprite('hz402_03', 2)	# 52-53
    sprite('hz402_04', 2)	# 54-55
    SFX_0('004_swing_grap_1_1')
    sprite('hz402_05', 2)	# 56-57
    GFX_0('EffChudan', -1)
    sprite('hz402_06', 3)	# 58-60
    SFX_3('hzse_06')
    sprite('hz402_07', 3)	# 61-63
    sprite('hz402_08', 2)	# 64-65	 **attackbox here**
    RefreshMultihit()
    sprite('hz402_09', 2)	# 66-67	 **attackbox here**
    sprite('hz402_10', 32767)	# 68-32834
    Recovery()
    label(9)
    sprite('hz402_11', 2)	# 32835-32836
    setInvincible(0)
    Unknown1084(1)
    Unknown3029(0)
    sprite('hz402_12', 3)	# 32837-32839
    sprite('hz402_13', 3)	# 32840-32842
    sprite('hz402_14', 3)	# 32843-32845
    sprite('hz402_15', 2)	# 32846-32847

@State
def LowAssaultA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Unknown11001(9, 5, 10)
        AirUntechableTime(40)
        Hitstop(6)
        GroundedHitstunAnimation(2)
        AirHitstunAnimation(9)
        PushbackX(2000)
        AirPushbackY(-34000)
        YImpluseBeforeWallbounce(0)
        Unknown9190(1)
        Unknown9118(50)
        WhiffCancel('HaseiAssault')
        WhiffCancel('CmnActInvincibleAttack')
        SLOT_65 = 0
    sprite('hz411_00', 3)	# 1-3
    Unknown1084(1)
    physicsXImpulse(10000)
    sprite('hz411_01', 3)	# 4-6
    tag_voice(1, 'bhz214_0', 'bhz214_1', 'bhz214_2', '')
    Unknown1019(50)
    sprite('hz411_02', 3)	# 7-9
    Unknown1019(50)
    sprite('hz411_03', 3)	# 10-12
    GFX_0('Eff411', -1)
    SFX_0('006_swing_blade_1')
    SFX_3('hzse_06')
    Unknown1084(1)
    sprite('hz411_04', 2)	# 13-14
    sprite('hz411_05', 2)	# 15-16	 **attackbox here**
    sprite('hz411_06', 2)	# 17-18
    sprite('hz411_07', 2)	# 19-20
    sprite('hz411_08', 2)	# 21-22
    sprite('hz411_09', 2)	# 23-24
    sprite('hz411_10', 2)	# 25-26
    GFX_0('EffKamae', 0)
    GFX_0('EffKamaeLand', -1)

    def upon_23():
        sendToLabel(0)
    WhiffCancelEnable(1)
    sprite('hz411_10', 2)	# 27-28
    SFX_3('hzse_05')
    sprite('hz400_02', 5)	# 29-33
    sprite('hz400_03', 5)	# 34-38
    sprite('hz400_04', 5)	# 39-43
    sprite('hz400_05', 5)	# 44-48
    sprite('hz400_06', 5)	# 49-53
    sprite('hz400_07', 5)	# 54-58
    sprite('hz400_08', 5)	# 59-63
    sprite('hz400_09', 5)	# 64-68
    callSubroutine('Kamae_Zanzou')
    Unknown2037(1)
    label(0)
    sprite('hz403_00', 1)	# 69-69
    WhiffCancelEnable(0)
    AttackP1(90)
    Hitstop(16)
    Unknown11001(0, 5, 10)
    AirHitstunAnimation(11)
    GroundedHitstunAnimation(11)
    Unknown9095()
    Unknown9190(0)
    Unknown11058('0000000000000000010000000000000000000000')
    Unknown9016(1)
    HitLow(2)
    Unknown2004(1, 0)
    if SLOT_2:
        Damage(2200)
        AirPushbackX(3000)
        AirPushbackY(22000)
        Unknown11001(0, 5, 10)
        Hitstop(8)
    else:
        AirPushbackX(3000)
        AirPushbackY(16000)
    clearUponHandler(3)
    clearUponHandler(23)
    GFX_0('EffLandAura', -1)
    sprite('hz403_00', 2)	# 70-71
    Unknown26('EffKamae')
    Unknown26('EffKamaeLand')
    sprite('hz403_01', 2)	# 72-73
    SFX_0('007_swing_knife_1')
    Unknown1019(200)
    sprite('hz403_02', 2)	# 74-75
    Unknown1019(200)
    sprite('hz403_03', 2)	# 76-77
    tag_voice(0, 'bhz203_0', 'bhz203_1', 'bhz203_2', '')
    SFX_0('007_swing_knife_1')
    sprite('hz403_04', 2)	# 78-79
    Unknown1019(30)
    GFX_0('EffGedan', -1)
    sprite('hz403_05', 2)	# 80-81
    Unknown1019(50)
    SFX_0('007_swing_knife_1')
    if SLOT_52:
        Unknown23119(32768, 9, 2)
    sprite('hz403_06', 2)	# 82-83
    SFX_3('hzse_06')
    sprite('hz403_07', 2)	# 84-85
    sprite('hz403_08', 4)	# 86-89	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    Unknown1051(0)
    SFX_0('009_swing_rapier_1')
    SFX_0('004_swing_grap_1_0')
    sprite('hz403_09', 4)	# 90-93
    setInvincible(0)
    Recovery()
    sprite('hz403_10', 3)	# 94-96
    sprite('hz403_11', 3)	# 97-99
    sprite('hz403_12', 3)	# 100-102
    sprite('hz403_13', 3)	# 103-105
    Unknown3029(0)
    sprite('hz403_14', 2)	# 106-107
    sprite('hz403_15', 2)	# 108-109

@State
def LowAssaultB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(3)
        Damage(2200)
        AttackP1(90)
        Unknown11001(0, 5, 10)
        AirUntechableTime(40)
        Hitstop(8)
        PushbackX(2000)
        Hitstop(16)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(22000)
        Unknown9095()
        Unknown9190(0)
        Unknown11058('0000000000000000010000000000000000000000')
        Unknown9016(1)
        HitLow(2)
        Unknown2004(1, 0)
        WhiffCancel('CmnActInvincibleAttack')

        def upon_3():
            SLOT_65 = (SLOT_65 + 2)
            if (SLOT_65 > 22):
                callSubroutine('Kamae_Zanzou')

                def upon_24():
                    sendToLabel(0)
        SLOT_65 = 0
    sprite('hz400_00', 3)	# 1-3
    sprite('hz400_01', 2)	# 4-5
    Unknown1084(1)
    sprite('hz400_01', 1)	# 6-6
    GFX_0('EffKamae', 0)
    GFX_0('EffKamaeLand', -1)
    WhiffCancelEnable(1)
    sprite('hz400_02', 5)	# 7-11
    tag_voice(1, 'bhz200_0', 'bhz200_1', 'bhz200_2', '')
    SFX_3('hzse_05')
    sprite('hz400_03', 5)	# 12-16
    sprite('hz400_04', 5)	# 17-21
    sprite('hz400_05', 5)	# 22-26
    sprite('hz400_06', 5)	# 27-31
    sprite('hz400_07', 5)	# 32-36
    sprite('hz400_08', 5)	# 37-41
    sprite('hz400_09', 5)	# 42-46
    label(0)
    sprite('hz403_00', 1)	# 47-47
    WhiffCancelEnable(0)
    clearUponHandler(3)
    clearUponHandler(24)
    GFX_0('EffLandAura', -1)
    sprite('hz403_00', 1)	# 48-48
    Unknown26('EffKamae')
    Unknown26('EffKamaeLand')
    sprite('hz403_01', 2)	# 49-50
    SFX_0('007_swing_knife_1')
    Unknown1019(200)
    sprite('hz403_02', 2)	# 51-52
    Unknown1019(200)
    sprite('hz403_03', 2)	# 53-54
    tag_voice(0, 'bhz203_0', 'bhz203_1', 'bhz203_2', '')
    SFX_0('007_swing_knife_1')
    sprite('hz403_04', 2)	# 55-56
    Unknown1019(30)
    GFX_0('EffGedan', -1)
    sprite('hz403_05', 2)	# 57-58
    Unknown1019(50)
    SFX_0('007_swing_knife_1')
    if SLOT_52:
        Unknown23119(32768, 9, 2)
    sprite('hz403_06', 1)	# 59-59
    SFX_3('hzse_06')
    sprite('hz403_07', 2)	# 60-61
    sprite('hz403_08', 4)	# 62-65	 **attackbox here**
    RefreshMultihit()
    Unknown1019(0)
    Unknown1051(0)
    SFX_0('009_swing_rapier_1')
    SFX_0('004_swing_grap_1_0')
    sprite('hz403_09', 4)	# 66-69
    setInvincible(0)
    Recovery()
    sprite('hz403_10', 3)	# 70-72
    sprite('hz403_11', 3)	# 73-75
    sprite('hz403_12', 3)	# 76-78
    sprite('hz403_13', 3)	# 79-81
    Unknown3029(0)
    sprite('hz403_14', 2)	# 82-83
    sprite('hz403_15', 2)	# 84-85

@State
def AntiAir():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(0)
        Unknown11092(1)
        Unknown11046(1)
        Unknown11001(7, 30, 30)
        Unknown11056(0)
        Unknown9016(1)
        Unknown11034(0)
        Unknown11033(2)
        AirPushbackX(0)
        Unknown11068(1)
        Unknown12052(2)
        Unknown11058('0000000000000000000000000100000000000000')
        Unknown30048(1)
        Unknown30065(0)
        Unknown11091(10)

        def upon_78():
            setInvincible(1)
            sendToLabel(0)
            Unknown11069('AntiAir')

        def upon_3():
            if SLOT_2:
                if Unknown23146('16000000416e746941697200000000000000000000000000000000000000000000000000'):
                    Unknown48('160000000200000053000000040000000200000053000000')
                    Unknown48('190000000200000033000000040000000200000017000000')
                    SLOT_51 = (SLOT_51 + (-300000))
                    Unknown48('160000000200000017000000190000000200000033000000')
    sprite('hz405_00', 2)	# 1-2
    sprite('hz405_01', 1)	# 3-3
    sprite('hz405_01', 1)	# 4-4
    tag_voice(1, 'bhz205_0', 'bhz205_1', 'bhz205_2', '')
    GFX_0('AntiAirWindSmoke', -1)
    GFX_0('ExBodyAuraAntiAir', -1)
    Unknown36(1)
    Unknown1007(-80000)
    Unknown35()
    Unknown23125('')
    Unknown2058(-5000)
    Unknown1084(1)
    sprite('hz405_02', 2)	# 5-6
    sprite('hz405_03', 2)	# 7-8
    sprite('hz405_04', 2)	# 9-10
    sprite('hz405_05', 3)	# 11-13
    SFX_3('hzse_02')
    SFX_3('hzse_04')
    GFX_0('KusariAntiAir', 109)
    Unknown38(4, 1)
    Unknown4020(4)
    Unknown21015('416e746941697257696e64536d6f6b6500000000000000000000000000000000f501000000000000')
    sprite('hz405_06', 3)	# 14-16
    sprite('hz405_06', 5)	# 17-21
    SLOT_51 = 1
    sprite('hz405_20', 2)	# 22-23
    Unknown23027()
    Unknown21015('416e746941697257696e64536d6f6b6500000000000000000000000000000000f601000000000000')
    Recovery()
    sprite('hz405_21', 2)	# 24-25
    sprite('hz405_22', 2)	# 26-27
    sprite('hz405_23', 2)	# 28-29
    sprite('hz405_24', 2)	# 30-31
    sprite('hz405_25', 2)	# 32-33
    sprite('hz405_26', 2)	# 34-35
    SFX_0('006_swing_blade_0')
    sprite('hz405_27', 3)	# 36-38
    sprite('hz405_28', 3)	# 39-41
    sprite('hz405_29', 3)	# 42-44
    sprite('hz405_30', 3)	# 45-47
    sprite('hz405_31', 3)	# 48-50
    sprite('hz405_32', 3)	# 51-53
    ExitState()
    label(0)
    clearUponHandler(78)
    Unknown2037(1)
    Unknown23029(4, 501, 0)
    Unknown2015(150)
    sprite('hz405_07', 6)	# 54-59
    sprite('hz405_08', 6)	# 60-65
    sprite('hz405_09', 2)	# 66-67
    sprite('hz405_10', 2)	# 68-69
    tag_voice(0, 'bhz206_0', 'bhz206_1', 'bhz206_2', '')
    Unknown21015('416e746941697257696e64536d6f6b6500000000000000000000000000000000f601000000000000')
    sprite('hz405_11', 2)	# 70-71
    SFX_0('011_spin_0')
    sprite('hz405_12', 2)	# 72-73
    Unknown2037(0)
    RefreshMultihit()
    Damage(3300)
    AirPushbackX(-60000)
    AirPushbackY(6000)
    AirUntechableTime(120)
    Unknown11001(0, 0, 0)
    Hitstop(0)
    Unknown9202(25)
    Unknown11068(0)
    Unknown11023(1)
    Unknown9178(1)
    WallbounceReboundTime(0)
    Unknown9310(20)
    Unknown11069('')
    sprite('hz405_13', 5)	# 74-78
    Unknown23027()
    sprite('hz405_14', 5)	# 79-83
    sprite('hz405_15', 20)	# 84-103
    sprite('hz405_15', 7)	# 104-110
    Unknown23073()
    sprite('hz405_16', 5)	# 111-115
    sprite('hz405_17', 5)	# 116-120
    sprite('hz405_18', 5)	# 121-125
    sprite('hz405_19', 5)	# 126-130

@State
def SPThrow():

    def upon_IMMEDIATE():
        Unknown17011('SPThrowExe', 2, 0, 0)
        Unknown11054(120000)
        setInvincible(1)
        Unknown22019('0000000000000000000000000000000001000000')
        physicsXImpulse(8000)
        Unknown2037(1)

        def upon_3():
            if (SLOT_18 >= 25):
                sendToLabel(1)
            if (SLOT_18 >= 3):
                if (SLOT_19 < 180000):
                    sendToLabel(1)
    sprite('hz032_00', 3)	# 1-3
    sprite('hz032_01', 3)	# 4-6
    Unknown23125('')
    Unknown2058(-5000)
    Unknown2037(0)
    Unknown1019(200)
    sprite('hz032_02', 3)	# 7-9
    Unknown8007(100, 1, 1)
    Unknown1019(200)
    sprite('hz032_03', 3)	# 10-12
    sprite('hz032_02', 3)	# 13-15
    sprite('hz032_04', 3)	# 16-18
    Unknown1019(80)
    sprite('hz032_04ex01', 3)	# 19-21
    Unknown1019(60)
    Unknown8010(100, 1, 1)
    sprite('hz032_04ex02', 3)	# 22-24
    sprite('hz032_05', 3)	# 25-27
    Unknown1019(40)
    sprite('hz032_06', 3)	# 28-30
    Unknown1019(20)
    sprite('hz032_07', 3)	# 31-33
    label(1)
    sprite('hz406_00', 3)	# 34-36
    clearUponHandler(3)
    if SLOT_2:
        Unknown23125('')
        Unknown2058(-5000)
    else:
        pass
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    SFX_3('hzse_09')
    sprite('hz406_01', 2)	# 37-38
    SFX_3('hzse_09')
    tag_voice(1, 'bhz207_0', 'bhz207_1', 'bhz207_2', '')
    GFX_0('EffLandAura', -1)
    GFX_0('EffCommandThrowAura', -1)
    sprite('hz406_01', 2)	# 39-40
    sprite('hz406_02', 2)	# 41-42
    GFX_0('EffCommandThrowWind', 0)
    SFX_0('004_swing_grap_1_0')
    sprite('hz406_03', 2)	# 43-44
    SFX_3('hzse_09')
    GFX_0('EffCommandThrowWind', 0)
    sprite('hz406_04', 3)	# 45-47	 **attackbox here**
    GFX_0('EffCommandThrowWind', 1)
    SFX_0('004_swing_grap_1_0')
    Unknown1084(1)
    sprite('hz406_05', 2)	# 48-49
    setInvincible(0)
    sprite('hz406_06', 2)	# 50-51
    sprite('hz406_07', 3)	# 52-54
    sprite('hz406_08', 3)	# 55-57
    sprite('hz406_09', 3)	# 58-60
    sprite('hz406_10', 3)	# 61-63
    sprite('hz406_11', 3)	# 64-66
    sprite('hz406_12', 3)	# 67-69
    sprite('hz406_13', 3)	# 70-72
    sprite('hz406_14', 3)	# 73-75
    sprite('hz406_15', 3)	# 76-78

@State
def SPThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(2, 0, 0)
        AttackLevel_(3)
        Damage(0)
        GroundedHitstunAnimation(4)
        AirHitstunAnimation(4)
        AttackP2(50)
        Hitstop(6)
        Unknown9154(45)
        PushbackX(8000)
        Unknown9016(1)
        Unknown30065(0)
        Unknown11091(10)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('80000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('000000000400000032000000a0000000')
        Unknown3075('00000000000000000000000010000000')
        Unknown3076(1010)
        Unknown3077(900)
    sprite('hz406_04', 12)	# 1-12	 **attackbox here**
    SFX_3('hzse_09')
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown2017(0)
    Unknown5003(1)
    sprite('hz406_16', 3)	# 13-15
    SFX_3('hzse_09')
    sprite('hz406_17', 3)	# 16-18
    SFX_3('hzse_09')
    SFX_0('100_hit_grap_3')
    sprite('hz406_18', 1)	# 19-19	 **attackbox here**
    SFX_3('hzse_09')
    sprite('hz406_19', 6)	# 20-25
    sprite('hz406_20', 4)	# 26-29
    SFX_0('007_swing_knife_2')
    sprite('hz406_21', 2)	# 30-31
    sprite('hz406_22', 2)	# 32-33
    sprite('hz406_23', 2)	# 34-35
    sprite('hz406_24', 2)	# 36-37
    sprite('hz406_25', 2)	# 38-39

@State
def AirAssaultA():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(3)
        AttackP1(80)
        GroundedHitstunAnimation(1)
        AirPushbackY(-68000)
        YImpluseBeforeWallbounce(0)
        AirUntechableTime(50)
        Unknown9310(1)
        Unknown11065(1)
        Unknown9016(1)
        clearUponHandler(2)
        sendToLabelUpon(2, 9)

        def upon_11():
            Unknown2037(1)
    sprite('hz412_00', 3)	# 1-3
    Unknown1084(1)
    physicsYImpulse(12000)
    setGravity(2400)
    physicsXImpulse(4000)
    Unknown3029(1)
    Unknown3069(2)
    Unknown3071(5)
    Unknown3074('00000000ab00000039000000ab000000')
    Unknown3075('00000000000000000000000000000000')
    sprite('hz412_01', 3)	# 4-6
    sprite('hz412_02', 3)	# 7-9
    tag_voice(1, 'bhz215_0', 'bhz215_1', 'bhz215_2', '')
    sprite('hz412_03', 2)	# 10-11	 **attackbox here**
    Unknown1019(50)
    YAccel(120)
    Unknown1039(150)
    Unknown4049(1440)
    Unknown4052()
    Unknown4045('687a65665f343132666c6173680000000000000000000000000000000000000000000000')
    SFX_0('007_swing_knife_2')
    SFX_0('004_swing_grap_1_0')
    sprite('hz412_04', 3)	# 12-14	 **attackbox here**
    GFX_0('Eff412Zanzo', -1)
    label(0)
    sprite('hz412_05', 3)	# 15-17	 **attackbox here**
    sprite('hz412_04', 3)	# 18-20	 **attackbox here**
    loopRest()
    gotoLabel(0)
    label(9)
    sprite('hz412_06', 4)	# 21-24
    Recovery()
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('hz412_07', 4)	# 25-28
    Unknown3029(0)
    if (not SLOT_2):
        Unknown13021(1)
        Unknown13016(1)
        Unknown13017(1)
        Unknown13014(1)
        Unknown13015(1)
        Unknown13003(1)
        Unknown13002(1)
    sprite('hz412_08', 4)	# 29-32
    sprite('hz412_09', 4)	# 33-36

@State
def AirAssaultB():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(-60000)
        AirPushbackX(30000)
        AirUntechableTime(50)
        Unknown9015(1)
        Unknown9310(1)
        physicsXImpulse(10000)
        physicsYImpulse(10000)
        setGravity(900)
        Unknown22004(10, 1)
    sprite('hz404_00', 2)	# 1-2
    tag_voice(1, 'bhz204_0', 'bhz204_1', 'bhz204_2', '')
    GFX_0('EffAirAura', -1)
    Unknown36(1)
    Unknown1007(320000)
    Unknown35()
    sprite('hz404_01', 1)	# 3-3
    GFX_0('EffUchiOtoshi', -1)
    sprite('hz404_01', 1)	# 4-4
    sprite('hz404_02', 3)	# 5-7
    SFX_0('004_swing_grap_1_0')
    SFX_3('hzse_06')
    sprite('hz404_03', 2)	# 8-9
    SFX_0('004_swing_grap_1_1')
    sprite('hz404_04', 2)	# 10-11	 **attackbox here**
    Unknown1019(50)
    sprite('hz404_05', 2)	# 12-13	 **attackbox here**
    Unknown1019(50)
    setGravity(2000)
    sprite('hz404_06', 2)	# 14-15	 **attackbox here**
    sprite('hz404_07', 3)	# 16-18
    Recovery()
    sprite('hz404_08', 3)	# 19-21
    sprite('hz404_09', 3)	# 22-24
    sprite('hz404_10', 3)	# 25-27
    sprite('hz404_11', 3)	# 28-30
    sprite('hz404_12', 3)	# 31-33

@State
def AirAssaultC():

    def upon_IMMEDIATE():
        Unknown17003()
        AttackLevel_(4)
        Damage(1100)
        AttackP1(80)
        AirHitstunAnimation(10)
        GroundedHitstunAnimation(10)
        AirPushbackY(-60000)
        AirPushbackX(30000)
        AirUntechableTime(50)
        Unknown9015(1)
        Hitstop(6)
        Unknown9310(1)
        Unknown11056(0)
        physicsXImpulse(10000)
        physicsYImpulse(10000)
        setGravity(900)
        Unknown22004(10, 1)
    sprite('hz404_00', 2)	# 1-2
    tag_voice(1, 'bhz204_0', 'bhz204_1', 'bhz204_2', '')
    GFX_0('EffAirAura', -1)
    Unknown36(1)
    Unknown1007(320000)
    Unknown35()
    sprite('hz404_01', 1)	# 3-3
    GFX_0('EffUchiOtoshi', -1)
    sprite('hz404_01', 1)	# 4-4
    Unknown23125('')
    Unknown2058(-5000)
    sprite('hz404_02', 3)	# 5-7
    SFX_0('004_swing_grap_1_0')
    SFX_3('hzse_06')
    sprite('hz404_03', 2)	# 8-9
    SFX_0('004_swing_grap_1_1')
    sprite('hz404_04', 2)	# 10-11	 **attackbox here**
    Unknown1019(50)
    sprite('hz404_05', 2)	# 12-13	 **attackbox here**
    RefreshMultihit()
    Unknown1019(50)
    setGravity(2000)
    sprite('hz404_06', 2)	# 14-15	 **attackbox here**
    RefreshMultihit()
    sprite('hz404_07', 2)	# 16-17
    Recovery()
    sprite('hz404_08', 2)	# 18-19
    sprite('hz404_09', 2)	# 20-21
    sprite('hz404_10', 2)	# 22-23
    sprite('hz404_11', 2)	# 24-25
    sprite('hz404_12', 2)	# 26-27

@State
def UltimateAssault():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(0)
        AttackLevel_(5)
        Damage(3980)
        AttackP1(60)
        AttackP2(80)
        Hitstop(30)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(90000)
        AirPushbackX(3000)
        YImpluseBeforeWallbounce(1600)
        AirUntechableTime(120)
        Unknown11056(0)
        sendToLabelUpon(2, 1)
        Unknown2004(1, 0)

        def upon_STATE_END():
            Unknown3001(255)
        if SLOT_136:
            Unknown10000(80)
    sprite('hz430_00', 3)	# 1-3
    setInvincible(1)
    sprite('hz430_00', 30)	# 4-33
    tag_voice(1, 'bhz250_0', 'bhz250_1', '', '')
    Unknown2036(40, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EffUltimateAssaultBunshinA', -1)
    GFX_0('EffUltimateAssaultBunshinB', -1)
    Unknown3032()
    Unknown3004(-10)
    sprite('hz430_01', 3)	# 34-36
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(40000)
    Unknown3004(150)
    sprite('hz430_02', 3)	# 37-39
    Unknown1019(25)
    sprite('hz430_03', 3)	# 40-42
    Unknown1019(25)
    sprite('hz430_04', 2)	# 43-44
    Unknown1019(25)
    SFX_0('004_swing_grap_1_2')
    Unknown8004(100, 1, 1)
    GFX_0('HZEF_UltimateAssault', -1)
    sprite('hz430_05', 3)	# 45-47	 **attackbox here**
    SFX_3('hzse_14')
    tag_voice(0, 'bhz251_0', 'bhz251_1', '', '')
    ScreenShake(10000, 10000)
    setInvincible(0)
    sprite('hz430_06', 5)	# 48-52
    physicsYImpulse(8000)
    sprite('hz430_07', 5)	# 53-57
    Unknown1044()
    sprite('hz430_08', 5)	# 58-62
    label(0)
    sprite('hz430_09', 5)	# 63-67
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz430_10', 3)	# 68-70
    Unknown1019(0)
    sprite('hz430_11', 3)	# 71-73
    sprite('hz430_12', 3)	# 74-76
    sprite('hz430_13', 3)	# 77-79
    sprite('hz430_14', 3)	# 80-82
    sprite('hz430_15', 4)	# 83-86
    sprite('hz430_16', 4)	# 87-90
    sprite('hz430_17', 4)	# 91-94
    sprite('hz430_18', 4)	# 95-98

@State
def UltimateAssault_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(0)
        AttackLevel_(5)
        Damage(4980)
        AttackP1(60)
        AttackP2(80)
        Hitstop(30)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(90000)
        AirPushbackX(3000)
        YImpluseBeforeWallbounce(1600)
        AirUntechableTime(120)
        Unknown11056(0)
        sendToLabelUpon(2, 1)
        Unknown2004(1, 0)

        def upon_12():
            ScreenShake(40000, 40000)

        def upon_STATE_END():
            Unknown3001(255)
        if SLOT_136:
            Unknown10000(80)
    sprite('hz430_00', 3)	# 1-3
    setInvincible(1)
    sprite('hz430_00', 30)	# 4-33
    tag_voice(1, 'bhz250_0', 'bhz250_1', '', '')
    Unknown2036(40, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EffUltimateAssaultBunshinA', -1)
    GFX_0('EffUltimateAssaultBunshinB', -1)
    Unknown3032()
    Unknown3004(-10)
    sprite('hz430_01', 3)	# 34-36
    SFX_FOOTSTEP_(100, 1, 1)
    physicsXImpulse(50000)
    Unknown3004(150)
    sprite('hz430_02', 3)	# 37-39
    Unknown1019(25)
    sprite('hz430_03', 3)	# 40-42
    Unknown1019(25)
    SFX_3('hzse_07')
    sprite('hz430_04', 2)	# 43-44
    Unknown1019(25)
    SFX_0('004_swing_grap_1_2')
    Unknown8004(100, 1, 1)
    GFX_0('HZEF_UltimateAssault', -1)
    GFX_0('HZEF_UltimateAssaultOD', -1)
    sprite('hz430_05', 3)	# 45-47	 **attackbox here**
    SFX_3('hzse_14')
    tag_voice(0, 'bhz251_0', 'bhz251_1', '', '')
    ScreenShake(10000, 10000)
    setInvincible(0)
    sprite('hz430_06', 5)	# 48-52
    physicsYImpulse(8000)
    sprite('hz430_07', 5)	# 53-57
    Unknown1044()
    sprite('hz430_08', 5)	# 58-62
    label(0)
    sprite('hz430_09', 5)	# 63-67
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('hz430_10', 3)	# 68-70
    Unknown1019(0)
    sprite('hz430_11', 3)	# 71-73
    sprite('hz430_12', 3)	# 74-76
    sprite('hz430_13', 3)	# 77-79
    sprite('hz430_14', 3)	# 80-82
    sprite('hz430_15', 4)	# 83-86
    sprite('hz430_16', 4)	# 87-90
    sprite('hz430_17', 4)	# 91-94
    sprite('hz430_18', 4)	# 95-98

@State
def UltimateShot():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(1)
        Damage(500)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(1)
        Unknown11066(1)
        Unknown11064(1)
        Unknown9016(1)
        Unknown30048(1)
        Unknown2004(1, 0)
        Unknown23027()
        Unknown1084(1)

        def upon_3():
            if SLOT_2:
                pass
            if SLOT_53:
                if SLOT_54:
                    SLOT_54 = 0
                    sendToLabel(22)
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 1009):
                Unknown2064(1)
                Unknown11108('03000000')
            if (SLOT_48 == 1008):
                if (not SLOT_55):
                    SLOT_55 = 1
                    sendToLabel(0)
            if (SLOT_48 == 1010):
                SLOT_53 = 1

        def upon_STATE_END():
            Unknown12046(0)
        Unknown13024(0)
        Unknown11069('UltimateShot')
    sprite('hz431_00', 4)	# 1-4
    setInvincible(1)
    Unknown2036(30, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('UltimateLockMagic', -1)
    GFX_0('DDLockAura', -1)
    sprite('hz431_01', 2)	# 5-6
    SFX_3('hzse_05')
    sprite('hz431_02', 20)	# 7-26
    tag_voice(1, 'bhz252_0', 'bhz252_1', '', '')
    sprite('hz431_02', 11)	# 27-37
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('hz431_03', 4)	# 38-41
    Unknown21015('556c74696d6174654c6f636b4d61676963000000000000000000000000000000e903000000000000')
    sprite('hz431_04', 4)	# 42-45
    sprite('hz431_05', 4)	# 46-49
    GFX_0('UltimateLockObj', -1)
    Unknown21015('556c74696d6174654c6f636b4d61676963000000000000000000000000000000ea03000000000000')
    GFX_0('EffUltimateLockSignal', -1)
    sprite('hz431_06', 3)	# 50-52
    Unknown13024(1)
    setInvincible(0)
    Unknown21015('556c74696d6174654c6f636b4f626a43656e7465720000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a546f700000000000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a426f74746f6d0000000000000000000000eb03000000000000')
    Unknown21015('44444c6f636b4175726100000000000000000000000000000000000000000000eb03000000000000')
    sprite('hz431_07', 3)	# 53-55
    sprite('hz431_08', 3)	# 56-58
    sprite('hz431_06', 3)	# 59-61
    sprite('hz431_07', 3)	# 62-64
    sprite('hz431_08', 3)	# 65-67
    sprite('hz431_06', 3)	# 68-70
    sprite('hz431_07', 3)	# 71-73
    sprite('hz431_08', 3)	# 74-76
    sprite('hz431_06', 3)	# 77-79
    sprite('hz431_07', 3)	# 80-82
    sprite('hz431_08', 3)	# 83-85
    sprite('hz431_56', 3)	# 86-88
    sprite('hz431_57', 3)	# 89-91
    sprite('hz431_58', 3)	# 92-94
    sprite('hz431_59', 3)	# 95-97
    sprite('hz431_60', 3)	# 98-100
    loopRest()
    ExitState()
    label(0)
    Unknown21015('44444c6f636b4175726100000000000000000000000000000000000000000000eb03000000000000')
    sprite('hz431_06', 4)	# 101-104
    Unknown2006()
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('hz431_07', 4)	# 105-108
    Unknown12046(25)
    sprite('hz431_08', 4)	# 109-112
    Unknown12046(50)
    sprite('hz431_06', 5)	# 113-117
    Unknown12046(75)
    sprite('hz431_07', 5)	# 118-122
    Unknown12046(100)
    sprite('hz431_08', 5)	# 123-127
    Unknown12046(125)
    sprite('hz431_09', 3)	# 128-130
    Unknown23027()
    Unknown12046(150)
    sprite('hz431_10', 3)	# 131-133
    Unknown12046(175)
    sprite('hz431_11', 3)	# 134-136
    GFX_0('UltimateKusari', 109)
    SLOT_54 = 1
    Unknown12046(200)
    sprite('hz431_12', 3)	# 137-139
    Unknown21015('556c74696d6174654c6f636b4f626a43656e7465720000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a546f700000000000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a426f74746f6d0000000000000000000000eb03000000000000')
    SLOT_52 = 10
    loopRest()
    label(1)
    sprite('hz431_13', 3)	# 140-142
    sprite('hz431_14', 3)	# 143-145
    sprite('hz431_15', 2)	# 146-147
    sprite('hz431_15', 1)	# 148-148
    SLOT_52 = (SLOT_52 + (-1))
    if SLOT_52:
        _gotolabel(1)
    label(22)
    SLOT_54 = 0
    Unknown12046(0)
    sprite('hz431_16', 4)	# 149-152
    sprite('hz431_17', 4)	# 153-156
    SFX_0('011_spin_0')
    sprite('hz431_18', 4)	# 157-160
    sprite('hz431_19', 8)	# 161-168
    sprite('hz431_20', 28)	# 169-196
    sprite('hz431_21', 5)	# 197-201
    loopRest()
    Unknown2017(0)
    GFX_0('UltimateWindSmoke', -1)
    GFX_1('hzef_ultimateauraopt', -1)
    GFX_0('DDBodyAura', -1)
    tag_voice(0, 'bhz253_0', 'bhz253_1', '', '')
    sprite('hz431_22', 1)	# 202-202	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23', 1)	# 203-203	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 204-204
    sprite('hz431_24', 1)	# 205-205	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25', 1)	# 206-206	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 207-207
    sprite('hz431_26', 1)	# 208-208	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27', 1)	# 209-209	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 210-210
    sprite('hz431_28', 1)	# 211-211	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29', 1)	# 212-212	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 213-213
    sprite('hz431_22', 1)	# 214-214	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23', 1)	# 215-215	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 216-216
    sprite('hz431_24', 1)	# 217-217	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25', 1)	# 218-218	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 219-219
    sprite('hz431_26', 1)	# 220-220	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27', 1)	# 221-221	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 222-222
    sprite('hz431_28', 1)	# 223-223	 **attackbox here**
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(20000)
    AirPushbackX(2000)
    YImpluseBeforeWallbounce(700)
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29', 1)	# 224-224	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('hz431_30', 3)	# 225-227
    GFX_0('HZEF_DDBackAura', -1)
    Unknown21015('556c74696d61746557696e64536d6f6b65000000000000000000000000000000ec03000000000000')
    Unknown21015('4444426f64794175726100000000000000000000000000000000000000000000ee03000000000000')
    sprite('hz431_31', 3)	# 228-230
    sprite('hz431_32', 3)	# 231-233
    sprite('hz431_33', 3)	# 234-236
    sprite('hz431_34', 3)	# 237-239
    sprite('hz431_35', 3)	# 240-242
    SFX_3('hzse_08')
    SFX_3('hzse_05')
    sprite('hz431_36', 3)	# 243-245
    sprite('hz431_37', 2)	# 246-247
    sprite('hz431_38', 3)	# 248-250
    GFX_0('EffDDSnakeFang', -1)
    ScreenShake(0, 10000)
    sprite('hz431_39', 3)	# 251-253
    ScreenShake(0, 8000)
    sprite('hz431_38', 3)	# 254-256
    ScreenShake(0, 6000)
    sprite('hz431_39', 3)	# 257-259
    ScreenShake(0, 4000)
    sprite('hz431_38', 3)	# 260-262
    ScreenShake(0, 2000)
    sprite('hz431_39', 3)	# 263-265
    sprite('hz431_38', 3)	# 266-268
    sprite('hz431_39', 3)	# 269-271
    sprite('hz431_38', 3)	# 272-274
    sprite('hz431_39', 3)	# 275-277
    sprite('hz431_40', 2)	# 278-279
    Unknown20000(1)
    Unknown21015('556c74696d61746557696e64536d6f6b65000000000000000000000000000000ed03000000000000')
    sprite('hz431_41', 1)	# 280-280
    SFX_0('009_swing_rapier_1')
    sprite('hz431_42', 3)	# 281-283	 **attackbox here**
    SFX_3('hzse_14')
    SFX_3('hzse_03')
    ScreenShake(15000, 15000)
    Unknown11064(0)
    AttackLevel_(4)
    Damage(3000)
    AttackP2(60)
    AirHitstunAnimation(9)
    GroundedHitstunAnimation(9)
    AirPushbackY(10000)
    AirPushbackX(50000)
    YImpluseBeforeWallbounce(1300)
    Unknown9202(20)
    Unknown9310(22)
    Hitstop(12)
    RefreshMultihit()
    Unknown11068(1)
    Unknown11078(1)
    Unknown11069('')
    Unknown13024(1)
    Unknown20000(0)
    setInvincible(0)
    Unknown23159('UltimateShotFinish')
    sprite('hz431_43', 5)	# 284-288
    Unknown2017(1)
    Unknown21015('485a45465f44444261636b417572610000000000000000000000000000000000eb03000000000000')
    Unknown21015('4444426f64794175726100000000000000000000000000000000000000000000ef03000000000000')
    sprite('hz431_44', 5)	# 289-293
    sprite('hz431_45', 5)	# 294-298
    sprite('hz431_43', 5)	# 299-303
    sprite('hz431_44', 5)	# 304-308
    sprite('hz431_45', 5)	# 309-313
    sprite('hz431_43', 5)	# 314-318
    sprite('hz431_44', 5)	# 319-323
    sprite('hz431_45', 5)	# 324-328
    sprite('hz431_46', 5)	# 329-333
    sprite('hz431_47', 5)	# 334-338
    sprite('hz431_48', 5)	# 339-343
    sprite('hz431_49', 5)	# 344-348
    SFX_3('hzse_09')
    sprite('hz431_50', 4)	# 349-352
    SFX_3('hzse_09')
    sprite('hz431_51', 4)	# 353-356
    SFX_3('hzse_09')
    sprite('hz431_52', 3)	# 357-359
    SFX_0('007_swing_knife_2')
    sprite('hz431_53', 12)	# 360-371
    sprite('hz431_55', 4)	# 372-375

@State
def UltimateShot_OD():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        AttackLevel_(1)
        Damage(250)
        AttackP2(100)
        GroundedHitstunAnimation(1)
        AirUntechableTime(100)
        AirPushbackY(0)
        AirPushbackX(0)
        Hitstop(2)
        Unknown11066(1)
        Unknown11064(1)
        Unknown9016(1)
        Unknown2004(1, 0)
        SLOT_64 = 1

        def upon_STATE_END():
            SLOT_64 = 0

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(100)

        def upon_3():
            if SLOT_2:
                pass
            if SLOT_53:
                if SLOT_54:
                    SLOT_54 = 0
                    sendToLabel(22)
        Unknown2064(0)

        def upon_43():
            if (SLOT_48 == 1009):
                Unknown2064(1)
                Unknown11108('03000000')
            if (SLOT_48 == 1008):
                if (not SLOT_2):
                    Unknown2038(1)
                    sendToLabel(0)
            if (SLOT_48 == 1010):
                SLOT_53 = 1

        def upon_STATE_END():
            Unknown12046(0)
        Unknown13024(0)
        Unknown11069('UltimateShot_OD')
    sprite('hz431_00', 4)	# 1-4
    setInvincible(1)
    Unknown2036(30, -1, 0)
    Unknown30080('')
    Unknown2058(-10000)
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('UltimateLockMagic', -1)
    GFX_0('DDLockAura', -1)
    sprite('hz431_01', 2)	# 5-6
    SFX_3('hzse_05')
    sprite('hz431_02', 20)	# 7-26
    tag_voice(1, 'bhz252_0', 'bhz252_1', '', '')
    sprite('hz431_02', 11)	# 27-37
    Unknown22019('0000000000000000000000000100000000000000')
    sprite('hz431_03', 4)	# 38-41
    Unknown21015('556c74696d6174654c6f636b4d61676963000000000000000000000000000000e903000000000000')
    sprite('hz431_04', 4)	# 42-45
    sprite('hz431_05', 4)	# 46-49
    GFX_0('UltimateLockObj_OD', -1)
    Unknown21015('556c74696d6174654c6f636b4d61676963000000000000000000000000000000ea03000000000000')
    GFX_0('EffUltimateLockSignal', -1)
    sprite('hz431_06', 3)	# 50-52
    Unknown13024(1)
    setInvincible(0)
    Unknown21015('556c74696d6174654c6f636b4f626a43656e7465720000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a546f700000000000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a426f74746f6d0000000000000000000000eb03000000000000')
    Unknown21015('44444c6f636b4175726100000000000000000000000000000000000000000000eb03000000000000')
    sprite('hz431_07', 3)	# 53-55
    sprite('hz431_08', 3)	# 56-58
    sprite('hz431_06', 3)	# 59-61
    sprite('hz431_07', 3)	# 62-64
    sprite('hz431_08', 3)	# 65-67
    sprite('hz431_06', 3)	# 68-70
    sprite('hz431_07', 3)	# 71-73
    sprite('hz431_08', 3)	# 74-76
    sprite('hz431_06', 3)	# 77-79
    sprite('hz431_07', 3)	# 80-82
    sprite('hz431_08', 3)	# 83-85
    sprite('hz431_56', 3)	# 86-88
    sprite('hz431_57', 3)	# 89-91
    sprite('hz431_58', 3)	# 92-94
    sprite('hz431_59', 3)	# 95-97
    sprite('hz431_60', 3)	# 98-100
    loopRest()
    ExitState()
    label(0)
    Unknown21015('44444c6f636b4175726100000000000000000000000000000000000000000000eb03000000000000')
    sprite('hz431_06', 4)	# 101-104
    Unknown2006()
    setInvincible(1)
    Unknown22019('0100000001000000010000000100000001000000')
    sprite('hz431_07', 4)	# 105-108
    Unknown12046(25)
    sprite('hz431_08', 4)	# 109-112
    Unknown12046(50)
    sprite('hz431_06', 5)	# 113-117
    Unknown12046(75)
    sprite('hz431_07', 5)	# 118-122
    Unknown12046(100)
    sprite('hz431_08', 5)	# 123-127
    Unknown12046(125)
    sprite('hz431_09', 3)	# 128-130
    Unknown23027()
    Unknown12046(150)
    sprite('hz431_10', 3)	# 131-133
    Unknown12046(175)
    sprite('hz431_11', 3)	# 134-136
    GFX_0('UltimateKusari', 109)
    SLOT_54 = 1
    Unknown12046(200)
    sprite('hz431_12', 3)	# 137-139
    Unknown21015('556c74696d6174654c6f636b4f626a43656e7465720000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a546f700000000000000000000000000000eb03000000000000')
    Unknown21015('556c74696d6174654c6f636b4f626a426f74746f6d0000000000000000000000eb03000000000000')
    SLOT_52 = 10
    loopRest()
    label(1)
    sprite('hz431_13', 3)	# 140-142
    sprite('hz431_14', 3)	# 143-145
    sprite('hz431_15', 2)	# 146-147
    sprite('hz431_15', 1)	# 148-148
    SLOT_52 = (SLOT_52 + (-1))
    if SLOT_52:
        _gotolabel(1)
    label(22)
    SLOT_54 = 0
    Unknown12046(0)
    sprite('hz431_16', 4)	# 149-152
    sprite('hz431_17', 4)	# 153-156
    SFX_0('011_spin_0')
    sprite('hz431_18', 4)	# 157-160
    sprite('hz431_19', 8)	# 161-168
    sprite('hz431_20', 28)	# 169-196
    sprite('hz431_21', 5)	# 197-201
    loopRest()
    Unknown2017(0)
    GFX_0('UltimateWindSmoke', -1)
    GFX_1('hzef_ultimateauraopt', -1)
    GFX_0('DDBodyAura', -1)
    tag_voice(0, 'bhz253_0', 'bhz253_1', '', '')
    sprite('hz431_22', 1)	# 202-202	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23', 1)	# 203-203	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 204-204
    sprite('hz431_24', 1)	# 205-205	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25', 1)	# 206-206	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 207-207
    sprite('hz431_26', 1)	# 208-208	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27', 1)	# 209-209	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 210-210
    sprite('hz431_28', 1)	# 211-211	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29', 1)	# 212-212	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 213-213
    sprite('hz431_22', 1)	# 214-214	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    sprite('hz431_23', 1)	# 215-215	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 216-216
    sprite('hz431_24', 1)	# 217-217	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    sprite('hz431_25', 1)	# 218-218	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 219-219
    sprite('hz431_26', 1)	# 220-220	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    sprite('hz431_27', 1)	# 221-221	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 222-222
    sprite('hz431_28', 1)	# 223-223	 **attackbox here**
    RefreshMultihit()
    sprite('hz431_29', 1)	# 224-224	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    Hitstop(1)
    sprite('hz431_22', 1)	# 225-225	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 226-226
    sprite('hz431_24', 1)	# 227-227	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 228-228
    sprite('hz431_26', 1)	# 229-229	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 230-230
    sprite('hz431_28', 1)	# 231-231	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 232-232
    sprite('hz431_22', 1)	# 233-233	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 234-234
    sprite('hz431_24', 1)	# 235-235	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 236-236
    sprite('hz431_26', 1)	# 237-237	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 238-238
    sprite('hz431_28', 1)	# 239-239	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29', 1)	# 240-240	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('hz431_22', 1)	# 241-241	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 242-242
    sprite('hz431_24', 1)	# 243-243	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 244-244
    sprite('hz431_26', 1)	# 245-245	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 246-246
    sprite('hz431_28', 1)	# 247-247	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 248-248
    sprite('hz431_22', 1)	# 249-249	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoA', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 250-250
    sprite('hz431_24', 1)	# 251-251	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoB', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 252-252
    sprite('hz431_26', 1)	# 253-253	 **attackbox here**
    RefreshMultihit()
    GFX_0('EffDDZanzoC', -1)
    SFX_0('009_swing_rapier_0')
    sprite('null', 1)	# 254-254
    sprite('hz431_28', 1)	# 255-255	 **attackbox here**
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(20000)
    AirPushbackX(2000)
    YImpluseBeforeWallbounce(700)
    Unknown11072(1, 200000, 40000)
    RefreshMultihit()
    GFX_0('EffDDZanzoD', -1)
    sprite('hz431_29', 1)	# 256-256	 **attackbox here**
    SFX_0('009_swing_rapier_0')
    sprite('hz431_30', 3)	# 257-259
    sprite('hz431_31', 3)	# 260-262
    sprite('hz431_32', 3)	# 263-265
    sprite('hz431_33', 3)	# 266-268
    Unknown21015('556c74696d61746557696e64536d6f6b65000000000000000000000000000000ed03000000000000')
    GFX_0('hzef432_bind', -1)
    SFX_0('022_magiccircle_c')
    sprite('hz432_10', 3)	# 269-271
    GFX_0('HZEF_DDBackAura', -1)
    sprite('hz432_11', 3)	# 272-274
    sprite('hz432_12', 3)	# 275-277
    Unknown21015('4444426f64794175726100000000000000000000000000000000000000000000ef03000000000000')
    sprite('hz432_13', 3)	# 278-280
    sprite('hz432_14', 3)	# 281-283
    sprite('hz432_15', 3)	# 284-286
    sprite('hz432_13', 3)	# 287-289
    sprite('hz432_14', 3)	# 290-292
    tag_voice(0, 'bhz254_0', 'bhz254_1', '', '')
    GFX_0('EffDDSnakeFangOD', -1)
    sprite('hz432_15', 3)	# 293-295
    sprite('hz432_16', 3)	# 296-298
    sprite('hz432_17', 3)	# 299-301
    sprite('hz432_18', 4)	# 302-305
    Unknown21015('485a45465f44444261636b417572610000000000000000000000000000000000eb03000000000000')
    sprite('hz432_19', 2)	# 306-307
    Unknown2016(360)
    physicsXImpulse(2000)
    physicsYImpulse(10000)
    setGravity(1500)
    sprite('hz432_20', 2)	# 308-309	 **attackbox here**
    RefreshMultihit()
    AttackLevel_(4)
    Damage(1250)
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(5000)
    AirPushbackY(17000)
    Unknown9095()
    Unknown9016(0)
    Unknown9015(1)
    Hitstop(13)
    Unknown9310(1)
    Unknown11050('000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown11072(0, 0, 0)
    Unknown21015('687a65663433325f62696e640000000000000000000000000000000000000000eb03000000000000')
    sprite('hz432_21', 3)	# 310-312
    sprite('hz432_22', 3)	# 313-315
    sprite('hz432_47', 3)	# 316-318
    SFX_3('hzse_11')
    sprite('hz432_48', 32767)	# 319-33085
    SFX_3('hzse_12')
    label(100)
    sprite('hz432_49', 3)	# 33086-33088	 **attackbox here**
    RefreshMultihit()
    AttackP2(60)
    AirHitstunAnimation(18)
    GroundedHitstunAnimation(18)
    Unknown9178(1)
    WallbounceReboundTime(0)
    AirPushbackX(50000)
    AirPushbackY(15000)
    Hitstop(20)
    Unknown9310(60)
    Unknown11064(0)
    Unknown1084(1)
    ScreenShake(50000, 50000)
    SFX_0('005_swing_grap_2_0')
    SFX_0('025_cleanhit_grap')
    SFX_0('025_cleanhit_grap')
    SFX_0('213_bound_1')
    SFX_3('hzse_12')
    Unknown23159('UltimateShot_ODFinish')
    Unknown13024(1)
    Unknown11069('')
    sprite('hz432_50', 5)	# 33089-33093
    sprite('hz432_51', 5)	# 33094-33098
    sprite('hz432_52', 5)	# 33099-33103
    sprite('hz432_53', 5)	# 33104-33108
    sprite('hz432_53ex', 5)	# 33109-33113
    clearUponHandler(3)
    sprite('hz432_57', 5)	# 33114-33118
    sprite('hz432_58', 5)	# 33119-33123
    sprite('hz432_59', 5)	# 33124-33128
    sprite('hz601_17', 5)	# 33129-33133
    SFX_0('019_cloth_a')
    sprite('hz601_18', 5)	# 33134-33138
    sprite('hz601_19', 5)	# 33139-33143
    sprite('hz301_00', 5)	# 33144-33148
    sprite('hz301_01', 5)	# 33149-33153
    sprite('hz301_02', 5)	# 33154-33158
    sprite('hz301_03', 5)	# 33159-33163
    sprite('hz301_02', 5)	# 33164-33168
    sprite('hz301_03', 5)	# 33169-33173
    sprite('hz301_02', 5)	# 33174-33178
    sprite('hz301_03', 5)	# 33179-33183
    sprite('hz301_04', 5)	# 33184-33188
    sprite('hz301_05', 5)	# 33189-33193
    sprite('hz301_06', 5)	# 33194-33198
    sprite('hz301_07', 5)	# 33199-33203

@State
def AstralHeat():

    def upon_IMMEDIATE():
        Unknown17018()
        Unknown11069('AstralHeat')
        AttackLevel_(3)
        Unknown11068(1)
        Unknown11078(1)
        Unknown11091(100)
        setInvincible(1)
        Unknown1084(1)

        def upon_43():
            if (SLOT_48 == 1512):
                Unknown23157(0)
                Unknown2037(1)
    sprite('hz450_00', 4)	# 1-4
    SFX_4('bhz290')
    Unknown2036(46, -1, 2)
    Unknown23147()
    Unknown4004('6175726100000000000000000000000000000000000000000000000000000000ffff0000')
    GFX_0('EMB_AST', -1)
    Unknown23024(2)
    Unknown20000(1)
    Unknown20003(1)
    sprite('hz450_01', 6)	# 5-10
    sprite('hz450_02', 6)	# 11-16
    sprite('hz450_03', 25)	# 17-41
    sprite('hz450_04', 6)	# 42-47
    sprite('hz450_05', 6)	# 48-53
    sprite('hz450_06', 3)	# 54-56
    sprite('hz450_07', 3)	# 57-59
    sprite('hz450_08', 3)	# 60-62
    GFX_0('HZEF_ASTBACK', -1)
    GFX_0('HZEF_ASTMagicCircle', -1)
    SFX_0('015_blaze_1')
    sprite('hz450_09', 3)	# 63-65
    GFX_0('KusariAstral', 0)
    Unknown23029(1, 1501, 0)
    SFX_0('019_quake_0')
    SFX_3('hzse_06')
    sprite('hz450_10', 3)	# 66-68
    GFX_0('KusariAstral', 1)
    Unknown23029(1, 1502, 0)
    sprite('hz450_11', 3)	# 69-71
    GFX_0('KusariAstral', 2)
    Unknown23029(1, 1503, 0)
    sprite('hz450_12', 3)	# 72-74
    GFX_0('KusariAstral', 3)
    Unknown23029(1, 1504, 0)
    SFX_3('hzse_06')
    sprite('hz450_13', 3)	# 75-77
    GFX_0('KusariAstral', 4)
    Unknown23029(1, 1505, 0)
    sprite('hz450_09', 3)	# 78-80
    GFX_0('KusariAstral', 5)
    Unknown23029(1, 1506, 0)
    sprite('hz450_10', 3)	# 81-83
    GFX_0('KusariAstral', 6)
    Unknown23029(1, 1507, 0)
    sprite('hz450_11', 3)	# 84-86
    GFX_0('KusariAstral', 7)
    Unknown23029(1, 1508, 0)
    sprite('hz450_12', 3)	# 87-89
    sprite('hz450_13', 3)	# 90-92
    sprite('hz450_09', 3)	# 93-95
    SFX_0('019_quake_0')
    sprite('hz450_10', 3)	# 96-98
    sprite('hz450_11', 3)	# 99-101
    sprite('hz450_12', 3)	# 102-104
    sprite('hz450_13', 3)	# 105-107
    sprite('hz450_09', 3)	# 108-110
    sprite('hz450_10', 3)	# 111-113
    sprite('hz450_11', 3)	# 114-116
    sprite('hz450_12', 3)	# 117-119
    sprite('hz450_13', 3)	# 120-122
    sprite('hz450_09', 3)	# 123-125
    sprite('hz450_10', 3)	# 126-128
    sprite('hz450_11', 3)	# 129-131
    sprite('hz450_12', 3)	# 132-134
    sprite('hz450_13', 3)	# 135-137
    Unknown21015('4b757361726941737472616c0000000000000000000000000000000000000000e605000000000000')
    loopRest()
    if SLOT_2:
        _gotolabel(0)
    sprite('hz450_23', 4)	# 138-141
    setInvincible(0)
    Unknown21015('4b757361726941737472616c0000000000000000000000000000000000000000e705000000000000')
    sprite('hz450_24', 4)	# 142-145
    sprite('hz450_25', 4)	# 146-149
    sprite('hz450_26', 4)	# 150-153
    sprite('hz450_27', 4)	# 154-157
    sprite('hz450_28', 4)	# 158-161
    loopRest()
    ExitState()
    label(0)
    Unknown23084(1)
    Unknown20004(1)
    Unknown20006(1)
    Unknown23024(3)
    Unknown21015('485a45465f4153544241434b0000000000000000000000000000000000000000e705000000000000')
    sprite('hz450_14', 3)	# 162-164
    tag_voice(1, 'bhz291', 'bhz293', '', '')
    SFX_0('019_quake_0')
    sprite('hz450_15', 3)	# 165-167
    Unknown23088(1, 1)
    sprite('hz450_16', 3)	# 168-170
    GFX_0('HZEF_ASTSIGNAL', -1)
    sprite('hz450_17', 3)	# 171-173
    Unknown21015('4b757361726941737472616c0000000000000000000000000000000000000000e705000000000000')
    loopRest()
    loopRelated(17, 350)
    sendToLabelUpon(17, 2)
    sprite('hz450_18', 6)	# 174-179
    SFX_3('hzse_00')
    SFX_3('hzse_05')
    GFX_0('AST_Enshutsu', -1)
    sprite('hz450_19', 6)	# 180-185
    sprite('hz450_20', 6)	# 186-191
    sprite('hz450_21', 6)	# 192-197
    sprite('hz450_22', 6)	# 198-203
    Unknown3032()
    Unknown3004(-1)
    loopRest()
    sprite('hz450_18', 6)	# 204-209
    sprite('hz450_19', 6)	# 210-215
    sprite('hz450_20', 6)	# 216-221
    SFX_3('hzse_08')
    SFX_0('015_blaze_0')
    SFX_0('019_quake_0')
    sprite('hz450_21', 6)	# 222-227
    SFX_0('019_quake_1')
    SFX_3('hzse_08')
    sprite('hz450_22', 6)	# 228-233
    SFX_0('019_quake_0')
    loopRest()
    label(1)
    sprite('hz450_18', 6)	# 234-239
    SFX_0('019_quake_1')
    sprite('hz450_19', 6)	# 240-245
    SFX_0('019_quake_0')
    sprite('hz450_20', 6)	# 246-251
    SFX_0('019_quake_1')
    sprite('hz450_21', 6)	# 252-257
    SFX_0('019_quake_0')
    sprite('hz450_22', 6)	# 258-263
    SFX_0('019_quake_1')
    loopRest()
    gotoLabel(1)
    label(2)
    sprite('null', 40)	# 264-303
    Unknown3004(0)
    SFX_0('019_quake_0')
    sprite('null', 40)	# 304-343
    SFX_0('019_quake_0')
    sprite('null', 40)	# 344-383
    tag_voice(0, 'bhz292', 'bhz294', '', '')
    SFX_0('019_quake_0')
    sprite('null', 40)	# 384-423
    SFX_0('019_quake_0')
    sprite('null', 40)	# 424-463
    SFX_3('hzse_07')
    SFX_0('019_quake_0')
    sprite('null', 40)	# 464-503
    SFX_0('019_quake_0')
    sprite('null', 35)	# 504-538
    SFX_3('hzse_03')
    SFX_3('hzse_06')
    SFX_3('hzse_08')
    label(99)
    Unknown11064(3)
    AirHitstunAnimation(10)
    GroundedHitstunAnimation(10)
    AirPushbackY(100000)
    AirPushbackX(0)
    AirUntechableTime(666)
    Damage(42000)
    Unknown11091(100)
    Hitstop(10)
    PushbackX(0)
    Unknown11023(1)
    sprite('hz450_lastatk', 10)	# 539-548	 **attackbox here**
    GFX_0('bhz_AH_ray', -1)
    GFX_0('bhz_AH_ray2', -1)
    sprite('null', 20)	# 549-568
    GFX_0('HZAST_BlackOut', -1)
    Unknown23024(0)
    sprite('null', 78)	# 569-646
    Unknown20001(1)
    loopRest()
    Unknown18010()
    Unknown21011(320)
    Unknown3031()
    Unknown3001(255)
    Unknown1000(0)
    Unknown2019(500)
    Unknown36(22)
    Unknown2005()
    Unknown1084(1)
    Unknown1000(0)
    teleportRelativeX(280000)
    teleportRelativeY(2560000)
    physicsXImpulse(1000)
    Unknown1044()
    Unknown35()
    sprite('hz001_00', 6)	# 647-652
    sprite('hz001_01', 6)	# 653-658
    sprite('hz001_02', 8)	# 659-666
    sprite('hz001_03', 8)	# 667-674
    sprite('hz001_04', 8)	# 675-682
    sprite('hz001_05', 8)	# 683-690
    sprite('hz001_04', 8)	# 691-698
    sprite('hz001_03', 8)	# 699-706
    sprite('hz001_02', 8)	# 707-714
    sprite('hz001_03', 8)	# 715-722
    sprite('hz611_00', 4)	# 723-726
    sprite('hz611_01', 10)	# 727-736
    sprite('hz611_02', 4)	# 737-740
    SFX_0('019_cloth_a')
    sprite('hz611_03', 4)	# 741-744
    sprite('hz611_04', 4)	# 745-748
    sprite('hz611_05', 4)	# 749-752
    sprite('hz611_06', 4)	# 753-756
    sprite('hz611_07', 4)	# 757-760
    sprite('hz611_08', 6)	# 761-766
    SFX_4('bhz522')
    Unknown21011(200)
    loopRest()
    label(100)
    sprite('hz611_09', 6)	# 767-772
    sprite('hz611_10', 6)	# 773-778
    sprite('hz611_11', 6)	# 779-784
    loopRest()
    gotoLabel(100)

@State
def RlAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBOunce_()
        Unknown2017(0)

        def upon_14():
            SFX_1('hz054')
    sprite('hz900_00', 32767)	# 1-32767
    Unknown2017(0)
    Unknown2053(0)
    Unknown2034(0)
    Unknown20001(1)
    Unknown20000(1)
    Unknown20004(1)
    Unknown2007()
    Unknown1000(0)
    teleportRelativeY(0)
    Unknown1084(1)
    GFX_0('RLAstLockmc', 0)
    GFX_0('RLAstLockAura', 0)
    loopRest()

@State
def AmAstralDamage():

    def upon_IMMEDIATE():
        ScriptEndGroundBOunce_()
        Unknown2017(0)
        teleportRelativeY(250000)
    sprite('hz901_00', 50)	# 1-50
    physicsYImpulse(-150)
    sprite('hz901_00', 50)	# 51-100
    physicsYImpulse(150)
    SFX_1('hz055')
    Unknown18003('6135633561356333306135633561356335613563356135633500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    label(0)
    sprite('hz901_00', 50)	# 101-150
    physicsYImpulse(-150)
    sprite('hz901_00', 50)	# 151-200
    physicsYImpulse(150)
    gotoLabel(0)

@Subroutine
def MouthTableInit():
    Unknown18011('bhz000', 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz500', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz501', 12643, 12340, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz502', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 25399, 24887, 25399, 24887, 25399, 12849, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz503', 12643, 12343, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz504', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz505', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz520', 14177, 14179, 12641, 25397, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz521', 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 12899, 24888, 13361, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz522', 14179, 14177, 14179, 14177, 14179, 14177, 13923, 24880, 13617, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz523', 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz524', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14130, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz525', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24885, 25399, 24887, 25399, 24887, 25399, 13618, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz402_0', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz402_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz403_0', 13923, 13921, 13923, 13921, 13923, 14689, 13155, 24885, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz403_1', 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 13411, 24880, 25400, 24888, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601baz', 12643, 14177, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601bny', 12643, 14689, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601bpt', 12643, 12897, 25400, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz600pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25392, 14133, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601pyo', 12643, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz600rbl', 12643, 14177, 14179, 14177, 12643, 24882, 25399, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz600uca', 12643, 14177, 14179, 12641, 25394, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 14131, 14177, 14179, 14177, 14179, 14177, 12643, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25401, 24887, 25401, 24887, 25401, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601ume', 12643, 12641, 25396, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 13619, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz601umi', 14177, 14179, 14177, 14179, 12641, 25400, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz701baz', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25393, 14132, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz701bny', 12643, 14177, 14179, 14177, 12899, 24880, 12849, 14179, 14177, 14179, 14177, 13411, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz700bpt', 12643, 24880, 25399, 12339, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz700pna', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24889, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz701pyo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz700rbl', 12643, 14177, 14179, 12897, 25396, 13365, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz701uca', 12643, 12641, 25394, 24887, 25399, 24889, 25399, 24887, 13873, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz700ugo', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz701ume', 12643, 12897, 25392, 12342, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12850, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('bhz701umi', 14177, 14179, 14177, 14179, 14177, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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
    PartnerChar('bny')
    if SLOT_0:
        _gotolabel(100)
    PartnerChar('baz')
    if SLOT_0:
        _gotolabel(110)
    PartnerChar('pyo')
    if SLOT_0:
        _gotolabel(120)
    PartnerChar('ugo')
    if SLOT_0:
        _gotolabel(130)
    PartnerChar('bpt')
    if SLOT_0:
        _gotolabel(140)
    PartnerChar('rbl')
    if SLOT_0:
        _gotolabel(150)
    PartnerChar('pna')
    if SLOT_0:
        _gotolabel(160)
    PartnerChar('uca')
    if SLOT_0:
        _gotolabel(170)
    PartnerChar('umi')
    if SLOT_0:
        _gotolabel(180)
    PartnerChar('ume')
    if SLOT_0:
        _gotolabel(190)
    label(482)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('hz600_00', 60)	# 2-61
    if SLOT_158:
        Unknown7006('bhz504', 100, 897214562, 12592, 0, 0, 100, 897214562, 12848, 0, 0, 100, 897214562, 13104, 0, 0, 100)
    sprite('hz600_01', 6)	# 62-67
    sprite('hz600_02', 6)	# 68-73
    sprite('hz600_03', 6)	# 74-79
    sprite('hz600_04', 6)	# 80-85
    sprite('hz600_05', 6)	# 86-91
    sprite('hz600_06', 6)	# 92-97
    sprite('hz600_07', 6)	# 98-103
    sprite('hz600_08', 6)	# 104-109
    sprite('hz600_09', 6)	# 110-115
    sprite('hz600_10', 6)	# 116-121
    sprite('hz600_11', 6)	# 122-127
    sprite('hz600_12', 6)	# 128-133
    SFX_0('019_cloth_c')
    sprite('hz600_13', 6)	# 134-139
    sprite('hz600_14', 6)	# 140-145
    sprite('hz600_15', 6)	# 146-151
    sprite('hz600_16', 6)	# 152-157
    sprite('hz600_17', 6)	# 158-163
    sprite('hz600_18', 6)	# 164-169
    sprite('hz600_19', 6)	# 170-175
    Unknown23018(1)
    label(1)
    sprite('hz000_00', 8)	# 176-183
    sprite('hz000_01', 8)	# 184-191
    sprite('hz000_02', 8)	# 192-199
    sprite('hz000_03', 8)	# 200-207
    sprite('hz000_04', 8)	# 208-215
    sprite('hz000_05', 8)	# 216-223
    sprite('hz000_06', 8)	# 224-231
    sprite('hz000_07', 8)	# 232-239
    sprite('hz000_08', 8)	# 240-247
    if SLOT_97:
        _gotolabel(1)
    sprite('hz000_00', 8)	# 248-255
    Unknown21007(24, 41)
    sprite('hz000_01', 8)	# 256-263
    sprite('hz000_02', 8)	# 264-271
    sprite('hz000_03', 8)	# 272-279
    sprite('hz000_04', 8)	# 280-287
    sprite('hz000_05', 8)	# 288-295
    sprite('hz000_06', 8)	# 296-303
    sprite('hz000_07', 8)	# 304-311
    sprite('hz000_08', 8)	# 312-319
    ExitState()
    label(10)
    sprite('hz601_00', 5)	# 320-324
    Unknown7006('bhz505', 100, 897214562, 12336, 0, 0, 100, 897214562, 12848, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('hz601_01', 5)	# 325-329
    sprite('hz601_02', 5)	# 330-334
    sprite('hz601_03', 5)	# 335-339
    sprite('hz601_04', 5)	# 340-344
    sprite('hz601_05', 5)	# 345-349
    sprite('hz601_06', 5)	# 350-354
    sprite('hz601_07', 5)	# 355-359
    sprite('hz601_08', 5)	# 360-364
    sprite('hz601_09', 5)	# 365-369
    sprite('hz601_10', 5)	# 370-374
    sprite('hz601_11', 5)	# 375-379
    label(2)
    sprite('hz601_12', 5)	# 380-384
    if SLOT_97:
        _gotolabel(2)
    sprite('hz601_12', 16)	# 385-400
    sprite('hz601_12', 1)	# 401-401
    label(3)
    sprite('hz601_12', 5)	# 402-406
    if SLOT_97:
        _gotolabel(3)
    sprite('hz601_13', 6)	# 407-412
    Unknown21007(24, 41)
    sprite('hz601_14', 6)	# 413-418
    sprite('hz601_15', 6)	# 419-424
    sprite('hz601_16', 6)	# 425-430
    sprite('hz601_17', 7)	# 431-437
    sprite('hz601_18', 5)	# 438-442
    sprite('hz601_19', 5)	# 443-447
    Unknown21011(60)
    loopRest()
    ExitState()
    label(20)
    sprite('hz000_00', 1)	# 448-448
    SFX_1('bhz701ume')
    label(21)
    sprite('hz000_00', 8)	# 449-456
    sprite('hz000_01', 8)	# 457-464
    sprite('hz000_02', 8)	# 465-472
    sprite('hz000_03', 8)	# 473-480
    sprite('hz000_04', 8)	# 481-488
    sprite('hz000_05', 8)	# 489-496
    sprite('hz000_06', 8)	# 497-504
    sprite('hz000_07', 8)	# 505-512
    sprite('hz000_08', 8)	# 513-520
    gotoLabel(21)
    label(100)
    sprite('hz000_00', 1)	# 521-521
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
        Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('hz000_00', 8)	# 522-529
    sprite('hz000_01', 8)	# 530-537
    sprite('hz000_02', 8)	# 538-545
    sprite('hz000_03', 8)	# 546-553
    sprite('hz000_04', 8)	# 554-561
    sprite('hz000_05', 8)	# 562-569
    sprite('hz000_06', 8)	# 570-577
    sprite('hz000_07', 8)	# 578-585
    sprite('hz000_08', 8)	# 586-593
    gotoLabel(101)
    label(102)
    sprite('hz610_00', 6)	# 594-599
    sprite('hz610_01', 6)	# 600-605
    SFX_1('bhz601bny')
    sprite('hz610_02', 6)	# 606-611
    sprite('hz610_03', 6)	# 612-617
    sprite('hz610_04', 6)	# 618-623
    sprite('hz610_05', 6)	# 624-629
    sprite('hz610_03', 6)	# 630-635
    sprite('hz610_04', 6)	# 636-641
    sprite('hz610_05', 6)	# 642-647
    sprite('hz610_06', 6)	# 648-653
    sprite('hz610_07', 6)	# 654-659
    sprite('hz610_08', 5)	# 660-664
    sprite('hz610_09', 5)	# 665-669
    sprite('hz610_10', 32767)	# 670-33436
    Unknown23018(1)
    ExitState()
    label(110)
    sprite('hz000_00', 1)	# 33437-33437
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('hz000_00', 8)	# 33438-33445
    sprite('hz000_01', 8)	# 33446-33453
    sprite('hz000_02', 8)	# 33454-33461
    sprite('hz000_03', 8)	# 33462-33469
    sprite('hz000_04', 8)	# 33470-33477
    sprite('hz000_05', 8)	# 33478-33485
    sprite('hz000_06', 8)	# 33486-33493
    sprite('hz000_07', 8)	# 33494-33501
    sprite('hz000_08', 8)	# 33502-33509
    gotoLabel(111)
    label(112)
    sprite('hz300_00', 6)	# 33510-33515
    SFX_1('bhz601baz')
    sprite('hz300_01', 6)	# 33516-33521
    sprite('hz300_02', 6)	# 33522-33527
    sprite('hz300_03', 6)	# 33528-33533
    sprite('hz300_04', 6)	# 33534-33539
    sprite('hz300_05', 6)	# 33540-33545
    label(113)
    sprite('hz300_06', 1)	# 33546-33546
    if SLOT_97:
        _gotolabel(113)
    sprite('hz300_06', 30)	# 33547-33576
    sprite('hz300_07', 6)	# 33577-33582
    sprite('hz300_08', 6)	# 33583-33588
    sprite('hz300_09', 6)	# 33589-33594
    Unknown23018(1)
    label(114)
    sprite('hz000_00', 8)	# 33595-33602
    sprite('hz000_01', 8)	# 33603-33610
    sprite('hz000_02', 8)	# 33611-33618
    sprite('hz000_03', 8)	# 33619-33626
    sprite('hz000_04', 8)	# 33627-33634
    sprite('hz000_05', 8)	# 33635-33642
    sprite('hz000_06', 8)	# 33643-33650
    sprite('hz000_07', 8)	# 33651-33658
    sprite('hz000_08', 8)	# 33659-33666
    gotoLabel(114)
    ExitState()
    label(120)
    sprite('hz000_00', 1)	# 33667-33667

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('hz000_00', 8)	# 33668-33675
    sprite('hz000_01', 8)	# 33676-33683
    sprite('hz000_02', 8)	# 33684-33691
    sprite('hz000_03', 8)	# 33692-33699
    sprite('hz000_04', 8)	# 33700-33707
    sprite('hz000_05', 8)	# 33708-33715
    sprite('hz000_06', 8)	# 33716-33723
    sprite('hz000_07', 8)	# 33724-33731
    sprite('hz000_08', 8)	# 33732-33739
    gotoLabel(121)
    label(122)
    sprite('hz615_00', 6)	# 33740-33745
    sprite('hz615_01', 6)	# 33746-33751
    sprite('hz615_02', 6)	# 33752-33757
    sprite('hz615_03', 6)	# 33758-33763
    SFX_1('bhz601pyo')
    sprite('hz615_04', 8)	# 33764-33771
    label(123)
    sprite('hz615_05', 1)	# 33772-33772
    if SLOT_97:
        _gotolabel(123)
    sprite('hz615_05', 30)	# 33773-33802
    sprite('hz615_04', 6)	# 33803-33808
    sprite('hz615_03', 6)	# 33809-33814
    Unknown21007(24, 40)
    sprite('hz615_02', 6)	# 33815-33820
    Unknown21011(300)
    label(124)
    sprite('hz000_00', 8)	# 33821-33828
    sprite('hz000_01', 8)	# 33829-33836
    sprite('hz000_02', 8)	# 33837-33844
    sprite('hz000_03', 8)	# 33845-33852
    sprite('hz000_04', 8)	# 33853-33860
    sprite('hz000_05', 8)	# 33861-33868
    sprite('hz000_06', 8)	# 33869-33876
    sprite('hz000_07', 8)	# 33877-33884
    sprite('hz000_08', 8)	# 33885-33892
    gotoLabel(124)
    ExitState()
    label(130)
    sprite('hz000_00', 1)	# 33893-33893

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('hz000_00', 8)	# 33894-33901
    sprite('hz000_01', 8)	# 33902-33909
    sprite('hz000_02', 8)	# 33910-33917
    sprite('hz000_03', 8)	# 33918-33925
    sprite('hz000_04', 8)	# 33926-33933
    sprite('hz000_05', 8)	# 33934-33941
    sprite('hz000_06', 8)	# 33942-33949
    sprite('hz000_07', 8)	# 33950-33957
    sprite('hz000_08', 8)	# 33958-33965
    gotoLabel(131)
    label(132)
    sprite('hz615_00', 6)	# 33966-33971
    sprite('hz615_01', 6)	# 33972-33977
    sprite('hz615_02', 6)	# 33978-33983
    sprite('hz615_03', 6)	# 33984-33989
    SFX_1('bhz601ugo')
    sprite('hz615_04', 8)	# 33990-33997
    label(133)
    sprite('hz615_05', 1)	# 33998-33998
    if SLOT_97:
        _gotolabel(133)
    sprite('hz615_05', 30)	# 33999-34028
    sprite('hz615_04', 6)	# 34029-34034
    sprite('hz615_03', 6)	# 34035-34040
    sprite('hz615_02', 6)	# 34041-34046
    Unknown23018(1)
    label(134)
    sprite('hz000_00', 8)	# 34047-34054
    sprite('hz000_01', 8)	# 34055-34062
    sprite('hz000_02', 8)	# 34063-34070
    sprite('hz000_03', 8)	# 34071-34078
    sprite('hz000_04', 8)	# 34079-34086
    sprite('hz000_05', 8)	# 34087-34094
    sprite('hz000_06', 8)	# 34095-34102
    sprite('hz000_07', 8)	# 34103-34110
    sprite('hz000_08', 8)	# 34111-34118
    gotoLabel(134)
    ExitState()
    label(140)
    sprite('hz000_00', 1)	# 34119-34119
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1230000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('hz000_00', 8)	# 34120-34127
    sprite('hz000_01', 8)	# 34128-34135
    sprite('hz000_02', 8)	# 34136-34143
    sprite('hz000_03', 8)	# 34144-34151
    sprite('hz000_04', 8)	# 34152-34159
    sprite('hz000_05', 8)	# 34160-34167
    sprite('hz000_06', 8)	# 34168-34175
    sprite('hz000_07', 8)	# 34176-34183
    sprite('hz000_08', 8)	# 34184-34191
    gotoLabel(141)
    label(142)
    sprite('hz615_00', 6)	# 34192-34197
    sprite('hz615_01', 6)	# 34198-34203
    sprite('hz615_02', 6)	# 34204-34209
    sprite('hz615_03', 6)	# 34210-34215
    SFX_1('bhz601bpt')
    sprite('hz615_04', 8)	# 34216-34223
    label(143)
    sprite('hz615_05', 1)	# 34224-34224
    if SLOT_97:
        _gotolabel(143)
    sprite('hz615_05', 30)	# 34225-34254
    sprite('hz615_04', 4)	# 34255-34258
    sprite('hz615_03', 4)	# 34259-34262
    sprite('hz615_02', 4)	# 34263-34266
    Unknown21007(24, 40)
    Unknown23018(1)
    label(144)
    sprite('hz000_00', 8)	# 34267-34274
    sprite('hz000_01', 8)	# 34275-34282
    sprite('hz000_02', 8)	# 34283-34290
    sprite('hz000_03', 8)	# 34291-34298
    sprite('hz000_04', 8)	# 34299-34306
    sprite('hz000_05', 8)	# 34307-34314
    sprite('hz000_06', 8)	# 34315-34322
    sprite('hz000_07', 8)	# 34323-34330
    sprite('hz000_08', 8)	# 34331-34338
    gotoLabel(144)
    ExitState()
    label(150)
    sprite('hz615_00', 6)	# 34339-34344
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('hz615_01', 6)	# 34345-34350
    sprite('hz615_02', 6)	# 34351-34356
    sprite('hz615_03', 6)	# 34357-34362
    SFX_1('bhz600rbl')
    sprite('hz615_04', 8)	# 34363-34370
    label(151)
    sprite('hz615_05', 1)	# 34371-34371
    if SLOT_97:
        _gotolabel(151)
    sprite('hz615_05', 15)	# 34372-34386
    sprite('hz615_05', 15)	# 34387-34401
    Unknown21007(24, 40)
    sprite('hz615_04', 6)	# 34402-34407
    sprite('hz615_03', 6)	# 34408-34413
    sprite('hz615_02', 6)	# 34414-34419
    Unknown21011(240)
    label(152)
    sprite('hz000_00', 8)	# 34420-34427
    sprite('hz000_01', 8)	# 34428-34435
    sprite('hz000_02', 8)	# 34436-34443
    sprite('hz000_03', 8)	# 34444-34451
    sprite('hz000_04', 8)	# 34452-34459
    sprite('hz000_05', 8)	# 34460-34467
    sprite('hz000_06', 8)	# 34468-34475
    sprite('hz000_07', 8)	# 34476-34483
    sprite('hz000_08', 8)	# 34484-34491
    gotoLabel(152)
    ExitState()
    label(160)
    sprite('hz600_00', 60)	# 34492-34551
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    SFX_1('bhz600pna')
    sprite('hz600_01', 6)	# 34552-34557
    sprite('hz600_02', 6)	# 34558-34563
    sprite('hz600_03', 6)	# 34564-34569
    sprite('hz600_04', 6)	# 34570-34575
    sprite('hz600_05', 6)	# 34576-34581
    sprite('hz600_06', 6)	# 34582-34587
    sprite('hz600_07', 6)	# 34588-34593
    sprite('hz600_08', 6)	# 34594-34599
    sprite('hz600_09', 6)	# 34600-34605
    sprite('hz600_10', 6)	# 34606-34611
    sprite('hz600_11', 6)	# 34612-34617
    sprite('hz600_12', 6)	# 34618-34623
    SFX_0('019_cloth_c')
    sprite('hz600_13', 6)	# 34624-34629
    sprite('hz600_14', 6)	# 34630-34635
    sprite('hz600_15', 6)	# 34636-34641
    sprite('hz600_16', 6)	# 34642-34647
    sprite('hz600_17', 6)	# 34648-34653
    sprite('hz600_18', 6)	# 34654-34659
    sprite('hz600_19', 6)	# 34660-34665
    label(161)
    sprite('hz000_00', 8)	# 34666-34673
    sprite('hz000_01', 8)	# 34674-34681
    sprite('hz000_02', 8)	# 34682-34689
    sprite('hz000_03', 8)	# 34690-34697
    sprite('hz000_04', 8)	# 34698-34705
    sprite('hz000_05', 8)	# 34706-34713
    sprite('hz000_06', 8)	# 34714-34721
    sprite('hz000_07', 8)	# 34722-34729
    sprite('hz000_08', 8)	# 34730-34737
    if SLOT_97:
        _gotolabel(161)
    sprite('hz000_00', 1)	# 34738-34738
    Unknown21007(24, 40)
    Unknown21011(360)
    label(162)
    sprite('hz000_00', 8)	# 34739-34746
    sprite('hz000_01', 8)	# 34747-34754
    sprite('hz000_02', 8)	# 34755-34762
    sprite('hz000_03', 8)	# 34763-34770
    sprite('hz000_04', 8)	# 34771-34778
    sprite('hz000_05', 8)	# 34779-34786
    sprite('hz000_06', 8)	# 34787-34794
    sprite('hz000_07', 8)	# 34795-34802
    sprite('hz000_08', 8)	# 34803-34810
    gotoLabel(162)
    ExitState()
    label(170)
    sprite('hz600_00', 10)	# 34811-34820
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)
    sprite('hz600_00', 50)	# 34821-34870
    SFX_1('bhz600uca')
    sprite('hz600_01', 6)	# 34871-34876
    sprite('hz600_02', 6)	# 34877-34882
    sprite('hz600_03', 6)	# 34883-34888
    sprite('hz600_04', 6)	# 34889-34894
    sprite('hz600_05', 6)	# 34895-34900
    sprite('hz600_06', 6)	# 34901-34906
    sprite('hz600_07', 6)	# 34907-34912
    sprite('hz600_08', 6)	# 34913-34918
    sprite('hz600_09', 6)	# 34919-34924
    sprite('hz600_10', 6)	# 34925-34930
    sprite('hz600_11', 6)	# 34931-34936
    sprite('hz600_12', 6)	# 34937-34942
    SFX_0('019_cloth_c')
    sprite('hz600_13', 6)	# 34943-34948
    sprite('hz600_14', 6)	# 34949-34954
    sprite('hz600_15', 6)	# 34955-34960
    sprite('hz600_16', 6)	# 34961-34966
    sprite('hz600_17', 6)	# 34967-34972
    sprite('hz600_18', 6)	# 34973-34978
    sprite('hz600_19', 6)	# 34979-34984
    label(171)
    sprite('hz000_00', 8)	# 34985-34992
    sprite('hz000_01', 8)	# 34993-35000
    sprite('hz000_02', 8)	# 35001-35008
    sprite('hz000_03', 8)	# 35009-35016
    sprite('hz000_04', 8)	# 35017-35024
    sprite('hz000_05', 8)	# 35025-35032
    sprite('hz000_06', 8)	# 35033-35040
    sprite('hz000_07', 8)	# 35041-35048
    sprite('hz000_08', 8)	# 35049-35056
    if SLOT_97:
        _gotolabel(171)
    sprite('hz000_00', 1)	# 35057-35057
    Unknown21007(24, 40)
    Unknown21011(240)
    label(172)
    sprite('hz000_00', 8)	# 35058-35065
    sprite('hz000_01', 8)	# 35066-35073
    sprite('hz000_02', 8)	# 35074-35081
    sprite('hz000_03', 8)	# 35082-35089
    sprite('hz000_04', 8)	# 35090-35097
    sprite('hz000_05', 8)	# 35098-35105
    sprite('hz000_06', 8)	# 35106-35113
    sprite('hz000_07', 8)	# 35114-35121
    sprite('hz000_08', 8)	# 35122-35129
    gotoLabel(172)
    ExitState()
    label(180)
    sprite('hz000_00', 1)	# 35130-35130
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('hz000_00', 8)	# 35131-35138
    sprite('hz000_01', 8)	# 35139-35146
    sprite('hz000_02', 8)	# 35147-35154
    sprite('hz000_03', 8)	# 35155-35162
    sprite('hz000_04', 8)	# 35163-35170
    sprite('hz000_05', 8)	# 35171-35178
    sprite('hz000_06', 8)	# 35179-35186
    sprite('hz000_07', 8)	# 35187-35194
    sprite('hz000_08', 8)	# 35195-35202
    gotoLabel(181)
    label(182)
    sprite('hz300_00', 6)	# 35203-35208
    SFX_1('bhz601umi')
    sprite('hz300_01', 6)	# 35209-35214
    sprite('hz300_02', 6)	# 35215-35220
    sprite('hz300_03', 6)	# 35221-35226
    sprite('hz300_04', 6)	# 35227-35232
    sprite('hz300_05', 6)	# 35233-35238
    label(183)
    sprite('hz300_06', 1)	# 35239-35239
    if SLOT_97:
        _gotolabel(183)
    sprite('hz300_06', 30)	# 35240-35269
    sprite('hz300_07', 6)	# 35270-35275
    sprite('hz300_08', 6)	# 35276-35281
    sprite('hz300_09', 6)	# 35282-35287
    Unknown23018(1)
    label(184)
    sprite('hz000_00', 8)	# 35288-35295
    sprite('hz000_01', 8)	# 35296-35303
    sprite('hz000_02', 8)	# 35304-35311
    sprite('hz000_03', 8)	# 35312-35319
    sprite('hz000_04', 8)	# 35320-35327
    sprite('hz000_05', 8)	# 35328-35335
    sprite('hz000_06', 8)	# 35336-35343
    sprite('hz000_07', 8)	# 35344-35351
    sprite('hz000_08', 8)	# 35352-35359
    gotoLabel(184)
    ExitState()
    label(190)
    sprite('hz000_00', 1)	# 35360-35360
    if SLOT_158:
        Unknown1000(-1230000)
    else:
        Unknown1000(-1465000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('hz000_00', 8)	# 35361-35368
    sprite('hz000_01', 8)	# 35369-35376
    sprite('hz000_02', 8)	# 35377-35384
    sprite('hz000_03', 8)	# 35385-35392
    sprite('hz000_04', 8)	# 35393-35400
    sprite('hz000_05', 8)	# 35401-35408
    sprite('hz000_06', 8)	# 35409-35416
    sprite('hz000_07', 8)	# 35417-35424
    sprite('hz000_08', 8)	# 35425-35432
    gotoLabel(191)
    label(192)
    sprite('hz610_00', 6)	# 35433-35438
    sprite('hz610_01', 6)	# 35439-35444
    SFX_1('bhz601ume')
    sprite('hz610_02', 6)	# 35445-35450
    sprite('hz610_03', 6)	# 35451-35456
    sprite('hz610_04', 6)	# 35457-35462
    sprite('hz610_05', 6)	# 35463-35468
    sprite('hz610_03', 6)	# 35469-35474
    sprite('hz610_04', 6)	# 35475-35480
    sprite('hz610_05', 6)	# 35481-35486
    sprite('hz610_06', 6)	# 35487-35492
    sprite('hz610_07', 6)	# 35493-35498
    sprite('hz610_08', 5)	# 35499-35503
    sprite('hz610_09', 5)	# 35504-35508
    sprite('hz610_10', 32767)	# 35509-68275
    Unknown23018(1)
    ExitState()
    label(991)
    sprite('hz000_00', 1)	# 68276-68276
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('hz000_00', 8)	# 68277-68284
    sprite('hz000_01', 8)	# 68285-68292
    sprite('hz000_02', 8)	# 68293-68300
    sprite('hz000_03', 8)	# 68301-68308
    sprite('hz000_04', 8)	# 68309-68316
    sprite('hz000_05', 8)	# 68317-68324
    sprite('hz000_06', 8)	# 68325-68332
    sprite('hz000_07', 8)	# 68333-68340
    sprite('hz000_08', 8)	# 68341-68348
    gotoLabel(992)
    label(993)
    sprite('hz033_00', 1)	# 68349-68349
    sprite('hz033_01', 2)	# 68350-68351

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
    sprite('hz033_02', 3)	# 68352-68354
    sprite('hz033_03', 3)	# 68355-68357
    loopRest()
    label(994)
    sprite('hz033_03', 3)	# 68358-68360
    sprite('hz033_04', 3)	# 68361-68363
    loopRest()
    gotoLabel(994)
    label(995)
    sprite('null', 3)	# 68364-68366
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
            if PartnerChar('bny'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('pyo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('pna'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bpt'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('baz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('rbl'):
                if (SLOT_145 <= 500000):
                    if (SLOT_29 < 500000):
                        sendToLabel(160)
                        clearUponHandler(3)
                        Unknown36(24)
                        SLOT_53 = 1
                        Unknown35()
            if PartnerChar('uca'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('umi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('ume'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    random_(2, 0, 50)
    if SLOT_0:
        _gotolabel(10)
    sprite('hz610_00', 6)	# 4-9
    sprite('hz610_01', 6)	# 10-15
    sprite('hz610_02', 6)	# 16-21
    sprite('hz610_03', 6)	# 22-27
    sprite('hz610_04', 6)	# 28-33
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bhz524', 100, 897214562, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bhz402_0', 100, 880437346, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bhz521', 100, 897214562, 12850, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('hz610_05', 6)	# 34-39
    sprite('hz610_03', 6)	# 40-45
    sprite('hz610_04', 6)	# 46-51
    sprite('hz610_05', 6)	# 52-57
    sprite('hz610_03', 6)	# 58-63
    sprite('hz610_04', 6)	# 64-69
    sprite('hz610_05', 6)	# 70-75
    sprite('hz610_06', 6)	# 76-81
    sprite('hz610_07', 6)	# 82-87
    sprite('hz610_08', 5)	# 88-92
    sprite('hz610_09', 5)	# 93-97
    sprite('hz610_10', 32767)	# 98-32864
    Unknown23018(1)
    label(10)
    sprite('hz001_00', 6)	# 32865-32870
    if SLOT_158:
        if SLOT_52:
            Unknown7006('bhz524', 100, 897214562, 13618, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('bhz402_0', 100, 880437346, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('bhz521', 100, 897214562, 12850, 0, 0, 100, 897214562, 12338, 0, 0, 100, 0, 0, 0, 0, 0)
    Unknown23018(1)
    sprite('hz001_01', 6)	# 32871-32876
    sprite('hz001_02', 8)	# 32877-32884
    sprite('hz001_03', 8)	# 32885-32892
    sprite('hz001_04', 8)	# 32893-32900
    sprite('hz001_05', 8)	# 32901-32908
    sprite('hz001_04', 8)	# 32909-32916
    sprite('hz001_03', 8)	# 32917-32924
    sprite('hz001_02', 8)	# 32925-32932
    sprite('hz001_03', 8)	# 32933-32940
    sprite('hz611_00', 4)	# 32941-32944
    sprite('hz611_01', 10)	# 32945-32954
    sprite('hz611_02', 4)	# 32955-32958
    SFX_0('019_cloth_a')
    sprite('hz611_03', 4)	# 32959-32962
    sprite('hz611_04', 4)	# 32963-32966
    sprite('hz611_05', 4)	# 32967-32970
    sprite('hz611_06', 4)	# 32971-32974
    sprite('hz611_07', 4)	# 32975-32978
    sprite('hz611_08', 6)	# 32979-32984
    label(2)
    sprite('hz611_09', 6)	# 32985-32990
    sprite('hz611_10', 6)	# 32991-32996
    sprite('hz611_11', 6)	# 32997-33002
    loopRest()
    gotoLabel(2)
    label(100)
    sprite('hz000_00', 1)	# 33003-33003

    def upon_40():
        clearUponHandler(40)
        sendToLabel(102)
    label(101)
    sprite('hz000_00', 8)	# 33004-33011
    sprite('hz000_01', 8)	# 33012-33019
    sprite('hz000_02', 8)	# 33020-33027
    sprite('hz000_03', 8)	# 33028-33035
    sprite('hz000_04', 8)	# 33036-33043
    sprite('hz000_05', 8)	# 33044-33051
    sprite('hz000_06', 8)	# 33052-33059
    sprite('hz000_07', 8)	# 33060-33067
    sprite('hz000_08', 8)	# 33068-33075
    gotoLabel(101)
    label(102)
    sprite('hz610_00', 6)	# 33076-33081
    sprite('hz610_01', 6)	# 33082-33087
    sprite('hz610_02', 6)	# 33088-33093
    sprite('hz610_03', 6)	# 33094-33099
    sprite('hz610_04', 6)	# 33100-33105
    SFX_1('bhz701bny')
    sprite('hz610_05', 6)	# 33106-33111
    sprite('hz610_03', 6)	# 33112-33117
    sprite('hz610_04', 6)	# 33118-33123
    sprite('hz610_05', 6)	# 33124-33129
    sprite('hz610_03', 6)	# 33130-33135
    sprite('hz610_04', 6)	# 33136-33141
    sprite('hz610_05', 6)	# 33142-33147
    sprite('hz610_06', 6)	# 33148-33153
    sprite('hz610_07', 6)	# 33154-33159
    sprite('hz610_08', 5)	# 33160-33164
    sprite('hz610_09', 5)	# 33165-33169
    sprite('hz610_10', 32767)	# 33170-65936
    Unknown23018(1)
    label(110)
    sprite('hz000_00', 1)	# 65937-65937

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('hz000_00', 8)	# 65938-65945
    sprite('hz000_01', 8)	# 65946-65953
    sprite('hz000_02', 8)	# 65954-65961
    sprite('hz000_03', 8)	# 65962-65969
    sprite('hz000_04', 8)	# 65970-65977
    sprite('hz000_05', 8)	# 65978-65985
    sprite('hz000_06', 8)	# 65986-65993
    sprite('hz000_07', 8)	# 65994-66001
    sprite('hz000_08', 8)	# 66002-66009
    gotoLabel(111)
    label(112)
    sprite('hz610_00', 6)	# 66010-66015
    sprite('hz610_01', 6)	# 66016-66021
    sprite('hz610_02', 6)	# 66022-66027
    sprite('hz610_03', 6)	# 66028-66033
    sprite('hz610_04', 6)	# 66034-66039
    SFX_1('bhz701pyo')
    sprite('hz610_05', 6)	# 66040-66045
    sprite('hz610_03', 6)	# 66046-66051
    sprite('hz610_04', 6)	# 66052-66057
    sprite('hz610_05', 6)	# 66058-66063
    sprite('hz610_03', 6)	# 66064-66069
    sprite('hz610_04', 6)	# 66070-66075
    sprite('hz610_05', 6)	# 66076-66081
    sprite('hz610_06', 6)	# 66082-66087
    sprite('hz610_07', 6)	# 66088-66093
    sprite('hz610_08', 5)	# 66094-66098
    sprite('hz610_09', 5)	# 66099-66103
    label(113)
    sprite('hz610_10', 1)	# 66104-66104
    if SLOT_97:
        _gotolabel(113)
    sprite('hz610_10', 30)	# 66105-66134
    sprite('hz610_10', 32767)	# 66135-98901
    Unknown21007(24, 40)
    Unknown21011(150)
    label(120)
    sprite('hz610_00', 6)	# 98902-98907
    sprite('hz610_01', 6)	# 98908-98913
    sprite('hz610_02', 6)	# 98914-98919
    sprite('hz610_03', 6)	# 98920-98925
    sprite('hz610_04', 6)	# 98926-98931
    SFX_1('bhz700pna')
    sprite('hz610_05', 6)	# 98932-98937
    sprite('hz610_03', 6)	# 98938-98943
    sprite('hz610_04', 6)	# 98944-98949
    sprite('hz610_05', 6)	# 98950-98955
    sprite('hz610_03', 6)	# 98956-98961
    sprite('hz610_04', 6)	# 98962-98967
    sprite('hz610_05', 6)	# 98968-98973
    sprite('hz610_06', 6)	# 98974-98979
    sprite('hz610_07', 6)	# 98980-98985
    sprite('hz610_08', 5)	# 98986-98990
    sprite('hz610_09', 5)	# 98991-98995
    label(121)
    sprite('hz610_10', 1)	# 98996-98996
    if SLOT_97:
        _gotolabel(121)
    sprite('hz610_10', 30)	# 98997-99026
    sprite('hz610_10', 32767)	# 99027-131793
    Unknown21007(24, 40)
    Unknown21011(360)
    label(130)
    sprite('hz610_00', 6)	# 131794-131799
    sprite('hz610_01', 6)	# 131800-131805
    sprite('hz610_02', 6)	# 131806-131811
    sprite('hz610_03', 6)	# 131812-131817
    sprite('hz610_04', 6)	# 131818-131823
    SFX_1('bhz700bpt')
    sprite('hz610_05', 6)	# 131824-131829
    sprite('hz610_03', 6)	# 131830-131835
    sprite('hz610_04', 6)	# 131836-131841
    sprite('hz610_05', 6)	# 131842-131847
    sprite('hz610_03', 6)	# 131848-131853
    sprite('hz610_04', 6)	# 131854-131859
    sprite('hz610_05', 6)	# 131860-131865
    sprite('hz610_06', 6)	# 131866-131871
    sprite('hz610_07', 6)	# 131872-131877
    sprite('hz610_08', 5)	# 131878-131882
    sprite('hz610_09', 5)	# 131883-131887
    label(131)
    sprite('hz610_10', 1)	# 131888-131888
    if SLOT_97:
        _gotolabel(131)
    sprite('hz610_10', 30)	# 131889-131918
    sprite('hz610_10', 32767)	# 131919-164685
    Unknown21011(240)
    Unknown21007(24, 40)
    label(140)
    sprite('hz000_00', 1)	# 164686-164686

    def upon_40():
        clearUponHandler(40)
        sendToLabel(142)
    label(141)
    sprite('hz000_00', 8)	# 164687-164694
    sprite('hz000_01', 8)	# 164695-164702
    sprite('hz000_02', 8)	# 164703-164710
    sprite('hz000_03', 8)	# 164711-164718
    sprite('hz000_04', 8)	# 164719-164726
    sprite('hz000_05', 8)	# 164727-164734
    sprite('hz000_06', 8)	# 164735-164742
    sprite('hz000_07', 8)	# 164743-164750
    sprite('hz000_08', 8)	# 164751-164758
    gotoLabel(141)
    label(142)
    sprite('hz001_00', 6)	# 164759-164764
    SFX_1('bhz701baz')
    sprite('hz001_01', 6)	# 164765-164770
    sprite('hz001_02', 8)	# 164771-164778
    sprite('hz001_03', 8)	# 164779-164786
    sprite('hz001_04', 8)	# 164787-164794
    sprite('hz001_05', 8)	# 164795-164802
    sprite('hz001_04', 8)	# 164803-164810
    sprite('hz001_03', 8)	# 164811-164818
    sprite('hz001_02', 8)	# 164819-164826
    sprite('hz001_03', 8)	# 164827-164834
    sprite('hz611_00', 4)	# 164835-164838
    sprite('hz611_01', 10)	# 164839-164848
    sprite('hz611_02', 4)	# 164849-164852
    SFX_0('019_cloth_a')
    sprite('hz611_03', 4)	# 164853-164856
    sprite('hz611_04', 4)	# 164857-164860
    sprite('hz611_05', 4)	# 164861-164864
    sprite('hz611_06', 4)	# 164865-164868
    sprite('hz611_07', 4)	# 164869-164872
    sprite('hz611_08', 6)	# 164873-164878
    Unknown23018(1)
    label(143)
    sprite('hz611_09', 6)	# 164879-164884
    sprite('hz611_10', 6)	# 164885-164890
    sprite('hz611_11', 6)	# 164891-164896
    loopRest()
    gotoLabel(143)
    label(150)
    sprite('hz610_00', 6)	# 164897-164902
    sprite('hz610_01', 6)	# 164903-164908
    sprite('hz610_02', 6)	# 164909-164914
    sprite('hz610_03', 6)	# 164915-164920
    sprite('hz610_04', 6)	# 164921-164926
    SFX_1('bhz700ugo')
    sprite('hz610_05', 6)	# 164927-164932
    sprite('hz610_03', 6)	# 164933-164938
    sprite('hz610_04', 6)	# 164939-164944
    sprite('hz610_05', 6)	# 164945-164950
    sprite('hz610_03', 6)	# 164951-164956
    sprite('hz610_04', 6)	# 164957-164962
    sprite('hz610_05', 6)	# 164963-164968
    sprite('hz610_06', 6)	# 164969-164974
    sprite('hz610_07', 6)	# 164975-164980
    sprite('hz610_08', 5)	# 164981-164985
    sprite('hz610_09', 5)	# 164986-164990
    label(151)
    sprite('hz610_10', 1)	# 164991-164991
    if SLOT_97:
        _gotolabel(151)
    sprite('hz610_10', 32767)	# 164992-197758
    Unknown21007(24, 40)
    Unknown21011(320)
    label(160)

    def upon_3():
        if SLOT_2:
            if (SLOT_29 < 280000):
                Unknown2037(0)
                sendToLabel(162)
    sprite('hz030_00', 7)	# 197759-197765
    physicsXImpulse(5000)
    Unknown2037(1)
    sprite('hz030_01', 7)	# 197766-197772
    label(161)
    sprite('hz030_02', 7)	# 197773-197779
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_03', 7)	# 197780-197786
    sprite('hz030_04', 7)	# 197787-197793
    sprite('hz030_05', 7)	# 197794-197800
    sprite('hz030_06', 7)	# 197801-197807
    sprite('hz030_07', 7)	# 197808-197814
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('hz030_08', 7)	# 197815-197821
    sprite('hz030_09', 7)	# 197822-197828
    sprite('hz030_10', 7)	# 197829-197835
    sprite('hz030_11', 7)	# 197836-197842
    loopRest()
    gotoLabel(161)
    label(162)
    physicsXImpulse(0)
    sprite('hz612_00', 6)	# 197843-197848
    sprite('hz612_01', 6)	# 197849-197854
    sprite('hz612_02', 6)	# 197855-197860
    sprite('hz612_03', 6)	# 197861-197866
    sprite('hz612_04', 8)	# 197867-197874
    sprite('hz612_05', 8)	# 197875-197882
    sprite('hz612_06', 4)	# 197883-197886
    sprite('hz612_07', 6)	# 197887-197892
    SFX_1('bhz700rbl')
    sprite('hz612_08', 6)	# 197893-197898
    sprite('hz612_09', 6)	# 197899-197904
    sprite('hz612_10', 6)	# 197905-197910
    sprite('hz612_11', 5)	# 197911-197915
    sprite('hz612_12', 4)	# 197916-197919
    sprite('hz612_06', 4)	# 197920-197923
    sprite('hz612_07', 6)	# 197924-197929
    sprite('hz612_08', 6)	# 197930-197935
    sprite('hz612_09', 6)	# 197936-197941
    sprite('hz612_10', 6)	# 197942-197947
    sprite('hz612_11', 5)	# 197948-197952
    sprite('hz612_12', 4)	# 197953-197956
    label(163)
    sprite('hz612_06', 4)	# 197957-197960
    sprite('hz612_07', 6)	# 197961-197966
    sprite('hz612_08', 6)	# 197967-197972
    sprite('hz612_09', 6)	# 197973-197978
    sprite('hz612_10', 6)	# 197979-197984
    sprite('hz612_11', 5)	# 197985-197989
    sprite('hz612_12', 4)	# 197990-197993
    if SLOT_97:
        _gotolabel(163)
    sprite('hz612_06', 4)	# 197994-197997
    sprite('hz612_07', 6)	# 197998-198003
    sprite('hz612_08', 6)	# 198004-198009
    sprite('hz612_09', 6)	# 198010-198015
    sprite('hz612_10', 6)	# 198016-198021
    Unknown21007(24, 40)
    Unknown21011(240)
    sprite('hz612_11', 5)	# 198022-198026
    sprite('hz612_12', 4)	# 198027-198030
    label(164)
    sprite('hz612_06', 4)	# 198031-198034
    sprite('hz612_07', 6)	# 198035-198040
    sprite('hz612_08', 6)	# 198041-198046
    sprite('hz612_09', 6)	# 198047-198052
    sprite('hz612_10', 6)	# 198053-198058
    sprite('hz612_11', 5)	# 198059-198063
    sprite('hz612_12', 4)	# 198064-198067
    gotoLabel(164)
    label(170)
    sprite('hz000_00', 1)	# 198068-198068

    def upon_40():
        clearUponHandler(40)
        sendToLabel(172)
    label(171)
    sprite('hz000_00', 8)	# 198069-198076
    sprite('hz000_01', 8)	# 198077-198084
    sprite('hz000_02', 8)	# 198085-198092
    sprite('hz000_03', 8)	# 198093-198100
    sprite('hz000_04', 8)	# 198101-198108
    sprite('hz000_05', 8)	# 198109-198116
    sprite('hz000_06', 8)	# 198117-198124
    sprite('hz000_07', 8)	# 198125-198132
    sprite('hz000_08', 8)	# 198133-198140
    gotoLabel(171)
    label(172)
    sprite('hz610_00', 6)	# 198141-198146
    sprite('hz610_01', 6)	# 198147-198152
    sprite('hz610_02', 6)	# 198153-198158
    sprite('hz610_03', 6)	# 198159-198164
    sprite('hz610_04', 6)	# 198165-198170
    SFX_1('bhz701uca')
    sprite('hz610_05', 6)	# 198171-198176
    sprite('hz610_03', 6)	# 198177-198182
    sprite('hz610_04', 6)	# 198183-198188
    sprite('hz610_05', 6)	# 198189-198194
    sprite('hz610_03', 6)	# 198195-198200
    sprite('hz610_04', 6)	# 198201-198206
    sprite('hz610_05', 6)	# 198207-198212
    sprite('hz610_06', 6)	# 198213-198218
    sprite('hz610_07', 6)	# 198219-198224
    sprite('hz610_08', 5)	# 198225-198229
    sprite('hz610_09', 5)	# 198230-198234
    sprite('hz610_10', 32767)	# 198235-231001
    Unknown23018(1)
    label(180)
    sprite('hz000_00', 1)	# 231002-231002

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('hz000_00', 8)	# 231003-231010
    sprite('hz000_01', 8)	# 231011-231018
    sprite('hz000_02', 8)	# 231019-231026
    sprite('hz000_03', 8)	# 231027-231034
    sprite('hz000_04', 8)	# 231035-231042
    sprite('hz000_05', 8)	# 231043-231050
    sprite('hz000_06', 8)	# 231051-231058
    sprite('hz000_07', 8)	# 231059-231066
    sprite('hz000_08', 8)	# 231067-231074
    gotoLabel(181)
    label(182)
    sprite('hz610_00', 6)	# 231075-231080
    sprite('hz610_01', 6)	# 231081-231086
    sprite('hz610_02', 6)	# 231087-231092
    sprite('hz610_03', 6)	# 231093-231098
    sprite('hz610_04', 6)	# 231099-231104
    sprite('hz610_05', 6)	# 231105-231110
    sprite('hz610_06', 6)	# 231111-231116
    sprite('hz610_07', 6)	# 231117-231122
    SFX_1('bhz701umi')
    Unknown21011(240)
    sprite('hz610_08', 5)	# 231123-231127
    sprite('hz610_09', 5)	# 231128-231132
    sprite('hz610_10', 32767)	# 231133-263899
    label(190)
    sprite('hz000_00', 1)	# 263900-263900

    def upon_40():
        clearUponHandler(40)
        sendToLabel(192)
    label(191)
    sprite('hz000_00', 8)	# 263901-263908
    sprite('hz000_01', 8)	# 263909-263916
    sprite('hz000_02', 8)	# 263917-263924
    sprite('hz000_03', 8)	# 263925-263932
    sprite('hz000_04', 8)	# 263933-263940
    sprite('hz000_05', 8)	# 263941-263948
    sprite('hz000_06', 8)	# 263949-263956
    sprite('hz000_07', 8)	# 263957-263964
    sprite('hz000_08', 8)	# 263965-263972
    gotoLabel(191)
    label(192)
    sprite('hz001_00', 6)	# 263973-263978
    SFX_1('bhz701ume')
    sprite('hz001_01', 6)	# 263979-263984
    sprite('hz001_02', 8)	# 263985-263992
    sprite('hz001_03', 8)	# 263993-264000
    sprite('hz001_04', 8)	# 264001-264008
    sprite('hz001_05', 8)	# 264009-264016
    sprite('hz001_04', 8)	# 264017-264024
    sprite('hz001_03', 8)	# 264025-264032
    sprite('hz001_02', 8)	# 264033-264040
    sprite('hz001_03', 8)	# 264041-264048
    sprite('hz611_00', 4)	# 264049-264052
    sprite('hz611_01', 10)	# 264053-264062
    sprite('hz611_02', 4)	# 264063-264066
    SFX_0('019_cloth_a')
    sprite('hz611_03', 4)	# 264067-264070
    sprite('hz611_04', 4)	# 264071-264074
    sprite('hz611_05', 4)	# 264075-264078
    sprite('hz611_06', 4)	# 264079-264082
    sprite('hz611_07', 4)	# 264083-264086
    sprite('hz611_08', 6)	# 264087-264092
    Unknown23018(1)
    label(193)
    sprite('hz611_09', 6)	# 264093-264098
    sprite('hz611_10', 6)	# 264099-264104
    sprite('hz611_11', 6)	# 264105-264110
    loopRest()
    gotoLabel(193)

@State
def CmnActLose():
    sprite('hz620_00', 7)	# 1-7
    if SLOT_158:
        Unknown7006('bhz403_0', 100, 880437346, 828322608, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sprite('hz620_01', 7)	# 8-14
    sprite('hz620_02', 7)	# 15-21
    sprite('hz620_03', 4)	# 22-25
    sprite('hz620_04', 4)	# 26-29
    sprite('hz620_05', 4)	# 30-33
    sprite('hz620_06', 7)	# 34-40
    sprite('hz620_07', 7)	# 41-47
    sprite('hz620_08', 7)	# 48-54
    Unknown23018(1)
    label(0)
    sprite('hz620_02', 7)	# 55-61
    sprite('hz620_03', 4)	# 62-65
    sprite('hz620_04', 4)	# 66-69
    sprite('hz620_05', 4)	# 70-73
    sprite('hz620_06', 7)	# 74-80
    sprite('hz620_07', 7)	# 81-87
    sprite('hz620_08', 7)	# 88-94
    loopRest()
    gotoLabel(0)