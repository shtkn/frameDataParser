@Subroutine
def ExSkillInit():
    MinimumDamagePct(10)
    Unknown30065(0)

@Subroutine
def InvSkillInit():
    Unknown30065(100)

@Subroutine
def PartnerSkillInit():
    AttackP1(70)
    Unknown11042(1)

@Subroutine
def PreInit():
    Unknown12019('70616400000000000000000000000000')

@Subroutine
def MatchInit():
    AirBDashDuration(13)
    Unknown12037(-1800)
    Unknown12024(1)
    Unknown13039(1)
    Unknown2049(1)
    Unknown30093(1, 5, 34, 0, 0)
    Unknown3060('0000000076725f6c61796572310000000000000000000000000000000000000000000000')
    Unknown3061(0, 5)
    Unknown3063(0, 65000)
    Unknown3062(0, 100000)
    Move_Register('AutoFDash', 0x0)
    Unknown14009(6)
    Move_AirGround_(0x2000)
    Move_Input_(0x78)
    Unknown14013('CmnActFDash')
    Move_EndRegister()
    Move_Register('NmlAtk5A', 0x7)
    MoveMaxChainRepeat(3)
    Unknown15013(2000)
    Unknown14015(0, 450000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5AAAA', 0x7)
    Unknown14005(1)
    Unknown14015(0, 450000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4A', 0x6)
    MoveMaxChainRepeat(3)
    Unknown14015(0, 300000, -200000, 200000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk4AA', 0x6)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4AAA', 0x6)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk4AAAA', 0x6)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtk2A', 0x4)
    Unknown14027('NmlAtk4A')
    MoveMaxChainRepeat(3)
    Unknown15009()
    Unknown14015(0, 350000, -100000, 150000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkChain2A', 0x4)
    Unknown14005(1)
    Unknown14027('NmlAtk4A')
    Move_EndRegister()
    Move_Register('NmlAtk5B', 0x19)
    MoveMaxChainRepeat(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 500000, -200000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BB', 0x19)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 650000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk5BBB', 0x19)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 600000, -200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2B', 0x16)
    MoveMaxChainRepeat(1)
    Unknown14015(0, 350000, 200000, 400000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtk2BB', 0x1f)
    Unknown14005(1)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_EndRegister()
    Move_Register('CmnActCrushAttack', 0x66)
    Unknown15008()
    Unknown14015(0, 500000, -200000, 200000, 350, 25)
    Move_EndRegister()
    Move_Register('NmlAtk2C', 0x28)
    Unknown15009()
    Unknown14015(0, 500000, -100000, 150000, 500, 50)
    Move_EndRegister()
    Move_Register('CmnActChangePartnerQuickOut', 0x63)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5A', 0x10)
    Unknown14015(0, 350000, -150000, 250000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5AA', 0x10)
    Unknown14005(1)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5B', 0x22)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 500000, -350000, 50000, 1000, 50)
    Move_EndRegister()
    Move_Register('NmlAtkAIR5C', 0x34)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Unknown14015(0, 500000, 50000, 450000, 500, 25)
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
    Move_Register('SpecialShotFastLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15021(1)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1500)
    Unknown15011(10000)
    Unknown14015(800000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('SpecialShotSlowLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15021(1)
    Unknown15014(1)
    Unknown15012(1500)
    Unknown15011(10000)
    Unknown14015(800000, 1200000, -200000, 200000, 100, 5)
    Move_EndRegister()
    Move_Register('SpecialSearchShotLand', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(1)
    Unknown14015(800000, 1200000, -200000, 200000, 100, 5)
    Move_EndRegister()
    Move_Register('SpecialAntiAirFast', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_A)
    Unknown14015(0, 450000, -200000, 200000, 500, 25)
    Move_EndRegister()
    Move_Register('SpecialAntiAirSlow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15013(2000)
    Unknown15027(2000)
    Unknown14015(-400000, 400000, -200000, 200000, 100, 0)
    Move_EndRegister()
    Move_Register('SpecialThrow', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_214)
    Move_Input_(INPUT_PRESS_C)
    Unknown15010()
    Unknown14015(0, 400000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('SpecialShotFastAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_A)
    Unknown15014(1)
    Unknown15013(1)
    Unknown15012(1500)
    Unknown14015(800000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('SpecialShotSlowAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_B)
    Unknown15014(1)
    Unknown15012(1500)
    Unknown14015(800000, 1200000, -200000, 200000, 250, 10)
    Move_EndRegister()
    Move_Register('SpecialSearchShotAir', INPUT_SPECIALMOVE)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3086)
    Move_Input_(INPUT_236)
    Move_Input_(INPUT_PRESS_C)
    Unknown15014(2000)
    Unknown14015(400000, 1200000, -600000, 200000, 100, 5)
    Move_EndRegister()
    Move_Register('CmnActInvincibleAttack', 0x64)
    Unknown15006(0)
    Unknown15013(0)
    Unknown15012(0)
    Unknown15014(6000)
    Unknown15020(500, 1000, 100, 1000)
    Unknown14015(0, 400000, -200000, 200000, 250, 5)
    Move_EndRegister()
    Move_Register('UltimateAsasultLand', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(650000, 1400000, -200000, 400000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateAsasultLandSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15021(1)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(650000, 1400000, -200000, 400000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateAsasultAir', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(150000, 650000, -500000, 100000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateAsasultAirSP', 0x68)
    Move_AirGround_(0x2001)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_236)
    Move_Input_(0xde)
    Unknown15013(1)
    Unknown15012(1)
    Unknown15014(3000)
    Unknown14015(150000, 650000, -500000, 100000, 100, 0)
    Move_EndRegister()
    Move_Register('UltimateBlade', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3089)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(4000)
    Unknown14015(0, 550000, -200000, 200000, 150, 5)
    Move_EndRegister()
    Move_Register('UltimateBladeSP', 0x68)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x3089)
    Move_AirGround_(0x3081)
    Move_Input_(INPUT_214)
    Move_Input_(0xde)
    Unknown15012(1)
    Unknown15014(4000)
    Unknown14015(0, 550000, -200000, 200000, 150, 5)
    Move_EndRegister()
    Move_Register('AstralHeat', 0x69)
    Move_AirGround_(0x2000)
    Move_AirGround_(0x3083)
    Move_AirGround_(0x300e)
    Move_AirGround_(0x304a)
    Move_Input_(0xcd)
    Move_Input_(0xde)
    Unknown15014(3000)
    Unknown15013(3000)
    Unknown14015(-350000, 850000, -200000, 100000, 1000, 50)
    Move_EndRegister()
    Unknown15024('NmlAtk5A', 'NmlAtk5AA', 10000000)
    Unknown15024('NmlAtk5AA', 'NmlAtk5AAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5AAAA', 10000000)
    Unknown15024('NmlAtk5AAA', 'NmlAtk5B', 10000000)
    Unknown15024('NmlAtk4A', 'NmlAtk4AA', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk4AAA', 10000000)
    Unknown15024('NmlAtk4AA', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk4AAA', 'NmlAtk4AAAA', 10000000)
    Unknown15024('NmlAtk5B', 'NmlAtk5BB', 10000000)
    Unknown15024('NmlAtk5BB', 'NmlAtk5BBB', 10000000)
    Unknown15024('NmlAtk5BBB', 'NmlAtk2C', 10000000)
    Unknown15024('NmlAtk5BBB', 'SpecialAntiAirFast', 10000000)
    Unknown15024('NmlAtk5BBB', 'SpecialAntiAirSlow', 10000000)
    Unknown15024('NmlAtk5BBB', 'SpecialShotSlowLand', 10000000)
    Unknown15024('NmlAtk2A', 'NmlAtk5A', 10000000)
    Unknown15024('NmlAtk2B', 'NmlAtk2BB', 10000000)
    Unknown15024('NmlAtk2B', 'FJump', 10000000)
    Unknown15024('NmlAtkAIR5A', 'NmlAtkAIR5AA', 10000000)
    Unknown15024('NmlAtkAIR5AA', 'NmlAtkAIR5C', 10000000)
    Unknown12018(0, 'ad060_00')
    Unknown12018(1, 'ad060_01')
    Unknown12018(2, 'ad060_02')
    Unknown12018(3, 'ad060_03')
    Unknown12018(4, 'ad060_04')
    Unknown12018(5, 'ad060_05')
    Unknown12018(6, 'ad060_06')
    Unknown12018(7, 'ad040_02')
    Unknown12018(8, 'ad040_02')
    Unknown12018(9, 'ad045_02')
    Unknown12018(10, 'ad060_00')
    Unknown12018(11, 'ad060_01')
    Unknown12018(12, 'ad060_03')
    Unknown12018(13, 'ad060_05')
    Unknown12018(14, 'ad060_07')
    Unknown12018(15, 'ad125_00')
    Unknown12018(16, 'ad050_00')
    Unknown12018(17, 'ad052_00')
    Unknown12018(18, 'ad054_00')
    Unknown12018(19, 'ad000_00')
    Unknown12018(20, 'ad000_00')
    Unknown12018(25, 'ad063_00')
    Unknown12018(26, 'ad063_01')
    Unknown12018(27, 'ad063_02')
    Unknown12018(28, 'ad063_05')
    Unknown12018(29, 'ad060_12')
    Unknown12018(24, 'ad072_03')
    Unknown7010(0, 'pad000')
    Unknown7010(1, 'pad001')
    Unknown7010(2, 'pad002')
    Unknown7010(3, 'pad003')
    Unknown7010(4, 'pad004')
    Unknown7010(5, 'pad005')
    Unknown7010(6, 'pad006')
    Unknown7010(7, 'pad007')
    Unknown7010(8, 'pad008')
    Unknown7010(9, 'pad009')
    Unknown7010(10, 'pad010')
    Unknown7010(15, 'pad015')
    Unknown7010(16, 'pad016')
    Unknown7010(17, 'pad017')
    Unknown7010(18, 'pad018')
    Unknown7010(19, 'pad019')
    Unknown7010(20, 'pad020')
    Unknown7010(21, 'pad021')
    Unknown7010(22, 'pad022')
    Unknown7010(23, 'pad023')
    Unknown7010(24, 'pad024')
    Unknown7010(25, 'pad025')
    Unknown7010(28, 'pad028')
    Unknown7010(29, 'pad029')
    Unknown7010(30, 'pad030')
    Unknown7010(31, 'pad031')
    Unknown7010(32, 'pad032')
    Unknown7010(33, 'pad033')
    Unknown7010(34, 'pad034')
    Unknown7010(35, 'pad035')
    Unknown7010(36, 'pad036')
    Unknown7010(37, 'pad037')
    Unknown7010(39, 'pad039')
    Unknown7010(42, 'pad042')
    Unknown7010(43, 'pad043')
    Unknown7010(44, 'pad044')
    Unknown7010(45, 'pad045')
    Unknown7010(46, 'pad046')
    Unknown7010(47, 'pad047')
    Unknown7010(48, 'pad048')
    Unknown7010(49, 'pad049')
    Unknown7010(50, 'pad050')
    Unknown7010(52, 'pad052')
    Unknown7010(53, 'pad053')
    Unknown7010(54, 'pad100_0')
    Unknown7010(55, 'pad100_1')
    Unknown7010(56, 'pad100_2')
    Unknown7010(63, 'pad101_0')
    Unknown7010(64, 'pad101_1')
    Unknown7010(65, 'pad101_2')
    Unknown7010(57, 'pad102_0')
    Unknown7010(58, 'pad102_1')
    Unknown7010(59, 'pad102_2')
    Unknown7010(66, 'pad103_0')
    Unknown7010(67, 'pad103_1')
    Unknown7010(68, 'pad103_2')
    Unknown7010(60, 'pad104_0')
    Unknown7010(61, 'pad104_1')
    Unknown7010(62, 'pad104_2')
    Unknown7010(69, 'pad105_0')
    Unknown7010(70, 'pad105_1')
    Unknown7010(71, 'pad105_2')
    Unknown7010(72, 'pad150')
    Unknown7010(73, 'pad151')
    Unknown7010(74, 'pad152')
    Unknown7010(85, 'pad153')
    Unknown7010(87, 'pad154')
    Unknown7010(88, 'pad155')
    Unknown7010(96, 'pad161_0')
    Unknown7010(97, 'pad161_1')
    Unknown7010(92, 'pad162_0')
    Unknown7010(93, 'pad162_1')
    Unknown7010(98, 'pad163_0')
    Unknown7010(99, 'pad163_1')
    Unknown7010(100, 'pad164_0')
    Unknown7010(101, 'pad164_1')
    Unknown7010(105, 'pad165_0')
    Unknown7010(106, 'pad165_1')
    Unknown7010(102, 'pad166_0')
    Unknown7010(103, 'pad166_1')
    Unknown7010(90, 'pad167_0')
    Unknown7010(91, 'pad167_1')
    Unknown7010(107, 'pad168_0')
    Unknown7010(108, 'pad168_1')
    Unknown7010(110, 'pad169_0')
    Unknown7010(111, 'pad169_1')
    Unknown7010(112, 'pad159_0')
    Unknown7010(113, 'pad159_1')
    Unknown7010(94, 'pad400_0')
    Unknown7010(95, 'pad400_1')
    Unknown12059('00000000436d6e416374496e76696e6369626c6541747461636b00000000000000000000')
    Unknown12059('010000004e6d6c41746b3441000000000000000000000000000000000000000000000000')
    Unknown12059('02000000556c74696d61746541736173756c744c616e6400000000000000000000000000')
    Unknown12059('03000000556c74696d61746541736173756c744c616e6453500000000000000000000000')
    Unknown12059('04000000556c74696d617465426c61646500000000000000000000000000000000000000')
    Unknown12059('05000000556c74696d617465426c61646553500000000000000000000000000000000000')
    Unknown12059('06000000436d6e4163744244617368000000000000000000000000000000000000000000')
    Unknown12059('070000004e6d6c41746b5468726f77000000000000000000000000000000000000000000')
    Unknown12059('08000000436d6e4163744368616e6765506172746e6572517569636b4f75740000000000')
    Unknown23003(0, 1, 31, 1, 1, 0, -1, -1)
    Unknown23004(0, 1)
    Unknown23044(0, 1)
    Unknown30036('5041445f506572736f6e61437265617465000000000000000000000000000000ffffffff')
    Unknown38(11, 1)

@Subroutine
def MatchInit2():
    callSubroutine('CheckPowerUpTraining')

@Subroutine
def CheckPowerUpTraining():
    if SLOT_IsPlayer2:
        Unknown58('TRI_PADPowerUp', 2, 67)
        if (SLOT_67 == 1):
            SLOT_31 = 1

@Subroutine
def OnFrameStep():
    if (not SLOT_81):
        if SLOT_90:
            Unknown58('TRI_PADPowerUp', 2, 67)
            if (SLOT_67 == 1):
                SLOT_31 = 1
                if (not Unknown46(5)):
                    Unknown13(5)
                    GFX_0('PowerUpAura', 100)
                    Unknown38(5, 1)
            if (SLOT_67 == 2):
                SLOT_31 = 0
                if Unknown46(5):
                    Unknown13(5)
    if (not SLOT_21):
        if SLOT_31:
            SLOT_31 = 0
        if Unknown46(5):
            Unknown13(5)

@Subroutine
def OnDamage():
    if SLOT_31:
        SLOT_31 = 0

@Subroutine
def OnActionBeginPre():
    SLOT_4 = 0

@Subroutine
def OnActionBegin():
    SLOT_78 = 100
    if SLOT_31:
        if (not SLOT_4):
            SLOT_78 = 110
        if (not Unknown46(5)):
            Unknown13(5)
            GFX_0('PowerUpAura', 100)
            Unknown38(5, 1)
            if Unknown23148('CmnActTagBattleWait'):
                Unknown13(5)

@State
def CmnActStand():
    label(0)
    sprite('ad000_00', 9)	# 1-9
    sprite('ad000_01', 9)	# 10-18
    sprite('ad000_02', 9)	# 19-27
    sprite('ad000_03', 9)	# 28-36
    sprite('ad000_04', 9)	# 37-45
    sprite('ad000_05', 9)	# 46-54
    sprite('ad000_06', 9)	# 55-63
    sprite('ad000_07', 9)	# 64-72
    loopRest()
    random_(1, 2, 87)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(0, 2, 123)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(0, 2, 122)
    if SLOT_ReturnVal:
        _gotolabel(0)
    random_(2, 0, 90)
    if SLOT_ReturnVal:
        _gotolabel(0)
    sprite('ad001_00', 9)	# 73-81
    SLOT_88 = 960
    SFX_1('pad000')
    sprite('ad001_01', 9)	# 82-90
    sprite('ad001_02', 9)	# 91-99
    sprite('ad001_03', 12)	# 100-111
    sprite('ad001_04', 12)	# 112-123
    sprite('ad001_03', 12)	# 124-135
    sprite('ad001_02', 12)	# 136-147
    sprite('ad001_03', 12)	# 148-159
    sprite('ad001_04', 12)	# 160-171
    sprite('ad001_03', 12)	# 172-183
    sprite('ad001_02', 12)	# 184-195
    sprite('ad001_03', 12)	# 196-207
    sprite('ad001_04', 12)	# 208-219
    sprite('ad001_03', 12)	# 220-231
    sprite('ad001_02', 12)	# 232-243
    sprite('ad001_01', 9)	# 244-252
    sprite('ad001_00', 9)	# 253-261
    loopRest()
    gotoLabel(0)

@State
def CmnActStandTurn():
    sprite('ad003_00', 4)	# 1-4
    sprite('ad003_01', 4)	# 5-8
    sprite('ad003_02', 4)	# 9-12

@State
def CmnActStand2Crouch():
    sprite('ad010_00', 4)	# 1-4
    sprite('ad010_01', 4)	# 5-8

@State
def CmnActCrouch():
    label(0)
    sprite('ad010_02', 6)	# 1-6
    sprite('ad010_03', 6)	# 7-12
    sprite('ad010_04', 6)	# 13-18
    sprite('ad010_05', 6)	# 19-24
    sprite('ad010_06', 6)	# 25-30
    sprite('ad010_07', 6)	# 31-36
    sprite('ad010_08', 6)	# 37-42
    sprite('ad010_09', 6)	# 43-48
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchTurn():
    sprite('ad013_00', 4)	# 1-4
    sprite('ad013_01', 4)	# 5-8
    sprite('ad013_02', 4)	# 9-12

@State
def CmnActCrouch2Stand():
    sprite('ad010_01', 4)	# 1-4
    sprite('ad010_00', 4)	# 5-8

@State
def CmnActJumpPre():
    sprite('ad010_00', 4)	# 1-4

@State
def CmnActJumpUpper():
    label(0)
    sprite('ad020_00', 4)	# 1-4
    sprite('ad020_01', 4)	# 5-8
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpUpperEnd():
    sprite('ad020_02', 3)	# 1-3
    sprite('ad020_03', 3)	# 4-6
    sprite('ad020_04', 3)	# 7-9

@State
def CmnActJumpDown():
    sprite('ad020_05', 3)	# 1-3
    sprite('ad020_06', 3)	# 4-6
    label(0)
    sprite('ad020_07', 4)	# 7-10
    sprite('ad020_08', 4)	# 11-14
    loopRest()
    gotoLabel(0)

@State
def CmnActJumpLanding():
    sprite('ad010_01', 3)	# 1-3
    sprite('ad010_00', 3)	# 4-6

@State
def CmnActLandingStiffLoop():
    sprite('ad211_08', 2)	# 1-2
    sprite('ad211_08', 32767)	# 3-32769
    loopRest()

@State
def CmnActLandingStiffEnd():
    sprite('ad010_02', 2)	# 1-2
    sprite('ad010_03', 2)	# 3-4
    sprite('ad010_04', 2)	# 5-6

@State
def CmnActFWalk():
    sprite('null', 60)	# 1-60

@State
def CmnActBWalk():
    sprite('ad031_00', 3)	# 1-3
    sprite('ad031_01', 3)	# 4-6
    label(0)
    sprite('ad031_02', 6)	# 7-12
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ad031_03', 6)	# 13-18
    sprite('ad031_04', 6)	# 19-24
    sprite('ad031_05', 6)	# 25-30
    sprite('ad031_06', 6)	# 31-36
    sprite('ad031_07', 6)	# 37-42
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ad031_08', 6)	# 43-48
    sprite('ad031_09', 6)	# 49-54
    sprite('ad031_10', 6)	# 55-60
    sprite('ad031_11', 6)	# 61-66
    loopRest()
    gotoLabel(0)

@State
def CmnActFDash():
    sprite('ad030_00', 4)	# 1-4
    sprite('ad032_00', 2)	# 5-6
    label(0)
    sprite('ad032_01', 4)	# 7-10
    sprite('ad032_02', 4)	# 11-14
    sprite('ad032_03', 4)	# 15-18
    Unknown8006(100, 1, 1)
    sprite('ad032_04', 4)	# 19-22
    sprite('ad032_05', 4)	# 23-26
    sprite('ad032_06', 4)	# 27-30
    sprite('ad032_07', 4)	# 31-34
    Unknown8006(100, 1, 1)
    sprite('ad032_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActFDashStop():
    sprite('ad032_09', 7)	# 1-7
    sprite('ad032_10', 5)	# 8-12

@State
def CmnActBDash():

    def upon_IMMEDIATE():
        Unknown2042(1)
        setInvincibleFor(7)
        Unknown1084(1)
        Unknown23001(100, 0)
        Unknown23076()
        sendToLabelUpon(2, 1)
        Unknown28(8, '_NEUTRAL')
    sprite('ad033_00', 2)	# 1-2
    sprite('ad033_01', 3)	# 3-5
    physicsXImpulse(-18000)
    physicsYImpulse(8800)
    setGravity(1550)
    Unknown8002()
    sprite('ad033_02', 3)	# 6-8
    label(0)
    sprite('ad033_01', 3)	# 9-11
    sprite('ad033_02', 3)	# 12-14
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad033_03', 3)	# 15-17
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ad033_04', 3)	# 18-20

@State
def CmnActBDashLanding():
    sprite('null', 60)	# 1-60

@State
def CmnActAirFDash():
    sprite('ad035_00', 3)	# 1-3
    label(0)
    sprite('ad035_01', 3)	# 4-6
    sprite('ad035_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirBDash():
    sprite('ad033_01', 3)	# 1-3
    physicsYImpulse(12000)
    sprite('ad033_02', 3)	# 4-6
    sprite('ad033_01', 3)	# 7-9
    sprite('ad033_02', 3)	# 10-12
    sprite('ad033_01', 3)	# 13-15
    sprite('ad033_02', 3)	# 16-18
    sprite('ad033_01', 3)	# 19-21
    sprite('ad033_02', 3)	# 22-24
    sprite('ad020_05', 3)	# 25-27
    sprite('ad020_06', 3)	# 28-30
    label(0)
    sprite('ad020_07', 4)	# 31-34
    sprite('ad020_08', 4)	# 35-38
    loopRest()
    gotoLabel(0)

@State
def CmnActHitStandLv1():
    sprite('ad050_00', 1)	# 1-1
    sprite('ad050_01', 1)	# 2-2
    sprite('ad050_00', 2)	# 3-4

@State
def CmnActHitStandLv2():
    sprite('ad050_01', 1)	# 1-1
    sprite('ad050_02', 1)	# 2-2
    sprite('ad050_01', 2)	# 3-4
    sprite('ad050_00', 2)	# 5-6

@State
def CmnActHitStandLv3():
    sprite('ad050_02', 1)	# 1-1
    sprite('ad050_03', 1)	# 2-2
    sprite('ad050_02', 2)	# 3-4
    sprite('ad050_01', 2)	# 5-6
    sprite('ad050_00', 2)	# 7-8

@State
def CmnActHitStandLv4():
    sprite('ad050_03', 1)	# 1-1
    sprite('ad050_04', 1)	# 2-2
    sprite('ad050_03', 2)	# 3-4
    sprite('ad050_02', 2)	# 5-6
    sprite('ad050_01', 2)	# 7-8
    sprite('ad050_00', 2)	# 9-10

@State
def CmnActHitStandLv5():
    sprite('ad050_04', 1)	# 1-1
    sprite('ad050_04', 1)	# 2-2
    sprite('ad050_04', 2)	# 3-4
    sprite('ad050_03', 2)	# 5-6
    sprite('ad050_02', 2)	# 7-8
    sprite('ad050_01', 2)	# 9-10
    sprite('ad050_00', 2)	# 11-12

@State
def CmnActHitStandLowLv1():
    sprite('ad052_00', 1)	# 1-1
    sprite('ad052_01', 1)	# 2-2
    sprite('ad052_00', 2)	# 3-4

@State
def CmnActHitStandLowLv2():
    sprite('ad052_01', 1)	# 1-1
    sprite('ad052_02', 1)	# 2-2
    sprite('ad052_01', 2)	# 3-4
    sprite('ad052_00', 2)	# 5-6

@State
def CmnActHitStandLowLv3():
    sprite('ad052_02', 1)	# 1-1
    sprite('ad052_03', 1)	# 2-2
    sprite('ad052_02', 2)	# 3-4
    sprite('ad052_01', 2)	# 5-6
    sprite('ad052_00', 2)	# 7-8

@State
def CmnActHitStandLowLv4():
    sprite('ad052_03', 1)	# 1-1
    sprite('ad052_04', 1)	# 2-2
    sprite('ad052_03', 2)	# 3-4
    sprite('ad052_02', 2)	# 5-6
    sprite('ad052_01', 2)	# 7-8
    sprite('ad052_00', 2)	# 9-10

@State
def CmnActHitStandLowLv5():
    sprite('ad052_04', 1)	# 1-1
    sprite('ad052_04', 1)	# 2-2
    sprite('ad052_04', 2)	# 3-4
    sprite('ad052_03', 2)	# 5-6
    sprite('ad052_02', 2)	# 7-8
    sprite('ad052_01', 2)	# 9-10
    sprite('ad052_00', 2)	# 11-12

@State
def CmnActHitCrouchLv1():
    sprite('ad054_00', 1)	# 1-1
    sprite('ad054_01', 1)	# 2-2
    sprite('ad054_00', 2)	# 3-4

@State
def CmnActHitCrouchLv2():
    sprite('ad054_01', 1)	# 1-1
    sprite('ad054_02', 1)	# 2-2
    sprite('ad054_01', 2)	# 3-4
    sprite('ad054_00', 2)	# 5-6

@State
def CmnActHitCrouchLv3():
    sprite('ad054_02', 1)	# 1-1
    sprite('ad054_03', 1)	# 2-2
    sprite('ad054_02', 2)	# 3-4
    sprite('ad054_01', 2)	# 5-6
    sprite('ad054_00', 2)	# 7-8

@State
def CmnActHitCrouchLv4():
    sprite('ad054_03', 1)	# 1-1
    sprite('ad054_04', 1)	# 2-2
    sprite('ad054_03', 2)	# 3-4
    sprite('ad054_02', 2)	# 5-6
    sprite('ad054_01', 2)	# 7-8
    sprite('ad054_00', 2)	# 9-10

@State
def CmnActHitCrouchLv5():
    sprite('ad054_04', 1)	# 1-1
    sprite('ad054_04', 1)	# 2-2
    sprite('ad054_04', 2)	# 3-4
    sprite('ad054_03', 2)	# 5-6
    sprite('ad054_02', 2)	# 7-8
    sprite('ad054_01', 2)	# 9-10
    sprite('ad054_00', 2)	# 11-12

@State
def CmnActBDownUpper():
    sprite('ad060_00', 4)	# 1-4
    label(0)
    sprite('ad060_01', 4)	# 5-8
    sprite('ad060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownUpperEnd():
    sprite('ad060_03', 4)	# 1-4

@State
def CmnActBDownDown():
    sprite('ad060_04', 8)	# 1-8
    label(0)
    sprite('ad060_05', 4)	# 9-12
    sprite('ad060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActBDownCrash():
    sprite('ad060_07', 4)	# 1-4

@State
def CmnActBDownBound():
    sprite('null', 60)	# 1-60

@State
def CmnActBDownLoop():
    sprite('null', 60)	# 1-60

@State
def CmnActBDown2Stand():
    sprite('null', 60)	# 1-60

@State
def CmnActFDownUpper():
    sprite('ad063_00', 3)	# 1-3

@State
def CmnActFDownUpperEnd():
    sprite('ad063_01', 3)	# 1-3

@State
def CmnActFDownDown():
    label(0)
    sprite('ad063_03', 3)	# 1-3
    sprite('ad063_04', 3)	# 4-6
    loopRest()
    gotoLabel(0)

@State
def CmnActFDownCrash():
    sprite('ad063_05', 6)	# 1-6

@State
def CmnActFDownBound():
    sprite('ad060_08', 2)	# 1-2
    sprite('ad060_09', 2)	# 3-4
    sprite('ad060_10', 2)	# 5-6
    sprite('ad060_11', 2)	# 7-8

@State
def CmnActFDownLoop():
    sprite('ad060_12', 3)	# 1-3

@State
def CmnActFDown2Stand():
    sprite('ad064_00', 6)	# 1-6
    sprite('ad064_01', 6)	# 7-12
    sprite('ad064_02', 6)	# 13-18
    sprite('ad064_03', 6)	# 19-24

@State
def CmnActVDownUpper():
    sprite('ad060_00', 4)	# 1-4
    label(0)
    sprite('ad060_01', 4)	# 5-8
    sprite('ad060_02', 4)	# 9-12
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownUpperEnd():
    sprite('ad060_03', 4)	# 1-4
    sprite('ad060_04', 4)	# 5-8

@State
def CmnActVDownDown():
    sprite('ad060_04', 8)	# 1-8
    label(0)
    sprite('ad060_05', 4)	# 9-12
    sprite('ad060_06', 4)	# 13-16
    loopRest()
    gotoLabel(0)

@State
def CmnActVDownCrash():
    sprite('ad060_07', 4)	# 1-4

@State
def CmnActBlowoff():
    sprite('ad072_00', 3)	# 1-3
    sprite('ad072_01', 3)	# 4-6
    sprite('ad072_02', 3)	# 7-9
    label(0)
    sprite('ad072_01', 3)	# 10-12
    sprite('ad072_02', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActKirimomiUpper():
    label(0)
    sprite('ad074_00', 3)	# 1-3
    sprite('ad074_01', 3)	# 4-6
    sprite('ad074_02', 3)	# 7-9
    sprite('ad074_03', 3)	# 10-12
    loopRest()
    gotoLabel(0)

@State
def CmnActSkeleton():
    sprite('null', 60)	# 1-60

@State
def CmnActFreeze():
    sprite('ad052_01', 1)	# 1-1

@State
def CmnActWallBound():
    sprite('ad072_03', 3)	# 1-3

@State
def CmnActWallBoundDown():
    sprite('ad063_00', 3)	# 1-3
    sprite('ad063_01', 3)	# 4-6
    sprite('ad063_02', 3)	# 7-9
    label(0)
    sprite('ad063_03', 3)	# 10-12
    sprite('ad063_04', 3)	# 13-15
    loopRest()
    gotoLabel(0)

@State
def CmnActStaggerLoop():
    sprite('ad070_00', 32767)	# 1-32767

@State
def CmnActStaggerDown():
    sprite('ad070_01', 4)	# 1-4
    sprite('ad070_02', 4)	# 5-8
    sprite('ad070_03', 4)	# 9-12
    sprite('ad070_04', 4)	# 13-16
    sprite('ad070_05', 4)	# 17-20
    sprite('ad070_06', 4)	# 21-24

@State
def CmnActUkemiStagger():
    sprite('ad040_03', 2)	# 1-2
    sprite('ad040_02', 2)	# 3-4
    sprite('ad040_01', 2)	# 5-6
    sprite('ad040_00', 2)	# 7-8

@State
def CmnActUkemiAirF():
    sprite('ad020_02', 3)	# 1-3
    sprite('ad020_03', 3)	# 4-6
    sprite('ad020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirB():
    sprite('ad020_02', 3)	# 1-3
    sprite('ad020_03', 3)	# 4-6
    sprite('ad020_04', 32767)	# 7-32773

@State
def CmnActUkemiAirN():
    sprite('ad020_02', 3)	# 1-3
    sprite('ad020_03', 3)	# 4-6
    sprite('ad020_04', 32767)	# 7-32773

@State
def CmnActUkemiLandF():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandB():
    sprite('null', 60)	# 1-60

@State
def CmnActUkemiLandN():
    sprite('ad112_00', 3)	# 1-3
    sprite('ad112_01', 3)	# 4-6
    sprite('ad112_02', 3)	# 7-9
    sprite('ad112_03', 3)	# 10-12
    sprite('ad112_04', 3)	# 13-15
    sprite('ad112_05', 3)	# 16-18
    label(0)
    sprite('ad020_07', 4)	# 19-22
    sprite('ad020_08', 4)	# 23-26
    loopRest()
    gotoLabel(0)

@State
def CmnActUkemiLandNLanding():
    sprite('ad010_01', 3)	# 1-3
    sprite('ad010_00', 3)	# 4-6

@State
def CmnActMidGuardPre():
    sprite('ad040_00', 3)	# 1-3
    sprite('ad040_01', 3)	# 4-6

@State
def CmnActMidGuardLoop():
    label(0)
    sprite('ad040_02', 5)	# 1-5
    sprite('ad040_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActMidGuardEnd():
    sprite('ad040_01', 3)	# 1-3
    sprite('ad040_00', 3)	# 4-6

@State
def CmnActMidHeavyGuardLoop():
    sprite('ad040_04', 1)	# 1-1
    label(0)
    sprite('ad040_02', 5)	# 2-6
    sprite('ad040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActMidHeavyGuardEnd():
    sprite('ad040_01', 3)	# 1-3
    sprite('ad040_00', 3)	# 4-6

@State
def CmnActHighGuardPre():
    sprite('ad040_00', 3)	# 1-3
    sprite('ad040_01', 3)	# 4-6

@State
def CmnActHighGuardLoop():
    sprite('ad040_04', 1)	# 1-1
    label(0)
    sprite('ad040_02', 5)	# 2-6
    sprite('ad040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighGuardEnd():
    sprite('ad040_01', 3)	# 1-3
    sprite('ad040_00', 3)	# 4-6

@State
def CmnActHighHeavyGuardLoop():
    sprite('ad040_04', 1)	# 1-1
    label(0)
    sprite('ad040_02', 5)	# 2-6
    sprite('ad040_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActHighHeavyGuardEnd():
    sprite('ad040_01', 3)	# 1-3
    sprite('ad040_00', 3)	# 4-6

@State
def CmnActCrouchGuardPre():
    sprite('ad043_00', 3)	# 1-3
    sprite('ad043_01', 3)	# 4-6

@State
def CmnActCrouchGuardLoop():
    label(0)
    sprite('ad043_02', 5)	# 1-5
    sprite('ad043_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchGuardEnd():
    sprite('ad043_01', 3)	# 1-3
    sprite('ad043_00', 3)	# 4-6

@State
def CmnActCrouchHeavyGuardLoop():
    sprite('ad043_04', 1)	# 1-1
    label(0)
    sprite('ad043_02', 5)	# 2-6
    sprite('ad043_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActCrouchHeavyGuardEnd():
    sprite('ad043_01', 3)	# 1-3
    sprite('ad043_00', 3)	# 4-6

@State
def CmnActAirGuardPre():
    sprite('ad045_00', 3)	# 1-3
    sprite('ad045_01', 3)	# 4-6

@State
def CmnActAirGuardLoop():
    label(0)
    sprite('ad045_02', 5)	# 1-5
    sprite('ad045_03', 5)	# 6-10
    loopRest()
    gotoLabel(0)

@State
def CmnActAirGuardEnd():
    sprite('ad045_01', 3)	# 1-3
    sprite('ad045_00', 3)	# 4-6

@State
def CmnActAirHeavyGuardLoop():
    sprite('ad045_04', 1)	# 1-1
    label(0)
    sprite('ad045_02', 5)	# 2-6
    sprite('ad045_03', 5)	# 7-11
    loopRest()
    gotoLabel(0)

@State
def CmnActAirHeavyGuardEnd():
    sprite('ad045_01', 3)	# 1-3
    sprite('ad045_00', 3)	# 4-6

@State
def CmnActGuardBreakStand():
    sprite('ad040_04', 2)	# 1-2
    sprite('ad040_04', 2)	# 3-4
    sprite('ad040_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ad040_02', 4)	# 6-9
    sprite('ad040_01', 4)	# 10-13
    sprite('ad040_00', 4)	# 14-17

@State
def CmnActGuardBreakCrouch():
    sprite('ad043_04', 2)	# 1-2
    sprite('ad043_04', 2)	# 3-4
    sprite('ad043_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ad043_02', 4)	# 6-9
    sprite('ad043_01', 4)	# 10-13
    sprite('ad043_00', 4)	# 14-17

@State
def CmnActGuardBreakAir():
    sprite('ad045_04', 2)	# 1-2
    sprite('ad045_04', 2)	# 3-4
    sprite('ad045_04', 1)	# 5-5
    Unknown2042(1)
    sprite('ad045_02', 4)	# 6-9
    sprite('ad045_01', 4)	# 10-13
    sprite('ad045_00', 4)	# 14-17

@State
def CmnActAirTurn():
    sprite('ad025_00', 1)	# 1-1
    sprite('ad025_01', 2)	# 2-3
    sprite('ad025_02', 1)	# 4-4

@State
def CmnActLockWait():
    sprite('ad040_02', 1)	# 1-1
    sprite('ad040_01', 3)	# 2-4
    sprite('ad040_00', 3)	# 5-7

@State
def CmnActLockReject():
    sprite('ad200_00', 5)	# 1-5
    sprite('ad200_01', 5)	# 6-10
    sprite('ad200_02', 3)	# 11-13	 **attackbox here**
    sprite('ad200_03', 8)	# 14-21
    sprite('ad200_04', 8)	# 22-29

@State
def CmnActAirLockWait():
    sprite('null', 60)	# 1-60

@State
def CmnActAirLockReject():
    sprite('null', 60)	# 1-60

@State
def CmnActLandSpin():
    sprite('null', 60)	# 1-60

@State
def CmnActLandSpinDown():
    sprite('null', 60)	# 1-60

@State
def CmnActVertSpin():
    sprite('null', 60)	# 1-60

@State
def CmnActSlideAir():
    sprite('ad124_00', 2)	# 1-2
    label(0)
    sprite('ad124_01', 2)	# 3-4
    sprite('ad124_02', 2)	# 5-6
    sprite('ad124_03', 2)	# 7-8
    sprite('ad124_04', 2)	# 9-10
    sprite('ad124_05', 2)	# 11-12
    sprite('ad124_06', 2)	# 13-14
    sprite('ad124_07', 2)	# 15-16
    sprite('ad124_08', 2)	# 17-18
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideKeep():
    sprite('ad077_02', 4)	# 1-4
    label(0)
    sprite('ad077_03', 3)	# 5-7
    sprite('ad077_04', 3)	# 8-10
    loopRest()
    gotoLabel(0)

@State
def CmnActSlideEnd():
    sprite('ad077_05', 5)	# 1-5
    sprite('ad077_06', 4)	# 6-9

@State
def CmnActAomukeSlideKeep():
    sprite('null', 60)	# 1-60

@State
def CmnActAomukeSlideEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstBegin():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstLoop():
    sprite('null', 60)	# 1-60

@State
def CmnActBurstEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActAirBurstBegin():
    sprite('null', 60)	# 1-60

@State
def CmnActAirBurstLoop():
    sprite('null', 60)	# 1-60

@State
def CmnActAirBurstEnd():
    sprite('null', 60)	# 1-60

@State
def CmnActOverDriveBegin():
    label(0)
    sprite('ad121_00', 3)	# 1-3
    sprite('ad121_01', 3)	# 4-6
    sprite('ad121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveLoop():
    sprite('ad121_03', 3)	# 1-3
    label(0)
    sprite('ad121_04', 2)	# 4-5
    sprite('ad121_05', 2)	# 6-7
    sprite('ad121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActOverDriveEnd():
    sprite('ad121_07', 4)	# 1-4
    sprite('ad020_04', 4)	# 5-8
    sprite('ad010_00', 4)	# 9-12

@State
def CmnActAirOverDriveBegin():
    label(0)
    sprite('ad121_00', 3)	# 1-3
    sprite('ad121_01', 3)	# 4-6
    sprite('ad121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveLoop():
    sprite('ad121_03', 3)	# 1-3
    label(0)
    sprite('ad121_04', 2)	# 4-5
    sprite('ad121_05', 2)	# 6-7
    sprite('ad121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirOverDriveEnd():
    sprite('ad121_07', 3)	# 1-3
    sprite('ad020_04', 3)	# 4-6
    sprite('ad020_05', 3)	# 7-9
    sprite('ad020_06', 3)	# 10-12
    label(0)
    sprite('ad020_07', 4)	# 13-16
    sprite('ad020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PAD_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 9999, 0)
    label(0)
    sprite('ad121_00', 3)	# 1-3
    sprite('ad121_01', 3)	# 4-6
    sprite('ad121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushLoop():
    sprite('ad121_03', 3)	# 1-3
    label(0)
    sprite('ad121_04', 2)	# 4-5
    sprite('ad121_05', 2)	# 6-7
    sprite('ad121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossRushEnd():
    sprite('ad121_07', 4)	# 1-4
    sprite('ad020_04', 2)	# 5-6
    sprite('ad020_05', 2)	# 7-8
    sprite('ad020_06', 2)	# 9-10
    sprite('ad020_07', 2)	# 11-12

@State
def CmnActAirCrossRushBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PAD_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 9999, 0)
    label(0)
    sprite('ad121_00', 3)	# 1-3
    sprite('ad121_01', 3)	# 4-6
    sprite('ad121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushLoop():
    sprite('ad121_03', 3)	# 1-3
    label(0)
    sprite('ad121_04', 2)	# 4-5
    sprite('ad121_05', 2)	# 6-7
    sprite('ad121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossRushEnd():
    sprite('ad121_07', 3)	# 1-3
    sprite('ad020_04', 3)	# 4-6
    sprite('ad020_05', 3)	# 7-9
    sprite('ad020_06', 3)	# 10-12
    label(0)
    sprite('ad020_07', 4)	# 13-16
    sprite('ad020_08', 4)	# 17-20
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PAD_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 9999, 0)
    label(0)
    sprite('ad121_00', 3)	# 1-3
    sprite('ad121_01', 3)	# 4-6
    sprite('ad121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeLoop():
    sprite('ad121_03', 3)	# 1-3
    label(0)
    sprite('ad121_04', 2)	# 4-5
    sprite('ad121_05', 2)	# 6-7
    sprite('ad121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActCrossChangeEnd():
    sprite('ad121_07', 4)	# 1-4
    sprite('ad020_04', 2)	# 5-6
    sprite('ad020_05', 2)	# 7-8
    sprite('ad020_06', 2)	# 9-10
    sprite('ad020_07', 2)	# 11-12

@State
def CmnActAirCrossChangeBegin():

    def upon_IMMEDIATE():
        loopRelated(17, 7)

        def upon_17():
            Unknown36(28)
            Unknown23148('PAD_PersonaWait')
            Unknown48('030000000200000033000000190000000200000000000000')
            Unknown35()
            if (not SLOT_51):
                Unknown23029(11, 9999, 0)
    label(0)
    sprite('ad121_00', 3)	# 1-3
    sprite('ad121_01', 3)	# 4-6
    sprite('ad121_02', 3)	# 7-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeLoop():
    sprite('ad121_03', 3)	# 1-3
    label(0)
    sprite('ad121_04', 2)	# 4-5
    sprite('ad121_05', 2)	# 6-7
    sprite('ad121_06', 2)	# 8-9
    loopRest()
    gotoLabel(0)

@State
def CmnActAirCrossChangeEnd():
    sprite('ad121_07', 3)	# 1-3
    sprite('ad020_04', 3)	# 4-6
    sprite('ad020_05', 3)	# 7-9
    sprite('ad020_06', 3)	# 10-12
    label(0)
    sprite('ad020_07', 4)	# 13-16
    sprite('ad020_08', 4)	# 17-20
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
    if Unknown46(5):
        Unknown13(5)

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
        DisableAttackRestOfMove()

        def upon_41():
            clearUponHandler(41)
            sendToLabel(100)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
    sprite('null', 2)	# 1-2
    sprite('null', 600)	# 3-602
    label(100)
    sprite('null', 28)	# 603-630
    sprite('null', 1)	# 631-631
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeY(1500000)
    physicsYImpulse(-300000)
    Unknown2053(1)
    EnableCollision(1)
    sprite('ad251_02', 2)	# 632-633
    SFX_3('hit_m_fast')
    sprite('ad251_03', 32767)	# 634-33400	 **attackbox here**
    label(1)
    sprite('ad251_03ex01', 3)	# 33401-33403	 **attackbox here**
    sprite('ad010_00', 3)	# 33404-33406
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ad010_01', 3)	# 33407-33409
    sprite('ad010_02', 5)	# 33410-33414
    sprite('ad010_03', 5)	# 33415-33419
    sprite('ad010_01', 3)	# 33420-33422
    sprite('ad010_00', 3)	# 33423-33425

@State
def CmnActChangePartnerQuickIn():
    sprite('ad032_05', 3)	# 1-3
    sprite('ad032_06', 5)	# 4-8
    sprite('ad032_07', 7)	# 9-15
    sprite('ad032_09', 7)	# 16-22
    sprite('ad032_10', 7)	# 23-29

@State
def CmnActChangePartnerOut():

    def upon_IMMEDIATE():
        Unknown17013()
    sprite('ad033_01', 3)	# 1-3
    sprite('ad033_02', 3)	# 4-6
    sprite('ad033_01', 3)	# 7-9
    sprite('ad033_02', 3)	# 10-12
    sprite('ad033_01', 3)	# 13-15
    sprite('ad033_02', 3)	# 16-18
    sprite('ad033_01', 3)	# 19-21
    sprite('ad033_02', 3)	# 22-24
    sprite('ad033_01', 3)	# 25-27
    sprite('ad033_02', 3)	# 28-30
    sprite('ad033_01', 30)	# 31-60

@State
def CmnActChangePartnerQuickOut():

    def upon_IMMEDIATE():
        Unknown17013()

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)
    sprite('ad033_00', 1)	# 1-1
    sprite('ad033_01', 4)	# 2-5
    sprite('ad033_02', 4)	# 6-9
    loopRest()
    label(0)
    sprite('ad033_02', 3)	# 10-12
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad033_03', 3)	# 13-15
    sprite('ad033_04', 3)	# 16-18

@State
def CmnActChangeReturnAppeal():
    sprite('ad611_00', 3)	# 1-3
    sprite('ad611_01', 7)	# 4-10
    sprite('ad611_02', 7)	# 11-17
    sprite('ad611_03', 7)	# 18-24
    sprite('ad611_04', 7)	# 25-31
    sprite('ad611_05', 7)	# 32-38
    sprite('ad611_01', 7)	# 39-45
    sprite('ad611_02', 7)	# 46-52
    sprite('ad611_03', 7)	# 53-59
    sprite('ad611_04', 7)	# 60-66
    sprite('ad611_05', 7)	# 67-73
    sprite('ad611_00', 3)	# 74-76

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
    sprite('ad020_07', 4)	# 3-6
    Unknown1019(95)
    sprite('ad020_08', 4)	# 7-10
    Unknown1019(95)
    loopRest()
    gotoLabel(0)
    label(99)
    sprite('ad010_00', 2)	# 11-12
    Unknown8000(100, 1, 1)
    sprite('keep', 100)	# 13-112

@State
def CmnActChangePartnerAssistAtk_A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 61)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 2512):
                Recovery()
    sprite('ad233_00', 3)	# 1-3
    sprite('ad233_01', 3)	# 4-6
    Unknown23029(11, 2502, 0)
    tag_voice(1, 'pad121_0', 'pad122_0', 'pad123_0', '')
    sprite('ad233_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    sprite('ad233_03', 3)	# 10-12
    sprite('ad233_04', 4)	# 13-16
    sprite('ad233_05', 4)	# 17-20
    sprite('ad233_06', 4)	# 21-24
    sprite('ad233_04', 5)	# 25-29
    sprite('ad233_05', 5)	# 30-34
    sprite('ad233_06', 5)	# 35-39
    label(0)
    sprite('ad233_04', 6)	# 40-45
    sprite('ad233_05', 6)	# 46-51
    sprite('ad233_06', 6)	# 52-57
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad233_01', 6)	# 58-63
    sprite('ad233_00', 6)	# 64-69
    sprite('ad010_01', 3)	# 70-72
    sprite('ad010_00', 3)	# 73-75

@State
def CmnActChangePartnerAssistAtk_B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 45)

        def upon_17():
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 2511):
                Recovery()
    sprite('ad232_00', 3)	# 1-3
    sprite('ad232_01', 3)	# 4-6
    Unknown23029(11, 2501, 0)
    tag_voice(1, 'pad306_0', 'pad306_1', '', '')
    sprite('ad232_02', 3)	# 7-9
    sprite('ad232_03', 4)	# 10-13
    GFX_1('persona_enter_ply', 0)
    sprite('ad232_04', 4)	# 14-17
    sprite('ad232_05', 4)	# 18-21
    label(0)
    sprite('ad232_03', 4)	# 22-25
    sprite('ad232_04', 4)	# 26-29
    sprite('ad232_05', 4)	# 30-33
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad232_06', 3)	# 34-36
    sprite('ad232_07', 3)	# 37-39
    sprite('ad010_01', 3)	# 40-42
    sprite('ad010_00', 3)	# 43-45

@State
def CmnActChangePartnerAssistAtk_D():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        AttackLevel_(4)
        Damage(1500)
        Unknown11092(1)
        Hitstop(6)
        Unknown9310(10)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-30000)
        AirPushbackX(1000)
        PushbackX(12000)
        Unknown2004(1, 0)
        callSubroutine('PartnerSkillInit')

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)

        def upon_CLEAR_OR_EXIT():
            if SLOT_2:
                if (SLOT_19 < 200000):
                    clearUponHandler(3)
                    Unknown1019(35)
    sprite('ad400_00', 2)	# 1-2
    sprite('ad400_05', 2)	# 3-4
    Unknown8001(1, 0)
    physicsXImpulse(50000)
    physicsYImpulse(8000)
    Unknown1043()
    Unknown2037(1)
    Unknown7007('7061643130385f300000000000000000640000007061643130385f310000000000000000640000007061643130385f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ad400_06', 3)	# 5-7
    sprite('ad400_07', 3)	# 8-10
    sprite('ad400_08', 30)	# 11-40
    label(1)
    sprite('ad400_09', 3)	# 41-43	 **attackbox here**
    Unknown2037(0)
    Unknown8000(100, 1, 1)
    Unknown1019(25)
    SFX_3('ad008')
    GFX_0('adef_400_explosion', 100)
    sprite('ad400_09', 3)	# 44-46	 **attackbox here**
    Unknown1019(25)
    sprite('ad400_10', 6)	# 47-52
    GFX_0('ad400_Gun', 100)
    Unknown1084(1)
    sprite('ad400_11', 3)	# 53-55
    sprite('ad400_12', 2)	# 56-57
    SFX_3('hit_m_fast')
    sprite('ad400_13', 6)	# 58-63	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(2500)
    AirPushbackY(30000)
    AirUntechableTime(45)
    Unknown9311()
    Hitstop(12)
    Unknown9215()
    sprite('ad400_13', 2)	# 64-65	 **attackbox here**
    StartMultihit()
    sprite('ad400_14', 8)	# 66-73
    Recovery()
    sprite('ad400_15', 8)	# 74-81
    sprite('ad231_09ex', 8)	# 82-89
    sprite('ad231_10ex', 8)	# 90-97

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
    Unknown2036(111, -1, 0)
    sprite('null', 1)	# 2-2
    teleportRelativeX(-1500000)
    teleportRelativeY(240000)
    setGravity(0)
    physicsYImpulse(-9600)
    SLOT_12 = SLOT_19
    teleportRelativeX(-200000)
    Unknown1019(4)
    label(0)
    sprite('ad020_07', 4)	# 3-6
    sprite('ad020_08', 4)	# 7-10
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 10)	# 11-20
    if SLOT_58:
        enterState('UltimateDUOSP')
    else:
        enterState('UltimateDUO')

@State
def UltimateDUO():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        SLOT_4 = 1
        Unknown1084(1)
        Unknown36(28)
        Unknown23148('PAD_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4211):
                loopRelated(17, 258)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(3)
                Unknown13024(0)
                sendToLabel(1)
            if (SLOT_48 == 4212):
                Unknown13024(1)
            if (SLOT_48 == 4213):
                setInvincible(0)
    sprite('ad433_00', 3)	# 1-3
    sprite('ad433_01', 3)	# 4-6
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ad433_02', 4)	# 7-10
    sprite('ad433_03', 6)	# 11-16
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(61200)
    physicsYImpulse(-900)
    Unknown35()
    sprite('ad433_04', 6)	# 17-22
    sprite('ad433_05', 6)	# 23-28
    sprite('ad433_03', 6)	# 29-34
    sprite('ad433_04', 6)	# 35-40
    sprite('ad433_05', 6)	# 41-46
    sprite('ad433_03', 6)	# 47-52
    sprite('ad433_04', 6)	# 53-58
    sprite('ad433_05', 6)	# 59-64
    sprite('ad433_06', 3)	# 65-67
    Unknown23029(11, 4005, 0)
    sprite('ad433_07', 3)	# 68-70
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('ad433_08', 6)	# 71-76
    sprite('ad433_09', 6)	# 77-82
    sprite('ad433_10', 6)	# 83-88
    sprite('ad433_08', 5)	# 89-93
    sprite('ad433_09', 5)	# 94-98
    sprite('ad433_10', 5)	# 99-103
    setInvincible(0)
    sprite('ad433_08', 5)	# 104-108
    sprite('ad433_09', 5)	# 109-113
    sprite('ad433_10', 5)	# 114-118
    sprite('ad433_08', 5)	# 119-123
    sprite('ad433_09', 5)	# 124-128
    sprite('ad433_10', 5)	# 129-133
    sprite('ad433_01', 5)	# 134-138
    sprite('ad433_00', 5)	# 139-143
    ExitState()
    label(1)
    sprite('ad433_09', 5)	# 144-148
    sprite('ad433_10', 5)	# 149-153
    sprite('ad433_01', 5)	# 154-158
    sprite('ad432_04', 5)	# 159-163
    sprite('ad432_05', 5)	# 164-168
    sprite('ad432_06', 5)	# 169-173
    sprite('ad432_07', 6)	# 174-179
    label(2)
    sprite('ad432_08', 6)	# 180-185
    sprite('ad432_09', 6)	# 186-191
    sprite('ad432_10', 6)	# 192-197
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ad432_11', 6)	# 198-203
    sprite('ad432_12', 6)	# 204-209

@State
def UltimateDUOSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23056('')
        Unknown30063(1)
        SLOT_4 = 1
        Unknown1084(1)
        Unknown36(28)
        Unknown23148('PAD_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4214):
                loopRelated(17, 287)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(3)
                Unknown13024(0)
                sendToLabel(1)
            if (SLOT_48 == 4215):
                Unknown13024(1)
            if (SLOT_48 == 4216):
                setInvincible(0)
    sprite('ad433_00', 3)	# 1-3
    sprite('ad433_01', 3)	# 4-6
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ad433_02', 4)	# 7-10
    sprite('ad433_03', 6)	# 11-16
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(61200)
    physicsYImpulse(-900)
    Unknown35()
    sprite('ad433_04', 6)	# 17-22
    sprite('ad433_05', 6)	# 23-28
    sprite('ad433_03', 6)	# 29-34
    sprite('ad433_04', 6)	# 35-40
    sprite('ad433_05', 6)	# 41-46
    sprite('ad433_03', 6)	# 47-52
    sprite('ad433_04', 6)	# 53-58
    sprite('ad433_05', 6)	# 59-64
    sprite('ad433_06', 3)	# 65-67
    Unknown23029(11, 4006, 0)
    sprite('ad433_07', 3)	# 68-70
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('ad433_08', 6)	# 71-76
    sprite('ad433_09', 6)	# 77-82
    sprite('ad433_10', 6)	# 83-88
    sprite('ad433_08', 5)	# 89-93
    sprite('ad433_09', 5)	# 94-98
    sprite('ad433_10', 5)	# 99-103
    setInvincible(0)
    sprite('ad433_08', 5)	# 104-108
    sprite('ad433_09', 5)	# 109-113
    sprite('ad433_10', 5)	# 114-118
    sprite('ad433_08', 5)	# 119-123
    sprite('ad433_09', 5)	# 124-128
    sprite('ad433_10', 5)	# 129-133
    sprite('ad433_01', 5)	# 134-138
    sprite('ad433_00', 5)	# 139-143
    ExitState()
    label(1)
    sprite('ad433_01', 5)	# 144-148
    sprite('ad433_00', 5)	# 149-153
    sprite('ad000_00', 5)	# 154-158
    sprite('ad610_00', 6)	# 159-164
    sprite('ad610_01', 6)	# 165-170
    sprite('ad610_02', 6)	# 171-176
    Unknown4004('4361726400000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown38(4, 1)
    Unknown36(1)
    teleportRelativeX(50000)
    Unknown1007(350000)
    physicsYImpulse(-900)
    Unknown35()
    sprite('ad610_03', 6)	# 177-182
    sprite('ad610_04', 6)	# 183-188
    sprite('ad610_05', 6)	# 189-194
    sprite('ad610_06', 6)	# 195-200
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    Unknown2036(60, -1, 0)
    label(2)
    sprite('ad610_07', 6)	# 201-206
    sprite('ad610_08', 6)	# 207-212
    sprite('ad610_09', 6)	# 213-218
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ad610_02', 4)	# 219-222
    sprite('ad610_01', 4)	# 223-226
    sprite('ad610_00', 4)	# 227-230

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
            sendToLabel(1)
    sprite('null', 120)	# 1-120
    label(0)
    sprite('null', 8)	# 121-128
    Unknown1086(22)
    teleportRelativeX(-150000)
    teleportRelativeX(-580000)
    Unknown1007(2900000)
    physicsXImpulse(20000)
    physicsYImpulse(-100000)
    sprite('ad251_00', 7)	# 129-135
    sprite('ad251_01', 7)	# 136-142
    sprite('ad251_02', 6)	# 143-148
    SFX_3('hit_m_fast')
    sprite('ad251_03ex01', 3)	# 149-151	 **attackbox here**
    sprite('ad251_03ex01', 32767)	# 152-32918	 **attackbox here**
    label(1)
    sprite('ad251_03ex01', 2)	# 32919-32920	 **attackbox here**
    Unknown1019(5)
    sprite('ad010_00', 3)	# 32921-32923
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ad010_01', 3)	# 32924-32926
    sprite('ad010_02', 6)	# 32927-32932
    sprite('ad010_03', 6)	# 32933-32938
    sprite('ad010_01', 6)	# 32939-32944
    sprite('ad010_00', 6)	# 32945-32950

@State
def CmnActChangeReturnAppealBurst():
    sprite('ad064_01', 50)	# 1-50
    sprite('ad064_02', 5)	# 51-55
    sprite('ad064_03', 25)	# 56-80

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
    sprite('ad251_03', 32767)	# 32-32798	 **attackbox here**
    label(1)
    sprite('keep', 1)	# 32799-32799
    sprite('ad251_07', 3)	# 32800-32802
    if SLOT_3:
        enterState('CmnActAComboFinalBlowFinish')
    Unknown23022(0)
    sprite('ad251_08', 3)	# 32803-32805
    sprite('ad010_00', 3)	# 32806-32808
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ad010_01', 3)	# 32809-32811
    sprite('ad010_02', 5)	# 32812-32816
    sprite('ad010_03', 5)	# 32817-32821
    sprite('ad010_01', 4)	# 32822-32825
    sprite('ad010_00', 4)	# 32826-32829

@State
def CmnActAComboFinalBlowFinish():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown9016(1)
        DisableAttackRestOfMove()
    sprite('keep', 1)	# 1-1
    StartMultihit()
    sprite('ad251_08', 2)	# 2-3
    sprite('ad010_00', 2)	# 4-5
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    sprite('ad010_01', 2)	# 6-7
    sprite('ad010_02', 2)	# 8-9
    sprite('ad010_03', 2)	# 10-11
    sprite('ad010_01', 2)	# 12-13
    sprite('ad010_00', 2)	# 14-15
    sprite('ad406_07', 3)	# 16-18
    sprite('ad406_08', 3)	# 19-21
    sprite('ad406_09', 3)	# 22-24
    sprite('ad406_10', 3)	# 25-27
    sprite('ad406_11', 7)	# 28-34
    Unknown23029(11, 2008, 0)
    GFX_1('persona_enter_ply', 1)
    SFX_3('persona_destroy')
    Unknown7009(2)
    sprite('ad406_12', 6)	# 35-40	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    sprite('ad406_13', 5)	# 41-45
    sprite('ad406_14', 5)	# 46-50
    sprite('ad406_15', 5)	# 51-55
    sprite('ad406_13', 5)	# 56-60
    sprite('ad406_14', 5)	# 61-65
    sprite('ad406_01', 5)	# 66-70
    sprite('ad406_00', 5)	# 71-75

@State
def NmlAtk5A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        AirPushbackY(16000)
        PushbackX(19800)
        HitOrBlockCancel('NmlAtk5AA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
    sprite('ad203_00', 2)	# 1-2
    sprite('ad203_01', 2)	# 3-4
    sprite('ad203_02', 2)	# 5-6
    SFX_3('hit_m_middle')
    sprite('ad203_03', 3)	# 7-9	 **attackbox here**
    Unknown7009(1)
    sprite('ad203_04', 6)	# 10-15
    Recovery()
    Unknown2063()
    sprite('ad203_12', 6)	# 16-21
    sprite('ad203_13', 6)	# 22-27

@State
def NmlAtk5AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Damage(500)
        Unknown11092(1)
        Hitstop(2)
        AirPushbackX(10000)
        AirPushbackY(2500)
        PushbackX(12000)
        AirUntechableTime(22)
        Unknown14077(0)
        HitOrBlockCancel('NmlAtk5AAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ad203_04', 3)	# 1-3
    sprite('ad203_05', 3)	# 4-6
    Unknown8006(100, 1, 0)
    Unknown1047(15000)
    physicsXImpulse(10000)
    sprite('ad203_06', 2)	# 7-8
    sprite('ad203_07', 3)	# 9-11	 **attackbox here**
    RefreshMultihit()
    sprite('ad203_05', 3)	# 12-14
    Unknown1019(50)
    Unknown8006(100, 1, 0)
    sprite('ad203_06', 2)	# 15-16
    SFX_3('hit_m_fast')
    sprite('ad203_07', 3)	# 17-19	 **attackbox here**
    RefreshMultihit()
    sprite('ad203_05', 3)	# 20-22
    Unknown8006(100, 1, 0)
    sprite('ad203_06', 2)	# 23-24
    SFX_3('hit_m_fast')
    sprite('ad203_07', 3)	# 25-27	 **attackbox here**
    RefreshMultihit()
    Unknown14077(1)
    AirPushbackX(15000)
    AirPushbackY(20000)
    Hitstop(11)
    Unknown9215()
    sprite('ad203_09', 4)	# 28-31
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ad203_10', 4)	# 32-35
    sprite('ad203_11', 4)	# 36-39
    sprite('ad203_12', 4)	# 40-43
    sprite('ad203_13', 4)	# 44-47

@State
def NmlAtk5AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(1500)
        Unknown11092(1)
        Unknown9310(10)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackY(-30000)
        AirPushbackX(1000)
        PushbackX(12000)
        Unknown2004(1, 0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        Unknown14077(0)
        HitOrBlockCancel('NmlAtk5AAAA')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ad400_00', 2)	# 1-2
    sprite('ad400_01', 2)	# 3-4
    sprite('ad400_05', 2)	# 5-6
    Unknown8001(1, 0)
    physicsXImpulse(32000)
    physicsYImpulse(8000)
    Unknown1043()
    Unknown7007('7061643130395f300000000000000000640000007061643130395f310000000000000000640000007061643130395f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ad400_06', 3)	# 7-9
    sprite('ad400_07', 3)	# 10-12
    sprite('ad400_08', 30)	# 13-42
    label(1)
    sprite('ad400_09', 3)	# 43-45	 **attackbox here**
    Unknown8000(100, 1, 1)
    Unknown1084(1)
    SFX_3('ad008')
    GFX_0('adef_400_explosion', 100)
    sprite('ad400_10', 6)	# 46-51
    GFX_0('ad400_Gun', 100)
    sprite('ad400_11', 3)	# 52-54
    sprite('ad400_12', 2)	# 55-56
    SFX_3('hit_m_fast')
    sprite('ad400_13', 3)	# 57-59	 **attackbox here**
    RefreshMultihit()
    GroundedHitstunAnimation(9)
    AirHitstunAnimation(9)
    AirPushbackX(2500)
    AirPushbackY(21000)
    AirUntechableTime(29)
    Unknown9311()
    Unknown9215()
    Unknown14077(1)
    sprite('ad400_14', 6)	# 60-65
    Recovery()
    Unknown2063()
    sprite('ad400_15', 6)	# 66-71
    sprite('ad231_09ex', 6)	# 72-77
    sprite('ad231_10ex', 6)	# 78-83

@State
def NmlAtk5AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        Damage(0)
        Hitstop(1)
        Unknown11082(1)
        Unknown11044(1)

        def upon_78():
            Unknown11050('050000000000000000000000000000000000000000000000000000000000000000000000')
            enterState('NmlAtk5AAAAGrip')
    sprite('ad406_00', 1)	# 1-1
    sprite('ad406_01', 1)	# 2-2
    sprite('ad406_02', 2)	# 3-4
    Unknown1051(50)
    sprite('ad406_03', 2)	# 5-6
    sprite('ad406_01ex', 2)	# 7-8
    SFX_3('hit_l_fast')
    sprite('ad406_04', 2)	# 9-10	 **attackbox here**
    Recovery()
    Unknown2063()
    sprite('ad406_05', 3)	# 11-13
    sprite('ad406_06', 20)	# 14-33
    SFX_1('pad154')
    sprite('ad406_05', 4)	# 34-37
    sprite('ad406_04', 4)	# 38-41	 **attackbox here**
    StartMultihit()
    sprite('ad406_01', 4)	# 42-45
    sprite('ad406_00', 4)	# 46-49

@State
def NmlAtk5AAAAGrip():

    def upon_IMMEDIATE():
        Unknown17011('NmlAtk5AAAAExe', 1, 0, 0)
        Unknown2018(0, 80)
        Unknown11032('ffffffffffffffffffffffffffffffff')
        Unknown11054(-1)
        Unknown11002(-1)
        AttackP2(100)
        Hitstop(0)
        Unknown11025(0)
        Unknown11064(1)
        Unknown30061(1)
        JumpCancel_(0)
        setInvincible(1)
    sprite('ad406_04', 2)	# 1-2	 **attackbox here**
    RefreshMultihit()
    sprite('ad406_05', 3)	# 3-5
    Recovery()
    Unknown2063()
    sprite('ad406_06', 20)	# 6-25
    SFX_1('pad154')
    sprite('ad406_05', 4)	# 26-29
    sprite('ad406_04', 4)	# 30-33	 **attackbox here**
    sprite('ad406_01', 4)	# 34-37
    sprite('ad406_00', 4)	# 38-41

@State
def NmlAtk5AAAAExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        JumpCancel_(0)
        AttackLevel_(0)
        Damage(0)
        AttackP2(100)
        Hitstop(0)
        AirHitstunAnimation(0)
        GroundedHitstunAnimation(0)
        AirPushbackY(18000)
        AirPushbackX(14000)
        PushbackX(28000)
        hitstun(30)
        Unknown23086(1)
        Unknown11064(1)
        loopRelated(17, 104)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 2011):
                Recovery()
                Unknown2063()
    sprite('ad406_04', 12)	# 1-12	 **attackbox here**
    StartMultihit()
    tag_voice(1, 'pad202_0', 'pad202_1', 'pad202_2', '')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown2018(1, 80)
    sprite('ad406_07', 7)	# 13-19
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_08', 7)	# 20-26
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_09', 7)	# 27-33
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_10', 7)	# 34-40
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_07', 7)	# 41-47
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_08', 7)	# 48-54
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_09', 7)	# 55-61
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_10', 7)	# 62-68
    SFX_3('cloth_l')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown23029(11, 2001, 0)
    sprite('ad406_11', 5)	# 69-73
    GFX_1('persona_enter_ply', 1)
    SFX_3('persona_destroy')
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    sprite('ad406_11', 13)	# 74-86
    Unknown5000(17, 0)
    Unknown5001('0000000000000000000000000000000000000000')
    Unknown21012('5041445f506572736f6e615468726f7753686f7400000000000000000000000021000000')
    sprite('ad406_12', 3)	# 87-89	 **attackbox here**
    SFX_3('hit_m_fast')
    RefreshMultihit()
    Unknown2018(0, 80)
    sprite('ad406_13', 5)	# 90-94
    sprite('ad406_14', 5)	# 95-99
    tag_voice(0, 'pad203_0', 'pad203_1', 'pad203_2', '')
    sprite('ad406_15', 5)	# 100-104
    Unknown2018(1, 80)
    label(0)
    sprite('ad406_13', 5)	# 105-109
    sprite('ad406_14', 5)	# 110-114
    sprite('ad406_15', 5)	# 115-119
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad406_13', 5)	# 120-124
    sprite('ad406_14', 5)	# 125-129
    sprite('ad406_15', 5)	# 130-134
    sprite('ad406_16', 6)	# 135-140
    sprite('ad406_01', 6)	# 141-146
    sprite('ad406_00', 6)	# 147-152

@State
def NmlAtk5B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5BB')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockJumpCancel(1)
        Unknown1112('')
        loopRelated(17, 30)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 2012):
                Recovery()
                Unknown2063()
    sprite('ad204_00', 3)	# 1-3
    sprite('ad204_01', 3)	# 4-6
    Unknown7009(5)
    Unknown23029(11, 2002, 0)
    sprite('ad204_02', 3)	# 7-9
    sprite('ad204_03', 4)	# 10-13
    GFX_1('persona_enter_ply', 0)
    sprite('ad204_04', 4)	# 14-17
    sprite('ad204_05', 4)	# 18-21
    label(0)
    sprite('ad204_03', 4)	# 22-25
    sprite('ad204_04', 4)	# 26-29
    sprite('ad204_05', 4)	# 30-33
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad204_06', 4)	# 34-37
    sprite('ad204_07', 4)	# 38-41

@State
def NmlAtk5BB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk5BBB')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        loopRelated(17, 40)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 2013):
                Recovery()
                Unknown2063()
    sprite('ad408_00', 3)	# 1-3
    sprite('ad408_01', 3)	# 4-6
    Unknown23029(11, 2003, 0)
    label(0)
    sprite('ad408_02', 4)	# 7-10
    sprite('ad408_03', 4)	# 11-14
    sprite('ad408_04', 4)	# 15-18
    SFX_3('slash_knife_fast')
    sprite('ad408_05', 4)	# 19-22
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad408_06', 3)	# 23-25
    sprite('ad408_07', 3)	# 26-28

@State
def NmlAtk5BBB():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        loopRelated(17, 44)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 2014):
                Recovery()
                Unknown2063()
    sprite('keep', 2)	# 1-2
    sprite('ad408_05', 1)	# 3-3
    sprite('ad408_05', 4)	# 4-7
    Unknown7007('7061643330305f300000000000000000640000007061643330305f310000000000000000640000007061643330305f320000000000000000640000000000000000000000000000000000000000000000')
    Unknown23029(11, 2004, 0)
    label(0)
    sprite('ad408_02', 4)	# 8-11
    sprite('ad408_03', 4)	# 12-15
    sprite('ad408_04', 4)	# 16-19
    SFX_3('slash_knife_fast')
    sprite('ad408_05', 4)	# 20-23
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad408_06', 3)	# 24-26
    sprite('ad408_07', 3)	# 27-29

@State
def NmlAtk4A():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(2)
        HitOrBlockCancel('NmlAtk4AA')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ad200_00', 3)	# 1-3
    sprite('ad200_01', 2)	# 4-5
    SFX_3('hit_l_fast')
    Unknown1051(80)
    sprite('ad200_02', 3)	# 6-8	 **attackbox here**
    Unknown7009(0)
    sprite('ad200_03', 8)	# 9-16
    Recovery()
    Unknown2063()
    sprite('ad200_04', 8)	# 17-24

@State
def NmlAtk4AA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtk4AAA')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
        HitOrBlockJumpCancel(1)
    sprite('ad201_00', 3)	# 1-3
    sprite('ad201_01', 3)	# 4-6
    sprite('ad201_02', 3)	# 7-9
    SFX_3('hit_m_fast')
    physicsXImpulse(30000)
    Unknown1028(-2500)
    Unknown8007(0, 1, 1)
    Unknown7009(3)
    sprite('ad201_03', 3)	# 10-12	 **attackbox here**
    sprite('ad201_04', 3)	# 13-15
    Unknown1028(0)
    Recovery()
    Unknown2063()
    sprite('ad201_05', 4)	# 16-19
    Unknown1019(80)
    Unknown8007(0, 1, 1)
    sprite('ad201_06', 4)	# 20-23
    Unknown1019(80)
    sprite('ad201_07', 4)	# 24-27
    Unknown1019(80)
    Unknown8007(0, 1, 1)
    sprite('ad201_08', 4)	# 28-31
    Unknown1019(80)
    sprite('ad201_09', 4)	# 32-35
    Unknown8010(0, 1, 1)
    Unknown1019(0)

@State
def NmlAtk4AAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(4)
        AttackP1(90)
        HitLow(2)
        Unknown11058('0000000000000000010000000000000000000000')
        GroundedHitstunAnimation(11)
        AirHitstunAnimation(11)
        AirPushbackX(16000)
        AirPushbackY(-20000)
        Unknown9310(10)
        Unknown2004(1, 0)

        def upon_LANDING():
            clearUponHandler(2)
            sendToLabel(1)
        HitOrBlockCancel('NmlAtk4AAAA')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
    sprite('ad202_00', 3)	# 1-3
    sprite('ad202_01', 3)	# 4-6
    Unknown8001(1, 0)
    physicsXImpulse(25000)
    Unknown1028(-500)
    physicsYImpulse(9000)
    setGravity(3000)
    sprite('ad202_02', 3)	# 7-9
    sprite('ad202_03', 30)	# 10-39
    label(1)
    sprite('ad202_04', 3)	# 40-42	 **attackbox here**
    SFX_3('hit_m_middle')
    Unknown7009(4)
    sprite('ad202_04ex', 2)	# 43-44
    Unknown8010(0, 1, 1)
    Recovery()
    Unknown2063()
    sprite('ad202_05', 2)	# 45-46
    Unknown1019(40)
    sprite('ad202_06', 4)	# 47-50
    Unknown8010(0, 1, 1)
    Unknown1084(1)
    sprite('ad202_07', 4)	# 51-54
    sprite('ad202_08', 4)	# 55-58
    sprite('ad202_09', 4)	# 59-62

@State
def NmlAtk4AAAA():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        JumpCancel_(0)
    sprite('ad405_00', 6)	# 1-6
    sprite('ad405_01', 9)	# 7-15
    SFX_3('hit_l_fast')
    Unknown7007('7061643330335f300000000000000000640000007061643330335f310000000000000000640000007061643330335f320000000000000000640000000000000000000000000000000000000000000000')
    SFX_3('ad006')
    sprite('ad405_02', 3)	# 16-18
    GFX_0('adef_405_muzzle_a', 2)
    GFX_0('dmy_LowShotA_Atk', 0)
    sprite('ad405_03', 6)	# 19-24
    sprite('ad405_04', 6)	# 25-30
    sprite('ad405_05', 6)	# 31-36
    sprite('ad405_06', 6)	# 37-42
    sprite('ad405_00', 6)	# 43-48

@State
def CmnActCrushAttack():

    def upon_IMMEDIATE():
        Unknown30072('')
    sprite('ad210_00', 2)	# 1-2
    sprite('ad210_01', 2)	# 3-4
    sprite('ad210_02', 1)	# 5-5
    Unknown8007(100, 1, 0)
    physicsXImpulse(34000)
    sprite('ad210_02', 1)	# 6-6
    tag_voice(1, 'pad156_0', 'pad156_1', '', '')
    sprite('ad210_03', 2)	# 7-8
    sprite('ad210_04', 2)	# 9-10
    sprite('ad210_05', 5)	# 11-15
    Unknown8001(0, 100)
    Unknown1019(25)
    physicsYImpulse(15000)
    setGravity(2600)
    sprite('ad210_06', 5)	# 16-20
    sendToLabelUpon(2, 1)
    sprite('ad210_07', 15)	# 21-35
    SFX_3('hit_m_middle')
    label(1)
    sprite('ad210_08', 1)	# 36-36	 **attackbox here**
    Unknown8000(100, 1, 1)
    SFX_1('pad116')
    RefreshMultihit()
    Unknown23086(1)
    Unknown1019(0)
    sprite('ad210_08', 2)	# 37-38	 **attackbox here**
    sprite('ad210_09', 2)	# 39-40
    sprite('ad210_10', 3)	# 41-43
    sprite('ad210_11', 7)	# 44-50
    sprite('ad210_10', 2)	# 51-52
    sprite('ad210_12', 2)	# 53-54
    sprite('ad210_13', 2)	# 55-56

@State
def CmnActCrushAttackChase1st():

    def upon_IMMEDIATE():
        Unknown30073(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(11)
    sprite('ad210_08', 1)	# 1-1	 **attackbox here**
    sprite('ad210_09', 2)	# 2-3
    sprite('ad210_10', 3)	# 4-6
    sprite('ad210_11', 8)	# 7-14
    sprite('ad210_10', 3)	# 15-17
    sprite('ad210_12', 3)	# 18-20
    sprite('ad210_13', 3)	# 21-23
    sprite('ad200_00', 3)	# 24-26
    sprite('ad200_01', 3)	# 27-29
    SFX_3('hit_l_fast')
    physicsXImpulse(10000)
    sprite('ad200_02', 3)	# 30-32	 **attackbox here**
    RefreshMultihit()
    Unknown1084(1)
    tag_voice(0, 'pad157_0', 'pad157_1', '', '')
    sprite('ad200_03', 6)	# 33-38
    sprite('ad200_04', 6)	# 39-44
    label(0)
    sprite('ad000_00', 9)	# 45-53
    sprite('ad000_01', 9)	# 54-62
    sprite('ad000_02', 9)	# 63-71
    sprite('ad000_03', 9)	# 72-80
    sprite('ad000_04', 9)	# 81-89
    sprite('ad000_05', 9)	# 90-98
    sprite('ad000_06', 9)	# 99-107
    sprite('ad000_07', 9)	# 108-116
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 117-117

@State
def CmnActCrushAttackChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(0)
        DisableAttackRestOfMove()
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('keep', 3)	# 1-3
    sprite('ad201_00', 3)	# 4-6
    sprite('ad201_01', 6)	# 7-12
    sprite('ad201_02', 2)	# 13-14
    SFX_3('hit_m_fast')
    physicsXImpulse(10000)
    Unknown8007(0, 1, 1)
    sprite('ad201_03', 3)	# 15-17	 **attackbox here**
    RefreshMultihit()
    Unknown1019(50)
    sprite('ad201_04', 3)	# 18-20
    Unknown1019(50)
    sprite('ad201_05', 4)	# 21-24
    Unknown1019(50)
    Unknown8007(0, 1, 1)
    sprite('ad201_06', 4)	# 25-28
    Unknown1019(50)
    sprite('ad201_07', 4)	# 29-32
    Unknown1019(50)
    Unknown8007(0, 1, 1)
    sprite('ad201_08', 4)	# 33-36
    Unknown1019(50)
    sprite('ad201_09', 4)	# 37-40
    Unknown8010(0, 1, 1)
    Unknown1019(0)
    label(0)
    sprite('ad000_00', 9)	# 41-49
    sprite('ad000_01', 9)	# 50-58
    sprite('ad000_02', 9)	# 59-67
    sprite('ad000_03', 9)	# 68-76
    sprite('ad000_04', 9)	# 77-85
    sprite('ad000_05', 9)	# 86-94
    sprite('ad000_06', 9)	# 95-103
    sprite('ad000_07', 9)	# 104-112
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 113-113

@State
def CmnActCrushAttackFinish():

    def upon_IMMEDIATE():
        Unknown30075(0)
        DisableAttackRestOfMove()
    sprite('ad406_07', 3)	# 1-3
    sprite('ad406_08', 3)	# 4-6
    sprite('ad406_09', 3)	# 7-9
    sprite('ad406_10', 3)	# 10-12
    tag_voice(0, 'pad158_0', 'pad158_1', '', '')
    sprite('ad406_11', 7)	# 13-19
    Unknown23029(11, 2008, 0)
    GFX_1('persona_enter_ply', 1)
    SFX_3('persona_destroy')
    sprite('ad406_12', 6)	# 20-25	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    sprite('ad406_13', 5)	# 26-30
    sprite('ad406_14', 5)	# 31-35
    sprite('ad406_15', 5)	# 36-40
    sprite('ad406_13', 5)	# 41-45
    sprite('ad406_14', 5)	# 46-50
    sprite('ad406_01', 5)	# 51-55
    sprite('ad406_00', 5)	# 56-60

@State
def CmnActCrushAttackExFinish():

    def upon_IMMEDIATE():
        Unknown30089(0)
        DisableAttackRestOfMove()
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('ad000_00', 9)	# 1-9
    sprite('ad000_01', 9)	# 10-18
    sprite('ad000_02', 9)	# 19-27
    sprite('ad000_03', 9)	# 28-36
    sprite('ad000_04', 9)	# 37-45
    sprite('ad000_05', 9)	# 46-54
    sprite('ad000_06', 9)	# 55-63
    sprite('ad000_07', 9)	# 64-72
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad406_07', 3)	# 73-75
    sprite('ad406_08', 3)	# 76-78
    sprite('ad406_09', 3)	# 79-81
    sprite('ad406_10', 3)	# 82-84
    tag_voice(0, 'pad158_0', 'pad158_1', '', '')
    sprite('ad406_11', 7)	# 85-91
    Unknown23029(11, 2008, 0)
    GFX_1('persona_enter_ply', 1)
    SFX_3('persona_destroy')
    sprite('ad406_12', 6)	# 92-97	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    sprite('ad406_13', 5)	# 98-102
    sprite('ad406_14', 5)	# 103-107
    sprite('ad406_15', 5)	# 108-112
    sprite('ad406_13', 5)	# 113-117
    sprite('ad406_14', 5)	# 118-122
    sprite('ad406_01', 5)	# 123-127
    sprite('ad406_00', 5)	# 128-132

@State
def CmnActCrushAttackAssistChase1st():

    def upon_IMMEDIATE():
        Unknown30073(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('null', 23)	# 1-23
    Unknown1086(22)
    teleportRelativeY(0)
    sprite('null', 1)	# 24-24
    Unknown30081('')
    Unknown1086(22)
    teleportRelativeX(-1100000)
    Unknown1007(200000)
    setGravity(0)
    SLOT_12 = SLOT_19
    Unknown1019(10)
    sprite('ad400_05', 4)	# 25-28
    physicsXImpulse(65000)
    physicsYImpulse(15000)
    setGravity(3500)

    def upon_LANDING():
        clearUponHandler(2)
        sendToLabel(10)
    sprite('ad400_06', 4)	# 29-32
    Unknown1019(80)
    sprite('ad400_07', 4)	# 33-36
    Unknown1019(80)
    sprite('ad400_08', 32767)	# 37-32803
    Unknown1019(80)
    label(10)
    sprite('ad400_09', 3)	# 32804-32806	 **attackbox here**
    Unknown1084(1)
    Unknown8000(100, 1, 1)
    SFX_3('ad008')
    RefreshMultihit()
    GFX_0('adef_400_explosion', 100)
    sprite('ad400_10', 32767)	# 32807-65573
    GFX_0('ad400_Gun', 100)
    label(0)
    sprite('ad000_00', 9)	# 65574-65582
    sprite('ad000_01', 9)	# 65583-65591
    sprite('ad000_02', 9)	# 65592-65600
    sprite('ad000_03', 9)	# 65601-65609
    sprite('ad000_04', 9)	# 65610-65618
    sprite('ad000_05', 9)	# 65619-65627
    sprite('ad000_06', 9)	# 65628-65636
    sprite('ad000_07', 9)	# 65637-65645
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 65646-65646

@State
def CmnActCrushAttackAssistChase2nd():

    def upon_IMMEDIATE():
        Unknown30074(1)
        loopRelated(17, 180)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    sprite('ad400_10', 3)	# 1-3
    sprite('ad400_11', 4)	# 4-7
    sprite('ad400_12', 4)	# 8-11
    SFX_3('hit_m_fast')
    sprite('ad400_13', 3)	# 12-14	 **attackbox here**
    RefreshMultihit()
    sprite('ad400_14', 5)	# 15-19
    sprite('ad400_15', 5)	# 20-24
    sprite('ad231_09ex', 5)	# 25-29
    sprite('ad231_10ex', 5)	# 30-34
    label(0)
    sprite('ad000_00', 9)	# 35-43
    sprite('ad000_01', 9)	# 44-52
    sprite('ad000_02', 9)	# 53-61
    sprite('ad000_03', 9)	# 62-70
    sprite('ad000_04', 9)	# 71-79
    sprite('ad000_05', 9)	# 80-88
    sprite('ad000_06', 9)	# 89-97
    sprite('ad000_07', 9)	# 98-106
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('keep', 1)	# 107-107

@State
def CmnActCrushAttackAssistFinish():

    def upon_IMMEDIATE():
        Unknown30075(1)
    sprite('ad406_07', 3)	# 1-3
    sprite('ad406_08', 3)	# 4-6
    sprite('ad406_09', 3)	# 7-9
    sprite('ad406_10', 3)	# 10-12
    sprite('ad406_11', 7)	# 13-19
    Unknown23029(11, 2008, 0)
    GFX_1('persona_enter_ply', 1)
    SFX_3('persona_destroy')
    sprite('ad406_12', 6)	# 20-25	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    sprite('ad406_13', 5)	# 26-30
    sprite('ad406_14', 5)	# 31-35
    sprite('ad406_15', 5)	# 36-40
    sprite('ad406_13', 5)	# 41-45
    sprite('ad406_14', 5)	# 46-50
    sprite('ad406_01', 5)	# 51-55
    sprite('ad406_00', 5)	# 56-60

@State
def CmnActCrushAttackAssistExFinish():

    def upon_IMMEDIATE():
        Unknown30089(1)
        DisableAttackRestOfMove()
        loopRelated(17, 60)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
    label(0)
    sprite('ad000_00', 9)	# 1-9
    sprite('ad000_01', 9)	# 10-18
    sprite('ad000_02', 9)	# 19-27
    sprite('ad000_03', 9)	# 28-36
    sprite('ad000_04', 9)	# 37-45
    sprite('ad000_05', 9)	# 46-54
    sprite('ad000_06', 9)	# 55-63
    sprite('ad000_07', 9)	# 64-72
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad406_07', 3)	# 73-75
    sprite('ad406_08', 3)	# 76-78
    sprite('ad406_09', 3)	# 79-81
    sprite('ad406_10', 3)	# 82-84
    sprite('ad406_11', 7)	# 85-91
    Unknown23029(11, 2008, 0)
    GFX_1('persona_enter_ply', 1)
    SFX_3('persona_destroy')
    sprite('ad406_12', 6)	# 92-97	 **attackbox here**
    RefreshMultihit()
    SFX_3('hit_m_fast')
    sprite('ad406_13', 5)	# 98-102
    sprite('ad406_14', 5)	# 103-107
    sprite('ad406_15', 5)	# 108-112
    sprite('ad406_13', 5)	# 113-117
    sprite('ad406_14', 5)	# 118-122
    sprite('ad406_01', 5)	# 123-127
    sprite('ad406_00', 5)	# 128-132

@State
def NmlAtk2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtkChain2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('ad230_00', 2)	# 1-2
    sprite('ad230_01', 2)	# 3-4
    sprite('ad230_02', 2)	# 5-6
    Unknown1051(80)
    SFX_3('hit_l_fast')
    sprite('ad230_03', 3)	# 7-9	 **attackbox here**
    Unknown7009(0)
    sprite('ad230_04', 4)	# 10-13
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ad230_01', 4)	# 14-17
    sprite('ad230_00', 4)	# 18-21

@State
def NmlAtkChain2A():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(2)
        AttackP1(90)
        HitLow(2)
        WhiffCancel('NmlAtkChain2A')
        HitOrBlockCancel('NmlAtk5A')
        HitOrBlockCancel('NmlAtk2A')
        HitOrBlockCancel('NmlAtk5B')
        HitOrBlockCancel('NmlAtk2B')
        HitOrBlockCancel('CmnActCrushAttack')
        HitOrBlockCancel('NmlAtk2C')
        HitOrBlockCancel('NmlAtkThrow')
        HitOrBlockCancel('NmlAtkBackThrow')
    sprite('keep', 3)	# 1-3
    sprite('ad230_02', 3)	# 4-6
    Unknown1051(80)
    SFX_3('hit_l_fast')
    sprite('ad230_03', 3)	# 7-9	 **attackbox here**
    Unknown7009(0)
    sprite('ad230_04', 3)	# 10-12
    Recovery()
    Unknown2063()
    WhiffCancelEnable(1)
    sprite('ad230_01', 4)	# 13-16
    sprite('ad230_00', 4)	# 17-20

@State
def NmlAtk2B():

    def upon_IMMEDIATE():
        AttackDefaults_StandingNormal()
        AttackLevel_(3)
        Unknown11058('0000000001000000000000000000000000000000')
        AttackP1(90)
        AttackP2(70)
        AirPushbackX(10000)
        AirPushbackY(30000)
        AirHitstunAnimation(9)
        GroundedHitstunAnimation(9)
        Unknown18009(1)
        HitOrBlockJumpCancel(1)

        def upon_LANDING():
            clearUponHandler(2)
            Unknown1084(1)
            sendToLabel(1)

        def upon_STATE_END():
            Unknown1019(80)
            YAccel(80)
            Unknown1043()

        def upon_78():
            HitCancel('NmlAtk2BB')
    sprite('ad231_00', 3)	# 1-3
    sprite('ad231_01', 3)	# 4-6
    sprite('ad231_02', 3)	# 7-9
    setInvincible(1)
    Unknown22019('0100000000000000000000000000000000000000')
    sprite('ad231_03', 3)	# 10-12
    SFX_3('hit_m_fast')
    physicsXImpulse(16000)
    Unknown7007('7061643130365f300000000000000000640000007061643130365f310000000000000000640000007061643130365f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ad231_04', 5)	# 13-17	 **attackbox here**
    Unknown8001(1, 0)
    Unknown1028(-400)
    physicsXImpulse(12000)
    physicsYImpulse(28000)
    setGravity(3000)
    RefreshMultihit()
    Unknown18009(0)
    sprite('ad231_05', 3)	# 18-20
    setInvincible(0)
    Recovery()
    Unknown2063()
    sprite('ad231_06', 30)	# 21-50
    label(1)
    sprite('ad231_07', 2)	# 51-52
    sprite('ad231_08', 6)	# 53-58
    sprite('ad231_09', 4)	# 59-62
    sprite('ad231_10', 4)	# 63-66

@State
def NmlAtk2BB():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        JumpCancel_(0)

        def upon_43():
            if (SLOT_48 == 2017):
                loopRelated(17, 60)

                def upon_17():
                    clearUponHandler(17)

                    def upon_LANDING():
                        clearUponHandler(2)
                        Unknown1084(1)
                        sendToLabel(20)
                    sendToLabel(10)
                Unknown1084(1)
                Unknown13045(0)
                sendToLabel(1)
            if (SLOT_48 == 2018):
                JumpCancel_(1)
    sprite('ad252_00', 3)	# 1-3
    sprite('ad252_01', 6)	# 4-9
    Unknown7007('6164313036000000000000000000000064000000616431303700000000000000000000006400000061643130380000000000000000000000640000006164313039000000000000000000000064000000')
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ad252_01', 1)	# 10-10
    Unknown23029(11, 2006, 0)
    sprite('ad252_02', 3)	# 11-13
    sprite('ad252_03', 4)	# 14-17
    GFX_1('persona_enter_ply', 0)
    sprite('ad252_04', 4)	# 18-21
    sprite('ad252_05', 4)	# 22-25
    sprite('ad252_03', 4)	# 26-29
    sprite('ad252_04', 4)	# 30-33
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    sprite('ad252_05', 4)	# 34-37
    sprite('ad252_03', 4)	# 38-41
    sprite('ad252_06', 5)	# 42-46
    sprite('ad252_07', 5)	# 47-51
    ExitState()
    label(1)
    sprite('ad252_03', 4)	# 52-55
    sprite('ad252_04', 4)	# 56-59
    sprite('ad252_05', 4)	# 60-63
    loopRest()
    gotoLabel(1)
    label(10)
    sprite('ad252_06', 5)	# 64-68
    Unknown1018()
    Unknown1019(85)
    physicsYImpulse(10000)
    Unknown1043()
    sprite('ad252_07', 5)	# 69-73
    sprite('ad020_05', 3)	# 74-76
    sprite('ad020_06', 3)	# 77-79
    label(11)
    sprite('ad020_07', 4)	# 80-83
    sprite('ad020_08', 4)	# 84-87
    loopRest()
    gotoLabel(11)
    label(20)
    sprite('ad010_00', 3)	# 88-90
    sprite('ad010_01', 3)	# 91-93
    sprite('ad010_02', 6)	# 94-99
    sprite('ad010_01', 6)	# 100-105
    sprite('ad010_00', 6)	# 106-111
    ExitState()

@State
def NmlAtk2C():

    def upon_IMMEDIATE():
        AttackDefaults_CrouchingNormal()
        AttackLevel_(4)
        AttackP1(90)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        blockstun(20)
        AirPushbackX(5000)
        AirPushbackY(20500)
        AirUntechableTime(30)
        HitLow(2)
    sprite('ad210_00', 2)	# 1-2
    sprite('ad210_01', 2)	# 3-4
    sprite('ad210_02', 2)	# 5-6
    Unknown8007(100, 1, 0)
    physicsXImpulse(30000)
    sprite('ad210_03', 1)	# 7-7
    Unknown8007(100, 1, 0)
    sprite('ad211_00', 2)	# 8-9
    Unknown8010(0, 1, 1)
    Unknown7007('7061643130375f300000000000000000640000007061643130375f310000000000000000640000007061643130375f320000000000000000640000000000000000000000000000000000000000000000')
    sprite('ad211_01', 2)	# 10-11
    Unknown1019(75)
    sprite('ad211_02', 2)	# 12-13
    SFX_3('hit_m_fast')
    Unknown1019(75)
    sprite('ad211_03', 3)	# 14-16	 **attackbox here**
    Unknown1019(50)
    sprite('ad211_04', 4)	# 17-20
    Unknown1019(0)
    Recovery()
    Unknown2063()
    sprite('ad211_05', 4)	# 21-24
    sprite('ad211_06', 4)	# 25-28
    sprite('ad211_07', 4)	# 29-32
    sprite('ad211_08', 6)	# 33-38

@State
def NmlAtkAIR5A():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtkAIR5AA')
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ad251_00', 2)	# 1-2
    sprite('ad251_01', 2)	# 3-4
    sprite('ad251_02', 3)	# 5-7
    SFX_3('hit_m_fast')
    sprite('ad251_03', 3)	# 8-10	 **attackbox here**
    Unknown7009(1)
    sprite('ad251_04', 3)	# 11-13	 **attackbox here**
    sprite('ad251_05', 3)	# 14-16
    sprite('ad251_06', 3)	# 17-19
    sprite('ad251_07', 3)	# 20-22
    sprite('ad251_08', 3)	# 23-25

@State
def NmlAtkAIR5AA():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        AttackLevel_(3)
        HitOrBlockCancel('NmlAtkAIR5B')
        HitOrBlockCancel('NmlAtkAIR5C')
        HitOrBlockJumpCancel(1)
    sprite('ad250_00', 3)	# 1-3
    sprite('ad250_01', 2)	# 4-5
    sprite('ad250_02', 2)	# 6-7
    SFX_3('hit_l_fast')
    sprite('ad250_03', 3)	# 8-10	 **attackbox here**
    Unknown7009(3)
    sprite('ad250_04', 3)	# 11-13
    sprite('ad250_05', 3)	# 14-16
    sprite('ad250_05', 3)	# 17-19

@State
def NmlAtkAIR5B():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
        Unknown4009(11)

        def upon_LANDING():
            Unknown23029(11, 9001, 0)

        def upon_STATE_END():
            Unknown23029(11, 9002, 0)
            Unknown4009(0)

        def upon_43():
            if (SLOT_48 == 2015):
                Recovery()
                Unknown2063()
    sprite('ad252_00', 3)	# 1-3
    sprite('ad252_01', 6)	# 4-9
    Unknown7009(2)
    Unknown23029(11, 2005, 0)
    GFX_1('persona_enter_ply', 0)
    sprite('ad252_02', 3)	# 10-12
    sprite('ad252_03', 4)	# 13-16
    sprite('ad252_04', 4)	# 17-20
    sprite('ad252_05', 4)	# 21-24
    sprite('ad252_03', 4)	# 25-28
    sprite('ad252_04', 4)	# 29-32
    sprite('ad252_05', 4)	# 33-36
    sprite('ad252_03', 4)	# 37-40
    sprite('ad252_04', 4)	# 41-44
    sprite('ad252_06', 5)	# 45-49
    sprite('ad252_07', 5)	# 50-54

@State
def NmlAtkAIR5C():

    def upon_IMMEDIATE():
        AttackDefaults_AirNormal()
    sprite('ad252_00', 3)	# 1-3
    sprite('ad252_01', 6)	# 4-9
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)
    sprite('ad252_01', 1)	# 10-10
    Unknown7009(2)
    Unknown23029(11, 2007, 0)
    sprite('ad252_02', 3)	# 11-13
    sprite('ad252_03', 4)	# 14-17
    GFX_1('persona_enter_ply', 0)
    sprite('ad252_04', 4)	# 18-21
    sprite('ad252_05', 4)	# 22-25
    sprite('ad252_03', 4)	# 26-29
    sprite('ad252_04', 4)	# 30-33
    Unknown2001()
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)
    sprite('ad252_05', 4)	# 34-37
    sprite('ad252_03', 4)	# 38-41
    sprite('ad252_06', 5)	# 42-46
    sprite('ad252_07', 5)	# 47-51

@Subroutine
def ThrowApproachInit():
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

@State
def NmlAtkThrow():

    def upon_IMMEDIATE():
        Unknown17011('ThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ad032_00', 4)	# 1-4
    label(0)
    sprite('ad032_01', 4)	# 5-8
    sprite('ad032_02', 4)	# 9-12
    sprite('ad032_03', 4)	# 13-16
    Unknown8006(100, 1, 1)
    sprite('ad032_04', 4)	# 17-20
    sprite('ad032_05', 4)	# 21-24
    sprite('ad032_06', 4)	# 25-28
    sprite('ad032_07', 4)	# 29-32
    Unknown8006(100, 1, 1)
    sprite('ad032_08', 4)	# 33-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad310_00', 2)	# 37-38
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ad310_01', 1)	# 39-39
    sprite('ad310_02', 3)	# 40-42	 **attackbox here**
    SFX_3('hit_l_fast')
    RefreshMultihit()
    sprite('ad310_03', 4)	# 43-46
    Unknown1084(1)
    sprite('ad310_04', 9)	# 47-55
    SFX_1('pad154')
    sprite('ad310_05', 5)	# 56-60
    sprite('ad310_00', 5)	# 61-65

@State
def ThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(2000)
        AttackP2(50)
        AirUntechableTime(50)
        Hitstop(3)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(25000)
        YImpluseBeforeWallbounce(2500)
        Unknown9310(60)
    sprite('ad310_02', 3)	# 1-3	 **attackbox here**
    SFX_3('hit_l_fast')
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ad310_02', 6)	# 4-9	 **attackbox here**
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    sprite('ad311_00', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('ad311_01', 6)	# 13-18
    sprite('ad311_01', 5)	# 19-23
    sprite('ad311_01', 5)	# 24-28
    sprite('ad311_02', 5)	# 29-33
    SFX_1('pad153')
    sprite('ad311_03', 5)	# 34-38
    sprite('ad311_04', 5)	# 39-43
    sprite('ad311_05', 5)	# 44-48
    sprite('ad311_06', 5)	# 49-53
    sprite('ad311_07', 5)	# 54-58
    sprite('ad311_05', 5)	# 59-63
    sprite('ad311_06', 5)	# 64-68
    sprite('ad311_07', 5)	# 69-73
    sprite('ad311_05', 5)	# 74-78
    sprite('ad311_06', 5)	# 79-83
    sprite('ad311_07', 5)	# 84-88
    sprite('ad311_08', 5)	# 89-93

@State
def NmlAtkBackThrow():

    def upon_IMMEDIATE():
        Unknown17011('BackThrowExe', 1, 0, 0)
        Unknown11054(120000)
        callSubroutine('ThrowApproachInit')
    sprite('ad032_00', 4)	# 1-4
    label(0)
    sprite('ad032_01', 4)	# 5-8
    sprite('ad032_02', 4)	# 9-12
    sprite('ad032_03', 4)	# 13-16
    Unknown8006(100, 1, 1)
    sprite('ad032_04', 4)	# 17-20
    sprite('ad032_05', 4)	# 21-24
    sprite('ad032_06', 4)	# 25-28
    sprite('ad032_07', 4)	# 29-32
    Unknown8006(100, 1, 1)
    sprite('ad032_08', 4)	# 33-36
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad310_00', 2)	# 37-38
    clearUponHandler(3)
    Unknown1019(10)
    Unknown8010(100, 1, 1)
    sprite('ad310_01', 1)	# 39-39
    sprite('ad310_02', 3)	# 40-42	 **attackbox here**
    SFX_3('hit_l_fast')
    RefreshMultihit()
    sprite('ad310_03', 4)	# 43-46
    Unknown1084(1)
    sprite('ad310_04', 9)	# 47-55
    SFX_1('pad154')
    sprite('ad310_05', 5)	# 56-60
    sprite('ad310_00', 5)	# 61-65

@State
def BackThrowExe():

    def upon_IMMEDIATE():
        Unknown17012(1, 0, 0)
        AttackLevel_(2)
        Damage(2000)
        AttackP2(50)
        AirUntechableTime(50)
        Hitstop(3)
        AirHitstunAnimation(11)
        GroundedHitstunAnimation(11)
        AirPushbackX(3000)
        AirPushbackY(25000)
        YImpluseBeforeWallbounce(2500)
        Unknown9310(60)
    sprite('ad310_02', 3)	# 1-3	 **attackbox here**
    SFX_3('hit_l_fast')
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000000000000')
    StartMultihit()
    Unknown5003(1)
    sprite('ad310_02', 6)	# 4-9	 **attackbox here**
    Unknown2005()
    Unknown5000(8, 0)
    Unknown5001('0000000004000000040000000000000008000000')
    StartMultihit()
    sprite('ad311_00', 3)	# 10-12	 **attackbox here**
    RefreshMultihit()
    sprite('ad311_01', 6)	# 13-18
    sprite('ad311_01', 5)	# 19-23
    sprite('ad311_01', 5)	# 24-28
    sprite('ad311_02', 5)	# 29-33
    SFX_1('pad153')
    sprite('ad311_03', 5)	# 34-38
    sprite('ad311_04', 5)	# 39-43
    sprite('ad311_05', 5)	# 44-48
    sprite('ad311_06', 5)	# 49-53
    sprite('ad311_07', 5)	# 54-58
    sprite('ad311_05', 5)	# 59-63
    sprite('ad311_06', 5)	# 64-68
    sprite('ad311_07', 5)	# 69-73
    sprite('ad311_05', 5)	# 74-78
    sprite('ad311_06', 5)	# 79-83
    sprite('ad311_07', 5)	# 84-88
    sprite('ad311_08', 5)	# 89-93

@State
def CmnActInvincibleAttack():

    def upon_IMMEDIATE():
        Unknown17024('')
        Unknown11063(1)
        Unknown1051(30)
        GuardPoint_(1)
        Unknown22031(-1, 17)
        SLOT_59 = 0

        def upon_42():
            SLOT_59 = 1
            Unknown1084(1)
            Unknown23022(1)
            ScreenShake(8000, 2000)
            sendToLabel(0)
    sprite('ad030_01', 3)	# 1-3
    physicsXImpulse(4000)
    sprite('ad030_02', 6)	# 4-9
    tag_voice(1, 'pad200_0', 'pad200_1', 'pad200_2', '')
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ad030_03', 6)	# 10-15
    sprite('ad030_04', 6)	# 16-21
    sprite('ad030_05', 4)	# 22-25
    sprite('ad030_05', 2)	# 26-27
    setInvincible(0)
    sprite('ad030_06', 6)	# 28-33
    sprite('ad030_07', 6)	# 34-39
    SFX_FOOTSTEP_(100, 1, 1)
    sprite('ad030_08', 6)	# 40-45
    sprite('keep', 10)	# 46-55
    enterState('CmnActInvincibleAttackCounter')
    ExitState()
    label(0)
    sprite('keep', 10)	# 56-65
    sprite('keep', 10)	# 66-75
    enterState('CmnActInvincibleAttackCounter')

@State
def CmnActInvincibleAttackCounter():

    def upon_IMMEDIATE():
        Unknown17024('')
        AttackLevel_(4)
        Damage(2300)
        AirUntechableTime(60)
        AirPushbackX(30000)
        AirPushbackY(28000)
        GroundedHitstunAnimation(1)
        Unknown2004(1, 0)
        callSubroutine('InvSkillInit')
        Unknown30068(1)
        Unknown14083(0)

        def upon_11():
            clearUponHandler(11)
            sendToLabel(1)
        Unknown3029(1)
        Unknown3069(2)
        Unknown3072('60000000000000000000000000000000')
        Unknown3073('00000000000000000000000000000000')
        Unknown3074('00000000dc0000002000000000000000')
        Unknown3075('00000000800000000000000020000000')
        Unknown3076(1010)
        Unknown3077(1000)
        if SLOT_59:
            setInvincible(1)

        def upon_STATE_END():
            SLOT_59 = 0
    sprite('ad401_00', 1)	# 1-1
    sprite('ad401_01', 2)	# 2-3
    sprite('ad401_02', 3)	# 4-6	 **attackbox here**
    SFX_3('airdash_l')
    physicsXImpulse(50000)
    RefreshMultihit()
    GFX_0('adef_401_dash', 100)
    sprite('ad401_03', 3)	# 7-9	 **attackbox here**
    sprite('ad401_02', 3)	# 10-12	 **attackbox here**
    SFX_3('airdash_l')
    label(1)
    sprite('keep', 3)	# 13-15
    StartMultihit()
    sprite('ad401_04', 6)	# 16-21
    setInvincible(0)
    SFX_3('airdash_l')
    Unknown1019(75)
    sprite('ad401_05', 6)	# 22-27
    Unknown1019(50)
    sprite('ad401_06', 6)	# 28-33
    Unknown1019(50)
    sprite('ad401_07', 6)	# 34-39
    Unknown1019(50)
    sprite('ad401_08', 6)	# 40-45
    Unknown1019(50)
    sprite('ad401_09', 6)	# 46-51
    Unknown1019(50)

@State
def SpecialShotFastLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ad205_00', 3)	# 1-3
    sprite('ad205_01', 3)	# 4-6
    tag_voice(1, 'pad120_2', 'pad123_2', 'pad124_2', '')
    sprite('ad205_02', 2)	# 7-8
    GFX_1('persona_enter_ply', 0)
    sprite('ad205_02', 1)	# 9-9
    Unknown23029(11, 3001, 0)
    sprite('ad205_03', 3)	# 10-12
    sprite('ad205_04', 3)	# 13-15
    sprite('ad205_05', 3)	# 16-18
    sprite('ad205_06', 3)	# 19-21
    sprite('ad205_04', 3)	# 22-24
    sprite('ad205_05', 3)	# 25-27
    sprite('ad205_06', 3)	# 28-30
    sprite('ad205_04', 4)	# 31-34
    sprite('ad205_05', 4)	# 35-38
    sprite('ad205_06', 4)	# 39-42
    sprite('ad205_04', 5)	# 43-47
    sprite('ad205_05', 5)	# 48-52
    sprite('ad205_06', 5)	# 53-57
    sprite('ad205_01', 6)	# 58-63
    sprite('ad205_00', 6)	# 64-69

@State
def SpecialShotSlowLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
    sprite('ad205_00', 3)	# 1-3
    sprite('ad205_01', 3)	# 4-6
    tag_voice(1, 'pad120_2', 'pad123_2', 'pad124_2', '')
    sprite('ad205_02', 2)	# 7-8
    GFX_1('persona_enter_ply', 0)
    sprite('ad205_02', 1)	# 9-9
    Unknown23029(11, 3002, 0)
    sprite('ad205_03', 3)	# 10-12
    sprite('ad205_04', 3)	# 13-15
    sprite('ad205_05', 3)	# 16-18
    sprite('ad205_06', 3)	# 19-21
    sprite('ad205_04', 3)	# 22-24
    sprite('ad205_05', 3)	# 25-27
    sprite('ad205_06', 3)	# 28-30
    sprite('ad205_04', 4)	# 31-34
    sprite('ad205_05', 4)	# 35-38
    sprite('ad205_06', 4)	# 39-42
    sprite('ad205_04', 5)	# 43-47
    sprite('ad205_05', 5)	# 48-52
    sprite('ad205_06', 5)	# 53-57
    sprite('ad205_01', 6)	# 58-63
    sprite('ad205_00', 6)	# 64-69

@State
def SpecialSearchShotLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 3511):
                Recovery()
    sprite('ad233_00', 3)	# 1-3
    sprite('ad233_01', 3)	# 4-6
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 3501, 0)
    tag_voice(1, 'pad121_0', 'pad122_0', 'pad123_0', '')
    Unknown18009(1)
    sprite('ad233_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    sprite('ad233_03', 3)	# 10-12
    sprite('ad233_04', 3)	# 13-15
    sprite('ad233_05', 3)	# 16-18
    sprite('ad233_06', 3)	# 19-21
    sprite('ad233_04', 4)	# 22-25
    sprite('ad233_05', 4)	# 26-29
    sprite('ad233_06', 4)	# 30-33
    sprite('ad233_04', 5)	# 34-38
    sprite('ad233_05', 5)	# 39-43
    sprite('ad233_06', 5)	# 44-48
    sprite('ad233_01', 4)	# 49-52
    sprite('ad233_00', 4)	# 53-56

@Subroutine
def SpecialShotAirPushSpeed():
    Unknown1017()
    Unknown1022()
    Unknown1037()
    Unknown1084(1)

@Subroutine
def SpecialShotAirPopSpeed():
    Unknown1018()
    Unknown1023()
    Unknown1038()
    Unknown1019(85)
    YAccel(85)

@State
def SpecialShotFastAir():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ad253_00', 3)	# 1-3
    sprite('ad253_01', 3)	# 4-6
    callSubroutine('SpecialShotAirPushSpeed')
    Unknown23029(11, 3001, 0)
    tag_voice(1, 'pad120_2', 'pad123_2', 'pad124_2', '')
    sprite('ad253_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    sprite('ad253_03', 3)	# 10-12
    sprite('ad253_04', 3)	# 13-15
    sprite('ad253_05', 3)	# 16-18
    sprite('ad253_06', 3)	# 19-21
    sprite('ad253_04', 3)	# 22-24
    sprite('ad253_05', 3)	# 25-27
    sprite('ad253_06', 3)	# 28-30
    sprite('ad253_04', 4)	# 31-34
    sprite('ad253_05', 4)	# 35-38
    sprite('ad253_06', 4)	# 39-42
    sprite('ad253_04', 5)	# 43-47
    sprite('ad253_05', 5)	# 48-52
    sprite('ad253_06', 5)	# 53-57
    sprite('ad253_01', 4)	# 58-61
    callSubroutine('SpecialShotAirPopSpeed')
    sprite('ad253_00', 4)	# 62-65

@State
def SpecialShotSlowAir():

    def upon_IMMEDIATE():
        Unknown17003()
    sprite('ad253_00', 3)	# 1-3
    sprite('ad253_01', 3)	# 4-6
    callSubroutine('SpecialShotAirPushSpeed')
    Unknown23029(11, 3002, 0)
    tag_voice(1, 'pad120_2', 'pad123_2', 'pad124_2', '')
    sprite('ad253_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    sprite('ad253_03', 3)	# 10-12
    sprite('ad253_04', 3)	# 13-15
    sprite('ad253_05', 3)	# 16-18
    sprite('ad253_06', 3)	# 19-21
    sprite('ad253_04', 3)	# 22-24
    sprite('ad253_05', 3)	# 25-27
    sprite('ad253_06', 3)	# 28-30
    sprite('ad253_04', 4)	# 31-34
    sprite('ad253_05', 4)	# 35-38
    sprite('ad253_06', 4)	# 39-42
    sprite('ad253_04', 5)	# 43-47
    sprite('ad253_05', 5)	# 48-52
    sprite('ad253_06', 5)	# 53-57
    sprite('ad253_01', 6)	# 58-63
    callSubroutine('SpecialShotAirPopSpeed')
    sprite('ad253_00', 6)	# 64-69

@State
def SpecialSearchShotAir():

    def upon_IMMEDIATE():
        Unknown17003()

        def upon_43():
            if (SLOT_48 == 3511):
                Recovery()
    sprite('ad253_00', 3)	# 1-3
    sprite('ad253_01', 3)	# 4-6
    callSubroutine('SpecialShotAirPushSpeed')
    Unknown23125('')
    ConsumeSuperMeter(-5000)
    Unknown23029(11, 3501, 0)
    tag_voice(1, 'pad121_0', 'pad122_0', 'pad123_0', '')
    sprite('ad253_02', 3)	# 7-9
    GFX_1('persona_enter_ply', 0)
    sprite('ad253_03', 3)	# 10-12
    sprite('ad253_04', 3)	# 13-15
    sprite('ad253_05', 3)	# 16-18
    sprite('ad253_06', 3)	# 19-21
    sprite('ad253_04', 4)	# 22-25
    sprite('ad253_05', 4)	# 26-29
    sprite('ad253_06', 4)	# 30-33
    sprite('ad253_04', 5)	# 34-38
    sprite('ad253_05', 5)	# 39-43
    sprite('ad253_06', 5)	# 44-48
    sprite('ad253_01', 6)	# 49-54
    callSubroutine('SpecialShotAirPopSpeed')
    sprite('ad253_00', 6)	# 55-60

@State
def SpecialAntiAirFast():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        loopRelated(17, 65)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)

        def upon_43():
            if (SLOT_48 == 3017):
                loopRelated(17, 90)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(1)
            if (SLOT_48 == 3011):
                Recovery()
    sprite('ad432_00', 3)	# 1-3
    sprite('ad432_01', 5)	# 4-8
    tag_voice(1, 'pad204_0', 'pad204_1', 'pad204_2', '')
    Unknown23029(11, 3003, 0)
    sprite('ad432_02', 5)	# 9-13
    sprite('ad432_00', 5)	# 14-18
    sprite('ad432_03', 3)	# 19-21
    sprite('ad432_04', 3)	# 22-24
    sprite('ad432_05', 3)	# 25-27
    sprite('ad432_06', 3)	# 28-30
    sprite('ad432_07', 6)	# 31-36
    sprite('ad432_08', 1)	# 37-37
    GFX_1('persona_enter_ply', 0)
    sprite('ad432_08', 5)	# 38-42
    sprite('ad432_09', 6)	# 43-48
    sprite('ad432_10', 6)	# 49-54
    label(0)
    sprite('ad432_08', 6)	# 55-60
    sprite('ad432_09', 6)	# 61-66
    sprite('ad432_10', 6)	# 67-72
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad432_11', 6)	# 73-78
    sprite('ad432_12', 6)	# 79-84

@State
def SpecialAntiAirSlow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()

        def upon_43():
            if (SLOT_48 == 3014):
                loopRelated(17, 160)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(10)
                sendToLabel(1)
            if (SLOT_48 == 3012):
                Recovery()
    sprite('ad434_00', 3)	# 1-3
    sprite('ad434_00', 3)	# 4-6
    tag_voice(1, 'pad205_0', 'pad205_1', 'pad205_2', '')
    Unknown23029(11, 3004, 0)
    sprite('ad434_01', 6)	# 7-12
    sprite('ad434_02', 6)	# 13-18
    sprite('ad434_03', 6)	# 19-24
    sprite('ad434_04', 4)	# 25-28
    sprite('ad434_05', 4)	# 29-32
    sprite('ad434_06', 4)	# 33-36
    sprite('ad434_04', 4)	# 37-40
    sprite('ad434_05', 4)	# 41-44
    sprite('ad434_06', 4)	# 45-48
    sprite('ad434_04', 5)	# 49-53
    sprite('ad434_05', 5)	# 54-58
    sprite('ad434_06', 5)	# 59-63
    sprite('ad434_04', 5)	# 64-68
    sprite('ad434_05', 5)	# 69-73
    sprite('ad434_06', 5)	# 74-78
    sprite('ad434_07', 6)	# 79-84
    sprite('ad434_08', 6)	# 85-90
    ExitState()
    label(1)
    sprite('keep', 2)	# 91-92
    label(2)
    sprite('ad434_04', 6)	# 93-98
    sprite('ad434_05', 6)	# 99-104
    sprite('ad434_06', 6)	# 105-110
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('keep', 2)	# 111-112
    sprite('ad434_07', 6)	# 113-118
    sprite('ad434_08', 6)	# 119-124

@State
def SpecialThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingSpecial()
        Unknown14083(0)

        def upon_43():
            if (SLOT_48 == 3015):
                Unknown23022(1)
                Unknown13045(0)
                loopRelated(17, 210)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(10)
                sendToLabel(1)
            if (SLOT_48 == 3013):
                Recovery()
            if (SLOT_48 == 3016):
                Unknown14083(1)
                tag_voice(0, 'pad207_0', 'pad207_1', 'pad207_2', '')
    sprite('ad433_00', 3)	# 1-3
    sprite('ad433_01', 5)	# 4-8
    Unknown23029(11, 3005, 0)
    sprite('ad433_02', 5)	# 9-13
    sprite('ad433_03', 3)	# 14-16
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(16200)
    physicsYImpulse(-1800)
    Unknown35()
    sprite('ad433_04', 3)	# 17-19
    sprite('ad433_05', 3)	# 20-22
    sprite('ad433_06', 2)	# 23-24
    sprite('ad433_07', 3)	# 25-27
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('ad433_08', 5)	# 28-32
    sprite('ad433_09', 5)	# 33-37
    sprite('ad433_10', 5)	# 38-42
    sprite('ad433_08', 5)	# 43-47
    sprite('ad433_09', 5)	# 48-52
    sprite('ad433_10', 5)	# 53-57
    sprite('ad433_01', 5)	# 58-62
    sprite('ad433_00', 5)	# 63-67
    ExitState()
    label(1)
    sprite('ad433_07', 15)	# 68-82
    tag_voice(1, 'pad206_0', 'pad206_1', 'pad206_2', '')
    sprite('ad433_11', 6)	# 83-88
    label(2)
    sprite('ad433_12', 7)	# 89-95
    sprite('ad433_13', 7)	# 96-102
    sprite('ad433_14', 7)	# 103-109
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('ad433_01', 7)	# 110-116
    sprite('ad433_00', 7)	# 117-123

@State
def UltimateAsasultLand():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        loopRelated(17, 163)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4011):
                setInvincible(0)
    sprite('ad430_00', 3)	# 1-3
    sprite('ad430_01', 4)	# 4-7
    sprite('ad430_02', 4)	# 8-11
    Unknown7007('7061643235305f300000000000000000640000007061643235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    Unknown2036(53, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown23029(11, 4001, 0)
    sprite('ad430_03', 4)	# 12-15
    sprite('ad430_01', 4)	# 16-19
    sprite('ad430_02', 4)	# 20-23
    sprite('ad430_03', 4)	# 24-27
    sprite('ad430_01', 4)	# 28-31
    sprite('ad430_02', 4)	# 32-35
    sprite('ad430_04', 3)	# 36-38
    sprite('ad430_05', 10)	# 39-48
    sprite('ad430_06', 6)	# 49-54
    sprite('ad430_07', 6)	# 55-60
    GFX_1('persona_enter_ply', 0)
    sprite('ad430_08', 6)	# 61-66
    sprite('ad430_09', 6)	# 67-72
    label(0)
    sprite('ad430_07', 6)	# 73-78
    sprite('ad430_08', 6)	# 79-84
    sprite('ad430_09', 6)	# 85-90
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad430_01', 6)	# 91-96
    sprite('ad430_00', 6)	# 97-102

@State
def UltimateAsasultLandSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        loopRelated(17, 190)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4011):
                setInvincible(0)
    sprite('ad430_00', 3)	# 1-3
    sprite('ad430_01', 4)	# 4-7
    sprite('ad430_02', 4)	# 8-11
    Unknown7007('7061643235305f300000000000000000640000007061643235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    Unknown2036(53, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown23029(11, 4021, 0)
    sprite('ad430_03', 4)	# 12-15
    sprite('ad430_01', 4)	# 16-19
    sprite('ad430_02', 4)	# 20-23
    sprite('ad430_03', 4)	# 24-27
    sprite('ad430_01', 4)	# 28-31
    sprite('ad430_02', 4)	# 32-35
    sprite('ad430_04', 3)	# 36-38
    sprite('ad430_05', 10)	# 39-48
    sprite('ad430_06', 6)	# 49-54
    sprite('ad430_07', 6)	# 55-60
    GFX_1('persona_enter_ply', 0)
    sprite('ad430_08', 6)	# 61-66
    sprite('ad430_09', 6)	# 67-72
    label(0)
    sprite('ad430_07', 6)	# 73-78
    sprite('ad430_08', 6)	# 79-84
    sprite('ad430_09', 6)	# 85-90
    loopRest()
    gotoLabel(0)
    label(1)
    sprite('ad430_01', 6)	# 91-96
    sprite('ad430_00', 6)	# 97-102

@State
def UltimateAsasultAir():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        setInvincible(1)
        Unknown1017()
        Unknown1084(1)
        loopRelated(17, 146)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4011):
                setInvincible(0)
    sprite('ad430_10', 3)	# 1-3
    sprite('ad430_11', 4)	# 4-7
    sprite('ad430_12', 4)	# 8-11
    Unknown7007('7061643235305f300000000000000000640000007061643235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    Unknown2036(53, -1, 0)
    ConsumeSuperMeter(-10000)
    GFX_0('UltimateAirAssaultAsiba', 100)
    Unknown23029(11, 4001, 0)
    sprite('ad430_13', 4)	# 12-15
    sprite('ad430_11', 4)	# 16-19
    sprite('ad430_12', 4)	# 20-23
    sprite('ad430_13', 4)	# 24-27
    sprite('ad430_11', 4)	# 28-31
    sprite('ad430_12', 4)	# 32-35
    sprite('ad430_14', 3)	# 36-38
    sprite('ad430_05ex', 10)	# 39-48
    sprite('ad430_06ex', 6)	# 49-54
    sprite('ad430_07ex', 6)	# 55-60
    GFX_1('persona_enter_ply', 0)
    sprite('ad430_08ex', 6)	# 61-66
    sprite('ad430_09ex', 6)	# 67-72
    label(0)
    sprite('ad430_07ex', 6)	# 73-78
    sprite('ad430_08ex', 6)	# 79-84
    sprite('ad430_09ex', 6)	# 85-90
    gotoLabel(0)
    label(1)
    sprite('ad430_15', 4)	# 91-94
    sprite('ad430_16', 4)	# 95-98
    sprite('ad020_04', 4)	# 99-102
    Unknown21012('556c74696d61746541697241737361756c74417369626100000000000000000020000000')
    Unknown1018()
    Unknown1019(70)
    physicsYImpulse(14000)
    setGravity(2000)
    Unknown22004(5, 5)
    sprite('ad020_05', 4)	# 103-106
    sprite('ad020_06', 4)	# 107-110
    label(2)
    sprite('ad020_07', 4)	# 111-114
    sprite('ad020_08', 4)	# 115-118
    gotoLabel(2)

@State
def UltimateAsasultAirSP():

    def upon_IMMEDIATE():
        AttackDefaults_AirDD()
        Unknown23055('')
        setInvincible(1)
        Unknown1017()
        Unknown1084(1)
        loopRelated(17, 173)

        def upon_17():
            clearUponHandler(17)
            sendToLabel(1)
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4011):
                setInvincible(0)
    sprite('ad430_10', 3)	# 1-3
    sprite('ad430_11', 4)	# 4-7
    sprite('ad430_12', 4)	# 8-11
    Unknown7007('7061643235305f300000000000000000640000007061643235305f3100000000000000006400000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    Unknown30080('')
    Unknown2036(53, -1, 0)
    ConsumeSuperMeter(-10000)
    GFX_0('UltimateAirAssaultAsiba', 100)
    Unknown23029(11, 4021, 0)
    sprite('ad430_13', 4)	# 12-15
    sprite('ad430_11', 4)	# 16-19
    sprite('ad430_12', 4)	# 20-23
    sprite('ad430_13', 4)	# 24-27
    sprite('ad430_11', 4)	# 28-31
    sprite('ad430_12', 4)	# 32-35
    sprite('ad430_14', 3)	# 36-38
    sprite('ad430_05ex', 10)	# 39-48
    sprite('ad430_06ex', 6)	# 49-54
    sprite('ad430_07ex', 6)	# 55-60
    GFX_1('persona_enter_ply', 0)
    sprite('ad430_08ex', 6)	# 61-66
    sprite('ad430_09ex', 6)	# 67-72
    label(0)
    sprite('ad430_07ex', 6)	# 73-78
    sprite('ad430_08ex', 6)	# 79-84
    sprite('ad430_09ex', 6)	# 85-90
    gotoLabel(0)
    label(1)
    sprite('ad430_15', 4)	# 91-94
    sprite('ad430_16', 4)	# 95-98
    sprite('ad020_04', 4)	# 99-102
    Unknown21012('556c74696d61746541697241737361756c74417369626100000000000000000020000000')
    Unknown1018()
    Unknown1019(70)
    physicsYImpulse(14000)
    setGravity(2000)
    Unknown22004(5, 5)
    sprite('ad020_05', 4)	# 103-106
    sprite('ad020_06', 4)	# 107-110
    label(2)
    sprite('ad020_07', 4)	# 111-114
    sprite('ad020_08', 4)	# 115-118
    gotoLabel(2)

@State
def UltimateThrow():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown13024(0)

        def upon_43():
            if (SLOT_48 == 4018):
                Unknown23022(1)
                loopRelated(17, 310)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(10)
                sendToLabel(1)
            if (SLOT_48 == 4019):
                Unknown13024(1)
    sprite('ad433_00', 3)	# 1-3
    setInvincible(1)
    sprite('ad433_01', 6)	# 4-9
    if SLOT_43:
        SFX_1('ad320')
    else:
        SFX_1('ad319')
    sprite('ad433_02', 6)	# 10-15
    Unknown30080('')
    Unknown2036(45, -1, 0)
    ConsumeSuperMeter(-10000)
    sprite('ad433_03', 5)	# 16-20
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(61200)
    physicsYImpulse(-1800)
    Unknown35()
    sprite('ad433_04', 5)	# 21-25
    sprite('ad433_05', 5)	# 26-30
    sprite('ad433_03', 5)	# 31-35
    sprite('ad433_04', 5)	# 36-40
    sprite('ad433_06', 2)	# 41-42
    Unknown23029(11, 4004, 0)
    sprite('ad433_07', 3)	# 43-45
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_0('persona_destroy')
    sprite('ad433_08', 5)	# 46-50
    sprite('ad433_09', 5)	# 51-55
    sprite('ad433_10', 5)	# 56-60
    sprite('ad433_08', 5)	# 61-65
    setInvincible(0)
    sprite('ad433_09', 5)	# 66-70
    sprite('ad433_10', 5)	# 71-75
    sprite('ad433_08', 5)	# 76-80
    sprite('ad433_09', 5)	# 81-85
    sprite('ad433_10', 5)	# 86-90
    sprite('ad433_08', 5)	# 91-95
    sprite('ad433_09', 5)	# 96-100
    sprite('ad433_01', 5)	# 101-105
    sprite('ad433_00', 5)	# 106-110
    ExitState()
    label(1)
    sprite('ad433_07', 15)	# 111-125
    sprite('ad433_11', 6)	# 126-131
    label(2)
    sprite('ad433_12', 7)	# 132-138
    sprite('ad433_13', 7)	# 139-145
    sprite('ad433_14', 7)	# 146-152
    loopRest()
    gotoLabel(2)
    label(10)
    sprite('ad433_01', 7)	# 153-159
    sprite('ad433_00', 7)	# 160-166

@State
def UltimateBlade():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
        Unknown36(28)
        Unknown23148('PAD_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4012):
                loopRelated(17, 230)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(3)
                Unknown13024(0)
                sendToLabel(1)
            if (SLOT_48 == 4013):
                Unknown13024(1)
            if (SLOT_48 == 4014):
                setInvincible(0)
    sprite('ad433_00', 3)	# 1-3
    sprite('ad433_01', 3)	# 4-6
    tag_voice(1, 'pad254_0', 'pad254_1', '', '')
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ad433_02', 4)	# 7-10
    sprite('ad433_03', 6)	# 11-16
    Unknown30080('')
    Unknown2036(70, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(61200)
    physicsYImpulse(-900)
    Unknown35()
    sprite('ad433_04', 6)	# 17-22
    sprite('ad433_05', 6)	# 23-28
    sprite('ad433_03', 6)	# 29-34
    sprite('ad433_04', 6)	# 35-40
    sprite('ad433_05', 6)	# 41-46
    sprite('ad433_03', 6)	# 47-52
    sprite('ad433_04', 6)	# 53-58
    sprite('ad433_05', 6)	# 59-64
    sprite('ad433_06', 3)	# 65-67
    Unknown23029(11, 4002, 0)
    sprite('ad433_07', 3)	# 68-70
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('ad433_08', 6)	# 71-76
    sprite('ad433_09', 6)	# 77-82
    sprite('ad433_10', 6)	# 83-88
    sprite('ad433_08', 5)	# 89-93
    sprite('ad433_09', 5)	# 94-98
    sprite('ad433_10', 5)	# 99-103
    setInvincible(0)
    sprite('ad433_08', 5)	# 104-108
    sprite('ad433_09', 5)	# 109-113
    sprite('ad433_10', 5)	# 114-118
    sprite('ad433_08', 5)	# 119-123
    sprite('ad433_09', 5)	# 124-128
    sprite('ad433_10', 5)	# 129-133
    sprite('ad433_01', 5)	# 134-138
    sprite('ad433_00', 5)	# 139-143
    ExitState()
    label(1)
    sprite('ad433_09', 5)	# 144-148
    sprite('ad433_10', 5)	# 149-153
    sprite('ad433_01', 5)	# 154-158
    sprite('ad432_04', 5)	# 159-163
    sprite('ad432_05', 5)	# 164-168
    sprite('ad432_06', 5)	# 169-173
    sprite('ad432_07', 6)	# 174-179
    tag_voice(0, 'pad255_0', 'pad255_1', '', '')
    label(2)
    sprite('ad432_08', 6)	# 180-185
    sprite('ad432_09', 6)	# 186-191
    sprite('ad432_10', 6)	# 192-197
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ad432_11', 6)	# 198-203
    sprite('ad432_12', 6)	# 204-209

@State
def UltimateBladeSP():

    def upon_IMMEDIATE():
        AttackDefaults_StandingDD()
        Unknown23055('')
        Unknown1084(1)
        Unknown36(28)
        Unknown23148('PAD_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()
        setInvincible(1)

        def upon_43():
            if (SLOT_48 == 4015):
                loopRelated(17, 282)

                def upon_17():
                    clearUponHandler(17)
                    sendToLabel(3)
                Unknown13024(0)
                sendToLabel(1)
            if (SLOT_48 == 4016):
                Unknown13024(1)
            if (SLOT_48 == 4017):
                setInvincible(0)
    sprite('ad433_00', 3)	# 1-3
    sprite('ad433_01', 3)	# 4-6
    tag_voice(1, 'pad254_0', 'pad254_1', '', '')
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ad433_02', 4)	# 7-10
    sprite('ad433_03', 6)	# 11-16
    Unknown30080('')
    Unknown2036(70, -1, 0)
    ConsumeSuperMeter(-10000)
    Unknown4004('436172640000000000000000000000000000000000000000000000000000000000000000')
    Unknown38(4, 1)
    Unknown36(1)
    Unknown1007(61200)
    physicsYImpulse(-900)
    Unknown35()
    sprite('ad433_04', 6)	# 17-22
    sprite('ad433_05', 6)	# 23-28
    sprite('ad433_03', 6)	# 29-34
    sprite('ad433_04', 6)	# 35-40
    sprite('ad433_05', 6)	# 41-46
    sprite('ad433_03', 6)	# 47-52
    sprite('ad433_04', 6)	# 53-58
    sprite('ad433_05', 6)	# 59-64
    sprite('ad433_06', 3)	# 65-67
    Unknown23029(11, 4003, 0)
    sprite('ad433_07', 3)	# 68-70
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    sprite('ad433_08', 6)	# 71-76
    sprite('ad433_09', 6)	# 77-82
    sprite('ad433_10', 6)	# 83-88
    sprite('ad433_08', 5)	# 89-93
    sprite('ad433_09', 5)	# 94-98
    sprite('ad433_10', 5)	# 99-103
    setInvincible(0)
    sprite('ad433_08', 5)	# 104-108
    sprite('ad433_09', 5)	# 109-113
    sprite('ad433_10', 5)	# 114-118
    sprite('ad433_08', 5)	# 119-123
    sprite('ad433_09', 5)	# 124-128
    sprite('ad433_10', 5)	# 129-133
    sprite('ad433_01', 5)	# 134-138
    sprite('ad433_00', 5)	# 139-143
    ExitState()
    label(1)
    sprite('ad433_01', 5)	# 144-148
    sprite('ad433_00', 5)	# 149-153
    sprite('ad000_00', 5)	# 154-158
    sprite('ad610_00', 6)	# 159-164
    sprite('ad610_01', 6)	# 165-170
    sprite('ad610_02', 6)	# 171-176
    Unknown4004('4361726400000000000000000000000000000000000000000000000000000000ffff0000')
    Unknown38(4, 1)
    Unknown36(1)
    teleportRelativeX(50000)
    Unknown1007(350000)
    physicsYImpulse(-900)
    Unknown35()
    sprite('ad610_03', 6)	# 177-182
    sprite('ad610_04', 6)	# 183-188
    tag_voice(0, 'pad255_0', 'pad255_1', '', '')
    sprite('ad610_05', 6)	# 189-194
    sprite('ad610_06', 6)	# 195-200
    Unknown13(4)
    GFX_1('persona_enter_ply', 0)
    SFX_3('persona_destroy')
    Unknown2036(60, -1, 0)
    label(2)
    sprite('ad610_07', 6)	# 201-206
    sprite('ad610_08', 6)	# 207-212
    sprite('ad610_09', 6)	# 213-218
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('ad610_02', 4)	# 219-222
    sprite('ad610_01', 4)	# 223-226
    sprite('ad610_00', 4)	# 227-230

@State
def AstralHeat():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown36(28)
        Unknown23148('PAD_PersonaWait')
        Unknown48('030000000200000033000000190000000200000000000000')
        Unknown35()

        def upon_43():
            if (SLOT_48 == 4511):
                Unknown23022(1)
                if SLOT_31:
                    SLOT_31 = 0
                if Unknown46(5):
                    Unknown13(5)
                sendToLabel(1)
        Unknown2004(1, 0)
    sprite('ad450_00', 3)	# 1-3
    setInvincible(1)
    sprite('ad450_00', 3)	# 4-6
    GFX_0('P4U_Cutin_Parent', 100)
    Unknown2036(60, -1, 2)
    Unknown23147()
    if (not SLOT_51):
        Unknown23029(11, 9999, 0)
    sprite('ad450_01', 4)	# 7-10
    tag_voice(1, 'pad290_0', 'pad290_1', '', '')
    sprite('ad450_02', 4)	# 11-14
    sprite('ad450_03', 4)	# 15-18
    sprite('ad450_01', 4)	# 19-22
    sprite('ad450_02', 4)	# 23-26
    sprite('ad450_03', 4)	# 27-30
    sprite('ad450_04', 6)	# 31-36
    sprite('ad450_05', 6)	# 37-42
    sprite('ad450_06', 5)	# 43-47
    sprite('ad450_07', 5)	# 48-52
    sprite('ad450_08', 5)	# 53-57
    sprite('ad450_06', 5)	# 58-62
    GFX_0('mgef_450_yuka', 100)
    Unknown38(10, 1)
    sprite('ad450_07', 5)	# 63-67
    sprite('ad450_08', 5)	# 68-72
    sprite('ad450_06', 5)	# 73-77
    sprite('ad450_07', 5)	# 78-82
    sprite('ad450_08', 5)	# 83-87
    setInvincible(0)
    sprite('ad450_06', 5)	# 88-92
    sprite('ad450_07', 5)	# 93-97
    SFX_3('ad011')
    sprite('ad450_08', 5)	# 98-102
    SFX_3('blood_h')
    sprite('ad450_06', 5)	# 103-107
    sprite('ad450_07', 5)	# 108-112
    sprite('ad450_08', 5)	# 113-117
    Unknown21007(10, 32)
    sprite('ad450_09', 8)	# 118-125
    Unknown23024(0)
    sprite('ad450_10', 8)	# 126-133
    ExitState()
    label(1)
    sprite('keep', 3)	# 134-136
    enterState('AstralHeatExe')

@State
def AstralHeatExe():

    def upon_IMMEDIATE():
        AttackDefaults_Astral()
        Unknown23022(1)
        Unknown23084(1)
        Unknown23022(1)
        Unknown23157(0)
        Unknown23088(1, 1)

        def upon_43():
            if (SLOT_48 == 4505):
                sendToLabel(2)
            if (SLOT_48 == 4507):
                sendToLabel(10)
            if (SLOT_48 == 4521):
                Unknown23024(0)
    sprite('ad450_06', 5)	# 1-5
    Unknown23029(11, 4501, 0)
    tag_voice(0, 'pad291_0', 'pad291_1', '', '')
    sprite('ad450_07', 5)	# 6-10
    sprite('ad450_08', 5)	# 11-15
    sprite('ad450_06', 5)	# 16-20
    Unknown3032()
    Unknown3004(-8)
    sprite('ad450_07', 5)	# 21-25
    sprite('ad450_08', 5)	# 26-30
    sprite('ad450_06', 5)	# 31-35
    sprite('ad450_07', 5)	# 36-40
    sprite('ad450_08', 5)	# 41-45
    sprite('ad450_06', 5)	# 46-50
    sprite('ad450_07', 5)	# 51-55
    sprite('ad450_08', 5)	# 56-60
    sprite('null', 2000)	# 61-2060
    Unknown1000(100000)
    Unknown3004(0)
    label(2)
    sprite('ad610_00', 6)	# 2061-2066
    Unknown3001(255)
    sprite('ad610_01', 6)	# 2067-2072
    SFX_3('cloth_m')
    sprite('ad610_02', 6)	# 2073-2078
    sprite('ad610_03', 6)	# 2079-2084
    SFX_3('cloth_m')
    sprite('ad610_04', 6)	# 2085-2090
    sprite('ad610_05', 6)	# 2091-2096
    SFX_3('cloth_m')
    sprite('ad610_06', 6)	# 2097-2102
    tag_voice(0, 'pad294_0', 'pad294_1', '', '')
    sprite('ad610_07', 6)	# 2103-2108
    SFX_3('cloth_m')
    sprite('ad610_08', 6)	# 2109-2114
    sprite('ad610_09', 6)	# 2115-2120
    SFX_3('cloth_m')
    sprite('ad610_07', 6)	# 2121-2126
    sprite('ad610_08', 6)	# 2127-2132
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 2133-2138
    sprite('ad610_07', 6)	# 2139-2144
    sprite('ad610_08', 6)	# 2145-2150
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 2151-2156
    sprite('ad610_07', 6)	# 2157-2162
    SFX_3('cloth_m')
    Unknown3032()
    Unknown3004(-7)
    Unknown23130(16711680, 60, 1)
    Unknown23069(0)
    Unknown18010()
    sprite('ad610_08', 6)	# 2163-2168
    sprite('ad610_09', 6)	# 2169-2174
    SFX_3('cloth_m')
    sprite('ad610_07', 6)	# 2175-2180
    sprite('ad610_08', 6)	# 2181-2186
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 2187-2192
    label(3)
    sprite('ad610_07', 6)	# 2193-2198
    sprite('ad610_08', 6)	# 2199-2204
    sprite('ad610_09', 6)	# 2205-2210
    sprite('ad610_07', 6)	# 2211-2216
    sprite('ad610_08', 6)	# 2217-2222
    sprite('ad610_09', 6)	# 2223-2228
    Unknown18008()
    loopRest()
    gotoLabel(3)
    label(10)
    sprite('null', 32767)	# 2229-34995
    Unknown3032()
    Unknown3038(1)
    Unknown18008()

@Subroutine
def MouthTableInit():
    Unknown18011('pad000', 12643, 24882, 25401, 24889, 25400, 12337, 14177, 13923, 12641, 25394, 13364, 13921, 13923, 13921, 13923, 13921, 13923, 14689, 13923, 12641, 25401, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pad600def', 12899, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad600def', '001')
    Unknown18011('pad601def', 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601def', '002')
    Unknown18011('pad602def', 12643, 14689, 14691, 14433, 14435, 14433, 14435, 14433, 12899, 24880, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad602def', '003')
    Unknown18011('pad603def', 13155, 12897, 25398, 13105, 14433, 14179, 14433, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad603def', '004')
    Unknown18011('pad604def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad604def', '005')
    Unknown18011('pad605def', 12899, 12641, 25394, 12849, 12641, 25394, 12849, 14433, 14435, 14177, 14179, 14433, 14435, 14177, 14179, 12641, 25394, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad605def', '006')
    Unknown18011('pad700def', 12643, 24882, 25397, 24884, 25397, 13107, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 12849, 12897, 25392, 13361, 12897, 25392, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700def', '007')
    Unknown18011('pad701def', 12643, 12641, 25400, 24887, 25399, 12850, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701def', '008')
    Unknown18011('pad702def', 14177, 14179, 14177, 14179, 12641, 25392, 12337, 14177, 14179, 13921, 13923, 14433, 12899, 24880, 25398, 24888, 25400, 24888, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad702def', '009')
    Unknown18011('pad703def', 13155, 14433, 12643, 24889, 12337, 14435, 14433, 14435, 12641, 25400, 12337, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad703def', '010')
    Unknown18011('pad704def', 12899, 14177, 14179, 12641, 25397, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad704def', '011')
    Unknown18011('pad705def', 14177, 14179, 14177, 14179, 14177, 14179, 13921, 13923, 13921, 13923, 14689, 14691, 14177, 14179, 12641, 25396, 13361, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad705def', '012')
    Unknown18011('pad402_0', 12643, 24882, 25397, 24885, 25397, 12851, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 14179, 12897, 25394, 12593, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pad402_1', 12643, 12641, 25399, 14129, 13921, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25398, 13873, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pad403_0', 12899, 13921, 13411, 24882, 25401, 24889, 25401, 24889, 25401, 24889, 25401, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pad403_1', 12899, 13153, 25392, 13617, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25398, 13873, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pad600bjn', 12899, 14433, 14435, 14177, 12899, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 12643, 24880, 25399, 24887, 25399, 24887, 25400, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad600bjn', '017')
    Unknown18011('pad601btg', 13411, 12897, 25393, 24887, 25399, 12850, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12897, 25392, 14386, 14177, 12643, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601btg', '018')
    Unknown18011('pad600bha', 12899, 12897, 25392, 24889, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24887, 13873, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12849, 12643, 24882, 25399, 24887, 14385, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad600bha', '019')
    Unknown18011('pad601bhz', 12899, 14177, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 12899, 24881, 25398, 24886, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601bhz', '020')
    Unknown18011('pad601bjb', 12643, 13921, 13923, 13921, 13923, 13921, 13923, 13921, 14691, 12897, 25400, 13361, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25392, 24887, 12850, 12643, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601bjb', '021')
    Unknown18011('pad601pbc', 13411, 12641, 25400, 24889, 12849, 13667, 24885, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 13873, 12643, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601pbc', '022')
    Unknown18011('pad600pyu', 13155, 12641, 25395, 24887, 12337, 12643, 24880, 25401, 24889, 25401, 24889, 25401, 14130, 13921, 13923, 13921, 13923, 14433, 14435, 14433, 14435, 13921, 13923, 13921, 13923, 13921, 13923, 12641, 25400, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad600pyu', '023')
    Unknown18011('pad601pla', 12643, 12897, 25394, 13617, 12641, 25398, 12340, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12897, 25392, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601pla', '024')
    Unknown18011('pad600uhy', 12643, 14689, 14691, 14689, 14691, 14689, 14691, 12641, 25400, 24889, 25401, 12344, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25396, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad600uhy', '025')
    Unknown18011('pad601ugo', 12643, 24882, 25398, 24886, 25398, 24885, 25398, 24885, 13363, 13411, 24885, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 14385, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601ugo', '026')
    Unknown18011('pad601rrb', 13155, 13921, 13923, 13921, 13923, 13921, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 25394, 12849, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601rrb', '027')
    Unknown18011('pad603rrb', 12643, 24880, 14388, 13155, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad603rrb', '028')
    Unknown18011('pad601uhi', 14433, 14435, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 14177, 13667, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25400, 24888, 25400, 24888, 25400, 24888, 12594, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad601uhi', '029')
    Unknown18011('pad600bsu', 12643, 14177, 13155, 24880, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 12850, 14689, 13667, 14689, 13667, 14689, 14691, 12641, 25394, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad600bsu', '030')
    Unknown18011('pad701bjn', 13155, 12897, 25397, 12849, 12641, 25400, 13363, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 12641, 25398, 56, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701bjn', '031')
    Unknown18011('pad701btg', 14691, 13665, 13667, 13665, 13667, 13665, 12899, 24883, 12337, 12643, 24880, 25398, 12337, 12641, 25394, 13877, 13921, 12899, 24886, 25399, 24889, 25399, 24887, 25399, 24887, 25398, 24886, 25398, 24886, 25398, 24886, 25401, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701btg', '032')
    Unknown18011('pad701bha', 12899, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 13155, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 12849, 12641, 25398, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701bha', '033')
    Unknown18011('pad700bhz', 13411, 14433, 13155, 24882, 25398, 24886, 25398, 24886, 25398, 24886, 25398, 24888, 25400, 24888, 25400, 24888, 25400, 12851, 13921, 12643, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700bhz', '034')
    Unknown18011('pad701bjb', 12899, 14689, 14691, 14689, 14691, 13921, 13923, 13921, 13667, 24887, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 12338, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701bjb', '035')
    Unknown18011('pad701pbc', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 24884, 25398, 24885, 25398, 24885, 25398, 24886, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701pbc', '036')
    Unknown18011('pad700pyu', 12643, 12897, 25394, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 24888, 25400, 14390, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 14433, 14435, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700pyu', '037')
    Unknown18011('pad700pla', 13411, 12641, 25397, 24887, 14386, 12643, 24884, 14386, 12643, 24884, 25399, 24887, 25399, 24887, 25399, 24887, 12337, 12899, 24885, 25398, 13618, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 13665, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700pla', '038')
    Unknown18011('pad700uhy', 13155, 14433, 14435, 12641, 25398, 24888, 25400, 24888, 14385, 13411, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 13361, 14179, 14177, 14179, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700uhy', '039')
    Unknown18011('pad700ugo', 13921, 13923, 13921, 13923, 12641, 25397, 14642, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 24888, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 12594, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700ugo', '040')
    Unknown18011('pad701rrb', 13923, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 14691, 14689, 13155, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad701rrb', '041')
    Unknown18011('pad700uhi', 12643, 12641, 25396, 13362, 13153, 25396, 13619, 14689, 14691, 14177, 14179, 14689, 14691, 14689, 14691, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700uhi', '042')
    Unknown18011('pad700bsu', 12899, 13921, 13923, 13921, 13923, 12897, 25396, 14642, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 14433, 14435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad700bsu', '043')
    Unknown18011('pad294_0', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown18011('pad294_1', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    Unknown30092('pad294_0', '044')
    Unknown30092('pad294_1', '045')
    if SLOT_172:
        Unknown18011('pad000', 12643, 12643, 14177, 13411, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad600def', 12643, 12643, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 12899, 13155, 14177, 14179, 14177, 14179, 12641, 13667, 14177, 14179, 14177, 13923, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 24888, 25399, 24887, 25393, 24882, 25399, 25396, 24881, 25399, 24887, 25397, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25398, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad602def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad603def', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 13155, 24882, 25399, 24887, 25394, 24881, 25399, 25393, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25393, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad604def', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 14179, 14177, 14179, 14177, 14179, 13409, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad605def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 24887, 25399, 24887, 25399, 25397, 13873, 14177, 14179, 14177, 14179, 14177, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12899, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 14177, 14179, 14177, 14179, 13409, 12899, 14177, 13667, 12643, 12641, 12643, 24882, 25399, 24887, 25399, 25393, 24882, 25399, 24887, 25399, 24887, 25398, 12849, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701def', 12643, 12643, 14177, 14179, 14177, 14179, 13155, 14177, 14179, 12641, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad702def', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 13667, 14177, 14179, 13409, 13155, 14177, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad703def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13665, 12643, 24882, 25399, 24887, 25399, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad704def', 12643, 12643, 14177, 14179, 14177, 13923, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13667, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad705def', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 14177, 14179, 14177, 14179, 12897, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad402_0', 12643, 12643, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 13923, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad402_1', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 14179, 12641, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad403_0', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad403_1', 12643, 12643, 14177, 14179, 14177, 13155, 13411, 13409, 12643, 24889, 25399, 24887, 25399, 24887, 25397, 24881, 25399, 24887, 25399, 24887, 25399, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad600bjn', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 13155, 14177, 13411, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 12897, 12643, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 14177, 14179, 13409, 12643, 14177, 14179, 13921, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601btg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13155, 14177, 14179, 14177, 14179, 14177, 13667, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad600bha', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12899, 14177, 14179, 14177, 12643, 14177, 14179, 12641, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601bhz', 12643, 12643, 14177, 14179, 12897, 13411, 14177, 13923, 12899, 13665, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 13155, 14177, 14179, 12643, 14177, 14179, 14177, 12643, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601bjb', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12899, 24887, 25399, 24887, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 24881, 25399, 25395, 24881, 25396, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601pbc', 12643, 12643, 14177, 14179, 13153, 13923, 14177, 13155, 12643, 24883, 25399, 24887, 25399, 24887, 25399, 25398, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 24881, 25398, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad600pyu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 13667, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 13665, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601pla', 12643, 12643, 14177, 14179, 14177, 14179, 13921, 12899, 14177, 13923, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 14177, 14179, 13409, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad600uhy', 12643, 12643, 14177, 14179, 13155, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 12641, 14435, 14177, 14179, 12897, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13411, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601ugo', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12899, 24883, 25399, 24887, 25399, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25398, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601rrb', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25394, 25399, 49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad603rrb', 12643, 13923, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 25400, 25399, 25399, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad601uhi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13923, 14177, 14179, 13409, 12899, 13921, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad600bsu', 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13153, 12643, 14177, 14179, 14177, 13155, 13923, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701bjn', 12643, 12643, 14177, 13667, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701btg', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 12897, 13155, 14177, 14179, 14177, 14179, 13921, 12643, 14177, 14179, 12641, 13411, 14177, 14179, 14177, 14179, 14177, 13155, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701bha', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 12643, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700bhz', 12643, 14177, 14179, 14177, 12899, 12643, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25399, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701bjb', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 14691, 14177, 13155, 14691, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13667, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701pbc', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 13921, 12643, 24889, 25399, 24887, 25399, 24887, 25399, 24887, 25396, 24881, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 24887, 25399, 25394, 53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700pyu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13923, 12643, 14177, 14179, 14177, 14179, 12897, 12643, 14177, 14179, 13153, 13411, 14177, 13667, 12643, 14177, 14179, 14177, 12899, 12899, 14177, 13667, 12643, 14177, 14179, 14435, 13409, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700pla', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12897, 12643, 12897, 12899, 24882, 25399, 24887, 25399, 25393, 24884, 25399, 25399, 24882, 25399, 24887, 25398, 24881, 25399, 25396, 24882, 25399, 24887, 25399, 24887, 25399, 24887, 25395, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700uhy', 12643, 12643, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 13921, 13155, 14177, 14179, 14177, 12643, 14435, 12641, 12899, 24880, 25399, 24887, 25399, 24887, 25393, 24885, 25399, 24887, 25399, 24887, 25399, 25396, 24882, 25399, 24887, 25393, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700ugo', 12643, 13155, 14177, 14179, 14177, 13411, 12899, 14177, 14179, 14177, 12899, 13411, 14177, 14179, 14177, 14179, 14177, 14179, 12643, 14177, 14179, 14435, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad701rrb', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 13155, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 12641, 13411, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700uhi', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12643, 12643, 14177, 14179, 14177, 14179, 14177, 13411, 13155, 13665, 12643, 51, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad700bsu', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 12899, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 13409, 13155, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad294_0', 12643, 12899, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        Unknown18011('pad294_1', 12643, 12643, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 14177, 14179, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

@State
def CmnActEntry():
    label(0)
    sprite('null', 1)	# 1-1
    loopRest()
    if SLOT_17:
        _gotolabel(0)
    PartnerChar('bsu')
    if SLOT_ReturnVal:
        _gotolabel(100)
    PartnerChar('bjn')
    if SLOT_ReturnVal:
        _gotolabel(110)
    PartnerChar('btg')
    if SLOT_ReturnVal:
        _gotolabel(120)
    PartnerChar('bha')
    if SLOT_ReturnVal:
        _gotolabel(130)
    PartnerChar('bhz')
    if SLOT_ReturnVal:
        _gotolabel(140)
    PartnerChar('bjb')
    if SLOT_ReturnVal:
        _gotolabel(150)
    PartnerChar('pbc')
    if SLOT_ReturnVal:
        _gotolabel(160)
    PartnerChar('pyu')
    if SLOT_ReturnVal:
        _gotolabel(170)
    PartnerChar('pla')
    if SLOT_ReturnVal:
        _gotolabel(180)
    PartnerChar('uhy')
    if SLOT_ReturnVal:
        _gotolabel(190)
    PartnerChar('ugo')
    if SLOT_ReturnVal:
        _gotolabel(200)
    PartnerChar('uhi')
    if SLOT_ReturnVal:
        _gotolabel(210)
    PartnerChar('rrb')
    if SLOT_ReturnVal:
        _gotolabel(220)
    Unknown19(991, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(1)
    sprite('ad600_00', 10)	# 2-11
    sprite('ad600_00', 1)	# 12-12
    if SLOT_158:
        random_(2, 0, 40)
        if SLOT_ReturnVal:
            _gotolabel(2)
        Unknown7006('pad600def', 100, 912548208, 1701065008, 102, 0, 100, 912548208, 1701065264, 102, 0, 100, 912548208, 1701065520, 102, 0, 100)
        label(2)
        Unknown7006('pad604def', 100, 912548208, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    label(3)
    sprite('ad600_00', 1)	# 13-13
    if SLOT_97:
        _gotolabel(3)
    sprite('ad600_00', 10)	# 14-23
    sprite('ad600_01', 8)	# 24-31
    sprite('ad600_02', 8)	# 32-39
    sprite('ad600_03', 8)	# 40-47
    sprite('ad600_04', 8)	# 48-55
    sprite('ad600_05', 8)	# 56-63
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    sprite('ad600_06', 24)	# 64-87
    sprite('ad600_07', 6)	# 88-93
    Unknown23018(1)
    sprite('ad001_00', 6)	# 94-99
    ExitState()
    label(10)
    sprite('null', 6)	# 100-105
    Unknown2034(0)
    Unknown1000(-1860000)
    label(11)
    sprite('ad030_00', 6)	# 106-111
    physicsXImpulse(5000)
    GFX_0('adef_601aura', 100)
    if SLOT_158:
        Unknown7006('pad600def', 100, 912548208, 1701065008, 102, 0, 100, 912548208, 1701065264, 102, 0, 100, 912548208, 1701065520, 102, 0, 100)
    sprite('ad030_01', 6)	# 112-117
    sprite('ad030_02', 6)	# 118-123
    sprite('ad030_03', 6)	# 124-129
    SFX_3('walk_stone_light')
    sprite('ad030_04', 6)	# 130-135
    sprite('ad030_05', 6)	# 136-141
    sprite('ad030_06', 6)	# 142-147
    sprite('ad030_07', 6)	# 148-153
    sprite('ad030_08', 6)	# 154-159
    SFX_3('walk_stone_light')
    sprite('ad030_09', 6)	# 160-165
    sprite('ad030_10', 6)	# 166-171
    sprite('ad030_11', 6)	# 172-177
    sprite('ad030_02', 6)	# 178-183
    sprite('ad030_03', 6)	# 184-189
    SFX_3('walk_stone_light')
    sprite('ad030_04', 6)	# 190-195
    sprite('ad030_05', 6)	# 196-201
    sprite('ad030_06', 6)	# 202-207
    sprite('ad030_07', 6)	# 208-213
    sprite('ad030_08', 7)	# 214-220
    SFX_3('walk_stone_light')
    sprite('ad030_00', 6)	# 221-226
    Unknown1084(1)
    Unknown26('adef_601aura')
    sprite('ad001_00', 6)	# 227-232
    sprite('ad001_01', 6)	# 233-238
    sprite('ad601_00', 9)	# 239-247
    sprite('ad601_01', 8)	# 248-255
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 256-263
    sprite('ad601_03', 8)	# 264-271
    sprite('ad601_04', 8)	# 272-279
    sprite('ad601_01', 8)	# 280-287
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 288-295
    sprite('ad601_03', 8)	# 296-303
    sprite('ad601_04', 8)	# 304-311
    sprite('ad601_01', 8)	# 312-319
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 320-327
    sprite('ad601_03', 8)	# 328-335
    Unknown23018(1)
    sprite('ad601_04', 8)	# 336-343
    sprite('ad601_05', 6)	# 344-349
    sprite('ad001_00', 6)	# 350-355
    ExitState()
    label(100)
    sprite('ad001_00', 6)	# 356-361
    Unknown1000(-1465000)
    SFX_1('pad600bsu')
    sprite('ad001_01', 6)	# 362-367
    sprite('ad601_00', 9)	# 368-376
    sprite('ad601_01', 8)	# 377-384
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 385-392
    sprite('ad601_03', 8)	# 393-400
    sprite('ad601_04', 8)	# 401-408
    sprite('ad601_01', 8)	# 409-416
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 417-424
    sprite('ad601_03', 8)	# 425-432
    sprite('ad601_04', 8)	# 433-440
    sprite('ad601_01', 8)	# 441-448
    SFX_3('ad015')
    label(101)
    sprite('ad601_01', 1)	# 449-449
    if SLOT_97:
        _gotolabel(101)
    sprite('ad601_02', 6)	# 450-455
    sprite('ad601_03', 6)	# 456-461
    sprite('ad601_04', 6)	# 462-467
    sprite('ad601_05', 6)	# 468-473
    sprite('ad001_00', 6)	# 474-479
    sprite('ad000_00', 9)	# 480-488
    Unknown21007(24, 40)
    Unknown21011(120)
    label(102)
    sprite('ad000_01', 9)	# 489-497
    sprite('ad000_02', 9)	# 498-506
    sprite('ad000_03', 9)	# 507-515
    sprite('ad000_04', 9)	# 516-524
    sprite('ad000_05', 9)	# 525-533
    sprite('ad000_06', 9)	# 534-542
    sprite('ad000_07', 9)	# 543-551
    sprite('ad000_00', 9)	# 552-560
    gotoLabel(102)
    label(110)
    sprite('ad600_00', 8)	# 561-568
    SFX_1('pad600bjn')
    label(111)
    sprite('ad600_00', 1)	# 569-569
    if SLOT_97:
        _gotolabel(111)
    sprite('ad600_00', 15)	# 570-584
    sprite('ad600_01', 8)	# 585-592
    sprite('ad600_02', 8)	# 593-600
    sprite('ad600_03', 8)	# 601-608
    sprite('ad600_04', 8)	# 609-616
    sprite('ad600_05', 8)	# 617-624
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    sprite('ad600_06', 24)	# 625-648
    sprite('ad600_07', 6)	# 649-654
    sprite('ad001_00', 6)	# 655-660
    Unknown21007(24, 40)
    Unknown21011(120)
    label(112)
    sprite('ad000_00', 9)	# 661-669
    sprite('ad000_01', 9)	# 670-678
    sprite('ad000_02', 9)	# 679-687
    sprite('ad000_03', 9)	# 688-696
    sprite('ad000_04', 9)	# 697-705
    sprite('ad000_05', 9)	# 706-714
    sprite('ad000_06', 9)	# 715-723
    sprite('ad000_07', 9)	# 724-732
    gotoLabel(112)
    label(120)
    sprite('ad600_00', 32767)	# 733-33499

    def upon_40():
        clearUponHandler(40)
        SFX_1('pad601btg')
        sendToLabel(121)
    label(121)
    sprite('ad600_00', 15)	# 33500-33514
    sprite('ad600_01', 8)	# 33515-33522
    sprite('ad600_02', 8)	# 33523-33530
    sprite('ad600_03', 8)	# 33531-33538
    sprite('ad600_04', 8)	# 33539-33546
    sprite('ad600_05', 8)	# 33547-33554
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    sprite('ad600_06', 24)	# 33555-33578
    label(122)
    sprite('ad600_06', 1)	# 33579-33579
    if SLOT_97:
        _gotolabel(122)
    sprite('ad600_07', 6)	# 33580-33585
    sprite('ad001_00', 6)	# 33586-33591
    Unknown23018(1)
    label(123)
    sprite('ad000_00', 9)	# 33592-33600
    sprite('ad000_01', 9)	# 33601-33609
    sprite('ad000_02', 9)	# 33610-33618
    sprite('ad000_03', 9)	# 33619-33627
    sprite('ad000_04', 9)	# 33628-33636
    sprite('ad000_05', 9)	# 33637-33645
    sprite('ad000_06', 9)	# 33646-33654
    sprite('ad000_07', 9)	# 33655-33663
    gotoLabel(123)
    label(130)
    sprite('ad600_00', 10)	# 33664-33673
    sprite('ad600_00', 5)	# 33674-33678
    SFX_1('pad600bha')
    sprite('ad600_01', 8)	# 33679-33686
    sprite('ad600_02', 8)	# 33687-33694
    sprite('ad600_03', 8)	# 33695-33702
    sprite('ad600_04', 8)	# 33703-33710
    sprite('ad600_05', 8)	# 33711-33718
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    sprite('ad600_06', 24)	# 33719-33742
    label(132)
    sprite('ad600_06', 1)	# 33743-33743
    if SLOT_97:
        _gotolabel(132)
    sprite('ad600_07', 6)	# 33744-33749
    sprite('ad001_00', 6)	# 33750-33755
    Unknown21007(24, 40)
    Unknown21011(120)
    label(133)
    sprite('ad000_00', 9)	# 33756-33764
    sprite('ad000_01', 9)	# 33765-33773
    sprite('ad000_02', 9)	# 33774-33782
    sprite('ad000_03', 9)	# 33783-33791
    sprite('ad000_04', 9)	# 33792-33800
    sprite('ad000_05', 9)	# 33801-33809
    sprite('ad000_06', 9)	# 33810-33818
    sprite('ad000_07', 9)	# 33819-33827
    gotoLabel(133)
    label(140)
    sprite('ad600_00', 32767)	# 33828-66594

    def upon_40():
        clearUponHandler(40)
        SFX_1('pad601bhz')
        sendToLabel(141)
    label(141)
    sprite('ad600_00', 1)	# 66595-66595
    if SLOT_97:
        _gotolabel(141)
    sprite('ad600_01', 8)	# 66596-66603
    sprite('ad600_02', 8)	# 66604-66611
    sprite('ad600_03', 8)	# 66612-66619
    sprite('ad600_04', 8)	# 66620-66627
    sprite('ad600_05', 8)	# 66628-66635
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    sprite('ad600_06', 24)	# 66636-66659
    sprite('ad600_07', 6)	# 66660-66665
    sprite('ad001_00', 6)	# 66666-66671
    Unknown23018(1)
    label(142)
    sprite('ad000_00', 9)	# 66672-66680
    sprite('ad000_01', 9)	# 66681-66689
    sprite('ad000_02', 9)	# 66690-66698
    sprite('ad000_03', 9)	# 66699-66707
    sprite('ad000_04', 9)	# 66708-66716
    sprite('ad000_05', 9)	# 66717-66725
    sprite('ad000_06', 9)	# 66726-66734
    sprite('ad000_07', 9)	# 66735-66743
    gotoLabel(142)
    label(150)
    sprite('ad000_00', 9)	# 66744-66752

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ad000_01', 9)	# 66753-66761
    sprite('ad000_02', 9)	# 66762-66770
    sprite('ad000_03', 9)	# 66771-66779
    sprite('ad000_04', 9)	# 66780-66788
    sprite('ad000_05', 9)	# 66789-66797
    sprite('ad000_06', 9)	# 66798-66806
    sprite('ad000_07', 9)	# 66807-66815
    sprite('ad000_00', 9)	# 66816-66824
    gotoLabel(151)
    label(152)
    sprite('ad001_00', 6)	# 66825-66830
    SFX_1('pad601bjb')
    sprite('ad001_01', 6)	# 66831-66836
    Unknown23018(1)
    label(153)
    sprite('ad001_02', 9)	# 66837-66845
    sprite('ad001_03', 9)	# 66846-66854
    sprite('ad001_04', 9)	# 66855-66863
    sprite('ad001_03', 9)	# 66864-66872
    gotoLabel(153)
    label(160)
    sprite('ad652_00', 8)	# 66873-66880
    Unknown1000(-1330000)
    Unknown2019(1000)

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ad652_01', 8)	# 66881-66888
    sprite('ad652_02', 8)	# 66889-66896
    sprite('ad652_00', 8)	# 66897-66904
    gotoLabel(161)
    label(162)
    sprite('ad652_03', 8)	# 66905-66912
    sprite('ad652_04', 8)	# 66913-66920
    SFX_1('pad601pbc')
    label(163)
    sprite('ad652_05', 8)	# 66921-66928
    sprite('ad652_06', 8)	# 66929-66936
    sprite('ad652_04', 8)	# 66937-66944
    if SLOT_97:
        _gotolabel(163)
    sprite('ad652_05', 8)	# 66945-66952
    sprite('ad652_06', 8)	# 66953-66960
    Unknown21011(30)
    label(164)
    sprite('ad652_04', 8)	# 66961-66968
    sprite('ad652_05', 8)	# 66969-66976
    sprite('ad652_06', 8)	# 66977-66984
    gotoLabel(164)
    label(170)
    sprite('ad600_00', 115)	# 66985-67099
    Unknown1000(-1465000)
    SFX_1('pad600pyu')
    sprite('ad600_01', 8)	# 67100-67107
    sprite('ad600_02', 8)	# 67108-67115
    sprite('ad600_03', 8)	# 67116-67123
    sprite('ad600_04', 8)	# 67124-67131
    sprite('ad600_05', 8)	# 67132-67139
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    label(171)
    sprite('ad600_06', 1)	# 67140-67140
    if SLOT_97:
        _gotolabel(171)
    sprite('ad600_06', 10)	# 67141-67150
    sprite('ad600_07', 6)	# 67151-67156
    sprite('ad001_00', 6)	# 67157-67162
    Unknown21007(24, 40)
    Unknown21011(120)
    label(172)
    sprite('ad000_00', 9)	# 67163-67171
    sprite('ad000_01', 9)	# 67172-67180
    sprite('ad000_02', 9)	# 67181-67189
    sprite('ad000_03', 9)	# 67190-67198
    sprite('ad000_04', 9)	# 67199-67207
    sprite('ad000_05', 9)	# 67208-67216
    sprite('ad000_06', 9)	# 67217-67225
    sprite('ad000_07', 9)	# 67226-67234
    gotoLabel(172)
    label(180)
    sprite('ad000_00', 9)	# 67235-67243

    def upon_40():
        clearUponHandler(40)
        sendToLabel(182)
    label(181)
    sprite('ad000_01', 9)	# 67244-67252
    sprite('ad000_02', 9)	# 67253-67261
    sprite('ad000_03', 9)	# 67262-67270
    sprite('ad000_04', 9)	# 67271-67279
    sprite('ad000_05', 9)	# 67280-67288
    sprite('ad000_06', 9)	# 67289-67297
    sprite('ad000_07', 9)	# 67298-67306
    sprite('ad000_00', 9)	# 67307-67315
    gotoLabel(181)
    label(182)
    sprite('ad001_00', 6)	# 67316-67321
    SFX_1('pad601pla')
    sprite('ad001_01', 6)	# 67322-67327
    Unknown23018(1)
    label(183)
    sprite('ad001_02', 9)	# 67328-67336
    sprite('ad001_03', 9)	# 67337-67345
    sprite('ad001_04', 9)	# 67346-67354
    sprite('ad001_03', 9)	# 67355-67363
    gotoLabel(183)
    label(190)
    sprite('ad001_00', 6)	# 67364-67369
    Unknown1000(-1460000)
    sprite('ad001_01', 6)	# 67370-67375
    sprite('ad601_00', 9)	# 67376-67384
    SFX_1('pad600uhy')
    sprite('ad601_01', 8)	# 67385-67392
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 67393-67400
    sprite('ad601_03', 8)	# 67401-67408
    sprite('ad601_04', 8)	# 67409-67416
    sprite('ad601_01', 8)	# 67417-67424
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 67425-67432
    sprite('ad601_03', 8)	# 67433-67440
    sprite('ad601_04', 8)	# 67441-67448
    sprite('ad601_01', 8)	# 67449-67456
    SFX_3('ad015')
    label(191)
    sprite('ad601_01', 1)	# 67457-67457
    if SLOT_97:
        _gotolabel(191)
    sprite('ad601_02', 6)	# 67458-67463
    sprite('ad601_03', 6)	# 67464-67469
    sprite('ad601_04', 6)	# 67470-67475
    sprite('ad601_05', 6)	# 67476-67481
    sprite('ad001_00', 6)	# 67482-67487
    sprite('ad000_00', 9)	# 67488-67496
    Unknown21007(24, 40)
    Unknown21011(120)
    label(192)
    sprite('ad000_01', 9)	# 67497-67505
    sprite('ad000_02', 9)	# 67506-67514
    sprite('ad000_03', 9)	# 67515-67523
    sprite('ad000_04', 9)	# 67524-67532
    sprite('ad000_05', 9)	# 67533-67541
    sprite('ad000_06', 9)	# 67542-67550
    sprite('ad000_07', 9)	# 67551-67559
    sprite('ad000_00', 9)	# 67560-67568
    gotoLabel(192)
    label(200)
    sprite('ad000_00', 9)	# 67569-67577

    def upon_40():
        clearUponHandler(40)
        sendToLabel(202)
    label(201)
    sprite('ad000_01', 9)	# 67578-67586
    sprite('ad000_02', 9)	# 67587-67595
    sprite('ad000_03', 9)	# 67596-67604
    sprite('ad000_04', 9)	# 67605-67613
    sprite('ad000_05', 9)	# 67614-67622
    sprite('ad000_06', 9)	# 67623-67631
    sprite('ad000_07', 9)	# 67632-67640
    sprite('ad000_00', 9)	# 67641-67649
    gotoLabel(201)
    label(202)
    sprite('ad001_00', 6)	# 67650-67655
    sprite('ad001_01', 6)	# 67656-67661
    sprite('ad601_00', 9)	# 67662-67670
    SFX_1('pad601ugo')
    sprite('ad601_01', 8)	# 67671-67678
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 67679-67686
    sprite('ad601_03', 8)	# 67687-67694
    sprite('ad601_04', 8)	# 67695-67702
    sprite('ad601_01', 8)	# 67703-67710
    SFX_3('ad015')
    sprite('ad601_02', 8)	# 67711-67718
    sprite('ad601_03', 8)	# 67719-67726
    sprite('ad601_04', 8)	# 67727-67734
    sprite('ad601_01', 8)	# 67735-67742
    SFX_3('ad015')
    label(203)
    sprite('ad601_01', 1)	# 67743-67743
    if SLOT_97:
        _gotolabel(203)
    sprite('ad601_02', 6)	# 67744-67749
    sprite('ad601_03', 6)	# 67750-67755
    sprite('ad601_04', 6)	# 67756-67761
    sprite('ad601_05', 6)	# 67762-67767
    sprite('ad001_00', 6)	# 67768-67773
    Unknown23018(1)
    label(204)
    sprite('ad000_00', 9)	# 67774-67782
    sprite('ad000_01', 9)	# 67783-67791
    sprite('ad000_02', 9)	# 67792-67800
    sprite('ad000_03', 9)	# 67801-67809
    sprite('ad000_04', 9)	# 67810-67818
    sprite('ad000_05', 9)	# 67819-67827
    sprite('ad000_06', 9)	# 67828-67836
    sprite('ad000_07', 9)	# 67837-67845
    gotoLabel(204)
    label(210)
    sprite('ad600_00', 32767)	# 67846-100612

    def upon_40():
        clearUponHandler(40)
        SFX_1('pad601uhi')
        sendToLabel(211)
    label(211)
    sprite('ad600_00', 128)	# 100613-100740
    sprite('ad600_01', 8)	# 100741-100748
    sprite('ad600_02', 8)	# 100749-100756
    sprite('ad600_03', 8)	# 100757-100764
    sprite('ad600_04', 8)	# 100765-100772
    sprite('ad600_05', 8)	# 100773-100780
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    label(212)
    sprite('ad600_06', 24)	# 100781-100804
    if SLOT_97:
        _gotolabel(212)
    sprite('ad600_07', 6)	# 100805-100810
    sprite('ad001_00', 6)	# 100811-100816
    Unknown23018(1)
    label(213)
    sprite('ad000_00', 9)	# 100817-100825
    sprite('ad000_01', 9)	# 100826-100834
    sprite('ad000_02', 9)	# 100835-100843
    sprite('ad000_03', 9)	# 100844-100852
    sprite('ad000_04', 9)	# 100853-100861
    sprite('ad000_05', 9)	# 100862-100870
    sprite('ad000_06', 9)	# 100871-100879
    sprite('ad000_07', 9)	# 100880-100888
    gotoLabel(213)
    label(220)
    sprite('ad600_00', 32767)	# 100889-133655

    def upon_40():
        clearUponHandler(40)
        SFX_1('pad601rrb')
        sendToLabel(221)
    label(221)
    sprite('ad600_00', 8)	# 133656-133663

    def upon_40():
        clearUponHandler(40)
        sendToLabel(224)
    sprite('ad600_01', 8)	# 133664-133671
    sprite('ad600_02', 8)	# 133672-133679
    sprite('ad600_03', 8)	# 133680-133687
    sprite('ad600_04', 8)	# 133688-133695
    sprite('ad600_05', 8)	# 133696-133703
    GFX_0('ad600_Cort', 100)
    SFX_3('cloth_m')
    label(222)
    sprite('ad600_06', 1)	# 133704-133704
    if SLOT_97:
        _gotolabel(222)
    sprite('ad600_06', 14)	# 133705-133718
    sprite('ad600_07', 6)	# 133719-133724
    sprite('ad001_00', 6)	# 133725-133730
    Unknown21007(24, 40)
    label(223)
    sprite('ad000_00', 9)	# 133731-133739
    sprite('ad000_01', 9)	# 133740-133748
    sprite('ad000_02', 9)	# 133749-133757
    sprite('ad000_03', 9)	# 133758-133766
    sprite('ad000_04', 9)	# 133767-133775
    sprite('ad000_05', 9)	# 133776-133784
    sprite('ad000_06', 9)	# 133785-133793
    sprite('ad000_07', 9)	# 133794-133802
    gotoLabel(223)
    label(224)
    sprite('ad611_00', 7)	# 133803-133809
    SFX_1('pad603rrb')
    sprite('ad611_01', 7)	# 133810-133816
    sprite('ad611_02', 7)	# 133817-133823
    sprite('ad611_03', 7)	# 133824-133830
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 133831-133837
    sprite('ad611_05', 7)	# 133838-133844
    sprite('ad611_01', 7)	# 133845-133851
    sprite('ad611_02', 7)	# 133852-133858
    sprite('ad611_03', 7)	# 133859-133865
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 133866-133872
    sprite('ad611_05', 7)	# 133873-133879
    sprite('ad611_01', 7)	# 133880-133886
    sprite('ad611_02', 7)	# 133887-133893
    sprite('ad611_03', 7)	# 133894-133900
    SFX_3('ad015')
    sprite('ad611_06', 9)	# 133901-133909
    sprite('ad611_07', 9)	# 133910-133918
    sprite('ad611_08', 8)	# 133919-133926
    Unknown23018(1)
    label(225)
    sprite('ad611_09', 8)	# 133927-133934
    sprite('ad611_10', 8)	# 133935-133942
    sprite('ad611_11', 8)	# 133943-133950
    gotoLabel(225)
    label(991)
    sprite('ad000_00', 1)	# 133951-133951
    Unknown2019(1000)
    Unknown21011(120)
    label(992)
    sprite('ad000_00', 9)	# 133952-133960
    sprite('ad000_01', 9)	# 133961-133969
    sprite('ad000_02', 9)	# 133970-133978
    sprite('ad000_03', 9)	# 133979-133987
    sprite('ad000_04', 9)	# 133988-133996
    sprite('ad000_05', 9)	# 133997-134005
    sprite('ad000_06', 9)	# 134006-134014
    sprite('ad000_07', 9)	# 134015-134023
    loopRest()
    gotoLabel(992)

@State
def CmnActRoundWin():
    sprite('keep', 32767)	# 1-32767

@State
def CmnActMatchWin():
    if SLOT_169:
        _gotolabel(482)
    sprite('keep', 2)	# 1-2

    def upon_CLEAR_OR_EXIT():
        SLOT_58 = 1
        Unknown48('19000000020000003400000018000000020000003a000000')
        if SLOT_52:
            if PartnerChar('bsu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(100)
                    clearUponHandler(3)
            if PartnerChar('bjn'):
                if (SLOT_145 <= 500000):
                    sendToLabel(110)
                    clearUponHandler(3)
            if PartnerChar('btg'):
                if (SLOT_145 <= 500000):
                    sendToLabel(120)
                    clearUponHandler(3)
            if PartnerChar('bha'):
                if (SLOT_145 <= 500000):
                    sendToLabel(130)
                    clearUponHandler(3)
            if PartnerChar('bhz'):
                if (SLOT_145 <= 500000):
                    sendToLabel(140)
                    clearUponHandler(3)
            if PartnerChar('bjb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(150)
                    clearUponHandler(3)
            if PartnerChar('pbc'):
                if (SLOT_145 <= 500000):
                    sendToLabel(160)
                    clearUponHandler(3)
            if PartnerChar('pyu'):
                if (SLOT_145 <= 500000):
                    sendToLabel(170)
                    clearUponHandler(3)
            if PartnerChar('pla'):
                if (SLOT_145 <= 500000):
                    sendToLabel(180)
                    clearUponHandler(3)
            if PartnerChar('uhy'):
                if (SLOT_145 <= 500000):
                    sendToLabel(190)
                    clearUponHandler(3)
            if PartnerChar('ugo'):
                if (SLOT_145 <= 500000):
                    sendToLabel(200)
                    clearUponHandler(3)
            if PartnerChar('uhi'):
                if (SLOT_145 <= 500000):
                    sendToLabel(210)
                    clearUponHandler(3)
            if PartnerChar('rrb'):
                if (SLOT_145 <= 500000):
                    sendToLabel(220)
                    clearUponHandler(3)
    label(482)
    sprite('keep', 1)	# 3-3
    clearUponHandler(3)
    SLOT_58 = 0
    Unknown19(10, 2, 158)
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('ad610_00', 6)	# 4-9

    def upon_43():
        if (SLOT_48 == 10004):
            Unknown2037(1)
        if (SLOT_48 == 10003):
            sendToLabel(3)
    if SLOT_158:
        if SLOT_108:
            Unknown7006('pad402_0', 100, 878993776, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pad700def', 100, 929325424, 1701065008, 102, 0, 100, 929325424, 1701065264, 102, 0, 100, 929325424, 1701065520, 102, 0, 100)
    sprite('ad610_01', 6)	# 10-15
    sprite('ad610_02', 6)	# 16-21
    sprite('ad610_03', 6)	# 22-27
    SFX_3('cloth_m')
    sprite('ad610_04', 6)	# 28-33
    sprite('ad610_05', 6)	# 34-39
    sprite('ad610_06', 6)	# 40-45
    label(1)
    sprite('ad610_07', 6)	# 46-51
    SFX_3('cloth_m')
    sprite('ad610_08', 6)	# 52-57
    sprite('ad610_09', 6)	# 58-63
    sprite('ad610_07', 6)	# 64-69
    sprite('ad610_08', 6)	# 70-75
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 76-81
    if SLOT_97:
        _gotolabel(1)
    sprite('ad610_07', 6)	# 82-87
    Unknown23029(11, 10001, 0)
    sprite('ad610_08', 6)	# 88-93
    sprite('ad610_09', 6)	# 94-99
    SFX_3('cloth_m')
    sprite('ad610_07', 6)	# 100-105
    sprite('ad610_08', 6)	# 106-111
    sprite('ad610_09', 6)	# 112-117
    sprite('ad610_07', 6)	# 118-123
    SFX_0('cloth_m')
    sprite('ad610_08', 6)	# 124-129
    sprite('ad610_09', 6)	# 130-135
    sprite('ad610_07', 6)	# 136-141
    sprite('ad610_08', 6)	# 142-147
    SFX_0('cloth_m')
    sprite('ad610_09', 6)	# 148-153
    sprite('ad610_07', 6)	# 154-159
    sprite('ad610_08', 6)	# 160-165
    sprite('ad610_09', 6)	# 166-171
    SFX_0('cloth_m')
    sprite('ad610_07', 6)	# 172-177
    if (not SLOT_2):
        Unknown3032()
        Unknown3004(-7)
        Unknown23130(16711680, 60, 1)
        Unknown23069(0)
    Unknown23018(1)
    sprite('ad610_07', 6)	# 178-183
    sprite('ad610_08', 6)	# 184-189
    sprite('ad610_09', 6)	# 190-195
    label(2)
    sprite('ad610_07', 6)	# 196-201
    sprite('ad610_08', 6)	# 202-207
    sprite('ad610_09', 6)	# 208-213
    sprite('ad610_07', 6)	# 214-219
    sprite('ad610_08', 6)	# 220-225
    sprite('ad610_09', 6)	# 226-231
    loopRest()
    gotoLabel(2)
    label(3)
    sprite('null', 32767)	# 232-32998
    Unknown3032()
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    Unknown18008()
    loopRest()
    label(10)
    sprite('ad611_00', 7)	# 32999-33005
    if SLOT_158:
        if SLOT_52:
            Unknown7006('pad704def', 100, 929325424, 1701066032, 102, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        elif SLOT_108:
            Unknown7006('pad402_0', 100, 878993776, 828322352, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        else:
            Unknown7006('pad700def', 100, 929325424, 1701065008, 102, 0, 100, 929325424, 1701065264, 102, 0, 100, 929325424, 1701065520, 102, 0, 100)
    sprite('ad611_01', 7)	# 33006-33012
    sprite('ad611_02', 7)	# 33013-33019
    sprite('ad611_03', 7)	# 33020-33026
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33027-33033
    sprite('ad611_05', 7)	# 33034-33040
    sprite('ad611_01', 7)	# 33041-33047
    sprite('ad611_02', 7)	# 33048-33054
    sprite('ad611_03', 7)	# 33055-33061
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33062-33068
    sprite('ad611_05', 7)	# 33069-33075
    sprite('ad611_01', 7)	# 33076-33082
    sprite('ad611_02', 7)	# 33083-33089
    sprite('ad611_03', 7)	# 33090-33096
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33097-33103
    sprite('ad611_05', 7)	# 33104-33110
    sprite('ad611_01', 7)	# 33111-33117
    sprite('ad611_02', 7)	# 33118-33124
    sprite('ad611_03', 7)	# 33125-33131
    SFX_3('ad015')
    sprite('ad611_06', 9)	# 33132-33140
    sprite('ad611_07', 9)	# 33141-33149
    sprite('ad611_08', 8)	# 33150-33157
    Unknown23018(1)
    label(11)
    sprite('ad611_09', 8)	# 33158-33165
    sprite('ad611_10', 8)	# 33166-33173
    sprite('ad611_11', 8)	# 33174-33181
    gotoLabel(11)
    label(100)
    sprite('keep', 1)	# 33182-33182
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(103)
        elif (SLOT_38 == 1):
            sendToLabel(103)
    label(101)
    sprite('ad611_00', 7)	# 33183-33189
    SFX_1('pad700bsu')
    sprite('ad611_01', 7)	# 33190-33196
    sprite('ad611_02', 7)	# 33197-33203
    sprite('ad611_03', 7)	# 33204-33210
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33211-33217
    sprite('ad611_05', 7)	# 33218-33224
    sprite('ad611_01', 7)	# 33225-33231
    sprite('ad611_02', 7)	# 33232-33238
    sprite('ad611_03', 7)	# 33239-33245
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33246-33252
    sprite('ad611_05', 7)	# 33253-33259
    sprite('ad611_01', 7)	# 33260-33266
    sprite('ad611_02', 7)	# 33267-33273
    sprite('ad611_03', 7)	# 33274-33280
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33281-33287
    sprite('ad611_05', 7)	# 33288-33294
    sprite('ad611_01', 7)	# 33295-33301
    sprite('ad611_02', 7)	# 33302-33308
    sprite('ad611_03', 7)	# 33309-33315
    SFX_3('ad015')
    sprite('ad611_06', 9)	# 33316-33324
    sprite('ad611_07', 9)	# 33325-33333
    sprite('ad611_08', 8)	# 33334-33341
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            Unknown2038(-1)
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(200)
    label(102)
    sprite('ad611_09', 8)	# 33342-33349
    sprite('ad611_10', 8)	# 33350-33357
    sprite('ad611_11', 8)	# 33358-33365
    gotoLabel(102)
    label(103)
    sprite('ad003_00', 4)	# 33366-33369
    Unknown2005()
    sprite('ad003_01', 4)	# 33370-33373
    sprite('ad003_02', 4)	# 33374-33377
    gotoLabel(101)
    label(110)
    sprite('ad000_00', 9)	# 33378-33386

    def upon_40():
        clearUponHandler(40)
        sendToLabel(112)
    label(111)
    sprite('ad000_01', 9)	# 33387-33395
    sprite('ad000_02', 9)	# 33396-33404
    sprite('ad000_03', 9)	# 33405-33413
    sprite('ad000_04', 9)	# 33414-33422
    sprite('ad000_05', 9)	# 33423-33431
    sprite('ad000_06', 9)	# 33432-33440
    sprite('ad000_07', 9)	# 33441-33449
    sprite('ad000_00', 9)	# 33450-33458
    gotoLabel(111)
    label(112)
    sprite('ad611_00', 7)	# 33459-33465
    SFX_1('pad701bjn')
    sprite('ad611_06', 9)	# 33466-33474
    sprite('ad611_07', 9)	# 33475-33483
    sprite('ad611_08', 8)	# 33484-33491
    sprite('ad611_09', 8)	# 33492-33499
    sprite('ad611_10', 8)	# 33500-33507
    sprite('ad611_11', 8)	# 33508-33515
    Unknown23018(1)
    label(113)
    sprite('ad611_09', 8)	# 33516-33523
    sprite('ad611_10', 8)	# 33524-33531
    sprite('ad611_11', 8)	# 33532-33539
    gotoLabel(113)
    label(120)
    sprite('ad000_00', 9)	# 33540-33548

    def upon_40():
        clearUponHandler(40)
        sendToLabel(122)
    label(121)
    sprite('ad000_01', 9)	# 33549-33557
    sprite('ad000_02', 9)	# 33558-33566
    sprite('ad000_03', 9)	# 33567-33575
    sprite('ad000_04', 9)	# 33576-33584
    sprite('ad000_05', 9)	# 33585-33593
    sprite('ad000_06', 9)	# 33594-33602
    sprite('ad000_07', 9)	# 33603-33611
    sprite('ad000_00', 9)	# 33612-33620
    gotoLabel(121)
    label(122)
    sprite('ad611_00', 7)	# 33621-33627
    SFX_1('pad701btg')
    sprite('ad611_06', 9)	# 33628-33636
    sprite('ad611_07', 9)	# 33637-33645
    sprite('ad611_08', 8)	# 33646-33653
    sprite('ad611_09', 8)	# 33654-33661
    sprite('ad611_10', 8)	# 33662-33669
    sprite('ad611_11', 8)	# 33670-33677
    Unknown23018(1)
    label(123)
    sprite('ad611_09', 8)	# 33678-33685
    sprite('ad611_10', 8)	# 33686-33693
    sprite('ad611_11', 8)	# 33694-33701
    gotoLabel(123)
    label(130)
    sprite('ad000_00', 9)	# 33702-33710

    def upon_40():
        clearUponHandler(40)
        sendToLabel(132)
    label(131)
    sprite('ad000_01', 9)	# 33711-33719
    sprite('ad000_02', 9)	# 33720-33728
    sprite('ad000_03', 9)	# 33729-33737
    sprite('ad000_04', 9)	# 33738-33746
    sprite('ad000_05', 9)	# 33747-33755
    sprite('ad000_06', 9)	# 33756-33764
    sprite('ad000_07', 9)	# 33765-33773
    sprite('ad000_00', 9)	# 33774-33782
    gotoLabel(131)
    label(132)
    sprite('keep', 1)	# 33783-33783
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(135)
        elif (SLOT_38 == 1):
            sendToLabel(135)
    label(133)
    sprite('ad611_00', 7)	# 33784-33790
    SFX_1('pad701bha')
    Unknown23018(1)
    label(134)
    sprite('ad611_01', 7)	# 33791-33797
    sprite('ad611_02', 7)	# 33798-33804
    sprite('ad611_03', 7)	# 33805-33811
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 33812-33818
    sprite('ad611_05', 7)	# 33819-33825
    gotoLabel(134)
    label(135)
    sprite('ad003_00', 4)	# 33826-33829
    Unknown2005()
    sprite('ad003_01', 4)	# 33830-33833
    sprite('ad003_02', 4)	# 33834-33837
    gotoLabel(133)
    label(140)
    sprite('ad610_00', 6)	# 33838-33843
    SFX_1('pad700bhz')
    sprite('ad610_01', 6)	# 33844-33849
    sprite('ad610_02', 6)	# 33850-33855
    sprite('ad610_03', 6)	# 33856-33861
    SFX_3('cloth_m')
    sprite('ad610_04', 6)	# 33862-33867
    sprite('ad610_05', 6)	# 33868-33873
    sprite('ad610_06', 6)	# 33874-33879
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(150)
    label(141)
    sprite('ad610_07', 6)	# 33880-33885
    SFX_3('cloth_m')
    sprite('ad610_08', 6)	# 33886-33891
    sprite('ad610_09', 6)	# 33892-33897
    sprite('ad610_07', 6)	# 33898-33903
    sprite('ad610_08', 6)	# 33904-33909
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 33910-33915
    sprite('ad610_07', 6)	# 33916-33921
    sprite('ad610_08', 6)	# 33922-33927
    gotoLabel(141)
    label(150)
    sprite('ad000_00', 9)	# 33928-33936

    def upon_40():
        clearUponHandler(40)
        sendToLabel(152)
    label(151)
    sprite('ad000_01', 9)	# 33937-33945
    sprite('ad000_02', 9)	# 33946-33954
    sprite('ad000_03', 9)	# 33955-33963
    sprite('ad000_04', 9)	# 33964-33972
    sprite('ad000_05', 9)	# 33973-33981
    sprite('ad000_06', 9)	# 33982-33990
    sprite('ad000_07', 9)	# 33991-33999
    sprite('ad000_00', 9)	# 34000-34008
    gotoLabel(151)
    label(152)
    sprite('ad611_00', 7)	# 34009-34015
    SFX_1('pad701bjb')
    sprite('ad611_06', 9)	# 34016-34024
    sprite('ad611_07', 9)	# 34025-34033
    sprite('ad611_08', 8)	# 34034-34041
    sprite('ad611_09', 8)	# 34042-34049
    sprite('ad611_10', 8)	# 34050-34057
    sprite('ad611_11', 8)	# 34058-34065
    Unknown23018(1)
    label(153)
    sprite('ad611_09', 8)	# 34066-34073
    sprite('ad611_10', 8)	# 34074-34081
    sprite('ad611_11', 8)	# 34082-34089
    gotoLabel(153)
    label(160)
    sprite('ad000_00', 9)	# 34090-34098

    def upon_40():
        clearUponHandler(40)
        sendToLabel(162)
    label(161)
    sprite('ad000_01', 9)	# 34099-34107
    sprite('ad000_02', 9)	# 34108-34116
    sprite('ad000_03', 9)	# 34117-34125
    sprite('ad000_04', 9)	# 34126-34134
    sprite('ad000_05', 9)	# 34135-34143
    sprite('ad000_06', 9)	# 34144-34152
    sprite('ad000_07', 9)	# 34153-34161
    sprite('ad000_00', 9)	# 34162-34170
    gotoLabel(161)
    label(162)
    sprite('ad611_00', 7)	# 34171-34177
    SFX_1('pad701pbc')
    sprite('ad611_06', 9)	# 34178-34186
    sprite('ad611_07', 9)	# 34187-34195
    sprite('ad611_08', 8)	# 34196-34203
    sprite('ad611_09', 8)	# 34204-34211
    sprite('ad611_10', 8)	# 34212-34219
    sprite('ad611_11', 8)	# 34220-34227
    Unknown23018(1)
    label(163)
    sprite('ad611_09', 8)	# 34228-34235
    sprite('ad611_10', 8)	# 34236-34243
    sprite('ad611_11', 8)	# 34244-34251
    gotoLabel(163)
    label(170)
    sprite('ad001_00', 9)	# 34252-34260
    SFX_1('pad700pyu')
    sprite('ad001_01', 9)	# 34261-34269
    label(171)
    sprite('ad001_02', 9)	# 34270-34278
    sprite('ad001_03', 9)	# 34279-34287
    sprite('ad001_04', 9)	# 34288-34296
    sprite('ad001_03', 9)	# 34297-34305
    if SLOT_97:
        _gotolabel(171)
    sprite('ad001_02', 9)	# 34306-34314
    Unknown21007(24, 40)
    Unknown21011(180)
    label(172)
    sprite('ad001_03', 9)	# 34315-34323
    sprite('ad001_04', 9)	# 34324-34332
    sprite('ad001_03', 9)	# 34333-34341
    sprite('ad001_02', 9)	# 34342-34350
    gotoLabel(172)
    label(180)
    sprite('ad610_00', 6)	# 34351-34356

    def upon_43():
        clearUponHandler(43)
        sendToLabel(183)
    SFX_1('pad700pla')
    sprite('ad610_01', 6)	# 34357-34362
    sprite('ad610_02', 6)	# 34363-34368
    sprite('ad610_03', 6)	# 34369-34374
    SFX_3('cloth_m')
    sprite('ad610_04', 6)	# 34375-34380
    sprite('ad610_05', 6)	# 34381-34386
    sprite('ad610_06', 6)	# 34387-34392
    label(181)
    sprite('ad610_07', 6)	# 34393-34398
    SFX_3('cloth_m')
    sprite('ad610_08', 6)	# 34399-34404
    sprite('ad610_09', 6)	# 34405-34410
    sprite('ad610_07', 6)	# 34411-34416
    sprite('ad610_08', 6)	# 34417-34422
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 34423-34428
    if SLOT_97:
        _gotolabel(181)
    sprite('ad610_07', 6)	# 34429-34434
    Unknown23029(11, 10002, 0)
    sprite('ad610_08', 6)	# 34435-34440
    sprite('ad610_09', 6)	# 34441-34446
    SFX_3('cloth_m')
    sprite('ad610_07', 6)	# 34447-34452
    sprite('ad610_08', 6)	# 34453-34458
    sprite('ad610_09', 6)	# 34459-34464
    sprite('ad610_07', 6)	# 34465-34470
    SFX_0('cloth_m')
    sprite('ad610_08', 6)	# 34471-34476
    sprite('ad610_09', 6)	# 34477-34482
    sprite('ad610_07', 6)	# 34483-34488
    sprite('ad610_08', 6)	# 34489-34494
    SFX_0('cloth_m')
    sprite('ad610_09', 6)	# 34495-34500
    sprite('ad610_07', 6)	# 34501-34506
    sprite('ad610_08', 6)	# 34507-34512
    sprite('ad610_09', 6)	# 34513-34518
    SFX_0('cloth_m')
    sprite('ad610_07', 6)	# 34519-34524
    Unknown3032()
    Unknown3004(-7)
    Unknown23130(16711680, 60, 1)
    Unknown23069(0)
    sprite('ad610_08', 6)	# 34525-34530
    sprite('ad610_09', 6)	# 34531-34536
    sprite('ad610_07', 6)	# 34537-34542
    SFX_0('cloth_m')
    sprite('ad610_08', 6)	# 34543-34548
    sprite('ad610_09', 6)	# 34549-34554
    label(182)
    sprite('ad610_07', 6)	# 34555-34560
    sprite('ad610_08', 6)	# 34561-34566
    sprite('ad610_09', 6)	# 34567-34572
    sprite('ad610_07', 6)	# 34573-34578
    sprite('ad610_08', 6)	# 34579-34584
    sprite('ad610_09', 6)	# 34585-34590
    gotoLabel(182)
    label(183)
    sprite('null', 30)	# 34591-34620
    Unknown21007(24, 40)
    Unknown3032()
    Unknown3038(1)
    Unknown3001(0)
    Unknown3004(0)
    sprite('null', 32767)	# 34621-67387
    Unknown21011(140)
    label(190)
    sprite('keep', 1)	# 67388-67388
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(194)
        elif (SLOT_38 == 1):
            sendToLabel(194)
    label(191)
    sprite('ad611_00', 7)	# 67389-67395
    SFX_1('pad700uhy')
    label(192)
    sprite('ad611_01', 7)	# 67396-67402
    sprite('ad611_02', 7)	# 67403-67409
    sprite('ad611_03', 7)	# 67410-67416
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 67417-67423
    sprite('ad611_05', 7)	# 67424-67430
    if SLOT_97:
        _gotolabel(192)
    sprite('ad611_01', 7)	# 67431-67437
    Unknown21007(24, 40)
    Unknown21011(120)
    label(193)
    sprite('ad611_02', 7)	# 67438-67444
    sprite('ad611_03', 7)	# 67445-67451
    SFX_3('ad015')
    sprite('ad611_04', 7)	# 67452-67458
    sprite('ad611_05', 7)	# 67459-67465
    sprite('ad611_01', 7)	# 67466-67472
    gotoLabel(193)
    label(194)
    sprite('ad003_00', 4)	# 67473-67476
    Unknown2005()
    sprite('ad003_01', 4)	# 67477-67480
    sprite('ad003_02', 4)	# 67481-67484
    gotoLabel(191)
    label(200)
    sprite('keep', 1)	# 67485-67485
    if (SLOT_38 == SLOT_152):
        if (SLOT_22 >= SLOT_148):
            if (SLOT_38 == 0):
                sendToLabel(204)
        elif (SLOT_38 == 1):
            sendToLabel(204)
    label(201)
    sprite('ad611_00', 7)	# 67486-67492
    SFX_1('pad700ugo')
    sprite('ad611_06', 9)	# 67493-67501
    sprite('ad611_07', 9)	# 67502-67510
    sprite('ad611_08', 8)	# 67511-67518
    label(202)
    sprite('ad611_09', 8)	# 67519-67526
    sprite('ad611_10', 8)	# 67527-67534
    sprite('ad611_11', 8)	# 67535-67542
    if SLOT_97:
        _gotolabel(202)
    sprite('ad611_09', 8)	# 67543-67550
    Unknown21007(24, 40)
    Unknown21011(270)
    label(203)
    sprite('ad611_10', 8)	# 67551-67558
    sprite('ad611_11', 8)	# 67559-67566
    sprite('ad611_09', 8)	# 67567-67574
    gotoLabel(203)
    label(204)
    sprite('ad003_00', 4)	# 67575-67578
    Unknown2005()
    sprite('ad003_01', 4)	# 67579-67582
    sprite('ad003_02', 4)	# 67583-67586
    gotoLabel(201)
    label(210)
    sprite('ad611_00', 7)	# 67587-67593
    SFX_1('pad700uhi')
    sprite('ad611_06', 9)	# 67594-67602
    sprite('ad611_07', 9)	# 67603-67611
    sprite('ad611_08', 8)	# 67612-67619
    Unknown2037(30)

    def upon_CLEAR_OR_EXIT():
        if (not SLOT_97):
            SLOT_2 = (SLOT_2 + (-1))
            if (not SLOT_2):
                clearUponHandler(3)
                Unknown21007(24, 40)
                Unknown21011(240)
    label(211)
    sprite('ad611_09', 8)	# 67620-67627
    sprite('ad611_10', 8)	# 67628-67635
    sprite('ad611_11', 8)	# 67636-67643
    gotoLabel(211)
    label(220)
    sprite('ad000_00', 9)	# 67644-67652

    def upon_40():
        clearUponHandler(40)
        sendToLabel(222)
    label(221)
    sprite('ad000_01', 9)	# 67653-67661
    sprite('ad000_02', 9)	# 67662-67670
    sprite('ad000_03', 9)	# 67671-67679
    sprite('ad000_04', 9)	# 67680-67688
    sprite('ad000_05', 9)	# 67689-67697
    sprite('ad000_06', 9)	# 67698-67706
    sprite('ad000_07', 9)	# 67707-67715
    sprite('ad000_00', 9)	# 67716-67724
    gotoLabel(221)
    label(222)
    sprite('ad610_00', 6)	# 67725-67730
    SFX_1('pad701rrb')
    sprite('ad610_01', 6)	# 67731-67736
    SFX_3('cloth_m')
    sprite('ad610_02', 6)	# 67737-67742
    sprite('ad610_03', 6)	# 67743-67748
    sprite('ad610_04', 6)	# 67749-67754
    sprite('ad610_05', 6)	# 67755-67760
    SFX_3('cloth_m')
    sprite('ad610_06', 6)	# 67761-67766
    label(223)
    sprite('ad610_07', 6)	# 67767-67772
    sprite('ad610_08', 6)	# 67773-67778
    sprite('ad610_09', 6)	# 67779-67784
    SFX_3('cloth_m')
    sprite('ad610_07', 6)	# 67785-67790
    sprite('ad610_08', 6)	# 67791-67796
    sprite('ad610_09', 6)	# 67797-67802
    sprite('ad610_07', 6)	# 67803-67808
    SFX_3('cloth_m')
    sprite('ad610_08', 6)	# 67809-67814
    sprite('ad610_09', 6)	# 67815-67820
    sprite('ad610_07', 6)	# 67821-67826
    sprite('ad610_08', 6)	# 67827-67832
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 67833-67838
    if SLOT_97:
        _gotolabel(223)
    sprite('ad610_07', 6)	# 67839-67844
    Unknown23018(1)
    label(224)
    sprite('ad610_08', 6)	# 67845-67850
    sprite('ad610_09', 6)	# 67851-67856
    SFX_3('cloth_m')
    sprite('ad610_07', 6)	# 67857-67862
    sprite('ad610_08', 6)	# 67863-67868
    sprite('ad610_09', 6)	# 67869-67874
    sprite('ad610_07', 6)	# 67875-67880
    SFX_3('cloth_m')
    sprite('ad610_08', 6)	# 67881-67886
    sprite('ad610_09', 6)	# 67887-67892
    sprite('ad610_07', 6)	# 67893-67898
    sprite('ad610_08', 6)	# 67899-67904
    SFX_3('cloth_m')
    sprite('ad610_09', 6)	# 67905-67910
    sprite('ad610_07', 6)	# 67911-67916
    gotoLabel(224)

@State
def CmnActLose():
    random_(2, 0, 50)
    if SLOT_ReturnVal:
        _gotolabel(10)
    label(0)
    sprite('ad070_00', 6)	# 1-6
    if SLOT_158:
        SFX_1('pad403_0')
    sprite('ad070_01', 6)	# 7-12
    sprite('ad070_02', 2)	# 13-14
    sprite('ad070_03', 32767)	# 15-32781
    Unknown21011(60)
    label(10)
    sprite('ad001_00', 9)	# 32782-32790
    SFX_1('pad403_1')
    sprite('ad001_01', 9)	# 32791-32799
    sprite('ad001_02', 9)	# 32800-32808
    sprite('ad001_03', 12)	# 32809-32820
    sprite('ad001_04', 12)	# 32821-32832
    sprite('ad001_03', 12)	# 32833-32844
    sprite('ad001_02', 12)	# 32845-32856
    sprite('ad001_03', 12)	# 32857-32868
    sprite('ad001_04', 12)	# 32869-32880
    sprite('ad001_03', 12)	# 32881-32892
    sprite('ad001_02', 12)	# 32893-32904
    sprite('ad001_03', 12)	# 32905-32916
    sprite('ad001_04', 32767)	# 32917-65683
    Unknown21011(60)